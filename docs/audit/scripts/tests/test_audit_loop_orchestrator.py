"""Panel-aware top-level audit-loop orchestration."""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import orchestrate_audit_batch as batch
import orchestrate_audit_loop as audit_loop


def _args() -> argparse.Namespace:
    return argparse.Namespace(
        lane=None,
        max_workers=4,
        max_passes=0,
        max_lane_cycles=0,
        batch_rounds=6,
        stall_minutes=45,
        runner_timeout_sec=120,
        codex_timeout_sec=2700,
        push_retries=3,
        skip_forensic_canary=True,
        dry_run=False,
    )


class BatchExitSemanticsTest(unittest.TestCase):
    def test_judicial_handoff_is_resumable(self):
        report = [{"cid": "row", "result": "judicial_panel_required"}]
        self.assertFalse(batch.report_has_hard_blocker(report))

    def test_validation_failure_remains_hard(self):
        report = [{"cid": "row", "result": "validation_failed"}]
        self.assertTrue(batch.report_has_hard_blocker(report))

    def test_mixed_failure_records_the_judicial_handoff(self):
        report = [{"cid": "broken", "result": "validation_failed"}]
        selected = [{"claim_id": "disputed"}]
        current = {
            "disputed": {"cross_confirmation": {"status": "disagreement"}}
        }

        disagreements = batch.append_judicial_handoffs(selected, current, report)

        self.assertEqual(disagreements, ["disputed"])
        self.assertIn(
            {"cid": "disputed", "result": "judicial_panel_required"}, report
        )
        self.assertTrue(batch.report_has_hard_blocker(report))


class AutomaticPanelResumeTest(unittest.TestCase):
    def test_disagreement_batch_is_panelled_then_same_lane_resumes(self):
        args = _args()
        # cycle 1 lands the disagreement/panel resolution; cycle 2 reaches
        # the lane fixed point. drain_lane reads HEAD before/after each cycle.
        heads = iter(["h0", "h1", "h1", "h1"])
        labels: list[str] = []

        def fake_run(label, command, env=None):
            labels.append(label)
            return 0

        with mock.patch.object(audit_loop, "git_head", side_effect=lambda: next(heads)), \
             mock.patch.object(audit_loop, "run_command", side_effect=fake_run):
            rc, progressed = audit_loop.drain_lane("lane_a", args)

        self.assertEqual(rc, 0)
        self.assertTrue(progressed)
        self.assertEqual(
            labels,
            [
                "batch-lane_a-cycle-1",
                "panel-after-lane_a-cycle-1",
                "batch-lane_a-cycle-2",
                "panel-after-lane_a-cycle-2",
            ],
        )

    def test_batch_hard_failure_panels_before_stopping(self):
        args = _args()
        labels: list[str] = []

        def fake_run(label, command, env=None):
            labels.append(label)
            return 1 if label.startswith("batch-") else 0

        with mock.patch.object(audit_loop, "git_head", return_value="h0"), \
             mock.patch.object(audit_loop, "run_command", side_effect=fake_run):
            rc, progressed = audit_loop.drain_lane("lane_a", args)

        self.assertEqual(rc, 1)
        self.assertFalse(progressed)
        self.assertEqual(
            labels,
            ["batch-lane_a-cycle-1", "panel-after-lane_a-cycle-1"],
        )


class CampaignContractTest(unittest.TestCase):
    def test_inherited_campaign_lock_is_reentrant_for_child(self):
        held = batch.acquire_exclusive_drain_lock("top-level-test")
        self.assertIsNotNone(held)
        try:
            with mock.patch.dict(
                os.environ,
                {batch.INHERITED_DRAIN_LOCK_FD_ENV: str(held.fileno())},
            ):
                inherited = batch.acquire_exclusive_drain_lock("child-test")
            self.assertIsNotNone(inherited)
            inherited.close()
        finally:
            held.close()

    def test_forensic_selector_uses_canonical_source_predicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            queue = Path(tmp) / "queue.json"
            queue.write_text(
                json.dumps(
                    {
                        "queue": [
                            {
                                "claim_id": "bounded_obstruction",
                                "ready": True,
                                "audit_status": "unaudited",
                                "claim_type": "bounded_theorem",
                                "note_path": "docs/EXAMPLE_OBSTRUCTION_NOTE.md",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with mock.patch.object(audit_loop, "QUEUE", queue), mock.patch.object(
                batch, "source_requires_forensic", return_value=True
            ):
                selected = audit_loop.first_ready_forensic_claim()
        self.assertEqual(selected, "bounded_obstruction")

    def test_unknown_lane_fails_before_opening_panel(self):
        with mock.patch.object(
            audit_loop, "configured_lane_names", return_value=["lane_a"]
        ), mock.patch.object(audit_loop, "run_panel") as run_panel:
            rc = audit_loop.main(
                [
                    "--dry-run",
                    "--skip-forensic-canary",
                    "--lane",
                    "definitely_unknown",
                ]
            )
        self.assertEqual(rc, 2)
        run_panel.assert_not_called()

    def test_verdict_summary_never_rematerializes_ledger_cache(self):
        with mock.patch.object(
            audit_loop, "audit_status_snapshot", return_value={"row": "audited_clean"}
        ), mock.patch.object(batch, "load_rows") as load_rows:
            with mock.patch.dict(
                audit_loop.PROGRESS,
                {"baseline_status": {"row": "audit_in_progress"}},
            ):
                counts = audit_loop.landed_verdict_counts()
        self.assertEqual(counts["audited_clean"], 1)
        load_rows.assert_not_called()


if __name__ == "__main__":
    unittest.main()
