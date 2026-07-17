#!/usr/bin/env python3
"""Cycle 206: generated carrier/molecule recoil under one strict QCA.

Extend the Cycle-205 Thirring molecule by a distinguishable third Dirac
carrier.  All three walkers receive strict one-edge updates.  The projectile
acquires an onsite phase when it meets either molecule constituent, replacing
the externally imposed force profile by local momentum exchange.

The collision runner tests strict locality, covariance, conserved total
translation charge, molecular-band survival, interaction deletion, finite-ring
stability, and the distinction between generated recoil and a single-channel
inertial-mass fit.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np

from strict_thirring_qca_bound_molecule_cycle205_2026_07_16 import (
    bound_eigenpair,
    prepare_bound_packet,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "GENERATED_CARRIER_MOLECULE_RECOIL_CYCLE206_NOTE_2026-07-16.md"
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
        "prior work",
        "distinguishable third carrier",
        "onsite collision phase",
        "generated recoil",
        "total translation charge",
        "molecular-band population",
        "outgoing entangled mixture",
        "record-conditioned scattering branch",
        "one-dimensional",
        "proper-cubic lift remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves attribution and candidate-law scope", not missing, missing)


def single_walk_block(momentum: float, mass: float) -> np.ndarray:
    normalization = np.sqrt(1 - mass * mass)
    return np.asarray(
        [
            [normalization * np.exp(1j * momentum), -1j * mass],
            [-1j * mass, normalization * np.exp(-1j * momentum)],
        ],
        dtype=complex,
    )


def positive_phase_spinor(momentum: float, mass: float) -> tuple[float, np.ndarray]:
    values, vectors = np.linalg.eig(single_walk_block(momentum, mass))
    phases = np.angle(values)
    chosen = int(np.argmax(phases))
    vector = vectors[:, chosen]
    return float(phases[chosen]), vector / np.linalg.norm(vector)


def prepare_projectile(
    length: int,
    mass: float,
    centre: int,
    central_momentum: float,
    momentum_width: float,
) -> np.ndarray:
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    coefficients = np.zeros((length, 2), dtype=complex)
    _, reference = positive_phase_spinor(central_momentum, mass)
    for index, momentum in enumerate(momenta):
        delta = np.angle(np.exp(1j * (momentum - central_momentum)))
        envelope = np.exp(-0.5 * (delta / momentum_width) ** 2)
        _, spinor = positive_phase_spinor(float(momentum), mass)
        spinor *= np.exp(-1j * np.angle(np.vdot(reference, spinor)))
        coefficients[index] = envelope * spinor
    coefficients /= np.linalg.norm(coefficients)
    packet = np.fft.ifft(coefficients, axis=0, norm="ortho")
    packet = np.roll(packet, length // 2 + centre, axis=0)
    return packet / np.linalg.norm(packet)


def apply_walk_axis(
    state: np.ndarray, particle: int, mass: float
) -> np.ndarray:
    internal_axis = 3 + particle
    zero = [slice(None)] * state.ndim
    one = [slice(None)] * state.ndim
    zero[internal_axis] = 0
    one[internal_axis] = 1
    zero = tuple(zero)
    one = tuple(one)
    zero_input = state[zero]
    one_input = state[one]
    normalization = np.sqrt(1 - mass * mass)
    output = np.empty_like(state)
    output[zero] = (
        normalization * np.roll(zero_input, -1, axis=particle)
        - 1j * mass * one_input
    )
    output[one] = (
        -1j * mass * zero_input
        + normalization * np.roll(one_input, 1, axis=particle)
    )
    return output


def apply_interactions(
    state: np.ndarray, pair_coupling: float, projectile_coupling: float
) -> np.ndarray:
    state = state.copy()
    length = state.shape[0]
    diagonal = np.arange(length)
    pair_phase = np.exp(1j * pair_coupling)
    projectile_phase = np.exp(1j * projectile_coupling)
    state[diagonal, diagonal, :, 0, 1, :] *= pair_phase
    state[diagonal, diagonal, :, 1, 0, :] *= pair_phase
    state[diagonal, :, diagonal, :, :, :] *= projectile_phase
    state[:, diagonal, diagonal, :, :, :] *= projectile_phase
    return state


def apply_three_body_step(
    state: np.ndarray,
    pair_mass: float,
    projectile_mass: float,
    pair_coupling: float,
    projectile_coupling: float,
    *,
    interaction_first: bool = True,
) -> np.ndarray:
    if interaction_first:
        output = apply_interactions(state, pair_coupling, projectile_coupling)
        output = apply_walk_axis(output, 0, pair_mass)
        output = apply_walk_axis(output, 1, pair_mass)
        return apply_walk_axis(output, 2, projectile_mass)
    output = apply_walk_axis(state, 0, pair_mass)
    output = apply_walk_axis(output, 1, pair_mass)
    output = apply_walk_axis(output, 2, projectile_mass)
    return apply_interactions(output, pair_coupling, projectile_coupling)


def position_probability(state: np.ndarray) -> np.ndarray:
    return np.sum(np.abs(state) ** 2, axis=(3, 4, 5))


def circular_mean(probability: np.ndarray) -> float:
    length = len(probability)
    coordinate = np.arange(length)
    phase = np.sum(probability * np.exp(2j * np.pi * coordinate / length))
    index = (np.angle(phase) % (2 * np.pi)) * length / (2 * np.pi)
    return float((index - length // 2 + length // 2) % length - length // 2)


def translation_phase(state: np.ndarray, axes: tuple[int, ...]) -> tuple[float, float]:
    translated = state
    for axis in axes:
        translated = np.roll(translated, 1, axis=axis)
    overlap = np.vdot(state, translated)
    return float(-np.angle(overlap)), float(abs(overlap))


def observables(state: np.ndarray) -> dict[str, float]:
    length = state.shape[0]
    probability = position_probability(state)
    pair_first = np.sum(probability, axis=2)
    molecule_site = 0.5 * (
        np.sum(pair_first, axis=1) + np.sum(pair_first, axis=0)
    )
    projectile_site = np.sum(probability, axis=(0, 1))
    indices = np.arange(length)
    coordinates = indices.astype(float) - length // 2
    first_coordinate, second_coordinate = np.meshgrid(
        coordinates, coordinates, indexing="ij"
    )
    relative = (
        indices[:, None] - indices[None, :] + length // 2
    ) % length - length // 2
    pair_relative_probability = np.sum(probability, axis=2)
    pair_momentum, pair_coherence = translation_phase(state, (0, 1))
    projectile_momentum, projectile_coherence = translation_phase(state, (2,))
    total_momentum, total_coherence = translation_phase(state, (0, 1, 2))
    first_third_contact = np.sum(probability[indices, :, indices])
    second_third_contact = np.sum(probability[:, indices, indices])
    triple = np.sum(probability[indices, indices, indices])
    return {
        "pair_centre": float(
            np.sum(
                pair_first * (first_coordinate + second_coordinate) / 2
            ).real
        ),
        "pair_circular_centre": circular_mean(molecule_site),
        "projectile_centre": circular_mean(projectile_site),
        "close_probability": float(
            np.sum(pair_relative_probability[np.abs(relative) <= 2]).real
        ),
        "relative_variance": float(
            np.sum(pair_relative_probability * relative**2).real
        ),
        "contact_probability": float(
            (first_third_contact + second_third_contact - triple).real
        ),
        "pair_momentum": pair_momentum,
        "pair_momentum_coherence": pair_coherence,
        "projectile_momentum": projectile_momentum,
        "projectile_momentum_coherence": projectile_coherence,
        "total_momentum": total_momentum,
        "total_momentum_coherence": total_coherence,
        "norm": float(np.linalg.norm(state)),
    }


def project_bound_branch(
    state: np.ndarray, pair_mass: float, pair_coupling: float
) -> tuple[np.ndarray, np.ndarray]:
    """Project particles 0/1 onto the selected Cycle-205 molecular band.

    The transform uses the same asymmetric total-momentum gauge as the exact
    two-particle block: r=x1-x2 and y=x2.  The projectile degrees of freedom
    are retained, so this is a genuine subsystem-band projection rather than
    a product-state fit.
    """
    length = state.shape[0]
    base = np.arange(length)
    relative_base = np.empty_like(state)
    for relative in range(length):
        relative_base[relative] = state[
            (base + relative) % length, base, :, :, :, :
        ]
    relative_momentum = np.fft.fft(relative_base, axis=1, norm="ortho")
    projected_momentum = np.zeros_like(relative_momentum)
    branch_weights = np.zeros(length, dtype=float)
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    for index, momentum in enumerate(momenta):
        vector = bound_eigenpair(
            length, float(momentum), pair_mass, pair_coupling
        ).vector
        coefficient = np.einsum(
            "rab,rxabc->xc",
            np.conjugate(vector),
            relative_momentum[:, index],
            optimize=True,
        )
        branch_weights[index] = float(np.sum(np.abs(coefficient) ** 2).real)
        projected_momentum[:, index] = np.einsum(
            "rab,xc->rxabc", vector, coefficient, optimize=True
        )
    projected_relative_base = np.fft.ifft(
        projected_momentum, axis=1, norm="ortho"
    )
    projected = np.empty_like(state)
    for relative in range(length):
        projected[(base + relative) % length, base, :, :, :, :] = (
            projected_relative_base[relative]
        )
    return projected, branch_weights


@lru_cache(maxsize=None)
def branch_group_velocities(
    length: int, pair_mass: float, pair_coupling: float
) -> tuple[float, ...]:
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    phases = np.asarray(
        [
            bound_eigenpair(length, float(momentum), pair_mass, pair_coupling).phase
            for momentum in momenta
        ]
    )
    order = np.argsort(momenta)
    sorted_phases = np.unwrap(phases[order])
    sorted_velocities = -np.gradient(
        sorted_phases, momenta[order], edge_order=2
    )
    velocities = np.empty(length, dtype=float)
    velocities[order] = sorted_velocities
    return tuple(float(value) for value in velocities)


def bound_branch_observables(
    state: np.ndarray, pair_mass: float, pair_coupling: float
) -> dict[str, float]:
    projected, weights = project_bound_branch(state, pair_mass, pair_coupling)
    population = float(np.sum(weights))
    if population <= 0:
        raise RuntimeError("selected bound branch has zero population")
    projected /= np.sqrt(population)
    result = observables(projected)
    momenta = 2 * np.pi * np.fft.fftfreq(len(weights))
    mean_phase = np.sum(weights * np.exp(1j * momenta)) / population
    velocities = np.asarray(
        branch_group_velocities(
            len(weights), pair_mass, pair_coupling
        )
    )
    return {
        "bound_population": population,
        "bound_pair_centre": result["pair_centre"],
        "bound_pair_circular_centre": result["pair_circular_centre"],
        "bound_projectile_centre": result["projectile_centre"],
        "bound_pair_momentum": float(np.angle(mean_phase)),
        "bound_pair_momentum_coherence": float(abs(mean_phase)),
        "bound_band_velocity": float(np.sum(weights * velocities) / population),
        "bound_close_probability": result["close_probability"],
    }


@dataclass
class Trajectory:
    rows: list[dict[str, float]]
    final_state: np.ndarray
    bound_rows: list[dict[str, float]] | None = None
    snapshots: dict[int, np.ndarray] | None = None


def run_collision(
    projectile_coupling: float,
    *,
    length: int = 64,
    duration: int = 54,
    pair_centre: int = -13,
    projectile_centre: int = 15,
    projectile_momentum: float = 0.72,
    projectile_momentum_width: float = 0.13,
    pair_mass: float = 0.6,
    pair_coupling: float = 0.2 * np.pi,
    pair_momentum_width: float = 0.16,
    project_branch: bool = False,
    snapshot_steps: tuple[int, ...] = (),
) -> Trajectory:
    projectile_mass = 0.3
    pair = prepare_bound_packet(
        length, pair_mass, pair_coupling, pair_momentum_width
    )
    pair = np.roll(np.roll(pair, pair_centre, axis=0), pair_centre, axis=1)
    projectile = prepare_projectile(
        length,
        projectile_mass,
        projectile_centre,
        projectile_momentum,
        projectile_momentum_width,
    )
    state = np.einsum("ijab,kc->ijkabc", pair, projectile, optimize=True)
    state /= np.linalg.norm(state)
    rows = [observables(state)]
    snapshots = {0: state.copy()} if 0 in snapshot_steps else {}
    bound_rows = (
        [bound_branch_observables(state, pair_mass, pair_coupling)]
        if project_branch
        else None
    )
    for step in range(1, duration + 1):
        state = apply_three_body_step(
            state,
            pair_mass,
            projectile_mass,
            pair_coupling,
            projectile_coupling,
        )
        rows.append(observables(state))
        if step in snapshot_steps:
            snapshots[step] = state.copy()
        if bound_rows is not None:
            bound_rows.append(
                bound_branch_observables(state, pair_mass, pair_coupling)
            )
    return Trajectory(rows, state, bound_rows, snapshots)


def translate_all(state: np.ndarray, displacement: int) -> np.ndarray:
    translated = state
    for axis in (0, 1, 2):
        translated = np.roll(translated, displacement, axis=axis)
    return translated


def mirror_all(state: np.ndarray) -> np.ndarray:
    indices = (-np.arange(state.shape[0])) % state.shape[0]
    mirrored = state
    for axis in (0, 1, 2):
        mirrored = np.take(mirrored, indices, axis=axis)
    return np.flip(mirrored, axis=(3, 4, 5))


def exchange_pair(state: np.ndarray) -> np.ndarray:
    return -np.transpose(state, (1, 0, 2, 4, 3, 5))


def projectile_purity(state: np.ndarray) -> float:
    matrix = np.transpose(state, (0, 1, 3, 4, 2, 5)).reshape(
        -1, 2 * state.shape[2]
    )
    reduced = matrix.conj().T @ matrix
    return float(np.trace(reduced @ reduced).real)


def local_law_controls() -> None:
    length = 6
    pair_mass = 0.61
    projectile_mass = 0.37
    pair_coupling = 0.19 * np.pi
    projectile_coupling = 0.07 * np.pi
    rng = np.random.default_rng(206)
    state = rng.normal(size=(length, length, length, 2, 2, 2)) + 1j * rng.normal(
        size=(length, length, length, 2, 2, 2)
    )
    state /= np.linalg.norm(state)
    evolved = apply_three_body_step(
        state,
        pair_mass,
        projectile_mass,
        pair_coupling,
        projectile_coupling,
    )
    check(
        "three-carrier update is unitary on a generic complex state",
        abs(np.linalg.norm(evolved) - 1) < 2e-13,
        np.linalg.norm(evolved),
    )
    check(
        "one common translation commutes with the local update",
        np.allclose(
            apply_three_body_step(
                translate_all(state, 1),
                pair_mass,
                projectile_mass,
                pair_coupling,
                projectile_coupling,
            ),
            translate_all(evolved, 1),
            atol=2e-13,
        ),
    )
    check(
        "reflection plus internal-label exchange is an exact covariance",
        np.allclose(
            apply_three_body_step(
                mirror_all(state),
                pair_mass,
                projectile_mass,
                pair_coupling,
                projectile_coupling,
            ),
            mirror_all(evolved),
            atol=2e-13,
        ),
    )

    alternate = apply_three_body_step(
        state,
        pair_mass,
        projectile_mass,
        pair_coupling,
        projectile_coupling,
        interaction_first=False,
    )
    conjugated = apply_interactions(
        apply_three_body_step(
            apply_interactions(
                state, -pair_coupling, -projectile_coupling
            ),
            pair_mass,
            projectile_mass,
            pair_coupling,
            projectile_coupling,
        ),
        pair_coupling,
        projectile_coupling,
    )
    check(
        "walk/interaction cyclic schedules are related by a time-origin conjugacy",
        np.allclose(alternate, conjugated, atol=2e-13),
        np.linalg.norm(alternate - conjugated),
    )

    delta = np.zeros_like(state)
    centre = length // 2
    delta[centre, centre, centre, 0, 1, 0] = 1
    once = apply_three_body_step(
        delta,
        pair_mass,
        projectile_mass,
        pair_coupling,
        projectile_coupling,
    )
    occupied = np.argwhere(position_probability(once) > 1e-14)
    check(
        "each carrier moves by at most one edge in one strict tick",
        all(
            all(abs(int(row[axis]) - centre) <= 1 for axis in (0, 1, 2))
            for row in occupied
        ),
        occupied.tolist(),
    )


def collision_metrics(
    projectile_coupling: float, *, length: int = 72
) -> dict[str, object]:
    pair_mass = 0.85
    pair_coupling = 0.1 * np.pi
    trajectory = run_collision(
        projectile_coupling,
        length=length,
        duration=42,
        pair_mass=pair_mass,
        pair_coupling=pair_coupling,
        pair_centre=-10,
        projectile_centre=10,
        pair_momentum_width=0.2,
        projectile_momentum_width=0.2,
    )
    rows = trajectory.rows
    initial = rows[0]
    final = rows[-1]
    bound = bound_branch_observables(
        trajectory.final_state, pair_mass, pair_coupling
    )
    metrics: dict[str, object] = {
        "coupling_fraction": projectile_coupling / np.pi,
        "initial": initial,
        "final": final,
        "bound": bound,
        "max_contact": max(row["contact_probability"] for row in rows),
        "total_phase_drift": max(
            abs(row["total_momentum"] - initial["total_momentum"])
            for row in rows
        ),
        "total_coherence_drift": max(
            abs(
                row["total_momentum_coherence"]
                - initial["total_momentum_coherence"]
            )
            for row in rows
        ),
        "norm_drift": max(abs(row["norm"] - 1) for row in rows),
        "exchange_residual": np.linalg.norm(
            trajectory.final_state - exchange_pair(trajectory.final_state)
        ),
        "projectile_purity": projectile_purity(trajectory.final_state),
    }
    return metrics


def collision_tournament() -> None:
    deleted = collision_metrics(0.0)
    weak = collision_metrics(0.03 * np.pi)
    strong = collision_metrics(0.06 * np.pi)

    for label, result in (("deleted", deleted), ("weak", weak), ("strong", strong)):
        check(
            f"{label} trajectory preserves norm and exact total translation characteristic",
            result["norm_drift"] < 2e-12
            and result["total_phase_drift"] < 2e-12
            and result["total_coherence_drift"] < 2e-12,
            {
                "norm": result["norm_drift"],
                "phase": result["total_phase_drift"],
                "coherence": result["total_coherence_drift"],
            },
        )
        check(
            f"{label} trajectory preserves fermionic antisymmetry of the molecule",
            result["exchange_residual"] < 2e-11,
            result["exchange_residual"],
        )

    deleted_initial = deleted["initial"]
    deleted_final = deleted["final"]
    deleted_bound = deleted["bound"]
    check(
        "collision geometry without the projectile phase produces no recoil",
        deleted["max_contact"] > 0.07
        and abs(deleted_final["pair_momentum"] - deleted_initial["pair_momentum"]) < 2e-12
        and abs(
            deleted_final["pair_circular_centre"]
            - deleted_initial["pair_circular_centre"]
        )
        < 2e-10
        and abs(deleted_bound["bound_population"] - 1) < 2e-10,
        {
            "max_contact": deleted["max_contact"],
            "pair_momentum": deleted_final["pair_momentum"],
            "pair_centre": deleted_final["pair_circular_centre"],
            "bound_population": deleted_bound["bound_population"],
        },
    )

    for label, result, minimum_population in (
        ("weak", weak, 0.985),
        ("strong", strong, 0.95),
    ):
        initial = result["initial"]
        final = result["final"]
        bound = result["bound"]
        pair_change = final["pair_momentum"] - initial["pair_momentum"]
        projectile_change = (
            final["projectile_momentum"] - initial["projectile_momentum"]
        )
        check(
            f"{label} onsite collision generates opposite carrier/molecule momentum changes",
            pair_change > 0
            and projectile_change < 0
            and abs(pair_change + projectile_change) < 1.2e-3,
            {
                "pair_change": pair_change,
                "projectile_change": projectile_change,
                "exact_total_phase_drift": result["total_phase_drift"],
            },
        )
        check(
            f"{label} collision leaves a dominant tightly bound molecular branch",
            bound["bound_population"] > minimum_population
            and bound["bound_close_probability"] > 0.997
            and final["contact_probability"] < 0.006
            and result["max_contact"] > 0.07,
            {
                "bound_population": bound["bound_population"],
                "bound_close": bound["bound_close_probability"],
                "peak_contact": result["max_contact"],
                "final_contact": final["contact_probability"],
            },
        )
        check(
            f"{label} collision generates whole-molecule displacement without an external force profile",
            abs(
                bound["bound_pair_circular_centre"]
                - initial["pair_circular_centre"]
            )
            > (0.2 if label == "weak" else 0.5),
            {
                "initial": initial["pair_circular_centre"],
                "final_bound": bound["bound_pair_circular_centre"],
            },
        )

    check(
        "stronger local collision increases recoil and inelastic leakage",
        abs(strong["final"]["pair_momentum"]) > 3 * abs(weak["final"]["pair_momentum"])
        and strong["bound"]["bound_population"] < weak["bound"]["bound_population"]
        and strong["projectile_purity"] < weak["projectile_purity"] < 1,
        {
            "weak_pair_momentum": weak["final"]["pair_momentum"],
            "strong_pair_momentum": strong["final"]["pair_momentum"],
            "weak_bound_population": weak["bound"]["bound_population"],
            "strong_bound_population": strong["bound"]["bound_population"],
            "purities": (weak["projectile_purity"], strong["projectile_purity"]),
        },
    )

    finite = collision_metrics(0.03 * np.pi, length=64)
    check(
        "molecular recoil observables are stable under a held-out ring size",
        abs(
            finite["bound"]["bound_population"]
            - weak["bound"]["bound_population"]
        )
        < 2e-3
        and abs(
            finite["bound"]["bound_pair_momentum"]
            - weak["bound"]["bound_pair_momentum"]
        )
        < 2e-3
        and abs(
            finite["bound"]["bound_pair_circular_centre"]
            - weak["bound"]["bound_pair_circular_centre"]
        )
        < 0.05,
        {
            "L64": finite["bound"],
            "L72": weak["bound"],
        },
    )

    check(
        "candidate collision uses generic complex non-Clifford phases",
        min(abs(0.03 * np.pi - index * np.pi / 4) for index in range(-4, 5)) > 1e-3
        and min(abs(0.1 * np.pi - index * np.pi / 4) for index in range(-4, 5)) > 1e-3,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    local_law_controls()
    collision_tournament()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "GENERATED_BOUND_MOLECULE_RECOIL" if FAIL == 0 else "CYCLE206_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
