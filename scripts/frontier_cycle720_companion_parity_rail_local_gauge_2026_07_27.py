#!/usr/bin/env python3
"""Cycle-720 local-Z2 realization of the companion channel parity rail.

The repeated-star Choi tensor needs one graded parity bit on every virtual
nearest-neighbour bond.  This probe asks whether that bit is a prohibited
global parity service or an ordinary local gauge rail.  It introduces two
half-edge bits per edge, one edge-equality constraint, and one cell Gauss
constraint.  The constraints are tested against the actual independent Choi
projector charges and against the existing companion relation-center algebra.

All rail cycles are summed.  No Wilson-loop value or total-parity value is
queried by the tensor.  Parity-off-diagonal inputs remain outside the declared
parity-superselected law domain, exactly as in the parent CPTP certificate.
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

from hashlib import sha256
from itertools import product as cartesian_product
import json

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O
import frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27 as R
import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T


Pauli = M.Pauli
Coord = tuple[int, int, int]


def pauli_product(rows) -> Pauli:
    output = Pauli()
    for row in rows:
        output = output @ row
    return output


def edge_key(left: Coord, right: Coord) -> tuple[Coord, Coord]:
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def gf2_rank(rows) -> int:
    return C_RANK(rows)


C_RANK = F.C.R.F.base.gf2_rank


def equation_report(
    cells: tuple[Coord, ...],
    edges: tuple[tuple[int, int], ...],
    charge: int,
    delete_equality: int | None = None,
    delete_gauss: int | None = None,
) -> tuple[int, int]:
    equations = []
    for edge in range(len(edges)):
        if edge == delete_equality:
            continue
        equations.append(((1 << (2 * edge)) | (1 << (2 * edge + 1)), 0))
    for cell in range(len(cells)):
        if cell == delete_gauss:
            continue
        mask = 0
        for edge, (left, right) in enumerate(edges):
            if cell == left:
                mask |= 1 << (2 * edge)
            elif cell == right:
                mask |= 1 << (2 * edge + 1)
        equations.append((mask, (charge >> cell) & 1))
    _solution, rank, contradictions = F.C.gf2_solve(equations)
    return rank, contradictions


def incidence_rows(
    cells: tuple[Coord, ...], edges: tuple[tuple[int, int], ...]
) -> tuple[int, ...]:
    return tuple(
        sum(
            1 << edge
            for edge, (left, right) in enumerate(edges)
            if cell in (left, right)
        )
        for cell in range(len(cells))
    )


def open_plaquette_masks(fixture: M.CompanionFixture) -> tuple[int, ...]:
    lookup = {
        edge_key(fixture.cells[left], fixture.cells[right]): edge
        for edge, (left, right, *_rest) in enumerate(fixture.edges)
    }
    masks = []
    sx, sy, sz = fixture.shape
    for cell in fixture.cells:
        for left_axis in range(3):
            for right_axis in range(left_axis + 1, 3):
                shape = (sx, sy, sz)
                if (
                    cell[left_axis] + 1 >= shape[left_axis]
                    or cell[right_axis] + 1 >= shape[right_axis]
                ):
                    continue
                a = list(cell)
                b = list(cell)
                ab = list(cell)
                a[left_axis] += 1
                b[right_axis] += 1
                ab[left_axis] += 1
                ab[right_axis] += 1
                perimeter = (
                    edge_key(cell, tuple(a)),
                    edge_key(cell, tuple(b)),
                    edge_key(tuple(a), tuple(ab)),
                    edge_key(tuple(b), tuple(ab)),
                )
                masks.append(sum(1 << lookup[edge] for edge in perimeter))
    return tuple(masks)


def local_channel_charge_basis(
    fixture: M.CompanionFixture,
) -> tuple[tuple[Pauli, int], ...]:
    cells = set(fixture.cells)
    lookup = {cell: index for index, cell in enumerate(fixture.cells)}
    choi_qubits = fixture.qubits + fixture.matter_qubits
    tagged = []
    for center in fixture.cells:
        patch_cells = {center} | {
            R.add(center, direction) for direction in R.DIRECTIONS
            if R.add(center, direction) in cells
        }
        patch = O.arbitrary_fixture(patch_cells)
        factor = O.build_factorization(patch)
        domain, local_qubits = O.reduced_channel_domain(
            factor, tuple(patch_cells)
        )
        entries = R.channel_graph_entries(
            patch, factor, patch_cells, fixture, True
        )
        for vector, (row, _support) in zip(domain, entries):
            pulled = O.target_pullback(
                factor,
                vector,
                local_qubits,
                False,
                retain_patch_parity=True,
            )
            charge = 0
            for local_cell, cell in enumerate(patch.cells):
                local_x = (pulled.x >> (6 * local_cell)) & 0x3F
                charge |= (local_x.bit_count() & 1) << lookup[cell]
            tagged.append((row, charge))
    return R.independent_tagged_rows(tuple(tagged), choi_qubits)


def companion_center_cycle_certificate(
    fixture: M.CompanionFixture,
) -> dict[str, object]:
    cell_edges = tuple(
        (left, right) for left, right, *_rest in fixture.edges
    )
    cycles = M.homogeneous_nullspace(
        incidence_rows(fixture.cells, cell_edges), len(cell_edges)
    )
    link_rows = tuple(
        fixture.companion_eta(left, left_mode % 6)
        @ fixture.companion_eta(right, right_mode % 6)
        for left, right, _owner, _axis, left_mode, right_mode in fixture.edges
    )
    cycle_rows = tuple(
        pauli_product(
            link_rows[edge] for edge in range(len(link_rows))
            if (cycle >> edge) & 1
        )
        for cycle in cycles
    )
    factor = O.build_factorization(fixture)
    center_start = factor.logical + factor.gauge
    signed_centers = factor.physical_w[
        center_start:center_start + factor.center - 1
    ]
    center_vectors = tuple(
        row.symplectic(fixture.qubits) for row in signed_centers
    )
    cycle_vectors = tuple(
        row.symplectic(fixture.qubits) for row in cycle_rows
    )
    phase_deltas = []
    signed_coordinate_failures = 0
    for row in cycle_rows:
        combination = U.span_combination(
            row.symplectic(fixture.qubits), center_vectors
        )
        if combination is None:
            signed_coordinate_failures += 1
            continue
        replay = pauli_product(
            signed_centers[index]
            for index in range(len(signed_centers))
            if (combination >> index) & 1
        )
        signed_coordinate_failures += (row.x, row.z) != (replay.x, replay.z)
        phase_deltas.append((row.phase - replay.phase) % 4)
    plaquettes = open_plaquette_masks(fixture)
    physical = tuple(row[1] for row in M.operator_rows(fixture))
    return {
        "graph_cycle_rank": len(cycles),
        "companion_cycle_operator_rank": gf2_rank(cycle_vectors),
        "phase_fixed_nonparity_center_rank": gf2_rank(center_vectors),
        "cycle_rows_outside_center_span": M.span_failures(
            cycle_vectors, center_vectors
        ),
        "center_rows_outside_cycle_span": M.span_failures(
            center_vectors, cycle_vectors
        ),
        "cycle_center_signed_coordinate_failures": signed_coordinate_failures,
        "cycle_center_phase_deltas": tuple(phase_deltas),
        "cycle_center_phase_deltas_are_orientable_signs": all(
            phase in (0, 2) for phase in phase_deltas
        ),
        "cycle_operator_physical_algebra_commutator_failures": sum(
            M.symplectic(
                cycle.symplectic(fixture.qubits),
                generator.symplectic(fixture.qubits),
                fixture.qubits,
            )
            for cycle in cycle_rows for generator in physical
        ),
        "elementary_open_plaquette_count": len(plaquettes),
        "elementary_open_plaquette_rank": gf2_rank(plaquettes),
        "all_open_cycles_generated_by_local_plaquettes": (
            gf2_rank(plaquettes) == len(cycles)
            and M.span_failures(cycles, plaquettes) == 0
        ),
    }


def open_box_certificate(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = M.CompanionFixture.build(shape)
    edges = tuple((left, right) for left, right, *_rest in fixture.edges)
    cells = fixture.cells
    cycle_rank = len(edges) - len(cells) + 1
    charges = local_channel_charge_basis(fixture)
    charge_vectors = tuple(charge for _row, charge in charges)
    constraint_rank, zero_contradictions = equation_report(cells, edges, 0)
    charge_contradictions = tuple(
        equation_report(cells, edges, charge)[1]
        for charge in charge_vectors
    )
    one_odd_charge = 1
    _rank, odd_contradictions = equation_report(
        cells, edges, one_odd_charge
    )
    deleted_equality_odd_contradictions = min(
        equation_report(
            cells, edges, one_odd_charge, delete_equality=edge
        )[1]
        for edge in range(len(edges))
    )
    _rank, deleted_gauss_odd_contradictions = equation_report(
        cells, edges, one_odd_charge, delete_gauss=0
    )
    tensor = R.box_tensor_certificate(shape)
    parent = F.phase_fixed_factorization(shape)
    return {
        "shape": shape,
        "cells": len(cells),
        "edges": len(edges),
        "rail_half_edge_qubits": 2 * len(edges),
        "edge_equality_constraints": len(edges),
        "cell_Gauss_constraints": len(cells),
        "constraint_rank": constraint_rank,
        "rail_solution_dimension_for_every_even_charge": (
            2 * len(edges) - constraint_rank
        ),
        "expected_cycle_dimension": cycle_rank,
        "zero_charge_contradictions": zero_contradictions,
        "independent_Choi_selector_charges": len(charges),
        "Choi_selector_charge_rank": gf2_rank(charge_vectors),
        "expected_complete_even_charge_rank": len(cells) - 1,
        "odd_selector_charge_columns": sum(
            charge.bit_count() & 1 for charge in charge_vectors
        ),
        "Choi_charge_Gauss_contradictions": sum(charge_contradictions),
        "single_odd_charge_rejected": odd_contradictions > 0,
        "delete_one_edge_equality_admits_odd_charge": (
            deleted_equality_odd_contradictions == 0
        ),
        "delete_one_cell_Gauss_admits_odd_charge": (
            deleted_gauss_odd_contradictions == 0
        ),
        "companion_center_cycles": companion_center_cycle_certificate(fixture),
        "both_parity_sector_replay_failures": sum(
            sector["global_from_local_signed_replay_failures"]
            + sector["local_from_global_signed_replay_failures"]
            for sector in tensor["sector_certificates"]
        ),
        "unconditioned_parent_projector_equality": tensor[
            "CPTP_TP_certificate"
        ]["equal_parent_projector_from_signed_span_both_directions"],
        "sector_host_query_used": tensor[
            "sector_summed_parity_channel"
        ]["host_sector_query_used"],
        "factorwise_parent_channel_intertwiner_exact": parent[
            "phase_fixed_intertwiner"
        ]["factorwise_full_word_intertwiner_exact"],
        "gauge_coordinate_failures_under_physical_update": parent[
            "phase_fixed_intertwiner"
        ]["gauge_coordinate_failures_for_every_physical_generator"],
        "repeated_channel_full_update_intertwiner_exact_by_signed_equality": (
            tensor["CPTP_TP_certificate"][
                "equal_parent_projector_from_signed_span_both_directions"
            ]
            and parent["phase_fixed_intertwiner"][
                "factorwise_full_word_intertwiner_exact"
            ]
        ),
    }


def periodic_graph(length: int = 3):
    cells = tuple(cartesian_product(range(length), repeat=3))
    lookup = {cell: index for index, cell in enumerate(cells)}
    edges = []
    edge_lookup = {}
    for cell in cells:
        for axis in range(3):
            target = list(cell)
            target[axis] = (target[axis] + 1) % length
            target = tuple(target)
            key = edge_key(cell, target)
            if key in edge_lookup:
                continue
            edge_lookup[key] = len(edges)
            edges.append((lookup[key[0]], lookup[key[1]]))
    return cells, tuple(edges), edge_lookup


def periodic_plaquettes(
    length: int,
    cells: tuple[Coord, ...],
    edge_lookup: dict[tuple[Coord, Coord], int],
) -> tuple[int, ...]:
    masks = []
    for cell in cells:
        for left_axis in range(3):
            for right_axis in range(left_axis + 1, 3):
                a = list(cell)
                b = list(cell)
                ab = list(cell)
                a[left_axis] = (a[left_axis] + 1) % length
                b[right_axis] = (b[right_axis] + 1) % length
                ab[left_axis] = (ab[left_axis] + 1) % length
                ab[right_axis] = (ab[right_axis] + 1) % length
                perimeter = (
                    edge_key(cell, tuple(a)),
                    edge_key(cell, tuple(b)),
                    edge_key(tuple(a), tuple(ab)),
                    edge_key(tuple(b), tuple(ab)),
                )
                masks.append(sum(
                    1 << edge_lookup[edge] for edge in perimeter
                ))
    return tuple(masks)


def frame_tuple(frame) -> tuple[Coord, Coord, Coord]:
    return tuple(
        tuple(int(value) for value in row) for row in frame
    )  # type: ignore[return-value]


def matvec_mod(frame, cell: Coord, length: int) -> Coord:
    return tuple(
        int(value) % length for value in frame @ np.asarray(cell, dtype=int)
    )


def periodic_certificate(length: int = 3) -> dict[str, object]:
    cells, edges, edge_lookup = periodic_graph(length)
    cycle_rank = len(edges) - len(cells) + 1
    plaquettes = periodic_plaquettes(length, cells, edge_lookup)
    plaquette_rank = gf2_rank(plaquettes)
    constraint_rank, contradictions = equation_report(cells, edges, 0)
    odd_contradictions = equation_report(cells, edges, 1)[1]
    frames = tuple(frame_tuple(frame) for frame in T.proper_cubic_frames())
    frame_index = {frame: index for index, frame in enumerate(frames)}

    def compose(left, right):
        return tuple(tuple(
            sum(left[row][middle] * right[middle][column]
                for middle in range(3))
            for column in range(3)
        ) for row in range(3))

    cell_permutations = []
    edge_permutations = []
    frame_failures = 0
    plaquette_span_failures = 0
    for frame in frames:
        cell_map = tuple(
            cells.index(matvec_mod(np.asarray(frame), cell, length))
            for cell in cells
        )
        edge_map = []
        for left, right in edges:
            key = edge_key(
                cells[cell_map[left]], cells[cell_map[right]]
            )
            if key not in edge_lookup:
                frame_failures += 1
                continue
            edge_map.append(edge_lookup[key])
        cell_permutations.append(cell_map)
        edge_permutations.append(tuple(edge_map))
        transformed_plaquettes = tuple(
            sum(
                1 << edge_map[edge]
                for edge in range(len(edges)) if (row >> edge) & 1
            )
            for row in plaquettes
        )
        plaquette_span_failures += M.span_failures(
            transformed_plaquettes, plaquettes
        )
    product_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            target = frame_index[compose(left, right)]
            product_failures += tuple(
                cell_permutations[left_index][
                    cell_permutations[right_index][cell]
                ]
                for cell in range(len(cells))
            ) != cell_permutations[target]
            product_failures += tuple(
                edge_permutations[left_index][
                    edge_permutations[right_index][edge]
                ]
                for edge in range(len(edges))
            ) != edge_permutations[target]
    return {
        "topology": f"periodic_{length}x{length}x{length}",
        "cells": len(cells),
        "edges": len(edges),
        "cycle_rank": cycle_rank,
        "local_plaquette_rank": plaquette_rank,
        "noncontractible_Z2_holonomy_rank": cycle_rank - plaquette_rank,
        "rail_constraint_rank": constraint_rank,
        "rail_solution_dimension": 2 * len(edges) - constraint_rank,
        "zero_charge_contradictions": contradictions,
        "single_odd_charge_rejected": odd_contradictions > 0,
        "topological_sector_policy": (
            "all rail-loop sectors are summed; fixing a flat Wilson sector "
            "would import three bits, but this tensor fixes none"
        ),
        "proper_cubic_frames": len(frames),
        "frame_incidence_failures": frame_failures,
        "frame_plaquette_span_failures": plaquette_span_failures,
        "ordered_frame_products": len(frames) ** 2,
        "frame_product_permutation_failures": product_failures,
    }


def main() -> None:
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
    boxes = tuple(open_box_certificate(shape) for shape in shapes)
    periodic = periodic_certificate()
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "local edge equality plus cell Gauss constraints solve every actual Choi selector charge with constant cycle multiplicity",
        all(
            row["zero_charge_contradictions"] == 0
            and row["Choi_charge_Gauss_contradictions"] == 0
            and row["rail_solution_dimension_for_every_even_charge"]
            == row["expected_cycle_dimension"]
            and row["Choi_selector_charge_rank"]
            == row["expected_complete_even_charge_rank"]
            and row["odd_selector_charge_columns"] == 0
            for row in boxes
        ),
    )
    check(
        "the virtual rail cycle algebra is exactly the existing phase-oriented local companion-center algebra",
        all(
            row["companion_center_cycles"]["graph_cycle_rank"]
            == row["companion_center_cycles"][
                "companion_cycle_operator_rank"
            ]
            == row["companion_center_cycles"][
                "phase_fixed_nonparity_center_rank"
            ]
            and row["companion_center_cycles"][
                "cycle_rows_outside_center_span"
            ] == 0
            and row["companion_center_cycles"][
                "center_rows_outside_cycle_span"
            ] == 0
            and row["companion_center_cycles"][
                "cycle_center_signed_coordinate_failures"
            ] == 0
            and row["companion_center_cycles"][
                "cycle_center_phase_deltas_are_orientable_signs"
            ]
            and row["companion_center_cycles"][
                "cycle_operator_physical_algebra_commutator_failures"
            ] == 0
            and row["companion_center_cycles"][
                "all_open_cycles_generated_by_local_plaquettes"
            ]
            for row in boxes
        ),
    )
    check(
        "the rail contraction uses the same tensor in both parity sectors with no host query",
        all(
            row["both_parity_sector_replay_failures"] == 0
            and row["unconditioned_parent_projector_equality"]
            and row["sector_host_query_used"] is False
            for row in boxes
        ),
    )
    check(
        "edge-equality and cell-Gauss deletions actively admit a forbidden odd charge",
        all(
            row["single_odd_charge_rejected"]
            and row["delete_one_edge_equality_admits_odd_charge"]
            and row["delete_one_cell_Gauss_admits_odd_charge"]
            for row in boxes
        ),
    )
    check(
        "the periodic rail sums rather than supplies its three holonomies and is 24/576 covariant",
        periodic["noncontractible_Z2_holonomy_rank"] == 3
        and periodic["rail_solution_dimension"] == periodic["cycle_rank"]
        and periodic["zero_charge_contradictions"] == 0
        and periodic["single_odd_charge_rejected"]
        and periodic["proper_cubic_frames"] == 24
        and periodic["ordered_frame_products"] == 576
        and periodic["frame_incidence_failures"] == 0
        and periodic["frame_plaquette_span_failures"] == 0
        and periodic["frame_product_permutation_failures"] == 0,
    )
    check(
        "the repeated local tensor inherits the exact free seam contact full-update channel intertwiner on every held box",
        all(
            row["factorwise_parent_channel_intertwiner_exact"]
            and row["gauge_coordinate_failures_under_physical_update"] == 0
            and row[
                "repeated_channel_full_update_intertwiner_exact_by_signed_equality"
            ]
            for row in boxes
        ),
    )

    report = {
        "status": "cycle720-positive-local-Z2-parity-rail__M2-Stinespring-and-active-content-covariance-open",
        "pass": all(row["pass"] for row in checks),
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "checks": checks,
        "open_boxes": boxes,
        "periodic_loop_topology": periodic,
        "rail_contraction_theorem": (
            "For each projector selection, the cell odd-parity charges are an "
            "even vector. Half-edge equality and cell Gauss equations therefore "
            "have exactly 2^(E-N+1) solutions, independent of the selection. "
            "Summing all rail solutions multiplies every signed projector term "
            "by the same factor, removed by Choi normalization."
        ),
        "supplied": [
            "the parity-superselected law domain; parity-off-diagonal coherences remain erased",
            "local phase orientations of the already existing R2 companion-center constraints",
            "maximally mixed gauge/reference preparation from the parent channel",
            "the fixed local matter/companion port convention",
        ],
        "derived": [
            "one explicit edge-local Z2 half-rail and cell-local Gauss/equality constraint system",
            "constant-multiplicity contraction for the complete even selector-charge space",
            "exact equality of rail cycles and the existing companion nonparity center algebra at ranks 5,9,16,30",
            "generation of every open-box cycle by local elementary plaquettes",
            "sector-summed even/odd operation with no host parity query",
            "periodic three-holonomy sectors summed rather than fixed or supplied",
            "active equality and Gauss deletions",
            "exact inherited repeated-channel free/seam/contact intertwiner",
            "24/576 covariance of the rail incidence, plaquette span, and permutations",
        ],
        "open": [
            "a literal 2x2x2 Clifford/Stinespring circuit on M2 sites with semantic environments separated from returned work",
            "active 24/576 covariance of the signed companion Choi content, not only the rail incidence/plaquette tensor",
            "autonomous local preparation/enforcement of the phase-oriented center sector and maximally mixed gauge",
            "derive rather than supply the parity-superselected law domain",
            "time, source/gravity, Record, and Born/history bridges",
        ],
        "claim_ceiling": (
            "The virtual parity rail is constructively realized as bounded local "
            "Z2 gauge structure, and on open boxes it is exactly the already "
            "present companion-center cycle algebra. It is not a global parity "
            "query or fixed Wilson service. Full compiler closure remains false "
            "until center/gauge preparation, literal M2 Stinespring execution, "
            "and active signed-content covariance close."
        ),
        "compiler_claim_gate": {
            "local_Z2_parity_rail": "PASS",
            "no_host_parity_query": "PASS",
            "open_box_topological_supply": "NONE",
            "periodic_holonomy_policy": "PASS_all_three_summed_not_fixed",
            "repeated_channel_update_intertwiner": "PASS",
            "literal_M2_Stinespring": "OPEN",
            "active_signed_content_covariance": "OPEN",
            "full_autonomous_compiler_claim_allowed": False,
        },
        "no_go_discipline": {
            "N1_alternatives": "local gauge rails, direct fermionic tensors, dissipative centers, pure dilations, and alternate Pin lifts remain live",
            "N2_wall_independence": "rail locality closes separately from center genesis, Stinespring execution, and signed content covariance",
            "N3_hidden_imports": "law-domain superselection, center phases, gauge mixture/reference, port order, and topology are explicit",
            "N4_residual_matching": "constraint ranks, signed center spans, sector replay, deletions, topology, covariance, and update intertwining are separate",
            "N5_resolution": "four held open boxes and one 3x3x3 periodic topology without refit",
            "N6_partial_closure": "the local rail is retained without promoting the still-open autonomous compiler",
            "N7_steelman": "a local stabilizer-pumping Stinespring may prepare the same center/gauge tensor with returned work",
            "N8_cross_cycle_echo": "identifies the tensor rail with the previously independent R2 companion-center ranks",
            "gate": "FAIL_for_broad_no_go__constructive_local-gauge-positive",
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print("LOCAL_Z2_PARITY_RAIL_POSITIVE__M2_STINESPRING_AND_SIGNED_CONTENT_COVARIANCE_OPEN")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
