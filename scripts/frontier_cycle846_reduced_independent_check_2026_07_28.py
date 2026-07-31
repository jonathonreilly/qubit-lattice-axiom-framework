#!/usr/bin/env python3
"""Cycle 846 independent adversarial checker: the reduced structure.

The source primaries are SHA-pinned, import-blocklisted, and read only as
text/AST.  This checker independently decodes the Cycle-830 literal fixture
bank and replays the Boolean X/CNOT/Toffoli circuit with integer bit slices.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle846_reduced_braids_delay_law_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle841_deciding_the_tick_2026_07_28.py",
)

import ast
import base64
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import lcm
from pathlib import Path
import struct
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, FIXTURE_PATH, CLOCK_PATH = AUDIT_INPUT_PATHS
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
MEET_CONTROLLER_TICK = 3
NORMALIZED_DEPTH = 64
EVENT_ORDER = (0, 2, 1)
CHRONOLOGICAL_ORDER = (1, 2, 0)
PAIR_POSITIONS = ((0, 5), (0, 6))
PAIR_FUNNEL_MOVEMENTS = {1: 193205, 2: 246664, 0: 1142427}
PAIR_MOMENTS = {event: movement + 5 for event, movement in PAIR_FUNNEL_MOVEMENTS.items()}
NINE_FUNNEL_MOVEMENT = 14739
NINE_RESIDUAL_TARGET = (595, 64)
LCM_SKELETON = lcm(4464, 5952)
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
REGISTER_WIRES = (
    1, 6, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 71, 75, 76, 77, 78, 79, 80, 82, 83,
    84, 86, 87, 89, 105, 109, 110, 111, 112, 113, 114, 116,
    117,
)
THREE_WIRES = (88, 124, 125)
EXPECTED_PAIR_BRAID_SHA256 = "dc7156746a46cbe6edfaceb4ccfb9b27fc7250d2608a991848cfec6f62f39932"
EXPECTED_NINE_PARTITION_SHA256 = "726b74aefc7afa6e1790c7dc73a59eacdadeec72246e19ac01104be09d49829d"
EXPECTED_MATCHING_SUBSETS = (
    ((2, 7), (2, 8)),
    ((3, 8), (3, 9)),
    ((3, 8), (4, 9)),
    ((3, 9), (4, 9)),
    ((4, 10), (5, 10)),
)

EXPECTED_SHA256 = {
    PRIMARY_PATH: "172313524341e958d36e1028f0cec5e64e81c4efd915c009073049998c37fc45",
    FIXTURE_PATH: "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    CLOCK_PATH: "9879f900590b2a9cdded11d2b691d48adf5c5baff96af4f88b7483bfc98a0b54",
}
EXPECTED_GIT_BLOBS = {
    PRIMARY_PATH: "2e0eb1848b92ab3f43a5ada64664ab45b58f5bb1",
    FIXTURE_PATH: "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    CLOCK_PATH: "379bbe1f4d7ae3432488359fbf3009adfe2a5984",
}
EXPECTED_GATE_RAW_SHA256 = "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
EXPECTED_FAMILY_RAW_SHA256 = "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
EXPECTED_TARGET_RAW_SHA256 = "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"

Pair = tuple[int, int]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _ImportFirewall(importlib.abc.MetaPathFinder):
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


FIREWALL = _ImportFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def object_digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(f"expected one function {name}, got {len(matches)}")
    return matches[0]


def loaded_names(node: ast.AST) -> set[str]:
    return {
        item.id for item in ast.walk(node)
        if isinstance(item, ast.Name) and isinstance(item.ctx, ast.Load)
    }


def read_source_packet() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {path: ast.parse(payload, filename=path) for path, payload in payloads.items()}
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    imports: set[str] = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    primary_tree = trees[PRIMARY_PATH]
    clock_tree = trees[CLOCK_PATH]
    source_contract = {
        "primary_pair_positions": literal_assignment(primary_tree, "PAIR_POSITIONS") == PAIR_POSITIONS,
        "primary_backbone": literal_assignment(primary_tree, "BACKBONE") == BACKBONE,
        "primary_pair_moments": literal_assignment(primary_tree, "PAIR_MOMENTS") == PAIR_MOMENTS,
        "primary_register_wires": literal_assignment(primary_tree, "REGISTER_WIRES") == REGISTER_WIRES,
        "cycle841_residual_target": literal_assignment(clock_tree, "COHORT_RESIDUALS") == NINE_RESIDUAL_TARGET,
        "cycle841_has_raw_catchup": isinstance(function_node(clock_tree, "raw_catchup"), ast.FunctionDef),
        "cycle841_has_accounting_consequence": isinstance(
            function_node(clock_tree, "accounting_consequence"), ast.FunctionDef
        ),
    }
    shas = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    controls = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "files_read": len(AUDIT_INPUT_PATHS),
        "file_read_limit": 7,
        "source_access_mode": {path: "TEXT_AST_ONLY_BLOCKLISTED" for path in AUDIT_INPUT_PATHS},
        "source_sha256": shas,
        "expected_source_sha256": EXPECTED_SHA256,
        "source_git_blobs": blobs,
        "expected_source_git_blobs": EXPECTED_GIT_BLOBS,
        "source_contract": source_contract,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_loaded_at_start": blocked_loaded,
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= (set(sys.stdlib_module_names) | {"__future__"}),
        "self_sha256": sha256(self_payload).hexdigest(),
    }
    controls["pass"] = all((
        controls["AUDIT_INPUT_PATHS_literal"],
        controls["existing_worktree_relative"],
        len(AUDIT_INPUT_PATHS) <= 7,
        shas == EXPECTED_SHA256,
        blobs == EXPECTED_GIT_BLOBS,
        all(source_contract.values()),
        not blocked_loaded,
        not FIREWALL.hits,
        controls["stdlib_only"],
    ))
    return {"payloads": payloads, "trees": trees, "self_tree": self_tree, "controls": controls}


def lawful_pairs() -> tuple[Pair, ...]:
    def separation(pair: Pair) -> int:
        return min((pair[1] - pair[0]) % RING_STATIONS, (pair[0] - pair[1]) % RING_STATIONS)

    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if separation(pair) > 1
    )


def decode_fixtures(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(
        literal_assignment(tree, name)
        for name in ("GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85")
    )
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("Cycle-830 fixture literals are missing")
    gate_raw, family_raw, target_raw = (
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    cursor = 22
    macros: list[tuple[Gate, ...]] = []
    for length in lengths:
        macro: list[Gate] = []
        for _ in range(length):
            macro.append(struct.unpack("<BHHH", gate_raw[cursor:cursor + 7]))
            cursor += 7
        macros.append(tuple(macro))
    keys = tuple(sorted((event, pair) for event in range(4) for pair in lawful_pairs()))
    states = {
        key: int.from_bytes(
            family_raw[index * STATE_BYTES:(index + 1) * STATE_BYTES], "little"
        )
        for index, key in enumerate(keys)
    }
    target = int.from_bytes(target_raw, "little")
    fixture_checks = {
        "eleven_macros": len(macros) == RING_STATIONS,
        "gate_count": sum(lengths) == GATE_COUNT,
        "gate_payload_consumed": cursor == len(gate_raw),
        "family_size": len(states) == FAMILY_SIZE,
        "family_payload_size": len(family_raw) == FAMILY_SIZE * STATE_BYTES,
        "target_payload_size": len(target_raw) == STATE_BYTES,
        "gate_raw_sha256": sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256,
        "family_raw_sha256": sha256(family_raw).hexdigest() == EXPECTED_FAMILY_RAW_SHA256,
        "target_raw_sha256": sha256(target_raw).hexdigest() == EXPECTED_TARGET_RAW_SHA256,
    }
    return {
        "macros": tuple(macros),
        "keys": keys,
        "states": states,
        "target": target,
        "raw_digests": (
            sha256(gate_raw).hexdigest(),
            sha256(family_raw).hexdigest(),
            sha256(target_raw).hexdigest(),
        ),
        "checks": fixture_checks,
        "pass": all(fixture_checks.values()),
    }


def fixture_digest(fixtures: dict[str, object]) -> str:
    hasher = sha256()
    for macro in fixtures["macros"]:
        hasher.update(len(macro).to_bytes(2, "little"))
        for gate in macro:
            hasher.update(struct.pack("<BHHH", *gate))
    for key in fixtures["keys"]:
        hasher.update(compact(key).encode("utf-8"))
        hasher.update(fixtures["states"][key].to_bytes(STATE_BYTES, "little"))
    hasher.update(fixtures["target"].to_bytes(STATE_BYTES, "little"))
    return hasher.hexdigest()


def transpose_states(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        pending = state
        while pending:
            bit = pending & -pending
            columns[bit.bit_length() - 1] |= 1 << lane
            pending ^= bit
    return columns


def capture_state(columns: list[int], lane: int) -> int:
    return sum(
        1 << wire for wire, column in enumerate(columns)
        if (column >> lane) & 1
    )


def capture_states(columns: list[int], count: int) -> tuple[int, ...]:
    states = [0] * count
    live_mask = (1 << count) - 1
    for wire, column in enumerate(columns):
        live = column & live_mask
        while live:
            bit = live & -live
            states[bit.bit_length() - 1] |= 1 << wire
            live ^= bit
    return tuple(states)


def compile_phases(
    macros: tuple[tuple[Gate, ...], ...],
    lane_pairs: tuple[Pair, ...],
) -> tuple[tuple[MaskedGate, ...], ...]:
    phases: list[tuple[MaskedGate, ...]] = []
    for phase in range(RING_STATIONS):
        rows: list[MaskedGate] = []
        for station, macro in enumerate(macros):
            mask = sum(
                1 << lane
                for lane, pair in enumerate(lane_pairs)
                if station in (
                    (pair[0] + phase) % RING_STATIONS,
                    (pair[1] + phase) % RING_STATIONS,
                )
            )
            if mask:
                rows.extend((*gate, mask) for gate in macro)
        phases.append(tuple(rows))
    return tuple(phases)


def apply_schedule(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        elif kind == 2:
            columns[third] ^= columns[first] & columns[second] & mask
        else:
            raise AssertionError(f"unknown gate kind {kind}")


def pair_difference_lookup(pair_count: int) -> tuple[int, ...]:
    lane_bits = pair_count * 2
    return tuple(
        sum(
            (((value >> (2 * index)) ^ (value >> (2 * index + 1))) & 1) << index
            for index in range(pair_count)
        )
        for value in range(1 << lane_bits)
    )


def pair_difference_mask(
    columns: list[int], lookup: tuple[int, ...], pair_count: int
) -> int:
    different = 0
    lane_mask = (1 << (2 * pair_count)) - 1
    complete = (1 << pair_count) - 1
    for column in columns:
        different |= lookup[column & lane_mask]
        if different == complete:
            break
    return different


def replay_pair_braids(
    fixtures: dict[str, object],
    horizons: dict[int, int],
) -> dict[str, object]:
    events = tuple(event for event in CHRONOLOGICAL_ORDER if event in horizons)
    keys = tuple((event, pair) for event in events for pair in PAIR_POSITIONS)
    base_states = tuple(fixtures["states"][key] for key in keys)
    base_pairs = tuple(key[1] for key in keys)
    states = base_states + base_states
    lane_pairs = base_pairs + base_pairs
    phases = compile_phases(fixtures["macros"], lane_pairs)
    movement = tuple(row for phase in phases for row in phase)
    columns = transpose_states(states)
    meet_columns = columns.copy()
    for phase in phases[:MEET_CONTROLLER_TICK]:
        apply_schedule(meet_columns, phase)
    lookup = pair_difference_lookup(len(events))
    meet_different = pair_difference_mask(meet_columns, lookup, len(events))
    current = {
        event: not bool(meet_different & (1 << index))
        for index, event in enumerate(events)
    }
    shapes = {event: [current[event]] for event in events}
    tails: dict[int, bytearray] = {event: bytearray() for event in events}
    funnel_states: dict[int, int] = {}
    duplicate_at_funnel: dict[int, bool] = {}
    maximum = max(horizons.values())
    for step in range(1, maximum + 1):
        apply_schedule(columns, movement)
        different = pair_difference_mask(columns, lookup, len(events))
        for index, event in enumerate(events):
            horizon = horizons[event]
            if step > horizon:
                continue
            united = not bool(different & (1 << index))
            if united != current[event]:
                shapes[event].append(united)
                current[event] = united
            if step >= horizon - NORMALIZED_DEPTH:
                tails[event].append(int(united))
            if step == horizon:
                left_lane = 2 * index
                right_lane = left_lane + 1
                left = capture_state(columns, left_lane)
                right = capture_state(columns, right_lane)
                duplicate_offset = len(keys)
                funnel_states[event] = left
                duplicate_at_funnel[event] = all((
                    left == right,
                    left == capture_state(columns, left_lane + duplicate_offset),
                    right == capture_state(columns, right_lane + duplicate_offset),
                ))
    normalized = {event: bytes(reversed(tails[event])) for event in events}
    duplicate_end = all(
        capture_state(columns, lane) == capture_state(columns, lane + len(keys))
        for lane in range(len(keys))
    )
    return {
        "events": events,
        "normalized": normalized,
        "normalized_sha256": {event: sha256(normalized[event]).hexdigest() for event in events},
        "rle_shapes": {event: tuple("UNITED" if value else "SEPARATE" for value in shapes[event]) for event in events},
        "meet_status": {event: "UNITED" if not bool(meet_different & (1 << index)) else "SEPARATE" for index, event in enumerate(events)},
        "funnel_states": funnel_states,
        "funnel_weights": {event: state.bit_count() for event, state in funnel_states.items()},
        "tail_lengths_exact": all(len(tails[event]) == NORMALIZED_DEPTH + 1 for event in events),
        "duplicate_initial": states[:len(keys)] == states[len(keys):],
        "duplicate_schedule_masks": all(
            ((mask >> lane) & 1) == ((mask >> (lane + len(keys))) & 1)
            for _kind, _first, _second, _third, mask in movement
            for lane in range(len(keys))
        ),
        "duplicate_at_funnel": duplicate_at_funnel,
        "duplicate_end": duplicate_end,
        "movement_schedule_rows": len(movement),
    }


def partition(states: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    groups: dict[int, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(sorted((tuple(group) for group in groups.values()), key=lambda row: row[0]))


def replay_nine_tail(fixtures: dict[str, object]) -> dict[str, object]:
    initial = tuple(fixtures["states"][(0, pair)] for pair in BACKBONE)
    states = initial + initial
    phases = compile_phases(fixtures["macros"], BACKBONE + BACKBONE)
    movement = tuple(row for phase in phases for row in phase)
    columns = transpose_states(states)
    captured: list[tuple[int, ...]] = []
    duplicates_exact = True
    for step in range(1, NINE_FUNNEL_MOVEMENT + 1):
        apply_schedule(columns, movement)
        if step >= NINE_FUNNEL_MOVEMENT - NORMALIZED_DEPTH:
            row = capture_states(columns, 2 * len(BACKBONE))
            captured.append(row[:len(BACKBONE)])
            duplicates_exact &= row[:len(BACKBONE)] == row[len(BACKBONE):]
    normalized_states = tuple(reversed(captured))
    return {
        "normalized_states": normalized_states,
        "normalized_partitions": tuple(partition(row) for row in normalized_states),
        "normalized_partition_sha256": object_digest(tuple(partition(row) for row in normalized_states)),
        "terminal_weights": tuple(state.bit_count() for state in normalized_states[0]),
        "terminal_all_equal": len(set(normalized_states[0])) == 1,
        "terminal_matches_fixture_target": all(state == fixtures["target"] for state in normalized_states[0]),
        "tail_length_exact": len(normalized_states) == NORMALIZED_DEPTH + 1,
        "duplicate_initial": states[:len(BACKBONE)] == states[len(BACKBONE):],
        "duplicate_tail_exact": duplicates_exact,
        "duplicate_end": all(
            capture_state(columns, lane) == capture_state(columns, lane + len(BACKBONE))
            for lane in range(len(BACKBONE))
        ),
        "movement_schedule_rows": len(movement),
    }


def certificate_reduced_braids(
    pair_data: dict[str, object],
    nine_data: dict[str, object],
) -> dict[str, object]:
    normalized = pair_data["normalized"]
    common = normalized[CHRONOLOGICAL_ORDER[0]]
    identity = all(normalized[event] == common for event in CHRONOLOGICAL_ORDER)
    rows = []
    for left, right in combinations(range(len(BACKBONE)), 2):
        sequence = bytes(
            states[left] == states[right]
            for states in nine_data["normalized_states"]
        )
        rows.append({
            "lane_subset": (left, right),
            "key_subset": (BACKBONE[left], BACKBONE[right]),
            "sequence_sha256": sha256(sequence).hexdigest(),
            "reproduces_pair_braid": sequence == common,
            "status": "PASS" if sequence == common else "FAIL",
        })
    matches = tuple(row["key_subset"] for row in rows if row["reproduces_pair_braid"])
    failures = tuple(row["key_subset"] for row in rows if not row["reproduces_pair_braid"])
    expected_failures = tuple(
        (BACKBONE[left], BACKBONE[right])
        for left, right in combinations(range(len(BACKBONE)), 2)
        if (BACKBONE[left], BACKBONE[right]) not in EXPECTED_MATCHING_SUBSETS
    )
    pair_sha_rows = tuple(
        (event, sha256(normalized[event]).hexdigest())
        for event in CHRONOLOGICAL_ORDER
    )
    checks = {
        "three_normalized_pair_braids_identical": identity,
        "pair_braid_exact_digest": all(
            digest == EXPECTED_PAIR_BRAID_SHA256 for _event, digest in pair_sha_rows
        ),
        "pair_tail_lengths_65": pair_data["tail_lengths_exact"],
        "pair_funnels_are_united": all(pair_data["duplicate_at_funnel"].values()),
        "pair_rle_topologies_identical": len({
            pair_data["rle_shapes"][event] for event in CHRONOLOGICAL_ORDER
        }) == 1,
        "nine_tail_length_65": nine_data["tail_length_exact"],
        "nine_terminal_all_equal": nine_data["terminal_all_equal"],
        "nine_terminal_matches_fixture_target": nine_data["terminal_matches_fixture_target"],
        "nine_partition_exact_digest": (
            nine_data["normalized_partition_sha256"] == EXPECTED_NINE_PARTITION_SHA256
        ),
        "all_36_subsets_censused": len(rows) == 36,
        "exact_five_match": matches == EXPECTED_MATCHING_SUBSETS,
        "exact_31_fail": failures == expected_failures and len(failures) == 31,
    }
    passed = all(checks.values())
    return {
        "certificate": "THE REDUCED BRAIDS",
        "status": "PASS" if passed else "FAIL",
        "findings": (
            "the three pair-cohorts' normalized depth-0..64 braids are IDENTICAL (the reduced partition law)",
            "exactly 5/36 two-subset restrictions reproduce the pair-braid",
            f"the exact five subsets are {compact(matches)}",
            "the other 31 two-subset restrictions FAIL",
        ),
        "scope": (
            "IDENTICAL means the landed normalized depth-0..64 Boolean partition braid; "
            "it does not identify the unequal-duration raw meet-to-funnel byte streams"
        ),
        "pair_event_order": CHRONOLOGICAL_ORDER,
        "pair_braid_sha256_by_event": pair_sha_rows,
        "pair_rle_topology_by_event": tuple(
            (event, pair_data["rle_shapes"][event]) for event in CHRONOLOGICAL_ORDER
        ),
        "matching_subsets": matches,
        "expected_matching_subsets": EXPECTED_MATCHING_SUBSETS,
        "failing_subsets": failures,
        "matching_count": len(matches),
        "failing_count": len(failures),
        "restriction_rows": tuple(rows),
        "checks": checks,
        "pass": passed,
    }


def target_blind_accounting(times: dict[int, int]) -> tuple[dict[str, object], ...]:
    rows = []
    for source, target in zip(CHRONOLOGICAL_ORDER, CHRONOLOGICAL_ORDER[1:]):
        gap = times[target] - times[source]
        quotient, remainder = divmod(gap, LCM_SKELETON)
        catchup = gap - LCM_SKELETON
        rows.append({
            "transition": (source, target),
            "gap": gap,
            "lcm_multiple": quotient,
            "euclidean_remainder": remainder,
            "one_lcm_catchup": catchup,
            "euclidean_accounting_holds": gap == quotient * LCM_SKELETON + remainder,
            "cycle841_accounting_holds": gap == LCM_SKELETON + catchup,
        })
    return tuple(rows)


def certificate_accounting(
    pair_data: dict[str, object],
    self_tree: ast.Module,
) -> dict[str, object]:
    pair_funnels_present = set(pair_data["funnel_states"]) == set(CHRONOLOGICAL_ORDER)
    clocks = {
        "MOMENT": {
            event: PAIR_FUNNEL_MOVEMENTS[event] + 5 for event in CHRONOLOGICAL_ORDER
        },
        "MOMENT_MINUS_FIVE": {
            event: PAIR_FUNNEL_MOVEMENTS[event] for event in CHRONOLOGICAL_ORDER
        },
    }
    clock_rows = tuple({
        "clock": clock,
        "times_chronological_1_2_0": tuple(times[event] for event in CHRONOLOGICAL_ORDER),
        "rows": target_blind_accounting(times),
    } for clock, times in clocks.items())
    raw_by_clock = tuple(
        tuple(row["one_lcm_catchup"] for row in clock["rows"])
        for clock in clock_rows
    )
    euclidean_by_clock = tuple(
        tuple(
            (row["lcm_multiple"], row["euclidean_remainder"])
            for row in clock["rows"]
        )
        for clock in clock_rows
    )
    fixed_residual_hits = tuple(
        tuple(
            candidate for candidate in NINE_RESIDUAL_TARGET
            if (row["gap"] - candidate) % LCM_SKELETON == 0
        )
        for row in clock_rows[0]["rows"]
    )
    accounting_node = function_node(self_tree, "target_blind_accounting")
    target_literals = {
        item.value for item in ast.walk(accounting_node)
        if isinstance(item, ast.Constant) and isinstance(item.value, int)
    }
    target_blind = (
        "NINE_RESIDUAL_TARGET" not in loaded_names(accounting_node)
        and 595 not in target_literals
        and 64 not in target_literals
    )
    identity_holds = all(
        row["euclidean_accounting_holds"] and row["cycle841_accounting_holds"]
        for clock in clock_rows for row in clock["rows"]
    )
    residual_failure_real = (
        raw_by_clock == ((35603, 877907), (35603, 877907))
        and all(raw != NINE_RESIDUAL_TARGET for raw in raw_by_clock)
        and fixed_residual_hits == ((), ())
    )
    checks = {
        "all_pair_funnels_replayed": pair_funnels_present,
        "lcm_exact": LCM_SKELETON == 17856,
        "target_blind_implementation_ast": target_blind,
        "physics_clocks_are_uniform_shift": all(
            clocks["MOMENT"][event] - clocks["MOMENT_MINUS_FIVE"][event] == 5
            for event in CHRONOLOGICAL_ORDER
        ),
        "pair_gap_values_exact": tuple(
            row["gap"] for row in clock_rows[0]["rows"]
        ) == (53459, 895763),
        "lcm_multiple_plus_remainder_exact": (
            euclidean_by_clock
            == (((2, 17747), (50, 2963)), ((2, 17747), (50, 2963)))
        ),
        "cycle841_accounting_identity_holds": identity_holds,
        "residual_595_64_failure_real": residual_failure_real,
    }
    passed = all(checks.values())
    return {
        "certificate": "THE ACCOUNTING",
        "status": "PASS" if passed else "FAIL",
        "findings": (
            "the 841 accounting identity HOLDS for the pair gaps on both physics clocks",
            "the pair-gap {595,64} residual law FAILS",
            "the target-blind one-LCM catch-ups are {35603,877907} on both physics clocks",
            "the Euclidean lcm-multiple decompositions are 2*17856+17747 and 50*17856+2963",
        ),
        "accounting_scope": (
            "gap=lcm+catch-up is an exact accounting identity, not a prediction of the catch-up values"
        ),
        "formula": "catchup(s,t)=t_target-t_source-lcm(4464,5952)",
        "lcm_skeleton": LCM_SKELETON,
        "clock_rows": clock_rows,
        "raw_catchup_by_clock": raw_by_clock,
        "euclidean_decomposition_by_clock": euclidean_by_clock,
        "residual_target_used_only_after_raw_computation": NINE_RESIDUAL_TARGET,
        "fixed_residual_hits": fixed_residual_hits,
        "checks": checks,
        "pass": passed,
    }


def support_indices(mask: int) -> tuple[int, ...]:
    support = []
    while mask:
        bit = mask & -mask
        support.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(support)


def certificate_pair_wires(pair_data: dict[str, object]) -> dict[str, object]:
    states = pair_data["funnel_states"]
    weights = tuple(states[event].bit_count() for event in EVENT_ORDER)
    wire_patterns = {
        wire: tuple((states[event] >> wire) & 1 for event in EVENT_ORDER)
        for wire in THREE_WIRES
    }
    codes = {
        event: tuple((states[event] >> wire) & 1 for wire in THREE_WIRES)
        for event in EVENT_ORDER
    }
    event1_iff_code001 = all(
        (codes[event] == (0, 0, 1)) == (event == 1)
        for event in EVENT_ORDER
    )
    event02_iff_code110 = all(
        (codes[event] == (1, 1, 0)) == (event in (0, 2))
        for event in EVENT_ORDER
    )
    each_wire_discriminates_both_directions = all(
        (((states[event] >> wire) & 1) == expected) == (event == 1)
        for wire, expected in ((88, 0), (124, 0), (125, 1))
        for event in EVENT_ORDER
    )
    register = frozenset(REGISTER_WIRES)
    edge_rows = []
    for source, target in ((0, 2), (2, 1), (0, 1)):
        support = support_indices(states[source] ^ states[target])
        outside = tuple(sorted(set(support) - register))
        exactly_one_is_event1 = (source == 1) ^ (target == 1)
        edge_rows.append({
            "edge": (source, target),
            "xor_support_count": len(support),
            "xor_support_sha256": object_digest(support),
            "outside_register_support": outside,
            "three_wire_iff_exactly_one_event1": (outside == THREE_WIRES) == exactly_one_is_event1,
            "register_only_iff_neither_event1": (outside == ()) == (not exactly_one_is_event1),
        })
    outside_by_edge = tuple(row["outside_register_support"] for row in edge_rows)
    expected_weights = tuple(49 + 2 * rank * rank for rank in range(3))
    checks = {
        "three_wire_patterns_exact": wire_patterns == {
            88: (1, 1, 0), 124: (1, 1, 0), 125: (0, 0, 1),
        },
        "event1_iff_code001": event1_iff_code001,
        "events0_or2_iff_code110": event02_iff_code110,
        "each_wire_discriminates_both_directions": each_wire_discriminates_both_directions,
        "outside_register_support_exact": outside_by_edge == ((), THREE_WIRES, THREE_WIRES),
        "extension_both_directions_every_edge": all(
            row["three_wire_iff_exactly_one_event1"]
            and row["register_only_iff_neither_event1"]
            for row in edge_rows
        ),
        "three_point_quadratic_exact": weights == expected_weights == (49, 51, 57),
    }
    passed = all(checks.values())
    return {
        "certificate": "THE PAIR WIRES",
        "status": "PASS" if passed else "FAIL",
        "findings": (
            "wires (88/124/125) discriminate/encode in both directions on the three pair-funnel configurations",
            "the pair three-wire register extension (wires 88/124/125) HOLDS in both directions on every relevant event edge",
            "the pair quadratic weight law is exact on its three points",
        ),
        "event_order_for_codes_and_weights": EVENT_ORDER,
        "wire_patterns_by_wire": wire_patterns,
        "three_wire_code_by_event": codes,
        "edge_rows": tuple(edge_rows),
        "weights": weights,
        "quadratic_values": expected_weights,
        "quadratic_formula": "w_pair(q)=49+2*q^2 for q=0,1,2",
        "quadratic_scope": "THREE-POINT EXACTNESS ONLY; no extrapolation beyond q in {0,1,2} is claimed",
        "checks": checks,
        "pass": passed,
    }


def certificate_controls(
    packet_controls: dict[str, object],
    fixtures: dict[str, object],
    replay_fixtures: dict[str, object],
    pair_data: dict[str, object],
    nine_data: dict[str, object],
    science_certificates: tuple[dict[str, object], ...],
    elapsed: float,
) -> dict[str, object]:
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    first_fixture_digest = fixture_digest(fixtures)
    replay_fixture_digest = fixture_digest(replay_fixtures)
    determinism = {
        "fixture_decode_replay_exact": (
            first_fixture_digest == replay_fixture_digest
            and fixtures["raw_digests"] == replay_fixtures["raw_digests"]
            and fixtures["checks"] == replay_fixtures["checks"]
        ),
        "pair_duplicate_initial": pair_data["duplicate_initial"],
        "pair_duplicate_schedule_masks": pair_data["duplicate_schedule_masks"],
        "pair_duplicate_each_funnel": all(pair_data["duplicate_at_funnel"].values()),
        "pair_duplicate_end": pair_data["duplicate_end"],
        "nine_duplicate_initial": nine_data["duplicate_initial"],
        "nine_duplicate_tail": nine_data["duplicate_tail_exact"],
        "nine_duplicate_end": nine_data["duplicate_end"],
    }
    science_digest = object_digest(tuple(
        {key: value for key, value in certificate.items() if key != "pass"}
        for certificate in science_certificates
    ))
    base_pass = all((
        packet_controls["pass"],
        fixtures["pass"],
        replay_fixtures["pass"],
        all(determinism.values()),
        not blocked_loaded,
        not FIREWALL.hits,
        elapsed < AUDIT_TIMEOUT_SEC,
    ))
    return {
        "certificate": "CONTROLS",
        "status": "FAIL",
        "findings": (
            "all source SHAs and git blobs are exact",
            "all source primaries are BLOCKLISTED and consumed as text/AST only",
            "determinism duplicates and fixture replay are exact",
            "literal AUDIT_INPUT_PATHS are existing worktree-relative paths",
            "runtime is below 1400s and stdout is below 150KB",
        ),
        "source_controls": packet_controls,
        "fixture_checks": fixtures["checks"],
        "fixture_digest_first": first_fixture_digest,
        "fixture_digest_replay": replay_fixture_digest,
        "determinism": determinism,
        "science_digest": science_digest,
        "blocked_modules_loaded_at_end": blocked_loaded,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_below_limit": False,
        "base_pass_before_stdout": base_pass,
        "pass": False,
    }


def stable_output(
    certificates: dict[str, dict[str, object]],
    report: dict[str, object],
) -> str:
    controls = certificates["CONTROLS"]
    previous = -1
    for _ in range(12):
        output = "\n".join([
            *(f"CERTIFICATE_{name}={compact(value)}" for name, value in certificates.items()),
            f"REPORT={compact(report)}",
        ]) + "\n"
        size = len(output.encode("utf-8"))
        controls["stdout_bytes"] = size
        controls["stdout_below_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["base_pass_before_stdout"] and controls["stdout_below_limit"]
        controls["status"] = "PASS" if controls["pass"] else "FAIL"
        report["checks"]["CONTROLS"] = controls["pass"]
        report["pass"] = all(report["checks"].values())
        report["stdout_bytes"] = size
        report["terminal"] = (
            "CYCLE846_REDUCED_INDEPENDENT_CHECK_PASS"
            if report["pass"] else "CYCLE846_REDUCED_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        if size == previous:
            return output
        previous = size
    raise AssertionError("stdout byte accounting did not stabilize")


def run() -> int:
    started = monotonic()
    packet = read_source_packet()
    fixtures = decode_fixtures(packet["trees"][FIXTURE_PATH])
    pair_data = replay_pair_braids(fixtures, PAIR_FUNNEL_MOVEMENTS)
    nine_data = replay_nine_tail(fixtures)
    reduced = certificate_reduced_braids(pair_data, nine_data)
    accounting = certificate_accounting(pair_data, packet["self_tree"])
    wires = certificate_pair_wires(pair_data)
    replay_fixtures = decode_fixtures(packet["trees"][FIXTURE_PATH])
    elapsed = monotonic() - started
    controls = certificate_controls(
        packet["controls"], fixtures, replay_fixtures, pair_data, nine_data,
        (reduced, accounting, wires), elapsed,
    )
    certificates = {
        "THE_REDUCED_BRAIDS": reduced,
        "THE_ACCOUNTING": accounting,
        "THE_PAIR_WIRES": wires,
        "CONTROLS": controls,
    }
    science_pass = all(certificate["pass"] for certificate in (reduced, accounting, wires))
    report = {
        "cycle": 846,
        "role": "INDEPENDENT ADVERSARIAL CHECKER — the reduced structure",
        "adversarial_verdict": "PRIMARY_NOT_REFUTED" if science_pass else "PRIMARY_REFUTED",
        "primary_science_refuted": not science_pass,
        "checks": {
            "THE_REDUCED_BRAIDS": reduced["pass"],
            "THE_ACCOUNTING": accounting["pass"],
            "THE_PAIR_WIRES": wires["pass"],
            "CONTROLS": False,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
        "terminal": "CYCLE846_REDUCED_INDEPENDENT_CHECK_HONEST_FAIL",
    }
    output = stable_output(certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 846,
            "status": "FAIL",
            "failure": "stdout limit exceeded",
            "terminal": "CYCLE846_REDUCED_INDEPENDENT_CHECK_HONEST_FAIL",
        }))
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        print(compact({
            "cycle": 846,
            "status": "FAIL",
            "error_type": type(error).__name__,
            "error": str(error),
            "terminal": "CYCLE846_REDUCED_INDEPENDENT_CHECK_HONEST_FAIL",
        }))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
