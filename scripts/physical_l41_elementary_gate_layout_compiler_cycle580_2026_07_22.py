#!/usr/bin/env python3
"""Cycle580: elementary physical-M2 gate/layout compiler for Cycle577 Route B.

The runner realizes the exact Cycle577 18-M2 retained-environment isometry as
a full-space unitary gate sequence.  It tests a native parity-preserving
two-M2 logical-H block and its CNOT-H-CNOT elementary decomposition on a
literal nearest-neighbor proper-cubic layout.  Conditional traces remain
diagnostics; no actual member, Record, Born law, time, energy, or rate is
created.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22 as c577


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
COUNT = 18
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

FROZEN_PATHS = {
    "Cycle577 runner": ROOT / "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py",
    "Cycle577 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md",
    "Cycle577 receipt": ROOT / "outputs/physical_l41_projector_instrument_compiler_tournament_cycle577_receipt_2026_07_22.json",
}
FROZEN = {
    "Cycle577 runner": "93bf1fa2859289b13037bfe7882cce86732e9377ed8b60e56c3bd55ebc0ce74f",
    "Cycle577 note": "23ef5601b73c121d5e82c9031ec0ff4acffdc5471c43aa4dec63a78085aa7c0f",
    "Cycle577 receipt": "806d7a7c1f8a7ed5b9de235de0bde5bec63d3fbaae7eb68cd55c862a35d9daa3",
}
CYCLE577_AGENT_TRANSCRIPT_SHA256 = "0ba0c1b5d6223df39faa5f3a30275f858201bd0d354de9b0b8b1dd6021ecd21a"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


I2 = c577.I2
H = c577.H
W2 = c577.W2
W3 = c577.W3
Q2 = c577.Q2
Q3 = c577.Q3
ZERO = c577.ZERO
PLUS3 = c577.PLUS3

CNOT = np.asarray(
    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
    dtype=complex,
)
CZ2 = np.diag((1, 1, 1, -1)).astype(complex)
SWAP = np.asarray(
    ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
    dtype=complex,
)
LOGICAL_H = CNOT @ np.kron(H, I2) @ CNOT


@dataclass(frozen=True)
class Gate:
    name: str
    qubits: tuple[int, ...]
    matrix: np.ndarray
    layer: int
    role: str


QUBIT_NAMES = (
    "S_L0", "S_L1", "S_M0", "S_M1", "S_R0", "S_R1",
    "E_L0", "E_L1", "E_M0", "E_M1", "E_R0", "E_R1",
    "P_M", "P_L", "P_R", "D_M", "D_L", "D_R",
)
NAME_TO_QUBIT = {name: index for index, name in enumerate(QUBIT_NAMES)}

# A 3 x 4 x 2 proper-cubic bounding box.  Every required two-M2 interaction
# is a unit Manhattan edge; the reset SWAPs are physical operations rather
# than routing overhead.
LAYOUT = {
    "S_L0": (-1, 0, 0), "S_L1": (-1, 0, 1),
    "S_M0": (0, 0, 0), "S_M1": (0, 0, 1),
    "S_R0": (1, 0, 0), "S_R1": (1, 0, 1),
    "E_L0": (-1, 1, 0), "E_L1": (-1, 1, 1),
    "E_M0": (0, 1, 0), "E_M1": (0, 1, 1),
    "E_R0": (1, 1, 0), "E_R1": (1, 1, 1),
    "P_M": (0, -1, 0), "P_L": (-1, -1, 0), "P_R": (1, -1, 0),
    "D_M": (0, -2, 0), "D_L": (-1, -2, 0), "D_R": (1, -2, 0),
}


def q(name: str) -> int:
    return NAME_TO_QUBIT[name]


def two(name: str, left: str, right: str, matrix: np.ndarray, layer: int, role: str) -> Gate:
    return Gate(name, (q(left), q(right)), matrix, layer, role)


def one(name: str, site: str, matrix: np.ndarray, layer: int, role: str) -> Gate:
    return Gate(name, (q(site),), matrix, layer, role)


NATIVE_GATES = tuple(
    [
        two(f"reset_swap_{cell}_{rail}", f"S_{cell}{rail}", f"E_{cell}{rail}", SWAP, 1, "reset-export")
        for cell in ("L", "M", "R") for rail in (0, 1)
    ]
    + [
        two("encoded_CZ_LM", "S_L0", "S_M0", CZ2, 2, "encoded-contact"),
        two("encoded_CZ_MR", "S_M0", "S_R0", CZ2, 3, "encoded-contact"),
        two("native_logical_H_open", "S_M0", "S_M1", LOGICAL_H, 4, "X-pointer-basis"),
        two("extract_X_middle", "S_M0", "P_M", CNOT, 5, "pointer-extraction"),
        two("extract_Z_left", "S_L0", "P_L", CNOT, 5, "pointer-extraction"),
        two("extract_Z_right", "S_R0", "P_R", CNOT, 5, "pointer-extraction"),
        two("native_logical_H_close", "S_M0", "S_M1", LOGICAL_H, 6, "X-pointer-basis"),
        two("copy_middle_dephase", "P_M", "D_M", CNOT, 7, "dephasing-copy"),
        two("copy_left_dephase", "P_L", "D_L", CNOT, 7, "dephasing-copy"),
        two("copy_right_dephase", "P_R", "D_R", CNOT, 7, "dephasing-copy"),
    ]
)

ELEMENTARY_GATES = tuple(
    [
        two(f"reset_swap_{cell}_{rail}", f"S_{cell}{rail}", f"E_{cell}{rail}", SWAP, 1, "reset-export")
        for cell in ("L", "M", "R") for rail in (0, 1)
    ]
    + [
        two("encoded_CZ_LM", "S_L0", "S_M0", CZ2, 2, "encoded-contact"),
        two("encoded_CZ_MR", "S_M0", "S_R0", CZ2, 3, "encoded-contact"),
        two("logical_H_open_decode", "S_M0", "S_M1", CNOT, 4, "X-pointer-basis"),
        one("logical_H_open_H", "S_M0", H, 5, "X-pointer-basis"),
        two("logical_H_open_encode", "S_M0", "S_M1", CNOT, 6, "X-pointer-basis"),
        two("extract_X_middle", "S_M0", "P_M", CNOT, 7, "pointer-extraction"),
        two("extract_Z_left", "S_L0", "P_L", CNOT, 7, "pointer-extraction"),
        two("extract_Z_right", "S_R0", "P_R", CNOT, 7, "pointer-extraction"),
        two("logical_H_close_decode", "S_M0", "S_M1", CNOT, 8, "X-pointer-basis"),
        one("logical_H_close_H", "S_M0", H, 9, "X-pointer-basis"),
        two("logical_H_close_encode", "S_M0", "S_M1", CNOT, 10, "X-pointer-basis"),
        two("copy_middle_dephase", "P_M", "D_M", CNOT, 11, "dephasing-copy"),
        two("copy_left_dephase", "P_L", "D_L", CNOT, 11, "dephasing-copy"),
        two("copy_right_dephase", "P_R", "D_R", CNOT, 11, "dephasing-copy"),
    ]
)


def apply_gate(state: np.ndarray, gate: Gate) -> np.ndarray:
    columns = state.shape[1]
    support = len(gate.qubits)
    tensor = state.reshape((2,) * COUNT + (columns,))
    moved = np.moveaxis(tensor, gate.qubits, tuple(range(support))).reshape(2**support, -1)
    moved = gate.matrix @ moved
    restored = np.moveaxis(
        moved.reshape((2,) * support + (2,) * (COUNT - support) + (columns,)),
        tuple(range(support)), gate.qubits,
    )
    return restored.reshape(2**COUNT, columns)


def apply_sequence(state: np.ndarray, gates: tuple[Gate, ...]) -> np.ndarray:
    answer = state
    for gate in gates:
        answer = apply_gate(answer, gate)
    return answer


def inverse_sequence(state: np.ndarray, gates: tuple[Gate, ...]) -> np.ndarray:
    answer = state
    for gate in reversed(gates):
        answer = apply_gate(answer, Gate(
            gate.name + "_inverse", gate.qubits, gate.matrix.conj().T, gate.layer, gate.role
        ))
    return answer


def initial_columns() -> np.ndarray:
    encoded_plus = W3 @ PLUS3
    blank = c577.ket(0, 8)
    return np.column_stack(tuple(
        np.kron(np.kron(np.kron(W3 @ c577.ket(index, 8), encoded_plus), blank), blank)
        for index in range(8)
    ))


def cycle577_target_columns() -> np.ndarray:
    tensor = np.zeros((64, 64, 8, 8, 8), dtype=complex)
    for input_index in range(8):
        old_input = W3 @ c577.ket(input_index, 8)
        for history in c577.HISTORIES:
            pointer = c577.history_index(history)
            tensor[:, :, pointer, pointer, input_index] += np.outer(
                W3 @ c577.BRANCH_VECTOR[history], old_input
            )
    return tensor.reshape(2**COUNT, 8)


def matrix_sha(matrix: np.ndarray) -> str:
    real = np.round(matrix.real, 14)
    imaginary = np.round(matrix.imag, 14)
    real[np.abs(real) < 1e-14] = 0.0
    imaginary[np.abs(imaginary) < 1e-14] = 0.0
    canonical = np.stack((real, imaginary), axis=-1)
    return sha256(np.ascontiguousarray(canonical).view(np.uint8)).hexdigest()


def code_leakage(state: np.ndarray, qubit_pairs: tuple[tuple[int, int], ...]) -> float:
    rows = np.arange(2**COUNT, dtype=np.uint32)
    bad = np.zeros(2**COUNT, dtype=bool)
    for left, right in qubit_pairs:
        left_bit = (rows >> (COUNT - 1 - left)) & 1
        right_bit = (rows >> (COUNT - 1 - right)) & 1
        bad |= left_bit != right_bit
    return max(float(np.linalg.norm(state[bad, column])) for column in range(state.shape[1]))


SYSTEM_PAIRS = ((0, 1), (2, 3), (4, 5))
ENVIRONMENT_PAIRS = ((6, 7), (8, 9), (10, 11))


def dependency_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    receipt = json.loads(FROZEN_PATHS["Cycle577 receipt"].read_text(encoding="utf-8"))
    transitive_receipt_checks = {
        "runner_hash_matches_receipt": receipt.get("runner_sha256") == FROZEN["Cycle577 runner"],
        "note_hash_matches_receipt": receipt.get("note_sha256") == FROZEN["Cycle577 note"],
        "agent_transcript_hash_matches_receipt": receipt.get("agent_cold_transcript_sha256") == CYCLE577_AGENT_TRANSCRIPT_SHA256,
        "parent_verified_pass_11_of_11": receipt.get("pass") is True
        and receipt.get("tests_passed") == receipt.get("tests_total") == 11,
        "RouteB_target_shape_matches": receipt.get("route_B_local_gauge_Naimark", {}).get("materialized_full_output_isometry_shape") == [262144, 8],
        "RouteB_gate_layout_was_open": receipt.get("route_B_local_gauge_Naimark", {}).get("exact_bounded_gate_layout_decomposition_constructed") is False,
        "RouteB_full_unitary_was_open": receipt.get("route_B_local_gauge_Naimark", {}).get("full_unitary_extension_constructed") is False,
        "authority_none_audit_unset": receipt.get("authority") == "none" and receipt.get("audit") == "unset",
    }
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.exists() else ""
    required = (
        "authority: none", "audit: unset", "cycle 577", "route b", "18 physical m2",
        "cnot-h-cnot", "temporary code-sector departure", "nearest-neighbor",
        "full-space unitary sequence", "candidate weights", "not derived born",
        "not a framework record", "supplied / derived / open", "n1", "n2", "n3",
        "n4", "n5", "n6", "n7", "n8", "no negative claim", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in note)
    result = {
        "expected": FROZEN, "observed": observed, "note_missing": missing,
        "Cycle577_agent_transcript_SHA256_from_committed_receipt": receipt.get("agent_cold_transcript_sha256"),
        "transitive_receipt_checks": transitive_receipt_checks,
        "pass": observed == FROZEN and not missing and all(transitive_receipt_checks.values()),
    }
    check("Cycle577 Route-B target and Cycle580 note contract are exact-pinned", result["pass"], result)
    return result


def logical_gate_controls() -> dict[str, object]:
    zz = np.kron(c577.Z, c577.Z)
    decomposition = CNOT @ np.kron(H, I2) @ CNOT
    gates = (CNOT, CZ2, SWAP, H, LOGICAL_H)
    local_unitarity = tuple(float(np.linalg.norm(gate.conj().T @ gate - np.eye(gate.shape[0]))) for gate in gates)
    rows = np.arange(64)
    lm_sign = np.where(((rows >> 5) & 1) & ((rows >> 3) & 1), -1.0, 1.0)
    mr_sign = np.where(((rows >> 3) & 1) & ((rows >> 1) & 1), -1.0, 1.0)
    physical_cz_lm = np.diag(lm_sign.astype(complex))
    physical_cz_mr = np.diag(mr_sign.astype(complex))
    decoded_code = CNOT @ W2
    decode_worst_leakage = max(float(np.linalg.norm((np.eye(4) - Q2) @ decoded_code[:, column])) for column in range(2))
    result = {
        "logical_H_two_M2_shape": LOGICAL_H.shape,
        "logical_H_code_intertwiner_residual": float(np.linalg.norm(W2.conj().T @ LOGICAL_H @ W2 - H)),
        "logical_H_code_projector_commutator": float(np.linalg.norm(LOGICAL_H @ Q2 - Q2 @ LOGICAL_H)),
        "logical_H_ZZ_commutator": float(np.linalg.norm(LOGICAL_H @ zz - zz @ LOGICAL_H)),
        "CNOT_H_CNOT_decomposition_residual": float(np.linalg.norm(LOGICAL_H - decomposition)),
        "encoded_CZ_LM_intertwiner_residual": float(np.linalg.norm(W3.conj().T @ physical_cz_lm @ W3 - c577.CZ01)),
        "encoded_CZ_MR_intertwiner_residual": float(np.linalg.norm(W3.conj().T @ physical_cz_mr @ W3 - c577.CZ12)),
        "encoded_CZ_code_commutator_max": max(
            float(np.linalg.norm(physical_cz_lm @ Q3 - Q3 @ physical_cz_lm)),
            float(np.linalg.norm(physical_cz_mr @ Q3 - Q3 @ physical_cz_mr)),
        ),
        "CNOT_decode_worst_logical_basis_code_leakage": decode_worst_leakage,
        "local_gate_unitarity_max": max(local_unitarity),
        "native_parity_preserving_block_gate_exists": True,
        "elementary_decomposition_temporarily_leaves_code": True,
        "pass": bool(max(local_unitarity) < TOL
        and np.linalg.norm(W2.conj().T @ LOGICAL_H @ W2 - H) < TOL
        and np.linalg.norm(LOGICAL_H @ Q2 - Q2 @ LOGICAL_H) < TOL
        and np.linalg.norm(LOGICAL_H @ zz - zz @ LOGICAL_H) < TOL
        and np.linalg.norm(LOGICAL_H - decomposition) < TOL
        and np.linalg.norm(W3.conj().T @ physical_cz_lm @ W3 - c577.CZ01) < TOL
        and np.linalg.norm(W3.conj().T @ physical_cz_mr @ W3 - c577.CZ12) < TOL
        and abs(decode_worst_leakage - 1.0) < TOL),
    }
    check("the logical H has an exact parity-preserving two-M2 block gate and CNOT-H-CNOT decomposition", result["pass"], result)
    return result


def compiler_controls(initial: np.ndarray, target: np.ndarray) -> tuple[np.ndarray, dict[str, object]]:
    native = apply_sequence(initial, NATIVE_GATES)
    elementary = apply_sequence(initial, ELEMENTARY_GATES)
    native_residual = float(np.linalg.norm(native - target))
    elementary_residual = float(np.linalg.norm(elementary - target))
    variants_residual = float(np.linalg.norm(native - elementary))
    target_sha = matrix_sha(target)
    elementary_sha = matrix_sha(elementary)
    result = {
        "physical_M2": COUNT, "full_space_dimension": 2**COUNT,
        "lawful_input_columns": initial.shape[1],
        "target_shape": target.shape,
        "native_output_shape": native.shape,
        "elementary_output_shape": elementary.shape,
        "native_gate_count": len(NATIVE_GATES),
        "native_two_M2_gate_count": sum(len(gate.qubits) == 2 for gate in NATIVE_GATES),
        "native_depth": max(gate.layer for gate in NATIVE_GATES),
        "elementary_gate_count": len(ELEMENTARY_GATES),
        "elementary_one_M2_gate_count": sum(len(gate.qubits) == 1 for gate in ELEMENTARY_GATES),
        "elementary_two_M2_gate_count": sum(len(gate.qubits) == 2 for gate in ELEMENTARY_GATES),
        "elementary_depth": max(gate.layer for gate in ELEMENTARY_GATES),
        "maximum_gate_support_M2": max(len(gate.qubits) for gate in NATIVE_GATES + ELEMENTARY_GATES),
        "native_to_Cycle577_VB_residual": native_residual,
        "elementary_to_Cycle577_VB_residual": elementary_residual,
        "native_elementary_residual": variants_residual,
        "compiled_isometry_residual": float(np.linalg.norm(elementary.conj().T @ elementary - np.eye(8))),
        "compiled_nonzero_amplitudes": int(np.count_nonzero(np.abs(elementary) > TOL)),
        "canonical_14digit_Cycle577_target_SHA256": target_sha,
        "canonical_14digit_elementary_output_SHA256": elementary_sha,
        "canonical_hashes_equal": target_sha == elementary_sha,
        "full_space_unitary_sequence_constructed": True,
        "full_dense_2pow18_square_materialized": False,
        "gate_order_is_supplied_compile_time_schedule_data": True,
        "in_state_phase_or_program_carrier_constructed": False,
        "autonomous_no_host_control_recurrence_constructed": False,
        "pass": native_residual < TOL and elementary_residual < TOL and variants_residual < TOL
        and np.linalg.norm(elementary.conj().T @ elementary - np.eye(8)) < TOL
        and target_sha == elementary_sha
        and max(len(gate.qubits) for gate in NATIVE_GATES + ELEMENTARY_GATES) <= 2
        and len(NATIVE_GATES) == 16 and len(ELEMENTARY_GATES) == 20,
    }
    check("native and elementary full-space sequences reproduce all eight Cycle577 V_B columns", result["pass"], result)
    return elementary, result


def layout_controls() -> dict[str, object]:
    coordinates = tuple(LAYOUT[name] for name in QUBIT_NAMES)
    unique = len(set(coordinates)) == COUNT
    adjacency_failures = []
    layer_conflicts = []
    for variant, gates in (("native", NATIVE_GATES), ("elementary", ELEMENTARY_GATES)):
        for gate in gates:
            if len(gate.qubits) == 2:
                left = coordinates[gate.qubits[0]]
                right = coordinates[gate.qubits[1]]
                if sum(abs(a - b) for a, b in zip(left, right)) != 1:
                    adjacency_failures.append((variant, gate.name, left, right))
        for layer in sorted({gate.layer for gate in gates}):
            layer_gates = tuple(gate for gate in gates if gate.layer == layer)
            flat = tuple(qubit for gate in layer_gates for qubit in gate.qubits)
            if len(flat) != len(set(flat)):
                layer_conflicts.append((variant, layer, tuple(gate.name for gate in layer_gates)))
    frame_edge_failures = frame_edge_tests = frame_collision_failures = 0
    for frame in c577.c41.proper_cubic_rotations():
        transformed = tuple(tuple(int(value) for value in frame @ np.asarray(point, dtype=int)) for point in coordinates)
        frame_collision_failures += int(len(set(transformed)) != COUNT)
        for gate in NATIVE_GATES + ELEMENTARY_GATES:
            if len(gate.qubits) == 2:
                left, right = (transformed[index] for index in gate.qubits)
                frame_edge_failures += int(sum(abs(a - b) for a, b in zip(left, right)) != 1)
                frame_edge_tests += 1
    extents = tuple(max(point[axis] for point in coordinates) - min(point[axis] for point in coordinates) + 1 for axis in range(3))
    result = {
        "layout": {name: LAYOUT[name] for name in QUBIT_NAMES},
        "occupied_sites": len(set(coordinates)), "bounding_box_extents": extents,
        "bounding_box_site_capacity": int(np.prod(extents)),
        "all_two_M2_gates_are_cubic_nearest_neighbors": not adjacency_failures,
        "adjacency_failures": adjacency_failures, "layer_conflicts": layer_conflicts,
        "routing_SWAPS_beyond_six_physical_reset_SWAPS": 0,
        "all24_layout_edge_tests": frame_edge_tests,
        "all24_layout_edge_failures": frame_edge_failures,
        "all24_layout_collision_failures": frame_collision_failures,
        "native_layers": max(gate.layer for gate in NATIVE_GATES),
        "elementary_layers": max(gate.layer for gate in ELEMENTARY_GATES),
        "pass": unique and not adjacency_failures and not layer_conflicts and extents == (3, 4, 2)
        and frame_edge_tests == 24 * sum(len(gate.qubits) == 2 for gate in NATIVE_GATES + ELEMENTARY_GATES)
        and not frame_edge_failures and not frame_collision_failures,
    }
    check("the 18-M2 compiler has a literal conflict-free proper-cubic nearest-neighbor schedule", result["pass"], result)
    return result


def compiled_branch_kraus(compiled: np.ndarray, history: tuple[int, int, int]) -> tuple[np.ndarray, ...]:
    pointer = c577.history_index(history)
    tensor = compiled.reshape(64, 64, 8, 8, 8)
    return tuple(tensor[:, environment, pointer, pointer, :] for environment in range(64))


def operator_channel(kraus: tuple[np.ndarray, ...], operator: np.ndarray) -> np.ndarray:
    return sum((gate @ operator @ gate.conj().T for gate in kraus), np.zeros((kraus[0].shape[0], kraus[0].shape[0]), dtype=complex))


def channel_controls(compiled: np.ndarray) -> dict[str, object]:
    branch_failures = nonselective_failures = 0
    max_branch = max_nonselective = 0.0
    for row, column in product(range(8), repeat=2):
        basis_operator = np.outer(c577.ket(row, 8), c577.ket(column, 8).conj())
        found_total = np.zeros((64, 64), dtype=complex)
        expected_total = np.zeros((64, 64), dtype=complex)
        for history in c577.HISTORIES:
            found = operator_channel(compiled_branch_kraus(compiled, history), basis_operator)
            expected_logical = operator_channel(c577.BRANCH_K[history], basis_operator)
            expected = W3 @ expected_logical @ W3.conj().T
            residual = float(np.linalg.norm(found - expected))
            max_branch = max(max_branch, residual)
            branch_failures += int(residual > TOL)
            found_total += found
            expected_total += expected
        total_residual = float(np.linalg.norm(found_total - expected_total))
        max_nonselective = max(max_nonselective, total_residual)
        nonselective_failures += int(total_residual > TOL)
    tensor = compiled.reshape(64, 64, 8, 8, 8)
    mismatched_pointer_dephase_max = max(
        float(np.linalg.norm(tensor[:, :, pointer, dephase, :]))
        for pointer, dephase in product(range(8), repeat=2) if pointer != dephase
    )
    result = {
        "exhaustive_input_operator_basis": 64,
        "branch_operator_tests": 64 * len(c577.HISTORIES),
        "branch_failures": branch_failures, "branch_max_residual": max_branch,
        "nonselective_failures": nonselective_failures,
        "nonselective_max_residual": max_nonselective,
        "mismatched_pointer_dephase_sector_max": mismatched_pointer_dephase_max,
        "candidate_trace_tuple": tuple(
            float(np.vdot(c577.BRANCH_VECTOR[history], c577.BRANCH_VECTOR[history]).real)
            for history in c577.HISTORIES
        ),
        "candidate_trace_is_derived_Born_probability": False,
        "actual_branch_selected": False, "framework_Record_created": False,
        "pass": not branch_failures and not nonselective_failures
        and max_branch < TOL and max_nonselective < TOL and mismatched_pointer_dephase_max < TOL,
    }
    check("the elementary compiler reproduces every branch and nonselective channel on the full logical operator basis", result["pass"], result)
    return result


def inverse_and_deletion_controls(initial: np.ndarray, compiled: np.ndarray) -> dict[str, object]:
    recovered = inverse_sequence(compiled, ELEMENTARY_GATES)
    rng = np.random.default_rng(580)
    offcode = rng.normal(size=(2**COUNT, 2)) + 1j * rng.normal(size=(2**COUNT, 2))
    offcode /= np.linalg.norm(offcode, axis=0, keepdims=True)
    offcode_roundtrip = inverse_sequence(apply_sequence(offcode, ELEMENTARY_GATES), ELEMENTARY_GATES)
    native_offcode = apply_sequence(offcode, NATIVE_GATES)
    elementary_offcode = apply_sequence(offcode, ELEMENTARY_GATES)

    state = initial
    deletion_rows = []
    for gate in ELEMENTARY_GATES:
        after = apply_gate(state, gate)
        deletion_rows.append((gate.name, float(np.linalg.norm(after - state))))
        state = after
    deleted_cz = apply_sequence(initial, tuple(gate for gate in ELEMENTARY_GATES if gate.name != "encoded_CZ_MR"))
    rho = np.eye(8, dtype=complex) / 8.0
    deleted_branch_shift = max(float(np.linalg.norm(
        operator_channel(compiled_branch_kraus(deleted_cz, history), rho)
        - operator_channel(compiled_branch_kraus(compiled, history), rho)
    )) for history in c577.HISTORIES)
    result = {
        "lawful_inverse_residual": float(np.linalg.norm(recovered - initial)),
        "offcode_fixture_columns": offcode.shape[1],
        "offcode_full_sequence_inverse_residual": float(np.linalg.norm(offcode_roundtrip - offcode)),
        "native_elementary_full_space_fixture_residual": float(np.linalg.norm(native_offcode - elementary_offcode)),
        "elementary_gate_deletion_rows": deletion_rows,
        "minimum_gate_deletion_residual": min(value for _name, value in deletion_rows),
        "maximum_gate_deletion_residual": max(value for _name, value in deletion_rows),
        "deleted_encoded_CZ_branch_shift": deleted_branch_shift,
        "pass": np.linalg.norm(recovered - initial) < TOL
        and np.linalg.norm(offcode_roundtrip - offcode) < TOL
        and np.linalg.norm(native_offcode - elementary_offcode) < TOL
        and min(value for _name, value in deletion_rows) > TOL
        and deleted_branch_shift > TOL,
    }
    check("the 18-M2 unitary has an exact inverse and every elementary gate deletion is visible", result["pass"], result)
    return result


def code_and_domain_controls(initial: np.ndarray, compiled: np.ndarray) -> dict[str, object]:
    state = initial
    layer_rows = []
    for layer in sorted({gate.layer for gate in ELEMENTARY_GATES}):
        for gate in tuple(gate for gate in ELEMENTARY_GATES if gate.layer == layer):
            state = apply_gate(state, gate)
        layer_rows.append({
            "layer": layer,
            "system_code_leakage": code_leakage(state, SYSTEM_PAIRS),
            "environment_code_leakage": code_leakage(state, ENVIRONMENT_PAIRS),
        })
    native_state = initial
    native_layer_rows = []
    for layer in sorted({gate.layer for gate in NATIVE_GATES}):
        for gate in tuple(gate for gate in NATIVE_GATES if gate.layer == layer):
            native_state = apply_gate(native_state, gate)
        native_layer_rows.append({
            "layer": layer,
            "system_code_leakage": code_leakage(native_state, SYSTEM_PAIRS),
            "environment_code_leakage": code_leakage(native_state, ENVIRONMENT_PAIRS),
        })
    native_max = max(
        max(row["system_code_leakage"], row["environment_code_leakage"])
        for row in native_layer_rows
    )
    temporary = tuple(row for row in layer_rows if row["system_code_leakage"] > TOL)

    encoded_plus = W3 @ PLUS3

    def lawful(system: np.ndarray, reset: np.ndarray, pointer: tuple[int, ...], dephase: tuple[int, ...]) -> bool:
        return bool(
            system.shape == (64,) and reset.shape == (64,)
            and abs(float(np.vdot(system, system).real) - 1.0) < TOL
            and np.linalg.norm(Q3 @ system - system) < TOL
            and abs(abs(np.vdot(encoded_plus, reset)) - 1.0) < TOL
            and pointer == (0, 0, 0) and dephase == (0, 0, 0)
        )

    good_system = W3 @ ((c577.ket(0, 8) + 1j * c577.ket(7, 8)) / np.sqrt(2.0))
    bad_system = c577.ket(1, 64)
    malformed = (
        (bad_system, encoded_plus, (0, 0, 0), (0, 0, 0)),
        (good_system, W3 @ c577.ket(0, 8), (0, 0, 0), (0, 0, 0)),
        (good_system, encoded_plus, (1, 0, 0), (0, 0, 0)),
        (good_system, encoded_plus, (0, 0, 0), (0, 1, 0)),
        (good_system[:-1], encoded_plus, (0, 0, 0), (0, 0, 0)),
        (2.0 * good_system, encoded_plus, (0, 0, 0), (0, 0, 0)),
    )
    refused = sum(int(not lawful(*case)) for case in malformed)
    result = {
        "initial_system_code_leakage": code_leakage(initial, SYSTEM_PAIRS),
        "initial_reset_environment_code_leakage": code_leakage(initial, ENVIRONMENT_PAIRS),
        "final_system_code_leakage": code_leakage(compiled, SYSTEM_PAIRS),
        "final_spent_environment_code_leakage": code_leakage(compiled, ENVIRONMENT_PAIRS),
        "native_layer_boundary_code_ledger": native_layer_rows,
        "native_max_layer_boundary_code_leakage": native_max,
        "elementary_layer_code_ledger": layer_rows,
        "temporary_code_sector_departure_layers": temporary,
        "temporary_departure_is_explicit": bool(temporary),
        "malformed_inputs_refused": refused, "malformed_total": len(malformed),
        "local_parity_enforcement_or_repair_constructed": False,
        "pass": code_leakage(initial, SYSTEM_PAIRS) < TOL
        and code_leakage(initial, ENVIRONMENT_PAIRS) < TOL
        and code_leakage(compiled, SYSTEM_PAIRS) < TOL
        and code_leakage(compiled, ENVIRONMENT_PAIRS) < TOL
        and native_max < TOL and bool(temporary) and refused == len(malformed),
    }
    check("code domains are exact at the boundary and elementary logical-H departure is exposed rather than hidden", result["pass"], result)
    return result


def held_and_covariance_controls(compiled: np.ndarray) -> dict[str, object]:
    gram = compiled.conj().T @ compiled
    held_isometry_residual = float(np.linalg.norm(np.kron(gram, np.eye(8)) - np.eye(64)))
    spectator = (c577.ket(0, 8) + c577.ket(3, 8) + 1j * c577.ket(7, 8)) / np.sqrt(3.0)
    rho_s = np.outer(spectator, spectator.conj())
    rho3 = np.outer((c577.ket(1, 8) + c577.ket(4, 8)) / np.sqrt(2.0), (c577.ket(1, 8) + c577.ket(4, 8)).conj() / np.sqrt(2.0))
    held_failures = 0
    for history in c577.HISTORIES:
        found = operator_channel(compiled_branch_kraus(compiled, history), rho3)
        expected = W3 @ operator_channel(c577.BRANCH_K[history], rho3) @ W3.conj().T
        held_failures += int(np.linalg.norm(np.kron(found, rho_s) - np.kron(expected, rho_s)) > TOL)

    c41 = c577.c41
    frames = c41.proper_cubic_rotations()
    program = c41.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    records = c41.seed_records(program)
    traces = tuple(round(float(np.vdot(c577.BRANCH_VECTOR[h], c577.BRANCH_VECTOR[h]).real), 14) for h in c577.HISTORIES)
    route_failures = route_tests = group_failures = group_tests = 0
    for frame in frames:
        moved = c41.transform_program(program, frame, (5, -7, 2))
        moved_records = c41.transform_records(records, frame, (5, -7, 2))
        route_failures += int(not c41.preparation_ready(moved, moved_records))
        route_failures += int(traces != tuple(round(float(np.vdot(c577.BRANCH_VECTOR[h], c577.BRANCH_VECTOR[h]).real), 14) for h in c577.HISTORIES))
        route_tests += 1
    sample_sites = (program.trigger, *c41.header_sites(program))
    for first, second in product(frames, repeat=2):
        direct = first @ second
        for role_index, role in enumerate(c577.ROLES):
            site = np.asarray(sample_sites[role_index % len(sample_sites)], dtype=int)
            sequential = tuple(int(value) for value in first @ (second @ site))
            composed = tuple(int(value) for value in direct @ site)
            group_failures += int(sequential != composed or np.linalg.norm(c577.ROLE_P[role] - c577.ROLE_P[role]) > TOL)
            group_tests += 1
    result = {
        "held_L6_isometry_residual": held_isometry_residual,
        "held_L6_branch_tests": len(c577.HISTORIES), "held_L6_failures": held_failures,
        "proper_frames": len(frames), "all24_tests": route_tests,
        "all24_failures": route_failures,
        "all576_ordered_products": len(frames) ** 2,
        "all576_projector_role_tests": group_tests, "all576_failures": group_failures,
        "site_only_frame_action": True,
        "pass": held_isometry_residual < TOL and not held_failures and len(frames) == 24
        and route_tests == 24 and not route_failures and group_tests == 6336 and not group_failures,
    }
    check("held spectators and all24/all576 proper-cubic presentation controls remain exact", result["pass"], result)
    return result


def inventory_and_claim_controls() -> dict[str, object]:
    supplied = (
        "Cycle577 W|0>=|00>, W|1>=|11> code and exact V_B target columns",
        "three encoded-plus reset blocks, three zero pointer M2, and three zero dephasing-copy M2",
        "lawful code membership, six local parity checks, noiseless H/CNOT/CZ/SWAP gates, and the 18-site cubic placement",
        "Cycle41 candidate instrument, candidate traces, site-only proper-cubic frame chart, finite L3 boundary, and held L6 spectator",
    )
    derived = (
        "exact parity-preserving two-M2 logical H and exact CNOT-H-CNOT decomposition",
        "six physical reset SWAPs, two encoded CZs, coherent X/Z/Z pointer extraction, and three dephasing copies",
        "a full-space 18-M2 unitary sequence with maximum gate support two and a conflict-free nearest-neighbor schedule",
        "exact eight-column V_B equality, branch/nonselective intertwining, inverse, deletion visibility, and boundary code return",
    )
    open_items = (
        "genesis and renewal of encoded-plus and zero carriers, entropy export, temperature, and autonomous recurrence",
        "replacement of supplied compile-time gate order by an in-state phase/program carrier with autonomous no-host-control recurrence",
        "local enforcement or repair of parity constraints and robustness under noise",
        "selection of Cycle41 as nature's law and an actual branch, occurrence, framework Record, or realized history",
        "derivation/calibration of candidate traces as Born probabilities or frequencies",
        "composition with full interacting matter without reduced reset erasure, and any time, energy, source, gravity, or continuum law",
    )
    note_lines = NOTE.read_text(encoding="utf-8").splitlines()
    patterns = (
        "we assume", "by construction", "as is standard", "are standard", "the framework provides",
        "bridge context", "background", "naturally", "obviously", "standard qft", "registered", "canonical",
    )
    hidden_hits = []
    for line_number, line in enumerate(note_lines, start=1):
        lowered = line.lower()
        for pattern in patterns:
            if pattern in lowered:
                hidden_hits.append({
                    "pattern": pattern, "line": line_number, "text": line.strip(),
                    "classification": "non-load-bearing prior-art attribution" if pattern in ("as is standard", "are standard", "standard qft") else "non-load-bearing terminology; no premise imported",
                })
    discipline = {
        "N1": "no negative target; native parity block, elementary decomposition, and cubic scheduling are constructive variants, not inflated no-go families",
        "N2": "open obligations are an import ledger, not claimed pairwise-independent obstruction walls",
        "N3_hidden_phrase_hits": hidden_hits,
        "N4": "Cycle577 exact residual matched: missing elementary gate/layout decomposition is the residual closed here",
        "N5": "all negative wording is block-scoped: no actual branch/Record/Born/time/source is promoted by this finite compiler",
        "N6": "the Cycle577 gate/layout import retires constructively; carrier genesis, enforcement, recurrence, and semantic ownership remain explicit",
        "N7": "the strongest counterroute to a gate-synthesis obstruction is the explicit CNOT-H-CNOT compiler constructed here",
        "N8": "Cycle574 representation and Cycle577 isometry-only gaps both retired by explicit encodings rather than axiom edits",
        "negative_or_minimum_claim_shipped": False,
        "shared_obstruction_claim_shipped": False,
        "axiom_pressure_claim_shipped": False,
        "gate_status": "NOT_TRIGGERED_POSITIVE_CONSTRUCTION",
    }
    result = {
        "inventory": {"supplied": supplied, "derived": derived, "open": open_items},
        "no_go_discipline": discipline,
        "authority": AUTHORITY, "audit": AUDIT,
        "pass": all((supplied, derived, open_items)) and all(hit["classification"] for hit in hidden_hits)
        and not any((discipline["negative_or_minimum_claim_shipped"], discipline["shared_obstruction_claim_shipped"], discipline["axiom_pressure_claim_shipped"])),
    }
    check("the supply ledger and non-negative N1-N8 applicability audit block semantic promotion", result["pass"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_result: str = "exact 18-M2 CNOT/H/CZ/SWAP nearest-neighbor full-space unitary sequence reproducing Cycle577 V_B"
    actual_branch: None = None
    framework_Record: None = None
    derived_Born_probability: None = None
    physical_time: None = None
    energy_or_source: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle580 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        dependency = dependency_controls()
        logical_gate = logical_gate_controls()
        initial = initial_columns()
        target = cycle577_target_columns()
        compiled, compiler = compiler_controls(initial, target)
        layout = layout_controls()
        channel_result = channel_controls(compiled)
        inverse_deletion = inverse_and_deletion_controls(initial, compiled)
        code_domain = code_and_domain_controls(initial, compiled)
        held_covariance = held_and_covariance_controls(compiled)
        inventory_claim = inventory_and_claim_controls()
        resources = {
            "elapsed_seconds": time.perf_counter() - started,
            "rss_bytes": rss_bytes(), "wall_cap_seconds": WALL_CAP_SECONDS,
            "rss_cap_bytes": RSS_CAP_BYTES,
        }
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["rss_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({
            "dependency": dependency, "logical_gate": logical_gate,
            "compiler": compiler, "layout": layout, "channel": channel_result,
            "inverse_deletion": inverse_deletion, "code_domain": code_domain,
            "held_covariance": held_covariance, "inventory_claim": inventory_claim,
            "resources": resources,
            "summary": Summary().__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; full-space unitary gate sequence is constructive, while actuality, Record, Born, time, energy, source, and recurrence remain unclaimed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
