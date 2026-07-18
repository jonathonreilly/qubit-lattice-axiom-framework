#!/usr/bin/env python3
"""Exact finite witnesses for the collapsed foundation-atom ledger.

The checks establish only interface non-entailment.  They do not prove that a
single deeper lattice law cannot jointly close the atoms.
"""

from __future__ import annotations

from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "FOUNDATION_ATOM_LEDGER_AND_DEPENDENCY_MAP_NOTE_2026-07-13.md"
AXIOM = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PAULIS = (I2, X, Y, Z)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def probability(rho: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(rho * effect))


def source_contract() -> None:
    section("A - Authority and atom contract")
    axiom = " ".join(AXIOM.read_text().split())
    note_raw = NOTE.read_text()
    note = " ".join(note_raw.lower().replace("**", "").split())
    registry = json.loads(REGISTRY.read_text())

    check("A live foundation still has four axiom blocks", all(f"### {name}" in axiom for name in ("Lattice", "Qubit", "Admissibility", "Record")))
    check("A live state definition remains record configuration", "A state is a configuration of records." in axiom)
    check("A registry has exactly four canonical premise nodes", len(registry["canonical_ids"]) == 4)
    check("A note is authority-free", "authority: none" in note)
    check("A note contains N1-N8", all(f"### N{i}" in note_raw for i in range(1, 9)))
    for atom in ("`c`", "`s`", "`l`", "`v`", "`x`", "`w`"):
        check(f"A collapsed atom present: {atom}", atom in note)
    for interface in ("`o`", "`t`", "`i`", "`g`", "`b`"):
        check(f"A downstream interface present: {interface}", interface in note)


def composition_witness() -> None:
    section("B - Composition is independent of one-site data")
    products = tuple(sp.kronecker_product(a, b) for a in PAULIS for b in PAULIS)
    ordinary_rank = sp.Matrix.hstack(*(matrix.reshape(16, 1) for matrix in products)).rank()
    duplicate_products = tuple(sp.diag(matrix, matrix) for matrix in products)
    duplicate_rank = sp.Matrix.hstack(*(matrix.reshape(64, 1) for matrix in duplicate_products)).rank()
    central = sp.diag(sp.eye(4), -sp.eye(4))
    span = sp.Matrix.hstack(*(matrix.reshape(64, 1) for matrix in duplicate_products))
    augmented = sp.Matrix.hstack(span, central.reshape(64, 1))

    check("B ordinary two-site products span M4", ordinary_rank == 16)
    check("B duplicate-sector local products retain the same rank", duplicate_rank == 16)
    matrix_units = []
    for row in range(4):
        for column in range(4):
            unit = sp.zeros(4)
            unit[row, column] = 1
            matrix_units.extend((sp.diag(unit, sp.zeros(4)), sp.diag(sp.zeros(4), unit)))
    full_duplicate_rank = sp.Matrix.hstack(*(matrix.reshape(64, 1) for matrix in matrix_units)).rank()
    check("B duplicate composite algebra has constructed complex dimension 32", full_duplicate_rank == 32)
    check("B silent central sector lies outside local-product span", augmented.rank() == duplicate_rank + 1)


def state_law_and_permanence_witnesses() -> None:
    section("C - Complete state, exact law, and permanence separate")
    rho_plus = (I2 + X) / 2
    rho_minus = (I2 - X) / 2
    p_x_plus = (I2 + X) / 2
    preparation_to_record = {
        "plus_preparation": "same_record_configuration",
        "minus_preparation": "same_record_configuration",
    }
    check(
        "C two distinct preparations map to one terminal record label",
        len(preparation_to_record) == 2
        and len(set(preparation_to_record.values())) == 1,
    )
    check("C hidden plus/minus phases have different future record statistics", probability(rho_plus, p_x_plus) == 1 and probability(rho_minus, p_x_plus) == 0)

    availability = frozenset({0, 1})
    full_support = frozenset({0, 1})
    singleton_support = frozenset({0})
    check("C one static menu admits menu-complete support", full_support == availability)
    check("C the same static menu admits incomplete physical support", singleton_support < availability)

    initial = {"x": "p"}
    append_future = {"x": "p", "z": "q"}
    migrating_future = {"y": "p", "z": "q"}
    check("C append rule preserves the exact site/content pair", append_future.get("x") == initial["x"])
    check("C migration preserves content but violates same-site permanence", "p" in migrating_future.values() and migrating_future.get("x") != "p")


