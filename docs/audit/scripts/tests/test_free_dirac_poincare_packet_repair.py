#!/usr/bin/env python3
"""Regression tests for the free-Dirac authority packet repair."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import codex_audit_runner as audit_runner  # noqa: E402


TARGET = "free_dirac_poincare_representation_bounded_note_2026-05-30"
AUTHORITY = (
    "free_staggered_pole_residue_dirac_carrier_car_relabeling_"
    "bounded_theorem_note_2026-07-17"
)
PROMPT_TEMPLATE = REPO_ROOT / "docs" / "audit" / "AUDIT_AGENT_PROMPT_TEMPLATE.md"


def ledger_row(claim_id: str) -> dict:
    path = (
        REPO_ROOT
        / "docs"
        / "audit"
        / "data"
        / "ledger"
        / claim_id[:2]
        / f"{claim_id}.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


class FreeDiracPoincarePacketRepairTest(unittest.TestCase):
    def test_authority_override_is_exactly_scoped(self) -> None:
        body = "x" * 20_118

        target_limit = audit_runner.authority_note_limit(TARGET, AUTHORITY, 1)
        unrelated_limit = audit_runner.authority_note_limit(
            "unrelated_claim", AUTHORITY, 1
        )

        self.assertEqual(target_limit, 22_000)
        self.assertEqual(unrelated_limit, 10_000)
        self.assertNotIn(
            "packet-clipped",
            audit_runner.clip_packet_text(body, target_limit, AUTHORITY),
        )
        self.assertIn(
            "packet-clipped",
            audit_runner.clip_packet_text(body, unrelated_limit, AUTHORITY),
        )

    def test_restricted_prompt_contains_complete_real_authority(self) -> None:
        ledger_rows = audit_runner.load_ledger_rows()
        target_row = ledger_rows[TARGET]
        authority_row = ledger_row(AUTHORITY)
        authority_note_path = authority_row["note_path"]
        authority_body = (REPO_ROOT / authority_note_path).read_text(
            encoding="utf-8"
        )
        manifest: dict[str, dict] = {}

        prompt = audit_runner.render_prompt(
            target_row,
            ledger_rows,
            PROMPT_TEMPLATE.read_text(encoding="utf-8"),
            runner_timeout_sec=120,
            use_cache=True,
            evidence_manifest_out=manifest,
            audit_invocation_id="free-dirac-packet-regression",
        )
        fitted_prompt, transport_bound = audit_runner.fit_prompt_to_transport_limit(
            prompt,
            manifest,
            TARGET,
        )

        self.assertEqual(manifest[authority_note_path]["text"], authority_body)
        self.assertIsNone(transport_bound)
        self.assertEqual(fitted_prompt.count(authority_body), 1)
        self.assertNotIn("packet-clipped", manifest[authority_note_path]["text"])
        clipped_load_bearing = {
            path
            for path, entry in manifest.items()
            if entry.get("role") in audit_runner.LOAD_BEARING_EVIDENCE_ROLES
            and any(
                marker in str(entry.get("text", ""))
                for marker in audit_runner.CLIPPED_EVIDENCE_MARKERS
            )
        }
        self.assertEqual(clipped_load_bearing, set())
        for section in (
            "## 2. Finite-spacing pole and residue",
            "## 3. Dirac spectral fibers at finite spacing",
            "## 4. Continuum carrier and universal-cover Poincare action",
            "## 5. Finite CAR construction and antiparticle relabelling",
        ):
            self.assertIn(section, manifest[authority_note_path]["text"])


if __name__ == "__main__":
    unittest.main()
