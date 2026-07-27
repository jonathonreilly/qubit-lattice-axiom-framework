#!/usr/bin/env python3
"""Tests for the derivation-obligation registry/note reconciliation lint.

`docs/audit/data/derivation_obligations.json` and the source note named by each
entry's `current_path` are two records of the same open obligation. Before this
rule nothing reconciled them: `audit_lint` checked `target` for truthiness only,
no rule in the repository validated `self_liquidation_condition` against its
note (`no_go_discipline_gate` reads the field, but only to pick an evidence
excerpt), and the note was never opened — so a registry entry could record a
weaker target or a closure condition copied from a different section of its own
note with no gate firing.

The lint never repairs a divergence and never decides which surface is right:
what an obligation demands is owner/audit-lane content. Exact mechanical
comparisons are error-eligible with the current population grandfathered in a
shrink-only baseline; the one lexical comparison is advisory at every run and
cannot be baselined; the `open_gate` typing invariant is neither.

Run via:
  python3 -m unittest docs.audit.scripts.tests.test_derivation_obligation_reconciliation
or:
  python3 docs/audit/scripts/tests/test_derivation_obligation_reconciliation.py
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

# parents[3] of docs/audit/scripts/tests/<file> is docs/, not the repo root.
DOCS_ROOT = Path(__file__).resolve().parents[3]
SCRIPTS_DIR = DOCS_ROOT / "audit" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import audit_lint  # noqa: E402


ALIGNED_NOTE = """# Example Obligation

**Type:** open_gate

## Exact target

Derive from the retained framework chain whether the widget carrier is the
`same` physical channel as the sprocket readout.

Trailing paragraph that is not part of the target.

## Closure criterion

A closing theorem must construct the widget carrier, identify its physical
readout map, and prove the sprocket correspondence.

## Running-program relation

This obligation is self-liquidating. If the running widget program derives
this exact channel at retained grade, the obligation is removed.

## Non-claims

