#!/usr/bin/env python3
"""Tests for the derivation-obligation registry/note reconciliation lint.

`docs/audit/data/derivation_obligations.json` and the source note named by each
entry's `current_path` are two records of the same open obligation. Before this
rule nothing compared them: `audit_lint` checked `target` for truthiness only,
no rule in the repository read `self_liquidation_condition`, and the note was
never opened — so a registry entry could record a weaker target or a closure
condition copied from a different section of its own note with no gate firing.

The lint never repairs a divergence and never decides which surface is right:
what an obligation demands is owner/audit-lane content. It reports, and the
current population is grandfathered in a shrink-only baseline.

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

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPTS_DIR = REPO_ROOT / "audit" / "scripts"
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
    return {
        kind
        for kind, _message in audit_lint.obligation_reconciliation_findings(
            dep_id, entry, note, row
        )
    }


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
                "example_obligation", entry, ALIGNED_NOTE, OPEN_GATE_ROW
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
                dep_id, entry, note_text, None
            ):
                found.add(f"{dep_id}:{kind}")
        return found

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

    def test_no_live_divergence_escapes_the_baseline(self):
        # Exactly the invariant strict lint enforces: a NEW divergence is an
        # error. Failing here means a registry entry or its note drifted apart
        # without owner adjudication.
        escaped = sorted(self.live_findings() - self.baseline)
        self.assertEqual(escaped, [], f"un-grandfathered divergences: {escaped}")

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


class ChainSatisfactionBoundaryTest(unittest.TestCase):
    """Lock the certification/retention divergence the false docstring hid.

    `compute_lane_certification.status_satisfies_certification` claimed to
    "match the pipeline's chain boundary", but
    `compute_effective_status.is_chain_satisfying_status` accepts `meta` and it
    does not. The asymmetry is deliberate policy
    (`lane_certification_config.json`: "Metadata does not"), and it is why
    `meta` rows inside a lane closure are permanent blockers. These assertions
    make a silent drift in either direction fail a test instead of a docstring.
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
