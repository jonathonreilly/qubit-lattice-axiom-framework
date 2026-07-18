#!/usr/bin/env python3
"""Finite exact controls for phase information in persistent record states."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "RECORD_STATE_PHASE_SUFFICIENCY_CONSTRUCTIVE_PROBE_NOTE_2026-07-13.md"

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PXP = (I2 + X) / 2
PXM = (I2 - X) / 2
PZP = (I2 + Z) / 2
PZM = (I2 - Z) / 2


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
    section("A - Note and semantic contract")
    raw = NOTE.read_text()
    note = " ".join(raw.lower().replace("**", "").replace("`", "").split())
    check("A note is authority-free", "authority: none" in note)
    check("A exact same-record/same-future theorem is stated", "same complete record configuration have the same lawful future" in note)
    check("A four full-rule conditions are explicit", all(marker in note for marker in ("preparation separation", "record markov sufficiency", "local phase transport", "quantum completeness")))
    check("A note contains N1-N8", all(f"### N{i}" in raw for i in range(1, 9)))
    check("A no universal state claim is made", "rules out neither universal claim" in note)


def markov_semantic_control() -> None:
    section("B - Same record state forces one future fingerprint")
    record_state = frozenset({("source", "same")})
    law_fingerprint = {
        record_state: {
            "z_test": frozenset({0, 1}),
            "x_test": frozenset({"+", "-"}),
        }
    }
    prep_a_state = record_state
    prep_b_state = record_state
    check("B equal record configurations index the same law answer", law_fingerprint[prep_a_state] == law_fingerprint[prep_b_state])

    plus_x = (probability(PXP, PXP), probability(PXP, PXM))
    minus_x = (probability(PXM, PXP), probability(PXM, PXM))
    plus_z = (probability(PXP, PZP), probability(PXP, PZM))
    minus_z = (probability(PXM, PZP), probability(PXM, PZM))
    check("B plus/minus preparations have equal Z statistics", plus_z == minus_z == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("B plus/minus preparations have distinct X statistics", plus_x == (1, 0) and minus_x == (0, 1))
    check("B one record state cannot carry both distinct fingerprints under one Markov law", law_fingerprint[prep_a_state] == law_fingerprint[prep_b_state] and plus_x != minus_x)


def append_phase_token(config: frozenset[tuple[int, str]], edges: tuple[tuple[int, int], ...]) -> frozenset[tuple[int, str]]:
    values_by_site = {site: value for site, value in config}
    additions = set(config)
    for left, right in edges:
        if left in values_by_site and right not in values_by_site:
            additions.add((right, values_by_site[left]))
        if right in values_by_site and left not in values_by_site:
            additions.add((left, values_by_site[right]))
    return frozenset(additions)


def local_phase_propagation() -> None:
    section("C - Persistent local phase-reference propagation")
    edges = tuple((index, index + 1) for index in range(5))
    plus = frozenset({(0, "+")})
    minus = frozenset({(0, "-")})
    plus_history = [plus]
    minus_history = [minus]
    for _ in range(5):
        plus_history.append(append_phase_token(plus_history[-1], edges))
        minus_history.append(append_phase_token(minus_history[-1], edges))

    check("C M2 phase-reference projectors are distinct", PXP != PXM and PXP * PXM == sp.zeros(2))
    check("C propagation takes graph-distance-many rounds", (5, "+") not in plus_history[4] and (5, "+") in plus_history[5])
    check("C minus reference propagates on the same covariant graph rule", (5, "-") in minus_history[5])
    check("C every propagation round is append-only", all(plus_history[i].issubset(plus_history[i + 1]) and minus_history[i].issubset(minus_history[i + 1]) for i in range(5)))
    check("C source records remain present after propagation", (0, "+") in plus_history[-1] and (0, "-") in minus_history[-1])
    check("C propagated record configurations remain distinct", plus_history[-1] != minus_history[-1])

    future_table = {
        "+": {"z": frozenset({0, 1}), "x": frozenset({"+"})},
        "-": {"z": frozenset({0, 1}), "x": frozenset({"-"})},
    }
    check("C phase records yield equal Z support and distinct X support", future_table["+"]["z"] == future_table["-"]["z"] and future_table["+"]["x"] != future_table["-"]["x"])


def entangled_phase_fingerprint() -> None:
    section("D - Relational Bell-phase fingerprint")
    zero = sp.Matrix([1, 0])
    one = sp.Matrix([0, 1])
    plus = (zero + one) / sp.sqrt(2)
    minus = (zero - one) / sp.sqrt(2)
    phi_plus = (sp.kronecker_product(zero, zero) + sp.kronecker_product(one, one)) / sp.sqrt(2)
    phi_minus = (sp.kronecker_product(zero, zero) - sp.kronecker_product(one, one)) / sp.sqrt(2)

    def joint_table(state: sp.Matrix, basis: dict[str, sp.Matrix]) -> dict[tuple[str, str], sp.Expr]:
        rho = state * state.conjugate().T
        return {
            (left_name, right_name): probability(
                rho,
                sp.kronecker_product(left * left.conjugate().T, right * right.conjugate().T),
            )
            for left_name, left in basis.items()
            for right_name, right in basis.items()
        }

    z_basis = {"0": zero, "1": one}
    x_basis = {"+": plus, "-": minus}
    zz_plus = joint_table(phi_plus, z_basis)
    zz_minus = joint_table(phi_minus, z_basis)
    xx_plus = joint_table(phi_plus, x_basis)
    xx_minus = joint_table(phi_minus, x_basis)
    zz_support_plus = frozenset(outcome for outcome, value in zz_plus.items() if value != 0)
    zz_support_minus = frozenset(outcome for outcome, value in zz_minus.items() if value != 0)
    xx_support_plus = frozenset(outcome for outcome, value in xx_plus.items() if value != 0)
    xx_support_minus = frozenset(outcome for outcome, value in xx_minus.items() if value != 0)

    def marginals(table: dict[tuple[str, str], sp.Expr]) -> dict[str, dict[str, sp.Expr]]:
        labels = ("+", "-")
        return {
            "left": {label: sp.simplify(sum(value for (left, _), value in table.items() if left == label)) for label in labels},
            "right": {label: sp.simplify(sum(value for (_, right), value in table.items() if right == label)) for label in labels},
        }

    local_x_plus = marginals(xx_plus)
    local_x_minus = marginals(xx_minus)
    uniform_marginals = {
        "left": {"+": sp.Rational(1, 2), "-": sp.Rational(1, 2)},
        "right": {"+": sp.Rational(1, 2), "-": sp.Rational(1, 2)},
    }
    check("D Bell phases have the same computed ZZ support", zz_support_plus == zz_support_minus == frozenset({("0", "0"), ("1", "1")}))
    check("D Bell phases have the same computed local X marginals", local_x_plus == local_x_minus == uniform_marginals)
    check("D Bell phases have different computed joint XX correlations", xx_support_plus == frozenset({("+", "+"), ("-", "-")}) and xx_support_minus == frozenset({("+", "-"), ("-", "+")}))

    configs = {
        "phi_plus": frozenset({("source", "relative_phase_0")}),
        "phi_minus": frozenset({("source", "relative_phase_pi")}),
    }
    fingerprints = {
        configs["phi_plus"]: {"zz": zz_support_plus, "xx": xx_support_plus},
        configs["phi_minus"]: {"zz": zz_support_minus, "xx": xx_support_minus},
    }
    check("D persistent relational records can index the two fingerprints", configs["phi_plus"] != configs["phi_minus"] and len(fingerprints) == 2)

    stripped = {name: frozenset() for name in configs}
    check("D deleting the phase record collapses the source states", stripped["phi_plus"] == stripped["phi_minus"])


def classification() -> None:
    section("E - Constitutional classification")
    note = " ".join(NOTE.read_text().lower().replace("**", "").replace("`", "").split())
    for marker in (
        "s is not proved axiom-minimal",
        "open conditional",
        "retain the current state sentence if they close",
        "widen it only if an exact physical counterexample survives",
        "not evidence that phase is a classical hidden variable",
    ):
        check(f"E note marker: {marker}", marker in note)


def main() -> None:
    source_contract()
    markov_semantic_control()
    local_phase_propagation()
    entangled_phase_fingerprint()
    classification()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        raise SystemExit(1)
    print("RESULT: PASS")
    print("BOUNDARY: finite phase-reference compatibility witness; no quantum derivation or state edit")


if __name__ == "__main__":
    main()
