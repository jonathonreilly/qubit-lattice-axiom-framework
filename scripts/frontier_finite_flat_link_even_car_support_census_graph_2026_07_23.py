#!/usr/bin/env python3
"""Pauli/GF(2), cellulation, graph/link, frame, and covariance definitions.

Ordinary-import helper for the finite flat-link even-CAR support census.  This
module is source-complete in the restricted audit packet; it is not a separate
claim or authority surface.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product

import numpy as np


K = 129
DIRECTIONS = np.asarray(
    ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)),
    dtype=int,
)
REVERSE_MODE = (1, 0, 3, 2, 5, 4)


def bit_indices(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


@dataclass(frozen=True)
class Pauli:
    """Pauli ``i^phase X^x Z^z`` represented by integer support masks."""

    phase: int = 0
    x: int = 0
    z: int = 0

    def __matmul__(self, other: "Pauli") -> "Pauli":
        phase = (self.phase + other.phase + 2 * (self.z & other.x).bit_count()) % 4
        return Pauli(phase, self.x ^ other.x, self.z ^ other.z)

    def commutes(self, other: "Pauli") -> bool:
        return ((self.x & other.z).bit_count() + (self.z & other.x).bit_count()) % 2 == 0

    def symplectic(self, qubits: int) -> int:
        return self.x | (self.z << qubits)


def pauli_product(rows) -> Pauli:
    result = Pauli()
    for row in rows:
        result = result @ row
    return result


def echelon(rows) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for source in rows:
        row = int(source)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return pivots


def gf2_rank(rows) -> int:
    return len(echelon(rows))


def phase_rank(rows, qubits: int) -> tuple[int, int]:
    pivots: dict[int, Pauli] = {}
    inconsistent = 0
    for original in rows:
        row = original
        vector = row.symplectic(qubits)
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                row = row @ pivots[pivot]
                vector = row.symplectic(qubits)
            else:
                pivots[pivot] = row
                break
        if not vector and row.phase % 4:
            inconsistent += 1
    return len(pivots), inconsistent


def pauli_pivots(rows, qubits: int) -> dict[int, Pauli]:
    """Return a phase-carrying echelon basis for a commuting Pauli family."""

    pivots: dict[int, Pauli] = {}
    for original in rows:
        row = original
        vector = row.symplectic(qubits)
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                row = row @ pivots[pivot]
                vector = row.symplectic(qubits)
            else:
                pivots[pivot] = row
                break
    return pivots


def pauli_remainder(row: Pauli, pivots: dict[int, Pauli], qubits: int) -> Pauli:
    """Reduce a Pauli including phase, so ``Pauli()`` means exact membership."""

    vector = row.symplectic(qubits)
    while vector:
        pivot = vector.bit_length() - 1
        if pivot not in pivots:
            return row
        row = row @ pivots[pivot]
        vector = row.symplectic(qubits)
    return row


def quotient_complement(base, candidates) -> tuple[int, ...]:
    pivots = echelon(base)
    output = []
    for source in candidates:
        row = int(source)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                output.append(int(source))
                break
    return tuple(output)


def independent_pauli_basis(rows, qubits: int) -> tuple[Pauli, ...]:
    pivots: dict[int, int] = {}
    output = []
    for pauli in rows:
        reduced = pauli.symplectic(qubits)
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                output.append(pauli)
                break
    return tuple(output)


def symplectic_product(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    return (
        ((left & mask) & (right >> qubits)).bit_count()
        + ((left >> qubits) & (right & mask)).bit_count()
    ) & 1


def symplectic_gram_rank(rows: tuple[int, ...], qubits: int) -> int:
    gram = []
    for left in rows:
        row = 0
        for index, right in enumerate(rows):
            if symplectic_product(left, right, qubits):
                row |= 1 << index
        gram.append(row)
    return gf2_rank(gram)


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    unique = {tuple(int(value) for value in frame.ravel()): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


FRAMES = proper_cubic_frames()
FRAME_INDEX = {tuple(int(value) for value in frame.ravel()): index for index, frame in enumerate(FRAMES)}


def signed_axis(frame: np.ndarray, axis: int) -> tuple[int, int]:
    image = frame @ np.eye(3, dtype=int)[:, axis]
    target = int(np.flatnonzero(image)[0])
    return target, int(image[target])


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    output = []
    for direction in DIRECTIONS:
        transformed = frame @ direction
        output.append(int(np.flatnonzero(np.all(DIRECTIONS == transformed, axis=1))[0]))
    return tuple(output)


@dataclass(frozen=True)
class BaseEdge:
    u: int
    v: int
    kind: str
    owner: tuple[int, int, int]


class PyramidCellulation:
    """Dual graph of the proper-cubic square-pyramid coarse-cell subdivision."""

    def __init__(self, length: int):
        if length < 3:
            raise ValueError("periodic L>=3 required")
        self.length = length
        self.cells = tuple(product(range(length), repeat=3))
        self.vertices = []
        self.vertex_index = {}
        for cell in self.cells:
            for mode in range(6):
                self.vertex_index[(cell, mode)] = len(self.vertices)
                self.vertices.append((cell, mode))
        self.edges: list[tuple[int, int, str, tuple[int, int, int]]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}

        def add_edge(u: int, v: int, kind: str, owner) -> None:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate edge", u, v))
            self.edge_lookup[key] = len(self.edges)
            self.edges.append((u, v, kind, owner))

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE_MODE[left] != right:
                    add_edge(
                        self.vertex_index[(cell, left)],
                        self.vertex_index[(cell, right)],
                        "internal_triangle",
                        cell,
                    )
            for axis in range(3):
                target = list(cell)
                target[axis] = (target[axis] + 1) % length
                add_edge(
                    self.vertex_index[(cell, 2 * axis)],
                    self.vertex_index[(tuple(target), 2 * axis + 1)],
                    "outer_square",
                    cell,
                )
        self.incident = [[] for _ in self.vertices]
        for edge, (u, v, _kind, _owner) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()

    def edge_between(self, u: int, v: int) -> int:
        return self.edge_lookup[frozenset((u, v))]

    def cycle_mask(self, vertices: list[int]) -> int:
        mask = 0
        for index, source in enumerate(vertices):
            mask ^= 1 << self.edge_between(source, vertices[(index + 1) % len(vertices)])
        return mask


def primal_edge_cycles(graph: PyramidCellulation):
    rows = []
    for cell in graph.cells:
        for bits in product((0, 1), repeat=3):
            modes = [2 * axis + (0 if bits[axis] else 1) for axis in range(3)]
            vertices = [graph.vertex_index[(cell, mode)] for mode in modes]
            rows.append((graph.cycle_mask(vertices), vertices, "center_corner_edge"))
    for corner in graph.cells:
        for axis in range(3):
            first, second = [value for value in range(3) if value != axis]

            def local_cell(first_shift: int, second_shift: int):
                cell = list(corner)
                cell[first] = (cell[first] - first_shift) % graph.length
                cell[second] = (cell[second] - second_shift) % graph.length
                return tuple(cell)

            def first_direction(shift: int) -> int:
                return 2 * first + (0 if shift else 1)

            def second_direction(shift: int) -> int:
                return 2 * second + (0 if shift else 1)

            labels = (
                (local_cell(0, 0), first_direction(0)),
                (local_cell(0, 0), second_direction(0)),
                (local_cell(0, 1), second_direction(1)),
                (local_cell(0, 1), first_direction(0)),
                (local_cell(1, 1), first_direction(1)),
                (local_cell(1, 1), second_direction(1)),
                (local_cell(1, 0), second_direction(0)),
                (local_cell(1, 0), first_direction(1)),
            )
            vertices = [graph.vertex_index[label] for label in labels]
            rows.append((graph.cycle_mask(vertices), vertices, "coarse_grid_edge"))
    return rows


def wilson_cycles(graph: PyramidCellulation) -> list[list[int]]:
    rows = []
    for axis in range(3):
        transverse = (axis + 1) % 3
        vertices = []
        for step in range(graph.length):
            cell = [0, 0, 0]
            cell[axis] = step
            next_cell = list(cell)
            next_cell[axis] = (next_cell[axis] + 1) % graph.length
            vertices.extend(
                (
                    graph.vertex_index[(tuple(cell), 2 * axis)],
                    graph.vertex_index[(tuple(next_cell), 2 * axis + 1)],
                    graph.vertex_index[(tuple(next_cell), 2 * transverse)],
                )
            )
        rows.append(vertices)
    return rows


@dataclass(frozen=True)
class Edge:
    u: int
    v: int | None
    kind: str
    owner: tuple[int, int, int]
    label: int = -1


class PunctureGraph:
    """One rough terminal and six sink spokes added to each coarse cell."""

    def __init__(self, length: int):
        self.length = length
        self.base = PyramidCellulation(length)
        self.cells = self.base.cells
        self.cell_index = {cell: index for index, cell in enumerate(self.cells)}
        self.matter_count = len(self.base.vertices)
        self.vertices = list(self.base.vertices) + [(cell, "sink") for cell in self.cells]
        self.sink_index = {cell: self.matter_count + self.cell_index[cell] for cell in self.cells}
        self.edges: list[Edge] = []
        self.edge_lookup = {}
        self.spoke_lookup = {}
        self.terminal_lookup = {}

        def add_internal(u: int, v: int, kind: str, owner, label: int = -1) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate", u, v, kind))
            index = len(self.edges)
            self.edges.append(Edge(u, v, kind, owner, label))
            self.edge_lookup[key] = index
            return index

        for u, v, kind, owner in self.base.edges:
            add_internal(u, v, f"matter_{kind}", owner)
        for cell in self.cells:
            sink = self.sink_index[cell]
            for mode in range(6):
                index = add_internal(
                    sink,
                    self.base.vertex_index[(cell, mode)],
                    "puncture_spoke",
                    cell,
                    mode,
                )
                self.spoke_lookup[(cell, mode)] = index
        for cell in self.cells:
            index = len(self.edges)
            self.edges.append(Edge(self.sink_index[cell], None, "rough_terminal", cell, 0))
            self.terminal_lookup[(cell, 0)] = index

        self.incident = [[] for _ in self.vertices]
        for edge, row in enumerate(self.edges):
            self.incident[row.u].append(edge)
            if row.v is not None:
                self.incident[row.v].append(edge)
        for row in self.incident:
            row.sort()

    @property
    def qubits(self) -> int:
        return len(self.edges)

    def edge_between(self, u: int, v: int) -> int:
        return self.edge_lookup[frozenset((u, v))]

    def B(self, vertex: int) -> Pauli:
        z = 0
        for edge in self.incident[vertex]:
            z ^= 1 << edge
        return Pauli(z=z)

    def A(self, source: int, target: int) -> Pauli:
        edge = self.edge_between(source, target)
        z = 0
        for vertex in (source, target):
            for incident in self.incident[vertex]:
                if incident == edge:
                    break
                z ^= 1 << incident
        return Pauli(0 if source < target else 2, 1 << edge, z)

    def cycle_mask(self, vertices: list[int]) -> int:
        mask = 0
        for index, source in enumerate(vertices):
            mask ^= 1 << self.edge_between(source, vertices[(index + 1) % len(vertices)])
        return mask

    def loop_pauli(self, vertices: list[int]) -> Pauli:
        result = Pauli(phase=len(vertices) % 4)
        for index, source in enumerate(vertices):
            result = result @ self.A(source, vertices[(index + 1) % len(vertices)])
        return result

    def local_cycles(self):
        rows = list(primal_edge_cycles(self.base))
        for u, v, kind, owner in self.base.edges:
            if kind == "internal_triangle":
                vertices = [self.sink_index[owner], u, v]
                rows.append((self.cycle_mask(vertices), vertices, "puncture_triangle"))
        return rows

    def wilson_cycles(self):
        return wilson_cycles(self.base)

    def cell_constraint(self, cell) -> Pauli:
        result = self.B(self.sink_index[cell])
        for mode in range(6):
            result = result @ self.B(self.base.vertex_index[(cell, mode)])
        return result

    def mapped_matter_A(self, base_edge: int) -> Pauli:
        u, v, kind, _owner = self.base.edges[base_edge]
        result = self.A(u, v)
        if kind == "outer_square":
            left_cell = self.base.vertices[u][0]
            right_cell = self.base.vertices[v][0]
            result = result @ Pauli(
                x=(1 << self.terminal_lookup[(left_cell, 0)])
                ^ (1 << self.terminal_lookup[(right_cell, 0)])
            )
        return result


def local_stabilizers(graph: PunctureGraph) -> tuple[Pauli, ...]:
    return tuple(
        [graph.loop_pauli(vertices) for _mask, vertices, _kind in graph.local_cycles()]
        + [graph.cell_constraint(cell) for cell in graph.cells]
    )


def wilson_initializers(graph: PunctureGraph) -> tuple[Pauli, ...]:
    return tuple(graph.loop_pauli(vertices) for vertices in graph.wilson_cycles())


def gauge_Z(graph: PunctureGraph, cell) -> Pauli:
    terminal = graph.terminal_lookup[(cell, 0)]
    return graph.B(graph.sink_index[cell]) @ Pauli(z=1 << terminal)


def gauge_generators(graph: PunctureGraph):
    return tuple(gauge_Z(graph, cell) for cell in graph.cells)


def hermitian_normalize(pauli: Pauli) -> Pauli:
    return Pauli((pauli.x & pauli.z).bit_count() & 1, pauli.x, pauli.z)


def onsite_hopping(graph: PunctureGraph, cell, left: int, right: int) -> Pauli:
    if left == right:
        raise ValueError("onsite hopping endpoints must differ")
    if left > right:
        canonical = onsite_hopping(graph, cell, right, left)
        return Pauli((canonical.phase + 2) % 4, canonical.x, canonical.z)
    source = graph.base.vertex_index[(cell, left)]
    target = graph.base.vertex_index[(cell, right)]
    direct_key = frozenset((source, target))
    if direct_key in graph.base.edge_lookup:
        return graph.mapped_matter_A(graph.base.edge_lookup[direct_key])
    helper = next(
        graph.base.vertex_index[(cell, mode)]
        for mode in range(6)
        if mode not in (left, right)
        and frozenset((source, graph.base.vertex_index[(cell, mode)])) in graph.base.edge_lookup
        and frozenset((graph.base.vertex_index[(cell, mode)], target)) in graph.base.edge_lookup
    )
    first = graph.mapped_matter_A(graph.base.edge_lookup[frozenset((source, helper))])
    second = graph.mapped_matter_A(graph.base.edge_lookup[frozenset((helper, target))])
    # The two-edge product already carries the intermediate Jordan-Wigner
    # parity.  Multiplying B(helper) cancels that parity and breaks the even-CAR
    # incidence algebra for the three absent reverse pairs.  The minus sign is
    # the orientation calibration fixed by H_ij H_jk H_ik = -i on code.
    result = hermitian_normalize(first @ second)
    return Pauli((result.phase + 2) % 4, result.x, result.z)


def add_cell(cell, axis: int, amount: int, length: int):
    row = list(cell)
    row[axis] = (row[axis] + amount) % length
    return tuple(row)


def link_code(length: int):
    cells = tuple(product(range(length), repeat=3))
    links = tuple((cell, axis) for cell in cells for axis in range(3))
    index = {link: q for q, link in enumerate(links)}
    stars = []
    for cell in cells:
        mask = 0
        for axis in range(3):
            mask ^= 1 << index[(cell, axis)]
            mask ^= 1 << index[(add_cell(cell, axis, -1, length), axis)]
        stars.append(Pauli(x=mask))
    plaquettes = []
    for cell in cells:
        for first, second in combinations(range(3), 2):
            mask = (
                (1 << index[(cell, first)])
                ^ (1 << index[(add_cell(cell, first, 1, length), second)])
                ^ (1 << index[(add_cell(cell, second, 1, length), first)])
                ^ (1 << index[(cell, second)])
            )
            plaquettes.append(Pauli(z=mask))
    logical_z = []
    logical_x = []
    for axis in range(3):
        logical_z.append(
            Pauli(z=sum(1 << index[(tuple(step if value == axis else 0 for value in range(3)), axis)] for step in range(length)))
        )
        logical_x.append(
            Pauli(x=sum(1 << index[(cell, axis)] for cell in cells if cell[axis] == 0))
        )
    return {
        "cells": cells,
        "links": links,
        "index": index,
        "qubits": len(links),
        "stars": tuple(stars),
        "plaquettes": tuple(plaquettes),
        "logical_z": tuple(logical_z),
        "logical_x": tuple(logical_x),
    }


def directed_link(left, right, length: int):
    for axis in range(3):
        if add_cell(left, axis, 1, length) == right:
            return left, axis
        if add_cell(right, axis, 1, length) == left:
            return right, axis
    raise AssertionError((left, right, length))


def lift_link_z(graph_qubits: int, link_index: int) -> Pauli:
    return Pauli(z=1 << (graph_qubits + link_index))


def support(row: Pauli) -> int:
    return row.x | row.z


def periodic_l1(left, right, modulus: int) -> int:
    return sum(min((a - b) % modulus, (b - a) % modulus) for a, b in zip(left, right))


def support_diameter(mask: int, positions, modulus: int) -> int:
    points = tuple(positions[q] for q in bit_indices(mask))
    if len(points) < 2:
        return 0
    return max(periodic_l1(left, right, modulus) for left, right in combinations(points, 2))


def graph_position(graph: PunctureGraph, qubit: int):
    row = graph.edges[qubit]
    center = 2 * K * np.asarray(row.owner, dtype=int)
    if row.kind == "rough_terminal":
        offset = np.zeros(3, dtype=int)
    elif row.kind == "puncture_spoke":
        offset = 8 * DIRECTIONS[row.label]
    elif row.kind == "matter_internal_triangle":
        left = graph.base.vertices[row.u][1]
        right = graph.base.vertices[row.v][1]
        offset = 4 * (DIRECTIONS[left] + DIRECTIONS[right])
    elif row.kind == "matter_outer_square":
        offset = 32 * DIRECTIONS[graph.base.vertices[row.u][1]]
    else:
        raise ValueError(row.kind)
    return tuple(int(value % (2 * K * graph.length)) for value in center + offset)


def link_midpoint(cell, axis: int, length: int):
    modulus = 2 * K * length
    row = [(2 * K * cell[value]) % modulus for value in range(3)]
    row[axis] = (row[axis] + K) % modulus
    return tuple(row)


def sector_controls(code, length: int) -> dict:
    """Execute the flat-link gradient/topological formula in all eight sectors."""

    cells = code["cells"]
    root = (0, 0, 0)
    nonroot = tuple(cell for cell in cells if cell != root)
    gauge_index = {cell: index for index, cell in enumerate(nonroot)}
    topological_offset = len(nonroot)

    def gauge_value(cell):
        return 0 if cell == root else 1 << gauge_index[cell]

    expressions = []
    for cell, axis in code["links"]:
        target = add_cell(cell, axis, 1, length)
        value = gauge_value(cell) ^ gauge_value(target)
        if cell[axis] == length - 1:
            value ^= 1 << (topological_offset + axis)
        expressions.append(value)

    flatness_failures = 0
    for plaquette in code["plaquettes"]:
        value = 0
        for q in bit_indices(plaquette.z):
            value ^= expressions[q]
        flatness_failures += value != 0

    sector_failures = 0
    sector_rows = []
    for sector in range(8):
        assignment = 0
        for axis in range(3):
            if (sector >> axis) & 1:
                assignment |= 1 << (topological_offset + axis)
        link_values = tuple((expression & assignment).bit_count() & 1 for expression in expressions)
        plaquette_failures = sum(
            (sum(link_values[q] for q in bit_indices(row.z)) & 1) != 0
            for row in code["plaquettes"]
        )
        loop_failures = 0
        measured = []
        for axis in range(3):
            cursor = [0, 0, 0]
            value = 0
            for _ in range(length):
                value ^= link_values[code["index"][(tuple(cursor), axis)]]
                cursor[axis] = (cursor[axis] + 1) % length
            measured.append(value)
            loop_failures += value != ((sector >> axis) & 1)
        sector_failures += plaquette_failures + loop_failures
        sector_rows.append(
            {
                "sector": tuple(1 if (sector >> axis) & 1 else 0 for axis in range(3)),
                "measured_loop_bits": tuple(measured),
                "plaquette_failures": plaquette_failures,
                "loop_failures": loop_failures,
            }
        )

    return {
        "expression_rank": gf2_rank(expressions),
        "expected_expression_rank": length**3 + 2,
        "formula_flatness_failures": flatness_failures,
        "all_eight_sector_failures": sector_failures,
        "sector_rows": sector_rows,
        "topological_input_qubits": 3,
        "topological_input_preparation_or_genesis_constructed": False,
        "pass": gf2_rank(expressions) == length**3 + 2
        and flatness_failures == sector_failures == 0,
    }


def graph_link_code(length: int):
    graph = PunctureGraph(length)
    link = link_code(length)
    cells = length**3
    graph_qubits = graph.qubits
    total = graph_qubits + link["qubits"]
    local = local_stabilizers(graph)
    wilsons = wilson_initializers(graph)
    gauge_z = gauge_generators(graph)
    cell_index = {cell: index for index, cell in enumerate(graph.cells)}

    correlations = []
    for link_index, (cell, axis) in enumerate(link["links"]):
        target = add_cell(cell, axis, 1, length)
        row = (
            lift_link_z(graph_qubits, link_index)
            @ gauge_z[cell_index[cell]]
            @ gauge_z[cell_index[target]]
        )
        if cell[axis] == length - 1:
            row = row @ wilsons[axis]
        correlations.append(row)
    correlations = tuple(correlations)
    combined = local + correlations

    lifted_plaquettes = []
    plaquette_equal_failures = 0
    for plaquette in link["plaquettes"]:
        lifted = Pauli(plaquette.phase, plaquette.x << graph_qubits, plaquette.z << graph_qubits)
        lifted_plaquettes.append(lifted)
        actual = pauli_product(correlations[q] for q in bit_indices(plaquette.z))
        plaquette_equal_failures += actual != lifted
    lifted_plaquettes = tuple(lifted_plaquettes)

    B = tuple(graph.B(vertex) for vertex in range(graph.matter_count))
    A = []
    A_link = []
    outer = 0
    for edge, (source, target, kind, _owner) in enumerate(graph.base.edges):
        row = graph.mapped_matter_A(edge)
        linked = None
        if kind == "outer_square":
            left = graph.base.vertices[source][0]
            right = graph.base.vertices[target][0]
            cell, axis = directed_link(left, right, length)
            linked = link["index"][(cell, axis)]
            row = row @ lift_link_z(graph_qubits, linked)
            outer += 1
        A.append(row)
        A_link.append(linked)
    A = tuple(A)
    matter = B + A

    local_rank, local_inconsistent = phase_rank(local, total)
    combined_rank, combined_inconsistent = phase_rank(combined, total)
    combined_vectors = tuple(row.symplectic(total) for row in combined)
    matter_vectors = tuple(row.symplectic(total) for row in matter)
    representatives = quotient_complement(combined_vectors, matter_vectors)
    quotient_dimension = len(representatives)
    quotient_gram_rank = symplectic_gram_rank(representatives, total)
    stabilizer_commutator_failures = sum(
        not generator.commutes(stabilizer)
        for generator in matter
        for stabilizer in combined
    )

    dressing_type_failures = 0
    for edge, linked in enumerate(A_link):
        delta = graph.mapped_matter_A(edge) @ A[edge]
        expected = Pauli() if linked is None else lift_link_z(graph_qubits, linked)
        dressing_type_failures += delta != expected

    positions = tuple(graph_position(graph, q) for q in range(graph_qubits))
    positions += tuple(link_midpoint(cell, axis, length) for cell, axis in link["links"])
    modulus = 2 * K * length
    placement_collisions = len(positions) - len(set(positions))

    gauss = []
    for cell in graph.cells:
        parity = pauli_product(
            B[graph.base.vertex_index[(cell, mode)]] for mode in range(6)
        )
        star_x = Pauli()
        for axis in range(3):
            star_x = star_x @ Pauli(x=1 << (graph_qubits + link["index"][(cell, axis)]))
            prior = add_cell(cell, axis, -1, length)
            star_x = star_x @ Pauli(x=1 << (graph_qubits + link["index"][(prior, axis)]))
        gauss.append(parity @ star_x)
    gauss = tuple(gauss)
    gauss_matter_failures = sum(not row.commutes(generator) for row in gauss for generator in matter)
    gauss_plaquette_failures = sum(not row.commutes(plaquette) for row in gauss for plaquette in lifted_plaquettes)

    local_basis = independent_pauli_basis(local, total)
    deleted_rank, _deleted_inconsistent = phase_rank(local_basis[1:] + correlations, total)
    flipped = (
        Pauli((correlations[0].phase + 2) % 4, correlations[0].x, correlations[0].z),
    ) + correlations[1:]
    _flipped_rank, flipped_inconsistent = phase_rank(local + flipped + (correlations[0],), total)
    sectors = sector_controls(link, length)

    maximum_gauss_diameter = max(
        support_diameter(support(row), positions, modulus) for row in gauss
    )
    maximum_plaquette_diameter = max(
        support_diameter(support(row), positions, modulus) for row in lifted_plaquettes
    )
    maximum_correlation_weight = max(support(row).bit_count() for row in correlations)
    maximum_correlation_diameter = max(
        support_diameter(support(row), positions, modulus) for row in correlations
    )
    row = {
        "length": length,
        "split": f"L{length}-finite-census",
        "coarse_cells": cells,
        "graph_M2": graph_qubits,
        "flat_link_M2": link["qubits"],
        "active_M2": total,
        "active_M2_per_cell": total // cells,
        "graph_local_rank": local_rank,
        "expected_graph_local_rank": 15 * cells - 2,
        "combined_rank": combined_rank,
        "expected_combined_rank": 18 * cells - 2,
        "combined_code_exponent": total - combined_rank,
        "expected_code_exponent": 7 * cells + 2,
        "matter_quotient_dimension": quotient_dimension,
        "expected_matter_quotient_dimension": 12 * cells - 1,
        "matter_quotient_symplectic_rank": quotient_gram_rank,
        "expected_matter_quotient_symplectic_rank": 12 * cells - 2,
        "matter_center_dimension": quotient_dimension - quotient_gram_rank,
        "outer_link_dressed_A": outer,
        "plaquette_product_equality_failures": plaquette_equal_failures,
        "dressing_type_failures": dressing_type_failures,
        "matter_constraint_commutator_failures": stabilizer_commutator_failures,
        "local_Gauss_rows": len(gauss),
        "Gauss_matter_commutator_failures": gauss_matter_failures,
        "Gauss_plaquette_commutator_failures": gauss_plaquette_failures,
        "maximum_Gauss_weight": max(support(row).bit_count() for row in gauss),
        "maximum_plaquette_weight": max(support(row).bit_count() for row in lifted_plaquettes),
        "maximum_Gauss_fine_L1_diameter": maximum_gauss_diameter,
        "maximum_plaquette_fine_L1_diameter": maximum_plaquette_diameter,
        "maximum_compile_time_correlation_weight": maximum_correlation_weight,
        "maximum_compile_time_correlation_fine_L1_diameter": maximum_correlation_diameter,
        "placement_collisions": placement_collisions,
        "delete_one_independent_check_rank": deleted_rank,
        "expected_deleted_rank": combined_rank - 1,
        "malformed_phase_inconsistencies": flipped_inconsistent,
        "topological_sector_controls": sectors,
    }
    row["pass"] = bool(
        local_inconsistent == combined_inconsistent == 0
        and local_rank == 15 * cells - 2
        and combined_rank == 18 * cells - 2
        and total - combined_rank == 7 * cells + 2
        and quotient_dimension == 12 * cells - 1
        and quotient_gram_rank == 12 * cells - 2
        and quotient_dimension - quotient_gram_rank == 1
        and outer == 3 * cells
        and plaquette_equal_failures == dressing_type_failures == stabilizer_commutator_failures == 0
        and gauss_matter_failures == gauss_plaquette_failures == placement_collisions == 0
        and maximum_gauss_diameter <= 4 * K
        and maximum_plaquette_diameter <= 2 * K
        and deleted_rank == combined_rank - 1
        and flipped_inconsistent > 0
        and sectors["pass"]
    )
    internal = {
        "graph": graph,
        "link": link,
        "B": B,
        "A": A,
        "A_link": tuple(A_link),
        "positions": positions,
        "local_constraints": local,
        "correlation_section": correlations,
        "combined_constraints": combined,
        "graph_qubits": graph_qubits,
        "total_qubits": total,
    }
    return row, internal


def permute_mask(mask: int, mapping) -> int:
    output = 0
    for source in bit_indices(mask):
        output ^= 1 << mapping[source]
    return output


def gf2_basis(rows):
    return echelon(rows)


def in_span(value: int, pivots) -> bool:
    while value:
        pivot = value.bit_length() - 1
        if pivot not in pivots:
            return False
        value ^= pivots[pivot]
    return True


def link_mapping(code, frame: np.ndarray, length: int):
    mapping = []
    for cell, axis in code["links"]:
        target_axis, sign = signed_axis(frame, axis)
        mapped = tuple(int(value) % length for value in frame @ np.asarray(cell, dtype=int))
        if sign < 0:
            mapped = add_cell(mapped, target_axis, -1, length)
        mapping.append(code["index"][(mapped, target_axis)])
    return tuple(mapping)


def link_covariance(code, length: int) -> dict:
    mappings = tuple(link_mapping(code, frame, length) for frame in FRAMES)
    frame_bijection_failures = sum(len(set(mapping)) != code["qubits"] for mapping in mappings)
    group_failures = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            direct = mappings[FRAME_INDEX[tuple(int(value) for value in (left @ right).ravel())]]
            group_failures += tuple(
                mappings[left_index][mappings[right_index][q]] for q in range(code["qubits"])
            ) != direct
    star_masks = {row.x for row in code["stars"]}
    plaquette_masks = {row.z for row in code["plaquettes"]}
    plaquette_basis = gf2_basis(plaquette_masks)
    star_basis = gf2_basis(star_masks)
    constraint_failures = 0
    homology_failures = 0
    for frame, mapping in zip(FRAMES, mappings):
        constraint_failures += sum(permute_mask(row.x, mapping) not in star_masks for row in code["stars"])
        constraint_failures += sum(permute_mask(row.z, mapping) not in plaquette_masks for row in code["plaquettes"])
        for axis in range(3):
            target, _sign = signed_axis(frame, axis)
            homology_failures += not in_span(
                permute_mask(code["logical_z"][axis].z, mapping) ^ code["logical_z"][target].z,
                plaquette_basis,
            )
            homology_failures += not in_span(
                permute_mask(code["logical_x"][axis].x, mapping) ^ code["logical_x"][target].x,
                star_basis,
            )
    return {
        "proper_cubic_frames": len(FRAMES),
        "frame_products": len(FRAMES) ** 2,
        "frame_bijection_failures": frame_bijection_failures,
        "all576_group_failures": group_failures,
        "constraint_image_failures": constraint_failures,
        "logical_homology_image_failures": homology_failures,
        "pass": frame_bijection_failures == group_failures == constraint_failures == homology_failures == 0,
    }


def graph_frame_maps(graph: PunctureGraph, frame: np.ndarray):
    modes = direction_map(frame)
    vertex_map = []
    for vertex in range(graph.matter_count):
        cell, mode = graph.base.vertices[vertex]
        target_cell = tuple(int(value % graph.length) for value in frame @ np.asarray(cell))
        vertex_map.append(graph.base.vertex_index[(target_cell, modes[mode])])
    for cell in graph.cells:
        target_cell = tuple(int(value % graph.length) for value in frame @ np.asarray(cell))
        vertex_map.append(graph.sink_index[target_cell])
    edge_map = []
    for row in graph.edges:
        if row.v is None:
            target_cell = tuple(int(value % graph.length) for value in frame @ np.asarray(row.owner))
            edge_map.append(graph.terminal_lookup[(target_cell, row.label)])
        else:
            edge_map.append(graph.edge_between(vertex_map[row.u], vertex_map[row.v]))
    return tuple(vertex_map), tuple(edge_map)


def order_gauge(graph: PunctureGraph, vertex_map, edge_map):
    toggles = [0] * graph.qubits
    pairs = []
    for source_vertex, target_vertex in enumerate(vertex_map):
        pulled = [edge_map[edge] for edge in graph.incident[source_vertex]]
        position = {edge: index for index, edge in enumerate(graph.incident[target_vertex])}
        for index, left in enumerate(pulled):
            for right in pulled[index + 1 :]:
                if position[left] > position[right]:
                    toggles[left] ^= 1 << right
                    toggles[right] ^= 1 << left
                    pairs.append((left, right))
    return tuple(toggles), tuple(pairs)


@dataclass(frozen=True)
class FrameData:
    vertex_map: tuple[int, ...]
    edge_map: tuple[int, ...]
    toggles: tuple[int, ...]
    pairs: frozenset[frozenset[int]]
    flips: int


def transform_pauli(pauli: Pauli, data: FrameData) -> Pauli:
    x = z = 0
    for source in bit_indices(pauli.x):
        x ^= 1 << data.edge_map[source]
    for source in bit_indices(pauli.z):
        z ^= 1 << data.edge_map[source]
    phase = pauli.phase
    xbits = tuple(bit_indices(x))
    if len(xbits) > 1:
        phase = (phase + 2 * sum(frozenset(pair) in data.pairs for pair in combinations(xbits, 2))) % 4
    for edge in xbits:
        z ^= data.toggles[edge]
    phase = (phase + 2 * (x & data.flips).bit_count()) % 4
    return Pauli(phase, x, z)


def frame_data(graph: PunctureGraph, frame: np.ndarray) -> FrameData:
    vertex_map, edge_map = graph_frame_maps(graph, frame)
    toggles, pairs = order_gauge(graph, vertex_map, edge_map)
    pair_set = frozenset(frozenset(pair) for pair in pairs)
    provisional = FrameData(vertex_map, edge_map, toggles, pair_set, 0)
    flips = 0
    for source_edge, row in enumerate(graph.edges):
        if row.v is None:
            continue
        transformed = transform_pauli(graph.A(row.u, row.v), provisional)
        target = graph.A(vertex_map[row.u], vertex_map[row.v])
        if (transformed.phase - target.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
    return FrameData(vertex_map, edge_map, toggles, pair_set, flips)


def transform_graph_link_pauli(
    pauli: Pauli,
    data: FrameData,
    link_map: tuple[int, ...],
    graph_qubits: int,
) -> Pauli:
    """Transport both graph and link factors, preserving the Pauli phase."""

    graph_mask = (1 << graph_qubits) - 1
    graph_part = transform_pauli(
        Pauli(pauli.phase, pauli.x & graph_mask, pauli.z & graph_mask), data
    )
    link_x = permute_mask(pauli.x >> graph_qubits, link_map) << graph_qubits
    link_z = permute_mask(pauli.z >> graph_qubits, link_map) << graph_qubits
    return Pauli(graph_part.phase, graph_part.x | link_x, graph_part.z | link_z)
