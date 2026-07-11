#!/usr/bin/env python3
"""Verification runner for the primitive-retirement review after the four-axiom reset.

The runner checks registry/source alignment and the narrow review conclusion:
the current four-axiom surface does not retire any approved framework primitive.
It does not modify the registry or apply audit verdicts.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "PRIMITIVE_RETIREMENT_REVIEW_AFTER_FOUR_AXIOM_RESET_NOTE_2026-07-05.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC_SUPPORT = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md"
KINETIC_B4_NOGO = ROOT / "docs" / "KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md"
KINETIC_BW_NOGO = ROOT / "docs" / "KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md"
KINETIC_COMPOSITION = ROOT / "docs" / "KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
DECISION_HISTORY = ROOT / "docs" / "audit" / "data" / "premise_decision_history.json"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
SCALE_RUNNER = ROOT / "scripts" / "scale_reference_primitive_boundary_check.py"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def norm(text: str) -> str:
    return " ".join(text.split())


def has(text: str, phrase: str) -> bool:
    return norm(phrase) in norm(text)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def main() -> int:
    print("=" * 78)
    print("PRIMITIVE RETIREMENT REVIEW AFTER FOUR-AXIOM RESET")
    print("=" * 78)
    print("Scope: review/gate-map verification only; no registry edit.")
    print()

    note = read(NOTE)
    axioms = read(AXIOMS)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    kinetic_support = read(KINETIC_SUPPORT)
    kinetic_b4 = read(KINETIC_B4_NOGO)
    kinetic_bw = read(KINETIC_BW_NOGO)
    kinetic_composition = read(KINETIC_COMPOSITION)
    registry = load_json(REGISTRY)
    tier_a = load_json(DECISION_HISTORY)
    ledger_rows = load_json(LEDGER)["rows"]
    scale_runner = read(SCALE_RUNNER)

    print("Registry/front-door checks")
    canonical = registry.get("canonical_ids", [])
    expected = [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]
    check("axiom premise registry has exactly the expected current ids", canonical == expected, str(canonical))
    nodes = registry.get("nodes", {})
    check("minimal axioms current path is the four-axiom memo", nodes["minimal_axioms"]["current_path"] == "docs/MINIMAL_AXIOMS_2026-06-29.md")
    check("scale primitive current path is stable", nodes["scale_reference_primitive"]["current_path"] == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    check("kinetic primitive current path is stable", nodes["kinetic_isotropy_primitive"]["current_path"] == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    check("realized-state primitive current path is stable", nodes["realized_state_primitive"]["current_path"] == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    check("decision history has zero active premise targets", tier_a.get("genuine_admitted_input_count") == 0, str(tier_a.get("genuine_admitted_input_count")))
    check("decision history canonical live IDs are empty", tier_a.get("canonical_ids") == [], str(tier_a.get("canonical_ids")))
    check("live derivation targets are empty on current main", tier_a.get("derivation_targets", {}) == {}, str(tier_a.get("derivation_targets", {})))
    retired_targets = tier_a.get("retired_derivation_targets", {})
    check("theta retirement is recorded separately", "strong_cp_theta_zero_note" in retired_targets)
    check("AC_phi_lambda retirement is recorded separately", "staggered_dirac_realization_gate_note_2026-05-03" in retired_targets)
    print()

    print("Updated axiom-surface checks")
    for phrase in [
        "Physical sites are the points of the cubic lattice `Z^3`",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "There is one fixed nearest-neighbor admissibility rule",
        "Records form.",
        "A state is a configuration of records.",
        "A law privileges no states.",
        "A choice not fixed by the supplied structure remains a named conditional or open dependency.",
        "Admissibility is not a dynamics axiom.",
        "It does not choose a Hamiltonian or transfer operator",
        "define a time metric",
        "scale-reference primitive",
    ]:
        check(f"axiom memo contains boundary: {phrase[:52]}", has(axioms, phrase))
    print()

    print("Primitive source-boundary checks")
    check("scale source declares exactly one dimensionful reference", "exactly one dimensionful reference" in scale)
    check("scale source declares units conversion, not physics axiom", "This is a units conversion, not a physics axiom." in scale)
    check("scale source forbids dimensionless content", "zero dimensionless" in scale)
    check("scale source does not derive a/l_P=1", "It does not assert `a/l_P = 1` as a derived theorem." in scale)
    check("kinetic source declares c_t=c_s", "c_t = c_s" in kinetic)
    check("kinetic source says c_t = c_s is supplied rather than derived", "`c_t = c_s` is supplied rather than derived" in kinetic)
    check(
        "kinetic source lists scale reference among structures not used as a derivation",
        "scale reference, and records' causal order" in kinetic
        and "are not used here as a derivation of that equality" in kinetic,
    )
    check("realized source says laws do not pick state", "The laws do not pick the state; the world does" in realized)
    check("realized source says pointwise evaluation only", "Derivations may evaluate at the realized state, pointwise." in realized)
    check("realized source forbids state-selection content", "It does not supply a state, state-selection rule" in realized)
    print()

    print("Kinetic route checks")
    check("kinetic support states current structures do not determine xi", "do not determine the\ndimensionless kinetic ratio `xi := c_t / c_s`" in kinetic_support)
    check("kinetic support leaves future retained dynamics route open", has(kinetic_support, "a future retained dynamics could derive the same kinetic isotropy and retire the primitive"))
    check("B4 no-go says transitivity route is circular", "Circularity certificate" in kinetic_b4 and "vanishes exactly when `c_t = c_s`" in kinetic_b4)
    check("B4 no-go preserves primitive", "The approved primitive is unchanged and not retired here." in kinetic_b4)
    check("B-W no-go requires a separate normalization rule", "derive the B-W readout/normalization rule `E_E(k)=|omega(k)|`" in kinetic_bw)
    check("composition note names single-tick placement residual", "single-tick normalization-placement reading is not derived" in kinetic_composition)
    print()

    print("Ledger classification checks")
    for claim_id in expected:
        row = ledger_rows.get(claim_id, {})
        check(f"ledger row exists for {claim_id}", bool(row))
        check(f"{claim_id} is meta effective status", row.get("effective_status") == "meta", str(row.get("effective_status")))
        check(f"{claim_id} is not a retained theorem", row.get("claim_type") == "meta", str(row.get("claim_type")))
    print()

    print("Review-note conclusion checks")
    check("review note states no primitive is presently retireable", "No primitive is presently retireable" in note)
    check("review note uses canonical meta claim type", "**Claim type:** meta" in note and "**Type:** meta" in note)
    check("review note keeps scale primitive", "`scale_reference_primitive` | keep" in note)
    check("review note keeps kinetic primitive but marks it targetable", "`kinetic_isotropy_primitive` | keep, but targetable" in note)
    check("review note keeps realized-state primitive", "`realized_state_primitive` | keep" in note)
    check("review note forbids registry edit from this review", "No registry edit is warranted" in note)
    check("review note records kinetic bridge stack needed for retirement", "the B-W/OS0 readout rule" in note and "single-tick kernel" in note)
    check(
        "review note records completed hygiene repairs without science reclassification",
        "Hygiene Repairs Verified On 2026-07-10" in note
        and "completed hygiene repairs are not retirement evidence" in note,
    )
    check("review note has current-main posture line", "Current-main posture (2026-07-11)" in note)
    check("review note records the sole foundation", "sole\n  axiom/approved-primitive foundation" in note)
    check("review note records absence of an admission registry", "absence of an admission registry" in note)
    for idx in range(1, 9):
        check(f"review note carries N{idx} no-go-discipline section", f"**N{idx}" in note)
    check("N1 records at least five attempted routes", note.count("`ATTEMPTED`") >= 5)
    check("N2 records the collapsed pairwise independence table", "closing first closes second?" in note and "dimensionful scale / kinetic-form ratio" in note)
    check("N3 classifies registered and supplied phrase hits", "cited machine-registry authority" in note and "cited primitive-source boundary" in note)
    check("N4 distinguishes exact, support-only, and partial residual matches", "support-only witness" in note and "route map only, not a witness" in note)
    print()

    print("Hygiene diagnostic checks")
    stale_count_check = "historical registry genuine count remains two" in scale_runner
    current_count_check = "note rejects an admission registry" in scale_runner
    check(
        "scale boundary runner rejects an admission registry",
        current_count_check and not stale_count_check,
    )
    old_baseline_refs = [
        p.name for p, text in [(SCALE, scale), (KINETIC, kinetic), (REALIZED, realized)]
        if re.search(r"three named axioms|Lattice \+ Quantum \+ Record|MINIMAL_AXIOMS_2026-06-0[45]", text)
    ]
    check("primitive source notes carry no pre-reset baseline narrative", not old_baseline_refs, ", ".join(old_baseline_refs))
    print()

    print("Verdicts")
    print("  scale_reference_primitive: KEEP -- no dimensionful derivation from current axioms")
    print("  kinetic_isotropy_primitive: KEEP -- best future retirement lane, not closed now")
    print("  realized_state_primitive: KEEP -- laws remain state-blind; no selector supplied")
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
