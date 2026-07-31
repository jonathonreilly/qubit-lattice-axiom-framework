#!/usr/bin/env python3
"""Cycle 756: exact finite graph-combinatorics census on C35.

This dependency-free runner proves and evaluates only the independent-set
stratum formula and the local occupied-endpoint incidence count for labelled
adjacent-pair masks. It contains no mapper, reversible-word, or controller
claim.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
from time import perf_counter


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/CYCLE_GRAPH_C35_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/CYCLE_GRAPH_C35_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STATIONS = 35
EXPECTED_STRATA = (
    1,
    35,
    560,
    5_425,
    35_525,
    166_257,
    573_300,
    1_480_050,
    2_877_875,
    4_206_125,
    4_576_264,
    3_640_210,
    2_057_510,
    791_350,
    193_800,
    27_132,
    1_785,
    35,
)
EXPECTED_TOTAL = 20_633_239
EXPECTED_PAIR_MASKS = 35
EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES = 70
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

    check("c35_closed_formula_matches_declared_strata", closed == EXPECTED_STRATA)
    check("c35_fraction_form_matches_closed_formula", fraction == closed)
    check("c35_path_split_matches_closed_formula", split == closed)
    check("c35_strata_sum_matches_declared_total", sum(closed) == EXPECTED_TOTAL)
    check("c35_total_matches_lucas_recurrence", sum(closed) == lucas_number(STATIONS))
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
        "occupied_endpoint_incidence_total_is_seventy",
        sum(incidence_rows) == EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES,
    )
    check(
        "note_declares_finite_graph_only_scope",
        "finite graph-combinatorics support result only" in note_text
        and "does not evaluate" in note_text
        and "any mapper" in note_text
        and "Independent claim audit remains required." in note_text,
    )

    report = {
        "cycle": 756,
        "claim": "c35_independent_set_census_and_adjacent_pair_incidences",
        "stations": STATIONS,
        "strata": list(closed),
        "independent_set_total": sum(closed),
        "lucas_number": lucas_number(STATIONS),
        "adjacent_pair_masks": len(pair_masks),
        "occupied_endpoint_incidences": sum(incidence_rows),
        "pair_mask_sha256": stable_digest(pair_masks),
        "passed": sum(CHECKS.values()),
        "failed": len(CHECKS) - sum(CHECKS.values()),
        "runtime_sec": round(perf_counter() - started, 6),
    }
    terminal = (
        "CYCLE756_C35_INDEPENDENT_SET_CENSUS_PASS"
        if report["failed"] == 0
        else "CYCLE756_C35_INDEPENDENT_SET_CENSUS_FAIL"
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
