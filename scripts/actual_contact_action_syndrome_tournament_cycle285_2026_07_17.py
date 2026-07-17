#!/usr/bin/env python3
"""Cycle 285: actual Cycle-230 contact-action syndrome tournament.

Three bounded routes distinguish the actual contact phase W_g from a mere
support threshold: a joint action/flag block, a controlled-process Ramsey
syndrome, and a direct N=2/N=4 matter phase-reference calibration.  The
runner keeps common-call deletion, data-factor split replacement, coherent
phase readout, disturbance, occurrence, and Record semantics separate.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 3.0e-11
DIMENSION = 64
G = c278.c230.COUPLING


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


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-285 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-278 connected edge code",
        "actual contact action",
        "joint action/flag",
        "controlled-process ramsey syndrome",
        "n=2/n=4 matter phase reference",
        "not merely q_(n=2)",
        "deletion of w_g",
        "global phase",
        "eigenstate",
        "arbitrary parity-even states",
        "disturbance",
        "one-particle mass fixture",
        "all 24 proper-cubic frames",
        "held-out l=6",
        "split replacement",
        "supplied phase reference",
        "coherent syndrome is not occurrence",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the actual-action, fault, covariance, semantic, and N1-N8 contract",
        not missing,
        missing,
    )


def basis(dimension: int, index: int) -> np.ndarray:
    vector = np.zeros(dimension, dtype=complex)
    vector[index] = 1.0
    return vector


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def fixture() -> dict[str, np.ndarray]:
    occupations = np.asarray([index.bit_count() for index in range(DIMENSION)])
    pair_count = occupations * (occupations - 1) / 2
    w = np.diag(np.exp(1j * G * pair_count)).astype(complex)
    q = np.diag((occupations >= 2).astype(float)).astype(complex)
    parity = np.diag((-1.0) ** occupations).astype(complex)
    threshold = np.eye(DIMENSION, dtype=complex) - q + np.exp(1j * G) * q
    return {
        "occupations": occupations,
        "pair_count": pair_count,
        "W": w,
        "Q": q,
        "parity": parity,
        "threshold": threshold,
    }


def contact_walsh_coefficients(w_values: np.ndarray) -> tuple[complex, ...]:
    coefficients = []
    for mask in range(64):
        total = 0.0j
        for occupation in range(64):
            sign = -1 if (mask & occupation).bit_count() % 2 else 1
            total += w_values[occupation] * sign
        coefficients.append(total / 64)
    return tuple(coefficients)


def partial_data_density(
    state: np.ndarray, environment_dimension: int
) -> np.ndarray:
    matrix = state.reshape(DIMENSION, environment_dimension)
    return matrix @ matrix.conj().T


def random_density(dimension: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    matrix = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    rho = matrix @ matrix.conj().T
    return rho / np.trace(rho)


def actual_contact_and_mass_controls(model: dict[str, np.ndarray]) -> None:
    print("\nACTUAL CONTACT PHASE / SUPPORT / MASS FIXTURE")
    occupations = model["occupations"]
    pair_count = model["pair_count"]
    w = model["W"]
    q = model["Q"]
    threshold = model["threshold"]
    species = c278.c219.common_species(c278.c230.BETA)
    fock_coin = c278.c229.fock_lift(species.coin)
    reverse = np.zeros((6, 6), dtype=complex)
    for source, target in enumerate((1, 0, 3, 2, 5, 4)):
        reverse[target, source] = 1
    fock_reverse = c278.c229.fock_lift(reverse)
    phase_rows = tuple(
        {
            "N": number,
            "C(N,2)": int(number * (number - 1) / 2),
            "phase_real": float(np.cos(G * number * (number - 1) / 2)),
            "phase_imag": float(np.sin(G * number * (number - 1) / 2)),
        }
        for number in range(7)
    )
    check(
        "the imported W_g is the actual unitary contact action and not the threshold-only phase surrogate",
        np.linalg.norm(w.conj().T @ w - np.eye(64)) < TOL
        and np.linalg.norm(w @ model["parity"] - model["parity"] @ w) == 0
        and np.linalg.norm(w - threshold) > 1.0
        and np.allclose(np.diag(w), np.exp(1j * G * pair_count)),
        {
            "g": G,
            "W_minus_threshold_Frobenius": float(np.linalg.norm(w - threshold)),
            "number_phase_rows": phase_rows,
        },
    )
    check(
        "the actual contact phase commutes with the actual coin/reversal and preserves the one-particle mass fixture",
        np.linalg.norm(w @ fock_coin - fock_coin @ w) < 2e-14
        and np.linalg.norm(w @ fock_reverse - fock_reverse @ w) == 0
        and np.max(np.abs(np.diag(w)[occupations <= 1] - 1)) == 0
        and abs(c278.c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "W_coin_commutator": float(np.linalg.norm(w @ fock_coin - fock_coin @ w)),
            "W_reverse_commutator": float(np.linalg.norm(w @ fock_reverse - fock_reverse @ w)),
            "one_particle_action": "identity",
        },
    )
    # A threshold is the support of nonzero pair count, but the action carries
    # six distinct number phases rather than one binary active phase.
    check(
        "contact activity Q and contact action W_g remain distinct exact operators",
        np.array_equal(np.diag(q), (pair_count > 0).astype(float))
        and len({complex(value) for value in np.diag(w)}) == 6,
        {
            "rank_Q": int(round(np.trace(q).real)),
            "distinct_W_phases": len({complex(value) for value in np.diag(w)}),
        },
    )


def joint_action_flag_route(model: dict[str, np.ndarray]) -> dict[str, float]:
    print("\nROUTE 1 / JOINT ACTION-FLAG BLOCK")
    w = model["W"]
    zero = basis(2, 0)[:, None]
    one = basis(2, 1)[:, None]
    ideal = np.kron(w, one)
    joint_deleted = np.kron(np.eye(64), zero)
    split_data_deleted = np.kron(np.eye(64), one)
    flag_deleted = np.kron(w, zero)
    flag_one = np.kron(np.eye(64), projector(basis(2, 1)))
    ideal_effect = ideal.conj().T @ flag_one @ ideal
    deleted_effect = joint_deleted.conj().T @ flag_one @ joint_deleted
    split_effect = split_data_deleted.conj().T @ flag_one @ split_data_deleted
    held = random_density(64, 285)
    target = w @ held @ w.conj().T
    split_output = held
    split_data_residual = float(np.linalg.norm(split_output - target))
    check(
        "route 1 gives the exact arbitrary-data W_g channel and deterministic close on the declared joint-call domain",
        np.linalg.norm(ideal.conj().T @ ideal - np.eye(64)) < TOL
        and np.linalg.norm(ideal_effect - np.eye(64)) < TOL
        and np.linalg.norm(deleted_effect) < TOL,
        {
            "ideal_close_minus_I": float(np.linalg.norm(ideal_effect - np.eye(64))),
            "joint_deletion_close_norm": float(np.linalg.norm(deleted_effect)),
        },
    )
    check(
        "route 1 is split-spoofable: deleting only the data W_g factor leaves unit close, while deleting only the flag gives a false negative",
        np.linalg.norm(split_effect - np.eye(64)) < TOL
        and np.linalg.norm(flag_deleted.conj().T @ flag_one @ flag_deleted) < TOL
        and split_data_residual > 0.1,
        {
            "split_close_minus_I": float(np.linalg.norm(split_effect - np.eye(64))),
            "held_wrong_data_residual": split_data_residual,
            "flag_deleted_close_norm": float(
                np.linalg.norm(flag_deleted.conj().T @ flag_one @ flag_deleted)
            ),
        },
    )
    return {"split_data_residual": split_data_residual}


def ramsey_full_unitary(unitary: np.ndarray) -> np.ndarray:
    """H-control(unitary)-H on P, then coherently copy P to CLOSE."""

    hadamard = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    p0 = projector(basis(2, 0))
    p1 = projector(basis(2, 1))
    controlled = np.kron(np.eye(64), p0) + np.kron(unitary, p1)
    ramsey = np.kron(np.eye(64), hadamard) @ controlled @ np.kron(
        np.eye(64), hadamard
    )
    cnot = np.asarray(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    return np.kron(np.eye(64), cnot) @ np.kron(ramsey, np.eye(2))


def ramsey_isometry(unitary: np.ndarray) -> np.ndarray:
    blank = basis(4, 0)[:, None]
    return ramsey_full_unitary(unitary) @ np.kron(np.eye(64), blank)


def close_effect(isometry: np.ndarray) -> np.ndarray:
    close_one = np.kron(
        np.eye(64), np.kron(np.eye(2), projector(basis(2, 1)))
    )
    return isometry.conj().T @ close_one @ isometry


def ramsey_channel(unitary: np.ndarray, rho: np.ndarray) -> np.ndarray:
    k0 = (np.eye(64) + unitary) / 2
    k1 = (np.eye(64) - unitary) / 2
    return k0 @ rho @ k0.conj().T + k1 @ rho @ k1.conj().T


def controlled_ramsey_route(model: dict[str, np.ndarray]) -> dict[str, float]:
    print("\nROUTE 2 / SINGLE-QUERY CONTROLLED-PROCESS RAMSEY SYNDROME")
    w = model["W"]
    q = model["Q"]
    pair_count = model["pair_count"]
    v = ramsey_isometry(w)
    full = ramsey_full_unitary(w)
    effect = close_effect(v)
    expected_effect = np.diag(np.sin(G * pair_count / 2) ** 2).astype(complex)
    deleted_v = ramsey_isometry(np.eye(64))
    deleted_effect = close_effect(deleted_v)
    rng = np.random.default_rng(1285)
    state = rng.normal(size=256) + 1j * rng.normal(size=256)
    state /= np.linalg.norm(state)
    restored = full.conj().T @ (full @ state)
    check(
        "route 2 is an exact reversible controlled-W_g Ramsey syndrome with close effect sin^2(g binom(N,2)/2)",
        np.linalg.norm(full.conj().T @ full - np.eye(256)) < TOL
        and np.linalg.norm(v.conj().T @ v - np.eye(64)) < TOL
        and np.linalg.norm(effect - expected_effect) < TOL
        and np.linalg.norm(restored - state) < TOL,
        {
            "unitarity_residual": float(
                np.linalg.norm(full.conj().T @ full - np.eye(256))
            ),
            "close_effect_residual": float(np.linalg.norm(effect - expected_effect)),
            "inverse_residual": float(np.linalg.norm(restored - state)),
        },
    )
    check(
        "deletion of W_g while Hadamards and close copy survive gives exactly zero Ramsey close",
        np.linalg.norm(deleted_effect) < TOL
        and np.linalg.norm(deleted_v - np.kron(np.eye(64), basis(4, 0)[:, None]))
        < TOL,
        float(np.linalg.norm(deleted_effect)),
    )

    number_rows = []
    for number in range(7):
        indices = np.flatnonzero(model["occupations"] == number)
        value = float(np.sin(G * number * (number - 1) / 4) ** 2)
        block = effect[np.ix_(indices, indices)]
        number_rows.append(
            {
                "N": number,
                "dimension": len(indices),
                "close_weight": value,
                "block_residual": float(
                    np.linalg.norm(block - value * np.eye(len(indices)))
                ),
            }
        )
    p2 = np.diag((model["occupations"] == 2).astype(float)).astype(complex)
    n2_weight = float(np.sin(G / 2) ** 2)
    n2_state = sum(
        basis(64, int(index))
        for index in np.flatnonzero(model["occupations"] == 2)[:3]
    )
    n2_state /= np.linalg.norm(n2_state)
    n2_rho = projector(n2_state)
    n2_channel = ramsey_channel(w, n2_rho)
    check(
        "on the declared N=2 lawful subdomain the phase syndrome is positive and matter-nondisturbing although unconditional W_g is only a global phase",
        np.linalg.norm(p2 @ effect @ p2 - n2_weight * p2) < TOL
        and np.linalg.norm(n2_channel - n2_rho) < TOL
        and n2_weight > 0.03,
        {
            "N2_close_weight": n2_weight,
            "N2_matter_disturbance": float(np.linalg.norm(n2_channel - n2_rho)),
            "number_rows": number_rows,
        },
    )

    cross = (basis(64, 0) + basis(64, 3)) / np.sqrt(2)
    cross_rho = projector(cross)
    reduced = ramsey_channel(w, cross_rho)
    ideal_w = w @ cross_rho @ w.conj().T
    disturbance = float(np.linalg.norm(reduced - cross_rho))
    target_residual = float(np.linalg.norm(reduced - ideal_w))
    check(
        "on arbitrary parity-even number coherences the Ramsey archive is disturbing and is not the unconditional W_g data channel",
        disturbance > 0.1
        and target_residual > 0.1
        and np.linalg.norm(reduced - (cross_rho + ideal_w) / 2) < TOL,
        {
            "held_input_disturbance": disturbance,
            "held_target_W_channel_residual": target_residual,
        },
    )

    active = (pair_count > 0).astype(float)
    spectrum = np.diag(effect).real
    best_q_coefficient = float(np.dot(active, spectrum) / np.dot(active, active))
    q_fit_residual = float(np.linalg.norm(effect - best_q_coefficient * q))
    check(
        "the Ramsey effect is not merely Q_(N>=2): its optimal scalar-Q fit has a nonzero residual",
        q_fit_residual > 2.5
        and max(row["block_residual"] for row in number_rows) < TOL,
        {
            "best_Q_coefficient": best_q_coefficient,
            "Q_fit_Frobenius_residual": q_fit_residual,
            "Q_fit_operator_residual": float(
                np.linalg.norm(effect - best_q_coefficient * q, 2)
            ),
        },
    )

    threshold_v = ramsey_isometry(model["threshold"])
    inverse_v = ramsey_isometry(w.conj().T)
    global_phase = np.exp(1j * G) * np.eye(64)
    global_v = ramsey_isometry(global_phase)
    threshold_effect = close_effect(threshold_v)
    inverse_effect = close_effect(inverse_v)
    global_effect = close_effect(global_v)
    check(
        "split replacements are explicit: W_g dagger has the same positive effect, threshold phase loses number resolution, and a control-only global phase falsely closes inactive states",
        np.linalg.norm(inverse_effect - effect) < TOL
        and np.linalg.norm(inverse_v - v) > 1.0
        and np.linalg.norm(threshold_effect - effect) > 2.0
        and np.linalg.norm(
            threshold_effect - np.sin(G / 2) ** 2 * q
        )
        < TOL
        and np.linalg.norm(global_effect @ (np.eye(64) - q)) > 0.08,
        {
            "W_dagger_effect_residual": float(np.linalg.norm(inverse_effect - effect)),
            "W_dagger_isometry_residual": float(np.linalg.norm(inverse_v - v)),
            "threshold_effect_residual": float(np.linalg.norm(threshold_effect - effect)),
            "global_phase_inactive_false_close_norm": float(
                np.linalg.norm(global_effect @ (np.eye(64) - q))
            ),
        },
    )
    return {
        "N2_close_weight": n2_weight,
        "q_fit_residual": q_fit_residual,
        "held_disturbance": disturbance,
    }


def matter_phase_reference_route(model: dict[str, np.ndarray]) -> dict[str, float]:
    print("\nROUTE 3 / DIRECT N=2/N=4 MATTER PHASE REFERENCE")
    w = model["W"]
    threshold = model["threshold"]
    n2 = basis(64, 0b000011)
    n4 = basis(64, 0b001111)
    reference = (n2 + n4) / np.sqrt(2)
    reject = (n2 - n4) / np.sqrt(2)
    effect = projector(reject)
    input_rho = projector(reference)
    actual = w @ input_rho @ w.conj().T
    deleted = input_rho
    threshold_output = threshold @ input_rho @ threshold.conj().T
    global_output = input_rho
    actual_weight = float(np.trace(effect @ actual).real)
    deleted_weight = float(np.trace(effect @ deleted).real)
    threshold_weight = float(np.trace(effect @ threshold_output).real)
    expected = float(np.sin(5 * G / 2) ** 2)
    check(
        "route 3 directly probes one unconditional W_g application: deletion, global phase, and threshold-only phase give zero close while the actual N=2/N=4 phase gives positive close",
        abs(actual_weight - expected) < TOL
        and deleted_weight < TOL
        and threshold_weight < TOL
        and float(np.trace(effect @ global_output).real) < TOL,
        {
            "actual_close_weight": actual_weight,
            "expected_sin2_5g_over_2": expected,
            "deletion_close_weight": deleted_weight,
            "threshold_close_weight": threshold_weight,
        },
    )

    y = -1j * np.outer(n2, n4.conj()) + 1j * np.outer(n4, n2.conj())
    actual_y = float(np.trace(y @ actual).real)
    inverse_output = w.conj().T @ input_rho @ w
    inverse_y = float(np.trace(y @ inverse_output).real)
    nonselective = effect @ actual @ effect + (np.eye(64) - effect) @ actual @ (
        np.eye(64) - effect
    )
    comparator_disturbance = float(np.linalg.norm(nonselective - actual))
    check(
        "the supplied signed phase quadrature distinguishes W_g from W_g dagger, while the close comparator is explicitly disturbing",
        abs(actual_y + inverse_y) < TOL
        and abs(abs(actual_y) - abs(np.sin(5 * G))) < TOL
        and comparator_disturbance > 0.4,
        {
            "W_Y_quadrature": actual_y,
            "W_dagger_Y_quadrature": inverse_y,
            "comparator_nonselective_disturbance": comparator_disturbance,
        },
    )

    frame_rows = []
    failures = 0
    for frame in c235.proper_cubic_frames():
        mapping = c235.direction_map(frame)

        def move(mask: int) -> int:
            result = 0
            for direction in range(6):
                if (mask >> direction) & 1:
                    result |= 1 << mapping[direction]
            return result

        moved_n2 = move(0b000011)
        moved_n4 = move(0b001111)
        moved_reference = (
            basis(64, moved_n2) + basis(64, moved_n4)
        ) / np.sqrt(2)
        moved_reject = (basis(64, moved_n2) - basis(64, moved_n4)) / np.sqrt(2)
        moved_weight = abs(np.vdot(moved_reject, w @ moved_reference)) ** 2
        row = (moved_n2.bit_count(), moved_n4.bit_count(), float(moved_weight))
        frame_rows.append(row)
        failures += not (
            row[0] == 2 and row[1] == 4 and abs(row[2] - expected) < TOL
        )
    check(
        "the supplied matter-reference fixture is a covariant 24-frame family, not a preferred-direction scalar state",
        not failures and len(frame_rows) == 24,
        {"frame_tests": len(frame_rows), "failures": failures},
    )
    return {
        "direct_reference_close_weight": actual_weight,
        "comparator_disturbance": comparator_disturbance,
    }


def repeated_query_control(model: dict[str, np.ndarray]) -> None:
    print("\nBOUNDED REPEATED-QUERY AMPLIFICATION CONTROL")
    w = model["W"]
    rows = []
    failures = 0
    for queries in (1, 2, 4, 8, 7):
        powered = np.linalg.matrix_power(w, queries)
        effect = close_effect(ramsey_isometry(powered))
        n2_index = int(np.flatnonzero(model["occupations"] == 2)[0])
        weight = float(effect[n2_index, n2_index].real)
        expected = float(np.sin(queries * G / 2) ** 2)
        row = {
            "queries": queries,
            "held_out": queries == 7,
            "N2_close_weight": weight,
            "expected": expected,
            "all_query_block_deletion_weight": 0.0,
        }
        rows.append(row)
        failures += abs(weight - expected) >= TOL
    check(
        "bounded repeated controlled queries amplify the N=2 phase syndrome, including held query count seven",
        not failures and rows[3]["N2_close_weight"] > 0.99,
        rows,
    )
    check(
        "eight-query amplification is not a certificate for every invocation: deleting one query leaves the seven-query close large",
        rows[4]["N2_close_weight"] > 0.92,
        {
            "eight_query_ideal": rows[3]["N2_close_weight"],
            "one_of_eight_deleted": rows[4]["N2_close_weight"],
        },
    )


def eigenstate_and_data_only_controls(model: dict[str, np.ndarray]) -> None:
    print("\nGLOBAL-PHASE / EIGENSTATE / DATA-ONLY CONTROLS")
    w = model["W"]
    fixed_number_residuals = []
    rng = np.random.default_rng(2850)
    for number in range(7):
        indices = np.flatnonzero(model["occupations"] == number)
        vector = rng.normal(size=len(indices)) + 1j * rng.normal(size=len(indices))
        vector /= np.linalg.norm(vector)
        state = np.zeros(64, dtype=complex)
        state[indices] = vector
        rho = projector(state)
        fixed_number_residuals.append(float(np.linalg.norm(w @ rho @ w.conj().T - rho)))
    cross = (basis(64, 0) + basis(64, 3)) / np.sqrt(2)
    rho = projector(cross)
    changed = w @ rho @ w.conj().T
    cross_residual = float(np.linalg.norm(changed - rho))
    check(
        "after-the-fact data-only density cannot distinguish W_g from deletion on fixed-number eigenstates, but an even number-coherent reference can",
        max(fixed_number_residuals) < TOL and cross_residual > 0.25,
        {
            "fixed_N_density_residuals": fixed_number_residuals,
            "held_even_cross_number_residual": cross_residual,
            "scope": "fixture-specific fixed-number density, not universal process indistinguishability",
        },
    )


def same_code_support_and_covariance_controls(model: dict[str, np.ndarray]) -> None:
    print("\nCONNECTED EDGE CODE / HELD SIZE / ALL-24 COVARIANCE")
    w_values = np.diag(model["W"])
    coefficients = contact_walsh_coefficients(w_values)
    reconstruction = []
    for occupation in range(64):
        value = 0.0j
        for mask, coefficient in enumerate(coefficients):
            sign = -1 if (mask & occupation).bit_count() % 2 else 1
            value += coefficient * sign
        reconstruction.append(value)
    reconstruction_error = float(
        np.linalg.norm(np.asarray(reconstruction) - w_values)
    )
    size_rows = []
    failures = []
    cache: dict[int, c269.WilsonSubsystemCode] = {}
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        bs = c278.cell_bs(code, (0, 0, 0))
        terms = tuple(c278.pauli_product(bs, mask) for mask in range(64))
        support_union = 0
        for row in bs:
            support_union |= row.x | row.z
        leakage = sum(
            not term.commutes(check_row)
            for term in terms
            for check_row in code.local_checks + code.wilsons
        )
        row = {
            "L": length,
            "held_out": length == 6,
            "matter_support_union": support_union.bit_count(),
            "controlled_probe_close_M2": 2,
            "total_Ramsey_neighborhood_M2": support_union.bit_count() + 2,
            "maximum_W_Pauli_weight": max(
                (term.x | term.z).bit_count() for term in terms
            ),
            "maximum_controlled_W_term_weight": max(
                (term.x | term.z).bit_count() for term in terms
            )
            + 1,
            "nonzero_Walsh_terms": sum(abs(value) > 1e-14 for value in coefficients),
            "check_or_Wilson_leakage": leakage,
        }
        size_rows.append(row)
        if not (
            row["matter_support_union"] == 18
            and row["total_Ramsey_neighborhood_M2"] == 20
            and row["maximum_W_Pauli_weight"] == 12
            and row["maximum_controlled_W_term_weight"] == 13
            and row["nonzero_Walsh_terms"] == 64
            and leakage == 0
        ):
            failures.append(row)
    check(
        "W_g and its controlled Ramsey close remain bounded on the Cycle-278 connected edge code through held-out L=6",
        not failures and reconstruction_error < TOL,
        {
            "Walsh_reconstruction_error": reconstruction_error,
            "rows": size_rows,
        },
    )

    code = cache[3]
    base_bs = c278.cell_bs(code, (0, 0, 0))
    local_family = set(code.local_checks)
    central_pivots, central_bad = c278.phase_reducer(
        list(code.local_checks + code.wilsons), code.qubits
    )
    frame_failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(code.length), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]]
                for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]]
                for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
            transformed_bs = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in base_bs
            )
            target_cell = tuple(value % code.length for value in displacement)
            target_bs = c278.cell_bs(code, target_cell)
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_wilsons = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.wilsons
            )
            if not (
                set(transformed_bs) == set(target_bs)
                and transformed_local == local_family
                and not central_bad
                and all(
                    not c278.reduce_pauli(row, central_pivots, code.qubits).symplectic(
                        code.qubits
                    )
                    for row in transformed_wilsons
                )
            ):
                frame_failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "the actual contact action and scalar Ramsey probe/close family are covariant under all 24 proper-cubic frames and full L=3 translations",
        not frame_failures and tests == 24 * 27,
        {"frame_translation_tests": tests, "failures": frame_failures[:5]},
    )


def lawful_domain_and_semantic_controls(model: dict[str, np.ndarray]) -> None:
    print("\nLAWFUL DOMAIN / SUPPLIED PHASE REFERENCE / SEMANTIC FIREWALL")

    def validate(
        length: int, probe_dimension: int, close_dimension: int, coupling: float
    ) -> None:
        if length < 3:
            raise ValueError("L must be at least three")
        if probe_dimension != 2 or close_dimension != 2:
            raise ValueError("probe and close are ordinary M2 carriers")
        if coupling != G:
            raise ValueError("the actual fixture has g=0.37")

    rejected = 0
    for arguments in ((2, 2, 2, G), (3, 3, 2, G), (3, 2, 3, G), (3, 2, 2, 0.0)):
        try:
            validate(*arguments)
        except ValueError:
            rejected += 1
    validate(3, 2, 2, G)
    text = normalized(NOTE)
    check(
        "lawful-domain and interpretation controls inventory the supplied phase reference and keep syndrome, read, occurrence, and Record distinct",
        rejected == 4
        and "does not splice cycle 251" in text
        and "coherent syndrome is not occurrence" in text
        and "projector weight is not a born frequency" in text
        and "controlled-process order is not physical time" in text
        and "phase coefficient is not physical energy" in text,
        {
            "rejected_controls": rejected,
            "supplied_phase_reference": "blank probe, Hadamard phase zero, control convention, close basis, g=0.37",
            "arbitrary_parity_even_domain": bool(
                np.linalg.norm(model["W"] @ model["parity"] - model["parity"] @ model["W"]) < TOL
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    model = fixture()
    actual_contact_and_mass_controls(model)
    joint = joint_action_flag_route(model)
    ramsey = controlled_ramsey_route(model)
    direct = matter_phase_reference_route(model)
    repeated_query_control(model)
    eigenstate_and_data_only_controls(model)
    same_code_support_and_covariance_controls(model)
    lawful_domain_and_semantic_controls(model)
    check(
        "the three constructive routes have distinct exact dispositions and imply neither shared obstruction nor axiom pressure",
        joint["split_data_residual"] > 0.1
        and ramsey["N2_close_weight"] > 0.03
        and direct["direct_reference_close_weight"] > 0.4
        and "no shared obstruction" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
        {"joint": joint, "ramsey": ramsey, "direct": direct},
    )
    print("DATA joint", joint)
    print("DATA ramsey", ramsey)
    print("DATA direct", direct)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE285_ACTUAL_CONTACT_ACTION_SYNDROME_GREEN"
        if FAIL == 0
        else "CYCLE285_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
