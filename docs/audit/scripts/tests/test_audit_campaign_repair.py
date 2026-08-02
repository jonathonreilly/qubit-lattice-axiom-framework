"""Repair routing for campaign-scoped audit exclusions."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import audit_campaign_repair as repair


class CampaignRepairTest(unittest.TestCase):
    def test_load_exclusions_rejects_malformed_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "campaign-row-exclusions.jsonl"
            path.write_text('{"claim_id":"row"}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "has no reason"):
                repair.load_exclusions(path)

    def test_routes_operational_exclusions_without_minting_verdicts(self):
        rows = {
            "schema": {
                "audit_status": "unaudited",
                "effective_status": "unaudited",
                "note_path": "docs/schema.md",
            },
            "compute": {
                "audit_status": "unaudited",
                "effective_status": "unaudited",
                "note_path": "docs/compute.md",
                "runner_path": "scripts/compute.py",
            },
            "blocked": {
                "audit_status": "unaudited",
                "effective_status": "unaudited",
                "note_path": "docs/blocked.md",
            },
            "transaction": {
                "audit_status": "unaudited",
                "effective_status": "unaudited",
                "note_path": "docs/transaction.md",
            },
        }
        exclusions = [
            {
                "claim_id": "schema",
                "reason": repair.SCHEMA_QUARANTINE,
                "failures": [{
                    "failure_class": "scientific_reaudit_required",
                }],
            },
            {"claim_id": "compute", "reason": repair.COMPUTE_QUARANTINE},
            {
                "claim_id": "blocked",
                "reason": repair.BLOCKED_REENTRY,
                "invalidation_reason": "classifier_promoted_to_class_A",
            },
            {
                "claim_id": "transaction",
                "reason": repair.TRANSACTION_QUARANTINE,
            },
        ]

        plan = repair.build_plan(exclusions, rows)
        by_claim = {item["claim_id"]: item for item in plan}

        self.assertEqual(
            by_claim["schema"]["route"], "fresh_scientific_seat_required"
        )
        self.assertTrue(by_claim["schema"]["ready_for_new_campaign"])
        self.assertEqual(by_claim["compute"]["route"], "supply_compute_artifact")
        self.assertEqual(
            by_claim["compute"]["command"],
            "python3 scripts/cached_runner_output.py scripts/compute.py",
        )
        self.assertEqual(by_claim["blocked"]["route"], "repair_invalidation_cause")
        self.assertEqual(
            by_claim["blocked"]["invalidation_reason"],
            "classifier_promoted_to_class_A",
        )
        self.assertEqual(
            by_claim["transaction"]["route"], "repair_claim_transaction"
        )
        self.assertTrue(all("audit_status" in item["current"] for item in plan))

    def test_exhausted_packet_completion_does_not_request_full_reaudit(self):
        item = repair.repair_route(
            {
                "claim_id": "row",
                "reason": repair.SCHEMA_QUARANTINE,
                "failures": [{
                    "failure_class": "packet_completion_exhausted",
                    "error_code": "N2_WALL_EVIDENCE_BINDING_MISMATCH",
                }],
            },
            {"audit_status": "unaudited", "effective_status": "unaudited"},
        )

        self.assertEqual(item["route"], "repair_packet_completion_contract")
        self.assertFalse(item["ready_for_new_campaign"])
        self.assertIn("do not spend another full seat", item["action"])

    def test_resolved_blocked_reentry_is_safe_to_reconsider(self):
        item = repair.repair_route(
            {"claim_id": "row", "reason": repair.BLOCKED_REENTRY},
            {"audit_status": "audited_clean", "effective_status": "retained"},
        )

        self.assertEqual(item["route"], "already_moved_out_of_reentry")
        self.assertTrue(item["ready_for_new_campaign"])

    def test_routes_selector_skips_to_their_governed_owners(self):
        rows = {
            "conditional": {
                "audit_status": "audited_conditional",
                "effective_status": "audited_conditional",
            },
            "dependency": {
                "audit_status": "unaudited",
                "effective_status": "retained_pending_chain",
                "deps": ["upstream", "retained_parent"],
            },
            "upstream": {
                "audit_status": "unaudited",
                "effective_status": "unaudited",
            },
            "retained_parent": {
                "audit_status": "audited_clean",
                "effective_status": "retained",
            },
            "forensic": {
                "audit_status": "unaudited",
                "effective_status": "unaudited",
            },
            "hash": {
                "audit_status": "unaudited",
                "effective_status": "unaudited",
            },
        }
        records = [
            {
                "claim_id": "conditional",
                "reason": "awaiting_science_repair",
                "detail": (
                    "awaiting repair (sources and deps unchanged since "
                    "audited_conditional)"
                ),
            },
            {
                "claim_id": "dependency",
                "reason": "dependencies_not_retained",
                "detail": "dependencies are not retained-grade",
            },
            {
                "claim_id": "forensic",
                "reason": "forensic_source_shape",
                "detail": "source shape requires forensic tier",
            },
            {
                "claim_id": "hash",
                "reason": "note_hash_drift",
                "detail": (
                    "ledger note_hash lags the note file; run "
                    "seed_audit_ledger.py + pipeline and commit before auditing"
                ),
            },
        ]

        plan = repair.build_plan(records, rows)
        by_claim = {item["claim_id"]: item for item in plan}

        self.assertEqual(
            by_claim["conditional"]["route"], "validated_science_handoff"
        )
        self.assertEqual(
            by_claim["dependency"]["route"],
            "repair_or_audit_upstream_dependencies",
        )
        self.assertEqual(
            by_claim["dependency"]["blocking_dependencies"], ["upstream"]
        )
        self.assertEqual(by_claim["forensic"]["route"], "forensic_audit")
        self.assertEqual(by_claim["hash"]["route"], "refresh_note_hash_pipeline")

    def test_retained_selector_skip_is_recorded_as_non_actionable(self):
        item = repair.repair_route(
            {
                "claim_id": "retained",
                "reason": "effective_status_not_actionable",
                "detail": (
                    "effective_status=retained - already retained-grade or "
                    "governed"
                ),
            },
            {"audit_status": "audited_clean", "effective_status": "retained"},
        )

        self.assertEqual(item["route"], "already_settled_or_governed")
        self.assertTrue(item["ready_for_new_campaign"])

    def test_campaign_loader_includes_selector_skip_inventory(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repair.batch.persist_campaign_selection_skips(
                workdir / "campaign-selector-skips.jsonl",
                ["row: dependencies are not retained-grade"],
            )

            records = repair.load_campaign_records(workdir)

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["reason"], "dependencies_not_retained")


if __name__ == "__main__":
    unittest.main()
