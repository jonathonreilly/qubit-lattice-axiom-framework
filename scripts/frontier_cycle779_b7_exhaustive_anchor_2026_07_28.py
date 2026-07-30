#!/usr/bin/env python3
"""Cycle 779: seventh anchor at b=7, n=51, with an honest timed scope.

The exact C_51 independent-set census is computed twice without materializing
its 45.5 billion masks.  Every C=7 mapper row is discharged directly.  A
warm end-to-end benchmark then selects the largest complete prefix of whole
occupancy strata admitted by a conservative 1500-second budget model.  The
selected strata are streamed exhaustively through the Cycle-761 bit-plane
clean-work quotient; no partial stratum or silent sample contributes coverage.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys
from time import perf_counter

sys.dont_write_bytecode = True

import numba
import numpy as np

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle740_table_parameterized_mapper_2026_07_28 as M740


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
BENCHMARK_BATCHES = 4
BENCHMARK_K = 8
BITPLANE_BATCH = 1 << 20
BUDGET_RESERVE_SEC = 240
RATE_DERATE_NUMERATOR = 13
RATE_DERATE_DENOMINATOR = 20

BANKS = 7
CAPACITY = 7
STATIONS = 51
EXPECTED_L51 = 45_537_549_124
EXPECTED_FULL_STEPS = 2_322_415_005_324
EXPECTED_DATA_WIDTH = 3_250
EXPECTED_ROW_KINDS = {
    "bank": 7,
    "cross": 6,
    "finalizer": 1,
    "handoff": 12,
    "relay": 24,
    "source": 1,
}

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)

EXPECTED_MODULE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "be1d0af8a7dae03b8eff414c1a88ec21fc04c3e92984569a15324b5da2c0fdd3",
}
LINEAGE_ANCHORS = {
    "cycle756_b5_primary": {
        "commit": "361c3e9f212155cca59004b88b3ef227f1a43f40",
        "blob": "3f9d019d68ce96dde4c5f1823800a06fc5316518",
    },
    "cycle761_b6_primary": {
        "commit": "9b3ee1725494da84dd24bfa7df675003baab347f",
        "blob": "ce19fef7faf03cb3f336717556409b7b1c24e70e",
    },
    "cycle761_b6_independent": {
        "commit": "9b3ee1725494da84dd24bfa7df675003baab347f",
        "blob": "045feb69d405c68bac5aa45293c9d341e60e2755",
    },
    "cycle740_mapper_source": {
        "commit": "361c3e9f212155cca59004b88b3ef227f1a43f40",
        "blob": "523df5a77342d2eaa9a3a78d9d9997a94145baeb",
    },
}
COPIED_MODULE_PROVENANCE = (
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py "
    "was absent locally and from freshly fetched origin/main; copied "
    "byte-exactly from commit "
    "361c3e9f212155cca59004b88b3ef227f1a43f40 "
    "(blob 523df5a77342d2eaa9a3a78d9d9997a94145baeb)"
)
STDOUT_BYTES_EMITTED = 0


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_json_bytes(value)).hexdigest()


def emit_line(line: str) -> None:
    global STDOUT_BYTES_EMITTED
    STDOUT_BYTES_EMITTED += len(line.encode()) + 1
    print(line, flush=True)


def file_sha256(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def module_anchor_certificate() -> dict[str, object]:
    observed = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    table_law = M740.table_law_certificate()
    equivalence = M740.equivalence_certificate()
    exact = (
        tuple(AUDIT_INPUT_PATHS) == AUDIT_INPUT_PATHS
        and all(Path(path).is_file() for path in AUDIT_INPUT_PATHS)
        and observed == EXPECTED_MODULE_SHA256
        and table_law["exact"]
        and equivalence["exact"]
        and equivalence["all_byte_identical"]
    )
    return {
        "literal_audit_input_paths": AUDIT_INPUT_PATHS,
        "module_sha256": observed,
        "lineage_commit_and_blob_anchors": LINEAGE_ANCHORS,
        "copied_module_provenance": COPIED_MODULE_PROVENANCE,
        "M740_table_law_exact": table_law["exact"],
        "M740_C12_equivalence_exact": equivalence["exact"],
        "exact": exact,
    }


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


def endpoint_state_cycle_counts(stations: int) -> tuple[int, ...]:
    totals = [0] * (stations // 2 + 1)
    for first in (0, 1):
        states: dict[tuple[int, int], int] = {(first, first): 1}
        for _position in range(1, stations):
            following: dict[tuple[int, int], int] = {}
            for (last, occupied), multiplicity in states.items():
                zero = (0, occupied)
                following[zero] = following.get(zero, 0) + multiplicity
                if not last:
                    one = (1, occupied + 1)
                    following[one] = (
                        following.get(one, 0) + multiplicity
                    )
            states = following
        for (last, occupied), multiplicity in states.items():
            if not (first and last):
                totals[occupied] += multiplicity
    return tuple(totals)


def closed_cycle_stratum_count(stations: int, occupied: int) -> int:
    if occupied == 0:
        return 1
    return (
        stations
        * comb(stations - occupied - 1, occupied - 1)
        // occupied
    )


def census_certificate() -> dict[str, object]:
    recurrence_counts = cycle_independence_counts(STATIONS)
    endpoint_counts = endpoint_state_cycle_counts(STATIONS)
    formula_counts = tuple(
        closed_cycle_stratum_count(STATIONS, occupied)
        for occupied in range(STATIONS // 2 + 1)
    )
    lucas, lucas_trace = lucas_number(STATIONS)
    repeated_counts = cycle_independence_counts(STATIONS)
    first_digest = stable_digest(recurrence_counts)
    repeated_digest = stable_digest(repeated_counts)
    exact = (
        recurrence_counts == endpoint_counts == formula_counts
        and recurrence_counts == repeated_counts
        and first_digest == repeated_digest
        and sum(recurrence_counts) == lucas == EXPECTED_L51
        and lucas * STATIONS == EXPECTED_FULL_STEPS
        and len(recurrence_counts) == STATIONS // 2 + 1
    )
    return {
        "ring": STATIONS,
        "counts_by_k": recurrence_counts,
        "path_polynomial_recurrence_total": sum(recurrence_counts),
        "endpoint_state_census_total": sum(endpoint_counts),
        "closed_formula_total": sum(formula_counts),
        "independent_scalar_L51": lucas,
        "full_orbit_station_steps": lucas * STATIONS,
        "lucas_trace_sha256": lucas_trace,
        "census_sha256": first_digest,
        "repeated_census_sha256": repeated_digest,
        "census_repeat_byte_identical": first_digest == repeated_digest,
        "exact": exact,
    }


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(int(wire) for wire in gate.wires)


def row_clean_work_certificate() -> dict[str, object]:
    program = tuple(M740.parameterized_program(BANKS, CAPACITY))
    frozen_program = tuple(K.interleaved_program(BANKS))
    data_width = int(M740.parameterized_data_width(CAPACITY))
    bank_bases, link_bases = M740.parameterized_bases(CAPACITY)
    primitive = M740.primitive_clean_certificate()
    row_kinds: Counter[str] = Counter()
    semantic_kinds: Counter[str] = Counter()
    failures: list[dict[str, object]] = []
    mapped_hasher = sha256()
    controlled_gate_total = 0

    for station, row in enumerate(program):
        row_kinds[str(row[0])] += 1
        try:
            word = tuple(
                M740.parameterized_mapped_macro(row, CAPACITY)
            )
            clean = M740.validate_clean_word(
                word,
                data_width,
                data_width + station,
                data_width + 2 * len(program) + station,
                bool(primitive["exact"]),
            )
            semantic_kinds.update(gate.kind for gate in word)
            controlled_gate_total += int(clean["controlled_gates"])
            mapped_hasher.update(stable_json_bytes(tuple(
                gate_signature(gate) for gate in word
            )))
            if not clean["pass"]:
                failures.append({
                    "station": station,
                    "row_kind": row[0],
                    "row_index": row[1],
                    "clean": clean,
                })
        except Exception as error:
            failures.append({
                "station": station,
                "row_kind": row[0],
                "row_index": row[1],
                "error": f"{type(error).__name__}: {error}",
            })

    controller = tuple(
        M740.parameterized_controller_word(
            program, data_width, CAPACITY
        )
    )
    controller_width = data_width + 3 * STATIONS
    controller_structure_failures = sum(
        any(
            not isinstance(wire, int)
            or wire < 0
            or wire >= controller_width
            for wire in gate.wires
        )
        or len(set(gate.wires)) != len(gate.wires)
        for gate in controller
    )
    expected_bank_bases = tuple(41 + 131 * i for i in range(CAPACITY))
    expected_link_bases = tuple(
        41 + 131 * CAPACITY + 382 * i
        for i in range(CAPACITY - 1)
    )
    exact = (
        len(program) == STATIONS == 8 * BANKS - 5
        and program == frozen_program
        and data_width == EXPECTED_DATA_WIDTH
        and bank_bases == expected_bank_bases
        and link_bases == expected_link_bases
        and dict(sorted(row_kinds.items())) == EXPECTED_ROW_KINDS
        and primitive["exact"]
        and not failures
        and controller_structure_failures == 0
    )
    return {
        "banks": BANKS,
        "capacity": CAPACITY,
        "rows_checked": len(program),
        "row_kind_counts": dict(sorted(row_kinds.items())),
        "semantic_gate_kind_counts":
            dict(sorted(semantic_kinds.items())),
        "controlled_gate_total": controlled_gate_total,
        "controller_gate_count": len(controller),
        "controller_structure_failures": controller_structure_failures,
        "data_width": data_width,
        "bank_bases": bank_bases,
        "link_bases": link_bases,
        "mapped_rows_sha256": mapped_hasher.hexdigest(),
        "row_failure_count": len(failures),
        "row_failures": failures,
        "all_51_rows_clean": exact,
        "exact": exact,
    }


DILATION_CHUNK_BITS = 10
DILATION_CHUNK_MASK = (1 << DILATION_CHUNK_BITS) - 1


def _dilate_chunk(value: int) -> int:
    output = 0
    earlier_selected = 0
    for position in range(DILATION_CHUNK_BITS):
        if (value >> position) & 1:
            output |= 1 << (position + earlier_selected)
            earlier_selected += 1
    return output


DILATION_TABLE = np.asarray(
    [_dilate_chunk(value) for value in range(1 << DILATION_CHUNK_BITS)],
    dtype=np.int64,
)
DILATION_POPCOUNTS = np.asarray(
    [value.bit_count() for value in range(1 << DILATION_CHUNK_BITS)],
    dtype=np.int64,
)


@numba.njit(cache=False)
def _fill_dilated_combinations(
    output: np.ndarray,
    start: int,
    prefix: int,
    universe: int,
    combination: int,
    limit: int,
    dilation_table: np.ndarray,
    dilation_popcounts: np.ndarray,
) -> tuple[int, int]:
    """Fill one bounded batch using the Cycle-761 Gosper/dilation order."""

    filled = 0
    while combination < limit and filled < output.size:
        value = 0
        earlier_selected = 0
        base = 0
        while base < universe:
            chunk = (
                combination >> base
            ) & DILATION_CHUNK_MASK
            value |= int(dilation_table[chunk]) << (
                base + earlier_selected
            )
            earlier_selected += int(dilation_popcounts[chunk])
            base += DILATION_CHUNK_BITS
        output[filled] = np.uint64(prefix | (value << start))
        filled += 1
        low = combination & -combination
        raised = combination + low
        combination = raised + (
            ((raised ^ combination) // low) >> 2
        )
    return filled, combination


def cycle_stratum_batches(
    stations: int, occupied: int, batch_size: int
):
    """Yield every C_n independent mask in one k-stratum, in bounded batches."""

    cases = [(1, stations - 1, occupied, 0)]
    if occupied:
        cases.append((2, stations - 3, occupied - 1, 1))
    for start, length, selected, prefix in cases:
        if selected < 0 or selected > (length + 1) // 2:
            continue
        if selected == 0:
            yield np.asarray([prefix], dtype="<u8")
            continue
        universe = length - selected + 1
        combination = (1 << selected) - 1
        limit = 1 << universe
        while combination < limit:
            batch = np.empty(batch_size, dtype="<u8")
            filled, combination = _fill_dilated_combinations(
                batch,
                start,
                prefix,
                universe,
                combination,
                limit,
                DILATION_TABLE,
                DILATION_POPCOUNTS,
            )
            if filled <= 0:
                raise AssertionError("dilation generator made no progress")
            yield batch[:filled]


def batch_to_bitplanes(
    batch: np.ndarray, occupied: int
) -> tuple[tuple[int, ...], dict[str, int]]:
    rows = int(batch.size)
    byte_matrix = batch.view(np.uint8).reshape(rows, 8)
    populations = np.bitwise_count(batch)
    population_failures = int(
        np.count_nonzero(populations != occupied)
    )
    ring_mask = np.uint64((1 << STATIONS) - 1)
    rotated = (
        ((batch << np.uint64(1)) & ring_mask)
        | (batch >> np.uint64(STATIONS - 1))
    )
    adjacency_failures = int(np.count_nonzero(batch & rotated))
    outside_mask = np.uint64(((1 << 64) - 1) ^ int(ring_mask))
    range_failures = int(np.count_nonzero(batch & outside_mask))
    unpacked = np.unpackbits(
        byte_matrix, axis=1, bitorder="little"
    )[:, :STATIONS]
    packed = np.packbits(
        unpacked.T, axis=1, bitorder="little"
    )
    planes = tuple(
        int.from_bytes(packed[station].tobytes(), "little")
        for station in range(STATIONS)
    )
    return planes, {
        "rows": rows,
        "population_failures": population_failures,
        "input_adjacency_failures": adjacency_failures,
        "input_range_failures": range_failures,
        "first_mask": int(batch[0]) if rows else -1,
        "last_mask": int(batch[-1]) if rows else -1,
        "mask_sum_mod_2_64": int(batch.sum(dtype=np.uint64)),
    }


def bitsliced_population_count(
    planes: list[int] | tuple[int, ...],
) -> tuple[int, ...]:
    width = max(1, len(planes).bit_length())
    output = [0] * width
    for plane in planes:
        carry = plane
        digit = 0
        while carry:
            if digit == len(output):
                output.append(0)
            overlap = output[digit] & carry
            output[digit] ^= carry
            carry = overlap
            digit += 1
    return tuple(output)


ORBIT_FAILURE_KEYS = (
    "translation_failure_config_steps",
    "B_rail_failure_config_steps",
    "work_failure_config_steps",
    "population_failure_config_steps",
    "token_support_failure_config_steps",
    "adjacency_failure_config_steps",
    "ownership_failure_config_steps",
    "distance_transport_failure_config_steps",
    "rail_closure_failures",
)


def empty_orbit_stats() -> dict[str, int]:
    return {
        "configurations": 0,
        "station_steps": 0,
        "occupied_station_invariant_checks": 0,
        "distance_pair_incidence_checks": 0,
        "ownership_violation_station_incidences": 0,
        "adjacency_pair_incidences": 0,
        **{key: 0 for key in ORBIT_FAILURE_KEYS},
    }


def evaluate_rail_bitplanes(
    original: tuple[int, ...], rows: int, occupied: int
) -> dict[str, int]:
    """Cycle-761 bit-plane clean-work quotient, at all 51 Q boundaries."""

    row_full = (1 << rows) - 1
    a = list(original)
    b = [0] * STATIONS
    stats = empty_orbit_stats()
    stats["configurations"] = rows

    for step in range(STATIONS):
        translation_bad = 0
        b_bad = 0
        work_bad = 0
        token_support_bad = 0
        adjacency_bad = 0
        ownership_bad = 0

        for station in range(STATIONS):
            expected = original[(station - step) % STATIONS]
            translation_bad |= a[station] ^ expected
            b_bad |= b[station]
            token_support_bad |= (
                (a[station] | b[station]) & ~row_full
            )
            right = (station + 1) % STATIONS
            incidence = a[station] & a[right]
            stats["adjacency_pair_incidences"] += (
                incidence.bit_count()
            )
            adjacency_bad |= incidence
            left = (station - 1) % STATIONS
            dirty = (
                a[left]
                | a[right]
                | b[left]
                | b[station]
                | b[right]
                | work_bad
            )
            violation = a[station] & dirty
            stats["ownership_violation_station_incidences"] += (
                violation.bit_count()
            )
            ownership_bad |= violation

        population_bad = 0
        actual_count = bitsliced_population_count(a + b)
        for digit, observed in enumerate(actual_count):
            expected = row_full if (occupied >> digit) & 1 else 0
            population_bad |= observed ^ expected

        stats["translation_failure_config_steps"] += (
            translation_bad.bit_count()
        )
        stats["B_rail_failure_config_steps"] += b_bad.bit_count()
        stats["work_failure_config_steps"] += work_bad.bit_count()
        stats["population_failure_config_steps"] += (
            population_bad.bit_count()
        )
        stats["token_support_failure_config_steps"] += (
            token_support_bad.bit_count()
        )
        stats["adjacency_failure_config_steps"] += (
            adjacency_bad.bit_count()
        )
        stats["ownership_failure_config_steps"] += (
            ownership_bad.bit_count()
        )
        # A translated bit-plane configuration preserves every pair distance
        # by the independently checked cyclic isometry.  Thus any possible
        # distance-transport failure is contained in translation_bad.
        stats["distance_transport_failure_config_steps"] += (
            translation_bad.bit_count()
        )
        stats["occupied_station_invariant_checks"] += rows * occupied
        stats["distance_pair_incidence_checks"] += (
            rows * comb(occupied, 2)
        )
        stats["station_steps"] += rows

        # Exact action of the Cycle-761 two disjoint SWAP layers R1 then R2.
        a, b = b, a
        for station in range(STATIONS):
            target = (station + 1) % STATIONS
            b[station], a[target] = a[target], b[station]

    closure_bad = 0
    for observed, expected in zip(a, original):
        closure_bad |= observed ^ expected
    for plane in b:
        closure_bad |= plane
    stats["rail_closure_failures"] = closure_bad.bit_count()
    return stats


def add_stats(target: dict[str, int], source: dict[str, int]) -> None:
    for key, value in source.items():
        target[key] += value


def cyclic_distance_isometry_failures(stations: int) -> int:
    failures = 0
    for shift in range(stations):
        for left in range(stations):
            for right in range(left + 1, stations):
                original = min(
                    (right - left) % stations,
                    (left - right) % stations,
                )
                moved_left = (left + shift) % stations
                moved_right = (right + shift) % stations
                moved = min(
                    (moved_right - moved_left) % stations,
                    (moved_left - moved_right) % stations,
                )
                failures += int(original != moved)
    return failures


def batch_zero_violations(
    validation: dict[str, int], orbit: dict[str, int]
) -> bool:
    return (
        validation["population_failures"] == 0
        and validation["input_adjacency_failures"] == 0
        and validation["input_range_failures"] == 0
        and all(orbit[key] == 0 for key in ORBIT_FAILURE_KEYS)
        and orbit["ownership_violation_station_incidences"] == 0
        and orbit["adjacency_pair_incidences"] == 0
    )


def benchmark_certificate(
    counts: tuple[int, ...], rows_exact: bool
) -> dict[str, object]:
    if not rows_exact:
        return {"exact": False, "error": "row-clean prerequisite failed"}

    # Compile the bounded generator before the measured region.
    warm_iterator = cycle_stratum_batches(STATIONS, 3, 32)
    warm_batch = next(warm_iterator)
    if int(warm_batch.size) != 32:
        raise AssertionError("generator warm-up failed")

    iterator = cycle_stratum_batches(
        STATIONS, BENCHMARK_K, BITPLANE_BATCH
    )
    generated_seconds = 0.0
    transpose_seconds = 0.0
    evaluator_seconds = 0.0
    rows = 0
    zero_violations = True
    first_slice: dict[str, object] | None = None

    for ordinal in range(BENCHMARK_BATCHES):
        marked = perf_counter()
        batch = next(iterator)
        generated_seconds += perf_counter() - marked

        marked = perf_counter()
        planes, validation = batch_to_bitplanes(batch, BENCHMARK_K)
        transpose_seconds += perf_counter() - marked

        marked = perf_counter()
        orbit = evaluate_rail_bitplanes(
            planes, int(batch.size), BENCHMARK_K
        )
        evaluator_seconds += perf_counter() - marked
        rows += int(batch.size)
        zero_violations &= batch_zero_violations(validation, orbit)
        if ordinal == 0:
            first_slice = {
                "scope": (
                    f"first {int(batch.size)} masks of complete stratum "
                    f"k={BENCHMARK_K}; rate/determinism slice only"
                ),
                "rows": int(batch.size),
                "raw_bytes_sha256":
                    sha256(batch.tobytes(order="C")).hexdigest(),
                "validation_sha256": stable_digest(validation),
                "orbit_sha256": stable_digest(orbit),
            }

    pipeline_seconds = (
        generated_seconds + transpose_seconds + evaluator_seconds
    )
    measured_steps = rows * STATIONS
    pipeline_rate = measured_steps / pipeline_seconds
    evaluator_rate = measured_steps / evaluator_seconds
    effective_rate = (
        pipeline_rate
        * RATE_DERATE_NUMERATOR
        / RATE_DERATE_DENOMINATOR
    )

    prefix = 0
    selected_k_max = -1
    estimates = []
    for occupied, count in enumerate(counts):
        prefix += count
        steps = prefix * STATIONS
        estimate = steps / effective_rate
        fits = estimate + BUDGET_RESERVE_SEC < AUDIT_TIMEOUT_SEC
        estimates.append({
            "k_max": occupied,
            "configurations": prefix,
            "station_steps": steps,
            "conservative_estimated_seconds": round(estimate, 6),
            "plus_reserve_fits": fits,
        })
        if fits:
            selected_k_max = occupied

    if selected_k_max < 0:
        raise AssertionError("benchmark admits no complete stratum")
    full_estimate = EXPECTED_FULL_STEPS / effective_rate
    full_sweep_fits = (
        full_estimate + BUDGET_RESERVE_SEC < AUDIT_TIMEOUT_SEC
    )
    selected = estimates[selected_k_max]
    next_estimate = (
        estimates[selected_k_max + 1]
        if selected_k_max + 1 < len(estimates)
        else None
    )
    largest_exact = (
        selected["plus_reserve_fits"]
        and (
            next_estimate is None
            or not next_estimate["plus_reserve_fits"]
        )
    )
    exact = (
        rows == BENCHMARK_BATCHES * BITPLANE_BATCH
        and rows < counts[BENCHMARK_K]
        and zero_violations
        and first_slice is not None
        and pipeline_rate > 0
        and evaluator_rate > 0
        and effective_rate > 0
        and largest_exact
        and (
            full_sweep_fits
            == (selected_k_max == len(counts) - 1)
        )
    )
    return {
        "benchmark_scope": (
            f"first {rows} masks of k={BENCHMARK_K}; "
            "declared rate measurement only, not sweep coverage"
        ),
        "benchmark_rows": rows,
        "benchmark_station_steps": measured_steps,
        "batch_size": BITPLANE_BATCH,
        "batches": BENCHMARK_BATCHES,
        "generated_seconds": round(generated_seconds, 6),
        "transpose_seconds": round(transpose_seconds, 6),
        "evaluator_seconds": round(evaluator_seconds, 6),
        "pipeline_seconds": round(pipeline_seconds, 6),
        "measured_evaluator_station_steps_per_second":
            round(evaluator_rate, 3),
        "measured_pipeline_station_steps_per_second":
            round(pipeline_rate, 3),
        "rate_derating": (
            RATE_DERATE_NUMERATOR,
            RATE_DERATE_DENOMINATOR,
        ),
        "budget_effective_station_steps_per_second":
            round(effective_rate, 3),
        "budget_reserve_seconds": BUDGET_RESERVE_SEC,
        "full_sweep_conservative_estimated_seconds":
            round(full_estimate, 6),
        "full_sweep_plus_reserve_fits": full_sweep_fits,
        "selected_k_max": selected_k_max,
        "selected_prefix": selected,
        "next_prefix": next_estimate,
        "largest_complete_prefix_by_budget": largest_exact,
        "zero_violations": zero_violations,
        "first_slice": first_slice,
        "exact": exact,
    }


def sweep_certificate(
    counts: tuple[int, ...],
    selected_k_max: int,
) -> dict[str, object]:
    started = perf_counter()
    aggregate = empty_orbit_stats()
    completed: list[int] = []
    per_k: dict[int, dict[str, object]] = {}
    batch_count = 0
    validation_failures = {
        "population_failures": 0,
        "input_adjacency_failures": 0,
        "input_range_failures": 0,
    }
    evidence_hasher = sha256()
    transpose_seconds = 0.0
    evaluator_seconds = 0.0

    for occupied in range(selected_k_max + 1):
        stratum_started = perf_counter()
        stratum_count = 0
        stratum_batches = 0
        for batch in cycle_stratum_batches(
            STATIONS, occupied, BITPLANE_BATCH
        ):
            marked = perf_counter()
            planes, validation = batch_to_bitplanes(batch, occupied)
            transpose_seconds += perf_counter() - marked

            marked = perf_counter()
            orbit = evaluate_rail_bitplanes(
                planes, int(batch.size), occupied
            )
            evaluator_seconds += perf_counter() - marked
            add_stats(aggregate, orbit)
            for key in validation_failures:
                validation_failures[key] += validation[key]
            evidence_hasher.update(stable_json_bytes({
                "batch": batch_count,
                "k": occupied,
                "validation": validation,
                "orbit": orbit,
            }))
            stratum_count += int(batch.size)
            stratum_batches += 1
            batch_count += 1

        stratum_complete = stratum_count == counts[occupied]
        if stratum_complete:
            completed.append(occupied)
        per_k[occupied] = {
            "expected": counts[occupied],
            "streamed": stratum_count,
            "batches": stratum_batches,
            "complete": stratum_complete,
            "seconds": round(perf_counter() - stratum_started, 6),
        }
        emit_line(
            "SWEEP_PROGRESS "
            f"k={occupied} configurations={stratum_count} "
            f"complete={stratum_complete} "
            f"elapsed={perf_counter() - started:.3f}s"
        )

    elapsed = perf_counter() - started
    expected_configurations = sum(counts[:selected_k_max + 1])
    expected_steps = expected_configurations * STATIONS
    expected_occupied_checks = sum(
        occupied * counts[occupied] * STATIONS
        for occupied in range(selected_k_max + 1)
    )
    expected_distance_checks = sum(
        comb(occupied, 2) * counts[occupied] * STATIONS
        for occupied in range(selected_k_max + 1)
    )
    isometry_failures = cyclic_distance_isometry_failures(STATIONS)
    zero_violations = (
        all(value == 0 for value in validation_failures.values())
        and all(aggregate[key] == 0 for key in ORBIT_FAILURE_KEYS)
        and aggregate["ownership_violation_station_incidences"] == 0
        and aggregate["adjacency_pair_incidences"] == 0
        and isometry_failures == 0
    )
    complete_prefix = (
        tuple(completed) == tuple(range(selected_k_max + 1))
        and all(
            per_k[occupied]["complete"]
            for occupied in range(selected_k_max + 1)
        )
        and aggregate["configurations"] == expected_configurations
        and aggregate["station_steps"] == expected_steps
        and aggregate["occupied_station_invariant_checks"]
        == expected_occupied_checks
        and aggregate["distance_pair_incidence_checks"]
        == expected_distance_checks
    )
    full_sweep = selected_k_max == len(counts) - 1
    scope = (
        "full"
        if full_sweep
        else f"partial (declared strata k=0..{selected_k_max})"
    )
    return {
        "sweep_scope": scope,
        "full_sweep": full_sweep,
        "completed_strata": tuple(completed),
        "partially_evaluated_strata": (),
        "unswept_strata": tuple(
            range(selected_k_max + 1, len(counts))
        ),
        "configurations": expected_configurations,
        "station_steps": expected_steps,
        "per_k": per_k,
        "batch_count": batch_count,
        "bitplane_batch": BITPLANE_BATCH,
        "validation_failures": validation_failures,
        "orbit_stats": aggregate,
        "cyclic_distance_isometry_failures": isometry_failures,
        "distance_check_method": (
            "direct bit-plane equality to the expected cyclic translation "
            "at every station-step, composed with an exhaustive exact "
            "C_51 cyclic-distance isometry check"
        ),
        "zero_violations": zero_violations,
        "complete_prefix_exact": complete_prefix,
        "orbit_evidence_sha256": evidence_hasher.hexdigest(),
        "transpose_seconds": round(transpose_seconds, 6),
        "evaluator_seconds": round(evaluator_seconds, 6),
        "runtime_seconds": round(elapsed, 6),
        "station_steps_per_second":
            round(expected_steps / elapsed, 3),
        "exact": complete_prefix and zero_violations,
    }


def ownership_reasons(
    a_mask: int,
    b_mask: int,
    work_mask: int,
    station: int,
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


def near_miss_certificate() -> dict[str, object]:
    rows = []
    passed = 0
    violating_stations = 0
    reason_incidences = 0
    for left in range(STATIONS):
        right = (left + 1) % STATIONS
        mask = (1 << left) | (1 << right)
        violations = tuple(
            (station, ownership_reasons(mask, 0, 0, station))
            for station in range(STATIONS)
            if ownership_reasons(mask, 0, 0, station)
        )
        sites = tuple(station for station, _reasons in violations)
        reasons = tuple(
            reason
            for _station, station_reasons in violations
            for reason in station_reasons
        )
        exact = (
            sites == tuple(sorted((left, right)))
            and len(violations) == 2
            and len(reasons) == 2
        )
        passed += int(exact)
        violating_stations += len(violations)
        reason_incidences += len(reasons)
        rows.append((left, right, sites, reasons, exact))
    exact = (
        passed == STATIONS
        and violating_stations == 2 * STATIONS
        and reason_incidences == 2 * STATIONS
    )
    return {
        "adjacent_pair_controls": STATIONS,
        "controls_passed": passed,
        "violating_stations": violating_stations,
        "expected_violating_stations": 2 * STATIONS,
        "reason_incidences": reason_incidences,
        "near_miss_table_sha256": stable_digest(rows),
        "exact": exact,
    }


def determinism_certificate(
    census: dict[str, object],
    benchmark: dict[str, object],
) -> dict[str, object]:
    iterator = cycle_stratum_batches(
        STATIONS, BENCHMARK_K, BITPLANE_BATCH
    )
    batch = next(iterator)
    planes, validation = batch_to_bitplanes(batch, BENCHMARK_K)
    orbit = evaluate_rail_bitplanes(
        planes, int(batch.size), BENCHMARK_K
    )
    repeated = {
        "scope": (
            f"first {int(batch.size)} masks of complete stratum "
            f"k={BENCHMARK_K}; rate/determinism slice only"
        ),
        "rows": int(batch.size),
        "raw_bytes_sha256":
            sha256(batch.tobytes(order="C")).hexdigest(),
        "validation_sha256": stable_digest(validation),
        "orbit_sha256": stable_digest(orbit),
    }
    original = benchmark["first_slice"]
    slice_exact = repeated == original
    census_exact = (
        census["census_sha256"]
        == census["repeated_census_sha256"]
        and census["census_repeat_byte_identical"]
    )
    return {
        "declared_slice": repeated["scope"],
        "first_slice": original,
        "repeated_slice": repeated,
        "slice_byte_identical": slice_exact,
        "census_byte_identical": census_exact,
        "zero_violations": batch_zero_violations(validation, orbit),
        "exact": (
            slice_exact
            and census_exact
            and batch_zero_violations(validation, orbit)
        ),
    }


def run_certificate(
    name: str, function: object, *args: object
) -> dict[str, object]:
    try:
        report = function(*args)
        if not isinstance(report, dict):
            raise TypeError(f"{name} did not return a dict")
        return report
    except Exception as error:
        return {
            "exact": False,
            "error": f"{type(error).__name__}: {error}"[:1000],
        }


def main() -> int:
    started = perf_counter()
    checks: dict[str, bool] = {}

    anchors = run_certificate(
        "module_anchor_certificate", module_anchor_certificate
    )
    checks["A"] = bool(anchors.get("exact"))
    emit_line(
        f"{'PASS' if checks['A'] else 'FAIL'} "
        "A_landed_module_anchors_and_copy_provenance "
        f"sha={stable_digest(anchors)} "
        f"copied={COPIED_MODULE_PROVENANCE}"
    )

    census = run_certificate("census_certificate", census_certificate)
    checks["B"] = bool(census.get("exact"))
    emit_line(
        "CENSUS_PRE_SWEEP "
        f"L51_scalar={census.get('independent_scalar_L51')} "
        f"L51_census={census.get('path_polynomial_recurrence_total')} "
        f"full_station_steps={census.get('full_orbit_station_steps')}"
    )
    emit_line(
        "CENSUS_STRATA "
        + ", ".join(
            f"k={occupied}:{count}"
            for occupied, count in enumerate(
                census.get("counts_by_k", ())
            )
        )
    )
    emit_line(
        f"{'PASS' if checks['B'] else 'FAIL'} "
        "B_L51_census_equality_and_strata_recurrence "
        f"L51={census.get('independent_scalar_L51')} "
        f"digest={census.get('census_sha256')}"
    )

    rows = run_certificate(
        "row_clean_work_certificate", row_clean_work_certificate
    )
    checks["C"] = bool(rows.get("exact"))
    emit_line(
        "ROWS_C7_COUNTS "
        f"{json.dumps(rows.get('row_kind_counts', {}), sort_keys=True)}"
    )
    emit_line(
        f"{'PASS' if checks['C'] else 'FAIL'} "
        "C_all_51_rows_clean_C7_table_law "
        f"rows={rows.get('rows_checked')} "
        f"data_width={rows.get('data_width')} "
        f"row_failures={rows.get('row_failure_count')}"
    )

    counts = tuple(census.get("counts_by_k", ()))
    benchmark = run_certificate(
        "benchmark_certificate",
        benchmark_certificate,
        counts,
        bool(rows.get("exact")),
    )
    emit_line(
        "BENCHMARK_DECLARED "
        f"scope={benchmark.get('benchmark_scope')} "
        "evaluator_rate="
        f"{benchmark.get('measured_evaluator_station_steps_per_second')} "
        "pipeline_rate="
        f"{benchmark.get('measured_pipeline_station_steps_per_second')} "
        "budget_rate="
        f"{benchmark.get('budget_effective_station_steps_per_second')}"
    )
    emit_line(
        "BUDGET_PRE_SWEEP "
        f"full_steps={EXPECTED_FULL_STEPS} "
        "full_conservative_seconds="
        f"{benchmark.get('full_sweep_conservative_estimated_seconds')} "
        f"reserve={BUDGET_RESERVE_SEC} "
        f"full_fits={benchmark.get('full_sweep_plus_reserve_fits')} "
        f"selected_k_max={benchmark.get('selected_k_max')} "
        f"selected={benchmark.get('selected_prefix')} "
        f"next={benchmark.get('next_prefix')}"
    )

    if benchmark.get("exact"):
        sweep = run_certificate(
            "sweep_certificate",
            sweep_certificate,
            counts,
            int(benchmark["selected_k_max"]),
        )
    else:
        sweep = {
            "exact": False,
            "error": "benchmark prerequisite failed",
            "sweep_scope": "none",
            "station_steps": 0,
            "zero_violations": False,
            "runtime_seconds": 0,
            "station_steps_per_second": 0,
        }
    checks["D"] = bool(
        benchmark.get("exact")
        and sweep.get("exact")
        and sweep.get("zero_violations")
    )
    emit_line(
        f"{'PASS' if checks['D'] else 'FAIL'} "
        "D_declared_strata_orbit_sweep_zero_violations "
        f"sweep_scope={sweep.get('sweep_scope')} "
        f"station_steps={sweep.get('station_steps')} "
        f"rate={sweep.get('station_steps_per_second')} "
        f"zero_violations={sweep.get('zero_violations')}"
    )

    near_miss = run_certificate(
        "near_miss_certificate", near_miss_certificate
    )
    determinism = run_certificate(
        "determinism_certificate",
        determinism_certificate,
        census,
        benchmark,
    )
    elapsed = perf_counter() - started

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "scope": "Cycle 779 seventh anchor b=7 n=51",
        "A_module_anchors": anchors,
        "B_census": census,
        "C_rows": rows,
        "D_benchmark": benchmark,
        "D_sweep": sweep,
        "E_near_miss": near_miss,
        "E_determinism": determinism,
        "runtime_seconds": round(elapsed, 6),
    }
    provisional = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    stdout_bound = (
        STDOUT_BYTES_EMITTED + len(provisional.encode()) + 4096
        < STDOUT_LIMIT_BYTES
    )
    checks["E"] = bool(
        near_miss.get("exact")
        and determinism.get("exact")
        and elapsed < AUDIT_TIMEOUT_SEC
        and stdout_bound
    )
    emit_line(
        f"{'PASS' if checks['E'] else 'FAIL'} "
        "E_near_miss_determinism_runtime_stdout_bounds "
        f"near_miss_violating_stations="
        f"{near_miss.get('violating_stations')} "
        f"slice_byte_identical="
        f"{determinism.get('slice_byte_identical')} "
        f"runtime={elapsed:.6f}s stdout_bound={stdout_bound}"
    )

    report["checks"] = checks
    report["checks_passed"] = sum(checks.values())
    report["checks_failed"] = sum(not value for value in checks.values())
    report["pass"] = all(checks.values())
    report["terminal"] = (
        "CYCLE779_B7_EXHAUSTIVE_ANCHOR_ALL_PASS"
        if report["pass"]
        else "CYCLE779_B7_EXHAUSTIVE_ANCHOR_HONEST_FAIL"
    )
    report["report_sha256"] = stable_digest(report)
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    if STDOUT_BYTES_EMITTED + len(final_json.encode()) + 1 >= (
        STDOUT_LIMIT_BYTES
    ):
        emit_line(json.dumps({
            "checks": checks,
            "pass": False,
            "reason": "stdout bound exceeded at final serialization",
            "terminal": "CYCLE779_B7_EXHAUSTIVE_ANCHOR_HONEST_FAIL",
        }, sort_keys=True, separators=(",", ":")))
        return 1
    emit_line(final_json)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
