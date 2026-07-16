"""Tests for the shadow-mode dispatch emitters (dispatch-retarget design
note, 2026-07-16): live-row would-park projection and the publication lane.
Reporting-only machinery — these tests also pin that nothing here mutates
queue ordering."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import compute_audit_queue as caq  # noqa: E402


def _row(status="audited_conditional", snapshot=None):
    return {
        "audit_status": status,
        "effective_status": status,
        "audit_state_snapshot": snapshot or {},
    }


class LiveWouldParkTest(unittest.TestCase):
    def test_parks_when_no_recorded_blocker_moved(self):
        rows = {"dep_a": {"effective_status": "unaudited", "claim_type": "no_go",
                          "claim_scope": "s", "note_hash": "h1"}}
        row = _row(snapshot={
            "dep_effective_status": {"dep_a": "unaudited"},
            "dep_claim_type": {"dep_a": "no_go"},
            "dep_claim_scope": {"dep_a": "s"},
            "dep_axiom_premise_note_hash": {"dep_a": "h1"},
        })
        parked, reason = caq._live_conditional_would_park(row, rows)
        self.assertTrue(parked)
        self.assertEqual(reason, "no_recorded_blocker_movement")

    def test_unparks_on_dep_status_change(self):
        rows = {"dep_a": {"effective_status": "retained"}}
        row = _row(snapshot={"dep_effective_status": {"dep_a": "unaudited"}})
        parked, reason = caq._live_conditional_would_park(row, rows)
        self.assertFalse(parked)
        self.assertIn("dep_effective_status_changed", reason)

    def test_unparks_on_dep_scope_change(self):
        rows = {"dep_a": {"effective_status": "unaudited", "claim_scope": "WIDER"}}
        row = _row(snapshot={
            "dep_effective_status": {"dep_a": "unaudited"},
            "dep_claim_scope": {"dep_a": "narrow"},
        })
        parked, reason = caq._live_conditional_would_park(row, rows)
        self.assertFalse(parked)
        self.assertIn("dep_claim_scope_changed", reason)

    def test_fail_open_without_snapshot_dep_map(self):
        parked, reason = caq._live_conditional_would_park(_row(), {})
        self.assertFalse(parked)
        self.assertEqual(reason, "fail_open_no_snapshot_dep_map")


class PublicationLaneTest(unittest.TestCase):
    def _with_paths(self, gap, manifest):
        tmp = tempfile.TemporaryDirectory()
        base = Path(tmp.name)
        old = (caq.PUBLICATION_GAP_PATH, caq.LANE_MANIFEST_PATH)
        caq.PUBLICATION_GAP_PATH = base / "gap.json"
        caq.LANE_MANIFEST_PATH = base / "manifest.json"
        if gap is not None:
            caq.PUBLICATION_GAP_PATH.write_text(json.dumps(gap))
        if manifest is not None:
            caq.LANE_MANIFEST_PATH.write_text(json.dumps(manifest))
        self.addCleanup(lambda: (setattr(caq, "PUBLICATION_GAP_PATH", old[0]),
                                 setattr(caq, "LANE_MANIFEST_PATH", old[1]),
                                 tmp.cleanup()))

    def _pending(self):
        return [
            {"claim_id": "cited_row", "criticality": "critical", "ready": True,
             "transitive_descendants": 5, "load_bearing_score": 2.0},
            {"claim_id": "uncited_row", "criticality": "critical", "ready": True,
             "transitive_descendants": 9, "load_bearing_score": 3.0},
            {"claim_id": "break_target", "criticality": "high", "ready": False,
             "transitive_descendants": 1, "load_bearing_score": 1.0,
             "would_park": False},
        ]

    def test_lane_is_candidate_subset_in_pending_order(self):
        self._with_paths(
            gap={"entries": [{"claim_id": "cited_row"}]},
            manifest={"admitted": ["cited_row"], "frozen_commit": "abc"},
        )
        lane = caq.build_publication_lane(
            self._pending(), [{"claim_id": "break_target"}]
        )
        self.assertEqual([e["claim_id"] for e in lane["lane"]],
                         ["cited_row", "break_target"])
        self.assertTrue(lane["lane"][0]["manifest_admitted"])
        self.assertFalse(lane["lane"][1]["manifest_admitted"])
        self.assertEqual(lane["pending_admission"], ["break_target"])
        self.assertEqual(lane["admitted_in_lane"], 1)
        self.assertTrue(lane["shadow_only"])

    def test_missing_gap_yields_empty_lane_flagged(self):
        self._with_paths(gap=None, manifest={"admitted": []})
        lane = caq.build_publication_lane(self._pending(), [])
        self.assertFalse(lane["gap_available"])
        self.assertEqual(lane["lane_size"], 0)

    def test_admitted_absent_from_candidates_reported(self):
        self._with_paths(
            gap={"entries": [{"claim_id": "cited_row"}]},
            manifest={"admitted": ["cited_row", "ghost_row"]},
        )
        lane = caq.build_publication_lane(self._pending(), [])
        self.assertEqual(lane["admitted_absent_from_candidates"], ["ghost_row"])


if __name__ == "__main__":
    unittest.main()