def actuality_probability_and_update_witnesses() -> None:
    section("D - Actuality, weights, and operational update separate")
    support = ("branch_0", "branch_1")
    selector_a = support[0]
    selector_b = support[1]
    check("D one continuation support admits different realized selectors", selector_a != selector_b and selector_a in support and selector_b in support)

    weights_a = {"branch_0": sp.Rational(1, 2), "branch_1": sp.Rational(1, 2)}
    weights_b = {"branch_0": sp.Rational(1, 4), "branch_1": sp.Rational(3, 4)}
    check("D both candidate measures are normalized on one support", sum(weights_a.values()) == sum(weights_b.values()) == 1)
    check("D actual-member choice does not determine ensemble weights", weights_a != weights_b)

    p0 = (I2 + Z) / 2
    k_keep = p0
    k_flip = X * p0
    effect_keep = k_keep.conjugate().T * k_keep
    effect_flip = k_flip.conjugate().T * k_flip
    input_state = (I2 + X) / 2
    prob = probability(input_state, p0)
    post_keep = sp.simplify(k_keep * input_state * k_keep.conjugate().T / prob)
    post_flip = sp.simplify(k_flip * input_state * k_flip.conjugate().T / prob)
    check("D two instruments have one immediate effect", effect_keep == effect_flip == p0)
    check("D equal effects permit different future states", post_keep != post_flip)


def downstream_interface_witnesses() -> None:
    section("E - Time, matter, resource/gravity, and boundary separate")
    event_order = ("e0", "e1", "e2")
    clock_a = {event: index for index, event in enumerate(event_order)}
    clock_b = {event: 2 * index for index, event in enumerate(event_order)}
    check("E one event order admits inequivalent durations", event_order == tuple(clock_a) == tuple(clock_b) and clock_a["e2"] != clock_b["e2"])

    # Hard-core lowering operators commute across sites; Jordan-Wigner CAR
    # lowering operators anticommute.  Both have the same one-site M2 carrier
    # and occupation projectors.
    sigma_minus = sp.Matrix([[0, 1], [0, 0]])
    hard_a = sp.kronecker_product(sigma_minus, I2)
    hard_b = sp.kronecker_product(I2, sigma_minus)
    car_a = hard_a
    car_b = sp.kronecker_product(Z, sigma_minus)
    check("E hard-core cross-site lowering operators commute", hard_a * hard_b - hard_b * hard_a == sp.zeros(4))
    check("E CAR cross-site lowering operators anticommute", car_a * car_b + car_b * car_a == sp.zeros(4))
    occupation = sigma_minus.conjugate().T * sigma_minus
    check("E both readings retain the same one-site occupation projector", occupation == sp.Matrix([[0, 0], [0, 1]]))

    history = (0, 1, 2, 3)
    capacity_linear = {step: step for step in history}
    capacity_quadratic = {step: step * step for step in history}
    gravity_a = {step: sp.Rational(1, 10) * capacity_linear[step] for step in history}
    gravity_b = {step: sp.Rational(1, 5) * capacity_linear[step] for step in history}
    check("E one append history admits different capacity functionals", capacity_linear != capacity_quadratic)
    check("E one capacity history admits different response couplings", gravity_a != gravity_b)

    transition = {0: 1, 1: 0}
    initial_a = 0
    initial_b = 1
    check("E one law admits distinct boundary/initial states", transition[initial_a] != transition[initial_b])


def classification_contract() -> None:
    section("F - Constitutional classification")
    note = " ".join(NOTE.read_text().lower().replace("**", "").split())
    for marker in (
        "four candidate constitutional homes remain",
        "qubit for `c`",
        "qualification for `s`",
        "canonical law specification",
        "record for `v`",
        "not a reason to insert a selector or born rule into record",
        "no broad no-go is claimed",
    ):
        check(f"F note marker: {marker}", marker in note.replace("`pass`", "pass").replace("`fail`", "fail"))


def main() -> None:
    source_contract()
    composition_witness()
    state_law_and_permanence_witnesses()
    actuality_probability_and_update_witnesses()
    downstream_interface_witnesses()
    classification_contract()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        raise SystemExit(1)
    print("RESULT: PASS")
    print("BOUNDARY: finite interface-independence witnesses; no universal axiom need is claimed")


if __name__ == "__main__":
    main()
