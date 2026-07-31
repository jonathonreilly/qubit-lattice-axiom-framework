#!/usr/bin/env python3
"""Cycle 845: partition-refinement route for the merged-why question.

All named source primaries are blocked from import and are consumed only as
text/AST.  The landed Cycle-830 literal fixture bank is decoded independently,
and the Boolean X/CNOT/Toffoli evolution is reimplemented with Python integers.

Certificate A computes the full event-0 nine-trajectory partition sequence
from the tick-3 meet to S*, at the declared complete-movement stride, as an
exact reconstructible run-length encoding.  Certificate B compares the last
64 complete movements across cohorts and cross-references every partition
event against the Cycle-835 39-field register change-times.  Certificate C
gives the narrow partition-law verdict.  Certificate D enforces provenance,
BLOCKLIST, determinism, runtime, and stdout controls.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle835_register_mechanism_2026_07_28.py",
    "scripts/frontier_cycle842_local_causal_theorem_2026_07_28.py",
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
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR23-20260729"
RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
MEET_CONTROLLER_TICK = 3
PARTITION_STRIDE_CONTROLLER_TICKS = RING_STATIONS
CROSS_COHORT_WINDOW_MOVEMENTS = 64
EVENT_ORDER = (0, 2, 1)
FUNNEL_MOMENTS = {0: 14739, 2: 33190, 1: 51110}
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
WITNESS_PAIR = BACKBONE[0]
REGISTER_FIELDS = (
    "source.LEFT_ENDPOINT",
    "source.RIGHT_ENDPOINT",
    "bank0.cell0.pred[0]",
    "bank0.cell0.pred[1]",
    "bank0.cell0.pred[2]",
    "bank0.cell0.pred[3]",
    "bank0.cell0.pred[4]",
    "bank0.cell0.pred[5]",
    "bank0.cell0.rotor_before[0]",
    "bank0.cell0.rotor_before[1]",
    "bank0.cell0.rotor_before[2]",
    "bank0.cell0.rotor_before[3]",
    "bank0.cell0.rotor_after[0]",
    "bank0.cell0.rotor_after[1]",
    "bank0.cell0.rotor_after[2]",
    "bank0.cell0.rotor_after[3]",
    "bank0.cell0.carry",
    "bank0.cell0.orientation",
    "bank0.cell1.pred[0]",
    "bank0.cell1.pred[1]",
    "bank0.cell1.pred[2]",
    "bank0.cell1.pred[3]",
    "bank0.cell1.pred[4]",
    "bank0.cell1.pred[5]",
    "bank0.cell1.rotor_before[1]",
    "bank0.cell1.rotor_before[2]",
    "bank0.cell1.rotor_before[3]",
    "bank0.cell1.rotor_after[1]",
    "bank0.cell1.rotor_after[2]",
    "bank0.cell1.carry",
    "bank0.cell1.orientation",
    "bank0.HEAD[0]",
    "bank0.HEAD[1]",
    "bank0.HEAD[2]",
    "bank0.HEAD[3]",
    "bank0.HEAD[4]",
    "bank0.HEAD[5]",
    "bank0.ROTOR[1]",
    "bank0.ROTOR[2]",
)
# Mechanically copied from the SHA-pinned Cycle-835 trajectory certificate.
REGISTER_WIRES = (
    1, 6, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 71, 75, 76, 77, 78, 79, 80, 82, 83,
    84, 86, 87, 89, 105, 109, 110, 111, 112, 113, 114, 116,
    117,
)
EXPECTED_FUNNEL_SHA256 = {
    0: "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a",
    2: "0015151ee4b751c35a5671fbb4f301d8569e78fc5a7ebe9f77372865b153c99b",
    1: "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41",
}
EXPECTED_FUNNEL_WEIGHTS = {0: 44, 2: 45, 1: 46}
EXPECTED_CHANGE_TIME_UNIQUE_SEQUENCES = 74
EXPECTED_CHANGE_TIME_RAW_BYTES = 203926
EXPECTED_CHANGE_TIME_RAW_SHA256 = (
    "3d588a959c0f461859b41931a104237adcd2df5e33bd29aa7457811cca0d702d"
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
EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[2]:
        "6b8c26ff77d99225aaa985c645aeee9fa1fb3db19517aec727ff38e0cbcc03f5",
    AUDIT_INPUT_PATHS[3]:
        "65ced87db73db177c561e0dd293ae88963c15929d820f6dd99417a27ba647def",
}
EXPECTED_SOURCE_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[2]: "a9bfc3d151a591b3d0a4ba06acaa30ed04ff7e67",
    AUDIT_INPUT_PATHS[3]: "a1836d84d8dda74c4f79cc1bbc60ef798d86a2e3",
}
COPIED_LINEAGE_PINS = {
    "cycle830": {
        "commit": "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "source_sha256": EXPECTED_SOURCE_SHA256[AUDIT_INPUT_PATHS[1]],
        "git_blob": EXPECTED_SOURCE_GIT_BLOBS[AUDIT_INPUT_PATHS[1]],
    },
    "cycle835": {
        "commit": "1522d92ec6",
        "source_sha256": EXPECTED_SOURCE_SHA256[AUDIT_INPUT_PATHS[2]],
        "git_blob": EXPECTED_SOURCE_GIT_BLOBS[AUDIT_INPUT_PATHS[2]],
    },
}

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
Partition = tuple[tuple[int, ...], ...]

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any text/AST-only source primary is imported."""

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
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
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
        timeout=20,
    ).stdout.strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
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


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    source_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    source_blobs = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    ast_basis = {
        "cycle719_core": {
            "interleaved_program", "run_orbit",
        } <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle830_partition_lineage": {
            "decode_fixtures", "partition_keys",
            "trajectory_and_mechanism_certificates",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle835_register_lineage": {
            "track_register_trajectories", "change_time_encoding",
            "register_wires",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle842_meet_lineage": {
            "meeting_geometry", "evolve_bounded_forward",
            "certificate_b_forward_argument",
        } <= function_names(trees[AUDIT_INPUT_PATHS[3]]),
    }
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    stdlib_roots = set(sys.stdlib_module_names) | {"__future__"}
    literal_cross_checks = {
        "cycle835_REGISTER_FIELDS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "REGISTER_FIELDS"
            ) == REGISTER_FIELDS,
        "cycle835_FUNNEL_MOMENTS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "FUNNEL_MOMENTS"
            ) == FUNNEL_MOMENTS,
        "cycle835_BACKBONE":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "BACKBONE"
            ) == BACKBONE,
        "cycle842_MEET_CONTROLLER_TICK":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "MEET_CONTROLLER_TICK"
            ) == MEET_CONTROLLER_TICK,
        "cycle842_EXPECTED_REACHING_KEYS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "EXPECTED_REACHING_KEYS"
            ) == tuple((0, pair) for pair in BACKBONE),
    }
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 7,
        "source_sha256": source_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "source_git_blobs": source_blobs,
        "expected_source_git_blobs": EXPECTED_SOURCE_GIT_BLOBS,
        "copied_lineage_pins": COPIED_LINEAGE_PINS,
        "AST_basis": ast_basis,
        "literal_cross_checks": literal_cross_checks,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_start": blocked_loaded,
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= stdlib_roots,
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": git_text("branch", "--show-current"),
        "expected_git_branch": EXPECTED_BRANCH,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob(self_payload),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 7
        and source_sha == EXPECTED_SOURCE_SHA256
        and source_blobs == EXPECTED_SOURCE_GIT_BLOBS
        and all(ast_basis.values())
        and all(literal_cross_checks.values())
        and not blocked_loaded
        and not FIREWALL.hits
        and result["stdlib_only"]
        and result["git_branch"] == EXPECTED_BRANCH
    )
    return result, trees


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


