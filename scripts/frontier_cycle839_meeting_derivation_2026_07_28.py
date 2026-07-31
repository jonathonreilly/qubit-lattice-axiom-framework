#!/usr/bin/env python3
"""Cycle 839: exact two-arc meeting theorem and causal-derivation attempt.

The graph-wavefront construction is kept distinct from the landed controller:
the former expands in both directions on C11, while the latter common-
translates every live A-rail token.  Later certificates test the proposed
bridge without executing either the Cycle-837 or Cycle-830 primary.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle837_why_sep5_2026_07_28.py",
)

import ast
import base64
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
RING_STATIONS = 11
SEPARATIONS = tuple(range(1, RING_STATIONS // 2 + 1))
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
MECHANISM_ENTRY_MOVEMENTS = 14739
MECHANISM_ENTRY_CONTROLLER_TICKS = (
    MECHANISM_ENTRY_MOVEMENTS * RING_STATIONS
)
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
HISTORICAL_830_COMMIT = "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744"
HISTORICAL_830_PATH = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py"
)
HISTORICAL_830_SPEC = (
    f"{HISTORICAL_830_COMMIT}:{HISTORICAL_830_PATH}"
)
EXPECTED_830_SOURCE_SHA256 = (
    "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58"
)
EXPECTED_830_SOURCE_GIT_BLOB = (
    "98b1571228ad0902301b6853208ef249ea2c2973"
)
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_SSTAR_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)
EXPECTED_SSTAR_BIT_TUPLE_SHA256 = (
    "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a"
)
EXPECTED_REACHING_KEYS = (
    (0, (1, 6)),
    (0, (1, 7)),
    (0, (2, 7)),
    (0, (2, 8)),
    (0, (3, 8)),
    (0, (3, 9)),
    (0, (4, 9)),
    (0, (4, 10)),
    (0, (5, 10)),
)
EXPECTED_CONTROLLER_TICK_HITS = tuple(
    (tick, key)
    for tick in range(
        MECHANISM_ENTRY_CONTROLLER_TICKS - 4,
        MECHANISM_ENTRY_CONTROLLER_TICKS + 1,
    )
    for key in EXPECTED_REACHING_KEYS
    if tick >= (
        MECHANISM_ENTRY_CONTROLLER_TICKS - (key[1][0] - 1)
    )
)

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def arc_vertices(
    start: int,
    direction: int,
    length: int,
) -> tuple[int, ...]:
    return tuple(
        (start + direction * offset) % RING_STATIONS
        for offset in range(length + 1)
    )


def enumerated_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    for tick in range(length + 1):
        from_left = {
            vertices[index] for index in range(length + 1)
            if index <= tick
        }
        from_right = {
            vertices[index] for index in range(length + 1)
            if length - index <= tick
        }
        overlap = from_left & from_right
        if overlap:
            return tick, tuple(
                station for station in vertices if station in overlap
            )
    raise AssertionError(("arc wavefronts did not meet", vertices))


def theorem_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    tick = (length + 1) // 2
    return tick, tuple(vertices[length - tick:tick + 1])


def source_swap_reflection(
    station: int,
    left: int,
    right: int,
) -> int:
    return (left + right - station) % RING_STATIONS


def oriented_pairs(separation: int) -> tuple[Pair, ...]:
    return tuple(
        (left, (left + separation) % RING_STATIONS)
        for left in range(RING_STATIONS)
    )


def pair_meeting_row(left: int, separation: int) -> dict[str, object]:
    right = (left + separation) % RING_STATIONS
    short_arc = arc_vertices(left, +1, separation)
    long_arc = arc_vertices(left, -1, RING_STATIONS - separation)
    short_formula = theorem_arc_meeting(short_arc)
    long_formula = theorem_arc_meeting(long_arc)
    short_enumerated = enumerated_arc_meeting(short_arc)
    long_enumerated = enumerated_arc_meeting(long_arc)
    short_centers = short_formula[1]
    long_centers = long_formula[1]
    reflection = {
        station: source_swap_reflection(station, left, right)
        for station in short_centers + long_centers
    }
    return {
        "oriented_pair": (left, right),
        "arc_lengths": (separation, RING_STATIONS - separation),
        "meeting_times": (short_formula[0], long_formula[0]),
        "short_arc_meeting_stations": short_centers,
        "long_arc_meeting_stations": long_centers,
        "meeting_station_union": tuple(sorted(
            set(short_centers) | set(long_centers)
        )),
        "two_arc_time_tie": short_formula[0] == long_formula[0],
        "source_swap_reflection_on_meeting_stations": tuple(
            sorted(reflection.items())
        ),
        "short_meeting_set_reflection_invariant": {
            source_swap_reflection(station, left, right)
            for station in short_centers
        } == set(short_centers),
        "long_meeting_set_reflection_invariant": {
            source_swap_reflection(station, left, right)
            for station in long_centers
        } == set(long_centers),
        "formula_equals_enumeration": (
            short_formula == short_enumerated
            and long_formula == long_enumerated
        ),
    }


def meeting_theorem_certificate() -> dict[str, object]:
    rows = []
    all_pair_rows = {}
    for separation in SEPARATIONS:
        pair_rows = tuple(
            pair_meeting_row(left, separation)
            for left in range(RING_STATIONS)
        )
        all_pair_rows[separation] = pair_rows
        representative = pair_rows[0]
        rotation_exact = all(
            row["meeting_times"] == representative["meeting_times"]
            and row["short_arc_meeting_stations"] == tuple(
                (station + left) % RING_STATIONS
                for station in representative[
                    "short_arc_meeting_stations"
                ]
            )
            and row["long_arc_meeting_stations"] == tuple(
                (station + left) % RING_STATIONS
                for station in representative[
                    "long_arc_meeting_stations"
                ]
            )
            for left, row in enumerate(pair_rows)
        )
        rows.append({
            "separation": separation,
            "arc_lengths": representative["arc_lengths"],
            "meeting_times_short_long":
                representative["meeting_times"],
            "representative_oriented_pair":
                representative["oriented_pair"],
            "representative_short_meeting_stations":
                representative["short_arc_meeting_stations"],
            "representative_long_meeting_stations":
                representative["long_arc_meeting_stations"],
            "representative_meeting_station_union":
                representative["meeting_station_union"],
            "short_center_type": (
                "MIDPOINT_FIXED"
                if separation % 2 == 0
                else "CENTRAL_EDGE_EXCHANGED"
            ),
            "long_center_type": (
                "MIDPOINT_FIXED"
                if (RING_STATIONS - separation) % 2 == 0
                else "CENTRAL_EDGE_EXCHANGED"
            ),
            "two_arc_time_tie": representative["two_arc_time_tie"],
            "all_11_rotations_exact": rotation_exact,
            "all_11_formula_equal_enumeration": all(
                row["formula_equals_enumeration"] for row in pair_rows
            ),
            "all_11_source_swap_reflection_symmetric": all(
                row["short_meeting_set_reflection_invariant"]
                and row["long_meeting_set_reflection_invariant"]
                for row in pair_rows
            ),
        })
    expected = (
        (1, (1, 5), (0, 1), (6,)),
        (2, (1, 5), (1,), (7, 6)),
        (3, (2, 4), (1, 2), (7,)),
        (4, (2, 4), (2,), (8, 7)),
        (5, (3, 3), (2, 3), (8,)),
    )
    observed = tuple(
        (
            row["separation"],
            row["meeting_times_short_long"],
            row["representative_short_meeting_stations"],
            row["representative_long_meeting_stations"],
        )
        for row in rows
    )
    tie_separations = tuple(
        row["separation"] for row in rows if row["two_arc_time_tie"]
    )
    exact = (
        observed == expected
        and tie_separations == (5,)
        and all(row["all_11_rotations_exact"] for row in rows)
        and all(
            row["all_11_formula_equal_enumeration"] for row in rows
        )
        and all(
            row["all_11_source_swap_reflection_symmetric"]
            for row in rows
        )
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "model":
            "two counterpropagating radius-one graph wavefronts, treated "
            "separately on the two simple arcs joining each source pair",
        "rule_chain": (
            "On an arc v_0,...,v_L, tick t reaches indices k<=t from "
            "v_0 and L-k<=t from v_L.  Intersection therefore first "
            "occurs at t=ceil(L/2), with L-t<=k<=t.  The source-swap "
            "reflection k->L-k fixes an even-arc midpoint or exchanges "
            "an odd-arc central edge.  C11 supplies arc lengths s and "
            "11-s, so their first-meeting times are "
            "(ceil(s/2),ceil((11-s)/2))."
        ),
        "per_separation_table": tuple(rows),
        "simultaneous_two_arc_meeting_separations": tie_separations,
        "theorem":
            "For every unordered pair on C11 at separation s=1..5, the "
            "two arc-wise meetings have the displayed rotation-uniform, "
            "source-swap-symmetric center sets; their times tie at (3,3) "
            "if and only if s=5.",
        "pass": exact,
    }


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def git_bytes(*arguments: str) -> bytes:
    completed = subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        timeout=20,
    )
    return completed.stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode().strip()


def cyclic_separation(pair: Pair) -> int:
    left, right = pair
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def lawful_pairs() -> tuple[Pair, ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def state_bit_tuple_sha256(state: int) -> str:
    return sha256(bytes(
        (state >> wire) & 1 for wire in range(STATE_BITS)
    )).hexdigest()


def state_packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def state_set_sha256(states: tuple[int, ...]) -> str:
    hasher = sha256()
    for state in sorted(set(states)):
        hasher.update(state.to_bytes(STATE_BYTES, "little"))
    return hasher.hexdigest()


def decode_cycle830_fixtures() -> dict[str, object]:
    source = git_bytes("show", HISTORICAL_830_SPEC)
    tree = ast.parse(source, filename=HISTORICAL_830_SPEC)
    gate_encoded = literal_assignment(tree, "GATE_CONSTANTS_B85")
    family_encoded = literal_assignment(tree, "FAMILY_STATES_B85")
    target_encoded = literal_assignment(tree, "SSTAR_PACKED_B85")
    if not all(isinstance(value, str) for value in (
        gate_encoded, family_encoded, target_encoded
    )):
        raise AssertionError("Cycle-830 literal fixtures not found")
    gate_raw = zlib.decompress(base64.b85decode(gate_encoded))
    family_raw = zlib.decompress(base64.b85decode(family_encoded))
    target_raw = zlib.decompress(base64.b85decode(target_encoded))
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros = []
    for length in lengths:
        rows = []
        for _index in range(length):
            rows.append(struct.unpack(
                "<BHHH", gate_raw[offset:offset + 7]
            ))
            offset += 7
        macros.append(tuple(rows))
    pairs = lawful_pairs()
    keys = tuple(sorted(
        (event, pair)
        for event in range(2 * FIXTURE_BANKS)
        for pair in pairs
    ))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little"
        )
    target = int.from_bytes(target_raw, "little")
    source_sha = sha256(source).hexdigest()
    source_blob = git_text("rev-parse", HISTORICAL_830_SPEC)
    exact = (
        source_sha == EXPECTED_830_SOURCE_SHA256
        and source_blob == EXPECTED_830_SOURCE_GIT_BLOB
        and len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and sha256(family_raw).hexdigest()
        == EXPECTED_FAMILY_RAW_SHA256
        and len(target_raw) == STATE_BYTES
        and sha256(target_raw).hexdigest()
        == EXPECTED_SSTAR_PACKED_SHA256
        and len(pairs) == 44
        and len(keys) == len(states) == FAMILY_SIZE
        and target.bit_count() == 44
        and state_bit_tuple_sha256(target)
        == EXPECTED_SSTAR_BIT_TUPLE_SHA256
    )
    return {
        "macros": tuple(macros),
        "keys": keys,
        "states": states,
        "target": target,
        "public": {
            "source_access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY",
            "source_commit": HISTORICAL_830_COMMIT,
            "source_path": HISTORICAL_830_PATH,
            "source_sha256": source_sha,
            "source_git_blob": source_blob,
            "fixture_import_status":
                "DISCLOSED_CONDITIONAL_INPUT: hashes prevent drift but "
                "do not independently prove the historical extraction",
            "macro_gate_counts": lengths,
            "macro_gate_count": sum(lengths),
            "family_key_count": len(states),
            "state_bits": STATE_BITS,
            "target_hamming_weight": target.bit_count(),
            "target_bit_tuple_sha256": state_bit_tuple_sha256(target),
            "target_packed_sha256": state_packed_sha256(target),
            "pass": exact,
        },
    }


def build_phase_schedules(
    macros: tuple[tuple[Gate, ...], ...],
    lane_keys: tuple[Key, ...],
) -> tuple[tuple[MaskedGate, ...], ...]:
    schedules = []
    for phase in range(RING_STATIONS):
        rows = []
        for station, macro in enumerate(macros):
            lane_mask = sum(
                1 << lane
                for lane, key in enumerate(lane_keys)
                if station in {
                    (key[1][0] + phase) % RING_STATIONS,
                    (key[1][1] + phase) % RING_STATIONS,
                }
            )
            if lane_mask:
                rows.extend(
                    (kind, first, second, third, lane_mask)
                    for kind, first, second, third in macro
                )
        schedules.append(tuple(rows))
    return tuple(schedules)


def bit_slice(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        value = state
        while value:
            bit = value & -value
            columns[bit.bit_length() - 1] |= 1 << lane
            value ^= bit
    return columns


def capture_lanes(columns: list[int], lane_count: int) -> tuple[int, ...]:
    states = [0] * lane_count
    lane_limit = (1 << lane_count) - 1
    for wire, column in enumerate(columns):
        live = column & lane_limit
        while live:
            bit = live & -live
            states[bit.bit_length() - 1] |= 1 << wire
            live ^= bit
    return tuple(states)


def apply_masked(
    columns: list[int],
    schedule: tuple[MaskedGate, ...],
) -> None:
    for kind, first, second, third, lane_mask in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        elif kind == 2:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )
        else:
            raise AssertionError(("unknown gate kind", kind))


def matching_mask(
    columns: list[int],
    target: int,
    lane_mask: int,
    signature: tuple[int, ...],
) -> int:
    candidates = lane_mask
    for wire in signature:
        column = columns[wire] & lane_mask
        candidates &= column if (target >> wire) & 1 else lane_mask ^ column
        if not candidates:
            return 0
    for wire in range(STATE_BITS):
        column = columns[wire] & lane_mask
        candidates &= column if (target >> wire) & 1 else lane_mask ^ column
        if not candidates:
            return 0
    return candidates


def lane_numbers(mask: int) -> tuple[int, ...]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


def lanes_equal(
    columns: list[int],
    left_lane: int,
    right_lane: int,
) -> bool:
    return all(
        ((column >> left_lane) & 1) == ((column >> right_lane) & 1)
        for column in columns
    )


def evolve_controller_ticks(
    fixtures: dict[str, object],
) -> dict[str, object]:
    macros = fixtures["macros"]
    keys = fixtures["keys"]
    states = fixtures["states"]
    target = fixtures["target"]
    assert isinstance(macros, tuple)
    assert isinstance(keys, tuple)
    assert isinstance(states, dict)
    assert isinstance(target, int)
    replay_key = keys[0]
    lane_keys = keys + (replay_key,)
    columns = bit_slice(tuple(states[key] for key in lane_keys))
    schedules = build_phase_schedules(macros, lane_keys)
    primary_mask = (1 << len(keys)) - 1
    target_active = tuple(
        wire for wire in range(STATE_BITS) if (target >> wire) & 1
    )
    spread = tuple(sorted(set(
        index * (STATE_BITS - 1) // 191
        for index in range(192)
    )))
    signature = tuple(sorted(set(target_active + spread)))
    snapshots: dict[int, tuple[int, ...]] = {}
    exact_hits = []
    determinism_ticks = []
    expected_schedule_lengths = tuple(
        sum(len(macro) for macro in macros)
        for _phase in range(RING_STATIONS)
    )
    lane_participation = [0] * len(lane_keys)
    for schedule in schedules:
        for _kind, _first, _second, _third, mask in schedule:
            live = mask
            while live:
                bit = live & -live
                lane_participation[bit.bit_length() - 1] += 1
                live ^= bit
    schedule_shape_exact = (
        tuple(map(len, schedules)) == expected_schedule_lengths
        and all(
            count == WORD_GATE_COUNT for count in lane_participation
        )
    )

    for tick in range(1, MECHANISM_ENTRY_CONTROLLER_TICKS + 1):
        phase = (tick - 1) % RING_STATIONS
        apply_masked(columns, schedules[phase])
        if tick <= 5:
            snapshots[tick] = capture_lanes(columns, len(keys))
            determinism_ticks.append({
                "controller_tick": tick,
                "duplicate_lane_exact": lanes_equal(
                    columns, 0, len(keys)
                ),
            })
        matches = matching_mask(
            columns, target, primary_mask, signature
        )
        exact_hits.extend(
            (tick, keys[lane]) for lane in lane_numbers(matches)
        )
    determinism_ticks.append({
        "controller_tick": MECHANISM_ENTRY_CONTROLLER_TICKS,
        "duplicate_lane_exact": lanes_equal(columns, 0, len(keys)),
    })
    expected_hits = EXPECTED_CONTROLLER_TICK_HITS
    exact = (
        schedule_shape_exact
        and tuple(exact_hits) == expected_hits
        and set(snapshots) == set(range(1, 6))
        and all(
            row["duplicate_lane_exact"] for row in determinism_ticks
        )
    )
    return {
        "snapshots": snapshots,
        "public": {
            "microstep_rule":
                "At controller phase q, apply the landed macro at each "
                "live A-token station p+q in station order, then common-"
                "translate both A tokens by +1; B is clean after the step.",
            "declared_search_bound_controller_ticks":
                MECHANISM_ENTRY_CONTROLLER_TICKS,
            "equivalent_complete_movements":
                MECHANISM_ENTRY_MOVEMENTS,
            "check_granularity":
                "every completed controller tick, including all 11 "
                "within-movement phases",
            "primary_lanes": len(keys),
            "duplicate_determinism_lanes": 1,
            "phase_schedule_gate_rows":
                tuple(map(len, schedules)),
            "per_lane_gate_rows_per_complete_movement":
                tuple(sorted(set(lane_participation))),
            "signature_prefilter_wires": len(signature),
            "all_exact_target_hits": tuple(exact_hits),
            "expected_exact_target_hits": expected_hits,
            "duplicate_determinism_checks": tuple(determinism_ticks),
            "pass": exact,
        },
    }


def rail_bookkeeping(
    pair: Pair,
    tick: int,
    meeting_stations: tuple[int, ...],
) -> dict[str, object]:
    a_positions = tuple(
        (station + tick) % RING_STATIONS for station in pair
    )
    b_positions: tuple[int, ...] = ()
    left, right = pair
    reflected_a = {
        source_swap_reflection(station, left, right)
        for station in a_positions
    }
    return {
        "controller_tick": tick,
        "A_token_positions": a_positions,
        "B_token_positions": b_positions,
        "meeting_station_A_B_rows": tuple(
            (
                station,
                int(station in a_positions),
                int(station in b_positions),
            )
            for station in meeting_stations
        ),
        "A_tokens_on_meeting_stations": sum(
            station in meeting_stations for station in a_positions
        ),
        "total_A_tokens": len(a_positions),
        "total_B_tokens": len(b_positions),
        "token_collision": len(set(a_positions)) != len(a_positions),
        "A_row_source_swap_reflection_symmetric":
            reflected_a == set(a_positions),
    }


def state_projection_summary(
    states: tuple[int, ...],
    representative: int,
) -> dict[str, object]:
    return {
        "labeled_configuration_count": len(states),
        "projected_unique_5815_bit_state_count": len(set(states)),
        "projected_state_set_sha256": state_set_sha256(states),
        "hamming_weight_census": dict(sorted(Counter(
            state.bit_count() for state in states
        ).items())),
        "representative_bit_tuple_sha256":
            state_bit_tuple_sha256(representative),
        "representative_packed_sha256":
            state_packed_sha256(representative),
        "representative_hamming_weight": representative.bit_count(),
    }


def meet_configurations_certificate(
    certificate_a: dict[str, object],
    fixtures: dict[str, object],
    dynamics: dict[str, object],
) -> dict[str, object]:
    keys = fixtures["keys"]
    snapshots = dynamics["snapshots"]
    assert isinstance(keys, tuple)
    assert isinstance(snapshots, dict)
    key_index = {key: index for index, key in enumerate(keys)}
    theorem_rows = {
        int(row["separation"]): row
        for row in certificate_a["per_separation_table"]
    }
    rows = []
    for separation in SEPARATIONS:
        theorem = theorem_rows[separation]
        pair = (0, separation)
        short_tick, long_tick = theorem[
            "meeting_times_short_long"
        ]
        short_stations = theorem[
            "representative_short_meeting_stations"
        ]
        long_stations = theorem[
            "representative_long_meeting_stations"
        ]
        short_rail = rail_bookkeeping(
            pair, short_tick, short_stations
        )
        long_rail = rail_bookkeeping(
            pair, long_tick, long_stations
        )
        union_stations = theorem[
            "representative_meeting_station_union"
        ]
        tie_rail = (
            rail_bookkeeping(pair, short_tick, union_stations)
            if short_tick == long_tick else None
        )
        base = {
            "separation": separation,
            "meeting_times_short_long": (short_tick, long_tick),
            "representative_short_meeting_stations": short_stations,
            "representative_long_meeting_stations": long_stations,
            "representative_short_rail_configuration": short_rail,
            "representative_long_rail_configuration": long_rail,
            "simultaneous_union_rail_configuration": tie_rail,
            "actual_tokens_common_translate": True,
            "actual_tokens_collide_at_either_arc_meeting":
                short_rail["token_collision"]
                or long_rail["token_collision"],
            "actual_full_state_domain":
                "LANDED_PAIRWISE_SEPARATED_FAMILY"
                if separation > 1
                else "OUTSIDE_LANDED_PAIRWISE_SEPARATED_FAMILY",
        }
        if separation == 1:
            base.update({
                "lawful_key_count": 0,
                "full_state_meet_configurations":
                    "UNDEFINED_OUTSIDE_LANDED_FAMILY",
            })
        else:
            separation_keys = tuple(
                key for key in keys
                if cyclic_separation(key[1]) == separation
            )
            indices = tuple(key_index[key] for key in separation_keys)
            short_states = tuple(
                snapshots[short_tick][index] for index in indices
            )
            long_states = tuple(
                snapshots[long_tick][index] for index in indices
            )
            representative_key = (0, pair)
            representative_index = key_index[representative_key]
            base.update({
                "lawful_key_count": len(separation_keys),
                "configuration_definition":
                    "(event, fixed pair word, 5815-bit data state, "
                    "A/B controller rails) after the displayed number of "
                    "radius-one controller ticks",
                "representative_key": representative_key,
                "short_meet_full_state_projection":
                    state_projection_summary(
                        short_states,
                        snapshots[short_tick][representative_index],
                    ),
                "long_meet_full_state_projection":
                    state_projection_summary(
                        long_states,
                        snapshots[long_tick][representative_index],
                    ),
                "short_equals_long_full_state_projection":
                    short_states == long_states,
            })
        rows.append(base)
    s5 = rows[-1]
    tie_rail = s5["simultaneous_union_rail_configuration"]
    exact = (
        fixtures["public"]["pass"]
        and dynamics["public"]["pass"]
        and tuple(row["lawful_key_count"] for row in rows)
        == (0, 44, 44, 44, 44)
        and not any(
            row["actual_tokens_collide_at_either_arc_meeting"]
            for row in rows
        )
        and isinstance(tie_rail, dict)
        and tie_rail["A_tokens_on_meeting_stations"] == 2
        and tie_rail["total_A_tokens"] == 2
        and not tie_rail["A_row_source_swap_reflection_symmetric"]
        and all(
            row["simultaneous_union_rail_configuration"] is None
            for row in rows[:-1]
        )
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "meet_configurations_table": tuple(rows),
        "exact_local_consequence":
            "Only s=5 puts both common-translating A tokens on the union "
            "of the two arc-center sets at one tick.  The occupied A row "
            "is nevertheless not source-swap-reflection symmetric, B "
            "remains clean, and no token collision occurs.",
        "charge_row_boundary":
            "The landed controller rule exposes A/B token rails.  No "
            "additional meeting-station charge row is identified in the "
            "pinned Cycle-719/837 rule chain, so none is invented here.",
        "funnel_geometry_boundary":
            "Cycle 837 records the target [1,1] occupancy as bank-cell "
            "geometry, not ring-pair geometry; the meeting-center rail "
            "configuration therefore does not derive that occupancy.",
        "pass": exact,
    }


def reachability_certificate(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
    fixtures: dict[str, object],
    dynamics: dict[str, object],
) -> dict[str, object]:
    keys = fixtures["keys"]
    target = fixtures["target"]
    hits = dynamics["public"]["all_exact_target_hits"]
    assert isinstance(keys, tuple)
    assert isinstance(target, int)
    theorem_rows = {
        int(row["separation"]): row
        for row in certificate_a["per_separation_table"]
    }
    rows = []
    for separation in SEPARATIONS:
        short_tick, long_tick = theorem_rows[separation][
            "meeting_times_short_long"
        ]
        if separation == 1:
            rows.append({
                "separation": separation,
                "outcome":
                    "OUTSIDE_LANDED_PAIRWISE_SEPARATED_FAMILY",
                "short_meet_forward_bound_controller_ticks": None,
                "long_meet_forward_bound_controller_ticks": None,
                "reaching_keys": (),
            })
            continue
        separation_hits = tuple(
            (tick, key) for tick, key in hits
            if cyclic_separation(key[1]) == separation
        )
        reaching_keys = tuple(sorted({
            key for _tick, key in separation_hits
        }))
        short_reaching = tuple(
            (
                tick - short_tick,
                key,
            )
            for tick, key in separation_hits if tick >= short_tick
        )
        long_reaching = tuple(
            (
                tick - long_tick,
                key,
            )
            for tick, key in separation_hits if tick >= long_tick
        )
        rows.append({
            "separation": separation,
            "lawful_meet_configuration_count": 44,
            "target_metric":
                "exact equality of all 5815 data bits to S*; hamming "
                "weight 44 alone is not accepted",
            "short_meet_forward_bound_controller_ticks":
                MECHANISM_ENTRY_CONTROLLER_TICKS - short_tick,
            "long_meet_forward_bound_controller_ticks":
                MECHANISM_ENTRY_CONTROLLER_TICKS - long_tick,
            "short_meet_exact_reaches": short_reaching,
            "long_meet_exact_reaches": long_reaching,
            "reaching_keys": reaching_keys,
            "nonreaching_labeled_configurations":
                44 - len(reaching_keys),
            "outcome": (
                "EXACT_NINE_REACH"
                if separation == 5 else "NO_EXACT_REACH_WITHIN_BOUND"
            ),
        })
    row_by_separation = {
        int(row["separation"]): row for row in rows
    }
    s5 = row_by_separation[5]
    exact = (
        certificate_b["pass"]
        and target.bit_count() == 44
        and tuple(hits) == EXPECTED_CONTROLLER_TICK_HITS
        and all(
            not row_by_separation[separation][
                "short_meet_exact_reaches"
            ]
            and not row_by_separation[separation][
                "long_meet_exact_reaches"
            ]
            for separation in (2, 3, 4)
        )
        and s5["reaching_keys"] == EXPECTED_REACHING_KEYS
        and s5["nonreaching_labeled_configurations"] == 35
        and s5["short_meet_forward_bound_controller_ticks"]
        == MECHANISM_ENTRY_CONTROLLER_TICKS - 3
        and s5["long_meet_forward_bound_controller_ticks"]
        == MECHANISM_ENTRY_CONTROLLER_TICKS - 3
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "declared_scope":
            "All 176 landed lawful event/pair initial states; every "
            "completed controller tick from the relevant first-movement "
            "meet configuration through 14739 complete movements.",
        "target": {
            "name": "Cycle-830 event-0 S* funnel skeleton",
            "state_bits": STATE_BITS,
            "hamming_weight": target.bit_count(),
            "bit_tuple_sha256": state_bit_tuple_sha256(target),
            "packed_sha256": state_packed_sha256(target),
        },
        "per_separation_reachability": tuple(rows),
        "exact_outcome":
            "From the s=5 tick-3 meet configurations, exactly the nine "
            "event-0, origin-absent keys reach S*: a final-movement "
            "staircase starts with (5,10) at global tick 162125 and adds "
            "the left-4, left-3, left-2, then left-1 pairs through the "
            "common boundary at tick 162129.  The other 35 s=5 "
            "configurations and all 132 lawful s=2,3,4 configurations do "
            "not reach S* anywhere within their declared bounds.  s=1 "
            "is outside the landed family.",
        "pass": exact,
    }


def verdict_certificate(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
    reachability: dict[str, object],
) -> dict[str, object]:
    exact = (
        certificate_a["pass"]
        and certificate_b["pass"]
        and reachability["pass"]
    )
    return {
        "verdict": "PARTIAL" if exact else "OPEN",
        "links_that_hold": (
            "Auxiliary radius-one arc propagation gives a unique s=5 "
            "(3,3) two-arc time tie.",
            "At that tick only, both actual common-translating A tokens "
            "lie in the combined arc-center set.",
            "Within the declared exact all-microstep bound, precisely the "
            "nine event-0, origin-absent s=5 meet configurations reach "
            "the exact weight-44 S* state; every other landed lawful meet "
            "configuration does not.",
        ),
        "links_that_fail_or_remain_open": (
            "The auxiliary counterpropagating wavefront is not a state "
            "variable or update rule of the actual controller.",
            "The actual s=5 token row is not reflection-symmetric and "
            "contains no collision or identified interference/charge row.",
            "The (3,3) property is not sufficient: it labels 44 lawful "
            "event/pair configurations, while only nine reach S*.",
            "The funnel [1,1] occupancy is landed bank-cell geometry, so "
            "no rule maps the meeting-center token bookkeeping to it.",
            "The bounded family census establishes correlation and exact "
            "reachability, not a counterfactual causal mechanism or an "
            "unbounded necessity theorem.",
        ),
        "causal_chain_established": False,
        "sharp_reading":
            "PARTIAL: the meeting theorem, actual rail consequence, and "
            "bounded reach/nonreach classification hold exactly; the "
            "tie-to-funnel causal link remains open.",
        "pass": exact,
    }


def render(certificates: dict[str, object], report: dict[str, object]) -> str:
    return "\n".join((
        *(
            f"CERTIFICATE {name} {compact(value)}"
            for name, value in certificates.items()
        ),
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    )) + "\n"


def run() -> int:
    started = monotonic()
    certificate_a = meeting_theorem_certificate()
    fixtures = decode_cycle830_fixtures()
    dynamics = evolve_controller_ticks(fixtures)
    certificate_b = meet_configurations_certificate(
        certificate_a, fixtures, dynamics
    )
    reachability = reachability_certificate(
        certificate_a, certificate_b, fixtures, dynamics
    )
    certificate_c = verdict_certificate(
        certificate_a, certificate_b, reachability
    )
    replay_a = meeting_theorem_certificate()
    deterministic_a = (
        certificate_a == replay_a
        and digest(certificate_a) == digest(replay_a)
    )
    elapsed = monotonic() - started
    certificates = {
        "A_MEETING_THEOREM": certificate_a,
        "B_MEET_CONFIGURATIONS": certificate_b,
        "B_FORWARD_REACHABILITY": reachability,
        "C_VERDICT": certificate_c,
        "FIXTURE_PROVENANCE": fixtures["public"],
        "DYNAMICS_SEARCH": dynamics["public"],
    }
    checks = {
        "A_MEETING_THEOREM": bool(certificate_a["pass"]),
        "B_MEET_CONFIGURATIONS": bool(certificate_b["pass"]),
        "B_FORWARD_REACHABILITY": bool(reachability["pass"]),
        "C_HONEST_PARTIAL_VERDICT": bool(certificate_c["pass"])
            and certificate_c["verdict"] == "PARTIAL",
        "FIXTURE_PROVENANCE": bool(fixtures["public"]["pass"]),
        "MICROSTEP_DYNAMICS_SEARCH": bool(dynamics["public"]["pass"]),
        "A_DETERMINISTIC_REPLAY": deterministic_a,
        "RUNTIME_BOUND": elapsed < AUDIT_TIMEOUT_SEC,
    }
    report = {
        "cycle": 839,
        "stage": "certificates-A-B-C",
        "meeting_times_by_separation": tuple(
            (
                row["separation"],
                row["meeting_times_short_long"],
            )
            for row in certificate_a["per_separation_table"]
        ),
        "unique_tie": certificate_a[
            "simultaneous_two_arc_meeting_separations"
        ],
        "meet_configuration_outcome":
            certificate_b["exact_local_consequence"],
        "reachability_outcome": reachability["exact_outcome"],
        "verdict": certificate_c["verdict"],
        "causal_chain_established":
            certificate_c["causal_chain_established"],
        "deterministic_A_replay": deterministic_a,
        "runtime_seconds": round(elapsed, 6),
        "checks": checks,
        "pass": all(checks.values()),
        "terminal": "CYCLE839_CAUSAL_DERIVATION_HONEST_FAIL",
    }
    if report["pass"]:
        report["terminal"] = "CYCLE839_CAUSAL_DERIVATION_PARTIAL_PASS"
    output = render(certificates, report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE839_CAUSAL_DERIVATION_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
