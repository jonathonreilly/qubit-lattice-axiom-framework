#!/usr/bin/env python3
"""Cycle 853: exhaustive generator-usage census for the Cycle-851 parities.

The Cycle-851 v2 primary and its fixture source are SHA-pinned, parsed only as
text/AST, and blocked from import.  This runner reconstructs the exact landed
X/CNOT/Toffoli generators and the 27 family trajectories independently.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
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
import struct
import subprocess
import sys
import tempfile
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR26-20260729"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "2d5796c01613ca3b5deec05e7e86c6fe7240ba7dd87f704c90579f21d0cc45c8",
    AUDIT_INPUT_PATHS[1]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "471b1d688cf96d9be26b5c49087a147c896e8994",
    AUDIT_INPUT_PATHS[1]: "98b1571228ad0902301b6853208ef249ea2c2973",
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_COUNTEREXAMPLES = (
    {
        "candidate": "BANK0_HEAD1_XOR_HEAD2", "wires": (110, 111),
        "generator_pair": (3, 8), "modulus": 2, "residue": 0,
        "before_parity": 1, "after_parity": 0, "input_weight": 2908,
        "input_state_sha256":
            "bf498daa3ab78cd5054acf599438bf217061160e689cb5444b151cc624246292",
        "output_state_sha256":
            "d2c267606915846b6f225929738d7359e6aa703df26899baddab13adcff1eb90",
    },
    {
        "candidate": "BANK0_HEAD1_XOR_HEAD3", "wires": (110, 112),
        "generator_pair": (1, 6), "modulus": 3, "residue": 2,
        "before_parity": 1, "after_parity": 0, "input_weight": 1938,
        "input_state_sha256":
            "b63a01ce21af92c441485b9968037997785d0aa323ae3a9a5a876927c0deadd3",
        "output_state_sha256":
            "ab39ed7516074ce7f060ae49fde382e49c5a00f70100becef64c2d77ebdd3a0e",
    },
    {
        "candidate": "BANK0_HEAD1_XOR_HEAD4", "wires": (110, 113),
        "generator_pair": (3, 8), "modulus": 2, "residue": 0,
        "before_parity": 1, "after_parity": 0, "input_weight": 2908,
        "input_state_sha256":
            "bf498daa3ab78cd5054acf599438bf217061160e689cb5444b151cc624246292",
        "output_state_sha256":
            "d2c267606915846b6f225929738d7359e6aa703df26899baddab13adcff1eb90",
    },
    {
        "candidate": "BANK0_HEAD1_XOR_HEAD5", "wires": (110, 114),
        "generator_pair": (2, 7), "modulus": 3, "residue": 1,
        "before_parity": 0, "after_parity": 1, "input_weight": 1938,
        "input_state_sha256":
            "b2e35a28601615d86ddb090ad3becf786039e21726318b22c7205dfcb7cca5c8",
        "output_state_sha256":
            "b284f30e3cb5e8146c7f69592a0abc868ae8600856486a989cd1664d25293af7",
    },
)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

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
LANDED_TRANSITIONS = 891486
REACHABLE_STATES = LANDED_TRANSITIONS + len(EVENTS) * len(BACKBONE)
GENERATOR_APPLICATIONS = sum(RESOLUTION_MOMENTS.values())


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


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def state_sha256(state: int) -> str:
    return sha256(bytes((state >> wire) & 1 for wire in range(STATE_BITS))).hexdigest()


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
    actual_sha = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    actual_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    primary_names = function_names(trees[AUDIT_INPUT_PATHS[0]])
    fixture_names = function_names(trees[AUDIT_INPUT_PATHS[1]])
    basis = {
        "cycle851_v2_counterexample_method": {
            "universal_composed_parity_attempt", "build_word", "apply_word",
            "build_masked_schedule",
        } <= primary_names,
        "cycle830_fixture_basis": {
            "decode_fixtures", "build_words", "apply_word",
        } <= fixture_names,
        "cycle851_constants_exact": (
            literal_assignment(trees[AUDIT_INPUT_PATHS[0]], "BACKBONE") == BACKBONE
            and literal_assignment(trees[AUDIT_INPUT_PATHS[0]], "RESOLUTION_MOMENTS")
            == RESOLUTION_MOMENTS
            and literal_assignment(trees[AUDIT_INPUT_PATHS[0]], "STATE_BITS")
            == STATE_BITS
        ),
    }
    public = {
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
        "AST_basis": basis,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "text_AST_only": AUDIT_INPUT_PATHS,
        "direct_frontier_imports": tuple(sorted(
            name for name in imports if name.startswith("frontier_cycle")
        )),
        "firewall_hits": tuple(FIREWALL.hits),
    }
    public["pass"] = (
        public["literal_AUDIT_INPUT_PATHS"]
        and public["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(basis.values())
        and not public["direct_frontier_imports"]
        and not FIREWALL.hits
    )
    return public, trees


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min((right - left) % RING_STATIONS, (left - right) % RING_STATIONS) > 1
    )


def decode_fixtures(tree: ast.Module) -> dict[str, object]:
    gate_encoded = literal_assignment(tree, "GATE_CONSTANTS_B85")
    family_encoded = literal_assignment(tree, "FAMILY_STATES_B85")
    if not isinstance(gate_encoded, str) or not isinstance(family_encoded, str):
        raise AssertionError("Cycle-830 literal fixture bank missing")
    gate_raw = zlib.decompress(base64.b85decode(gate_encoded))
    family_raw = zlib.decompress(base64.b85decode(family_encoded))
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
        "family_states": len(states),
        "separated_pairs": len(separated_pairs()),
    }
    public["pass"] = (
        offset == len(gate_raw)
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and sum(lengths) == GATE_COUNT
        and len(states) == FAMILY_SIZE
        and len(separated_pairs()) == 44
    )
    return {"macros": tuple(macros), "states": states, "public": public}


def build_word(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    pair: tuple[int, int],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for step in range(RING_STATIONS):
        live = {(pair[0] + step) % RING_STATIONS, (pair[1] + step) % RING_STATIONS}
        for station, macro in enumerate(macros):
            if station in live:
                rows.extend(macro)
    return tuple(rows)


def build_masked_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for step in range(RING_STATIONS):
        masks = [0] * RING_STATIONS
        for lane, (_event, pair) in enumerate(lanes):
            masks[(pair[0] + step) % RING_STATIONS] |= 1 << lane
            masks[(pair[1] + step) % RING_STATIONS] |= 1 << lane
        for station, macro in enumerate(macros):
            if masks[station]:
                rows.extend((*row, masks[station]) for row in macro)
    return tuple(rows)


def apply_word(state: int, word: tuple[tuple[int, int, int, int], ...]) -> int:
    for kind, first, second, third in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        elif kind == 2:
            state ^= (((state >> first) & 1) & ((state >> second) & 1)) << third
        else:
            raise AssertionError(("unknown gate kind", kind))
    return state


def parity(state: int, wires: tuple[int, int]) -> int:
    return ((state >> wires[0]) ^ (state >> wires[1])) & 1


def gate_target(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    return first if kind == 0 else second if kind == 1 else third


def backward_support(
    wires: tuple[int, int], word: tuple[tuple[int, int, int, int], ...],
) -> tuple[int, ...]:
    relevant = set(wires)
    for kind, first, second, third in reversed(word):
        if gate_target((kind, first, second, third)) not in relevant:
            continue
        if kind == 1:
            relevant.add(first)
        elif kind == 2:
            relevant.update((first, second))
    return tuple(sorted(relevant))


def ranges(values: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if not values:
        return ()
    answer = []
    start = previous = values[0]
    for value in values[1:]:
        if value != previous + 1:
            answer.append((start, previous))
            start = value
        previous = value
    answer.append((start, previous))
    return tuple(answer)


def extract_patterns(
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> tuple[dict[str, object], ...]:
    patterns = []
    for expected in EXPECTED_COUNTEREXAMPLES:
        wires = expected["wires"]
        assert isinstance(wires, tuple)
        found = None
        for modulus in range(2, 17):
            for residue in range(modulus):
                before = sum(1 << wire for wire in range(residue, STATE_BITS, modulus))
                for pair in BACKBONE:
                    after = apply_word(before, words[pair])
                    if parity(before, wires) != parity(after, wires):
                        found = {
                            "candidate": expected["candidate"],
                            "wires": wires,
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
        if found != expected:
            raise AssertionError(("Cycle-851 counterexample drift", expected, found))
        pair = expected["generator_pair"]
        modulus = int(expected["modulus"])
        residue = int(expected["residue"])
        assert isinstance(pair, tuple)
        support = backward_support(wires, words[pair])
        expected_values = tuple(int(wire % modulus == residue) for wire in support)
        local_only = sum(
            value << wire for wire, value in zip(support, expected_values)
        )
        exterior_mask = ((1 << STATE_BITS) - 1) ^ sum(1 << wire for wire in support)
        exterior_one = local_only ^ exterior_mask
        local_after = apply_word(local_only, words[pair])
        exterior_after = apply_word(exterior_one, words[pair])
        local_deltas = (
            parity(local_only, wires) ^ parity(local_after, wires),
            parity(exterior_one, wires) ^ parity(exterior_after, wires),
        )
        patterns.append({
            "pattern_id": f"P{len(patterns) + 1}_{expected['candidate']}_F{pair[0]}_{pair[1]}",
            "candidate": expected["candidate"],
            "parity_fields": (
                "bank0.HEAD[1]",
                f"bank0.HEAD[{wires[1] - 109}]",
            ),
            "parity_wires": wires,
            "generator": f"F_{pair[0]}_{pair[1]}",
            "generator_pair": pair,
            "ordered_primitive_count": len(words[pair]),
            "cycle851_exact_counterexample": {
                "input_definition":
                    f"x[wire]=1 iff wire mod {modulus} == {residue}",
                "input_weight": expected["input_weight"],
                "input_state_sha256": expected["input_state_sha256"],
                "output_state_sha256": expected["output_state_sha256"],
                "before_parity": expected["before_parity"],
                "after_parity": expected["after_parity"],
                "exact_rule_counterexample": True,
            },
            "local_support": support,
            "local_expected_values": expected_values,
            "support_wire_count": len(support),
            "support_wire_ranges": ranges(support),
            "support_sha256": sha256(struct.pack(f"<{len(support)}H", *support)).hexdigest(),
            "local_configuration":
                f"for every w in support, x[w]=1 iff w mod {modulus} == {residue}",
            "violating_cylinder":
                "all 5815-bit inputs matching local_configuration on support; exterior wires arbitrary",
            "flip": f"{expected['before_parity']}->{expected['after_parity']}",
            "backward_slice_locality_proof": (
                "Reverse the ordered circuit from the two parity outputs; whenever a relevant target is met, add its CNOT/Toffoli controls. Induction through the slice proves exterior-input independence."
            ),
            "exterior_zero_and_one_deltas": local_deltas,
            "locality_verified": local_deltas == (1, 1),
        })
    return tuple(patterns)


KERNEL_C = r'''#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define STATE_BITS 5815
#define LANES 27
#define PATTERNS 4
#define MAX_SUPPORT 545
#define MAX_STEPS 51115
#define MAX_APPS 99054
#define VECTOR_BYTES ((MAX_APPS + 7) / 8)

typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c; uint64_t mask;
} MaskedGate;
typedef struct __attribute__((packed)) {
    uint64_t lane_mask; uint16_t parity_a, parity_b, support_n;
} PatternHeader;
typedef struct __attribute__((packed)) { uint16_t wire; uint8_t expected; } Cell;

static void die(const char *message) { perror(message); exit(2); }
static void *load_exact(const char *path, size_t item_size, size_t *count) {
    FILE *f = fopen(path, "rb"); if (!f) die(path);
    if (fseek(f, 0, SEEK_END)) die("fseek");
    long bytes = ftell(f); if (bytes < 0 || bytes % (long)item_size) die("size");
    rewind(f); void *p = malloc((size_t)bytes); if (!p) die("malloc");
    if (fread(p, 1, (size_t)bytes, f) != (size_t)bytes) die("fread");
    fclose(f); *count = (size_t)bytes / item_size; return p;
}
static uint64_t active_for_transition(int time) {
    uint64_t mask = 0;
    if (time < 14744) mask |= (UINT64_C(1) << 9) - 1;
    if (time < 33195) mask |= ((UINT64_C(1) << 9) - 1) << 9;
    if (time < 51115) mask |= ((UINT64_C(1) << 9) - 1) << 18;
    return mask;
}
static uint64_t active_for_state(int time) {
    uint64_t mask = 0;
    if (time <= 14744) mask |= (UINT64_C(1) << 9) - 1;
    if (time <= 33195) mask |= ((UINT64_C(1) << 9) - 1) << 9;
    if (time <= 51115) mask |= ((UINT64_C(1) << 9) - 1) << 18;
    return mask;
}
int main(int argc, char **argv) {
    if (argc != 7) { fprintf(stderr, "argc\n"); return 2; }
    size_t sched_n, column_n;
    MaskedGate *schedule = load_exact(argv[1], sizeof(MaskedGate), &sched_n);
    uint64_t *initial = load_exact(argv[2], sizeof(uint64_t), &column_n);
    if (column_n != STATE_BITS) return 3;
    FILE *pf = fopen(argv[3], "rb"); if (!pf) die(argv[3]);
    PatternHeader headers[PATTERNS]; Cell cells[PATTERNS][MAX_SUPPORT];
    memset(cells, 0, sizeof(cells));
    for (int p = 0; p < PATTERNS; ++p) {
        if (fread(&headers[p], sizeof(headers[p]), 1, pf) != 1) die("pattern header");
        if (headers[p].support_n > MAX_SUPPORT) return 4;
        if (fread(cells[p], sizeof(Cell), headers[p].support_n, pf) != headers[p].support_n)
            die("pattern cells");
    }
    if (fgetc(pf) != EOF) return 5; fclose(pf);
    size_t vector_size = (size_t)PATTERNS * MAX_SUPPORT * VECTOR_BYTES;
    uint8_t *vectors = calloc(vector_size, 1); if (!vectors) die("calloc");
    uint64_t columns[STATE_BITS]; memcpy(columns, initial, sizeof(columns));
    uint64_t applications[PATTERNS] = {0}, occurrences[PATTERNS] = {0};
    uint64_t pattern_violations[PATTERNS] = {0}, global_violations[PATTERNS] = {0};
    uint64_t reachable_single[PATTERNS][MAX_SUPPORT] = {{0}};
    uint64_t total_transitions = 0, reachable_states = 0;
    for (int time = 0; time <= MAX_STEPS; ++time) {
        uint64_t state_active = active_for_state(time);
        reachable_states += (uint64_t)__builtin_popcountll(state_active);
        for (int p = 0; p < PATTERNS; ++p)
            for (uint16_t i = 0; i < headers[p].support_n; ++i) {
                uint64_t matching = cells[p][i].expected
                    ? columns[cells[p][i].wire] : ~columns[cells[p][i].wire];
                reachable_single[p][i] +=
                    (uint64_t)__builtin_popcountll(matching & state_active);
            }
        if (time == MAX_STEPS) break;
        uint64_t active = active_for_transition(time);
        total_transitions += (uint64_t)__builtin_popcountll(active);
        uint64_t global_before[PATTERNS], pattern_before[PATTERNS];
        for (int p = 0; p < PATTERNS; ++p) {
            global_before[p] = columns[headers[p].parity_a] ^ columns[headers[p].parity_b];
            pattern_before[p] = global_before[p] & headers[p].lane_mask;
            uint64_t eligible = active & headers[p].lane_mask;
            for (int lane = 0; lane < LANES; ++lane) if ((eligible >> lane) & 1ULL) {
                uint64_t index = applications[p]++;
                if (index >= MAX_APPS) return 6;
                int full = 1;
                for (uint16_t i = 0; i < headers[p].support_n; ++i) {
                    int actual = (int)((columns[cells[p][i].wire] >> lane) & 1ULL);
                    if (actual == cells[p][i].expected) {
                        size_t offset = ((size_t)p * MAX_SUPPORT + i) * VECTOR_BYTES;
                        vectors[offset + (index >> 3)] |= (uint8_t)(1U << (index & 7));
                    } else full = 0;
                }
                occurrences[p] += (uint64_t)full;
            }
        }
        for (size_t i = 0; i < sched_n; ++i) {
            MaskedGate g = schedule[i];
            if (g.kind == 0) columns[g.a] ^= g.mask;
            else if (g.kind == 1) columns[g.b] ^= columns[g.a] & g.mask;
            else columns[g.c] ^= columns[g.a] & columns[g.b] & g.mask;
        }
        for (int p = 0; p < PATTERNS; ++p) {
            uint64_t after = columns[headers[p].parity_a] ^ columns[headers[p].parity_b];
            global_violations[p] += (uint64_t)__builtin_popcountll(
                (global_before[p] ^ after) & active
            );
            pattern_violations[p] += (uint64_t)__builtin_popcountll(
                (pattern_before[p] ^ (after & headers[p].lane_mask))
                & active & headers[p].lane_mask
            );
        }
    }
    FILE *vf = fopen(argv[4], "wb"); if (!vf) die(argv[4]);
    for (int p = 0; p < PATTERNS; ++p)
        for (uint16_t i = 0; i < headers[p].support_n; ++i) {
            size_t offset = ((size_t)p * MAX_SUPPORT + i) * VECTOR_BYTES;
            if (fwrite(vectors + offset, 1, VECTOR_BYTES, vf) != VECTOR_BYTES) die("vectors");
    }
    fclose(vf);
    FILE *cf = fopen(argv[5], "wb"); if (!cf) die(argv[5]);
    for (int p = 0; p < PATTERNS; ++p)
        if (fwrite(reachable_single[p], sizeof(uint64_t), headers[p].support_n, cf)
                != headers[p].support_n) die("reachable counts");
    fclose(cf);
    FILE *summary = fopen(argv[6], "w"); if (!summary) die(argv[6]);
    fprintf(summary, "schedule_rows=%zu\ntotal_transitions=%" PRIu64 "\nreachable_states=%" PRIu64 "\nvector_bytes=%d\n",
            sched_n, total_transitions, reachable_states, VECTOR_BYTES);
    for (int p = 0; p < PATTERNS; ++p)
        fprintf(summary, "pattern_%d_applications=%" PRIu64 "\npattern_%d_occurrences=%" PRIu64 "\npattern_%d_parity_violations=%" PRIu64 "\nglobal_parity_%d_violations=%" PRIu64 "\n",
                p, applications[p], p, occurrences[p], p, pattern_violations[p], p, global_violations[p]);
    fclose(summary); free(schedule); free(initial); free(vectors); return 0;
}
'''


def write_kernel_inputs(
    directory: Path,
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    states: dict[tuple[int, tuple[int, int]], int],
    patterns: tuple[dict[str, object], ...],
) -> dict[str, object]:
    schedule = build_masked_schedule(macros, lanes)
    (directory / "schedule.bin").write_bytes(b"".join(
        struct.pack("<BHHHQ", *row) for row in schedule
    ))
    columns = tuple(sum(
        ((states[key] >> wire) & 1) << lane
        for lane, key in enumerate(lanes)
    ) for wire in range(STATE_BITS))
    (directory / "columns.bin").write_bytes(struct.pack("<5815Q", *columns))
    pattern_payload = bytearray()
    for pattern in patterns:
        pair = pattern["generator_pair"]
        support = pattern["local_support"]
        values = pattern["local_expected_values"]
        parity_wires = pattern["parity_wires"]
        assert isinstance(pair, tuple) and isinstance(support, tuple)
        assert isinstance(values, tuple) and isinstance(parity_wires, tuple)
        lane_mask = sum(
            1 << lane for lane, (_event, lane_pair) in enumerate(lanes)
            if lane_pair == pair
        )
        pattern_payload.extend(struct.pack(
            "<QHHH", lane_mask, parity_wires[0], parity_wires[1], len(support)
        ))
        for wire, value in zip(support, values):
            pattern_payload.extend(struct.pack("<HB", wire, value))
    (directory / "patterns.bin").write_bytes(pattern_payload)
    return {
        "schedule_rows": len(schedule),
        "schedule_sha256": sha256((directory / "schedule.bin").read_bytes()).hexdigest(),
        "columns_sha256": sha256((directory / "columns.bin").read_bytes()).hexdigest(),
        "patterns_sha256": sha256(pattern_payload).hexdigest(),
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
        ("cc", "--version"), check=True, capture_output=True, text=True, timeout=20,
    ).stdout.splitlines()[0]
    return {
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "binary_sha256": sha256(binary.read_bytes()).hexdigest(),
        "compiler": version,
        "compiler_stderr": completed.stderr,
    }


def execute_kernel(directory: Path, label: str) -> dict[str, object]:
    vectors = directory / f"vectors_{label}.bin"
    reachable_counts = directory / f"reachable_counts_{label}.bin"
    summary_path = directory / f"summary_{label}.txt"
    completed = subprocess.run(
        (
            str(directory / "kernel"), str(directory / "schedule.bin"),
            str(directory / "columns.bin"), str(directory / "patterns.bin"),
            str(vectors), str(reachable_counts), str(summary_path),
        ),
        cwd=ROOT, check=True, capture_output=True, text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    summary = {}
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        key, value = line.split("=", 1)
        summary[key] = int(value)
    return {
        "summary": summary,
        "vectors": vectors.read_bytes(),
        "reachable_counts": reachable_counts.read_bytes(),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def localization_census(
    payload: bytes,
    reachable_count_payload: bytes,
    patterns: tuple[dict[str, object], ...],
    vector_bytes: int,
) -> tuple[dict[str, object], ...]:
    offset = 0
    count_offset = 0
    rows = []
    for pattern in patterns:
        support = pattern["local_support"]
        values = pattern["local_expected_values"]
        parity_wires = pattern["parity_wires"]
        assert isinstance(support, tuple) and isinstance(values, tuple)
        assert isinstance(parity_wires, tuple)
        vectors = []
        for _wire in support:
            vector = int.from_bytes(payload[offset:offset + vector_bytes], "little")
            offset += vector_bytes
            vectors.append(vector)
        count_size = 8 * len(support)
        single_counts = struct.unpack(
            f"<{len(support)}Q",
            reachable_count_payload[count_offset:count_offset + count_size],
        )
        count_offset += count_size
        zero_singles = tuple(
            index for index, count in enumerate(single_counts) if count == 0
        )
        full = (1 << GENERATOR_APPLICATIONS) - 1
        for vector in vectors:
            full &= vector
        full_count = full.bit_count()
        if zero_singles:
            level = "single_wire_value"
            chosen_indices = (zero_singles[0],)
        else:
            raise AssertionError(
                "Pinned family reached the second localization rung; a full-reachable pair census is required"
            )
        chosen_wires = tuple(support[index] for index in chosen_indices)
        chosen_values = tuple(values[index] for index in chosen_indices)
        structurally_smaller = len(chosen_indices) < len(parity_wires)
        is_parity_pair = set(chosen_wires) == set(parity_wires)
        localized = full_count == 0 and structurally_smaller and not is_parity_pair
        rows.append({
            "pattern_id": pattern["pattern_id"],
            "generator_pair": pattern["generator_pair"],
            "parity_wires": parity_wires,
            "declared_granularity_ladder": (
                "single-wire target values on backward support",
                "wire-pair target configurations on backward support",
                "full witness-derived local configuration on backward support",
            ),
            "ladder_search_rule":
                "stop only after the first total rung, because all later rungs are provably non-minimal",
            "complete_reachable_state_census": REACHABLE_STATES,
            "complete_generator_application_census": GENERATOR_APPLICATIONS,
            "single_wire_configurations_checked": len(support),
            "minimum_single_wire_occurrences": min(single_counts),
            "zero_single_wire_configuration_count": len(zero_singles),
            "wire_pair_search": "NOT_REACHED_SINGLE_WIRE_RUNG_TOTAL",
            "full_local_search":
                "NOT_REACHED_FOR_LOCALIZATION; exact relevant-generator occurrence independently checked in B_USAGE_CENSUS",
            "full_local_configuration_occurrences": full_count,
            "smallest_total_blocking_level": level,
            "named_blocker": {
                "wires": chosen_wires,
                "required_values": chosen_values,
                "statement": (
                    " AND ".join(
                        f"x[{wire}]={value}" for wire, value in zip(chosen_wires, chosen_values)
                    ) + (
                        " never occurs in any of the 891,513 reachable states; "
                        f"therefore it never occurs before F_{pattern['generator_pair'][0]}_{pattern['generator_pair'][1]}"
                    )
                    if chosen_wires else "no blocker found"
                ),
                "occurrences": 0 if chosen_wires else None,
            },
            "honesty_guard": {
                "blocker_wire_count": len(chosen_wires),
                "conserved_parity_wire_count": len(parity_wires),
                "structurally_smaller_than_conserved_parity": structurally_smaller,
                "is_conserved_parity_wire_pair": is_parity_pair,
                "global_parity_or_reachability_only": not localized,
            },
            "verdict": (
                "USAGE_LOCALIZED"
                if localized else "USAGE_IRREDUCIBLE_AT_DECLARED_GRANULARITY"
            ),
            "pass": full_count == 0 and level != "none",
        })
    if offset != len(payload):
        raise AssertionError(("match-vector payload length drift", offset, len(payload)))
    if count_offset != len(reachable_count_payload):
        raise AssertionError((
            "reachable-count payload length drift", count_offset,
            len(reachable_count_payload),
        ))
    return tuple(rows)


def public_pattern(pattern: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in pattern.items()
        if key not in {"local_support", "local_expected_values"}
    }


def run() -> int:
    started = monotonic()
    sources, trees = source_controls()
    fixtures = decode_fixtures(trees[AUDIT_INPUT_PATHS[1]])
    macros = fixtures["macros"]
    states = fixtures["states"]
    assert isinstance(macros, tuple) and isinstance(states, dict)
    words = {pair: build_word(macros, pair) for pair in BACKBONE}
    patterns = extract_patterns(words)
    lanes = tuple((event, pair) for event in EVENTS for pair in BACKBONE)

    with tempfile.TemporaryDirectory(prefix="cycle853-") as temp_name:
        temp = Path(temp_name)
        kernel_inputs = write_kernel_inputs(temp, macros, lanes, states, patterns)
        compiler = compile_kernel(temp)
        replay_first = execute_kernel(temp, "first")
        replay_second = execute_kernel(temp, "second")

    exact_replay = replay_first == replay_second
    summary = replay_first["summary"]
    vector_bytes = int(summary["vector_bytes"])
    localization = localization_census(
        replay_first["vectors"], replay_first["reachable_counts"],
        patterns, vector_bytes,
    )

    certificate_a = {
        "source": AUDIT_INPUT_PATHS[0],
        "extraction": (
            "Exact replay of Cycle-851 v2's ordered candidate search: moduli 2..16, residues in order, then nine BACKBONE generators."
        ),
        "pattern_family_definition": (
            "Four witness-derived violating cylinders. For each exact Cycle-851 counterexample, the support is the syntactic backward dependency slice of the two final HEAD outputs through that exact ordered generator; the local assignment is the counterexample restricted to that support, and all exterior wires are free. This is precisely the four extracted witness cylinders, not a claim to enumerate every parity-flipping input."
        ),
        "patterns": tuple(public_pattern(pattern) for pattern in patterns),
        "pattern_count": len(patterns),
        "finding": "FOUR_EXACT_CYCLE851_VIOLATING_PATTERN_CYLINDERS_EXTRACTED",
        "pass": (
            len(patterns) == len(EXPECTED_COUNTEREXAMPLES) == 4
            and all(pattern["ordered_primitive_count"] == WORD_GATE_COUNT for pattern in patterns)
            and all(pattern["locality_verified"] for pattern in patterns)
        ),
    }

    usage_rows = []
    for index, pattern in enumerate(patterns):
        usage_rows.append({
            "pattern_id": pattern["pattern_id"],
            "generator_pair": pattern["generator_pair"],
            "eligible_applications": summary[f"pattern_{index}_applications"],
            "violating_pattern_occurrences": summary[f"pattern_{index}_occurrences"],
            "parity_flips_on_eligible_generator":
                summary[f"pattern_{index}_parity_violations"],
            "parity_flips_across_all_nine_generators":
                summary[f"global_parity_{index}_violations"],
            "independent_match_vector_full_occurrences":
                localization[index]["full_local_configuration_occurrences"],
        })
    certificate_b = {
        "scope": (
            "All 891,486 landed transitions: 27 lanes = events (0,2,1) x nine BACKBONE pairs, each from t=0 through its event horizon; every pre-generator state is censused."
        ),
        "complete_landed_transition_count": summary["total_transitions"],
        "expected_complete_landed_transition_count": LANDED_TRANSITIONS,
        "per_pattern": tuple(usage_rows),
        "finding": "ZERO_VIOLATING_PATTERN_OCCURRENCES_ACROSS_891486_LANDED_TRANSITIONS",
        "pass": (
            summary["total_transitions"] == LANDED_TRANSITIONS
            and all(row["eligible_applications"] == GENERATOR_APPLICATIONS for row in usage_rows)
            and all(row["violating_pattern_occurrences"] == 0 for row in usage_rows)
            and all(row["independent_match_vector_full_occurrences"] == 0 for row in usage_rows)
            and all(row["parity_flips_across_all_nine_generators"] == 0 for row in usage_rows)
        ),
    }

    localized_count = sum(row["verdict"] == "USAGE_LOCALIZED" for row in localization)
    certificate_c = {
        "search_policy": (
            "Search the declared ladder in increasing arity and stop at the first total rung. A level is total only when its exact target assignment has zero occurrences in all 891,513 reachable states, including terminal states; ties use lexicographically least wires."
        ),
        "complete_reachable_state_count": summary["reachable_states"],
        "expected_complete_reachable_state_count": REACHABLE_STATES,
        "honesty_policy": (
            "A local explanation is accepted only when the blocker uses fewer wires than the conserved two-wire parity and is not the parity pair itself. Pair/full-support absence is reported honestly as reachability-level irreducibility."
        ),
        "per_pattern": localization,
        "localized_patterns": localized_count,
        "irreducible_patterns": len(localization) - localized_count,
        "finding": (
            "ALL_PATTERNS_HAVE_SUB_PARITY_LOCAL_BLOCKERS"
            if localized_count == len(localization)
            else "ONE_OR_MORE_PATTERNS_IRREDUCIBLE_AT_DECLARED_GRANULARITY"
        ),
        "pass": (
            summary["reachable_states"] == REACHABLE_STATES
            and all(row["pass"] for row in localization)
        ),
    }

    overall_verdict = (
        "USAGE_LOCALIZED"
        if localized_count == len(localization)
        else "USAGE_IRREDUCIBLE_AT_DECLARED_GRANULARITY"
    )
    certificate_d = {
        "verdict": overall_verdict,
        "per_pattern": tuple({
            "pattern_id": row["pattern_id"],
            "verdict": row["verdict"],
            "smallest_total_blocking_level": row["smallest_total_blocking_level"],
            "named_blocker": row["named_blocker"],
        } for row in localization),
        "mixed_outcome": 0 < localized_count < len(localization),
        "finding": overall_verdict,
        "pass": (
            len(localization) == 4
            and all(row["verdict"] in {
                "USAGE_LOCALIZED", "USAGE_IRREDUCIBLE_AT_DECLARED_GRANULARITY",
            } for row in localization)
        ),
    }

    elapsed = monotonic() - started
    branch = subprocess.run(
        ("git", "branch", "--show-current"), cwd=ROOT, check=True,
        capture_output=True, text=True, timeout=20,
    ).stdout.strip()
    replay_control = {
        "exact_replay": exact_replay,
        "first_summary": replay_first["summary"],
        "second_summary": replay_second["summary"],
        "vectors_exact": replay_first["vectors"] == replay_second["vectors"],
        "vectors_sha256": sha256(replay_first["vectors"]).hexdigest(),
        "reachable_counts_exact": (
            replay_first["reachable_counts"] == replay_second["reachable_counts"]
        ),
        "reachable_counts_sha256":
            sha256(replay_first["reachable_counts"]).hexdigest(),
        "kernel_stdout": replay_first["stdout"],
        "kernel_stderr": replay_first["stderr"],
    }
    controls = {
        **sources,
        "fixture_reconstruction": fixtures["public"],
        "expected_branch": EXPECTED_BRANCH,
        "actual_branch": branch,
        "branch_exact": branch == EXPECTED_BRANCH,
        "kernel_inputs": kernel_inputs,
        "compiled_exact_integer_kernel": compiler,
        "determinism_replay": replay_control,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
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
        and fixtures["public"]["pass"]
        and controls["branch_exact"]
        and exact_replay
        and replay_control["vectors_exact"]
        and replay_control["reachable_counts_exact"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    certificates = {
        "A_VIOLATING_PATTERNS": certificate_a,
        "B_USAGE_CENSUS": certificate_b,
        "C_BLOCKING_LOCALIZATION": certificate_c,
        "D_VERDICT": certificate_d,
        "E_CONTROLS": controls,
    }
    checks = {
        "A_VIOLATING_PATTERNS": bool(certificate_a["pass"]),
        "B_USAGE_CENSUS": bool(certificate_b["pass"]),
        "C_BLOCKING_LOCALIZATION": bool(certificate_c["pass"]),
        "D_VERDICT": bool(certificate_d["pass"]),
        "E_CONTROLS": False,
    }
    report = {
        "cycle": 853,
        "target": "generator-usage census for Cycle-851 affine HEAD parities",
        "verdict": overall_verdict,
        "pattern_count": len(patterns),
        "runtime_seconds": round(elapsed, 6),
        "checks": {},
        "pass": False,
        "terminal": "CYCLE853_GENERATOR_USAGE_CENSUS_HONEST_FAIL",
    }

    def render() -> str:
        lines = []
        for name, value in certificates.items():
            lines.append(f"{name}: {'PASS' if checks[name] else 'FAIL'}")
            lines.append(f"{name}_FINDING={value['finding']}")
            lines.append(f"{name}_CERTIFICATE={compact(value)}")
        lines.append(f"REPORT={compact(report)}")
        return "\n".join(lines) + "\n"

    for _iteration in range(10):
        controls["pass"] = controls_base
        controls["finding"] = "CONTROLS_PASS" if controls["pass"] else "CONTROLS_FAIL"
        checks["E_CONTROLS"] = controls["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE853_GENERATOR_USAGE_CENSUS_PASS"
            if report["pass"] else "CYCLE853_GENERATOR_USAGE_CENSUS_HONEST_FAIL"
        )
        output = render()
        controls["stdout_bytes"] = len(output.encode("utf-8"))
        controls["pass"] = controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
    output = render()
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        print(compact({
            "pass": False,
            "terminal": "CYCLE853_GENERATOR_USAGE_CENSUS_HONEST_FAIL",
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
            "terminal": "CYCLE853_GENERATOR_USAGE_CENSUS_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
