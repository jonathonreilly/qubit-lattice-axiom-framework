#!/usr/bin/env python3
"""Regression tests for the Cycle 873 authority packet repair."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import codex_audit_runner as audit_runner  # noqa: E402


TARGET = (
    "recurrent_f17_uniform_affine_open_box_cycle873_"
    "bounded_theorem_note_2026-08-03"
)
AUTHORITIES = {
    "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-29.md",
    (
        "openreference_cubic_recurrent_physical_m2_matter_compiler_"
        "cycle870_bounded_theorem_note_2026-08-02"
    ): (
        "docs/OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_"
        "CYCLE870_BOUNDED_THEOREM_NOTE_2026-08-02.md"
    ),
    (
        "openreference_matter_endpoint_causal_interval_packet_cycle871_"
        "bounded_theorem_note_2026-08-02"
    ): (
        "docs/OPENREFERENCE_MATTER_ENDPOINT_CAUSAL_INTERVAL_PACKET_"
        "CYCLE871_BOUNDED_THEOREM_NOTE_2026-08-02.md"
    ),
    (
        "physical_m2_full34_fixed_packet_composition_cycle714_"
        "bounded_theorem_note_2026-07-26"
    ): (
        "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_"
        "CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md"
    ),
}


class Cycle873AuthorityPacketRepairTest(unittest.TestCase):
    def test_all_four_real_authorities_are_complete_only_for_target(self) -> None:
        total = 0
        for authority, relative_path in AUTHORITIES.items():
            body = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            target_limit = audit_runner.authority_note_limit(
                TARGET, authority, len(AUTHORITIES)
            )
            unrelated_limit = audit_runner.authority_note_limit(
                "unrelated_claim", authority, len(AUTHORITIES)
            )
            total += target_limit
            self.assertGreaterEqual(target_limit, len(body))
            self.assertNotIn(
                "packet-clipped",
                audit_runner.clip_packet_text(body, target_limit, authority),
            )
            self.assertIn(
                "packet-clipped",
                audit_runner.clip_packet_text(body, unrelated_limit, authority),
            )

        self.assertEqual(total, 73_000)
        self.assertLess(total, audit_runner.CODEX_INPUT_CHAR_LIMIT)


if __name__ == "__main__":
    unittest.main()
