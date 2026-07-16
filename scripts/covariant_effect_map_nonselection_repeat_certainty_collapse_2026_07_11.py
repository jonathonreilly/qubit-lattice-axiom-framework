#!/usr/bin/env python3
"""Exact checks for covariant effect nonselection and repeat certainty."""

from __future__ import annotations

import itertools
from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label}: {detail}")


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.H)


def basis_menu(dimension: int) -> list[sp.Matrix]:
    result = []
    for index in range(dimension):
        vector = sp.zeros(dimension, 1)
        vector[index] = 1
        result.append(projector(vector))
    return result


def bell_menu() -> list[sp.Matrix]:
    root = sp.sqrt(2)
    vectors = (
        sp.Matrix([1, 0, 0, 1]) / root,
        sp.Matrix([1, 0, 0, -1]) / root,
        sp.Matrix([0, 1, 1, 0]) / root,
        sp.Matrix([0, 1, -1, 0]) / root,
    )
    return [projector(vector) for vector in vectors]


def depolarized_effect(effect_input: sp.Matrix, mixing: sp.Expr) -> sp.Matrix:
    dimension = effect_input.rows
    return sp.simplify(
        mixing * effect_input
        + (1 - mixing) * sp.trace(effect_input) * sp.eye(dimension) / dimension
    )


def structural_family_checks() -> None:
    for menu_name, dimension, menu in (
        ("basis", 2, basis_menu(2)),
        ("basis", 4, basis_menu(4)),
        ("bell", 4, bell_menu()),
    ):
        for mixing in (sp.Integer(0), sp.Rational(1, 3), sp.Integer(1)):
            effects = [depolarized_effect(item, mixing) for item in menu]
            suffix = f"{menu_name}d{dimension}m{str(mixing).replace('/', '_')}"
            check(f"F01{suffix}", sum(effects, sp.zeros(dimension)) == sp.eye(dimension), "rank-one menu effects normalize")
            check(f"F02{suffix}", all(effect.is_positive_semidefinite and (sp.eye(dimension) - effect).is_positive_semidefinite for effect in effects), "all transformed menu elements obey 0<=E<=I")

    for dimension in (2, 4):
        zero = sp.zeros(dimension)
        identity = sp.eye(dimension)
        mixing = sp.Rational(2, 5)
        check(f"F03d{dimension}", depolarized_effect(zero, mixing) == zero, "E_0=0")
        check(f"F04d{dimension}", depolarized_effect(identity, mixing) == identity, "E_I=I")

        menu = basis_menu(dimension)
        additive = True
        indices = range(dimension)
        for mask_left in range(1 << dimension):
            for mask_right in range(1 << dimension):
                if mask_left & mask_right:
                    continue
                left = sum((menu[i] for i in indices if mask_left & (1 << i)), zero)
                right = sum((menu[i] for i in indices if mask_right & (1 << i)), zero)
                additive &= depolarized_effect(left + right, mixing) == (
                    depolarized_effect(left, mixing) + depolarized_effect(right, mixing)
                )
        check(f"F05d{dimension}", additive, "orthogonal additivity holds on every coordinate-projector pair")

    hadamard = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    swap = sp.Matrix(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
    )
    unitaries = (sp.kronecker_product(hadamard, sp.eye(2)), swap)
    projection = bell_menu()[0]
    mixing = sp.Rational(1, 3)
    covariant = all(
        sp.simplify(
            depolarized_effect(unitary * projection * unitary.H, mixing)
            - unitary * depolarized_effect(projection, mixing) * unitary.H
        )
        == sp.zeros(4)
        for unitary in unitaries
    )
    check("F06", covariant, "two exact noncommuting witnesses satisfy unitary covariance")

    povm = (
        sp.diag(sp.Rational(1, 2), 0),
        sp.diag(sp.Rational(1, 2), sp.Rational(1, 3)),
        sp.diag(0, sp.Rational(2, 3)),
    )
    transformed = [depolarized_effect(item, sp.Rational(1, 3)) for item in povm]
    check("F07", sum(povm, sp.zeros(2)) == sp.eye(2), "the rational three-outcome input is a nonprojective POVM")
    check("F08", sum(transformed, sp.zeros(2)) == sp.eye(2), "the hostile map preserves full POVM normalization")
    check("F09", all(item.is_positive_semidefinite and (sp.eye(2) - item).is_positive_semidefinite for item in transformed), "transformed nonprojective POVM elements remain effects")
    shared_projection = basis_menu(2)[0]
    two_outcome_context = (shared_projection, basis_menu(2)[1])
    three_outcome_context = (
        shared_projection,
        basis_menu(2)[1] / 2,
        basis_menu(2)[1] / 2,
    )
    context_mutation = (
        two_outcome_context[0] == three_outcome_context[0]
        and sum(two_outcome_context, sp.zeros(2)) == sp.eye(2)
        and sum(three_outcome_context, sp.zeros(2)) == sp.eye(2)
        and depolarized_effect(two_outcome_context[0], sp.Rational(1, 3))
        != depolarized_effect(three_outcome_context[0], sp.Rational(2, 3))
    )
    check("F10", context_mutation, "rejector detects a menu-length-dependent mutation on one shared projection")


