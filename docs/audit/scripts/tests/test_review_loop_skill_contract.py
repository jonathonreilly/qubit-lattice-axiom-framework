"""Mutation tests for the review-loop quality/safety contract."""

import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import check_review_loop_skill_contract as contract  # noqa: E402


class ReviewLoopReferenceRoutingTest(unittest.TestCase):
    """Routed instructions must remain reachable and covered by the guard."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.entry = self.root / contract.SKILL_REL
        source = contract.REPO_ROOT / contract.SKILL_REL
        self.entry.parent.mkdir(parents=True)
        shutil.copyfile(source, self.entry)
        for relative in (*contract.REFERENCE_TRIGGER_RULES,
                         contract.LANDING_SCRIPT_PACKAGE_PATH):
            destination = self.entry.parent / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source.parent / relative, destination)
        self.script = self.entry.parent / contract.LANDING_SCRIPT_PACKAGE_PATH

    def load(self):
        return contract.load_skill_contract(self.root)

    def edit(self, path, old, new):
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8")

    def test_live_routes_load_complete_contract(self):
        skill, missing = self.load()
        self.assertEqual(missing, [])
        for relative in contract.SKILL_CONTRACT_REFERENCES:
            self.assertIn((self.entry.parent / relative).read_text(), skill)
        self.assertEqual(set(contract.SKILL_RULE_LOCATIONS), set(contract.SKILL_RULES))
        self.assertEqual(set(contract.UNIT_RULE_LOCATIONS), set(contract.UNIT_PROSE_RULES))

    def test_missing_procedure_holds_operation(self):
        (self.entry.parent / "references/SCIENCE_LENSES.md").unlink()
        self.assertIn("reference_unreadable_science_lenses", self.load()[1])

    def test_hidden_or_sample_route_does_not_count(self):
        text = self.entry.read_text()
        row = next(line for line in text.splitlines()
                   if line.startswith("| Every scientific, code, governance"))
        for replacement in ("<!--\n" + row + "\n-->",
                            "```markdown\n" + row + "\n```",
                            "    " + row):
            with self.subTest(replacement=replacement):
                self.entry.write_text(text.replace(row, replacement))
                self.assertIn("reference_route_science_lenses", self.load()[1])

    def test_optional_or_wrong_mode_route_does_not_count(self):
        self.edit(self.entry,
                  "| Every scientific, code, governance, or methodology review and affected-fix confirmation |",
                  "| Optional background after landing |")
        self.assertIn("reference_route_science_lenses", self.load()[1])

    def test_optional_suffix_cannot_disable_a_mandatory_route(self):
        self.edit(self.entry,
                  "methodology review and affected-fix confirmation |",
                  "methodology review and affected-fix confirmation; may skip this optional reference |")
        self.assertIn("reference_route_science_lenses", self.load()[1])

    def test_science_rules_cannot_be_hidden_in_landing_only_file(self):
        lenses = self.entry.parent / "references/SCIENCE_LENSES.md"
        landing = self.entry.parent / "references/LANDING.md"
        landing.write_text(landing.read_text() + "\n" + lenses.read_text())
        lenses.write_text("No review lenses apply before authorized landing.\n")
        self.assertIn("routed_reviewer_lenses", self.load()[1])

    def test_validation_recipe_cannot_be_moved_out_of_shared_procedure(self):
        combined = self.entry.parent / "references/COMBINED_VALIDATION.md"
        landing = self.entry.parent / "references/LANDING.md"
        text = combined.read_text()
        start = text.index("   On the frozen integrated candidate,")
        landing.write_text(landing.read_text() + "\n" + text[start:])
        combined.write_text(text[:start])
        self.assertIn("routed_landing_train_combined_gate", self.load()[1])

    def test_missing_reference_cannot_be_ignored(self):
        self.edit(self.entry,
                  "required reference holds the dependent operation",
                  "required reference may be skipped during the dependent operation")
        self.assertIn("reference_routing_unread_holds_action", self.load()[1])

    def test_cross_file_delimiters_cannot_repair_missing_instructions(self):
        one = self.entry.parent / "references/REVIEW_UNITS.md"
        two = self.entry.parent / "references/LANDING.md"
        one.write_text(one.read_text() + "\n<!--\n")
        two.write_text("-->\n" + two.read_text())
        self.assertIn("reference_markdown_structure_review_units", self.load()[1])

    def test_outside_package_substitution_fails(self):
        reference = self.entry.parent / "references/SCIENCE_LENSES.md"
        outside = self.root / "other-revision.md"
        shutil.copyfile(reference, outside)
        reference.unlink()
        reference.symlink_to(outside)
        self.assertIn("reference_outside_package_science_lenses", self.load()[1])

    def test_relocated_rule_still_reaches_existing_semantic_guard(self):
        self.edit(self.entry.parent / "references/REVIEW_UNITS.md",
                  "never infer a scientific verdict or restamp an old execution",
                  "reuse a receipt to infer a scientific verdict")
        skill, missing = self.load()
        self.assertIn("routed_versioned_mechanical_receipt", missing)
        root = contract.REPO_ROOT
        failures = contract.validate_texts(
            skill,
            (root / contract.LANDING_SCRIPT_REL).read_text(),
            (root / contract.GENERATOR_REL).read_text(),
            (root / contract.PIPELINE_REL).read_text(),
        )
        self.assertIn("versioned_mechanical_receipt", failures)

    def test_landing_script_is_read_from_the_package_only(self):
        script, missing = contract.load_landing_script(self.root)
        self.assertEqual(missing, [])
        self.assertEqual(script, (contract.REPO_ROOT / contract.LANDING_SCRIPT_REL).read_text())
        outside = self.root / "other-land-train.sh"
        shutil.copyfile(self.script, outside)
        self.script.unlink()
        self.assertEqual(contract.load_landing_script(self.root),
                         ("", ["landing_script_unreadable"]))
        self.script.symlink_to(outside)
        self.assertEqual(contract.load_landing_script(self.root),
                         ("", ["landing_script_outside_package"]))

    def test_landing_reference_must_run_the_package_script(self):
        landing = self.entry.parent / "references/LANDING.md"
        original = landing.read_text()
        command = "   " + contract.LANDING_RUN_COMMAND + "\n"
        self.assertEqual(original.count(command), 1)
        for mutated in (
            # Another file, a second command, or no command at all.
            original.replace(command, '   bash "$TMPDIR/land_train.sh" "$TRAIN_FILE"\n'),
            original.replace(command, command + "   git push origin HEAD:main\n"),
            original.replace(command, "   # " + command.strip() + "\n"),
            original.replace(command, ""),
            # The command hidden from a reader, or run a second time elsewhere.
            original.replace("   ```bash\n" + command, "   ```text\n" + command),
            original + "\n```bash\n" + contract.LANDING_RUN_COMMAND + "\n```\n",
        ):
            self.assertNotEqual(mutated, original)
            landing.write_text(mutated)
            with self.subTest(mutated=mutated[-200:]):
                self.assertIn("routed_landing_script_entry", self.load()[1])
        landing.write_text(original)
        self.assertEqual(self.load()[1], [])

    def test_review_only_cannot_mutate_callers_source_or_index(self):
        self.edit(self.entry.parent / "references/COMBINED_VALIDATION.md",
                  "the caller's source and index",
                  "only the caller's source")
        self.assertIn("review_only_validation_isolation", self.load()[1])

    def test_dirty_proof_cannot_be_validated_as_head_only(self):
        self.edit(self.entry.parent / "references/COMBINED_VALIDATION.md",
                  "staged, unstaged and untracked reviewed content and all declared inputs",
                  "only the committed source")
        self.assertIn("review_only_validation_isolation", self.load()[1])


class ReviewLoopSkillContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        root = contract.REPO_ROOT
        cls.skill, routing_failures = contract.load_skill_contract(root)
        assert not routing_failures, routing_failures
        cls.script, script_failures = contract.load_landing_script(root)
        assert not script_failures, script_failures
        cls.command = (root / contract.COMMAND_REL).read_text(encoding="utf-8")
        cls.generator = (root / contract.GENERATOR_REL).read_text(encoding="utf-8")
        cls.pipeline = (root / contract.PIPELINE_REL).read_text(encoding="utf-8")
        cls.placement_references = {
            name: (root / path).read_text(encoding="utf-8")
            for name, path in contract.PLACEMENT_REFERENCES.items()
        }

    def missing(
        self, *, skill=None, command=None, generator=None, pipeline=None,
        placement_references=None, script=None,
    ) -> list[str]:
        return contract.validate_texts(
            self.skill if skill is None else skill,
            self.script if script is None else script,
            self.generator if generator is None else generator,
            self.pipeline if pipeline is None else pipeline,
            self.command if command is None else command,
            self.placement_references if placement_references is None
            else placement_references,
        )

    def assert_skill_mutation_fails(self, needle: str, family: str) -> None:
        mutated = self.skill.replace(needle, "REMOVED_BY_MUTATION")
        self.assertTrue(mutated != self.skill, f"mutation needle absent: {needle}")
        self.assertIn(family, self.missing(skill=mutated))

    def assert_script_mutation_fails(self, needle: str, family: str) -> None:
        mutated = self.script.replace(needle, "REMOVED_BY_MUTATION")
        self.assertNotEqual(mutated, self.script, f"mutation needle absent: {needle}")
        self.assertIn(family, self.missing(script=mutated))

    def mutate_script(self, needle: str, replacement: str) -> str:
        mutated = self.script.replace(needle, replacement, 1)
        self.assertNotEqual(mutated, self.script, f"mutation needle absent: {needle}")
        return mutated

    def assert_command_mutation_fails(self, needle: str, family: str) -> None:
        mutated = self.command.replace(needle, "REMOVED_BY_MUTATION")
        self.assertNotEqual(mutated, self.command, f"mutation needle absent: {needle}")
        self.assertIn(family, self.missing(command=mutated))

    def mutate_skill_fence(self, marker: str, needle: str, replacement: str) -> str:
        start = self.skill.index(marker)
        end = self.skill.index("\n   ```", start)
        block = self.skill[start:end]
        mutated_block = block.replace(needle, replacement, 1)
        self.assertNotEqual(mutated_block, block, f"mutation needle absent: {needle}")
        return self.skill[:start] + mutated_block + self.skill[end:]

    def test_committed_contract_passes(self):
        self.assertEqual(self.missing(), [])

    def test_receipt_cannot_claim_science_authority(self):
        self.assert_skill_mutation_fails(
            'never infer a scientific verdict or restamp an old execution',
            'versioned_mechanical_receipt')

    def test_history_reuse_requires_anchored_manifest(self):
        self.assert_skill_mutation_fails(
            'mapping and externally pinned manifest checks',
            'exact_history_and_exclusive_reuse')

    def test_pool_release_cannot_discard_residue(self):
        self.assert_skill_mutation_fails(
            'rejects tracked/untracked/ignored residue and unfinished Git operations',
            'exact_history_and_exclusive_reuse')

    def test_dependent_base_preservation_is_required(self):
        for needle in (
            "So protect dependents before the landing push",
            "including drafts",
            "re-list open PRs targeting the old base immediately before the",
            "preserve the parent branch for recovery",
            "After the push, verify the expected dependent PRs remain open",
            "restore the exact deleted parent ref with an absent-ref lease",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "dependent_pr_base_preservation")

    def test_command_preserves_dependent_prs(self):
        self.assert_command_mutation_fails(
            "retarget dependent bases to `main`", "command_dependent_base_preservation"
        )

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
        start = self.skill.index("Before using this workflow")
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
        start = self.skill.index("Before using this workflow")
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
            "Before using this workflow, inspect",
            "Before using this workflow, do not inspect",
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

    def test_combined_validation_requires_full_pipeline(self):
        mutated = self.skill.replace("run_pipeline.sh \\", "run_pipeline.sh --verdict-only \\", 1)
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("landing_train_combined_gate", self.missing(skill=mutated))

    def test_model_and_effort_are_fail_closed(self):
        self.assert_skill_mutation_fails("**fast reviewer**", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("from a different model family", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("configured reviewer** in that setting", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("its actual configuration stated", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("restricted-input reviewer context", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("separation from authorship and independent checks", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("Never label same-family", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("independent confirmation gate", "reviewer_model_and_effort")

    def test_negated_model_and_effort_are_fail_closed(self):
        mutated = self.skill.replace(
            "use the **fast reviewer**",
            "do not use the **fast reviewer**",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_negated_configuration_clause_is_fail_closed(self):
        mutated = self.skill.replace(
            "If a requested", "Do not If a requested", 1
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_negated_owner_choice_clause_is_fail_closed(self):
        mutated = self.skill.replace(
            "Respect a later explicit owner", "Do not Respect a later explicit owner", 1
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_soft_wrapped_negations_cannot_supply_affirmative_clauses(self):
        for clause in [
            "If a requested",
            "Respect a later explicit owner",
            "If no different-family reviewer",
        ]:
            for prefix in ["Do not\n ", "Never\n  ", "Do not\n"]:
                with self.subTest(clause=clause, prefix=prefix):
                    mutated = self.skill.replace(clause, prefix + clause, 1)
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

    def test_train_scheduler_is_fail_closed(self):
        for needle in (
            "trains of at most eight",
            "depart with the useful ready batch as soon as the coordinator is available",
            "do not wait for an arbitrary collection deadline or an unfinished reviewer",
            "open the next empty",
            "one-component trains",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "landing_train_scheduler")

    def test_coherent_unit_obligations_cannot_be_hidden_or_removed(self):
        start = self.skill.index("## Coherent review units and validation placement")
        end = self.skill.index("## Default Entry", start)
        section = self.skill[start:end]
        expected = {
            "coherent_unit_coverage",
            "unit_provenance_and_recheck",
            "shared_validation_placement",
        }
        for wrapper in ("<!--\n{}\n-->\n", "```text\n{}\n```\n"):
            mutated = self.skill[:start] + wrapper.format(section) + self.skill[end:]
            with self.subTest(wrapper=wrapper):
                self.assertTrue(expected <= set(self.missing(skill=mutated)))

    def test_unit_coverage_and_provenance_fail_closed(self):
        cases = (
            ("Run every applicable reviewer lens on the complete final unit",
             "Do not run every applicable reviewer lens on the complete final unit",
             "coherent_unit_coverage"),
            ("Unmapped content\nblocks unit confirmation.",
             "Unmapped content is acceptable.", "coherent_unit_coverage"),
            ("A changed PR head fails the provenance",
             "A changed PR head passes the provenance", "unit_provenance_and_recheck"),
            ("or semantic interaction reopens the affected conclusion",
             "or semantic interaction preserves the affected conclusion",
             "unit_provenance_and_recheck"),
            ("mark-ready is not PASS, and a still-draft PR cannot land.",
             "mark-ready is PASS, and a still-draft PR can land.", "unit_scope_and_close"),
            ("never delete the recovery ref of such a PR.",
             "delete the recovery ref of such a PR.", "unit_scope_and_close"),
            ("After the loop, verify each constituent's accepted/narrowed/superseding",
             "After the loop, skip each constituent's accepted/narrowed/superseding",
             "unit_scope_and_close"),
            ("is not a changed head in\nthis sense.",
             "is not a changed head in\nany sense.", "unit_provenance_and_recheck"),
            ("under an exact lease on that frozen SHA",
             "with a plain force-push", "unit_provenance_and_recheck"),
            ("only after\nthe frozen head is recorded under a recovery ref",
             "whether or not\nthe frozen head is recorded", "unit_provenance_and_recheck"),
            ("before or after that push, still fails the gate.",
             "before or after that push, is accepted.", "unit_provenance_and_recheck"),
        )
        for needle, replacement, family in cases:
            mutated = self.skill.replace(needle, replacement, 1)
            self.assertNotEqual(mutated, self.skill, needle)
            with self.subTest(needle=needle):
                self.assertIn(family, self.missing(skill=mutated))

    def test_landed_pr_is_merged_and_never_closed_by_hand(self):
        for needle in (
            "Review-loop never\ncloses a landed PR",
            "Close a PR only when nothing from it reaches `main`",
            "merges nothing through GitHub and closes no landed PR.",
            "A `NOT_MERGED` line means the mechanism failed",
            "do not close it by hand, and report it to the owner",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "landed_pr_shows_merged")

    def test_shared_validation_identity_cannot_be_weakened(self):
        for needle in (
            "identical frozen base and candidate",
            "command/options, tool/runtime versions, declared inputs, and evidence",
            "accessible successful logs and their hashes",
            "already validated unit whose raw tree equals the whole integrated candidate",
            "changed base/tree/input, or changed validation scope invalidates reuse",
            "verify all non-generated bytes stayed identical",
            "again on each constituent or unit before enrollment",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "shared_validation_placement")

    def test_validation_placement_is_required_in_coupled_references(self):
        for name in contract.PLACEMENT_REFERENCES:
            for wrapper in ("REMOVED", "<!--\n{}\n-->", "```text\n{}\n```"):
                references = dict(self.placement_references)
                references[name] = wrapper.format(references[name])
                with self.subTest(name=name, wrapper=wrapper):
                    self.assertIn(f"shared_validation_reference_{name}",
                                  self.missing(placement_references=references))

    def test_command_unit_validation_is_fail_closed(self):
        for needle in (
            "complete constituent",
            "perform one full",
            "do not require duplicate per-PR or per-unit full runs",
            "collection wait",
            "Mark-ready is not PASS",
        ):
            with self.subTest(needle=needle):
                self.assert_command_mutation_fails(needle, "command_unit_validation")

    def _run_gate_fragment(self, marker: str, fail_at: int) -> tuple[int, list[str], str]:
        """Execute the actual documented shell with inert command substitutes.

        The substitutions only log calls and fail at a chosen call. No pipeline,
        audit, Git mutation, or external action runs in these behavioral tests.
        """
        scan = contract._markdown_scan(self.skill)
        blocks = [body for _, body in scan.fenced_blocks if marker in body]
        self.assertEqual(len(blocks), 1)
        with tempfile.TemporaryDirectory() as tmp:
            script = textwrap.dedent("""\
                gate_call() {
                  printf '%s\\n' "$*" >> calls
                  gate_count=$(wc -l < calls)
                  [ "$gate_count" -ne "$FAIL_AT" ] || return 7
                  if [ "$1" = git ] && [ "$2" = merge-base ]; then
                    printf '%s\\n' frozen-base
                  fi
                }
                bash() { gate_call bash "$@"; }
                python3() { gate_call python3 "$@"; }
                git() { gate_call git "$@"; }
                """)
            script += f"FAIL_AT={fail_at}\n" + blocks[0] + "\necho GATE_COMPLETED\n"
            proc = subprocess.run(["bash", "-c", script], cwd=tmp, text=True,
                                  capture_output=True, check=False)
            calls = (Path(tmp) / "calls").read_text().splitlines()
            return proc.returncode, calls, proc.stdout

    def test_combined_validation_runs_each_gate_once_and_short_circuits_failure(self):
        marker = "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate"
        status, calls, stdout = self._run_gate_fragment(marker, 0)
        self.assertEqual(status, 0)
        self.assertEqual(len(calls), 3)
        self.assertIn("GATE_COMPLETED", stdout)
        for fail_at in (1, 2, 3):
            with self.subTest(fail_at=fail_at):
                status, calls, stdout = self._run_gate_fragment(marker, fail_at)
                self.assertNotEqual(status, 0)
                self.assertEqual(len(calls), fail_at)
                self.assertNotIn("GATE_COMPLETED", stdout)

    def test_combined_diff_checks_fail_closed_at_every_command(self):
        marker = "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate"
        status, calls, stdout = self._run_gate_fragment(marker, 0)
        self.assertEqual(status, 0)
        self.assertEqual(len(calls), 4)
        self.assertIn("GATE_COMPLETED", stdout)
        for fail_at in (1, 2, 3, 4):
            with self.subTest(fail_at=fail_at):
                status, calls, stdout = self._run_gate_fragment(marker, fail_at)
                self.assertNotEqual(status, 0)
                self.assertEqual(len(calls), fail_at)
                self.assertNotIn("GATE_COMPLETED", stdout)

    def test_train_combined_gate_is_fail_closed(self):
        for needle in (
            "combined gate is mechanical",
            (
                "python3 docs/audit/scripts/check_changed_audit_evidence.py "
                "--base origin/main"
            ),
            'git diff --check "$review_base"..HEAD',
            "git diff --cached --check",
            "VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>",
            "VALIDATED_TREE=<combined-candidate-tree-sha>",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(
                    needle, "landing_train_combined_gate"
                )
        for needle in (
            'VALIDATED_BASE="${entries[0]}"',
            'VALIDATED_TREE="${entries[0]}"',
            'if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then',
            'if [ "$(git rev-parse \'HEAD^{tree}\')" != "$VALIDATED_TREE" ]; then',
        ):
            with self.subTest(needle=needle):
                self.assert_script_mutation_fails(
                    needle, "landing_train_combined_gate"
                )

    def test_train_combined_commands_are_bound_to_their_active_blocks(self):
        cases = (
            (
                "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate",
                "bash docs/audit/scripts/run_pipeline.sh",
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate",
                "python3 docs/audit/scripts/audit_lint.py --strict",
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate",
                "python3 docs/audit/scripts/check_changed_audit_evidence.py "
                "--base origin/main",
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate",
                'git diff --check "$review_base"..HEAD',
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate",
                "git diff --check \\\n",
                "true # removed\n",
            ),
            (
                "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate",
                "git diff --cached --check",
                "true # removed",
            ),
        )
        for marker, command, replacement in cases:
            mutated = self.mutate_skill_fence(marker, command, replacement)
            with self.subTest(command=command):
                self.assertIn(
                    "landing_train_combined_gate", self.missing(skill=mutated)
                )

    def test_train_validated_guards_must_stay_active_at_push_depth(self):
        for line in (
            '     if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then',
            '     if [ "$(git rev-parse \'HEAD^{tree}\')" != "$VALIDATED_TREE" ]; then',
        ):
            mutated = self.mutate_script(
                line, "     if false; then\n" + line + "\n     fi"
            )
            with self.subTest(line=line):
                self.assertIn(
                    "landing_train_combined_gate", self.missing(script=mutated)
                )

    def test_train_head_guard_is_fail_closed(self):
        # The documented train file and the prose that describes the loop.
        for needle in (
            "PR_NUMBERS=<pr-a-number> <pr-b-number> ...",
            "PR_HEADS=<pr-a-frozen-head-sha> <pr-b-frozen-head-sha> ...",
            "PR_HEAD_REFS=<pr-a-head-branch> <pr-b-head-branch> ...",
            "PR_TIPS=<pr-a-newest> <pr-b-newest> ...",
            "refs/review-loop/recovery/pr-",
            "post-push head check",
            "force-with-lease=refs/heads/<head>:<frozen-head-sha>",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "landing_train_head_guard")
        # The loop itself.
        for needle in (
            "PR_NUMBERS=(",
            "PR_HEADS=(",
            "PR_HEAD_REFS=(",
            "PR_TIPS=(",
            "verify_frozen_pr_heads()",
            "verify_pr_github_state()",
            "record_recovery_refs()",
            "refs/review-loop/recovery/pr-",
            "move_pr_heads()",
            "restore_frozen_pr_heads()",
            "PR head moved; dissolve the train without pushing",
        ):
            with self.subTest(needle=needle):
                self.assert_script_mutation_fails(needle, "landing_train_head_guard")

    def test_train_head_checks_must_bracket_every_push(self):
        for line in (
            "     if ! verify_frozen_pr_heads; then",
            "     if ! verify_pr_github_state; then",
            "     if ! record_recovery_refs; then",
            "     if ! move_pr_heads; then",
            "     if ! wait_for_landed_pr_heads; then",
            "     if ! restore_frozen_pr_heads; then",
            '     if ! verify_pr_head "$pr" "$expected"; then',
        ):
            mutated = self.mutate_script(
                line, "     if false; then\n" + line + "\n     fi"
            )
            with self.subTest(line=line):
                self.assertIn("landing_train_head_guard", self.missing(script=mutated))

    def test_train_head_fetch_compare_and_failure_are_structurally_bound(self):
        mutations = (
            (
                'if ! git fetch -q origin "+pull/$pr/head:$live_ref"; then',
                "if ! true; then",
            ),
            ('[ "$actual" = "$expected" ]', '[ "$actual" != "$expected" ]'),
            (
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT,
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT.replace(
                    "       exit 1", "       true # nonfatal", 1
                ),
            ),
            (
                'if ! verify_pr_head "$pr" "$expected"; then',
                "if false; then",
            ),
            ('elif pr_shows_merged "$pr"; then', "elif true; then"),
            # The head push must stay leased on the frozen SHA and atomic.
            (
                '"--force-with-lease=refs/heads/${PR_HEAD_REFS[$index]}:${PR_HEADS[$index]}"',
                '"--force"',
            ),
            (
                'git push -q --atomic "${leases[@]}" origin "${specs[@]}"',
                'git push -q "${leases[@]}" origin "${specs[@]}"',
            ),
            # A guard may not be dropped from the chain before the main push.
            (
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT,
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT.replace(
                    "     if ! record_recovery_refs; then", "     if false; then", 1
                ),
            ),
            (
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT,
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT.replace(
                    "       restore_frozen_pr_heads\n", "", 1
                ),
            ),
            # A head that cannot be restored must stop the loop.
            (
                contract.TRAIN_HEAD_RESTORE_CONTEXT,
                contract.TRAIN_HEAD_RESTORE_CONTEXT.replace(
                    "       exit 1", "       true # nonfatal", 1
                ),
            ),
        )
        for needle, replacement in mutations:
            mutated = self.mutate_script(needle, replacement)
            with self.subTest(needle=needle):
                self.assertIn("landing_train_head_guard", self.missing(script=mutated))

    def test_command_train_contract_is_fail_closed(self):
        for needle in (
            "continuously collected trains of at most eight",
            "double-buffered landing train",
            "next empty train",
            "immediately before push",
            "records each frozen head under a recovery ref",
            "--force-with-lease=<ref>:<frozen-head-sha>",
            "rechecks each landed head after the push",
            "the loop closes no landed PR",
        ):
            with self.subTest(needle=needle):
                self.assert_command_mutation_fails(needle, "command_landing_train")

    def test_live_surface_routing_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "relevant sharded rows under `docs/audit/data/ledger/`",
            "live_surface_routing",
        )
        mutated = self.skill + "\nUse docs/publication/ci3_z3 as a live surface.\n"
        self.assertIn("live_surface_routing", self.missing(skill=mutated))

    def test_pipeline_evidence_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "check_changed_audit_evidence.py", "pipeline_strict_and_evidence"
        )

    def test_manifest_landing_is_fail_closed(self):
        self.assert_skill_mutation_fails("before EVERY push attempt", "manifest_landing")
        self.assert_script_mutation_fails(
            "run_citation_graph_build.py", "manifest_landing"
        )

    def test_manifest_sequencer_progress_is_fail_closed(self):
        for needle in (
            'while [ -z "$cherry_pick_complete" ]; do',
            'if [ "$conflicted_commit" = "$last_conflicted_commit" ]; then',
            "FAILED: manifest repair made no sequencer progress",
        ):
            with self.subTest(needle=needle):
                self.assert_script_mutation_fails(
                    needle, "manifest_sequencer_progress"
                )

    def test_disk_worktree_guards_are_fail_closed(self):
        self.assert_skill_mutation_fails("5242880", "disk_and_worktree_guards")

    def test_landing_containment_is_fail_closed(self):
        self.assert_script_mutation_fails(
            'if ! git merge-base --is-ancestor "$landed" origin/main; then',
            "fail_closed_landing",
        )

    def test_inert_landing_containment_tokens_are_fail_closed(self):
        mutated = self.mutate_script(
            'if ! git merge-base --is-ancestor "$landed" origin/main; then',
            'if false; then # git merge-base --is-ancestor "$landed" origin/main',
        )
        self.assertIn("fail_closed_landing", self.missing(script=mutated))

    def test_outer_conditional_containment_is_fail_closed(self):
        block = (
            '   if ! git merge-base --is-ancestor "$landed" origin/main; then\n'
            '     echo "FAILED: $landed not contained in origin/main" >&2\n'
            "     exit 1\n"
            "   fi"
        )
        mutated = self.mutate_script(block, "   if false; then\n" + block + "\n   fi")
        self.assertIn("fail_closed_landing", self.missing(script=mutated))

    def test_whole_containment_context_outer_conditional_is_fail_closed(self):
        start = self.script.index(contract.CONTAINMENT_CONTEXT)
        end = self.script.index('   echo "LANDED $landed"', start)
        mutated = (
            self.script[:start]
            + "   if false; then\n"
            + self.script[start:end]
            + "   fi\n"
            + self.script[end:]
        )
        self.assertIn("fail_closed_landing", self.missing(script=mutated))

    def test_containment_context_in_heredoc_is_fail_closed(self):
        mutated = self.mutate_script(
            contract.CONTAINMENT_CONTEXT,
            "   cat <<'HIDDEN_CONTAINMENT'\n"
            + contract.CONTAINMENT_CONTEXT
            + "\nHIDDEN_CONTAINMENT",
        )
        self.assertIn("fail_closed_landing", self.missing(script=mutated))

    def test_containment_context_in_second_heredoc_is_fail_closed(self):
        for opener in (
            "   cat <<'FIRST' <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' \\\n     <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' |\n     cat <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' &&\n     cat <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' ||\n     cat <<'HIDDEN-CONTAINMENT'\n",
        ):
            mutated = self.mutate_script(
                contract.CONTAINMENT_CONTEXT,
                opener
                + "FIRST\n"
                + contract.CONTAINMENT_CONTEXT
                + "\nHIDDEN-CONTAINMENT",
            )
            with self.subTest(opener=opener):
                self.assertIn("fail_closed_landing", self.missing(script=mutated))

    def test_containment_context_in_general_substitutions_is_fail_closed(self):
        for opener, closer in (
            ("   hidden=$( :\n", "\n   ) || true"),
            ("   hidden=$\\\n( :\n", "\n) || true"),
            ("   hidden=<( :\n", "\n   )"),
            ("   hidden=` :\n", "\n   ` || true"),
            ("   ( :\n", "\n   ) || true"),
        ):
            mutated = self.mutate_script(
                contract.CONTAINMENT_CONTEXT,
                opener + contract.CONTAINMENT_CONTEXT + closer,
            )
            with self.subTest(opener=opener):
                self.assertIn("fail_closed_landing", self.missing(script=mutated))

    def test_unterminated_landing_shell_context_is_fail_closed(self):
        marker = '   echo "LANDED $landed"'
        mutated = self.mutate_script(marker, marker + "\n   hidden=$( :")
        self.assertIn("fail_closed_landing", self.missing(script=mutated))

    def test_landing_script_must_define_read_inputs_and_run_the_loop(self):
        call = contract.LANDING_SCRIPT_CALL
        read = "   " + contract.LANDING_SCRIPT_READS_INPUT + "\n"
        mutations = (
            # The loop is defined and never run, run conditionally, or run
            # with more commands after it.
            ("\n" + call + "\n", "\n"),
            ("\n" + call + "\n", "\nif false; then\n" + call + "\nfi\n"),
            ("\n" + call + "\n", "\n# " + call + "\n"),
            ("\n" + call + "\n", "\n" + 'land_train "$@"' + "\nexit 0\n"),
            ("\n" + call + "\n", "\n" + call + "\ngit push origin HEAD:main\n"),
            # The body is not the function body.
            ("\nland_train() {\n", "\nland_train_unused() {\n"),
            ("\nland_train() {\n", "\nif false; then\nland_train() {\n"),
            # The inputs are not read first, or are read conditionally.
            (read, ""),
            (read, "   if false; then\n" + read + "   fi\n"),
            (read, "   git push origin HEAD:main\n" + read),
            # An entry is accepted without its form check.
            ('if ! is_object_name "$entry"; then', "if false; then"),
            ('if ! git check-ref-format "refs/heads/$entry"; then', "if false; then"),
            ("*[!0123456789]*) train_file_error", "*[!0123456789]*) true"),
            ('if [ "${#entries[@]}" -ne 1 ]; then', "if false; then"),
            # A name the documented train file sets is not assigned.
            ('COMMITS) COMMITS=("${entries[@]}") ;;', "COMMITS) ;;"),
            ('PR_TIPS) PR_TIPS=("${entries[@]}") ;;', "PR_TIPS) ;;"),
            ('VALIDATED_TREE) VALIDATED_TREE="${entries[0]}" ;;', "VALIDATED_TREE) ;;"),
            ("\nread_train_file() {\n", "\nread_train_file_unused() {\n"),
        )
        for needle, replacement in mutations:
            mutated = self.mutate_script(needle, replacement)
            with self.subTest(needle=needle, replacement=replacement):
                self.assertIn("landing_script_entry", self.missing(script=mutated))
        for needle in (
            "The train's fail-closed landing loop is the script",
            "Never paste or edit a copy of",
            "COMMITS=<pr-a-oldest> ... <pr-a-newest> <pr-b-oldest> ...",
            "The script parses the train file and never executes it.",
            contract.LANDING_RUN_COMMAND,
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "landing_script_entry")

    def test_every_loop_guard_fails_with_the_loop_outside_the_function(self):
        # Closing the function early leaves the loop text in place but no
        # longer inside the body that the last line runs.
        read = "   " + contract.LANDING_SCRIPT_READS_INPUT + "\n"
        mutated = self.mutate_script(read, read + "}\nunused_loop() {\n")
        missing = self.missing(script=mutated)
        for family in ("fail_closed_landing", "landing_train_combined_gate",
                       "landing_train_head_guard"):
            with self.subTest(family=family):
                self.assertIn(family, missing)

    def test_commented_out_loop_clauses_do_not_count(self):
        cases = (
            ("   for attempt in 1 2 3 4; do", "fail_closed_landing"),
            ('       echo "FAILED: PR head moved; dissolve the train without pushing" >&2',
             "landing_train_head_guard"),
            ('         echo "FAILED: manifest repair made no sequencer progress" >&2',
             "manifest_sequencer_progress"),
        )
        for line, family in cases:
            mutated = self.mutate_script(line + "\n", "# " + line + "\n")
            with self.subTest(line=line):
                self.assertIn(family, self.missing(script=mutated))

    def test_command_names_the_landing_script(self):
        for needle in ("`scripts/land_train.sh`", "never paste or edit a"):
            with self.subTest(needle=needle):
                self.assert_command_mutation_fails(needle, "command_landing_train")

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


# Test double for the GitHub behaviour the landing loop relies on, as observed
# on 2026-11-10 with PRs 10151 and 10152: an open PR's refs/pull/<n>/head
# follows its head branch; once main holds that head the PR is merged, its
# pull ref stops moving and its head branch is deleted. Nothing here contacts
# GitHub, so these tests check the loop against this model, not GitHub itself.
GITHUB_DOUBLE_HOOK = """#!/bin/sh
[ -e no-follow ] && exit 0
while read -r old new ref; do
  case "$ref" in
    refs/heads/unit-[0-9]*)
      n="${ref#refs/heads/unit-}"
      [ -e "merged-$n" ] && continue
      case "$new" in
        0000000000000000000000000000000000000000) ;;
        *) git update-ref "refs/pull/$n/head" "$new" ;;
      esac
      ;;
  esac
