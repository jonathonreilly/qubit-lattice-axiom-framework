#!/usr/bin/env python3
"""Cycle 839 independent adversarial check.

The Cycle-839 and Cycle-837 primaries are SHA-pinned text/AST inputs only.
Meeting geometry is recomputed by path-graph breadth-first layers, rail
motion by literal two-SWAP-layer simulation, and the bounded Boolean search
by a fresh exact engine over only the complete s=4 and s=5 cohorts.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle837_why_sep5_2026_07_28.py",
    "scripts/frontier_cycle839_meeting_derivation_2026_07_28.py",
)

import ast
import base64
from collections import Counter
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
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
HORIZON_TICK = 162129
HISTORICAL_COMMIT = "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744"
HISTORICAL_PATH = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py"
)
HISTORICAL_SPEC = f"{HISTORICAL_COMMIT}:{HISTORICAL_PATH}"
EXPECTED_HISTORICAL_SHA256 = (
    "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58"
)
EXPECTED_HISTORICAL_BLOB = "98b1571228ad0902301b6853208ef249ea2c2973"
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_TARGET_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)
EXPECTED_TARGET_BITS_SHA256 = (
    "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a"
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    AUDIT_INPUT_PATHS[2]:
        "f210ebc75909977eaa468a20b45f9a75ab9ad2e2ac0e48d0c4aab04d3a0a9a9f",
    AUDIT_INPUT_PATHS[3]:
        "bba2ce68e34bb6c502681c201ba83666e9f674aea2606ced4e3f894fdadfe4fa",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    AUDIT_INPUT_PATHS[2]: "8889e129f006bdaf4d3a3d7dd7bb3f1cac595ca7",
    AUDIT_INPUT_PATHS[3]: "9289962e4cdd24732a9c5d1ea53b360d236948f8",
}
BLOCKLISTED_MODULES = (
    Path(AUDIT_INPUT_PATHS[2]).stem,
    Path(AUDIT_INPUT_PATHS[3]).stem,
)
EXPECTED_REPRESENTATIVES = {
    1: ((1, 5), (0, 1), (6,)),
    2: ((1, 5), (1,), (7, 6)),
    3: ((2, 4), (1, 2), (7,)),
    4: ((2, 4), (2,), (8, 7)),
    5: ((3, 3), (2, 3), (8,)),
}
EXPECTED_PROJECTED_UNIQUE = {
    2: (21, 34),
    3: (25, 33),
    4: (26, 32),
    5: (21, 21),
}
PARTIAL_FINDING = (
    "PARTIAL: the meeting theorem, actual rail consequence, and bounded "
    "reach/nonreach classification hold exactly; the tie-to-funnel causal "
    "link remains open."
)

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]


class _BlockedPrimaryFinder(importlib.abc.MetaPathFinder):
    """Fail closed if either text/AST-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _BlockedPrimaryFinder()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        timeout=30,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode().strip()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


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


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef | None:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    return matches[0] if len(matches) == 1 else None


