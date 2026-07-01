#!/usr/bin/env python3
"""Verifier for the AC_phi_lambda C3 readout unit normal form."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def l3(a: int, b: int) -> Fraction:
    pair = (a % 3, b % 3)
    if pair in {(1, 2), (2, 1)}:
        return Fraction(2, 9)
    if pair in {(1, 1), (2, 2)}:
        return Fraction(1, 9)
    raise ValueError(pair)


def readout(c: Fraction, count: int, density: Fraction) -> Fraction:
    return c * count * density


def shifted_readout(c: Fraction, shift: Fraction, count: int, density: Fraction) -> Fraction:
    if count == 0:
        return Fraction(0)
    return c * count * density + shift


def quadratic_readout(c: Fraction, q: Fraction, count: int, density: Fraction) -> Fraction:
    return c * count * density + q * count * (count - 1)


def main() -> int:
    print("=== AC_phi_lambda C3-covariant readout unit normal form ===")

    files = [
        "docs/ACPHILAMBDA_C3_COVARIANT_READOUT_UNIT_NORMAL_FORM_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md",
        "docs/PHYSICAL_READOUT_SELECTION_INDEPENDENCE_2026-07-01.md",
        "docs/ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md",
        "docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/ACPHILAMBDA_C3_COVARIANT_READOUT_UNIT_NORMAL_FORM_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    phase = read("docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md")
    independence = read("docs/PHYSICAL_READOUT_SELECTION_INDEPENDENCE_2026-07-01.md")
    edge = read("docs/ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md")
    scalar = read("docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no axiom or registry edits", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    flat_axioms = flat(axioms)
    check("axioms supply finite additive record readout", "finite collection of pairwise-disjoint records" in flat_axioms and "I(empty)=0" in flat_axioms)
    check("axioms do not supply physical observable bridge", "physical observable bridge" in axioms)
    check("phase note has direct readout implication", "direct local scalar readout" in phase and "|delta| = L3(1,2) = 2/9" in phase)
    check("independence note keeps readout selector open", "W_defect_readout_selection" in independence)
    check("edge note localizes selected C3 defect", "selected edge-minimal C3 generation context" in edge and "L3(1,2) = 2/9" in edge)

    print("\nPART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    check("no registered P_readout_selection", "P_readout_selection" not in registry_text)
    check("minimal axioms registry excludes physical observable bridge", "physical observable bridge" in registry["nodes"]["minimal_axioms"]["note"])
    check("minimal axioms registry excludes weighting/normalization", "weighting" in registry["nodes"]["minimal_axioms"]["note"] and "normalization" in registry["nodes"]["minimal_axioms"]["note"])

    print("\nPART C -- selected C3 arithmetic")
    selected = l3(1, 2)
    selected_reverse = l3(2, 1)
    contrast_11 = l3(1, 1)
    contrast_22 = l3(2, 2)
    check("selected pair gives 2/9", selected == Fraction(2, 9), selected)
    check("selected pair is order-independent", selected_reverse == selected, selected_reverse)
    check("equal-weight contrasts give 1/9", contrast_11 == contrast_22 == Fraction(1, 9), (contrast_11, contrast_22))
    check("selected density is nonzero", selected != 0)
    check("contrast differs from selected density", contrast_11 != selected)

    print("\nPART D -- additive unit family")
    units = [Fraction(1), Fraction(1, 2), Fraction(2), Fraction(-1)]
    for c in units:
        check(f"unit {c} has empty readout zero", readout(c, 0, selected) == 0)
        check(
            f"unit {c} is additive over disjoint counts",
            readout(c, 2, selected) + readout(c, 3, selected) == readout(c, 5, selected),
            (readout(c, 2, selected), readout(c, 3, selected), readout(c, 5, selected)),
        )
    check("identity unit gives 2/9 singleton", readout(Fraction(1), 1, selected) == Fraction(2, 9))
    check("half unit gives 1/9 singleton on selected line", readout(Fraction(1, 2), 1, selected) == Fraction(1, 9))
    check("double unit gives 4/9 singleton", readout(Fraction(2), 1, selected) == Fraction(4, 9))
    singleton_value = Fraction(5, 9)
    c_from_singleton = singleton_value / selected
    check("any singleton value determines c", c_from_singleton == Fraction(5, 2), c_from_singleton)
    check("reconstructed singleton from c matches", readout(c_from_singleton, 1, selected) == singleton_value)
    check("collection readout is count times singleton", readout(c_from_singleton, 4, selected) == 4 * singleton_value)

    print("\nPART E -- non-additive contrasts are rejected by additivity")
    c = Fraction(1)
    shift = Fraction(1, 7)
    q = Fraction(1, 5)
    shifted_ok = shifted_readout(c, shift, 1, selected) + shifted_readout(c, shift, 1, selected) == shifted_readout(c, shift, 2, selected)
    quadratic_ok = quadratic_readout(c, q, 1, selected) + quadratic_readout(c, q, 1, selected) == quadratic_readout(c, q, 2, selected)
    check("nonzero shifted nonempty readout fails additivity", not shifted_ok)
    check("quadratic count correction fails additivity", not quadratic_ok)
    check("linear unit family survives these guards", readout(c, 1, selected) + readout(c, 1, selected) == readout(c, 2, selected))

    print("\nPART F -- note content")
    check("note states one-parameter normal form", "I_c(R) = c * |R| * L" in note)
    check("note identifies W_defect_identity_unit", "W_defect_identity_unit" in note)
    check("note says c=1 is not derived", "does not derive `c = 1`" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note gives sharpened primitive target", "physical phase readout selects the identity unit c=1" in flat_note)
    check("phase note and new note agree on direct value", "|delta| = 2/9" in note and "|delta| = 2/9" in phase)
    check("scalar no-go supports singleton selector boundary", "Record additivity alone" in scalar and "branch-to-scalar map" in scalar)
    check("primitive recommendation supports P_readout_selection fallback", "P_readout_selection" in primitive)

    print("\nPART G -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    for route in [
        "C3 arithmetic route",
        "Record-additivity route",
        "C3-covariant local scalar route",
        "Direct-unit route",
        "Source/action or eta route",
        "New primitive route",
    ]:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed residual is W_defect_identity_unit", "W_defect_identity_unit." in note)
    check("N3 classifies identity unit as missing selector", "| `identity unit` | The missing physical readout selector" in note)
    check("N4 residual table includes phase normal form", "ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM" in note)
    check("N5 narrows resolution", "finite singleton-record and finite disjoint-record resolution" in flat_note)
    check("N6 lists source/action, eta, and instrument routes", "source/action theorem" in note and "eta/holonomy theorem" in note and "instrument readout theorem" in note)
    check("N7 steelman preserves non-direct route", "different scalar surface" in flat_note)
    check("N8 cross-cycle echo separates context, scalar line, unit", "which carrier/context is selected" in flat_note and "which unit maps that line" in flat_note)

    print("\nPART H -- non-overclaim checks")
    overclaims = [
        "therefore AC_phi_lambda is closed",
        "therefore c = 1 is derived",
        "therefore non-direct readout contexts are impossible",
        "therefore a new ontology axiom is required",
        "therefore source/action routes fail",
        "therefore probability gates are closed",
    ]
    for phrase in overclaims:
        check(f"note avoids overclaim assertion: {phrase}", phrase not in flat_note)
    check("note has explicit non-claims section", "## Non-Claims" in note and "This note does not claim:" in note)
    check("non-claims preserve no AC closure", "- `AC_phi_lambda` is closed;" in note)
    check("non-claims preserve no c=1 derivation", "- the identity unit `c = 1` is derived from the ontology axioms;" in note)
    check("non-claims preserve future routes", "future source/action, eta, holonomy" in note)
    check("note says not terminal no-go", "not a terminal no-go against deriving the identity unit" in flat_note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
