#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-761 b=6, n=43 anchor.

The Cycle-761 primary is parsed as inert source data and is blocklisted as an
import.  Census, row-cleanliness, orbit-stratum enumeration, bit-plane rail
evaluation, and adjacent-pair near misses are reimplemented here.
"""
from __future__ import annotations

import ast
from collections import Counter
import json
from math import comb
from pathlib import Path
import sys
from time import perf_counter

sys.dont_write_bytecode = True

import numpy as np

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle740_table_parameterized_mapper_2026_07_28 as M740


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/B6_EXHAUSTIVE_ANCHOR_CYCLE761_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

PRIMARY_PATH = (
    "scripts/frontier_cycle761_b6_exhaustive_anchor_2026_07_28.py"
)
BLOCKLIST = (
    "frontier_cycle761_b6_exhaustive_anchor_2026_07_28",
)
BOUND_LANGUAGE = (
    "k<=11 exhausted; residual counted-not-swept; no full-sweep claim"
)
STDOUT_LIMIT_BYTES = 150 * 1024

BANKS = 6
CAPACITY = 6
STATIONS = 43
SWEEP_K_MAX = 11
EXPECTED_L43 = 969_323_029
EXPECTED_SWEPT = 402_580_148
EXPECTED_RESIDUAL = 566_742_881
EXPECTED_STATION_STEPS = 17_310_946_364
EXPECTED_COUNTS = (
    1,
    43,
    860,
    10_621,
    90_687,
    567_987,
    2_701_776,
    9_970_840,
    28_915_436,
    66_335_412,
    120_609_840,
    173_376_645,
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

# A larger bit-plane makes the full 402,580,148-mask recount practical while
# retaining only one bounded batch.  It is independent of the primary's batch.
BITPLANE_BATCH = 1 << 20
DILATION_CHUNK_BITS = 10
DILATION_CHUNK_MASK = (1 << DILATION_CHUNK_BITS) - 1

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


def assigned_literal(tree: ast.Module, name: str) -> object:
    values: list[ast.AST] = []
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
        raise AssertionError(("literal assignment", name, len(values)))
    return ast.literal_eval(values[0])


def function_return_literal(
    tree: ast.Module, function_name: str, key_name: str
) -> object:
    functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == function_name
    ]
    if len(functions) != 1:
        raise AssertionError(("function", function_name, len(functions)))
    matches: list[ast.AST] = []
    for node in ast.walk(functions[0]):
        if not isinstance(node, ast.Return) or not isinstance(
            node.value, ast.Dict
        ):
            continue
        for key, value in zip(node.value.keys, node.value.values):
            if (
                isinstance(key, ast.Constant)
                and key.value == key_name
            ):
                matches.append(value)
    if len(matches) != 1:
        raise AssertionError(
            ("literal return field", function_name, key_name, len(matches))
        )
    return ast.literal_eval(matches[0])


def closed_cycle_counts(stations: int) -> tuple[int, ...]:
    counts = [1]
    for occupied in range(1, stations // 2 + 1):
        counts.append(
            stations
            * comb(stations - occupied - 1, occupied - 1)
            // occupied
        )
    return tuple(counts)


def extraction() -> dict[str, object]:
    """Literal-eval the primary as inert data, then extract its exact bound."""

    source = Path(PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    audit_paths = assigned_literal(tree, "AUDIT_INPUT_PATHS")
    timeout = assigned_literal(tree, "AUDIT_TIMEOUT_SEC")
    note_path = assigned_literal(tree, "NOTE_PATH")
    stations = assigned_literal(tree, "STATIONS")
    banks = assigned_literal(tree, "BANK_COUNT")
    capacity = assigned_literal(tree, "CAPACITY")
    sweep_k_max = assigned_literal(tree, "SWEEP_K_MAX")
    lucas_target = assigned_literal(tree, "EXPECTED_LUCAS_43")
    bound_statement = function_return_literal(
        tree, "sweep_certificate", "sweep_bound_statement"
    )
    full_sweep = function_return_literal(
        tree, "sweep_certificate", "full_sweep"
    )

    counts = closed_cycle_counts(int(stations))
    swept = sum(counts[: int(sweep_k_max) + 1])
    residual = sum(counts[int(sweep_k_max) + 1 :])
    station_steps = int(stations) * swept
    exact = (
        audit_paths == AUDIT_INPUT_PATHS
        and timeout == AUDIT_TIMEOUT_SEC
        and note_path == NOTE_PATH
        and stations == STATIONS
        and banks == BANKS
        and capacity == CAPACITY
        and sweep_k_max == SWEEP_K_MAX
        and lucas_target == EXPECTED_L43
        and counts == EXPECTED_COUNTS
        and sum(counts) == EXPECTED_L43
        and swept == EXPECTED_SWEPT
        and residual == EXPECTED_RESIDUAL
        and station_steps == EXPECTED_STATION_STEPS
        and full_sweep is False
        and "0<=k<=11 is enumerated" in bound_statement
        and "12<=k<=21 are recurrence-counted only" in bound_statement
        and "not enumerated, sampled, partially swept, or materialized"
        in bound_statement
    )
    return {
        "literal_eval_only": True,
        "primary_imported": BLOCKLIST[0] in sys.modules,
        "counts_by_k": counts,
        "total": sum(counts),
        "swept_k0_through_k11": swept,
        "residual_k12_through_k21": residual,
        "station_steps": station_steps,
        "rows": stations,
        "near_miss_rows": stations,
        "primary_full_sweep_literal": full_sweep,
        "primary_bound_statement": bound_statement,
        "exact": exact and BLOCKLIST[0] not in sys.modules,
    }


def census_recount() -> dict[str, object]:
    """Recount C_43 by an endpoint-state DP plus a scalar Lucas stream."""

    totals = [0] * (STATIONS // 2 + 1)
    for first in (0, 1):
        # State is (last_bit, population) -> number of prefixes.
        states: dict[tuple[int, int], int] = {(first, first): 1}
        for _position in range(1, STATIONS):
            next_states: dict[tuple[int, int], int] = {}
            for (last, occupied), multiplicity in states.items():
                key0 = (0, occupied)
                next_states[key0] = (
                    next_states.get(key0, 0) + multiplicity
                )
                if not last:
                    key1 = (1, occupied + 1)
                    next_states[key1] = (
                        next_states.get(key1, 0) + multiplicity
                    )
            states = next_states
        for (last, occupied), multiplicity in states.items():
            if not (first and last):
                totals[occupied] += multiplicity

    lucas_older, lucas_newer = 2, 1
    for _index in range(2, STATIONS + 1):
        lucas_older, lucas_newer = (
            lucas_newer,
            lucas_older + lucas_newer,
        )
    counts = tuple(totals)
    total = sum(counts)
    swept = sum(counts[: SWEEP_K_MAX + 1])
    residual = sum(counts[SWEEP_K_MAX + 1 :])
    return {
        "method": "first/last endpoint-state dynamic-program stream",
        "counts_by_k": counts,
        "total": total,
        "lucas_stream": lucas_newer,
        "swept_k0_through_k11": swept,
        "residual_k12_through_k21": residual,
        "exact": (
            counts == EXPECTED_COUNTS
            and total == lucas_newer == EXPECTED_L43
            and swept == EXPECTED_SWEPT
            and residual == EXPECTED_RESIDUAL
        ),
    }


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(int(wire) for wire in gate.wires)


def own_controlled_signatures(
    word: tuple[object, ...], control: int, work: int
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    lifted: list[tuple[str, tuple[int, ...]]] = []
    for gate in word:
        wires = tuple(int(wire) for wire in gate.wires)
        if gate.kind == "X":
            lifted.append(("CNOT", (control, wires[0])))
        elif gate.kind == "CNOT":
            lifted.append(("TOF", (control, wires[0], wires[1])))
        elif gate.kind == "TOF":
            lifted.extend(
                (
                    ("TOF", (control, wires[0], work)),
                    ("TOF", (work, wires[1], wires[2])),
                    ("TOF", (control, wires[0], work)),
                )
            )
        else:
            raise ValueError(("unsupported semantic gate", gate.kind))
    return tuple(lifted)


def primitive_clean_truth_failures(kind: str) -> int:
    failures = 0
    if kind == "X":
        for control in (0, 1):
            for target in (0, 1):
                observed_target = target ^ control
                failures += observed_target != (target ^ control)
    elif kind == "CNOT":
        for control in (0, 1):
            for left in (0, 1):
                for target in (0, 1):
                    observed_target = target ^ (control & left)
                    failures += observed_target != (
                        target ^ (control & left)
                    )
    elif kind == "TOF":
        for control in (0, 1):
            for left in (0, 1):
                for right in (0, 1):
                    for target in (0, 1):
                        work = 0
                        work ^= control & left
                        observed_target = target ^ (work & right)
                        work ^= control & left
                        failures += observed_target != (
                            target ^ (control & left & right)
                        )
                        failures += work != 0
    else:
        raise ValueError(kind)
    return failures


def expected_swap_signatures(
    left: int, right: int
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    return (
        ("CNOT", (left, right)),
        ("CNOT", (right, left)),
        ("CNOT", (left, right)),
    )


def rows_recount() -> dict[str, object]:
    """Independently validate every emitted row and the exact controller."""

    program = tuple(M740.parameterized_program(BANKS, CAPACITY))
    data_width = int(M740.parameterized_data_width(CAPACITY))
    row_kinds: Counter[str] = Counter()
    semantic_kinds: Counter[str] = Counter()
    row_failures: list[dict[str, object]] = []
    q_expected: list[tuple[str, tuple[int, ...]]] = []
    arities = {"X": 1, "CNOT": 2, "TOF": 3}
    primitive_failures = {
        kind: primitive_clean_truth_failures(kind)
        for kind in arities
    }

    for station, row in enumerate(program):
        kind, index, _local = row
        row_kinds[str(kind)] += 1
        reasons: list[str] = []
        try:
            word = tuple(
                M740.parameterized_mapped_macro(row, CAPACITY)
            )
            control = data_width + station
            work = data_width + 2 * len(program) + station
            for gate in word:
                semantic_kinds[gate.kind] += 1
                wires = tuple(int(wire) for wire in gate.wires)
                if gate.kind not in arities:
                    reasons.append(f"kind:{gate.kind}")
                    continue
                if len(wires) != arities[gate.kind]:
                    reasons.append(f"arity:{gate.kind}")
                if len(set(wires)) != len(wires):
                    reasons.append(f"repeated_operand:{gate.kind}")
                if any(wire < 0 or wire >= data_width for wire in wires):
                    reasons.append(f"data_domain:{gate.kind}")
                if primitive_failures[gate.kind]:
                    reasons.append(f"truth:{gate.kind}")
            q_expected.extend(
                own_controlled_signatures(word, control, work)
            )
        except Exception as error:
            reasons.append(error_text(error))
        if reasons:
            row_failures.append(
                {
                    "station": station,
                    "kind": kind,
                    "index": index,
                    "reasons": reasons,
                }
            )

    controller = tuple(
        M740.parameterized_controller_word(
            program, data_width, CAPACITY
        )
    )
    actual_signatures = tuple(gate_signature(gate) for gate in controller)
    a_base = data_width
    b_base = data_width + len(program)
    r_expected: list[tuple[str, tuple[int, ...]]] = []
    for station in range(len(program)):
        r_expected.extend(
            expected_swap_signatures(
                a_base + station, b_base + station
            )
        )
    for station in range(len(program)):
        r_expected.extend(
            expected_swap_signatures(
                b_base + station,
                a_base + (station + 1) % len(program),
            )
        )
    expected_controller = tuple(q_expected) + tuple(r_expected)
    expected_row_kinds = {
        "bank": 6,
        "cross": 5,
        "finalizer": 1,
        "handoff": 10,
        "relay": 20,
        "source": 1,
    }
    exact = (
        len(program) == STATIONS
        and data_width == 2_737
        and dict(sorted(row_kinds.items())) == expected_row_kinds
        and not row_failures
        and all(value == 0 for value in primitive_failures.values())
        and actual_signatures == expected_controller
    )
    return {
        "banks": BANKS,
        "capacity": CAPACITY,
        "data_width": data_width,
        "rows_checked": len(program),
        "row_kind_counts": dict(sorted(row_kinds.items())),
        "semantic_gate_kind_counts": dict(
            sorted(semantic_kinds.items())
        ),
        "primitive_truth_failures": primitive_failures,
        "row_failure_count": len(row_failures),
        "row_failures": row_failures[:10],
        "q_gates": len(q_expected),
        "rail_gates": len(r_expected),
        "controller_gates": len(controller),
        "literal_controller_exact": actual_signatures
        == expected_controller,
        "all_43_rows_clean": exact,
        "exact": exact,
    }


def _dilate_chunk(value: int) -> int:
    output = 0
    extra = 0
    for position in range(DILATION_CHUNK_BITS):
        if (value >> position) & 1:
            output |= 1 << (position + extra)
            extra += 1
    return output


DILATION_TABLE = tuple(
    _dilate_chunk(value)
    for value in range(1 << DILATION_CHUNK_BITS)
)
DILATION_POPCOUNTS = tuple(
    value.bit_count()
    for value in range(1 << DILATION_CHUNK_BITS)
)
NP_BYTE_POPCOUNTS = np.asarray(
    [value.bit_count() for value in range(256)], dtype=np.uint8
)


def dilate_combination(combination: int, universe: int) -> int:
    """Insert one zero after each earlier selected compressed position."""

    output = 0
    earlier_selected = 0
    base = 0
    while base < universe:
        chunk = (combination >> base) & DILATION_CHUNK_MASK
        output |= DILATION_TABLE[chunk] << (
            base + earlier_selected
        )
        earlier_selected += DILATION_POPCOUNTS[chunk]
        base += DILATION_CHUNK_BITS
    return output


def cycle_stratum_batches(
    stations: int, occupied: int, batch_size: int
):
    """Yield one C_n k-stratum in bounded batches, with no partial omission."""

    batch: list[int] = []
    cases = ((1, stations - 1, occupied, 0),)
    if occupied:
        cases += ((2, stations - 3, occupied - 1, 1),)
    for start, length, selected, prefix in cases:
        if selected < 0 or selected > (length + 1) // 2:
            continue
        if selected == 0:
            batch.append(prefix)
            if len(batch) == batch_size:
                yield batch
                batch = []
            continue
        universe = length - selected + 1
        combination = (1 << selected) - 1
        limit = 1 << universe
        while combination < limit:
            batch.append(
                prefix
                | (dilate_combination(combination, universe) << start)
            )
            if len(batch) == batch_size:
                yield batch
                batch = []
            low = combination & -combination
            raised = combination + low
            combination = raised + (
                ((raised ^ combination) // low) >> 2
            )
    if batch:
        yield batch


def batch_to_bitplanes(
    batch: list[int], occupied: int
) -> tuple[tuple[int, ...], int, int, int]:
    rows = len(batch)
    array = np.asarray(batch, dtype="<u8")
    bytes_view = array.view(np.uint8).reshape(rows, 8)
    if hasattr(np, "bitwise_count"):
        populations = np.bitwise_count(array)
    else:
        populations = NP_BYTE_POPCOUNTS[bytes_view].sum(axis=1)
    population_failures = int(
        np.count_nonzero(populations != occupied)
    )
    ring_mask = np.uint64((1 << STATIONS) - 1)
    rotated = (
        ((array << np.uint64(1)) & ring_mask)
        | (array >> np.uint64(STATIONS - 1))
    )
    adjacency_failures = int(np.count_nonzero(array & rotated))
    range_failures = int(np.count_nonzero(array & ~ring_mask))

    unpacked = np.unpackbits(
        bytes_view, axis=1, bitorder="little"
    )[:, :STATIONS]
    packed = np.packbits(
        unpacked.T, axis=1, bitorder="little"
    )
    planes = tuple(
        int.from_bytes(packed[station].tobytes(), "little")
        for station in range(STATIONS)
    )
    return (
        planes,
        population_failures,
        adjacency_failures,
        range_failures,
    )


def evaluate_rail_bitplanes(
    original: tuple[int, ...], rows: int
) -> dict[str, int]:
    """Evaluate all 43 Q-boundary rail states in a clean-work quotient."""

    row_full = (1 << rows) - 1
    a = list(original)
    b = [0] * STATIONS
    failures = {
        "translation_failure_station_steps": 0,
        "B_rail_failure_station_steps": 0,
        "token_support_failure_station_steps": 0,
        "adjacency_failure_station_steps": 0,
        "ownership_failure_station_steps": 0,
        "rail_closure_failures": 0,
    }
    for step in range(STATIONS):
        translation_bad = 0
        b_bad = 0
        token_support_bad = 0
        adjacency_bad = 0
        ownership_bad = 0
        for station in range(STATIONS):
            expected = original[(station - step) % STATIONS]
            translation_bad |= a[station] ^ expected
            b_bad |= b[station]
            token_support_bad |= (a[station] | b[station]) & ~row_full
            right = (station + 1) % STATIONS
            adjacency_bad |= a[station] & a[right]
            left = (station - 1) % STATIONS
            dirty = (
                a[left]
                | a[right]
                | b[left]
                | b[station]
                | b[right]
            )
            ownership_bad |= a[station] & dirty
        failures["translation_failure_station_steps"] += (
            translation_bad.bit_count()
        )
        failures["B_rail_failure_station_steps"] += b_bad.bit_count()
        failures["token_support_failure_station_steps"] += (
            token_support_bad.bit_count()
        )
        failures["adjacency_failure_station_steps"] += (
            adjacency_bad.bit_count()
        )
        failures["ownership_failure_station_steps"] += (
            ownership_bad.bit_count()
        )

        # Exact action of the two disjoint SWAP layers R1 then R2.
        a, b = b, a
        for station in range(STATIONS):
            target = (station + 1) % STATIONS
            b[station], a[target] = a[target], b[station]

    closure_bad = 0
    for observed, expected in zip(a, original):
        closure_bad |= observed ^ expected
    for plane in b:
        closure_bad |= plane
    failures["rail_closure_failures"] = closure_bad.bit_count()
    return failures


def sweep_recount(
    counts: tuple[int, ...], rows: dict[str, object]
) -> dict[str, object]:
    """Exhaust k<=11 using independent batches and a bit-plane evaluator."""

    if not rows.get("exact", False):
        return {
            "exact": False,
            "error": "row-clean quotient prerequisite failed",
            "completed_k": (),
            "configurations": 0,
            "station_steps": 0,
        }

    started = perf_counter()
    completed_k: list[int] = []
    per_k: dict[int, int] = {}
    configurations = 0
    station_steps = 0
    batches = 0
    population_failures = 0
    input_adjacency_failures = 0
    input_range_failures = 0
    orbit_failures = {
        "translation_failure_station_steps": 0,
        "B_rail_failure_station_steps": 0,
        "token_support_failure_station_steps": 0,
        "adjacency_failure_station_steps": 0,
        "ownership_failure_station_steps": 0,
        "rail_closure_failures": 0,
    }

    for occupied in range(SWEEP_K_MAX + 1):
        stratum_count = 0
        for batch in cycle_stratum_batches(
            STATIONS, occupied, BITPLANE_BATCH
        ):
            planes, pop_bad, adjacent_bad, range_bad = (
                batch_to_bitplanes(batch, occupied)
            )
            batch_orbit = evaluate_rail_bitplanes(
                planes, len(batch)
            )
            population_failures += pop_bad
            input_adjacency_failures += adjacent_bad
            input_range_failures += range_bad
            for key, value in batch_orbit.items():
                orbit_failures[key] += value
            stratum_count += len(batch)
            configurations += len(batch)
            station_steps += len(batch) * STATIONS
            batches += 1
        per_k[occupied] = stratum_count
        if stratum_count == counts[occupied]:
            completed_k.append(occupied)

    elapsed = perf_counter() - started
    residual = sum(counts[SWEEP_K_MAX + 1 :])
    zero_violations = (
        population_failures == 0
        and input_adjacency_failures == 0
        and input_range_failures == 0
        and all(value == 0 for value in orbit_failures.values())
    )
    exact = (
        tuple(completed_k) == tuple(range(SWEEP_K_MAX + 1))
        and all(
            per_k[occupied] == counts[occupied]
            for occupied in range(SWEEP_K_MAX + 1)
        )
        and configurations == EXPECTED_SWEPT
        and residual == EXPECTED_RESIDUAL
        and station_steps == EXPECTED_STATION_STEPS
        and zero_violations
    )
    return {
        "evaluator": (
            "independent bit-plane clean-work quotient of the exact "
            "M740 C=6 controller; all Q rows discharged by rows_recount"
        ),
        "completed_k": tuple(completed_k),
        "per_k_counts": per_k,
        "configurations": configurations,
        "station_steps": station_steps,
        "batches": batches,
        "bitplane_batch": BITPLANE_BATCH,
        "population_failures": population_failures,
        "input_adjacency_failures": input_adjacency_failures,
        "input_range_failures": input_range_failures,
        "orbit_failures": orbit_failures,
        "zero_violations": zero_violations,
        "residual_counted_not_swept": residual,
        "full_sweep": False,
        "coverage": BOUND_LANGUAGE,
        "runtime_seconds": round(elapsed, 6),
        "exact": exact,
    }


def ownership_reasons(
    a_mask: int, b_mask: int, work_mask: int, station: int
) -> tuple[str, ...]:
    if not ((a_mask >> station) & 1):
        return ()
    left = (station - 1) % STATIONS
    right = (station + 1) % STATIONS
    terms = (
        ("left_A", (a_mask >> left) & 1),
        ("right_A", (a_mask >> right) & 1),
        ("left_B", (b_mask >> left) & 1),
        ("own_B", (b_mask >> station) & 1),
        ("right_B", (b_mask >> right) & 1),
        ("own_work", (work_mask >> station) & 1),
    )
    return tuple(label for label, value in terms if value)


def near_miss_recount() -> dict[str, object]:
    passed_rows = 0
    violating_station_total = 0
    reason_total = 0
    for left in range(STATIONS):
        right = (left + 1) % STATIONS
        mask = (1 << left) | (1 << right)
        violations = tuple(
            (
                station,
                ownership_reasons(mask, 0, 0, station),
            )
            for station in range(STATIONS)
            if ownership_reasons(mask, 0, 0, station)
        )
        sites = tuple(station for station, _reasons in violations)
        reasons = tuple(
            reason
            for _station, station_reasons in violations
            for reason in station_reasons
        )
        row_exact = (
            sites == tuple(sorted((left, right)))
            and len(violations) == 2
            and len(reasons) == 2
        )
        passed_rows += int(row_exact)
        violating_station_total += len(violations)
        reason_total += len(reasons)
    return {
        "rows_checked": STATIONS,
        "rows_passed": passed_rows,
        "violating_stations": violating_station_total,
        "reason_incidences": reason_total,
        "exact": (
            passed_rows == STATIONS
            and violating_station_total == 2 * STATIONS
            and reason_total == 2 * STATIONS
        ),
    }


def discipline(
    extracted: dict[str, object], sweep: dict[str, object]
) -> dict[str, object]:
    loaded_blocklist = tuple(
        name for name in BLOCKLIST if name in sys.modules
    )
    exact = (
        not loaded_blocklist
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
        )
        and extracted["primary_full_sweep_literal"] is False
        and sweep.get("full_sweep") is False
        and sweep.get("residual_counted_not_swept")
        == EXPECTED_RESIDUAL
        and sweep.get("coverage") == BOUND_LANGUAGE
        and BOUND_LANGUAGE
        == "k<=11 exhausted; residual counted-not-swept; no full-sweep claim"
    )
    return {
        "blocklist": BLOCKLIST,
        "loaded_blocklist": loaded_blocklist,
        "audit_input_paths_literal_expected": True,
        "bound_language": BOUND_LANGUAGE,
        "k_le_11_exhausted": sweep.get("completed_k")
        == tuple(range(12)),
        "residual_counted_not_swept": sweep.get(
            "residual_counted_not_swept"
        ),
        "full_sweep_claim": False,
        "exact": exact,
    }


def run_certificate(
    label: str, function: object, *args: object
) -> dict[str, object]:
    try:
        report = function(*args)
        if not isinstance(report, dict):
            raise TypeError(("certificate did not return dict", label))
        return report
    except Exception as error:
        ERRORS[label] = error_text(error)
        return {"exact": False, "error": ERRORS[label]}


def main() -> int:
    started = perf_counter()

    extracted = run_certificate("extraction", extraction)
    check(
        "A_extraction_literal_primary_census_rows_near_miss",
        extracted.get("exact")
        and extracted.get("total") == EXPECTED_L43
        and extracted.get("swept_k0_through_k11") == EXPECTED_SWEPT
        and extracted.get("residual_k12_through_k21")
        == EXPECTED_RESIDUAL
        and extracted.get("station_steps")
        == EXPECTED_STATION_STEPS
        and extracted.get("rows") == 43
        and extracted.get("near_miss_rows") == 43,
    )

    census = run_certificate("census_recount", census_recount)
    check(
        "B_independent_streamed_C43_census_recount",
        census.get("exact")
        and census.get("total") == EXPECTED_L43
        and census.get("swept_k0_through_k11") == EXPECTED_SWEPT
        and census.get("residual_k12_through_k21")
        == EXPECTED_RESIDUAL,
    )

    rows = run_certificate("rows_recount", rows_recount)
    check(
        "C_independent_all_43_b6_rows_clean_recount",
        rows.get("exact")
        and rows.get("rows_checked") == 43
        and rows.get("row_failure_count") == 0,
    )

    sweep = run_certificate(
        "sweep_recount",
        sweep_recount,
        tuple(census.get("counts_by_k", ())),
        rows,
    )
    check(
        "D_independent_k0_through_k11_bitplane_sweep_recount",
        sweep.get("exact")
        and sweep.get("configurations") == EXPECTED_SWEPT
        and sweep.get("station_steps") == EXPECTED_STATION_STEPS
        and sweep.get("zero_violations") is True,
    )

    near_miss = run_certificate(
        "near_miss_recount", near_miss_recount
    )
    check(
        "E_independent_near_miss_43_of_43",
        near_miss.get("exact")
        and near_miss.get("rows_passed") == 43,
    )

    bounded_discipline = run_certificate(
        "discipline", discipline, extracted, sweep
    )
    check(
        "F_blocklist_and_honest_bound_discipline",
        bounded_discipline.get("exact")
        and not bounded_discipline.get("loaded_blocklist")
        and bounded_discipline.get("bound_language")
        == BOUND_LANGUAGE,
    )

    elapsed = perf_counter() - started
    check("TIMEOUT_runtime_under_1800_seconds", elapsed < AUDIT_TIMEOUT_SEC)

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "A_extraction": extracted,
        "B_census_recount": census,
        "C_rows_recount": rows,
        "D_sweep_recount": sweep,
        "E_near_miss_recount": near_miss,
        "F_discipline": bounded_discipline,
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
        "CYCLE761_B6_ANCHOR_INDEPENDENT_CHECK_ALL_PASS"
        if report["pass"]
        else "CYCLE761_B6_ANCHOR_INDEPENDENT_CHECK_HONEST_FAIL"
    )

    text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        fallback = {
            "checks": report["checks"],
            "checks_passed": report["checks_passed"],
            "checks_failed": report["checks_failed"] + 1,
            "errors": ERRORS,
            "pass": False,
            "reason": "stdout bound exceeded",
            "terminal": (
                "CYCLE761_B6_ANCHOR_INDEPENDENT_CHECK_HONEST_FAIL"
            ),
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
