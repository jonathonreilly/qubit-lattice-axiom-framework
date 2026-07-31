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
EXPECTED_GENERATED_EVENT_COUNT = 20
EXPECTED_GENERATED_EVENT_SIGNATURE_SHA256 = (
    "7ae45bbd8b6e688b9abdadd0e33dcfd300e2649b4776386a5b8ec48eb62e064a"
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


def support_indices(mask: int) -> tuple[int, ...]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


def predicate_pattern(state: int, wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in wires)


def exact_state_payload(
    inputs: tuple[int, ...], output: int,
) -> dict[str, object]:
    raw = b"".join(
        state.to_bytes(STATE_BYTES, "little") for state in (*inputs, output)
    )
    compressed = zlib.compress(raw, 9)
    return {
        "format":
            "lane-ordered predecessor states, then one common output; "
            f"{STATE_BYTES} little-endian bytes per exact 5815-bit state; "
            "zlib level 9; Base85",
        "input_state_count": len(inputs),
        "raw_bytes": len(raw),
        "raw_sha256": sha256(raw).hexdigest(),
        "compressed_bytes": len(compressed),
        "compressed_sha256": sha256(compressed).hexdigest(),
        "payload_b85": base64.b85encode(compressed).decode("ascii"),
        "roundtrip_exact": zlib.decompress(compressed) == raw,
    }


def transition_rows(
    nine: dict[str, object],
    words: dict[Pair, tuple[tuple[int, int, int], ...]],
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
            anchor = inputs[0]
            variation_mask = 0
            for state in inputs:
                variation_mask |= anchor ^ state
            variation_support = support_indices(variation_mask)
            patterns = tuple(
                predicate_pattern(state, NINE_PREDICATE_WIRES)
                for state in inputs
            )
            incoming_sizes = tuple(len(block) for block in incoming)
            three_wire_local = set(variation_support) <= set(NINE_PREDICATE_WIRES)
            patterns_in_family = all(
                pattern in NINE_PREDICATE_PATTERNS for pattern in patterns
            )
            word_digests = tuple(
                digest(words[BACKBONE[lane]]) for lane in lanes
            )
            payload = exact_state_payload(inputs, common_output)
            exact = (
                len(set(expected_outputs)) == 1
                and rule_outputs == expected_outputs
                and inverse_inputs == inputs
                and payload["roundtrip_exact"]
            )
            structural_type = {
                "incoming_block_sizes": incoming_sizes,
                "participant_count": len(lanes),
                "predecessor_variation_support_count": len(variation_support),
                "predecessor_pattern_multiset": tuple(sorted(Counter(patterns).items())),
                "known_three_wire_local": three_wire_local,
                "all_patterns_in_landed_nine_family": patterns_in_family,
            }
            rows.append({
                "event_index": event_index,
                "scale": "NINE",
                "normalized_depth": depth,
                "predecessor_depth": depth + 1,
                "incoming_lane_blocks": incoming,
                "incoming_key_blocks": tuple(
                    tuple(BACKBONE[lane] for lane in block) for block in incoming
                ),
                "coincident_lane_subset": lanes,
                "coincident_key_subset": tuple(BACKBONE[lane] for lane in lanes),
                "one_step_rule":
                    "for every lane k, x_k = W_k^{-1}(y), equivalently "
                    "W_k(x_k)=y, with the exact x_k,y bytes printed below",
                "word_gate_count_by_lane": tuple(
                    len(words[BACKBONE[lane]]) for lane in lanes
                ),
                "word_sha256_by_lane": word_digests,
                "predecessor_state_packed_sha256_by_lane": tuple(
                    packed_sha256(state) for state in inputs
                ),
                "common_output_packed_sha256": packed_sha256(common_output),
                "predecessor_variation_support": variation_support,
                "predecessor_variation_support_sha256": digest(variation_support),
                "landed_nine_predicate_wires": NINE_PREDICATE_WIRES,
                "predecessor_patterns_on_landed_wires": patterns,
                "common_output_pattern_on_landed_wires":
                    predicate_pattern(common_output, NINE_PREDICATE_WIRES),
                "known_three_wire_local": three_wire_local,
                "all_patterns_in_landed_nine_family": patterns_in_family,
                "structural_precondition_type": structural_type,
                "structural_precondition_type_sha256": digest(structural_type),
                "exact_precondition_payload": payload,
                "rule_outputs_equal_printed_common_output":
                    rule_outputs == expected_outputs and len(set(rule_outputs)) == 1,
                "inverse_rule_recovers_every_printed_predecessor":
                    inverse_inputs == inputs,
                "pass": exact,
            })
            event_index += 1
    return tuple(rows)


def first_share_rows(nine: dict[str, object]) -> tuple[dict[str, object], ...]:
    states_by_depth = nine["states_by_depth"]
    seen: set[tuple[int, int]] = set()
    rows = []
    for depth in range(NORMALIZED_DEPTH, -1, -1):
        partition = partition_of(states_by_depth[depth])
        predecessor = partition_of(states_by_depth[depth + 1])
        for block in partition:
            new_pairs = tuple(
                pair for pair in combinations(block, 2) if pair not in seen
            )
            if not new_pairs:
                continue
            predecessor_equal = tuple(
                states_by_depth[depth + 1][left]
                == states_by_depth[depth + 1][right]
                for left, right in new_pairs
            )
            left_censored_pairs = tuple(
                pair for pair, equal in zip(new_pairs, predecessor_equal)
                if equal
            )
            generated_pairs = tuple(
                pair for pair, equal in zip(new_pairs, predecessor_equal)
                if not equal
            )
            if left_censored_pairs and generated_pairs:
                classification = "BOUNDARY_MIXED_CENSORED_AND_GENERATED"
            elif left_censored_pairs:
                classification = "LEFT_CENSORED_FIRST_OBSERVATION"
            else:
                classification = "GENERATED_FIRST_COINCIDENCE"
            rows.append({
                "normalized_depth": depth,
                "coincident_lane_block": block,
                "coincident_key_block": tuple(BACKBONE[lane] for lane in block),
                "new_pair_count": len(new_pairs),
                "new_lane_pairs": new_pairs,
                "left_censored_lane_pairs": left_censored_pairs,
                "generated_lane_pairs": generated_pairs,
                "left_censored_key_pairs": tuple(
                    (BACKBONE[left], BACKBONE[right])
                    for left, right in left_censored_pairs
                ),
                "generated_key_pairs": tuple(
                    (BACKBONE[left], BACKBONE[right])
                    for left, right in generated_pairs
                ),
                "new_key_pairs": tuple(
                    (BACKBONE[left], BACKBONE[right])
                    for left, right in new_pairs
                ),
                "classification": classification,
                "all_new_pairs_separate_at_depth_plus_one":
                    not any(predecessor_equal),
            })
            seen.update(new_pairs)
    if len(seen) != len(tuple(combinations(range(len(BACKBONE)), 2))):
        raise AssertionError("first-share census did not cover all 36 pairs")
    return tuple(rows)


def pair_copy_certificate(
    normalized_partitions: tuple[Partition, ...],
) -> dict[str, object]:
    pair_sequence = (True,) * (NORMALIZED_DEPTH + 1)
    sequence_sha = sha256(bytes(map(int, pair_sequence))).hexdigest()
    rle_checks = tuple({
        "event": event,
        "sample_count": sample_count,
        "partition": "UNITED",
        "computed_exact_sequence_sha256":
            sha256(b"\x01" * sample_count).hexdigest(),
        "expected_exact_sequence_sha256": expected,
        "exact": sha256(b"\x01" * sample_count).hexdigest() == expected,
    } for event, sample_count, expected in COPIED_CYCLE846["full_RLE"])
    matching = []
    restriction_rows = []
    for left, right in combinations(range(len(BACKBONE)), 2):
        restriction = tuple(
            any(left in block and right in block for block in partition)
            for partition in normalized_partitions
        )
        holds = restriction == pair_sequence
        restriction_rows.append({
            "nine_lane_subset": (left, right),
            "nine_key_subset": (BACKBONE[left], BACKBONE[right]),
            "restricted_depth_sequence_sha256":
                sha256(bytes(map(int, restriction))).hexdigest(),
            "reproduces_pair_braid": holds,
        })
        if holds:
            matching.append((BACKBONE[left], BACKBONE[right]))
    no_depth_transition = all(
        pair_sequence[depth] == pair_sequence[depth + 1]
        for depth in range(NORMALIZED_DEPTH)
    )
    result = {
        "copy_provenance": COPIED_CYCLE846,
        "two_keys": PAIR_POSITIONS,
        "landed_three_wire_representation": PAIR_PREDICATE_WIRES,
        "normalized_depth_bounds": (0, NORMALIZED_DEPTH),
        "normalized_partition": "UNITED at every depth",
        "computed_normalized_depth_sequence_sha256": sequence_sha,
        "expected_normalized_depth_sequence_sha256": EXPECTED_PAIR_DEPTH_SHA256,
        "full_meet_to_funnel_RLE_checks": rle_checks,
        "generated_coincidence_event_count": 0,
        "generated_event_reason":
            "No SEPARATE->UNITED step exists: the SHA-pinned full RLE is one "
            "UNITED row from the meet through every cohort funnel.",
        "first_observed_share": {
            "normalized_depth": NORMALIZED_DEPTH,
            "classification": "LEFT_CENSORED; PREEXISTS_WINDOW_AND_MEET",
            "one_step_coincidence_precondition": None,
        },
        "restriction_rows_every_nine_subset": tuple(restriction_rows),
        "matching_nine_key_subsets": tuple(matching),
        "matching_subset_count": len(matching),
        "expected_matching_nine_key_subsets": EXPECTED_MATCHING_NINE_SUBSETS,
        "pass": (
            sequence_sha == EXPECTED_PAIR_DEPTH_SHA256
            and all(row["exact"] for row in rle_checks)
            and no_depth_transition
            and tuple(matching) == EXPECTED_MATCHING_NINE_SUBSETS
            and len(restriction_rows) == 36
        ),
    }
    return result


def certificate_a_generative_test(
    fixtures: dict[str, object], nine: dict[str, object],
) -> tuple[dict[str, object], tuple[dict[str, object], ...]]:
    words = {pair: compile_word(fixtures["macros"], pair) for pair in BACKBONE}
    events = transition_rows(nine, words)
    first_shares = first_share_rows(nine)
    pair = pair_copy_certificate(nine["normalized_partitions"])
    event_signature = tuple(
        (row["normalized_depth"], row["incoming_lane_blocks"],
         row["coincident_lane_subset"])
        for row in events
    )
    public_nine = {
        "normalization":
            "depth 0 is the funnel; depth+1 is the one-movement predecessor",
        "depth_bounds": (0, NORMALIZED_DEPTH),
        "predecessor_depth_computed": PREDECESSOR_DEPTH,
        "normalized_partition_sha256": nine["normalized_partition_sha256"],
        "expected_normalized_partition_sha256":
            EXPECTED_NORMALIZED_PARTITION_SHA256,
        "normalized_partitions": nine["normalized_partitions"],
        "first_share_sequence": first_shares,
        "generated_one_step_coincidence_events": events,
        "generated_event_count": len(events),
        "generated_event_signature": event_signature,
        "generated_event_signature_sha256": digest(event_signature),
        "expected_generated_event_count": EXPECTED_GENERATED_EVENT_COUNT,
        "expected_generated_event_signature_sha256":
            EXPECTED_GENERATED_EVENT_SIGNATURE_SHA256,
        "all_event_preconditions_exact": all(row["pass"] for row in events),
        "terminal_matches_target": nine["terminal_matches_target"],
        "duplicate_exact_every_captured_depth":
            nine["duplicate_exact_every_captured_depth"],
    }
    result = {
        "certificate_role": "A_BRAID_GENERATIVE_TEST",
        "event_definition":
            "A generated coincidence is an output equality block at depth d "
            "receiving lanes from at least two equality blocks at depth d+1. "
            "First-share rows are separately printed, including censored depth-64 "
            "observations.",
        "nine_braid": public_nine,
        "pair_braid": pair,
        "event_sequence_is_small": len(events) < NORMALIZED_DEPTH + 1,
        "pass": (
            fixtures["public"]["pass"] and nine["pass"] and pair["pass"]
            and len(events) == EXPECTED_GENERATED_EVENT_COUNT
            and digest(event_signature)
            == EXPECTED_GENERATED_EVENT_SIGNATURE_SHA256
            and all(row["pass"] for row in events)
            and len(first_shares) >= 1
        ),
    }
    return result, events


def certificate_b_schema_hunt(
    certificate_a: dict[str, object],
    events: tuple[dict[str, object], ...],
) -> dict[str, object]:
    type_counts = Counter(
        row["structural_precondition_type_sha256"] for row in events
    )
    type_examples = {}
    for row in events:
        key = row["structural_precondition_type_sha256"]
        type_examples.setdefault(key, row["structural_precondition_type"])
    local_rows = tuple(
        row["event_index"] for row in events if row["known_three_wire_local"]
    )
    family_rows = tuple(
        row["event_index"] for row in events
        if row["all_patterns_in_landed_nine_family"]
    )
    pair_event_count = certificate_a["pair_braid"]["generated_coincidence_event_count"]
    exact_inverse_coverage = all(
        row["rule_outputs_equal_printed_common_output"]
        and row["inverse_rule_recovers_every_printed_predecessor"]
        for row in events
    )
    candidates = (
        {
            "name": "LANDED_THREE_WIRE_PATTERN_AT_SCALE_OFFSETS",
            "schema":
                "predecessor variation is confined to (40,81,105) at nine "
                "scale or (88,124,125) at pair scale, with one shared local "
                "pattern family sufficient for coincidence",
            "nine_event_coverage": len(local_rows),
            "nine_event_total": len(events),
            "nine_pattern_family_coverage": len(family_rows),
            "pair_event_coverage": 0,
            "pair_event_total": pair_event_count,
            "cross_scale_nonvacuous": bool(events) and pair_event_count > 0,
            "holds": (
                len(local_rows) == len(events)
                and bool(events) and pair_event_count > 0
            ),
            "status": "FAILS",
        },
        {
            "name": "EXACT_RULE_PREIMAGE_IDENTITY",
            "schema": "x_k=W_k^{-1}(y) for every participant k",
            "nine_event_coverage": len(events) if exact_inverse_coverage else 0,
            "nine_event_total": len(events),
            "pair_event_coverage": 0,
            "pair_event_total": pair_event_count,
            "formal_identity_holds": exact_inverse_coverage,
            "mechanism_candidate": False,
            "rejection_reason":
                "It requires the full printed predecessor/common-output states "
                "and the event depth.  It is an exact inverse-image certificate, "
                "not a local schema that predicts an event.",
            "status": "EXACT_BUT_TAUTOLOGICAL",
        },
    )
    census = tuple({
        "type_sha256": key,
        "count": type_counts[key],
        "type": type_examples[key],
    } for key in sorted(type_counts))
    return {
        "certificate_role": "B_PRECONDITION_SCHEMA_HUNT",
        "verdict": "NO_SINGLE_CROSS_SCALE_LOCAL_SCHEMA",
        "mechanism_candidate_found": False,
        "nine_generated_event_count": len(events),
        "pair_generated_event_count": pair_event_count,
        "pair_constraint":
            "The pair braid is persistently UNITED and supplies no generated "
            "one-step coincidence instance; cross-scale event coverage would be "
            "vacuous, so it cannot certify one mechanism schema.",
        "candidate_tests": candidates,
        "honest_precondition_type_census": census,
        "distinct_precondition_type_count": len(census),
        "known_three_wire_local_event_indices": local_rows,
        "landed_nine_pattern_family_event_indices": family_rows,
        "scope_boundary":
            "The exact event-specific inverse images are certificates A, not a "
            "derived predictive law.  No claim is made beyond depths 0..64.",
        "pass": (
            certificate_a["pass"] and exact_inverse_coverage
            and not any(candidate.get("holds", False) for candidate in candidates)
            and len(census) >= 1 and pair_event_count == 0
        ),
    }


def certificate_c_forward_rederivation(
    certificate_a: dict[str, object], certificate_b: dict[str, object],
) -> dict[str, object]:
    if certificate_b["mechanism_candidate_found"]:
        return {
            "certificate_role": "C_FORWARD_REDERIVATION",
            "verdict": "INTERNAL_ERROR_UNIMPLEMENTED_SCHEMA_BRANCH",
            "pass": False,
        }
    return {
        "certificate_role": "C_FORWARD_REDERIVATION",
        "verdict": "NOT_ATTEMPTED_NO_SINGLE_SCHEMA",
        "prediction": None,
        "comparison_to_nine_braid": None,
        "comparison_to_pair_braid": None,
        "why_exact_preimages_are_not_used":
            "Each exact preimage payload already contains the full states and "
            "event depth to be predicted; replaying it would be circular full-state "
            "execution, not a derivation from the marked meet plus a local schema.",
        "honest_gap":
            "The braid is reduced to named exact event preconditions, but those "
            "preconditions do not collapse to one nonvacuous local law across the "
            "nine and pair scales.  The merged why therefore remains open.",
        "certificate_a_available": certificate_a["pass"],
        "certificate_b_no_schema_exact": certificate_b["pass"],
        "pass": certificate_a["pass"] and certificate_b["pass"],
    }


def certificate_d_controls(
    source: dict[str, object], fixtures: dict[str, object],
    fixture_replay: dict[str, object], nine: dict[str, object],
    events: tuple[dict[str, object], ...], elapsed: float,
) -> dict[str, object]:
    copied_rle_exact = all(
        sha256(b"\x01" * sample_count).hexdigest() == expected
        for _event, sample_count, expected in COPIED_CYCLE846["full_RLE"]
    )
    blocked_at_end = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    result = {
        "certificate_role": "D_CONTROLS",
        "source_controls": source,
        "primary_access_policy":
            "All literal AUDIT_INPUT_PATHS and the SHA-pinned Cycle-846 copy "
            "are BLOCKLISTED and consumed only as text/AST; none is imported "
            "or executed.",
        "blocked_modules_loaded_at_end": blocked_at_end,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": {
            "fixture_decode_exact_replay":
                fixture_digest(fixtures) == fixture_digest(fixture_replay),
            "fixture_digest_first": fixture_digest(fixtures),
            "fixture_digest_replay": fixture_digest(fixture_replay),
            "nine_duplicate_exact_every_captured_depth":
                nine["duplicate_exact_every_captured_depth"],
            "event_transform_repeat_digest_exact":
                digest(events) == digest(tuple(dict(row) for row in events)),
            "every_rule_forward_inverse_roundtrip_exact":
                all(row["inverse_rule_recovers_every_printed_predecessor"]
                    for row in events),
            "copied_pair_full_RLE_hashes_exact": copied_rle_exact,
        },
        "exact_arithmetic":
            "Boolean gates, states, equality partitions, supports, event "
            "preimages, counts, bytes, and hashes are exact; wall time alone "
            "is floating point.",
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_below_limit": False,
        "base_pass_before_stdout": False,
        "pass": False,
    }
    result["base_pass_before_stdout"] = (
        source["pass"] and fixtures["public"]["pass"]
        and fixture_replay["public"]["pass"] and nine["pass"]
        and bool(events) and all(row["pass"] for row in events)
        and not blocked_at_end and not FIREWALL.hits
        and all(result["determinism"].values())
        and result["runtime_below_limit"]
    )
    return result


def render_report(
    certificate_a: dict[str, object], certificate_b: dict[str, object],
    certificate_c: dict[str, object], certificate_d: dict[str, object],
    elapsed: float,
) -> str:
    report = {
        "cycle": 848,
        "title": "the two-scale braid derivation (merged why, attempt three)",
        "checks": {
            "A_GENERATIVE_TEST": certificate_a["pass"],
            "B_SCHEMA_HUNT": certificate_b["pass"],
            "C_FORWARD_REDERIVATION": certificate_c["pass"],
            "D_CONTROLS": certificate_d["pass"],
        },
        "certificate_A_event_count":
            certificate_a["nine_braid"]["generated_event_count"],
        "certificate_B_verdict": certificate_b["verdict"],
        "certificate_C_verdict": certificate_c["verdict"],
        "merged_why_status": "OPEN_EXACT_EVENT_CENSUS_ONLY",
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": certificate_d["stdout_bytes"],
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": all(certificate_datum["pass"] for certificate_datum in (
            certificate_a, certificate_b, certificate_c, certificate_d,
        )),
        "terminal": "CYCLE848_BRAID_DERIVATION_HONEST_GAP",
    }
    return "\n".join((
        "CERTIFICATE_A_GENERATIVE_TEST=" + compact(certificate_a),
        "CERTIFICATE_B_SCHEMA_HUNT=" + compact(certificate_b),
        "CERTIFICATE_C_FORWARD_REDERIVATION=" + compact(certificate_c),
        "CERTIFICATE_D_CONTROLS=" + compact(certificate_d),
        "REPORT=" + compact(report),
    ))


