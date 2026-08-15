"""Packet-consumer parity for the circulant spectral-fold sibling checker."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
AUDIT_SCRIPTS = REPO_ROOT / "docs" / "audit" / "scripts"
sys.path.insert(0, str(AUDIT_SCRIPTS))

import build_citation_graph  # noqa: E402


def _load_packet_dependencies():
    path = REPO_ROOT / "scripts" / "audit_packet_script_deps.py"
    spec = importlib.util.spec_from_file_location("circulant_packet_deps", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CirculantSpectralFoldPacketHelperTest(unittest.TestCase):
    CLAIM_ID = "circulant_spectral_fold_exact_algebra_support_note_2026-08-09"
    PRIMARY = "scripts/salvaged_circulant_spectral_fold_2026_08_09.py"
    HELPER = (
        "scripts/salvaged_circulant_spectral_fold_"
        "independent_check_2026_08_09.py"
    )

    def test_both_packet_consumers_resolve_exactly_the_independent_checker(self):
        packet_dependencies = _load_packet_dependencies()
        expected = [self.HELPER]
        self.assertEqual(
            build_citation_graph.helper_runner_paths_for_claim(
                self.CLAIM_ID, self.PRIMARY
            ),
            expected,
        )
        self.assertEqual(
            packet_dependencies.helper_runner_paths_for_claim(
                self.CLAIM_ID, Path(self.PRIMARY).stem
            ),
            expected,
        )


if __name__ == "__main__":
    unittest.main()
