"""Seat-blocked judicial rows: projection, auto-unfreeze, memo shape."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from orchestrate_judicial_panel import (
    seat_blocked_projection,
    seat_context_error,
    write_seat_blocked_memo,
)
import orchestrate_judicial_panel as panel


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
        "claim_scope": "s",
        "claim_type": "positive_theorem",
    }


GOOD_SEAT = {"verdict_rationale": "full reasoning", "audit_invocation_id": "inv-1"}
BARE_SEAT = {"verdict_rationale": "", "audit_invocation_id": "inv-2"}


class SeatBlockedProjectionTest(unittest.TestCase):
    def test_missing_rationale_blocks_and_archived_rationale_unblocks(self):
        rows = {
            "blocked": _row("blocked", first=BARE_SEAT, second=GOOD_SEAT),
            "recovered": _row(
                "recovered",
                first=BARE_SEAT,
                second=GOOD_SEAT,
                prev=[{"audit_invocation_id": "inv-2", "verdict_rationale": "archived text"}],
            ),
            "healthy": _row("healthy", first=GOOD_SEAT, second=GOOD_SEAT),
            "settled": _row("settled", status="third_confirmed_first",
                            first=BARE_SEAT, second=None),
        }
        blocked = seat_blocked_projection(rows)
        self.assertEqual(sorted(blocked), ["blocked"])
        self.assertIn("first_audit", blocked["blocked"]["detail"])
        self.assertIn("disagreement_fingerprint", blocked["blocked"])
        self.assertIn("rationale-preserving", blocked["blocked"]["repair"])

    def test_missing_seat_summary_blocks(self):
        rows = {"nofirst": _row("nofirst", first=None, second=GOOD_SEAT)}
        blocked = seat_blocked_projection(rows)
        self.assertEqual(sorted(blocked), ["nofirst"])
        self.assertIn("missing", blocked["nofirst"]["detail"])

    def test_projection_matches_seat_context_error(self):
        # The projection must be exactly the disagreement rows where
        # seat_context_error fires — no independent policy.
        rows = {
            "a": _row("a", first=BARE_SEAT, second=GOOD_SEAT),
            "b": _row("b", first=GOOD_SEAT, second=GOOD_SEAT),
        }
        blocked = seat_blocked_projection(rows)
        for cid, row in rows.items():
            self.assertEqual(cid in blocked, seat_context_error(row) is not None)

    def test_memo_write_is_deterministic_projection(self):
        import tempfile
        from unittest import mock

        rows = {"blocked": _row("blocked", first=BARE_SEAT, second=GOOD_SEAT)}
        blocked = seat_blocked_projection(rows)
        with tempfile.TemporaryDirectory() as tmp:
            memo = Path(tmp) / "judicial_seat_blocked.json"
            with mock.patch.object(
                panel, "_seat_blocked_memo_path", lambda: memo
            ):
                write_seat_blocked_memo(blocked)
                first = memo.read_bytes()
                write_seat_blocked_memo(blocked)
                second = memo.read_bytes()
        self.assertEqual(first, second)
        payload = json.loads(first)
        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(sorted(payload["rows"]), ["blocked"])
        # Empty projection empties the memo (auto-unfreeze), never deletes it.
        with tempfile.TemporaryDirectory() as tmp:
            memo = Path(tmp) / "judicial_seat_blocked.json"
            with mock.patch.object(
                panel, "_seat_blocked_memo_path", lambda: memo
            ):
                write_seat_blocked_memo({})
            self.assertEqual(json.loads(memo.read_text())["rows"], {})


if __name__ == "__main__":
    unittest.main()
