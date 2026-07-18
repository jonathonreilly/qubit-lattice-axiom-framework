#!/usr/bin/env python3
"""Constructive interface between carried and site-reservoir source blocks.

The site-reservoir Q=1 block and one carried e/g direction block are both
seven dimensional.  Their exchange gates have opposite exponential signs,
so a local minus sign on the reservoir-to-excited basis image gives an exact
vertex intertwiner.  Extending over all six matter directions also
intertwines the onsite matter/field coins and proper-cubic frame actions.

The fixed-reservoir stream leaves that local image.  A tagged sparse model
quantifies the residual, then tests two constructive repairs: a co-moving
reservoir permutation and a staggered matter-stream/reservoir-catch-up word.
This is a one-matter logical interface probe, not a Cycle-269 physical state
encoder, a full-Fock compiler, energy, gravity, a clock, or a no-go claim.
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
    "CARRIED_SITE_RESERVOIR_INTERFACE_MAPPING_NOTE_2026-07-17.md"
)

BETA = -0.3
COUPLING = 0.8
CONTACT_COUPLING = 0.37
TOLERANCE = 5e-11

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
    text = NOTE.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the interface note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "seven-state",
        "local minus sign",
        "exact vertex intertwiner",
        "exact coin intertwiner",
        "all 24 proper-cubic frames",
        "fixed reservoir",
        "co-moving repair",
        "staggered catch-up repair",
        "conditional transposition",
        "norm-preserving involution",
        "intermediate leakage",
        "staggered inverse residual",
        "one-matter",
        "not a cycle-269 physical state encoder",
        "not energy",
        "not gravity",
        "contact fixture is not applied",
        "supplied structure",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note preserves the constructive interface and scope contract", not missing, missing)


def site_exchange(angle: float) -> tuple[np.ndarray, np.ndarray]:
    """H and exp(-i angle H) on reservoir direct-sum six field directions."""
    exchange = np.zeros((7, 7), dtype=complex)
    exchange[0, 1:] = c210.UNIFORM.conj()
    exchange[1:, 0] = c210.UNIFORM
    gate = (
        np.eye(7, dtype=complex)
        + (np.cos(angle) - 1) * (exchange @ exchange)
        - 1j * np.sin(angle) * exchange
    )
    return exchange, gate


def interface_isometry() -> np.ndarray:
    """J: matter-direction x (reservoir + field) -> E direct-sum GF."""
    result = np.zeros((42, 42), dtype=complex)
    for matter_direction in range(6):
        site_base = 7 * matter_direction
        result[matter_direction, site_base] = -1
        for field_direction in range(6):
            carried_index = 6 + 6 * matter_direction + field_direction
            result[carried_index, site_base + 1 + field_direction] = 1
    return result


def site_coin(matter_coin: np.ndarray, field_coin: np.ndarray) -> np.ndarray:
    result = np.zeros((42, 42), dtype=complex)
    for source_matter in range(6):
        for target_matter in range(6):
            matter_coefficient = matter_coin[target_matter, source_matter]
            result[7 * target_matter, 7 * source_matter] = matter_coefficient
            for source_field in range(6):
                for target_field in range(6):
                    result[
                        7 * target_matter + 1 + target_field,
                        7 * source_matter + 1 + source_field,
                    ] = (
                        matter_coefficient
                        * field_coin[target_field, source_field]
                    )
    return result


def carried_coin(matter_coin: np.ndarray, field_coin: np.ndarray) -> np.ndarray:
    result = np.zeros((42, 42), dtype=complex)
    result[:6, :6] = matter_coin
    result[6:, 6:] = np.kron(matter_coin, field_coin)
    return result


def site_frame(frame: np.ndarray) -> np.ndarray:
    direction = c210.direction_permutation(frame)
    internal = np.zeros((7, 7), dtype=complex)
    internal[0, 0] = 1
    internal[1:, 1:] = direction
    return np.kron(direction, internal)


def carried_frame(frame: np.ndarray) -> np.ndarray:
    direction = c210.direction_permutation(frame)
    result = np.zeros((42, 42), dtype=complex)
    result[:6, :6] = direction
    result[6:, 6:] = np.kron(direction, direction)
    return result


def local_interface_controls(species: c210.Species, angle: float) -> None:
    print("\nLOCAL SEVEN-STATE / 42-STATE INTERFACE")
    site_h, site_v7 = site_exchange(angle)
    site_v = np.kron(np.eye(6, dtype=complex), site_v7)
    carried_h, carried_v, _charge = carried.active_blocks(angle)
    interface = interface_isometry()
    check(
        "the local phase-gauged map is an exact isometry and vertex intertwiner",
        np.linalg.norm(interface.conj().T @ interface - np.eye(42)) < TOLERANCE
        and np.linalg.norm(interface @ interface.conj().T - np.eye(42)) < TOLERANCE
        and np.linalg.norm(interface @ site_v - carried_v @ interface) < TOLERANCE
        and np.linalg.norm(interface @ np.kron(np.eye(6), site_h) + carried_h @ interface)
        < TOLERANCE,
        {
            "isometry_residual": float(
                np.linalg.norm(interface.conj().T @ interface - np.eye(42))
            ),
            "vertex_intertwiner_residual": float(
                np.linalg.norm(interface @ site_v - carried_v @ interface)
            ),
            "generator_sign_residual": float(
                np.linalg.norm(
                    interface @ np.kron(np.eye(6), site_h)
                    + carried_h @ interface
                )
            ),
        },
    )

    onsite_site = site_coin(species.coin, c214.FIELD_COIN)
    onsite_carried = carried_coin(species.coin, c214.FIELD_COIN)
    check(
        "the same local map exactly intertwines the matter and field coins",
        np.linalg.norm(interface @ onsite_site - onsite_carried @ interface)
        < TOLERANCE,
        float(np.linalg.norm(interface @ onsite_site - onsite_carried @ interface)),
    )

    covariance = []
    for frame in c210.proper_cubic_frames():
        covariance.append(
            np.linalg.norm(
                carried_frame(frame) @ interface - interface @ site_frame(frame)
            )
        )
    check(
        "the local interface is covariant under all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < TOLERANCE,
        max(covariance),
    )

    site_basis_indices = (1 << 6,) + tuple(1 << direction for direction in range(6))
    carried_indices = carried.physical_active_indices()
    check(
        "one direction block maps seven physical reservoir/field basis states into seven distinct states of the direct 18-M2 code",
        len(site_basis_indices) == len(set(site_basis_indices)) == 7
        and len(carried_indices) == len(set(carried_indices)) == 42,
        {
            "input_reservoir_field_M2": 7,
            "output_direct_code_M2": 18,
            "fixed_direction_block_dimension": 7,
            "all_direction_dimension": 42,
        },
    )


@dataclass
class SiteState:
    """One matter carrier with either one tagged reservoir or one field."""

    reservoir: dict[tuple[Position, Position], np.ndarray]
    field: dict[tuple[Position, Position], np.ndarray]

    def copy(self) -> "SiteState":
        return SiteState(
            {key: value.copy() for key, value in self.reservoir.items()},
            {key: value.copy() for key, value in self.field.items()},
        )


def zero_vector() -> np.ndarray:
    return np.zeros(6, dtype=complex)


def zero_pair() -> np.ndarray:
    return np.zeros((6, 6), dtype=complex)


def add_position(position: Position, direction: int, sign: int = 1) -> Position:
    return tuple(
        int(position[axis] + sign * c210.DIRECTIONS[direction, axis])
        for axis in range(3)
    )


def site_norm(state: SiteState) -> float:
    return float(
        sum(np.vdot(value, value).real for value in state.reservoir.values())
        + sum(np.vdot(value, value).real for value in state.field.values())
    )


def site_residual(left: SiteState, right: SiteState) -> float:
    total = 0.0
    for key in left.reservoir.keys() | right.reservoir.keys():
        difference = left.reservoir.get(key, zero_vector()) - right.reservoir.get(
            key, zero_vector()
        )
        total += float(np.vdot(difference, difference).real)
    for key in left.field.keys() | right.field.keys():
        difference = left.field.get(key, zero_pair()) - right.field.get(
            key, zero_pair()
        )
        total += float(np.vdot(difference, difference).real)
    return float(np.sqrt(total))


def carried_to_site(state: carried.CarriedState) -> SiteState:
    return SiteState(
        {(body, body): -value.copy() for body, value in state.excited.items()},
        {key: value.copy() for key, value in state.pair.items()},
    )


def scale_carried(
    state: carried.CarriedState, coefficient: complex
) -> carried.CarriedState:
    return carried.CarriedState(
        {key: coefficient * value for key, value in state.excited.items()},
        {key: coefficient * value for key, value in state.pair.items()},
    )


def site_to_carried(state: SiteState) -> carried.CarriedState:
    off_code = [
        (body, reservoir)
        for (body, reservoir), value in state.reservoir.items()
        if body != reservoir and np.vdot(value, value).real > 1e-24
    ]
    if off_code:
        raise ValueError(f"fixed reservoir state is outside the local image: {off_code[:3]}")
    excited: dict[Position, np.ndarray] = {}
    for (body, _reservoir), value in state.reservoir.items():
        excited[body] = excited.get(body, zero_vector()) - value
    return carried.CarriedState(
        excited, {key: value.copy() for key, value in state.field.items()}
    )


def coincidence_leakage(state: SiteState) -> float:
    return float(
        np.sqrt(
            sum(
                np.vdot(value, value).real
                for (body, reservoir), value in state.reservoir.items()
                if body != reservoir
            )
        )
    )


def site_coin_gate(
    state: SiteState, matter_coin: np.ndarray, field_coin: np.ndarray
) -> SiteState:
    return SiteState(
        {key: matter_coin @ value for key, value in state.reservoir.items()},
        {
            key: np.einsum(
                "ab,cd,bd->ac", matter_coin, field_coin, value, optimize=True
            )
            for key, value in state.field.items()
        },
    )


def site_vertex_gate(state: SiteState, angle: float) -> SiteState:
    output = state.copy()
    positions = {
        body for body, reservoir in state.reservoir if body == reservoir
    }
    positions.update(body for body, field in state.field if body == field)
    cosine = np.cos(angle)
    sine = np.sin(angle)
    for position in positions:
        reservoir = state.reservoir.get((position, position), zero_vector())
        pair = state.field.get((position, position), zero_pair())
        scalar = pair @ c210.UNIFORM
        transverse = pair - np.outer(scalar, c210.UNIFORM.conj())
        output.reservoir[(position, position)] = (
            cosine * reservoir - 1j * sine * scalar
        )
        new_scalar = -1j * sine * reservoir + cosine * scalar
        output.field[(position, position)] = transverse + np.outer(
            new_scalar, c210.UNIFORM.conj()
        )
    return output


def site_body_stream(
    state: SiteState, *, co_moving: bool, inverse: bool = False
) -> SiteState:
    reservoir_output: dict[tuple[Position, Position], np.ndarray] = {}
    field_output: dict[tuple[Position, Position], np.ndarray] = {}
    sign = -1 if inverse else 1
    for (body, reservoir), value in state.reservoir.items():
        for direction in range(6):
            moved_body = add_position(body, direction, sign)
            moved_reservoir = (
                add_position(reservoir, direction, sign) if co_moving else reservoir
            )
            reservoir_output.setdefault(
                (moved_body, moved_reservoir), zero_vector()
            )[direction] += value[direction]
    for (body, field), value in state.field.items():
        for direction in range(6):
            moved_body = add_position(body, direction, sign)
            field_output.setdefault((moved_body, field), zero_pair())[
                direction, :
            ] += value[direction, :]
    return SiteState(reservoir_output, field_output)


def reservoir_catch_up(state: SiteState) -> SiteState:
    """Swap the streamed body's upstream and colocated reservoir tags.

    For each matter direction this is a transposition on the full tagged basis,
    not a many-to-one reset onto the colocated tag.  It is therefore its own
    inverse both on and away from the local code image.
    """
    output: dict[tuple[Position, Position], np.ndarray] = {}
    for (body, reservoir), value in state.reservoir.items():
        for direction in range(6):
            amplitude = value[direction]
            expected_upstream = add_position(body, direction, -1)
            if reservoir == expected_upstream:
                target_reservoir = body
            elif reservoir == body:
                target_reservoir = expected_upstream
            else:
                target_reservoir = reservoir
            output.setdefault((body, target_reservoir), zero_vector())[
                direction
            ] += amplitude
    return SiteState(output, {key: value.copy() for key, value in state.field.items()})


def site_field_stream(state: SiteState, *, inverse: bool = False) -> SiteState:
    output: dict[tuple[Position, Position], np.ndarray] = {}
    sign = -1 if inverse else 1
    for (body, field), value in state.field.items():
        for direction in range(6):
            moved_field = add_position(field, direction, sign)
            output.setdefault((body, moved_field), zero_pair())[
                :, direction
            ] += value[:, direction]
    return SiteState(
        {key: value.copy() for key, value in state.reservoir.items()}, output
    )


def site_step(
    state: SiteState,
    matter_coin: np.ndarray,
    field_coin: np.ndarray,
    angle: float,
    *,
    mode: str,
) -> tuple[SiteState, SiteState | None]:
    coined = site_coin_gate(state, matter_coin, field_coin)
    sourced = site_vertex_gate(coined, angle)
    if mode == "fixed":
        body_moved = site_body_stream(sourced, co_moving=False)
        intermediate = None
    elif mode == "co_moving":
        body_moved = site_body_stream(sourced, co_moving=True)
        intermediate = None
    elif mode == "staggered":
        intermediate = site_body_stream(sourced, co_moving=False)
        body_moved = reservoir_catch_up(intermediate)
    else:
        raise ValueError(f"unknown site stream mode {mode}")
    return site_field_stream(body_moved), intermediate


def inverse_co_moving_step(
    state: SiteState,
    matter_coin: np.ndarray,
    field_coin: np.ndarray,
    angle: float,
) -> SiteState:
    unfielded = site_field_stream(state, inverse=True)
    unbodied = site_body_stream(unfielded, co_moving=True, inverse=True)
    unsourced = site_vertex_gate(unbodied, -angle)
    return site_coin_gate(unsourced, matter_coin.conj().T, field_coin.conj().T)


def inverse_staggered_step(
    state: SiteState,
    matter_coin: np.ndarray,
    field_coin: np.ndarray,
    angle: float,
) -> SiteState:
    unfielded = site_field_stream(state, inverse=True)
    uncaught = reservoir_catch_up(unfielded)
    unbodied = site_body_stream(uncaught, co_moving=False, inverse=True)
    unsourced = site_vertex_gate(unbodied, -angle)
    return site_coin_gate(unsourced, matter_coin.conj().T, field_coin.conj().T)


def rotate_site(state: SiteState, frame: np.ndarray) -> SiteState:
    direction = c210.direction_permutation(frame)

    def rotate_position(position: Position) -> Position:
        return tuple(int(value) for value in frame @ np.asarray(position))

    return SiteState(
        {
            (rotate_position(body), rotate_position(reservoir)): direction @ value
            for (body, reservoir), value in state.reservoir.items()
        },
        {
            (rotate_position(body), rotate_position(field)): direction
            @ value
            @ direction.T
            for (body, field), value in state.field.items()
        },
    )


def sparse_stream_controls(species: c210.Species, angle: float) -> None:
    print("\nFIXED / CO-MOVING / STAGGERED STREAM INTERFACE")
    carried_initial = carried.CarriedState({(0, 0, 0): c210.UNIFORM.copy()}, {})
    site_initial = carried_to_site(carried_initial)
    carried_output, _diagnostics = carried.sparse_step(
        carried_initial, species.coin, c214.FIELD_COIN, angle
    )
    carried_image = carried_to_site(carried_output)

    fixed, _ = site_step(
        site_initial, species.coin, c214.FIELD_COIN, angle, mode="fixed"
    )
    fixed_residual = site_residual(fixed, carried_image)
    fixed_leakage = coincidence_leakage(fixed)
    expected_reservoir_weight = np.cos(angle) ** 2
    check(
        "the fixed-reservoir stream has the exact tagged-position mismatch and leaves the local image",
        abs(fixed_leakage - np.sqrt(expected_reservoir_weight)) < TOLERANCE
        and abs(fixed_residual - np.sqrt(2 * expected_reservoir_weight))
        < TOLERANCE,
        {
            "reservoir_branch_weight": expected_reservoir_weight,
            "image_leakage_norm": fixed_leakage,
            "tagged_stream_residual": fixed_residual,
            "expected_residual": float(np.sqrt(2 * expected_reservoir_weight)),
        },
    )

    co_moving, _ = site_step(
        site_initial, species.coin, c214.FIELD_COIN, angle, mode="co_moving"
    )
    check(
        "the co-moving reservoir repair exactly intertwines one complete coin-vertex-stream step",
        coincidence_leakage(co_moving) < TOLERANCE
        and site_residual(co_moving, carried_image) < TOLERANCE,
        {
            "leakage": coincidence_leakage(co_moving),
            "full_step_residual": site_residual(co_moving, carried_image),
        },
    )

    staggered, intermediate = site_step(
        site_initial, species.coin, c214.FIELD_COIN, angle, mode="staggered"
    )
    if intermediate is None:
        raise AssertionError("staggered step did not expose its intermediate slice")
    staggered_restored = inverse_staggered_step(
        staggered, species.coin, c214.FIELD_COIN, angle
    )
    check(
        "the staggered matter-stream then reservoir-catch-up repair has intermediate leakage and exact macrostep closure",
        abs(coincidence_leakage(intermediate) - fixed_leakage) < TOLERANCE
        and coincidence_leakage(staggered) < TOLERANCE
        and site_residual(staggered, co_moving) < TOLERANCE
        and site_residual(staggered_restored, site_initial) < TOLERANCE,
        {
            "intermediate_leakage": coincidence_leakage(intermediate),
            "final_leakage": coincidence_leakage(staggered),
            "staggered_vs_co_moving": site_residual(staggered, co_moving),
            "staggered_inverse_residual": site_residual(
                staggered_restored, site_initial
            ),
        },
    )

    adversarial_body = (2, -1, 0)
    adversarial_direction = 0
    adversarial_upstream = add_position(
        adversarial_body, adversarial_direction, -1
    )
    upstream_amplitude = zero_vector()
    upstream_amplitude[adversarial_direction] = 0.6 + 0.2j
    colocated_amplitude = zero_vector()
    colocated_amplitude[adversarial_direction] = -0.3 + 0.5j
    off_image = SiteState(
        {
            (adversarial_body, adversarial_upstream): upstream_amplitude,
            (adversarial_body, adversarial_body): colocated_amplitude,
        },
        {},
    )
    caught_once = reservoir_catch_up(off_image)
    caught_twice = reservoir_catch_up(caught_once)
    check(
        "the catch-up is a norm-preserving involution on an adversarial off-image tagged state",
        abs(site_norm(caught_once) - site_norm(off_image)) < TOLERANCE
        and site_residual(caught_twice, off_image) < TOLERANCE
        and abs(
            caught_once.reservoir[(adversarial_body, adversarial_body)][
                adversarial_direction
            ]
            - upstream_amplitude[adversarial_direction]
        )
        < TOLERANCE
        and abs(
            caught_once.reservoir[(adversarial_body, adversarial_upstream)][
                adversarial_direction
            ]
            - colocated_amplitude[adversarial_direction]
        )
        < TOLERANCE,
        {
            "norm_residual": abs(site_norm(caught_once) - site_norm(off_image)),
            "involution_residual": site_residual(caught_twice, off_image),
        },
    )

    carried_state = carried_initial
    site_state = site_initial
    multi_tick_residuals = []
    for _tick in range(4):
        carried_state, _ = carried.sparse_step(
            carried_state, species.coin, c214.FIELD_COIN, angle
        )
        site_state, _ = site_step(
            site_state,
            species.coin,
            c214.FIELD_COIN,
            angle,
            mode="co_moving",
        )
        multi_tick_residuals.append(
            site_residual(site_state, carried_to_site(carried_state))
        )
    restored = site_state
    for _tick in range(4):
        restored = inverse_co_moving_step(
            restored, species.coin, c214.FIELD_COIN, angle
        )
    check(
        "the co-moving interface remains exact for four ticks and is reversible",
        max(multi_tick_residuals) < TOLERANCE
        and site_residual(restored, site_initial) < TOLERANCE,
        {
            "maximum_four_tick_intertwiner_residual": max(multi_tick_residuals),
            "inverse_residual": site_residual(restored, site_initial),
        },
    )


def covariance_and_deletion_controls(species: c210.Species, angle: float) -> None:
    print("\nSPARSE COVARIANCE / DELETION / SCOPE")
    rng = np.random.default_rng(2026071703)
    carried_random = carried.CarriedState(
        {
            (1, -1, 0): rng.normal(size=6) + 1j * rng.normal(size=6),
        },
        {
            ((0, 0, 0), (0, 0, 0)): rng.normal(size=(6, 6))
            + 1j * rng.normal(size=(6, 6)),
            ((-1, 0, 1), (1, 0, -1)): rng.normal(size=(6, 6))
            + 1j * rng.normal(size=(6, 6)),
        },
    )
    carried_random = scale_carried(
        carried_random, 1 / np.sqrt(carried.state_norm(carried_random))
    )
    site_random = carried_to_site(carried_random)
    reference_co, _ = site_step(
        site_random, species.coin, c214.FIELD_COIN, angle, mode="co_moving"
    )
    reference_staggered, _ = site_step(
        site_random, species.coin, c214.FIELD_COIN, angle, mode="staggered"
    )
    covariance = []
    staggered_covariance = []
    for frame in c210.proper_cubic_frames():
        rotated = rotate_site(site_random, frame)
        rotated_co, _ = site_step(
            rotated, species.coin, c214.FIELD_COIN, angle, mode="co_moving"
        )
        rotated_staggered, _ = site_step(
            rotated, species.coin, c214.FIELD_COIN, angle, mode="staggered"
        )
        covariance.append(
            site_residual(rotated_co, rotate_site(reference_co, frame))
        )
        staggered_covariance.append(
            site_residual(
                rotated_staggered, rotate_site(reference_staggered, frame)
            )
        )
    check(
        "the co-moving and staggered repaired macrosteps are covariant under all 24 proper-cubic frames",
        len(covariance) == len(staggered_covariance) == 24
        and max(covariance + staggered_covariance) < TOLERANCE,
        {
            "co_moving_maximum": max(covariance),
            "staggered_maximum": max(staggered_covariance),
        },
    )

    deleted_carried = carried.CarriedState({(0, 0, 0): c210.UNIFORM.copy()}, {})
    deleted_site = carried_to_site(deleted_carried)
    deleted_carried, _ = carried.sparse_step(
        deleted_carried, species.coin, c214.FIELD_COIN, 0.0
    )
    deleted_co, _ = site_step(
        deleted_site, species.coin, c214.FIELD_COIN, 0.0, mode="co_moving"
    )
    deleted_fixed, _ = site_step(
        deleted_site, species.coin, c214.FIELD_COIN, 0.0, mode="fixed"
    )
    check(
        "coupling deletion preserves the co-moving interface while maximizing the fixed-reservoir stream mismatch",
        site_residual(deleted_co, carried_to_site(deleted_carried)) < TOLERANCE
        and abs(site_residual(deleted_fixed, carried_to_site(deleted_carried)) - np.sqrt(2))
        < TOLERANCE,
        {
            "co_moving_deletion_residual": site_residual(
                deleted_co, carried_to_site(deleted_carried)
            ),
            "fixed_deletion_residual": site_residual(
                deleted_fixed, carried_to_site(deleted_carried)
            ),
        },
    )

    phases = tuple(
        np.exp(1j * CONTACT_COUPLING * number * (number - 1) / 2)
        for number in (0, 1, 2)
    )
    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    check(
        "the interface preserves the one-particle mass fixture; the separate contact fixture is not applied",
        abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(phases[0] - 1) < TOLERANCE
        and abs(phases[1] - 1) < TOLERANCE
        and abs(phases[2] - np.exp(1j * CONTACT_COUPLING)) < TOLERANCE,
        {
            "analytic_mass": species.analytic_mass,
            "dispersion_mass": dispersion_mass,
            "executed_matter_number": 1,
            "contact_applied": False,
        },
    )


def main() -> int:
    species = c219.common_species(BETA)
    angle = COUPLING * species.analytic_mass
    note_contract()
    local_interface_controls(species, angle)
    sparse_stream_controls(species, angle)
    covariance_and_deletion_controls(species, angle)
    print(
        "DIAGNOSTIC",
        {
            "beta": BETA,
            "angle": angle,
            "local_interface": "direction x seven-state Q=1 block",
            "fixed_stream": "reservoir tag remains at departure cell",
            "co_moving_repair": "reservoir tag follows matter edge",
            "staggered_repair": "matter stream then reservoir catch-up",
            "physical_boundary": "logical matter direction; no Cycle269 state encoder",
        },
    )
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
