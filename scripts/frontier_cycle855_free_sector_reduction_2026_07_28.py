#!/usr/bin/env python3
"""Cycle 855: exact reachable reduction to the Cycle-854 free sector.

The Cycle-854 inheritance family is recomputed from Cycle-830 primitive gate
fixtures.  Cited scientific primaries are SHA/blob pinned, parsed as text/AST
only, and blocked from import.  Closure is tested on the complete Cycle-853
boundary census, generator by generator, before any reduced machine is named.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle848_braid_derivation_2026_07_28.py",
    "scripts/frontier_cycle853_generator_usage_census_2026_07_28.py",
    "scripts/frontier_cycle854_braid_inheritance_2026_07_28.py",
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
import tempfile
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR28-20260729"
EXPECTED_BASE = "eaa53c423ee6f7d854ad35cd2bc0f240c7fee0dc"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[1]:
        "a9fdefbffe16495e62258804d3abbddb48aaa500e365f56c739c24959162ca48",
    AUDIT_INPUT_PATHS[2]:
        "946a2ffcbb3ddad19ff2213831593f7ea93a97d9a680fec50a674391592863b7",
    AUDIT_INPUT_PATHS[3]:
        "348c78729f97cb8f5b7c1da53bbf4ee18e8a89a5860a622721a937d36196f754",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[1]: "c55036475e2389565b1c4b69e96595db99e03779",
    AUDIT_INPUT_PATHS[2]: "b28e895ffa847973a5a8ae594d3eb7796b0bc018",
    AUDIT_INPUT_PATHS[3]: "d59753105863646fbd443e74ebe5406224b95c67",
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

RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
EVENTS = (0, 2, 1)
RESOLUTION_MOMENTS = {0: 14744, 2: 33195, 1: 51115}
FULL_REACHABLE_STATES = 891513
FULL_LANDED_TRANSITIONS = 891486
NINE_FUNNEL_MOVEMENT = 14739
NORMALIZED_DEPTH = 64
PREDECESSOR_DEPTH = NORMALIZED_DEPTH + 1
PREDICATE_WIRES = (40, 81, 105)
K3_MARK_BITS = (256, 262)
EXPECTED_EVENT_COUNT = 20
EXPECTED_TYPE_COUNT = 16
EXPECTED_INHERITED_WIRE_COUNT = 5320
EXPECTED_INHERITED_PAIR_COUNT = 14148540
EXPECTED_FREE_WIRE_COUNT = STATE_BITS - EXPECTED_INHERITED_WIRE_COUNT
EXPECTED_EVENT_SIGNATURE_SHA256 = (
    "7ae45bbd8b6e688b9abdadd0e33dcfd300e2649b4776386a5b8ec48eb62e064a"
)
EXPECTED_NORMALIZED_PARTITION_SHA256 = (
    "726b74aefc7afa6e1790c7dc73a59eacdadeec72246e19ac01104be09d49829d"
)
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
    bases = {
        "cycle830_literal_fixture_basis": {
            "decode_fixtures", "build_words", "apply_word",
        } <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle848_braid_basis": {
            "evolve_nine", "transition_rows", "certificate_b_schema_hunt",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle853_reachable_census_basis": {
            "build_masked_schedule", "write_kernel_inputs", "execute_kernel",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle854_inheritance_basis": {
            "inheritance_census", "precondition_entailment", "decomposition",
        } <= function_names(trees[AUDIT_INPUT_PATHS[3]]),
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
            literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "EVENTS") == EVENTS
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "RESOLUTION_MOMENTS"
            ) == RESOLUTION_MOMENTS
            and literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "STATE_BITS")
            == STATE_BITS
        ),
        "cycle854_counts_exact": (
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "EXPECTED_INHERITED_WIRE_COUNT"
            ) == EXPECTED_INHERITED_WIRE_COUNT
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "EXPECTED_INHERITED_PAIR_COUNT"
            ) == EXPECTED_INHERITED_PAIR_COUNT
        ),
    }
    actual_sha = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    actual_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
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
        "AST_basis": bases,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "text_AST_only": AUDIT_INPUT_PATHS,
        "cycle854_certificate_parsed": False,
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
        and all(bases.values())
        and not public["direct_frontier_imports"]
        and not FIREWALL.hits
        and public["branch_exact"]
        and base_is_ancestor
    )
    return public, trees


def lawful_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


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
        (event, pair) for event in range(2 * FIXTURE_BANKS)
        for pair in lawful_pairs()
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
        "macros": tuple(macros), "states": states,
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


def gate_target(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    return first if kind == 0 else second if kind == 1 else third


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


def inheritance_reconstruction(
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> tuple[dict[str, object], dict[str, object]]:
    target_counts = []
    for pair in BACKBONE:
        counts: dict[int, list[int]] = defaultdict(lambda: [0, 0, 0])
        for row in words[pair]:
            counts[gate_target(row)][row[0]] += 1
        target_counts.append(counts)
    profiles = {
        wire: tuple(tuple(counts[wire]) for counts in target_counts)
        for wire in range(STATE_BITS)
    }

    def x_signature(profile: tuple[tuple[int, int, int], ...]) -> tuple[int, ...] | None:
        if any(cnot or toffoli for _x, cnot, toffoli in profile):
            return None
        return tuple(x_count % 2 for x_count, _cnot, _toffoli in profile)

    signature_by_wire = {
        wire: signature for wire, profile in profiles.items()
        if (signature := x_signature(profile)) is not None
    }
    signature_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for wire, signature in signature_by_wire.items():
        signature_groups[signature].append(wire)
    zero_signature = (0,) * len(BACKBONE)
    inherited = tuple(
        wire for wire in range(STATE_BITS)
        if signature_by_wire.get(wire) == zero_signature
    )
    inherited_set = set(inherited)
    free = tuple(wire for wire in range(STATE_BITS) if wire not in inherited_set)
    free_set = set(free)
    pair_count = sum(
        len(group) * (len(group) - 1) // 2
        for group in signature_groups.values()
    )
    pair_family_groups = tuple(
        (signature, tuple(group))
        for signature, group in sorted(signature_groups.items())
        if len(group) >= 2
    )
    free_wires_in_pair_family = tuple(sorted({
        wire for _signature, group in pair_family_groups for wire in group
        if wire in free_set
    }))

    support_rows = []
    for pair in BACKBONE:
        free_targets = set()
        free_controls = set()
        inherited_controls = set()
        inherited_to_free = set()
        free_to_free = set()
        channels = Counter()
        for kind, first, second, third in words[pair]:
            target = first if kind == 0 else second if kind == 1 else third
            controls = () if kind == 0 else (first,) if kind == 1 else (first, second)
            if target in free_set:
                free_targets.add(target)
                for control in controls:
                    if control in inherited_set:
                        inherited_controls.add(control)
                        inherited_to_free.add((control, target))
                        channels[f"{kind}:INHERITED_CONTROL_TO_FREE_TARGET"] += 1
                    else:
                        free_controls.add(control)
                        free_to_free.add((control, target))
                        channels[f"{kind}:FREE_CONTROL_TO_FREE_TARGET"] += 1
        support_rows.append({
            "generator": pair,
            "free_target_count": len(free_targets),
            "free_target_ranges": ranges(tuple(sorted(free_targets))),
            "free_control_count": len(free_controls),
            "free_control_ranges": ranges(tuple(sorted(free_controls))),
            "inherited_control_count": len(inherited_controls),
            "inherited_control_ranges": ranges(tuple(sorted(inherited_controls))),
            "inherited_to_free_channel_count": len(inherited_to_free),
            "free_to_free_channel_count": len(free_to_free),
            "primitive_channel_counts": tuple(sorted(channels.items())),
        })

    private = {
        "profiles": profiles,
        "signature_by_wire": signature_by_wire,
        "signature_groups": {
            key: tuple(value) for key, value in signature_groups.items()
        },
        "inherited_wires": inherited,
        "free_wires": free,
    }
    certificate = {
        "reconstruction_basis": (
            "Independent primitive-target census of all 6,212 gates in each "
            "BACKBONE generator; no Cycle-854 result row is parsed."
        ),
        "inherited_wire_count": len(inherited),
        "inherited_wire_ranges": ranges(inherited),
        "inherited_pair_parity_count": pair_count,
        "inherited_pair_family_group_count": len(pair_family_groups),
        "pair_family_is_exactly_all_unordered_inherited_wire_pairs": (
            len(pair_family_groups) == 1
            and pair_family_groups[0][0] == zero_signature
            and pair_family_groups[0][1] == inherited
            and pair_count == len(inherited) * (len(inherited) - 1) // 2
        ),
        "free_wires_in_inherited_pair_parity_family":
            free_wires_in_pair_family,
        "free_wire_count": len(free),
        "free_wire_ranges": ranges(free),
        "free_wire_sha256": digest(free),
        "support_map": tuple(support_rows),
        "finding": "FREE_COMPLEMENT_RECOMPUTED",
        "pass": (
            len(inherited) == EXPECTED_INHERITED_WIRE_COUNT
            and pair_count == EXPECTED_INHERITED_PAIR_COUNT
            and len(free) == EXPECTED_FREE_WIRE_COUNT
            and len(pair_family_groups) == 1
            and pair_family_groups[0][0] == zero_signature
            and pair_family_groups[0][1] == inherited
            and not free_wires_in_pair_family
            and set(inherited).isdisjoint(free)
            and len(inherited) + len(free) == STATE_BITS
        ),
    }
    return certificate, private


def compile_words(
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> dict[tuple[int, int], tuple[tuple[int, int, int], ...]]:
    compiled = {}
    for pair, word in words.items():
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
        compiled[pair] = tuple(rows)
    return compiled


def apply_compiled(
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


def partition_of(states: tuple[object, ...]) -> tuple[tuple[int, ...], ...]:
    groups: dict[object, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(sorted(
        (tuple(group) for group in groups.values()), key=lambda group: group[0],
    ))


def evolve_nine(fixtures: dict[str, object]) -> dict[str, object]:
    states_fixture = fixtures["states"]
    macros = fixtures["macros"]
    assert isinstance(states_fixture, dict) and isinstance(macros, tuple)
    initial = tuple(states_fixture[(0, pair)] for pair in BACKBONE)
    columns = bit_slice(initial)
    schedule = movement_schedule(macros)
    tail = []
    for movement in range(1, NINE_FUNNEL_MOVEMENT + 1):
        advance(columns, schedule)
        if movement >= NINE_FUNNEL_MOVEMENT - PREDECESSOR_DEPTH:
            tail.append(capture_lanes(columns, len(BACKBONE)))
    states_by_depth = tuple(reversed(tail))
    partitions = tuple(
        partition_of(states)
        for states in states_by_depth[:NORMALIZED_DEPTH + 1]
    )
    public = {
        "captured_depth_count": len(states_by_depth),
        "movement_schedule_rows": len(schedule),
        "normalized_partition_sha256": digest(partitions),
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
    return {"states_by_depth": states_by_depth, "public": public}


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
    assert isinstance(states_by_depth, tuple)
    rows = []
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
                apply_compiled(inputs_at_depth[lane], words[BACKBONE[lane]])
                for lane in lanes
            )
            common_output = expected_outputs[0]
            inverse_inputs = tuple(
                apply_compiled(
                    common_output, words[BACKBONE[lane]], reverse=True,
                )
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
            rows.append({
                "event_index": len(rows),
                "normalized_depth": depth,
                "predecessor_depth": depth + 1,
                "incoming_lane_blocks": incoming,
                "coincident_lanes": lanes,
                "coincident_keys": tuple(BACKBONE[lane] for lane in lanes),
                "predecessor_states": inputs,
                "successor_states": expected_outputs,
                "predecessor_variation_support": variation_support,
                "structural_precondition_type": structural_type,
                "type_sha256": digest(structural_type),
                "pass": (
                    len(set(expected_outputs)) == 1
                    and rule_outputs == expected_outputs
                    and inverse_inputs == inputs
                ),
            })
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


def project_state(state: int, free_wires: tuple[int, ...]) -> bytes:
    packed = bytearray((len(free_wires) + 7) // 8)
    for index, wire in enumerate(free_wires):
        if (state >> wire) & 1:
            packed[index >> 3] |= 1 << (index & 7)
    return bytes(packed)


def free_support_certificate(
    base: dict[str, object], private: dict[str, object],
    events: tuple[dict[str, object], ...],
) -> dict[str, object]:
    inherited = set(private["inherited_wires"])
    free = set(private["free_wires"])
    signature_by_wire = private["signature_by_wire"]
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    structural_types = {}
    for event in events:
        grouped[event["type_sha256"]].append(event)
        structural_types[event["type_sha256"]] = event["structural_precondition_type"]
    type_rows = []
    for index, key in enumerate(sorted(grouped), 1):
        occurrences = grouped[key]
        supports = tuple(sorted(set(
            tuple(sorted(set(PREDICATE_WIRES) | set(
                occurrence["predecessor_variation_support"]
            )))
            for occurrence in occurrences
        )))
        union = tuple(sorted({wire for support in supports for wire in support}))
        type_rows.append({
            "type_id": f"T{index:02d}",
            "type_sha256": key,
            "occurrence_count": len(occurrences),
            "cycle848_structural_type": structural_types[key],
            "exact_support_variants": supports,
            "exact_support_union": union,
            "inside_free_complement": tuple(wire for wire in union if wire in free),
            "outside_free_complement": tuple(wire for wire in union if wire not in free),
            "all_support_wires_free": set(union) <= free,
        })
    mark_rows = tuple({
        "wire": wire,
        "inside_free_complement": wire in free,
        "inside_inherited_wire_family": wire in inherited,
        "x_only_toggle_signature": signature_by_wire.get(wire),
    } for wire in K3_MARK_BITS)
    mark_pair_inherited = (
        signature_by_wire.get(K3_MARK_BITS[0]) is not None
        and signature_by_wire.get(K3_MARK_BITS[0])
        == signature_by_wire.get(K3_MARK_BITS[1])
    )
    result = {
        **base,
        "braid_precondition_type_count": len(type_rows),
        "braid_type_support_map": tuple(type_rows),
        "braid_all_16_type_supports_inside_free_complement": all(
            row["all_support_wires_free"] for row in type_rows
        ),
        "k3_mark_bits": mark_rows,
        "k3_mark_pair_inside_inherited_pair_parity_family": mark_pair_inherited,
        "finding": "FREE_COMPLEMENT_AND_BRAID_SUPPORTS_CERTIFIED",
    }
    result["pass"] = (
        base["pass"]
        and len(type_rows) == EXPECTED_TYPE_COUNT
        and sum(row["occurrence_count"] for row in type_rows)
        == EXPECTED_EVENT_COUNT
        and result["braid_all_16_type_supports_inside_free_complement"]
        and all(
            row["inside_free_complement"] != row["inside_inherited_wire_family"]
            for row in mark_rows
        )
    )
    return result


def build_masked_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for phase in range(RING_STATIONS):
        masks = [0] * RING_STATIONS
        for lane, (_event, pair) in enumerate(lanes):
            masks[(pair[0] + phase) % RING_STATIONS] |= 1 << lane
            masks[(pair[1] + phase) % RING_STATIONS] |= 1 << lane
        for station, macro in enumerate(macros):
            if masks[station]:
                rows.extend((*row, masks[station]) for row in macro)
    return tuple(rows)


KERNEL_C = r'''#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define STATE_BITS 5815
#define FREE_WIRES 495
#define FREE_BYTES ((FREE_WIRES + 7) / 8)
#define LANES 27
#define GENERATORS 9
#define MAX_STEPS 51115
#define FULL_STATES 891513
#define FULL_TRANSITIONS 891486

typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c; uint32_t mask;
} MaskedGate;
typedef struct __attribute__((packed)) {
    uint8_t free_bits[FREE_BYTES]; uint8_t inherited_class;
} StateRecord;
typedef struct __attribute__((packed)) {
    uint8_t input[FREE_BYTES], output[FREE_BYTES];
    uint8_t generator, inherited_class, lane; uint32_t time;
} Transition;
typedef struct __attribute__((packed)) {
    uint8_t input[FREE_BYTES], output[FREE_BYTES]; uint8_t generator;
} Probe;

static void die(const char *message) { perror(message); exit(2); }
static void *load_exact(const char *path, size_t item_size, size_t *count) {
    FILE *f = fopen(path, "rb"); if (!f) die(path);
    if (fseek(f, 0, SEEK_END)) die("fseek");
    long bytes = ftell(f); if (bytes < 0 || bytes % (long)item_size) die("size");
    rewind(f); void *p = malloc((size_t)bytes ? (size_t)bytes : 1); if (!p) die("malloc");
    if (bytes && fread(p, 1, (size_t)bytes, f) != (size_t)bytes) die("fread");
    fclose(f); *count = (size_t)bytes / item_size; return p;
}
static uint32_t active_for_state(int time) {
    uint32_t mask = 0;
    if (time <= 14744) mask |= (UINT32_C(1) << 9) - 1;
    if (time <= 33195) mask |= ((UINT32_C(1) << 9) - 1) << 9;
    if (time <= 51115) mask |= ((UINT32_C(1) << 9) - 1) << 18;
    return mask;
}
static uint32_t active_for_transition(int time) {
    uint32_t mask = 0;
    if (time < 14744) mask |= (UINT32_C(1) << 9) - 1;
    if (time < 33195) mask |= ((UINT32_C(1) << 9) - 1) << 9;
    if (time < 51115) mask |= ((UINT32_C(1) << 9) - 1) << 18;
    return mask;
}
static void pack_free(
    uint8_t out[FREE_BYTES], const uint32_t columns[STATE_BITS],
    const uint16_t free_wires[FREE_WIRES], int lane
) {
    memset(out, 0, FREE_BYTES);
    for (int i = 0; i < FREE_WIRES; ++i)
        if ((columns[free_wires[i]] >> lane) & 1U)
            out[i >> 3] |= (uint8_t)(1U << (i & 7));
}
static int state_cmp(const void *left_raw, const void *right_raw) {
    const StateRecord *left = left_raw, *right = right_raw;
    int order = memcmp(left->free_bits, right->free_bits, FREE_BYTES);
    if (order) return order;
    return (left->inherited_class > right->inherited_class)
        - (left->inherited_class < right->inherited_class);
}
static int transition_cmp(const void *left_raw, const void *right_raw) {
    const Transition *left = left_raw, *right = right_raw;
    if (left->generator != right->generator)
        return (left->generator > right->generator) - (left->generator < right->generator);
    int order = memcmp(left->input, right->input, FREE_BYTES);
    if (order) return order;
    if (left->inherited_class != right->inherited_class)
        return (left->inherited_class > right->inherited_class)
            - (left->inherited_class < right->inherited_class);
    if (left->lane != right->lane)
        return (left->lane > right->lane) - (left->lane < right->lane);
    return (left->time > right->time) - (left->time < right->time);
}
static int same_transition_key(const Transition *left, const Transition *right) {
    return left->generator == right->generator
        && memcmp(left->input, right->input, FREE_BYTES) == 0;
}
static int compare_probe_key(const Transition *row, const Probe *probe) {
    if (row->generator != probe->generator)
        return (row->generator > probe->generator) - (row->generator < probe->generator);
    return memcmp(row->input, probe->input, FREE_BYTES);
}

int main(int argc, char **argv) {
    if (argc != 8) { fprintf(stderr, "argc\n"); return 2; }
    size_t sched_n, column_n, free_n, class_n, probe_n;
    MaskedGate *schedule = load_exact(argv[1], sizeof(MaskedGate), &sched_n);
    uint32_t *initial = load_exact(argv[2], sizeof(uint32_t), &column_n);
    uint16_t *free_wires = load_exact(argv[3], sizeof(uint16_t), &free_n);
    uint8_t *classes = load_exact(argv[4], sizeof(uint8_t), &class_n);
    Probe *probes = load_exact(argv[5], sizeof(Probe), &probe_n);
    if (column_n != STATE_BITS || free_n != FREE_WIRES || class_n != LANES) return 3;
    StateRecord *states = malloc((size_t)FULL_STATES * sizeof(StateRecord));
    Transition *transitions = malloc((size_t)FULL_TRANSITIONS * sizeof(Transition));
    if (!states || !transitions) die("record malloc");
    uint32_t columns[STATE_BITS]; memcpy(columns, initial, sizeof(columns));
    size_t state_n = 0, transition_n = 0;
    for (int time = 0; time <= MAX_STEPS; ++time) {
        uint32_t state_active = active_for_state(time);
        for (int lane = 0; lane < LANES; ++lane) if ((state_active >> lane) & 1U) {
            StateRecord *row = &states[state_n++];
            pack_free(row->free_bits, columns, free_wires, lane);
            row->inherited_class = classes[lane];
        }
        if (time == MAX_STEPS) break;
        uint32_t active = active_for_transition(time);
        size_t step_start = transition_n;
        for (int lane = 0; lane < LANES; ++lane) if ((active >> lane) & 1U) {
            Transition *row = &transitions[transition_n++];
            pack_free(row->input, columns, free_wires, lane);
            row->generator = (uint8_t)(lane % GENERATORS);
            row->inherited_class = classes[lane];
            row->lane = (uint8_t)lane; row->time = (uint32_t)time;
        }
        for (size_t i = 0; i < sched_n; ++i) {
            MaskedGate gate = schedule[i]; uint32_t mask = gate.mask & active;
            if (gate.kind == 0) columns[gate.a] ^= mask;
            else if (gate.kind == 1) columns[gate.b] ^= columns[gate.a] & mask;
            else if (gate.kind == 2)
                columns[gate.c] ^= columns[gate.a] & columns[gate.b] & mask;
            else return 4;
        }
        size_t row_index = step_start;
        for (int lane = 0; lane < LANES; ++lane) if ((active >> lane) & 1U)
            pack_free(transitions[row_index++].output, columns, free_wires, lane);
        if (row_index != transition_n) return 5;
    }
    if (state_n != FULL_STATES || transition_n != FULL_TRANSITIONS) return 6;

    qsort(states, state_n, sizeof(StateRecord), state_cmp);
    uint64_t reduced_states = 0, unique_full_states = 0;
    uint64_t state_collision_groups = 0, state_variation_groups = 0;
    uint64_t state_variation_pairs = 0;
    for (size_t start = 0; start < state_n;) {
        size_t end = start + 1;
        while (end < state_n && !memcmp(
            states[start].free_bits, states[end].free_bits, FREE_BYTES
        )) ++end;
        ++reduced_states; if (end - start > 1) ++state_collision_groups;
        uint64_t class_counts[LANES] = {0};
        for (size_t i = start; i < end; ++i) ++class_counts[states[i].inherited_class];
        int distinct = 0;
        for (int c = 0; c < LANES; ++c) if (class_counts[c]) {
            ++distinct; ++unique_full_states;
            for (int d = c + 1; d < LANES; ++d)
                state_variation_pairs += class_counts[c] * class_counts[d];
        }
        if (distinct > 1) ++state_variation_groups;
        start = end;
    }

    qsort(transitions, transition_n, sizeof(Transition), transition_cmp);
    uint64_t induced_edges = 0, transition_collision_groups = 0;
    uint64_t inherited_variation_groups = 0, inherited_pinned_groups = 0;
    uint64_t inherited_variation_pairs = 0, coupling_groups = 0;
    uint64_t coupling_pair_witnesses = 0;
    Transition variation_witness[2]; int have_variation_witness = 0;
    FILE *wf = fopen(argv[7], "wb"); if (!wf) die(argv[7]);
    for (size_t start = 0; start < transition_n;) {
        size_t end = start + 1;
        while (end < transition_n && same_transition_key(
            &transitions[start], &transitions[end]
        )) ++end;
        ++induced_edges; if (end - start > 1) ++transition_collision_groups;
        uint64_t class_counts[LANES] = {0}; int distinct = 0, coupled = 0;
        for (size_t i = start; i < end; ++i) {
            ++class_counts[transitions[i].inherited_class];
            if (memcmp(transitions[start].output, transitions[i].output, FREE_BYTES)) coupled = 1;
        }
        for (int c = 0; c < LANES; ++c) if (class_counts[c]) {
            ++distinct;
            for (int d = c + 1; d < LANES; ++d)
                inherited_variation_pairs += class_counts[c] * class_counts[d];
        }
        if (distinct > 1) {
            ++inherited_variation_groups;
            if (!have_variation_witness) {
                size_t other = start + 1;
                while (other < end && transitions[other].inherited_class
                       == transitions[start].inherited_class) ++other;
                if (other < end) {
                    variation_witness[0] = transitions[start];
                    variation_witness[1] = transitions[other];
                    have_variation_witness = 1;
                }
            }
        } else ++inherited_pinned_groups;
        if (coupled) {
            ++coupling_groups;
            for (size_t left = start; left < end; ++left)
                for (size_t right = left + 1; right < end; ++right)
                    if (memcmp(
                        transitions[left].output, transitions[right].output, FREE_BYTES
                    )) {
                        if (fwrite(&transitions[left], sizeof(Transition), 1, wf) != 1
                            || fwrite(&transitions[right], sizeof(Transition), 1, wf) != 1)
                            die("coupling witness");
                        ++coupling_pair_witnesses;
                    }
        }
        start = end;
    }

    uint64_t probe_matches = 0, probe_output_mismatches = 0;
    for (size_t p = 0; p < probe_n; ++p) {
        size_t lo = 0, hi = transition_n;
        while (lo < hi) {
            size_t mid = lo + (hi - lo) / 2;
            if (compare_probe_key(&transitions[mid], &probes[p]) < 0) lo = mid + 1;
            else hi = mid;
        }
        if (lo < transition_n && compare_probe_key(&transitions[lo], &probes[p]) == 0) {
            if (!memcmp(transitions[lo].output, probes[p].output, FREE_BYTES)) ++probe_matches;
            else ++probe_output_mismatches;
        }
    }

    int witness_kind = coupling_groups ? 2 : have_variation_witness ? 1 : 0;
    if (!coupling_groups && have_variation_witness
        && fwrite(variation_witness, sizeof(Transition), 2, wf) != 2)
        die("variation witness");
    fclose(wf);
    FILE *summary = fopen(argv[6], "w"); if (!summary) die(argv[6]);
    fprintf(summary,
        "schedule_rows=%zu\nfull_reachable_states=%zu\nfull_landed_transitions=%zu\n"
        "unique_full_states=%" PRIu64 "\nreduced_reachable_states=%" PRIu64 "\n"
        "state_collision_groups=%" PRIu64 "\nstate_inherited_variation_groups=%" PRIu64 "\n"
        "state_inherited_variation_pairs=%" PRIu64 "\ninduced_transition_edges=%" PRIu64 "\n"
        "transition_collision_groups=%" PRIu64 "\ninherited_variation_groups=%" PRIu64 "\n"
        "inherited_pinned_groups=%" PRIu64 "\ninherited_variation_pairs=%" PRIu64 "\n"
        "coupling_groups=%" PRIu64 "\ncoupling_pair_witnesses=%" PRIu64 "\n"
        "witness_kind=%d\nprobe_count=%zu\n"
        "probe_matches=%" PRIu64 "\nprobe_output_mismatches=%" PRIu64 "\n",
        sched_n, state_n, transition_n, unique_full_states, reduced_states,
        state_collision_groups, state_variation_groups, state_variation_pairs,
        induced_edges, transition_collision_groups, inherited_variation_groups,
        inherited_pinned_groups, inherited_variation_pairs, coupling_groups,
        coupling_pair_witnesses, witness_kind, probe_n, probe_matches,
        probe_output_mismatches);
    fclose(summary);
    free(schedule); free(initial); free(free_wires); free(classes); free(probes);
    free(states); free(transitions); return 0;
}
'''


def initial_inherited_classes(
    states: dict[tuple[int, tuple[int, int]], int],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    inherited_wires: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...], dict[str, object]]:
    mask = sum(1 << wire for wire in inherited_wires)
    values = tuple(states[key] & mask for key in lanes)
    representatives: dict[int, int] = {}
    classes = []
    for value in values:
        if value not in representatives:
            representatives[value] = len(representatives)
        classes.append(representatives[value])
    public = {
        "lane_count": len(lanes),
        "distinct_inherited_boundary_value_vectors": len(representatives),
        "class_multiplicities": tuple(sorted(Counter(classes).items())),
        "class_assignment": tuple(classes),
        "inherited_values_pinned_along_each_lane": True,
        "inherited_projection_sha256_by_class": tuple(
            sha256(value.to_bytes(STATE_BYTES, "little")).hexdigest()
            for value, _class_id in sorted(
                representatives.items(), key=lambda item: item[1],
            )
        ),
    }
    class_values = tuple(
        value for value, _class_id in sorted(
            representatives.items(), key=lambda item: item[1],
        )
    )
    return tuple(classes), class_values, public


def braid_probes(
    events: tuple[dict[str, object], ...], free_wires: tuple[int, ...],
) -> tuple[tuple[bytes, bytes, int], ...]:
    probes = []
    for event in events:
        for lane, before, after in zip(
            event["coincident_lanes"], event["predecessor_states"],
            event["successor_states"],
        ):
            probes.append((
                project_state(before, free_wires),
                project_state(after, free_wires),
                lane,
            ))
    return tuple(probes)


def write_kernel_inputs(
    directory: Path,
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    states: dict[tuple[int, tuple[int, int]], int],
    free_wires: tuple[int, ...], inherited_classes: tuple[int, ...],
    probes: tuple[tuple[bytes, bytes, int], ...],
) -> dict[str, object]:
    schedule = build_masked_schedule(macros, lanes)
    schedule_payload = b"".join(
        struct.pack("<BHHHI", *row) for row in schedule
    )
    columns = tuple(sum(
        ((states[key] >> wire) & 1) << lane
        for lane, key in enumerate(lanes)
    ) for wire in range(STATE_BITS))
    columns_payload = struct.pack(f"<{STATE_BITS}I", *columns)
    free_payload = struct.pack(f"<{len(free_wires)}H", *free_wires)
    classes_payload = bytes(inherited_classes)
    probes_payload = b"".join(
        before + after + bytes((generator,))
        for before, after, generator in probes
    )
    payloads = {
        "schedule.bin": schedule_payload,
        "columns.bin": columns_payload,
        "free_wires.bin": free_payload,
        "classes.bin": classes_payload,
        "probes.bin": probes_payload,
    }
    for name, payload in payloads.items():
        (directory / name).write_bytes(payload)
    return {
        "schedule_rows": len(schedule),
        "free_wire_count": len(free_wires),
        "probe_count": len(probes),
        "input_sha256": tuple(
            (name, sha256(payload).hexdigest())
            for name, payload in payloads.items()
        ),
    }


def compile_kernel(directory: Path) -> dict[str, object]:
    source = directory / "kernel.c"
    binary = directory / "kernel"
    source.write_text(KERNEL_C, encoding="utf-8")
    completed = subprocess.run(
        ("cc", "-O3", "-std=c11", str(source), "-o", str(binary)),
        cwd=ROOT, check=True, capture_output=True, text=True, timeout=60,
    )
    version = subprocess.run(
        ("cc", "--version"), check=True, capture_output=True,
        text=True, timeout=20,
    ).stdout.splitlines()[0]
    return {
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "binary_sha256": sha256(binary.read_bytes()).hexdigest(),
        "compiler": version,
        "compiler_stderr": completed.stderr,
    }


def execute_kernel(directory: Path, label: str) -> dict[str, object]:
    summary_path = directory / f"summary_{label}.txt"
    witness_path = directory / f"witness_{label}.bin"
    completed = subprocess.run(
        (
            str(directory / "kernel"), str(directory / "schedule.bin"),
            str(directory / "columns.bin"), str(directory / "free_wires.bin"),
            str(directory / "classes.bin"), str(directory / "probes.bin"),
            str(summary_path), str(witness_path),
        ),
        cwd=ROOT, check=True, capture_output=True, text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    summary = {}
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        key, value = line.split("=", 1)
        summary[key] = int(value)
    witness = witness_path.read_bytes()
    return {
        "summary": summary,
        "witness": witness,
        "witness_sha256": sha256(witness).hexdigest(),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def decode_witness(
    payload: bytes, free_wires: tuple[int, ...], class_values: tuple[int, ...],
) -> dict[str, object] | None:
    free_bytes = (len(free_wires) + 7) // 8
    record = 2 * free_bytes + 3 + 4
    if not payload:
        return None
    if len(payload) % (2 * record):
        raise AssertionError(("witness size drift", len(payload), 2 * record))
    decoded_pairs = []
    channel_counts: Counter[tuple[object, ...]] = Counter()
    for pair_offset in range(0, len(payload), 2 * record):
        raw_rows = []
        rows = []
        for row_offset in (pair_offset, pair_offset + record):
            before = payload[row_offset:row_offset + free_bytes]
            after_start = row_offset + free_bytes
            after = payload[after_start:after_start + free_bytes]
            metadata_start = after_start + free_bytes
            generator, inherited_class, lane, time = struct.unpack(
                "<BBBI", payload[metadata_start:metadata_start + 7],
            )
            raw_rows.append((before, after))
            rows.append({
                "generator": BACKBONE[generator],
                "generator_index": generator,
                "inherited_class": inherited_class,
                "lane": lane,
                "event": EVENTS[lane // len(BACKBONE)],
                "time": time,
                "free_input_sha256": sha256(before).hexdigest(),
                "free_successor_sha256": sha256(after).hexdigest(),
            })
        successor_delta = int.from_bytes(bytes(
            left ^ right for left, right in zip(
                raw_rows[0][1], raw_rows[1][1],
            )
        ), "little")
        free_delta_indices = support_indices(successor_delta)
        left_class = rows[0]["inherited_class"]
        right_class = rows[1]["inherited_class"]
        inherited_delta_wires = support_indices(
            class_values[left_class] ^ class_values[right_class]
        )
        inherited_left_ones = tuple(
            wire for wire in inherited_delta_wires
            if (class_values[left_class] >> wire) & 1
        )
        inherited_right_ones = tuple(
            wire for wire in inherited_delta_wires
            if (class_values[right_class] >> wire) & 1
        )
        free_delta_wires = tuple(
            free_wires[index] for index in free_delta_indices
        )
        same_successor = not free_delta_wires
        pair = {
            "rows": tuple(rows),
            "same_free_input": raw_rows[0][0] == raw_rows[1][0],
            "different_inherited_class": left_class != right_class,
            "same_free_successor": same_successor,
        }
        decoded_pairs.append(pair)
        if not same_successor:
            channel_counts[(
                rows[0]["generator_index"], left_class, right_class,
                ranges(inherited_delta_wires), ranges(inherited_left_ones),
                ranges(inherited_right_ones), free_delta_wires,
            )] += 1
    channels = tuple({
        "generator": BACKBONE[key[0]],
        "inherited_class_pair": (key[1], key[2]),
        "inherited_difference_wire_ranges": key[3],
        "class_a_one_wire_ranges_on_difference": key[4],
        "class_b_one_wire_ranges_on_difference": key[5],
        "free_successor_difference_wires": key[6],
        "reachable_coupling_group_count": count,
    } for key, count in sorted(channel_counts.items()))
    return {
        "exact_witness_pair_count": len(decoded_pairs),
        "witness_payload_sha256": sha256(payload).hexdigest(),
        "first_pair": decoded_pairs[0],
        "all_pairs_valid": all(
            pair["same_free_input"] and pair["different_inherited_class"]
            for pair in decoded_pairs
        ),
        "coupling_channels": channels,
    }


def collision_signature(
    states_by_depth: tuple[tuple[object, ...], ...],
) -> tuple[tuple[int, tuple[tuple[int, ...], ...], tuple[int, ...]], ...]:
    rows = []
    for depth in range(NORMALIZED_DEPTH, -1, -1):
        inputs = states_by_depth[depth + 1]
        outputs = states_by_depth[depth]
        predecessor = partition_of(inputs)
        for output_block in partition_of(outputs):
            incoming = tuple(
                tuple(lane for lane in block if lane in output_block)
                for block in predecessor
                if any(lane in output_block for lane in block)
            )
            if len(incoming) >= 2:
                rows.append((depth, incoming, tuple(output_block)))
    return tuple(rows)


def analysis_once(trees: dict[str, ast.Module]) -> dict[str, object]:
    fixtures = decode_fixtures(trees[AUDIT_INPUT_PATHS[0]])
    macros = fixtures["macros"]
    assert isinstance(macros, tuple)
    gate_words = build_gate_words(macros)
    inheritance, private = inheritance_reconstruction(gate_words)
    nine = evolve_nine(fixtures)
    events = transition_rows(nine, compile_words(gate_words))
    replay_surface = {
        "fixture": fixtures["public"],
        "inheritance": inheritance,
        "nine": nine["public"],
        "states_by_depth_sha256": digest(nine["states_by_depth"]),
        "events_sha256": digest(tuple({
            key: value for key, value in event.items()
            if key not in {"predecessor_states", "successor_states"}
        } for event in events)),
        "event_state_sha256": digest(tuple(
            (event["predecessor_states"], event["successor_states"])
            for event in events
        )),
    }
    return {
        "fixtures": fixtures,
        "gate_words": gate_words,
        "inheritance": inheritance,
        "private": private,
        "nine": nine,
        "events": events,
        "replay_surface": replay_surface,
    }


def closure_certificate(
    summary: dict[str, int], witness: dict[str, object] | None,
    inherited_classes: dict[str, object],
) -> dict[str, object]:
    coupled = summary["coupling_groups"] > 0
    variation_groups = summary["inherited_variation_groups"]
    pinned_groups = summary["inherited_pinned_groups"]
    if variation_groups:
        variation_statement = (
            f"{variation_groups} equal-(generator,free-input) groups contain "
            "distinct exact inherited vectors; every such group was compared."
        )
    else:
        variation_statement = (
            "The reachable census pins inherited values to one exact vector in "
            "every equal-(generator,free-input) group; constancy implies trivial closure."
        )
    first_pair = witness["first_pair"] if witness is not None else None
    channels = witness["coupling_channels"] if witness is not None else ()
    public_witness = (
        {key: value for key, value in witness.items() if key != "coupling_channels"}
        if witness is not None else None
    )
    witness_valid = (
        (coupled and witness is not None and first_pair is not None
         and witness["all_pairs_valid"]
         and witness["exact_witness_pair_count"]
         == summary["coupling_pair_witnesses"]
         and sum(row["reachable_coupling_group_count"] for row in channels)
         == summary["coupling_pair_witnesses"]
         and first_pair["same_free_input"]
         and first_pair["different_inherited_class"]
         and not first_pair["same_free_successor"])
        or (
            not coupled and variation_groups > 0
            and witness is not None and first_pair is not None
            and witness["exact_witness_pair_count"] == 1
            and first_pair["same_free_input"]
            and first_pair["different_inherited_class"]
            and first_pair["same_free_successor"]
        )
        or (not coupled and variation_groups == 0 and witness is None)
    )
    result = {
        "tested_relation": (
            "For each of the nine labeled complete-generator maps F_pair, group "
            "all reachable nonterminal boundary states by their exact 495-bit free "
            "projection and compare exact projected successors across inherited classes."
        ),
        "full_boundary_state_census": summary["full_reachable_states"],
        "full_boundary_step_census": summary["full_landed_transitions"],
        "generator_alphabet": BACKBONE,
        "induced_generator_free_input_groups": summary["induced_transition_edges"],
        "groups_with_multiple_labeled_occurrences":
            summary["transition_collision_groups"],
        "groups_with_distinct_inherited_vectors": variation_groups,
        "exact_distinct_inherited_pair_comparisons":
            summary["inherited_variation_pairs"],
        "groups_with_inherited_values_pinned": pinned_groups,
        "pinned_constancy_statement": variation_statement,
        "initial_inherited_classes": inherited_classes,
        "free_successor_disagreement_groups": summary["coupling_groups"],
        "exact_coupling_pair_witnesses": summary["coupling_pair_witnesses"],
        "witness": public_witness,
        "coupling_channel_count": len(channels) if coupled else 0,
        "coupling_channels": channels if coupled else (),
        "verdict": "COUPLED" if coupled else "FREE_SECTOR_CLOSED",
        "finding": "COUPLED" if coupled else "FREE_SECTOR_CLOSED",
        "pass": False,
    }
    result["pass"] = (
        summary["full_reachable_states"] == FULL_REACHABLE_STATES
        and summary["full_landed_transitions"] == FULL_LANDED_TRANSITIONS
        and variation_groups + pinned_groups
        == summary["induced_transition_edges"]
        and witness_valid
    )
    return result


def reduced_machine_certificate(
    summary: dict[str, int], closure: dict[str, object],
    nine: dict[str, object], events: tuple[dict[str, object], ...],
    free_wires: tuple[int, ...], probe_count: int,
) -> dict[str, object]:
    full_states = nine["states_by_depth"]
    assert isinstance(full_states, tuple)
    projected = tuple(tuple(
        project_state(state, free_wires) for state in depth_states
    ) for depth_states in full_states)
    full_signature = collision_signature(full_states)
    projected_signature = collision_signature(projected)
    exact_braid = (
        len(full_signature) == len(projected_signature) == EXPECTED_EVENT_COUNT
        and projected_signature == full_signature
        and digest(projected_signature) == EXPECTED_EVENT_SIGNATURE_SHA256
        and summary["probe_count"] == probe_count
        and summary["probe_matches"] == probe_count
        and summary["probe_output_mismatches"] == 0
    )
    closed = closure["verdict"] == "FREE_SECTOR_CLOSED"
    if closed:
        finding = "REDUCED_MACHINE_EXACT_AND_BRAID_REPRODUCED"
        definition = {
            "states": (
                "Distinct exact 495-bit free projections occurring among all "
                "891,513 labeled reachable generator-boundary states."
            ),
            "step": (
                "For each observed (free state, F_pair), the unique free projection "
                "of the full successor; B proves independence from inherited class."
            ),
            "reachable_state_count": summary["reduced_reachable_states"],
            "induced_labeled_edge_count": summary["induced_transition_edges"],
        }
    else:
        finding = "REDUCED_MACHINE_NOT_DEFINED_COUPLED"
        definition = None
    result = {
        "full_labeled_reachable_size": FULL_REACHABLE_STATES,
        "unique_full_bit_states_in_census": summary["unique_full_states"],
        "reduced_reachable_size": (
            summary["reduced_reachable_states"] if closed else None
        ),
        "strictly_smaller_than_full_891513": (
            closed and summary["reduced_reachable_states"] < FULL_REACHABLE_STATES
        ),
        "projection_collision_groups": summary["state_collision_groups"],
        "projection_groups_with_distinct_inherited_vectors":
            summary["state_inherited_variation_groups"],
        "exact_state_inherited_pair_collisions":
            summary["state_inherited_variation_pairs"],
        "reduced_automaton": definition,
        "braid_event_count_full": len(full_signature),
        "braid_event_count_free_projection": len(projected_signature),
        "braid_event_signature_preserved": projected_signature == full_signature,
        "braid_structural_type_count": len({
            event["type_sha256"] for event in events
        }),
        "braid_transition_probes": summary["probe_count"],
        "braid_transition_probes_reproduced": summary["probe_matches"],
        "braid_probe_output_mismatches": summary["probe_output_mismatches"],
        "braid_20_events_reproduced": exact_braid,
        "coupling_channels_if_not_reduced": closure["coupling_channels"],
        "finding": finding,
        "pass": False,
    }
    result["pass"] = (
        (
            closed
            and result["strictly_smaller_than_full_891513"]
            and exact_braid
        )
        or (
            not closed
            and bool(result["coupling_channels_if_not_reduced"])
        )
    )
    return result


def run() -> int:
    started = monotonic()
    sources, trees = source_controls()
    first = analysis_once(trees)
    second = analysis_once(trees)
    scientific_replay_exact = first["replay_surface"] == second["replay_surface"]
    fixtures = first["fixtures"]
    states = fixtures["states"]
    macros = fixtures["macros"]
    free_wires = first["private"]["free_wires"]
    inherited_wires = first["private"]["inherited_wires"]
    assert isinstance(states, dict) and isinstance(macros, tuple)
    assert isinstance(free_wires, tuple) and isinstance(inherited_wires, tuple)
    events = first["events"]
    certificate_a = free_support_certificate(
        first["inheritance"], first["private"], events,
    )
    lanes = tuple((event, pair) for event in EVENTS for pair in BACKBONE)
    classes, class_values, class_public = initial_inherited_classes(
        states, lanes, inherited_wires,
    )
    inherited_mask = sum(1 << wire for wire in inherited_wires)
    compiled = compile_words(first["gate_words"])
    explicit_lane_invariance = all(
        not ((apply_compiled(states[key], compiled[pair]) ^ states[key])
             & inherited_mask)
        for key in lanes for pair in BACKBONE
    )
    class_public["explicit_27_by_9_boundary_invariance_check"] = (
        explicit_lane_invariance
    )
    probes = braid_probes(events, free_wires)

    with tempfile.TemporaryDirectory(prefix="cycle855-") as temp_name:
        temp = Path(temp_name)
        kernel_inputs = write_kernel_inputs(
            temp, macros, lanes, states, free_wires, classes, probes,
        )
        compiler = compile_kernel(temp)
        kernel_first = execute_kernel(temp, "first")
        kernel_second = execute_kernel(temp, "second")

    kernel_replay_exact = kernel_first == kernel_second
    summary = kernel_first["summary"]
    witness = decode_witness(
        kernel_first["witness"], free_wires, class_values,
    )
    certificate_b = closure_certificate(summary, witness, class_public)
    certificate_c = reduced_machine_certificate(
        summary, certificate_b, first["nine"], events, free_wires, len(probes),
    )

    elapsed = monotonic() - started
    blocked_at_end = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    controls_base = (
        sources["pass"]
        and fixtures["public"]["pass"]
        and second["fixtures"]["public"]["pass"]
        and first["nine"]["public"]["pass"]
        and second["nine"]["public"]["pass"]
        and scientific_replay_exact
        and explicit_lane_invariance
        and kernel_replay_exact
        and summary["schedule_rows"] == kernel_inputs["schedule_rows"]
        and not blocked_at_end
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificate_d = {
        "source_controls": sources,
        "fixture_reconstruction_first": fixtures["public"],
        "fixture_reconstruction_second": second["fixtures"]["public"],
        "primary_access_policy": (
            "Every literal AUDIT_INPUT_PATHS entry is SHA/blob pinned, BLOCKLISTED, "
            "and consumed as text/AST only; no cited primary is imported or executed."
        ),
        "cycle854_family_recomputed_not_parsed": True,
        "kernel_inputs": kernel_inputs,
        "compiled_exact_integer_kernel": compiler,
        "determinism_replay": {
            "scientific_reconstruction_exact": scientific_replay_exact,
            "scientific_first_sha256": digest(first["replay_surface"]),
            "scientific_second_sha256": digest(second["replay_surface"]),
            "kernel_exact": kernel_replay_exact,
            "kernel_first_summary": kernel_first["summary"],
            "kernel_second_summary": kernel_second["summary"],
            "kernel_witness_sha256": kernel_first["witness_sha256"],
            "kernel_stdout": kernel_first["stdout"],
            "kernel_stderr": kernel_first["stderr"],
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
        "A_FREE_COMPLEMENT": certificate_a,
        "B_CLOSURE_TEST": certificate_b,
        "C_REDUCED_MACHINE": certificate_c,
        "D_CONTROLS": certificate_d,
    }
    checks = {
        "A_FREE_COMPLEMENT": bool(certificate_a["pass"]),
        "B_CLOSURE_TEST": bool(certificate_b["pass"]),
        "C_REDUCED_MACHINE": bool(certificate_c["pass"]),
        "D_CONTROLS": False,
    }
    report = {
        "cycle": 855,
        "title": "the free-sector reduction",
        "verdict": certificate_b["verdict"],
        "free_wire_count": certificate_a["free_wire_count"],
        "full_reachable_size": FULL_REACHABLE_STATES,
        "reduced_reachable_size": certificate_c["reduced_reachable_size"],
        "braid_20_events_reproduced": certificate_c["braid_20_events_reproduced"],
        "runtime_seconds": round(elapsed, 6),
        "checks": {},
        "pass": False,
        "terminal": "CYCLE855_FREE_SECTOR_REDUCTION_HONEST_FAIL",
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
            "CYCLE855_FREE_SECTOR_REDUCTION_PASS"
            if report["pass"] else "CYCLE855_FREE_SECTOR_REDUCTION_HONEST_FAIL"
        )
        output = render()
        stdout_bytes = len(output.encode("utf-8"))
        certificate_d["stdout_bytes"] = stdout_bytes
        certificate_d["stdout_below_limit"] = stdout_bytes < STDOUT_LIMIT_BYTES
        controls_base = controls_base and stdout_bytes < STDOUT_LIMIT_BYTES
    output = render()
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 855,
            "pass": False,
            "terminal": "CYCLE855_STDOUT_LIMIT_EXCEEDED",
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
                "cycle": 855,
                "pass": False,
                "terminal": "CYCLE855_FREE_SECTOR_REDUCTION_HONEST_FAIL",
                "exception_type": type(error).__name__,
                "exception": str(error),
            }))
            return 1
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: frontier_cycle855_free_sector_reduction_2026_07_28.py"
        )
    try:
        completed = subprocess.run(
            (sys.executable, str(Path(__file__).resolve()), "--_worker"),
            cwd=ROOT, capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        print(compact({
            "cycle": 855,
            "pass": False,
            "terminal": "CYCLE855_TIMEOUT",
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        }))
        return 1
    stdout_bytes = len(completed.stdout.encode("utf-8"))
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 855,
            "pass": False,
            "terminal": "CYCLE855_STDOUT_LIMIT_EXCEEDED",
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
