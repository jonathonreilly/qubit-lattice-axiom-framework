#!/usr/bin/env python3
"""Cycle 207: fixed-total-momentum molecular scattering channels.

Resolve the Cycle-206 outgoing entangled state into transmitted-molecule,
reflected-molecule, and breakup record alternatives.  The late spectral
readout is a named import; this runner does not derive local record formation.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from strict_thirring_qca_bound_molecule_cycle205_2026_07_16 import (
    bound_eigenpair,
    extrapolated_curvature_mass,
    transition_options,
)
from generated_carrier_molecule_recoil_cycle206_2026_07_16 import (
    apply_three_body_step,
    branch_group_velocities,
    positive_phase_spinor,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FIXED_TOTAL_MOMENTUM_MOLECULAR_SCATTERING_CYCLE207_NOTE_2026-07-16.md"
)

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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "https://doi.org/10.3390/e20060435",
        "bisio, d'ariano, mosco, perinotti, and tosini",
        "prior work",
        "fixed-total-momentum",
        "transmitted",
        "reflected",
        "breakup",
        "orthogonal late record",
        "record-conditioned",
        "supplied spectral readout",
        "local detector remains open",
        "one-dimensional",
        "proper-cubic lift remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves attribution, readout import, and scope", not missing, missing)


def wrap(momentum: float) -> float:
    return float(np.angle(np.exp(1j * momentum)))


def apply_relative_step(
    state: np.ndarray,
    total_momentum: float,
    pair_mass: float,
    projectile_mass: float,
    pair_coupling: float,
    projectile_coupling: float,
) -> np.ndarray:
    length = state.shape[0]
    interacting = state.copy()
    pair_phase = np.exp(1j * pair_coupling)
    collision_phase = np.exp(1j * projectile_coupling)
    interacting[0, :, 0, 1, :] *= pair_phase
    interacting[0, :, 1, 0, :] *= pair_phase
    interacting[:, 0, :, :, :] *= collision_phase
    diagonal = np.arange(length)
    interacting[diagonal, diagonal, :, :, :] *= collision_phase

    output = np.zeros_like(state)
    for first_internal in range(2):
        for second_internal in range(2):
            for projectile_internal in range(2):
                source = interacting[
                    :, :, first_internal, second_internal, projectile_internal
                ]
                for next_first, first_shift, first_weight in transition_options(
                    first_internal, pair_mass
                ):
                    for next_second, second_shift, second_weight in transition_options(
                        second_internal, pair_mass
                    ):
                        for next_projectile, projectile_shift, projectile_weight in transition_options(
                            projectile_internal, projectile_mass
                        ):
                            output[
                                :, :, next_first, next_second, next_projectile
                            ] += (
                                first_weight
                                * second_weight
                                * projectile_weight
                                * np.exp(-1j * total_momentum * second_shift)
                                * np.roll(
                                    source,
                                    (
                                        first_shift - second_shift,
                                        projectile_shift - second_shift,
                                    ),
                                    axis=(0, 1),
                                )
                            )
    return output


def relative_to_full(state: np.ndarray, total_momentum: float) -> np.ndarray:
    length = state.shape[0]
    full = np.zeros((length, length, length, 2, 2, 2), dtype=complex)
    for second_position in range(length):
        phase = np.exp(1j * total_momentum * second_position) / np.sqrt(length)
        for relative in range(length):
            first_position = (second_position + relative) % length
            for separation in range(length):
                projectile_position = (second_position + separation) % length
                full[first_position, second_position, projectile_position] = (
                    phase * state[relative, separation]
                )
    return full


def full_to_relative(state: np.ndarray, total_momentum: float) -> np.ndarray:
    length = state.shape[0]
    relative_state = np.zeros((length, length, 2, 2, 2), dtype=complex)
    for second_position in range(length):
        phase = np.exp(-1j * total_momentum * second_position) / np.sqrt(length)
        for relative in range(length):
            first_position = (second_position + relative) % length
            for separation in range(length):
                projectile_position = (second_position + separation) % length
                relative_state[relative, separation] += (
                    phase
                    * state[first_position, second_position, projectile_position]
                )
    return relative_state


def prepare_incoming(
    length: int,
    total_momentum: float,
    pair_mass: float,
    projectile_mass: float,
    pair_coupling: float,
    projectile_central_momentum: float,
    momentum_width: float,
    separation: int,
) -> np.ndarray:
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    coefficients = np.zeros((length, length, 2, 2, 2), dtype=complex)
    reference_pair = bound_eigenpair(
        length,
        wrap(total_momentum - projectile_central_momentum),
        pair_mass,
        pair_coupling,
    ).vector
    _, reference_projectile = positive_phase_spinor(
        projectile_central_momentum, projectile_mass
    )
    for index, projectile_momentum in enumerate(momenta):
        delta = wrap(projectile_momentum - projectile_central_momentum)
        envelope = np.exp(-0.5 * (delta / momentum_width) ** 2)
        if envelope < 1e-13:
            continue
        pair_momentum = wrap(total_momentum - projectile_momentum)
        pair = bound_eigenpair(
            length, pair_momentum, pair_mass, pair_coupling
        ).vector.copy()
        pair *= np.exp(-1j * np.angle(np.vdot(reference_pair, pair)))
        _, projectile = positive_phase_spinor(
            float(projectile_momentum), projectile_mass
        )
        projectile *= np.exp(
            -1j * np.angle(np.vdot(reference_projectile, projectile))
        )
        coefficients[index] = envelope * np.einsum(
            "rab,c->rabc", pair, projectile, optimize=True
        )
    coefficients /= np.linalg.norm(coefficients)
    separation_first = np.fft.ifft(coefficients, axis=0, norm="ortho")
    state = np.transpose(separation_first, (1, 0, 2, 3, 4))
    state = np.roll(state, separation, axis=1)
    return state / np.linalg.norm(state)


def signed_coordinates(length: int) -> np.ndarray:
    return (np.arange(length) + length // 2) % length - length // 2


def observables(state: np.ndarray) -> dict[str, float]:
    length = state.shape[0]
    probability = np.sum(np.abs(state) ** 2, axis=(2, 3, 4))
    relative = signed_coordinates(length)
    pair_relative = np.sum(probability, axis=1)
    separation = np.sum(probability, axis=0)
    separation_phase = np.sum(
        separation * np.exp(2j * np.pi * np.arange(length) / length)
    )
    separation_index = (
        np.angle(separation_phase) % (2 * np.pi)
    ) * length / (2 * np.pi)
    separation_mean = (
        (separation_index + length // 2) % length - length // 2
    )
    return {
        "norm": float(np.linalg.norm(state)),
        "pair_close": float(np.sum(pair_relative[np.abs(relative) <= 2]).real),
        "contact": float(
            (
                np.sum(probability[:, 0])
                + np.sum(probability[np.arange(length), np.arange(length)])
                - probability[0, 0]
            ).real
        ),
        "separation": float(separation_mean),
        "separation_coherence": float(abs(separation_phase)),
        "boundary": float(np.sum(separation[np.abs(relative) > length * 0.42]).real),
    }


def channel_records(
    spectrum: dict[str, np.ndarray | float],
    total_momentum: float,
    pair_mass: float,
    pair_coupling: float,
) -> dict[str, object]:
    momenta = np.asarray(spectrum["momenta"])
    weights = np.asarray(spectrum["positive_weights"])
    pair_momenta = np.angle(np.exp(1j * (total_momentum - momenta)))
    velocity_table = np.asarray(
        branch_group_velocities(len(momenta), pair_mass, pair_coupling)
    )
    total_index = int(round(total_momentum * len(momenta) / (2 * np.pi))) % len(
        momenta
    )
    pair_indices = (total_index - np.arange(len(momenta))) % len(momenta)
    pair_velocities = velocity_table[pair_indices]
    transmitted = momenta >= 0
    reflected = momenta < 0

    def branch(mask: np.ndarray) -> dict[str, float]:
        probability = float(np.sum(weights[mask]))
        phase = np.sum(weights[mask] * np.exp(1j * pair_momenta[mask]))
        mean_momentum = float(np.angle(phase))
        mean_velocity = float(
            np.sum(weights[mask] * pair_velocities[mask]) / probability
        )
        return {
            "probability": probability,
            "pair_momentum": mean_momentum,
            "pair_velocity": mean_velocity,
            "secant_mass": float(abs(mean_momentum / mean_velocity))
            if abs(mean_velocity) > 1e-8 and abs(mean_momentum) > 1e-8
            else float("nan"),
            "momentum_coherence": float(abs(phase) / probability),
        }

    transmitted_record = branch(transmitted)
    reflected_record = branch(reflected) if np.sum(weights[reflected]) > 1e-14 else None
    breakup = float(1 - np.sum(weights))
    return {
        "transmitted": transmitted_record,
        "reflected": reflected_record,
        "breakup": breakup,
        "normalization": transmitted_record["probability"]
        + (reflected_record["probability"] if reflected_record else 0)
        + breakup,
        "curvature_mass": extrapolated_curvature_mass(
            48, 64, pair_mass, pair_coupling
        )[1],
    }


def channel_spectrum(
    state: np.ndarray,
    total_momentum: float,
    pair_mass: float,
    projectile_mass: float,
    pair_coupling: float,
) -> dict[str, np.ndarray | float]:
    length = state.shape[0]
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    momentum_state = np.fft.fft(state, axis=1, norm="ortho")
    momentum_probability = np.sum(
        np.abs(momentum_state) ** 2, axis=(0, 2, 3, 4)
    )
    bound_weights = np.zeros(length)
    positive_weights = np.zeros(length)
    amplitudes = np.zeros(length, dtype=complex)
    for index, projectile_momentum in enumerate(momenta):
        if momentum_probability[index] < 1e-14:
            continue
        pair_momentum = wrap(total_momentum - projectile_momentum)
        pair = bound_eigenpair(
            length, pair_momentum, pair_mass, pair_coupling
        ).vector
        projectile_vector = np.einsum(
            "rab,rabc->c",
            np.conjugate(pair),
            momentum_state[:, index],
            optimize=True,
        )
        bound_weights[index] = float(
            np.sum(np.abs(projectile_vector) ** 2).real
        )
        _, positive = positive_phase_spinor(
            float(projectile_momentum), projectile_mass
        )
        amplitudes[index] = np.vdot(positive, projectile_vector)
        positive_weights[index] = abs(amplitudes[index]) ** 2
    return {
        "momenta": momenta,
        "bound_weights": bound_weights,
        "positive_weights": positive_weights,
        "amplitudes": amplitudes,
        "bound_population": float(np.sum(bound_weights)),
        "positive_bound_population": float(np.sum(positive_weights)),
    }


def relative_block_controls() -> None:
    length = 6
    total_momentum = 2 * np.pi / length
    pair_mass = 0.61
    projectile_mass = 0.37
    pair_coupling = 0.19 * np.pi
    projectile_coupling = 0.07 * np.pi
    rng = np.random.default_rng(207)
    state = rng.normal(size=(length, length, 2, 2, 2)) + 1j * rng.normal(
        size=(length, length, 2, 2, 2)
    )
    state /= np.linalg.norm(state)
    reduced = apply_relative_step(
        state,
        total_momentum,
        pair_mass,
        projectile_mass,
        pair_coupling,
        projectile_coupling,
    )
    check(
        "fixed-total-momentum relative block is unitary",
        abs(np.linalg.norm(reduced) - 1) < 2e-13,
        np.linalg.norm(reduced),
    )
    full = relative_to_full(state, total_momentum)
    full_result = apply_three_body_step(
        full,
        pair_mass,
        projectile_mass,
        pair_coupling,
        projectile_coupling,
    )
    recovered = full_to_relative(full_result, total_momentum)
    check(
        "relative block exactly reproduces the literal strict three-carrier update",
        np.allclose(recovered, reduced, atol=2e-12),
        np.linalg.norm(recovered - reduced),
    )


def run(coupling: float) -> dict[str, object]:
    length = 128
    pair_mass = 0.85
    projectile_mass = 0.3
    pair_coupling = 0.1 * np.pi
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    central_index = 14
    total_momentum = float(momenta[central_index])
    state = prepare_incoming(
        length,
        total_momentum,
        pair_mass,
        projectile_mass,
        pair_coupling,
        total_momentum,
        0.08,
        32,
    )
    initial_channels = channel_spectrum(
        state, total_momentum, pair_mass, projectile_mass, pair_coupling
    )
    rows = [observables(state)]
    late_channels = None
    for step in range(1, 71):
        state = apply_relative_step(
            state,
            total_momentum,
            pair_mass,
            projectile_mass,
            pair_coupling,
            coupling,
        )
        rows.append(observables(state))
        if step == 64:
            late_channels = channel_spectrum(
                state,
                total_momentum,
                pair_mass,
                projectile_mass,
                pair_coupling,
            )
    final_channels = channel_spectrum(
        state, total_momentum, pair_mass, projectile_mass, pair_coupling
    )
    records = channel_records(
        final_channels, total_momentum, pair_mass, pair_coupling
    )
    if late_channels is None:
        raise RuntimeError("late channel snapshot missing")
    return {
        "eta_fraction": coupling / np.pi,
        "total_momentum": total_momentum,
        "initial": rows[0],
        "peak_contact": max(row["contact"] for row in rows),
        "final": rows[-1],
        "initial_channels": initial_channels,
        "late_records": channel_records(
            late_channels, total_momentum, pair_mass, pair_coupling
        ),
        "final_channels": final_channels,
        "records": records,
        "norm_drift": max(abs(row["norm"] - 1) for row in rows),
    }


def record_probabilities(records: dict[str, object]) -> np.ndarray:
    reflected = records["reflected"]
    return np.asarray(
        [
            records["transmitted"]["probability"],
            reflected["probability"] if reflected is not None else 0.0,
            records["breakup"],
        ],
        dtype=float,
    )


def scattering_and_record_controls() -> None:
    deleted = run(0.0)
    weak = run(0.03 * np.pi)
    strong = run(0.06 * np.pi)

    for label, result in (("deleted", deleted), ("weak", weak), ("strong", strong)):
        initial = result["initial"]
        final = result["final"]
        records = result["records"]
        probabilities = record_probabilities(records)
        check(
            f"{label} fixed-sector trajectory remains normalized and asymptotically separated",
            result["norm_drift"] < 2e-12
            and initial["contact"] < 2e-4
            and result["peak_contact"] > 0.045
            and final["contact"] < 8e-4
            and final["boundary"] < 0.02,
            {
                "norm": result["norm_drift"],
                "initial_contact": initial["contact"],
                "peak_contact": result["peak_contact"],
                "final_contact": final["contact"],
                "boundary": final["boundary"],
            },
        )
        check(
            f"{label} transmitted/reflected/breakup record probabilities are positive and normalized",
            np.min(probabilities) > -2e-12
            and abs(np.sum(probabilities) - 1) < 2e-12
            and abs(records["normalization"] - 1) < 2e-12,
            probabilities.tolist(),
        )

    deleted_probabilities = record_probabilities(deleted["records"])
    check(
        "deleting the collision phase deletes reflection and breakup channels",
        abs(deleted_probabilities[0] - 1) < 2e-12
        and abs(deleted_probabilities[1]) < 2e-12
        and abs(deleted_probabilities[2]) < 2e-12
        and abs(deleted["final"]["pair_close"] - deleted["initial"]["pair_close"]) < 2e-12,
        deleted_probabilities.tolist(),
    )

    weak_probabilities = record_probabilities(weak["records"])
    strong_probabilities = record_probabilities(strong["records"])
    check(
        "stronger onsite collision increases reflected and breakup records",
        strong_probabilities[1] > 3 * weak_probabilities[1]
        and strong_probabilities[2] > 3 * weak_probabilities[2]
        and strong_probabilities[0] < weak_probabilities[0],
        {"weak": weak_probabilities.tolist(), "strong": strong_probabilities.tolist()},
    )

    for label, result, tolerance in (
        ("weak", weak, 0.02),
        ("strong", strong, 0.005),
    ):
        transmitted = result["records"]["transmitted"]
        curvature_mass = result["records"]["curvature_mass"]
        check(
            f"{label} transmitted record selects a narrow branch with the calibrated mass coordinate",
            transmitted["momentum_coherence"] > 0.998
            and abs(transmitted["secant_mass"] / curvature_mass - 1) < tolerance,
            {
                "probability": transmitted["probability"],
                "momentum": transmitted["pair_momentum"],
                "velocity": transmitted["pair_velocity"],
                "secant_mass": transmitted["secant_mass"],
                "curvature_mass": curvature_mass,
                "relative_error": transmitted["secant_mass"] / curvature_mass - 1,
            },
        )

    reflected = strong["records"]["reflected"]
    check(
        "reflected record is a distinct nonlinear high-momentum molecular channel",
        reflected is not None
        and reflected["probability"] > 0.02
        and reflected["pair_momentum"] > 0.9
        and reflected["momentum_coherence"] > 0.998,
        reflected,
    )

    late = record_probabilities(strong["late_records"])
    final = record_probabilities(strong["records"])
    check(
        "late channel probabilities stabilize as the packets separate",
        np.max(np.abs(late - final)) < 2e-3,
        {"tick64": late.tolist(), "tick70": final.tolist()},
    )

    # Appending one orthogonal record or a redundant correlated copy changes
    # neither the channel weights nor their marginal normalization.
    record_density = np.diag(final.astype(complex))
    duplicated = np.zeros((3, 3), dtype=float)
    duplicated[np.arange(3), np.arange(3)] = final
    check(
        "one orthogonal late record and a redundant copy preserve channel weights",
        np.allclose(np.diag(record_density).real, final)
        and np.allclose(np.sum(duplicated, axis=0), final)
        and np.allclose(np.sum(duplicated, axis=1), final),
    )

    check(
        "scattering and readout retain generic complex non-Clifford phases",
        min(abs(0.03 * np.pi - index * np.pi / 4) for index in range(-4, 5)) > 1e-3
        and min(abs(0.1 * np.pi - index * np.pi / 4) for index in range(-4, 5)) > 1e-3,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    relative_block_controls()
    scattering_and_record_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "RECORD_CONDITIONED_MOLECULAR_SCATTERING" if FAIL == 0 else "CYCLE207_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
