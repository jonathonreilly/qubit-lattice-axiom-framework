"""Exclusive audit-lane orchestrator lock: one instance per repo/machine."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import orchestrate_audit_batch as batch


class DrainLockTest(unittest.TestCase):
    def test_second_acquire_refused_until_first_released(self):
        first = batch.acquire_exclusive_drain_lock("test-first")
        self.assertIsNotNone(first)
        try:
            second = batch.acquire_exclusive_drain_lock("test-second")
            self.assertIsNone(second)
        finally:
            first.close()
        third = batch.acquire_exclusive_drain_lock("test-third")
        self.assertIsNotNone(third)
        third.close()

    def test_lock_path_is_repo_keyed_and_outside_repo(self):
        import hashlib
        import tempfile

        key = hashlib.sha256(str(batch.REPO_ROOT).encode("utf-8")).hexdigest()[:12]
        expected = Path(tempfile.gettempdir()) / f"audit-lane-{key}.lock"
        handle = batch.acquire_exclusive_drain_lock("test-path")
        try:
            self.assertEqual(Path(handle.name), expected)
            self.assertNotIn(
                str(batch.REPO_ROOT), str(Path(handle.name).parent)
            )
        finally:
            handle.close()


if __name__ == "__main__":
    unittest.main()
