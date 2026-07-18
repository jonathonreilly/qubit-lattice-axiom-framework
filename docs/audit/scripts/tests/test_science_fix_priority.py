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
        lane = {"lane_row"}
        easy_bridge = _row("x", "conditional_missing_bridge_theorem",
                           descendants=999, difficulty="easy")
        medium_lane_renaming = _row("lane_row", "renaming",
                                    descendants=999, difficulty="medium")
        self.assertLess(sfl.candidate_sort_key(easy_bridge, lane),
                        sfl.candidate_sort_key(medium_lane_renaming, lane))

    def test_lane_beats_category_within_bucket(self):
        lane = {"lane_row"}
        lane_bridge = _row("lane_row", "conditional_missing_bridge_theorem")
        stray_renaming = _row("other", "renaming", descendants=999)
        self.assertLess(sfl.candidate_sort_key(lane_bridge, lane),
                        sfl.candidate_sort_key(stray_renaming, lane))

    def test_mechanical_before_bridge_then_descendants(self):
        rows = [
            _row("bridge_big", "conditional_missing_bridge_theorem", 999),
            _row("rename_small", "renaming", 1),
            _row("rename_big", "renaming", 50),
            _row("numerical", "numerical_match", 999),
        ]
        rows.sort(key=lambda r: sfl.candidate_sort_key(r, set()))
        self.assertEqual([r["claim_id"] for r in rows],
                         ["rename_big", "rename_small", "numerical", "bridge_big"])

    def test_category_rank_parity_with_categories(self):
        self.assertEqual(set(sfl.CATEGORY_RANK), set(sfl.CATEGORIES))


class PublicationLaneIdsTest(unittest.TestCase):
    def test_reads_admitted_and_degrades_to_empty(self):
        import tempfile
        from unittest import mock

        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "publication_lane_manifest.json"
            manifest.write_text(json.dumps({"admitted": ["a", "b"]}))
            with mock.patch.object(sfl, "PUBLICATION_LANE_MANIFEST", manifest):
                self.assertEqual(sfl.publication_lane_ids(), {"a", "b"})
            with mock.patch.object(
                sfl, "PUBLICATION_LANE_MANIFEST", Path(tmp) / "absent.json"
            ):
                self.assertEqual(sfl.publication_lane_ids(), set())


class OpenScienceFixPrTest(unittest.TestCase):
    def _probe(self, returncode=0, stdout="[]", raises=None):
        from unittest import mock

        def fake_run(*args, **kwargs):
            if raises:
                raise raises
            return mock.Mock(returncode=returncode, stdout=stdout)

        with mock.patch.object(sfl.subprocess, "run", fake_run):
            return sfl.open_science_fix_pr("claim_x")

    def test_match_requires_claim_id_in_title(self):
        prs = json.dumps([
            {"title": "science-fix: claim_y hardening", "url": "u1"},
            {"title": "science-fix: claim_x bridge", "url": "u2"},
        ])
        self.assertEqual(self._probe(stdout=prs), "u2")

    def test_no_match_and_gh_failure_return_none(self):
        self.assertIsNone(self._probe(stdout="[]"))
        self.assertIsNone(self._probe(returncode=1))
        self.assertIsNone(self._probe(stdout="not-json"))
        self.assertIsNone(self._probe(raises=OSError("gh missing")))


if __name__ == "__main__":
    unittest.main()
