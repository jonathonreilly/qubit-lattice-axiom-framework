"""Tests for the guard keeping science replay independent of process documents."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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

    def test_runner_declaring_a_live_process_doc_is_found(self):
        self.write("scripts/live.py", f"AUDIT_INPUT_PATHS = ('{DOC}', 'docs/NOTE.md')\n")
        self.write("scripts/clean.py", "AUDIT_INPUT_PATHS = ('docs/NOTE.md',)\n# docs/ai_methodology/x.md\n")
        found = guard.declared_process_inputs(self.root)
        self.assertEqual(found, {"scripts/live.py": [DOC]})

    def test_live_manifest_pin_without_snapshot_is_a_problem(self):
        self.pin_manifest()
        self.assertIn("pins live", guard.unresolved_manifest_pins(self.root)[0])

    def test_pin_resolved_by_matching_snapshot_passes(self):
        self.pin_manifest()
        self.snapshot()
        self.assertEqual(guard.unresolved_manifest_pins(self.root), [])

    def test_snapshot_with_different_bytes_is_a_problem(self):
        self.pin_manifest()
        self.snapshot("tampered\n")
        self.assertIn("does not match", guard.unresolved_manifest_pins(self.root)[0])

    def test_science_paths_are_not_process_documents(self):
        for path in ("docs/NOTE.md", "docs/ai_methodology/raw/old.md", "outputs/x.json"):
            self.assertIsNone(guard.PROCESS_PATH_RE.match(path), path)


class RepositoryTest(unittest.TestCase):
    def test_repository_has_no_new_process_dependency(self):
        self.assertEqual(guard.unresolved_manifest_pins(guard.REPO_ROOT), [])
        self.assertEqual(set(guard.declared_process_inputs(guard.REPO_ROOT)), guard.KNOWN_LIVE_INPUTS)


if __name__ == "__main__":
    unittest.main()
