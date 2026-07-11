#!/usr/bin/env python3
"""Behavior tests for the science-fix campaign supervisor."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


PROJECT_ROOT = Path(__file__).resolve().parents[4]


def _load_module():
    name = "science_fix_loop_under_test"
    sys.modules.pop(name, None)
    spec = importlib.util.spec_from_file_location(
        name, PROJECT_ROOT / "scripts" / "science_fix_loop.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class ScienceFixLoopTests(unittest.TestCase):
    def setUp(self):
        self.sfl = _load_module()

    def test_transient_failures_are_classified(self):
        self.assertEqual(
            self.sfl.classify_transient_failure(
                stderr="You've hit your usage limit. purchase more credits"
            ),
            "usage_limit",
        )
        self.assertEqual(
            self.sfl.classify_transient_failure(
                stderr="Selected model is at capacity. Please try again"
            ),
            "model_capacity",
        )
        self.assertIsNone(
            self.sfl.classify_transient_failure(stderr="invalid prompt")
        )

    def test_retry_transient_does_not_retry_scientific_punts(self):
        quota = {
            "outcome": "codex_failed",
            "codex_stderr_tail": "ERROR: You've hit your usage limit.",
        }
        self.assertTrue(self.sfl.attempt_is_eligible(quota, False, True))
        self.assertFalse(self.sfl.attempt_is_eligible(
            {"outcome": "no_edits"}, False, True
        ))
        self.assertFalse(self.sfl.attempt_is_eligible(
            {"outcome": "pr_opened"}, True, True
        ))

    def test_transient_stop_releases_only_own_unattempted_rows(self):
        with tempfile.TemporaryDirectory() as td:
            self.sfl.STATE_FILE = Path(td) / "state.json"
            self.sfl._write_state_unlocked({
                "attempts": {
                    "mine": {"outcome": "in_progress", "worker_id": "w1"},
                    "other": {"outcome": "in_progress", "worker_id": "w2"},
                    "done": {"outcome": "pr_opened", "worker_id": "w1"},
                }
            })
            released = self.sfl.release_unattempted_claims([
                {"claim_id": "mine"},
                {"claim_id": "other"},
                {"claim_id": "done"},
            ], "w1")
            state = self.sfl._read_state_unlocked()["attempts"]
        self.assertEqual(released, 1)
        self.assertNotIn("mine", state)
        self.assertIn("other", state)
        self.assertIn("done", state)

    def test_clean_worktree_recovers_nested_worker_pr(self):
        branch_result = SimpleNamespace(stdout="physics-loop/block01\n")
        gh_result = SimpleNamespace(
            returncode=0,
            stdout=json.dumps([{
                "number": 42,
                "url": "https://example.test/pull/42",
                "state": "OPEN",
                "headRefName": "physics-loop/block01",
            }]),
        )
        with mock.patch.object(self.sfl, "git", return_value=branch_result), \
             mock.patch.object(self.sfl.subprocess, "run", return_value=gh_result):
            pr = self.sfl.find_existing_pr(Path("/tmp/worktree"), "planned")
        self.assertEqual(pr["number"], 42)
        self.assertEqual(pr["state"], "OPEN")


if __name__ == "__main__":
    unittest.main()
