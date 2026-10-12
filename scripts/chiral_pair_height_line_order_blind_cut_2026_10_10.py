#!/usr/bin/env python3
"""A height-linear line in the 48-point normalised bond space fails one moment."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_HEIGHT_LINE_ORDER_BLIND_CUT_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md']


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def det3(matrix: list[list[int]]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper() -> list[list[list[int]]]:
    found = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for src, dst in enumerate(perm):
                matrix[dst][src] = signs[src]
            if det3(matrix) == 1:
                found.append(matrix)
    return found


def apply(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def directions() -> list[tuple[int, int, int]]:
    found = []
    for axis in range(3):
        for sign in (-1, 1):
            vector = [0, 0, 0]
            vector[axis] = sign
            found.append(tuple(vector))
    return found


def negate(direction: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(-coordinate for coordinate in direction)


def dot(point: tuple[int, ...], direction: tuple[int, int, int]) -> int:
    return sum(left * right for left, right in zip(point, direction))


def alphabet() -> list[tuple[int, int, int]]:
    found = []
    for perm in permutations((1, 2, 3)):
        for signs in product((-1, 1), repeat=3):
            found.append(tuple(sign * value for sign, value in zip(signs, perm)))
    return sorted(set(found))


def phi(
    direction: tuple[int, int, int],
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    coeff: Fraction,
) -> Fraction:
    return Fraction(1) + coeff * dot(left, direction) * dot(right, negate(direction))


def moment(
    records: list[tuple[int, int, int]],
    direction: tuple[int, int, int],
    other: tuple[int, int, int],
    right: tuple[int, int, int],
    other_right: tuple[int, int, int],
    coeff: Fraction,
) -> Fraction:
    total = sum(
        (
            phi(direction, left, right, coeff)
            * phi(other, left, other_right, coeff)
            for left in records
        ),
        start=Fraction(0),
    )
    return total / len(records)


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    records = alphabet()
    orbit = {apply(matrix, (1, 2, 3)) for matrix in group}
    other = [point for point in records if point not in orbit]
    checks.check(
        "the alphabet is the chiral pair of two proper orbits",
        len(records) == 48
        and len(orbit) == 24
        and len(other) == 24
        and (2, 1, 3) in other,
    )
    axis_steps = directions()
    checks.check(
        "six axis directions",
        axis_steps == [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)],
    )

    coeff = Fraction(1, 10)
    bond_symmetric = all(
        phi(direction, left, right, coeff) == phi(negate(direction), right, left, coeff)
        for direction in axis_steps
        for left in records
        for right in records
    )
    checks.check("the height-linear factor is bond-symmetric", bond_symmetric)
    covariant = all(
        phi(apply(matrix, direction), apply(matrix, left), apply(matrix, right), coeff)
        == phi(direction, left, right, coeff)
        for matrix in group
        for direction in axis_steps
        for left in records
        for right in records
    )
    checks.check("the height-linear factor is soldered under proper rotations", covariant)

    far_end = all(
        sum(phi(direction, left, right, coeff) for right in records) == 48
        for direction in axis_steps
        for left in records
    )
    checks.check("every far-end sum equals 48", far_end)

    square_moment = Fraction(sum(point[2] * point[2] for point in records), len(records))
    mean_height = Fraction(sum(point[2] for point in records), len(records))
    checks.check(
        "one coordinate has mean 0 and second moment 14/3",
        mean_height == 0 and square_moment == Fraction(14, 3),
    )

    up = (0, 0, 1)
    down = (0, 0, -1)
    identity_holds = all(
        moment(records, up, down, left, right, coeff)
        == 1 + square_moment * coeff * coeff * left[2] * right[2]
        for left in records
        for right in records
    )
    checks.check(
        "every opposite-direction moment equals 1 plus (14/3) c^2 times the two heights",
        identity_holds,
    )
    seed = (1, 2, 3)
    witness = moment(records, up, down, seed, seed, coeff)
    checks.check(
        "at coefficient 1/10 the opposite moment on (1, 2, 3) is 71/50",
        witness == Fraction(71, 50),
    )
    values = [
        phi(direction, left, right, coeff)
        for direction in axis_steps
        for left in records
        for right in records
    ]
    checks.check(
        "that factor is strictly positive and not constant",
        all(value > 0 for value in values) and len(set(values)) > 1,
    )

    side = (1, 0, 0)
    perpendicular = all(
        moment(records, side, up, left, right, coeff) == 1
        for left in records
        for right in records
    )
    checks.check("every perpendicular moment on e_x and e_z equals 1", perpendicular)
    checks.check(
        "at coefficient 0 the opposite moment equals 1",
        moment(records, up, down, seed, seed, Fraction(0)) == 1,
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)
    print("per_element: checked exact arithmetic on the explicitly enumerated finite record and bond data above; no continuum or empirical input is tested.")
    print("per_site: checked and not executed — this runner contains no evolving site ensemble; finite centre-record sums are the local mathematical object.")
    print("per_mode: checked and not executed — no momentum spectrum, physical particle mode or dispersion relation is computed in this finite alphabet runner.")
    print("per_block: checked the finite algebraic blocks and coefficient cases described by the named predicates; unlisted support sectors are outside this execution.")
    print("lattice_wide: checked and not executed — no whole-lattice dynamics is simulated; any all-window statement depends on the source proof and its cited converse.")



if __name__ == "__main__":
    main()
