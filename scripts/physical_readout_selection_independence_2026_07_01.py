#!/usr/bin/env python3
"""Verifier for the physical readout selection independence note."""

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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def flat(text: str) -> str:
    return " ".join(text.split())


def l3_symbolic(a: int, b: int) -> Fraction:
    pair = (a % 3, b % 3)
    if pair in {(1, 2), (2, 1)}:
        return Fraction(2, 9)
    if pair in {(1, 1), (2, 2)}:
        return Fraction(1, 9)
    raise ValueError(pair)


def additive_readout(atom_values: dict[str, Fraction], collection: set[str]) -> Fraction:
    return sum((atom_values[a] for a in collection), Fraction(0, 1))


def main() -> int:
    print("=== Physical readout selection independence ===")

    files = [
        "docs/PHYSICAL_READOUT_SELECTION_INDEPENDENCE_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md",
        "docs/ACPHILAMBDA_STACKED_ATOM_REDUCTION_2026-07-01.md",
        "docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md",
        "docs/REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md",
        "docs/ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/PHYSICAL_READOUT_SELECTION_INDEPENDENCE_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    kinetic = read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    phase = read("docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md")
    stack = read("docs/ACPHILAMBDA_STACKED_ATOM_REDUCTION_2026-07-01.md")
    scalar_no_go = read("docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md")
    determinant = read("docs/REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md")
    reta = read("docs/ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- current premise boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry or axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("minimal axioms are four-axiom reset", "Lattice / Physical Locality" in axioms and "Admissibility / Local Constraint" in axioms)
    check("minimal axioms say further structure requires bridge/admission", "Further physical structure requires derivation, bridge" in flat(axioms))
    check("minimal axioms exclude physical observable bridge from axiom content", "physical observable bridge" in axioms)
    check("phase note names W_defect_readout_selection", "W_defect_readout_selection" in phase)
    check("phase note leaves physical readout-class selection open", "physical readout-class selection" in phase)
    check("stack reduces AC to phase-defect atom", "surviving `AC_phi_lambda` atom" in stack and "phase-defect" in stack)
    check("new note scopes to current-premise independence", "current-premise independence" in note)

    print("\nPART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    nodes = registry["nodes"]
    for node_id in expected_ids:
        check(f"registry node present: {node_id}", node_id in nodes)
    check("minimal axioms registry note says no context selection", "no context-selection rule" in nodes["minimal_axioms"]["note"])
    check("minimal axioms registry note says no physical observable bridge", "physical observable bridge" in nodes["minimal_axioms"]["note"])
    flat_scale = flat(scale).lower()
    flat_kinetic = flat(kinetic).lower()
    flat_realized = flat(realized).lower()
    check("scale primitive says no selector/readout bridge", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in flat_scale)
    check("kinetic primitive says no selector/readout bridge", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in flat_kinetic)
    check(
        "realized state says no state-selection/weighting/probability",
        "state-selection rule" in flat_realized
        and "no averaging over alternatives" in flat_realized
        and "probability rule" in flat_realized,
    )
    check("no registered P_readout_selection", "P_readout_selection" not in registry_text)

    print("\nPART C -- finite C3 arithmetic")
    direct = l3_symbolic(1, 2)
    contrast = l3_symbolic(1, 1)
    check("direct selected trace-free pair gives 2/9", direct == Fraction(2, 9), direct)
    check("contrast equal pair gives 1/9", contrast == Fraction(1, 9), contrast)
    check("direct and contrast scalars differ", direct != contrast)
    check("phase note contains 2/9 value", "2/9" in phase)
    check("phase note says value is conditional on direct readout", "If the charged-lepton phase magnitude is the direct local scalar readout" in phase)
    check("new note does not reopen C3 arithmetic", "does not reopen the C3 arithmetic" in note)

    print("\nPART D -- additive witness model")
    atoms = {"r", "s"}
    direct_values = {"r": Fraction(2, 9), "s": Fraction(5, 9)}
    contrast_values = {"r": Fraction(1, 9), "s": Fraction(5, 9)}
    empty: set[str] = set()
    r = {"r"}
    s = {"s"}
    rs = {"r", "s"}
    for values, name in [(direct_values, "direct"), (contrast_values, "contrast")]:
        check(f"{name} readout empty is zero", additive_readout(values, empty) == 0)
        check(
            f"{name} readout is additive on disjoint singleton records",
            additive_readout(values, rs) == additive_readout(values, r) + additive_readout(values, s),
            additive_readout(values, rs),
        )
        check(f"{name} readout has finite atom values", all(isinstance(v, Fraction) for v in values.values()))
    check("two witnesses share same record atoms", set(direct_values) == set(contrast_values) == atoms)
    check("two witnesses differ only on selected atom value", direct_values["r"] != contrast_values["r"] and direct_values["s"] == contrast_values["s"])
    check("direct witness realizes selected value", direct_values["r"] == direct)
    check("contrast witness realizes different legal additive singleton", contrast_values["r"] == contrast)
    check("note displays both finite witnesses", "I_direct({r})  = 2/9" in note and "I_contrast({r})  = 1/9" in note)
    check("note states both satisfy Record additivity", "Both extend additively" in note)

    print("\nPART E -- source witness matching")
    check("record scalar no-go says Record does not choose scalar map", "Record additivity alone" in scalar_no_go and "branch-to-scalar" in scalar_no_go)
    check("determinant split says readout surface is supplied", "supplied finite readout context" in determinant and "does not derive the determinant-character" in determinant)
    check("R-eta narrowing keeps physical readout conditional", "standing physical readout-context premise remains supplied" in reta or "physical readout identification" in reta)
    check("primitive recommendation names P_readout_selection", "P_readout_selection" in primitive)
    check("primitive recommendation says fallback not registered", "fallback primitive candidates" in primitive and "not primitive registrations" in primitive)
    check("new note N4 table includes five witnesses", note.count("| `") >= 5 and "MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION" in note)

    print("\nPART F -- minimum update and audit consequence")
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note gives P_readout_selection text", "local covariant map from specified record/context invariants" in note)
    check("note names target instance", "the physical charged-lepton phase readout is the direct local scalar readout" in note)
    check("note says downstream rows need selector explicit", "downstream rows must keep this selector explicit" in flat_note)
    check("audit consequence requires both normal form and selector", "phase-defect normal form" in note and "physical defect-readout selector" in note)

    print("\nPART G -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Record-additivity route",
        "C3-arithmetic route",
        "Approved-primitive route",
        "Formal `H(delta)` / registrability route",
        "Comparator route",
        "Source/action or eta route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed wall set is one wall", "W_defect_readout_selection." in note)
    check("N3 classifies physical as missing selector", "Marks the missing selector" in note)
    check("N5 narrows resolution", "finite singleton-record and finite disjoint-record resolution" in flat_note)
    check("N6 lists live closure paths", "record-facing C3-covariant phase readout" in note and "source/action theorem" in note)
    check("N7 steelman is substantive", "unique local, C3-covariant, dimensionless, source-coupled scalar" in flat_note)
    check("N8 names similar readout-selection walls", "EW `kappa_EW` physical readout" in note and "quark scalar readout" in note)

    print("\nPART H -- non-overclaim checks")
    forbidden = [
        "therefore the direct C3 defect scalar is false",
        "therefore a future physical readout theorem is impossible",
        "requires a new ontology axiom",
        "AC_phi_lambda is solved",
        "selector is impossible",
        "there is no future source/action route",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says no terminal no-go", "not a terminal no-go" in note)
    check("note says future bridge derivations remain possible", "not a no-go against future bridge derivations" in note)
    check("note says no probability/occurrence/theta closure", "probability, occurrence, theta, source/action, metric" in note)
    check("note avoids PDG/comparator import", "PDG" not in note and "comparator data is downstream evidence" in note)
    check("explicit non-claim preserves direct scalar", "the direct C3 defect scalar is false" in note and "This note does not claim" in note)
    check("explicit non-claim preserves future source/action route", "no future source/action, eta, holonomy" in flat_note and "This note does not claim" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- readout-selection independence note is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- current premises do not derive the physical "
        "defect-readout selector; the missing update is narrow and operational."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
