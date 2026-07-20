"""Fail-closed regression tests for the D3 committed-evidence manifest."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
RUNNER_PATH = SCRIPT_DIR / "d3_bar_window_measurement_2026_07_11.py"
SPEC = importlib.util.spec_from_file_location("d3_bar_window_evidence", RUNNER_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {RUNNER_PATH}")
runner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runner
SPEC.loader.exec_module(runner)


class CommittedEvidenceManifestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = json.loads(runner.EVIDENCE_MANIFEST_PATH.read_text())
        self.identity = runner._identity()

    def _load(self, payload: dict) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with mock.patch.object(runner, "EVIDENCE_MANIFEST_PATH", path):
                return runner._load_completion_manifest(self.identity)

    def test_committed_manifest_authenticates(self) -> None:
        loaded = self._load(copy.deepcopy(self.payload))
        self.assertEqual(loaded["schema"], runner.EVIDENCE_MANIFEST_SCHEMA)

    def test_deleting_any_required_map_entry_fails_closed(self) -> None:
        for map_name in (
            "generation_sources",
            "reporter_sources",
            "generation_blobs",
            "artifacts",
            "cases",
        ):
            with self.subTest(map_name=map_name):
                payload = copy.deepcopy(self.payload)
                first_key = next(iter(payload[map_name]))
                del payload[map_name][first_key]
                with self.assertRaises(RuntimeError):
                    self._load(payload)

    def test_historical_generation_blob_identity_is_required(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["generation_blobs"][runner.HISTORICAL_GENERATION_RUNNER] = "0" * 40
        with self.assertRaises(RuntimeError):
            self._load(payload)

    def test_case_stream_hash_must_match_artifact_map(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["cases"]["lam_0p02"]["stream_sha256"] = "0" * 64
        with self.assertRaises(RuntimeError):
            self._load(payload)


if __name__ == "__main__":
    unittest.main()
