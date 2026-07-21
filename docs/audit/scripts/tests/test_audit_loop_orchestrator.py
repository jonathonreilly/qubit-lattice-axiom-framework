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
        max_workers=10,
        max_passes=0,
        max_lane_cycles=0,
        batch_rounds=6,
        stall_minutes=45,
        runner_timeout_sec=120,
        codex_timeout_sec=2700,
        push_retries=3,
        dispatch_science_fixes=False,
        skip_forensic_canary=True,
        dry_run=False,
    )


class WorkerDefaultTest(unittest.TestCase):
    def test_top_level_loop_defaults_to_ten_parallel_workers(self):
        args = audit_loop.build_parser().parse_args([])
        self.assertEqual(args.max_workers, 10)

    def test_standalone_batch_defaults_to_ten_parallel_workers(self):
        args = batch.build_parser().parse_args(["--claims", "row"])
        self.assertEqual(args.max_workers, 10)

    def test_top_level_loop_propagates_worker_limit_to_batch(self):
        args = _args()
        command = audit_loop.batch_command("lane_a", args)
        worker_flag = command.index("--max-workers")
        self.assertEqual(command[worker_flag + 1], "10")

        args.max_workers = 7
        command = audit_loop.batch_command("lane_a", args)
        worker_flag = command.index("--max-workers")
        self.assertEqual(command[worker_flag + 1], "7")

    def test_batch_selection_fills_ten_worker_capacity(self):
        rows = [
            {"claim_id": f"row-{index}", "criticality": "high"}
            for index in range(11)
        ]
        selected = batch.selected_batch(rows, max_workers=10)
        self.assertEqual([row["claim_id"] for row in selected], [
            f"row-{index}" for index in range(10)
        ])


class BatchExitSemanticsTest(unittest.TestCase):
    def test_judicial_handoff_is_resumable(self):
        report = [{"cid": "row", "result": "judicial_panel_required"}]
        self.assertFalse(batch.report_has_hard_blocker(report))

    def test_validation_failure_remains_hard(self):
        report = [{"cid": "row", "result": "validation_failed"}]
        self.assertTrue(batch.report_has_hard_blocker(report))

    def test_campaign_quarantine_makes_only_its_schema_failures_resumable(self):
        report = [
            {"cid": "quarantined", "result": "validation_failed"},
            {"cid": "quarantined", "result": "schema_invalid_quarantined"},
        ]
        self.assertFalse(batch.report_has_hard_blocker(report))

        report.append({"cid": "other", "result": "validation_failed"})
        self.assertTrue(batch.report_has_hard_blocker(report))

    def test_banked_clean_seat_defers_only_the_invalid_peer(self):
        report = [
            {"cid": "row", "result": "validation_failed"},
            {"cid": "row", "result": "critical_peer_pending"},
            {"cid": "row", "result": "schema_invalid_peer_deferred"},
            {"cid": "row", "result": "audited_clean"},
        ]
        self.assertFalse(batch.report_has_hard_blocker(report))

    def test_science_fix_dispatch_is_a_sidecar_not_an_audit_blocker(self):
        for result in ("science_fix_dispatched", "science_fix_dispatch_failed"):
            with self.subTest(result=result):
                self.assertFalse(
                    batch.report_has_hard_blocker(
                        [{"cid": "repairable", "result": result}]
                    )
                )

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


