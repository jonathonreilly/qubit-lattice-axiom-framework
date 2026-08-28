#!/usr/bin/env python3
"""Exact gauge-vector matter, source, stress, and transfer checks."""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_gauge_vector_matter_source_transfer_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_GAUGE_VECTOR_MATTER_SOURCE_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_METRIC_SOURCE_POLARIZED_SEAM_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_gauge_vector_matter_source_transfer_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_metric_coefficient",
    "erase_matter_current",
    "break_matter_equation",
    "erase_metric_stress",
    "erase_source_response",
    "break_mixed_reciprocity",
    "break_matter_link_reciprocity",
    "break_orientation_reversal",
    "promote_improper_gauge_force",
    "claim_sector_selection",
    "negative_gauge_coupling",
    "negative_matter_coupling",
    "erase_unmatched_source_falsifier",
    "zero_matter_injective",
    "erase_matter_support_degree",
    "claim_physical_matter",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def exterior_character(relative: sp.Matrix) -> sp.Expr:
    return sp.expand((sp.eye(3) + relative).det())


def defect(relative: sp.Matrix) -> sp.Expr:
    return sp.simplify(16 - 2 * exterior_character(relative))


def hop_norm(source: sp.Matrix, target: sp.Matrix,
             rotation: sp.Matrix) -> sp.Expr:
    difference = target - rotation * source
    return sp.expand((difference.T * difference)[0])


