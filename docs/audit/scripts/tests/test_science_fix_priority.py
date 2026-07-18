"""Science-fix scheduling: lane priority, category ranks, cross-clone dedupe."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import science_fix_loop as sfl


def _row(cid, category, descendants=1, difficulty="easy"):
    return {"claim_id": cid, "category": category,
            "descendants": descendants, "difficulty": difficulty}


class CandidateSortKeyTest(unittest.TestCase):
    def test_difficulty_dominates_everything(self):
        easy_bridge = _row("x", "conditional_missing_bridge_theorem",
                           descendants=999, difficulty="easy")
        medium_renaming = _row("y", "renaming",
                               descendants=999, difficulty="medium")
        self.assertLess(sfl.candidate_sort_key(easy_bridge),
                        sfl.candidate_sort_key(medium_renaming))

    def test_mechanical_before_bridge_then_descendants(self):
        rows = [
            _row("bridge_big", "conditional_missing_bridge_theorem", 999),
            _row("rename_small", "renaming", 1),
            _row("rename_big", "renaming", 50),
            _row("numerical", "numerical_match", 999),
        ]
        rows.sort(key=sfl.candidate_sort_key)
        self.assertEqual([r["claim_id"] for r in rows],
                         ["rename_big", "rename_small", "numerical", "bridge_big"])

    def test_category_rank_parity_with_categories(self):
        self.assertEqual(set(sfl.CATEGORY_RANK), set(sfl.CATEGORIES))

    def test_no_lane_term_without_cutover_ratification(self):
        # Governance: the shadow-only publication-lane manifest must not
        # feed live scheduling before the owner's cutover ratification.
        self.assertFalse(hasattr(sfl, "publication_lane_ids"))
        source = (Path(sfl.__file__)).read_text(encoding="utf-8")
        self.assertNotIn("publication_lane_manifest.json\"", source)


class OpenScienceFixPrTest(unittest.TestCase):
    def _probe(self, returncode=0, stdout="[]", raises=None):
        from unittest import mock

        def fake_run(*args, **kwargs):
            if raises:
                raise raises
            return mock.Mock(returncode=returncode, stdout=stdout)

        with mock.patch.object(sfl.subprocess, "run", fake_run):
            return sfl.open_science_fix_pr("claim_x")

    def test_matches_body_even_when_title_truncated(self):
        # open_pr truncates titles at 70 chars; the body always embeds the
        # full claim id, so body-match must carry the dedupe.
        prs = json.dumps([
            {"title": "science-fix: attempt to close some_other_claim...",
             "body": "derivation in `claim_y`", "url": "u1"},
            {"title": "science-fix: attempt to close a_very_long_claim_na...",
             "body": "missing derivation in `claim_x` (search for `claim_x`)",
             "url": "u2"},
        ])
        self.assertEqual(self._probe(stdout=prs), "u2")

    def test_title_match_is_secondary(self):
        prs = json.dumps([
            {"title": "science-fix: claim_x bridge", "body": "", "url": "u3"},
        ])
        self.assertEqual(self._probe(stdout=prs), "u3")

    def test_no_match_and_gh_failure_return_none(self):
        self.assertIsNone(self._probe(stdout="[]"))
        self.assertIsNone(self._probe(returncode=1))
        self.assertIsNone(self._probe(stdout="not-json"))
        self.assertIsNone(self._probe(raises=OSError("gh missing")))



class CleanupWorktreeBranchTest(unittest.TestCase):
    def test_cleanup_removes_worktree_and_local_branch(self):
        import subprocess

        path, branch = sfl.make_worktree("cleanup_probe_claim", "testrun0")
        try:
            self.assertTrue(path.exists())
            listed = subprocess.run(
                ["git", "branch", "--list", branch],
                cwd=sfl.REPO_ROOT, capture_output=True, text=True,
            ).stdout
            self.assertIn(branch, listed)
        finally:
            sfl.cleanup_worktree(path, branch)
        self.assertFalse(path.exists())
        listed = subprocess.run(
            ["git", "branch", "--list", branch],
            cwd=sfl.REPO_ROOT, capture_output=True, text=True,
        ).stdout
        self.assertNotIn(branch, listed)

if __name__ == "__main__":
    unittest.main()
