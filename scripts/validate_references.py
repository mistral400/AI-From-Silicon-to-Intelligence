#!/usr/bin/env python3
"""Validate BibTeX records, citation keys, and local Markdown links."""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ENTRY_START = re.compile(r"@\s*([A-Za-z][A-Za-z0-9_-]*)\s*([({])")
CITATION_BLOCK = re.compile(r"\[@([^\]]+)\]")
CITATION_KEY = re.compile(r"(?<![\w])@([A-Za-z0-9_:.+/-]+)")
MD_LINK_START = re.compile(r"!?\[[^\]]*\]\(")
HTML_LINK = re.compile(r"\b(?:href|src)\s*=\s*([\"'])(.*?)\1", re.IGNORECASE)
HTML_ID = re.compile(r"\b(?:id|name)\s*=\s*([\"'])(.*?)\1", re.IGNORECASE)
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
EXPLICIT_ID = re.compile(r"\s*\{#([A-Za-z0-9_.:-]+)[^}]*\}\s*$")
INLINE_CODE = re.compile(chr(96) + r"+.*?" + chr(96) + r"+")


@dataclass(frozen=True)
class Issue:
    path: str
    line: int
    message: str

    def __str__(self) -> str:
        where = f"{self.path}:{self.line}" if self.line else self.path
        return f"{where}: {self.message}"


@dataclass(frozen=True)
class BibEntry:
    entry_type: str
    key: str
    fields: dict[str, str]
    line: int


def _entry_end(source: str, start: int, opener: str) -> int | None:
    depth, braces = 1, 0
    quoted = escaped = False
    for index, char in enumerate(source[start:], start):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"' and braces == 0:
            quoted = not quoted
            continue
        if quoted:
            continue
        if char == "{":
            braces += 1
        elif char == "}" and braces:
            braces -= 1
        elif opener == "{" and char == "}" and braces == 0:
            depth -= 1
            if depth == 0:
                return index
        elif opener == "(" and braces == 0:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return index
    return None


def _split_top_level(value: str) -> list[str]:
    parts, start = [], 0
    braces = parens = 0
    quoted = escaped = False
    for index, char in enumerate(value):
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == '"' and braces == 0:
            quoted = not quoted
        elif not quoted:
            if char == "{":
                braces += 1
            elif char == "}" and braces:
                braces -= 1
            elif char == "(" and braces == 0:
                parens += 1
            elif char == ")" and parens:
                parens -= 1
            elif char == "," and braces == 0 and parens == 0:
                parts.append(value[start:index].strip())
                start = index + 1
    if value[start:].strip():
        parts.append(value[start:].strip())
    return parts


def _unwrap(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == "{" and value[-1] == "}":
        return value[1:-1].strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1].strip()
    return value


def parse_bibtex(source: str, path: str) -> tuple[list[BibEntry], list[Issue]]:
    entries, issues, position = [], [], 0
    while match := ENTRY_START.search(source, position):
        kind, opener = match.group(1).lower(), match.group(2)
        end = _entry_end(source, match.end(), opener)
        line = source.count("\n", 0, match.start()) + 1
        if end is None:
            issues.append(Issue(path, line, f"unterminated BibTeX @{kind} entry"))
            break
        position = end + 1
        if kind in {"comment", "preamble", "string"}:
            continue
        parts = _split_top_level(source[match.end():end])
        if not parts or not parts[0]:
            issues.append(Issue(path, line, f"BibTeX @{kind} entry has no citation key"))
            continue
        key = parts[0].strip()
        if not re.fullmatch(r"[A-Za-z0-9_:.+/-]+", key):
            issues.append(Issue(path, line, f"invalid BibTeX citation key {key!r}"))
            continue
        fields = {}
        for part in parts[1:]:
            field = re.match(r"\s*([A-Za-z][A-Za-z0-9_-]*)\s*=\s*(.*?)\s*$", part, re.DOTALL)
            if not field:
                if part:
                    issues.append(Issue(path, line, f"malformed field in BibTeX entry {key!r}"))
                continue
            fields[field.group(1).lower()] = _unwrap(field.group(2))
        entries.append(BibEntry(kind, key, fields, line))
    return entries, issues


