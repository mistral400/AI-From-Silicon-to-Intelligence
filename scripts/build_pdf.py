#!/usr/bin/env python3
"""Build the current PDF preview from canonical Markdown using Pandoc/XeLaTeX."""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ROOT / "book" / "index.md",
    ROOT / "book" / "table-of-contents.md",
    ROOT / "book" / "chapter-template.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "pdf" / "preview.pdf")
    args = parser.parse_args()

    missing = [str(path.relative_to(ROOT)) for path in SOURCES if not path.is_file()]
    if missing:
        parser.error("Missing source files: " + ", ".join(missing))
    for executable in ("pandoc", "xelatex"):
        if shutil.which(executable) is None:
            parser.error(f"Required executable not found: {executable}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "pandoc",
        *map(str, SOURCES),
        "--from=markdown",
        "--pdf-engine=xelatex",
        "--citeproc",
        f"--bibliography={ROOT / 'references' / 'references.bib'}",
        "--toc",
        "--number-sections",
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
