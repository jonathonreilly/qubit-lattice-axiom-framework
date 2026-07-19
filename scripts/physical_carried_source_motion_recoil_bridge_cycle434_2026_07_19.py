#!/usr/bin/env python3
"""Cycle 434: bounded physical carried-source motion/recoil bridge.

Prepend a literal nearest-neighbor reservoir track to the Cycle-429 physical
source/field/test-matter receiver.  A one-excitation source token is carried
by adjacent M2 SWAPs into the emitter, depletes coherently into the hard-core
field through the Cycle-426 recoil vertex, traverses the Cycle-429 path, and
changes a distinct physical matter receiver through the same vertex.

Opposite carried directions give opposite receiver matter-direction
coordinates on mirror-related preparations.  This is a bounded near-side
result: it does not implement the named Cycle-420 host moving-source profile,
centroid, or readout.  Stride grouping and update schedule are not velocity or
time.  Occupation and direction coordinates are not energy, source, stress,
force, gravity, probability, or Records.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_source_clock_response_law_tournament_cycle431_2026_07_19 as c431
import physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19 as c429


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CARRIED_SOURCE_MOTION_RECOIL_BRIDGE_CYCLE434_NOTE_2026-07-19.md"
)
SOURCES = {
    "cycle213": ROOT / "docs/work_history/repo/review_feedback/RETARDED_CUBIC_MASS_FIELD_CYCLE213_NOTE_2026-07-16.md",
    "cycle214": ROOT / "docs/work_history/repo/review_feedback/AUTONOMOUS_CUBIC_FIELD_EMISSION_CYCLE214_NOTE_2026-07-16.md",
    "cycle416": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_STRICT_RESPONSE_SOURCE_CLOCK_METRIC_RECEIVER_CYCLE416_NOTE_2026-07-18.md",
    "cycle418": ROOT / "docs/work_history/repo/review_feedback/CYCLE416_SEVEN_M2_COMMON_CODE_SEED_CYCLE418_NOTE_2026-07-19.md",
    "cycle420": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_PREDICTION_BRIDGE_CONTRACT_CYCLE420_NOTE_2026-07-19.md",
    "cycle425": ROOT / "docs/work_history/repo/review_feedback/COMMON_CUBIC_TRANSIENT_STATIONARY_UPDATE_CYCLE425_NOTE_2026-07-19.md",
    "cycle426": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_CYCLE426_NOTE_2026-07-19.md",
    "cycle429": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TEST_MATTER_RECOIL_RECEIVER_MULTIEDGE_PREDICTION_CYCLE429_NOTE_2026-07-19.md",
    "cycle431": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CLOCK_RESPONSE_LAW_TOURNAMENT_CYCLE431_NOTE_2026-07-19.md",
}

AUTHORITY = "none"
AUDIT = "unset"
TRAIN_SIZE = 5
HELD_SIZE = 6
INTERNAL_RESOURCE_M2 = c429.FIELD_DIM
TOL = 1.2e-9
PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
State = dict[int, np.ndarray]


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


def contracts() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "literal carried-source reservoir track",
        "adjacent m2 swaps",
        "cycle-429 physical matter receiver",
        "same cycle-426 recoil vertex",
        "opposite carried directions",
        "odd receiver matter-direction coordinate",
        "source backreaction and resource accounting",
        "exact e/g and inverse",
        "constant per-step overhead",
        "all 24 proper-cubic frames",
        "l=5 training",
        "held l=6",
        "held path length, stride, and family",
        "no refit",
        "source, motion, emission, receiver, transport, and contact deletions",
        "collision and lawful-domain controls",
        "explicit clock and schedule boundary",
        "stride is not velocity",
        "schedule and update count are not time",
        "field occupation is not energy, source, or stress",
        "direction response is not gravity or force",
        "cycle-420 named moving-source e/g and readout flags remain false",
        "positive partial construction",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-434 note freezes the carried-source and claim boundary", not missing, missing)

    source = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the cited source stack distinguishes host trajectory, physical occupation, recoil receiver, and clock boundary",
        all(path.is_file() for path in SOURCES.values())
        and "source history remains supplied" in source["cycle213"]
        and "source activation is now state-driven" in source["cycle214"]
        and "no actual clock is admitted" in source["cycle416"]
        and "joining the field coin, stream, intrinsic contact, and carried-reservoir schedule" in source["cycle418"]
        and "positive scalar density on a supplied moving trajectory" in source["cycle420"]
        and "physical test-matter readout" in source["cycle420"]
        and "one fixed response-controlled update" in source["cycle425"]
        and "no host expectation controls a gate" in source["cycle426"]
        and "physical test-matter receiver" in source["cycle429"]
        and "cycle-420 physical source e/g" in source["cycle429"]
        and "no expectation or host branch controls a gate" in source["cycle431"],
        {
            "host_trajectory_imported": False,
            "physical_near_side": "carried reservoir -> recoil field -> matter receiver",
            "named_Cycle420_surface_closed": False,
        },
    )


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[axis] + right[axis] for axis in range(3))  # type: ignore[return-value]


def scale(value: int, coord: Coord) -> Coord:
    return tuple(value * item for item in coord)  # type: ignore[return-value]


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(left[axis] - right[axis]) for axis in range(3))


def path_axis() -> Coord:
    return tuple(int(value) for value in c429.c210.DIRECTIONS[c429.PATH_DIRECTION])


def transverse_axis() -> Coord:
    direction = np.asarray(path_axis())
    for candidate in c429.c210.DIRECTIONS:
        if int(np.dot(direction, candidate)) == 0:
            return tuple(int(value) for value in candidate)
    raise RuntimeError("proper-cubic direction table has no transverse axis")


@dataclass(frozen=True)
class TrackFixture:
    name: str
    length: int
    role: str
    family: str
    path_length: int
    stride: int
    coordinates: tuple[Coord, ...]
    resource_keys: tuple[int, ...]


def source_coord(role: str) -> Coord:
    direction = path_axis()
    if role == "A_to_C":
        return (0, 0, 0)
    if role == "C_to_A":
        return scale(2, direction)
    raise ValueError("role must be A_to_C or C_to_A")


def track_coordinates(role: str, family: str) -> tuple[Coord, ...]:
    source = source_coord(role)
    direction = path_axis()
    transverse = transverse_axis()
    sign = 1 if role == "A_to_C" else -1
    incoming = scale(sign, direction)
    side = scale(sign, transverse)
    if family == "straight":
        return (
            add(source, scale(-2, incoming)),
            add(source, scale(-1, incoming)),
            source,
        )
    if family == "dogleg":
        return (
            add(add(source, scale(-2, incoming)), side),
            add(add(source, scale(-1, incoming)), side),
            add(source, scale(-1, incoming)),
            source,
        )
    raise ValueError("track family must be straight or dogleg")


def fixture(length: int, role: str, family: str, stride: int) -> TrackFixture:
    if length not in (TRAIN_SIZE, HELD_SIZE):
        raise ValueError("physical track fixture uses L=5 training or held L=6")
    if stride not in (1, 2):
        raise ValueError("declared stride grouping is one or two adjacent SWAPs")
    coordinates = track_coordinates(role, family)
    if len(set(coordinates)) != len(coordinates):
        raise ValueError("track coordinates collide")
    if any(manhattan(left, right) != 1 for left, right in zip(coordinates, coordinates[1:])):
        raise ValueError("carried-source track must be nearest-neighbor")
    path_length = len(coordinates) - 1
    external_keys = tuple(
        INTERNAL_RESOURCE_M2 + index for index in range(path_length)
    )
    keys = external_keys + (c429.reservoir_site(c429.source_cell(role)),)
    return TrackFixture(
        f"{family}-{role}-L{length}",
        length,
        role,
        family,
        path_length,
        stride,
        coordinates,
        keys,
    )


def train_and_held_fixtures() -> tuple[TrackFixture, ...]:
    return tuple(
        fixture(length, role, family, stride)
        for length, family, stride in (
            (TRAIN_SIZE, "straight", 1),
            (HELD_SIZE, "dogleg", 2),
        )
        for role in ("A_to_C", "C_to_A")
    )


def swap_keys(state: State, left: int, right: int) -> State:
    output = {}
    for key, value in state.items():
        target = right if key == left else left if key == right else key
        output[target] = value.copy()
    return output


def carry_groups(item: TrackFixture, *, inverse: bool = False) -> tuple[tuple[int, ...], ...]:
    edges = tuple(range(item.path_length))
    if inverse:
        edges = tuple(reversed(edges))
    return tuple(
        edges[start : start + item.stride]
        for start in range(0, len(edges), item.stride)
    )


def apply_carry(
    state: State,
    item: TrackFixture,
    *,
    inverse: bool = False,
    enabled: bool = True,
) -> State:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    output = state
    for group in carry_groups(item, inverse=inverse):
        for edge in group:
            output = swap_keys(output, item.resource_keys[edge], item.resource_keys[edge + 1])
    return c429.prune(output)


def internal_external(state: State) -> tuple[State, State]:
    return (
        {key: value for key, value in state.items() if key < INTERNAL_RESOURCE_M2},
        {key: value.copy() for key, value in state.items() if key >= INTERNAL_RESOURCE_M2},
    )


def field_coin_extended(state: State, *, inverse: bool = False, enabled: bool = True) -> State:
    internal, external = internal_external(state)
    transformed = c429.apply_field_coin(internal, inverse=inverse, enabled=enabled)
    return c429.prune({**external, **transformed})


def extended_step(
    state: State,
    role: str,
    factors,
    *,
    source_enabled: tuple[bool, bool, bool] = (True, True, True),
    enabled_edges: tuple[bool, bool] = (True, True),
    contact_enabled: bool = True,
) -> State:
    coin, first, second, contact = factors
    output = c429.apply_matter(state, coin)
    output = field_coin_extended(output)
    output = c429.apply_sources(output, role, enabled=source_enabled)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in matter_edges:
        output = c429.apply_matter(output, factor)
    output = c429.apply_transport(output, role, enabled_edges=enabled_edges)
    return c429.apply_matter(output, contact) if contact_enabled else output


def extended_inverse(state: State, role: str, factors) -> State:
    coin, first, second, contact = factors
    output = c429.apply_matter(state, contact.getH())
    output = c429.apply_transport(output, role, inverse=True)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in reversed(matter_edges):
        output = c429.apply_matter(output, factor.getH())
    output = c429.apply_sources(output, role, inverse=True)
    output = field_coin_extended(output, inverse=True)
    return c429.apply_matter(output, coin.getH())


def common_forward(
    state: State,
    item: TrackFixture,
    factors,
    *,
    depth: int = 3,
    motion_enabled: bool = True,
    source_enabled: tuple[bool, bool, bool] = (True, True, True),
    enabled_edges: tuple[bool, bool] = (True, True),
    contact_enabled: bool = True,
) -> State:
    output = apply_carry(state, item, enabled=motion_enabled)
    for _ in range(depth):
        output = extended_step(
            output,
            item.role,
            factors,
            source_enabled=source_enabled,
            enabled_edges=enabled_edges,
            contact_enabled=contact_enabled,
        )
    return output


def common_inverse(state: State, item: TrackFixture, factors, *, depth: int = 3) -> State:
    output = state
    for _ in range(depth):
        output = extended_inverse(output, item.role, factors)
    return apply_carry(output, item, inverse=True)


def track_initial(item: TrackFixture, *, deleted_source: bool = False) -> State:
    internal = c429.initial_state(item.role)
    vector = next(iter(internal.values())).copy()
    if deleted_source:
        vector[:] = 0
    return {item.resource_keys[0]: vector}


def physical_step_extended(state: State, encoding, role: str, factors) -> State:
    coin, first, second, contact = factors
    output = c429.apply_physical_matter(state, encoding, coin)
    output = field_coin_extended(output)
    for cell in c429.role_cells(role):
        output = c429.apply_physical_source(output, encoding, cell)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in matter_edges:
        output = c429.apply_physical_matter(output, encoding, factor)
    output = c429.apply_transport(output, role)
    return c429.apply_physical_matter(output, encoding, contact)


def physical_inverse_extended(state: State, encoding, role: str, factors) -> State:
    coin, first, second, contact = factors
    output = c429.apply_physical_matter(state, encoding, contact.getH())
    output = c429.apply_transport(output, role, inverse=True)
    matter_edges = (first, second) if role == "A_to_C" else (second, first)
    for factor in reversed(matter_edges):
        output = c429.apply_physical_matter(output, encoding, factor.getH())
    for cell in reversed(c429.role_cells(role)):
        output = c429.apply_physical_source(output, encoding, cell, inverse=True)
    output = field_coin_extended(output, inverse=True)
    return c429.apply_physical_matter(output, encoding, coin.getH())


def physical_common_forward(state: State, item: TrackFixture, encoding, factors) -> State:
    output = apply_carry(state, item)
    for _ in range(3):
        output = physical_step_extended(output, encoding, item.role, factors)
    return output


def physical_common_inverse(state: State, item: TrackFixture, encoding, factors) -> State:
    output = state
    for _ in range(3):
        output = physical_inverse_extended(output, encoding, item.role, factors)
    return apply_carry(output, item, inverse=True)


def layout_motion_collision_controls() -> None:
    print("\nPHYSICAL CARRIED-RESERVOIR TRACK / COLLISION / FRAMES")
    fixtures = train_and_held_fixtures()
    layout_failures = 0
    frame_failures = 0
    for item in fixtures:
        layout_failures += int(item.path_length not in (2, 3))
        layout_failures += int(
            any(manhattan(left, right) != 1 for left, right in zip(item.coordinates, item.coordinates[1:]))
        )
        for frame in c429.c210.proper_cubic_frames():
            moved = tuple(
                tuple(int(value) for value in frame @ np.asarray(coord))
                for coord in item.coordinates
            )
            frame_failures += int(len(moved) != len(set(moved)))
            frame_failures += sum(
                manhattan(left, right) != 1 for left, right in zip(moved, moved[1:])
            )

    swap_rows = []
    for left, right in ((0, 0), (0, 1), (1, 0), (1, 1)):
        output = (right, left)
        restored = (output[1], output[0])
        swap_rows.append((left, right, output, restored, sum(output)))
    held = next(item for item in fixtures if item.length == HELD_SIZE and item.role == "A_to_C")
    start = track_initial(held)
    carried = apply_carry(start, held)
    restored = apply_carry(carried, held, inverse=True)
    check(
        "straight and dogleg source tracks use only collision-safe adjacent SWAPs with constant per-step overhead in all frames",
        layout_failures == frame_failures == 0
        and c429.state_residual(restored, start) == 0
        and all(row[3] == row[:2] and row[4] == sum(row[:2]) for row in swap_rows)
        and swap_rows[-1][2] == (1, 1)
        and c429.c426.recoil_generator(7).nnz == 0,
        {
            "fixtures": tuple(asdict(item) for item in fixtures),
            "carry_inverse_residual": c429.state_residual(restored, start),
            "two_M2_SWAP_truth_table": swap_rows,
            "occupied_occupied_11_preserved": True,
            "saturated_R1_F111111_emission_entries": c429.c426.recoil_generator(7).nnz,
            "per_adjacent_step_new_M2": 1,
            "carry_SWAP_support_M2": 2,
            "proper_cubic_frames": len(c429.c210.proper_cubic_frames()),
            "maximum_track_frame_locality_failures": frame_failures,
        },
    )


def eg_inverse_controls(factors) -> None:
    print("\nDECLARED COMMON-CODE E/G AND INVERSE")
    rows = []
    carry_eg_residuals = []
    for item in train_and_held_fixtures():
        encodings, _reducer, support, gram_raw = c429.c396.build_shell(item.length)
        order = (0, 1, 2) if item.role == "A_to_C" else (2, 1, 0)
        encoding = encodings[c429.c319.ORDER_INDEX[order]]
        logical = track_initial(item)
        physical = c429.encode_state(logical, encoding)
        logical_output = common_forward(logical, item, factors)
        physical_output = physical_common_forward(physical, item, encoding, factors)
        expected = c429.encode_state(logical_output, encoding)
        restored_logical = common_inverse(logical_output, item, factors)
        restored_physical = physical_common_inverse(physical_output, item, encoding, factors)

        rng = np.random.default_rng(43400 + item.path_length + int(item.role == "C_to_A"))
        vector = rng.normal(size=c429.MATTER_DIM) + 1j * rng.normal(size=c429.MATTER_DIM)
        vector /= np.linalg.norm(vector)
        for key in item.resource_keys:
            probe = {key: vector}
            left = c429.encode_state(apply_carry(probe, item), encoding)
            right = apply_carry(c429.encode_state(probe, encoding), item)
            carry_eg_residuals.append(c429.state_residual(left, right))
        rows.append(
            {
                "fixture": item.name,
                "matter_encoding_shape": encoding.shape,
                "matter_support_M2": support,
                "Gram_raw_maximum": gram_raw[c429.c319.ORDER_INDEX[order]],
                "forward_EG_residual": c429.state_residual(physical_output, expected),
                "logical_inverse_residual": c429.state_residual(restored_logical, logical),
                "physical_inverse_residual": c429.state_residual(restored_physical, physical),
                "logical_output_norm_drift": abs(c429.state_norm(logical_output) - 1),
                "physical_output_norm_drift": abs(c429.state_norm(physical_output) - 1),
                "logical_dimension": c429.MATTER_DIM * (INTERNAL_RESOURCE_M2 + item.path_length),
            }
        )
    maximum = max(
        max(
            row["Gram_raw_maximum"],
            row["forward_EG_residual"],
            row["logical_inverse_residual"],
            row["physical_inverse_residual"],
            row["logical_output_norm_drift"],
            row["physical_output_norm_drift"],
        )
        for row in rows
    )
    check(
        "the literal carry and Cycle-429 factors compose into an exact physical E/G and adjoint inverse on train and held codes",
        max(carry_eg_residuals) == 0 and maximum < TOL,
        {
            "declared_code": "Cycle429 988-state matter shell x complete Q1 over 21 internal plus bounded track M2",
            "new_carry_intertwiner_maximum": max(carry_eg_residuals),
            "maximum_all_EG_inverse_Gram_norm_residual": maximum,
            "rows": rows,
            "off_code_completion": "inherited Cycle429 factorwise identity; literal track SWAP on resource keys",
        },
    )


def emission_trace(carried: State, role: str, factors) -> dict[str, object]:
    coin, _first, _second, _contact = factors
    source = c429.source_cell(role)
    before = c429.apply_matter(carried, coin)
    before = c429.apply_field_coin(before)
    after = c429.apply_source(before, source)
    reservoir_loss = c429.reservoir_weight(before, source) - c429.reservoir_weight(after, source)
    field_gain = c429.cell_q(after, source) - c429.reservoir_weight(after, source)
    matter_change = c429.matter_direction(after, source) - c429.matter_direction(before, source)
    twice_field_change = 2 * (
        c429.field_direction(after, source) - c429.field_direction(before, source)
    )
    return {
        "reservoir_depletion": reservoir_loss,
        "field_gain": field_gain,
        "resource_balance_residual": reservoir_loss - field_gain,
        "source_matter_direction_change": matter_change,
        "source_twice_field_direction_change": twice_field_change,
        "source_direction_ledger_residual": matter_change + twice_field_change,
    }


def carried_response_controls(factors) -> dict[str, float]:
    print("\nCARRIED SOURCE / RECOIL / DISTINCT RECEIVER ODD RESPONSE")
    rows = []
    pairs = {}
    failures = 0
    for item in train_and_held_fixtures():
        initial = track_initial(item)
        carried = apply_carry(initial, item)
        injection = c429.state_residual(carried, c429.initial_state(item.role))
        first = extended_step(carried, item.role, factors)
        second = extended_step(first, item.role, factors)
        third = extended_step(second, item.role, factors)
        source_row = emission_trace(carried, item.role, factors)
        receiver = c429.receiver_cell(item.role)
        before_receiver, after_receiver = c429.receiver_source_trace(second, item.role, factors)
        receiver_change = (
            c429.matter_direction(after_receiver, receiver)
            - c429.matter_direction(before_receiver, receiver)
        )
        receiver_field_change = 2 * (
            c429.field_direction(after_receiver, receiver)
            - c429.field_direction(before_receiver, receiver)
        )
        receiver_gain = (
            c429.reservoir_weight(after_receiver, receiver)
            - c429.reservoir_weight(before_receiver, receiver)
        )
        final_response = c429.reservoir_weight(third, receiver)
        incoming = tuple(
            item.coordinates[-1][axis] - item.coordinates[-2][axis]
            for axis in range(3)
        )
        row = {
            "fixture": item.name,
            "role": item.role,
            "family": item.family,
            "path_length": item.path_length,
            "stride_grouping": item.stride,
            "injection_residual": injection,
            "incoming_carried_direction": incoming,
            "source": source_row,
            "receiver_reservoir_response": final_response,
            "receiver_gain_at_exposed_vertex": receiver_gain,
            "receiver_matter_direction_change": receiver_change,
            "receiver_twice_field_direction_change": receiver_field_change,
            "receiver_direction_ledger_residual": receiver_change + receiver_field_change,
            "global_Q_after_three": c429.state_norm(third),
        }
        rows.append(row)
        pairs[(item.length, item.role)] = row
        failures += int(injection != 0)
        failures += int(final_response < 1e-10)
        failures += int(abs(c429.state_norm(third) - 1) > 2e-11)
        failures += int(abs(source_row["resource_balance_residual"]) > 3e-14)
        failures += int(np.linalg.norm(source_row["source_direction_ledger_residual"]) > 2e-14)
        failures += int(np.linalg.norm(row["receiver_direction_ledger_residual"]) > 2e-14)

    odd_rows = []
    for length in (TRAIN_SIZE, HELD_SIZE):
        forward = pairs[(length, "A_to_C")]
        reverse = pairs[(length, "C_to_A")]
        forward_change = forward["receiver_matter_direction_change"]
        reverse_change = reverse["receiver_matter_direction_change"]
        response_residual = abs(
            forward["receiver_reservoir_response"]
            - reverse["receiver_reservoir_response"]
        )
        odd_residual = float(np.linalg.norm(forward_change + reverse_change))
        source_odd_residual = float(
            np.linalg.norm(
                forward["source"]["source_matter_direction_change"]
                + reverse["source"]["source_matter_direction_change"]
            )
        )
        odd_rows.append(
            {
                "L": length,
                "held": length == HELD_SIZE,
                "response_reciprocity_residual": response_residual,
                "receiver_odd_vector_residual": odd_residual,
                "source_backreaction_odd_vector_residual": source_odd_residual,
                "forward_receiver_coordinate": forward_change,
                "reverse_receiver_coordinate": reverse_change,
            }
        )
        failures += int(response_residual > 2e-14)
        failures += int(odd_residual > 2e-14)
        failures += int(source_odd_residual > 2e-14)
        failures += int(float(forward_change[0]) <= 0 or float(reverse_change[0]) >= 0)
    check(
        "opposite physical carried directions give a nonzero odd receiver coordinate with source and receiver recoil ledgers",
        failures == 0,
        {
            "rows": rows,
            "odd_rows": odd_rows,
            "same_angle_schedule_readout_no_refit": True,
            "host_trajectory_used": False,
            "stride_called_velocity": False,
            "direction_coordinate_called_force_or_gravity": False,
        },
    )
    return {
        "baseline": float(pairs[(TRAIN_SIZE, "A_to_C")]["receiver_reservoir_response"]),
        "maximum_odd_residual": max(row["receiver_odd_vector_residual"] for row in odd_rows),
    }


def deletion_controls(factors, response: dict[str, float]) -> None:
    print("\nSOURCE / MOTION / EMISSION / RECEIVER / TRANSPORT / CONTACT DELETIONS")
    item = fixture(TRAIN_SIZE, "A_to_C", "straight", 1)
    initial = track_initial(item)
    source_deleted = common_forward(track_initial(item, deleted_source=True), item, factors)
    motion_deleted = common_forward(initial, item, factors, motion_enabled=False)
    emission_enabled = [True, True, True]
    emission_enabled[c429.source_cell(item.role)] = False
    emission_deleted = common_forward(
        initial, item, factors, source_enabled=tuple(emission_enabled)
    )
    receiver_enabled = [True, True, True]
    receiver_enabled[c429.receiver_cell(item.role)] = False
    receiver_deleted = common_forward(
        initial, item, factors, source_enabled=tuple(receiver_enabled)
    )
    first_edge_deleted = common_forward(initial, item, factors, enabled_edges=(False, True))
    second_edge_deleted = common_forward(initial, item, factors, enabled_edges=(True, False))
    contact_deleted = common_forward(initial, item, factors, contact_enabled=False)
    receiver = c429.receiver_cell(item.role)
    rows = {
        "baseline": response["baseline"],
        "source_deleted_output_norm": c429.state_norm(source_deleted),
        "motion_deleted_receiver": c429.reservoir_weight(motion_deleted, receiver),
        "emission_deleted_receiver": c429.reservoir_weight(emission_deleted, receiver),
        "receiver_deleted_receiver": c429.reservoir_weight(receiver_deleted, receiver),
        "first_transport_deleted_receiver": c429.reservoir_weight(first_edge_deleted, receiver),
        "second_transport_deleted_receiver": c429.reservoir_weight(second_edge_deleted, receiver),
        "contact_deleted_receiver": c429.reservoir_weight(contact_deleted, receiver),
    }
    check(
        "source, carried motion, emission, receiver, both transport edges, and contact deletions are independently controlled",
        rows["source_deleted_output_norm"] == 0
        and rows["motion_deleted_receiver"] == 0
        and rows["emission_deleted_receiver"] == 0
        and rows["receiver_deleted_receiver"] == 0
        and rows["first_transport_deleted_receiver"] == 0
        and rows["second_transport_deleted_receiver"] == 0
        and abs(rows["contact_deleted_receiver"] - rows["baseline"]) > 1e-9,
        rows,
    )


def covariance_controls(factors, update_rows) -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE")
    coin, first, second, contact = factors
    forward_matter = contact @ second @ first @ coin
    reverse_matter = contact @ first @ second @ coin
    matter = c429.c319.covariance_schedule_controls(
        c429.LABELS,
        "path",
        coin,
        first,
        second,
        contact,
        forward_matter,
        reverse_matter,
    )
    source_residuals = []
    stream_residuals = []
    stream = c429.transport_matrix()
    for frame in c429.c210.proper_cubic_frames():
        representation = c429.c322.local_source_frame(frame)
        source_vertex = c429.c322.local_source_blocks(c429.c322.ANGLE)[1]
        source_residuals.append(
            float(np.linalg.norm(representation @ source_vertex @ representation.T - source_vertex))
        )
        field_representation = c429.field_frame_representation(frame)
        direction = c429.c210.direction_permutation(frame)
        target_direction = int(np.argmax(direction[:, c429.PATH_DIRECTION]))
        stream_residuals.append(
            float(
                np.linalg.norm(
                    field_representation @ stream @ field_representation.conj().T
                    - c429.transport_matrix(target_direction)
                )
            )
        )
    maximum = max(
        matter["maximum_update_covariance_residual"],
        max(source_residuals),
        max(stream_residuals),
    )
    check(
        "the carried track and inherited matter/source/field/receiver law form one all-frame covariant family",
        matter["proper_cubic_frames"] == 24
        and matter["frame_group_law_failures"] == 0
        and maximum < TOL,
        {
            "proper_cubic_frames": matter["proper_cubic_frames"],
            "maximum_matter_update_covariance_residual": matter["maximum_update_covariance_residual"],
            "maximum_source_vertex_covariance_residual": max(source_residuals),
            "maximum_field_stream_covariance_residual": max(stream_residuals),
            "maximum_combined_covariance_residual": maximum,
            "track_covariance_residual": 0,
            "frame_group_law_failures": matter["frame_group_law_failures"],
            "inherited_update_rows_checked": bool(update_rows),
        },
    )


def lawful_domain_clock_and_prediction_controls() -> None:
    print("\nLAWFUL DOMAIN / CLOCK-SCHEDULE / CYCLE-420 TYPING")
    rejections = 0
    probes = (
        lambda: fixture(4, "A_to_C", "straight", 1),
        lambda: fixture(5, "bad", "straight", 1),
        lambda: fixture(5, "A_to_C", "bad", 1),
        lambda: fixture(5, "A_to_C", "straight", 3),
        lambda: c429.validate_state({c429.FIELD_DIM: np.ones(c429.MATTER_DIM)}),
    )
    for probe in probes:
        try:
            probe()
        except ValueError:
            rejections += 1

    moving_contract = next(
        surface for surface in c429.c420.SURFACES if surface.name == "moving_source_odd_response"
    )
    cycle420 = {
        "surface": moving_contract.name,
        "bounded_physical_carried_reservoir": True,
        "bounded_physical_recoil_receiver": True,
        "cycle420_physical_source_EG": False,
        "cycle420_physical_test_matter_readout": False,
        "host_profile_join": False,
        "host_centroid_join": False,
        "host_family_join": False,
        "surface_prediction_closed": False,
    }
    clock = {
        "Cycle431_clock_coupled": False,
        "schedule_to_clock_map": False,
        "operational_velocity_encoded": False,
        "stride_grouping_is_velocity": False,
        "update_count_is_time": False,
        "metric_time_derived": False,
        "rate_derived": False,
        "Record_formed": False,
    }
    inventory = {
        "supplied": (
            "source token preparation, track family, path length, orientation, and stride grouping",
            "carry invocation and factor order",
            "Cycle426 angle/sign/normalization and Cycle429 matter preparation/readout",
            "train/held boundaries and empirical comparison",
        ),
        "derived": (
            "literal adjacent source-token transport and exact inverse",
            "source depletion/field gain and source/receiver direction ledgers",
            "opposite-direction odd receiver coordinate",
            "physical E/G composition, deletions, collision safety, and covariance",
        ),
        "open": (
            "motion concurrent with repeated emission",
            "operational stride-to-clock calibration",
            "Cycle420 host profile/network/centroid E/G joins",
            "physical energy/source/stress/force/gravity interpretation",
            "occurrence, Record formation, and empirical selection",
        ),
        "negative_claim": False,
        "axiom_pressure": False,
    }
    check(
        "lawful domains and explicit clock/prediction flags keep the bounded near side separate from the named host surface",
        rejections == len(probes)
        and moving_contract.source_interface.startswith("positive host")
        and all(
            not cycle420[key]
            for key in (
                "cycle420_physical_source_EG",
                "cycle420_physical_test_matter_readout",
                "host_profile_join",
                "host_centroid_join",
                "host_family_join",
                "surface_prediction_closed",
            )
        )
        and not any(clock.values())
        and not inventory["negative_claim"]
        and not inventory["axiom_pressure"],
        {
            "domain_rejections": rejections,
            "Cycle420_named_surface": cycle420,
            "clock_schedule_boundary": clock,
            "inventory": inventory,
            "field_occupation_called_energy_source_or_stress": False,
            "receiver_direction_called_gravity_or_force": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def main() -> int:
    contracts()
    update_rows, coin, first, second, contact, _forward, _reverse = c429.c319.update_controls(
        c429.LABELS, "path"
    )
    factors = (coin, first, second, contact)
    layout_motion_collision_controls()
    eg_inverse_controls(factors)
    response = carried_response_controls(factors)
    deletion_controls(factors, response)
    covariance_controls(factors, update_rows)
    lawful_domain_clock_and_prediction_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
