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
EXPECTED_CYCLE838_K2_KEYS = (
    (2, (0, 5), 0),
    (2, (0, 5), 1),
    (2, (0, 5), 2),
    (2, (0, 6), 0),
    (2, (0, 6), 1),
    (2, (0, 6), 2),
)
DELAYED_KEYS = tuple(
    (event, pair)
    for event in (0, 1, 2)
    for pair in ((0, 5), (0, 6))
)
DELAYED_HORIZON_MOVEMENTS = 262144
EXPECTED_DELAYED_FUNNELS = {
    1: {
        "movement": 193210,
        "state_bit_tuple_sha256":
            "835170ded93f7f20c2aea6a09f637ff9cbea888d5676cb175510f0d3ade9ac0b",
        "hamming_weight": 52,
    },
    2: {
        "movement": 246669,
        "state_bit_tuple_sha256":
            "009fb7554ec831949e8cb3658c40d55affb0b6b9e66cf68229b9cd749418d3cd",
        "hamming_weight": 47,
    },
}
EXPECTED_EVENT0_HORIZON_STATE_SHA256 = (
    "c0a5c891f747369c925cadb48b0e20dc950c267d96277dd4d178cf369a931565"
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
    worktree_trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
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
        "cycle719_controller_basis": {
            "interleaved_program", "mapped_macro",
            "apply_controller_step", "run_orbit",
        } <= function_names(worktree_trees[AUDIT_INPUT_PATHS[0]]),
        "cycle822_family_and_predictor_basis": {
            "build_family", "sstar_anatomy", "entry_predictors",
        } <= function_names(worktree_trees[AUDIT_INPUT_PATHS[1]]),
        "cycle832_funnel_basis": {
            "build_seed_family", "packed_schedule",
            "advance", "funnel_anatomies",
        } <= function_names(worktree_trees[AUDIT_INPUT_PATHS[2]]),
        "cycle839_reimplementation_basis": {
            "decode_cycle830_fixtures", "build_phase_schedules",
            "apply_masked", "evolve_controller_ticks",
            "reachability_certificate",
        } <= function_names(historical_trees["cycle839_primary"]),
        "cycle838_delayed_basis": {
            "watched_residual_rows", "masked_schedule", "advance",
            "evolve", "optional_k2_certificate",
        } <= function_names(historical_trees["cycle838_primary"]),
        "cycle838_station0_literal_cohort":
            literal_assignment(
                historical_trees["cycle838_primary"],
                "K2_STATION0_S5_OPEN_THROUGH_T65536",
            ) == EXPECTED_CYCLE838_K2_KEYS,
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
        "pinned_historical_input_count": len(HISTORICAL_SOURCES),
        "total_source_primary_count":
            len(AUDIT_INPUT_PATHS) + len(HISTORICAL_SOURCES),
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
        and result["total_source_primary_count"] <= result["read_cap"]
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
    lane_keys = s5_keys + s5_keys
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
                "all_44_exact": all(
                    all(
                        ((column >> lane) & 1)
                        == ((column >> (lane + len(s5_keys))) & 1)
                        for column in columns
                    )
                    for lane in range(len(s5_keys))
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
        and all(row["all_44_exact"] for row in duplicate_checks)
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


def meeting_geometry(pair: Pair) -> dict[str, object]:
    left, right = pair
    if (right - left) % RING_STATIONS == 5:
        short_direction = 1
    elif (left - right) % RING_STATIONS == 5:
        short_direction = -1
    else:
        raise AssertionError(("not an s=5 pair", pair))
    short_arc = tuple(
        (left + short_direction * offset) % RING_STATIONS
        for offset in range(6)
    )
    long_arc = tuple(
        (left - short_direction * offset) % RING_STATIONS
        for offset in range(7)
    )
    short_centers = short_arc[2:4]
    long_centers = long_arc[3:4]
    centers = tuple(sorted(set(short_centers + long_centers)))
    reflection = lambda station: (left + right - station) % RING_STATIONS
    a_positions = tuple(
        (station + 3) % RING_STATIONS for station in pair
    )
    return {
        "short_arc_direction_from_sorted_left": short_direction,
        "sorted_gap": right - left,
        "short_arc": short_arc,
        "long_arc": long_arc,
        "meeting_times_short_long": (3, 3),
        "short_meeting_centers": short_centers,
        "long_meeting_center": long_centers,
        "meeting_center_union": centers,
        "center_sets_source_swap_reflection_symmetric": (
            {reflection(station) for station in short_centers}
            == set(short_centers)
            and {reflection(station) for station in long_centers}
            == set(long_centers)
        ),
        "A_token_positions_at_meet": a_positions,
        "B_token_positions_at_meet": (),
        "both_A_tokens_on_center_union": all(
            station in centers for station in a_positions
        ),
        "A_row_source_swap_reflection_symmetric":
            {reflection(station) for station in a_positions}
            == set(a_positions),
        "token_collision": len(set(a_positions)) != 2,
    }


def meeting_theorem_certificate() -> dict[str, object]:
    rows = []
    for separation in range(1, 6):
        short_time = (separation + 1) // 2
        long_time = (RING_STATIONS - separation + 1) // 2
        rows.append({
            "separation": separation,
            "arc_lengths": (separation, RING_STATIONS - separation),
            "meeting_times_short_long": (short_time, long_time),
            "tie": short_time == long_time,
        })
    s5_geometries = tuple(
        meeting_geometry(pair)
        for pair in lawful_pairs() if cyclic_separation(pair) == 5
    )
    exact = (
        tuple(
            row["meeting_times_short_long"] for row in rows
        ) == ((1, 5), (1, 5), (2, 4), (2, 4), (3, 3))
        and tuple(
            row["separation"] for row in rows if row["tie"]
        ) == (5,)
        and len(s5_geometries) == 11
        and all(
            row["center_sets_source_swap_reflection_symmetric"]
            and row["both_A_tokens_on_center_union"]
            and not row["A_row_source_swap_reflection_symmetric"]
            and not row["token_collision"]
            for row in s5_geometries
        )
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "per_separation_table": tuple(rows),
        "unique_tie_separation": 5,
        "theorem":
            "On C11, the two radius-one arc meetings occur at "
            "(ceil(s/2),ceil((11-s)/2)); the times tie at (3,3) iff s=5.",
        "meet_symmetry":
            "For every s=5 rotation/orientation, each auxiliary arc-center "
            "set is source-swap-reflection symmetric.  Both landed A tokens "
            "are on their three-station union at tick 3, although the actual "
            "two-token A row itself is not reflection symmetric.",
        "all_11_s5_geometries": s5_geometries,
        "pass": exact,
    }


def configuration_sha256(
    key: Key,
    state: int,
    geometry: dict[str, object],
) -> str:
    return digest((
        key,
        state_packed_sha256(state),
        geometry["A_token_positions_at_meet"],
        geometry["B_token_positions_at_meet"],
        geometry["meeting_center_union"],
    ))


def meet_prefix_pattern(state: int) -> tuple[str, str]:
    return (
        block_sha256(state, SOURCE_BLOCK),
        block_sha256(state, BANK0_BLOCK),
    )


def property_p(state: int) -> bool:
    return meet_prefix_pattern(state) in EXPECTED_MEET_PREFIX_PATTERNS


def certificate_a_split(
    fixtures: dict[str, object],
    dynamics: dict[str, object],
) -> dict[str, object]:
    keys = dynamics["keys"]
    meet_states = dynamics["meet_states"]
    exact_hits = dynamics["exact_hits"]
    target = fixtures["target"]
    assert isinstance(keys, tuple)
    assert isinstance(meet_states, tuple)
    assert isinstance(exact_hits, tuple)
    assert isinstance(target, int)
    hit_ticks = {
        key: tuple(
            tick for tick, hit_key in exact_hits if hit_key == key
        )
        for key in keys
    }
    rows = []
    for key, state in zip(keys, meet_states):
        event, pair = key
        geometry = meeting_geometry(pair)
        block_rows = tuple({
            "block": name,
            "range": block,
            "hamming_weight": block_value(state, block).bit_count(),
            "sha256": block_sha256(state, block),
        } for name, block in REGISTER_BLOCKS)
        ticks = hit_ticks[key]
        rows.append({
            "key": key,
            "event_index_embedded": event,
            "fixed_pair_word": pair,
            "origin_member": 0 in pair,
            "cyclic_separation": cyclic_separation(pair),
            "meet_controller_tick": 3,
            "meeting_centers": geometry["meeting_center_union"],
            "A_token_positions": geometry["A_token_positions_at_meet"],
            "B_token_positions": geometry["B_token_positions_at_meet"],
            "orientation": geometry[
                "short_arc_direction_from_sorted_left"
            ],
            "sorted_gap_parity": (pair[1] - pair[0]) % 2,
            "data_state_hamming_weight": state.bit_count(),
            "data_state_packed_sha256": state_packed_sha256(state),
            "register_blocks": block_rows,
            "meet_prefix_pattern": meet_prefix_pattern(state),
            "property_P": property_p(state),
            "configuration_sha256":
                configuration_sha256(key, state, geometry),
            "bounded_fate": (
                "REACHES_EXACT_SSTAR"
                if ticks else "NO_EXACT_SSTAR_WITHIN_BOUND"
            ),
            "exact_Sstar_hit_controller_ticks": ticks,
            "forward_bound_from_meet_controller_ticks":
                SSTAR_BOUND_CONTROLLER_TICKS - 3,
        })
    reaching = tuple(
        row["key"] for row in rows
        if row["bounded_fate"] == "REACHES_EXACT_SSTAR"
    )
    nonreaching = tuple(
        row["key"] for row in rows
        if row["bounded_fate"] == "NO_EXACT_SSTAR_WITHIN_BOUND"
    )
    exact = (
        fixtures["public"]["pass"]
        and dynamics["public"]["pass"]
        and len(rows) == 44
        and reaching == EXPECTED_REACHING_KEYS
        and len(nonreaching) == 35
        and tuple(exact_hits) == EXPECTED_CONTROLLER_TICK_HITS
        and all(row["cyclic_separation"] == 5 for row in rows)
        and all(
            row["forward_bound_from_meet_controller_ticks"]
            == SSTAR_BOUND_CONTROLLER_TICKS - 3
            for row in rows
        )
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "target": {
            "name": "exact Cycle-830 S*",
            "state_bits": STATE_BITS,
            "hamming_weight": target.bit_count(),
            "packed_sha256": state_packed_sha256(target),
            "bit_tuple_sha256": state_bit_tuple_sha256(target),
        },
        "meet_configuration_definition":
            "(embedded event index, fixed pair word, 5815-bit data state, "
            "A/B controller rails, auxiliary arc-center sets) at tick 3",
        "bounded_search":
            "Every completed controller tick from the tick-3 meet through "
            "tick 162129; exact 5815-bit equality, never weight alone.",
        "rows_44": tuple(rows),
        "reaching_keys": reaching,
        "reaching_count": len(reaching),
        "nonreaching_keys": nonreaching,
        "nonreaching_count": len(nonreaching),
        "partition": f"{len(reaching)}-vs-{len(nonreaching)}",
        "pass": exact,
    }


def structural_candidate_row(
    name: str,
    values: tuple[object, ...],
    labels: tuple[bool, ...],
    statement: str,
) -> dict[str, object]:
    positive = {
        compact(value) for value, label in zip(values, labels) if label
    }
    negative = {
        compact(value) for value, label in zip(values, labels) if not label
    }
    overlap = tuple(sorted(positive & negative))
    return {
        "candidate": name,
        "statement": statement,
        "positive_unique_value_count": len(positive),
        "negative_unique_value_count": len(negative),
        "positive_negative_overlap_count": len(overlap),
        "overlap_sha256": digest(overlap),
        "values_separate_classes_exactly": not overlap,
    }


def certificate_b_discriminator(
    certificate_a: dict[str, object],
    meeting: dict[str, object],
) -> dict[str, object]:
    rows = certificate_a["rows_44"]
    assert isinstance(rows, tuple)
    labels = tuple(
        row["bounded_fate"] == "REACHES_EXACT_SSTAR" for row in rows
    )
    candidates = (
        structural_candidate_row(
            "event_index",
            tuple(row["event_index_embedded"] for row in rows),
            labels,
            "embedded event index alone",
        ),
        structural_candidate_row(
            "origin_membership",
            tuple(row["origin_member"] for row in rows),
            labels,
            "fixed pair-word origin membership alone",
        ),
        structural_candidate_row(
            "source_register_block",
            tuple(row["register_blocks"][0]["sha256"] for row in rows),
            labels,
            "exact 41-bit source-register contents",
        ),
        structural_candidate_row(
            "bank0_register_block",
            tuple(row["register_blocks"][1]["sha256"] for row in rows),
            labels,
            "exact 131-bit bank-0 register contents",
        ),
        structural_candidate_row(
            "bank1_register_block",
            tuple(row["register_blocks"][2]["sha256"] for row in rows),
            labels,
            "exact 131-bit bank-1 register contents",
        ),
        structural_candidate_row(
            "link0_register_block",
            tuple(row["register_blocks"][3]["sha256"] for row in rows),
            labels,
            "exact 382-bit link-0 register contents",
        ),
        structural_candidate_row(
            "source_plus_bank0_register_blocks",
            tuple(row["meet_prefix_pattern"] for row in rows),
            labels,
            "joint exact contents of source and bank-0 at the meet",
        ),
        structural_candidate_row(
            "register_block_weight_tuple",
            tuple(tuple(
                block["hamming_weight"]
                for block in row["register_blocks"]
            ) for row in rows),
            labels,
            "source/bank0/bank1/link0 Hamming-weight tuple",
        ),
        structural_candidate_row(
            "token_charge_row_placement",
            tuple((
                row["A_token_positions"],
                row["B_token_positions"],
                row["meeting_centers"],
            ) for row in rows),
            labels,
            "A/B rail placement relative to the meet centers",
        ),
        structural_candidate_row(
            "parity_orientation",
            tuple((
                row["orientation"],
                row["sorted_gap_parity"],
                sum(row["meeting_centers"]) % 2,
            ) for row in rows),
            labels,
            "short-arc orientation and pair/center parity data",
        ),
    )
    property_keys = tuple(
        row["key"] for row in rows if row["property_P"]
    )
    reaching_keys = tuple(
        row["key"] for row, label in zip(rows, labels) if label
    )
    unified_predicate_keys = tuple(
        row["key"] for row in rows
        if (
            row["event_index_embedded"] == 0
            and not row["origin_member"]
            and row["cyclic_separation"] == 5
        )
    )
    observed_patterns = tuple(sorted({
        row["meet_prefix_pattern"] for row in rows if row["property_P"]
    }))
    expected_patterns = tuple(sorted(EXPECTED_MEET_PREFIX_PATTERNS))
    candidate_map = {
        row["candidate"]: row for row in candidates
    }
    exact = (
        certificate_a["pass"]
        and meeting["pass"]
        and property_keys == reaching_keys == EXPECTED_REACHING_KEYS
        and unified_predicate_keys == property_keys
        and observed_patterns == expected_patterns
        and candidate_map[
            "source_plus_bank0_register_blocks"
        ]["values_separate_classes_exactly"]
        and not candidate_map[
            "source_register_block"
        ]["values_separate_classes_exactly"]
        and not candidate_map[
            "bank0_register_block"
        ]["values_separate_classes_exactly"]
        and not candidate_map[
            "register_block_weight_tuple"
        ]["values_separate_classes_exactly"]
    )
    return {
        "verdict": "LINK_FOUND" if exact else "OPEN",
        "property_P":
            "At the tick-3 meet, the ordered (41-bit source register, "
            "131-bit bank-0 register) content has one of the four literal "
            "SHA-pinned patterns in EXPECTED_MEET_PREFIX_PATTERNS.",
        "property_P_pattern_count": len(EXPECTED_MEET_PREFIX_PATTERNS),
        "expected_patterns": EXPECTED_MEET_PREFIX_PATTERNS,
        "observed_property_patterns": observed_patterns,
        "candidate_table": candidates,
        "minimality_within_tested_block_family":
            "The joint source+bank0 content is exact; source alone, bank0 "
            "alone, every other individual active block, their weight tuple, "
            "rail placement, and parity/orientation all overlap the 35.",
        "both_directions": {
            "P_implies_bounded_Sstar_reach_on_44":
                property_keys == reaching_keys,
            "bounded_Sstar_reach_implies_P_on_44":
                reaching_keys == property_keys,
            "property_keys": property_keys,
            "reaching_keys": reaching_keys,
        },
        "mechanical_chain_on_44": {
            "meeting_theorem_unique_3_3_tie": meeting["pass"],
            "all_s5_meets_have_center_set_symmetry": all(
                geometry[
                    "center_sets_source_swap_reflection_symmetric"
                ]
                for geometry in meeting["all_11_s5_geometries"]
            ),
            "unified_entry_predicate_keys": unified_predicate_keys,
            "unified_predicate_iff_P":
                unified_predicate_keys == property_keys,
            "P_iff_bounded_funnel_reach":
                property_keys == reaching_keys,
        },
        "causal_boundary":
            "P is a finite exact meet-register discriminator and its "
            "sufficiency is established by the complete bounded evolution.  "
            "It is not yet a local update-rule theorem or an unbounded basin "
            "necessity theorem.",
        "pass": exact,
    }


def delayed_cohort_evolution(
    fixtures: dict[str, object],
) -> dict[str, object]:
    macros = fixtures["macros"]
    states = fixtures["states"]
    assert isinstance(macros, tuple)
    assert isinstance(states, dict)
    lane_keys = DELAYED_KEYS + DELAYED_KEYS
    columns = bit_slice(tuple(states[key] for key in lane_keys))
    schedule = build_movement_schedule(macros, lane_keys)
    capture_moments = tuple(sorted({
        DELAYED_HORIZON_MOVEMENTS,
        *(
            int(row["movement"])
            for row in EXPECTED_DELAYED_FUNNELS.values()
        ),
    }))
    captures = {}
    duplicate_checks = []
    for movement in range(1, DELAYED_HORIZON_MOVEMENTS + 1):
        apply_masked(columns, schedule)
        if movement in capture_moments:
            state_rows = capture_lanes(columns, len(lane_keys))
            captures[movement] = state_rows[:len(DELAYED_KEYS)]
            duplicate_checks.append({
                "movement": movement,
                "all_6_exact": all(
                    state_rows[lane]
                    == state_rows[lane + len(DELAYED_KEYS)]
                    for lane in range(len(DELAYED_KEYS))
                ),
            })
    expected_schedule_rows = tuple(sorted(set(
        sum(
            len(macros[
                (position + phase) % RING_STATIONS
            ])
            for phase in range(RING_STATIONS)
            for position in key[1]
        )
        for key in DELAYED_KEYS
    )))
    exact = (
        fixtures["public"]["pass"]
        and len(DELAYED_KEYS) == 6
        and set(captures) == set(capture_moments)
        and expected_schedule_rows == (WORD_GATE_COUNT,)
        and all(row["all_6_exact"] for row in duplicate_checks)
    )
    return {
        "captures": captures,
        "public": {
            "keys": DELAYED_KEYS,
            "Cycle838_key_encoding": EXPECTED_CYCLE838_K2_KEYS,
            "movement_horizon": DELAYED_HORIZON_MOVEMENTS,
            "movement_schedule_gate_rows": len(schedule),
            "per_lane_gate_rows_per_movement":
                expected_schedule_rows,
            "capture_moments": capture_moments,
            "duplicate_determinism_checks": tuple(duplicate_checks),
            "pass": exact,
        },
    }


def certificate_c_delayed(
    certificate_a: dict[str, object],
    delayed: dict[str, object],
) -> dict[str, object]:
    meet_rows = {
        row["key"]: row for row in certificate_a["rows_44"]
    }
    captures = delayed["captures"]
    assert isinstance(captures, dict)
    delayed_meets = tuple({
        "key": key,
        "meet_controller_tick": meet_rows[key]["meet_controller_tick"],
        "data_state_packed_sha256":
            meet_rows[key]["data_state_packed_sha256"],
        "meet_prefix_pattern": meet_rows[key]["meet_prefix_pattern"],
        "property_P": meet_rows[key]["property_P"],
        "origin_member": meet_rows[key]["origin_member"],
        "A_token_positions": meet_rows[key]["A_token_positions"],
        "meeting_centers": meet_rows[key]["meeting_centers"],
    } for key in DELAYED_KEYS)
    cohort_rows = []
    for event, expected in sorted(EXPECTED_DELAYED_FUNNELS.items()):
        movement = int(expected["movement"])
        event_indices = tuple(
            index for index, key in enumerate(DELAYED_KEYS)
            if key[0] == event
        )
        event_states = tuple(
            captures[movement][index] for index in event_indices
        )
        hashes = tuple(
            state_bit_tuple_sha256(state) for state in event_states
        )
        cohort_rows.append({
            "event": event,
            "geometry_pairs": tuple(
                DELAYED_KEYS[index][1] for index in event_indices
            ),
            "meet_states_equal_within_event": (
                len({
                    meet_rows[DELAYED_KEYS[index]][
                        "data_state_packed_sha256"
                    ]
                    for index in event_indices
                }) == 1
            ),
            "property_P_status": tuple(
                meet_rows[DELAYED_KEYS[index]]["property_P"]
                for index in event_indices
            ),
            "Cycle838_first_clean_movement": movement,
            "independent_trajectory_capture_movement": movement,
            "two_pair_states_exactly_equal": len(set(event_states)) == 1,
            "terminal_state_bit_tuple_sha256": hashes[0],
            "expected_terminal_state_bit_tuple_sha256":
                expected["state_bit_tuple_sha256"],
            "terminal_hamming_weight": event_states[0].bit_count(),
            "expected_terminal_hamming_weight":
                expected["hamming_weight"],
            "terminal_exact": (
                len(set(event_states)) == 1
                and len(set(hashes)) == 1
                and hashes[0] == expected["state_bit_tuple_sha256"]
                and event_states[0].bit_count()
                == expected["hamming_weight"]
            ),
        })
    event0_indices = tuple(
        index for index, key in enumerate(DELAYED_KEYS) if key[0] == 0
    )
    event0_horizon_states = tuple(
        captures[DELAYED_HORIZON_MOVEMENTS][index]
        for index in event0_indices
    )
    event0_meets = tuple(
        meet_rows[DELAYED_KEYS[index]] for index in event0_indices
    )
    accepted_source_hashes = {
        source_hash
        for source_hash, _bank0_hash in EXPECTED_MEET_PREFIX_PATTERNS
    }
    event0_origin_perturbation = {
        "keys": tuple(DELAYED_KEYS[index] for index in event0_indices),
        "source_register_still_in_entrant_source_class": all(
            row["register_blocks"][0]["sha256"]
            in accepted_source_hashes
            for row in event0_meets
        ),
        "joint_source_bank0_prefix_outside_P": all(
            not row["property_P"] for row in event0_meets
        ),
        "station0_pair_meet_states_equal":
            len({
                row["data_state_packed_sha256"]
                for row in event0_meets
            }) == 1,
        "horizon_movement": DELAYED_HORIZON_MOVEMENTS,
        "horizon_state_bit_tuple_sha256": tuple(
            state_bit_tuple_sha256(state)
            for state in event0_horizon_states
        ),
        "expected_horizon_state_bit_tuple_sha256":
            EXPECTED_EVENT0_HORIZON_STATE_SHA256,
        "horizon_hash_exact": all(
            state_bit_tuple_sha256(state)
            == EXPECTED_EVENT0_HORIZON_STATE_SHA256
            for state in event0_horizon_states
        ),
        "horizon_pair_states_equal":
            len(set(event0_horizon_states)) == 1,
        "full_configurations_still_distinct":
            len({
                DELAYED_KEYS[index][1] for index in event0_indices
            }) == 2,
        "Cycle838_status":
            "both event-0 station-0 keys remain open through movement 262144",
    }
    distinct_funnels = (
        len({
            row["terminal_state_bit_tuple_sha256"]
            for row in cohort_rows
        }) == len(cohort_rows) == 2
    )
    mechanical_exact = (
        certificate_a["pass"]
        and delayed["public"]["pass"]
        and len(delayed_meets) == 6
        and all(row["origin_member"] for row in delayed_meets)
        and not any(row["property_P"] for row in delayed_meets)
        and all(row["terminal_exact"] for row in cohort_rows)
        and all(
            row["meet_states_equal_within_event"] for row in cohort_rows
        )
        and distinct_funnels
        and event0_origin_perturbation[
            "source_register_still_in_entrant_source_class"
        ]
        and event0_origin_perturbation[
            "joint_source_bank0_prefix_outside_P"
        ]
        and event0_origin_perturbation["horizon_hash_exact"]
        and event0_origin_perturbation[
            "horizon_pair_states_equal"
        ]
        and event0_origin_perturbation[
            "full_configurations_still_distinct"
        ]
    )
    return {
        "verdict": "PARTIAL" if mechanical_exact else "FAILS",
        "pinned_Cycle838_scope":
            "the two station-0 s=5 geometries (0,5) and (0,6), for "
            "events 0,1,2",
        "delayed_meet_rows": delayed_meets,
        "resolved_event_cohorts": tuple(cohort_rows),
        "two_later_funnels_are_distinct": distinct_funnels,
        "event0_origin_isolation": event0_origin_perturbation,
        "account":
            "Origin membership changes bank-0 enough to move the event-0 "
            "meet prefix outside P while leaving its source-register class "
            "inside the entrant source class.  Events 1 and 2 also lie "
            "outside P and the two station-0 geometries synchronize only at "
            "the exact later Cycle-838 terminal states (movements 193210 "
            "and 246669), which are distinct funnels.  The event-0 projected "
            "data states coincide at movement 262144, but the fixed pair "
            "words keep the full configurations and next update words "
            "distinct; Cycle 838 therefore still finds both open.",
        "why_not_HOLDS":
            "The register displacement classifies the delay and reproduces "
            "the two later terminal states, but no local theorem derives "
            "either waiting time or funnel identity from the displaced "
            "bank-0 contents.  Cycle-838 first-clean minimality is source-"
            "pinned rather than independently rescanned here.",
        "pass": mechanical_exact,
    }


def certificate_d_verdict(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
    certificate_c: dict[str, object],
) -> dict[str, object]:
    closed_44 = (
        certificate_a["pass"]
        and certificate_b["pass"]
        and certificate_b["verdict"] == "LINK_FOUND"
        and certificate_b["mechanical_chain_on_44"][
            "unified_predicate_iff_P"
        ]
        and certificate_b["mechanical_chain_on_44"][
            "P_iff_bounded_funnel_reach"
        ]
    )
    if closed_44 and certificate_c["verdict"] == "HOLDS":
        verdict = "CAUSAL_CHAIN_CLOSED"
    elif closed_44 and certificate_c["pass"]:
        verdict = "LINK_FOUND_CHAIN_PARTIAL"
    else:
        verdict = "OPEN"
    exact = (
        closed_44
        and certificate_c["pass"]
        and certificate_c["verdict"] == "PARTIAL"
        and verdict == "LINK_FOUND_CHAIN_PARTIAL"
    )
    return {
        "verdict": verdict,
        "44_key_loop_closed_mechanically": closed_44,
        "delayed_account": certificate_c["verdict"],
        "causal_chain_closed": verdict == "CAUSAL_CHAIN_CLOSED",
        "sharp_reading":
            "The missing finite meet-level link is found exactly: P is "
            "equivalent to the nine bounded S* entrants on all 44 and to the "
            "unified entry predicate.  The broader causal chain remains "
            "partial because P is a four-pattern finite discriminator, not "
            "a local rule theorem, and the origin-shifted register content "
            "does not derive the delayed waiting times or terminal identities.",
        "pass": exact,
    }


def render(
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    return "\n".join((
        *(
            f"CERTIFICATE {name} {compact(value)}"
            for name, value in certificates.items()
        ),
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    )) + "\n"


def stable_render(
    certificates: dict[str, object],
    checks: dict[str, bool],
    report: dict[str, object],
    controls_base: bool,
) -> str:
    controls = certificates["E_CONTROLS"]
    assert isinstance(controls, dict)
    for _attempt in range(20):
        controls["pass"] = (
            controls_base
            and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        checks["E_CONTROLS"] = bool(controls["pass"])
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE840_LINK_FOUND_CHAIN_PARTIAL_PASS"
            if (
                report["pass"]
                and report["verdict"] == "LINK_FOUND_CHAIN_PARTIAL"
            )
            else "CYCLE840_MISSING_LINK_HONEST_FAIL"
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
    controls = source_controls()
    fixtures = decode_cycle830_fixtures()
    dynamics = evolve_s5_to_sstar_bound(fixtures)
    meeting = meeting_theorem_certificate()
    certificate_a = certificate_a_split(fixtures, dynamics)
    certificate_b = certificate_b_discriminator(certificate_a, meeting)
    delayed = delayed_cohort_evolution(fixtures)
    certificate_c = certificate_c_delayed(certificate_a, delayed)
    certificate_d = certificate_d_verdict(
        certificate_a, certificate_b, certificate_c
    )
    deterministic = (
        all(
            row["all_44_exact"]
            for row in dynamics["public"][
                "duplicate_determinism_checks"
            ]
        )
        and all(
            row["all_6_exact"]
            for row in delayed["public"]["duplicate_determinism_checks"]
        )
    )
    elapsed = monotonic() - started
    controls.update({
        "source_controls_pass": controls["pass"],
        "fixture_provenance": fixtures["public"],
        "Cycle839_reimplementation": dynamics["public"],
        "Cycle838_delayed_reimplementation": delayed["public"],
        "blocked_modules_loaded_at_end": tuple(sorted(
            name for name in sys.modules
            if name.rsplit(".", 1)[-1] in {
                Path(path).stem for path in AUDIT_INPUT_PATHS
            } | {
                Path(path).stem
                for _label, _commit, path, _sha, _blob
                in HISTORICAL_SOURCES
            }
        )),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "exact_arithmetic":
            "Graph arcs, Boolean X/CNOT/Toffoli gates, bit slices, complete "
            "integer movement/tick bounds, 5815-bit equality, counts, and "
            "SHA digests use exact Python integers/bytes/sets.  Only "
            "monotonic wall runtime is floating point.",
        "determinism": {
            "method":
                "in-run duplicate lanes for every one of the 44 s=5 keys "
                "and all six Cycle-838 station-0 cohort keys",
            "s5_all_44_duplicate_checks":
                dynamics["public"]["duplicate_determinism_checks"],
            "delayed_all_6_duplicate_checks":
                delayed["public"]["duplicate_determinism_checks"],
            "exact": deterministic,
        },
        "certificate_digest_sha256": digest((
            meeting,
            certificate_a,
            certificate_b,
            certificate_c,
            certificate_d,
            dynamics["public"],
            delayed["public"],
        )),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "user_runtime_ceiling_seconds": 1500,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    })
    controls_base = (
        controls["source_controls_pass"]
        and fixtures["public"]["pass"]
        and dynamics["public"]["pass"]
        and delayed["public"]["pass"]
        and meeting["pass"]
        and certificate_a["pass"]
        and certificate_b["pass"]
        and certificate_c["pass"]
        and certificate_d["pass"]
        and deterministic
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC < 1500
    )
    certificates = {
        "A_44_WAY_SPLIT": certificate_a,
        "B_MEET_DISCRIMINATOR": {
            "meeting_theorem": meeting,
            **certificate_b,
        },
        "C_DELAYED_COHORTS": certificate_c,
        "D_VERDICT": certificate_d,
        "E_CONTROLS": controls,
    }
    checks = {
        "A_EXACT_9_VS_35": bool(
            certificate_a["pass"]
            and certificate_a["partition"] == "9-vs-35"
        ),
        "B_EXACT_DISCRIMINATOR": bool(
            certificate_b["pass"]
            and certificate_b["verdict"] == "LINK_FOUND"
        ),
        "C_DELAY_ACCOUNT_PARTIAL": bool(
            certificate_c["pass"]
            and certificate_c["verdict"] == "PARTIAL"
        ),
        "D_LINK_FOUND_CHAIN_PARTIAL": bool(
            certificate_d["pass"]
            and certificate_d["verdict"]
            == "LINK_FOUND_CHAIN_PARTIAL"
        ),
        "E_CONTROLS": False,
        "FULL_DUPLICATE_DETERMINISM": deterministic,
        "RUNTIME_BOUND": elapsed < AUDIT_TIMEOUT_SEC,
    }
    report = {
        "cycle": 840,
        "stage": "certificates-A-B-C-D-E",
        "partition": certificate_a["partition"],
        "reaching_count": certificate_a["reaching_count"],
        "nonreaching_count": certificate_a["nonreaching_count"],
        "discriminator": certificate_b["verdict"],
        "property_P": certificate_b["property_P"],
        "44_key_loop_closed_mechanically":
            certificate_d["44_key_loop_closed_mechanically"],
        "delayed_account": certificate_c["verdict"],
        "delayed_funnel_moments": tuple(
            (
                row["event"],
                row["Cycle838_first_clean_movement"],
                row["terminal_state_bit_tuple_sha256"],
            )
            for row in certificate_c["resolved_event_cohorts"]
        ),
        "verdict": certificate_d["verdict"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE840_MISSING_LINK_HONEST_FAIL",
    }
    output = stable_render(
        certificates, checks, report, controls_base
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
            "terminal": "CYCLE840_MISSING_LINK_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
