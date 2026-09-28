#!/usr/bin/env python3
"""Build the current PDF preview from the ordered Markdown sources using Pandoc/XeLaTeX."""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "book" / "book-order.txt"


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
    command = [
        "pandoc",
        *map(str, sources),
        "--from=markdown",
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
    subprocess.run(command, cwd=ROOT, check=True)
    print(f"PDF preview written to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
