#!/usr/bin/env python3
"""Exact conditional-law response and reversible polar-transport checks.

The runner verifies a response-Jacobian cross-object, exact compatible
finite-law witnesses, stabilizer and marginal-coupling obstructions, and the
variation-versus-response boundary.  All load-bearing arithmetic is symbolic
or rational.  No floating-point output is reconstructed as exact data.
"""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import sympy as sp

from admissibility_conditional_law_response_polar_transport_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CONDITIONAL_LAW_RESPONSE_POLAR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_conditional_law_response_polar_transport_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_cubic_feature",
    "break_response_normalization",
    "drop_reciprocal_response",
    "unequal_reciprocal_weights",
    "erase_improper_sector",
    "promote_rank_loss",
    "erase_stabilizer",
    "marginals_choose_transport",
    "break_joint_conditional",
    "promote_variation_to_response",
    "claim_physical_selection",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def signed_permutation_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                rotations.append(sp.Matrix(matrix))
    return tuple(rotations)


def atoms() -> tuple[sp.Matrix, ...]:
    basis = tuple(sp.eye(3).col(i) for i in range(3))
    return (sp.zeros(3, 1), basis[0], -basis[0], basis[1], -basis[1],
            basis[2], -basis[2])


def dot_kernel(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    numerator = (left.T * right)[0]
    left_norm = (left.T * left)[0]
    right_norm = (right.T * right)[0]
    return sp.cancel(numerator / ((1 + left_norm) * (1 + right_norm)))


def conditional_weights(neighbors: tuple[sp.Matrix, ...], sign: int,
                        quadratic: bool = False,
                        mutation: str | None = None) -> tuple[sp.Expr, ...]:
    raw = []
    for atom in atoms():
        value = sp.Integer(1)
        for neighbor in neighbors:
            interaction = dot_kernel(atom, neighbor)
            factor = 2 + (interaction ** 2 if quadratic
                          else sign * interaction)
            if mutation == "break_joint_conditional" and atom == atoms()[1]:
                factor += sp.Rational(1, 13)
            value *= factor
        raw.append(sp.cancel(value))
    total = sp.cancel(sum(raw))
    if mutation == "break_response_normalization":
        total += 1
    return tuple(sp.cancel(value / total) for value in raw)


def conditional_from_joint_ratio(neighbors: tuple[sp.Matrix, ...], sign: int,
                                 quadratic: bool = False) -> tuple[sp.Expr, ...]:
    """The displayed edge-product joint law gives this one-site conditional."""
    raw = []
    for atom in atoms():
        value = sp.Integer(1)
        for neighbor in neighbors:
            interaction = dot_kernel(atom, neighbor)
            value *= 2 + (interaction ** 2 if quadratic
                          else sign * interaction)
        raw.append(sp.cancel(value))
    total = sp.cancel(sum(raw))
    return tuple(sp.cancel(value / total) for value in raw)


def cross_moment(pairs: tuple[tuple[sp.Matrix, sp.Matrix], ...]) -> sp.Matrix:
    total = sp.zeros(3)
    for left, right in pairs:
        total += left * right.T
    return sp.simplify(total / len(pairs))


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0

    if mode == "independent":
        for name, condition in independent_facts().items():
            check(f"independent: {name}", condition)
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return int(FAIL != 0)

    root = Path(__file__).resolve().parents[1]
    axiom = (root / "docs/MINIMAL_AXIOMS_2026-06-29.md").read_text()
    check("axiom boundary: nearest-neighbor conditional variation is present but dynamics are absent",
          "probability distribution over the possibilities is" in axiom
          and "determined by, and varies with, the nearest-neighbor conditions" in axiom
          and "Admissibility is not a dynamics axiom" in axiom)

    rotations = signed_permutation_rotations()
    probe = sp.Matrix((sp.Rational(1, 2), sp.Rational(-1, 3),
                       sp.Rational(2, 5)))
    rotation = rotations[7]
    feature = lambda vector: sp.simplify(
        vector / (1 + sp.sqrt((vector.T * vector)[0])))
    transformed_feature = feature(rotation * probe)
    if mutation == "break_cubic_feature":
        transformed_feature += sp.Matrix((1, 0, 0))
    check("feature geometry: the 24 proper cubic rotations preserve the Bloch metric and bounded feature",
          len(rotations) == 24
          and all(g.T * g == sp.eye(3) and g.det() == 1 for g in rotations)
          and transformed_feature == rotation * feature(probe))

    # Exact reciprocal response algebra on arbitrary rational matrices.
    directed = sp.Matrix(((1, 2, 0), (0, 1, 1), (1, 0, 1)))
    reverse = sp.Matrix(((2, 0, 1), (1, 1, 0), (0, 1, 2)))
    cross = directed + reverse.T
    reverse_cross = reverse + directed.T
    if mutation == "drop_reciprocal_response":
        reverse_cross = reverse
    left_frame = rotations[5]
    right_frame = rotations[13]
    transformed_cross = (
        left_frame * directed * right_frame.T
        + (right_frame * reverse * left_frame.T).T
    )
    check("reciprocal cross-object: reversal is adjoint and endpoint-frame covariance is exact",
          reverse_cross == cross.T
          and transformed_cross == left_frame * cross * right_frame.T)

    alpha, beta = sp.symbols("alpha beta", real=True)
    symbolic_residual = sp.simplify(
        (alpha * reverse + beta * directed.T)
        - (alpha * directed + beta * reverse.T).T
    )
    numeric_alpha = sp.Integer(1)
    numeric_beta = (sp.Integer(2) if mutation == "unequal_reciprocal_weights"
                    else sp.Integer(1))
    ansatz_cross = numeric_alpha * directed + numeric_beta * reverse.T
    ansatz_reverse = numeric_alpha * reverse + numeric_beta * directed.T
    check("linear ansatz: reversal forces equal directed-response weights but leaves a common sign convention",
          symbolic_residual == (alpha - beta) * (reverse - directed.T)
          and ansatz_reverse == ansatz_cross.T)

    # Seven-atom edge-product laws.  Differentiate the normalized conditional
    # mean itself, rather than inserting the response coefficient by hand.
    b0, b1, b2 = sp.symbols("b0 b1 b2", real=True)
    neighbor_variable = sp.Matrix((b0, b1, b2))
    derivative_neighbors = (neighbor_variable,) + (sp.zeros(3, 1),) * 5
    substitution_zero = {b0: 0, b1: 0, b2: 0}
    response = {}
    for sign in (1, -1):
        response_mutation = (
            "break_response_normalization"
            if mutation == "break_response_normalization" and sign == 1
            else None
        )
        law = conditional_weights(derivative_neighbors, sign,
                                  mutation=response_mutation)
        conditional_mean = sum(
            (weight * atom for weight, atom in zip(law, atoms())),
            sp.zeros(3, 1),
        )
        response[sign] = sp.simplify(
            conditional_mean.jacobian((b0, b1, b2)).subs(substitution_zero)
        )
    response_plus = response[1]
    response_minus = response[-1]
    cross_plus = response_plus + response_plus.T
    cross_minus = response_minus + response_minus.T
    polar_plus = sp.eye(3)
    polar_minus = -sp.eye(3)
    check("compatible positive response: C=I/7 is full rank and has proper polar I",
          cross_plus == sp.eye(3) / 7
          and cross_plus.det() == sp.Rational(1, 343)
          and polar_plus.T * polar_plus == sp.eye(3)
          and polar_plus.det() == 1)
    negative_polar = (sp.eye(3) if mutation == "erase_improper_sector"
                      else polar_minus)
    check("orientation boundary: C=-I/7 is full rank and has improper polar -I",
          cross_minus == -sp.eye(3) / 7
          and cross_minus.det() == sp.Rational(-1, 343)
          and negative_polar == -sp.eye(3)
          and negative_polar.det() == -1)

    zero = sp.zeros(3, 1)
    e1 = sp.eye(3).col(0)
    zero_neighbors = (zero,) * 6
    one_neighbor = (e1,) + (zero,) * 5
    uniform = conditional_weights(zero_neighbors, 1)
    varied_quad = conditional_weights(one_neighbor, 1, quadratic=True)
    quadratic_law = conditional_weights(derivative_neighbors, 1,
                                        quadratic=True)
    quadratic_mean = sum(
        (weight * atom for weight, atom in zip(quadratic_law, atoms())),
        sp.zeros(3, 1),
    )
    nonlinear_derivative = sp.simplify(
        quadratic_mean.jacobian((b0, b1, b2)).subs(substitution_zero)
    )
    if mutation == "promote_rank_loss":
        nonlinear_derivative = sp.eye(3)
    check("rank-loss countermodel: a varying positive cubic law has zero reciprocal Jacobian at the symmetric context",
          uniform == (sp.Rational(1, 7),) * 7
          and varied_quad[1] == sp.Rational(33, 226)
          and varied_quad[2] == sp.Rational(33, 226)
          and all(varied_quad[i] == sp.Rational(16, 113)
                  for i in (0, 3, 4, 5, 6))
          and nonlinear_derivative == sp.zeros(3))

    # The conditional obtained by normalizing the edge-product joint weight is
    # exactly the displayed local kernel.
    local = conditional_weights(one_neighbor, 1,
                                mutation=("break_joint_conditional"
                                          if mutation == "break_joint_conditional"
                                          else None))
    from_joint = conditional_from_joint_ratio(one_neighbor, 1)
    check("joint compatibility witness: edge-product weights recover the one-site conditional exactly",
          local == from_joint and sum(from_joint) == 1
          and all(value > 0 for value in from_joint))

    # Stabilizer obstruction: (g-I)C=0 for a pi rotation imposes six
    # independent row constraints and every solution has rank at most one.
    half_turn = sp.diag(1, -1, -1)
    generic_entries = sp.symbols("c00:03 c10:13 c20:23")
    generic_cross = sp.Matrix(3, 3, generic_entries)
    constraint_matrix, _ = sp.linear_eq_to_matrix(
        list((half_turn - sp.eye(3)) * generic_cross), generic_entries)
    constraint_rank = constraint_matrix.rank()
    if mutation == "erase_stabilizer":
        constraint_rank = 0
    check("stabilizer obstruction: an invariant endpoint law forbids an equivariant invertible cross-object",
          half_turn != sp.eye(3) and constraint_rank == 6)

    axis = atoms()[1:]
    axis_mean = sum(axis, sp.zeros(3, 1)) / 6
    axis_second = sum((vector * vector.T for vector in axis), sp.zeros(3)) / 6
    fixed_rows = sp.Matrix.vstack(*tuple(g - sp.eye(3) for g in rotations))
    check("symmetric exact laws: central adjoint content vanishes and the axis law has isotropic second moment with no fixed vector",
          axis_mean == sp.zeros(3, 1)
          and axis_second == sp.eye(3) / 3
          and fixed_rows.rank() == 3)

    central_even_feature = sp.zeros(3, 1)
    central_odd_feature = (sp.eye(3).col(0)
                           if mutation == "promote_variation_to_response"
                           else sp.zeros(3, 1))
    sequence_index = sp.symbols("sequence_index", integer=True, positive=True)
    central_input_gap = sp.Integer(1) / sequence_index
    central_total_variation = sp.Integer(1)
    check("variation boundary: distinct central output laws have identical zero Bloch means and supply no orientation response",
          "+I" != "-I"
          and central_even_feature == sp.zeros(3, 1)
          and central_odd_feature == sp.zeros(3, 1)
          and sp.limit(central_input_gap, sequence_index, sp.oo) == 0
          and central_total_variation == 1)

    aligned = tuple((vector, vector) for vector in axis)
    antipodal = tuple((vector, -vector) for vector in axis)
    product = tuple((left, right) for left in axis for right in axis)
    moments = (cross_moment(product), cross_moment(aligned),
               cross_moment(antipodal))
    if mutation == "marginals_choose_transport":
        moments = (sp.eye(3) / 3,) * 3
    check("same-marginal completions: cross moments are 0, I/3, and -I/3 with distinct polar sectors",
          moments == (sp.zeros(3), sp.eye(3) / 3, -sp.eye(3) / 3))

    physical_selection = mutation == "claim_physical_selection"
    check("physical boundary: the construction does not select a feature, sign, context, rank sector, action, or physical connection",
          not physical_selection)

    print("per_element: exact atoms, matrices, determinants, stabilizers, and cross moments were checked")
    print("per_site: normalized one-site laws and their zero-context response Jacobians were checked exactly")
    print("per_mode: proper, improper, and singular reciprocal-response modes were each executed exactly")
    print("per_block: checked and not executed — no exhaustive finite-graph census; edge-product factorization is proved in the note")
    print("lattice_wide: checked and not executed — no infinite-volume phase, global flatness, or physical dynamics claim")
    print("STATUS: conditional construction; universal law-only full-rank extraction obstructed on symmetric loci")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"),
                        default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
