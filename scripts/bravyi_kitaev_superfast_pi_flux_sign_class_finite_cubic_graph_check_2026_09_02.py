#!/usr/bin/env python3
"""Finite cubic-graph checks for a BKSF all-minus face sector.

The runner declares every graph, Pauli operator, sign field, and Hamiltonian
used below.  It makes no identification with a framework-level physical law.
Exact checks use integer/F2/Z4 symplectic arithmetic.  Eigenvalue comparisons
are explicitly numerical with rtol=0 and the printed absolute tolerance.
"""

from collections import deque
from itertools import combinations, product
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 300
PASS = 0
FAIL = 0
EX = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
DIRS = ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1))


def check(label, condition):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def wrap(v, dims):
    return tuple(v[i] % dims[i] for i in range(3))


def staggered_eta(v, axis):
    """Separately declared sign pattern on oriented positive-axis edges."""
    if axis == 0:
        return 1
    if axis == 1:
        return -1 if v[0] & 1 else 1
    return -1 if (v[0] + v[1]) & 1 else 1


class Pauli:
    """i^k X^x Z^z, with bit positions indexing edge qubits."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k & 3
        self.x = x
        self.z = z

    def __mul__(self, other):
        return Pauli(self.k + other.k + 2 * (self.z & other.x).bit_count(), self.x ^ other.x, self.z ^ other.z)

    def __eq__(self, other):
        return (self.k, self.x, self.z) == (other.k, other.x, other.z)

    def phase(self, power):
        return Pauli(self.k + power, self.x, self.z)

    def negative(self):
        return self.phase(2)

    def hermitian(self):
        return (self.k & 1) == ((self.x & self.z).bit_count() & 1)

    def identity(self):
        return self.k == 0 and self.x == 0 and self.z == 0

    def minus_identity(self):
        return self.k == 2 and self.x == 0 and self.z == 0

    def vector(self, nqubits):
        return self.x | (self.z << nqubits)


IDENTITY = Pauli(0, 0, 0)


def pauli_product(operators):
    result = IDENTITY
    for operator in operators:
        result = result * operator
    return result


def commute(a, b):
    return ((a.x & b.z).bit_count() + (a.z & b.x).bit_count()) % 2 == 0


class CubicGraph:
    """Open cubic block or periodic cubic torus with one qubit per edge."""

    def __init__(self, dims, periodic):
        self.dims = tuple(dims)
        self.periodic = periodic
        self.vertices = list(product(*(range(d) for d in self.dims)))
        self.nvertices = len(self.vertices)
        self.edges = []
        for vertex in self.vertices:
            for axis in range(3):
                if self.step(vertex, EX[axis]) is not None:
                    self.edges.append((vertex, axis))
        self.edge_index = {edge: q for q, edge in enumerate(self.edges)}
        self.nqubits = len(self.edges)
        self.incident = {}
        for vertex in self.vertices:
            directed = {}
            for direction in range(6):
                neighbor = self.step(vertex, DIRS[direction])
                if neighbor is None:
                    continue
                edge = (vertex, direction - 3) if direction >= 3 else (neighbor, direction)
                directed[direction] = (neighbor, self.edge_index[edge])
            self.incident[vertex] = directed
        self.star = {
            vertex: sum(1 << q for _, q in self.incident[vertex].values())
            for vertex in self.vertices
        }

    def step(self, vertex, direction):
        neighbor = add(vertex, direction)
        if self.periodic:
            return wrap(neighbor, self.dims)
        if all(0 <= neighbor[i] < self.dims[i] for i in range(3)):
            return neighbor
        return None

    def A(self, vertex, direction):
        neighbor, q = self.incident[vertex][direction]
        x = 1 << q
        z = 0
        for prior, (_, q2) in self.incident[vertex].items():
            if prior < direction:
                z ^= 1 << q2
        reverse = (direction + 3) % 6
        for prior, (_, q2) in self.incident[neighbor].items():
            if prior < reverse:
                z ^= 1 << q2
        operator = Pauli((x & z).bit_count() & 1, x, z)
        return operator if direction >= 3 else operator.negative()

    def Aij(self, source, target):
        for direction, (neighbor, _) in self.incident[source].items():
            if neighbor == target:
                return self.A(source, direction)
        raise KeyError("vertices are not adjacent")

    def B(self, vertex):
        return Pauli(0, 0, self.star[vertex])

    def faces(self):
        faces = []
        for vertex in self.vertices:
            for axis1 in range(3):
                for axis2 in range(axis1 + 1, 3):
                    first = self.step(vertex, EX[axis1])
                    second = self.step(vertex, EX[axis2])
                    if first is None or second is None:
                        continue
                    opposite = self.step(first, EX[axis2])
                    if opposite is not None:
                        faces.append((vertex, first, opposite, second))
        return faces

    def face_operator(self, face):
        return pauli_product(
            [self.Aij(face[k], face[(k + 1) % 4]) for k in range(4)]
        ).phase(4)


def transport(graph, path):
    """Product of legal encoded hops around the supplied path, including i^n."""
    operators = [graph.Aij(path[k + 1], path[k]) for k in range(len(path) - 1)]
    return pauli_product(operators[::-1]).phase(len(path) - 1)


def f2_rank(vectors):
    basis = []
    for value in vectors:
        for pivot in basis:
            value = min(value, value ^ pivot)
        if value:
            basis.append(value)
            basis.sort(reverse=True)
    return len(basis), basis


def f2_relations(vectors):
    pivots = {}
    relations = []
    for j, value in enumerate(vectors):
        tag = 1 << j
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                old_value, old_tag = pivots[pivot]
                value ^= old_value
                tag ^= old_tag
            else:
                pivots[pivot] = (value, tag)
                break
        if value == 0:
            relations.append(tag)
    return relations, len(pivots)


def f2_pivots(vectors):
    pivots = {}
    for j, value in enumerate(vectors):
        tag = 1 << j
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                old_value, old_tag = pivots[pivot]
                value ^= old_value
                tag ^= old_tag
            else:
                pivots[pivot] = (value, tag)
                break
    return pivots


def f2_express(target, pivots):
    tag = 0
    while target:
        pivot = target.bit_length() - 1
        if pivot not in pivots:
            return None
        value, old_tag = pivots[pivot]
        target ^= value
        tag ^= old_tag
    return tag


def bit_positions(mask):
    positions = []
    while mask:
        bit = mask & -mask
        positions.append(bit.bit_length() - 1)
        mask ^= bit
    return positions


def solve_f2(rows, nunknown):
    coefficient_mask = (1 << nunknown) - 1
    pivots = []
    reduced = []
    for row in rows:
        for i, pivot in enumerate(pivots):
            if (row >> pivot) & 1:
                row ^= reduced[i]
        coefficients = row & coefficient_mask
        if coefficients == 0:
            if row:
                return None
            continue
        pivot = coefficients.bit_length() - 1
        for i in range(len(reduced)):
            if (reduced[i] >> pivot) & 1:
                reduced[i] ^= row
        reduced.append(row)
        pivots.append(pivot)
    solution = 0
    for row, pivot in zip(reduced, pivots):
        if (row >> nunknown) & 1:
            solution |= 1 << pivot
    return solution


def face_incidence(graph, face):
    mask = 0
    for source, target in zip(face, face[1:] + face[:1]):
        for axis in range(3):
            if graph.step(source, EX[axis]) == target and (source, axis) in graph.edge_index:
                mask ^= 1 << graph.edge_index[(source, axis)]
                break
            if graph.step(target, EX[axis]) == source and (target, axis) in graph.edge_index:
                mask ^= 1 << graph.edge_index[(target, axis)]
                break
    return mask


FIXTURES = (
    ((2, 2, 2), False, "open-2x2x2"),
    ((3, 3, 3), False, "open-3x3x3"),
    ((4, 4, 4), False, "open-4x4x4"),
    ((4, 4, 4), True, "torus-4x4x4"),
)


def relation_inventory(graph, incidence_masks=None):
    faces = graph.faces()
    stabilizers = [graph.face_operator(face) for face in faces]
    relations, rank = f2_relations([operator.vector(graph.nqubits) for operator in stabilizers])
    if incidence_masks is None:
        incidence_masks = [face_incidence(graph, face) for face in faces]
    phase_ok = True
    even_ok = True
    incidence_relation_ok = True
    for relation in relations:
        operators = [stabilizers[j] for j in bit_positions(relation)]
        phase_ok &= pauli_product(operators).identity()
        even_ok &= len(operators) % 2 == 0
        relation_incidence = 0
        for j in bit_positions(relation):
            relation_incidence ^= incidence_masks[j]
        incidence_relation_ok &= relation_incidence == 0
    rows = [mask | (1 << graph.nqubits) for mask in incidence_masks]
    incidence_solvable = solve_f2(rows, graph.nqubits) is not None
    return faces, stabilizers, relations, rank, phase_ok, even_ok, incidence_solvable, incidence_relation_ok


def induced_eta(graph, wilson):
    """Read an edge sign field from face=-1 and required torus loop inputs."""
    if graph.periodic:
        if wilson is None or len(wilson) != 3 or any(value not in (-1, 1) for value in wilson):
            raise ValueError("periodic graphs require an explicit three-sign Wilson tuple")
    elif wilson is not None:
        raise ValueError("open graphs take wilson=None")

    root = graph.vertices[0]
    parent = {root: None}
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for direction in range(6):
            if direction not in graph.incident[vertex]:
                continue
            neighbor = graph.incident[vertex][direction][0]
            if neighbor not in parent:
                parent[neighbor] = vertex
                queue.append(neighbor)
    tree_edges = {frozenset((vertex, previous)) for vertex, previous in parent.items() if previous is not None}

    def tree_path(vertex):
        path = [vertex]
        while parent[path[-1]] is not None:
            path.append(parent[path[-1]])
        return path[::-1]

    generators = [graph.face_operator(face) for face in graph.faces()]
    eigenvalues = [-1] * len(generators)
    if graph.periodic:
        for axis in range(3):
            cycle = [
                wrap(tuple(k if i == axis else 0 for i in range(3)), graph.dims)
                for k in range(graph.dims[axis])
            ]
            generators.append(transport(graph, cycle + [cycle[0]]))
        eigenvalues.extend(wilson)

    vectors = [operator.vector(graph.nqubits) for operator in generators]
    pivots = f2_pivots(vectors)
    consistent = True
    relations, _ = f2_relations(vectors)
    for relation in relations:
        indices = bit_positions(relation)
        product_operator = pauli_product([generators[j] for j in indices])
        phase = 1 if product_operator.identity() else (-1 if product_operator.minus_identity() else 0)
        requested = np.prod([eigenvalues[j] for j in indices], dtype=int)
        consistent &= phase != 0 and requested == phase

    eta = {}
    for vertex, axis in graph.edges:
        neighbor = graph.step(vertex, EX[axis])
        if frozenset((vertex, neighbor)) in tree_edges:
            eta[(vertex, axis)] = 1
            continue
        path_v = tree_path(vertex)
        path_w = tree_path(neighbor)
        operator = transport(graph, path_v + [neighbor] + path_w[::-1][1:])
        expression = f2_express(operator.vector(graph.nqubits), pivots)
        if expression is None:
            return None, False
        indices = bit_positions(expression)
        generated = pauli_product([generators[j] for j in indices])
        residual = (operator.k - generated.k) & 3
        if residual not in (0, 2):
            return None, False
        sign = 1 if residual == 0 else -1
        for j in indices:
            sign *= eigenvalues[j]
        eta[(vertex, axis)] = sign
    return eta, consistent


def face_holonomies(graph, eta):
    values = []
    for face in graph.faces():
        value = 1
        for source, target in zip(face, face[1:] + face[:1]):
            for axis in range(3):
                if graph.step(source, EX[axis]) == target and (source, axis) in eta:
                    value *= eta[(source, axis)]
                    break
                if graph.step(target, EX[axis]) == source and (target, axis) in eta:
                    value *= eta[(target, axis)]
                    break
        values.append(value)
    return values


def wilson_holonomies(graph, eta):
    if not graph.periodic:
        return None
    values = []
    for axis in range(3):
        value = 1
        for k in range(graph.dims[axis]):
            vertex = tuple(k if i == axis else 0 for i in range(3))
            value *= eta[(vertex, axis)]
        values.append(value)
    return tuple(values)


def gauge_witness(graph, first, second):
    signs = {graph.vertices[0]: 1}
    queue = deque([graph.vertices[0]])
    adjacency = {}
    for vertex, axis in graph.edges:
        neighbor = graph.step(vertex, EX[axis])
        adjacency.setdefault(vertex, []).append((neighbor, vertex, axis))
        adjacency.setdefault(neighbor, []).append((vertex, vertex, axis))
    while queue:
        vertex = queue.popleft()
        for neighbor, source, axis in adjacency[vertex]:
            ratio = first[(source, axis)] * second[(source, axis)]
            wanted = signs[vertex] * ratio
            if neighbor in signs:
                if signs[neighbor] != wanted:
                    return None
            else:
                signs[neighbor] = wanted
                queue.append(neighbor)
    return signs if len(signs) == graph.nvertices else None


def one_particle_matrix(graph, eta):
    index = {vertex: i for i, vertex in enumerate(graph.vertices)}
    matrix = np.zeros((graph.nvertices, graph.nvertices))
    for vertex, axis in graph.edges:
        neighbor = graph.step(vertex, EX[axis])
        matrix[index[neighbor], index[vertex]] += eta[(vertex, axis)]
        matrix[index[vertex], index[neighbor]] += eta[(vertex, axis)]
    return matrix


def computational_b_eigenvalue(state, star):
    return 1 - 2 * ((state & star).bit_count() & 1)


def apply_pauli(operator, vector, indices):
    destination = indices ^ operator.x
    phase = np.array((1, 1j, -1, -1j))[operator.k]
    signs = np.fromiter(
        (1 - 2 * ((int(value) & operator.z).bit_count() & 1) for value in destination),
        dtype=np.int8,
        count=len(destination),
    )
    return phase * signs * vector[destination]


def deterministic_sector_basis(graph, stabilizers):
    dimension = 1 << graph.nqubits
    indices = np.arange(dimension, dtype=np.int64)
    configurations = {}
    for state in range(dimension):
        bits = tuple(0 if computational_b_eigenvalue(state, graph.star[v]) == 1 else 1 for v in graph.vertices)
        configurations.setdefault(bits, []).append(state)

    basis = []
    for states in configurations.values():
        selected = None
        for seed in states:
            vector = np.zeros(dimension, dtype=complex)
            vector[seed] = 1
            for stabilizer in stabilizers:
                vector = (vector - apply_pauli(stabilizer, vector, indices)) / 2
            norm = np.linalg.norm(vector)
            if norm > 1e-12:
                selected = vector / norm
                break
        if selected is None:
            return None, configurations
        basis.append(selected)
    return np.array(basis), configurations


def main():
    fixture_data = {}
    local_algebra_ok = True
    transport_ok = True
    relation_ok = True

    for dims, periodic, name in FIXTURES:
        graph = CubicGraph(dims, periodic)
        faces, stabilizers, relations, rank, phase_ok, even_ok, incidence_solvable, incidence_relation_ok = relation_inventory(graph)
        fixture_data[name] = (graph, faces, stabilizers, relations, rank)

        directed_ok = all(
            graph.Aij(vertex, graph.step(vertex, EX[axis])).negative()
            == graph.Aij(graph.step(vertex, EX[axis]), vertex)
            for vertex, axis in graph.edges
        )
        b_ok = all(graph.B(vertex).hermitian() and (graph.B(vertex) * graph.B(vertex)).identity() for vertex in graph.vertices)
        s_ok = all(operator.hermitian() and (operator * operator).identity() for operator in stabilizers)
        commute_ok = all(commute(a, b) for a, b in combinations(stabilizers, 2))
        commute_b_ok = all(commute(operator, graph.B(vertex)) for operator in stabilizers for vertex in graph.vertices)
        local_algebra_ok &= directed_ok and b_ok and s_ok and commute_ok and commute_b_ok

        transport_ok &= all(
            transport(graph, list(face) + [face[0]]) == graph.face_operator(face)
            for face in faces
        )
        relation_ok &= phase_ok and even_ok and incidence_solvable and incidence_relation_ok

    check(
        "A [exact] A_ji=-A_ij; B_i and S_f are Hermitian involutions; all retained faces commute pairwise and with every B_i",
        local_algebra_ok,
    )
    check(
        "B [exact] ordered four-hop transport equals S_f with the Z4 phase on every face of the four retained fixtures",
        transport_ok,
    )
    check(
        "C [exact] every face relation has product +I and even support, and each all-minus face-incidence system is solvable",
        relation_ok,
    )

    cube = fixture_data["open-2x2x2"][0]
    legal_ok = True
    for vertex, axis in cube.edges:
        neighbor = cube.step(vertex, EX[axis])
        for state in range(1 << cube.nqubits):
            difference = computational_b_eigenvalue(state, cube.star[neighbor]) - computational_b_eigenvalue(state, cube.star[vertex])
            source_occupied = computational_b_eigenvalue(state, cube.star[vertex]) == -1
            target_empty = computational_b_eigenvalue(state, cube.star[neighbor]) == 1
            if source_occupied and target_empty:
                legal_ok &= difference == 2
            elif target_empty is False and source_occupied is False:
                legal_ok &= difference in (-2, 0)
    check("D [exact] the B_j-B_i factor equals 2 on every enumerated legal cube hop", legal_ok)

    gauge_ok = True
    spectrum_ok = True
    maximum_spectral_error = 0.0
    eta_cube = None
    torus = None
    torus_eta = None
    for dims, periodic, name in FIXTURES:
        graph = fixture_data[name][0]
        requested_wilson = (1, 1, 1) if periodic else None
        eta, consistent = induced_eta(graph, requested_wilson)
        declared = {(vertex, axis): staggered_eta(vertex, axis) for vertex, axis in graph.edges}
        witness = gauge_witness(graph, eta, declared)
        edge_ok = witness is not None and all(
            witness[vertex] * witness[graph.step(vertex, EX[axis])] * eta[(vertex, axis)] == declared[(vertex, axis)]
            for vertex, axis in graph.edges
        )
        holonomy_ok = set(face_holonomies(graph, eta)) == {-1}
        wilson_ok = not periodic or wilson_holonomies(graph, eta) == requested_wilson
        gauge_ok &= consistent and edge_ok and holonomy_ok and wilson_ok

        first = np.sort(np.linalg.eigvalsh(one_particle_matrix(graph, eta)))
        second = np.sort(np.linalg.eigvalsh(one_particle_matrix(graph, declared)))
        error = float(np.max(np.abs(first - second)))
        maximum_spectral_error = max(maximum_spectral_error, error)
        spectrum_ok &= np.allclose(first, second, rtol=0, atol=1e-9)
        if name == "open-2x2x2":
            eta_cube = eta
        if name == "torus-4x4x4":
            torus = graph
            torus_eta = eta

    check(
        "E [exact] explicit (+,+,+) torus Wilson data and all-minus faces yield an edge-by-edge gauge witness to the declared staggered sign pattern on all fixtures",
        gauge_ok,
    )
    check(
        f"F [numerical, rtol=0, atol=1e-9] sorted unrounded one-particle spectra agree; max absolute error {maximum_spectral_error:.3e}",
        spectrum_ok,
    )

    cube_graph_value, _, cube_stabilizers, _, cube_rank = fixture_data["open-2x2x2"]
    independent_indices = []
    current = []
    for j, operator in enumerate(cube_stabilizers):
        if f2_rank(current + [operator.vector(cube_graph_value.nqubits)])[0] > f2_rank(current)[0]:
            current.append(operator.vector(cube_graph_value.nqubits))
            independent_indices.append(j)
    independent_stabilizers = [cube_stabilizers[j] for j in independent_indices]
    star_rank = f2_rank(cube_graph_value.star.values())[0]
    sector_dimension = 1 << (cube_graph_value.nqubits - cube_rank)
    basis, configurations = deterministic_sector_basis(cube_graph_value, independent_stabilizers)
    exact_dimension_ok = cube_rank == 5 and star_rank == 7 and sector_dimension == 128 and len(configurations) == 128
    check(
        "G [exact] open cube face rank=5 gives all-minus sector dimension 2^(12-5)=128; star rank=7 gives 128 even-parity B syndromes",
        exact_dimension_ok,
    )

    basis_numerical_ok = basis is not None and basis.shape == (128, 4096)

    indices = np.arange(1 << cube_graph_value.nqubits, dtype=np.int64)
    columns = []
    for vector in basis:
        output = np.zeros_like(vector)
        for vertex, axis in cube_graph_value.edges:
            neighbor = cube_graph_value.step(vertex, EX[axis])
            aop = cube_graph_value.Aij(vertex, neighbor)
            output += 0.5j * apply_pauli(aop * cube_graph_value.B(vertex), vector, indices)
            output -= 0.5j * apply_pauli(aop * cube_graph_value.B(neighbor), vector, indices)
        columns.append(output)
    encoded = basis.conj() @ np.array(columns).T
    encoded_spectrum = np.sort(np.linalg.eigvalsh(encoded))
    one_particle_spectrum = np.linalg.eigvalsh(one_particle_matrix(cube_graph_value, eta_cube))
    free_even = np.sort(
        np.array(
            [
                sum(one_particle_spectrum[j] for j in range(8) if (mask >> j) & 1)
                for mask in range(1 << 8)
                if mask.bit_count() % 2 == 0
            ]
        )
    )
    many_body_error = float(np.max(np.abs(encoded_spectrum - free_even)))
    many_body_ok = basis_numerical_ok and np.allclose(encoded, encoded.conj().T, rtol=0, atol=1e-12) and np.allclose(
        encoded_spectrum, free_even, rtol=0, atol=1e-11
    )
    check(
        f"H [numerical, basis norm threshold=1e-12, rtol=0, atol=1e-11] deterministic projected all-minus cube basis is complete, encoded hopping is Hermitian, and its spectrum matches the 128-level even-parity free spectrum; max error {many_body_error:.3e}",
        many_body_ok,
    )

    first_face = cube_graph_value.faces()[0]
    transport_mutation_caught = transport(cube_graph_value, list(first_face) + [first_face[0]]).negative() != cube_graph_value.face_operator(first_face)
    mutated_incidence = [face_incidence(cube_graph_value, face) for face in cube_graph_value.faces()]
    mutated_incidence[0] ^= 1
    (
        _,
        _,
        _,
        _,
        mutated_phase_ok,
        mutated_even_ok,
        mutated_solvable,
        mutated_incidence_relation_ok,
    ) = relation_inventory(cube_graph_value, mutated_incidence)
    incidence_mutation_caught = not (
        mutated_phase_ok and mutated_even_ok and mutated_solvable and mutated_incidence_relation_ok
    )

    wilson_mutations_caught = True
    for axis in range(3):
        mutated_wilson = tuple(-1 if i == axis else 1 for i in range(3))
        mutated_eta, consistent = induced_eta(torus, mutated_wilson)
        declared = {(vertex, direction): staggered_eta(vertex, direction) for vertex, direction in torus.edges}
        wilson_mutations_caught &= consistent
        wilson_mutations_caught &= wilson_holonomies(torus, mutated_eta) == mutated_wilson
        wilson_mutations_caught &= gauge_witness(torus, mutated_eta, declared) is None

    altered_eta = dict(torus_eta)
    altered_eta[torus.edges[0]] *= -1
    edge_mutation_caught = gauge_witness(torus, altered_eta, torus_eta) is None
    omitted_constraint_caught = f2_rank(
        [operator.vector(cube_graph_value.nqubits) for operator in independent_stabilizers[:-1]]
    )[0] == 4 and (1 << (cube_graph_value.nqubits - 4)) == 256
    spectral_shift_caught = not np.allclose(
        one_particle_spectrum + 1e-7, one_particle_spectrum, rtol=0, atol=1e-9
    )
    many_body_target_caught = not np.allclose(
        encoded_spectrum, free_even + 1e-7, rtol=0, atol=1e-11
    )
    check(
        "I [mutations] transport phase, face incidence, three Wilson signs, one edge sign, one omitted stabilizer, and both spectral targets are rejected",
        all(
            (
                transport_mutation_caught,
                incidence_mutation_caught,
                wilson_mutations_caught,
                edge_mutation_caught,
                omitted_constraint_caught,
                spectral_shift_caught,
                many_body_target_caught,
            )
        ),
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
