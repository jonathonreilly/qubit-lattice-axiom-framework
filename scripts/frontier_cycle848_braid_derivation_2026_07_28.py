#!/usr/bin/env python3
"""Cycle 848: exact local-coincidence census for the two-scale braids.

The nine-state window is independently replayed from the Cycle-830 literal
fixture bank.  The expensive pair-braid result is a SHA/blob/commit-pinned
copy of Cycle 846; its complete RLE is UNITED and therefore contains no
generated coincidence transition.  Named primaries are text/AST-only and
fail closed if imported.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle842_local_causal_theorem_2026_07_28.py",
    "scripts/frontier_cycle845_partition_route_2026_07_28.py",
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
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR24-20260729"
EXPECTED_BASE = "4f97118a3a5b0831e075d5050d538658abaad115"
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
NORMALIZED_DEPTH = 64
PREDECESSOR_DEPTH = NORMALIZED_DEPTH + 1
NINE_FUNNEL_MOVEMENT = 14739
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
NINE_PREDICATE_WIRES = (40, 81, 105)
NINE_PREDICATE_PATTERNS = ((0, 0, 0), (0, 1, 1), (1, 0, 0))
PAIR_PREDICATE_WIRES = (88, 124, 125)
PAIR_POSITIONS = ((0, 5), (0, 6))
EXPECTED_NORMALIZED_PARTITION_SHA256 = (
    "726b74aefc7afa6e1790c7dc73a59eacdadeec72246e19ac01104be09d49829d"
)
EXPECTED_PAIR_DEPTH_SHA256 = (
    "dc7156746a46cbe6edfaceb4ccfb9b27fc7250d2608a991848cfec6f62f39932"
)
EXPECTED_MATCHING_NINE_SUBSETS = (
    ((2, 7), (2, 8)),
    ((3, 8), (3, 9)),
    ((3, 8), (4, 9)),
    ((3, 9), (4, 9)),
    ((4, 10), (5, 10)),
)
EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[1]:
        "65ced87db73db177c561e0dd293ae88963c15929d820f6dd99417a27ba647def",
    AUDIT_INPUT_PATHS[2]:
        "b97e227375a8cc14580d8f413897df2209e9e872b1a46ec59f9a2e61af593ca8",
}
EXPECTED_SOURCE_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[1]: "a1836d84d8dda74c4f79cc1bbc60ef798d86a2e3",
    AUDIT_INPUT_PATHS[2]: "3c7a6e61bbc656b7c6b69b96be36066d0ad1e8e8",
}
COPIED_CYCLE846 = {
    "commit": "7af6f39f9f2714a5a836af8b1bd3170b2afd4715",
    "path": "scripts/frontier_cycle846_reduced_braids_delay_law_2026_07_28.py",
    "source_sha256":
        "172313524341e958d36e1028f0cec5e64e81c4efd915c009073049998c37fc45",
    "git_blob": "2e0eb1848b92ab3f43a5ada64664ab45b58f5bb1",
    "normalized_depth_sequence_sha256": EXPECTED_PAIR_DEPTH_SHA256,
    "full_RLE": (
        (1, 193206, "311fbdc9dd81ab2d62a214a17cb3d356fb66919181791e002c721a1e946283a4"),
        (2, 246665, "f1b8c00d3c3d598261f65f849bdd98ae9fb3788a5289ad278c4ccc5e35b12e20"),
        (0, 1142428, "5d207cf5085ae36f7a607c63eae04bc4ce2e2b43a67ea5209e306971be32ca6e"),
    ),
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
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
Partition = tuple[tuple[int, ...], ...]

BLOCKLISTED_MODULES = tuple(sorted({
    *(Path(path).stem for path in AUDIT_INPUT_PATHS),
    Path(str(COPIED_CYCLE846["path"])).stem,
}))


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
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, check=True,
        capture_output=True, timeout=30,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode("utf-8").strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == name
                    for target in node.targets)
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
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {path: ast.parse(payload, filename=path)
             for path, payload in payloads.items()}
    copied_spec = f"{COPIED_CYCLE846['commit']}:{COPIED_CYCLE846['path']}"
    copied_payload = git_bytes("show", copied_spec)
    copied_tree = ast.parse(copied_payload, filename=copied_spec)
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    source_sha = {path: sha256(payload).hexdigest()
                  for path, payload in payloads.items()}
    source_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    copied_checks = {
        "source_sha256_exact":
            sha256(copied_payload).hexdigest() == COPIED_CYCLE846["source_sha256"],
        "git_blob_exact": git_blob(copied_payload) == COPIED_CYCLE846["git_blob"],
        "PAIR_POSITIONS_exact":
            literal_assignment(copied_tree, "PAIR_POSITIONS") == PAIR_POSITIONS,
        "BACKBONE_exact":
            literal_assignment(copied_tree, "BACKBONE") == BACKBONE,
        "NORMALIZED_DEPTH_exact":
            literal_assignment(copied_tree, "NORMALIZED_DEPTH") == NORMALIZED_DEPTH,
        "AST_basis": {
            "pair_braids", "nine_tail", "certificate_a_reduced_braids"
        } <= function_names(copied_tree),
    }
    ast_basis = {
        "cycle830_fixtures": all(
            literal_assignment(trees[AUDIT_INPUT_PATHS[0]], name) is not None
            for name in ("GATE_CONSTANTS_B85", "FAMILY_STATES_B85",
                         "SSTAR_PACKED_B85")
        ),
        "cycle842_predicate": (
            literal_assignment(trees[AUDIT_INPUT_PATHS[1]],
                               "DISCRIMINATOR_WIRES") == NINE_PREDICATE_WIRES
            and literal_assignment(trees[AUDIT_INPUT_PATHS[1]],
                                   "DISCRIMINATOR_PATTERNS")
            == NINE_PREDICATE_PATTERNS
            and {"certificate_a_wire_dynamics", "discriminator_mask"}
            <= function_names(trees[AUDIT_INPUT_PATHS[1]])
        ),
        "cycle845_braid": {
            "partition_of", "partition_event", "certificate_a_partition_dynamics"
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle846_copy": all(copied_checks.values()),
    }
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    stdlib_roots = set(sys.stdlib_module_names) | {"__future__"}
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", EXPECTED_BASE, "HEAD"),
        cwd=ROOT, timeout=20,
    ).returncode == 0
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "pinned_copy_count": 1,
        "total_source_primary_count": len(AUDIT_INPUT_PATHS) + 1,
        "maximum_source_primaries": 7,
        "source_sha256": source_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "source_git_blobs": source_blobs,
        "expected_source_git_blobs": EXPECTED_SOURCE_GIT_BLOBS,
        "copied_cycle846": {**COPIED_CYCLE846, "checks": copied_checks},
        "AST_basis": ast_basis,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_start": blocked_loaded,
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= stdlib_roots,
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": git_text("branch", "--show-current"),
        "expected_branch": EXPECTED_BRANCH,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob(self_payload),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and result["total_source_primary_count"] <= 7
        and source_sha == EXPECTED_SOURCE_SHA256
        and source_blobs == EXPECTED_SOURCE_GIT_BLOBS
        and all(ast_basis.values())
        and not blocked_loaded
        and not FIREWALL.hits
        and result["stdlib_only"]
        and result["git_branch"] == EXPECTED_BRANCH
        and base_is_ancestor
    )
    trees["copied_cycle846"] = copied_tree
    return result, trees


def cyclic_separation(pair: Pair) -> int:
    return min((pair[1] - pair[0]) % RING_STATIONS,
               (pair[0] - pair[1]) % RING_STATIONS)


def lawful_pairs() -> tuple[Pair, ...]:
    return tuple(pair for pair in combinations(range(RING_STATIONS), 2)
                 if cyclic_separation(pair) > 1)


def state_sha256(state: int) -> str:
    return sha256(bytes((state >> wire) & 1
                        for wire in range(STATE_BITS))).hexdigest()


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def decode_cycle830_fixtures(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(literal_assignment(tree, name) for name in (
        "GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85",
    ))
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("Cycle-830 literal fixtures not found")
    gate_raw, family_raw, target_raw = tuple(
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros = []
    for length in lengths:
        rows = []
        for _index in range(length):
            rows.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(rows))
    pairs = lawful_pairs()
    keys = tuple(sorted((event, pair) for event in range(4) for pair in pairs))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(family_raw[start:start + STATE_BYTES],
                                     "little")
    target = int.from_bytes(target_raw, "little")
    public = {
        "macro_gate_counts": lengths,
        "macro_gate_count": sum(lengths),
        "family_key_count": len(states),
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "target_raw_sha256": sha256(target_raw).hexdigest(),
        "target_state_sha256": state_sha256(target),
        "target_weight": target.bit_count(),
    }
    public["pass"] = (
        len(lengths) == RING_STATIONS and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and len(target_raw) == STATE_BYTES
        and len(states) == FAMILY_SIZE and len(pairs) == 44
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and public["target_raw_sha256"] == EXPECTED_SSTAR_PACKED_SHA256
    )
    return {"macros": tuple(macros), "keys": keys, "states": states,
            "target": target, "public": public}


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
                1 << lane for lane, pair in enumerate(lane_pairs)
                if station in {(pair[0] + phase) % RING_STATIONS,
                               (pair[1] + phase) % RING_STATIONS}
            )
            if lane_mask:
                rows.extend((kind, first, second, third, lane_mask)
                            for kind, first, second, third in macro)
        schedules.append(tuple(rows))
    return tuple(schedules)


def movement_schedule(
    phases: tuple[tuple[MaskedGate, ...], ...],
) -> tuple[MaskedGate, ...]:
    return tuple(row for phase in phases for row in phase)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, lane_mask in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        elif kind == 2:
            columns[third] ^= columns[first] & columns[second] & lane_mask
        else:
            raise AssertionError(("unknown gate kind", kind))


def compile_word(
    macros: tuple[tuple[Gate, ...], ...], pair: Pair,
) -> tuple[tuple[int, int, int], ...]:
    rows = []
    for phase in range(RING_STATIONS):
        live = {(pair[0] + phase) % RING_STATIONS,
                (pair[1] + phase) % RING_STATIONS}
        for station, macro in enumerate(macros):
            if station not in live:
                continue
            for kind, first, second, third in macro:
                if kind == 0:
                    rows.append((0, 0, 1 << first))
                elif kind == 1:
                    rows.append((1, 1 << first, 1 << second))
                elif kind == 2:
                    rows.append((2, (1 << first) | (1 << second), 1 << third))
                else:
                    raise AssertionError(("unknown gate kind", kind))
    if len(rows) != WORD_GATE_COUNT:
        raise AssertionError(("unexpected word length", pair, len(rows)))
    return tuple(rows)


def apply_word(
    state: int, word: tuple[tuple[int, int, int], ...], *, reverse: bool = False,
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
    return tuple(sorted((tuple(group) for group in groups.values()),
                        key=lambda group: group[0]))


def evolve_nine(fixtures: dict[str, object]) -> dict[str, object]:
    initial = tuple(fixtures["states"][(0, pair)] for pair in BACKBONE)
    duplicated = initial + initial
    phases = build_phase_schedules(fixtures["macros"], BACKBONE + BACKBONE)
    schedule = movement_schedule(phases)
    columns = bit_slice(duplicated)
    forward_tail = []
    duplicate_exact = True
    for movement in range(1, NINE_FUNNEL_MOVEMENT + 1):
        advance(columns, schedule)
        if movement >= NINE_FUNNEL_MOVEMENT - PREDECESSOR_DEPTH:
            states = capture_lanes(columns, 2 * len(BACKBONE))
            duplicate_exact &= states[:len(BACKBONE)] == states[len(BACKBONE):]
            forward_tail.append(states[:len(BACKBONE)])
    states_by_depth = tuple(reversed(forward_tail))
    partitions = tuple(partition_of(states)
                       for states in states_by_depth[:NORMALIZED_DEPTH + 1])
    return {
        "states_by_depth": states_by_depth,
        "normalized_partitions": partitions,
        "normalized_partition_sha256": digest(partitions),
        "movement_schedule_rows": len(schedule),
        "duplicate_exact_every_captured_depth": duplicate_exact,
        "terminal_matches_target": all(
            state == fixtures["target"] for state in states_by_depth[0]
        ),
        "pass": (
            len(states_by_depth) == PREDECESSOR_DEPTH + 1
            and duplicate_exact
            and digest(partitions) == EXPECTED_NORMALIZED_PARTITION_SHA256
            and all(state == fixtures["target"] for state in states_by_depth[0])
        ),
    }


def run() -> int:
    """Scaffold entry point; certificates are added in the next commit."""
    started = monotonic()
    source, trees = source_controls()
    fixtures = decode_cycle830_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    nine = evolve_nine(fixtures)
    report = {
        "cycle": 848,
        "stage": "CORE_SCAFFOLD",
        "source_controls": source,
        "fixtures": fixtures["public"],
        "nine": {key: value for key, value in nine.items()
                 if key != "states_by_depth"},
        "runtime_seconds": round(monotonic() - started, 6),
        "pass": source["pass"] and fixtures["public"]["pass"] and nine["pass"],
    }
    print(compact(report))
    return 0 if report["pass"] else 1


def main() -> int:
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
