#!/usr/bin/env python3
"""Independent exact check of the supplied Cycle-766 S3-cubed census.

This checker intentionally does not import the primary Cycle-766 runner.  It
uses inverse-index transformation and direct count-vector distance formulas as
a separate implementation path over the same supplied Cycle-763 inputs.
"""

from __future__ import annotations

from fractions import Fraction
import json

from frontier_cycle763_symmetry_broken_ensembles_2026_07_28 import (
    COMPARATOR,
    VECTORS,
)


AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
)

SUPPLIED_PER_ROW_BIJECTION = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)
EXPECTED_ROWS = (
    (13, 128, 68),
    (232, 97, 1),
    (146, 5, 432),
)
EXPECTED_POOL = (391, 230, 501)
EXPECTED_COMPARATOR_TV = (
    Fraction(4185210791616554691, 10450000000000000000),
    Fraction(87657118548737201, 206250000000000000),
    Fraction(1140349238972309449, 3643750000000000000),
    Fraction(21609661557155861, 1168750000000000000),
)
EXPECTED_UNIFORM_TV = (
    Fraction(175, 627),
    Fraction(61, 165),
    Fraction(713, 1749),
    Fraction(24, 187),
)
EXPECTED_SECOND_SCORE = Fraction(
    823671370658282203,
    28050000000000000000,
)


def enumerate_bijections() -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (a, b, c)
        for a in range(3)
        for b in range(3)
        for c in range(3)
        if a != b and a != c and b != c
    )


def transform_by_inverse_index(
    vector: tuple[int, int, int],
    input_to_output: tuple[int, int, int],
) -> tuple[int, int, int]:
    if set(input_to_output) != {0, 1, 2}:
        raise ValueError("mapping must be a bijection")
    return tuple(
        vector[input_to_output.index(output_coordinate)]
        for output_coordinate in range(3)
    )


def direct_tv(
    counts: tuple[int, int, int],
    target: tuple[Fraction, Fraction, Fraction],
) -> Fraction:
    denominator = sum(counts)
    if denominator <= 0:
        raise ValueError("counts must have positive total")
    return sum(
        abs(Fraction(count, denominator) - target[index])
        for index, count in enumerate(counts)
    ) / 2


def add_rows(rows: tuple[tuple[int, int, int], ...]) -> tuple[int, int, int]:
    return (
        sum(row[0] for row in rows),
        sum(row[1] for row in rows),
        sum(row[2] for row in rows),
    )


def main() -> int:
    uniform = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    bijections = enumerate_bijections()
    candidate_rows = tuple(
        transform_by_inverse_index(vector, mapping)
        for vector, mapping in zip(
            VECTORS,
            SUPPLIED_PER_ROW_BIJECTION,
            strict=True,
        )
    )
    candidate_pool = add_rows(candidate_rows)
    candidate_scopes = (*candidate_rows, candidate_pool)
    comparator_values = tuple(direct_tv(scope, COMPARATOR) for scope in candidate_scopes)
    uniform_values = tuple(direct_tv(scope, uniform) for scope in candidate_scopes)

    scores: list[Fraction] = []
    pooled_closer = 0
    all_scopes_closer = 0
    candidate_occurrences = 0
    for first in bijections:
        for second in bijections:
            for third in bijections:
                mapping = (first, second, third)
                rows = (
                    transform_by_inverse_index(VECTORS[0], first),
                    transform_by_inverse_index(VECTORS[1], second),
                    transform_by_inverse_index(VECTORS[2], third),
                )
                scopes = (*rows, add_rows(rows))
                comparator_distances = tuple(direct_tv(scope, COMPARATOR) for scope in scopes)
                uniform_distances = tuple(direct_tv(scope, uniform) for scope in scopes)
                scores.append(comparator_distances[-1])
                pooled_closer += comparator_distances[-1] < uniform_distances[-1]
                all_scopes_closer += all(
                    comparator_tv < uniform_tv
                    for comparator_tv, uniform_tv in zip(
                        comparator_distances,
                        uniform_distances,
                        strict=True,
                    )
                )
                candidate_occurrences += mapping == SUPPLIED_PER_ROW_BIJECTION

    candidate_score = comparator_values[-1]
    strictly_lower = sum(score < candidate_score for score in scores)
    tied = sum(score == candidate_score for score in scores)
    distinct_scores = sorted(set(scores))

    checks = {
        "A independently enumerated S3 cubed": (
            len(bijections) == 6
            and len(set(bijections)) == 6
            and len(scores) == 216
        ),
        "B inverse-index transform reproduces exact rows": (
            candidate_rows == EXPECTED_ROWS and candidate_pool == EXPECTED_POOL
        ),
        "C direct exact comparator distances": comparator_values
        == EXPECTED_COMPARATOR_TV,
        "D direct exact uniform distances": uniform_values == EXPECTED_UNIFORM_TV,
        "E independent endpoint classifications": tuple(
            comparator_tv < uniform_tv
            for comparator_tv, uniform_tv in zip(
                comparator_values,
                uniform_values,
                strict=True,
            )
        )
        == (False, False, True, True),
        "F independent unique pooled rank": strictly_lower == 0 and tied == 1,
        "G independent next score and endpoint counts": (
            distinct_scores[0] == candidate_score
            and distinct_scores[1] == EXPECTED_SECOND_SCORE
            and pooled_closer == 91
            and all_scopes_closer == 18
        ),
        "H candidate appears once": candidate_occurrences == 1,
    }

    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label)

    report = {
        "boundary": (
            "independent exact check of supplied synthetic rows, comparator, "
            "coordinate order, and per-row bijection over S3 cubed only"
        ),
        "checks": checks,
        "comparator_tv_exact": tuple(str(value) for value in comparator_values),
        "mapping_input_to_output": SUPPLIED_PER_ROW_BIJECTION,
        "next_distinct_pooled_comparator_tv_exact": str(distinct_scores[1]),
        "pass": all(checks.values()),
        "pooled": candidate_pool,
        "rank_by_pooled_comparator_tv": (1, 1),
        "rows": candidate_rows,
        "terminal": (
            "CYCLE766_INDEPENDENT_CONDITIONAL_S3_CUBED_PASS"
            if all(checks.values())
            else "CYCLE766_INDEPENDENT_CONDITIONAL_S3_CUBED_FAIL"
        ),
        "uniform_tv_exact": tuple(str(value) for value in uniform_values),
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
