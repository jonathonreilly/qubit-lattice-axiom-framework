#!/usr/bin/env python3
"""Independent adversarial reconstruction of the OpenReference full update.

This runner intentionally does *not* import the joined Cycle870 runner, the
placement runner, Cycle703, Cycle712, or any other top-level compiler.
It reconstructs the graph, Pauli algebra, logical chart, physical repetition
lift, ordered Cycle219/Cycle230 word, and cubic semantics locally.  The only
physics inputs imported from current main are the supplied Cycle219 coin family
and Cycle230 beta/contact coupling.

The receipt distinguishes three statements which must not be conflated:

* each reverse/dressed-stream FSWAP polynomial is a Hermitian involution on the
  entire graph-edge Hilbert space;
* the correctly ordered full update is exact on the common loop/D code;
* the first-rail Z extension is equivariant under an orientation reversal only
  modulo the stream repetition stabilizer (the physical site permutation itself
  is, of course, a full-space representation).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path
import subprocess
import sys
from typing import Iterable, Sequence

import numpy as np


DEFAULT_REPO = Path(__file__).resolve().parents[1]
TARGET_JOIN_REL = "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py"
TARGET_PLACEMENT_REL = "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py"
TARGET_JOIN_RECEIPT_REL = "outputs/cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json"
EXPECTED_BASE_COMMIT = "4d6dedee82a14e13cbccb8bf62d6eac1227a4f0c"
EXPECTED_DIRECT_INPUT_SHA256 = {
    "common_matter_field_coin_family_cycle219_2026_07_16.py": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
}
EXPECTED_TARGET_SHA256 = {
    TARGET_JOIN_REL: "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
    TARGET_PLACEMENT_REL: "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
    TARGET_JOIN_RECEIPT_REL: "d6be75419b1fab56853127d55730b63a23ef7d44205e66b7fa73c9f19aac8611",
}
TOL = 8.0e-10

Coord = tuple[int, int, int]
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
REVERSE = (1, 0, 3, 2, 5, 4)
REVERSE_PAIRS = ((0, 1), (2, 3), (4, 5))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def box(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
    return tuple(product(*(range(length) for length in shape)))


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] + right[i] for i in range(3))


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * component for component in row)


@dataclass(frozen=True)
class Pauli:
    """i^phase X^x Z^z, with little-endian bit masks."""

    phase: int = 0
    x: int = 0
    z: int = 0

    def __post_init__(self) -> None:
        object.__setattr__(self, "phase", self.phase % 4)

    def __matmul__(self, other: "Pauli") -> "Pauli":
        # Z(left) X(right) contributes one minus sign per overlap.
        phase = self.phase + other.phase + 2 * ((self.z & other.x).bit_count() & 1)
        return Pauli(phase, self.x ^ other.x, self.z ^ other.z)

    def dagger(self) -> "Pauli":
        # (XZ)^dagger = (-1)^(x.z) XZ.
        return Pauli(-self.phase + 2 * ((self.x & self.z).bit_count() & 1), self.x, self.z)

    def commutes(self, other: "Pauli") -> bool:
        return (((self.x & other.z).bit_count() + (self.z & other.x).bit_count()) & 1) == 0

    def hermitian(self) -> bool:
        return self == self.dagger()

    def support(self) -> int:
        return self.x | self.z

    def weight(self) -> int:
        return self.support().bit_count()

    def symplectic(self, qubits: int) -> int:
        return self.x | (self.z << qubits)


Polynomial = dict[tuple[int, int], complex]


def clean_poly(value: dict[tuple[int, int], complex], tol: float = 2e-12) -> Polynomial:
    return {key: complex(coefficient) for key, coefficient in value.items() if abs(coefficient) > tol}


def pauli_polynomial(rows: Iterable[tuple[complex, Pauli]]) -> Polynomial:
    output: dict[tuple[int, int], complex] = defaultdict(complex)
    for coefficient, row in rows:
        output[(row.x, row.z)] += coefficient * (1j ** row.phase)
    return clean_poly(output)


def poly_add(*values: Polynomial) -> Polynomial:
    output: dict[tuple[int, int], complex] = defaultdict(complex)
    for value in values:
        for key, coefficient in value.items():
            output[key] += coefficient
    return clean_poly(output)


def poly_scale(value: Polynomial, coefficient: complex) -> Polynomial:
    return clean_poly({key: coefficient * item for key, item in value.items()})


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    output: dict[tuple[int, int], complex] = defaultdict(complex)
    for (lx, lz), lc in left.items():
        for (rx, rz), rc in right.items():
            sign = -1 if ((lz & rx).bit_count() & 1) else 1
            output[(lx ^ rx, lz ^ rz)] += sign * lc * rc
    return clean_poly(output)


def poly_dagger(value: Polynomial) -> Polynomial:
    return clean_poly(
        {
            (x, z): coefficient.conjugate() * (-1 if ((x & z).bit_count() & 1) else 1)
            for (x, z), coefficient in value.items()
        }
    )


IDENTITY_POLY: Polynomial = {(0, 0): 1.0 + 0.0j}


def poly_residual(left: Polynomial, right: Polynomial) -> float:
    keys = set(left) | set(right)
    return float(math.sqrt(sum(abs(left.get(key, 0) - right.get(key, 0)) ** 2 for key in keys)))


def poly_unitarity_residual(value: Polynomial) -> float:
    return poly_residual(poly_mul(poly_dagger(value), value), IDENTITY_POLY)


def poly_involution_residual(value: Polynomial) -> float:
    return poly_residual(poly_mul(value, value), IDENTITY_POLY)


def poly_hermiticity_residual(value: Polynomial) -> float:
    return poly_residual(value, poly_dagger(value))


def pauli_product(rows: Iterable[Pauli]) -> Pauli:
    result = Pauli()
    for row in rows:
        result = result @ row
    return result


def gf2_rank(rows: Iterable[int]) -> int:
    basis: dict[int, int] = {}
    for source in rows:
        row = source
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


class SignedStabilizerReducer:
    """Canonicalize Pauli polynomials modulo signed +1 stabilizers."""

    def __init__(self, stabilizers: Sequence[Pauli], qubits: int):
        self.qubits = qubits
        self.basis: dict[int, tuple[int, Pauli]] = {}
        for source in stabilizers:
            row = source
            vector = row.symplectic(qubits)
            while vector:
                pivot = vector.bit_length() - 1
                if pivot in self.basis:
                    _, prior = self.basis[pivot]
                    row = row @ prior
                    vector = row.symplectic(qubits)
                else:
                    self.basis[pivot] = (vector, row)
                    break
            if not vector and row != Pauli():
                raise AssertionError(("inconsistent signed stabilizer", row))

    @property
    def rank(self) -> int:
        return len(self.basis)

    def pauli(self, source: Pauli) -> Pauli:
        row = source
        vector = row.symplectic(self.qubits)
        for pivot in sorted(self.basis, reverse=True):
            if (vector >> pivot) & 1:
                _, prior = self.basis[pivot]
                row = row @ prior
                vector = row.symplectic(self.qubits)
        return row

    def polynomial(self, value: Polynomial) -> Polynomial:
        output: dict[tuple[int, int], complex] = defaultdict(complex)
        for (x, z), coefficient in value.items():
            row = self.pauli(Pauli(0, x, z))
            output[(row.x, row.z)] += coefficient * (1j ** row.phase)
        return clean_poly(output)


class OpenReferenceGraph:
    """Independent reconstruction of the seven-vertex open graph."""

    def __init__(self, cells: Sequence[Coord]):
        self.cells = tuple(sorted(set(cells)))
        if not self.cells:
            raise ValueError("empty graph")
        self.cell_set = set(self.cells)
        self.vertices: list[tuple[Coord, int]] = []
        self.vertex_index: dict[tuple[Coord, int], int] = {}
        for cell in self.cells:
            for mode in range(7):
                self.vertex_index[(cell, mode)] = len(self.vertices)
                self.vertices.append((cell, mode))

        self.edges: list[tuple[int, int, str, Coord]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.cross_edge: dict[tuple[Coord, int, int], int] = {}

        def add_edge(u: int, v: int, kind: str, owner: Coord) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise AssertionError(("duplicate edge", key))
            index = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = index
            return index

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] != right:
                    add_edge(
                        self.vertex_index[(cell, left)],
                        self.vertex_index[(cell, right)],
                        "octahedral",
                        cell,
                    )
            reference = self.vertex_index[(cell, 6)]
            for mode in range(6):
                add_edge(reference, self.vertex_index[(cell, mode)], "spoke", cell)

        for cell in self.cells:
            for axis in range(3):
                target = list(cell)
                target[axis] += 1
                target_cell = tuple(target)
                if target_cell not in self.cell_set:
                    continue
                matter = add_edge(
                    self.vertex_index[(cell, 2 * axis + 1)],
                    self.vertex_index[(target_cell, 2 * axis)],
                    "matter_stream",
                    cell,
                )
                reference = add_edge(
                    self.vertex_index[(cell, 6)],
                    self.vertex_index[(target_cell, 6)],
                    "reference_bond",
                    cell,
                )
                self.cross_edge[(cell, axis, 0)] = matter
                self.cross_edge[(cell, axis, 1)] = reference

        self.incident: list[list[int]] = [[] for _ in self.vertices]
        for edge, (u, v, _kind, _owner) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()

    @property
    def coarse_edges(self) -> int:
        return sum(kind == "matter_stream" for _u, _v, kind, _owner in self.edges)

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

    def path_A(self, vertices: Sequence[int]) -> Pauli:
        # i^(length-2) converts the ordered Majorana-edge product to A(path).
        result = Pauli((len(vertices) - 2) % 4)
        for left, right in zip(vertices, vertices[1:]):
            result = result @ self.A(left, right)
        return result

    def loop(self, vertices: Sequence[int]) -> Pauli:
        result = Pauli(len(vertices) % 4)
        for index, source in enumerate(vertices):
            result = result @ self.A(source, vertices[(index + 1) % len(vertices)])
        return result

    def D(self, cell: Coord) -> Pauli:
        return pauli_product(self.B(self.vertex_index[(cell, mode)]) for mode in range(7))


def local_cycles(graph: OpenReferenceGraph) -> tuple[tuple[Pauli, str, object], ...]:
    rows: list[tuple[Pauli, str, object]] = []
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for left, right in combinations(range(6), 2):
            if REVERSE[left] == right:
                continue
            rows.append(
                (
                    graph.loop(
                        (
                            reference,
                            graph.vertex_index[(cell, left)],
                            graph.vertex_index[(cell, right)],
                        )
                    ),
                    "cell_triangle",
                    (cell, left, right),
                )
            )
    for (cell, axis, copy), _edge in graph.cross_edge.items():
        if copy:
            continue
        target = list(cell)
        target[axis] += 1
        target_cell = tuple(target)
        rows.append(
            (
                graph.loop(
                    (
                        graph.vertex_index[(cell, 6)],
                        graph.vertex_index[(cell, 2 * axis + 1)],
                        graph.vertex_index[(target_cell, 2 * axis)],
                        graph.vertex_index[(target_cell, 6)],
                    )
                ),
                "bond_rectangle",
                (cell, axis),
            )
        )
    for cell in graph.cells:
        for first, second in combinations(range(3), 2):
            c10 = list(cell)
            c10[first] += 1
            c10 = tuple(c10)
            c01 = list(cell)
            c01[second] += 1
            c01 = tuple(c01)
            c11 = list(cell)
            c11[first] += 1
            c11[second] += 1
            c11 = tuple(c11)
            if not all(row in graph.cell_set for row in (c10, c01, c11)):
                continue
            rows.append(
                (
                    graph.loop(
                        (
                            graph.vertex_index[(cell, 2 * first + 1)],
                            graph.vertex_index[(c10, 2 * first)],
                            graph.vertex_index[(c10, 2 * second + 1)],
                            graph.vertex_index[(c11, 2 * second)],
                            graph.vertex_index[(c11, 2 * first)],
                            graph.vertex_index[(c01, 2 * first + 1)],
                            graph.vertex_index[(c01, 2 * second)],
                            graph.vertex_index[(cell, 2 * second + 1)],
                        )
                    ),
                    "coarse_plaquette",
                    (cell, first, second),
                )
            )
    return tuple(rows)


def constraints(graph: OpenReferenceGraph) -> tuple[Pauli, ...]:
    return tuple(row for row, _kind, _key in local_cycles(graph)) + tuple(
        graph.D(cell) for cell in graph.cells
    )


def logical_pairs(graph: OpenReferenceGraph) -> dict[tuple[Coord, int], tuple[Pauli, Pauli]]:
    output: dict[tuple[Coord, int], tuple[Pauli, Pauli]] = {}
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            zrow = graph.B(graph.vertex_index[(cell, mode)])
            suffix = pauli_product(
                graph.B(graph.vertex_index[(cell, other)]) for other in range(mode, 6)
            )
            xrow = Pauli(3) @ suffix @ graph.A(graph.vertex_index[(cell, mode)], reference)
            output[(cell, mode)] = (xrow, zrow)
    return output


I2 = np.eye(2, dtype=complex)
X2 = np.asarray(((0, 1), (1, 0)), dtype=complex)
Y2 = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
Z2 = np.diag((1, -1)).astype(complex)
LOCAL_PAULIS = (I2, X2, Y2, Z2)


def tensor_little_endian(rows: Sequence[np.ndarray]) -> np.ndarray:
    result = np.asarray(((1.0 + 0.0j,),))
    for row in reversed(rows):
        result = np.kron(result, row)
    return result


def mapped_pauli(labels: Sequence[int], wires: Sequence[tuple[Coord, int]], pairs) -> Pauli:
    result = Pauli()
    for label, wire in zip(labels, wires):
        xrow, zrow = pairs[wire]
        if label == 1:
            result = result @ xrow
        elif label == 2:
            result = result @ (Pauli(1) @ xrow @ zrow)
        elif label == 3:
            result = result @ zrow
    return result


def map_local_matrix(unitary: np.ndarray, wires: Sequence[tuple[Coord, int]], pairs) -> Polynomial:
    arity = len(wires)
    dimension = 1 << arity
    if unitary.shape != (dimension, dimension):
        raise ValueError((unitary.shape, arity))
    rows = []
    for labels in product(range(4), repeat=arity):
        basis = tensor_little_endian(tuple(LOCAL_PAULIS[label] for label in labels))
        coefficient = np.trace(basis.conj().T @ unitary) / dimension
        if abs(coefficient) > 2e-13:
            rows.append((complex(coefficient), mapped_pauli(labels, wires, pairs)))
    return pauli_polynomial(rows)


FSWAP = np.asarray(
    ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
    dtype=complex,
)


def fswap_target(
    pair_a: tuple[Pauli, Pauli],
    pair_b: tuple[Pauli, Pauli],
    parity_pairs: Sequence[tuple[Pauli, Pauli]] = (),
) -> Polynomial:
    xa, za = pair_a
    xb, zb = pair_b
    ya = Pauli(1) @ xa @ za
    yb = Pauli(1) @ xb @ zb
    parity = pauli_product(pair[1] for pair in parity_pairs)
    return pauli_polynomial(
        (
            (0.5, za),
            (0.5, zb),
            (0.5, xa @ parity @ xb),
            (0.5, ya @ parity @ yb),
        )
    )


def onsite_fswap_rows(graph: OpenReferenceGraph, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    left, right = 2 * axis, 2 * axis + 1
    u = graph.vertex_index[(cell, left)]
    v = graph.vertex_index[(cell, right)]
    reference = graph.vertex_index[(cell, 6)]
    path = graph.path_A((u, reference, v))
    return (
        graph.B(u),
        graph.B(v),
        Pauli(3) @ graph.B(u) @ path,
        Pauli(1) @ graph.B(v) @ path,
    )


def seam_fswap_rows(graph: OpenReferenceGraph, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    target = list(cell)
    target[axis] += 1
    target_cell = tuple(target)
    u = graph.vertex_index[(cell, 2 * axis + 1)]
    v = graph.vertex_index[(target_cell, 2 * axis)]
    ru = graph.vertex_index[(cell, 6)]
    rv = graph.vertex_index[(target_cell, 6)]
    core = graph.A(u, v) @ graph.A(ru, rv)
    spectator = pauli_product(
        graph.B(graph.vertex_index[(target_cell, mode)])
        for mode in range(6)
        if mode != 2 * axis
    )
    return (
        graph.B(u),
        graph.B(v),
        Pauli(2) @ spectator @ core,
        spectator @ graph.B(u) @ graph.B(v) @ core,
    )


def fswap_poly(rows: Sequence[Pauli]) -> Polynomial:
    return pauli_polynomial((0.5, row) for row in rows)


def carrier_placement(graph: OpenReferenceGraph) -> dict[int, tuple[Coord, ...]]:
    """Independent spacing-16 18N+3E placement reconstruction."""
    output: dict[int, tuple[Coord, ...]] = {}
    for edge, (u, v, kind, owner) in enumerate(graph.edges):
        center = scale(16, owner)
        if kind == "octahedral":
            left, right = graph.vertices[u][1], graph.vertices[v][1]
            offset = scale(2, add(DIRECTIONS[left], DIRECTIONS[right]))
            sites = (add(center, offset),)
        elif kind == "spoke":
            left, right = graph.vertices[u][1], graph.vertices[v][1]
            mode = right if right != 6 else left
            sites = (add(center, scale(4, DIRECTIONS[mode])),)
        elif kind in ("matter_stream", "reference_bond"):
            left_cell = graph.vertices[u][0]
            right_cell = graph.vertices[v][0]
            delta = tuple(abs(left_cell[i] - right_cell[i]) for i in range(3))
            axis = delta.index(1)
            direction = tuple(int(i == axis) for i in range(3))
            if kind == "matter_stream":
                sites = (
                    add(center, scale(7, direction)),
                    add(center, scale(9, direction)),
                )
            else:
                sites = (add(center, scale(8, direction)),)
        else:
            raise AssertionError(kind)
        output[edge] = sites
    return output


def physical_index(site_map: dict[int, tuple[Coord, ...]]) -> tuple[tuple[Coord, ...], dict[Coord, int]]:
    sites = tuple(sorted(site for carriers in site_map.values() for site in carriers))
    return sites, {site: index for index, site in enumerate(sites)}


def lift_pauli(row: Pauli, site_map: dict[int, tuple[Coord, ...]], lookup: dict[Coord, int]) -> Pauli:
    """X repeats on both stream rails; Z selects the first rail."""
    x = z = 0
    for edge, carriers in site_map.items():
        if (row.x >> edge) & 1:
            for site in carriers:
                x ^= 1 << lookup[site]
        if (row.z >> edge) & 1:
            z ^= 1 << lookup[carriers[0]]
    return Pauli(row.phase, x, z)


def repetition_stabilizers(site_map, lookup) -> tuple[Pauli, ...]:
    return tuple(
        Pauli(z=(1 << lookup[carriers[0]]) | (1 << lookup[carriers[1]]))
        for carriers in site_map.values()
        if len(carriers) == 2
    )


def support_diameter(support: int, sites: Sequence[Coord]) -> int:
    selected = [sites[index] for index in range(len(sites)) if (support >> index) & 1]
    return max(
        (
            sum(abs(left[i] - right[i]) for i in range(3))
            for left in selected
            for right in selected
        ),
        default=0,
    )


def occupied(basis: int, modes: int) -> tuple[int, ...]:
    return tuple(index for index in range(modes) if (basis >> index) & 1)


def fock_lift(one_particle: np.ndarray) -> np.ndarray:
    modes = one_particle.shape[0]
    occupations = tuple(occupied(basis, modes) for basis in range(1 << modes))
    output = np.zeros((1 << modes, 1 << modes), dtype=complex)
    for target, target_modes in enumerate(occupations):
        for source, source_modes in enumerate(occupations):
            if len(target_modes) != len(source_modes):
                continue
            output[target, source] = (
                1.0
                if not target_modes
                else np.linalg.det(one_particle[np.ix_(target_modes, source_modes)])
            )
    return output


def fock_lift_restricted(one_particle: np.ndarray, basis: Sequence[int]) -> np.ndarray:
    modes = one_particle.shape[0]
    occupations = tuple(occupied(state, modes) for state in basis)
    output = np.zeros((len(basis), len(basis)), dtype=complex)
    for target, target_modes in enumerate(occupations):
        for source, source_modes in enumerate(occupations):
            if len(target_modes) != len(source_modes):
                continue
            output[target, source] = (
                1.0
                if not target_modes
                else np.linalg.det(one_particle[np.ix_(target_modes, source_modes)])
            )
    return output


def fock_two_mode(one_particle: np.ndarray) -> np.ndarray:
    if one_particle.shape != (2, 2):
        raise ValueError(one_particle.shape)
    return fock_lift(one_particle)


@dataclass(frozen=True)
class Gate:
    kind: str
    wires: tuple[int, ...]
    matrix: np.ndarray


def compile_adjacent_qr(unitary: np.ndarray) -> tuple[tuple[Gate, ...], float]:
    """Independent adjacent Givens reconstruction of the supplied 6x6 coin."""
    work = np.asarray(unitary, dtype=complex).copy()
    eliminations: list[tuple[int, int, np.ndarray]] = []
    for column in range(5):
        for lower in range(5, column, -1):
            upper = lower - 1
            a, b = work[upper, column], work[lower, column]
            if abs(b) < 1e-13:
                continue
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                (
                    (np.conj(a) / radius, np.conj(b) / radius),
                    (-b / radius, a / radius),
                ),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    schedule: list[Gate] = []
    for index, phase in enumerate(np.diag(work)):
        if abs(phase - 1) >= 1e-13:
            schedule.append(Gate("coin_phase", (index,), np.diag((1, phase)).astype(complex)))
    for upper, lower, elimination in reversed(eliminations):
        schedule.append(
            Gate("coin_givens", (upper, lower), fock_two_mode(elimination.conj().T))
        )
    return tuple(schedule), float(np.linalg.norm(work - np.diag(np.diag(work))))


def embed_gate(matrix: np.ndarray, wires: Sequence[int], count: int) -> np.ndarray:
    """Little-endian tensor embedding (valid here for adjacent local CAR gates)."""
    output = np.zeros((1 << count, 1 << count), dtype=complex)
    for source in range(1 << count):
        local_source = sum(((source >> wire) & 1) << index for index, wire in enumerate(wires))
        for local_target in range(1 << len(wires)):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) < 1e-15:
                continue
            target = source
            for index, wire in enumerate(wires):
                if (local_target >> index) & 1:
                    target |= 1 << wire
                else:
                    target &= ~(1 << wire)
            output[target, source] += amplitude
    return output


def apply_local_gate_restricted(
    matrix: np.ndarray, wires: Sequence[int], modes: int, basis: Sequence[int]
) -> np.ndarray:
    lookup = {state: index for index, state in enumerate(basis)}
    output = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, state in enumerate(basis):
        local_source = sum(((state >> wire) & 1) << index for index, wire in enumerate(wires))
        for local_target in range(1 << len(wires)):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) < 1e-15:
                continue
            target = state
            for index, wire in enumerate(wires):
                if (local_target >> index) & 1:
                    target |= 1 << wire
                else:
                    target &= ~(1 << wire)
            if target not in lookup:
                raise AssertionError(("number leakage", wires, state, target))
            output[lookup[target], column] += amplitude
    return output


def permutation_matrix(mapping: Sequence[int]) -> np.ndarray:
    output = np.zeros((len(mapping), len(mapping)), dtype=complex)
    for source, target in enumerate(mapping):
        output[target, source] = 1
    return output


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


def mode_map(frame: np.ndarray) -> tuple[int, ...]:
    result = []
    for direction in DIRECTIONS:
        target = tuple(int(value) for value in frame @ np.asarray(direction, dtype=int))
        result.append(DIRECTIONS.index(target))
    return tuple(result)


def fock_permutation_action(mapping: Sequence[int], state: int) -> tuple[int, int]:
    targets = [mapping[mode] for mode in range(len(mapping)) if (state >> mode) & 1]
    inversions = sum(
        targets[left] > targets[right]
        for left in range(len(targets))
        for right in range(left + 1, len(targets))
    )
    return sum(1 << mode for mode in targets), (-1 if inversions & 1 else 1)


def inverse_mapping(mapping: Sequence[int]) -> tuple[int, ...]:
    output = [0] * len(mapping)
    for source, target in enumerate(mapping):
        output[target] = source
    return tuple(output)


def matrix_word(gates: Sequence[Gate], modes: int) -> np.ndarray:
    result = np.eye(1 << modes, dtype=complex)
    for gate in gates:
        result = embed_gate(gate.matrix, gate.wires, modes) @ result
    return result


def polynomial_terms_commute(value: Polynomial, stabilizers: Sequence[Pauli]) -> int:
    failures = 0
    for x, z in value:
        row = Pauli(0, x, z)
        failures += sum(not row.commutes(stabilizer) for stabilizer in stabilizers)
    return failures


def polynomial_support(value: Polynomial) -> int:
    result = 0
    for x, z in value:
        result |= x | z
    return result


def jw_even_generators(mode_count: int, tree_pairs: Sequence[tuple[int, int]]):
    def local_operator(operators: dict[int, np.ndarray]) -> np.ndarray:
        result = np.asarray(((1.0 + 0.0j,),))
        for mode in reversed(range(mode_count)):
            result = np.kron(result, operators.get(mode, I2))
        return result

    bs = [local_operator({mode: Z2}) for mode in range(mode_count)]
    majoranas = []
    for mode in range(mode_count):
        operators = {lower: Z2 for lower in range(mode)}
        operators[mode] = X2
        majoranas.append(local_operator(operators))
    path_as = [-1j * majoranas[left] @ majoranas[right] for left, right in tree_pairs]
    return tuple(bs + path_as)


def normalized_even_bases(
    logical_generators: Sequence[np.ndarray], physical_generators: Sequence[Pauli]
) -> tuple[tuple[np.ndarray, ...], tuple[Pauli, ...]]:
    logical_basis = []
    physical_basis = []
    dimension = logical_generators[0].shape[0]
    for mask in range(1 << len(logical_generators)):
        logical = np.eye(dimension, dtype=complex)
        physical = Pauli()
        for index, (logical_generator, physical_generator) in enumerate(
            zip(logical_generators, physical_generators)
        ):
            if (mask >> index) & 1:
                logical = logical @ logical_generator
                physical = physical @ physical_generator
        if np.linalg.norm(logical - logical.conj().T) > TOL:
            logical = 1j * logical
            physical = Pauli(1) @ physical
        if np.linalg.norm(logical - logical.conj().T) > TOL or not physical.hermitian():
            raise AssertionError(("even basis normalization", mask, physical))
        logical_basis.append(logical)
        physical_basis.append(physical)
    return tuple(logical_basis), tuple(physical_basis)


def principal_hermitian_log(unitary: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eig(unitary)
    phases = -np.angle(values)
    result = vectors @ np.diag(phases) @ np.linalg.inv(vectors)
    return (result + result.conj().T) / 2


def target_style_log_extension_certificate(
    graph: OpenReferenceGraph,
    pairs,
    graph_stabilizers: Sequence[Pauli],
    reducer: SignedStabilizerReducer,
    coin_schedule: Sequence[Gate],
    contact: np.ndarray,
    site_map,
    lookup,
    repeat: Sequence[Pauli],
) -> dict[str, object]:
    """Reconstruct the joined scratch's exp(i mapped-Hermitian-log) factors."""
    entries: list[tuple[str, Coord, tuple[int, ...], np.ndarray]] = []
    for cell in graph.cells:
        for gate in coin_schedule:
            entries.append((gate.kind, cell, gate.wires, gate.matrix))
        for left, right in combinations(range(6), 2):
            entries.append(("contact_pair", cell, (left, right), contact))

    maximum_log_residual = 0.0
    maximum_code_target_residual = 0.0
    maximum_imaginary_coefficient = 0.0
    full_space_Hermitian_failures = 0
    physical_term_Hermitian_failures = 0
    constraint_commutator_failures = 0
    lifted_Hermitian_failures = 0
    repetition_commutator_failures = 0
    maximum_active_terms = 0
    total_active_terms = 0
    maximum_physical_support = 0
    maximum_physical_diameter = 0
    template_cache: dict[tuple[bytes, int], tuple[np.ndarray, tuple[np.ndarray, ...]]] = {}

    for kind, cell, modes, unitary in entries:
        vertices = tuple(graph.vertex_index[(cell, mode)] for mode in modes)
        if len(modes) == 1:
            paths: tuple[tuple[int, ...], ...] = ()
        elif REVERSE[modes[0]] == modes[1]:
            paths = ((vertices[0], graph.vertex_index[(cell, 6)], vertices[1]),)
        else:
            paths = ((vertices[0], vertices[1]),)
        local_tree_pairs = tuple(
            (vertices.index(path[0]), vertices.index(path[-1])) for path in paths
        )
        logical_generators = jw_even_generators(len(vertices), local_tree_pairs)
        physical_generators = tuple(
            [graph.B(vertex) for vertex in vertices]
            + [graph.path_A(path) for path in paths]
        )
        logical_basis, physical_basis = normalized_even_bases(
            logical_generators, physical_generators
        )
        cache_key = (np.round(unitary, 14).tobytes(), len(vertices))
        if cache_key in template_cache:
            hamiltonian, _cached_basis = template_cache[cache_key]
        else:
            hamiltonian = principal_hermitian_log(unitary)
            template_cache[cache_key] = (hamiltonian, logical_basis)
        coefficients = tuple(
            np.trace(row.conj().T @ hamiltonian) / unitary.shape[0]
            for row in logical_basis
        )
        rebuilt = sum(value * row for value, row in zip(coefficients, logical_basis))
        maximum_log_residual = max(
            maximum_log_residual, float(np.linalg.norm(rebuilt - hamiltonian))
        )
        active = tuple(
            (complex(value), row)
            for value, row in zip(coefficients, physical_basis)
            if abs(value) > 2e-13
        )
        physical_hamiltonian = pauli_polynomial(active)
        target_hamiltonian = map_local_matrix(
            hamiltonian, tuple((cell, mode) for mode in modes), pairs
        )
        maximum_code_target_residual = max(
            maximum_code_target_residual,
            poly_residual(
                reducer.polynomial(physical_hamiltonian),
                reducer.polynomial(target_hamiltonian),
            ),
        )
        maximum_imaginary_coefficient = max(
            maximum_imaginary_coefficient,
            max((abs(value.imag) for value, _row in active), default=0.0),
        )
        physical_term_Hermitian_failures += sum(not row.hermitian() for _value, row in active)
        full_space_Hermitian_failures += poly_hermiticity_residual(physical_hamiltonian) > TOL
        constraint_commutator_failures += polynomial_terms_commute(
            physical_hamiltonian, graph_stabilizers
        )
        lifted_hamiltonian = lift_polynomial(physical_hamiltonian, site_map, lookup)
        lifted_Hermitian_failures += poly_hermiticity_residual(lifted_hamiltonian) > TOL
        repetition_commutator_failures += polynomial_terms_commute(
            lifted_hamiltonian, repeat
        )
        support = polynomial_support(lifted_hamiltonian)
        maximum_physical_support = max(maximum_physical_support, support.bit_count())
        maximum_physical_diameter = max(
            maximum_physical_diameter,
            support_diameter(support, tuple(sorted(lookup, key=lookup.get))),
        )
        maximum_active_terms = max(maximum_active_terms, len(active))
        total_active_terms += len(active)

    return {
        "factors": len(entries),
        "coin_factors": len(graph.cells) * len(coin_schedule),
        "contact_factors": len(graph.cells) * 15,
        "active_Hermitian_Pauli_terms": total_active_terms,
        "maximum_active_terms_per_factor": maximum_active_terms,
        "maximum_log_expansion_residual": maximum_log_residual,
        "maximum_signed_code_target_residual": maximum_code_target_residual,
        "maximum_coefficient_imaginary_part": maximum_imaginary_coefficient,
        "physical_term_Hermitian_failures": physical_term_Hermitian_failures,
        "physical_Hamiltonian_full_space_Hermitian_failures": full_space_Hermitian_failures,
        "physical_exponential_full_space_unitarity_failures": full_space_Hermitian_failures,
        "constraint_commutator_failures": constraint_commutator_failures,
        "lifted_Hamiltonian_Hermitian_failures": lifted_Hermitian_failures,
        "repetition_commutator_failures": repetition_commutator_failures,
        "maximum_physical_generator_support": maximum_physical_support,
        "maximum_physical_generator_L1_diameter": maximum_physical_diameter,
        "unitarity_reason": "exp(-i H_phys) is unitary on the full carrier Hilbert space because H_phys=H_phys^dagger",
    }


