"""The suite runner fails a test file that changes the checkout."""
from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import run_audit_tests as runner

WRITER = """\
import unittest
from pathlib import Path


class WriterTest(unittest.TestCase):
    def test_writes(self):
        (Path(__file__).resolve().parents[1] / "{name}").write_text("{text}")
"""

CLEAN = """\
import unittest


class CleanTest(unittest.TestCase):
    def test_nothing(self):
        pass
"""

# Passes, but leaves the repository unreadable, so the next git status fails.
BREAKS_GIT = """\
import unittest
from pathlib import Path


class BreaksGitTest(unittest.TestCase):
    def test_corrupts_head(self):
        (Path(__file__).resolve().parents[1] / ".git" / "HEAD").write_text("garbage\\n")
"""


class TreeStateTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        (self.root / ".gitignore").write_text("__pycache__/\ncache/\n")
        (self.root / "tracked.txt").write_text("baseline\n")
        (self.root / "tests").mkdir()
        self._git("init", "-q")
        self._git("add", ".")
        self._git(
            "-c", "user.name=Audit Test", "-c", "user.email=audit-test@example.invalid",
            "-c", "commit.gpgsign=false",
            "commit", "-q", "-m", "baseline",
        )
        patcher = mock.patch.object(runner, "REPO_ROOT", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)

    def _git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True)

    def _change(self, write) -> list[str]:
        before = runner.tree_state()
        write()
        return runner.changed_paths(before, runner.tree_state())

    def test_clean_tree_has_no_state(self):
        self.assertEqual(runner.tree_state(), {})

    def test_tracked_write_is_reported(self):
        changed = self._change(lambda: (self.root / "tracked.txt").write_text("rewritten\n"))
        self.assertEqual(changed, ["tracked.txt"])

    def test_second_write_to_a_dirty_file_is_reported(self):
        (self.root / "tracked.txt").write_text("edited by hand\n")
        changed = self._change(lambda: (self.root / "tracked.txt").write_text("rewritten\n"))
        self.assertEqual(changed, ["tracked.txt"])

    def test_identical_rewrite_is_not_reported(self):
        changed = self._change(lambda: (self.root / "tracked.txt").write_text("baseline\n"))
        self.assertEqual(changed, [])

    def test_untracked_file_is_reported_and_ignored_cache_is_not(self):
        def write():
            (self.root / "cache").mkdir()
            (self.root / "cache" / "built.json").write_text("{}\n")
            (self.root / "stray.txt").write_text("stray\n")

        self.assertEqual(self._change(write), ["stray.txt"])

    def test_deleted_file_is_reported(self):
        changed = self._change(lambda: (self.root / "tracked.txt").unlink())
        self.assertEqual(changed, ["tracked.txt"])

    def _main(self) -> tuple[int, str]:
        out = io.StringIO()
        with mock.patch.object(runner, "TESTS_DIR", self.root / "tests"), \
                mock.patch.object(runner, "KNOWN_BROKEN", {}), \
                mock.patch.dict(runner.os.environ, {"GITHUB_ACTIONS": ""}), \
                contextlib.redirect_stdout(out):
            rc = runner.main()
        return rc, out.getvalue()

    def test_main_fails_a_file_that_writes_the_checkout(self):
        tests = self.root / "tests"
        (tests / "test_clean.py").write_text(CLEAN)
        (tests / "test_writer.py").write_text(WRITER.format(name="tracked.txt", text="dirty"))
        self._git("add", "tests")
        rc, report = self._main()
        self.assertEqual(rc, 1)
        self.assertIn("test_clean.py: PASS\n", report)
        self.assertIn("  changed: tracked.txt\n", report)
        self.assertIn("test_writer.py: FAIL, changed the checkout\n", report)
        self.assertIn("unexpected failures: 1\n", report)

    def test_main_fails_when_git_status_fails_before_any_file(self):
        (self.root / "tests" / "test_clean.py").write_text(CLEAN)
        not_a_repo = tempfile.TemporaryDirectory()
        self.addCleanup(not_a_repo.cleanup)
        outside = Path(not_a_repo.name).resolve()
        # The ceiling stops git from finding a repository above the scratch dir.
        with mock.patch.object(runner, "REPO_ROOT", outside), \
                mock.patch.dict(runner.os.environ, {"GIT_CEILING_DIRECTORIES": str(outside.parent)}):
            rc, report = self._main()
        self.assertEqual(rc, 1)
        self.assertIn("FAIL: git status failed", report)
        self.assertNotIn("PASS", report)
        self.assertNotIn("unexpected failures: 0", report)

    def test_main_fails_when_git_status_fails_after_a_file(self):
        tests = self.root / "tests"
        (tests / "test_breaks_git.py").write_text(BREAKS_GIT)
        (tests / "test_later.py").write_text(CLEAN)
        self._git("add", "tests")
        rc, report = self._main()
        self.assertEqual(rc, 1)
        self.assertIn("test_breaks_git.py: FAIL, git status failed after this file\n", report)
        self.assertNotIn("test_later.py", report)
        self.assertNotIn("PASS", report)
        self.assertIn("unexpected failures: 1\n", report)


if __name__ == "__main__":
    unittest.main()
