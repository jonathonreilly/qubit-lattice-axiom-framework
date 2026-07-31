#!/usr/bin/env python3
"""Conditional finite-vector distance and S3 permutation certificate.

The vectors and comparator below are supplied synthetic inputs.  This runner
proves only exact normalization, L1/total-variation identities, and a finite
six-permutation statement.  It assigns no occurrence, probability, physical
outcome, apparatus, or framework meaning to the coordinates.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
import json


AUDIT_TIMEOUT_SEC = 30

VECTORS = (
    (13, 128, 68),
    (97, 1, 232),
    (432, 146, 5),
)
COMPARATOR = (
    Fraction(36002393478282646, 10**17),
    Fraction(21194155104147802, 10**17),
    Fraction(42803451417569552, 10**17),
)
UNIFORM = (Fraction(1, 3),) * 3

EXPECTED_IDENTITY_L1 = (
    (
        Fraction(4185210791616554691, 5225000000000000000),
        Fraction(350, 627),
    ),
    (
        Fraction(56717881451262799, 103125000000000000),
        Fraction(122, 165),
    ),
    (
        Fraction(1528400761027690551, 1821875000000000000),
        Fraction(1426, 1749),
    ),
)
EXPECTED_PERMUTATION_FLAGS = {
    (0, 1, 2): (False, True, False),
    (0, 2, 1): (False, False, True),
    (1, 0, 2): (True, True, False),
    (1, 2, 0): (False, False, True),
    (2, 0, 1): (True, False, False),
    (2, 1, 0): (False, True, True),
}


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


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": f"{float(value):.15f}",
        "exact": str(value),
    }


def identity_rows() -> tuple[dict[str, object], ...]:
    rows = []
    for index, vector in enumerate(VECTORS):
        simplex = normalize(vector)
        comparator_l1 = l1(simplex, COMPARATOR)
        uniform_l1 = l1(simplex, UNIFORM)
        rows.append(
            {
                "coordinate_row": index,
                "counts": vector,
                "simplex": tuple(str(value) for value in simplex),
                "simplex_sum": str(sum(simplex, start=Fraction())),
                "comparator_l1": fraction_record(comparator_l1),
                "comparator_tv": fraction_record(comparator_l1 / 2),
                "uniform_l1": fraction_record(uniform_l1),
                "uniform_tv": fraction_record(uniform_l1 / 2),
                "closer_to_comparator": comparator_l1 < uniform_l1,
            }
        )
    return tuple(rows)


def permutation_rows() -> tuple[dict[str, object], ...]:
    rows = []
    for permutation in permutations(range(3)):
        flags = []
        for vector in VECTORS:
            permuted = normalize(tuple(vector[index] for index in permutation))
            comparator_l1 = l1(permuted, COMPARATOR)
            uniform_l1 = l1(permuted, UNIFORM)
            if comparator_l1 == uniform_l1:
                raise AssertionError(("unexpected distance tie", permutation, vector))
            flags.append(comparator_l1 < uniform_l1)
        rows.append(
            {
                "permutation": permutation,
                "closer_to_comparator": tuple(flags),
                "all_three_closer": all(flags),
            }
        )
    return tuple(rows)


def main() -> int:
    identity = identity_rows()
    permuted = permutation_rows()
    observed_l1 = tuple(
        (
            l1(normalize(vector), COMPARATOR),
            l1(normalize(vector), UNIFORM),
        )
        for vector in VECTORS
    )
    observed_flags = {
        tuple(row["permutation"]): tuple(row["closer_to_comparator"])
        for row in permuted
    }
    checks = {
        "A supplied simplex domains": (
            len(VECTORS) == 3
            and all(len(vector) == 3 and sum(vector) > 0 for vector in VECTORS)
            and all(sum(normalize(vector), start=Fraction()) == 1 for vector in VECTORS)
            and len(COMPARATOR) == 3
            and all(value > 0 for value in COMPARATOR)
            and sum(COMPARATOR, start=Fraction()) == 1
            and sum(UNIFORM, start=Fraction()) == 1
            and COMPARATOR != UNIFORM
        ),
        "B exact identity-order L1 values": observed_l1 == EXPECTED_IDENTITY_L1,
        "C identity endpoint classification": tuple(
            row["closer_to_comparator"] for row in identity
        )
        == (False, True, False),
        "D exhaustive S3 classification": (
            len(permuted) == 6
            and len(observed_flags) == 6
            and observed_flags == EXPECTED_PERMUTATION_FLAGS
        ),
        "E no global coordinate permutation makes all three closer": not any(
            row["all_three_closer"] for row in permuted
        ),
        "F total variation is half L1": all(
            row["comparator_tv"]["exact"]
            == str(Fraction(row["comparator_l1"]["exact"]) / 2)
            and row["uniform_tv"]["exact"]
            == str(Fraction(row["uniform_l1"]["exact"]) / 2)
            for row in identity
        ),
    }
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label)
    report = {
        "boundary": (
            "supplied synthetic ordered vectors and comparator only; no physical "
            "mapping, occurrence, probability, frequency, apparatus, or framework claim"
        ),
        "checks": checks,
        "identity_rows": identity,
        "pass": all(checks.values()),
        "permutation_rows": permuted,
        "terminal": (
            "CYCLE763_CONDITIONAL_FINITE_VECTOR_PERMUTATION_PASS"
            if all(checks.values())
            else "CYCLE763_CONDITIONAL_FINITE_VECTOR_PERMUTATION_FAIL"
        ),
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