def source_controls() -> tuple[dict[str, object], ast.Module]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    imports = tuple(sorted({
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in self_tree.body
        if isinstance(node, ast.ImportFrom)
        and node.module != "__future__"
    }))
    expected_imports = (
        "ast", "base64", "collections", "hashlib", "importlib.abc",
        "itertools", "json", "pathlib", "struct", "subprocess", "sys",
        "time", "zlib",
    )
    source_rows = []
    for path in AUDIT_INPUT_PATHS:
        payload = payloads[path]
        source_rows.append({
            "path": path,
            "access": (
                "TEXT_AST_ONLY_BLOCKLISTED"
                if Path(path).stem in BLOCKLISTED_MODULES
                else "TEXT_AST_PROVENANCE_ONLY"
            ),
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": EXPECTED_SHA256[path],
            "sha256_exact":
                sha256(payload).hexdigest() == EXPECTED_SHA256[path],
            "git_blob": git_blob(payload),
            "expected_git_blob": EXPECTED_GIT_BLOBS[path],
            "git_blob_exact":
                git_blob(payload) == EXPECTED_GIT_BLOBS[path],
        })
    cycle719 = payloads[AUDIT_INPUT_PATHS[0]].decode()
    cycle832 = payloads[AUDIT_INPUT_PATHS[1]].decode()
    cycle837 = payloads[AUDIT_INPUT_PATHS[2]].decode()
    cycle839 = payloads[AUDIT_INPUT_PATHS[3]].decode()
    ast_basis = {
        "cycle719_two_swap_layers": all(
            fragment in cycle719 for fragment in (
                "def apply_controller_step(",
                "if a[station]:",
                "a[station], b[station] = b[station], a[station]",
                "target = (station + 1) % stations",
                "b[station], a[target] = a[target], b[station]",
            )
        ),
        "cycle832_target_scope": all(
            fragment in cycle832 for fragment in (
                "STATE_BITS = 5815",
                "FUNNEL_MOMENTS = {0: 14739",
                "full_state_hamming_weight",
            )
        ),
        "cycle837_boundary_only": all(
            fragment in cycle837 for fragment in (
                "def first_ball_meeting(",
                '"both_arcs_first_overlap_simultaneously"',
                '"occupancy_1_1_is_bank_cell_geometry": True',
                "Literal landed controller tokens are common-translated",
            )
        ),
        "cycle839_claim_packet": all(
            fragment in cycle839 for fragment in (
                "def meeting_theorem_certificate(",
                "def meet_configurations_certificate(",
                "def reachability_certificate(",
                "def verdict_certificate(",
            )
        ),
        "blocked_function_nodes_present": (
            function_node(trees[AUDIT_INPUT_PATHS[2]], "first_ball_meeting")
            is not None
            and function_node(
                trees[AUDIT_INPUT_PATHS[3]], "verdict_certificate"
            ) is not None
        ),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "all_paths_existing_worktree_relative": all(
            (ROOT / path).is_file() and not Path(path).is_absolute()
            for path in AUDIT_INPUT_PATHS
        ),
        "named_file_reads": {
            "worktree_inputs": len(AUDIT_INPUT_PATHS),
            "pinned_git_objects": 1,
            "checker_self": 1,
            "total": len(AUDIT_INPUT_PATHS) + 2,
            "limit": 6,
        },
        "source_rows": tuple(source_rows),
        "AST_provenance_basis": ast_basis,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_start": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_imports": imports,
        "expected_stdlib_imports": expected_imports,
        "stdlib_only": imports == expected_imports,
        "git_head": git_text("rev-parse", "HEAD"),
        "pass": False,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_paths_existing_worktree_relative"]
        and result["named_file_reads"]["total"] <= 6
        and all(
            row["sha256_exact"] and row["git_blob_exact"]
            for row in source_rows
        )
        and all(ast_basis.values())
        and result["stdlib_only"]
        and not result["blocked_modules_loaded_at_start"]
        and not result["firewall_hits_at_start"]
    )
    return result, trees[AUDIT_INPUT_PATHS[3]]


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


def bit_tuple_sha256(state: int) -> str:
    return sha256(bytes(
        (state >> wire) & 1 for wire in range(STATE_BITS)
    )).hexdigest()


