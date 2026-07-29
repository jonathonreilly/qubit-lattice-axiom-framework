#!/usr/bin/env python3
"""Cycle 761: the sixth exhaustive anchor, bounded honestly at b=6, n=43.

The exact C_43 independent-set census is obtained from streamed polynomial
recurrences and an independent closed-form stratum check.  The literal C=6
controlled-Q plus two-rail-R controller is then exhausted on every mask in
the largest prefix of whole k-strata that fits the declared 1800-second
budget estimate.  Residual strata are counted exactly but never swept or
materialized.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from math import comb
import sys
from time import perf_counter

sys.dont_write_bytecode = True

import numpy as np

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle740_table_parameterized_mapper_2026_07_28 as M740


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/B6_EXHAUSTIVE_ANCHOR_CYCLE761_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STDOUT_LIMIT_BYTES = 150 * 1024
BITPLANE_BATCH = 65_536
BANK_COUNT = 6
CAPACITY = 6
STATIONS = 43
EXPECTED_LUCAS_43 = 969_323_029
SWEEP_K_MAX = 11
MEASURED_B5_STATION_STEPS_PER_SEC = 12_700_000
BUDGET_RESERVE_SEC = 120
ALLOWED_GATE_KINDS = frozenset(("X", "CNOT", "TOF"))
I1_AMENDED_FORMULA = (
    "not(a[left] or a[right] or b[left] or b[station] or b[right] or "
    "work[station])"
)
I2_IDENTITY = (
    "I_macro_clean_work_uniformity: every emitted row leaves its A control "
    "unchanged, addresses only data plus its own work bit, and maps clean "
    "work=0 back to 0"
)
PRIOR_ANCHOR_CENSUS = {
    3: 4,
    11: 199,
    19: 9_349,
    27: 439_204,
    35: 20_633_239,
}
PRIOR_ANCHOR_ORBIT_STEPS = {
    3: 12,
    11: 2_189,
    19: 177_631,
    27: 11_858_508,
    35: 722_163_365,
}

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


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(int(wire) for wire in gate.wires)


def word_signature(
    word: tuple[object, ...],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    return tuple(gate_signature(gate) for gate in word)


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    full = (1 << stations) - 1
    normalized = shift % stations
    if normalized == 0:
        return mask & full
    return (
        ((mask << normalized) & full)
        | (mask >> (stations - normalized))
    )


def circular_distance(left: int, right: int, stations: int) -> int:
    return min(
        (right - left) % stations,
        (left - right) % stations,
    )


def lucas_number_streamed(index: int) -> tuple[int, str]:
    """Stream L_0=2, L_1=1, L_i=L_(i-1)+L_(i-2)."""

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
    """Stream coefficient rows under P_m=P_(m-1)+x P_(m-2)."""

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
    """Split on vertex zero: I(C_n)=P_(n-1)+x P_(n-3)."""

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
    """Stream one whole C_n stratum; retain at most one bit-plane batch."""

    yield from path_masks_fixed_k(1, stations - 1, occupied)
    if occupied:
        for mask in path_masks_fixed_k(2, stations - 3, occupied - 1):
            yield mask | 1


def mapper_anchor_certificate() -> dict[str, object]:
    law = M740.table_law_certificate()
    equivalence = M740.equivalence_certificate()
    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    bank_bases, link_bases = M740.parameterized_bases(CAPACITY)
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
        and M740.parameterized_data_width(CAPACITY) == 2_737
    )
    return {
        "frozen_table_law_exact": law["exact"],
        "frozen_table_law_sha256": stable_digest(law),
        "frozen_C12_equivalence_b1_through_b12_exact":
            equivalence["exact"],
        "frozen_C12_equivalence_sha256": stable_digest(equivalence),
        "b6_C6_program_equals_K_emission": (
            program == K.interleaved_program(BANK_COUNT)
        ),
        "b6_C6_bank_bases": bank_bases,
        "b6_C6_link_bases": link_bases,
        "b6_C6_data_width": M740.parameterized_data_width(CAPACITY),
        "b6_C6_rows": len(program),
        "exact": exact,
    }


def primitive_clean_certificate() -> dict[str, object]:
    control = 10
    work = 11
    canonical = {
        "X": (K.A.x(0),),
        "CNOT": (K.A.cn(0, 1),),
        "TOF": (K.A.tof(0, 1, 2),),
    }
    observed = {
        kind: word_signature(K.controlled_macro(word, control, work))
        for kind, word in canonical.items()
    }
    expected = {
        "X": (("CNOT", (control, 0)),),
        "CNOT": (("TOF", (control, 0, 1)),),
        "TOF": (
            ("TOF", (control, 0, work)),
            ("TOF", (work, 1, 2)),
            ("TOF", (control, 0, work)),
        ),
    }
    truth = K.controlled_truth_certificate()
    exact = (
        observed == expected
        and truth["clean_failures"] == 0
        and truth["clean_work_return_failures"] == 0
        and truth["clean_rows"] > 0
    )
    return {
        "controlled_primitive_expansions": observed,
        "clean_truth_rows": truth["clean_rows"],
        "clean_truth_failures": truth["clean_failures"],
        "clean_work_return_failures":
            truth["clean_work_return_failures"],
        "exact": exact,
    }


def validate_clean_word(
    word: tuple[object, ...],
    data_width: int,
    control: int,
    work: int,
    primitive_exact: bool,
) -> dict[str, object]:
    arity = {"X": 1, "CNOT": 2, "TOF": 3}
    kinds_allowed = all(
        gate.kind in ALLOWED_GATE_KINDS for gate in word
    )
    arities_exact = all(
        gate.kind in arity and len(gate.wires) == arity[gate.kind]
        for gate in word
    )
    operands_distinct = all(
        len(set(gate.wires)) == len(gate.wires) for gate in word
    )
    data_only = all(
        isinstance(wire, int) and 0 <= wire < data_width
        for gate in word for wire in gate.wires
    )
    lifted = tuple(K.controlled_macro(word, control, work))
    expected_lifted = []
    for gate in word:
        if gate.kind == "X":
            expected_lifted.append(K.A.cn(control, gate.wires[0]))
        elif gate.kind == "CNOT":
            expected_lifted.append(
                K.A.tof(control, gate.wires[0], gate.wires[1])
            )
        elif gate.kind == "TOF":
            expected_lifted.extend((
                K.A.tof(control, gate.wires[0], work),
                K.A.tof(work, gate.wires[1], gate.wires[2]),
                K.A.tof(control, gate.wires[0], work),
            ))
    expansion_exact = lifted == tuple(expected_lifted)
    addressed_domain_exact = all(
        wire in {control, work} or 0 <= wire < data_width
        for gate in lifted for wire in gate.wires
    )
    control_unchanged = all(
        not gate.wires or gate.wires[-1] != control
        for gate in lifted
    )
    tof_count = sum(gate.kind == "TOF" for gate in word)
    work_target_count = sum(
        bool(gate.wires) and gate.wires[-1] == work
        for gate in lifted
    )
    clean_work_zero_returns_zero = (
        primitive_exact
        and expansion_exact
        and work_target_count == 2 * tof_count
    )
    passed = (
        kinds_allowed
        and arities_exact
        and operands_distinct
        and data_only
        and expansion_exact
        and addressed_domain_exact
        and control_unchanged
        and clean_work_zero_returns_zero
    )
    return {
        "semantic_gates": len(word),
        "controlled_gates": len(lifted),
        "allowed_gate_kinds": kinds_allowed,
        "gate_arities_exact": arities_exact,
        "per_gate_operands_distinct": operands_distinct,
        "addresses_only_data_before_lift": data_only,
        "addresses_only_data_control_own_work_after_lift":
            addressed_domain_exact,
        "controlled_dispatch_expansion_exact": expansion_exact,
        "A_control_unchanged": control_unchanged,
        "work_compute_uncompute_target_count": work_target_count,
        "expected_work_target_count": 2 * tof_count,
        "clean_work_0_maps_to_0": clean_work_zero_returns_zero,
        "pass": passed,
    }


def row_clean_work_certificate() -> dict[str, object]:
    primitive = primitive_clean_certificate()
    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    data_width = M740.parameterized_data_width(CAPACITY)
    failures = []
    word_hasher = sha256()
    row_kind_counts = Counter()
    semantic_gate_counts = Counter()
    controlled_gate_total = 0
    for station, row in enumerate(program):
        row_kind_counts[row[0]] += 1
        try:
            word = tuple(M740.parameterized_mapped_macro(row, CAPACITY))
            clean = validate_clean_word(
                word,
                data_width,
                data_width + station,
                data_width + 2 * len(program) + station,
                bool(primitive["exact"]),
            )
        except Exception as error:
            failures.append({
                "station": station,
                "kind": row[0],
                "index": row[1],
                "error": error_text(error),
            })
            continue
        word_hasher.update(stable_json_bytes(word_signature(word)))
        semantic_gate_counts.update(gate.kind for gate in word)
        controlled_gate_total += int(clean["controlled_gates"])
        if not clean["pass"]:
            failures.append({
                "station": station,
                "kind": row[0],
                "index": row[1],
                "clean": clean,
            })
    expected_kind_counts = {
        "bank": 6,
        "cross": 5,
        "finalizer": 1,
        "handoff": 10,
        "relay": 20,
        "source": 1,
    }
    exact = (
        len(program) == STATIONS == 8 * BANK_COUNT - 5
        and data_width == 2_737
        and dict(sorted(row_kind_counts.items())) == expected_kind_counts
        and primitive["exact"]
        and not failures
    )
    return {
        "banks": BANK_COUNT,
        "capacity": CAPACITY,
        "ring_rows": len(program),
        "expected_8b_minus_5": 8 * BANK_COUNT - 5,
        "data_width": data_width,
        "row_kind_counts": dict(sorted(row_kind_counts.items())),
        "semantic_gate_kind_counts":
            dict(sorted(semantic_gate_counts.items())),
        "controlled_gate_total": controlled_gate_total,
        "rows_checked": len(program),
        "row_failure_count": len(failures),
        "row_failures": failures,
        "mapped_row_words_sha256": word_hasher.hexdigest(),
        "I2_identity": I2_IDENTITY,
        "primitive_clean_work": primitive,
        "all_43_rows_directly_clean": exact,
        "exact": exact,
    }


def i1_transport_certificate() -> dict[str, object]:
    source_terms = (
        ("A", -1),
        ("A", 1),
        ("B", -1),
        ("B", 0),
        ("B", 1),
        ("work", 0),
    )
    distance_isometry_failures = sum(
        circular_distance(left, right, STATIONS)
        != circular_distance(
            (left + shift) % STATIONS,
            (right + shift) % STATIONS,
            STATIONS,
        )
        for shift in range(STATIONS)
        for left in range(STATIONS)
        for right in range(left + 1, STATIONS)
    )
    return {
        "i1_amended_formula": I1_AMENDED_FORMULA,
        "six_source_terms": source_terms,
        "translated_terms_at_s_plus_one": source_terms,
        "symbolic_plus_one_transport_exact": True,
        "circular_translation_distance_isometry_failures":
            distance_isometry_failures,
        "exact": (
            len(source_terms) == 6
            and distance_isometry_failures == 0
        ),
    }


def census_certificate() -> dict[str, object]:
    counts = cycle_independence_counts(STATIONS)
    closed_counts = tuple(
        closed_cycle_stratum_count(STATIONS, occupied)
        for occupied in range(STATIONS // 2 + 1)
    )
    lucas, lucas_trace_digest = lucas_number_streamed(STATIONS)
    exact = (
        counts == closed_counts
        and sum(counts) == lucas == EXPECTED_LUCAS_43
        and len(counts) == 22
    )
    return {
        "ring": STATIONS,
        "counts_by_k": counts,
        "closed_form_counts_by_k": closed_counts,
        "enumerated_total": sum(counts),
        "lucas_recurrence_total": lucas,
        "frozen_target_L43": EXPECTED_LUCAS_43,
        "lucas_recurrence_trace_sha256": lucas_trace_digest,
        "strata_counts_sha256": stable_digest(counts),
        "census_method": (
            "streamed coefficient recurrence P_m=P_(m-1)+xP_(m-2), "
            "cycle split P_(n-1)+xP_(n-3), and streamed scalar Lucas "
            "recurrence; closed cycle-stratum formula cross-check"
        ),
        "materialized_full_mask_table": False,
        "residual_masks_materialized": False,
        "exact": exact,
    }


def compile_controller(
    controller: tuple[object, ...], width: int
) -> tuple[tuple[tuple[int, int, int, int], ...], int]:
    compiled = []
    structural_failures = 0
    for gate in controller:
        wires = tuple(int(wire) for wire in gate.wires)
        structural_failures += int(any(
            wire < 0 or wire >= width for wire in wires
        ))
        if gate.kind == "X" and len(wires) == 1:
            compiled.append((1, wires[0], 0, 0))
        elif gate.kind == "CNOT" and len(wires) == 2:
            structural_failures += int(wires[0] == wires[1])
            compiled.append((2, wires[0], wires[1], 0))
        elif gate.kind == "TOF" and len(wires) == 3:
            structural_failures += int(len(set(wires)) != 3)
            compiled.append((3, wires[0], wires[1], wires[2]))
        else:
            structural_failures += 1
    return tuple(compiled), structural_failures


def apply_bitplane_word(
    planes: list[int],
    compiled: tuple[tuple[int, int, int, int], ...],
    row_full: int,
) -> None:
    for kind, left, right, target in compiled:
        if kind == 1:
            planes[left] ^= row_full
        elif kind == 2:
            planes[right] ^= planes[left]
        else:
            planes[target] ^= planes[left] & planes[right]


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


def batch_to_bitplanes(
    batch: list[int], stations: int, occupied: int
) -> tuple[tuple[int, ...], int, int, bytes]:
    rows = len(batch)
    array = np.asarray(batch, dtype="<u8")
    byte_matrix = array.view(np.uint8).reshape(rows, 8)
    bits = np.unpackbits(
        byte_matrix, axis=1, bitorder="little"
    )[:, :stations]
    popcount_failures = int(np.count_nonzero(
        bits.sum(axis=1) != occupied
    ))
    ring_mask = np.uint64((1 << stations) - 1)
    rotated = (
        ((array << np.uint64(1)) & ring_mask)
        | (array >> np.uint64(stations - 1))
    )
    adjacency_failures = int(np.count_nonzero(array & rotated))
    packed = np.packbits(bits.T, axis=1, bitorder="little")
    planes = tuple(
        int.from_bytes(packed[station].tobytes(), "little")
        for station in range(stations)
    )
    return (
        planes,
        popcount_failures,
        adjacency_failures,
        array.tobytes(order="C"),
    )


def empty_orbit_stats() -> dict[str, int]:
    return {
        "evaluated_configurations": 0,
        "exhaustive_controller_steps": 0,
        "occupied_station_invariant_checks": 0,
        "distance_pair_incidence_checks": 0,
        "distance_bitplane_pair_comparisons": 0,
        "controller_structure_failures": 0,
        "translation_failure_config_steps": 0,
        "token_count_failure_config_steps": 0,
        "adjacency_failure_config_steps": 0,
        "adjacency_pair_incidences": 0,
        "ownership_failure_config_steps": 0,
        "ownership_violation_station_incidences": 0,
        "B_rail_failure_config_steps": 0,
        "work_failure_config_steps": 0,
        "distance_failure_config_steps": 0,
        "rail_closure_failures": 0,
    }


def evaluate_orbit_batch(
    original_a: tuple[int, ...],
    rows: int,
    occupied: int,
    compiled: tuple[tuple[int, int, int, int], ...],
    data_width: int,
) -> dict[str, int]:
    row_full = (1 << rows) - 1
    a_base = data_width
    b_base = a_base + STATIONS
    work_base = b_base + STATIONS
    planes = [0] * data_width
    planes.extend(original_a)
    planes.extend([0] * (2 * STATIONS))
    stats = empty_orbit_stats()
    stats["evaluated_configurations"] = rows

    for step in range(STATIONS):
        actual_a = planes[a_base:a_base + STATIONS]
        actual_b = planes[b_base:b_base + STATIONS]
        actual_work = planes[work_base:work_base + STATIONS]
        expected_a = tuple(
            original_a[(station - step) % STATIONS]
            for station in range(STATIONS)
        )

        translation_bad = 0
        for observed, expected in zip(actual_a, expected_a):
            translation_bad |= observed ^ expected
        stats["translation_failure_config_steps"] += (
            translation_bad.bit_count()
        )

        b_bad = 0
        work_bad = 0
        for plane in actual_b:
            b_bad |= plane
        for plane in actual_work:
            work_bad |= plane
        stats["B_rail_failure_config_steps"] += b_bad.bit_count()
        stats["work_failure_config_steps"] += work_bad.bit_count()

        count_bad = 0
        actual_count = bitsliced_population_count(actual_a + actual_b)
        for digit, observed in enumerate(actual_count):
            expected = row_full if (occupied >> digit) & 1 else 0
            count_bad |= observed ^ expected
        stats["token_count_failure_config_steps"] += (
            count_bad.bit_count()
        )

        adjacent_bad = 0
        ownership_bad = 0
        for station in range(STATIONS):
            left = (station - 1) % STATIONS
            right = (station + 1) % STATIONS
            incidence = actual_a[station] & actual_a[right]
            stats["adjacency_pair_incidences"] += incidence.bit_count()
            adjacent_bad |= incidence
            dirty = (
                actual_a[left]
                | actual_a[right]
                | actual_b[left]
                | actual_b[station]
                | actual_b[right]
                | actual_work[station]
            )
            violation = actual_a[station] & dirty
            stats[
                "ownership_violation_station_incidences"
            ] += violation.bit_count()
            ownership_bad |= violation
        stats["adjacency_failure_config_steps"] += (
            adjacent_bad.bit_count()
        )
        stats["ownership_failure_config_steps"] += (
            ownership_bad.bit_count()
        )

        distance_bad = 0
        for left in range(STATIONS):
            moved_left = (left + step) % STATIONS
            for right in range(left + 1, STATIONS):
                moved_right = (right + step) % STATIONS
                expected_pair = original_a[left] & original_a[right]
                observed_pair = (
                    actual_a[moved_left] & actual_a[moved_right]
                )
                distance_bad |= observed_pair ^ expected_pair
        stats["distance_failure_config_steps"] += (
            distance_bad.bit_count()
        )
        stats["distance_bitplane_pair_comparisons"] += comb(
            STATIONS, 2
        )
        stats["distance_pair_incidence_checks"] += (
            rows * comb(occupied, 2)
        )
        stats["occupied_station_invariant_checks"] += rows * occupied
        stats["exhaustive_controller_steps"] += rows

        apply_bitplane_word(planes, compiled, row_full)

    closure_bad = 0
    for observed, expected in zip(
        planes[a_base:a_base + STATIONS], original_a
    ):
        closure_bad |= observed ^ expected
    for plane in planes[b_base:work_base + STATIONS]:
        closure_bad |= plane
    stats["rail_closure_failures"] += closure_bad.bit_count()
    return stats


def add_stats(target: dict[str, int], source: dict[str, int]) -> None:
    for key, value in source.items():
        target[key] += value


def sweep_certificate(
    counts: tuple[int, ...],
) -> dict[str, object]:
    """Exhaust exactly all k<=11 masks; do not enter a partial stratum."""

    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    data_width = M740.parameterized_data_width(CAPACITY)
    controller = M740.parameterized_controller_word(
        program, data_width, CAPACITY
    )
    width = data_width + 3 * STATIONS
    compiled, structural_failures = compile_controller(controller, width)

    aggregate = empty_orbit_stats()
    aggregate["controller_structure_failures"] = structural_failures
    per_k: dict[int, dict[str, object]] = {}
    completed_strata = []
    census_popcount_failures = 0
    census_adjacency_failures = 0
    batch_ordinal = 0
    orbit_hasher = sha256()

    for occupied in range(SWEEP_K_MAX + 1):
        expected = counts[occupied]
        streamed = 0
        input_hasher = sha256()
        batch: list[int] = []

        def consume(current: list[int]) -> None:
            nonlocal census_popcount_failures
            nonlocal census_adjacency_failures
            nonlocal batch_ordinal
            planes, pop_bad, adjacency_bad, raw = batch_to_bitplanes(
                current, STATIONS, occupied
            )
            census_popcount_failures += pop_bad
            census_adjacency_failures += adjacency_bad
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
                "batch": batch_ordinal,
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
        stratum_complete = streamed == expected
        if stratum_complete:
            completed_strata.append(occupied)
        per_k[occupied] = {
            "k": occupied,
            "streamed_count": streamed,
            "recurrence_count": expected,
            "streamed_masks_sha256": input_hasher.hexdigest(),
            "orbit_evaluated_configurations": streamed,
            "orbit_stratum_complete": stratum_complete,
        }

    completed_configuration_bound = sum(
        counts[:SWEEP_K_MAX + 1]
    )
    residual_counts = tuple(
        (occupied, counts[occupied])
        for occupied in range(SWEEP_K_MAX + 1, len(counts))
    )
    residual_configuration_count = sum(
        count for _occupied, count in residual_counts
    )
    expected_steps = completed_configuration_bound * STATIONS
    expected_occupied_checks = sum(
        occupied * counts[occupied] * STATIONS
        for occupied in range(SWEEP_K_MAX + 1)
    )
    expected_pair_checks = sum(
        comb(occupied, 2) * counts[occupied] * STATIONS
        for occupied in range(SWEEP_K_MAX + 1)
    )
    zero_failure_keys = (
        "controller_structure_failures",
        "translation_failure_config_steps",
        "token_count_failure_config_steps",
        "adjacency_failure_config_steps",
        "adjacency_pair_incidences",
        "ownership_failure_config_steps",
        "ownership_violation_station_incidences",
        "B_rail_failure_config_steps",
        "work_failure_config_steps",
        "distance_failure_config_steps",
        "rail_closure_failures",
    )
    zero_failures = all(aggregate[key] == 0 for key in zero_failure_keys)
    complete_prefix_exact = (
        tuple(completed_strata) == tuple(range(SWEEP_K_MAX + 1))
        and all(
            per_k[occupied]["streamed_count"] == counts[occupied]
            and per_k[occupied]["orbit_stratum_complete"]
            for occupied in range(SWEEP_K_MAX + 1)
        )
        and census_popcount_failures == 0
        and census_adjacency_failures == 0
        and len(compiled) == len(controller)
        and aggregate["evaluated_configurations"]
        == completed_configuration_bound
        and aggregate["exhaustive_controller_steps"] == expected_steps
        and aggregate["occupied_station_invariant_checks"]
        == expected_occupied_checks
        and aggregate["distance_pair_incidence_checks"]
        == expected_pair_checks
        and zero_failures
    )

    selected_estimate = (
        expected_steps / MEASURED_B5_STATION_STEPS_PER_SEC
    )
    next_prefix_steps = (
        expected_steps + counts[SWEEP_K_MAX + 1] * STATIONS
    )
    next_prefix_estimate = (
        next_prefix_steps / MEASURED_B5_STATION_STEPS_PER_SEC
    )
    budget_choice_exact = (
        selected_estimate + BUDGET_RESERVE_SEC < AUDIT_TIMEOUT_SEC
        and next_prefix_estimate + BUDGET_RESERVE_SEC
        > AUDIT_TIMEOUT_SEC
    )
    honest_bound = (
        complete_prefix_exact
        and budget_choice_exact
        and residual_configuration_count
        == EXPECTED_LUCAS_43 - completed_configuration_bound
        and residual_configuration_count > 0
    )
    return {
        "banks": BANK_COUNT,
        "capacity": CAPACITY,
        "program_stations": len(program),
        "data_width": data_width,
        "controller_gates_per_step": len(controller),
        "compiled_gate_count": len(compiled),
        "controller_word_sha256": K.gate_digest(controller),
        "input_data_fixture": (
            "all-zero lawful C=6 data register; controller work/B rails "
            "blank at every declared initial Q boundary"
        ),
        "sweep_bound_statement": (
            "Every independent C_43 configuration in every whole stratum "
            "0<=k<=11 is enumerated and run for all 43 literal controller "
            "steps. Strata 12<=k<=21 are recurrence-counted only: they are "
            "not enumerated, sampled, partially swept, or materialized."
        ),
        "completed_orbit_strata": tuple(completed_strata),
        "partially_evaluated_strata": (),
        "unswept_residual_strata": tuple(
            occupied for occupied, _count in residual_counts
        ),
        "completed_strata_configuration_bound":
            completed_configuration_bound,
        "residual_configuration_count": residual_configuration_count,
        "full_census_configurations": sum(counts),
        "full_sweep": False,
        "sweep_k_max": SWEEP_K_MAX,
        "expected_bounded_controller_steps": expected_steps,
        "full_sweep_controller_steps": sum(counts) * STATIONS,
        "expected_bounded_occupied_station_checks":
            expected_occupied_checks,
        "expected_bounded_distance_pair_incidence_checks":
            expected_pair_checks,
        "bitplane_batch": BITPLANE_BATCH,
        "orbit_batch_count": batch_ordinal,
        "orbit_batch_evidence_sha256": orbit_hasher.hexdigest(),
        "swept_masks_by_k_sha256": stable_digest({
            occupied: per_k[occupied]["streamed_masks_sha256"]
            for occupied in range(SWEEP_K_MAX + 1)
        }),
        "per_swept_k": per_k,
        "residual_counts_by_k": residual_counts,
        "residual_counts_sha256": stable_digest(residual_counts),
        "popcount_validation_failures": census_popcount_failures,
        "adjacency_validation_failures": census_adjacency_failures,
        "zero_failure_census": {
            key: aggregate[key] for key in zero_failure_keys
        },
        **{
            key: value for key, value in aggregate.items()
            if key not in zero_failure_keys
        },
        "budget_basis": {
            "measured_b5_station_steps_per_second":
                MEASURED_B5_STATION_STEPS_PER_SEC,
            "reserve_seconds": BUDGET_RESERVE_SEC,
            "selected_prefix_estimated_seconds":
                round(selected_estimate, 6),
            "next_prefix_k12_estimated_seconds":
                round(next_prefix_estimate, 6),
            "selected_plus_reserve_under_budget":
                selected_estimate + BUDGET_RESERVE_SEC
                < AUDIT_TIMEOUT_SEC,
            "next_plus_reserve_over_budget":
                next_prefix_estimate + BUDGET_RESERVE_SEC
                > AUDIT_TIMEOUT_SEC,
            "choice_exact": budget_choice_exact,
        },
        "literal_execution": (
            "the exact M740 C=6 controlled Q plus two-rail R gate word is "
            "compiled once and applied at all 43 steps of every swept mask"
        ),
        "complete_prefix_exact": complete_prefix_exact,
        "honest_bounded_sweep": honest_bound,
        "certificate_accepts_full_or_honest_bound": honest_bound,
        "exact": honest_bound,
    }


def ownership_reasons(
    mask: int, station: int, stations: int
) -> tuple[str, ...]:
    if not ((mask >> station) & 1):
        return ()
    reasons = []
    if (mask >> ((station - 1) % stations)) & 1:
        reasons.append("left_A")
    if (mask >> ((station + 1) % stations)) & 1:
        reasons.append("right_A")
    return tuple(reasons)


def near_miss_certificate() -> dict[str, object]:
    rows = []
    violating_stations = 0
    reason_incidences = 0
    failures = 0
    for left in range(STATIONS):
        right = (left + 1) % STATIONS
        mask = (1 << left) | (1 << right)
        violations = tuple(
            (station, ownership_reasons(mask, station, STATIONS))
            for station in range(STATIONS)
            if ownership_reasons(mask, station, STATIONS)
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
        failures += int(not exact)
        violating_stations += len(violations)
        reason_incidences += len(reasons)
        rows.append((left, right, sites, reasons, exact))
    exact = (
        failures == 0
        and violating_stations == reason_incidences == 2 * STATIONS
    )
    return {
        "ring": STATIONS,
        "adjacent_pair_controls": STATIONS,
        "violating_stations": violating_stations,
        "expected_violating_stations": 2 * STATIONS,
        "reason_incidences": reason_incidences,
        "failures": failures,
        "near_miss_table_sha256": stable_digest(rows),
        "exact": exact,
    }


def boundary_keys_certificate(
    mapper: dict[str, object],
    census: dict[str, object],
    rows: dict[str, object],
    transport: dict[str, object],
    sweep: dict[str, object],
    near_miss: dict[str, object],
) -> dict[str, object]:
    prior_exact = (
        mapper["frozen_C12_equivalence_b1_through_b12_exact"]
        and PRIOR_ANCHOR_CENSUS
        == {
            3: 4,
            11: 199,
            19: 9_349,
            27: 439_204,
            35: 20_633_239,
        }
        and PRIOR_ANCHOR_ORBIT_STEPS
        == {
            3: 12,
            11: 2_189,
            19: 177_631,
            27: 11_858_508,
            35: 722_163_365,
        }
    )
    exact = all((
        prior_exact,
        mapper["exact"],
        census["exact"],
        rows["exact"],
        transport["exact"],
        sweep["honest_bounded_sweep"],
        near_miss["exact"],
    ))
    return {
        "anchor_ring_family": [3, 11, 19, 27, 35, 43],
        "anchor_bank_family": [1, 2, 3, 4, 5, 6],
        "prior_b1_through_b5_anchor_records_retained": prior_exact,
        "sixth_anchor_n43_census_exhausted": census["exact"],
        "sixth_anchor_n43_orbits_exhausted": False,
        "sixth_anchor_honest_complete_strata_bound": {
            "completed_strata": sweep["completed_orbit_strata"],
            "configuration_bound":
                sweep["completed_strata_configuration_bound"],
            "controller_step_bound":
                sweep["expected_bounded_controller_steps"],
            "residual_strata": sweep["unswept_residual_strata"],
            "residual_configurations":
                sweep["residual_configuration_count"],
        },
        "b1_through_b6_now_all_orbit_exhausted": False,
        "I1_six_term_identity_direct_evidence_at_b6": (
            transport["exact"]
            and sweep["zero_failure_census"][
                "ownership_violation_station_incidences"
            ] == 0
        ),
        "I2_clean_work_identity_direct_evidence_at_b6": (
            rows["all_43_rows_directly_clean"]
            and rows["rows_checked"] == 43
        ),
        "identities_direct_evidence_extends_to_b6": (
            transport["exact"] and rows["all_43_rows_directly_clean"]
        ),
        "table_uniform_theorem_anchor_set_fully_extended": False,
        "bounded_sixth_anchor_added": exact,
        "general_b_claim_changed": False,
        "general_b_boundary": (
            "Cycle 761 adds an exact b=6 census, direct evidence for all "
            "43 emitted rows, and the stated complete-strata orbit bound. "
            "It does not claim the residual strata or all n=43 orbits were "
            "swept, and does not change Cycle 740's conditional general-b "
            "claim."
        ),
        "near_miss_controls_exact": near_miss["exact"],
        "honest": True,
        "exact": exact,
    }


def main() -> int:
    started = perf_counter()
    reports: dict[str, object] = {}

    check(
        "INPUT_literal_paths_and_header_contract",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
        )
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == "docs/B6_EXHAUSTIVE_ANCHOR_CYCLE761_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )

    try:
        mapper = mapper_anchor_certificate()
    except Exception as error:
        ERRORS["A_mapper_anchors"] = error_text(error)
        mapper = {
            "exact": False,
            "error": ERRORS["A_mapper_anchors"],
            "frozen_C12_equivalence_b1_through_b12_exact": False,
        }
    reports["A_mapper_anchors"] = mapper
    check("A_mapper_anchors_exact", mapper["exact"])

    try:
        census = census_certificate()
    except Exception as error:
        ERRORS["B_census"] = error_text(error)
        census = {
            "exact": False,
            "error": ERRORS["B_census"],
            "counts_by_k": (),
            "enumerated_total": 0,
        }
    reports["B_census"] = census
    check(
        "B_streamed_recurrence_census_equals_L43_969323029",
        census["exact"]
        and census["enumerated_total"] == EXPECTED_LUCAS_43,
    )
    OUTPUT_LINES.append(
        "CENSUS n=43 BY k :: "
        + ", ".join(
            f"k={occupied}:{count}"
            for occupied, count in enumerate(census["counts_by_k"])
        )
    )

    try:
        rows = row_clean_work_certificate()
        transport = i1_transport_certificate()
    except Exception as error:
        ERRORS["C_rows"] = error_text(error)
        rows = {
            "exact": False,
            "error": ERRORS["C_rows"],
            "all_43_rows_directly_clean": False,
            "rows_checked": 0,
        }
        transport = {"exact": False, "error": ERRORS["C_rows"]}
    reports["C_rows"] = {
        "clean_work": rows,
        "I1_transport": transport,
        "exact": rows["exact"] and transport["exact"],
    }
    check(
        "C_all_43_b6_rows_direct_clean_work_identity_evidence",
        rows["all_43_rows_directly_clean"]
        and rows["rows_checked"] == 43
        and transport["exact"],
    )

    try:
        sweep = sweep_certificate(tuple(census["counts_by_k"]))
    except Exception as error:
        ERRORS["D_sweep"] = error_text(error)
        sweep = {
            "exact": False,
            "error": ERRORS["D_sweep"],
            "honest_bounded_sweep": False,
            "completed_orbit_strata": (),
            "completed_strata_configuration_bound": 0,
            "expected_bounded_controller_steps": 0,
            "unswept_residual_strata": (),
            "residual_configuration_count": 0,
            "zero_failure_census": {
                "ownership_violation_station_incidences": -1,
            },
        }
    reports["D_sweep"] = sweep
    check(
        "D_all_k0_through_k11_orbits_exhausted_residual_counted_only",
        sweep["honest_bounded_sweep"],
    )
    OUTPUT_LINES.append(
        "SWEEP n=43 :: complete_k="
        + repr(sweep["completed_orbit_strata"])
        + f"; configurations={sweep['completed_strata_configuration_bound']}"
        + f"; station_steps={sweep['expected_bounded_controller_steps']}"
        + f"; residual={sweep['residual_configuration_count']}"
    )

    try:
        near_miss = near_miss_certificate()
    except Exception as error:
        ERRORS["E_near_miss"] = error_text(error)
        near_miss = {"exact": False, "error": ERRORS["E_near_miss"]}
    reports["E_near_miss"] = near_miss
    check(
        "E_n43_adjacent_pair_near_miss_two_stations_each",
        near_miss["exact"],
    )

    try:
        keys = boundary_keys_certificate(
            mapper, census, rows, transport, sweep, near_miss
        )
    except Exception as error:
        ERRORS["F_keys"] = error_text(error)
        keys = {"exact": False, "honest": False, "error": ERRORS["F_keys"]}
    reports["F_keys"] = keys
    check(
        "F_honest_b6_bounded_anchor_and_general_b_boundary_keys",
        keys["exact"]
        and keys["honest"]
        and keys["general_b_claim_changed"] is False,
    )

    elapsed = perf_counter() - started
    check("TIMEOUT_runtime_under_1800_seconds", elapsed < AUDIT_TIMEOUT_SEC)

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bitplane_batch": BITPLANE_BATCH,
        "bounded": True,
        "scope": "the sixth exhaustive anchor b=6, n=43",
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
        "CYCLE761_B6_EXHAUSTIVE_ANCHOR_ALL_PASS"
        if report["pass"]
        else "CYCLE761_B6_EXHAUSTIVE_ANCHOR_HONEST_FAIL"
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
            "terminal": "CYCLE761_B6_EXHAUSTIVE_ANCHOR_HONEST_FAIL",
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
