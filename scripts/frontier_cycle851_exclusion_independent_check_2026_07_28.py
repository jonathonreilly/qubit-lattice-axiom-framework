#!/usr/bin/env python3
"""Cycle 851 independent adversarial check of the S0' near-miss.

The primary is a blocked text/AST input.  This checker decodes the landed
fixtures itself, constructs the X/CNOT/Toffoli words itself, and runs a
separately written exact bit-sliced replay.  Its invariant hunt is organized
around the one differing bit rather than copied from the primary.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle851_sstar_prime_exclusion_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
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
import tempfile
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, FIXTURE_PATH, LINEAGE_PATH, WIRE_MAP_PATH = AUDIT_INPUT_PATHS
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
EXPECTED_SHA256 = {
    PRIMARY_PATH: "2d5796c01613ca3b5deec05e7e86c6fe7240ba7dd87f704c90579f21d0cc45c8",
    FIXTURE_PATH: "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    LINEAGE_PATH: "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    WIRE_MAP_PATH: "b97e227375a8cc14580d8f413897df2209e9e872b1a46ec59f9a2e61af593ca8",
}
EXPECTED_GIT_BLOBS = {
    PRIMARY_PATH: "471b1d688cf96d9be26b5c49087a147c896e8994",
    FIXTURE_PATH: "98b1571228ad0902301b6853208ef249ea2c2973",
    LINEAGE_PATH: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    WIRE_MAP_PATH: "3c7a6e61bbc656b7c6b69b96be36066d0ad1e8e8",
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_S0_PRIME_SHA256 = (
    "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12"
)
EXPECTED_S1_SHA256 = (
    "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41"
)

RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
HEAD1_WIRE = 110
S1_MOVEMENT = 51110
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
EVENTS = (0, 2, 1)
RESOLUTION_MOMENTS = {0: 14744, 2: 33195, 1: 51115}


class _BlockedSourceFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids source import: {fullname}")
        return None


FIREWALL = _BlockedSourceFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def state_sha256(state: int) -> str:
    unpacked = bytes((state >> wire) & 1 for wire in range(STATE_BITS))
    return sha256(unpacked).hexdigest()


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


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


def function_string_literals(tree: ast.Module, name: str) -> frozenset[str]:
    functions = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(functions) != 1:
        return frozenset()
    return frozenset(
        node.value for node in ast.walk(functions[0])
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )


def source_controls(
) -> tuple[dict[str, object], dict[str, bytes], dict[str, ast.Module]]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {path: ast.parse(payload, filename=path) for path, payload in payloads.items()}
    actual_sha = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    actual_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    literal_paths = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    primary_literals = function_string_literals(
        trees[PRIMARY_PATH], "local_invariant_hunt"
    )
    required_declared_labels = frozenset({
        "FULL_5815", "SOURCE_ENDPOINTS", "LANDED_REGISTER_39",
        "BANK0_HEAD_6", "S0PRIME_COMPANION_WIRE",
        "all_untouched_wire_parities", "weight_bands",
        "three_wire_predicate_triples", "conserved_subregister_patterns",
    })
    primary_literal_contract = {
        "HEAD1_WIRE": literal_assignment(trees[PRIMARY_PATH], "HEAD1_WIRE"),
        "BACKBONE": literal_assignment(trees[PRIMARY_PATH], "BACKBONE"),
        "RESOLUTION_MOMENTS": literal_assignment(
            trees[PRIMARY_PATH], "RESOLUTION_MOMENTS"
        ),
        "declared_labels_present": required_declared_labels <= primary_literals,
    }
    public = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS": literal_paths == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "source_access": "read_bytes plus ast.parse only; no source module imported",
        "direct_frontier_imports": tuple(sorted(
            name for name in imports if name.startswith("frontier_cycle")
        )),
        "firewall_hits": tuple(FIREWALL.hits),
        "primary_literal_contract": primary_literal_contract,
    }
    public["pass"] = (
        public["literal_AUDIT_INPUT_PATHS"]
        and public["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and not public["direct_frontier_imports"]
        and not FIREWALL.hits
        and primary_literal_contract == {
            "HEAD1_WIRE": HEAD1_WIRE,
            "BACKBONE": BACKBONE,
            "RESOLUTION_MOMENTS": RESOLUTION_MOMENTS,
            "declared_labels_present": True,
        }
    )
    return public, payloads, trees


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
        "family_states": len(states),
        "family_weight_census": dict(sorted(Counter(map(int.bit_count, states.values())).items())),
    }
    public["pass"] = (
        offset == len(gate_raw)
        and len(family_raw) == len(keys) * STATE_BYTES
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and len(states) == 176
    )
    return {"macros": tuple(macros), "states": states, "public": public}


def build_word(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    pair: tuple[int, int],
) -> tuple[tuple[int, int, int, int], ...]:
    word = []
    for movement in range(RING_STATIONS):
        live = {(pair[0] + movement) % RING_STATIONS,
                (pair[1] + movement) % RING_STATIONS}
        for station, macro in enumerate(macros):
            if station in live:
                word.extend(macro)
    return tuple(word)


def apply_word(state: int, word: tuple[tuple[int, int, int, int], ...]) -> int:
    for kind, first, second, third in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        elif kind == 2:
            state ^= (((state >> first) & 1) & ((state >> second) & 1)) << third
        else:
            raise AssertionError(("unknown gate", kind))
    return state


def gate_target(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    return first if kind == 0 else second if kind == 1 else third


def build_masked_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    schedule = []
    for movement in range(RING_STATIONS):
        station_masks = [0] * RING_STATIONS
        for lane, (_event, pair) in enumerate(lanes):
            station_masks[(pair[0] + movement) % RING_STATIONS] |= 1 << lane
            station_masks[(pair[1] + movement) % RING_STATIONS] |= 1 << lane
        for station, macro in enumerate(macros):
            lane_mask = station_masks[station]
            if lane_mask:
                schedule.extend((*row, lane_mask) for row in macro)
    return tuple(schedule)


KERNEL_C = r'''#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define STATE_BITS 5815
#define STATE_BYTES 727
#define LANES 27
#define REGISTER_BITS 39
#define COUNTER_BITS 13
#define TARGET_MOVEMENT 51110
#define LAST_MOVEMENT 51115

typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c;
} Gate;
typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c; uint64_t lanes;
} MaskedGate;

static void fail(const char *message) { perror(message); exit(2); }
static void *read_all(const char *path, size_t width, size_t *count) {
    FILE *stream = fopen(path, "rb"); if (!stream) fail(path);
    if (fseek(stream, 0, SEEK_END)) fail("fseek");
    long bytes = ftell(stream); if (bytes < 0 || bytes % (long)width) fail("size");
    rewind(stream); void *data = malloc((size_t)bytes); if (!data) fail("malloc");
    if (fread(data, 1, (size_t)bytes, stream) != (size_t)bytes) fail("fread");
    fclose(stream); *count = (size_t)bytes / width; return data;
}
static uint64_t active_states(int movement) {
    uint64_t mask = 0;
    if (movement <= 14744) mask |= (UINT64_C(1) << 9) - 1;
    if (movement <= 33195) mask |= ((UINT64_C(1) << 9) - 1) << 9;
    if (movement <= 51115) mask |= ((UINT64_C(1) << 9) - 1) << 18;
    return mask;
}
static uint64_t active_transitions(int movement) {
    uint64_t mask = 0;
    if (movement < 14744) mask |= (UINT64_C(1) << 9) - 1;
    if (movement < 33195) mask |= ((UINT64_C(1) << 9) - 1) << 9;
    if (movement < 51115) mask |= ((UINT64_C(1) << 9) - 1) << 18;
    return mask;
}
static void execute_word(uint64_t *state, const Gate *word, size_t count) {
    for (size_t i = 0; i < count; ++i) {
        Gate g = word[i];
        if (g.kind == 0) state[g.a] ^= UINT64_C(1);
        else if (g.kind == 1) state[g.b] ^= state[g.a];
        else if (g.kind == 2) state[g.c] ^= state[g.a] & state[g.b];
        else exit(4);
    }
}
static void execute_schedule(uint64_t *columns, const MaskedGate *rows, size_t count) {
    for (size_t i = 0; i < count; ++i) {
        MaskedGate g = rows[i];
        if (g.kind == 0) columns[g.a] ^= g.lanes;
        else if (g.kind == 1) columns[g.b] ^= columns[g.a] & g.lanes;
        else if (g.kind == 2) columns[g.c] ^= columns[g.a] & columns[g.b] & g.lanes;
        else exit(5);
    }
}
static uint64_t register_projection(
    const uint64_t *columns, const uint16_t *wires, int lane
) {
    uint64_t value = 0;
    for (int bit = 0; bit < REGISTER_BITS; ++bit)
        value |= ((columns[wires[bit]] >> lane) & UINT64_C(1)) << bit;
    return value;
}
static void span_insert(uint64_t *basis, uint64_t value) {
    for (int bit = REGISTER_BITS - 1; bit >= 0 && value; --bit) {
        if (!((value >> bit) & UINT64_C(1))) continue;
        if (basis[bit]) value ^= basis[bit];
        else { basis[bit] = value; return; }
    }
}
static uint64_t span_reduce(const uint64_t *basis, uint64_t value) {
    for (int bit = REGISTER_BITS - 1; bit >= 0 && value; --bit)
        if (((value >> bit) & UINT64_C(1)) && basis[bit]) value ^= basis[bit];
    return value;
}
static void dump_lane(const char *path, const uint64_t *columns, int lane) {
    uint8_t out[STATE_BYTES]; memset(out, 0, sizeof(out));
    for (int wire = 0; wire < STATE_BITS; ++wire)
        if ((columns[wire] >> lane) & UINT64_C(1))
            out[wire >> 3] |= (uint8_t)(1U << (wire & 7));
    FILE *stream = fopen(path, "wb"); if (!stream) fail(path);
    if (fwrite(out, 1, sizeof(out), stream) != sizeof(out)) fail("fwrite");
    fclose(stream);
}
static void dump_single(const char *path, const uint64_t *state) {
    uint8_t out[STATE_BYTES]; memset(out, 0, sizeof(out));
    for (int wire = 0; wire < STATE_BITS; ++wire)
        if (state[wire] & UINT64_C(1)) out[wire >> 3] |= (uint8_t)(1U << (wire & 7));
    FILE *stream = fopen(path, "wb"); if (!stream) fail(path);
    if (fwrite(out, 1, sizeof(out), stream) != sizeof(out)) fail("fwrite");
    fclose(stream);
}

int main(int argc, char **argv) {
    if (argc != 9) { fprintf(stderr, "expected eight paths\n"); return 2; }
    size_t word_n, schedule_n, seed_n, column_n, register_n;
    Gate *word = read_all(argv[1], sizeof(Gate), &word_n);
    MaskedGate *schedule = read_all(argv[2], sizeof(MaskedGate), &schedule_n);
    uint8_t *seed = read_all(argv[3], 1, &seed_n);
    uint64_t *initial = read_all(argv[4], sizeof(uint64_t), &column_n);
    uint16_t *register_wires = read_all(argv[5], sizeof(uint16_t), &register_n);
    if (seed_n != STATE_BYTES || column_n != STATE_BITS || register_n != REGISTER_BITS)
        return 3;

    uint64_t target[STATE_BITS];
    for (int wire = 0; wire < STATE_BITS; ++wire)
        target[wire] = (seed[wire >> 3] >> (wire & 7)) & 1U;
    for (int movement = 0; movement < TARGET_MOVEMENT; ++movement)
        execute_word(target, word, word_n);
    target[110] ^= UINT64_C(1);
    dump_single(argv[6], target);

    uint64_t columns[STATE_BITS]; memcpy(columns, initial, sizeof(columns));
    uint64_t basis[REGISTER_BITS] = {0};
    uint32_t best_distance = UINT32_MAX, best_movement = 0, best_lane = 0;
    uint64_t hits = 0, visited = 0, transition_count = 0;
    uint64_t profile = UINT64_C(1469598103934665603);
    for (int movement = 0; movement <= LAST_MOVEMENT; ++movement) {
        uint64_t active = active_states(movement), counters[COUNTER_BITS] = {0};
        visited += (uint64_t)__builtin_popcountll(active);
        for (int wire = 0; wire < STATE_BITS; ++wire) {
            uint64_t carry = (columns[wire] ^ (target[wire] ? active : 0)) & active;
            for (int bit = 0; carry && bit < COUNTER_BITS; ++bit) {
                uint64_t next = counters[bit] & carry;
                counters[bit] ^= carry; carry = next;
            }
        }
        for (int lane = 0; lane < LANES; ++lane) if ((active >> lane) & 1U) {
            uint32_t distance = 0;
            for (int bit = 0; bit < COUNTER_BITS; ++bit)
                distance |= (uint32_t)(((counters[bit] >> lane) & 1U) << bit);
            if (distance == 0) ++hits;
            if (distance < best_distance) {
                best_distance = distance; best_movement = (uint32_t)movement;
                best_lane = (uint32_t)lane;
            }
            profile ^= (uint64_t)distance + ((uint64_t)movement << 13) + ((uint64_t)lane << 48);
            profile *= UINT64_C(1099511628211);
        }
        if (movement == LAST_MOVEMENT) break;
        uint64_t before[LANES];
        for (int lane = 0; lane < LANES; ++lane)
            before[lane] = register_projection(columns, register_wires, lane);
        execute_schedule(columns, schedule, schedule_n);
        uint64_t transitions = active_transitions(movement);
        transition_count += (uint64_t)__builtin_popcountll(transitions);
        for (int lane = 0; lane < LANES; ++lane) if ((transitions >> lane) & 1U) {
            uint64_t after = register_projection(columns, register_wires, lane);
            span_insert(basis, before[lane] ^ after);
        }
    }

    memcpy(columns, initial, sizeof(columns));
    for (uint32_t movement = 0; movement < best_movement; ++movement)
        execute_schedule(columns, schedule, schedule_n);
    dump_lane(argv[7], columns, (int)best_lane);

    int head_index = -1, rank = 0;
    for (int bit = 0; bit < REGISTER_BITS; ++bit) {
        if (register_wires[bit] == 110) head_index = bit;
        if (basis[bit]) ++rank;
    }
    uint64_t head_remainder = head_index < 0 ? UINT64_MAX
        : span_reduce(basis, UINT64_C(1) << head_index);
    FILE *summary = fopen(argv[8], "w"); if (!summary) fail(argv[8]);
    fprintf(summary,
        "min_distance=%u\nbest_movement=%u\nbest_lane=%u\ntarget_hits=%" PRIu64
        "\nvisited_states=%" PRIu64 "\ntransition_count=%" PRIu64
        "\nword_rows=%zu\nschedule_rows=%zu"
        "\nprofile=%016" PRIx64 "\nregister_rank=%d\nhead_register_index=%d"
        "\nhead_unit_remainder=%016" PRIx64 "\n",
        best_distance, best_movement, best_lane, hits, visited, transition_count,
        word_n, schedule_n,
        profile, rank, head_index, head_remainder);
    for (int bit = 0; bit < REGISTER_BITS; ++bit)
        fprintf(summary, "basis_%02d=%016" PRIx64 "\n", bit, basis[bit]);
    fclose(summary);
    free(word); free(schedule); free(seed); free(initial); free(register_wires);
    return 0;
}
'''


def write_kernel_inputs(
    directory: Path,
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    states: dict[tuple[int, tuple[int, int]], int],
    register_wires: tuple[int, ...],
) -> dict[str, object]:
    word = build_word(macros, BACKBONE[0])
    schedule = build_masked_schedule(macros, lanes)
    paths = {
        "word": directory / "target_word.bin",
        "schedule": directory / "masked_schedule.bin",
        "seed": directory / "seed.bin",
        "columns": directory / "columns.bin",
        "register": directory / "register_wires.bin",
    }
    paths["word"].write_bytes(b"".join(struct.pack("<BHHH", *row) for row in word))
    paths["schedule"].write_bytes(b"".join(
        struct.pack("<BHHHQ", *row) for row in schedule
    ))
    paths["seed"].write_bytes(
        states[(1, BACKBONE[0])].to_bytes(STATE_BYTES, "little")
    )
    columns = tuple(sum(
        ((states[key] >> wire) & 1) << lane for lane, key in enumerate(lanes)
    ) for wire in range(STATE_BITS))
    paths["columns"].write_bytes(struct.pack("<5815Q", *columns))
    paths["register"].write_bytes(struct.pack("<39H", *register_wires))
    return {
        "word_rows": len(word),
        "schedule_rows": len(schedule),
        "digests": {
            name: sha256(path.read_bytes()).hexdigest() for name, path in paths.items()
        },
    }


def compile_kernel(directory: Path) -> dict[str, object]:
    source = directory / "independent.c"
    binary = directory / "independent"
    source.write_text(KERNEL_C, encoding="utf-8")
    built = subprocess.run(
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
        "stderr": built.stderr,
    }


def execute_kernel(directory: Path, label: str) -> dict[str, object]:
    target = directory / f"target_{label}.bin"
    closest = directory / f"closest_{label}.bin"
    summary_path = directory / f"summary_{label}.txt"
    completed = subprocess.run(
        (
            str(directory / "independent"),
            str(directory / "target_word.bin"),
            str(directory / "masked_schedule.bin"),
            str(directory / "seed.bin"), str(directory / "columns.bin"),
            str(directory / "register_wires.bin"), str(target), str(closest),
            str(summary_path),
        ),
        cwd=ROOT, check=True, capture_output=True, text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    summary: dict[str, int | str] = {}
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        name, value = line.split("=", 1)
        if name == "profile" or name.startswith("basis_") or name == "head_unit_remainder":
            summary[name] = value
        else:
            summary[name] = int(value)
    return {
        "summary": summary,
        "target": target.read_bytes(),
        "closest": closest.read_bytes(),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def projection(state: int, wires: tuple[int, ...]) -> int:
    return sum(((state >> wire) & 1) << bit for bit, wire in enumerate(wires))


def parity(state: int, wires: tuple[int, ...]) -> int:
    return projection(state, wires).bit_count() & 1


def transition_components(
    wires: tuple[int, ...],
    gates: tuple[tuple[int, int, int, int], ...],
) -> tuple[tuple[int, ...], ...]:
    """Exact components induced by every primitive on a local projection."""
    size = 1 << len(wires)
    parent = list(range(size))
    local = {wire: bit for bit, wire in enumerate(wires)}

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(left: int, right: int) -> None:
        left, right = find(left), find(right)
        if left != right:
            parent[max(left, right)] = min(left, right)

    for kind, first, second, third in gates:
        target = first if kind == 0 else second if kind == 1 else third
        if target not in local:
            continue
        controls = () if kind == 0 else (first,) if kind == 1 else (first, second)
        for pattern in range(size):
            if all(
                control not in local or ((pattern >> local[control]) & 1)
                for control in controls
            ):
                union(pattern, pattern ^ (1 << local[target]))
    groups: dict[int, list[int]] = {}
    for pattern in range(size):
        groups.setdefault(find(pattern), []).append(pattern)
    return tuple(tuple(group) for _root, group in sorted(groups.items()))


def component_index(components: tuple[tuple[int, ...], ...], pattern: int) -> int:
    return next(index for index, group in enumerate(components) if pattern in group)


def primary_declared_family_check(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    states: dict[tuple[int, tuple[int, int]], int],
    target: int,
    field_wire: dict[str, int],
    register_wires: tuple[int, ...],
) -> dict[str, object]:
    gates = tuple(row for macro in macros for row in macro)
    mutable = frozenset(map(gate_target, gates))
    head_wires = tuple(field_wire[f"bank0.HEAD[{index}]"] for index in range(6))
    explicit = {
        "FULL_5815": tuple(range(STATE_BITS)),
        "SOURCE_ENDPOINTS": (
            field_wire["source.LEFT_ENDPOINT"], field_wire["source.RIGHT_ENDPOINT"],
        ),
        "LANDED_REGISTER_39": register_wires,
        "BANK0_HEAD_6": head_wires,
        "S0PRIME_COMPANION_WIRE": (HEAD1_WIRE,),
    }
    parity_rows = []
    exclusions = []
    for name, wires in explicit.items():
        sensitive = HEAD1_WIRE in wires
        failure_gate = next((row for row in gates if gate_target(row) in wires), None)
        preserved = failure_gate is None
        matching = next((key for key, state in sorted(states.items())
                         if parity(state, wires) == parity(target, wires)), None)
        separates = matching is None
        disposition = (
            "DEAD_BY_ONE_BIT_LEMMA" if not sensitive
            else "FAILS_PRIMITIVE_INDUCTION" if not preserved
            else "DOES_NOT_SEPARATE" if not separates
            else "EXCLUSION"
        )
        parity_rows.append({
            "candidate": name,
            "wire_count": len(wires),
            "includes_differing_bit": sensitive,
            "primitive_induction_preserved": preserved,
            "exact_failure_gate": failure_gate,
            "separates_initial_family": separates,
            "nonseparation_witness": matching,
            "lemma_disposition": disposition,
        })
        if preserved and separates:
            exclusions.append({"class": "declared_parity", "candidate": name})

    untouched = tuple(wire for wire in range(STATE_BITS) if wire not in mutable)
    untouched_row = {
        "candidate_count": f"2^{len(untouched)} parities plus the full U pattern",
        "head_is_mutable": HEAD1_WIRE in mutable,
        "head_in_U": HEAD1_WIRE in untouched,
        "constant_under_decisive_flip": HEAD1_WIRE not in untouched,
        "lemma_disposition": "DEAD_BY_ONE_BIT_LEMMA",
    }
    initial_weights = frozenset(state.bit_count() for state in states.values())
    weight_witness = next(
        key for key, state in sorted(states.items())
        if state.bit_count() == target.bit_count()
    )
    weight_row = {
        "candidates": ("initial exact weight set", "initial containing interval"),
        "sensitive_to_decisive_flip_at_S1": True,
        "target_weight": target.bit_count(),
        "target_weight_in_initial_set": target.bit_count() in initial_weights,
        "nonseparation_witness": weight_witness,
        "lemma_disposition": "SENSITIVE_BUT_DOES_NOT_SEPARATE",
    }

    toffoli = tuple(sorted({
        (first, second, third)
        for kind, first, second, third in gates if kind == 2
    }))
    touching = tuple(row for row in toffoli if HEAD1_WIRE in row)
    triples = tuple(dict.fromkeys((
        (head_wires[0], head_wires[1], head_wires[2]),
        (field_wire["source.LEFT_ENDPOINT"],
         field_wire["source.RIGHT_ENDPOINT"], HEAD1_WIRE),
        *toffoli[:3], *touching[:3],
    )))
    triple_rows = []
    for wires in triples:
        components = transition_components(wires, gates)
        target_pattern = projection(target, wires)
        target_component = component_index(components, target_pattern)
        if HEAD1_WIRE in wires:
            flip_pattern = target_pattern ^ (1 << wires.index(HEAD1_WIRE))
            sensitive_members_exist = (
                component_index(components, flip_pattern) != target_component
            )
        else:
            sensitive_members_exist = False
        matching = next((
            key for key, state in sorted(states.items())
            if component_index(components, projection(state, wires)) == target_component
        ), None)
        separates = matching is None
        triple_rows.append({
            "wires": wires,
            "component_count": len(components),
            "all_members_primitive_induction_preserved": True,
            "head_sensitive_member_exists": sensitive_members_exist,
            "target_component": components[target_component],
            "separates_initial_family": separates,
            "nonseparation_witness": matching,
            "lemma_disposition": (
                "SENSITIVE_AND_EXCLUDING" if sensitive_members_exist and separates
                else "SENSITIVE_BUT_DOES_NOT_SEPARATE" if sensitive_members_exist
                else "DEAD_BY_ONE_BIT_LEMMA"
            ),
        })
        if separates:
            exclusions.append({
                "class": "declared_three_wire_component", "wires": wires,
            })
    return {
        "explicit_parities": tuple(parity_rows),
        "all_untouched_parities_and_pattern": untouched_row,
        "weight_bands": weight_row,
        "three_wire_component_families": tuple(triple_rows),
        "declared_exclusions": tuple(exclusions),
        "pass": (
            not exclusions
            and untouched_row["head_is_mutable"]
            and untouched_row["constant_under_decisive_flip"]
            and weight_row["target_weight_in_initial_set"]
            and all(row["nonseparation_witness"] is not None for row in triple_rows)
        ),
    }


def centered_local_hunt(
    gates: tuple[tuple[int, int, int, int], ...],
    states: dict[tuple[int, tuple[int, int]], int],
    target: int,
) -> dict[str, object]:
    incident = tuple(row for row in gates if HEAD1_WIRE in row[1:])
    neighbors = tuple(sorted({wire for row in incident for wire in row[1:]
                              if wire != HEAD1_WIRE}))
    supports = [(HEAD1_WIRE,)]
    for neighbor_count in range(1, 4):
        supports.extend(tuple(sorted((HEAD1_WIRE, *chosen)))
                        for chosen in combinations(neighbors, neighbor_count))
    supports.append(tuple(sorted((HEAD1_WIRE, *neighbors))))
    supports = list(dict.fromkeys(supports))
    rows = []
    exclusions = []
    for wires in supports:
        components = transition_components(wires, gates)
        target_pattern = projection(target, wires)
        flipped_pattern = target_pattern ^ (1 << wires.index(HEAD1_WIRE))
        target_component = component_index(components, target_pattern)
        flip_component = component_index(components, flipped_pattern)
        matching = next((
            key for key, state in sorted(states.items())
            if component_index(components, projection(state, wires)) == target_component
        ), None)
        separates = matching is None
        row = {
            "support": wires,
            "patterns": 1 << len(wires),
            "component_count": len(components),
            "induction_proof": (
                "components are the exact equivalence closure of every projected "
                "X/CNOT/Toffoli edge, with external controls universally covered; "
                "component-constant predicates are preserved gate-by-gate and hence "
                "by every landed word"
            ),
            "target_and_head_flip_same_component": target_component == flip_component,
            "separates_initial_family": separates,
            "nonseparation_witness": matching,
        }
        rows.append(row)
        if separates:
            exclusions.append({
                "class": "centered_local_component_indicator",
                "support": wires,
                "target_component": components[target_component],
            })
    x_head_gates = tuple(row for row in gates if row[0] == 0 and row[1] == HEAD1_WIRE)
    return {
        "direct_neighbors": neighbors,
        "supports_exhausted": len(rows),
        "support_rule": "all head-centered supports of size 1..4 in the direct gate star, plus the full star",
        "candidate_rows": tuple(rows),
        "unconditional_X_head_gates": x_head_gates,
        "general_primitive_induction_theorem": (
            "Because an unconditional X primitive toggles wire 110 with every other "
            "wire fixed, every function invariant under every primitive is constant "
            "on the decisive wire-110 flip; the one-bit lemma therefore kills the "
            "entire primitive-inductive function class, not only these local supports."
        ),
        "exclusions": tuple(exclusions),
        "pass": (
            bool(x_head_gates)
            and not exclusions
            and all(row["target_and_head_flip_same_component"] for row in rows)
            and all(row["nonseparation_witness"] is not None for row in rows)
        ),
    }


def reduce_span(basis: tuple[int, ...], value: int) -> int:
    for bit in range(len(basis) - 1, -1, -1):
        if ((value >> bit) & 1) and basis[bit]:
            value ^= basis[bit]
    return value


def orthogonal_nullspace(
    equations: tuple[int, ...], width: int,
) -> tuple[int, ...]:
    """Return a canonical basis for vectors orthogonal to every equation."""
    rows = [row for row in equations if row]
    pivot_columns = []
    rank = 0
    for column in range(width):
        selected = next((
            index for index in range(rank, len(rows))
            if (rows[index] >> column) & 1
        ), None)
        if selected is None:
            continue
        rows[rank], rows[selected] = rows[selected], rows[rank]
        for index in range(len(rows)):
            if index != rank and ((rows[index] >> column) & 1):
                rows[index] ^= rows[rank]
        pivot_columns.append(column)
        rank += 1
    free_columns = tuple(
        column for column in range(width) if column not in pivot_columns
    )
    result = []
    for free in free_columns:
        vector = 1 << free
        for row, pivot in zip(rows[:rank], pivot_columns):
            if (row & vector).bit_count() & 1:
                vector |= 1 << pivot
        result.append(vector)
    return tuple(result)


def run() -> int:
    started = monotonic()
    sources, _payloads, trees = source_controls()
    fixtures = decode_fixtures(trees[FIXTURE_PATH])
    macros = fixtures["macros"]
    states = fixtures["states"]
    assert isinstance(macros, tuple) and isinstance(states, dict)

    lineage = {
        "BACKBONE": literal_assignment(trees[LINEAGE_PATH], "BACKBONE"),
        "EVENTS": literal_assignment(trees[LINEAGE_PATH], "EVENTS"),
        "RESOLUTION_MOMENTS": literal_assignment(
            trees[LINEAGE_PATH], "RESOLUTION_MOMENTS"
        ),
    }
    register_fields = literal_assignment(trees[WIRE_MAP_PATH], "REGISTER_FIELDS")
    register_wires = literal_assignment(trees[WIRE_MAP_PATH], "REGISTER_WIRES")
    if not isinstance(register_fields, tuple) or not isinstance(register_wires, tuple):
        raise AssertionError("Cycle-845 register map literals missing")
    field_wire = dict(zip(register_fields, register_wires))
    lineage_exact = (
        lineage == {
            "BACKBONE": BACKBONE,
            "EVENTS": EVENTS,
            "RESOLUTION_MOMENTS": RESOLUTION_MOMENTS,
        }
        and len(register_fields) == len(register_wires) == 39
        and field_wire.get("bank0.HEAD[1]") == HEAD1_WIRE
    )
    lanes = tuple((event, pair) for event in EVENTS for pair in BACKBONE)

    with tempfile.TemporaryDirectory(prefix="cycle851-independent-") as temp_name:
        temp = Path(temp_name)
        kernel_inputs = write_kernel_inputs(
            temp, macros, lanes, states, register_wires
        )
        compiler = compile_kernel(temp)
        first = execute_kernel(temp, "first")
        second = execute_kernel(temp, "second")
        deterministic = first == second
        summary = first["summary"]
        target = int.from_bytes(first["target"], "little")
        closest = int.from_bytes(first["closest"], "little")

    s1 = target ^ (1 << HEAD1_WIRE)
    closest_lane = int(summary["best_lane"])
    closest_key = lanes[closest_lane]
    expected_visited = sum(
        RESOLUTION_MOMENTS[event] + 1 for event, _pair in lanes
    )
    expected_transitions = sum(
        RESOLUTION_MOMENTS[event] for event, _pair in lanes
    )
    differing_wires = tuple(
        wire for wire in range(STATE_BITS) if ((closest ^ target) >> wire) & 1
    )

    unvisited = {
        "independent_state_rule": (
            "Each decoded t=0 fixture is advanced by the independently constructed "
            "ordered pair word; the C kernel evaluates all 27 lanes at every inclusive "
            "landed movement and computes exact bitwise Hamming distances."
        ),
        "lineage_literals": lineage,
        "lineage_and_wire_map_exact": lineage_exact,
        "fixture_reconstruction": fixtures["public"],
        "landed_lanes": lanes,
        "inclusive_horizons": RESOLUTION_MOMENTS,
        "visited_states": summary["visited_states"],
        "expected_visited_states": expected_visited,
        "target": {
            "definition": "S0' = F_(1,6)^51110(x_event1_pair(1,6)) XOR bit 110",
            "weight": target.bit_count(),
            "tuple_byte_sha256": state_sha256(target),
            "packed_sha256": packed_sha256(target),
        },
        "exact_hit_count": summary["target_hits"],
        "closest_approach": {
            "hamming_distance": summary["min_distance"],
            "event": closest_key[0],
            "pair": closest_key[1],
            "movement": summary["best_movement"],
            "state_weight": closest.bit_count(),
            "state_tuple_byte_sha256": state_sha256(closest),
            "state_packed_sha256": packed_sha256(closest),
            "equals_constructed_S1": closest == s1,
            "differing_wires": differing_wires,
            "tie_break": "least movement, then lineage lane order",
        },
        "finding": "S0PRIME_UNVISITED_EXACT_ONE_BIT_NEAR_MISS_CONFIRMED",
    }
    unvisited["pass"] = (
        lineage_exact
        and fixtures["public"]["pass"]
        and len(lanes) == 27
        and summary["visited_states"] == expected_visited == 891513
        and summary["transition_count"] == expected_transitions
        and summary["target_hits"] == 0
        and summary["min_distance"] == 1
        and summary["best_movement"] == S1_MOVEMENT
        and closest_key == (1, (1, 6))
        and closest.bit_count() == 46
        and target.bit_count() == 47
        and closest == s1
        and differing_wires == (HEAD1_WIRE,)
        and state_sha256(target) == EXPECTED_S0_PRIME_SHA256
        and state_sha256(closest) == EXPECTED_S1_SHA256
    )

    declared = primary_declared_family_check(
        macros, states, target, field_wire, register_wires
    )
    one_bit = {
        "S1_tuple_byte_sha256": state_sha256(s1),
        "S0_prime_tuple_byte_sha256": state_sha256(target),
        "xor_weight": (s1 ^ target).bit_count(),
        "differing_wires": tuple(
            wire for wire in range(STATE_BITS) if ((s1 ^ target) >> wire) & 1
        ),
        "differing_field": "bank0.HEAD[1]",
        "lemma": (
            "S1 is visited and S0'=S1 XOR bit 110.  Therefore any invariant "
            "constant under the bit-110 flip gives S0' the already-reachable S1 "
            "value and cannot exclude S0'.  Every excluding invariant must be "
            "sensitive to exactly this flip."
        ),
        "primary_declared_family_verification": declared,
        "finding": "ONE_BIT_110_BANK0_HEAD1_LEMMA_CONFIRMED",
    }
    one_bit["pass"] = (
        unvisited["pass"]
        and one_bit["xor_weight"] == 1
        and one_bit["differing_wires"] == (HEAD1_WIRE,)
        and field_wire["bank0.HEAD[1]"] == HEAD1_WIRE
        and declared["pass"]
    )

    gates = tuple(row for macro in macros for row in macro)
    centered = centered_local_hunt(gates, states, target)

    all_one = (1 << STATE_BITS) - 1
    bit_witness = None
    for pair in BACKBONE:
        after = apply_word(all_one, build_word(macros, pair))
        if ((all_one ^ after) >> HEAD1_WIRE) & 1:
            bit_witness = {
                "pair": pair,
                "input": "ALL_ONE_5815",
                "before_bit": (all_one >> HEAD1_WIRE) & 1,
                "after_bit": (after >> HEAD1_WIRE) & 1,
                "before_state_sha256": state_sha256(all_one),
                "after_state_sha256": state_sha256(after),
            }
            break
    one_wire_functions = (
        {
            "truth_table": (0, 0), "name": "constant_zero",
            "whole_step_preserved": True, "head_flip_sensitive": False,
            "disposition": "DEAD_BY_ONE_BIT_LEMMA",
        },
        {
            "truth_table": (1, 1), "name": "constant_one",
            "whole_step_preserved": True, "head_flip_sensitive": False,
            "disposition": "DEAD_BY_ONE_BIT_LEMMA",
        },
        {
            "truth_table": (0, 1), "name": "identity",
            "whole_step_preserved": False, "head_flip_sensitive": True,
            "exact_failure_witness": bit_witness,
            "disposition": "FAILS_WHOLE_STEP_PRESERVATION",
        },
        {
            "truth_table": (1, 0), "name": "complement",
            "whole_step_preserved": False, "head_flip_sensitive": True,
            "exact_failure_witness": bit_witness,
            "disposition": "FAILS_WHOLE_STEP_PRESERVATION",
        },
    )

    basis = tuple(
        int(str(summary[f"basis_{bit:02d}"]), 16) for bit in range(39)
    )
    head_register_index = register_wires.index(HEAD1_WIRE)
    basis_pivots_exact = all(
        value == 0 or value.bit_length() - 1 == bit
        for bit, value in enumerate(basis)
    )
    head_unit_remainder = reduce_span(basis, 1 << head_register_index)
    nullspace = orthogonal_nullspace(basis, 39)
    register_initials = {
        key: projection(state, register_wires) for key, state in sorted(states.items())
    }
    target_register = projection(target, register_wires)
    head_sensitive_separators = []
    for selection in range(1 << len(nullspace)):
        coefficient = 0
        for bit, vector in enumerate(nullspace):
            if (selection >> bit) & 1:
                coefficient ^= vector
        if not ((coefficient >> head_register_index) & 1):
            continue
        target_value = (coefficient & target_register).bit_count() & 1
        initial_values = frozenset(
            (coefficient & value).bit_count() & 1
            for value in register_initials.values()
        )
        if len(initial_values) == 1 and target_value not in initial_values:
            support_indices = tuple(
                bit for bit in range(39) if (coefficient >> bit) & 1
            )
            head_sensitive_separators.append({
                "coefficient_hex": f"{coefficient:010x}",
                "support_indices": support_indices,
                "support_fields": tuple(register_fields[bit] for bit in support_indices),
                "support_wires": tuple(register_wires[bit] for bit in support_indices),
                "initial_value_all_176_fixtures": next(iter(initial_values)),
                "target_value": target_value,
                "orthogonal_to_complete_delta_basis": all(
                    not ((coefficient & row).bit_count() & 1) for row in basis
                ),
            })
    minimum_weight = min(
        (len(row["support_indices"]) for row in head_sensitive_separators),
        default=None,
    )
    minimal_separators = tuple(
        row for row in head_sensitive_separators
        if len(row["support_indices"]) == minimum_weight
    )
    affine_register = {
        "support": "Cycle-845 landed 39-wire register",
        "all_affine_forms": "2^40 including the constant term",
        "head_sensitive_affine_forms": "2^39 including the constant term",
        "complete_transition_count": summary["transition_count"],
        "expected_complete_transition_count": expected_transitions,
        "delta_span_rank": sum(bool(value) for value in basis),
        "kernel_reported_rank": summary["register_rank"],
        "basis_hex": tuple(f"{value:016x}" for value in basis),
        "head_register_index": head_register_index,
        "head_unit_remainder": f"{head_unit_remainder:016x}",
        "nullspace_dimension": len(nullspace),
        "head_sensitive_separating_members": len(head_sensitive_separators),
        "minimum_separating_support_weight": minimum_weight,
        "minimal_excluding_invariants": minimal_separators,
        "proof": (
            "For an affine form a.x+c, preservation on a step with delta d is "
            "a.d=0.  The kernel inserted the exact projected delta of every landed "
            "transition into this GF(2) basis.  Each displayed coefficient is "
            "orthogonal to the basis and therefore has zero change on every one of "
            "the 891486 transitions.  Its base value is 0 on every fixture while "
            "S0' has value 1.  Finite induction over each complete landed step "
            "relation excludes S0'; no transition was sampled or omitted."
        ),
        "preserved_head_sensitive_member_exists": bool(minimal_separators),
        "separation_test": "all 176 decoded fixture bases versus the exact S0' target",
        "pass": (
            summary["transition_count"] == expected_transitions
            and basis_pivots_exact
            and sum(bool(value) for value in basis) == summary["register_rank"]
            and head_register_index == summary["head_register_index"]
            and head_unit_remainder != 0
            and str(summary["head_unit_remainder"]) != "0000000000000000"
            and len(nullspace) == 39 - int(summary["register_rank"])
            and minimum_weight == 2
            and len(minimal_separators) == 4
            and all(row["orthogonal_to_complete_delta_basis"]
                    for row in minimal_separators)
        ),
    }

    affine_exclusions = tuple({
        "class": "complete_landed_step_affine_invariant",
        **row,
        "induction_horizon_count": expected_transitions,
    } for row in minimal_separators)
    exclusions = tuple(centered["exclusions"]) + affine_exclusions
    ruling = (
        "S0PRIME_EXCLUDED_BY_INVARIANT"
        if exclusions else "OPEN_AFTER_LEMMA_PRIORITIZED_EXTENSION"
    )
    constructive = {
        "scope": (
            "Beyond the primary: the universal primitive-inductive function class; "
            "all centered direct-star component invariants on supports through size "
            "four plus the full star; all affine forms on the landed 39-wire register "
            "against every landed transition; and all four functions of wire 110 alone "
            "against the whole composed step."
        ),
        "primitive_inductive_all_functions": {
            "unconditional_X_head_gates": centered["unconditional_X_head_gates"],
            "proof": centered["general_primitive_induction_theorem"],
            "exclusion_possible": False,
        },
        "centered_local_component_hunt": centered,
        "landed_register_affine_hunt": affine_register,
        "whole_step_one_wire_function_hunt": {
            "complete_function_count": len(one_wire_functions),
            "exact_step_failure_witness": bit_witness,
            "candidates": one_wire_functions,
            "exclusion_found": False,
        },
        "exclusions": exclusions,
        "ruling": ruling,
        "remaining_open_scope": (
            "None for the bounded landed family and horizons: any one displayed "
            "affine invariant is already an exclusion theorem.  No universal "
            "all-state-space invariant outside the landed relation is claimed."
        ),
        "finding": (
            "EXCLUSION_THEOREM_FOUND"
            if exclusions else "NO_EXCLUSION_AFTER_LEMMA_PRIORITIZED_EXTENSION"
        ),
    }
    constructive["pass"] = (
        centered["pass"]
        and affine_register["pass"]
        and bit_witness is not None
        and bit_witness["pair"] == (3, 8)
        and bool(affine_exclusions)
    )

    elapsed = monotonic() - started
    replay_control = {
        "exact_full_replay": deterministic,
        "summary_exact": first["summary"] == second["summary"],
        "target_bytes_exact": first["target"] == second["target"],
        "closest_bytes_exact": first["closest"] == second["closest"],
        "first_summary": first["summary"],
        "second_summary": second["summary"],
    }
    controls = {
        **sources,
        "kernel_inputs": kernel_inputs,
        "independently_compiled_kernel": compiler,
        "determinism": replay_control,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "finding": "CONTROLS_PASS",
        "pass": False,
    }
    controls_base = (
        sources["pass"]
        and deterministic
        and replay_control["summary_exact"]
        and replay_control["target_bytes_exact"]
        and replay_control["closest_bytes_exact"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    certificates = {
        "THE_UNVISITED_NULL": unvisited,
        "THE_ONE_BIT_LEMMA": one_bit,
        "THE_CONSTRUCTIVE_HUNT": constructive,
        "CONTROLS": controls,
    }
    checks = {
        "THE_UNVISITED_NULL": bool(unvisited["pass"]),
        "THE_ONE_BIT_LEMMA": bool(one_bit["pass"]),
        "THE_CONSTRUCTIVE_HUNT": bool(constructive["pass"]),
        "CONTROLS": False,
    }
    report = {
        "cycle": 851,
        "target": "S0' weight-47 independent one-bit adversarial check",
        "ruling": ruling,
        "primary_refuted": bool(exclusions),
        "checks": {},
        "runtime_seconds": round(elapsed, 6),
        "pass": False,
        "terminal": "CYCLE851_INDEPENDENT_CHECK_FAIL",
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
        checks["CONTROLS"] = bool(controls["pass"])
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE851_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if report["pass"] else "CYCLE851_INDEPENDENT_CHECK_FAIL"
        )
        output = render()
        controls["stdout_bytes"] = len(output.encode("utf-8"))
        controls["pass"] = controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
    output = render()
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        print(compact({
            "pass": False,
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
            "terminal": "CYCLE851_INDEPENDENT_CHECK_FAIL",
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
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE851_INDEPENDENT_CHECK_FAIL",
        }))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