This note derives no value and changes no audit verdict.
"""

ALIGNED_ENTRY = {
    "current_path": "docs/EXAMPLE_OBLIGATION.md",
    "target": (
        "Derive from the retained framework chain whether the widget carrier "
        "is the same physical channel as the sprocket readout."
    ),
    "self_liquidation_condition": (
        "A closing theorem that constructs the widget carrier, identifies its "
        "physical readout map, and proves the sprocket correspondence removes "
        "the obligation."
    ),
}

OPEN_GATE_ROW = {"claim_type": "open_gate"}


def kinds(entry, note=ALIGNED_NOTE, row=OPEN_GATE_ROW, dep_id="example_obligation"):
    findings = audit_lint.obligation_reconciliation_findings(dep_id, entry, note)
    findings += audit_lint.obligation_row_typing_findings(dep_id, row)
    return {kind for kind, _message in findings}


class ObligationReconciliationRuleTest(unittest.TestCase):
    def test_aligned_entry_produces_no_findings(self):
        self.assertEqual(kinds(ALIGNED_ENTRY), set())

    def test_backticks_and_wrapping_do_not_count_as_divergence(self):
        entry = dict(ALIGNED_ENTRY)
        entry["target"] = (
            "Derive from   the retained framework chain whether the `widget`\n"
            "carrier is the same physical channel as the `sprocket` readout."
        )
        self.assertEqual(kinds(entry), set())

    def test_target_that_drops_a_conjunct_is_reported(self):
        entry = dict(ALIGNED_ENTRY)
        entry["target"] = (
            "Derive whether the widget carrier is the same physical channel "
            "as the sprocket readout."
        )
        self.assertIn("target_mismatch", kinds(entry))

    def test_target_mismatch_message_quotes_both_surfaces(self):
        entry = dict(ALIGNED_ENTRY)
        entry["target"] = "Derive whether the widget carrier is anything at all."
        message = dict(
            audit_lint.obligation_reconciliation_findings(
                "example_obligation", entry, ALIGNED_NOTE
            )
        )["target_mismatch"]
        self.assertIn("anything at all", message)
        self.assertIn("sprocket readout", message)

    def test_missing_exact_target_section_is_reported(self):
        note = ALIGNED_NOTE.replace("## Exact target", "## Goal")
        self.assertIn("exact_target_section_missing", kinds(ALIGNED_ENTRY, note=note))

    def test_missing_closure_criterion_section_is_reported(self):
        note = ALIGNED_NOTE.replace("## Closure criterion", "## How it closes")
        self.assertIn(
            "closure_criterion_section_missing", kinds(ALIGNED_ENTRY, note=note)
        )

    def test_absent_self_liquidation_condition_is_reported(self):
        entry = dict(ALIGNED_ENTRY)
        entry.pop("self_liquidation_condition")
        self.assertIn("self_liquidation_condition_missing", kinds(entry))

    def test_closure_condition_copied_from_another_section_is_reported(self):
        # The measured defect: the registry paraphrases the note's
        # "## Running-program relation" instead of its "## Closure criterion",
        # dropping the conjuncts the auditor treats as binding.
        entry = dict(ALIGNED_ENTRY)
        entry["self_liquidation_condition"] = (
            "A retained widget-program theorem deriving this exact channel "
            "removes the obligation; until then it blocks dependent closure."
        )
        self.assertIn("closure_condition_not_grounded", kinds(entry))

    def test_closure_condition_grounded_in_the_criterion_passes(self):
        entry = dict(ALIGNED_ENTRY)
        entry["self_liquidation_condition"] = (
            "A closing theorem constructing the widget carrier and proving the "
            "sprocket correspondence removes the obligation."
        )
        self.assertNotIn("closure_condition_not_grounded", kinds(entry))

    def test_uncited_governance_source_is_reported(self):
        entry = dict(ALIGNED_ENTRY)
        entry["historical_governance_source"] = "docs/SOME_GOVERNANCE_DECISION.md"
        self.assertIn("governance_source_not_cited", kinds(entry))

    def test_cited_governance_source_passes(self):
        entry = dict(ALIGNED_ENTRY)
        entry["historical_governance_source"] = "docs/SOME_GOVERNANCE_DECISION.md"
        note = ALIGNED_NOTE + "\nAdopted via `SOME_GOVERNANCE_DECISION.md`.\n"
        self.assertNotIn("governance_source_not_cited", kinds(entry, note=note))

    def test_fenced_heading_does_not_hijack_a_section(self):
        # A fenced ``## Exact target`` is sample text, not a section. Parsed as
        # one it replaced the real body and produced a target_mismatch ERROR
        # against a registry entry that matched its note exactly.
        note = ALIGNED_NOTE + (
            "\n## Appendix\n\n```\n## Exact target\n"
            "Sample text that is not the target.\n```\n"
        )
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())
        self.assertNotIn("Exact target", audit_lint.markdown_sections(
            "# T\n\n## Only\n\n~~~\n## Exact target\nfenced\n~~~\n"
        ))

    def test_repeated_heading_keeps_the_first_body(self):
        note = ALIGNED_NOTE + (
            "\n## Exact target\n\nA later restatement that is not the target.\n"
        )
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())

    def test_atx_closed_heading_names_the_section(self):
        # `## Exact target ##` is valid Markdown for the same heading. Reading
        # the trailing hashes as part of the name made a valid note report
        # exact_target_section_missing as a hard error.
        note = ALIGNED_NOTE.replace("## Exact target", "## Exact target ##")
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())

    def test_a_shorter_run_does_not_close_a_longer_fence(self):
        note = ALIGNED_NOTE + (
            "\n## Appendix\n\n````\n```\n## Exact target\nnot the target\n````\n"
        )
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())

    def test_an_info_string_line_does_not_close_a_fence(self):
        note = ALIGNED_NOTE + (
            "\n## Appendix\n\n```\n```python\n## Exact target\nnot the target\n```\n"
        )
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())

    def test_only_an_unindented_heading_opens_a_section(self):
        # Deliberate departure from CommonMark, locked here so it stays a
        # decision rather than drifting: an indented `##` is also how a heading
        # nested in a list item looks, and separating the two needs full
        # container parsing (marker width, content indent, lazy continuation).
        # The two failure modes are not symmetric. A nested heading accepted as
        # a section claims the name first and silently compares the wrong text
        # against the registry; a top-level heading indented 1-3 spaces and
        # missed raises exact_target_section_missing, which names the file and
        # the section and is fixed by unindenting it. Take the loud failure.
        self.assertEqual(kinds(ALIGNED_ENTRY), set())
        for indent in (" ", "  ", "   ", "    "):
            note = ALIGNED_NOTE.replace("## Exact target", indent + "## Exact target")
            self.assertNotIn("Exact target", audit_lint.markdown_sections(note))
            self.assertIn(
                "exact_target_section_missing",
                kinds(ALIGNED_ENTRY, note=note),
                repr(indent),
            )

    def test_a_fence_interrupting_the_target_paragraph_is_dropped(self):
        # A fence may interrupt a paragraph with no blank line. Folding its
        # lines into the section made them part of the opening paragraph the
        # target comparison reads, producing a false target_mismatch.
        note = ALIGNED_NOTE.replace(
            "`same` physical channel as the sprocket readout.\n",
            "`same` physical channel as the sprocket readout.\n"
            "```\nsample text\n```\n",
        )
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())

    def test_a_heading_nested_in_a_list_item_is_not_a_section(self):
        # CommonMark allows a heading inside a list item. Read as a section it
        # claims the name FIRST, so the real top-level heading is ignored as a
        # repeat and the note reports a target_mismatch it does not have. This
        # is why a section heading must be unindented: every nested heading is
        # indented by construction, at whatever the item's content indent is.
        markers = ("-", "*", "+", "1.", "2)", "10.")
        for marker in markers:
            for indent in ("  ", "   ", "    "):
                note = ALIGNED_NOTE.replace(
                    "## Exact target",
                    f"{marker} item\n{indent}## Exact target\n{indent}nested body\n"
                    "\n## Exact target",
                    1,
                )
                self.assertEqual(
                    kinds(ALIGNED_ENTRY, note=note), set(), f"{marker!r}/{indent!r}"
                )
                self.assertNotIn(
                    "nested body", audit_lint.markdown_sections(note)["Exact target"]
                )

    def test_a_lazy_continuation_does_not_expose_a_nested_heading(self):
        # CommonMark lazy continuation: an unindented paragraph line continues
        # the list item, so the list is still open at the nested heading. Any
        # rule that decided "unindented prose closes the list" would let the
        # nested heading through; an unindented-only heading rule cannot.
        note = ALIGNED_NOTE.replace(
            "## Exact target",
            "1. item\nlazy continuation\n   ## Exact target\n   nested body\n"
            "\n## Exact target",
            1,
        )
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())
        self.assertNotIn(
            "nested body", audit_lint.markdown_sections(note)["Exact target"]
        )

    def test_a_blockquoted_heading_is_not_a_section(self):
        note = ALIGNED_NOTE + "\n> ## Exact target\n> quoted\n"
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())

    def test_an_unindented_heading_after_a_list_is_a_section(self):
        # An ATX heading is never a lazy continuation, so an unindented heading
        # ends the list and opens its section normally.
        note = ALIGNED_NOTE.replace(
            "## Closure criterion", "- item\n- item two\n## Closure criterion", 1
        )
        self.assertIn("Closure criterion", audit_lint.markdown_sections(note))
        self.assertEqual(kinds(ALIGNED_ENTRY, note=note), set())

    def test_a_dropped_fence_still_separates_the_paragraphs_it_split(self):
        # A fence between two paragraphs with no blank lines is a paragraph
        # break. Removing its lines outright would splice the paragraphs into
        # one and make the second paragraph part of the compared target.
        note = (
            "# Example\n\n## Exact target\n\nDerive the widget carrier.\n"
            "```\nsample\n```\n"
            "A second paragraph that is not the target.\n\n"
            "## Closure criterion\n\nA closing theorem constructs it.\n"
        )
        entry = dict(ALIGNED_ENTRY)
        entry["target"] = "Derive the widget carrier."
        self.assertNotIn("target_mismatch", kinds(entry, note=note))

    def test_live_obligation_notes_parse_to_their_four_sections(self):
        # The fence/heading rules must not change the live population's parse.
        registry = json.loads(
            audit_lint.DERIVATION_OBLIGATIONS_PATH.read_text(encoding="utf-8")
        )
        for dep_id, entry in sorted((registry.get("nodes") or {}).items()):
            note_path = audit_lint.REPO_ROOT / entry["current_path"]
            parsed = audit_lint.markdown_sections(
                note_path.read_text(encoding="utf-8")
            )
            self.assertEqual(
                sorted(parsed),
                [
                    "Closure criterion",
                    "Exact target",
                    "Non-claims",
                    "Running-program relation",
                ],
                dep_id,
            )

    def test_obligation_row_typed_away_from_open_gate_is_reported(self):
        # The registry preamble promises obligations "never satisfy dependency
        # closure". Only claim_type == open_gate carries that promise through
        # compute_effective_status.clean_status; a bounded_theorem retyping
        # plus a clean verdict would launder an open obligation into a
        # retained-grade premise.
        self.assertIn(
            "ledger_row_not_open_gate",
            kinds(ALIGNED_ENTRY, row={"claim_type": "bounded_theorem"}),
        )

    def test_meta_retyping_is_reported_too(self):
        # meta is the shorter version of the same hole:
        # is_chain_satisfying_status accepts "meta" directly, with no
        # retained-grade step in between. Requiring exactly open_gate covers it.
        self.assertIn(
            "ledger_row_not_open_gate",
            kinds(ALIGNED_ENTRY, row={"claim_type": "meta"}),
        )

    def test_typing_check_does_not_depend_on_the_note(self):
        # The invariant is row-only: it must not inherit the reconciliation
        # function's precondition that current_path exists on disk.
        self.assertEqual(
            [kind for kind, _ in audit_lint.obligation_row_typing_findings(
                "example_obligation", {"claim_type": "positive_theorem"}
            )],
            ["ledger_row_not_open_gate"],
        )

    def test_absent_ledger_row_does_not_assert_a_typing(self):
        # A registered obligation with no ledger row already errors elsewhere;
        # this rule must not invent a claim_type for it.
        self.assertNotIn("ledger_row_not_open_gate", kinds(ALIGNED_ENTRY, row=None))


class ObligationReconciliationBaselineTest(unittest.TestCase):
    """The shipped baseline is a ratchet over the real registry, not a switch."""

    def setUp(self):
        self.registry = json.loads(
            audit_lint.DERIVATION_OBLIGATIONS_PATH.read_text(encoding="utf-8")
        )
        self.baseline = {
            line.strip()
            for line in audit_lint.OBLIGATION_RECONCILIATION_BASELINE_PATH.read_text(
                encoding="utf-8"
            ).splitlines()
            if line.strip() and not line.strip().startswith("#")
        }

    def live_findings(self):
        found = set()
        for dep_id, entry in (self.registry.get("nodes") or {}).items():
            note_path = audit_lint.REPO_ROOT / (entry.get("current_path") or "")
            if not note_path.exists():
                continue
            note_text = note_path.read_text(encoding="utf-8", errors="replace")
            for kind, _message in audit_lint.obligation_reconciliation_findings(
                dep_id, entry, note_text
            ):
                found.add(f"{dep_id}:{kind}")
        return found

    def error_eligible_live_findings(self):
        return {
            key
            for key in self.live_findings()
            if key.rpartition(":")[2] not in audit_lint.OBLIGATION_RECONCILIATION_ADVISORY_KINDS
        }

    def test_every_baseline_line_is_a_registered_id_and_known_kind(self):
        registered = set(self.registry.get("nodes") or {})
        for line in sorted(self.baseline):
            dep_id, _, kind = line.rpartition(":")
            self.assertIn(dep_id, registered, f"{line}: unregistered obligation id")
            self.assertIn(
                kind,
                audit_lint.OBLIGATION_RECONCILIATION_KINDS,
                f"{line}: unknown finding kind",
            )

    def test_baseline_matches_the_live_error_eligible_population_exactly(self):
        # Both directions. `live - baseline` is the invariant the lint enforces:
        # a NEW divergence is an error. `baseline - live` is the drain the lint
        # can only report as a notice — asserting it here means a drained line
        # must be pruned in the same change, so the file cannot silently accrete
        # dead suppressions.
        self.assertEqual(
            sorted(self.error_eligible_live_findings()), sorted(self.baseline)
        )

    def test_advisory_kinds_are_never_baselined(self):
        # The lexical comparison cannot be suppressed by this file, so a line
        # naming it would be dead weight that implies an enforcement it lacks.
        advisory = sorted(
            line
            for line in self.baseline
            if line.rpartition(":")[2]
            in audit_lint.OBLIGATION_RECONCILIATION_ADVISORY_KINDS
        )
        self.assertEqual(advisory, [])
        self.assertTrue(
            audit_lint.OBLIGATION_RECONCILIATION_ADVISORY_KINDS
            & self.live_findings_kinds(),
            "the advisory kind should still reproduce live; if it no longer does, "
            "re-examine whether it is worth reporting at all",
        )

    def live_findings_kinds(self):
        return {key.rpartition(":")[2] for key in self.live_findings()}

    def test_typing_launder_is_not_grandfatherable(self):
        # ledger_row_not_open_gate protects the registry's own preamble promise
        # rather than reporting a wording divergence, so the baseline must not
        # be able to suppress it — in the rule, or in the shipped file.
        self.assertIn(
            "ledger_row_not_open_gate",
            audit_lint.OBLIGATION_RECONCILIATION_NON_GRANDFATHERABLE_KINDS,
        )
        laundered = sorted(
            line for line in self.baseline if line.endswith(":ledger_row_not_open_gate")
        )
        self.assertEqual(laundered, [])

    def test_every_live_obligation_row_is_typed_open_gate(self):
        # The live half of the non-grandfatherable invariant. The unit tests
        # above exercise the rule; this asserts the actual auditor-owned
        # claim_type on the three registered rows, which is what the rule
        # protects.
        import ledger_io

        rows = ledger_io.load_ledger()["rows"]
        for dep_id in sorted(self.registry.get("nodes") or {}):
            self.assertIn(dep_id, rows, f"{dep_id}: registered obligation has no row")
            self.assertEqual(
                [],
                audit_lint.obligation_row_typing_findings(dep_id, rows[dep_id]),
                f"{dep_id}: claim_type={rows[dep_id].get('claim_type')!r}",
            )


class ChainSatisfactionBoundaryTest(unittest.TestCase):
    """Lock the certification/retention divergence the false docstring hid.

    `compute_lane_certification.status_satisfies_certification` claimed to
    "match the pipeline's chain boundary", but
    `compute_effective_status.is_chain_satisfying_status` accepts `meta` and it
    does not. The asymmetry is deliberate policy
    (`lane_certification_config.json`: "Metadata does not"), and it is why a
    `meta` row inside a lane closure blocks that lane for as long as it stays
    typed `meta` — clearing it takes a source-level change, not audit
    throughput. These assertions make a silent drift in either direction fail a
    test instead of a docstring.
    """

    def setUp(self):
        import compute_effective_status
        import compute_lane_certification

        self.effective = compute_effective_status
        self.certification = compute_lane_certification

    def test_meta_satisfies_retention_but_not_certification(self):
        self.assertTrue(self.effective.is_chain_satisfying_status("meta"))
        self.assertFalse(self.certification.status_satisfies_certification("x", "meta"))

    def test_retained_grade_satisfies_both(self):
        for status in ("retained", "retained_bounded", "retained_no_go"):
            self.assertTrue(self.effective.is_chain_satisfying_status(status), status)
            self.assertTrue(
                self.certification.status_satisfies_certification("x", status), status
            )

    def test_unaudited_and_open_gate_satisfy_neither(self):
        for status in ("unaudited", "open_gate", "retained_pending_chain"):
            self.assertFalse(self.effective.is_chain_satisfying_status(status), status)
            self.assertFalse(
                self.certification.status_satisfies_certification("x", status), status
            )

    def test_certification_docstring_does_not_claim_parity(self):
        doc = re.sub(
            r"\s+", " ", self.certification.status_satisfies_certification.__doc__ or ""
        )
        self.assertNotIn("Match the pipeline's chain boundary", doc)
        self.assertIn("Metadata does NOT satisfy", doc)


if __name__ == "__main__":
    unittest.main()
