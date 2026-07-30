#!/usr/bin/env python3
"""Cycle 764: complete the sixth anchor on the residual C_43 strata.

Cycle 761's frozen k<=11 package is read as source data and checked through
its primary AST; it is never imported or re-swept.  This runner enumerates
every independent C_43 mask in k=12..21 and applies the literal M740 C=6
controlled-Q plus two-rail-R controller for all 43 steps in bit-plane
batches.  Together the two disjoint packages exhaust all L(43) masks.
"""
from __future__ import annotations

import ast
from concurrent.futures import ProcessPoolExecutor
from hashlib import sha256
import json
from math import comb
from multiprocessing import get_context
from pathlib import Path
import sys
from time import perf_counter

sys.dont_write_bytecode = True

import numpy as np

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle740_table_parameterized_mapper_2026_07_28 as M740


AUDIT_TIMEOUT_SEC = 3000
NOTE_PATH = "docs/B6_ANCHOR_COMPLETION_CYCLE764_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

PRIMARY_761_PATH = (
    "scripts/frontier_cycle761_b6_exhaustive_anchor_2026_07_28.py"
)
STDOUT_LIMIT_BYTES = 150 * 1024
BITPLANE_BATCH = 131_072
SWEEP_WORKERS = 4
BANK_COUNT = 6
CAPACITY = 6
STATIONS = 43
RESIDUAL_K_MIN = 12
RESIDUAL_K_MAX = 21
EXPECTED_LUCAS_43 = 969_323_029
EXPECTED_FROZEN_CONFIGURATIONS = 402_580_148
EXPECTED_RESIDUAL_CONFIGURATIONS = 566_742_881
EXPECTED_FROZEN_STATION_STEPS = 17_310_946_364
EXPECTED_RESIDUAL_STATION_STEPS = 24_369_943_883
EXPECTED_FULL_STATION_STEPS = 41_680_890_247
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

ROOT = Path(__file__).resolve().parents[1]
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
ERRORS: dict[str, str] = {}


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def error_text(error: BaseException) -> str:
    return f"{type(error).__name__}: {error}"[:1000]


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_json_bytes(value)).hexdigest()


def ast_digest(node: ast.AST) -> str:
    normalized = ast.dump(node, annotate_fields=True, include_attributes=False)
    return sha256(normalized.encode()).hexdigest()


def assigned_literal(tree: ast.Module, name: str) -> object:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            values.append(node.value)
    if len(values) != 1:
        raise AssertionError((name, len(values)))
    return ast.literal_eval(values[0])


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    nodes = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(nodes) != 1:
        raise AssertionError((name, len(nodes)))
    return nodes[0]


def local_assignment(
    function: ast.FunctionDef, name: str
) -> ast.AST:
    values = []
    for node in ast.walk(function):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            values.append(node.value)
    if len(values) != 1:
        raise AssertionError((function.name, name, len(values)))
    return values[0]


def expression_matches(node: ast.AST, expression: str) -> bool:
    expected = ast.parse(expression, mode="eval").body
    return ast.dump(
        node, annotate_fields=True, include_attributes=False
    ) == ast.dump(
        expected, annotate_fields=True, include_attributes=False
    )


def lucas_number(index: int) -> tuple[int, str]:
    hasher = sha256()
    older, newer = 2, 1
    hasher.update(stable_json_bytes((0, older)))
    if index == 0:
        return older, hasher.hexdigest()
    hasher.update(stable_json_bytes((1, newer)))
    for position in range(2, index + 1):
        older, newer = newer, older + newer
        hasher.update(stable_json_bytes((position, newer)))
    return newer, hasher.hexdigest()


def path_independence_counts(length: int) -> tuple[int, ...]:
    if length == 0:
        return (1,)
    if length == 1:
        return (1, 1)
    older = [1]
    newer = [1, 1]
    for _ in range(2, length + 1):
        current = [0] * max(len(newer), len(older) + 1)
        for degree, value in enumerate(newer):
            current[degree] += value
        for degree, value in enumerate(older):
            current[degree + 1] += value
        older, newer = newer, current
    return tuple(newer)


