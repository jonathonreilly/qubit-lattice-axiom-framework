"""Tests for the read-only closure report on notes named without a link."""
import json
import contextlib
import io
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import report_closure_unlinked_mentions as report  # noqa: E402


class ClosureUnlinkedMentionsTest(unittest.TestCase):
    def _repo(self, tmp: Path, notes: dict) -> None:
        for claim_id, (text, deps) in notes.items():
            note = tmp / f"docs/{claim_id.upper()}.md"
            note.parent.mkdir(parents=True, exist_ok=True)
            note.write_text(text)
            shard = tmp / f"docs/audit/data/ledger/{claim_id[:2]}/{claim_id}.json"
            shard.parent.mkdir(parents=True, exist_ok=True)
            shard.write_text(json.dumps({
                "claim_id": claim_id,
                "note_path": f"docs/{claim_id.upper()}.md",
                "claim_type": "no_go",
                "deps": deps,
            }))

    def _mentions(self, notes: dict, roots: list[str]) -> list[dict]:
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self._repo(tmp, notes)
            rows = report.load_rows(tmp)
            return report.unlinked_mentions(rows, report.dependency_closure(rows, roots), tmp)

    def test_backticked_note_outside_closure_is_reported(self):
        found = self._mentions(
            {"root_a": ("uses `HIDDEN_B.md` here", []), "hidden_b": ("", [])}, ["root_a"]
        )
        self.assertEqual([m["claim_id"] for m in found], ["hidden_b"])
        self.assertEqual(found[0]["named_by"], ["root_a"])

    def test_linked_dependency_and_transitive_mentions_are_not_gaps(self):
        found = self._mentions(
            {
                "root_a": ("[dep](DEP_B.md)", ["dep_b"]),
                "dep_b": ("see `ROOT_A.md` and `LEAF_C.md`", ["leaf_c"]),
                "leaf_c": ("", []),
            },
            ["root_a"],
        )
        self.assertEqual(found, [])

    def test_mention_from_a_transitive_dependency_is_reported(self):
        found = self._mentions(
            {
                "root_a": ("", ["dep_b"]),
                "dep_b": ("assumes HIDDEN_C.md", []),
                "hidden_c": ("", []),
            },
            ["root_a"],
        )
        self.assertEqual(found[0]["named_by"], ["dep_b"])

    def test_names_that_are_not_ledger_notes_are_ignored(self):
        self.assertEqual(self._mentions({"root_a": ("see README.md", [])}, ["root_a"]), [])

    def test_notes_missing_from_disk_are_named(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self._repo(tmp, {"root_a": ("", ["dep_b"]), "dep_b": ("", [])})
            (tmp / "docs/DEP_B.md").unlink()
            rows = report.load_rows(tmp)
            closure = report.dependency_closure(rows, ["root_a"])
            self.assertEqual(report.unreadable_notes(rows, closure, tmp), ["dep_b"])

    def test_missing_dependency_shard_refuses_incomplete_closure(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self._repo(tmp, {"root_a": ("", ["missing_b"])})
            stderr = io.StringIO()
            with patch.object(report, "REPO_ROOT", tmp), patch.object(
                sys, "argv", ["report", "--root", "root_a", "--json"]
            ), contextlib.redirect_stderr(stderr):
                self.assertEqual(report.main(), 3)
            self.assertIn("missing ledger rows", stderr.getvalue())
            self.assertIn("missing_b", stderr.getvalue())

    def _duplicate_names(self, tmp: Path, mention: str) -> tuple[dict, set[str]]:
        self._repo(tmp, {"root_a": (mention, [])})
        rows = report.load_rows(tmp)
        for claim_id in ("first", "second"):
            rows[claim_id] = {
                "claim_id": claim_id,
                "note_path": f"docs/{claim_id}/README.md",
                "claim_type": "meta",
                "deps": [],
            }
        return rows, {"root_a"}

    def test_qualified_name_preserves_directory_identity(self):
        for mention in ("docs/first/README.md", "./first/README.md"):
            with self.subTest(mention=mention), tempfile.TemporaryDirectory() as d:
                tmp = Path(d)
                rows, closure = self._duplicate_names(tmp, mention)
                found = report.unlinked_mentions(rows, closure, tmp)
                self.assertEqual([m["claim_id"] for m in found], ["first"])

    def test_qualified_nonledger_path_does_not_fall_back_to_basename(self):
        for mention in (
            "./raw/README.md",
            "prefix+docs/first/README.md",
            "https://example.org/docs/first/README.md",
        ):
            with self.subTest(mention=mention), tempfile.TemporaryDirectory() as d:
                tmp = Path(d)
                rows, closure = self._duplicate_names(tmp, mention)
                self.assertEqual(report.unlinked_mentions(rows, closure, tmp), [])

    def test_ambiguous_bare_name_preserves_all_candidates(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            rows, closure = self._duplicate_names(tmp, "README.md")
            found = report.unlinked_mentions(rows, closure, tmp)
            self.assertEqual([m["claim_id"] for m in found], ["first", "second"])
            self.assertTrue(all(m["named_by"] == ["root_a"] for m in found))


if __name__ == "__main__":
    unittest.main()