class SchemaRecoveryTest(unittest.TestCase):
    def test_known_n8_failure_gets_exact_mechanism_repair_guidance(self):
        blob = {
            "no_go_discipline": {
                "N8_cross_cycle_echo": {
                    "echoes": [
                        {
                            "mechanism": "projector-kernel obstruction",
                            "disposition": "paraphrased obstruction",
                        }
                    ]
                }
            }
        }

        guidance = batch.schema_repair_guidance(
            blob,
            "N8 echo 1.disposition must name its indexed mechanism",
        )

        self.assertIn('"projector-kernel obstruction"', guidance)
        self.assertIn("copy the exact mechanism string", guidance)

    def test_campaign_quarantine_persists_exact_failures_once(self):
        report = [
            {
                "cid": "row",
                "pass": 1,
                "result": "validation_failed",
                "detail": "N8 exact validator error",
            }
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quarantine.jsonl"
            batch.persist_campaign_quarantine(path, {"row"}, report)
            batch.persist_campaign_quarantine(path, {"row"}, report)

            records = [json.loads(line) for line in path.read_text().splitlines()]

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["claim_id"], "row")
        self.assertEqual(records[0]["failures"][0]["detail"], "N8 exact validator error")

    def test_science_handoff_requires_valid_actionable_verdict(self):
        job = {
            "cid": "row",
            "row": {
                "note_path": "docs/ROW.md",
                "claim_type": "bounded_theorem",
                "transitive_descendants": 7,
            },
        }
        clean = {"audit": {"verdict": "audited_clean"}}
        actionable = {
            "audit": {
                "verdict": "audited_conditional",
                "claim_type": "bounded_theorem",
                "claim_scope": "The asserted bound under stated inputs.",
                "load_bearing_step_class": "B",
                "notes_for_re_audit_if_any": (
                    "missing_bridge_theorem — prove the missing implication"
                ),
                "verdict_rationale": "The implication is only asserted.",
                "load_bearing_step": "Therefore the bound follows.",
                "audit_invocation_id": "a" * 32,
            }
        }

        self.assertIsNone(batch.science_fix_handoff(job, clean))
        handoff = batch.science_fix_handoff(job, actionable)
        self.assertIsNotNone(handoff)
        self.assertEqual(
            handoff["category"],
            "conditional_missing_bridge_theorem",
        )
        self.assertIn("prove the missing implication", handoff["repair_target"])
        self.assertNotIn("prompt_body", handoff)

        for verdict in (
            "audited_failed",
            "audited_renaming",
            "audited_numerical_match",
        ):
            incomplete = {"audit": dict(actionable["audit"], verdict=verdict)}
            incomplete["audit"]["verdict_rationale"] = ""
            with self.subTest(verdict=verdict):
                self.assertIsNone(batch.science_fix_handoff(job, incomplete))

    def test_batch_emits_handoff_only_after_validated_verdict_applies(self):
        job = {
            "cid": "row",
            "pass": 1,
            "row": {
                "claim_id": "row",
                "note_path": "docs/ROW.md",
                "claim_type": "bounded_theorem",
                "criticality": None,
            },
        }
        envelope = {
            "audit": {
                "verdict": "audited_failed",
                "claim_type": "bounded_theorem",
                "claim_scope": "The central equality in this note.",
                "verdict_rationale": "The central equality is contradicted.",
                "load_bearing_step": "The claimed equality holds.",
                "load_bearing_step_class": "B",
                "notes_for_re_audit_if_any": "Replace the false equality.",
                "audit_invocation_id": "c" * 32,
            }
        }
        with mock.patch.object(
            batch,
            "finalize_worker",
            return_value=(envelope, {"result": "delivery_validated"}),
        ), mock.patch.object(
            batch,
            "apply_one_serialized",
            return_value=(True, {"cid": "row", "result": "audited_failed"}),
        ):
            ok, _, quarantines, handoffs = batch.apply_serialized([job], [])

        self.assertTrue(ok)
        self.assertEqual(quarantines, set())
        self.assertEqual([row["claim_id"] for row in handoffs], ["row"])

    def test_banked_clean_seat_does_not_quarantine_whole_claim(self):
        row = {
            "claim_id": "row",
            "note_path": "docs/ROW.md",
            "claim_type": "bounded_theorem",
            "criticality": "critical",
            "audit_status": "unaudited",
            "cross_confirmation": None,
        }
        jobs = [
            {"cid": "row", "pass": 1, "row": row},
            {"cid": "row", "pass": 2, "row": row},
        ]

        def finalize(job):
            if job["pass"] == 1:
                return {"audit": {"verdict": "audited_clean"}}, {"ok": True}
            return None, {
                "cid": "row",
                "pass": 2,
                "result": "validation_failed",
                "detail": "N8 exact validator error",
            }

        report = []
        with mock.patch.object(batch, "finalize_worker", side_effect=finalize), \
                mock.patch.object(
                    batch,
                    "apply_one_serialized",
                    return_value=(True, {"cid": "row", "result": "audited_clean"}),
                ):
            ok, _, quarantines, _ = batch.apply_serialized(jobs, report)

        self.assertTrue(ok)
        self.assertEqual(quarantines, set())
        self.assertIn(
            "schema_invalid_peer_deferred",
            {item["result"] for item in report},
        )

    def test_dispatch_serializes_one_handoff_and_starts_detached_worker(self):
        handoff = {
            "claim_id": "row",
            "category": "failed",
            "note_path": "docs/ROW.md",
            "descendants": 0,
            "cls": "(B)",
            "audit_invocation_id": "d" * 32,
            "audit_verdict": "audited_failed",
            "claim_type": "bounded_theorem",
            "claim_scope": "The central equality.",
            "verdict_rationale": "The equality is contradicted.",
            "load_bearing_step": "The claimed equality holds.",
            "repair_target": "Replace the false equality.",
        }
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(
            batch.subprocess,
            "Popen",
            return_value=mock.Mock(pid=1234),
        ) as popen:
            launched = batch.launch_science_fix_worker([handoff], Path(tmp))
            payload = json.loads(launched[1].read_text(encoding="utf-8"))

        self.assertEqual(launched[0], 1234)
        self.assertEqual(payload["schema"], "audit_science_fix_handoff_v1")
        self.assertEqual(payload["rows"][0]["claim_id"], "row")
        self.assertTrue(popen.call_args.kwargs["start_new_session"])
        self.assertIn("--retry-failed", popen.call_args.args[0])


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

    def test_inner_batches_share_campaign_quarantine_and_dispatch_policy(self):
        args = _args()
        args.campaign_quarantine_file = Path("/tmp/campaign/quarantine.jsonl")

        command = audit_loop.batch_command("lane_a", args)

        self.assertIn("--campaign-quarantine-file", command)
        self.assertIn(str(args.campaign_quarantine_file), command)
        self.assertNotIn("--dispatch-science-fixes", command)

        args.dispatch_science_fixes = True
        self.assertIn(
            "--dispatch-science-fixes",
            audit_loop.batch_command("lane_a", args),
        )


if __name__ == "__main__":
    unittest.main()