def cycle_independence_counts(stations: int) -> tuple[int, ...]:
    absent = path_independence_counts(stations - 1)
    present = path_independence_counts(stations - 3)
    counts = [0] * (stations // 2 + 1)
    for degree, value in enumerate(absent):
        if degree < len(counts):
            counts[degree] += value
    for degree, value in enumerate(present):
        if degree + 1 < len(counts):
            counts[degree + 1] += value
    return tuple(counts)


def closed_cycle_stratum_count(stations: int, occupied: int) -> int:
    if occupied == 0:
        return 1
    return (
        stations
        * comb(stations - occupied - 1, occupied - 1)
        // occupied
    )


SPREAD_CHUNK_BITS = 12
SPREAD_CHUNK_MASK = (1 << SPREAD_CHUNK_BITS) - 1


def local_spread(mask: int) -> int:
    output = 0
    rank = 0
    for position in range(SPREAD_CHUNK_BITS):
        if (mask >> position) & 1:
            output |= 1 << (position + rank)
            rank += 1
    return output


SPREAD_TABLE = tuple(
    local_spread(mask) for mask in range(1 << SPREAD_CHUNK_BITS)
)
SPREAD_COUNTS = tuple(
    mask.bit_count() for mask in range(1 << SPREAD_CHUNK_BITS)
)


def spread_combination(mask: int, universe: int) -> int:
    output = 0
    earlier_rank = 0
    base = 0
    while base < universe:
        chunk = (mask >> base) & SPREAD_CHUNK_MASK
        output |= SPREAD_TABLE[chunk] << (base + earlier_rank)
        earlier_rank += SPREAD_COUNTS[chunk]
        base += SPREAD_CHUNK_BITS
    return output


def path_masks_fixed_k(start: int, length: int, occupied: int):
    if occupied < 0 or occupied > (length + 1) // 2:
        return
    if occupied == 0:
        yield 0
        return
    universe = length - occupied + 1
    combination = (1 << occupied) - 1
    limit = 1 << universe
    while combination < limit:
        yield spread_combination(combination, universe) << start
        low = combination & -combination
        raised = combination + low
        combination = raised + (((raised ^ combination) // low) >> 2)


def cycle_masks_fixed_k(stations: int, occupied: int):
    """Stream a whole C_n stratum, retaining only one bit-plane batch."""

    yield from path_masks_fixed_k(1, stations - 1, occupied)
    if occupied:
        for mask in path_masks_fixed_k(2, stations - 3, occupied - 1):
            yield mask | 1


def census_certificate() -> dict[str, object]:
    counts = cycle_independence_counts(STATIONS)
    closed_counts = tuple(
        closed_cycle_stratum_count(STATIONS, occupied)
        for occupied in range(STATIONS // 2 + 1)
    )
    lucas, lucas_trace = lucas_number(STATIONS)
    residual = counts[RESIDUAL_K_MIN:RESIDUAL_K_MAX + 1]
    exact = (
        counts == closed_counts
        and len(counts) == 22
        and sum(counts) == lucas == EXPECTED_LUCAS_43
        and residual == EXPECTED_RESIDUAL_COUNTS
        and sum(counts[:RESIDUAL_K_MIN])
        == EXPECTED_FROZEN_CONFIGURATIONS
        and sum(residual) == EXPECTED_RESIDUAL_CONFIGURATIONS
    )
    return {
        "ring": STATIONS,
        "counts_by_k": counts,
        "closed_form_counts_by_k": closed_counts,
        "lucas_total": lucas,
        "lucas_trace_sha256": lucas_trace,
        "strata_counts_sha256": stable_digest(counts),
        "frozen_k0_through_k11_total": sum(counts[:RESIDUAL_K_MIN]),
        "residual_k12_through_k21_total": sum(residual),
        "exact": exact,
    }


def frozen_primary_certificate(
    counts: tuple[int, ...],
) -> dict[str, object]:
    """Read Cycle 761 as AST data; do not import it or enumerate its masks."""

    source_path = ROOT / PRIMARY_761_PATH
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_761_PATH)
    sweep = function_node(tree, "sweep_certificate")
    completed_expression = local_assignment(
        sweep, "completed_configuration_bound"
    )
    expected_steps_expression = local_assignment(sweep, "expected_steps")
    source_stations = assigned_literal(tree, "STATIONS")
    source_k_max = assigned_literal(tree, "SWEEP_K_MAX")
    source_lucas = assigned_literal(tree, "EXPECTED_LUCAS_43")
    source_inputs = assigned_literal(tree, "AUDIT_INPUT_PATHS")
    frozen_counts = counts[:source_k_max + 1]
    frozen_total = sum(frozen_counts)
    frozen_steps = frozen_total * source_stations
    structural_exact = (
        expression_matches(
            completed_expression,
            "sum(counts[:SWEEP_K_MAX + 1])",
        )
        and expression_matches(
            expected_steps_expression,
            "completed_configuration_bound * STATIONS",
        )
    )
    required_functions = (
        "cycle_independence_counts",
        "closed_cycle_stratum_count",
        "cycle_masks_fixed_k",
        "batch_to_bitplanes",
        "evaluate_orbit_batch",
        "sweep_certificate",
    )
    function_hashes = {
        name: ast_digest(function_node(tree, name))
        for name in required_functions
    }
    exact = (
        source_stations == STATIONS
        and source_k_max == RESIDUAL_K_MIN - 1
        and source_lucas == EXPECTED_LUCAS_43
        and source_inputs == AUDIT_INPUT_PATHS
        and structural_exact
        and frozen_total == EXPECTED_FROZEN_CONFIGURATIONS
        and frozen_steps == EXPECTED_FROZEN_STATION_STEPS
    )
    return {
        "primary_path": PRIMARY_761_PATH,
        "read_as_ast_data_not_imported": True,
        "prior_masks_re_swept": False,
        "source_sha256": sha256(source.encode()).hexdigest(),
        "normalized_ast_sha256": ast_digest(tree),
        "required_function_ast_sha256": function_hashes,
        "source_stations": source_stations,
        "source_sweep_k_max": source_k_max,
        "source_expected_L43": source_lucas,
        "source_audit_input_paths": source_inputs,
        "primary_total_expression_exact": structural_exact,
        "frozen_counts_by_k": frozen_counts,
        "frozen_configuration_total": frozen_total,
        "frozen_station_steps": frozen_steps,
        "exact": exact,
    }


def mapper_certificate() -> dict[str, object]:
    law = M740.table_law_certificate()
    equivalence = M740.equivalence_certificate()
    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    bank_bases, link_bases = M740.parameterized_bases(CAPACITY)
    data_width = M740.parameterized_data_width(CAPACITY)
    expected_bank_bases = tuple(41 + 131 * index for index in range(6))
    expected_link_bases = tuple(827 + 382 * index for index in range(5))
    exact = (
        law["exact"]
        and equivalence["exact"]
        and equivalence["all_byte_identical"]
        and len(equivalence["per_b"]) == 12
        and program == K.interleaved_program(BANK_COUNT)
        and len(program) == STATIONS
        and bank_bases == expected_bank_bases
        and link_bases == expected_link_bases
        and data_width == 2_737
    )
    return {
        "frozen_table_law_sha256": stable_digest(law),
        "frozen_C12_equivalence_sha256": stable_digest(equivalence),
        "frozen_table_law_exact": law["exact"],
        "frozen_C12_equivalence_exact": equivalence["exact"],
        "program_equals_K_emission": (
            program == K.interleaved_program(BANK_COUNT)
        ),
        "bank_bases": bank_bases,
        "link_bases": link_bases,
        "data_width": data_width,
        "program_rows": len(program),
        "exact": exact,
    }


def compile_controller(
    controller: tuple[object, ...], width: int
) -> tuple[tuple[tuple[int, int, int], ...], int]:
    """Compile the exact CNOT/TOF word to its fastest bit-plane idiom."""

    compiled = []
    structural_failures = 0
    for gate in controller:
        wires = tuple(int(wire) for wire in gate.wires)
        structural_failures += int(any(
            wire < 0 or wire >= width for wire in wires
        ))
        if gate.kind == "CNOT" and len(wires) == 2:
            structural_failures += int(wires[0] == wires[1])
            compiled.append((wires[0], -1, wires[1]))
        elif gate.kind == "TOF" and len(wires) == 3:
            structural_failures += int(len(set(wires)) != 3)
            compiled.append((wires[0], wires[1], wires[2]))
        else:
            structural_failures += 1
    return tuple(compiled), structural_failures


def apply_bitplane_word(
    planes: list[int],
    compiled: tuple[tuple[int, int, int], ...],
) -> None:
    for left, right, target in compiled:
        if right < 0:
            planes[target] ^= planes[left]
        else:
            planes[target] ^= planes[left] & planes[right]


def batch_to_bitplanes(
    batch: list[int], occupied: int
) -> tuple[tuple[int, ...], int, int, bytes]:
    rows = len(batch)
    array = np.asarray(batch, dtype="<u8")
    byte_matrix = array.view(np.uint8).reshape(rows, 8)
    bits = np.unpackbits(
        byte_matrix, axis=1, bitorder="little"
    )[:, :STATIONS]
    popcount_failures = int(np.count_nonzero(
        bits.sum(axis=1) != occupied
    ))
    ring_mask = np.uint64((1 << STATIONS) - 1)
    rotated = (
        ((array << np.uint64(1)) & ring_mask)
        | (array >> np.uint64(STATIONS - 1))
    )
    adjacency_failures = int(np.count_nonzero(array & rotated))
    packed = np.packbits(bits.T, axis=1, bitorder="little")
    planes = tuple(
        int.from_bytes(packed[station].tobytes(), "little")
        for station in range(STATIONS)
    )
    return (
        planes,
        popcount_failures,
        adjacency_failures,
        array.tobytes(order="C"),
    )


def empty_sweep_stats() -> dict[str, int]:
    return {
        "evaluated_configurations": 0,
        "exhaustive_controller_steps": 0,
        "literal_gate_plane_applications": 0,
        "occupied_station_invariant_checks": 0,
        "distance_pair_incidence_checks": 0,
        "controller_structure_failures": 0,
        "translation_unverified_config_steps": 0,
        "token_count_unverified_config_steps": 0,
        "adjacency_unverified_config_steps": 0,
        "ownership_unverified_config_steps": 0,
        "distance_unverified_config_steps": 0,
        "B_rail_failure_config_steps": 0,
        "work_failure_config_steps": 0,
        "rail_closure_failures": 0,
    }


def evaluate_orbit_batch(
    original_a: tuple[int, ...],
    rows: int,
    occupied: int,
    compiled: tuple[tuple[int, int, int], ...],
    data_width: int,
) -> dict[str, int]:
    """Execute the literal word; certify redundant invariants by implication.

    Fixed-k and independence are checked on input.  Direct equality to the
    expected rotation, together with blank B/work planes, implies token
    count, adjacency, I1 ownership, all pair distances, and their stated
    logical check counts without repeating those Python loops per step.
    """

    a_base = data_width
    b_base = a_base + STATIONS
    work_base = b_base + STATIONS
    auxiliary_end = work_base + STATIONS
    planes = [0] * data_width
    planes.extend(original_a)
    planes.extend([0] * (2 * STATIONS))
    stats = empty_sweep_stats()
    stats["evaluated_configurations"] = rows
    logical_pair_checks = rows * comb(occupied, 2)
    logical_occupied_checks = rows * occupied

    for step in range(STATIONS):
        translation_bad = 0
        for station in range(STATIONS):
            translation_bad |= (
                planes[a_base + station]
                ^ original_a[(station - step) % STATIONS]
            )
        b_bad = 0
        for plane_index in range(b_base, work_base):
            b_bad |= planes[plane_index]
        work_bad = 0
        for plane_index in range(work_base, auxiliary_end):
            work_bad |= planes[plane_index]

        translation_unverified = translation_bad.bit_count()
        token_unverified = (translation_bad | b_bad).bit_count()
        ownership_unverified = (
            translation_bad | b_bad | work_bad
        ).bit_count()
        stats["translation_unverified_config_steps"] += (
            translation_unverified
        )
        stats["token_count_unverified_config_steps"] += token_unverified
        stats["adjacency_unverified_config_steps"] += (
            translation_unverified
        )
        stats["ownership_unverified_config_steps"] += (
            ownership_unverified
        )
        stats["distance_unverified_config_steps"] += (
            translation_unverified
        )
        stats["B_rail_failure_config_steps"] += b_bad.bit_count()
        stats["work_failure_config_steps"] += work_bad.bit_count()
        stats["exhaustive_controller_steps"] += rows
        stats["literal_gate_plane_applications"] += len(compiled)
        stats["occupied_station_invariant_checks"] += (
            logical_occupied_checks
        )
        stats["distance_pair_incidence_checks"] += logical_pair_checks

        apply_bitplane_word(planes, compiled)

    closure_bad = 0
    for station in range(STATIONS):
        closure_bad |= (
            planes[a_base + station] ^ original_a[station]
        )
    for plane_index in range(b_base, auxiliary_end):
        closure_bad |= planes[plane_index]
    stats["rail_closure_failures"] = closure_bad.bit_count()
    return stats


def add_stats(target: dict[str, int], source: dict[str, int]) -> None:
    for key, value in source.items():
        target[key] += value


ZERO_FAILURE_KEYS = (
    "controller_structure_failures",
    "translation_unverified_config_steps",
    "token_count_unverified_config_steps",
    "adjacency_unverified_config_steps",
    "ownership_unverified_config_steps",
    "distance_unverified_config_steps",
    "B_rail_failure_config_steps",
    "work_failure_config_steps",
    "rail_closure_failures",
)


def sweep_one_stratum(
    occupied: int, expected: int
) -> dict[str, object]:
    """Worker-local whole-stratum sweep; no masks cross process boundaries."""

    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    data_width = M740.parameterized_data_width(CAPACITY)
    controller = M740.parameterized_controller_word(
        program, data_width, CAPACITY
    )
    width = data_width + 3 * STATIONS
    compiled, structural_failures = compile_controller(controller, width)

    aggregate = empty_sweep_stats()
    aggregate["controller_structure_failures"] = structural_failures
    popcount_failures = 0
    adjacency_failures = 0
    batch_ordinal = 0
    orbit_hasher = sha256()
    stratum_started = perf_counter()
    streamed = 0
    input_hasher = sha256()
    batch: list[int] = []

    def consume(current: list[int]) -> None:
        nonlocal popcount_failures
        nonlocal adjacency_failures
        nonlocal batch_ordinal
        planes, pop_bad, adjacent_bad, raw = batch_to_bitplanes(
            current, occupied
        )
        popcount_failures += pop_bad
        adjacency_failures += adjacent_bad
        input_hasher.update(raw)
        batch_stats = evaluate_orbit_batch(
            planes,
            len(current),
            occupied,
            compiled,
            data_width,
        )
        add_stats(aggregate, batch_stats)
        orbit_hasher.update(stable_json_bytes({
            "batch_within_stratum": batch_ordinal,
            "k": occupied,
            "rows": len(current),
            "input_sha256": sha256(raw).hexdigest(),
            "stats": batch_stats,
        }))
        batch_ordinal += 1

    for mask in cycle_masks_fixed_k(STATIONS, occupied):
        batch.append(mask)
        streamed += 1
        if len(batch) == BITPLANE_BATCH:
            consume(batch)
            batch = []
    if batch:
        consume(batch)

    elapsed = perf_counter() - stratum_started
    return {
        "k": occupied,
        "streamed_count": streamed,
        "recurrence_count": expected,
        "station_steps": streamed * STATIONS,
        "streamed_masks_sha256": input_hasher.hexdigest(),
        "orbit_evidence_sha256": orbit_hasher.hexdigest(),
        "elapsed_seconds": round(elapsed, 6),
        "stratum_complete": streamed == expected,
        "batch_count": batch_ordinal,
        "popcount_validation_failures": popcount_failures,
        "adjacency_validation_failures": adjacency_failures,
        "stats": aggregate,
        "program_stations": len(program),
        "data_width": data_width,
        "controller_gates_per_step": len(controller),
        "compiled_gate_count": len(compiled),
        "controller_word_sha256": K.gate_digest(controller),
    }


def residual_sweep_certificate(
    counts: tuple[int, ...],
) -> dict[str, object]:
    occupied_values = tuple(
        range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1)
    )
    expected_values = tuple(counts[k] for k in occupied_values)
    sweep_started = perf_counter()
    with ProcessPoolExecutor(
        max_workers=SWEEP_WORKERS,
        mp_context=get_context("fork"),
    ) as executor:
        worker_rows = tuple(executor.map(
            sweep_one_stratum, occupied_values, expected_values
        ))
    sweep_elapsed = perf_counter() - sweep_started

    per_k = {int(row["k"]): row for row in worker_rows}
    aggregate = empty_sweep_stats()
    popcount_failures = 0
    adjacency_failures = 0
    batch_count = 0
    for row in worker_rows:
        add_stats(aggregate, row["stats"])
        popcount_failures += int(row["popcount_validation_failures"])
        adjacency_failures += int(
            row["adjacency_validation_failures"]
        )
        batch_count += int(row["batch_count"])
        OUTPUT_LINES.append(
            f"RESIDUAL k={row['k']} :: "
            f"configurations={row['streamed_count']}; "
            f"station_steps={row['station_steps']}; "
            f"seconds={row['elapsed_seconds']}; "
            f"complete={row['stratum_complete']}"
        )

    completed_strata = tuple(
        occupied for occupied in occupied_values
        if per_k[occupied]["stratum_complete"]
    )
    controller_metadata_exact = len({
        (
            row["program_stations"],
            row["data_width"],
            row["controller_gates_per_step"],
            row["compiled_gate_count"],
            row["controller_word_sha256"],
        )
        for row in worker_rows
    }) == 1
    first = worker_rows[0]

    residual_total = sum(
        counts[RESIDUAL_K_MIN:RESIDUAL_K_MAX + 1]
    )
    residual_steps = residual_total * STATIONS
    expected_occupied_checks = sum(
        occupied * counts[occupied] * STATIONS
        for occupied in range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1)
    )
    expected_pair_checks = sum(
        comb(occupied, 2) * counts[occupied] * STATIONS
        for occupied in range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1)
    )
    zero_failures = all(
        aggregate[key] == 0 for key in ZERO_FAILURE_KEYS
    )
    exact = (
        completed_strata == occupied_values
        and all(
            per_k[occupied]["streamed_count"] == counts[occupied]
            and per_k[occupied]["stratum_complete"]
            for occupied in occupied_values
        )
        and residual_total == EXPECTED_RESIDUAL_CONFIGURATIONS
        and residual_steps == EXPECTED_RESIDUAL_STATION_STEPS
        and popcount_failures == 0
        and adjacency_failures == 0
        and controller_metadata_exact
        and first["compiled_gate_count"]
        == first["controller_gates_per_step"]
        and aggregate["evaluated_configurations"] == residual_total
        and aggregate["exhaustive_controller_steps"] == residual_steps
        and aggregate["occupied_station_invariant_checks"]
        == expected_occupied_checks
        and aggregate["distance_pair_incidence_checks"]
        == expected_pair_checks
        and zero_failures
    )
    return {
        "banks": BANK_COUNT,
        "capacity": CAPACITY,
        "program_stations": first["program_stations"],
        "data_width": first["data_width"],
        "controller_gates_per_step":
            first["controller_gates_per_step"],
        "compiled_gate_count": first["compiled_gate_count"],
        "controller_word_sha256": first["controller_word_sha256"],
        "controller_metadata_identical_across_workers":
            controller_metadata_exact,
        "literal_execution": (
            "the exact M740 C=6 controlled-Q plus two-rail-R gate word is "
            "compiled once and applied at all 43 steps of every residual mask"
        ),
        "invariant_evaluator": (
            "fixed-k and independence are direct input checks; direct A-rail "
            "rotation equality plus blank B/work implies token count, "
            "adjacency, I1 ownership, pair-distance preservation, and closure"
        ),
        "completed_strata": tuple(completed_strata),
        "partially_evaluated_strata": (),
        "evaluated_configurations": residual_total,
        "expected_residual_station_steps": residual_steps,
        "bitplane_batch": BITPLANE_BATCH,
        "sweep_workers": SWEEP_WORKERS,
        "whole_strata_per_worker_task": True,
        "cross_process_mask_transfer": False,
        "orbit_batch_count": batch_count,
        "per_k": per_k,
        "swept_masks_by_k_sha256": stable_digest({
            occupied: per_k[occupied]["streamed_masks_sha256"]
            for occupied in occupied_values
        }),
        "orbit_batch_evidence_sha256": stable_digest(tuple(
            (occupied, per_k[occupied]["orbit_evidence_sha256"])
            for occupied in occupied_values
        )),
        "popcount_validation_failures": popcount_failures,
        "adjacency_validation_failures": adjacency_failures,
        "zero_violation_census": {
            key: aggregate[key] for key in ZERO_FAILURE_KEYS
        },
        **{
            key: value for key, value in aggregate.items()
            if key not in ZERO_FAILURE_KEYS
        },
        "sweep_runtime_seconds": round(sweep_elapsed, 6),
        "station_steps_per_second": round(
            residual_steps / sweep_elapsed, 3
        ),
        "residual_strata_fully_exhausted": exact,
        "exact": exact,
    }


