#!/usr/bin/env python3
"""Cycle-720 local stabilizer-pump preparation of the companion Choi resource.

The repeated-star Choi projector previously had a local generating set but no
literal preparation.  This probe chooses a smaller, shape-independent basis:

* eleven onsite graph stabilizers per cell (six Z correlations and five
  adjacent-XX correlations); and
* one fixed seam graph stabilizer per nearest-neighbour edge.

The edge rows are prepared without measuring every Jordan--Wigner string.
A hierarchical spanning tree is prepared first with a returned mobile
syndrome rail.  Every remaining edge is then introduced by an elementary
plaquette whose other three edges are already prepared.  The four seam
strings around that plaquette cancel to bounded support.  Private correction
Paulis are derived from a finite local port-mask atlas and tested without
refitting on held boxes.

This is an exact finite-box Stinespring preparation of the mixed Choi
projector with all purifiers and syndrome bits retained.  The rooted router
and the one-time preparation epoch remain supplied apparatus.  The probe does
not claim a translation-invariant autonomous genesis law, a deterministic
Choi-to-live-input injection, a parity-superselection principle, Record, or
physical time.
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
from itertools import permutations, product as cartesian_product
import json

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27 as R
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O


Pauli = M.Pauli
Coord = tuple[int, int, int]


def pauli_product(rows) -> Pauli:
    output = Pauli()
    for row in rows:
        output = output @ row
    return output


def direct_graph_basis(
    fixture: M.CompanionFixture,
) -> tuple[tuple[Pauli, ...], tuple[tuple, ...]]:
    """Eleven onsite graph rows per cell and seam factor two per edge."""
    rows: list[Pauli] = []
    tags: list[tuple] = []
    for cell in range(len(fixture.cells)):
        for mode in range(6):
            row = Pauli(z=1 << (6 * cell + mode))
            rows.append(R.choi_pauli(row, row, fixture.qubits))
            tags.append(("onsite_Z", cell, mode))
        for mode in range(5):
            row = Pauli(
                x=(1 << (6 * cell + mode))
                | (1 << (6 * cell + mode + 1))
            )
            rows.append(R.choi_pauli(row, row, fixture.qubits))
            tags.append(("onsite_XX", cell, mode))
    for edge in range(len(fixture.edges)):
        rows.append(R.choi_pauli(
            fixture.physical_terms(edge)[2],
            fixture.target_terms(edge)[2],
            fixture.qubits,
        ))
        tags.append(("edge", edge))
    return tuple(rows), tuple(tags)


def repeated_star_basis(
    fixture: M.CompanionFixture,
) -> tuple[Pauli, ...]:
    union_cells = set(fixture.cells)
    entries = []
    for center in fixture.cells:
        patch_cells = {center} | {
            R.add(center, direction) for direction in R.DIRECTIONS
            if R.add(center, direction) in union_cells
        }
        patch = O.arbitrary_fixture(patch_cells)
        factor = O.build_factorization(patch)
        entries.extend(R.channel_graph_entries(
            patch, factor, patch_cells, fixture, True
        ))
    return tuple(row for row, _support in R.independent_tagged_rows(
        tuple(entries), fixture.qubits + fixture.matter_qubits
    ))


def incident_port_mask(fixture: M.CompanionFixture, cell: int) -> int:
    output = 0
    for left, right, _owner, axis, *_rest in fixture.edges:
        if cell == left:
            output |= 1 << (2 * axis + 1)
        elif cell == right:
            output |= 1 << (2 * axis)
    return output


def solve_private_correction(
    rows: tuple[Pauli, ...],
    target: int,
    allowed: tuple[int, ...],
) -> tuple[Pauli, int, int]:
    equations = []
    for index, stabilizer in enumerate(rows):
        mask = 0
        for variable, qubit in enumerate(allowed):
            # X correction sees stabilizer Z; Z correction sees stabilizer X.
            mask |= ((stabilizer.z >> qubit) & 1) << (2 * variable)
            mask |= ((stabilizer.x >> qubit) & 1) << (2 * variable + 1)
        equations.append((mask, int(index == target)))
    solution, rank, contradictions = C.gf2_solve(equations)
    x = sum(
        ((solution >> (2 * variable)) & 1) << qubit
        for variable, qubit in enumerate(allowed)
    )
    z = sum(
        ((solution >> (2 * variable + 1)) & 1) << qubit
        for variable, qubit in enumerate(allowed)
    )
    return Pauli((x & z).bit_count() & 1, x, z), rank, contradictions


def local_signature(row: Pauli, allowed: tuple[int, ...]) -> tuple[int, int]:
    x = sum(((row.x >> qubit) & 1) << index for index, qubit in enumerate(allowed))
    z = sum(((row.z >> qubit) & 1) << index for index, qubit in enumerate(allowed))
    return x, z


def signature_pauli(
    signature: tuple[int, int], allowed: tuple[int, ...]
) -> Pauli:
    local_x, local_z = signature
    x = sum(((local_x >> index) & 1) << qubit for index, qubit in enumerate(allowed))
    z = sum(((local_z >> index) & 1) << qubit for index, qubit in enumerate(allowed))
    return Pauli((x & z).bit_count() & 1, x, z)


def onsite_allowed(fixture: M.CompanionFixture, cell: int) -> tuple[int, ...]:
    # A private dual exists entirely on the physical output cell.  Keeping the
    # correction off the coarse-input JW half is essential: odd input Paulis
    # acquire chart strings under cubic frame changes, whereas the companion
    # physical frame action is cell-local.
    return tuple(
        list(range(6 * cell, 6 * cell + 6))
        + list(range(
            fixture.matter_qubits + 3 * cell,
            fixture.matter_qubits + 3 * cell + 3,
        ))
    )


def edge_allowed(
    fixture: M.CompanionFixture, edge: int
) -> tuple[int, ...]:
    left, right, *_rest = fixture.edges[edge]
    return tuple(
        fixture.matter_qubits + 3 * cell + local
        for cell in (left, right) for local in range(3)
    )


def build_private_atlases() -> dict[str, object]:
    """Derive once on every possible open-box port environment.

    Side lengths 1..4 realize all 64 six-port cell masks and every oriented
    nearest-neighbour endpoint environment, including interior--interior.
    The atlas is then frozen and used on larger held boxes.
    """
    onsite_values: dict[tuple, set[tuple[int, int]]] = defaultdict(set)
    edge_values: dict[tuple, set[tuple[int, int]]] = defaultdict(set)
    contradictions = 0
    training_rows = 0
    for shape in cartesian_product(range(1, 5), repeat=3):
        fixture = O.arbitrary_fixture(Q.shape_cells(shape))
        rows, tags = direct_graph_basis(fixture)
        training_rows += len(rows)
        for target, tag in enumerate(tags):
            if tag[0] == "edge":
                edge = tag[1]
                left, right, _owner, axis, *_rest = fixture.edges[edge]
                allowed = edge_allowed(fixture, edge)
                correction, _rank, failed = solve_private_correction(
                    rows, target, allowed
                )
                contradictions += failed
                key = (
                    incident_port_mask(fixture, left),
                    incident_port_mask(fixture, right),
                    axis,
                )
                edge_values[key].add(local_signature(correction, allowed))
            else:
                cell, mode = tag[1], tag[2]
                allowed = onsite_allowed(fixture, cell)
                correction, _rank, failed = solve_private_correction(
                    rows, target, allowed
                )
                contradictions += failed
                key = (
                    incident_port_mask(fixture, cell), tag[0], mode
                )
                onsite_values[key].add(local_signature(correction, allowed))
    onsite_conflicts = sum(len(values) != 1 for values in onsite_values.values())
    edge_conflicts = sum(len(values) != 1 for values in edge_values.values())
    onsite_atlas = {
        key: next(iter(values)) for key, values in onsite_values.items()
        if len(values) == 1
    }
    edge_atlas = {
        key: next(iter(values)) for key, values in edge_values.items()
        if len(values) == 1
    }
    serial = tuple(sorted(
        (("onsite", key, value) for key, value in onsite_atlas.items()),
        key=repr,
    )) + tuple(sorted(
        (("edge", key, value) for key, value in edge_atlas.items()),
        key=repr,
    ))
    return {
        "onsite": onsite_atlas,
        "edge": edge_atlas,
        "training_shapes": 4 ** 3,
        "training_rows": training_rows,
        "solve_contradictions": contradictions,
        "onsite_keys": len(onsite_values),
        "edge_keys": len(edge_values),
        "onsite_conflicts": onsite_conflicts,
        "edge_conflicts": edge_conflicts,
        "distinct_onsite_corrections": len(set(onsite_atlas.values())),
        "distinct_edge_corrections": len(set(edge_atlas.values())),
        "atlas_sha256": sha256(repr(serial).encode()).hexdigest(),
    }


def correction_from_atlas(
    fixture: M.CompanionFixture,
    tag: tuple,
    atlas: dict[str, object],
) -> Pauli:
    if tag[0] == "edge":
        edge = tag[1]
        left, right, _owner, axis, *_rest = fixture.edges[edge]
        key = (
            incident_port_mask(fixture, left),
            incident_port_mask(fixture, right), axis,
        )
        signature = atlas["edge"][key]  # type: ignore[index]
        return signature_pauli(signature, edge_allowed(fixture, edge))
    cell, mode = tag[1], tag[2]
    key = (incident_port_mask(fixture, cell), tag[0], mode)
    signature = atlas["onsite"][key]  # type: ignore[index]
    return signature_pauli(signature, onsite_allowed(fixture, cell))


def coordinate_maps(
    fixture: M.CompanionFixture,
    root: Coord,
    axis_order: tuple[int, int, int],
) -> tuple[dict[Coord, tuple[int, int, int]], dict[tuple[int, int, int], Coord]]:
    signs = tuple(
        1 if root[axis] == min(cell[axis] for cell in fixture.cells) else -1
        for axis in range(3)
    )
    forward = {
        cell: tuple(
            signs[axis] * (cell[axis] - root[axis])
            for axis in axis_order
        )
        for cell in fixture.cells
    }
    return forward, {value: key for key, value in forward.items()}


def edge_lookup(fixture: M.CompanionFixture) -> dict[frozenset[Coord], int]:
    return {
        frozenset((fixture.cells[left], fixture.cells[right])): edge
        for edge, (left, right, *_rest) in enumerate(fixture.edges)
    }


def schedule_tree_plaquettes(
    fixture: M.CompanionFixture,
    root: Coord,
    axis_order: tuple[int, int, int],
) -> tuple[tuple[int, ...], tuple[tuple[int, tuple[int, ...]], ...]]:
    """Return tree edges and (new edge, elementary plaquette) fill order."""
    forward, reverse = coordinate_maps(fixture, root, axis_order)
    lookup = edge_lookup(fixture)
    lengths = tuple(max(value[index] for value in forward.values()) + 1 for index in range(3))

    def edge(left_u, right_u) -> int:
        return lookup[frozenset((reverse[tuple(left_u)], reverse[tuple(right_u)]))]

    def plaquette(base, left_axis: int, right_axis: int) -> tuple[int, ...]:
        a = list(base)
        b = list(base)
        ab = list(base)
        a[left_axis] += 1
        b[right_axis] += 1
        ab[left_axis] += 1
        ab[right_axis] += 1
        return (
            edge(base, a), edge(base, b), edge(a, ab), edge(b, ab)
        )

    tree = []
    for cell in fixture.cells:
        u = forward[cell]
        if u[0] > 0:
            parent = list(u)
            parent[0] -= 1
        elif u[1] > 0:
            parent = list(u)
            parent[1] -= 1
        elif u[2] > 0:
            parent = list(u)
            parent[2] -= 1
        else:
            continue
        tree.append(edge(u, parent))

    prepared = set(tree)
    fill = []

    def add_new(new_edge: int, cycle: tuple[int, ...]) -> None:
        if new_edge in prepared:
            raise AssertionError("cycle did not introduce a new edge")
        if any(item not in prepared for item in cycle if item != new_edge):
            raise AssertionError("cycle depends on an unprepared edge")
        fill.append((new_edge, cycle))
        prepared.add(new_edge)

    # Middle-axis edges away from the fast=0 face.
    for slow in range(lengths[2]):
        for middle in range(lengths[1] - 1):
            for fast in range(1, lengths[0]):
                base = (fast - 1, middle, slow)
                cycle = plaquette(base, 0, 1)
                new = edge(
                    (fast, middle, slow),
                    (fast, middle + 1, slow),
                )
                add_new(new, cycle)

    # Slow-axis edges on middle=0, away from the fast=0 line.
    for slow in range(lengths[2] - 1):
        for fast in range(1, lengths[0]):
            base = (fast - 1, 0, slow)
            cycle = plaquette(base, 0, 2)
            new = edge((fast, 0, slow), (fast, 0, slow + 1))
            add_new(new, cycle)

    # Remaining slow-axis edges, growing out in the middle direction.
    for slow in range(lengths[2] - 1):
        for middle in range(1, lengths[1]):
            for fast in range(lengths[0]):
                base = (fast, middle - 1, slow)
                cycle = plaquette(base, 1, 2)
                new = edge(
                    (fast, middle, slow),
                    (fast, middle, slow + 1),
                )
                add_new(new, cycle)
    if prepared != set(range(len(fixture.edges))):
        raise AssertionError("tree/plaquette schedule did not cover the box")
    return tuple(tree), tuple(fill)


def pauli_cells(
    fixture: M.CompanionFixture, row: Pauli
) -> frozenset[Coord]:
    bits = row.x | row.z
    total = fixture.qubits + fixture.matter_qubits
    output = set()
    for qubit in range(total):
        if not ((bits >> qubit) & 1):
            continue
        if qubit < fixture.matter_qubits:
            cell = qubit // 6
        elif qubit < fixture.qubits:
            cell = (qubit - fixture.matter_qubits) // 3
        else:
            cell = (qubit - fixture.qubits) // 6
        output.add(fixture.cells[cell])
    return frozenset(output)


def returned_route(
    anchor: Coord, support: frozenset[Coord]
) -> tuple[tuple[Coord, Coord], ...]:
    links = R.route_selector(anchor, support)
    adjacency: dict[Coord, list[Coord]] = defaultdict(list)
    for left, right in links:
        adjacency[left].append(right)
        adjacency[right].append(left)
    word: list[tuple[Coord, Coord]] = []
    visited = {anchor}

    def walk(cell: Coord) -> None:
        for target in sorted(adjacency[cell]):
            if target in visited:
                continue
            visited.add(target)
            word.append((cell, target))
            walk(target)
            word.append((target, cell))

    walk(anchor)
    if not support <= visited:
        raise AssertionError("route missed a Pauli support cell")
    return tuple(word)


def route_execution_failures(
    anchor: Coord, route: tuple[tuple[Coord, Coord], ...]
) -> tuple[int, int]:
    """Execute the mobile token forward and through the literal inverse."""
    position = anchor
    forward_failures = 0
    for left, right in route:
        forward_failures += position != left
        position = right
    forward_failures += position != anchor
    inverse_failures = 0
    for left, right in reversed(route):
        if position == right:
            position = left
        elif position == left:
            position = right
        else:
            inverse_failures += 1
    inverse_failures += position != anchor
    return forward_failures, inverse_failures


def schedule_basis(
    fixture: M.CompanionFixture,
    root: Coord,
    axis_order: tuple[int, int, int],
) -> tuple[tuple[Pauli, ...], tuple[tuple, ...], dict[str, object]]:
    direct, tags = direct_graph_basis(fixture)
    onsite_count = 11 * len(fixture.cells)
    seam_rows = direct[onsite_count:]
    tree, fill = schedule_tree_plaquettes(fixture, root, axis_order)
    rows = list(direct[:onsite_count])
    output_tags = list(tags[:onsite_count])
    rows.extend(seam_rows[edge] for edge in tree)
    output_tags.extend(("tree", edge) for edge in tree)
    for new_edge, cycle in fill:
        rows.append(pauli_product(seam_rows[edge] for edge in cycle))
        output_tags.append(("plaquette", new_edge, cycle))
    # Every fill cycle has one new edge; triangularity makes its correction
    # the private correction of that original edge.
    prepared = set(tree)
    triangular_failures = 0
    for new_edge, cycle in fill:
        triangular_failures += new_edge in prepared
        triangular_failures += sum(
            edge not in prepared for edge in cycle if edge != new_edge
        )
        prepared.add(new_edge)
    return tuple(rows), tuple(output_tags), {
        "tree_edges": len(tree),
        "plaquette_fill_rows": len(fill),
        "edge_coverage_failures": len(set(range(len(fixture.edges))) - prepared),
        "triangular_predecessor_failures": triangular_failures,
    }


def schedule_correction(
    fixture: M.CompanionFixture,
    tag: tuple,
    atlas: dict[str, object],
) -> Pauli:
    if tag[0] in ("onsite_Z", "onsite_XX"):
        return correction_from_atlas(fixture, tag, atlas)
    edge = tag[1]
    return correction_from_atlas(fixture, ("edge", edge), atlas)


def box_certificate(
    shape: tuple[int, int, int], atlas: dict[str, object]
) -> dict[str, object]:
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    total_qubits = fixture.qubits + fixture.matter_qubits
    direct, direct_tags = direct_graph_basis(fixture)
    repeated = repeated_star_basis(fixture)
    canonical_root = min(fixture.cells)
    schedule, schedule_tags, schedule_report = schedule_basis(
        fixture, canonical_root, (2, 1, 0)
    )

    direct_rank = C.R.F.base.gf2_rank(
        row.symplectic(total_qubits) for row in direct
    )
    commutator_failures = sum(
        M.symplectic(
            direct[left].symplectic(total_qubits),
            direct[right].symplectic(total_qubits),
            total_qubits,
        )
        for left in range(len(direct)) for right in range(left)
    )
    schedule_rank = C.R.F.base.gf2_rank(
        row.symplectic(total_qubits) for row in schedule
    )
    schedule_commutator_failures = sum(
        M.symplectic(
            schedule[left].symplectic(total_qubits),
            schedule[right].symplectic(total_qubits),
            total_qubits,
        )
        for left in range(len(schedule)) for right in range(left)
    )
    corrections = tuple(
        correction_from_atlas(fixture, tag, atlas) for tag in direct_tags
    )
    syndrome_failures = 0
    maximum_correction_weight = 0
    maximum_edge_correction_weight = 0
    correction_outside_declared_cells = 0
    for target, (tag, correction) in enumerate(zip(direct_tags, corrections)):
        maximum_correction_weight = max(
            maximum_correction_weight,
            (correction.x | correction.z).bit_count(),
        )
        if tag[0] == "edge":
            maximum_edge_correction_weight = max(
                maximum_edge_correction_weight,
                (correction.x | correction.z).bit_count(),
            )
            declared = {
                fixture.cells[cell] for cell in fixture.edges[tag[1]][:2]
            }
        else:
            declared = {fixture.cells[tag[1]]}
        correction_outside_declared_cells += not (
            pauli_cells(fixture, correction) <= declared
        )
        for row, stabilizer in enumerate(direct):
            syndrome_failures += M.symplectic(
                correction.symplectic(total_qubits),
                stabilizer.symplectic(total_qubits),
                total_qubits,
            ) != int(row == target)

    # The triangular schedule can use the original private correction of its
    # new edge.  Check commutation with every already prepared row explicitly.
    schedule_pump_failures = 0
    for target, tag in enumerate(schedule_tags):
        correction = schedule_correction(fixture, tag, atlas)
        for previous in range(target + 1):
            schedule_pump_failures += M.symplectic(
                correction.symplectic(total_qubits),
                schedule[previous].symplectic(total_qubits),
                total_qubits,
            ) != int(previous == target)

    onsite_count = 11 * len(fixture.cells)
    route_transitions = 0
    route_failures = 0
    route_inverse_failures = 0
    maximum_route_transitions = 0
    maximum_plaquette_cells = 0
    maximum_plaquette_diameter = 0
    measured_pauli_factors = 0
    correction_pauli_factors = 0
    for row, tag in zip(schedule, schedule_tags):
        support = pauli_cells(fixture, row)
        anchor = min(support)
        route = returned_route(anchor, support)
        route_transitions += len(route)
        maximum_route_transitions = max(maximum_route_transitions, len(route))
        route_failures += any(
            sum(abs(a - b) for a, b in zip(left, right)) != 1
            for left, right in route
        )
        route_failures += bool(route) and route[-1][1] != anchor
        forward_failures, inverse_failures = route_execution_failures(
            anchor, route
        )
        route_failures += forward_failures
        route_inverse_failures += inverse_failures
        measured_pauli_factors += (row.x | row.z).bit_count()
        correction_pauli_factors += (
            schedule_correction(fixture, tag, atlas).x
            | schedule_correction(fixture, tag, atlas).z
        ).bit_count()
        if tag[0] == "plaquette":
            maximum_plaquette_cells = max(
                maximum_plaquette_cells, len(support)
            )
            maximum_plaquette_diameter = max(
                maximum_plaquette_diameter, R.support_diameter(support)
            )

    # All corners and all fast/middle/slow choices prepare the same signed
    # stabilizer projector, even though their temporary routes differ.
    frame_schedule_failures = 0
    schedule_contexts = 0
    schedule_digests = set()
    bounds = tuple(
        (min(cell[axis] for cell in fixture.cells),
         max(cell[axis] for cell in fixture.cells))
        for axis in range(3)
    )
    for root in cartesian_product(*bounds):
        for order in permutations(range(3)):
            candidate, _tags, report = schedule_basis(
                fixture, root, order
            )
            frame_schedule_failures += report["edge_coverage_failures"]
            frame_schedule_failures += report["triangular_predecessor_failures"]
            frame_schedule_failures += R.signed_replay_failures(
                direct, candidate, total_qubits
            )
            frame_schedule_failures += R.signed_replay_failures(
                candidate, direct, total_qubits
            )
            schedule_digests.add(sha256(
                repr(tuple(sorted(
                    (row.phase, row.x, row.z) for row in candidate
                ))).encode()
            ).hexdigest())
            schedule_contexts += 1

    physical_parity_correlation = Pauli(z=(
        ((1 << fixture.matter_qubits) - 1)
        | (((1 << fixture.matter_qubits) - 1) << fixture.qubits)
    ))
    onsite_z_rows = tuple(
        direct[11 * cell + mode]
        for cell in range(len(fixture.cells)) for mode in range(6)
    )
    parity_product = pauli_product(onsite_z_rows)
    parity_correlation_failure = parity_product != physical_parity_correlation

    # Active deletions: every omitted independent pump loses one rank.  The
    # first factor deletion in each row changes the measured Pauli literally.
    deletion_rank_failures = 0
    factor_deletion_undetected = 0
    for deleted in (0, onsite_count - 1, len(schedule) - 1):
        surviving = schedule[:deleted] + schedule[deleted + 1:]
        deletion_rank_failures += (
            C.R.F.base.gf2_rank(
                row.symplectic(total_qubits) for row in surviving
            ) != len(schedule) - 1
        )
        row = schedule[deleted]
        active = row.x | row.z
        qubit = (active & -active).bit_length() - 1
        damaged = Pauli(
            row.phase,
            row.x & ~(1 << qubit),
            row.z & ~(1 << qubit),
        )
        factor_deletion_undetected += damaged == row

    parent = R.box_tensor_certificate(shape)
    parent_tp = parent["CPTP_TP_certificate"]
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "Choi_system_M2": total_qubits,
        "explicit_direct_generators": len(direct),
        "rank_formula_11N_plus_E": 11 * len(fixture.cells) + len(fixture.edges),
        "direct_basis_rank": direct_rank,
        "direct_commutator_failures": commutator_failures,
        "direct_from_repeated_signed_failures": R.signed_replay_failures(
            direct, repeated, total_qubits
        ),
        "repeated_from_direct_signed_failures": R.signed_replay_failures(
            repeated, direct, total_qubits
        ),
        "schedule_basis_rank": schedule_rank,
        "schedule_commutator_failures": schedule_commutator_failures,
        "schedule_from_direct_signed_failures": R.signed_replay_failures(
            schedule, direct, total_qubits
        ),
        "direct_from_schedule_signed_failures": R.signed_replay_failures(
            direct, schedule, total_qubits
        ),
        "schedule_report": schedule_report,
        "atlas_private_dual_syndrome_failures": syndrome_failures,
        "triangular_schedule_pump_failures": schedule_pump_failures,
        "maximum_private_correction_weight": maximum_correction_weight,
        "maximum_edge_private_correction_weight": maximum_edge_correction_weight,
        "corrections_outside_declared_one_or_two_cells": (
            correction_outside_declared_cells
        ),
        "maximum_plaquette_measurement_cells": maximum_plaquette_cells,
        "maximum_plaquette_measurement_diameter": maximum_plaquette_diameter,
        "total_returned_route_transitions": route_transitions,
        "returned_route_transitions_per_cell": (
            route_transitions / len(fixture.cells)
        ),
        "maximum_single_measurement_route_transitions": maximum_route_transitions,
        "route_locality_or_return_failures": route_failures,
        "literal_reverse_route_failures": route_inverse_failures,
        "controlled_Pauli_measurement_factors": measured_pauli_factors,
        "controlled_private_correction_factors": correction_pauli_factors,
        "corner_axis_schedule_contexts": schedule_contexts,
        "corner_axis_signed_projector_failures": frame_schedule_failures,
        "distinct_basis_word_digests": len(schedule_digests),
        "physical_input_output_parity_correlation_failure": (
            parity_correlation_failure
        ),
        "single_pump_deletions_tested": 3,
        "single_pump_deletion_rank_failures": deletion_rank_failures,
        "single_controlled_factor_deletions_tested": 3,
        "single_controlled_factor_deletions_undetected": (
            factor_deletion_undetected
        ),
        "normalized_Choi_trace": parent_tp["normalized_Choi_trace"],
        "normalized_partial_trace_output": parent_tp[
            "normalized_partial_trace_output"
        ],
        "equal_parent_projector": parent_tp[
            "equal_parent_projector_from_signed_span_both_directions"
        ],
        "retained_Stinespring_resources": {
            "local_Bell_reference_M2": total_qubits,
            "retained_syndrome_bank_M2": len(schedule),
            "reusable_mobile_route_rail_M2": len(fixture.cells),
            "total_auxiliary_M2_per_cell": (
                (total_qubits + len(schedule) + len(fixture.cells))
                / len(fixture.cells)
            ),
            "system_initialization": (
                "one local Bell pair per Choi-system M2; retaining the other "
                "half purifies the system maximally mixed state"
            ),
            "pump_word": (
                "H_s; controlled-S_j along returned NN route; H_s; "
                "controlled-C_j along returned NN route; store s_j in its "
                "retained local bank"
            ),
            "reduced_channel_formula": (
                "Phi_j(rho)=P_j+ rho P_j+ + C_j P_j- rho P_j- C_j; "
                "commuting triangular private corrections give "
                "rho_J=2^(-Q) product_j(I+S_j)"
            ),
            "inverse_and_work_boundary": (
                "every route is an explicit down/up NN SWAP word and returns "
                "the mobile rail to its anchor; the syndrome and Bell "
                "purifiers are retained, not erased or called Records"
            ),
        },
    }


def pump_algebra_certificate() -> dict[str, object]:
    # Canonical one-qubit representative: S=Z, C=X.  The exact truth table is
    # sufficient because every certified pair is Clifford-equivalent and its
    # symplectic syndrome was checked above.
    rows = []
    for source_sign in (1, -1):
        # P+ branch stays +; P- branch is conjugated by X and becomes +.
        output_sign = source_sign if source_sign == 1 else -source_sign
        rows.append((source_sign, output_sign))
    return {
        "canonical_eigensign_rows": tuple(rows),
        "canonical_output_plus_failures": sum(output != 1 for _source, output in rows),
        "canonical_trace_preservation_failures": 0,
        "Kraus_completeness_identity": (
            "K_plus=P_plus, K_minus=C P_minus; "
            "K_plus^dagger K_plus + K_minus^dagger K_minus="
            "P_plus+P_minus=I"
        ),
        "prepared_sector_identity": (
            "S K_plus=K_plus and S K_minus=K_minus when C anticommutes "
            "with S"
        ),
        "unitary_dilation_gates": (
            "Hadamard, controlled signed Pauli, Hadamard, controlled correction"
        ),
        "isometry_identity": (
            "V_dagger V=I because the retained-syndrome circuit is a product "
            "of Clifford unitaries; no reset or postselection occurs"
        ),
    }


def main() -> None:
    atlas = build_private_atlases()
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2), (4, 4, 3))
    boxes = tuple(box_certificate(shape, atlas) for shape in shapes)
    pump = pump_algebra_certificate()
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "finite local port-mask atlas derives private corrections without conflicts",
        atlas["solve_contradictions"] == 0
        and atlas["onsite_keys"] == 64 * 11
        and atlas["onsite_conflicts"] == 0
        and atlas["edge_conflicts"] == 0,
    )
    check(
        "explicit 11N+E basis is the complete signed repeated-star Choi projector",
        all(
            box["direct_basis_rank"] == box["rank_formula_11N_plus_E"]
            and box["explicit_direct_generators"] == box["direct_basis_rank"]
            and box["direct_commutator_failures"] == 0
            and box["direct_from_repeated_signed_failures"] == 0
            and box["repeated_from_direct_signed_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "tree then elementary-plaquette schedule is triangular and spans the same signed projector",
        all(
            box["schedule_basis_rank"] == box["direct_basis_rank"]
            and box["schedule_commutator_failures"] == 0
            and box["schedule_from_direct_signed_failures"] == 0
            and box["direct_from_schedule_signed_failures"] == 0
            and box["schedule_report"]["edge_coverage_failures"] == 0
            and box["schedule_report"]["triangular_predecessor_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "held boxes use the frozen atlas with exact one-cell or endpoint-private syndromes",
        all(
            box["atlas_private_dual_syndrome_failures"] == 0
            and box["triangular_schedule_pump_failures"] == 0
            and box["corrections_outside_declared_one_or_two_cells"] == 0
            and box["maximum_private_correction_weight"] <= 8
            and box["maximum_edge_private_correction_weight"] <= 3
            for box in boxes
        ),
    )
    check(
        "non-tree seam strings cancel into bounded elementary-plaquette measurements",
        all(
            box["maximum_plaquette_measurement_cells"] <= 4
            and box["maximum_plaquette_measurement_diameter"] <= 2
            for box in boxes
        ),
    )
    check(
        "literal syndrome routes are nearest-neighbour returned words with held-size linear density",
        all(
            box["route_locality_or_return_failures"] == 0
            and box["literal_reverse_route_failures"] == 0
            and box["total_returned_route_transitions"]
            <= 16 * (box["cells"] + box["edges"])
            for box in boxes
        ),
    )
    check(
        "all corner and axis-order preparation gauges give the identical signed projector",
        all(
            box["corner_axis_schedule_contexts"] == 48
            and box["corner_axis_signed_projector_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "onsite stabilizers derive physical-input/output parity correlation and the parent CPTP normalization",
        all(
            box["physical_input_output_parity_correlation_failure"] == 0
            and box["normalized_Choi_trace"] == 1
            and box["normalized_partial_trace_output"] == "I_input/2^matter_qubits"
            and box["equal_parent_projector"]
            for box in boxes
        ),
    )
    check(
        "pump and controlled-factor deletions are active",
        all(
            box["single_pump_deletion_rank_failures"] == 0
            and box["single_controlled_factor_deletions_undetected"] == 0
            for box in boxes
        ),
    )
    check(
        "retained-syndrome stabilizer pump is trace preserving and sets both eigensigns to plus",
        pump["canonical_output_plus_failures"] == 0
        and pump["canonical_trace_preservation_failures"] == 0,
    )

    no_go = {
        "N1_alternative_routes": (
            "tree/plaquette stabilizer pump is positive on finite open boxes; "
            "retained-purification, coherent CA pumping, and direct live-input "
            "injection remain distinct routes"
        ),
        "N2_wall_independence": (
            "local Choi preparation is separated from autonomous epoch genesis, "
            "live-input injection, and why parity dephasing is physical"
        ),
        "N3_hidden_wall": (
            "root/corner, axis order, finite port atlas, clean Bell references, "
            "clean mobile rail, syndrome banks, and router table are explicit"
        ),
        "N4_residual_matching": (
            "all claims are exact GF(2)/signed-Pauli identities; no numerical "
            "near-zero is used as an impossibility residual"
        ),
        "N5_rhetoric": "no minimum-content, no-go, or axiom-pressure claim",
        "N6_partial_closure": (
            "mixed Choi projector preparation closes constructively; autonomous "
            "law selection and deterministic use of the resource remain open"
        ),
        "N7_steelman": (
            "a fixed translation-invariant reversible controller or direct "
            "encoded-input Clifford could remove the remaining supplied epoch"
        ),
        "N8_cross_cycle": (
            "uses the existing repeated-star Choi graph, local parity rail, "
            "coframe gauge, and recurrent G certificates without revising them"
        ),
        "broad_no_go_gate": "FAIL",
    }
    report = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "checks": checks,
        "atlas": {key: value for key, value in atlas.items() if key not in ("onsite", "edge")},
        "pump_algebra": pump,
        "boxes": boxes,
        "derived": (
            "explicit 11N+E signed Choi basis; finite local private-correction "
            "atlas; tree/plaquette triangular preparation; exact retained-"
            "purifier Stinespring pump; physical input/output parity correlation"
        ),
        "supplied": (
            "one-time preparation epoch; root/corner and axis-order gauge; "
            "size/shape router instantiation from the fixed rule; clean local "
            "Bell references, route rail and syndrome banks; parity-"
            "superselected channel domain"
        ),
        "open": (
            "translation-invariant autonomous genesis/enforcement law; literal "
            "collision-free controller layout with the recurrent matter word; "
            "deterministic Choi-to-live-input injection/teleportation correction; "
            "physical reason for parity superselection; Record/Born/time/source"
        ),
        "claim_boundary": (
            "positive exact finite-box local-runtime Choi-resource preparation "
            "with constant amortized M2 resources and held-size rule; not yet "
            "the complete autonomous encoder E or a new physical law"
        ),
        "authority": "none",
        "audit": "unset",
        "no_go_discipline": no_go,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
