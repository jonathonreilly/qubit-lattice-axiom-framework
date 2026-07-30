#!/usr/bin/env python3
"""Self-contained finite reference and companion fixtures for Cycle 727."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations

from frontier_cycle727_finite_pauli_tableau_2026_07_28 import (
    Coord,
    Pauli,
    anticommutes,
    box_cells,
    complete_tableau,
    decode,
    expected_logical_terms,
    gf2_rank,
    gf2_solve,
    pauli_product,
    target_cell,
)


def product(rows) -> Pauli:
    return pauli_product(rows)


def symmetric_index(left: int, right: int, size: int) -> int:
    if left > right:
        left, right = right, left
    return left * size - left * (left - 1) // 2 + right - left


def kernel_relations(vectors: tuple[int, ...]) -> tuple[int, ...]:
    pivots: dict[int, tuple[int, int]] = {}
    output = []
    for index, original in enumerate(vectors):
        vector = original
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (vector, combination)
                break
            old_vector, old_combination = pivots[pivot]
            vector ^= old_vector
            combination ^= old_combination
        else:
            output.append(combination)
    return tuple(output)


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
        cells = box_cells(shape)
        cell_index = {cell: index for index, cell in enumerate(cells)}
        edge_rows = []
        for cell in cells:
            for axis in range(3):
                target = target_cell(cell, axis)
                if target not in cell_index:
                    continue
                left = cell_index[cell]
                right = cell_index[target]
                edge_rows.append((
                    left,
                    right,
                    cell,
                    axis,
                    6 * left + 2 * axis + 1,
                    6 * right + 2 * axis,
                ))
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
                z=sum(
                    1 << (matter_qubits + edge)
                    for edge in incident[vertex]
                )
            )

        def gauge_a(source: int, target: int) -> Pauli:
            edge = next(
                index
                for index, (left, right, *_rest) in enumerate(edges)
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

        adjacency: list[list[tuple[int, int]]] = [
            [] for _cell in cells
        ]
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
            positions = {
                vertex: index for index, vertex in enumerate(source_chain)
            }
            common = next(
                vertex for vertex in target_chain if vertex in positions
            )
            return (
                source_chain[: positions[common] + 1]
                + list(
                    reversed(
                        target_chain[: target_chain.index(common)]
                    )
                )
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
            loops.append(
                Pauli(phase=len(factors) % 4) @ product(factors)
            )

        local_plaquettes = []
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
                local_plaquettes.append(product(
                    gauge_a(
                        vertices[index],
                        vertices[(index + 1) % 4],
                    )
                    for index in range(4)
                ))

        logical_z = tuple(
            Pauli(z=1 << mode) for mode in range(matter_qubits)
        )
        gauss = []
        for cell in range(len(cells) - 1):
            matter_parity = Pauli(
                z=sum(
                    1 << (6 * cell + mode) for mode in range(6)
                )
            )
            gauss.append(matter_parity @ gauge_b(cell))
        w_rows = logical_z + tuple(loops) + tuple(gauss)
        if len(w_rows) != qubits:
            raise ValueError(("wrong W count", len(w_rows), qubits))
        if gf2_rank(
            row.symplectic(qubits) for row in w_rows
        ) != qubits:
            raise ValueError("W rows are not independent")
        v_rows = complete_tableau(w_rows, (), qubits)
        if any(
            anticommutes(w_row, v_row) != int(left == right)
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
        coordinates = decode(
            row, self.w_rows, self.v_rows, self.qubits
        )
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
        _left, _right, owner, axis, _lm, _rm = self.edges[edge]
        return expected_logical_terms(self.cells, owner, axis)

    def physical_terms(self, edge: int) -> tuple[Pauli, ...]:
        left, right, _owner, _axis, left_mode, right_mode = (
            self.edges[edge]
        )

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
            Pauli(phase=2)
            @ gamma(left, left_mode, False)
            @ gamma(right, right_mode, True)
            @ gauge,
            gamma(left, left_mode, True)
            @ gamma(right, right_mode, False)
            @ gauge,
        )


@dataclass
class EulerMarkerGauge:
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
            if all(
                tuple(
                    cell[axis] + int(axis in subset)
                    for axis in range(3)
                ) in cell_set
                for subset in (
                    (0,),
                    (1,),
                    (2,),
                    (0, 1),
                    (0, 2),
                    (1, 2),
                    (0, 1, 2),
                )
            ):
                objects.append(("cube", cell, (0, 1, 2)))
        marker_objects = tuple(objects)
        marker_offset = base.qubits
        marker_index = {
            row: index for index, row in enumerate(marker_objects)
        }
        vertex_marker = {
            cell: marker_index[("vertex", cell, ())] for cell in cells
        }
        equality_rows = []
        equality_basis = []
        for index, (_kind, owner, _axes) in enumerate(marker_objects):
            if index == vertex_marker[owner]:
                continue
            row = Pauli(
                z=(1 << (marker_offset + index))
                | (
                    1
                    << (
                        marker_offset + vertex_marker[owner]
                    )
                )
            )
            equality_rows.append(row)
            equality_basis.append(row)
        for edge, (
            left,
            right,
            _owner,
            _axis,
            _lm,
            _rm,
        ) in enumerate(base.edges):
            row = Pauli(
                z=(
                    1
                    << (
                        marker_offset
                        + vertex_marker[cells[left]]
                    )
                )
                | (
                    1
                    << (
                        marker_offset
                        + vertex_marker[cells[right]]
                    )
                )
            )
            equality_rows.append(row)
            if edge in base.tree_edges:
                equality_basis.append(row)
        owned: dict[Coord, list[int]] = {
            cell: [] for cell in cells
        }
        for index, (_kind, owner, _axes) in enumerate(marker_objects):
            owned[owner].append(index)
        gauss = []
        for cell_index, cell in enumerate(cells):
            matter = sum(
                1 << (6 * cell_index + mode) for mode in range(6)
            )
            markers = sum(
                1 << (marker_offset + index)
                for index in owned[cell]
            )
            gauss.append(
                Pauli(z=matter | markers)
                @ base.gauge_b(cell_index)  # type: ignore[attr-defined]
            )
        w_rows = (
            base.logical_z
            + base.gauge_loops
            + tuple(gauss)
            + tuple(equality_basis)
        )
        qubits = base.qubits + len(marker_objects)
        if len(w_rows) != qubits:
            raise ValueError(
                ("wrong Euler-marker W count", len(w_rows), qubits)
            )
        if gf2_rank(
            row.symplectic(qubits) for row in w_rows
        ) != qubits:
            raise ValueError("Euler-marker W rows are not independent")
        return cls(
            base,
            marker_objects,
            tuple(equality_rows),
            tuple(equality_basis),
            tuple(gauss),
            tuple(w_rows),
            complete_tableau(w_rows, (), qubits),
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
        coordinates = decode(
            row, self.w_rows, self.v_rows, self.qubits
        )
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
        return self.base.gauge_a(  # type: ignore[attr-defined]
            source, target
        )

    def gauge_b(self, vertex: int):
        return self.base.gauge_b(vertex)  # type: ignore[attr-defined]


@dataclass(frozen=True)
class CompanionFixture:
    shape: tuple[int, int, int]
    cells: tuple[Coord, ...]
    edges: tuple[tuple[int, int, Coord, int, int, int], ...]
    matter_qubits: int
    qubits: int

    @classmethod
    def build(cls, shape: tuple[int, int, int]) -> "CompanionFixture":
        base = CellEdgeGauge.build(shape)
        return cls(
            shape,
            base.cells,
            base.edges,
            base.matter_qubits,
            base.matter_qubits + 3 * len(base.cells),
        )

    def matter_gamma(
        self, cell: int, mode: int, odd: bool
    ) -> Pauli:
        endpoint = 6 * cell + mode
        prefix = sum(
            1 << (6 * cell + item) for item in range(mode)
        )
        return Pauli(
            phase=int(odd),
            x=1 << endpoint,
            z=prefix | ((1 << endpoint) if odd else 0),
        )

    def companion_eta(self, cell: int, direction: int) -> Pauli:
        local = direction // 2
        odd = direction & 1
        endpoint = self.matter_qubits + 3 * cell + local
        prefix = sum(
            1 << (self.matter_qubits + 3 * cell + item)
            for item in range(local)
        )
        return Pauli(
            phase=odd,
            x=1 << endpoint,
            z=prefix | ((1 << endpoint) if odd else 0),
        )

    def endpoint(
        self, cell: int, direction: int, odd: bool
    ) -> Pauli:
        return self.matter_gamma(
            cell, direction, odd
        ) @ self.companion_eta(cell, direction)

    def physical_terms(self, edge: int) -> tuple[Pauli, ...]:
        left, right, _owner, _axis, left_mode, right_mode = (
            self.edges[edge]
        )
        return (
            Pauli(z=1 << left_mode),
            Pauli(z=1 << right_mode),
            Pauli(phase=2)
            @ self.endpoint(left, left_mode % 6, False)
            @ self.endpoint(right, right_mode % 6, True),
            self.endpoint(left, left_mode % 6, True)
            @ self.endpoint(right, right_mode % 6, False),
        )

    def target_terms(self, edge: int) -> tuple[Pauli, ...]:
        _left, _right, owner, axis, _lm, _rm = self.edges[edge]
        return expected_logical_terms(self.cells, owner, axis)


def operator_rows(fixture: CompanionFixture):
    rows = []
    for edge in range(len(fixture.edges)):
        rows.extend(
            ("seam", physical, target)
            for physical, target in zip(
                fixture.physical_terms(edge),
                fixture.target_terms(edge),
            )
        )
    for mode in range(fixture.matter_qubits):
        row = Pauli(z=1 << mode)
        rows.append(("onsite_B", row, row))
    for cell in range(len(fixture.cells)):
        for left_local, right_local in combinations(range(6), 2):
            left = 6 * cell + left_local
            right = 6 * cell + right_local
            endpoints = (1 << left) | (1 << right)
            between = (
                (1 << right) - 1
            ) ^ ((1 << (left + 1)) - 1)
            rows.extend((
                (
                    "onsite_even",
                    Pauli(
                        phase=2,
                        x=endpoints,
                        z=between | endpoints,
                    ),
                    Pauli(
                        phase=2,
                        x=endpoints,
                        z=between | endpoints,
                    ),
                ),
                (
                    "onsite_even",
                    Pauli(x=endpoints, z=between),
                    Pauli(x=endpoints, z=between),
                ),
            ))
    return tuple(rows)


def relation_certificate(
    fixture: CompanionFixture,
) -> dict[str, object]:
    rows = operator_rows(fixture)
    physical = tuple(row[1] for row in rows)
    target = tuple(row[2] for row in rows)
    physical_vectors = tuple(
        row.symplectic(fixture.qubits) for row in physical
    )
    target_vectors = tuple(
        row.symplectic(fixture.matter_qubits) for row in target
    )
    gram_failures = sum(
        anticommutes(physical[left], physical[right])
        != anticommutes(target[left], target[right])
        for left in range(len(rows))
        for right in range(left)
    )
    target_kernel = kernel_relations(target_vectors)
    relation_rows = []
    target_relation_phase_failures = 0
    for combination in target_kernel:
        selected_physical = tuple(
            row
            for index, row in enumerate(physical)
            if (combination >> index) & 1
        )
        selected_target = tuple(
            row
            for index, row in enumerate(target)
            if (combination >> index) & 1
        )
        physical_product = product(selected_physical)
        target_product = product(selected_target)
        if target_product.x or target_product.z:
            raise AssertionError("target kernel replay failed")
        relation_rows.append(Pauli(
            phase=(
                physical_product.phase - target_product.phase
            ) % 4,
            x=physical_product.x,
            z=physical_product.z,
        ))
        target_relation_phase_failures += (
            target_product.phase % 2
        )
    relation_rank = gf2_rank(
        row.symplectic(fixture.qubits) for row in relation_rows
    )
    physical_rank = gf2_rank(physical_vectors)
    target_rank = gf2_rank(target_vectors)
    central_failures = sum(
        anticommutes(relation, generator)
        for relation in relation_rows
        for generator in physical
    )
    relation_commutator_failures = sum(
        anticommutes(relation_rows[left], relation_rows[right])
        for left in range(len(relation_rows))
        for right in range(left)
    )
    pivots: dict[int, tuple[int, int]] = {}
    relation_phase_contradictions = 0
    for index, relation in enumerate(relation_rows):
        vector = relation.symplectic(fixture.qubits)
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (vector, combination)
                break
            old_vector, old_combination = pivots[pivot]
            vector ^= old_vector
            combination ^= old_combination
        else:
            replay = product(
                row
                for item, row in enumerate(relation_rows)
                if (combination >> item) & 1
            )
            relation_phase_contradictions += replay.phase != 0
    return {
        "generator_rows": len(rows),
        "physical_rank": physical_rank,
        "target_even_rank": target_rank,
        "expected_target_even_rank": 2 * fixture.matter_qubits - 1,
        "commutator_Gram_failures": gram_failures,
        "target_kernel_generators": len(target_kernel),
        "relation_stabilizer_rank": relation_rank,
        "relation_centralizer_failures": central_failures,
        "relation_mutual_commutator_failures": (
            relation_commutator_failures
        ),
        "relation_phase_contradictions": (
            relation_phase_contradictions
        ),
        "target_relation_phase_parity_failures": (
            target_relation_phase_failures
        ),
        "relation_rows": tuple(relation_rows),
    }


def qubit_cell(fixture: CompanionFixture, qubit: int) -> int:
    if qubit < fixture.matter_qubits:
        return qubit // 6
    return (qubit - fixture.matter_qubits) // 3
