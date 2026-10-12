#!/usr/bin/env python3
"""Lower-height crosses on the chiral pair lie off the five height-3 kernels."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_LOWER_HEIGHT_CROSSES_OUTSIDE_FIVE_KERNELS_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md']

KAPPA = Fraction(1, 2)
HEIGHTS = (1, 2)


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


def dot(point: tuple[int, ...], direction: tuple[int, int, int]) -> int:
    return sum(left * right for left, right in zip(point, direction))


def alphabet() -> list[tuple[int, int, int]]:
    found = []
    for perm in permutations((1, 2, 3)):
        for signs in product((-1, 1), repeat=3):
            found.append(tuple(sign * value for sign, value in zip(signs, perm)))
    return sorted(set(found))


def transverse_sign(direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
    if dot(point, direction) != 3:
        return 0
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def seed_cross(
    height: int,
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    swapped: bool,
) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if swapped:
        matched_abs = abs(x_coord) == abs(y_prime) and abs(y_coord) == abs(x_prime)
    else:
        matched_abs = abs(x_coord) == abs(x_prime) and abs(y_coord) == abs(y_prime)
    if not matched_abs:
        return 0
    raw = x_coord * y_prime - y_coord * x_prime
    if raw == 0:
        return 0
    return 1 if raw > 0 else -1


def determinant(rows: list[list[int]]) -> Fraction:
    size = len(rows)
    matrix = [list(map(Fraction, row)) for row in rows]
    sign = Fraction(1)
    for index in range(size):
        pivot = next((row for row in range(index, size) if matrix[row][index] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != index:
            matrix[index], matrix[pivot] = matrix[pivot], matrix[index]
            sign = -sign
        for row in range(index + 1, size):
            factor = matrix[row][index] / matrix[index][index]
            matrix[row] = [
                matrix[row][column] - factor * matrix[index][column] for column in range(size)
            ]
    value = sign
    for index in range(size):
        value *= matrix[index][index]
    return value


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    records = alphabet()
    positive = {apply(matrix, (1, 2, 3)) for matrix in group}
    chirality = {point: (1 if point in positive else -1) for point in records}
    other = [point for point in records if point not in positive]
    checks.check(
        "the alphabet is the chiral pair of two proper orbits",
        len(records) == 48
        and len(positive) == 24
        and len(other) == 24
        and (2, 1, 3) in other
        and (1, 2, -3) in other,
    )
    axis_steps = directions()
    checks.check(
        "six axis directions",
        axis_steps == [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)],
    )
    up = (0, 0, 1)

    def transported(
        height: int,
        direction: tuple[int, int, int],
        left: tuple[int, int, int],
        right: tuple[int, int, int],
        swapped: bool,
        frame: list[list[int]],
    ) -> int:
        inverse = transpose(frame)
        return seed_cross(height, apply(inverse, left), apply(inverse, right), swapped)

    frames = {
        direction: [matrix for matrix in group if apply(matrix, up) == direction]
        for direction in axis_steps
    }
    frame_ok = all(len(choices) == 4 for choices in frames.values()) and all(
        transported(height, direction, left, right, swapped, choices[0])
        == transported(height, direction, left, right, swapped, choice)
        for direction, choices in frames.items()
        for choice in choices
        for left in records
        for right in records
        for height in HEIGHTS
        for swapped in (False, True)
    )
    checks.check("all four crosses are independent of the frame sending e_z to d", frame_ok)

    def cross(
        height: int,
        direction: tuple[int, int, int],
        left: tuple[int, int, int],
        right: tuple[int, int, int],
        swapped: bool,
    ) -> int:
        return transported(height, direction, left, right, swapped, frames[direction][0])

    soldered = all(
        cross(height, apply(matrix, direction), apply(matrix, left), apply(matrix, right), swapped)
        == cross(height, direction, left, right, swapped)
        for matrix in group
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
        for swapped in (False, True)
    )
    checks.check("all four crosses are soldered under proper rotations", soldered)
    bond_symmetric = all(
        cross(height, direction, left, right, swapped)
        == cross(height, negate(direction), right, left, swapped)
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
        for swapped in (False, True)
    )
    checks.check("all four crosses are bond-symmetric", bond_symmetric)

    def live_count(point: tuple[int, int, int], height: int, swapped: bool) -> int:
        return sum(
            1
            for direction in axis_steps
            if any(cross(height, direction, point, right, swapped) for right in records)
        )

    one_live = all(
        live_count(point, height, swapped) <= 1
        for point in records
        for height in HEIGHTS
        for swapped in (False, True)
    )
    left_slice = all(
        sum(cross(height, direction, left, right, swapped) for left in records) == 0
        for direction in axis_steps
        for right in records
        for height in HEIGHTS
        for swapped in (False, True)
    )
    not_zero = all(
        any(
            cross(height, direction, left, right, swapped)
            for direction in axis_steps
            for left in records
            for right in records
        )
        for height in HEIGHTS
        for swapped in (False, True)
    )
    checks.check(
        "each cross has at most one live direction and every left slice sums to 0",
        one_live and left_slice and not_zero,
    )

    kernel_values = {
        cross(height, direction, left, right, swapped)
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
        for swapped in (False, True)
    }
    factor_values = {1 + KAPPA * value for value in kernel_values}
    checks.check(
        "at coefficient 1/2 each cross takes values 1/2, 1, and 3/2",
        kernel_values == {-1, 0, 1} and factor_values == {Fraction(1, 2), Fraction(1), Fraction(3, 2)},
    )
    far_end = all(
        sum(1 + KAPPA * cross(height, direction, left, right, swapped) for right in records) == 48
        for direction in axis_steps
        for left in records
        for height in HEIGHTS
        for swapped in (False, True)
    )
    checks.check("every far-end sum equals 48", far_end)

    def cap_chirality(direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
        if dot(point, direction) != 3:
            return 0
        return chirality[point]

    def sign_product(direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
        return chirality[point] * transverse_sign(direction, point)

    def nine(
        direction: tuple[int, int, int],
        left: tuple[int, int, int],
        right: tuple[int, int, int],
    ) -> list[int]:
        return [
            cap_chirality(direction, left) * cap_chirality(negate(direction), right),
            transverse_sign(direction, left) * transverse_sign(negate(direction), right),
            sign_product(direction, left) * sign_product(negate(direction), right),
            cross(3, direction, left, right, False),
            cross(3, direction, left, right, True),
            cross(1, direction, left, right, False),
            cross(1, direction, left, right, True),
            cross(2, direction, left, right, False),
            cross(2, direction, left, right, True),
        ]

    source = (-2, -1, 3)
    partners = ((-2, -1, -3), (-2, 1, -3), (-1, -2, -3), (-1, 2, -3), (1, -2, -3))
    lower_bonds = (
        ((2, -3, 1), (2, 3, -1)),
        ((2, 3, 1), (3, 2, -1)),
        ((1, -3, 2), (1, 3, -2)),
        ((1, 3, 2), (3, 1, -2)),
    )
    expected = [
        [-1, 1, -1, 0, 0, 0, 0, 0, 0],
        [1, -1, -1, -1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0],
        [-1, -1, 1, 0, -1, 0, 0, 0, 0],
        [-1, -1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, -1],
    ]
    rows = [nine(up, source, partner) for partner in partners]
    rows.extend(nine(up, left, right) for left, right in lower_bonds)
    idle = all(value == 0 for value in nine(up, (1, 2, 3), (1, 2, 3)))
    checks.check(
        "nine bonds have determinant 8 against the five kernels",
        rows == expected and determinant(rows) == 8 and idle,
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
