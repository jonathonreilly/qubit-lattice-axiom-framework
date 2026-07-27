#!/usr/bin/env python3
"""Cycle-720 raw-mode Bell ceiling and its bounded-locality failure.

This probe narrows the declared law domain to one supplied total-parity
sector.  The local Choi pump is augmented by the corresponding input-parity
stabilizer, fixing the correlated physical center sector while retaining the
mixed gauge factor.  A live input in the same sector is Bell-coupled locally
to the Choi input half.  The Bell X-correction word has even Hamming parity;
it is decoded reversibly on a bounded-degree tree of the 6N modes.  Each tree
edge has an explicit physical companion correction, and the controller word
is uncomputed after the corrections are applied.

The corrected branch algebra is exact on a declared fixed-parity/center
sector, but the spatial raw-X correction requires a Jordan--Wigner Z cleanup
whose physical support grows on non-collinear boxes.  This is therefore an
exact channel ceiling and a route-specific live-input locality failure, not a
bounded-local physical encoder.  The parity label, gauge mixture,
Choi-preparation epoch, Bell/syndrome banks, rooted mode tree, and route tables
remain explicit.  No no-go or axiom-pressure claim is made.
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
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
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

from collections import defaultdict
from hashlib import sha256
from itertools import product as cartesian_product
import json

import numpy as np

import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O


Pauli = M.Pauli
Coord = tuple[int, int, int]


def canonical(row: Pauli) -> Pauli:
    return Pauli((row.x & row.z).bit_count() & 1, row.x, row.z)


def operator_syndrome(
    fixture: M.CompanionFixture, physical: Pauli, target: Pauli
) -> tuple[int, ...]:
    return tuple(
        M.symplectic(
            physical.symplectic(fixture.qubits),
            row_physical.symplectic(fixture.qubits),
            fixture.qubits,
        )
        ^ M.symplectic(
            target.symplectic(fixture.matter_qubits),
            row_target.symplectic(fixture.matter_qubits),
            fixture.matter_qubits,
        )
        for _family, row_physical, row_target in M.operator_rows(fixture)
    )


def physical_z(fixture: M.CompanionFixture, mask: int) -> Pauli:
    return Pauli(z=mask & ((1 << fixture.matter_qubits) - 1))


def target_z(mask: int) -> Pauli:
    return Pauli(z=mask)


def mode_tree(
    fixture: M.CompanionFixture,
) -> tuple[tuple[tuple[int, int, Pauli, Pauli, str], ...], int]:
    """A tree on all 6N modes with paired physical/raw-X corrections."""
    rows = []
    # Each cell's six modes form one local path.
    for cell in range(len(fixture.cells)):
        for local in range(5):
            left = 6 * cell + local
            right = left + 1
            target = Pauli(x=(1 << left) | (1 << right))
            rows.append((left, right, target, target, "onsite"))

    # The hierarchical spatial tree connects those cell paths.  A seam
    # factor represents X_u X_v times a JW-Z word; multiply the corresponding
    # onsite Z images into both sides to obtain the raw Bell X-pair correction.
    root_cell = max(fixture.cells)
    cell_tree, _fill = P.schedule_tree_plaquettes(
        fixture, root_cell, (2, 1, 0)
    )
    for edge in cell_tree:
        _left_cell, _right_cell, _owner, _axis, left, right = (
            fixture.edges[edge]
        )
        seam_physical = fixture.physical_terms(edge)[2]
        seam_target = fixture.target_terms(edge)[2]
        cleanup_physical = physical_z(fixture, seam_target.z)
        cleanup_target = target_z(seam_target.z)
        physical = canonical(seam_physical @ cleanup_physical)
        target = canonical(seam_target @ cleanup_target)
        rows.append((left, right, physical, target, "spatial"))
    root_mode = 6 * fixture.cells.index(root_cell) + 5
    return tuple(rows), root_mode


def tree_structure(
    modes: int,
    edges: tuple[tuple[int, int, Pauli, Pauli, str], ...],
    root: int,
):
    adjacency: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for edge, (left, right, *_rest) in enumerate(edges):
        adjacency[left].append((right, edge))
        adjacency[right].append((left, edge))
    parent: dict[int, tuple[int, int] | None] = {root: None}
    order = [root]
    for vertex in order:
        for target, edge in sorted(adjacency[vertex]):
            if target in parent:
                continue
            parent[target] = (vertex, edge)
            order.append(target)
    return parent, tuple(order)


def decode_even_x(
    a: int,
    modes: int,
    parent: dict[int, tuple[int, int] | None],
    order: tuple[int, ...],
) -> tuple[int, int, tuple[tuple[int, int], ...]]:
    """Postorder child->parent CNOTs leave subtree parity at each child."""
    state = a
    word = []
    coefficients = 0
    for child in reversed(order[1:]):
        owner, edge = parent[child]  # type: ignore[misc]
        child_value = (state >> child) & 1
        coefficients |= child_value << edge
        state ^= child_value << owner
        word.append((child, owner))
    root = order[0]
    return coefficients, (state >> root) & 1, tuple(word)


def apply_cnot_bits(state: int, word: tuple[tuple[int, int], ...]) -> int:
    for control, target in word:
        state ^= ((state >> control) & 1) << target
    return state


def correction_for_outcome(
    fixture: M.CompanionFixture,
    edges: tuple[tuple[int, int, Pauli, Pauli, str], ...],
    parent,
    order,
    a: int,
    b: int,
) -> tuple[Pauli, Pauli, int, int, tuple[tuple[int, int], ...]]:
    coefficients, root_parity, controller_word = decode_even_x(
        a, fixture.matter_qubits, parent, order
    )
    physical = physical_z(fixture, b)
    target = target_z(b)
    for edge, (_left, _right, row_physical, row_target, _kind) in enumerate(edges):
        if (coefficients >> edge) & 1:
            physical = physical @ row_physical
            target = target @ row_target
    return (
        canonical(physical), canonical(target), coefficients,
        root_parity, controller_word,
    )


def physical_row_cells(
    fixture: M.CompanionFixture, row: Pauli
) -> frozenset[Coord]:
    return P.pauli_cells(fixture, row)


def sector_resource_certificate(
    fixture: M.CompanionFixture,
) -> dict[str, object]:
    rows, _tags = P.direct_graph_basis(fixture)
    input_parity = Pauli(
        z=((1 << fixture.matter_qubits) - 1) << fixture.qubits
    )
    augmented = rows + (input_parity,)
    corner = max(fixture.cells)
    cell = fixture.cells.index(corner)
    allowed = tuple(
        list(range(6 * cell, 6 * cell + 6))
        + list(range(
            fixture.matter_qubits + 3 * cell,
            fixture.matter_qubits + 3 * cell + 3,
        ))
        + list(range(
            fixture.qubits + 6 * cell,
            fixture.qubits + 6 * cell + 6,
        ))
    )
    correction, _rank, contradictions = P.solve_private_correction(
        augmented, len(rows), allowed
    )
    total = fixture.qubits + fixture.matter_qubits
    syndrome_failures = sum(
        M.symplectic(
            correction.symplectic(total), row.symplectic(total), total
        ) != int(index == len(rows))
        for index, row in enumerate(augmented)
    )
    support = P.pauli_cells(fixture, input_parity)
    measurement_route = P.returned_route(min(support), support)
    correction_route = P.returned_route(
        min(support), frozenset((min(support), corner))
    )
    factor = O.build_factorization(fixture)
    center_rows = tuple(
        Pauli(row.phase, row.x, row.z)
        for row in factor.physical_w[
            factor.logical + factor.gauge:
            factor.logical + factor.gauge + factor.center
        ]
    )
    center_choi = tuple(
        Pauli(row.phase, row.x, row.z) for row in center_rows
    )
    center_signed_failures = 0
    for parity in (0, 1):
        signed_sector = Pauli(
            phase=2 * parity,
            x=input_parity.x,
            z=input_parity.z,
        )
        signed_augmented = rows + (signed_sector,)
        expected_center = list(center_choi)
        parity_row = expected_center[-1]
        expected_center[-1] = Pauli(
            (parity_row.phase + 2 * parity) % 4,
            parity_row.x,
            parity_row.z,
        )
        center_signed_failures += P.R.signed_replay_failures(
            tuple(expected_center), signed_augmented, total
        )
    output_projection_rank = P.C.R.F.base.gf2_rank(
        P.R.output_vector(row, fixture.qubits) for row in augmented
    )
    return {
        "sector_labels_tested": ("even", "odd"),
        "sector_stabilizer_rank_increment": (
            P.C.R.F.base.gf2_rank(
                row.symplectic(total) for row in augmented
            ) - P.C.R.F.base.gf2_rank(
                row.symplectic(total) for row in rows
            )
        ),
        "corner_private_correction_contradictions": contradictions,
        "corner_private_correction_syndrome_failures": syndrome_failures,
        "corner_private_correction_weight": (
            correction.x | correction.z
        ).bit_count(),
        "corner_private_correction_support_cells": len(
            P.pauli_cells(fixture, correction)
        ),
        "global_sector_measurement_route_transitions": len(measurement_route),
        "sector_correction_route_transitions": len(correction_route),
        "sector_measurement_route_failures": (
            P.route_execution_failures(min(support), measurement_route)[0]
        ),
        "sector_correction_route_failures": (
            P.route_execution_failures(min(support), correction_route)[0]
        ),
        "logical_qubits_in_fixed_parity_sector": factor.logical,
        "fixed_physical_center_rows": factor.center,
        "mixed_gauge_M2": factor.gauge,
        "Choi_graph_rank_equals_2L_plus_C": (
            len(rows) == 2 * factor.logical + factor.center
        ),
        "center_rows_outside_fixed_sector_Choi_span": M.span_failures(
            tuple(row.symplectic(total) for row in center_choi),
            tuple(row.symplectic(total) for row in augmented),
        ),
        "both_parity_sector_center_signed_replay_failures": (
            center_signed_failures
        ),
        "normalized_fixed_sector_input_marginal": (
            "Pi_parity/2^(matter_qubits-1)"
        ),
        "input_marginal_stabilizer_kernel_rank": (
            len(augmented) - output_projection_rank
        ),
        "boundary": (
            "the parity sign is supplied to the one additional pump; the "
            "pump is coherent and trace preserving, with its syndrome retained"
        ),
    }


def bell_parity_certificate(modes: int) -> dict[str, object]:
    same_sector_failures = 0
    mismatch_detection_failures = 0
    cases = 0
    if modes <= 6:
        for parity in (0, 1):
            sector = tuple(
                row for row in range(1 << modes)
                if row.bit_count() % 2 == parity
            )
            opposite = tuple(
                row for row in range(1 << modes)
                if row.bit_count() % 2 != parity
            )
            for live in sector:
                for resource in sector:
                    same_sector_failures += (live ^ resource).bit_count() % 2
                    cases += 1
                for resource in opposite:
                    mismatch_detection_failures += (
                        (live ^ resource).bit_count() % 2 != 1
                    )
    else:
        # Exercise independent same-sector and opposite-sector generators;
        # linearity extends these parity characters to the full space.
        for mode in range(modes):
            next_mode = (mode + 1) % modes
            live_odd = 1 << mode
            resource_odd = 1 << next_mode
            live_even = live_odd | resource_odd
            resource_even = 0
            same_sector_failures += (
                (live_odd ^ resource_odd).bit_count() % 2 != 0
            )
            same_sector_failures += (
                (live_even ^ resource_even).bit_count() % 2 != 0
            )
            mismatch_detection_failures += (
                (live_odd ^ resource_even).bit_count() % 2 != 1
            )
            mismatch_detection_failures += (
                (live_even ^ resource_odd).bit_count() % 2 != 1
            )
            cases += 4
    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2.0)
    cnot = np.asarray((
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0),
    ), dtype=complex)
    bell = np.kron(h, np.eye(2)) @ cnot
    return {
        "computational_parity_cases": cases,
        "same_sector_even_X_outcome_failures": same_sector_failures,
        "opposite_sector_root_bit_detection_failures": (
            mismatch_detection_failures
        ),
        "local_Bell_gate_unitarity_residual": float(np.linalg.norm(
            bell.conj().T @ bell - np.eye(4)
        )),
        "coherent_word": (
            "CNOT(live,input-half), H(live); retain both Bell registers, "
            "decode the input-half X word on the local mode tree, control "
            "physical corrections, then reverse the decoder CNOTs"
        ),
    }


def outcome_samples(modes: int) -> tuple[tuple[int, int], ...]:
    rows = {(0, 0), (0, (1 << modes) - 1)}
    rows.update((0, 1 << mode) for mode in range(modes))
    rows.update(((1 << 0) | (1 << mode), 0) for mode in range(1, modes))
    for seed in range(64):
        a = int.from_bytes(
            sha256(f"a:{modes}:{seed}".encode()).digest(), "little"
        ) & ((1 << modes) - 1)
        if a.bit_count() & 1:
            a ^= 1
        b = int.from_bytes(
            sha256(f"b:{modes}:{seed}".encode()).digest(), "little"
        ) & ((1 << modes) - 1)
        rows.add((a, b))
    return tuple(sorted(rows))


def box_certificate(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    factor = O.build_factorization(fixture)
    edges, root = mode_tree(fixture)
    modes = fixture.matter_qubits
    parent, order = tree_structure(modes, edges, root)
    tree_failures = (
        len(edges) != modes - 1
        or len(parent) != modes
        or len(order) != modes
    )
    target_vectors = tuple(
        row_target.symplectic(modes)
        for _left, _right, _physical, row_target, _kind in edges
    ) + tuple(Pauli(z=1 << mode).symplectic(modes) for mode in range(modes))
    even_reference = tuple(
        Pauli(z=1 << mode).symplectic(modes) for mode in range(modes)
    ) + tuple(
        Pauli(x=(1 << 0) | (1 << mode)).symplectic(modes)
        for mode in range(1, modes)
    )
    target_rank = P.C.R.F.base.gf2_rank(target_vectors)
    even_span_failures = M.span_failures(even_reference, target_vectors)

    generator_syndrome_failures = 0
    generator_gauge_commutator_failures = 0
    generator_center_commutator_failures = 0
    maximum_generator_cells = 0
    maximum_generator_diameter = 0
    total_generator_route_transitions = 0
    generator_route_failures = 0
    mode_tree_CNOT_nonlocal_failures = 0
    edge_child = {
        edge: child
        for child, relation in parent.items()
        if relation is not None
        for _owner, edge in (relation,)
    }
    gauge_rows = (
        factor.physical_w[factor.logical:factor.logical + factor.gauge]
        + factor.physical_v[factor.logical:factor.logical + factor.gauge]
    )
    center_rows = factor.physical_w[
        factor.logical + factor.gauge:
        factor.logical + factor.gauge + factor.center
    ]
    for edge, (left, right, physical, target, kind) in enumerate(edges):
        generator_syndrome_failures += sum(operator_syndrome(
            fixture, physical, target
        ))
        generator_gauge_commutator_failures += sum(
            M.symplectic(
                physical.symplectic(fixture.qubits),
                row.symplectic(fixture.qubits),
                fixture.qubits,
            ) for row in gauge_rows
        )
        generator_center_commutator_failures += sum(
            M.symplectic(
                physical.symplectic(fixture.qubits),
                row.symplectic(fixture.qubits),
                fixture.qubits,
            ) for row in center_rows
        )
        cells = physical_row_cells(fixture, physical)
        maximum_generator_cells = max(maximum_generator_cells, len(cells))
        maximum_generator_diameter = max(
            maximum_generator_diameter, P.R.support_diameter(cells)
        )
        anchor = fixture.cells[edge_child[edge] // 6]
        route = P.returned_route(anchor, cells)
        total_generator_route_transitions += len(route)
        forward, inverse = P.route_execution_failures(anchor, route)
        generator_route_failures += forward + inverse
        left_cell = fixture.cells[left // 6]
        right_cell = fixture.cells[right // 6]
        expected_distance = 0 if kind == "onsite" else 1
        mode_tree_CNOT_nonlocal_failures += (
            sum(abs(a - b) for a, b in zip(left_cell, right_cell))
            != expected_distance
        )
    for mode in range(modes):
        physical = Pauli(z=1 << mode)
        target = Pauli(z=1 << mode)
        generator_syndrome_failures += sum(operator_syndrome(
            fixture, physical, target
        ))

    controller_basis_failures = 0
    controller_inverse_failures = 0
    root_parity_failures = 0
    for mode in range(1, modes):
        a = (1 << 0) | (1 << mode)
        coefficients, parity, word = decode_even_x(
            a, modes, parent, order
        )
        transformed = apply_cnot_bits(a, word)
        replay = apply_cnot_bits(transformed, tuple(reversed(word)))
        reconstructed = 0
        for edge, (left, right, *_rest) in enumerate(edges):
            if (coefficients >> edge) & 1:
                reconstructed ^= (1 << left) | (1 << right)
        controller_basis_failures += reconstructed != a
        controller_inverse_failures += replay != a
        root_parity_failures += parity != 0
    _coefficients, mismatch_root, _word = decode_even_x(
        1, modes, parent, order
    )

    branch_failures = 0
    target_binary_failures = 0
    controller_word_failures = 0
    maximum_branch_physical_weight = 0
    samples = outcome_samples(modes)
    if modes <= 6:
        samples = tuple(
            (a, b)
            for a in range(1 << modes) if a.bit_count() % 2 == 0
            for b in range(1 << modes)
        )
    for a, b in samples:
        physical, target, _coefficients, parity, word = correction_for_outcome(
            fixture, edges, parent, order, a, b
        )
        expected = canonical(Pauli(x=a, z=b))
        target_binary_failures += (target.x, target.z) != (expected.x, expected.z)
        branch_failures += sum(operator_syndrome(
            fixture, physical, expected
        ))
        transformed = apply_cnot_bits(a, word)
        controller_word_failures += (
            ((transformed >> root) & 1) != parity
            or apply_cnot_bits(transformed, tuple(reversed(word))) != a
        )
        root_parity_failures += parity != 0
        maximum_branch_physical_weight = max(
            maximum_branch_physical_weight,
            (physical.x | physical.z).bit_count(),
        )

    # Delete one spatial correction: its paired raw-X generator must cease to
    # implement the branch syndrome.
    spatial = next(
        row for row in edges if row[4] == "spatial"
    ) if len(fixture.cells) > 1 else edges[0]
    deletion_syndrome_mismatches = sum(operator_syndrome(
        fixture, Pauli(), spatial[3]
    ))
    sector = sector_resource_certificate(fixture)
    bell = bell_parity_certificate(modes)
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "matter_M2": modes,
        "physical_output_M2": fixture.qubits,
        "mode_tree_edges": len(edges),
        "mode_tree_failures": int(bool(tree_failures)),
        "even_Pauli_dimension": 2 * modes - 1,
        "correction_target_rank": target_rank,
        "even_reference_rows_outside_correction_span": even_span_failures,
        "physical_correction_generator_syndrome_failures": (
            generator_syndrome_failures
        ),
        "physical_correction_generator_gauge_commutator_failures": (
            generator_gauge_commutator_failures
        ),
        "physical_correction_generator_center_commutator_failures": (
            generator_center_commutator_failures
        ),
        "maximum_generator_support_cells": maximum_generator_cells,
        "maximum_generator_support_diameter": maximum_generator_diameter,
        "total_generator_route_transitions": total_generator_route_transitions,
        "generator_route_locality_return_failures": generator_route_failures,
        "mode_tree_decoder_CNOT_locality_failures": (
            mode_tree_CNOT_nonlocal_failures
        ),
        "generator_route_transitions_per_cell": (
            total_generator_route_transitions / len(fixture.cells)
        ),
        "controller_basis_failures": controller_basis_failures,
        "controller_inverse_failures": controller_inverse_failures,
        "lawful_even_root_parity_failures": root_parity_failures,
        "unlawful_odd_root_detection_failures": mismatch_root != 1,
        "Bell_outcome_branches_tested": len(samples),
        "branch_target_binary_failures": target_binary_failures,
        "branch_Heisenberg_intertwiner_failures": branch_failures,
        "branch_controller_word_failures": controller_word_failures,
        "maximum_sampled_branch_physical_weight": (
            maximum_branch_physical_weight
        ),
        "delete_one_spatial_correction_syndrome_mismatches": (
            deletion_syndrome_mismatches
        ),
        "sector_resource": sector,
        "Bell_coupling": bell,
        "channel_identity": (
            "for every lawful Bell branch P, the executed physical correction "
            "C(P) has [C(P),A_physical]=[P,A_input] on every generating "
            "observable; therefore correction o E(P rho P) = E(rho) on the "
            "fixed sector, with the gauge factor still mixed"
        ),
    }


def main() -> None:
    shapes = (
        (1, 1, 1), (2, 2, 2), (3, 2, 2),
        (4, 2, 2), (5, 2, 2), (5, 3, 2),
    )
    boxes = tuple(box_certificate(shape) for shape in shapes)
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "fixed parity adds one independent Choi stabilizer with a bounded corner correction and retained syndrome",
        all(
            box["sector_resource"]["sector_stabilizer_rank_increment"] == 1
            and box["sector_resource"]["corner_private_correction_contradictions"] == 0
            and box["sector_resource"]["corner_private_correction_syndrome_failures"] == 0
            and box["sector_resource"]["corner_private_correction_support_cells"] == 1
            and box["sector_resource"][
                "center_rows_outside_fixed_sector_Choi_span"
            ] == 0
            and box["sector_resource"][
                "both_parity_sector_center_signed_replay_failures"
            ] == 0
            and box["sector_resource"][
                "input_marginal_stabilizer_kernel_rank"
            ] == 1
            for box in boxes
        ),
    )
    check(
        "local Bell coupling makes every same-sector X word even and detects a parity mismatch at the decoder root",
        all(
            box["Bell_coupling"]["same_sector_even_X_outcome_failures"] == 0
            and box["Bell_coupling"]["opposite_sector_root_bit_detection_failures"] == 0
            and box["Bell_coupling"]["local_Bell_gate_unitarity_residual"] < 4.0e-15
            and box["unlawful_odd_root_detection_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "bounded-degree mode tree spans the complete even Pauli correction algebra and the reversible decoder returns its work",
        all(
            box["mode_tree_failures"] == 0
            and box["correction_target_rank"] == box["even_Pauli_dimension"]
            and box["even_reference_rows_outside_correction_span"] == 0
            and box["controller_inverse_failures"] == 0
            and box["lawful_even_root_parity_failures"] == 0
            and box["generator_route_locality_return_failures"] == 0
            and box["mode_tree_decoder_CNOT_locality_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "every physical correction generator is the exact gauge-and-center-preserving image of its raw Bell Pauli",
        all(
            box["physical_correction_generator_syndrome_failures"] == 0
            and box["physical_correction_generator_gauge_commutator_failures"] == 0
            and box["physical_correction_generator_center_commutator_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "exhaustive one-cell and deterministic larger-box branches satisfy the corrected-channel intertwiner",
        all(
            box["branch_target_binary_failures"] == 0
            and box["branch_Heisenberg_intertwiner_failures"] == 0
            and box["branch_controller_word_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "spatial correction deletion is detected",
        all(
            box["delete_one_spatial_correction_syndrome_mismatches"] > 0
            for box in boxes[1:]
        ),
    )
    nontrivial = boxes[1:]
    locality_gate = all(
        box["maximum_generator_support_cells"] <= 2
        and box["maximum_generator_support_diameter"] <= 1
        for box in nontrivial
    )
    check(
        "held non-collinear ladder detects failure of the bounded two-cell raw-X correction gate",
        not locality_gate
        and boxes[-1]["maximum_generator_support_cells"] > 2
        and boxes[-1]["maximum_generator_support_diameter"] > 1,
    )
    report = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "checks": checks,
        "boxes": boxes,
        "derived": (
            "fixed-sector raw Bell parity law, exact Heisenberg branch "
            "correction algebra, and a held-size locality falsification of "
            "the raw-X/Jordan--Wigner-cleanup correction route"
        ),
        "supplied": (
            "fixed parity label shared by live input and resource; one-time "
            "Choi preparation epoch; fixed local center signs; mixed gauge "
            "reference; rooted mode-tree/router table; clean Bell and "
            "syndrome registers"
        ),
        "open": (
            "autonomous sector/genesis law; sector-summed live-input encoder; "
            "collision-free merge of preparation, Bell, decoder and recurrent "
            "G controllers; physical reason for parity superselection; downstream "
            "time/source/Record/Born bridges"
        ),
        "claim_boundary": (
            "exact fixed-sector corrected-channel algebra only; the raw-mode "
            "Bell route fails the bounded-local correction gate because its "
            "Jordan--Wigner cleanup grows on non-collinear boxes; not a "
            "physical compiler, no no-go, and no axiom pressure"
        ),
        "authority": "none",
        "audit": "unset",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
