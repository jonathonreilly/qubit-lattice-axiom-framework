#!/usr/bin/env python3
"""Independent checker for the bounded Cycle 764 b=6 completion claim.

The Cycle 764 primary is parsed only as AST data.  Its two declared landed
inputs are imported under their requested names.  Residual C_43 masks are
streamed by an independently implemented C helper, and every one is checked
at all 43 controller boundaries using the literal controller's independently
compiled two-rail transfer map.
"""
from __future__ import annotations

import ast
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from math import comb
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from time import perf_counter

sys.dont_write_bytecode = True

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle740_table_parameterized_mapper_2026_07_28 as M740


AUDIT_TIMEOUT_SEC = 3000
NOTE_PATH = "docs/B6_ANCHOR_COMPLETION_CYCLE764_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)

PRIMARY_PATH = "scripts/frontier_cycle764_b6_anchor_completion_2026_07_28.py"
PRIMARY_MODULE = "frontier_cycle764_b6_anchor_completion_2026_07_28"
STDOUT_LIMIT_BYTES = 150 * 1024
STATIONS = 43
RESIDUAL_K_MIN = 12
RESIDUAL_K_MAX = 21
BANK_COUNT = 6
CAPACITY = 6
SWEEP_WORKERS = 4
EXPECTED_RESIDUAL_COUNTS = (
    195_747_825,
    171_655_785,
    115_000_920,
    57_500_460,
    20_764_055,
    5_167_525,
    826_804,
    76_153,
    3_311,
    43,
)
EXPECTED_FROZEN_CONFIGURATIONS = 402_580_148
EXPECTED_RESIDUAL_CONFIGURATIONS = 566_742_881
EXPECTED_LUCAS_43 = 969_323_029
EXPECTED_FROZEN_STEPS = 17_310_946_364
EXPECTED_RESIDUAL_STEPS = 24_369_943_883
EXPECTED_FULL_STEPS = 41_680_890_247
COMPLETION_LANGUAGE = (
    "Cycle 764 completes only the finite b=6,n=43 anchor by joining "
    "the retained Cycle 761 k<=11 package to the newly swept "
    "k=12..21 residual; it does not alter Cycle 740's conditional "
    "general-b claim."
)

CHECKS: dict[str, bool] = {}
LINES: list[str] = []
ERRORS: dict[str, str] = {}


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def assigned_literal(tree: ast.Module, name: str) -> object:
    """Return one top-level assignment using ast.literal_eval only."""

    matches: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("literal assignment", name, len(matches)))
    return ast.literal_eval(matches[0])


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function", name, len(matches)))
    return matches[0]


def returned_literal(tree: ast.Module, function: str, key: str) -> object:
    """Literal-evaluate a named key in a function's sole returned dict."""

    returned = [
        node.value
        for node in ast.walk(function_node(tree, function))
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returned) != 1:
        raise AssertionError(("returned dict", function, len(returned)))
    values: list[ast.AST] = []
    for key_node, value_node in zip(returned[0].keys, returned[0].values):
        if key_node is not None and ast.literal_eval(key_node) == key:
            values.append(value_node)
    if len(values) != 1:
        raise AssertionError(("returned key", function, key, len(values)))
    return ast.literal_eval(values[0])


def _literal_return_dict(tree: ast.Module, function: str) -> dict[str, object]:
    returned = [
        node.value
        for node in ast.walk(function_node(tree, function))
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returned) != 1:
        raise AssertionError(("literal return dict", function, len(returned)))
    value = ast.literal_eval(returned[0])
    if not isinstance(value, dict):
        raise AssertionError(("not dict", function))
    return value


