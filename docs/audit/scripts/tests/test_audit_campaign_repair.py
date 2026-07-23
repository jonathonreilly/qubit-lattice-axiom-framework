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
            with self.assertRaisesRegex(ValueError, "missing reason"):
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
            {"claim_id": "schema", "reason": repair.SCHEMA_QUARANTINE},
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

        self.assertEqual(by_claim["schema"]["route"], "fresh_schema_valid_seat")
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

    def test_resolved_blocked_reentry_is_safe_to_reconsider(self):
        item = repair.repair_route(
            {"claim_id": "row", "reason": repair.BLOCKED_REENTRY},
            {"audit_status": "audited_clean", "effective_status": "retained"},
        )

        self.assertEqual(item["route"], "already_moved_out_of_reentry")
        self.assertTrue(item["ready_for_new_campaign"])


if __name__ == "__main__":
    unittest.main()