@dataclass(frozen=True)
class PhysicalFactor:
    stage: str
    kind: str
    owner: Coord
    key: tuple[object, ...]
    logical_wires: tuple[tuple[Coord, int], ...]
    polynomial: Polynomial
    fswap_rows: tuple[Pauli, ...] = ()


def build_ordered_factors(
    graph: OpenReferenceGraph,
    pairs: dict[tuple[Coord, int], tuple[Pauli, Pauli]],
    coin_schedule: Sequence[Gate],
    contact: np.ndarray,
) -> dict[str, tuple[PhysicalFactor, ...]]:
    stages: dict[str, list[PhysicalFactor]] = {
        "coin": [],
        "reverse": [],
        "seam": [],
        "contact": [],
    }
    for cell in graph.cells:
        for index, gate in enumerate(coin_schedule):
            wires = tuple((cell, mode) for mode in gate.wires)
            stages["coin"].append(
                PhysicalFactor(
                    "coin",
                    gate.kind,
                    cell,
                    ("coin", index, gate.kind, gate.wires),
                    wires,
                    map_local_matrix(gate.matrix, wires, pairs),
                )
            )
    for cell in graph.cells:
        for axis in range(3):
            rows = onsite_fswap_rows(graph, cell, axis)
            wires = ((cell, 2 * axis), (cell, 2 * axis + 1))
            stages["reverse"].append(
                PhysicalFactor(
                    "reverse",
                    "reverse_fswap",
                    cell,
                    ("reverse", axis),
                    wires,
                    fswap_poly(rows),
                    rows,
                )
            )
    for cell in graph.cells:
        for axis in range(3):
            target = list(cell)
            target[axis] += 1
            target_cell = tuple(target)
            if target_cell not in graph.cell_set:
                continue
            rows = seam_fswap_rows(graph, cell, axis)
            wires = ((cell, 2 * axis + 1), (target_cell, 2 * axis))
            stages["seam"].append(
                PhysicalFactor(
                    "seam",
                    "seam_fswap",
                    cell,
                    ("seam", axis, target_cell),
                    wires,
                    fswap_poly(rows),
                    rows,
                )
            )
    for cell in graph.cells:
        for index, (left, right) in enumerate(combinations(range(6), 2)):
            wires = ((cell, left), (cell, right))
            stages["contact"].append(
                PhysicalFactor(
                    "contact",
                    "contact_pair",
                    cell,
                    ("contact", index, left, right),
                    wires,
                    map_local_matrix(contact, wires, pairs),
                )
            )
    return {key: tuple(value) for key, value in stages.items()}