def extraction() -> dict[str, object]:
    """Extract the primary's census claims as inert, literal AST data."""

    source = Path(PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    names = (
        "AUDIT_TIMEOUT_SEC",
        "NOTE_PATH",
        "AUDIT_INPUT_PATHS",
        "STATIONS",
        "RESIDUAL_K_MIN",
        "RESIDUAL_K_MAX",
        "EXPECTED_LUCAS_43",
        "EXPECTED_FROZEN_CONFIGURATIONS",
        "EXPECTED_RESIDUAL_CONFIGURATIONS",
        "EXPECTED_FROZEN_STATION_STEPS",
        "EXPECTED_RESIDUAL_STATION_STEPS",
        "EXPECTED_FULL_STATION_STEPS",
        "EXPECTED_RESIDUAL_COUNTS",
        "ZERO_FAILURE_KEYS",
    )
    literals = {name: assigned_literal(tree, name) for name in names}
    empty_stats = _literal_return_dict(tree, "empty_sweep_stats")
    zero_keys = tuple(literals["ZERO_FAILURE_KEYS"])
    zero_census = {key: empty_stats[key] for key in zero_keys}

    near_function = function_node(tree, "near_miss_certificate")
    near_literals = [
        ast.literal_eval(node)
        for node in ast.walk(near_function)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and node.value == 860
    ]
    completion_language = returned_literal(
        tree, "keys_certificate", "honest_boundary"
    )
    expected_tuple = (
        EXPECTED_RESIDUAL_CONFIGURATIONS,
        EXPECTED_RESIDUAL_STEPS,
        EXPECTED_LUCAS_43,
        EXPECTED_FROZEN_CONFIGURATIONS,
        EXPECTED_FROZEN_STEPS,
        EXPECTED_FULL_STEPS,
        EXPECTED_RESIDUAL_COUNTS,
    )
    observed_tuple = (
        literals["EXPECTED_RESIDUAL_CONFIGURATIONS"],
        literals["EXPECTED_RESIDUAL_STATION_STEPS"],
        literals["EXPECTED_LUCAS_43"],
        literals["EXPECTED_FROZEN_CONFIGURATIONS"],
        literals["EXPECTED_FROZEN_STATION_STEPS"],
        literals["EXPECTED_FULL_STATION_STEPS"],
        literals["EXPECTED_RESIDUAL_COUNTS"],
    )
    arithmetic = {
        "configurations": (
            int(literals["EXPECTED_FROZEN_CONFIGURATIONS"])
            + int(literals["EXPECTED_RESIDUAL_CONFIGURATIONS"])
        ),
        "station_steps": (
            int(literals["EXPECTED_FROZEN_STATION_STEPS"])
            + int(literals["EXPECTED_RESIDUAL_STATION_STEPS"])
        ),
    }
    exact = (
        observed_tuple == expected_tuple
        and literals["AUDIT_TIMEOUT_SEC"] == AUDIT_TIMEOUT_SEC
        and literals["NOTE_PATH"] == NOTE_PATH
        and literals["AUDIT_INPUT_PATHS"] == AUDIT_INPUT_PATHS
        and literals["STATIONS"] == STATIONS
        and literals["RESIDUAL_K_MIN"] == RESIDUAL_K_MIN
        and literals["RESIDUAL_K_MAX"] == RESIDUAL_K_MAX
        and zero_census
        and all(value == 0 for value in zero_census.values())
        and near_literals == [860]
        and arithmetic["configurations"] == EXPECTED_LUCAS_43
        and arithmetic["station_steps"] == EXPECTED_FULL_STEPS
        and completion_language == COMPLETION_LANGUAGE
    )
    return {
        "primary_read_as_data_only": True,
        "primary_imported": PRIMARY_MODULE in sys.modules,
        "primary_source_sha256": sha256(source.encode()).hexdigest(),
        "residual_configurations": observed_tuple[0],
        "residual_station_steps": observed_tuple[1],
        "zero_violation_census": zero_census,
        "near_miss_controls": near_literals[0] if near_literals else None,
        "completion_arithmetic": arithmetic,
        "completion_language": completion_language,
        "exact": exact,
    }


def path_counts(length: int) -> tuple[int, ...]:
    """Independence polynomial coefficients for a path, by recurrence."""

    previous_previous = [1]
    if length == 0:
        return tuple(previous_previous)
    previous = [1, 1]
    for _ in range(2, length + 1):
        current = [0] * max(len(previous), len(previous_previous) + 1)
        for degree, value in enumerate(previous):
            current[degree] += value
        for degree, value in enumerate(previous_previous):
            current[degree + 1] += value
        previous_previous, previous = previous, current
    return tuple(previous)


def cycle_counts(stations: int) -> tuple[int, ...]:
    """Split on station zero and combine two independently counted paths."""

    station_zero_absent = path_counts(stations - 1)
    station_zero_present = path_counts(stations - 3)
    result = [0] * (stations // 2 + 1)
    for degree, value in enumerate(station_zero_absent):
        if degree < len(result):
            result[degree] += value
    for degree, value in enumerate(station_zero_present):
        if degree + 1 < len(result):
            result[degree + 1] += value
    return tuple(result)


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(int(wire) for wire in gate.wires)


def controller_transfer_certificate() -> dict[str, object]:
    """Compile the literal C=6 word to its exact rail transfer, independently."""

    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    data_width = M740.parameterized_data_width(CAPACITY)
    controller = M740.parameterized_controller_word(
        program, data_width, CAPACITY
    )
    rail_base = data_width
    b_base = rail_base + STATIONS
    work_base = b_base + STATIONS
    width = work_base + STATIONS
    first_rail_target = next(
        index
        for index, gate in enumerate(controller)
        if rail_base <= int(gate.wires[-1]) < work_base
    )
    q_word = controller[:first_rail_target]
    rail_word = controller[first_rail_target:]

    structural_failures = 0
    work_blocks = 0
    index = 0
    while index < len(q_word):
        gate = q_word[index]
        wires = tuple(int(wire) for wire in gate.wires)
        structural_failures += int(
            not wires or any(wire < 0 or wire >= width for wire in wires)
        )
        target = wires[-1]
        structural_failures += int(rail_base <= target < work_base)
        if work_base <= target < width:
            if index + 2 >= len(q_word):
                structural_failures += 1
                index += 1
                continue
            middle = q_word[index + 1]
            closing = q_word[index + 2]
            middle_wires = tuple(int(wire) for wire in middle.wires)
            exact_block = (
                gate_signature(gate) == gate_signature(closing)
                and gate.kind == "TOF"
                and middle.kind == "TOF"
                and target in middle_wires[:-1]
                and middle_wires[-1] < data_width
                and middle_wires[-1] not in wires[:-1]
                and rail_base <= wires[0] < b_base
                and target - work_base == wires[0] - rail_base
            )
            structural_failures += int(not exact_block)
            work_blocks += int(exact_block)
            index += 3
        else:
            structural_failures += sum(
                work_base <= wire < width for wire in wires
            )
            index += 1

    symbolic = [1 << index for index in range(2 * STATIONS)]
    rail_gate_failures = 0
    for gate in rail_word:
        wires = tuple(int(wire) for wire in gate.wires)
        valid = (
            gate.kind == "CNOT"
            and len(wires) == 2
            and all(rail_base <= wire < work_base for wire in wires)
            and wires[0] != wires[1]
        )
        rail_gate_failures += int(not valid)
        if valid:
            control, target = (
                wires[0] - rail_base,
                wires[1] - rail_base,
            )
            symbolic[target] ^= symbolic[control]

    expected = []
    for station in range(STATIONS):
        expected.append(1 << ((station - 1) % STATIONS))
    for station in range(STATIONS):
        expected.append(1 << (STATIONS + (station + 1) % STATIONS))
    transfer_exact = tuple(symbolic) == tuple(expected)
    table_law = M740.table_law_certificate()
    equivalence = M740.equivalence_certificate()
    exact = (
        len(program) == STATIONS
        and program == K.interleaved_program(BANK_COUNT)
        and data_width == 2_737
        and len(controller) == 28_532
        and first_rail_target == len(q_word)
        and len(rail_word) == 6 * STATIONS
        and structural_failures == rail_gate_failures == 0
        and work_blocks > 0
        and transfer_exact
        and table_law["exact"]
        and equivalence["exact"]
        and equivalence["all_byte_identical"]
    )
    return {
        "program_stations": len(program),
        "data_width": data_width,
        "controller_gates": len(controller),
        "q_gates": len(q_word),
        "rail_gates": len(rail_word),
        "clean_work_compute_act_uncompute_blocks": work_blocks,
        "controller_word_sha256": K.gate_digest(controller),
        "q_never_targets_A_or_B": structural_failures == 0,
        "blank_work_returns_blank_universally": structural_failures == 0,
        "compiled_transfer": "A'[s]=A[s-1], B'[s]=B[s+1]",
        "compiled_transfer_exact": transfer_exact,
        "exact": exact,
    }


STREAM_EVALUATOR_C = r"""
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define N 43
#define RING ((UINT64_C(1) << N) - UINT64_C(1))

typedef struct {
    uint64_t configurations;
    uint64_t station_steps;
    uint64_t input_popcount_failures;
    uint64_t input_adjacency_failures;
    uint64_t translation_failures;
    uint64_t token_count_failures;
    uint64_t adjacency_failures;
    uint64_t ownership_failures;
    uint64_t distance_failures;
    uint64_t b_rail_failures;
    uint64_t closure_failures;
    uint64_t trace;
} Stats;

static inline uint64_t rotl43(uint64_t value) {
    return ((value << 1) & RING) | (value >> (N - 1));
}

static inline uint64_t rotr43(uint64_t value) {
    return (value >> 1) | ((value & UINT64_C(1)) << (N - 1));
}

static inline uint64_t mix64(uint64_t value) {
    value ^= value >> 30;
    value *= UINT64_C(0xbf58476d1ce4e5b9);
    value ^= value >> 27;
    value *= UINT64_C(0x94d049bb133111eb);
    return value ^ (value >> 31);
}

static inline uint64_t spread_combination(uint64_t combination) {
    uint64_t output = 0;
    unsigned rank = 0;
    while (combination) {
        unsigned position = (unsigned)__builtin_ctzll(combination);
        output |= UINT64_C(1) << (position + rank);
        combination &= combination - 1;
        ++rank;
    }
    return output;
}

static inline void evaluate_mask(uint64_t mask, unsigned occupied, Stats *stats) {
    volatile uint64_t a = mask;
    volatile uint64_t b = 0;
    uint64_t expected = mask;
    stats->configurations += 1;
    stats->input_popcount_failures +=
        (uint64_t)(__builtin_popcountll(mask) != (int)occupied);
    stats->input_adjacency_failures += (uint64_t)((mask & rotl43(mask)) != 0);
    for (unsigned step = 0; step < N; ++step) {
        uint64_t observed_a = a;
        uint64_t observed_b = b;
        uint64_t translation_bad = observed_a ^ expected;
        uint64_t adjacent_bad = observed_a & rotl43(observed_a);
        stats->translation_failures += (uint64_t)(translation_bad != 0);
        stats->token_count_failures +=
            (uint64_t)(__builtin_popcountll(observed_a) != (int)occupied);
        stats->adjacency_failures += (uint64_t)(adjacent_bad != 0);
        stats->ownership_failures += (uint64_t)(adjacent_bad != 0);
        stats->distance_failures += (uint64_t)(translation_bad != 0);
        stats->b_rail_failures += (uint64_t)(observed_b != 0);
        stats->trace ^= mix64(
            observed_a
            ^ (expected << 7)
            ^ ((uint64_t)step << 51)
            ^ stats->configurations
        );
        a = rotl43(observed_a);
        b = rotr43(observed_b);
        expected = rotl43(expected);
        stats->station_steps += 1;
    }
    stats->closure_failures += (uint64_t)(a != mask || b != 0);
}

static inline uint64_t next_combination(uint64_t value) {
    uint64_t low = value & (UINT64_C(0) - value);
    uint64_t raised = value + low;
    unsigned shift = (unsigned)__builtin_ctzll(low) + 2;
    return raised + ((raised ^ value) >> shift);
}

static void stream_path(
    unsigned start,
    unsigned length,
    unsigned occupied,
    uint64_t forced,
    Stats *stats
) {
    if (occupied == 0) {
        evaluate_mask(forced, (unsigned)__builtin_popcountll(forced), stats);
        return;
    }
    unsigned universe = length - occupied + 1;
    uint64_t combination = (UINT64_C(1) << occupied) - 1;
    uint64_t limit = UINT64_C(1) << universe;
    unsigned total_occupied = occupied + (unsigned)__builtin_popcountll(forced);
    while (combination < limit) {
        uint64_t mask = (spread_combination(combination) << start) | forced;
        evaluate_mask(mask, total_occupied, stats);
        combination = next_combination(combination);
    }
}

int main(int argc, char **argv) {
    if (argc != 2) return 64;
    int occupied = atoi(argv[1]);
    if (occupied < 12 || occupied > 21) return 65;
    Stats stats = {0};
    stream_path(1, N - 1, (unsigned)occupied, 0, &stats);
    stream_path(2, N - 3, (unsigned)(occupied - 1), 1, &stats);
    printf(
        "%d %" PRIu64 " %" PRIu64 " %" PRIu64 " %" PRIu64
        " %" PRIu64 " %" PRIu64 " %" PRIu64 " %" PRIu64
        " %" PRIu64 " %" PRIu64 " %" PRIu64 " %016" PRIx64 "\n",
        occupied,
        stats.configurations,
        stats.station_steps,
        stats.input_popcount_failures,
        stats.input_adjacency_failures,
        stats.translation_failures,
        stats.token_count_failures,
        stats.adjacency_failures,
        stats.ownership_failures,
        stats.distance_failures,
        stats.b_rail_failures,
        stats.closure_failures,
        stats.trace
    );
    return 0;
}
"""


def compile_stream_evaluator(directory: str) -> str:
    source_path = Path(directory) / "cycle764_independent_stream.c"
    executable_path = Path(directory) / "cycle764_independent_stream"
    source_path.write_text(STREAM_EVALUATOR_C, encoding="utf-8")
    command = (
        os.environ.get("CC", "cc"),
        "-O3",
        "-std=c11",
        "-DNDEBUG",
        str(source_path),
        "-o",
        str(executable_path),
    )
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"C evaluator compile failed ({result.returncode}): "
            f"{result.stderr[-2000:]}"
        )
    return str(executable_path)


SWEEP_FIELDS = (
    "k",
    "configurations",
    "station_steps",
    "input_popcount_failures",
    "input_adjacency_failures",
    "translation_failures",
    "token_count_failures",
    "adjacency_failures",
    "ownership_failures",
    "distance_failures",
    "b_rail_failures",
    "closure_failures",
    "trace",
)


def run_stratum(executable: str, occupied: int) -> dict[str, object]:
    started = perf_counter()
    result = subprocess.run(
        (executable, str(occupied)),
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC - 120,
        check=False,
    )
    elapsed = perf_counter() - started
    if result.returncode != 0:
        raise RuntimeError(
            f"k={occupied} evaluator failed ({result.returncode}): "
            f"{result.stderr[-2000:]}"
        )
    pieces = result.stdout.strip().split()
    if len(pieces) != len(SWEEP_FIELDS):
        raise AssertionError(("helper output", occupied, pieces))
    row: dict[str, object] = {}
    for name, piece in zip(SWEEP_FIELDS, pieces):
        row[name] = piece if name == "trace" else int(piece)
    row["elapsed_seconds"] = round(elapsed, 6)
    return row


def strata_recount() -> dict[str, object]:
    """Stream each residual stratum once; retain counts and sweep evidence."""

    started = perf_counter()
    with tempfile.TemporaryDirectory(prefix="cycle764-independent-") as directory:
        executable = compile_stream_evaluator(directory)
        with ThreadPoolExecutor(max_workers=SWEEP_WORKERS) as executor:
            rows = tuple(executor.map(
                lambda occupied: run_stratum(executable, occupied),
                range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1),
            ))
    elapsed = perf_counter() - started
    rows = tuple(sorted(rows, key=lambda row: int(row["k"])))
    streamed_counts = tuple(int(row["configurations"]) for row in rows)
    recurrence_counts = cycle_counts(STATIONS)
    residual_recurrence = recurrence_counts[
        RESIDUAL_K_MIN:RESIDUAL_K_MAX + 1
    ]
    frozen_total = sum(recurrence_counts[:RESIDUAL_K_MIN])
    residual_total = sum(streamed_counts)
    exact = (
        streamed_counts == residual_recurrence == EXPECTED_RESIDUAL_COUNTS
        and frozen_total == EXPECTED_FROZEN_CONFIGURATIONS
        and residual_total == EXPECTED_RESIDUAL_CONFIGURATIONS
        and sum(recurrence_counts) == EXPECTED_LUCAS_43
    )
    return {
        "counts_by_k": dict(zip(
            range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1),
            streamed_counts,
        )),
        "streamed_residual_total": residual_total,
        "recurrence_frozen_total": frozen_total,
        "recurrence_L43_total": sum(recurrence_counts),
        "split_reproduced": exact,
        "rows": rows,
        "runtime_seconds": round(elapsed, 6),
        "exact": exact,
    }


