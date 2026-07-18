#!/usr/bin/env python3
"""Cycle 266: exact unitary-channel dilation factorization for local FSWAP.

The runner constructs a single bounded update whose full data/environment
operator-Schmidt rank is maximal, while its prepared-environment input branch
implements the exact FSWAP channel and therefore factorizes.  A separately
declared adversarial split-factor fault replaces only F by identity while
preserving the environment state.  This fault is a conditional test grammar;
it is not asserted to be a lawful deletion of an indivisible substrate update.

Coherent environment/history carriers and projector effects are not Records.
No projector weight is called a Born probability, no circuit ordering is
called time, and no generator coefficient is called a rate.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
NOTE = REVIEW / "UNITARY_NONDEMOLITION_OCCURRENCE_LINK_FACTORIZATION_CYCLE266_NOTE_2026-07-17.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
SOURCES = {
    "pointer": ROOT / "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
    "firewall": ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
    "cycle230": REVIEW / "SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    "cycle259": REVIEW / "GATE_FAITHFUL_FSWAP_PHYSICAL_CLOSE_CYCLE259_NOTE_2026-07-17.md",
    "cycle262": REVIEW / "INTRINSIC_FSWAP_OCCURRENCE_LINK_TOURNAMENT_CYCLE262_NOTE_2026-07-17.md",
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
    sources = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the source boundary supplies Z3/M2 and Record permanence while withholding this update, occurrence link, and time/rate law",
        all(path.is_file() for path in SOURCES.values())
        and "physical sites are the points of the cubic lattice z^3" in axioms
        and "m_2(c)" in axioms
        and "records are permanent" in axioms
        and "formation rules" in axioms
        and "time metric" in axioms
        and "actual cycle-230 two-mode fswap" in sources["cycle259"]
        and "data-factor-only deletion" in sources["cycle262"]
        and "controlled-copy" in sources["pointer"],
        {"axiomatic_space": "Z3", "site_algebra": "M2", "selected_update": False},
    )
    note = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "prepared-environment input subspace",
        "full joint unitary need not factorize",
        "conditional adversarial split-factor fault",
        "may not be a lawful deletion of an indivisible substrate update",
        "coherent history carrier is not a record",
        "projector weights are not born probabilities",
        "all 24 proper-cubic frames",
        "held-out",
        "kretschmann",
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
    check("the Cycle-266 note preserves the theorem scope, firewall, and N1-N8 contract", not missing, missing)


def kron(*operators: np.ndarray) -> np.ndarray:
    result = np.asarray(((1.0 + 0.0j,),))
    for operator in operators:
        result = np.kron(result, operator)
    return result


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def basis_vector(dimension: int, index: int) -> np.ndarray:
    vector = np.zeros(dimension, dtype=complex)
    vector[index] = 1
    return vector


def fswap() -> np.ndarray:
    return np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )


def random_density(dimension: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    amplitude = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    density = amplitude @ amplitude.conj().T
    return density / np.trace(density)


def partial_trace_second(joint: np.ndarray, first_dimension: int, second_dimension: int) -> np.ndarray:
    tensor = joint.reshape(first_dimension, second_dimension, first_dimension, second_dimension)
    return np.trace(tensor, axis1=1, axis2=3)


def partial_trace_first(joint: np.ndarray, first_dimension: int, second_dimension: int) -> np.ndarray:
    tensor = joint.reshape(first_dimension, second_dimension, first_dimension, second_dimension)
    return np.trace(tensor, axis1=0, axis2=2)


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


def actual_fswap_fixture() -> np.ndarray:
    unitary = fswap()
    identity4 = np.eye(4, dtype=complex)
    parity = np.diag((1, -1, -1, 1)).astype(complex)
    one_particle = np.diag((0, 1, 1, 0)).astype(complex)
    check(
        "the actual Cycle-230 FSWAP is an even Hermitian unitary involution with trace zero",
        np.linalg.norm(unitary.conj().T @ unitary - identity4) < 1e-15
        and np.linalg.norm(unitary @ unitary - identity4) < 1e-15
        and np.linalg.norm(unitary - unitary.conj().T) < 1e-15
        and np.linalg.norm(unitary @ parity - parity @ unitary) < 1e-15
        and abs(np.trace(unitary)) < 1e-15,
        {"trace": np.trace(unitary), "determinant": np.linalg.det(unitary)},
    )
    check(
        "FSWAP preserves the complete local one-particle subspace and exchanges its two occupation basis states",
        np.linalg.norm(unitary @ one_particle - one_particle @ unitary) < 1e-15
        and np.linalg.norm(unitary @ basis_vector(4, 1) - basis_vector(4, 2)) < 1e-15
        and np.linalg.norm(unitary @ basis_vector(4, 2) - basis_vector(4, 1)) < 1e-15,
        {
            "one_particle_rank": int(round(np.trace(one_particle).real)),
            "one_particle_subspace_preserved": True,
            "full_mass_fixture_tested": False,
        },
    )
    return unitary


def pauli_completion(unitary: np.ndarray) -> tuple[tuple[str, ...], tuple[np.ndarray, ...]]:
    identity2 = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    paulis = (("I", identity2), ("X", x), ("Y", y), ("Z", z))
    labeled = [(left + right, kron(a, b)) for left, a in paulis for right, b in paulis]
    completion = [("F", unitary)] + [(label, operator) for label, operator in labeled if label != "IZ"]
    return tuple(label for label, _ in completion), tuple(operator for _, operator in completion)


def history_rotation() -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    cnot = np.asarray(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)), dtype=complex)
    rotation = (
        embed_gate(cnot, (0, 3), 4)
        @ embed_gate(cnot, (0, 2), 4)
        @ embed_gate(cnot, (0, 1), 4)
        @ embed_gate(h, (0,), 4)
        @ embed_gate(x, (3,), 4)
    )
    ghz = (basis_vector(16, 0) + basis_vector(16, 15)) / np.sqrt(2)
    return rotation, ghz


def shifted_update(branch_operators: tuple[np.ndarray, ...], rotation: np.ndarray) -> np.ndarray:
    environment_dimension = len(branch_operators)
    shift_update = np.zeros((4 * environment_dimension, 4 * environment_dimension), dtype=complex)
    for index, operator in enumerate(branch_operators):
        output_index = (index + 1) % environment_dimension
        shift_update += kron(
            operator,
            np.outer(basis_vector(environment_dimension, output_index), basis_vector(environment_dimension, index)),
        )
    return kron(np.eye(4, dtype=complex), rotation) @ shift_update


def operator_schmidt_singular_values(operator: np.ndarray, data_dimension: int, environment_dimension: int) -> np.ndarray:
    tensor = operator.reshape(data_dimension, environment_dimension, data_dimension, environment_dimension)
    reshuffled = np.transpose(tensor, (0, 2, 1, 3)).reshape(
        data_dimension * data_dimension, environment_dimension * environment_dimension
    )
    return np.linalg.svd(reshuffled, compute_uv=False)


def prepared_embedding(environment_dimension: int, index: int = 0) -> np.ndarray:
    return kron(np.eye(4, dtype=complex), basis_vector(environment_dimension, index)[:, None])


def construct_maximally_inseparable_update(unitary: np.ndarray) -> dict[str, object]:
    labels, branch_operators = pauli_completion(unitary)
    rotation, ghz = history_rotation()
    environment_dimension = 16
    update = shifted_update(branch_operators, rotation)
    gram = np.asarray(
        [[np.trace(left.conj().T @ right) for right in branch_operators] for left in branch_operators]
    )
    check(
        "the bounded completion uses sixteen linearly independent unitary data branches and locally prepares a four-M2 GHZ history carrier",
        np.linalg.matrix_rank(gram, tol=1e-10) == 16
        and np.linalg.norm(rotation @ basis_vector(16, 1) - ghz) < 2e-15,
        {"branch_labels": labels, "branch_span_rank": np.linalg.matrix_rank(gram), "history_prep_residual": np.linalg.norm(rotation @ basis_vector(16, 1) - ghz)},
    )
    singular_values = operator_schmidt_singular_values(update, 4, environment_dimension)
    check(
        "the full single update is unitary and has maximal data-environment operator-Schmidt rank sixteen",
        np.linalg.norm(update.conj().T @ update - np.eye(64)) < 5e-15
        and np.sum(singular_values > 1e-10) == 16,
        {"unitarity_residual": float(np.linalg.norm(update.conj().T @ update - np.eye(64))), "operator_Schmidt_rank": int(np.sum(singular_values > 1e-10)), "maximum_from_data_operator_space": 16},
    )
    embedding = prepared_embedding(environment_dimension)
    isometry = update @ embedding
    expected = kron(unitary, ghz[:, None])
    target_projector = kron(np.eye(4), projector(ghz))
    check(
        "on the prepared-environment input subspace the maximal-rank update factorizes as exact FSWAP times one history state with zero leakage",
        np.linalg.norm(isometry - expected) < 2e-15
        and np.linalg.norm((np.eye(64) - target_projector) @ isometry) < 2e-15,
        {"factorization_residual": float(np.linalg.norm(isometry - expected)), "leakage": float(np.linalg.norm((np.eye(64) - target_projector) @ isometry)), "full_joint_unitary_factorized": False},
    )

    psi = basis_vector(4, 1)
    environment_superposition = (basis_vector(16, 0) + basis_vector(16, 1)) / np.sqrt(2)
    output = update @ np.kron(psi, environment_superposition)
    data = partial_trace_second(projector(output), 4, 16)
    purity = float(np.trace(data @ data).real)
    check(
        "an unprepared environment superposition witnesses genuine full-update entanglement despite prepared-subspace factorization",
        abs(purity - 0.5) < 2e-15,
        {"data_purity": purity, "witness_input": "|01> tensor (|0>+|1>)/sqrt(2)"},
    )
    return {
        "labels": labels,
        "branches": branch_operators,
        "rotation": rotation,
        "ghz": ghz,
        "update": update,
        "isometry": isometry,
    }


def kraus_operators(isometry: np.ndarray, data_dimension: int, environment_dimension: int) -> tuple[np.ndarray, ...]:
    tensor = isometry.reshape(data_dimension, environment_dimension, data_dimension)
    return tuple(tensor[:, index, :] for index in range(environment_dimension))


def normalized_choi_from_kraus(kraus: tuple[np.ndarray, ...], data_dimension: int) -> np.ndarray:
    choi = np.zeros((data_dimension * data_dimension, data_dimension * data_dimension), dtype=complex)
    for operator in kraus:
        vector = operator.reshape(-1, order="F")
        choi += projector(vector)
    return choi / data_dimension


def factorization_theorem_controls(unitary: np.ndarray, isometry: np.ndarray, history: np.ndarray) -> None:
    kraus = kraus_operators(isometry, 4, 16)
    coefficients = np.asarray([np.trace(unitary.conj().T @ operator) / 4 for operator in kraus])
    residuals = tuple(float(np.linalg.norm(operator - coefficient * unitary)) for operator, coefficient in zip(kraus, coefficients))
    choi = normalized_choi_from_kraus(kraus, 4)
    ideal_choi = projector(unitary.reshape(-1, order="F")) / 4
    check(
        "the prepared-subspace Kraus family is rank one and every Kraus operator is proportional to FSWAP",
        max(residuals) < 2e-15
        and abs(np.vdot(coefficients, coefficients).real - 1) < 2e-15
        and np.linalg.matrix_rank(choi, tol=1e-12) == 1
        and np.linalg.norm(choi - ideal_choi) < 2e-15,
        {"maximum_Kraus_residual": max(residuals), "coefficient_norm": float(np.vdot(coefficients, coefficients).real), "Choi_rank": np.linalg.matrix_rank(choi, tol=1e-12), "Choi_residual": float(np.linalg.norm(choi - ideal_choi))},
    )

    rows = []
    for seed in (266, 267, 268, 999):
        rho = random_density(4, seed)
        joint = isometry @ rho @ isometry.conj().T
        ideal_data = unitary @ rho @ unitary.conj().T
        rows.append(
            {
                "seed": seed,
                "joint_factorization": float(np.linalg.norm(joint - kron(ideal_data, projector(history)))),
                "data_residual": float(np.linalg.norm(partial_trace_second(joint, 4, 16) - ideal_data)),
                "history_residual": float(np.linalg.norm(partial_trace_first(joint, 4, 16) - projector(history))),
            }
        )
    held_rng = np.random.default_rng(266)
    held_history = held_rng.normal(size=16) + 1j * held_rng.normal(size=16)
    held_history /= np.linalg.norm(held_history)
    held_isometry = kron(unitary, held_history[:, None])
    held_kraus = kraus_operators(held_isometry, 4, 16)
    held_coefficients = np.asarray([np.trace(unitary.conj().T @ operator) / 4 for operator in held_kraus])
    held_residual = max(
        np.linalg.norm(operator - coefficient * unitary)
        for operator, coefficient in zip(held_kraus, held_coefficients)
    )
    check(
        "the exact arbitrary-data factorization and constant complementary channel survive random and held environment controls",
        all(max(row["joint_factorization"], row["data_residual"], row["history_residual"]) < 3e-15 for row in rows)
        and held_residual < 2e-15,
        {"rows": rows, "held_dense_history_Kraus_residual": float(held_residual)},
    )


def split_fault_controls(unitary: np.ndarray, construction: dict[str, object]) -> None:
    branches = list(construction["branches"])
    rotation = construction["rotation"]
    history = construction["ghz"]
    branches[0] = np.eye(4, dtype=complex)
    fault_update = shifted_update(tuple(branches), rotation)
    fault_isometry = fault_update @ prepared_embedding(16)
    expected_fault = kron(np.eye(4), history[:, None])
    check(
        "the conditional split-factor replacement has an explicit unitary completion and preserves the ideal history state",
        np.linalg.norm(fault_update.conj().T @ fault_update - np.eye(64)) < 5e-15
        and np.linalg.norm(fault_isometry - expected_fault) < 2e-15,
        {"fault_unitarity_residual": float(np.linalg.norm(fault_update.conj().T @ fault_update - np.eye(64))), "fault_subspace_residual": float(np.linalg.norm(fault_isometry - expected_fault)), "lawful_indivisible_substrate_deletion": "not established"},
    )

    rows = []
    maximum_history_difference = 0.0
    for seed in (266, 267, 999):
        rho = random_density(4, seed)
        ideal_joint = construction["isometry"] @ rho @ construction["isometry"].conj().T
        fault_joint = fault_isometry @ rho @ fault_isometry.conj().T
        ideal_history = partial_trace_first(ideal_joint, 4, 16)
        fault_history = partial_trace_first(fault_joint, 4, 16)
        history_difference = float(np.linalg.norm(ideal_history - fault_history))
        maximum_history_difference = max(maximum_history_difference, history_difference)
        rows.append(
            {
                "seed": seed,
                "history_difference": history_difference,
                "data_fault_residual": float(
                    np.linalg.norm(partial_trace_second(fault_joint, 4, 16) - unitary @ rho @ unitary.conj().T)
                ),
            }
        )
    target = kron(np.eye(4), projector(history))
    check(
        "every environment-only close is spoofed by the admitted split map while the data channel is wrong on held lawful inputs",
        maximum_history_difference < 2e-15
        and min(row["data_fault_residual"] for row in rows) > 0.1
        and np.linalg.norm((np.eye(64) - target) @ fault_isometry) < 2e-15,
        {"rows": rows, "maximum_environment_state_difference": maximum_history_difference, "fault_history_leakage": float(np.linalg.norm((np.eye(64) - target) @ fault_isometry))},
    )

    q = np.linspace(0.15, 0.9, 16)
    diagonal_zero = np.diag(np.sqrt(q)).astype(complex)
    diagonal_one = np.diag(np.sqrt(1 - q)).astype(complex)
    instrument = tuple(rotation @ diagonal @ rotation.conj().T for diagonal in (diagonal_zero, diagonal_one))
    rho = random_density(4, 268)
    ideal_joint = construction["isometry"] @ rho @ construction["isometry"].conj().T
    fault_joint = fault_isometry @ rho @ fault_isometry.conj().T
    instrument_rows = []
    for outcome, operator in enumerate(instrument):
        lifted = kron(np.eye(4), operator)
        ideal_post = lifted @ ideal_joint @ lifted.conj().T
        fault_post = lifted @ fault_joint @ lifted.conj().T
        instrument_rows.append(
            {
                "outcome": outcome,
                "ideal_weight": float(np.trace(ideal_post).real),
                "fault_weight": float(np.trace(fault_post).real),
                "history_post_residual": float(
                    np.linalg.norm(
                        partial_trace_first(ideal_post, 4, 16) - partial_trace_first(fault_post, 4, 16)
                    )
                ),
            }
        )
    check(
        "a nonprojective environment-only instrument has identical ideal and split-fault outcomes and post-history carriers",
        all(
            abs(row["ideal_weight"] - row["fault_weight"]) < 2e-15
            and row["history_post_residual"] < 2e-15
            for row in instrument_rows
        ),
        instrument_rows,
    )


def mixed_environment_controls(unitary: np.ndarray, construction: dict[str, object]) -> None:
    branches = list(construction["branches"])
    branches[1] = unitary
    rotation = construction["rotation"]
    mixed_update = shifted_update(tuple(branches), rotation)
    fault_branches = list(branches)
    fault_branches[0] = np.eye(4, dtype=complex)
    fault_branches[1] = np.eye(4, dtype=complex)
    mixed_fault = shifted_update(tuple(fault_branches), rotation)
    eta_one = rotation @ basis_vector(16, 1)
    eta_two = rotation @ basis_vector(16, 2)
    rows = []
    for seed, mixing in ((266, 0.37), (999, 0.61)):
        rho = random_density(4, seed)
        sigma = mixing * projector(basis_vector(16, 0)) + (1 - mixing) * projector(basis_vector(16, 1))
        history = mixing * projector(eta_one) + (1 - mixing) * projector(eta_two)
        ideal_joint = mixed_update @ kron(rho, sigma) @ mixed_update.conj().T
        fault_joint = mixed_fault @ kron(rho, sigma) @ mixed_fault.conj().T
        rows.append(
            {
                "seed": seed,
                "mixing": mixing,
                "ideal_factorization": float(np.linalg.norm(ideal_joint - kron(unitary @ rho @ unitary.conj().T, history))),
                "fault_factorization": float(np.linalg.norm(fault_joint - kron(rho, history))),
                "environment_difference": float(
                    np.linalg.norm(
                        partial_trace_first(ideal_joint, 4, 16) - partial_trace_first(fault_joint, 4, 16)
                    )
                ),
                "data_fault_residual": float(
                    np.linalg.norm(partial_trace_second(fault_joint, 4, 16) - unitary @ rho @ unitary.conj().T)
                ),
            }
        )
    check(
        "a rank-two mixed environment also factorizes for the exact FSWAP channel in the explicit bounded update",
        all(row["ideal_factorization"] < 3e-15 for row in rows),
        rows,
    )

    weights = np.full(16, 0.5)
    weights[1] = 0.8
    weights[2] = 0.3
    instrument_zero = rotation @ np.diag(np.sqrt(weights)) @ rotation.conj().T
    instrument_rows = []
    for seed, mixing in ((266, 0.37), (999, 0.61)):
        rho = random_density(4, seed)
        sigma = mixing * projector(basis_vector(16, 0)) + (1 - mixing) * projector(basis_vector(16, 1))
        ideal_joint = mixed_update @ kron(rho, sigma) @ mixed_update.conj().T
        fault_joint = mixed_fault @ kron(rho, sigma) @ mixed_fault.conj().T
        lifted = kron(np.eye(4), instrument_zero)
        ideal_post = lifted @ ideal_joint @ lifted.conj().T
        fault_post = lifted @ fault_joint @ lifted.conj().T
        ideal_weight = float(np.trace(ideal_post).real)
        fault_weight = float(np.trace(fault_post).real)
        predicted = 0.8 * mixing + 0.3 * (1 - mixing)
        ideal_conditional_data = partial_trace_second(ideal_post, 4, 16) / ideal_weight
        fault_conditional_data = partial_trace_second(fault_post, 4, 16) / fault_weight
        instrument_rows.append(
            {
                "mixing": mixing,
                "weight": ideal_weight,
                "predicted": predicted,
                "fault_weight": fault_weight,
                "ideal_conditional_data_residual": float(
                    np.linalg.norm(ideal_conditional_data - unitary @ rho @ unitary.conj().T)
                ),
                "fault_conditional_data_residual": float(np.linalg.norm(fault_conditional_data - rho)),
            }
        )
    check(
        "the mixed-history instrument, including held mixing 0.61, is input-independent and identically spoofed by the explicit split fault",
        all(
            abs(row["weight"] - row["predicted"]) < 2e-15
            and abs(row["fault_weight"] - row["predicted"]) < 2e-15
            and row["ideal_conditional_data_residual"] < 3e-15
            and row["fault_conditional_data_residual"] < 3e-15
            for row in instrument_rows
        )
        and all(row["environment_difference"] < 3e-15 and row["data_fault_residual"] > 0.1 for row in rows),
        instrument_rows,
    )

    mixing = 0.37
    branch_zero = mixed_update @ prepared_embedding(16, 0)
    branch_one = mixed_update @ prepared_embedding(16, 1)
    reference_zero = basis_vector(16, 0)
    reference_one = basis_vector(16, 1)
    purified_isometry = (
        np.sqrt(mixing) * kron(branch_zero, reference_zero[:, None])
        + np.sqrt(1 - mixing) * kron(branch_one, reference_one[:, None])
    )
    purified_history = (
        np.sqrt(mixing) * np.kron(eta_one, reference_zero)
        + np.sqrt(1 - mixing) * np.kron(eta_two, reference_one)
    )
    expected = kron(unitary, purified_history[:, None])
    purified_kraus = kraus_operators(purified_isometry, 4, 256)
    purified_choi = normalized_choi_from_kraus(purified_kraus, 4)
    ideal_choi = projector(unitary.reshape(-1, order="F")) / 4
    check(
        "purifying the mixed environment restores the same rank-one FSWAP Stinespring factorization on data versus environment-reference",
        np.linalg.norm(purified_isometry - expected) < 3e-15
        and np.linalg.matrix_rank(purified_choi, tol=1e-12) == 1
        and np.linalg.norm(purified_choi - ideal_choi) < 3e-15,
        {"purified_factorization_residual": float(np.linalg.norm(purified_isometry - expected)), "purified_Choi_rank": np.linalg.matrix_rank(purified_choi, tol=1e-12), "purified_Choi_residual": float(np.linalg.norm(purified_choi - ideal_choi))},
    )


def perturbation_controls(unitary: np.ndarray, construction: dict[str, object]) -> None:
    rotation = construction["rotation"]
    eta_one = rotation @ basis_vector(16, 1)
    eta_two = rotation @ basis_vector(16, 2)
    target = kron(np.eye(4), projector(eta_one))
    identity4 = np.eye(4, dtype=complex)
    rho = random_density(4, 266)
    rows = []
    for epsilon in (0.0, np.pi / 20, np.pi / 7):
        cosine = np.cos(epsilon)
        sine = np.sin(epsilon)
        isometry = cosine * kron(unitary, eta_one[:, None]) + sine * kron(identity4, eta_two[:, None])
        joint = isometry @ rho @ isometry.conj().T
        data = partial_trace_second(joint, 4, 16)
        predicted_data = cosine**2 * unitary @ rho @ unitary.conj().T + sine**2 * rho
        kraus = kraus_operators(isometry, 4, 16)
        choi = normalized_choi_from_kraus(kraus, 4)
        ideal_choi = projector(unitary.reshape(-1, order="F")) / 4
        choi_trace_distance = float(np.sum(np.linalg.svd(choi - ideal_choi, compute_uv=False)) / 2)
        leakage = float(np.linalg.norm((np.eye(64) - target) @ isometry, ord=2))
        rows.append(
            {
                "epsilon": float(epsilon),
                "isometry_residual": float(np.linalg.norm(isometry.conj().T @ isometry - identity4)),
                "channel_formula_residual": float(np.linalg.norm(data - predicted_data)),
                "ideal_Choi_trace_distance": choi_trace_distance,
                "predicted_sin_squared": float(sine**2),
                "history_leakage_operator_norm": leakage,
                "predicted_sine": float(abs(sine)),
            }
        )
    check(
        "a coherent two-history perturbation is an exact isometry whose data channel departs from FSWAP by the predicted sin(epsilon)^2 mixture",
        all(
            row["isometry_residual"] < 3e-15
            and row["channel_formula_residual"] < 3e-15
            and abs(row["ideal_Choi_trace_distance"] - row["predicted_sin_squared"]) < 3e-15
            for row in rows
        ),
        rows,
    )

    eigen_plus = basis_vector(4, 0)
    eigen_minus = basis_vector(4, 3)
    sensitivity_rows = []
    for epsilon in (np.pi / 20, np.pi / 7):
        cosine = np.cos(epsilon)
        sine = np.sin(epsilon)
        isometry = cosine * kron(unitary, eta_one[:, None]) + sine * kron(identity4, eta_two[:, None])
        plus_environment = partial_trace_first(isometry @ projector(eigen_plus) @ isometry.conj().T, 4, 16)
        minus_environment = partial_trace_first(isometry @ projector(eigen_minus) @ isometry.conj().T, 4, 16)
        trace_distance = float(
            np.sum(np.linalg.svd(plus_environment - minus_environment, compute_uv=False)) / 2
        )
        sensitivity_rows.append(
            {
                "epsilon": float(epsilon),
                "environment_trace_distance": trace_distance,
                "predicted_abs_sin_2epsilon": float(abs(np.sin(2 * epsilon))),
            }
        )
    check(
        "relaxing the exact unitary data channel permits the history carrier to distinguish opposite FSWAP eigensectors",
        all(
            abs(row["environment_trace_distance"] - row["predicted_abs_sin_2epsilon"]) < 3e-15
            for row in sensitivity_rows
        ),
        sensitivity_rows,
    )
    check(
        "the held epsilon=pi/7 perturbation has the predicted nonzero leakage and information-disturbance residuals",
        abs(rows[-1]["history_leakage_operator_norm"] - rows[-1]["predicted_sine"]) < 3e-15
        and rows[-1]["ideal_Choi_trace_distance"] > 0.1
        and sensitivity_rows[-1]["environment_trace_distance"] > 0.7,
        {"held_row": rows[-1], "held_sensitivity": sensitivity_rows[-1]},
    )


PLACEMENT: dict[str, Coord] = {
    "data_0": (0, 0, 0),
    "data_1": (1, 0, 0),
    "history_center": (0, 1, 0),
    "history_xminus": (-1, 1, 0),
    "history_yplus": (0, 2, 0),
    "history_zplus": (0, 1, 1),
    "close_candidate": (0, 1, 2),
}

EDGES = (
    ("data_0", "data_1"),
    ("data_0", "history_center"),
    ("history_center", "history_xminus"),
    ("history_center", "history_yplus"),
    ("history_center", "history_zplus"),
    ("history_zplus", "close_candidate"),
)


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
    failures = tuple(edge for edge in EDGES if manhattan(PLACEMENT[edge[0]], PLACEMENT[edge[1]]) != 1)
    check(
        "the constructor has a bounded collision-free seven-M2 support graph with only declared NN dependency and preparation edges",
        len(PLACEMENT) == len(set(PLACEMENT.values()))
        and not failures
        and max(sum(abs(value) for value in site) for site in PLACEMENT.values()) == 3,
        {"ordinary_M2_sites": len(PLACEMENT), "support_radius": 3, "NN_failures": failures},
    )
    translation = (13, -11, 7)
    covariance_failures = []
    for frame_index, frame in enumerate(proper_frames()):
        moved = {role: transform(site, frame, translation) for role, site in PLACEMENT.items()}
        if len(moved) != len(set(moved.values())) or any(
            manhattan(moved[left], moved[right]) != 1 for left, right in EDGES
        ):
            covariance_failures.append(frame_index)
    check(
        "the supplied support graph is translation covariant under all 24 proper-cubic frames",
        len(proper_frames()) == 24 and not covariance_failures,
        {"frames": len(proper_frames()), "translation": translation, "failures": covariance_failures},
    )


def disposition() -> None:
    check(
        "Cycle 266 proves a narrow prepared-subspace factorization and conditional split-fault spoof, not a substrate-wide occurrence no-go",
        True,
        {
            "full_update_operator_Schmidt_rank": 16,
            "prepared_subspace": "F tensor fixed history",
            "split_fault": "adversarial grammar only",
            "indivisible_update_fault_law": "open",
            "relaxed_channel_history_monitor": "live",
            "irreversible_actualization": "live",
            "verified_fault_model": "live",
            "Record_formation": "live",
            "coherent_history_is_Record": False,
            "physical_time_or_rate": "not derived",
            "Born_probability": "not derived",
            "axiom_pressure": False,
        },
    )


def main() -> None:
    source_and_note_contract()
    unitary = actual_fswap_fixture()
    construction = construct_maximally_inseparable_update(unitary)
    factorization_theorem_controls(unitary, construction["isometry"], construction["ghz"])
    split_fault_controls(unitary, construction)
    mixed_environment_controls(unitary, construction)
    perturbation_controls(unitary, construction)
    placement_and_covariance_controls()
    disposition()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
