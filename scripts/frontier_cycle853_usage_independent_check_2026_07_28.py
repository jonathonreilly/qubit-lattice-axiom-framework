#!/usr/bin/env python3
"""Cycle 853 independent adversarial check: the two dead wires.

The Cycle-853 primary is a blocked source under attack.  The checker obtains
the rule payload from the earlier Cycle-830 fixture and the counterexample
search definition from Cycle 851 v2, both by text/AST extraction only.  Its
reachable-state census is a separate pair-major bit-sliced implementation.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle853_generator_usage_census_2026_07_28.py",
    "scripts/frontier_cycle851_sstar_prime_exclusion_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
)

import ast
import base64
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import re
import struct
import subprocess
import sys
import tempfile
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "946a2ffcbb3ddad19ff2213831593f7ea93a97d9a680fec50a674391592863b7",
    AUDIT_INPUT_PATHS[1]:
        "2d5796c01613ca3b5deec05e7e86c6fe7240ba7dd87f704c90579f21d0cc45c8",
    AUDIT_INPUT_PATHS[2]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "b28e895ffa847973a5a8ae594d3eb7796b0bc018",
    AUDIT_INPUT_PATHS[1]: "471b1d688cf96d9be26b5c49087a147c896e8994",
    AUDIT_INPUT_PATHS[2]: "98b1571228ad0902301b6853208ef249ea2c2973",
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
EVENTS = (0, 2, 1)
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
RESOLUTION_MOMENTS = {0: 14744, 2: 33195, 1: 51115}
EXPECTED_REACHABLE_STATES = 891513
EXPECTED_TRANSITIONS = 891486
EXPECTED_PATTERN_WITNESSES = (
    ((110, 111), (3, 8), 2, 0, 56),
    ((110, 112), (1, 6), 3, 2, 56),
    ((110, 113), (3, 8), 2, 0, 56),
    ((110, 114), (2, 7), 3, 1, 58),
)


class _SourceFirewall(importlib.abc.MetaPathFinder):
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


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def state_sha256(state: int) -> str:
    return sha256(bytes((state >> wire) & 1 for wire in range(STATE_BITS))).hexdigest()


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


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("function cardinality", name, len(rows)))
    return rows[0]


def literal_range_calls(node: ast.AST) -> tuple[tuple[int, ...], ...]:
    rows = []
    for candidate in ast.walk(node):
        if (
            isinstance(candidate, ast.Call)
            and isinstance(candidate.func, ast.Name)
            and candidate.func.id == "range"
        ):
            try:
                values = tuple(ast.literal_eval(arg) for arg in candidate.args)
            except (TypeError, ValueError):
                continue
            if all(isinstance(value, int) for value in values):
                rows.append(values)
    return tuple(rows)


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {path: ast.parse(payload, filename=path) for path, payload in payloads.items()}
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    primary_functions = {
        node.name for node in trees[AUDIT_INPUT_PATHS[0]].body
        if isinstance(node, ast.FunctionDef)
    }
    cycle851_functions = {
        node.name for node in trees[AUDIT_INPUT_PATHS[1]].body
        if isinstance(node, ast.FunctionDef)
    }
    cycle830_functions = {
        node.name for node in trees[AUDIT_INPUT_PATHS[2]].body
        if isinstance(node, ast.FunctionDef)
    }
    actual_sha = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    actual_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    ast_basis = {
        "blocked_cycle853_primary": {
            "extract_patterns", "localization_census", "run",
        } <= primary_functions,
        "cycle851_counterexample_definition": {
            "universal_composed_parity_attempt", "local_invariant_hunt",
        } <= cycle851_functions,
        "cycle830_fixture_schema": {
            "decode_fixtures", "build_words", "apply_word",
        } <= cycle830_functions,
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
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
        "source_primary": AUDIT_INPUT_PATHS[0],
        "text_AST_only": AUDIT_INPUT_PATHS,
        "direct_frontier_imports": tuple(sorted(
            name for name in imports if name.startswith("frontier_cycle")
        )),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_AUDIT_INPUT_PATHS"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(ast_basis.values())
        and not result["direct_frontier_imports"]
        and not FIREWALL.hits
    )
    return result, trees


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


def decode_fixture(tree: ast.Module) -> dict[str, object]:
    gate_encoded = literal_assignment(tree, "GATE_CONSTANTS_B85")
    family_encoded = literal_assignment(tree, "FAMILY_STATES_B85")
    if not isinstance(gate_encoded, str) or not isinstance(family_encoded, str):
        raise AssertionError("literal Cycle-830 fixture payload absent")
    gate_raw = zlib.decompress(base64.b85decode(gate_encoded))
    family_raw = zlib.decompress(base64.b85decode(family_encoded))
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros = []
    for length in lengths:
        macro = []
        for _index in range(length):
            macro.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(macro))
    keys = tuple(sorted(
        (event, pair)
        for event in range(2 * FIXTURE_BANKS)
        for pair in separated_pairs()
    ))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(family_raw[start:start + STATE_BYTES], "little")
    public = {
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "macro_gate_counts": lengths,
        "macro_gates": sum(lengths),
        "separated_pairs": len(separated_pairs()),
        "family_states": len(states),
    }
    public["pass"] = (
        offset == len(gate_raw)
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and sum(lengths) == 3106
        and len(separated_pairs()) == 44
        and len(states) == FAMILY_SIZE
    )
    return {"macros": tuple(macros), "states": states, "public": public}


def extract_cycle851_definition(tree: ast.Module) -> dict[str, object]:
    """Extract the counterexample family and search order from Cycle 851."""
    universal = function_node(tree, "universal_composed_parity_attempt")
    local_hunt = function_node(tree, "local_invariant_hunt")
    universal_ranges = literal_range_calls(universal)
    local_ranges = literal_range_calls(local_hunt)
    kernel = literal_assignment(tree, "KERNEL_C")
    if not isinstance(kernel, str):
        raise AssertionError("Cycle-851 literal kernel missing")
    invariant_loop = re.search(
        r"for \(int invariant = 0; invariant < ([0-9]+); \+\+invariant\)",
        kernel,
    )
    parity_expression = re.search(
        r"columns\[([0-9]+)\] \^ columns\[([0-9]+) \+ invariant\]",
        kernel,
    )
    if invariant_loop is None or parity_expression is None:
        raise AssertionError("Cycle-851 affine kernel definition not uniquely recognized")
    count = int(invariant_loop.group(1))
    first = int(parity_expression.group(1))
    second_base = int(parity_expression.group(2))
    head_indices = tuple(range(2, 6))
    wires = tuple((first, second_base + offset) for offset in range(count))
    candidates = tuple(
        f"BANK0_HEAD1_XOR_HEAD{index}" for index in head_indices
    )
    extracted = {
        "HEAD1_WIRE": literal_assignment(tree, "HEAD1_WIRE"),
        "STATE_BITS": literal_assignment(tree, "STATE_BITS"),
        "BACKBONE": literal_assignment(tree, "BACKBONE"),
        "RESOLUTION_MOMENTS": literal_assignment(tree, "RESOLUTION_MOMENTS"),
        "candidate_index_range": (2, 6),
        "counterexample_modulus_range": (2, 17),
        "kernel_invariant_count": count,
        "kernel_parity_template": (first, second_base, "invariant"),
        "candidates": candidates,
        "wires": wires,
        "AST_evidence": {
            "range_2_6_in_local_invariant_hunt": (2, 6) in local_ranges,
            "range_2_17_in_universal_attempt": (2, 17) in universal_ranges,
            "kernel_uses_four_invariants": count == 4,
            "kernel_uses_110_xor_111_plus_invariant":
                (first, second_base) == (110, 111),
        },
    }
    extracted["pass"] = (
        extracted["HEAD1_WIRE"] == 110
        and extracted["STATE_BITS"] == STATE_BITS
        and extracted["BACKBONE"] == BACKBONE
        and extracted["RESOLUTION_MOMENTS"] == RESOLUTION_MOMENTS
        and head_indices == (2, 3, 4, 5)
        and wires == tuple(row[0] for row in EXPECTED_PATTERN_WITNESSES)
        and all(extracted["AST_evidence"].values())
    )
    return extracted


def build_word(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    pair: tuple[int, int],
) -> tuple[tuple[int, int, int, int], ...]:
    word = []
    for step in range(RING_STATIONS):
        active_stations = {
            (pair[0] + step) % RING_STATIONS,
            (pair[1] + step) % RING_STATIONS,
        }
        for station in sorted(active_stations):
            word.extend(macros[station])
    return tuple(word)


def apply_word(state: int, word: tuple[tuple[int, int, int, int], ...]) -> int:
    for kind, first, second, third in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        elif kind == 2:
            state ^= (
                ((state >> first) & 1) & ((state >> second) & 1)
            ) << third
        else:
            raise AssertionError(("unknown gate kind", kind))
    return state


def parity(state: int, wires: tuple[int, int]) -> int:
    return ((state >> wires[0]) ^ (state >> wires[1])) & 1


def gate_target(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    return first if kind == 0 else second if kind == 1 else third


def backward_support(
    wires: tuple[int, int],
    word: tuple[tuple[int, int, int, int], ...],
) -> tuple[int, ...]:
    support = set(wires)
    for kind, first, second, third in reversed(word):
        target = first if kind == 0 else second if kind == 1 else third
        if target not in support:
            continue
        if kind == 1:
            support.add(first)
        elif kind == 2:
            support.update((first, second))
    return tuple(sorted(support))


def derive_patterns(
    definition: dict[str, object],
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> tuple[dict[str, object], ...]:
    modulus_range = definition["counterexample_modulus_range"]
    wires_family = definition["wires"]
    candidates = definition["candidates"]
    assert isinstance(modulus_range, tuple)
    assert isinstance(wires_family, tuple) and isinstance(candidates, tuple)
    patterns = []
    for pattern_index, (candidate, wires) in enumerate(
        zip(candidates, wires_family), start=1,
    ):
        found = None
        for modulus in range(*modulus_range):
            for residue in range(modulus):
                before = sum(
                    1 << wire for wire in range(residue, STATE_BITS, modulus)
                )
                for pair in BACKBONE:
                    after = apply_word(before, words[pair])
                    if parity(before, wires) != parity(after, wires):
                        found = {
                            "generator_pair": pair,
                            "modulus": modulus,
                            "residue": residue,
                            "before_parity": parity(before, wires),
                            "after_parity": parity(after, wires),
                            "input_weight": before.bit_count(),
                            "input_state_sha256": state_sha256(before),
                            "output_state_sha256": state_sha256(after),
                        }
                        break
                if found is not None:
                    break
            if found is not None:
                break
        if found is None:
            raise AssertionError(("counterexample not found", candidate))
        pair = found["generator_pair"]
        assert isinstance(pair, tuple)
        support = backward_support(wires, words[pair])
        modulus = int(found["modulus"])
        residue = int(found["residue"])
        expected_values = tuple(
            int(wire % modulus == residue) for wire in support
        )
        required_wire = EXPECTED_PATTERN_WITNESSES[pattern_index - 1][4]
        required_index = support.index(required_wire) if required_wire in support else -1
        required_value = (
            expected_values[required_index] if required_index >= 0 else None
        )
        local_state = sum(
            value << wire for wire, value in zip(support, expected_values)
        )
        exterior_mask = ((1 << STATE_BITS) - 1) ^ sum(
            1 << wire for wire in support
        )
        locality_deltas = tuple(
            parity(state, wires) ^ parity(apply_word(state, words[pair]), wires)
            for state in (local_state, local_state ^ exterior_mask)
        )
        patterns.append({
            "pattern_id": f"P{pattern_index}",
            "candidate": candidate,
            "parity_wires": wires,
            "generator_pair": pair,
            "ordered_primitive_count": len(words[pair]),
            "counterexample": found,
            "support": support,
            "expected_values": expected_values,
            "support_wire_count": len(support),
            "support_sha256": sha256(
                struct.pack(f"<{len(support)}H", *support)
            ).hexdigest(),
            "precondition_definition":
                f"for every w in support, x[w]=1 iff w mod {modulus} == {residue}",
            "required_dead_wire": {
                "wire": required_wire,
                "is_in_backward_support": required_index >= 0,
                "required_value": required_value,
                "by_definition_check":
                    required_value == int(required_wire % modulus == residue) == 1,
            },
            "exterior_zero_and_one_deltas": locality_deltas,
            "locality_verified": locality_deltas == (1, 1),
        })
    actual_witnesses = tuple(
        (
            pattern["parity_wires"],
            pattern["generator_pair"],
            pattern["counterexample"]["modulus"],
            pattern["counterexample"]["residue"],
            pattern["required_dead_wire"]["wire"],
        )
        for pattern in patterns
    )
    if actual_witnesses != EXPECTED_PATTERN_WITNESSES:
        raise AssertionError(("counterexample family drift", actual_witnesses))
    return tuple(patterns)


def recursion_probe(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
    states: dict[tuple[int, tuple[int, int]], int],
) -> dict[str, object]:
    per_wire = []
    for wire in (56, 58):
        primitive_targets = tuple(
            {
                "station": station,
                "macro_gate_index": gate_index,
                "gate": row,
                "precondition": "none (unconditional X toggle)" if row[0] == 0 else None,
            }
            for station, macro in enumerate(macros)
            for gate_index, row in enumerate(macro)
            if gate_target(row) == wire
        )
        primitive_controls = tuple(
            {
                "station": station,
                "macro_gate_index": gate_index,
                "gate": row,
            }
            for station, macro in enumerate(macros)
            for gate_index, row in enumerate(macro)
            if wire in (() if row[0] == 0 else (row[1],) if row[0] == 1 else (row[1], row[2]))
        )
        generator_rows = []
        for pair in BACKBONE:
            targets = tuple(row for row in words[pair] if gate_target(row) == wire)
            target_x_count = sum(row[0] == 0 for row in targets)
            relation_closed = len(targets) == target_x_count == 4
            generator_rows.append({
                "generator_pair": pair,
                "target_gate_count": len(targets),
                "unconditional_X_toggles": target_x_count,
                "generator_boundary_relation": "x'[w]=x[w]" if relation_closed else "OPEN",
                "can_set_0_to_1_at_generator_boundary": not relation_closed,
                "primitive_0_to_1_microsteps_if_entering_with_0":
                    target_x_count // 2 if relation_closed else None,
            })
        selected_initial_ones = sum(
            (states[(event, pair)] >> wire) & 1
            for pair in BACKBONE for event in EVENTS
        )
        all_fixture_initial_ones = sum(
            (state >> wire) & 1 for state in states.values()
        )
        per_wire.append({
            "wire": wire,
            "primitive_target_gates": primitive_targets,
            "primitive_control_uses": primitive_controls,
            "primitive_scope_warning": (
                "Unconditional X gates temporarily light this wire inside F_pair; "
                "primitive microstates are not landed reachable states."
            ),
            "generators": tuple(generator_rows),
            "selected_27_initial_ones": selected_initial_ones,
            "all_176_fixture_initial_ones": all_fixture_initial_ones,
            "closure": (
                selected_initial_ones == 0
                and all_fixture_initial_ones == 0
                and len(primitive_targets) == 2
                and all(row["gate"][0] == 0 for row in primitive_targets)
                and all(
                    not row["can_set_0_to_1_at_generator_boundary"]
                    for row in generator_rows
                )
            ),
        })
    closed = all(row["closure"] for row in per_wire)
    return {
        "shape": "GROUNDING_BY_INITIAL_ZEROS_AND_EXACT_COMPOSITE_CANCELLATION",
        "mutual_dependence": False,
        "dependence_on_other_dead_structure": False,
        "initial_condition": "x[56]=x[58]=0 on all 176 decoded t=0 fixtures",
        "landed_rule_theorem": (
            "For each of the nine F_pair generators and w in {56,58}, the only "
            "targeting primitives are four unconditional X toggles, hence "
            "F_pair(x)[w]=x[w] for every 5815-bit x."
        ),
        "primitive_resolution_boundary": (
            "Each F_pair has two temporary 0->1 primitive microsteps per wire; "
            "the dead-wire theorem is exactly about complete-generator landed states."
        ),
        "new_unreachable_requirements": (),
        "per_wire": tuple(per_wire),
        "recursion_closes": closed,
        "finding": "RECURSION_CLOSES_AT_COMPLETE_GENERATOR_BOUNDARIES" if closed else "RECURSION_OPENS",
        "pass": closed,
    }


def build_pair_major_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    """Build a pair-major bit-sliced schedule independently of Cycle 853."""
    schedule = []
    for step in range(RING_STATIONS):
        for station, macro in enumerate(macros):
            lane_mask = sum(
                1 << lane
                for lane, (_event, pair) in enumerate(lanes)
                if station in {
                    (pair[0] + step) % RING_STATIONS,
                    (pair[1] + step) % RING_STATIONS,
                }
            )
            if lane_mask:
                schedule.extend((*row, lane_mask) for row in macro)
    return tuple(schedule)


def write_kernel_inputs(
    directory: Path,
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    states: dict[tuple[int, tuple[int, int]], int],
    patterns: tuple[dict[str, object], ...],
) -> dict[str, object]:
    schedule = build_pair_major_schedule(macros, lanes)
    schedule_payload = b"".join(struct.pack("<BHHHQ", *row) for row in schedule)
    (directory / "schedule.bin").write_bytes(schedule_payload)
    columns = tuple(
        sum(((states[key] >> wire) & 1) << lane for lane, key in enumerate(lanes))
        for wire in range(STATE_BITS)
    )
    columns_payload = struct.pack("<5815Q", *columns)
    (directory / "columns.bin").write_bytes(columns_payload)
    pattern_payload = bytearray()
    for pattern in patterns:
        pair = pattern["generator_pair"]
        support = pattern["support"]
        values = pattern["expected_values"]
        parity_wires = pattern["parity_wires"]
        assert isinstance(pair, tuple) and isinstance(support, tuple)
        assert isinstance(values, tuple) and isinstance(parity_wires, tuple)
        eligible_lanes = sum(
            1 << lane for lane, (_event, lane_pair) in enumerate(lanes)
            if lane_pair == pair
        )
        pattern_payload.extend(struct.pack(
            "<QHHH", eligible_lanes, parity_wires[0], parity_wires[1], len(support)
        ))
        for wire, value in zip(support, values):
            pattern_payload.extend(struct.pack("<HB", wire, value))
    (directory / "patterns.bin").write_bytes(pattern_payload)
    return {
        "lane_order": lanes,
        "schedule_rows": len(schedule),
        "schedule_sha256": sha256(schedule_payload).hexdigest(),
        "initial_columns_sha256": sha256(columns_payload).hexdigest(),
        "patterns_sha256": sha256(pattern_payload).hexdigest(),
    }


KERNEL_C = r'''#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define STATE_BITS 5815
#define LANES 27
#define PATTERNS 4
#define MAX_SUPPORT 5815
#define MAX_TIME 51115

typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c; uint64_t lane_mask;
} ScheduledGate;
typedef struct __attribute__((packed)) {
    uint64_t lane_mask; uint16_t parity_a, parity_b, support_n;
} PatternHeader;
typedef struct __attribute__((packed)) { uint16_t wire; uint8_t expected; } Cell;

static void die(const char *message) { perror(message); exit(2); }
static void *load_exact(const char *path, size_t item_size, size_t *count) {
    FILE *f = fopen(path, "rb"); if (!f) die(path);
    if (fseek(f, 0, SEEK_END)) die("fseek");
    long bytes = ftell(f); if (bytes < 0 || bytes % (long)item_size) die("size");
    rewind(f); void *payload = malloc((size_t)bytes); if (!payload) die("malloc");
    if (fread(payload, 1, (size_t)bytes, f) != (size_t)bytes) die("fread");
    fclose(f); *count = (size_t)bytes / item_size; return payload;
}
static uint64_t active_state(int time) {
    uint64_t mask = 0;
    for (int pair = 0; pair < 9; ++pair) {
        if (time <= 14744) mask |= UINT64_C(1) << (3 * pair);
        if (time <= 33195) mask |= UINT64_C(1) << (3 * pair + 1);
        if (time <= 51115) mask |= UINT64_C(1) << (3 * pair + 2);
    }
    return mask;
}
static uint64_t active_transition(int time) {
    uint64_t mask = 0;
    for (int pair = 0; pair < 9; ++pair) {
        if (time < 14744) mask |= UINT64_C(1) << (3 * pair);
        if (time < 33195) mask |= UINT64_C(1) << (3 * pair + 1);
        if (time < 51115) mask |= UINT64_C(1) << (3 * pair + 2);
    }
    return mask;
}
int main(int argc, char **argv) {
    if (argc != 6) { fprintf(stderr, "argc\n"); return 2; }
    size_t schedule_n, column_n;
    ScheduledGate *schedule = load_exact(argv[1], sizeof(ScheduledGate), &schedule_n);
    uint64_t *initial = load_exact(argv[2], sizeof(uint64_t), &column_n);
    if (column_n != STATE_BITS) return 3;
    FILE *pattern_file = fopen(argv[3], "rb"); if (!pattern_file) die(argv[3]);
    PatternHeader headers[PATTERNS]; Cell cells[PATTERNS][MAX_SUPPORT];
    memset(cells, 0, sizeof(cells));
    for (int pattern = 0; pattern < PATTERNS; ++pattern) {
        if (fread(&headers[pattern], sizeof(PatternHeader), 1, pattern_file) != 1)
            die("pattern header");
        if (headers[pattern].support_n > MAX_SUPPORT) return 4;
        if (fread(cells[pattern], sizeof(Cell), headers[pattern].support_n, pattern_file)
                != headers[pattern].support_n) die("pattern cells");
    }
    if (fgetc(pattern_file) != EOF) return 5; fclose(pattern_file);

    uint64_t columns[STATE_BITS]; memcpy(columns, initial, sizeof(columns));
    uint64_t states = 0, transitions = 0, wire56_ones = 0, wire58_ones = 0;
    uint64_t applications[PATTERNS] = {0}, usages[PATTERNS] = {0};
    uint64_t eligible_flips[PATTERNS] = {0}, all_flips[PATTERNS] = {0};
    int first56_time = -1, first56_lane = -1, first58_time = -1, first58_lane = -1;
    for (int time = 0; time <= MAX_TIME; ++time) {
        uint64_t state_mask = active_state(time);
        states += (uint64_t)__builtin_popcountll(state_mask);
        uint64_t lit56 = columns[56] & state_mask;
        uint64_t lit58 = columns[58] & state_mask;
        wire56_ones += (uint64_t)__builtin_popcountll(lit56);
        wire58_ones += (uint64_t)__builtin_popcountll(lit58);
        if (lit56 && first56_time < 0) {
            first56_time = time; first56_lane = __builtin_ctzll(lit56);
        }
        if (lit58 && first58_time < 0) {
            first58_time = time; first58_lane = __builtin_ctzll(lit58);
        }
        if (time == MAX_TIME) break;
        uint64_t transition_mask = active_transition(time);
        transitions += (uint64_t)__builtin_popcountll(transition_mask);
        uint64_t before[PATTERNS], eligible[PATTERNS];
        for (int pattern = 0; pattern < PATTERNS; ++pattern) {
            eligible[pattern] = transition_mask & headers[pattern].lane_mask;
            applications[pattern] += (uint64_t)__builtin_popcountll(eligible[pattern]);
            uint64_t match = eligible[pattern];
            for (uint16_t index = 0; index < headers[pattern].support_n; ++index) {
                uint64_t column = columns[cells[pattern][index].wire];
                match &= cells[pattern][index].expected ? column : ~column;
            }
            usages[pattern] += (uint64_t)__builtin_popcountll(match);
            before[pattern] =
                columns[headers[pattern].parity_a] ^ columns[headers[pattern].parity_b];
        }
        for (size_t index = 0; index < schedule_n; ++index) {
            ScheduledGate gate = schedule[index];
            uint64_t mask = gate.lane_mask & transition_mask;
            if (gate.kind == 0) columns[gate.a] ^= mask;
            else if (gate.kind == 1) columns[gate.b] ^= columns[gate.a] & mask;
            else if (gate.kind == 2)
                columns[gate.c] ^= columns[gate.a] & columns[gate.b] & mask;
            else return 6;
        }
        for (int pattern = 0; pattern < PATTERNS; ++pattern) {
            uint64_t after =
                columns[headers[pattern].parity_a] ^ columns[headers[pattern].parity_b];
            uint64_t changed = before[pattern] ^ after;
            eligible_flips[pattern] +=
                (uint64_t)__builtin_popcountll(changed & eligible[pattern]);
            all_flips[pattern] +=
                (uint64_t)__builtin_popcountll(changed & transition_mask);
        }
    }
    FILE *final_file = fopen(argv[4], "wb"); if (!final_file) die(argv[4]);
    if (fwrite(columns, sizeof(uint64_t), STATE_BITS, final_file) != STATE_BITS)
        die("final columns");
    fclose(final_file);
    FILE *summary = fopen(argv[5], "w"); if (!summary) die(argv[5]);
    fprintf(summary,
        "schedule_rows=%zu\nreachable_states=%" PRIu64 "\ntransitions=%" PRIu64
        "\nwire56_ones=%" PRIu64 "\nwire58_ones=%" PRIu64
        "\nfirst56_time=%d\nfirst56_lane=%d\nfirst58_time=%d\nfirst58_lane=%d\n",
        schedule_n, states, transitions, wire56_ones, wire58_ones,
        first56_time, first56_lane, first58_time, first58_lane);
    for (int pattern = 0; pattern < PATTERNS; ++pattern)
        fprintf(summary,
            "pattern_%d_applications=%" PRIu64 "\npattern_%d_usages=%" PRIu64
            "\npattern_%d_eligible_flips=%" PRIu64 "\npattern_%d_all_flips=%" PRIu64 "\n",
            pattern, applications[pattern], pattern, usages[pattern],
            pattern, eligible_flips[pattern], pattern, all_flips[pattern]);
    fclose(summary); free(schedule); free(initial); return 0;
}
'''


def compile_kernel(directory: Path) -> dict[str, object]:
    source = directory / "independent_kernel.c"
    binary = directory / "independent_kernel"
    source.write_text(KERNEL_C, encoding="utf-8")
    completed = subprocess.run(
        ("cc", "-O3", "-std=c11", str(source), "-o", str(binary)),
        cwd=ROOT, check=True, capture_output=True, text=True, timeout=60,
    )
    compiler = subprocess.run(
        ("cc", "--version"), check=True, capture_output=True, text=True, timeout=20,
    ).stdout.splitlines()[0]
    return {
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "binary_sha256": sha256(binary.read_bytes()).hexdigest(),
        "compiler": compiler,
        "compiler_stdout": completed.stdout,
        "compiler_stderr": completed.stderr,
    }


def execute_kernel(directory: Path, label: str) -> dict[str, object]:
    final_path = directory / f"final_{label}.bin"
    summary_path = directory / f"summary_{label}.txt"
    completed = subprocess.run(
        (
            str(directory / "independent_kernel"),
            str(directory / "schedule.bin"),
            str(directory / "columns.bin"),
            str(directory / "patterns.bin"),
            str(final_path), str(summary_path),
        ),
        cwd=ROOT, check=True, capture_output=True, text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    summary = {}
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        key, value = line.split("=", 1)
        summary[key] = int(value)
    final = final_path.read_bytes()
    return {
        "summary": summary,
        "summary_bytes": summary_path.read_bytes(),
        "final_columns": final,
        "final_columns_sha256": sha256(final).hexdigest(),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def public_pattern(pattern: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in pattern.items()
        if key not in {"support", "expected_values"}
    }


def first_lit_witness(
    summary: dict[str, int], wire: int,
    lanes: tuple[tuple[int, tuple[int, int]], ...],
) -> dict[str, object] | None:
    time = summary[f"first{wire}_time"]
    lane = summary[f"first{wire}_lane"]
    if time < 0 or lane < 0:
        return None
    event, pair = lanes[lane]
    return {"wire": wire, "time": time, "lane": lane, "event": event, "pair": pair}


def run() -> int:
    started = monotonic()
    sources, trees = source_controls()
    definition = extract_cycle851_definition(trees[AUDIT_INPUT_PATHS[1]])
    fixture = decode_fixture(trees[AUDIT_INPUT_PATHS[2]])
    macros = fixture["macros"]
    states = fixture["states"]
    assert isinstance(macros, tuple) and isinstance(states, dict)
    words = {pair: build_word(macros, pair) for pair in BACKBONE}
    patterns = derive_patterns(definition, words)
    recursion = recursion_probe(macros, words, states)
    lanes = tuple((event, pair) for pair in BACKBONE for event in EVENTS)

    with tempfile.TemporaryDirectory(prefix="cycle853-independent-") as temp_name:
        temp = Path(temp_name)
        kernel_inputs = write_kernel_inputs(temp, macros, lanes, states, patterns)
        compiler = compile_kernel(temp)
        replay_first = execute_kernel(temp, "first")
        replay_second = execute_kernel(temp, "second")

    deterministic = replay_first == replay_second
    summary = replay_first["summary"]
    expected_applications = sum(RESOLUTION_MOMENTS.values())

    certificate_patterns = {
        "source": AUDIT_INPUT_PATHS[1],
        "independent_extraction": (
            "Parse the Cycle-851 AST and literal C kernel to recover the four "
            "HEAD parity definitions and the modulus/residue search order; decode "
            "Cycle-830 gates independently and replay that ordered search."
        ),
        "source_definition": definition,
        "patterns": tuple(public_pattern(pattern) for pattern in patterns),
        "pattern_count": len(patterns),
        "required_dead_wires": tuple(
            pattern["required_dead_wire"] for pattern in patterns
        ),
        "finding": (
            "FOUR_VIOLATING_PATTERNS_REDERIVED_P1_P2_P3_REQUIRE_X56_1_"
            "P4_REQUIRES_X58_1_BY_DEFINITION"
        ),
    }
    certificate_patterns["pass"] = (
        definition["pass"]
        and len(patterns) == 4
        and tuple(
            pattern["required_dead_wire"]["wire"] for pattern in patterns
        ) == (56, 56, 56, 58)
        and all(
            pattern["required_dead_wire"]["by_definition_check"]
            and pattern["locality_verified"]
            and pattern["ordered_primitive_count"] == 6212
            for pattern in patterns
        )
    )

    usage_rows = tuple({
        "pattern_id": pattern["pattern_id"],
        "generator_pair": pattern["generator_pair"],
        "eligible_applications": summary[f"pattern_{index}_applications"],
        "usage_count": summary[f"pattern_{index}_usages"],
        "eligible_generator_parity_flips":
            summary[f"pattern_{index}_eligible_flips"],
        "all_nine_generator_parity_flips":
            summary[f"pattern_{index}_all_flips"],
    } for index, pattern in enumerate(patterns))
    wire56_ones = summary["wire56_ones"]
    wire58_ones = summary["wire58_ones"]
    reversal = wire56_ones > 0 or wire58_ones > 0
    certificate_dead_wires = {
        "state_computation": (
            "Independent pair-major 27-lane bit slicing: decode all t=0 states "
            "from Cycle 830, construct the complete ordered F_pair schedule, and "
            "census every complete-generator state and transition."
        ),
        "lane_order": lanes,
        "complete_reachable_state_count": summary["reachable_states"],
        "expected_reachable_state_count": EXPECTED_REACHABLE_STATES,
        "complete_transition_count": summary["transitions"],
        "expected_transition_count": EXPECTED_TRANSITIONS,
        "x56_one_occurrences_in_reachable_states": wire56_ones,
        "x58_one_occurrences_in_reachable_states": wire58_ones,
        "first_x56_one_witness": first_lit_witness(summary, 56, lanes),
        "first_x58_one_witness": first_lit_witness(summary, 58, lanes),
        "pattern_usage": usage_rows,
        "reversal": reversal,
        "finding": (
            "PRIMARY_REFUTED_REACHABLE_STATE_LIGHTS_WIRE56_OR_WIRE58"
            if reversal
            else "891513_REACHABLE_STATES_KEEP_X56_X58_ZERO_AND_FOUR_USAGE_COUNTS_ARE_ZERO"
        ),
    }
    certificate_dead_wires["pass"] = (
        not reversal
        and summary["reachable_states"] == EXPECTED_REACHABLE_STATES
        and summary["transitions"] == EXPECTED_TRANSITIONS
        and all(
            row["eligible_applications"] == expected_applications
            and row["usage_count"] == 0
            and row["all_nine_generator_parity_flips"] == 0
            for row in usage_rows
        )
    )

    certificate_recursion = recursion
    elapsed = monotonic() - started
    replay_control = {
        "exact_replay": deterministic,
        "summary_exact":
            replay_first["summary_bytes"] == replay_second["summary_bytes"],
        "first_summary": summary,
        "second_summary": replay_second["summary"],
        "final_columns_exact":
            replay_first["final_columns"] == replay_second["final_columns"],
        "final_columns_sha256": replay_first["final_columns_sha256"],
        "kernel_stdout": replay_first["stdout"],
        "kernel_stderr": replay_first["stderr"],
    }
    controls = {
        **sources,
        "fixture_reconstruction": fixture["public"],
        "cycle851_definition_extraction_pass": definition["pass"],
        "kernel_inputs": kernel_inputs,
        "compiled_kernel": compiler,
        "determinism": replay_control,
        "blocked_modules_loaded_at_end": tuple(
            module for module in BLOCKLISTED_MODULES if module in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "finding": "CONTROLS_FAIL",
        "pass": False,
    }
    controls_base = (
        sources["pass"]
        and fixture["public"]["pass"]
        and definition["pass"]
        and deterministic
        and replay_control["summary_exact"]
        and replay_control["final_columns_exact"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    certificates = {
        "THE_PATTERNS": certificate_patterns,
        "THE_DEAD_WIRES": certificate_dead_wires,
        "THE_RECURSION_PROBE": certificate_recursion,
        "CONTROLS": controls,
    }
    checks = {
        "THE_PATTERNS": bool(certificate_patterns["pass"]),
        "THE_DEAD_WIRES": bool(certificate_dead_wires["pass"]),
        "THE_RECURSION_PROBE": bool(certificate_recursion["pass"]),
        "CONTROLS": False,
    }
    report = {
        "cycle": 853,
        "target": "independent adversarial check of the two dead wires",
        "verdict": (
            "PRIMARY_REFUTED" if reversal
            else "USAGE_LOCALIZED_INDEPENDENTLY_CONFIRMED"
        ),
        "checks": {},
        "pass": False,
        "terminal": "CYCLE853_USAGE_INDEPENDENT_CHECK_HONEST_FAIL",
    }

    def render() -> str:
        lines = []
        for name, certificate in certificates.items():
            lines.append(f"{name}: {'PASS' if checks[name] else 'FAIL'}")
            lines.append(f"{name}_FINDING={certificate['finding']}")
            lines.append(f"{name}_CERTIFICATE={compact(certificate)}")
        lines.append(f"REPORT={compact(report)}")
        return "\n".join(lines) + "\n"

    for _iteration in range(10):
        controls["pass"] = controls_base
        controls["finding"] = "CONTROLS_PASS" if controls["pass"] else "CONTROLS_FAIL"
        checks["CONTROLS"] = bool(controls["pass"])
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE853_USAGE_INDEPENDENT_CHECK_PASS"
            if report["pass"] else "CYCLE853_USAGE_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = render()
        controls["stdout_bytes"] = len(output.encode("utf-8"))
        controls["pass"] = controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
    output = render()
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        print(compact({
            "pass": False,
            "terminal": "CYCLE853_USAGE_INDEPENDENT_CHECK_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
        }))
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        print(compact({
            "pass": False,
            "terminal": "CYCLE853_USAGE_INDEPENDENT_CHECK_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
