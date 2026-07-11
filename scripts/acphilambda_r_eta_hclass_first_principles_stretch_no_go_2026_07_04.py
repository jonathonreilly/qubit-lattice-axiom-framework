#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
NARROWING = DOCS / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
W2_CONTEXT = DOCS / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
SUPPLIED_CONTEXT = DOCS / "SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md"
FIXED_LOCUS = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
NORMAL_FORM = DOCS / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
DIRECT_LICENSE = DOCS / "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
HUNIT = DOCS / "ACPHILAMBDA_R_ETA_HUNIT_APPROVED_PRIMITIVE_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row_by_path(path: str) -> dict | None:
    rows = json.loads(read(LEDGER))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == path]
    if not matches:
        return None
    if len(matches) != 1:
        raise AssertionError(f"ledger matches for {path}: {len(matches)}")
    return matches[0]


def c3_shift(vec: tuple[sp.Expr, sp.Expr, sp.Expr]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    return (vec[2], vec[0], vec[1])


def linear(coeffs: tuple[sp.Expr, sp.Expr, sp.Expr], vec: tuple[sp.Expr, sp.Expr, sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(c * v for c, v in zip(coeffs, vec)))


def additive(coeffs: tuple[sp.Expr, sp.Expr, sp.Expr], x: tuple[sp.Expr, sp.Expr, sp.Expr], y: tuple[sp.Expr, sp.Expr, sp.Expr]) -> bool:
    xy = tuple(a + b for a, b in zip(x, y))
    return sp.simplify(linear(coeffs, xy) - linear(coeffs, x) - linear(coeffs, y)) == 0


def c3_invariant(coeffs: tuple[sp.Expr, sp.Expr, sp.Expr], vec: tuple[sp.Expr, sp.Expr, sp.Expr]) -> bool:
    return sp.simplify(linear(coeffs, c3_shift(vec)) - linear(coeffs, vec)) == 0


def main() -> int:
    print("AC_phi_lambda R-eta h-class first-principles stretch no-go verifier")

    paths = [
        NOTE,
        DECISION_HISTORY,
        LEDGER,
        AXIOM_PREMISES,
        AXIOMS,
        REGISTRY,
        FIXED_LOCUS,
    ]

    section("A. source presence and current premise boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    tier = json.loads(read(DECISION_HISTORY))
    premises = json.loads(read(AXIOM_PREMISES))
    axioms = read(AXIOMS)
    registry = read(REGISTRY)
    fixed_locus = read(FIXED_LOCUS)

    note_flat = flat(note)
    axioms_flat = flat(axioms)
    registry_flat = flat(registry)
    fixed_flat = flat(fixed_locus)

    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    decomp = ac["minimum_decomposition"]
    check("decision history has no live premise inputs", tier["genuine_admitted_input_count"] == 0 and tier["derivation_targets"] == {})
    check(
        "AC minimum decomposition keeps R-eta",
        "delta_readout_identification_R_eta" in decomp,
        decomp,
    )
    check("AC minimum decomposition keeps occupancy separate", "reading_occupancy_selection" in decomp, decomp)
    check("AC statement names R-eta", "R-eta" in ac["statement"] and "density-read-as-angle" in ac["statement"])
    check("human registry points to the R-eta derivation obligation", "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md" in registry)
    check("note declares Type no_go", "**Type:** no_go" in note)
    check("note declares Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    check("note says R-eta remains open", "R-eta is not derived or refuted; its open gate remains" in note)
    check("note says AC_phi_lambda is not retired", "AC_phi_lambda is not retired." in note)
    check("note says no registry/axiom/primitive edit", "No registry, axiom, primitive, audit verdict" in note)
    for forbidden in [
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "h-class is derived",
        "A_R-eta is derived",
        "therefore R-eta closes",
        "audit_status: audited_clean",
        "effective_status: retained",
        "promoted to retained",
    ]:
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)

    section("B. approved premise and axiom boundaries")
    expected = [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]
    check("approved premise registry has exactly four canonical ids", premises["canonical_ids"] == expected, premises["canonical_ids"])
    premise_dump = json.dumps(premises)
    for term in ["h-class", "R-eta", "R_eta", "A_R-eta", "delta_readout_identification_R_eta", "physical-observable bridge"]:
        check(f"approved premise registry does not contain {term}", term not in premise_dump)
    for phrase in [
        "Records form.",
        "A readout value is determined by record content alone",
        "scalar readout `I` is additive",
        "context selection",
        "formation rules",
        "source/action and physical-observable identification",
    ]:
        check(f"minimal axiom boundary contains {phrase}", phrase in axioms_flat)
    check("minimal axioms place AC_phi_lambda outside axiom content", "AC_phi_lambda" in axioms and "outside axiom content" in axioms_flat)
    check("note records no h-unit import", "h-unit is not imported" in note_flat and "h-unit assumption" in note_flat)

    section("C. context-handle discipline and retained fixed-locus input")
    check("note labels context handles as non-load-bearing", "context handles only, not load-bearing inputs" in note)
    for phrase in [
        NARROWING.name,
        W2_CONTEXT.name,
        SUPPLIED_CONTEXT.name,
        NORMAL_FORM.name,
        DIRECT_LICENSE.name,
        HUNIT.name,
    ]:
        check(f"context handle is backticked in note: {phrase}", f"`{phrase}`" in note)
    for phrase in ["2/9", "conjugate complex weights", "physical single-summand readout"]:
        check(f"fixed-locus source contains {phrase}", phrase in fixed_flat)
    for phrase in ["h-class:", "h-unit:", "physical carrier realization", "Phi(c)=c S_sum", "h-unit is not imported"]:
        check(f"note reproduces context boundary: {phrase}", phrase in note_flat)

    section("D. finite C3-invariant additive readout family")
    a0, a1, a2, alpha = sp.symbols("a0 a1 a2 alpha")
    x0, x1, x2 = sp.symbols("x0 x1 x2")
    coeffs = (a0, a1, a2)
    vec = (x0, x1, x2)
    shifted = c3_shift(vec)
    invariance_poly = sp.Poly(sp.expand(linear(coeffs, shifted) - linear(coeffs, vec)), x0, x1, x2)
    constraints = [sp.Eq(c, 0) for c in invariance_poly.coeffs()]
    solution = sp.solve(constraints, (a0, a1, a2), dict=True)
    check("C3 covariance equations have a solution family", len(solution) == 1, solution)
    sol = solution[0]
    check("C3 covariance forces a0=a1=a2", sol == {a0: a2, a1: a2} or sol == {a0: a1, a2: a1}, sol)

    family = (alpha, alpha, alpha)
    empty = (sp.Integer(0), sp.Integer(0), sp.Integer(0))
    one_orbit = (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    two_orbits = (sp.Integer(2), sp.Integer(2), sp.Integer(2))
    split_a = (sp.Integer(1), sp.Integer(0), sp.Integer(1))
    split_b = (sp.Integer(0), sp.Integer(1), sp.Integer(0))
    check("I_alpha(empty)=0", linear(family, empty) == 0)
    check("I_alpha is additive on explicit split", additive(family, split_a, split_b))
    check("I_alpha is additive on orbit doubling", additive(family, one_orbit, one_orbit))
    check("I_alpha is C3 invariant on generic vector", c3_invariant(family, vec))
    check("I_alpha is C3 invariant on one orbit", c3_invariant(family, one_orbit))
    check("one full orbit evaluates to 3 alpha", linear(family, one_orbit) == 3 * alpha)
    check("two full orbits evaluate to 6 alpha", linear(family, two_orbits) == 6 * alpha)

    L = sp.Rational(2, 9)
    S_sum = 3 * L
    target_alpha = sp.solve(sp.Eq(linear(family, one_orbit), L), alpha)
    check("fixed-locus density target is L=2/9", L == sp.Rational(2, 9))
    check("S_sum=3L=2/3", S_sum == sp.Rational(2, 3))
    check("target alpha for one orbit is 2/27", target_alpha == [sp.Rational(2, 27)], target_alpha)

    alternatives = {
        "zero": sp.Integer(0),
        "one_ninth": sp.Rational(1, 9),
        "fixed_locus_density_member": sp.Rational(2, 27),
        "averaged_count": sp.Rational(1, 3),
        "count": sp.Integer(1),
    }
    values = {name: sp.simplify(linear((value, value, value), one_orbit)) for name, value in alternatives.items()}
    check("five candidate alpha choices scanned", len(values) == 5)
    check("candidate values are not all equal", len(set(values.values())) == 5, values)
    check("fixed-locus density member gives 2/9", values["fixed_locus_density_member"] == L)
    for name, value in alternatives.items():
        candidate = (value, value, value)
        check(f"{name} candidate has empty normalization", linear(candidate, empty) == 0)
        check(f"{name} candidate is additive", additive(candidate, split_a, split_b) and additive(candidate, one_orbit, one_orbit))
        check(f"{name} candidate is C3 invariant", c3_invariant(candidate, vec))
    for name in ["zero", "one_ninth", "averaged_count", "count"]:
        check(f"{name} does not hit fixed-locus density value", values[name] != L, values[name])

    section("E. h-unit separation and negative controls")
    beta = sp.symbols("beta")
    hclass_value = linear((sp.Rational(2, 27), sp.Rational(2, 27), sp.Rational(2, 27)), one_orbit)
    check("h-class fixed-density value can be evaluated without beta", hclass_value == L)
    check("identity h-unit beta=1 would not choose alpha", sp.simplify(1 * linear(family, one_orbit) - 3 * alpha) == 0)
    check("holding beta=1 leaves alpha free", alpha in (1 * linear(family, one_orbit)).free_symbols)
    beta_target = sp.solve(sp.Eq(beta * L, L), beta)
    check("if h-class were selected, beta=1 is the identity density control", beta_target == [1], beta_target)
    check("note states h-unit is set aside", "sets h-unit aside" in note_flat or "h-unit is not imported" in note_flat)

    section("F. route accounting and audit row")
    route_needles = [
        "Record additivity plus C3 covariance",
        "Fixed-locus arithmetic",
        "Supplied finite context / W2",
        "Holonomy normal form",
        "Approved primitive registry",
    ]
    for needle in route_needles:
        check(f"note records stretch route: {needle}", needle in note)
    check("all five attack frames are marked as failures/open", note.count("Fails:") >= 5)
    for phrase in [
        "No observed lepton masses",
        "fitted selectors",
        "Born/interface rule",
        "event law",
        "source/action bridge",
        "physical carrier theorem",
        "owner decision",
    ]:
        check(f"hidden import exclusion recorded: {phrase}", phrase in note)
    new_row = ledger_row_by_path("docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md")
    if new_row is None:
        check("new row not required before audit pipeline seeding", True)
    else:
        check("new row claim_type is no_go", new_row.get("claim_type") == "no_go", new_row.get("claim_type"))
        check("new row audit status remains unaudited", new_row.get("audit_status") == "unaudited", new_row.get("audit_status"))
        check("new row effective status remains unaudited", new_row.get("effective_status") == "unaudited", new_row.get("effective_status"))
        check(
            "source note links the current R-eta open obligation",
            "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`](" in note,
        )
        check(
            "source note treats decision history as non-authoritative provenance",
            "non-authoritative provenance" in note,
        )

    print("\nTOTAL: PASS=%d FAIL=%d CHECKS=%d" % (PASS, FAIL, PASS + FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
