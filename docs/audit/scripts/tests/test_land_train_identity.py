"""The landing loop refuses a clone whose commits would carry no set email."""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[4]
LANDING_SCRIPT = REPO_ROOT / "docs/ai_methodology/skills/review-loop/scripts/land_train.sh"
IDENTITY_LINE = (
    "FAILED: git user.email is not set: a landed commit would carry a committer "
    "address made from the host name, in a public repository. Set git config "
    "user.name and user.email in this clone."
)
SHAS = ("1" * 40, "2" * 40, "3" * 40, "4" * 40)
TRAIN = (
    f"VALIDATED_BASE={SHAS[0]}\n"
    f"VALIDATED_TREE={SHAS[1]}\n"
    f"COMMITS={SHAS[2]} {SHAS[3]}\n"
    "PR_NUMBERS=1 2\n"
    f"PR_HEADS={SHAS[2]} {SHAS[3]}\n"
    "PR_HEAD_REFS=unit-1 unit-2\n"
    f"PR_TIPS={SHAS[2]} {SHAS[3]}\n"
)


@unittest.skipUnless(shutil.which("git") and shutil.which("bash"), "requires Git and Bash")
class LandingIdentityTest(unittest.TestCase):
    def run_loop(self, email: str | None) -> dict:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            empty = root / "empty.gitconfig"
            empty.write_text("", encoding="utf-8")
            env = {k: v for k, v in os.environ.items()
                   if not k.startswith(("GIT_", "EMAIL"))}
            env.update(GIT_CONFIG_GLOBAL=str(empty), GIT_CONFIG_SYSTEM=os.devnull,
                       GIT_CONFIG_NOSYSTEM="1", GIT_CEILING_DIRECTORIES=str(root))

            def git(cwd: Path, *args: str) -> str:
                return subprocess.run(["git", *args], cwd=cwd, env=env, text=True,
                                      capture_output=True, check=True).stdout

            remote, seed, work = root / "remote.git", root / "seed", root / "work"
            git(root, "init", "-q", "--bare", "-b", "main", str(remote))
            git(root, "init", "-q", "-b", "main", str(seed))
            (seed / "a.txt").write_text("a\n", encoding="utf-8")
            git(seed, "add", ".")
            git(seed, "-c", "user.name=t", "-c", "user.email=t@example.org",
                "-c", "commit.gpgsign=false", "commit", "-qm", "seed")
            git(seed, "push", "-q", str(remote), "HEAD:main")
            git(root, "init", "-q", "-b", "main", str(work))
            git(work, "remote", "add", "origin", str(remote))
            if email:
                git(work, "config", "user.email", email)
            train = root / "train.txt"
            train.write_text(TRAIN, encoding="utf-8")
            proc = subprocess.run(["bash", str(LANDING_SCRIPT), str(train)], cwd=work,
                                  env=env, text=True, capture_output=True, timeout=120)
            return {
                "exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                "refs": git(work, "for-each-ref"),
                "fetched": (work / ".git" / "FETCH_HEAD").exists(),
                "commits": git(work, "rev-list", "--all"),
                "remote_refs": git(remote, "for-each-ref"),
            }

    def test_no_email_refuses_before_any_fetch_commit_or_ref(self):
        result = self.run_loop(None)
        self.assertEqual(result["exit"], 1, result)
        self.assertEqual(result["stdout"], "", result)
        self.assertEqual(result["stderr"], IDENTITY_LINE + "\n", result)
        self.assertEqual(result["refs"], "", result)
        self.assertEqual(result["commits"], "", result)
        self.assertFalse(result["fetched"], result)
        self.assertEqual(result["remote_refs"].count("\n"), 1, result)

    def test_an_email_gets_past_the_guard_and_fails_later(self):
        result = self.run_loop("lander@example.org")
        self.assertEqual(result["exit"], 1, result)
        self.assertNotIn("user.email", result["stderr"], result)
        # The made-up commits draw git's own "bad object" lines before it.
        self.assertTrue(result["stderr"].endswith(
            "\nFAILED: main moved; rebuild and rerun the combined gate\n"), result)
        self.assertTrue(result["fetched"], "the loop reached its fetch")


if __name__ == "__main__":
    unittest.main()
