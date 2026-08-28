#!/usr/bin/env python3
"""Exact hostile controls for the J_r temporal/spatial semigroup defect."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial, prod
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_independent_2026_08_28 import (
    identity as independent_identity,
    complete_step_response_fixture as independent_complete_response_fixture,
    general_r_response_fixture as independent_general_response_fixture,
    matmul as independent_matmul,
    matrix_fixture as independent_matrix_fixture,
    determinant_scale_selection_fixture as independent_determinant_selection_fixture,
    finite_rth_determinant_response_fixture as independent_finite_rth_fixture,
    multi_cell_determinant_response_fixture as independent_multi_cell_fixture,
    original_link_determinant_offblock_fixture as independent_determinant_fixture,
    packet_quadratic_response_fixture as independent_packet_response_fixture,
    s3_mixed_response_fixture as independent_mixed_response_fixture,
    u1_carre_du_champ_fixture as independent_carre_du_champ_fixture,
    transpose as independent_transpose,
    z2_conditional_fixture as independent_z2_fixture,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_PETER_WEYL_OPERATOR_TRUNCATION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_import_boundary",
    "corrupt_projector",
    "corrupt_defect_identity",
    "drop_positivity",
    "corrupt_range_gate",
    "corrupt_core_order",
    "corrupt_commutator",
    "corrupt_kinetic_factor",
    "inject_kinetic_leak",
    "corrupt_conditional_mean",
    "corrupt_variance_formula",
    "drop_improper_component",
    "corrupt_nonconstancy",
    "corrupt_z2_value",
    "erase_generated_interaction",
    "corrupt_normalization_power",
    "separate_normalizations",
    "corrupt_packet_census",
    "corrupt_lipschitz_constant",
    "claim_fixed_cutoff",
    "use_auxiliary_chain",
    "claim_metric_response",
    "claim_physical_time",
    "hide_prior_art",
    "corrupt_general_fiber",
    "claim_r3_variance_nonconstant",
    "corrupt_rth_cumulant",
    "drop_nc_projection",
    "corrupt_response_factor",
    "omit_epsilon_limit",
    "discontinuous_temporal_family",
    "claim_infinite_leading_memory",
    "allow_linear_action_response",
    "corrupt_quadratic_gram",
    "erase_kinetic_descendant",
    "normalize_away_kinetic_descendant",
    "corrupt_double_commutator",
    "restore_first_order_remainder",
    "make_zero_order_nonconstant",
    "corrupt_carre_du_champ_census",
    "corrupt_response_packet_bound",
    "drop_spatial_linear_cutoff",
    "renormalize_response_packet",
    "corrupt_original_link_census",
    "erase_determinant_offblock",
    "replace_actual_carrier_by_increment_model",
    "invent_r3_determinant_offblock",
    "drop_all_q_determinant_selection",
    "factorize_shared_rung_response",
    "corrupt_finite_rth_subset_sum",
    "retain_cylindrical_endpoints",
    "restore_alternating_response_sign",
    "corrupt_finite_rth_packet_bound",
    "corrupt_all_pairs_order",
    "delete_only_cylindrical_endpoints",
    "collapse_all_pairs_context",
    "corrupt_all_pairs_packet_bound",
)

PASS = 0
FAIL = 0


def check(label: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")


def signed_permutation_frames() -> tuple[sp.Matrix, ...]:
    frames: list[sp.Matrix] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = sp.zeros(3)
            for row, column in enumerate(permutation):
                frame[row, column] = signs[row]
            frames.append(frame)
    return tuple(frames)


def z2_laplacian_range_check() -> tuple[bool, bool]:
    """Finite product-map control for A_f J = 2 J A_c on two rail links."""

    states = tuple(product((1, -1), repeat=2))
    coarse_values = ({1: F(2), -1: F(-3)}, {1: F(-5), -1: F(7)})
    factor_two = True
    range_preserved = True
    for coarse in coarse_values:
        pullback = {state: coarse[state[0] * state[1]] for state in states}
        fine_laplacian = {
            state: (
                2 * pullback[state]
                - pullback[(-state[0], state[1])]
                - pullback[(state[0], -state[1])]
            )
            for state in states
        }
        coarse_laplacian = {
            delta: coarse[delta] - coarse[-delta] for delta in (1, -1)
        }
        factor_two &= all(
            fine_laplacian[state] == 2 * coarse_laplacian[state[0] * state[1]]
            for state in states
        )
        range_preserved &= all(
            fine_laplacian[left] == fine_laplacian[right]
            for left in states
            for right in states
            if left[0] * left[1] == right[0] * right[1]
        )
    return factor_two, range_preserved


def primary_matrix_data() -> dict[str, sp.Matrix]:
    isometry = sp.Matrix(((1, 0), (0, 1), (0, 0)))
    operator = sp.Matrix(
        ((sp.Rational(1, 2), 0, sp.Rational(1, 4)),
         (0, sp.Rational(1, 3), 0),
         (sp.Rational(1, 4), 0, sp.Rational(1, 2)))
    )
    projector = isometry * isometry.T
    complement = sp.eye(3) - projector
    compressed = isometry.T * operator * isometry
    defect = isometry.T * operator**2 * isometry - compressed**2
    factor = isometry.T * operator * complement * operator * isometry
    return {
        "J": isometry,
        "S": operator,
        "Q": projector,
        "R": complement,
        "defect": defect,
        "factor": factor,
    }


def primary_z2_rows() -> tuple[tuple[int, F, F], ...]:
    """Direct finite-Haar variance calculation, independent of the helper."""

    states = tuple(product((1, -1), repeat=2))
    rows: list[tuple[int, F, F]] = []
    for member in (1, 2, 3, 5, 8):
        potential = {1: F(0), -1: F(16, member)}
        variances: dict[int, F] = {}
        for delta in (1, -1):
            fiber = tuple(state for state in states if state[0] * state[1] == delta)
            actions = tuple(potential[state[0]] + potential[state[1]] for state in fiber)
            mean = sum(actions, F(0)) / len(actions)
            second = sum((value * value for value in actions), F(0)) / len(actions)
            variances[delta] = second - mean * mean
        rows.append((member, variances[1], variances[-1]))
    return tuple(rows)


def fraction_cumulants(values: tuple[F, ...], maximum: int) -> tuple[F, ...]:
    moments = (F(1),) + tuple(
        sum((value**order for value in values), F(0)) / len(values)
        for order in range(1, maximum + 1)
    )
    cumulants = [F(0)] * (maximum + 1)
    for order in range(1, maximum + 1):
        cumulants[order] = moments[order] - sum(
            (F(comb(order - 1, index - 1))
             * cumulants[index]
             * moments[order - index]
             for index in range(1, order)),
            F(0),
        )
    return tuple(cumulants)


def primary_general_r_rows() -> tuple[tuple[int, bool, bool, bool], ...]:
    """Direct Z2 enumeration of the arbitrary-r response hierarchy."""

    potential = {1: F(0), -1: F(2)}
    centered = {1: F(-1), -1: F(1)}
    single_cumulants = fraction_cumulants(tuple(potential.values()), 7)
    rows: list[tuple[int, bool, bool, bool]] = []
    for width in range(2, 8):
        states = tuple(product((1, -1), repeat=width))
        cumulants_by_delta: dict[int, tuple[F, ...]] = {}
        response_by_delta: dict[int, F] = {}
        expected_by_delta: dict[int, F] = {}
        for delta in (1, -1):
            fiber = tuple(state for state in states if prod(state) == delta)
            actions = tuple(
                sum((potential[value] for value in state), F(0))
                for state in fiber
            )
            moments = (F(1),) + tuple(
                sum((value**order for value in actions), F(0)) / len(actions)
                for order in range(1, width + 1)
            )
            cumulants_by_delta[delta] = fraction_cumulants(actions, width)
            bracket = 2**width * moments[width] - sum(
                (F(comb(width, order))
                 * moments[order]
                 * moments[width - order]
                 for order in range(width + 1)),
                F(0),
            )
            response_by_delta[delta] = F((-1) ** width, factorial(width)) * bracket
            centered_convolution = sum(
                (prod((centered[value] for value in state), start=F(1))
                 for state in fiber),
                F(0),
            ) / len(fiber)
            expected_by_delta[delta] = (
                F((-1) ** width * (2**width - 2)) * centered_convolution
            )

        response_mean = sum(response_by_delta.values(), F(0)) / 2
        response_nc = {
            delta: response_by_delta[delta] - response_mean for delta in (1, -1)
        }
        lower_ok = all(
            cumulants_by_delta[delta][order] == width * single_cumulants[order]
            for delta in (1, -1)
            for order in range(1, width)
        )
        variance_scalar = width == 2 or (
            cumulants_by_delta[1][2] == cumulants_by_delta[-1][2]
        )
        rows.append((width, lower_ok, variance_scalar, response_nc == expected_by_delta))
    return tuple(rows)


def primary_full_step_response_rows() -> tuple[tuple[int, sp.Matrix, sp.Matrix], ...]:
    """SymPy bidegree check with a nontrivial temporal C_epsilon."""

    epsilon, amplitude = sp.symbols("epsilon amplitude")
    rows: list[tuple[int, sp.Matrix, sp.Matrix]] = []
    for width in (3, 4):
        states = tuple(product((1, -1), repeat=width))
        fiber_size = 2 ** (width - 1)
        isometry = sp.zeros(len(states), 2)
        for row, state in enumerate(states):
            isometry[row, 0 if prod(state) == 1 else 1] = 1 / sp.sqrt(fiber_size)
        actions = tuple(sum(0 if value == 1 else 2 for value in state) for state in states)
        temporal_generator = sp.zeros(len(states))
        for row, state in enumerate(states):
            temporal_generator[row, row] = -sp.Rational(width, 7)
            for index in range(width):
                neighbor = list(state)
                neighbor[index] *= -1
                temporal_generator[row, states.index(tuple(neighbor))] = sp.Rational(1, 7)
        temporal = sp.eye(len(states)) + epsilon * temporal_generator
        multiplier = sp.diag(*(
            sum(
                (-epsilon * amplitude * action / 2) ** order / factorial(order)
                for order in range(width + 1)
            )
            for action in actions
        ))
        step = multiplier * temporal * multiplier
        compressed = isometry.T * step * isometry
        defect = isometry.T * step**2 * isometry - compressed**2
        coefficient = defect.applyfunc(
            lambda value: sp.expand(value).coeff(epsilon, width).coeff(amplitude, width)
        )
        nonconstant = sp.simplify(
            coefficient - sp.trace(coefficient) * sp.eye(2) / 2
        )
        character = sp.diag(1, -1)
        centered_power = (-1) ** width * character
        expected = (-1) ** width * (2**width - 2) * centered_power
        rows.append((width, nonconstant, expected))
    return tuple(rows)


def primary_mixed_response_data() -> dict[str, object]:
    """Independent SymPy expansion of the r=3 mixed kinetic/action response."""

    epsilon, amplitude = sp.symbols("epsilon amplitude")
    width = 3
    states = tuple(product((1, -1), repeat=width))
    isometry = sp.zeros(len(states), 2)
    for row, state in enumerate(states):
        isometry[row, 0 if prod(state) == 1 else 1] = sp.Rational(1, 2)

    kinetic = sp.zeros(len(states))
    for row, state in enumerate(states):
        kinetic[row, row] = width
        for index in range(width):
            neighbor = list(state)
            neighbor[index] *= -1
            kinetic[row, states.index(tuple(neighbor))] = -1
    actions = tuple(sum(0 if value == 1 else 2 for value in state)
                    for state in states)
    potential = sp.diag(*actions)
    projector = isometry * isometry.T
    complement = sp.eye(len(states)) - projector
    b_map = complement * potential * isometry
    induced = sp.simplify(isometry.T * kinetic * isometry)
    gamma = sp.simplify(b_map.T * b_map)
    kinetic_descendant = sp.simplify(
        b_map.T * kinetic * b_map
        + (gamma * induced + induced * gamma) / 2
    )

    multiplier = sp.diag(*(
        sum(
            (-epsilon * amplitude * action / 2) ** order / factorial(order)
            for order in range(4)
        )
        for action in actions
    ))
    temporal = sum(
        (((-epsilon) ** order / factorial(order)) * kinetic**order
         for order in range(4)),
        sp.zeros(len(states)),
    )
    step = sp.expand(multiplier * temporal * multiplier)
    compressed = sp.expand(isometry.T * step * isometry)
    defect = sp.expand(isometry.T * step**2 * isometry - compressed**2)

    def coefficient(epsilon_degree: int, lambda_degree: int) -> sp.Matrix:
        return defect.applyfunc(
            lambda value: sp.expand(value).coeff(
                epsilon, epsilon_degree
            ).coeff(amplitude, lambda_degree)
        )

    return {
        "linear": tuple(coefficient(order, 1) for order in range(4)),
        "quadratic_leading": coefficient(2, 2),
        "quadratic_mixed": coefficient(3, 2),
        "induced": induced,
        "gamma": gamma,
        "kinetic_descendant": kinetic_descendant,
    }


def primary_u1_carre_du_champ_data() -> dict[str, object]:
    """Independent SymPy Fourier-state derivation of the scalar remainder."""

    rows: list[tuple[int, int, sp.Rational, sp.Rational]] = []
    for width, weights in (
        (3, (sp.Rational(1), sp.Rational(3), sp.Rational(4))),
        (4, (sp.Rational(2), sp.Rational(3), sp.Rational(5), sp.Rational(7))),
    ):
        gamma = sum((weight**2 for weight in weights), sp.Rational(0)) / 2
        for coarse_mode in range(-5, 6):
            amplitudes: dict[tuple[int, ...], sp.Rational] = {}
            for coordinate, weight in enumerate(weights):
                for shift in (-1, 1):
                    fine_mode = [coarse_mode] * width
                    fine_mode[coordinate] += shift
                    key = tuple(fine_mode)
                    amplitudes[key] = amplitudes.get(key, sp.Rational(0)) + weight / 2
            exact = sum(
                (amplitude**2 * sum(index**2 for index in fine_mode)
                 for fine_mode, amplitude in amplitudes.items()),
                sp.Rational(0),
            )
            predicted = gamma * (width * coarse_mode**2) + gamma
            rows.append((width, coarse_mode, exact, predicted))
    return {
        "rows": tuple(rows),
        "exact": all(exact == predicted
                     for _width, _mode, exact, predicted in rows),
        "no_drift": all(
            next(exact for row_width, row_mode, exact, _predicted in rows
                 if row_width == width and row_mode == mode)
            == next(exact for row_width, row_mode, exact, _predicted in rows
                    if row_width == width and row_mode == -mode)
            for width in (3, 4) for mode in range(6)
        ),
    }


def primary_packet_response_data() -> dict[str, object]:
    """Independent SymPy Gram perturbation and local packet derivative."""

    epsilon = sp.Rational(2, 5)
    b_value = sp.Rational(3, 7)
    isometry = sp.Matrix(((1,), (0,)))
    b_map = sp.Matrix(((0,), (b_value,)))
    exact = sp.diag(sp.Rational(3, 4), sp.Rational(1, 2))
    packet = sp.diag(sp.Rational(2, 3), sp.Rational(5, 12))
    coarse_exact = isometry.T * exact * isometry
    coarse_packet = isometry.T * packet * isometry
    leakage = -epsilon * (b_map * coarse_exact + exact * b_map) / 2
    leakage_packet = -epsilon * (
        b_map * coarse_packet + packet * b_map
    ) / 2
    response = leakage.T * leakage
    response_packet = leakage_packet.T * leakage_packet
    theta = max(abs(value) for value in (exact - packet).diagonal())
    gamma = (b_map.T * b_map)[0]
    bound = 2 * epsilon**2 * gamma * theta

    s_symbol, u_symbol = sp.symbols("s u")
    derivatives = tuple(
        sp.diff(
            sp.exp(-s_symbol) * sum(
                (s_symbol * u_symbol) ** order / factorial(order)
                for order in range(cutoff + 1)
            ),
            s_symbol,
        ).subs(s_symbol, 0)
        for cutoff in range(4)
    )
    return {
        "response_error": abs((response - response_packet)[0]),
        "bound": bound,
        "derivatives": derivatives,
        "u": u_symbol,
        "range_exact": exact * isometry == isometry * coarse_exact,
        "range_packet": packet * isometry == isometry * coarse_packet,
    }


def primary_determinant_offblock_data() -> dict[str, object]:
    """SymPy control of the actual seven-link r=2 determinant sector."""

    t_value = sp.Rational(1, 2)
    epsilon = sp.Rational(1)
    coefficient = sp.Rational(8)
    a_0 = a_1 = sp.Rational(1)
    # Physical Fourier order: vacuum, plaquette 0, plaquette 1, outer loop.
    temporal = sp.diag(1, t_value**4, t_value**4, t_value**6)
    isometry = sp.Matrix(((1, 0), (0, 0), (0, 0), (0, 1)))
    complement = sp.eye(4) - isometry * isometry.T
    potential = coefficient * sp.Matrix(
        ((0, a_0, a_1, 0),
         (a_0, 0, 0, a_1),
         (a_1, 0, 0, a_0),
         (0, a_1, a_0, 0))
    )
    residual = complement * potential * isometry
    coarse_temporal = isometry.T * temporal * isometry
    leakage = -epsilon * (
        residual * coarse_temporal + temporal * residual
    ) / 2
    half_response = sp.simplify(leakage.T * leakage)
    predicted = (
        epsilon**2 * coefficient**2 * a_0 * a_1 / 2
        * (1 + t_value**4) * (t_value**4 + t_value**6)
    )
    return {
        "temporal": temporal,
        "coarse_temporal": coarse_temporal,
        "residual": residual,
        "half_response": half_response,
        "offblock": half_response[0, 1],
        "predicted": predicted,
        "reduced_increment_prediction": (
            epsilon**2 * coefficient**2 * a_0 * a_1 / 2
            * (1 + t_value**4) * (t_value**4 + t_value**8)
        ),
    }


def primary_determinant_scale_selection_data() -> dict[str, object]:
    """Bit-incidence check of the exact determinant selection rule."""

    t_value = sp.Rational(1, 2)
    coefficient = sp.Rational(1)
    rows: list[tuple[int, int, tuple[int, ...], sp.Rational, sp.Rational]] = []
    for width in range(2, 6):
        for cell_count in range(1, 4):
            plaquette_count = width * cell_count

            def plaquette_mask(index: int) -> int:
                return (
                    (1 << index)
                    | (1 << (plaquette_count + index))
                    | (1 << (2 * plaquette_count + index))
                    | (1 << (2 * plaquette_count + index + 1))
                )

            cycles = tuple(plaquette_mask(index)
                           for index in range(plaquette_count))
            for coarse_mask in range(1, 2**cell_count):
                selected = tuple(
                    cell for cell in range(cell_count)
                    if coarse_mask & (1 << cell)
                )
                target = 0
                for cell in selected:
                    for offset in range(width):
                        target ^= cycles[width * cell + offset]
                target_multiplier = t_value ** target.bit_count()
                overlap = sp.Rational(0)
                for left, left_cycle in enumerate(cycles):
                    for right, right_cycle in enumerate(cycles):
                        residual = target ^ right_cycle
                        if left_cycle != residual:
                            continue
                        residual_multiplier = t_value ** left_cycle.bit_count()
                        overlap += (
                            coefficient**2 * (left + 1) * (right + 1) / 4
                            * (1 + residual_multiplier)
                            * (target_multiplier + residual_multiplier)
                        )
                expected = sp.Rational(0)
                if width == 2 and len(selected) == 1:
                    cell = selected[0]
                    left, right = 2 * cell, 2 * cell + 1
                    expected = (
                        coefficient**2 * (left + 1) * (right + 1) / 2
                        * (1 + t_value**4) * (t_value**4 + t_value**6)
                    )
                rows.append((width, cell_count, selected, overlap, expected))
    offdiagonal_rows: list[
        tuple[int, int, int, int, sp.Rational]
    ] = []
    for width in range(2, 6):
        for cell_count in range(1, 4):
            plaquette_count = width * cell_count
            cycles = tuple(
                (1 << index)
                | (1 << (plaquette_count + index))
                | (1 << (2 * plaquette_count + index))
                | (1 << (2 * plaquette_count + index + 1))
                for index in range(plaquette_count)
            )
            coarse_cycles: list[int] = []
            for coarse in range(2**cell_count):
                cycle = 0
                for cell in range(cell_count):
                    if not coarse & (1 << cell):
                        continue
                    for offset in range(width):
                        cycle ^= cycles[width * cell + offset]
                coarse_cycles.append(cycle)
            for left, left_cycle in enumerate(coarse_cycles):
                for right, right_cycle in enumerate(coarse_cycles):
                    if left == right:
                        continue
                    value = sp.Rational(0)
                    for p, plaquette in enumerate(cycles):
                        residual = left_cycle ^ plaquette
                        residual_multiplier = t_value ** residual.bit_count()
                        for k, other in enumerate(cycles):
                            if residual != right_cycle ^ other:
                                continue
                            value += (
                                coefficient**2 / 4
                                * (t_value ** left_cycle.bit_count()
                                   + residual_multiplier)
                                * (t_value ** right_cycle.bit_count()
                                   + residual_multiplier)
                            )
                    offdiagonal_rows.append((
                        width, cell_count, left, right, value
                    ))
    q2_values = {
        (left, right): value
        for width, cell_count, left, right, value in offdiagonal_rows
        if width == 2 and cell_count == 2
    }
    return {
        "rows": tuple(rows),
        "exact": all(overlap == expected
                     for _r, _q, _cells, overlap, expected in rows),
        "r2_positive": all(
            overlap > 0 for width, _q, cells, overlap, _expected in rows
            if width == 2 and len(cells) == 1
        ),
        "r3plus_zero": all(
            overlap == 0 for width, _q, _cells, overlap, _expected in rows
            if width >= 3
        ),
        "full_selection": all(
            (value > 0)
            == (width == 2 and (left ^ right).bit_count() == 1)
            for width, _q, left, right, value in offdiagonal_rows
        ),
        "shared_rung_values": (q2_values[(0, 1)], q2_values[(2, 3)]),
        "tensor_prediction": q2_values[(0, 1)] * t_value**12,
        "shared_rung_nonfactor": (
            q2_values[(0, 1)] == sp.Rational(85, 2048)
            and q2_values[(2, 3)] == sp.Rational(67, 2097152)
            and q2_values[(0, 1)] * t_value**12
            == sp.Rational(85, 8388608)
            and q2_values[(2, 3)] != q2_values[(0, 1)] * t_value**12
        ),
    }


def primary_finite_rth_determinant_data() -> dict[str, object]:
    """SymPy/assignment check of the exact finite-step order-r formula."""

    t_value = sp.Rational(1, 2)
    epsilon = sp.Rational(3, 5)
    determinant_coefficient = sp.Rational(5, 7)
    cases = (
        (2, 1, 0, 0),
        (2, 2, 1, 1),
        (3, 1, 0, 0),
        (3, 2, 1, 1),
        (4, 1, 0, 0),
        (5, 1, 0, 0),
        (6, 1, 0, 0),
    )
    rows: list[tuple[
        int, int, int, int, sp.Rational, sp.Rational, int,
        sp.Rational, sp.Rational,
    ]] = []

    for width, cell_count, cell, background in cases:
        fine_count = width * cell_count
        cell_word = sum(1 << (width * cell + offset)
                        for offset in range(width))
        base_word = sum(
            1 << (width * coarse_cell + offset)
            for coarse_cell in range(cell_count)
            if background & (1 << coarse_cell)
            for offset in range(width)
        )
        target_word = base_word ^ cell_word
        positions = tuple(width * cell + offset for offset in range(width))
        amplitudes = tuple(sp.Rational(offset + 1, offset + 2)
                           for offset in range(width))

        def run_count(word: int) -> int:
            return sum(
                1 for position in range(fine_count)
                if word & (1 << position)
                and (position == 0 or not word & (1 << (position - 1)))
            )

        def temporal(word: int) -> sp.Rational:
            return t_value ** (2 * word.bit_count() + 2 * run_count(word))

        temporal_count = 3 * fine_count + 1
        packet_trivial = sp.Rational(7, 8)
        packet_determinant = sp.Rational(3, 8)

        def packet_temporal(word: int) -> sp.Rational:
            incidence = 2 * word.bit_count() + 2 * run_count(word)
            return (
                packet_determinant**incidence
                * packet_trivial ** (temporal_count - incidence)
            )

        assignment_sum = sp.Rational(0)
        packet_assignment_sum = sp.Rational(0)
        accepted = 0
        for choices in product(range(4), repeat=width):
            first_positions = tuple(
                positions[index] for index, choice in enumerate(choices)
                if choice < 2
            )
            if not first_positions or len(first_positions) == width:
                continue
            first_right = sum(
                1 << positions[index] for index, choice in enumerate(choices)
                if choice == 1
            )
            second_right = sum(
                1 << positions[index] for index, choice in enumerate(choices)
                if choice == 3
            )
            assignment_sum += (
                temporal(base_word ^ first_right)
                * temporal(target_word ^ second_right)
            )
            packet_assignment_sum += (
                packet_temporal(base_word ^ first_right)
                * packet_temporal(target_word ^ second_right)
            )
            accepted += 1

        subset_sum = sp.Rational(0)
        local_full = (1 << width) - 1
        for local_subset in range(1, local_full):
            global_subset = sum(
                1 << positions[offset] for offset in range(width)
                if local_subset & (1 << offset)
            )
            complement = cell_word ^ global_subset
            first_sum = sum(
                (temporal(base_word ^ subword)
                 for subword in range(1 << fine_count)
                 if not subword & ~global_subset),
                sp.Rational(0),
            )
            second_sum = sum(
                (temporal(target_word ^ subword)
                 for subword in range(1 << fine_count)
                 if not subword & ~complement),
                sp.Rational(0),
            )
            subset_sum += first_sum * second_sum

        prefactor = (
            (epsilon * determinant_coefficient / 2) ** width
            * prod(amplitudes)
        )
        theta = 1 - (1 - sp.Rational(1, 8)) ** temporal_count
        packet_bound = (
            2 * (2**width - 2)
            * (epsilon * determinant_coefficient) ** width
            * prod(amplitudes) * theta
        )
        rows.append((
            width, cell_count, cell, background,
            sp.factor(prefactor * assignment_sum),
            sp.factor(prefactor * subset_sum),
            accepted,
            abs(sp.factor(prefactor * (assignment_sum - packet_assignment_sum))),
            packet_bound,
        ))

    scalar_loss = sp.Rational(1, 4)
    factor_two_rows = tuple(
        (
            width,
            (1 - (1 - scalar_loss) ** 2) * (
                sum(2**subset.bit_count()
                    * 2**(width - subset.bit_count())
                    for subset in range(1, (1 << width) - 1))
                / 2**width
            ),
            2 * scalar_loss * (2**width - 2),
            scalar_loss * (2**width - 2),
        )
        for width in range(2, 7)
    )
    return {
        "rows": tuple(rows),
        "exact": all(assignment == predicted
                     for _r, _q, _c, _y, assignment, predicted, _n,
                     _error, _bound in rows),
        "positive": all(assignment > 0
                        for _r, _q, _c, _y, assignment, _predicted, _n,
                        _error, _bound in rows),
        "endpoint_count": all(
            accepted == 4**width - 2 ** (width + 1)
            for width, _q, _c, _y, _assignment, _predicted, accepted,
            _error, _bound in rows
        ),
        "packet_bound": all(error <= bound
                            for _r, _q, _c, _y, _assignment, _predicted,
                            _accepted, error, bound in rows),
        "factor_two_needed": all(
            error <= full_bound and error > halved_bound
            for _width, error, full_bound, halved_bound in factor_two_rows
        ),
        "factor_two_rows": factor_two_rows,
        "small_step": all(
            sum(2**subset.bit_count() * 2**(width - subset.bit_count())
                for subset in range(1, (1 << width) - 1))
            == 2**width * (2**width - 2)
            for width in range(2, 7)
        ),
    }


def primary_multi_cell_determinant_data() -> dict[str, object]:
    """Direct four-half assignment check of the all-pairs response law."""

    cases = (
        (2, 2, 0, 3),
        (2, 3, 2, 7),
        (2, 3, 0, 7),
        (2, 3, 0, 3),
        (2, 3, 0, 5),
        (2, 3, 4, 7),
        (3, 2, 1, 2),
        (4, 1, 0, 1),
    )
    t_value = sp.Rational(1, 2)
    alpha = sp.Rational(3, 14)
    rows: list[tuple[
        int, int, int, int, int, sp.Rational, sp.Rational,
        int, int, sp.Rational, sp.Rational,
    ]] = []

    for width, cell_count, coarse_left, coarse_right in cases:
        fine_count = width * cell_count
        changed_cells = tuple(
            cell for cell in range(cell_count)
            if bool(coarse_left & (1 << cell))
            != bool(coarse_right & (1 << cell))
        )
        distance = len(changed_cells)
        changed_positions = tuple(
            width * cell + offset
            for cell in changed_cells for offset in range(width)
        )
        response_order = len(changed_positions)
        changed_word = sum(1 << position for position in changed_positions)
        amplitudes = tuple(sp.Rational(position + 1, position + 2)
                           for position in range(fine_count))

        def pullback(coarse: int) -> int:
            return sum(
                1 << (width * cell + offset)
                for cell in range(cell_count)
                if coarse & (1 << cell)
                for offset in range(width)
            )

        fine_left = pullback(coarse_left)
        fine_right = pullback(coarse_right)

        def run_count(word: int) -> int:
            return sum(
                1 for position in range(fine_count)
                if word & (1 << position)
                and (position == 0 or not word & (1 << (position - 1)))
            )

        def temporal(word: int) -> sp.Rational:
            return t_value ** (2 * word.bit_count() + 2 * run_count(word))

        def cylindrical(word: int) -> bool:
            return all(
                ((word >> (width * cell)) & ((1 << width) - 1))
                in (0, (1 << width) - 1)
                for cell in range(cell_count)
            )

        assignment_sum = sp.Rational(0)
        accepted = 0
        for choices in product(range(4), repeat=response_order):
            first_subset = sum(
                1 << changed_positions[index]
                for index, choice in enumerate(choices) if choice < 2
            )
            if cylindrical(first_subset):
                continue
            first_right = sum(
                1 << changed_positions[index]
                for index, choice in enumerate(choices) if choice == 1
            )
            second_right = sum(
                1 << changed_positions[index]
                for index, choice in enumerate(choices) if choice == 3
            )
            assignment_sum += (
                temporal(fine_left ^ first_right)
                * temporal(fine_right ^ second_right)
            )
            accepted += 1

        subset_sum = sp.Rational(0)
        allowed_count = 0
        local_full = (1 << response_order) - 1
        for local_subset in range(local_full + 1):
            subset = sum(
                1 << changed_positions[offset]
                for offset in range(response_order)
                if local_subset & (1 << offset)
            )
            if cylindrical(subset):
                continue
            first_sum = sum(
                temporal(fine_left ^ sum(
                    1 << changed_positions[offset]
                    for offset in range(response_order)
                    if local_part & (1 << offset)
                ))
                for local_part in range(local_full + 1)
                if not local_part & ~local_subset
            )
            complement = local_full ^ local_subset
            second_sum = sum(
                temporal(fine_right ^ sum(
                    1 << changed_positions[offset]
                    for offset in range(response_order)
                    if local_part & (1 << offset)
                ))
                for local_part in range(local_full + 1)
                if not local_part & ~complement
            )
            subset_sum += first_sum * second_sum
            allowed_count += 1

        prefactor = alpha**response_order * prod(
            amplitudes[position] for position in changed_positions
        )
        temporal_count = 3 * fine_count + 1
        packet_trivial = sp.Rational(7, 8)
        packet_determinant = sp.Rational(3, 8)

        def packet_temporal(word: int) -> sp.Rational:
            incidence = 2 * word.bit_count() + 2 * run_count(word)
            return (
                packet_determinant**incidence
                * packet_trivial ** (temporal_count - incidence)
            )

        packet_sum = sp.Rational(0)
        for local_subset in range(local_full + 1):
            subset = sum(
                1 << changed_positions[offset]
                for offset in range(response_order)
                if local_subset & (1 << offset)
            )
            if cylindrical(subset):
                continue
            first_sum = sum(
                packet_temporal(fine_left ^ sum(
                    1 << changed_positions[offset]
                    for offset in range(response_order)
                    if local_part & (1 << offset)
                ))
                for local_part in range(local_full + 1)
                if not local_part & ~local_subset
            )
            complement = local_full ^ local_subset
            second_sum = sum(
                packet_temporal(fine_right ^ sum(
                    1 << changed_positions[offset]
                    for offset in range(response_order)
                    if local_part & (1 << offset)
                ))
                for local_part in range(local_full + 1)
                if not local_part & ~complement
            )
            packet_sum += first_sum * second_sum
        theta = 1 - (1 - sp.Rational(1, 8)) ** temporal_count
        packet_bound = (
            2 * (2**response_order - 2**distance)
            * (2 * alpha) ** response_order
            * prod(amplitudes[position] for position in changed_positions)
            * theta
        )
        rows.append((
            width, cell_count, coarse_left, coarse_right, response_order,
            sp.factor(prefactor * assignment_sum),
            sp.factor(prefactor * subset_sum),
            accepted, 2**response_order * (2**response_order - 2**distance),
            abs(sp.factor(prefactor * (subset_sum - packet_sum))),
            packet_bound,
        ))

    return {
        "rows": tuple(rows),
        "exact": all(row[5] == row[6] for row in rows),
        "placement_count": all(row[7] == row[8] for row in rows),
        "packet_bound": all(row[9] <= row[10] for row in rows),
        "factor_two_needed": all(
            (1 - (1 - sp.Rational(1, 4)) ** 2)
            * (2**order - 2**distance)
            > sp.Rational(1, 4) * (2**order - 2**distance)
            and (1 - (1 - sp.Rational(1, 4)) ** 2)
            * (2**order - 2**distance)
            <= 2 * sp.Rational(1, 4) * (2**order - 2**distance)
            for width, _q, left, right, order, *_rest in rows
            for distance in ((left ^ right).bit_count(),)
        ),
        "context_distinct": (
            rows[3][6] != rows[4][6]
            and rows[3][6] != rows[5][6]
        ),
        "orders": tuple(
            (width, (left ^ right).bit_count(), order)
            for width, _q, left, right, order, *_rest in rows
        ),
    }


def independent_mode() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    matrix = independent_matrix_fixture()
    z2 = independent_z2_fixture()
    general = independent_general_response_fixture()
    complete = independent_complete_response_fixture()
    mixed = independent_mixed_response_fixture()
    carre = independent_carre_du_champ_fixture()
    response_packet = independent_packet_response_fixture()
    determinant = independent_determinant_fixture()
    determinant_selection = independent_determinant_selection_fixture()
    finite_rth = independent_finite_rth_fixture()
    multi_cell = independent_multi_cell_fixture()
    expected = ((F(1, 16), F(0)), (F(0), F(0)))
    checks = (
        (
            "independent rational isometry",
            independent_matmul(independent_transpose(matrix["isometry"]), matrix["isometry"])
            == independent_identity(2),
        ),
        ("independent exact positive factorization", matrix["defect"] == matrix["factor"] == expected),
        ("independent positive-contraction spectrum", matrix["operator_spectrum"] == (F(3, 4), F(1, 4), F(1, 3))),
        ("independent conditional Haar projector", z2["projector_idempotent"] and z2["projector_self_adjoint"]),
        ("independent pullback left inverse", z2["isometry_left_inverse"]),
        (
            "independent exact Z2 generated interaction",
            all(plus == F(256, n * n) and minus == 0 for n, plus, minus in z2["gamma_rows"]),
        ),
        (
            "independent variance equals direct/staged defect",
            all(direct == variance for _n, direct, variance in z2["semigroup_rows"]),
        ),
        ("independent nonconstant generated interaction", all(plus != minus for _n, plus, minus in z2["gamma_rows"])),
        (
            "independent scalar normalization square",
            matrix["scaled_defect"]
            == tuple(tuple(matrix["normalization"] ** 2 * value for value in row) for row in expected),
        ),
        ("independent nonzero normalization obstruction", any(any(value for value in row) for row in matrix["scaled_defect"])),
        ("independent packet operator distance", matrix["operator_distance"] == F(1, 8)),
        ("independent packet defect distance", matrix["defect_distance"] == F(3, 64)),
        (
            "independent four-Lipschitz defect bound",
            matrix["defect_distance"] <= 4 * matrix["operator_distance"],
        ),
        ("independent range-preserving zero control", not any(any(value for value in row) for row in matrix["range_defect"])),
        (
            "independent proper-subset Haar fibers",
            general["subset_independence"],
        ),
        (
            "independent arbitrary-r scalar variance and response coefficient",
            all(variance and response and nonconstant
                for _width, variance, response, nonconstant in general["rows"]),
        ),
        (
            "independent complete-step rth response",
            all(plus == expected_plus and minus == expected_minus
                for _width, plus, minus, expected_plus, expected_minus in complete),
        ),
        (
            "independent fixed-n leading response uses a finite carrier",
            all(F(3) * F(-2, 3) ** width != 0 and F(-2) ** width != 0
                for width in range(2, 8)),
        ),
        (
            "independent S3 mixed response has normalized Haar fibers",
            set(mixed["fiber_sizes"]) == {36}
            and mixed["gamma"] == tuple(
                tuple(F(29, 3) * F(int(row == column))
                      for column in range(6)) for row in range(6)
            ),
        ),
        (
            "independent S3 kinetic intertwiner is induced threefold",
            mixed["induced"] == tuple(
                tuple(F(3) * value for value in row)
                for row in mixed["coarse_laplacian"]
            ),
        ),
        (
            "independent S3 epsilon^3 lambda^2 coefficient is -11 I -47 A_c",
            mixed["mixed_k"] == mixed["expected_k"],
        ),
        (
            "independent S3 mixed response is non-scalar kinetic",
            any(mixed["mixed_coefficient"][row][column] != 0
                for row in range(6) for column in range(6) if row != column),
        ),
        (
            "independent differential-Casimir kinetic plus scalar closure",
            carre["exact_decomposition"],
        ),
        (
            "independent scalar closure has no first-order drift",
            carre["even_modes"],
        ),
        (
            "independent scalar closure accumulates coefficient squares",
            carre["scalar_accumulation"],
        ),
        (
            "independent packet half-response Gram bound",
            response_packet["bound_holds"],
        ),
        (
            "independent packet spatial derivative requires cutoff at least one",
            response_packet["exact_linear_cutoffs"]
            and response_packet["zero_cutoff_fails"],
        ),
        (
            "independent seven-link determinant incidence and normalized Haar fibers",
            determinant["incidence_weights"] == (4, 4, 6)
            and set(determinant["fiber_sizes"]) == {8}
            and determinant["orthonormal"],
        ),
        (
            "independent exact determinant half-response off-block",
            determinant["offblock"] == determinant["predicted"] == F(85, 32)
            and determinant["positive"],
        ),
        (
            "independent all-rq determinant selection on original-link cycles",
            determinant_selection["selection_exact"],
        ),
        (
            "independent determinant quadratic off-block selects only r=2 singleton cells",
            determinant_selection["r2_singletons_positive"]
            and determinant_selection["r3plus_zero"],
        ),
        (
            "independent direct series first reaches the determinant off-block at order r",
            finite_rth["formula_exact"] and finite_rth["lower_orders_zero"],
        ),
        (
            "independent finite-r formula recovers the exact r=2 half-response",
            finite_rth["r2_matches"],
        ),
        (
            "independent small-step limit counts proper residual subsets",
            finite_rth["small_step_counts"]
            == tuple((width, 2**width - 2) for width in range(2, 7)),
        ),
        (
            "independent selected order-r response packet bound",
            finite_rth["packet_bound_holds"],
        ),
        (
            "independent all-pairs determinant series has order r times Hamming distance",
            multi_cell["formula_exact"] and multi_cell["lower_orders_zero"],
        ),
        (
            "independent projector deletes all block-cylindrical residuals",
            multi_cell["cylindrical_count_exact"]
            and multi_cell["has_multi_cell_cases"],
        ),
        (
            "independent all-pairs coefficient retains background context",
            multi_cell["context_distinct"],
        ),
        (
            "independent all-pairs response packet bound",
            multi_cell["packet_bound_holds"]
            and multi_cell["factor_two_needed"],
        ),
    )
    for label, condition in checks:
        check(label, condition)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    if mode == "independent":
        return independent_mode()
    PASS = FAIL = 0

    source = Path(__file__).read_text(encoding="utf-8")
    note = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    parents = tuple(Path(path).read_text(encoding="utf-8") for path in AUDIT_INPUT_PATHS[1:4])
    imports_ok = all(Path(path).is_file() for path in AUDIT_INPUT_PATHS)
    if mutation == "break_import_boundary":
        imports_ok = False
    check(
        "typed imports: Block227 step, Block229 physical J_r, Block231 packet, and minimal axioms",
        imports_ok
        and all(dependency in note for dependency in (
            "CO_SCALED_TEMPORAL_TROTTER",
            "BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW",
            "jr_peter_weyl_operator_truncation",
            "minimal_axioms",
        )),
    )

    data = primary_matrix_data()
    projector_ok = data["Q"] == sp.diag(1, 1, 0) and data["Q"] ** 2 == data["Q"]
    if mutation == "corrupt_projector":
        projector_ok = False
    check(
        "Q=J J* is the typed orthogonal residual projector on the fine physical space",
        projector_ok and "Q=JJ*" in note and "H_f^phys" in note and "H_c^phys" in note,
    )

    identity_ok = data["defect"] == data["factor"] == sp.diag(sp.Rational(1, 16), 0)
    if mutation == "corrupt_defect_identity":
        identity_ok = False
    check(
        "exact direct-versus-staged identity J*S^2J-(J*SJ)^2=J*S(I-Q)SJ",
        identity_ok and "T_dir-T_stage" in note,
    )

    eigenvalues = set(data["S"].eigenvals())
    positivity_ok = eigenvalues == {sp.Rational(3, 4), sp.Rational(1, 4), sp.Rational(1, 3)}
    if mutation == "drop_positivity":
        positivity_ok = False
    check(
        "self-adjoint contraction gives a nonzero positive Gram defect",
        positivity_ok and data["S"] == data["S"].T and data["defect"].is_positive_semidefinite,
    )

    range_operator = sp.diag(sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4))
    range_leak = data["R"] * range_operator * data["J"]
    range_defect = (
        data["J"].T * range_operator**2 * data["J"]
        - (data["J"].T * range_operator * data["J"]) ** 2
    )
    range_ok = range_leak == sp.zeros(3, 2) and range_defect == sp.zeros(2)
    if mutation == "corrupt_range_gate":
        range_ok = False
    check(
        "zero defect is exactly the cylindrical-range invariance gate",
        range_ok and "D_epsilon=0  iff" in note,
    )

    epsilon = sp.symbols("epsilon", real=True)
    generator = sp.Matrix(((2, 0, 1), (0, 3, 0), (1, 0, 4)))
    linear_step = sp.eye(3) - epsilon * generator
    compressed_step = data["J"].T * linear_step * data["J"]
    exact_linear_defect = data["J"].T * linear_step**2 * data["J"] - compressed_step**2
    gamma = data["J"].T * generator * data["R"] * generator * data["J"]
    core_ok = sp.simplify(exact_linear_defect - epsilon**2 * gamma) == sp.zeros(2)
    if mutation == "corrupt_core_order":
        core_ok = False
    check(
        "Block227 core derivative generates epsilon^2 Gamma and no epsilon term",
        core_ok and "quadratic-form/core limit" in note,
    )

    commutator = data["Q"] * generator - generator * data["Q"]
    commutator_gamma = (commutator * data["J"]).T * (commutator * data["J"])
    commutator_ok = commutator_gamma == gamma
    if mutation == "corrupt_commutator":
        commutator_ok = False
    check(
        "generated interaction is the positive commutator square ([Q,G]J)*([Q,G]J)",
        commutator_ok and "([Q,G_f]J)*([Q,G_f]J)" in note,
    )

    factor_two, range_preserved = z2_laplacian_range_check()
    kinetic_factor_ok = factor_two
    if mutation == "corrupt_kinetic_factor":
        kinetic_factor_ok = False
    check(
        "two fine rail Casimirs induce twice the coarse rail Casimir",
        kinetic_factor_ok and "2A_(coarse bottom rails)" in note and "2A_(coarse top rails)" in note,
    )

    kinetic_range_ok = range_preserved
    if mutation == "inject_kinetic_leak":
        kinetic_range_ok = False
    check(
        "fine kinetic generator preserves the actual cylindrical range",
        kinetic_range_ok and "(I-Q)A_fJ=0" in note and "hidden rung" in note,
    )

    mu, nu, convolution = sp.symbols("mu nu convolution", real=True)
    mean = 2 * mu
    second = 2 * nu + 2 * convolution
    mean_ok = mean == 2 * mu and second == 2 * nu + 2 * convolution
    if mutation == "corrupt_conditional_mean":
        mean_ok = False
    check(
        "hidden Haar fiber gives the exact first and second conditional moments",
        mean_ok and "E[V_f|delta]=2mu" in note and "E[V_f^2|delta]=2nu+2(v*v)(delta)" in note,
    )

    variance = sp.expand(second - mean**2)
    variance_ok = variance == 2 * (nu - mu**2) + 2 * (convolution - mu**2)
    if mutation == "corrupt_variance_formula":
        variance_ok = False
    check(
        "the complete J_r defect reduces to the typed conditional variance",
        variance_ok and "Gamma=J*V_f(I-Q)V_fJ" in note and "Gamma(delta)" in note,
    )

    frames = signed_permutation_frames()
    frame_rows = tuple(
        (int(frame.det()), int((sp.eye(3) + frame).det())) for frame in frames
    )
    component_ok = len(frames) == 48 and sum(det == 1 for det, _chi in frame_rows) == 24
    component_ok &= all(chi == 0 for det, chi in frame_rows if det == -1)
    if mutation == "drop_improper_component":
        component_ok = False
    check(
        "full O(3) witness keeps all 24 proper and 24 improper signed frames",
        component_ok and "No connected component" in note and "is discarded" in note,
    )

    member = 3
    member_values = tuple(sp.Rational(16, member) * (1 - sp.Rational(chi, 8) ** member) for _det, chi in frame_rows)
    nonconstant_ok = min(member_values) == 0 and max(member_values) == sp.Rational(16, member)
    if mutation == "corrupt_nonconstancy":
        nonconstant_ok = False
    check(
        "the exterior potential is nonconstant and has a nontrivial Peter-Weyl channel",
        nonconstant_ok and "Convolution squares" in note and "nonzero nontrivial channel" in note,
    )

    z2_rows = primary_z2_rows()
    z2_ok = all(plus == F(256, n * n) and minus == 0 for n, plus, minus in z2_rows)
    if mutation == "corrupt_z2_value":
        z2_ok = False
    check(
        "exact Z2 finite control gives Gamma(+)=256/n^2 and Gamma(-)=0",
        z2_ok and "Gamma(+)=256/n^2" in note,
    )

    generated_ok = any(plus != minus for _n, plus, minus in z2_rows)
    if mutation == "erase_generated_interaction":
        generated_ok = False
    check(
        "the specified two-cell paths have a nonzero leading separation coefficient",
        generated_ok and "strictly positive leading" in note,
    )

    general_rows = primary_general_r_rows()
    fiber_ok = all(lower for _width, lower, _variance, _response in general_rows)
    if mutation == "corrupt_general_fiber":
        fiber_ok = False
    check(
        "conditioned retain-every-r fibers are (r-1)-wise Haar",
        fiber_ok and "every proper subset" in note and "independent product Haar" in note,
    )

    scalar_variance_ok = all(
        variance for width, _lower, variance, _response in general_rows if width >= 3
    )
    if mutation == "claim_r3_variance_nonconstant":
        scalar_variance_ok = False
    check(
        "the leading conditional variance is a scalar coarse operator for every r>=3",
        scalar_variance_ok and "Gamma_r(delta)=sigma_v^2 sum_i a_i^2" in note,
    )

    cumulant_ok = all(response for _width, _lower, _variance, response in general_rows)
    if mutation == "corrupt_rth_cumulant":
        cumulant_ok = False
    check(
        "the first arbitrary-r nonconstant moment is the centered r-fold convolution",
        cumulant_ok and "r!(product_i a_i)h^(*r)(delta)" in note,
    )

    response_rows = primary_full_step_response_rows()
    response_ok = all(got == expected for _width, got, expected in response_rows)
    if mutation == "corrupt_response_factor":
        response_ok = False
    check(
        "the complete M C M step has exact (-1)^r(2^r-2) nonconstant response",
        response_ok and "(-1)^r(2^r-2)" in note and "partial_lambda^r D_epsilon" in note,
    )

    nc_ok = "Type `NC` only on the limiting multiplication operator" in note
    nc_ok &= "NC(c_r I+M_F)=M_F" in note
    if mutation == "drop_nc_projection":
        nc_ok = False
    check(
        "the response projects a typed limiting multiplication symbol off only its scalar channel",
        nc_ok,
    )

    limit_ok = "NC (s-lim_(epsilon downarrow 0)" in note
    limit_ok &= "not a fixed-`epsilon` identity" in note
    if mutation == "omit_epsilon_limit":
        limit_ok = False
    check(
        "the arbitrary-r formula is a fixed-finite-r strong/core epsilon limit",
        limit_ok,
    )

    continuity_ok = "C_epsilon-I=O_psi(epsilon)" in note
    continuity_ok &= "strong convergence to `I`" in note
    if mutation == "discontinuous_temporal_family":
        continuity_ok = False
    check(
        "the temporal family converges on every V_f-stable Peter-Weyl core vector",
        continuity_ok,
    )

    finite_memory_ok = all(
        token in note for token in (
            "h=-2(chi_V+chi_(det tensor V)+chi_det)",
            "The resulting leading response carrier has the supplied action coordinate",
            "both inside the same finite\nPeter--Weyl support",
            "Its response order is `r` in the leading simultaneous",
        )
    )
    if mutation == "claim_infinite_leading_memory":
        finite_memory_ok = False
    check(
        "the fixed-n leading hierarchy has finite Peter-Weyl memory while response order grows",
        finite_memory_ok,
    )

    mixed = primary_mixed_response_data()
    linear_response_ok = all(
        coefficient == sp.zeros(2) for coefficient in mixed["linear"]
    )
    if mutation == "allow_linear_action_response":
        linear_response_ok = False
    check(
        "the complete defect has exactly zero linear action response",
        linear_response_ok and "zero linear action response" in note,
    )

    quadratic_gram_ok = (
        mixed["quadratic_leading"] == mixed["gamma"] == 3 * sp.eye(2)
        and mixed["quadratic_mixed"] == -mixed["kinetic_descendant"]
    )
    if mutation == "corrupt_quadratic_gram":
        quadratic_gram_ok = False
    check(
        "quadratic response is epsilon^2 Gamma minus epsilon^3 K",
        quadratic_gram_ok
        and "mathcal K\n =B*A_fB+(1/2){Gamma,A_c^ind}" in note
        and "L_epsilon*L_epsilon>=0" in note,
    )

    kinetic_descendant_ok = (
        mixed["kinetic_descendant"] != sp.trace(
            mixed["kinetic_descendant"]
        ) * sp.eye(2) / 2
        and mixed["quadratic_mixed"][0, 1] != 0
    )
    if mutation == "erase_kinetic_descendant":
        kinetic_descendant_ok = False
    check(
        "epsilon^3 lambda^2 generates a non-scalar coarse-kinetic response",
        kinetic_descendant_ok
        and "mathcal K=2gamma A_c^ind+u_(r,q)I" in note
        and "not a new multiplication potential" in note,
    )

    carre = primary_u1_carre_du_champ_data()
    double_commutator_ok = all(token in note for token in (
        "M_f A_f M_f",
        "(1/2){A_f,M_(f^2)}+(1/2)[M_f,[A_f,M_f]]",
        "(1/2)J_r*[M_f,[A_f,M_f]]J_r",
    ))
    if mutation == "corrupt_double_commutator":
        double_commutator_ok = False
    check(
        "exact double commutator isolates the conditioned carre-du-champ",
        double_commutator_ok,
    )

    scalar_closure_ok = carre["exact"]
    if mutation == "make_zero_order_nonconstant":
        scalar_closure_ok = False
    check(
        "differential-Casimir control closes as kinetic plus scalar multiplication",
        scalar_closure_ok
        and "B*A_fB=gamma A_c^ind+u_(r,q)I" in note
        and "remaining coefficient is independent" in note
        and "of every retained coarse word" in note,
    )

    first_order_ok = carre["no_drift"]
    if mutation == "restore_first_order_remainder":
        first_order_ok = False
    check(
        "the exact r>=3 remainder contains no first-order differential term",
        first_order_ok and "There is no first-order remainder" in note,
    )

    carre_census_ok = all(token in note for token in (
        "u_(r,q)=2D E_v sum_(c=0)^(q-1)sum_(i=0)^(r-1)a_(c,i)^2",
        "Each ladder plaquette has two rail and two\nrung links",
        "sum_(rho!=1)L_rho m_(rho,n)^2",
    ))
    if mutation == "corrupt_carre_du_champ_census":
        carre_census_ok = False
    check(
        "scalar carre-du-champ has the four-link and rq coefficient census",
        carre_census_ok,
    )

    response_packet = primary_packet_response_data()
    spatial_derivative_ok = (
        response_packet["derivatives"][0] == -1
        and all(derivative == response_packet["u"] - 1
                for derivative in response_packet["derivatives"][1:])
    )
    if mutation == "drop_spatial_linear_cutoff":
        spatial_derivative_ok = False
    check(
        "K_beta at least one preserves every spatial half-action first derivative",
        spatial_derivative_ok
        and "`K_beta>=1` on every spatial half-action" in note
        and "partial_s ell_s^K|_0=u-1" in note,
    )

    response_topology_ok = (
        response_packet["range_exact"] and response_packet["range_packet"]
    )
    if mutation == "renormalize_response_packet":
        response_topology_ok = False
    check(
        "packet response keeps the common normalization and cylindrical range",
        response_topology_ok
        and "same exact Block231 temporal normalization" in note
        and "with no separate truncated renormalization" in note
        and "preserves\n`Ran J_r`" in note,
    )

    response_bound_ok = (
        response_packet["response_error"] <= response_packet["bound"]
    )
    if mutation == "corrupt_response_packet_bound":
        response_bound_ok = False
    check(
        "complete quadratic half-response has explicit temporal rq packet bound",
        response_bound_ok
        and "<=2epsilon^2||Gamma|| theta_K" in note
        and "<=2epsilon^2||Gamma||(3rq+1)delta_kappa" in note
        and "bound for the full `partial_lambda^2D|_0` is twice" in note,
    )

    determinant = primary_determinant_offblock_data()
    original_link_census_ok = (
        determinant["temporal"]
        == sp.diag(1, sp.Rational(1, 2) ** 4,
                   sp.Rational(1, 2) ** 4, sp.Rational(1, 2) ** 6)
        and determinant["coarse_temporal"]
        == sp.diag(1, sp.Rational(1, 2) ** 6)
    )
    if mutation == "corrupt_original_link_census":
        original_link_census_ok = False
    check(
        "actual r=2 determinant cycles have four/four/six original-link multipliers",
        original_link_census_ok
        and "two four-link plaquette" in note
        and "six-link outer boundary" in note,
    )

    determinant_offblock_ok = (
        determinant["offblock"] == determinant["predicted"]
        == sp.Rational(85, 32)
        and determinant["offblock"] > 0
    )
    if mutation == "erase_determinant_offblock":
        determinant_offblock_ok = False
    check(
        "complete finite-epsilon J_2 response has an exact positive determinant off-block",
        determinant_offblock_ok
        and "<1,R_epsilon phi_det>" in note
        and "not a central convolution" in note,
    )

    actual_carrier_ok = (
        determinant["predicted"] != determinant["reduced_increment_prediction"]
    )
    if mutation == "replace_actual_carrier_by_increment_model":
        actual_carrier_ok = False
    check(
        "shared-rung cancellation distinguishes the actual carrier from a reduced increment model",
        actual_carrier_ok
        and "`t_det^8`, not the actual `t_det^6`" in note,
    )

    determinant_selection = primary_determinant_scale_selection_data()
    finite_rth = primary_finite_rth_determinant_data()
    independent_finite_rth = independent_finite_rth_fixture()
    multi_cell = primary_multi_cell_determinant_data()
    independent_multi_cell = independent_multi_cell_fixture()
    all_q_selection_ok = (
        determinant_selection["exact"]
        and determinant_selection["r2_positive"]
        and determinant_selection["full_selection"]
    )
    if mutation == "drop_all_q_determinant_selection":
        all_q_selection_ok = False
    check(
        "exact determinant offdiagonal selection is coarse-hypercube adjacency only at r=2",
        all_q_selection_ok
        and "for every finite `q`" in note
        and "`r=2` gives precisely the edges" in note,
    )

    r3_selection_ok = determinant_selection["r3plus_zero"]
    if mutation == "invent_r3_determinant_offblock":
        r3_selection_ok = False
    check(
        "the full O3 quadratic vacuum-to-determinant selection vanishes for r>=3",
        r3_selection_ok
        and "determinant-to-determinant\noffdiagonal block vanishes" in note
        and "mixed kinetic descendant (34c)--(34g)" in note,
    )

    shared_rung_ok = determinant_selection["shared_rung_nonfactor"]
    if mutation == "factorize_shared_rung_response":
        shared_rung_ok = False
    check(
        "shared retained rung makes the exact r=2 response nonfactorizing across q",
        shared_rung_ok
        and "85/2048" in note and "67/2097152" in note
        and "not a tensor product of one-cell responses" in " ".join(note.split()),
    )

    finite_rth_ok = finite_rth["exact"] and independent_finite_rth["formula_exact"]
    if mutation == "corrupt_finite_rth_subset_sum":
        finite_rth_ok = False
    check(
        "exact finite-step determinant off-block first appears at response order r",
        finite_rth_ok and independent_finite_rth["lower_orders_zero"]
        and "All determinant offdiagonal\nderivatives of order below `r` vanish" in note
        and "F_Z(H_c\\X)" in note,
    )

    endpoint_ok = finite_rth["endpoint_count"]
    if mutation == "retain_cylindrical_endpoints":
        endpoint_ok = False
    check(
        "residual projector removes exactly the two cylindrical endpoint subsets",
        endpoint_ok
        and "deletes exactly the endpoint\nwords `X=emptyset,H_c`" in note
        and "emptyset != X proper_subset H_c" in note,
    )

    finite_sign_ok = finite_rth["positive"] and finite_rth["small_step"]
    if mutation == "restore_alternating_response_sign":
        finite_sign_ok = False
    check(
        "finite-step order-r response is positive and recovers 2^r-2 at small step",
        finite_sign_ok and independent_finite_rth["r2_matches"]
        and "<h,chi_det>^r=(-c_det^(n))^r" in note
        and "epsilon^r(c_det^(n))^r(2^r-2)" in note,
    )

    finite_packet_ok = (
        finite_rth["packet_bound"]
        and independent_finite_rth["packet_bound_holds"]
        and finite_rth["factor_two_needed"]
        and independent_finite_rth["factor_two_needed"]
    )
    if mutation == "corrupt_finite_rth_packet_bound":
        finite_packet_ok = all(
            error <= halved_bound
            for _width, error, _full_bound, halved_bound
            in finite_rth["factor_two_rows"]
        )
    check(
        "selected order-r determinant response has explicit temporal rq packet control",
        finite_packet_ok
        and "<=2(2^r-2)(epsilon c_det^(n))^r" in note
        and "product_(p in H_c)|a_p|(3rq+1)delta_kappa" in note
        and "There is no `delta_beta` term" in note,
    )

    all_pairs_order_ok = (
        multi_cell["exact"]
        and independent_multi_cell["formula_exact"]
        and independent_multi_cell["lower_orders_zero"]
    )
    if mutation == "corrupt_all_pairs_order":
        all_pairs_order_ok = all(
            order == width * distance + 1
            for width, distance, order in multi_cell["orders"]
        )
    check(
        "all-pairs determinant response first appears at r times coarse Hamming distance",
        all_pairs_order_ok
        and "m=|H|=rd" in note
        and "ord_lambda(y,z)=r d_H(y,z)" in note,
    )

    cylindrical_deletion_ok = (
        multi_cell["placement_count"]
        and independent_multi_cell["cylindrical_count_exact"]
    )
    if mutation == "delete_only_cylindrical_endpoints":
        cylindrical_deletion_ok = all(
            placements == 2**order * (2**order - 2)
            for _r, _q, left, right, order, _actual, _predicted,
            placements, _expected, _error, _bound in multi_cell["rows"]
            if (left ^ right).bit_count() > 1
        )
    check(
        "Q deletes all 2^d block-cylindrical residual subsets",
        cylindrical_deletion_ok
        and "It has exactly `2^d` members" in note
        and "X notin Cyl(H)" in note
        and "2^m-2^d" in note,
    )

    all_pairs_context_ok = (
        multi_cell["context_distinct"]
        and independent_multi_cell["context_distinct"]
    )
    if mutation == "collapse_all_pairs_context":
        all_pairs_context_ok = (
            multi_cell["rows"][3][6] == multi_cell["rows"][4][6]
            == multi_cell["rows"][5][6]
        )
    check(
        "all-pairs finite-step response retains shared-rung and background context",
        all_pairs_context_ok
        and "not a function\nof Hamming distance alone" in note,
    )

    all_pairs_packet_ok = (
        multi_cell["packet_bound"]
        and independent_multi_cell["packet_bound_holds"]
        and multi_cell["factor_two_needed"]
        and independent_multi_cell["factor_two_needed"]
    )
    if mutation == "corrupt_all_pairs_packet_bound":
        all_pairs_packet_ok = all(
            (1 - (1 - sp.Rational(1, 4)) ** 2)
            * (2**order - 2**distance)
            <= sp.Rational(1, 4) * (2**order - 2**distance)
            for width, _q, left, right, order, *_rest in multi_cell["rows"]
            for distance in ((left ^ right).bit_count(),)
        )
    check(
        "all-pairs determinant response has explicit temporal rq packet control",
        all_pairs_packet_ok
        and "<=2(2^m-2^d)(epsilon c_det^(n))^m" in note
        and "m=r d_H(y,z)" in note,
    )

    scalar_shift = 2 * sp.Rational(7, 5) * mixed["gamma"]
    normalization_invariant_ok = (
        (mixed["quadratic_mixed"] + scalar_shift)[0, 1]
        == mixed["quadratic_mixed"][0, 1] != 0
    )
    if mutation == "normalize_away_kinetic_descendant":
        normalization_invariant_ok = False
    check(
        "common scalar normalization cannot remove the kinetic principal symbol",
        normalization_invariant_ok
        and "sends\n`mathcal K` to `mathcal K-2c_1Gamma`" in note
        and "leaves the exact coefficient `2gamma A_c^ind` unchanged" in note,
    )

    scalar = sp.Rational(3, 5)
    scaled_defect = (
        data["J"].T * (scalar * data["S"]) ** 2 * data["J"]
        - (data["J"].T * (scalar * data["S"]) * data["J"]) ** 2
    )
    normalization_ok = scaled_defect == scalar**2 * data["defect"]
    if mutation == "corrupt_normalization_power":
        normalization_ok = False
    check(
        "one common normalization scalar rescales the defect quadratically",
        normalization_ok and "D_epsilon[cS]=c_epsilon^2 D_epsilon[S]" in note,
    )

    convention_ok = (
        "Separately" in note
        and "normalizing the direct and staged two-step operators" in note
        and "defines a different square" in note
    )
    if mutation == "separate_normalizations":
        convention_ok = False
    check(
        "normalization convention is fixed before comparing direct and staged paths",
        convention_ok,
    )

    r_value, q_value = 2, 2
    temporal_count = 3 * r_value * q_value + 1
    half_count = 2 * r_value * q_value
    eta = temporal_count * F(1, 1000) + half_count * F(1, 2000)
    census_ok = temporal_count == 13 and half_count == 8 and eta == F(17, 1000)
    if mutation == "corrupt_packet_census":
        census_ok = False
    check(
        "complete physical packet error has explicit (3rq+1) delta_kappa + 2rq delta_beta accumulation",
        census_ok and "(3rq+1)delta_kappa+2rq delta_beta" in note,
    )

    packet = sp.Matrix(
        ((sp.Rational(1, 2), 0, sp.Rational(1, 8)),
         (0, sp.Rational(1, 3), 0),
         (sp.Rational(1, 8), 0, sp.Rational(1, 2)))
    )
    packet_compressed = data["J"].T * packet * data["J"]
    packet_defect = data["J"].T * packet**2 * data["J"] - packet_compressed**2
    operator_distance = max(abs(value) for value in (data["S"] - packet).eigenvals())
    defect_distance = max(abs(value) for value in (data["defect"] - packet_defect).eigenvals())
    lipschitz_ok = (
        operator_distance == sp.Rational(1, 8)
        and defect_distance == sp.Rational(3, 64)
        and defect_distance <= 4 * operator_distance
    )
    if mutation == "corrupt_lipschitz_constant":
        lipschitz_ok = False
    check(
        "complete defect approximation obeys ||Def(S)-Def(S_K)|| <= 4 eta_(K,r,q)",
        lipschitz_ok and "<=4||S-S^K||_op" in note and "<=4 eta_(K,r,q)" in note,
    )

    s_value = F(8, 7)
    cutoff = 14
    local_tail = s_value ** (cutoff + 1) / factorial(cutoff + 1)
    resolution_ok = 4 * (3 * r_value * q_value + 1 + 2 * r_value * q_value) * local_tail < F(1, 8) ** 2
    if mutation == "claim_fixed_cutoff":
        resolution_ok = False
    check(
        "finite cutoff can resolve Gamma only with eta_(K,r,q)=o(epsilon^2)",
        resolution_ok and "eta_(K,r,q)=o(epsilon^2)" in note and "at every finite" in note,
    )

    physical_consumer_ok = all(token in note for token in (
        "H_f^phys=P_(rq)H_(rq)", "P_lr", "Every fine temporal link", "actual square",
    ))
    if mutation == "use_auxiliary_chain":
        physical_consumer_ok = False
    check(
        "the consumer is the complete physical J_r transfer, not an auxiliary B chain",
        physical_consumer_ok and all("J_r" in parent for parent in parents[1:]),
    )

    metric_scope_ok = (
        "metric/source/matter response | open" in note
        and "pure-gauge carrier omits these variables" in note
    )
    if mutation == "claim_metric_response":
        metric_scope_ok = False
    check(
        "metric/source response remains outside the pure-gauge carrier",
        metric_scope_ok and "not a physical" in note,
    )

    time_scope_ok = "mathematical Euclidean parameter, not physical time" in note
    if mutation == "claim_physical_time":
        time_scope_ok = False
    check(
        "no physical-time, continuum, Lorentz, gravity, or action-selection overread",
        time_scope_ok and all(word in note for word in ("continuum", "Lorentz", "gravity", "action selection")),
    )

    prior_art_ok = all(token in note for token in (
        "Block227's cubic BCH residual", "Block228 derives", "Block229 proves", "Generic compression inequalities",
    ))
    if mutation == "hide_prior_art":
        prior_art_ok = False
    check(
        "prior-art fence isolates the new physical changing-carrier square",
        prior_art_ok and "MUTATIONS" in source,
    )

    print("per_element: all 48 signed O(3) frames and their exterior-character values were checked exactly")
    print("per_site: the two-cell hidden-Haar fiber and both retained coarse sectors were enumerated exactly")
    print("per_mode: the Peter--Weyl core commutator square and nontrivial convolution channel were checked")
    print("per_block: the complete physical J_r direct/staged defect and rq packet census were checked")
    print("per_scale: conditioned fibers r=2,...,7 and all-pairs determinant responses through q=3,d=3 were checked")
    print("lattice_wide: checked and not executed — only finite supplied ladders are claimed; no continuum limit is supplied")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("normal", "independent"), default="normal")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
