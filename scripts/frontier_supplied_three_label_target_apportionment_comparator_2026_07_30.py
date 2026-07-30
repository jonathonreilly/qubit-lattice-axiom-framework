#!/usr/bin/env python3
"""Exact finite arithmetic for a supplied three-label comparator fixture."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/SUPPLIED_THREE_LABEL_TARGET_APPORTIONMENT_COMPARATOR_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_supplied_three_label_target_apportionment_comparator_2026_07_30.py",
    "docs/SUPPLIED_THREE_LABEL_TARGET_APPORTIONMENT_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-07-30.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
TARGET_NUMERATORS = (
    36_002_393_478_282_646,
    21_194_155_104_147_802,
    42_803_451_417_569_552,
)
TARGET_DENOMINATOR = 100_000_000_000_000_000
PROFILE_SIZES = (8, 32, 128, 512)
PROFILE_COUNTS = (
    (3, 2, 3),
    (11, 7, 14),
    (46, 27, 55),
    (184, 109, 219),
)
TOLERANCES = (
    Fraction(3, 50),
    Fraction(1, 50),
    Fraction(1, 500),
    Fraction(1, 1000),
)
EXPECTED_DISAGREEMENT_COUNTS = (
    (0, 2, 3, 3),
    (0, 0, 3, 3),
    (0, 0, 0, 2),
    (0, 0, 0, 0),
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def declared_hashes() -> dict[str, str]:
    return {relative: digest(ROOT / relative) for relative in AUDIT_INPUT_PATHS}


def target() -> tuple[Fraction, ...]:
    return tuple(
        Fraction(numerator, TARGET_DENOMINATOR)
        for numerator in TARGET_NUMERATORS
    )


def largest_remainder(size: int) -> tuple[int, ...]:
    raw = tuple(
        Fraction(size * numerator, TARGET_DENOMINATOR)
        for numerator in TARGET_NUMERATORS
    )
    floors = [value.numerator // value.denominator for value in raw]
    remaining = size - sum(floors)
    order = sorted(
        range(len(raw)),
        key=lambda index: (raw[index] - floors[index], -index),
        reverse=True,
    )
    for index in order[:remaining]:
        floors[index] += 1
    return tuple(floors)


def comparison_row(size: int, counts: tuple[int, ...]) -> dict[str, object]:
    simplex = tuple(Fraction(count, size) for count in counts)
    residuals = tuple(
        left - right
        for left, right in zip(simplex, target(), strict=True)
    )
    disagreement_counts = tuple(
        sum(abs(residual) > tolerance for residual in residuals)
        for tolerance in TOLERANCES
    )
    return {
        "M": size,
        "counts": list(counts),
        "largest_remainder_counts": list(largest_remainder(size)),
        "simplex": [str(value) for value in simplex],
        "residuals": [str(value) for value in residuals],
        "maximum_absolute_residual": str(max(abs(value) for value in residuals)),
        "disagreement_counts": list(disagreement_counts),
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    hashes_before = declared_hashes()
    exact_target = target()

    check(
        "supplied target is an exact rational simplex",
        all(value >= 0 for value in exact_target)
        and sum(exact_target, start=Fraction()) == 1,
        tuple(str(value) for value in exact_target),
    )

    rows = tuple(
        comparison_row(size, counts)
        for size, counts in zip(PROFILE_SIZES, PROFILE_COUNTS, strict=True)
    )
    check(
        "authored profiles are exhaustive and equal their declared largest-remainder construction",
        all(
            len(counts) == len(TARGET_NUMERATORS)
            and all(count >= 0 for count in counts)
            and sum(counts) == size
            and counts == largest_remainder(size)
            for size, counts in zip(PROFILE_SIZES, PROFILE_COUNTS, strict=True)
        ),
        tuple((row["M"], row["counts"]) for row in rows),
    )
    check(
        "exact finite comparator census matches the declared table",
        tuple(tuple(row["disagreement_counts"]) for row in rows)
        == EXPECTED_DISAGREEMENT_COUNTS,
        tuple(tuple(row["disagreement_counts"]) for row in rows),
    )

    maximum_residuals = tuple(
        Fraction(str(row["maximum_absolute_residual"])) for row in rows
    )
    check(
        "the four supplied fixtures have strictly decreasing maximum discrepancies",
        all(
            left > right
            for left, right in zip(
                maximum_residuals[:-1],
                maximum_residuals[1:],
                strict=True,
            )
        ),
        tuple(str(value) for value in maximum_residuals),
    )

    control_rows = tuple(
        comparison_row(size, (size, 0, 0)) for size in PROFILE_SIZES
    )
    check(
        "first-slot-only hostile controls disagree in all slots at every declared tolerance",
        all(
            tuple(row["disagreement_counts"]) == (3, 3, 3, 3)
            for row in control_rows
        ),
        tuple(tuple(row["disagreement_counts"]) for row in control_rows),
    )

    hashes_after = declared_hashes()
    check(
        "declared source inputs stayed byte-stable",
        hashes_before == hashes_after
        and set(hashes_after) == set(AUDIT_INPUT_PATHS),
        hashes_after,
    )

    runtime = perf_counter() - started
    payload = {
        "all_checks_pass": FAIL == 0,
        "audit_input_sha256": hashes_after,
        "boundaries": {
            "asymptotic_convergence_claimed": False,
            "born_law_selected": False,
            "empirical_calibration_claimed": False,
            "framework_records_supplied": False,
            "occurrence_generator_supplied": False,
        },
        "check_totals": {"fail": FAIL, "pass": PASS},
        "control_rows": control_rows,
        "fixture_kind": "authored-largest-remainder-target-apportionment",
        "profile_rows": rows,
        "runtime_seconds": round(runtime, 6),
        "target": [str(value) for value in exact_target],
        "tolerances": [str(value) for value in TOLERANCES],
    }
    print("SUMMARY PASS", PASS, "FAIL", FAIL, "RUNTIME_SEC", f"{runtime:.6f}")
    print("RESULT_JSON", json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
