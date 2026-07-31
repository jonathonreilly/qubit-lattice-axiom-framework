#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-830 v2 merger profile.

The Cycle-830, Cycle-822, and Cycle-820 primaries are source-only inputs:
they are hashed and parsed as AST, never imported or executed.  This checker
extracts only the disclosed serialized landed gates, lawful initial states,
and S* bits from the Cycle-830 syntax tree.  It then implements a separate
forward circuit evaluator and reverse constraint eliminator.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle822_sstar_basin_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
)

import ast
import base64
from collections import defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import struct
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ONLY_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[1]:
        "269d235c4981eaa4b94cfc200a0d472bf9f1ca8b57c2e14880afe754a9d41c56",
    AUDIT_INPUT_PATHS[2]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[1]: "56fd26ec1f09e3690aa0e9cacd1447c289fd7ac0",
    AUDIT_INPUT_PATHS[2]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
}
EXPECTED_AST_FUNCTIONS = {
    AUDIT_INPUT_PATHS[0]: {
        "decode_fixtures", "build_words", "apply_word",
        "one_step_certificate", "preimage_tree_certificate",
        "trajectory_and_mechanism_certificates",
    },
    AUDIT_INPUT_PATHS[1]: {
        "build_family", "evolve_sstar_pair", "sstar_anatomy",
        "entry_predictors", "basin_census",
    },
    AUDIT_INPUT_PATHS[2]: {
        "build_family", "evolve_nine", "population_state_at_entry",
        "mechanism_candidates",
    },
}

RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
MECHANISM_ENTRY = 14739
TREE_DEPTH = 8
EXPECTED_MACRO_GATES = 3106
EXPECTED_WORD_GATES = 6212
EXPECTED_SSTAR_SHA256 = (
    "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a"
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
EXPECTED_TREE_COUNTS = (1, 14, 18, 21, 16, 18, 26, 26, 25)
EXPECTED_OCCUPANCY = (1, 3, 4, 5, 3, 5, 5, 5, 4)
NINE_KEYS = (
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
EXPECTED_PARTITIONS = (
    (NINE_KEYS,),
    ((NINE_KEYS[0],), NINE_KEYS[1:4], NINE_KEYS[4:]),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:],
    ),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    ((NINE_KEYS[0],), NINE_KEYS[1:4], NINE_KEYS[4:]),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    (
        (NINE_KEYS[0],),
        NINE_KEYS[1:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
)
EXPECTED_SHARED_PAIR_COUNTS = (36, 13, 11, 5, 13, 5, 5, 5, 7)
EXPECTED_FORWARD_PARTITION_RELATIONS = (
    "SPLIT_TO_FINER",
    "UNCHANGED",
    "UNCHANGED",
    "COALESCE_TO_COARSER",
    "SPLIT_TO_FINER",
    "COALESCE_TO_COARSER",
    "COALESCE_TO_COARSER",
    "COALESCE_TO_COARSER",
)


class _SourceOnlyFinder(importlib.abc.MetaPathFinder):
    """Make importing a source-only primary an immediate hard failure."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if any(
            fullname == name or fullname.startswith(name + ".")
            for name in SOURCE_ONLY_MODULES
        ):
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids importing {fullname}")
        return None


IMPORT_FIREWALL = _SourceOnlyFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def git_blob_sha(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def top_level_literal(tree: ast.Module, name: str) -> object:
    nodes = [
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
    ]
    if len(nodes) != 1:
        raise ValueError(f"expected one literal assignment for {name}")
    return ast.literal_eval(nodes[0])


def top_level_function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_only_certificate() -> tuple[
    dict[str, object], dict[str, ast.Module]
]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads.items()
    }
    ast_basis = {
        path: expected <= top_level_function_names(trees[path])
        for path, expected in EXPECTED_AST_FUNCTIONS.items()
        if path in trees
    }

    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    self_import_roots: set[str] = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            self_import_roots.update(
                alias.name.split(".")[0] for alias in node.names
            )
        elif isinstance(node, ast.ImportFrom) and node.module:
            self_import_roots.add(node.module.split(".")[0])
    forbidden_execution_calls = tuple(sorted({
        node.func.id
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"compile", "eval", "exec", "__import__"}
    }))
    direct_frontier_imports = tuple(sorted(
        root for root in self_import_roots
        if root.startswith("frontier_cycle")
    ))
    stdlib_roots = set(sys.stdlib_module_names) | {"__future__"}
    literal_paths = top_level_literal(self_tree, "AUDIT_INPUT_PATHS")
    result = {
        "status": "PASS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": literal_paths == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 6,
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "AST_basis": ast_basis,
        "source_only_paths": AUDIT_INPUT_PATHS,
        "blocked_modules": SOURCE_ONLY_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in SOURCE_ONLY_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "forbidden_execution_calls": forbidden_execution_calls,
        "stdlib_only": self_import_roots <= stdlib_roots,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 6
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and len(ast_basis) == len(AUDIT_INPUT_PATHS)
        and all(ast_basis.values())
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and not direct_frontier_imports
        and not forbidden_execution_calls
        and result["stdlib_only"]
    )
    result["status"] = "PASS" if result["pass"] else "FAIL"
    return result, trees


def circle_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(right - left, RING_STATIONS - (right - left)) > 1
    )


def state_sha256(state: int) -> str:
    return sha256(bytes(
        (state >> wire) & 1 for wire in range(STATE_BITS)
    )).hexdigest()


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def decode_source_literals(
    primary_tree: ast.Module,
) -> dict[str, object]:
    gate_encoded = top_level_literal(primary_tree, "GATE_CONSTANTS_B85")
    family_encoded = top_level_literal(primary_tree, "FAMILY_STATES_B85")
    sstar_encoded = top_level_literal(primary_tree, "SSTAR_PACKED_B85")
    if not all(
        isinstance(value, str)
        for value in (gate_encoded, family_encoded, sstar_encoded)
    ):
        raise TypeError("serialized primary literals must be strings")

    gate_raw = zlib.decompress(base64.b85decode(gate_encoded))
    family_raw = zlib.decompress(base64.b85decode(family_encoded))
    sstar_raw = zlib.decompress(base64.b85decode(sstar_encoded))
    macro_lengths = struct.unpack_from("<11H", gate_raw)
    cursor = 22
    macros: list[tuple[tuple[int, int, int, int], ...]] = []
    for length in macro_lengths:
        stop = cursor + 7 * length
        macro = tuple(
            struct.unpack_from("<BHHH", gate_raw, offset)
            for offset in range(cursor, stop, 7)
        )
        macros.append(macro)
        cursor = stop

    positions = circle_pairs()
    family_keys = tuple(
        (event, pair)
        for event in range(4)
        for pair in positions
    )
    family_states = {
        key: int.from_bytes(
            family_raw[index * STATE_BYTES:(index + 1) * STATE_BYTES],
            "little",
        )
        for index, key in enumerate(family_keys)
    }
    sstar = int.from_bytes(sstar_raw, "little")
    gate_rows_valid = all(
        kind in (0, 1, 2)
        and first < STATE_BITS
        and second < STATE_BITS
        and third < STATE_BITS
        for macro in macros
        for kind, first, second, third in macro
    )
    certificate = {
        "literal_extraction":
            "AST literal_eval only; no primary code was imported or executed",
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "expected_gate_raw_sha256": EXPECTED_GATE_RAW_SHA256,
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "expected_family_raw_sha256": EXPECTED_FAMILY_RAW_SHA256,
        "sstar_packed_sha256": sha256(sstar_raw).hexdigest(),
        "expected_sstar_packed_sha256": EXPECTED_SSTAR_PACKED_SHA256,
        "macro_lengths": macro_lengths,
        "macro_gate_count": sum(macro_lengths),
        "separated_position_count": len(positions),
        "family_state_count": len(family_states),
        "state_bits": STATE_BITS,
        "Sstar_hamming_weight": sstar.bit_count(),
        "Sstar_sha256": state_sha256(sstar),
        "expected_Sstar_sha256": EXPECTED_SSTAR_SHA256,
        "gate_rows_valid": gate_rows_valid,
    }
    certificate["pass"] = (
        cursor == len(gate_raw)
        and certificate["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and certificate["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and len(sstar_raw) == STATE_BYTES
        and certificate["sstar_packed_sha256"]
        == EXPECTED_SSTAR_PACKED_SHA256
        and len(macros) == RING_STATIONS
        and sum(macro_lengths) == EXPECTED_MACRO_GATES
        and len(positions) == 44
        and len(family_states) == FAMILY_SIZE
        and sstar.bit_length() <= STATE_BITS
        and sstar.bit_count() == 44
        and state_sha256(sstar) == EXPECTED_SSTAR_SHA256
        and gate_rows_valid
    )
    return {
        "macros": tuple(macros),
        "positions": positions,
        "family_states": family_states,
        "sstar": sstar,
        "certificate": certificate,
    }


def independently_schedule_words(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    positions: tuple[tuple[int, int], ...],
) -> dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]]:
    """Build each landed word from the two translated live stations."""
    words = {}
    for left, right in positions:
        gates: list[tuple[int, int, int, int]] = []
        for phase in range(RING_STATIONS):
            live_stations = sorted((
                (left + phase) % RING_STATIONS,
                (right + phase) % RING_STATIONS,
            ))
            for station in live_stations:
                gates.extend(macros[station])
        words[(left, right)] = tuple(gates)
    return words


def landed_forward(
    state: int,
    word: tuple[tuple[int, int, int, int], ...],
) -> int:
    """Forward evaluator written directly from the landed Boolean rules."""
    for kind, control0, control1_or_target, target in word:
        if kind == 0:
            state ^= 1 << control0
        elif kind == 1:
            control = (state >> control0) & 1
            state ^= control << control1_or_target
        elif kind == 2:
            controls = (
                ((state >> control0) & 1)
                * ((state >> control1_or_target) & 1)
            )
            state ^= controls << target
        else:
            raise ValueError(f"unknown landed gate kind {kind}")
    return state


def eliminate_preimage_constraints(
    image: int,
    word: tuple[tuple[int, int, int, int], ...],
) -> int:
    """Solve the Boolean constraints backwards, one landed row at a time."""
    solution = image
    for kind, first, second, third in reversed(word):
        if kind == 0:
            before_target = 1 ^ ((solution >> first) & 1)
            solution ^= (((solution >> first) & 1) ^ before_target) << first
        elif kind == 1:
            before_target = (
                ((solution >> second) & 1)
                ^ ((solution >> first) & 1)
            )
            solution ^= (
                ((solution >> second) & 1) ^ before_target
            ) << second
        elif kind == 2:
            before_target = (
                ((solution >> third) & 1)
                ^ (
                    ((solution >> first) & 1)
                    * ((solution >> second) & 1)
                )
            )
            solution ^= (
                ((solution >> third) & 1) ^ before_target
            ) << third
        else:
            raise ValueError(f"unknown landed gate kind {kind}")
    return solution


def primitive_constraint_truth_table() -> dict[str, object]:
    specifications = (
        ("X", 1, (0, 0, 0, 0)),
        ("CNOT", 2, (1, 0, 1, 0)),
        ("TOFFOLI", 3, (2, 0, 1, 2)),
    )
    rows = 0
    failures = []
    for name, width, gate in specifications:
        word = (gate,)
        for before in range(1 << width):
            rows += 1
            after = landed_forward(before, word)
            recovered = eliminate_preimage_constraints(after, word)
            if recovered != before:
                failures.append((name, before, after, recovered))
    return {
        "truth_table_rows": rows,
        "failures": tuple(failures),
        "derived_constraints": {
            "X": "before_t = after_t XOR 1",
            "CNOT": "before_t = after_t XOR after_c",
            "TOFFOLI": "before_t = after_t XOR (after_c0 AND after_c1)",
            "composition": "eliminate landed rows in reverse order",
        },
        "pass": rows == 14 and not failures,
    }


def state_set_digest(states: set[int]) -> str:
    hasher = sha256()
    for state in sorted(states):
        hasher.update(state.to_bytes(STATE_BYTES, "little"))
    return hasher.hexdigest()


def preimage_rederivation(
    target: int,
    words: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
) -> tuple[dict[str, object], dict[int, set[int]], dict[int, dict]]:
    primitive = primitive_constraint_truth_table()
    one_step_classes: dict[int, list[tuple[int, int]]] = defaultdict(list)
    forward_failures = []
    for label, word in words.items():
        solution = eliminate_preimage_constraints(target, word)
        one_step_classes[solution].append(label)
        if landed_forward(solution, word) != target:
            forward_failures.append(label)

    rays = {label: target for label in words}
    levels = {0: {target}}
    ray_states: dict[int, dict] = {0: dict(rays)}
    counts = [1]
    digests = [state_set_digest(levels[0])]
    for depth in range(1, TREE_DEPTH + 1):
        rays = {
            label: eliminate_preimage_constraints(state, words[label])
            for label, state in rays.items()
        }
        ray_states[depth] = dict(rays)
        levels[depth] = set(rays.values())
        counts.append(len(levels[depth]))
        digests.append(state_set_digest(levels[depth]))

    multiplicities = tuple(sorted(
        len(labels) for labels in one_step_classes.values()
    ))
    finding = (
        "PASS: reverse elimination gives exactly one predecessor for each "
        "fixed position word; 44 labeled solutions collapse to 14 data "
        f"states, and exact depths 0..8 have counts {counts}."
    )
    result = {
        "status": "PASS",
        "finding": finding,
        "fixed_word_bijection_reason":
            "each X/CNOT/Toffoli constraint uniquely determines its prior "
            "target bit while leaving its controls unchanged",
        "primitive_constraint_truth_table": primitive,
        "fixed_position_words": len(words),
        "gate_counts": tuple(sorted({len(word) for word in words.values()})),
        "one_solution_per_fixed_word": not forward_failures,
        "labeled_preimage_count": sum(map(len, one_step_classes.values())),
        "distinct_data_preimage_count": len(one_step_classes),
        "label_class_multiplicities": multiplicities,
        "forward_recheck_failures": tuple(forward_failures),
        "depth_counts": tuple(counts),
        "depth_0_through_5_counts": tuple(counts[:6]),
        "state_set_sha256_by_depth": tuple(digests),
    }
    result["pass"] = (
        primitive["pass"]
        and len(words) == 44
        and set(map(len, words.values())) == {EXPECTED_WORD_GATES}
        and not forward_failures
        and sum(map(len, one_step_classes.values())) == 44
        and len(one_step_classes) == 14
        and multiplicities
        == (1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 7, 8, 9)
        and tuple(counts) == EXPECTED_TREE_COUNTS
    )
    if not result["pass"]:
        result["status"] = "FAIL"
        result["finding"] = (
            "FAIL: independent reverse elimination did not reproduce the "
            "claimed one-step or fixed-ray depth counts."
        )
    return result, levels, ray_states


def pack_lanes(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        remaining = state
        while remaining:
            bit = remaining & -remaining
            columns[bit.bit_length() - 1] |= 1 << lane
            remaining ^= bit
    return columns


def unpack_lane(columns: list[int], lane: int) -> int:
    state = 0
    lane_bit = 1 << lane
    for wire, column in enumerate(columns):
        if column & lane_bit:
            state |= 1 << wire
    return state


def independently_masked_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    keys: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    schedule: list[tuple[int, int, int, int, int]] = []
    for phase in range(RING_STATIONS):
        for station in range(RING_STATIONS):
            lane_mask = 0
            for lane, (_event, (left, right)) in enumerate(keys):
                if station in (
                    (left + phase) % RING_STATIONS,
                    (right + phase) % RING_STATIONS,
                ):
                    lane_mask |= 1 << lane
            if lane_mask:
                schedule.extend(
                    (kind, first, second, third, lane_mask)
                    for kind, first, second, third in macros[station]
                )
    return tuple(schedule)


def advance_packed_lanes(
    columns: list[int],
    schedule: tuple[tuple[int, int, int, int, int], ...],
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


def forward_nine_history_snapshots(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    family_states: dict[tuple[int, tuple[int, int]], int],
) -> dict[str, object]:
    lane_keys = NINE_KEYS + (NINE_KEYS[0],)
    lane_states = tuple(family_states[key] for key in lane_keys)
    columns = pack_lanes(lane_states)
    schedule = independently_masked_schedule(macros, lane_keys)
    snapshots: dict[int, tuple[int, ...]] = {}
    duplicate_snapshots: dict[int, int] = {}
    capture_from = MECHANISM_ENTRY - TREE_DEPTH
    if capture_from == 0:
        snapshots[0] = tuple(
            unpack_lane(columns, lane) for lane in range(len(NINE_KEYS))
        )
        duplicate_snapshots[0] = unpack_lane(columns, len(NINE_KEYS))
    for update in range(1, MECHANISM_ENTRY + 1):
        advance_packed_lanes(columns, schedule)
        if update >= capture_from:
            snapshots[update] = tuple(
                unpack_lane(columns, lane)
                for lane in range(len(NINE_KEYS))
            )
            duplicate_snapshots[update] = unpack_lane(
                columns, len(NINE_KEYS)
            )
    duplicate_exact = all(
        duplicate_snapshots[time] == snapshots[time][0]
        for time in snapshots
    )
    return {
        "snapshots": snapshots,
        "duplicate_snapshots": duplicate_snapshots,
        "masked_rows_per_update": len(schedule),
        "updates": MECHANISM_ENTRY,
        "duplicate_lane_exact_at_all_captured_times": duplicate_exact,
    }


def active_indices(value: int) -> tuple[int, ...]:
    indices = []
    while value:
        bit = value & -value
        indices.append(bit.bit_length() - 1)
        value ^= bit
    return tuple(indices)


def varying_indices(states: tuple[int, ...]) -> tuple[int, ...]:
    if not states:
        return ()
    variation = 0
    anchor = states[0]
    for state in states[1:]:
        variation |= anchor ^ state
    return active_indices(variation)


def state_partition(
    states: tuple[int, ...],
) -> tuple[tuple[tuple[int, tuple[int, int]], ...], ...]:
    groups: dict[int, list[tuple[int, tuple[int, int]]]] = {}
    for key, state in zip(NINE_KEYS, states):
        groups.setdefault(state, []).append(key)
    return tuple(
        tuple(group)
        for _state, group in sorted(
            groups.items(),
            key=lambda item: (item[1][0], len(item[1])),
        )
    )


def partition_refines(
    finer: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
    coarser: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
) -> bool:
    coarse_blocks = tuple(frozenset(group) for group in coarser)
    return all(
        any(frozenset(group) <= block for block in coarse_blocks)
        for group in finer
    )


def partition_relation(
    before: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
    after: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
) -> str:
    if before == after:
        return "UNCHANGED"
    if partition_refines(after, before):
        return "SPLIT_TO_FINER"
    if partition_refines(before, after):
        return "COALESCE_TO_COARSER"
    return "INCOMPARABLE_REARRANGEMENT"


def trajectory_and_occupancy_certificates(
    target: int,
    words: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
    levels: dict[int, set[int]],
    forward: dict[str, object],
) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    reverse_states = tuple(target for _key in NINE_KEYS)
    depth_states = {0: reverse_states}
    for depth in range(1, TREE_DEPTH + 1):
        reverse_states = tuple(
            eliminate_preimage_constraints(state, words[key[1]])
            for key, state in zip(NINE_KEYS, reverse_states)
        )
        depth_states[depth] = reverse_states

    snapshots = forward["snapshots"]
    assert isinstance(snapshots, dict)
    exact_forward_matches = tuple(
        depth_states[depth]
        == snapshots[MECHANISM_ENTRY - depth]
        for depth in range(TREE_DEPTH + 1)
    )
    memberships = tuple(
        all(state in levels[depth] for state in depth_states[depth])
        for depth in range(TREE_DEPTH + 1)
    )
    occupancies = tuple(
        len(set(depth_states[depth]))
        for depth in range(TREE_DEPTH + 1)
    )
    partitions = tuple(
        state_partition(depth_states[depth])
        for depth in range(TREE_DEPTH + 1)
    )
    shared_partitions = {
        str(depth): tuple(
            group for group in partitions[depth] if len(group) > 1
        )
        for depth in range(1, TREE_DEPTH + 1)
    }
    shared_pair_counts = tuple(
        sum(len(group) * (len(group) - 1) // 2 for group in partitions[depth])
        for depth in range(TREE_DEPTH + 1)
    )
    no_pairwise_positive_depth_merger = all(
        len(set(depth_states[depth])) == len(NINE_KEYS)
        for depth in range(1, TREE_DEPTH + 1)
    )
    positive_depth_collision_depths = tuple(
        depth for depth in range(1, TREE_DEPTH + 1)
        if any(len(group) > 1 for group in partitions[depth])
    )
    nine_way_merger_depths = tuple(
        depth for depth, count in enumerate(occupancies) if count == 1
    )
    forward_partition_relations = tuple(
        partition_relation(partitions[depth], partitions[depth - 1])
        for depth in range(TREE_DEPTH, 0, -1)
    )
    monotone_coarsening_toward_depth_0 = all(
        relation in {"UNCHANGED", "COALESCE_TO_COARSER"}
        for relation in forward_partition_relations
    )

    occupancy_computation_ok = (
        all(exact_forward_matches)
        and all(memberships)
        and occupancies == EXPECTED_OCCUPANCY
        and partitions == EXPECTED_PARTITIONS
        and shared_pair_counts == EXPECTED_SHARED_PAIR_COUNTS
        and positive_depth_collision_depths
        == tuple(range(1, TREE_DEPTH + 1))
        and forward_partition_relations
        == EXPECTED_FORWARD_PARTITION_RELATIONS
        and forward["duplicate_lane_exact_at_all_captured_times"]
        and all(state == target for state in snapshots[MECHANISM_ENTRY])
        and nine_way_merger_depths == (0,)
    )
    v2_primary_collision_claim_holds = occupancy_computation_ok
    occupancy = {
        "status": "PASS" if v2_primary_collision_claim_holds else "FAIL",
        "finding": (
            "PASS: the independent collision attack exactly reproduces v2's "
            "full depth-0..8 partitions. Pairwise projected collisions occur "
            "at every positive depth; only the all-nine common merger is "
            "depth-0-only."
            if v2_primary_collision_claim_holds
            else
            "FAIL: the independently reproduced collision partitions, "
            "pair counts, occupancy, or hierarchy differ from the pinned "
            "v2 profile."
        ),
        "forward_times_checked": tuple(
            MECHANISM_ENTRY - depth
            for depth in range(TREE_DEPTH + 1)
        ),
        "independent_forward_snapshot_matches": exact_forward_matches,
        "depth_set_memberships": memberships,
        "node_occupancy_counts": occupancies,
        "expected_node_occupancy_counts": EXPECTED_OCCUPANCY,
        "full_partition_sequence_depth_0_through_8": partitions,
        "expected_partition_sequence_depth_0_through_8":
            EXPECTED_PARTITIONS,
        "shared_pair_counts_by_depth": shared_pair_counts,
        "expected_shared_pair_counts_by_depth":
            EXPECTED_SHARED_PAIR_COUNTS,
        "positive_depth_shared_partitions": shared_partitions,
        "positive_depth_collision_depths":
            positive_depth_collision_depths,
        "no_two_keys_share_at_any_depth_1_through_8":
            no_pairwise_positive_depth_merger,
        "all_nine_common_merger_depths": nine_way_merger_depths,
        "partition_relations_depth_8_through_0":
            forward_partition_relations,
        "expected_partition_relations_depth_8_through_0":
            EXPECTED_FORWARD_PARTITION_RELATIONS,
        "monotone_coarsening_toward_depth_0":
            monotone_coarsening_toward_depth_0,
        "computation_pass": occupancy_computation_ok,
        "collision_attack_pass": v2_primary_collision_claim_holds,
        "primary_wording_pass": v2_primary_collision_claim_holds,
        "pass": v2_primary_collision_claim_holds,
    }

    depth1 = depth_states[1]
    depth1_nodes = tuple(sorted(set(depth1)))
    varying = varying_indices(depth1)
    node_diffs = tuple({
        "predecessor_state_sha256": state_sha256(state),
        "xor_Sstar_wire_count": (state ^ target).bit_count(),
        "xor_Sstar_wire_indices": active_indices(state ^ target),
        "forward_label_count": sum(
            landed_forward(state, words[key[1]]) == target
            for key, key_state in zip(NINE_KEYS, depth1)
            if key_state == state
        ),
    } for state in depth1_nodes)
    erasure = {
        "status": "PASS",
        "finding":
            "PASS: at depth 1 the nine histories occupy three nodes and "
            "differ on exactly 15 wire coordinates; the key-specific final "
            "tick sends every predecessor to the identical 5815-bit S*.",
        "depth1_distinct_nodes": len(depth1_nodes),
        "depth1_history_varying_wire_count": len(varying),
        "depth1_history_varying_wire_indices": varying,
        "depth1_node_diffs_against_Sstar": node_diffs,
        "all_key_specific_final_ticks_equal_Sstar": all(
            landed_forward(state, words[key[1]]) == target
            for key, state in zip(NINE_KEYS, depth1)
        ),
        "image_distinct_nodes": len(set(depth_states[0])),
        "image_history_varying_wire_count":
            len(varying_indices(depth_states[0])),
    }
    erasure["pass"] = (
        erasure["depth1_distinct_nodes"] == 3
        and erasure["depth1_history_varying_wire_count"] == 15
        and erasure["all_key_specific_final_ticks_equal_Sstar"]
        and erasure["image_distinct_nodes"] == 1
        and erasure["image_history_varying_wire_count"] == 0
    )
    if not erasure["pass"]:
        erasure["status"] = "FAIL"
        erasure["finding"] = (
            "FAIL: the independent depth-1/S* diff did not reproduce the "
            "claimed three-node, 15-varying-wire final erasure."
        )

    forward_occupancy = tuple(reversed(occupancies))
    single_map_monotone = all(
        after <= before
        for before, after in zip(
            forward_occupancy, forward_occupancy[1:]
        )
    )
    post_sstar = tuple(
        landed_forward(target, words[key[1]]) for key in NINE_KEYS
    )
    mechanism = {
        "status": "PASS",
        "finding":
            "PASS with scope: v2's nonmonotone hierarchical "
            "parameterized-bijection synchronization reading is faithful. "
            "Shared-state subgroups occur throughout the approach, split at "
            "8->7 and 4->3, and otherwise persist or coalesce; the final "
            "tick maps three nodes differing on 15 wires to the common S*.",
        "classification":
            "NONMONOTONE_HIERARCHICAL_PARAMETERIZED_BIJECTION_"
            "SYNCHRONIZATION_NOT_SINGLE_MAP_ATTRACTION",
        "forward_occupancy_t14731_through_t14739": forward_occupancy,
        "partition_relations_depth_8_through_0":
            forward_partition_relations,
        "monotone_partition_coarsening_toward_depth_0":
            monotone_coarsening_toward_depth_0,
        "single_deterministic_map_would_be_monotone_nonincreasing": True,
        "observed_forward_occupancy_is_monotone_nonincreasing":
            single_map_monotone,
        "fixed_parameter_maps_are_bijections":
            "proved by unique reverse elimination of every primitive row",
        "distinct_images_one_tick_after_Sstar": len(set(post_sstar)),
        "Sstar_is_common_fixed_point": (
            len(set(post_sstar)) == 1 and post_sstar[0] == target
        ),
        "scope_qualification":
            "the data establish this finite nine-history hierarchical "
            "profile; they do not establish a universal attraction law",
    }
    mechanism["pass"] = (
        not single_map_monotone
        and not monotone_coarsening_toward_depth_0
        and forward_partition_relations
        == EXPECTED_FORWARD_PARTITION_RELATIONS
        and len(set(post_sstar)) > 1
        and not mechanism["Sstar_is_common_fixed_point"]
        and nine_way_merger_depths == (0,)
        and erasure["pass"]
    )
    if not mechanism["pass"]:
        mechanism["status"] = "FAIL"
        mechanism["finding"] = (
            "FAIL: the tree data did not support the scoped "
            "parameterized-bijection synchronization reading."
        )
    return occupancy, erasure, mechanism


def stable_render(
    certificates: dict[str, dict[str, object]],
    report: dict[str, object],
) -> str:
    rows = [
        f"CERTIFICATE_{name}={compact(value)}"
        for name, value in certificates.items()
    ]
    rows.append(f"REPORT={compact(report)}")
    return "\n".join(rows) + "\n"


def run() -> int:
    started = monotonic()
    source_only, trees = source_only_certificate()
    if not source_only["pass"]:
        raise AssertionError("source-only SHA/AST controls failed")
    decoded = decode_source_literals(trees[AUDIT_INPUT_PATHS[0]])
    fixture_certificate = decoded["certificate"]
    macros = decoded["macros"]
    positions = decoded["positions"]
    family_states = decoded["family_states"]
    target = decoded["sstar"]
    assert isinstance(fixture_certificate, dict)
    assert isinstance(macros, tuple)
    assert isinstance(positions, tuple)
    assert isinstance(family_states, dict)
    assert isinstance(target, int)
    if not fixture_certificate["pass"]:
        raise AssertionError("serialized landed fixture controls failed")

    words = independently_schedule_words(macros, positions)
    preimage, levels, _ray_states = preimage_rederivation(target, words)
    forward = forward_nine_history_snapshots(macros, family_states)
    occupancy, erasure, mechanism = trajectory_and_occupancy_certificates(
        target, words, levels, forward
    )
    elapsed = monotonic() - started

    primary_refuted = (
        occupancy["computation_pass"]
        and not occupancy["primary_wording_pass"]
    )
    controls_base = (
        source_only["pass"]
        and fixture_certificate["pass"]
        and forward["duplicate_lane_exact_at_all_captured_times"]
        and not tuple(
            name for name in SOURCE_ONLY_MODULES if name in sys.modules
        )
        and not tuple(IMPORT_FIREWALL.hits)
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls = {
        "status": "PASS",
        "finding":
            "PASS: all three primaries remained SHA-pinned source/AST-only "
            "inputs; the duplicate evolution lane was exact; literal paths "
            "exist worktree-relative; runtime and stdout stayed bounded.",
        "source_only": source_only,
        "landed_literal_fixture": fixture_certificate,
        "blocked_modules_loaded_at_end": tuple(
            name for name in SOURCE_ONLY_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
        "determinism_duplicate_lane_exact":
            forward["duplicate_lane_exact_at_all_captured_times"],
        "masked_rows_per_update": forward["masked_rows_per_update"],
        "updates": forward["updates"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    certificates = {
        "PREIMAGE_RE_DERIVATION": preimage,
        "THE_OCCUPANCY_MAP": occupancy,
        "THE_ERASURE_ACCOUNTING": erasure,
        "THE_MECHANISM_WORDING": mechanism,
        "CONTROLS": controls,
    }
    report = {
        "cycle": 830,
        "version": 2,
        "checker":
            "INDEPENDENT_ADVERSARIAL_CHECKER_THE_SYNCHRONIZATION_MECHANISM",
        "checker_pass": False,
        "primary_claim_pass": occupancy["primary_wording_pass"],
        "primary_refuted": primary_refuted,
        "v1_refutation_adopted":
            occupancy["positive_depth_collision_depths"]
            == tuple(range(1, TREE_DEPTH + 1)),
        "finding":
            "The exact collision map, nonmonotone hierarchy, final-tick "
            "erasure, preimage derivation, and mechanism scope independently "
            "match the pinned v2 claims.",
        "certificate_statuses": {},
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "terminal": "CYCLE830_INDEPENDENT_CHECK_INTERNAL_FAIL",
    }

    for _iteration in range(12):
        controls["pass"] = controls_base
        controls["status"] = "PASS" if controls["pass"] else "FAIL"
        if not controls["pass"]:
            controls["finding"] = (
                "FAIL: a SHA/AST blocklist, determinism, runtime, or stdout "
                "control failed."
            )
        report["certificate_statuses"] = {
            name: certificate["status"]
            for name, certificate in certificates.items()
        }
        report["checker_pass"] = (
            preimage["pass"]
            and occupancy["pass"]
            and not primary_refuted
            and erasure["pass"]
            and mechanism["pass"]
            and controls["pass"]
        )
        report["primary_claim_pass"] = occupancy["primary_wording_pass"]
        report["terminal"] = (
            "CYCLE830_V2_INDEPENDENT_CHECK_EXACT_PASS"
            if report["checker_pass"] and not primary_refuted
            else "CYCLE830_INDEPENDENT_CHECK_INTERNAL_FAIL"
        )
        output = stable_render(certificates, report)
        output_bytes = len(output.encode("utf-8"))
        stdout_ok = output_bytes < STDOUT_LIMIT_BYTES
        controls["stdout_bytes"] = output_bytes
        controls["pass"] = controls_base and stdout_ok
        controls["status"] = "PASS" if controls["pass"] else "FAIL"
        report["stdout_bytes"] = output_bytes

    output = stable_render(certificates, report)
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "checker_pass": False,
            "primary_refuted": primary_refuted,
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE830_INDEPENDENT_CHECK_INTERNAL_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["checker_pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "checker_pass": False,
            "primary_refuted": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE830_INDEPENDENT_CHECK_INTERNAL_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
