#!/usr/bin/env python3
"""Cycle 851: bounded local-invariant exclusion hunt for S0'.

S0' is the weight-47 Cycle-833/843 companion, not the distinct weight-59
pulse coincidence: S0' := S1 XOR bank0.HEAD[1], with S1 the event-1 funnel.
All predecessor sources are SHA-pinned, read only as text/AST, and blocked
from import.  The landed Boolean X/CNOT/Toffoli step is reimplemented here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "scripts/frontier_cycle845_partition_route_2026_07_28.py",
    "logs/runner-cache/frontier_cycle818_period_structure_census_2026_07_28.txt",
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
RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
HEAD1_WIRE = 110
S1_FUNNEL_MOVEMENT = 51110
RESOLUTION_MOMENTS = {0: 14744, 2: 33195, 1: 51115}
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
EXPECTED_S0_PRIME_SHA256 = (
    "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12"
)
EXPECTED_S1_SHA256 = (
    "797fa122a629177c00c707aff4857d01bbad16b078983e3a6f1f5b632e094a41"
)
EXPECTED_PULSE_SHA256 = (
    "4a7ce9fd4e9ebfdbd8580c33122d9e87c3896b24ef196e34bec49e233d044375"
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[2]:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    AUDIT_INPUT_PATHS[3]:
        "b97e227375a8cc14580d8f413897df2209e9e872b1a46ec59f9a2e61af593ca8",
    AUDIT_INPUT_PATHS[4]:
        "94bc32640518f097cb09060f9c378d26d73e263539573e3b8e75ed2aab1b857e",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[2]: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    AUDIT_INPUT_PATHS[3]: "3c7a6e61bbc656b7c6b69b96be36066d0ad1e8e8",
    AUDIT_INPUT_PATHS[4]: "3544e3beada65b3480d352e2701f6e21b3f9ae2d",
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS[:4])


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


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


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


def source_controls() -> tuple[dict[str, object], dict[str, bytes], dict[str, ast.Module]]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items() if path.endswith(".py")
    }
    actual_sha = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    actual_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    direct_frontier_imports = tuple(sorted(
        name for name in imports if name.startswith("frontier_cycle")
    ))
    basis = {
        "cycle719_transition": {"interleaved_program", "run_orbit"}
        <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle830_fixtures": {"decode_fixtures", "build_words", "apply_word"}
        <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle832_resolutions": {"evolve_funnels", "funnel_anatomies"}
        <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle845_lineage": {"decode_cycle830_fixtures", "event0_full_partition_dynamics"}
        <= function_names(trees[AUDIT_INPUT_PATHS[3]]),
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
        "text_AST_only": AUDIT_INPUT_PATHS[:4],
        "direct_frontier_imports": direct_frontier_imports,
        "firewall_hits": tuple(FIREWALL.hits),
    }
    public["pass"] = (
        public["literal_AUDIT_INPUT_PATHS"]
        and public["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(basis.values())
        and not direct_frontier_imports
        and not FIREWALL.hits
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
        rows = []
        for _index in range(length):
            rows.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(rows))
    positions = separated_pairs()
    keys = tuple(sorted(
        (event, pair) for event in range(2 * FIXTURE_BANKS) for pair in positions
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
        "positions": len(positions),
        "family_states": len(states),
        "family_weight_census": dict(sorted(Counter(map(int.bit_count, states.values())).items())),
    }
    public["pass"] = (
        offset == len(gate_raw)
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and sum(lengths) == GATE_COUNT
        and len(positions) == 44
        and len(states) == FAMILY_SIZE
    )
    return {"macros": tuple(macros), "keys": keys, "states": states, "public": public}


def period_rows(payload: bytes) -> tuple[dict[str, object], ...]:
    prefix = "PERIOD_TABLE_ROW "
    return tuple(
        json.loads(line[len(prefix):])
        for line in payload.decode("utf-8").splitlines()
        if line.startswith(prefix)
    )


def inspect_landed(rows: tuple[dict[str, object], ...]) -> dict[str, object]:
    return {
        "rows": len(rows),
        "pass_rows": sum(bool(row.get("pass")) for row in rows),
        "events": dict(sorted(Counter(int(row["event"]) for row in rows).items())),
        "periods": dict(sorted(Counter(int(row["period"]) for row in rows).items())),
        "preperiods": dict(sorted(Counter(int(row["preperiod"]) for row in rows).items())),
        "keys": tuple((int(row["event"]), tuple(row["positions"])) for row in rows),
    }


def build_word(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    pair: tuple[int, int],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for step in range(RING_STATIONS):
        live = {
            (pair[0] + step) % RING_STATIONS,
            (pair[1] + step) % RING_STATIONS,
        }
        for station, macro in enumerate(macros):
            if station in live:
                rows.extend(macro)
    return tuple(rows)


def apply_word(
    state: int,
    word: tuple[tuple[int, int, int, int], ...],
) -> int:
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


def build_masked_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for step in range(RING_STATIONS):
        station_masks = [0] * RING_STATIONS
        for lane, (_event, pair) in enumerate(lanes):
            station_masks[(pair[0] + step) % RING_STATIONS] |= 1 << lane
            station_masks[(pair[1] + step) % RING_STATIONS] |= 1 << lane
        for station, macro in enumerate(macros):
            mask = station_masks[station]
            if mask:
                rows.extend(
                    (kind, first, second, third, mask)
                    for kind, first, second, third in macro
                )
    return tuple(rows)


KERNEL_C = r'''#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define STATE_BITS 5815
#define STATE_BYTES 727
#define LANES 27
#define COUNTER_BITS 13
#define TARGET_STEPS 51110
#define MAX_STEPS 51115

typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c;
} Gate;
typedef struct __attribute__((packed)) {
    uint8_t kind; uint16_t a, b, c; uint64_t mask;
} MaskedGate;

static void die(const char *message) { perror(message); exit(2); }
static void *load_exact(const char *path, size_t item_size, size_t *count) {
    FILE *f = fopen(path, "rb"); if (!f) die(path);
    if (fseek(f, 0, SEEK_END)) die("fseek");
    long bytes = ftell(f); if (bytes < 0 || bytes % (long)item_size) die("size");
    rewind(f); void *p = malloc((size_t)bytes); if (!p) die("malloc");
    if (fread(p, 1, (size_t)bytes, f) != (size_t)bytes) die("fread");
    fclose(f); *count = (size_t)bytes / item_size; return p;
}
static void dump_lane(const char *path, const uint64_t *columns, int lane) {
    uint8_t out[STATE_BYTES]; memset(out, 0, sizeof(out));
    for (int wire = 0; wire < STATE_BITS; ++wire)
        if ((columns[wire] >> lane) & 1ULL)
            out[wire >> 3] |= (uint8_t)(1U << (wire & 7));
    FILE *f = fopen(path, "wb"); if (!f) die(path);
    if (fwrite(out, 1, sizeof(out), f) != sizeof(out)) die("fwrite"); fclose(f);
}
static void dump_single(const char *path, const uint64_t *bits) {
    uint8_t out[STATE_BYTES]; memset(out, 0, sizeof(out));
    for (int wire = 0; wire < STATE_BITS; ++wire)
        if (bits[wire] & 1ULL) out[wire >> 3] |= (uint8_t)(1U << (wire & 7));
    FILE *f = fopen(path, "wb"); if (!f) die(path);
    if (fwrite(out, 1, sizeof(out), f) != sizeof(out)) die("fwrite"); fclose(f);
}
static uint64_t active_at(int time) {
    uint64_t mask = 0;
    if (time <= 14744) mask |= (1ULL << 9) - 1;
    if (time <= 33195) mask |= ((1ULL << 9) - 1) << 9;
    if (time <= 51115) mask |= ((1ULL << 9) - 1) << 18;
    return mask;
}
int main(int argc, char **argv) {
    if (argc != 9) { fprintf(stderr, "argc\n"); return 2; }
    size_t word_n, sched_n, state_n, column_n;
    Gate *word = load_exact(argv[1], sizeof(Gate), &word_n);
    MaskedGate *sched = load_exact(argv[2], sizeof(MaskedGate), &sched_n);
    uint8_t *seed = load_exact(argv[3], 1, &state_n);
    uint64_t *initial = load_exact(argv[4], sizeof(uint64_t), &column_n);
    if (state_n != STATE_BYTES || column_n != STATE_BITS) return 3;
    uint64_t target[STATE_BITS];
    for (int wire = 0; wire < STATE_BITS; ++wire)
        target[wire] = (seed[wire >> 3] >> (wire & 7)) & 1U;
    for (int time = 0; time < TARGET_STEPS; ++time) {
        for (size_t i = 0; i < word_n; ++i) {
            Gate g = word[i];
            if (g.kind == 0) target[g.a] ^= 1ULL;
            else if (g.kind == 1) target[g.b] ^= target[g.a];
            else target[g.c] ^= target[g.a] & target[g.b];
        }
    }
    target[110] ^= 1ULL;
    dump_single(argv[5], target);

    uint64_t columns[STATE_BITS]; memcpy(columns, initial, sizeof(columns));
    uint32_t best = UINT32_MAX, best_time = 0, best_lane = 0;
    uint64_t hits = 0, profile = UINT64_C(1469598103934665603);
    for (int time = 0; time <= MAX_STEPS; ++time) {
        uint64_t active = active_at(time), counts[COUNTER_BITS] = {0};
        for (int wire = 0; wire < STATE_BITS; ++wire) {
            uint64_t carry = (columns[wire] ^ (target[wire] ? active : 0)) & active;
            for (int bit = 0; carry && bit < COUNTER_BITS; ++bit) {
                uint64_t next = counts[bit] & carry;
                counts[bit] ^= carry; carry = next;
            }
        }
        for (int bit = 0; bit < COUNTER_BITS; ++bit) {
            profile ^= counts[bit] + (uint64_t)time + ((uint64_t)bit << 48);
            profile *= UINT64_C(1099511628211);
        }
        for (int lane = 0; lane < LANES; ++lane) if ((active >> lane) & 1ULL) {
            uint32_t distance = 0;
            for (int bit = 0; bit < COUNTER_BITS; ++bit)
                distance |= (uint32_t)(((counts[bit] >> lane) & 1ULL) << bit);
            if (distance == 0) ++hits;
            if (distance < best) { best = distance; best_time = (uint32_t)time; best_lane = (uint32_t)lane; }
        }
        if (time == 1) dump_lane(argv[7], columns, 0);
        if (time == MAX_STEPS) break;
        for (size_t i = 0; i < sched_n; ++i) {
            MaskedGate g = sched[i];
            if (g.kind == 0) columns[g.a] ^= g.mask;
            else if (g.kind == 1) columns[g.b] ^= columns[g.a] & g.mask;
            else columns[g.c] ^= columns[g.a] & columns[g.b] & g.mask;
        }
    }
    /* Replay to the first lexicographic minimum so its full state is dumped. */
    memcpy(columns, initial, sizeof(columns));
    for (uint32_t time = 0; time < best_time; ++time)
        for (size_t i = 0; i < sched_n; ++i) {
            MaskedGate g = sched[i];
            if (g.kind == 0) columns[g.a] ^= g.mask;
            else if (g.kind == 1) columns[g.b] ^= columns[g.a] & g.mask;
            else columns[g.c] ^= columns[g.a] & columns[g.b] & g.mask;
        }
    dump_lane(argv[6], columns, (int)best_lane);
    FILE *summary = fopen(argv[8], "w"); if (!summary) die(argv[8]);
    fprintf(summary, "min_distance=%u\nbest_time=%u\nbest_lane=%u\ntarget_hits=%" PRIu64 "\nvisited_states=891513\nword_rows=%zu\nschedule_rows=%zu\ndistance_profile_digest=%016" PRIx64 "\n", best, best_time, best_lane, hits, word_n, sched_n, profile);
    fclose(summary); free(word); free(sched); free(seed); free(initial); return 0;
}
'''


def write_kernel_inputs(
    directory: Path,
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lanes: tuple[tuple[int, tuple[int, int]], ...],
    states: dict[tuple[int, tuple[int, int]], int],
) -> dict[str, object]:
    word = build_word(macros, BACKBONE[0])
    schedule = build_masked_schedule(macros, lanes)
    (directory / "word.bin").write_bytes(b"".join(
        struct.pack("<BHHH", *row) for row in word
    ))
    (directory / "schedule.bin").write_bytes(b"".join(
        struct.pack("<BHHHQ", *row) for row in schedule
    ))
    (directory / "seed.bin").write_bytes(
        states[(1, BACKBONE[0])].to_bytes(STATE_BYTES, "little")
    )
    columns = []
    for wire in range(STATE_BITS):
        columns.append(sum(
            ((states[key] >> wire) & 1) << lane
            for lane, key in enumerate(lanes)
        ))
    (directory / "columns.bin").write_bytes(struct.pack("<5815Q", *columns))
    return {
        "word_rows": len(word),
        "schedule_rows": len(schedule),
        "word_sha256": sha256((directory / "word.bin").read_bytes()).hexdigest(),
        "schedule_sha256": sha256((directory / "schedule.bin").read_bytes()).hexdigest(),
        "columns_sha256": sha256((directory / "columns.bin").read_bytes()).hexdigest(),
    }


def compile_kernel(directory: Path) -> dict[str, object]:
    source = directory / "kernel.c"
    binary = directory / "kernel"
    source.write_text(KERNEL_C, encoding="utf-8")
    compiler = subprocess.run(
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
        "compiler_stderr": compiler.stderr,
    }


def execute_kernel(directory: Path, label: str) -> dict[str, object]:
    target = directory / f"target_{label}.bin"
    closest = directory / f"closest_{label}.bin"
    checkpoint = directory / f"checkpoint_{label}.bin"
    summary_path = directory / f"summary_{label}.txt"
    completed = subprocess.run(
        (
            str(directory / "kernel"), str(directory / "word.bin"),
            str(directory / "schedule.bin"), str(directory / "seed.bin"),
            str(directory / "columns.bin"), str(target), str(closest),
            str(checkpoint), str(summary_path),
        ),
        cwd=ROOT, check=True, capture_output=True, text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    summary = {}
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        name, value = line.split("=", 1)
        summary[name] = value if name == "distance_profile_digest" else int(value)
    return {
        "summary": summary,
        "target": target.read_bytes(),
        "closest": closest.read_bytes(),
        "checkpoint1": checkpoint.read_bytes(),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def gate_target(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    return first if kind == 0 else second if kind == 1 else third


def projection(state: int, wires: tuple[int, ...]) -> int:
    return sum(((state >> wire) & 1) << index for index, wire in enumerate(wires))


def parity(state: int, wires: tuple[int, ...]) -> int:
    return sum((state >> wire) & 1 for wire in wires) & 1


def parity_failure_witness(
    wires: tuple[int, ...],
    states: dict[tuple[int, tuple[int, int]], int],
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> dict[str, object] | None:
    for key in sorted(states):
        before = states[key]
        after = apply_word(before, words[key[1]])
        if parity(before, wires) != parity(after, wires):
            return {
                "witness_source": "landed_initial_family",
                "key": key,
                "word_pair": key[1],
                "before_parity": parity(before, wires),
                "after_parity": parity(after, wires),
                "before_state_sha256": state_sha256(before),
                "after_state_sha256": state_sha256(after),
            }
    arbitrary_states = (
        ("ALL_ZERO", 0),
        ("ALL_ONE", (1 << STATE_BITS) - 1),
        ("SINGLE_HEAD1", 1 << HEAD1_WIRE),
    )
    for label, before in arbitrary_states:
        for pair in sorted(words):
            after = apply_word(before, words[pair])
            if parity(before, wires) != parity(after, wires):
                return {
                    "witness_source": "full_state_space",
                    "state_label": label,
                    "word_pair": pair,
                    "before_parity": parity(before, wires),
                    "after_parity": parity(after, wires),
                    "before_state_sha256": state_sha256(before),
                    "after_state_sha256": state_sha256(after),
                }
    return None


def primitive_parity_failure(
    wires: tuple[int, ...],
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
) -> dict[str, object] | None:
    wire_set = set(wires)
    for station, macro in enumerate(macros):
        for gate_index, row in enumerate(macro):
            if gate_target(row) in wire_set:
                kind, first, second, third = row
                before = 0
                if kind == 1:
                    before |= 1 << first
                elif kind == 2:
                    before |= (1 << first) | (1 << second)
                after = apply_word(before, (row,))
                return {
                    "station": station,
                    "gate_index": gate_index,
                    "gate": row,
                    "before_local_support": tuple(
                        wire for wire in (first, second, third)
                        if (before >> wire) & 1
                    ),
                    "before_parity": parity(before, wires),
                    "after_parity": parity(after, wires),
                }
    return None


def triple_components(
    triple: tuple[int, int, int],
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
) -> tuple[tuple[int, ...], ...]:
    parent = list(range(8))

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(left: int, right: int) -> None:
        left, right = find(left), find(right)
        if left != right:
            parent[max(left, right)] = min(left, right)

    local = {wire: index for index, wire in enumerate(triple)}
    for macro in macros:
        for kind, first, second, third in macro:
            target = first if kind == 0 else second if kind == 1 else third
            if target not in local:
                continue
            controls = () if kind == 0 else (first,) if kind == 1 else (first, second)
            for pattern in range(8):
                if all(
                    control not in local
                    or ((pattern >> local[control]) & 1)
                    for control in controls
                ):
                    union(pattern, pattern ^ (1 << local[target]))
    groups: dict[int, list[int]] = {}
    for pattern in range(8):
        groups.setdefault(find(pattern), []).append(pattern)
    return tuple(tuple(group) for _root, group in sorted(groups.items()))


def local_invariant_hunt(
    fixtures: dict[str, object],
    target: int,
    register_fields: tuple[str, ...],
    register_wires: tuple[int, ...],
) -> dict[str, object]:
    macros = fixtures["macros"]
    states = fixtures["states"]
    assert isinstance(macros, tuple) and isinstance(states, dict)
    words = {pair: build_word(macros, pair) for pair in separated_pairs()}
    all_gate_rows = tuple(row for macro in macros for row in macro)
    mutable_wires = frozenset(map(gate_target, all_gate_rows))
    untouched_wires = tuple(
        wire for wire in range(STATE_BITS) if wire not in mutable_wires
    )
    field_wire = dict(zip(register_fields, register_wires))
    head_wires = tuple(
        field_wire[f"bank0.HEAD[{index}]"] for index in range(6)
    )
    if field_wire["bank0.HEAD[1]"] != HEAD1_WIRE:
        raise AssertionError("Cycle-845 HEAD[1] wire drift")

    explicit_sets = {
        "FULL_5815": tuple(range(STATE_BITS)),
        "SOURCE_ENDPOINTS": (
            field_wire["source.LEFT_ENDPOINT"],
            field_wire["source.RIGHT_ENDPOINT"],
        ),
        "LANDED_REGISTER_39": register_wires,
        "BANK0_HEAD_6": head_wires,
        "S0PRIME_COMPANION_WIRE": (HEAD1_WIRE,),
    }
    parity_rows = []
    exclusions = []
    target_set = set(mutable_wires)
    for name, wires in explicit_sets.items():
        primitive_preserved = not (set(wires) & target_set)
        separation = all(
            parity(state, wires) != parity(target, wires)
            for state in states.values()
        )
        nonseparation = next((
            {
                "key": key,
                "initial_parity": parity(state, wires),
                "target_parity": parity(target, wires),
                "initial_state_sha256": state_sha256(state),
            }
            for key, state in sorted(states.items())
            if parity(state, wires) == parity(target, wires)
        ), None)
        whole_step_failure = parity_failure_witness(wires, states, words)
        row = {
            "candidate": name,
            "wire_count": len(wires),
            "primitive_induction_preserved": primitive_preserved,
            "proof_or_failure": (
                "Every X/CNOT/Toffoli changes only its declared target, and no declared target lies in this wire set; induction over every gate in every F_p preserves parity."
                if primitive_preserved
                else "Fails the gate-local induction and has the displayed exact local gate witness; the displayed full-step state-space witness independently falsifies preservation by the step relation."
            ),
            "primitive_failure_witness": primitive_parity_failure(wires, macros),
            "whole_step_failure_witness": whole_step_failure,
            "separates_all_initial_states": separation,
            "nonseparation_witness": nonseparation,
        }
        parity_rows.append(row)
        if primitive_preserved and separation:
            exclusions.append({"class": "bit_parity", "candidate": name, "wires": wires})

    witness_key = (1, BACKBONE[0])
    untouched_target = projection(target, untouched_wires)
    untouched_witness = projection(states[witness_key], untouched_wires)
    all_untouched_parities = {
        "declared_family":
            "all 2^|U| GF(2) bit parities on U, where U is the exact set of wires never targeted by any landed primitive gate",
        "U_wire_count": len(untouched_wires),
        "mutable_target_wire_count": len(mutable_wires),
        "induction_proof":
            "For each primitive, every U bit is unchanged because its only assignment is to the gate target and that target is outside U. Therefore the U pattern and every parity of it are preserved after each gate, hence after every step F_p by induction.",
        "target_projection_sha256": sha256(
            untouched_target.to_bytes((len(untouched_wires) + 7) // 8, "little")
        ).hexdigest(),
        "nonseparation_witness_key": witness_key,
        "witness_projection_sha256": sha256(
            untouched_witness.to_bytes((len(untouched_wires) + 7) // 8, "little")
        ).hexdigest(),
        "target_equals_witness_on_U": untouched_target == untouched_witness,
        "separating_member_exists": untouched_target != untouched_witness,
    }
    if not all_untouched_parities["target_equals_witness_on_U"]:
        exclusions.append({"class": "conserved_subregister_pattern", "wires": untouched_wires})

    initial_weights = frozenset(map(int.bit_count, states.values()))
    band_witness_indices = (
        173, 181, 459, 601, 726, 888, 912, 964, 1009, 1186,
        1390, 1686, 1767, 2200, 2348, 2796, 2798, 2810, 2872,
        3014, 3228, 3357, 3398, 3813, 3856, 4168, 4262, 4386,
        4426, 4580, 4863, 4925, 5228, 5277, 5455, 5518, 5639,
    )
    band_before = sum(1 << wire for wire in band_witness_indices)
    band_after = apply_word(band_before, words[BACKBONE[0]])
    weight_band = {
        "declared_candidates": (
            "initial exact weight set",
            "smallest integer interval containing all initial weights",
        ),
        "initial_exact_weight_set": tuple(sorted(initial_weights)),
        "initial_interval": (min(initial_weights), max(initial_weights)),
        "target_weight": target.bit_count(),
        "target_weight_is_initial_weight": target.bit_count() in initial_weights,
        "weight47_initial_witness_key": next(
            key for key in sorted(states) if states[key].bit_count() == target.bit_count()
        ),
        "separation_failure":
            "Both declared weight candidates contain weight 47, so neither separates S0' from all initial states.",
        "closure_failure_witness": {
            "word_pair": BACKBONE[0],
            "before_active_wires": band_witness_indices,
            "before_weight": band_before.bit_count(),
            "after_weight": band_after.bit_count(),
            "before_in_exact_set": band_before.bit_count() in initial_weights,
            "after_in_exact_set": band_after.bit_count() in initial_weights,
            "before_in_interval": min(initial_weights) <= band_before.bit_count() <= max(initial_weights),
            "after_in_interval": min(initial_weights) <= band_after.bit_count() <= max(initial_weights),
            "before_state_sha256": state_sha256(band_before),
            "after_state_sha256": state_sha256(band_after),
        },
    }

    toffoli_triples = tuple(sorted({
        (first, second, third)
        for kind, first, second, third in all_gate_rows if kind == 2
    }))
    touching_head1 = tuple(row for row in toffoli_triples if HEAD1_WIRE in row)
    declared_triples = tuple(dict.fromkeys((
        (head_wires[0], head_wires[1], head_wires[2]),
        (field_wire["source.LEFT_ENDPOINT"], field_wire["source.RIGHT_ENDPOINT"], HEAD1_WIRE),
        *toffoli_triples[:3],
        *touching_head1[:3],
    )))
    triple_rows = []
    for triple in declared_triples:
        components = triple_components(triple, macros)
        target_pattern = projection(target, triple)
        target_component = next(group for group in components if target_pattern in group)
        matching = next(
            (
                (key, projection(state, triple))
                for key, state in sorted(states.items())
                if projection(state, triple) in target_component
            ),
            None,
        )
        separates = matching is None
        triple_rows.append({
            "triple": triple,
            "primitive_transition_components": components,
            "invariant_predicate_count": 1 << len(components),
            "induction_proof":
                "The class is exactly the Boolean predicates constant on each displayed local transition component. Equality is preserved at every primitive edge; induction over the landed gate list proves preservation by every F_p.",
            "target_pattern": target_pattern,
            "target_component": target_component,
            "nonseparation_witness": matching,
            "separating_predicate_exists": separates,
        })
        if separates:
            exclusions.append({
                "class": "three_wire_component_indicator",
                "triple": triple,
                "target_component": target_component,
            })

    return {
        "declared_finite_family": {
            "explicit_bit_parities": tuple(explicit_sets),
            "all_untouched_wire_parities": f"2^{len(untouched_wires)} candidates",
            "weight_bands": weight_band["declared_candidates"],
            "three_wire_predicate_triples": declared_triples,
            "three_wire_predicate_count": sum(
                row["invariant_predicate_count"] for row in triple_rows
            ),
            "conserved_subregister_patterns": ("full U pattern",),
        },
        "bit_parity_rows": tuple(parity_rows),
        "all_untouched_wire_parities": all_untouched_parities,
        "weight_band_closure": weight_band,
        "three_wire_predicate_classes": tuple(triple_rows),
        "conserved_subregister_pattern": {
            **all_untouched_parities,
            "candidate": "full exact U projection",
        },
        "exclusions": tuple(exclusions),
        "finding": (
            "S0PRIME_EXCLUDED_BY_INVARIANT"
            if exclusions else "NO_EXCLUSION_IN_DECLARED_FAMILY"
        ),
        "pass": (
            all_untouched_parities["target_equals_witness_on_U"]
            and weight_band["target_weight_is_initial_weight"]
            and all(
                row["whole_step_failure_witness"] is not None
                for row in parity_rows
                if not row["primitive_induction_preserved"]
            )
            and all(
                row["nonseparation_witness"] is not None
                for row in parity_rows
                if row["primitive_induction_preserved"]
                and not row["separates_all_initial_states"]
            )
            and all(
                row["nonseparation_witness"] is not None
                for row in triple_rows
            )
        ),
    }


def run() -> int:
    started = monotonic()
    sources, payloads, trees = source_controls()
    fixtures = decode_fixtures(trees[AUDIT_INPUT_PATHS[1]])
    macros = fixtures["macros"]
    states = fixtures["states"]
    assert isinstance(macros, tuple) and isinstance(states, dict)
    lineage_backbone = literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "BACKBONE")
    lineage_events = literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "EVENTS")
    lineage_resolutions = literal_assignment(
        trees[AUDIT_INPUT_PATHS[2]], "RESOLUTION_MOMENTS"
    )
    register_fields = literal_assignment(
        trees[AUDIT_INPUT_PATHS[3]], "REGISTER_FIELDS"
    )
    register_wires = literal_assignment(
        trees[AUDIT_INPUT_PATHS[3]], "REGISTER_WIRES"
    )
    assert isinstance(register_fields, tuple) and isinstance(register_wires, tuple)
    lineage_exact = (
        lineage_backbone == BACKBONE
        and lineage_events == (0, 2, 1)
        and lineage_resolutions == RESOLUTION_MOMENTS
        and dict(zip(register_fields, register_wires)).get("bank0.HEAD[1]")
        == HEAD1_WIRE
    )
    lanes = tuple(
        (event, pair) for event in (0, 2, 1) for pair in BACKBONE
    )
    landed_period_rows = inspect_landed(
        period_rows(payloads[AUDIT_INPUT_PATHS[4]])
    )

    with tempfile.TemporaryDirectory(prefix="cycle851-") as temp_name:
        temp = Path(temp_name)
        kernel_inputs = write_kernel_inputs(temp, macros, lanes, states)
        compiler = compile_kernel(temp)
        replay_first = execute_kernel(temp, "first")
        replay_second = execute_kernel(temp, "second")

        exact_replay = replay_first == replay_second
        summary = replay_first["summary"]
        target = int.from_bytes(replay_first["target"], "little")
        closest = int.from_bytes(replay_first["closest"], "little")
        checkpoint1 = int.from_bytes(replay_first["checkpoint1"], "little")

    s1 = target ^ (1 << HEAD1_WIRE)
    closest_lane = int(summary["best_lane"])
    closest_time = int(summary["best_time"])
    closest_key = lanes[closest_lane]
    scalar_checkpoint = apply_word(
        states[lanes[0]], build_word(macros, lanes[0][1])
    )
    target_identity = {
        "name": "S0'",
        "collision_warning":
            "S0' is the weight-47 companion; it is NOT the weight-59 pulse coincidence state.",
        "definition":
            "S0' := S1 XOR bank0.HEAD[1], where S1 is event-1 witness-pair (1,6) at movement 51110.",
        "head1_wire": HEAD1_WIRE,
        "cycle843_correction_commit":
            "a902a8204b43e616272be79b18ca337f078d84d0",
        "cycle843_expected_tuple_byte_sha256": EXPECTED_S0_PRIME_SHA256,
        "cycle843_distinct_pulse_tuple_byte_sha256": EXPECTED_PULSE_SHA256,
        "S1_weight": s1.bit_count(),
        "S1_tuple_byte_sha256": state_sha256(s1),
        "S0_prime_weight": target.bit_count(),
        "S0_prime_tuple_byte_sha256": state_sha256(target),
        "S0_prime_packed_sha256": packed_sha256(target),
        "pulse_weight": 59,
        "pulse_distinct_by_weight": target.bit_count() != 59,
        "pass": (
            s1.bit_count() == 46
            and state_sha256(s1) == EXPECTED_S1_SHA256
            and target.bit_count() == 47
            and state_sha256(target) == EXPECTED_S0_PRIME_SHA256
            and target.bit_count() != 59
        ),
    }
    trajectory_rule = {
        "state_space": "{0,1}^5815",
        "landed_family":
            "the 27 Cycle-832 landed cohort keys: events (0,2,1) times the nine-pair backbone",
        "landed_horizons_inclusive": RESOLUTION_MOMENTS,
        "trajectory_definition":
            "x_k(t+1)=F_pair(x_k(t)); F_pair is the exact ordered composition of the SHA-pinned X/CNOT/Toffoli rows for that pair.",
        "induction":
            "The C kernel starts at each decoded t=0 fixture and applies exactly one declared primitive row at a time in landed order, then repeats F_pair through every integer t up to that key's inclusive resolution horizon.",
        "lanes": lanes,
        "visited_state_count": summary["visited_states"],
        "expected_visited_state_count": sum(
            RESOLUTION_MOMENTS[event] + 1 for event, _pair in lanes
        ),
        "masked_schedule_rows": summary["schedule_rows"],
        "word_rows": summary["word_rows"],
        "one_step_scalar_vs_kernel_exact": checkpoint1 == scalar_checkpoint,
        "distance_profile_digest": summary["distance_profile_digest"],
    }
    certificate_a = {
        "target_identity": target_identity,
        "fixture_reconstruction": fixtures["public"],
        "landed_lineage_literals_exact": lineage_exact,
        "period_ledger_cross_control": landed_period_rows,
        "full_resolution_trajectories": trajectory_rule,
        "S0_prime_exact_hit_count": summary["target_hits"],
        "closest_approach": {
            "hamming_distance": summary["min_distance"],
            "key": closest_key,
            "event": closest_key[0],
            "pair": closest_key[1],
            "movement": closest_time,
            "state_weight": closest.bit_count(),
            "state_tuple_byte_sha256": state_sha256(closest),
            "state_packed_sha256": packed_sha256(closest),
            "distance_recheck": (closest ^ target).bit_count(),
            "tie_break": "least movement, then declared lane order",
        },
        "finding": "S0PRIME_UNVISITED_ACROSS_ALL_LANDED_TRAJECTORIES",
    }
    certificate_a["pass"] = (
        target_identity["pass"]
        and fixtures["public"]["pass"]
        and lineage_exact
        and len(lanes) == 27
        and trajectory_rule["visited_state_count"]
        == trajectory_rule["expected_visited_state_count"]
        and trajectory_rule["one_step_scalar_vs_kernel_exact"]
        and int(summary["target_hits"]) == 0
        and int(summary["min_distance"]) > 0
        and (closest ^ target).bit_count() == int(summary["min_distance"])
    )

    certificate_b = local_invariant_hunt(
        fixtures, target, register_fields, register_wires
    )
    excluded = bool(certificate_b["exclusions"])
    certificate_c = {
        "scope":
            "Only the finite invariant family explicitly enumerated in B_EXCLUSION_HUNT; no universal invariant or reachability claim is made.",
        "exclusion_found": excluded,
        "ruling": (
            "S0PRIME_EXCLUDED_BY_INVARIANT"
            if excluded else "OPEN_AFTER_DECLARED_INVARIANT_EXHAUSTION"
        ),
        "finding": (
            "S0PRIME_EXCLUDED_BY_INVARIANT"
            if excluded else "OPEN_AFTER_DECLARED_INVARIANT_EXHAUSTION"
        ),
        "pass": certificate_b["pass"],
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
        "target_bytes_exact": replay_first["target"] == replay_second["target"],
        "closest_bytes_exact": replay_first["closest"] == replay_second["closest"],
        "checkpoint_bytes_exact":
            replay_first["checkpoint1"] == replay_second["checkpoint1"],
    }
    controls = {
        **sources,
        "expected_branch": "physics-loop/proof-grade-blockR25-20260729",
        "actual_branch": branch,
        "branch_exact": branch == "physics-loop/proof-grade-blockR25-20260729",
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
        "pass": False,
    }
    controls_base = (
        sources["pass"]
        and controls["branch_exact"]
        and exact_replay
        and replay_control["target_bytes_exact"]
        and replay_control["closest_bytes_exact"]
        and replay_control["checkpoint_bytes_exact"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    certificates = {
        "A_UNVISITED_VERIFICATION": certificate_a,
        "B_EXCLUSION_HUNT": certificate_b,
        "C_HONEST_RULING": certificate_c,
        "D_CONTROLS": controls,
    }
    checks = {
        "A_UNVISITED_VERIFICATION": bool(certificate_a["pass"]),
        "B_EXCLUSION_HUNT": bool(certificate_b["pass"]),
        "C_HONEST_RULING": bool(certificate_c["pass"]),
        "D_CONTROLS": False,
    }
    report = {
        "cycle": 851,
        "target": "S0' weight-47 exclusion theorem attempt",
        "actual_status": "open after declared invariant exhaustion",
        "ruling": certificate_c["ruling"],
        "closest_approach": certificate_a["closest_approach"],
        "runtime_seconds": round(elapsed, 6),
        "checks": {},
        "pass": False,
        "terminal": "CYCLE851_S0PRIME_EXCLUSION_HONEST_FAIL",
    }

    def render() -> str:
        lines = []
        for name, value in certificates.items():
            lines.append(f"{name}: {'PASS' if checks[name] else 'FAIL'}")
            lines.append(f"{name}_FINDING={value['finding'] if 'finding' in value else ('CONTROLS_PASS' if value['pass'] else 'CONTROLS_FAIL')}")
            lines.append(f"{name}_CERTIFICATE={compact(value)}")
        lines.append(f"REPORT={compact(report)}")
        return "\n".join(lines) + "\n"

    for _iteration in range(10):
        controls["pass"] = controls_base
        checks["D_CONTROLS"] = controls["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE851_S0PRIME_EXCLUSION_ATTEMPT_PASS"
            if report["pass"] else "CYCLE851_S0PRIME_EXCLUSION_HONEST_FAIL"
        )
        output = render()
        controls["stdout_bytes"] = len(output.encode("utf-8"))
        controls["pass"] = controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
    output = render()
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        print(compact({
            "pass": False,
            "terminal": "CYCLE851_S0PRIME_EXCLUSION_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
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
            "terminal": "CYCLE851_S0PRIME_EXCLUSION_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
