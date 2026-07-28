#!/usr/bin/env python3
"""Regression tests for the taste-readout restricted-packet repair."""

from __future__ import annotations

import json
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

    def test_restricted_prompt_contains_complete_real_authority(self) -> None:
        target = "teleportation_taste_readout_operator_model_note"
        authority = "teleportation_retained_axis_operator_algebra_closure_note"
        target_path = (
            REPO_ROOT / "docs" / "audit" / "data" / "ledger" / "te" / f"{target}.json"
        )
        authority_path = (
            REPO_ROOT
            / "docs"
            / "audit"
            / "data"
            / "ledger"
            / "te"
            / f"{authority}.json"
        )
        target_row = json.loads(target_path.read_text(encoding="utf-8"))
        authority_row = json.loads(authority_path.read_text(encoding="utf-8"))
        authority_note_path = authority_row["note_path"]
        authority_body = (REPO_ROOT / authority_note_path).read_text(encoding="utf-8")
        manifest: dict[str, dict] = {}

        prompt = audit_runner.render_prompt(
            target_row,
            {target: target_row, authority: authority_row},
            (
                "{{FOREACH cited_authority IN CITED_AUTHORITIES}}"
                "{{ENDFOREACH}}"
            ),
            runner_timeout_sec=1,
            skip_runner_stdout=True,
            evidence_manifest_out=manifest,
        )

        self.assertEqual(manifest[authority_note_path]["text"], authority_body)
        self.assertIn(authority_body, prompt)
        self.assertNotIn("packet-clipped", manifest[authority_note_path]["text"])

    def test_only_real_dependency_is_a_status_gate(self) -> None:
        results = taste_runner.teleportation_boundary_check_results(REPO_ROOT)
        status_rows = results[: len(taste_runner.BOUNDARY_CLAIM_IDS)]
        gated = {
            claim_id
            for claim_id, (_, passed, _) in zip(
                taste_runner.BOUNDARY_CLAIM_IDS, status_rows, strict=True
            )
            if passed is not None
        }

        self.assertEqual(gated, taste_runner.LOAD_BEARING_DEPENDENCY_IDS)
        for effective in taste_runner.RETAINED_EFFECTIVE_STATUSES:
            self.assertTrue(
                taste_runner.is_retained_grade({"effective_status": effective})
            )
        for effective in (
            "audited_conditional",
            "audited_failed",
            "audited_renaming",
            "open_gate",
        ):
            self.assertFalse(
                taste_runner.is_retained_grade({"effective_status": effective})
            )


if __name__ == "__main__":
    unittest.main()
