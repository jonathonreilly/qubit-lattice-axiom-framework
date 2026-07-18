"""15-minute drain summary: cadence gating, content, and inertness."""
from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import orchestrate_audit_batch as batch


class _ExplodingProc:
    """The ticker must never touch process objects (a real poll() mutates
    Popen state); any attribute access here fails the test."""

    def __getattr__(self, name):
        raise AssertionError(f"ticker touched proc.{name}")


def _reset(report=None, round_targets=None):
    batch.PROGRESS.update(
        {"t0": None, "last": 0.0, "report": report,
         "round_targets": round_targets, "jobs": None}
    )


def _capture(**kwargs) -> str:
    buf = io.StringIO()
    with redirect_stdout(buf):
        batch.maybe_progress_summary(**kwargs)
    return buf.getvalue()


class DrainProgressSummaryTest(unittest.TestCase):
    def test_first_unforced_call_is_baseline_silent(self):
        _reset(report=[])
        self.assertEqual(_capture(), "")
        # Immediately after baseline, still inside the interval: silent.
        self.assertEqual(_capture(), "")

    def test_interval_gates_and_elapsed_reports(self):
        _reset(report=[{"result": "audited_clean"}, {"result": "audited_clean"},
                       {"result": "validation_failed"}], round_targets=7)
        self.assertEqual(_capture(), "")  # baseline
        batch.PROGRESS["last"] -= 901  # step past the 15-minute window
        batch.PROGRESS["t0"] -= 3900  # pretend 65 minutes elapsed
        out = _capture()
        self.assertIn("== drain summary [1h05m]", out)
        self.assertIn("audited_clean x2", out)
        self.assertIn("validation_failed x1", out)
        self.assertIn("dep-ready at round start: 7", out)
        # And the window re-arms.
        self.assertEqual(_capture(), "")

    def test_force_reports_even_inside_window_and_lists_live_workers(self):
        _reset(report=[], round_targets=None)
        jobs = [
            {"returncode": None, "proc": _ExplodingProc(),
             "row": {"claim_id": "row_a"}, "pass": 1, "started": 0.0},
            {"returncode": 0, "proc": _ExplodingProc(),
             "row": {"claim_id": "row_b"}, "pass": 2, "started": 0.0},
        ]
        out = _capture(jobs=jobs, force=True)
        self.assertIn("active workers: 1", out)
        self.assertIn("row_a#p1", out)
        self.assertNotIn("row_b", out)
        self.assertIn("outcomes so far: none yet", out)
        self.assertNotIn("dep-ready at round start", out)

    def test_registered_jobs_used_when_none_passed(self):
        _reset(report=[])
        batch.PROGRESS["jobs"] = [
            {"returncode": None, "proc": _ExplodingProc(),
             "row": {"claim_id": "row_c"}, "pass": 1, "started": 0.0},
        ]
        out = _capture(force=True)
        self.assertIn("row_c#p1", out)
        batch.PROGRESS["jobs"] = None

    def test_ticker_thread_start_is_idempotent(self):
        before = batch._TICKER_STARTED
        try:
            batch._TICKER_STARTED = True  # never spawn a real thread in tests
            batch.start_progress_ticker()
            batch.start_progress_ticker()
            self.assertTrue(batch._TICKER_STARTED)
        finally:
            batch._TICKER_STARTED = before


if __name__ == "__main__":
    unittest.main()
