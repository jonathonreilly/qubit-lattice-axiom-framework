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


class PriorDigestTest(unittest.TestCase):
    def test_lane_without_committed_digest_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            git("init", "-q", cwd=repo)
            target = repo / "target"
            (target / "prior").mkdir(parents=True)
            (target / "GOAL.md").write_text("goal\n", encoding="utf-8")
            git("add", "-A", cwd=repo)
            git("commit", "-q", "-m", "goal", cwd=repo)
            base = ("preflight", "--target", str(target), "--min-disk-gb", "0",
                    "--min-mem-pct", "0")
            digest = target / "prior" / "a1.md"

            def refused(*extra: str) -> bool:
                code, out = call(*base, *extra)
                self.assertEqual(code == 1, "refuse  prior digest" in out, out)
                return code == 1

            self.assertFalse(refused())
            self.assertTrue(refused("--lane", "a1"), "missing")
            digest.write_text("", encoding="utf-8")
            git("add", "-A", cwd=repo)
            git("commit", "-q", "--allow-empty", "-m", "empty digest", cwd=repo)
            self.assertTrue(refused("--lane", "a1"), "empty")
            digest.write_text("main proves nothing on this target\n", encoding="utf-8")
            self.assertTrue(refused("--lane", "a1"), "edited, not committed")
            git("add", "-A", cwd=repo)
            self.assertTrue(refused("--lane", "a1"), "staged, not committed")
            git("commit", "-q", "-m", "digest", cwd=repo)
            self.assertFalse(refused("--lane", "a1"))
            self.assertTrue(refused("--lane", "a2"), "another lane's digest")
            self.assertTrue(refused("--lane", "../prior/a1"), "path in the name")
            (target / "prior" / ".gitignore").write_text("a3.md\n", encoding="utf-8")
            (target / "prior" / "a3.md").write_text("ignored\n", encoding="utf-8")
            self.assertTrue(refused("--lane", "a3"), "ignored, never committed")
            digest.write_text("edited after the commit\n", encoding="utf-8")
            self.assertTrue(refused("--lane", "a1"), "changed since the commit")
            self.assertEqual(
                call("preflight", "--lane", "a1", "--min-disk-gb", "0",
                     "--min-mem-pct", "0")[0], 1, "a lane with no target")


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
                author: str = "p/m/e s1", answers: str = "none",
                drop: tuple[str, ...] = ()) -> Path:
    lines = [f"  - {lab_ops.span_hash(folder, ref)} {ref}" for ref in text]
    split = len(lines)
    lines += [f"  - {lab_ops.span_hash(folder, ref)} {who} {ref}" for who, ref in reads]
    front = [
        f"statement: {statement}", "commit: " + "0" * 40,
        f"content: {lab_ops.content_hash(lines)}", "text:", *lines[:split],
        "reads:", *lines[split:], f"verdict: {verdict}", f"failure: {failure}",
        "path: a different derivation", f"checker: {checker}", f"author: {author}",
        f"answers: {answers}", "steer: none",
    ]
    front = [line for line in front if line.split(":")[0] not in drop]
    path = folder / "checks" / name
    path.write_text("\n".join(["---", *front, "---", "## Finding", ""]), encoding="utf-8")
    return path


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

    def part(self, *lines: str) -> None:
        (self.folder / "parts" / "core.md").write_text(
            "lead: p/m/e s1\nlease_until: 2999-01-01T00:00Z\n## Obligations\n"
            + "".join(f"{line}\n" for line in lines), encoding="utf-8",
        )

    def status(self) -> str:
        code, text = call("status", str(self.folder))
        self.assertEqual(code, 0)
        return text

    def test_standing_is_computed_from_check_records(self):
        folder = self.folder
        self.part("- argued: alpha -> x", "- argued: beta given alpha -> x",
                  "- argued: gamma -> x", "- argued: delta -> x",
                  "- argued: epsilon -> x", "- argued: zeta given beta -> x")
        write_check(folder, "alpha-1.md", "alpha", "right", ("notes/proofs.md#Alpha",))
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
        self.assertIn("rejected check record beta-1.md: checker and author are the "
                      "same session", text)

        # A third path answers the wrong record: delta is checked.
        write_check(folder, "delta-3.md", "delta", "right", ("notes/delta.md",),
                    checker="p/m/e s4", answers="delta-2.md")
        self.assertIn("open 1 argued 1 checked-given 1 checked 2 refuted 1", self.status())

    def test_an_edit_returns_a_checked_statement_to_argued_not_open(self):
        folder = self.folder
        self.part("- open: alpha -> x", "- argued: beta -> x")
        write_check(folder, "alpha-1.md", "alpha", "right", ("notes/proofs.md#Alpha",))
        write_check(folder, "beta-1.md", "beta", "right", ("notes/proofs.md#Beta",))
        self.assertIn("open 0 argued 0 checked-given 0 checked 2", self.status())
        proofs = folder / "notes" / "proofs.md"
        proofs.write_text(proofs.read_text().replace("beta argument", "beta, revised"),
                          encoding="utf-8")
        text = self.status()
        self.assertIn("open 0 argued 1 checked-given 0 checked 1", text)
        self.assertIn("1 check record(s) are about an earlier text: beta", text)
        proofs.write_text(proofs.read_text().replace("alpha argument", "alpha, revised"),
                          encoding="utf-8")
        self.assertIn("open 0 argued 2 checked-given 0 checked 0", self.status())

    def test_a_record_with_the_wrong_content_hash_is_rejected(self):
        self.part("- argued: alpha -> x")
        record = write_check(self.folder, "alpha-1.md", "alpha", "right",
                             ("notes/proofs.md#Alpha",))
        self.assertIn("argued 0 checked-given 0 checked 1", self.status())
        lines = record.read_text().splitlines()
        lines = ["content: " + "0" * 64 if line.startswith("content:") else line
                 for line in lines]
        record.write_text("\n".join(lines) + "\n", encoding="utf-8")
        text = self.status()
        self.assertIn("rejected check record alpha-1.md: content does not match", text)
        self.assertIn("argued 1 checked-given 0 checked 0", text)

    def test_a_record_missing_a_field_is_rejected(self):
        self.part("- argued: alpha -> x")
        for field in ("author", "commit", "path", "verdict"):
            with self.subTest(field=field):
                write_check(self.folder, "alpha-1.md", "alpha", "right",
                            ("notes/proofs.md#Alpha",), drop=(field,))
                text = self.status()
                self.assertIn(f"rejected check record alpha-1.md: {field} is missing", text)
                self.assertIn("argued 1 checked-given 0 checked 0", text)

    def test_a_rejected_wrong_record_still_blocks_checked(self):
        self.part("- argued: epsilon -> x")
        write_check(self.folder, "epsilon-1.md", "epsilon", "right", ("notes/epsilon.md",))
        write_check(self.folder, "epsilon-2.md", "epsilon", "wrong", ("notes/epsilon.md",),
                    failure="counterexample notes/epsilon.md:1", checker="p/m/e s3",
                    answers="epsilon-2.md")
        text = self.status()
        self.assertIn("rejected check record epsilon-2.md: a record cannot answer itself",
                      text)
        self.assertIn("argued 1 checked-given 0 checked 0", text)
        self.assertIn("not checked until a record answers epsilon-2.md: epsilon", text)

    def test_an_answered_record_stops_suppressing(self):
        folder = self.folder
        self.part("- argued: gamma -> x")
        write_check(folder, "gamma-1.md", "gamma", "right", ("notes/gamma.md",))
        write_check(folder, "gamma-2.md", "gamma", "wrong", ("notes/gamma.md",),
                    failure="step notes/gamma.md:1", checker="p/m/e s3")
        write_check(folder, "gamma-3.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s4", answers="gamma-2.md")
        self.assertIn("argued 0 checked-given 0 checked 1", self.status())
        write_check(folder, "gamma-4.md", "gamma", "wrong", ("notes/gamma.md",),
                    failure="step notes/gamma.md:1", checker="p/m/e s5",
                    answers="gamma-3.md")
        text = self.status()
        self.assertIn("argued 1 checked-given 0 checked 0", text)
        self.assertIn("disputed, so argued: gamma", text)

    def test_a_suppressed_answer_does_not_suppress(self):
        # The right record that answered the failure is itself answered, so the
        # failure stands again and the statement is open.
        folder = self.folder
        self.part("- argued: zeta -> x")
        write_check(folder, "zeta-1.md", "zeta", "wrong", ("notes/zeta.md",),
                    failure="step notes/zeta.md:1")
        write_check(folder, "zeta-2.md", "zeta", "right", ("notes/zeta.md",),
                    checker="p/m/e s3", answers="zeta-1.md")
        self.assertIn("open 0 argued 0 checked-given 0 checked 1", self.status())
        write_check(folder, "zeta-3.md", "zeta", "undecided", ("notes/zeta.md",),
                    checker="p/m/e s4", answers="zeta-2.md")
        self.assertIn("open 1 argued 0 checked-given 0 checked 0", self.status())

    def test_an_answer_cycle_suppresses_nothing(self):
        folder = self.folder
        self.part("- argued: delta -> x")
        write_check(folder, "delta-1.md", "delta", "right", ("notes/delta.md",),
                    answers="delta-2.md")
        write_check(folder, "delta-2.md", "delta", "wrong", ("notes/delta.md",),
                    failure="counterexample notes/delta.md:1", checker="p/m/e s3",
                    answers="delta-1.md")
        self.assertIn("disputed, so argued: delta", self.status())

    def test_a_circle_of_reads_is_not_closed(self):
        folder = self.folder
        self.part("- argued: alpha -> x", "- argued: beta -> x")
        write_check(folder, "alpha-1.md", "alpha", "right", ("notes/proofs.md#Alpha",),
                    reads=(("beta", "notes/proofs.md#Beta"),))
        write_check(folder, "beta-1.md", "beta", "right", ("notes/proofs.md#Beta",),
                    reads=(("alpha", "notes/proofs.md#Alpha"),))
        text = self.status()
        self.assertIn("checked-given 2 checked 0", text)
        self.assertIn("open obligations: 2", text)
        self.assertIn("(a circle of reads)", text)

    def test_each_invalid_field_is_rejected_by_name(self):
        self.part("- argued: gamma -> x")
        cases = (
            ("commit: " + "0" * 40, "commit: abc", "commit is not 40 hex digits"),
            ("verdict: right", "verdict: maybe", "verdict is not right, wrong or undecided"),
            ("checker: p/m/e s2", "checker: nobody", "checker is not"),
            ("author: p/m/e s1", "author: p/m s1", "author is not"),
            ("failure: none", "failure: step notes/gamma.md:1",
             "only a wrong verdict names a failure"),
            ("verdict: right", "verdict: wrong", "a wrong verdict names"),
            ("verdict: right", "verdict: wrong\nverdict: right", "verdict appears twice"),
            ("text:", "raw: x\ntext:", "unknown line: raw: x"),
            ("statement: gamma", "statement: gamma two", "statement is not a name"),
        )
        for old, new, reason in cases:
            with self.subTest(new=new):
                record = write_check(self.folder, "gamma-1.md", "gamma", "right",
                                     ("notes/gamma.md",))
                self.assertIn("checked-given 0 checked 1", self.status())
                body = record.read_text()
                self.assertEqual(body.count(old), 1)
                record.write_text(body.replace(old, new), encoding="utf-8")
                text = self.status()
                self.assertIn(f"rejected check record gamma-1.md: {reason}", text)
                self.assertIn("checked-given 0 checked 0", text)

    def test_a_rejected_wrong_record_is_cleared_only_by_an_answer(self):
        folder = self.folder
        self.part("- argued: epsilon -> x")
        write_check(folder, "epsilon-1.md", "epsilon", "right", ("notes/epsilon.md",))
        write_check(folder, "epsilon-2.md", "epsilon", "wrong", ("notes/epsilon.md",),
                    failure="counterexample notes/epsilon.md:1", checker="p/m/e s3",
                    answers="epsilon-2.md")
        self.assertIn("argued 1 checked-given 0 checked 0", self.status())
        # A new text does not clear it: a broken record's hashes show nothing.
        (folder / "notes" / "epsilon.md").write_text("epsilon, revised\n", encoding="utf-8")
        write_check(folder, "epsilon-3.md", "epsilon", "right", ("notes/epsilon.md",),
                    checker="p/m/e s4")
        text = self.status()
        self.assertIn("argued 1 checked-given 0 checked 0", text)
        self.assertIn("not checked until a record answers epsilon-2.md: epsilon", text)
        # A counting record that answers it does.
        write_check(folder, "epsilon-4.md", "epsilon", "right", ("notes/epsilon.md",),
                    checker="p/m/e s5", answers="epsilon-2.md")
        self.assertIn("argued 0 checked-given 0 checked 1", self.status())

    def test_a_wrong_record_about_an_earlier_text_still_needs_an_answer(self):
        folder = self.folder
        self.part("- argued: gamma -> x")
        write_check(folder, "gamma-1.md", "gamma", "wrong", ("notes/gamma.md",),
                    failure="step notes/gamma.md:1")
        self.assertIn("open 1 argued 0 checked-given 0 checked 0", self.status())
        (folder / "notes" / "gamma.md").write_text("gamma, repaired\n", encoding="utf-8")
        self.assertIn("open 0 argued 1 checked-given 0 checked 0", self.status())
        write_check(folder, "gamma-2.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s3")
        text = self.status()
        self.assertIn("open 0 argued 1 checked-given 0 checked 0", text)
        self.assertIn("not checked until a record answers gamma-1.md: gamma", text)
        write_check(folder, "gamma-3.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s4", answers="gamma-1.md")
        self.assertIn("open 0 argued 0 checked-given 0 checked 1", self.status())

    def test_one_record_can_answer_several_and_a_chain_needs_them_all(self):
        folder = self.folder
        self.part("- argued: gamma -> x")
        write_check(folder, "gamma-1.md", "gamma", "wrong", ("notes/gamma.md",),
                    failure="step notes/gamma.md:1")
        (folder / "notes" / "gamma.md").write_text("gamma, second try\n", encoding="utf-8")
        write_check(folder, "gamma-2.md", "gamma", "wrong", ("notes/gamma.md",),
                    failure="step notes/gamma.md:1", checker="p/m/e s3",
                    answers="gamma-1.md")
        (folder / "notes" / "gamma.md").write_text("gamma, third try\n", encoding="utf-8")
        # Answering only the later failure leaves the earlier one outstanding.
        answer = write_check(folder, "gamma-3.md", "gamma", "right", ("notes/gamma.md",),
                             checker="p/m/e s4", answers="gamma-2.md")
        self.assertIn("not checked until a record answers gamma-1.md: gamma", self.status())
        answer.unlink()
        write_check(folder, "gamma-3.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s4", answers="gamma-1.md, gamma-2.md")
        self.assertIn("open 0 argued 0 checked-given 0 checked 1", self.status())

    def test_a_long_answer_chain_alternates(self):
        # wrong <- right <- wrong <- right: the last is live, so the third is set
        # aside, the second stands again and the first is set aside.
        folder = self.folder
        self.part("- argued: delta -> x")
        write_check(folder, "delta-1.md", "delta", "wrong", ("notes/delta.md",),
                    failure="step notes/delta.md:1")
        write_check(folder, "delta-2.md", "delta", "right", ("notes/delta.md",),
                    checker="p/m/e s3", answers="delta-1.md")
        write_check(folder, "delta-3.md", "delta", "wrong", ("notes/delta.md",),
                    failure="step notes/delta.md:1", checker="p/m/e s4",
                    answers="delta-2.md")
        self.assertIn("open 1 argued 0 checked-given 0 checked 0", self.status())
        write_check(folder, "delta-4.md", "delta", "right", ("notes/delta.md",),
                    checker="p/m/e s5", answers="delta-3.md")
        self.assertIn("open 0 argued 0 checked-given 0 checked 1", self.status())

    def test_an_answer_that_was_itself_set_aside_lifts_nothing(self):
        folder = self.folder
        self.part("- argued: epsilon -> x")
        write_check(folder, "epsilon-1.md", "epsilon", "wrong", ("notes/epsilon.md",),
                    failure="counterexample notes/epsilon.md:1", answers="epsilon-1.md")
        write_check(folder, "epsilon-2.md", "epsilon", "right", ("notes/epsilon.md",),
                    checker="p/m/e s3", answers="epsilon-1.md")
        self.assertIn("argued 0 checked-given 0 checked 1", self.status())
        write_check(folder, "epsilon-3.md", "epsilon", "undecided", ("notes/epsilon.md",),
                    checker="p/m/e s4", answers="epsilon-2.md")
        write_check(folder, "epsilon-4.md", "epsilon", "right", ("notes/epsilon.md",),
                    checker="p/m/e s5")
        text = self.status()
        self.assertIn("argued 1 checked-given 0 checked 0", text)
        self.assertIn("not checked until a record answers epsilon-1.md: epsilon", text)

    def test_a_truncated_record_is_held_against_the_statement_it_names(self):
        folder = self.folder
        self.part("- argued: gamma -> x")
        write_check(folder, "gamma-1.md", "gamma", "right", ("notes/gamma.md",))
        # The file name does not start with the statement's name.
        record = write_check(folder, "second-look.md", "gamma", "wrong",
                             ("notes/gamma.md",), checker="p/m/e s3",
                             failure="counterexample notes/gamma.md:1")
        record.write_text(record.read_text().replace("\n---\n## Finding", "\n## Finding"),
                          encoding="utf-8")
        text = self.status()
        self.assertIn("rejected check record second-look.md: front matter is not closed",
                      text)
        self.assertIn("not checked until a record answers second-look.md: gamma", text)

    def test_a_circle_of_answers_lifts_no_block(self):
        folder = self.folder
        self.part("- argued: epsilon -> x", "- argued: gamma -> x")
        # A rejected negative record, then two right records that answer each
        # other, one of which also names the negative record.
        write_check(folder, "epsilon-9.md", "epsilon", "wrong", ("notes/epsilon.md",),
                    failure="counterexample notes/epsilon.md:1", answers="epsilon-9.md")
        write_check(folder, "epsilon-a.md", "epsilon", "right", ("notes/epsilon.md",),
                    checker="p/m/e s3", answers="epsilon-b.md epsilon-9.md")
        write_check(folder, "epsilon-b.md", "epsilon", "right", ("notes/epsilon.md",),
                    checker="p/m/e s4", answers="epsilon-a.md")
        # The same against a wrong record about an earlier text.
        write_check(folder, "gamma-1.md", "gamma", "wrong", ("notes/gamma.md",),
                    failure="step notes/gamma.md:1")
        (folder / "notes" / "gamma.md").write_text("gamma, repaired\n", encoding="utf-8")
        write_check(folder, "gamma-a.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s3", answers="gamma-b.md, gamma-1.md")
        write_check(folder, "gamma-b.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s4", answers="gamma-a.md")
        text = self.status()
        self.assertIn("open 0 argued 2 checked-given 0 checked 0", text)
        self.assertIn("not checked until a record answers epsilon-9.md: epsilon", text)
        self.assertIn("not checked until a record answers gamma-1.md: gamma", text)
        # A record outside the circle answers each, and both are checked.
        write_check(folder, "epsilon-c.md", "epsilon", "right", ("notes/epsilon.md",),
                    checker="p/m/e s5", answers="epsilon-9.md")
        write_check(folder, "gamma-c.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s5", answers="gamma-1.md")
        self.assertIn("open 0 argued 0 checked-given 0 checked 2", self.status())

    def test_files_that_cannot_be_read_are_reported_not_fatal(self):
        folder = self.folder
        self.part("- argued: gamma -> x")
        write_check(folder, "gamma-1.md", "gamma", "right", ("notes/gamma.md",))
        (folder / "checks" / "gamma-bad.md").symlink_to(folder / "nowhere.md")
        (folder / "checks" / "gamma-note.txt").write_text("aside\n", encoding="utf-8")
        text = self.status()
        self.assertIn("rejected check record gamma-bad.md: cannot be read", text)
        self.assertIn("not checked until a record answers gamma-bad.md: gamma", text)
        self.assertIn("not a check record, ignored: checks/gamma-note.txt", text)
        self.assertIn("open obligations: 1", text)
        write_check(folder, "gamma-2.md", "gamma", "right", ("notes/gamma.md",),
                    checker="p/m/e s3", answers="gamma-bad.md")
        self.assertIn("open obligations: 0", self.status())
        (folder / "parts" / "lost.md").symlink_to(folder / "nowhere.md")
        text = self.status()
        self.assertIn("unreadable part file lost.md", text)
        self.assertIn("open obligations: 1", text)

    def test_a_part_file_with_bad_bytes_keeps_its_obligations_and_adds_one(self):
        self.part("- argued: alpha -> x", "- open: beta -> x")
        damaged = self.folder / "parts" / "core.md"
        damaged.write_bytes(damaged.read_bytes() + b"- argued: gam\xffma -> x\n\xff\n")
        text = self.status()
        self.assertIn("open 1 argued 1 checked-given 0 checked 0", text)
        self.assertIn("this file is not valid UTF-8, counted as one more open obligation",
                      text)
        # alpha, beta, the line that can no longer be read, and one for the damage
        self.assertIn("open obligations: 4", text)

    def test_unreadable_records_block_what_they_name(self):
        import hashlib
        folder = self.folder
        self.part("- argued: gamma -> x", "- argued: zeta -> x")
        write_check(folder, "gamma-1.md", "gamma", "right", ("notes/gamma.md",))
        write_check(folder, "zeta-1.md", "zeta", "right", ("notes/zeta.md",))
        self.assertIn("checked-given 0 checked 2", self.status())

        def wrong(name: str) -> Path:
            return write_check(folder, name, "gamma", "wrong", ("notes/gamma.md",),
                               failure="counterexample notes/gamma.md:1",
                               checker="p/m/e s3")

        def redigest(body: str) -> str:
            raw = [line for line in body.splitlines() if line.startswith("  - ")]
            digest = hashlib.sha256("\n".join(raw).encode()).hexdigest()
            return "\n".join(f"content: {digest}" if line.startswith("content:") else line
                             for line in body.splitlines()) + "\n"

        real = lab_ops.span_hash(folder, "notes/gamma.md")
        cases = (
            # the closing line of the front matter is missing
            (lambda body: body.replace("\n---\n## Finding", "\n## Finding"),
             "front matter is not closed", 1),
            # not front matter at all: held against the name its file starts with
            (lambda body: "garbage\n", "no front matter", 1),
            # a hash that is not a hash, with the digest recomputed to match
            (lambda body: redigest(body.replace(real, "not-a-sha")),
             "a text line is not `<sha256> ...`", 1),
            # the text section twice
            (lambda body: body.replace("reads:\n", "text:\nreads:\n"),
             "text appears twice", 1),
            # two statements named: both are held
            (lambda body: body.replace("statement: gamma", "statement: gamma\nstatement: zeta"),
             "statement appears twice", 0),
        )
        for change, reason, left in cases:
            with self.subTest(reason=reason):
                record = wrong("gamma-2.md")
                record.write_text(change(record.read_text()), encoding="utf-8")
                text = self.status()
                self.assertIn(f"rejected check record gamma-2.md: {reason}", text)
                self.assertIn(f"checked-given 0 checked {left}", text)
                self.assertIn("not checked until a record answers gamma-2.md: gamma", text)
                answer = write_check(folder, "gamma-3.md", "gamma", "right",
                                     ("notes/gamma.md",), checker="p/m/e s4",
                                     answers="gamma-2.md")
                self.assertIn(f"checked-given 0 checked {left + 1}", self.status())
                answer.unlink()

    def test_a_record_outside_an_answer_cycle_can_still_answer_into_it(self):
        folder = self.folder
        self.part("- argued: delta -> x")
        write_check(folder, "delta-1.md", "delta", "right", ("notes/delta.md",),
                    answers="delta-2.md")
        write_check(folder, "delta-2.md", "delta", "wrong", ("notes/delta.md",),
                    failure="counterexample notes/delta.md:1", checker="p/m/e s3",
                    answers="delta-1.md")
        self.assertIn("disputed, so argued: delta", self.status())
        write_check(folder, "delta-3.md", "delta", "right", ("notes/delta.md",),
                    checker="p/m/e s4", answers="delta-2.md")
        self.assertIn("argued 0 checked-given 0 checked 1", self.status())

    def test_a_typed_legacy_label_reopens_on_a_stale_or_rejected_record(self):
        folder = self.folder
        self.part("- discharged: gamma -> x", "- discharged: zeta -> x")
        write_check(folder, "gamma-1.md", "gamma", "right", ("notes/gamma.md",))
        self.assertIn("open obligations: 0", self.status())
        (folder / "notes" / "gamma.md").write_text("gamma, revised\n", encoding="utf-8")
        text = self.status()
        self.assertIn("typed discharged, but 1 check record(s) are about an earlier text: "
                      "gamma", text)
        self.assertIn("open obligations: 1", text)
        write_check(folder, "zeta-1.md", "zeta", "wrong", ("notes/zeta.md",),
                    failure="counterexample notes/zeta.md:1", answers="zeta-1.md")
        text = self.status()
        self.assertIn("typed discharged, but no record answers zeta-1.md: zeta", text)
        self.assertIn("open obligations: 2", text)

    def test_a_corrupted_hash_does_not_pass_for_an_earlier_text(self):
        folder = self.folder
        self.part("- argued: epsilon -> x")
        write_check(folder, "epsilon-1.md", "epsilon", "right", ("notes/epsilon.md",))
        wrong = write_check(folder, "epsilon-2.md", "epsilon", "wrong",
                            ("notes/epsilon.md",), checker="p/m/e s3",
                            failure="counterexample notes/epsilon.md:1")
        self.assertIn("disputed, so argued: epsilon", self.status())
        # Corrupt the span hash only: the source has not changed.
        real = lab_ops.span_hash(folder, "notes/epsilon.md")
        body = wrong.read_text()
        self.assertEqual(body.count(f"  - {real} "), 1)
        wrong.write_text(body.replace(f"  - {real} ", "  - " + "0" * 64 + " "),
                         encoding="utf-8")
        text = self.status()
        self.assertIn("rejected check record epsilon-2.md: content does not match", text)
        self.assertIn("argued 1 checked-given 0 checked 0", text)
        self.assertIn("open obligations: 1", text)

    def test_a_broken_record_blocks_unless_it_plainly_says_right(self):
        folder = self.folder
        self.part("- argued: gamma -> x")
        write_check(folder, "gamma-1.md", "gamma", "right", ("notes/gamma.md",))
        cases = (
            ("verdict: right", "verdict: right\nverdict: wrong", True),
            ("verdict: right", "verdict: wrong\nverdict: right", True),
            ("verdict: right\n", "", True),
            ("verdict: right", "verdict: maybe", True),
            ("path: a different derivation\n", "", False),
            ("verdict: right", "verdict: undecided\nsteer: none", False),
        )
        for old, new, blocks in cases:
            with self.subTest(new=new):
                broken = write_check(folder, "gamma-2.md", "gamma", "right",
                                     ("notes/gamma.md",), checker="p/m/e s3")
                body = broken.read_text()
                self.assertEqual(body.count(old), 1)
                broken.write_text(body.replace(old, new), encoding="utf-8")
                text = self.status()
                self.assertIn("rejected check record gamma-2.md", text)
                self.assertIn("checked 0" if blocks else "checked 1", text)

    def test_a_repeated_heading_names_no_text(self):
        note = self.folder / "notes" / "twice.md"
        note.write_text("## Same\nfirst\n\n## Same\nsecond\n", encoding="utf-8")
        self.assertIsNone(lab_ops.span_hash(self.folder, "notes/twice.md#Same"))
        self.assertIsNone(lab_ops.span_hash(self.folder, "notes/twice.md#Missing"))
        cwd = Path.cwd()
        try:
            os.chdir(self.folder)
            self.assertEqual(call("check-hash", "--text", "notes/twice.md#Same")[0], 1)
        finally:
            os.chdir(cwd)

    def test_obligation_lines_allow_spacing_and_fail_closed(self):
        self.part("-  open: alpha -> x", "- argued:\tbeta given alpha -> x",
                  "- checked: gamma -> x", "- argued: two words -> x", "- note this")
        text = self.status()
        self.assertIn("open 1 argued 1 checked-given 0 checked 0", text)
        self.assertIn("open obligations: 5", text)
        self.assertIn("unreadable obligation, counted open: - checked: gamma -> x", text)
        self.assertIn("unreadable obligation, counted open: - argued: two words -> x", text)

    def test_a_typed_legacy_label_does_not_outrank_a_check_record(self):
        self.part("- discharged: epsilon -> x", "- discharged: zeta -> x")
        write_check(self.folder, "epsilon-1.md", "epsilon", "wrong", ("notes/epsilon.md",),
                    failure="counterexample notes/epsilon.md:1")
        text = self.status()
        self.assertIn("typed discharged, but check records give refuted: epsilon", text)
        self.assertIn("typed, not computed: gap 0 unchecked 0 implication 0 discharged 2",
                      text)
        self.assertIn("open obligations: 1", text)

    def test_check_hash_matches_hashes_computed_independently(self):
        import hashlib
        section = hashlib.sha256(b"## Alpha\nalpha argument\n\n").hexdigest()
        whole = hashlib.sha256(b"gamma\n").hexdigest()
        text_line = f"  - {section} notes/proofs.md#Alpha"
        reads_line = f"  - {whole} gamma notes/gamma.md"
        content = hashlib.sha256(f"{text_line}\n{reads_line}".encode()).hexdigest()
        cwd = Path.cwd()
        try:
            os.chdir(self.folder)
            code, text = call("check-hash", "--text", "notes/proofs.md#Alpha",
                              "--reads", "gamma=notes/gamma.md")
            self.assertEqual(code, 0)
            self.assertEqual(text.splitlines(),
                             [f"content: {content}", "text:", text_line, "reads:", reads_line])
            self.assertEqual(call("check-hash", "--text", "notes/proofs.md#Missing")[0], 1)
            self.assertEqual(call("check-hash", "--text", "notes/gamma.md",
                                  "--reads", "two words=notes/gamma.md")[0], 1)
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

    def test_step_references_count_as_rules_and_raw_captures_do_not(self):
        skill = "docs/ai_methodology/skills/x/SKILL.md"
        command = ".claude/commands/x.md"
        raw = "docs/ai_methodology/raw/capture.md"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            remote = root / "remote.git"
            subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remote)],
                           check=True)
            seed = root / "seed"
            subprocess.run(["git", "clone", "-q", str(remote), str(seed)],
                           check=True, capture_output=True)
            for rel in (skill, command, raw):
                (seed / rel).parent.mkdir(parents=True)
                (seed / rel).write_text("one\n", encoding="utf-8")
            git("add", ".", cwd=seed)
            git("commit", "-q", "-m", "seed", cwd=seed)
            git("push", "-q", "origin", "HEAD:main", cwd=seed)
            work = root / "work"
            subprocess.run(["git", "clone", "-q", str(remote), str(work)],
                           check=True, capture_output=True)
            cwd = Path.cwd()
            try:
                os.chdir(work)
                (seed / raw).write_text("two\n", encoding="utf-8")
                git("commit", "-q", "-am", "raw capture", cwd=seed)
                git("push", "-q", "origin", "HEAD:main", cwd=seed)
                self.assertEqual(call("doctor")[0], 0)

                (seed / skill).write_text("two\n", encoding="utf-8")
                git("commit", "-q", "-am", "skill rule", cwd=seed)
                git("push", "-q", "origin", "HEAD:main", cwd=seed)
                code, text = call("doctor")
                self.assertEqual(code, 1)
                self.assertIn(f"differs: {skill}", text)
                self.assertNotIn(raw, text)
                self.assertNotIn(command, text)

                (seed / command).write_text("two\n", encoding="utf-8")
                git("commit", "-q", "-am", "command", cwd=seed)
                git("push", "-q", "origin", "HEAD:main", cwd=seed)
                self.assertIn(f"differs: {command}", call("doctor")[1])
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
