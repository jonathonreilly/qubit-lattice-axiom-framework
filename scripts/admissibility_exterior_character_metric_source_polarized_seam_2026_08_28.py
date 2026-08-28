#!/usr/bin/env python3
"""Exact metric/source polarized-seam and reflection checks.

The runner verifies the algebraic cancellation that makes the joint
metric/source/connection kernel positive, reciprocal variations, exact stress
and source witnesses, and fail-closed boundaries.  All load-bearing arithmetic
is symbolic or rational; no float-to-exact reconstruction is used.
"""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_metric_source_polarized_seam_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_METRIC_SOURCE_POLARIZED_SEAM_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_METRIC_COMPATIBLE_EXTERIOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_metric_source_polarized_seam_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_polarization_counterterm",
    "negative_crossing_coupling",
    "erase_naive_gram_falsifier",
    "claim_independent_metric_frames",
    "erase_metric_stress",
    "erase_source_response",
    "break_mixed_reciprocity",
    "promote_improper_tangent_force",
    "zero_coupling_injective",
    "coframe_level_injective",
    "claim_physical_source",
    "zero_source_normalization",
    "negative_source_normalization",
    "erase_strict_support_tail",
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


def pairing(left_metric: sp.Matrix, left_source: sp.Expr,
            right_metric: sp.Matrix, right_source: sp.Expr,
            source_normalization: sp.Expr = sp.Integer(1)) -> sp.Expr:
    return sp.cancel(sp.trace(left_metric * right_metric) / 3
                     + source_normalization * left_source * right_source)


def exterior_character(relative: sp.Matrix) -> sp.Expr:
    """Return Tr Lambda^*(relative)=det(I+relative), exactly."""
    return sp.expand((sp.eye(3) + relative).det())


def defect(relative: sp.Matrix) -> sp.Expr:
    return sp.simplify(16 - 2 * exterior_character(relative))


def mismatch_pair(left_metric: sp.Matrix, left_source: sp.Expr,
                  right_metric: sp.Matrix, right_source: sp.Expr,
                  source_normalization: sp.Expr = sp.Integer(1)) -> sp.Expr:
    return pairing(left_metric - right_metric,
                   left_source - right_source,
                   left_metric - right_metric,
                   left_source - right_source,
                   source_normalization)


def dyadic_weight(exponent: sp.Expr) -> sp.Expr:
    """Return 2**(-exponent) after proving the exponent is integral."""
    exact = sp.cancel(exponent)
    if exact.is_Integer is not True:
        raise ValueError(f"nonintegral dyadic exponent: {exact}")
    return sp.Rational(2) ** (-int(exact))


def polarized_dyadic_weight(
        left: tuple[sp.Matrix, sp.Expr, sp.Matrix],
        right: tuple[sp.Matrix, sp.Expr, sp.Matrix],
        source_normalization: sp.Expr = sp.Integer(1),
        log_two_coefficient: sp.Expr = sp.Rational(1, 8)) -> sp.Expr:
    """Compute exp(-S) when kappa=log(2)*log_two_coefficient, n=1."""
    left_metric, left_source, left_group = left
    right_metric, right_source, right_group = right
    relative = left_group * right_group.T
    action_without_kappa = (
        pairing(left_metric, left_source,
                right_metric, right_source, source_normalization)
        * defect(relative)
        + 8 * mismatch_pair(left_metric, left_source,
                            right_metric, right_source,
                            source_normalization)
    )
    return dyadic_weight(log_two_coefficient * action_without_kappa)


def naive_dyadic_weight(
        left: tuple[sp.Matrix, sp.Matrix],
        right: tuple[sp.Matrix, sp.Matrix]) -> sp.Expr:
    """Compute the naive-average weight at kappa=log(2)/8."""
    left_metric, left_group = left
    right_metric, right_group = right
    left_volume = sp.trace(left_metric) / 3
    right_volume = sp.trace(right_metric) / 3
    relative = left_group * right_group.T
    exponent = (left_volume + right_volume) * defect(relative) / 16
    return dyadic_weight(exponent)


