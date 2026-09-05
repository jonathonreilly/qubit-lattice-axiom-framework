#!/usr/bin/env python3
"""Independent finite checks for the native physical-edge Record instrument.

This checker uses dense edge-Pauli matrices only for graphs with at most six
edges and direct occupation-sign fermion matrices for four modes.  It is an
independent same-model-family check and does not import another scientific
runner.
"""

from __future__ import annotations

import os

for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import ast
import hashlib
import itertools
import math
import pathlib
import sys
from dataclasses import dataclass

import numpy as np
import scipy.linalg


AUDIT_TIMEOUT_SEC = 180
DENSE_MATRIX_AXIS_LIMIT = 600
ATOL = 3.0e-10
RANK_TOL = 2.0e-9

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
Z2 = np.diag([1.0, -1.0]).astype(complex)


class CheckFailure(AssertionError):
    """A scientific or source-contract check failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value))) if value.size else 0.0


def close(left: np.ndarray, right: np.ndarray, message: str, tol: float = ATOL) -> None:
    error = max_abs(np.asarray(left) - np.asarray(right))
    require(error <= tol, f"{message}: residual={error:.3e}")


def matrix_rank(matrix: np.ndarray, tol: float = RANK_TOL) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tol))


def pauli_word(edge_count: int, operators: dict[int, np.ndarray]) -> np.ndarray:
    require(2**edge_count <= DENSE_MATRIX_AXIS_LIMIT, "dense Pauli matrix too large")
    result = np.ones((1, 1), dtype=complex)
    for edge_index in range(edge_count):
        result = np.kron(result, operators.get(edge_index, I2))
    return result


@dataclass(frozen=True)
class SmallGraph:
    vertex_count: int
    edges: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        normalized = tuple(tuple(sorted(edge)) for edge in self.edges)
        require(normalized == self.edges, "edges must be stored in canonical orientation")
        require(len(set(normalized)) == len(normalized), "graph has a repeated edge")
        require(all(i != j for i, j in normalized), "graph has a loop")

    @property
    def edge_count(self) -> int:
        return len(self.edges)

    @property
    def dimension(self) -> int:
        return 2**self.edge_count

    def edge_index(self, i: int, j: int) -> int:
        return self.edges.index(tuple(sorted((i, j))))

    def neighbors(self, vertex: int) -> tuple[int, ...]:
        values = []
        for i, j in self.edges:
            if i == vertex:
                values.append(j)
            elif j == vertex:
                values.append(i)
        return tuple(sorted(values))

    def vertex_parity(self, vertex: int) -> np.ndarray:
        operators = {
            self.edge_index(vertex, neighbor): Z2
            for neighbor in self.neighbors(vertex)
        }
        return pauli_word(self.edge_count, operators)

    def edge_generator(self, i: int, j: int) -> np.ndarray:
        edge_position = self.edge_index(i, j)
        operators: dict[int, np.ndarray] = {edge_position: X2}
        for neighbor in self.neighbors(i):
            if neighbor < j:
                operators[self.edge_index(i, neighbor)] = Z2
        for neighbor in self.neighbors(j):
            if neighbor < i:
                operators[self.edge_index(j, neighbor)] = Z2
        orientation = 1.0 if i < j else -1.0
        return orientation * pauli_word(self.edge_count, operators)

    def hopping_generator(self, edge: tuple[int, int]) -> np.ndarray:
        i, j = edge
        a_ij = self.edge_generator(i, j)
        return 0.5j * a_ij @ (self.vertex_parity(i) - self.vertex_parity(j))

    def edge_z(self, edge: tuple[int, int]) -> np.ndarray:
        return pauli_word(self.edge_count, {self.edge_index(*edge): Z2})

    def cycle_stabilizer(self, oriented_vertices: tuple[int, ...]) -> np.ndarray:
        require(oriented_vertices[0] == oriented_vertices[-1], "cycle must be closed")
        length = len(oriented_vertices) - 1
        result = (1j**length) * np.eye(self.dimension, dtype=complex)
        for i, j in zip(oriented_vertices[:-1], oriented_vertices[1:]):
            result = result @ self.edge_generator(i, j)
        return result


@dataclass(frozen=True)
class FockCarrier:
    mode_count: int
    masks: tuple[int, ...]
    annihilators_full: tuple[np.ndarray, ...]
    vertex_parities: tuple[np.ndarray, ...]
    edge_generators: dict[tuple[int, int], np.ndarray]
    hoppings: dict[tuple[int, int], np.ndarray]
    number: np.ndarray


def direct_even_fock(mode_count: int) -> FockCarrier:
    full_dimension = 2**mode_count
    annihilators = []
    for mode in range(mode_count):
        operator = np.zeros((full_dimension, full_dimension), dtype=complex)
        lower_mask = (1 << mode) - 1
        for mask in range(full_dimension):
            if (mask >> mode) & 1:
                sign = -1.0 if (mask & lower_mask).bit_count() % 2 else 1.0
                operator[mask ^ (1 << mode), mask] = sign
        annihilators.append(operator)
    masks = tuple(mask for mask in range(full_dimension) if mask.bit_count() % 2 == 0)
    selector = np.ix_(masks, masks)
    identity = np.eye(full_dimension, dtype=complex)
    majoranas = [operator + operator.conj().T for operator in annihilators]
    vertex_parities = []
    for operator in annihilators:
        parity = identity - 2.0 * operator.conj().T @ operator
        vertex_parities.append(parity[selector])
    edge_generators: dict[tuple[int, int], np.ndarray] = {}
    hoppings: dict[tuple[int, int], np.ndarray] = {}
    for i in range(mode_count):
        for j in range(i + 1, mode_count):
            edge = (i, j)
            a_ij = -1j * majoranas[i] @ majoranas[j]
            edge_generators[edge] = a_ij[selector]
            direct_hop = (
                annihilators[i].conj().T @ annihilators[j]
                + annihilators[j].conj().T @ annihilators[i]
            )
            hoppings[edge] = direct_hop[selector]
    number_values = np.array([mask.bit_count() for mask in masks], dtype=float)
    return FockCarrier(
        mode_count=mode_count,
        masks=masks,
        annihilators_full=tuple(annihilators),
        vertex_parities=tuple(vertex_parities),
        edge_generators=edge_generators,
        hoppings=hoppings,
        number=np.diag(number_values).astype(complex),
    )


def code_isometry(
    graph: SmallGraph,
    fock: FockCarrier,
    cycles: tuple[tuple[int, ...], ...],
) -> np.ndarray:
    physical_dimension = graph.dimension
    fock_dimension = len(fock.masks)
    physical_identity = np.eye(physical_dimension, dtype=complex)
    fock_identity = np.eye(fock_dimension, dtype=complex)
    constraints = []
    for vertex in range(graph.vertex_count):
        constraints.append(
            np.kron(fock_identity, graph.vertex_parity(vertex))
            - np.kron(fock.vertex_parities[vertex].T, physical_identity)
        )
    for edge in graph.edges:
        constraints.append(
            np.kron(fock_identity, graph.edge_generator(*edge))
            - np.kron(fock.edge_generators[edge].T, physical_identity)
        )
    for cycle in cycles:
        stabilizer = graph.cycle_stabilizer(cycle)
        constraints.append(np.kron(fock_identity, stabilizer - physical_identity))
    constraint_matrix = np.vstack(constraints)
    null_basis = scipy.linalg.null_space(constraint_matrix, rcond=1.0e-11)
    require(null_basis.shape[1] == 1, f"intertwiner nullity is {null_basis.shape[1]}")
    isometry = null_basis[:, 0].reshape((physical_dimension, fock_dimension), order="F")
    gram = isometry.conj().T @ isometry
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    require(float(np.min(eigenvalues)) > 1.0e-10, "intertwiner has deficient rank")
    inverse_root = eigenvectors @ np.diag(eigenvalues**-0.5) @ eigenvectors.conj().T
    isometry = isometry @ inverse_root
    close(isometry.conj().T @ isometry, fock_identity, "intertwiner isometry")
    return isometry


def commutant_nullity(generators: list[np.ndarray]) -> int:
    dimension = generators[0].shape[0]
    identity = np.eye(dimension, dtype=complex)
    constraints = [
        np.kron(identity, generator) - np.kron(generator.T, identity)
        for generator in generators
    ]
    singular_values = np.linalg.svd(np.vstack(constraints), compute_uv=False)
    return int(np.count_nonzero(singular_values <= RANK_TOL))


def normalized(vector: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(vector))
    require(norm > 1.0e-14, "cannot normalize a zero vector")
    return vector / norm


def fixed_number_vector(fock: FockCarrier, particle_number: int) -> np.ndarray:
    vector = np.zeros(len(fock.masks), dtype=complex)
    for position, mask in enumerate(fock.masks):
        if mask.bit_count() == particle_number:
            real_part = 1.0 + 0.17 * (position + 1)
            imaginary_part = 0.11 * ((position + 2) ** 2 % 7)
            vector[position] = real_part + 1j * imaginary_part
    return normalized(vector)


def projector_from_involution(involution: np.ndarray, sign: int) -> np.ndarray:
    require(sign in (-1, 1), "projector sign must be plus or minus one")
    return 0.5 * (np.eye(involution.shape[0], dtype=complex) + sign * involution)


def range_basis(projector: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(projector)
    basis = eigenvectors[:, eigenvalues > 0.5]
    close(basis.conj().T @ basis, np.eye(basis.shape[1]), "range basis")
    return basis


def physical_number(graph: SmallGraph) -> np.ndarray:
    identity = np.eye(graph.dimension, dtype=complex)
    return sum(
        (identity - graph.vertex_parity(vertex)) / 2.0
        for vertex in range(graph.vertex_count)
    )


def basis_vector(fock: FockCarrier, mask: int) -> np.ndarray:
    vector = np.zeros(len(fock.masks), dtype=complex)
    vector[fock.masks.index(mask)] = 1.0
    return vector


def restricted_generators(
    fock: FockCarrier,
    edges: tuple[tuple[int, int], ...],
    subspace: np.ndarray,
) -> list[np.ndarray]:
    generators = list(fock.vertex_parities) + [fock.edge_generators[edge] for edge in edges]
    return [subspace.conj().T @ generator @ subspace for generator in generators]


def direct_dictionary_check() -> str:
    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    path = SmallGraph(4, ((0, 1), (1, 2), (2, 3)))
    fock = direct_even_fock(4)
    square_cycle = (0, 1, 2, 3, 0)
    square_stabilizer = square.cycle_stabilizer(square_cycle)
    close(square_stabilizer, square_stabilizer.conj().T, "square stabilizer Hermiticity")
    close(square_stabilizer @ square_stabilizer, np.eye(16), "square stabilizer square")
    require(matrix_rank(projector_from_involution(square_stabilizer, 1)) == 8, "square code rank")
    square_isometry = code_isometry(square, fock, (square_cycle,))
    path_isometry = code_isometry(path, fock, ())
    for graph, isometry in ((square, square_isometry), (path, path_isometry)):
        for vertex in range(4):
            close(
                graph.vertex_parity(vertex) @ isometry,
                isometry @ fock.vertex_parities[vertex],
                f"B dictionary graph_edges={graph.edge_count} vertex={vertex}",
            )
        for edge in graph.edges:
            physical_a = graph.edge_generator(*edge)
            physical_t = graph.hopping_generator(edge)
            fock_a = fock.edge_generators[edge]
            fock_t_from_dictionary = (
                0.5j
                * fock_a
                @ (fock.vertex_parities[edge[0]] - fock.vertex_parities[edge[1]])
            )
            close(physical_a @ isometry, isometry @ fock_a, f"A dictionary edge={edge}")
            close(fock_t_from_dictionary, fock.hoppings[edge], f"direct CAR hopping edge={edge}")
            close(physical_t @ isometry, isometry @ fock.hoppings[edge], f"T dictionary edge={edge}")
            i, j = edge
            expected_square = 0.5 * (
                np.eye(graph.dimension) - graph.vertex_parity(i) @ graph.vertex_parity(j)
            )
            close(physical_t @ physical_t, expected_square, f"T square edge={edge}")
    generators = list(fock.vertex_parities) + [fock.edge_generators[e] for e in path.edges]
    require(commutant_nullity(generators) == 1, "connected-tree surviving algebra is not full")

    ring6 = SmallGraph(6, ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)))
    oriented6 = (0, 1, 2, 3, 4, 5, 0)
    stabilizer6 = ring6.cycle_stabilizer(oriented6)
    close(stabilizer6, stabilizer6.conj().T, "length-six stabilizer Hermiticity")
    close(stabilizer6 @ stabilizer6, np.eye(64), "length-six stabilizer square")
    require(matrix_rank(projector_from_involution(stabilizer6, 1)) == 32, "length-six code rank")
    wrong_last_orientation = (-1.0) * stabilizer6
    direct_wrong = (1j**6) * np.eye(64, dtype=complex)
    for i, j in zip(oriented6[:-2], oriented6[1:-1]):
        direct_wrong = direct_wrong @ ring6.edge_generator(i, j)
    direct_wrong = direct_wrong @ ring6.edge_generator(0, 5)
    close(direct_wrong, wrong_last_orientation, "negative closing orientation is load-bearing")
    return "square/path dictionaries, full tree algebra, and length-6 phase verified"


def nonbridge_instrument_check() -> str:
    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    fock = direct_even_fock(4)
    cycle = (0, 1, 2, 3, 0)
    stabilizer = square.cycle_stabilizer(cycle)
    code_projector = projector_from_involution(stabilizer, 1)
    isometry = code_isometry(square, fock, (cycle,))
    recorded_edge = (0, 3)
    record_z = square.edge_z(recorded_edge)
    close(stabilizer @ record_z, -record_z @ stabilizer, "nonbridge cycle anticommutation")
    close(
        code_projector @ record_z @ code_projector,
        np.zeros_like(code_projector),
        "compressed nonbridge Z vanishes",
    )
    state = fixed_number_vector(fock, 2)
    physical_state = isometry @ state
    surviving_edges = tuple(edge for edge in square.edges if edge != recorded_edge)
    fock_generators = list(fock.vertex_parities) + [
        fock.edge_generators[edge] for edge in surviving_edges
    ]
    require(commutant_nullity(fock_generators) == 1, "nonbridge surviving algebra commutant")
    branch_states = []
    for sign in (-1, 1):
        projector = projector_from_involution(record_z, sign)
        branch_map = math.sqrt(2.0) * projector @ isometry
        close(branch_map.conj().T @ branch_map, np.eye(8), f"nonbridge J_{sign} isometry")
        require(matrix_rank(projector) == 8, f"updated nonbridge code rank sign={sign}")
        probability = float(np.vdot(physical_state, projector @ physical_state).real)
        require(abs(probability - 0.5) <= ATOL, f"nonbridge probability sign={sign}")
        for vertex in range(4):
            close(
                square.vertex_parity(vertex) @ branch_map,
                branch_map @ fock.vertex_parities[vertex],
                f"nonbridge surviving B vertex={vertex} sign={sign}",
            )
        for edge in surviving_edges:
            close(
                square.edge_generator(*edge) @ branch_map,
                branch_map @ fock.edge_generators[edge],
                f"nonbridge surviving A edge={edge} sign={sign}",
            )
        branch_state = branch_map @ state
        close(record_z @ branch_state, sign * branch_state, f"sharp nonbridge Record {sign}")
        branch_states.append(branch_state)
    require(abs(np.vdot(branch_states[0], branch_states[1])) <= ATOL, "raw branches not orthogonal")
    return "fair physical Z branches and faithful full surviving CAR algebra verified"


def bridge_and_history_check() -> str:
    fock = direct_even_fock(4)
    path = SmallGraph(4, ((0, 1), (1, 2), (2, 3)))
    path_isometry = code_isometry(path, fock, ())
    number = physical_number(path)
    close(number @ path_isometry, path_isometry @ fock.number, "path original number dictionary")
    for edge in path.edges:
        close(
            number @ path.hopping_generator(edge),
            path.hopping_generator(edge) @ number,
            f"full physical number conservation edge={edge}",
        )

    central_z = path.edge_z((1, 2))
    central_parity = fock.vertex_parities[0] @ fock.vertex_parities[1]
    leaf_z = path.edge_z((0, 1))
    leaf_parity = fock.vertex_parities[0]
    close(central_z @ path_isometry, path_isometry @ central_parity, "bridge 2+2 identity")
    close(leaf_z @ path_isometry, path_isometry @ leaf_parity, "bridge 1+3 identity")
    number_two = np.diag([float(mask.bit_count() == 2) for mask in fock.masks]).astype(complex)
    expected_central_dimensions = {-1: 4, 1: 2}
    for record_z, parity, label, expected_dimensions in (
        (central_z, central_parity, "2+2", expected_central_dimensions),
        (leaf_z, leaf_parity, "1+3", {-1: 3, 1: 3}),
    ):
        for sign in (-1, 1):
            physical_projector = projector_from_involution(record_z, sign)
            parity_projector = projector_from_involution(parity, sign)
            close(
                physical_projector @ path_isometry,
                path_isometry @ parity_projector,
                f"bridge conditional map {label} sign={sign}",
            )
            require(matrix_rank(physical_projector) == 4, f"bridge code rank {label} sign={sign}")
            fixed_dimension = matrix_rank(number_two @ parity_projector)
            require(
                fixed_dimension == expected_dimensions[sign],
                f"fixed-N bridge dimension {label} sign={sign}: {fixed_dimension}",
            )

    even_left = basis_vector(fock, 0b0011)
    odd_left = basis_vector(fock, 0b0101)
    for state, certain_sign in ((even_left, 1), (odd_left, -1)):
        physical_state = path_isometry @ state
        certain = float(
            np.vdot(physical_state, projector_from_involution(central_z, certain_sign) @ physical_state).real
        )
        impossible = float(
            np.vdot(physical_state, projector_from_involution(central_z, -certain_sign) @ physical_state).real
        )
        require(abs(certain - 1.0) <= ATOL and abs(impossible) <= ATOL, "deterministic/zero bridge outcome")

    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    cycle = (0, 1, 2, 3, 0)
    square_isometry = code_isometry(square, fock, (cycle,))
    old_edge = (0, 3)
    new_edge = (1, 2)
    old_z_operator = square.edge_z(old_edge)
    new_z_operator = square.edge_z(new_edge)
    component_parity = fock.vertex_parities[0] @ fock.vertex_parities[1]
    state = fixed_number_vector(fock, 2)
    nonzero_joint_probabilities = []
    for old_sign in (-1, 1):
        old_projector = projector_from_involution(old_z_operator, old_sign)
        require(matrix_rank(old_projector) == 8, "first nonbridge history rank")
        close(
            (new_z_operator - old_sign * square.vertex_parity(0) @ square.vertex_parity(1))
            @ old_projector
            @ square_isometry,
            np.zeros((16, 8), dtype=complex),
            f"old-boundary bridge sign old={old_sign}",
        )
        for new_sign in (-1, 1):
            new_projector = projector_from_involution(new_z_operator, new_sign)
            parity_sign = new_sign * old_sign
            parity_projector = projector_from_involution(component_parity, parity_sign)
            history_map = new_projector @ old_projector @ square_isometry
            close(
                history_map,
                old_projector @ square_isometry @ parity_projector,
                f"two-event signed parity old={old_sign} new={new_sign}",
            )
            require(matrix_rank(history_map) == 4, "bridge history code rank")
            close(
                old_z_operator @ history_map,
                old_sign * history_map,
                "old Record permanence",
            )
            probability = float(np.linalg.norm(history_map @ state) ** 2)
            require(probability > 1.0e-4, "generic history unexpectedly has zero probability")
            nonzero_joint_probabilities.append(probability)
            parity_basis = range_basis(parity_projector)
            faithful_map = math.sqrt(2.0) * history_map @ parity_basis
            close(
                faithful_map.conj().T @ faithful_map,
                np.eye(4),
                "history faithful isometry",
            )
            surviving = ((0, 1), (2, 3))
            restricted = restricted_generators(fock, surviving, parity_basis)
            require(commutant_nullity(restricted) == 1, "split surviving algebra not full on branch")
            physical_generators = [square.vertex_parity(v) for v in range(4)] + [
                square.edge_generator(*edge) for edge in surviving
            ]
            fock_generators = list(fock.vertex_parities) + [
                fock.edge_generators[edge] for edge in surviving
            ]
            for physical_generator, fock_generator in zip(physical_generators, fock_generators):
                close(
                    physical_generator @ faithful_map,
                    faithful_map @ (parity_basis.conj().T @ fock_generator @ parity_basis),
                    "two-event full surviving generator",
                )
    require(abs(sum(nonzero_joint_probabilities) - 1.0) <= ATOL, "joint history normalization")
    return "2+2, 1+3, deterministic, zero, and signed old-boundary branches verified"


def run_checks() -> int:
    checks = [
        ("direct_dictionary", direct_dictionary_check),
        ("nonbridge_instrument", nonbridge_instrument_check),
        ("bridge_and_history", bridge_and_history_check),
    ]
    passed = 0
    failed = 0
    for name, function in checks:
        try:
            detail = function()
            print(f"PASS {name}: {detail}")
            passed += 1
        except Exception as error:  # deliberate runner boundary
            print(f"FAIL {name}: {type(error).__name__}: {error}")
            failed += 1
    source_bytes = pathlib.Path(__file__).read_bytes()
    print(f"source_sha256={hashlib.sha256(source_bytes).hexdigest()}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(run_checks())
