from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import audit_science_fingerprint as science
import check_changed_audit_evidence
import codex_audit_runner
import compute_audit_queue
import invalidate_stale_audits
import restore_overaggressively_invalidated_audits as restore


def _sha(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


class ScienceFingerprintFixture(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.data = self.root / "docs" / "audit" / "data"
        self.data.mkdir(parents=True)
        self._write("docs/AXIOM.md", "# Stable axiom\n")
        self._write("docs/DEP.md", "# Stable dependency\n")
        self._write("docs/TARGET.md", "# Target theorem\n")
        self._write("docs/CHAIN.md", "# Downstream theorem\n")
        self._write("docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md", "prompt-v1\n")
        self._write(
            "docs/audit/scripts/no_go_discipline_gate.py",
            "# packet-policy-v1\n",
        )
        for relative in (
            "docs/audit/scripts/apply_audit.py",
            "docs/audit/scripts/audit_contract.py",
            "docs/audit/scripts/orchestrate_audit_loop.py",
            "scripts/codex_audit_runner.py",
        ):
            self._write(relative, "# packet-policy-v1\n")
        self._write(
            "docs/ai_methodology/skills/audit-loop/SKILL.md",
            "# audit-loop-v1\n",
        )
        policy_data_paths = {
            "docs/audit/data/doc_authority_registry.json",
            "docs/audit/data/tier_a_admissions.json",
            "docs/audit/data/owner_governed_premise_nodes.json",
            "docs/audit/data/source_path_aliases.json",
        }
        for relative in (
            path
            for path in science.DEPENDENCY_POLICY_SOURCES
            if path not in policy_data_paths
        ):
            self._write(
                relative,
                "{}\n" if relative.endswith(".json") else "# policy-v1\n",
            )
        self._write_json("docs/audit/data/source_path_aliases.json", {})
        self._write_json(
            "docs/audit/data/axiom_premise_nodes.json",
            {
                "schema_version": 1,
                "canonical_ids": ["axiom"],
                "nodes": {
                    "axiom": {
                        "current_path": "docs/AXIOM.md",
                        "aliased_paths": ["docs/AXIOM.md"],
                        "note": "fixture axiom",
                    }
                },
            },
        )
        self._write_json(
            "docs/audit/data/doc_authority_registry.json",
            {"schema_version": 1, "rows": []},
        )
        self._write_json(
            "docs/audit/data/dependency_policy_epoch.json",
            {
                "schema": "dependency_policy_epoch_manifest_v1",
                "epoch": "fixture_dependency_policy_v1",
                "sources": {
                    relative: (
                        hashlib.sha256((self.root / relative).read_bytes()).hexdigest()
                        if (self.root / relative).is_file()
                        else None
                    )
                    for relative in science.DEPENDENCY_POLICY_SOURCES
                },
            },
        )
        self._write_json(
            "docs/audit/data/legacy_science_epoch_baseline.json",
            {
                "schema": "legacy_science_epoch_baseline_v1",
                "framework_premise_epoch_digest": (
                    science.framework_premise_epoch(self.root)
                ),
                "dependency_policy_epoch_digest": (
                    science.dependency_policy_epoch(self.root)
                ),
            },
        )
        self.rows = {
            "axiom": self._row(
                "axiom", "docs/AXIOM.md", claim_type="meta",
                effective_status="meta",
            ),
            "dep": self._row(
                "dep", "docs/DEP.md", claim_type="positive_theorem",
                effective_status="retained",
            ),
            "target": self._row(
                "target", "docs/TARGET.md", deps=["axiom"],
                claim_type="positive_theorem", effective_status="retained",
            ),
            "chain": self._row(
                "chain", "docs/CHAIN.md", deps=["target"],
                claim_type="positive_theorem", effective_status="retained",
            ),
        }

    def _write(self, relative: str, body: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")

    def _write_json(self, relative: str, value: object) -> None:
        self._write(relative, json.dumps(value, indent=2, sort_keys=True) + "\n")

    def _row(
        self,
        claim_id: str,
        note_path: str,
        *,
        deps: list[str] | None = None,
        claim_type: str,
        effective_status: str,
    ) -> dict:
        body = (self.root / note_path).read_text(encoding="utf-8")
        return {
            "claim_id": claim_id,
            "note_path": note_path,
            "note_hash": _sha(body),
            "deps": list(deps or []),
            "claim_type": claim_type,
            "claim_scope": f"scope for {claim_id}",
            "effective_status": effective_status,
            "audit_status": "audited_numerical_match",
            "criticality": "leaf",
            "runner_path": None,
            "helper_runner_paths": [],
        }

    def test_axiom_edit_invalidates_direct_and_transitive_science(self) -> None:
        direct_before = science.build_science_fingerprint(
            self.rows["target"], self.rows, self.root
        )
        transitive_before = science.build_science_fingerprint(
            self.rows["chain"], self.rows, self.root
        )

        self._write("docs/AXIOM.md", "# Materially revised axiom\n")

        direct_after = science.build_science_fingerprint(
            self.rows["target"], self.rows, self.root
        )
        transitive_after = science.build_science_fingerprint(
            self.rows["chain"], self.rows, self.root
        )
        self.assertEqual(
            science.science_fingerprint_change(direct_before, direct_after),
            "science_changed:framework_premise_epoch",
        )
        self.assertEqual(
            science.science_fingerprint_change(transitive_before, transitive_after),
            "science_changed:framework_premise_epoch",
        )

    def test_same_status_dependency_content_change_invalidates(self) -> None:
        target = dict(self.rows["target"])
        target["deps"] = ["dep"]
        before = science.build_science_fingerprint(target, self.rows, self.root)
        self._write("docs/DEP.md", "# Changed dependency, same retained tier\n")
        after = science.build_science_fingerprint(target, self.rows, self.root)
        self.assertEqual(
            science.science_fingerprint_change(before, after),
            "science_changed:dependency:dep:note_sha256",
        )

    def test_dependency_criteria_change_invalidates_without_status_change(self) -> None:
        before = science.build_science_fingerprint(
            self.rows["chain"], self.rows, self.root
        )
        self._write(
            "docs/audit/scripts/premise_nodes.py",
            "# policy-v2: changed accepted-dependency criteria\n",
        )
        manifest_path = "docs/audit/data/dependency_policy_epoch.json"
        manifest = json.loads((self.root / manifest_path).read_text())
        manifest["epoch"] = "fixture_dependency_policy_v2"
        manifest["sources"]["docs/audit/scripts/premise_nodes.py"] = (
            hashlib.sha256(
                (self.root / "docs/audit/scripts/premise_nodes.py").read_bytes()
            ).hexdigest()
        )
        self._write_json(manifest_path, manifest)
        after = science.build_science_fingerprint(
            self.rows["chain"], self.rows, self.root
        )
        self.assertEqual(
            science.science_fingerprint_change(before, after),
            "science_changed:dependency_policy_epoch",
        )

    def test_unreviewed_dependency_policy_change_fails_closed(self) -> None:
        self._write(
            "docs/audit/scripts/premise_nodes.py",
            "# changed without refreshing the governed epoch manifest\n",
        )
        with self.assertRaisesRegex(
            science.ScienceFingerprintError,
            "dependency-policy epoch manifest",
        ):
            science.build_science_fingerprint(
                self.rows["target"], self.rows, self.root
            )

    def test_readiness_policy_is_inside_dependency_epoch(self) -> None:
        before = science.build_science_fingerprint(
            self.rows["chain"], self.rows, self.root
        )
        policy_path = "docs/audit/scripts/forensic_evidence_readiness.py"
        self._write(policy_path, "# reviewed readiness policy v2\n")
        manifest_path = "docs/audit/data/dependency_policy_epoch.json"
        manifest = json.loads((self.root / manifest_path).read_text())
        manifest["epoch"] = "fixture_dependency_policy_v2"
        manifest["sources"][policy_path] = hashlib.sha256(
            (self.root / policy_path).read_bytes()
        ).hexdigest()
        self._write_json(manifest_path, manifest)
        after = science.build_science_fingerprint(
            self.rows["chain"], self.rows, self.root
        )
        self.assertEqual(
            science.science_fingerprint_change(before, after),
            "science_changed:dependency_policy_epoch",
        )

    def test_premise_removal_is_visible_to_legacy_snapshots(self) -> None:
        snapshot = {
            "deps": ["axiom"],
            "dep_axiom_premise_note_hash": {
                "axiom": self.rows["axiom"]["note_hash"]
            },
        }
        self._write_json(
            "docs/audit/data/axiom_premise_nodes.json",
            {"schema_version": 1, "canonical_ids": [], "nodes": {}},
        )
        self.assertEqual(
            science.legacy_premise_snapshot_change(
                snapshot, self.rows["target"], self.rows, self.root
            ),
            "axiom_premise_classification_changed:axiom",
        )

    def test_premise_addition_is_visible_to_legacy_snapshots(self) -> None:
        target = dict(self.rows["target"])
        target["deps"] = ["dep"]
        snapshot = {
            "deps": ["dep"],
            "dep_axiom_premise_note_hash": {},
        }
        self._write_json(
            "docs/audit/data/axiom_premise_nodes.json",
            {
                "schema_version": 1,
                "canonical_ids": ["dep"],
                "nodes": {
                    "dep": {
                        "current_path": "docs/DEP.md",
                        "aliased_paths": ["docs/DEP.md"],
                        "note": "newly classified fixture premise",
                    }
                },
            },
        )
        self.assertEqual(
            science.legacy_premise_snapshot_change(
                snapshot, target, self.rows, self.root
            ),
            "axiom_premise_classification_changed:dep",
        )

    def test_future_axiom_change_invalidates_legacy_snapshots(self) -> None:
        target = dict(self.rows["target"])
        target["deps"] = ["dep"]
        target["audit_state_snapshot"] = {
            "deps": ["dep"],
            "dep_effective_status": {"dep": "retained"},
            "dep_claim_type": {"dep": "positive_theorem"},
            "dep_claim_scope": {"dep": "scope for dep"},
            "dep_axiom_premise_note_hash": {},
            "criticality": "leaf",
            "runner_hash": None,
            "helper_runner_hashes": {},
        }
        rows = {**self.rows, "target": target}
        self._write("docs/AXIOM.md", "# Reviewed axiom revision\n")

        with mock.patch.object(invalidate_stale_audits, "REPO_ROOT", self.root):
            self.assertEqual(
                invalidate_stale_audits.detect_invalidation(target, rows),
                "legacy_framework_premise_epoch_changed",
            )

    def test_future_axiom_change_invalidates_snapshotless_active_judgment(self) -> None:
        target = {
            **self.rows["target"],
            "audit_status": "audit_in_progress",
            "audit_state_snapshot": None,
            "cross_confirmation": {
                "status": "awaiting_second",
                "first_audit": {"verdict": "audited_clean"},
            },
        }
        rows = {**self.rows, "target": target}
        self._write("docs/AXIOM.md", "# Reviewed axiom revision\n")
        with mock.patch.object(invalidate_stale_audits, "REPO_ROOT", self.root):
            self.assertEqual(
                invalidate_stale_audits.detect_invalidation(target, rows),
                "legacy_framework_premise_epoch_changed",
            )

    def test_in_progress_sweep_skips_only_empty_placeholders(self) -> None:
        empty = {
            "audit_status": "audit_in_progress",
            "audit_state_snapshot": None,
            "cross_confirmation": None,
            "auditor": None,
        }
        self.assertFalse(
            invalidate_stale_audits.audit_in_progress_has_live_judgment(empty)
        )
        self.assertTrue(
            invalidate_stale_audits.audit_in_progress_has_live_judgment(
                {**empty, "auditor": "recorded-first-seat"}
            )
        )
        self.assertTrue(
            invalidate_stale_audits.audit_in_progress_has_live_judgment(
                {
                    **empty,
                    "cross_confirmation": {
                        "status": "awaiting_second",
                        "first_audit": {"verdict": "audited_clean"},
                    },
                }
            )
        )

    def test_future_policy_change_invalidates_legacy_snapshots(self) -> None:
        target = dict(self.rows["target"])
        target["audit_state_snapshot"] = {
            "deps": ["axiom"],
            "dep_effective_status": {"axiom": "meta"},
            "dep_claim_type": {"axiom": "meta"},
            "dep_claim_scope": {"axiom": "scope for axiom"},
            "dep_axiom_premise_note_hash": {
                "axiom": self.rows["axiom"]["note_hash"]
            },
            "criticality": "leaf",
            "runner_hash": None,
            "helper_runner_hashes": {},
        }
        rows = {**self.rows, "target": target}
        policy_path = "docs/audit/scripts/premise_nodes.py"
        self._write(policy_path, "# reviewed dependency policy v2\n")
        manifest_path = "docs/audit/data/dependency_policy_epoch.json"
        manifest = json.loads((self.root / manifest_path).read_text())
        manifest["epoch"] = "fixture_dependency_policy_v2"
        manifest["sources"][policy_path] = hashlib.sha256(
            (self.root / policy_path).read_bytes()
        ).hexdigest()
        self._write_json(manifest_path, manifest)

        with mock.patch.object(invalidate_stale_audits, "REPO_ROOT", self.root):
            self.assertEqual(
                invalidate_stale_audits.detect_invalidation(target, rows),
                "legacy_dependency_policy_epoch_changed",
            )

        archived = {
            **target,
            "audit_state_snapshot": target["audit_state_snapshot"],
            "invalidation_reason": "criticality_increased:leaf->medium",
        }
        reset = {
            **target,
            "audit_status": "unaudited",
            "previous_audits": [archived],
        }
        with mock.patch.object(restore, "REPO_ROOT", self.root):
            self.assertIsNone(
                restore.restore_audit_from_previous(
                    reset,
                    {**rows, "target": reset},
                )
            )

    def test_declared_runner_input_change_invalidates(self) -> None:
        self._write("data/input.json", '{"value": 1}\n')
        self._write(
            "scripts/check_target.py",
            "AUDIT_INPUT_PATHS = ('data/input.json',)\nprint('PASS')\n",
        )
        target = dict(self.rows["target"])
        target["runner_path"] = "scripts/check_target.py"
        before = science.build_science_fingerprint(target, self.rows, self.root)
        self._write("data/input.json", '{"value": 2}\n')
        after = science.build_science_fingerprint(target, self.rows, self.root)
        self.assertEqual(
            science.science_fingerprint_change(before, after),
            "science_changed:runner_or_declared_input",
        )

    def test_packet_policy_change_does_not_change_science(self) -> None:
        before_science = science.build_science_fingerprint(
            self.rows["target"], self.rows, self.root
        )
        before_policy = science.packet_policy_fingerprint(self.root)
        self._write("docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md", "prompt-v2\n")
        after_science = science.build_science_fingerprint(
            self.rows["target"], self.rows, self.root
        )
        after_policy = science.packet_policy_fingerprint(self.root)
        self.assertIsNone(
            science.science_fingerprint_change(before_science, after_science)
        )
        self.assertNotEqual(before_policy["digest"], after_policy["digest"])

    def test_packet_upgrade_cannot_change_frozen_judgment(self) -> None:
        row = {
            **self.rows["target"],
            "verdict_rationale": "frozen scientific rationale",
            "audit_invocation_id": "11111111-1111-4111-8111-111111111111",
            "audit_invocation_history": [
                "11111111-1111-4111-8111-111111111111"
            ],
            "no_go_discipline": {"required": True, "status": "FAIL"},
        }
        baseline = science.judgment_fingerprint(row)
        packet_only = {
            **row,
            "no_go_discipline": {"required": True, "status": "PASS"},
        }
        self.assertIsNone(
            science.judgment_fingerprint_change(baseline, packet_only)
        )
        changed_judgment = {
            **packet_only,
            "verdict_rationale": "rewritten rationale",
        }
        self.assertEqual(
            science.judgment_fingerprint_change(baseline, changed_judgment),
            "audit_judgment_changed_without_new_fingerprint",
        )
        changed_seat = {
            **packet_only,
            "audit_invocation_id": "22222222-2222-4222-8222-222222222222",
        }
        self.assertEqual(
            science.judgment_fingerprint_change(baseline, changed_seat),
            "audit_judgment_changed_without_new_fingerprint",
        )
        extended_replay_history = {
            **packet_only,
            "audit_invocation_history": [
                "11111111-1111-4111-8111-111111111111",
                "22222222-2222-4222-8222-222222222222",
            ],
        }
        self.assertIsNone(
            science.judgment_fingerprint_change(
                baseline,
                extended_replay_history,
            )
        )

    def test_live_invalidator_catches_legacy_premise_reclassification(self) -> None:
        target = dict(self.rows["target"])
        target["audit_state_snapshot"] = {
            "deps": ["axiom"],
            "dep_effective_status": {"axiom": "meta"},
            "dep_claim_type": {"axiom": "meta"},
            "dep_claim_scope": {"axiom": "scope for axiom"},
            "dep_axiom_premise_note_hash": {
                "axiom": self.rows["axiom"]["note_hash"]
            },
            "criticality": "leaf",
            "runner_hash": None,
            "helper_runner_hashes": {},
        }
        rows = {**self.rows, "target": target}
        self._write_json(
            "docs/audit/data/axiom_premise_nodes.json",
            {"schema_version": 1, "canonical_ids": [], "nodes": {}},
        )
        baseline_path = "docs/audit/data/legacy_science_epoch_baseline.json"
        baseline = json.loads((self.root / baseline_path).read_text())
        baseline["framework_premise_epoch_digest"] = (
            science.framework_premise_epoch(self.root)
        )
        self._write_json(baseline_path, baseline)
        with mock.patch.object(invalidate_stale_audits, "REPO_ROOT", self.root):
            self.assertEqual(
                invalidate_stale_audits.detect_invalidation(target, rows),
                "axiom_premise_classification_changed:axiom",
            )

    def test_restore_refuses_any_v2_science_drift(self) -> None:
        baseline = science.build_science_fingerprint(
            self.rows["target"], self.rows, self.root
        )
        archived = {
            "audit_status": "audited_numerical_match",
            "audit_state_snapshot": {"science_fingerprint": baseline},
            "invalidation_reason": "criticality_increased:leaf->medium",
        }
        reset = {
            **self.rows["target"],
            "audit_status": "unaudited",
            "previous_audits": [archived],
        }
        rows = {**self.rows, "target": reset}
        self._write("docs/AXIOM.md", "# Changed before restore\n")
        with mock.patch.object(restore, "REPO_ROOT", self.root):
            self.assertIsNone(restore.restore_audit_from_previous(reset, rows))

    def test_restore_rejects_tampered_frozen_judgment(self) -> None:
        audited = {
            **self.rows["target"],
            "audit_status": "audited_numerical_match",
            "audit_date": "2026-08-01",
            "auditor": "independent-seat",
            "verdict_rationale": "original frozen rationale",
        }
        science_baseline = science.build_science_fingerprint(
            audited, self.rows, self.root
        )
        snapshot = {
            "science_fingerprint": science_baseline,
            "judgment_fingerprint": science.judgment_fingerprint(audited),
        }
        archived = {
            **audited,
            "verdict_rationale": "tampered archived rationale",
            "audit_state_snapshot": snapshot,
            "invalidation_reason": "no_go_discipline_packet_missing",
        }
        reset = {
            **self.rows["target"],
            "audit_status": "unaudited",
            "previous_audits": [archived],
        }
        rows = {**self.rows, "target": reset}
        with mock.patch.object(restore, "REPO_ROOT", self.root):
            self.assertIsNone(restore.restore_audit_from_previous(reset, rows))

    def test_restore_preserves_frozen_seat_when_replay_history_grows(self) -> None:
        invocation_id = "11111111-1111-4111-8111-111111111111"
        audited = {
            **self.rows["target"],
            "audit_status": "audited_numerical_match",
            "audit_date": "2026-08-01",
            "auditor": "independent-seat",
            "audit_invocation_id": invocation_id,
            "audit_invocation_history": [invocation_id],
            "verdict_rationale": "original frozen rationale",
        }
        snapshot = {
            "science_fingerprint": science.build_science_fingerprint(
                audited, self.rows, self.root
            ),
            "judgment_fingerprint": science.judgment_fingerprint(audited),
        }
        archived = {
            **audited,
            "audit_state_snapshot": snapshot,
            "invalidation_reason": "criticality_increased:leaf->medium",
        }
        reset = {
            **self.rows["target"],
            "audit_status": "unaudited",
            "audit_invocation_id": None,
            "audit_invocation_history": [
                "22222222-2222-4222-8222-222222222222"
            ],
            "previous_audits": [archived],
        }
        rows = {**self.rows, "target": reset}
        with mock.patch.object(restore, "REPO_ROOT", self.root):
            restored = restore.restore_audit_from_previous(reset, rows)
        self.assertIsNotNone(restored)
        assert restored is not None
        self.assertIsNone(
            science.judgment_fingerprint_change(
                snapshot["judgment_fingerprint"],
                restored,
            )
        )
        self.assertEqual(
            restored["audit_invocation_history"],
            [
                invocation_id,
                "22222222-2222-4222-8222-222222222222",
            ],
        )

    def test_queue_routes_only_exact_science_to_packet_upgrade(self) -> None:
        baseline = science.build_science_fingerprint(
            self.rows["target"], self.rows, self.root
        )
        archived = {
            "audit_status": "audited_clean",
            "claim_type": self.rows["target"]["claim_type"],
            "claim_scope": self.rows["target"]["claim_scope"],
            "invalidation_reason": "no_go_discipline_packet_missing",
        }
        archived["audit_state_snapshot"] = {
            "science_fingerprint": baseline,
            "judgment_fingerprint": science.judgment_fingerprint(
                {**self.rows["target"], **archived}
            ),
        }
        target = {
            **self.rows["target"],
            "audit_status": "unaudited",
            "previous_audits": [archived],
        }
        rows = {**self.rows, "target": target}
        with mock.patch.object(compute_audit_queue, "REPO_ROOT", self.root):
            self.assertEqual(
                compute_audit_queue.audit_work_kind(target, rows),
                ("legacy_packet_upgrade", None),
            )
            target_without_proof = {
                **target,
                "previous_audits": [
                    {**archived, "audit_state_snapshot": {}}
                ],
            }
            self.assertEqual(
                compute_audit_queue.audit_work_kind(
                    target_without_proof,
                    {**rows, "target": target_without_proof},
                )[0],
                "fresh_scientific_audit",
            )

            newer_live_judgment = {
                **target,
                "audit_status": "audited_conditional",
                "verdict_rationale": "newer live scientific judgment",
            }
            self.assertEqual(
                compute_audit_queue.audit_work_kind(
                    newer_live_judgment,
                    {**rows, "target": newer_live_judgment},
                )[0],
                "fresh_scientific_audit",
            )

            newer_archive = {
                **archived,
                "invalidation_reason": "science_changed:target_source",
            }
            reset_with_newer_archive = {
                **target,
                "previous_audits": [archived, newer_archive],
            }
            self.assertEqual(
                compute_audit_queue.audit_work_kind(
                    reset_with_newer_archive,
                    {**rows, "target": reset_with_newer_archive},
                )[0],
                "fresh_scientific_audit",
            )

            self._write("docs/AXIOM.md", "# Changed axiom after audit\n")
            self.assertEqual(
                compute_audit_queue.audit_work_kind(target, rows)[0],
                "fresh_scientific_audit",
            )

    def test_scientific_selector_excludes_preflight_and_packet_work(self) -> None:
        queue_path = self.root / "queue.json"
        queue_path.write_text(
            json.dumps({
                "queue": [
                    {
                        "claim_id": "fresh",
                        "ready": True,
                        "audit_work_kind": "fresh_scientific_audit",
                    },
                    {
                        "claim_id": "evidence",
                        "ready": False,
                        "audit_work_kind": "evidence_repair_required",
                    },
                    {
                        "claim_id": "upgrade",
                        "ready": True,
                        "audit_work_kind": "legacy_packet_upgrade",
                    },
                    {
                        "claim_id": "reconstruct",
                        "ready": True,
                        "audit_work_kind": "provenance_reconstruction_required",
                    },
                    {
                        "claim_id": "blocked-fresh",
                        "ready": False,
                        "audit_work_kind": "fresh_scientific_audit",
                    },
                ]
            }),
            encoding="utf-8",
        )
        with mock.patch.object(codex_audit_runner, "QUEUE_PATH", queue_path):
            self.assertEqual(
                [row["claim_id"] for row in codex_audit_runner.load_queue()],
                ["fresh"],
            )
            self.assertEqual(
                [
                    row["claim_id"]
                    for row in codex_audit_runner.load_queue(ready_only=False)
                ],
                ["fresh", "blocked-fresh"],
            )

    def test_deployed_legacy_epoch_baseline_change_fails_review_gate(self) -> None:
        paths = {check_changed_audit_evidence.LEGACY_EPOCH_BASELINE_PATH}
        with (
            mock.patch.object(
                check_changed_audit_evidence,
                "merge_base_commit",
                return_value="base-sha",
            ),
            mock.patch.object(
                check_changed_audit_evidence,
                "_git",
                return_value=(
                    check_changed_audit_evidence.LEGACY_EPOCH_BASELINE_PATH
                    + "\n"
                ),
            ),
        ):
            failures = check_changed_audit_evidence.immutable_control_failures(
                "origin/main",
                paths,
            )
        self.assertEqual(
            failures[0]["control"],
            "immutable_legacy_science_epoch_baseline",
        )

    def test_initial_legacy_epoch_baseline_introduction_is_allowed(self) -> None:
        paths = {check_changed_audit_evidence.LEGACY_EPOCH_BASELINE_PATH}
        with (
            mock.patch.object(
                check_changed_audit_evidence,
                "merge_base_commit",
                return_value="base-sha",
            ),
            mock.patch.object(
                check_changed_audit_evidence,
                "_git",
                return_value="",
            ),
        ):
            self.assertEqual(
                check_changed_audit_evidence.immutable_control_failures(
                    "origin/main",
                    paths,
                ),
                [],
            )


if __name__ == "__main__":
    unittest.main()
