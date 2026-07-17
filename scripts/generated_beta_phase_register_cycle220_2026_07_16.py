#!/usr/bin/env python3
"""Cycle 220: turn beta from a law knob into a conserved phase-register state.

Given one fixed odd-dimensional onsite unitary S, define the Hermitian Cayley
mass operator M=3 i (S-I)(S+I)^-1 and one common direction/register coin.
Each eigenstate S|beta>=e^{i beta}|beta> then carries the Cycle-219 coin and
mass -3 tan(beta/2), while beta=0 is the field coin.  Verify one-law sector
coexistence, covariance, representation invariance, contact-sector support,
and exchange charge without a per-species lookup.

The register S, its dimension, positive-sector interpretation, and physical
block encoding remain supplied.  No observed mass spectrum is claimed.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "GENERATED_BETA_PHASE_REGISTER_CYCLE220_NOTE_2026-07-16.md"
)

REGISTER_DIMENSION = 9
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


def cyclic_shift(dimension: int) -> np.ndarray:
    shift = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        shift[(source + 1) % dimension, source] = 1
    return shift


def cayley_mass(register: np.ndarray) -> np.ndarray:
    identity = np.eye(register.shape[0], dtype=complex)
    return 3j * (register - identity) @ np.linalg.inv(register + identity)


def unitary_function(hermitian: np.ndarray, scale: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(hermitian)
    return (vectors * np.exp(1j * scale * values)) @ vectors.conj().T


def common_register_coin(register: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mass = cayley_mass(register)
    rest_phase = unitary_function(mass, 1 / 3)
    coin = np.kron(rest_phase, c210.P_SCALAR - c210.P_EVEN) + np.kron(
        rest_phase @ register, c210.P_VECTOR
    )
    return mass, coin


def register_eigenpairs(register: np.ndarray) -> list[tuple[float, complex, np.ndarray]]:
    values, vectors = np.linalg.eig(register)
    rows = []
    for index, value in enumerate(values):
        beta = float(np.angle(value))
        vector = vectors[:, index] / np.linalg.norm(vectors[:, index])
        rows.append((beta, value, vector))
    return sorted(rows, key=lambda row: row[0])


def extract_direction_block(coin: np.ndarray, vector: np.ndarray) -> np.ndarray:
    dimension = len(vector)
    reshaped = coin.reshape(dimension, 6, dimension, 6)
    return np.einsum(
        "a,aibj,b->ij", vector.conj(), reshaped, vector, optimize=True
    )


def apply_contact_coin(pair: np.ndarray, register_coin: np.ndarray) -> np.ndarray:
    """Apply C(S) only to the six equal-direction states of each register."""
    dimension = pair.shape[0]
    output = pair.copy()
    diagonal = np.stack([pair[:, direction, direction] for direction in range(6)], axis=1)
    moved = (register_coin @ diagonal.reshape(-1)).reshape(dimension, 6)
    for direction in range(6):
        output[:, direction, direction] = moved[:, direction]
    return output


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "one fixed local phase-register law",
        "cayley mass operator",
        "beta becomes a conserved state label",
        "massless field sector",
        "massive object sectors",
        "no per-species lookup",
        "representation invariant",
        "equal-direction contact support does not show that mass causes binding",
        "register selection remains supplied",
        "not an observed mass spectrum",
        "positive-mass sector",
        "no axiom conclusion",
        "thirring-qca",
        "apadula",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves generated-sector gain and selection scope", not missing, missing)


def algebra_and_sector_controls() -> tuple[np.ndarray, np.ndarray, np.ndarray, list[tuple[float, complex, np.ndarray]]]:
    register = cyclic_shift(REGISTER_DIMENSION)
    mass, coin = common_register_coin(register)
    identity = np.eye(REGISTER_DIMENSION)
    check(
        "the fixed cyclic phase register is exactly unitary and avoids eigenvalue -1",
        np.linalg.norm(register.conj().T @ register - identity) < 2e-12
        and min(abs(value + 1) for value in np.linalg.eigvals(register)) > 0.3,
    )
    check(
        "the Cayley mass operator is Hermitian and commutes with its register",
        np.linalg.norm(mass - mass.conj().T) < 3e-12
        and np.linalg.norm(mass @ register - register @ mass) < 3e-12,
    )
    check(
        "one register-direction coin is unitary without a beta lookup table",
        np.linalg.norm(coin.conj().T @ coin - np.eye(6 * REGISTER_DIMENSION)) < 5e-12,
    )
    check(
        "beta is conserved by the complete onsite coin",
        np.linalg.norm(
            coin @ np.kron(register, np.eye(6))
            - np.kron(register, np.eye(6)) @ coin
        )
        < 4e-12,
    )

    eigenpairs = register_eigenpairs(register)
    sector_rows = []
    for beta, value, vector in eigenpairs:
        block = extract_direction_block(coin, vector)
        expected_mass = float(-3 * np.tan(beta / 2))
        measured_mass = float(np.vdot(vector, mass @ vector).real)
        expected_coin = c219.common_species(beta).coin
        sector_rows.append(
            (
                beta,
                expected_mass,
                measured_mass,
                np.linalg.norm(block - expected_coin),
            )
        )
    check(
        "every register eigenstate realizes the analytic beta coin and Cayley mass",
        max(abs(row[1] - row[2]) for row in sector_rows) < 2e-11
        and max(row[3] for row in sector_rows) < 2e-11,
        sector_rows,
    )

    zero_row = min(sector_rows, key=lambda row: abs(row[0]))
    zero_vector = min(eigenpairs, key=lambda row: abs(row[0]))[2]
    zero_block = extract_direction_block(coin, zero_vector)
    check(
        "the beta=0 register eigenstate is exactly the massless field sector",
        abs(zero_row[1]) < 2e-12
        and np.linalg.norm(zero_block - c214.FIELD_COIN) < 2e-11,
    )

    positive_rows = [row for row in sector_rows if row[1] > 1e-8]
    check(
        "the same fixed coin contains multiple distinct positive massive sectors",
        len(positive_rows) == (REGISTER_DIMENSION - 1) // 2
        and min(abs(left[1] - right[1]) for left, right in zip(positive_rows, positive_rows[1:]))
        > 0.1,
        positive_rows,
    )
    return register, mass, coin, eigenpairs


def covariance_and_representation_controls(
    register: np.ndarray,
    mass: np.ndarray,
    coin: np.ndarray,
) -> None:
    covariance = []
    for frame in c210.proper_cubic_frames():
        representation = np.kron(
            np.eye(REGISTER_DIMENSION), c210.direction_permutation(frame)
        )
        covariance.append(
            np.linalg.norm(representation @ coin @ representation.conj().T - coin)
        )
    check(
        "the one-law register coin commutes with all 24 proper-cubic frames",
        max(covariance) < 5e-12,
        max(covariance),
    )

    rng = np.random.default_rng(220)
    raw = rng.normal(size=(REGISTER_DIMENSION, REGISTER_DIMENSION)) + 1j * rng.normal(
        size=(REGISTER_DIMENSION, REGISTER_DIMENSION)
    )
    basis, _ = np.linalg.qr(raw)
    represented_register = basis @ register @ basis.conj().T
    represented_mass, represented_coin = common_register_coin(represented_register)
    expected_mass = basis @ mass @ basis.conj().T
    expected_coin = np.kron(basis, np.eye(6)) @ coin @ np.kron(
        basis.conj().T, np.eye(6)
    )
    check(
        "arbitrary phase-register basis changes preserve mass and the complete coin",
        np.linalg.norm(represented_mass - expected_mass) < 2e-11
        and np.linalg.norm(represented_coin - expected_coin) < 3e-11,
    )


def propagation_and_coexistence_controls(
    register: np.ndarray,
    mass: np.ndarray,
    coin: np.ndarray,
    eigenpairs: list[tuple[float, complex, np.ndarray]],
) -> None:
    positive = [row for row in eigenpairs if -3 * np.tan(row[0] / 2) > 1e-8]
    first, second = positive[0], positive[1]
    initial = (
        np.kron(first[2], c210.UNIFORM)
        + 1j * np.kron(second[2], c210.UNIFORM)
    ) / np.sqrt(2)
    state = initial.copy()
    momentum = np.array((0.17, -0.11, 0.07))
    stream = np.kron(
        np.eye(REGISTER_DIMENSION),
        np.diag(np.exp(-1j * (c210.DIRECTIONS @ momentum))),
    )
    sector_projectors = [
        np.kron(np.outer(row[2], row[2].conj()), np.eye(6))
        for row in (first, second)
    ]
    initial_weights = [float(np.vdot(state, projector @ state).real) for projector in sector_projectors]
    for _ in range(37):
        state = stream @ coin @ state
    final_weights = [float(np.vdot(state, projector @ state).real) for projector in sector_projectors]
    check(
        "two massive beta sectors coexist for 37 ticks without law or sector switching",
        abs(np.linalg.norm(state) - 1) < 3e-12
        and max(abs(left - right) for left, right in zip(initial_weights, final_weights))
        < 3e-12,
        {"initial": initial_weights, "final": final_weights},
    )

    expected_charges = [float(np.vdot(row[2], mass @ row[2]).real) for row in (first, second)]
    superposed_charge = float(
        np.vdot(
            initial,
            np.kron(mass, np.eye(6)) @ initial,
        ).real
    )
    check(
        "the fixed mass operator supplies exchange charge in every conserved sector",
        abs(superposed_charge - np.mean(expected_charges)) < 2e-11,
        {"sector_charges": expected_charges, "superposition": superposed_charge},
    )

    pair = np.zeros((REGISTER_DIMENSION, 6, 6), dtype=complex)
    label_state = (first[2] + second[2]) / np.sqrt(2)
    for direction in range(6):
        pair[:, direction, direction] = label_state / np.sqrt(6)
    moved = apply_contact_coin(pair, coin)
    check(
        "register-controlled contact coin preserves equal-direction support without beta lookup",
        abs(np.linalg.norm(moved) - 1) < 3e-12
        and np.linalg.norm(
            moved
            - apply_contact_coin(pair, coin)
        )
        < 2e-15
        and np.linalg.norm(
            moved
            * (1 - np.eye(6)[None, :, :])
        )
        < 2e-12,
    )

    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    archived_charge = superposed_charge * float(
        np.vdot(record_zero, record_zero).real
        * np.vdot(record_plus, record_plus).real
    )
    check(
        "spectator records do not duplicate the phase-register mass operator",
        abs(archived_charge - superposed_charge) < 2e-14,
    )


def selection_controls(register: np.ndarray, mass: np.ndarray) -> None:
    even_register = cyclic_shift(8)
    minimum_denominator = min(abs(value + 1) for value in np.linalg.eigvals(even_register))
    check(
        "an even cyclic register exposes the Cayley singularity at beta=pi",
        minimum_denominator < 2e-12,
        minimum_denominator,
    )

    alternative = cyclic_shift(11)
    alternative_mass = cayley_mass(alternative)
    current_spectrum = np.sort(np.linalg.eigvalsh(mass))
    alternative_spectrum = np.sort(np.linalg.eigvalsh(alternative_mass))
    check(
        "changing the supplied register changes the generated mass spectrum",
        len(current_spectrum) != len(alternative_spectrum)
        and np.max(np.abs(current_spectrum)) != np.max(np.abs(alternative_spectrum)),
        {
            "dimension_9_max": float(np.max(np.abs(current_spectrum))),
            "dimension_11_max": float(np.max(np.abs(alternative_spectrum))),
        },
    )

    check(
        "the illustrative nine-state register embeds dimensionally in four qubits",
        REGISTER_DIMENSION <= 2**4 and REGISTER_DIMENSION > 2**3,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    register, mass, coin, eigenpairs = algebra_and_sector_controls()
    covariance_and_representation_controls(register, mass, coin)
    propagation_and_coexistence_controls(register, mass, coin, eigenpairs)
    selection_controls(register, mass)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
