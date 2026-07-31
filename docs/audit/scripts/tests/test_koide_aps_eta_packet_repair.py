#!/usr/bin/env python3
"""Regression tests for the Koide APS eta restricted-packet repair."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import codex_audit_runner as audit_runner  # noqa: E402
import runner_cache  # noqa: E402


TARGET = "koide_aps_eta_topological_robustness_bounded_theorem_note_2026-07-02"
AUTHORITY = "koide_aps_block_by_block_forcing_note_2026-04-21"
RUNNER = "scripts/frontier_koide_aps_topological_robustness.py"


class KoideApsEtaPacketRepairTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = audit_runner.ledger_io.load_ledger()["rows"]
        cls.target_row = cls.rows[TARGET]
        cls.authority_row = cls.rows[AUTHORITY]

    def test_authority_override_is_exactly_scoped(self) -> None:
        body = "x" * 12_320

        target_limit = audit_runner.authority_note_limit(TARGET, AUTHORITY, 2)
        unrelated_limit = audit_runner.authority_note_limit(
            "other_claim",
            AUTHORITY,
            2,
        )

        self.assertEqual(target_limit, 20_000)
        self.assertEqual(unrelated_limit, 10_000)
        self.assertNotIn(
            "packet-clipped",
            audit_runner.clip_packet_text(body, target_limit, AUTHORITY),
        )
        self.assertIn(
            "packet-clipped",
            audit_runner.clip_packet_text(body, unrelated_limit, AUTHORITY),
        )

    def test_cached_stdout_uses_current_transport_budget(self) -> None:
        cache_path, header, body = runner_cache.load_cache(RUNNER)
        self.assertIsNotNone(cache_path)
        self.assertIsNotNone(header)
        self.assertIsNotNone(body)
        assert cache_path is not None
        assert header is not None
        assert body is not None

        self.assertGreater(len(body), 6_000)
        self.assertLessEqual(len(body), audit_runner.RUNNER_STDOUT_CHAR_LIMIT)
        expected = (
            f"[runner cache hit: {cache_path.name}, "
            f"sha {header['runner_sha256'][:12]}]\n{body}"
        )
        actual = audit_runner.find_cached_runner_output(RUNNER)

        self.assertEqual(actual, expected)
        self.assertNotIn("runner cache excerpt clipped", actual)

    def test_real_restricted_packet_has_complete_load_bearing_evidence(self) -> None:
        packet_rows = {
            claim_id: self.rows[claim_id]
            for claim_id in [TARGET, *self.target_row["deps"]]
        }
        authority_path = self.authority_row["note_path"]
        authority_body = (REPO_ROOT / authority_path).read_text(encoding="utf-8")
        manifest: dict[str, dict] = {}

        prompt = audit_runner.render_prompt(
            self.target_row,
            packet_rows,
            (
                "{{FOREACH cited_authority IN CITED_AUTHORITIES}}"
                "{{ENDFOREACH}}\n{{RUNNER_STDOUT}}"
            ),
            runner_timeout_sec=1,
            use_cache=True,
            evidence_manifest_out=manifest,
        )

        self.assertEqual(manifest[authority_path]["text"], authority_body)
        self.assertIn(authority_body, prompt)

        stdout_path = audit_runner.no_go_discipline_gate.runner_stdout_evidence_path(
            TARGET
        )
        cached_stdout = audit_runner.find_cached_runner_output(RUNNER)
        self.assertEqual(manifest[stdout_path]["text"], cached_stdout)
        self.assertIn(cached_stdout, prompt)

        clipped_load_bearing = []
        for path, entry in manifest.items():
            roles = set(entry.get("roles") or [])
            if not roles.intersection(audit_runner.LOAD_BEARING_EVIDENCE_ROLES):
                continue
            text = str(entry.get("text") or "")
            if any(
                marker in text for marker in audit_runner.CLIPPED_EVIDENCE_MARKERS
            ):
                clipped_load_bearing.append(path)
        self.assertEqual(clipped_load_bearing, [])


if __name__ == "__main__":
    unittest.main()
