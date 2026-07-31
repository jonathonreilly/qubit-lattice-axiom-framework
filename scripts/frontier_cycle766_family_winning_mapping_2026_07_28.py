#!/usr/bin/env python3
"""Exact conditional census for a supplied cyclic member of S3 cubed.

The ordered count vectors and comparator are supplied synthetic inputs from
the current Cycle-763 conditional arithmetic source.  The per-row bijection is
also supplied.  This runner proves only exact finite transformation, distance,
and S3-cubed census statements.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
import json

from frontier_cycle763_symmetry_broken_ensembles_2026_07_28 import (
    COMPARATOR,
    VECTORS,
)


AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
)

UNIFORM = (Fraction(1, 3),) * 3

# Each tuple maps supplied input coordinate -> output coordinate.  This is a
# theorem condition, not a derived association.
SUPPLIED_PER_ROW_BIJECTION = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)

EXPECTED_TRANSFORMED_ROWS = (
    (13, 128, 68),
    (232, 97, 1),
    (146, 5, 432),
)
EXPECTED_POOLED = (391, 230, 501)

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
EXPECTED_SCOPE_FLAGS = (False, False, True, True)
EXPECTED_SECOND_DISTINCT_POOLED_TV = Fraction(
    823671370658282203,
    28050000000000000000,
)


def normalize(vector: tuple[int, ...]) -> tuple[Fraction, ...]:
    total = sum(vector)
    if total <= 0:
        raise ValueError("vectors must have positive total")
    return tuple(Fraction(value, total) for value in vector)


def total_variation(
    vector: tuple[Fraction, ...],
    target: tuple[Fraction, ...],
) -> Fraction:
    return sum(
        (abs(value - expected) for value, expected in zip(vector, target, strict=True)),
        start=Fraction(),
    ) / 2


def apply_input_to_output_bijection(
    vector: tuple[int, ...],
    mapping: tuple[int, ...],
) -> tuple[int, ...]:
    if tuple(sorted(mapping)) != tuple(range(len(vector))):
        raise ValueError("mapping must be a bijection")
    output = [0] * len(vector)
    for input_coordinate, count in enumerate(vector):
        output[mapping[input_coordinate]] += count
    return tuple(output)


def pool(rows: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(sum(row[index] for row in rows) for index in range(3))


def distance_bundle(
    rows: tuple[tuple[int, ...], ...],
) -> tuple[tuple[Fraction, Fraction], ...]:
    return tuple(
        (
            total_variation(normalize(scope), COMPARATOR),
            total_variation(normalize(scope), UNIFORM),
        )
        for scope in (*rows, pool(rows))
    )


def family_census() -> tuple[dict[str, object], ...]:
    bijections = tuple(permutations(range(3)))
    records = []
    for mapping in product(bijections, repeat=3):
        rows = tuple(
            apply_input_to_output_bijection(vector, row_mapping)
            for vector, row_mapping in zip(VECTORS, mapping, strict=True)
        )
        distances = distance_bundle(rows)
        records.append(
            {
                "mapping": mapping,
                "pooled_comparator_tv": distances[-1][0],
                "pooled_comparator_closer": distances[-1][0] < distances[-1][1],
                "all_scopes_comparator_closer": all(
                    comparator_tv < uniform_tv
                    for comparator_tv, uniform_tv in distances
                ),
            }
        )
    return tuple(records)


def fraction_record(value: Fraction) -> dict[str, str]:
    return {"decimal": f"{float(value):.15f}", "exact": str(value)}


def main() -> int:
    candidate_rows = tuple(
        apply_input_to_output_bijection(vector, mapping)
        for vector, mapping in zip(
            VECTORS,
            SUPPLIED_PER_ROW_BIJECTION,
            strict=True,
        )
    )
    candidate_pooled = pool(candidate_rows)
    candidate_distances = distance_bundle(candidate_rows)
    candidate_score = candidate_distances[-1][0]
    census = family_census()

    strictly_lower = sum(
        record["pooled_comparator_tv"] < candidate_score for record in census
    )
    tied = sum(
        record["pooled_comparator_tv"] == candidate_score for record in census
    )
    distinct_scores = sorted({record["pooled_comparator_tv"] for record in census})
    pooled_closer = sum(record["pooled_comparator_closer"] for record in census)
    all_scopes_closer = sum(
        record["all_scopes_comparator_closer"] for record in census
    )

    checks = {
        "A supplied domains and simplexes": (
            len(VECTORS) == 3
            and all(len(vector) == 3 and sum(vector) > 0 for vector in VECTORS)
            and len(COMPARATOR) == 3
            and all(value > 0 for value in COMPARATOR)
            and sum(COMPARATOR, start=Fraction()) == 1
            and sum(UNIFORM, start=Fraction()) == 1
            and all(
                tuple(sorted(mapping)) == (0, 1, 2)
                for mapping in SUPPLIED_PER_ROW_BIJECTION
            )
        ),
        "B exact supplied-map transformed rows": (
            candidate_rows == EXPECTED_TRANSFORMED_ROWS
            and candidate_pooled == EXPECTED_POOLED
            and tuple(map(sum, candidate_rows)) == tuple(map(sum, VECTORS))
        ),
        "C exact endpoint total-variation values": (
            tuple(pair[0] for pair in candidate_distances) == EXPECTED_COMPARATOR_TV
            and tuple(pair[1] for pair in candidate_distances) == EXPECTED_UNIFORM_TV
        ),
        "D exact endpoint classifications": tuple(
            comparator_tv < uniform_tv
            for comparator_tv, uniform_tv in candidate_distances
        )
        == EXPECTED_SCOPE_FLAGS,
        "E exhaustive S3-cubed family cardinality": (
            len(census) == 216
            and len({record["mapping"] for record in census}) == 216
        ),
        "F unique pooled minimum and exact rank": (
            strictly_lower == 0 and tied == 1
        ),
        "G exact second distinct pooled score": (
            len(distinct_scores) > 1
            and distinct_scores[0] == candidate_score
            and distinct_scores[1] == EXPECTED_SECOND_DISTINCT_POOLED_TV
        ),
        "H exact S3-cubed endpoint counts": (
            pooled_closer == 91 and all_scopes_closer == 18
        ),
        "I supplied map occurs exactly once": sum(
            record["mapping"] == SUPPLIED_PER_ROW_BIJECTION for record in census
        )
        == 1,
    }

    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label)

    report = {
        "boundary": (
            "supplied synthetic vectors, comparator, coordinate order, and per-row "
            "bijection; exhaustive only over S3 cubed; finite conditional arithmetic only"
        ),
        "candidate": {
            "comparator_tv": tuple(
                fraction_record(pair[0]) for pair in candidate_distances
            ),
            "mapping_input_to_output": SUPPLIED_PER_ROW_BIJECTION,
            "pooled": candidate_pooled,
            "rank_by_pooled_comparator_tv": (1, 1),
            "rows": candidate_rows,
            "uniform_tv": tuple(
                fraction_record(pair[1]) for pair in candidate_distances
            ),
        },
        "checks": checks,
        "family": {
            "all_four_scopes_comparator_closer": all_scopes_closer,
            "members": len(census),
            "next_distinct_pooled_comparator_tv": fraction_record(
                distinct_scores[1]
            ),
            "pooled_comparator_closer": pooled_closer,
            "ties_at_candidate_pooled_comparator_tv": tied,
        },
        "pass": all(checks.values()),
        "terminal": (
            "CYCLE766_CONDITIONAL_S3_CUBED_UNIQUE_MINIMUM_PASS"
            if all(checks.values())
            else "CYCLE766_CONDITIONAL_S3_CUBED_UNIQUE_MINIMUM_FAIL"
        ),
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
