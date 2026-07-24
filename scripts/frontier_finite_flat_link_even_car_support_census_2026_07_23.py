#!/usr/bin/env python3
"""Self-contained finite certificate for a flat-link even-CAR support census.

Paired note:
    docs/FINITE_FLAT_LINK_EVEN_CAR_SUPPORT_CENSUS_BOUNDED_THEOREM_NOTE_2026-07-23.md

The runner imports no campaign module or receipt.  It reconstructs the finite
graph/link code, the six-mode free-plus-contact factor family, the supplied
topological chart, and every reported control from definitions in this file.
It is a bounded support/census certificate, not a representation theorem,
autonomous update law, or physical-site compiler.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import schur


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1800
TOL = 2e-11
BETA = -0.3
CONTACT_COUPLING = 0.37
K = 129
LENGTHS = (3, 6, 7)
PASS = 0
FAIL = 0

DIRECTIONS = np.asarray(
    ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)),
    dtype=int,
)
REVERSE_MODE = (1, 0, 3, 2, 5, 4)
I6 = np.eye(6, dtype=complex)
REVERSE = np.zeros((6, 6), dtype=complex)
REVERSE[np.arange(6), REVERSE_MODE] = 1
UNIFORM = np.ones(6, dtype=complex) / math.sqrt(6)
P_SCALAR = np.outer(UNIFORM, UNIFORM.conj())
P_EVEN = (I6 + REVERSE) / 2 - P_SCALAR
P_VECTOR = (I6 - REVERSE) / 2


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {label} :: {detail}")


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


def covariance_controls(rows, internals) -> dict:
    mode_maps = tuple(direction_map(frame) for frame in FRAMES)
    mode_group_failures = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            direct = mode_maps[FRAME_INDEX[tuple(int(value) for value in (left @ right).ravel())]]
            mode_group_failures += tuple(
                mode_maps[left_index][mode_maps[right_index][mode]] for mode in range(6)
            ) != direct

    size_rows = []
    total_failures = mode_group_failures
    for row, code in zip(rows, internals):
        length = row["length"]
        graph = code["graph"]
        link = code["link"]
        link_maps = tuple(link_mapping(link, frame, length) for frame in FRAMES)
        B_failures = A_failures = link_dressing_failures = 0
        combined_covariance_executed = length == 3
        combined_local_failures = combined_correlation_failures = 0
        combined_pivots = (
            pauli_pivots(code["combined_constraints"], code["total_qubits"])
            if combined_covariance_executed
            else {}
        )
        for frame, link_map in zip(FRAMES, link_maps):
            data = frame_data(graph, frame)
            for source, generator in enumerate(code["B"]):
                B_failures += transform_pauli(generator, data) != code["B"][data.vertex_map[source]]
            for edge, (source, target, _kind, _owner) in enumerate(graph.base.edges):
                transformed = transform_pauli(graph.mapped_matter_A(edge), data)
                target_edge = graph.base.edge_lookup[frozenset((data.vertex_map[source], data.vertex_map[target]))]
                target_raw = graph.mapped_matter_A(target_edge)
                target_source, target_target, _target_kind, _target_owner = graph.base.edges[target_edge]
                expected_phase = 2 if (data.vertex_map[source], data.vertex_map[target]) == (target_target, target_source) else 0
                expected = Pauli((target_raw.phase + expected_phase) % 4, target_raw.x, target_raw.z)
                A_failures += transformed != expected
                linked = code["A_link"][edge]
                mapped_link = None if linked is None else link_map[linked]
                link_dressing_failures += mapped_link != code["A_link"][target_edge]
            if combined_covariance_executed:
                combined_local_failures += sum(
                    pauli_remainder(
                        transform_graph_link_pauli(
                            generator, data, link_map, code["graph_qubits"]
                        ),
                        combined_pivots,
                        code["total_qubits"],
                    )
                    != Pauli()
                    for generator in code["local_constraints"]
                )
                combined_correlation_failures += sum(
                    pauli_remainder(
                        transform_graph_link_pauli(
                            generator, data, link_map, code["graph_qubits"]
                        ),
                        combined_pivots,
                        code["total_qubits"],
                    )
                    != Pauli()
                    for generator in code["correlation_section"]
                )
        link_control = link_covariance(link, length)
        failures = B_failures + A_failures + link_dressing_failures + int(not link_control["pass"])
        total_failures += failures
        size_rows.append(
            {
                "length": length,
                "B_generator_map_failures": B_failures,
                "oriented_A_map_failures": A_failures,
                "link_dressing_map_failures": link_dressing_failures,
                "combined_code_space_covariance_executed": combined_covariance_executed,
                "combined_local_constraint_span_failures": combined_local_failures if combined_covariance_executed else None,
                "fixed_chart_correlation_span_failures": combined_correlation_failures if combined_covariance_executed else None,
                "fixed_combined_code_space_covariant": (
                    combined_local_failures == combined_correlation_failures == 0
                    if combined_covariance_executed
                    else None
                ),
                "transported_chart_covariant_by_construction": True,
                "link_covariance": link_control,
                "pass": failures == 0,
            }
        )
    return {
        "proper_cubic_frames": len(FRAMES),
        "frame_products": len(FRAMES) ** 2,
        "signed_six_mode_all576_group_failures": mode_group_failures,
        "fixed_chart_combined_code_space_covariant_at_L3": size_rows[0]["fixed_combined_code_space_covariant"],
        "combined_code_space_covariance_sizes": (3,),
        "fixed_chart_invariant_claimed": False,
        "compile_time_chart_transport_supplied": True,
        "size_rows": size_rows,
        "pass": total_failures == 0,
    }


def onsite_even_car_controls(internals) -> dict:
    """Execute the complete 6 B / 15 H onsite incidence algebra and transport."""

    size_rows = []
    total_failures = 0
    for code in internals:
        graph = code["graph"]
        local = code["local_constraints"]
        pivots = pauli_pivots(local, graph.qubits)
        B_square_failures = B_pair_commutator_failures = 0
        H_square_failures = B_H_incidence_failures = H_H_incidence_failures = 0
        H_triangle_on_code_phase_failures = 0
        derived_exact_frame_failures = derived_on_code_frame_failures = 0

        for cell in graph.cells:
            B = tuple(
                graph.B(graph.base.vertex_index[(cell, mode)]) for mode in range(6)
            )
            H = {
                pair: onsite_hopping(graph, cell, *pair)
                for pair in combinations(range(6), 2)
            }
            B_square_failures += sum(row @ row != Pauli() for row in B)
            B_pair_commutator_failures += sum(
                not B[left].commutes(B[right]) for left, right in combinations(range(6), 2)
            )
            H_square_failures += sum(row @ row != Pauli() for row in H.values())
            B_H_incidence_failures += sum(
                B[mode].commutes(row) == (mode in pair)
                for pair, row in H.items()
                for mode in range(6)
            )
            H_H_incidence_failures += sum(
                left_row.commutes(right_row) == (len(set(left_pair) & set(right_pair)) == 1)
                for (left_pair, left_row), (right_pair, right_row) in combinations(H.items(), 2)
            )
            H_triangle_on_code_phase_failures += sum(
                pauli_remainder(
                    H[(left, middle)] @ H[(middle, right)] @ H[(left, right)],
                    pivots,
                    graph.qubits,
                )
                != Pauli(phase=3)
                for left, middle, right in combinations(range(6), 3)
            )

        for frame in FRAMES:
            data = frame_data(graph, frame)
            modes = direction_map(frame)
            # One cell represents the translation orbit; the definitions and
            # frame map are exactly translation-covariant on the periodic torus.
            for cell in (graph.cells[0],):
                target_cell = tuple(
                    int(value % graph.length) for value in frame @ np.asarray(cell)
                )
                for left, right in combinations(range(6), 2):
                    transformed = transform_pauli(
                        onsite_hopping(graph, cell, left, right), data
                    )
                    mapped_left, mapped_right = modes[left], modes[right]
                    target = onsite_hopping(
                        graph,
                        target_cell,
                        min(mapped_left, mapped_right),
                        max(mapped_left, mapped_right),
                    )
                    if mapped_left > mapped_right:
                        target = Pauli((target.phase + 2) % 4, target.x, target.z)
                    difference = transformed @ target
                    derived_exact_frame_failures += difference != Pauli()
                    derived_on_code_frame_failures += (
                        pauli_remainder(difference, pivots, graph.qubits) != Pauli()
                    )

        failures = (
            B_square_failures
            + B_pair_commutator_failures
            + H_square_failures
            + B_H_incidence_failures
            + H_H_incidence_failures
            + H_triangle_on_code_phase_failures
            + derived_on_code_frame_failures
        )
        total_failures += failures
        size_rows.append(
            {
                "length": graph.length,
                "onsite_B_rows": 6 * graph.length**3,
                "onsite_H_rows": 15 * graph.length**3,
                "B_square_failures": B_square_failures,
                "B_pair_commutator_failures": B_pair_commutator_failures,
                "H_square_failures": H_square_failures,
                "B_H_endpoint_incidence_failures": B_H_incidence_failures,
                "H_H_endpoint_incidence_failures": H_H_incidence_failures,
                "H_triangle_minus_i_on_code_failures": H_triangle_on_code_phase_failures,
                "derived_all24_exact_Pauli_failures": derived_exact_frame_failures,
                "derived_all24_on_code_failures": derived_on_code_frame_failures,
                "derived_frame_translation_orbit_representatives": 1,
                "pass": failures == 0,
            }
        )
    return {
        "proper_cubic_frames": len(FRAMES),
        "complete_onsite_bilinears_per_cell": 15,
        "size_rows": size_rows,
        "pass": total_failures == 0,
    }


@dataclass(frozen=True)
class ModeGate:
    kind: str
    sites: tuple[int, ...]
    matrix: tuple[complex, ...]


def common_coin(beta: float = BETA) -> tuple[np.ndarray, float]:
    inertial_mass = float(3 * np.tan(-beta / 2))
    rest_phase = inertial_mass / 3
    coin = np.exp(1j * rest_phase) * (
        P_SCALAR - P_EVEN + np.exp(1j * beta) * P_VECTOR
    )
    return coin, inertial_mass


def one_particle_matrix(gate: ModeGate) -> np.ndarray:
    size = 1 if gate.kind == "phase" else 2
    return np.asarray(gate.matrix, dtype=complex).reshape(size, size)


def compile_adjacent_qr(unitary: np.ndarray):
    work = unitary.copy()
    eliminations = []
    for column in range(5):
        for lower in range(5, column, -1):
            upper = lower - 1
            a = work[upper, column]
            b = work[lower, column]
            if abs(b) < 1e-13:
                continue
            radius = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                ((np.conj(a) / radius, np.conj(b) / radius), (-b / radius, a / radius)),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    schedule = []
    for index, phase in enumerate(np.diag(work)):
        if abs(phase - 1) >= 1e-13:
            schedule.append(ModeGate("phase", (index,), (complex(phase),)))
    for upper, lower, elimination in reversed(eliminations):
        schedule.append(ModeGate("givens", (upper, lower), tuple(elimination.conj().T.reshape(-1))))
    reconstructed = np.eye(6, dtype=complex)
    for gate in schedule:
        factor = np.eye(6, dtype=complex)
        factor[np.ix_(gate.sites, gate.sites)] = one_particle_matrix(gate)
        reconstructed = factor @ reconstructed
    return tuple(schedule), {
        "givens": sum(gate.kind == "givens" for gate in schedule),
        "phases": sum(gate.kind == "phase" for gate in schedule),
        "diagonalization_residual": float(np.linalg.norm(work - np.diag(np.diag(work)))),
        "reconstruction_residual": float(np.linalg.norm(reconstructed - unitary)),
        "reconstructed": reconstructed,
    }


def occupied_modes(basis: int, mode_count: int):
    return tuple(mode for mode in range(mode_count) if (basis >> mode) & 1)


def fock_lift(unitary: np.ndarray) -> np.ndarray:
    mode_count = unitary.shape[0]
    dimension = 1 << mode_count
    occupied = tuple(occupied_modes(basis, mode_count) for basis in range(dimension))
    output = np.zeros((dimension, dimension), dtype=complex)
    for target, target_modes in enumerate(occupied):
        for source, source_modes in enumerate(occupied):
            if len(target_modes) != len(source_modes):
                continue
            output[target, source] = 1 if not target_modes else np.linalg.det(
                unitary[np.ix_(target_modes, source_modes)]
            )
    return output


def embedded_gate(gate: ModeGate) -> np.ndarray:
    one_particle = np.eye(6, dtype=complex)
    one_particle[np.ix_(gate.sites, gate.sites)] = one_particle_matrix(gate)
    return fock_lift(one_particle)


def number_sector_leakage(matrix: np.ndarray) -> float:
    numbers = np.asarray([basis.bit_count() for basis in range(matrix.shape[0])])
    forbidden = numbers[:, None] != numbers[None, :]
    return float(np.linalg.norm(matrix[forbidden]))


def local_factor_controls() -> tuple[dict, tuple[ModeGate, ...]]:
    coin, analytic_mass = common_coin()
    schedule, qr = compile_adjacent_qr(coin)
    gamma_coin = fock_lift(coin)
    compiled_coin = np.eye(64, dtype=complex)
    for gate in schedule:
        compiled_coin = embedded_gate(gate) @ compiled_coin

    contact_diagonal = np.asarray(
        [np.exp(1j * CONTACT_COUPLING * basis.bit_count() * (basis.bit_count() - 1) / 2) for basis in range(64)],
        dtype=complex,
    )
    contact = np.diag(contact_diagonal)
    compiled_contact_diagonal = np.ones(64, dtype=complex)
    for left, right in combinations(range(6), 2):
        for basis in range(64):
            if ((basis >> left) & 1) and ((basis >> right) & 1):
                compiled_contact_diagonal[basis] *= np.exp(1j * CONTACT_COUPLING)
    compiled_contact = np.diag(compiled_contact_diagonal)

    reverse_gates = tuple(
        ModeGate("givens", pair, tuple(np.asarray(((0, 1), (1, 0)), dtype=complex).reshape(-1)))
        for pair in ((0, 1), (2, 3), (4, 5))
    )
    compiled_reverse = np.eye(64, dtype=complex)
    for gate in reverse_gates:
        compiled_reverse = embedded_gate(gate) @ compiled_reverse
    direct_reverse = fock_lift(REVERSE)

    # This is a canonical 64-dimensional word reconstruction.  It is not an
    # intertwiner into the graph/link M2 factors: no such E is constructed here.
    direct = contact @ direct_reverse @ gamma_coin
    compiled = compiled_contact @ compiled_reverse @ compiled_coin
    explicit_inverse = np.eye(64, dtype=complex)
    for factor in (
        compiled_contact.conj().T,
        compiled_reverse.conj().T,
        compiled_coin.conj().T,
    ):
        explicit_inverse = factor @ explicit_inverse

    deleted_coin = np.eye(64, dtype=complex)
    for gate in schedule[1:]:
        deleted_coin = embedded_gate(gate) @ deleted_coin
    deleted_contact_diagonal = np.ones(64, dtype=complex)
    deleted_pair = next(iter(combinations(range(6), 2)))
    for left, right in tuple(combinations(range(6), 2))[1:]:
        for basis in range(64):
            if ((basis >> left) & 1) and ((basis >> right) & 1):
                deleted_contact_diagonal[basis] *= np.exp(1j * CONTACT_COUPLING)
    deleted_contact = np.diag(deleted_contact_diagonal)

    scalar_phase = complex(np.vdot(UNIFORM, qr["reconstructed"] @ UNIFORM))
    compiled_mass = float(np.angle(scalar_phase)) / (1 / 3)
    identity = np.eye(64, dtype=complex)
    rows = {
        "QR_Givens": qr["givens"],
        "QR_onsite_phases": qr["phases"],
        "one_particle_reconstruction_residual": qr["reconstruction_residual"],
        "exterior_coin_reconstruction_residual": float(np.linalg.norm(compiled_coin - gamma_coin)),
        "fifteen_contact_reconstruction_residual": float(np.linalg.norm(compiled_contact - contact)),
        "reverse_FSWAP_word_reconstruction_residual": float(np.linalg.norm(compiled_reverse - direct_reverse)),
        "full_M64_ordered_word_reconstruction_residual": float(np.linalg.norm(compiled - direct)),
        "full_M64_word_unitarity_residual": float(np.linalg.norm(compiled.conj().T @ compiled - identity)),
        "full_M64_explicit_inverse_residual": float(np.linalg.norm(explicit_inverse @ compiled - identity)),
        "number_sector_leakage_residual": number_sector_leakage(compiled),
        "compiled_rest_mass": compiled_mass,
        "analytic_mass_fixture": analytic_mass,
        "mass_fixture_residual": abs(compiled_mass - analytic_mass),
        "contact_active_two_particle_states": sum(basis.bit_count() == 2 for basis in range(64)),
        "contact_deletion_residual": float(np.linalg.norm(deleted_contact - contact, ord=2)),
        "expected_contact_deletion_residual": float(abs(np.exp(1j * CONTACT_COUPLING) - 1)),
        "deleted_coin_factor_residual": float(np.linalg.norm(deleted_coin - gamma_coin, ord=2)),
        "deleted_contact_pair": deleted_pair,
    }
    rows["pass"] = bool(
        rows["QR_Givens"] == 10
        and rows["QR_onsite_phases"] == 1
        and rows["one_particle_reconstruction_residual"] < TOL
        and rows["exterior_coin_reconstruction_residual"] < TOL
        and rows["fifteen_contact_reconstruction_residual"] < TOL
        and rows["reverse_FSWAP_word_reconstruction_residual"] < TOL
        and rows["full_M64_ordered_word_reconstruction_residual"] < TOL
        and rows["full_M64_word_unitarity_residual"] < TOL
        and rows["full_M64_explicit_inverse_residual"] < TOL
        and rows["number_sector_leakage_residual"] == 0
        and rows["mass_fixture_residual"] < TOL
        and rows["contact_active_two_particle_states"] == 15
        and abs(rows["contact_deletion_residual"] - rows["expected_contact_deletion_residual"]) < TOL
        and rows["deleted_coin_factor_residual"] > 1e-3
    )
    return rows, schedule


def polynomial_controls(schedule: tuple[ModeGate, ...]) -> dict:
    eye = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    left_B = np.kron(z, eye)
    right_B = np.kron(eye, z)
    hopping = np.kron(y, x)
    basis = []
    for left, right, active in product((0, 1), repeat=3):
        basis.append(
            (
                f"Bl^{left} Br^{right} A^{active}",
                np.linalg.matrix_power(left_B, left)
                @ np.linalg.matrix_power(right_B, right)
                @ np.linalg.matrix_power(hopping, active),
            )
        )

    def expand(matrix):
        coefficients = tuple(np.trace(row.conj().T @ matrix) / 4 for _name, row in basis)
        rebuilt = sum(
            (value * row for value, (_name, row) in zip(coefficients, basis)),
            np.zeros((4, 4), dtype=complex),
        )
        return coefficients, float(np.linalg.norm(rebuilt - matrix))

    maximum_coin = 0.0
    payload = []
    for gate in schedule:
        if gate.kind == "givens":
            matrix = fock_lift(one_particle_matrix(gate))
            coefficients, residual = expand(matrix)
            maximum_coin = max(maximum_coin, residual)
            payload.append(
                {
                    "sites": gate.sites,
                    "coefficients": tuple(
                        (basis[index][0], value.real.hex(), value.imag.hex())
                        for index, value in enumerate(coefficients)
                    ),
                }
            )

    phase = np.exp(1j * CONTACT_COUPLING)
    contact = np.diag((1, 1, 1, phase)).astype(complex)
    contact_coefficients, contact_residual = expand(contact)
    fswap = fock_lift(np.asarray(((0, 1), (1, 0)), dtype=complex))
    fswap_coefficients, fswap_residual = expand(fswap)
    expected_fswap = {
        "Bl^0 Br^1 A^0": 0.5,
        "Bl^0 Br^1 A^1": -0.5j,
        "Bl^1 Br^0 A^0": 0.5,
        "Bl^1 Br^0 A^1": 0.5j,
    }
    fswap_sign_failures = sum(
        abs(value - expected_fswap.get(name, 0)) > 1e-14
        for value, (name, _row) in zip(fswap_coefficients, basis)
    )
    contact_expected = {
        "Bl^0 Br^0 A^0": (3 + phase) / 4,
        "Bl^0 Br^1 A^0": (1 - phase) / 4,
        "Bl^1 Br^0 A^0": (1 - phase) / 4,
        "Bl^1 Br^1 A^0": (phase - 1) / 4,
    }
    contact_sign_failures = sum(
        abs(value - contact_expected.get(name, 0)) > 1e-14
        for value, (name, _row) in zip(contact_coefficients, basis)
    )
    rows = {
        "maximum_coin_polynomial_reconstruction_residual": maximum_coin,
        "contact_polynomial_reconstruction_residual": contact_residual,
        "FSWAP_polynomial_reconstruction_residual": fswap_residual,
        "contact_exact_coefficient_sign_failures": contact_sign_failures,
        "FSWAP_exact_coefficient_sign_failures": fswap_sign_failures,
        "coin_coefficient_sha256": sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest(),
    }
    rows["pass"] = bool(
        maximum_coin < TOL
        and contact_residual < TOL
        and fswap_residual < TOL
        and contact_sign_failures == fswap_sign_failures == 0
    )
    return rows


def three_mode_gate_controls(schedule: tuple[ModeGate, ...]) -> dict:
    """Catch cancellation of the helper parity in a two-edge onsite path.

    The endpoint modes occupy positions 0 and 2 and the path helper occupies
    position 1.  In little-endian Fock order the correct endpoint bilinear is
    ``Y_2 Z_1 X_0``.  The former extra ``B_helper`` changed it to
    ``Y_2 I_1 X_0``; applying identical polynomial coefficients to that wrong
    bilinear gives an operator-level comparison control.
    """

    eye = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    left_B = np.kron(np.kron(z, eye), eye)
    helper_B = np.kron(np.kron(eye, z), eye)
    right_B = np.kron(np.kron(eye, eye), z)
    correct_A = np.kron(np.kron(y, z), x)
    cancelled_A = helper_B @ correct_A

    def algebra_basis(active_A):
        return tuple(
            np.linalg.matrix_power(left_B, left)
            @ np.linalg.matrix_power(right_B, right)
            @ np.linalg.matrix_power(active_A, active)
            for left, right, active in product((0, 1), repeat=3)
        )

    correct_basis = algebra_basis(correct_A)
    cancelled_basis = algebra_basis(cancelled_A)

    def residuals(matrix):
        coefficients = tuple(np.trace(row.conj().T @ matrix) / 8 for row in correct_basis)
        correct = sum(
            (coefficient * row for coefficient, row in zip(coefficients, correct_basis)),
            np.zeros((8, 8), dtype=complex),
        )
        cancelled = sum(
            (coefficient * row for coefficient, row in zip(coefficients, cancelled_basis)),
            np.zeros((8, 8), dtype=complex),
        )
        return float(np.linalg.norm(correct - matrix)), float(np.linalg.norm(cancelled - matrix, ord=2))

    reverse_pairs = {(0, 1), (2, 3), (4, 5)}
    tested = []
    for gate in schedule:
        if gate.kind != "givens" or tuple(gate.sites) not in reverse_pairs:
            continue
        one_particle = np.eye(3, dtype=complex)
        one_particle[np.ix_((0, 2), (0, 2))] = one_particle_matrix(gate)
        tested.append(("coin_Givens", gate.sites, *residuals(fock_lift(one_particle))))
    swap = np.eye(3, dtype=complex)
    swap[np.ix_((0, 2), (0, 2))] = np.asarray(((0, 1), (1, 0)), dtype=complex)
    for pair in sorted(reverse_pairs):
        tested.append(("reverse_FSWAP", pair, *residuals(fock_lift(swap))))

    correct = [row[2] for row in tested]
    cancelled = [row[3] for row in tested]
    rows = {
        "three_mode_factors_tested": len(tested),
        "correct_two_edge_maximum_Frobenius_residual": max(correct),
        "extra_helper_B_minimum_operator_residual": min(cancelled),
        "factor_rows": tuple(
            {
                "kind": kind,
                "coarse_modes": pair,
                "correct_Frobenius_residual": good,
                "extra_helper_B_operator_residual": bad,
            }
            for kind, pair, good, bad in tested
        ),
    }
    rows["pass"] = bool(
        rows["three_mode_factors_tested"] == 8
        and rows["correct_two_edge_maximum_Frobenius_residual"] < TOL
        and rows["extra_helper_B_minimum_operator_residual"] > 1e-2
    )
    return rows


def factor_presentation(length: int, code, schedule: tuple[ModeGate, ...]):
    graph = code["graph"]
    B = code["B"]
    A = code["A"]
    factors = []

    def bv(cell, mode):
        return B[graph.base.vertex_index[(cell, mode)]]

    def add(kind, stage, cell, modes, rows):
        mask = 0
        for row in rows:
            mask |= support(row)
        factors.append(
            {
                "kind": kind,
                "stage": stage,
                "cell": cell,
                "modes": modes,
                "support": mask,
                "weight": mask.bit_count(),
            }
        )

    for gate_index, gate in enumerate(schedule):
        for cell in graph.cells:
            if gate.kind == "phase":
                mode = gate.sites[0]
                add("coin_phase", f"coin_{gate_index}", cell, (mode,), (bv(cell, mode),))
            else:
                left, right = gate.sites
                add(
                    "coin_Givens",
                    f"coin_{gate_index}",
                    cell,
                    (left, right),
                    (bv(cell, left), bv(cell, right), onsite_hopping(graph, cell, left, right)),
                )
    for reverse_index, (left, right) in enumerate(((0, 1), (2, 3), (4, 5))):
        for cell in graph.cells:
            add(
                "reverse_FSWAP",
                f"reverse_{reverse_index}",
                cell,
                (left, right),
                (bv(cell, left), bv(cell, right), onsite_hopping(graph, cell, left, right)),
            )
    for edge, (source, target, kind, _owner) in enumerate(graph.base.edges):
        if kind == "outer_square":
            left_cell, left_mode = graph.base.vertices[source]
            _right_cell, right_mode = graph.base.vertices[target]
            add("spatial_FSWAP", "spatial_stream", left_cell, (left_mode, right_mode), (B[source], B[target], A[edge]))
    for contact_index, (left, right) in enumerate(combinations(range(6), 2)):
        for cell in graph.cells:
            add(
                "contact_phase",
                f"contact_{contact_index}",
                cell,
                (left, right),
                (bv(cell, left), bv(cell, right)),
            )

    stages = defaultdict(list)
    for factor in factors:
        stages[factor["stage"]].append(factor)
    palette = total_layers = disjoint_failures = 0
    histogram = Counter()
    for stage in sorted(stages):
        colors = []
        for factor in stages[stage]:
            for color, union in enumerate(colors):
                if not (union & factor["support"]):
                    colors[color] |= factor["support"]
                    factor["color"] = color
                    break
            else:
                factor["color"] = len(colors)
                colors.append(factor["support"])
        palette = max(palette, len(colors))
        total_layers += len(colors)
        histogram[len(colors)] += 1
        by_color = defaultdict(list)
        for factor in stages[stage]:
            by_color[factor["color"]].append(factor["support"])
        for masks in by_color.values():
            union = 0
            for mask in masks:
                disjoint_failures += bool(union & mask)
                union |= mask

    modulus = 2 * K * length
    maximum_diameter = max(
        support_diameter(factor["support"], code["positions"], modulus) for factor in factors
    )
    cells = length**3
    kinds = Counter(factor["kind"] for factor in factors)
    row = {
        "length": length,
        "split": f"L{length}-finite-census",
        "complete_factor_count": len(factors),
        "expected_factor_count": 32 * cells,
        "factor_counts": dict(kinds),
        "ordered_stage_groups": len(stages),
        "finite_color_palette": palette,
        "sequential_color_layers": total_layers,
        "stage_color_count_histogram": dict(histogram),
        "support_disjoint_color_failures": disjoint_failures,
        "maximum_factor_M2_weight": max(factor["weight"] for factor in factors),
        "maximum_factor_fine_L1_diameter": maximum_diameter,
        "constant_overhead_active_algebra_M2_per_cell": 25,
        "factor_order_supplied": True,
        "autonomous_controller_constructed": False,
    }
    row["pass"] = bool(
        len(factors) == 32 * cells
        and kinds
        == {
            "coin_Givens": 10 * cells,
            "coin_phase": cells,
            "reverse_FSWAP": 3 * cells,
            "spatial_FSWAP": 3 * cells,
            "contact_phase": 15 * cells,
        }
        and len(stages) == 30
        and palette <= 7
        and total_layers <= 58
        and disjoint_failures == 0
        and row["maximum_factor_M2_weight"] <= 14
        and maximum_diameter <= 4 * K
    )
    return row


def walk_symbol(momentum: np.ndarray) -> np.ndarray:
    coin, _mass = common_coin()
    stream = np.diag(np.exp(-1j * (DIRECTIONS @ np.asarray(momentum, dtype=float))))
    return stream @ coin


def circular_distance(phases: np.ndarray, target: float) -> np.ndarray:
    return np.abs(np.angle(np.exp(1j * (phases - target))))


def band_subspace(
    momentum: np.ndarray,
    target_phase: float | None = None,
    target_value: complex | None = None,
    dimension: int | None = None,
    tolerance: float = 1e-7,
):
    triangular, vectors = schur(walk_symbol(momentum), output="complex")
    values = np.diag(triangular)
    phases = np.angle(values)
    if target_phase is not None:
        indices = np.where(circular_distance(phases, target_phase) < tolerance)[0]
    elif target_value is not None and dimension is not None:
        indices = np.argsort(np.abs(values - target_value))[:dimension]
    else:
        raise ValueError("supply target_phase or target_value and dimension")
    return phases[indices], vectors[:, indices]


def internal_wedge(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    amplitude = np.outer(first, second) - np.outer(second, first)
    return amplitude[np.triu_indices(6, 1)]


def contact_form_factor(particle_first, particle_second, hole_first, hole_second):
    result = np.zeros(
        (
            particle_first.shape[1] * particle_second.shape[1],
            hole_first.shape[1] * hole_second.shape[1],
        ),
        dtype=complex,
    )
    for first_hole in range(hole_first.shape[1]):
        for second_hole in range(hole_second.shape[1]):
            hole_wedge = internal_wedge(hole_first[:, first_hole], hole_second[:, second_hole])
            source = first_hole * hole_second.shape[1] + second_hole
            for first_particle in range(particle_first.shape[1]):
                for second_particle in range(particle_second.shape[1]):
                    particle_wedge = internal_wedge(
                        particle_first[:, first_particle], particle_second[:, second_particle]
                    )
                    target = first_particle * particle_second.shape[1] + second_particle
                    result[target, source] = np.vdot(particle_wedge, hole_wedge)
    return result


def bloch_subspace(momentum: np.ndarray, internal: np.ndarray, length: int) -> np.ndarray:
    coordinates = np.asarray(tuple(product(range(length), repeat=3)), dtype=float)
    envelope = np.exp(1j * (coordinates @ momentum)) / np.sqrt(length**3)
    return np.vstack(
        tuple((envelope[:, None] * internal[:, band][None, :]).reshape(-1) for band in range(internal.shape[1]))
    ).T


def direct_spatial_contact_block(particle_first, particle_second, hole_first, hole_second, length: int):
    result = np.zeros(
        (
            particle_first.shape[1] * particle_second.shape[1],
            hole_first.shape[1] * hole_second.shape[1],
        ),
        dtype=complex,
    )
    for site_number in range(length**3):
        local = slice(6 * site_number, 6 * (site_number + 1))
        result += contact_form_factor(
            particle_first[local], particle_second[local], hole_first[local], hole_second[local]
        )
    return result


def l3_modular_resonance_controls() -> tuple[dict, np.ndarray]:
    length = 3
    unit = 2 * np.pi / length
    momenta = {
        "h1": unit * np.asarray((0, 1, 0), dtype=float),
        "h2": unit * np.asarray((0, -1, 0), dtype=float),
        "p1": unit * np.asarray((1, 1, 1), dtype=float),
        "p2": unit * np.asarray((-1, -1, -1), dtype=float),
    }
    targets = {
        "h1": -0.148864781941705,
        "h2": -2.9904574355314986,
        "p1": 0.0759239848775555,
        "p2": 3.067939104828828,
    }
    subspaces = {name: band_subspace(momentum, targets[name]) for name, momentum in momenta.items()}
    phases = {name: subspaces[name][0] for name in subspaces}
    vectors = {name: subspaces[name][1] for name in subspaces}
    form = contact_form_factor(vectors["p1"], vectors["p2"], vectors["h1"], vectors["h2"])
    singulars = np.linalg.svd(form, compute_uv=False)
    phase_costs = (
        phases["p1"][:, None, None, None]
        + phases["p2"][None, :, None, None]
        - phases["h1"][None, None, :, None]
        - phases["h2"][None, None, None, :]
    )
    phase_residual = float(np.max(np.abs(phase_costs - 2 * np.pi)))

    spatial = {name: bloch_subspace(momenta[name], vectors[name], length) for name in vectors}
    direct = direct_spatial_contact_block(
        spatial["p1"], spatial["p2"], spatial["h1"], spatial["h2"], length
    )
    spatial_reduction_residual = float(np.linalg.norm(direct - form / length**3))

    unbalanced_momentum = momenta["p2"] + unit * np.asarray((1, 0, 0))
    triangular, unbalanced_vectors = schur(walk_symbol(unbalanced_momentum), output="complex")
    unbalanced_phases = np.angle(np.diag(triangular))
    unbalanced_vectors = unbalanced_vectors[:, unbalanced_phases > 1e-9]
    unbalanced_internal = contact_form_factor(
        vectors["p1"], unbalanced_vectors, vectors["h1"], vectors["h2"]
    )
    unbalanced_spatial = bloch_subspace(unbalanced_momentum, unbalanced_vectors, length)
    unbalanced_direct = direct_spatial_contact_block(
        spatial["p1"], unbalanced_spatial, spatial["h1"], spatial["h2"], length
    )

    rng = np.random.default_rng(2302)
    gauge_residuals = []
    for _ in range(12):
        rotated = {}
        for name, subspace in vectors.items():
            trial = rng.normal(size=(subspace.shape[1], subspace.shape[1]))
            trial = trial + 1j * rng.normal(size=trial.shape)
            gauge, _r = np.linalg.qr(trial)
            rotated[name] = subspace @ gauge
        rotated_form = contact_form_factor(
            rotated["p1"], rotated["p2"], rotated["h1"], rotated["h2"]
        )
        gauge_residuals.append(
            float(np.linalg.norm(np.linalg.svd(rotated_form, compute_uv=False) - singulars))
        )

    frame_residuals = []
    for frame in FRAMES:
        transformed = {
            name: band_subspace(frame @ momenta[name], targets[name])[1]
            for name in momenta
        }
        transformed_form = contact_form_factor(
            transformed["p1"], transformed["p2"], transformed["h1"], transformed["h2"]
        )
        frame_residuals.append(
            float(np.linalg.norm(np.linalg.svd(transformed_form, compute_uv=False) - singulars))
        )

    rows = {
        "phase_residual_to_2pi": phase_residual,
        "singular_values": tuple(float(value) for value in singulars),
        "form_Frobenius_norm": float(np.linalg.norm(form)),
        "direct_spatial_reduction_residual": spatial_reduction_residual,
        "momentum_balance_residual": float(
            max(
                np.linalg.norm(momenta["h1"] + momenta["h2"]),
                np.linalg.norm(momenta["p1"] + momenta["p2"]),
            )
        ),
        "unbalanced_internal_norm": float(np.linalg.norm(unbalanced_internal)),
        "unbalanced_spatial_norm": float(np.linalg.norm(unbalanced_direct)),
        "maximum_degenerate_basis_residual": max(gauge_residuals),
        "maximum_proper_cubic_singular_value_residual": max(frame_residuals),
        "proper_cubic_frames": len(frame_residuals),
    }
    rows["pass"] = bool(
        phase_residual < 3e-14
        and len(singulars) == 2
        and singulars[-1] > 0.45
        and singulars[0] > 0.49
        and np.linalg.norm(form) > 0.67
        and spatial_reduction_residual < 2e-15
        and rows["momentum_balance_residual"] < 2e-15
        and rows["unbalanced_internal_norm"] > 0.1
        and rows["unbalanced_spatial_norm"] < 2e-15
        and max(gauge_residuals) < 3e-15
        and max(frame_residuals) < 2e-13
    )
    return rows, form


def seam_block(lower: float, upper: float, target: complex):
    hole_phase_plus, hole_plus = band_subspace(
        np.full(3, lower), target_value=target, dimension=2
    )
    hole_phase_minus, hole_minus = band_subspace(
        np.full(3, -lower), target_value=target, dimension=2
    )
    particle_phase_plus, particle_plus = band_subspace(
        np.full(3, upper), target_value=target, dimension=2
    )
    particle_phase_minus, particle_minus = band_subspace(
        np.full(3, -upper), target_value=target, dimension=2
    )
    form = contact_form_factor(particle_plus, particle_minus, hole_plus, hole_minus)
    phase_cost = float(
        np.mean(particle_phase_plus)
        + np.mean(particle_phase_minus)
        - np.mean(hole_phase_plus)
        - np.mean(hole_phase_minus)
    )
    return form, phase_cost, {
        "hole_plus": hole_phase_plus,
        "hole_minus": hole_phase_minus,
        "particle_plus": particle_phase_plus,
        "particle_minus": particle_phase_minus,
    }


def finite_volume_seam_controls(form_l3: np.ndarray) -> dict:
    """Reexecute the shrinking-seam fixture retained from historical Cycle 230."""

    minus_root = 1.5783929737448452
    lengths = (18, 34, 78, 416)
    rows = []
    for length in lengths:
        lower_index = int(np.floor(minus_root * length / (2 * np.pi)))
        lower = 2 * np.pi * lower_index / length
        upper = 2 * np.pi * (lower_index + 1) / length
        form, phase_cost, phase_data = seam_block(lower, upper, -1)
        singulars = np.linalg.svd(form, compute_uv=False)
        rows.append(
            {
                "L": length,
                "lower_gap": minus_root - lower,
                "upper_gap": upper - minus_root,
                "phase_cost": phase_cost,
                "wrapped_phase": abs(float(np.angle(np.exp(1j * phase_cost)))),
                "singular_min": float(np.min(singulars)),
                "singular_max": float(np.max(singulars)),
                "frobenius": float(np.linalg.norm(form)),
                "raw_operator_over_g": float(np.max(singulars) / length**3),
                "hole_phase_max": float(
                    max(np.max(phase_data[name]) for name in ("hole_plus", "hole_minus"))
                ),
                "particle_phase_min": float(
                    min(np.min(phase_data[name]) for name in ("particle_plus", "particle_minus"))
                ),
                "maximum_degenerate_spread": float(
                    max(np.ptp(values) for values in phase_data.values())
                ),
            }
        )

    shrinking_pass = bool(
        rows[-1]["wrapped_phase"] < 0.0046
        and rows[-1]["wrapped_phase"] < rows[0]["wrapped_phase"] / 20
        and max(rows[-1]["lower_gap"], rows[-1]["upper_gap"]) < 0.0077
        and all(row["hole_phase_max"] < 0 for row in rows)
        and all(row["particle_phase_min"] > 0 for row in rows)
        and max(row["maximum_degenerate_spread"] for row in rows) < 3e-14
    )
    strength_pass = bool(
        min(row["singular_min"] for row in rows) > 0.97
        and rows[-1]["singular_min"] > 0.9998
        and abs(rows[-1]["singular_max"] - 1) < 2e-4
        and rows[-1]["raw_operator_over_g"] < rows[0]["raw_operator_over_g"] / 1000
    )

    plus_root = 1.563199679844947
    delta = 1e-3
    minus_singulars = np.linalg.svd(
        seam_block(minus_root - delta, minus_root + delta, -1)[0], compute_uv=False
    )
    plus_form, plus_cost, _ = seam_block(plus_root - delta, plus_root + delta, 1)
    plus_singulars = np.linalg.svd(plus_form, compute_uv=False)
    ordinary_crossing_residual = float(np.linalg.norm(minus_singulars - plus_singulars))

    last_length = lengths[-1]
    lower_index = int(np.floor(minus_root * last_length / (2 * np.pi)))
    lower = 2 * np.pi * lower_index / last_length
    upper = 2 * np.pi * (lower_index + 1) / last_length
    reference_singulars = np.linalg.svd(seam_block(lower, upper, -1)[0], compute_uv=False)
    frame_residuals = []
    for frame in FRAMES:
        subspaces = []
        for momentum in (
            np.full(3, upper),
            np.full(3, -upper),
            np.full(3, lower),
            np.full(3, -lower),
        ):
            subspaces.append(
                band_subspace(frame @ momentum, target_value=-1, dimension=2)[1]
            )
        transformed = contact_form_factor(*subspaces)
        frame_residuals.append(
            float(np.linalg.norm(np.linalg.svd(transformed, compute_uv=False) - reference_singulars))
        )

    rng = np.random.default_rng(230)
    source = rng.normal(size=form_l3.shape[1]) + 1j * rng.normal(size=form_l3.shape[1])
    target = rng.normal(size=form_l3.shape[0]) + 1j * rng.normal(size=form_l3.shape[0])
    source /= np.linalg.norm(source)
    target /= np.linalg.norm(target)
    spectator = np.asarray((1, 1j), dtype=complex) / np.sqrt(2)
    extra = np.asarray((np.sqrt(0.3), np.sqrt(0.7)), dtype=complex)
    base = np.vdot(target, form_l3 @ source)
    one_spectator = np.vdot(
        np.kron(target, spectator),
        np.kron(form_l3, np.eye(2)) @ np.kron(source, spectator),
    )
    two_spectators = np.vdot(
        np.kron(np.kron(target, spectator), extra),
        np.kron(form_l3, np.eye(4)) @ np.kron(np.kron(source, spectator), extra),
    )
    spectator_residual = float(max(abs(base - one_spectator), abs(base - two_spectators)))

    result = {
        "minus_root_selector": minus_root,
        "plus_root_selector": plus_root,
        "sampled_lengths": lengths,
        "rows": rows,
        "shrinking_phase_control_pass": shrinking_pass,
        "reduced_strength_control_pass": strength_pass,
        "ordinary_crossing_singular_residual": ordinary_crossing_residual,
        "ordinary_crossing_phase_cost": plus_cost,
        "maximum_proper_cubic_singular_residual": max(frame_residuals),
        "passive_spectator_residual": spectator_residual,
    }
    result["pass"] = bool(
        shrinking_pass
        and strength_pass
        and ordinary_crossing_residual < 3e-13
        and abs(plus_cost) < 7e-4
        and max(frame_residuals) < 3e-13
        and spectator_residual < 2e-15
    )
    return result


def source_dependency_closure() -> dict:
    source = Path(__file__).read_text(encoding="utf-8")
    forbidden = (
        "git" + " show",
        "merge" + "-base",
        "sub" + "process",
        "sys" + ".path",
        "docs/work_" + "history",
        "outputs/" + "physical_",
        "cycle" + "653",
        "cycle" + "656",
    )
    observed = {fragment: source.lower().count(fragment.lower()) for fragment in forbidden}
    imports = tuple(
        line.strip()
        for line in source.splitlines()
        if line.startswith("import ") or line.startswith("from ")
    )
    allowed = {
        "from __future__ import annotations",
        "from collections import Counter, defaultdict",
        "from dataclasses import dataclass",
        "from hashlib import sha256",
        "from itertools import combinations, permutations, product",
        "import json",
        "import math",
        "from pathlib import Path",
        "import numpy as np",
        "from scipy.linalg import schur",
    }
    return {
        "imports": imports,
        "unexpected_imports": tuple(sorted(set(imports) - allowed)),
        "forbidden_reference_counts": observed,
        "pass": not (set(imports) - allowed) and not any(observed.values()),
    }


def main() -> int:
    print("finite flat-link even-CAR support-census runner")
    print(f"sizes={LENGTHS} beta={BETA} contact_coupling={CONTACT_COUPLING}")
    result = {}
    try:
        closure = source_dependency_closure()
        check("fresh dependency closure has no campaign modules, receipts, Git objects, or ancestry gates", closure["pass"], closure)

        local, schedule = local_factor_controls()
        check(
            "six-mode coin/reverse/contact factors reconstruct the canonical M64 ordered word with inverse, leakage, deletion, and mass controls",
            local["pass"],
            {
                "word": local["full_M64_ordered_word_reconstruction_residual"],
                "inverse": local["full_M64_explicit_inverse_residual"],
                "mass": local["mass_fixture_residual"],
                "contact_deletion": local["contact_deletion_residual"],
            },
        )
        polynomials = polynomial_controls(schedule)
        check("coin/contact/FSWAP even-CAR polynomials reconstruct with exact sign controls", polynomials["pass"], polynomials)
        three_mode = three_mode_gate_controls(schedule)
        check(
            "three-mode endpoint controls retain helper parity and distinguish the extra-B expression",
            three_mode["pass"],
            three_mode,
        )
        l3_resonance, form_l3 = l3_modular_resonance_controls()
        check(
            "L3 modular resonance fixture is balanced, nonzero, basis-stable, spatially reduced, and all-24 covariant",
            l3_resonance["pass"],
            l3_resonance,
        )
        finite_seam = finite_volume_seam_controls(form_l3)
        check(
            "shrinking finite-volume seam fixture is reexecuted at L18/L34/L78/L416 "
            "(historical Cycle 230 provenance)",
            finite_seam["pass"],
            finite_seam,
        )

        rows = []
        internals = []
        presentations = []
        for length in LENGTHS:
            row, internal = graph_link_code(length)
            rows.append(row)
            internals.append(internal)
            check(
                f"L{length} 25-M2/cell graph/link quotient, local constraints, sectors, deletion, and malformed-domain controls",
                row["pass"],
                {
                    "rank": row["combined_rank"],
                    "quotient": row["matter_quotient_dimension"],
                    "gram": row["matter_quotient_symplectic_rank"],
                    "sector_failures": row["topological_sector_controls"]["all_eight_sector_failures"],
                },
            )
            presentation = factor_presentation(length, internal, schedule)
            presentations.append(presentation)
            check(
                f"L{length} displayed 32N factor census has bounded support and support-disjoint finite coloring",
                presentation["pass"],
                {
                    "factors": presentation["complete_factor_count"],
                    "palette": presentation["finite_color_palette"],
                    "layers": presentation["sequential_color_layers"],
                    "max_weight": presentation["maximum_factor_M2_weight"],
                },
            )

        finite_palette_bound = all(row["finite_color_palette"] <= 7 for row in presentations)
        check(
            "all three finite census sizes use at most seven support colors",
            finite_palette_bound,
            {f"L{row['length']}": row["finite_color_palette"] for row in presentations},
        )
        covariance = covariance_controls(rows, internals)
        check(
            "all 24 proper-cubic frames and all 576 products preserve signed modes, graph generators, links, constraints, and homology",
            covariance["pass"],
            covariance,
        )
        onsite_algebra = onsite_even_car_controls(internals)
        check(
            "all 15 onsite bilinears satisfy the even-CAR incidence algebra and derived all-24 covariance on code",
            onsite_algebra["pass"],
            onsite_algebra,
        )
        fixed_chart_boundary = {
            "executed_sizes": (3,),
            "L3_local_constraint_failures": covariance["size_rows"][0]["combined_local_constraint_span_failures"],
            "L3_correlation_section_failures": covariance["size_rows"][0]["fixed_chart_correlation_span_failures"],
            "fixed_chart_invariant_claimed": False,
            "transported_chart_supplied": True,
        }
        fixed_chart_boundary["pass"] = bool(
            fixed_chart_boundary["L3_local_constraint_failures"] == 0
            and fixed_chart_boundary["L3_correlation_section_failures"] > 0
        )
        check(
            "combined code-space covariance boundary is explicit: local constraints transport, fixed Wilson section does not",
            fixed_chart_boundary["pass"],
            fixed_chart_boundary,
        )

        support_census = {
            "scope": "finite L3, L6, and L7 census fixtures",
            "result": "rank, support, algebra, coloring, and fixture census for the displayed graph/link Pauli data",
            "physical_encoding_E_constructed": False,
            "E_G_intertwiner_test_executed": False,
            "all_displayed_32N_factor_supports_reexecuted": all(row["pass"] for row in presentations),
            "active_algebra_M2_per_cell": 25,
            "runtime_global_Jordan_Wigner_order": False,
            "runtime_nonlocal_parity_service": False,
            "runtime_Wilson_table": False,
            "compile_time_nonlocal_Wilson_section": True,
            "topological_input_chart_supplied": True,
            "autonomous_update_law_claimed": False,
            "physical_site_compiler_claimed": False,
            "pass": all(row["pass"] for row in rows + presentations)
            and local["pass"]
            and polynomials["pass"]
            and three_mode["pass"]
            and l3_resonance["pass"]
            and finite_seam["pass"]
            and covariance["pass"]
            and onsite_algebra["pass"]
            and fixed_chart_boundary["pass"],
        }
        check("bounded finite flat-link even-CAR support census", support_census["pass"], support_census)
        result = {
            "authority": "none",
            "audit": "unset",
            "claim_type": "bounded_theorem",
            "strict_autonomous_physical_law": False,
            "physical_site_compiler_claimed": False,
            "physical_encoding_E_constructed": False,
            "E_G_intertwiner_test_executed": False,
            "dependency_closure": closure,
            "canonical_M64_word": local,
            "even_CAR_polynomials": polynomials,
            "three_mode_helper_parity": three_mode,
            "L3_modular_resonance_fixture": l3_resonance,
            "shrinking_finite_volume_seam_fixture": finite_seam,
            "graph_link_rows": rows,
            "factor_presentations": presentations,
            "covariance": covariance,
            "onsite_even_CAR_algebra": onsite_algebra,
            "combined_code_space_covariance_boundary": fixed_chart_boundary,
            "support_census": support_census,
            "supplied_structure": {
                "runtime_dependencies": (
                    "Python standard library",
                    "NumPy",
                    "SciPy scipy.linalg.schur",
                ),
                "beta_minus_0p3_coin_family": True,
                "contact_coupling_0p37": True,
                "six_mode_direction_order": tuple(
                    tuple(int(value) for value in direction) for direction in DIRECTIONS
                ),
                "reverse_mode_map": REVERSE_MODE,
                "coin_formula": (
                    "C=exp(i*m/3)*(P_scalar-P_even+exp(i*beta)*P_vector), "
                    "m=3*tan(-beta/2)"
                ),
                "coin_projectors": {
                    "uniform_vector": "s=(1,1,1,1,1,1)/sqrt(6)",
                    "P_scalar": "|s><s|",
                    "P_even": "(I+R)/2-P_scalar",
                    "P_vector": "(I-R)/2",
                    "R": "reverse-mode permutation (0 1)(2 3)(4 5)",
                },
                "pauli_convention": (
                    "i^phase X^x Z^z; product phase adds "
                    "2*popcount(z_left & x_right) modulo 4"
                ),
                "periodic_L3_L6_L7_domains": True,
                "rough_puncture_graph_and_one_terminal_per_cell": True,
                "local_incident_edge_order": "ascending construction index",
                "missing_reverse_pair_helper": "first admissible third mode in ascending mode order",
                "flat_link_logical_section_and_three_topological_inputs": True,
                "compile_time_nonlocal_Wilson_correlation_section": True,
                "K129_sparse_placement_scale": True,
                "fine_support_embedding": {
                    "periodic_modulus": "2*K*L",
                    "cell_center": "2*K*cell",
                    "rough_terminal_offset": "0",
                    "puncture_spoke_offset": "8*direction[mode]",
                    "internal_edge_offset": "4*(direction[left]+direction[right])",
                    "outer_edge_offset": "32*direction[source_mode]",
                    "flat_link_midpoint": "cell_center+K*axis_unit_vector",
                },
                "Wilson_chart_convention": {
                    "origin": (0, 0, 0),
                    "axis_loop_steps": "0 through L-1",
                    "transverse_mode_axis": "(axis+1) mod 3",
                },
                "flat_link_chart_convention": {
                    "logical_Z": "axis loop through the coordinate origin",
                    "logical_X": "axis-oriented links on the coordinate-zero plane",
                    "sector_gradient_root": (0, 0, 0),
                    "topological_bit_insertion": "positive-axis periodic wrap link",
                },
                "thirty_stage_group_factor_order": True,
                "color_labels_supplied": False,
                "coloring_convention": (
                    "deterministic greedy first-fit within lexicographically sorted stages; "
                    "factors retain construction and lexicographic cell order"
                ),
                "compile_time_frame_and_chart_transport": True,
                "L3_target_momentum_indices": {
                    "h1": (0, 1, 0),
                    "h2": (0, -1, 0),
                    "p1": (1, 1, 1),
                    "p2": (-1, -1, -1),
                },
                "L3_target_phases": {
                    "h1": -0.148864781941705,
                    "h2": -2.9904574355314986,
                    "p1": 0.0759239848775555,
                    "p2": 3.067939104828828,
                },
                "seam_root_locations": {
                    "minus_one": 1.5783929737448452,
                    "plus_one": 1.563199679844947,
                },
                "finite_seam_lengths": (18, 34, 78, 416),
                "selection_and_numerical_conventions": {
                    "global_residual_tolerance": TOL,
                    "QR_drop_and_phase_cutoff": 1e-13,
                    "polynomial_coefficient_sign_tolerance": 1e-14,
                    "L3_band_phase_tolerance": 1e-7,
                    "unbalanced_positive_phase_cutoff": 1e-9,
                    "seam_eigenvalue_selector": "two nearest eigenvalues to supplied target",
                    "seam_selected_dimension": 2,
                    "seam_root_neighborhood_delta": 1e-3,
                },
                "acceptance_thresholds": {
                    "L3_phase_residual": 3e-14,
                    "L3_singular_minima": (0.49, 0.45),
                    "L3_form_Frobenius_minimum": 0.67,
                    "L3_spatial_and_momentum_residual": 2e-15,
                    "L3_unbalanced_internal_minimum": 0.1,
                    "L3_degenerate_basis_residual": 3e-15,
                    "L3_proper_cubic_residual": 2e-13,
                    "seam_terminal_wrapped_phase": 0.0046,
                    "seam_terminal_gap": 0.0077,
                    "seam_degenerate_spread": 3e-14,
                    "seam_singular_minimum_all_sizes": 0.97,
                    "seam_terminal_singular_minimum": 0.9998,
                    "seam_terminal_singular_maximum_residual": 2e-4,
                    "seam_crossing_and_frame_residual": 3e-13,
                    "seam_plus_phase_cost": 7e-4,
                    "passive_spectator_residual": 2e-15,
                    "extra_helper_B_operator_residual_minimum": 1e-2,
                    "deleted_coin_factor_residual_minimum": 1e-3,
                    "color_palette_maximum": 7,
                    "sequential_layers_maximum": 58,
                    "factor_weight_maximum": 14,
                },
                "deterministic_RNG_seeds": {
                    "degenerate_band_basis": 2302,
                    "passive_spectator": 230,
                },
                "topological_input_bits_supplied": True,
                "physical_M64_to_M2_encoding_E": False,
                "blank_M2_reference_preparation": False,
                "autonomous_controller_clock_work_return": False,
                "reference_or_topological_sector_genesis": False,
            },
            "scope_boundaries": {
                "controller": "the 30-stage-group, at-most-58-layer factor order is supplied",
                "physical_encoding": "no M64-to-graph/link code isometry E is constructed or tested",
                "reference_genesis": "the correlated graph/link section is supplied; no blank preparation is constructed",
                "topological_sector": "three input qubits are lawful and all eight basis sectors are checked, but no local genesis/selection mechanism is supplied",
                "fixed_chart_covariance": "the local constraints transport, but the supplied fixed Wilson correlation section has measured span failures",
                "static_local_alignment": "the logical graph/link alignment is supplied rather than enforced by one commuting all-local static constraint family",
            },
        }
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner exception :: {exc!r}")
    result["tests_passed"] = PASS
    result["tests_failed"] = FAIL
    result["pass"] = FAIL == 0
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True, default=float))
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
