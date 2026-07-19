"""Panel-aware top-level audit-loop orchestration."""
from __future__ import annotations

import argparse
import sys
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

    def test_batch_hard_failure_stops_before_panel(self):
        args = _args()
        labels: list[str] = []

        def fake_run(label, command, env=None):
            labels.append(label)
            return 1

        with mock.patch.object(audit_loop, "git_head", return_value="h0"), \
             mock.patch.object(audit_loop, "run_command", side_effect=fake_run):
            rc, progressed = audit_loop.drain_lane("lane_a", args)

        self.assertEqual(rc, 1)
        self.assertFalse(progressed)
        self.assertEqual(labels, ["batch-lane_a-cycle-1"])


if __name__ == "__main__":
    unittest.main()
