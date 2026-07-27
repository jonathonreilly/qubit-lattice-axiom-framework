#!/usr/bin/env python3
"""Cycle-720 coherent cell-edge gauge common-E support.

This probe replaces the shared scalar-reference seam carrier by one BKSF
gauge qubit per coarse-cell edge.  The local Gauss rows are

    D_c = P_c B_g(c),

and each cross-cell Majorana bilinear is dressed by the corresponding local
gauge A_e.  Gauge plaquette loops plus all but one Gauss row leave exactly the
full 6N matter dimension on an open connected box.  The omitted row is an
explicit root-charge diagnostic.

A second construction removes that root by adding one marker qubit to every
vertex, edge, face, and cube, locally equating all markers, and assigning every
Gauss row its incident Euler marker.  On a contractible open box the odd Euler
object count retains both matter-parity sectors with no runtime parity query.
The uniform marker sector and its genesis remain supplied, so this support
construction does not call the result an autonomous full-parity encoder.

The immediate question is whether the resulting physical Pauli family has an
exact common logical Clifford orientation to the ordinary coarse-CAR seam
family, and whether that orientation is bounded/local rather than a hidden
exterior-order transform.
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
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
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

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27 as R


Pauli = R.Pauli
Coord = tuple[int, int, int]
FAIL = 0


def check(label: str, condition: bool, detail=None) -> None:
    global FAIL
    print("PASS" if condition else "FAIL", label, "::", detail)
    FAIL += not condition


def product(rows) -> Pauli:
    result = Pauli()
    for row in rows:
        result = result @ row
    return result


def gf2_solve(rows: list[tuple[int, int]]) -> tuple[int, int, int]:
    """Return one free-zero solution, coefficient rank, contradictions."""
    pivots: dict[int, tuple[int, int]] = {}
    contradictions = 0
    for original_mask, original_rhs in rows:
        mask, rhs = original_mask, original_rhs
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                old_mask, old_rhs = pivots[pivot]
                mask ^= old_mask
                rhs ^= old_rhs
            else:
                pivots[pivot] = (mask, rhs)
                break
        else:
            contradictions += rhs
    solution = 0
    # Each stored pivot is the highest bit in its row.  With free variables
    # zero, lower pivots must therefore be assigned first.
    for pivot in sorted(pivots):
        mask, rhs = pivots[pivot]
        if ((mask & solution).bit_count() & 1) != rhs:
            solution ^= 1 << pivot
    return solution, len(pivots), contradictions


@dataclass
class CellEdgeGauge:
    shape: tuple[int, int, int]
    cells: tuple[Coord, ...]
    edges: tuple[tuple[int, int, Coord, int, int, int], ...]
    incident: tuple[tuple[int, ...], ...]
    matter_qubits: int
    qubits: int
    tree_edges: tuple[int, ...]
    gauge_loops: tuple[Pauli, ...]
    local_plaquettes: tuple[Pauli, ...]
    logical_z: tuple[Pauli, ...]
    gauss: tuple[Pauli, ...]
    w_rows: tuple[Pauli, ...]
    v_rows: tuple[Pauli, ...]

    @classmethod
    def build(cls, shape: tuple[int, int, int]) -> "CellEdgeGauge":
        cells = R.G.box_cells(shape)
        cell_index = {cell: index for index, cell in enumerate(cells)}
        edge_rows = []
        for cell in cells:
            for axis in range(3):
                target = R.target_cell(cell, axis)
                if target not in cell_index:
                    continue
                left_cell = cell_index[cell]
                right_cell = cell_index[target]
                left_mode = 6 * left_cell + 2 * axis + 1
                right_mode = 6 * right_cell + 2 * axis
                edge_rows.append(
                    (left_cell, right_cell, cell, axis, left_mode, right_mode)
                )
        edges = tuple(edge_rows)
        incident_rows: list[list[int]] = [[] for _cell in cells]
        for edge, (left, right, *_rest) in enumerate(edges):
            incident_rows[left].append(edge)
            incident_rows[right].append(edge)
        incident = tuple(tuple(sorted(row)) for row in incident_rows)
        matter_qubits = 6 * len(cells)
        qubits = matter_qubits + len(edges)

        def gauge_b(vertex: int) -> Pauli:
            return Pauli(
                z=sum(1 << (matter_qubits + edge) for edge in incident[vertex])
            )

        def gauge_a(source: int, target: int) -> Pauli:
            edge = next(
                edge
                for edge, (left, right, *_rest) in enumerate(edges)
                if {left, right} == {source, target}
            )
            z = 0
            for vertex in (source, target):
                for other in incident[vertex]:
                    if other == edge:
                        break
                    z ^= 1 << (matter_qubits + other)
            return Pauli(
                phase=0 if source < target else 2,
                x=1 << (matter_qubits + edge),
                z=z,
            )

        adjacency: list[list[tuple[int, int]]] = [[] for _cell in cells]
        for edge, (left, right, *_rest) in enumerate(edges):
            adjacency[left].append((right, edge))
            adjacency[right].append((left, edge))
        for row in adjacency:
            row.sort()
        parent: list[int | None] = [None] * len(cells)
        seen = {0}
        queue = deque([0])
        tree_edges = []
        while queue:
            source = queue.popleft()
            for target, edge in adjacency[source]:
                if target in seen:
                    continue
                seen.add(target)
                parent[target] = source
                tree_edges.append(edge)
                queue.append(target)
        if len(seen) != len(cells):
            raise ValueError("cell graph is disconnected")

        def tree_path(source: int, target: int) -> list[int]:
            source_chain = []
            vertex: int | None = source
            while vertex is not None:
                source_chain.append(vertex)
                vertex = parent[vertex]
            target_chain = []
            vertex = target
            while vertex is not None:
                target_chain.append(vertex)
                vertex = parent[vertex]
            positions = {vertex: index for index, vertex in enumerate(source_chain)}
            common = next(vertex for vertex in target_chain if vertex in positions)
            return (
                source_chain[: positions[common] + 1]
                + list(reversed(target_chain[: target_chain.index(common)]))
            )

        loops = []
        for edge, (left, right, *_rest) in enumerate(edges):
            if edge in tree_edges:
                continue
            vertices = tree_path(left, right)
            factors = [
                gauge_a(vertices[index], vertices[index + 1])
                for index in range(len(vertices) - 1)
            ] + [gauge_a(right, left)]
            loops.append(Pauli(phase=len(factors) % 4) @ product(factors))

        local_plaquettes = []
        cell_index = {cell: index for index, cell in enumerate(cells)}
        for cell in cells:
            for first, second in combinations(range(3), 2):
                first_step = list(cell)
                first_step[first] += 1
                first_step = tuple(first_step)
                second_step = list(cell)
                second_step[second] += 1
                second_step = tuple(second_step)
                corner = list(cell)
                corner[first] += 1
                corner[second] += 1
                corner = tuple(corner)
                if not all(
                    vertex in cell_index
                    for vertex in (first_step, second_step, corner)
                ):
                    continue
                vertices = (
                    cell_index[cell],
                    cell_index[first_step],
                    cell_index[corner],
                    cell_index[second_step],
                )
                factors = [
                    gauge_a(vertices[index], vertices[(index + 1) % 4])
                    for index in range(4)
                ]
                local_plaquettes.append(product(factors))

        logical_z = tuple(Pauli(z=1 << mode) for mode in range(matter_qubits))
        gauss = []
        # The last cell is an explicit root-charge port.  Omitting its Gauss
        # row retains both total matter-parity sectors without a runtime query.
        for cell in range(len(cells) - 1):
            matter_parity = Pauli(
                z=sum(1 << (6 * cell + mode) for mode in range(6))
            )
            gauss.append(matter_parity @ gauge_b(cell))
        w_rows = logical_z + tuple(loops) + tuple(gauss)
        if len(w_rows) != qubits:
            raise ValueError(("wrong W count", len(w_rows), qubits))
        if R.F.base.gf2_rank(row.symplectic(qubits) for row in w_rows) != qubits:
            raise ValueError("W rows are not independent")
        v_rows = tuple(R.F.complete_tableau(list(w_rows), [], qubits))
        if any(
            R.C709.anticommutes(w_row, v_row) != int(left == right)
            for left, w_row in enumerate(w_rows)
            for right, v_row in enumerate(v_rows)
        ):
            raise ValueError("canonical completion failed")
        result = cls(
            shape,
            cells,
            edges,
            incident,
            matter_qubits,
            qubits,
            tuple(tree_edges),
            tuple(loops),
            tuple(local_plaquettes),
            logical_z,
            tuple(gauss),
            w_rows,
            v_rows,
        )
        result.gauge_b = gauge_b  # type: ignore[attr-defined]
        result.gauge_a = gauge_a  # type: ignore[attr-defined]
        return result

    def decoded(self, row: Pauli) -> tuple[Pauli, int, int]:
        coordinates = R.F.decode(row, self.w_rows, self.v_rows, self.qubits)
        mask = (1 << self.matter_qubits) - 1
        return (
            Pauli(
                phase=coordinates.phase,
                x=coordinates.v_mask & mask,
                z=coordinates.w_mask & mask,
            ),
            coordinates.v_mask >> self.matter_qubits,
            coordinates.w_mask >> self.matter_qubits,
        )

    def expected_terms(self, edge: int) -> tuple[Pauli, ...]:
        _left, _right, cell, axis, _left_mode, _right_mode = self.edges[edge]
        shell = type("CellShell", (), {"cells": self.cells})()
        return R.expected_logical_terms(shell, cell, axis)

    def physical_terms(self, edge: int) -> tuple[Pauli, ...]:
        left, right, _cell, _axis, left_mode, right_mode = self.edges[edge]
        # One fixed six-mode Jordan-Wigner convention is allowed *inside* a
        # coarse cell.  The gauge A_e replaces every inter-cell string.  Both
        # endpoint factors must therefore use their own local Majorana prefix;
        # merely truncating the global between-mask would miss one prefix and
        # reproduce the shared-cell commutator defect.
        def gamma(cell: int, endpoint: int, odd: bool) -> Pauli:
            prefix = sum(
                1 << (6 * cell + mode)
                for mode in range(endpoint - 6 * cell)
            )
            return Pauli(
                phase=int(odd),
                x=1 << endpoint,
                z=prefix | ((1 << endpoint) if odd else 0),
            )

        gauge = self.gauge_a(left, right)  # type: ignore[attr-defined]
        return (
            Pauli(z=1 << left_mode),
            Pauli(z=1 << right_mode),
            Pauli(phase=2) @ gamma(left, left_mode, False)
                @ gamma(right, right_mode, True) @ gauge,
            gamma(left, left_mode, True)
                @ gamma(right, right_mode, False) @ gauge,
        )


@dataclass
class EulerMarkerGauge:
    """Root-free open-box full-parity extension by a covariant Euler marker."""

    base: CellEdgeGauge
    marker_objects: tuple[tuple[str, Coord, tuple[int, ...]], ...]
    marker_equalities: tuple[Pauli, ...]
    marker_equality_basis: tuple[Pauli, ...]
    gauss: tuple[Pauli, ...]
    w_rows: tuple[Pauli, ...]
    v_rows: tuple[Pauli, ...]

    @classmethod
    def build(cls, shape: tuple[int, int, int]) -> "EulerMarkerGauge":
        base = CellEdgeGauge.build(shape)
        cells = base.cells
        cell_set = set(cells)
        objects: list[tuple[str, Coord, tuple[int, ...]]] = []
        objects.extend(("vertex", cell, ()) for cell in cells)
        objects.extend(
            ("edge", cell, (axis,))
            for _left, _right, cell, axis, _lm, _rm in base.edges
        )
        for cell in cells:
            for first, second in combinations(range(3), 2):
                targets = []
                for delta in ((first,), (second,), (first, second)):
                    target = list(cell)
                    for axis in delta:
                        target[axis] += 1
                    targets.append(tuple(target))
                if all(target in cell_set for target in targets):
                    objects.append(("face", cell, (first, second)))
        for cell in cells:
            corner = tuple(value + 1 for value in cell)
            if all(
                tuple(cell[axis] + int(axis in subset) for axis in range(3)) in cell_set
                for subset in (
                    (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)
                )
            ):
                objects.append(("cube", cell, (0, 1, 2)))
        marker_objects = tuple(objects)
        marker_offset = base.qubits
        marker_index = {row: index for index, row in enumerate(marker_objects)}
        vertex_marker = {
            cell: marker_index[("vertex", cell, ())] for cell in cells
        }
        equality_rows = []
        equality_basis = []
        # Every higher-dimensional object is locally tied to its lower-corner
        # vertex marker.  Add all cell-neighbor equalities as the covariant
        # displayed family, but use only a tree subset in the independent W.
        for index, (_kind, owner, _axes) in enumerate(marker_objects):
            if index == vertex_marker[owner]:
                continue
            row = Pauli(
                z=(1 << (marker_offset + index))
                | (1 << (marker_offset + vertex_marker[owner]))
            )
            equality_rows.append(row)
            equality_basis.append(row)
        for edge, (left, right, _cell, _axis, _lm, _rm) in enumerate(base.edges):
            row = Pauli(
                z=(1 << (marker_offset + vertex_marker[cells[left]]))
                | (1 << (marker_offset + vertex_marker[cells[right]]))
            )
            equality_rows.append(row)
            if edge in base.tree_edges:
                equality_basis.append(row)

        owned: dict[Coord, list[int]] = {cell: [] for cell in cells}
        for index, (_kind, owner, _axes) in enumerate(marker_objects):
            owned[owner].append(index)
        gauss = []
        for cell_index, cell in enumerate(cells):
            matter = sum(1 << (6 * cell_index + mode) for mode in range(6))
            markers = sum(1 << (marker_offset + index) for index in owned[cell])
            gauss.append(Pauli(z=matter | markers) @ base.gauge_b(cell_index))  # type: ignore[attr-defined]
        w_rows = (
            base.logical_z
            + base.gauge_loops
            + tuple(gauss)
            + tuple(equality_basis)
        )
        qubits = base.qubits + len(marker_objects)
        if len(w_rows) != qubits:
            raise ValueError(("wrong Euler-marker W count", len(w_rows), qubits))
        if R.F.base.gf2_rank(row.symplectic(qubits) for row in w_rows) != qubits:
            raise ValueError("Euler-marker W rows are not independent")
        v_rows = tuple(R.F.complete_tableau(list(w_rows), [], qubits))
        return cls(
            base,
            marker_objects,
            tuple(equality_rows),
            tuple(equality_basis),
            tuple(gauss),
            tuple(w_rows),
            v_rows,
        )

    @property
    def shape(self):
        return self.base.shape

    @property
    def cells(self):
        return self.base.cells

    @property
    def edges(self):
        return self.base.edges

    @property
    def matter_qubits(self):
        return self.base.matter_qubits

    @property
    def qubits(self):
        return self.base.qubits + len(self.marker_objects)

    def physical_terms(self, edge: int):
        return self.base.physical_terms(edge)

    def expected_terms(self, edge: int):
        return self.base.expected_terms(edge)

    def decoded(self, row: Pauli):
        coordinates = R.F.decode(row, self.w_rows, self.v_rows, self.qubits)
        mask = (1 << self.matter_qubits) - 1
        return (
            Pauli(
                phase=coordinates.phase,
                x=coordinates.v_mask & mask,
                z=coordinates.w_mask & mask,
            ),
            coordinates.v_mask >> self.matter_qubits,
            coordinates.w_mask >> self.matter_qubits,
        )

    def gauge_a(self, source: int, target: int):
        return self.base.gauge_a(source, target)  # type: ignore[attr-defined]

    def gauge_b(self, vertex: int):
        return self.base.gauge_b(vertex)  # type: ignore[attr-defined]


def symmetric_index(left: int, right: int, size: int) -> int:
    if left > right:
        left, right = right, left
    return left * size - left * (left - 1) // 2 + right - left


def diagonal_common_e(fixture: CellEdgeGauge) -> dict[str, object]:
    """Solve a general logical diagonal Clifford, then audit its locality."""
    modes = fixture.matter_qubits
    variables = modes * (modes + 1) // 2
    rows: list[tuple[int, int]] = []
    decoded_rows = []
    leakage_failures = stabilizer_commutator_failures = 0
    operator_rows: list[tuple[str, Pauli, Pauli]] = []
    for edge in range(len(fixture.edges)):
        operator_rows.extend(
            ("seam", physical, target)
            for physical, target in zip(
                fixture.physical_terms(edge), fixture.expected_terms(edge)
            )
        )
    for mode in range(modes):
        row = Pauli(z=1 << mode)
        operator_rows.append(("onsite_B", row, row))
    for cell in range(len(fixture.cells)):
        for left_local, right_local in combinations(range(6), 2):
            left = 6 * cell + left_local
            right = 6 * cell + right_local
            endpoints = (1 << left) | (1 << right)
            between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
            for row in (
                Pauli(phase=2, x=endpoints, z=between | endpoints),
                Pauli(x=endpoints, z=between),
            ):
                operator_rows.append(("onsite_even", row, row))

    for family, physical, target in operator_rows:
        decoded, leakage, _stabilizer = fixture.decoded(physical)
        decoded_rows.append((family, decoded, target))
        leakage_failures += bool(leakage)
        stabilizer_commutator_failures += sum(
            R.C709.anticommutes(physical, row)
            for row in fixture.w_rows[modes:]
        )
        if decoded.x != target.x:
            return {
                "coordinate_system_inconsistent": True,
                "X_coordinate_failures": 1,
            }
        difference = decoded.z ^ target.z
        for output in range(modes):
            mask = 0
            bits = decoded.x
            while bits:
                bit = bits & -bits
                source = bit.bit_length() - 1
                mask ^= 1 << symmetric_index(source, output, modes)
                bits ^= bit
            rows.append((mask, (difference >> output) & 1))

    def restricted_coordinate_system(radius: int) -> dict[str, int]:
        allowed = []
        for left in range(modes):
            left_cell = fixture.cells[left // 6]
            for right in range(left, modes):
                right_cell = fixture.cells[right // 6]
                distance = sum(abs(a - b) for a, b in zip(left_cell, right_cell))
                if distance <= radius:
                    allowed.append((left, right))
        index = {pair: item for item, pair in enumerate(allowed)}
        restricted_rows = []
        for _family, decoded, target in decoded_rows:
            difference = decoded.z ^ target.z
            for output in range(modes):
                mask = 0
                bits = decoded.x
                while bits:
                    bit = bits & -bits
                    source = bit.bit_length() - 1
                    pair = tuple(sorted((source, output)))
                    if pair in index:
                        mask ^= 1 << index[pair]
                    bits ^= bit
                restricted_rows.append((mask, (difference >> output) & 1))
        _solution, restricted_rank, restricted_contradictions = gf2_solve(
            restricted_rows
        )
        return {
            "variables": len(allowed),
            "rank": restricted_rank,
            "contradictions": restricted_contradictions,
        }

    restricted = {
        f"cell_radius_{radius}": restricted_coordinate_system(radius)
        for radius in range(4)
    }
    solution, rank, contradictions = gf2_solve(rows)
    if contradictions:
        return {
            "coordinate_system_inconsistent": True,
            "X_coordinate_failures": 0,
            "symmetric_variables": variables,
            "coefficient_rank": rank,
            "augmented_contradictions": contradictions,
            "logical_leakage_failures": leakage_failures,
            "stabilizer_commutator_failures": stabilizer_commutator_failures,
            "restricted_coordinate_systems": restricted,
        }

    matrix_rows = [0] * modes
    active_pairs = []
    for left in range(modes):
        for right in range(left, modes):
            if (solution >> symmetric_index(left, right, modes)) & 1:
                matrix_rows[left] ^= 1 << right
                if left != right:
                    matrix_rows[right] ^= 1 << left
                active_pairs.append((left, right))

    # First use the Hermitian phase of each X image.  A remaining even phase
    # can be repaired by conjugation with one logical Z per selected mode.
    base_images = []
    for mode in range(modes):
        z = matrix_rows[mode]
        base_images.append(
            Pauli(phase=(z >> mode) & 1, x=1 << mode, z=z)
        )
    base_images.extend(Pauli(z=1 << mode) for mode in range(modes))
    phase_rows = []
    phase_parity_failures = 0
    for _family, decoded, target in decoded_rows:
        transformed = R.C709.apply_images(base_images, decoded, modes)
        if transformed.x != target.x or transformed.z != target.z:
            raise AssertionError("coordinate solve did not replay")
        difference = (target.phase - transformed.phase) % 4
        phase_parity_failures += difference & 1
        phase_rows.append((decoded.x, difference // 2))
    phase_solution, phase_rank, phase_contradictions = gf2_solve(phase_rows)
    phase_equation_replay_failures = sum(
        ((mask & phase_solution).bit_count() & 1) != rhs
        for mask, rhs in phase_rows
    )
    images = []
    for mode in range(modes):
        z = matrix_rows[mode]
        phase = ((z >> mode) & 1) + 2 * ((phase_solution >> mode) & 1)
        images.append(Pauli(phase=phase, x=1 << mode, z=z))
    images.extend(Pauli(z=1 << mode) for mode in range(modes))
    transformed_coordinate_failures = transformed_phase_failures = 0
    family_failures: dict[str, int] = {}
    for family, decoded, target in decoded_rows:
        transformed = R.C709.apply_images(images, decoded, modes)
        transformed_coordinate_failures += (
            transformed.x != target.x or transformed.z != target.z
        )
        transformed_phase_failures += transformed.phase != target.phase
        family_failures[family] = family_failures.get(family, 0) + int(
            transformed.x != target.x
            or transformed.z != target.z
            or transformed.phase != target.phase
        )
    transformed_failures = transformed_coordinate_failures + transformed_phase_failures

    def cell(mode: int) -> int:
        return mode // 6

    cross_cell_pairs = [pair for pair in active_pairs if cell(pair[0]) != cell(pair[1])]
    cell_distances = [
        sum(
            abs(fixture.cells[cell(left)][axis] - fixture.cells[cell(right)][axis])
            for axis in range(3)
        )
        for left, right in cross_cell_pairs
    ]
    return {
        "coordinate_system_inconsistent": False,
        "symmetric_variables": variables,
        "equations": len(rows),
        "coefficient_rank": rank,
        "augmented_contradictions": contradictions,
        "phase_rank": phase_rank,
        "phase_parity_failures": phase_parity_failures,
        "phase_contradictions": phase_contradictions,
        "phase_equation_replay_failures": phase_equation_replay_failures,
        "logical_leakage_failures": leakage_failures,
        "stabilizer_commutator_failures": stabilizer_commutator_failures,
        "restricted_coordinate_systems": restricted,
        "transformed_logical_term_failures": transformed_failures,
        "transformed_coordinate_failures": transformed_coordinate_failures,
        "transformed_phase_failures": transformed_phase_failures,
        "transformed_family_failures": family_failures,
        "onsite_even_generator_rows": sum(
            family == "onsite_even" for family, _decoded, _target in decoded_rows
        ),
        "active_diagonal_terms": len(active_pairs),
        "active_onsite_S_terms": sum(left == right for left, right in active_pairs),
        "active_cross_cell_CZ_terms": len(cross_cell_pairs),
        "maximum_cross_cell_CZ_distance": max(cell_distances, default=0),
        "active_Z_phase_repairs": phase_solution.bit_count(),
        "active_pairs": tuple(active_pairs),
    }


def span_product(target: Pauli, generators: tuple[Pauli, ...], qubits: int) -> bool:
    pivots: dict[int, tuple[int, int]] = {}
    for index, generator in enumerate(generators):
        mask = generator.symplectic(qubits)
        combination = 1 << index
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                old_mask, old_combination = pivots[pivot]
                mask ^= old_mask
                combination ^= old_combination
            else:
                pivots[pivot] = (mask, combination)
                break
    mask = target.symplectic(qubits)
    combination = 0
    while mask:
        pivot = mask.bit_length() - 1
        if pivot not in pivots:
            return False
        old_mask, old_combination = pivots[pivot]
        mask ^= old_mask
        combination ^= old_combination
    reconstructed = product(
        generator
        for index, generator in enumerate(generators)
        if (combination >> index) & 1
    )
    return reconstructed == target


def support(row: Pauli) -> frozenset[int]:
    mask = row.x | row.z
    return frozenset(index for index in range(mask.bit_length()) if (mask >> index) & 1)


def constraint_and_update_certificate(fixture: CellEdgeGauge) -> dict[str, object]:
    cycle_rank = len(fixture.edges) - len(fixture.cells) + 1
    local_rank = R.F.base.gf2_rank(
        row.symplectic(fixture.qubits) for row in fixture.local_plaquettes
    )
    path_failures = sum(
        not span_product(row, fixture.local_plaquettes, fixture.qubits)
        for row in fixture.gauge_loops
    )
    stabilizers = fixture.w_rows[fixture.matter_qubits :]
    term_commutator_failures = 0
    maximum_term_weight = maximum_seam_union = 0
    deleted_gauge_syndromes = []
    colour_rows = []
    shared_edge_usage = [0] * len(fixture.edges)
    for edge, (_left, _right, cell, axis, _lm, _rm) in enumerate(fixture.edges):
        terms = fixture.physical_terms(edge)
        shared_edge_usage[edge] += 1
        term_commutator_failures += sum(
            R.C709.anticommutes(term, row)
            for term in terms
            for row in stabilizers
        )
        maximum_term_weight = max(
            maximum_term_weight, *(len(support(term)) for term in terms)
        )
        union = frozenset().union(*(support(term) for term in terms))
        maximum_seam_union = max(maximum_seam_union, len(union))
        # Remove the one edge-gauge A factor from an active hopping word.
        gauge = fixture.gauge_a(  # type: ignore[attr-defined]
            fixture.edges[edge][0], fixture.edges[edge][1]
        )
        bare = terms[2] @ gauge
        deleted_gauge_syndromes.append(
            sum(R.C709.anticommutes(bare, row) for row in fixture.gauss)
        )
        colour = (axis,) + tuple(value & 1 for value in cell)
        colour_rows.append((colour, union))
    same_colour_collisions = sum(
        left_colour == right_colour and bool(left_support & right_support)
        for (left_colour, left_support), (right_colour, right_support)
        in combinations(colour_rows, 2)
    )
    independent_loop_rank = R.F.base.gf2_rank(
        row.symplectic(fixture.qubits) for row in fixture.gauge_loops
    )
    delete_loop_ranks = tuple(
        R.F.base.gf2_rank(
            row.symplectic(fixture.qubits)
            for index, row in enumerate(fixture.gauge_loops)
            if index != deleted
        )
        for deleted in range(len(fixture.gauge_loops))
    )
    logical_x_weights = tuple(
        len(support(row)) for row in fixture.v_rows[: fixture.matter_qubits]
    )
    return {
        "shape": fixture.shape,
        "cells": len(fixture.cells),
        "matter_qubits": fixture.matter_qubits,
        "edge_gauge_qubits": len(fixture.edges),
        "constant_qubit_overhead_per_cell_upper_bound": 6 + 3,
        "displayed_local_plaquettes": len(fixture.local_plaquettes),
        "local_plaquette_rank": local_rank,
        "cycle_space_rank": cycle_rank,
        "maximum_local_plaquette_weight": max(
            (len(support(row)) for row in fixture.local_plaquettes), default=0
        ),
        "fundamental_path_loops_outside_local_plaquette_span": path_failures,
        "displayed_Gauss_rows": len(fixture.gauss),
        "omitted_root_Gauss_rows": 1,
        "root_cell": fixture.cells[-1],
        "full_tableau_rank": R.F.base.gf2_rank(
            row.symplectic(fixture.qubits) for row in fixture.w_rows
        ),
        "code_exponent": fixture.matter_qubits,
        "term_stabilizer_commutator_failures": term_commutator_failures,
        "maximum_physical_term_weight": maximum_term_weight,
        "maximum_seam_support_union": maximum_seam_union,
        "fixed_schedule_phases": 24,
        "same_phase_support_collisions": same_colour_collisions,
        "shared_edge_register_use_minimum": min(shared_edge_usage, default=0),
        "shared_edge_register_use_maximum": max(shared_edge_usage, default=0),
        "delete_gauge_A_Gauss_syndrome_minimum": min(
            deleted_gauge_syndromes, default=0
        ),
        "delete_gauge_A_Gauss_syndrome_maximum": max(
            deleted_gauge_syndromes, default=0
        ),
        "independent_loop_rank": independent_loop_rank,
        "delete_one_independent_loop_rank_maximum": max(delete_loop_ranks, default=0),
        "maximum_raw_tableau_logical_X_weight": max(logical_x_weights, default=0),
        "minimum_raw_tableau_logical_X_weight": min(logical_x_weights, default=0),
        "local_refresh_statement": (
            "each matter endpoint flip is paired with the same edge A_e; "
            "the two endpoint Gauss syndromes cancel algebraically"
        ),
    }


def euler_marker_certificate(fixture: EulerMarkerGauge) -> dict[str, object]:
    base = fixture.base
    counts = {
        kind: sum(row[0] == kind for row in fixture.marker_objects)
        for kind in ("vertex", "edge", "face", "cube")
    }
    euler_characteristic = (
        counts["vertex"] - counts["edge"] + counts["face"] - counts["cube"]
    )
    stabilizers = fixture.w_rows[fixture.matter_qubits :]
    term_commutator_failures = 0
    deleted_gauge_syndromes = []
    for edge, (left, right, _cell, _axis, _lm, _rm) in enumerate(fixture.edges):
        terms = fixture.physical_terms(edge)
        term_commutator_failures += sum(
            R.C709.anticommutes(term, row)
            for term in terms
            for row in stabilizers
        )
        bare = terms[2] @ fixture.gauge_a(left, right)
        deleted_gauge_syndromes.append(
            sum(R.C709.anticommutes(bare, row) for row in fixture.gauss)
        )
    equality_rank = R.F.base.gf2_rank(
        row.symplectic(fixture.qubits) for row in fixture.marker_equalities
    )
    basis_rank = R.F.base.gf2_rank(
        row.symplectic(fixture.qubits) for row in fixture.marker_equality_basis
    )
    delete_equality_ranks = tuple(
        R.F.base.gf2_rank(
            row.symplectic(fixture.qubits)
            for index, row in enumerate(fixture.marker_equality_basis)
            if index != deleted
        )
        for deleted in range(len(fixture.marker_equality_basis))
    )
    return {
        "shape": fixture.shape,
        "cells": len(fixture.cells),
        "matter_qubits": fixture.matter_qubits,
        "edge_gauge_qubits": len(fixture.edges),
        "Euler_marker_qubits": len(fixture.marker_objects),
        "marker_cell_counts": counts,
        "Euler_characteristic": euler_characteristic,
        "marker_count_parity": len(fixture.marker_objects) & 1,
        "displayed_local_marker_equalities": len(fixture.marker_equalities),
        "marker_equality_rank": equality_rank,
        "independent_marker_equality_rank": basis_rank,
        "maximum_marker_equality_weight": max(
            (len(support(row)) for row in fixture.marker_equalities), default=0
        ),
        "displayed_Gauss_rows": len(fixture.gauss),
        "omitted_root_Gauss_rows": 0,
        "maximum_Euler_Gauss_weight": max(
            (len(support(row)) for row in fixture.gauss), default=0
        ),
        "full_tableau_rank": R.F.base.gf2_rank(
            row.symplectic(fixture.qubits) for row in fixture.w_rows
        ),
        "physical_qubits": fixture.qubits,
        "code_exponent": fixture.qubits - len(stabilizers),
        "term_stabilizer_commutator_failures": term_commutator_failures,
        "delete_gauge_A_Gauss_syndrome_minimum": min(
            deleted_gauge_syndromes, default=0
        ),
        "delete_gauge_A_Gauss_syndrome_maximum": max(
            deleted_gauge_syndromes, default=0
        ),
        "delete_one_marker_equality_rank_maximum": max(
            delete_equality_ranks, default=0
        ),
        "runtime_global_parity_query_used": False,
        "global_marker_sector_preparation_supplied": True,
        "full_parity_relation": (
            "product_c D_c = P_matter times product_all_markers(Z); "
            "local equality makes product_all_markers(Z)=Z_sector because chi(box)=1"
        ),
    }


def frame_tuple(frame) -> tuple[Coord, Coord, Coord]:
    return tuple(tuple(int(value) for value in row) for row in frame)  # type: ignore[return-value]


def matvec(frame: tuple[Coord, Coord, Coord], vector: Coord) -> Coord:
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matmul(left, right):
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )


def schedule_covariance_certificate() -> dict[str, object]:
    frames = tuple(
        frame_tuple(frame) for frame in R.C703.prior.proper_cubic_frames()
    )
    frame_index = {frame: index for index, frame in enumerate(frames)}
    colours = tuple(
        (axis, px, py, pz)
        for axis in range(3)
        for px in range(2)
        for py in range(2)
        for pz in range(2)
    )

    def colour_map(frame):
        output = {}
        for axis, px, py, pz in colours:
            source = (px, py, pz)
            step = tuple(int(index == axis) for index in range(3))
            left = matvec(frame, source)
            right = matvec(frame, tuple(source[i] + step[i] for i in range(3)))
            target_axis = next(i for i in range(3) if left[i] != right[i])
            lower = tuple(min(left[i], right[i]) for i in range(3))
            output[(axis, px, py, pz)] = (target_axis,) + tuple(
                value & 1 for value in lower
            )
        return output

    maps = tuple(colour_map(frame) for frame in frames)
    bijection_failures = sum(len(set(row.values())) != len(colours) for row in maps)
    product_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            target = frame_index[matmul(left, right)]
            product_failures += any(
                maps[left_index][maps[right_index][colour]] != maps[target][colour]
                for colour in colours
            )
    translation_failures = 0
    for shift in ((x, y, z) for x in range(2) for y in range(2) for z in range(2)):
        mapped = {
            colour: (colour[0],) + tuple(colour[i + 1] ^ shift[i] for i in range(3))
            for colour in colours
        }
        translation_failures += len(set(mapped.values())) != len(colours)
    return {
        "proper_cubic_frames": len(frames),
        "frame_colour_bijection_failures": bijection_failures,
        "ordered_frame_products": len(frames) ** 2,
        "frame_colour_product_failures": product_failures,
        "translation_parity_residues": 8,
        "translation_colour_failures": translation_failures,
        "constraint_family_covariance": (
            "cell incidence, Gauss stars, and elementary square plaquettes are transported geometrically"
        ),
        "transformed_common_E_executed": False,
        "Euler_marker_object_family_transported": True,
        "uniform_marker_sector_genesis_supplied": True,
    }


def main() -> None:
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2))
    fixtures = tuple(CellEdgeGauge.build(shape) for shape in shapes)
    constraints = tuple(constraint_and_update_certificate(row) for row in fixtures)
    root_common_e = tuple(diagonal_common_e(row) for row in fixtures)
    euler_fixtures = tuple(EulerMarkerGauge.build(shape) for shape in shapes)
    euler_constraints = tuple(euler_marker_certificate(row) for row in euler_fixtures)
    common_e = tuple(diagonal_common_e(row) for row in euler_fixtures)
    covariance = schedule_covariance_certificate()
    mass_contact = R.C703.mass_and_contact_certificate()

    check(
        "local plaquettes span every tree-path loop and the sparse code has exact 6N capacity",
        all(
            row["local_plaquette_rank"] == row["cycle_space_rank"]
            and row["fundamental_path_loops_outside_local_plaquette_span"] == 0
            and row["full_tableau_rank"] == row["matter_qubits"] + row["edge_gauge_qubits"]
            and row["code_exponent"] == row["matter_qubits"]
            and row["maximum_local_plaquette_weight"] <= 9
            for row in constraints
        ),
        constraints,
    )
    check(
        "one edge-gauge-dressed seam grammar preserves every constraint and has a collision-free fixed 24-phase schedule",
        all(
            row["term_stabilizer_commutator_failures"] == 0
            and row["same_phase_support_collisions"] == 0
            and row["shared_edge_register_use_minimum"] == 1
            and row["shared_edge_register_use_maximum"] == 1
            and row["delete_gauge_A_Gauss_syndrome_minimum"] > 0
            and row["delete_one_independent_loop_rank_maximum"]
                == row["independent_loop_rank"] - 1
            for row in constraints
        ),
        constraints,
    )
    check(
        "the Euler marker removes the preferred root and retains both parity sectors using only local displayed constraints",
        all(
            row["Euler_characteristic"] == 1
            and row["marker_count_parity"] == 1
            and row["marker_equality_rank"] == row["Euler_marker_qubits"] - 1
            and row["independent_marker_equality_rank"] == row["Euler_marker_qubits"] - 1
            and row["omitted_root_Gauss_rows"] == 0
            and row["full_tableau_rank"] == row["physical_qubits"]
            and row["code_exponent"] == row["matter_qubits"]
            and row["term_stabilizer_commutator_failures"] == 0
            and row["delete_gauge_A_Gauss_syndrome_minimum"] == 2
            and row["delete_one_marker_equality_rank_maximum"]
                == row["independent_marker_equality_rank"] - 1
            and not row["runtime_global_parity_query_used"]
            for row in euler_constraints
        ),
        euler_constraints,
    )
    check(
        "the explicit stabilizer-tableau E orientation intertwines seam and the complete onsite even-CAR generator family",
        all(
            not row["coordinate_system_inconsistent"]
            and row["augmented_contradictions"] == 0
            and row["phase_contradictions"] == 0
            and row["phase_equation_replay_failures"] == 0
            and row["logical_leakage_failures"] == 0
            and row["stabilizer_commutator_failures"] == 0
            and row["transformed_logical_term_failures"] == 0
            and not any(row["transformed_family_failures"].values())
            for row in common_e
        ),
        tuple({key: value for key, value in row.items() if key != "active_pairs"} for row in common_e),
    )
    check(
        "the current common E remains honestly nonlocal and the uniform parity-marker sector is supplied",
        all(
            row["restricted_coordinate_systems"]["cell_radius_2"]["contradictions"] > 0
            and row["maximum_cross_cell_CZ_distance"] > 2
            for row in common_e
        )
        and all(row["global_marker_sector_preparation_supplied"] for row in euler_constraints),
        {
            "restricted": tuple(row["restricted_coordinate_systems"] for row in common_e),
            "Euler_markers": tuple(row["Euler_marker_qubits"] for row in euler_constraints),
        },
    )
    check(
        "the fixed schedule is a proper-cubic and translation colour action",
        covariance["proper_cubic_frames"] == 24
        and covariance["frame_colour_bijection_failures"] == 0
        and covariance["ordered_frame_products"] == 576
        and covariance["frame_colour_product_failures"] == 0
        and covariance["translation_colour_failures"] == 0,
        covariance,
    )
    check(
        "the one-particle mass and local contact fixtures are unchanged",
        mass_contact["one_particle_coin_eigen_residual"] < R.TOL
        and mass_contact["one_particle_mass_residual"] < R.TOL
        and mass_contact["contact_vacuum_and_one_particle_residual"] < R.TOL
        and mass_contact["contact_double_occupation_phase_residual"] < R.TOL,
        mass_contact,
    )

    report = {
        "status": "cycle720-positive-coherent-edge-gauge-common-E-nonlocal-marker-genesis-open",
        "pass": FAIL == 0,
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "constraints_and_update": constraints,
        "Euler_full_parity_extension": euler_constraints,
        "root_diagnostic_common_E": tuple(
            {key: value for key, value in row.items() if key != "active_pairs"}
            for row in root_common_e
        ),
        "common_E": tuple(
            {key: value for key, value in row.items() if key != "active_pairs"}
            for row in common_e
        ),
        "schedule_covariance": covariance,
        "mass_contact": mass_contact,
        "derived": (
            "one edge gauge qubit per coarse bond and bounded local Gauss/plaquette constraints",
            "elementary plaquettes span every supplied spanning-tree path loop on all three boxes",
            "a root-free Euler marker built from local vertex/edge/face/cube registers carries both matter-parity sectors on every contractible box without a runtime parity query",
            "one local gauge A_e dresses each inter-cell Majorana bilinear and preserves every constraint",
            "an explicit full-rank stabilizer tableau plus solved logical Clifford orientation intertwines every seam and every onsite even-CAR generator",
            "contact is diagonal and the one-particle mass fixture is unchanged",
            "a fixed 24-phase edge schedule has disjoint physical Pauli support and an exact 24/576/translation colour action",
        ),
        "supplied": (
            "one uniform Euler-marker superselection sector and its nonlocal genesis",
            "one stabilizer vacuum seed and its local plaquette/Gauss/equality sector",
            "one within-cell six-mode Majorana order",
            "the solved finite-box logical Clifford orientation of E",
            "the 24 program phases; these are a schedule, not physical time",
            "Cycle219 coin and Cycle230 contact parameters",
        ),
        "open": (
            "derive bounded autonomous preparation of the uniform Euler-marker sector rather than supplying its GHZ-like genesis",
            "replace the long-range logical Clifford/state orientation by a bounded-radius common E or prove a locally generated stabilizer-orbit description",
            "execute transformed common-E covariance rather than only constraint/schedule covariance",
            "place and route the new matter-plus-edge-gauge code on literal M2 repetition sites",
            "compose the literal non-Clifford coin/contact rotations with the routed seam word",
            "autonomous vacuum/genesis, syndrome repair, periodic Wilson sectors, and fault tolerance",
        ),
        "claim_ceiling": (
            "Positive coherent edge-gauge algebra and finite-box state-isometry result: a single root-free Euler-marker E orientation closes seam plus the full onsite even-CAR generator family with zero tableau leakage on 2x2x2 and two held boxes. "
            "It does not close the requested local physical compiler because that E contains growing-distance logical CZ structure, the uniform marker-sector genesis is supplied, transformed-E covariance is unexecuted, and the new code is not yet literally placed/routed on physical M2."
        ),
        "no_go_discipline": {
            "gate": "FAIL_for_broad_no_go__constructive_partial_only",
            "N1_alternatives": (
                "scalar-reference direct seam: physically routed but shared-cell commutator defect",
                "matter-only diagonal rephase: inconsistent",
                "coherent cell-edge gauge root diagnostic: positive exact finite-box even-algebra E",
                "Euler-marker full-parity extension: positive root-free local constraints, uniform-sector genesis open",
                "stabilizer orbit from a fixed vacuum seed: path independence modulo local plaquettes established, bounded preparation open",
                "endpoint-incidence qutrit and fully symmetric quotient remain live",
            ),
            "N2_wall_independence": (
                "finite algebraic E existence is separated from bounded-radius E",
                "full-parity capacity is separated from uniform marker-sector genesis",
                "abstract sparse code is separated from literal M2 placement/routing",
                "operator-family covariance is separated from transformed-E covariance",
            ),
            "N3_hidden_imports": (
                "uniform Euler-marker sector", "stabilizer vacuum", "within-cell order", "finite-box logical Clifford", "program phases"
            ),
            "N4_residual_matching": (
                "zero binary tableau mismatches and leakage for the claimed even generator family",
                "positive restricted-radius contradictions are charged against local E rather than algebraic E",
                "mass/contact numbers are not credited as physical routing",
            ),
            "N5_resolution": "2x2x2 plus held 3x2x2 and 3x3x2; no arbitrary-size or periodic transformed-E claim",
            "N6_partial_closure": "local constraints, local update, common finite E, held size, deletion controls, and schedule covariance close separately",
            "N7_steelman": "a locally generated plaquette-orbit E or covariant dynamical charge marker could remove the long-range E orientation and uniform-marker genesis supplies",
            "N8_cross_cycle_echo": "Cycle703 local-D algebra, Cycle706 graph equivalence, Cycle709 seam routing, and Cycle658 endpoint incidence remain consistent but do not by themselves close this new E",
        },
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str, separators=(",", ":")).encode()
    ).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    if FAIL:
        raise SystemExit(1)
    print("COHERENT_EDGE_GAUGE_EULER_COMMON_E_FINITE_POSITIVE_LOCALITY_GENESIS_OPEN")


if __name__ == "__main__":
    main()
