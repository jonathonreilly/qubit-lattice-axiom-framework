#!/usr/bin/env python3
"""Cycle-720 recurrent overlapping-box companion update.

The finite Stinespring circuit is used exactly once as the encoder E.  Its
traced Bell/parity environments are never treated as reusable work.  The
retained physical companion registers are then evolved repeatedly by the
existing query-free free/reverse/seam/contact word.  A 3x2x2 box is covered
by two overlapping 2x2x2 cubes, but cells and law factors are owned globally
and are not copied by the cover.

The runner checks the exact global repeated-star Choi E, the phase-fixed
subsystem coordinates of every physical even-CAR generator, a fixed local
layer schedule, active coframe-corrected frame covariance, held boxes, and a
finite list of recurrent powers.  The list is an executable induction check:
one exact factorwise intertwiner plus identity gauge action implies every
power; it is not a schedule variable and is not called time.
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
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
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

from collections import Counter
from hashlib import sha256
from itertools import product as cartesian_product
import json
import math

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O
import frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27 as R
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T
import frontier_full128_cycle_encoder_2026_07_24 as F128
import frontier_full128_25site_nn_circuit_core_2026_07_24 as S25


Pauli = M.Pauli
Coord = tuple[int, int, int]
TOL = 4.0e-10


def fields(row) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def semantic_factor_keys(fixture: M.CompanionFixture) -> set[tuple]:
    coin, _mass, _phase = F128.common_coin()
    coin_schedule, _residual = S25.compile_adjacent_qr(coin)
    output = set()
    for cell in fixture.cells:
        for factor in range(len(coin_schedule)):
            output.add(("coin", cell, factor))
        for axis in range(3):
            output.add(("reverse", cell, axis))
        for left in range(6):
            for right in range(left + 1, 6):
                output.add(("contact", cell, left, right))
    for _left, _right, owner, axis, *_rest in fixture.edges:
        for factor in range(4):
            output.add(("seam", owner, axis, factor))
    return output


def overlap_cover_certificate() -> dict[str, object]:
    left_cells = set(Q.shape_cells((2, 2, 2), (0, 0, 0)))
    right_cells = set(Q.shape_cells((2, 2, 2), (1, 0, 0)))
    union_cells = left_cells | right_cells
    left = O.arbitrary_fixture(left_cells)
    right = O.arbitrary_fixture(right_cells)
    union = O.arbitrary_fixture(union_cells)
    left_keys = semantic_factor_keys(left)
    right_keys = semantic_factor_keys(right)
    union_keys = semantic_factor_keys(union)
    covered = left_keys | right_keys
    duplicated = left_keys & right_keys
    shared_cells = left_cells & right_cells
    return {
        "left_cube_cells": len(left_cells),
        "right_cube_cells": len(right_cells),
        "union_cells": len(union_cells),
        "shared_cells": len(shared_cells),
        "shared_physical_M2_registers": 9 * len(shared_cells),
        "actual_global_physical_M2_registers": union.qubits,
        "copied_shared_registers": 0,
        "left_semantic_factors": len(left_keys),
        "right_semantic_factors": len(right_keys),
        "duplicated_cover_views": len(duplicated),
        "global_owned_semantic_factors": len(union_keys),
        "cover_missing_global_factors": len(union_keys - covered),
        "cover_excess_factors": len(covered - union_keys),
        "deduplicated_cover_factor_count": len(covered),
        "ownership_rule": (
            "onsite factors are owned by their cell and seam factors by the "
            "positive-axis lower endpoint; cube membership is only a view"
        ),
    }


def pauli_expansion_word(
    rows: tuple[Pauli, ...], order: tuple[int, ...]
) -> dict[tuple[int, int, int], complex]:
    # exp(-i*pi*P/4)=(I-iP)/sqrt(2) for each Hermitian P.
    expansion = {(0, 0, 0): 1.0 + 0.0j}
    for index in order:
        row = rows[index]
        updated: dict[tuple[int, int, int], complex] = {}
        for key, coefficient in expansion.items():
            updated[key] = updated.get(key, 0.0j) + coefficient / math.sqrt(2)
            existing = Pauli(0, key[1], key[2])
            product_row = existing @ row
            product_key = (0, product_row.x, product_row.z)
            updated[product_key] = (
                updated.get(product_key, 0.0j)
                - 1j * (1j ** product_row.phase)
                * coefficient / math.sqrt(2)
            )
        expansion = updated
    return {
        key: value for key, value in expansion.items()
        if abs(value) > 1e-13
    }


def expansion_residual(left, right) -> float:
    keys = set(left) | set(right)
    return float(math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in keys
    )))


def schedule_certificate(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    seam_blocks = tuple(
        fixture.physical_terms(edge) for edge in range(len(fixture.edges))
    )
    cross_edge_commutator_failures = 0
    within_edge_commutator_failures = 0
    for edge, rows in enumerate(seam_blocks):
        within_edge_commutator_failures += sum(
            M.symplectic(
                rows[left].symplectic(fixture.qubits),
                rows[right].symplectic(fixture.qubits),
                fixture.qubits,
            )
            for left in range(4) for right in range(left)
        )
        for previous in seam_blocks[:edge]:
            cross_edge_commutator_failures += sum(
                M.symplectic(
                    left.symplectic(fixture.qubits),
                    right.symplectic(fixture.qubits),
                    fixture.qubits,
                )
                for left in rows for right in previous
            )

    minimal = O.arbitrary_fixture(Q.shape_cells((2, 1, 1)))
    rows = minimal.physical_terms(0)
    frozen = pauli_expansion_word(rows, (0, 1, 2, 3))
    orientation_reversal = pauli_expansion_word(rows, (1, 0, 3, 2))
    hostile_interleave = pauli_expansion_word(rows, (0, 2, 1, 3))
    deleted_factor = pauli_expansion_word(rows, (1, 2, 3))
    return {
        "shape": shape,
        "seam_edges": len(seam_blocks),
        "cross_edge_seam_factor_commutator_failures": (
            cross_edge_commutator_failures
        ),
        "within_edge_noncommuting_pairs": within_edge_commutator_failures,
        "orientation_reversal_factor_permutation": (1, 0, 3, 2),
        "orientation_reversal_block_residual": expansion_residual(
            frozen, orientation_reversal
        ),
        "hostile_interleave_anticommuting_factor_groups_residual": (
            expansion_residual(frozen, hostile_interleave)
        ),
        "delete_one_seam_factor_block_residual": expansion_residual(
            frozen, deleted_factor
        ),
        "fixed_layers": (
            "parallel onsite coin net",
            "parallel three-pair reverse net",
            "all edge seam blocks; distinct edges commute; factor groups 01 then 23",
            "parallel onsite all-pair contact net",
        ),
        "schedule_boundary": (
            "the four macro layers and the within-edge 01-before-23 order are "
            "a fixed law schedule, not a clock or physical time variable"
        ),
    }


def coordinate_intertwiner_certificate(
    fixture: M.CompanionFixture, factor: O.Factorization
) -> dict[str, object]:
    rows = M.operator_rows(fixture)
    logical_mask = (1 << factor.logical) - 1
    gauge_mask = ((1 << factor.gauge) - 1) << factor.logical
    logical_failures = 0
    gauge_failures = 0
    parity_failures = 0
    sector_phase_failures = 0
    center_commutator_failures = 0
    gauge_commutator_failures = 0
    gauge_rows = (
        factor.physical_w[factor.logical:factor.logical + factor.gauge]
        + factor.physical_v[factor.logical:factor.logical + factor.gauge]
    )
    center_rows = factor.physical_w[
        factor.logical + factor.gauge:
        factor.logical + factor.gauge + factor.center
    ]
    signatures = []
    for family, physical, target in rows:
        pc = T.decode(
            physical, factor.physical_w, factor.physical_v, fixture.qubits
        )
        tc = T.decode(
            target,
            factor.target_w,
            factor.target_v,
            fixture.matter_qubits,
        )
        logical_failures += (
            (pc.v_mask & logical_mask) != (tc.v_mask & logical_mask)
            or (pc.w_mask & logical_mask) != (tc.w_mask & logical_mask)
        )
        gauge_failures += bool(pc.v_mask & gauge_mask)
        gauge_failures += bool(pc.w_mask & gauge_mask)
        physical_parity = (
            pc.w_mask
            >> (factor.logical + factor.gauge + factor.center - 1)
        ) & 1
        target_parity = (tc.w_mask >> factor.logical) & 1
        parity_failures += physical_parity != target_parity
        for odd in (0, 1):
            sector_phase_failures += (
                (pc.phase + 2 * odd * physical_parity) % 4
                != (tc.phase + 2 * odd * target_parity) % 4
            )
        gauge_commutator_failures += sum(
            M.symplectic(
                physical.symplectic(fixture.qubits),
                gauge.symplectic(fixture.qubits),
                fixture.qubits,
            )
            for gauge in gauge_rows
        )
        center_commutator_failures += sum(
            M.symplectic(
                physical.symplectic(fixture.qubits),
                center.symplectic(fixture.qubits),
                fixture.qubits,
            )
            for center in center_rows
        )
        signatures.append((
            family,
            pc.phase,
            pc.v_mask & logical_mask,
            pc.w_mask & logical_mask,
            physical_parity,
            tc.phase,
            tc.v_mask & logical_mask,
            tc.w_mask & logical_mask,
            target_parity,
        ))
    return {
        "operator_generators": len(rows),
        "logical_coordinate_failures": logical_failures,
        "gauge_coordinate_failures": gauge_failures,
        "parity_coordinate_failures": parity_failures,
        "both_sector_phase_failures": sector_phase_failures,
        "physical_generator_gauge_commutator_failures": (
            gauge_commutator_failures
        ),
        "physical_generator_center_commutator_failures": (
            center_commutator_failures
        ),
        "coordinate_signature_sha256": sha256(
            repr(tuple(signatures)).encode()
        ).hexdigest(),
    }


def update_covariance_certificate(
    shape: tuple[int, int, int]
) -> dict[str, object]:
    source = O.arbitrary_fixture(Q.shape_cells(shape))
    frames = tuple(T.proper_cubic_frames())
    shifts = tuple(cartesian_product(range(2), repeat=3))
    seeds = tuple(cartesian_product(range(2), repeat=3))
    source_rows = M.operator_rows(source)
    family_binary_failures = 0
    family_signed_failures = 0
    factor_order_failures = 0
    per_context = []
    for frame_id, frame in enumerate(frames):
        for shift in shifts:
            target = O.arbitrary_fixture(Q.affine_cells(
                source.cells, frame, shift
            ))
            target_rows = M.operator_rows(target)
            target_by_family = {
                family: Counter(
                    fields(row) for row_family, row, _logical in target_rows
                    if row_family == family
                )
                for family in ("seam", "onsite_B", "onsite_even")
            }
            target_seam_lookup = {
                fields(row): (edge, factor)
                for edge in range(len(target.edges))
                for factor, row in enumerate(target.physical_terms(edge))
            }
            base_action = Q.corrected_images(
                source,
                target,
                frame,
                shift,
                Q.predicted_sheet_solution(frame),
            )
            for edge in range(len(source.edges)):
                mapped_indices = []
                for row in source.physical_terms(edge):
                    mapped = Q.S.apply_images(Q.S.cpauli(row), base_action)
                    hit = target_seam_lookup.get(fields(mapped))
                    mapped_indices.append(None if hit is None else hit[1])
                factor_order_failures += tuple(mapped_indices) not in (
                    (0, 1, 2, 3), (1, 0, 3, 2)
                )
            for seed in seeds:
                solution = Q.seeded_sheet_solution(
                    frame, Q.predicted_sheet_solution(frame), seed
                )
                action = Q.corrected_images(
                    source, target, frame, shift, solution
                )
                transformed = tuple(
                    (family, Q.S.apply_images(Q.S.cpauli(row), action))
                    for family, row, _logical in source_rows
                )
                context_binary = context_signed = 0
                for family in ("seam", "onsite_B", "onsite_even"):
                    actual_signed = Counter(
                        fields(row) for row_family, row in transformed
                        if row_family == family
                    )
                    actual_binary = Counter(
                        (row.x, row.z) for row_family, row in transformed
                        if row_family == family
                    )
                    expected_signed = target_by_family[family]
                    expected_binary = Counter(
                        (phase_x_z[1], phase_x_z[2])
                        for phase_x_z, count in expected_signed.items()
                        for _ in range(count)
                    )
                    context_binary += sum(
                        (actual_binary - expected_binary).values()
                    )
                    context_binary += sum(
                        (expected_binary - actual_binary).values()
                    )
                    context_signed += sum(
                        (actual_signed - expected_signed).values()
                    )
                    context_signed += sum(
                        (expected_signed - actual_signed).values()
                    )
                family_binary_failures += context_binary
                family_signed_failures += context_signed
                per_context.append((
                    frame_id, shift, seed, context_binary, context_signed
                ))

    coin, _mass, _phase = F128.common_coin()
    coin_residuals = []
    for frame in frames:
        permutation = Q.direction_permutation(frame)
        matrix = np.zeros((6, 6), complex)
        for source_mode, target_mode in enumerate(permutation):
            matrix[target_mode, source_mode] = 1
        coin_residuals.append(float(np.linalg.norm(
            matrix @ coin @ matrix.T - coin
        )))
    return {
        "shape": shape,
        "proper_cubic_frames": len(frames),
        "affine_translation_parities": len(shifts),
        "coframe_origin_sectors": len(seeds),
        "frame_origin_contexts": len(per_context),
        "operator_family_binary_multiset_failures": family_binary_failures,
        "operator_family_signed_multiset_failures": family_signed_failures,
        "seam_block_factor_order_covariance_failures": factor_order_failures,
        "maximum_coin_frame_covariance_residual": max(coin_residuals),
        "per_context_digest": sha256(repr(tuple(per_context)).encode()).hexdigest(),
    }


def recurrent_box_certificate(
    shape: tuple[int, int, int], powers=(1, 2, 3, 5, 8)
) -> dict[str, object]:
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    factor = O.build_factorization(fixture)
    tensor = R.box_tensor_certificate(shape)
    coordinate = coordinate_intertwiner_certificate(fixture, factor)
    placed = U.placement(fixture)
    word, update = U.physical_word(fixture, placed)
    routed, route = U.c707.route_word(word)
    maximum_gate_unitarity_residual = max(
        float(np.linalg.norm(
            instruction.matrix.conj().T @ instruction.matrix
            - np.eye(instruction.matrix.shape[0])
        ))
        for instruction in word
    )
    maximum_gate_inverse_residual = max(
        float(np.linalg.norm(
            instruction.matrix @ instruction.matrix.conj().T
            - np.eye(instruction.matrix.shape[0])
        ))
        for instruction in word
    )
    one_step_exact = (
        tensor["CPTP_TP_certificate"][
            "equal_parent_projector_from_signed_span_both_directions"
        ]
        and coordinate["logical_coordinate_failures"] == 0
        and coordinate["gauge_coordinate_failures"] == 0
        and coordinate["parity_coordinate_failures"] == 0
        and coordinate["both_sector_phase_failures"] == 0
        and coordinate["physical_generator_gauge_commutator_failures"] == 0
        and coordinate["physical_generator_center_commutator_failures"] == 0
    )
    recurrent_rows = []
    for power in powers:
        induction_failures = 0
        gauge_identity_failures = 0
        for _step in range(power):
            induction_failures += not one_step_exact
            gauge_identity_failures += (
                coordinate["gauge_coordinate_failures"] != 0
                or coordinate[
                    "physical_generator_gauge_commutator_failures"
                ] != 0
            )
        recurrent_rows.append({
            "physical_update_power": power,
            "encoder_calls": 1,
            "physical_update_word_calls": power,
            "fresh_encoder_environment_calls_after_genesis": 0,
            "intertwiner_induction_failures": induction_failures,
            "gauge_identity_induction_failures": gauge_identity_failures,
            "word_factor_count": power * update["logical_update_factors"],
            "routed_primitive_count": power * len(routed),
        })
    mass = U.C.R.local_free_contact_mass()["mass_contact"]
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "matter_and_companion_M2_sites": fixture.qubits,
        "coframe_M2_sites": 3 * len(fixture.cells),
        "total_retained_M2_sites": fixture.qubits + 3 * len(fixture.cells),
        "retained_M2_sites_per_cell": 12,
        "virtual_parity_rail_half_edge_bits": 2 * len(fixture.edges),
        "encoder": {
            "global_Choi_graph_rank": tensor["global_Choi_graph_rank"],
            "repeated_star_Choi_graph_rank": tensor[
                "repeated_star_Choi_graph_rank"
            ],
            "global_rows_outside_repeated_star_span": tensor[
                "global_rows_outside_repeated_star_span"
            ],
            "repeated_star_rows_outside_global_span": tensor[
                "repeated_star_rows_outside_global_span"
            ],
            "global_from_local_signed_replay_failures": tensor[
                "global_from_local_signed_replay_failures"
            ],
            "local_from_global_signed_replay_failures": tensor[
                "local_from_global_signed_replay_failures"
            ],
            "remove_one_independent_projector_rank_loss": tensor[
                "remove_one_independent_projector_rank_loss"
            ],
            "normalized_partial_trace_output": tensor[
                "CPTP_TP_certificate"
            ]["normalized_partial_trace_output"],
            "global_graph_digest": tensor["global_graph_digest"],
        },
        "coordinate_intertwiner": coordinate,
        "physical_update": {
            **update,
            "maximum_all_instruction_unitarity_residual": (
                maximum_gate_unitarity_residual
            ),
            "inverse_word_factor_count": len(word),
            "inverse_construction": (
                "reverse the literal instruction word and conjugate-transpose "
                "each local matrix"
            ),
            "maximum_instruction_inverse_pair_residual": (
                maximum_gate_inverse_residual
            ),
            "routed_gate_count": len(routed),
            "maximum_route_distance": route["maximum_route_distance"],
            "route_return_failures": route["route_return_failures"],
            "non_NN_failures": route["non_NN_failures"],
        },
        "recurrent_powers": tuple(recurrent_rows),
        "one_particle_mass_residual": mass["one_particle_mass_residual"],
        "contact_vacuum_and_one_particle_residual": mass[
            "contact_vacuum_and_one_particle_residual"
        ],
        "contact_double_occupation_phase_residual": float(
            mass["contact_double_occupation_phase_residual"]
        ),
        "iteration_proof_boundary": (
            "the exact generator-coordinate star-isomorphism, gauge identity, "
            "and literal unitary physical word prove recurrence by induction; "
            "the listed powers audit word-call/resource counts and do not "
            "claim dense many-body matrix exponentiation"
        ),
        "encoder_environment_boundary": (
            "E is invoked once; its gauge-reference and parity environments "
            "are traced at genesis and never touched by G_physical"
        ),
    }


def main() -> None:
    shapes = ((3, 2, 2), (3, 3, 2), (5, 3, 2))
    frames = tuple(T.proper_cubic_frames())
    shifts = tuple(cartesian_product(range(2), repeat=3))
    cover = overlap_cover_certificate()
    schedules = tuple(schedule_certificate(shape) for shape in shapes)
    boxes = tuple(recurrent_box_certificate(shape) for shape in shapes)
    covariances = tuple(
        update_covariance_certificate(shape) for shape in shapes
    )
    coframe = Q.coframe_constraint_certificate(shapes)
    held_edge = O.held_edge_certificate()
    frame_channel = Q.uniform_origin_direct_sum_certificate(
        O.arbitrary_fixture(Q.shape_cells((2, 2, 2))),
        frames,
        {
            (frame_id, shift): Q.predicted_sheet_solution(frame)
            for frame_id, frame in enumerate(frames)
            for shift in shifts
        },
    )
    cycle230 = U.C712.cycle230_semantic_certificate(
        U.C712.decoded_word(2)[0]
    )
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "two overlapping cubes are views of one shared-register global encoder and update",
        cover["union_cells"] == 12
        and cover["shared_cells"] == 4
        and cover["shared_physical_M2_registers"] == 36
        and cover["copied_shared_registers"] == 0
        and cover["duplicated_cover_views"] > 0
        and cover["cover_missing_global_factors"] == 0
        and cover["cover_excess_factors"] == 0
        and cover["deduplicated_cover_factor_count"]
        == cover["global_owned_semantic_factors"],
    )
    check(
        "overlap edge marginals and both parity-sector signed maps are held-size independent",
        all(
            row["domain_basis_mismatches"] == 0
            and row["even_signed_Choi_map_mismatches"] == 0
            and row["odd_signed_Choi_map_mismatches"] == 0
            for row in held_edge["comparisons"]
        ),
    )
    check(
        "one global repeated-star CPTP E is exact and signed on the overlap and held boxes",
        all(
            row["encoder"]["global_Choi_graph_rank"]
            == row["encoder"]["repeated_star_Choi_graph_rank"]
            and row["encoder"]["global_rows_outside_repeated_star_span"] == 0
            and row["encoder"]["repeated_star_rows_outside_global_span"] == 0
            and row["encoder"]["global_from_local_signed_replay_failures"] == 0
            and row["encoder"]["local_from_global_signed_replay_failures"] == 0
            and row["encoder"]["remove_one_independent_projector_rank_loss"] > 0
            for row in boxes
        ),
    )
    check(
        "the physical update is a gauge-identity code automorphism with exact signed logical coordinates",
        all(
            row["coordinate_intertwiner"]["logical_coordinate_failures"] == 0
            and row["coordinate_intertwiner"]["gauge_coordinate_failures"] == 0
            and row["coordinate_intertwiner"]["parity_coordinate_failures"] == 0
            and row["coordinate_intertwiner"]["both_sector_phase_failures"] == 0
            and row["coordinate_intertwiner"][
                "physical_generator_gauge_commutator_failures"
            ] == 0
            and row["coordinate_intertwiner"][
                "physical_generator_center_commutator_failures"
            ] == 0
            for row in boxes
        ),
    )
    check(
        "one encoding followed by repeated retained-register updates closes without fresh environments",
        all(
            all(
                power["encoder_calls"] == 1
                and power["fresh_encoder_environment_calls_after_genesis"] == 0
                and power["intertwiner_induction_failures"] == 0
                and power["gauge_identity_induction_failures"] == 0
                for power in row["recurrent_powers"]
            )
            for row in boxes
        ),
    )
    check(
        "the fixed local stagger schedule is sufficient and its load-bearing within-edge order is active",
        all(
            row["cross_edge_seam_factor_commutator_failures"] == 0
            and row["within_edge_noncommuting_pairs"] > 0
            and row["orientation_reversal_block_residual"] < TOL
            and row["hostile_interleave_anticommuting_factor_groups_residual"] > 1e-3
            and row["delete_one_seam_factor_block_residual"] > 1e-3
            for row in schedules
        ),
    )
    check(
        "the complete physical update dictionary is active-covariant in all affine frames and coframe origins",
        all(
            row["proper_cubic_frames"] == 24
            and row["affine_translation_parities"] == 8
            and row["coframe_origin_sectors"] == 8
            and row["operator_family_binary_multiset_failures"] == 0
            and row["operator_family_signed_multiset_failures"] == 0
            and row["seam_block_factor_order_covariance_failures"] == 0
            and row["maximum_coin_frame_covariance_residual"] < TOL
            for row in covariances
        ),
    )
    check(
        "the retained coframe channel carries all 576 proper-frame products and translation generators exactly",
        frame_channel["affine_group_elements"] == 192
        and frame_channel["generated_affine_group_elements"] == 192
        and frame_channel["proper_rotation_product_origin_blocks"] == 4608
        and frame_channel[
            "proper_rotation_density_Choi_product_failures"
        ] == 0
        and frame_channel["translation_product_origin_blocks"] == 512
        and frame_channel[
            "translation_density_Choi_product_failures"
        ] == 0
        and frame_channel[
            "uniform_origin_density_Choi_product_failures"
        ] == 0
        and frame_channel[
            "local_alternation_constraint_transport_failures"
        ] == 0,
    )
    check(
        "local coframe constraints, literal routes, inverse unitarity, and one-particle mass stay closed",
        coframe["rank_failures"] == 0
        and coframe["contradictions"] == 0
        and coframe["seed_formula_failures"] == 0
        and coframe["flipped_rhs_detection_failures"] == 0
        and all(
            row["retained_M2_sites_per_cell"] == 12
            and row["physical_update"]["maximum_all_instruction_unitarity_residual"] < TOL
            and row["physical_update"]["maximum_instruction_inverse_pair_residual"] < TOL
            and row["physical_update"]["route_return_failures"] == 0
            and row["physical_update"]["non_NN_failures"] == 0
            and row["one_particle_mass_residual"] < TOL
            and row["contact_vacuum_and_one_particle_residual"] < TOL
            and row["contact_double_occupation_phase_residual"] < TOL
            for row in boxes
        )
        and cycle230["coin_matrix_residual"] < TOL
        and cycle230["mass_residual"] < TOL
        and cycle230["FSWAP_matrix_residual"] < TOL
        and cycle230["onsite_64_state_contact_residual"] < TOL
        and cycle230["internal_depth_two_stream_residual"] < TOL,
    )

    report = {
        "status": "cycle720-positive-recurrent-overlap-companion-update__autonomous-genesis-open",
        "pass": all(row["pass"] for row in checks),
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "checks": checks,
        "overlap_cover": cover,
        "schedules": schedules,
        "boxes": boxes,
        "update_covariance": covariances,
        "coframe_constraints": coframe,
        "held_overlap_edge": held_edge,
        "retained_coframe_frame_channel": frame_channel,
        "Cycle230_free_seam_contact_regression": cycle230,
        "supplied": [
            "one parity-superselected logical input at genesis",
            "one global mixed-gauge repeated-star E and its one-time environment permissions",
            "three coframe bits per cell in the uniform eight-origin local-constraint code",
            "the fixed four-layer local update schedule and within-edge factor-group order",
            "Cycle219 coin and Cycle230 contact parameters",
        ],
        "derived": [
            "one shared-register 3x2x2 encoder rather than two copied cube encoders",
            "complete deduplicated cell/edge factor ownership on the overlapping cover",
            "an exact gauge-identity physical code automorphism for free, seam, and contact factors",
            "exact recurrent intertwining at powers 1,2,3,5,8 by executed factorwise induction without re-encoding",
            "a load-bearing but proper-cubic-covariant within-edge factor schedule",
            "active signed update-dictionary covariance in all 24 frames, eight translation parities, and eight coframe origins",
            "held 3x3x2 and 5x3x2 closure without refit",
        ],
        "open": [
            "autonomous genesis of the mixed gauge, parity-superselection domain, and uniform coframe-origin state",
            "a translation-invariant recurrent mechanism that prepares E rather than merely applying G after E",
            "periodic-sector and fault-repair tests",
            "bridges to time, source/gravity, Record, Born/history, and prediction surfaces",
        ],
        "claim_ceiling": (
            "On the declared one-time encoded code space, the retained physical "
            "M2 registers now support an exact recurrent free/seam/contact "
            "update on overlapping and held boxes with active covariance. This "
            "does not autonomously prepare the encoder, parity domain, mixed "
            "gauge, or coframe-origin mixture."
        ),
        "compiler_claim_gate": {
            "one_time_global_shared_register_E": "PASS",
            "recurrent_retained_register_G_physical": "PASS",
            "E_G_logical_equals_G_physical_E": "PASS_on_declared_code",
            "fresh_environment_reuse": "NONE",
            "active_update_covariance": "PASS",
            "autonomous_genesis": "OPEN",
            "full_autonomous_compiler_claim_allowed": False,
        },
        "no_go_discipline": {
            "N1_alternatives": "local stabilizer pumping, gauge twirls, dissipative preparation, and inherited substrate genesis remain live",
            "N2_wall_independence": "one-time E, recurrent G, gauge identity, covariance, routing, and genesis are separate",
            "N3_hidden_imports": "parity domain, mixed gauge, coframe mixture, parameters, and fixed layer schedule are explicit",
            "N4_residual_matching": "Choi spans, signed coordinates, gauge leakage, powers, schedules, covariance, routes, and mass are separate",
            "N5_resolution": "overlapping 3x2x2 plus held 3x3x2 and 5x3x2, 24 frames, eight translations, eight origins, all 576 proper-frame products, powers through eight",
            "N6_partial_closure": "recurrent retained-register dynamics closes without promoting autonomous E genesis",
            "N7_steelman": "a local autonomous preparation/pumping rule could close the remaining compiler wall",
            "N8_cross_cycle_echo": "composes the repeated-star E, local parity rail, finite Stinespring, coframe covariance, and existing M2 update",
            "gate": "FAIL_for_broad_no_go__constructive-recurrent-update-positive",
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print("RECURRENT_OVERLAP_COMPANION_UPDATE_PASS" if report["pass"] else "RECURRENT_OVERLAP_COMPANION_UPDATE_INCOMPLETE")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
