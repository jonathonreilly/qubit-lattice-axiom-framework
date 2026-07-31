#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-845 partition braid.

The Cycle-845, Cycle-830, and Cycle-835 primaries are source evidence only:
they are SHA-pinned, parsed as text/AST, and blocked from import/execution.
The fixture decoder, Boolean evolution, state hashing, partition extraction,
normalization tests, and falsification counts are implemented in this file.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle845_partition_route_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle835_register_mechanism_2026_07_28.py",
)

import ast
import base64
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, FIXTURE_PATH, REGISTER_PATH = AUDIT_INPUT_PATHS
EXPECTED_SOURCE_SHA256 = {
    PRIMARY_PATH:
        "b97e227375a8cc14580d8f413897df2209e9e872b1a46ec59f9a2e61af593ca8",
    FIXTURE_PATH:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    REGISTER_PATH:
        "6b8c26ff77d99225aaa985c645aeee9fa1fb3db19517aec727ff38e0cbcc03f5",
}
EXPECTED_SOURCE_GIT_BLOBS = {
    PRIMARY_PATH: "3c7a6e61bbc656b7c6b69b96be36066d0ad1e8e8",
    FIXTURE_PATH: "98b1571228ad0902301b6853208ef249ea2c2973",
    REGISTER_PATH: "a9bfc3d151a591b3d0a4ba06acaa30ed04ff7e67",
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_TARGET_RAW_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)

RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
GATE_COUNT = 3106
MOVEMENT_GATE_COUNT = 6212
MEET_CONTROLLER_TICK = 3
WINDOW_DEPTH = 64
EVENT_ORDER = (0, 2, 1)
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
WITNESS_PAIR = BACKBONE[0]
REGISTER_WIRES = (
    1, 6, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 71, 75, 76, 77, 78, 79, 80, 82, 83,
    84, 86, 87, 89, 105, 109, 110, 111, 112, 113, 114, 116,
    117,
)
EXPECTED_PREUNION_WIRE_COUNTS = (15, 3, 9)
EXPECTED_SAME_TICK_COARSENINGS = 1321
EXPECTED_TOTAL_COARSENINGS = 2773

Pair = tuple[int, int]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
ScalarGate = tuple[int, int, int]
Partition = tuple[tuple[int, ...], ...]

BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in AUDIT_INPUT_PATHS
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a source primary is accidentally imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids importing {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def object_digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def git_text(*arguments: str) -> str:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    ).stdout.strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def top_level_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(f"expected one function named {name}")
    return rows[0]


def direct_import_roots(tree: ast.Module) -> tuple[str, ...]:
    roots: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".", 1)[0])
    return tuple(sorted(roots))


