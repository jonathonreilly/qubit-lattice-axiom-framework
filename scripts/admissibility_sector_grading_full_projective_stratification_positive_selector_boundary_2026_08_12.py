#!/usr/bin/env python3
"""Classify the complete projective grading space of the Cycle-876 model.

The parent package classified one affine chart and supplied one point at chart
infinity.  This runner rebuilds its stipulated six-direction, three-sector,
1,296-support model and classifies every nonzero real projective grading by
the exact rank-one lines and rank-two points on which a support can balance.

The result is conditional algebra.  It neither selects the grading physically
nor identifies it with generation chirality or a gravitational sign carrier.
"""

from __future__ import annotations

from collections import Counter
from functools import reduce
from itertools import combinations, product
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SECTOR_GRADING_FULL_PROJECTIVE_STRATIFICATION_POSITIVE_"
    "SELECTOR_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "GRADING_AFFINE_CHART_ALGEBRA_CYCLE876_SUPPORT_NOTE_2026-08-09.md"
)

AUDIT_TIMEOUT_SEC = 120


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, key, statement, condition, detail=""):
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def directions():
    out = []
    for axis in range(3):
        for sign in (1, -1):
            row = [0, 0, 0]
            row[axis] = sign
            out.append(tuple(row))
    return tuple(out)


DIRECTIONS = directions()


def all_supports():
    return tuple(
        (incoming, triple)
        for incoming in range(6)
        for triple in product(range(6), repeat=3)
    )


def support_matrix(incoming, triple):
    """Rows of M with M w = 0 the exact three-vector balance equation."""
    columns = (
        tuple(
            DIRECTIONS[triple[0]][axis] - DIRECTIONS[incoming][axis]
            for axis in range(3)
        ),
        DIRECTIONS[triple[1]],
        DIRECTIONS[triple[2]],
    )
    return tuple(
        tuple(columns[column][row] for column in range(3))
        for row in range(3)
    )