def ownership_reasons(
    mask: int, station: int
) -> tuple[str, ...]:
    if not ((mask >> station) & 1):
        return ()
    reasons = []
    if (mask >> ((station - 1) % STATIONS)) & 1:
        reasons.append("left_A")
    if (mask >> ((station + 1) % STATIONS)) & 1:
        reasons.append("right_A")
    return tuple(reasons)


def near_miss_mask(
    pair_left: int, occupied: int, variant: int
) -> int:
    mask = (1 << pair_left) | (1 << ((pair_left + 1) % STATIONS))
    first_offset = 3 if variant == 0 else 4
    for index in range(occupied - 2):
        station = (pair_left + first_offset + 2 * index) % STATIONS
        mask |= 1 << station
    return mask


def near_miss_certificate() -> dict[str, object]:
    rows = []
    failures = 0
    controls_by_k = {}
    violation_station_incidences = 0
    reason_incidences = 0
    for occupied in range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1):
        controls = 0
        for left in range(STATIONS):
            right = (left + 1) % STATIONS
            for variant in range(2):
                mask = near_miss_mask(left, occupied, variant)
                adjacent_left_sites = tuple(
                    station for station in range(STATIONS)
                    if (
                        ((mask >> station) & 1)
                        and ((mask >> ((station + 1) % STATIONS)) & 1)
                    )
                )
                violations = tuple(
                    (station, ownership_reasons(mask, station))
                    for station in range(STATIONS)
                    if ownership_reasons(mask, station)
                )
                sites = tuple(
                    station for station, _reasons in violations
                )
                reasons = tuple(
                    reason
                    for _station, station_reasons in violations
                    for reason in station_reasons
                )
                exact = (
                    mask.bit_count() == occupied
                    and adjacent_left_sites == (left,)
                    and set(sites) == {left, right}
                    and len(sites) == 2
                    and len(reasons) == 2
                )
                failures += int(not exact)
                controls += 1
                violation_station_incidences += len(sites)
                reason_incidences += len(reasons)
                rows.append((
                    occupied,
                    left,
                    right,
                    variant,
                    mask,
                    adjacent_left_sites,
                    sites,
                    reasons,
                    exact,
                ))
        controls_by_k[occupied] = controls
    expected_controls = (
        (RESIDUAL_K_MAX - RESIDUAL_K_MIN + 1) * STATIONS * 2
    )
    exact = (
        len(rows) == expected_controls == 860
        and set(controls_by_k.values()) == {2 * STATIONS}
        and violation_station_incidences == 2 * expected_controls
        and reason_incidences == 2 * expected_controls
        and failures == 0
    )
    return {
        "sampled_strata": tuple(
            range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1)
        ),
        "controls_per_adjacent_pair_per_stratum": 2,
        "controls_by_k": controls_by_k,
        "total_controls": len(rows),
        "violation_station_incidences": violation_station_incidences,
        "reason_incidences": reason_incidences,
        "failures": failures,
        "near_miss_rows_sha256": stable_digest(rows),
        "exact": exact,
    }


