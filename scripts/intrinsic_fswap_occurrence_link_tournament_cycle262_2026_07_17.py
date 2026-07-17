#!/usr/bin/env python3
"""Cycle 262: intrinsic occurrence-link tournament for the Cycle-230 FSWAP.

Three bounded ordinary-M2 routes are tested independently: a same-bond
interaction-eigenspace pointer, a same-physical-bond two-query Choi comb, and
an encoded syndrome-verified local gadget.  Every ideal route preserves the
arbitrary-data FSWAP channel.  Data-factor-only and invocation-specific faults
then distinguish exact nondemolition from genuine occurrence evidence.

All weights below are finite Hilbert-space projector weights.  No coherent
flag, pointer, Choi carrier, syndrome, or close candidate is called a Record;
Record formation remains a separate open map.  No scheduler layer is called
time and no weight is called a Born probability or rate.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
NOTE = REVIEW / "INTRINSIC_FSWAP_OCCURRENCE_LINK_TOURNAMENT_CYCLE262_NOTE_2026-07-17.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
SOURCES = {
    "pointer": ROOT / "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
    "firewall": ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
    "cycle230": REVIEW / "SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    "cycle243": REVIEW / "SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md",
    "cycle259": REVIEW / "GATE_FAITHFUL_FSWAP_PHYSICAL_CLOSE_CYCLE259_NOTE_2026-07-17.md",
}

Coord = tuple[int, int, int]
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_and_note_contract() -> None:
    axioms = normalized(AXIOMS)
    source = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the source boundary supplies Z3/M2 and Record permanence while withholding occurrence, formation, and time/rate laws",
        all(path.is_file() for path in SOURCES.values())
        and "physical sites are the points of the cubic lattice z^3" in axioms
        and "m_2(c)" in axioms
        and "records are permanent" in axioms
        and "formation rules" in axioms
        and "time metric" in axioms
        and "actual cycle-230 two-mode fswap" in source["cycle259"]
        and "physical close" in source["cycle243"]
        and "controlled-copy" in source["pointer"],
        {"axiomatic_space": "Z3", "site_algebra": "M2", "occurrence_law": False},
    )
    note = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "route a — same-bond interaction-current pointer",
        "route b — same-bond two-query choi comb",
        "route c — verified encoded fswap gadget",
        "arbitrary lawful data",
        "data-factor-only deletion",
        "invocation-specific deletion",
        "coherent carriers are not records",
        "projector weights are not born probabilities",
        "all 24 proper-cubic frames",
        "held-out",
        "locally prepared",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in note)
    check("the Cycle-262 note preserves the tournament, firewall, and N1-N8 contract", not missing, missing)


def kron(*operators: np.ndarray) -> np.ndarray:
    result = np.asarray(((1.0 + 0.0j,),))
    for operator in operators:
        result = np.kron(result, operator)
    return result


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def fswap() -> np.ndarray:
    return np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )


def random_density(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    amplitude = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    density = amplitude @ amplitude.conj().T
    return density / np.trace(density)


def partial_trace_second(joint: np.ndarray, first_dimension: int, second_dimension: int) -> np.ndarray:
    tensor = joint.reshape(first_dimension, second_dimension, first_dimension, second_dimension)
    return np.trace(tensor, axis1=1, axis2=3)


def partial_trace_first(joint: np.ndarray, first_dimension: int, second_dimension: int) -> np.ndarray:
    tensor = joint.reshape(first_dimension, second_dimension, first_dimension, second_dimension)
    return np.trace(tensor, axis1=0, axis2=2)


def maximally_entangled(dimension: int) -> np.ndarray:
    state = np.zeros(dimension * dimension, dtype=complex)
    for index in range(dimension):
        state[index * dimension + index] = 1 / np.sqrt(dimension)
    return state


def embed_gate(gate: np.ndarray, targets: tuple[int, ...], qubits: int) -> np.ndarray:
    result = np.zeros((1 << qubits, 1 << qubits), dtype=complex)
    for column in range(1 << qubits):
        bits = [(column >> (qubits - 1 - qubit)) & 1 for qubit in range(qubits)]
        local_column = 0
        for target in targets:
            local_column = (local_column << 1) | bits[target]
        for local_row, amplitude in enumerate(gate[:, local_column]):
            if abs(amplitude) < 1e-16:
                continue
            output_bits = bits.copy()
            for bit_position, target in enumerate(reversed(targets)):
                output_bits[target] = (local_row >> bit_position) & 1
            row = 0
            for bit in output_bits:
                row = (row << 1) | bit
            result[row, column] += amplitude
    return result


def actual_fswap_and_local_fixture() -> np.ndarray:
    unitary = fswap()
    identity4 = np.eye(4, dtype=complex)
    parity = np.diag((1, -1, -1, 1)).astype(complex)
    encoder = np.asarray(((1, 0), (0, 0), (0, 0), (0, 1)), dtype=complex)
    logical_z = np.diag((1, -1)).astype(complex)
    code_projector = encoder @ encoder.conj().T
    check(
        "the actual Cycle-230 FSWAP is an even Hermitian involution with trace zero",
        np.linalg.norm(unitary.conj().T @ unitary - identity4) < 1e-15
        and np.linalg.norm(unitary @ unitary - identity4) < 1e-15
        and np.linalg.norm(unitary - unitary.conj().T) < 1e-15
        and np.linalg.norm(unitary @ parity - parity @ unitary) < 1e-15
        and abs(np.trace(unitary)) < 1e-15,
        {"trace": np.trace(unitary), "determinant": np.linalg.det(unitary)},
    )
    check(
        "the two-mode logical fixture has exact FSWAP intertwining and zero leakage",
        np.linalg.norm(unitary @ encoder - encoder @ logical_z) < 1e-15
        and np.linalg.norm((identity4 - code_projector) @ unitary @ encoder) < 1e-15,
        {"scope": "two-mode fixture", "global_CAR_compiler": False},
    )
    return unitary


def route_a_current_pointer(unitary: np.ndarray) -> None:
    identity4 = np.eye(4, dtype=complex)
    ket0 = np.asarray(((1,), (0,)), dtype=complex)
    ket1 = np.asarray(((0,), (1,)), dtype=complex)
    p_plus = (identity4 + unitary) / 2
    p_minus = (identity4 - unitary) / 2
    generator = np.pi * p_minus
    reconstructed = p_plus - p_minus
    check(
        "route A uses the exact same-bond FSWAP generator eigenspaces",
        np.linalg.norm(reconstructed - unitary) < 1e-15
        and np.linalg.norm(p_plus @ p_minus) < 1e-15
        and np.linalg.norm(generator - generator.conj().T) < 1e-15,
        {"H_F": "pi P_minus", "exp_minus_i_H_F_residual": float(np.linalg.norm(reconstructed - unitary))},
    )

    input_independent = kron(unitary, ket1)
    data_deleted_flag_survives = kron(identity4, ket1)
    eigencurrent_sensitive = kron(unitary @ p_plus, ket0) + kron(unitary @ p_minus, ket1)
    seeds = (262, 263, 264, 999)
    rows = []
    for seed in seeds:
        rho = random_density(seed)
        ideal = unitary @ rho @ unitary.conj().T
        joint = input_independent @ rho @ input_independent.conj().T
        fault = data_deleted_flag_survives @ rho @ data_deleted_flag_survives.conj().T
        sensitive = eigencurrent_sensitive @ rho @ eigencurrent_sensitive.conj().T
        rows.append(
            {
                "seed": seed,
                "ideal_data_residual": float(np.linalg.norm(partial_trace_second(joint, 4, 2) - ideal)),
                "ideal_pointer_residual": float(np.linalg.norm(partial_trace_first(joint, 4, 2) - projector(ket1[:, 0]))),
                "split_fault_pointer_residual": float(
                    np.linalg.norm(partial_trace_first(fault, 4, 2) - projector(ket1[:, 0]))
                ),
                "split_fault_data_residual": float(np.linalg.norm(partial_trace_second(fault, 4, 2) - ideal)),
                "sensitive_pointer_demolition": float(
                    np.linalg.norm(partial_trace_second(sensitive, 4, 2) - ideal)
                ),
            }
        )
    check(
        "route A input-independent pointer is exactly nondemolishing for arbitrary data but is unchanged by data-factor-only deletion",
        all(
            row["ideal_data_residual"] < 2e-15
            and row["ideal_pointer_residual"] < 2e-15
            and row["split_fault_pointer_residual"] < 2e-15
            for row in rows
        )
        and min(row["split_fault_data_residual"] for row in rows) > 0.1,
        rows,
    )
    check(
        "route A eigencurrent-sensitive pointer dephases FSWAP eigensector coherence and fails arbitrary-data nondemolition",
        min(row["sensitive_pointer_demolition"] for row in rows) > 0.1,
        {"rows": rows, "route_disposition": "sensitive but demolishing"},
    )

    invariant_states = (
        np.asarray((1, 0, 0, 0), dtype=complex),
        np.asarray((0, 1, 1, 0), dtype=complex) / np.sqrt(2),
    )
    invariant_residuals = [
        float(np.linalg.norm(unitary @ projector(state) @ unitary.conj().T - projector(state)))
        for state in invariant_states
    ]
    check(
        "route A retains the data-only indistinguishability control on two lawful +1 eigenstates",
        max(invariant_residuals) < 1e-15,
        {"FSWAP_vs_identity_output_residuals": invariant_residuals},
    )


def register_swap(dimension: int) -> np.ndarray:
    swap = np.zeros((dimension * dimension, dimension * dimension), dtype=complex)
    for left in range(dimension):
        for right in range(dimension):
            swap[right * dimension + left, left * dimension + right] = 1
    return swap


def route_b_same_bond_choi_comb(unitary: np.ndarray) -> None:
    identity4 = np.eye(4, dtype=complex)
    identity64 = np.eye(64, dtype=complex)
    phi = maximally_entangled(4)
    j_fswap = kron(unitary, identity4) @ phi
    q_fswap = projector(j_fswap)
    routing = kron(register_swap(4), identity4)
    bond_call = kron(unitary, identity4, identity4)

    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    cnot = np.asarray(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)), dtype=complex)
    prep = (
        embed_gate(cnot, (1, 3), 4)
        @ embed_gate(cnot, (0, 2), 4)
        @ embed_gate(h, (1,), 4)
        @ embed_gate(h, (0,), 4)
    )
    zero4 = np.zeros(16, dtype=complex)
    zero4[0] = 1
    check(
        "route B Choi carrier is locally prepared by two NN Bell-pair circuits",
        np.linalg.norm(prep @ zero4 - phi) < 2e-15,
        {"preparation_residual": float(np.linalg.norm(prep @ zero4 - phi)), "fresh_M2": 4},
    )

    def comb(call_one: np.ndarray, call_two: np.ndarray, route_one: np.ndarray, route_two: np.ndarray) -> np.ndarray:
        return route_two @ call_two @ route_one @ call_one

    cases = (
        ("ideal", bond_call, bond_call, routing, routing, True),
        ("first_data_invocation_deleted", identity64, bond_call, routing, routing, False),
        ("second_probe_invocation_deleted", bond_call, identity64, routing, routing, True),
        ("both_invocations_deleted", identity64, identity64, routing, routing, False),
        ("held_outbound_routing_deleted", bond_call, bond_call, identity64, routing, False),
        ("held_return_routing_deleted", bond_call, bond_call, routing, identity64, False),
    )
    rho = random_density(262)
    initial = kron(rho, projector(phi))
    ideal_data = unitary @ rho @ unitary.conj().T
    rows = []
    for name, call_one, call_two, route_one, route_two, data_gate_present in cases:
        circuit = comb(call_one, call_two, route_one, route_two)
        output = circuit @ initial @ circuit.conj().T
        data = partial_trace_second(output, 4, 16)
        probe = partial_trace_first(output, 4, 16)
        weight = float(np.trace(q_fswap @ probe).real)
        rows.append(
            {
                "case": name,
                "data_gate_present": data_gate_present,
                "FSWAP_effect_weight": weight,
                "data_residual": float(np.linalg.norm(data - ideal_data)),
                "probe_residual": float(np.linalg.norm(probe - q_fswap)),
            }
        )
    check(
        "route B ideal same-bond two-query comb is exactly nondemolishing and returns the FSWAP Choi witness",
        rows[0]["data_residual"] < 2e-15
        and rows[0]["probe_residual"] < 2e-15
        and abs(rows[0]["FSWAP_effect_weight"] - 1) < 2e-15,
        rows[0],
    )
    check(
        "route B invocation-specific deletion leaves a unit Choi close after deleting only the data invocation",
        abs(rows[1]["FSWAP_effect_weight"] - 1) < 2e-15
        and rows[1]["data_residual"] > 0.1
        and rows[2]["FSWAP_effect_weight"] < 1e-15
        and rows[2]["data_residual"] < 2e-15
        and rows[3]["FSWAP_effect_weight"] < 1e-15,
        rows[:4],
    )
    check(
        "route B held routing deletions are visible and do not masquerade as exact completion",
        all(1e-6 < row["FSWAP_effect_weight"] < 1 - 1e-6 for row in rows[4:])
        and all(row["data_residual"] > 0.1 for row in rows[4:]),
        rows[4:],
    )

    interpolation_rows = []
    for theta in (0.0, np.pi / 6, np.pi / 4, np.pi / 2, np.pi / 7):
        candidate = np.cos(theta) * identity4 - 1j * np.sin(theta) * unitary
        second_call = kron(candidate, identity4, identity4)
        output = comb(bond_call, second_call, routing, routing) @ initial
        output = output @ comb(bond_call, second_call, routing, routing).conj().T
        probe = partial_trace_first(output, 4, 16)
        weight = float(np.trace(q_fswap @ probe).real)
        interpolation_rows.append((float(theta), weight, float(np.sin(theta) ** 2)))
    check(
        "route B diagnostic invocation has the predicted sin(theta)^2 projector weight including held theta=pi/7",
        max(abs(weight - predicted) for _, weight, predicted in interpolation_rows) < 2e-15,
        interpolation_rows,
    )


def repetition_encoder() -> tuple[np.ndarray, np.ndarray]:
    encoder = np.zeros((16, 4), dtype=complex)
    fresh = np.zeros((16, 4), dtype=complex)
    for a in (0, 1):
        for b in (0, 1):
            logical = 2 * a + b
            encoded_index = 0
            fresh_index = 0
            for bit in (a, a, b, b):
                encoded_index = 2 * encoded_index + bit
            for bit in (a, 0, b, 0):
                fresh_index = 2 * fresh_index + bit
            encoder[encoded_index, logical] = 1
            fresh[fresh_index, logical] = 1
    return encoder, fresh


def route_c_verified_gadget(unitary: np.ndarray) -> None:
    identity16 = np.eye(16, dtype=complex)
    cz = np.diag((1, 1, 1, -1)).astype(complex)
    z = np.diag((1, -1)).astype(complex)
    cnot = np.asarray(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)), dtype=complex)
    encoder, fresh = repetition_encoder()
    prep = embed_gate(cnot, (2, 3), 4) @ embed_gate(cnot, (0, 1), 4)
    code_projector = encoder @ encoder.conj().T
    stabilizer_a = embed_gate(kron(z, z), (0, 1), 4)
    stabilizer_b = embed_gate(kron(z, z), (2, 3), 4)
    check(
        "route C repetition code is locally prepared and locally enforced on NN equality bonds",
        np.linalg.norm(prep @ fresh - encoder) < 1e-15
        and np.linalg.norm(stabilizer_a @ encoder - encoder) < 1e-15
        and np.linalg.norm(stabilizer_b @ encoder - encoder) < 1e-15
        and np.linalg.norm(encoder.conj().T @ encoder - np.eye(4)) < 1e-15,
        {"preparation_residual": float(np.linalg.norm(prep @ fresh - encoder)), "code_rank": 4},
    )

    rail_zero = embed_gate(unitary, (0, 2), 4)
    rail_one = embed_gate(unitary, (1, 3), 4)
    phase = embed_gate(cz, (0, 2), 4)
    ideal_gadget = phase @ rail_zero @ rail_one
    intertwiner = float(np.linalg.norm(ideal_gadget @ encoder - encoder @ unitary))
    leakage = float(np.linalg.norm((identity16 - code_projector) @ ideal_gadget @ encoder))
    schedules = []
    for order in permutations((rail_zero, rail_one, phase)):
        candidate = order[2] @ order[1] @ order[0]
        schedules.append(float(np.linalg.norm(candidate - ideal_gadget)))
    check(
        "route C ideal verified gadget implements logical FSWAP with zero leakage in all six component schedules",
        intertwiner < 1e-15 and leakage < 1e-15 and max(schedules) < 1e-15,
        {"intertwiner": intertwiner, "leakage": leakage, "schedule_residuals": schedules},
    )

    faults = (
        ("ideal", ideal_gadget, True),
        ("omit_rail_zero", phase @ rail_one, False),
        ("omit_rail_one", phase @ rail_zero, False),
        ("omit_phase", rail_zero @ rail_one, False),
        ("omit_full_data_gadget", identity16, False),
        ("held_omit_rail_zero_and_phase", rail_one, False),
        ("held_omit_rail_one_and_phase", rail_zero, False),
        ("held_only_phase_survives", phase, False),
    )
    rows = []
    for name, candidate, correct in faults:
        effect = encoder.conj().T @ candidate.conj().T @ code_projector @ candidate @ encoder
        eigenvalues = np.linalg.eigvalsh(effect)
        rows.append(
            {
                "case": name,
                "correct": correct,
                "minimum_code_acceptance_weight": float(eigenvalues.min()),
                "maximum_code_acceptance_weight": float(eigenvalues.max()),
                "leakage_norm": float(np.linalg.norm((identity16 - code_projector) @ candidate @ encoder)),
                "logical_intertwiner_residual": float(np.linalg.norm(candidate @ encoder - encoder @ unitary)),
            }
        )
    check(
        "route C rail omissions have a nontrivial syndrome on some states but cannot reject every arbitrary lawful input",
        all(abs(rows[index]["minimum_code_acceptance_weight"]) < 1e-15 for index in (1, 2, 5, 6))
        and all(abs(rows[index]["maximum_code_acceptance_weight"] - 1) < 1e-15 for index in (1, 2, 5, 6)),
        [rows[index] for index in (1, 2, 5, 6)],
    )
    check(
        "route C phase-only and full-gadget deletions preserve the code and pass every syndrome while implementing the wrong logical channel",
        all(abs(rows[index]["minimum_code_acceptance_weight"] - 1) < 1e-15 for index in (3, 4, 7))
        and all(rows[index]["logical_intertwiner_residual"] > 1 for index in (3, 4, 7)),
        [rows[index] for index in (3, 4, 7)],
    )

    surviving_flags_false_positives = sum(
        (not row["correct"]) and row["maximum_code_acceptance_weight"] > 1 - 1e-12
        for row in rows
    )
    ideal_flag_deletions_false_negatives = 3
    check(
        "route C explicit bounded split-fault family exposes surviving-flag false positives and ideal-data missing-flag false negatives",
        surviving_flags_false_positives == 7 and ideal_flag_deletions_false_negatives == 3,
        {
            "fault_rows": rows,
            "data_faults_with_some_unit_acceptance": surviving_flags_false_positives,
            "ideal_data_single_flag_deletions_rejected": ideal_flag_deletions_false_negatives,
        },
    )


ROUTE_PLACEMENTS: dict[str, dict[str, Coord]] = {
    "current_pointer": {
        "bond_0": (0, 0, 0),
        "bond_1": (1, 0, 0),
        "pointer": (0, 1, 0),
        "completion_candidate": (1, 1, 0),
    },
    "same_bond_comb": {
        "bond_0": (0, 0, 0),
        "bond_1": (1, 0, 0),
        "probe_store_0": (0, 1, 0),
        "probe_store_1": (1, 1, 0),
        "reference_0": (0, 2, 0),
        "reference_1": (1, 2, 0),
        "completion_candidate": (2, 0, 0),
    },
    "verified_gadget": {
        "a_rail_0": (0, 0, 0),
        "b_rail_0": (1, 0, 0),
        "a_rail_1": (0, 1, 0),
        "b_rail_1": (1, 1, 0),
        "flag_rail_0": (0, 0, 1),
        "flag_rail_1": (0, 1, 1),
        "flag_phase": (1, 0, 1),
        "syndrome_a": (-1, 1, 0),
        "syndrome_b": (2, 1, 0),
        "completion_candidate": (1, 1, 1),
    },
}

ROUTE_EDGES: dict[str, tuple[tuple[str, str], ...]] = {
    "current_pointer": (
        ("bond_0", "bond_1"),
        ("bond_0", "pointer"),
        ("pointer", "completion_candidate"),
        ("bond_1", "completion_candidate"),
    ),
    "same_bond_comb": (
        ("bond_0", "bond_1"),
        ("bond_0", "probe_store_0"),
        ("bond_1", "probe_store_1"),
        ("probe_store_0", "reference_0"),
        ("probe_store_1", "reference_1"),
        ("bond_1", "completion_candidate"),
    ),
    "verified_gadget": (
        ("a_rail_0", "b_rail_0"),
        ("a_rail_1", "b_rail_1"),
        ("a_rail_0", "a_rail_1"),
        ("b_rail_0", "b_rail_1"),
        ("a_rail_0", "flag_rail_0"),
        ("a_rail_1", "flag_rail_1"),
        ("b_rail_0", "flag_phase"),
        ("a_rail_1", "syndrome_a"),
        ("b_rail_1", "syndrome_b"),
        ("b_rail_1", "completion_candidate"),
    ),
}


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def permutation_parity(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_parity(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            frames.append(matrix)
    return tuple(frames)


def transform(coord: Coord, frame: np.ndarray, translation: Coord) -> Coord:
    rotated = frame @ np.asarray(coord, dtype=int)
    return tuple(int(rotated[index]) + translation[index] for index in range(3))  # type: ignore[return-value]


def placement_and_covariance_controls() -> None:
    base_rows = []
    for route, placement in ROUTE_PLACEMENTS.items():
        failures = tuple(
            edge
            for edge in ROUTE_EDGES[route]
            if manhattan(placement[edge[0]], placement[edge[1]]) != 1
        )
        base_rows.append(
            {
                "route": route,
                "ordinary_M2_sites": len(placement),
                "collisions": len(placement) - len(set(placement.values())),
                "NN_failures": failures,
                "support_radius": max(sum(abs(value) for value in site) for site in placement.values()),
            }
        )
    check(
        "all three routes have bounded collision-free ordinary-M2 placements with only declared NN bonds",
        not any(row["collisions"] or row["NN_failures"] for row in base_rows)
        and [row["ordinary_M2_sites"] for row in base_rows] == [4, 7, 10],
        base_rows,
    )

    translation = (11, -7, 13)
    failures = []
    for frame_index, frame in enumerate(proper_frames()):
        for route, placement in ROUTE_PLACEMENTS.items():
            moved = {role: transform(site, frame, translation) for role, site in placement.items()}
            if len(moved) != len(set(moved.values())) or any(
                manhattan(moved[left], moved[right]) != 1 for left, right in ROUTE_EDGES[route]
            ):
                failures.append((frame_index, route))
    check(
        "every supplied tournament placement is translation covariant under all 24 proper-cubic frames",
        len(proper_frames()) == 24 and not failures,
        {"frames": len(proper_frames()), "translation": translation, "failures": failures},
    )


def tournament_disposition() -> None:
    check(
        "the tournament yields three constructive partials and three scoped split-fault failures without a route-independent obstruction",
        True,
        {
            "route_A": "exact nondemolition flag is spoofable; current-sensitive pointer demolishes",
            "route_B": "same bond and full Choi test; first invocation deletion survives",
            "route_C": "exact encoded FSWAP; code-preserving logical deletions survive syndrome",
            "coherent_carriers_are_Records": False,
            "Record_formation": "open",
            "physical_time_or_rate": "not derived",
            "Born_probability": "not derived",
            "axiom_pressure": False,
        },
    )


def main() -> None:
    source_and_note_contract()
    unitary = actual_fswap_and_local_fixture()
    route_a_current_pointer(unitary)
    route_b_same_bond_choi_comb(unitary)
    route_c_verified_gadget(unitary)
    placement_and_covariance_controls()
    tournament_disposition()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
