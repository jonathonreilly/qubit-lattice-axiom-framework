#!/usr/bin/env python3
"""Reservoir-free Route 2: execute six hard-core field M2 through N_f=0,1,2.

This runner applies the selected all-occupancy local law to an ordinary sparse
tensor-product basis.  There is one moving six-direction matter carrier and
six ordinary hard-core mediator modes at every visited cubic cell.  The field
coin acts on a cell's weight-one subspace and as identity otherwise; the
matter-controlled vertex rotates local field vacuum and the uniform local
one-excitation state; streaming is the ordinary directional-mode permutation.

No global zero/one-field projector or host-side emission schedule is used.
The resulting ledger is a squared-norm field-number-sector weight, not a Born
probability, energy, work, stress, a clock rate, or a gravitational source.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FULL_HARD_CORE_HIGHER_FIELD_HISTORY_ROUTE_2_NOTE_2026-07-17.md"
)

BETA = -0.3
CONTACT_COUPLING = 0.37
MEDIATOR_COUPLING = 0.8
TOLERANCE = 4e-11
# The decisive history is compact enough to retain every nonzero floating
# amplitude.  This is intentionally zero: sparse cleanup removes exact zeros
# only, and the reported discarded-norm budget must remain zero.
PRUNE_THRESHOLD = 0.0
BRANCH_THRESHOLD = 0.0
PRUNED_NORM_TOTAL = 0.0

Position = tuple[int, int, int]
FieldMode = tuple[int, int, int, int]
FieldConfiguration = tuple[FieldMode, ...]
StateKey = tuple[Position, int, FieldConfiguration]

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


def add_position(
    position: Position, displacement: np.ndarray, side: int | None = None
) -> Position:
    moved = tuple(
        int(position[axis] + int(displacement[axis])) for axis in range(3)
    )
    if side is None:
        return moved
    return tuple(value % side for value in moved)


def canonical_field(modes: list[FieldMode] | tuple[FieldMode, ...]) -> FieldConfiguration:
    answer = tuple(sorted(modes))
    if len(answer) != len(set(answer)):
        raise ValueError("hard-core field configuration contains a duplicate mode")
    return answer


def mode_position(mode: FieldMode) -> Position:
    return mode[:3]


@dataclass
class FullState:
    amplitudes: dict[StateKey, complex]

    def cleaned(self, threshold: float | None = None) -> "FullState":
        global PRUNED_NORM_TOTAL
        cutoff = PRUNE_THRESHOLD if threshold is None else threshold
        retained: dict[StateKey, complex] = {}
        discarded_norm = 0.0
        for key, value in self.amplitudes.items():
            if abs(value) > cutoff:
                retained[key] = value
            else:
                discarded_norm += float(abs(value) ** 2)
        PRUNED_NORM_TOTAL += discarded_norm
        return FullState(retained)


@dataclass(frozen=True)
class LocalLaw:
    matter_coin: np.ndarray
    field_coin: np.ndarray
    scalar_projector: np.ndarray
    field_rotation: np.ndarray
    field_number: np.ndarray
    angle: float


def state_norm(state: FullState) -> float:
    return float(sum(abs(value) ** 2 for value in state.amplitudes.values()))


def state_residual(left: FullState, right: FullState) -> float:
    return float(
        np.sqrt(
            sum(
                abs(left.amplitudes.get(key, 0) - right.amplitudes.get(key, 0))
                ** 2
                for key in left.amplitudes.keys() | right.amplitudes.keys()
            )
        )
    )


def scale_state(state: FullState, coefficient: complex) -> FullState:
    return FullState(
        {key: coefficient * value for key, value in state.amplitudes.items()}
    ).cleaned()


def add_states(left: FullState, right: FullState) -> FullState:
    amplitudes: defaultdict[StateKey, complex] = defaultdict(complex)
    for state in (left, right):
        for key, value in state.amplitudes.items():
            amplitudes[key] += value
    return FullState(dict(amplitudes)).cleaned()


def scalar_matter_state(
    position: Position = (0, 0, 0),
    field: FieldConfiguration = (),
) -> FullState:
    return FullState(
        {
            (position, direction, field): complex(c210.UNIFORM[direction])
            for direction in range(6)
        }
    )


def local_scalar_field_state(position: Position = (0, 0, 0)) -> FullState:
    amplitudes: dict[StateKey, complex] = {}
    for matter_direction in range(6):
        for field_direction in range(6):
            amplitudes[
                (
                    position,
                    matter_direction,
                    ((position[0], position[1], position[2], field_direction),),
                )
            ] = complex(
                c210.UNIFORM[matter_direction] * c210.UNIFORM[field_direction]
            )
    return FullState(amplitudes)


def field_number_distribution(state: FullState) -> dict[int, float]:
    result: defaultdict[int, float] = defaultdict(float)
    for (_position, _direction, field), amplitude in state.amplitudes.items():
        result[len(field)] += float(abs(amplitude) ** 2)
    return dict(sorted(result.items()))


def matter_density(state: FullState) -> dict[Position, float]:
    density: defaultdict[Position, float] = defaultdict(float)
    for (position, _direction, _field), amplitude in state.amplitudes.items():
        density[position] += float(abs(amplitude) ** 2)
    return dict(density)


def field_density(state: FullState) -> dict[Position, float]:
    density: defaultdict[Position, float] = defaultdict(float)
    for (_body, _direction, field), amplitude in state.amplitudes.items():
        weight = float(abs(amplitude) ** 2)
        for mode in field:
            density[mode_position(mode)] += weight
    return dict(density)


def field_mode_density(state: FullState) -> dict[tuple[Position, int], float]:
    density: defaultdict[tuple[Position, int], float] = defaultdict(float)
    for (_body, _direction, field), amplitude in state.amplitudes.items():
        weight = float(abs(amplitude) ** 2)
        for x, y, z, direction in field:
            density[((x, y, z), direction)] += weight
    return dict(density)


def dictionary_residual(
    left: dict[Position, float], right: dict[Position, float]
) -> float:
    return max(
        (
            abs(left.get(key, 0.0) - right.get(key, 0.0))
            for key in left.keys() | right.keys()
        ),
        default=0.0,
    )


def expected_field_number(state: FullState) -> float:
    return float(
        sum(number * weight for number, weight in field_number_distribution(state).items())
    )


def make_local_law(species: c210.Species, angle: float) -> LocalLaw:
    identity64 = np.eye(64, dtype=complex)
    one_particle = tuple(1 << direction for direction in range(6))
    vacuum = np.zeros(64, dtype=complex)
    vacuum[0] = 1
    scalar = np.zeros(64, dtype=complex)
    scalar[list(one_particle)] = c210.UNIFORM
    field_coin = identity64.copy()
    field_coin[np.ix_(one_particle, one_particle)] = c214.FIELD_COIN
    source_projector = np.outer(vacuum, vacuum) + np.outer(scalar, scalar.conj())
    source_flip = np.outer(vacuum, scalar.conj()) + np.outer(scalar, vacuum.conj())
    field_rotation = (
        identity64
        + (np.cos(angle) - 1) * source_projector
        + 1j * np.sin(angle) * source_flip
    )
    number_values = np.sum(c229.occupation_table(6), axis=1)
    return LocalLaw(
        matter_coin=species.coin,
        field_coin=field_coin,
        scalar_projector=c210.P_SCALAR,
        field_rotation=field_rotation,
        field_number=np.diag(number_values),
        angle=angle,
    )


def apply_matter_coin(state: FullState, coin: np.ndarray) -> FullState:
    output: defaultdict[StateKey, complex] = defaultdict(complex)
    for (position, source_direction, field), amplitude in state.amplitudes.items():
        for target_direction in range(6):
            coefficient = coin[target_direction, source_direction]
            if abs(coefficient) > BRANCH_THRESHOLD:
                output[(position, target_direction, field)] += coefficient * amplitude
    return FullState(dict(output)).cleaned()


def apply_field_coin(state: FullState, coin64: np.ndarray) -> FullState:
    output: defaultdict[StateKey, complex] = defaultdict(complex)
    for (body, matter_direction, field), amplitude in state.amplitudes.items():
        local_modes: defaultdict[Position, list[int]] = defaultdict(list)
        for x, y, z, direction in field:
            local_modes[(x, y, z)].append(direction)
        singleton_cells = tuple(
            sorted(position for position, directions in local_modes.items() if len(directions) == 1)
        )
        branches: dict[FieldConfiguration, complex] = {field: amplitude}
        for position in singleton_cells:
            next_branches: defaultdict[FieldConfiguration, complex] = defaultdict(complex)
            for configuration, branch_amplitude in branches.items():
                local = [mode for mode in configuration if mode_position(mode) == position]
                if len(local) != 1:
                    raise AssertionError("onsite field number changed during coin application")
                source_direction = local[0][3]
                retained = [mode for mode in configuration if mode_position(mode) != position]
                source_basis = 1 << source_direction
                for target_direction in range(6):
                    coefficient = coin64[1 << target_direction, source_basis]
                    if abs(coefficient) > BRANCH_THRESHOLD:
                        target = canonical_field(
                            retained
                            + [
                                (
                                    position[0],
                                    position[1],
                                    position[2],
                                    target_direction,
                                )
                            ]
                        )
                        next_branches[target] += coefficient * branch_amplitude
            branches = dict(next_branches)
        for configuration, branch_amplitude in branches.items():
            output[(body, matter_direction, configuration)] += branch_amplitude
    return FullState(dict(output)).cleaned()


def split_local_field(
    field: FieldConfiguration, position: Position
) -> tuple[FieldConfiguration, int]:
    retained: list[FieldMode] = []
    basis = 0
    for mode in field:
        if mode_position(mode) == position:
            basis |= 1 << mode[3]
        else:
            retained.append(mode)
    return canonical_field(retained), basis


def join_local_field(
    retained: FieldConfiguration, position: Position, basis: int
) -> FieldConfiguration:
    modes = list(retained)
    modes.extend(
        (position[0], position[1], position[2], direction)
        for direction in range(6)
        if (basis >> direction) & 1
    )
    return canonical_field(modes)


def apply_vertex(state: FullState, law: LocalLaw) -> FullState:
    grouped: dict[tuple[Position, FieldConfiguration], np.ndarray] = {}
    for (position, matter_direction, field), amplitude in state.amplitudes.items():
        retained, local_basis = split_local_field(field, position)
        vector = grouped.setdefault(
            (position, retained), np.zeros((6, 64), dtype=complex)
        )
        vector[matter_direction, local_basis] += amplitude

    output: defaultdict[StateKey, complex] = defaultdict(complex)
    delta_rotation = law.field_rotation - np.eye(64, dtype=complex)
    for (position, retained), vector in grouped.items():
        transformed = vector + law.scalar_projector @ vector @ delta_rotation.T
        for matter_direction, local_basis in zip(
            *np.nonzero(np.abs(transformed) > BRANCH_THRESHOLD)
        ):
            field = join_local_field(retained, position, int(local_basis))
            output[(position, int(matter_direction), field)] += transformed[
                matter_direction, local_basis
            ]
    return FullState(dict(output)).cleaned()


def apply_stream(state: FullState, side: int | None = None) -> FullState:
    output: defaultdict[StateKey, complex] = defaultdict(complex)
    for (body, matter_direction, field), amplitude in state.amplitudes.items():
        moved_body = add_position(body, c210.DIRECTIONS[matter_direction], side)
        moved_field = []
        for x, y, z, direction in field:
            moved = add_position((x, y, z), c210.DIRECTIONS[direction], side)
            moved_field.append((moved[0], moved[1], moved[2], direction))
        output[(moved_body, matter_direction, canonical_field(moved_field))] += amplitude
    return FullState(dict(output)).cleaned()


def free_step(state: FullState, law: LocalLaw, side: int | None = None) -> FullState:
    return apply_stream(
        apply_field_coin(apply_matter_coin(state, law.matter_coin), law.field_coin),
        side,
    )


def incoming_field_density(
    edge_current: dict[tuple[Position, int], float], side: int | None = None
) -> dict[Position, float]:
    incoming: defaultdict[Position, float] = defaultdict(float)
    for (source, direction), value in edge_current.items():
        destination = add_position(source, c210.DIRECTIONS[direction], side)
        incoming[destination] += value
    return dict(incoming)


def incoming_matter_density(
    state: FullState, side: int | None = None
) -> dict[Position, float]:
    incoming: defaultdict[Position, float] = defaultdict(float)
    for (source, direction, _field), amplitude in state.amplitudes.items():
        destination = add_position(source, c210.DIRECTIONS[direction], side)
        incoming[destination] += float(abs(amplitude) ** 2)
    return dict(incoming)


def full_step(
    state: FullState, law: LocalLaw, side: int | None = None
) -> tuple[FullState, dict[str, object]]:
    pruning_before = PRUNED_NORM_TOTAL
    before_field = field_density(state)
    before_matter = matter_density(state)
    before_number = expected_field_number(state)

    matter_coined = apply_matter_coin(state, law.matter_coin)
    coined = apply_field_coin(matter_coined, law.field_coin)
    coin_field = field_density(coined)
    coin_matter = matter_density(coined)

    sourced = apply_vertex(coined, law)
    sourced_field = field_density(sourced)
    sourced_matter = matter_density(sourced)
    source_current = {
        position: sourced_field.get(position, 0.0) - coin_field.get(position, 0.0)
        for position in sourced_field.keys() | coin_field.keys()
    }
    edge_current = field_mode_density(sourced)
    field_incoming = incoming_field_density(edge_current, side)
    matter_incoming = incoming_matter_density(sourced, side)

    output = apply_stream(sourced, side)
    output_field = field_density(output)
    output_matter = matter_density(output)
    continuity_target = {
        position: source_current.get(position, 0.0)
        + field_incoming.get(position, 0.0)
        - sourced_field.get(position, 0.0)
        for position in (
            source_current.keys() | field_incoming.keys() | sourced_field.keys()
        )
    }
    continuity_observed = {
        position: output_field.get(position, 0.0) - coin_field.get(position, 0.0)
        for position in output_field.keys() | coin_field.keys()
    }

    diagnostics: dict[str, object] = {
        "basis_count_before": len(state.amplitudes),
        "basis_count_after": len(output.amplitudes),
        "norm_residual": max(
            abs(state_norm(candidate) - state_norm(state))
            for candidate in (matter_coined, coined, sourced, output)
        ),
        "field_coin_density_residual": dictionary_residual(before_field, coin_field),
        "matter_coin_density_residual": dictionary_residual(before_matter, coin_matter),
        "matter_vertex_density_residual": dictionary_residual(coin_matter, sourced_matter),
        "source_sum": sum(source_current.values()),
        "number_change_at_vertex": expected_field_number(sourced) - before_number,
        "field_stream_residual": dictionary_residual(output_field, field_incoming),
        "matter_stream_residual": dictionary_residual(output_matter, matter_incoming),
        "continuity_residual": dictionary_residual(continuity_observed, continuity_target),
        "source_current": source_current,
        "field_edge_current_sum": sum(edge_current.values()),
        "field_number_before_stream": expected_field_number(sourced),
        "distribution": field_number_distribution(output),
        "expected_field_number": expected_field_number(output),
        "discarded_norm": PRUNED_NORM_TOTAL - pruning_before,
    }
    return output, diagnostics


def rotate_position(position: Position, frame: np.ndarray) -> Position:
    return tuple(int(value) for value in frame @ np.asarray(position, dtype=int))


def direction_target(direction: int, frame: np.ndarray) -> int:
    permutation = c210.direction_permutation(frame)
    return int(np.argmax(permutation[:, direction]))


def rotate_state(state: FullState, frame: np.ndarray) -> FullState:
    output: defaultdict[StateKey, complex] = defaultdict(complex)
    for (body, matter_direction, field), amplitude in state.amplitudes.items():
        moved_body = rotate_position(body, frame)
        moved_matter_direction = direction_target(matter_direction, frame)
        moved_field = []
        for x, y, z, direction in field:
            moved = rotate_position((x, y, z), frame)
            moved_field.append(
                (moved[0], moved[1], moved[2], direction_target(direction, frame))
            )
        output[
            (moved_body, moved_matter_direction, canonical_field(moved_field))
        ] += amplitude
    return FullState(dict(output)).cleaned()


def embed_periodic(state: FullState, side: int) -> FullState:
    center = side // 2
    output: defaultdict[StateKey, complex] = defaultdict(complex)
    for (body, matter_direction, field), amplitude in state.amplitudes.items():
        moved_body = tuple((value + center) % side for value in body)
        moved_field = [
            ((x + center) % side, (y + center) % side, (z + center) % side, direction)
            for x, y, z, direction in field
        ]
        output[(moved_body, matter_direction, canonical_field(moved_field))] += amplitude
    return FullState(dict(output)).cleaned()


def local_law_controls(law: LocalLaw) -> None:
    identity64 = np.eye(64, dtype=complex)
    number_values = np.diag(law.field_number).real
    check(
        "the selected hard-core coin and source rotation are exact all-occupancy unitaries",
        np.linalg.norm(law.field_coin.conj().T @ law.field_coin - identity64) < 3e-12
        and np.linalg.norm(law.field_rotation.conj().T @ law.field_rotation - identity64)
        < 3e-12
        and np.linalg.norm(
            law.field_coin[np.ix_(number_values != 1, number_values != 1)]
            - identity64[np.ix_(number_values != 1, number_values != 1)]
        )
        < 3e-12,
        {"local_dimension": 64, "ordinary_hard_core_M2": 6},
    )

    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        permutation = c210.direction_permutation(frame)
        field_frame = np.zeros((64, 64), dtype=complex)
        for basis in range(64):
            target = 0
            for direction in range(6):
                if (basis >> direction) & 1:
                    target |= 1 << int(np.argmax(permutation[:, direction]))
            field_frame[target, basis] = 1
        frame_residuals.extend(
            (
                np.linalg.norm(
                    permutation @ law.matter_coin - law.matter_coin @ permutation
                ),
                np.linalg.norm(field_frame @ law.field_coin - law.field_coin @ field_frame),
                np.linalg.norm(
                    field_frame @ law.field_rotation - law.field_rotation @ field_frame
                ),
            )
        )
    check(
        "the complete local blocks commute with all 24 proper-cubic frames",
        len(frame_residuals) == 72 and max(frame_residuals) < 3e-11,
        max(frame_residuals),
    )


def higher_field_history_controls(law: LocalLaw) -> tuple[FullState, list[dict[str, object]]]:
    state = scalar_matter_state()
    rows: list[dict[str, object]] = []
    for tick in (1, 2):
        state, diagnostics = full_step(state, law)
        row = {"tick": tick, **diagnostics}
        rows.append(row)

    maximum_ledger_residual = max(
        max(
            float(row[key])
            for key in (
                "norm_residual",
                "field_coin_density_residual",
                "matter_coin_density_residual",
                "matter_vertex_density_residual",
                "field_stream_residual",
                "matter_stream_residual",
                "continuity_residual",
            )
        )
        for row in rows
    )
    check(
        "the autonomous N_f=0 to N_f=1,2 history has an exact local source/edge ledger",
        maximum_ledger_residual < TOLERANCE
        and all(
            abs(float(row["source_sum"]) - float(row["number_change_at_vertex"]))
            < TOLERANCE
            and abs(
                float(row["field_edge_current_sum"])
                - float(row["field_number_before_stream"])
            )
            < TOLERANCE
            and float(row["discarded_norm"]) == 0.0
            for row in rows
        ),
        [
            {
                "tick": row["tick"],
                "basis_count_after": row["basis_count_after"],
                "distribution": row["distribution"],
                "source_sum": row["source_sum"],
                "discarded_norm": row["discarded_norm"],
                "maximum_ledger_residual": max(
                    float(row[key])
                    for key in (
                        "norm_residual",
                        "field_coin_density_residual",
                        "matter_coin_density_residual",
                        "matter_vertex_density_residual",
                        "field_stream_residual",
                        "matter_stream_residual",
                        "continuity_residual",
                    )
                ),
            }
            for row in rows
        ],
    )
    check(
        "the decisive two-tick history uses zero sparse-amplitude pruning",
        all(float(row["discarded_norm"]) == 0.0 for row in rows),
        [float(row["discarded_norm"]) for row in rows],
    )
    nf2_weight = float(rows[-1]["distribution"].get(2, 0.0))
    check(
        "the second autonomous tick has genuine two-mediator support with no blockade",
        nf2_weight > 1e-6
        and set(rows[-1]["distribution"]).issuperset({0, 1, 2}),
        {
            "Nf2_weight": nf2_weight,
            "Nf_sector_weights": rows[-1]["distribution"],
            "basis_count": rows[-1]["basis_count_after"],
        },
    )
    return state, rows


def absorption_and_resource_controls(law: LocalLaw, rows: list[dict[str, object]]) -> None:
    absorption_input = local_scalar_field_state()
    _absorption_output, absorption = full_step(absorption_input, law)
    expected_absorption = -np.sin(law.angle) ** 2
    check(
        "a prepared local scalar mediator undergoes exact autonomous absorption",
        abs(float(absorption["source_sum"]) - expected_absorption) < 4e-12
        and float(absorption["source_sum"]) < 0
        and float(absorption["continuity_residual"]) < TOLERANCE,
        {
            "source_current": absorption["source_sum"],
            "expected": expected_absorption,
            "output_distribution": absorption["distribution"],
        },
    )

    spectator_modes = canonical_field(
        [
            (3, 0, 0, 0),
            (0, 3, 0, 2),
        ]
    )
    nf2_input = scalar_matter_state(field=spectator_modes)
    nf2_coined = apply_field_coin(
        apply_matter_coin(nf2_input, law.matter_coin), law.field_coin
    )
    nf3_output = apply_vertex(nf2_coined, law)
    nf3_weight = field_number_distribution(nf3_output).get(3, 0.0)
    expected_emission = np.sin(law.angle) ** 2
    check(
        "N_f<=2 is not invariant: a local-vacuum N_f=2 state emits a third mediator",
        nf3_weight is not None
        and abs(float(nf3_weight) - expected_emission) < 4e-12,
        {
            "Nf3_weight": nf3_weight,
            "sin_squared_angle": expected_emission,
        },
    )

    cumulative_source = sum(float(row["source_sum"]) for row in rows)
    final_expected_number = float(rows[-1]["expected_field_number"])
    check(
        "matter count plus mediator count has the quantified repeated-emission seam",
        abs(final_expected_number - cumulative_source) < 4e-11
        and cumulative_source > 0
        and abs(sum(matter_density(absorption_input).values()) - 1) < 3e-12,
        {
            "matter_number_change": 0.0,
            "mediator_number_change_after_two_ticks": final_expected_number,
            "cumulative_onsite_source_current": cumulative_source,
            "missing_local_reservoir_coordinate": -cumulative_source,
        },
    )


def deletion_covariance_and_held_size_controls(
    law: LocalLaw, two_tick_state: FullState
) -> None:
    deleted_law = LocalLaw(
        matter_coin=law.matter_coin,
        field_coin=law.field_coin,
        scalar_projector=law.scalar_projector,
        field_rotation=np.eye(64, dtype=complex),
        field_number=law.field_number,
        angle=0.0,
    )
    initial = scalar_matter_state()
    deleted = initial
    bare = initial
    for _tick in range(2):
        deleted, diagnostics = full_step(deleted, deleted_law)
        bare = free_step(bare, deleted_law)
    check(
        "vertex deletion returns the bare massive walk and exact field vacuum",
        state_residual(deleted, bare) < 3e-12
        and expected_field_number(deleted) < 2e-14
        and float(diagnostics["continuity_residual"]) < TOLERANCE,
        state_residual(deleted, bare),
    )

    covariance_residuals = []
    # A genuine N_f=2 tensor configuration is sufficient for the all-frame law
    # test and avoids mistaking a needlessly large third-tick expansion for
    # additional scientific coverage.
    covariance_input = scalar_matter_state(
        field=canonical_field(
            [
                (1, 1, 0, 0),
                (-1, 0, 1, 3),
            ]
        )
    )
    reference, _ = full_step(covariance_input, law)
    for frame in c210.proper_cubic_frames():
        rotated_output, _ = full_step(rotate_state(covariance_input, frame), law)
        covariance_residuals.append(
            state_residual(rotated_output, rotate_state(reference, frame))
        )
    check(
        "the genuine higher-field update commutes with all 24 proper-cubic frames",
        len(covariance_residuals) == 24
        and max(covariance_residuals) < TOLERANCE,
        max(covariance_residuals),
    )

    infinite_states = [initial]
    state = initial
    for _tick in range(2):
        state, _ = full_step(state, law)
        infinite_states.append(state)
    held_rows = []
    for side in (5, 7):
        periodic = embed_periodic(initial, side)
        residuals = []
        for tick in range(1, 3):
            periodic, _ = full_step(periodic, law, side)
            residuals.append(
                state_residual(periodic, embed_periodic(infinite_states[tick], side))
            )
        held_rows.append((side, max(residuals)))
    check(
        "held L=5,7 tori reproduce the two-tick infinite sparse history without wrap",
        max(residual for _side, residual in held_rows) < TOLERANCE,
        held_rows,
    )


def composition_mass_contact_and_static_controls(
    law: LocalLaw, species: c210.Species
) -> None:
    left = scalar_matter_state((-1, 0, 0))
    right = scalar_matter_state((2, 1, 0))
    combined = add_states(scale_state(left, 0.6), scale_state(right, 0.8j))
    evolved_combined, _ = full_step(combined, law)
    evolved_left, _ = full_step(left, law)
    evolved_right, _ = full_step(right, law)
    expected = add_states(
        scale_state(evolved_left, 0.6), scale_state(evolved_right, 0.8j)
    )
    check(
        "the logical-matter/physical-hard-core-field sparse update composes linearly on separated source packets",
        state_residual(evolved_combined, expected) < 3e-12,
        state_residual(evolved_combined, expected),
    )

    occupations = c229.occupation_table(6)
    matter_number = np.sum(occupations, axis=1)
    contact = np.diag(
        np.exp(1j * CONTACT_COUPLING * matter_number * (matter_number - 1) / 2)
    )
    analytic_mass = species.analytic_mass
    check(
        "the separate Cycle-230 contact fixture is identity at N_m=1 and the bare mass fixture is retained",
        np.max(np.abs(np.diag(contact)[matter_number <= 1] - 1)) < 2e-15
        and abs(
            np.diag(contact)[int(np.where(matter_number == 2)[0][0])]
            - np.exp(1j * CONTACT_COUPLING)
        )
        < 2e-15
        and abs(c219.rest_mass(species) / analytic_mass - 1) < 2e-12,
        {
            "bare_analytic_mass": analytic_mass,
            "bare_rest_mass": c219.rest_mass(species),
            "dressed_mass": "not tested",
        },
    )

    side = 9
    source = c211.point_source(side)
    coin_field = c216.solve_coin_field(source)
    green = c211.solve_field(source)
    static_residual = np.linalg.norm(c216.scalar_field(coin_field).real - 3 * green)
    laplacian_source = 6 * source - sum(
        (
            np.roll(source, displacement, axis=axis)
            for axis in range(3)
            for displacement in (-1, 1)
        ),
        np.zeros_like(source),
    )
    additive_port = -laplacian_source / 6
    additive_response = 3 * c211.solve_field(additive_port)
    additive_identity = np.linalg.norm(additive_response + source / 2)
    additive_target_residual = np.linalg.norm(additive_response - 3 * green)
    check(
        "only after the autonomous history, the same one-field coin retains static 3 L^+",
        static_residual < 6e-12,
        static_residual,
    )
    check(
        "the selected additive Cycle-215 port remains an external comparator, not this history",
        additive_identity < 3e-12 and additive_target_residual > 1,
        {
            "minus_half_identity_residual": additive_identity,
            "static_target_residual": additive_target_residual,
        },
    )


def note_contract() -> None:
    text = NOTE.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    text = " ".join(text.split())
    required = (
        "authority: none",
        "audit: unset",
        "ordinary hard-core",
        "no global blockade",
        "n_f=0",
        "n_f=2",
        "squared-norm n_f-sector weight",
        "not a born probability",
        "local source/edge ledger",
        "autonomous absorption",
        "not invariant",
        "source-capacity seam",
        "all 24 proper-cubic frames",
        "held l=5,7",
        "bare mass",
        "contact fixture is evaluated separately",
        "externally supplied additive cycle-215 port",
        "not the autonomous hard-core history",
        "3 l^+",
        "supplied structure",
        "no no-go claim",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the higher-field scope and semantic boundaries", not missing, missing)


def main() -> int:
    species = c219.common_species(BETA)
    charge = c219.rest_mass(species)
    angle = MEDIATOR_COUPLING * charge
    law = make_local_law(species, angle)

    note_contract()
    local_law_controls(law)
    two_tick_state, rows = higher_field_history_controls(law)
    absorption_and_resource_controls(law, rows)
    deletion_covariance_and_held_size_controls(law, two_tick_state)
    composition_mass_contact_and_static_controls(law, species)
    print(
        "DIAGNOSTIC",
        {
            "beta": BETA,
            "charge": charge,
            "mediator_coupling": MEDIATOR_COUPLING,
            "angle": angle,
            "matter_representation": "logical_one_particle_uncompiled",
            "physical_field_M2_per_cell": 6,
            "update_order": "matter coin + all-occupancy field coin, vertex, ordinary streams",
        },
    )
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
