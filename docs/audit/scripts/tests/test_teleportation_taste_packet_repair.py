#!/usr/bin/env python3
"""Regression tests for the taste-readout restricted-packet repair."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import codex_audit_runner as audit_runner  # noqa: E402
import frontier_teleportation_taste_readout_operator_model as taste_runner  # noqa: E402


class TeleportationTastePacketRepairTest(unittest.TestCase):
    def test_authority_override_is_exactly_scoped(self) -> None:
        target = "teleportation_taste_readout_operator_model_note"
        authority = "teleportation_retained_axis_operator_algebra_closure_note"
        body = "x" * 13_927

        target_limit = audit_runner.authority_note_limit(target, authority, 1)
        unrelated_limit = audit_runner.authority_note_limit("other_claim", authority, 1)

        self.assertEqual(target_limit, 20_000)
        self.assertEqual(unrelated_limit, 10_000)
        self.assertNotIn(
            "packet-clipped",
            audit_runner.clip_packet_text(body, target_limit, authority),
        )
        self.assertIn(
            "packet-clipped",
            audit_runner.clip_packet_text(body, unrelated_limit, authority),
        )

    def test_boundary_statuses_are_validated_as_pairs(self) -> None:
        retained = taste_runner.BOUNDARY_STATUS_PAIRS[
            "teleportation_causal_channel_note"
        ]
        apparatus = taste_runner.BOUNDARY_STATUS_PAIRS[
            "teleportation_apparatus_dynamics_closure_note"
        ]

        self.assertIn(("retained_bounded", "audited_clean"), retained)
        self.assertNotIn(("retained_bounded", "audited_failed"), retained)
        self.assertIn(("audited_failed", "audited_failed"), apparatus)
        self.assertNotIn(("audited_failed", "audited_clean"), apparatus)


if __name__ == "__main__":
    unittest.main()