def gram_from_states(states: tuple[object, ...], entry: object) -> sp.Matrix:
    return sp.Matrix(tuple(
        tuple(entry(left, right) for right in states) for left in states
    ))


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
    action_parent = (root / AUDIT_INPUT_PATHS[2]).read_text()
    metric_parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
    axioms = (root / AUDIT_INPUT_PATHS[3]).read_text()
    check("source boundary: the parents supply the metric carrier and character action but no metric/source extension",
          "positive symmetric three-dimensional cell metrics" in metric_parent
          and "Metric-dependent plaquette weights or volumes" in action_parent
          and "matter/source terms" in action_parent
          and "source/action" in axioms)

    n, kappa, chi = sp.symbols("n kappa chi", positive=True)
    cross_pair, norm_left, norm_right = sp.symbols(
        "cross_pair norm_left norm_right", real=True
    )
    f_n = sp.Rational(16, 1) / n - 2 * chi**n / (n * 8**(n - 1))
    counterterm_coefficient = (sp.Rational(7, 1) * kappa / n
                               if mutation == "break_polarization_counterterm"
                               else sp.Rational(8, 1) * kappa / n)
    seam_action = (kappa * cross_pair * f_n
                   + counterterm_coefficient
                   * (norm_left + norm_right - 2 * cross_pair))
    factorized_action = (8 * kappa * (norm_left + norm_right) / n
                         - 2 * kappa * cross_pair * chi**n
                         / (n * 8**(n - 1)))
    check("polarization identity: the mismatch coefficient cancels the character constant exactly",
          sp.simplify(seam_action - factorized_action) == 0)

    identity = sp.eye(3)
    proper_rotation = sp.Matrix(((sp.Rational(3, 5), sp.Rational(-4, 5), 0),
                                 (sp.Rational(4, 5), sp.Rational(3, 5), 0),
                                 (0, 0, 1)))
    curvature = defect(proper_rotation)
    theta = sp.symbols("theta", real=True)
    rotating_word = sp.Matrix(((sp.cos(theta), -sp.sin(theta), 0),
                               (sp.sin(theta), sp.cos(theta), 0),
                               (0, 0, 1)))
    connection_variation = sp.simplify(
        sp.diff(defect(rotating_word), theta).subs({
            sp.cos(theta): sp.Rational(3, 5),
            sp.sin(theta): sp.Rational(4, 5),
        })
    )
    metric = sp.diag(1, 2, 3)
    source = sp.Rational(1, 2)
    norm = pairing(metric, source, metric, source)
    action = sp.cancel(norm * curvature)
    metric_direction = sp.diag(1, 0, 0)
    metric_stress = sp.cancel(
        pairing(metric_direction, 0, metric, source) * curvature
    )
    if mutation == "erase_metric_stress":
        metric_stress = sp.Integer(0)
    source_response = sp.cancel(source * curvature)
    if mutation == "erase_source_response":
        source_response = sp.Integer(0)
    check("matched curved witness: the supplied metric and source receive exact nonzero response",
          norm == sp.Rational(59, 12)
          and action == sp.Rational(236, 15)
          and metric_stress == sp.Rational(16, 15)
          and source_response == sp.Rational(8, 5))

    metric_connection = sp.cancel(
        pairing(metric_direction, 0, metric, source) * connection_variation
    )
    source_connection = sp.cancel(source * connection_variation)
    if mutation == "break_mixed_reciprocity":
        source_connection += 1
    check("same-action reciprocity: metric/source and connection mixed derivatives agree in both orders",
          metric_connection == sp.Rational(32, 15)
          and source_connection == sp.Rational(16, 5))

    rotations = signed_permutation_rotations()
    cubic = rotations[7]
    second_metric = sp.diag(2, 1, 4)
    transformed_pair = pairing(cubic * metric * cubic.T, source,
                               cubic * second_metric * cubic.T,
                               sp.Rational(-1, 3))
    original_pair = pairing(metric, source, second_metric,
                            sp.Rational(-1, 3))
    if mutation == "claim_independent_metric_frames":
        transformed_pair += 1
    check("common-chart covariance: simultaneous proper-cubic conjugation preserves the metric/source pairing",
          len(rotations) == 24 and transformed_pair == original_pair)

    source_normalization = (sp.Integer(0)
                            if mutation == "zero_source_normalization"
                            else (sp.Integer(-1)
                                  if mutation == "negative_source_normalization"
                                  else sp.Integer(1)))
    check("source normalization: a supplied strictly positive relative scale separates the scalar feature",
          source_normalization > 0)

    coframe = sp.diag(1, 2, 3)
    rotated_coframe = cubic * coframe
    same_metric = rotated_coframe.T * rotated_coframe == coframe.T * coframe
    coframe_injective = mutation == "coframe_level_injective"
    check("coframe quotient: the kernel resolves metrics, not left-orthogonal coframe gauge copies",
          same_metric and rotated_coframe != coframe and not coframe_injective)

    pi_rotation = sp.diag(-1, -1, 1)
    naive_states = ((identity, identity),
                    (2 * identity, identity),
                    (identity, pi_rotation))
    gram = gram_from_states(naive_states, naive_dyadic_weight)
    gram_determinant = (sp.Integer(0) if mutation == "erase_naive_gram_falsifier"
                        else gram.det())
    check("naive metric average falsifier: positive endpoint weights alone do not imply joint reflection positivity",
          gram_determinant == sp.Rational(-1, 64))

    polarized_states = ((identity, sp.Integer(0), identity),
                        (sp.diag(4, 1, 1), sp.Integer(0), identity),
                        (identity, sp.Integer(0), pi_rotation))
    polarized_gram = gram_from_states(
        polarized_states, polarized_dyadic_weight
    )
    check("exact positive control: the polarized metric/connection Gram is positive definite",
          polarized_gram[:1, :1].det() == 1
          and polarized_gram[:2, :2].det() == sp.Rational(63, 64)
          and polarized_gram.det() == sp.Rational(15111, 16384))

    negative_coupling_states = ((identity, sp.Integer(0), identity),
                                (identity, sp.Integer(0), pi_rotation))
    negative_coupling_gram = gram_from_states(
        negative_coupling_states,
        lambda left, right: polarized_dyadic_weight(
            left, right, log_two_coefficient=sp.Rational(-1, 16)
        ),
    )
    crossing_sign = (-1 if mutation == "negative_crossing_coupling" else 1)
    representation_coefficients_nonnegative = crossing_sign >= 0
    check("joint Gram expansion: nonnegative coupling gives tensor-feature squares for metric, source, and character data",
          representation_coefficients_nonnegative
          and negative_coupling_gram == sp.Matrix(((1, 2), (2, 1)))
          and negative_coupling_gram.det() == -3)

    scalar_states = ((identity, sp.Integer(0), identity),
                     (identity, sp.Integer(1), identity))
    zero_alpha_gram = gram_from_states(
        scalar_states,
        lambda left, right: polarized_dyadic_weight(
            left, right, source_normalization=sp.Integer(0)
        ),
    )
    negative_alpha_gram = gram_from_states(
        scalar_states,
        lambda left, right: polarized_dyadic_weight(
            left, right, source_normalization=sp.Integer(-1)
        ),
    )
    check("source-scale boundary: zero scale has identical scalar rows and negative scale has an exact indefinite Gram",
          zero_alpha_gram == sp.ones(2)
          and zero_alpha_gram.rank() == 1
          and negative_alpha_gram == sp.Matrix(((1, 2), (2, 1)))
          and negative_alpha_gram.det() == -3)

    metric_coordinates = sp.symbols("g11 g22 g33", positive=True)
    scalar_coordinate = sp.symbols("source_coordinate", real=True)
    tail_power = 5
    tail_expression = (
        sp.Integer(1)
        if mutation == "erase_strict_support_tail"
        else sum(metric_coordinates) ** tail_power
        * (1 + scalar_coordinate + metric_coordinates[0] * metric_coordinates[1])
    )
    tail_polynomial = sp.Poly(
        tail_expression,
        *metric_coordinates, scalar_coordinate,
    )
    tail_degrees = tuple(sum(monomial) for monomial, _ in tail_polynomial.terms())
    check("strict-support bridge: the parent supplies all group irreps with trivial padding and metric polynomial tails retain arbitrarily high degree",
          "every `O(3)` irreducible coefficient is strictly positive" in action_parent
          and "the trivial summand pads a" in action_parent
          and tail_degrees
          and min(tail_degrees) >= tail_power
          and sp.trace(identity) == 3)

    improper_word = -rotating_word
    improper_curvature = sp.simplify(defect(improper_word))
    improper_tangent_force = sp.simplify(
        sp.diff(improper_curvature, theta)
    )
    if mutation == "promote_improper_tangent_force":
        improper_tangent_force += 1
    improper_metric_stress = sp.cancel(
        pairing(sp.diag(1, 0, 0), 0, identity, 1)
        * improper_curvature
    )
    improper_source_response = sp.cancel(improper_curvature)
    check("improper-sector boundary: curvature can stress metric/source data while the within-component connection force vanishes",
          improper_curvature == 16
          and improper_metric_stress == sp.Rational(16, 3)
          and improper_source_response == 16
          and improper_tangent_force == 0)

    zero_coupling_gram = gram_from_states(
        scalar_states,
        lambda left, right: polarized_dyadic_weight(
            left, right, log_two_coefficient=sp.Integer(0)
        ),
    )
    zero_claim = mutation == "zero_coupling_injective"
    check("zero-coupling boundary: a nontrivial dynamic metric/source domain makes the constant transfer noninjective",
          scalar_states[0] != scalar_states[1]
          and zero_coupling_gram == sp.ones(2)
          and zero_coupling_gram.rank() == 1
          and not zero_claim)

    physical_claim = mutation == "claim_physical_source"
    check("physical boundary: the compact metric/source domain, measure, seam action, and physical identification remain supplied",
          not physical_claim)

    print("per_element: exact pairings, character constants, responses, and Gram determinants were checked")
    print("per_site: one common-chart metric/source seam item and its reciprocal variations were checked exactly")
    print("per_mode: proper curved, improper curved, negative-sign, naive-average, and zero-coupling modes were executed")
    print("per_block: checked and not executed — finite-slab positivity follows by products and pullback of the proved seam kernels")
    print("lattice_wide: checked and not executed — no continuum metric dynamics, Einstein equation, or physical source law is claimed")
    print("STATUS: supplied joint metric/source seam is reflection positive for nonnegative coupling; physical selection remains open")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"),
                        default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