def cyclic_separation(pair: Pair) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def lawful_pairs() -> tuple[Pair, ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def decode_fixture(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(
        literal_assignment(tree, name)
        for name in (
            "GATE_CONSTANTS_B85",
            "FAMILY_STATES_B85",
            "SSTAR_PACKED_B85",
        )
    )
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("Cycle-830 fixture literals are missing")
    gate_raw, family_raw, target_raw = (
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros: list[tuple[Gate, ...]] = []
    for length in lengths:
        macro: list[Gate] = []
        for _ in range(length):
            macro.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(macro))
    pairs = lawful_pairs()
    keys = tuple(sorted(
        (event, pair)
        for event in range(4)
        for pair in pairs
    ))
    states = {
        key: int.from_bytes(
            family_raw[index * STATE_BYTES:(index + 1) * STATE_BYTES],
            "little",
        )
        for index, key in enumerate(keys)
    }
    target = int.from_bytes(target_raw, "little")
    exact = (
        len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and len(keys) == len(states) == 176
        and len(family_raw) == 176 * STATE_BYTES
        and len(target_raw) == STATE_BYTES
        and sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256
        and sha256(family_raw).hexdigest() == EXPECTED_FAMILY_RAW_SHA256
        and sha256(target_raw).hexdigest() == EXPECTED_TARGET_RAW_SHA256
    )
    return {
        "macros": tuple(macros),
        "states": states,
        "target": target,
        "macro_lengths": lengths,
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "target_raw_sha256": sha256(target_raw).hexdigest(),
        "pass": exact,
    }


def fixture_digest(fixture: dict[str, object]) -> str:
    payload = {
        "macro_lengths": fixture["macro_lengths"],
        "gate_raw_sha256": fixture["gate_raw_sha256"],
        "family_raw_sha256": fixture["family_raw_sha256"],
        "target_raw_sha256": fixture["target_raw_sha256"],
        "state_hashes": tuple(
            (
                key,
                packed_state_sha256(state),
            )
            for key, state in sorted(fixture["states"].items())
        ),
    }
    return object_digest(payload)


def packed_state_sha256(state: int) -> str:
    """Independent state hash: packed little-endian, unlike the primary."""

    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def hashed_partition(states: tuple[int, ...]) -> Partition:
    """Exact equality partition using our own packed-byte SHA keys."""

    groups: dict[tuple[bytes, bytes], list[int]] = {}
    for lane, state in enumerate(states):
        payload = state.to_bytes(STATE_BYTES, "little")
        key = (sha256(payload).digest(), payload)
        groups.setdefault(key, []).append(lane)
    return tuple(sorted(
        (tuple(group) for group in groups.values()),
        key=lambda group: group[0],
    ))


def varying_wires(states: tuple[int, ...]) -> tuple[int, ...]:
    varying = 0
    reference = states[0]
    for state in states[1:]:
        varying |= reference ^ state
    rows: list[int] = []
    while varying:
        bit = varying & -varying
        rows.append(bit.bit_length() - 1)
        varying ^= bit
    return tuple(rows)


def equivalent_pairs(partition: Partition) -> frozenset[tuple[int, int]]:
    return frozenset(
        pair
        for block in partition
        for pair in combinations(block, 2)
    )


def transition_kind(before: Partition, after: Partition) -> str:
    left = equivalent_pairs(before)
    right = equivalent_pairs(after)
    if left < right:
        return "COARSENING"
    if right < left:
        return "REFINEMENT"
    if left != right:
        return "MIXED"
    return "UNCHANGED"


def build_phase_schedules(
    macros: tuple[tuple[Gate, ...], ...],
    lane_specs: tuple[tuple[int, Pair], ...],
) -> tuple[tuple[MaskedGate, ...], ...]:
    """Construct gate masks by station occupancy, independently of Cycle-845."""

    phases: list[tuple[MaskedGate, ...]] = []
    for phase in range(RING_STATIONS):
        station_masks = [0] * RING_STATIONS
        for lane, pair in lane_specs:
            station_masks[(pair[0] + phase) % RING_STATIONS] |= 1 << lane
            station_masks[(pair[1] + phase) % RING_STATIONS] |= 1 << lane
        rows: list[MaskedGate] = []
        for station, lane_mask in enumerate(station_masks):
            if not lane_mask:
                continue
            rows.extend(
                (kind, first, second, third, lane_mask)
                for kind, first, second, third in macros[station]
            )
        phases.append(tuple(rows))
    return tuple(phases)


def flatten_schedule(
    phases: tuple[tuple[MaskedGate, ...], ...],
) -> tuple[MaskedGate, ...]:
    return tuple(row for phase in phases for row in phase)


def advance_columns(
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
            raise AssertionError(f"unknown gate kind {kind}")


def columns_from_states(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        remaining = state
        while remaining:
            bit = remaining & -remaining
            columns[bit.bit_length() - 1] |= 1 << lane
            remaining ^= bit
    return columns


def capture_first_lanes(
    columns: list[int],
    lane_count: int,
) -> tuple[int, ...]:
    states = [0] * lane_count
    lane_mask = (1 << lane_count) - 1
    for wire, column in enumerate(columns):
        live = column & lane_mask
        while live:
            bit = live & -live
            states[bit.bit_length() - 1] |= 1 << wire
            live ^= bit
    return tuple(states)


def capture_lane(columns: list[int], lane: int) -> int:
    lane_bit = 1 << lane
    return sum(
        1 << wire
        for wire, column in enumerate(columns)
        if column & lane_bit
    )


def register_projection(columns: list[int], lane: int) -> int:
    return sum(
        ((columns[wire] >> lane) & 1) << field
        for field, wire in enumerate(REGISTER_WIRES)
    )


def compile_scalar_words(
    macros: tuple[tuple[Gate, ...], ...],
) -> dict[Pair, tuple[ScalarGate, ...]]:
    words: dict[Pair, tuple[ScalarGate, ...]] = {}
    for pair in BACKBONE:
        rows: list[ScalarGate] = []
        for phase in range(RING_STATIONS):
            occupied = {
                (pair[0] + phase) % RING_STATIONS,
                (pair[1] + phase) % RING_STATIONS,
            }
            for station in sorted(occupied):
                for kind, first, second, third in macros[station]:
                    if kind == 0:
                        rows.append((0, 0, 1 << first))
                    elif kind == 1:
                        rows.append((1, 1 << first, 1 << second))
                    elif kind == 2:
                        rows.append((
                            2,
                            (1 << first) | (1 << second),
                            1 << third,
                        ))
                    else:
                        raise AssertionError(f"unknown gate kind {kind}")
        words[pair] = tuple(rows)
    return words


def apply_scalar_word(
    state: int,
    word: tuple[ScalarGate, ...],
    *,
    reverse: bool,
) -> int:
    rows = reversed(word) if reverse else word
    for kind, controls, target in rows:
        if kind == 0 or state & controls == controls:
            state ^= target
    return state


def run_forward_recomputation(
    fixture: dict[str, object],
) -> dict[str, object]:
    macros = fixture["macros"]
    states_by_key = fixture["states"]
    target = fixture["target"]
    assert isinstance(macros, tuple)
    assert isinstance(states_by_key, dict)
    assert isinstance(target, int)

    event0_initial = tuple(
        states_by_key[(0, pair)] for pair in BACKBONE
    )
    witness_initial = tuple(
        states_by_key[(event, WITNESS_PAIR)] for event in EVENT_ORDER
    )
    all_initial = (
        event0_initial + event0_initial
        + witness_initial + witness_initial
    )
    event0_primary = tuple(range(9))
    event0_duplicate = tuple(range(9, 18))
    witness_primary = dict(zip(EVENT_ORDER, range(18, 21)))
    witness_duplicate = dict(zip(EVENT_ORDER, range(21, 24)))
    combined_pairs = (
        BACKBONE + BACKBONE
        + (WITNESS_PAIR,) * (2 * len(EVENT_ORDER))
    )
    combined_phases = build_phase_schedules(
        macros, tuple(enumerate(combined_pairs))
    )
    combined_schedule = flatten_schedule(combined_phases)
    witness_specs = tuple(
        (lane, WITNESS_PAIR)
        for lane in tuple(witness_primary.values())
        + tuple(witness_duplicate.values())
    )
    witness_schedule = flatten_schedule(
        build_phase_schedules(macros, witness_specs)
    )

    meet_columns = columns_from_states(event0_initial + event0_initial)
    meet_phases = build_phase_schedules(
        macros, tuple(enumerate(BACKBONE + BACKBONE))
    )
    for phase in range(MEET_CONTROLLER_TICK):
        advance_columns(meet_columns, meet_phases[phase])
    meet_all = capture_first_lanes(meet_columns, 18)
    meet_states = meet_all[:9]
    meet_duplicate_exact = meet_states == meet_all[9:]
    meet_partition = hashed_partition(meet_states)

    columns = columns_from_states(all_initial)
    previous_register = {
        event: register_projection(columns, witness_primary[event])
        for event in EVENT_ORDER
    }
    register_change_sets = {
        event: [set() for _ in REGISTER_WIRES]
        for event in EVENT_ORDER
    }
    event0_partitions = [meet_partition]
    event0_coarsening_movements: list[int] = []
    previous_partition = meet_partition
    event0_tail_states: dict[int, tuple[int, ...]] = {}
    event0_tail_partitions: dict[int, Partition] = {}
    funnels: dict[int, int] = {}
    event0_duplicate_exact_every_sample = meet_duplicate_exact
    register_duplicate_exact_every_movement = True
    funnel_duplicate_exact = True

    for movement in range(1, max(FUNNEL_MOMENTS.values()) + 1):
        schedule = (
            combined_schedule
            if movement <= FUNNEL_MOMENTS[0]
            else witness_schedule
        )
        advance_columns(columns, schedule)

        for event in EVENT_ORDER:
            if movement > FUNNEL_MOMENTS[event]:
                continue
            primary_projection = register_projection(
                columns, witness_primary[event]
            )
            duplicate_projection = register_projection(
                columns, witness_duplicate[event]
            )
            register_duplicate_exact_every_movement &= (
                primary_projection == duplicate_projection
            )
            flipped = primary_projection ^ previous_register[event]
            while flipped:
                bit = flipped & -flipped
                register_change_sets[event][
                    bit.bit_length() - 1
                ].add(movement)
                flipped ^= bit
            previous_register[event] = primary_projection
            if movement == FUNNEL_MOMENTS[event]:
                funnel = capture_lane(columns, witness_primary[event])
                duplicate = capture_lane(
                    columns, witness_duplicate[event]
                )
                funnels[event] = funnel
                funnel_duplicate_exact &= funnel == duplicate

        if movement <= FUNNEL_MOMENTS[0]:
            event0_all = capture_first_lanes(columns, 18)
            event0_states = event0_all[:9]
            event0_duplicate_exact_every_sample &= (
                event0_states == event0_all[9:]
            )
            partition = hashed_partition(event0_states)
            event0_partitions.append(partition)
            if (
                partition != previous_partition
                and transition_kind(
                    previous_partition, partition
                ) == "COARSENING"
            ):
                event0_coarsening_movements.append(movement)
            previous_partition = partition
            if movement >= FUNNEL_MOMENTS[0] - WINDOW_DEPTH:
                event0_tail_states[movement] = event0_states
                event0_tail_partitions[movement] = partition

    event0_final_states = event0_tail_states[FUNNEL_MOMENTS[0]]
    witness_event0_matches_backbone = (
        funnels[0] == event0_final_states[0]
    )
    return {
        "macros": macros,
        "funnels": funnels,
        "register_change_sets": register_change_sets,
        "event0_partitions": tuple(event0_partitions),
        "event0_coarsening_movements":
            tuple(event0_coarsening_movements),
        "event0_tail_states": event0_tail_states,
        "event0_tail_partitions": event0_tail_partitions,
        "event0_final_states": event0_final_states,
        "meet_partition": meet_partition,
        "combined_schedule_rows": len(combined_schedule),
        "witness_schedule_rows": len(witness_schedule),
        "meet_duplicate_exact": meet_duplicate_exact,
        "event0_duplicate_exact_every_sample":
            event0_duplicate_exact_every_sample,
        "register_duplicate_exact_every_movement":
            register_duplicate_exact_every_movement,
        "funnel_duplicate_exact": funnel_duplicate_exact,
        "witness_event0_matches_backbone":
            witness_event0_matches_backbone,
        "event0_all_reach_target":
            all(state == target for state in event0_final_states),
        "funnel_packed_sha256": tuple(
            (event, packed_state_sha256(funnels[event]))
            for event in EVENT_ORDER
        ),
    }


def relabel_partition_to_pairs(
    partition: Partition,
    event: int,
) -> tuple[tuple[tuple[int, Pair], ...], ...]:
    return tuple(
        tuple((event, BACKBONE[lane]) for lane in block)
        for block in partition
    )


def erase_expected_event_key(
    partition: tuple[tuple[tuple[int, Pair], ...], ...],
) -> tuple[tuple[Pair, ...], ...]:
    return tuple(
        tuple(pair for _event, pair in block)
        for block in partition
    )


def reverse_braid_recomputation(
    forward: dict[str, object],
) -> dict[str, object]:
    macros = forward["macros"]
    funnels = forward["funnels"]
    assert isinstance(macros, tuple)
    assert isinstance(funnels, dict)
    words = compile_scalar_words(macros)
    word_lengths = tuple(
        (pair, len(words[pair])) for pair in BACKBONE
    )
    if {length for _pair, length in word_lengths} != {
        MOVEMENT_GATE_COUNT
    }:
        raise AssertionError("compiled movement word length drifted")

    cohorts: dict[int, dict[str, object]] = {}
    raw_labeled_braids = {}
    all_roundtrips = True
    for event in EVENT_ORDER:
        states = (funnels[event],) * len(BACKBONE)
        depth_states = [states]
        depth_partitions = [hashed_partition(states)]
        roundtrip = True
        for _depth in range(1, WINDOW_DEPTH + 1):
            predecessor = tuple(
                apply_scalar_word(
                    state, words[pair], reverse=True
                )
                for pair, state in zip(BACKBONE, states)
            )
            roundtrip &= all(
                apply_scalar_word(
                    before, words[pair], reverse=False
                ) == after
                for pair, before, after in zip(
                    BACKBONE, predecessor, states
                )
            )
            states = predecessor
            depth_states.append(states)
            depth_partitions.append(hashed_partition(states))

        forward_partitions = tuple(reversed(depth_partitions))
        forward_movements = tuple(
            range(
                FUNNEL_MOMENTS[event] - WINDOW_DEPTH,
                FUNNEL_MOMENTS[event] + 1,
            )
        )
        coarsening_movements = tuple(
            forward_movements[index]
            for index in range(1, len(forward_partitions))
            if forward_partitions[index] != forward_partitions[index - 1]
            and transition_kind(
                forward_partitions[index - 1],
                forward_partitions[index],
            ) == "COARSENING"
        )
        raw_labeled = tuple(
            (
                FUNNEL_MOMENTS[event] - depth,
                relabel_partition_to_pairs(partition, event),
            )
            for depth, partition in enumerate(depth_partitions)
        )
        raw_labeled_braids[event] = raw_labeled
        cohorts[event] = {
            "depth_states": tuple(depth_states),
            "depth_partitions": tuple(depth_partitions),
            "coarsening_movements": coarsening_movements,
            "pre_union_partition": depth_partitions[1],
            "pre_union_varying_wires": varying_wires(depth_states[1]),
            "reverse_forward_roundtrip_exact": roundtrip,
            "exact_depth_partition_sha256":
                object_digest(tuple(enumerate(depth_partitions))),
            "exact_depth_state_sha256": object_digest(tuple(
                tuple(packed_state_sha256(state) for state in row)
                for row in depth_states
            )),
        }
        all_roundtrips &= roundtrip

    reference = cohorts[0]["depth_partitions"]
    normalized_identical = all(
        cohorts[event]["depth_partitions"] == reference
        for event in EVENT_ORDER[1:]
    )
    event0_forward_reverse_exact = all(
        cohorts[0]["depth_states"][depth]
        == forward["event0_tail_states"][
            FUNNEL_MOMENTS[0] - depth
        ]
        and cohorts[0]["depth_partitions"][depth]
        == forward["event0_tail_partitions"][
            FUNNEL_MOMENTS[0] - depth
        ]
        for depth in range(WINDOW_DEPTH + 1)
    )
    expected_rekeyed = {
        event: tuple(
            (
                FUNNEL_MOMENTS[event] - movement,
                erase_expected_event_key(partition),
            )
            for movement, partition in raw_labeled_braids[event]
        )
        for event in EVENT_ORDER
    }
    expected_key_relabeling_exact = all(
        expected_rekeyed[event] == expected_rekeyed[0]
        for event in EVENT_ORDER[1:]
    )
    raw_braids_distinct = len({
        object_digest(raw_labeled_braids[event])
        for event in EVENT_ORDER
    }) == len(EVENT_ORDER)
    preunion_counts = tuple(
        len(cohorts[event]["pre_union_varying_wires"])
        for event in EVENT_ORDER
    )
    return {
        "cohorts": cohorts,
        "raw_labeled_braids": raw_labeled_braids,
        "expected_rekeyed_braids": expected_rekeyed,
        "word_lengths": word_lengths,
        "normalized_partitions_identical": normalized_identical,
        "event0_forward_reverse_exact": event0_forward_reverse_exact,
        "all_reverse_forward_roundtrips_exact": all_roundtrips,
        "raw_braids_pairwise_distinct": raw_braids_distinct,
        "expected_key_and_time_relabeling_exact":
            expected_key_relabeling_exact,
        "preunion_varying_wire_counts": preunion_counts,
    }


def normalize_synthetic_braid(
    raw: dict[int, Partition],
    funnel_movement: int,
) -> tuple[Partition, ...]:
    depths = tuple(
        funnel_movement - movement for movement in raw
    )
    if set(depths) != set(range(len(raw))):
        raise AssertionError("synthetic braid is not a complete depth window")
    return tuple(
        raw[funnel_movement - depth]
        for depth in range(len(raw))
    )


def synthetic_normalization_controls() -> dict[str, object]:
    total = (tuple(range(9)),)
    three_blocks = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    discrete = tuple((lane,) for lane in range(9))
    altered_same_shape = (
        (0, 1, 3), (2, 4, 5), (6, 7, 8),
    )
    base_values = (total, three_blocks, discrete)
    base_raw = {
        100 - depth: partition
        for depth, partition in enumerate(base_values)
    }
    offset_raw = {
        900 - depth: partition
        for depth, partition in enumerate(base_values)
    }
    altered_raw = dict(offset_raw)
    altered_raw[899] = altered_same_shape
    base_normal = normalize_synthetic_braid(base_raw, 100)
    offset_normal = normalize_synthetic_braid(offset_raw, 900)
    altered_normal = normalize_synthetic_braid(altered_raw, 900)
    return {
        "offset_only_braids_normalize_equal":
            base_normal == offset_normal,
        "deliberately_different_same_shape_braid_stays_different":
            base_normal != altered_normal,
        "changed_depth": 1,
        "base_changed_partition": three_blocks,
        "adversarial_changed_partition": altered_same_shape,
        "block_sizes_held_fixed":
            tuple(map(len, three_blocks))
            == tuple(map(len, altered_same_shape)),
        "normalization_is_not_constant":
            len({object_digest(base_normal), object_digest(altered_normal)})
            == 2,
    }


def normalization_ast_evidence(
    primary_source: bytes,
    primary_tree: ast.Module,
) -> dict[str, object]:
    reverse = top_level_function(primary_tree, "reverse_cohort_windows")
    partition = top_level_function(primary_tree, "partition_of")
    reverse_dump = ast.dump(reverse, include_attributes=False)
    partition_dump = ast.dump(partition, include_attributes=False)
    reverse_calls = tuple(sorted({
        node.func.id
        if isinstance(node.func, ast.Name)
        else node.func.attr
        for node in ast.walk(reverse)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }))
    suspicious_value_normalizers = tuple(
        name for name in reverse_calls
        if any(
            token in name.lower()
            for token in ("canonical", "relabel", "permute", "normalize")
        )
    )
    time_subtractions = sum(
        isinstance(node, ast.BinOp)
        and isinstance(node.op, ast.Sub)
        and "FUNNEL_MOMENTS" in ast.dump(
            node.left, include_attributes=False
        )
        and isinstance(node.right, ast.Name)
        and node.right.id == "depth"
        for node in ast.walk(reverse)
    )
    direct_partition_tuple_comparison = any(
        isinstance(node, ast.Compare)
        and any(isinstance(operator, ast.Eq) for operator in node.ops)
        and "depth_partitions" in ast.dump(
            node, include_attributes=False
        )
        and "internal" in ast.dump(node, include_attributes=False)
        for node in ast.walk(reverse)
    )
    state_keyed_grouping = (
        "attr='setdefault'" in partition_dump
        and "Name(id='state'" in partition_dump
        and "Name(id='lane'" in partition_dump
        and "attr='append'" in partition_dump
    )
    reverse_source = ast.get_source_segment(
        primary_source.decode("utf-8"), reverse
    )
    partition_source = ast.get_source_segment(
        primary_source.decode("utf-8"), partition
    )
    return {
        "primary_definition":
            "fixed BACKBONE lane order identifies (event,pair) by pair; "
            "absolute movement m is re-keyed to depth d=h_e-m; exact "
            "partition tuples are then compared without value remapping",
        "quotients_trajectory_event_key": True,
        "trajectory_pair_labels_preserved": True,
        "aligns_absolute_time_to_funnel_depth": True,
        "partition_value_normalizer": "NONE",
        "partition_representation":
            "blocks are ordered by first fixed lane only; membership is "
            "preserved and equality is exact",
        "time_subtraction_nodes": time_subtractions,
        "direct_partition_tuple_comparison":
            direct_partition_tuple_comparison,
        "state_keyed_exact_grouping": state_keyed_grouping,
        "reverse_window_calls": reverse_calls,
        "suspicious_value_normalizer_calls":
            suspicious_value_normalizers,
        "reverse_function_ast_sha256":
            sha256(reverse_dump.encode("utf-8")).hexdigest(),
        "partition_function_ast_sha256":
            sha256(partition_dump.encode("utf-8")).hexdigest(),
        "reverse_function_text_sha256":
            sha256(reverse_source.encode("utf-8")).hexdigest()
            if reverse_source is not None else None,
        "partition_function_text_sha256":
            sha256(partition_source.encode("utf-8")).hexdigest()
            if partition_source is not None else None,
        "pass": (
            time_subtractions >= 2
            and direct_partition_tuple_comparison
            and state_keyed_grouping
            and not suspicious_value_normalizers
        ),
    }


def source_controls(
    payloads: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    source_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    source_blobs = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    primary = trees[PRIMARY_PATH]
    register = trees[REGISTER_PATH]
    fixture = trees[FIXTURE_PATH]
    literal_cross_checks = {
        "primary_BACKBONE":
            literal_assignment(primary, "BACKBONE") == BACKBONE,
        "primary_EVENT_ORDER":
            literal_assignment(primary, "EVENT_ORDER") == EVENT_ORDER,
        "primary_FUNNEL_MOMENTS":
            literal_assignment(primary, "FUNNEL_MOMENTS")
            == FUNNEL_MOMENTS,
        "primary_REGISTER_WIRES":
            literal_assignment(primary, "REGISTER_WIRES")
            == REGISTER_WIRES,
        "primary_CROSS_COHORT_WINDOW_MOVEMENTS":
            literal_assignment(
                primary, "CROSS_COHORT_WINDOW_MOVEMENTS"
            ) == WINDOW_DEPTH,
        "register_BACKBONE":
            literal_assignment(register, "BACKBONE") == BACKBONE,
        "register_FUNNEL_MOMENTS":
            literal_assignment(register, "FUNNEL_MOMENTS")
            == FUNNEL_MOMENTS,
        "fixture_literals_present": all(
            isinstance(literal_assignment(fixture, name), str)
            for name in (
                "GATE_CONSTANTS_B85",
                "FAMILY_STATES_B85",
                "SSTAR_PACKED_B85",
            )
        ),
    }
    ast_basis = {
        "primary": all(
            any(
                isinstance(node, ast.FunctionDef) and node.name == name
                for node in primary.body
            )
            for name in (
                "partition_of",
                "reverse_cohort_windows",
                "cross_reference_partition_events",
            )
        ),
        "fixture": any(
            isinstance(node, ast.FunctionDef)
            and node.name == "decode_fixtures"
            for node in fixture.body
        ),
        "register": all(
            any(
                isinstance(node, ast.FunctionDef) and node.name == name
                for node in register.body
            )
            for name in (
                "track_register_trajectories",
                "change_time_encoding",
            )
        ),
    }
    path_rows = tuple(
        {
            "path": path,
            "exists": (ROOT / path).is_file(),
            "worktree_relative": not Path(path).is_absolute(),
        }
        for path in AUDIT_INPUT_PATHS
    )
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    imports = direct_import_roots(self_tree)
    stdlib_only = set(imports) <= (
        set(sys.stdlib_module_names) | {"__future__"}
    )
    exact = (
        literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
        == AUDIT_INPUT_PATHS
        and all(
            row["exists"] and row["worktree_relative"]
            for row in path_rows
        )
        and source_sha == EXPECTED_SOURCE_SHA256
        and source_blobs == EXPECTED_SOURCE_GIT_BLOBS
        and all(literal_cross_checks.values())
        and all(ast_basis.values())
        and stdlib_only
        and not blocked_loaded
        and not FIREWALL.hits
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — Controls source intake is SHA-pinned, literal-path, "
            "worktree-relative, text/AST-only, and BLOCKLIST-clean."
            if exact else
            "FAIL — Controls source intake, provenance, or BLOCKLIST failed."
        ),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "input_path_rows": path_rows,
        "unique_source_files_read": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "source_sha256": source_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "source_git_blobs": source_blobs,
        "expected_source_git_blobs": EXPECTED_SOURCE_GIT_BLOBS,
        "literal_cross_checks": literal_cross_checks,
        "AST_basis": ast_basis,
        "direct_import_roots": imports,
        "stdlib_only": stdlib_only,
        "BLOCKLIST": {
            "modules": BLOCKLISTED_MODULES,
            "policy": "TEXT_AST_ONLY; NEVER IMPORT OR EXECUTE",
            "loaded": blocked_loaded,
            "firewall_hits": tuple(FIREWALL.hits),
        },
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": git_text("branch", "--show-current"),
        "pass": exact,
    }


def normalization_certificate(
    ast_evidence: dict[str, object],
    braid: dict[str, object],
) -> dict[str, object]:
    synthetic = synthetic_normalization_controls()
    synthetic_pass = all(
        value for key, value in synthetic.items()
        if key in {
            "offset_only_braids_normalize_equal",
            "deliberately_different_same_shape_braid_stays_different",
            "block_sizes_held_fixed",
            "normalization_is_not_constant",
        }
    )
    exact = (
        ast_evidence["pass"]
        and synthetic_pass
        and braid["raw_braids_pairwise_distinct"]
        and braid["expected_key_and_time_relabeling_exact"]
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — THE NORMALIZATION AUDIT: normalization removes only "
            "the cohort event tag and absolute funnel offset; it preserves "
            "pair/lane partition membership, a deliberately different "
            "same-shape braid remains different, and the raw cohorts agree "
            "exactly after only the declared key/time relabeling. The "
            "partition identity is not normalized into existence."
            if exact else
            "FAIL — THE NORMALIZATION AUDIT: the declared normalization "
            "can collapse distinguishing partition content or the raw "
            "cohorts require more than the declared key/time relabeling."
        ),
        "ruling": (
            "REAL_PARTITION_IDENTITY_NOT_MANUFACTURED"
            if exact else "PRIMARY_REFUTED_NORMALIZATION_MANUFACTURES_IDENTITY"
        ),
        "primary_AST_definition": ast_evidence,
        "synthetic_adversarial_control": synthetic,
        "raw_braid_audit": {
            "raw_braids_pairwise_distinct":
                braid["raw_braids_pairwise_distinct"],
            "difference_expected":
                "absolute movement keys and cohort event component of "
                "trajectory keys only",
            "expected_key_and_time_relabeling_exact":
                braid["expected_key_and_time_relabeling_exact"],
            "raw_labeled_braid_sha256": tuple(
                (
                    event,
                    object_digest(braid["raw_labeled_braids"][event]),
                )
                for event in EVENT_ORDER
            ),
            "rekeyed_braid_sha256": tuple(
                (
                    event,
                    object_digest(braid["expected_rekeyed_braids"][event]),
                )
                for event in EVENT_ORDER
            ),
        },
        "scope_warning":
            "The equality is partition-valued, not state-valued; partition "
            "extraction intentionally forgets the unequal wire content of "
            "distinct blocks.",
        "pass": exact,
    }


def braid_recomputation_certificate(
    fixture: dict[str, object],
    forward: dict[str, object],
    braid: dict[str, object],
) -> dict[str, object]:
    cohorts = braid["cohorts"]
    exact = (
        fixture["pass"]
        and braid["normalized_partitions_identical"]
        and braid["event0_forward_reverse_exact"]
        and braid["all_reverse_forward_roundtrips_exact"]
        and forward["event0_all_reach_target"]
        and forward["witness_event0_matches_backbone"]
        and len(forward["event0_partitions"])
        == FUNNEL_MOMENTS[0] + 1
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — THE BRAID RECOMPUTATION: an independent packed-state "
            "SHA-256 equality partition and independent Boolean replay give "
            "identical event-0/2/1 partition sequences at every depth 0..64."
            if exact else
            "FAIL — THE BRAID RECOMPUTATION: independent replay does not "
            "recover the claimed exact depth-0..64 partition identity."
        ),
        "state_hash_definition":
            "SHA-256 of each 5815-bit state packed into 728 little-endian "
            "bytes, with packed bytes retained in the equality key",
        "partition_definition":
            "group fixed lane labels by (packed SHA-256, exact packed bytes); "
            "sort blocks by their first fixed lane",
        "depth_bounds": (0, WINDOW_DEPTH),
        "event_order": EVENT_ORDER,
        "cohort_depth_partition_sha256": tuple(
            (
                event,
                cohorts[event]["exact_depth_partition_sha256"],
            )
            for event in EVENT_ORDER
        ),
        "cohort_depth_state_sha256": tuple(
            (
                event,
                cohorts[event]["exact_depth_state_sha256"],
            )
            for event in EVENT_ORDER
        ),
        "funnel_packed_state_sha256":
            forward["funnel_packed_sha256"],
        "normalized_partitions_identical":
            braid["normalized_partitions_identical"],
        "event0_forward_reverse_full_state_exact":
            braid["event0_forward_reverse_exact"],
        "reverse_forward_roundtrips_exact":
            braid["all_reverse_forward_roundtrips_exact"],
        "event0_sample_count": len(forward["event0_partitions"]),
        "compiled_word_lengths": braid["word_lengths"],
        "pass": exact,
    }


def falsifications_certificate(
    forward: dict[str, object],
    braid: dict[str, object],
) -> dict[str, object]:
    per_event = []
    total_coarsenings = 0
    same_tick = 0
    for event in EVENT_ORDER:
        movements = (
            forward["event0_coarsening_movements"]
            if event == 0
            else braid["cohorts"][event]["coarsening_movements"]
        )
        register_union = set().union(
            *forward["register_change_sets"][event]
        )
        matched = sum(
            movement in register_union for movement in movements
        )
        per_event.append((event, len(movements), matched))
        total_coarsenings += len(movements)
        same_tick += matched
    preunion_counts = braid["preunion_varying_wire_counts"]
    preunion_partitions = tuple(
        braid["cohorts"][event]["pre_union_partition"]
        for event in EVENT_ORDER
    )
    common_three_node_partition = (
        len(set(preunion_partitions)) == 1
        and len(preunion_partitions[0]) == 3
    )
    preunion_law_falsified = (
        preunion_counts == EXPECTED_PREUNION_WIRE_COUNTS
        and preunion_counts != (15, 15, 15)
    )
    same_tick_law_falsified = (
        same_tick == EXPECTED_SAME_TICK_COARSENINGS
        and total_coarsenings == EXPECTED_TOTAL_COARSENINGS
        and same_tick < total_coarsenings
    )
    exact = (
        common_three_node_partition
        and preunion_law_falsified
        and same_tick_law_falsified
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — THE FALSIFICATIONS: the proposed common 15-wire "
            "pre-union law is false with event-order 0/2/1 counts 15/3/9; "
            "the same-tick register law is false with 1321 of 2773 "
            "coarsenings matched."
            if exact else
            "FAIL — THE FALSIFICATIONS: one or both independently "
            "recomputed falsification counts do not match 15/3/9 and "
            "1321/2773."
        ),
        "pre_union_15_wire_law": {
            "common_partition": preunion_partitions[0],
            "common_partition_block_sizes":
                tuple(map(len, preunion_partitions[0])),
            "common_three_node_partition": common_three_node_partition,
            "varying_wire_counts_event_0_2_1": preunion_counts,
            "varying_wire_indices": tuple(
                (
                    event,
                    braid["cohorts"][event][
                        "pre_union_varying_wires"
                    ],
                )
                for event in EVENT_ORDER
            ),
            "claimed_uniform_15_wire_law_holds": False,
            "falsified_exactly": preunion_law_falsified,
        },
        "same_tick_register_law": {
            "per_event_event_total_same_tick": tuple(per_event),
            "same_tick_coarsenings": same_tick,
            "total_coarsenings": total_coarsenings,
            "mismatched_coarsenings": total_coarsenings - same_tick,
            "law_holds": False,
            "falsified_exactly": same_tick_law_falsified,
        },
        "pass": exact,
    }


def controls_certificate(
    source: dict[str, object],
    fixture: dict[str, object],
    replay: dict[str, object],
    forward: dict[str, object],
    braid: dict[str, object],
    elapsed: float,
) -> dict[str, object]:
    fixture_first = fixture_digest(fixture)
    fixture_replay = fixture_digest(replay)
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    determinism = {
        "fixture_decode_replay_exact":
            fixture_first == fixture_replay
            and fixture["macro_lengths"] == replay["macro_lengths"],
        "meet_duplicate_exact": forward["meet_duplicate_exact"],
        "event0_duplicate_exact_every_sample":
            forward["event0_duplicate_exact_every_sample"],
        "register_duplicate_exact_every_movement":
            forward["register_duplicate_exact_every_movement"],
        "funnel_duplicate_exact": forward["funnel_duplicate_exact"],
        "event0_forward_reverse_full_state_exact":
            braid["event0_forward_reverse_exact"],
        "all_reverse_forward_roundtrips_exact":
            braid["all_reverse_forward_roundtrips_exact"],
    }
    base_pass = (
        source["pass"]
        and fixture["pass"]
        and replay["pass"]
        and all(determinism.values())
        and not blocked_loaded
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    return {
        "status": "PASS" if base_pass else "FAIL",
        "finding": (
            "PASS — Controls: source SHAs and literal worktree paths are "
            "exact; Cycle-845/830/835 stayed BLOCKLISTED and text/AST-only; "
            "duplicate replay is deterministic; runtime and stdout are "
            "bounded."
            if base_pass else
            "FAIL — Controls: provenance, BLOCKLIST, determinism, runtime, "
            "or stdout accounting failed."
        ),
        "source_controls": source,
        "fixture_determinism": {
            "first_digest": fixture_first,
            "replay_digest": fixture_replay,
            "exact": fixture_first == fixture_replay,
        },
        "determinism": determinism,
        "BLOCKLIST": {
            "modules": BLOCKLISTED_MODULES,
            "policy": "TEXT_AST_ONLY; NEVER IMPORT OR EXECUTE",
            "loaded_at_end": blocked_loaded,
            "firewall_hits_at_end": tuple(FIREWALL.hits),
        },
        "schedule_rows": {
            "combined_event0_and_witness":
                forward["combined_schedule_rows"],
            "witness_only": forward["witness_schedule_rows"],
        },
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "observed_runtime_seconds": round(elapsed, 6),
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "observed_stdout_bytes": 0,
        "stdout_below_limit": False,
        "base_pass_before_stdout_check": base_pass,
        "pass": False,
    }


def stable_render(report: dict[str, object]) -> str:
    certificates = report["certificates"]
    controls = certificates["Controls"]
    prior_size = -1
    for _attempt in range(12):
        lines = [
            f"NORMALIZATION_RULING={report['normalization_ruling']}",
            "CERTIFICATE_THE_NORMALIZATION_AUDIT="
            + compact(certificates["THE NORMALIZATION AUDIT"]),
            "CERTIFICATE_THE_BRAID_RECOMPUTATION="
            + compact(certificates["THE BRAID RECOMPUTATION"]),
            "CERTIFICATE_THE_FALSIFICATIONS="
            + compact(certificates["THE FALSIFICATIONS"]),
            "CERTIFICATE_CONTROLS=" + compact(controls),
            "REPORT=" + compact({
                key: value for key, value in report.items()
                if key != "certificates"
            }),
        ]
        rendered = "\n".join(lines) + "\n"
        size = len(rendered.encode("utf-8"))
        controls["observed_stdout_bytes"] = size
        controls["stdout_below_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = (
            controls["base_pass_before_stdout_check"]
            and controls["stdout_below_limit"]
        )
        controls["status"] = "PASS" if controls["pass"] else "FAIL"
        report["overall_pass"] = all(
            certificate["pass"]
            for certificate in certificates.values()
        )
        report["terminal"] = (
            "CYCLE845_PARTITION_INDEPENDENT_CHECK_PASS"
            if report["overall_pass"] else
            "CYCLE845_PARTITION_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        if size == prior_size:
            return rendered
        prior_size = size
    raise AssertionError("stdout accounting did not stabilize")


def scientific_disposition(
    normalization: dict[str, object],
    braid: dict[str, object],
    falsifications: dict[str, object],
) -> str:
    if not normalization["pass"]:
        return "PRIMARY_REFUTED_NORMALIZATION_MANUFACTURES_IDENTITY"
    if not braid["pass"]:
        return "PRIMARY_REFUTED_BRAID_RECOMPUTATION_MISMATCH"
    if not falsifications["pass"]:
        return "PRIMARY_REFUTED_FALSIFICATION_COUNT_MISMATCH"
    return (
        "PRIMARY_NOT_REFUTED_REAL_PARTITION_IDENTITY_WITH_"
        "STATE_CONTENT_SCOPE_BOUNDARY"
    )


def run() -> int:
    started = monotonic()
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    source = source_controls(payloads, trees)
    fixture = decode_fixture(trees[FIXTURE_PATH])
    fixture_replay = decode_fixture(trees[FIXTURE_PATH])
    forward = run_forward_recomputation(fixture)
    braid_data = reverse_braid_recomputation(forward)
    ast_evidence = normalization_ast_evidence(
        payloads[PRIMARY_PATH], trees[PRIMARY_PATH]
    )
    normalization = normalization_certificate(
        ast_evidence, braid_data
    )
    braid = braid_recomputation_certificate(
        fixture, forward, braid_data
    )
    falsifications = falsifications_certificate(
        forward, braid_data
    )
    elapsed = monotonic() - started
    controls = controls_certificate(
        source,
        fixture,
        fixture_replay,
        forward,
        braid_data,
        elapsed,
    )
    certificates = {
        "THE NORMALIZATION AUDIT": normalization,
        "THE BRAID RECOMPUTATION": braid,
        "THE FALSIFICATIONS": falsifications,
        "Controls": controls,
    }
    report = {
        "cycle": 845,
        "checker":
            "INDEPENDENT ADVERSARIAL CHECKER — is the braid identity real "
            "or normalized into existence?",
        "normalization_ruling": normalization["ruling"],
        "scientific_disposition": scientific_disposition(
            normalization, braid, falsifications
        ),
        "primary_refuted": not (
            normalization["pass"]
            and braid["pass"]
            and falsifications["pass"]
        ),
        "certificates": certificates,
        "runtime_seconds_before_render": round(elapsed, 6),
        "overall_pass": False,
        "terminal":
            "CYCLE845_PARTITION_INDEPENDENT_CHECK_HONEST_FAIL",
    }
    rendered = stable_render(report)
    if len(rendered.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(rendered)
    return 0 if report["overall_pass"] else 1


def main() -> int:
    started = monotonic()
    try:
        code = run()
    except Exception as error:
        print(compact({
            "cycle": 845,
            "error_type": type(error).__name__,
            "error": str(error),
            "pass": False,
            "terminal":
                "CYCLE845_PARTITION_INDEPENDENT_CHECK_HONEST_FAIL",
        }))
        return 1
    if monotonic() - started >= AUDIT_TIMEOUT_SEC:
        print(compact({
            "cycle": 845,
            "error": "runtime limit exceeded after render",
            "pass": False,
            "terminal":
                "CYCLE845_PARTITION_INDEPENDENT_CHECK_HONEST_FAIL",
        }))
        return 1
    return code


if __name__ == "__main__":
    raise SystemExit(main())