def run() -> int:
    started = monotonic()
    source, trees = source_controls()
    fixtures = decode_cycle830_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    nine = evolve_nine(fixtures)
    certificate_a, events = certificate_a_generative_test(fixtures, nine)
    certificate_b = certificate_b_schema_hunt(certificate_a, events)
    certificate_c = certificate_c_forward_rederivation(certificate_a, certificate_b)
    fixture_replay = decode_cycle830_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    elapsed = monotonic() - started
    certificate_d = certificate_d_controls(
        source, fixtures, fixture_replay, nine, events, elapsed,
    )
    for _iteration in range(8):
        rendered = render_report(
            certificate_a, certificate_b, certificate_c, certificate_d, elapsed,
        )
        stdout_bytes = len((rendered + "\n").encode("utf-8"))
        below = stdout_bytes < STDOUT_LIMIT_BYTES
        pass_value = certificate_d["base_pass_before_stdout"] and below
        if (
            certificate_d["stdout_bytes"] == stdout_bytes
            and certificate_d["stdout_below_limit"] == below
            and certificate_d["pass"] == pass_value
        ):
            break
        certificate_d["stdout_bytes"] = stdout_bytes
        certificate_d["stdout_below_limit"] = below
        certificate_d["pass"] = pass_value
    rendered = render_report(
        certificate_a, certificate_b, certificate_c, certificate_d, elapsed,
    )
    if len((rendered + "\n").encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    print(rendered)
    overall = all(certificate["pass"] for certificate in (
        certificate_a, certificate_b, certificate_c, certificate_d,
    ))
    return 0 if overall else 1


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--_worker":
        return run()
    if len(sys.argv) != 1:
        raise SystemExit("usage: frontier_cycle848_braid_derivation_2026_07_28.py")
    try:
        completed = subprocess.run(
            (sys.executable, str(Path(__file__).resolve()), "--_worker"),
            cwd=ROOT, capture_output=True, text=True,
            timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired as exc:
        print(compact({
            "cycle": 848, "pass": False,
            "terminal": "CYCLE848_TIMEOUT",
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        }))
        return 1
    stdout_size = len(completed.stdout.encode("utf-8"))
    if stdout_size >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 848, "pass": False,
            "terminal": "CYCLE848_STDOUT_LIMIT_EXCEEDED",
            "stdout_bytes": stdout_size,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }))
        return 1
    sys.stdout.write(completed.stdout)
    if completed.stderr:
        sys.stderr.write(completed.stderr)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
