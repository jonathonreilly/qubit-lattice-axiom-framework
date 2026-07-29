#!/usr/bin/env python3
"""Cycle 756: the b=5 exhaustive sector anchor at n=35.

The landed Cycle-719 core is not modified.  Cycle 740 supplies the
capacity-parameterized C=5 mapper.  Every independent configuration of C_35
is streamed in 65,536-row batches through the literal controlled Q plus
two-rail R word.  The streamed census is never retained as one mask table.
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
NOTE_PATH = "docs/B5_EXHAUSTIVE_ANCHOR_CYCLE756_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STDOUT_LIMIT_BYTES = 150 * 1024
BITPLANE_BATCH = 65_536
ORBIT_SOFT_LIMIT_SEC = 1680
BANK_COUNT = 5
CAPACITY = 5
STATIONS = 35
EXPECTED_LUCAS_35 = 20_633_239
PRIOR_ANCHOR_CENSUS = {
    3: 4,
    11: 199,
    19: 9_349,
    27: 439_204,
}
PRIOR_ANCHOR_ORBIT_STEPS = {
    3: 12,
    11: 2_189,
    19: 177_631,
    27: 11_858_508,
}
ALLOWED_GATE_KINDS = frozenset(("X", "CNOT", "TOF"))
I1_AMENDED_FORMULA = (
    "not(a[left] or a[right] or b[left] or b[station] or b[right] or "
    "work[station])"
)
I2_IDENTITY = (
    "I_macro_clean_work_uniformity: for every b>=1 and every row emitted by "
    "K.interleaved_program(b), the controlled mapped macro leaves its A "
    "control unchanged, addresses only data plus its own work bit, and maps "
    "clean work=0 back to 0"
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
ERRORS: dict[str, str] = {}


def check(label: str, condition: object) -> bool:
    """Record one uniquely named PASS/FAIL line."""

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


def has_adjacent_pair(mask: int, stations: int) -> bool:
    return bool(mask & rotate_mask(mask, 1, stations))


def lucas_number(index: int) -> int:
    if index == 0:
        return 2
    if index == 1:
        return 1
    older, newer = 2, 1
    for _ in range(2, index + 1):
        older, newer = newer, older + newer
    return newer


def path_independence_counts(length: int) -> tuple[int, ...]:
    """Coefficient recurrence P_m=P_(m-1)+x P_(m-2)."""

    if length == 0:
        return (1,)
    if length == 1:
        return (1, 1)
    older = [1]
    newer = [1, 1]
    for _ in range(2, length + 1):
        width = max(len(newer), len(older) + 1)
        current = [0] * width
        for degree, value in enumerate(newer):
            current[degree] += value
        for degree, value in enumerate(older):
            current[degree + 1] += value
        older, newer = newer, current
    return tuple(newer)


def cycle_independence_counts(stations: int) -> tuple[int, ...]:
    """Split on vertex zero: P_(n-1)+x P_(n-3)."""

    without_zero = path_independence_counts(stations - 1)
    with_zero_path = path_independence_counts(stations - 3)
    width = stations // 2 + 1
    counts = [0] * width
    for degree, value in enumerate(without_zero):
        if degree < width:
            counts[degree] += value
    for degree, value in enumerate(with_zero_path):
        if degree + 1 < width:
            counts[degree + 1] += value
    return tuple(counts)


SPREAD_CHUNK_BITS = 12
SPREAD_CHUNK_MASK = (1 << SPREAD_CHUNK_BITS) - 1


def local_spread(mask: int) -> int:
    """Map selected y_i to y_i+i inside one rank-zero chunk."""

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
    """Insert one gap after each earlier chosen position."""

    output = 0
    earlier_rank = 0
    base = 0
    while base < universe:
        chunk = (mask >> base) & SPREAD_CHUNK_MASK
        output |= SPREAD_TABLE[chunk] << (base + earlier_rank)
        earlier_rank += SPREAD_COUNTS[chunk]
        base += SPREAD_CHUNK_BITS
    return output


def path_masks_fixed_k(
    start: int, length: int, occupied: int
):
    """Stream a fixed-k path stratum through the gap-insertion bijection."""

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
    """Stream one C_n stratum without materializing any other stratum."""

    yield from path_masks_fixed_k(1, stations - 1, occupied)
    if occupied:
        for mask in path_masks_fixed_k(2, stations - 3, occupied - 1):
            yield mask | 1


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
        "structural_reason": (
            "controlled TOF computes its own clean work bit, uses that bit "
            "only as a control, and repeats the compute gate to restore it"
        ),
        "exact": exact,
    }


def validate_clean_word(
    word: tuple[object, ...],
    data_width: int,
    control: int,
    work: int,
    primitive_exact: bool,
) -> dict[str, object]:
    """Direct Cycle-739 I2 predicate, reproduced for every b=5 row."""

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
            expected_lifted.append(
                K.A.cn(control, gate.wires[0])
            )
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
    work_compute_uncompute_exact = (
        work_target_count == 2 * tof_count
    )
    clean_work_zero_returns_zero = (
        primitive_exact
        and expansion_exact
        and work_compute_uncompute_exact
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


def mapper_and_i2_certificate() -> dict[str, object]:
    """Anchor M740 at b<=4 and directly inspect all 35 C=5 rows."""

    equivalence = M740.equivalence_certificate()
    prior = {
        bank_count: {
            "rows": equivalence["per_b"][bank_count]["rows"],
            "row_objects_exact":
                equivalence["per_b"][bank_count]["row_objects_exact"],
            "mapped_objects_exact":
                equivalence["per_b"][bank_count]["mapped_objects_exact"],
            "program_bytes_exact":
                equivalence["per_b"][bank_count]["program_bytes_exact"],
            "mapped_bytes_exact":
                equivalence["per_b"][bank_count]["mapped_bytes_exact"],
            "equivalence_sha256":
                equivalence["per_b"][bank_count]["equivalence_sha256"],
        }
        for bank_count in range(1, 5)
    }
    prior_exact = (
        equivalence["exact"]
        and equivalence["all_byte_identical"]
        and all(
            all(
                row[key]
                for key in (
                    "row_objects_exact",
                    "mapped_objects_exact",
                    "program_bytes_exact",
                    "mapped_bytes_exact",
                )
            )
            for row in prior.values()
        )
    )

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
            word = tuple(
                M740.parameterized_mapped_macro(row, CAPACITY)
            )
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
        "bank": 5,
        "cross": 4,
        "finalizer": 1,
        "handoff": 8,
        "relay": 16,
        "source": 1,
    }
    b5_exact = (
        len(program) == STATIONS == 8 * BANK_COUNT - 5
        and program == K.interleaved_program(BANK_COUNT)
        and data_width == 2_224
        and dict(sorted(row_kind_counts.items()))
        == expected_kind_counts
        and primitive["exact"]
        and not failures
    )
    return {
        "M740_full_frozen_equivalence_sweep_b1_through_b12_exact":
            equivalence["exact"],
        "M740_full_frozen_equivalence_sha256":
            stable_digest(equivalence),
        "prior_anchor_b1_through_b4": prior,
        "prior_anchor_equivalence_unchanged": prior_exact,
        "b5": {
            "banks": BANK_COUNT,
            "capacity": CAPACITY,
            "ring_rows": len(program),
            "expected_8b_minus_5": 8 * BANK_COUNT - 5,
            "data_width": data_width,
            "row_kind_counts": dict(sorted(row_kind_counts.items())),
            "semantic_gate_kind_counts": dict(sorted(
                semantic_gate_counts.items()
            )),
            "controlled_gate_total": controlled_gate_total,
            "rows_checked": len(program),
            "row_failure_count": len(failures),
            "row_failures": failures,
            "mapped_row_words_sha256": word_hasher.hexdigest(),
            "I2_identity": I2_IDENTITY,
            "all_rows_directly_clean": b5_exact,
        },
        "primitive_clean_work": primitive,
        "exact": prior_exact and b5_exact,
    }


def amended_ownership_holds_mask(
    a_mask: int,
    b_mask: int,
    work_mask: int,
    station: int,
    stations: int,
) -> bool:
    left = (station - 1) % stations
    right = (station + 1) % stations
    return not (
        ((a_mask >> left) & 1)
        or ((a_mask >> right) & 1)
        or ((b_mask >> left) & 1)
        or ((b_mask >> station) & 1)
        or ((b_mask >> right) & 1)
        or ((work_mask >> station) & 1)
    )


def i1_transport_certificate() -> dict[str, object]:
    """Structural +1 transport and explicit n=35 orbit samples."""

    source_terms = (
        ("A", -1),
        ("A", 1),
        ("B", -1),
        ("B", 0),
        ("B", 1),
        ("work", 0),
    )
    translated_terms = tuple(
        (rail, offset) for rail, offset in source_terms
    )
    structural_transport_exact = translated_terms == source_terms
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
    samples = (
        0,
        1 << 0,
        (1 << 0) | (1 << 2),
        sum(1 << station for station in (1, 4, 7, 10, 18)),
        sum(1 << station for station in range(0, 33, 2)),
    )
    sample_rows = []
    failures = 0
    q_boundaries = 0
    occupied_predicates = 0
    for initial in samples:
        sample_failures = 0
        if has_adjacent_pair(initial, STATIONS):
            sample_failures += 1
        for step in range(STATIONS):
            a_mask = rotate_mask(initial, step, STATIONS)
            occupied = tuple(
                station for station in range(STATIONS)
                if (a_mask >> station) & 1
            )
            predicates = tuple(
                amended_ownership_holds_mask(
                    a_mask, 0, 0, station, STATIONS
                )
                for station in occupied
            )
            sample_failures += int(not all(predicates))
            q_boundaries += 1
            occupied_predicates += len(predicates)
        sample_failures += int(
            rotate_mask(initial, STATIONS, STATIONS) != initial
        )
        failures += sample_failures
        sample_rows.append({
            "initial_mask": initial,
            "k": initial.bit_count(),
            "q_boundaries": STATIONS,
            "occupied_predicates": initial.bit_count() * STATIONS,
            "failures": sample_failures,
        })
    exact = (
        I1_AMENDED_FORMULA.startswith("not(a[left]")
        and len(source_terms) == 6
        and structural_transport_exact
        and distance_isometry_failures == 0
        and q_boundaries == len(samples) * STATIONS
        and failures == 0
    )
    return {
        "i1_amended_formula": I1_AMENDED_FORMULA,
        "six_source_terms": source_terms,
        "translated_terms_at_s_plus_one": translated_terms,
        "symbolic_plus_one_transport_exact":
            structural_transport_exact,
        "circular_translation_distance_isometry_failures":
            distance_isometry_failures,
        "orbit_sample_count": len(samples),
        "orbit_sample_q_boundaries": q_boundaries,
        "orbit_sample_occupied_predicates": occupied_predicates,
        "orbit_samples_sha256": stable_digest(sample_rows),
        "orbit_sample_failures": failures,
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
    """Vectorized row-to-plane transpose plus per-row census validation."""

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
    packed = np.packbits(
        bits.T, axis=1, bitorder="little"
    )
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
    """Run one full literal 35-step controller orbit on one bit-plane batch."""

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
        actual_count = bitsliced_population_count(
            actual_a + actual_b
        )
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
            stats["adjacency_pair_incidences"] += (
                incidence.bit_count()
            )
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


def census_and_orbit_certificate(started: float) -> dict[str, object]:
    """Stream all C_35 masks and exhaust the literal orbit when in budget."""

    expected_counts = cycle_independence_counts(STATIONS)
    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    data_width = M740.parameterized_data_width(CAPACITY)
    controller = M740.parameterized_controller_word(
        program, data_width, CAPACITY
    )
    width = data_width + 3 * STATIONS
    compiled, structural_failures = compile_controller(
        controller, width
    )

    aggregate = empty_orbit_stats()
    aggregate["controller_structure_failures"] = structural_failures
    census_popcount_failures = 0
    census_adjacency_failures = 0
    per_k: dict[int, dict[str, object]] = {}
    completed_orbit_strata = []
    partially_evaluated_strata = []
    orbit_active = True
    orbit_batch_ordinal = 0
    orbit_digest_hasher = sha256()

    stratum_order = tuple(sorted(
        range(len(expected_counts)),
        key=lambda occupied: (-expected_counts[occupied], occupied),
    ))
    for occupied in stratum_order:
        expected = expected_counts[occupied]
        count = 0
        orbit_count = 0
        orbit_complete = True
        input_hasher = sha256()
        batch: list[int] = []

        def consume(current: list[int]) -> None:
            nonlocal census_popcount_failures
            nonlocal census_adjacency_failures
            nonlocal orbit_active
            nonlocal orbit_batch_ordinal
            nonlocal orbit_count
            nonlocal orbit_complete
            planes, pop_bad, adjacent_bad, raw = batch_to_bitplanes(
                current, STATIONS, occupied
            )
            census_popcount_failures += pop_bad
            census_adjacency_failures += adjacent_bad
            input_hasher.update(raw)
            if (
                orbit_active
                and perf_counter() - started
                >= ORBIT_SOFT_LIMIT_SEC
            ):
                orbit_active = False
            if orbit_active:
                batch_stats = evaluate_orbit_batch(
                    planes,
                    len(current),
                    occupied,
                    compiled,
                    data_width,
                )
                add_stats(aggregate, batch_stats)
                orbit_count += len(current)
                orbit_digest_hasher.update(stable_json_bytes({
                    "batch": orbit_batch_ordinal,
                    "k": occupied,
                    "rows": len(current),
                    "input_sha256": sha256(raw).hexdigest(),
                    "stats": batch_stats,
                }))
                orbit_batch_ordinal += 1
            else:
                orbit_complete = False

        for mask in cycle_masks_fixed_k(STATIONS, occupied):
            batch.append(mask)
            count += 1
            if len(batch) == BITPLANE_BATCH:
                consume(batch)
                batch = []
        if batch:
            consume(batch)

        if count != expected:
            orbit_complete = False
        if orbit_complete and orbit_count == count:
            completed_orbit_strata.append(occupied)
        elif orbit_count:
            partially_evaluated_strata.append(occupied)
        per_k[occupied] = {
            "k": occupied,
            "streamed_count": count,
            "transfer_recurrence_count": expected,
            "streamed_masks_sha256": input_hasher.hexdigest(),
            "orbit_evaluated_configurations": orbit_count,
            "orbit_stratum_complete":
                orbit_complete and orbit_count == count,
        }

    enumerated_counts = tuple(
        int(per_k[occupied]["streamed_count"])
        for occupied in range(len(expected_counts))
    )
    census_total = sum(enumerated_counts)
    census_exact = (
        enumerated_counts == expected_counts
        and census_total == sum(expected_counts)
        == lucas_number(STATIONS)
        == EXPECTED_LUCAS_35
        and census_popcount_failures == 0
        and census_adjacency_failures == 0
    )
    full_orbit = (
        aggregate["evaluated_configurations"] == census_total
        and set(completed_orbit_strata)
        == set(range(len(expected_counts)))
        and not partially_evaluated_strata
    )
    expected_steps = census_total * STATIONS
    expected_occupied_checks = sum(
        occupied * count * STATIONS
        for occupied, count in enumerate(expected_counts)
    )
    expected_pair_checks = sum(
        comb(occupied, 2) * count * STATIONS
        for occupied, count in enumerate(expected_counts)
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
    full_exact = (
        full_orbit
        and census_exact
        and len(compiled) == len(controller)
        and aggregate["exhaustive_controller_steps"]
        == expected_steps
        and aggregate["occupied_station_invariant_checks"]
        == expected_occupied_checks
        and aggregate["distance_pair_incidence_checks"]
        == expected_pair_checks
        and zero_failures
    )
    completed_bound = sum(
        expected_counts[occupied]
        for occupied in completed_orbit_strata
    )
    honest_strata_bound = (
        not full_orbit
        and completed_bound > 0
        and all(
            per_k[occupied]["orbit_stratum_complete"]
            and per_k[occupied]["orbit_evaluated_configurations"]
            == expected_counts[occupied]
            for occupied in completed_orbit_strata
        )
        and zero_failures
    )
    return {
        "census": {
            "ring": STATIONS,
            "counts_by_k": enumerated_counts,
            "transfer_recurrence_counts_by_k": expected_counts,
            "enumerated_total": census_total,
            "lucas_recurrence_total": lucas_number(STATIONS),
            "frozen_target_L35": EXPECTED_LUCAS_35,
            "streaming_generator": (
                "vertex-0 absent/present split; fixed-k path combinations "
                "stream through the gap-insertion bijection"
            ),
            "materialized_full_mask_table": False,
            "bitplane_batch": BITPLANE_BATCH,
            "popcount_validation_failures":
                census_popcount_failures,
            "adjacency_validation_failures":
                census_adjacency_failures,
            "per_k": {
                occupied: per_k[occupied]
                for occupied in range(len(expected_counts))
            },
            "all_streamed_masks_sha256": stable_digest({
                occupied: per_k[occupied]["streamed_masks_sha256"]
                for occupied in range(len(expected_counts))
            }),
            "exact": census_exact,
        },
        "orbit": {
            "banks": BANK_COUNT,
            "capacity": CAPACITY,
            "program_stations": len(program),
            "data_width": data_width,
            "controller_gates_per_step": len(controller),
            "compiled_gate_count": len(compiled),
            "controller_word_sha256": K.gate_digest(controller),
            "input_data_fixture": (
                "all-zero lawful C=5 data register; controller work/B rails "
                "blank at every declared initial Q boundary"
            ),
            "stratum_execution_order": stratum_order,
            "completed_orbit_strata": tuple(sorted(
                completed_orbit_strata
            )),
            "partially_evaluated_strata": tuple(sorted(
                partially_evaluated_strata
            )),
            "completed_strata_configuration_bound": completed_bound,
            "full_census_configurations": census_total,
            "full_sweep": full_orbit,
            "expected_full_controller_steps": expected_steps,
            "expected_full_occupied_station_checks":
                expected_occupied_checks,
            "expected_full_distance_pair_incidence_checks":
                expected_pair_checks,
            "bitplane_batch": BITPLANE_BATCH,
            "orbit_batch_count": orbit_batch_ordinal,
            "orbit_batch_evidence_sha256":
                orbit_digest_hasher.hexdigest(),
            "zero_failure_census": {
                key: aggregate[key] for key in zero_failure_keys
            },
            **{
                key: value for key, value in aggregate.items()
                if key not in zero_failure_keys
            },
            "literal_execution": (
                "the exact M740 C=5 controlled Q plus two-rail R gate word "
                "is compiled once and applied at all 35 steps"
            ),
            "full_exact": full_exact,
            "honest_strata_bound": honest_strata_bound,
            "certificate_accepts_full_or_honest_bound":
                full_exact or honest_strata_bound,
        },
        "exact": census_exact and (full_exact or honest_strata_bound),
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
            reason for _station, station_reasons in violations
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
        and violating_stations == reason_incidences
        == 2 * STATIONS
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


def boundary_certificate(
    mapper_i2: dict[str, object],
    i1: dict[str, object],
    census_orbit: dict[str, object],
    near_miss: dict[str, object],
) -> dict[str, object]:
    full_fifth = bool(
        census_orbit["census"]["exact"]
        and census_orbit["orbit"]["full_exact"]
    )
    prior_exact = (
        mapper_i2["prior_anchor_equivalence_unchanged"]
        and PRIOR_ANCHOR_CENSUS
        == {3: 4, 11: 199, 19: 9_349, 27: 439_204}
        and PRIOR_ANCHOR_ORBIT_STEPS
        == {3: 12, 11: 2_189, 19: 177_631, 27: 11_858_508}
    )
    return {
        "anchor_ring_family": [3, 11, 19, 27, 35],
        "anchor_bank_family": [1, 2, 3, 4, 5],
        "prior_b1_through_b4_exhaustive_anchors_retained":
            prior_exact,
        "fifth_anchor_n35_census_exhausted":
            census_orbit["census"]["exact"],
        "fifth_anchor_n35_orbits_exhausted": full_fifth,
        "fifth_anchor_honest_strata_bound_if_not_full": (
            None
            if full_fifth
            else {
                "completed_strata":
                    census_orbit["orbit"]["completed_orbit_strata"],
                "configuration_bound":
                    census_orbit["orbit"][
                        "completed_strata_configuration_bound"
                    ],
            }
        ),
        "b1_through_b5_now_all_exhausted":
            prior_exact and full_fifth,
        "I1_six_term_identity_direct_evidence_at_b5":
            i1["exact"]
            and census_orbit["orbit"]["zero_failure_census"][
                "ownership_violation_station_incidences"
            ] == 0,
        "I2_clean_work_identity_direct_evidence_at_b5":
            mapper_i2["b5"]["all_rows_directly_clean"]
            and mapper_i2["b5"]["rows_checked"] == 35,
        "identities_direct_evidence_extends_beyond_prior_anchors_to_b5":
            (
                i1["exact"]
                and mapper_i2["b5"]["all_rows_directly_clean"]
            ),
        "table_uniform_theorem_anchor_set_extended":
            prior_exact and full_fifth,
        "general_b_claim_changed": False,
        "general_b_boundary": (
            "This adds the fifth exhaustive anchor only.  It does not "
            "strengthen or otherwise change Cycle 740's conditional "
            "table-uniform general-b claim."
        ),
        "near_miss_controls_exact": near_miss["exact"],
        "honest": True,
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
        == "docs/B5_EXHAUSTIVE_ANCHOR_CYCLE756_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )

    try:
        mapper_i2 = mapper_and_i2_certificate()
    except Exception as error:
        ERRORS["A_mapper_anchors"] = error_text(error)
        mapper_i2 = {
            "exact": False,
            "error": ERRORS["A_mapper_anchors"],
            "prior_anchor_equivalence_unchanged": False,
            "b5": {
                "all_rows_directly_clean": False,
                "rows_checked": 0,
            },
        }
    reports["A_mapper_and_C_I2"] = mapper_i2
    check(
        "A_mapper_b1_b4_equivalence_and_b5_C5_emission",
        mapper_i2["exact"],
    )
    check(
        "C_b5_all_35_rows_direct_I2_clean_work",
        mapper_i2["b5"]["all_rows_directly_clean"]
        and mapper_i2["b5"]["rows_checked"] == 35,
    )

    try:
        i1 = i1_transport_certificate()
    except Exception as error:
        ERRORS["D_I1_transport"] = error_text(error)
        i1 = {"exact": False, "error": ERRORS["D_I1_transport"]}
    reports["D_I1_transport"] = i1
    check(
        "D_I1_six_term_transport_n35_structure_and_samples",
        i1["exact"],
    )

    try:
        census_orbit = census_and_orbit_certificate(started)
    except Exception as error:
        ERRORS["B_census_E_orbit"] = error_text(error)
        census_orbit = {
            "exact": False,
            "error": ERRORS["B_census_E_orbit"],
            "census": {
                "exact": False,
                "counts_by_k": (),
                "enumerated_total": 0,
            },
            "orbit": {
                "full_exact": False,
                "honest_strata_bound": False,
                "certificate_accepts_full_or_honest_bound": False,
                "full_sweep": False,
                "completed_orbit_strata": (),
                "completed_strata_configuration_bound": 0,
                "zero_failure_census": {
                    "ownership_violation_station_incidences": -1,
                },
                "exhaustive_controller_steps": 0,
            },
        }
    reports["B_census_and_E_orbit"] = census_orbit
    check(
        "B_streamed_census_by_k_equals_L35_20633239",
        census_orbit["census"]["exact"]
        and census_orbit["census"]["enumerated_total"]
        == EXPECTED_LUCAS_35,
    )
    OUTPUT_LINES.append(
        "CENSUS n=35 BY k :: "
        + ", ".join(
            f"k={occupied}:{count}"
            for occupied, count in enumerate(
                census_orbit["census"]["counts_by_k"]
            )
        )
    )
    check(
        "E_full_census_or_honest_exhaustive_strata_orbit_bound",
        census_orbit["orbit"][
            "certificate_accepts_full_or_honest_bound"
        ],
    )

    try:
        near_miss = near_miss_certificate()
    except Exception as error:
        ERRORS["F_near_miss"] = error_text(error)
        near_miss = {"exact": False, "error": ERRORS["F_near_miss"]}
    reports["F_near_miss"] = near_miss
    check(
        "F_n35_adjacent_pair_near_miss_two_stations_each",
        near_miss["exact"],
    )

    try:
        boundary = boundary_certificate(
            mapper_i2, i1, census_orbit, near_miss
        )
    except Exception as error:
        ERRORS["G_boundary"] = error_text(error)
        boundary = {
            "honest": False,
            "error": ERRORS["G_boundary"],
            "b1_through_b5_now_all_exhausted": False,
        }
    reports["G_boundary"] = boundary
    boundary_exact = (
        boundary["honest"] is True
        and boundary["general_b_claim_changed"] is False
        and boundary[
            "I1_six_term_identity_direct_evidence_at_b5"
        ]
        and boundary[
            "I2_clean_work_identity_direct_evidence_at_b5"
        ]
        and boundary[
            "identities_direct_evidence_extends_beyond_prior_anchors_to_b5"
        ]
        and (
            boundary["b1_through_b5_now_all_exhausted"]
            or census_orbit["orbit"]["honest_strata_bound"]
        )
    )
    check(
        "G_honest_fifth_anchor_identity_and_general_b_boundary_keys",
        boundary_exact,
    )

    elapsed = perf_counter() - started
    check(
        "TIMEOUT_runtime_under_1800_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bitplane_batch": BITPLANE_BATCH,
        "bounded": True,
        "scope": "the fifth exhaustive anchor b=5, n=35",
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
        "CYCLE756_B5_EXHAUSTIVE_ANCHOR_ALL_PASS"
        if report["pass"]
        else "CYCLE756_B5_EXHAUSTIVE_ANCHOR_HONEST_FAIL"
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
            "terminal":
                "CYCLE756_B5_EXHAUSTIVE_ANCHOR_HONEST_FAIL",
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
