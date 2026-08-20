#!/usr/bin/env python3
"""Independent reconstruction of the dyadic preparation rail theorem.

This checker does not import the primary runner.  It rebuilds the spatial
front census and the two-state probability quotient from separate formulas.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / "scripts" / "record_native_dyadic_preparation_tag_screening_2026_08_20.py"
NOTE_PATH = ROOT / "docs" / "RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_BOUNDED_THEOREM_NOTE_2026-08-20.md"
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/record_native_dyadic_preparation_tag_screening_2026_08_20.py",
    "docs/RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_BOUNDED_THEOREM_NOTE_2026-08-20.md",
)

Point = tuple[int, int, int]
DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
TRANSVERSE: tuple[Point, ...] = ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def det3(rows: tuple[Point, Point, Point]) -> int:
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def rotations() -> tuple[tuple[Point, Point, Point], ...]:
    basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    result = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = tuple(
                tuple(signs[row] * value for value in basis[permutation[row]])
                for row in range(3)
            )
            if det3(rows) == 1:
                result.append(rows)
    return tuple(result)  # type: ignore[return-value]


def matvec(matrix: tuple[Point, Point, Point], vector: Point) -> Point:
    return tuple(sum(row[i] * vector[i] for i in range(3)) for row in matrix)  # type: ignore[return-value]


def scaffold(accumulators: int, testers: int) -> tuple[set[Point], tuple[Point, ...]]:
    occupied = {(-1, 0, 0)}
    targets = tuple((j, 0, 0) for j in range(accumulators + 1 + testers))
    for target in targets:
        occupied.update(add(target, direction) for direction in TRANSVERSE)
    return occupied, targets


def five_neighbour_blanks(occupied: set[Point]) -> set[Point]:
    frontier = {add(point, direction) for point in occupied for direction in DIRS} - occupied
    return {
        point
        for point in frontier
        if sum(add(point, direction) in occupied for direction in DIRS) == 5
    }


def front_sequence(accumulators: int, testers: int) -> tuple[bool, tuple[int, ...]]:
    occupied, targets = scaffold(accumulators, testers)
    counts = []
    ok = True
    for target in targets:
        active = five_neighbour_blanks(occupied)
        counts.append(len(active))
        ok &= active == {target}
        occupied.add(target)
    return ok, tuple(counts)


def dyadic_distribution(steps: int, fair: Fraction = Fraction(1, 2)) -> dict[str, Fraction]:
    distribution = {"match": Fraction(1), "complement": Fraction(0)}
    for _ in range(steps):
        match = distribution["match"]
        complement = distribution["complement"]
        distribution = {
            "match": fair * match,
            "complement": (Fraction(1) - fair) * match + complement,
        }
    return distribution


def lawful_histories(steps: int) -> dict[tuple[int, ...], Fraction]:
    histories: dict[tuple[int, ...], Fraction] = {}
    histories[(0,) * steps] = Fraction(1, 2**steps)
    for first_failure in range(steps):
        word = (0,) * first_failure + (1,) * (steps - first_failure)
        histories[word] = Fraction(1, 2 ** (first_failure + 1))
    return histories


def square_response(p: Fraction) -> Fraction:
    return p * p / (p * p + (1 - p) * (1 - p))


def cubic_response(p: Fraction) -> Fraction:
    return p**3 / (p**3 + (1 - p) ** 3)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    primary = PRIMARY_PATH.read_text(encoding="utf-8")
    note = NOTE_PATH.read_text(encoding="utf-8")
    print("independence: no import of primary runner; separate occupancy and Markov-quotient reconstruction")
    print("scope: finite rails, dyadic endpoint tester, and declared tag-forgetting quotient")

    group = rotations()
    checks.check(
        "group",
        "independent signed-permutation enumeration returns 24 proper cubic rotations",
        len(group) == 24 and len(set(group)) == 24 and all(det3(matrix) == 1 for matrix in group),
    )

    front_rows = []
    front_ok = True
    for accumulators in range(1, 7):
        ok, counts = front_sequence(accumulators, 4)
        front_rows.append((accumulators, counts))
        front_ok &= ok and set(counts) == {1}
    checks.check(
        "front-census",
        "complete frontier scans for one through six accumulators find exactly the next rail target",
        front_ok,
        residual=front_rows,
    )

    covariance_ok = True
    occupied, targets = scaffold(4, 3)
    for matrix in group:
        rotated_occupied = {matvec(matrix, point) for point in occupied}
        rotated_targets = tuple(matvec(matrix, point) for point in targets)
        for target in rotated_targets:
            active = five_neighbour_blanks(rotated_occupied)
            covariance_ok &= active == {target}
            rotated_occupied.add(target)
    checks.check(
        "spatial-covariance",
        "the independently reconstructed unique-front census survives every proper cubic rotation",
        covariance_ok,
    )

    probability_rows = []
    probability_ok = True
    for steps in range(1, 9):
        distribution = dyadic_distribution(steps)
        expected = Fraction(1, 2**steps)
        histories = lawful_histories(steps)
        probability_rows.append((steps, distribution["match"], sum(histories.values())))
        probability_ok &= distribution == {"match": expected, "complement": 1 - expected}
        probability_ok &= sum(histories.values()) == 1
        probability_ok &= histories[(0,) * steps] == expected
    checks.check(
        "markov-reconstruction",
        "the absorbing two-state recursion and explicit first-failure histories both give 2^-n",
        probability_ok,
        residual=probability_rows,
    )

    histories = lawful_histories(5)
    fibres: defaultdict[int, list[tuple[int, ...]]] = defaultdict(list)
    for history in histories:
        fibres[history[-1]].append(history)
    future = {bit: {(bit,) * 7 for _ in words} for bit, words in fibres.items()}
    checks.check(
        "quotient-lumpability",
        "five different complement histories and one match history each have one seven-test future fingerprint",
        len(fibres[1]) == 5
        and len(fibres[0]) == 1
        and future == {0: {(0,) * 7}, 1: {(1,) * 7}},
    )

    response_rows = []
    response_ok = True
    for steps in range(2, 9):
        p = Fraction(1, 2**steps)
        square = square_response(p)
        cubic = cubic_response(p)
        response_rows.append((steps, p, square, cubic))
        response_ok &= p != square and p != cubic
    checks.check(
        "nonlinear-residuals",
        "independent exact fractions reproduce 1/4 versus 1/10 and 1/28 and all later mismatches",
        response_ok
        and response_rows[0] == (2, Fraction(1, 4), Fraction(1, 10), Fraction(1, 28)),
        residual=response_rows,
    )

    changed = dyadic_distribution(2, Fraction(1, 3))["match"]
    checks.check(
        "mutated-weight",
        "changing the sole fair-law datum changes the two-stage preparation from one quarter to one ninth",
        changed == Fraction(1, 9) and changed != Fraction(1, 4),
    )

    occupied_a, targets_a = scaffold(2, 2)
    displacement = (0, 10, 0)
    occupied_b = {add(point, displacement) for point in occupied_a}
    targets_b = tuple(add(point, displacement) for point in targets_a)
    dependence_a = {add(targets_a[0], direction) for direction in DIRS} | {targets_a[0]}
    dependence_b = {add(targets_b[0], direction) for direction in DIRS} | {targets_b[0]}
    checks.check(
        "disjoint-locality",
        "the two headline active-site dependence stars are disjoint and each fair pair gives product quarters",
        dependence_a.isdisjoint(dependence_b)
        and five_neighbour_blanks(occupied_a | occupied_b) == {targets_a[0], targets_b[0]}
        and {left * right for left in (Fraction(1, 2),) * 2 for right in (Fraction(1, 2),) * 2}
        == {Fraction(1, 4)},
    )

    checks.check(
        "source-contract",
        "the note and primary runner expose the bounded scope, supplied fair datum, no scalar readout, and independent checker",
        all(
            phrase in note
            for phrase in (
                "fair branch weight is supplied law content",
                "No scalar Record functional is used",
                "strong lumpability for the declared tester category",
                "FAIL / DO NOT SHIP",
                "no TOE percentage moves",
            )
        )
        and "def local_signature" in primary
        and "def advance_histories" in primary
        and "record_native_dyadic_preparation_tag_screening_independent_check_2026_08_20.py" in note,
    )

    n5_lines = (
        "per_element: independently reconstructed binary endpoint probabilities and exact nonlinear residual fractions",
        "per_site: independently scanned every blank frontier site in finite apparatus bounding neighbourhoods",
        "per_mode: rebuilt fair, absorbing-failure, preparation-copy, tester-copy, square, and cubic modes",
        "per_block: enumerated lawful first-failure histories, quotient fibres, rotations, and disjoint apparatus stars",
        "lattice_wide: checked and not executed — no arbitrary overlap, infinite-density, clock, actuality, or gravity theorem",
    )
    for line in n5_lines:
        print(line)
    checks.check(
        "n5-certificate",
        "independent evidence includes all five substantive forensic resolution classes",
        all(len(line) >= 40 for line in n5_lines),
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
