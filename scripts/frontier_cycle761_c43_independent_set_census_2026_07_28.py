#!/usr/bin/env python3
"""Cycle 761: exact finite graph-combinatorics census on C43.

This dependency-free runner proves and evaluates only the independent-set
stratum formula, labelled adjacent-pair masks, and a finite family of labelled
one-edge masks. It contains no mapper, reversible-word, or controller claim.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
from time import perf_counter


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/CYCLE_GRAPH_C43_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/CYCLE_GRAPH_C43_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STATIONS = 43
EXPECTED_STRATA = (
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
EXPECTED_TOTAL = 969_323_029
EXPECTED_PAIR_MASKS = 43
EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES = 86
ONE_EDGE_MIN_OCCUPIED = 12
ONE_EDGE_MAX_OCCUPIED = 21
ONE_EDGE_PHASES = (0, 1)
EXPECTED_ONE_EDGE_MASKS = 860
EXPECTED_ONE_EDGE_OCCUPIED_ENDPOINT_INCIDENCES = 1_720
STDOUT_LIMIT_BYTES = 150 * 1024

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def path_independence_polynomial(length: int) -> tuple[int, ...]:
    """Return path independent-set counts using P_m=P_(m-1)+xP_(m-2)."""

    if length == 0:
        return (1,)
    if length == 1:
        return (1, 1)
    older = (1,)
    newer = (1, 1)
    for _ in range(2, length + 1):
        width = max(len(newer), len(older) + 1)
        current = [0] * width
        for occupied, count in enumerate(newer):
            current[occupied] += count
        for occupied, count in enumerate(older):
            current[occupied + 1] += count
        older, newer = newer, tuple(current)
    return newer


def cycle_strata_from_split(stations: int) -> tuple[int, ...]:
    """Split on vertex zero: P_(n-1)+xP_(n-3)."""

    without_zero = path_independence_polynomial(stations - 1)
    with_zero = path_independence_polynomial(stations - 3)
    strata = [0] * (stations // 2 + 1)
    for occupied, count in enumerate(without_zero):
        if occupied < len(strata):
            strata[occupied] += count
    for occupied, count in enumerate(with_zero):
        if occupied + 1 < len(strata):
            strata[occupied + 1] += count
    return tuple(strata)


def cycle_strata_from_closed_formula(stations: int) -> tuple[int, ...]:
    rows = [1]
    for occupied in range(1, stations // 2 + 1):
        rows.append(
            comb(stations - occupied, occupied)
            + comb(stations - occupied - 1, occupied - 1)
        )
    return tuple(rows)


def cycle_strata_from_fraction_form(stations: int) -> tuple[int, ...]:
    rows = [1]
    for occupied in range(1, stations // 2 + 1):
        numerator = stations * comb(stations - occupied, occupied)
        denominator = stations - occupied
        quotient, remainder = divmod(numerator, denominator)
        if remainder:
            raise AssertionError(("nonintegral cycle count", stations, occupied))
        rows.append(quotient)
    return tuple(rows)


def lucas_number(index: int) -> int:
    if index == 0:
        return 2
    if index == 1:
        return 1
    older, newer = 2, 1
    for _ in range(2, index + 1):
        older, newer = newer, older + newer
    return newer


def rotate_left(mask: int, shift: int, width: int) -> int:
    full = (1 << width) - 1
    shift %= width
    if shift == 0:
        return mask & full
    return ((mask << shift) & full) | (mask >> (width - shift))


def adjacent_pair_masks(stations: int) -> tuple[int, ...]:
    return tuple(
        (1 << station) | (1 << ((station + 1) % stations))
        for station in range(stations)
    )


def occupied_endpoint_incidences(mask: int, stations: int) -> int:
    return sum(
        bool(mask & (1 << station))
        and bool(
            mask
            & (
                (1 << ((station - 1) % stations))
                | (1 << ((station + 1) % stations))
            )
        )
        for station in range(stations)
    )


def occupied_edges(mask: int, stations: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (station, (station + 1) % stations)
        for station in range(stations)
        if mask & (1 << station)
        and mask & (1 << ((station + 1) % stations))
    )


def one_edge_mask(
    stations: int, occupied: int, edge_start: int, phase: int
) -> int:
    mask = (1 << edge_start) | (1 << ((edge_start + 1) % stations))
    for index in range(occupied - 2):
        station = (edge_start + 3 + phase + 2 * index) % stations
        mask |= 1 << station
    return mask


def one_edge_mask_rows(
    stations: int,
) -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        (
            occupied,
            edge_start,
            phase,
            one_edge_mask(stations, occupied, edge_start, phase),
        )
        for occupied in range(ONE_EDGE_MIN_OCCUPIED, ONE_EDGE_MAX_OCCUPIED + 1)
        for edge_start in range(stations)
        for phase in ONE_EDGE_PHASES
    )


def stable_digest(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":")
    ).encode()
    return sha256(encoded).hexdigest()


def main() -> int:
    started = perf_counter()
    root = Path(__file__).resolve().parents[1]
    note_text = (root / NOTE_PATH).read_text(encoding="utf-8")

    closed = cycle_strata_from_closed_formula(STATIONS)
    fraction = cycle_strata_from_fraction_form(STATIONS)
    split = cycle_strata_from_split(STATIONS)
    pair_masks = adjacent_pair_masks(STATIONS)
    incidence_rows = tuple(
        occupied_endpoint_incidences(mask, STATIONS) for mask in pair_masks
    )
    one_edge_rows = one_edge_mask_rows(STATIONS)
    one_edge_masks = tuple(row[3] for row in one_edge_rows)
    one_edge_incidences = tuple(
        occupied_endpoint_incidences(mask, STATIONS) for mask in one_edge_masks
    )

    check("c43_closed_formula_matches_declared_strata", closed == EXPECTED_STRATA)
    check("c43_fraction_form_matches_closed_formula", fraction == closed)
    check("c43_path_split_matches_closed_formula", split == closed)
    check("c43_strata_sum_matches_declared_total", sum(closed) == EXPECTED_TOTAL)
    check("c43_total_matches_lucas_recurrence", sum(closed) == lucas_number(STATIONS))
    check(
        "adjacent_pair_mask_census_is_exact",
        len(pair_masks) == EXPECTED_PAIR_MASKS
        and len(set(pair_masks)) == EXPECTED_PAIR_MASKS,
    )
    check(
        "adjacent_pair_masks_have_two_occupied_vertices",
        all(mask.bit_count() == 2 for mask in pair_masks),
    )
    check(
        "adjacent_pair_masks_are_rotations_of_one_labelled_mask",
        set(pair_masks)
        == {rotate_left(pair_masks[0], shift, STATIONS) for shift in range(STATIONS)},
    )
    check(
        "each_pair_has_two_occupied_endpoint_incidences",
        incidence_rows == (2,) * EXPECTED_PAIR_MASKS,
    )
    check(
        "occupied_endpoint_incidence_total_is_eighty_six",
        sum(incidence_rows) == EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES,
    )
    check(
        "one_edge_family_has_exact_structural_row_count",
        len(one_edge_rows)
        == (ONE_EDGE_MAX_OCCUPIED - ONE_EDGE_MIN_OCCUPIED + 1)
        * STATIONS
        * len(ONE_EDGE_PHASES)
        == EXPECTED_ONE_EDGE_MASKS,
    )
    check(
        "one_edge_family_masks_are_pairwise_distinct",
        len(set(one_edge_masks)) == len(one_edge_masks),
    )
    check(
        "one_edge_family_rows_have_declared_cardinality",
        all(mask.bit_count() == occupied for occupied, _, _, mask in one_edge_rows),
    )
    check(
        "one_edge_family_rows_have_exactly_the_labelled_edge",
        all(
            occupied_edges(mask, STATIONS)
            == ((edge_start, (edge_start + 1) % STATIONS),)
            for _, edge_start, _, mask in one_edge_rows
        ),
    )
    check(
        "one_edge_family_has_exact_occupied_endpoint_incidence_total",
        one_edge_incidences == (2,) * EXPECTED_ONE_EDGE_MASKS
        and sum(one_edge_incidences)
        == EXPECTED_ONE_EDGE_OCCUPIED_ENDPOINT_INCIDENCES,
    )
    check(
        "note_declares_finite_graph_only_scope",
        "finite graph-combinatorics support result only" in note_text
        and "does not evaluate" in note_text
        and "any mapper" in note_text
        and "Independent claim audit remains required" in note_text,
    )

    report = {
        "cycle": 761,
        "claim": "c43_independent_set_census_and_adjacent_pair_incidences",
        "stations": STATIONS,
        "strata": list(closed),
        "independent_set_total": sum(closed),
        "lucas_number": lucas_number(STATIONS),
        "adjacent_pair_masks": len(pair_masks),
        "occupied_endpoint_incidences": sum(incidence_rows),
        "pair_mask_sha256": stable_digest(pair_masks),
        "one_edge_occupied_range": [ONE_EDGE_MIN_OCCUPIED, ONE_EDGE_MAX_OCCUPIED],
        "one_edge_phases": list(ONE_EDGE_PHASES),
        "one_edge_masks": len(one_edge_masks),
        "one_edge_occupied_endpoint_incidences": sum(one_edge_incidences),
        "one_edge_mask_sha256": stable_digest(one_edge_masks),
        "passed": sum(CHECKS.values()),
        "failed": len(CHECKS) - sum(CHECKS.values()),
        "runtime_sec": round(perf_counter() - started, 6),
    }
    terminal = (
        "CYCLE761_C43_INDEPENDENT_SET_CENSUS_PASS"
        if report["failed"] == 0
        else "CYCLE761_C43_INDEPENDENT_SET_CENSUS_FAIL"
    )
    report["terminal"] = terminal
    rendered = OUTPUT_LINES + [
        json.dumps(report, sort_keys=True, separators=(",", ":")),
        terminal,
    ]
    output = "\n".join(rendered) + "\n"
    if len(output.encode()) > STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout budget exceeded")
    print(output, end="")
    return 0 if report["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