def canonical_factor_word(stages: dict[str, tuple[PhysicalFactor, ...]]) -> tuple[PhysicalFactor, ...]:
    # A list is applied left-to-right, so the resulting operator is
    # contact * seam * reverse * coin.
    return stages["coin"] + stages["reverse"] + stages["seam"] + stages["contact"]


def target_enumeration_word(stages: dict[str, tuple[PhysicalFactor, ...]], cells: Sequence[Coord]):
    """Reproduce only the joined scratch's emitted ordering, without importing it."""
    output: list[PhysicalFactor] = []
    for cell in cells:
        output.extend(row for row in stages["coin"] if row.owner == cell)
        output.extend(row for row in stages["reverse"] if row.owner == cell)
        output.extend(row for row in stages["contact"] if row.owner == cell)
    output.extend(stages["seam"])
    return tuple(output)


def check_logical_chart(graph: OpenReferenceGraph, pairs, stabilizers) -> dict[str, object]:
    ordered = tuple((cell, mode) for cell in graph.cells for mode in range(6))
    pair_failures = stabilizer_failures = hermitian_failures = 0
    for index, key in enumerate(ordered):
        xrow, zrow = pairs[key]
        hermitian_failures += not xrow.hermitian()
        hermitian_failures += not zrow.hermitian()
        hermitian_failures += (xrow @ xrow) != Pauli()
        hermitian_failures += (zrow @ zrow) != Pauli()
        for other_index, other in enumerate(ordered):
            ox, oz = pairs[other]
            pair_failures += xrow.commutes(oz) != (index != other_index)
            pair_failures += not xrow.commutes(ox)
            pair_failures += not zrow.commutes(oz)
        for stabilizer in stabilizers:
            stabilizer_failures += not xrow.commutes(stabilizer)
            stabilizer_failures += not zrow.commutes(stabilizer)
    return {
        "logical_qubits": len(ordered),
        "canonical_pair_failures": pair_failures,
        "stabilizer_commutator_failures": stabilizer_failures,
        "Hermitian_involution_failures": hermitian_failures,
        "maximum_X_weight": max(pairs[key][0].weight() for key in ordered),
        "maximum_Z_weight": max(pairs[key][1].weight() for key in ordered),
    }


