#!/usr/bin/env python3
"""Cycle 842: rule-local wire dynamics and bounded causal-theorem attempt.

The source primaries named below are read as text/AST only.  Literal fixtures
are copied from a SHA-pinned git object and decoded here; no primary is
imported or executed.  All Boolean evolution is independently reimplemented
with Python integers.
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
MEET_CONTROLLER_TICK = 3
FORWARD_BOUND_FROM_MEET = (
    SSTAR_BOUND_CONTROLLER_TICKS - MEET_CONTROLLER_TICK
)
DISCRIMINATOR_WIRES = (40, 81, 105)
DISCRIMINATOR_PATTERNS = (
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 0),
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
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR22-20260729"
EXPECTED_BASE = "0eb7ca451782f17fed6473f786da09a7d40e995e"
HISTORICAL_SOURCES = (
    (
        "cycle830_fixture_primary",
        "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
        "98b1571228ad0902301b6853208ef249ea2c2973",
    ),
    (
        "cycle839_meeting_primary",
        EXPECTED_BASE,
        "scripts/frontier_cycle839_meeting_derivation_2026_07_28.py",
        "bba2ce68e34bb6c502681c201ba83666e9f674aea2606ced4e3f894fdadfe4fa",
        "9289962e4cdd24732a9c5d1ea53b360d236948f8",
    ),
    (
        "cycle840_representation_primary",
        "293c666cd22da9cfa6352fafd73a57bbe5492f05",
        "scripts/frontier_cycle840_missing_link_2026_07_28.py",
        "6b87eea4bf26e3c261b84597512d2177406c5875a8c0b6ad5af549f208fd7f19",
        "0b7375692320b50b68516af61ecbc53526f47145",
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

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]

BLOCKLISTED_MODULES = tuple(sorted({
    Path(path).stem for path in AUDIT_INPUT_PATHS
} | {
    Path(path).stem
    for _name, _commit, path, _sha, _blob in HISTORICAL_SOURCES
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
    historical_rows = []
    historical_trees = {}
    for name, commit, path, expected_sha, expected_blob in HISTORICAL_SOURCES:
        spec = f"{commit}:{path}"
        payload = git_bytes("show", spec)
        tree = ast.parse(payload, filename=spec)
        historical_trees[name] = tree
        observed_blob = git_text("rev-parse", spec)
        historical_rows.append({
            "name": name,
            "commit": commit,
            "path": path,
            "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": expected_sha,
            "git_blob": observed_blob,
            "expected_git_blob": expected_blob,
            "exact": (
                sha256(payload).hexdigest() == expected_sha
                and observed_blob == expected_blob
            ),
        })
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
    ast_basis = {
        "cycle719_controller_basis": {
            "mapped_macro", "apply_controller_step", "run_orbit",
        } <= function_names(worktree_trees[AUDIT_INPUT_PATHS[0]]),
        "cycle822_funnel_basis": {
            "build_family", "sstar_anatomy", "entry_predictors",
        } <= function_names(worktree_trees[AUDIT_INPUT_PATHS[1]]),
        "cycle832_moment_basis": {
            "packed_schedule", "advance", "funnel_anatomies",
        } <= function_names(worktree_trees[AUDIT_INPUT_PATHS[2]]),
        "cycle830_literal_fixtures": all(
            literal_assignment(
                historical_trees["cycle830_fixture_primary"], name
            ) is not None
            for name in (
                "GATE_CONSTANTS_B85", "FAMILY_STATES_B85",
                "SSTAR_PACKED_B85",
            )
        ),
        "cycle839_meeting_and_reach_basis": {
            "meeting_theorem_certificate", "reachability_certificate",
            "build_phase_schedules", "apply_masked",
        } <= function_names(
            historical_trees["cycle839_meeting_primary"]
        ),
        "cycle840_three_wire_basis": {
            "discriminator_pattern", "discriminator_d",
            "reconstruct_minimal_discriminator",
            "certificate_b_representation",
        } <= function_names(
            historical_trees["cycle840_representation_primary"]
        ),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "read_cap": 7,
        "named_worktree_input_count": len(AUDIT_INPUT_PATHS),
        "pinned_historical_copy_count": len(HISTORICAL_SOURCES),
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
            if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
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


def decode_cycle830_fixtures() -> dict[str, object]:
    name, commit, path, expected_source_sha, expected_source_blob = (
        HISTORICAL_SOURCES[0]
    )
    assert name == "cycle830_fixture_primary"
    spec = f"{commit}:{path}"
    source = git_bytes("show", spec)
    tree = ast.parse(source, filename=spec)
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
    exact = (
        sha256(source).hexdigest() == expected_source_sha
        and git_text("rev-parse", spec) == expected_source_blob
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
            "source_spec": spec,
            "source_sha256": sha256(source).hexdigest(),
            "source_git_blob": git_text("rev-parse", spec),
            "macro_gate_counts": lengths,
            "macro_gate_count": sum(lengths),
            "family_key_count": len(states),
            "target_hamming_weight": target.bit_count(),
            "target_packed_sha256": state_packed_sha256(target),
            "pass": exact,
        },
    }


def gate_clause(gate: Gate) -> tuple[str, tuple[int, ...], int, str]:
    kind, first, second, third = gate
    if kind == 0:
        return ("X", (), first, f"x[{first}] ^= 1")
    if kind == 1:
        return (
            "CNOT", (first,), second,
            f"x[{second}] ^= x[{first}]",
        )
    if kind == 2:
        return (
            "TOFFOLI", (first, second), third,
            f"x[{third}] ^= x[{first}] & x[{second}]",
        )
    raise AssertionError(("unknown gate kind", kind))


def certificate_a_wire_dynamics(
    fixtures: dict[str, object],
) -> dict[str, object]:
    macros = fixtures["macros"]
    assert isinstance(macros, tuple)
    touching_rows = []
    per_wire = {}
    for wire in DISCRIMINATOR_WIRES:
        rows = []
        for station, macro in enumerate(macros):
            for clause_index, gate in enumerate(macro):
                kind, controls, target, formula = gate_clause(gate)
                roles = []
                if wire in controls:
                    roles.append("READ_CONTROL")
                if wire == target:
                    roles.append("WRITE_TARGET")
                if roles:
                    row = {
                        "wire": wire,
                        "station": station,
                        "clause_index_zero_based": clause_index,
                        "gate_kind": kind,
                        "controls": controls,
                        "target": target,
                        "wire_roles": tuple(roles),
                        "exact_update": formula,
                    }
                    rows.append(row)
                    touching_rows.append(row)
        read_targets = tuple(sorted({
            int(row["target"]) for row in rows
            if "READ_CONTROL" in row["wire_roles"]
        }))
        write_controls = tuple(sorted({
            int(control)
            for row in rows
            if "WRITE_TARGET" in row["wire_roles"]
            for control in row["controls"]
        }))
        per_wire[wire] = {
            "wire": wire,
            "read_clause_count": sum(
                "READ_CONTROL" in row["wire_roles"] for row in rows
            ),
            "write_clause_count": sum(
                "WRITE_TARGET" in row["wire_roles"] for row in rows
            ),
            "read_influence_targets": read_targets,
            "write_dependency_controls": write_controls,
            "one_macro_orbit_neighborhood": tuple(sorted(
                {wire} | set(read_targets) | set(write_controls)
            )),
            "touching_rule_clauses": tuple(rows),
        }
    kind_counts = Counter(
        str(row["gate_kind"]) for row in touching_rows
    )
    exact = (
        fixtures["public"]["pass"]
        and sum(len(macro) for macro in macros) == GATE_COUNT
        and all(per_wire[wire]["touching_rule_clauses"]
                for wire in DISCRIMINATOR_WIRES)
        and len(touching_rows) == len({
            (
                row["wire"], row["station"],
                row["clause_index_zero_based"], row["wire_roles"],
            )
            for row in touching_rows
        })
    )
    return {
        "verdict": "WIRE_DYNAMICS_EXACT" if exact else "FAIL",
        "certificate_role": "A_WIRE_DYNAMICS",
        "wire_numbering":
            "zero-based bits of the packed 5815-bit landed data integer",
        "landed_clause_semantics": {
            "kind_0": "X: target ^= 1",
            "kind_1": "CNOT: target ^= control",
            "kind_2": "TOFFOLI: target ^= control_0 & control_1",
            "within_macro_order": "stored clause order",
            "controller_order":
                "at phase q, apply the macros at the two live A-token "
                "stations in station order; then both token positions "
                "common-translate by +1",
        },
        "per_wire": tuple(per_wire[wire] for wire in DISCRIMINATOR_WIRES),
        "touching_row_count": len(touching_rows),
        "touching_gate_kind_counts": tuple(sorted(kind_counts.items())),
        "scope":
            "all 3106 clauses in all 11 landed station macros; exact "
            "read/write incidence for wires 40/81/105",
        "pass": exact,
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
        candidates &= (
            column if (target >> wire) & 1 else lane_mask ^ column
        )
        if not candidates:
            return 0
    for wire in range(STATE_BITS):
        column = columns[wire] & lane_mask
        candidates &= (
            column if (target >> wire) & 1 else lane_mask ^ column
        )
        if not candidates:
            return 0
    return candidates


def discriminator_pattern_from_state(state: int) -> tuple[int, ...]:
    return tuple(
        (state >> wire) & 1 for wire in DISCRIMINATOR_WIRES
    )


def discriminator_mask(columns: list[int], lane_mask: int) -> int:
    c40, c81, c105 = (
        columns[wire] & lane_mask for wire in DISCRIMINATOR_WIRES
    )
    n40 = lane_mask ^ c40
    n81 = lane_mask ^ c81
    n105 = lane_mask ^ c105
    return (
        (n40 & n81 & n105)
        | (n40 & c81 & c105)
        | (c40 & n81 & n105)
    )


def pattern_columns(
    columns: list[int],
    lane: int,
) -> tuple[int, ...]:
    return tuple(
        (columns[wire] >> lane) & 1 for wire in DISCRIMINATOR_WIRES
    )


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
    reflection = lambda station: (
        left + right - station
    ) % RING_STATIONS
    a_positions = tuple(
        (station + MEET_CONTROLLER_TICK) % RING_STATIONS
        for station in pair
    )
    return {
        "short_arc_direction_from_sorted_left": short_direction,
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
        "token_collision": len(set(a_positions)) != 2,
    }


def evolve_bounded_forward(
    fixtures: dict[str, object],
) -> dict[str, object]:
    """Execute the full 44-member s=5 census and collect falsifiers."""
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
    lane_count = len(s5_keys)
    lane_keys = s5_keys + s5_keys
    columns = bit_slice(tuple(states[key] for key in lane_keys))
    schedules = build_phase_schedules(macros, lane_keys)
    primary_mask = (1 << lane_count) - 1
    duplicate_mask = primary_mask << lane_count
    signature = tuple(sorted(set(
        tuple(
            wire for wire in range(STATE_BITS)
            if (target >> wire) & 1
        ) + tuple(
            index * (STATE_BITS - 1) // 191 for index in range(192)
        )
    )))
    schedule_duplicate_exact = all(
        ((mask & duplicate_mask) >> lane_count)
        == (mask & primary_mask)
        for schedule in schedules
        for _kind, _first, _second, _third, mask in schedule
    )
    per_lane_gate_rows = [0] * len(lane_keys)
    for schedule in schedules:
        for _kind, _first, _second, _third, mask in schedule:
            live = mask
            while live:
                bit = live & -live
                per_lane_gate_rows[bit.bit_length() - 1] += 1
                live ^= bit
    meet_states: tuple[int, ...] | None = None
    meet_patterns: tuple[tuple[int, ...], ...] | None = None
    meet_d_mask: int | None = None
    first_pattern_change: list[dict[str, object] | None] = (
        [None] * lane_count
    )
    first_d_change: list[dict[str, object] | None] = [None] * lane_count
    first_hamming_increase: list[dict[str, object] | None] = (
        [None] * lane_count
    )
    previous_distances: tuple[int, ...] | None = None
    exact_hits = []
    duplicate_checkpoints = []
    hamming_window_end = 64

    for tick in range(1, SSTAR_BOUND_CONTROLLER_TICKS + 1):
        apply_masked(columns, schedules[(tick - 1) % RING_STATIONS])
        if tick == MEET_CONTROLLER_TICK:
            meet_states = capture_lanes(columns, lane_count)
            meet_patterns = tuple(
                discriminator_pattern_from_state(state)
                for state in meet_states
            )
            meet_d_mask = discriminator_mask(columns, primary_mask)
        if tick in (
            MEET_CONTROLLER_TICK,
            SSTAR_BOUND_CONTROLLER_TICKS,
        ):
            duplicate_checkpoints.append({
                "controller_tick": tick,
                "all_44_exact": all(
                    (column & primary_mask)
                    == ((column & duplicate_mask) >> lane_count)
                    for column in columns
                ),
            })
        if (
            meet_patterns is not None
            and meet_d_mask is not None
            and tick > MEET_CONTROLLER_TICK
        ):
            current_d_mask = discriminator_mask(columns, primary_mask)
            changed_d = current_d_mask ^ meet_d_mask
            for lane in lane_numbers(changed_d):
                if first_d_change[lane] is None:
                    first_d_change[lane] = {
                        "controller_tick": tick,
                        "from": bool((meet_d_mask >> lane) & 1),
                        "to": bool((current_d_mask >> lane) & 1),
                        "pattern": pattern_columns(columns, lane),
                    }
            for lane, initial_pattern in enumerate(meet_patterns):
                if first_pattern_change[lane] is None:
                    current_pattern = pattern_columns(columns, lane)
                    if current_pattern != initial_pattern:
                        first_pattern_change[lane] = {
                            "controller_tick": tick,
                            "from": initial_pattern,
                            "to": current_pattern,
                        }
        if MEET_CONTROLLER_TICK <= tick <= hamming_window_end:
            snapshot = capture_lanes(columns, lane_count)
            distances = tuple(
                (state ^ target).bit_count() for state in snapshot
            )
            if previous_distances is not None:
                for lane, (before, after) in enumerate(zip(
                    previous_distances, distances
                )):
                    if (
                        after > before
                        and first_hamming_increase[lane] is None
                    ):
                        first_hamming_increase[lane] = {
                            "from_tick": tick - 1,
                            "to_tick": tick,
                            "from_distance": before,
                            "to_distance": after,
                            "increase": after - before,
                        }
            previous_distances = distances
        matches = matching_mask(
            columns, target, primary_mask, signature
        )
        exact_hits.extend(
            (tick, s5_keys[lane]) for lane in lane_numbers(matches)
        )

    if (
        meet_states is None
        or meet_patterns is None
        or meet_d_mask is None
    ):
        raise AssertionError("tick-3 meet snapshot missing")
    hit_ticks = {
        key: tuple(
            tick for tick, hit_key in exact_hits if hit_key == key
        )
        for key in s5_keys
    }
    rows = tuple({
        "key": key,
        "meet_pattern": meet_patterns[lane],
        "meet_D": bool((meet_d_mask >> lane) & 1),
        "meet_state_packed_sha256": state_packed_sha256(
            meet_states[lane]
        ),
        "meet_state_hamming_weight": meet_states[lane].bit_count(),
        "meeting_geometry": meeting_geometry(key[1]),
        "first_pattern_change": first_pattern_change[lane],
        "first_D_change": first_d_change[lane],
        "first_hamming_distance_increase_through_tick_64":
            first_hamming_increase[lane],
        "exact_Sstar_hit_ticks": hit_ticks[key],
        "reaches_within_bound": bool(hit_ticks[key]),
        "first_hit_distance_from_meet": (
            hit_ticks[key][0] - MEET_CONTROLLER_TICK
            if hit_ticks[key] else None
        ),
    } for lane, key in enumerate(s5_keys))
    reaching_keys = tuple(
        row["key"] for row in rows if row["reaches_within_bound"]
    )
    marked_keys = tuple(row["key"] for row in rows if row["meet_D"])
    nonreaching_keys = tuple(
        row["key"] for row in rows if not row["reaches_within_bound"]
    )
    exact = (
        fixtures["public"]["pass"]
        and lane_count == 44
        and tuple(exact_hits) == EXPECTED_CONTROLLER_TICK_HITS
        and reaching_keys == EXPECTED_REACHING_KEYS
        and marked_keys == EXPECTED_REACHING_KEYS
        and len(nonreaching_keys) == 35
        and schedule_duplicate_exact
        and all(
            row["all_44_exact"] for row in duplicate_checkpoints
        )
        and set(per_lane_gate_rows) == {WORD_GATE_COUNT}
        and all(
            row["meeting_geometry"][
                "center_sets_source_swap_reflection_symmetric"
            ]
            and row["meeting_geometry"][
                "both_A_tokens_on_center_union"
            ]
            and not row["meeting_geometry"]["token_collision"]
            for row in rows
        )
    )
    return {
        "rows": rows,
        "keys": s5_keys,
        "meet_states": meet_states,
        "public": {
            "scope":
                "all 44 landed s=5 configurations; every completed "
                "controller tick 1..162129",
            "meet_controller_tick": MEET_CONTROLLER_TICK,
            "forward_bound_from_meet_controller_ticks":
                FORWARD_BOUND_FROM_MEET,
            "forward_bound_complete_movements":
                SSTAR_BOUND_MOVEMENTS,
            "exact_target_definition": {
                "state_bits": STATE_BITS,
                "hamming_weight": target.bit_count(),
                "packed_sha256": state_packed_sha256(target),
                "bit_tuple_sha256": state_bit_tuple_sha256(target),
            },
            "phase_schedule_gate_rows": tuple(map(len, schedules)),
            "per_lane_gate_rows_per_complete_movement":
                tuple(sorted(set(per_lane_gate_rows))),
            "structural_duplicate_schedule_exact":
                schedule_duplicate_exact,
            "duplicate_determinism_checkpoints":
                tuple(duplicate_checkpoints),
            "all_exact_target_hits": tuple(exact_hits),
            "marked_keys": marked_keys,
            "reaching_keys": reaching_keys,
            "nonreaching_keys": nonreaching_keys,
            "pass": exact,
        },
    }


def certificate_b_forward_argument(
    certificate_a: dict[str, object],
    evolution: dict[str, object],
) -> dict[str, object]:
    rows = evolution["rows"]
    assert isinstance(rows, tuple)
    marked = tuple(row for row in rows if row["meet_D"])
    controls = tuple(row for row in rows if not row["meet_D"])
    marked_pattern_changes = tuple({
        "key": row["key"],
        "counterexample": row["first_pattern_change"],
    } for row in marked if row["first_pattern_change"] is not None)
    marked_d_changes = tuple({
        "key": row["key"],
        "counterexample": row["first_D_change"],
    } for row in marked if row["first_D_change"] is not None)
    marked_hamming_failures = tuple({
        "key": row["key"],
        "counterexample":
            row["first_hamming_distance_increase_through_tick_64"],
    } for row in marked if (
        row["first_hamming_distance_increase_through_tick_64"]
        is not None
    ))
    control_hamming_failures = tuple({
        "key": row["key"],
        "counterexample":
            row["first_hamming_distance_increase_through_tick_64"],
    } for row in controls if (
        row["first_hamming_distance_increase_through_tick_64"]
        is not None
    ))
    finite_implication = (
        len(marked) == 9
        and all(row["reaches_within_bound"] for row in marked)
        and all(
            row["first_hit_distance_from_meet"] is not None
            and 0 <= row["first_hit_distance_from_meet"]
            <= FORWARD_BOUND_FROM_MEET
            for row in marked
        )
    )
    negative_control_exact = (
        len(controls) == 35
        and not any(row["reaches_within_bound"] for row in controls)
    )
    hamming_candidate_falsified = (
        bool(marked_hamming_failures)
        and bool(control_hamming_failures)
    )
    local_flag_conservation_falsified = bool(
        marked_pattern_changes or marked_d_changes
    )
    exact = (
        certificate_a["pass"]
        and evolution["public"]["pass"]
        and finite_implication
        and negative_control_exact
        and hamming_candidate_falsified
        and local_flag_conservation_falsified
    )
    return {
        "verdict": "BOUNDED_FORWARD_IMPLICATION_WITH_LOCAL_GAP",
        "certificate_role": "B_FORWARD_ARGUMENT_ATTEMPT",
        "theorem_scope":
            "the finite landed 44-member s=5 tick-3 meet domain",
        "antecedent":
            "symmetric (3,3) meet geometry AND meet-wire pattern on "
            "(40,81,105) in {000,011,100}",
        "conclusion":
            "exact 5815-bit weight-44 Cycle-830 S* is reached within "
            f"B={FORWARD_BOUND_FROM_MEET} completed controller ticks",
        "bound_B_controller_ticks": FORWARD_BOUND_FROM_MEET,
        "rule_level_bounded_forward_census": {
            "marked_trajectory_count": len(marked),
            "all_marked_reach_exact_target": finite_implication,
            "marked_rows": tuple({
                "key": row["key"],
                "meet_pattern": row["meet_pattern"],
                "first_hit_distance_from_meet":
                    row["first_hit_distance_from_meet"],
                "exact_Sstar_hit_ticks": row["exact_Sstar_hit_ticks"],
            } for row in marked),
            "every_rule_tick_checked": True,
            "target_comparison": "exact 5815-bit equality, not weight alone",
        },
        "candidate_invariant_chain": (
            {
                "link": "meet predicate is locally readable",
                "status": "PASS",
                "evidence":
                    "exact three-wire evaluation on all 44 meet states",
            },
            {
                "link": "three-wire word or Boolean D is conserved",
                "status": "FAIL",
                "marked_pattern_counterexamples":
                    marked_pattern_changes,
                "marked_D_counterexamples": marked_d_changes,
            },
            {
                "link": "Hamming distance to exact S* is nonincreasing",
                "status": "FAIL",
                "checked_window":
                    "every tick from meet tick 3 through tick 64",
                "marked_counterexamples": marked_hamming_failures,
                "nonreaching_counterexamples":
                    control_hamming_failures,
            },
            {
                "link":
                    "full deterministic landed evolution forces S* "
                    "within B on each marked meet",
                "status": "PASS",
                "evidence":
                    "all nine marked lanes, every tick, exact target",
            },
            {
                "link":
                    "a non-lookahead local invariant/monotone connects "
                    "the three-wire flag to the target skeleton",
                "status": "OPEN",
                "reason":
                    "the tested local flag is writable/nonconserved and "
                    "the tested target-distance monotone has explicit "
                    "counterexamples",
            },
        ),
        "lookahead_distance_certificate": {
            "definition":
                "first exact future S* hit tick minus current tick",
            "marked_meet_values": tuple(
                (row["key"], row["first_hit_distance_from_meet"])
                for row in marked
            ),
            "decreases_by_one_until_hit":
                all(row["first_hit_distance_from_meet"] is not None
                    for row in marked),
            "admissibility":
                "EXACT_BUT_LOOKAHEAD_DEFINED; certifies the finite "
                "implication but is not a local causal explanation",
        },
        "declared_nonreaching_control_sample": {
            "sampling_rule": "all 35 unmarked members of the landed s=5 census",
            "sample_size": len(controls),
            "sample_keys": tuple(row["key"] for row in controls),
            "no_exact_target_within_B": negative_control_exact,
            "lookahead_distance_absent": all(
                row["first_hit_distance_from_meet"] is None
                for row in controls
            ),
            "hamming_monotone_failure_count":
                len(control_hamming_failures),
        },
        "pass": exact,
    }


def certificate_c_verdict(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
) -> dict[str, object]:
    partial = certificate_a["pass"] and certificate_b["pass"]
    return {
        "verdict": "PARTIAL" if partial else "OPEN",
        "certificate_role": "C_LOCAL_CAUSAL_THEOREM_VERDICT",
        "links_that_hold": (
            "exact local read/write dynamics for wires 40/81/105",
            "exact meet-local predicate on the finite landed 44-member domain",
            f"marked-meet => exact S* within B={FORWARD_BOUND_FROM_MEET} "
            "by exhaustive rule-level bounded-forward execution",
            "all 35 unmarked controls fail to reach exact S* within B",
        ),
        "open_link":
            "No non-lookahead local invariant/monotone has been derived "
            "from the three writable wires and symmetric meet geometry to "
            "the weight-44 skeleton.",
        "why_not_LOCAL_THEOREM_ESTABLISHED":
            "The finite implication is machine-proved, but the requested "
            "local causal proof skeleton does not close: D is not conserved "
            "and Hamming distance to S* is not monotone.",
        "status_precision":
            "PARTIAL does not retract the bounded 9/44 reachability theorem; "
            "it withholds the stronger local causal explanation.",
        "pass": partial,
    }


def run() -> int:
    started = monotonic()
    controls = source_controls()
    fixtures = decode_cycle830_fixtures()
    certificate_a = certificate_a_wire_dynamics(fixtures)
    evolution = evolve_bounded_forward(fixtures)
    certificate_b = certificate_b_forward_argument(
        certificate_a, evolution
    )
    certificate_c = certificate_c_verdict(certificate_a, certificate_b)
    report = {
        "cycle": 842,
        "title": "the local causal theorem attempt",
        "certificate_A": certificate_a,
        "certificate_B": certificate_b,
        "certificate_C": certificate_c,
        "bounded_evolution": evolution["public"],
        "certificate_D_controls": controls,
        "elapsed_seconds": round(monotonic() - started, 6),
        "overall_pass": (
            controls["pass"]
            and certificate_a["pass"]
            and certificate_b["pass"]
            and certificate_c["pass"]
        ),
    }
    rendered = compact(report)
    if len(rendered.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    print(rendered)
    return 0 if report["overall_pass"] else 1


def main() -> int:
    started = monotonic()
    code = run()
    if monotonic() - started >= AUDIT_TIMEOUT_SEC:
        raise AssertionError("runtime limit exceeded")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
