"""Regression tests for dependency-aware runner-cache freshness."""

from __future__ import annotations

import sys
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import runner_cache as rc  # noqa: E402
import precompute_audit_runners as precompute  # noqa: E402


class DeclaredInputFreshnessTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        (self.root / "scripts").mkdir()
        (self.root / "docs").mkdir()
        self.runner = "scripts/fixture.py"
        self.source = self.root / "docs" / "source.md"
        self.source.write_text("v1\n", encoding="utf-8")
        (self.root / self.runner).write_text(
            "AUDIT_INPUT_PATHS = ('docs/source.md',)\nprint('PASS')\n",
            encoding="utf-8",
        )
        patcher = mock.patch.multiple(
            rc,
            REPO_ROOT=self.root,
            CACHE_DIR=self.root / "logs" / "runner-cache",
            LIVE_LOG_DIR=self.root / "logs" / "runner-cache" / ".in-progress",
        )
        patcher.start()
        self.addCleanup(patcher.stop)
        precompute_patcher = mock.patch.multiple(
            precompute,
            REPO_ROOT=self.root,
            CACHE_DIR=self.root / "logs" / "runner-cache",
        )
        precompute_patcher.start()
        self.addCleanup(precompute_patcher.stop)
        self.result = {
            "stdout": "PASS\n",
            "stderr": "",
            "timeout_sec": 120,
            "exit_code": 0,
            "elapsed_sec": 0.0,
            "status": "ok",
        }

    def _git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=True,
        )

    def _init_git(self) -> None:
        self._git("init")
        self._git("config", "user.name", "Runner Cache Test")
        self._git("config", "user.email", "runner-cache@example.invalid")
        self._git("add", "scripts/fixture.py", "docs/source.md")
        self._git("commit", "-m", "fixture base")

    def test_declared_input_mutation_invalidates_cache(self) -> None:
        cache = rc.write_cache(self.runner, dict(self.result))
        header = rc.parse_cache_header(cache.read_text(encoding="utf-8"))
        self.assertIsNotNone(header)
        self.assertEqual(
            header["input_fingerprint_sha256"],
            rc.declared_input_fingerprint(self.runner),
        )
        self.assertEqual(rc.cache_status(self.runner), "fresh")
        self.source.write_text("v2\n", encoding="utf-8")
        self.assertEqual(rc.cache_status(self.runner), "input_mismatch")
        self.assertIsNone(rc.cache_excerpt_for_audit(self.runner))

    def test_missing_fingerprint_is_rejected_for_declared_inputs(self) -> None:
        cache = rc.write_cache(self.runner, dict(self.result))
        text = cache.read_text(encoding="utf-8")
        text = "\n".join(
            line for line in text.splitlines()
            if not line.startswith("input_fingerprint_sha256:")
        ) + "\n"
        cache.write_text(text, encoding="utf-8")
        self.assertEqual(rc.cache_status(self.runner), "input_mismatch")

    def test_legacy_runner_without_declaration_remains_sha_pinned(self) -> None:
        (self.root / self.runner).write_text("print('PASS')\n", encoding="utf-8")
        cache = rc.write_cache(self.runner, dict(self.result))
        header = rc.parse_cache_header(cache.read_text(encoding="utf-8"))
        self.assertIsNone(header["input_fingerprint_sha256"])
        self.assertEqual(rc.cache_status(self.runner), "fresh")

    def test_invalid_or_missing_declared_input_cannot_be_cached(self) -> None:
        (self.root / self.runner).write_text(
            "AUDIT_INPUT_PATHS = ('docs/missing.md',)\n",
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            rc.write_cache(self.runner, dict(self.result))

    def test_input_mutation_during_execution_refuses_cache_write(self) -> None:
        before = rc.capture_runner_identity(self.runner)

        def mutate_while_running(_runner: str, timeout_sec: int) -> dict:
            self.source.write_text("v2\n", encoding="utf-8")
            return dict(self.result, timeout_sec=timeout_sec)

        with mock.patch.object(rc, "execute_runner", side_effect=mutate_while_running):
            with self.assertRaises(rc.RunnerIdentityChangedError):
                rc.execute_and_write_cache(self.runner, timeout_sec=120)
        self.assertNotEqual(before, rc.capture_runner_identity(self.runner))
        self.assertFalse(rc.cache_path_for(self.runner).exists())

    def test_input_aba_mutation_during_execution_refuses_cache_write(self) -> None:
        before = rc.capture_runner_identity(self.runner)

        def mutate_read_restore(_runner: str, timeout_sec: int) -> dict:
            self.source.write_text("v2\n", encoding="utf-8")
            observed = self.source.read_text(encoding="utf-8").strip()
            self.source.write_text("v1\n", encoding="utf-8")
            return dict(
                self.result,
                stdout=f"observed={observed}\n",
                timeout_sec=timeout_sec,
            )

        with mock.patch.object(rc, "execute_runner", side_effect=mutate_read_restore):
            with self.assertRaises(rc.RunnerIdentityChangedError):
                rc.execute_and_write_cache(self.runner, timeout_sec=120)
        self.assertEqual(before, rc.capture_runner_identity(self.runner))
        self.assertFalse(rc.cache_path_for(self.runner).exists())

    def test_staged_input_only_change_selects_declaring_runner(self) -> None:
        completed = __import__("subprocess").CompletedProcess(
            args=[], returncode=0, stdout="docs/source.md\n", stderr=""
        )
        with mock.patch.object(
            precompute, "collect_runners_from_ledger", return_value=[self.runner]
        ), mock.patch.object(precompute.subprocess, "run", return_value=completed):
            self.assertEqual(precompute.collect_runners_from_staged(), [self.runner])

    def test_pr_diff_input_only_change_selects_declaring_runner(self) -> None:
        completed = __import__("subprocess").CompletedProcess(
            args=[], returncode=0, stdout="docs/source.md\n", stderr=""
        )
        with mock.patch.object(
            precompute, "collect_runners_from_ledger", return_value=[self.runner]
        ), mock.patch.object(precompute.subprocess, "run", return_value=completed):
            self.assertEqual(
                precompute.collect_runners_from_pr_diff("origin/main"),
                [self.runner],
            )

    def test_real_staged_deletion_selects_declaring_runner(self) -> None:
        self._init_git()
        self.source.unlink()
        self._git("add", "-u", "docs/source.md")
        with mock.patch.object(
            precompute, "collect_runners_from_ledger", return_value=[self.runner]
        ):
            self.assertEqual(precompute.collect_runners_from_staged(), [self.runner])

    def test_real_staged_rename_selects_old_declared_path(self) -> None:
        self._init_git()
        self._git("mv", "docs/source.md", "docs/source-renamed.md")
        with mock.patch.object(
            precompute, "collect_runners_from_ledger", return_value=[self.runner]
        ):
            self.assertEqual(precompute.collect_runners_from_staged(), [self.runner])

    def test_real_pr_diff_deletion_selects_declaring_runner(self) -> None:
        self._init_git()
        self._git("branch", "base")
        self.source.unlink()
        self._git("add", "-u", "docs/source.md")
        self._git("commit", "-m", "delete declared input")
        with mock.patch.object(
            precompute, "collect_runners_from_ledger", return_value=[self.runner]
        ):
            self.assertEqual(precompute.collect_runners_from_pr_diff("base"), [self.runner])

    def test_real_pr_diff_rename_selects_old_declared_path(self) -> None:
        self._init_git()
        self._git("branch", "base")
        self._git("mv", "docs/source.md", "docs/source-renamed.md")
        self._git("commit", "-m", "rename declared input")
        with mock.patch.object(
            precompute, "collect_runners_from_ledger", return_value=[self.runner]
        ):
            self.assertEqual(precompute.collect_runners_from_pr_diff("base"), [self.runner])


if __name__ == "__main__":
    unittest.main()
