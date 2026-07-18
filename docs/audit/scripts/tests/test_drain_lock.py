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

        key = hashlib.sha256(batch._repo_identity().encode("utf-8")).hexdigest()[:12]
        expected = Path(tempfile.gettempdir()) / f"audit-lane-{key}.lock"
        handle = batch.acquire_exclusive_drain_lock("test-path")
        try:
            self.assertEqual(Path(handle.name), expected)
            self.assertNotIn(
                str(batch.REPO_ROOT), str(Path(handle.name).parent)
            )
        finally:
            handle.close()



class DrainLockWorktreeTest(unittest.TestCase):
    def test_second_worktree_of_same_clone_shares_the_lock(self):
        import subprocess
        import tempfile

        held = batch.acquire_exclusive_drain_lock("wt-primary")
        self.assertIsNotNone(held)
        tmp = tempfile.mkdtemp(prefix="drainlock-wt-")
        wt = Path(tmp) / "wt2"
        try:
            subprocess.run(
                ["git", "worktree", "add", "--detach", str(wt)],
                cwd=batch.REPO_ROOT, check=True, capture_output=True,
            )
            # Hermetic probe: the CURRENT module code (not the worktree's
            # HEAD checkout) with REPO_ROOT pointed at the second worktree —
            # tests the keying logic itself, pre- or post-commit.
            probe = subprocess.run(
                [sys.executable, "-c",
                 "import sys; from pathlib import Path\n"
                 "sys.path.insert(0, sys.argv[1])\n"
                 "import orchestrate_audit_batch as b\n"
                 "b.REPO_ROOT = Path(sys.argv[2])\n"
                 "h = b.acquire_exclusive_drain_lock('wt-secondary')\n"
                 "print('REFUSED' if h is None else 'ACQUIRED')",
                 str(Path(batch.__file__).parent), str(wt)],
                capture_output=True, text=True,
            )
            self.assertIn("REFUSED", probe.stdout,
                          msg=f"stdout={probe.stdout!r} stderr={probe.stderr!r}")
        finally:
            held.close()
            subprocess.run(
                ["git", "worktree", "remove", "--force", str(wt)],
                cwd=batch.REPO_ROOT, capture_output=True,
            )

if __name__ == "__main__":
    unittest.main()
