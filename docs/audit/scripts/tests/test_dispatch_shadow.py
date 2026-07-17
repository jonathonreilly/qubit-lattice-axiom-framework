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
import compute_dispatch_shadow as cds  # noqa: E402


def _row(status="audited_conditional", snapshot=None, previous=None):
    row = {
        "audit_status": status,
        "effective_status": status,
        "audit_state_snapshot": snapshot or {},
    }
    if previous is not None:
        row["previous_audits"] = previous
    return row


V1_SNAPSHOT = {
    "schema": "blocker_fingerprint_v1",
    "dep_effective_status": {"dep_a": "unaudited"},
    "dep_claim_type": {"dep_a": "no_go"},
    "dep_claim_scope": {"dep_a": "s"},
    "dep_axiom_premise_note_hash": {"dep_a": "h1"},
    "helper_runner_hashes": {},
    "runner_cache_state": {},
    "artifact_classifier_state": {},
    "policy_versions": {},
    "premise_registry_epoch": 1,
}
LEGACY_SNAPSHOT = {  # no schema marker: legacy, always dispatch-open
    "dep_effective_status": {"dep_a": "unaudited"},
}
DEP_UNCHANGED = {"dep_a": {"effective_status": "unaudited", "claim_type": "no_go",
                           "claim_scope": "s", "note_hash": "h1"}}


class LiveWouldParkTest(unittest.TestCase):
    def test_v1_complete_parks_when_nothing_moved(self):
        parked, reason = caq._live_conditional_would_park(
            _row(snapshot=dict(V1_SNAPSHOT)), dict(DEP_UNCHANGED))
        self.assertTrue(parked)
        self.assertEqual(reason, "no_recorded_blocker_movement")

    def test_v1_unparks_on_each_dependency_channel(self):
        for field, changed in (
            ("effective_status", "retained"),
            ("claim_type", "bounded_theorem"),
            ("claim_scope", "WIDER"),
            ("note_hash", "h2"),
        ):
            rows = {"dep_a": dict(DEP_UNCHANGED["dep_a"])}
            rows["dep_a"][field] = changed
            parked, reason = caq._live_conditional_would_park(
                _row(snapshot=dict(V1_SNAPSHOT)), rows)
            self.assertFalse(parked, field)
            self.assertIn("changed", reason)

    def test_v1_unparks_on_helper_hash_change(self):
        snap = dict(V1_SNAPSHOT)
        snap["helper_runner_hashes"] = {"scripts/h.py": "old"}
        row = _row(snapshot=snap)
        row["helper_runner_hashes_current"] = {"scripts/h.py": "new"}
        parked, reason = caq._live_conditional_would_park(row, dict(DEP_UNCHANGED))
        self.assertFalse(parked)
        self.assertIn("helper_runner_hash_changed", reason)

    def test_legacy_unversioned_always_dispatch_open(self):
        parked, reason = caq._live_conditional_would_park(
            _row(snapshot=dict(LEGACY_SNAPSHOT)), dict(DEP_UNCHANGED))
        self.assertFalse(parked)
        self.assertEqual(reason, "fail_open_legacy_unversioned")

    def test_absent_snapshot_dispatch_open(self):
        parked, reason = caq._live_conditional_would_park(_row(), {})
        self.assertFalse(parked)
        self.assertEqual(reason, "fail_open_no_snapshot")

    def test_v1_incomplete_fails_loudly(self):
        snap = dict(V1_SNAPSHOT)
        del snap["policy_versions"]
        with self.assertRaises(caq.FingerprintV1Invalid):
            caq._live_conditional_would_park(_row(snapshot=snap), {})

    def test_live_projection_ignores_archived_decoy(self):
        decoy = [{"audit_status": "audited_conditional",
                  "audit_state_snapshot": {
                      "dep_effective_status": {"dep_a": "retained"}}}]
        parked, reason = caq._live_conditional_would_park(
            _row(snapshot=dict(V1_SNAPSHOT), previous=decoy), dict(DEP_UNCHANGED))
        self.assertTrue(parked)
        self.assertEqual(reason, "no_recorded_blocker_movement")


