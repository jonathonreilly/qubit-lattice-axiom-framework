#!/usr/bin/env python3
"""Cycle 212: generated recoil of the Cycle-210 proper-cubic object.

Within the exact equal-direction bound sector, reduce the three-carrier law to
one six-direction molecule and one six-direction projectile.  They receive a
proper-cubic onsite partial-SWAP only at contact, then their own local coins
and one-edge streams.  Late relational branches are tested for generated
recoil and the independently fixed Cycle-210 curvature mass.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path

import numpy as np

import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PROPER_CUBIC_GENERATED_RECOIL_CYCLE212_NOTE_2026-07-16.md"
)

I36 = np.eye(36, dtype=complex)
SWAP = np.zeros((36, 36), dtype=complex)
for first, second in product(range(6), repeat=2):
    SWAP[second * 6 + first, first * 6 + second] = 1

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


def wrap(value: np.ndarray | float) -> np.ndarray | float:
    return np.angle(np.exp(1j * np.asarray(value)))


def projectile_coin() -> np.ndarray:
    return c210.cubic_coin(-0.7, -0.55, 0.1)


def scalar_branch(momentum: np.ndarray, coin: np.ndarray) -> tuple[float, np.ndarray]:
    values, vectors = np.linalg.eig(c210.molecular_bloch(momentum, coin))
    index = int(np.argmax(np.abs(vectors.conj().T @ c210.UNIFORM)))
    vector = vectors[:, index]
    vector *= np.exp(-1j * np.angle(np.vdot(c210.UNIFORM, vector)))
    return float(np.angle(values[index])), vector / np.linalg.norm(vector)


def partial_swap(angle: float) -> np.ndarray:
    return np.cos(angle) * I36 + 1j * np.sin(angle) * SWAP


def prepare_incoming(
    length: int = 25,
    separation: int = 4,
    longitudinal_width: float = 0.35,
    transverse_width: float = 1.5,
) -> tuple[np.ndarray, np.ndarray, c210.Species]:
    species = c210.tuned_species(-0.4)
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    central = float(momenta[2])
    total = np.array((central, 0.0, 0.0))
    state_k = np.zeros((length, length, length, 6, 6), dtype=complex)
    for ix, iy, iz in product(range(length), repeat=3):
        projectile_momentum = np.array(
            (momenta[ix], momenta[iy], momenta[iz])
        )
        delta = np.asarray(wrap(projectile_momentum - total), dtype=float)
        envelope = np.exp(
            -0.5 * (delta[0] / longitudinal_width) ** 2
            -0.5 * (delta[1] / transverse_width) ** 2
            -0.5 * (delta[2] / transverse_width) ** 2
        )
        if envelope < 1e-12:
            continue
        molecule_momentum = np.asarray(wrap(total - projectile_momentum), dtype=float)
        _, molecule = c210.branch_eigenpair(molecule_momentum, species)
        _, projectile = scalar_branch(projectile_momentum, projectile_coin())
        state_k[ix, iy, iz] = envelope * np.outer(molecule, projectile)
    state_k /= np.linalg.norm(state_k)
    state = np.fft.ifftn(state_k, axes=(0, 1, 2), norm="ortho")
    state = np.roll(state, separation, axis=0)
    return state / np.linalg.norm(state), total, species


def apply_step(
    state: np.ndarray,
    total_momentum: np.ndarray,
    species: c210.Species,
    collision_angle: float,
) -> np.ndarray:
    length = state.shape[0]
    working = state.reshape(length, length, length, 36).copy()
    working[0, 0, 0] = partial_swap(collision_angle) @ working[0, 0, 0]
    working = working.reshape(length, length, length, 6, 6)
    mixed = np.einsum(
        "ai,bj,xyzij->xyzab",
        species.coin,
        projectile_coin(),
        working,
        optimize=True,
    )
    output = np.zeros_like(mixed)
    for molecule_direction, projectile_direction in product(range(6), repeat=2):
        relative_shift = tuple(
            int(value)
            for value in (
                c210.DIRECTIONS[projectile_direction]
                - c210.DIRECTIONS[molecule_direction]
            )
        )
        phase = np.exp(
            -1j
            * float(
                total_momentum @ c210.DIRECTIONS[molecule_direction]
            )
        )
        output[..., molecule_direction, projectile_direction] += phase * np.roll(
            mixed[..., molecule_direction, projectile_direction],
            relative_shift,
            axis=(0, 1, 2),
        )
    return output


def signed_coordinates(length: int) -> np.ndarray:
    return (np.arange(length) + length // 2) % length - length // 2


def observables(state: np.ndarray) -> dict[str, object]:
    probability = np.sum(np.abs(state) ** 2, axis=(3, 4))
    coordinate = signed_coordinates(state.shape[0])
    grids = np.meshgrid(coordinate, coordinate, coordinate, indexing="ij")
    means = []
    coherences = []
    for axis in range(3):
        marginal = np.sum(
            probability,
            axis=tuple(index for index in range(3) if index != axis),
        )
        phase = np.sum(
            marginal
            * np.exp(2j * np.pi * np.arange(state.shape[0]) / state.shape[0])
        )
        index = (np.angle(phase) % (2 * np.pi)) * state.shape[0] / (2 * np.pi)
        means.append(float((index + state.shape[0] // 2) % state.shape[0] - state.shape[0] // 2))
        coherences.append(float(abs(phase)))
    boundary_mask = np.logical_or.reduce(
        tuple(np.abs(grid) > 0.42 * state.shape[0] for grid in grids)
    )
    return {
        "norm": float(np.linalg.norm(state)),
        "contact": float(probability[0, 0, 0]),
        "mean_relative": means,
        "position_coherence": coherences,
        "boundary": float(
            np.sum(probability[boundary_mask])
        ),
    }


def local_masks(length: int, guard: int = 1) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    coordinate = signed_coordinates(length)
    x = coordinate[:, None, None]
    transmitted = np.broadcast_to(x < -guard, (length, length, length))
    reflected = np.broadcast_to(x > guard, (length, length, length))
    unresolved = ~(transmitted | reflected)
    return transmitted, reflected, unresolved


def local_probabilities(state: np.ndarray) -> np.ndarray:
    probability = np.sum(np.abs(state) ** 2, axis=(3, 4))
    return np.asarray(
        [float(np.sum(probability[mask])) for mask in local_masks(state.shape[0])]
    )


def project(state: np.ndarray, mask: np.ndarray) -> np.ndarray:
    projected = state * mask[..., None, None]
    return projected / np.linalg.norm(projected)


def phase_gradient(momentum: np.ndarray, species: c210.Species, step: float = 1e-4) -> np.ndarray:
    velocity = np.zeros(3)
    for axis in range(3):
        plus = momentum.copy()
        minus = momentum.copy()
        plus[axis] += step
        minus[axis] -= step
        p = c210.phase_near_origin(np.asarray(wrap(plus)), species)
        m = c210.phase_near_origin(np.asarray(wrap(minus)), species)
        velocity[axis] = -(p - m) / (2 * step)
    return velocity


def molecular_branch(state: np.ndarray, total: np.ndarray, species: c210.Species) -> dict[str, object]:
    length = state.shape[0]
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    state_k = np.fft.fftn(state, axes=(0, 1, 2), norm="ortho")
    weights = np.zeros((length, length, length))
    molecule_momenta = np.zeros((length, length, length, 3))
    for ix, iy, iz in product(range(length), repeat=3):
        projectile_momentum = np.array((momenta[ix], momenta[iy], momenta[iz]))
        molecule_momentum = np.asarray(wrap(total - projectile_momentum), dtype=float)
        molecule_momenta[ix, iy, iz] = molecule_momentum
        _, vector = c210.branch_eigenpair(molecule_momentum, species)
        projectile_vector = np.einsum(
            "a,ab->b", np.conjugate(vector), state_k[ix, iy, iz]
        )
        weights[ix, iy, iz] = float(np.sum(np.abs(projectile_vector) ** 2))
    population = float(np.sum(weights))
    mean = np.zeros(3)
    coherence = np.zeros(3)
    for axis in range(3):
        phase = np.sum(weights * np.exp(1j * molecule_momenta[..., axis]))
        mean[axis] = np.angle(phase)
        coherence[axis] = abs(phase) / population
    velocity = phase_gradient(mean.copy(), species)
    momentum_norm = float(np.linalg.norm(mean))
    velocity_norm = float(np.linalg.norm(velocity))
    return {
        "population": population,
        "mean_momentum": mean,
        "momentum_coherence": coherence,
        "group_velocity": velocity,
        "secant_mass": momentum_norm / velocity_norm if velocity_norm > 1e-10 else float("nan"),
    }


@dataclass(frozen=True)
class Run:
    angle: float
    initial: dict[str, object]
    peak_contact: float
    final: dict[str, object]
    probabilities: np.ndarray
    state: np.ndarray
    total: np.ndarray
    species: c210.Species


def run(angle: float, duration: int = 16, length: int = 25) -> Run:
    state, total, species = prepare_incoming(length=length)
    initial = observables(state)
    rows = [initial]
    for _ in range(duration):
        state = apply_step(state, total, species, angle)
        rows.append(observables(state))
    return Run(
        angle,
        initial,
        max(float(row["contact"]) for row in rows),
        rows[-1],
        local_probabilities(state),
        state,
        total,
        species,
    )


def branch(result: Run, index: int) -> dict[str, object]:
    return molecular_branch(
        project(result.state, local_masks(result.state.shape[0])[index]),
        result.total,
        result.species,
    )


def tangent_mass(momentum: np.ndarray, species: c210.Species, step: float = 1e-3) -> float:
    plus = momentum.copy()
    minus = momentum.copy()
    plus[0] += step
    minus[0] -= step
    derivative = (
        phase_gradient(plus, species)[0] - phase_gradient(minus, species)[0]
    ) / (2 * step)
    return float(1 / abs(derivative))


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "proper-cubic",
        "third carrier",
        "onsite partial-swap",
        "generated recoil",
        "incremental mass",
        "collision deletion",
        "relational branch",
        "supplied late partition",
        "finite pre-asymptotic",
        "global novelty has not been established",
        "record formation remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves attribution, detector import, and scope", not missing, missing)


def law_controls() -> None:
    species = c210.tuned_species(-0.4)
    angle = 0.25 * np.pi
    collision = partial_swap(angle)
    check(
        "partial-SWAP is a nontrivial onsite unitary",
        np.linalg.norm(SWAP @ SWAP - I36) < 2e-12
        and np.linalg.norm(SWAP.conj().T - SWAP) < 2e-12
        and np.linalg.norm(collision.conj().T @ collision - I36) < 3e-12
        and np.linalg.norm(collision - I36) > 1,
    )

    probe = np.array((0.17, -0.11, 0.07))
    residuals = []
    for frame in c210.proper_cubic_frames():
        representation = c210.direction_permutation(frame)
        pair_representation = np.kron(representation, representation)
        residuals.append(
            max(
                np.linalg.norm(
                    pair_representation
                    @ collision
                    @ pair_representation.conj().T
                    - collision
                ),
                np.linalg.norm(
                    representation
                    @ c210.molecular_bloch(probe, species.coin)
                    @ representation.conj().T
                    - c210.molecular_bloch(frame @ probe, species.coin)
                ),
                np.linalg.norm(
                    representation
                    @ c210.molecular_bloch(probe, projectile_coin())
                    @ representation.conj().T
                    - c210.molecular_bloch(frame @ probe, projectile_coin())
                ),
            )
        )
    check(
        "molecule, projectile, and collision are exact in all 24 cubic frames",
        max(residuals) < 3e-12,
        max(residuals),
    )

    rng = np.random.default_rng(212)
    random_state = rng.normal(size=(5, 5, 5, 6, 6)) + 1j * rng.normal(
        size=(5, 5, 5, 6, 6)
    )
    random_state /= np.linalg.norm(random_state)
    evolved = apply_step(
        random_state, np.array((0.31, -0.17, 0.09)), species, angle
    )
    check(
        "the fixed-total-momentum relative update is unitary",
        abs(np.linalg.norm(evolved) - 1) < 3e-12,
        np.linalg.norm(evolved),
    )
    delta = np.zeros((7, 7, 7, 6, 6), dtype=complex)
    delta[0, 0, 0, 0, 1] = 1
    support = np.argwhere(
        np.sum(
            np.abs(apply_step(delta, np.zeros(3), species, angle)) ** 2,
            axis=(3, 4),
        )
        > 1e-14
    )
    signed = (support + 3) % 7 - 3
    check(
        "one tick streams each carrier one edge and relative support by at most two",
        np.max(np.abs(signed)) <= 2,
        signed.tolist(),
    )

    coin_product = np.kron(species.coin, projectile_coin())
    check(
        "collision/coin cyclic time-origin schedules have identical onsite phases",
        np.allclose(
            np.sort_complex(np.linalg.eigvals(collision @ coin_product)),
            np.sort_complex(np.linalg.eigvals(coin_product @ collision)),
            atol=3e-12,
        ),
    )
    fourier = np.exp(
        2j * np.pi * np.outer(np.arange(6), np.arange(6)) / 6
    ) / np.sqrt(6)
    basis = np.kron(fourier, fourier)
    transformed_collision = basis @ collision @ basis.conj().T
    check(
        "common coin-basis conjugation preserves the partial-SWAP spectrum",
        np.linalg.norm(
            basis.conj().T @ transformed_collision @ basis - collision
        )
        < 3e-12
        and all(
            abs(
                np.trace(np.linalg.matrix_power(transformed_collision, power))
                - np.trace(np.linalg.matrix_power(collision, power))
            )
            < 3e-11
            for power in range(1, 5)
        ),
    )
    phases = (-0.7, -0.55, 0.1, species.alpha, species.beta, species.rest_phase)
    check(
        "the collision tournament retains generic complex non-Clifford phases",
        all(
            min(abs(value - multiple * np.pi / 4) for multiple in range(-8, 9))
            > 1e-3
            for value in phases
        ),
        phases,
    )


def collision_controls() -> tuple[Run, Run, Run]:
    deleted = run(0.0)
    intermediate = run(0.25 * np.pi)
    strong = run(0.5 * np.pi)
    for label, result in (
        ("deleted", deleted),
        ("intermediate", intermediate),
        ("strong", strong),
    ):
        check(
            f"{label} trajectory stays normalized with a real contact event",
            abs(float(result.final["norm"]) - 1) < 3e-12
            and result.peak_contact > 0.004
            and float(result.initial["contact"]) < 0.0044,
            {
                "peak_contact": result.peak_contact,
                "initial": result.initial["contact"],
                "final": result.final["contact"],
            },
        )
        check(
            f"{label} relational T/R/X alternatives are positive and normalized",
            np.min(result.probabilities) >= 0
            and abs(float(np.sum(result.probabilities)) - 1) < 3e-12,
            result.probabilities.tolist(),
        )

    deleted_r = branch(deleted, 1)
    intermediate_r = branch(intermediate, 1)
    strong_r = branch(strong, 1)
    generated_momenta = (
        float(intermediate_r["mean_momentum"][0] - deleted_r["mean_momentum"][0]),
        float(strong_r["mean_momentum"][0] - deleted_r["mean_momentum"][0]),
    )
    check(
        "the fixed onsite collision generates a monotone reflected-branch recoil",
        0.003 < generated_momenta[0] < generated_momenta[1]
        and generated_momenta[1] > 0.005
        and strong.probabilities[1] - deleted.probabilities[1] > 0.009,
        {
            "delta_momentum": generated_momenta,
            "delta_R_probability": strong.probabilities[1] - deleted.probabilities[1],
        },
    )

    incremental = []
    for candidate in (intermediate_r, strong_r):
        delta_momentum = np.asarray(candidate["mean_momentum"]) - np.asarray(
            deleted_r["mean_momentum"]
        )
        delta_velocity = np.asarray(candidate["group_velocity"]) - np.asarray(
            deleted_r["group_velocity"]
        )
        incremental.append(
            float(np.linalg.norm(delta_momentum) / np.linalg.norm(delta_velocity))
        )
    independent_tangent = tangent_mass(
        np.asarray(deleted_r["mean_momentum"]), deleted.species
    )
    check(
        "generated incremental recoil carries the independently fixed tangent mass",
        max(abs(value / independent_tangent - 1) for value in incremental) < 0.004,
        {"incremental": incremental, "tangent": independent_tangent},
    )
    check(
        "generated recoil remains within 2.5 percent of the rest/curvature mass",
        max(
            abs(value / deleted.species.analytic_mass - 1)
            for value in incremental
        )
        < 0.025,
        {
            "incremental": incremental,
            "rest_curvature": deleted.species.analytic_mass,
        },
    )
    check(
        "the strong relational R branch remains predominantly in the molecular scalar band",
        strong_r["population"] > 0.88
        and strong_r["momentum_coherence"][0] > 0.92,
        strong_r,
    )

    duplicated = np.diag(strong.probabilities)
    check(
        "a redundant late outcome copy preserves every branch weight",
        np.allclose(np.sum(duplicated, axis=0), strong.probabilities)
        and np.allclose(np.sum(duplicated, axis=1), strong.probabilities),
    )
    return deleted, intermediate, strong


def finite_size_controls() -> None:
    rows = []
    for length in (29, 33):
        deleted = run(0.0, length=length)
        strong = run(0.5 * np.pi, length=length)
        deleted_r = branch(deleted, 1)
        strong_r = branch(strong, 1)
        delta_momentum = np.asarray(strong_r["mean_momentum"]) - np.asarray(
            deleted_r["mean_momentum"]
        )
        delta_velocity = np.asarray(strong_r["group_velocity"]) - np.asarray(
            deleted_r["group_velocity"]
        )
        rows.append(
            (
                length,
                float(np.linalg.norm(delta_momentum) / np.linalg.norm(delta_velocity)),
                float(delta_momentum[0]),
            )
        )
    check(
        "held-out volumes retain the incremental mass despite pre-asymptotic recoil drift",
        max(row[1] for row in rows) / min(row[1] for row in rows) - 1 < 0.002
        and all(row[2] > 0.004 for row in rows),
        rows,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    law_controls()
    collision_controls()
    finite_size_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PROPER_CUBIC_GENERATED_RECOIL" if FAIL == 0 else "CYCLE212_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
