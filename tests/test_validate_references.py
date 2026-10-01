from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_references import validate_repository  # noqa: E402


GOOD_BIB = """@misc{alpha2024,
  author = {Example Author},
  title = {A verified source},
  year = {2024},
  url = {https://example.org/source}
}
"""


class ValidateReferencesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "references").mkdir()
        (self.root / "book").mkdir()
        self.write("references/references.bib", GOOD_BIB)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def issues(self) -> list[str]:
        return [str(issue) for issue in validate_repository(self.root)]

    def test_valid_citation_and_local_anchor(self) -> None:
        self.write(
            "book/chapter.md",
            "# Chapter\n\nSee [Example Author (2024)](#ref-alpha2024).\n\n"
            "## References\n\n### Source {#ref-alpha2024}\n\nSource details.\n",
        )
        self.assertEqual([], self.issues())

    def test_missing_citation_key_is_reported(self) -> None:
        self.write("book/chapter.md", "See [Missing source](#ref-absent2024).\n")
        issues = self.issues()
        self.assertTrue(any("unknown BibTeX key 'absent2024'" in issue for issue in issues))
        self.assertTrue(any("broken local anchor" in issue for issue in issues))

    def test_missing_pandoc_citation_key_is_reported(self) -> None:
        self.write("book/chapter.md", "Cite [@absent2024].\n")
        self.assertTrue(any("citation key 'absent2024' does not exist" in issue for issue in self.issues()))

    def test_malformed_link_is_reported_without_crashing(self) -> None:
        self.write("book/chapter.md", "[bad](http://[::1).\n")
        self.assertTrue(any("invalid local link" in issue for issue in self.issues()))

    def test_duplicate_bibtex_key_is_reported(self) -> None:
        duplicate = GOOD_BIB + GOOD_BIB.replace("A verified source", "Another source")
        self.write("references/references.bib", duplicate)
        self.write("book/chapter.md", "# Empty\n")
        self.assertTrue(any("duplicate BibTeX key 'alpha2024'" in issue for issue in self.issues()))

    def test_broken_file_and_fragment_are_reported(self) -> None:
        self.write("book/chapter.md", "[asset](missing.svg) and [page](other.md#absent).\n")
        self.write("book/other.md", "# Present\n")
        issues = self.issues()
        self.assertTrue(any("broken local link 'missing.svg'" in issue for issue in issues))
        self.assertTrue(any("broken local anchor 'other.md#absent'" in issue for issue in issues))

    def test_code_examples_are_not_treated_as_citations_or_links(self) -> None:
        self.write(
            "book/chapter.md",
            "~~~markdown\n[missing](missing.md) [@not-a-real-key]\n~~~\n",
        )
        self.assertEqual([], self.issues())

    def test_invalid_reference_metadata_is_reported(self) -> None:
        self.write(
            "references/references.bib",
            "@misc{bad2024, title={Incomplete}, year={2024}, url={not-a-url}}\n",
        )
        self.write("book/chapter.md", "# Empty\n")
        issues = self.issues()
        self.assertTrue(any("missing author/editor metadata" in issue for issue in issues))
        self.assertTrue(any("invalid URL" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()