def check_fswaps(
    graph: OpenReferenceGraph,
    factors: Sequence[PhysicalFactor],
    pairs,
    stabilizers,
    reducer: SignedStabilizerReducer | None = None,
) -> dict[str, object]:
    full_hermitian_failures = full_involution_failures = row_hermitian_failures = 0
    constraint_failures = target_failures = deletion_failures = 0
    target_checks = 0
    weights: list[int] = []
    maximum_target_residual = 0.0
    ordered_wires = tuple((cell, mode) for cell in graph.cells for mode in range(6))
    wire_index = {wire: index for index, wire in enumerate(ordered_wires)}
    for factor in factors:
        value = factor.polynomial
        full_hermitian_failures += poly_hermiticity_residual(value) > TOL
        full_involution_failures += poly_involution_residual(value) > TOL
        row_hermitian_failures += sum(not row.hermitian() for row in factor.fswap_rows)
        constraint_failures += polynomial_terms_commute(value, stabilizers)
        weights.extend(row.weight() for row in factor.fswap_rows)
        if reducer is not None:
            target_checks += 1
            first = wire_index[factor.logical_wires[0]]
            second = wire_index[factor.logical_wires[1]]
            low, high = sorted((first, second))
            parity_pairs = tuple(pairs[ordered_wires[index]] for index in range(low + 1, high))
            target = fswap_target(
                pairs[factor.logical_wires[0]],
                pairs[factor.logical_wires[1]],
                parity_pairs,
            )
            residual = poly_residual(
                reducer.polynomial(value), reducer.polynomial(target)
            )
            maximum_target_residual = max(maximum_target_residual, residual)
            target_failures += residual > TOL
        for deleted in range(4):
            shortened = fswap_poly(
                tuple(row for index, row in enumerate(factor.fswap_rows) if index != deleted)
            )
            deletion_failures += poly_unitarity_residual(shortened) <= TOL
    return {
        "factors": len(factors),
        "terms": 4 * len(factors),
        "row_Hermitian_failures": row_hermitian_failures,
        "full_space_Hermitian_failures": full_hermitian_failures,
        "full_space_involution_failures": full_involution_failures,
        "constraint_commutator_failures": constraint_failures,
        "exact_code_target_checks": target_checks,
        "exact_code_target_failures": target_failures,
        "maximum_code_target_residual": maximum_target_residual,
        "term_deletions_not_detected": deletion_failures,
        "minimum_term_weight": min(weights, default=0),
        "maximum_term_weight": max(weights, default=0),
    }


def lift_polynomial(value: Polynomial, site_map, lookup) -> Polynomial:
    output: dict[tuple[int, int], complex] = defaultdict(complex)
    for (x, z), coefficient in value.items():
        row = lift_pauli(Pauli(0, x, z), site_map, lookup)
        output[(row.x, row.z)] += coefficient
    return clean_poly(output)


def fixture_certificate(
    shape: tuple[int, int, int],
    coin_schedule: Sequence[Gate],
    contact: np.ndarray,
) -> tuple[dict[str, object], dict[str, object]]:
    graph = OpenReferenceGraph(box(shape))
    graph_stabilizers = constraints(graph)
    pairs = logical_pairs(graph)
    reducer = SignedStabilizerReducer(graph_stabilizers, len(graph.edges))
    stages = build_ordered_factors(graph, pairs, coin_schedule, contact)
    word = canonical_factor_word(stages)
    site_map = carrier_placement(graph)
    sites, lookup = physical_index(site_map)
    repeat = repetition_stabilizers(site_map, lookup)
    lifted_constraints = tuple(lift_pauli(row, site_map, lookup) for row in graph_stabilizers) + repeat

    collisions = len(sites) - len(set(sites))
    if collisions:
        raise AssertionError(("placement collisions", shape, collisions))

    factor_constraint_failures = 0
    factor_full_unitarity_failures = 0
    lifted_unitarity_failures = 0
    repetition_commutator_failures = 0
    homomorphism_failures = 0
    maximum_physical_factor_weight = 0
    maximum_physical_factor_diameter = 0
    physical_supports: list[tuple[PhysicalFactor, int]] = []
    for factor in word:
        factor_constraint_failures += polynomial_terms_commute(
            factor.polynomial, graph_stabilizers
        )
        factor_full_unitarity_failures += poly_unitarity_residual(factor.polynomial) > TOL
        lifted = lift_polynomial(factor.polynomial, site_map, lookup)
        lifted_unitarity_failures += poly_unitarity_residual(lifted) > TOL
        repetition_commutator_failures += polynomial_terms_commute(lifted, repeat)
        support = polynomial_support(lifted)
        physical_supports.append((factor, support))
        maximum_physical_factor_weight = max(
            maximum_physical_factor_weight, support.bit_count()
        )
        maximum_physical_factor_diameter = max(
            maximum_physical_factor_diameter, support_diameter(support, sites)
        )
        terms = tuple(Pauli(0, x, z) for x, z in factor.polynomial)
        for left in terms:
            for right in terms:
                homomorphism_failures += (
                    lift_pauli(left @ right, site_map, lookup)
                    != lift_pauli(left, site_map, lookup) @ lift_pauli(right, site_map, lookup)
                )

    # Shared-register evidence: seams and onsite factors are not detached copies.
    onsite_support = [
        support
        for factor, support in physical_supports
        if factor.stage in ("coin", "reverse", "contact")
    ]
    seam_support = [support for factor, support in physical_supports if factor.stage == "seam"]
    seam_onsite_overlaps = sum(bool(left & right) for left in seam_support for right in onsite_support)
    seam_seam_overlaps = sum(
        bool(seam_support[left] & seam_support[right])
        for left in range(len(seam_support))
        for right in range(left)
    )
    endpoint_reuse_failures = 0
    for factor in stages["seam"]:
        for wire in factor.logical_wires:
            endpoint_reuse_failures += wire not in pairs
            endpoint_reuse_failures += pairs.get(wire) != logical_pairs(graph).get(wire)

    stage_counts = {stage: len(rows) for stage, rows in stages.items()}
    kind_counts = Counter(factor.kind for factor in word)
    fswap_rows = stages["reverse"] + stages["seam"]
    fswap = check_fswaps(
        graph,
        fswap_rows,
        pairs,
        graph_stabilizers,
        None,
    )
    fswap["exact_code_target_scope"] = (
        "exercised on the independent two-cell complete graph; larger fixtures "
        "check full-space polynomial algebra and common-code preservation"
    )
    chart = check_logical_chart(graph, pairs, graph_stabilizers)
    target_style_log_extension = target_style_log_extension_certificate(
        graph,
        pairs,
        graph_stabilizers,
        reducer,
        coin_schedule,
        contact,
        site_map,
        lookup,
        repeat,
    )
    physical_rank = gf2_rank(
        row.symplectic(len(sites)) for row in lifted_constraints
    )
    abstract_rank = reducer.rank
    expected_abstract_edges = 18 * len(graph.cells) + 2 * graph.coarse_edges
    expected_physical = 18 * len(graph.cells) + 3 * graph.coarse_edges

    row = {
        "shape": shape,
        "cells": len(graph.cells),
        "coarse_edges": graph.coarse_edges,
        "abstract_graph_edges": len(graph.edges),
        "expected_18N_plus_2E": expected_abstract_edges,
        "physical_carriers": len(sites),
        "expected_18N_plus_3E": expected_physical,
        "matter_stream_repetition_checks": len(repeat),
        "placement_collisions": collisions,
        "constraint_rows_supplied": len(graph_stabilizers),
        "abstract_constraint_rank": abstract_rank,
        "physical_constraint_rank": physical_rank,
        "abstract_logical_qubits_from_rank": len(graph.edges) - abstract_rank,
        "physical_logical_qubits_from_rank": len(sites) - physical_rank,
        "stage_counts": stage_counts,
        "factor_kind_counts": dict(kind_counts),
        "ordered_factor_count": len(word),
        "factor_full_space_unitarity_failures": factor_full_unitarity_failures,
        "factor_constraint_commutator_failures": factor_constraint_failures,
        "lifted_factor_full_space_unitarity_failures": lifted_unitarity_failures,
        "repetition_commutator_failures": repetition_commutator_failures,
        "repetition_lift_homomorphism_failures": homomorphism_failures,
        "maximum_physical_factor_weight": maximum_physical_factor_weight,
        "maximum_physical_factor_L1_diameter": maximum_physical_factor_diameter,
        "analytic_physical_weight_cap": 72,
        "analytic_physical_L1_diameter_cap": 70,
        "bounded_support_argument": (
            "A factor touches at most two adjacent cell-stars. Each cell-star "
            "has at most 18 onsite carriers plus six incident (two-rail matter "
            "+ one-rail reference) bond triples, hence <=36 carriers and <=72 "
            "for two stars. All incident carriers lie within L-infinity 9 of "
            "their spacing-16 cell center, giving L1 diameter <=16+6*9=70."
        ),
        "seam_onsite_shared_register_overlaps": seam_onsite_overlaps,
        "seam_seam_shared_register_overlaps": seam_seam_overlaps,
        "seam_endpoint_reuse_failures": endpoint_reuse_failures,
        "logical_chart": chart,
        "fswap": fswap,
        "target_style_coin_contact_log_extension": target_style_log_extension,
        "leakage": {
            "direct_factor_graph_code_leakage_failures": factor_constraint_failures,
            "target_style_log_graph_code_leakage_failures": target_style_log_extension[
                "constraint_commutator_failures"
            ],
            "repetition_code_leakage_failures": repetition_commutator_failures,
            "common_physical_code_logical_qubits": len(sites) - physical_rank,
        },
    }
    context = {
        "graph": graph,
        "stabilizers": graph_stabilizers,
        "pairs": pairs,
        "reducer": reducer,
        "stages": stages,
        "word": word,
        "site_map": site_map,
        "sites": sites,
        "lookup": lookup,
        "repeat": repeat,
    }
    return row, context


