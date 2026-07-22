#!/usr/bin/env python3
"""Cycle582: autonomous-controller/resource tournament for Cycle580 V_B.

The runner tests an in-state program/cursor law at finite supplied horizon, a
finite conveyor/debit ledger, and three reversible uncompute/reset attempts.
Copied pointers remain conditional outputs rather than framework Records;
candidate traces remain diagnostics rather than derived probabilities.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22 as c580


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_L41_AUTONOMOUS_RECURRENCE_RESOURCE_TOURNAMENT_CYCLE582_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
PHASES = 11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

FROZEN_PATHS = {
    "Cycle580 runner": ROOT / "scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py",
    "Cycle580 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md",
    "Cycle580 receipt": ROOT / "outputs/physical_l41_elementary_gate_layout_compiler_cycle580_receipt_2026_07_22.json",
}
FROZEN = {
    "Cycle580 runner": "c46917d4a932cd3ad9a78e0547625055f5adf9d5cf7393700d7e6715dd515cd3",
    "Cycle580 note": "e8ca5acdaec0c7ec5f0ba9772d7736352bcf132e961483d93f19c679439df276",
    "Cycle580 receipt": "bff5c4a6a691a991dd18058e7600dc7d8e102e569f4d32ef9f91711eef3c14ab",
}
CYCLE580_AGENT_TRANSCRIPT_SHA256 = "186fa69e34c55655194d79329fc2fbf1c5521006f4ffc295c5a49c70747e6763"


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


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.linalg.svd(left - right, compute_uv=False).sum() / 2.0)


Sparse = dict[int, np.ndarray]
ControllerSparse = dict[tuple[int, int, int], np.ndarray]


def add_vector(mapping: dict, key: object, value: np.ndarray) -> None:
    if key in mapping:
        mapping[key] += value
    else:
        mapping[key] = value.copy()


def prune(state: Sparse) -> Sparse:
    return {word: value for word, value in state.items() if np.linalg.norm(value) > 1e-13}


def sparse_gate(state: Sparse, matrix: np.ndarray, qubits: tuple[int, ...], count: int) -> Sparse:
    masks = tuple(1 << (count - 1 - qubit) for qubit in qubits)
    support = len(qubits)
    output: Sparse = {}
    for word, amplitudes in state.items():
        input_index = 0
        for mask in masks:
            input_index = (input_index << 1) | int(bool(word & mask))
        for output_index in range(2**support):
            coefficient = matrix[output_index, input_index]
            if abs(coefficient) < 1e-15:
                continue
            new_word = word
            for position, mask in enumerate(masks):
                bit = (output_index >> (support - 1 - position)) & 1
                new_word = (new_word | mask) if bit else (new_word & ~mask)
            add_vector(output, new_word, coefficient * amplitudes)
    return prune(output)


def sparse_gram(state: Sparse) -> np.ndarray:
    return sum((np.outer(value.conj(), value) for value in state.values()), np.zeros((8, 8), dtype=complex))


def sparse_distance(left: Sparse, right: Sparse) -> float:
    total = 0.0
    zero = np.zeros(8, dtype=complex)
    for key in set(left) | set(right):
        total += float(np.linalg.norm(left.get(key, zero) - right.get(key, zero)) ** 2)
    return float(np.sqrt(total))


def local_index(word: int, qubits: tuple[int, ...], count: int) -> int:
    result = 0
    for qubit in qubits:
        result = (result << 1) | int(bool(word & (1 << (count - 1 - qubit))))
    return result


def clear_qubits(word: int, qubits: tuple[int, ...], count: int) -> int:
    result = word
    for qubit in qubits:
        result &= ~(1 << (count - 1 - qubit))
    return result


def reduced_density_dict(state: Sparse, coefficients: np.ndarray, qubits: tuple[int, ...], count: int) -> dict[tuple[int, int], complex]:
    groups: dict[int, dict[int, complex]] = {}
    for word, vector in state.items():
        amplitude = np.dot(vector, coefficients)
        if abs(amplitude) < 1e-14:
            continue
        complement = clear_qubits(word, qubits, count)
        index = local_index(word, qubits, count)
        groups.setdefault(complement, {})[index] = groups.setdefault(complement, {}).get(index, 0.0j) + amplitude
    rho: dict[tuple[int, int], complex] = {}
    for amplitudes in groups.values():
        for left, right in product(amplitudes, repeat=2):
            rho[(left, right)] = rho.get((left, right), 0.0j) + amplitudes[left] * amplitudes[right].conjugate()
    return {key: value for key, value in rho.items() if abs(value) > 1e-13}


def density_dict_distance(left: dict[tuple[int, int], complex], right: dict[tuple[int, int], complex]) -> float:
    return float(np.sqrt(sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in set(left) | set(right))))


def density_dict_to_dense(rho: dict[tuple[int, int], complex], dimension: int) -> np.ndarray:
    result = np.zeros((dimension, dimension), dtype=complex)
    for (left, right), value in rho.items():
        result[left, right] = value
    return result


def code_leakage(state: Sparse, pairs: tuple[tuple[int, int], ...], count: int) -> float:
    column_bad = np.zeros(8, dtype=float)
    for word, vector in state.items():
        bad = any(
            bool(word & (1 << (count - 1 - left))) != bool(word & (1 << (count - 1 - right)))
            for left, right in pairs
        )
        if bad:
            column_bad += np.abs(vector) ** 2
    return float(np.sqrt(column_bad.max()))


def state_count(horizon: int) -> int:
    return 6 + 12 * horizon


def slot_qubits(slot: int) -> tuple[int, ...]:
    return tuple(range(6 + 12 * slot, 6 + 12 * (slot + 1)))


def slot_environment_qubits(slot: int) -> tuple[int, ...]:
    return tuple(range(6 + 12 * slot, 12 + 12 * slot))


def remap_qubits(qubits: tuple[int, ...], slot: int) -> tuple[int, ...]:
    return tuple(qubit if qubit < 6 else 6 + 12 * slot + (qubit - 6) for qubit in qubits)


def initial_sparse(horizon: int) -> Sparse:
    count = state_count(horizon)
    encoded_plus = c580.W3 @ c580.PLUS3
    reset_indices = tuple(int(index) for index in np.flatnonzero(np.abs(encoded_plus) > TOL))
    state: Sparse = {}
    for reset_words in product(reset_indices, repeat=horizon):
        reset_amplitude = np.prod(tuple(encoded_plus[index] for index in reset_words))
        for logical_input in range(8):
            system_word = int(np.argmax(np.abs(c580.W3[:, logical_input])))
            word = system_word << (12 * horizon)
            for slot, reset_word in enumerate(reset_words):
                word |= reset_word << (12 * (horizon - 1 - slot) + 6)
            vector = state.setdefault(word, np.zeros(8, dtype=complex))
            vector[logical_input] += reset_amplitude
    return prune(state)


def layer_gates(phase: int) -> tuple[c580.Gate, ...]:
    return tuple(gate for gate in c580.ELEMENTARY_GATES if gate.layer == phase + 1)


def apply_invocation(state: Sparse, slot: int, horizon: int, noisy_open_h: np.ndarray | None = None) -> Sparse:
    answer = state
    count = state_count(horizon)
    for phase in range(PHASES):
        for gate in layer_gates(phase):
            matrix = noisy_open_h if noisy_open_h is not None and gate.name == "logical_H_open_H" else gate.matrix
            answer = sparse_gate(answer, matrix, remap_qubits(gate.qubits, slot), count)
    return answer


def controller_from_quantum(state: Sparse, phase: int = 0, cursor: int = 0) -> ControllerSparse:
    return {(word, phase, cursor): vector.copy() for word, vector in state.items()}


def controller_groups(state: ControllerSparse) -> dict[tuple[int, int], Sparse]:
    groups: dict[tuple[int, int], Sparse] = {}
    for (word, phase, cursor), vector in state.items():
        groups.setdefault((phase, cursor), {})[word] = vector.copy()
    return groups


def autonomous_step(state: ControllerSparse, horizon: int, *, suppress_head_advance: bool = False,
                    suppress_cursor_advance: bool = False) -> ControllerSparse:
    count = state_count(horizon)
    output: ControllerSparse = {}
    for (phase, cursor), quantum in controller_groups(state).items():
        if not (0 <= phase < PHASES and 0 <= cursor < horizon):
            raise ValueError("controller leaves declared phase/cursor code domain")
        evolved = quantum
        for gate in layer_gates(phase):
            evolved = sparse_gate(evolved, gate.matrix, remap_qubits(gate.qubits, cursor), count)
        next_phase = phase if suppress_head_advance else (phase + 1) % PHASES
        next_cursor = cursor
        if phase == PHASES - 1 and not suppress_head_advance and not suppress_cursor_advance:
            next_cursor = (cursor + 1) % horizon
        for word, vector in evolved.items():
            add_vector(output, (word, next_phase, next_cursor), vector)
    return {key: value for key, value in output.items() if np.linalg.norm(value) > 1e-13}


def autonomous_inverse_step(state: ControllerSparse, horizon: int) -> ControllerSparse:
    count = state_count(horizon)
    output: ControllerSparse = {}
    for (phase, cursor), quantum in controller_groups(state).items():
        previous_phase = (phase - 1) % PHASES
        previous_cursor = (cursor - 1) % horizon if phase == 0 else cursor
        evolved = quantum
        for gate in reversed(layer_gates(previous_phase)):
            evolved = sparse_gate(evolved, gate.matrix.conj().T, remap_qubits(gate.qubits, previous_cursor), count)
        for word, vector in evolved.items():
            add_vector(output, (word, previous_phase, previous_cursor), vector)
    return {key: value for key, value in output.items() if np.linalg.norm(value) > 1e-13}


def controller_quantum(state: ControllerSparse, phase: int, cursor: int) -> Sparse:
    result = {
        word: vector.copy() for (word, found_phase, found_cursor), vector in state.items()
        if found_phase == phase and found_cursor == cursor
    }
    if len(result) != len(state):
        raise ValueError("controller state is not on the expected single phase/cursor rail")
    return result


def controller_distance(left: ControllerSparse, right: ControllerSparse) -> float:
    total = 0.0
    zero = np.zeros(8, dtype=complex)
    for key in set(left) | set(right):
        total += float(np.linalg.norm(left.get(key, zero) - right.get(key, zero)) ** 2)
    return float(np.sqrt(total))


def one_hot_embedding(rails: int) -> np.ndarray:
    result = np.zeros((2**rails, rails), dtype=complex)
    for rail in range(rails):
        result[1 << (rails - 1 - rail), rail] = 1.0
    return result


def dense_from_sparse(state: Sparse, count: int) -> np.ndarray:
    result = np.zeros((2**count, 8), dtype=complex)
    for word, vector in state.items():
        result[word, :] = vector
    return result


def dependency_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    receipt = json.loads(FROZEN_PATHS["Cycle580 receipt"].read_text(encoding="utf-8"))
    receipt_checks = {
        "runner": receipt.get("runner_sha256") == FROZEN["Cycle580 runner"],
        "note": receipt.get("note_sha256") == FROZEN["Cycle580 note"],
        "transcript": receipt.get("agent_cold_transcript_sha256") == CYCLE580_AGENT_TRANSCRIPT_SHA256,
        "parent_10_of_10": receipt.get("pass") is True and receipt.get("tests_passed") == receipt.get("tests_total") == 10,
        "single_invocation_closed": receipt.get("scope_boundary", {}).get("single_invocation_gate_layout_closed") is True,
        "recurrence_open": receipt.get("scope_boundary", {}).get("autonomous_recurrence_closed") is False,
        "authority_audit": receipt.get("authority") == "none" and receipt.get("audit") == "unset",
    }
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.exists() else ""
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c",
        "in-state", "finite stock is not renewable", "copied pointer is not a framework record",
        "candidate traces are not derived born", "phase is not time", "carrier count is not energy",
        "supplied / derived / open", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8",
        "n1 status: **fail**", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in note)
    result = {
        "expected": FROZEN, "observed": observed, "receipt_checks": receipt_checks,
        "Cycle580_agent_transcript_SHA256_from_receipt": receipt.get("agent_cold_transcript_sha256"),
        "note_missing": missing,
        "pass": observed == FROZEN and all(receipt_checks.values()) and not missing,
    }
    check("Cycle580 single-invocation target and Cycle582 note contract are exact-pinned", result["pass"], result)
    return result


def route_a_controls() -> tuple[ControllerSparse, dict[str, object]]:
    # One invocation: exact equality to the dense Cycle580 elementary compiler.
    initial_one = initial_sparse(1)
    controlled_one = controller_from_quantum(initial_one)
    for _step in range(PHASES):
        controlled_one = autonomous_step(controlled_one, 1)
    found_one = dense_from_sparse(controller_quantum(controlled_one, 0, 0), 18)
    dense_initial = c580.initial_columns()
    target_one = c580.apply_sequence(dense_initial, c580.ELEMENTARY_GATES)
    one_residual = float(np.linalg.norm(found_one - target_one))

    horizon = 2
    count = state_count(horizon)
    initial = initial_sparse(horizon)
    controller = controller_from_quantum(initial)
    direct = initial
    boundary_states: list[ControllerSparse] = []
    direct_residuals = []
    inverse_step_residuals = []
    for invocation in range(horizon):
        for _phase in range(PHASES):
            before = controller
            after = autonomous_step(before, horizon)
            recovered = autonomous_inverse_step(after, horizon)
            inverse_step_residuals.append(controller_distance(recovered, before))
            controller = after
        direct = apply_invocation(direct, invocation, horizon)
        expected_cursor = (invocation + 1) % horizon
        direct_residuals.append(sparse_distance(controller_quantum(controller, 0, expected_cursor), direct))
        boundary_states.append(controller)

    coefficients = (c580.c577.ket(0, 8) + 1j * c580.c577.ket(7, 8)) / np.sqrt(2.0)
    slot0 = slot_qubits(0)
    slot1 = slot_qubits(1)
    first_quantum = controller_quantum(boundary_states[0], 0, 1)
    final_quantum = controller_quantum(boundary_states[1], 0, 0)
    archive_first = reduced_density_dict(first_quantum, coefficients, slot0, count)
    archive_final = reduced_density_dict(final_quantum, coefficients, slot0, count)
    fresh_initial = reduced_density_dict(initial, coefficients, slot1, count)
    fresh_after_first = reduced_density_dict(first_quantum, coefficients, slot1, count)
    archive_invariance = density_dict_distance(archive_first, archive_final)
    unused_fresh_invariance = density_dict_distance(fresh_initial, fresh_after_first)

    # Head/cursor deletions are active.
    deleted_head = controller_from_quantum(initial)
    for step in range(PHASES * horizon):
        deleted_head = autonomous_step(deleted_head, horizon, suppress_head_advance=(step == 3))
    head_deletion_residual = controller_distance(deleted_head, controller)
    deleted_cursor = controller_from_quantum(initial)
    for step in range(PHASES * horizon):
        deleted_cursor = autonomous_step(deleted_cursor, horizon, suppress_cursor_advance=(step == PHASES - 1))
    cursor_deletion_residual = controller_distance(deleted_cursor, controller)

    # Boundary code and coherent gate-noise controls.
    system_pairs = ((0, 1), (2, 3), (4, 5))
    environment_pairs = tuple(
        (6 + 12 * slot + offset, 6 + 12 * slot + offset + 1)
        for slot in range(horizon) for offset in (0, 2, 4)
    )
    final_system_leakage = code_leakage(final_quantum, system_pairs, count)
    final_environment_leakage = code_leakage(final_quantum, environment_pairs, count)
    noise_rows = []
    for epsilon in (1e-3, 1e-2):
        rz = np.diag((np.exp(-0.5j * epsilon), np.exp(0.5j * epsilon)))
        noisy = apply_invocation(initial_one, 0, 1, noisy_open_h=rz @ c580.H)
        ideal = controller_quantum(controlled_one, 0, 0)
        noise_rows.append((epsilon, sparse_distance(noisy, ideal)))

    h11 = one_hot_embedding(PHASES)
    h2 = one_hot_embedding(horizon)
    malformed_controller_cases = (
        (PHASES, 0, 1, 1), (0, horizon, 1, 1),
        (0, 0, 0, 1), (0, 0, 2, 1), (0, 0, 1, 0), (0, 0, 1, 2),
    )

    def lawful_controller(case: tuple[int, int, int, int]) -> bool:
        phase, cursor, head_occupancy, cursor_occupancy = case
        return 0 <= phase < PHASES and 0 <= cursor < horizon and head_occupancy == cursor_occupancy == 1

    malformed_refused = sum(int(not lawful_controller(case)) for case in malformed_controller_cases)
    result = {
        "route": "A priority in-state phase/program plus resource cursor",
        "train_horizon": horizon,
        "single_invocation_Cycle580_VB_residual": one_residual,
        "repeated_direct_residuals": direct_residuals,
        "autonomous_step_inverse_residual_max": max(inverse_step_residuals),
        "final_repeated_Gram_residual": float(np.linalg.norm(sparse_gram(final_quantum) - np.eye(8))),
        "slot0_archive_invariance_after_second_invocation": archive_invariance,
        "slot1_unused_fresh_invariance_after_first_invocation": unused_fresh_invariance,
        "head_advance_deletion_residual": head_deletion_residual,
        "cursor_advance_deletion_residual": cursor_deletion_residual,
        "final_system_code_leakage": final_system_leakage,
        "final_all_resource_environment_code_leakage": final_environment_leakage,
        "coherent_H_noise_rows": noise_rows,
        "head_H11_embedding_shape": h11.shape,
        "cursor_H2_embedding_shape": h2.shape,
        "head_H11_isometry_residual": float(np.linalg.norm(h11.conj().T @ h11 - np.eye(PHASES))),
        "cursor_H2_isometry_residual": float(np.linalg.norm(h2.conj().T @ h2 - np.eye(horizon))),
        "physical_M2_at_train_horizon": count + PHASES + horizon,
        "maximum_phase_cursor_controlled_support_M2": 4,
        "same_autonomous_step_law_repeated": True,
        "host_selects_layer": False,
        "host_repeats_same_law": True,
        "controller_nearest_neighbor_gate_decomposition_constructed": False,
        "local_controller_code_enforcement_constructed": False,
        "malformed_controller_states_refused": malformed_refused,
        "malformed_controller_total": len(malformed_controller_cases),
        "phase_is_time": False,
        "pass": one_residual < TOL and max(direct_residuals) < TOL
        and max(inverse_step_residuals) < TOL
        and np.linalg.norm(sparse_gram(final_quantum) - np.eye(8)) < TOL
        and archive_invariance < TOL and unused_fresh_invariance < TOL
        and head_deletion_residual > TOL and cursor_deletion_residual > TOL
        and final_system_leakage < TOL and final_environment_leakage < TOL
        and noise_rows[1][1] > noise_rows[0][1] > TOL
        and np.linalg.norm(h11.conj().T @ h11 - np.eye(PHASES)) < TOL
        and np.linalg.norm(h2.conj().T @ h2 - np.eye(horizon)) < TOL
        and malformed_refused == len(malformed_controller_cases),
    }
    check("Route A gives exact finite-horizon recurrence under one in-state-controlled update with explicit locality residual", result["pass"], result)
    return controller, result


def rotate_packets(labels: tuple[int, ...], deleted_swap: int | None = None) -> tuple[int, ...]:
    output = list(labels)
    for position in range(len(output) - 1):
        if position != deleted_swap:
            output[position], output[position + 1] = output[position + 1], output[position]
    return tuple(output)


def route_b_controls() -> tuple[Sparse, dict[str, object]]:
    train_horizon, held_horizon = 2, 3
    held_count = state_count(held_horizon)
    initial = initial_sparse(held_horizon)
    controller = controller_from_quantum(initial)
    boundary_quantum = []
    for invocation in range(held_horizon):
        for _phase in range(PHASES):
            controller = autonomous_step(controller, held_horizon)
        boundary_quantum.append(controller_quantum(controller, 0, (invocation + 1) % held_horizon))
    final = boundary_quantum[-1]
    held_gram_residual = float(np.linalg.norm(sparse_gram(final) - np.eye(8)))
    coefficients = (c580.c577.ket(1, 8) + c580.c577.ket(6, 8)) / np.sqrt(2.0)
    slot0 = slot_qubits(0)
    archive_at_first = reduced_density_dict(boundary_quantum[0], coefficients, slot0, held_count)
    archive_at_held = reduced_density_dict(final, coefficients, slot0, held_count)
    held_archive_residual = density_dict_distance(archive_at_first, archive_at_held)

    # The next modulo-cursor invocation reuses spent slot zero and is outside
    # the lawful finite-stock domain.  Its visible change is a capacity alarm,
    # not a universal no-go or a renewal theorem.
    overrun = controller
    for _phase in range(PHASES):
        overrun = autonomous_step(overrun, held_horizon)
    overrun_quantum = controller_quantum(overrun, 0, 1)
    overrun_archive = reduced_density_dict(overrun_quantum, coefficients, slot0, held_count)
    overrun_slot0_change = density_dict_distance(archive_at_held, overrun_archive)

    labels = tuple(range(held_horizon))
    rotated = rotate_packets(labels)
    # Explicit inverse is a right rotation; write it directly to avoid calling
    # the forward routine a second time and hiding direction.
    inverse_recovered = (rotated[-1],) + rotated[:-1]
    deleted = rotate_packets(labels, deleted_swap=0)
    debit_rows = tuple({
        "completed_invocations": invocation,
        "fresh_slots_remaining": held_horizon - invocation,
        "spent_archive_slots": invocation,
        "fresh_M2_remaining": 12 * (held_horizon - invocation),
    } for invocation in range(held_horizon + 1))
    result = {
        "route": "B finite conveyor/reservoir debit",
        "train_horizon": train_horizon, "held_horizon": held_horizon,
        "active_system_M2": 6, "fresh_resource_M2_per_invocation": 12,
        "held_initial_fresh_resource_M2": 12 * held_horizon,
        "phase_head_M2": PHASES, "held_cursor_M2": held_horizon,
        "held_total_physical_M2": held_count + PHASES + held_horizon,
        "debit_rows": debit_rows,
        "history_owner": "each spent 12-M2 packet retains old-input environment plus pointer/dephasing outputs",
        "held_Gram_residual": held_gram_residual,
        "slot0_archive_held_invariance": held_archive_residual,
        "overrun_reuses_spent_slot0_change": overrun_slot0_change,
        "packet_labels_after_left_rotation": rotated,
        "packet_inverse_recovered": inverse_recovered,
        "deleted_conveyor_swap_labels": deleted,
        "conveyor_two_M2_SWAPS_per_boundary": 12 * (held_horizon - 1),
        "conveyor_depth_per_boundary": held_horizon - 1,
        "phase_controlled_active_station_max_support_M2": 3,
        "replicated_local_phase_ring_synchronization_genesis_derived": False,
        "literal_conveyor_geometry_constructed": False,
        "finite_stock_is_renewable": False,
        "stationary_fresh_spent_balance_derived": False,
        "pass": held_gram_residual < TOL and held_archive_residual < TOL
        and overrun_slot0_change > TOL and inverse_recovered == labels
        and deleted != rotated and debit_rows[-1]["fresh_slots_remaining"] == 0,
    }
    check("Route B gives an exact held-horizon debit/archive ledger and visibly refuses to call finite stock renewable", result["pass"], result)
    return final, result


def partial_density_dense(vector: np.ndarray, dimensions: tuple[int, ...], keep_axis: int) -> np.ndarray:
    tensor = vector.reshape(dimensions)
    moved = np.moveaxis(tensor, keep_axis, 0).reshape(dimensions[keep_axis], -1)
    return moved @ moved.conj().T


def append_blank_qubits(matrix: np.ndarray, blanks: int) -> Sparse:
    output: Sparse = {}
    for row in np.flatnonzero(np.max(np.abs(matrix), axis=1) > TOL):
        output[int(row) << blanks] = matrix[int(row), :].copy()
    return output


def sparse_inverse_cycle580(state: Sparse, count: int) -> Sparse:
    answer = state
    for gate in reversed(c580.ELEMENTARY_GATES):
        answer = sparse_gate(answer, gate.matrix.conj().T, gate.qubits, count)
    return answer


def active_pure_fidelity(state: Sparse, coefficients: np.ndarray, active_width: int,
                         target: np.ndarray, count: int) -> float:
    archive_width = count - active_width
    grouped: dict[int, complex] = {}
    for word, vector in state.items():
        amplitude = np.dot(vector, coefficients)
        active = word >> archive_width
        archive = word & ((1 << archive_width) - 1)
        grouped[archive] = grouped.get(archive, 0.0j) + target[active].conjugate() * amplitude
    return float(sum(abs(value) ** 2 for value in grouped.values()))


def route_c_controls() -> dict[str, object]:
    initial = c580.initial_columns()
    compiled = c580.apply_sequence(initial, c580.ELEMENTARY_GATES)
    recovered = c580.inverse_sequence(compiled, c580.ELEMENTARY_GATES)
    coefficient0 = c580.c577.ket(0, 8)
    output0 = compiled @ coefficient0
    recovered0 = recovered @ coefficient0
    dims = (64, 64, 8, 8)
    pointer_before = partial_density_dense(output0, dims, 2)
    pointer_after = partial_density_dense(recovered0, dims, 2)
    dephase_before = partial_density_dense(output0, dims, 3)
    dephase_after = partial_density_dense(recovered0, dims, 3)
    environment_before = partial_density_dense(output0, dims, 1)
    environment_after = partial_density_dense(recovered0, dims, 1)
    system_after = partial_density_dense(recovered0, dims, 0)
    system_target = np.outer(c580.W3 @ coefficient0, (c580.W3 @ coefficient0).conj())

    # Copy pointer and dephasing words to six archive M2, then uncompute the
    # original 18 M2.  Which-history information blocks exact active reset.
    copied_pointer = append_blank_qubits(compiled, 6)
    for control, target in ((12, 18), (13, 19), (14, 20), (15, 21), (16, 22), (17, 23)):
        copied_pointer = sparse_gate(copied_pointer, c580.CNOT, (control, target), 24)
    archive_before_inverse = reduced_density_dict(copied_pointer, coefficient0, tuple(range(18, 24)), 24)
    pointer_uncomputed = sparse_inverse_cycle580(copied_pointer, 24)
    archive_after_inverse = reduced_density_dict(pointer_uncomputed, coefficient0, tuple(range(18, 24)), 24)
    active_reset_fidelity_with_pointer_copy = active_pure_fidelity(
        pointer_uncomputed, coefficient0, 18, initial @ coefficient0, 24
    )

    # Copy the three logical old-input environment rails.  Computational
    # basis inputs can be copied, but a coherent 000+111 fixture loses restored
    # system coherence after the inverse.
    copied_old = append_blank_qubits(compiled, 3)
    for control, target in ((6, 18), (8, 19), (10, 20)):
        copied_old = sparse_gate(copied_old, c580.CNOT, (control, target), 21)
    old_uncomputed = sparse_inverse_cycle580(copied_old, 21)
    coherent = (c580.c577.ket(0, 8) + c580.c577.ket(7, 8)) / np.sqrt(2.0)
    restored_system_dict = reduced_density_dict(old_uncomputed, coherent, tuple(range(6)), 21)
    restored_system = density_dict_to_dense(restored_system_dict, 64)
    coherent_encoded = c580.W3 @ coherent
    coherent_target = np.outer(coherent_encoded, coherent_encoded.conj())
    old_copy_restored_system_trace_distance = trace_distance(restored_system, coherent_target)

    # Contract-scoped archive dimension: preserve an arbitrary old logical
    # input (dimension 8) and one independently readable supported pointer
    # label (four sectors) while resetting the carrier block to one fixed
    # blank.  This is a rank statement for this exact branch-conditioned
    # contract, not a minimum-content theorem for recurrence in general.
    supported = tuple(
        history for history in c580.c577.HISTORIES
        if np.vdot(c580.c577.BRANCH_VECTOR[history], c580.c577.BRANCH_VECTOR[history]).real > TOL
    )
    normalized_branches = tuple(
        c580.W3 @ c580.c577.BRANCH_VECTOR[history]
        / np.linalg.norm(c580.c577.BRANCH_VECTOR[history])
        for history in supported
    )
    branch_gram = np.asarray([
        [np.vdot(left, right) for right in normalized_branches]
        for left in normalized_branches
    ])
    contract_columns = []
    for logical_input, history in product(range(8), supported):
        contract_columns.append(np.kron(
            np.kron(normalized_branches[supported.index(history)], c580.W3 @ c580.c577.ket(logical_input, 8)),
            c580.c577.ket(c580.c577.history_index(history), 8),
        ))
    contract_matrix = np.column_stack(contract_columns)
    contract_rank = int(np.linalg.matrix_rank(contract_matrix, tol=TOL))
    contract_archive_qubits = int((contract_rank - 1).bit_length())

    result = {
        "route": "C reversible uncompute/reset attempts",
        "full_inverse_initial_residual": float(np.linalg.norm(recovered - initial)),
        "full_inverse_pointer_output_erasure_trace_distance": trace_distance(pointer_before, pointer_after),
        "full_inverse_dephasing_output_erasure_trace_distance": trace_distance(dephase_before, dephase_after),
        "full_inverse_old_input_environment_erasure_trace_distance": trace_distance(environment_before, environment_after),
        "full_inverse_restored_system_trace_distance": trace_distance(system_after, system_target),
        "pointer_dephase_archive_invariance_through_inverse": density_dict_distance(archive_before_inverse, archive_after_inverse),
        "active_18M2_reset_fidelity_after_pointer_dephase_copy": active_reset_fidelity_with_pointer_copy,
        "active_18M2_reset_infidelity_after_pointer_dephase_copy": 1.0 - active_reset_fidelity_with_pointer_copy,
        "old_input_copy_coherent_restored_system_trace_distance": old_copy_restored_system_trace_distance,
        "supported_pointer_labels": len(supported),
        "normalized_supported_active_branch_Gram_residual": float(np.linalg.norm(branch_gram - np.eye(len(supported)))),
        "old_input_dimension": 8,
        "branch_conditioned_reset_contract_rank": contract_rank,
        "branch_conditioned_reset_contract_archive_qubits_at_least": contract_archive_qubits,
        "dimension_bound_is_contract_scoped_not_general_recurrence_minimum": True,
        "full_inverse_reuses_carriers_only_by_erasing_episode": True,
        "copy_then_uncompute_exact_active_reset_achieved": False,
        "universal_archive_preserving_reset_no_go_claimed": False,
        "pass": np.linalg.norm(recovered - initial) < TOL
        and trace_distance(pointer_before, pointer_after) > TOL
        and trace_distance(dephase_before, dephase_after) > TOL
        and trace_distance(environment_before, environment_after) > TOL
        and trace_distance(system_after, system_target) < TOL
        and density_dict_distance(archive_before_inverse, archive_after_inverse) < TOL
        and 1.0 - active_reset_fidelity_with_pointer_copy > TOL
        and old_copy_restored_system_trace_distance > TOL
        and len(supported) == 4 and np.linalg.norm(branch_gram - np.eye(4)) < TOL
        and contract_rank == 32 and contract_archive_qubits == 5,
    }
    check("Route C exact tests expose the output-erasure versus reusable-carrier tradeoff without promoting it to a universal no-go", result["pass"], result)
    return result


def matter_geometry_controls(final_held: Sparse) -> dict[str, object]:
    horizon = 3
    count = state_count(horizon)
    gram = sparse_gram(final_held)
    coefficient0 = c580.c577.ket(0, 8)
    coefficient7 = c580.c577.ket(7, 8)
    active0 = density_dict_to_dense(reduced_density_dict(final_held, coefficient0, tuple(range(6)), count), 64)
    active7 = density_dict_to_dense(reduced_density_dict(final_held, coefficient7, tuple(range(6)), count), 64)
    archive0 = density_dict_to_dense(reduced_density_dict(final_held, coefficient0, slot_environment_qubits(0), count), 64)
    archive7 = density_dict_to_dense(reduced_density_dict(final_held, coefficient7, slot_environment_qubits(0), count), 64)
    frames = c580.c577.c41.proper_cubic_rotations()
    layout_points = tuple(np.asarray(c580.LAYOUT[name], dtype=int) for name in c580.QUBIT_NAMES)
    frame_layout_failures = 0
    for frame in frames:
        transformed = tuple(tuple(int(value) for value in frame @ point) for point in layout_points)
        frame_layout_failures += int(len(set(transformed)) != len(layout_points))
    result = {
        "global_input_0_7_overlap_after_held_horizon": complex(gram[0, 7]).real,
        "global_input_0_7_trace_distance": float(np.sqrt(max(0.0, 1.0 - abs(gram[0, 7]) ** 2))),
        "active_reduced_input_0_7_trace_distance": trace_distance(active0, active7),
        "slot0_old_input_environment_0_7_trace_distance": trace_distance(archive0, archive7),
        "matter_distinction_retained_globally": True,
        "matter_distinction_retained_in_active_reduced_system": False,
        "base_Cycle580_proper_frames": len(frames),
        "base_layout_all24_collision_failures": frame_layout_failures,
        "Cycle580_all24_edge_tests_from_receipt": 816,
        "Cycle580_all576_projector_role_tests_from_receipt": 6336,
        "controller_and_conveyor_literal_cubic_layout_constructed": False,
        "pass": abs(gram[0, 7]) < TOL
        and abs(trace_distance(active0, active7)) < TOL
        and abs(trace_distance(archive0, archive7) - 1.0) < TOL
        and len(frames) == 24 and not frame_layout_failures,
    }
    check("repeated invocation preserves input distinction globally and in the first spent environment while retaining the all24 base geometry", result["pass"], result)
    return result


def no_go_and_inventory_controls() -> dict[str, object]:
    routes = (
        {
            "family": "in-state phase plus cursor",
            "object_formulation": "finite-horizon sparse isometry with unary H11 program and H_H resource cursor",
            "mechanism_invariant": "one homogeneous phase-conditioned update, reversible clock/cursor permutation, disjoint spent slots",
            "terminal_obligation": "compile the controlled update and conveyor into a literal collision-safe cubic NN law with local controller enforcement",
            "status": "ATTEMPTED",
            "evidence": "Route A exact at code-coordinate finite horizon; physical controller routing/enforcement remains open",
            "citation": "Cycle582 runner:route_a_controls",
        },
        {
            "family": "finite conveyor and debit",
            "object_formulation": "H supplied 12-M2 resource packets with spent-history ownership",
            "mechanism_invariant": "packet permutation, exact debit, archive spectator invariance",
            "terminal_obligation": "derive stationary fresh/spent balance rather than modulo reuse of spent stock",
            "status": "ATTEMPTED",
            "evidence": "Route B passes held H3 and detects first overrun; finite stock is exhausted",
            "citation": "Cycle582 runner:route_b_controls",
        },
        {
            "family": "reversible uncompute/reset",
            "object_formulation": "Cycle580 inverse with zero, pointer-copy, and old-input-copy archives",
            "mechanism_invariant": "global unitarity, which-history retention, active reset fidelity",
            "terminal_obligation": "reset carriers while retaining an independent faithful quantum output/history owner",
            "status": "ATTEMPTED",
            "evidence": "Route C exact tested attempts expose erasure or reset/coherence residuals",
            "citation": "Cycle582 runner:route_c_controls",
        },
        {
            "family": "bi-infinite fresh/spent streaming QCA",
            "object_formulation": "translation-invariant reservoir and garbage rays",
            "mechanism_invariant": "ballistic carrier flow and local scattering",
            "terminal_obligation": "prove stationary low-entropy inflow, collision safety, and arbitrary-volume recurrence",
            "status": "UNTESTED_OPEN_NOT_COUNTED",
            "evidence": "concrete reopen route; no Cycle582 construction or retained ruling-out authority",
            "citation": "Cycle483 and Cycle580 optimal-next-campaign receipts",
        },
        {
            "family": "error-corrected catalytic workspace",
            "object_formulation": "encoded catalyst plus syndrome/garbage export",
            "mechanism_invariant": "coherent correction and catalytic return",
            "terminal_obligation": "return the catalyst exactly while binding all exported syndrome/history information",
            "status": "UNTESTED_OPEN_NOT_COUNTED",
            "evidence": "mathematically actionable route not attempted here",
            "citation": "Cycle582 N7 steelman",
        },
    )
    walls = (
        "literal local controller/conveyor compilation",
        "stationary fresh/spent resource balance",
        "archive-preserving exact carrier reset",
        "controller/code enforcement and noise tolerance",
    )
    pair_reasons = (
        (0, 1, "a local controller can still consume finite stock", "stationary carrier balance supplies no local program routing"),
        (0, 2, "local scheduling does not make inverse reset preserve archives", "archive-preserving reset does not place or clock gates"),
        (0, 3, "a compiled controller can lack enforcement/noise repair", "enforcement does not compile the recurrence geometry"),
        (1, 2, "renewal can export rather than reset spent carriers", "reset of one carrier does not prove stationary supply balance"),
        (1, 3, "stationary flow can carry uncorrected controller faults", "error correction does not generate low-entropy inflow"),
        (2, 3, "archive-preserving reset can be noise-fragile", "enforcement does not solve quantum output retention during reset"),
    )
    pair_table = tuple({
        "pair": (walls[left], walls[right]), "left_closes_right": "no",
        "left_to_right_reason": left_reason, "right_closes_left": "no",
        "right_to_left_reason": right_reason, "independent": True,
    } for left, right, left_reason, right_reason in pair_reasons)
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
    residual_table = (
        {"witness": "Cycle580 receipt", "witness_residual": "compile-time order; no in-state program or recurrence", "claimed_closed": "finite-horizon in-state code-coordinate scheduling", "match": "yes"},
        {"witness": "Cycle483 note", "witness_residual": "finite bath/export is not renewal", "claimed_closed": "finite debit only, not renewal", "match": "yes"},
        {"witness": "Cycle577 note", "witness_residual": "inverse erases the output episode", "claimed_closed": "three explicit uncompute/reset attempts", "match": "yes"},
        {"witness": "Cycle580 layout", "witness_residual": "single-invocation NN gates", "claimed_closed": "autonomous controller NN layout", "match": "no — base geometry only; dropped as controller-layout closure"},
    )
    partial_paths = (
        "spatial program-token QCA compiling phase controls into two-M2 NN scatterings",
        "bi-infinite or stationary fresh/spent carrier flow with explicit boundary state",
        "coherent error-corrected catalyst with syndrome/history export",
        "bounded archive teleport/swap followed by independently proved carrier re-preparation",
    )
    steelman = {
        "mechanism": "a translation-invariant reversible QCA streams a bi-infinite encoded-plus/zero reservoir through one local Cycle580 scattering station, carries spent packets outward, and transports a spatial program token whose collisions implement each elementary gate",
        "terminal_obligation": "construct the bounded-neighborhood update, prove stationary fresh/spent balance and collision safety at arbitrary volume, and preserve a faithful independent output algebra",
        "disposition": "concrete untested route; any broad recurrence/reset no-go is premature",
    }
    echo = (
        "Cycle574 representation gap retired by faithful W encoding",
        "Cycle577 isometry-only gap retired by Cycle580 elementary circuit",
        "Cycle483 hidden discard retired at finite export but not renewal",
        "Cycle580 host-order gap narrowed here to controller locality/enforcement",
    )
    qualifying = tuple(route for route in routes if route["status"] in ("ATTEMPTED", "RULED OUT BY PRIOR"))
    supplied = (
        "Cycle580 exact 18-M2 elementary circuit and base cubic layout",
        "finite H resource packets, pure encoded-plus/zero preparation, unary phase/cursor code domains",
        "same autonomous update invocation count, modulo cursor convention, noiseless controlled gates, and held boundaries",
        "candidate traces, conditional pointer typing, site-only proper-cubic presentation, and global trace functional",
    )
    derived = (
        "exact H1 Cycle580 equality and H2/H3 repeated finite-horizon code-coordinate recurrence",
        "exact archive invariance, inverse step, debit ledger, overrun detection, and global input-distinction retention",
        "exact full-inverse output erasure plus pointer/dephase-copy and old-input-copy reset residuals",
        "active deletions, coherent gate-noise response, malformed-controller refusal, and base all24 geometry",
    )
    open_items = (
        "literal proper-cubic NN decomposition of phase/cursor controls and conveyor routing",
        "local controller/code enforcement, repair, noise threshold, and arbitrary-volume collision theorem",
        "stationary fresh/spent balance, carrier genesis, renewal, entropy sink, temperature, and unbounded horizon",
        "archive-preserving exact quantum carrier reset beyond the attempted copy schemes",
        "actual branch, framework Record, Born/frequency calibration, physical time, energy, source, gravity, and matter-compatible active nonerasure",
    )
    result = {
        "N1_routes": routes, "N1_qualifying": len(qualifying), "N1_required": 5,
        "N1_status": "FAIL", "N2_walls": walls, "N2_pairwise": pair_table,
        "N3_hidden_hits": hidden_hits, "N4_residual_table": residual_table,
        "N5": "negative observations are limited to the tested finite horizons and three explicit Route-C maps",
        "N6_partial_closure_paths": partial_paths, "N7_steelman": steelman,
        "N8_cross_cycle_echo": echo,
        "artifact_status": "POSITIVE_FINITE_HORIZON_PARTIAL_CONSTRUCTION_WITH_ROUTE_SPECIFIC_FALSIFIERS",
        "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP",
        "shared_obstruction": "DO_NOT_SHIP", "axiom_pressure": "DO_NOT_SHIP",
        "inventory": {"supplied": supplied, "derived": derived, "open": open_items},
        "pass": len(routes) == 5 and len(qualifying) == 3 and len(pair_table) == 6
        and all(row["independent"] for row in pair_table)
        and all(hit["classification"] for hit in hidden_hits)
        and sum(row["match"] == "yes" for row in residual_table) == 3
        and len(partial_paths) == 4 and all(steelman.values()) and len(echo) == 4,
    }
    check("N1-N8 fails broad negatives honestly and retains a positive finite-horizon construction with route-specific falsifiers", result["pass"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_result: str = "exact H2/H3 in-state-controlled finite-stock recurrence of Cycle580 V_B at code-coordinate resolution"
    actual_branch: None = None
    framework_Record: None = None
    derived_Born_probability: None = None
    physical_time: None = None
    energy_or_source: None = None
    renewable_resource_law: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle582 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        dependency = dependency_controls()
        _train_controller, route_a = route_a_controls()
        held_final, route_b = route_b_controls()
        route_c = route_c_controls()
        matter_geometry = matter_geometry_controls(held_final)
        discipline_inventory = no_go_and_inventory_controls()
        resources = {
            "elapsed_seconds": time.perf_counter() - started, "rss_bytes": rss_bytes(),
            "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES,
        }
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["rss_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({
            "dependency": dependency, "route_A": route_a, "route_B": route_b,
            "route_C": route_c, "matter_geometry": matter_geometry,
            "discipline_inventory": discipline_inventory, "resources": resources,
            "summary": Summary().__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; finite stock is not renewable; copied pointer is not Record; candidate trace is not Born; phase is not time; carrier count is not energy/source")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