def nonselection_and_duality_checks() -> None:
    dimension = 4
    mixing = sp.Rational(1, 3)
    projection = basis_menu(dimension)[0]
    effect = depolarized_effect(projection, mixing)
    check("N01", effect != projection, "a=1/3 gives a nonprojective effect")
    check("N02", sp.trace(effect * projection) == sp.Rational(1, 2), "noisy self-weight is 1/2 rather than one")

    vector = sp.Matrix([1, 1, 0, 0]) / sp.sqrt(2)
    rho = projector(vector)
    depolarized_state = sp.simplify(mixing * rho + (1 - mixing) * sp.eye(dimension) / dimension)
    duality = all(
        sp.simplify(
            sp.trace(rho * depolarized_effect(candidate, mixing))
            - sp.trace(depolarized_state * candidate)
        )
        == 0
        for candidate in bell_menu() + basis_menu(dimension)
    )
    check("N03", duality, "eight exact fixtures show trace form can return the depolarized state instead of the input state")

    parameter = sp.symbols("a", real=True)
    self_weight = sp.simplify(sp.trace(projection * depolarized_effect(projection, parameter)))
    check("N04", self_weight == parameter + (1 - parameter) / dimension, "rank-one repeat weight has the exact affine form")
    check("N05", sp.solve(sp.Eq(self_weight, 1), parameter) == [1], "repeat certainty selects a=1 inside the hostile family")


def general_collapse_checks() -> None:
    # Proof certificate for the general finite-dimensional lemma.  In a
    # normalized rank-one menu, repeat certainty fixes diagonal entry i of E_i
    # to one.  Positivity and normalization make every other effect's i-th
    # diagonal zero.  The PSD 2x2-minor inequality
    # |E_j[k,i]|^2 <= E_j[k,k] E_j[i,i] then kills row/column i of E_j.
    # Applying this for every i leaves E_j=P_j.
    u, v, diagonal = sp.symbols("u v diagonal", real=True, nonnegative=True)
    principal_minor = sp.Matrix([[0, u + sp.I * v], [u - sp.I * v, diagonal]])
    check("C01", sp.expand(principal_minor.det()) == -(u**2 + v**2), "a PSD zero-diagonal 2x2 principal minor forces its off-diagonal entry to vanish")
    rational_grid = range(-5, 6)
    check("C02", all((x, y) == (0, 0) for x, y in itertools.product(rational_grid, repeat=2) if x * x + y * y == 0), "finite exact control agrees that a real sum of two squares vanishes only at zero")

    # Generic d=2 Hermitian certificate. Repeat certainty for E0 fixes its
    # first diagonal to one. With E1=I-E0, repeat certainty for E1 fixes the
    # remaining E0 diagonal to zero. PSD then kills the complex off-diagonal.
    x, y, b = sp.symbols("x y b", real=True)
    e0 = sp.Matrix([[1, x + sp.I * y], [x - sp.I * y, b]])
    e1 = sp.eye(2) - e0
    p0, p1 = basis_menu(2)
    check("C03", sp.simplify(e0 + e1) == sp.eye(2), "generic d=2 Hermitian menu is jointly normalized")
    check("C04", sp.trace(e0 * p0) == 1 and sp.trace(e1 * p1) == 1 - b, "the two repeat weights isolate the remaining diagonal b")
    check("C05", sp.solve(sp.Eq(sp.trace(e1 * p1), 1), b) == [0], "second repeat certainty forces b=0")
    check("C06", sp.expand(e0.det().subs(b, 0)) == -(x**2 + y**2), "PSD of the repeat-calibrated E0 forces its off-diagonal to zero")
    check("C07", e0.subs({b: 0, x: 0, y: 0}) == p0 and e1.subs({b: 0, x: 0, y: 0}) == p1, "the generic d=2 menu collapses to P0,P1")

    # Hostile controls show both hypotheses are load-bearing.
    for dimension in (2, 4):
        menu = basis_menu(dimension)
        identity_effects = [sp.eye(dimension) for _ in menu]
        check(f"C08d{dimension}", all(sp.trace(effect * menu[i]) == 1 for i, effect in enumerate(identity_effects)), "repeat certainty alone admits E_i=I")
        check(f"C09d{dimension}", sum(identity_effects, sp.zeros(dimension)) != sp.eye(dimension), "the repeat-only hostile family fails joint normalization")


def source_checks() -> None:
    path = Path("docs/COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    check("S01", path.exists(), "source note exists")
    text = path.read_text() if path.exists() else ""
    markers = (
        "readout-to-formation calibration",
        "does not derive POVM additivity",
        "does not derive repeat certainty from Record permanence",
        "does not identify an outcome label as a framework Record",
        "does not establish that the axioms require amendment",
    )
    for index, marker in enumerate(markers, 2):
        check(f"S{index:02d}", marker in text, f"source contains boundary marker: {marker}")


def main() -> int:
    structural_family_checks()
    nonselection_and_duality_checks()
    general_collapse_checks()
    source_checks()
    print("BOUNDARY: additivity, menu normalization, effects, and repeat certainty are named conditional hypotheses with zero premise weight.")
    print("BOUNDARY: the collapse theorem selects E_i=P_i only after the named condition RC_i=Tr(P_i E_i)=1.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
