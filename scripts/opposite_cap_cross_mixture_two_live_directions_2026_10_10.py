#!/usr/bin/env python3
"""A positive cap plus the opposite matched cross has two live directions."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/OPPOSITE_CAP_CROSS_MIXTURE_TWO_LIVE_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md']


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


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [[matrix[j][i] for j in range(3)] for i in range(3)]


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


def dot(point, direction) -> int:
    return sum(left * right for left, right in zip(point, direction))


def cap(point, direction, level: int) -> int:
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    if point[axis] != direction[axis] * level:
        return 0
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def sign_of(value: int) -> int:
    if value == 0:
        return 0
    return 1 if value > 0 else -1


def matched_raw(orientation: int, height: int, left, right) -> int:
    if left[2] != orientation * height or right[2] != -orientation * height:
        return 0
    if abs(left[0]) != abs(right[0]) or abs(left[1]) != abs(right[1]):
        return 0
    return sign_of(left[0] * right[1] - left[1] * right[0])


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6)
    upward = (0, 0, 1)
    carriers = {
        direction: next(matrix for matrix in group if apply(matrix, upward) == direction)
        for direction in axis_steps
    }
    checks.check("each direction has a carrier", len(carriers) == 6)

    def matched(orientation: int, height: int, direction, left, right) -> int:
        inverse = transpose(carriers[direction])
        return matched_raw(orientation, height, apply(inverse, left), apply(inverse, right))

    def cap_kernel(level: int, direction, left, right) -> int:
        return cap(left, direction, level) * cap(right, negate(direction), level)

    def mixed(direction, left, right) -> int:
        return cap_kernel(3, direction, left, right) + matched(-1, 3, direction, left, right)

    symmetric = all(
        mixed(direction, left, right) == mixed(negate(direction), right, left)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    )
    checks.check("the mixture is bond-symmetric", symmetric)

    values = {
        mixed(direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("mixture values lie in {-1, 0, 1}", values == {-1, 0, 1})

    opposite_live = True
    both_used = False
    for point in orbit:
        live = [
            direction
            for direction in axis_steps
            if any(mixed(direction, point, right) for right in orbit)
        ]
        if len(live) != 2 or negate(live[0]) != live[1]:
            opposite_live = False
        for first in axis_steps:
            for second in axis_steps:
                if second == negate(first) and any(
                    mixed(first, point, right) and mixed(second, point, other)
                    for right in orbit
                    for other in orbit
                ):
                    both_used = True
    checks.check("every record activates two opposite directions", opposite_live)
    checks.check("some record is nonzero in both opposite directions", both_used)

    seed = (1, 2, 3)
    seed_live = [
        direction for direction in axis_steps if any(mixed(direction, seed, right) for right in orbit)
    ]
    checks.check(
        "the seed (1, 2, 3) is live in e_z and -e_z",
        seed in orbit and set(seed_live) == {upward, negate(upward)},
    )

    slice_mean = all(
        sum(mixed(direction, point, right) for point in orbit) == 0
        for direction in axis_steps
        for right in orbit
    )
    checks.check("every slice has sum 0", slice_mean)

    moments = {
        Fraction(
            sum(
                (1 + mixed(direction, point, right))
                * (1 + mixed(negate(direction), point, other))
                for point in orbit
            ),
            len(orbit),
        )
        for direction in axis_steps
        for right in orbit
        for other in orbit
    }
    checks.check("every opposite-direction product has mean 1", moments == {Fraction(1)})

    positive = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    seen_values = {
        1 + Fraction(1, 2) * mixed(direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("half-parameter factors stay positive", seen_values == positive)

    cap_moment = Fraction(
        sum(
            (1 + cap_kernel(3, (1, 0, 0), point, (-3, -2, -1)))
            * (1 + cap_kernel(-3, (-1, 0, 0), point, (-3, -2, -1)))
            for point in orbit
        ),
        len(orbit),
    )
    checks.check(
        "the two level-3 cap lines have moment 7/6",
        (-3, -2, -1) in orbit and cap_moment == Fraction(7, 6),
    )

    disjoint = all(
        cap_kernel(3, direction, left, right) == 0
        or matched(-1, 3, direction, left, right) == 0
        for direction in axis_steps
        for left in orbit
        for right in orbit
    )
    checks.check("the cap and the opposite cross have disjoint bonds", disjoint)

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
