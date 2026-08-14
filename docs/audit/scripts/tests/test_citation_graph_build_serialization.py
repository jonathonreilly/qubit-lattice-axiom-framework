"""Cross-checkout serialization tests for the citation-graph launcher."""
from __future__ import annotations

import fcntl
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import run_citation_graph_build as launcher


class CitationGraphBuildSerializationTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        self.origin = root / "origin.git"
        self.clone_a = root / "clone-a"
        self.clone_b = root / "clone-b"
        self.worktree = root / "worktree-a"

        self._git("init", "--bare", str(self.origin), cwd=root)
        self._git("clone", str(self.origin), str(self.clone_a), cwd=root)
        self._git("config", "user.name", "Citation Graph Test", cwd=self.clone_a)
        self._git(
            "config",
            "user.email",
            "citation-graph@example.invalid",
            cwd=self.clone_a,
        )
        scripts = self.clone_a / "docs" / "audit" / "scripts"
        scripts.mkdir(parents=True)
        shutil.copyfile(Path(launcher.__file__), scripts / Path(launcher.__file__).name)
        (scripts / "build_citation_graph.py").write_text(
            """\
import json
import os
import sys
import time
from pathlib import Path

marker = os.environ.get("CITATION_GRAPH_TEST_MARKER")
if marker:
    Path(marker).write_text("started", encoding="utf-8")
args_path = os.environ.get("CITATION_GRAPH_TEST_ARGS")
if args_path:
    Path(args_path).write_text(json.dumps(sys.argv[1:]), encoding="utf-8")
print("BUILDER_STARTED", flush=True)
time.sleep(float(os.environ.get("CITATION_GRAPH_TEST_SLEEP", "0")))
raise SystemExit(int(os.environ.get("CITATION_GRAPH_TEST_EXIT", "0")))
""",
            encoding="utf-8",
        )
        self._git("add", "docs/audit/scripts", cwd=self.clone_a)
        self._git("commit", "-m", "fixture", cwd=self.clone_a)
        self._git("push", "origin", "HEAD:main", cwd=self.clone_a)
        self._git("symbolic-ref", "HEAD", "refs/heads/main", cwd=self.origin)
        self._git("clone", str(self.origin), str(self.clone_b), cwd=root)
        self._git(
            "worktree",
            "add",
            "--detach",
            str(self.worktree),
            "HEAD",
            cwd=self.clone_a,
        )

    def tearDown(self):
        subprocess.run(
            ["git", "worktree", "remove", "--force", str(self.worktree)],
            cwd=self.clone_a,
            capture_output=True,
            text=True,
        )
        self.temporary.cleanup()

    def _git(self, *args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )

    def _lock_path(self, checkout: Path) -> Path:
        with mock.patch.object(launcher, "REPO_ROOT", checkout):
            return launcher.citation_graph_lock_path()

    def _launch(
        self,
        checkout: Path,
        *,
        extra_env: dict[str, str] | None = None,
        args: tuple[str, ...] = (),
    ) -> subprocess.Popen[str]:
        environment = os.environ.copy()
        environment.update(extra_env or {})
        script = checkout / "docs" / "audit" / "scripts" / Path(launcher.__file__).name
        return subprocess.Popen(
            [sys.executable, str(script), *args],
            cwd=checkout,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_independent_clones_and_worktree_share_lock_path(self):
        expected = self._lock_path(self.clone_a)
        self.assertEqual(expected, self._lock_path(self.clone_b))
        self.assertEqual(expected, self._lock_path(self.worktree))

    def test_independent_clone_waits_for_owner(self):
        marker = Path(self.temporary.name) / "acquired"
        lock_path = self._lock_path(self.clone_a)
        with lock_path.open("a+", encoding="utf-8") as owner:
            fcntl.flock(owner.fileno(), fcntl.LOCK_EX)
            child = self._launch(
                self.clone_b,
                extra_env={"CITATION_GRAPH_TEST_MARKER": str(marker)},
            )
            try:
                with self.assertRaises(subprocess.TimeoutExpired):
                    child.wait(timeout=0.2)
                self.assertFalse(marker.exists())
            except BaseException:
                child.kill()
                child.wait(timeout=5)
                raise
        stdout, stderr = child.communicate(timeout=5)
        self.assertEqual(child.returncode, 0, (stdout, stderr))
        self.assertEqual(marker.read_text(encoding="utf-8"), "started")
        self.assertIn("Waiting for serialized citation-graph build lock", stderr)

    def test_sigterm_releases_exec_inherited_lock(self):
        marker = Path(self.temporary.name) / "held"
        child = self._launch(
            self.clone_b,
            extra_env={
                "CITATION_GRAPH_TEST_MARKER": str(marker),
                "CITATION_GRAPH_TEST_SLEEP": "60",
            },
        )
        self.assertEqual(child.stdout.readline().strip(), "BUILDER_STARTED")
        self.assertEqual(marker.read_text(encoding="utf-8"), "started")
        child.terminate()
        child.wait(timeout=5)
        child.stdout.close()
        child.stderr.close()

        lock_path = self._lock_path(self.clone_a)
        with lock_path.open("a+", encoding="utf-8") as next_owner:
            fcntl.flock(next_owner.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

    def test_builder_exit_status_and_arguments_are_forwarded(self):
        args_path = Path(self.temporary.name) / "args.json"
        child = self._launch(
            self.clone_b,
            extra_env={
                "CITATION_GRAPH_TEST_ARGS": str(args_path),
                "CITATION_GRAPH_TEST_EXIT": "23",
            },
            args=("--probe", "value"),
        )
        stdout, stderr = child.communicate(timeout=5)
        self.assertEqual(child.returncode, 23, (stdout, stderr))
        self.assertEqual(args_path.read_text(encoding="utf-8"), '["--probe", "value"]')


if __name__ == "__main__":
    unittest.main()