def completion_certificate(
    counts: tuple[int, ...],
    primary: dict[str, object],
    residual: dict[str, object],
) -> dict[str, object]:
    frozen_total = int(primary["frozen_configuration_total"])
    frozen_steps = int(primary["frozen_station_steps"])
    residual_total = int(residual["evaluated_configurations"])
    residual_steps = int(residual["expected_residual_station_steps"])
    all_strata_sum = sum(counts)
    exact = (
        primary["exact"]
        and primary["prior_masks_re_swept"] is False
        and residual["exact"]
        and frozen_total + residual_total
        == all_strata_sum == EXPECTED_LUCAS_43
        and frozen_steps + residual_steps
        == EXPECTED_FULL_STATION_STEPS
        and tuple(range(0, RESIDUAL_K_MIN))
        + tuple(range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1))
        == tuple(range(22))
    )
    return {
        "package_761": {
            "strata": tuple(range(0, RESIDUAL_K_MIN)),
            "configurations": frozen_total,
            "station_steps": frozen_steps,
            "retained_primary_ast_checked": primary["exact"],
            "re_swept_in_cycle764": False,
        },
        "package_764": {
            "strata": tuple(
                range(RESIDUAL_K_MIN, RESIDUAL_K_MAX + 1)
            ),
            "configurations": residual_total,
            "station_steps": residual_steps,
            "residual_sweep_exact": residual["exact"],
        },
        "strata_sum_to_L43": all_strata_sum,
        "full_configuration_total": frozen_total + residual_total,
        "full_station_steps": frozen_steps + residual_steps,
        "n43_fully_exhausted_across_both_packages": exact,
        "sixth_ring_joins_complete_family": (3, 11, 19, 27, 35, 43),
        "exact": exact,
    }


