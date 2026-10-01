#!/usr/bin/env python3
"""Build the current PDF preview from the ordered Markdown sources using Pandoc/XeLaTeX."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "book" / "book-order.txt"
REFERENCE_ID = re.compile(r"(?<=\{#)ref-([A-Za-z0-9_:.+/-]+)(?=\})")
REFERENCE_LINK = re.compile(r"(?<=\]\(#)ref-([A-Za-z0-9_:.+/-]+)(?=\))")


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


def stage_pdf_sources(sources: list[Path]) -> list[Path]:
    """Create temporary source copies with reference anchors unique across the PDF."""
    staged: list[Path] = []
    try:
        for index, source in enumerate(sources, start=1):
            chapter_prefix = f"chapter-{index:02d}-{source.stem}"
            markdown = source.read_text(encoding="utf-8")
            markdown = REFERENCE_ID.sub(
                lambda match: f"{chapter_prefix}-ref-{match.group(1)}", markdown
            )
            markdown = REFERENCE_LINK.sub(
                lambda match: f"{chapter_prefix}-ref-{match.group(1)}", markdown
            )
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                suffix=source.suffix,
                prefix=f".{source.stem}-pdf-",
                dir=source.parent,
                delete=False,
            ) as temporary:
                temporary.write(markdown)
                staged.append(Path(temporary.name))
    except Exception:
        for path in staged:
            path.unlink(missing_ok=True)
        raise
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
    pdf_sources = stage_pdf_sources(sources)
    command = [
        "pandoc",
        *map(str, pdf_sources),
        "--from=markdown+tex_math_single_backslash",
        "--pdf-engine=xelatex",
        "--citeproc",
        f"--bibliography={ROOT / 'references' / 'references.bib'}",
        "--toc",
        "--toc-depth=2",
        "--number-sections",
        "-V", "title=AI From Silicon to Intelligence",
        "-V", "subtitle=Une encyclopédie technique de l’intelligence artificielle moderne",
        "-V", "lang=fr-FR",
        "-V", "mainfont=Latin Modern Roman",
        "-V", "geometry:margin=25mm",
        "-V", "toc-title=Table des matières",
        "-o", str(args.output),
    ]
    try:
        subprocess.run(command, cwd=ROOT, check=True)
    finally:
        for path in pdf_sources:
            path.unlink(missing_ok=True)
    print(f"PDF preview written to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
