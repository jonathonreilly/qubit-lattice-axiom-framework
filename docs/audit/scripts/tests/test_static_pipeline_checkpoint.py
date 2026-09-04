#!/usr/bin/env python3
"""Regression tests for the full-pipeline static checkpoint."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PROJECT_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(PROJECT_ROOT))

from docs.audit.scripts import static_pipeline_checkpoint as checkpoint


class StaticInputFingerprintTest(unittest.TestCase):
    def test_seed_deleted_tracked_shard_is_not_reopened(self) -> None:
        """The seed receipt fingerprints the post-seed filesystem, not index ghosts."""
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            data = repo / "docs" / "audit" / "data"
            ledger = data / "ledger" / "aa"
            scripts = repo / "scripts"
            ledger.mkdir(parents=True)
            scripts.mkdir()
            live = ledger / "live.json"
            live.write_text('{"claim_id": "live", "runner_path": null}\n')

            tracked_listing = "\n".join(
                (
                    "docs/audit/data/ledger/aa/deleted.json",
                    "docs/audit/data/ledger/aa/live.json",
                )
            ) + "\n"
            listed = subprocess.CompletedProcess(
                args=["git", "ls-files"],
                returncode=0,
                stdout=tracked_listing,
                stderr="",
            )

            with (
                mock.patch.object(checkpoint, "REPO_ROOT", repo),
                mock.patch.object(checkpoint, "DATA", data),
                mock.patch.object(checkpoint, "run_git", return_value=listed),
            ):
                digest, detail = checkpoint.static_input_fingerprint()

            self.assertIsNotNone(digest, detail)
            self.assertEqual("static input tree fingerprinted", detail)


if __name__ == "__main__":
    unittest.main()