done
for n in 1 2 3; do
  [ -e "merged-$n" ] && continue
  head="$(git rev-parse -q --verify "refs/pull/$n/head")" || continue
  if git merge-base --is-ancestor "$head" refs/heads/main 2>/dev/null; then
    : > "merged-$n"
    git update-ref -d "refs/heads/unit-$n"
  fi
done
"""

GH_DOUBLE = """gh() {
  printf 'gh %s\\n' "$*" >> "$CALL_LOG"
  local head
  [ -z "${GH_BROKEN:-}" ] || return 1
  case "$1 $2" in
    "pr list")
      printf '%s\\n' "${GH_OPEN_DEPENDENTS:-0}"
      ;;
    "pr view")
      head="$(command git --git-dir="$REMOTE" rev-parse "refs/pull/$3/head")" || return 1
      case "$*" in
        *isDraft*)
          printf '%s %s false %s unit-%s %s\\n' "${GH_STATE:-OPEN}" \\
            "${GH_DRAFT:-false}" "${GH_BASE:-main}" "$3" "$head"
          ;;
        *)
          if [ -e "$REMOTE/merged-$3" ]; then echo MERGED; else echo OPEN; fi
          ;;
      esac
      ;;
    *) return 1 ;;
  esac
}
"""


LANDING_SCRIPT = contract.REPO_ROOT / contract.LANDING_SCRIPT_REL


@unittest.skipUnless(shutil.which("git") and shutil.which("bash"), "requires Git and Bash")
class ReviewLoopLandingSequenceTest(unittest.TestCase):
    """Run the landing script against three real local Git branches.

    Each branch adds a separate note and changes the same one-line manifest.
    Thus one invocation must handle two successive manifest conflicts. Remote
    means a temporary local bare repository with a hook that stands in for
    GitHub's pull-request bookkeeping; these tests never use the network.

    The script file itself runs, on a train file, as LANDING.md says. Bash
    reads the file named by BASH_ENV before a script, so the `gh`, `git`,
    `sleep` and `python3` doubles are shell functions defined there.
    """

    STATE_FAULTS = {
        "pr-is-draft": "GH_DRAFT=true\n",
        "pr-base-not-main": "GH_BASE=integration\n",
        "pr-not-open": "GH_STATE=CLOSED\n",
        "open-dependent": "GH_OPEN_DEPENDENTS=1\n",
        "gh-unavailable": "GH_BROKEN=1\n",
    }

    def run_sequence(self, fault=None, mutate_loop=False, two_commit_unit=False,
                     tips=None, train_edit=None):
        env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                   GIT_AUTHOR_NAME="Fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
                   GIT_COMMITTER_NAME="Fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid",
                   GIT_AUTHOR_DATE="2026-09-07T01:00:00Z",
                   GIT_COMMITTER_DATE="2026-09-07T01:00:00Z")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            remote, work = root / "remote.git", root / "work"
            remote.mkdir()
            work.mkdir()

            def git(cwd, *args):
                proc = subprocess.run(["git", *args], cwd=cwd, env=env, text=True,
                                      capture_output=True, check=True)
                return proc.stdout.strip()

            def ref(name):
                proc = subprocess.run(["git", "rev-parse", "-q", "--verify", name],
                                      cwd=remote, env=env, text=True, capture_output=True)
                return proc.stdout.strip() or None

            def write(path, content):
                dest = work / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content)

            def commit(message):
                git(work, "add", ".")
                git(work, "-c", "commit.gpgsign=false", "commit", "-qm", message)
                return git(work, "rev-parse", "HEAD")

            manifest = "docs/audit/data/citation_graph_manifest.json"
            git(remote, "init", "--bare", "-q")
            hook = remote / "hooks" / "post-receive"
            hook.parent.mkdir(exist_ok=True)
            hook.write_text(GITHUB_DOUBLE_HOOK)
            hook.chmod(0o755)
            git(work, "init", "-q", "-b", "main")
            git(work, "config", "commit.gpgsign", "false")
            write("source.txt", "base\n")
            write("notes/base.md", "base\n")
            write(manifest, '["base"]\n')
            write("docs/audit/scripts/run_citation_graph_build.py", "pass\n")
            write("docs/audit/scripts/write_citation_graph_manifest.py",
                  "from pathlib import Path\nimport json\n"
                  f"Path({manifest!r}).write_text(json.dumps(sorted("
                  "p.stem for p in Path('notes').glob('*.md'))) + '\\n')\n")
            base = commit("base")
            git(work, "remote", "add", "origin", str(remote))
            git(work, "push", "-q", "origin", "HEAD:main")
            heads, commits, notes = [], [], ["base"]
            for number, letter in enumerate("abc", 1):
                git(work, "checkout", "-q", "--detach", base)
                unit_notes = [letter]
                write(f"notes/{letter}.md", letter + "\n")
                write(manifest, json.dumps(sorted([letter, "base"])) + "\n")
                if fault == "later-source-conflict" and letter in "ac":
                    write("source.txt", letter + "\n")
                head = commit("unit " + letter)
                commits.append(head)
                if two_commit_unit and letter == "a":
                    unit_notes.append("a2")
                    write("notes/a2.md", "a2\n")
                    write(manifest, json.dumps(sorted(["a", "a2", "base"])) + "\n")
                    head = commit("unit a, second commit")
                    commits.append(head)
                heads.append(head)
                notes += unit_notes
                git(work, "push", "-q", "origin", f"{head}:refs/heads/unit-{number}")
            git(work, "checkout", "-q", "--detach", base)
            for note in notes[1:]:
                write(f"notes/{note}.md", note + "\n")
            write(manifest, json.dumps(sorted(notes)) + "\n")
            commit("validated candidate")
            tree = git(work, "rev-parse", "HEAD^{tree}")
            # A commit that another lander could push to main meanwhile.
            git(work, "checkout", "-q", "--detach", base)
            write("notes/racer.md", "racer\n")
            racer = commit("another landing")
            git(work, "push", "-q", "origin", f"{racer}:refs/fixture/racer")
            git(work, "checkout", "-q", "--detach", base)
            if fault == "head-moved":
                git(work, "push", "-q", "--force", "origin", f"{racer}:refs/heads/unit-2")
            if fault == "lease-refused":
                # The branch moved but GitHub has not yet shown it on the PR.
                git(remote, "update-ref", "refs/heads/unit-2", racer)
            if fault == "pull-refs-do-not-follow":
                (remote / "no-follow").write_text("")
            for number, head in enumerate(heads, 1):
                expected = racer if fault == "head-moved" and number == 2 else head
                self.assertEqual(ref(f"refs/pull/{number}/head"), expected)
            # The train file is the block LANDING.md documents, filled in.
            skill, routing_failures = contract.load_skill_contract(contract.REPO_ROOT)
            self.assertEqual(routing_failures, [])
            blocks = contract._markdown_scan(skill).fenced_blocks
            train_text = textwrap.dedent(
                next(body for _, body in blocks if "VALIDATED_BASE=<" in body)) + "\n"
            replacements = {
                "VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>": f"VALIDATED_BASE={base}",
                "VALIDATED_TREE=<combined-candidate-tree-sha>": f"VALIDATED_TREE={tree}",
                "COMMITS=<pr-a-oldest> ... <pr-a-newest> <pr-b-oldest> ...": "COMMITS=" + " ".join(commits),
                "PR_NUMBERS=<pr-a-number> <pr-b-number> ...": "PR_NUMBERS=1 2 3",
                "PR_HEADS=<pr-a-frozen-head-sha> <pr-b-frozen-head-sha> ...": "PR_HEADS=" + " ".join(heads),
                "PR_HEAD_REFS=<pr-a-head-branch> <pr-b-head-branch> ...": "PR_HEAD_REFS=unit-1 unit-2 unit-3",
                "PR_TIPS=<pr-a-newest> <pr-b-newest> ...": "PR_TIPS=" + " ".join(
                    heads if tips is None else [heads[i] for i in tips]),
            }
            for old, new in replacements.items():
                self.assertIn(old, train_text)
                train_text = train_text.replace(old, new)
            self.assertNotIn("<", train_text)
            if train_edit is not None:
                edited = train_edit(train_text)
                self.assertNotEqual(edited, train_text)
                train_text = edited
            train = root / "train.txt"
            train.write_text(train_text)
            script = LANDING_SCRIPT
            if mutate_loop or fault == "script-replaced-mid-run":
                script = root / "land_train.sh"
                code = LANDING_SCRIPT.read_text()
            if mutate_loop:
                # A single conditional repair recreates the reviewed defect:
                # the second conflict reaches the final tree guard unresolved.
                old = 'while [ -z "$cherry_pick_complete" ]; do'
                self.assertIn(old, code)
                start = code.index(old)
                end = code.index("\n     done", start)
                code = (code[:start] + code[start:end].replace(old, 'if [ -z "$cherry_pick_complete" ]; then', 1)
                        + "\n     fi" + code[end + len("\n     done"):])
            if script != LANDING_SCRIPT:
                script.write_text(code)
            prelude = f"CALL_LOG={shlex.quote(str(root / 'git-calls.log'))}\n"
            prelude += f"SCRIPT={shlex.quote(str(script))}\n"
            prelude += f"REMOTE={shlex.quote(str(remote))}\nRACER={racer}\n"
            prelude += self.STATE_FAULTS.get(fault, "") + GH_DOUBLE
            prelude += "sleep() { :; }\ngit() {\n  printf '%s\\n' \"$*\" >> \"$CALL_LOG\"\n"
            main_push = '[ "$*" != "push -q origin HEAD:main" ]'
            injections = {
                "inspect-fails": '[ "$*" != "diff --name-only --diff-filter=U" ] || return 7',
                "head-lookup-fails": '[ "$*" != "rev-parse --verify CHERRY_PICK_HEAD" ] || return 7',
                "stage-fails": f'[ "$*" != "add {manifest}" ] || return 7',
                # Simulate a staging tool reporting success without resolving
                # the index: real --continue must fail at the same commit.
                "no-progress": f'[ "$*" != "add {manifest}" ] || return 0',
                "continue-fails": '[ "$*" != "cherry-pick --continue" ] || return 7',
                "recovery-push-fails": 'case "$*" in *refs/review-loop/recovery/*) [ "$1" != push ] || return 7 ;; esac',
                # The push of main never reaches the remote.
                "main-push-fails": main_push + " || return 7",
                # The remote accepts the push but the client sees an error.
                "main-push-reported-failed": main_push + ' || { command git "$@"; return 7; }',
                # Another landing reaches main between the gate and the push.
                "main-moved-during-landing": main_push + ' || command git --git-dir="$REMOTE" update-ref refs/heads/main "$RACER"',
                # A carried commit rewrites the script while it runs: larger
                # than before, so bash would find text at its old offset.
                "script-replaced-mid-run": '[ "$1" != cherry-pick ] || for n in $(seq 4000); do echo "echo REPLACED; exit 97"; done > "$SCRIPT"',
            }
            if fault in injections:
                prelude += "  " + injections[fault] + "\n"
            prelude += '  command git "$@"\n}\n'
            if fault == "generator-fails":
                prelude += "python3() { return 9; }\n"
            doubles = root / "doubles.sh"
            doubles.write_text(prelude)
            proc = subprocess.run(["bash", str(script), str(train)], cwd=work,
                                  env=dict(env, BASH_ENV=str(doubles)),
                                  text=True, capture_output=True, timeout=120)
            log = root / "git-calls.log"
            calls = log.read_text().splitlines() if log.exists() else []
            pushes = [c for c in calls if c.startswith("push ")]
            return {
                "exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                "calls": calls, "executed": (work / "executed").exists(),
                "pushes": len(pushes),
                "push_order": [
                    "recovery" if "refs/review-loop/recovery/" in c
                    else "heads" if c.startswith("push -q --atomic ")
                    else "main" if c == "push -q origin HEAD:main"
                    else "restore" if c.startswith("push -q --force-with-lease=")
                    else "other"
                    for c in pushes
                ],
                "head_push": next((c for c in pushes if c.startswith("push -q --atomic ")), ""),
                "starts": sum(c.startswith("cherry-pick ") and not c.startswith("cherry-pick --") for c in calls),
                "continues": calls.count("cherry-pick --continue"),
                "remote_changed": ref("refs/heads/main") != base,
                "remote_main": ref("refs/heads/main"),
                "remote_tree": git(remote, "rev-parse", "refs/heads/main^{tree}"),
                "expected_tree": tree,
                "base": base, "racer": racer, "frozen": heads,
                "branches": [ref(f"refs/heads/unit-{n}") for n in (1, 2, 3)],
                "pulls": [ref(f"refs/pull/{n}/head") for n in (1, 2, 3)],
                "recovery": [ref(f"refs/review-loop/recovery/pr-{n}/{head}")
                             for n, head in enumerate(heads, 1)],
                "merged": [(remote / f"merged-{n}").exists() for n in (1, 2, 3)],
                "landed_parents": [
                    git(remote, "rev-list", "--count", f"{base}..refs/pull/{n}/head")
                    for n in (1, 2, 3)
                ],
            }

    def assert_nothing_moved(self, result, pushes=0):
        self.assertNotEqual(result["exit"], 0, result)
        self.assertEqual(result["pushes"], pushes, result)
        self.assertFalse(result["remote_changed"], result)
        self.assertEqual(result["merged"], [False, False, False], result)
        self.assertNotIn("MERGED", result["stdout"], result)

    def test_three_units_resolve_two_manifest_conflicts_without_replay(self):
        result = self.run_sequence()
        self.assertEqual(result["exit"], 0, result)
        self.assertEqual(result["starts"], 1, result)
        self.assertEqual(result["continues"], 2, result)
        self.assertEqual(result["push_order"], ["recovery", "heads", "main"], result)
        self.assertEqual(result["remote_tree"], result["expected_tree"], result)

    def test_every_carried_pr_ends_merged_on_a_stacked_head(self):
        result = self.run_sequence()
        self.assertEqual(result["exit"], 0, result)
        # Each frozen head was recorded before any head moved.
        self.assertEqual(result["recovery"], result["frozen"], result)
        self.assertEqual(result["stdout"].count("RECOVERY_REF "), 3, result)
        # Every head moved under an exact lease on its frozen SHA, atomically.
        for number, head in enumerate(result["frozen"], 1):
            self.assertIn(f"--force-with-lease=refs/heads/unit-{number}:{head}",
                          result["head_push"])
        self.assertIn("--atomic", result["head_push"])
        # The landed heads are new commits, stacked in train order, and main
        # is the last of them.
        self.assertEqual(result["landed_parents"], ["1", "2", "3"], result)
        self.assertEqual(result["pulls"][2], result["remote_main"], result)
        # Units 2 and 3 land on new parents, so their heads are new commits.
        # Unit 1 already sat on the gated base; with this fixture's fixed
        # dates its cherry-pick is the same commit, and the leased push of an
        # unchanged head is a no-op that must still end merged.
        for frozen, landed in list(zip(result["frozen"], result["pulls"]))[1:]:
            self.assertNotEqual(frozen, landed, result)
        self.assertEqual(result["merged"], [True, True, True], result)
        self.assertEqual(result["stdout"].count("\nMERGED "), 3, result)
        self.assertNotIn("NOT_MERGED", result["stderr"], result)
        self.assertNotIn("LEAVE_OPEN", result["stderr"], result)
        # The model deletes merged head branches, as GitHub did in the trial.
        self.assertEqual(result["branches"], [None, None, None], result)

    def test_a_two_commit_pr_lands_on_the_commit_that_completes_it(self):
        result = self.run_sequence(two_commit_unit=True)
        self.assertEqual(result["exit"], 0, result)
        self.assertEqual(result["landed_parents"], ["2", "3", "4"], result)
        self.assertEqual(result["merged"], [True, True, True], result)
        self.assertEqual(result["remote_tree"], result["expected_tree"], result)

    def test_pr_tips_must_follow_commit_order_and_end_the_train(self):
        for tips, message in (((1, 0, 2), "not in COMMITS in train order"),
                              ((0, 1, 1), "last PR tip is not the last reviewed commit")):
            with self.subTest(tips=tips):
                result = self.run_sequence(tips=tips)
                self.assert_nothing_moved(result)
                self.assertEqual(result["starts"], 0, result)
                self.assertIn(message, result["stderr"])

    def test_github_state_guard_refuses_before_any_push(self):
        for fault in self.STATE_FAULTS:
            with self.subTest(fault=fault):
                result = self.run_sequence(fault)
                self.assert_nothing_moved(result)
                self.assertEqual(result["branches"], result["frozen"], result)
                self.assertIn("nothing was pushed", result["stderr"])

    def test_moved_head_dissolves_the_train_before_any_push(self):
        result = self.run_sequence("head-moved")
        self.assert_nothing_moved(result)
        self.assertIn("PR head moved; dissolve the train", result["stderr"])

    def test_no_head_moves_without_a_recorded_recovery_ref(self):
        result = self.run_sequence("recovery-push-fails")
        self.assert_nothing_moved(result, pushes=1)
        self.assertEqual(result["branches"], result["frozen"], result)
        self.assertEqual(result["recovery"], [None, None, None], result)
        self.assertIn("no head was moved", result["stderr"])

    def test_refused_lease_moves_no_head_at_all(self):
        result = self.run_sequence("lease-refused")
        self.assert_nothing_moved(result, pushes=2)
        self.assertEqual(result["push_order"], ["recovery", "heads"], result)
        frozen = result["frozen"]
        self.assertEqual(result["branches"], [frozen[0], result["racer"], frozen[2]], result)
        self.assertEqual(result["pulls"], frozen, result)
        self.assertIn("leased head push refused", result["stderr"])

    def test_main_is_not_pushed_until_every_pr_shows_its_new_head(self):
        result = self.run_sequence("pull-refs-do-not-follow")
        self.assertNotEqual(result["exit"], 0, result)
        self.assertFalse(result["remote_changed"], result)
        self.assertNotIn("main", result["push_order"], result)
        self.assertEqual(result["push_order"][:2], ["recovery", "heads"], result)
        self.assertEqual(result["push_order"][2:], ["restore"] * 3, result)
        self.assertEqual(result["branches"], result["frozen"], result)
        self.assertIn("does not show the pushed head", result["stderr"])

    def test_failed_main_push_restores_every_head(self):
        result = self.run_sequence("main-push-fails")
        self.assertNotEqual(result["exit"], 0, result)
        self.assertFalse(result["remote_changed"], result)
        self.assertEqual(result["starts"], 4, result)
        self.assertEqual(result["branches"], result["frozen"], result)
        self.assertEqual(result["pulls"], result["frozen"], result)
        self.assertEqual(result["merged"], [False, False, False], result)
        self.assertIn("landing did not complete after 4 attempts", result["stderr"])

    def test_push_accepted_but_reported_failed_still_lands(self):
        result = self.run_sequence("main-push-reported-failed")
        self.assertEqual(result["exit"], 0, result)
        self.assertEqual(result["starts"], 1, result)
        self.assertNotIn("restore", result["push_order"], result)
        self.assertEqual(result["remote_tree"], result["expected_tree"], result)
        self.assertEqual(result["merged"], [True, True, True], result)
        self.assertEqual(result["stdout"].count("\nMERGED "), 3, result)

    def test_main_moved_during_landing_restores_heads_and_stops(self):
        result = self.run_sequence("main-moved-during-landing")
        self.assertNotEqual(result["exit"], 0, result)
        self.assertEqual(result["remote_main"], result["racer"], result)
        self.assertEqual(result["branches"], result["frozen"], result)
        self.assertEqual(result["merged"], [False, False, False], result)
        self.assertIn("main moved; rebuild and rerun the combined gate", result["stderr"])

    def test_candidate_must_match_the_gated_base_and_tree(self):
        # Both values are well-formed object names; only the loop's own
        # comparison with the fetched main and the rebuilt tree can refuse.
        for replacement, starts, message in (
            (r"VALIDATED_BASE=\1\nVALIDATED_TREE=\1", 1,
             "integrated tree differs from the validated candidate"),
            (r"VALIDATED_BASE=\2\nVALIDATED_TREE=\2", 0,
             "main moved; rebuild and rerun the combined gate"),
        ):
            with self.subTest(message=message):
                result = self.run_sequence(train_edit=lambda text: re.sub(
                    r"(?m)^VALIDATED_BASE=(\w+)\nVALIDATED_TREE=(\w+)$", replacement, text))
                self.assert_nothing_moved(result)
                self.assertEqual(result["starts"], starts, result)
                self.assertIn(message, result["stderr"])

    def test_script_replaced_while_it_runs_still_lands_the_same_train(self):
        result = self.run_sequence("script-replaced-mid-run")
        self.assertEqual(result["exit"], 0, result)
        self.assertNotIn("REPLACED", result["stdout"], result)
        self.assertEqual(result["push_order"], ["recovery", "heads", "main"], result)
        self.assertEqual(result["remote_tree"], result["expected_tree"], result)
        self.assertEqual(result["stdout"].count("\nMERGED "), 3, result)

    # A well-formed train file for a repository that has none of its objects.
    SHAS = tuple(letter * 40 for letter in "abcd")
    TRAIN = (
        "VALIDATED_BASE={0}\nVALIDATED_TREE={3}\nCOMMITS={1} {2}\n"
        "PR_NUMBERS=1 2\nPR_HEADS={1} {2}\nPR_HEAD_REFS=unit-1 unit-2\n"
        "PR_TIPS={1} {2}\n"
    ).format(*SHAS)

    def run_reader(self, train_text, shell="bash"):
        """Run the script on a train file in an empty repository with no remote.

        Nothing can be fetched or pushed there, so a train file that passes
        the form checks still ends in a refusal. The log shows every `git`,
        `gh` and `python3` call the script made.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            work, log = root / "work", root / "calls.log"
            work.mkdir()
            env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                       GIT_CEILING_DIRECTORIES=str(root), BASH_ENV=str(root / "doubles.sh"))
            subprocess.run(["git", "init", "-q", "-b", "main"], cwd=work, env=env, check=True)
            (root / "train.txt").write_text(train_text)
            (root / "doubles.sh").write_text(
                f"CALL_LOG={shlex.quote(str(log))}\n"
                "git() { printf 'git %s\\n' \"$*\" >> \"$CALL_LOG\"; command git \"$@\"; }\n"
                "gh() { printf 'gh %s\\n' \"$*\" >> \"$CALL_LOG\"; return 1; }\n"
                "python3() { printf 'python3 %s\\n' \"$*\" >> \"$CALL_LOG\"; return 1; }\n"
                "sleep() { :; }\n")
            proc = subprocess.run([shell, str(LANDING_SCRIPT), str(root / "train.txt")],
                                  cwd=work, env=env, text=True, capture_output=True, timeout=60)
            return {
                "exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                "calls": log.read_text().splitlines() if log.exists() else [],
                "executed": (work / "executed").exists(),
            }

    def test_well_formed_train_file_reaches_the_loop_and_its_guards(self):
        result = self.run_reader(self.TRAIN)
        self.assertEqual(result["exit"], 1, result)
        self.assertIn("git check-ref-format refs/heads/unit-1", result["calls"])
        self.assertIn("git fetch -q origin +refs/heads/main:refs/remotes/origin/main",
                      result["calls"])
        self.assertIn("FAILED: landing did not complete after 4 attempts", result["stderr"])
        # The guards of the loop still judge the inventory, not the reader.
        for edit, message in (
            (("PR_NUMBERS=1 2", "PR_NUMBERS=1"),
             "FAILED: PR number/head/branch/tip inventory mismatch\n"),
            (("PR_NUMBERS=1 2", "PR_NUMBERS="),
             "FAILED: PR number/head/branch/tip inventory mismatch\n"),
            (("PR_TIPS={1} {2}".format(*self.SHAS), "PR_TIPS={2} {1}".format(*self.SHAS)),
             "FAILED: PR tip {1} is not in COMMITS in train order\n".format(*self.SHAS)),
            (("PR_TIPS={1} {2}".format(*self.SHAS), "PR_TIPS={1} {1}".format(*self.SHAS)),
             "FAILED: the last PR tip is not the last reviewed commit\n"),
        ):
            with self.subTest(message=message):
                self.assertIn(edit[0], self.TRAIN)
                result = self.run_reader(self.TRAIN.replace(*edit))
                self.assertEqual(result["exit"], 1, result)
                self.assertEqual(result["stderr"], message, result)
                self.assertFalse([c for c in result["calls"]
                                  if not c.startswith("git check-ref-format ")], result)

    def test_malformed_train_file_stops_before_any_other_command(self):
        def line(name, value):
            return lambda text: re.sub(rf"(?m)^{name}=.*$", f"{name}={value}", text)

        def drop(name):
            return lambda text: re.sub(rf"(?m)^{name}=.*\n", "", text)

        sha = "0123456789abcdef0123456789abcdef01234567"
        cases = (
            (lambda text: text + "EXTRA=1\n", "line 8 is not one of the seven"),
            (lambda text: text + "export PR_TIPS\n", "line 8 is not one of the seven"),
            (lambda text: " " + text, "line 1 is not one of the seven"),
            (lambda text: text + "PR_NUMBERS=1 2\n", "line 8 sets PR_NUMBERS a second time"),
            (drop("VALIDATED_BASE"), "VALIDATED_BASE is missing"),
            (drop("COMMITS"), "COMMITS is missing"),
            (drop("PR_TIPS"), "PR_TIPS is missing"),
            (line("VALIDATED_BASE", ""), "VALIDATED_BASE needs exactly one entry"),
            (line("VALIDATED_TREE", f"{sha} {sha}"), "VALIDATED_TREE needs exactly one entry"),
            (line("VALIDATED_BASE", sha[:12]), "VALIDATED_BASE entry is not a full object name"),
            (line("VALIDATED_BASE", sha.upper()), "VALIDATED_BASE entry is not a full object name"),
            (line("VALIDATED_BASE", sha + "0"), "VALIDATED_BASE entry is not a full object name"),
            (line("VALIDATED_TREE", "HEAD^{tree}"), "VALIDATED_TREE entry is not a full object name"),
            (line("COMMITS", "unit-1 unit-2"), "COMMITS entry is not a full object name: unit-1"),
            (line("PR_HEADS", f"{sha}\t{sha}"), "PR_HEADS entry is not a full object name"),
            (line("PR_TIPS", f"{sha} {sha}\r"), "PR_TIPS entry is not a full object name"),
            (line("PR_NUMBERS", "1 #2"), "PR_NUMBERS entry is not a PR number: #2"),
            (line("PR_NUMBERS", "1 -2"), "PR_NUMBERS entry is not a PR number: -2"),
            (line("PR_NUMBERS", "*"), "PR_NUMBERS entry is not a PR number: *"),
            (line("PR_HEAD_REFS", "unit-1 unit..2"), "PR_HEAD_REFS entry is not a branch name: unit..2"),
            (line("PR_HEAD_REFS", "unit-1 unit-2:main"), "PR_HEAD_REFS entry is not a branch name: unit-2:main"),
            (line("PR_HEAD_REFS", "*"), "PR_HEAD_REFS entry is not a branch name: *"),
        )
        for edit, message in cases:
            with self.subTest(message=message):
                edited = edit(self.TRAIN)
                self.assertNotEqual(edited, self.TRAIN)
                result = self.run_reader(edited)
                self.assertEqual(result["exit"], 1, result)
                self.assertEqual(result["stdout"], "", result)
                self.assertIn("FAILED: train file: " + message, result["stderr"], result)
                # Only the form of a branch name was asked of git: no fetch,
                # no cherry-pick, no push and no call to GitHub.
                self.assertFalse([c for c in result["calls"]
                                  if not c.startswith("git check-ref-format ")], result)

    def test_train_file_is_parsed_and_never_executed(self):
        payloads = (
            "$(touch executed)",
            "`touch executed`",
            "unit-1; touch executed",
            "unit-1\ntouch executed",
            "unit-1 && touch executed",
            "unit-1 | touch executed",
            "unit-1 > executed",
        )
        for name in ("VALIDATED_BASE", "COMMITS", "PR_NUMBERS", "PR_HEAD_REFS"):
            for payload in payloads:
                with self.subTest(name=name, payload=payload):
                    result = self.run_reader(re.sub(
                        rf"(?m)^{name}=.*$", lambda _: f"{name}={payload}", self.TRAIN))
                    self.assertEqual(result["exit"], 1, result)
                    self.assertFalse(result["executed"], result)
                    self.assertIn("FAILED: ", result["stderr"], result)
                    self.assertFalse([c for c in result["calls"] if c.startswith("git push")
                                      or c.startswith("gh ")], result)

    def test_branch_names_that_look_like_commands_move_nothing(self):
        # Three entries that git accepts as branch names: the inventory
        # matches, so the refusal comes from the GitHub-state guard.
        result = self.run_sequence(train_edit=lambda text: text.replace(
            "PR_HEAD_REFS=unit-1 unit-2 unit-3", "PR_HEAD_REFS=unit-1; touch executed"))
        self.assert_nothing_moved(result)
        self.assertFalse(result["executed"], result)
        self.assertIn("nothing was pushed", result["stderr"])

    def test_train_file_comments_blank_lines_and_missing_final_newline(self):
        result = self.run_sequence(
            train_edit=lambda text: "# frozen train\n\n" + text.replace("\nPR_", "\n\n# next\nPR_").rstrip("\n"))
        self.assertEqual(result["exit"], 0, result)
        self.assertEqual(result["stdout"].count("\nMERGED "), 3, result)
        self.assertEqual(result["remote_tree"], result["expected_tree"], result)

    def test_script_needs_exactly_one_readable_train_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            for args, message in (
                ([], "FAILED: usage: land_train.sh <train-file>"),
                (["a", "b"], "FAILED: usage: land_train.sh <train-file>"),
                (["missing-train-file"], "FAILED: train file: cannot read missing-train-file"),
                ([tmp], f"FAILED: train file: cannot read {tmp}"),
            ):
                with self.subTest(args=args):
                    proc = subprocess.run(["bash", str(LANDING_SCRIPT), *args], cwd=tmp,
                                          text=True, capture_output=True, timeout=60)
                    self.assertEqual(proc.returncode, 1, proc)
                    self.assertEqual(proc.stdout, "", proc)
                    self.assertEqual(proc.stderr.strip(), message, proc)

    @unittest.skipUnless(shutil.which("dash"), "requires dash")
    def test_a_shell_that_is_not_bash_is_refused_at_the_first_command(self):
        result = self.run_reader(self.TRAIN, shell="dash")
        self.assertEqual(result["exit"], 1, result)
        self.assertEqual(result["calls"], [], result)
        self.assertEqual(result["stderr"].strip(), "FAILED: run the landing loop with bash")

    def test_single_repair_mutation_cannot_land_three_units(self):
        result = self.run_sequence(mutate_loop=True)
        self.assert_nothing_moved(result)

    def test_later_source_conflict_is_not_treated_as_another_manifest(self):
        result = self.run_sequence("later-source-conflict")
        self.assert_nothing_moved(result)
        self.assertEqual(result["starts"], 1, result)
        self.assertEqual(result["continues"], 1, result)
        self.assertIn("source conflict or sequencer failure", result["stderr"])

    def test_manifest_sequence_tool_failures_and_no_progress_fail_closed(self):
        for fault in ("inspect-fails", "head-lookup-fails", "stage-fails", "no-progress",
                      "continue-fails", "generator-fails"):
            with self.subTest(fault=fault):
                result = self.run_sequence(fault)
                self.assert_nothing_moved(result)
                self.assertEqual(result["starts"], 1, result)
                if fault == "no-progress":
                    self.assertIn("no sequencer progress", result["stderr"])


if __name__ == "__main__":
    unittest.main()
