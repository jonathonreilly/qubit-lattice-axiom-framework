#!/usr/bin/env python3
"""Independent adversarial check of Cycle 855's coupled free sector.

The cited sources are SHA/blob pinned and parsed only as text/AST.  This
checker reconstructs the primitive fixtures, the free complement, the full
boundary census, and the braid probes without importing or executing Cycle
855 or any of its source primaries.  In addition to checking the published
cross-parameter coupling, it tests closure separately at every fixed exact
inherited parameter value.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle855_free_sector_reduction_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle848_braid_derivation_2026_07_28.py",
    "scripts/frontier_cycle853_generator_usage_census_2026_07_28.py",
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
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "2e61ea66ffb32a511c0e60c6b084fe4207b2e55d04bfe4de136516a91ca94a40",
    AUDIT_INPUT_PATHS[1]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[2]:
        "a9fdefbffe16495e62258804d3abbddb48aaa500e365f56c739c24959162ca48",
    AUDIT_INPUT_PATHS[3]:
        "946a2ffcbb3ddad19ff2213831593f7ea93a97d9a680fec50a674391592863b7",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "d3aa88b65b7cc8aae565fe12902a65b39576d3b5",
    AUDIT_INPUT_PATHS[1]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[2]: "c55036475e2389565b1c4b69e96595db99e03779",
    AUDIT_INPUT_PATHS[3]: "b28e895ffa847973a5a8ae594d3eb7796b0bc018",
}

RING_STATIONS = 11
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
FULL_TRANSITIONS = 891486
NINE_FUNNEL_MOVEMENT = 14739
NORMALIZED_DEPTH = 64
PREDECESSOR_DEPTH = NORMALIZED_DEPTH + 1
EXPECTED_EVENT_COUNT = 20
EXPECTED_PROBE_COUNT = 86
EXPECTED_FREE_COUNT = 495
EXPECTED_INHERITED_COUNT = STATE_BITS - EXPECTED_FREE_COUNT
EXPECTED_WITNESS_COUNT = 3447
EXPECTED_CHANNEL_COUNT = 50
EXPECTED_AFFECTED_FREE_WIRES = (71, 105, 124, 125, 255, 256)
EXPECTED_X_CHANNEL = (1, 6)
EXPECTED_X_STATES = ((0, 1), (1, 0))
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_TARGET_RAW_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)
EXPECTED_EVENT_SIGNATURE_SHA256 = (
    "7ae45bbd8b6e688b9abdadd0e33dcfd300e2649b4776386a5b8ec48eb62e064a"
)
EXPECTED_PARTITION_SHA256 = (
    "726b74aefc7afa6e1790c7dc73a59eacdadeec72246e19ac01104be09d49829d"
)

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _SourceFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only audit source is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _SourceFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    prefix = f"blob {len(payload)}\0".encode("ascii")
    return sha1(prefix + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    nodes = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            nodes.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            nodes.append(node.value)
    if len(nodes) != 1:
        return None
    try:
        return ast.literal_eval(nodes[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


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


def support(mask: int) -> tuple[int, ...]:
    wires = []
    while mask:
        bit = mask & -mask
        wires.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(wires)


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
    fixture_tree = trees[AUDIT_INPUT_PATHS[1]]
    braid_tree = trees[AUDIT_INPUT_PATHS[2]]
    census_tree = trees[AUDIT_INPUT_PATHS[3]]
    primary_tree = trees[AUDIT_INPUT_PATHS[0]]
    ast_basis = {
        "cycle830_literal_fixture_basis": {
            "decode_fixtures", "build_words", "apply_word",
        } <= function_names(fixture_tree),
        "cycle848_braid_basis": {
            "evolve_nine", "transition_rows", "certificate_b_schema_hunt",
        } <= function_names(braid_tree),
        "cycle853_boundary_basis": {
            "build_masked_schedule", "write_kernel_inputs", "execute_kernel",
        } <= function_names(census_tree),
        "landed_nine_predicates_exact": (
            literal_assignment(braid_tree, "NINE_PREDICATE_WIRES")
            == (40, 81, 105)
        ),
        "landed_pair_predicates_exact": (
            literal_assignment(braid_tree, "PAIR_PREDICATE_WIRES")
            == (88, 124, 125)
        ),
        "landed_mark_definition_exact": (
            literal_assignment(primary_tree, "K3_MARK_BITS") == (256, 262)
        ),
        "cycle853_constants_exact": (
            literal_assignment(census_tree, "BACKBONE") == BACKBONE
            and literal_assignment(census_tree, "EVENTS") == EVENTS
            and literal_assignment(census_tree, "RESOLUTION_MOMENTS")
            == RESOLUTION_MOMENTS
        ),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": (
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS
        ),
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "AST_basis": ast_basis,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "source_primary_text_AST_only": AUDIT_INPUT_PATHS[0],
        "all_inputs_text_AST_only": AUDIT_INPUT_PATHS,
        "direct_frontier_imports": tuple(sorted(
            name for name in imports if name.startswith("frontier_cycle")
        )),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "pass": False,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(ast_basis.values())
        and not result["direct_frontier_imports"]
        and not FIREWALL.hits
    )
    return result, trees


def lawful_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


def decode_literal_fixtures(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(literal_assignment(tree, name) for name in (
        "GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85",
    ))
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("literal fixture bank unavailable")
    gate_raw, family_raw, target_raw = tuple(
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    cursor = 22
    macros = []
    for length in lengths:
        macro = []
        for _ in range(length):
            macro.append(struct.unpack("<BHHH", gate_raw[cursor:cursor + 7]))
            cursor += 7
        macros.append(tuple(macro))
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
        "macro_count": len(macros),
        "primitive_gate_count": sum(lengths),
        "family_key_count": len(states),
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "target_raw_sha256": sha256(target_raw).hexdigest(),
    }
    public["pass"] = (
        len(macros) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and cursor == len(gate_raw)
        and len(states) == FAMILY_SIZE
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and len(target_raw) == STATE_BYTES
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and public["target_raw_sha256"] == EXPECTED_TARGET_RAW_SHA256
    )
    return {
        "macros": tuple(macros),
        "states": states,
        "target": int.from_bytes(target_raw, "little"),
        "public": public,
    }


def build_words(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
) -> dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]]:
    words = {}
    for pair in BACKBONE:
        rows = []
        for phase in range(RING_STATIONS):
            active = {
                (pair[0] + phase) % RING_STATIONS,
                (pair[1] + phase) % RING_STATIONS,
            }
            for station, macro in enumerate(macros):
                if station in active:
                    rows.extend(macro)
        if len(rows) != WORD_GATE_COUNT:
            raise AssertionError(("generator word drift", pair, len(rows)))
        words[pair] = tuple(rows)
    return words


def target_wire(gate: tuple[int, int, int, int]) -> int:
    kind, first, second, third = gate
    return first if kind == 0 else second if kind == 1 else third


def reconstruct_free_sector(
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
    nine_predicates: tuple[int, ...], pair_predicates: tuple[int, ...],
    mark_bits: tuple[int, ...],
) -> tuple[dict[str, object], dict[str, object]]:
    target_counts = []
    for pair in BACKBONE:
        counts: dict[int, list[int]] = defaultdict(lambda: [0, 0, 0])
        for gate in words[pair]:
            counts[target_wire(gate)][gate[0]] += 1
        target_counts.append(counts)
    profiles = {}
    signatures = {}
    for wire in range(STATE_BITS):
        profile = tuple(tuple(counts[wire]) for counts in target_counts)
        profiles[wire] = profile
        if all(cnot == 0 and toffoli == 0 for _x, cnot, toffoli in profile):
            signatures[wire] = tuple(x_count & 1 for x_count, _c, _t in profile)
    zero = (0,) * len(BACKBONE)
    inherited = tuple(wire for wire in range(STATE_BITS) if signatures.get(wire) == zero)
    inherited_set = set(inherited)
    free = tuple(wire for wire in range(STATE_BITS) if wire not in inherited_set)
    free_set = set(free)
    braid_support = tuple(sorted(set(nine_predicates) | set(pair_predicates)))
    physical = {
        "wire_105": {
            "identification": "NINE_THREE_WIRE_PREDICATE",
            "landed_tuple": nine_predicates,
            "confirmed": 105 in nine_predicates,
        },
        "wire_124": {
            "identification": "PAIR_THREE_WIRE_PREDICATE",
            "landed_tuple": pair_predicates,
            "confirmed": 124 in pair_predicates,
        },
        "wire_125": {
            "identification": "PAIR_THREE_WIRE_PREDICATE",
            "landed_tuple": pair_predicates,
            "confirmed": 125 in pair_predicates,
        },
        "wire_256": {
            "identification": "K3_MARK_BIT",
            "landed_tuple": mark_bits,
            "confirmed": 256 in mark_bits,
        },
    }
    certificate = {
        "independent_basis": (
            "Primitive target-kind counts over each independently assembled "
            "6,212-gate generator word; inherited means X-only zero parity "
            "under all nine words, and free is its exact complement."
        ),
        "inherited_wire_count": len(inherited),
        "inherited_wire_ranges": ranges(inherited),
        "free_wire_count": len(free),
        "free_wire_ranges": ranges(free),
        "free_wire_sha256": digest(free),
        "mark_bits": mark_bits,
        "mark_bits_free": tuple(bit for bit in mark_bits if bit in free_set),
        "landed_nine_predicate_wires": nine_predicates,
        "landed_pair_predicate_wires": pair_predicates,
        "braid_support_wires": braid_support,
        "braid_supports_free": tuple(bit for bit in braid_support if bit in free_set),
        "physical_identifications": physical,
        "finding": "FREE_SECTOR_495_WITH_MARK_AND_BRAID_SUPPORTS",
        "pass": False,
    }
    certificate["pass"] = (
        len(inherited) == EXPECTED_INHERITED_COUNT
        and len(free) == EXPECTED_FREE_COUNT
        and set(inherited).isdisjoint(free)
        and len(inherited) + len(free) == STATE_BITS
        and set(mark_bits) <= free_set
        and set(braid_support) <= free_set
        and all(row["confirmed"] for row in physical.values())
    )
    return certificate, {
        "profiles": profiles,
        "signatures": signatures,
        "inherited_wires": inherited,
        "free_wires": free,
    }


def compile_words(
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> dict[tuple[int, int], tuple[tuple[int, int, int], ...]]:
    result = {}
    for pair, word in words.items():
        compiled = []
        for kind, first, second, third in word:
            if kind == 0:
                compiled.append((0, 0, 1 << first))
            elif kind == 1:
                compiled.append((1, 1 << first, 1 << second))
            elif kind == 2:
                compiled.append((2, (1 << first) | (1 << second), 1 << third))
            else:
                raise AssertionError(("unknown gate", kind))
        result[pair] = tuple(compiled)
    return result


def apply_word(
    state: int, word: tuple[tuple[int, int, int], ...], *, reverse: bool = False,
) -> int:
    gates = reversed(word) if reverse else word
    for kind, controls, target in gates:
        if kind == 0 or state & controls == controls:
            state ^= target
    return state


def make_movement_schedule(
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


def states_to_columns(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        value = state
        while value:
            bit = value & -value
            columns[bit.bit_length() - 1] |= 1 << lane
            value ^= bit
    return columns


def columns_to_states(columns: list[int], lane_count: int) -> tuple[int, ...]:
    result = [0] * lane_count
    lane_mask = (1 << lane_count) - 1
    for wire, column in enumerate(columns):
        live = column & lane_mask
        while live:
            bit = live & -live
            result[bit.bit_length() - 1] |= 1 << wire
            live ^= bit
    return tuple(result)


def advance_columns(
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
            raise AssertionError(("unknown gate", kind))


def partition(states: tuple[object, ...]) -> tuple[tuple[int, ...], ...]:
    groups: dict[object, list[int]] = {}
    for lane, state in enumerate(states):
        groups.setdefault(state, []).append(lane)
    return tuple(sorted(
        (tuple(group) for group in groups.values()), key=lambda group: group[0],
    ))


def reconstruct_braid(
    fixtures: dict[str, object],
    compiled: dict[tuple[int, int], tuple[tuple[int, int, int], ...]],
    free_wires: tuple[int, ...], nine_predicates: tuple[int, ...],
) -> tuple[dict[str, object], tuple[tuple[bytes, bytes, int], ...]]:
    states = fixtures["states"]
    macros = fixtures["macros"]
    assert isinstance(states, dict) and isinstance(macros, tuple)
    columns = states_to_columns(tuple(states[(0, pair)] for pair in BACKBONE))
    schedule = make_movement_schedule(macros)
    tail = []
    for movement in range(1, NINE_FUNNEL_MOVEMENT + 1):
        advance_columns(columns, schedule)
        if movement >= NINE_FUNNEL_MOVEMENT - PREDECESSOR_DEPTH:
            tail.append(columns_to_states(columns, len(BACKBONE)))
    depths = tuple(reversed(tail))
    partitions = tuple(partition(row) for row in depths[:NORMALIZED_DEPTH + 1])
    event_rows = []
    probes = []
    all_local = True
    local_event_count = 0
    event_support_union = set()
    all_rule_exact = True
    for depth in range(NORMALIZED_DEPTH, -1, -1):
        before_all = depths[depth + 1]
        after_all = depths[depth]
        before_partition = partition(before_all)
        for output_block in partition(after_all):
            incoming = tuple(
                tuple(lane for lane in block if lane in output_block)
                for block in before_partition
                if any(lane in output_block for lane in block)
            )
            if len(incoming) < 2:
                continue
            lanes = tuple(output_block)
            variation = 0
            for lane in lanes[1:]:
                variation |= before_all[lanes[0]] ^ before_all[lane]
            variation_support = support(variation)
            exact_event_support = set(nine_predicates) | set(variation_support)
            event_support_union.update(exact_event_support)
            rule_exact = all(
                apply_word(before_all[lane], compiled[BACKBONE[lane]])
                == after_all[lane]
                for lane in lanes
            )
            inverse_exact = all(
                apply_word(
                    after_all[lanes[0]], compiled[BACKBONE[lane]], reverse=True,
                ) == before_all[lane]
                for lane in lanes
            )
            all_rule_exact &= rule_exact and inverse_exact
            is_local = set(variation_support) <= set(nine_predicates)
            all_local &= is_local
            local_event_count += int(is_local)
            event_rows.append((depth, incoming, lanes))
            for lane in lanes:
                before = project(before_all[lane], free_wires)
                after = project(after_all[lane], free_wires)
                probes.append((before, after, lane))
    signature = tuple(event_rows)
    public = {
        "event_count": len(event_rows),
        "transition_probe_count": len(probes),
        "event_signature_sha256": digest(signature),
        "normalized_partition_sha256": digest(partitions),
        "terminal_matches_fixture_target": all(
            state == fixtures["target"] for state in depths[0]
        ),
        "all_variation_inside_landed_three_wire_support": all_local,
        "three_wire_local_event_count": local_event_count,
        "exact_event_support_union": tuple(sorted(event_support_union)),
        "all_exact_event_support_wires_free": event_support_union <= set(free_wires),
        "all_forward_and_inverse_rules_exact": all_rule_exact,
        "event_signature": signature,
    }
    public["pass"] = (
        len(event_rows) == EXPECTED_EVENT_COUNT
        and len(probes) == EXPECTED_PROBE_COUNT
        and public["event_signature_sha256"] == EXPECTED_EVENT_SIGNATURE_SHA256
        and public["normalized_partition_sha256"] == EXPECTED_PARTITION_SHA256
        and public["terminal_matches_fixture_target"]
        and public["all_exact_event_support_wires_free"]
        and all_rule_exact
    )
    return public, tuple(probes)


def project(state: int, free_wires: tuple[int, ...]) -> bytes:
    packed = bytearray((len(free_wires) + 7) // 8)
    for index, wire in enumerate(free_wires):
        if (state >> wire) & 1:
            packed[index >> 3] |= 1 << (index & 7)
    return bytes(packed)


def make_full_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for phase in range(RING_STATIONS):
        station_masks = [0] * RING_STATIONS
        for lane, (_event, pair) in enumerate(lanes):
            station_masks[(pair[0] + phase) % RING_STATIONS] |= 1 << lane
            station_masks[(pair[1] + phase) % RING_STATIONS] |= 1 << lane
        for station, macro in enumerate(macros):
            if station_masks[station]:
                rows.extend((*gate, station_masks[station]) for gate in macro)
    return tuple(rows)


def inherited_parameters(
    states: dict[tuple[int, tuple[int, int]], int],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    inherited_wires: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...], dict[str, object]]:
    inherited_mask = sum(1 << wire for wire in inherited_wires)
    values = tuple(states[key] & inherited_mask for key in lanes)
    value_to_id: dict[int, int] = {}
    ids = []
    for value in values:
        if value not in value_to_id:
            value_to_id[value] = len(value_to_id)
        ids.append(value_to_id[value])
    class_values = tuple(
        value for value, _identifier in sorted(
            value_to_id.items(), key=lambda item: item[1],
        )
    )
    public = {
        "parameter_count": len(class_values),
        "lane_parameter_ids": tuple(ids),
        "parameter_lane_multiplicities": tuple(sorted(Counter(ids).items())),
        "parameter_sha256": tuple(
            sha256(value.to_bytes(STATE_BYTES, "little")).hexdigest()
            for value in class_values
        ),
        "x1_x6_values": tuple(
            ((value >> 1) & 1, (value >> 6) & 1) for value in class_values
        ),
    }
    return tuple(ids), class_values, public


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
#define MAX_PARAMETERS 27
#define MAX_STEPS 51115
#define FULL_STATES 891513
#define FULL_TRANSITIONS 891486

typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c; uint32_t mask;
} Gate;
typedef struct __attribute__((packed)) {
    uint8_t free_bits[FREE_BYTES]; uint8_t parameter, lane;
} StateRow;
typedef struct __attribute__((packed)) {
    uint8_t input[FREE_BYTES], output[FREE_BYTES];
    uint8_t generator, parameter, lane; uint32_t time;
} StepRow;
typedef struct __attribute__((packed)) {
    uint8_t input[FREE_BYTES], output[FREE_BYTES]; uint8_t generator;
} Probe;

static void die(const char *message) { perror(message); exit(2); }
static void *load(const char *path, size_t item_size, size_t *count) {
    FILE *file = fopen(path, "rb"); if (!file) die(path);
    if (fseek(file, 0, SEEK_END)) die("fseek");
    long bytes = ftell(file); if (bytes < 0 || bytes % (long)item_size) die("size");
    rewind(file);
    void *payload = malloc(bytes ? (size_t)bytes : 1); if (!payload) die("malloc");
    if (bytes && fread(payload, 1, (size_t)bytes, file) != (size_t)bytes) die("fread");
    fclose(file); *count = (size_t)bytes / item_size; return payload;
}
static uint32_t states_active(int time) {
    uint32_t mask = 0;
    if (time <= 14744) mask |= (UINT32_C(1) << 9) - 1;
    if (time <= 33195) mask |= ((UINT32_C(1) << 9) - 1) << 9;
    if (time <= 51115) mask |= ((UINT32_C(1) << 9) - 1) << 18;
    return mask;
}
static uint32_t steps_active(int time) {
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
static int state_compare(const void *left_raw, const void *right_raw) {
    const StateRow *left = left_raw, *right = right_raw;
    if (left->parameter != right->parameter)
        return (left->parameter > right->parameter) - (left->parameter < right->parameter);
    int order = memcmp(left->free_bits, right->free_bits, FREE_BYTES);
    if (order) return order;
    return (left->lane > right->lane) - (left->lane < right->lane);
}
static int step_compare(const void *left_raw, const void *right_raw) {
    const StepRow *left = left_raw, *right = right_raw;
    if (left->generator != right->generator)
        return (left->generator > right->generator) - (left->generator < right->generator);
    int order = memcmp(left->input, right->input, FREE_BYTES);
    if (order) return order;
    if (left->parameter != right->parameter)
        return (left->parameter > right->parameter) - (left->parameter < right->parameter);
    if (left->lane != right->lane)
        return (left->lane > right->lane) - (left->lane < right->lane);
    return (left->time > right->time) - (left->time < right->time);
}
static int same_cross_key(const StepRow *left, const StepRow *right) {
    return left->generator == right->generator
        && memcmp(left->input, right->input, FREE_BYTES) == 0;
}
static int compare_probe(const StepRow *row, const Probe *probe) {
    if (row->generator != probe->generator)
        return (row->generator > probe->generator) - (row->generator < probe->generator);
    return memcmp(row->input, probe->input, FREE_BYTES);
}

int main(int argc, char **argv) {
    if (argc != 8) { fprintf(stderr, "argc\n"); return 2; }
    size_t gate_n, column_n, free_n, assignment_n, probe_n;
    Gate *schedule = load(argv[1], sizeof(Gate), &gate_n);
    uint32_t *initial = load(argv[2], sizeof(uint32_t), &column_n);
    uint16_t *free_wires = load(argv[3], sizeof(uint16_t), &free_n);
    uint8_t *assignments = load(argv[4], sizeof(uint8_t), &assignment_n);
    Probe *probes = load(argv[5], sizeof(Probe), &probe_n);
    if (column_n != STATE_BITS || free_n != FREE_WIRES || assignment_n != LANES) return 3;
    int parameter_count = 0;
    for (int lane = 0; lane < LANES; ++lane)
        if ((int)assignments[lane] + 1 > parameter_count)
            parameter_count = (int)assignments[lane] + 1;
    StateRow *states = malloc((size_t)FULL_STATES * sizeof(StateRow));
    StepRow *steps = malloc((size_t)FULL_TRANSITIONS * sizeof(StepRow));
    if (!states || !steps) die("record malloc");
    uint32_t columns[STATE_BITS]; memcpy(columns, initial, sizeof(columns));
    size_t state_n = 0, step_n = 0;
    for (int time = 0; time <= MAX_STEPS; ++time) {
        uint32_t state_mask = states_active(time);
        for (int lane = 0; lane < LANES; ++lane) if ((state_mask >> lane) & 1U) {
            StateRow *row = &states[state_n++];
            pack_free(row->free_bits, columns, free_wires, lane);
            row->parameter = assignments[lane]; row->lane = (uint8_t)lane;
        }
        if (time == MAX_STEPS) break;
        uint32_t step_mask = steps_active(time);
        size_t step_start = step_n;
        for (int lane = 0; lane < LANES; ++lane) if ((step_mask >> lane) & 1U) {
            StepRow *row = &steps[step_n++];
            pack_free(row->input, columns, free_wires, lane);
            row->generator = (uint8_t)(lane % GENERATORS);
            row->parameter = assignments[lane]; row->lane = (uint8_t)lane;
            row->time = (uint32_t)time;
        }
        for (size_t i = 0; i < gate_n; ++i) {
            Gate gate = schedule[i]; uint32_t mask = gate.mask & step_mask;
            if (gate.kind == 0) columns[gate.a] ^= mask;
            else if (gate.kind == 1) columns[gate.b] ^= columns[gate.a] & mask;
            else if (gate.kind == 2)
                columns[gate.c] ^= columns[gate.a] & columns[gate.b] & mask;
            else return 4;
        }
        size_t row_index = step_start;
        for (int lane = 0; lane < LANES; ++lane) if ((step_mask >> lane) & 1U)
            pack_free(steps[row_index++].output, columns, free_wires, lane);
        if (row_index != step_n) return 5;
    }
    if (state_n != FULL_STATES || step_n != FULL_TRANSITIONS) return 6;

    qsort(states, state_n, sizeof(StateRow), state_compare);
    uint64_t parameter_sizes[MAX_PARAMETERS] = {0};
    for (size_t start = 0; start < state_n;) {
        size_t end = start + 1;
        while (end < state_n
               && states[start].parameter == states[end].parameter
               && !memcmp(states[start].free_bits, states[end].free_bits, FREE_BYTES)) ++end;
        ++parameter_sizes[states[start].parameter]; start = end;
    }

    qsort(steps, step_n, sizeof(StepRow), step_compare);
    uint64_t cross_groups = 0, cross_collision_groups = 0;
    uint64_t distinct_parameter_groups = 0, coupling_groups = 0, coupling_pairs = 0;
    uint64_t parameter_step_groups = 0, parameter_collision_groups = 0;
    uint64_t parameter_disagreement_groups = 0, parameter_disagreement_pairs = 0;
    uint64_t lane_step_groups = 0, lane_disagreement_groups = 0, lane_disagreement_pairs = 0;
    FILE *witness = fopen(argv[7], "wb"); if (!witness) die(argv[7]);
    for (size_t start = 0; start < step_n;) {
        size_t end = start + 1;
        while (end < step_n && same_cross_key(&steps[start], &steps[end])) ++end;
        ++cross_groups; if (end - start > 1) ++cross_collision_groups;
        int distinct_parameters = 0, last_parameter = -1, cross_coupled = 0;
        for (size_t pstart = start; pstart < end;) {
            size_t pend = pstart + 1;
            while (pend < end && steps[pend].parameter == steps[pstart].parameter) ++pend;
            ++parameter_step_groups; ++distinct_parameters;
            if (pend - pstart > 1) ++parameter_collision_groups;
            int parameter_bad = 0;
            for (size_t left = pstart; left < pend; ++left)
                for (size_t right = left + 1; right < pend; ++right)
                    if (memcmp(steps[left].output, steps[right].output, FREE_BYTES)) {
                        parameter_bad = 1; ++parameter_disagreement_pairs;
                    }
            if (parameter_bad) ++parameter_disagreement_groups;
            for (size_t lstart = pstart; lstart < pend;) {
                size_t lend = lstart + 1;
                while (lend < pend && steps[lend].lane == steps[lstart].lane) ++lend;
                ++lane_step_groups; int lane_bad = 0;
                for (size_t left = lstart; left < lend; ++left)
                    for (size_t right = left + 1; right < lend; ++right)
                        if (memcmp(steps[left].output, steps[right].output, FREE_BYTES)) {
                            lane_bad = 1; ++lane_disagreement_pairs;
                        }
                if (lane_bad) ++lane_disagreement_groups;
                lstart = lend;
            }
            last_parameter = steps[pstart].parameter; (void)last_parameter;
            pstart = pend;
        }
        if (distinct_parameters > 1) ++distinct_parameter_groups;
        for (size_t left = start; left < end; ++left)
            for (size_t right = left + 1; right < end; ++right)
                if (memcmp(steps[left].output, steps[right].output, FREE_BYTES)) {
                    cross_coupled = 1;
                    if (fwrite(&steps[left], sizeof(StepRow), 1, witness) != 1
                        || fwrite(&steps[right], sizeof(StepRow), 1, witness) != 1)
                        die("witness write");
                    ++coupling_pairs;
                }
        if (cross_coupled) ++coupling_groups;
        start = end;
    }
    fclose(witness);

    uint64_t probe_matches = 0, probe_mismatches = 0;
    for (size_t p = 0; p < probe_n; ++p) {
        size_t lo = 0, hi = step_n;
        while (lo < hi) {
            size_t mid = lo + (hi - lo) / 2;
            if (compare_probe(&steps[mid], &probes[p]) < 0) lo = mid + 1;
            else hi = mid;
        }
        if (lo < step_n && compare_probe(&steps[lo], &probes[p]) == 0) {
            int matched = 0;
            for (size_t index = lo;
                 index < step_n && compare_probe(&steps[index], &probes[p]) == 0;
                 ++index)
                if (!memcmp(steps[index].output, probes[p].output, FREE_BYTES)) {
                    matched = 1; break;
                }
            if (matched) ++probe_matches; else ++probe_mismatches;
        }
    }

    FILE *summary = fopen(argv[6], "w"); if (!summary) die(argv[6]);
    fprintf(summary,
        "schedule_rows=%zu\nfull_reachable_states=%zu\nfull_transitions=%zu\n"
        "parameter_count=%d\ncross_key_groups=%" PRIu64 "\n"
        "cross_key_collision_groups=%" PRIu64 "\n"
        "cross_key_distinct_parameter_groups=%" PRIu64 "\n"
        "coupling_groups=%" PRIu64 "\ncoupling_pair_witnesses=%" PRIu64 "\n"
        "parameter_step_groups=%" PRIu64 "\nparameter_collision_groups=%" PRIu64 "\n"
        "parameter_disagreement_groups=%" PRIu64 "\nparameter_disagreement_pairs=%" PRIu64 "\n"
        "lane_step_groups=%" PRIu64 "\nlane_disagreement_groups=%" PRIu64 "\n"
        "lane_disagreement_pairs=%" PRIu64 "\nprobe_count=%zu\n"
        "probe_matches=%" PRIu64 "\nprobe_mismatches=%" PRIu64 "\n",
        gate_n, state_n, step_n, parameter_count, cross_groups,
        cross_collision_groups, distinct_parameter_groups, coupling_groups,
        coupling_pairs, parameter_step_groups, parameter_collision_groups,
        parameter_disagreement_groups, parameter_disagreement_pairs,
        lane_step_groups, lane_disagreement_groups, lane_disagreement_pairs,
        probe_n, probe_matches, probe_mismatches);
    for (int parameter = 0; parameter < parameter_count; ++parameter)
        fprintf(summary, "parameter_size_%d=%" PRIu64 "\n",
                parameter, parameter_sizes[parameter]);
    fclose(summary);
    free(schedule); free(initial); free(free_wires); free(assignments); free(probes);
    free(states); free(steps); return 0;
}
'''


def write_kernel_inputs(
    directory: Path,
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    states: dict[tuple[int, tuple[int, int]], int],
    free_wires: tuple[int, ...], parameter_ids: tuple[int, ...],
    probes: tuple[tuple[bytes, bytes, int], ...],
) -> dict[str, object]:
    schedule = make_full_schedule(macros, lanes)
    payloads = {
        "schedule.bin": b"".join(struct.pack("<BHHHI", *row) for row in schedule),
        "columns.bin": struct.pack(f"<{STATE_BITS}I", *tuple(sum(
            ((states[key] >> wire) & 1) << lane
            for lane, key in enumerate(lanes)
        ) for wire in range(STATE_BITS))),
        "free.bin": struct.pack(f"<{len(free_wires)}H", *free_wires),
        "parameters.bin": bytes(parameter_ids),
        "probes.bin": b"".join(
            before + after + bytes((generator,))
            for before, after, generator in probes
        ),
    }
    for name, payload in payloads.items():
        (directory / name).write_bytes(payload)
    return {
        "schedule_rows": len(schedule),
        "probe_count": len(probes),
        "input_sha256": tuple(
            (name, sha256(payload).hexdigest())
            for name, payload in payloads.items()
        ),
    }


def compile_kernel(directory: Path) -> dict[str, object]:
    source = directory / "checker.c"
    binary = directory / "checker"
    source.write_text(KERNEL_C, encoding="utf-8")
    completed = subprocess.run(
        ("cc", "-O3", "-std=c11", str(source), "-o", str(binary)),
        cwd=ROOT, check=True, capture_output=True, text=True, timeout=60,
    )
    compiler = subprocess.run(
        ("cc", "--version"), check=True, capture_output=True,
        text=True, timeout=20,
    ).stdout.splitlines()[0]
    return {
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "binary_sha256": sha256(binary.read_bytes()).hexdigest(),
        "compiler": compiler,
        "compiler_stderr": completed.stderr,
    }


def execute_kernel(directory: Path, label: str) -> dict[str, object]:
    summary_path = directory / f"summary-{label}.txt"
    witness_path = directory / f"witness-{label}.bin"
    completed = subprocess.run(
        (
            str(directory / "checker"), str(directory / "schedule.bin"),
            str(directory / "columns.bin"), str(directory / "free.bin"),
            str(directory / "parameters.bin"), str(directory / "probes.bin"),
            str(summary_path), str(witness_path),
        ),
        cwd=ROOT, check=True, capture_output=True, text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    summary = {}
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        key, raw_value = line.split("=", 1)
        summary[key] = int(raw_value)
    witness = witness_path.read_bytes()
    return {
        "summary": summary,
        "witness": witness,
        "witness_sha256": sha256(witness).hexdigest(),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def decode_coupling_witnesses(
    payload: bytes, free_wires: tuple[int, ...],
    parameter_values: tuple[int, ...],
) -> dict[str, object]:
    free_bytes = (len(free_wires) + 7) // 8
    record_bytes = 2 * free_bytes + 3 + 4
    if len(payload) % (2 * record_bytes):
        raise AssertionError(("witness payload size", len(payload), record_bytes))
    witness_count = len(payload) // (2 * record_bytes)
    channels: Counter[tuple[object, ...]] = Counter()
    affected = set()
    generators = set()
    x_state_pairs = set()
    all_same_input = True
    all_distinct_parameter = True
    all_distinct_output = True
    first_pair = None
    for offset in range(0, len(payload), 2 * record_bytes):
        decoded = []
        raw = []
        for row_offset in (offset, offset + record_bytes):
            before = payload[row_offset:row_offset + free_bytes]
            after_start = row_offset + free_bytes
            after = payload[after_start:after_start + free_bytes]
            metadata = after_start + free_bytes
            generator, parameter, lane, time = struct.unpack(
                "<BBBI", payload[metadata:metadata + 7],
            )
            raw.append((before, after))
            decoded.append({
                "generator": BACKBONE[generator],
                "generator_index": generator,
                "parameter": parameter,
                "lane": lane,
                "event": EVENTS[lane // len(BACKBONE)],
                "time": time,
                "free_input_sha256": sha256(before).hexdigest(),
                "free_output_sha256": sha256(after).hexdigest(),
            })
        left_parameter = decoded[0]["parameter"]
        right_parameter = decoded[1]["parameter"]
        assert isinstance(left_parameter, int) and isinstance(right_parameter, int)
        inherited_delta = support(
            parameter_values[left_parameter] ^ parameter_values[right_parameter]
        )
        left_ones = tuple(
            wire for wire in inherited_delta
            if (parameter_values[left_parameter] >> wire) & 1
        )
        right_ones = tuple(
            wire for wire in inherited_delta
            if (parameter_values[right_parameter] >> wire) & 1
        )
        delta_packed = int.from_bytes(bytes(
            left ^ right for left, right in zip(raw[0][1], raw[1][1])
        ), "little")
        free_delta = tuple(free_wires[index] for index in support(delta_packed))
        affected.update(free_delta)
        generators.add(decoded[0]["generator_index"])
        left_x = tuple(
            (parameter_values[left_parameter] >> wire) & 1
            for wire in EXPECTED_X_CHANNEL
        )
        right_x = tuple(
            (parameter_values[right_parameter] >> wire) & 1
            for wire in EXPECTED_X_CHANNEL
        )
        x_state_pairs.add(tuple(sorted((left_x, right_x))))
        all_same_input &= raw[0][0] == raw[1][0]
        all_distinct_parameter &= left_parameter != right_parameter
        all_distinct_output &= bool(free_delta)
        channel_key = (
            decoded[0]["generator_index"], left_parameter, right_parameter,
            ranges(inherited_delta), ranges(left_ones), ranges(right_ones), free_delta,
        )
        channels[channel_key] += 1
        if first_pair is None:
            first_pair = {
                "rows": tuple(decoded),
                "inherited_difference_wire_ranges": ranges(inherited_delta),
                "x1_x6_states": (left_x, right_x),
                "free_successor_difference_wires": free_delta,
            }
    channel_rows = tuple({
        "generator": BACKBONE[key[0]],
        "parameter_pair": (key[1], key[2]),
        "inherited_difference_wire_ranges": key[3],
        "left_one_wire_ranges": key[4],
        "right_one_wire_ranges": key[5],
        "free_successor_difference_wires": key[6],
        "witness_count": count,
    } for key, count in sorted(channels.items()))
    return {
        "exact_witness_pair_count": witness_count,
        "channel_signature_count": len(channel_rows),
        "affected_free_wire_set": tuple(sorted(affected)),
        "generator_indices": tuple(sorted(generators)),
        "generator_pairs": tuple(BACKBONE[index] for index in sorted(generators)),
        "x_channel": EXPECTED_X_CHANNEL,
        "x_state_pairs": tuple(sorted(x_state_pairs)),
        "all_pairs_same_free_input": all_same_input,
        "all_pairs_distinct_parameter": all_distinct_parameter,
        "all_pairs_distinct_free_successor": all_distinct_output,
        "first_pair": first_pair,
        "channel_signatures": channel_rows,
        "witness_payload_sha256": sha256(payload).hexdigest(),
    }


def analysis_once(trees: dict[str, ast.Module]) -> dict[str, object]:
    fixture_tree = trees[AUDIT_INPUT_PATHS[1]]
    braid_tree = trees[AUDIT_INPUT_PATHS[2]]
    primary_tree = trees[AUDIT_INPUT_PATHS[0]]
    nine_predicates = literal_assignment(braid_tree, "NINE_PREDICATE_WIRES")
    pair_predicates = literal_assignment(braid_tree, "PAIR_PREDICATE_WIRES")
    mark_bits = literal_assignment(primary_tree, "K3_MARK_BITS")
    if not all(isinstance(value, tuple) for value in (
        nine_predicates, pair_predicates, mark_bits,
    )):
        raise AssertionError("landed physical wire definitions unavailable")
    fixtures = decode_literal_fixtures(fixture_tree)
    macros = fixtures["macros"]
    assert isinstance(macros, tuple)
    words = build_words(macros)
    free_certificate, free_private = reconstruct_free_sector(
        words, nine_predicates, pair_predicates, mark_bits,
    )
    compiled = compile_words(words)
    braid, probes = reconstruct_braid(
        fixtures, compiled, free_private["free_wires"], nine_predicates,
    )
    replay_surface = {
        "fixtures": fixtures["public"],
        "free_wire_sha256": free_certificate["free_wire_sha256"],
        "free_wire_count": free_certificate["free_wire_count"],
        "inherited_wire_count": free_certificate["inherited_wire_count"],
        "braid": braid,
        "probe_sha256": sha256(b"".join(
            before + after + bytes((generator,))
            for before, after, generator in probes
        )).hexdigest(),
    }
    return {
        "fixtures": fixtures,
        "words": words,
        "compiled": compiled,
        "free_certificate": free_certificate,
        "free_private": free_private,
        "braid": braid,
        "probes": probes,
        "replay_surface": replay_surface,
    }


def run() -> int:
    started = monotonic()
    controls_source, trees = source_controls()
    first = analysis_once(trees)
    second = analysis_once(trees)
    scientific_determinism = first["replay_surface"] == second["replay_surface"]
    fixtures = first["fixtures"]
    states = fixtures["states"]
    macros = fixtures["macros"]
    free_wires = first["free_private"]["free_wires"]
    inherited_wires = first["free_private"]["inherited_wires"]
    assert isinstance(states, dict) and isinstance(macros, tuple)
    assert isinstance(free_wires, tuple) and isinstance(inherited_wires, tuple)
    lanes = tuple((event, pair) for event in EVENTS for pair in BACKBONE)
    parameter_ids, parameter_values, parameter_public = inherited_parameters(
        states, lanes, inherited_wires,
    )
    inherited_mask = sum(1 << wire for wire in inherited_wires)
    compiled = first["compiled"]
    boundary_constant = all(
        not ((apply_word(states[key], compiled[pair]) ^ states[key]) & inherited_mask)
        for key in lanes for pair in BACKBONE
    )
    parameter_public["explicit_27_keys_by_9_generators_invariance"] = boundary_constant

    with tempfile.TemporaryDirectory(prefix="cycle855-independent-") as temp_name:
        temp = Path(temp_name)
        inputs = write_kernel_inputs(
            temp, macros, lanes, states, free_wires, parameter_ids, first["probes"],
        )
        compiler = compile_kernel(temp)
        kernel_first = execute_kernel(temp, "first")
        kernel_second = execute_kernel(temp, "second")

    kernel_determinism = kernel_first == kernel_second
    summary = kernel_first["summary"]
    decoded = decode_coupling_witnesses(
        kernel_first["witness"], free_wires, parameter_values,
    )

    free_certificate = first["free_certificate"]
    free_certificate["exact_generated_event_support_wires"] = (
        first["braid"]["exact_event_support_union"]
    )
    free_certificate["exact_generated_event_supports_free"] = (
        first["braid"]["all_exact_event_support_wires_free"]
    )
    free_certificate["pass"] = bool(
        free_certificate["pass"]
        and fixtures["public"]["pass"]
        and second["fixtures"]["public"]["pass"]
        and free_certificate["exact_generated_event_supports_free"]
    )

    physical = free_certificate["physical_identifications"]
    coupling_certificate = {
        "tested_relation": (
            "Across inherited parameters, group the complete 891,486-step "
            "boundary census by exact (generator, 495-bit free input), then "
            "compare every pair of exact free successors."
        ),
        "full_boundary_state_count": summary["full_reachable_states"],
        "full_boundary_step_count": summary["full_transitions"],
        "cross_key_group_count": summary["cross_key_groups"],
        "cross_key_collision_group_count": summary["cross_key_collision_groups"],
        "cross_key_distinct_parameter_groups":
            summary["cross_key_distinct_parameter_groups"],
        "free_successor_disagreement_groups": summary["coupling_groups"],
        "exact_coupling_pair_witnesses": summary["coupling_pair_witnesses"],
        "channel_signature_count": decoded["channel_signature_count"],
        "affected_free_wire_set": decoded["affected_free_wire_set"],
        "generator_coverage": decoded["generator_pairs"],
        "inherited_channel": decoded["x_channel"],
        "inherited_channel_state_exchange": EXPECTED_X_STATES,
        "observed_channel_state_pairs": decoded["x_state_pairs"],
        "physical_identifications": {
            key: physical[key]
            for key in ("wire_105", "wire_124", "wire_125", "wire_256")
        },
        "witness_validity": {
            "all_same_free_input": decoded["all_pairs_same_free_input"],
            "all_distinct_parameter": decoded["all_pairs_distinct_parameter"],
            "all_distinct_free_successor":
                decoded["all_pairs_distinct_free_successor"],
            "first_pair": decoded["first_pair"],
            "payload_sha256": decoded["witness_payload_sha256"],
        },
        "channel_signatures": decoded["channel_signatures"],
        "verdict": "CROSS_KEY_COUPLED",
        "finding": "CROSS_KEY_COUPLED_3447_WITNESSES_50_CHANNEL_SIGNATURES",
        "pass": False,
    }
    coupling_certificate["pass"] = (
        summary["full_reachable_states"] == FULL_REACHABLE_STATES
        and summary["full_transitions"] == FULL_TRANSITIONS
        and summary["coupling_pair_witnesses"] == EXPECTED_WITNESS_COUNT
        and decoded["exact_witness_pair_count"] == EXPECTED_WITNESS_COUNT
        and decoded["channel_signature_count"] == EXPECTED_CHANNEL_COUNT
        and decoded["affected_free_wire_set"] == EXPECTED_AFFECTED_FREE_WIRES
        and decoded["generator_indices"] == tuple(range(len(BACKBONE)))
        and decoded["x_state_pairs"] == (EXPECTED_X_STATES,)
        and decoded["all_pairs_same_free_input"]
        and decoded["all_pairs_distinct_parameter"]
        and decoded["all_pairs_distinct_free_successor"]
        and all(row["confirmed"] for row in physical.values())
    )

    parameter_rows = []
    for parameter, value in enumerate(parameter_values):
        lane_indices = tuple(
            index for index, identifier in enumerate(parameter_ids)
            if identifier == parameter
        )
        parameter_rows.append({
            "parameter_id": parameter,
            "inherited_projection_sha256":
                parameter_public["parameter_sha256"][parameter],
            "x1_x6": ((value >> 1) & 1, (value >> 6) & 1),
            "boundary_keys": tuple(lanes[index] for index in lane_indices),
            "reachable_free_projection_size": summary[f"parameter_size_{parameter}"],
        })
    per_key_certificate = {
        "tested_relation": (
            "For each fixed exact inherited parameter p and generator F, "
            "all reachable boundary states with the same 495-bit free input "
            "must have the same projected successor."
        ),
        "parameter_definition": (
            "The exact 5,320-bit inherited projection, independently verified "
            "constant under all nine complete generator words at every one of "
            "the 27 landed boundary keys."
        ),
        "parameters": parameter_public,
        "per_parameter_reachable_sizes": tuple(parameter_rows),
        "fixed_parameter_transition_groups": summary["parameter_step_groups"],
        "fixed_parameter_collision_groups": summary["parameter_collision_groups"],
        "fixed_parameter_successor_disagreement_groups":
            summary["parameter_disagreement_groups"],
        "fixed_parameter_successor_disagreement_pairs":
            summary["parameter_disagreement_pairs"],
        "same_boundary_key_successor_disagreement_groups":
            summary["lane_disagreement_groups"],
        "same_boundary_key_successor_disagreement_pairs":
            summary["lane_disagreement_pairs"],
        "verdict": "PER_KEY_AUTONOMOUS",
        "relationship_to_primary": (
            "REFINES_DOES_NOT_CONTRADICT_CROSS_KEY_COUPLED: the braid lives "
            "in a parameterized family of 495-wire machines; forgetting the "
            "fixed inherited parameter destroys autonomy."
        ),
        "finding": "PER_KEY_AUTONOMOUS",
        "pass": False,
    }
    per_key_certificate["pass"] = (
        boundary_constant
        and summary["parameter_count"] == len(parameter_values)
        and summary["parameter_disagreement_groups"] == 0
        and summary["parameter_disagreement_pairs"] == 0
        and summary["lane_disagreement_groups"] == 0
        and summary["lane_disagreement_pairs"] == 0
        and all(row["reachable_free_projection_size"] > 0 for row in parameter_rows)
    )

    braid_certificate = {
        "independent_braid_reconstruction": first["braid"],
        "full_census_transition_probe_count": summary["probe_count"],
        "full_census_transition_probes_reproduced": summary["probe_matches"],
        "full_census_transition_probe_mismatches": summary["probe_mismatches"],
        "event_reproduction": (
            first["braid"]["event_count"], EXPECTED_EVENT_COUNT,
        ),
        "transition_probe_reproduction": (
            summary["probe_matches"], EXPECTED_PROBE_COUNT,
        ),
        "finding": "BRAID_REPRODUCED_20_OF_20_EVENTS_86_OF_86_TRANSITION_PROBES",
        "pass": False,
    }
    braid_certificate["pass"] = (
        first["braid"]["pass"]
        and second["braid"]["pass"]
        and summary["probe_count"] == EXPECTED_PROBE_COUNT
        and summary["probe_matches"] == EXPECTED_PROBE_COUNT
        and summary["probe_mismatches"] == 0
    )

    elapsed = monotonic() - started
    blocked_at_end = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    controls_base = (
        controls_source["pass"]
        and scientific_determinism
        and kernel_determinism
        and boundary_constant
        and summary["schedule_rows"] == inputs["schedule_rows"]
        and not blocked_at_end
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls_certificate = {
        "source_controls": controls_source,
        "primary_access_policy": (
            "Cycle 855 and all other literal AUDIT_INPUT_PATHS are SHA/blob "
            "pinned, BLOCKLISTED, and consumed only as text/AST; none is "
            "imported or executed."
        ),
        "independent_reconstruction_not_primary_result_parsing": True,
        "kernel_inputs": inputs,
        "compiler": compiler,
        "determinism": {
            "scientific_replay_exact": scientific_determinism,
            "scientific_first_sha256": digest(first["replay_surface"]),
            "scientific_second_sha256": digest(second["replay_surface"]),
            "kernel_replay_exact": kernel_determinism,
            "kernel_summary": summary,
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
        "THE_FREE_SECTOR": free_certificate,
        "THE_COUPLING_WITNESSES": coupling_certificate,
        "THE_PER_KEY_REFINEMENT": per_key_certificate,
        "THE_BRAID_REPRODUCTION": braid_certificate,
        "CONTROLS": controls_certificate,
    }
    checks = {
        name: bool(certificate["pass"])
        for name, certificate in certificates.items()
    }
    checks["CONTROLS"] = False
    report = {
        "cycle": 855,
        "checker": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "primary_cross_key_verdict": "COUPLED",
        "constructive_refinement": "PER_KEY_AUTONOMOUS",
        "refutes_primary": False,
        "relationship": "REFINES_DOES_NOT_CONTRADICT",
        "free_wire_count": free_certificate["free_wire_count"],
        "witness_count": decoded["exact_witness_pair_count"],
        "channel_signature_count": decoded["channel_signature_count"],
        "checks": {},
        "runtime_seconds": round(elapsed, 6),
        "pass": False,
        "terminal": "CYCLE855_INDEPENDENT_CHECK_HONEST_FAIL",
    }

    def render() -> str:
        lines = []
        for name, certificate in certificates.items():
            lines.append(f"{name}: {'PASS' if checks[name] else 'FAIL'}")
            lines.append(f"{name}_FINDING={certificate['finding']}")
            lines.append(f"{name}_CERTIFICATE={compact(certificate)}")
        lines.append(f"REPORT={compact(report)}")
        return "\n".join(lines) + "\n"

    for _ in range(12):
        controls_certificate["pass"] = controls_base
        controls_certificate["finding"] = (
            "CONTROLS_PASS" if controls_certificate["pass"] else "CONTROLS_FAIL"
        )
        checks["CONTROLS"] = controls_certificate["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE855_INDEPENDENT_CHECK_PASS"
            if report["pass"] else "CYCLE855_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = render()
        stdout_bytes = len(output.encode("utf-8"))
        controls_certificate["stdout_bytes"] = stdout_bytes
        controls_certificate["stdout_below_limit"] = stdout_bytes < STDOUT_LIMIT_BYTES
        controls_base = controls_base and stdout_bytes < STDOUT_LIMIT_BYTES
    output = render()
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 855,
            "pass": False,
            "terminal": "CYCLE855_INDEPENDENT_STDOUT_LIMIT_EXCEEDED",
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
                "terminal": "CYCLE855_INDEPENDENT_CHECK_HONEST_FAIL",
                "exception_type": type(error).__name__,
                "exception": str(error),
            }))
            return 1
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: frontier_cycle855_reduction_independent_check_2026_07_28.py"
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
            "terminal": "CYCLE855_INDEPENDENT_TIMEOUT",
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        }))
        return 1
    stdout_bytes = len(completed.stdout.encode("utf-8"))
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 855,
            "pass": False,
            "terminal": "CYCLE855_INDEPENDENT_STDOUT_LIMIT_EXCEEDED",
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