def _visible_lines(source: str) -> list[str]:
    output, fence_char, fence_length = [], "", 0
    for line in source.splitlines():
        fence = re.match(r"^ {0,3}(\x60{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)
            if not fence_char:
                fence_char, fence_length = marker[0], len(marker)
                output.append("")
                continue
            if marker[0] == fence_char and len(marker) >= fence_length:
                fence_char, fence_length = "", 0
                output.append("")
                continue
        if fence_char:
            output.append("")
        else:
            line = re.sub(r"<!--.*?-->", "", line)
            output.append(INLINE_CODE.sub("", line))
    return output


def _links(line: str) -> list[tuple[int, str]]:
    result = []
    for match in MD_LINK_START.finditer(line):
        index = match.end()
        while index < len(line) and line[index].isspace():
            index += 1
        if index >= len(line):
            continue
        if line[index] == "<":
            end = line.find(">", index + 1)
            if end < 0:
                continue
            destination = line[index + 1:end]
        else:
            start, nested, escaped = index, 0, False
            while index < len(line):
                char = line[index]
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "(":
                    nested += 1
                elif char == ")":
                    if nested == 0:
                        break
                    nested -= 1
                elif char.isspace() and nested == 0:
                    break
                index += 1
            destination = line[start:index]
        destination = re.sub(r"\\([\\() ])", r"\1", destination).strip()
        if destination:
            result.append((match.start(), destination))
    result.extend((m.start(), m.group(2).strip()) for m in HTML_LINK.finditer(line))
    return result


def _slugify(title: str) -> str:
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", title)
    title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", title)
    title = re.sub(r"[*_~]", "", title).replace(chr(96), "")
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    title = "".join(char if char.isalnum() or char in "-_ " else " " for char in title)
    return re.sub(r"[\s-]+", "-", title).strip("-")


def _anchors(source: str) -> set[str]:
    result, counts = set(), {}
    for line in _visible_lines(source):
        result.update(match.group(2) for match in HTML_ID.finditer(line))
        heading = HEADING.match(line)
        if not heading:
            continue
        title = heading.group(2)
        explicit = EXPLICIT_ID.search(title)
        if explicit:
            result.add(explicit.group(1))
            title = title[:explicit.start()]
        slug = _slugify(title)
        if slug:
            occurrence = counts.get(slug, 0)
            counts[slug] = occurrence + 1
            result.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return result


def _metadata_issues(entry: BibEntry, path: str) -> list[Issue]:
    errors, fields = [], entry.fields
    for name in ("title", "year"):
        if not fields.get(name, "").strip():
            errors.append(Issue(path, entry.line, f"BibTeX entry {entry.key!r} is missing required field {name!r}"))
    if not (fields.get("author") or fields.get("editor")):
        errors.append(Issue(path, entry.line, f"BibTeX entry {entry.key!r} is missing author/editor metadata"))
    if entry.entry_type == "article" and not fields.get("journal"):
        errors.append(Issue(path, entry.line, f"BibTeX article {entry.key!r} is missing required field 'journal'"))
    if entry.entry_type in {"inproceedings", "conference"} and not fields.get("booktitle"):
        errors.append(Issue(path, entry.line, f"BibTeX conference entry {entry.key!r} is missing required field 'booktitle'"))
    url, doi = fields.get("url", "").strip(), fields.get("doi", "").strip()
    if not url and not doi:
        errors.append(Issue(path, entry.line, f"BibTeX entry {entry.key!r} needs a URL or DOI"))
    if url:
        parsed = urlsplit(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(Issue(path, entry.line, f"BibTeX entry {entry.key!r} has an invalid URL: {url!r}"))
    if doi:
        doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
        if not re.fullmatch(r"10\.\d{4,9}/\S+", doi):
            errors.append(Issue(path, entry.line, f"BibTeX entry {entry.key!r} has an invalid DOI: {doi!r}"))
    return errors


def _check_link(root: Path, source: Path, line: int, destination: str,
                anchors: dict[Path, set[str]], issues: list[Issue]) -> None:
    relative = source.relative_to(root).as_posix()
    try:
        parsed = urlsplit(destination)
    except ValueError:
        issues.append(Issue(relative, line, f"invalid local link {destination!r}"))
        return
    if destination.lower().startswith("javascript:"):
        issues.append(Issue(relative, line, "javascript: links are not allowed"))
        return
    if parsed.scheme or parsed.netloc or destination.startswith("//"):
        return
    raw_path = unquote(parsed.path)
    if parsed.path.startswith("/"):
        target = (root / raw_path.lstrip("\\/")).resolve()
    elif parsed.path:
        target = (source.parent / raw_path).resolve()
    else:
        target = source.resolve()
    try:
        target.relative_to(root)
    except ValueError:
        issues.append(Issue(relative, line, f"local link escapes the repository: {destination!r}"))
        return
    if target.is_dir():
        target = next((target / name for name in ("index.md", "README.md") if (target / name).is_file()), target)
    if not target.exists():
        issues.append(Issue(relative, line, f"broken local link {destination!r}"))
        return
    fragment = unquote(parsed.fragment)
    if fragment and target.suffix.lower() == ".md":
        available = anchors.get(target.resolve())
        if available is None:
            available = _anchors(target.read_text(encoding="utf-8"))
        if fragment not in available:
            issues.append(Issue(relative, line, f"broken local anchor {destination!r}"))


def validate_repository(root: Path) -> list[Issue]:
    root = root.resolve()
    bib = root / "references" / "references.bib"
    bib_rel = bib.relative_to(root).as_posix()
    if not bib.is_file():
        return [Issue(bib_rel, 0, "bibliography file does not exist")]
    entries, issues = parse_bibtex(bib.read_text(encoding="utf-8"), bib_rel)
    keys = {}
    for entry in entries:
        folded = entry.key.casefold()
        if folded in keys:
            issues.append(Issue(bib_rel, entry.line, f"duplicate BibTeX key {entry.key!r} (first defined on line {keys[folded].line})"))
        else:
            keys[folded] = entry
        issues.extend(_metadata_issues(entry, bib_rel))

    ignored = {".git", ".venv", "site", "tmp", "work", "node_modules"}
    markdown = sorted(path for path in root.rglob("*.md") if not set(path.relative_to(root).parts) & ignored)
    pages = {path.resolve(): path.read_text(encoding="utf-8") for path in markdown}
    anchors = {path: _anchors(text) for path, text in pages.items()}
    citations = []
    for path, source in pages.items():
        for line_number, line in enumerate(_visible_lines(source), start=1):
            for block in CITATION_BLOCK.finditer(line):
                citations.extend((path, line_number, match.group(1)) for match in CITATION_KEY.finditer(block.group(0)))
            for _, destination in _links(line):
                try:
                    parsed_link = urlsplit(destination)
                except ValueError:
                    _check_link(root, path, line_number, destination, anchors, issues)
                    continue
                fragment = unquote(parsed_link.fragment)
                ref = re.fullmatch(r"ref-([A-Za-z0-9_:.+/-]+)", fragment)
                if ref:
                    citations.append((path, line_number, ref.group(1)))
                    if ref.group(1).casefold() not in keys:
                        issues.append(Issue(path.relative_to(root).as_posix(), line_number, f"reference anchor uses unknown BibTeX key {ref.group(1)!r}"))
                _check_link(root, path, line_number, destination, anchors, issues)
    for path, line_number, key in citations:
        if key.casefold() not in keys:
            issues.append(Issue(path.relative_to(root).as_posix(), line_number, f"citation key {key!r} does not exist in {bib_rel}"))
    return sorted(issues, key=lambda issue: (issue.path, issue.line, issue.message))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root")
    args = parser.parse_args()
    issues = validate_repository(args.root)
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        print(f"Validation failed: {len(issues)} issue(s).", file=sys.stderr)
        return 1
    print("Reference and local-link validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



