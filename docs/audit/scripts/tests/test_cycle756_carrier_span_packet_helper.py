"""Packet-consumer parity for the Cycle 756 carrier-span sibling checker."""
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
    spec = importlib.util.spec_from_file_location("cycle756_packet_deps", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Cycle756CarrierSpanPacketHelperTest(unittest.TestCase):
    CLAIM_ID = (
        "physical_cell_cutting_blind_space_carrier_span_cycle756_note_2026-08-09"
    )
    PRIMARY = (
        "scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_2026_08_09.py"
    )
    HELPER = (
        "scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_"
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
