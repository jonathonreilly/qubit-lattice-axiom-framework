"""Mutation tests for the review-loop quality/safety contract."""

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import check_review_loop_skill_contract as contract  # noqa: E402


class ReviewLoopSkillContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        root = contract.REPO_ROOT
        cls.skill = (root / contract.SKILL_REL).read_text(encoding="utf-8")
        cls.generator = (root / contract.GENERATOR_REL).read_text(encoding="utf-8")
        cls.pipeline = (root / contract.PIPELINE_REL).read_text(encoding="utf-8")

    def missing(self, *, skill=None, generator=None, pipeline=None) -> list[str]:
        return contract.validate_texts(
            self.skill if skill is None else skill,
            self.generator if generator is None else generator,
            self.pipeline if pipeline is None else pipeline,
        )

    def assert_skill_mutation_fails(self, needle: str, family: str) -> None:
        mutated = self.skill.replace(needle, "REMOVED_BY_MUTATION")
        self.assertNotEqual(mutated, self.skill, f"mutation needle absent: {needle}")
        self.assertIn(family, self.missing(skill=mutated))

    def test_committed_contract_passes(self):
        self.assertEqual(self.missing(), [])

    def test_freshness_is_fail_closed(self):
        self.assert_skill_mutation_fails("## Skill Freshness", "freshness")

    def test_authority_reads_are_fail_closed(self):
        self.assert_skill_mutation_fails(
            "**Mandatory authority read:**", "mandatory_authority_reads"
        )

    def test_model_and_effort_are_fail_closed(self):
        self.assert_skill_mutation_fails("GPT-5.6-Sol", "reviewer_model_and_effort")

    def test_reviewer_lenses_are_fail_closed(self):
        self.assert_skill_mutation_fails("ProofObligationReviewer", "reviewer_lenses")

    def test_independent_math_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "independent route", "independent_math_and_mutations"
        )

    def test_proof_import_governance_is_fail_closed(self):
        self.assert_skill_mutation_fails("EQUIVALENT-GAP", "proof_import_governance")

    def test_no_go_is_fail_closed(self):
        self.assert_skill_mutation_fails("N1-N8", "no_go_discipline")

    def test_audit_boundary_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "## Audit-System Compatibility Gate", "audit_compatibility_boundary"
        )

    def test_same_session_confirmation_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "same reviewer thread/session", "same_session_confirmation"
        )

    def test_pipeline_evidence_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "check_changed_audit_evidence.py", "pipeline_strict_and_evidence"
        )

    def test_manifest_landing_is_fail_closed(self):
        self.assert_skill_mutation_fails("before EVERY push attempt", "manifest_landing")

    def test_disk_worktree_guards_are_fail_closed(self):
        self.assert_skill_mutation_fails("5242880", "disk_and_worktree_guards")

    def test_landing_containment_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "merge-base --is-ancestor", "fail_closed_landing"
        )

    def test_generated_router_is_fail_closed(self):
        mutated = self.generator.replace("missing_authority_router_coverage", "removed")
        self.assertIn("generated_authority_router", self.missing(generator=mutated))

    def test_pipeline_registration_is_fail_closed(self):
        mutated = self.pipeline.replace("check_review_loop_skill_contract.py", "removed")
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))


if __name__ == "__main__":
    unittest.main()
