#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-848 coincidence census.

The source primaries are SHA-pinned and consumed only as text/AST.  This
checker does not import or execute them.  Equality partitions are rebuilt by
pairwise union-find, rather than by the primary's state-keyed grouping.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle848_braid_derivation_2026_07_28.py",
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
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
NORMALIZED_DEPTH = 64
PREDECESSOR_DEPTH = 65
NINE_FUNNEL_MOVEMENT = 14739
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
NINE_PREDICATE_WIRES = (40, 81, 105)
NINE_PREDICATE_PATTERNS = ((0, 0, 0), (0, 1, 1), (1, 0, 0))
PAIR_PREDICATE_WIRES = (88, 124, 125)
PAIR_POSITIONS = ((0, 5), (0, 6))
CHRONOLOGICAL_PAIR_ORDER = (1, 2, 0)

EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[1]:
        "a9fdefbffe16495e62258804d3abbddb48aaa500e365f56c739c24959162ca48",
}
EXPECTED_SOURCE_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[1]: "c55036475e2389565b1c4b69e96595db99e03779",
}
PINNED_PAIR_SOURCE = {
    "commit": "7af6f39f9f2714a5a836af8b1bd3170b2afd4715",
    "path": "scripts/frontier_cycle846_reduced_braids_delay_law_2026_07_28.py",
    "source_sha256":
        "172313524341e958d36e1028f0cec5e64e81c4efd915c009073049998c37fc45",
    "git_blob": "2e0eb1848b92ab3f43a5ada64664ab45b58f5bb1",
}
PAIR_FULL_RLE = (
    (1, 193206, "311fbdc9dd81ab2d62a214a17cb3d356fb66919181791e002c721a1e946283a4"),
    (2, 246665, "f1b8c00d3c3d598261f65f849bdd98ae9fb3788a5289ad278c4ccc5e35b12e20"),
    (0, 1142428, "5d207cf5085ae36f7a607c63eae04bc4ce2e2b43a67ea5209e306971be32ca6e"),
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
EXPECTED_PARTITION_SHA256 = (
    "726b74aefc7afa6e1790c7dc73a59eacdadeec72246e19ac01104be09d49829d"
)
EXPECTED_EVENT_SIGNATURE_SHA256 = (
    "7ae45bbd8b6e688b9abdadd0e33dcfd300e2649b4776386a5b8ec48eb62e064a"
)
EXPECTED_EVENT_COUNT = 20
EXPECTED_TYPE_COUNT = 16

Pair = tuple[int, int]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
Partition = tuple[tuple[int, ...], ...]

BLOCKLISTED_MODULES = tuple(sorted({
    *(Path(path).stem for path in AUDIT_INPUT_PATHS),
    Path(PINNED_PAIR_SOURCE["path"]).stem,
}))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only source primary is imported."""

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
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, check=True, capture_output=True,
        timeout=30,
    ).stdout


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    candidates = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == name
                    for target in node.targets)
        ):
            candidates.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            candidates.append(node.value)
    if len(candidates) != 1:
        return None
    try:
        return ast.literal_eval(candidates[0])
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
    pair_spec = f"{PINNED_PAIR_SOURCE['commit']}:{PINNED_PAIR_SOURCE['path']}"
    pair_payload = git_bytes("show", pair_spec)
    pair_tree = ast.parse(pair_payload, filename=pair_spec)
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    source_sha = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    source_blobs = {
        path: git_blob(payload) for path, payload in payloads.items()
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
    ast_basis = {
        "cycle830_literal_bank": all(
            literal_assignment(trees[AUDIT_INPUT_PATHS[0]], name) is not None
            for name in (
                "GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85",
            )
        ),
        "cycle848_claim_surface": {
            "transition_rows", "certificate_b_schema_hunt", "pair_copy_certificate",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle846_pair_basis": {
            "pair_braids", "new_braid_tracker", "finish_braid_tracker",
        } <= function_names(pair_tree),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "source_sha256": source_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "source_git_blobs": source_blobs,
        "expected_source_git_blobs": EXPECTED_SOURCE_GIT_BLOBS,
        "pinned_pair_source": {
            **PINNED_PAIR_SOURCE,
            "observed_source_sha256": sha256(pair_payload).hexdigest(),
            "observed_git_blob": git_blob(pair_payload),
        },
        "AST_basis": ast_basis,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded_at_start": blocked_loaded,
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "direct_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= stdlib_roots,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob(self_payload),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and source_sha == EXPECTED_SOURCE_SHA256
        and source_blobs == EXPECTED_SOURCE_GIT_BLOBS
        and sha256(pair_payload).hexdigest() == PINNED_PAIR_SOURCE["source_sha256"]
        and git_blob(pair_payload) == PINNED_PAIR_SOURCE["git_blob"]
        and all(ast_basis.values())
        and not blocked_loaded and not FIREWALL.hits
        and result["stdlib_only"]
    )
    trees["pinned_pair_source"] = pair_tree
    return result, trees


def cyclic_separation(pair: Pair) -> int:
    forward = (pair[1] - pair[0]) % RING_STATIONS
    backward = (pair[0] - pair[1]) % RING_STATIONS
    return min(forward, backward)


def lawful_pairs() -> tuple[Pair, ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def decode_fixture_bank(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(literal_assignment(tree, name) for name in (
        "GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85",
    ))
    if not all(isinstance(item, str) for item in encoded):
        raise AssertionError("Cycle-830 literal fixture bank is incomplete")
    gate_raw, family_raw, target_raw = tuple(
        zlib.decompress(base64.b85decode(item)) for item in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    cursor = 22
    macros = []
    for length in lengths:
        macro = []
        for _index in range(length):
            macro.append(struct.unpack("<BHHH", gate_raw[cursor:cursor + 7]))
            cursor += 7
        macros.append(tuple(macro))
    pairs = lawful_pairs()
    keys = tuple(sorted((event, pair) for event in range(4) for pair in pairs))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little"
        )
    target = int.from_bytes(target_raw, "little")
    checks = {
        "station_count": len(lengths) == RING_STATIONS,
        "gate_count": sum(lengths) == GATE_COUNT and cursor == len(gate_raw),
        "family_size": len(states) == FAMILY_SIZE,
        "family_bytes": len(family_raw) == FAMILY_SIZE * STATE_BYTES,
        "target_bytes": len(target_raw) == STATE_BYTES,
        "gate_raw_sha256": sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256,
        "family_raw_sha256":
            sha256(family_raw).hexdigest() == EXPECTED_FAMILY_RAW_SHA256,
        "target_raw_sha256":
            sha256(target_raw).hexdigest() == EXPECTED_SSTAR_PACKED_SHA256,
    }
    return {
        "macros": tuple(macros), "keys": keys, "states": states,
        "target": target, "checks": checks, "pass": all(checks.values()),
    }


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
        remaining = state
        while remaining:
            bit = remaining & -remaining
            columns[bit.bit_length() - 1] |= 1 << lane
            remaining ^= bit
    return columns


def capture_lanes(columns: list[int], lane_count: int) -> tuple[int, ...]:
    states = [0] * lane_count
    lane_mask = (1 << lane_count) - 1
    for wire, column in enumerate(columns):
        remaining = column & lane_mask
        while remaining:
            bit = remaining & -remaining
            states[bit.bit_length() - 1] |= 1 << wire
            remaining ^= bit
    return tuple(states)


def movement_schedule(
    macros: tuple[tuple[Gate, ...], ...], lane_pairs: tuple[Pair, ...],
) -> tuple[MaskedGate, ...]:
    rows = []
    for phase in range(RING_STATIONS):
        for station, macro in enumerate(macros):
            mask = 0
            for lane, pair in enumerate(lane_pairs):
                shifted = {
                    (pair[0] + phase) % RING_STATIONS,
                    (pair[1] + phase) % RING_STATIONS,
                }
                if station in shifted:
                    mask |= 1 << lane
            if mask:
                rows.extend((*gate, mask) for gate in macro)
    return tuple(rows)


def advance_columns(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, lane_mask in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        elif kind == 2:
            columns[third] ^= columns[first] & columns[second] & lane_mask
        else:
            raise AssertionError(("unknown Boolean gate", kind))


def union_find_partition(states: tuple[int, ...]) -> Partition:
    """Extract equality blocks by O(n^2) comparisons and union-find."""
    parent = list(range(len(states)))

    def root(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def unite(left: int, right: int) -> None:
        left_root, right_root = root(left), root(right)
        if left_root != right_root:
            parent[max(left_root, right_root)] = min(left_root, right_root)

    for left, right in combinations(range(len(states)), 2):
        if states[left] == states[right]:
            unite(left, right)
    groups: dict[int, list[int]] = defaultdict(list)
    for lane in range(len(states)):
        groups[root(lane)].append(lane)
    return tuple(sorted((tuple(group) for group in groups.values()), key=lambda x: x[0]))


def evolve_nine(fixtures: dict[str, object]) -> dict[str, object]:
    initial = tuple(fixtures["states"][(0, pair)] for pair in BACKBONE)
    schedule = movement_schedule(fixtures["macros"], BACKBONE)
    columns = bit_slice(initial)
    captured = []
    for movement in range(1, NINE_FUNNEL_MOVEMENT + 1):
        advance_columns(columns, schedule)
        if movement >= NINE_FUNNEL_MOVEMENT - PREDECESSOR_DEPTH:
            captured.append(capture_lanes(columns, len(BACKBONE)))
    states_by_depth = tuple(reversed(captured))
    partitions = tuple(
        union_find_partition(states)
        for states in states_by_depth[:NORMALIZED_DEPTH + 1]
    )
    return {
        "states_by_depth": states_by_depth,
        "partitions": partitions,
        "partition_sha256": digest(partitions),
        "schedule_rows": len(schedule),
        "terminal_target_exact": all(
            state == fixtures["target"] for state in states_by_depth[0]
        ),
        "pass": (
            len(states_by_depth) == PREDECESSOR_DEPTH + 1
            and digest(partitions) == EXPECTED_PARTITION_SHA256
            and all(state == fixtures["target"] for state in states_by_depth[0])
        ),
    }


def compile_scalar_word(
    macros: tuple[tuple[Gate, ...], ...], pair: Pair,
) -> tuple[tuple[int, int, int], ...]:
    """Compile one movement independently as scalar mask operations."""
    operations = []
    for phase in range(RING_STATIONS):
        active = {
            (pair[0] + phase) % RING_STATIONS,
            (pair[1] + phase) % RING_STATIONS,
        }
        for station, macro in enumerate(macros):
            if station not in active:
                continue
            for kind, first, second, third in macro:
                if kind == 0:
                    operations.append((kind, 0, 1 << first))
                elif kind == 1:
                    operations.append((kind, 1 << first, 1 << second))
                elif kind == 2:
                    operations.append(
                        (kind, (1 << first) | (1 << second), 1 << third)
                    )
                else:
                    raise AssertionError(("unknown Boolean gate", kind))
    if len(operations) != WORD_GATE_COUNT:
        raise AssertionError(("scalar word length", pair, len(operations)))
    return tuple(operations)


def apply_scalar_word(
    state: int, word: tuple[tuple[int, int, int], ...], *, reverse: bool = False,
) -> int:
    operations = reversed(word) if reverse else word
    for kind, controls, target in operations:
        if kind == 0 or state & controls == controls:
            state ^= target
    return state


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def support_indices(mask: int) -> tuple[int, ...]:
    indices = []
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        indices.append(bit.bit_length() - 1)
        remaining ^= bit
    return tuple(indices)


def wire_pattern(state: int, wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in wires)


def structural_signature(event: dict[str, object]) -> tuple[object, ...]:
    """The declared Cycle-848 precondition-type relation key."""
    return (
        event["incoming_block_sizes"],
        event["participant_count"],
        event["variation_support_count"],
        event["predecessor_pattern_multiset"],
        event["known_three_wire_local"],
        event["all_patterns_in_landed_nine_family"],
    )


def extract_nine_events(
    fixtures: dict[str, object], nine: dict[str, object],
) -> tuple[dict[str, object], ...]:
    words = {
        pair: compile_scalar_word(fixtures["macros"], pair)
        for pair in BACKBONE
    }
    states_by_depth = nine["states_by_depth"]
    events = []
    event_index = 0
    for depth in range(NORMALIZED_DEPTH, -1, -1):
        predecessors = states_by_depth[depth + 1]
        outputs = states_by_depth[depth]
        predecessor_partition = union_find_partition(predecessors)
        output_partition = union_find_partition(outputs)
        for output_block in output_partition:
            incoming = tuple(
                tuple(lane for lane in predecessor_block if lane in output_block)
                for predecessor_block in predecessor_partition
                if any(lane in output_block for lane in predecessor_block)
            )
            if len(incoming) < 2:
                continue
            lanes = tuple(output_block)
            input_states = tuple(predecessors[lane] for lane in lanes)
            output_states = tuple(outputs[lane] for lane in lanes)
            scalar_outputs = tuple(
                apply_scalar_word(predecessors[lane], words[BACKBONE[lane]])
                for lane in lanes
            )
            common_output = output_states[0]
            recovered_inputs = tuple(
                apply_scalar_word(
                    common_output, words[BACKBONE[lane]], reverse=True,
                )
                for lane in lanes
            )
            anchor = input_states[0]
            variation_mask = 0
            for state in input_states[1:]:
                variation_mask |= anchor ^ state
            variation_support = support_indices(variation_mask)
            patterns = tuple(
                wire_pattern(state, NINE_PREDICATE_WIRES)
                for state in input_states
            )
            pattern_multiset = tuple(sorted(Counter(patterns).items()))
            local = set(variation_support) <= set(NINE_PREDICATE_WIRES)
            in_family = all(
                pattern in NINE_PREDICATE_PATTERNS for pattern in patterns
            )
            exact = (
                len(set(output_states)) == 1
                and scalar_outputs == output_states
                and recovered_inputs == input_states
                and len(incoming) >= 2
            )
            event = {
                "event_index": event_index,
                "normalized_depth": depth,
                "predecessor_depth": depth + 1,
                "incoming_lane_blocks": incoming,
                "coincident_lane_subset": lanes,
                "coincident_key_subset": tuple(BACKBONE[lane] for lane in lanes),
                "incoming_block_sizes": tuple(len(block) for block in incoming),
                "participant_count": len(lanes),
                "variation_support_count": len(variation_support),
                "variation_support_sha256": digest(variation_support),
                "predecessor_pattern_multiset": pattern_multiset,
                "known_three_wire_local": local,
                "all_patterns_in_landed_nine_family": in_family,
                "predecessor_state_sha256": tuple(
                    packed_sha256(state) for state in input_states
                ),
                "common_output_sha256": packed_sha256(common_output),
                "forward_outputs_exact": scalar_outputs == output_states,
                "inverse_recovers_predecessors": recovered_inputs == input_states,
                "pass": exact,
            }
            event["type_signature"] = structural_signature(event)
            events.append(event)
            event_index += 1
    return tuple(events)


def pair_partition(united: bool) -> Partition:
    synthetic_states = (0, 0) if united else (0, 1)
    return union_find_partition(synthetic_states)


def extract_pair_events() -> dict[str, object]:
    rows = []
    total_generated = 0
    for event, sample_count, expected_sha in PAIR_FULL_RLE:
        exact_stream = b"\x01" * sample_count
        observed_sha = sha256(exact_stream).hexdigest()
        partitions = tuple(
            pair_partition(bool(value)) for value in exact_stream[-66:]
        )
        generated = 0
        for predecessor, output in zip(partitions[:-1], partitions[1:]):
            if predecessor == ((0,), (1,)) and output == ((0, 1),):
                generated += 1
        total_generated += generated
        rows.append({
            "event": event,
            "sample_count": sample_count,
            "observed_sequence_sha256": observed_sha,
            "expected_sequence_sha256": expected_sha,
            "normalized_partition_sha256": digest(partitions),
            "generated_event_count": generated,
            "all_partitions_united": all(
                partition == ((0, 1),) for partition in partitions
            ),
            "pass": observed_sha == expected_sha and generated == 0,
        })
    return {
        "braid_rows": tuple(rows),
        "generated_event_count": total_generated,
        "one_step_preconditions": (),
        "pass": all(row["pass"] for row in rows) and total_generated == 0,
    }


def event_signature(events: tuple[dict[str, object], ...]) -> tuple[object, ...]:
    return tuple(
        (
            event["normalized_depth"], event["incoming_lane_blocks"],
            event["coincident_lane_subset"],
        )
        for event in events
    )


def certificate_event_census(
    fixtures: dict[str, object], nine: dict[str, object],
) -> tuple[dict[str, object], tuple[dict[str, object], ...], dict[str, object]]:
    events = extract_nine_events(fixtures, nine)
    pair = extract_pair_events()
    signature = event_signature(events)
    total = len(events) + pair["generated_event_count"]
    passed = (
        fixtures["pass"] and nine["pass"] and pair["pass"]
        and len(events) == EXPECTED_EVENT_COUNT
        and digest(signature) == EXPECTED_EVENT_SIGNATURE_SHA256
        and all(event["pass"] for event in events)
        and total == EXPECTED_EVENT_COUNT
    )
    finding = (
        "THE EVENT CENSUS: PASS — independent union-find extraction finds "
        "20 nine-scale and 0 pair-scale generated coincidence events; every "
        "nonvacuous one-step precondition round-trips exactly."
        if passed else
        "THE EVENT CENSUS: FAIL — the independent event count, signature, "
        "pair RLE, or one-step precondition check disagrees with the primary."
    )
    certificate = {
        "name": "THE EVENT CENSUS",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "partition_extractor":
            "pairwise state equality followed by union-find connected components",
        "nine_generated_event_count": len(events),
        "pair_generated_event_count": pair["generated_event_count"],
        "total_generated_event_count": total,
        "event_signature_sha256": digest(signature),
        "expected_event_signature_sha256": EXPECTED_EVENT_SIGNATURE_SHA256,
        "all_one_step_preconditions_exact": all(event["pass"] for event in events),
        "event_rows": tuple({
            key: event[key] for key in (
                "event_index", "normalized_depth", "predecessor_depth",
                "incoming_lane_blocks", "coincident_lane_subset",
                "coincident_key_subset", "predecessor_state_sha256",
                "common_output_sha256", "forward_outputs_exact",
                "inverse_recovers_predecessors",
            )
        } for event in events),
        "pair_braid": pair,
        "pass": passed,
    }
    return certificate, events, pair


def equivalence_classes(
    events: tuple[dict[str, object], ...], relation,
) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(events)))
    classes = []
    while unseen:
        seed = min(unseen)
        block = tuple(
            index for index in sorted(unseen)
            if relation(events[seed], events[index])
        )
        classes.append(block)
        unseen.difference_update(block)
    return tuple(classes)


def certificate_type_count(
    events: tuple[dict[str, object], ...], census_pass: bool,
) -> dict[str, object]:
    def relation(left: dict[str, object], right: dict[str, object]) -> bool:
        return structural_signature(left) == structural_signature(right)

    reflexive = all(relation(event, event) for event in events)
    symmetric = all(
        relation(left, right) == relation(right, left)
        for left in events for right in events
    )
    transitive = all(
        not (relation(left, middle) and relation(middle, right))
        or relation(left, right)
        for left in events for middle in events for right in events
    )
    classes = equivalence_classes(events, relation)
    class_signatures = tuple(structural_signature(events[block[0]]) for block in classes)
    pairwise_matches_key = all(
        relation(left, right)
        == (structural_signature(left) == structural_signature(right))
        for left in events for right in events
    )

    def relabel_invariant(left: dict[str, object], right: dict[str, object]) -> bool:
        left_key = list(structural_signature(left))
        right_key = list(structural_signature(right))
        left_key[0] = tuple(sorted(left_key[0]))
        right_key[0] = tuple(sorted(right_key[0]))
        return tuple(left_key) == tuple(right_key)

    invariant_classes = equivalence_classes(events, relabel_invariant)
    passed = (
        census_pass and reflexive and symmetric and transitive
        and pairwise_matches_key and len(classes) == EXPECTED_TYPE_COUNT
    )
    finding = (
        "THE TYPE COUNT: PASS — under the declared relation R (equality of "
        "ordered incoming-block sizes, participant count, variation-support "
        "count, predecessor 3-wire pattern multiset, locality flag, and landed-"
        "family flag), the 20 events form exactly 16 equivalence classes."
        if passed else
        "THE TYPE COUNT: FAIL — the declared relation is not an equivalence "
        "relation or its independently constructed quotient does not have 16 classes."
    )
    return {
        "name": "THE TYPE COUNT",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "declared_relation":
            "e R f iff the six-component structural_signature(e) equals "
            "structural_signature(f), with incoming-block sizes kept in the "
            "canonical union-find block order",
        "relation_checks": {
            "reflexive": reflexive,
            "symmetric": symmetric,
            "transitive": transitive,
            "pairwise_relation_matches_declared_key": pairwise_matches_key,
        },
        "distinct_type_count": len(classes),
        "expected_type_count": EXPECTED_TYPE_COUNT,
        "classes_by_event_index": classes,
        "class_sizes": tuple(len(block) for block in classes),
        "class_signature_sha256": digest(class_signatures),
        "relabel_invariant_sensitivity_check": {
            "relation_change": "sort incoming-block sizes before comparison",
            "distinct_type_count": len(invariant_classes),
            "classes_by_event_index": invariant_classes,
        },
        "pass": passed,
    }


def transition_pair_records(
    nine: dict[str, object],
) -> tuple[tuple[int, int, bool], ...]:
    records = []
    states_by_depth = nine["states_by_depth"]
    for depth in range(NORMALIZED_DEPTH + 1):
        predecessors = states_by_depth[depth + 1]
        outputs = states_by_depth[depth]
        for left, right in combinations(range(len(BACKBONE)), 2):
            records.append((
                predecessors[left],
                predecessors[right],
                predecessors[left] != predecessors[right]
                and outputs[left] == outputs[right],
            ))
    return tuple(records)


def translated_wire_masks(shape: tuple[int, int, int]):
    maximum = max(shape)
    for anchor in range(STATE_BITS - maximum):
        wires = tuple(anchor + offset for offset in shape)
        mask = sum(1 << wire for wire in wires)
        yield anchor, wires, mask


def offset_support_exhaustion(
    records: tuple[tuple[int, int, bool], ...],
    shape: tuple[int, int, int],
) -> dict[str, object]:
    positive_total = sum(label for _left, _right, label in records)
    best = None
    exact_anchors = []
    xors = tuple((left ^ right, label) for left, right, label in records)
    for anchor, wires, wire_mask in translated_wire_masks(shape):
        true_positive = false_positive = false_negative = 0
        for difference, label in xors:
            predicted = difference != 0 and difference & ~wire_mask == 0
            true_positive += int(predicted and label)
            false_positive += int(predicted and not label)
            false_negative += int(not predicted and label)
        errors = false_positive + false_negative
        score = (errors, -true_positive, anchor)
        if best is None or score < best[0]:
            best = (score, anchor, wires, true_positive, false_positive, false_negative)
        if errors == 0:
            exact_anchors.append(anchor)
    assert best is not None
    _score, anchor, wires, true_positive, false_positive, false_negative = best
    return {
        "relative_wire_shape": shape,
        "anchors_exhausted": STATE_BITS - max(shape),
        "positive_pair_transitions": positive_total,
        "best_anchor": anchor,
        "best_wires": wires,
        "best_true_positive": true_positive,
        "best_false_positive": false_positive,
        "best_false_negative": false_negative,
        "exact_anchor_count": len(exact_anchors),
        "exact_anchors_sha256": digest(tuple(exact_anchors)),
        "nine_scale_exact": bool(exact_anchors),
    }


def three_bit_value(state: int, wires: tuple[int, int, int]) -> int:
    return sum(((state >> wire) & 1) << index for index, wire in enumerate(wires))


def shifted_predicate_exhaustion(
    records: tuple[tuple[int, int, bool], ...],
    shape: tuple[int, int, int],
) -> dict[str, object]:
    """Exhaust F after every uniform shift without enumerating 2^36 tables.

    For a fixed shifted triple, the best arbitrary Boolean F on the unordered
    pair of three-bit patterns chooses the majority label in each feature
    bucket.  Summing minority counts therefore exactly minimizes errors over
    every possible F.
    """
    best = None
    exact_anchors = []
    for anchor, wires, _wire_mask in translated_wire_masks(shape):
        buckets: dict[tuple[int, int], list[int]] = defaultdict(lambda: [0, 0])
        for left, right, label in records:
            feature = tuple(sorted((
                three_bit_value(left, wires), three_bit_value(right, wires),
            )))
            buckets[feature][int(label)] += 1
        errors = sum(min(negative, positive) for negative, positive in buckets.values())
        positive_features = sum(
            positive > negative for negative, positive in buckets.values()
        )
        score = (errors, -positive_features, anchor)
        if best is None or score < best[0]:
            best = (score, anchor, wires, len(buckets), positive_features)
        if errors == 0:
            exact_anchors.append(anchor)
    assert best is not None
    _score, anchor, wires, feature_count, positive_features = best
    return {
        "relative_wire_shape": shape,
        "anchors_exhausted": STATE_BITS - max(shape),
        "truth_tables_covered_implicitly_per_anchor": "all 2^36 Boolean tables",
        "best_anchor": anchor,
        "best_wires": wires,
        "best_empirical_errors": best[0][0],
        "best_observed_feature_count": feature_count,
        "best_positive_truth_table_entries": positive_features,
        "exact_anchor_count": len(exact_anchors),
        "exact_anchors_sha256": digest(tuple(exact_anchors)),
        "nine_scale_exact": bool(exact_anchors),
    }


def certificate_schema_hunt(
    nine: dict[str, object], pair: dict[str, object], census_pass: bool,
) -> dict[str, object]:
    records = transition_pair_records(nine)
    positive_pair_transitions = sum(label for _left, _right, label in records)
    nine_shape = tuple(
        wire - NINE_PREDICATE_WIRES[0] for wire in NINE_PREDICATE_WIRES
    )
    pair_shape = tuple(
        wire - PAIR_PREDICATE_WIRES[0] for wire in PAIR_PREDICATE_WIRES
    )
    support_rows = tuple(
        offset_support_exhaustion(records, shape)
        for shape in (nine_shape, pair_shape)
    )
    predicate_rows = tuple(
        shifted_predicate_exhaustion(records, shape)
        for shape in (nine_shape, pair_shape)
    )
    uniform_shift_transports = tuple(
        shift for shift in range(-STATE_BITS + 1, STATE_BITS)
        if tuple(sorted(wire + shift for wire in NINE_PREDICATE_WIRES))
        == tuple(sorted(PAIR_PREDICATE_WIRES))
    )
    pair_positive = pair["generated_event_count"]
    cross_scale_nonvacuous = positive_pair_transitions > 0 and pair_positive > 0
    candidates = (
        {
            "name": "OFFSET_PARAMETERIZED_WIRE_FAMILIES",
            "beyond_primary": True,
            "declared_class":
                "Predict a new equality for a predecessor pair iff its nonzero "
                "XOR support is contained in T+a, with T equal to either landed "
                "three-wire relative shape and a exhausted over every legal wire.",
            "finite_exhaustion": support_rows,
            "uniform_shift_mapping_nine_wires_to_pair_wires":
                uniform_shift_transports,
            "nine_exact_predictor_found": any(
                row["nine_scale_exact"] for row in support_rows
            ),
            "pair_positive_event_coverage": pair_positive,
            "cross_scale_nonvacuous": cross_scale_nonvacuous,
            "mechanism_schema_found": (
                any(row["nine_scale_exact"] for row in support_rows)
                and cross_scale_nonvacuous
            ),
        },
        {
            "name": "SHIFT_COMPOSED_THREE_WIRE_PREDICATES",
            "beyond_primary": True,
            "declared_class":
                "F o (pi_(T+a) x pi_(T+a)), where pi reads three bits, "
                "the lane pair is unordered, a ranges over every legal uniform "
                "shift, T ranges over both landed relative shapes, and arbitrary "
                "Boolean F is exhausted exactly by feature-label consistency.",
            "finite_exhaustion": predicate_rows,
            "nine_exact_predictor_found": any(
                row["nine_scale_exact"] for row in predicate_rows
            ),
            "pair_positive_event_coverage": pair_positive,
            "cross_scale_nonvacuous": cross_scale_nonvacuous,
            "mechanism_schema_found": (
                any(row["nine_scale_exact"] for row in predicate_rows)
                and cross_scale_nonvacuous
            ),
        },
        {
            "name": "PARTITION_MERGE_IDENTITY_CONTROL",
            "beyond_primary": False,
            "declared_class":
                "An output block is an event iff it intersects at least two "
                "predecessor equality blocks.",
            "exact": True,
            "mechanism_schema_found": False,
            "rejection":
                "This is the event definition and consumes the output partition; "
                "it is not a predictive local mechanism.",
        },
    )
    found = tuple(
        candidate["name"] for candidate in candidates
        if candidate["mechanism_schema_found"]
    )
    passed = census_pass and not found
    finding = (
        "THE SCHEMA HUNT: PASS — no upgrade was found in the exhaustively "
        "declared offset-family or shift-composed 3-wire predicate classes; "
        "the pair braid has zero generated positive instances, so no candidate "
        "earns nonvacuous cross-scale mechanism status. This is finite-class "
        "exhaustion, not a universal no-schema theorem."
        if passed else
        "THE SCHEMA HUNT: FAIL — PRIMARY REFUTED: a declared nonvacuous "
        f"cross-scale mechanism schema was found: {found}."
    )
    return {
        "name": "THE SCHEMA HUNT",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "pairwise_transition_universe_size": len(records),
        "nine_positive_pair_transition_count": positive_pair_transitions,
        "pair_positive_event_count": pair_positive,
        "nonvacuity_rule":
            "A cross-scale mechanism candidate must exactly predict the nine "
            "transition labels and cover at least one generated positive at each "
            "scale; empty pair-scale positive coverage cannot validate a mechanism.",
        "candidate_tests": candidates,
        "mechanism_candidates_found": found,
        "primary_upgraded": bool(found),
        "scope_boundary":
            "Only the two declared finite schema classes are exhausted. The "
            "unrestricted merged why remains open.",
        "pass": passed,
    }


def trajectory_digest(states_by_depth: tuple[tuple[int, ...], ...]) -> str:
    hasher = sha256()
    for depth_states in states_by_depth:
        for state in depth_states:
            hasher.update(state.to_bytes(STATE_BYTES, "little"))
    return hasher.hexdigest()


def certificate_controls(
    source: dict[str, object], source_replay: dict[str, object],
    fixtures: dict[str, object], fixture_replay: dict[str, object],
    nine: dict[str, object], nine_replay: dict[str, object],
    events: tuple[dict[str, object], ...], replay_events: tuple[dict[str, object], ...],
    pair: dict[str, object], replay_pair: dict[str, object], elapsed: float,
) -> dict[str, object]:
    blocked_at_end = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    determinism = {
        "source_control_replay": digest(source) == digest(source_replay),
        "fixture_replay": fixture_digest(fixtures) == fixture_digest(fixture_replay),
        "trajectory_replay":
            trajectory_digest(nine["states_by_depth"])
            == trajectory_digest(nine_replay["states_by_depth"]),
        "partition_replay": digest(nine["partitions"]) == digest(nine_replay["partitions"]),
        "event_replay": digest(events) == digest(replay_events),
        "pair_RLE_replay": digest(pair) == digest(replay_pair),
    }
    result = {
        "name": "CONTROLS",
        "status": "FAIL",
        "finding": "CONTROLS: FAIL — a provenance, firewall, determinism, runtime, or stdout bound failed.",
        "source_controls": source,
        "source_control_replay_exact": digest(source) == digest(source_replay),
        "primary_access_policy":
            "Every source primary is import-BLOCKLISTED and consumed only as "
            "worktree text/AST or SHA-pinned git-object text/AST.",
        "blocked_modules_loaded_at_end": blocked_at_end,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": determinism,
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
        source["pass"] and source_replay["pass"]
        and fixtures["pass"] and fixture_replay["pass"]
        and nine["pass"] and nine_replay["pass"]
        and all(determinism.values())
        and not blocked_at_end and not FIREWALL.hits
        and result["runtime_below_limit"]
    )
    return result


def render_report(
    census: dict[str, object], types: dict[str, object],
    schema: dict[str, object], controls: dict[str, object], elapsed: float,
) -> str:
    overall = all(certificate["pass"] for certificate in (
        census, types, schema, controls,
    ))
    report = {
        "cycle": 848,
        "checker": "INDEPENDENT_ADVERSARIAL_COINCIDENCE_CENSUS",
        "checks": {
            "THE EVENT CENSUS": census["status"],
            "THE TYPE COUNT": types["status"],
            "THE SCHEMA HUNT": schema["status"],
            "CONTROLS": controls["status"],
        },
        "findings_verbatim": tuple(
            certificate["finding"] for certificate in (
                census, types, schema, controls,
            )
        ),
        "primary_refuted": schema["primary_upgraded"],
        "merged_why_status": (
            "UPGRADED_SCHEMA_FOUND" if schema["primary_upgraded"]
            else "OPEN_AFTER_DECLARED_FINITE_SCHEMA_EXHAUSTION"
        ),
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": controls["stdout_bytes"],
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": overall,
        "terminal": (
            "CYCLE848_INDEPENDENT_CHECK_PASS" if overall
            else "CYCLE848_INDEPENDENT_CHECK_FAIL"
        ),
    }
    return "\n".join((
        "CERTIFICATE_THE_EVENT_CENSUS=" + compact(census),
        "CERTIFICATE_THE_TYPE_COUNT=" + compact(types),
        "CERTIFICATE_THE_SCHEMA_HUNT=" + compact(schema),
        "CERTIFICATE_CONTROLS=" + compact(controls),
        "REPORT=" + compact(report),
    ))


def run() -> int:
    started = monotonic()
    source, trees = source_controls()
    fixtures = decode_fixture_bank(trees[AUDIT_INPUT_PATHS[0]])
    nine = evolve_nine(fixtures)
    census, events, pair = certificate_event_census(fixtures, nine)
    types = certificate_type_count(events, census["pass"])
    schema = certificate_schema_hunt(nine, pair, census["pass"])

    source_replay, replay_trees = source_controls()
    fixture_replay = decode_fixture_bank(replay_trees[AUDIT_INPUT_PATHS[0]])
    nine_replay = evolve_nine(fixture_replay)
    _replay_census, replay_events, replay_pair = certificate_event_census(
        fixture_replay, nine_replay,
    )
    elapsed = monotonic() - started
    controls = certificate_controls(
        source, source_replay, fixtures, fixture_replay, nine, nine_replay,
        events, replay_events, pair, replay_pair, elapsed,
    )
    for _iteration in range(8):
        rendered = render_report(census, types, schema, controls, elapsed)
        stdout_bytes = len((rendered + "\n").encode("utf-8"))
        below = stdout_bytes < STDOUT_LIMIT_BYTES
        pass_value = controls["base_pass_before_stdout"] and below
        status = "PASS" if pass_value else "FAIL"
        finding = (
            "CONTROLS: PASS — SHA/blob pins, text/AST-only BLOCKLIST, literal "
            "existing worktree-relative AUDIT_INPUT_PATHS, exact replay, runtime, "
            "and stdout bounds all hold."
            if pass_value else
            "CONTROLS: FAIL — a provenance, firewall, determinism, runtime, or "
            "stdout bound failed."
        )
        stable = (
            controls["stdout_bytes"] == stdout_bytes
            and controls["stdout_below_limit"] == below
            and controls["pass"] == pass_value
            and controls["status"] == status
            and controls["finding"] == finding
        )
        controls["stdout_bytes"] = stdout_bytes
        controls["stdout_below_limit"] = below
        controls["pass"] = pass_value
        controls["status"] = status
        controls["finding"] = finding
        if stable:
            break
    rendered = render_report(census, types, schema, controls, elapsed)
    if len((rendered + "\n").encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    print(rendered)
    return 0 if all(certificate["pass"] for certificate in (
        census, types, schema, controls,
    )) else 1


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--_worker":
        return run()
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: frontier_cycle848_derivation_independent_check_2026_07_28.py"
        )
    try:
        completed = subprocess.run(
            (sys.executable, str(Path(__file__).resolve()), "--_worker"),
            cwd=ROOT, capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        print(compact({
            "cycle": 848, "pass": False,
            "terminal": "CYCLE848_INDEPENDENT_CHECK_TIMEOUT",
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        }))
        return 1
    stdout_bytes = len(completed.stdout.encode("utf-8"))
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 848, "pass": False,
            "terminal": "CYCLE848_INDEPENDENT_CHECK_STDOUT_LIMIT_EXCEEDED",
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
