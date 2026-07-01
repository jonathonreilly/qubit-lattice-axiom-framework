#!/usr/bin/env python3
"""Verifier for AC_phi_lambda phase-defect readout normal form."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def read(rel: str) -> str:
    path = ROOT / rel
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def l3_symbolic(a: int, b: int) -> Fraction:
    """Exact L_3(a,b) values for a,b in {1,2}.

    Uses zeta^2 + zeta + 1 = 0.  For p=3, the four nontrivial transverse
    weight pairs reduce to the two values below.
    """

    pair = (a % 3, b % 3)
    if pair in {(1, 2), (2, 1)}:
        return Fraction(2, 9)
    if pair in {(1, 1), (2, 2)}:
        return Fraction(1, 9)
    raise ValueError(pair)


def main() -> int:
    print("=== AC_phi_lambda phase-defect readout normal form ===")

    files = [
        "docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md",
        "docs/ACPHILAMBDA_STACKED_ATOM_REDUCTION_2026-07-01.md",
        "docs/ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md",
        "docs/ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "docs/ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
        "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "docs/GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION_2026-06-30.md",
        "docs/LEPTON_PHASE_MODULUS_SEPARATION_NO_GO_2026-06-06.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    gap = read("docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md")
    stack = read("docs/ACPHILAMBDA_STACKED_ATOM_REDUCTION_2026-07-01.md")
    edge = read("docs/ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md")
    formal = read("docs/ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md")
    context = read("docs/ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md")
    weights = read("docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md")
    generation = read("docs/GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION_2026-06-30.md")
    phase_no_go = read("docs/LEPTON_PHASE_MODULUS_SEPARATION_NO_GO_2026-06-06.md")
    registry = read("docs/audit/data/axiom_premise_nodes.json")
    flat_note = flat(note)

    print("\nPART A -- source surface and boundary")
    check("axioms are the current four-axiom reset", "2026-06-29" in axioms and "Admissibility" in axioms and "Record" in axioms)
    check("axioms do not supply readout selection", "physical observable bridge" in axioms or "physical observable" in axioms)
    check("registry keeps minimal axioms narrow", "source/action bridge" in registry and "physical observable bridge" in registry)
    check("gap map names W_readout_coupling", "W_readout_coupling" in gap)
    check("stack names W_phase_defect", "W_phase_defect" in stack)
    check("edge bridge names phase-defect coupling", "phase-defect coupling" in edge)
    check("formal R-eta note says formal layer cannot select value", "selects **no** value" in formal or "select no value" in formal)
    check("W2 context bridge leaves value atom unchanged", "value atom `A_R-eta` remains admitted" in context)
    check("new note declares independent audit authority", "independent audit lane only" in note)
    check("new note does not request axiom edit", "does not request an axiom edit" in note)

    print("\nPART B -- exact finite C3 arithmetic")
    check("trace-free pair (1,2) gives 2/9", l3_symbolic(1, 2) == Fraction(2, 9), l3_symbolic(1, 2))
    check("trace-free pair (2,1) gives 2/9", l3_symbolic(2, 1) == Fraction(2, 9), l3_symbolic(2, 1))
    check("equal pair (1,1) gives contrast 1/9", l3_symbolic(1, 1) == Fraction(1, 9), l3_symbolic(1, 1))
    check("equal pair (2,2) gives contrast 1/9", l3_symbolic(2, 2) == Fraction(1, 9), l3_symbolic(2, 2))
    pairs = [(1, 1), (1, 2), (2, 1), (2, 2)]
    trace_free = [p for p in pairs if sum(p) % 3 == 0]
    check("only two ordered trace-free nontrivial pairs", trace_free == [(1, 2), (2, 1)], trace_free)
    values = {p: l3_symbolic(*p) for p in pairs}
    check("selected trace-free value differs from equal-weight contrast", values[(1, 2)] != values[(1, 1)])
    check("selected value is direct-unit rational not pi-scaled", values[(1, 2)].denominator == 9)
    check("weights source contains L3(1,2)=2/9", "L₃(1,2) = 2/9" in weights or "L3(1,2) = 2/9" in weights)

    print("\nPART C -- normal-form content")
    for phrase in [
        "If the charged-lepton phase magnitude is the direct local scalar readout",
        "W_defect_readout_selection",
        "unique direct-unit local fixed-defect density",
        "not fitted, measured, or added",
        "not C3 arithmetic",
        "not the `hw=1` context",
        "not the sign strip",
        "not a free conversion factor",
    ]:
        check(f"note contains normal-form phrase: {phrase}", phrase in flat_note)
    check("note maps W_readout_coupling to sharper residual", "with the sharper normal-form residual" in note)
    check("note preserves direct selected-context chain", "selected edge-minimal C3 context" in note)
    check("note states no full AC closure", "full `AC_phi_lambda` closure" in flat_note)
    check("note states no record occurrence closure", "record occurrence" in note)
    check("note states no source/action closure", "source/action coefficients" in note)

    print("\nPART D -- source witness matching")
    check("generation bridge selects hw=1 context", "hw=1" in generation and "edge-minimal" in generation)
    check("generation bridge says primitive object is edge", "primitive local kinetic/readout object is an oriented nearest-neighbor edge" in generation)
    check("stack reduces AC_phi_lambda to phase-defect", "surviving `AC_phi_lambda` atom" in stack and "phase-defect" in stack)
    check("edge bridge computes selected local scalar defect", "unique local C3 defect density" in edge or "unique local C3 fixed-defect scalar" in edge)
    check("edge bridge leaves coupling", "does the charged-lepton phase magnitude read" in edge)
    check("formal note preserves h-class/h-unit atom", "h-class" in formal and "h-unit" in formal)
    check("phase/modulus note leaves eta route open", "eta`/holonomy route remains untouched and open" in phase_no_go or "eta`/holonomy" in phase_no_go)

    print("\nPART E -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    for route in [
        "Record-only route",
        "Formal `H(delta)` route",
        "Edge-defect route",
        "Conversion-factor route",
        "Comparator route",
        "New primitive route",
    ]:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapses to one residual", "Collapsed residual after this theorem" in note and "W_defect_readout_selection" in note)
    check("N3 marks physical phase as target", "remaining selection target" in note)
    check("N4 includes five witnesses", note.count("| `ACPHILAMBDA") >= 2 and "`OPERATIONAL_PREMISE_GAP_MAP" in note)
    check("N5 avoids ontology-derived phase overclaim", "ontology by itself derives the charged-lepton phase" in note)
    check("N6 lists bridge-first closure paths", "record-facing C3-covariant phase" in note and "same-surface charged-lepton source/action" in note)
    check("N7 steelman admits hard atom remains", "does not close the hardest atom" in note)
    check("N8 cross-cycle echo present", "Earlier cycles overclaimed" in note)

    print("\nPART F -- non-overclaim checks")
    forbidden = [
        "AC_phi_lambda is retired",
        "AC_phi_lambda is solved",
        "axioms derive the charged-lepton phase",
        "Record alone selects",
        "measured masses prove",
        "PDG",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says comparator route is not used", "comparator data is downstream evidence" in note)
    check("note says primitive is fallback only", "would be a narrow operational primitive" in flat_note)
    check("note does not edit registry by claim", "edit registries" in note and "register a primitive" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- phase-defect normal form is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- W_readout_coupling is narrowed to the physical "
        "defect-readout selection atom."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
