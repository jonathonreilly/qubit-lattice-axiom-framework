"""Checks for the guards in scripts/lab_ops.py that protect work and models."""
import contextlib
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import lab_ops


def call(*argv: str) -> tuple[int, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = lab_ops.main(list(argv))
    return code, out.getvalue()


def git(*args: str, cwd: Path) -> None:
    subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.org", *args],
        cwd=cwd, check=True, capture_output=True,
    )


class FloorTest(unittest.TestCase):
    def test_model_outside_floor_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "GOAL.md").write_text(
                "model_floor worker: strong@high, other\n", encoding="utf-8"
            )
            base = ("preflight", "--target", tmp, "--min-disk-gb", "0",
                    "--min-mem-pct", "0")
            cases = (
                (("--role", "worker", "--model", "strong", "--effort", "high"), 0),
                (("--role", "worker", "--model", "other"), 0),
                (("--role", "worker", "--model", "strong", "--effort", "low"), 1),
                (("--role", "worker", "--model", "weak"), 1),
                (("--role", "worker"), 1),
                (("--role", "checker", "--model", "strong"), 1),
            )
            for extra, expected in cases:
                with self.subTest(extra=extra):
                    self.assertEqual(call(*base, *extra)[0], expected)


class NumericLockTest(unittest.TestCase):
    def test_second_holder_is_refused_until_release(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = os.environ.get("LAB_LOCK_DIR")
            os.environ["LAB_LOCK_DIR"] = tmp
            try:
                self.assertEqual(call("numeric-lock", "acquire", "--holder", "a")[0], 0)
                self.assertEqual(call("numeric-lock", "acquire", "--holder", "b")[0], 2)
                base = ("preflight", "--numeric", "--min-disk-gb", "0",
                        "--min-mem-pct", "0", "--max-load", "100000")
                self.assertIn("refuse  numeric lock", call(*base)[1])
                self.assertEqual(call("numeric-lock", "release", "--holder", "a")[0], 0)
                self.assertEqual(call("numeric-lock", "acquire", "--holder", "b")[0], 0)
            finally:
                if old is None:
                    del os.environ["LAB_LOCK_DIR"]
                else:
                    os.environ["LAB_LOCK_DIR"] = old


class StatusTest(unittest.TestCase):
    def test_counts_open_obligations_and_expired_leases(self):
        with tempfile.TemporaryDirectory() as tmp:
            parts = Path(tmp) / "parts"
            parts.mkdir()
            (parts / "core.md").write_text(
                "lead: a/b/c s1\nlease_until: 2000-01-01T00:00Z\n"
                "## Obligations\n- gap: one -> x\n- unchecked: two -> x\n"
                "- implication: three given one -> x\n- discharged: four -> x\n"
                "## Requests\n- other: change the bound\n",
                encoding="utf-8",
            )
            (parts / "core--route.md").write_text(
                "lead: d/e/f s2\nlease_until: 2999-01-01T00:00Z\n- gap: ignored -> x\n",
                encoding="utf-8",
            )
            code, text = call("status", tmp)
        self.assertEqual(code, 0)
        self.assertIn("open obligations: 3", text)
        self.assertIn("expired 2000-01-01T00:00Z", text)
        self.assertIn("live until 2999-01-01T00:00Z", text)
        self.assertIn("request from core: other: change the bound", text)


class WorktreeTest(unittest.TestCase):
    def test_remove_refuses_until_work_is_pushed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            remote = root / "remote.git"
            subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remote)],
                           check=True)
            seed = root / "seed"
            subprocess.run(["git", "clone", "-q", str(remote), str(seed)],
                           check=True, capture_output=True)
            (seed / "AGENTS.md").write_text("rules\n", encoding="utf-8")
            (seed / "other.txt").write_text("not needed\n", encoding="utf-8")
            git("add", ".", cwd=seed)
            git("commit", "-q", "-m", "seed", cwd=seed)
            git("push", "-q", "origin", "HEAD:main", cwd=seed)

            tree = root / "tree"
            cwd = Path.cwd()
            try:
                os.chdir(seed)
                self.assertEqual(call("worktree-add", "work", "--dir", str(tree))[0], 0)
                self.assertTrue((tree / "AGENTS.md").exists())
                self.assertFalse((tree / "other.txt").exists())

                (tree / "AGENTS.md").write_text("changed\n", encoding="utf-8")
                self.assertEqual(call("worktree-remove", str(tree))[0], 1)
                git("commit", "-q", "-am", "work", cwd=tree)
                self.assertEqual(call("worktree-remove", str(tree))[0], 1)
                (tree / "scratch.txt").write_text("keep me\n", encoding="utf-8")
                git("push", "-q", "origin", "HEAD:refs/heads/work", cwd=tree)
                self.assertEqual(call("worktree-remove", str(tree))[0], 1)
                self.assertTrue(tree.exists())
                self.assertEqual(
                    call("worktree-remove", str(tree), "--discard-untracked")[0], 0
                )
                self.assertFalse(tree.exists())
            finally:
                os.chdir(cwd)


if __name__ == "__main__":
    unittest.main()
