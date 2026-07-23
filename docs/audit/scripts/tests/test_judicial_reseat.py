"""Reseat of seat-blocked judicial disagreements: the audit must FINISH.

A disagreement row whose recorded seats cannot back a valid panel packet is
reseated — broken seats archived with full provenance, row reopened for
fresh cross-confirmation — never frozen and never panel-retried as recorded.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from orchestrate_judicial_panel import (
    RESEAT_REASON,
    reseat_disposition,
    reseat_mutation,
    seat_context_error,
)


def _row(cid, status="disagreement", first=None, second=None, prev=None):
    return {
        "claim_id": cid,
        "cross_confirmation": {
            "status": status,
            "first_audit": first,
            "second_audit": second,
        },
        "previous_audits": prev or [],
        "audit_status": "audit_in_progress",
        "blocker": "cross_confirmation_disagreement",
        "claim_scope": "s",
        "claim_type": "positive_theorem",
        "note_hash": "abc123",
        "verdict_rationale": "in-progress rationale",
    }


GOOD_SEAT = {"verdict_rationale": "full reasoning", "audit_invocation_id": "inv-1"}
BARE_SEAT = {"verdict_rationale": "", "audit_invocation_id": "inv-2"}


class ReseatDispositionTest(unittest.TestCase):
    def test_blocked_resolved_recovered(self):
        blocked = _row("a", first=BARE_SEAT, second=GOOD_SEAT)
        resolved = _row("b", status="third_confirmed_first",
                        first=BARE_SEAT, second=None)
        recovered = _row(
            "c",
            first=BARE_SEAT,
            second=GOOD_SEAT,
            prev=[{"audit_invocation_id": "inv-2", "verdict_rationale": "archived"}],
        )
        self.assertEqual(reseat_disposition(blocked), "blocked")
        self.assertEqual(reseat_disposition(resolved), "resolved")
        self.assertEqual(reseat_disposition(recovered), "recovered")

    def test_disposition_is_exactly_seat_context_error(self):
        # No independent policy: for disagreement rows, blocked <=> the panel's
        # own seat_context_error fires.
        rows = [
            _row("x", first=BARE_SEAT, second=GOOD_SEAT),
            _row("y", first=GOOD_SEAT, second=GOOD_SEAT),
            _row("w", first={"verdict_rationale": "   ",
                             "audit_invocation_id": "inv-9"}, second=GOOD_SEAT),
            _row("z", first=None, second=GOOD_SEAT),
        ]
        for row in rows:
            expected = "blocked" if seat_context_error(row) else "recovered"
            self.assertEqual(reseat_disposition(row), expected, row["claim_id"])


class ReseatMutationTest(unittest.TestCase):
    def test_archives_seats_with_reason_and_reopens_row(self):
        prior_entry = {"audit_invocation_id": "old", "verdict_rationale": "old text"}
        row = _row("a", first=BARE_SEAT, second=GOOD_SEAT, prev=[prior_entry])
        new_row = reseat_mutation(row)
        # Exactly one new archive entry; existing history untouched.
        self.assertEqual(len(new_row["previous_audits"]), 2)
        self.assertEqual(new_row["previous_audits"][0], prior_entry)
        archived = new_row["previous_audits"][-1]
        # The broken seats are preserved verbatim in the archive.
        self.assertEqual(archived["cross_confirmation"]["first_audit"], BARE_SEAT)
        self.assertEqual(archived["cross_confirmation"]["second_audit"], GOOD_SEAT)
        self.assertEqual(archived["audit_status"], "audit_in_progress")
        self.assertEqual(archived["invalidation_reason"], RESEAT_REASON)
        # The row is reopened for fresh seating: no minted verdict.
        self.assertEqual(new_row["audit_status"], "unaudited")
        self.assertIsNone(new_row["cross_confirmation"])
        self.assertIsNone(new_row["blocker"])
        self.assertIsNone(new_row["verdict_rationale"])

    def test_reseated_row_is_no_longer_blocked(self):
        row = _row("a", first=BARE_SEAT, second=GOOD_SEAT)
        new_row = reseat_mutation(row)
        self.assertEqual(reseat_disposition(new_row), "resolved")

    def test_mutation_does_not_share_history_with_input(self):
        row = _row("a", first=BARE_SEAT, second=GOOD_SEAT)
        new_row = reseat_mutation(row)
        self.assertEqual(len(row.get("previous_audits") or []), 0)
        self.assertEqual(len(new_row["previous_audits"]), 1)



class ReseatOutcomeShapeTest(unittest.TestCase):
    def test_gate_failures_return_outcome_dicts_and_ok_set(self):
        from unittest import mock

        import orchestrate_judicial_panel as panel

        with mock.patch.object(
            panel.batch,
            "commit_generated_transaction",
            return_value={
                "ok": False,
                "result": "gate_failed",
                "detail": "pipeline failed: boom",
            },
        ):
            outcome = panel.reseat_blocked_row("row_x", 3)
        self.assertIsInstance(outcome, dict)
        self.assertEqual(outcome["cid"], "row_x")
        self.assertEqual(outcome["result"], "reseat_pipeline_failed")
        self.assertNotIn(outcome["result"], panel.RESEAT_OK_RESULTS)
        for ok in ("reseated", "resolved", "recovered"):
            self.assertIn(ok, panel.RESEAT_OK_RESULTS)

if __name__ == "__main__":
    unittest.main()
