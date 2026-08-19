"""Mutation tests for the review-loop quality/safety contract."""

import re
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

    def test_commented_freshness_is_fail_closed(self):
        start = self.skill.index("## Skill Freshness")
        end = self.skill.index("## Model And Tool Boundary")
        mutated = (
            self.skill[:start]
            + "<!--\n"
            + self.skill[start:end]
            + "-->\n"
            + self.skill[end:]
        )
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_unterminated_html_comment_is_fail_closed(self):
        start = self.skill.index("## Reviewer Fanout")
        mutated = self.skill[:start] + "<!--\n" + self.skill[start:]
        missing = self.missing(skill=mutated)
        self.assertIn("markdown_structure", missing)
        self.assertIn("reviewer_lenses", missing)

    def test_commonmark_commented_freshness_is_fail_closed(self):
        start = self.skill.index("## Skill Freshness")
        end = self.skill.index("## Model And Tool Boundary")
        mutated = (
            self.skill[:start]
            + "[//]: # (## Skill Freshness SKILL_FRESHNESS_CHECK.md origin/main)\n\n"
            + self.skill[end:]
        )
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_multiline_reference_definition_cannot_supply_freshness(self):
        start = self.skill.index("Before applying this skill")
        end = self.skill.index("## Model And Tool Boundary", start)
        positive = self.skill[start:end].rstrip()
        mutated = (
            self.skill[:start]
            + '[hidden-freshness]: <#> "title starts\n'
            + positive
            + '\n"\n\n'
            + self.skill[end:]
        )
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_next_line_reference_layouts_cannot_supply_freshness(self):
        start = self.skill.index("Before applying this skill")
        end = self.skill.index("## Model And Tool Boundary", start)
        positive = self.skill[start:end].rstrip()
        for prefix in (
            '[hidden]: <#>\n  "title starts\n',
            '[hidden]:\n  <#> "title starts\n',
        ):
            mutated = (
                self.skill[:start]
                + prefix
                + positive
                + '\n"\n\n'
                + self.skill[end:]
            )
            with self.subTest(prefix=prefix):
                self.assertIn("freshness", self.missing(skill=mutated))

    def test_negated_freshness_is_fail_closed(self):
        mutated = self.skill.replace(
            "Before applying this skill, perform",
            "Before applying this skill, do not perform",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_authority_reads_are_fail_closed(self):
        self.assert_skill_mutation_fails(
            "**Mandatory authority read:**", "mandatory_authority_reads"
        )

    def test_negated_authority_reads_are_fail_closed(self):
        mutated = self.skill.replace(
            "judgment, read the current axiom memo",
            "judgment, do not read the current axiom memo",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("mandatory_authority_reads", self.missing(skill=mutated))

    def test_model_and_effort_are_fail_closed(self):
        self.assert_skill_mutation_fails("GPT-5.6-Sol", "reviewer_model_and_effort")

    def test_negated_model_and_effort_are_fail_closed(self):
        mutated = self.skill.replace(
            "Run it with the user's configured",
            "Do not run it with the user's configured",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_each_reviewer_lens_is_fail_closed(self):
        for reviewer in (
            "CodeRunnerReviewer",
            "PhysicsClaimReviewer",
            "ProofObligationReviewer",
            "ImportSupportReviewer",
            "NatureRetentionReviewer",
            "NoGoDisciplineReviewer",
            "LabelingConventionReviewer",
            "RepoGovernanceReviewer",
            "MethodologySkillReviewer",
        ):
            with self.subTest(reviewer=reviewer):
                self.assert_skill_mutation_fails(reviewer, "reviewer_lenses")

    def test_negated_reviewer_sections_are_fail_closed(self):
        reviewers = (
            "CodeRunnerReviewer",
            "PhysicsClaimReviewer",
            "ProofObligationReviewer",
            "ImportSupportReviewer",
            "NatureRetentionReviewer",
            "NoGoDisciplineReviewer",
            "LabelingConventionReviewer",
            "RepoGovernanceReviewer",
        )
        for index, reviewer in enumerate(reviewers):
            start_marker = f"\n- `{reviewer}`"
            start = self.skill.index(start_marker)
            if index + 1 < len(reviewers):
                end = self.skill.index(f"\n- `{reviewers[index + 1]}`", start + 1)
            else:
                end = self.skill.index("\n### Optional Reviewer", start + 1)
            mutated = (
                self.skill[:start]
                + f"\n- Do not run `{reviewer}`.\n"
                + self.skill[end:]
            )
            with self.subTest(reviewer=reviewer):
                self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        methodology_start = self.skill.index(
            "Run `MethodologySkillReviewer` when files under"
        )
        methodology_end = self.skill.index("\n\n## Reviewer Prompt", methodology_start)
        mutated = (
            self.skill[:methodology_start]
            + "Do not run `MethodologySkillReviewer` when methodology files change."
            + self.skill[methodology_end:]
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_fenced_reviewer_sections_are_fail_closed(self):
        start = self.skill.index("### Required Reviewers")
        end = self.skill.index("## Reviewer Prompt", start)
        mutated = (
            self.skill[:start]
            + "```text\n"
            + self.skill[start:end]
            + "```\n\n"
            + self.skill[end:]
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_unterminated_fenced_reviewer_sections_are_fail_closed(self):
        start = self.skill.index("### Required Reviewers")
        mutated = self.skill[:start] + "```text\n" + self.skill[start:]
        missing = self.missing(skill=mutated)
        self.assertIn("markdown_structure", missing)
        self.assertIn("reviewer_lenses", missing)

    def test_indented_code_cannot_supply_reviewer_sections(self):
        start = self.skill.index("### Required Reviewers")
        end = self.skill.index("## Reviewer Prompt", start)
        indented = "\n".join(
            "    " + line for line in self.skill[start:end].splitlines()
        )
        mutated = self.skill[:start] + indented + "\n" + self.skill[end:]
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_optional_reviewer_heading_is_fail_closed(self):
        mutated = self.skill.replace(
            "### Optional Reviewer", "### Historical Example", 1
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_hidden_affirmative_reviewer_bodies_are_fail_closed(self):
        needles = dict(contract.REVIEWER_BODY_RULES)
        for index, (reviewer, pattern) in enumerate(needles.items()):
            match = re.search(
                pattern,
                self.skill,
                re.IGNORECASE | re.DOTALL | re.MULTILINE,
            )
            self.assertIsNotNone(match, reviewer)
            assert match is not None
            positive = match.group(0)
            replacement = (
                "  Do not run this reviewer.\n\n"
                f'[hidden-reviewer-{index}]: <#> "title starts\n'
                + positive
                + '\n"'
            )
            mutated = self.skill[: match.start()] + replacement + self.skill[match.end() :]
            with self.subTest(reviewer=reviewer):
                self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        match = re.search(
            contract.METHODOLOGY_BODY_RULE,
            self.skill,
            re.IGNORECASE | re.DOTALL | re.MULTILINE,
        )
        self.assertIsNotNone(match)
        assert match is not None
        positive = match.group(0)
        replacement = (
            "Do not run this reviewer.\n\n"
            '[hidden-methodology]: <#> "title starts\n'
            + positive
            + '\n"'
        )
        mutated = self.skill[: match.start()] + replacement + self.skill[match.end() :]
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_named_reviewer_negations_are_fail_closed(self):
        for reviewer in contract.REVIEWER_BODY_RULES:
            label = f"- `{reviewer}`\n"
            mutated = self.skill.replace(
                label,
                label + f"  Do not run `{reviewer}`.\n",
                1,
            )
            with self.subTest(reviewer=reviewer):
                self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        anchor = "Run `MethodologySkillReviewer` when files under"
        mutated = self.skill.replace(
            anchor,
            "Do not run `MethodologySkillReviewer`.\n\n" + anchor,
            1,
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_active_reviewer_contradictions_are_fail_closed(self):
        variants = (
            lambda reviewer: f"  However, do not run `{reviewer}`.\n",
            lambda reviewer: f"  `{reviewer}` must not run.\n",
            lambda reviewer: f"  - Skip `{reviewer}`.\n",
            lambda reviewer: f"  `{reviewer}` is not required.\n",
        )
        for reviewer, pattern in contract.REVIEWER_BODY_RULES.items():
            match = re.search(
                pattern,
                self.skill,
                re.IGNORECASE | re.DOTALL | re.MULTILINE,
            )
            self.assertIsNotNone(match, reviewer)
            assert match is not None
            for variant in variants:
                mutated = (
                    self.skill[: match.end()]
                    + "\n"
                    + variant(reviewer)
                    + self.skill[match.end() :]
                )
                with self.subTest(reviewer=reviewer, variant=variant(reviewer)):
                    self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        match = re.search(
            contract.METHODOLOGY_BODY_RULE,
            self.skill,
            re.IGNORECASE | re.DOTALL | re.MULTILINE,
        )
        self.assertIsNotNone(match)
        assert match is not None
        mutated = (
            self.skill[: match.end()]
            + "\nHowever, do not run `MethodologySkillReviewer`."
            + self.skill[match.end() :]
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

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
            'if ! git merge-base --is-ancestor "$landed" origin/main; then',
            "fail_closed_landing",
        )

    def test_inert_landing_containment_tokens_are_fail_closed(self):
        mutated = self.skill.replace(
            'if ! git merge-base --is-ancestor "$landed" origin/main; then',
            'if false; then # git merge-base --is-ancestor "$landed" origin/main',
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_outer_conditional_containment_is_fail_closed(self):
        block = (
            '   if ! git merge-base --is-ancestor "$landed" origin/main; then\n'
            '     echo "FAILED: $landed not contained in origin/main" >&2\n'
            "     exit 1\n"
            "   fi"
        )
        mutated = self.skill.replace(
            block,
            "   if false; then\n" + block + "\n   fi",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_whole_containment_context_outer_conditional_is_fail_closed(self):
        start = self.skill.index(contract.CONTAINMENT_CONTEXT)
        end = self.skill.index('   echo "LANDED $landed"', start)
        mutated = (
            self.skill[:start]
            + "   if false; then\n"
            + self.skill[start:end]
            + "   fi\n"
            + self.skill[end:]
        )
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_containment_context_in_heredoc_is_fail_closed(self):
        mutated = self.skill.replace(
            contract.CONTAINMENT_CONTEXT,
            "   cat <<'HIDDEN_CONTAINMENT'\n"
            + contract.CONTAINMENT_CONTEXT
            + "\nHIDDEN_CONTAINMENT",
            1,
        )
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_containment_context_in_second_heredoc_is_fail_closed(self):
        for opener in (
            "   cat <<'FIRST' <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' \\\n     <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' |\n     cat <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' &&\n     cat <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' ||\n     cat <<'HIDDEN-CONTAINMENT'\n",
        ):
            mutated = self.skill.replace(
                contract.CONTAINMENT_CONTEXT,
                opener
                + "FIRST\n"
                + contract.CONTAINMENT_CONTEXT
                + "\nHIDDEN-CONTAINMENT",
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_containment_context_in_general_substitutions_is_fail_closed(self):
        for opener, closer in (
            ("   hidden=$( :\n", "\n   ) || true"),
            ("   hidden=$\\\n( :\n", "\n) || true"),
            ("   hidden=<( :\n", "\n   )"),
            ("   hidden=` :\n", "\n   ` || true"),
            ("   ( :\n", "\n   ) || true"),
        ):
            mutated = self.skill.replace(
                contract.CONTAINMENT_CONTEXT,
                opener + contract.CONTAINMENT_CONTEXT + closer,
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_unterminated_landing_shell_context_is_fail_closed(self):
        marker = '   echo "LANDED $landed"'
        mutated = self.skill.replace(marker, marker + "\n   hidden=$( :", 1)
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_generated_router_is_fail_closed(self):
        mutated = self.generator.replace("missing_authority_router_coverage", "removed")
        self.assertIn("generated_authority_router", self.missing(generator=mutated))

    def test_pipeline_registration_is_fail_closed(self):
        mutated = self.pipeline.replace("check_review_loop_skill_contract.py", "removed")
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_commented_pipeline_registration_is_fail_closed(self):
        mutated = self.pipeline.replace(
            "python3 docs/audit/scripts/check_review_loop_skill_contract.py",
            "# python3 docs/audit/scripts/check_review_loop_skill_contract.py",
            1,
        )
        self.assertNotEqual(mutated, self.pipeline)
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_conditional_pipeline_registration_is_fail_closed(self):
        command = "python3 docs/audit/scripts/check_review_loop_skill_contract.py"
        mutated = self.pipeline.replace(
            command,
            "if false; then\n" + command + "\nfi",
            1,
        )
        self.assertNotEqual(mutated, self.pipeline)
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_whole_pipeline_context_outer_conditional_is_fail_closed(self):
        start = self.pipeline.index(contract.PIPELINE_CONTRACT_CONTEXT)
        end = self.pipeline.index("\necho\n", start)
        mutated = (
            self.pipeline[:start]
            + "if false; then\n"
            + self.pipeline[start:end]
            + "\nfi\n"
            + self.pipeline[end:]
        )
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_pipeline_context_in_heredoc_is_fail_closed(self):
        mutated = self.pipeline.replace(
            contract.PIPELINE_CONTRACT_CONTEXT,
            "cat <<'HIDDEN_CONTRACT'\n"
            + contract.PIPELINE_CONTRACT_CONTEXT
            + "\nHIDDEN_CONTRACT",
            1,
        )
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_pipeline_context_in_general_heredocs_is_fail_closed(self):
        for delimiter in ("HIDDEN-CONTEXT", "1"):
            mutated = self.pipeline.replace(
                contract.PIPELINE_CONTRACT_CONTEXT,
                f"cat <<'{delimiter}'\n"
                + contract.PIPELINE_CONTRACT_CONTEXT
                + f"\n{delimiter}",
                1,
            )
            with self.subTest(delimiter=delimiter):
                self.assertIn(
                    "pipeline_contract_registration", self.missing(pipeline=mutated)
                )

    def test_pipeline_context_in_second_heredoc_is_fail_closed(self):
        for opener in (
            "cat <<'FIRST' <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' \\\n  <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' |\n  cat <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' &&\n  cat <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' ||\n  cat <<'HIDDEN-CONTRACT'\n",
        ):
            mutated = self.pipeline.replace(
                contract.PIPELINE_CONTRACT_CONTEXT,
                opener
                + "FIRST\n"
                + contract.PIPELINE_CONTRACT_CONTEXT
                + "\nHIDDEN-CONTRACT",
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn(
                    "pipeline_contract_registration", self.missing(pipeline=mutated)
                )

    def test_pipeline_context_in_command_substitutions_is_fail_closed(self):
        for opener, closer in (
            ("hidden=`\n", "`\n"),
            ("hidden=$(\n", ")\n"),
            ("hidden=$( :\n", ") || true\n"),
            ("hidden=$\\\n( :\n", ") || true\n"),
            ("hidden=>( :\n", ")\n"),
            ("( :\n", ") || true\n"),
        ):
            mutated = self.pipeline.replace(
                contract.PIPELINE_CONTRACT_CONTEXT,
                opener + contract.PIPELINE_CONTRACT_CONTEXT + "\n" + closer,
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn(
                    "pipeline_contract_registration", self.missing(pipeline=mutated)
                )

    def test_unterminated_pipeline_shell_context_is_fail_closed(self):
        mutated = self.pipeline + "\nhidden=$( :\n"
        self.assertIn(
            "pipeline_contract_registration", self.missing(pipeline=mutated)
        )


if __name__ == "__main__":
    unittest.main()