def skew(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify((matrix - matrix.T) / 2)


def so_pair(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(-sp.trace(left * right) / 2)


def dyadic(exponent: sp.Expr) -> sp.Expr:
    exact = sp.cancel(exponent)
    if exact.is_Integer is not True:
        raise ValueError(f"nonintegral dyadic exponent: {exact}")
    return sp.Rational(2) ** (-int(exact))


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


def two_history_core(histories: tuple[object, object],
                     exponent) -> sp.Matrix:
    return sp.Matrix(2, 2, lambda row, column:
                     dyadic(exponent(histories[row], histories[column])))


def multiply_by_half_actions(core: sp.Matrix, positive: sp.Matrix,
                             negative: sp.Matrix | None = None) -> sp.Matrix:
    other = positive if negative is None else negative
    return sp.diag(*positive) * core * sp.diag(*other)


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
    source_note = (root / AUDIT_INPUT_PATHS[0]).read_text()
    seam_parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
    action_parent = (root / AUDIT_INPUT_PATHS[2]).read_text()
    axioms = (root / AUDIT_INPUT_PATHS[3]).read_text()
    check("import boundary: parents supply the dynamic metric/source seam and orthogonal character carrier but no vector-matter action or physical matter source",
          "every `O(3)` irreducible coefficient is strictly positive" in action_parent
          and "b(X,Y)^m chi_(rho^(tensor nm))" in seam_parent
          and "G=E^T E" in seam_parent
          and "source/action" in axioms
          and "(Theta F)(z_-)=overline(F(theta z_-))" in source_note
          and "K_cross(z_-,z_+)" in source_note
          and "incident improper plaquette word" in source_note
          and "per-block and" in source_note
          and "checked but not executed" in source_note)

    identity = sp.eye(3)
    e1 = sp.Matrix((1, 0, 0))
    e2 = sp.Matrix((0, 1, 0))
    e3 = sp.Matrix((0, 0, 1))
    proper_rotation = sp.Matrix(((sp.Rational(3, 5), sp.Rational(-4, 5), 0),
                                 (sp.Rational(4, 5), sp.Rational(3, 5), 0),
                                 (0, 0, 1)))
    pi_rotation = sp.diag(-1, -1, 1)
    improper = sp.diag(-1, 1, 1)
    curvature = defect(proper_rotation)

    a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3", positive=True)
    scales = (a0, a1, a2, a3)
    volume = 1 / sp.prod(scales)
    c12 = sp.cancel(volume * a1**2 * a2**2)
    d1 = sp.cancel(volume * a1**2)
    coefficient_ok = all(
        sp.simplify(scales[index] * sp.diff(c12, scales[index])
                    - (1 if index in (1, 2) else -1) * c12) == 0
        for index in range(4)
    ) and all(
        sp.simplify(scales[index] * sp.diff(d1, scales[index])
                    - (1 if index == 1 else -1) * d1) == 0
        for index in range(4)
    ) and all(
        sp.simplify(scales[index] * sp.diff(volume, scales[index]) + volume) == 0
        for index in range(4)
    )
    if mutation == "break_metric_coefficient":
        coefficient_ok = False
    check("diagonal coframe coefficients: logarithmic variations of volume, plaquette weight, and hopping weight are exact",
          coefficient_ok)

    witness = {a0: 2, a1: 3, a2: 5, a3: 7}
    witness_volume = sp.cancel(volume.subs(witness))
    witness_c12 = sp.cancel(c12.subs(witness))
    witness_d1 = sp.cancel(d1.subs(witness))
    gauge_action = sp.cancel(witness_c12 * curvature)
    matter_distance = hop_norm(e1, e2, proper_rotation)
    matter_action = sp.cancel(witness_d1 * matter_distance / 2)
    mass, source_value, quartic, zeta = sp.symbols(
        "mass source quartic zeta", real=True)
    site_norm = sp.symbols("site_norm", nonnegative=True)
    site_action_symbolic = sp.expand(
        volume * ((mass - zeta * source_value) * site_norm / 2
                  + quartic * site_norm**2 / 4)
    )
    site_witness = {
        **witness, mass: 1, source_value: sp.Rational(1, 2),
        quartic: 0, zeta: 1, site_norm: 1,
    }
    site_action = sp.cancel(site_action_symbolic.subs(site_witness))
    total_action = sp.cancel(gauge_action + matter_action + site_action)
    check("exact local action witness: gauge, hopping, and source-potential terms share one rational action",
          curvature == sp.Rational(16, 5)
          and witness_volume == sp.Rational(1, 210)
          and witness_c12 == sp.Rational(15, 14)
          and witness_d1 == sp.Rational(3, 70)
          and gauge_action == sp.Rational(24, 7)
          and matter_action == sp.Rational(3, 350)
          and site_action == sp.Rational(1, 840)
          and total_action == sp.Rational(2063, 600))

    local_action_symbolic = sp.expand(
        c12 * curvature + d1 * matter_distance / 2 + site_action_symbolic)
    stress = tuple(sp.cancel(
        scales[index] * sp.diff(local_action_symbolic, scales[index])
    ).subs(site_witness) for index in range(4))
    if mutation == "erase_metric_stress":
        stress = (sp.Integer(0),) + stress[1:]
    check("slice-action coframe response: all four diagonal logarithmic derivatives are exact and nonzero",
          stress == (sp.Rational(-2063, 600), sp.Rational(14431, 4200),
                     sp.Rational(14359, 4200), sp.Rational(-2063, 600)))

    source_response_expr = sp.diff(site_action_symbolic, source_value)
    source_response = sp.cancel(source_response_expr.subs(site_witness))
    if mutation == "erase_source_response":
        source_response = 0
    source_metric_mixed = sp.cancel(
        a0 * sp.diff(source_response_expr, a0)
    ).subs(site_witness)
    reverse_mixed = sp.cancel(
        sp.diff(a0 * sp.diff(site_action_symbolic, a0), source_value)
    ).subs(site_witness)
    if mutation == "break_mixed_reciprocity":
        reverse_mixed += 1
    target_parameter, mixed_theta = sp.symbols(
        "target_parameter mixed_theta", real=True)
    varied_target = e2 + target_parameter * e1
    mixed_rotation = sp.Matrix(
        ((sp.cos(mixed_theta), -sp.sin(mixed_theta), 0),
         (sp.sin(mixed_theta), sp.cos(mixed_theta), 0),
         (0, 0, 1)))
    mixed_hopping_action = (
        witness_d1 * hop_norm(e1, varied_target, mixed_rotation) / 2)
    matter_link_mixed = sp.simplify(
        sp.diff(sp.diff(mixed_hopping_action, mixed_theta), target_parameter).subs(
            {target_parameter: 0,
             sp.sin(mixed_theta): sp.Rational(4, 5),
             sp.cos(mixed_theta): sp.Rational(3, 5)})
    )
    reverse_matter_link_mixed = sp.simplify(
        sp.diff(sp.diff(mixed_hopping_action, target_parameter), mixed_theta).subs(
            {target_parameter: 0,
             sp.sin(mixed_theta): sp.Rational(4, 5),
             sp.cos(mixed_theta): sp.Rational(3, 5)})
    )
    if mutation == "break_matter_link_reciprocity":
        reverse_matter_link_mixed += 1
    check("slice-action source response and coframe-source reciprocity are exact",
          source_response == sp.Rational(-1, 420)
          and source_metric_mixed == reverse_mixed == sp.Rational(1, 420))
    check("slice-action matter-link mixed derivative is reciprocal",
          matter_link_mixed == reverse_matter_link_mixed
          == sp.Rational(6, 175))

    theta = sp.symbols("theta", real=True)
    rotation_word = sp.Matrix(((sp.cos(theta), -sp.sin(theta), 0),
                               (sp.sin(theta), sp.cos(theta), 0),
                               (0, 0, 1)))
    generator = sp.Matrix(((0, -1, 0), (1, 0, 0), (0, 0, 0)))
    improper_word = rotation_word * improper
    gauge_improper_derivative = sp.simplify(sp.diff(defect(improper_word), theta))
    matter_word = rotation_word * improper
    matter_derivative = sp.simplify(
        sp.diff(hop_norm(e1, e2, matter_word) / 2, theta).subs(theta, 0)
    )
    matter_current = skew(improper * e1 * e2.T)
    current_pair = sp.simplify(2 * so_pair(matter_current, generator))
    proper_gauge_direct = sp.simplify(
        sp.diff(witness_c12 * defect(rotation_word), theta).subs(
            {sp.sin(theta): sp.Rational(4, 5),
             sp.cos(theta): sp.Rational(3, 5)})
    )
    proper_matter_direct = sp.simplify(
        sp.diff(witness_d1 * hop_norm(e1, e2, rotation_word) / 2,
                theta).subs(
            {sp.sin(theta): sp.Rational(4, 5),
             sp.cos(theta): sp.Rational(3, 5)})
    )
    proper_gauge_force = 8 * so_pair(
        witness_c12 * skew(proper_rotation), generator)
    proper_matter_force = 2 * witness_d1 * so_pair(
        skew(proper_rotation * e1 * e2.T), generator)
    if mutation == "erase_matter_current":
        current_pair = 0
        proper_matter_force = 0
    check("slice-link variation: direct proper and improper derivatives equal the ordered plaquette force plus the skew matter current",
          matter_derivative == 1 and current_pair == matter_derivative
          and proper_gauge_direct == proper_gauge_force == sp.Rational(48, 7)
          and proper_matter_direct == proper_matter_force == sp.Rational(-9, 350)
          and proper_gauge_direct + proper_matter_direct
              == proper_gauge_force + proper_matter_force
              == sp.Rational(2391, 350))

    px = sp.Matrix(sp.symbols("px0:3", real=True))
    py = sp.Matrix(sp.symbols("py0:3", real=True))
    local_action = (witness_d1 * hop_norm(px, py, proper_rotation) / 2
                    + witness_volume * ((mass - zeta * source_value) * (px.T * px)[0] / 2
                                        + quartic * (px.T * px)[0] ** 2 / 4))
    derived_gradient = sp.Matrix([sp.diff(local_action, component) for component in px])
    expected_gradient = (witness_d1 * (px - proper_rotation.T * py)
                         + witness_volume * (mass - zeta * source_value
                                             + quartic * (px.T * px)[0]) * px)
    if mutation == "break_matter_equation":
        expected_gradient += e1
    boundary_point = e1
    boundary_action = -(px.T * px)[0] / 2
    boundary_gradient = sp.Matrix([
        sp.diff(boundary_action, component) for component in px
    ]).subs(dict(zip(px, boundary_point)))
    normal_direction = -boundary_gradient
    tangent_projector = sp.eye(3) - boundary_point * boundary_point.T
    check("matter equation: the interior Euler-Lagrange gradient and an exact compact-ball normal-cone boundary witness are correctly typed",
          sp.simplify(derived_gradient - expected_gradient) == sp.zeros(3, 1)
          and boundary_gradient == -boundary_point
          and normal_direction == boundary_point
          and tangent_projector * normal_direction == sp.zeros(3, 1))

    reverse_distance = hop_norm(e2, e1, proper_rotation.T)
    if mutation == "break_orientation_reversal":
        reverse_distance += 1
    rotations = signed_permutation_rotations()
    cubic = rotations[7]
    covariant_distance = hop_norm(cubic * e1, cubic * e2,
                                  cubic * proper_rotation * cubic.T)
    check("orientation and proper-cubic covariance: edge reversal and simultaneous internal frame change preserve hopping",
          reverse_distance == matter_distance
          and len(rotations) == 24
          and covariant_distance == matter_distance
          and defect(cubic * proper_rotation * cubic.T) == curvature)

    if mutation == "promote_improper_gauge_force":
        gauge_improper_derivative += 1
    check("improper-sector current: character force vanishes within the component while the matter current can be nonzero",
          gauge_improper_derivative == 0 and matter_current != sp.zeros(3))

    collision = (defect(pi_rotation) == defect(improper) == 16
                 and hop_norm(e3, e3, pi_rotation) == 0
                 and hop_norm(e3, e3, improper) == 0)
    if mutation == "claim_sector_selection":
        collision = False
    check("determinant-sector boundary: the complete local action has an exact proper/improper collision",
          collision)

    connection_histories = (identity, pi_rotation)
    matter_histories = (sp.zeros(3, 1), e1)
    parent_feature_norm = sp.Rational(2)
    gauge_core = two_history_core(
        connection_histories,
        lambda left, right: parent_feature_norm * defect(left * right.T) / 32,
    )
    matter_core = two_history_core(
        matter_histories,
        lambda left, right: hop_norm(right, left, identity),
    )
    source_halves = sp.Matrix(tuple(
        dyadic(-hop_norm(history, sp.zeros(3, 1), identity))
        for history in matter_histories))
    positive_gram = multiply_by_half_actions(
        gauge_core.multiply_elementwise(matter_core), source_halves)
    check("shared-link positive control: dynamic seam, matter, and reflection-matched source factors give a positive exact Gram",
          positive_gram.det() == sp.Rational(15, 4)
          and positive_gram[0, 0] > 0
          and "injective on (24)" in seam_parent)

    gauge_sign = -1 if mutation == "negative_gauge_coupling" else 1
    negative_gauge_gram = two_history_core(
        connection_histories,
        lambda left, right: -defect(left * right.T) / 16,
    )
    check("gauge sign boundary: nonnegative crossing character coefficients are required and the negative sign has an exact Gram falsifier",
          gauge_sign >= 0
          and negative_gauge_gram == sp.Matrix(((1, 2), (2, 1)))
          and negative_gauge_gram.det() == -3)

    matter_sign = -1 if mutation == "negative_matter_coupling" else 1
    antipodal_histories = (e1, -e1)
    negative_matter_gram = two_history_core(
        antipodal_histories,
        lambda left, right: -hop_norm(right, left, identity) / 4,
    )
    check("matter sign boundary: nonnegative temporal hopping is required and the negative sign has an antipodal Gram falsifier",
          matter_sign >= 0
          and negative_matter_gram.det() == -3)

    positive_halves = sp.Matrix(tuple(
        dyadic(-hop_norm(history, sp.zeros(3, 1), identity))
        for history in matter_histories))
    negative_halves = sp.Matrix(tuple(
        dyadic(sp.Integer(0)) for _history in matter_histories))
    if mutation == "erase_unmatched_source_falsifier":
        negative_halves = positive_halves
    unmatched_source = multiply_by_half_actions(
        sp.ones(2), positive_halves, negative_halves)
    test_vector = sp.Matrix((1, sp.I))
    unmatched_value = sp.simplify((sp.conjugate(test_vector).T
                                  * unmatched_source * test_vector)[0])
    real_test_vector = sp.Matrix((3, -2))
    real_unmatched_value = (
        real_test_vector.T * unmatched_source * real_test_vector)[0]
    check("source reflection boundary: unmatched half-source multipliers give a non-Hermitian kernel and complex quadratic form",
          unmatched_source != unmatched_source.T
          and unmatched_value == 3 - sp.I
          and real_unmatched_value == -1)

    zero_matter_gram = two_history_core(
        matter_histories, lambda _left, _right: sp.Integer(0))
    zero_claim = mutation == "zero_matter_injective"
    check("zero matter coupling: the matter core is rank one and cannot be injective on a nontrivial compact ball",
          zero_matter_gram.rank() == 1 and not zero_claim)

    feature_variable = sp.symbols("feature_variable", real=True)
    temporal_strength = sp.Rational(2)
    matter_series = sp.exp(temporal_strength * feature_variable).series(
        feature_variable, 0, 7).removeO()
    matter_coefficients = tuple(sp.expand(matter_series).coeff(
        feature_variable, degree) for degree in range(7))
    ball_radius = sp.symbols("ball_radius", nonnegative=True)
    ball_measure_normalization = sp.integrate(
        3 * ball_radius**2, (ball_radius, 0, 1))
    if mutation == "erase_matter_support_degree":
        matter_coefficients = matter_coefficients[:3] + (sp.Integer(0),) + matter_coefficients[4:]
    check("strict-support bridge: positive temporal hopping supplies every tensor degree and the parent supplies every group irrep",
          all(matter_coefficients[degree]
                  == temporal_strength**degree / sp.factorial(degree)
              and matter_coefficients[degree] > 0
              for degree in range(7))
          and ball_measure_normalization == 1
          and "sum_(k>=0) tau^k/k!" in source_note
          and "density on the compact ball" in source_note.lower()
          and "every `O(3)` irreducible coefficient is strictly positive" in action_parent
          and "homogeneous metric/source" in seam_parent)

    radial = sp.symbols("radial", nonnegative=True)
    radial_second = sp.integrate(3 * radial**4, (radial, 0, 1))
    radial_fourth = sp.integrate(3 * radial**6, (radial, 0, 1))
    susceptibility = sp.cancel(
        witness_volume**2 * (radial_fourth - radial_second**2) / 4)
    physical_claim = mutation == "claim_physical_matter"
    check("physical boundary: finite source susceptibility is positive but the matter, source, metric stress, time, and Hamiltonian readings remain supplied",
          radial_second == sp.Rational(3, 5)
          and radial_fourth == sp.Rational(3, 7)
          and susceptibility == 3 * witness_volume**2 / 175
          and susceptibility > 0 and not physical_claim)

    print("per_element: exact Q, coframe weights, hopping current, source derivative, and Gram entries were recomputed")
    print("per_site: one compact matter site, one oriented link, and one scalar-source potential were checked exactly")
    print("per_mode: proper, improper, positive-sign, negative-sign, zero-coupling, and unmatched-source modes were executed")
    print("per_block: checked and not executed — finite reflected slabs follow by products, gauge projection, and bounded positive multipliers")
    print("lattice_wide: checked and not executed — no continuum matter law, Einstein equation, Lorentz covariance, or physical Hamiltonian is claimed")
    print("STATUS: supplied compact gauge-vector matter action has exact slice response, full endpoint equations, and a positive finite transfer for strict disclosed signs")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"),
                        default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
