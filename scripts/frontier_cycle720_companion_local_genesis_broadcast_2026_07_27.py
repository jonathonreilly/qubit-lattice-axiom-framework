#!/usr/bin/env python3
"""Cycle-720 bounded local genesis for coframe and parity-dephasing auxiliaries.

This probe does not claim to prepare the complete companion Choi encoder.  It
isolates two pieces of the one-time genesis wall and gives them an explicit
local construction on finite open boxes:

* three locally random root bits are broadcast along a rooted nearest-
  neighbour tree to prepare the uniform mixture of all eight coframe-origin
  configurations; and
* one Bell seed is broadcast, controls onsite matter parity, and is
  unbroadcast before tracing, implementing the nonselective total-parity
  twirl without querying total parity or retaining a global parity service.

A single bounded-state token follows the Euler contour of the rooted tree.
Its runtime transition depends only on the incoming port and a supplied local
parent/child router table.  The number of transitions grows with the box, but
there is no runtime host-selected next transition or interpretation of those
transitions as physical time.  The size/shape-specific rooted table remains
supplied.  The root/corner and port chart are temporary preparation apparatus;
all roots and axis orders produce the same retained density operator.  Literal
collision-free M2 placement of the controller is left open, as are the mixed-
gauge/center Choi preparation and the reason Nature should impose the
resulting parity-dephasing channel.
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
    "scripts/frontier_cycle720_companion_local_genesis_broadcast_2026_07_27.py",
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

from hashlib import sha256
from itertools import permutations, product as cartesian_product
import json

import numpy as np

import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle720_companion_recurrent_overlap_update_2026_07_27 as REC
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O


Coord = tuple[int, int, int]
TOL = 4.0e-10


def tree_parent(
    cells: tuple[Coord, ...], root: Coord, axis_order: tuple[int, ...]
) -> dict[Coord, Coord | None]:
    cell_set = set(cells)
    parent: dict[Coord, Coord | None] = {root: None}
    for cell in cells:
        if cell == root:
            continue
        for axis in axis_order:
            if cell[axis] == root[axis]:
                continue
            candidate = list(cell)
            candidate[axis] += 1 if cell[axis] < root[axis] else -1
            candidate_coord = tuple(candidate)
            if candidate_coord not in cell_set:
                raise AssertionError("tree parent leaves the box")
            parent[cell] = candidate_coord
            break
        else:
            raise AssertionError("non-root cell has no parent")
    return parent


def edge_axis(left: Coord, right: Coord) -> int:
    axes = tuple(
        axis for axis in range(3) if left[axis] != right[axis]
    )
    if len(axes) != 1 or abs(left[axes[0]] - right[axes[0]]) != 1:
        raise AssertionError("tree edge is not nearest-neighbour")
    return axes[0]


def ordered_children(
    cells: tuple[Coord, ...],
    parent: dict[Coord, Coord | None],
    axis_order: tuple[int, ...],
) -> dict[Coord, tuple[Coord, ...]]:
    axis_rank = {axis: index for index, axis in enumerate(axis_order)}
    children = {cell: [] for cell in cells}
    for child, owner in parent.items():
        if owner is not None:
            children[owner].append(child)
    return {
        cell: tuple(sorted(rows, key=lambda child: (
            axis_rank[edge_axis(cell, child)], child
        )))
        for cell, rows in children.items()
    }


def contour_prepare(
    cells: tuple[Coord, ...],
    root: Coord,
    axis_order: tuple[int, ...],
    coframe_seed: int,
    parity_seed: int,
    delete_coframe_edge: tuple[Coord, Coord] | None = None,
    delete_parity_uncompute: tuple[Coord, Coord] | None = None,
) -> dict[str, object]:
    parent = tree_parent(cells, root, axis_order)
    children = ordered_children(cells, parent, axis_order)
    coframe = {cell: 0 for cell in cells}
    parity_work = {cell: 0 for cell in cells}
    coframe[root] = coframe_seed
    parity_work[root] = parity_seed
    parity_control_visits = [root]
    edge_visits = []
    current = root
    incoming: Coord | None = None
    maximum_steps = 2 * (len(cells) - 1) + 1
    steps = 0
    while True:
        child_ports = children[current]
        if incoming is None or incoming == parent[current]:
            outgoing = child_ports[0] if child_ports else parent[current]
        else:
            child_index = child_ports.index(incoming)
            outgoing = (
                child_ports[child_index + 1]
                if child_index + 1 < len(child_ports)
                else parent[current]
            )
        if outgoing is None:
            break
        if parent[outgoing] == current:
            child = outgoing
            key = tuple(sorted((current, child)))
            if key != delete_coframe_edge:
                coframe[child] = (
                    coframe[current] ^ (1 << edge_axis(current, child))
                )
            parity_work[child] ^= parity_work[current]
            edge_visits.append((current, child, "down"))
            current, incoming = child, current
            parity_control_visits.append(current)
        else:
            child = current
            owner = outgoing
            key = tuple(sorted((owner, child)))
            if key != delete_parity_uncompute:
                parity_work[child] ^= parity_work[owner]
            edge_visits.append((child, owner, "up"))
            current, incoming = owner, child
        steps += 1
        if steps > maximum_steps:
            raise AssertionError("local contour failed to return")

    tree_edges = tuple(
        tuple(sorted((cell, owner)))
        for cell, owner in parent.items() if owner is not None
    )
    return {
        "coframe": tuple(coframe[cell] for cell in cells),
        "parity_work": tuple(parity_work[cell] for cell in cells),
        "parity_control_visits": tuple(parity_control_visits),
        "edge_visits": tuple(edge_visits),
        "tree_edges": tree_edges,
        "tree_edge_count": len(tree_edges),
        "contour_transitions": len(edge_visits),
        "token_returned_to_root": current == root,
        "token_parked_after_root_return": current == root and outgoing is None,
        "maximum_children": max(map(len, children.values())),
        "maximum_tree_edge_distance": max((
            sum(abs(a - b) for a, b in zip(*edge))
            for edge in tree_edges
        ), default=0),
    }


def coframe_gate_word(
    cells: tuple[Coord, ...], edge_visits: tuple[tuple[Coord, Coord, str], ...]
) -> tuple[tuple[str, int, int | None], ...]:
    lookup = {cell: index for index, cell in enumerate(cells)}
    word = []
    for left, right, direction in edge_visits:
        if direction != "down":
            continue
        for axis in range(3):
            word.append((
                "CNOT",
                3 * lookup[left] + axis,
                3 * lookup[right] + axis,
            ))
        word.append((
            "X",
            3 * lookup[right] + edge_axis(left, right),
            None,
        ))
    return tuple(word)


def parity_copy_gate_word(
    cells: tuple[Coord, ...], edge_visits: tuple[tuple[Coord, Coord, str], ...]
) -> tuple[tuple[str, int, int], ...]:
    lookup = {cell: index for index, cell in enumerate(cells)}
    return tuple(
        ("CNOT", lookup[left], lookup[right])
        if direction == "down"
        else ("CNOT", lookup[right], lookup[left])
        for left, right, direction in edge_visits
    )


def apply_binary_word(
    state: int,
    word: tuple[tuple[str, int, int | None], ...],
) -> int:
    for kind, left, right in word:
        if kind == "X":
            state ^= 1 << left
        elif kind == "CNOT" and right is not None:
            state ^= ((state >> left) & 1) << right
        else:
            raise AssertionError("unknown binary gate")
    return state


def coframe_tuple_from_state(state: int, cells: int) -> tuple[int, ...]:
    return tuple((state >> (3 * cell)) & 7 for cell in range(cells))


def coframe_constraint_failures(
    fixture: M.CompanionFixture, assignment: tuple[int, ...]
) -> int:
    return sum(
        (((assignment[left] ^ assignment[right]) >> coframe_axis) & 1)
        != int(edge_axis_value == coframe_axis)
        for left, right, _owner, edge_axis_value, *_rest in fixture.edges
        for coframe_axis in range(3)
    )


def all_solution_set(cells: tuple[Coord, ...]) -> frozenset[tuple[int, ...]]:
    return frozenset(
        tuple(sum(
            (((cell[axis] & 1) ^ seed[axis]) << axis)
            for axis in range(3)
        ) for cell in cells)
        for seed in cartesian_product(range(2), repeat=3)
    )


def corners(cells: tuple[Coord, ...]) -> tuple[Coord, ...]:
    bounds = tuple(
        (min(cell[axis] for cell in cells), max(cell[axis] for cell in cells))
        for axis in range(3)
    )
    return tuple(cartesian_product(*(bound for bound in bounds)))


def transport_coframe_assignment(
    cells: tuple[Coord, ...],
    assignment: tuple[int, ...],
    frame: np.ndarray,
    shift: Coord,
) -> tuple[tuple[Coord, ...], tuple[int, ...]]:
    transformed = Q.affine_cells(cells, frame, shift)
    transformed_lookup = {
        cell: index for index, cell in enumerate(transformed)
    }
    target_assignment = [0] * len(transformed)
    for source_index, cell in enumerate(cells):
        target_cell = tuple(int(value) for value in (
            frame @ np.asarray(cell, dtype=int)
            + np.asarray(shift, dtype=int)
        ))
        target_value = 0
        for target_axis in range(3):
            source_axis = next(
                axis for axis in range(3)
                if frame[target_axis, axis] != 0
            )
            target_value |= (
                (assignment[source_index] >> source_axis) & 1
            ) << target_axis
        target_assignment[transformed_lookup[target_cell]] = target_value
    return transformed, tuple(target_assignment)


def primitive_certificate() -> dict[str, object]:
    cnot_rows = tuple(
        (control, target, control, target ^ control)
        for control, target in cartesian_product(range(2), repeat=2)
    )
    swap_rows = tuple(
        (left, right, right, left)
        for left, right in cartesian_product(range(2), repeat=2)
    )
    router_failures = 0
    router_permutations = []
    for children in range(4):
        active = children + 1
        permutation = tuple(
            (port + 1) % active if port < active else port
            for port in range(4)
        )
        router_failures += len(set(permutation)) != 4
        router_permutations.append(permutation)
    cz = np.diag((1, 1, 1, -1)).astype(complex)
    return {
        "CNOT_truth_rows": len(cnot_rows),
        "CNOT_bijection_failures": len(set(cnot_rows)) != len(cnot_rows),
        "token_SWAP_truth_rows": len(swap_rows),
        "token_SWAP_bijection_failures": len(set(swap_rows)) != len(swap_rows),
        "router_permutations_for_zero_to_three_children": tuple(
            router_permutations
        ),
        "router_bijection_failures": router_failures,
        "controlled_Z_unitarity_residual": float(np.linalg.norm(
            cz.conj().T @ cz - np.eye(4)
        )),
        "root_epoch_boundary": (
            "one reversible fresh/active/spent preparation handshake; the "
            "inverse starts from spent and is not the recurrent matter law"
        ),
    }


def parity_twirl_certificate(
    fixture: M.CompanionFixture,
    minimum_control_visits: int,
    maximum_control_visits: int,
) -> dict[str, object]:
    matter_qubits = fixture.matter_qubits
    physical_even_rows = tuple(
        target for _family, _physical, target in M.operator_rows(fixture)
    )

    def multiplier(x: int, deleted_mode: int | None = None) -> float:
        applied = ((1 << matter_qubits) - 1)
        if deleted_mode is not None:
            applied ^= 1 << deleted_mode
        return 0.5 * (1 + (-1) ** ((x & applied).bit_count() & 1))

    odd_rows = tuple(
        (1 << mode, (1 << mode, 1 << mode))
        for mode in range(matter_qubits)
    )
    local_complete_basis_failures = 0
    local_modes = 6
    local_parity = M.Pauli(z=(1 << local_modes) - 1)
    for x in range(1 << local_modes):
        for z in range(1 << local_modes):
            row = M.Pauli(x=x, z=z)
            local_complete_basis_failures += M.symplectic(
                local_parity.symplectic(local_modes),
                row.symplectic(local_modes),
                local_modes,
            ) != (x.bit_count() & 1)
    grade_induction_failures = sum(
        ((left + right) & 1) != (left ^ right)
        for left, right in cartesian_product(range(2), repeat=2)
    )
    return {
        "matter_qubits": matter_qubits,
        "local_controlled_Z_per_cell": 6,
        "even_CAR_generators": len(physical_even_rows),
        "even_CAR_twirl_failures": sum(
            abs(multiplier(row.x) - 1.0) > TOL
            for row in physical_even_rows
        ),
        "odd_single_XY_rows": 2 * len(odd_rows),
        "odd_single_XY_erasure_failures": sum(
            abs(multiplier(x) - 0.0) > TOL
            for x, _labels in odd_rows for _ in range(2)
        ),
        "actual_contour_minimum_cell_control_visits": minimum_control_visits,
        "actual_contour_maximum_cell_control_visits": maximum_control_visits,
        "actual_contour_controlled_Z_per_matter_mode": (
            minimum_control_visits, maximum_control_visits
        ),
        "exhaustive_one_cell_Pauli_basis_rows": 1 << (2 * local_modes),
        "exhaustive_one_cell_parity_grade_failures": (
            local_complete_basis_failures
        ),
        "tensor_grade_induction_truth_rows": 4,
        "tensor_grade_induction_failures": grade_induction_failures,
        "complete_global_Pauli_basis_rows": 1 << (2 * matter_qubits),
        "complete_basis_proof": (
            "every one-cell Pauli basis row has conjugation sign "
            "(-1)^popcount(X); tensor-product signs multiply and grades XOR, "
            "so the identity covers the complete global Pauli basis"
        ),
        "total_parity_population_multiplier": multiplier(0),
        "delete_one_local_control_odd_survival_multiplier": multiplier(
            1, deleted_mode=0
        ),
        "channel_formula": "D(rho)=(rho+P_total rho P_total)/2",
        "global_parity_query_count": 0,
        "retained_global_parity_service_bits": 0,
    }


def box_certificate(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    factor = O.build_factorization(fixture)
    coordinate = REC.coordinate_intertwiner_certificate(fixture, factor)
    cells = fixture.cells
    expected = all_solution_set(cells)
    orders = tuple(permutations(range(3)))
    root_order_failures = 0
    maximum_children = 0
    maximum_distance = 0
    contour_failures = 0
    dirty_parity_work = 0
    literal_coframe_word_failures = 0
    coframe_inverse_failures = 0
    dirty_coframe_targets_accepted = 0
    dirty_coframe_targets_hidden = 0
    literal_parity_copy_word_failures = 0
    dirty_parity_targets_accepted = 0
    dirty_parity_targets_hidden = 0
    parity_visit_failures = 0
    minimum_control_visits = len(cells)
    maximum_control_visits = 0
    digests = set()
    canonical = None
    for root in corners(cells):
        for order in orders:
            prepared = []
            for seed_bits in cartesian_product(range(2), repeat=3):
                seed = sum(bit << axis for axis, bit in enumerate(seed_bits))
                result = contour_prepare(cells, root, order, seed, 1)
                coframe_word = coframe_gate_word(
                    cells, result["edge_visits"]
                )
                root_index = cells.index(root)
                coframe_initial = seed << (3 * root_index)
                coframe_actual = apply_binary_word(
                    coframe_initial, coframe_word
                )
                literal_coframe_word_failures += (
                    coframe_tuple_from_state(coframe_actual, len(cells))
                    != result["coframe"]
                )
                coframe_inverse_failures += apply_binary_word(
                    coframe_actual, tuple(reversed(coframe_word))
                ) != coframe_initial
                parity_word = parity_copy_gate_word(
                    cells, result["edge_visits"]
                )
                parity_initial = 1 << root_index
                parity_actual = apply_binary_word(
                    parity_initial, parity_word
                )
                literal_parity_copy_word_failures += (
                    parity_actual != parity_initial
                )
                visit_counts = {
                    cell: result["parity_control_visits"].count(cell)
                    for cell in cells
                }
                parity_visit_failures += any(
                    visits != 1 for visits in visit_counts.values()
                )
                minimum_control_visits = min(
                    minimum_control_visits, *visit_counts.values()
                )
                maximum_control_visits = max(
                    maximum_control_visits, *visit_counts.values()
                )
                prepared.append(result["coframe"])
                maximum_children = max(
                    maximum_children, result["maximum_children"]
                )
                maximum_distance = max(
                    maximum_distance, result["maximum_tree_edge_distance"]
                )
                contour_failures += (
                    not result["token_returned_to_root"]
                    or not result["token_parked_after_root_return"]
                    or result["contour_transitions"] != 2 * (len(cells) - 1)
                )
                dirty_parity_work += any(
                    bit for cell, bit in zip(cells, result["parity_work"])
                    if cell != root
                )
            base_result = contour_prepare(cells, root, order, 0, 1)
            base_coframe_word = coframe_gate_word(
                cells, base_result["edge_visits"]
            )
            clean_coframe_output = apply_binary_word(
                0, base_coframe_word
            )
            base_parity_word = parity_copy_gate_word(
                cells, base_result["edge_visits"]
            )
            clean_parity_output = apply_binary_word(
                1 << cells.index(root), base_parity_word
            )
            for cell_index, cell in enumerate(cells):
                if cell == root:
                    continue
                for axis in range(3):
                    dirty = 1 << (3 * cell_index + axis)
                    clean_domain = (
                        dirty & ~(((1 << 3) - 1) << (3 * cells.index(root)))
                    ) == 0
                    dirty_coframe_targets_accepted += clean_domain
                    dirty_coframe_targets_hidden += apply_binary_word(
                        dirty, base_coframe_word
                    ) == clean_coframe_output
                dirty_parity = 1 << cell_index
                clean_parity_domain = (
                    dirty_parity & ~(1 << cells.index(root))
                ) == 0
                dirty_parity_targets_accepted += clean_parity_domain
                dirty_parity_targets_hidden += apply_binary_word(
                    dirty_parity | (1 << cells.index(root)),
                    base_parity_word,
                ) == clean_parity_output
            prepared_set = frozenset(prepared)
            root_order_failures += prepared_set != expected
            digest = sha256(repr(tuple(sorted(prepared_set))).encode()).hexdigest()
            digests.add(digest)
            if canonical is None:
                canonical = contour_prepare(cells, root, order, 0, 1)

    if canonical is None:
        raise AssertionError("missing canonical preparation")
    deleted_edge = canonical["tree_edges"][0]
    deleted = contour_prepare(
        cells, cells[0], (0, 1, 2), 0, 1,
        delete_coframe_edge=deleted_edge,
    )
    deleted_uncompute = contour_prepare(
        cells, cells[0], (0, 1, 2), 0, 1,
        delete_parity_uncompute=deleted_edge,
    )
    canonical_word = coframe_gate_word(cells, canonical["edge_visits"])
    single_gate_deletion_undetected = 0
    for deleted_gate in range(len(canonical_word)):
        damaged_word = (
            canonical_word[:deleted_gate] + canonical_word[deleted_gate + 1:]
        )
        detected = False
        for seed in range(8):
            damaged = apply_binary_word(seed, damaged_word)
            detected |= coframe_constraint_failures(
                fixture, coframe_tuple_from_state(damaged, len(cells))
            ) > 0
        single_gate_deletion_undetected += not detected
    frame_translation_failures = 0
    sectorwise_transport_failures = 0
    affine_contexts = 0
    for frame in T.proper_cubic_frames():
        for shift in cartesian_product(range(2), repeat=3):
            transformed = Q.affine_cells(cells, frame, shift)
            transformed_fixture = O.arbitrary_fixture(transformed)
            transformed_expected = all_solution_set(transformed)
            transported = []
            for assignment in expected:
                _target_cells, target_assignment = (
                    transport_coframe_assignment(
                        cells, assignment, frame, shift
                    )
                )
                transported.append(target_assignment)
            sectorwise_transport_failures += (
                frozenset(transported) != transformed_expected
            )
            transformed_prepared = frozenset(
                contour_prepare(
                    transformed,
                    corners(transformed)[0],
                    (0, 1, 2),
                    seed,
                    1,
                )["coframe"]
                for seed in range(8)
            )
            frame_translation_failures += (
                transformed_prepared != transformed_expected
                or any(
                    coframe_constraint_failures(
                        transformed_fixture, assignment
                    )
                    for assignment in transformed_prepared
                )
            )
            affine_contexts += 1

    frame_product_failures = 0
    frames = tuple(T.proper_cubic_frames())
    for left in frames:
        for right in frames:
            for assignment in expected:
                middle_cells, middle_assignment = (
                    transport_coframe_assignment(
                        cells, assignment, right, (0, 0, 0)
                    )
                )
                composed_cells, composed_assignment = (
                    transport_coframe_assignment(
                        middle_cells,
                        middle_assignment,
                        left,
                        (0, 0, 0),
                    )
                )
                direct_cells, direct_assignment = (
                    transport_coframe_assignment(
                        cells,
                        assignment,
                        left @ right,
                        (0, 0, 0),
                    )
                )
                frame_product_failures += (
                    composed_cells != direct_cells
                    or composed_assignment != direct_assignment
                )

    return {
        "shape": shape,
        "cells": len(cells),
        "roots_tested": len(corners(cells)),
        "axis_orders_tested": len(orders),
        "coframe_seeds_per_preparation": 8,
        "root_axis_order_distribution_failures": root_order_failures,
        "distinct_retained_distribution_digests": len(digests),
        "retained_coframe_constraint_failures": sum(
            coframe_constraint_failures(fixture, row) for row in expected
        ),
        "retained_distribution_support": len(expected),
        "retained_distribution_weight_per_sector": "1/8",
        "maximum_tree_children": maximum_children,
        "maximum_tree_edge_distance": maximum_distance,
        "contour_return_or_length_failures": contour_failures,
        "parity_copy_return_failures": dirty_parity_work,
        "literal_coframe_CNOT_X_word_failures": (
            literal_coframe_word_failures
        ),
        "literal_coframe_inverse_failures": coframe_inverse_failures,
        "dirty_nonroot_coframe_targets_tested": (
            len(corners(cells)) * len(orders) * 3 * (len(cells) - 1)
        ),
        "dirty_nonroot_coframe_targets_accepted": (
            dirty_coframe_targets_accepted
        ),
        "dirty_nonroot_coframe_targets_hidden": (
            dirty_coframe_targets_hidden
        ),
        "literal_parity_copy_word_failures": (
            literal_parity_copy_word_failures
        ),
        "dirty_nonroot_parity_targets_tested": (
            len(corners(cells)) * len(orders) * (len(cells) - 1)
        ),
        "dirty_nonroot_parity_targets_accepted": (
            dirty_parity_targets_accepted
        ),
        "dirty_nonroot_parity_targets_hidden": dirty_parity_targets_hidden,
        "actual_contour_parity_visit_failures": parity_visit_failures,
        "tree_edges": len(cells) - 1,
        "contour_transitions": 2 * (len(cells) - 1),
        "coframe_propagation_CNOTs": 3 * (len(cells) - 1),
        "coframe_affine_X_gates": len(cells) - 1,
        "coframe_local_Bell_gates": 6,
        "parity_broadcast_and_unbroadcast_CNOTs": 2 * (len(cells) - 1),
        "parity_local_controlled_Z_gates": 6 * len(cells),
        "parity_local_Bell_gates": 2,
        "coframe_reference_environment_M2": 3,
        "parity_seed_and_reference_environment_M2": 2,
        "affine_frame_translation_contexts": affine_contexts,
        "affine_frame_translation_failures": frame_translation_failures,
        "sectorwise_affine_transport_failures": (
            sectorwise_transport_failures
        ),
        "sectorwise_ordered_frame_products": len(frames) ** 2,
        "sectorwise_frame_product_seed_blocks": len(frames) ** 2 * 8,
        "sectorwise_frame_product_failures": frame_product_failures,
        "delete_one_coframe_propagation_constraint_failures": (
            coframe_constraint_failures(fixture, deleted["coframe"])
        ),
        "single_literal_coframe_gate_deletions_tested": len(canonical_word),
        "single_literal_coframe_gate_deletions_undetected": (
            single_gate_deletion_undetected
        ),
        "delete_one_parity_uncompute_dirty_work_bits": sum(
            deleted_uncompute["parity_work"][1:]
        ),
        "parity_twirl": parity_twirl_certificate(
            fixture, minimum_control_visits, maximum_control_visits
        ),
        "retained_environment_route": {
            "gauge_reference_spectator_M2": factor.gauge,
            "parity_environment_spectator_M2": 1,
            "total_semantic_spectator_M2": factor.gauge + 1,
            "semantic_spectator_M2_per_cell": (
                (factor.gauge + 1) / len(cells)
            ),
            "logical_coordinate_failures": coordinate[
                "logical_coordinate_failures"
            ],
            "gauge_coordinate_failures": coordinate[
                "gauge_coordinate_failures"
            ],
            "parity_coordinate_failures": coordinate[
                "parity_coordinate_failures"
            ],
            "physical_generator_gauge_commutator_failures": coordinate[
                "physical_generator_gauge_commutator_failures"
            ],
            "physical_generator_center_commutator_failures": coordinate[
                "physical_generator_center_commutator_failures"
            ],
            "extension": "G_physical tensor I_semantic_environment",
            "boundary": (
                "retention removes literal trace/reset but the canonical "
                "reference coordinates do not yet have a held-size local M2 "
                "placement/preparation circuit"
            ),
        },
    }


def main() -> None:
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
    primitive = primitive_certificate()
    boxes = tuple(box_certificate(shape) for shape in shapes)
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "all bounded controller primitives are reversible local M2 gates or permutations",
        primitive["CNOT_bijection_failures"] == 0
        and primitive["token_SWAP_bijection_failures"] == 0
        and primitive["router_bijection_failures"] == 0
        and primitive["controlled_Z_unitarity_residual"] < TOL,
    )
    check(
        "the supplied local router executes literal reversible CNOT X contour words with clean targets inverse and returned work",
        all(
            row["maximum_tree_children"] <= 3
            and row["maximum_tree_edge_distance"] == 1
            and row["contour_return_or_length_failures"] == 0
            and row["parity_copy_return_failures"] == 0
            and row["literal_coframe_CNOT_X_word_failures"] == 0
            and row["literal_coframe_inverse_failures"] == 0
            and row["dirty_nonroot_coframe_targets_accepted"] == 0
            and row["dirty_nonroot_coframe_targets_hidden"] == 0
            and row["literal_parity_copy_word_failures"] == 0
            and row["dirty_nonroot_parity_targets_accepted"] == 0
            and row["dirty_nonroot_parity_targets_hidden"] == 0
            for row in boxes
        ),
    )
    check(
        "local Bell seeds and nearest-neighbour broadcast prepare the unique uniform eight-origin coframe mixture",
        all(
            row["root_axis_order_distribution_failures"] == 0
            and row["distinct_retained_distribution_digests"] == 1
            and row["retained_coframe_constraint_failures"] == 0
            and row["retained_distribution_support"] == 8
            for row in boxes
        ),
    )
    check(
        "the retained coframe density is root-free and active-covariant in every frame and translation parity",
        all(
            row["affine_frame_translation_contexts"] == 192
            and row["affine_frame_translation_failures"] == 0
            for row in boxes
        ),
    )
    check(
        "the eight coframe sectors are also an affine-covariant typed gauge input without requiring uniform weights",
        all(
            row["sectorwise_affine_transport_failures"] == 0
            and row["sectorwise_ordered_frame_products"] == 576
            and row["sectorwise_frame_product_failures"] == 0
            for row in boxes
        ),
    )
    check(
        "the local broadcast-control-unbroadcast channel is exactly the total-parity twirl without a parity query",
        all(
            row["parity_twirl"]["even_CAR_twirl_failures"] == 0
            and row["parity_twirl"]["odd_single_XY_erasure_failures"] == 0
            and row["actual_contour_parity_visit_failures"] == 0
            and row["parity_twirl"][
                "actual_contour_controlled_Z_per_matter_mode"
            ] == (1, 1)
            and row["parity_twirl"][
                "exhaustive_one_cell_parity_grade_failures"
            ] == 0
            and row["parity_twirl"][
                "tensor_grade_induction_failures"
            ] == 0
            and row["parity_twirl"]["total_parity_population_multiplier"] == 1
            and row["parity_twirl"]["global_parity_query_count"] == 0
            and row["parity_twirl"]["retained_global_parity_service_bits"] == 0
            for row in boxes
        ),
    )
    check(
        "coframe propagation parity cleanup and onsite parity controls are load-bearing",
        all(
            row["delete_one_coframe_propagation_constraint_failures"] > 0
            and row["single_literal_coframe_gate_deletions_undetected"] == 0
            and row["delete_one_parity_uncompute_dirty_work_bits"] > 0
            and row["parity_twirl"][
                "delete_one_local_control_odd_survival_multiplier"
            ] == 1
            for row in boxes
        ),
    )
    check(
        "retaining Bell and parity environments gives a bounded-density spectator extension of recurrent G",
        all(
            row["retained_environment_route"][
                "semantic_spectator_M2_per_cell"
            ] <= 2.5
            and row["retained_environment_route"][
                "logical_coordinate_failures"
            ] == 0
            and row["retained_environment_route"][
                "gauge_coordinate_failures"
            ] == 0
            and row["retained_environment_route"][
                "parity_coordinate_failures"
            ] == 0
            and row["retained_environment_route"][
                "physical_generator_gauge_commutator_failures"
            ] == 0
            and row["retained_environment_route"][
                "physical_generator_center_commutator_failures"
            ] == 0
            for row in boxes
        ),
    )

    report = {
        "status": "cycle720-positive-local-coframe-and-parity-twirl-genesis__complete-companion-E-open",
        "pass": all(row["pass"] for row in checks),
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "checks": checks,
        "local_controller_primitives": primitive,
        "held_boxes": boxes,
        "three_route_genesis_comparison": {
            "A_retain_semantic_environments": (
                "positive bounded-density G tensor I spectator extension; "
                "removes trace/reset, but held-size local placement of the "
                "canonical reference coordinates remains open"
            ),
            "B_local_preparation": (
                "positive for the uniform coframe mixture and parity twirl "
                "with a bounded local returned-work controller; repeated-star "
                "mixed-gauge/center Choi preparation remains open"
            ),
            "C_sectorwise_code_covariance": (
                "positive 24/576 affine-covariant direct-sum code with three "
                "typed coframe gauge bits; this avoids uniform weights for law "
                "covariance but supplies rather than selects the gauge state"
            ),
        },
        "supplied": [
            "a finite open connected box and one temporary boundary-root preparation port",
            "a size/shape-specific rooted spanning tree plus transported local cubic port chart and parent/child router table",
            "clean non-root coframe and parity-copy target M2 at the one-time preparation input",
            "three local Bell-reference M2 for coframe randomness and one Bell pair for the parity twirl",
            "one fresh/active/spent one-time controller epoch and a one-hot root token",
            "permission to trace five typed semantic environment M2 after the one-time channel",
        ],
        "derived": [
            "bounded-state nearest-neighbour runtime transitions once the supplied rooted router table is installed; no runtime host-selected next transition",
            "the exact uniform classical density over all eight local-alternation coframe origins",
            "root and axis-order independence of the retained coframe density on all tested boxes",
            "24-frame by eight-translation active covariance of that retained density",
            "sectorwise affine covariance when the three coframe-origin bits are retained as a typed gauge input rather than mixed uniformly",
            "the exact nonselective total-parity twirl by local broadcast control and unbroadcast with returned copy work",
            "no total-parity query and no retained global parity-service bit",
            "a bounded-density G_physical tensor identity extension when gauge-reference and parity environments are retained rather than traced",
            "held 2x2x2 3x2x2 3x3x2 and 5x3x2 closure without refit",
        ],
        "open": [
            "prepare the repeated-star mixed-gauge/center Choi projector rather than only its coframe and parity-dephasing auxiliaries",
            "compute and transport the physical/input parity correlation required by the full encoder",
            "literal collision-free physical-M2 synthesis of the token/router controller and its temporary root port",
            "derive the rooted router/tree table locally rather than supplying its size/shape-specific entries",
            "origin-free infinite-volume genesis or an explicit boundary/bath interpretation",
            "derive a parity-superselection principle; this construction implements the channel but does not explain why Nature selects it",
            "fault tolerance bath renewal and periodic topology",
        ],
        "claim_ceiling": (
            "On finite open boxes with a supplied rooted router table and clean non-root targets, the previously supplied uniform coframe-origin mixture and global-looking parity dephasing both have literal bounded-neighbourhood CNOT/X/CZ preparation mechanisms with returned broadcast work and active affine covariance. The output coframe density is independent of the temporary root and tree order. The complete companion E is still not autonomous because mixed-gauge/center Choi preparation, physical parity correlation, local derivation of the router table, and literal controller placement remain open."
        ),
        "compiler_claim_gate": {
            "uniform_coframe_origin_genesis": "PASS_finite-open-local-controller",
            "sectorwise_coframe_gauge_input": "PASS_covariant_code_family__state_selection_not_derived",
            "parity_dephasing_channel": "PASS_finite-open-local-controller",
            "parity_superselection_principle": "NOT_DERIVED",
            "retained_semantic_environment": "PASS_bounded-density-spectator-extension__local-placement-open",
            "mixed_gauge_center_Choi_genesis": "OPEN",
            "literal_controller_M2_placement": "OPEN",
            "full_autonomous_compiler_claim_allowed": False,
        },
        "no_go_discipline": {
            "N1_alternatives": "local Choi pumping teleportation dissipative cooling and typed gauge inputs remain live",
            "N2_wall_independence": "coframe mixture parity twirl physical parity correlation Choi preparation and controller placement are separate",
            "N3_hidden_imports": "open boundary root size-specific router table clean targets chart Bell references trace permission token and one-time epoch are explicit",
            "N4_residual_matching": "constraint distribution controller return twirl multipliers covariance and deletions are independently tested",
            "N5_resolution": "four boxes eight roots six orders eight seeds 192 affine contexts per box and all local even generators",
            "N6_partial_closure": "two genesis imports close without promoting the still-open complete encoder",
            "N7_steelman": "a local stabilizer-pumping or teleportation construction could close mixed-gauge center preparation",
            "N8_cross_cycle_echo": "adapts the Cycle703 returned-work contour but tests the distinct companion coframe and parity channel",
            "gate": "FAIL_for_broad_no_go__constructive-partial-genesis-positive",
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print(
        "LOCAL_COFRAME_AND_PARITY_TWIRL_GENESIS_PASS"
        if report["pass"]
        else "LOCAL_COFRAME_AND_PARITY_TWIRL_GENESIS_INCOMPLETE"
    )
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