def det3(matrix):
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def matrix_vector(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def canonical(vector):
    entries = tuple(int(value) for value in vector)
    nonzero = [abs(value) for value in entries if value]
    if not nonzero:
        raise ValueError("zero vector has no projective class")
    divisor = reduce(gcd, nonzero)
    entries = tuple(value // divisor for value in entries)
    for value in entries:
        if value:
            return tuple(-item for item in entries) if value < 0 else entries
    raise AssertionError("unreachable")


def rank_and_kernel(matrix):
    determinant = det3(matrix)
    if determinant:
        return 3, None
    for left, right in combinations(matrix, 2):
        candidate = cross(left, right)
        if candidate != (0, 0, 0):
            return 2, canonical(candidate)
    for row in matrix:
        if row != (0, 0, 0):
            return 1, canonical(row)
    return 0, None


def has_strict_positive_representative(point):
    return all(value > 0 for value in point) or all(value < 0 for value in point)


def has_nonnegative_representative(point):
    return all(value >= 0 for value in point) or all(value <= 0 for value in point)


def classification():
    supports = all_supports()
    matrices = []
    rank_counts = Counter()
    line_multiplicities = Counter()
    point_multiplicities = Counter()

    for incoming, triple in supports:
        matrix = support_matrix(incoming, triple)
        rank, kernel = rank_and_kernel(matrix)
        matrices.append(matrix)
        rank_counts[rank] += 1
        if rank == 1:
            line_multiplicities[kernel] += 1
        elif rank == 2:
            point_multiplicities[kernel] += 1

    point_totals = {}
    point_incidence = {}
    for point, own_multiplicity in point_multiplicities.items():
        incident = tuple(
            sorted(
                (normal, multiplicity)
                for normal, multiplicity in line_multiplicities.items()
                if dot(normal, point) == 0
            )
        )
        point_incidence[point] = incident
        point_totals[point] = own_multiplicity + sum(
            multiplicity for _, multiplicity in incident
        )

    line_intersections = set()
    for left, right in combinations(line_multiplicities, 2):
        point = cross(left, right)
        if point != (0, 0, 0):
            line_intersections.add(canonical(point))

    direct_counts = {
        point: sum(
            matrix_vector(matrix, point) == (0, 0, 0) for matrix in matrices
        )
        for point in point_multiplicities
    }
    candidate_counts = list(point_totals.values()) + list(
        line_multiplicities.values()
    ) + [0]
    maximum = max(candidate_counts)
    maximizers = tuple(
        sorted(point for point, count in point_totals.items() if count == maximum)
    )

    strictly_positive_points = {
        point: count
        for point, count in point_totals.items()
        if has_strict_positive_representative(point)
    }
    strict_generic_bound = max(line_multiplicities.values(), default=0)
    strict_maximum = max(
        list(strictly_positive_points.values()) + [strict_generic_bound, 0]
    )
    strict_maximizers = tuple(
        sorted(
            point
            for point, count in strictly_positive_points.items()
            if count == strict_maximum
        )
    )
    nonnegative_maximizers = tuple(
        sorted(point for point in maximizers if has_nonnegative_representative(point))
    )

    return {
        "support_count": len(supports),
        "matrices": matrices,
        "rank_counts": dict(rank_counts),
        "line_multiplicities": dict(line_multiplicities),
        "point_multiplicities": dict(point_multiplicities),
        "point_incidence": point_incidence,
        "point_totals": point_totals,
        "line_intersections": line_intersections,
        "direct_counts": direct_counts,
        "maximum": maximum,
        "maximizers": maximizers,
        "strict_generic_bound": strict_generic_bound,
        "strict_maximum": strict_maximum,
        "strict_maximizers": strict_maximizers,
        "nonnegative_maximizers": nonnegative_maximizers,
    }


EXPECTED_LINES = {
    (0, 1, -1): 36,
    (0, 1, 1): 36,
    (2, -1, -1): 6,
    (2, -1, 1): 6,
    (2, 1, -1): 6,
    (2, 1, 1): 6,
}

EXPECTED_POINT_TOTALS = {
    (0, 1, -1): 216,
    (0, 1, 1): 216,
    (1, -2, 0): 36,
    (1, -1, -1): 90,
    (1, -1, 1): 90,
    (1, 0, -2): 36,
    (1, 0, 0): 216,
    (1, 0, 2): 36,
    (1, 1, -1): 90,
    (1, 1, 1): 90,
    (1, 2, 0): 36,
}


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    result = classification()

    print("analytic_boundary: exact integer projective stratification of the stipulated Cycle-876 finite model")
    print("physical_boundary: no sector grading, positivity domain, maximization principle, object lineage, chirality carrier, or gravity sign is selected")
    print("external_scientific_inputs: none; the parent model is reconstructed from its committed in-repository stipulations")

    checks.check(
        "source-and-axiom-boundary",
        "the parent leaves projective classification open and the axioms supply no sector-grading selector",
        "projective classification is OPEN" in parent
        and "No possibility is privileged" in axiom_flat
        and "A choice not fixed by the supplied structure" in axiom_flat,
    )
    checks.check(
        "complete-model-rank-stratification",
        "all 1,296 supports are partitioned by exact balance-matrix rank",
        result["support_count"] == 1296
        and result["rank_counts"] == {1: 96, 2: 768, 3: 432}
        and sum(result["rank_counts"].values()) == 1296,
        f"ranks={result['rank_counts']}",
    )
    checks.check(
        "rank-one-projective-lines",
        "the complete positive-dimensional lawful locus is six projective lines with exact multiplicities",
        result["line_multiplicities"] == EXPECTED_LINES,
        f"lines={sorted(result['line_multiplicities'].items())}",
    )
    checks.check(
        "rank-two-projective-points",
        "all isolated support kernels reduce to eleven projective classes",
        len(result["point_multiplicities"]) == 11
        and sum(result["point_multiplicities"].values()) == 768
        and result["line_intersections"].issubset(result["point_multiplicities"]),
        f"point multiplicities={sorted(result['point_multiplicities'].items())}",
    )
    checks.check(
        "incidence-count-identity",
        "direct support counts equal rank-two multiplicity plus every incident rank-one line",
        result["direct_counts"] == result["point_totals"]
        and result["point_totals"] == EXPECTED_POINT_TOTALS,
        f"point totals={sorted(result['point_totals'].items())}",
    )
    checks.check(
        "unrestricted-maximizer-fork",
        "the unrestricted projective maximum is 216 at exactly three classes",
        result["maximum"] == 216
        and result["maximizers"]
        == ((0, 1, -1), (0, 1, 1), (1, 0, 0))
        and "exactly three unrestricted maximizers" in note_flat,
        f"maximum={result['maximum']}; maximizers={result['maximizers']}",
    )
    checks.check(
        "strict-positive-unit-selector",
        "inside the strictly positive cone the unit class is the unique maximum",
        result["strict_generic_bound"] == 36
        and result["strict_maximum"] == 90
        and result["strict_maximizers"] == ((1, 1, 1),)
        and result["nonnegative_maximizers"] == ((0, 1, 1), (1, 0, 0))
        and "strict positivity plus lawful-support maximization" in note_flat,
        f"strict maximum={result['strict_maximum']}; strict maximizers={result['strict_maximizers']}; nonnegative unrestricted maximizers={result['nonnegative_maximizers']}",
    )
    checks.check(
        "axiom-choice-not-physical-identification",
        "the note keeps the selector premises and physical grading/sign bridges explicitly open",
        "No-Go Discipline Gate" in note
        and "Promotion Value Gate" in note
        and "not current-axiom content" in note_flat
        and "no toe percentage movement is claimed" in note_flat.lower()
        and "physical chirality/sign carrier" in note_flat,
    )

    print("per_element: checked every entry of every 3x3 balance matrix and primitive projective representative")
    print("per_site: checked the complete stipulated six-direction, three-sector one-block model")
    print("per_mode: checked all six projective lines, all eleven isolated points, and every line-point incidence; no Fourier-mode claim is made")
    print("per_block: checked all 1,296 supports and the exact unrestricted, nonnegative, and strictly positive selector domains")
    print("lattice_wide: checked and not executed — the stipulated one-block grading model is not a full-Z3, physical-lineage, chirality, or gravity theorem")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
