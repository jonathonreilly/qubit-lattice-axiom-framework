#!/usr/bin/env python3
"""Cycle 854: boundary-inheritance attack on the Cycle-848 braid.

The declared inheritance ladder has exactly two levels: single wire values,
then two-wire parities.  Admission is by an input-independent primitive-toggle
derivation at complete-generator boundaries, never by trajectory correlation.
The Cycle-830 fixture source and the Cycle-848/853 scientific primaries are
SHA/blob-pinned, parsed as text/AST only, and blocked from import.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle848_braid_derivation_2026_07_28.py",
    "scripts/frontier_cycle853_usage_independent_check_2026_07_28.py",
)

import ast
import base64
from collections import Counter, defaultdict
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
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR27-20260729"
EXPECTED_BASE = "e07dc8e094abd7d2633a805139ae100585e03d62"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[1]:
        "a9fdefbffe16495e62258804d3abbddb48aaa500e365f56c739c24959162ca48",
    AUDIT_INPUT_PATHS[2]:
        "4cdabe8126f4cc8ab64ee7b3ad4772299770e4640dea1eff1351996a6092173c",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[1]: "c55036475e2389565b1c4b69e96595db99e03779",
    AUDIT_INPUT_PATHS[2]: "b0a1bdcb9ffa4ebce9bad73485489fe8c7094919",
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
EXPECTED_NORMALIZED_PARTITION_SHA256 = (
    "726b74aefc7afa6e1790c7dc73a59eacdadeec72246e19ac01104be09d49829d"
)
EXPECTED_EVENT_SIGNATURE_SHA256 = (
    "7ae45bbd8b6e688b9abdadd0e33dcfd300e2649b4776386a5b8ec48eb62e064a"
)

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
PREDICATE_WIRES = (40, 81, 105)
EXPECTED_EVENT_COUNT = 20
EXPECTED_TYPE_COUNT = 16
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
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


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
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
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    actual_sha = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    actual_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    basis = {
        "cycle830_literal_fixture_basis": {
            "decode_fixtures", "build_words", "apply_word",
        } <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle848_braid_census_basis": {
            "evolve_nine", "transition_rows", "certificate_b_schema_hunt",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle853_boundary_mechanism_basis": {
            "recursion_probe", "extract_patterns", "run",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle848_constants_exact": (
            literal_assignment(trees[AUDIT_INPUT_PATHS[1]], "BACKBONE")
            == BACKBONE
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[1]], "NINE_PREDICATE_WIRES"
            ) == PREDICATE_WIRES
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[1]], "EXPECTED_GENERATED_EVENT_COUNT"
            ) == EXPECTED_EVENT_COUNT
        ),
        "cycle853_constants_exact": (
            literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "BACKBONE")
            == BACKBONE
            and literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "STATE_BITS")
            == STATE_BITS
        ),
    }
    branch = subprocess.run(
        ("git", "branch", "--show-current"), cwd=ROOT, check=True,
        capture_output=True, text=True, timeout=20,
    ).stdout.strip()
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", EXPECTED_BASE, "HEAD"),
        cwd=ROOT, timeout=20,
    ).returncode == 0
    public = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "AST_basis": basis,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "text_AST_only": AUDIT_INPUT_PATHS,
        "direct_frontier_imports": tuple(sorted(
            name for name in imports if name.startswith("frontier_cycle")
        )),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "expected_branch": EXPECTED_BRANCH,
        "actual_branch": branch,
        "branch_exact": branch == EXPECTED_BRANCH,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
    }
    public["pass"] = (
        public["AUDIT_INPUT_PATHS_literal"]
        and public["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(basis.values())
        and not public["direct_frontier_imports"]
        and not FIREWALL.hits
        and public["branch_exact"]
        and base_is_ancestor
    )
    return public, trees


def cyclic_separation(pair: tuple[int, int]) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def lawful_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def state_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def decode_fixtures(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(literal_assignment(tree, name) for name in (
        "GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85",
    ))
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("Cycle-830 literal fixture bank missing")
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
    keys = tuple(sorted(
        (event, pair) for event in range(4) for pair in lawful_pairs()
    ))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little",
        )
    public = {
        "macro_gate_counts": lengths,
        "macro_gate_count": sum(lengths),
        "family_key_count": len(states),
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "target_raw_sha256": sha256(target_raw).hexdigest(),
    }
    public["pass"] = (
        len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and len(target_raw) == STATE_BYTES
        and len(states) == FAMILY_SIZE
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and public["target_raw_sha256"] == EXPECTED_SSTAR_PACKED_SHA256
    )
    return {
        "macros": tuple(macros), "keys": keys, "states": states,
        "target": int.from_bytes(target_raw, "little"), "public": public,
    }


def build_gate_words(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
) -> dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]]:
    words = {}
    for pair in BACKBONE:
        rows = []
        for phase in range(RING_STATIONS):
            live = {
                (pair[0] + phase) % RING_STATIONS,
                (pair[1] + phase) % RING_STATIONS,
            }
            for station, macro in enumerate(macros):
                if station in live:
                    rows.extend(macro)
        if len(rows) != WORD_GATE_COUNT:
            raise AssertionError(("word gate count drift", pair, len(rows)))
        words[pair] = tuple(rows)
    return words


def compile_words(
    gate_words: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
) -> dict[tuple[int, int], tuple[tuple[int, int, int], ...]]:
    result = {}
    for pair, word in gate_words.items():
        rows = []
        for kind, first, second, third in word:
            if kind == 0:
                rows.append((0, 0, 1 << first))
            elif kind == 1:
                rows.append((1, 1 << first, 1 << second))
            elif kind == 2:
                rows.append((2, (1 << first) | (1 << second), 1 << third))
            else:
                raise AssertionError(("unknown gate kind", kind))
        result[pair] = tuple(rows)
    return result


def apply_word(
    state: int, word: tuple[tuple[int, int, int], ...], *, reverse: bool = False,
) -> int:
    rows = reversed(word) if reverse else word
    for kind, controls, target in rows:
        if kind == 0 or state & controls == controls:
            state ^= target
    return state


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


def movement_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for phase in range(RING_STATIONS):
        for station, macro in enumerate(macros):
            lane_mask = sum(
                1 << lane for lane, pair in enumerate(BACKBONE)
                if station in {
                    (pair[0] + phase) % RING_STATIONS,
                    (pair[1] + phase) % RING_STATIONS,
                }
            )
            if lane_mask:
                rows.extend((*gate, lane_mask) for gate in macro)
    return tuple(rows)


def advance(
    columns: list[int], schedule: tuple[tuple[int, int, int, int, int], ...],
) -> None:
    for kind, first, second, third, lane_mask in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        elif kind == 2:
            columns[third] ^= columns[first] & columns[second] & lane_mask
        else:
            raise AssertionError(("unknown gate kind", kind))


def partition_of(states: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    groups: dict[int, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(sorted(
        (tuple(group) for group in groups.values()), key=lambda group: group[0],
    ))


def evolve_nine(fixtures: dict[str, object]) -> dict[str, object]:
    initial = tuple(fixtures["states"][(0, pair)] for pair in BACKBONE)
    columns = bit_slice(initial)
    schedule = movement_schedule(fixtures["macros"])
    forward_tail = []
    for movement in range(1, NINE_FUNNEL_MOVEMENT + 1):
        advance(columns, schedule)
        if movement >= NINE_FUNNEL_MOVEMENT - PREDECESSOR_DEPTH:
            forward_tail.append(capture_lanes(columns, len(BACKBONE)))
    states_by_depth = tuple(reversed(forward_tail))
    partitions = tuple(
        partition_of(states)
        for states in states_by_depth[:NORMALIZED_DEPTH + 1]
    )
    public = {
        "states_by_depth": states_by_depth,
        "normalized_partition_sha256": digest(partitions),
        "captured_depth_count": len(states_by_depth),
        "movement_schedule_rows": len(schedule),
        "terminal_matches_target": all(
            state == fixtures["target"] for state in states_by_depth[0]
        ),
    }
    public["pass"] = (
        len(states_by_depth) == PREDECESSOR_DEPTH + 1
        and public["normalized_partition_sha256"]
        == EXPECTED_NORMALIZED_PARTITION_SHA256
        and public["terminal_matches_target"]
    )
    return public


def support_indices(mask: int) -> tuple[int, ...]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


def predicate_pattern(state: int) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in PREDICATE_WIRES)


def transition_rows(
    nine: dict[str, object],
    words: dict[tuple[int, int], tuple[tuple[int, int, int], ...]],
) -> tuple[dict[str, object], ...]:
    states_by_depth = nine["states_by_depth"]
    rows = []
    event_index = 0
    for depth in range(NORMALIZED_DEPTH, -1, -1):
        inputs_at_depth = states_by_depth[depth + 1]
        outputs_at_depth = states_by_depth[depth]
        predecessor = partition_of(inputs_at_depth)
        output_partition = partition_of(outputs_at_depth)
        for output_block in output_partition:
            incoming = tuple(
                tuple(lane for lane in block if lane in output_block)
                for block in predecessor
                if any(lane in output_block for lane in block)
            )
            if len(incoming) < 2:
                continue
            lanes = tuple(output_block)
            inputs = tuple(inputs_at_depth[lane] for lane in lanes)
            expected_outputs = tuple(outputs_at_depth[lane] for lane in lanes)
            rule_outputs = tuple(
                apply_word(inputs_at_depth[lane], words[BACKBONE[lane]])
                for lane in lanes
            )
            common_output = expected_outputs[0]
            inverse_inputs = tuple(
                apply_word(common_output, words[BACKBONE[lane]], reverse=True)
                for lane in lanes
            )
            variation_mask = 0
            for state in inputs[1:]:
                variation_mask |= inputs[0] ^ state
            variation_support = support_indices(variation_mask)
            patterns = tuple(predicate_pattern(state) for state in inputs)
            structural_type = {
                "incoming_block_sizes": tuple(len(block) for block in incoming),
                "participant_count": len(lanes),
                "predecessor_variation_support_count": len(variation_support),
                "predecessor_pattern_multiset":
                    tuple(sorted(Counter(patterns).items())),
                "known_three_wire_local":
                    set(variation_support) <= set(PREDICATE_WIRES),
                "all_patterns_in_landed_nine_family": all(
                    pattern in ((0, 0, 0), (0, 1, 1), (1, 0, 0))
                    for pattern in patterns
                ),
            }
            exact = (
                len(set(expected_outputs)) == 1
                and rule_outputs == expected_outputs
                and inverse_inputs == inputs
            )
            rows.append({
                "event_index": event_index,
                "normalized_depth": depth,
                "predecessor_depth": depth + 1,
                "incoming_lane_blocks": incoming,
                "coincident_lanes": lanes,
                "coincident_keys": tuple(BACKBONE[lane] for lane in lanes),
                "predecessor_states": inputs,
                "predecessor_variation_support": variation_support,
                "predecessor_patterns_on_landed_wires": patterns,
                "structural_precondition_type": structural_type,
                "type_sha256": digest(structural_type),
                "pass": exact,
            })
            event_index += 1
    signature = tuple(
        (row["normalized_depth"], row["incoming_lane_blocks"],
         row["coincident_lanes"])
        for row in rows
    )
    if (
        len(rows) != EXPECTED_EVENT_COUNT
        or digest(signature) != EXPECTED_EVENT_SIGNATURE_SHA256
        or not all(row["pass"] for row in rows)
    ):
        raise AssertionError(("Cycle-848 event census drift", len(rows), digest(signature)))
    return tuple(rows)


def main() -> int:
    print(compact({
        "cycle": 854,
        "pass": False,
        "terminal": "CYCLE854_IMPLEMENTATION_IN_PROGRESS",
    }))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
