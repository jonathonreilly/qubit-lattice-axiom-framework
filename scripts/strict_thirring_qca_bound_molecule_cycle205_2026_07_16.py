#!/usr/bin/env python3
"""Cycle 205: strict interacting Dirac-QCA bound molecule.

Reproduce the two-particle Thirring quantum walk of Bisio et al. on a finite
ring.  A strict one-edge Dirac walk for each fermion is composed with an onsite
opposite-component interaction phase.  The runner identifies a localized
fermionic bound band, constructs a center-localized molecule from its exact
finite-ring eigenvectors, and compares total impulse rate / centre acceleration
with the independently extracted quasienergy curvature mass.

The construction is a one-dimensional candidate-law probe.  It is not a
proper-cubic lift, a selected microscopic law, or an axiom result.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "STRICT_THIRRING_QCA_BOUND_MOLECULE_CYCLE205_NOTE_2026-07-16.md"
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
        "https://arxiv.org/abs/1804.08508",
        "strict local update",
        "onsite interaction phase",
        "fermionic antisymmetry",
        "bound molecule",
        "total force",
        "curvature mass",
        "spectator record",
        "one-dimensional",
        "proper-cubic lift remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the literature and candidate-law boundaries", not missing, missing)


def basis_index(relative: int, first_internal: int, second_internal: int, length: int) -> int:
    return ((relative % length) * 2 + first_internal) * 2 + second_internal


def transition_options(internal: int, mass: float) -> tuple[tuple[int, int, complex], ...]:
    normalization = np.sqrt(1 - mass * mass)
    shift = -1 if internal == 0 else 1
    return (
        (internal, shift, complex(normalization)),
        (1 - internal, 0, -1j * mass),
    )


def thirring_block(
    length: int,
    total_momentum: float,
    mass: float,
    coupling: float,
    *,
    interaction_first: bool = True,
) -> np.ndarray:
    dimension = 4 * length
    free = np.zeros((dimension, dimension), dtype=complex)
    interaction = np.ones(dimension, dtype=complex)
    for relative in range(length):
        for first_internal in range(2):
            for second_internal in range(2):
                column = basis_index(relative, first_internal, second_internal, length)
                if relative == 0 and first_internal != second_internal:
                    interaction[column] = np.exp(1j * coupling)
                for next_first, first_shift, first_weight in transition_options(first_internal, mass):
                    for next_second, second_shift, second_weight in transition_options(second_internal, mass):
                        row = basis_index(
                            relative + first_shift - second_shift,
                            next_first,
                            next_second,
                            length,
                        )
                        free[row, column] += (
                            first_weight
                            * second_weight
                            * np.exp(-1j * total_momentum * second_shift)
                        )
    if interaction_first:
        return free * interaction[None, :]
    return interaction[:, None] * free


def exchange_relative(vector: np.ndarray, total_momentum: float) -> np.ndarray:
    length = vector.shape[0]
    signed_relative = (
        np.arange(length) + length // 2
    ) % length - length // 2
    exchanged = np.empty_like(vector)
    for relative in range(length):
        for first_internal in range(2):
            for second_internal in range(2):
                exchanged[relative, first_internal, second_internal] = vector[
                    (-relative) % length, second_internal, first_internal
                ] * np.exp(1j * total_momentum * signed_relative[relative])
    return exchanged


@dataclass(frozen=True)
class BoundEigenpair:
    phase: float
    vector: np.ndarray
    close_probability: float
    relative_variance: float
    antisymmetry_residual: float


@lru_cache(maxsize=None)
def bound_eigenpair(
    length: int, total_momentum_key: float, mass: float, coupling: float
) -> BoundEigenpair:
    total_momentum = float(total_momentum_key)
    block = thirring_block(length, total_momentum, mass, coupling)
    eigenvalues, eigenvectors = np.linalg.eig(block)
    phases = np.angle(eigenvalues)
    reshaped = eigenvectors.reshape(length, 2, 2, -1)
    relative_probabilities = np.sum(np.abs(reshaped) ** 2, axis=(1, 2))
    signed_relative = (
        np.arange(length) + length // 2
    ) % length - length // 2
    close_mask = np.abs(signed_relative) <= 2
    close = np.sum(relative_probabilities[close_mask], axis=0)
    residuals = np.asarray(
        [
            np.linalg.norm(
                exchange_relative(reshaped[..., index], total_momentum)
                + reshaped[..., index]
            )
            for index in range(eigenvectors.shape[1])
        ]
    )
    candidates = np.where(
        (phases > 0.02) & (phases < 2.5) & (residuals < 2e-8)
    )[0]
    if not len(candidates):
        raise RuntimeError("No localized positive-phase fermionic branch found")
    chosen = int(candidates[np.argmax(close[candidates])])
    probability = relative_probabilities[:, chosen]
    return BoundEigenpair(
        phase=float(phases[chosen]),
        vector=reshaped[..., chosen],
        close_probability=float(close[chosen]),
        relative_variance=float(np.sum(probability * signed_relative**2).real),
        antisymmetry_residual=float(residuals[chosen]),
    )


def phase_curvature_mass(
    length: int, mass: float, coupling: float
) -> tuple[float, float, float]:
    # A periodic finite ring admits only total momenta 2 pi n / L.  Using the
    # first nonzero momentum keeps the curvature test inside the literal
    # finite model instead of silently imposing a twisted boundary.
    step = 2 * np.pi / length
    rest = bound_eigenpair(length, 0.0, mass, coupling).phase
    plus = bound_eigenpair(length, float(step), mass, coupling).phase
    minus = bound_eigenpair(length, float(-step), mass, coupling).phase
    curvature = (plus - 2 * rest + minus) / step**2
    return rest, float(curvature), float(1 / curvature)


def extrapolated_curvature_mass(
    first_length: int, second_length: int, mass: float, coupling: float
) -> tuple[float, float]:
    """Remove the leading O((2 pi/L)^2) finite-difference error."""
    first_curvature = phase_curvature_mass(first_length, mass, coupling)[1]
    second_curvature = phase_curvature_mass(second_length, mass, coupling)[1]
    extrapolated = (
        second_length**2 * second_curvature
        - first_length**2 * first_curvature
    ) / (second_length**2 - first_length**2)
    return float(extrapolated), float(1 / extrapolated)


def apply_real_step(
    state: np.ndarray,
    mass: float,
    coupling: float,
    *,
    interaction_first: bool = True,
) -> np.ndarray:
    length = state.shape[0]
    diagonal = np.eye(length, dtype=bool)

    def interaction(packet: np.ndarray) -> np.ndarray:
        packet = packet.copy()
        packet[diagonal, 0, 1] *= np.exp(1j * coupling)
        packet[diagonal, 1, 0] *= np.exp(1j * coupling)
        return packet

    def free(packet: np.ndarray) -> np.ndarray:
        normalization = np.sqrt(1 - mass * mass)
        first = np.empty_like(packet)
        first[:, :, 0, :] = (
            normalization * np.roll(packet[:, :, 0, :], -1, axis=0)
            - 1j * mass * packet[:, :, 1, :]
        )
        first[:, :, 1, :] = (
            -1j * mass * packet[:, :, 0, :]
            + normalization * np.roll(packet[:, :, 1, :], 1, axis=0)
        )
        second = np.empty_like(first)
        second[:, :, :, 0] = (
            normalization * np.roll(first[:, :, :, 0], -1, axis=1)
            - 1j * mass * first[:, :, :, 1]
        )
        second[:, :, :, 1] = (
            -1j * mass * first[:, :, :, 0]
            + normalization * np.roll(first[:, :, :, 1], 1, axis=1)
        )
        return second

    return free(interaction(state)) if interaction_first else interaction(free(state))


def relative_to_full(vector: np.ndarray, total_momentum: float) -> np.ndarray:
    length = vector.shape[0]
    full = np.zeros((length, length, 2, 2), dtype=complex)
    for second_position in range(length):
        phase = np.exp(1j * total_momentum * second_position) / np.sqrt(length)
        for relative in range(length):
            first_position = (second_position + relative) % length
            full[first_position, second_position] = phase * vector[relative]
    return full


def full_to_relative(state: np.ndarray, total_momentum: float) -> np.ndarray:
    length = state.shape[0]
    vector = np.zeros((length, 2, 2), dtype=complex)
    for second_position in range(length):
        phase = np.exp(-1j * total_momentum * second_position) / np.sqrt(length)
        for relative in range(length):
            first_position = (second_position + relative) % length
            vector[relative] += phase * state[first_position, second_position]
    return vector


def local_block_and_schedule_controls() -> None:
    length = 24
    mass = 0.6
    coupling = 0.2 * np.pi
    momentum = 2 * np.pi / length
    block = thirring_block(length, momentum, mass, coupling)
    check(
        "finite total-momentum block is exactly unitary to numerical precision",
        np.linalg.norm(block.conj().T @ block - np.eye(4 * length)) < 2e-12,
    )

    rng = np.random.default_rng(205)
    relative = rng.normal(size=(length, 2, 2)) + 1j * rng.normal(size=(length, 2, 2))
    relative /= np.linalg.norm(relative)
    full = relative_to_full(relative, momentum)
    real_result = apply_real_step(full, mass, coupling)
    block_result = (block @ relative.reshape(-1)).reshape(length, 2, 2)
    recovered = full_to_relative(real_result, momentum)
    check(
        "literal real-space update agrees with the fixed-total-momentum block",
        np.allclose(recovered, block_result, atol=2e-12),
        np.linalg.norm(recovered - block_result),
    )

    delta = np.zeros((length, length, 2, 2), dtype=complex)
    centre = length // 2
    delta[centre, centre, 0, 1] = 1
    evolved = apply_real_step(delta, mass, coupling)
    occupied = np.argwhere(np.sum(np.abs(evolved) ** 2, axis=(2, 3)) > 1e-14)
    check(
        "strict local update moves each constituent by at most one edge",
        all(
            abs(int(first) - centre) <= 1 and abs(int(second) - centre) <= 1
            for first, second in occupied
        ),
        occupied.tolist(),
    )

    walk_then_interaction = thirring_block(
        length, momentum, mass, coupling, interaction_first=False
    )
    first_spectrum = np.linalg.eigvals(block)
    second_spectrum = np.linalg.eigvals(walk_then_interaction)
    spectral_distance = max(
        max(min(abs(value - other) for other in second_spectrum) for value in first_spectrum),
        max(min(abs(value - other) for other in first_spectrum) for value in second_spectrum),
    )
    check(
        "cyclic interaction/walk ordering preserves the finite spectrum",
        spectral_distance < 2e-11,
        spectral_distance,
    )


def bound_band_tournament() -> None:
    reference = []
    for length in (32, 48, 64):
        pair = bound_eigenpair(length, 0.0, 0.6, 0.2 * np.pi)
        rest, curvature, inertia = phase_curvature_mass(length, 0.6, 0.2 * np.pi)
        reference.append((rest, curvature, inertia, pair.close_probability))
    first_extrapolated = extrapolated_curvature_mass(32, 48, 0.6, 0.2 * np.pi)
    second_extrapolated = extrapolated_curvature_mass(48, 64, 0.6, 0.2 * np.pi)
    check(
        "bound branch rest phase and O(1/L^2)-extrapolated curvature converge",
        abs(reference[-1][0] - reference[-2][0]) < 2e-12
        and abs(second_extrapolated[0] / first_extrapolated[0] - 1) < 2e-3,
        {
            "finite_ring": reference,
            "extrapolated_32_48": first_extrapolated,
            "extrapolated_48_64": second_extrapolated,
        },
    )

    for mass, coupling in (
        (0.3, 0.1 * np.pi),
        (0.3, 0.35 * np.pi),
        (0.6, 0.2 * np.pi),
        (0.6, 0.5 * np.pi),
        (0.85, 0.1 * np.pi),
        (0.85, 0.35 * np.pi),
    ):
        pair = bound_eigenpair(48, 0.0, mass, coupling)
        rest, curvature, inertia = phase_curvature_mass(48, mass, coupling)
        check(
            f"m={mass}, chi/pi={coupling / np.pi:.2f} has a localized fermionic bound band",
            pair.close_probability > 0.7
            and pair.antisymmetry_residual < 2e-8
            and curvature > 0
            and inertia > 0,
            {
                "rest_phase": rest,
                "curvature_mass": inertia,
                "close_probability": pair.close_probability,
            },
        )


def prepare_bound_packet(
    length: int,
    mass: float,
    coupling: float,
    momentum_width: float,
) -> np.ndarray:
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    coefficients = np.zeros((length, length, 2, 2), dtype=complex)
    reference = bound_eigenpair(length, 0.0, mass, coupling).vector
    for index, momentum in enumerate(momenta):
        envelope = np.exp(-0.5 * (momentum / momentum_width) ** 2)
        if envelope < 1e-12:
            continue
        vector = bound_eigenpair(
            length, float(momentum), mass, coupling
        ).vector.copy()
        overlap = np.vdot(reference, vector)
        vector *= np.exp(-1j * np.angle(overlap))
        coefficients[index] = envelope * vector
    coefficients /= np.linalg.norm(coefficients)
    centre_relative = np.fft.ifft(coefficients, axis=0, norm="ortho")
    state = np.zeros_like(centre_relative)
    for second_position in range(length):
        for relative in range(length):
            first_position = (second_position + relative) % length
            state[first_position, second_position] = centre_relative[
                second_position, relative
            ]
    state = np.roll(np.roll(state, length // 2, axis=0), length // 2, axis=1)
    return state


def pair_observables(state: np.ndarray) -> dict[str, float]:
    length = state.shape[0]
    positions = np.arange(length, dtype=float) - length // 2
    first, second = np.meshgrid(positions, positions, indexing="ij")
    centre = (first + second) / 2
    indices = np.arange(length)
    relative = (indices[:, None] - indices[None, :] + length // 2) % length - length // 2
    probability = np.sum(np.abs(state) ** 2, axis=(2, 3))
    mean = float(np.sum(probability * centre).real)
    return {
        "centre": mean,
        "centre_variance": float(np.sum(probability * (centre - mean) ** 2).real),
        "relative_variance": float(np.sum(probability * relative**2).real),
        "close_probability": float(np.sum(probability[np.abs(relative) <= 2]).real),
        "boundary_probability": float(
            np.sum(
                probability[
                    (np.abs(first) > length / 4) | (np.abs(second) > length / 4)
                ]
            ).real
        ),
    }


def exchange_full(state: np.ndarray) -> np.ndarray:
    return -np.transpose(state, (1, 0, 3, 2))


def forced_step(
    state: np.ndarray,
    mass: float,
    coupling: float,
    force_per_constituent: float,
) -> np.ndarray:
    length = state.shape[0]
    positions = np.arange(length, dtype=float) - length // 2
    first, second = np.meshgrid(positions, positions, indexing="ij")
    half_kick = np.exp(
        0.5j * force_per_constituent * (first + second)
    )[:, :, None, None]
    return half_kick * apply_real_step(
        half_kick * state, mass, coupling
    )


def forced_molecule_response() -> None:
    length = 128
    mass = 0.6
    coupling = 0.2 * np.pi
    force_per_constituent = 1e-4
    duration = 40
    state = prepare_bound_packet(length, mass, coupling, 0.07)
    initial = pair_observables(state)
    check(
        "prepared molecular packet has exact fermionic antisymmetry",
        np.linalg.norm(state - exchange_full(state)) < 2e-10,
        np.linalg.norm(state - exchange_full(state)),
    )

    times = [0.0]
    centres = [initial["centre"]]
    for step in range(duration):
        state = forced_step(state, mass, coupling, force_per_constituent)
        times.append(float(step + 1))
        centres.append(pair_observables(state)["centre"])
    acceleration = float(
        2 * np.polyfit(np.asarray(times), np.asarray(centres) - centres[0], 2)[0]
    )
    measured_mass = abs(2 * force_per_constituent / acceleration)
    rest = bound_eigenpair(64, 0.0, mass, coupling).phase
    curvature, expected_mass = extrapolated_curvature_mass(48, 64, mass, coupling)
    final = pair_observables(state)
    check(
        "strict molecule total-force/centre-acceleration recovers curvature mass",
        abs(measured_mass / expected_mass - 1) < 8e-3,
        {
            "measured": measured_mass,
            "expected": expected_mass,
            "rest_phase": rest,
            "curvature": curvature,
        },
    )
    check(
        "forced molecule remains internally bound and normalized",
        abs(final["close_probability"] - initial["close_probability"]) < 2e-3
        and abs(final["relative_variance"] - initial["relative_variance"]) < 2e-2
        and abs(np.linalg.norm(state) - 1) < 2e-10,
        {"initial": initial, "final": final, "norm": np.linalg.norm(state)},
    )
    check(
        "forced molecule remains isolated from the periodic boundary comparator",
        final["boundary_probability"] < 5e-3,
        final["boundary_probability"],
    )

    no_force = prepare_bound_packet(length, mass, coupling, 0.07)
    no_force_centres = [pair_observables(no_force)["centre"]]
    for _ in range(duration):
        no_force = forced_step(no_force, mass, coupling, 0.0)
        no_force_centres.append(pair_observables(no_force)["centre"])
    zero_acceleration = float(
        2
        * np.polyfit(
            np.arange(duration + 1, dtype=float),
            np.asarray(no_force_centres) - no_force_centres[0],
            2,
        )[0]
    )
    check(
        "force deletion removes molecular acceleration",
        abs(zero_acceleration) < 2e-8,
        zero_acceleration,
    )

    interaction_deleted = prepare_bound_packet(length, mass, coupling, 0.07)
    deleted_initial = pair_observables(interaction_deleted)
    for _ in range(duration):
        interaction_deleted = forced_step(interaction_deleted, mass, 0.0, 0.0)
    deleted_final = pair_observables(interaction_deleted)
    check(
        "interaction deletion substantially broadens the selected molecule",
        deleted_final["close_probability"] < deleted_initial["close_probability"] - 0.1
        and deleted_final["relative_variance"] > 50 * deleted_initial["relative_variance"],
        {"initial": deleted_initial, "final": deleted_final},
    )

    record_zero = np.array([1, 0], dtype=complex)
    record_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    one_record = state[..., None] * record_zero[None, None, None, None, :]
    two_records = (
        state[..., None, None]
        * record_zero[None, None, None, None, :, None]
        * record_plus[None, None, None, None, None, :]
    )
    check(
        "one or two spectator records do not change molecule probability",
        np.allclose(np.sum(np.abs(one_record) ** 2, axis=-1), np.abs(state) ** 2, atol=2e-12)
        and np.allclose(np.sum(np.abs(two_records) ** 2, axis=(-2, -1)), np.abs(state) ** 2, atol=2e-12),
    )


def complex_phase_control() -> None:
    mass = 0.6
    coupling = 0.2 * np.pi
    check(
        "mass mixing and onsite interaction use generic complex non-Clifford phases",
        min(abs(np.arcsin(mass) - index * np.pi / 4) for index in range(-4, 5)) > 1e-3
        and min(abs(coupling - index * np.pi / 4) for index in range(-4, 5)) > 1e-3,
        {"mixing/pi": np.arcsin(mass) / np.pi, "coupling/pi": coupling / np.pi},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    local_block_and_schedule_controls()
    bound_band_tournament()
    forced_molecule_response()
    complex_phase_control()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "STRICT_QCA_BOUND_MOLECULE" if FAIL == 0 else "CYCLE205_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
