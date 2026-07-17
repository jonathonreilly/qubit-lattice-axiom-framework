#!/usr/bin/env python3
"""Cycle 218: normalize rest, inertia, and exchange on one acoustic cone.

Cycle 215 fixes the candidate field acoustic speed to c^2=1/3 in lattice
units.  Replace the coordinate equality rest_phase=m_inertial with the
unit-covariant relation E_rest=m_inertial c^2.  Build the corresponding
proper-cubic SU(6) molecule family and test rest mass, dispersion mass, forced
inertia, static exchange charge, composition, covariance, and ablations.

The common-cone relation remains a candidate physical condition.  No axiom or
empirical Lorentz/GR conclusion is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COMMON_ACOUSTIC_CONE_MASS_CYCLE218_NOTE_2026-07-16.md"
)

C_SQUARED = 1 / 3
COUPLING = 0.025
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


@dataclass(frozen=True)
class ConeSpecies:
    beta: float
    alpha: float
    rest_energy: float
    inertial_mass: float
    coin: np.ndarray


def cone_species(beta: float) -> ConeSpecies:
    inertial_mass = float(3 * np.tan(-beta / 2))
    rest_energy = C_SQUARED * inertial_mass
    alpha = float((-6 * rest_energy - 3 * beta) / 2)
    return ConeSpecies(
        beta,
        alpha,
        rest_energy,
        inertial_mass,
        c210.cubic_coin(alpha, beta, rest_energy),
    )


def as_cycle210(species: ConeSpecies) -> c210.Species:
    return c210.Species(
        species.beta,
        species.alpha,
        species.rest_energy,
        species.inertial_mass,
        species.coin,
    )


def vacuum_relative_energy(species: ConeSpecies) -> float:
    scalar_eigenvalue = np.trace(c210.P_SCALAR @ species.coin)
    return float(np.angle(scalar_eigenvalue))


def exchange_charge(species: ConeSpecies) -> float:
    return vacuum_relative_energy(species) / C_SQUARED


def field_acoustic_speed() -> tuple[float, ...]:
    step = 1e-4
    directions = (
        np.array((1.0, 0.0, 0.0)),
        np.array((1.0, 1.0, 0.0)) / np.sqrt(2),
        np.array((1.0, 1.0, 1.0)) / np.sqrt(3),
    )
    slopes = []
    for direction in directions:
        momentum = step * direction
        walk = np.diag(
            np.exp(-1j * (c210.DIRECTIONS @ momentum))
        ) @ c214.FIELD_COIN
        phases = np.angle(np.linalg.eigvals(walk))
        slopes.append(float(min(value for value in phases if value > 1e-8) / step))
    return tuple(slopes)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "common acoustic cone",
        "c^2=1/3",
        "e_rest=m_inertial c^2",
        "exchange charge e_rest/c^2",
        "rest mass",
        "dispersion mass",
        "forced inertia",
        "species-independent exchange response",
        "unit-covariant correction",
        "condition remains supplied",
        "not an empirical lorentz theorem",
        "no axiom conclusion",
        "thirring-qca",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves correction, attribution, and scope", not missing, missing)


def common_cone_controls() -> tuple[ConeSpecies, ...]:
    slopes = field_acoustic_speed()
    check(
        "the selected field has one isotropic acoustic cone with c^2=1/3",
        max(abs(value**2 - C_SQUARED) for value in slopes) < 3e-8,
        slopes,
    )

    species_set = tuple(cone_species(beta) for beta in (-0.2, -0.3, -0.4))
    rows = []
    for species in species_set:
        cycle_species = as_cycle210(species)
        curvature = c210.curvature_tensor(cycle_species, step=1e-5)
        dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
        rest_mass = vacuum_relative_energy(species) / C_SQUARED
        determinant_phase = float(np.angle(np.linalg.det(species.coin)))
        rows.append(
            {
                "beta": species.beta,
                "alpha": species.alpha,
                "rest_energy": species.rest_energy,
                "rest_mass": rest_mass,
                "dispersion_mass": dispersion_mass,
                "target": species.inertial_mass,
            }
        )
        check(
            f"beta={species.beta} rest/c^2 equals independent dispersion mass",
            abs(rest_mass / species.inertial_mass - 1) < 2e-12
            and abs(dispersion_mass / species.inertial_mass - 1) < 8e-6
            and abs(determinant_phase) < 2e-12,
            rows[-1],
        )
        check(
            f"beta={species.beta} cone-aligned molecule and contact law stay unitary",
            np.linalg.norm(species.coin.conj().T @ species.coin - np.eye(6)) < 2e-12
            and np.linalg.norm(
                c210.interaction_correction(cycle_species).conj().T
                @ c210.interaction_correction(cycle_species)
                - np.eye(36)
            )
            < 3e-12,
        )

    held_out = cone_species(-0.35)
    held_curvature = c210.curvature_tensor(as_cycle210(held_out), step=1e-5)
    held_mass = 1 / float(np.mean(np.diag(held_curvature)))
    check(
        "a held-out species obeys the common-cone rest/curvature identity",
        abs(exchange_charge(held_out) / held_mass - 1) < 8e-6,
        {"charge": exchange_charge(held_out), "curvature_mass": held_mass},
    )

    frame_residuals = []
    reference = species_set[-1]
    for frame in c210.proper_cubic_frames():
        representation = c210.direction_permutation(frame)
        frame_residuals.append(
            np.linalg.norm(
                representation @ reference.coin @ representation.conj().T
                - reference.coin
            )
        )
    check(
        "the common-cone matter family remains covariant in all cubic frames",
        max(frame_residuals) < 2e-12,
        max(frame_residuals),
    )

    check(
        "the SU(6) even-sector phase becomes only a higher-order cone correction",
        all(
            abs(
                species.alpha
                - 3 * (np.tan(species.beta / 2) - species.beta / 2)
            )
            < 2e-12
            for species in species_set
        )
        and max(abs(species.alpha) for species in species_set) < 0.01,
        [species.alpha for species in species_set],
    )
    return species_set


def tangent_lorentz_controls(species_set: tuple[ConeSpecies, ...]) -> None:
    rows = []
    for species in species_set:
        cycle_species = as_cycle210(species)
        for momentum_value in (0.0001, 0.0003, 0.001):
            momentum = np.array((momentum_value, 0.0, 0.0))
            observed = c210.phase_near_origin(momentum, cycle_species)
            tangent = species.rest_energy + momentum_value**2 / (
                2 * species.inertial_mass
            )
            relativistic = np.sqrt(
                species.rest_energy**2 + C_SQUARED * momentum_value**2
            )
            rows.append(
                (
                    species.beta,
                    momentum_value,
                    abs(observed - tangent),
                    abs(observed - relativistic),
                )
            )
    small = [row for row in rows if row[1] == 0.0001]
    large = [row for row in rows if row[1] == 0.001]
    check(
        "the molecular band shares the acoustic relativistic tangent through p^2",
        max(row[3] for row in small) < 8e-13
        and all(
            large[index][3] > small[index][3]
            for index in range(len(small))
        ),
        rows,
    )


def inertia_and_exchange_controls(species_set: tuple[ConeSpecies, ...]) -> None:
    inertia_rows = []
    for species in species_set:
        response = c210.force_response(
            as_cycle210(species),
            2e-6,
            length=8192,
            momentum_width=0.0012,
            duration=150,
        )
        inertia_rows.append(
            (
                species.beta,
                response.measured_mass,
                species.inertial_mass,
                exchange_charge(species),
                response.band_probability,
            )
        )
    check(
        "forced inertia, dispersion mass, and E_rest/c^2 exchange charge agree",
        max(abs(row[1] / row[2] - 1) for row in inertia_rows) < 0.006
        and max(abs(row[3] / row[2] - 1) for row in inertia_rows) < 2e-12
        and min(row[4] for row in inertia_rows) > 0.999,
        inertia_rows,
    )

    side = 31
    kernel = 3 * c211.solve_field(c211.point_source(side))
    separation = (4, 0, 0)
    field_gradient = c211.gradient(kernel, separation)[0]
    source = species_set[-1]
    source_charge = exchange_charge(source)
    response_rows = []
    for species in species_set:
        charge = exchange_charge(species)
        force = COUPLING**2 * source_charge * charge * field_gradient
        response = c210.force_response(
            as_cycle210(species),
            force,
            length=8192,
            momentum_width=0.0012,
            duration=150,
        )
        expected = -COUPLING**2 * source_charge * field_gradient
        response_rows.append(
            (
                species.beta,
                charge,
                response.measured_mass,
                response.acceleration / expected,
            )
        )
    check(
        "the common-cone charge gives species-independent exchange response",
        max(abs(row[3] - 1) for row in response_rows) < 0.007,
        response_rows,
    )

    for species in species_set:
        pair_energy = 2 * species.rest_energy
        pair_mass = pair_energy / C_SQUARED
        check(
            f"beta={species.beta} two-object composition adds rest and inertial mass",
            abs(pair_mass / (2 * species.inertial_mass) - 1) < 2e-12,
            {"pair_rest_energy": pair_energy, "pair_mass": pair_mass},
        )

    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    charge = exchange_charge(source)
    archived = (
        charge,
        charge * np.vdot(record_zero, record_zero).real,
        charge
        * np.vdot(record_zero, record_zero).real
        * np.vdot(record_plus, record_plus).real,
    )
    check(
        "spectator record redundancy leaves common-cone mass and charge unchanged",
        max(abs(value - charge) for value in archived) < 2e-14,
        archived,
    )


def convention_and_ablation_controls(species_set: tuple[ConeSpecies, ...]) -> None:
    old_rows = []
    for beta in (-0.2, -0.3, -0.4):
        old = c210.tuned_species(beta)
        rest_mass_on_common_cone = old.rest_phase / C_SQUARED
        old_rows.append(rest_mass_on_common_cone / old.analytic_mass)
    check(
        "the prior numeric rest=mass tuning is a c=1 convention, not common-cone equality",
        max(abs(value - 3) for value in old_rows) < 2e-12,
        old_rows,
    )

    shifted_rows = []
    for species in species_set:
        shifted_energy = species.rest_energy + 0.03
        shifted_coin = c210.cubic_coin(
            species.alpha - 0.09,
            species.beta,
            shifted_energy,
        )
        shifted = ConeSpecies(
            species.beta,
            species.alpha - 0.09,
            shifted_energy,
            species.inertial_mass,
            shifted_coin,
        )
        shifted_rows.append(exchange_charge(shifted) / shifted.inertial_mass)
    check(
        "unitarity and SU(6) do not by themselves force common-cone mass alignment",
        max(shifted_rows) - min(shifted_rows) > 0.09
        and all(
            np.linalg.norm(
                c210.cubic_coin(
                    species.alpha - 0.09,
                    species.beta,
                    species.rest_energy + 0.03,
                ).conj().T
                @ c210.cubic_coin(
                    species.alpha - 0.09,
                    species.beta,
                    species.rest_energy + 0.03,
                )
                - np.eye(6)
            )
            < 2e-12
            for species in species_set
        ),
        shifted_rows,
    )

    reference = species_set[-1]
    lifted_coin = c210.cubic_coin(
        reference.alpha + 2 * np.pi,
        reference.beta + 2 * np.pi,
        reference.rest_energy + 2 * np.pi,
    )
    lifted = ConeSpecies(
        reference.beta + 2 * np.pi,
        reference.alpha + 2 * np.pi,
        reference.rest_energy + 2 * np.pi,
        reference.inertial_mass,
        lifted_coin,
    )
    check(
        "a 2pi coordinate lift changes neither the coin nor principal rest mass",
        np.linalg.norm(lifted.coin - reference.coin) < 2e-12
        and abs(exchange_charge(lifted) - exchange_charge(reference)) < 2e-12,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    species_set = common_cone_controls()
    tangent_lorentz_controls(species_set)
    inertia_and_exchange_controls(species_set)
    convention_and_ablation_controls(species_set)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