def sweep_recount(
    strata: dict[str, object],
    controller: dict[str, object],
) -> dict[str, object]:
    """Audit all boundary evaluations produced during the streamed recount."""

    rows = tuple(strata["rows"])
    failure_keys = (
        "input_popcount_failures",
        "input_adjacency_failures",
        "translation_failures",
        "token_count_failures",
        "adjacency_failures",
        "ownership_failures",
        "distance_failures",
        "b_rail_failures",
        "closure_failures",
    )
    failures = {
        key: sum(int(row[key]) for row in rows)
        for key in failure_keys
    }
    configurations = sum(int(row["configurations"]) for row in rows)
    station_steps = sum(int(row["station_steps"]) for row in rows)
    elapsed = float(strata["runtime_seconds"])
    exact = (
        controller["exact"]
        and strata["exact"]
        and configurations == EXPECTED_RESIDUAL_CONFIGURATIONS
        and station_steps == EXPECTED_RESIDUAL_STEPS
        and all(value == 0 for value in failures.values())
        and all(str(row["trace"]) != "0000000000000000" for row in rows)
    )
    return {
        "evaluator": (
            "independent streamed C enumerator; literal controller rail word "
            "compiled to A'[s]=A[s-1], B'[s]=B[s+1]"
        ),
        "configurations": configurations,
        "station_steps": station_steps,
        "zero_violation_census": failures,
        "work_failures": (
            0 if controller["blank_work_returns_blank_universally"] else 1
        ),
        "station_steps_per_second": round(station_steps / elapsed, 3),
        "runtime_seconds": elapsed,
        "exact": exact,
    }


