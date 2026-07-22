"""Panel-aware top-level audit-loop orchestration."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
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
        dispatch_science_fixes=False,
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

    def test_invalid_optional_packet_is_dropped_without_completion(self):
        invocation = "a" * 32
        blob = {
            "claim_id": "row",
            "audit_invocation_id": invocation,
            "load_bearing_step": "The bounded implication follows.",
            "load_bearing_step_class": "B",
            "claim_type": "bounded_theorem",
            "claim_scope": "The bounded implication.",
            "chain_closes": False,
            "chain_closure_explanation": "A named wall remains.",
            "verdict": "audited_conditional",
            "verdict_rationale": "The named wall remains open.",
            "negative_assertion_classes": ["bounded_with_named_walls"],
            "notes_for_re_audit_if_any": "scope_too_broad: narrow the claim.",
            "no_go_discipline": {"required": True, "status": "FAIL"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw.json"
            raw.write_text(json.dumps(blob), encoding="utf-8")
            job = {
                "cid": "row",
                "pass": 1,
                "stalled": False,
                "returncode": 0,
                "raw_output": raw,
                "row": {
                    "claim_id": "row",
                    "note_path": "",
                    "claim_type": "bounded_theorem",
                },
                "evidence_manifest": {},
                "invocation_id": invocation,
                "transport_bound": None,
                "auditor": "test-auditor",
                "independence": "cross_family",
                "delivery": root / "delivery.json",
                "workdir": root,
                "isolated": root,
            }
            with mock.patch.object(batch, "packet_completion_pass") as completion:
                envelope, result = batch.finalize_worker(job)

        completion.assert_not_called()
        self.assertIsNone(envelope["audit"]["no_go_discipline"])
        self.assertEqual(
            envelope["audit"]["negative_assertion_classes"],
            ["bounded_with_named_walls"],
        )
        self.assertIn("optional", result["detail"])

    def test_invalid_optional_packet_is_not_dropped_from_clean(self):
        invocation = "b" * 32
        blob = {
            "claim_id": "row",
            "audit_invocation_id": invocation,
            "load_bearing_step": "The exact identity follows.",
            "load_bearing_step_class": "B",
            "claim_type": "bounded_theorem",
            "claim_scope": "The exact identity.",
            "chain_closes": True,
            "chain_closure_explanation": "The calculation closes.",
            "verdict": "audited_clean",
            "verdict_rationale": "The bounded calculation is complete.",
            "negative_assertion_classes": [],
            "notes_for_re_audit_if_any": None,
            "no_go_discipline": {"required": True, "status": "PASS"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw.json"
            raw.write_text(json.dumps(blob), encoding="utf-8")
            job = {
                "cid": "row",
                "pass": 1,
                "stalled": False,
                "returncode": 0,
                "raw_output": raw,
                "row": {
                    "claim_id": "row",
                    "note_path": "",
                    "claim_type": "bounded_theorem",
                },
                "evidence_manifest": {},
                "invocation_id": invocation,
                "transport_bound": None,
                "auditor": "test-auditor",
                "independence": "cross_family",
                "delivery": root / "delivery.json",
                "workdir": root,
                "isolated": root,
            }
            with mock.patch.object(
                batch, "packet_completion_pass", return_value=None
            ) as completion:
                envelope, result = batch.finalize_worker(job)

        completion.assert_called_once()
        self.assertIsNone(envelope)
        self.assertEqual(result["result"], "validation_failed")
        self.assertIn("N1_alternative_routes", result["detail"])

    def test_terminal_verdict_cannot_mix_compute_required(self):
        invocation = "c" * 32
        blob = {
            "claim_id": "row",
            "audit_invocation_id": invocation,
            "load_bearing_step": "The exact identity follows.",
            "load_bearing_step_class": "B",
            "claim_type": "bounded_theorem",
            "claim_scope": "The exact identity.",
            "chain_closes": True,
            "chain_closure_explanation": "The calculation closes.",
            "verdict": "audited_clean",
            "verdict_rationale": "The bounded calculation is complete.",
            "negative_assertion_classes": [],
            "notes_for_re_audit_if_any": None,
            "no_go_discipline": None,
            "compute_required": "run the cached certificate",
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw.json"
            raw.write_text(json.dumps(blob), encoding="utf-8")
            job = {
                "cid": "row",
                "pass": 1,
                "stalled": False,
                "returncode": 0,
                "raw_output": raw,
                "row": {
                    "claim_id": "row",
                    "note_path": "",
                    "claim_type": "bounded_theorem",
                },
                "evidence_manifest": {},
                "invocation_id": invocation,
                "transport_bound": None,
                "auditor": "test-auditor",
                "independence": "cross_family",
                "delivery": root / "delivery.json",
                "workdir": root,
                "isolated": root,
            }
            with mock.patch.object(batch, "packet_completion_pass") as completion:
                envelope, result = batch.finalize_worker(job)

        completion.assert_not_called()
        self.assertIsNone(envelope)
        self.assertEqual(result["result"], "validation_failed")
        self.assertIn("compute_required cannot accompany", result["detail"])

    def test_dep_ready_post_verdict_reset_is_persisted_across_batches(self):
        selected = [{"claim_id": "row"}]
        current = {
            "row": {
                "claim_id": "row",
                "audit_status": "unaudited",
                "previous_audits": [
                    {"invalidation_reason": "no_go_discipline_packet_missing"}
                ],
            }
        }
        report = [
            {
                "cid": "row",
                "result": "audited_conditional",
                "commit": "deadbeef",
            }
        ]
        with mock.patch.object(batch, "compute_targets", return_value=([current["row"]], [])):
            reentries = batch.blocked_row_reentries(selected, current, report)

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "campaign-row-exclusions.jsonl"
            batch.persist_blocked_row_reentries(path, reentries)
            batch.persist_blocked_row_reentries(path, reentries)
            records = [json.loads(line) for line in path.read_text().splitlines()]
            loaded = batch.load_campaign_quarantine(path)

        self.assertEqual(
            reentries, {"row": "no_go_discipline_packet_missing"}
        )
        self.assertEqual(loaded, {"row"})
        self.assertEqual(len(records), 1)
        self.assertEqual(
            records[0]["reason"], batch.BLOCKED_ROW_QUARANTINE_RESULT
        )
        self.assertEqual(
            report[-1]["result"], batch.BLOCKED_ROW_QUARANTINE_RESULT
        )

    def test_banked_clean_seat_remains_eligible_for_second_pass(self):
        selected = [{"claim_id": "row"}]
        current = {
            "row": {
                "claim_id": "row",
                "audit_status": "audit_in_progress",
                "cross_confirmation": {"status": "awaiting_second"},
            }
        }
        report = [
            {"cid": "row", "result": "audited_clean", "commit": "deadbeef"}
        ]
        with mock.patch.object(batch, "compute_targets") as compute_targets:
            reentries = batch.blocked_row_reentries(selected, current, report)

        self.assertEqual(reentries, {})
        compute_targets.assert_not_called()

    def test_two_batches_exclude_reset_row_and_continue_other_seats(self):
        def row(
            cid: str,
            *,
            audit_status: str = "unaudited",
            criticality: str | None = None,
            cross_status: str | None = None,
            previous_audits: list[dict] | None = None,
            effective_status: str = "ready_for_audit",
        ) -> dict:
            return {
                "claim_id": cid,
                "note_path": f"docs/nonexistent-{cid}.md",
                "claim_type": "positive_theorem",
                "criticality": criticality,
                "audit_status": audit_status,
                "effective_status": effective_status,
                "cross_confirmation": (
                    {"status": cross_status} if cross_status else None
                ),
                "deps": [],
                "previous_audits": previous_audits or [],
            }

        blocked_before = row("blocked")
        other_before = row("other")
        second_before = row(
            "second",
            audit_status="audit_in_progress",
            criticality="critical",
            cross_status="awaiting_second",
        )
        first_rows = {
            item["claim_id"]: item
            for item in (blocked_before, other_before, second_before)
        }
        blocked_after = row(
            "blocked",
            previous_audits=[
                {
                    "audit_status": "audited_conditional",
                    "invalidation_reason": "no_go_discipline_packet_missing",
                }
            ],
        )
        first_after = dict(first_rows, blocked=blocked_after)
        second_after = {
            "blocked": blocked_after,
            "other": row(
                "other",
                audit_status="audited_clean",
                effective_status="retained",
            ),
            "second": row(
                "second",
                audit_status="audited_clean",
                criticality="critical",
                effective_status="retained",
            ),
        }
        launched_by_batch: list[list[tuple[str, int]]] = []

        def run_batch(
            workdir: Path,
            exclusion_file: Path,
            before: dict[str, dict],
            after: dict[str, dict],
            max_workers: int,
        ) -> int:
            launched: list[tuple[str, int]] = []
            launched_by_batch.append(launched)

            def launch_worker(selected, _rows, pass_no, *_args):
                launched.append((selected["claim_id"], pass_no))
                return {
                    "cid": selected["claim_id"],
                    "pass": pass_no,
                    "row": selected,
                }

            def apply_serialized(jobs, report, _retries):
                for job in jobs:
                    report.append(
                        {
                            "cid": job["cid"],
                            "pass": job["pass"],
                            "result": "audited_conditional",
                            "commit": f"commit-{job['cid']}",
                        }
                    )
                return True, set(), set(), []

            argv = [
                "orchestrate_audit_batch.py",
                "--claims",
                "blocked,other,second",
                "--max-workers",
                str(max_workers),
                "--rounds",
                "1",
                "--campaign-quarantine-file",
                str(exclusion_file),
            ]
            lock = mock.Mock()
            with mock.patch.object(sys, "argv", argv), mock.patch.dict(
                os.environ,
                {"AUDIT_BATCH_WORKDIR": str(workdir)},
            ), mock.patch.object(
                batch, "acquire_exclusive_drain_lock", return_value=lock
            ), mock.patch.object(
                batch, "clean_main_error", return_value=None
            ), mock.patch.object(
                batch, "load_rows", side_effect=[before, after]
            ), mock.patch.object(
                batch, "source_requires_forensic", return_value=False
            ), mock.patch.object(
                batch, "launch_worker", side_effect=launch_worker
            ), mock.patch.object(
                batch, "wait_workers"
            ), mock.patch.object(
                batch, "start_progress_ticker"
            ), mock.patch.object(
                batch, "maybe_progress_summary"
            ), mock.patch.object(
                batch, "apply_serialized", side_effect=apply_serialized
            ):
                result = batch.main()
            lock.close.assert_called_once_with()
            return result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            exclusion_file = root / "campaign-row-exclusions.jsonl"
            first_rc = run_batch(
                root / "batch-1",
                exclusion_file,
                first_rows,
                first_after,
                max_workers=1,
            )
            records_after_first = [
                json.loads(line)
                for line in exclusion_file.read_text(encoding="utf-8").splitlines()
            ]
            second_rc = run_batch(
                root / "batch-2",
                exclusion_file,
                first_after,
                second_after,
                max_workers=2,
            )

        self.assertEqual((first_rc, second_rc), (0, 0))
        self.assertEqual(launched_by_batch[0], [("blocked", 1)])
        self.assertNotIn(("blocked", 1), launched_by_batch[1])
        self.assertEqual(
            launched_by_batch[1],
            [("other", 1), ("second", 2)],
        )
        self.assertEqual(len(records_after_first), 1)
        self.assertEqual(records_after_first[0]["claim_id"], "blocked")
        self.assertEqual(
            records_after_first[0]["invalidation_reason"],
            "no_go_discipline_packet_missing",
        )

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
            "apply_claim_serialized",
            return_value=(True, [{"cid": "row", "result": "audited_failed"}]),
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
                    "apply_claim_serialized",
                    return_value=(True, [{"cid": "row", "result": "audited_clean"}]),
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

    def test_missing_dependency_edge_is_dispatched(self):
        job = {
            "cid": "row",
            "row": {
                "note_path": "docs/ROW.md",
                "claim_type": "bounded_theorem",
                "transitive_descendants": 2,
            },
        }
        envelope = {
            "audit": {
                "verdict": "audited_conditional",
                "claim_type": "bounded_theorem",
                "claim_scope": "The bounded implication.",
                "load_bearing_step_class": "B",
                "notes_for_re_audit_if_any": (
                    "missing_dependency_edge: cite the retained authority"
                ),
                "verdict_rationale": "The cited authority is absent.",
                "load_bearing_step": "The implication follows from the authority.",
                "audit_invocation_id": "e" * 32,
            }
        }

        handoff = batch.science_fix_handoff(job, envelope)

        self.assertEqual(
            handoff["category"], "conditional_missing_dependency_edge"
        )


class ClaimTransactionTest(unittest.TestCase):
    def test_wait_workers_streams_complete_claim_before_slower_claim(self):
        class FakeProc:
            def __init__(self, polls):
                self.polls = iter(polls)
                self.returncode = None
                self.pid = 1234

            def poll(self):
                if self.returncode is None:
                    value = next(self.polls)
                    if value is not None:
                        self.returncode = value
                return self.returncode

            def wait(self):
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(cid, polls):
                log_path = root / f"{cid}.log"
                return {
                    "cid": cid,
                    "row": {"claim_id": cid},
                    "pass": 1,
                    "proc": FakeProc(polls),
                    "raw_output": root / f"{cid}.out",
                    "log_path": log_path,
                    "log_handle": log_path.open("w", encoding="utf-8"),
                    "last_size": 0,
                    "last_progress": time.monotonic(),
                    "stalled": False,
                }

            jobs = [job("ready", [0]), job("slow", [None, 0])]
            streamed = []
            with mock.patch.object(batch.time, "sleep", return_value=None):
                result = batch.wait_workers(
                    jobs,
                    stall_minutes=45,
                    on_claim_ready=lambda claim_jobs: (
                        streamed.append(claim_jobs[0]["cid"]) or True
                    ),
                )

        self.assertTrue(result)
        self.assertEqual(streamed, ["ready", "slow"])

    def test_wait_workers_holds_critical_claim_until_both_seats_exit(self):
        class FakeProc:
            def __init__(self, polls):
                self.polls = iter(polls)
                self.returncode = None
                self.pid = 1234

            def poll(self):
                if self.returncode is None:
                    value = next(self.polls)
                    if value is not None:
                        self.returncode = value
                return self.returncode

            def wait(self):
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(pass_no, polls):
                log_path = root / f"critical-{pass_no}.log"
                return {
                    "cid": "critical",
                    "row": {"claim_id": "critical", "criticality": "critical"},
                    "pass": pass_no,
                    "proc": FakeProc(polls),
                    "raw_output": root / f"critical-{pass_no}.out",
                    "log_path": log_path,
                    "log_handle": log_path.open("w", encoding="utf-8"),
                    "last_size": 0,
                    "last_progress": time.monotonic(),
                    "stalled": False,
                }

            jobs = [job(1, [0]), job(2, [None, 0])]
            streamed = []
            with mock.patch.object(batch.time, "sleep", return_value=None):
                result = batch.wait_workers(
                    jobs,
                    on_claim_ready=lambda claim_jobs: (
                        streamed.append(sorted(job["pass"] for job in claim_jobs))
                        or True
                    ),
                )

        self.assertTrue(result)
        self.assertEqual(streamed, [[1, 2]])

    def test_wait_workers_enforces_stall_during_long_callback(self):
        class FakeProc:
            next_pid = 2000

            def __init__(self, done=False):
                self.returncode = 0 if done else None
                self.pid = FakeProc.next_pid
                FakeProc.next_pid += 1

            def poll(self):
                return self.returncode

            def wait(self):
                if self.returncode is None:
                    self.returncode = -9
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(cid, done=False):
                log_path = root / f"{cid}.log"
                log_handle = log_path.open("w", encoding="utf-8")
                os.utime(log_path, (0.0, 0.0))
                return {
                    "cid": cid,
                    "row": {"claim_id": cid},
                    "pass": 1,
                    "proc": FakeProc(done),
                    "raw_output": root / f"{cid}.out",
                    "log_path": log_path,
                    "log_handle": log_handle,
                    "last_size": 0,
                    "last_activity": (0, 0.0),
                    "last_progress": 0.0,
                    "last_progress_wall": 0.0,
                    "stalled": False,
                }

            ready = job("ready", done=True)
            slow = job("slow")
            callback_started = threading.Event()
            release_callback = threading.Event()

            def callback(claim_jobs):
                if claim_jobs[0]["cid"] == "ready":
                    callback_started.set()
                    self.assertTrue(release_callback.wait(timeout=2))
                return True

            with mock.patch.object(
                batch.time, "time", side_effect=[0.0, 3600.0]
            ), mock.patch.object(
                batch.time,
                "sleep",
                side_effect=lambda _seconds: callback_started.wait(timeout=2),
            ), mock.patch.object(
                batch.os,
                "killpg",
                side_effect=lambda _pid, _signal: release_callback.set(),
            ) as killpg:
                result = batch.wait_workers(
                    [ready, slow],
                    stall_minutes=1,
                    on_claim_ready=callback,
                )

        self.assertTrue(result)
        self.assertTrue(slow["stalled"])
        killpg.assert_called_once()

    def test_wait_workers_callback_failure_terminates_remaining_seats(self):
        class FakeProc:
            next_pid = 3000

            def __init__(self, done=False):
                self.returncode = 0 if done else None
                self.pid = FakeProc.next_pid
                FakeProc.next_pid += 1

            def poll(self):
                return self.returncode

            def wait(self):
                if self.returncode is None:
                    self.returncode = -9
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(cid, done=False):
                log_path = root / f"{cid}.log"
                return {
                    "cid": cid,
                    "row": {"claim_id": cid},
                    "pass": 1,
                    "proc": FakeProc(done),
                    "raw_output": root / f"{cid}.out",
                    "log_path": log_path,
                    "log_handle": log_path.open("w", encoding="utf-8"),
                    "last_size": 0,
                    "last_progress": time.monotonic(),
                    "stalled": False,
                }

            ready = job("ready", done=True)
            slow = job("slow")
            with mock.patch.object(batch.os, "killpg") as killpg:
                result = batch.wait_workers(
                    [ready, slow],
                    on_claim_ready=lambda _jobs: False,
                )

        self.assertFalse(result)
        self.assertEqual(slow["returncode"], -9)
        self.assertTrue(all(job["log_handle"].closed for job in (ready, slow)))
        killpg.assert_called_once()

    def test_committer_shell_skips_launch_when_already_cancelled(self):
        cancel = threading.Event()
        cancel.set()
        batch._COMMAND_CONTEXT.cancel_event = cancel
        started = time.monotonic()
        try:
            with mock.patch.object(batch.subprocess, "Popen") as popen:
                result = batch.sh(
                    [sys.executable, "-c", "pass"],
                    timeout=30,
                )
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        popen.assert_not_called()
        self.assertEqual(result.returncode, 125)
        self.assertIn("cancelled", result.stderr)
        self.assertLess(time.monotonic() - started, 3)

    def test_committer_shell_rechecks_cancel_after_short_command(self):
        cancel = threading.Event()
        proc = mock.Mock(returncode=0)
        proc.communicate.side_effect = lambda timeout=None: (
            cancel.set() or "stdout",
            "stderr",
        )
        batch._COMMAND_CONTEXT.cancel_event = cancel
        try:
            with mock.patch.object(batch.subprocess, "Popen", return_value=proc):
                result = batch.sh(["quick-command"])
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        self.assertEqual(result.returncode, 125)
        self.assertEqual(result.stdout, "stdout")
        self.assertEqual(result.stderr, "stderr")

    def test_committer_shell_preserves_normal_short_command_result(self):
        cancel = threading.Event()
        proc = mock.Mock(returncode=7)
        proc.communicate.return_value = ("stdout", "stderr")
        batch._COMMAND_CONTEXT.cancel_event = cancel
        try:
            with mock.patch.object(batch.subprocess, "Popen", return_value=proc):
                result = batch.sh(["quick-command"])
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        self.assertEqual(result.returncode, 7)
        self.assertEqual(result.stdout, "stdout")
        self.assertEqual(result.stderr, "stderr")

    def test_rollback_commands_bypass_committer_cancellation(self):
        reset = mock.Mock(returncode=0, stdout="", stderr="")
        branch = mock.Mock(returncode=0, stdout="main\n", stderr="")
        status = mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(
            batch, "sh", side_effect=[reset, branch, status]
        ) as sh:
            ok, detail = batch.reset_to_origin_main()

        self.assertTrue(ok, detail)
        self.assertEqual(sh.call_count, 3)
        self.assertTrue(
            all(call.kwargs.get("honor_cancel") is False for call in sh.call_args_list)
        )

    def test_verdict_only_path_allowlist_is_narrower_than_commit_allowlist(self):
        self.assertTrue(
            batch.verdict_only_generated_path(
                "docs/audit/data/ledger/ro/row.json"
            )
        )
        self.assertTrue(
            batch.verdict_only_generated_path(
                "docs/publication/ci3_z3/RESULTS_INDEX_EFFECTIVE_STATUS.md"
            )
        )
        self.assertFalse(
            batch.verdict_only_generated_path(
                "docs/audit/data/lane_certification_config.json"
            )
        )
        self.assertFalse(
            batch.verdict_only_generated_path(
                "docs/audit/scripts/audit_lint.py"
            )
        )

    def test_verdict_only_eligibility_rejects_cache_hash_mismatch(self):
        checkpoint = "c" * 40
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "docs" / "audit" / "data"
            data.mkdir(parents=True)
            for name in batch.static_checkpoint.STATIC_CACHE_NAMES:
                (data / name).write_text("{}", encoding="utf-8")
            checkpoint_path = data / "static_pipeline_checkpoint.json"
            checkpoint_path.write_text(
                json.dumps({
                    "schema": batch.static_checkpoint.FINAL_SCHEMA,
                    "static_cache_sha256": {
                        name: hashlib.sha256(b"{}").hexdigest()
                        for name in batch.static_checkpoint.STATIC_CACHE_NAMES
                    },
                    "static_input_sha256": checkpoint,
                }),
                encoding="utf-8",
            )
            (data / "runner_classification.json").write_text(
                '{"stale": true}', encoding="utf-8"
            )
            with mock.patch.object(
                batch.static_checkpoint, "REPO_ROOT", root
            ), mock.patch.object(
                batch.static_checkpoint, "DATA", data
            ), mock.patch.object(
                batch.static_checkpoint, "CHECKPOINT", checkpoint_path
            ):
                eligible, detail = batch.verdict_only_pipeline_eligibility()

        self.assertFalse(eligible)
        self.assertIn("do not match", detail)

    def test_verdict_only_eligibility_rejects_git_inspection_failure(self):
        with mock.patch.object(
            batch.static_checkpoint,
            "verify_checkpoint",
            return_value=(False, "git diff --name-only failed"),
        ):
            eligible, detail = batch.verdict_only_pipeline_eligibility()

        self.assertFalse(eligible)
        self.assertIn("git diff", detail)

    def test_checkpoint_worktree_inspection_fails_closed(self):
        failed = mock.Mock(returncode=128, stdout="", stderr="index failure")
        with mock.patch.object(
            batch.static_checkpoint, "run_git", return_value=failed
        ):
            fingerprint, detail = (
                batch.static_checkpoint.static_input_fingerprint()
            )

        self.assertIsNone(fingerprint)
        self.assertIn("failed", detail)

    def test_static_checkpoint_end_to_end_accepts_only_audit_row_delta(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def git(*args):
                return subprocess.run(
                    ["git", *args],
                    cwd=root,
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout.strip()

            git("init", "-q")
            git("config", "user.email", "checkpoint-test@example.invalid")
            git("config", "user.name", "Checkpoint Test")
            (root / ".gitignore").write_text(
                "docs/audit/data/citation_graph.json\n"
                "docs/audit/data/runner_classification.json\n"
                "docs/audit/data/static_pipeline_checkpoint.json\n"
                "docs/audit/data/static_pipeline_receipt_*.json\n"
                "docs/audit/data/ledger/hidden/\n"
                "docs/ignored_local_note.md\n"
                "scripts/ignored_*.py\n",
                encoding="utf-8",
            )
            data = root / "docs" / "audit" / "data"
            shard = data / "ledger" / "ro" / "row.json"
            shard.parent.mkdir(parents=True)
            ignored_note = root / "docs" / "ignored_local_note.md"
            ignored_note.parent.mkdir(parents=True, exist_ok=True)
            ignored_note.write_text("# Local graph input\n", encoding="utf-8")
            ignored_runner = root / "scripts" / "ignored_runner.py"
            ignored_runner.parent.mkdir(parents=True)
            ignored_runner.write_text("assert True\n", encoding="utf-8")
            ignored_helper = root / "scripts" / "ignored_helper.py"
            ignored_helper.write_text("VALUE = 1\n", encoding="utf-8")
            before = {
                "claim_id": "row",
                "deps": ["dep"],
                "runner_path": "scripts/ignored_runner.py",
                "helper_runner_paths": ["scripts/ignored_helper.py"],
                "audit_status": "unaudited",
            }
            shard.write_text(json.dumps(before), encoding="utf-8")
            ignored_ledger = data / "ledger" / "hidden" / "row.json"
            ignored_ledger.parent.mkdir(parents=True)
            ignored_ledger.write_text(
                json.dumps({"claim_id": "hidden", "deps": ["a"]}),
                encoding="utf-8",
            )
            ignored_ledger_sidecar = ignored_ledger.with_suffix(".sidecar")
            ignored_ledger_sidecar.write_text("one\n", encoding="utf-8")
            git("add", ".gitignore", str(shard.relative_to(root)))
            git("commit", "-qm", "baseline")

            for name in batch.static_checkpoint.STATIC_CACHE_NAMES:
                content = f"{{\"cache\": \"{name}\"}}\n".encode()
                (data / name).write_bytes(content)
            checkpoint = data / "static_pipeline_checkpoint.json"

            nonce = "a" * 32
            with mock.patch.object(
                batch.static_checkpoint, "REPO_ROOT", root
            ), mock.patch.object(
                batch.static_checkpoint, "DATA", data
            ), mock.patch.object(
                batch.static_checkpoint, "CHECKPOINT", checkpoint
            ), mock.patch.dict(
                os.environ,
                {batch.static_checkpoint.BUILD_NONCE_ENV: nonce},
            ):
                began, begin_detail = batch.static_checkpoint.begin_checkpoint()
                stale_prepare_ok, stale_prepare_detail = (
                    batch.static_checkpoint.prepare_checkpoint()
                )
                graph_receipt_ok, graph_receipt_detail = (
                    batch.static_checkpoint.record_producer_receipt(
                        "citation_graph"
                    )
                )
                seed_receipt_ok, seed_receipt_detail = (
                    batch.static_checkpoint.record_producer_receipt(
                        "seed_ledger"
                    )
                )
                prepared, prepare_detail = (
                    batch.static_checkpoint.prepare_checkpoint()
                )
                classifier_receipt_ok, classifier_receipt_detail = (
                    batch.static_checkpoint.record_producer_receipt(
                        "runner_classification"
                    )
                )
                captured, capture_detail = (
                    batch.static_checkpoint.capture_checkpoint()
                )
                finalized, finalize_detail = (
                    batch.static_checkpoint.finalize_checkpoint()
                )
                receipts_cleaned = not list(
                    data.glob("static_pipeline_receipt_*.json")
                )
                shard.write_text(
                    json.dumps(dict(before, audit_status="audited_clean")),
                    encoding="utf-8",
                )
                audit_ok, _ = batch.static_checkpoint.verify_checkpoint()
                with mock.patch.dict(
                    os.environ,
                    {batch.static_checkpoint.EXPECTED_NONCE_ENV: "b" * 32},
                ):
                    wrong_identity_ok, wrong_identity_detail = (
                        batch.static_checkpoint.verify_checkpoint()
                    )
                ignored_note.write_text(
                    "# Changed local graph input\n", encoding="utf-8"
                )
                ignored_note_ok, ignored_note_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_note.write_text(
                    "# Local graph input\n", encoding="utf-8"
                )
                ignored_runner.write_text("assert False\n", encoding="utf-8")
                ignored_runner_ok, ignored_runner_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_runner.write_text("assert True\n", encoding="utf-8")
                ignored_helper.write_text("VALUE = 2\n", encoding="utf-8")
                ignored_helper_ok, ignored_helper_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_helper.write_text("VALUE = 1\n", encoding="utf-8")
                ignored_ledger.write_text(
                    json.dumps({"claim_id": "hidden", "deps": ["b"]}),
                    encoding="utf-8",
                )
                ignored_ledger_ok, ignored_ledger_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_ledger.write_text(
                    json.dumps({"claim_id": "hidden", "deps": ["a"]}),
                    encoding="utf-8",
                )
                ignored_ledger_sidecar.write_text("two\n", encoding="utf-8")
                ignored_sidecar_ok, ignored_sidecar_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_ledger_sidecar.write_text("one\n", encoding="utf-8")
                shard.write_text(
                    json.dumps(dict(before, novel_topology={"edge": "new"})),
                    encoding="utf-8",
                )
                unknown_field_ok, unknown_field_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                shard.write_text(json.dumps(before), encoding="utf-8")
                ledger_sidecar = shard.parent / "topology.sidecar"
                ledger_sidecar.write_text("new topology\n", encoding="utf-8")
                ledger_sidecar_ok, ledger_sidecar_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ledger_sidecar.unlink()
                shard.write_text(
                    json.dumps(dict(before, deps=["rewired"])),
                    encoding="utf-8",
                )
                topology_ok, detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )

        self.assertTrue(began, begin_detail)
        self.assertFalse(stale_prepare_ok)
        self.assertIn("producer receipt", stale_prepare_detail)
        self.assertTrue(graph_receipt_ok, graph_receipt_detail)
        self.assertTrue(seed_receipt_ok, seed_receipt_detail)
        self.assertTrue(prepared, prepare_detail)
        self.assertTrue(classifier_receipt_ok, classifier_receipt_detail)
        self.assertTrue(captured, capture_detail)
        self.assertTrue(finalized, finalize_detail)
        self.assertTrue(receipts_cleaned)
        self.assertTrue(audit_ok)
        self.assertFalse(wrong_identity_ok)
        self.assertIn("changed during fast use", wrong_identity_detail)
        self.assertFalse(ignored_note_ok)
        self.assertIn("static repository inputs changed", ignored_note_detail)
        self.assertFalse(ignored_runner_ok)
        self.assertIn("static repository inputs changed", ignored_runner_detail)
        self.assertFalse(ignored_helper_ok)
        self.assertIn("static repository inputs changed", ignored_helper_detail)
        self.assertFalse(ignored_ledger_ok)
        self.assertIn("static repository inputs changed", ignored_ledger_detail)
        self.assertFalse(ignored_sidecar_ok)
        self.assertIn("static repository inputs changed", ignored_sidecar_detail)
        self.assertFalse(unknown_field_ok)
        self.assertIn("static repository inputs changed", unknown_field_detail)
        self.assertFalse(ledger_sidecar_ok)
        self.assertIn("static repository inputs changed", ledger_sidecar_detail)
        self.assertFalse(topology_ok)
        self.assertIn("static repository inputs changed", detail)

    def test_run_generated_gates_selects_verdict_only_pipeline(self):
        completed = mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(
            batch,
            "verdict_only_pipeline_eligibility",
            return_value=(True, "safe"),
        ), mock.patch.object(batch, "changed_paths", return_value=[]), \
             mock.patch.object(batch, "sh", return_value=completed) as sh:
            ok, detail = batch.run_generated_gates()

        self.assertTrue(ok)
        self.assertEqual(detail, "gates passed")
        self.assertEqual(
            sh.call_args_list[0].args[0],
            ["bash", str(batch.SCRIPTS / "run_pipeline.sh"), "--verdict-only"],
        )

    def test_run_generated_gates_falls_back_to_full_pipeline(self):
        completed = mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(
            batch,
            "verdict_only_pipeline_eligibility",
            return_value=(False, "source changed"),
        ), mock.patch.object(batch, "changed_paths", return_value=[]), \
             mock.patch.object(batch, "sh", return_value=completed) as sh:
            ok, detail = batch.run_generated_gates()

        self.assertTrue(ok)
        self.assertEqual(detail, "gates passed")
        self.assertEqual(
            sh.call_args_list[0].args[0],
            ["bash", str(batch.SCRIPTS / "run_pipeline.sh")],
        )

    def test_two_seats_share_pipeline_commit_and_push(self):
        row = {"claim_id": "critical", "criticality": "critical"}
        deliveries = [
            (
                {"cid": "critical", "pass": seat, "row": row},
                {
                    "audit": {"verdict": "audited_clean"},
                    "evidence_manifest": {},
                },
            )
            for seat in (1, 2)
        ]
        pushed = mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(
            batch, "sync_origin_main", return_value=(True, "base")
        ), mock.patch.object(
            batch.audit_runner, "apply_one", return_value=(True, "applied")
        ) as apply_one, mock.patch.object(
            batch, "run_generated_gates", return_value=(True, "gated")
        ) as gates, mock.patch.object(
            batch, "stage_and_commit", return_value=(True, "commit")
        ) as commit, mock.patch.object(batch, "sh", return_value=pushed) as sh:
            ok, results = batch.apply_claim_serialized(deliveries, retries=3)

        self.assertTrue(ok)
        self.assertEqual(apply_one.call_count, 2)
        gates.assert_called_once_with()
        commit.assert_called_once()
        self.assertEqual(sh.call_count, 1)
        self.assertEqual([item["pass"] for item in results], [1, 2])
        self.assertEqual({item["commit"] for item in results}, {"commit"})

    def test_push_race_replays_both_critical_seats_as_one_transaction(self):
        row = {"claim_id": "critical", "criticality": "critical"}
        deliveries = [
            (
                {"cid": "critical", "pass": seat, "row": row},
                {
                    "audit": {"verdict": "audited_clean"},
                    "evidence_manifest": {},
                },
            )
            for seat in (1, 2)
        ]
        commands = [
            mock.Mock(returncode=1, stdout="", stderr="push race"),
            mock.Mock(returncode=0, stdout="", stderr=""),
            mock.Mock(returncode=1, stdout="", stderr="not landed"),
            mock.Mock(returncode=0, stdout="", stderr=""),
        ]
        with mock.patch.object(
            batch, "sync_origin_main", return_value=(True, "base")
        ), mock.patch.object(
            batch.audit_runner, "apply_one", return_value=(True, "applied")
        ) as apply_one, mock.patch.object(
            batch, "run_generated_gates", return_value=(True, "gated")
        ) as gates, mock.patch.object(
            batch,
            "stage_and_commit",
            side_effect=[(True, "commit-1"), (True, "commit-2")],
        ) as commit, mock.patch.object(
            batch, "reset_to_origin_main", return_value=(True, "reset")
        ) as reset, mock.patch.object(
            batch, "sh", side_effect=commands
        ):
            ok, results = batch.apply_claim_serialized(deliveries, retries=2)

        self.assertTrue(ok)
        self.assertEqual(apply_one.call_count, 4)
        self.assertEqual(gates.call_count, 2)
        self.assertEqual(commit.call_count, 2)
        reset.assert_called_once_with()
        self.assertEqual({item["commit"] for item in results}, {"commit-2"})


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
