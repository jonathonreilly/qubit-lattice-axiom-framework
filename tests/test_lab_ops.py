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


def write_check(folder: Path, name: str, statement: str, verdict: str,
                text: tuple[str, ...], reads: tuple[tuple[str, str], ...] = (),
                failure: str = "none", checker: str = "p/m/e s2",
                author: str = "p/m/e s1", answers: str = "none") -> None:
    lines = [f"  - {lab_ops.span_hash(folder, ref)} {ref}" for ref in text]
    split = len(lines)
    lines += [f"  - {lab_ops.span_hash(folder, ref)} {who} {ref}" for who, ref in reads]
    (folder / "checks" / name).write_text("\n".join([
        "---", f"statement: {statement}", "commit: " + "0" * 40,
        f"content: {lab_ops.content_hash(lines)}", "text:", *lines[:split],
        "reads:", *lines[split:], f"verdict: {verdict}", f"failure: {failure}",
        "path: a different derivation", f"checker: {checker}", f"author: {author}",
        f"answers: {answers}", "steer: none", "---", "## Finding", "",
    ]), encoding="utf-8")


class StandingTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.folder = Path(tmp.name).resolve()
        for sub in ("parts", "checks", "notes"):
            (self.folder / sub).mkdir()
        (self.folder / "notes" / "proofs.md").write_text(
            "# Proofs\n\n## Alpha\nalpha argument\n\n## Beta\nbeta argument\n",
            encoding="utf-8",
        )
        for name in ("gamma", "delta", "epsilon", "zeta"):
            (self.folder / "notes" / f"{name}.md").write_text(f"{name}\n", encoding="utf-8")
        (self.folder / "parts" / "core.md").write_text(
            "lead: p/m/e s1\nlease_until: 2999-01-01T00:00Z\n## Obligations\n"
            "- argued: alpha -> x\n- argued: beta given alpha -> x\n"
            "- argued: gamma -> x\n- argued: delta -> x\n"
            "- argued: epsilon -> x\n- argued: zeta given beta -> x\n",
            encoding="utf-8",
        )

    def status(self) -> str:
        code, text = call("status", str(self.folder))
        self.assertEqual(code, 0)
        return text

    def test_standing_is_computed_from_check_records(self):
        folder = self.folder
        write_check(folder, "alpha-1.md", "alpha", "right", ("notes/proofs.md#Alpha",))
        # Same session on both sides: the record does not count.
        write_check(folder, "beta-1.md", "beta", "right", ("notes/proofs.md#Beta",),
                    checker="p/m/e s1")
        write_check(folder, "gamma-1.md", "gamma", "wrong", ("notes/gamma.md",),
                    failure="step notes/gamma.md:1")
        write_check(folder, "delta-1.md", "delta", "right", ("notes/delta.md",))
        write_check(folder, "delta-2.md", "delta", "wrong", ("notes/delta.md",),
                    failure="step notes/delta.md:1", checker="p/m/e s3")
        write_check(folder, "epsilon-1.md", "epsilon", "wrong", ("notes/epsilon.md",),
                    failure="counterexample notes/epsilon.md:1")
        write_check(folder, "zeta-1.md", "zeta", "right", ("notes/zeta.md",),
                    reads=(("beta", "notes/proofs.md#Beta"),))
        text = self.status()
        self.assertIn("open 1 argued 2 checked-given 1 checked 1 refuted 1", text)
        self.assertIn("open obligations: 4", text)
        self.assertIn("checked given beta: zeta", text)
        self.assertIn("disputed, so argued: delta", text)
        self.assertIn("1 check record(s) no longer count: beta", text)

        # A third path answers the wrong record: delta is checked.
        write_check(folder, "delta-3.md", "delta", "right", ("notes/delta.md",),
                    checker="p/m/e s4", answers="delta-2.md")
        self.assertIn("open 1 argued 1 checked-given 1 checked 2 refuted 1", self.status())

    def test_an_edit_returns_only_that_statement_to_argued(self):
        folder = self.folder
        write_check(folder, "alpha-1.md", "alpha", "right", ("notes/proofs.md#Alpha",))
        write_check(folder, "beta-1.md", "beta", "right", ("notes/proofs.md#Beta",))
        self.assertIn("argued 4 checked-given 0 checked 2", self.status())
        proofs = folder / "notes" / "proofs.md"
        proofs.write_text(proofs.read_text().replace("beta argument", "beta, revised"),
                          encoding="utf-8")
        text = self.status()
        self.assertIn("argued 5 checked-given 0 checked 1", text)
        self.assertIn("1 check record(s) no longer count: beta", text)

    def test_a_tampered_record_does_not_count(self):
        folder = self.folder
        write_check(folder, "alpha-1.md", "alpha", "right", ("notes/proofs.md#Alpha",))
        record = folder / "checks" / "alpha-1.md"
        record.write_text(record.read_text().replace("#Alpha", "#Beta"), encoding="utf-8")
        self.assertIn("argued 6 checked-given 0 checked 0", self.status())

    def test_check_hash_prints_lines_a_record_accepts(self):
        cwd = Path.cwd()
        try:
            os.chdir(self.folder)
            code, text = call("check-hash", "--text", "notes/proofs.md#Alpha",
                              "--reads", "beta=notes/proofs.md#Beta")
            self.assertEqual(code, 0)
            lines = text.splitlines()
            self.assertEqual(lines[1], "text:")
            self.assertEqual(lines[3], "reads:")
            self.assertEqual(lines[0], "content: " + lab_ops.content_hash([lines[2], lines[4]]))
            self.assertTrue(lines[4].endswith(" beta notes/proofs.md#Beta"))
            self.assertEqual(call("check-hash", "--text", "notes/proofs.md#Missing")[0], 1)
        finally:
            os.chdir(cwd)


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
            (seed / ".gitignore").write_text("valuable.log\n", encoding="utf-8")
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
                ignored = tree / "valuable.log"
                ignored.write_text("local results\n", encoding="utf-8")
                self.assertEqual(
                    call("worktree-remove", str(tree), "--discard-untracked")[0], 1
                )
                self.assertEqual(ignored.read_text(), "local results\n")
                (tree / "scratch.txt").unlink()
                self.assertEqual(call("worktree-remove", str(tree))[0], 1)
                self.assertEqual(ignored.read_text(), "local results\n")
                ignored.unlink()
                (tree / "scratch.txt").write_text("discard me\n", encoding="utf-8")
                self.assertEqual(
                    call("worktree-remove", str(tree), "--discard-untracked")[0], 0
                )
                self.assertFalse(tree.exists())
            finally:
                os.chdir(cwd)


