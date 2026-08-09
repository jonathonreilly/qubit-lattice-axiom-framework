"""Delivery-revalidation regression for relationship-context packets.

A note that declares machine-readable `contradicts:`/`cross_reference:`
relations (historic-intake wrappers do) must survive the delivery
revalidation transaction: the fingerprint the packet builder computes over
the exact evidence manifest must equal the fingerprint recomputed from the
rebuilt manifest, and any change to a referenced wrapper or archived
original must (a) change the packet fingerprint and (b) be diagnosable
through the dedicated relationship-context fingerprint, so the failure is
reported as relationship_context_superseded — never remote_state_superseded.
Relationship-free packets keep their previous behavior exactly.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import codex_audit_runner  # noqa: E402

RELATIONSHIP_NOTE = (
    "docs/historic_intake/"
    "HISTORIC_PR_BODY_BLOCK01_INTAKE_NOTE_2026-08-05.md"
)
RELATIONSHIP_FREE_NOTE = (
    "docs/historic_intake/"
    "HISTORIC_BORN_RULE_DERIVED_NOTE_INTAKE_NOTE_2026-08-05.md"
)


def _exact_manifest(note_path: str,
                    claim_id: str = "historic_intake.test_row") -> dict:
    manifest: dict = {}
    codex_audit_runner.render_prompt(
        {"claim_id": claim_id, "note_path": note_path},
        {},
        "{{NOTE_BODY}}",
        0,
        skip_runner_stdout=True,
        evidence_manifest_out=manifest,
        audit_invocation_id="test-invocation",
    )
    return manifest


class RelationshipContextDeliveryTest(unittest.TestCase):
    def test_exact_and_rebuilt_fingerprints_agree(self) -> None:
        row = {"claim_id": "historic_intake.test_row",
               "note_path": RELATIONSHIP_NOTE}
        exact = _exact_manifest(RELATIONSHIP_NOTE)
        exact_rel_entries = [
            path for path, entry in exact.items()
            if "relationship_context" in (entry.get("roles") or [])
        ]
        self.assertEqual(len(exact_rel_entries), 10)

        rebuilt = codex_audit_runner._packet_manifest_for_fingerprint(row, {})
        rebuilt_rel_entries = [
            path for path, entry in rebuilt.items()
            if "relationship_context" in (entry.get("roles") or [])
        ]
        self.assertEqual(sorted(exact_rel_entries), sorted(rebuilt_rel_entries))

        fp_exact = codex_audit_runner.audit_packet_source_fingerprint(
            row, {}, exact)
        fp_rebuilt = codex_audit_runner.audit_packet_source_fingerprint(
            row, {}, rebuilt)
        self.assertEqual(fp_exact, fp_rebuilt)

        rel_exact = codex_audit_runner.relationship_context_fingerprint(exact)
        rel_rebuilt = codex_audit_runner.relationship_context_fingerprint(
            rebuilt)
        self.assertEqual(rel_exact, rel_rebuilt)

    def test_referenced_original_change_is_relationship_diagnosable(self) -> None:
        row = {"claim_id": "historic_intake.test_row",
               "note_path": RELATIONSHIP_NOTE}
        exact = _exact_manifest(RELATIONSHIP_NOTE)
        fp_exact = codex_audit_runner.audit_packet_source_fingerprint(
            row, {}, exact)
        rel_exact = codex_audit_runner.relationship_context_fingerprint(exact)

        tampered_path = (
            "archive_unlanded/historic_intake_originals/packsci01/"
            "10254_CLAIM_STATUS_CERTIFICATE.md"
        )
        real_identity = codex_audit_runner._path_content_identity

        def tampered_identity(path):
            identity = real_identity(path)
            if str(path).endswith(tampered_path):
                identity = dict(identity)
                identity["bytes_sha256"] = "0" * 64
            return identity

        with mock.patch.object(
            codex_audit_runner, "_path_content_identity",
            side_effect=tampered_identity,
        ):
            rebuilt = codex_audit_runner._packet_manifest_for_fingerprint(
                row, {})
            fp_tampered = codex_audit_runner.audit_packet_source_fingerprint(
                row, {}, rebuilt)
            rel_tampered = codex_audit_runner.relationship_context_fingerprint(
                rebuilt)
        # the packet fingerprint moves AND the relationship-context
        # fingerprint moves, so the precondition reports the drift as
        # relationship_context_superseded before the generic packet check.
        self.assertNotEqual(fp_exact, fp_tampered)
        self.assertNotEqual(rel_exact, rel_tampered)

    def test_relationship_free_packet_behavior_unchanged(self) -> None:
        row = {"claim_id": "historic_intake.test_free_row",
               "note_path": RELATIONSHIP_FREE_NOTE}
        exact = _exact_manifest(RELATIONSHIP_FREE_NOTE,
                                claim_id="historic_intake.test_free_row")
        self.assertFalse(any(
            "relationship_context" in (entry.get("roles") or [])
            for entry in exact.values()
        ))
        rebuilt = codex_audit_runner._packet_manifest_for_fingerprint(row, {})
        self.assertFalse(any(
            "relationship_context" in (entry.get("roles") or [])
            for entry in rebuilt.values()
        ))
        fp_exact = codex_audit_runner.audit_packet_source_fingerprint(
            row, {}, exact)
        fp_rebuilt = codex_audit_runner.audit_packet_source_fingerprint(
            row, {}, rebuilt)
        self.assertEqual(fp_exact, fp_rebuilt)
        self.assertEqual(
            codex_audit_runner.relationship_context_fingerprint(exact),
            codex_audit_runner.relationship_context_fingerprint(rebuilt),
        )

    def test_unresolvable_reference_fails_closed_with_own_reason(self) -> None:
        row = {"claim_id": "historic_intake.test_row",
               "note_path": RELATIONSHIP_NOTE}
        broken_body = (
            "# Broken\n\nClaim type: bounded_theorem\n\n```yaml\n"
            "contradicts:\n- \"MISSING_WRAPPER.md\"\n```\n"
        )
        with mock.patch.object(
            codex_audit_runner, "read_note_body", return_value=broken_body,
        ):
            with self.assertRaises(
                codex_audit_runner.RelationshipContextError
            ):
                codex_audit_runner._packet_manifest_for_fingerprint(row, {})


if __name__ == "__main__":
    unittest.main()