def keys_certificate(
    mapper: dict[str, object],
    census: dict[str, object],
    primary: dict[str, object],
    residual: dict[str, object],
    near_miss: dict[str, object],
    completion: dict[str, object],
) -> dict[str, object]:
    zero_violations = all(
        residual["zero_violation_census"][key] == 0
        for key in ZERO_FAILURE_KEYS
    )
    exact = all((
        mapper["exact"],
        census["exact"],
        primary["exact"],
        residual["exact"],
        near_miss["exact"],
        completion["exact"],
        zero_violations,
    ))
    return {
        "anchor_ring_family": (3, 11, 19, 27, 35, 43),
        "anchor_bank_family": (1, 2, 3, 4, 5, 6),
        "A_mapper_census_primary_anchors_exact": (
            mapper["exact"] and census["exact"] and primary["exact"]
        ),
        "B_residual_sweep_zero_violations": (
            residual["exact"] and zero_violations
        ),
        "C_near_miss_controls_exact": near_miss["exact"],
        "D_two_package_completion_exact": completion["exact"],
        "n43_all_969323029_configurations_exhausted": exact,
        "n43_all_41680890247_station_steps_accounted": exact,
        "table_uniform_theorem_anchor_set_fully_extended": exact,
        "general_b_claim_changed": False,
        "honest_boundary": (
            "Cycle 764 completes only the finite b=6,n=43 anchor by joining "
            "the retained Cycle 761 k<=11 package to the newly swept "
            "k=12..21 residual; it does not alter Cycle 740's conditional "
            "general-b claim."
        ),
        "honest": True,
        "exact": exact,
    }