def rotate(mask: int, shift: int) -> int:
    ring = (1 << STATIONS) - 1
    shift %= STATIONS
    return ((mask << shift) & ring) | (mask >> (STATIONS - shift))


def near_miss_recount() -> dict[str, object]:
    """Construct two one-edge controls for every residual k and cycle edge."""

    controls = 0
    failures = 0
    ownership_incidences = 0
    per_k: dict[int, int] = {}
    digest = sha256()
    for occupied in range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1):
        k_controls = 0
        for left in range(STATIONS):
            right = (left + 1) % STATIONS
            for phase in (0, 1):
                mask = (1 << left) | (1 << right)
                offset = 3 + phase
                for ordinal in range(occupied - 2):
                    mask |= 1 << (
                        (left + offset + 2 * ordinal) % STATIONS
                    )
                adjacent_edges = tuple(
                    station
                    for station in range(STATIONS)
                    if (
                        ((mask >> station) & 1)
                        and ((mask >> ((station + 1) % STATIONS)) & 1)
                    )
                )
                violating_sites = tuple(
                    station
                    for station in range(STATIONS)
                    if (
                        ((mask >> station) & 1)
                        and (
                            ((mask >> ((station - 1) % STATIONS)) & 1)
                            or ((mask >> ((station + 1) % STATIONS)) & 1)
                        )
                    )
                )
                exact_row = (
                    mask.bit_count() == occupied
                    and adjacent_edges == (left,)
                    and set(violating_sites) == {left, right}
                    and len(violating_sites) == 2
                )
                failures += int(not exact_row)
                ownership_incidences += len(violating_sites)
                controls += 1
                k_controls += 1
                digest.update(
                    f"{occupied}:{left}:{phase}:{mask};".encode()
                )
        per_k[occupied] = k_controls
    exact = (
        controls == 860
        and set(per_k.values()) == {86}
        and ownership_incidences == 1_720
        and failures == 0
    )
    return {
        "controls": controls,
        "controls_by_k": per_k,
        "ownership_violation_incidences": ownership_incidences,
        "failures": failures,
        "rows_sha256": digest.hexdigest(),
        "exact": exact,
    }


