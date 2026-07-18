#!/usr/bin/env python3
"""Multi-tick delayed-recontact execution of the carried internal-source code.

Extend the inherited one-matter, Q=N_e+N_f=1 direct hard-core code through a
joint lattice history with the common matter coin/stream, the local
e <-> g+scalar-field exchange, and the finite field coin/stream.  The runner
records local charge transfer, directed edge currents, and colocated scalar
contact weight.  Here "retarded" means only that the local effect occurs after
intervening update/stream ticks; the state has no path-provenance register.  It
does not splice this direct code into Cycle 269 or call Q energy, stress, a
clock rate, or a gravitational source.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import carried_internal_species_source_field_ledger_repair_2026_07_17 as carried
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CARRIED_SOURCE_RETARDED_LATTICE_EXECUTION_NOTE_2026-07-17.md"
)

BETA = -0.3
MEDIATOR_COUPLING = 0.8
CONTACT_COUPLING = 0.37
TOLERANCE = 6e-11

Position = tuple[int, int, int]

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


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "q=n_e+n_f=1",
        "matter coin",
        "matter stream",
        "local exchange",
        "field stream",
        "six-tick",
        "means only that a local effect occurs",
        "delayed colocated recontact",
        "-0.0067710042558824495",
        "coherent interference",
        "squared-norm sector weights",
        "delta n_f",
        "local/global q",
        "all 24 proper-cubic frames",
        "held l=13,15",
        "mass fixture",
        "deletion",
        "not energy",
        "not the cycle-269",
        "no full-fock",
        "declared direct carried hard-core code",
        "no contact layer is applied",
        "supplied structure",
        "no no-go claim",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the delayed-recontact direct-code scope and boundaries",
        not missing,
        missing,
    )


def add_position(position: Position, direction: int, side: int | None = None) -> Position:
    moved = tuple(
        int(position[axis] + c210.DIRECTIONS[direction, axis])
        for axis in range(3)
    )
    if side is None:
        return moved
    return tuple(value % side for value in moved)


def state_scale(state: carried.CarriedState, coefficient: complex) -> carried.CarriedState:
    return carried.CarriedState(
        {key: coefficient * value for key, value in state.excited.items()},
        {key: coefficient * value for key, value in state.pair.items()},
    )


def state_normalized(state: carried.CarriedState) -> carried.CarriedState:
    return state_scale(state, 1 / np.sqrt(carried.state_norm(state)))


def periodic_body_stream(
    state: carried.CarriedState, side: int
) -> tuple[
    carried.CarriedState,
    dict[tuple[Position, int], float],
    dict[tuple[Position, int], float],
]:
    excited: dict[Position, np.ndarray] = {}
    pair: dict[tuple[Position, Position], np.ndarray] = {}
    matter_current: defaultdict[tuple[Position, int], float] = defaultdict(float)
    excitation_current: defaultdict[tuple[Position, int], float] = defaultdict(float)
    for body, value in state.excited.items():
        for direction in range(6):
            destination = add_position(body, direction, side)
            excited.setdefault(destination, carried.zero_vector())[direction] += value[
                direction
            ]
            amount = float(abs(value[direction]) ** 2)
            matter_current[(body, direction)] += amount
            excitation_current[(body, direction)] += amount
    for (body, field), value in state.pair.items():
        for direction in range(6):
            destination = add_position(body, direction, side)
            pair.setdefault((destination, field), carried.zero_pair())[
                direction, :
            ] += value[direction, :]
            matter_current[(body, direction)] += float(
                np.vdot(value[direction, :], value[direction, :]).real
            )
    return (
        carried.CarriedState(excited, pair),
        dict(matter_current),
        dict(excitation_current),
    )


def periodic_field_stream(
    state: carried.CarriedState, side: int
) -> tuple[carried.CarriedState, dict[tuple[Position, int], float]]:
    pair: dict[tuple[Position, Position], np.ndarray] = {}
    current: defaultdict[tuple[Position, int], float] = defaultdict(float)
    for (body, field), value in state.pair.items():
        for direction in range(6):
            destination = add_position(field, direction, side)
            pair.setdefault((body, destination), carried.zero_pair())[
                :, direction
            ] += value[:, direction]
            current[(field, direction)] += float(
                np.vdot(value[:, direction], value[:, direction]).real
            )
    return (
        carried.CarriedState(
            {key: value.copy() for key, value in state.excited.items()}, pair
        ),
        dict(current),
    )


def incoming_density(
    current: dict[tuple[Position, int], float], side: int | None = None
) -> dict[Position, float]:
    density: defaultdict[Position, float] = defaultdict(float)
    for (source, direction), value in current.items():
        density[add_position(source, direction, side)] += value
    return dict(density)


def add_densities(
    left: dict[Position, float], right: dict[Position, float]
) -> dict[Position, float]:
    result: defaultdict[Position, float] = defaultdict(float)
    for source in (left, right):
        for key, value in source.items():
            result[key] += value
    return dict(result)


def embed_periodic(state: carried.CarriedState, side: int) -> carried.CarriedState:
    center = side // 2

    def move(position: Position) -> Position:
        return tuple((value + center) % side for value in position)

    excited: dict[Position, np.ndarray] = {}
    pair: dict[tuple[Position, Position], np.ndarray] = {}
    for position, value in state.excited.items():
        excited.setdefault(move(position), carried.zero_vector())[:] += value
    for (body, field), value in state.pair.items():
        pair.setdefault((move(body), move(field)), carried.zero_pair())[:] += value
    return carried.CarriedState(excited, pair)


@dataclass(frozen=True)
class TickReport:
    tick: int
    norm_residual: float
    coin_q_residual: float
    vertex_q_residual: float
    matter_edge_residual: float
    q_edge_residual: float
    global_q_residual: float
    field_sector_weight: float
    excited_sector_weight: float
    source_sum: float
    minimum_local_source: float
    negative_source_cells: int
    colocated_scalar_contact: float
    diagonal_emission: float
    diagonal_field_depletion: float
    coherent_interference: float
    component_residual: float
    origin_source: float
    origin_colocated_scalar: float
    origin_emission: float
    origin_field_depletion: float
    origin_interference: float


def exchange_components(
    coined: carried.CarriedState, angle: float
) -> tuple[
    dict[Position, tuple[float, float, float, float]],
    float,
    float,
    float,
    float,
]:
    sine = np.sin(angle)
    cosine = np.cos(angle)
    positions = set(coined.excited)
    positions.update(body for body, field in coined.pair if body == field)
    rows: dict[Position, tuple[float, float, float, float]] = {}
    totals = np.zeros(4, dtype=float)
    for position in positions:
        excited = coined.excited.get(position, carried.zero_vector())
        pair = coined.pair.get((position, position), carried.zero_pair())
        colocated_scalar = pair @ c210.UNIFORM
        excited_weight = float(np.vdot(excited, excited).real)
        colocated_weight = float(np.vdot(colocated_scalar, colocated_scalar).real)
        emission = float(sine**2 * excited_weight)
        field_depletion = float(-sine**2 * colocated_weight)
        interference = float(
            2 * sine * cosine * np.imag(np.vdot(excited, colocated_scalar))
        )
        rows[position] = (
            colocated_weight,
            emission,
            field_depletion,
            interference,
        )
        totals += (colocated_weight, emission, field_depletion, interference)
    return rows, *tuple(float(value) for value in totals)


def joint_step(
    state: carried.CarriedState,
    species: c210.Species,
    angle: float,
    tick: int,
    side: int | None = None,
) -> tuple[carried.CarriedState, TickReport]:
    before_norm = carried.state_norm(state)
    before_q = carried.q_density(state)
    coined = carried.coin_gate(state, species.coin, c214.FIELD_COIN)
    coin_q_residual = carried.density_residual(carried.q_density(coined), before_q)
    (
        component_rows,
        colocated_scalar,
        diagonal_emission,
        diagonal_field_depletion,
        interference,
    ) = exchange_components(coined, angle)
    sourced, source_current, vertex_q_residual = carried.vertex_gate(coined, angle)

    if side is None:
        matter_moved, matter_current, excitation_current = carried.body_stream(sourced)
        output, field_current = carried.field_stream(matter_moved)
    else:
        matter_moved, matter_current, excitation_current = periodic_body_stream(
            sourced, side
        )
        output, field_current = periodic_field_stream(matter_moved, side)

    matter_target = incoming_density(matter_current, side)
    q_target = add_densities(
        incoming_density(excitation_current, side),
        incoming_density(field_current, side),
    )
    values = tuple(source_current.values())
    component_residual = max(
        (
            abs(
                source_current.get(position, 0.0)
                - sum(component_rows.get(position, (0.0, 0.0, 0.0, 0.0))[1:])
            )
            for position in source_current.keys() | component_rows.keys()
        ),
        default=0.0,
    )
    origin = (0, 0, 0) if side is None else (side // 2,) * 3
    origin_components = component_rows.get(origin, (0.0, 0.0, 0.0, 0.0))
    q_total = sum(carried.q_density(output).values())
    field_sector_weight = sum(carried.field_density(output).values())
    excited_sector_weight = sum(carried.excitation_density(output).values())
    return output, TickReport(
        tick=tick,
        norm_residual=abs(carried.state_norm(output) - before_norm),
        coin_q_residual=coin_q_residual,
        vertex_q_residual=vertex_q_residual,
        matter_edge_residual=carried.density_residual(
            carried.matter_density(matter_moved), matter_target
        ),
        q_edge_residual=carried.density_residual(carried.q_density(output), q_target),
        global_q_residual=abs(q_total - before_norm),
        field_sector_weight=field_sector_weight,
        excited_sector_weight=excited_sector_weight,
        source_sum=float(sum(values)),
        minimum_local_source=float(min(values, default=0.0)),
        negative_source_cells=sum(value < -1e-14 for value in values),
        colocated_scalar_contact=colocated_scalar,
        diagonal_emission=diagonal_emission,
        diagonal_field_depletion=diagonal_field_depletion,
        coherent_interference=interference,
        component_residual=component_residual,
        origin_source=float(source_current.get(origin, 0.0)),
        origin_colocated_scalar=origin_components[0],
        origin_emission=origin_components[1],
        origin_field_depletion=origin_components[2],
        origin_interference=origin_components[3],
    )


def local_and_global_charge_controls(angle: float) -> None:
    exchange, vertex, charge = carried.active_blocks(angle)
    check(
        "the inherited 42-state local exchange is unitary and exactly preserves Q",
        np.linalg.norm(vertex.conj().T @ vertex - np.eye(42)) < 3e-12
        and np.linalg.norm(vertex @ charge - charge @ vertex) < 3e-12
        and np.linalg.norm(exchange @ charge - charge @ exchange) < 3e-12,
        {
            "unitarity_residual": np.linalg.norm(
                vertex.conj().T @ vertex - np.eye(42)
            ),
            "charge_commutator": np.linalg.norm(vertex @ charge - charge @ vertex),
        },
    )


def randomized_exchange_decomposition_controls(angle: float) -> None:
    """Check direct Delta N_f against the exact coherent decomposition."""
    rng = np.random.default_rng(2026071703)
    sine = np.sin(angle)
    cosine = np.cos(angle)
    residuals = []
    charge_residuals = []
    for _case in range(48):
        excited = rng.normal(size=6) + 1j * rng.normal(size=6)
        colocated_scalar = rng.normal(size=6) + 1j * rng.normal(size=6)
        colocated_scalar *= np.exp(1j * rng.uniform(-np.pi, np.pi))
        raw_transverse = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
        transverse = raw_transverse - np.outer(
            raw_transverse @ c210.UNIFORM, c210.UNIFORM.conj()
        )
        pair = transverse + np.outer(
            colocated_scalar, c210.UNIFORM.conj()
        )
        new_excited, new_pair = carried.local_vertex(excited, pair, angle)
        direct_delta_field = float(
            np.vdot(new_pair, new_pair).real - np.vdot(pair, pair).real
        )
        formula_delta_field = float(
            sine**2
            * (
                np.vdot(excited, excited).real
                - np.vdot(colocated_scalar, colocated_scalar).real
            )
            + 2
            * sine
            * cosine
            * np.imag(np.vdot(excited, colocated_scalar))
        )
        delta_excited = float(
            np.vdot(new_excited, new_excited).real
            - np.vdot(excited, excited).real
        )
        residuals.append(abs(direct_delta_field - formula_delta_field))
        charge_residuals.append(abs(delta_excited + direct_delta_field))
    check(
        "randomized relative phases obey the exact direct Delta N_f decomposition",
        max(residuals) < 2e-12 and max(charge_residuals) < 2e-12,
        {
            "cases": len(residuals),
            "direct_vs_formula": max(residuals),
            "Delta_Ne_plus_Delta_Nf": max(charge_residuals),
        },
    )


def six_tick_history_controls(
    species: c210.Species, angle: float
) -> tuple[list[carried.CarriedState], list[TickReport]]:
    initial = carried.CarriedState({(0, 0, 0): c210.UNIFORM.copy()}, {})
    states = [initial]
    reports: list[TickReport] = []
    state = initial
    for tick in range(1, 7):
        state, report = joint_step(state, species, angle, tick)
        states.append(state)
        reports.append(report)

    residual_keys = (
        "norm_residual",
        "coin_q_residual",
        "vertex_q_residual",
        "matter_edge_residual",
        "q_edge_residual",
        "global_q_residual",
        "component_residual",
    )
    maximum_residual = max(
        float(getattr(report, key)) for report in reports for key in residual_keys
    )
    check(
        "the six-tick joint lattice history preserves local/global Q and both edge ledgers",
        maximum_residual < TOLERANCE
        and all(
            abs(
                report.field_sector_weight
                + report.excited_sector_weight
                - 1
            )
            < TOLERANCE
            for report in reports
        ),
        {
            "maximum_residual": maximum_residual,
            "squared_norm_sector_weights": [
                (
                    report.tick,
                    report.excited_sector_weight,
                    report.field_sector_weight,
                    report.source_sum,
                )
                for report in reports
            ],
        },
    )

    tick3 = reports[2]
    tick5 = reports[4]
    check(
        "the history has delayed colocated scalar recontact and negative local Delta N_f at the origin",
        reports[0].colocated_scalar_contact < 2e-14
        and reports[1].colocated_scalar_contact > 1e-4
        and tick3.origin_colocated_scalar > 1e-3
        and tick3.origin_source < -1e-3
        and tick5.origin_source < -1e-3
        and abs(
            tick3.origin_source
            - (
                tick3.origin_emission
                + tick3.origin_field_depletion
                + tick3.origin_interference
            )
        )
        < TOLERANCE,
        {
            "first_delayed_colocated_recontact_tick": 2,
            "path_provenance": "not represented",
            "tick3_origin": {
                "colocated_scalar_weight": tick3.origin_colocated_scalar,
                "Delta_Nf": tick3.origin_source,
                "emission": tick3.origin_emission,
                "field_depletion": tick3.origin_field_depletion,
                "coherent_interference": tick3.origin_interference,
            },
            "tick5_origin_Delta_Nf": tick5.origin_source,
        },
    )
    check(
        "negative local Delta N_f does not become global net field depletion through tick six",
        all(report.source_sum > 0 for report in reports)
        and reports[-1].field_sector_weight > reports[0].field_sector_weight,
        {
            "source_sums": [report.source_sum for report in reports],
            "negative_local_cells": [
                report.negative_source_cells for report in reports
            ],
        },
    )

    occupied_bodies = {
        position
        for position, value in carried.matter_density(states[-1]).items()
        if value > TOLERANCE
    }
    occupied_fields = {
        position
        for position, value in carried.field_density(states[-1]).items()
        if value > TOLERANCE
    }
    check(
        "matter and field stay within the six-edge causal cone",
        max(map(carried.l1, occupied_bodies), default=0) <= 6
        and max(map(carried.l1, occupied_fields), default=0) <= 6,
        {
            "max_matter_l1": max(map(carried.l1, occupied_bodies), default=0),
            "max_field_l1": max(map(carried.l1, occupied_fields), default=0),
        },
    )
    return states, reports


def covariance_controls(species: c210.Species, angle: float) -> None:
    rng = np.random.default_rng(2026071702)
    random_state = state_normalized(
        carried.CarriedState(
            {
                (0, 1, -1): rng.normal(size=6) + 1j * rng.normal(size=6),
            },
            {
                ((1, 0, 0), (-1, 1, 0)): rng.normal(size=(6, 6))
                + 1j * rng.normal(size=(6, 6)),
                ((0, 0, 0), (0, 0, 0)): rng.normal(size=(6, 6))
                + 1j * rng.normal(size=(6, 6)),
            },
        )
    )
    reference = random_state
    reference_states = []
    for tick in (1, 2):
        reference, _ = joint_step(reference, species, angle, tick)
        reference_states.append(reference)
    residuals = {1: [], 2: []}
    for frame in c210.proper_cubic_frames():
        rotated = carried.rotate_state(random_state, frame)
        for tick in (1, 2):
            rotated, _ = joint_step(rotated, species, angle, tick)
            residuals[tick].append(
                carried.state_residual(
                    rotated,
                    carried.rotate_state(reference_states[tick - 1], frame),
                )
            )
    check(
        "the joint history is covariant at both tick one and tick two under all 24 proper-cubic frames",
        all(len(residuals[tick]) == 24 for tick in (1, 2))
        and max(max(residuals[tick]) for tick in (1, 2)) < TOLERANCE,
        {tick: max(residuals[tick]) for tick in (1, 2)},
    )


def held_size_controls(
    species: c210.Species,
    angle: float,
    infinite_states: list[carried.CarriedState],
) -> None:
    rows = []
    for side in (13, 15):
        periodic = embed_periodic(infinite_states[0], side)
        residuals = []
        q_residuals = []
        for tick in range(1, 7):
            periodic, report = joint_step(periodic, species, angle, tick, side)
            residuals.append(
                carried.state_residual(
                    periodic, embed_periodic(infinite_states[tick], side)
                )
            )
            q_residuals.append(report.global_q_residual)
        rows.append((side, max(residuals), max(q_residuals)))
    check(
        "held L=13,15 tori reproduce the full six-tick infinite joint state without wrap",
        max(max(state_residual, q_residual) for _side, state_residual, q_residual in rows)
        < TOLERANCE,
        rows,
    )


def mass_deletion_and_formula_controls(
    species: c210.Species, angle: float
) -> None:
    initial = carried.CarriedState({(0, 0, 0): c210.UNIFORM.copy()}, {})
    deleted = initial
    bare = initial
    for tick in range(1, 5):
        deleted, report = joint_step(deleted, species, 0.0, tick)
        bare = carried.coin_gate(bare, species.coin, c214.FIELD_COIN)
        bare, _matter_current, _excitation_current = carried.body_stream(bare)
        bare, _field_current = carried.field_stream(bare)
    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    check(
        "source-coupling deletion gives the bare common massive walk",
        carried.state_residual(deleted, bare) < 3e-12
        and sum(carried.field_density(deleted).values()) < 2e-14
        and report.global_q_residual < TOLERANCE,
        carried.state_residual(deleted, bare),
    )
    check(
        "both carried internal labels inherit the common one-particle mass fixture",
        abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "analytic_mass": species.analytic_mass,
            "dispersion_mass": dispersion_mass,
            "rest_mass": c219.rest_mass(species),
        },
    )
    phases = tuple(
        np.exp(1j * CONTACT_COUPLING * number * (number - 1) / 2)
        for number in (0, 1, 2)
    )
    check(
        "a separate out-of-domain contact formula check reproduces the N=2 phase; no contact layer is applied",
        abs(phases[0] - 1) < 2e-15
        and abs(phases[1] - 1) < 2e-15
        and abs(phases[2] - np.exp(1j * CONTACT_COUPLING)) < 2e-15,
        phases,
    )


def physical_scope_controls() -> None:
    indices = carried.physical_active_indices()
    check(
        "the inherited 18-M2 basis injection has 42 distinct active indices without instantiating a global physical matrix",
        len(indices) == len(set(indices)) == 42
        and all(index < (1 << 18) for index in indices),
        {
            "matter_M2": 12,
            "field_M2": 6,
            "active_dimension": len(indices),
            "Cycle269_splice": False,
            "global_2^18_tensor_matrix_instantiated_here": False,
        },
    )


def main() -> int:
    species = c219.common_species(BETA)
    angle = MEDIATOR_COUPLING * species.analytic_mass
    note_contract()
    local_and_global_charge_controls(angle)
    randomized_exchange_decomposition_controls(angle)
    states, _reports = six_tick_history_controls(species, angle)
    covariance_controls(species, angle)
    held_size_controls(species, angle, states)
    mass_deletion_and_formula_controls(species, angle)
    physical_scope_controls()
    print(
        "DIAGNOSTIC",
        {
            "beta": BETA,
            "mass": species.analytic_mass,
            "angle": angle,
            "declared_sector": "one matter, Q=N_e+N_f=1",
            "matter_M2_per_cell": 12,
            "field_M2_per_cell": 6,
            "total_M2_per_cell": 18,
            "update": "matter+field coins, local exchange, matter stream, field stream",
        },
    )
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