def decode_fixture_object() -> dict[str, object]:
    source = git_bytes("show", HISTORICAL_SPEC)
    tree = ast.parse(source, filename=HISTORICAL_SPEC)
    encoded = tuple(
        literal_assignment(tree, name)
        for name in (
            "GATE_CONSTANTS_B85",
            "FAMILY_STATES_B85",
            "SSTAR_PACKED_B85",
        )
    )
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("historical literal fixture missing")
    gate_raw, family_raw, target_raw = tuple(
        zlib.decompress(base64.b85decode(value))
        for value in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    cursor = 22
    macros = []
    for length in lengths:
        macro = []
        for _ in range(length):
            macro.append(struct.unpack(
                "<BHHH", gate_raw[cursor:cursor + 7]
            ))
            cursor += 7
        macros.append(tuple(macro))
    pairs = lawful_pairs()
    keys = tuple(sorted(
        (event, pair)
        for event in range(4)
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
        "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY",
        "source_spec": HISTORICAL_SPEC,
        "source_sha256": sha256(source).hexdigest(),
        "source_git_blob": git_text("rev-parse", HISTORICAL_SPEC),
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "target_packed_sha256": sha256(target_raw).hexdigest(),
        "target_bit_tuple_sha256": bit_tuple_sha256(target),
        "target_hamming_weight": target.bit_count(),
        "macro_gate_counts": lengths,
        "family_key_count": len(keys),
        "pass": False,
    }
    public["pass"] = (
        public["source_sha256"] == EXPECTED_HISTORICAL_SHA256
        and public["source_git_blob"] == EXPECTED_HISTORICAL_BLOB
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and public["target_packed_sha256"]
        == EXPECTED_TARGET_PACKED_SHA256
        and public["target_bit_tuple_sha256"]
        == EXPECTED_TARGET_BITS_SHA256
        and cursor == len(gate_raw)
        and len(macros) == RING_STATIONS
        and sum(lengths) == 3106
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and len(keys) == len(states) == FAMILY_SIZE
        and len(target_raw) == STATE_BYTES
        and target.bit_count() == 44
    )
    return {
        "macros": tuple(macros),
        "keys": keys,
        "states": states,
        "target": target,
        "public": public,
    }


def arc_path(left: int, direction: int, length: int) -> tuple[int, ...]:
    return tuple(
        (left + direction * offset) % RING_STATIONS
        for offset in range(length + 1)
    )


def path_distances(
    vertices: tuple[int, ...],
    source: int,
) -> dict[int, int]:
    """Generic BFS on the supplied path graph, independent of index formulas."""
    neighbours = {vertex: set() for vertex in vertices}
    for first, second in zip(vertices, vertices[1:]):
        neighbours[first].add(second)
        neighbours[second].add(first)
    distance = {source: 0}
    frontier = [source]
    while frontier:
        current = frontier.pop(0)
        for neighbour in sorted(neighbours[current]):
            if neighbour not in distance:
                distance[neighbour] = distance[current] + 1
                frontier.append(neighbour)
    return distance


def bfs_first_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    left_distance = path_distances(vertices, vertices[0])
    right_distance = path_distances(vertices, vertices[-1])
    for tick in range(len(vertices)):
        overlap = tuple(
            vertex for vertex in vertices
            if left_distance[vertex] <= tick
            and right_distance[vertex] <= tick
        )
        if overlap:
            return tick, overlap
    raise AssertionError(("path fronts never meet", vertices))


def source_swap(station: int, left: int, right: int) -> int:
    return (left + right - station) % RING_STATIONS


def meeting_theorem_certificate() -> dict[str, object]:
    rows = []
    failures = []
    for separation in range(1, 6):
        rotation_rows = []
        for left in range(RING_STATIONS):
            right = (left + separation) % RING_STATIONS
            short = bfs_first_meeting(
                arc_path(left, +1, separation)
            )
            long = bfs_first_meeting(
                arc_path(left, -1, RING_STATIONS - separation)
            )
            short_symmetric = {
                source_swap(station, left, right)
                for station in short[1]
            } == set(short[1])
            long_symmetric = {
                source_swap(station, left, right)
                for station in long[1]
            } == set(long[1])
            rotation_rows.append({
                "oriented_pair": (left, right),
                "short": short,
                "long": long,
                "reflection_symmetric":
                    short_symmetric and long_symmetric,
            })
        representative = rotation_rows[0]
        expected_times, expected_short, expected_long = (
            EXPECTED_REPRESENTATIVES[separation]
        )
        rotation_exact = all(
            row["short"][0] == expected_times[0]
            and row["long"][0] == expected_times[1]
            and row["short"][1] == tuple(
                (station + left) % RING_STATIONS
                for station in expected_short
            )
            and row["long"][1] == tuple(
                (station + left) % RING_STATIONS
                for station in expected_long
            )
            and row["reflection_symmetric"]
            for left, row in enumerate(rotation_rows)
        )
        if not rotation_exact:
            failures.append(separation)
        rows.append({
            "separation": separation,
            "arc_lengths": (
                separation, RING_STATIONS - separation
            ),
            "meeting_times_short_long": (
                representative["short"][0],
                representative["long"][0],
            ),
            "representative_short_centers":
                representative["short"][1],
            "representative_long_centers":
                representative["long"][1],
            "all_11_rotations_and_reflections_exact": rotation_exact,
        })
    ties = tuple(
        row["separation"] for row in rows
        if row["meeting_times_short_long"][0]
        == row["meeting_times_short_long"][1]
    )
    observed = {
        row["separation"]: (
            row["meeting_times_short_long"],
            row["representative_short_centers"],
            row["representative_long_centers"],
        )
        for row in rows
    }
    passed = (
        observed == EXPECTED_REPRESENTATIVES
        and ties == (5,)
        and not failures
    )
    return {
        "name": "THE MEETING THEOREM",
        "verdict": "PASS" if passed else "FAIL",
        "method":
            "fresh BFS distance layers on each simple path, for all 55 "
            "oriented representatives; no primary function executed",
        "per_separation": tuple(rows),
        "unique_equal_time_separation": ties,
        "finding":
            "The independently enumerated short/long meeting times are "
            "(1,5),(1,5),(2,4),(2,4),(3,3), with the claimed "
            "representative centers; the two arc times tie only at s=5.",
        "pass": passed,
    }


def simulate_rail_ticks(
    pair: Pair,
    ticks: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Apply the literal R1 then R2 rail swaps, without a closed-form jump."""
    a = [int(station in pair) for station in range(RING_STATIONS)]
    b = [0] * RING_STATIONS
    for _ in range(ticks):
        for station in range(RING_STATIONS):
            a[station], b[station] = b[station], a[station]
        for station in range(RING_STATIONS):
            target = (station + 1) % RING_STATIONS
            b[station], a[target] = a[target], b[station]
    return (
        tuple(index for index, occupied in enumerate(a) if occupied),
        tuple(index for index, occupied in enumerate(b) if occupied),
    )


def token_claim_certificate(
    meeting: dict[str, object],
) -> dict[str, object]:
    theorem_rows = {
        row["separation"]: row for row in meeting["per_separation"]
    }
    rows = []
    for separation in range(1, 6):
        theorem = theorem_rows[separation]
        times = theorem["meeting_times_short_long"]
        centers = (
            theorem["representative_short_centers"]
            + theorem["representative_long_centers"]
        )
        union = set(centers)
        short_a, short_b = simulate_rail_ticks((0, separation), times[0])
        long_a, long_b = simulate_rail_ticks((0, separation), times[1])
        simultaneous_ticks = tuple(
            tick for tick in range(RING_STATIONS)
            if set(simulate_rail_ticks((0, separation), tick)[0])
            <= union
        )
        rows.append({
            "separation": separation,
            "landed_family": separation > 1,
            "short_meet": {
                "tick": times[0],
                "A": short_a,
                "B": short_b,
            },
            "long_meet": {
                "tick": times[1],
                "A": long_a,
                "B": long_b,
            },
            "combined_center_set": tuple(sorted(union)),
            "ticks_both_A_in_combined_centers":
                simultaneous_ticks,
            "collision_free":
                len(short_a) == len(set(short_a)) == 2
                and len(long_a) == len(set(long_a)) == 2,
            "B_clean": not short_b and not long_b,
        })
    s5 = rows[-1]
    s5_a, s5_b = simulate_rail_ticks((0, 5), 3)
    reflected = {
        source_swap(station, 0, 5) for station in s5_a
    }
    lawful_simultaneous = tuple(
        row["separation"] for row in rows
        if row["landed_family"]
        and row["ticks_both_A_in_combined_centers"]
    )
    passed = (
        lawful_simultaneous == (5,)
        and 3 in s5["ticks_both_A_in_combined_centers"]
        and set(s5_a) == {3, 8}
        and not s5_b
        and reflected != set(s5_a)
        and all(row["collision_free"] and row["B_clean"] for row in rows)
        and rows[0]["landed_family"] is False
    )
    return {
        "name": "THE TOKEN CLAIM",
        "verdict": "PASS" if passed else "FAIL",
        "method":
            "literal R1/R2 Boolean rail swaps for every tested tick; no "
            "primary rail-bookkeeping function executed",
        "per_separation": tuple(rows),
        "lawful_separations_with_simultaneous_A_center_placement":
            lawful_simultaneous,
        "s5_meet_tick_A": s5_a,
        "s5_meet_tick_B": s5_b,
        "s5_A_source_swap_reflection": tuple(sorted(reflected)),
        "s5_A_reflection_symmetric": reflected == set(s5_a),
        "finding":
            "Only s=5 puts both common-translating A tokens on the union "
            "of the two arc-center sets at one meeting tick. The occupied "
            "A row is not source-swap-reflection symmetric, B remains "
            "clean, and no token collision occurs; s=1 is outside the "
            "landed family.",
        "pass": passed,
    }


def transpose_states(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        remaining = state
        while remaining:
            bit = remaining & -remaining
            columns[bit.bit_length() - 1] |= 1 << lane
            remaining ^= bit
    return columns


def capture_states(
    columns: list[int],
    lane_count: int,
) -> tuple[int, ...]:
    states = [0] * lane_count
    lane_limit = (1 << lane_count) - 1
    for wire, column in enumerate(columns):
        live = column & lane_limit
        while live:
            bit = live & -live
            states[bit.bit_length() - 1] |= 1 << wire
            live ^= bit
    return tuple(states)


def station_masks(
    keys: tuple[Key, ...],
    phase: int,
) -> tuple[int, ...]:
    masks = [0] * RING_STATIONS
    for lane, (_event, pair) in enumerate(keys):
        for origin in pair:
            masks[(origin + phase) % RING_STATIONS] |= 1 << lane
    return tuple(masks)


def apply_controller_phase(
    columns: list[int],
    macros: tuple[tuple[Gate, ...], ...],
    masks: tuple[int, ...],
) -> None:
    for station, macro in enumerate(macros):
        lane_mask = masks[station]
        if not lane_mask:
            continue
        for kind, first, second, third in macro:
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


def early_snapshots(
    fixtures: dict[str, object],
) -> dict[int, tuple[int, ...]]:
    keys = fixtures["keys"]
    states = fixtures["states"]
    macros = fixtures["macros"]
    assert isinstance(keys, tuple)
    assert isinstance(states, dict)
    assert isinstance(macros, tuple)
    columns = transpose_states(tuple(states[key] for key in keys))
    snapshots = {}
    for tick in range(1, 6):
        apply_controller_phase(
            columns, macros, station_masks(keys, tick - 1)
        )
        snapshots[tick] = capture_states(columns, len(keys))
    return snapshots


def meet_configuration_certificate(
    meeting: dict[str, object],
    fixtures: dict[str, object],
    snapshots: dict[int, tuple[int, ...]],
) -> dict[str, object]:
    keys = fixtures["keys"]
    assert isinstance(keys, tuple)
    index = {key: lane for lane, key in enumerate(keys)}
    theorem_rows = {
        row["separation"]: row for row in meeting["per_separation"]
    }
    rows = [{
        "separation": 1,
        "outcome": "OUTSIDE_LANDED_PAIRWISE_SEPARATED_FAMILY",
        "projected_unique_short_long": None,
    }]
    for separation in range(2, 6):
        group = tuple(
            key for key in keys
            if cyclic_separation(key[1]) == separation
        )
        short_tick, long_tick = theorem_rows[separation][
            "meeting_times_short_long"
        ]
        short_states = tuple(
            snapshots[short_tick][index[key]] for key in group
        )
        long_states = tuple(
            snapshots[long_tick][index[key]] for key in group
        )
        rows.append({
            "separation": separation,
            "labeled_configuration_count": len(group),
            "meeting_times_short_long": (short_tick, long_tick),
            "projected_unique_short_long": (
                len(set(short_states)), len(set(long_states))
            ),
            "short_weight_census":
                dict(sorted(Counter(map(int.bit_count, short_states)).items())),
            "long_weight_census":
                dict(sorted(Counter(map(int.bit_count, long_states)).items())),
        })
    observed = {
        row["separation"]: row["projected_unique_short_long"]
        for row in rows[1:]
    }
    passed = (
        observed == EXPECTED_PROJECTED_UNIQUE
        and all(row["labeled_configuration_count"] == 44 for row in rows[1:])
    )
    return {
        "name": "THE MEET-CONFIGURATIONS TABLE",
        "verdict": "PASS" if passed else "FAIL",
        "rows": tuple(rows),
        "finding":
            "s=1 is outside the landed family; the independently "
            "projected unique 5815-bit state counts (short/long) are "
            "s2=21/34, s3=25/33, s4=26/32, and s5=21/21.",
        "pass": passed,
    }


def phase_operations(
    macros: tuple[tuple[Gate, ...], ...],
    keys: tuple[Key, ...],
) -> tuple[tuple[tuple[int, int, int, int, int], ...], ...]:
    phases = []
    for phase in range(RING_STATIONS):
        masks = station_masks(keys, phase)
        phases.append(tuple(
            (kind, first, second, third, masks[station])
            for station, macro in enumerate(macros)
            if masks[station]
            for kind, first, second, third in macro
        ))
    return tuple(phases)


def apply_operations(
    columns: list[int],
    operations: tuple[tuple[int, int, int, int, int], ...],
) -> None:
    for kind, first, second, third, lane_mask in operations:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )


def exact_target_lanes(
    columns: list[int],
    target: int,
    lane_mask: int,
    prefilter: tuple[int, ...],
) -> int:
    candidates = lane_mask
    for wire in prefilter:
        column = columns[wire] & lane_mask
        candidates &= (
            column if (target >> wire) & 1 else lane_mask ^ column
        )
        if not candidates:
            return 0
    for wire, raw_column in enumerate(columns):
        column = raw_column & lane_mask
        candidates &= (
            column if (target >> wire) & 1 else lane_mask ^ column
        )
        if not candidates:
            return 0
    return candidates


def set_lane_numbers(mask: int) -> tuple[int, ...]:
    lanes = []
    while mask:
        bit = mask & -mask
        lanes.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(lanes)


def duplicate_columns_equal(
    columns: list[int],
    cohort_size: int,
) -> bool:
    cohort_mask = (1 << cohort_size) - 1
    return all(
        (column & cohort_mask)
        == ((column >> cohort_size) & cohort_mask)
        for column in columns
    )


def bounded_reachability(
    fixtures: dict[str, object],
) -> dict[str, object]:
    all_keys = fixtures["keys"]
    all_states = fixtures["states"]
    macros = fixtures["macros"]
    target = fixtures["target"]
    assert isinstance(all_keys, tuple)
    assert isinstance(all_states, dict)
    assert isinstance(macros, tuple)
    assert isinstance(target, int)
    selected_keys = tuple(
        key for key in all_keys if cyclic_separation(key[1]) in (4, 5)
    )
    cohort_size = len(selected_keys)
    doubled_keys = selected_keys + selected_keys
    doubled_states = tuple(
        all_states[key] for key in doubled_keys
    )
    columns = transpose_states(doubled_states)
    operations = phase_operations(macros, doubled_keys)
    primary_mask = (1 << cohort_size) - 1
    duplicate_mask = primary_mask << cohort_size
    target_active = tuple(
        wire for wire in range(STATE_BITS) if (target >> wire) & 1
    )
    spread = tuple(sorted(set(
        index * (STATE_BITS - 1) // 127 for index in range(128)
    )))
    prefilter = tuple(sorted(set(target_active + spread)))
    checkpoints = {
        1, 2, 3, 4, 5, 1000, 10000, 50000, 100000, HORIZON_TICK
    }
    duplicate_checks = []
    primary_hits: list[tuple[int, Key]] = []
    duplicate_hits: list[tuple[int, Key]] = []
    for tick in range(1, HORIZON_TICK + 1):
        apply_operations(columns, operations[(tick - 1) % RING_STATIONS])
        primary_matches = exact_target_lanes(
            columns, target, primary_mask, prefilter
        )
        duplicate_matches = exact_target_lanes(
            columns, target, duplicate_mask, prefilter
        )
        primary_hits.extend(
            (tick, selected_keys[lane])
            for lane in set_lane_numbers(primary_matches)
        )
        duplicate_hits.extend(
            (tick, selected_keys[lane - cohort_size])
            for lane in set_lane_numbers(duplicate_matches)
        )
        if tick in checkpoints:
            duplicate_checks.append({
                "tick": tick,
                "all_5815_columns_equal":
                    duplicate_columns_equal(columns, cohort_size),
            })
    hits_by_separation = {}
    for separation, meet_tick in ((4, 2), (5, 3)):
        group = tuple(
            key for key in selected_keys
            if cyclic_separation(key[1]) == separation
        )
        hits = tuple(
            (tick, key) for tick, key in primary_hits
            if tick >= meet_tick
            and cyclic_separation(key[1]) == separation
        )
        reaching = tuple(sorted({key for _tick, key in hits}))
        hits_by_key = tuple(
            (
                key,
                tuple(tick for tick, hit_key in hits if hit_key == key),
            )
            for key in reaching
        )
        hits_by_separation[separation] = {
            "meet_tick": meet_tick,
            "labeled_configuration_count": len(group),
            "inclusive_global_horizon_tick": HORIZON_TICK,
            "exact_reaching_key_count": len(reaching),
            "nonreaching_key_count": len(group) - len(reaching),
            "reaching_keys": reaching,
            "exact_hit_ticks_by_key": hits_by_key,
        }
    backbone = tuple(
        (0, pair) for pair in lawful_pairs()
        if cyclic_separation(pair) == 5 and 0 not in pair
    )
    s4 = hits_by_separation[4]
    s5 = hits_by_separation[5]
    deterministic = (
        tuple(primary_hits) == tuple(duplicate_hits)
        and all(
            row["all_5815_columns_equal"] for row in duplicate_checks
        )
    )
    passed = (
        cohort_size == 88
        and tuple(map(len, operations)) == (3106,) * RING_STATIONS
        and target.bit_count() == 44
        and s4["labeled_configuration_count"] == 44
        and s4["exact_reaching_key_count"] == 0
        and s5["labeled_configuration_count"] == 44
        and s5["exact_reaching_key_count"] == 9
        and s5["reaching_keys"] == backbone
        and all(tick >= 3 for tick, _key in primary_hits)
        and deterministic
    )
    return {
        "name": "THE REACHABILITY SPLIT",
        "verdict": "PASS" if passed else "FAIL",
        "method":
            "fresh exact 5815-column Boolean evolution for the complete "
            "s=4 and s=5 cohorts, checked after every controller tick; "
            "the mirrored cohort independently exposes deterministic drift",
        "target_hamming_weight": target.bit_count(),
        "target_bit_tuple_sha256": bit_tuple_sha256(target),
        "selected_primary_lanes": cohort_size,
        "mirrored_determinism_lanes": cohort_size,
        "phase_gate_rows": tuple(map(len, operations)),
        "prefilter_wire_count": len(prefilter),
        "s4": s4,
        "s5": s5,
        "backbone_entrant_definition":
            "event=0, cyclic separation=5, neither endpoint is origin 0",
        "computed_nine_backbone_entrants": backbone,
        "all_primary_exact_hit_count": len(primary_hits),
        "duplicate_checks": tuple(duplicate_checks),
        "deterministic_duplicate_trace": deterministic,
        "finding":
            "Through inclusive controller tick 162129, the full s=4 "
            "cohort reaches exact weight-44 S* for 0/44 keys and the full "
            "s=5 cohort for 9/44 keys; the nine reaching keys are exactly "
            "the event-0, origin-absent separation-5 backbone entrants.",
        "pass": passed,
    }


def dict_has_false_binding(
    function: ast.FunctionDef,
    key_name: str,
) -> bool:
    for node in ast.walk(function):
        if not isinstance(node, ast.Dict):
            continue
        for key, value in zip(node.keys, node.values):
            if (
                isinstance(key, ast.Constant)
                and key.value == key_name
                and isinstance(value, ast.Constant)
                and value.value is False
            ):
                return True
    return False


def partial_ruling_certificate(
    primary_tree: ast.Module,
    meeting: dict[str, object],
    tokens: dict[str, object],
    configurations: dict[str, object],
    reachability: dict[str, object],
) -> dict[str, object]:
    function = function_node(primary_tree, "verdict_certificate")
    if function is None:
        return {
            "name": "THE PARTIAL RULING",
            "verdict": "FAIL",
            "finding": "Cycle-839 verdict_certificate AST node is missing.",
            "pass": False,
        }
    strings = tuple(
        node.value for node in ast.walk(function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    required_caveats = (
        "The auxiliary counterpropagating wavefront is not a state "
        "variable or update rule of the actual controller.",
        "The (3,3) property is not sufficient: it labels 44 lawful "
        "event/pair configurations, while only nine reach S*.",
        "The bounded family census establishes correlation and exact "
        "reachability, not a counterfactual causal mechanism or an "
        "unbounded necessity theorem.",
        PARTIAL_FINDING,
    )
    positive_overclaims = (
        "causal mechanism is established",
        "meeting tie causes the funnel",
        "meeting theorem derives the funnel",
        "unbounded necessity is proved",
    )
    joined = "\n".join(strings).lower()
    wording_exact = (
        all(caveat in strings for caveat in required_caveats)
        and dict_has_false_binding(function, "causal_chain_established")
        and not any(phrase in joined for phrase in positive_overclaims)
    )
    evidence_exact = all((
        meeting["pass"],
        tokens["pass"],
        configurations["pass"],
        reachability["pass"],
    ))
    passed = wording_exact and evidence_exact
    return {
        "name": "THE PARTIAL RULING",
        "verdict": "PASS" if passed else "FAIL",
        "AST_only_primary_audit": True,
        "required_caveats_present_verbatim": tuple(
            caveat for caveat in required_caveats if caveat in strings
        ),
        "causal_chain_established_literal_false":
            dict_has_false_binding(function, "causal_chain_established"),
        "positive_overclaim_phrases_found": tuple(
            phrase for phrase in positive_overclaims if phrase in joined
        ),
        "evidence_certificates_pass": evidence_exact,
        "finding": PARTIAL_FINDING,
        "pass": passed,
    }


def render(
    certificates: tuple[dict[str, object], ...],
    report: dict[str, object],
) -> str:
    lines = [
        (
            f"CERTIFICATE {certificate['name']} "
            f"{certificate['verdict']} :: {certificate['finding']}"
        )
        for certificate in certificates
    ]
    lines.extend((
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    ))
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: tuple[dict[str, object], ...],
    controls: dict[str, object],
    report: dict[str, object],
    controls_base: bool,
) -> str:
    for _ in range(20):
        controls["pass"] = (
            controls_base
            and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        controls["verdict"] = "PASS" if controls["pass"] else "FAIL"
        report["checks"]["CONTROLS"] = bool(controls["pass"])
        report["pass"] = all(report["checks"].values())
        science_names = (
            "THE MEETING THEOREM",
            "THE TOKEN CLAIM",
            "THE MEET-CONFIGURATIONS TABLE",
            "THE REACHABILITY SPLIT",
            "THE PARTIAL RULING",
        )
        science_pass = all(
            report["checks"].get(name, False) for name in science_names
        )
        report["terminal"] = (
            "CYCLE839_MEETING_INDEPENDENT_CHECK_PASS"
            if report["pass"] else (
                "CYCLE839_MEETING_PRIMARY_REFUTED"
                if not science_pass
                else "CYCLE839_MEETING_INDEPENDENT_CHECK_FAIL"
            )
        )
        output = render(certificates, report)
        size = len(output.encode())
        if (
            controls["stdout_bytes"] == size
            and report["stdout_bytes"] == size
        ):
            return output
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    controls, primary_tree = source_controls()
    source_controls_pass = bool(controls["pass"])
    fixture = decode_fixture_object()
    meeting = meeting_theorem_certificate()
    tokens = token_claim_certificate(meeting)
    snapshots = early_snapshots(fixture)
    replay_snapshots = early_snapshots(fixture)
    configurations = meet_configuration_certificate(
        meeting, fixture, snapshots
    )
    replay_configurations = meet_configuration_certificate(
        meeting_theorem_certificate(), fixture, replay_snapshots
    )
    reachability = bounded_reachability(fixture)
    partial = partial_ruling_certificate(
        primary_tree, meeting, tokens, configurations, reachability
    )
    deterministic_short = (
        snapshots == replay_snapshots
        and configurations == replay_configurations
        and meeting == meeting_theorem_certificate()
    )
    elapsed = monotonic() - started
    controls.update({
        "fixture_provenance": fixture["public"],
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": {
            "short_certificates_full_replay_exact": deterministic_short,
            "long_search_mirrored_88_lane_trace_exact":
                reachability["deterministic_duplicate_trace"],
            "certificate_sha256": digest((
                meeting, tokens, configurations, reachability, partial
            )),
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "user_runtime_ceiling_seconds": 1500,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "finding":
            "All source SHA/blob pins, the two-primary import firewall, "
            "literal worktree-relative input declaration, six-read cap, "
            "determinism checks, runtime ceiling, and stdout ceiling pass.",
        "pass": False,
    })
    controls_base = (
        source_controls_pass
        and fixture["public"]["pass"]
        and deterministic_short
        and reachability["deterministic_duplicate_trace"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC < 1500
    )
    controls["name"] = "CONTROLS"
    controls["verdict"] = "FAIL"
    certificates = (
        meeting,
        tokens,
        configurations,
        reachability,
        partial,
        controls,
    )
    checks = {
        certificate["name"]: bool(certificate["pass"])
        for certificate in certificates
    }
    report = {
        "cycle": 839,
        "checker": Path(__file__).name,
        "checks": checks,
        "meeting_times": tuple(
            row["meeting_times_short_long"]
            for row in meeting["per_separation"]
        ),
        "projected_unique_short_long": tuple(
            row["projected_unique_short_long"]
            for row in configurations["rows"][1:]
        ),
        "s4_exact_reach": (
            reachability["s4"]["exact_reaching_key_count"], 44
        ),
        "s5_exact_reach": (
            reachability["s5"]["exact_reaching_key_count"], 44
        ),
        "s5_reaching_keys": reachability["s5"]["reaching_keys"],
        "ruling": "PARTIAL" if partial["pass"] else "REFUTED",
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
        "terminal": "CYCLE839_MEETING_INDEPENDENT_CHECK_FAIL",
    }
    output = stable_render(
        certificates, controls, report, controls_base
    )
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
            "terminal": "CYCLE839_MEETING_INDEPENDENT_CHECK_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
