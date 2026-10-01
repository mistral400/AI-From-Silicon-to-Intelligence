from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_pdf import add_chapter_anchor, rewrite_pdf_links  # noqa: E402


class BuildPdfLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.first = self.root / "part" / "first.md"
        self.second = self.root / "part" / "second.md"
        self.first.parent.mkdir()
        self.first.touch()
        self.second.touch()
        self.anchors = {
            self.first.resolve(): "chapter-01-first",
            self.second.resolve(): "chapter-02-second",
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_adds_an_explicit_chapter_anchor(self) -> None:
        source = "# A chapter\n\nText.\n"
        self.assertEqual(add_chapter_anchor(source, "chapter-01-first"), "# A chapter {#chapter-01-first}\n\nText.\n")

    def test_rewrites_local_chapter_link(self) -> None:
        source = "Read [the next chapter](second.md)."
        actual = rewrite_pdf_links(source, self.first, self.anchors)
        self.assertEqual(actual, "Read [the next chapter](#chapter-02-second).")

    def test_rewrites_link_to_reference_anchor(self) -> None:
        source = "See [the reference](second.md#ref-paper2024)."
        actual = rewrite_pdf_links(source, self.first, self.anchors)
        self.assertEqual(actual, "See [the reference](#chapter-02-second-ref-paper2024).")

    def test_keeps_external_links_and_images_unchanged(self) -> None:
        source = "[web](https://example.org/page.md) ![art](second.md)"
        self.assertEqual(rewrite_pdf_links(source, self.first, self.anchors), source)

    def test_rejects_local_markdown_file_missing_from_manifest(self) -> None:
        with self.assertRaisesRegex(ValueError, "not in the chapter manifest"):
            rewrite_pdf_links("[plan](missing.md)", self.first, self.anchors)

    def test_rejects_unmapped_cross_chapter_heading_fragment(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsupported fragment"):
            rewrite_pdf_links("[section](second.md#details)", self.first, self.anchors)


if __name__ == "__main__":
    unittest.main()
