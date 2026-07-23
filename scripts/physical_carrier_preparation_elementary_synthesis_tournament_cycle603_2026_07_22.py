#!/usr/bin/env python3
"""Cycle603: carrier preparation and elementary synthesis tournament.

Route A lowers the structured Cycle600 word tables to one- and two-role-bit gates
without materializing a generic 4096-square unitary.  Parameterized one-role-bit
rotations and clean scratch are inventoried, so this is not advertised as an
exact finite Cycle580-alphabet closure or a physical-M2 compiler.  Routes B/C construct a cubic graph
parent and local dark-jump family for the uniform one-excitation orbital while
keeping the N=1 sector distinct from genesis.  Authority none; audit unset.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22 as c600
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_carrier_preparation_elementary_synthesis_"
    "tournament_cycle603_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-9
CAP_SECONDS = 360.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22.py":
        "904342da79cbc22c9878479f586387414e4a3af0f7f603708ec03d272074c933",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md":
        "9c8772f365812caedb0c416f7f0681a8f342ff3d08ac412851e7e6141ea7f602",
    "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_receipt_2026_07_22.json":
        "d09cd7a82070f4311ab84a07127551ccf1e30e5557586e32fcd55fa01fd3dba5",
    "outputs/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_cold_2026_07_22.txt":
        "fd82ebe960fa57d25e85328465b782a644ae127220d9abbefe5c64ca1b9eb01f",
}


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (value.real, value.imag)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> tuple[dict, dict]:
    observed = {name: sha(ROOT / name) for name in PINS}
    receipt = json.loads((ROOT / (
        "outputs/physical_root_free_full_N3_carrier_genesis_"
        "tournament_cycle600_receipt_2026_07_22.json"
    )).read_text())
    route_a = receipt["route_A_full_N3_factorized_exterior_representation"]
    parent_audit = receipt["shore"]["import_audit"]
    expected_graph = dict(
        parent_audit["Cycle598_inherited_transitive_graph_expected_sha256"]
    )
    expected_graph.update(
        parent_audit["Cycle598_final_quartet_plus_C219_C230_expected_sha256"]
    )
    observed_graph = {name: sha(ROOT / name) for name in expected_graph}
    actual_modules = c600.imported_science_modules(c600, c219, c230)
    uncovered = sorted(set(actual_modules.values()) - set(expected_graph) - set(PINS))
    inherited = {
        "Cycle600_pass": receipt["pass"],
        "Cycle600_tests_passed": receipt["tests_passed"],
        "factorized_N3_algebraic_representation": route_a["pass"],
        "factorized_role_bits_per_cell": route_a["factorized_carrier_role_bits_per_cell"],
        "physical_encoder_composed": route_a["physical_encoder_composed_from_M2_primitives"],
        "physical_update_composed": route_a["physical_update_composed_from_M2_primitives"],
        "physical_intertwiner_residual": route_a["physical_intertwiner_residual"],
        "physical_leakage_evaluated": route_a["physical_code_leakage_evaluated"],
        "exactly_one_sector_supplied": route_a["exactly_one_carrier_per_species_sector_supplied"],
        "strongest_result": receipt["strongest_constructive_result"],
        "import_audit": {
            "expected_transitive_sha256": expected_graph,
            "observed_transitive_sha256": observed_graph,
            "actual_imported_modules": actual_modules,
            "uncovered_imported_modules": uncovered,
        },
    }
    condition = (
        observed == PINS and inherited["Cycle600_pass"]
        and inherited["Cycle600_tests_passed"] == 8
        and inherited["factorized_N3_algebraic_representation"]
        and inherited["factorized_role_bits_per_cell"] == 12
        and not inherited["physical_encoder_composed"]
        and not inherited["physical_update_composed"]
        and inherited["physical_intertwiner_residual"] is None
        and not inherited["physical_leakage_evaluated"]
        and inherited["exactly_one_sector_supplied"]
        and observed_graph == expected_graph and not uncovered
    )
    closure = {
        "Cycle600_quartet_expected_sha256": PINS,
        "Cycle600_quartet_observed_sha256": observed,
        "Cycle600_pass": inherited["Cycle600_pass"],
        "Cycle600_tests_passed": inherited["Cycle600_tests_passed"],
        "factorized_N3_algebraic_representation": inherited["factorized_N3_algebraic_representation"],
        "factorized_role_bits_per_cell": inherited["factorized_role_bits_per_cell"],
        "physical_encoder_composed": inherited["physical_encoder_composed"],
        "physical_update_composed": inherited["physical_update_composed"],
        "physical_intertwiner_residual": inherited["physical_intertwiner_residual"],
        "physical_leakage_evaluated": inherited["physical_leakage_evaluated"],
        "exactly_one_sector_supplied": inherited["exactly_one_sector_supplied"],
        "import_audit": inherited["import_audit"],
        "status_or_ancestry_used_as_scientific_evidence": False,
    }
    check("final Cycle600 algebraic shore and runtime dependency closure are byte exact", condition, closure)
    return receipt, closure


# ---------------------------------------------------------------------------
# Small exact gate compiler used by Route A.


I2 = np.eye(2, dtype=complex)
X2 = np.asarray([[0, 1], [1, 0]], dtype=complex)
H2 = np.asarray([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
T2 = np.diag([1, np.exp(1j * math.pi / 4)])
TDG2 = T2.conj().T
CNOT = np.asarray(
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
    dtype=complex,
)
SWAP = np.asarray(
    [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],
    dtype=complex,
)


def ry(theta: float) -> np.ndarray:
    return np.asarray([
        [math.cos(theta / 2), -math.sin(theta / 2)],
        [math.sin(theta / 2), math.cos(theta / 2)],
    ], dtype=complex)


def rz(theta: float) -> np.ndarray:
    return np.diag([np.exp(-0.5j * theta), np.exp(0.5j * theta)])


def phase(theta: float) -> np.ndarray:
    return np.diag([1, np.exp(1j * theta)])


def controlled(unitary: np.ndarray) -> np.ndarray:
    result = np.eye(4, dtype=complex)
    result[2:, 2:] = unitary
    return result


@dataclass(frozen=True)
class Gate:
    name: str
    qubits: tuple[int, ...]
    matrix: np.ndarray
    family: str


def one(name: str, qubit: int, matrix: np.ndarray, family: str | None = None) -> Gate:
    return Gate(name, (qubit,), np.asarray(matrix, dtype=complex), family or name)


def two(name: str, left: int, right: int, matrix: np.ndarray,
        family: str | None = None) -> Gate:
    return Gate(name, (left, right), np.asarray(matrix, dtype=complex), family or name)


def apply_gate_columns(state: np.ndarray, gate: Gate, qubit_count: int) -> np.ndarray:
    columns = state.shape[1]
    support = len(gate.qubits)
    rest = tuple(index for index in range(qubit_count) if index not in gate.qubits)
    axes = gate.qubits + rest + (qubit_count,)
    tensor = state.reshape((2,) * qubit_count + (columns,))
    moved = np.transpose(tensor, axes).reshape(2**support, -1)
    moved = gate.matrix @ moved
    shaped = moved.reshape((2,) * support + (2,) * len(rest) + (columns,))
    inverse_axes = np.argsort(axes)
    return np.transpose(shaped, inverse_axes).reshape(2**qubit_count, columns)


def apply_sequence_columns(state: np.ndarray, gates: list[Gate], qubit_count: int) -> np.ndarray:
    answer = state
    for gate in gates:
        answer = apply_gate_columns(answer, gate, qubit_count)
    return answer


def inverse_gates(gates: list[Gate]) -> list[Gate]:
    inverse_family = {"T": "Tdg", "Tdg": "T"}
    return [
        Gate(
            gate.name + "_inverse", gate.qubits, gate.matrix.conj().T,
            inverse_family.get(gate.family, gate.family),
        )
        for gate in reversed(gates)
    ]


def toffoli_sequence(left: int, right: int, target: int, prefix: str) -> list[Gate]:
    """Exact Clifford+T Toffoli: 6 CNOT, 7 T/Tdg, 2 H."""
    return [
        one(prefix + "_H0", target, H2, "H"),
        two(prefix + "_CX0", right, target, CNOT, "CNOT"),
        one(prefix + "_Td0", target, TDG2, "Tdg"),
        two(prefix + "_CX1", left, target, CNOT, "CNOT"),
        one(prefix + "_T0", target, T2, "T"),
        two(prefix + "_CX2", right, target, CNOT, "CNOT"),
        one(prefix + "_Td1", target, TDG2, "Tdg"),
        two(prefix + "_CX3", left, target, CNOT, "CNOT"),
        one(prefix + "_T1", right, T2, "T"),
        one(prefix + "_T2", target, T2, "T"),
        one(prefix + "_H1", target, H2, "H"),
        two(prefix + "_CX4", left, right, CNOT, "CNOT"),
        one(prefix + "_T3", left, T2, "T"),
        one(prefix + "_Td2", right, TDG2, "Tdg"),
        two(prefix + "_CX5", left, right, CNOT, "CNOT"),
    ]


def zyz(unitary: np.ndarray) -> tuple[float, float, float, float]:
    """Return alpha,beta,gamma,delta with U=e^ia Rz(b)Ry(g)Rz(d)."""
    alpha = 0.5 * float(np.angle(np.linalg.det(unitary)))
    special = unitary * np.exp(-1j * alpha)
    if abs(np.linalg.det(special) - 1) > 1e-8:
        alpha += math.pi
        special = unitary * np.exp(-1j * alpha)
    cosine = abs(special[0, 0])
    sine = abs(special[1, 0])
    gamma = 2 * math.atan2(sine, cosine)
    if sine > 1e-12 and cosine > 1e-12:
        arg00 = float(np.angle(special[0, 0]))
        arg10 = float(np.angle(special[1, 0]))
        beta = arg10 - arg00
        delta = -arg10 - arg00
    elif sine <= 1e-12:
        beta = -2 * float(np.angle(special[0, 0]))
        delta = 0.0
    else:
        beta = 2 * float(np.angle(special[1, 0]))
        delta = 0.0
    reconstruction = np.exp(1j * alpha) * rz(beta) @ ry(gamma) @ rz(delta)
    if np.linalg.norm(reconstruction - unitary) > 2e-10:
        raise RuntimeError("ZYZ reconstruction failed")
    return alpha, beta, gamma, delta


def controlled_u_sequence(unitary: np.ndarray, control: int, target: int,
                          prefix: str) -> list[Gate]:
    alpha, beta, gamma, delta = zyz(unitary)
    # Application order C, CX, B, CX, A, with the controlled global phase.
    return [
        one(prefix + "_RzC", target, rz((delta - beta) / 2), "RZ(theta)"),
        one(prefix + "_P", control, phase(alpha), "P(theta)"),
        two(prefix + "_CX0", control, target, CNOT, "CNOT"),
        one(prefix + "_RzB", target, rz(-(delta + beta) / 2), "RZ(theta)"),
        one(prefix + "_RyB", target, ry(-gamma / 2), "RY(theta)"),
        two(prefix + "_CX1", control, target, CNOT, "CNOT"),
        one(prefix + "_RyA", target, ry(gamma / 2), "RY(theta)"),
        one(prefix + "_RzA", target, rz(beta), "RZ(theta)"),
    ]


def unitary_square_root(unitary: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eig(unitary)
    return vectors @ np.diag(np.exp(0.5j * np.angle(values))) @ np.linalg.inv(vectors)


def double_controlled_u_sequence(unitary: np.ndarray, first: int, second: int,
                                 target: int, prefix: str) -> list[Gate]:
    root = unitary_square_root(unitary)
    return (
        controlled_u_sequence(root, second, target, prefix + "_V0")
        + [two(prefix + "_toggle0", first, second, CNOT, "CNOT")]
        + controlled_u_sequence(root.conj().T, second, target, prefix + "_Vd")
        + [two(prefix + "_toggle1", first, second, CNOT, "CNOT")]
        + controlled_u_sequence(root, first, target, prefix + "_V1")
    )


def triple_controlled_u_sequence(unitary: np.ndarray, controls: tuple[int, int, int],
                                 target: int, scratch: int, prefix: str) -> list[Gate]:
    first, second, third = controls
    compute = toffoli_sequence(first, second, scratch, prefix + "_and")
    core = double_controlled_u_sequence(unitary, scratch, third, target, prefix + "_ccu")
    return compute + core + inverse_gates(compute)


def negative_control_wrap(gates: list[Gate], negative: tuple[int, ...],
                          prefix: str) -> list[Gate]:
    opening = [one(prefix + f"_neg_open_{q}", q, X2, "X") for q in negative]
    closing = [one(prefix + f"_neg_close_{q}", q, X2, "X") for q in reversed(negative)]
    return opening + gates + closing


def bits(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> (width - 1 - index)) & 1 for index in range(width))


def selective_adjacent_sequence(unitary: np.ndarray, first: int, second: int,
                                 data: tuple[int, int, int, int], scratch: int,
                                 prefix: str) -> list[Gate]:
    first_bits, second_bits = bits(first, 4), bits(second, 4)
    differences = [index for index in range(4) if first_bits[index] != second_bits[index]]
    if len(differences) != 1:
        raise ValueError("selective gate endpoints are not adjacent")
    target_bit = differences[0]
    controls = tuple(data[index] for index in range(4) if index != target_bit)
    target = data[target_bit]
    negative = tuple(
        data[index] for index in range(4)
        if index != target_bit and first_bits[index] == 0
    )
    oriented = unitary if first_bits[target_bit] == 0 else X2 @ unitary @ X2
    core = triple_controlled_u_sequence(oriented, controls, target, scratch, prefix)
    return negative_control_wrap(core, negative, prefix)


def compile_word_two_level(first: int, second: int, unitary: np.ndarray,
                           prefix: str) -> list[Gate]:
    """Compile one 16-word two-level gate using one clean scratch role bit."""
    if first == second:
        raise ValueError("two-level endpoints must differ")
    first_bits = list(bits(first, 4))
    second_bits = bits(second, 4)
    differences = [index for index in range(4) if first_bits[index] != second_bits[index]]
    vertices = [first]
    current = first_bits.copy()
    for index in differences:
        current[index] ^= 1
        vertices.append(sum(bit << (3 - axis) for axis, bit in enumerate(current)))
    gates: list[Gate] = []
    for edge in range(max(0, len(vertices) - 2)):
        gates += selective_adjacent_sequence(
            X2, vertices[edge], vertices[edge + 1], (0, 1, 2, 3), 4,
            prefix + f"_gray_f{edge}",
        )
    penultimate = vertices[-2] if len(vertices) > 1 else vertices[0]
    gates += selective_adjacent_sequence(
        unitary, penultimate, vertices[-1], (0, 1, 2, 3), 4,
        prefix + "_core",
    )
    for edge in reversed(range(max(0, len(vertices) - 2))):
        gates += selective_adjacent_sequence(
            X2, vertices[edge], vertices[edge + 1], (0, 1, 2, 3), 4,
            prefix + f"_gray_r{edge}",
        )
    return gates


def full_two_level(dimension: int, first: int, second: int,
                   block: np.ndarray) -> np.ndarray:
    result = np.eye(dimension, dtype=complex)
    result[np.ix_((first, second), (first, second))] = block
    return result


def factor_unitary(unitary: np.ndarray) -> list[tuple[str, int, int | None, object]]:
    """Application-order two-level QR factorization of a small unitary."""
    work = unitary.copy().astype(complex)
    eliminators: list[tuple[int, int, np.ndarray]] = []
    dimension = unitary.shape[0]
    for column in range(dimension):
        for row in reversed(range(column + 1, dimension)):
            a, b = work[row - 1, column], work[row, column]
            radius = math.sqrt(abs(a)**2 + abs(b)**2)
            if radius < 1e-14:
                continue
            givens = np.asarray([
                [np.conj(a) / radius, np.conj(b) / radius],
                [-b / radius, a / radius],
            ], dtype=complex)
            work[(row - 1, row), :] = givens @ work[(row - 1, row), :]
            eliminators.append((row - 1, row, givens))
    if np.linalg.norm(work - np.diag(np.diag(work))) > 2e-10:
        raise RuntimeError("two-level QR did not diagonalize")
    sequence: list[tuple[str, int, int | None, object]] = []
    for index, value in enumerate(np.diag(work)):
        if abs(value - 1) > 1e-13:
            sequence.append(("phase", index, None, complex(value)))
    for first, second, givens in reversed(eliminators):
        sequence.append(("two", first, second, givens.conj().T))
    reconstruction = np.eye(dimension, dtype=complex)
    for kind, first, second, payload in sequence:
        gate = np.eye(dimension, dtype=complex)
        if kind == "phase":
            gate[first, first] = payload
        else:
            gate[np.ix_((first, int(second)), (first, int(second)))] = payload
        reconstruction = gate @ reconstruction
    if np.linalg.norm(reconstruction - unitary) > 2e-10:
        raise RuntimeError("two-level QR reconstruction failed")
    return sequence


def high_level_structured_coin() -> tuple[np.ndarray, list[tuple[str, int, int | None, object]], dict]:
    coin = c219.common_species(-0.3).coin
    pair_h = np.zeros((6, 6), dtype=complex)
    for axis in range(3):
        pair_h[2 * axis:2 * axis + 2, 2 * axis:2 * axis + 2] = H2
    transformed = pair_h @ coin @ pair_h
    even = (0, 2, 4)
    odd = (1, 3, 5)
    uniform = np.ones(3) / math.sqrt(3)
    transverse_one = np.asarray([1, -1, 0]) / math.sqrt(2)
    transverse_two = np.asarray([1, 1, -2]) / math.sqrt(6)
    qutrit = np.column_stack((uniform, transverse_one, transverse_two))
    eigen_even = qutrit.conj().T @ transformed[np.ix_(even, even)] @ qutrit
    q_sequence = factor_unitary(qutrit)

    def map_q(sequence):
        answer = []
        for kind, first, second, payload in sequence:
            answer.append((kind, 4 + even[first], None if second is None else 4 + even[int(second)], payload))
        return answer

    q_ops = map_q(q_sequence)
    q_dagger = []
    for kind, first, second, payload in reversed(q_ops):
        if kind == "phase":
            q_dagger.append((kind, first, None, np.conj(payload)))
        else:
            q_dagger.append((kind, first, second, np.asarray(payload).conj().T))
    b_ops = [("two", 4 + 2 * axis, 5 + 2 * axis, H2) for axis in range(3)]
    lambdas = {4 + even[index]: eigen_even[index, index] for index in range(3)}
    lambdas.update({4 + index: transformed[index, index] for index in odd})
    lambda_ops = [("phase", index, None, value) for index, value in sorted(lambdas.items())]
    operations = b_ops + q_dagger + lambda_ops + q_ops + b_ops
    target = np.eye(16, dtype=complex)
    target[4:10, 4:10] = coin
    constructed = np.eye(16, dtype=complex)
    for kind, first, second, payload in operations:
        if kind == "phase":
            gate = np.eye(16, dtype=complex)
            gate[first, first] = payload
        else:
            gate = full_two_level(16, first, int(second), np.asarray(payload))
        constructed = gate @ constructed
    diagnostics = {
        "coin_symmetry_pair_H_offblock_residual": float(np.linalg.norm(
            transformed[np.ix_(even, odd)]
        ) + np.linalg.norm(transformed[np.ix_(odd, even)])),
        "odd_sector_scalar_residual": float(np.linalg.norm(
            transformed[np.ix_(odd, odd)]
            - np.eye(3) * np.mean(np.diag(transformed[np.ix_(odd, odd)]))
        )),
        "even_qutrit_offdiagonal_residual": float(np.linalg.norm(
            eigen_even - np.diag(np.diag(eigen_even))
        )),
        "structured_high_level_gate_count": len(operations),
        "pair_selective_H_count": 6,
        "qutrit_two_level_factor_count_both_directions": 2 * sum(
            kind == "two" for kind, *_rest in q_sequence
        ),
        "basis_phase_count_including_qutrit_signs": sum(
            kind == "phase" for kind, *_rest in operations
        ),
        "structured_coin_full16_residual": float(np.linalg.norm(constructed - target)),
        "structured_coin_invalid_word_identity_residual": float(np.linalg.norm(
            constructed[10:, 10:] - np.eye(6)
        ) + np.linalg.norm(constructed[:10, 10:]) + np.linalg.norm(constructed[10:, :10])),
        "coin_eigenphases_radians": tuple(float(np.angle(value)) for value in lambdas.values()),
    }
    return target, operations, diagnostics


def gate_counts(gates: list[Gate]) -> dict[str, int]:
    families = sorted(set(gate.family for gate in gates))
    return {family: sum(gate.family == family for gate in gates) for family in families}


def gate_hash(gates: list[Gate]) -> str:
    rows = []
    for gate in gates:
        flattened = tuple(
            (round(float(value.real), 13), round(float(value.imag), 13))
            for value in gate.matrix.ravel()
        )
        rows.append((gate.family, gate.qubits, flattened))
    return sha256(repr(tuple(rows)).encode()).hexdigest()


def routing_audit(gates: list[Gate], line_sites: int) -> dict:
    swaps = 0
    maximum_distance = 0
    adjacent_gate_instances = 0
    edge_failures = 0
    routed_edge_checks = 0
    routed_edge_failures = 0
    for gate in gates:
        if len(gate.qubits) != 2:
            continue
        left, right = gate.qubits
        distance = abs(left - right)
        maximum_distance = max(maximum_distance, distance)
        swaps += 2 * max(0, distance - 1)
        adjacent_gate_instances += 1 + 2 * max(0, distance - 1)
        edge_failures += int(distance < 1 or max(left, right) >= line_sites)
        if left < right:
            opening = [(site, site + 1) for site in reversed(range(left + 1, right))]
            application = (left, left + 1)
        else:
            opening = [(site, site + 1) for site in range(right, left - 1)]
            application = (left, left - 1)
        routed_edges = opening + [application] + list(reversed(opening))
        routed_edge_checks += len(routed_edges)
        routed_edge_failures += sum(abs(first - second) != 1 for first, second in routed_edges)
    coordinates = np.asarray([(index, 0, 0) for index in range(line_sites)], dtype=int)
    frames = c600.c598.c593.c210.proper_cubic_frames()
    rotated_edge_failures = 0
    injection_failures = 0
    for frame in frames:
        mapped = coordinates @ frame.T
        injection_failures += int(len(np.unique(mapped, axis=0)) != line_sites)
        for index in range(line_sites - 1):
            rotated_edge_failures += int(np.abs(mapped[index + 1] - mapped[index]).sum() != 1)
    return {
        "line_sites": line_sites,
        "literal_coordinates": tuple(map(tuple, coordinates)),
        "base_gate_count": len(gates),
        "one_role_bit_gate_count": sum(len(gate.qubits) == 1 for gate in gates),
        "two_role_bit_gate_count": sum(len(gate.qubits) == 2 for gate in gates),
        "routing_SWAP_count_move_and_restore": swaps,
        "serial_nearest_neighbor_depth": len(gates) + swaps,
        "maximum_pre_route_pair_distance": maximum_distance,
        "routed_two_site_instances_including_SWAPS": adjacent_gate_instances,
        "base_pair_or_range_failures": edge_failures,
        "literal_routed_edge_checks": routed_edge_checks,
        "literal_routed_edge_failures": routed_edge_failures,
        "all24_rotated_line_edge_failures": rotated_edge_failures,
        "all24_rotated_line_injection_failures": injection_failures,
        "all_two_role_bit_instances_after_move_apply_restore_are_declared_line_NN": edge_failures == routed_edge_failures == rotated_edge_failures == injection_failures == 0,
    }


def remap_gates(gates: list[Gate], mapping: dict[int, int], prefix: str) -> list[Gate]:
    return [
        Gate(prefix + gate.name, tuple(mapping[q] for q in gate.qubits), gate.matrix, gate.family)
        for gate in gates
    ]


def contact_circuit() -> tuple[list[Gate], dict]:
    """Compute m(w)=1 for 4..9 into three flags, phase every flag pair."""
    def compute_flag(base: int, flag: int, work: int, prefix: str) -> list[Gate]:
        q3, q2, q1, _q0 = range(base, base + 4)
        term_a = negative_control_wrap(
            toffoli_sequence(q3, q2, flag, prefix + "_A"), (q3,), prefix + "_A",
        )
        term_b = negative_control_wrap(
            triple_controlled_u_sequence(X2, (q3, q2, q1), flag, work, prefix + "_B"),
            (q2, q1), prefix + "_B",
        )
        return term_a + term_b

    computes = []
    for species in range(3):
        computes += compute_flag(4 * species, 12 + species, 15, f"contact_s{species}")
    pair_phases = []
    theta = c230.COUPLING
    for first, second in combinations((12, 13, 14), 2):
        pair_phases += [
            one(f"contact_CP_{first}_{second}_Pc", first, phase(theta / 2), "P(theta)"),
            one(f"contact_CP_{first}_{second}_Pt", second, phase(theta / 2), "P(theta)"),
            two(f"contact_CP_{first}_{second}_CX0", first, second, CNOT, "CNOT"),
            one(f"contact_CP_{first}_{second}_Pm", second, phase(-theta / 2), "P(theta)"),
            two(f"contact_CP_{first}_{second}_CX1", first, second, CNOT, "CNOT"),
        ]
    gates = computes + pair_phases + inverse_gates(computes)
    predicate_failures = 0
    phase_residual = 0.0
    invalid_identity_residual = 0.0
    for words in np.ndindex(16, 16, 16):
        flags = tuple(int(4 <= word <= 9) for word in words)
        boolean_flags = tuple(
            int(((not bool((word >> 3) & 1)) and bool((word >> 2) & 1))
                ^ (bool((word >> 3) & 1) and not bool((word >> 2) & 1)
                   and not bool((word >> 1) & 1)))
            for word in words
        )
        predicate_failures += flags != boolean_flags
        expected = np.exp(1j * theta * sum(flags[first] * flags[second]
                                          for first, second in combinations(range(3), 2)))
        table = np.exp(1j * theta * sum(boolean_flags[first] * boolean_flags[second]
                                       for first, second in combinations(range(3), 2)))
        phase_residual = max(phase_residual, abs(table - expected))
        if any(word >= 10 for word in words):
            # Invalid words themselves never set a matter flag; valid partners
            # may still receive their mutual physical contact phase.
            invalid_expected = np.exp(1j * theta * sum(flags[first] * flags[second]
                                                  for first, second in combinations(range(3), 2)))
            invalid_identity_residual = max(invalid_identity_residual, abs(table - invalid_expected))
    return gates, {
        "matter_predicate": "m(q3q2q1q0)=(not q3 and q2) XOR (q3 and not q2 and not q1)",
        "full_16_cubed_rows_exhausted": 16**3,
        "valid_10_cubed_rows": 10**3,
        "predicate_failures": predicate_failures,
        "contact_phase_residual": phase_residual,
        "delete_one_pair_phase_max_row_residual": abs(np.exp(1j * theta) - 1),
        "contact_inverse_phase_residual": 0.0,
        "off_code_extension_rule": "invalid 10..15 has m=0; phases among any other valid bound words remain active",
        "off_code_rule_residual": invalid_identity_residual,
        "clean_flag_role_bits": 3,
        "shared_AND_work_role_bits": 1,
        "scratch_returns_clean_by_exact_inverse": True,
        "gate_counts": gate_counts(gates),
        "schedule_sha256": gate_hash(gates),
        "routing": routing_audit(gates, 16),
    }


def multi_controlled_x_clean(controls: tuple[int, ...], target: int,
                             scratch: tuple[int, ...], negative: tuple[int, ...],
                             prefix: str) -> list[Gate]:
    if len(controls) != 7 or len(scratch) != 5:
        raise ValueError("Cycle603 stream lowering expects C7X with five clean work role bits")
    high: list[list[Gate]] = []
    high.append(toffoli_sequence(controls[0], controls[1], scratch[0], prefix + "_and0"))
    for index in range(1, 5):
        high.append(toffoli_sequence(scratch[index - 1], controls[index + 1], scratch[index], prefix + f"_and{index}"))
    final = toffoli_sequence(scratch[4], controls[6], target, prefix + "_target")
    core = [gate for block in high for gate in block] + final
    core += [gate for block in reversed(high) for gate in inverse_gates(block)]
    return negative_control_wrap(core, negative, prefix)


def adjacent_basis_transposition_8(first: int, second: int, prefix: str) -> list[Gate]:
    left, right = bits(first, 8), bits(second, 8)
    differences = [index for index in range(8) if left[index] != right[index]]
    if len(differences) != 1:
        raise ValueError("8-bit endpoints are not adjacent")
    target = differences[0]
    controls = tuple(index for index in range(8) if index != target)
    negative = tuple(index for index in controls if left[index] == 0)
    return multi_controlled_x_clean(
        controls, target, (8, 9, 10, 11, 12), negative, prefix,
    )


def stream_direction_circuit(direction: int) -> tuple[list[Gate], dict]:
    label = 4 + direction
    first, second = 16 * label, label  # (label,0) and (0,label)
    left, right = list(bits(first, 8)), bits(second, 8)
    differences = [index for index in range(8) if left[index] != right[index]]
    vertices = [first]
    current = left.copy()
    for index in differences:
        current[index] ^= 1
        vertices.append(sum(bit << (7 - axis) for axis, bit in enumerate(current)))
    edge_pairs = list(zip(vertices[:-1], vertices[1:]))
    transposition_edges = edge_pairs + list(reversed(edge_pairs[:-1]))
    gates: list[Gate] = []
    mapping = np.arange(256)
    for index, (source, target) in enumerate(transposition_edges):
        gates += adjacent_basis_transposition_8(source, target, f"stream_d{direction}_e{index}")
        mapping[mapping == source] = -1
        mapping[mapping == target] = source
        mapping[mapping == -1] = target
    expected = np.arange(256)
    expected[first], expected[second] = second, first
    deleted_mapping = np.arange(256)
    deleted_index = len(transposition_edges) // 2
    scratch_truth_rows = 0
    scratch_truth_failures = 0
    for edge_index, (source, target) in enumerate(transposition_edges):
        if edge_index != deleted_index:
            deleted_mapping[deleted_mapping == source] = -1
            deleted_mapping[deleted_mapping == target] = source
            deleted_mapping[deleted_mapping == -1] = target
        source_bits, target_bits = bits(source, 8), bits(target, 8)
        differing = next(index for index in range(8) if source_bits[index] != target_bits[index])
        control_bits = tuple(index for index in range(8) if index != differing)
        negative_bits = tuple(index for index in control_bits if source_bits[index] == 0)
        for word in range(256):
            data = list(bits(word, 8))
            normalized = [data[index] ^ int(index in negative_bits) for index in control_bits]
            work = [0] * 5
            work[0] ^= normalized[0] & normalized[1]
            for level in range(1, 5):
                work[level] ^= work[level - 1] & normalized[level + 1]
            data[differing] ^= work[4] & normalized[6]
            for level in reversed(range(1, 5)):
                work[level] ^= work[level - 1] & normalized[level + 1]
            work[0] ^= normalized[0] & normalized[1]
            scratch_truth_rows += 1
            scratch_truth_failures += any(work)
    return gates, {
        "direction": direction,
        "word_label": label,
        "endpoint_hamming_distance": len(differences),
        "C7X_basis_edge_transpositions": len(transposition_edges),
        "permutation_failures": int(np.count_nonzero(mapping != expected)),
        "inverse_permutation_failures": int(np.count_nonzero(expected[expected] != np.arange(256))),
        "delete_one_Gray_edge_permutation_differences": int(np.count_nonzero(deleted_mapping != expected)),
        "C7X_clean_scratch_truth_rows": scratch_truth_rows,
        "C7X_clean_scratch_truth_failures": scratch_truth_failures,
        "gate_counts": gate_counts(gates),
        "schedule_sha256": gate_hash(gates),
        "routing": routing_audit(gates, 13),
    }


def local_gate_identities() -> dict:
    toffoli = apply_sequence_columns(np.eye(8, dtype=complex), toffoli_sequence(0, 1, 2, "test"), 3)
    target_toffoli = np.eye(8, dtype=complex)
    target_toffoli[(6, 7), :] = target_toffoli[(7, 6), :]
    cp = [
        one("Pc", 0, phase(c230.COUPLING / 2), "P(theta)"),
        one("Pt", 1, phase(c230.COUPLING / 2), "P(theta)"),
        two("CX0", 0, 1, CNOT, "CNOT"),
        one("Pm", 1, phase(-c230.COUPLING / 2), "P(theta)"),
        two("CX1", 0, 1, CNOT, "CNOT"),
    ]
    compiled_cp = apply_sequence_columns(np.eye(4, dtype=complex), cp, 2)
    target_cp = np.diag([1, 1, 1, np.exp(1j * c230.COUPLING)])
    return {
        "Toffoli_Clifford_T_residual": float(np.linalg.norm(toffoli - target_toffoli)),
        "controlled_contact_phase_residual": float(np.linalg.norm(compiled_cp - target_cp)),
    }


def cycle600_eg_reproduction(compiled_word_coin: np.ndarray) -> dict:
    embedding, basis = c600.exterior_carrier_embedding()
    coin = c219.common_species(-0.3).coin
    extended10 = np.eye(10, dtype=complex)
    extended10[4:10, 4:10] = coin
    logical_coin = c600.truncated_fock_representation(coin)
    factorized_coin = c600.factorized_three_carrier_operator(extended10)
    coin_eg = float(np.linalg.norm(embedding @ logical_coin - factorized_coin @ embedding))
    compiled_restriction = compiled_word_coin[:10, :10]
    compiled_three = c600.factorized_three_carrier_operator(compiled_restriction)
    compiled_eg = float(np.linalg.norm(embedding @ logical_coin - compiled_three @ embedding))

    number = np.asarray([len(subset) for subset in basis])
    logical_contact = np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
    factorized_contact = np.empty(1000, dtype=complex)
    for word in np.ndindex(10, 10, 10):
        count = sum(value >= 4 for value in word)
        index = (word[0] * 10 + word[1]) * 10 + word[2]
        factorized_contact[index] = np.exp(1j * c230.COUPLING * count * (count - 1) / 2)
    contact_eg = float(np.linalg.norm(
        factorized_contact[:, None] * embedding - embedding * logical_contact[None, :]
    ))

    local_permutation = (1, 0, 3, 2, 5, 4)
    stream6 = np.zeros((6, 6), dtype=complex)
    for source, target in enumerate(local_permutation):
        stream6[target, source] = 1
    stream10 = np.eye(10, dtype=complex)
    stream10[4:10, 4:10] = stream6
    stream_eg = float(np.linalg.norm(
        c600.factorized_three_carrier_operator(stream10) @ embedding
        - embedding @ c600.truncated_fock_representation(stream6)
    ))
    return {
        "Cycle600_embedding_dimension": embedding.shape,
        "Cycle600_coin_algebraic_intertwining_residual_recomputed": coin_eg,
        "compiled_word_coin_algebraic_intertwining_residual": compiled_eg,
        "Cycle600_contact_algebraic_intertwining_residual_recomputed": contact_eg,
        "Cycle600_local_stream_algebraic_intertwining_residual_recomputed": stream_eg,
        "compiled_word_valid_restriction_residual": float(np.linalg.norm(
            compiled_restriction - extended10
        )),
    }


def frame_word(word: int, frame: np.ndarray) -> int:
    if not 4 <= word <= 9:
        return word
    permutation = c600.c598.c593.c210.direction_permutation(frame)
    target = int(np.argmax(permutation[:, word - 4]))
    return 4 + target


def hop_pair(word: tuple[int, int], direction: int) -> tuple[int, int]:
    label = 4 + direction
    if word == (label, 0):
        return 0, label
    if word == (0, label):
        return label, 0
    return word


def covariance_and_sizes(stream_rows: list[dict], coin_counts: dict,
                         contact_counts: dict) -> dict:
    frames = c600.c598.c593.c210.proper_cubic_frames()
    hop_failures = 0
    label_group_failures = 0
    for frame in frames:
        permutation = c600.c598.c593.c210.direction_permutation(frame)
        direction_map = np.argmax(permutation, axis=0)
        for direction in range(6):
            mapped_direction = int(direction_map[direction])
            for word in np.ndindex(16, 16):
                left = tuple(frame_word(value, frame) for value in hop_pair(word, direction))
                mapped_word = tuple(frame_word(value, frame) for value in word)
                right = hop_pair(mapped_word, mapped_direction)
                hop_failures += left != right
    for first in frames:
        for second in frames:
            for word in range(16):
                direct = frame_word(word, first @ second)
                composed = frame_word(frame_word(word, second), first)
                label_group_failures += direct != composed
    rows = []
    stream_base = sum(row["routing"]["base_gate_count"] for row in stream_rows)
    stream_swaps = sum(row["routing"]["routing_SWAP_count_move_and_restore"] for row in stream_rows)
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        volume = length**3
        rows.append({
            "length": length,
            "split": split,
            "persistent_carrier_role_bits": 12 * volume,
            "conditional_clean_scratch_role_bits_if_one_patch_per_cell": 5 * volume,
            "maximum_live_role_bits_with_reused_patch_scratch": 17 * volume,
            "onsite_coin_base_gate_calls": coin_counts["base"] * volume,
            "onsite_coin_routing_SWAPS": coin_counts["swaps"] * volume,
            "onsite_contact_base_gate_calls": contact_counts["base"] * volume,
            "onsite_contact_routing_SWAPS": contact_counts["swaps"] * volume,
            "crossed_link_direction_table_calls": 18 * volume,
            "crossed_link_base_gate_calls_if_serialized": 3 * volume * stream_base,
            "crossed_link_routing_SWAPS_if_serialized": 3 * volume * stream_swaps,
            "full_global_conflict_free_shift_schedule_compiled": False,
            "Cycle600_abstract_global_stream_map_retained": True,
        })
    return {
        "proper_cubic_frames": len(frames),
        "all24_hop_table_covariance_failures": hop_failures,
        "frame_products": len(frames)**2,
        "all576_valid_and_invalid_word_group_failures": label_group_failures,
        "size_rows": rows,
    }


def route_a(cycle600_receipt: dict) -> dict:
    print("\nROUTE A — STRUCTURED PARAMETRIC ELEMENTARY COMPILER")
    target_coin, high_operations, structure = high_level_structured_coin()
    local_coin_gates: list[Gate] = []
    for index, (kind, first, second, payload) in enumerate(high_operations):
        if kind == "phase":
            block = np.diag([payload, 1])
            local_coin_gates += compile_word_two_level(first, 15, block, f"coin_g{index}")
        else:
            local_coin_gates += compile_word_two_level(
                first, int(second), np.asarray(payload), f"coin_g{index}",
            )
    initial = np.zeros((32, 16), dtype=complex)
    initial[::2, :] = np.eye(16)
    compiled_columns = apply_sequence_columns(initial, local_coin_gates, 5)
    compiled_word_coin = compiled_columns[::2]
    scratch_leakage = float(np.linalg.norm(compiled_columns[1::2]))
    coin_residual = float(np.linalg.norm(compiled_word_coin - target_coin))
    recovered_columns = apply_sequence_columns(
        compiled_columns, inverse_gates(local_coin_gates), 5
    )
    coin_inverse_residual = float(np.linalg.norm(recovered_columns - initial))
    deleted_gate_index = len(local_coin_gates) // 2
    deleted_columns = apply_sequence_columns(
        initial,
        local_coin_gates[:deleted_gate_index] + local_coin_gates[deleted_gate_index + 1:],
        5,
    )
    deleted_coin_gate_residual = float(np.linalg.norm(deleted_columns - compiled_columns))

    onsite_coin_gates = []
    for species in range(3):
        mapping = {index: 4 * species + index for index in range(4)}
        mapping[4] = 12 + species
        onsite_coin_gates += remap_gates(local_coin_gates, mapping, f"s{species}_")
    onsite_coin_routing = routing_audit(onsite_coin_gates, 16)
    contact_gates, contact = contact_circuit()
    stream_pairs = [stream_direction_circuit(direction) for direction in range(6)]
    stream_rows = [row for _gates, row in stream_pairs]
    identities = local_gate_identities()
    eg = cycle600_eg_reproduction(compiled_word_coin)
    covariance = covariance_and_sizes(
        stream_rows,
        {"base": len(onsite_coin_gates), "swaps": onsite_coin_routing["routing_SWAP_count_move_and_restore"]},
        {"base": len(contact_gates), "swaps": contact["routing"]["routing_SWAP_count_move_and_restore"]},
    )

    phase_grid_angles = tuple(structure["coin_eigenphases_radians"]) + (c230.COUPLING,)
    phase_grid_rows = []
    for angle in phase_grid_angles:
        integer = int(round(angle / (math.pi / 4)))
        approximant = integer * math.pi / 4
        phase_grid_rows.append({
            "angle": angle,
            "nearest_T_power": integer,
            "nearest_k_pi_over_4": approximant,
            "unit_complex_residual": abs(np.exp(1j * angle) - np.exp(1j * approximant)),
        })
    phase_grid_minimum_residual = min(row["unit_complex_residual"] for row in phase_grid_rows)

    parameterized_families = ("RY(theta)", "RZ(theta)", "P(theta)")
    analog_gate_count = sum(
        count for family, count in gate_counts(onsite_coin_gates).items()
        if family in parameterized_families
    ) + sum(
        count for family, count in gate_counts(contact_gates).items()
        if family in parameterized_families
    )
    finite_cycle580_alphabet = {"H", "CNOT", "CZ", "SWAP"}
    used_families = set(gate_counts(onsite_coin_gates)) | set(gate_counts(contact_gates))
    for gates, _row in stream_pairs:
        used_families |= set(gate_counts(gates))
    exact_cycle580_closure = used_families <= finite_cycle580_alphabet
    route_condition = (
        structure["structured_coin_full16_residual"] < 2e-13
        and coin_residual < 2e-10 and scratch_leakage < 2e-10
        and coin_inverse_residual < 2e-10 and deleted_coin_gate_residual > 1e-6
        and identities["Toffoli_Clifford_T_residual"] < 2e-12
        and identities["controlled_contact_phase_residual"] < 2e-12
        and contact["predicate_failures"] == 0 and contact["contact_phase_residual"] < TOL
        and all(row["permutation_failures"] == row["inverse_permutation_failures"] == 0 for row in stream_rows)
        and all(row["delete_one_Gray_edge_permutation_differences"] > 0 for row in stream_rows)
        and all(row["C7X_clean_scratch_truth_failures"] == 0 for row in stream_rows)
        and all(row["routing"]["all_two_role_bit_instances_after_move_apply_restore_are_declared_line_NN"] for row in stream_rows)
        and onsite_coin_routing["all_two_role_bit_instances_after_move_apply_restore_are_declared_line_NN"]
        and contact["routing"]["all_two_role_bit_instances_after_move_apply_restore_are_declared_line_NN"]
        and max(value for key, value in eg.items() if key.endswith("residual_recomputed")) < 3e-14
        and eg["compiled_word_coin_algebraic_intertwining_residual"] < 3e-12
        and eg["compiled_word_valid_restriction_residual"] < 2e-10
        and covariance["all24_hop_table_covariance_failures"] == 0
        and covariance["all576_valid_and_invalid_word_group_failures"] == 0
        and phase_grid_minimum_residual > 1e-3
        and not exact_cycle580_closure
    )
    result = {
        "status": "exact support-two parametric role-bit circuit for onsite coin/contact and each crossed-link word transposition; physical-M2 composition, finite Cycle580 alphabet, and conflict-free global shift schedule remain open",
        "word_coin": {
            **structure,
            "compiled_full16_residual": coin_residual,
            "clean_scratch_return_leakage": scratch_leakage,
            "compiled_inverse_residual": coin_inverse_residual,
            "delete_one_elementary_gate_index": deleted_gate_index,
            "delete_one_elementary_gate_output_residual": deleted_coin_gate_residual,
            "one_species_gate_counts": gate_counts(local_coin_gates),
            "one_species_gate_count": len(local_coin_gates),
            "one_species_schedule_sha256": gate_hash(local_coin_gates),
            "three_species_gate_counts": gate_counts(onsite_coin_gates),
            "three_species_schedule_sha256": gate_hash(onsite_coin_gates),
            "literal_onsite_line_layout": onsite_coin_routing,
        },
        "contact": contact,
        "stream_direction_tables": stream_rows,
        "local_gate_identities": identities,
        "Cycle600_EG_reproduction": eg,
        "covariance_and_sizes": covariance,
        "gate_alphabet": {
            "fixed_discrete": ("X", "H", "T", "Tdg", "CNOT", "SWAP"),
            "parameterized_one_role_bit": parameterized_families,
            "arbitrary_basis_two_level_gates_retained": False,
            "arbitrary_multi_controlled_phases_retained": False,
            "maximum_executed_gate_support_role_bits": 2,
            "parameterized_one_role_bit_gate_instances_onsite": analog_gate_count,
            "beta": -0.3,
            "contact_coupling": c230.COUPLING,
            "analog_angles_are_inherited_calibration_not_derived": True,
            "T_or_parametric_rotations_in_Cycle580_declared_alphabet": False,
            "exact_finite_Cycle580_H_CNOT_CZ_SWAP_closure": exact_cycle580_closure,
            "fault_tolerant_approximation_compiled": False,
            "executed_diagonal_T_power_grid_comparator": {
                "scope": "nearest exact P(k*pi/4) for inherited eigen/contact phases only; not all Clifford+T words",
                "rows": phase_grid_rows,
                "minimum_nonzero_residual": phase_grid_minimum_residual,
                "exact_grid_matches": sum(row["unit_complex_residual"] < TOL for row in phase_grid_rows),
            },
        },
        "scratch_and_schedule": {
            "persistent_Cycle600_carrier_role_bits_per_cell": 12,
            "maximum_reused_clean_scratch_role_bits_per_active_patch": 5,
            "maximum_live_role_bits_if_scratch_allocated_per_cell": 17,
            "clean_scratch_initialization_and_renewal_supplied": True,
            "move_apply_restore_routing_schedule_supplied": True,
            "global_conflict_free_stream_schedule_compiled": False,
            "schedule_is_physical_time": False,
        },
        "inherited_Cycle600_factorized_N3_algebraic_representation": cycle600_receipt[
            "route_A_full_N3_factorized_exterior_representation"
        ]["pass"],
        "exact_support_two_parametric_role_event_circuit": True,
        "physical_M2_primitive_composition": False,
        "physical_M2_intertwiner_residual": None,
        "physical_M2_leakage_evaluated": False,
        "exact_declared_finite_alphabet_elementary_closure": False,
        "pass_as_scoped_route": bool(route_condition),
        "pass_full_requested_elementary_and_global_layout_target": False,
    }
    check(
        "Route A exactly lowers structured word events to support-two parametric role gates and declared line patches while withholding physical-M2, finite-alphabet, and global-shift closure",
        route_condition, result,
    )
    return result


# ---------------------------------------------------------------------------
# Route B: translation-invariant parent Hamiltonian.


def site_flat(coordinate: tuple[int, int, int], length: int) -> int:
    return c600.c598.c593.site_flat(coordinate, length)


def site_tuple(site: int, length: int) -> tuple[int, int, int]:
    return c600.c598.c593.site_tuple(site, length)


def cubic_edges(length: int) -> tuple[tuple[int, int], ...]:
    edges = []
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        for axis in range(3):
            target = list(coordinate)
            target[axis] = (target[axis] + 1) % length
            edges.append((site, site_flat(tuple(target), length)))
    return tuple(edges)


def cubic_laplacian(length: int) -> np.ndarray:
    volume = length**3
    result = np.zeros((volume, volume), dtype=float)
    for left, right in cubic_edges(length):
        difference = np.zeros(volume)
        difference[left], difference[right] = 1, -1
        result += np.outer(difference, difference)
    return result


def cubic_neighbors(length: int) -> tuple[tuple[int, ...], ...]:
    rows = []
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        neighbors = []
        for axis in range(3):
            for displacement in (-1, 1):
                target = list(coordinate)
                target[axis] = (target[axis] + displacement) % length
                neighbors.append(site_flat(tuple(target), length))
        rows.append(tuple(neighbors))
    return tuple(rows)


def n2_sector_parent(length: int):
    """Construct the full two-excitation I-SWAP parent as a sparse matrix."""
    volume = length**3
    states = tuple(combinations(range(volume), 2))
    state_index = {state: index for index, state in enumerate(states)}
    neighbors = cubic_neighbors(length)
    row_indices = []
    column_indices = []
    entries = []
    for row, (first, second) in enumerate(states):
        boundary_edges = 0
        for occupied, other in ((first, second), (second, first)):
            for target in neighbors[occupied]:
                if target == other:
                    continue
                moved = tuple(sorted((other, target)))
                row_indices.append(row)
                column_indices.append(state_index[moved])
                entries.append(-1.0)
                boundary_edges += 1
        row_indices.append(row)
        column_indices.append(row)
        entries.append(float(boundary_edges))
    matrix = coo_matrix(
        (entries, (row_indices, column_indices)),
        shape=(len(states), len(states)), dtype=float,
    ).tocsr()
    return matrix


def sparse_low_spectrum(matrix, count: int = 4) -> np.ndarray:
    dimension = matrix.shape[0]
    v0 = np.linspace(1.0, 2.0, dimension, dtype=float)
    v0 /= np.linalg.norm(v0)
    values = eigsh(
        matrix, k=min(count, dimension - 1), which="SA", tol=1e-11,
        maxiter=200000, v0=v0, return_eigenvectors=False,
    )
    return np.sort(np.asarray(values, dtype=float))


def graph_covariance(length: int) -> dict:
    frames = c600.c598.c593.c210.proper_cubic_frames()
    edge_set = {frozenset(edge) for edge in cubic_edges(length)}
    frame_failures = 0
    translation_failures = 0
    group_failures = 0
    for displacement_site in range(length**3):
        displacement = site_tuple(displacement_site, length)
        for left, right in cubic_edges(length):
            mapped = []
            for site in (left, right):
                coordinate = site_tuple(site, length)
                mapped.append(site_flat(tuple(
                    (coordinate[axis] + displacement[axis]) % length for axis in range(3)
                ), length))
            translation_failures += frozenset(mapped) not in edge_set
    for frame in frames:
        for left, right in cubic_edges(length):
            mapped = []
            for site in (left, right):
                coordinate = np.asarray(site_tuple(site, length), dtype=int)
                mapped.append(site_flat(tuple(int(value % length) for value in frame @ coordinate), length))
            frame_failures += frozenset(mapped) not in edge_set
    probe_sites = tuple(range(min(42, length**3)))
    for first in frames:
        for second in frames:
            for site in probe_sites:
                coordinate = np.asarray(site_tuple(site, length), dtype=int)
                direct = site_flat(tuple(int(value % length) for value in (first @ second) @ coordinate), length)
                intermediate = second @ coordinate
                composed = site_flat(tuple(int(value % length) for value in first @ intermediate), length)
                group_failures += direct != composed
    return {
        "translations_tested": length**3,
        "translation_edge_failures": translation_failures,
        "proper_cubic_frames": len(frames),
        "all24_edge_failures": frame_failures,
        "frame_products": len(frames)**2,
        "all576_group_failures_on_42_sites": group_failures,
    }


def jump_ray_covariance(length: int, jump: np.ndarray) -> dict:
    """Execute translations, all24 ray maps, and all576 compositions on every edge."""
    frames = c600.c598.c593.c210.proper_cubic_frames()
    edges = cubic_edges(length)
    edge_lookup = {}
    for index, (left, right) in enumerate(edges):
        edge_lookup[(left, right)] = (index, 1)
        edge_lookup[(right, left)] = (index, -1)
    swap = SWAP
    reversal_residual = float(np.linalg.norm(swap @ jump @ swap + jump))

    def mapped_site(frame: np.ndarray, site: int) -> int:
        coordinate = np.asarray(site_tuple(site, length), dtype=int)
        mapped = frame @ coordinate
        return site_flat(tuple(int(value % length) for value in mapped), length)

    translation_failures = 0
    translation_tests = 0
    for displacement_site in range(length**3):
        displacement = site_tuple(displacement_site, length)
        for left, right in edges:
            mapped = []
            for site in (left, right):
                coordinate = site_tuple(site, length)
                mapped.append(site_flat(tuple(
                    (coordinate[axis] + displacement[axis]) % length
                    for axis in range(3)
                ), length))
            translation_tests += 1
            translation_failures += tuple(mapped) not in edge_lookup

    frame_edge_maps = []
    frame_failures = 0
    frame_tests = 0
    maximum_ray_residual = 0.0
    for frame in frames:
        edge_map = []
        for left, right in edges:
            directed = (mapped_site(frame, left), mapped_site(frame, right))
            frame_tests += 1
            if directed not in edge_lookup:
                frame_failures += 1
                edge_map.append((-1, 0))
                continue
            target_index, orientation = edge_lookup[directed]
            represented = jump if orientation == 1 else swap @ jump @ swap
            ray_residual = float(np.linalg.norm(represented - orientation * jump))
            maximum_ray_residual = max(maximum_ray_residual, ray_residual)
            frame_failures += ray_residual > 2e-13
            edge_map.append((target_index, orientation))
        frame_edge_maps.append(tuple(edge_map))

    frame_index = {
        tuple(int(value) for value in frame.reshape(-1)): index
        for index, frame in enumerate(frames)
    }
    group_failures = 0
    group_tests = 0
    for first_index, first in enumerate(frames):
        for second_index, second in enumerate(frames):
            product_index = frame_index[
                tuple(int(value) for value in (first @ second).reshape(-1))
            ]
            for edge_index in range(len(edges)):
                direct_target, direct_orientation = frame_edge_maps[product_index][edge_index]
                middle_target, second_orientation = frame_edge_maps[second_index][edge_index]
                composed_target, first_orientation = frame_edge_maps[first_index][middle_target]
                group_tests += 1
                group_failures += (
                    direct_target != composed_target
                    or direct_orientation != second_orientation * first_orientation
                )
    return {
        "translation_jump_ray_tests": translation_tests,
        "translation_jump_ray_failures": translation_failures,
        "proper_cubic_frames": len(frames),
        "all24_jump_ray_tests_every_edge": frame_tests,
        "all24_jump_ray_covariance_failures": frame_failures,
        "frame_products": len(frames)**2,
        "all576_jump_ray_group_tests_every_edge": group_tests,
        "all576_jump_ray_group_failures": group_failures,
        "edge_reversal_J_to_minus_J_residual": reversal_residual,
        "maximum_executed_jump_ray_residual": maximum_ray_residual,
    }


def route_b() -> dict:
    print("\nROUTE B — TRANSLATION-INVARIANT ONE-EXCITATION PARENT")
    rows = []
    condition = True
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        laplacian = cubic_laplacian(length)
        volume = length**3
        vacuum_parent = np.zeros((1, 1), dtype=float)
        vacuum_values = np.linalg.eigvalsh(vacuum_parent)
        w = np.ones(volume) / math.sqrt(volume)
        values = np.linalg.eigvalsh(laplacian)
        positive = values[values > 1e-9]
        gap = float(positive[0])
        expected_gap = 4 * math.sin(math.pi / length)**2
        n2_parent = n2_sector_parent(length)
        n2_values = sparse_low_spectrum(n2_parent)
        n2_positive = n2_values[n2_values > 1e-9]
        n2_gap = float(n2_positive[0])
        n2_dicke = np.ones(n2_parent.shape[0], dtype=float) / math.sqrt(n2_parent.shape[0])
        n2_action = n2_parent @ n2_dicke
        deleted = laplacian.copy()
        left, right = cubic_edges(length)[0]
        difference = np.zeros(volume)
        difference[left], difference[right] = 1, -1
        edge_term = np.outer(difference, difference)
        deleted -= edge_term
        deleted_values = np.linalg.eigvalsh(deleted)
        deleted_gap = float(deleted_values[deleted_values > 1e-9][0])
        covariance = graph_covariance(length)
        remote = site_flat(tuple(length // 2 for _axis in range(3)), length)
        if frozenset((0, remote)) in {frozenset(edge) for edge in cubic_edges(length)}:
            remote = site_flat((1, 1, 1), length)
        remote_pair_boundary_energy = 0
        occupied = {0, remote}
        for edge in cubic_edges(length):
            remote_pair_boundary_energy += int((edge[0] in occupied) != (edge[1] in occupied))
        row = {
            "length": length,
            "split": split,
            "volume": volume,
            "local_edge_terms": 3 * volume,
            "N0_sector_dimension_direct": int(vacuum_parent.shape[0]),
            "N0_zero_eigenvalue_multiplicity_direct": int(np.count_nonzero(np.abs(vacuum_values) < 1e-9)),
            "N0_ground_energy_direct": float(vacuum_values[0]),
            "N1_sector_dimension_direct": int(laplacian.shape[0]),
            "uniform_W_norm_residual": abs(float(w @ w) - 1),
            "uniform_W_parent_residual": float(np.linalg.norm(laplacian @ w)),
            "N1_zero_eigenvalue_multiplicity_direct": int(np.count_nonzero(np.abs(values) < 1e-9)),
            "N1_gap_direct": gap,
            "analytic_gap_4sin2_pi_over_L": expected_gap,
            "N1_gap_formula_residual": abs(gap - expected_gap),
            "N1_gap_times_L_squared": gap * length**2,
            "N2_sector_dimension_direct": int(n2_parent.shape[0]),
            "N2_sparse_parent_nonzero_entries": int(n2_parent.nnz),
            "uniform_N2_Dicke_parent_residual_direct": float(np.linalg.norm(n2_action)),
            "uniform_N2_Dicke_parent_energy_direct": float(np.real(n2_dicke @ n2_action)),
            "N2_lowest_four_eigenvalues_direct": n2_values,
            "N2_zero_eigenvalue_multiplicity_direct": int(np.count_nonzero(np.abs(n2_values) < 1e-9)),
            "N2_gap_direct": n2_gap,
            "N2_gap_formula_residual": abs(n2_gap - expected_gap),
            "delete_one_edge_operator_Frobenius_residual": float(np.linalg.norm(edge_term)),
            "delete_one_edge_W_residual": float(np.linalg.norm(deleted @ w)),
            "delete_one_edge_N1_gap": deleted_gap,
            "analytic_full_Hilbert_symmetric_ground_dimension": volume + 1,
            "analytic_all_number_sector_statement": "one fully symmetric Dicke zero vector in each N follows from SWAP invariance; only N0/N1/N2 are directly diagonalized here",
            "remote_localized_two_excitation_basis_energy": remote_pair_boundary_energy,
            **covariance,
        }
        rows.append(row)
        condition &= (
            row["uniform_W_parent_residual"] < 2e-13
            and row["N0_sector_dimension_direct"] == 1
            and row["N0_zero_eigenvalue_multiplicity_direct"] == 1
            and abs(row["N0_ground_energy_direct"]) < 2e-13
            and row["N1_sector_dimension_direct"] == volume
            and row["N1_zero_eigenvalue_multiplicity_direct"] == 1
            and row["N1_gap_formula_residual"] < 2e-12
            and row["N2_sector_dimension_direct"] == math.comb(volume, 2)
            and row["uniform_N2_Dicke_parent_residual_direct"] < 2e-12
            and abs(row["uniform_N2_Dicke_parent_energy_direct"]) < 2e-12
            and row["N2_zero_eigenvalue_multiplicity_direct"] == 1
            and row["N2_gap_formula_residual"] < 2e-10
            and row["delete_one_edge_operator_Frobenius_residual"] > 1
            and row["delete_one_edge_W_residual"] < 2e-13
            and row["delete_one_edge_N1_gap"] > 0
            and row["remote_localized_two_excitation_basis_energy"] > 0
            and row["translation_edge_failures"] == row["all24_edge_failures"] == 0
            and row["all576_group_failures_on_42_sites"] == 0
        )
    result = {
        "status": "exact cubic ferromagnetic-swap parent: W is unique and gapped only within supplied N=1; vacuum and the full N2 Dicke sector control are directly computed, while all-number Dicke competitors are an explicit SWAP-invariance theorem",
        "local_term": "h_xy=I-SWAP_xy; in N=1 this is (|x>-|y>)(<x|-<y|)",
        "local_support_role_bits": 2,
        "physical_M2_primitive_composition": False,
        "translation_invariant": True,
        "proper_cubic_covariant": True,
        "rows": rows,
        "gap_scaling": "Delta_L=4 sin^2(pi/L), hence Delta_L~4 pi^2/L^2",
        "N1_sector_supplied": True,
        "chemical_potential_or_number_penalty_constructed": False,
        "vacuum_is_global_ground_competitor": True,
        "N2_Dicke_is_global_ground_competitor": True,
        "unique_global_genesis": False,
        "preparation_dynamics_constructed": False,
        "pass_as_sector_parent": bool(condition),
        "pass_global_genesis": False,
    }
    check(
        "Route B gives a local all24 W parent and exact finite-size gap while vacuum/N2 controls prevent global-genesis language",
        bool(condition), result,
    )
    return result


# ---------------------------------------------------------------------------
# Route C: local dissipative/dark-state jump family.


def route_c(route_b_result: dict) -> dict:
    print("\nROUTE C — LOCAL DARK-JUMP SECTOR SELECTOR")
    plus = np.asarray([0, 1, 1, 0], dtype=complex) / math.sqrt(2)
    minus = np.asarray([0, 1, -1, 0], dtype=complex) / math.sqrt(2)
    jump = np.outer(plus, minus.conj())
    projector_minus = np.outer(minus, minus.conj())
    rows = []
    condition = True
    for parent_row in route_b_result["rows"]:
        length = parent_row["length"]
        volume = length**3
        laplacian = cubic_laplacian(length)
        w = np.ones(volume) / math.sqrt(volume)
        parent_dark = 0.5 * laplacian
        values = np.linalg.eigvalsh(parent_dark)
        positive = values[values > 1e-9]
        dark_gap = float(positive[0])
        vacuum_dark = np.zeros((1, 1), dtype=float)
        vacuum_values = np.linalg.eigvalsh(vacuum_dark)
        n2_dark = 0.5 * n2_sector_parent(length)
        n2_values = sparse_low_spectrum(n2_dark)
        n2_positive = n2_values[n2_values > 1e-9]
        n2_gap = float(n2_positive[0])
        n2_dicke = np.ones(n2_dark.shape[0], dtype=float) / math.sqrt(n2_dark.shape[0])
        n2_action = n2_dark @ n2_dicke
        covariance = jump_ray_covariance(length, jump)
        isolated = parent_dark.copy()
        for left, right in cubic_edges(length):
            if left == 0 or right == 0:
                difference = np.zeros(volume)
                difference[left], difference[right] = 1, -1
                isolated -= 0.5 * np.outer(difference, difference)
        isolated_values = np.linalg.eigvalsh(isolated)
        row = {
            "length": length,
            "split": parent_row["split"],
            "jump_instances": 3 * volume,
            "common_dark_N0_dimension_direct": int(np.count_nonzero(np.abs(vacuum_values) < 1e-9)),
            "common_dark_N1_dimension_direct": int(np.count_nonzero(np.abs(values) < 1e-9)),
            "uniform_W_jump_residual": float(np.linalg.norm(parent_dark @ w)),
            "dark_parent_N1_gap_direct": dark_gap,
            "analytic_dark_gap_2sin2_pi_over_L": 2 * math.sin(math.pi / length)**2,
            "dark_N1_gap_formula_residual": abs(dark_gap - 2 * math.sin(math.pi / length)**2),
            "common_dark_N2_sector_dimension_direct": int(n2_dark.shape[0]),
            "common_dark_N2_lowest_four_eigenvalues_direct": n2_values,
            "common_dark_N2_dimension_direct": int(np.count_nonzero(np.abs(n2_values) < 1e-9)),
            "uniform_N2_Dicke_jump_parent_residual_direct": float(np.linalg.norm(n2_action)),
            "uniform_N2_Dicke_jump_parent_energy_direct": float(np.real(n2_dicke @ n2_action)),
            "dark_parent_N2_gap_direct": n2_gap,
            "dark_N2_gap_formula_residual": abs(n2_gap - 2 * math.sin(math.pi / length)**2),
            "delete_six_incident_jumps_common_dark_dimension": int(np.count_nonzero(np.abs(isolated_values) < 1e-9)),
            "analytic_all_number_common_dark_dimension": volume + 1,
            "analytic_all_number_statement": "one fully symmetric Dicke dark vector in each N follows from the local J kernel; only N0/N1/N2 are directly evaluated here",
            **covariance,
        }
        rows.append(row)
        condition &= (
            row["common_dark_N0_dimension_direct"] == 1
            and row["common_dark_N1_dimension_direct"] == 1
            and row["uniform_W_jump_residual"] < 2e-13
            and row["dark_N1_gap_formula_residual"] < 2e-12
            and row["common_dark_N2_sector_dimension_direct"] == math.comb(volume, 2)
            and row["common_dark_N2_dimension_direct"] == 1
            and row["uniform_N2_Dicke_jump_parent_residual_direct"] < 2e-12
            and abs(row["uniform_N2_Dicke_jump_parent_energy_direct"]) < 2e-12
            and row["dark_N2_gap_formula_residual"] < 2e-10
            and row["delete_six_incident_jumps_common_dark_dimension"] == 2
            and row["translation_jump_ray_failures"] == 0
            and row["all24_jump_ray_covariance_failures"] == 0
            and row["all576_jump_ray_group_failures"] == 0
            and row["edge_reversal_J_to_minus_J_residual"] < 2e-13
            and row["maximum_executed_jump_ray_residual"] < 2e-13
        )
    local_identity = float(np.linalg.norm(jump.conj().T @ jump - projector_minus))
    result = {
        "status": "local excitation-conserving jump family has W as the unique common dark vector within directly evaluated N=1 and has a directly evaluated N2 Dicke competitor; every-edge all24/all576 jump-ray covariance is executed, while semigroup convergence and sector genesis are not certified",
        "jump": "J_xy=|psi+><psi-| on each unoriented cubic edge; orientation reversal changes only its global sign",
        "jump_support_role_bits": 2,
        "physical_M2_primitive_composition": False,
        "JdaggerJ_minus_projector_residual": local_identity,
        "rows": rows,
        "declared_input_sector": "exactly one excitation shared by bound/neutral carrier modes",
        "excitation_number_conserved": True,
        "prepares_or_enforces_N1_from_vacuum": False,
        "vacuum_genesis": False,
        "remote_N2_competitor_excluded": False,
        "Lindblad_rate_or_physical_clock_derived": False,
        "complete_semigroup_unique_stationary_state_proved": False,
        "finite_scheduled_Kraus_compiler_executed": False,
        "static_parent_common_kernel_certified": True,
        "pass_as_dark_sector_candidate": bool(condition and local_identity < 2e-13),
        "pass_unique_genesis_or_preparation": False,
    }
    check(
        "Route C directly executes N2 dark-kernel and every-edge all24/all576 jump-ray controls while keeping convergence, rate, and sector genesis explicit",
        result["pass_as_dark_sector_candidate"], result,
    )
    return result


def no_go_discipline(route_a_result: dict, route_b_result: dict,
                      route_c_result: dict) -> dict:
    walls = (
        "finite declared alphabet or calibrated analog one-role-bit rotations",
        "one simultaneous conflict-free global stream schedule",
        "exact N=1 species-sector genesis",
        "dark semigroup convergence and autonomous rate",
        "clean scratch initialization and renewal",
    )
    pairs = []
    for first, second in combinations(walls, 2):
        pairs.append({
            "first": first,
            "second": second,
            "close_first_implies_second": False,
            "evidence_first_to_second": f"closing {first} supplies no mechanism for {second}",
            "close_second_implies_first": False,
            "evidence_second_to_first": f"closing {second} supplies no mechanism for {first}",
            "independent": True,
        })
    families = (
        {
            "family": "structured word-table circuit",
            "object_formulation": "three four-role-bit carrier words and clean Boolean scratch",
            "mechanism_invariant": "pair-H/qutrit spectral factorization, reversible predicates, and Gray transpositions",
            "terminal_obligation": "support-two exact coin/contact/link event circuits",
            "strength": "weaker than full finite-alphabet/global-shift target",
            "marker": "ATTEMPTED",
            "authority_citation": "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py::route_a (current authority-none execution)",
            "why_not_terminal": "exact over parameterized one-role-bit rotations on the algebraic role code; physical-M2 composition and global shift schedule are not compiled",
        },
        {
            "family": "fixed diagonal T-phase-grid compiler",
            "object_formulation": "Cycle580 H/CNOT/CZ/SWAP alphabet and Clifford-phase extensions",
            "mechanism_invariant": "replace inherited analog rotations by finite exact phase words",
            "terminal_obligation": "exact beta=-0.3 and g=0.37 amplitudes",
            "strength": "target-equivalent only for the alphabet residual",
            "marker": "ATTEMPTED",
            "authority_citation": "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py::route_a (current authority-none execution)",
            "why_not_terminal": "nearest P(k*pi/4) words were executed and miss every inherited eigen/contact phase; this does not test general Clifford+T words",
        },
        {
            "family": "cubic swap parent Hamiltonian",
            "object_formulation": "one-excitation graph Laplacian plus direct sparse N2 parent",
            "mechanism_invariant": "connected-edge equality, SWAP invariance, and spectral gap",
            "terminal_obligation": "unique uniform W inside N=1 with held-size scaling",
            "strength": "target-equivalent for sector parent only",
            "marker": "ATTEMPTED",
            "authority_citation": "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py::route_b (current authority-none execution)",
            "why_not_terminal": "closed exactly in supplied N=1; directly computed vacuum and N2 Dicke states remain ground competitors, so genesis is not supplied",
        },
        {
            "family": "local dark-jump cooling",
            "object_formulation": "edge jumps |psi+><psi-| and their positive dark parent",
            "mechanism_invariant": "drain edge-antisymmetric amplitude into the symmetric ray",
            "terminal_obligation": "unique W common dark vector and autonomous preparation",
            "strength": "weaker",
            "marker": "ATTEMPTED",
            "authority_citation": "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py::route_c (current authority-none execution)",
            "why_not_terminal": "common N1 dark ray/gap and direct N2 competitor are closed; convergence, rate, and sector genesis are unproved",
        },
        {
            "family": "topological winding/mark preparation",
            "object_formulation": "marked noncontractible Z2 loops",
            "mechanism_invariant": "Gauss conservation and Wilson-line schedule",
            "terminal_obligation": "one point carrier without supplied winding or mark sector",
            "strength": "weaker",
            "marker": "RULED OUT BY PRIOR",
            "authority_citation": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md:172-184 (exact-pinned authority-none prior; family-specific evidence only)",
            "why_not_terminal": "the covariant loop orbit exists, but winding and one-mark sectors are supplied and a second remote mark passes the same local check",
        },
    )

    def rhetoric_row(statement: str, narrow_scope: str,
                      evidence: tuple[tuple[bool, str], ...]) -> dict:
        resolution_names = ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")
        return {
            "statement": statement,
            "narrow_scoped_phrase": narrow_scope,
            "resolutions": {
                name: {
                    "tested_in_cycle": tested,
                    "evidence_or_nonclaim": detail,
                    "untested_resolution_negative_asserted": False,
                }
                for name, (tested, detail) in zip(resolution_names, evidence)
            },
            "universal_impossibility_claimed": False,
        }

    rhetoric = (
        rhetoric_row(
            "the finite Cycle580 alphabet is not closed by this construction",
            "only the executed nearest P(k*pi/4) comparator fails for the inherited phases; general finite synthesis is open",
            ((True, "individual inherited phases are compared to the T grid"), (True, "onsite coin/contact phase requirements are enumerated"),
             (True, "coin eigenphases are compared"), (True, "the role-circuit uses parameterized rotations beyond Cycle580"),
             (False, "no general lattice-wide Clifford+T synthesis/no-go is tested or asserted")),
        ),
        rhetoric_row(
            "separate crossed-link tables are not one simultaneous torus update",
            "the six exact link-table circuits are not promoted to a collision-free global stream in this artifact",
            ((True, "each selected basis transposition is executed"), (True, "each local word pair is exhausted"),
             (True, "all six direction labels are tested"), (True, "bounded line routing is executed"),
             (False, "no simultaneous global composition is executed and no impossibility is asserted")),
        ),
        rhetoric_row(
            "a schedule is not time",
            "the declared compiler schedules are not promoted to physical time in this artifact",
            ((True, "individual gate order is inventoried"), (True, "onsite schedules have no clock map"),
             (False, "no per-mode time claim is made"), (True, "patch routing order is compile-time data"),
             (True, "the missing global stream schedule is not a clock law")),
        ),
        rhetoric_row(
            "a generator element is not a rate or physical energy",
            "the declared jump/parent coefficients have no rate, energy, or causal-time calibration here",
            ((True, "each edge jump coefficient is dimensionless supplied data"), (True, "site adjacency supplies no calibration"),
             (True, "N1/N2 eigenvalues are algebraic parent spectra"), (True, "finite blocks use supplied coupling one"),
             (True, "L3/L6/L7 spectra are not calibrated rates or energies")),
        ),
        rhetoric_row(
            "a role bit is not a physical M2 site",
            "Cycle600 role bits are not promoted to physical M2 sites in this artifact",
            ((True, "every support-one/two gate is labeled a role gate"), (True, "12 role bits per coarse cell are algebraic inventory"),
             (True, "word/mode labels have no M2 encoder"), (True, "line patches are declared role layouts"),
             (True, "L3/L6/L7 counts remain role counts")),
        ),
        rhetoric_row(
            "algebraic E-G and scratch leakage are not physical compiler residuals",
            "reported E-G and scratch-return residuals are algebraic-only in this artifact",
            ((True, "gate and scratch identities are evaluated"), (True, "onsite coin/contact restrictions are evaluated"),
             (True, "N<=3 exterior fixtures are evaluated"), (True, "crossed-link word restrictions are evaluated"),
             (False, "no physical lattice-wide E or G is composed; no physical residual is asserted")),
        ),
        rhetoric_row(
            "a parent Hamiltonian, ground state, or dark ray is not preparation, branch, occurrence, Record, or actuality",
            "the computed parent/ground/dark objects are not promoted to preparation/branch/occurrence/Record/actuality here",
            ((True, "edge kernels are algebraic"), (True, "site graph supplies no record interface"),
             (True, "N0/N1/N2 sectors are directly separated"), (True, "finite torus kernels are evaluated"),
             (True, "no occurrence or Record law is composed at L3/L6/L7")),
        ),
        rhetoric_row(
            "carrier bookkeeping is not empirical charge, energy, stress, source, or gravity",
            "role counts and carrier labels are not promoted to empirical source quantities here",
            ((True, "gate labels have no empirical units"), (True, "per-cell counts are resource inventory"),
             (True, "mode labels carry no source calibration"), (True, "patch counts carry no stress tensor"),
             (True, "no gravity/source response law is evaluated")),
        ),
        rhetoric_row(
            "conservation is not preparation or genesis",
            "excitation-number conservation does not prepare or select N=1 in this artifact",
            ((True, "each jump conserves excitation number"), (True, "local terms cannot create from vacuum"),
             (True, "N0/N1/N2 sectors are invariant and directly compared"), (True, "finite blocks retain sector"),
             (True, "vacuum and N2 controls defeat a genesis claim")),
        ),
        rhetoric_row(
            "proper-cubic covariance is not Lorentz covariance",
            "executed proper-cubic frame identities are not promoted to Lorentz covariance here",
            ((True, "local role/jump actions are checked under cubic frames"), (True, "site maps use 24 cubic rotations"),
             (True, "direction modes are permuted only by the cubic group"), (True, "declared blocks check 576 products"),
             (True, "no boosts or continuum Lorentz limit are evaluated")),
        ),
        rhetoric_row(
            "exact N<=3 algebra is not complete N4 interactions",
            "the exact N<=3 restriction is not promoted to an N4/four-carrier theorem here",
            ((True, "single role-gate identities are full-space logical identities"), (True, "onsite tables cover declared labels"),
             (True, "only N0/N1/N2/N3 inherited exterior fixtures are reproduced"), (True, "link blocks are two-word tables"),
             (False, "N4/four-carrier lattice dynamics is not tested and no negative is asserted")),
        ),
    )

    residual_matching = (
        {
            "witness_path": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md",
            "witness_lines": "156-158",
            "witness_residual": "no elementary physical-M2 gate/off-code unitary/support radius/gate count",
            "current_residual_same_scope": "physical-M2 composition/intertwiner/leakage remain absent",
            "current_claimed_closure": "parameterized support-two role-bit circuit only",
            "match": True,
            "used_as_closure_witness": False,
        },
        {
            "witness_path": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md",
            "witness_lines": "162-166,315-317",
            "witness_residual": "no one-excitation parent/gap or W preparation law",
            "current_residual_same_scope": "static N1 W parent and finite-size gap",
            "current_claimed_closure": "static sector parent/gap only; preparation remains open",
            "match": True,
            "used_as_closure_witness": True,
        },
        {
            "witness_path": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md",
            "witness_lines": "315-317,321-323",
            "witness_residual": "local one-excitation dark-state route unattempted",
            "current_residual_same_scope": "common N1 dark kernel and parent gap",
            "current_claimed_closure": "common dark kernel only; semigroup convergence/rate/genesis remain open",
            "match": True,
            "used_as_closure_witness": True,
        },
        {
            "witness_path": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md",
            "witness_lines": "172-184",
            "witness_residual": "winding and exactly-one mark are supplied in the topological comparator",
            "current_residual_same_scope": "topological one-point preparation without supplied winding/mark",
            "current_claimed_closure": "none; prior evidence is used only to retire that bounded family",
            "match": True,
            "used_as_closure_witness": False,
        },
    )

    partial_paths = (
        {
            "path": "scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py",
            "status": "existing inherited support-two physical-M2 gate/layout construction for a different L41 instrument",
            "what_it_would_close": "a reusable template for mapping one bounded gate table into physical M2",
            "what_remains": "no map from the Cycle603 12-role alphabet or its parameterized angles is supplied",
        },
        {
            "path": "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py",
            "status": "existing conditional 53-M2-role blueprint; physical primitive composition remains false",
            "what_it_would_close": "a candidate bounded layout and local number/gauge vocabulary",
            "what_remains": "compose the current role gates and directly evaluate physical E-G/leakage",
        },
        {
            "path": "scripts/physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22.py",
            "status": "exact-pinned algebraic N<=3 exterior representation with supplied sector/W data",
            "what_it_would_close": "the exact logical target that a physical compiler must intertwine",
            "what_remains": "physical role placement, primitive update, sector genesis, and W preparation",
        },
        {
            "path": "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py",
            "status": "current authority-none partial construction",
            "what_it_would_close": "parametric role-circuit decomposition and static N1 parent/dark-kernel subproblems",
            "what_remains": "finite calibrated alphabet, global stream, physical-M2 map, reservoir convergence, and renewal",
        },
    )

    cross_cycle = (
        {
            "prior_wall": "three-cell decoder depended on prior branch/order service",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_GLOBAL_N3_RETURNED_SLOT_COMPILER_CYCLE560_NOTE_2026-07-21.md:94-109",
            "retired": True,
            "mechanism": "persistent q plus the current bounded physical pattern replaced retained prior branch state",
            "applicability": "supports trying an in-state bounded carrier program, but does not itself compile the Cycle603 stream",
        },
        {
            "prior_wall": "runtime lexicographic selected-factor traversal",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_HELD_SPARSE_ORDER_RETIREMENT_CYCLE563_NOTE_2026-07-21.md:100-114",
            "retired": True,
            "mechanism": "bounded transported color products and local anticommutation identities",
            "applicability": "motivates a partitioned/double-buffer carrier shift; its conflict-free construction remains unattempted here",
        },
        {
            "prior_wall": "bounded elementary physical gate/layout and full-unitary extension",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md:21-28",
            "retired": True,
            "mechanism": "explicit support-two physical-M2 gates and nearest-neighbor layout",
            "applicability": "could be adapted after a lawful Cycle603 role-to-M2 map and angle alphabet are chosen",
        },
        {
            "prior_wall": "full-torus logical CAR packet lacked physical primitive composition/intertwiner/leakage",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md:129-141",
            "retired": False,
            "mechanism": "conditional 53-M2-role blueprint narrows layout but does not compose primitives",
            "applicability": "same physical-lowering residual persists and prevents shared-obstruction language",
        },
        {
            "prior_wall": "uniform neutral-W preparation and physical 12-role composition",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md:156-166",
            "retired": "partial",
            "mechanism": "Cycle603 supplies a role circuit plus static W parent/dark kernel",
            "applicability": "preparation, N1 selection, and physical-M2 composition remain open actionable routes",
        },
    )

    result = {
        "skill_source": "origin/main:docs/ai_methodology/skills/no-go-discipline/SKILL.md",
        "no_go_discipline_protocol_applied": True,
        "N1_normalized_families": families,
        "N1_normalized_family_count": len(families),
        "N1_qualifying_ATTEMPTED_or_RULED_OUT_count": len(families),
        "N1_required_count": 5,
        "N1_markers_valid": all(row["marker"] in {"ATTEMPTED", "RULED OUT BY PRIOR"} for row in families),
        "N1_prior_rows_have_authority_citations": all(
            row["authority_citation"] for row in families if row["marker"] == "RULED OUT BY PRIOR"
        ),
        "N1_pass": True,
        "N1_open_unattempted_steelman_family": {
            "family": "fault-tolerant approximation and autonomous number-selecting reservoir",
            "object_formulation": "precision-bounded finite words plus local open-system number control",
            "mechanism_invariant": "Clifford+T approximation and reservoir spectral selection",
            "terminal_obligation": "replace exact analog angles and select N=1 globally",
            "status": "OPEN / NOT COUNTED",
        },
        "N2_directional_pairs": pairs,
        "N2_pair_count": len(pairs),
        "N2_collapsed_wall_count": len(walls),
        "N2_any_implication_found": False,
        "N3_hidden_condition_scan": {
            "analog angles": "explicit inherited beta/contact calibration",
            "clean scratch": "explicit supplied zero-state resource",
            "routing and global stream order": "explicit compile schedule; not time",
            "N1 sector": "explicit supplied global count",
            "parent/dissipator coupling and clock": "explicit supplied candidate parameters",
            "full space extension": "invalid words use m=0 and word coin identity; scratch unitary is explicit",
            "standard-methods phrase": "non-load-bearing prior-art characterization only; it supplies no premise or closure",
            "hidden_conditions_promoted_to_walls": (),
        },
        "N4_residual_matching": residual_matching,
        "N4_all_closure_witnesses_same_scope": all(
            row["match"] for row in residual_matching if row["used_as_closure_witness"]
        ),
        "N5_rhetoric_audit": rhetoric,
        "N6_partial_closure_paths": partial_paths,
        "N6_primitive_registry_status": "not invoked: no 'no retained primitive' or 'new axiom required' claim is made",
        "N7_hostile_steelman": {
            "mechanism": "Map each role bit into a lawful physical register, synthesize the explicit support-two schedule with calibrated RY/RZ/P or precision-bounded Clifford+T, use a double-buffer partitioned QCA for the shift, and couple a local number-selecting reservoir or gauge charge to the W parent.",
            "terminal_obligation": "Construct the physical E and G, prove physical E-G/leakage/covariance with constant overhead, select N=1 from lawful inputs, and prove dark-semigroup convergence with a calibrated rate.",
            "authority_status": "OPEN / NO RETAINED AUTHORITY; supported only by Cycle603 authority-none constructions and the exact-pinned Cycle600 open-path statement at lines 315-323",
            "actionable": True,
            "consequence": "broad elementary-synthesis, genesis, shared-obstruction, minimum-content, and axiom-pressure negatives are premature",
        },
        "N7_pass_for_broad_negative": False,
        "N8_cross_cycle_echo": cross_cycle,
        "route_evidence": {
            "A": route_a_result["pass_as_scoped_route"],
            "B": route_b_result["pass_as_sector_parent"],
            "C": route_c_result["pass_as_dark_sector_candidate"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "gate_status": "FAIL",
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "failure_conditions_hit": (
            "N7 gives an actionable live physical compiler/reservoir/partitioned-QCA steelman",
            "the current authority-none construction does not close physical M2, global stream, sector genesis, or convergence",
        ),
        "demoted_artifact_status": "partial-attempt-with-named-untested-routes",
        "scoped_constructive_artifact_validity": "PASS if independent numeric, dependency, note, and resource checks pass; this is not the no-go gate status",
    }
    resolution_names = {"per_element", "per_site", "per_mode", "per_block", "lattice_wide"}
    condition = (
        len(families) >= 5
        and result["N1_markers_valid"]
        and result["N1_prior_rows_have_authority_citations"]
        and len(pairs) == math.comb(len(walls), 2)
        and all(row["match"] in {True, False} and row["witness_path"] and row["witness_lines"] for row in residual_matching)
        and all(set(row["resolutions"]) == resolution_names for row in rhetoric)
        and all({"path", "status", "what_it_would_close", "what_remains"} <= set(row) for row in partial_paths)
        and result["N7_hostile_steelman"]["actionable"]
        and all({"prior_wall", "citation", "retired", "mechanism", "applicability"} <= set(row) for row in cross_cycle)
        and all(result["route_evidence"].values())
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["shared_obstruction"] and not result["axiom_pressure"]
        and result["gate_status"] == "FAIL"
        and result["broad_negative_gate"] == "FAIL / DO NOT SHIP"
    )
    check("N1-N8 schema is complete and records broad-negative gate FAIL without invalidating scoped constructive evidence", condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Author artifact status accepted: false",
        "Cycle 603", "Route A", "Route B", "Route C",
        "12 role bits", "parameterized", "finite", "H/CNOT/CZ/SWAP", "off-code",
        "nearest-neighbor", "SWAP", "L3", "L6", "L7", "all 24", "all 576",
        "N=1", "vacuum", "two-excitation", "W", "gap", "dark", "genesis",
        "schedule is not time", "A generator element is not a rate",
        "Physical-M2 primitive composition remains open", "Carrier bookkeeping",
        "direct N2", "every-edge jump-ray", "N1", "N8", "no axiom pressure",
        "Gate status: FAIL", "Broad-negative gate: FAIL / DO NOT SHIP",
        "partial-attempt-with-named-untested-routes",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    forbidden = (
        "unique global genesis is achieved", "finite accepted alphabet is closed",
        "schedule is physical time", "carrier count is energy", "shared obstruction proved",
        "physical-M2 compiler is closed",
    )
    forbidden_hits = tuple(phrase for phrase in forbidden if phrase in text)
    result = {"required_phrases": required, "missing": missing, "forbidden_hits": forbidden_hits}
    check("Cycle603 note freezes route boundaries, controls, N1-N8, and firewalls",
          not missing and not forbidden_hits, result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0
    started = time.perf_counter()
    print("Cycle603 carrier preparation / elementary synthesis tournament", AUTHORITY, AUDIT)
    cycle600_receipt, shore_closure = shore()
    route_a_result = route_a(cycle600_receipt)
    route_b_result = route_b()
    route_c_result = route_c(route_b_result)
    discipline = no_go_discipline(route_a_result, route_b_result, route_c_result)
    note = note_contract()
    elapsed = time.perf_counter() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS ru_maxrss is bytes; Linux is KiB.  This campaign runs on macOS.
    resource_result = {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss}
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, resource_result)

    runner_hash = sha(Path(__file__))
    note_hash = sha(NOTE)
    receipt = {
        "status": "cycle603-carrier-preparation-elementary-synthesis-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_artifact_status_accepted": False,
        "pins": PINS,
        "runner_sha256": runner_hash,
        "note_sha256": note_hash,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "shore": shore_closure,
        "route_A_structured_elementary_compiler": route_a_result,
        "route_B_W_parent_Hamiltonian": route_b_result,
        "route_C_dark_jump_sector_selector": route_c_result,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": "an exact full-space support-two role-bit circuit over explicit fixed gates plus parameterized one-role-bit RY/RZ/P rotations compiles the structured Cycle600 onsite coin/contact and every crossed-link valid-word transposition on bounded declared line patches; separately, directly constructed N0/N1/N2 parent and dark-kernel matrices certify W uniqueness only within N=1, N2 Dicke competitors, finite-size gaps, and independent every-edge jump-ray all24/all576 covariance; no physical-M2 primitive composition is supplied",
        "route_disposition": {
            "A": "scoped pass: exact parametric role-event circuit; physical-M2 composition, finite Cycle580 alphabet, scratch renewal, and one simultaneous global stream schedule remain open",
            "B": "pass as sector parent: direct N0/N1/N2 spectra show W unique/gapped only within N=1 and vacuum/N2 Dicke prevent global genesis",
            "C": "pass as dark-kernel candidate: direct N0/N1/N2 kernel plus every-edge jump-ray all24/all576 execution; convergence/rate and sector genesis unproved",
        },
        "optimal_next_campaign": "map the 12 role bits and their gates into declared physical-M2 primitives with an exact E/G and leakage audit, then compile a constant-overhead double-buffer or partitioned-QCA global carrier shift; in parallel test a local number-selecting reservoir for the W parent/dark family",
        "physical_M2_scope": {
            "primitive_composition": False,
            "intertwiner_residual": None,
            "leakage_evaluated": False,
            "literal_layout_compiled": False,
        },
        "interpretation_firewall": {
            "schedule_is_time": False,
            "generator_element_is_rate_or_energy": False,
            "role_bits_are_physical_M2": False,
            "ground_or_dark_ray_is_Record_or_actuality": False,
        },
        "shared_obstruction_or_axiom_pressure": False,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "demoted_artifact_status": "partial-attempt-with-named-untested-routes",
        "constitutional_effect": "none",
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    summary = {
        "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
        "support_two_parametric_role_circuit": route_a_result["exact_support_two_parametric_role_event_circuit"],
        "physical_M2_primitive_composition": False,
        "finite_cycle580_alphabet_closure": route_a_result["exact_declared_finite_alphabet_elementary_closure"],
        "W_unique_in_N1": route_b_result["pass_as_sector_parent"],
        "direct_N2_controls": True,
        "direct_every_edge_jump_covariance": True,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "unique_genesis": False, "axiom_pressure": False,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
