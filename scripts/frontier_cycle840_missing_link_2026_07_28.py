#!/usr/bin/env python3
"""Cycle 840: the meet-level discriminator behind the 9-of-44 S* split.

All predecessor runners are source primaries only.  Their required literal
fixtures are copied from SHA-pinned git objects and decoded here; none of the
primaries is imported or executed.  The landed Boolean dynamics is
independently reimplemented with Python integers.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle822_sstar_basin_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
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
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
SSTAR_BOUND_MOVEMENTS = 14739
SSTAR_BOUND_CONTROLLER_TICKS = SSTAR_BOUND_MOVEMENTS * RING_STATIONS

SOURCE_BLOCK = (0, 41)
BANK0_BLOCK = (41, 172)
BANK1_BLOCK = (172, 303)
LINK0_BLOCK = (1613, 1995)
REGISTER_BLOCKS = (
    ("source", SOURCE_BLOCK),
    ("bank0", BANK0_BLOCK),
    ("bank1", BANK1_BLOCK),
    ("link0", LINK0_BLOCK),
)

EXPECTED_BRANCH = "physics-loop/proof-grade-blockF19-20260729"
EXPECTED_BASE = "1522d92ec66956621093273f75eb4e4e4d366f7e"
HISTORICAL_SOURCES = (
    (
        "cycle839_primary",
        "863c268dd1",
        "scripts/frontier_cycle839_meeting_derivation_2026_07_28.py",
        "bba2ce68e34bb6c502681c201ba83666e9f674aea2606ced4e3f894fdadfe4fa",
        "9289962e4cdd24732a9c5d1ea53b360d236948f8",
    ),
    (
        "cycle838_primary",
        "da8484ced3",
        "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
        "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    ),
    (
        "cycle830_fixture_primary",
        "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
        "98b1571228ad0902301b6853208ef249ea2c2973",
    ),
)
EXPECTED_WORKTREE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "269d235c4981eaa4b94cfc200a0d472bf9f1ca8b57c2e14880afe754a9d41c56",
    AUDIT_INPUT_PATHS[2]:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
}
EXPECTED_WORKTREE_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "56fd26ec1f09e3690aa0e9cacd1447c289fd7ac0",
    AUDIT_INPUT_PATHS[2]: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
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
        SSTAR_BOUND_CONTROLLER_TICKS - 4,
        SSTAR_BOUND_CONTROLLER_TICKS + 1,
    )
    for key in EXPECTED_REACHING_KEYS
    if tick >= SSTAR_BOUND_CONTROLLER_TICKS - (key[1][0] - 1)
)
EXPECTED_MEET_PREFIX_PATTERNS = (
    (
        "ba5f27c37ebf2aa2a70ec87a6e237aa3f663443fb9b01618126a5ba588c2d7d4",
        "f4dbc620a03c9e1bbfc06f5fc30fb70a77b2a13149a8f9d44cb3aa769fe8e235",
    ),
    (
        "c73eb0b8c6e1888546b411bd694fd9d96d4b11b1920d11177699e8562167d5ca",
        "63223011e5f5442084d1fbfb6add65b7226d853c6212ac25f5a9090d08d7cbb6",
    ),
    (
        "c73eb0b8c6e1888546b411bd694fd9d96d4b11b1920d11177699e8562167d5ca",
        "e6a36aa3ab938b310bd0add14c8bce7d045d4d73201dbb3f2928a715a2a5b2e8",
    ),
    (
        "c73eb0b8c6e1888546b411bd694fd9d96d4b11b1920d11177699e8562167d5ca",
        "20e448e5ff534f9b865f946fa516aca11c03924630765cc857634bdcaf75fbf4",
    ),
)

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]


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
        blocked = {
            Path(item).stem for item in AUDIT_INPUT_PATHS
        } | {
            Path(path0).stem
            for _name, _commit, path0, _sha, _blob
            in HISTORICAL_SOURCES
        }
        if fullname.rsplit(".", 1)[-1] in blocked:
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
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        timeout=20,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode().strip()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


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


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    direct_imports = tuple(sorted({
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
    expected_stdlib = (
        "ast", "base64", "collections", "hashlib", "importlib.abc",
        "itertools", "json", "pathlib", "struct", "subprocess", "sys",
        "time", "zlib",
    )
    worktree_rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": "TEXT_AST_ONLY_BLOCKLISTED",
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_WORKTREE_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_WORKTREE_BLOBS[path],
        "exact": (
            sha256(payloads[path]).hexdigest()
            == EXPECTED_WORKTREE_SHA256[path]
            and git_blob(payloads[path]) == EXPECTED_WORKTREE_BLOBS[path]
        ),
    } for path in AUDIT_INPUT_PATHS)
    historical_rows = []
    historical_trees = {}
    for name, commit, path, expected_sha, expected_blob in HISTORICAL_SOURCES:
        spec = f"{commit}:{path}"
        payload = git_bytes("show", spec)
        tree = ast.parse(payload, filename=spec)
        historical_trees[name] = tree
        historical_rows.append({
            "name": name,
            "commit": commit,
            "path": path,
            "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": expected_sha,
            "git_blob": git_text("rev-parse", spec),
            "expected_git_blob": expected_blob,
            "exact": (
                sha256(payload).hexdigest() == expected_sha
                and git_text("rev-parse", spec) == expected_blob
            ),
        })
    ast_basis = {
        "cycle839_reimplementation_basis": {
            "decode_cycle830_fixtures", "build_phase_schedules",
            "apply_masked", "evolve_controller_ticks",
            "reachability_certificate",
        } <= function_names(historical_trees["cycle839_primary"]),
        "cycle838_delayed_basis": {
            "watched_residual_rows", "masked_schedule", "advance",
            "evolve", "optional_k2_certificate",
        } <= function_names(historical_trees["cycle838_primary"]),
        "cycle830_literal_fixtures": all(
            literal_assignment(
                historical_trees["cycle830_fixture_primary"], name
            ) is not None
            for name in (
                "GATE_CONSTANTS_B85", "FAMILY_STATES_B85",
                "SSTAR_PACKED_B85",
            )
        ),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "read_cap": 7,
        "named_worktree_input_count": len(AUDIT_INPUT_PATHS),
        "all_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in worktree_rows
        ),
        "worktree_source_rows": worktree_rows,
        "historical_source_rows": tuple(historical_rows),
        "AST_provenance_basis": ast_basis,
        "direct_imports": direct_imports,
        "expected_stdlib_imports": expected_stdlib,
        "stdlib_only": direct_imports == expected_stdlib,
        "blocked_modules_loaded_at_start": tuple(sorted(
            name for name in sys.modules
            if name.rsplit(".", 1)[-1] in {
                Path(path).stem for path in AUDIT_INPUT_PATHS
            } | {
                Path(path).stem
                for _name, _commit, path, _sha, _blob
                in HISTORICAL_SOURCES
            }
        )),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": git_text("branch", "--show-current"),
        "expected_git_branch": EXPECTED_BRANCH,
        "git_base": git_text("merge-base", "HEAD", EXPECTED_BASE),
        "expected_git_base": EXPECTED_BASE,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and len(AUDIT_INPUT_PATHS) <= result["read_cap"]
        and result["all_paths_existing_worktree_relative"]
        and all(row["exact"] for row in worktree_rows)
        and all(row["exact"] for row in historical_rows)
        and all(ast_basis.values())
        and result["stdlib_only"]
        and not result["blocked_modules_loaded_at_start"]
        and not result["firewall_hits_at_start"]
        and result["git_branch"] == EXPECTED_BRANCH
        and result["git_base"] == EXPECTED_BASE
    )
    return result


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


def block_value(state: int, block: tuple[int, int]) -> int:
    start, stop = block
    return (state >> start) & ((1 << (stop - start)) - 1)


def block_sha256(state: int, block: tuple[int, int]) -> str:
    start, stop = block
    width = stop - start
    return sha256(
        block_value(state, block).to_bytes((width + 7) // 8, "little")
    ).hexdigest()


def decode_cycle830_fixtures() -> dict[str, object]:
    row = next(
        item for item in HISTORICAL_SOURCES
        if item[0] == "cycle830_fixture_primary"
    )
    _name, commit, path, expected_sha, expected_blob = row
    spec = f"{commit}:{path}"
    source = git_bytes("show", spec)
    tree = ast.parse(source, filename=spec)
    encoded = tuple(
        literal_assignment(tree, name)
        for name in (
            "GATE_CONSTANTS_B85", "FAMILY_STATES_B85",
            "SSTAR_PACKED_B85",
        )
    )
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
    source_blob = git_text("rev-parse", spec)
    exact = (
        source_sha == expected_sha
        and source_blob == expected_blob
        and len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and sha256(family_raw).hexdigest() == EXPECTED_FAMILY_RAW_SHA256
        and len(target_raw) == STATE_BYTES
        and sha256(target_raw).hexdigest() == EXPECTED_SSTAR_PACKED_SHA256
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
            "source_access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "source_spec": spec,
            "source_sha256": source_sha,
            "source_git_blob": source_blob,
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
    lane_limit = (1 << lane_count) - 1
    for wire, column in enumerate(columns):
        live = column & lane_limit
        while live:
            bit = live & -live
            states[bit.bit_length() - 1] |= 1 << wire
            live ^= bit
    return tuple(states)


def build_phase_schedules(
    macros: tuple[tuple[Gate, ...], ...],
    lane_keys: tuple[Key, ...],
) -> tuple[tuple[MaskedGate, ...], ...]:
    schedules = []
    for phase in range(RING_STATIONS):
        rows = []
        for station, macro in enumerate(macros):
            mask = sum(
                1 << lane
                for lane, key in enumerate(lane_keys)
                if station in {
                    (key[1][0] + phase) % RING_STATIONS,
                    (key[1][1] + phase) % RING_STATIONS,
                }
            )
            if mask:
                rows.extend(
                    (kind, first, second, third, mask)
                    for kind, first, second, third in macro
                )
        schedules.append(tuple(rows))
    return tuple(schedules)


def build_movement_schedule(
    macros: tuple[tuple[Gate, ...], ...],
    lane_keys: tuple[Key, ...],
) -> tuple[MaskedGate, ...]:
    return tuple(
        gate
        for phase in build_phase_schedules(macros, lane_keys)
        for gate in phase
    )


def apply_masked(
    columns: list[int],
    schedule: tuple[MaskedGate, ...],
) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        elif kind == 2:
            columns[third] ^= columns[first] & columns[second] & mask
        else:
            raise AssertionError(("unknown gate kind", kind))


def lane_numbers(mask: int) -> tuple[int, ...]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


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


def evolve_s5_to_sstar_bound(
    fixtures: dict[str, object],
) -> dict[str, object]:
    macros = fixtures["macros"]
    all_keys = fixtures["keys"]
    states = fixtures["states"]
    target = fixtures["target"]
    assert isinstance(macros, tuple)
    assert isinstance(all_keys, tuple)
    assert isinstance(states, dict)
    assert isinstance(target, int)
    s5_keys = tuple(
        key for key in all_keys if cyclic_separation(key[1]) == 5
    )
    lane_keys = s5_keys + (s5_keys[0],)
    columns = bit_slice(tuple(states[key] for key in lane_keys))
    schedules = build_phase_schedules(macros, lane_keys)
    primary_mask = (1 << len(s5_keys)) - 1
    signature = tuple(sorted(set(
        tuple(
            wire for wire in range(STATE_BITS)
            if (target >> wire) & 1
        ) + tuple(
            index * (STATE_BITS - 1) // 191 for index in range(192)
        )
    )))
    meet_states: tuple[int, ...] | None = None
    exact_hits = []
    duplicate_checks = []
    for tick in range(1, SSTAR_BOUND_CONTROLLER_TICKS + 1):
        apply_masked(columns, schedules[(tick - 1) % RING_STATIONS])
        if tick == 3:
            meet_states = capture_lanes(columns, len(s5_keys))
        if tick in (3, SSTAR_BOUND_CONTROLLER_TICKS):
            duplicate_checks.append({
                "controller_tick": tick,
                "exact": all(
                    ((column >> 0) & 1)
                    == ((column >> len(s5_keys)) & 1)
                    for column in columns
                ),
            })
        hits = matching_mask(
            columns, target, primary_mask, signature
        )
        exact_hits.extend(
            (tick, s5_keys[lane]) for lane in lane_numbers(hits)
        )
    if meet_states is None:
        raise AssertionError("tick-3 meet snapshot missing")
    exact = (
        len(s5_keys) == 44
        and tuple(exact_hits) == EXPECTED_CONTROLLER_TICK_HITS
        and all(row["exact"] for row in duplicate_checks)
    )
    return {
        "keys": s5_keys,
        "meet_states": meet_states,
        "exact_hits": tuple(exact_hits),
        "public": {
            "scope":
                "all 44 s=5 keys, every completed controller tick 1..162129",
            "controller_tick_bound": SSTAR_BOUND_CONTROLLER_TICKS,
            "complete_movement_bound": SSTAR_BOUND_MOVEMENTS,
            "all_exact_target_hits": tuple(exact_hits),
            "duplicate_determinism_checks": tuple(duplicate_checks),
            "pass": exact,
        },
    }


def main() -> int:
    """The remaining certificates are added in the next incremental commit."""
    controls = source_controls()
    fixtures = decode_cycle830_fixtures()
    dynamics = evolve_s5_to_sstar_bound(fixtures)
    result = {
        "cycle": 840,
        "increment": "A_B_DYNAMICS_SCAFFOLD",
        "source_controls": controls["pass"],
        "fixtures": fixtures["public"]["pass"],
        "s5_dynamics": dynamics["public"]["pass"],
        "pass": (
            controls["pass"]
            and fixtures["public"]["pass"]
            and dynamics["public"]["pass"]
        ),
    }
    sys.stdout.write(compact(result) + "\n")
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
