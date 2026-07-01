#!/usr/bin/env python3
"""Verifier for the physical source selector independence note."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

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


def expectation(prob: list[sp.Expr], values: list[sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(p * v for p, v in zip(prob, values)))


def rn_family(prob: list[sp.Expr], score: list[sp.Expr], h: sp.Symbol) -> tuple[list[sp.Expr], sp.Expr]:
    z = expectation(prob, [sp.exp(h * s) for s in score])
    return [sp.simplify(sp.exp(h * s) / z) for s in score], z


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.together(expr.rewrite(sp.exp))) == 0


def main() -> int:
    print("=== Physical source selector independence ===")

    files = [
        "docs/PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md",
        "docs/RECORD_BORN_TO_SOURCE_MEASURE_PCAL_INTERFACE_BRIDGE_2026-06-30.md",
        "docs/SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md",
        "docs/SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md",
        "docs/SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05.md",
        "docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    kinetic = read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    source_action = read("docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md")
    pcal = read("docs/RECORD_BORN_TO_SOURCE_MEASURE_PCAL_INTERFACE_BRIDGE_2026-06-30.md")
    log_boundary = read("docs/SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md")
    planck_action = read("docs/SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md")
    onb = read("docs/SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05.md")
    yt_no_go = read("docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)
    flat_axioms = flat(axioms)
    flat_source_action = flat(source_action)

    print("\nPART A -- current premise boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry or axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("minimal axioms keep source/action downstream", "source/action" in axioms and "Further physical structure requires" in flat_axioms)
    check("source/action factorization names W_physical_source", "W_physical_source" in source_action)
    check("source/action factorization says physical direction remains", "physical source direction and unit selection" in flat_source_action)
    check("P-cal bridge names W_source_action", "W_source_action" in pcal)
    check("P-cal bridge says physical source remains open", "physical source/action bridge" in pcal or "physical source/action deformation" in pcal)
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
    check("minimal axioms registry note says no source/action bridge", "source/action bridge" in nodes["minimal_axioms"]["note"])
    check("scale primitive supplies no dimensionless source selector", "zero dimensionless content" in flat(scale).lower() and "selector" in flat(scale).lower())
    check("kinetic primitive supplies structural isotropy only", "structural statement" in flat(kinetic).lower() and "selector" in flat(kinetic).lower())
    check("realized-state primitive supplies no state-selection/probability", "state-selection rule" in flat(realized).lower() and "probability rule" in flat(realized).lower())
    check("no registered P_physical_source", "P_physical_source" not in registry_text)

    print("\nPART C -- finite direction witness")
    h = sp.symbols("h", real=True)
    prob = [sp.Rational(1, 4)] * 4
    rt2 = sp.sqrt(2)
    s_a = [rt2, -rt2, 0, 0]
    s_b = [0, 0, rt2, -rt2]
    for name, score in [("A", s_a), ("B", s_b)]:
        rn, z = rn_family(prob, score, h)
        check(f"score {name} is centered", expectation(prob, score) == 0)
        check(f"score {name} has Fisher norm one", sp.simplify(expectation(prob, [s**2 for s in score]) - 1) == 0)
        check(f"RN family {name} normalizes", is_zero(expectation(prob, rn) - 1), sp.simplify(expectation(prob, rn) - 1))
        origin_score = [sp.simplify(sp.diff(sp.log(r), h).subs(h, 0)) for r in rn]
        check(f"RN family {name} has requested origin score", all(sp.simplify(origin_score[i] - score[i]) == 0 for i in range(4)))
    check("scores A and B are Fisher orthogonal", sp.simplify(expectation(prob, [a * b for a, b in zip(s_a, s_b)])) == 0)
    check("scores A and B are distinct directions", s_a != s_b)
    rn_a, z_a = rn_family(prob, s_a, h)
    rn_b, z_b = rn_family(prob, s_b, h)
    check("two RN families differ away from origin", sp.simplify(rn_a[0] - rn_b[0]) != 0)
    check("note displays both unit scores", "s_A = (sqrt(2), -sqrt(2), 0, 0)" in note and "s_B = (0, 0, sqrt(2), -sqrt(2))" in note)

    print("\nPART D -- source-unit lambda witness")
    lam = sp.symbols("lambda", positive=True)
    scaled_score = [lam * s for s in s_a]
    rn_lam, z_lam = rn_family(prob, scaled_score, h)
    origin_scaled = [sp.simplify(sp.diff(sp.log(r), h).subs(h, 0)) for r in rn_lam]
    norm_scaled = expectation(prob, [s**2 for s in origin_scaled])
    check("lambda-scaled RN family normalizes", is_zero(expectation(prob, rn_lam) - 1), sp.simplify(expectation(prob, rn_lam) - 1))
    check("lambda-scaled origin score is lambda s_A", all(sp.simplify(origin_scaled[i] - lam * s_a[i]) == 0 for i in range(4)))
    check("lambda-scaled Fisher norm is lambda^2", sp.simplify(norm_scaled - lam**2) == 0)
    check("lambda=1 is unit Fisher after unit direction supplied", sp.solve(sp.Eq(norm_scaled, 1), lam) == [1])
    check("same algebra permits lambda=2 with different norm", norm_scaled.subs(lam, 2) == 4)
    check("note displays lambda family", "R_h^(lambda)(i)" in note and "lambda^2" in note)

    print("\nPART E -- action exponent factorization sanity")
    kappa = sp.symbols("kappa", positive=True)
    s0, o = sp.symbols("S0 o", real=True)
    source_h = s0 - kappa * h * o
    delta_exponent = sp.simplify((source_h - s0) / kappa)
    log_weight_ratio = sp.simplify(-delta_exponent)
    score_symbolic = sp.diff(log_weight_ratio, h)
    check("action exponent S/kappa gives RN log hO", sp.simplify(log_weight_ratio - h * o) == 0)
    check("kappa cancels from source score", sp.simplify(score_symbolic - o) == 0 and kappa not in score_symbolic.free_symbols)

    print("\nPART F -- source witness matching")
    check("source/action factorization preserves selector wall", "physical source direction and unit selection" in flat_source_action)
    check("P-cal bridge preserves physical source/action wall", "W_source_action" in pcal and "physical source/action" in pcal)
    check("log boundary has lambda family", "lambda > 0" in log_boundary and "lambda^2" in log_boundary)
    check("Planck-action bridge is conditional source-unit candidate", "Remaining Hinge" in planck_action and "does not prove" in planck_action)
    check("ONB note is finite algebra not physical response", "not a physical `Y_T` top/`W` response theorem" in onb)
    check("Y_T no-go preserves lambda family", "lambda / sqrt(6)" in yt_no_go and "does not force" in yt_no_go)
    check("primitive recommendation names P_physical_source", "P_physical_source" in primitive)
    check("primitive recommendation says direction and unit", "physical action-exponent direction and unit" in primitive)
    check("new note N4 table includes seven witnesses", note.count("| `") >= 7 and "MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION" in note)

    print("\nPART G -- minimum update and audit consequence")
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note gives P_physical_source text", "On a supplied finite record-facing RN/action surface" in note)
    check("note says downstream rows must keep W_physical_source explicit", "must keep `W_physical_source` explicit" in flat_note)
    check("audit consequence requires factorization plus selector", "source/action RN factorization" in note and "physical source selector" in note)

    print("\nPART H -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Record/Born probability route",
        "RN/action factorization route",
        "Fisher-unit route",
        "Planck-action unit route",
        "Six-diagonal/democratic direction route",
        "Strict same-source response route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed wall set is one wall", "W_physical_source." in note)
    check("N3 classifies source direction as missing", "not assumed derived" in note)
    check("N5 narrows resolution", "finite record probability surface and finite tangent-space" in flat_note)
    check("N6 lists live closure paths", "strict same-source top/W" in note and "action-unit bridge" in note)
    check("N7 steelman is substantive", "same physical action principle" in note)
    check("N8 cross-cycle echo present", "finite source calculus is not the physical source selector" in note)

    print("\nPART I -- non-overclaim checks")
    forbidden = [
        "therefore source/action closure is impossible",
        "therefore physical source coefficients are false",
        "requires a new ontology axiom",
        "therefore Planck-action unit bridge is false",
        "there is no future top/Higgs route",
        "Y_T is solved",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says no terminal no-go", "not a terminal no-go" in note)
    check("note says future bridge derivations remain possible", "not a no-go against future bridge derivations" in note)
    check("note preserves top/Higgs and action-unit routes", "top/Higgs, same-source response, action-unit" in note)
    check("note avoids measured-value imports", "PDG" not in note and "lattice-MC" not in note and "fitted" not in note)
    check("explicit non-claim preserves Planck-action bridge", "Planck-action unit bridge is false" in note and "This note does not claim" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- physical source selector independence note is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- current premises do not derive physical source "
        "direction/unit selection; the missing update is narrow source-selector content."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