def logical_fswap_polynomial(first: int, second: int) -> Polynomial:
    low, high = sorted((first, second))
    x = (1 << first) | (1 << second)
    between = sum(1 << mode for mode in range(low + 1, high))
    endpoints = (1 << first) | (1 << second)
    return {
        (0, 1 << first): 0.5 + 0.0j,
        (0, 1 << second): 0.5 + 0.0j,
        (x, between): 0.5 + 0.0j,
        (x, between | endpoints): -0.5 + 0.0j,
    }


def apply_poly_column(value: Polynomial, source: int) -> dict[int, complex]:
    output: dict[int, complex] = defaultdict(complex)
    for (x, z), coefficient in value.items():
        sign = -1 if ((z & source).bit_count() & 1) else 1
        output[source ^ x] += coefficient * sign
    return clean_poly(output)  # type: ignore[arg-type, return-value]


def exact_fswap_truth_table() -> dict[str, object]:
    first, second = 1, 6
    value = logical_fswap_polynomial(first, second)
    failures = 0
    maximum_residual = 0.0
    for source in range(1 << 12):
        permutation = list(range(12))
        permutation[first], permutation[second] = second, first
        source_occupied = [mode for mode in range(12) if (source >> mode) & 1]
        target_occupied = [permutation[mode] for mode in source_occupied]
        inversions = sum(
            target_occupied[left] > target_occupied[right]
            for left in range(len(target_occupied))
            for right in range(left + 1, len(target_occupied))
        )
        target = sum(1 << mode for mode in target_occupied)
        expected = -1.0 if inversions & 1 else 1.0
        column = apply_poly_column(value, source)
        residual = math.sqrt(
            sum(
                abs(column.get(key, 0) - (expected if key == target else 0)) ** 2
                for key in set(column) | {target}
            )
        )
        maximum_residual = max(maximum_residual, residual)
        failures += residual > 1e-12
    return {
        "logical_columns_checked": 1 << 12,
        "truth_table_failures": failures,
        "maximum_column_residual": maximum_residual,
        "modes_swapped": (first, second),
        "double_occupation_phase": -1,
    }


def seam_dressing_deletion_certificate() -> dict[str, object]:
    cells = ((0, 0, 0), (1, 0, 0))
    graph = OpenReferenceGraph(cells)
    stabilizers = constraints(graph)
    reducer = SignedStabilizerReducer(stabilizers, len(graph.edges))
    pairs = logical_pairs(graph)
    cell, target_cell, axis = cells[0], cells[1], 0
    u = graph.vertex_index[(cell, 1)]
    v = graph.vertex_index[(target_cell, 0)]
    ru = graph.vertex_index[(cell, 6)]
    rv = graph.vertex_index[(target_cell, 6)]
    matter_A = graph.A(u, v)
    reference_A = graph.A(ru, rv)
    core = matter_A @ reference_A
    spectator = pauli_product(
        graph.B(graph.vertex_index[(target_cell, mode)]) for mode in range(1, 6)
    )
    bu, bv = graph.B(u), graph.B(v)
    target = fswap_target(
        pairs[(cell, 1)],
        pairs[(target_cell, 0)],
        tuple(pairs[(cell, mode)] for mode in range(2, 6)),
    )
    good_rows = (bu, bv, Pauli(2) @ spectator @ core, spectator @ bu @ bv @ core)
    alternatives = {
        "omit_spectator": (bu, bv, Pauli(2) @ core, bu @ bv @ core),
        "omit_reference_A": (
            bu,
            bv,
            Pauli(2) @ spectator @ matter_A,
            spectator @ bu @ bv @ matter_A,
        ),
    }
    result = {
        "good_code_residual": poly_residual(
            reducer.polynomial(fswap_poly(good_rows)), reducer.polynomial(target)
        ),
        "good_constraint_commutator_failures": polynomial_terms_commute(
            fswap_poly(good_rows), stabilizers
        ),
        "term_deletions": [],
        "dressing_deletions": {},
    }
    for deleted in range(4):
        value = fswap_poly(tuple(row for index, row in enumerate(good_rows) if index != deleted))
        result["term_deletions"].append(
            {
                "deleted_term": deleted,
                "code_target_residual": poly_residual(
                    reducer.polynomial(value), reducer.polynomial(target)
                ),
                "full_space_unitarity_residual": poly_unitarity_residual(value),
            }
        )
    for name, rows in alternatives.items():
        value = fswap_poly(rows)
        result["dressing_deletions"][name] = {
            "code_target_residual": poly_residual(
                reducer.polynomial(value), reducer.polynomial(target)
            ),
            "constraint_commutator_failures": polynomial_terms_commute(value, stabilizers),
            "full_space_involution_residual": poly_involution_residual(value),
        }
    return result


