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
EXPECTED_INHERITED_WIRE_COUNT = 5320
EXPECTED_INHERITED_PAIR_COUNT = 14148540
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


def ranges(values: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if not values:
        return ()
    result = []
    start = previous = values[0]
    for value in values[1:]:
        if value != previous + 1:
            result.append((start, previous))
            start = value
        previous = value
    result.append((start, previous))
    return tuple(result)


def gate_target(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    return first if kind == 0 else second if kind == 1 else third


def inheritance_census(
    fixtures: dict[str, object],
    gate_words: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
) -> tuple[dict[str, object], dict[str, object]]:
    target_counts = []
    for pair in BACKBONE:
        counts: dict[int, list[int]] = defaultdict(lambda: [0, 0, 0])
        for row in gate_words[pair]:
            counts[gate_target(row)][row[0]] += 1
        target_counts.append(counts)

    profiles = {
        wire: tuple(tuple(target_counts[index][wire]) for index in range(len(BACKBONE)))
        for wire in range(STATE_BITS)
    }
    profile_groups: dict[
        tuple[tuple[int, int, int], ...], list[int]
    ] = defaultdict(list)
    for wire, profile in profiles.items():
        profile_groups[profile].append(wire)

    def x_only_signature(
        profile: tuple[tuple[int, int, int], ...],
    ) -> tuple[int, ...] | None:
        if any(cnot_count or toffoli_count
               for _x_count, cnot_count, toffoli_count in profile):
            return None
        return tuple(x_count % 2 for x_count, _cnot, _toffoli in profile)

    wire_family = tuple(
        wire for wire, profile in profiles.items()
        if x_only_signature(profile) == (0,) * len(BACKBONE)
    )
    wire_family_set = set(wire_family)
    signature_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    signature_by_wire = {}
    for wire, profile in profiles.items():
        signature = x_only_signature(profile)
        if signature is not None:
            signature_groups[signature].append(wire)
            signature_by_wire[wire] = signature
    pair_count = sum(
        len(wires) * (len(wires) - 1) // 2
        for wires in signature_groups.values()
    )

    public_profiles = []
    for profile, wires_list in sorted(
        profile_groups.items(), key=lambda item: (item[0], item[1][0]),
    ):
        wires = tuple(wires_list)
        signature = x_only_signature(profile)
        public_profiles.append({
            "wire_count": len(wires),
            "wire_ranges": ranges(wires),
            "per_generator": tuple({
                "generator": pair,
                "unconditional_X_targets": counts[0],
                "CNOT_targets": counts[1],
                "Toffoli_targets": counts[2],
            } for pair, counts in zip(BACKBONE, profile)),
            "x_only_toggle_signature": signature,
            "wire_level_admitted": signature == (0,) * len(BACKBONE),
        })
    pair_groups = tuple({
        "toggle_signature": signature,
        "wire_count": len(wires),
        "wire_ranges": ranges(tuple(wires)),
        "unordered_pair_count": len(wires) * (len(wires) - 1) // 2,
    } for signature, wires in sorted(signature_groups.items()) if len(wires) >= 2)

    invariant_mask = sum(1 << wire for wire in wire_family)
    ordered_states = tuple(fixtures["states"][key] for key in fixtures["keys"])
    initial_projection = b"".join(
        (state & invariant_mask).to_bytes(STATE_BYTES, "little")
        for state in ordered_states
    )
    initial_signatures = Counter(
        tuple((state >> wire) & 1 for state in ordered_states)
        for wire in wire_family
    )
    uniform_zero = initial_signatures.get((0,) * FAMILY_SIZE, 0)
    uniform_one = initial_signatures.get((1,) * FAMILY_SIZE, 0)
    dead_profiles = {
        wire: tuple({
            "generator": pair,
            "unconditional_X_targets": profiles[wire][index][0],
            "CNOT_targets": profiles[wire][index][1],
            "Toffoli_targets": profiles[wire][index][2],
            "boundary_relation": "x_out=x_in",
        } for index, pair in enumerate(BACKBONE))
        for wire in (56, 58)
    }
    dead_initial = {
        wire: sum((state >> wire) & 1 for state in ordered_states)
        for wire in (56, 58)
    }
    dead_special = {
        "wires": (56, 58),
        "wire_56_in_wire_family": 56 in wire_family_set,
        "wire_58_in_wire_family": 58 in wire_family_set,
        "pair_56_58_in_pair_family": (
            signature_by_wire.get(56) == signature_by_wire.get(58)
            and signature_by_wire.get(56) is not None
        ),
        "all_176_initial_one_counts": dead_initial,
        "forced_boundary_values": (0, 0),
        "forced_boundary_parity": 0,
        "per_wire_per_generator": dead_profiles,
        "cycle853_special_case_reappears": (
            dead_initial == {56: 0, 58: 0}
            and all(
                row["unconditional_X_targets"] == 4
                and row["CNOT_targets"] == 0
                and row["Toffoli_targets"] == 0
                for wire in (56, 58) for row in dead_profiles[wire]
            )
        ),
    }
    profile_coverage = sum(row["wire_count"] for row in public_profiles)
    certificate = {
        "declared_inheritance_ladder": (
            "LEVEL_1_SINGLE_WIRE_VALUE",
            "LEVEL_2_UNORDERED_WIRE_PAIR_PARITY",
        ),
        "derivation_rule": (
            "At a complete F_pair boundary, a single wire is inherited iff every "
            "primitive targeting it is an unconditional X and the X count is even "
            "for each of the nine generators (zero is even).  A wire-pair parity "
            "is inherited iff both target lists are X-only and their X-count "
            "parities agree generator by generator.  Conditional target gates "
            "are never cancelled or inferred from trajectory behavior."
        ),
        "all_wire_boundary_toggle_structures": tuple(public_profiles),
        "all_wire_profile_group_count": len(public_profiles),
        "all_wire_profile_coverage": profile_coverage,
        "all_wire_profiles_sha256": digest(tuple(profiles.items())),
        "level_1": {
            "family_count": len(wire_family),
            "family_wire_ranges": ranges(wire_family),
            "family_sha256": digest(wire_family),
            "nonfamily_count": STATE_BITS - len(wire_family),
            "nonfamily_wire_ranges": ranges(tuple(
                wire for wire in range(STATE_BITS) if wire not in wire_family_set
            )),
            "boundary_theorem":
                "x_t[w]=x_0[w] at every complete-generator boundary",
            "initial_projection_sha256": sha256(initial_projection).hexdigest(),
            "uniform_zero_initial_wires": uniform_zero,
            "uniform_one_initial_wires": uniform_one,
            "nonuniform_initial_wires":
                len(wire_family) - uniform_zero - uniform_one,
        },
        "level_2": {
            "family_count": pair_count,
            "compressed_complete_family": pair_groups,
            "family_definition":
                "For every displayed signature group, every unordered distinct "
                "pair of listed wires is in the family; there are no other pairs.",
            "boundary_theorem":
                "x_t[a] XOR x_t[b] = x_0[a] XOR x_0[b] at every complete-generator boundary",
            "family_sha256": digest(tuple(
                (signature, tuple(wires))
                for signature, wires in sorted(signature_groups.items())
                if len(wires) >= 2
            )),
        },
        "dead_wire_pair_special_case": dead_special,
        "trajectory_cooccurrence_used_for_admission": False,
        "finding": "FULL_TWO_LEVEL_EVEN_TOGGLE_INHERITANCE_FAMILY_CERTIFIED",
        "pass": (
            profile_coverage == STATE_BITS
            and len(wire_family) == EXPECTED_INHERITED_WIRE_COUNT
            and pair_count == EXPECTED_INHERITED_PAIR_COUNT
            and dead_special["cycle853_special_case_reappears"]
            and dead_special["pair_56_58_in_pair_family"]
        ),
    }
    private = {
        "wire_family": wire_family_set,
        "signature_by_wire": signature_by_wire,
        "signature_groups": {
            signature: tuple(wires) for signature, wires in signature_groups.items()
        },
    }
    return certificate, private


def occurrence_entailment(
    event: dict[str, object], fixtures: dict[str, object],
    inheritance: dict[str, object],
) -> dict[str, object]:
    component_wires = tuple(sorted(set(PREDICATE_WIRES) | set(
        event["predecessor_variation_support"]
    )))
    wire_family = inheritance["wire_family"]
    signature_by_wire = inheritance["signature_by_wire"]
    signature_groups = inheritance["signature_groups"]
    pattern_rows = []
    free_components = []
    constraint_rank = 0
    consistency = True
    for lane, key, state in zip(
        event["coincident_lanes"], event["coincident_keys"],
        event["predecessor_states"],
    ):
        initial = fixtures["states"][(0, key)]
        selected_by_signature: dict[tuple[int, ...], list[int]] = defaultdict(list)
        conditional_wires = []
        for wire in component_wires:
            signature = signature_by_wire.get(wire)
            if signature is None:
                conditional_wires.append(wire)
            else:
                selected_by_signature[signature].append(wire)
        forced_values = []
        forced_relations = []
        lane_free = []
        for wire in conditional_wires:
            lane_free.append(wire)
        for signature, selected in sorted(selected_by_signature.items()):
            anchors = tuple(
                wire for wire in signature_groups[signature]
                if wire in wire_family
            )
            if anchors:
                anchor = anchors[0]
                for wire in selected:
                    expected = (initial >> wire) & 1
                    actual = (state >> wire) & 1
                    forced_values.append((wire, expected))
                    consistency &= actual == expected
                    constraint_rank += 1
            else:
                representative = min(selected)
                lane_free.append(representative)
                for wire in sorted(selected):
                    if wire == representative:
                        continue
                    expected_parity = ((initial >> representative) ^ (initial >> wire)) & 1
                    actual_parity = ((state >> representative) ^ (state >> wire)) & 1
                    forced_relations.append((representative, wire, expected_parity))
                    consistency &= actual_parity == expected_parity
                    constraint_rank += 1
        required_values = tuple((state >> wire) & 1 for wire in component_wires)
        for wire in sorted(lane_free):
            free_components.append({
                "event_index": event["event_index"],
                "key": key,
                "wire": wire,
                "required_value": (state >> wire) & 1,
            })
        pattern_rows.append({
            "lane": lane,
            "key": key,
            "component_wires": component_wires,
            "required_values": required_values,
            "forced_wire_values": tuple(forced_values),
            "forced_pair_relations": tuple(forced_relations),
            "free_basis_wires": tuple(sorted(lane_free)),
        })
    cell_count = len(component_wires) * len(event["coincident_keys"])
    if constraint_rank == cell_count:
        verdict = "INHERITED"
    elif constraint_rank == 0:
        verdict = "FREE"
    else:
        verdict = "MIXED"
    return {
        "event_index": event["event_index"],
        "normalized_depth": event["normalized_depth"],
        "predecessor_depth": event["predecessor_depth"],
        "keys": event["coincident_keys"],
        "component_scope": (
            "Cycle-848 structural precondition components: exact predecessor "
            "variation-support wires plus landed predicate wires (40,81,105)."
        ),
        "component_wires": component_wires,
        "state_component_pattern_by_key": tuple(pattern_rows),
        "component_cell_count": cell_count,
        "inherited_constraint_rank": constraint_rank,
        "free_degree_count": len(free_components),
        "free_components": tuple(free_components),
        "observed_pattern_satisfies_derived_constraints": consistency,
        "verdict": verdict,
    }


def precondition_entailment(
    events: tuple[dict[str, object], ...], fixtures: dict[str, object],
    inheritance: dict[str, object],
) -> dict[str, object]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    structural_types = {}
    for event in events:
        key = event["type_sha256"]
        grouped[key].append(occurrence_entailment(event, fixtures, inheritance))
        structural_types[key] = event["structural_precondition_type"]
    type_rows = []
    for index, key in enumerate(sorted(grouped), 1):
        occurrences = tuple(grouped[key])
        cells = sum(row["component_cell_count"] for row in occurrences)
        rank = sum(row["inherited_constraint_rank"] for row in occurrences)
        free = tuple(
            component for row in occurrences for component in row["free_components"]
        )
        verdict = "INHERITED" if rank == cells else "FREE" if rank == 0 else "MIXED"
        type_rows.append({
            "type_id": f"T{index:02d}",
            "type_sha256": key,
            "cycle848_structural_type": structural_types[key],
            "occurrence_count": len(occurrences),
            "occurrences": occurrences,
            "component_cell_count": cells,
            "inherited_constraint_rank": rank,
            "free_degree_count": len(free),
            "free_components": free,
            "verdict": verdict,
            "entailment_basis": (
                "Only the level-1 fixed wire values and level-2 fixed pair "
                "parities derived in A are used.  Trajectory occurrence is used "
                "only to state the target pattern, never to prove entailment."
            ),
        })
    certificate = {
        "cycle848_generated_event_count": len(events),
        "cycle848_precondition_type_count": len(type_rows),
        "declared_component_scope": (
            "For each Cycle-848 structural precondition occurrence, the state-component "
            "pattern is the exact bit assignment on its predecessor variation support "
            "union (40,81,105), separately at the printed predecessor depth and keys."
        ),
        "declared_inheritance_levels_used": (
            "LEVEL_1_SINGLE_WIRE_VALUE",
            "LEVEL_2_UNORDERED_WIRE_PAIR_PARITY",
        ),
        "per_type": tuple(type_rows),
        "trajectory_cooccurrence_used_as_entailment": False,
        "finding": "ALL_16_BRAID_PRECONDITION_TYPES_CLASSIFIED_BY_DERIVATION",
        "pass": (
            len(events) == EXPECTED_EVENT_COUNT
            and len(type_rows) == EXPECTED_TYPE_COUNT
            and sum(row["occurrence_count"] for row in type_rows)
            == EXPECTED_EVENT_COUNT
            and all(
                occurrence["observed_pattern_satisfies_derived_constraints"]
                for row in type_rows for occurrence in row["occurrences"]
            )
            and all(row["verdict"] in {"INHERITED", "MIXED", "FREE"}
                    for row in type_rows)
        ),
    }
    return certificate


def analyze_once(fixtures: dict[str, object]) -> dict[str, object]:
    gate_words = build_gate_words(fixtures["macros"])
    certificate_a, private = inheritance_census(fixtures, gate_words)
    nine = evolve_nine(fixtures)
    events = transition_rows(nine, compile_words(gate_words))
    certificate_b = precondition_entailment(events, fixtures, private)
    return {
        "A_INHERITANCE_CENSUS": certificate_a,
        "B_BRAID_PRECONDITION_ENTAILMENT": certificate_b,
        "nine_reconstruction": {
            key: value for key, value in nine.items() if key != "states_by_depth"
        },
        "event_census_sha256": digest(tuple({
            key: value for key, value in event.items()
            if key != "predecessor_states"
        } for event in events)),
    }


def decomposition(certificate_b: dict[str, object]) -> dict[str, object]:
    verdict_counts = Counter(row["verdict"] for row in certificate_b["per_type"])
    inherited = verdict_counts["INHERITED"]
    mixed = verdict_counts["MIXED"]
    free = verdict_counts["FREE"]
    if inherited == EXPECTED_TYPE_COUNT:
        verdict = "INITIAL_CONDITION_INHERITED_MECHANISM_CANDIDATE_NOT_CLOSURE"
        finding = "ALL_16_TYPES_INHERITED_MECHANISM_CANDIDATE_FOUND_NOT_CLOSURE"
    elif 0 < inherited < EXPECTED_TYPE_COUNT:
        verdict = "MERGED_WHY_DECOMPOSES"
        finding = "PARTIAL_INHERITANCE_DECOMPOSES_THE_MERGED_WHY"
    else:
        verdict = "INHERITANCE_MECHANISM_DOES_NOT_REACH_BRAID_AT_DECLARED_LEVELS"
        finding = "ZERO_TYPES_INHERITED_BOUNDED_NEGATIVE_AT_DECLARED_LEVELS"
    mysterious = tuple(
        row["type_id"] for row in certificate_b["per_type"]
        if row["verdict"] != "INHERITED"
    )
    result = {
        "inherited_types": inherited,
        "mixed_types": mixed,
        "free_types": free,
        "total_types": EXPECTED_TYPE_COUNT,
        "decomposition": f"{inherited}/16 inherited, {mixed}/16 mixed, {free}/16 free",
        "mysterious_types": mysterious,
        "verdict": verdict,
        "candidate_not_closure": inherited == EXPECTED_TYPE_COUNT,
        "bounded_scope": (
            "Complete-generator boundaries; declared ladder of single-wire values "
            "then unordered wire-pair parities; Cycle-848 depths 0..64 and its "
            "structural state-component preconditions only."
        ),
        "finding": finding,
        "pass": (
            inherited + mixed + free == EXPECTED_TYPE_COUNT
            and certificate_b["pass"]
            and (
                (inherited == EXPECTED_TYPE_COUNT and result_case(verdict, "candidate"))
                or (0 < inherited < EXPECTED_TYPE_COUNT and result_case(verdict, "decomposes"))
                or (inherited == 0 and result_case(verdict, "negative"))
            )
        ),
    }
    return result


def result_case(verdict: str, case: str) -> bool:
    expected = {
        "candidate": "INITIAL_CONDITION_INHERITED_MECHANISM_CANDIDATE_NOT_CLOSURE",
        "decomposes": "MERGED_WHY_DECOMPOSES",
        "negative": "INHERITANCE_MECHANISM_DOES_NOT_REACH_BRAID_AT_DECLARED_LEVELS",
    }
    return verdict == expected[case]


def run() -> int:
    started = monotonic()
    sources, trees = source_controls()
    fixtures_first = decode_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    first = analyze_once(fixtures_first)
    fixtures_second = decode_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    second = analyze_once(fixtures_second)
    deterministic = first == second
    certificate_a = first["A_INHERITANCE_CENSUS"]
    certificate_b = first["B_BRAID_PRECONDITION_ENTAILMENT"]
    certificate_c = decomposition(certificate_b)
    elapsed = monotonic() - started
    blocked_at_end = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    controls_base = (
        sources["pass"]
        and fixtures_first["public"]["pass"]
        and fixtures_second["public"]["pass"]
        and deterministic
        and first["nine_reconstruction"]["pass"]
        and second["nine_reconstruction"]["pass"]
        and not blocked_at_end
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificate_d = {
        "source_controls": sources,
        "fixture_reconstruction_first": fixtures_first["public"],
        "fixture_reconstruction_second": fixtures_second["public"],
        "primary_access_policy": (
            "Every literal AUDIT_INPUT_PATHS entry is SHA/blob pinned, BLOCKLISTED, "
            "and consumed as text/AST only; no frontier primary is imported or executed."
        ),
        "determinism_replay": {
            "exact": deterministic,
            "first_sha256": digest(first),
            "second_sha256": digest(second),
            "nine_first": first["nine_reconstruction"],
            "nine_second": second["nine_reconstruction"],
            "event_census_first_sha256": first["event_census_sha256"],
            "event_census_second_sha256": second["event_census_sha256"],
        },
        "blocked_modules_loaded_at_end": blocked_at_end,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_below_limit": False,
        "finding": "CONTROLS_FAIL",
        "pass": False,
    }
    certificates = {
        "A_INHERITANCE_CENSUS": certificate_a,
        "B_BRAID_PRECONDITION_ENTAILMENT": certificate_b,
        "C_DECOMPOSITION": certificate_c,
        "D_CONTROLS": certificate_d,
    }
    checks = {
        "A_INHERITANCE_CENSUS": bool(certificate_a["pass"]),
        "B_BRAID_PRECONDITION_ENTAILMENT": bool(certificate_b["pass"]),
        "C_DECOMPOSITION": bool(certificate_c["pass"]),
        "D_CONTROLS": False,
    }
    report = {
        "cycle": 854,
        "title": "the inheritance attack on the braid",
        "decomposition": certificate_c["decomposition"],
        "inherited_wire_count": certificate_a["level_1"]["family_count"],
        "inherited_pair_parity_count": certificate_a["level_2"]["family_count"],
        "verdict": certificate_c["verdict"],
        "runtime_seconds": round(elapsed, 6),
        "checks": {},
        "pass": False,
        "terminal": "CYCLE854_BRAID_INHERITANCE_HONEST_FAIL",
    }

    def render() -> str:
        lines = []
        for name, value in certificates.items():
            lines.append(f"{name}: {'PASS' if checks[name] else 'FAIL'}")
            lines.append(f"{name}_FINDING={value['finding']}")
            lines.append(f"{name}_CERTIFICATE={compact(value)}")
        lines.append(f"REPORT={compact(report)}")
        return "\n".join(lines) + "\n"

    for _iteration in range(12):
        certificate_d["pass"] = controls_base
        certificate_d["finding"] = (
            "CONTROLS_PASS" if certificate_d["pass"] else "CONTROLS_FAIL"
        )
        checks["D_CONTROLS"] = certificate_d["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE854_BRAID_INHERITANCE_PASS"
            if report["pass"] else "CYCLE854_BRAID_INHERITANCE_HONEST_FAIL"
        )
        output = render()
        stdout_bytes = len(output.encode("utf-8"))
        certificate_d["stdout_bytes"] = stdout_bytes
        certificate_d["stdout_below_limit"] = stdout_bytes < STDOUT_LIMIT_BYTES
        controls_base = controls_base and stdout_bytes < STDOUT_LIMIT_BYTES
    output = render()
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 854,
            "pass": False,
            "terminal": "CYCLE854_STDOUT_LIMIT_EXCEEDED",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }))
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--_worker":
        try:
            return run()
        except Exception as error:
            print(compact({
                "cycle": 854,
                "pass": False,
                "terminal": "CYCLE854_BRAID_INHERITANCE_HONEST_FAIL",
                "exception_type": type(error).__name__,
                "exception": str(error),
            }))
            return 1
    if len(sys.argv) != 1:
        raise SystemExit("usage: frontier_cycle854_braid_inheritance_2026_07_28.py")
    try:
        completed = subprocess.run(
            (sys.executable, str(Path(__file__).resolve()), "--_worker"),
            cwd=ROOT, capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        print(compact({
            "cycle": 854,
            "pass": False,
            "terminal": "CYCLE854_TIMEOUT",
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        }))
        return 1
    stdout_bytes = len(completed.stdout.encode("utf-8"))
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 854,
            "pass": False,
            "terminal": "CYCLE854_STDOUT_LIMIT_EXCEEDED",
            "stdout_bytes": stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }))
        return 1
    sys.stdout.write(completed.stdout)
    if completed.stderr:
        sys.stderr.write(completed.stderr)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
