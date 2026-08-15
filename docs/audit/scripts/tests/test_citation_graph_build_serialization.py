"""Citation-graph serialization and review-loop landing-contract tests."""
from __future__ import annotations

import fcntl
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import run_citation_graph_build as launcher


REPO_ROOT = Path(__file__).resolve().parents[4]


class OperationalGraphBuildCommandTest(unittest.TestCase):
    def test_operational_commands_use_serialized_launcher(self):
        direct_command = re.compile(
            r"\bpython3\s+docs/audit/scripts/build_citation_graph\.py\b"
        )
        operational_paths = (
            ".claude/commands/workhorse.md",
            "docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md",
            "docs/ai_methodology/skills/physics-loop/SKILL.md",
            "docs/ai_methodology/skills/review-loop/SKILL.md",
            "docs/audit/README.md",
            "docs/audit/scripts/pre_commit_audit_check.sh",
            "docs/audit/scripts/run_pipeline.sh",
        )
        for relative in operational_paths:
            text = (REPO_ROOT / relative).read_text(encoding="utf-8")
            with self.subTest(path=relative):
                self.assertIsNone(direct_command.search(text))

        # References to the governed implementation remain valid; only direct
        # executable invocations bypass the serialization wrapper.
        conformance = (
            REPO_ROOT / "docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md"
        ).read_text(encoding="utf-8")
        self.assertIn("docs/audit/scripts/build_citation_graph.py", conformance)


class ReviewLoopLandingManifestContractTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.origin = self.root / "origin.git"
        self.worker = self.root / "worker"
        self._git("init", "--bare", str(self.origin), cwd=self.root)
        self._git("clone", str(self.origin), str(self.worker), cwd=self.root)
        self._git("config", "user.name", "Landing Loop Test", cwd=self.worker)
        self._git(
            "config",
            "user.email",
            "landing-loop@example.invalid",
            cwd=self.worker,
        )
        self._write_generator_stubs()
        (self.worker / ".gitignore").write_text(
            "docs/audit/data/citation_graph.json\n",
            encoding="utf-8",
        )
        (self.worker / "docs" / "mid.md").write_text("base\n", encoding="utf-8")
        (self.worker / "shared.txt").write_text("base\n", encoding="utf-8")
        self._run_generators()
        self._git("add", ".", cwd=self.worker)
        self._git("commit", "-m", "base", cwd=self.worker)
        self.base = self._git("rev-parse", "HEAD", cwd=self.worker).stdout.strip()
        self._git("branch", "-M", "main", cwd=self.worker)
        self._git("push", "origin", "HEAD:main", cwd=self.worker)
        self._git("symbolic-ref", "HEAD", "refs/heads/main", cwd=self.origin)

    def tearDown(self):
        self.temporary.cleanup()

    def _git(
        self,
        *args: str,
        cwd: Path,
        check: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=check,
            capture_output=True,
            text=True,
        )

    def _write_generator_stubs(self) -> None:
        scripts = self.worker / "docs" / "audit" / "scripts"
        scripts.mkdir(parents=True)
        shutil.copyfile(
            Path(launcher.__file__),
            scripts / "run_citation_graph_build.py",
        )
        (scripts / "build_citation_graph.py").write_text(
            """\
import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
nodes = {
    path.stem: {"deps": []}
    for path in sorted((root / "docs").glob("*.md"))
}
output = root / "docs" / "audit" / "data" / "citation_graph.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps({"nodes": nodes}, sort_keys=True) + "\\n")
""",
            encoding="utf-8",
        )
        (scripts / "write_citation_graph_manifest.py").write_text(
            """\
import json
import os
from pathlib import Path

root = Path(__file__).resolve().parents[3]
data = root / "docs" / "audit" / "data"
graph = json.loads((data / "citation_graph.json").read_text())
nodes = {
    node: {"deps_hash": "e3b0c44298fc", "out_degree": 0}
    for node in sorted(graph["nodes"])
}
manifest = {
    "edge_count": 0,
    "node_count": len(nodes),
    "nodes": nodes,
    "schema_version": 1,
}
(data / "citation_graph_manifest.json").write_text(
    json.dumps(manifest, indent=1, sort_keys=True) + "\\n"
)
marker = os.environ.get("LANDING_TEST_WRITER_FAIL_ONCE")
if marker and not Path(marker).exists():
    Path(marker).write_text("failed", encoding="utf-8")
    raise SystemExit(23)
""",
            encoding="utf-8",
        )

    def _run_generators(self) -> None:
        subprocess.run(
            [sys.executable, "docs/audit/scripts/run_citation_graph_build.py"],
            cwd=self.worker,
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            [sys.executable, "docs/audit/scripts/write_citation_graph_manifest.py"],
            cwd=self.worker,
            check=True,
            capture_output=True,
            text=True,
        )

    def _prepare_candidate_and_main(self, *, source_conflict: bool = False) -> str:
        self._git("switch", "-c", "candidate", self.base, cwd=self.worker)
        (self.worker / "docs" / "zzz.md").write_text(
            "candidate\n", encoding="utf-8"
        )
        if source_conflict:
            (self.worker / "shared.txt").write_text(
                "candidate\n", encoding="utf-8"
            )
        self._run_generators()
        self._git("add", "docs/zzz.md", cwd=self.worker)
        self._git(
            "add",
            "docs/audit/data/citation_graph_manifest.json",
            cwd=self.worker,
        )
        if source_conflict:
            self._git("add", "shared.txt", cwd=self.worker)
        self._git("commit", "-m", "topology candidate", cwd=self.worker)
        candidate = self._git("rev-parse", "HEAD", cwd=self.worker).stdout.strip()

        self._git("switch", "main", cwd=self.worker)
        (self.worker / "docs" / "aaa.md").write_text("main\n", encoding="utf-8")
        if source_conflict:
            (self.worker / "shared.txt").write_text("main\n", encoding="utf-8")
        self._run_generators()
        self._git("add", "docs/aaa.md", cwd=self.worker)
        self._git(
            "add",
            "docs/audit/data/citation_graph_manifest.json",
            cwd=self.worker,
        )
        if source_conflict:
            self._git("add", "shared.txt", cwd=self.worker)
        self._git("commit", "-m", "topology already on main", cwd=self.worker)
        self._git("push", "origin", "HEAD:main", cwd=self.worker)
        self._git("switch", "candidate", cwd=self.worker)
        return candidate

    def _landing_loop(self, commits: tuple[str, ...]) -> str:
        skill = (
            REPO_ROOT / "docs" / "ai_methodology" / "skills" /
            "review-loop" / "SKILL.md"
        ).read_text(encoding="utf-8")
        marker = "COMMITS=(<oldest-sha> ... <newest-sha>)"
        start = skill.index(marker)
        end = skill.index("```", start)
        loop = skill[start:end].replace(
            "<oldest-sha> ... <newest-sha>",
            " ".join(commits),
            1,
        )
        return "sleep() { :; }\n" + loop

    def _run_landing(
        self,
        commits: tuple[str, ...],
        *,
        extra_env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment.update(extra_env or {})
        return subprocess.run(
            ["bash", "-c", self._landing_loop(commits)],
            cwd=self.worker,
            env=environment,
            capture_output=True,
            text=True,
        )

    def _install_git_failure_wrapper(self) -> Path:
        binary_dir = self.root / "test-bin"
        binary_dir.mkdir()
        wrapper = binary_dir / "git"
        real_git = shutil.which("git")
        assert real_git is not None
        wrapper.write_text(
            f"""#!/bin/sh
if [ "$1" = fetch ] && [ -n "${{LANDING_TEST_FETCH_COUNT_FILE:-}}" ]; then
  count=$(cat "$LANDING_TEST_FETCH_COUNT_FILE" 2>/dev/null || echo 0)
  count=$((count + 1))
  printf '%s\\n' "$count" > "$LANDING_TEST_FETCH_COUNT_FILE"
  if [ "$count" = "${{LANDING_TEST_FAIL_FETCH_N:-0}}" ]; then
    exit 44
  fi
fi
if [ "$1" = push ] && [ "${{LANDING_TEST_FAIL_ALL_PUSHES:-}}" = 1 ]; then
  count=$(cat "$LANDING_TEST_PUSH_COUNT_FILE" 2>/dev/null || echo 0)
  printf '%s\\n' $((count + 1)) > "$LANDING_TEST_PUSH_COUNT_FILE"
  exit 45
fi
exec {shlex.quote(real_git)} "$@"
""",
            encoding="utf-8",
        )
        wrapper.chmod(0o755)
        return binary_dir

    def test_moved_main_retry_regenerates_and_preserves_both_advances(self):
        candidate = self._prepare_candidate_and_main()
        racer = self.root / "racer"
        self._git("clone", str(self.origin), str(racer), cwd=self.root)
        self._git("config", "user.name", "Race Test", cwd=racer)
        self._git("config", "user.email", "race@example.invalid", cwd=racer)
        (racer / "race.txt").write_text("moved main\n", encoding="utf-8")
        self._git("add", "race.txt", cwd=racer)
        self._git("commit", "-m", "independent main advance", cwd=racer)
        racer_commit = self._git("rev-parse", "HEAD", cwd=racer).stdout.strip()

        marker = self.root / "race-fired"
        hook = self.worker / ".git" / "hooks" / "pre-push"
        hook.write_text(
            "#!/bin/sh\n"
            f"if [ ! -e {shlex.quote(str(marker))} ]; then\n"
            f"  git -C {shlex.quote(str(racer))} push -q origin HEAD:main || exit 1\n"
            f"  touch {shlex.quote(str(marker))}\n"
            "fi\n",
            encoding="utf-8",
        )
        hook.chmod(0o755)
        self._git("config", "--unset-all", "remote.origin.fetch", cwd=self.worker)

        result = self._run_landing((candidate,))
        self.assertEqual(result.returncode, 0, (result.stdout, result.stderr))
        self.assertIn("LANDED ", result.stdout)
        self.assertTrue(marker.exists())
        self.assertEqual(
            self._git(
                "merge-base",
                "--is-ancestor",
                racer_commit,
                "origin/main",
                cwd=self.worker,
                check=False,
            ).returncode,
            0,
        )
        manifest = json.loads(
            self._git(
                "show",
                "origin/main:docs/audit/data/citation_graph_manifest.json",
                cwd=self.worker,
            ).stdout
        )
        self.assertEqual(manifest["node_count"], 3)
        self.assertEqual(sorted(manifest["nodes"]), ["aaa", "mid", "zzz"])

    def test_source_conflict_fails_without_push(self):
        candidate = self._prepare_candidate_and_main(source_conflict=True)
        before = self._git("rev-parse", "origin/main", cwd=self.worker).stdout.strip()
        result = self._run_landing((candidate,))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FAILED: source conflict", result.stderr)
        self._git(
            "fetch",
            "origin",
            "+refs/heads/main:refs/remotes/origin/main",
            cwd=self.worker,
        )
        self.assertEqual(
            self._git("rev-parse", "origin/main", cwd=self.worker).stdout.strip(),
            before,
        )

    def test_generated_manifest_residue_is_cleared_before_retry(self):
        candidate = self._prepare_candidate_and_main()
        failure_marker = self.root / "writer-failed"
        result = self._run_landing(
            (candidate,),
            extra_env={"LANDING_TEST_WRITER_FAIL_ONCE": str(failure_marker)},
        )
        self.assertEqual(result.returncode, 0, (result.stdout, result.stderr))
        self.assertTrue(failure_marker.exists())
        self.assertIn("LANDED ", result.stdout)

    def test_failed_containment_fetch_cannot_report_landed(self):
        candidate = self._prepare_candidate_and_main()
        binary_dir = self._install_git_failure_wrapper()
        fetch_count = self.root / "fetch-count"
        result = self._run_landing(
            (candidate,),
            extra_env={
                "PATH": f"{binary_dir}{os.pathsep}{os.environ['PATH']}",
                "LANDING_TEST_FETCH_COUNT_FILE": str(fetch_count),
                "LANDING_TEST_FAIL_FETCH_N": "2",
            },
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("LANDED ", result.stdout)
        self.assertIn("could not refresh origin/main", result.stderr)

    def test_four_failed_pushes_exhaust_without_success(self):
        candidate = self._prepare_candidate_and_main()
        binary_dir = self._install_git_failure_wrapper()
        push_count = self.root / "push-count"
        result = self._run_landing(
            (candidate,),
            extra_env={
                "PATH": f"{binary_dir}{os.pathsep}{os.environ['PATH']}",
                "LANDING_TEST_FAIL_ALL_PUSHES": "1",
                "LANDING_TEST_PUSH_COUNT_FILE": str(push_count),
            },
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(push_count.read_text(encoding="utf-8").strip(), "4")
        self.assertNotIn("LANDED ", result.stdout)
        self.assertIn("did not complete after 4 attempts", result.stderr)


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

    def _set_origin(self, checkout: Path, url: str) -> None:
        self._git("remote", "set-url", "origin", url, cwd=checkout)

    def _init_repo(self, checkout: Path) -> None:
        self._git("init", str(checkout), cwd=checkout.parent)
        self._git("config", "user.name", "Citation Graph Test", cwd=checkout)
        self._git(
            "config",
            "user.email",
            "citation-graph@example.invalid",
            cwd=checkout,
        )
        self._git("commit", "--allow-empty", "-m", "fixture", cwd=checkout)

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

    def test_renamed_github_remotes_share_lock_and_serialize(self):
        marker = Path(self.temporary.name) / "renamed-acquired"
        self._set_origin(
            self.clone_a,
            "git@github.com:jonathonreilly/cl3-lattice-framework.git",
        )
        self._set_origin(
            self.clone_b,
            "https://github.com/jonathonreilly/qubit-lattice-axiom-framework.git",
        )

        lock_path = self._lock_path(self.clone_a)
        self.assertEqual(lock_path, self._lock_path(self.clone_b))
        self.assertEqual(lock_path, self._lock_path(self.worktree))
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

    def test_github_remote_normalization_matrix(self):
        expected = "github:jonathonreilly/qubit-lattice-axiom-framework"
        equivalents = (
            "https://github.com/jonathonreilly/cl3-lattice-framework",
            "HTTP://GITHUB.COM/JONATHONREILLY/CL3-LATTICE-FRAMEWORK.GIT///",
            "https://user-a:secret-a@github.com:443/"
            "jonathonreilly/cl3-lattice-framework.git",
            "git://github.com:9418/jonathonreilly/"
            "qubit-lattice-axiom-framework.git",
            "git@github.com:jonathonreilly/cl3-lattice-framework.git",
            "ssh://git@github.com:22/jonathonreilly/"
            "qubit-lattice-axiom-framework/",
        )
        for remote in equivalents:
            with self.subTest(remote=remote):
                identity = launcher._canonical_remote_identity(remote)
                self.assertEqual(identity, expected)
                self.assertNotIn("secret", identity)

        self.assertNotEqual(
            launcher._canonical_remote_identity(
                "https://github.com/jonathonreilly/unrelated-repository.git"
            ),
            expected,
        )
        non_github = launcher._canonical_remote_identity(
            "https://user-b:secret-b@gitlab.com/"
            "jonathonreilly/qubit-lattice-axiom-framework.git"
        )
        self.assertNotEqual(non_github, expected)
        self.assertNotIn("user-b", non_github)
        self.assertNotIn("secret-b", non_github)

    def test_distinct_relative_local_origins_keep_distinct_locks(self):
        checkouts = []
        for name in ("relative-a", "relative-b"):
            parent = Path(self.temporary.name) / name
            origin = parent / "origin.git"
            checkout = parent / "checkout"
            parent.mkdir()
            self._git("init", "--bare", str(origin), cwd=parent)
            self._init_repo(checkout)
            self._git("remote", "add", "origin", "../origin.git", cwd=checkout)
            checkouts.append(checkout)

        self.assertNotEqual(
            self._lock_path(checkouts[0]),
            self._lock_path(checkouts[1]),
        )

    def test_no_origin_worktree_shares_lock_but_unrelated_repo_does_not(self):
        root = Path(self.temporary.name)
        checkout = root / "no-origin"
        linked = root / "no-origin-linked"
        unrelated = root / "no-origin-unrelated"
        self._init_repo(checkout)
        self._init_repo(unrelated)
        self._git(
            "worktree",
            "add",
            "--detach",
            str(linked),
            "HEAD",
            cwd=checkout,
        )
        try:
            self.assertEqual(self._lock_path(checkout), self._lock_path(linked))
            self.assertNotEqual(
                self._lock_path(checkout),
                self._lock_path(unrelated),
            )
        finally:
            subprocess.run(
                ["git", "worktree", "remove", "--force", str(linked)],
                cwd=checkout,
                capture_output=True,
                text=True,
            )

    def test_unrelated_github_repository_keeps_a_distinct_lock(self):
        self._set_origin(
            self.clone_a,
            "https://github.com/jonathonreilly/cl3-lattice-framework.git",
        )
        self._set_origin(
            self.clone_b,
            "https://github.com/jonathonreilly/unrelated-repository.git",
        )
        self.assertNotEqual(
            self._lock_path(self.clone_a),
            self._lock_path(self.clone_b),
        )

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
        lock_path = self._lock_path(self.clone_a)
        with lock_path.open("a+", encoding="utf-8") as contender:
            try:
                with self.assertRaises(BlockingIOError):
                    fcntl.flock(
                        contender.fileno(),
                        fcntl.LOCK_EX | fcntl.LOCK_NB,
                    )
            finally:
                child.terminate()
                child.wait(timeout=5)
                child.stdout.close()
                child.stderr.close()
            fcntl.flock(contender.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

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