def coin_contact_certificate(c219, c230) -> tuple[dict[str, object], tuple[Gate, ...], np.ndarray]:
    species = c219.common_species(c230.BETA)
    coin = np.asarray(species.coin, dtype=complex)
    schedule, qr_triangular_residual = compile_adjacent_qr(coin)
    coin_word = matrix_word(schedule, 6)
    coin_target = fock_lift(coin)
    schedule_deletions = []
    for deleted in range(len(schedule)):
        shortened = tuple(gate for index, gate in enumerate(schedule) if index != deleted)
        schedule_deletions.append(float(np.linalg.norm(matrix_word(shortened, 6) - coin_target)))

    contact = np.diag((1, 1, 1, np.exp(1j * c230.COUPLING))).astype(complex)
    contact_gates = tuple(
        Gate("contact_pair", (left, right), contact)
        for left, right in combinations(range(6), 2)
    )
    contact_word = matrix_word(contact_gates, 6)
    contact_target_diagonal = np.asarray(
        [
            np.exp(1j * c230.COUPLING * (state.bit_count() * (state.bit_count() - 1) // 2))
            for state in range(1 << 6)
        ],
        dtype=complex,
    )
    contact_target = np.diag(contact_target_diagonal)
    contact_deletions = []
    for deleted in range(len(contact_gates)):
        shortened = tuple(gate for index, gate in enumerate(contact_gates) if index != deleted)
        contact_deletions.append(float(np.linalg.norm(matrix_word(shortened, 6) - contact_target)))

    uniform = np.ones(6, dtype=complex) / math.sqrt(6)
    scalar_eigenvalue = complex(np.vdot(uniform, coin @ uniform))
    measured_mass = float(np.angle(scalar_eigenvalue)) / c219.C_SQUARED
    imported_cycle230_coin_residual = float(
        np.linalg.norm(coin - c230.c219.common_species(c230.BETA).coin)
    )
    result = {
        "Cycle219_beta_from_Cycle230": c230.BETA,
        "Cycle230_contact_coupling": c230.COUPLING,
        "coin_one_particle_unitarity_residual": float(
            np.linalg.norm(coin.conj().T @ coin - np.eye(6))
        ),
        "coin_QR_triangular_residual": qr_triangular_residual,
        "coin_schedule_factor_counts": dict(Counter(gate.kind for gate in schedule)),
        "coin_schedule_factors": len(schedule),
        "coin_Fock_target_residual": float(np.linalg.norm(coin_word - coin_target)),
        "coin_factor_unitarity_maximum_residual": max(
            float(np.linalg.norm(gate.matrix.conj().T @ gate.matrix - np.eye(gate.matrix.shape[0])))
            for gate in schedule
        ),
        "coin_factor_deletion_minimum_target_residual": min(schedule_deletions),
        "coin_factor_deletions_checked": len(schedule_deletions),
        "Cycle219_analytic_mass": species.analytic_mass,
        "Cycle219_rest_mass": c219.rest_mass(species),
        "independent_scalar_phase_mass": measured_mass,
        "mass_pairwise_maximum_residual": max(
            abs(species.analytic_mass - c219.rest_mass(species)),
            abs(species.analytic_mass - measured_mass),
        ),
        "Cycle230_imported_Cycle219_coin_residual": imported_cycle230_coin_residual,
        "contact_pair_factors": len(contact_gates),
        "contact_pair_unitarity_residual": float(
            np.linalg.norm(contact.conj().T @ contact - np.eye(4))
        ),
        "contact_full_onsite_target_residual": float(
            np.linalg.norm(contact_word - contact_target)
        ),
        "contact_factor_deletion_minimum_target_residual": min(contact_deletions),
        "contact_factor_deletions_checked": len(contact_deletions),
        "contact_vacuum_phase_residual": abs(contact_target_diagonal[0] - 1),
        "contact_one_particle_phase_maximum_residual": max(
            abs(contact_target_diagonal[1 << mode] - 1) for mode in range(6)
        ),
        "contact_two_particle_phase_maximum_residual": max(
            abs(contact_target_diagonal[(1 << left) | (1 << right)] - np.exp(1j * c230.COUPLING))
            for left, right in combinations(range(6), 2)
        ),
    }
    return result, schedule, contact


def two_cell_order_certificate(
    coin: np.ndarray,
    schedule: Sequence[Gate],
    contact: np.ndarray,
    target_stage_runs: Sequence[str],
) -> dict[str, object]:
    modes = 12
    basis = tuple(state for state in range(1 << modes) if state.bit_count() <= 2)
    identity = np.eye(len(basis), dtype=complex)

    block_coin = np.zeros((modes, modes), dtype=complex)
    block_coin[:6, :6] = coin
    block_coin[6:, 6:] = coin
    direct_coin = fock_lift_restricted(block_coin, basis)

    reverse_mapping = list(range(modes))
    for offset in (0, 6):
        for left, right in REVERSE_PAIRS:
            reverse_mapping[offset + left], reverse_mapping[offset + right] = (
                reverse_mapping[offset + right],
                reverse_mapping[offset + left],
            )
    direct_reverse = fock_lift_restricted(permutation_matrix(reverse_mapping), basis)
    seam_mapping = list(range(modes))
    seam_mapping[1], seam_mapping[6] = seam_mapping[6], seam_mapping[1]
    direct_seam = fock_lift_restricted(permutation_matrix(seam_mapping), basis)

    contact_diagonal = []
    for state in basis:
        n0 = (state & 0b111111).bit_count()
        n1 = (state >> 6).bit_count()
        contact_diagonal.append(
            np.exp(
                1j
                * float(np.angle(contact[3, 3]))
                * (n0 * (n0 - 1) + n1 * (n1 - 1))
                / 2
            )
        )
    direct_contact = np.diag(contact_diagonal)
    direct_update = direct_contact @ direct_seam @ direct_reverse @ direct_coin

    coin_factors = []
    for offset in (0, 6):
        for gate in schedule:
            coin_factors.append(
                apply_local_gate_restricted(
                    gate.matrix, tuple(offset + wire for wire in gate.wires), modes, basis
                )
            )
    reverse_factors = []
    for offset in (0, 6):
        for left, right in REVERSE_PAIRS:
            reverse_factors.append(
                apply_local_gate_restricted(FSWAP, (offset + left, offset + right), modes, basis)
            )
    contact_factors = []
    for offset in (0, 6):
        for left, right in combinations(range(6), 2):
            contact_factors.append(
                apply_local_gate_restricted(contact, (offset + left, offset + right), modes, basis)
            )

    factors_by_stage = {
        "coin": coin_factors,
        "reverse": reverse_factors,
        "seam": [direct_seam],
        "contact": contact_factors,
    }
    canonical_order = ("coin", "reverse", "seam", "contact")
    canonical = identity
    for stage in canonical_order:
        for factor in factors_by_stage[stage]:
            canonical = factor @ canonical

    # Counterfactual/order-deletion attack: contacts before the seam.  An early
    # scratch revision had this enumeration; the current pinned target does not.
    contact_before_seam = identity
    cursor_coin = cursor_reverse = cursor_contact = 0
    for _cell in range(2):
        for _ in schedule:
            contact_before_seam = coin_factors[cursor_coin] @ contact_before_seam
            cursor_coin += 1
        for _ in REVERSE_PAIRS:
            contact_before_seam = reverse_factors[cursor_reverse] @ contact_before_seam
            cursor_reverse += 1
        for _ in combinations(range(6), 2):
            contact_before_seam = contact_factors[cursor_contact] @ contact_before_seam
            cursor_contact += 1
    contact_before_seam = direct_seam @ contact_before_seam
    target_name_map = {
        "onsite_coin_mass": "coin",
        "onsite_reverse_fswap": "reverse",
        "directed_seam_fswap": "seam",
        "onsite_contact": "contact",
    }
    normalized_target_runs = tuple(
        target_name_map.get(name, f"unknown:{name}") for name in target_stage_runs
    )
    current_target_word = identity
    unknown_target_stages = sum(stage not in factors_by_stage for stage in normalized_target_runs)
    if not unknown_target_stages:
        for stage in normalized_target_runs:
            for factor in factors_by_stage[stage]:
                current_target_word = factor @ current_target_word
    current_residual = float(np.linalg.norm(current_target_word - direct_update))
    target_current_order_is_canonical = normalized_target_runs == canonical_order

    return {
        "logical_modes": modes,
        "number_sector_cutoff": 2,
        "exact_basis_dimension": len(basis),
        "canonical_stage_order": canonical_order,
        "canonical_operator_order": "contact @ seam @ reverse @ coin",
        "canonical_factor_count": len(coin_factors) + len(reverse_factors) + 1 + len(contact_factors),
        "canonical_word_target_residual": float(np.linalg.norm(canonical - direct_update)),
        "canonical_word_unitarity_residual": float(
            np.linalg.norm(canonical.conj().T @ canonical - identity)
        ),
        "target_emitted_stage_runs": tuple(target_stage_runs),
        "target_emitted_stage_runs_normalized": normalized_target_runs,
        "target_unknown_stage_names": unknown_target_stages,
        "target_emitted_order_target_residual": current_residual,
        "contact_seam_commutator_norm": float(
            np.linalg.norm(direct_contact @ direct_seam - direct_seam @ direct_contact)
        ),
        "contact_before_seam_counterfactual_target_residual": float(
            np.linalg.norm(contact_before_seam - direct_update)
        ),
        "maximum_contact_before_seam_entry_residual": float(
            np.max(np.abs(contact_before_seam - direct_update))
        ),
        "joined_scratch_checks_factor_stage_order": target_current_order_is_canonical,
        "independent_runner_composes_extracted_target_stage_word": (
            unknown_target_stages == 0 and current_residual <= TOL
        ),
    }


def covariance_certificate(coin: np.ndarray, coupling: float) -> dict[str, object]:
    frames = proper_cubic_frames()
    gammas: dict[tuple[int, ...], np.ndarray] = {}
    permutations_by_map: dict[tuple[int, ...], np.ndarray] = {}
    for frame in frames:
        mapping = mode_map(frame)
        one = permutation_matrix(mapping)
        permutations_by_map[mapping] = one
        gammas[mapping] = fock_lift(one)

    gamma_coin = fock_lift(coin)
    contact_diag = np.asarray(
        [
            np.exp(1j * coupling * (state.bit_count() * (state.bit_count() - 1) // 2))
            for state in range(1 << 6)
        ]
    )
    contact = np.diag(contact_diag)
    reverse_one = permutation_matrix(REVERSE)
    gamma_reverse = fock_lift(reverse_one)

    one_particle_coin_max = fock_coin_max = contact_max = reverse_max = 0.0
    signed_pair_max = 0.0
    family_failures = 0
    seam_endpoint_failures = 0
    frame_rows = []
    for frame in frames:
        mapping = mode_map(frame)
        one = permutations_by_map[mapping]
        gamma = gammas[mapping]
        one_particle_coin_max = max(
            one_particle_coin_max,
            float(np.linalg.norm(one @ coin @ one.conj().T - coin)),
        )
        fock_coin_max = max(
            fock_coin_max,
            float(np.linalg.norm(gamma @ gamma_coin @ gamma.conj().T - gamma_coin)),
        )
        contact_max = max(
            contact_max,
            float(np.linalg.norm(gamma @ contact @ gamma.conj().T - contact)),
        )
        reverse_max = max(
            reverse_max,
            float(np.linalg.norm(gamma @ gamma_reverse @ gamma.conj().T - gamma_reverse)),
        )
        mapped_reverse_pairs = {
            tuple(sorted((mapping[left], mapping[right]))) for left, right in REVERSE_PAIRS
        }
        family_failures += mapped_reverse_pairs != set(REVERSE_PAIRS)
        mapped_contacts = {
            tuple(sorted((mapping[left], mapping[right])))
            for left, right in combinations(range(6), 2)
        }
        family_failures += mapped_contacts != set(combinations(range(6), 2))

        for left, right in REVERSE_PAIRS:
            source_map = list(range(6))
            source_map[left], source_map[right] = source_map[right], source_map[left]
            target_left, target_right = mapping[left], mapping[right]
            target_map = list(range(6))
            target_map[target_left], target_map[target_right] = (
                target_map[target_right],
                target_map[target_left],
            )
            signed_pair_max = max(
                signed_pair_max,
                float(
                    np.linalg.norm(
                        gamma
                        @ fock_lift(permutation_matrix(source_map))
                        @ gamma.conj().T
                        - fock_lift(permutation_matrix(target_map))
                    )
                ),
            )

        # A positive-axis seam has source port -d and target port +d.
        endpoint_checks = 0
        for axis in range(3):
            displacement = DIRECTIONS[2 * axis]
            transformed = tuple(
                int(value) for value in frame @ np.asarray(displacement, dtype=int)
            )
            mapped_source = mapping[2 * axis + 1]
            mapped_target = mapping[2 * axis]
            endpoint_checks += DIRECTIONS[mapped_source] != tuple(-value for value in transformed)
            endpoint_checks += DIRECTIONS[mapped_target] != transformed
        seam_endpoint_failures += endpoint_checks
        frame_rows.append(
            {
                "mode_map": mapping,
                "fixed_plus_x_reverses_canonical_owner": DIRECTIONS[mapping[0]] in (
                    (-1, 0, 0),
                    (0, -1, 0),
                    (0, 0, -1),
                ),
            }
        )

    composition_failures = 0
    maximum_signed_composition_residual = 0.0
    maximum_one_particle_composition_residual = 0.0
    for left in frames:
        left_map = mode_map(left)
        left_one = permutations_by_map[left_map]
        left_gamma = gammas[left_map]
        for right in frames:
            right_map = mode_map(right)
            right_one = permutations_by_map[right_map]
            right_gamma = gammas[right_map]
            target_map = mode_map(left @ right)
            target_one = permutations_by_map[target_map]
            target_gamma = gammas[target_map]
            one_residual = float(np.linalg.norm(left_one @ right_one - target_one))
            signed_residual = float(np.linalg.norm(left_gamma @ right_gamma - target_gamma))
            maximum_one_particle_composition_residual = max(
                maximum_one_particle_composition_residual, one_residual
            )
            maximum_signed_composition_residual = max(
                maximum_signed_composition_residual, signed_residual
            )
            composition_failures += one_residual > TOL or signed_residual > TOL

    # Signed two-cell seam covariance, including the canonical-owner swap when
    # a frame reverses the oriented coarse edge.  This exhausts every logical
    # column without constructing a 4096-by-4096 dense matrix.
    signed_seam_columns = 0
    signed_seam_failures = 0
    signed_seam_endpoint_failures = 0
    for axis in range(3):
        source_endpoint = 2 * axis + 1
        target_endpoint = 6 + 2 * axis
        source_transposition = list(range(12))
        source_transposition[source_endpoint], source_transposition[target_endpoint] = (
            source_transposition[target_endpoint],
            source_transposition[source_endpoint],
        )
        for frame in frames:
            local_map = mode_map(frame)
            transformed_direction = tuple(
                int(value)
                for value in frame @ np.asarray(DIRECTIONS[2 * axis], dtype=int)
            )
            transformed_direction_index = DIRECTIONS.index(transformed_direction)
            target_axis = transformed_direction_index // 2
            reverses_owner = transformed_direction_index & 1
            cell_map = (1, 0) if reverses_owner else (0, 1)
            global_map = tuple(
                6 * cell_map[cell] + local_map[mode]
                for cell in range(2)
                for mode in range(6)
            )
            inverse_global = inverse_mapping(global_map)
            mapped_endpoints = {
                global_map[source_endpoint], global_map[target_endpoint]
            }
            canonical_endpoints = {2 * target_axis + 1, 6 + 2 * target_axis}
            signed_seam_endpoint_failures += mapped_endpoints != canonical_endpoints
            target_transposition = list(range(12))
            left, right = tuple(canonical_endpoints)
            target_transposition[left], target_transposition[right] = (
                target_transposition[right],
                target_transposition[left],
            )
            for state in range(1 << 12):
                intermediate, phase0 = fock_permutation_action(inverse_global, state)
                intermediate, phase1 = fock_permutation_action(source_transposition, intermediate)
                observed, phase2 = fock_permutation_action(global_map, intermediate)
                expected, expected_phase = fock_permutation_action(target_transposition, state)
                signed_seam_failures += (
                    observed != expected or phase0 * phase1 * phase2 != expected_phase
                )
                signed_seam_columns += 1

    # The physical coordinate action itself composes exactly on both rail sites.
    coordinate_composition_failures = 0
    sample_sites = (np.asarray((7, 0, 0), dtype=int), np.asarray((9, 0, 0), dtype=int))
    for left in frames:
        for right in frames:
            coordinate_composition_failures += any(
                not np.array_equal(left @ (right @ site), (left @ right) @ site)
                for site in sample_sites
            )

    return {
        "proper_cubic_frames": len(frames),
        "signed_frame_semantics_checked": len(frames),
        "signed_compositions_checked": len(frames) ** 2,
        "one_particle_coin_covariance_maximum_residual": one_particle_coin_max,
        "signed_Fock_coin_covariance_maximum_residual": fock_coin_max,
        "signed_Fock_contact_covariance_maximum_residual": contact_max,
        "signed_Fock_reverse_layer_covariance_maximum_residual": reverse_max,
        "signed_individual_reverse_FSWAP_covariance_maximum_residual": signed_pair_max,
        "reverse_contact_family_mapping_failures": family_failures,
        "seam_endpoint_semantic_mapping_failures": seam_endpoint_failures,
        "signed_intercell_FSWAP_columns_checked": signed_seam_columns,
        "signed_intercell_FSWAP_endpoint_failures": signed_seam_endpoint_failures,
        "signed_intercell_FSWAP_column_failures": signed_seam_failures,
        "composition_failures": composition_failures,
        "maximum_one_particle_composition_residual": maximum_one_particle_composition_residual,
        "maximum_signed_Fock_composition_residual": maximum_signed_composition_residual,
        "physical_coordinate_composition_failures": coordinate_composition_failures,
        "frame_rows": frame_rows,
    }


def repetition_extension_covariance_boundary() -> dict[str, object]:
    frames = proper_cubic_frames()
    positive_directions = tuple(np.eye(3, dtype=int)[axis] for axis in range(3))

    def canonicalize(direction: np.ndarray) -> tuple[np.ndarray, int]:
        row = np.asarray(direction, dtype=int)
        nonzero = next(int(value) for value in row if value)
        return (row if nonzero > 0 else -row), int(nonzero < 0)

    def rail_swap(frame: np.ndarray, direction: np.ndarray) -> tuple[np.ndarray, int]:
        return canonicalize(frame @ direction)

    def swap_mask(mask: int, swapped: int) -> int:
        if not swapped:
            return mask
        return ((mask & 1) << 1) | ((mask & 2) >> 1)

    # The repetition stabilizer is Z0 Z1.  Row reduction in this two-rail
    # quotient is explicit rather than inferred from an orientation count.
    def repetition_coset_zero(xmask: int, zmask: int) -> bool:
        if xmask:
            return False
        return zmask in (0b00, 0b11)

    lifted_x = (0b11, 0b00)
    lifted_z = (0b00, 0b01)
    frame_reversals = 0
    full_X_equivariance_failures = 0
    full_Z_equivariance_failures = 0
    code_Z_equivariance_failures = 0
    frame_rows = []
    for frame_index, frame in enumerate(frames):
        row_failures = Counter()
        row_reversals = 0
        for direction in positive_directions:
            _target_direction, swapped = rail_swap(frame, direction)
            row_reversals += swapped
            observed_x = (swap_mask(lifted_x[0], swapped), swap_mask(lifted_x[1], swapped))
            observed_z = (swap_mask(lifted_z[0], swapped), swap_mask(lifted_z[1], swapped))
            full_X_equivariance_failures += observed_x != lifted_x
            full_Z_equivariance_failures += observed_z != lifted_z
            quotient = (observed_z[0] ^ lifted_z[0], observed_z[1] ^ lifted_z[1])
            code_failure = not repetition_coset_zero(*quotient)
            code_Z_equivariance_failures += code_failure
            row_failures["X_full"] += observed_x != lifted_x
            row_failures["Z_full"] += observed_z != lifted_z
            row_failures["Z_code"] += code_failure
        frame_reversals += row_reversals
        frame_rows.append(
            {
                "frame_index": frame_index,
                "orientation_reversals_across_three_axes": row_reversals,
                "failure_census": dict(row_failures),
            }
        )

    product_reversals = 0
    full_space_representation_failures = 0
    code_product_failures = 0
    product_full_Z_failures = 0
    for left in frames:
        for right in frames:
            for direction in positive_directions:
                middle_direction, right_swap = rail_swap(right, direction)
                final_direction, left_swap = rail_swap(left, middle_direction)
                direct_direction, direct_swap = rail_swap(left @ right, direction)
                sequential_swap = right_swap ^ left_swap
                full_space_representation_failures += (
                    not np.array_equal(final_direction, direct_direction)
                    or sequential_swap != direct_swap
                )
                product_reversals += direct_swap
                observed_z = (
                    swap_mask(lifted_z[0], direct_swap),
                    swap_mask(lifted_z[1], direct_swap),
                )
                product_full_Z_failures += observed_z != lifted_z
                quotient = (
                    observed_z[0] ^ lifted_z[0],
                    observed_z[1] ^ lifted_z[1],
                )
                code_product_failures += not repetition_coset_zero(*quotient)

    return {
        "probe_abstract_edges": "+x,+y,+z matter_stream representatives",
        "frames_checked": len(frames),
        "orientation_reversing_for_probe": frame_reversals,
        "lifted_X_full_space_equivariance_failures": full_X_equivariance_failures,
        "lifted_Z_full_space_equivariance_failures": full_Z_equivariance_failures,
        "lifted_Z_code_equivariance_failures": code_Z_equivariance_failures,
        "frame_axis_cases_checked": len(frames) * len(positive_directions),
        "compositions_checked": len(frames) ** 2,
        "composition_axis_cases_checked": len(frames) ** 2 * len(positive_directions),
        "product_orientation_reversals_for_probe": product_reversals,
        "lifted_Z_product_full_space_equivariance_failures": product_full_Z_failures,
        "lifted_Z_product_code_equivariance_failures": code_product_failures,
        "full_space_site_permutation_representation_failures": full_space_representation_failures,
        "full_space_site_permutation_is_a_representation": (
            full_space_representation_failures == 0
        ),
        "canonical_first_rail_extension_is_full_space_covariant": False,
        "canonical_first_rail_extension_is_code_covariant": (
            code_Z_equivariance_failures == 0 and code_product_failures == 0
        ),
        "repetition_stabilizer_row": {"x": 0, "z": 3},
        "frame_rows": frame_rows,
        "boundary": (
            "For an orientation-reversing frame, T_F L(Z_edge) is Z on the "
            "target second rail whereas L(F Z_edge) is Z on the target first "
            "rail. Their quotient is the stream ZZ repetition stabilizer. "
            "Thus the geometric site permutation composes on the full Hilbert "
            "space, but the chosen abstract-to-physical first-rail section is "
            "equivariant only after restriction to the repetition code."
        ),
    }


def two_cell_code_certificate() -> dict[str, object]:
    graph = OpenReferenceGraph(((0, 0, 0), (1, 0, 0)))
    stabilizers = constraints(graph)
    reducer = SignedStabilizerReducer(stabilizers, len(graph.edges))
    pairs = logical_pairs(graph)
    reverse_factors = []
    for cell in graph.cells:
        for axis in range(3):
            rows = onsite_fswap_rows(graph, cell, axis)
            reverse_factors.append(
                PhysicalFactor(
                    "reverse",
                    "reverse_fswap",
                    cell,
                    (axis,),
                    ((cell, 2 * axis), (cell, 2 * axis + 1)),
                    fswap_poly(rows),
                    rows,
                )
            )
    seam_rows = seam_fswap_rows(graph, graph.cells[0], 0)
    seam_factor = PhysicalFactor(
        "seam",
        "seam_fswap",
        graph.cells[0],
        (0,),
        ((graph.cells[0], 1), (graph.cells[1], 0)),
        fswap_poly(seam_rows),
        seam_rows,
    )
    fswap = check_fswaps(
        graph,
        tuple(reverse_factors) + (seam_factor,),
        pairs,
        stabilizers,
        reducer,
    )
    target = fswap_target(
        pairs[(graph.cells[0], 1)],
        pairs[(graph.cells[1], 0)],
        tuple(pairs[(graph.cells[0], mode)] for mode in range(2, 6)),
    )
    exact_residual = poly_residual(
        reducer.polynomial(seam_factor.polynomial), reducer.polynomial(target)
    )
    return {
        "cells": 2,
        "abstract_edges": len(graph.edges),
        "constraint_rank": reducer.rank,
        "logical_qubits_from_rank": len(graph.edges) - reducer.rank,
        "onsite_reverse_factors": len(reverse_factors),
        "intercell_dressed_factors": 1,
        "dressed_seam_exact_signed_coset_residual": exact_residual,
        "all_fswaps": fswap,
        "truth_table": exact_fswap_truth_table(),
    }


def validate_receipt(receipt: dict[str, object]) -> list[str]:
    failures: list[str] = []

    sources = receipt["sources"]
    if not sources["expected_base_is_ancestor"]:
        failures.append("expected base is not an ancestor")
    if sources["joined_scratch_imported"]:
        failures.append("joined scratch was imported")

    coin = receipt["coin_mass_contact"]
    for key in (
        "coin_one_particle_unitarity_residual",
        "coin_QR_triangular_residual",
        "coin_Fock_target_residual",
        "coin_factor_unitarity_maximum_residual",
        "mass_pairwise_maximum_residual",
        "Cycle230_imported_Cycle219_coin_residual",
        "contact_pair_unitarity_residual",
        "contact_full_onsite_target_residual",
        "contact_vacuum_phase_residual",
        "contact_one_particle_phase_maximum_residual",
        "contact_two_particle_phase_maximum_residual",
    ):
        if coin[key] > TOL:
            failures.append(f"coin/contact {key}")
    if coin["coin_factor_deletion_minimum_target_residual"] <= TOL:
        failures.append("coin factor deletion inactive")
    if coin["contact_factor_deletion_minimum_target_residual"] <= TOL:
        failures.append("contact factor deletion inactive")
    if coin["coin_schedule_factor_counts"] != {"coin_phase": 1, "coin_givens": 10}:
        failures.append("unexpected actual Cycle219 QR factor census")

    fixtures = receipt["fixtures"]
    for row in fixtures:
        prefix = f"fixture {row['shape']}"
        n, e = row["cells"], row["coarse_edges"]
        if row["abstract_graph_edges"] != 18 * n + 2 * e:
            failures.append(prefix + " abstract edge formula")
        if row["physical_carriers"] != 18 * n + 3 * e:
            failures.append(prefix + " physical repetition formula")
        if row["abstract_logical_qubits_from_rank"] != 6 * n:
            failures.append(prefix + " abstract code rank")
        if row["physical_logical_qubits_from_rank"] != 6 * n:
            failures.append(prefix + " physical code rank")
        expected_counts = {
            "coin": 11 * n,
            "reverse": 3 * n,
            "seam": e,
            "contact": 15 * n,
        }
        if row["stage_counts"] != expected_counts:
            failures.append(prefix + " factor census")
        for key in (
            "placement_collisions",
            "factor_full_space_unitarity_failures",
            "factor_constraint_commutator_failures",
            "lifted_factor_full_space_unitarity_failures",
            "repetition_commutator_failures",
            "repetition_lift_homomorphism_failures",
            "seam_endpoint_reuse_failures",
        ):
            if row[key]:
                failures.append(prefix + " " + key)
        if row["seam_onsite_shared_register_overlaps"] <= 0:
            failures.append(prefix + " no seam/onsite overlap")
        if row["maximum_physical_factor_weight"] > row["analytic_physical_weight_cap"]:
            failures.append(prefix + " physical factor weight cap")
        if row["maximum_physical_factor_L1_diameter"] > row["analytic_physical_L1_diameter_cap"]:
            failures.append(prefix + " physical factor diameter cap")
        chart = row["logical_chart"]
        for key in (
            "canonical_pair_failures",
            "stabilizer_commutator_failures",
            "Hermitian_involution_failures",
        ):
            if chart[key]:
                failures.append(prefix + " chart " + key)
        fswap = row["fswap"]
        for key in (
            "row_Hermitian_failures",
            "full_space_Hermitian_failures",
            "full_space_involution_failures",
            "constraint_commutator_failures",
            "exact_code_target_failures",
            "term_deletions_not_detected",
        ):
            if fswap[key]:
                failures.append(prefix + " fswap " + key)
        if fswap["maximum_code_target_residual"] > TOL:
            failures.append(prefix + " fswap target residual")
        log_extension = row["target_style_coin_contact_log_extension"]
        for key in (
            "maximum_log_expansion_residual",
            "maximum_signed_code_target_residual",
            "maximum_coefficient_imaginary_part",
        ):
            if log_extension[key] > TOL:
                failures.append(prefix + " target log extension " + key)
        for key in (
            "physical_term_Hermitian_failures",
            "physical_Hamiltonian_full_space_Hermitian_failures",
            "physical_exponential_full_space_unitarity_failures",
            "constraint_commutator_failures",
            "lifted_Hamiltonian_Hermitian_failures",
            "repetition_commutator_failures",
        ):
            if log_extension[key]:
                failures.append(prefix + " target log extension " + key)
        if log_extension["maximum_physical_generator_support"] > row["analytic_physical_weight_cap"]:
            failures.append(prefix + " target log extension support")
        if log_extension["maximum_physical_generator_L1_diameter"] > row["analytic_physical_L1_diameter_cap"]:
            failures.append(prefix + " target log extension diameter")

    two = receipt["two_cell_exact"]
    if two["logical_qubits_from_rank"] != 12:
        failures.append("two-cell code rank")
    if two["dressed_seam_exact_signed_coset_residual"] > TOL:
        failures.append("two-cell dressed seam target")
    if two["truth_table"]["truth_table_failures"]:
        failures.append("two-cell logical truth table")

    dressing = receipt["deletion_and_dressing"]
    if dressing["good_code_residual"] > TOL or dressing["good_constraint_commutator_failures"]:
        failures.append("good seam dressing")
    for row in dressing["term_deletions"]:
        if row["code_target_residual"] <= TOL or row["full_space_unitarity_residual"] <= TOL:
            failures.append("inactive seam term deletion")
    for name, row in dressing["dressing_deletions"].items():
        if row["code_target_residual"] <= TOL:
            failures.append(f"inactive {name}")

    order = receipt["two_cell_order_attack"]
    if order["canonical_word_target_residual"] > TOL:
        failures.append("canonical full-update order")
    if order["target_emitted_order_target_residual"] > TOL:
        failures.append("target emitted factor-stage order")
    if not order["independent_runner_composes_extracted_target_stage_word"]:
        failures.append("independent extracted target stage word")
    if order["contact_before_seam_counterfactual_target_residual"] <= 0.1:
        failures.append("contact-before-seam order attack did not activate")
    if order["contact_seam_commutator_norm"] <= 0.1:
        failures.append("contact/seam commutator unexpectedly small")

    covariance = receipt["covariance"]
    for key in (
        "one_particle_coin_covariance_maximum_residual",
        "signed_Fock_coin_covariance_maximum_residual",
        "signed_Fock_contact_covariance_maximum_residual",
        "signed_Fock_reverse_layer_covariance_maximum_residual",
        "signed_individual_reverse_FSWAP_covariance_maximum_residual",
        "maximum_one_particle_composition_residual",
        "maximum_signed_Fock_composition_residual",
    ):
        if covariance[key] > TOL:
            failures.append("covariance " + key)
    for key in (
        "reverse_contact_family_mapping_failures",
        "seam_endpoint_semantic_mapping_failures",
        "signed_intercell_FSWAP_endpoint_failures",
        "signed_intercell_FSWAP_column_failures",
        "composition_failures",
        "physical_coordinate_composition_failures",
    ):
        if covariance[key]:
            failures.append("covariance " + key)

    boundary = receipt["physical_extension_order_boundary"]
    if boundary["orientation_reversing_for_probe"] != 36:
        failures.append("24-frame x three-axis rail reversal census")
    if boundary["product_orientation_reversals_for_probe"] != 864:
        failures.append("576-product x three-axis rail reversal census")
    if boundary["lifted_Z_code_equivariance_failures"]:
        failures.append("rail Z code covariance")
    if boundary["lifted_Z_product_code_equivariance_failures"]:
        failures.append("rail Z product code covariance")
    if boundary["full_space_site_permutation_representation_failures"]:
        failures.append("rail site representation")
    if boundary["lifted_Z_full_space_equivariance_failures"] != 36:
        failures.append("rail Z full-space boundary not detected")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    parser.add_argument(
        "--receipt",
        type=Path,
        default=DEFAULT_REPO / "outputs" / "cycle870_openreference_recurrent_update_independent_receipt_2026_08_02.json",
    )
    args = parser.parse_args()
    repo = args.repo.resolve()
    scripts = repo / "scripts"
    if not scripts.is_dir():
        raise SystemExit(f"missing scripts directory: {scripts}")
    sys.path.insert(0, str(scripts))

    direct_input_hashes = {
        name: sha256(scripts / name) for name in EXPECTED_DIRECT_INPUT_SHA256
    }
    direct_input_pin_failures = {
        name: {"expected": expected, "observed": direct_input_hashes[name]}
        for name, expected in EXPECTED_DIRECT_INPUT_SHA256.items()
        if direct_input_hashes[name] != expected
    }

    # These are the two actual supplied input surfaces; no joined runner is imported.
    import common_matter_field_coin_family_cycle219_2026_07_16 as c219
    import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

    expected_base_is_ancestor = subprocess.run(
        ("git", "-C", str(repo), "merge-base", "--is-ancestor", EXPECTED_BASE_COMMIT, "HEAD"),
        check=False,
    ).returncode == 0
    coin_mass_contact, schedule, contact = coin_contact_certificate(c219, c230)
    coin = np.asarray(c219.common_species(c230.BETA).coin, dtype=complex)

    fixture_rows = []
    contexts = []
    for shape in ((3, 2, 2), (5, 3, 2)):
        row, context = fixture_certificate(shape, schedule, contact)
        fixture_rows.append(row)
        contexts.append(context)

    target_join = repo / TARGET_JOIN_REL
    target_placement = repo / TARGET_PLACEMENT_REL
    target_join_receipt = repo / TARGET_JOIN_RECEIPT_REL
    target_hashes = {
        "joined_recurrent_compiler": sha256(target_join) if target_join.is_file() else None,
        "physical_M2_placement": sha256(target_placement) if target_placement.is_file() else None,
        "joined_recurrent_compiler_receipt": (
            sha256(target_join_receipt) if target_join_receipt.is_file() else None
        ),
    }
    target_pin_failures = {
        name: {"expected": expected, "observed": target_hashes[key]}
        for name, key, expected in (
            (
                TARGET_JOIN_REL,
                "joined_recurrent_compiler",
                EXPECTED_TARGET_SHA256[TARGET_JOIN_REL],
            ),
            (
                TARGET_PLACEMENT_REL,
                "physical_M2_placement",
                EXPECTED_TARGET_SHA256[TARGET_PLACEMENT_REL],
            ),
            (
                TARGET_JOIN_RECEIPT_REL,
                "joined_recurrent_compiler_receipt",
                EXPECTED_TARGET_SHA256[TARGET_JOIN_RECEIPT_REL],
            ),
        )
        if target_hashes[key] != expected
    }
    target_receipt = (
        json.loads(target_join_receipt.read_text())
        if target_join_receipt.is_file()
        else {}
    )
    target_stage_runs = tuple(
        target_receipt.get("fixtures", [{}])[0]
        .get("stage_order", {})
        .get("observed_rotation_stage_runs", ())
    )
    target_current_order_is_canonical = target_stage_runs == (
        "onsite_coin_mass",
        "onsite_reverse_fswap",
        "directed_seam_fswap",
        "onsite_contact",
    )
    order_attack = two_cell_order_certificate(
        coin, schedule, contact, target_stage_runs
    )
    bounded_unitary_factors = all(
        row["factor_full_space_unitarity_failures"] == 0
        and row["lifted_factor_full_space_unitarity_failures"] == 0
        and row["maximum_physical_factor_weight"] <= row["analytic_physical_weight_cap"]
        and row["maximum_physical_factor_L1_diameter"] <= row["analytic_physical_L1_diameter_cap"]
        for row in fixture_rows
    )
    artifact_path = Path(__file__).resolve().relative_to(repo)
    receipt: dict[str, object] = {
        "artifact": {
            "path": str(artifact_path),
            "sha256_before_receipt_write": sha256(Path(__file__).resolve()),
            "method": "independent reconstruction; target scratch read/hash only, never imported",
        },
        "sources": {
            "repo": ".",
            "expected_base_commit": EXPECTED_BASE_COMMIT,
            "expected_base_is_ancestor": expected_base_is_ancestor,
            "direct_physics_imports": (
                "common_matter_field_coin_family_cycle219_2026_07_16",
                "spatial_car_contact_seam_form_factor_cycle230_2026_07_17",
            ),
            "direct_input_sha256": direct_input_hashes,
            "direct_input_pin_failures": direct_input_pin_failures,
            "joined_scratch_imported": False,
            "joined_target_imported": False,
            "target_hashes": target_hashes,
            "expected_target_sha256": EXPECTED_TARGET_SHA256,
            "target_pin_failures": target_pin_failures,
        },
        "coin_mass_contact": coin_mass_contact,
        "fixtures": fixture_rows,
        "two_cell_exact": two_cell_code_certificate(),
        "deletion_and_dressing": seam_dressing_deletion_certificate(),
        "two_cell_order_attack": order_attack,
        "covariance": covariance_certificate(coin, c230.COUPLING),
        "physical_extension_order_boundary": repetition_extension_covariance_boundary(),
        "claim_boundary": {
            "bounded_M2_unitary_factors": bounded_unitary_factors,
            "nearest_neighbor_elementary_decomposition_claimed": False,
            "intrinsic_layer_or_clock_claimed": False,
            "semantic_covariance": "full signed logical Fock space",
            "bare_graph_Pauli_covariance": "requires the usual local incidence-order Clifford chart/gauge",
            "repetition_lift_section_covariance": "code space, not full physical Hilbert space under orientation reversal",
            "scope": "two supplied finite fixtures and the size-independent local templates they exercise",
        },
    }
    failures = [f"direct input pin:{name}" for name in direct_input_pin_failures]
    failures.extend(f"target pin:{name}" for name in target_pin_failures)
    failures.extend(validate_receipt(receipt))
    receipt["validation_failures"] = failures
    receipt["independent_reconstruction_pass"] = not failures
    receipt["joined_target_acceptance"] = {
        "accepted_as_an_ordered_full_update": not failures and target_current_order_is_canonical,
        "reason": (
            "The current joined target emits and asserts coin/reverse/seam/contact. The "
            "independent composed word matches the exact target. The joined target also "
            "supplies the executable composition; this receipt is independent ordered-action evidence."
            if target_current_order_is_canonical
            else
            "The joined target source does not contain the canonical coin/reverse/seam/contact order."
        ),
        "counterfactual_contact_before_seam_rejected": (
            order_attack["contact_before_seam_counterfactual_target_residual"] > 0.1
        ),
    }
    args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True, default=str))
    print("INDEPENDENT_OPENREFERENCE_RECONSTRUCTION_PASS" if not failures else "INDEPENDENT_OPENREFERENCE_RECONSTRUCTION_FAIL")
    print(
        "CURRENT_JOINED_SCRATCH_ORDER_ACCEPTED"
        if target_current_order_is_canonical and not failures
        else "JOINED_SCRATCH_ORDER_GAP_DETECTED"
    )
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