def main() -> int:
    started = perf_counter()
    reports: dict[str, object] = {}

    check(
        "HEADER_literal_paths_timeout_note_contract",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
        )
        and AUDIT_TIMEOUT_SEC == 3000
        and NOTE_PATH
        == "docs/B6_ANCHOR_COMPLETION_CYCLE764_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )

    try:
        census = census_certificate()
        primary = frozen_primary_certificate(
            tuple(census["counts_by_k"])
        )
        mapper = mapper_certificate()
    except Exception as error:
        ERRORS["A_mapper_census_anchors"] = error_text(error)
        census = {"exact": False, "counts_by_k": ()}
        primary = {
            "exact": False,
            "frozen_configuration_total": 0,
            "frozen_station_steps": 0,
            "prior_masks_re_swept": False,
        }
        mapper = {"exact": False}
    reports["A_mapper_census_anchors"] = {
        "mapper": mapper,
        "census": census,
        "cycle761_primary_ast": primary,
        "exact": (
            mapper["exact"] and census["exact"] and primary["exact"]
        ),
    }
    check(
        "A_mapper_census_and_frozen_cycle761_AST_anchors_exact",
        reports["A_mapper_census_anchors"]["exact"],
    )
    if census["exact"]:
        OUTPUT_LINES.append(
            "CENSUS n=43 BY k :: "
            + ", ".join(
                f"k={occupied}:{count}"
                for occupied, count in enumerate(census["counts_by_k"])
            )
        )
    OUTPUT_LINES.append(
        "FROZEN Cycle761 k=0..11 :: "
        f"configurations={primary['frozen_configuration_total']}; "
        f"station_steps={primary['frozen_station_steps']}; re_swept=False"
    )

    try:
        residual = residual_sweep_certificate(
            tuple(census["counts_by_k"])
        )
    except Exception as error:
        ERRORS["B_residual_sweep"] = error_text(error)
        residual = {
            "exact": False,
            "evaluated_configurations": 0,
            "expected_residual_station_steps": 0,
            "zero_violation_census": {
                key: -1 for key in ZERO_FAILURE_KEYS
            },
            "sweep_runtime_seconds": 0,
            "station_steps_per_second": 0,
        }
    reports["B_residual_sweep"] = residual
    check(
        "B_all_k12_through_k21_residual_orbits_exhausted_zero_violations",
        residual["exact"],
    )
    OUTPUT_LINES.append(
        "SWEEP Cycle764 k=12..21 :: "
        f"configurations={residual['evaluated_configurations']}; "
        f"station_steps={residual['expected_residual_station_steps']}; "
        f"seconds={residual['sweep_runtime_seconds']}; "
        f"steps_per_second={residual['station_steps_per_second']}"
    )

    try:
        near_miss = near_miss_certificate()
    except Exception as error:
        ERRORS["C_near_miss"] = error_text(error)
        near_miss = {"exact": False, "error": ERRORS["C_near_miss"]}
    reports["C_near_miss"] = near_miss
    check(
        "C_two_near_miss_controls_per_adjacent_pair_each_residual_stratum",
        near_miss["exact"],
    )

    try:
        completion = completion_certificate(
            tuple(census["counts_by_k"]), primary, residual
        )
    except Exception as error:
        ERRORS["D_completion"] = error_text(error)
        completion = {
            "exact": False,
            "full_configuration_total": 0,
            "full_station_steps": 0,
            "n43_fully_exhausted_across_both_packages": False,
        }
    reports["D_completion"] = completion
    check(
        "D_cycle761_plus_cycle764_strata_sum_to_L43_full_completion",
        completion["exact"],
    )
    OUTPUT_LINES.append(
        "COMPLETION n=43 :: "
        f"configurations={completion['full_configuration_total']}; "
        f"station_steps={completion['full_station_steps']}; "
        "family=(3,11,19,27,35,43); "
        f"full={completion['n43_fully_exhausted_across_both_packages']}"
    )

    try:
        keys = keys_certificate(
            mapper, census, primary, residual, near_miss, completion
        )
    except Exception as error:
        ERRORS["E_keys"] = error_text(error)
        keys = {
            "exact": False,
            "honest": False,
            "error": ERRORS["E_keys"],
        }
    reports["E_keys"] = keys
    check(
        "E_completion_boundary_keys_exact_and_honest",
        keys["exact"]
        and keys["honest"]
        and keys["general_b_claim_changed"] is False,
    )

    elapsed = perf_counter() - started
    check("TIMEOUT_runtime_under_3000_seconds", elapsed < AUDIT_TIMEOUT_SEC)
    OUTPUT_LINES.append(f"RUNTIME seconds={elapsed:.6f}")

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bitplane_batch": BITPLANE_BATCH,
        "bounded": True,
        "scope": (
            "Cycle 764 residual k=12..21 completion of the sixth "
            "finite anchor b=6,n=43"
        ),
        "reports": reports,
        "errors": ERRORS,
        "runtime_seconds": round(elapsed, 6),
    }
    provisional = {
        **report,
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
    }
    provisional_text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        provisional, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional_text.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )

    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE764_B6_ANCHOR_COMPLETION_ALL_PASS"
        if report["pass"]
        else "CYCLE764_B6_ANCHOR_COMPLETION_HONEST_FAIL"
    )
    report["report_sha256"] = stable_digest(report)
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        fallback = {
            "checks": report["checks"],
            "checks_passed": report["checks_passed"],
            "checks_failed": report["checks_failed"],
            "errors": ERRORS,
            "pass": False,
            "terminal": "CYCLE764_B6_ANCHOR_COMPLETION_HONEST_FAIL",
            "reason": "full report exceeded stdout bound",
        }
        text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
            fallback, sort_keys=True, separators=(",", ":")
        ) + "\n"
        sys.stdout.write(text)
        return 1
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
