"""Tests for the guard keeping science replay independent of process documents."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_runner_process_inputs as guard  # noqa: E402

DOC = "docs/ai_methodology/SCIENCE_WORKFLOW.md"
DIGEST = hashlib.sha256(b"old\n").hexdigest()


class GuardTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        subprocess.run(["git", "add", "--", rel], cwd=self.root, check=True)

    def pin_manifest(self):
        self.write("outputs/x_inputs/ARTIFACT_MANIFEST.json", json.dumps(
            {"files": [{"path": DOC, "bytes": 4, "sha256": DIGEST}]}
        ))

    def snapshot(self, content="old\n"):
        self.write("outputs/x/originals/WORKFLOW.md", content)
        self.write("outputs/x/PROCESS_INPUT_SNAPSHOTS.json", json.dumps({"files": {
            DOC: {"original": {"bytes": 4, "sha256": DIGEST},
                  "original_snapshot": "outputs/x/originals/WORKFLOW.md"},
        }}))

    def reviewed_routing(self):
        source = "# fixture representing a reviewed routing implementation\n"
        self.write("scripts/replay.py", source)
        contract = {"runner": "scripts/replay.py",
                    "runner_sha256": hashlib.sha256(source.encode()).hexdigest(),
                    "snapshots": "outputs/x/PROCESS_INPUT_SNAPSHOTS.json"}
        mock = patch.dict(guard.REVIEWED_REPLAY_PACKAGES,
                          {"outputs/x_inputs": contract}, clear=True)
        mock.start()
        self.addCleanup(mock.stop)

    def test_runner_declaring_a_live_process_doc_is_found(self):
        self.write("scripts/live.py", f"AUDIT_INPUT_PATHS = ('{DOC}', 'docs/NOTE.md')\n")
        self.write("scripts/clean.py", "AUDIT_INPUT_PATHS = ('docs/NOTE.md',)\n# docs/ai_methodology/x.md\n")
        found = guard.declared_process_inputs(self.root)
        self.assertEqual(found, {"scripts/live.py": [DOC]})

    def test_annotated_declaration_is_found(self):
        self.write("scripts/live.py", f"AUDIT_INPUT_PATHS: tuple[str, ...] = ('{DOC}',)\n")
        self.assertEqual(guard.declared_process_inputs(self.root), {"scripts/live.py": [DOC]})

    def test_known_runner_cannot_add_a_live_input(self):
        runner, known = next(iter(guard.KNOWN_LIVE_INPUTS.items()))
        declared = {key: list(value) for key, value in guard.KNOWN_LIVE_INPUTS.items()}
        self.assertEqual(guard.unexpected_live_inputs(declared), [])
        declared[runner] = [*known, DOC]
        self.assertIn(DOC, guard.unexpected_live_inputs(declared)[0])

    def test_removed_known_input_requires_baseline_cleanup(self):
        declared = {key: list(value) for key, value in guard.KNOWN_LIVE_INPUTS.items()}
        del declared[next(iter(declared))]
        self.assertIn('stale', guard.unexpected_live_inputs(declared)[0])

    def test_live_manifest_pin_without_snapshot_is_a_problem(self):
        self.pin_manifest()
        self.assertIn("pins live", guard.unresolved_manifest_pins(self.root)[0])

    def test_pin_resolved_by_matching_snapshot_passes(self):
        self.pin_manifest()
        self.snapshot()
        self.reviewed_routing()
        self.assertEqual(guard.unresolved_manifest_pins(self.root), [])

    def test_unrelated_snapshot_does_not_excuse_live_package(self):
        self.pin_manifest()
        self.snapshot()
        self.assertIn('without reviewed package routing', guard.unresolved_manifest_pins(self.root)[0])

    def test_changed_resolver_is_rejected(self):
        self.pin_manifest()
        self.snapshot()
        self.reviewed_routing()
        self.write('scripts/replay.py', '# now reads live files\n')
        self.assertIn('routing source changed', guard.unresolved_manifest_pins(self.root)[0])

    def test_missing_snapshot_map_is_rejected(self):
        self.pin_manifest()
        self.reviewed_routing()
        self.assertIn('snapshot map missing', guard.unresolved_manifest_pins(self.root)[0])

    def test_missing_snapshot_file_is_rejected(self):
        self.pin_manifest()
        self.snapshot()
        self.reviewed_routing()
        (self.root / 'outputs/x/originals/WORKFLOW.md').unlink()
        self.assertIn('does not match', guard.unresolved_manifest_pins(self.root)[0])

    def test_other_snapshot_map_cannot_override_package_selection(self):
        self.pin_manifest()
        self.snapshot()
        self.reviewed_routing()
        self.write('outputs/z/PROCESS_INPUT_SNAPSHOTS.json', json.dumps({'files': {
            DOC: {'original_snapshot': 'missing.md'},
        }}))
        self.assertEqual(guard.unresolved_manifest_pins(self.root), [])

    def test_snapshot_cannot_redirect_to_live_or_external_path(self):
        self.pin_manifest()
        self.snapshot()
        self.reviewed_routing()
        self.write(DOC, 'old\n')
        for target in (DOC, str(self.root / DOC), 'outputs/../' + DOC,
                       'outputs/x/untracked.md'):
            with self.subTest(target=target):
                self.write('outputs/x/PROCESS_INPUT_SNAPSHOTS.json', json.dumps({'files': {
                    DOC: {'original_snapshot': target},
                }}))
                self.assertIn('not tracked package storage', guard.unresolved_manifest_pins(self.root)[0])

    def test_snapshot_symlink_to_live_file_is_rejected(self):
        self.pin_manifest()
        self.snapshot()
        self.reviewed_routing()
        self.write(DOC, 'old\n')
        snapshot = self.root / 'outputs/x/originals/WORKFLOW.md'
        snapshot.unlink()
        snapshot.symlink_to(self.root / DOC)
        self.assertIn('symlink', guard.unresolved_manifest_pins(self.root)[0])

    def test_snapshot_with_different_bytes_is_a_problem(self):
        self.pin_manifest()
        self.snapshot("tampered\n")
        self.reviewed_routing()
        self.assertIn("does not match", guard.unresolved_manifest_pins(self.root)[0])

    def test_science_paths_are_not_process_documents(self):
        for path in ("docs/NOTE.md", "docs/ai_methodology/raw/old.md", "outputs/x.json"):
            self.assertIsNone(guard.PROCESS_PATH_RE.match(path), path)


class RepositoryTest(unittest.TestCase):
    def test_repository_has_no_new_process_dependency(self):
        self.assertEqual(guard.unresolved_manifest_pins(guard.REPO_ROOT), [])
        self.assertEqual(guard.unexpected_live_inputs(guard.declared_process_inputs(guard.REPO_ROOT)), [])


if __name__ == "__main__":
    unittest.main()
