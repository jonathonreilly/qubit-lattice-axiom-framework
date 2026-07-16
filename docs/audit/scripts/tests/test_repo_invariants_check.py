"""Regression tests for the repo-invariants harness.

Covers the review findings from PR #5399 round 1: markdown lexical context
(code spans/fences, angle-bracket destinations, titles, non-path artifacts),
schema-invalid ledger shards, tracked-set discipline (untracked files must
not perturb measurements; untracked link targets are violations), and
snapshot-diff sensitivity to missing-vs-null and empty-object changes.
"""

import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import repo_invariants_check as ric  # noqa: E402


class ScanMarkdownLinkTargetsTest(unittest.TestCase):
    def test_extracts_plain_link_with_relative_path(self):
        self.assertEqual(
            ric.scan_markdown_link_targets("see [x](../audit/data/ledger/)"),
            ["../audit/data/ledger/"],
        )

    def test_ignores_links_inside_inline_code(self):
        text = "every markdown link `[..](OTHER.md)` is treated as an edge"
        self.assertEqual(ric.scan_markdown_link_targets(text), [])

    def test_ignores_links_inside_fenced_code(self):
        text = "```\n[real looking](DEAD.md)\n```\nafter"
        self.assertEqual(ric.scan_markdown_link_targets(text), [])

    def test_ignores_math_artifact_not_path_shaped(self):
        text = "the Hessian candidate S[h] = 1/2 D^2 W[g_*](h,h) in the cell"
        self.assertEqual(ric.scan_markdown_link_targets(text), [])

    def test_handles_title_and_angle_bracket_destination(self):
        text = '[a](X.md "The X note") and [b](<sub dir/Y.md>)'
        self.assertEqual(
            ric.scan_markdown_link_targets(text), ["X.md", "sub dir/Y.md"]
        )

    def test_skips_external_and_mailto(self):
        text = "[w](https://example.org/x.md) [m](mailto:a@b.c) [k](K.md)"
        self.assertEqual(ric.scan_markdown_link_targets(text), ["K.md"])


class CollectLedgerSchemaTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._old_root = ric.REPO_ROOT
        ric.REPO_ROOT = self._tmp.name
        self.addCleanup(self._restore)
        shard_dir = Path(self._tmp.name) / ric.LEDGER_PREFIX / "aa"
        shard_dir.mkdir(parents=True)
        (shard_dir / "good_note.json").write_text(json.dumps(
            {"claim_id": "good_note", "effective_status": "unaudited",
             "note_path": "docs/GOOD_NOTE.md"}))
        (shard_dir / "list_shard.json").write_text("[]")
        (shard_dir / "null_claim.json").write_text(json.dumps(
            {"claim_id": None, "effective_status": "retained"}))

    def _restore(self):
        ric.REPO_ROOT = self._old_root
        self._tmp.cleanup()

    def test_schema_invalid_shards_recorded_not_crashed(self):
        tracked = [
            ric.LEDGER_PREFIX + "aa/good_note.json",
            ric.LEDGER_PREFIX + "aa/list_shard.json",
            ric.LEDGER_PREFIX + "aa/null_claim.json",
            "docs/GOOD_NOTE.md",
        ]
        result = ric.collect_ledger(tracked)
        self.assertEqual(result["shard_count"], 3)
        self.assertEqual(len(result["shard_parse_errors"]), 2)
        self.assertEqual(result["rows_with_missing_note_path"], 0)
        self.assertEqual(
            result["effective_status_histogram"], {"retained": 1, "unaudited": 1}
        )

    def test_untracked_files_do_not_perturb_measurement(self):
        # An extra shard exists on disk but is not in the tracked list.
        extra = Path(self._tmp.name) / ric.LEDGER_PREFIX / "aa" / "scratch.json"
        extra.write_text(json.dumps({"claim_id": "scratch"}))
        tracked = [ric.LEDGER_PREFIX + "aa/good_note.json", "docs/GOOD_NOTE.md"]
        result = ric.collect_ledger(tracked)
        self.assertEqual(result["shard_count"], 1)
        self.assertNotIn("scratch", json.dumps(result))


class AuthorityLinksTrackedSetTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        self._old_root = ric.REPO_ROOT
        ric.REPO_ROOT = str(root)
        self.addCleanup(self._restore)
        (root / "docs" / "repo").mkdir(parents=True)
        (root / "README.md").write_text(
            "[tracked](docs/TRACKED.md) [untracked](docs/PRESENT_UNTRACKED.md) "
            "[gone](docs/MISSING.md) [dir](docs/repo/)"
        )
        (root / "docs" / "TRACKED.md").write_text("x")
        (root / "docs" / "PRESENT_UNTRACKED.md").write_text("x")
        (root / "docs" / "repo" / "KEEP.md").write_text("x")

    def _restore(self):
        ric.REPO_ROOT = self._old_root
        self._tmp.cleanup()

    def test_untracked_and_missing_targets_are_violations(self):
        tracked = ["README.md", "docs/TRACKED.md", "docs/repo/KEEP.md"]
        result = ric.collect_authority_links(tracked)
        reasons = {v["target"]: v["reason"] for v in result["violations"]}
        self.assertEqual(
            reasons,
            {
                "docs/PRESENT_UNTRACKED.md": "untracked",
                "docs/MISSING.md": "missing",
            },
        )


class DiffSensitivityTest(unittest.TestCase):
    def _diff(self, a: dict, b: dict, allow=""):
        with tempfile.TemporaryDirectory() as tmp:
            pa, pb = Path(tmp) / "a.json", Path(tmp) / "b.json"
            pa.write_text(json.dumps(a))
            pb.write_text(json.dumps(b))
            out = io.StringIO()
            with redirect_stdout(out):
                code = ric.run_diff(
                    str(pa), str(pb),
                    {k for k in allow.split(",") if k},
                )
            return code, out.getvalue()

    def test_missing_vs_null_is_a_difference(self):
        code, out = self._diff({"a": {}}, {"a": {"k": None}})
        self.assertEqual(code, 1)
        self.assertIn("CHANGED", out)

    def test_empty_object_appearance_is_a_difference(self):
        code, out = self._diff({"a": {"k": 1}}, {"a": {"k": 1}, "b": {}})
        self.assertEqual(code, 1)

    def test_allow_is_dot_segment_bounded(self):
        code, _ = self._diff({"a": {"b": 1, "bb": 1}}, {"a": {"b": 2, "bb": 2}},
                             allow="a.b")
        self.assertEqual(code, 1)  # a.bb change is NOT covered by allow=a.b

    def test_identical_snapshots_pass(self):
        code, out = self._diff({"a": {"k": 1}}, {"a": {"k": 1}})
        self.assertEqual(code, 0)
        self.assertIn("IDENTICAL", out)


if __name__ == "__main__":
    unittest.main()
