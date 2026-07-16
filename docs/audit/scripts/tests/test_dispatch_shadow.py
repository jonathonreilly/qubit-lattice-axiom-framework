"""Tests for the shadow-mode dispatch emitters (dispatch-retarget design
note, 2026-07-16): live-row would-park classification (all compared
channels), lane eligibility under the tracked manifest authority, real
producer schemas, lifecycle projection against archived decoys, and a
hermetic golden check that shadow tagging leaves queue membership and order
untouched."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import compute_audit_queue as caq  # noqa: E402


def _row(status="audited_conditional", snapshot=None, previous=None):
    row = {
        "audit_status": status,
        "effective_status": status,
        "audit_state_snapshot": snapshot or {},
    }
    if previous is not None:
        row["previous_audits"] = previous
    return row


FULL_SNAPSHOT = {
    "dep_effective_status": {"dep_a": "unaudited"},
    "dep_claim_type": {"dep_a": "no_go"},
    "dep_claim_scope": {"dep_a": "s"},
    "dep_axiom_premise_note_hash": {"dep_a": "h1"},
}
DEP_UNCHANGED = {"dep_a": {"effective_status": "unaudited", "claim_type": "no_go",
                           "claim_scope": "s", "note_hash": "h1"}}


class LiveWouldParkTest(unittest.TestCase):
    def test_parks_when_no_recorded_blocker_moved(self):
        parked, reason = caq._live_conditional_would_park(
            _row(snapshot=FULL_SNAPSHOT), dict(DEP_UNCHANGED))
        self.assertTrue(parked)
        self.assertEqual(reason, "no_recorded_blocker_movement")

    def test_unparks_on_each_channel(self):
        for field, changed in (
            ("effective_status", "retained"),
            ("claim_type", "bounded_theorem"),
            ("claim_scope", "WIDER"),
            ("note_hash", "h2"),
        ):
            rows = {"dep_a": dict(DEP_UNCHANGED["dep_a"])}
            rows["dep_a"][field] = changed
            parked, reason = caq._live_conditional_would_park(
                _row(snapshot=FULL_SNAPSHOT), rows)
            self.assertFalse(parked, field)
            self.assertIn("changed", reason)

    def test_fail_open_without_snapshot_dep_map(self):
        parked, reason = caq._live_conditional_would_park(_row(), {})
        self.assertFalse(parked)
        self.assertEqual(reason, "fail_open_no_snapshot_dep_map")

    def test_live_projection_ignores_archived_decoy(self):
        # An archived verdict with CHANGED deps must not override the live
        # top-level snapshot (lifecycle projection: live rows read live).
        decoy = [{"audit_status": "audited_conditional",
                  "audit_state_snapshot": {
                      "dep_effective_status": {"dep_a": "retained"}}}]
        parked, reason = caq._live_conditional_would_park(
            _row(snapshot=FULL_SNAPSHOT, previous=decoy), dict(DEP_UNCHANGED))
        self.assertTrue(parked)
        self.assertEqual(reason, "no_recorded_blocker_movement")


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

    def _targets(self):
        # REAL producer schema: cycle_break_targets() emits primary_break_target.
        return [{"primary_break_target": "break_target", "cycle_length": 2}]

    def _manifest(self, admitted):
        return {"schema_version": 1, "frozen_commit": "abc",
                "admitted": admitted, "pending": []}

    def test_lane_contains_only_admitted_candidates_in_pending_order(self):
        self._with_paths(
            gap={"entries": [{"claim_id": "cited_row"}]},
            manifest=self._manifest(["cited_row"]),
        )
        lane = caq.build_publication_lane(self._pending(), self._targets())
        self.assertEqual([e["claim_id"] for e in lane["lane"]], ["cited_row"])
        self.assertEqual(lane["pending_admission"], ["break_target"])
        self.assertEqual(lane["manifest_state"], "ok")
        self.assertTrue(lane["shadow_only"])

    def test_admitted_break_target_enters_lane_via_real_schema(self):
        self._with_paths(
            gap={"entries": [{"claim_id": "cited_row"}]},
            manifest=self._manifest(["cited_row", "break_target"]),
        )
        lane = caq.build_publication_lane(self._pending(), self._targets())
        self.assertEqual([e["claim_id"] for e in lane["lane"]],
                         ["cited_row", "break_target"])
        self.assertTrue(lane["lane"][1]["is_primary_cycle_break_target"])
        self.assertEqual(lane["pending_admission"], [])

    def test_missing_manifest_yields_empty_lane_with_state(self):
        self._with_paths(gap={"entries": [{"claim_id": "cited_row"}]}, manifest=None)
        lane = caq.build_publication_lane(self._pending(), self._targets())
        self.assertEqual(lane["lane_size"], 0)
        self.assertEqual(lane["manifest_state"], "manifest_missing_or_unreadable")
        self.assertIn("cited_row", lane["pending_admission"])

    def test_malformed_manifest_rejected(self):
        self._with_paths(
            gap={"entries": [{"claim_id": "cited_row"}]},
            manifest={"schema_version": 1, "frozen_commit": "abc",
                      "admitted": ["cited_row"],
                      "pending": [{"claim_id": "x"}]},  # missing first_report_date
        )
        lane = caq.build_publication_lane(self._pending(), self._targets())
        self.assertEqual(lane["lane_size"], 0)
        self.assertEqual(lane["manifest_state"], "manifest_pending_entry_malformed")

    def test_missing_gap_yields_no_gap_candidates_flagged(self):
        self._with_paths(gap=None, manifest=self._manifest(["break_target"]))
        lane = caq.build_publication_lane(self._pending(), self._targets())
        self.assertFalse(lane["gap_available"])
        self.assertEqual([e["claim_id"] for e in lane["lane"]], ["break_target"])

    def test_admitted_absent_from_candidates_reported(self):
        self._with_paths(
            gap={"entries": [{"claim_id": "cited_row"}]},
            manifest=self._manifest(["cited_row", "ghost_row"]),
        )
        lane = caq.build_publication_lane(self._pending(), self._targets())
        self.assertEqual(lane["admitted_absent_from_candidates"], ["ghost_row"])


class GoldenQueueInvarianceTest(unittest.TestCase):
    """Shadow tagging must not change queue membership or order: run main()
    on a fixture ledger and compare against the documented sort applied to
    the same rows with the shadow tags stripped."""

    def test_membership_and_order_unchanged_by_shadow_tags(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            rows = {
                "crit_ready": {"audit_status": "unaudited", "criticality": "critical",
                               "deps": [], "transitive_descendants": 3,
                               "load_bearing_score": 1.0, "note_path": "docs/A.md"},
                "cond_live": {"audit_status": "audited_conditional",
                              "criticality": "high", "deps": ["crit_ready"],
                              "transitive_descendants": 1, "load_bearing_score": 0.5,
                              "note_path": "docs/B.md",
                              "audit_state_snapshot": {
                                  "dep_effective_status": {"crit_ready": "unaudited"}}},
                "leaf_row": {"audit_status": "unaudited", "criticality": "leaf",
                             "deps": [], "transitive_descendants": 0,
                             "load_bearing_score": 0.1, "note_path": "docs/C.md"},
            }
            for cid, r in rows.items():
                r.setdefault("effective_status", r["audit_status"])
            (base / "audit_ledger.json").write_text(json.dumps({"rows": rows}))
            patches = dict(
                CYCLE_INVENTORY_PATH=base / "cycle_inventory.json",
                LEDGER_PATH=base / "audit_ledger.json",
                QUEUE_JSON=base / "audit_queue.json",
                QUEUE_MD=base / "AUDIT_QUEUE.md",
                PUBLICATION_GAP_PATH=base / "gap.json",
                LANE_MANIFEST_PATH=base / "manifest.json",
                LANE_JSON=base / "lane.json",
            )
            with mock.patch.multiple(caq, **patches), \
                    mock.patch.object(caq, "REPO_ROOT", base), \
                    mock.patch.object(caq.ledger_io, "ensure_cache", lambda: None):
                caq.main()
            queue = json.loads((base / "audit_queue.json").read_text())
            got = [(e["claim_id"], e["ready"]) for e in queue["queue"]]
            stripped = []
            for e in queue["queue"]:
                clean = {k: v for k, v in e.items()
                         if k not in ("would_park", "would_park_reason")}
                stripped.append(clean)
            expected_order = sorted(
                stripped,
                key=lambda e: (-e["criticality_rank"], 0 if e["ready"] else 1,
                               -e["transitive_descendants"], -e["load_bearing_score"]),
            )
            self.assertEqual([e["claim_id"] for e in expected_order],
                             [g[0] for g in got])
            self.assertEqual({g[0] for g in got}, set(rows))
            cond = next(e for e in queue["queue"] if e["claim_id"] == "cond_live")
            self.assertIn("would_park", cond)
            self.assertTrue((base / "lane.json").exists())


if __name__ == "__main__":
    unittest.main()
