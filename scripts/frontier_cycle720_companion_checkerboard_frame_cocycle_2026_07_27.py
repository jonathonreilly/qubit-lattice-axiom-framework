#!/usr/bin/env python3
"""Cycle-720 local correction for the companion channel frame-sign defect.

The literal two-cube Stinespring runner found that the bare proper-cubic
coordinate action preserves the binary Choi domain but misses 504 signs.
This runner does not repair that finite circuit by decoder conjugation.
Instead it asks whether one translation-compatible, cell-local Pauli
correction can repair the signed Choi action on adjacent cubes and held
rectangular boxes.

The candidate correction has six possible checkerboard sheets: for each
companion axis and each local coframe value, apply Z on that cell's companion
qubit.  Coefficients are solved jointly on two overlapping 2x2x2 cubes for
every proper-cubic frame and all eight affine-translation parities, then
tested without refit on larger boxes and under frame composition.  The
period-two origin is not fixed: three cell bits with nearest-neighbour
alternation constraints leave all eight origin sectors as gauge choices.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md"
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from dataclasses import replace
from hashlib import sha256
from itertools import product as cartesian_product
import json

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O
import frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27 as C
import frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27 as S
import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712


Pauli = M.Pauli
Coord = tuple[int, int, int]
AffineKey = tuple[tuple[tuple[int, int, int], ...], tuple[int, int, int]]


def frame_tuple(frame: np.ndarray) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(int(value) for value in row) for row in frame)


def affine_cells(
    cells: tuple[Coord, ...], frame: np.ndarray, shift: Coord
) -> tuple[Coord, ...]:
    return tuple(sorted(
        tuple(int(value) for value in (
            frame @ np.asarray(cell, dtype=int) + np.asarray(shift, dtype=int)
        ))
        for cell in cells
    ))


def direction_permutation(frame: np.ndarray) -> tuple[int, ...]:
    return S.direction_permutation(frame)


def matter_images(
    source: M.CompanionFixture,
    target: M.CompanionFixture,
    frame: np.ndarray,
    shift: Coord,
):
    lookup = {cell: index for index, cell in enumerate(target.cells)}
    direction_map = direction_permutation(frame)
    majorana_map = []
    for cell in source.cells:
        mapped_cell = tuple(int(value) for value in (
            frame @ np.asarray(cell, dtype=int) + np.asarray(shift, dtype=int)
        ))
        target_cell = lookup[mapped_cell]
        for mode in range(6):
            target_mode = 6 * target_cell + direction_map[mode]
            majorana_map.extend((2 * target_mode, 2 * target_mode + 1))
    return S.block_majorana_images(
        source.matter_qubits, 0, 0, tuple(majorana_map)
    )


def physical_images(
    source: M.CompanionFixture,
    target: M.CompanionFixture,
    frame: np.ndarray,
    shift: Coord,
):
    lookup = {cell: index for index, cell in enumerate(target.cells)}
    direction_map = direction_permutation(frame)
    x_images = [None] * source.qubits
    z_images = [None] * source.qubits
    matter_majorana_map = tuple(
        item for mode in direction_map for item in (2 * mode, 2 * mode + 1)
    )
    for source_cell, cell in enumerate(source.cells):
        mapped_cell = tuple(int(value) for value in (
            frame @ np.asarray(cell, dtype=int) + np.asarray(shift, dtype=int)
        ))
        target_cell = lookup[mapped_cell]
        matter_x, matter_z = S.block_majorana_images(
            6, 6 * source_cell, 6 * target_cell, matter_majorana_map
        )
        for mode in range(6):
            x_images[6 * source_cell + mode] = matter_x[mode]
            z_images[6 * source_cell + mode] = matter_z[mode]
        companion_x, companion_z = S.block_majorana_images(
            3,
            source.matter_qubits + 3 * source_cell,
            target.matter_qubits + 3 * target_cell,
            direction_map,
        )
        for axis in range(3):
            source_qubit = source.matter_qubits + 3 * source_cell + axis
            x_images[source_qubit] = companion_x[axis]
            z_images[source_qubit] = companion_z[axis]
    if any(row is None for row in x_images + z_images):
        raise AssertionError("incomplete physical frame map")
    return tuple(x_images), tuple(z_images)


def product(rows) -> Pauli:
    output = Pauli()
    for row in rows:
        output = output @ row
    return output


def signed_membership(
    row: Pauli, basis: tuple[Pauli, ...], qubits: int
) -> tuple[Pauli | None, int | None]:
    combination = U.span_combination(
        row.symplectic(qubits),
        tuple(item.symplectic(qubits) for item in basis),
    )
    if combination is None:
        return None, None
    replay = product(
        basis[index]
        for index in range(len(basis))
        if (combination >> index) & 1
    )
    return replay, combination


def sheet_rows(fixture: M.CompanionFixture) -> tuple[Pauli, ...]:
    output = []
    for axis in range(3):
        for parity in range(2):
            z = 0
            for cell_index, cell in enumerate(fixture.cells):
                if cell[axis] % 2 == parity:
                    z |= 1 << (fixture.matter_qubits + 3 * cell_index + axis)
            output.append(Pauli(z=z))
    return tuple(output)


def anticommutes(left: Pauli, right: Pauli) -> int:
    return (
        ((left.x & right.z) ^ (left.z & right.x)).bit_count() & 1
    )


def translated_factor(
    fixture: M.CompanionFixture,
    cache: dict[tuple, O.Factorization],
) -> O.Factorization:
    minimum = tuple(min(cell[axis] for cell in fixture.cells) for axis in range(3))
    normalized = tuple(sorted(tuple(
        cell[axis] - minimum[axis] for axis in range(3)
    ) for cell in fixture.cells))
    axis_edges = tuple(
        (left, right, axis, left_mode % 6, right_mode % 6)
        for left, right, _owner, axis, left_mode, right_mode in fixture.edges
    )
    key = (normalized, axis_edges)
    if key not in cache:
        cache[key] = O.build_factorization(fixture)
        return cache[key]
    return replace(cache[key], fixture=fixture)


def transformed_rows_and_equations(
    source: M.CompanionFixture,
    source_factor: O.Factorization,
    target: M.CompanionFixture,
    target_factor: O.Factorization,
    frame: np.ndarray,
    shift: Coord,
):
    output_images = physical_images(source, target, frame, shift)
    input_images = matter_images(source, target, frame, shift)
    target_basis = C.channel_graph_rows(
        target, target_factor, set(target.cells), target, True
    )
    choi_qubits = target.qubits + target.matter_qubits
    sheets = sheet_rows(target)
    domain, local_qubits = O.reduced_channel_domain(
        source_factor, tuple(source.cells)
    )
    transformed = []
    equations = []
    binary_failures = 0
    odd_phase_failures = 0
    bare_signed_failures = 0
    for vector in domain:
        local_output = F.canonical_pauli(
            O.embed_local_vector(vector, local_qubits, source.qubits),
            source.qubits,
        )
        pulled = O.target_pullback(
            source_factor,
            vector,
            local_qubits,
            False,
            retain_patch_parity=True,
        )
        mapped_output = S.apply_images(S.cpauli(local_output), output_images)
        mapped_input = S.apply_images(S.cpauli(pulled), input_images)
        row = C.choi_pauli(
            Pauli(mapped_output.phase, mapped_output.x, mapped_output.z),
            Pauli(mapped_input.phase, mapped_input.x, mapped_input.z),
            target.qubits,
        )
        replay, _combination = signed_membership(row, target_basis, choi_qubits)
        if replay is None:
            binary_failures += 1
            continue
        delta = (replay.phase - row.phase) % 4
        bare_signed_failures += delta != 0
        if delta not in (0, 2):
            odd_phase_failures += 1
            continue
        mask = sum(
            anticommutes(sheet, Pauli(
                mapped_output.phase, mapped_output.x, mapped_output.z
            )) << index
            for index, sheet in enumerate(sheets)
        )
        equations.append((mask, delta // 2))
        transformed.append((row, replay, mask))
    return {
        "domain_rank": len(domain),
        "target_basis_rank": len(target_basis),
        "binary_failures": binary_failures,
        "odd_phase_failures": odd_phase_failures,
        "bare_signed_failures": bare_signed_failures,
        "equations": tuple(equations),
        "transformed": tuple(transformed),
    }


def solve_affine(
    source_fixtures: tuple[M.CompanionFixture, ...],
    source_factors: tuple[O.Factorization, ...],
    frame: np.ndarray,
    shift: Coord,
    factor_cache: dict[tuple, O.Factorization],
):
    contexts = []
    equations = []
    for source, source_factor in zip(source_fixtures, source_factors):
        target = O.arbitrary_fixture(affine_cells(source.cells, frame, shift))
        target_factor = translated_factor(target, factor_cache)
        context = transformed_rows_and_equations(
            source, source_factor, target, target_factor, frame, shift
        )
        contexts.append(context)
        equations.extend(context["equations"])
    solution, rank, contradictions = F.C.gf2_solve(tuple(equations))
    corrected_failures = sum(
        ((mask & solution).bit_count() & 1)
        != ((replay.phase - row.phase) % 4) // 2
        for context in contexts
        for row, replay, mask in context["transformed"]
    )
    uniform_sheet_visibility_failures = sum(
        (mask & (3 << (2 * axis))).bit_count() & 1
        for context in contexts
        for mask, _rhs in context["equations"]
        for axis in range(3)
    )
    return {
        "solution": solution,
        "equation_rank": rank,
        "contradictions": contradictions,
        "contexts": len(contexts),
        "domain_rows": sum(context["domain_rank"] for context in contexts),
        "binary_failures": sum(context["binary_failures"] for context in contexts),
        "odd_phase_failures": sum(context["odd_phase_failures"] for context in contexts),
        "bare_signed_failures": sum(context["bare_signed_failures"] for context in contexts),
        "corrected_signed_failures": corrected_failures,
        "uniform_sheet_channel_visibility_failures": (
            uniform_sheet_visibility_failures
        ),
    }


def shape_cells(shape: tuple[int, int, int], origin=(0, 0, 0)):
    return tuple(
        (origin[0] + x, origin[1] + y, origin[2] + z)
        for x in range(shape[0])
        for y in range(shape[1])
        for z in range(shape[2])
    )


def predicted_sheet_solution(frame: np.ndarray) -> int:
    """Select the odd coframe sheet for each negatively oriented target axis."""
    return sum(
        1 << (2 * axis + 1)
        for axis in range(3)
        if -1 in tuple(int(value) for value in frame[axis])
    )


def coframe_constraint_certificate(
    shapes: tuple[tuple[int, int, int], ...]
) -> dict[str, object]:
    rows = []
    for shape in shapes:
        fixture = O.arbitrary_fixture(shape_cells(shape))
        equations = []
        for left, right, _owner, edge_axis, *_rest in fixture.edges:
            for coframe_axis in range(3):
                equations.append((
                    (1 << (3 * left + coframe_axis))
                    | (1 << (3 * right + coframe_axis)),
                    int(edge_axis == coframe_axis),
                ))
        solution, rank, contradictions = F.C.gf2_solve(tuple(equations))
        formula_failures = 0
        for seed in cartesian_product(range(2), repeat=3):
            assignment = sum(
                ((cell[axis] % 2) ^ seed[axis])
                << (3 * cell_index + axis)
                for cell_index, cell in enumerate(fixture.cells)
                for axis in range(3)
            )
            formula_failures += any(
                ((mask & assignment).bit_count() & 1) != rhs
                for mask, rhs in equations
            )
        flipped = list(equations)
        flipped[0] = (flipped[0][0], flipped[0][1] ^ 1)
        _bad_solution, _bad_rank, flipped_contradictions = F.C.gf2_solve(
            tuple(flipped)
        )
        rows.append({
            "shape": shape,
            "cells": len(fixture.cells),
            "local_edge_equations": len(equations),
            "equation_rank": rank,
            "expected_connected_rank": 3 * (len(fixture.cells) - 1),
            "contradictions": contradictions,
            "solution_dimension": 3 * len(fixture.cells) - rank,
            "explicit_eight_seed_formula_failures": formula_failures,
            "flip_one_local_edge_rhs_contradictions": flipped_contradictions,
            "solver_seed": solution,
        })
    return {
        "per_shape": tuple(rows),
        "rank_failures": sum(
            row["equation_rank"] != row["expected_connected_rank"]
            for row in rows
        ),
        "contradictions": sum(row["contradictions"] for row in rows),
        "solution_dimension_failures": sum(
            row["solution_dimension"] != 3 for row in rows
        ),
        "seed_formula_failures": sum(
            row["explicit_eight_seed_formula_failures"] for row in rows
        ),
        "flipped_rhs_detection_failures": sum(
            row["flip_one_local_edge_rhs_contradictions"] == 0
            for row in rows
        ),
        "interpretation": (
            "three cell bits obey nearest-neighbour alternation; the eight "
            "global origin choices are the complete solution space and are "
            "not fixed by any local constraint"
        ),
    }


def corrected_images(
    source: M.CompanionFixture,
    target: M.CompanionFixture,
    frame: np.ndarray,
    shift: Coord,
    solution: int,
):
    bare = physical_images(source, target, frame, shift)
    sheets = sheet_rows(target)
    correction = product(
        sheets[index] for index in range(6) if (solution >> index) & 1
    )
    return tuple(tuple(
        type(row)(
            (row.phase + 2 * anticommutes(correction, Pauli(row.phase, row.x, row.z))) % 4,
            row.x,
            row.z,
        )
        for row in rows
    ) for rows in bare)


def images_equal(left, right) -> bool:
    return all(
        (a.phase % 4, a.x, a.z) == (b.phase % 4, b.x, b.z)
        for left_rows, right_rows in zip(left, right)
        for a, b in zip(left_rows, right_rows)
    )


def affine_composition_certificate(
    base: M.CompanionFixture,
    frames: tuple[np.ndarray, ...],
    solutions: dict[tuple[int, Coord], int],
) -> dict[str, object]:
    frame_keys = tuple(frame_tuple(frame) for frame in frames)
    frame_index = {key: index for index, key in enumerate(frame_keys)}
    shifts = tuple(cartesian_product(range(2), repeat=3))
    exact_representative_failures = 0
    binary_failures = 0
    odd_phase_failures = 0
    uniform_fit_contradictions = 0
    nonzero_uniform_residuals = 0
    residual_histogram: dict[int, int] = {}
    unit_translation_product_failures = 0
    identity_index = frame_index[frame_tuple(np.eye(3, dtype=int))]
    for left_id, left_frame in enumerate(frames):
        for right_id, right_frame in enumerate(frames):
            product_frame = left_frame @ right_frame
            product_id = frame_index[frame_tuple(product_frame)]
            for left_shift in shifts:
                for right_shift in shifts:
                    middle = O.arbitrary_fixture(affine_cells(
                        base.cells, right_frame, right_shift
                    ))
                    product_shift_array = (
                        left_frame @ np.asarray(right_shift, dtype=int)
                        + np.asarray(left_shift, dtype=int)
                    )
                    product_shift = tuple(
                        int(value) for value in product_shift_array
                    )
                    product_shift_key = tuple(
                        value % 2 for value in product_shift
                    )
                    final = O.arbitrary_fixture(affine_cells(
                        base.cells, product_frame, product_shift
                    ))
                    right_action = corrected_images(
                        base,
                        middle,
                        right_frame,
                        right_shift,
                        solutions[(right_id, right_shift)],
                    )
                    left_action = corrected_images(
                        middle,
                        final,
                        left_frame,
                        left_shift,
                        solutions[(left_id, left_shift)],
                    )
                    direct_action = corrected_images(
                        base,
                        final,
                        product_frame,
                        product_shift,
                        solutions[(product_id, product_shift_key)],
                    )
                    composed = S.compose_images(left_action, right_action)
                    exact_failure = not images_equal(composed, direct_action)
                    exact_representative_failures += exact_failure
                    if left_id == identity_index and right_id == identity_index:
                        unit_translation_product_failures += exact_failure
                    sheets = sheet_rows(final)
                    uniform = tuple(
                        sheets[2 * axis] @ sheets[2 * axis + 1]
                        for axis in range(3)
                    )
                    equations = []
                    for composed_rows, direct_rows in zip(
                        composed, direct_action
                    ):
                        for actual, expected in zip(
                            composed_rows, direct_rows
                        ):
                            if (actual.x, actual.z) != (expected.x, expected.z):
                                binary_failures += 1
                                continue
                            delta = (actual.phase - expected.phase) % 4
                            if delta not in (0, 2):
                                odd_phase_failures += 1
                                continue
                            equations.append((
                                sum(
                                    anticommutes(
                                        row,
                                        Pauli(
                                            expected.phase,
                                            expected.x,
                                            expected.z,
                                        ),
                                    ) << axis
                                    for axis, row in enumerate(uniform)
                                ),
                                delta // 2,
                            ))
                    residual, _rank, contradictions = F.C.gf2_solve(
                        tuple(equations)
                    )
                    uniform_fit_contradictions += contradictions
                    nonzero_uniform_residuals += residual != 0
                    residual_histogram[residual] = (
                        residual_histogram.get(residual, 0) + 1
                    )
    return {
        "affine_rotation_translation_products": (
            len(frames) ** 2 * len(shifts) ** 2
        ),
        "exact_fixed_representative_failures": exact_representative_failures,
        "binary_residual_failures": binary_failures,
        "odd_phase_residual_failures": odd_phase_failures,
        "uniform_coframe_gauge_fit_contradictions": uniform_fit_contradictions,
        "nonzero_uniform_coframe_gauge_residuals": nonzero_uniform_residuals,
        "uniform_residual_histogram": residual_histogram,
        "pure_translation_products": len(shifts) ** 2,
        "pure_translation_product_failures": unit_translation_product_failures,
        "quotient_affine_product_failures": (
            binary_failures + odd_phase_failures + uniform_fit_contradictions
        ),
        "boundary": (
            "one fixed checkerboard representative is not an exact affine "
            "representation; every residual is exactly one of the eight "
            "uniform coframe-origin gauge transformations"
        ),
    }


def transported_seed(
    frame: np.ndarray, shift: Coord, seed: Coord
) -> Coord:
    value = (
        np.abs(frame) @ np.asarray(seed, dtype=int)
        + np.asarray(shift, dtype=int)
    ) % 2
    return tuple(int(item) for item in value)


def seeded_sheet_solution(
    frame: np.ndarray, base_solution: int, target_seed: Coord
) -> int:
    output = base_solution
    for axis in range(3):
        if (
            -1 in tuple(int(value) for value in frame[axis])
            and target_seed[axis]
        ):
            output ^= 3 << (2 * axis)
    return output


def uniform_origin_direct_sum_certificate(
    base: M.CompanionFixture,
    frames: tuple[np.ndarray, ...],
    solutions: dict[tuple[int, Coord], int],
) -> dict[str, object]:
    """Execute the eight-origin gauge as a retained classical direct sum.

    Each origin sector is a locally constrained coframe basis state.  The
    frame permutes those sectors, while at most three onsite controlled-Zs per
    cell apply the signed companion correction.  Equality of the signed
    Clifford images in every block proves equality of density/Choi channels;
    block-global phases are irrelevant and no coherent-origin claim is made.
    """
    shifts = tuple(cartesian_product(range(2), repeat=3))
    frame_keys = tuple(frame_tuple(frame) for frame in frames)
    frame_index = {key: index for index, key in enumerate(frame_keys)}
    identity_index = frame_index[frame_tuple(np.eye(3, dtype=int))]

    def multiply(left, right):
        left_id, left_shift = left
        right_id, right_shift = right
        product_frame = frames[left_id] @ frames[right_id]
        product_shift = (
            frames[left_id] @ np.asarray(right_shift, dtype=int)
            + np.asarray(left_shift, dtype=int)
        ) % 2
        return (
            frame_index[frame_tuple(product_frame)],
            tuple(int(value) for value in product_shift),
        )

    rz = np.asarray(((0, -1, 0), (1, 0, 0), (0, 0, 1)), dtype=int)
    cycle = np.asarray(((0, 1, 0), (0, 0, 1), (1, 0, 0)), dtype=int)
    generators = (
        (identity_index, (1, 0, 0)),
        (identity_index, (0, 1, 0)),
        (identity_index, (0, 0, 1)),
        (frame_index[frame_tuple(rz)], (0, 0, 0)),
        (frame_index[frame_tuple(cycle)], (0, 0, 0)),
    )
    elements = tuple(
        (frame_id, shift)
        for frame_id in range(len(frames))
        for shift in shifts
    )
    generated = {(identity_index, (0, 0, 0))}
    frontier = list(generated)
    while frontier:
        right = frontier.pop()
        for left in generators:
            item = multiply(left, right)
            if item not in generated:
                generated.add(item)
                frontier.append(item)

    def action(
        source: M.CompanionFixture,
        target: M.CompanionFixture,
        element,
        actual_shift: Coord,
        target_seed: Coord,
    ):
        frame_id, shift_key = element
        return corrected_images(
            source,
            target,
            frames[frame_id],
            actual_shift,
            seeded_sheet_solution(
                frames[frame_id],
                solutions[(frame_id, shift_key)],
                target_seed,
            ),
        )

    def product_block(left, right, source_seed):
        product_element = multiply(left, right)
        left_id, left_shift = left
        right_id, right_shift = right
        product_id, product_shift_key = product_element
        product_shift = tuple(int(value) for value in (
            frames[left_id] @ np.asarray(right_shift, dtype=int)
            + np.asarray(left_shift, dtype=int)
        ))
        middle = O.arbitrary_fixture(affine_cells(
            base.cells, frames[right_id], right_shift
        ))
        final = O.arbitrary_fixture(affine_cells(
            base.cells, frames[product_id], product_shift
        ))
        middle_seed = transported_seed(
            frames[right_id], right_shift, source_seed
        )
        final_seed = transported_seed(
            frames[left_id], left_shift, middle_seed
        )
        direct_seed = transported_seed(
            frames[product_id], product_shift, source_seed
        )
        right_action = action(
            base, middle, right, right_shift, middle_seed
        )
        left_action = action(
            middle, final, left, left_shift, final_seed
        )
        direct_action = action(
            base,
            final,
            (product_id, product_shift_key),
            product_shift,
            direct_seed,
        )
        return (
            int(final_seed != direct_seed),
            int(not images_equal(
                S.compose_images(left_action, right_action), direct_action
            )),
        )

    generator_product_failures = 0
    seed_transport_failures = 0
    generator_blocks = 0
    for left in generators:
        for right in elements:
            for source_seed in shifts:
                seed_failure, physical_failure = product_block(
                    left, right, source_seed
                )
                seed_transport_failures += seed_failure
                generator_product_failures += physical_failure
                generator_blocks += 1

    rotation_product_failures = 0
    rotation_blocks = 0
    zero = (0, 0, 0)
    for left_id in range(len(frames)):
        for right_id in range(len(frames)):
            for source_seed in shifts:
                seed_failure, physical_failure = product_block(
                    (left_id, zero), (right_id, zero), source_seed
                )
                rotation_product_failures += (
                    seed_failure + physical_failure
                )
                rotation_blocks += 1

    translation_product_failures = 0
    translation_blocks = 0
    for left_shift in shifts:
        for right_shift in shifts:
            for source_seed in shifts:
                seed_failure, physical_failure = product_block(
                    (identity_index, left_shift),
                    (identity_index, right_shift),
                    source_seed,
                )
                translation_product_failures += (
                    seed_failure + physical_failure
                )
                translation_blocks += 1

    # Constraint preservation is checked explicitly on every tested box,
    # affine element, and origin sector using the transported local bits.
    constraint_transport_failures = 0
    constraint_contexts = 0
    for shape in ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2)):
        source = O.arbitrary_fixture(shape_cells(shape))
        for frame_id, frame in enumerate(frames):
            permutation = tuple(
                next(
                    column for column in range(3)
                    if abs(int(frame[axis, column])) == 1
                )
                for axis in range(3)
            )
            for shift in shifts:
                for seed in shifts:
                    target_seed = transported_seed(frame, shift, seed)
                    for cell in source.cells:
                        mapped = tuple(int(value) for value in (
                            frame @ np.asarray(cell, dtype=int)
                            + np.asarray(shift, dtype=int)
                        ))
                        for target_axis, source_axis in enumerate(permutation):
                            source_bit = (cell[source_axis] % 2) ^ seed[source_axis]
                            target_bit = (
                                (mapped[target_axis] % 2)
                                ^ target_seed[target_axis]
                            )
                            constraint_transport_failures += (
                                source_bit != target_bit
                            )
                    constraint_contexts += 1

    negative_axis_counts = tuple(sum(
        -1 in tuple(int(value) for value in frame[axis])
        for axis in range(3)
    ) for frame in frames)
    controlled_word_projection_failures = 0
    controlled_word_coframe_X_failures = 0
    controlled_CZ_counts = []
    controlled_primitive_counts = []
    zero = (0, 0, 0)
    for frame_id, frame in enumerate(frames):
        target = O.arbitrary_fixture(affine_cells(base.cells, frame, zero))
        bare = physical_images(base, target, frame, zero)
        augmented_rows = tuple(bare[0]) + tuple(bare[1])
        word = []
        logical_cz_count = 0
        for axis in range(3):
            if -1 not in tuple(int(value) for value in frame[axis]):
                continue
            for cell in range(len(target.cells)):
                control = target.qubits + 3 * cell + axis
                physical = target.matter_qubits + 3 * cell + axis
                augmented_rows = tuple(C712.append_cz(
                    list(augmented_rows), word, control, physical
                ))
                logical_cz_count += 1
        controlled_CZ_counts.append(logical_cz_count)
        controlled_primitive_counts.append(len(word))
        physical_mask = (1 << target.qubits) - 1
        for target_seed in shifts:
            assignment = sum(
                ((cell_coord[axis] % 2) ^ target_seed[axis])
                << (3 * cell + axis)
                for cell, cell_coord in enumerate(target.cells)
                for axis in range(3)
            )
            expected = corrected_images(
                base,
                target,
                frame,
                zero,
                seeded_sheet_solution(
                    frame,
                    solutions[(frame_id, zero)],
                    target_seed,
                ),
            )
            expected_rows = tuple(expected[0]) + tuple(expected[1])
            for actual, target_row in zip(
                augmented_rows, expected_rows
            ):
                controlled_word_coframe_X_failures += bool(
                    actual.x >> target.qubits
                )
                projected = Pauli(
                    (
                        actual.phase
                        + 2 * (((actual.z >> target.qubits) & assignment)
                               .bit_count() & 1)
                    ) % 4,
                    actual.x & physical_mask,
                    actual.z & physical_mask,
                )
                controlled_word_projection_failures += (
                    projected.phase % 4,
                    projected.x,
                    projected.z,
                ) != (
                    target_row.phase % 4,
                    target_row.x,
                    target_row.z,
                )
    return {
        "coframe_origin_sectors_uniformly_retained": 8,
        "affine_group_elements": len(elements),
        "generator_count": len(generators),
        "generated_affine_group_elements": len(generated),
        "generator_product_origin_blocks": generator_blocks,
        "seed_transport_failures": seed_transport_failures,
        "signed_physical_tableau_product_failures": generator_product_failures,
        "uniform_origin_density_Choi_product_failures": (
            seed_transport_failures + generator_product_failures
        ),
        "proper_rotation_product_origin_blocks": rotation_blocks,
        "proper_rotation_density_Choi_product_failures": (
            rotation_product_failures
        ),
        "translation_product_origin_blocks": translation_blocks,
        "translation_density_Choi_product_failures": (
            translation_product_failures
        ),
        "constraint_transport_contexts": constraint_contexts,
        "local_alternation_constraint_transport_failures": (
            constraint_transport_failures
        ),
        "onsite_controlled_Z_per_cell_range": (
            min(negative_axis_counts), max(negative_axis_counts)
        ),
        "two_cube_controlled_Z_gate_count_range": (
            8 * min(negative_axis_counts),
            8 * max(negative_axis_counts),
        ),
        "compiled_controlled_Z_count_range": (
            min(controlled_CZ_counts), max(controlled_CZ_counts)
        ),
        "compiled_controlled_Z_primitive_gate_count_range": (
            min(controlled_primitive_counts),
            max(controlled_primitive_counts),
        ),
        "compiled_controlled_word_coframe_X_failures": (
            controlled_word_coframe_X_failures
        ),
        "compiled_controlled_word_sector_projection_failures": (
            controlled_word_projection_failures
        ),
        "physical_word": (
            "permute the three coframe bits with the port frame, apply affine "
            "bit complements for unit translations, perform the bare frame "
            "word, then apply one onsite CZ(coframe_axis, companion_axis) for "
            "each negatively oriented target axis"
        ),
        "density_boundary": (
            "the uniform mixture over all eight retained coframe code sectors "
            "is an executed block-diagonal density/Choi channel; coherent "
            "off-diagonal origin phases are not claimed"
        ),
    }


def main() -> None:
    frames = tuple(T.proper_cubic_frames())
    frame_keys = tuple(frame_tuple(frame) for frame in frames)
    frame_index = {key: index for index, key in enumerate(frame_keys)}
    shifts = tuple(cartesian_product(range(2), repeat=3))
    left = O.arbitrary_fixture(shape_cells((2, 2, 2)))
    right = O.arbitrary_fixture(shape_cells((2, 2, 2), (1, 0, 0)))
    factor_cache: dict[tuple, O.Factorization] = {}
    left_factor = translated_factor(left, factor_cache)
    right_factor = translated_factor(right, factor_cache)
    source_fixtures = (left, right)
    source_factors = (left_factor, right_factor)

    solutions: dict[tuple[int, Coord], int] = {}
    fit_rows = []
    for frame_id, frame in enumerate(frames):
        for shift in shifts:
            result = solve_affine(
                source_fixtures,
                source_factors,
                frame,
                shift,
                factor_cache,
            )
            solutions[(frame_id, shift)] = result["solution"]
            fit_rows.append({
                "frame": frame_id,
                "shift_mod2": shift,
                **result,
            })
    formula_solution_failures = sum(
        row["solution"] != predicted_sheet_solution(frames[row["frame"]])
        for row in fit_rows
    )
    shift_dependence_failures = sum(
        len({
            row["solution"] for row in fit_rows if row["frame"] == frame_id
        }) != 1
        for frame_id in range(len(frames))
    )

    # The correction is a single global sheet Pauli.  Restricting it from the
    # two independently constructed target cubes to their mapped four-cell
    # overlap must give the same local Pauli.
    overlap_restriction_failures = 0
    for frame_id, frame in enumerate(frames):
        for shift in shifts:
            solution = solutions[(frame_id, shift)]
            targets = tuple(
                O.arbitrary_fixture(affine_cells(source.cells, frame, shift))
                for source in source_fixtures
            )
            mapped_overlap = set(targets[0].cells) & set(targets[1].cells)
            restrictions = []
            for target in targets:
                sheets = sheet_rows(target)
                correction = product(
                    sheets[index]
                    for index in range(6)
                    if (solution >> index) & 1
                )
                lookup = {cell: index for index, cell in enumerate(target.cells)}
                tagged = tuple(
                    (
                        cell,
                        tuple(
                            (correction.z >> (
                                target.matter_qubits + 3 * lookup[cell] + axis
                            )) & 1
                            for axis in range(3)
                        ),
                    )
                    for cell in sorted(mapped_overlap)
                )
                restrictions.append(tagged)
            overlap_restriction_failures += restrictions[0] != restrictions[1]

    # No-refit held boxes at zero affine shift.
    held_rows = []
    for shape in ((3, 2, 2), (3, 3, 2), (5, 3, 2)):
        source = O.arbitrary_fixture(shape_cells(shape))
        source_factor = translated_factor(source, factor_cache)
        for frame_id, frame in enumerate(frames):
            shift = (0, 0, 0)
            target = O.arbitrary_fixture(affine_cells(source.cells, frame, shift))
            target_factor = translated_factor(target, factor_cache)
            context = transformed_rows_and_equations(
                source, source_factor, target, target_factor, frame, shift
            )
            solution = solutions[(frame_id, shift)]
            corrected = sum(
                ((mask & solution).bit_count() & 1)
                != ((replay.phase - row.phase) % 4) // 2
                for row, replay, mask in context["transformed"]
            )
            held_rows.append({
                "shape": shape,
                "frame": frame_id,
                "domain_rank": context["domain_rank"],
                "binary_failures": context["binary_failures"],
                "odd_phase_failures": context["odd_phase_failures"],
                "bare_signed_failures": context["bare_signed_failures"],
                "corrected_signed_failures": corrected,
                "uniform_sheet_channel_visibility_failures": sum(
                    (mask & (3 << (2 * axis))).bit_count() & 1
                    for mask, _rhs in context["equations"]
                    for axis in range(3)
                ),
            })

    # Exact 24x24 composition at zero translation on the base cube.
    product_failures = 0
    for left_id, left_frame in enumerate(frames):
        for right_id, right_frame in enumerate(frames):
            middle = O.arbitrary_fixture(affine_cells(
                left.cells, right_frame, (0, 0, 0)
            ))
            final = O.arbitrary_fixture(affine_cells(
                middle.cells, left_frame, (0, 0, 0)
            ))
            product_frame = left_frame @ right_frame
            product_id = frame_index[frame_tuple(product_frame)]
            right_action = corrected_images(
                left,
                middle,
                right_frame,
                (0, 0, 0),
                solutions[(right_id, (0, 0, 0))],
            )
            left_action = corrected_images(
                middle,
                final,
                left_frame,
                (0, 0, 0),
                solutions[(left_id, (0, 0, 0))],
            )
            product_action = corrected_images(
                left,
                final,
                product_frame,
                (0, 0, 0),
                solutions[(product_id, (0, 0, 0))],
            )
            product_failures += not images_equal(
                S.compose_images(left_action, right_action), product_action
            )

    coframe = coframe_constraint_certificate(
        ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
    )
    affine_composition = affine_composition_certificate(
        left, frames, solutions
    )
    uniform_origin = uniform_origin_direct_sum_certificate(
        left, frames, solutions
    )

    report = {
        "status": "cycle720-checkerboard-local-frame-correction",
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "fit": {
            "proper_cubic_frames": len(frames),
            "affine_translation_parities": len(shifts),
            "adjacent_overlapping_cubes_per_fit": 2,
            "total_contexts": len(fit_rows) * 2,
            "total_domain_rows": sum(row["domain_rows"] for row in fit_rows),
            "binary_failures": sum(row["binary_failures"] for row in fit_rows),
            "odd_phase_failures": sum(row["odd_phase_failures"] for row in fit_rows),
            "bare_signed_failures": sum(row["bare_signed_failures"] for row in fit_rows),
            "fit_contradictions": sum(row["contradictions"] for row in fit_rows),
            "corrected_signed_failures": sum(row["corrected_signed_failures"] for row in fit_rows),
            "equation_rank_range": (
                min(row["equation_rank"] for row in fit_rows),
                max(row["equation_rank"] for row in fit_rows),
            ),
            "solution_weight_range": (
                min(row["solution"].bit_count() for row in fit_rows),
                max(row["solution"].bit_count() for row in fit_rows),
            ),
            "closed_form_negative_target_axis_rule_failures": (
                formula_solution_failures
            ),
            "solution_changes_across_eight_affine_shifts": (
                shift_dependence_failures
            ),
            "uniform_sheet_channel_visibility_failures": sum(
                row["uniform_sheet_channel_visibility_failures"]
                for row in fit_rows
            ),
            "solutions_by_frame_and_shift": tuple(fit_rows),
        },
        "overlap": {
            "shared_cells_per_adjacent_cube_pair": 4,
            "local_coframe_sheet_restriction_failures": overlap_restriction_failures,
        },
        "held": {
            "shapes": ((3, 2, 2), (3, 3, 2), (5, 3, 2)),
            "total_contexts": len(held_rows),
            "total_domain_rows": sum(row["domain_rank"] for row in held_rows),
            "binary_failures": sum(row["binary_failures"] for row in held_rows),
            "odd_phase_failures": sum(row["odd_phase_failures"] for row in held_rows),
            "bare_signed_failures": sum(row["bare_signed_failures"] for row in held_rows),
            "corrected_signed_failures": sum(row["corrected_signed_failures"] for row in held_rows),
            "uniform_sheet_channel_visibility_failures": sum(
                row["uniform_sheet_channel_visibility_failures"]
                for row in held_rows
            ),
            "per_context": tuple(held_rows),
        },
        "composition": {
            "ordered_frame_products": len(frames) ** 2,
            "corrected_physical_image_product_failures": product_failures,
        },
        "local_coframe_gauge": coframe,
        "affine_composition": affine_composition,
        "uniform_eight_origin_physical_channel": uniform_origin,
        "supplied": [
            "the landed proper-cubic action on cell coordinates and six matter ports",
            "the local three-companion-qubit frame action",
            "the existing parity-superselected companion channel domain",
            "three auxiliary coframe bits per cell constrained by local nearest-neighbour alternation",
            "a nonselected uniform classical mixture over the eight coframe-origin sectors with the coframe output retained",
        ],
        "derived": [
            "the fitted correction is the closed-form rule: select the target-axis coframe bit exactly when that frame row has negative orientation",
            "signed Choi repair by cell-local companion-Z conjugations only",
            "shared-cell restriction equality and no-refit held-box tests",
            "the local coframe constraints leave exactly eight unfixed origin sectors and every sector acts identically on the declared channel",
            "pure translations compose exactly; mixed affine products close exactly modulo the locally invisible coframe-origin gauge",
            "the uniform eight-origin retained density/Choi channel has an exact signed representation generated by three unit translations and two proper rotations",
            "the physical frame word uses at most three onsite coframe-controlled companion-Z gates per cell and preserves every local alternation relation",
        ],
        "open": [
            "decide whether the three-bit locally constrained coframe can be identified with existing port/gauge data rather than retained as auxiliary structure",
            "integrate the executed coframe-controlled frame word with the recurrent Stinespring update tile and retest routed gate words",
            "derive autonomous genesis of the local coframe constraints and uniform eight-origin mixture",
            "autonomously prepare the pure gauge references and parity environment",
        ],
        "claim_ceiling": (
            "This closes the signed proper-cubic/translation action on the "
            "declared uniform eight-origin coframe density/Choi channel with a "
            "bounded onsite controlled correction. A fixed representative "
            "closes only modulo origin gauge. It is not by itself a recurrent "
            "update circuit or autonomous-genesis theorem."
        ),
        "no_go_discipline": {
            "N1_alternatives": "edge-local corrections, coframe-free doubled cells, and gauge-covariant frame transport remain live",
            "N2_wall_independence": "signed covariance is separated from recurrent execution and ancilla genesis",
            "N3_hidden_imports": "three coframe bits per cell, their NN constraints, and the frame/port action are explicit",
            "N4_residual_matching": "binary domain, phase parity, signed fit, overlap, held sizes, fixed-representative products, and gauge-quotient products are separate",
            "N5_resolution": "all 24 frames, eight translation parities, adjacent cubes, three held boxes, 576 rotations, 36,864 quotient products, and 7,680 retained-origin generator blocks spanning all 192 affine elements",
            "N6_partial_closure": "retain any passing local correction without promoting recurrent or autonomous closure",
            "N7_steelman": "the observed checkerboard sheet is the smallest constructive repair found so far",
            "N8_cross_cycle_echo": "directly attacks the 504 bare-sign failures left by the finite Stinespring runner",
            "gate": "FAIL_for_broad_no_go__constructive_local_route_active",
        },
    }
    report["pass"] = (
        report["fit"]["binary_failures"] == 0
        and report["fit"]["odd_phase_failures"] == 0
        and report["fit"]["fit_contradictions"] == 0
        and report["fit"]["corrected_signed_failures"] == 0
        and report["fit"]["closed_form_negative_target_axis_rule_failures"] == 0
        and report["fit"]["solution_changes_across_eight_affine_shifts"] == 0
        and report["fit"]["uniform_sheet_channel_visibility_failures"] == 0
        and report["overlap"]["local_coframe_sheet_restriction_failures"] == 0
        and report["held"]["binary_failures"] == 0
        and report["held"]["odd_phase_failures"] == 0
        and report["held"]["corrected_signed_failures"] == 0
        and report["held"]["uniform_sheet_channel_visibility_failures"] == 0
        and report["composition"]["corrected_physical_image_product_failures"] == 0
        and report["local_coframe_gauge"]["rank_failures"] == 0
        and report["local_coframe_gauge"]["contradictions"] == 0
        and report["local_coframe_gauge"]["solution_dimension_failures"] == 0
        and report["local_coframe_gauge"]["seed_formula_failures"] == 0
        and report["local_coframe_gauge"]["flipped_rhs_detection_failures"] == 0
        and report["affine_composition"]["pure_translation_product_failures"] == 0
        and report["affine_composition"]["quotient_affine_product_failures"] == 0
        and report["uniform_eight_origin_physical_channel"][
            "generated_affine_group_elements"
        ] == 192
        and report["uniform_eight_origin_physical_channel"][
            "uniform_origin_density_Choi_product_failures"
        ] == 0
        and report["uniform_eight_origin_physical_channel"][
            "proper_rotation_product_origin_blocks"
        ] == 576 * 8
        and report["uniform_eight_origin_physical_channel"][
            "proper_rotation_density_Choi_product_failures"
        ] == 0
        and report["uniform_eight_origin_physical_channel"][
            "translation_product_origin_blocks"
        ] == 64 * 8
        and report["uniform_eight_origin_physical_channel"][
            "translation_density_Choi_product_failures"
        ] == 0
        and report["uniform_eight_origin_physical_channel"][
            "local_alternation_constraint_transport_failures"
        ] == 0
        and report["uniform_eight_origin_physical_channel"][
            "onsite_controlled_Z_per_cell_range"
        ][1] == 3
        and report["uniform_eight_origin_physical_channel"][
            "compiled_controlled_Z_count_range"
        ][1] == 24
        and report["uniform_eight_origin_physical_channel"][
            "compiled_controlled_word_coframe_X_failures"
        ] == 0
        and report["uniform_eight_origin_physical_channel"][
            "compiled_controlled_word_sector_projection_failures"
        ] == 0
    )
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print("CHECKERBOARD_LOCAL_FRAME_CORRECTION_PASS" if report["pass"] else "CHECKERBOARD_LOCAL_FRAME_CORRECTION_INCOMPLETE")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
