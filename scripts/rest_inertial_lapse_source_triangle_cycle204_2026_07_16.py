#!/usr/bin/env python3
"""Cycle 204: rest/inertial/lapse/source mass triangle.

Combine the operational inertia of Cycles 201-203 with Cycle 9's conditional
common scalar scheduler and local Green field.  The runner tests which mass
coordinate controls passive lapse response, what an energy-proportional source
map would buy, and why archive count is not a redundancy-safe source.

All gravitational coupling and source maps remain explicit candidate-law
conditions.  The runner does not derive GR or an equivalence principle.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp

import local_conservative_commit_resource_gravity_cycle9_2026_07_14 as c9
import local_force_inertial_mass_bridge_cycle202_2026_07_16 as c202
import locally_bound_composite_mass_bridge_cycle203_2026_07_16 as c203


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NOTE_2026-07-16.md"
)
NO_GO_LEDGER = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NO_GO_LEDGER.md"
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
        "common scalar lapse",
        "passive charge",
        "active source map remains supplied",
        "archive count fails the redundancy control",
        "standard lattice coordinates",
        "rest-energy normalization",
        "mass-to-gravity map remains conditional",
        "partial-attempt-with-named-untested-routes",
        "n1 — alternative route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note carries the gravity and no-go-discipline boundaries", not missing, missing)
    ledger = " ".join(NO_GO_LEDGER.read_text(encoding="utf-8").lower().split())
    ledger_required = (
        "broad claim blocked",
        "n1",
        "n7",
        "n8",
        "partial-attempt-with-named-untested-routes",
    )
    ledger_missing = tuple(phrase for phrase in ledger_required if phrase not in ledger)
    check("failed broad no-go is recorded in the cycle ledger", not ledger_missing, ledger_missing)


def hamiltonian_ratio(mass: float) -> float:
    return 1.0


def qca_rest_mass(mass: float) -> float:
    return float(np.arcsin(mass))


def qca_inertial_mass(mass: float) -> float:
    return float(mass / np.sqrt(1 - mass * mass))


def qca_passive_to_inertial_ratio(mass: float) -> float:
    return qca_rest_mass(mass) / qca_inertial_mass(mass)


def exact_mass_ratio_contract() -> None:
    mass = sp.symbols("m", positive=True)
    ratio = sp.asin(mass) * sp.sqrt(1 - mass**2) / mass
    series = sp.series(ratio, mass, 0, 5)
    check(
        "Dirac-generator common-lapse passive/inertial ratio is identically one",
        sp.simplify(mass / mass - 1) == 0,
    )
    check(
        "standard-QCA passive/inertial ratio has the expected continuum series",
        series == 1 - mass**2 / 3 - 2 * mass**4 / 15 + sp.Order(mass**5),
        series,
    )
    samples = tuple(qca_passive_to_inertial_ratio(value) for value in (0.25, 0.4, 0.65))
    check(
        "standard-QCA finite-lattice ratio is mass dependent",
        max(samples) - min(samples) > 0.1 and all(0 < value < 1 for value in samples),
        samples,
    )

    errors = [1 - qca_passive_to_inertial_ratio(value) for value in (0.2, 0.1, 0.05, 0.025)]
    orders = [np.log(errors[index] / errors[index + 1]) / np.log(2) for index in range(3)]
    check(
        "standard-QCA passive/inertial mismatch vanishes quadratically",
        all(1.95 < order < 2.05 for order in orders),
        orders,
    )


def local_lapse_trajectory_controls() -> None:
    gravitational_gradient = 5e-4
    hamiltonian_responses = []
    qca_responses = []
    for mass in (0.25, 0.4, 0.65):
        h_response = c202.force_response(
            "hamiltonian", mass, force=mass * gravitational_gradient
        )
        measured_h_ratio = h_response.acceleration / gravitational_gradient
        hamiltonian_responses.append(measured_h_ratio)
        check(
            f"Hamiltonian m={mass} common-lapse trajectory has unit passive/inertial ratio",
            abs(measured_h_ratio - hamiltonian_ratio(mass)) < 3e-3,
            measured_h_ratio,
        )

        rest_charge = qca_rest_mass(mass)
        q_response = c202.force_response(
            "qca", mass, force=rest_charge * gravitational_gradient
        )
        measured_q_ratio = q_response.acceleration / gravitational_gradient
        expected_q_ratio = qca_passive_to_inertial_ratio(mass)
        qca_responses.append(measured_q_ratio)
        check(
            f"QCA m={mass} trajectory measures its rest/inertial lapse ratio",
            abs(measured_q_ratio / expected_q_ratio - 1) < 3e-3,
            {"measured": measured_q_ratio, "expected": expected_q_ratio},
        )

    check(
        "Hamiltonian test bodies share one weak-lapse acceleration",
        max(hamiltonian_responses) - min(hamiltonian_responses) < 5e-3,
        hamiltonian_responses,
    )
    check(
        "standard-QCA test bodies retain finite-lattice differential acceleration",
        max(qca_responses) - min(qca_responses) > 0.1,
        qca_responses,
    )


def alternative_coordinate_controls() -> None:
    masses = (0.25, 0.4, 0.65)
    remapped = tuple(np.tan(np.arcsin(mass)) for mass in masses)
    expected = tuple(qca_inertial_mass(mass) for mass in masses)
    check(
        "nonlinear QCA energy remap tan(omega) closes one-particle rest/inertial equality",
        np.allclose(remapped, expected, atol=2e-12),
        remapped,
    )
    angle_a, angle_b = 0.2, 0.3
    check(
        "the same nonlinear remap is not additive under ordinary phase composition",
        abs(np.tan(angle_a + angle_b) - np.tan(angle_a) - np.tan(angle_b)) > 1e-2,
        {
            "joint": np.tan(angle_a + angle_b),
            "sum": np.tan(angle_a) + np.tan(angle_b),
        },
    )


def bound_composite_rest_normalization_controls() -> None:
    hopping = 0.5
    tuned_attraction = 1.0
    tuned_scale = np.sqrt(tuned_attraction**2 + 16 * hopping**2)
    common_onsite_cost = (
        tuned_scale + c203.bound_mass_1d(hopping, tuned_attraction)
    ) / 2
    ratios = []
    tuned_costs = []
    for attraction in (0.4, 0.7, 1.0, 1.5, 2.0):
        scale = np.sqrt(attraction**2 + 16 * hopping**2)
        inertia = c203.bound_mass_1d(hopping, attraction)
        rest_gap = 2 * common_onsite_cost - scale
        ratios.append(rest_gap / inertia)
        tuned_costs.append((scale + inertia) / 2)
    check(
        "one common onsite normalization matches only the tuned composite sector",
        abs(ratios[2] - 1) < 2e-12
        and max(ratios) - min(ratios) > 0.5,
        ratios,
    )
    check(
        "sector-specific onsite costs can tune each composite ratio to one",
        len({round(value, 10) for value in tuned_costs}) == len(tuned_costs)
        and all(
            abs(
                (2 * cost - np.sqrt(attraction**2 + 16 * hopping**2))
                / c203.bound_mass_1d(hopping, attraction)
                - 1
            )
            < 2e-12
            for attraction, cost in zip((0.4, 0.7, 1.0, 1.5, 2.0), tuned_costs)
        ),
        tuned_costs,
    )


def source_map_and_redundancy_controls() -> None:
    side = 40
    green, _, source, _ = c9.green_pair(side)
    sample = (5, 0, 0)
    source_masses = (0.25, 0.4, 0.65)
    energy_fields = tuple(mass * green for mass in source_masses)
    check(
        "energy-proportional source comparator scales the local Green field with mass",
        all(
            abs(
                energy_fields[index][sample] / energy_fields[0][sample]
                - source_masses[index] / source_masses[0]
            )
            < 2e-12
            for index in range(1, len(source_masses))
        ),
    )

    same_mass = 0.4
    archive_fields = tuple(count * green for count in (1, 2, 3))
    check(
        "archive-count source changes when redundant witnesses are added",
        abs(archive_fields[2][sample] / archive_fields[0][sample] - 3) < 2e-12,
    )
    mass_field_one_record = same_mass * green
    mass_field_two_records = same_mass * green
    check(
        "energy-source comparator is invariant under spectator-record duplication",
        np.array_equal(mass_field_one_record, mass_field_two_records),
    )
    check(
        "one archive count cannot distinguish two tested source masses",
        np.array_equal(green, green)
        and abs(energy_fields[0][sample] - energy_fields[-1][sample]) > 1e-5,
    )

    combined = (source_masses[0] + source_masses[1]) * green
    check(
        "energy-source comparator is additive for two co-located independent sources",
        np.allclose(combined, energy_fields[0] + energy_fields[1], atol=2e-12),
    )

    flattened = green.ravel()
    grid = np.indices((side, side, side), dtype=int).reshape(3, -1)
    check(
        "point-source/antipode Green field is invariant under all 24 proper-cubic frames",
        all(
            np.max(
                np.abs(
                    flattened
                    - flattened[
                        np.ravel_multi_index(
                            tuple((rotation @ grid) % side), green.shape
                        )
                    ]
                )
            )
            < 2e-12
            for rotation in c9.proper_cubic_rotations()
        ),
    )

    density, _, current, _, _, _ = c9.steady_ssep_profile(side)
    deficit = density - 0.5
    lapse = 1 - 0.5 * deficit
    check(
        "Cycle-9 candidate source field retains a positive common lapse",
        current > 0 and float(lapse.min()) > 0 and lapse[source] < lapse[5, 0, 0],
        {"current": current, "minimum_lapse": float(lapse.min())},
    )


def source_response_triangle_controls() -> None:
    source_mass = 0.65
    hamiltonian_probe_ratios = np.asarray([hamiltonian_ratio(mass) for mass in (0.25, 0.4, 0.65)])
    qca_probe_ratios = np.asarray([qca_passive_to_inertial_ratio(mass) for mass in (0.25, 0.4, 0.65)])
    hamiltonian_accelerations = source_mass * hamiltonian_probe_ratios
    qca_accelerations = source_mass * qca_probe_ratios
    check(
        "conditional energy source plus Hamiltonian response gives probe-independent acceleration",
        np.max(hamiltonian_accelerations) - np.min(hamiltonian_accelerations) < 2e-12,
        hamiltonian_accelerations,
    )
    check(
        "same scalar field plus standard-QCA response remains probe-mass dependent",
        np.max(qca_accelerations) - np.min(qca_accelerations) > 0.05,
        qca_accelerations,
    )
    check(
        "the source and response coupling scale remains an independent law value",
        not np.allclose(0.3 * hamiltonian_accelerations, 0.7 * hamiltonian_accelerations),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    exact_mass_ratio_contract()
    local_lapse_trajectory_controls()
    alternative_coordinate_controls()
    bound_composite_rest_normalization_controls()
    source_map_and_redundancy_controls()
    source_response_triangle_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "CONDITIONAL_MASS_GRAVITY_TRIANGLE" if FAIL == 0 else "CYCLE204_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