def state_sha256(state: int) -> str:
    return sha256(bytes(
        (state >> wire) & 1 for wire in range(STATE_BITS)
    )).hexdigest()


def packed_sha256(state: int) -> str:
    return sha256(
        state.to_bytes(STATE_BYTES, "little")
    ).hexdigest()


def decode_cycle830_fixtures(
    tree: ast.Module,
) -> dict[str, object]:
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
    public = {
        "macro_gate_counts": lengths,
        "macro_gate_count": sum(lengths),
        "family_key_count": len(states),
        "target_hamming_weight": target.bit_count(),
        "target_state_sha256": state_sha256(target),
        "target_packed_sha256": packed_sha256(target),
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "pass": (
            len(lengths) == RING_STATIONS
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
            and len(states) == FAMILY_SIZE
            and target.bit_count() == EXPECTED_FUNNEL_WEIGHTS[0]
            and state_sha256(target) == EXPECTED_FUNNEL_SHA256[0]
        ),
    }
    return {
        "macros": tuple(macros),
        "keys": keys,
        "states": states,
        "target": target,
        "public": public,
    }


def bit_slice(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        value = state
        while value:
            bit = value & -value
            columns[bit.bit_length() - 1] |= 1 << lane
            value ^= bit
    return columns


def capture_lanes(
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
    return sum(
        1 << wire
        for wire, column in enumerate(columns)
        if (column >> lane) & 1
    )


def build_phase_schedules(
    macros: tuple[tuple[Gate, ...], ...],
    lane_pairs: tuple[Pair, ...],
) -> tuple[tuple[MaskedGate, ...], ...]:
    schedules = []
    for phase in range(RING_STATIONS):
        rows = []
        for station, macro in enumerate(macros):
            lane_mask = sum(
                1 << lane
                for lane, pair in enumerate(lane_pairs)
                if station in {
                    (pair[0] + phase) % RING_STATIONS,
                    (pair[1] + phase) % RING_STATIONS,
                }
            )
            if lane_mask:
                rows.extend(
                    (kind, first, second, third, lane_mask)
                    for kind, first, second, third in macro
                )
        schedules.append(tuple(rows))
    return tuple(schedules)


def movement_schedule(
    phase_schedules: tuple[tuple[MaskedGate, ...], ...],
) -> tuple[MaskedGate, ...]:
    return tuple(
        row for schedule in phase_schedules for row in schedule
    )


def advance(
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


def compile_words(
    macros: tuple[tuple[Gate, ...], ...],
) -> dict[Pair, tuple[tuple[int, int, int], ...]]:
    words = {}
    for pair in BACKBONE:
        rows = []
        for phase in range(RING_STATIONS):
            live = {
                (pair[0] + phase) % RING_STATIONS,
                (pair[1] + phase) % RING_STATIONS,
            }
            for station, macro in enumerate(macros):
                if station not in live:
                    continue
                for kind, first, second, third in macro:
                    if kind == 0:
                        rows.append((0, 0, 1 << first))
                    elif kind == 1:
                        rows.append((1, 1 << first, 1 << second))
                    elif kind == 2:
                        rows.append((
                            2, (1 << first) | (1 << second), 1 << third,
                        ))
                    else:
                        raise AssertionError(("unknown gate kind", kind))
        words[pair] = tuple(rows)
    if {len(word) for word in words.values()} != {WORD_GATE_COUNT}:
        raise AssertionError("unexpected compiled word length")
    return words


def apply_compiled_word(
    state: int,
    word: tuple[tuple[int, int, int], ...],
    *,
    reverse: bool = False,
) -> int:
    rows = reversed(word) if reverse else word
    for kind, controls, target in rows:
        if kind == 0 or state & controls == controls:
            state ^= target
    return state


def partition_of(states: tuple[int, ...]) -> Partition:
    groups: dict[int, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(sorted(
        (tuple(group) for group in groups.values()),
        key=lambda group: group[0],
    ))


def equivalent_pairs(partition: Partition) -> frozenset[tuple[int, int]]:
    return frozenset(
        pair
        for block in partition
        for pair in combinations(block, 2)
    )


def transition_kind(before: Partition, after: Partition) -> str:
    before_pairs = equivalent_pairs(before)
    after_pairs = equivalent_pairs(after)
    if before_pairs < after_pairs:
        return "COARSENING"
    if after_pairs < before_pairs:
        return "REFINEMENT"
    if before_pairs != after_pairs:
        return "MIXED"
    return "UNCHANGED"


def varying_wire_indices(states: tuple[int, ...]) -> tuple[int, ...]:
    first = states[0]
    mask = 0
    for state in states[1:]:
        mask |= first ^ state
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def partition_event(
    before: Partition,
    after: Partition,
    before_states: tuple[int, ...],
    after_states: tuple[int, ...],
    *,
    from_tick: int,
    to_tick: int,
    from_movement: int | None,
    to_movement: int,
) -> dict[str, object]:
    before_wires = varying_wire_indices(before_states)
    after_wires = varying_wire_indices(after_states)
    return {
        "from_controller_tick": from_tick,
        "to_controller_tick": to_tick,
        "from_movement": from_movement,
        "to_movement": to_movement,
        "kind": transition_kind(before, after),
        "before_partition": before,
        "after_partition": after,
        "before_block_sizes": tuple(map(len, before)),
        "after_block_sizes": tuple(map(len, after)),
        "before_distinct_nodes": len(before),
        "after_distinct_nodes": len(after),
        "before_varying_wire_count": len(before_wires),
        "after_varying_wire_count": len(after_wires),
        "before_varying_wire_indices": before_wires,
        "after_varying_wire_indices": after_wires,
    }


def partition_rle(
    controller_ticks: tuple[int, ...],
    movements: tuple[int | None, ...],
    partitions: tuple[Partition, ...],
) -> tuple[dict[str, object], ...]:
    if not (
        len(controller_ticks) == len(movements) == len(partitions)
        and partitions
    ):
        raise AssertionError("malformed partition sample sequence")
    rows = []
    start = 0
    for index in range(1, len(partitions) + 1):
        if (
            index < len(partitions)
            and partitions[index] == partitions[start]
        ):
            continue
        rows.append({
            "sample_index_start": start,
            "sample_index_end": index - 1,
            "sample_count": index - start,
            "controller_tick_start": controller_ticks[start],
            "controller_tick_end": controller_ticks[index - 1],
            "movement_start": movements[start],
            "movement_end": movements[index - 1],
            "partition": partitions[start],
            "block_sizes": tuple(map(len, partitions[start])),
            "distinct_nodes": len(partitions[start]),
        })
        start = index
    return tuple(rows)


def partition_sequence_encoding(
    partitions: tuple[Partition, ...],
) -> dict[str, object]:
    raw = bytearray()
    for partition in partitions:
        labels = [0] * len(BACKBONE)
        for block_id, block in enumerate(partition):
            for lane in block:
                labels[lane] = block_id
        raw.extend(labels)
    compressed = zlib.compress(bytes(raw), level=9)
    decoded_raw = zlib.decompress(compressed)
    decoded = []
    for offset in range(0, len(decoded_raw), len(BACKBONE)):
        labels = decoded_raw[offset:offset + len(BACKBONE)]
        groups: dict[int, list[int]] = {}
        for lane, block_id in enumerate(labels):
            groups.setdefault(block_id, []).append(lane)
        decoded.append(tuple(
            tuple(groups[block_id]) for block_id in sorted(groups)
        ))
    return {
        "format":
            "one nine-byte restricted-growth partition row per sample; "
            "block IDs are assigned in first-label order; rows concatenate; "
            "zlib level 9; Base85",
        "sample_count": len(partitions),
        "raw_bytes": len(raw),
        "raw_sha256": sha256(raw).hexdigest(),
        "compressed_bytes": len(compressed),
        "compressed_sha256": sha256(compressed).hexdigest(),
        "payload_b85": base64.b85encode(compressed).decode("ascii"),
        "roundtrip_exact": tuple(decoded) == partitions,
    }


def event0_full_partition_dynamics(
    fixtures: dict[str, object],
) -> dict[str, object]:
    macros = fixtures["macros"]
    states_by_key = fixtures["states"]
    target = fixtures["target"]
    assert isinstance(macros, tuple)
    assert isinstance(states_by_key, dict)
    assert isinstance(target, int)
    initial = tuple(states_by_key[(0, pair)] for pair in BACKBONE)
    lane_pairs = BACKBONE + BACKBONE
    duplicate_initial = initial + initial
    phase_schedules = build_phase_schedules(macros, lane_pairs)
    schedule = movement_schedule(phase_schedules)

    meet_columns = bit_slice(duplicate_initial)
    for phase in range(MEET_CONTROLLER_TICK):
        advance(meet_columns, phase_schedules[phase])
    meet_all = capture_lanes(meet_columns, 2 * len(BACKBONE))
    meet_states = meet_all[:len(BACKBONE)]
    meet_duplicate_exact = (
        meet_states == meet_all[len(BACKBONE):]
    )

    columns = bit_slice(duplicate_initial)
    sample_ticks = [MEET_CONTROLLER_TICK]
    sample_movements: list[int | None] = [None]
    sample_partitions = [partition_of(meet_states)]
    event_rows = []
    previous_partition = sample_partitions[0]
    previous_states = meet_states
    previous_tick = MEET_CONTROLLER_TICK
    previous_movement: int | None = None
    duplicate_exact_every_sample = meet_duplicate_exact
    forward_tail_partitions: dict[int, Partition] = {}
    forward_tail_states: dict[int, tuple[int, ...]] = {}

    for movement in range(1, FUNNEL_MOMENTS[0] + 1):
        advance(columns, schedule)
        all_states = capture_lanes(columns, 2 * len(BACKBONE))
        primary_states = all_states[:len(BACKBONE)]
        duplicate_exact_every_sample &= (
            primary_states == all_states[len(BACKBONE):]
        )
        tick = movement * RING_STATIONS
        partition = partition_of(primary_states)
        sample_ticks.append(tick)
        sample_movements.append(movement)
        sample_partitions.append(partition)
        if movement >= (
            FUNNEL_MOMENTS[0] - CROSS_COHORT_WINDOW_MOVEMENTS
        ):
            forward_tail_partitions[movement] = partition
            forward_tail_states[movement] = primary_states
        if partition != previous_partition:
            event_rows.append(partition_event(
                previous_partition,
                partition,
                previous_states,
                primary_states,
                from_tick=previous_tick,
                to_tick=tick,
                from_movement=previous_movement,
                to_movement=movement,
            ))
        previous_partition = partition
        previous_states = primary_states
        previous_tick = tick
        previous_movement = movement

    final_states = previous_states
    partitions = tuple(sample_partitions)
    ticks = tuple(sample_ticks)
    movements = tuple(sample_movements)
    rle = partition_rle(ticks, movements, partitions)
    total = (tuple(range(len(BACKBONE))),)
    total_union_sample_indices = tuple(
        index for index, partition in enumerate(partitions)
        if partition == total
    )
    total_union_movements = tuple(
        movements[index] for index in total_union_sample_indices
    )
    sequence_encoding = partition_sequence_encoding(partitions)
    terminal_start = len(partitions) - (
        CROSS_COHORT_WINDOW_MOVEMENTS + 1
    )
    terminal_rle = partition_rle(
        ticks[terminal_start:],
        movements[terminal_start:],
        partitions[terminal_start:],
    )
    event_kind_counts = tuple(sorted({
        kind: sum(row["kind"] == kind for row in event_rows)
        for kind in ("COARSENING", "REFINEMENT", "MIXED")
    }.items()))
    return {
        "meet_states": meet_states,
        "partitions": partitions,
        "controller_ticks": ticks,
        "movements": movements,
        "rle": rle,
        "event_rows": tuple(event_rows),
        "forward_tail_partitions": forward_tail_partitions,
        "forward_tail_states": forward_tail_states,
        "final_states": final_states,
        "total_union_sample_indices": total_union_sample_indices,
        "total_union_movements": total_union_movements,
        "public": {
            "scope":
                "nine event-0 predicate-marked trajectories; full 5815-bit "
                "state equality",
            "sample_grid":
                "exact meet at controller tick 3, followed by every complete "
                "movement boundary at controller ticks 11*t for t=1..14739",
            "declared_stride_controller_ticks":
                PARTITION_STRIDE_CONTROLLER_TICKS,
            "sample_count": len(partitions),
            "movement_samples": FUNNEL_MOMENTS[0],
            "exact_sequence_sha256": digest(tuple(zip(ticks, partitions))),
            "exact_sequence_encoding": sequence_encoding,
            "exact_sequence_RLE_row_count": len(rle),
            "exact_sequence_RLE_sha256": digest(rle),
            "RLE_reconstructs_sample_count":
                sum(row["sample_count"] for row in rle),
            "terminal_64_movement_RLE": terminal_rle,
            "partition_event_count": len(event_rows),
            "partition_event_sha256": digest(tuple(event_rows)),
            "event_kind_counts": event_kind_counts,
            "total_union_sample_count": len(total_union_sample_indices),
            "total_union_movements_sha256": digest(
                total_union_movements
            ),
            "first_total_union_movement":
                total_union_movements[0]
                if total_union_movements else None,
            "last_total_union_before_funnel":
                total_union_movements[-2]
                if len(total_union_movements) > 1 else None,
            "funnel_union_movement": total_union_movements[-1],
            "funnel_union_is_first_total_union_from_meet":
                total_union_movements == (FUNNEL_MOMENTS[0],),
            "funnel_pre_union_partition": partitions[-2],
            "funnel_pre_union_distinct_nodes": len(partitions[-2]),
            "pre_union_varying_wire_indices":
                varying_wire_indices(
                    forward_tail_states[FUNNEL_MOMENTS[0] - 1]
                ),
            "pre_union_varying_wire_count": len(
                varying_wire_indices(
                    forward_tail_states[FUNNEL_MOMENTS[0] - 1]
                )
            ),
            "final_state_sha256_by_lane":
                tuple(state_sha256(state) for state in final_states),
            "duplicate_initial_exact": initial == duplicate_initial[:9],
            "duplicate_meet_exact": meet_duplicate_exact,
            "duplicate_exact_every_sample":
                duplicate_exact_every_sample,
            "movement_schedule_rows": len(schedule),
            "pass": (
                fixtures["public"]["pass"]
                and len(schedule) > WORD_GATE_COUNT
                and sum(row["sample_count"] for row in rle)
                == len(partitions)
                and sequence_encoding["roundtrip_exact"]
                and total_union_sample_indices
                and total_union_sample_indices[-1]
                == len(partitions) - 1
                and all(state == target for state in final_states)
                and duplicate_exact_every_sample
            ),
        },
    }


def register_projection(columns: list[int], lane: int) -> int:
    return sum(
        ((columns[wire] >> lane) & 1) << index
        for index, wire in enumerate(REGISTER_WIRES)
    )


def witness_register_trajectories(
    fixtures: dict[str, object],
) -> dict[str, object]:
    macros = fixtures["macros"]
    states_by_key = fixtures["states"]
    assert isinstance(macros, tuple)
    assert isinstance(states_by_key, dict)
    lane_rows = tuple(
        (event, role)
        for event in EVENT_ORDER
        for role in ("primary", "duplicate")
    )
    primary_index = {
        event: index
        for index, (event, role) in enumerate(lane_rows)
        if role == "primary"
    }
    duplicate_index = {
        event: index
        for index, (event, role) in enumerate(lane_rows)
        if role == "duplicate"
    }
    initial_states = tuple(
        states_by_key[(event, WITNESS_PAIR)]
        for event, _role in lane_rows
    )
    columns = bit_slice(initial_states)
    phases = build_phase_schedules(
        macros, (WITNESS_PAIR,) * len(lane_rows)
    )
    schedule = movement_schedule(phases)
    changes: dict[int, list[list[int]]] = {
        event: [[] for _wire in REGISTER_WIRES]
        for event in EVENT_ORDER
    }
    previous = {
        event: register_projection(columns, primary_index[event])
        for event in EVENT_ORDER
    }
    duplicate_initial_exact = all(
        initial_states[primary_index[event]]
        == initial_states[duplicate_index[event]]
        for event in EVENT_ORDER
    )
    duplicate_projection_exact_every_movement = True
    duplicate_full_window_exact = True
    funnels: dict[int, int] = {}
    duplicate_funnels: dict[int, int] = {}
    forward_windows: dict[int, dict[int, int]] = {
        event: {} for event in EVENT_ORDER
    }

    for movement in range(1, max(FUNNEL_MOMENTS.values()) + 1):
        advance(columns, schedule)
        for event in EVENT_ORDER:
            if movement > FUNNEL_MOMENTS[event]:
                continue
            primary_projection = register_projection(
                columns, primary_index[event]
            )
            duplicate_projection = register_projection(
                columns, duplicate_index[event]
            )
            duplicate_projection_exact_every_movement &= (
                primary_projection == duplicate_projection
            )
            flipped = primary_projection ^ previous[event]
            while flipped:
                bit = flipped & -flipped
                changes[event][bit.bit_length() - 1].append(movement)
                flipped ^= bit
            previous[event] = primary_projection
            if movement >= (
                FUNNEL_MOMENTS[event] - CROSS_COHORT_WINDOW_MOVEMENTS
            ):
                primary_state = capture_lane(
                    columns, primary_index[event]
                )
                duplicate_state = capture_lane(
                    columns, duplicate_index[event]
                )
                duplicate_full_window_exact &= (
                    primary_state == duplicate_state
                )
                forward_windows[event][movement] = primary_state
            if movement == FUNNEL_MOMENTS[event]:
                funnels[event] = capture_lane(
                    columns, primary_index[event]
                )
                duplicate_funnels[event] = capture_lane(
                    columns, duplicate_index[event]
                )

    expected_funnels = all(
        state_sha256(funnels[event]) == EXPECTED_FUNNEL_SHA256[event]
        and funnels[event].bit_count() == EXPECTED_FUNNEL_WEIGHTS[event]
        and funnels[event] == duplicate_funnels[event]
        for event in EVENT_ORDER
    )
    return {
        "changes": changes,
        "funnels": funnels,
        "forward_windows": forward_windows,
        "public": {
            "trajectory_keys":
                tuple((event, WITNESS_PAIR) for event in EVENT_ORDER),
            "register_field_count": len(REGISTER_FIELDS),
            "register_fields": REGISTER_FIELDS,
            "register_wire_indices": REGISTER_WIRES,
            "movement_schedule_rows": len(schedule),
            "inclusive_time_bounds":
                tuple((event, 0, FUNNEL_MOMENTS[event])
                      for event in EVENT_ORDER),
            "funnel_rows": tuple({
                "event": event,
                "movement": FUNNEL_MOMENTS[event],
                "state_sha256": state_sha256(funnels[event]),
                "hamming_weight": funnels[event].bit_count(),
            } for event in EVENT_ORDER),
            "duplicate_initial_exact": duplicate_initial_exact,
            "duplicate_projection_exact_every_movement":
                duplicate_projection_exact_every_movement,
            "duplicate_full_window_exact":
                duplicate_full_window_exact,
            "duplicate_funnels_exact": all(
                funnels[event] == duplicate_funnels[event]
                for event in EVENT_ORDER
            ),
            "pass": (
                len(REGISTER_FIELDS) == len(REGISTER_WIRES) == 39
                and len(schedule) == WORD_GATE_COUNT
                and duplicate_initial_exact
                and duplicate_projection_exact_every_movement
                and duplicate_full_window_exact
                and expected_funnels
            ),
        },
    }


def uleb128(value: int) -> bytes:
    if value < 0:
        raise ValueError(value)
    output = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            output.append(byte | 0x80)
        else:
            output.append(byte)
            return bytes(output)


def decode_uleb128(payload: bytes, offset: int) -> tuple[int, int]:
    value = 0
    shift = 0
    while True:
        if offset >= len(payload):
            raise ValueError("truncated ULEB128")
        byte = payload[offset]
        offset += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return value, offset
        shift += 7
        if shift > 63:
            raise ValueError("oversized ULEB128")


def change_time_encoding(
    changes: dict[int, list[list[int]]],
) -> dict[str, object]:
    sequences: list[tuple[int, ...]] = []
    sequence_ids: dict[tuple[int, ...], int] = {}
    field_maps = []
    for event in EVENT_ORDER:
        mappings = []
        for field, times in zip(REGISTER_FIELDS, changes[event]):
            sequence = tuple(times)
            if sequence not in sequence_ids:
                sequence_ids[sequence] = len(sequences)
                sequences.append(sequence)
            mappings.append((field, sequence_ids[sequence]))
        field_maps.append({
            "event": event,
            "trajectory_key": (event, WITNESS_PAIR),
            "field_to_sequence_id": tuple(mappings),
        })

    raw = bytearray()
    sequence_rows = []
    encoded_counts = []
    for sequence_id, sequence in enumerate(sequences):
        previous = 0
        encoded = bytearray()
        for movement in sequence:
            encoded.extend(uleb128(movement - previous))
            previous = movement
        raw.extend(encoded)
        encoded_counts.append((len(sequence), len(encoded)))
        sequence_rows.append({
            "sequence_id": sequence_id,
            "count": len(sequence),
            "first": sequence[0] if sequence else None,
            "last": sequence[-1] if sequence else None,
            "times_sha256": digest(sequence),
            "encoded_bytes": len(encoded),
        })
    compressed = zlib.compress(bytes(raw), level=9)
    decoded_raw = zlib.decompress(compressed)
    decoded_sequences = []
    offset = 0
    for count, _encoded_bytes in encoded_counts:
        previous = 0
        sequence = []
        for _index in range(count):
            delta, offset = decode_uleb128(decoded_raw, offset)
            previous += delta
            sequence.append(previous)
        decoded_sequences.append(tuple(sequence))
    roundtrip_exact = (
        offset == len(decoded_raw)
        and tuple(decoded_sequences) == tuple(sequences)
        and all(
            decoded_sequences[sequence_id]
            == tuple(changes[event][field_index])
            for event_index, event in enumerate(EVENT_ORDER)
            for field_index, (_field, sequence_id) in enumerate(
                field_maps[event_index]["field_to_sequence_id"]
            )
        )
    )
    return {
        "format":
            "Cycle-835 exact encoding: unique sequences in first-occurrence "
            "event/field order; unsigned LEB128 deltas from zero; sequences "
            "concatenated; counts delimit; zlib level 9",
        "field_maps": tuple(field_maps),
        "sequence_rows": tuple(sequence_rows),
        "unique_sequence_count": len(sequences),
        "raw_bytes": len(raw),
        "raw_sha256": sha256(raw).hexdigest(),
        "compressed_bytes": len(compressed),
        "compressed_sha256": sha256(compressed).hexdigest(),
        "roundtrip_exact": roundtrip_exact,
        "matches_cycle835": (
            len(sequences) == EXPECTED_CHANGE_TIME_UNIQUE_SEQUENCES
            and len(raw) == EXPECTED_CHANGE_TIME_RAW_BYTES
            and sha256(raw).hexdigest()
            == EXPECTED_CHANGE_TIME_RAW_SHA256
        ),
    }


def reverse_cohort_windows(
    fixtures: dict[str, object],
    witness: dict[str, object],
    event0: dict[str, object],
) -> dict[str, object]:
    macros = fixtures["macros"]
    assert isinstance(macros, tuple)
    words = compile_words(macros)
    cohort_rows = []
    internal = {}
    all_roundtrips = True
    all_witness_replays = True
    for event in EVENT_ORDER:
        funnel = witness["funnels"][event]
        forward_witness = witness["forward_windows"][event]
        states = (funnel,) * len(BACKBONE)
        depth_states = [states]
        depth_partitions = [partition_of(states)]
        roundtrip = True
        witness_replay = (
            states[0] == forward_witness[FUNNEL_MOMENTS[event]]
        )
        for depth in range(1, CROSS_COHORT_WINDOW_MOVEMENTS + 1):
            predecessor = tuple(
                apply_compiled_word(
                    state, words[pair], reverse=True
                )
                for pair, state in zip(BACKBONE, states)
            )
            roundtrip &= all(
                apply_compiled_word(before, words[pair]) == after
                for pair, before, after in zip(
                    BACKBONE, predecessor, states
                )
            )
            states = predecessor
            depth_states.append(states)
            depth_partitions.append(partition_of(states))
            witness_replay &= (
                states[0]
                == forward_witness[FUNNEL_MOMENTS[event] - depth]
            )
        depth_ticks = tuple(
            (FUNNEL_MOMENTS[event] - depth) * RING_STATIONS
            for depth in range(CROSS_COHORT_WINDOW_MOVEMENTS + 1)
        )
        depth_movements = tuple(
            FUNNEL_MOMENTS[event] - depth
            for depth in range(CROSS_COHORT_WINDOW_MOVEMENTS + 1)
        )
        rle = partition_rle(
            depth_ticks, depth_movements, tuple(depth_partitions)
        )
        forward_states = tuple(reversed(depth_states))
        forward_partitions = tuple(reversed(depth_partitions))
        forward_movements = tuple(reversed(depth_movements))
        event_rows = []
        for index in range(1, len(forward_partitions)):
            if forward_partitions[index] == forward_partitions[index - 1]:
                continue
            event_rows.append(partition_event(
                forward_partitions[index - 1],
                forward_partitions[index],
                forward_states[index - 1],
                forward_states[index],
                from_tick=forward_movements[index - 1] * RING_STATIONS,
                to_tick=forward_movements[index] * RING_STATIONS,
                from_movement=forward_movements[index - 1],
                to_movement=forward_movements[index],
            ))
        total = (tuple(range(len(BACKBONE))),)
        union_depths = tuple(
            depth for depth, partition in enumerate(depth_partitions)
            if partition == total
        )
        pre_union_wires = varying_wire_indices(depth_states[1])
        depth_encoding = partition_sequence_encoding(
            tuple(depth_partitions)
        )
        row = {
            "event": event,
            "funnel_movement": FUNNEL_MOMENTS[event],
            "normalized_depth_bounds":
                (0, CROSS_COHORT_WINDOW_MOVEMENTS),
            "depth_direction":
                "depth 0 is funnel; increasing depth moves backward",
            "exact_depth_partition_sha256":
                digest(tuple(enumerate(depth_partitions))),
            "exact_depth_partition_encoding": depth_encoding,
            "exact_depth_partition_RLE": rle,
            "partition_event_count": len(event_rows),
            "partition_event_kind_counts": tuple(sorted({
                kind: sum(item["kind"] == kind for item in event_rows)
                for kind in ("COARSENING", "REFINEMENT", "MIXED")
            }.items())),
            "partition_events_forward_sha256":
                digest(tuple(event_rows)),
            "total_union_depths": union_depths,
            "pre_union_partition": depth_partitions[1],
            "pre_union_distinct_nodes": len(depth_partitions[1]),
            "pre_union_varying_wire_indices": pre_union_wires,
            "pre_union_varying_wire_count": len(pre_union_wires),
            "reverse_forward_roundtrip_exact": roundtrip,
            "witness_forward_replay_exact": witness_replay,
            "funnel_state_sha256": state_sha256(funnel),
            "pass": (
                sum(item["sample_count"] for item in rle)
                == CROSS_COHORT_WINDOW_MOVEMENTS + 1
                and depth_encoding["roundtrip_exact"]
                and union_depths == (0,)
                and roundtrip
                and witness_replay
            ),
        }
        cohort_rows.append(row)
        internal[event] = {
            "depth_partitions": tuple(depth_partitions),
            "depth_states": tuple(depth_states),
            "forward_event_rows": tuple(event_rows),
        }
        all_roundtrips &= roundtrip
        all_witness_replays &= witness_replay

    event0_forward_match = all(
        internal[0]["depth_partitions"][depth]
        == event0["forward_tail_partitions"][
            FUNNEL_MOMENTS[0] - depth
        ]
        and internal[0]["depth_states"][depth]
        == event0["forward_tail_states"][
            FUNNEL_MOMENTS[0] - depth
        ]
        for depth in range(CROSS_COHORT_WINDOW_MOVEMENTS + 1)
    )
    normalized_partitions_identical = all(
        internal[event]["depth_partitions"]
        == internal[EVENT_ORDER[0]]["depth_partitions"]
        for event in EVENT_ORDER[1:]
    )
    result = {
        "cohort_rows": tuple(cohort_rows),
        "internal": internal,
        "normalized_partitions_identical":
            normalized_partitions_identical,
        "event0_forward_reverse_full_state_exact":
            event0_forward_match,
        "all_reverse_forward_roundtrips_exact": all_roundtrips,
        "all_witness_forward_replays_exact": all_witness_replays,
    }
    result["pass"] = (
        all(row["pass"] for row in cohort_rows)
        and event0_forward_match
        and all_roundtrips
        and all_witness_replays
    )
    return result


def cross_reference_partition_events(
    event0: dict[str, object],
    cohort_windows: dict[str, object],
    changes: dict[int, list[list[int]]],
) -> tuple[dict[str, object], ...]:
    rows = []
    for event in EVENT_ORDER:
        partition_rows = (
            event0["event_rows"] if event == 0
            else cohort_windows["internal"][event]["forward_event_rows"]
        )
        register_union = tuple(sorted({
            movement
            for field_changes in changes[event]
            for movement in field_changes
        }))
        change_sets = tuple(set(times) for times in changes[event])
        for partition_row in partition_rows:
            movement = partition_row["to_movement"]
            same_tick_fields = tuple(
                field
                for field, times in zip(REGISTER_FIELDS, change_sets)
                if movement in times
            )
            same_tick_field_mask = sum(
                1 << field_index
                for field_index, times in enumerate(change_sets)
                if movement in times
            )
            if register_union:
                nearest_distance, nearest_movement = min(
                    (abs(candidate - movement), candidate)
                    for candidate in register_union
                )
                nearest_delta = nearest_movement - movement
            else:
                nearest_movement = None
                nearest_delta = None
                nearest_distance = None
            rows.append({
                "event": event,
                "partition_transition_movement": movement,
                "partition_transition_kind": partition_row["kind"],
                "before_partition": partition_row["before_partition"],
                "after_partition": partition_row["after_partition"],
                "same_tick_register_change":
                    bool(same_tick_fields),
                "same_tick_register_fields": same_tick_fields,
                "same_tick_register_field_count":
                    len(same_tick_fields),
                "same_tick_register_field_mask":
                    same_tick_field_mask,
                "nearest_register_change_movement": nearest_movement,
                "nearest_register_change_delta": nearest_delta,
                "nearest_register_change_distance":
                    nearest_distance,
            })
    return tuple(rows)


def cross_reference_encoding(
    rows: tuple[dict[str, object], ...],
) -> dict[str, object]:
    kind_codes = {"COARSENING": 0, "REFINEMENT": 1, "MIXED": 2}
    raw = bytearray()
    exact_rows = []
    for row in rows:
        delta = row["nearest_register_change_delta"]
        if not isinstance(delta, int) or not -128 <= delta <= 127:
            raise AssertionError("nearest register delta exceeds encoding")
        packed = (
            int(row["event"]),
            int(row["partition_transition_movement"]),
            kind_codes[str(row["partition_transition_kind"])],
            int(row["same_tick_register_field_mask"]),
            delta,
        )
        raw.extend(struct.pack("<BIBQb", *packed))
        exact_rows.append(packed)
    compressed = zlib.compress(bytes(raw), level=9)
    decoded_raw = zlib.decompress(compressed)
    row_size = struct.calcsize("<BIBQb")
    decoded = tuple(
        struct.unpack("<BIBQb", decoded_raw[offset:offset + row_size])
        for offset in range(0, len(decoded_raw), row_size)
    )
    return {
        "format":
            "one <event:u8,movement:u32,kind:u8,register-field-mask:u64,"
            "nearest-delta:i8> row per partition transition; kind "
            "0=coarsening,1=refinement,2=mixed; zlib level 9; Base85",
        "row_count": len(rows),
        "raw_bytes": len(raw),
        "raw_sha256": sha256(raw).hexdigest(),
        "compressed_bytes": len(compressed),
        "compressed_sha256": sha256(compressed).hexdigest(),
        "payload_b85": base64.b85encode(compressed).decode("ascii"),
        "roundtrip_exact": decoded == tuple(exact_rows),
    }


def certificate_a_partition_dynamics(
    event0: dict[str, object],
) -> dict[str, object]:
    public = event0["public"]
    return {
        "certificate_role": "A_PARTITION_DYNAMICS",
        "formal_object":
            "equivalence partition of the nine labeled trajectories under "
            "exact equality of all 5815 state bits",
        "time_convention":
            "meet row at controller tick 3; thereafter one sample at every "
            "complete 11-controller-tick movement boundary through t=14739",
        "compression":
            "exact RLE; each row gives inclusive sample/tick/movement bounds "
            "and its canonical partition, so the full sampled sequence is "
            "reconstructible without omission",
        "event0_full_sequence": public,
        "pass": public["pass"],
    }


def certificate_b_partition_law_hunt(
    event0: dict[str, object],
    witness: dict[str, object],
    encoding: dict[str, object],
    cohort_windows: dict[str, object],
) -> dict[str, object]:
    cross_rows = cross_reference_partition_events(
        event0, cohort_windows, witness["changes"]
    )
    cross_encoding = cross_reference_encoding(cross_rows)
    coarsening_rows = tuple(
        row for row in cross_rows
        if row["partition_transition_kind"] == "COARSENING"
    )
    same_tick_law = (
        bool(coarsening_rows)
        and all(row["same_tick_register_change"]
                for row in coarsening_rows)
    )
    nearest_delta_set = tuple(sorted({
        row["nearest_register_change_delta"]
        for row in coarsening_rows
    }))
    normalized_identical = (
        cohort_windows["normalized_partitions_identical"]
    )
    cohort_rows = cohort_windows["cohort_rows"]
    preunion_partitions = tuple(
        row["pre_union_partition"] for row in cohort_rows
    )
    preunion_node_counts = tuple(
        row["pre_union_distinct_nodes"] for row in cohort_rows
    )
    preunion_wire_counts = tuple(
        row["pre_union_varying_wire_count"] for row in cohort_rows
    )
    union_depth_rows = tuple(
        (row["event"], row["total_union_depths"])
        for row in cohort_rows
    )
    common_preunion_shape = (
        len(set(preunion_partitions)) == 1
        and preunion_node_counts == (3, 3, 3)
        and preunion_wire_counts == (15, 15, 15)
        and all(depths == (0,) for _event, depths in union_depth_rows)
    )
    candidate_a = {
        "candidate":
            "coarsening event times coincide with Cycle-835 register "
            "change-times",
        "coarsening_event_count": len(coarsening_rows),
        "same_tick_count": sum(
            row["same_tick_register_change"] for row in coarsening_rows
        ),
        "nearest_register_change_delta_set": nearest_delta_set,
        "per_event_counts": tuple(
            (
                event,
                sum(row["event"] == event for row in coarsening_rows),
                sum(
                    row["event"] == event
                    and row["same_tick_register_change"]
                    for row in coarsening_rows
                ),
            )
            for event in EVENT_ORDER
        ),
        "cross_reference_encoding": cross_encoding,
        "first_three_rows": coarsening_rows[:3],
        "last_three_rows": coarsening_rows[-3:],
        "holds_exactly": same_tick_law,
        "status":
            "EXACT_SAME_TICK_LAW" if same_tick_law
            else "NO_EXACT_SAME_TICK_LAW",
    }
    candidate_b = {
        "candidate":
            "partition sequence identical across events 0/2/1 after "
            "normalizing movement time to depth from the cohort funnel",
        "bounded_window_movements": CROSS_COHORT_WINDOW_MOVEMENTS,
        "cohort_offsets": tuple(
            (event, FUNNEL_MOMENTS[event]) for event in EVENT_ORDER
        ),
        "cohort_depth_sequence_sha256": tuple(
            (row["event"], row["exact_depth_partition_sha256"])
            for row in cohort_rows
        ),
        "holds_exactly": normalized_identical,
        "status":
            "BOUNDED_COHORT_INVARIANT_BRAID"
            if normalized_identical else "FALSIFIED_ON_BOUNDED_WINDOW",
    }
    candidate_c = {
        "candidate":
            "the pre-union partition has one common three-node shape with "
            "exactly 15 varying wires, followed by the first total union",
        "pre_union_partitions": tuple(
            (row["event"], row["pre_union_partition"])
            for row in cohort_rows
        ),
        "pre_union_distinct_node_counts": tuple(zip(
            EVENT_ORDER, preunion_node_counts
        )),
        "pre_union_varying_wire_counts": tuple(zip(
            EVENT_ORDER, preunion_wire_counts
        )),
        "pre_union_varying_wire_indices": tuple(
            (row["event"], row["pre_union_varying_wire_indices"])
            for row in cohort_rows
        ),
        "total_union_depths": union_depth_rows,
        "event0_no_earlier_total_union_from_meet":
            event0["total_union_sample_indices"]
            == (event0["public"]["sample_count"] - 1,),
        "event0_total_union_sample_count":
            len(event0["total_union_sample_indices"]),
        "event0_first_total_union_movement":
            event0["total_union_movements"][0],
        "event0_last_total_union_before_funnel":
            event0["total_union_movements"][-2]
            if len(event0["total_union_movements"]) > 1 else None,
        "holds_exactly": common_preunion_shape,
        "status":
            "COMMON_3_NODE_15_WIRE_PREUNION"
            if common_preunion_shape else "COMMON_PREUNION_SHAPE_FALSIFIED",
    }
    exact_law_found = (
        candidate_a["holds_exactly"]
        or candidate_b["holds_exactly"]
    )
    return {
        "certificate_role": "B_PARTITION_LEVEL_LAW_HUNT",
        "register_trajectory_replay": witness["public"],
        "cycle835_change_time_encoding": encoding,
        "cross_cohort_windows": tuple(cohort_rows),
        "candidate_a_register_timing": candidate_a,
        "candidate_b_cohort_invariant": candidate_b,
        "candidate_c_partition_local_union": candidate_c,
        "exact_law_found": exact_law_found,
        "pass": (
            witness["public"]["pass"]
            and encoding["roundtrip_exact"]
            and encoding["matches_cycle835"]
            and cohort_windows["pass"]
            and cross_encoding["roundtrip_exact"]
        ),
    }


def certificate_c_verdict(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
) -> dict[str, object]:
    candidate_a = certificate_b["candidate_a_register_timing"]
    candidate_b = certificate_b["candidate_b_cohort_invariant"]
    candidate_c = certificate_b["candidate_c_partition_local_union"]
    law_found = (
        certificate_a["pass"]
        and certificate_b["pass"]
        and certificate_b["exact_law_found"]
    )
    partial = (
        certificate_a["pass"]
        and certificate_b["pass"]
        and (
            candidate_a["holds_exactly"]
            or candidate_b["holds_exactly"]
            or candidate_c["holds_exactly"]
        )
    )
    verdict = (
        "PARTITION_LAW_FOUND"
        if law_found else ("PARTIAL" if partial else "OPEN")
    )
    if candidate_b["holds_exactly"]:
        exact_statement = (
            "For e in (0,2,1), let h_e=(14739,33190,51110) and let "
            "Pi_e(d) be the full-5815-bit equality partition of the nine "
            "labeled backbone trajectories at movement h_e-d.  For every "
            "integer d in [0,64], Pi_0(d)=Pi_2(d)=Pi_1(d).  This is an "
            "exact bounded cohort-invariant partition braid after the "
            "cohort time-offsets h_e are removed."
        )
    elif candidate_a["holds_exactly"]:
        exact_statement = (
            "Every observed coarsening event in the complete event-0 "
            "partition sequence and the bounded event-2/event-1 windows "
            "occurs at an exact Cycle-835 39-field register change-time."
        )
    else:
        exact_statement = None
    return {
        "certificate_role": "C_VERDICT",
        "verdict": verdict,
        "exact_statement": exact_statement,
        "scope_boundary":
            "finite landed nine-trajectory system; event 0 is complete from "
            "the meet at the declared stride, while cross-cohort identity is "
            "proved only on the declared last-64-movement windows",
        "register_timing_disposition":
            candidate_a["status"],
        "cohort_invariant_disposition":
            candidate_b["status"],
        "preunion_disposition":
            candidate_c["status"],
        "does_not_claim":
            "a state-level invariant, an unbounded theorem, or a local pulse "
            "state-selection mechanism beyond the computed partition law",
        "pass": certificate_a["pass"] and certificate_b["pass"],
    }


def fixture_digest(fixtures: dict[str, object]) -> str:
    hasher = sha256()
    for macro in fixtures["macros"]:
        hasher.update(len(macro).to_bytes(2, "little"))
        for gate in macro:
            hasher.update(struct.pack("<BHHH", *gate))
    for key in fixtures["keys"]:
        hasher.update(compact(key).encode("utf-8"))
        hasher.update(
            fixtures["states"][key].to_bytes(STATE_BYTES, "little")
        )
    hasher.update(
        fixtures["target"].to_bytes(STATE_BYTES, "little")
    )
    return hasher.hexdigest()


def certificate_d_controls(
    source: dict[str, object],
    fixtures: dict[str, object],
    fixture_replay: dict[str, object],
    event0: dict[str, object],
    witness: dict[str, object],
    cohort_windows: dict[str, object],
    elapsed: float,
) -> dict[str, object]:
    first_digest = fixture_digest(fixtures)
    replay_digest = fixture_digest(fixture_replay)
    blocked_at_end = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    determinism = {
        "fixture_digest_first": first_digest,
        "fixture_digest_replay": replay_digest,
        "fixture_decode_exact_replay":
            first_digest == replay_digest
            and fixtures["public"] == fixture_replay["public"],
        "event0_duplicate_exact_every_sample":
            event0["public"]["duplicate_exact_every_sample"],
        "register_duplicate_projection_exact_every_movement":
            witness["public"][
                "duplicate_projection_exact_every_movement"
            ],
        "register_duplicate_full_window_exact":
            witness["public"]["duplicate_full_window_exact"],
        "reverse_forward_roundtrips_exact":
            cohort_windows["all_reverse_forward_roundtrips_exact"],
        "witness_forward_replays_exact":
            cohort_windows["all_witness_forward_replays_exact"],
        "event0_forward_reverse_full_state_exact":
            cohort_windows[
                "event0_forward_reverse_full_state_exact"
            ],
    }
    base_pass = (
        source["pass"]
        and all(
            value for key, value in determinism.items()
            if key not in {"fixture_digest_first", "fixture_digest_replay"}
        )
        and not blocked_at_end
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    return {
        "certificate_role": "D_CONTROLS",
        "source_controls": source,
        "primary_access_policy":
            "all AUDIT_INPUT_PATHS source primaries are BLOCKLISTED and "
            "consumed only as text/AST; no source primary is imported or "
            "executed",
        "blocked_modules_loaded_at_end": blocked_at_end,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": determinism,
        "exact_arithmetic":
            "all state updates, partitions, equality, ULEB128, counts, and "
            "digests use exact Python integers/bytes; only wall time is float",
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_seconds": round(elapsed, 6),
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_bytes": 0,
        "stdout_below_limit": False,
        "base_pass_before_stdout": base_pass,
        "pass": False,
    }


def stable_render(
    certificates: dict[str, dict[str, object]],
    report: dict[str, object],
) -> str:
    controls = certificates["D_CONTROLS"]
    previous_size = -1
    for _attempt in range(12):
        output = "\n".join([
            *(f"CERTIFICATE_{name}={compact(value)}"
              for name, value in certificates.items()),
            f"REPORT={compact(report)}",
        ]) + "\n"
        size = len(output.encode("utf-8"))
        controls["stdout_bytes"] = size
        controls["stdout_below_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = (
            controls["base_pass_before_stdout"]
            and controls["stdout_below_limit"]
        )
        report["checks"]["D_CONTROLS"] = controls["pass"]
        report["pass"] = all(report["checks"].values())
        report["terminal"] = (
            "CYCLE845_PARTITION_ROUTE_PASS"
            if report["pass"] else "CYCLE845_PARTITION_ROUTE_HONEST_FAIL"
        )
        report["stdout_bytes"] = size
        if size == previous_size:
            return output
        previous_size = size
    raise AssertionError("stdout accounting did not stabilize")


def run() -> int:
    started = monotonic()
    source, trees = source_controls()
    fixtures = decode_cycle830_fixtures(
        trees[AUDIT_INPUT_PATHS[1]]
    )
    certificate_a_data = event0_full_partition_dynamics(fixtures)
    witness = witness_register_trajectories(fixtures)
    encoding = change_time_encoding(witness["changes"])
    cohort_windows = reverse_cohort_windows(
        fixtures, witness, certificate_a_data
    )
    certificate_a = certificate_a_partition_dynamics(
        certificate_a_data
    )
    certificate_b = certificate_b_partition_law_hunt(
        certificate_a_data, witness, encoding, cohort_windows
    )
    certificate_c = certificate_c_verdict(
        certificate_a, certificate_b
    )
    fixture_replay = decode_cycle830_fixtures(
        trees[AUDIT_INPUT_PATHS[1]]
    )
    elapsed = monotonic() - started
    certificate_d = certificate_d_controls(
        source,
        fixtures,
        fixture_replay,
        certificate_a_data,
        witness,
        cohort_windows,
        elapsed,
    )
    certificates = {
        "A_PARTITION_DYNAMICS": certificate_a,
        "B_PARTITION_LAW_HUNT": certificate_b,
        "C_VERDICT": certificate_c,
        "D_CONTROLS": certificate_d,
    }
    checks = {
        "A_PARTITION_DYNAMICS": certificate_a["pass"],
        "B_PARTITION_LAW_HUNT": certificate_b["pass"],
        "C_VERDICT": certificate_c["pass"],
        "D_CONTROLS": False,
    }
    report = {
        "cycle": 845,
        "title": "the merged why, attempt two — partition refinement",
        "verdict": certificate_c["verdict"],
        "exact_law_statement": certificate_c["exact_statement"],
        "register_timing_disposition":
            certificate_c["register_timing_disposition"],
        "cohort_invariant_disposition":
            certificate_c["cohort_invariant_disposition"],
        "preunion_disposition":
            certificate_c["preunion_disposition"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": checks,
        "pass": False,
        "terminal": "CYCLE845_PARTITION_ROUTE_HONEST_FAIL",
    }
    output = stable_render(certificates, report)
    final_size = len(output.encode("utf-8"))
    if final_size >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 845,
            "pass": False,
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_size,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE845_PARTITION_ROUTE_HONEST_FAIL",
        }))
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        print(compact({
            "cycle": 845,
            "error_type": type(error).__name__,
            "error": str(error),
            "pass": False,
            "terminal": "CYCLE845_PARTITION_ROUTE_HONEST_FAIL",
        }))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
