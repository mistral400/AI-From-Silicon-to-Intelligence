#!/usr/bin/env python3
"""Build the current PDF preview from the ordered Markdown sources using Pandoc/XeLaTeX."""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "book" / "book-order.txt"
REFERENCE_ID = re.compile(r"(?<=\{#)ref-([A-Za-z0-9_:.+/-]+)(?=\})")
REFERENCE_LINK = re.compile(r"(?<=\]\(#)ref-([A-Za-z0-9_:.+/-]+)(?=\))")
MARKDOWN_LINK = re.compile(r"(?P<prefix>!?\[[^\]]*\]\(\s*)(?P<destination><[^>]*>|[^)\s]+)")


def read_sources() -> list[Path]:
    if not MANIFEST.is_file():
        raise FileNotFoundError(f"PDF source manifest not found: {MANIFEST.relative_to(ROOT)}")

    sources: list[Path] = []
    for line_number, raw_line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), start=1):
        entry = raw_line.strip()
        if not entry or entry.startswith("#"):
            continue
        relative = Path(entry)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"Unsafe path in {MANIFEST.name}:{line_number}: {entry}")
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f"Path escapes repository in {MANIFEST.name}:{line_number}: {entry}")
        if path.suffix.lower() != ".md":
            raise ValueError(f"Expected a Markdown source in {MANIFEST.name}:{line_number}: {entry}")
        if not path.is_file():
            raise FileNotFoundError(f"PDF source not found in {MANIFEST.name}:{line_number}: {entry}")
        sources.append(path)

    if not sources:
        raise ValueError(f"No Markdown sources listed in {MANIFEST.relative_to(ROOT)}")
    return sources


def add_chapter_anchor(markdown: str, chapter_anchor: str) -> str:
    """Give the chapter heading a stable target for links in the combined PDF."""
    lines = markdown.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if re.match(r"^#\s+", line):
            ending = "\n" if line.endswith("\n") else ""
            lines[index] = f"{line.rstrip()} {{#{chapter_anchor}}}{ending}"
            return "".join(lines)
    raise ValueError(f"Markdown source has no level-one chapter heading: {chapter_anchor}")


def rewrite_pdf_links(markdown: str, source: Path, chapter_anchors: dict[Path, str]) -> str:
    """Turn local Markdown chapter links into links within the combined PDF."""

    def replace(match: re.Match[str]) -> str:
        if match.group("prefix").startswith("!"):
            return match.group(0)
        destination = match.group("destination")
        wrapped = destination.startswith("<") and destination.endswith(">")
        raw_destination = destination[1:-1] if wrapped else destination
        parsed = urlsplit(raw_destination)
        if parsed.scheme or parsed.netloc or not parsed.path.lower().endswith(".md"):
            return match.group(0)
        raw_path = unquote(parsed.path)
        target = (ROOT / raw_path.lstrip("/\\")).resolve() if parsed.path.startswith("/") else (source.parent / raw_path).resolve()
        if target not in chapter_anchors:
            raise ValueError(f"PDF link target is not in the chapter manifest: {raw_destination!r}")
        anchor = chapter_anchors[target]
        if parsed.fragment:
            fragment = unquote(parsed.fragment)
            if not fragment.startswith("ref-"):
                raise ValueError(f"PDF cross-chapter link has an unsupported fragment: {raw_destination!r}")
            anchor = f"{anchor}-{fragment}"
        return f"{match.group('prefix')}#{anchor}"

    return MARKDOWN_LINK.sub(replace, markdown)


def stage_pdf_sources(sources: list[Path], staging_directory: Path) -> list[Path]:
    """Create temporary copies with unique anchors and PDF-local chapter links."""
    staged: list[Path] = []
    staging_directory.mkdir(parents=True, exist_ok=True)
    chapter_anchors = {
        source.resolve(): f"chapter-{index:02d}-{source.stem}"
        for index, source in enumerate(sources, start=1)
    }
    for source in sources:
        markdown = source.read_text(encoding="utf-8")
        chapter_prefix = chapter_anchors[source.resolve()]
        markdown = add_chapter_anchor(markdown, chapter_prefix)
        markdown = rewrite_pdf_links(markdown, source, chapter_anchors)
        markdown = REFERENCE_ID.sub(
            lambda match: f"{chapter_prefix}-ref-{match.group(1)}", markdown
        )
        markdown = REFERENCE_LINK.sub(
            lambda match: f"{chapter_prefix}-ref-{match.group(1)}", markdown
        )
        staged_path = staging_directory / f"{chapter_prefix}.md"
        staged_path.write_text(markdown, encoding="utf-8")
        staged.append(staged_path)
    return staged


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "pdf" / "preview.pdf")
    args = parser.parse_args()

    try:
        sources = read_sources()
    except (FileNotFoundError, ValueError) as error:
        parser.error(str(error))
    for executable in ("pandoc", "xelatex"):
        if shutil.which(executable) is None:
            parser.error(f"Required executable not found: {executable}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ai-silicon-pdf-") as temporary_directory:
        pdf_sources = stage_pdf_sources(sources, Path(temporary_directory))
        command = [
            "pandoc",
            *map(str, pdf_sources),
            f"--resource-path={os.pathsep.join([str(ROOT), *(str(source.parent) for source in sources)])}",
            "--from=markdown+tex_math_single_backslash",
            "--pdf-engine=xelatex",
            "--citeproc",
            f"--bibliography={ROOT / 'references' / 'references.bib'}",
            "--toc",
            "--toc-depth=1",
            "--number-sections",
            "--top-level-division=chapter",
            "-V", "documentclass=book",
            "-V", "classoption=openany",
            "-V", "title=AI From Silicon to Intelligence",
            "-V", "subtitle=Une encyclopédie technique de l’intelligence artificielle moderne",
            "-V", "lang=fr-FR",
            "-V", "papersize=a4",
            "-V", "fontsize=11pt",
            "-V", "mainfont=Latin Modern Roman",
            "-V", "monofont=Latin Modern Mono",
            "-V", "geometry:margin=24mm",
            "-V", "linestretch=1.08",
            "-V", "pagestyle=plain",
            "-V", "colorlinks=true",
            "-V", "linkcolor=blue",
            "-V", "urlcolor=blue",
            "-V", "citecolor=blue",
            "-V", "toc-title=Table des matières",
            "-o", str(args.output),
        ]
        subprocess.run(command, cwd=ROOT, check=True)
    print(f"PDF preview written to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
