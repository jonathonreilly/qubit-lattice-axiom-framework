#!/usr/bin/env python3
"""Cycle 846: reduced pair braids and the completed-family delay law.

The runner independently decodes the landed Cycle-830 literal fixture bank
and reimplements the Boolean X/CNOT/Toffoli evolution with Python integers.
Named source primaries are SHA-pinned, import-blocklisted, and consumed only
as text/AST.  Sibling lineage is pinned by commit and git-blob identity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
    "scripts/frontier_cycle841_deciding_the_tick_2026_07_28.py",
)

import ast
import base64
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import lcm
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockP19-20260729"
EXPECTED_BASE = "e71b3b8ae91a72dcaad68f7efacc97874776f834"
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
MEET_CONTROLLER_TICK = 3
NORMALIZED_DEPTH = 64
LCM_SKELETON = lcm(4464, 5952)
EVENT_ORDER = (0, 2, 1)
CHRONOLOGICAL_PAIR_ORDER = (1, 2, 0)
NINE_MOMENTS = {0: 14744, 2: 33195, 1: 51115}
NINE_FUNNEL_MOMENTS = {
    event: moment - 5 for event, moment in NINE_MOMENTS.items()
}
PAIR_MOMENTS = {1: 193210, 2: 246669, 0: 1142432}
PAIR_FUNNEL_MOMENTS = {
    event: moment - 5 for event, moment in PAIR_MOMENTS.items()
}
NINE_WEIGHTS = {0: 44, 2: 45, 1: 46}
PAIR_WEIGHTS = {0: 49, 2: 51, 1: 57}
PULSE_WEIGHT = 59
S0_PRIME_WEIGHT = 47
COHORT_RESIDUALS = (595, 64)
PAIR_POSITIONS = ((0, 5), (0, 6))
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

EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "b14262f6d54dc4f853bda13f321c816b3e762fa37b0b8276a2bec4955c51c481",
    AUDIT_INPUT_PATHS[1]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
    AUDIT_INPUT_PATHS[2]:
        "9879f900590b2a9cdded11d2b691d48adf5c5baff96af4f88b7483bfc98a0b54",
}
EXPECTED_SOURCE_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "1afe4941812f83f5e1fd5cc7c04e57231d703e8d",
    AUDIT_INPUT_PATHS[1]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
    AUDIT_INPUT_PATHS[2]: "379bbe1f4d7ae3432488359fbf3009adfe2a5984",
}
COPIED_LINEAGE_PINS = {
    "cycle830": {
        "commit": "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "path": AUDIT_INPUT_PATHS[0],
        "git_blob": "98b1571228ad0902301b6853208ef249ea2c2973",
    },
    "cycle838": {
        "commit": "7a42ba01f4f549550b1dcfadbefb9aaedce1c0c3",
        "path": "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
        "git_blob": "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    },
    "cycle844": {
        "commit": "d6f32365378db0a714a7111ed69cdee68e86cc6c",
        "path": "scripts/frontier_cycle844_standing_bets_2026_07_28.py",
        "git_blob": "a12245720a7e866134978c25629e19ba57596929",
    },
    "cycle845": {
        "commit": "4f97118a3a5b0831e075d5050d538658abaad115",
        "path": "scripts/frontier_cycle845_partition_route_2026_07_28.py",
        "git_blob": "3c7a6e61bbc656b7c6b69b96be36066d0ad1e8e8",
    },
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_SSTAR_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
Partition = tuple[tuple[int, ...], ...]

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only source primary is imported."""

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
        node.name for node in tree.body
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
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    stdlib_roots = set(sys.stdlib_module_names) | {"__future__"}
    lineage_observed = {
        name: git_text(
            "rev-parse", f"{row['commit']}:{row['path']}"
        )
        for name, row in COPIED_LINEAGE_PINS.items()
    }
    lineage_expected = {
        name: row["git_blob"] for name, row in COPIED_LINEAGE_PINS.items()
    }
    ast_basis = {
        "cycle830": {
            "decode_fixtures", "build_words", "apply_word",
            "partition_keys", "trajectory_and_mechanism_certificates",
        } <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle833": {
            "reconstruct_funnels", "edge_accounting",
            "rank_edge_field_map_certificate", "unification_certificate",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle841": {
            "clock_definitions", "raw_catchup", "accounting_consequence",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
    }
    literal_cross_checks = {
        "cycle833_FUNNEL_MOMENTS":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[1]], "FUNNEL_MOMENTS"
            ) == NINE_FUNNEL_MOMENTS,
        "cycle841_LCM_SKELETON":
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "COHORT_RESIDUALS"
            ) == COHORT_RESIDUALS,
    }
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    branch = git_text("branch", "--show-current")
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", EXPECTED_BASE, "HEAD"),
        cwd=ROOT,
        check=False,
        timeout=20,
    ).returncode == 0
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
        "maximum_named_files": 8,
        "source_sha256": source_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "source_git_blobs": source_blobs,
        "expected_source_git_blobs": EXPECTED_SOURCE_GIT_BLOBS,
        "copied_lineage_pins": COPIED_LINEAGE_PINS,
        "copied_lineage_observed_git_blobs": lineage_observed,
        "copied_lineage_expected_git_blobs": lineage_expected,
        "AST_basis": ast_basis,
        "literal_cross_checks": literal_cross_checks,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_start": blocked_loaded,
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= stdlib_roots,
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob(self_payload),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 8
        and source_sha == EXPECTED_SOURCE_SHA256
        and source_blobs == EXPECTED_SOURCE_GIT_BLOBS
        and lineage_observed == lineage_expected
        and all(ast_basis.values())
        and all(literal_cross_checks.values())
        and not blocked_loaded
        and not FIREWALL.hits
        and result["stdlib_only"]
        and branch == EXPECTED_BRANCH
        and base_is_ancestor
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
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def decode_cycle830_fixtures(tree: ast.Module) -> dict[str, object]:
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
        (event, pair) for event in range(4) for pair in pairs
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
        "target_raw_sha256": sha256(target_raw).hexdigest(),
    }
    public["pass"] = (
        len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and len(target_raw) == STATE_BYTES
        and public["target_raw_sha256"] == EXPECTED_SSTAR_PACKED_SHA256
        and len(pairs) == 44
        and len(states) == FAMILY_SIZE
        and target.bit_count() == NINE_WEIGHTS[0]
    )
    return {
        "macros": tuple(macros),
        "keys": keys,
        "states": states,
        "target": target,
        "public": public,
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
    hasher.update(fixtures["target"].to_bytes(STATE_BYTES, "little"))
    return hasher.hexdigest()


def bit_slice(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        value = state
        while value:
            bit = value & -value
            columns[bit.bit_length() - 1] |= 1 << lane
            value ^= bit
    return columns


def capture_lane(columns: list[int], lane: int) -> int:
    return sum(
        1 << wire
        for wire, column in enumerate(columns)
        if (column >> lane) & 1
    )


def capture_lanes(
    columns: list[int], lane_count: int
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
    phases: tuple[tuple[MaskedGate, ...], ...]
) -> tuple[MaskedGate, ...]:
    return tuple(row for phase in phases for row in phase)


def advance(
    columns: list[int], schedule: tuple[MaskedGate, ...]
) -> None:
    for kind, first, second, third, lane_mask in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )


def lane_equal(columns: list[int], left: int, right: int) -> bool:
    for column in columns:
        if ((column >> left) ^ (column >> right)) & 1:
            return False
    return True


def partition_of(states: tuple[int, ...]) -> Partition:
    groups: dict[int, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(sorted(
        (tuple(group) for group in groups.values()),
        key=lambda group: group[0],
    ))


def status_name(united: bool) -> str:
    return "UNITED" if united else "SEPARATE"


def relation(
    name: str,
    candidate: str,
    actual: object,
    expected: object,
    holds: bool,
) -> dict[str, object]:
    return {
        "name": name,
        "candidate": candidate,
        "actual": actual,
        "expected": expected,
        "holds_exactly": holds,
        "status": "HOLDS" if holds else "FAILS",
    }


def new_braid_tracker(event: int, united: bool) -> dict[str, object]:
    hasher = sha256()
    hasher.update(bytes((int(united),)))
    return {
        "event": event,
        "current": united,
        "start_sample": 0,
        "start_movement": None,
        "previous_movement": None,
        "sample_count": 1,
        "hasher": hasher,
        "rows": [],
    }


def update_braid_tracker(
    tracker: dict[str, object], movement: int, united: bool
) -> None:
    if united != tracker["current"]:
        tracker["rows"].append({
            "sample_index_start": tracker["start_sample"],
            "sample_index_end": tracker["sample_count"] - 1,
            "sample_count":
                tracker["sample_count"] - tracker["start_sample"],
            "movement_start": tracker["start_movement"],
            "movement_end": tracker["previous_movement"],
            "partition": status_name(bool(tracker["current"])),
        })
        tracker["current"] = united
        tracker["start_sample"] = tracker["sample_count"]
        tracker["start_movement"] = movement
    tracker["previous_movement"] = movement
    tracker["sample_count"] += 1
    tracker["hasher"].update(bytes((int(united),)))


def finish_braid_tracker(
    tracker: dict[str, object]
) -> dict[str, object]:
    tracker["rows"].append({
        "sample_index_start": tracker["start_sample"],
        "sample_index_end": tracker["sample_count"] - 1,
        "sample_count": tracker["sample_count"] - tracker["start_sample"],
        "movement_start": tracker["start_movement"],
        "movement_end": tracker["previous_movement"],
        "partition": status_name(bool(tracker["current"])),
    })
    rows = tuple(tracker["rows"])
    return {
        "event": tracker["event"],
        "sample_grid":
            "meet sample at controller tick 3, then each complete movement",
        "sample_count": tracker["sample_count"],
        "binary_encoding": "00=SEPARATE, 01=UNITED, one byte per sample",
        "exact_sequence_sha256": tracker["hasher"].hexdigest(),
        "RLE": rows,
        "RLE_row_count": len(rows),
        "RLE_reconstructs_exact_sample_count":
            sum(row["sample_count"] for row in rows)
            == tracker["sample_count"],
        "topological_RLE_shape": tuple(row["partition"] for row in rows),
    }


PAIR_DIFF_TABLE = tuple(
    sum(
        (((value >> left) ^ (value >> right)) & 1) << pair_index
        for pair_index, (left, right) in enumerate(((0, 1), (2, 3), (4, 5)))
    )
    for value in range(1 << 12)
)


def pair_difference_mask(columns: list[int]) -> int:
    different = 0
    lookup = PAIR_DIFF_TABLE
    for column in columns:
        different |= lookup[column]
        if different == 0b111:
            break
    return different


def pair_braids(fixtures: dict[str, object]) -> dict[str, object]:
    macros = fixtures["macros"]
    states_by_key = fixtures["states"]
    primary_keys = tuple(
        (event, pair)
        for event in CHRONOLOGICAL_PAIR_ORDER
        for pair in PAIR_POSITIONS
    )
    primary_states = tuple(states_by_key[key] for key in primary_keys)
    lane_pairs = tuple(key[1] for key in primary_keys) * 2
    initial_states = primary_states + primary_states
    phases = build_phase_schedules(macros, lane_pairs)
    schedule = movement_schedule(phases)
    columns = bit_slice(initial_states)
    meet_columns = columns.copy()
    for phase in range(MEET_CONTROLLER_TICK):
        advance(meet_columns, phases[phase])
    meet_different = pair_difference_mask(meet_columns)
    trackers = {
        event: new_braid_tracker(
            event, not bool(meet_different & (1 << index))
        )
        for index, event in enumerate(CHRONOLOGICAL_PAIR_ORDER)
    }
    tails: dict[int, list[bool]] = {
        event: [] for event in CHRONOLOGICAL_PAIR_ORDER
    }
    funnel_rows = {}
    captured_funnel_states = {}
    maximum = max(PAIR_FUNNEL_MOMENTS.values())
    for movement in range(1, maximum + 1):
        advance(columns, schedule)
        different = pair_difference_mask(columns)
        for index, event in enumerate(CHRONOLOGICAL_PAIR_ORDER):
            funnel = PAIR_FUNNEL_MOMENTS[event]
            if movement > funnel:
                continue
            united = not bool(different & (1 << index))
            update_braid_tracker(trackers[event], movement, united)
            if movement >= funnel - NORMALIZED_DEPTH:
                tails[event].append(united)
            if movement == funnel:
                left_lane = 2 * index
                right_lane = left_lane + 1
                left = capture_lane(columns, left_lane)
                right = capture_lane(columns, right_lane)
                captured_funnel_states[event] = left
                funnel_rows[event] = {
                    "event": event,
                    "resolution_moment": PAIR_MOMENTS[event],
                    "funnel_movement": funnel,
                    "moment_minus_five_exact":
                        PAIR_MOMENTS[event] - funnel == 5,
                    "two_keys": tuple(
                        key for key in primary_keys if key[0] == event
                    ),
                    "full_state_equal": left == right,
                    "state_sha256": state_sha256(left),
                    "packed_sha256": packed_sha256(left),
                    "weight": left.bit_count(),
                    "expected_weight": PAIR_WEIGHTS[event],
                    "weight_exact": left.bit_count() == PAIR_WEIGHTS[event],
                    "determinism_duplicates_equal": all(
                        lane_equal(columns, lane, lane + len(primary_keys))
                        for lane in (left_lane, right_lane)
                    ),
                }
                funnel_rows[event]["pass"] = all((
                    funnel_rows[event]["moment_minus_five_exact"],
                    funnel_rows[event]["full_state_equal"],
                    funnel_rows[event]["weight_exact"],
                    funnel_rows[event]["determinism_duplicates_equal"],
                ))
    full_braids = {
        event: finish_braid_tracker(trackers[event])
        for event in CHRONOLOGICAL_PAIR_ORDER
    }
    normalized = {
        event: tuple(reversed(tails[event]))
        for event in CHRONOLOGICAL_PAIR_ORDER
    }
    normalized_rows = tuple({
        "event": event,
        "depth_bounds": (0, NORMALIZED_DEPTH),
        "partition_by_depth": tuple(map(status_name, normalized[event])),
        "exact_depth_sequence_sha256":
            sha256(bytes(map(int, normalized[event]))).hexdigest(),
    } for event in CHRONOLOGICAL_PAIR_ORDER)
    normalized_identical = all(
        normalized[event] == normalized[CHRONOLOGICAL_PAIR_ORDER[0]]
        for event in CHRONOLOGICAL_PAIR_ORDER[1:]
    )
    topological_shapes = tuple(
        full_braids[event]["topological_RLE_shape"]
        for event in CHRONOLOGICAL_PAIR_ORDER
    )
    duplicate_end = all(
        lane_equal(columns, lane, lane + len(primary_keys))
        for lane in range(len(primary_keys))
    )
    result = {
        "primary_keys": primary_keys,
        "meeting_controller_tick": MEET_CONTROLLER_TICK,
        "meet_partitions": tuple(
            (event, status_name(not bool(meet_different & (1 << index))))
            for index, event in enumerate(CHRONOLOGICAL_PAIR_ORDER)
        ),
        "movement_schedule_rows": len(schedule),
        "full_meet_to_funnel_braids": tuple(
            full_braids[event] for event in CHRONOLOGICAL_PAIR_ORDER
        ),
        "funnel_rows": tuple(
            funnel_rows[event] for event in CHRONOLOGICAL_PAIR_ORDER
        ),
        "normalized_depth_rows": normalized_rows,
        "normalized": normalized,
        "full_byte_streams_identical":
            len({
                (
                    full_braids[event]["sample_count"],
                    full_braids[event]["exact_sequence_sha256"],
                )
                for event in CHRONOLOGICAL_PAIR_ORDER
            }) == 1,
        "topological_RLE_shapes_identical":
            len(set(topological_shapes)) == 1,
        "normalized_depth_0_64_identical": normalized_identical,
        "reduced_partition_law":
            "HOLDS" if normalized_identical else "FAILS",
        "duplicate_initial_exact":
            initial_states[:len(primary_keys)]
            == initial_states[len(primary_keys):],
        "duplicate_schedule_masks_exact": all(
            ((mask >> lane) & 1)
            == ((mask >> (lane + len(primary_keys))) & 1)
            for _kind, _first, _second, _third, mask in schedule
            for lane in range(len(primary_keys))
        ),
        "duplicate_end_exact": duplicate_end,
        "internal_funnel_states": captured_funnel_states,
    }
    result["pass"] = (
        fixtures["public"]["pass"]
        and len(schedule) > WORD_GATE_COUNT
        and all(row["pass"] for row in funnel_rows.values())
        and all(
            full_braids[event]["RLE_reconstructs_exact_sample_count"]
            and full_braids[event]["sample_count"]
            == PAIR_FUNNEL_MOMENTS[event] + 1
            for event in CHRONOLOGICAL_PAIR_ORDER
        )
        and all(len(tails[event]) == NORMALIZED_DEPTH + 1
                for event in CHRONOLOGICAL_PAIR_ORDER)
        and result["duplicate_initial_exact"]
        and result["duplicate_schedule_masks_exact"]
        and duplicate_end
    )
    return result


def nine_tail(fixtures: dict[str, object]) -> dict[str, object]:
    macros = fixtures["macros"]
    states_by_key = fixtures["states"]
    initial = tuple(states_by_key[(0, pair)] for pair in BACKBONE)
    phases = build_phase_schedules(macros, BACKBONE)
    schedule = movement_schedule(phases)
    columns = bit_slice(initial)
    meet_columns = columns.copy()
    for phase in range(MEET_CONTROLLER_TICK):
        advance(meet_columns, phases[phase])
    meet_partition = partition_of(capture_lanes(meet_columns, len(BACKBONE)))
    tail_states = []
    funnel = NINE_FUNNEL_MOMENTS[0]
    for movement in range(1, funnel + 1):
        advance(columns, schedule)
        if movement >= funnel - NORMALIZED_DEPTH:
            tail_states.append(capture_lanes(columns, len(BACKBONE)))
    normalized_states = tuple(reversed(tail_states))
    normalized_partitions = tuple(map(partition_of, normalized_states))
    terminal = normalized_states[0]
    return {
        "meeting_controller_tick": MEET_CONTROLLER_TICK,
        "meet_partition": meet_partition,
        "funnel_movement": funnel,
        "movement_schedule_rows": len(schedule),
        "normalized_depth_bounds": (0, NORMALIZED_DEPTH),
        "normalized_partitions": normalized_partitions,
        "normalized_partition_sha256": digest(normalized_partitions),
        "internal_normalized_states": normalized_states,
        "terminal_all_nine_equal": len(set(terminal)) == 1,
        "terminal_weight": terminal[0].bit_count(),
        "terminal_state_sha256": state_sha256(terminal[0]),
        "terminal_matches_fixture_target":
            all(state == fixtures["target"] for state in terminal),
        "pass": (
            len(normalized_states) == NORMALIZED_DEPTH + 1
            and len(set(terminal)) == 1
            and terminal[0].bit_count() == NINE_WEIGHTS[0]
            and all(state == fixtures["target"] for state in terminal)
        ),
    }


def certificate_a_reduced_braids(
    pairs: dict[str, object], nine: dict[str, object]
) -> dict[str, object]:
    common = pairs["normalized"][CHRONOLOGICAL_PAIR_ORDER[0]]
    nine_states = nine["internal_normalized_states"]
    restriction_rows = []
    for left, right in combinations(range(len(BACKBONE)), 2):
        restriction = tuple(
            states[left] == states[right] for states in nine_states
        )
        holds = restriction == common
        restriction_rows.append({
            "nine_lane_subset": (left, right),
            "nine_key_subset": (BACKBONE[left], BACKBONE[right]),
            "restricted_depth_sequence_sha256":
                sha256(bytes(map(int, restriction))).hexdigest(),
            "reproduces_pair_braid": holds,
            "status": "HOLDS" if holds else "FAILS",
        })
    matching = tuple(
        row["nine_key_subset"] for row in restriction_rows
        if row["reproduces_pair_braid"]
    )
    reduction_holds = bool(matching)
    public_pairs = {
        key: value for key, value in pairs.items()
        if key not in {"normalized", "internal_funnel_states"}
    }
    public_nine = {
        key: value for key, value in nine.items()
        if key != "internal_normalized_states"
    }
    return {
        "certificate_role": "A_REDUCED_BRAIDS",
        "normalization":
            "Cycle-845 convention: depth 0 is the cohort funnel and depth "
            "increases backward, here exhaustively through depth 64",
        "pair_computation": public_pairs,
        "nine_event0_replay": public_nine,
        "pair_braid_identity_tests": (
            relation(
                "full_byte_stream_identity",
                "unequal-duration full meet-to-funnel byte streams match",
                pairs["full_byte_streams_identical"], True,
                pairs["full_byte_streams_identical"],
            ),
            relation(
                "topological_RLE_shape_identity",
                "full braid RLE partition shapes match after time labels are removed",
                pairs["topological_RLE_shapes_identical"], True,
                pairs["topological_RLE_shapes_identical"],
            ),
            relation(
                "normalized_depth_0_64_identity",
                "three pair braids are identical on the landed Cycle-845 depth window",
                pairs["normalized_depth_0_64_identical"], True,
                pairs["normalized_depth_0_64_identical"],
            ),
        ),
        "reduction_candidate":
            "restrict the normalized nine-braid to each labeled two-subset "
            "and ask whether any exact binary sequence equals the common "
            "normalized pair-braid",
        "restriction_rows_every_subset": tuple(restriction_rows),
        "matching_nine_key_subsets": matching,
        "matching_subset_count": len(matching),
        "lawful_reduction_holds": reduction_holds,
        "lawful_reduction_status": "HOLDS" if reduction_holds else "FAILS",
        "reduced_partition_law_status": pairs["reduced_partition_law"],
        "scope_boundary":
            "full pair braids are computed and RLE-printed; IDENTICAL and "
            "REDUCTION use the same landed normalized depth-0..64 window "
            "as Cycle 845, not unequal-length raw streams",
        "pass": pairs["pass"] and nine["pass"] and len(restriction_rows) == 36,
    }


def fraction_row(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "exact": f"{value.numerator}/{value.denominator}",
    }


def certificate_b_delay_law() -> dict[str, object]:
    per_event = []
    for event in EVENT_ORDER:
        ratio = Fraction(PAIR_MOMENTS[event], NINE_MOMENTS[event])
        difference = PAIR_MOMENTS[event] - NINE_MOMENTS[event]
        per_event.append({
            "event": event,
            "nine_moment": NINE_MOMENTS[event],
            "origin_pair_moment": PAIR_MOMENTS[event],
            "origin_delay_difference": difference,
            "origin_delay_ratio": fraction_row(ratio),
            "integer_ratio": ratio.denominator == 1,
            "integer_ratio_status":
                "HOLDS" if ratio.denominator == 1 else "FAILS",
        })
    gaps = []
    transitions = tuple(zip(
        CHRONOLOGICAL_PAIR_ORDER,
        CHRONOLOGICAL_PAIR_ORDER[1:],
    ))
    for index, (source, target) in enumerate(transitions):
        gap = PAIR_MOMENTS[target] - PAIR_MOMENTS[source]
        quotient, residual = divmod(gap, LCM_SKELETON)
        nearest_multiple = quotient + int(2 * residual >= LCM_SKELETON)
        signed_nearest_residual = gap - nearest_multiple * LCM_SKELETON
        fixed_hits = tuple(
            candidate for candidate in COHORT_RESIDUALS
            if (gap - candidate) % LCM_SKELETON == 0
        )
        gaps.append({
            "chronological_transition": (source, target),
            "gap": gap,
            "floor_lcm_multiple": quotient,
            "euclidean_residual": residual,
            "exact_euclidean_decomposition":
                gap == quotient * LCM_SKELETON + residual,
            "exact_euclidean_status": "HOLDS",
            "nearest_lcm_multiple": nearest_multiple,
            "signed_nearest_residual": signed_nearest_residual,
            "landed_nine_residual_target": COHORT_RESIDUALS[index],
            "fixed_residual_hits": fixed_hits,
            "decomposes_with_any_landed_nine_residual": bool(fixed_hits),
            "landed_residual_status": "HOLDS" if fixed_hits else "FAILS",
        })
    clock_rows = []
    for clock, shift in (("MOMENT", 0), ("MOMENT_MINUS_FIVE", -5)):
        times = {
            event: PAIR_MOMENTS[event] + shift
            for event in CHRONOLOGICAL_PAIR_ORDER
        }
        raw = tuple(
            times[target] - times[source] - LCM_SKELETON
            for source, target in transitions
        )
        equations = tuple(
            times[target] - times[source]
            == LCM_SKELETON + catchup
            for (source, target), catchup in zip(transitions, raw)
        )
        clock_rows.append({
            "clock": clock,
            "times_chronological_event_1_2_0": tuple(
                times[event] for event in CHRONOLOGICAL_PAIR_ORDER
            ),
            "formula": "catchup(s,t)=t_target-t_source-lcm(4464,5952)",
            "one_lcm_raw_catchup": raw,
            "gap_equals_one_lcm_plus_catchup": equations,
            "accounting_identity_holds": all(equations),
            "accounting_identity_status":
                "HOLDS" if all(equations) else "FAILS",
            "equals_landed_nine_catchup_595_64": raw == COHORT_RESIDUALS,
            "landed_value_law_status":
                "HOLDS" if raw == COHORT_RESIDUALS else "FAILS",
        })
    differences = tuple(row["origin_delay_difference"] for row in per_event)
    ratios = tuple(
        (row["origin_delay_ratio"]["numerator"],
         row["origin_delay_ratio"]["denominator"])
        for row in per_event
    )
    exact_relations = (
        relation(
            "common_origin_delay_difference",
            "pair moment minus nine moment is event-independent",
            differences, (differences[0],) * 3,
            len(set(differences)) == 1,
        ),
        relation(
            "common_origin_delay_ratio",
            "pair moment divided by nine moment is event-independent",
            ratios, (ratios[0],) * 3,
            len(set(ratios)) == 1,
        ),
        relation(
            "pair_gaps_use_landed_residuals",
            "each chronological pair gap is n*17856 plus 595 then 64",
            tuple((row["gap"], row["fixed_residual_hits"]) for row in gaps),
            COHORT_RESIDUALS,
            all(row["decomposes_with_any_landed_nine_residual"] for row in gaps),
        ),
        relation(
            "physics_clock_accounting_identity",
            "Cycle-841 gap=lcm+raw-catchup identity holds on both physics clocks",
            tuple(row["accounting_identity_holds"] for row in clock_rows),
            (True, True),
            all(row["accounting_identity_holds"] for row in clock_rows),
        ),
        relation(
            "physics_clock_catchup_value_law",
            "pair-cohort raw catch-up repeats the landed nine 595,64 values",
            tuple(row["one_lcm_raw_catchup"] for row in clock_rows),
            (COHORT_RESIDUALS, COHORT_RESIDUALS),
            all(row["equals_landed_nine_catchup_595_64"] for row in clock_rows),
        ),
    )
    return {
        "certificate_role": "B_DELAY_LAW_CENSUS",
        "nine_moments_by_event": NINE_MOMENTS,
        "origin_pair_moments_by_event": PAIR_MOMENTS,
        "per_event_origin_delay_rows": tuple(per_event),
        "lcm_skeleton": LCM_SKELETON,
        "chronological_pair_order": CHRONOLOGICAL_PAIR_ORDER,
        "pair_gap_lcm_rows": tuple(gaps),
        "physics_clock_rows": tuple(clock_rows),
        "register_entry_disposition_from_cycle841":
            "not applied: REGISTER_FINAL_ENTRY has zero landed PHYSICS "
            "consumers; the applicable physics clocks are MOMENT and "
            "MOMENT_MINUS_FIVE",
        "exact_relation_tests": exact_relations,
        "pass": (
            all(row["exact_euclidean_decomposition"] for row in gaps)
            and all(row["accounting_identity_holds"] for row in clock_rows)
            and len(per_event) == 3
        ),
    }


def support_indices(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def register_accounting_rows(
    funnel_states: dict[int, int]
) -> tuple[dict[str, object], ...]:
    rows = []
    register_set = frozenset(REGISTER_WIRES)
    for source, target in ((0, 2), (2, 1), (0, 1)):
        left = funnel_states[source]
        right = funnel_states[target]
        support = support_indices(left ^ right)
        flipped_on = (right & ~left).bit_count()
        flipped_off = (left & ~right).bit_count()
        accounting = (
            left.bit_count() + flipped_on - flipped_off
            == right.bit_count()
        )
        outside_register = tuple(sorted(set(support) - register_set))
        localized = not outside_register
        outside_is_three = len(outside_register) == 3
        rows.append({
            "event_edge": (source, target),
            "source_weight": left.bit_count(),
            "target_weight": right.bit_count(),
            "xor_support_weight": len(support),
            "xor_support_sha256": digest(support),
            "xor_support_first_12": support[:12],
            "xor_support_last_12": support[-12:],
            "flipped_on": flipped_on,
            "flipped_off": flipped_off,
            "net_weight_increment": flipped_on - flipped_off,
            "weight_accounting_exact": accounting,
            "weight_accounting_status": "HOLDS" if accounting else "FAILS",
            "total_xor_is_exactly_three_wire": len(support) == 3,
            "total_three_wire_status":
                "HOLDS" if len(support) == 3 else "FAILS",
            "localized_to_landed_39_register_wires": localized,
            "register_localization_status":
                "HOLDS" if localized else "FAILS",
            "register_support_hit_count":
                len(set(support) & register_set),
            "outside_register_support": outside_register,
            "outside_register_support_count": len(outside_register),
            "outside_register_is_exactly_three_wire": outside_is_three,
            "outside_register_three_wire_status":
                "HOLDS" if outside_is_three else "FAILS",
            "register_plus_at_most_three_wire_extension":
                len(outside_register) <= 3,
            "register_plus_at_most_three_status":
                "HOLDS" if len(outside_register) <= 3 else "FAILS",
        })
    return tuple(rows)


def certificate_c_weight_law(
    funnel_states: dict[int, int]
) -> dict[str, object]:
    nine = tuple(NINE_WEIGHTS[event] for event in EVENT_ORDER)
    pair_reverse = tuple(PAIR_WEIGHTS[event] for event in EVENT_ORDER)
    pair_chrono = tuple(
        PAIR_WEIGHTS[event] for event in CHRONOLOGICAL_PAIR_ORDER
    )
    gallery = tuple(sorted((
        *NINE_WEIGHTS.values(), *PAIR_WEIGHTS.values(),
        PULSE_WEIGHT, S0_PRIME_WEIGHT,
    )))
    register_rows = register_accounting_rows(funnel_states)
    outside_register_by_edge = tuple(
        row["outside_register_support"] for row in register_rows
    )
    three_wire_register_expected = ((), (88, 124, 125), (88, 124, 125))
    tests = (
        relation(
            "nine_arrival_rank_linear_law",
            "w9(r)=44+r for arrival ranks r=0,1,2 (events 0,2,1)",
            nine, tuple(44 + rank for rank in range(3)),
            nine == tuple(44 + rank for rank in range(3)),
        ),
        relation(
            "pair_reverse_arrival_rank_quadratic_law",
            "wp(q)=49+2*q^2 for reverse-arrival ranks q=0,1,2 (events 0,2,1)",
            pair_reverse, tuple(49 + 2 * rank * rank for rank in range(3)),
            pair_reverse == tuple(49 + 2 * rank * rank for rank in range(3)),
        ),
        relation(
            "pair_chronological_rank_reverse_quadratic_law",
            "wp(r)=49+2*(2-r)^2 for chronological ranks r=0,1,2 (events 1,2,0)",
            pair_chrono,
            tuple(49 + 2 * (2 - rank) ** 2 for rank in range(3)),
            pair_chrono
            == tuple(49 + 2 * (2 - rank) ** 2 for rank in range(3)),
        ),
        relation(
            "pair_unit_step_rank_law",
            "pair weights rise by one in declared event order 0,2,1",
            pair_reverse, tuple(pair_reverse[0] + rank for rank in range(3)),
            pair_reverse == tuple(pair_reverse[0] + rank for rank in range(3)),
        ),
        relation(
            "nine_plus_S0_prime_consecutive_quartet",
            "nine funnels followed by S0' are 44,45,46,47",
            (*nine, S0_PRIME_WEIGHT), (44, 45, 46, 47),
            (*nine, S0_PRIME_WEIGHT) == (44, 45, 46, 47),
        ),
        relation(
            "pair_plus_pulse_reflection_sum",
            "49+59 equals 51+57",
            PAIR_WEIGHTS[0] + PULSE_WEIGHT,
            PAIR_WEIGHTS[2] + PAIR_WEIGHTS[1],
            PAIR_WEIGHTS[0] + PULSE_WEIGHT
            == PAIR_WEIGHTS[2] + PAIR_WEIGHTS[1],
        ),
        relation(
            "pair_plus_pulse_symmetric_offsets",
            "49,51,57,59 are centered at 54 with offsets -5,-3,3,5",
            tuple(weight - 54 for weight in (
                PAIR_WEIGHTS[0], PAIR_WEIGHTS[2],
                PAIR_WEIGHTS[1], PULSE_WEIGHT,
            )),
            (-5, -3, 3, 5),
            tuple(weight - 54 for weight in (
                PAIR_WEIGHTS[0], PAIR_WEIGHTS[2],
                PAIR_WEIGHTS[1], PULSE_WEIGHT,
            )) == (-5, -3, 3, 5),
        ),
        relation(
            "pair_minus_nine_cross_family_rank_law",
            "wp(r)-w9(r)=5-r+2*r^2 in event order 0,2,1",
            tuple(pair - base for pair, base in zip(pair_reverse, nine)),
            tuple(5 - rank + 2 * rank * rank for rank in range(3)),
            tuple(pair - base for pair, base in zip(pair_reverse, nine))
            == tuple(5 - rank + 2 * rank * rank for rank in range(3)),
        ),
        relation(
            "completed_gallery_strictly_increasing",
            "sorted gallery has no repeated weight",
            gallery, tuple(sorted(set(gallery))),
            len(gallery) == len(set(gallery)),
        ),
        relation(
            "pair_three_wire_register_extension_law",
            "edge 0->2 is register-only; edges 2->1 and 0->1 add the same exact three wires",
            outside_register_by_edge,
            three_wire_register_expected,
            outside_register_by_edge == three_wire_register_expected,
        ),
    )
    actual_weights = {
        event: funnel_states[event].bit_count() for event in EVENT_ORDER
    }
    support_union = set()
    for source, target in ((0, 2), (2, 1), (0, 1)):
        support_union.update(support_indices(
            funnel_states[source] ^ funnel_states[target]
        ))
    return {
        "certificate_role": "C_WEIGHT_LAW_CENSUS",
        "nine_gallery_event_order_0_2_1": nine,
        "pair_gallery_event_order_0_2_1": pair_reverse,
        "pair_moments_same_event_order_0_2_1": tuple(
            PAIR_MOMENTS[event] for event in EVENT_ORDER
        ),
        "pair_chronological_event_order_1_2_0": pair_chrono,
        "pulse_weight": PULSE_WEIGHT,
        "S0_prime_weight": S0_PRIME_WEIGHT,
        "completed_sorted_gallery": gallery,
        "exact_relation_tests": tests,
        "computed_pair_funnel_weights": actual_weights,
        "expected_pair_funnel_weights": PAIR_WEIGHTS,
        "pair_funnel_weights_exact": actual_weights == PAIR_WEIGHTS,
        "three_wire_and_register_accounting_every_edge": register_rows,
        "three_funnel_varying_wire_union_count": len(support_union),
        "three_funnel_varying_wire_union_sha256":
            digest(tuple(sorted(support_union))),
        "pass": (
            actual_weights == PAIR_WEIGHTS
            and all(row["weight_accounting_exact"] for row in register_rows)
            and len(tests) == 10
        ),
    }


def certificate_d_controls(
    source: dict[str, object],
    fixtures: dict[str, object],
    fixture_replay: dict[str, object],
    pairs: dict[str, object],
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
        "pair_duplicate_initial_exact": pairs["duplicate_initial_exact"],
        "pair_duplicate_schedule_masks_exact":
            pairs["duplicate_schedule_masks_exact"],
        "pair_duplicate_end_exact": pairs["duplicate_end_exact"],
        "pair_funnel_duplicate_exact": all(
            row["determinism_duplicates_equal"]
            for row in pairs["funnel_rows"]
        ),
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
            "every literal AUDIT_INPUT_PATHS primary is BLOCKLISTED and "
            "consumed only as text/AST; no source primary is imported or executed",
        "blocked_modules_loaded_at_end": blocked_at_end,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": determinism,
        "exact_arithmetic":
            "Boolean evolution, partitions, ratios, differences, lcm "
            "decompositions, weights, register accounting, and hashes are "
            "exact; wall time alone is floating point",
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
            "CYCLE846_REDUCED_BRAIDS_DELAY_LAW_EXACT_PASS"
            if report["pass"]
            else "CYCLE846_REDUCED_BRAIDS_DELAY_LAW_HONEST_FAIL"
        )
        report["stdout_bytes"] = size
        if size == previous_size:
            return output
        previous_size = size
    raise AssertionError("stdout accounting did not stabilize")


def run() -> int:
    started = monotonic()
    source, trees = source_controls()
    fixtures = decode_cycle830_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    pair_data = pair_braids(fixtures)
    funnel_states = pair_data["internal_funnel_states"]
    nine_data = nine_tail(fixtures)
    certificate_a = certificate_a_reduced_braids(pair_data, nine_data)
    certificate_b = certificate_b_delay_law()
    certificate_c = certificate_c_weight_law(funnel_states)
    fixture_replay = decode_cycle830_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    elapsed = monotonic() - started
    certificate_d = certificate_d_controls(
        source, fixtures, fixture_replay, pair_data, elapsed
    )
    certificates = {
        "A_REDUCED_BRAIDS": certificate_a,
        "B_DELAY_LAW": certificate_b,
        "C_WEIGHT_LAW": certificate_c,
        "D_CONTROLS": certificate_d,
    }
    checks = {
        "A_REDUCED_BRAIDS": certificate_a["pass"],
        "B_DELAY_LAW": certificate_b["pass"],
        "C_WEIGHT_LAW": certificate_c["pass"],
        "D_CONTROLS": False,
    }
    report = {
        "cycle": 846,
        "title": "the reduced braids and the delay law",
        "pair_reduced_partition_law":
            certificate_a["reduced_partition_law_status"],
        "pair_is_lawful_nine_reduction":
            certificate_a["lawful_reduction_status"],
        "pair_lcm_residual_law":
            certificate_b["exact_relation_tests"][2]["status"],
        "pair_physics_clock_accounting_identity":
            certificate_b["exact_relation_tests"][3]["status"],
        "pair_physics_clock_catchup_value_law":
            certificate_b["exact_relation_tests"][4]["status"],
        "pair_weight_rank_law":
            certificate_c["exact_relation_tests"][1]["status"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": checks,
        "pass": False,
        "terminal": "CYCLE846_REDUCED_BRAIDS_DELAY_LAW_HONEST_FAIL",
    }
    output = stable_render(certificates, report)
    final_size = len(output.encode("utf-8"))
    if final_size >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 846,
            "pass": False,
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_size,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE846_REDUCED_BRAIDS_DELAY_LAW_HONEST_FAIL",
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
            "error_type": type(error).__name__,
            "error": str(error),
            "pass": False,
            "terminal": "CYCLE846_REDUCED_BRAIDS_DELAY_LAW_HONEST_FAIL",
        }))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