class PublicationLaneTest(unittest.TestCase):
    def _queue(self):
        return {
            "queue": [
                {"claim_id": "cited_row", "criticality": "critical", "ready": True,
                 "transitive_descendants": 5, "load_bearing_score": 2.0},
                {"claim_id": "uncited_row", "criticality": "critical", "ready": True,
                 "transitive_descendants": 9, "load_bearing_score": 3.0},
                {"claim_id": "break_target", "criticality": "high", "ready": False,
                 "transitive_descendants": 1, "load_bearing_score": 1.0,
                 "would_park": False},
                {"claim_id": "pending_row", "criticality": "leaf", "ready": True,
                 "transitive_descendants": 0, "load_bearing_score": 0.1},
            ],
            # REAL producer schema: cycle_break_targets() emits primary_break_target.
            "cycle_break_targets": [
                {"primary_break_target": "break_target", "cycle_length": 2}
            ],
        }

    def _gap(self, ids=("cited_row", "pending_row")):
        return {"entries": [{"claim_id": cid} for cid in ids]}

    def _manifest(self, admitted, pending=()):
        return {"schema_version": 1, "frozen_commit": "abc",
                "admitted": list(admitted), "pending": list(pending)}

    def test_lane_contains_only_admitted_candidates_in_queue_order(self):
        lane = cds.build_lane(self._queue(), self._gap(),
                              self._manifest(["cited_row"]))
        self.assertEqual([e["claim_id"] for e in lane["lane"]], ["cited_row"])
        self.assertEqual(lane["manifest_state"], "ok")
        self.assertIn("break_target", lane["unmanifested_candidates"])
        self.assertIn("pending_row", lane["unmanifested_candidates"])
        self.assertTrue(lane["shadow_only"])

    def test_admitted_break_target_enters_lane_via_real_schema(self):
        lane = cds.build_lane(self._queue(), self._gap(),
                              self._manifest(["cited_row", "break_target"]))
        self.assertEqual([e["claim_id"] for e in lane["lane"]],
                         ["cited_row", "break_target"])
        self.assertTrue(lane["lane"][1]["is_primary_cycle_break_target"])

    def test_manifest_pending_add_reported_not_laned(self):
        lane = cds.build_lane(
            self._queue(), self._gap(),
            self._manifest(["cited_row"],
                           pending=[{"claim_id": "pending_row",
                                     "first_report_date": "2026-07-16",
                                     "action": "add"}]))
        self.assertEqual([e["claim_id"] for e in lane["lane"]], ["cited_row"])
        self.assertEqual(lane["pending_adds"][0]["claim_id"], "pending_row")
        self.assertNotIn("pending_row", lane["unmanifested_candidates"])

    def test_manifest_pending_removal_stays_laned_but_named(self):
        lane = cds.build_lane(
            self._queue(), self._gap(),
            self._manifest(["cited_row"],
                           pending=[{"claim_id": "cited_row",
                                     "first_report_date": "2026-07-16",
                                     "action": "remove"}]))
        row = next(e for e in lane["lane"] if e["claim_id"] == "cited_row")
        self.assertTrue(row["pending_removal"])
        self.assertEqual(lane["pending_removes"][0]["claim_id"], "cited_row")

    def test_pending_entry_without_action_is_malformed(self):
        lane = cds.build_lane(
            self._queue(), self._gap(),
            self._manifest(["cited_row"],
                           pending=[{"claim_id": "x",
                                     "first_report_date": "2026-07-16"}]))
        self.assertEqual(lane["manifest_state"], "manifest_pending_entry_malformed")
        self.assertEqual(lane["lane_size"], 0)

    def test_missing_manifest_yields_empty_lane_with_state(self):
        lane = cds.build_lane(self._queue(), self._gap(), None)
        self.assertEqual(lane["lane_size"], 0)
        self.assertEqual(lane["manifest_state"], "manifest_missing_or_unreadable")

    def test_malformed_manifest_rejected(self):
        lane = cds.build_lane(
            self._queue(), self._gap(),
            {"schema_version": 1, "frozen_commit": "abc",
             "admitted": ["cited_row"],
             "pending": [{"claim_id": "x", "action": "add"}]})  # no date
        self.assertEqual(lane["lane_size"], 0)
        self.assertEqual(lane["manifest_state"], "manifest_pending_entry_malformed")

    def test_missing_gap_flagged_and_targets_only(self):
        lane = cds.build_lane(self._queue(), None,
                              self._manifest(["break_target"]))
        self.assertFalse(lane["gap_available"])
        self.assertEqual([e["claim_id"] for e in lane["lane"]], ["break_target"])

    def test_admitted_absent_measured_against_lane_candidates(self):
        # ghost_row is admitted but neither cited nor a target; cited-but-not-
        # pending ids are also absent from LANE candidates by construction.
        lane = cds.build_lane(self._queue(), self._gap(),
                              self._manifest(["cited_row", "ghost_row"]))
        self.assertEqual(lane["admitted_absent_from_lane_candidates"],
                         ["ghost_row"])


class GoldenQueueInvarianceTest(unittest.TestCase):
    """Shadow tagging must not change queue membership or order: run main()
    on a fixture ledger and compare against the documented sort applied to
    the same rows with the shadow tags stripped."""

    def test_membership_and_order_unchanged_by_shadow_tags(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            rows = {
                # cond_parked and plain_high compete in the SAME
                # (criticality, ready) band: a shadow-derived sort term would
                # reorder them (parked row has HIGHER descendants, so the
                # documented key puts it FIRST; any would_park-aware term
                # would flip that).
                "cond_parked": {"audit_status": "audited_conditional",
                                "criticality": "high", "deps": [],
                                "transitive_descendants": 4,
                                "load_bearing_score": 0.5,
                                "note_path": "docs/B.md",
                                "audit_state_snapshot": {
                                    "schema": "blocker_fingerprint_v1",
                                    "dep_effective_status": {},
                                    "dep_claim_type": {},
                                    "dep_claim_scope": {},
                                    "dep_axiom_premise_note_hash": {},
                                    "helper_runner_hashes": {},
                                    "runner_cache_state": {},
                                    "artifact_classifier_state": {},
                                    "policy_versions": {},
                                    "premise_registry_epoch": 1}},
                "plain_high": {"audit_status": "unaudited",
                               "criticality": "high", "deps": [],
                               "transitive_descendants": 2,
                               "load_bearing_score": 0.9,
                               "note_path": "docs/D.md"},
                "crit_ready": {"audit_status": "unaudited", "criticality": "critical",
                               "deps": [], "transitive_descendants": 3,
                               "load_bearing_score": 1.0, "note_path": "docs/A.md"},
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
            # literal same-band expectation: any shadow-derived sort term
            # between readiness and descendants would flip these two.
            self.assertEqual(
                [g[0] for g in got],
                ["crit_ready", "cond_parked", "plain_high", "leaf_row"],
            )
            self.assertEqual({g[0] for g in got}, set(rows))
            cond = next(e for e in queue["queue"] if e["claim_id"] == "cond_parked")
            self.assertTrue(cond["would_park"])  # v1-complete + unmoved dep


if __name__ == "__main__":
    unittest.main()
