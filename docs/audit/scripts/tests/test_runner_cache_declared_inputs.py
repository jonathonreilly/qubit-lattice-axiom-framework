"""Regression tests for dependency-aware runner-cache freshness."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import runner_cache as rc  # noqa: E402


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
        self.result = {
            "stdout": "PASS\n",
            "stderr": "",
            "timeout_sec": 120,
            "exit_code": 0,
            "elapsed_sec": 0.0,
            "status": "ok",
        }

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


if __name__ == "__main__":
    unittest.main()
