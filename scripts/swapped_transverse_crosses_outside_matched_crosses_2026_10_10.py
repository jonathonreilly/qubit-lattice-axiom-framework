#!/usr/bin/env python3
"""Swapped-absolute transverse crosses lie outside the matched crosses."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/SWAPPED_TRANSVERSE_CROSSES_OUTSIDE_THE_MATCHED_CROSSES_BOUNDED_THEOREM_NOTE_2026-10-10.md']


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


def cap(point: tuple[int, ...], direction: tuple[int, int, int], level: int) -> int:
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    if point[axis] != direction[axis] * level:
        return 0
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def matched_raw(height: int, left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if left[2] != -height or right[2] != height:
        return 0
    if abs(left[0]) != abs(right[0]) or abs(left[1]) != abs(right[1]):
        return 0
    cross = left[0] * right[1] - left[1] * right[0]
    if cross == 0:
        return 0
    return 1 if cross > 0 else -1


def swapped_raw(height: int, left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if left[2] != -height or right[2] != height:
        return 0
    if abs(left[0]) != abs(right[1]) or abs(left[1]) != abs(right[0]):
        return 0
    cross = left[0] * right[1] - left[1] * right[0]
    if cross == 0:
        return 0
    return -1 if cross > 0 else 1


def rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank_now = 0
    columns = len(matrix[0]) if matrix else 0
    for col in range(columns):
        pivot = next((i for i in range(rank_now, len(matrix)) if matrix[i][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for i in range(len(matrix)):
            if i != rank_now and matrix[i][col] != 0:
                factor = matrix[i][col]
                matrix[i] = [
                    matrix[i][j] - factor * matrix[rank_now][j] for j in range(columns)
                ]
        rank_now += 1
    return rank_now


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
        direction: [matrix for matrix in group if apply(matrix, upward) == direction]
        for direction in axis_steps
    }
    checks.check(
        "each direction has four carriers",
        all(len(items) == 4 for items in carriers.values()),
    )

    def transported(raw, height, direction, left, right, matrix) -> int:
        inverse = transpose(matrix)
        return raw(height, apply(inverse, left), apply(inverse, right))

    def kernel(raw, height, direction, left, right) -> int:
        return transported(raw, height, direction, left, right, carriers[direction][0])

    well_defined = True
    for height in (1, 2, 3):
        for direction, matrices in carriers.items():
            for left in orbit:
                for right in orbit:
                    values = {
                        transported(swapped_raw, height, direction, left, right, matrix)
                        for matrix in matrices
                    }
                    if len(values) != 1:
                        well_defined = False
    checks.check("soldered extension of the swapped kernels is well defined", well_defined)

    symmetric = all(
        kernel(swapped_raw, height, direction, left, right)
        == kernel(swapped_raw, height, negate(direction), right, left)
        for height in (1, 2, 3)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    )
    checks.check("the swapped kernels are bond-symmetric", symmetric)

    nonzero_swap = True
    for height in (1, 2, 3):
        for left in orbit:
            for right in orbit:
                if left[2] != -height or right[2] != height:
                    continue
                if abs(left[0]) != abs(right[1]) or abs(left[1]) != abs(right[0]):
                    continue
                if left[0] * right[1] - left[1] * right[0] == 0:
                    nonzero_swap = False
    checks.check("a swapped transverse pair has nonzero cross", nonzero_swap)

    values = {
        kernel(swapped_raw, height, direction, left, right)
        for height in (1, 2, 3)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("swapped kernel values lie in {-1, 0, 1}", values == {-1, 0, 1})

    one_live = True
    for height in (1, 2, 3):
        for point in orbit:
            live = [
                direction
                for direction in axis_steps
                if any(
                    kernel(swapped_raw, height, direction, point, right) for right in orbit
                )
            ]
            if len(live) != 1:
                one_live = False
    checks.check("each record activates one direction", one_live)

    slice_mean = all(
        sum(kernel(swapped_raw, height, direction, point, right) for point in orbit) == 0
        for height in (1, 2, 3)
        for direction in axis_steps
        for right in orbit
    )
    checks.check("every swapped slice has sum 0", slice_mean)

    swapped_witnesses = {
        1: ((-3, -2, -1), (-2, -3, 1)),
        2: ((-3, 1, -2), (1, -3, 2)),
        3: ((-2, -1, -3), (-1, -2, 3)),
    }
    matched_witnesses = {
        1: ((-3, -2, -1), (-3, 2, 1)),
        2: ((-3, 1, -2), (3, 1, 2)),
        3: ((-2, -1, -3), (-2, 1, 3)),
    }
    for height, (left, right) in swapped_witnesses.items():
        checks.check(
            f"the swapped height-{height} witness bond has value -1",
            left in orbit
            and right in orbit
            and kernel(swapped_raw, height, upward, left, right) == -1,
        )
    matched_pin = all(
        left in orbit
        and right in orbit
        and kernel(matched_raw, height, upward, left, right) == -1
        for height, (left, right) in matched_witnesses.items()
    )
    checks.check("the matched comparison reproduces three witness values -1", matched_pin)

    levels = (-3, -2, -1, 1, 2, 3)

    def slice_orthogonal(height: int) -> bool:
        right = swapped_witnesses[height][1]
        slice_values = [
            kernel(swapped_raw, height, upward, point, right) for point in orbit
        ]
        cap_dots = all(
            sum(
                slice_values[index] * cap(point, upward, level)
                for index, point in enumerate(orbit)
            )
            == 0
            for level in levels
        )
        matched_dot = sum(
            slice_values[index] * kernel(matched_raw, height, upward, point, right)
            for index, point in enumerate(orbit)
        )
        return any(slice_values) and cap_dots and matched_dot == 0

    checks.check(
        "each swapped witness slice is orthogonal to the caps and its matched cross",
        all(slice_orthogonal(height) for height in (1, 2, 3)),
    )

    bonds = [
        (direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    ]

    def cross_row(raw, height: int) -> list[int]:
        return [
            kernel(raw, height, direction, left, right) for direction, left, right in bonds
        ]

    def cap_row(level: int) -> list[int]:
        return [
            cap(left, direction, level) * cap(right, negate(direction), level)
            for direction, left, right in bonds
        ]

    prior = [cap_row(level) for level in levels] + [
        cross_row(matched_raw, height) for height in (1, 2, 3)
    ]
    outside = (
        rank(prior) == 9
        and all(rank(prior + [cross_row(swapped_raw, height)]) == 10 for height in (1, 2, 3))
    )
    checks.check(
        "each swapped kernel lies outside the six caps and the three matched crosses",
        outside,
    )
    twelve = prior + [cross_row(swapped_raw, height) for height in (1, 2, 3)]
    checks.check("the twelve kernels are linearly independent", rank(twelve) == 12)

    positive = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    seen_values = {
        1 + Fraction(1, 2) * kernel(swapped_raw, height, direction, left, right)
        for height in (1, 2, 3)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("half-parameter factors stay positive", seen_values == positive)

    same_height = {
        kernel(matched_raw, 3, direction, left, right)
        + kernel(swapped_raw, 3, direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    same_live = True
    for point in orbit:
        live = [
            direction
            for direction in axis_steps
            if any(
                kernel(matched_raw, 3, direction, point, right)
                or kernel(swapped_raw, 3, direction, point, right)
                for right in orbit
            )
        ]
        if len(live) != 1:
            same_live = False
    same_slices = all(
        sum(
            kernel(matched_raw, 3, direction, point, right)
            + kernel(swapped_raw, 3, direction, point, right)
            for point in orbit
        )
        == 0
        for direction in axis_steps
        for right in orbit
    )
    checks.check(
        "matched plus swapped at height 3 stays one-hot with slice sum 0",
        same_height == {-1, 0, 1} and same_live and same_slices,
    )

    def mixed(direction, left, right) -> int:
        return kernel(swapped_raw, 1, direction, left, right) + kernel(
            swapped_raw, 2, direction, left, right
        )

    moment = Fraction(
        sum(
            (1 + mixed((-1, 0, 0), point, (-2, -3, 1)))
            * (1 + mixed((0, -1, 0), point, (-3, -1, 2)))
            for point in orbit
        ),
        len(orbit),
    )
    checks.check(
        "the sum across heights 1 and 2 has two-neighbour moment 23/24",
        (-2, -3, 1) in orbit and (-3, -1, 2) in orbit and moment == Fraction(23, 24),
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
