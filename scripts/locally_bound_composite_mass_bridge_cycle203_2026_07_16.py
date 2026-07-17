#!/usr/bin/env python3
"""Cycle 203: locally bound composite and its inertial mass.

Two distinguishable lattice carriers hop locally and attract only when they
occupy the same site.  The runner derives the bound band, prepares a localized
bound-pair packet, applies the same onsite force to each constituent, and
compares total force / centre acceleration with the independent bound-band
curvature mass.  It also tests interaction deletion and a proper-cubic 3D
fixed-total-momentum extension.

This is a candidate interaction mechanism, not a particle spectrum, a record
formation law, a gravitational coupling, or an axiom result.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCALLY_BOUND_COMPOSITE_MASS_BRIDGE_CYCLE203_NOTE_2026-07-16.md"
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
        "autonomously bound relative sector",
        "total force",
        "binding deletion",
        "rest-gap offset remains independent",
        "proper-cubic",
        "spectator record",
        "mass-to-gravity map remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the composite-mass scope boundary", not missing, missing)


def bound_energy_1d(total_momentum: np.ndarray | float, hopping: float, attraction: float) -> np.ndarray:
    momentum = np.asarray(total_momentum)
    return -np.sqrt(
        attraction * attraction
        + 16 * hopping * hopping * np.cos(momentum / 2) ** 2
    )


def bound_mass_1d(hopping: float, attraction: float) -> float:
    return float(np.sqrt(attraction * attraction + 16 * hopping * hopping) / (4 * hopping * hopping))


def exact_bound_band_contract() -> None:
    momentum, hopping, attraction = sp.symbols("K J U", real=True, positive=True)
    energy = -sp.sqrt(
        attraction**2 + 16 * hopping**2 * sp.cos(momentum / 2) ** 2
    )
    curvature = sp.simplify(sp.diff(energy, momentum, 2).subs(momentum, 0))
    expected = 4 * hopping**2 / sp.sqrt(attraction**2 + 16 * hopping**2)
    check(
        "bound-band curvature is exact",
        sp.simplify(curvature - expected) == 0,
        curvature,
    )
    check(
        "inverse curvature gives the composite dispersion mass",
        sp.simplify(1 / curvature - 1 / expected) == 0,
        sp.simplify(1 / curvature),
    )

    continuum_floor = -4 * hopping * sp.cos(momentum / 2)
    gap_at_rest = sp.simplify(continuum_floor.subs(momentum, 0) - energy.subs(momentum, 0))
    check(
        "positive attraction puts the rest state below the two-carrier continuum",
        sp.simplify(gap_at_rest - (sp.sqrt(attraction**2 + 16 * hopping**2) - 4 * hopping)) == 0,
        gap_at_rest,
    )


def wrapped_momenta(length: int) -> np.ndarray:
    return 2 * np.pi * np.fft.fftfreq(length)


def periodic_difference(length: int) -> np.ndarray:
    indices = np.arange(length)
    return (indices[:, None] - indices[None, :] + length // 2) % length - length // 2


def prepare_bound_band_packet(
    length: int,
    hopping: float,
    attraction: float,
    total_momentum_width: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Prepare the exact finite-ring bound eigenvector in each retained K block."""
    momenta = wrapped_momenta(length)
    packet_k = np.zeros((length, length), dtype=complex)
    first = np.arange(length)
    for total_index, total_momentum in enumerate(momenta):
        envelope = np.exp(-0.5 * (total_momentum / total_momentum_width) ** 2)
        if envelope <= 1e-14:
            continue
        second = (total_index - first) % length
        free_energy = -2 * hopping * (
            np.cos(momenta[first]) + np.cos(momenta[second])
        )
        continuum_floor = float(np.min(free_energy))

        def secular(energy: float) -> float:
            return float(attraction * np.mean(1 / (free_energy - energy)) - 1)

        finite_bound_energy = brentq(
            secular,
            continuum_floor - 20 * (attraction + 4 * hopping),
            continuum_floor - 1e-12,
            xtol=1e-14,
        )
        relative_vector = 1 / (free_energy - finite_bound_energy)
        relative_vector /= np.linalg.norm(relative_vector)
        packet_k[first, second] = envelope * relative_vector
    packet_k /= np.linalg.norm(packet_k)
    packet = np.fft.ifft2(packet_k, norm="ortho")
    packet = np.roll(np.roll(packet, length // 2, axis=0), length // 2, axis=1)
    return momenta, packet


def pair_coordinates(length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    positions = np.arange(length, dtype=float) - length // 2
    first_x, second_x = np.meshgrid(positions, positions, indexing="ij")
    centre = (first_x + second_x) / 2
    difference = periodic_difference(length)
    return positions, first_x, second_x, centre, difference


def pair_local_generator_action(
    packet: np.ndarray, hopping: float, attraction: float
) -> np.ndarray:
    kinetic = -hopping * (
        np.roll(packet, 1, axis=0)
        + np.roll(packet, -1, axis=0)
        + np.roll(packet, 1, axis=1)
        + np.roll(packet, -1, axis=1)
    )
    return kinetic - attraction * (periodic_difference(len(packet)) == 0) * packet


def local_generator_controls() -> None:
    length = 32
    hopping = 0.5
    attraction = 1.0
    rng = np.random.default_rng(203)
    packet = rng.normal(size=(length, length)) + 1j * rng.normal(size=(length, length))
    packet /= np.linalg.norm(packet)
    local = pair_local_generator_action(packet, hopping, attraction)

    momenta = wrapped_momenta(length)
    first_k, second_k = np.meshgrid(momenta, momenta, indexing="ij")
    free_energy = -2 * hopping * (np.cos(first_k) + np.cos(second_k))
    kinetic = np.fft.ifft2(
        free_energy * np.fft.fft2(packet, norm="ortho"), norm="ortho"
    )
    bloch_plus_contact = kinetic - attraction * (periodic_difference(length) == 0) * packet
    check(
        "two-carrier Bloch generator equals onsite-plus-edge real-space stencil",
        np.allclose(local, bloch_plus_contact, atol=2e-12),
        np.linalg.norm(local - bloch_plus_contact),
    )

    delta = np.zeros((length, length), dtype=complex)
    centre = length // 2
    delta[centre, centre] = 1
    support = set(map(tuple, np.argwhere(np.abs(pair_local_generator_action(delta, hopping, attraction)) > 1e-14)))
    allowed = {
        (centre, centre),
        (centre - 1, centre),
        (centre + 1, centre),
        (centre, centre - 1),
        (centre, centre + 1),
    }
    check(
        "one generator action reaches only onsite or one constituent edge move",
        support <= allowed,
        support,
    )

    translated = np.roll(np.roll(packet, 3, axis=0), 3, axis=1)
    check(
        "common lattice translation commutes with the pair generator",
        np.allclose(
            pair_local_generator_action(translated, hopping, attraction),
            np.roll(np.roll(local, 3, axis=0), 3, axis=1),
            atol=2e-12,
        ),
    )


def pair_observables(
    packet: np.ndarray,
    first_x: np.ndarray,
    second_x: np.ndarray,
    centre: np.ndarray,
    difference: np.ndarray,
) -> dict[str, float]:
    probability = np.abs(packet) ** 2
    mean_centre = float(np.sum(probability * centre).real)
    return {
        "centre": mean_centre,
        "centre_variance": float(np.sum(probability * (centre - mean_centre) ** 2).real),
        "relative_variance": float(np.sum(probability * difference**2).real),
        "close_probability": float(np.sum(probability[np.abs(difference) <= 2]).real),
        "boundary_probability": float(
            np.sum(probability[(np.abs(first_x) > len(packet) / 4) | (np.abs(second_x) > len(packet) / 4)]).real
        ),
    }


@dataclass(frozen=True)
class PairResponse:
    hopping: float
    prepared_attraction: float
    evolution_attraction: float
    force_per_constituent: float
    acceleration: float
    measured_mass: float
    expected_mass: float
    norm: float
    initial: dict[str, float]
    final: dict[str, float]
    final_packet: np.ndarray


def pair_response(
    attraction: float,
    *,
    hopping: float = 0.5,
    evolution_attraction: float | None = None,
    force_per_constituent: float = 1e-3,
    length: int = 320,
    total_momentum_width: float = 0.04,
    duration: float = 20,
    time_step: float = 0.05,
) -> PairResponse:
    if evolution_attraction is None:
        evolution_attraction = attraction
    momenta, packet = prepare_bound_band_packet(
        length, hopping, attraction, total_momentum_width
    )
    _, first_x, second_x, centre, difference = pair_coordinates(length)
    initial = pair_observables(packet, first_x, second_x, centre, difference)

    first_k, second_k = np.meshgrid(momenta, momenta, indexing="ij")
    kinetic_phase = np.exp(
        1j * 2 * hopping * (np.cos(first_k) + np.cos(second_k)) * time_step
    )
    potential = (
        -evolution_attraction * (difference == 0)
        - force_per_constituent * (first_x + second_x)
    )
    half_potential_phase = np.exp(-0.5j * potential * time_step)

    times = [0.0]
    centres = [initial["centre"]]
    sample_stride = max(1, round(0.5 / time_step))
    for step in range(round(duration / time_step)):
        packet *= half_potential_phase
        packet = np.fft.ifft2(
            np.fft.fft2(packet, norm="ortho") * kinetic_phase,
            norm="ortho",
        )
        packet *= half_potential_phase
        if (step + 1) % sample_stride == 0:
            times.append((step + 1) * time_step)
            centres.append(
                pair_observables(packet, first_x, second_x, centre, difference)["centre"]
            )

    acceleration = float(
        2
        * np.polyfit(
            np.asarray(times), np.asarray(centres) - initial["centre"], 2
        )[0]
    )
    total_force = 2 * force_per_constituent
    measured_mass = float(total_force / acceleration) if total_force else float("inf")
    final = pair_observables(packet, first_x, second_x, centre, difference)
    return PairResponse(
        hopping=hopping,
        prepared_attraction=attraction,
        evolution_attraction=evolution_attraction,
        force_per_constituent=force_per_constituent,
        acceleration=acceleration,
        measured_mass=measured_mass,
        expected_mass=bound_mass_1d(hopping, attraction),
        norm=float(np.linalg.norm(packet)),
        initial=initial,
        final=final,
        final_packet=packet,
    )


def direct_composite_tournament() -> dict[float, PairResponse]:
    results: dict[float, PairResponse] = {}
    for attraction in (0.4, 0.7, 1.0, 1.5, 2.0):
        response = pair_response(attraction)
        results[attraction] = response
        relative_error = abs(response.measured_mass / response.expected_mass - 1)
        check(
            f"U={attraction} total-force/centre-acceleration recovers bound-band mass",
            relative_error < 1e-3,
            {
                "measured": response.measured_mass,
                "expected": response.expected_mass,
                "relative_error": relative_error,
            },
        )
        check(
            f"U={attraction} composite remains internally bound while moving",
            abs(response.final["close_probability"] - response.initial["close_probability"]) < 5e-4
            and abs(response.final["relative_variance"] - response.initial["relative_variance"]) < 2e-2,
            {
                "close": (response.initial["close_probability"], response.final["close_probability"]),
                "relative_variance": (
                    response.initial["relative_variance"],
                    response.final["relative_variance"],
                ),
            },
        )
        check(
            f"U={attraction} pair evolution preserves norm and avoids the boundary",
            abs(response.norm - 1) < 2e-10
            and response.final["boundary_probability"] < 1e-5,
            {"norm": response.norm, "boundary": response.final["boundary_probability"]},
        )
    return results


def deletion_redundancy_and_schedule_controls(results: dict[float, PairResponse]) -> None:
    reference = results[1.0]
    deleted = pair_response(1.0, evolution_attraction=0, force_per_constituent=0)
    check(
        "binding deletion disperses the prepared pair",
        deleted.final["close_probability"] < 0.2
        and deleted.final["relative_variance"] > 100
        and reference.final["close_probability"] > 0.9,
        {
            "bound_close": reference.final["close_probability"],
            "deleted_close": deleted.final["close_probability"],
            "deleted_relative_variance": deleted.final["relative_variance"],
        },
    )

    force_deleted = pair_response(1.0, force_per_constituent=0)
    check(
        "force deletion removes centre acceleration without deleting binding",
        abs(force_deleted.acceleration) < 1e-12
        and force_deleted.final["close_probability"] > 0.9,
        force_deleted.acceleration,
    )

    check(
        "the force on the whole pair is the sum of constituent forces",
        abs(
            (2 * reference.force_per_constituent / reference.acceleration)
            / reference.expected_mass
            - 1
        ) < 1e-3
        and abs(
            (reference.force_per_constituent / reference.acceleration)
            / reference.expected_mass
            - 1
        ) > 0.4,
    )

    very_coarse = pair_response(1.0, time_step=0.2)
    coarse = pair_response(1.0, time_step=0.1)
    very_fine = pair_response(1.0, time_step=0.025)
    differences = (
        abs(very_coarse.acceleration - coarse.acceleration),
        abs(coarse.acceleration - reference.acceleration),
        abs(reference.acceleration - very_fine.acceleration),
    )
    refinement_ratios = (
        differences[0] / differences[1],
        differences[1] / differences[2],
    )
    check(
        "composite split-step acceleration converges at second order",
        all(3.5 < ratio < 4.5 for ratio in refinement_ratios),
        {
            "accelerations": (
                very_coarse.acceleration,
                coarse.acceleration,
                reference.acceleration,
                very_fine.acceleration,
            ),
            "refinement_ratios": refinement_ratios,
        },
    )

    packet = reference.final_packet
    exchange_residual = np.linalg.norm(packet - packet.T)
    check(
        "exchange-symmetric prepared sector remains exchange symmetric",
        exchange_residual < 2e-10,
        exchange_residual,
    )

    record_zero = np.array([1, 0], dtype=complex)
    record_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    one_record = packet[:, :, None] * record_zero[None, None, :]
    two_records = (
        packet[:, :, None, None]
        * record_zero[None, None, :, None]
        * record_plus[None, None, None, :]
    )
    check(
        "one or two decoupled spectator records preserve pair probability and norm",
        np.allclose(np.sum(np.abs(one_record) ** 2, axis=2), np.abs(packet) ** 2, atol=2e-12)
        and np.allclose(np.sum(np.abs(two_records) ** 2, axis=(2, 3)), np.abs(packet) ** 2, atol=2e-12),
    )


def weak_force_packet_convergence() -> None:
    settings = ((0.08, 0.003), (0.06, 0.002), (0.04, 0.001), (0.03, 0.0005))
    errors = []
    for width, force in settings:
        response = pair_response(
            1.0,
            total_momentum_width=width,
            force_per_constituent=force,
        )
        errors.append(abs(response.measured_mass / response.expected_mass - 1))
    check(
        "composite F/a converges as total push and momentum width shrink",
        all(errors[index + 1] < errors[index] for index in range(len(errors) - 1))
        and errors[-1] < 3e-4,
        errors,
    )


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    unique = {tuple(frame.reshape(-1)): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


def bound_energy_3d(
    total_momentum: np.ndarray,
    hopping: float,
    attraction: float,
    relative_length: int,
) -> tuple[float, float]:
    relative_momenta = wrapped_momenta(relative_length)
    relative_grid = np.meshgrid(
        relative_momenta, relative_momenta, relative_momenta, indexing="ij"
    )
    continuum = sum(
        -4
        * hopping
        * np.cos(float(total_momentum[axis]) / 2)
        * np.cos(relative_grid[axis])
        for axis in range(3)
    )
    continuum_floor = float(np.min(continuum))

    def secular(energy: float) -> float:
        return float(attraction * np.mean(1 / (continuum - energy)) - 1)

    lower = continuum_floor - 20 * (attraction + 12 * hopping)
    energy = brentq(secular, lower, continuum_floor - 1e-11, xtol=1e-13)
    return float(energy), continuum_floor


def cubic_bound_sector_controls() -> None:
    hopping = 0.5
    attraction = 6.0
    relative_length = 17
    origin = np.zeros(3)
    energy, continuum_floor = bound_energy_3d(
        origin, hopping, attraction, relative_length
    )
    check(
        "proper-cubic onsite attraction has a finite-grid bound sector",
        continuum_floor - energy > 1,
        {"energy": energy, "continuum_floor": continuum_floor},
    )

    finite_sizes = [
        bound_energy_3d(origin, hopping, attraction, length)[0]
        for length in (13, 17, 21)
    ]
    check(
        "proper-cubic bound energy is stable under relative-volume enlargement",
        abs(finite_sizes[-1] - finite_sizes[-2]) < 3e-8
        and abs(finite_sizes[-2] - finite_sizes[-3]) < 3e-6,
        finite_sizes,
    )

    probe = np.array([0.17, -0.11, 0.07])
    rotated_energies = [
        bound_energy_3d(frame @ probe, hopping, attraction, relative_length)[0]
        for frame in proper_cubic_frames()
    ]
    check(
        "bound band is invariant under all 24 proper-cubic frames",
        max(rotated_energies) - min(rotated_energies) < 2e-12,
        max(rotated_energies) - min(rotated_energies),
    )

    step = 0.03
    axis_curvatures = []
    for axis in range(3):
        displacement = np.zeros(3)
        displacement[axis] = step
        plus = bound_energy_3d(displacement, hopping, attraction, relative_length)[0]
        minus = bound_energy_3d(-displacement, hopping, attraction, relative_length)[0]
        axis_curvatures.append((plus - 2 * energy + minus) / step**2)
    check(
        "proper-cubic composite mass tensor is isotropic",
        max(axis_curvatures) - min(axis_curvatures) < 2e-10
        and min(axis_curvatures) > 0,
        axis_curvatures,
    )

    retained = []
    for candidate_attraction in (5.0, 6.0, 8.0):
        candidate_energy, candidate_floor = bound_energy_3d(
            origin, hopping, candidate_attraction, relative_length
        )
        retained.append(candidate_floor - candidate_energy)
    check(
        "cubic locality and binding retain multiple interaction strengths",
        all(gap > 0.3 for gap in retained) and len({round(gap, 8) for gap in retained}) == 3,
        retained,
    )


def rest_gap_offset_control() -> None:
    hopping = 0.5
    attraction = 1.0
    bound_rest = float(bound_energy_1d(0.0, hopping, attraction))
    inertial_mass = bound_mass_1d(hopping, attraction)
    onsite_costs = (2.0, 3.0)
    rest_gaps = tuple(2 * cost + bound_rest for cost in onsite_costs)
    check(
        "onsite rest offset changes rest gap without changing composite inertia",
        rest_gaps[0] != rest_gaps[1]
        and all(abs(inertial_mass - bound_mass_1d(hopping, attraction)) < 1e-12 for _ in onsite_costs),
        {"rest_gaps": rest_gaps, "inertial_mass": inertial_mass},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    exact_bound_band_contract()
    local_generator_controls()
    results = direct_composite_tournament()
    deletion_redundancy_and_schedule_controls(results)
    weak_force_packet_convergence()
    cubic_bound_sector_controls()
    rest_gap_offset_control()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "LOCALLY_BOUND_COMPOSITE_MASS_BRIDGE" if FAIL == 0 else "CYCLE203_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