class DoctorTest(unittest.TestCase):
    def test_rules_behind_main_are_refused_after_a_fetch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            remote = root / "remote.git"
            subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remote)],
                           check=True)
            seed = root / "seed"
            subprocess.run(["git", "clone", "-q", str(remote), str(seed)],
                           check=True, capture_output=True)
            (seed / "AGENTS.md").write_text("rules\n", encoding="utf-8")
            (seed / "notes.md").write_text("science\n", encoding="utf-8")
            git("add", ".", cwd=seed)
            git("commit", "-q", "-m", "seed", cwd=seed)
            git("push", "-q", "origin", "HEAD:main", cwd=seed)
            work = root / "work"
            subprocess.run(["git", "clone", "-q", str(remote), str(work)],
                           check=True, capture_output=True)

            cwd = Path.cwd()
            try:
                os.chdir(work)
                self.assertEqual(call("doctor")[0], 0)

                (seed / "notes.md").write_text("more science\n", encoding="utf-8")
                git("commit", "-q", "-am", "science only", cwd=seed)
                git("push", "-q", "origin", "HEAD:main", cwd=seed)
                code, text = call("doctor")
                self.assertEqual(code, 0)
                self.assertIn("1 commits behind", text)

                (seed / "AGENTS.md").write_text("new rules\n", encoding="utf-8")
                git("commit", "-q", "-am", "rules", cwd=seed)
                git("push", "-q", "origin", "HEAD:main", cwd=seed)
                self.assertEqual(call("doctor", "--no-fetch")[0], 0)
                code, text = call("doctor")
                self.assertEqual(code, 1)
                self.assertIn("differs: AGENTS.md", text)
            finally:
                os.chdir(cwd)

    def test_outside_a_checkout_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = Path.cwd()
            try:
                os.chdir(tmp)
                code, text = call("doctor", "--no-fetch")
            finally:
                os.chdir(cwd)
        self.assertEqual(code, 1)
        self.assertIn("refuse: cannot compare rules", text)


if __name__ == "__main__":
    unittest.main()
