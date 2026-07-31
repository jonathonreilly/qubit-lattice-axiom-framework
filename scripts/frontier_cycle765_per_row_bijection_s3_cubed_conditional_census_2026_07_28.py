#!/usr/bin/env python3
"""Exact conditional census for one supplied member of S3 cubed.

The count vectors and comparator are supplied synthetic inputs inherited from
the Cycle-763 conditional arithmetic certificate.  The per-row bijection is
also supplied.  This runner proves only exact finite normalization, distance,
and S3-cubed census statements.  It assigns no occurrence, probability,
physical outcome, apparatus, selector, convergence, or framework meaning.
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

UNIFORM = (Fraction(1, 3),) * 3

# Each tuple maps feature index -> output index.  This is a supplied theorem
# condition, not a derived association.
SUPPLIED_PER_ROW_BIJECTION = (
    (1, 2, 0),
    (0, 1, 2),
    (2, 0, 1),
)

EXPECTED_TRANSFORMED_ROWS = (
    (68, 13, 128),
    (97, 1, 232),
    (146, 5, 432),
)
EXPECTED_POOLED = (311, 19, 792)

EXPECTED_COMPARATOR_TV = (
    Fraction(240879915857997727, 1306250000000000000),
    Fraction(56717881451262799, 206250000000000000),
    Fraction(1140349238972309449, 3643750000000000000),
    Fraction(29521332868832351, 106250000000000000),
)
EXPECTED_UNIFORM_TV = (
    Fraction(175, 627),
    Fraction(61, 165),
    Fraction(713, 1749),
    Fraction(19, 51),
)


def normalize(vector: tuple[int, ...]) -> tuple[Fraction, ...]:
    total = sum(vector)
    if total <= 0:
        raise ValueError("vectors must have positive total")
    return tuple(Fraction(value, total) for value in vector)


def l1(
    vector: tuple[Fraction, ...],
    target: tuple[Fraction, ...],
) -> Fraction:
    return sum(
        (abs(value - expected) for value, expected in zip(vector, target, strict=True)),
        start=Fraction(),
    )


def total_variation(
    vector: tuple[Fraction, ...],
    target: tuple[Fraction, ...],
) -> Fraction:
    return l1(vector, target) / 2


def apply_feature_to_output_bijection(
    vector: tuple[int, ...],
    mapping: tuple[int, ...],
) -> tuple[int, ...]:
    if tuple(sorted(mapping)) != tuple(range(len(vector))):
        raise ValueError("mapping must be a bijection of the output indices")
    output = [0] * len(vector)
    for feature_index, count in enumerate(vector):
        output[mapping[feature_index]] += count
    return tuple(output)


def pool(rows: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(sum(row[index] for row in rows) for index in range(3))


def distance_bundle(
    rows: tuple[tuple[int, ...], ...],
) -> tuple[tuple[Fraction, Fraction], ...]:
    scopes = (*rows, pool(rows))
    return tuple(
        (
            total_variation(normalize(scope), COMPARATOR),
            total_variation(normalize(scope), UNIFORM),
        )
        for scope in scopes
    )


def family_census() -> tuple[dict[str, object], ...]:
    local_bijections = tuple(permutations(range(3)))
    records = []
    for mapping in product(local_bijections, repeat=3):
        rows = tuple(
            apply_feature_to_output_bijection(vector, local_map)
            for vector, local_map in zip(VECTORS, mapping, strict=True)
        )
        distances = distance_bundle(rows)
        records.append(
            {
                "mapping": mapping,
                "pooled_comparator_tv": distances[-1][0],
                "pooled_closer_to_comparator": distances[-1][0] < distances[-1][1],
                "all_scopes_closer_to_comparator": all(
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
        apply_feature_to_output_bijection(vector, mapping)
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
        row["pooled_comparator_tv"] < candidate_score for row in census
    )
    tied = sum(row["pooled_comparator_tv"] == candidate_score for row in census)
    all_scope = sum(row["all_scopes_closer_to_comparator"] for row in census)
    pooled_closer = sum(row["pooled_closer_to_comparator"] for row in census)

    checks = {
        "A supplied domains and simplexes": (
            len(VECTORS) == 3
            and all(len(vector) == 3 and sum(vector) > 0 for vector in VECTORS)
            and all(sum(normalize(vector), start=Fraction()) == 1 for vector in VECTORS)
            and len(COMPARATOR) == 3
            and all(value > 0 for value in COMPARATOR)
            and sum(COMPARATOR, start=Fraction()) == 1
            and sum(UNIFORM, start=Fraction()) == 1
            and COMPARATOR != UNIFORM
            and all(
                tuple(sorted(mapping)) == (0, 1, 2)
                for mapping in SUPPLIED_PER_ROW_BIJECTION
            )
        ),
        "B exact supplied-map transformed rows": (
            candidate_rows == EXPECTED_TRANSFORMED_ROWS
            and candidate_pooled == EXPECTED_POOLED
            and tuple(sum(row) for row in candidate_rows)
            == tuple(sum(vector) for vector in VECTORS)
        ),
        "C exact endpoint total-variation values": (
            tuple(row[0] for row in candidate_distances) == EXPECTED_COMPARATOR_TV
            and tuple(row[1] for row in candidate_distances) == EXPECTED_UNIFORM_TV
            and all(
                2 * comparator_tv
                == l1(normalize(scope), COMPARATOR)
                for scope, (comparator_tv, _uniform_tv) in zip(
                    (*candidate_rows, candidate_pooled),
                    candidate_distances,
                    strict=True,
                )
            )
        ),
        "D supplied map is comparator-closer at four scopes": all(
            comparator_tv < uniform_tv
            for comparator_tv, uniform_tv in candidate_distances
        ),
        "E exhaustive S3-cubed family cardinality": (
            len(census) == 216
            and len({row["mapping"] for row in census}) == 216
            and all(
                len(row["mapping"]) == 3
                and all(tuple(sorted(mapping)) == (0, 1, 2) for mapping in row["mapping"])
                for row in census
            )
        ),
        "F exact supplied-map pooled rank interval": (
            strictly_lower == 122
            and tied == 6
            and (strictly_lower + 1, strictly_lower + tied) == (123, 128)
        ),
        "G exact S3-cubed endpoint counts": (
            all_scope == 18 and pooled_closer == 91
        ),
        "H supplied map is present in census": sum(
            row["mapping"] == SUPPLIED_PER_ROW_BIJECTION for row in census
        )
        == 1,
    }

    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label)

    report = {
        "boundary": (
            "supplied synthetic vectors, comparator, coordinate order, and per-row "
            "bijection; exhaustive only over S3 cubed; no physical mapping, "
            "occurrence, probability, frequency, apparatus, selector, convergence, "
            "framework, or no-go claim"
        ),
        "candidate": {
            "comparator_tv": tuple(
                fraction_record(row[0]) for row in candidate_distances
            ),
            "mapping_feature_index_to_output_index": SUPPLIED_PER_ROW_BIJECTION,
            "pooled": candidate_pooled,
            "rank_interval_by_pooled_comparator_tv": (123, 128),
            "rows": candidate_rows,
            "uniform_tv": tuple(
                fraction_record(row[1]) for row in candidate_distances
            ),
        },
        "checks": checks,
        "family": {
            "all_four_scopes_comparator_closer": all_scope,
            "members": len(census),
            "pooled_comparator_closer": pooled_closer,
            "strictly_lower_pooled_comparator_tv": strictly_lower,
            "ties_at_candidate_pooled_comparator_tv": tied,
        },
        "pass": all(checks.values()),
        "terminal": (
            "CYCLE765_CONDITIONAL_S3_CUBED_CENSUS_PASS"
            if all(checks.values())
            else "CYCLE765_CONDITIONAL_S3_CUBED_CENSUS_FAIL"
        ),
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