def completion_audit(
    extraction_report: dict[str, object],
    strata: dict[str, object],
    sweep: dict[str, object],
) -> dict[str, object]:
    """Give the set partition argument and independently redo both sums."""

    frozen_strata = frozenset(range(0, RESIDUAL_K_MIN))
    residual_strata = frozenset(
        range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1)
    )
    all_possible_strata = frozenset(range(0, STATIONS // 2 + 1))
    disjoint = frozen_strata.isdisjoint(residual_strata)
    union_exact = frozen_strata | residual_strata == all_possible_strata
    set_level_argument = (
        "Let L_k(43)={m in L(43): popcount(m)=k}. The retained package is "
        "the disjoint union of L_k(43) for 0<=k<=11; the residual package "
        "is the disjoint union for 12<=k<=21. Distinct popcounts make the "
        "packages disjoint, and alpha(C_43)=floor(43/2)=21 makes their union "
        "all of L(43)."
    )
    configurations = (
        EXPECTED_FROZEN_CONFIGURATIONS
        + int(strata["streamed_residual_total"])
    )
    station_steps = EXPECTED_FROZEN_STEPS + int(sweep["station_steps"])
    exact = (
        extraction_report["exact"]
        and strata["exact"]
        and sweep["exact"]
        and disjoint
        and union_exact
        and configurations
        == EXPECTED_FROZEN_CONFIGURATIONS
        + EXPECTED_RESIDUAL_CONFIGURATIONS
        == EXPECTED_LUCAS_43
        and station_steps
        == EXPECTED_FROZEN_STEPS
        + EXPECTED_RESIDUAL_STEPS
        == EXPECTED_FULL_STEPS
    )
    return {
        "set_level_argument": set_level_argument,
        "frozen_strata": tuple(sorted(frozen_strata)),
        "residual_strata": tuple(sorted(residual_strata)),
        "disjoint": disjoint,
        "union_is_all_L43": union_exact,
        "configuration_arithmetic": (
            f"{EXPECTED_FROZEN_CONFIGURATIONS}+"
            f"{EXPECTED_RESIDUAL_CONFIGURATIONS}={configurations}"
        ),
        "station_step_arithmetic": (
            f"{EXPECTED_FROZEN_STEPS}+"
            f"{EXPECTED_RESIDUAL_STEPS}={station_steps}"
        ),
        "exact": exact,
    }


def discipline(extraction_report: dict[str, object]) -> dict[str, object]:
    """Enforce the primary-import blocklist and verbatim boundary language."""

    blocklist_clean = (
        PRIMARY_MODULE not in sys.modules
        and getattr(K, "__name__", "") == AUDIT_INPUT_PATHS[0][8:-3]
        and getattr(M740, "__name__", "") == AUDIT_INPUT_PATHS[1][8:-3]
        and PRIMARY_PATH not in AUDIT_INPUT_PATHS
    )
    language_verbatim = (
        extraction_report["completion_language"] == COMPLETION_LANGUAGE
    )
    return {
        "blocklisted_primary_module": PRIMARY_MODULE,
        "primary_imported": PRIMARY_MODULE in sys.modules,
        "blocklist_clean": blocklist_clean,
        "completion_language": COMPLETION_LANGUAGE,
        "completion_language_verbatim": language_verbatim,
        "exact": blocklist_clean and language_verbatim,
    }


def main() -> int:
    started = perf_counter()
    reports: dict[str, object] = {}

    check(
        "HEADER_timeout_note_and_pure_literal_inputs",
        AUDIT_TIMEOUT_SEC == 3000
        and NOTE_PATH
        == "docs/B6_ANCHOR_COMPLETION_CYCLE764_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
        ),
    )

    try:
        reports["extraction"] = extraction()
    except Exception as error:
        ERRORS["extraction"] = f"{type(error).__name__}: {error}"[:2000]
        reports["extraction"] = {
            "exact": False,
            "completion_language": None,
        }
    check("A_primary_AST_literal_extraction_exact", reports["extraction"]["exact"])

    try:
        reports["controller"] = controller_transfer_certificate()
    except Exception as error:
        ERRORS["controller"] = f"{type(error).__name__}: {error}"[:2000]
        reports["controller"] = {
            "exact": False,
            "blank_work_returns_blank_universally": False,
        }
    check(
        "B_literal_controller_independent_rail_compile_exact",
        reports["controller"]["exact"],
    )

    try:
        reports["strata"] = strata_recount()
    except Exception as error:
        ERRORS["strata"] = f"{type(error).__name__}: {error}"[:2000]
        reports["strata"] = {
            "exact": False,
            "rows": (),
            "streamed_residual_total": 0,
            "runtime_seconds": 0.0,
        }
    check(
        "C_streamed_k12_through_k21_strata_and_split_recount",
        reports["strata"]["exact"],
    )

    try:
        reports["sweep"] = sweep_recount(
            reports["strata"], reports["controller"]
        )
    except Exception as error:
        ERRORS["sweep"] = f"{type(error).__name__}: {error}"[:2000]
        reports["sweep"] = {
            "exact": False,
            "station_steps": 0,
            "station_steps_per_second": 0,
        }
    check(
        "D_all_24369943883_station_steps_zero_violations",
        reports["sweep"]["exact"],
    )

    try:
        reports["near_miss"] = near_miss_recount()
    except Exception as error:
        ERRORS["near_miss"] = f"{type(error).__name__}: {error}"[:2000]
        reports["near_miss"] = {"exact": False}
    check("E_all_860_near_miss_controls_exact", reports["near_miss"]["exact"])

    try:
        reports["completion"] = completion_audit(
            reports["extraction"],
            reports["strata"],
            reports["sweep"],
        )
    except Exception as error:
        ERRORS["completion"] = f"{type(error).__name__}: {error}"[:2000]
        reports["completion"] = {"exact": False}
    check(
        "F_two_packages_disjoint_and_union_all_L43",
        reports["completion"]["exact"],
    )

    try:
        reports["discipline"] = discipline(reports["extraction"])
    except Exception as error:
        ERRORS["discipline"] = f"{type(error).__name__}: {error}"[:2000]
        reports["discipline"] = {"exact": False}
    check(
        "G_blocklist_clean_and_completion_language_verbatim",
        reports["discipline"]["exact"],
    )

    elapsed = perf_counter() - started
    check("TIMEOUT_runtime_under_3000_seconds", elapsed < AUDIT_TIMEOUT_SEC)
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "reports": reports,
        "errors": ERRORS,
        "runtime_seconds": round(elapsed, 6),
        "checks": dict(sorted(CHECKS.items())),
    }
    provisional = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional.encode())
        + len("\n".join(LINES).encode())
        + 4096
        < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE764_COMPLETION_INDEPENDENT_CHECK_ALL_PASS"
        if report["pass"]
        else "CYCLE764_COMPLETION_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    text = "\n".join(LINES) + "\n" + json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        fallback = {
            "checks": report["checks"],
            "errors": ERRORS,
            "pass": False,
            "terminal": "CYCLE764_COMPLETION_INDEPENDENT_CHECK_HONEST_FAIL",
            "reason": "stdout bound exceeded",
        }
        text = "\n".join(LINES) + "\n" + json.dumps(
            fallback, sort_keys=True, separators=(",", ":")
        ) + "\n"
        sys.stdout.write(text)
        return 1
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
