#!/usr/bin/env python3
"""Orthogonal swapped crosses on the chiral pair lie off twenty-four kernels."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_ORTHOGONAL_SWAPPED_CROSS_OUTSIDE_TWENTY_FOUR_KERNELS_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md']

KAPPA = Fraction(1, 2)
HEIGHTS = (1, 2, 3)
KINDS = ("chi", "ts", "prod")
WEIGHTS = (-1, -1, 1, 1)
EXPECTED = (
    (1, 1, 1, 0, 1, 0, 0, -1, 0),
    (-1, -1, 1, 0, -1, 0, 0, 0, -1),
    (-1, -1, 1, 0, 1, 0, 0, 0, 1),
    (1, 1, 1, 0, -1, 0, 0, -1, 0),
)


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


def quarter(point: tuple[int, int, int]) -> tuple[int, int, int]:
    x_coord, y_coord, z_coord = point
    return (-y_coord, x_coord, z_coord)


def half_turn_x(point: tuple[int, int, int]) -> tuple[int, int, int]:
    x_coord, y_coord, z_coord = point
    return (x_coord, -y_coord, -z_coord)


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


def seed_parallel(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if x_coord * y_prime - y_coord * x_prime != 0:
        return 0
    raw = x_coord * x_prime + y_coord * y_prime
    if raw == 0:
        return 0
    return -1 if raw > 0 else 1


def seed_oblique(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if abs(x_coord) != abs(x_prime) or abs(y_coord) != abs(y_prime):
        return 0
    if x_coord * y_prime - y_coord * x_prime == 0:
        return 0
    raw = x_coord * x_prime + y_coord * y_prime
    if raw == 0:
        return 0
    return -1 if raw > 0 else 1


def seed_swapped(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if abs(x_coord) != abs(y_prime) or abs(y_coord) != abs(x_prime):
        return 0
    raw = x_coord * x_prime + y_coord * y_prime
    if raw == 0:
        return 0
    return -1 if raw > 0 else 1


def seed_orthogonal(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if abs(x_coord) != abs(y_prime) or abs(y_coord) != abs(x_prime):
        return 0
    if x_coord * x_prime + y_coord * y_prime != 0:
        return 0
    raw = x_coord * y_prime - y_coord * x_prime
    if raw == 0:
        return 0
    return 1 if raw > 0 else -1


def rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    width = len(rows[0])
    matrix = [list(row) for row in rows]
    pivot_column = 0
    found = 0
    for row_index in range(len(matrix)):
        if pivot_column >= width:
            break
        pivot = None
        while pivot_column < width:
            pivot = next(
                (probe for probe in range(row_index, len(matrix)) if matrix[probe][pivot_column] != 0),
                None,
            )
            if pivot is not None:
                break
            pivot_column += 1
        if pivot is None:
            break
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        scale = matrix[row_index][pivot_column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][pivot_column] == 0:
                continue
            factor = matrix[other][pivot_column]
            matrix[other] = [
                matrix[other][column] - factor * matrix[row_index][column] for column in range(width)
            ]
        found += 1
        pivot_column += 1
    return found


def witness_bonds(height: int) -> list[tuple[tuple[int, int, int], tuple[int, int, int], int]]:
    transverse = sorted(value for value in (1, 2, 3) if value != height)
    low, high = transverse
    left_neg = (-high, -low, height)
    left_pos = (-high, low, height)
    rights = (
        (-low, -high, -height),
        (-low, high, -height),
        (low, -high, -height),
        (-low, high, -height),
    )
    lefts = (left_neg, left_neg, left_neg, left_pos)
    return [
        (left, right, weight) for left, right, weight in zip(lefts, rights, WEIGHTS)
    ]


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
    frames = {
        direction: [matrix for matrix in group if apply(matrix, up) == direction] for direction in axis_steps
    }

    def cap_sign(kind: str, height: int, direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
        if dot(point, direction) != height:
            return 0
        axis = next(index for index, coordinate in enumerate(direction) if coordinate)
        transverse = [point[index] for index in range(3) if index != axis]
        transverse_sign = 1 if transverse[0] * transverse[1] > 0 else -1
        orbit_sign = chirality[point]
        if kind == "chi":
            return orbit_sign
        if kind == "ts":
            return transverse_sign
        return orbit_sign * transverse_sign

    def cap_kernel(
        kind: str,
        height: int,
        direction: tuple[int, int, int],
        left: tuple[int, int, int],
        right: tuple[int, int, int],
    ) -> int:
        return cap_sign(kind, height, direction, left) * cap_sign(kind, height, negate(direction), right)

    def transported(seed, height: int, direction: tuple[int, int, int], left, right) -> int:
        inverse = transpose(frames[direction][0])
        return seed(height, apply(inverse, left), apply(inverse, right))

    def cross(height, direction, left, right, swapped: bool) -> int:
        return transported(lambda h, a, b: seed_cross(h, a, b, swapped), height, direction, left, right)

    def parallel(height, direction, left, right) -> int:
        return transported(seed_parallel, height, direction, left, right)

    def oblique(height, direction, left, right) -> int:
        return transported(seed_oblique, height, direction, left, right)

    def swapped_dot(height, direction, left, right) -> int:
        return transported(seed_swapped, height, direction, left, right)

    def orthogonal(height, direction, left, right) -> int:
        return transported(seed_orthogonal, height, direction, left, right)

    frame_invariant = all(
        len(
            {
                seed_orthogonal(height, apply(transpose(matrix), left), apply(transpose(matrix), right))
                for matrix in frames[direction]
            }
        )
        == 1
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
    )
    soldered = all(
        orthogonal(height, apply(matrix, direction), apply(matrix, left), apply(matrix, right))
        == orthogonal(height, direction, left, right)
        for matrix in group
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
    )
    checks.check(
        "each orthogonal swapped cross is frame-invariant and soldered",
        frame_invariant and soldered and all(len(frames[direction]) == 4 for direction in axis_steps),
    )
    bond_symmetric = all(
        orthogonal(height, direction, left, right) == orthogonal(height, negate(direction), right, left)
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
    )
    checks.check("each orthogonal swapped cross is bond-symmetric", bond_symmetric)
    one_live = all(
        sum(
            1
            for direction in axis_steps
            if any(orthogonal(height, direction, left, right) for right in records)
        )
        <= 1
        for left in records
        for height in HEIGHTS
    )
    left_slice = all(
        sum(orthogonal(height, direction, left, right) for left in records) == 0
        for direction in axis_steps
        for right in records
        for height in HEIGHTS
    )
    not_zero = all(
        any(
            orthogonal(height, direction, left, right)
            for direction in axis_steps
            for left in records
            for right in records
        )
        for height in HEIGHTS
    )
    checks.check(
        "every left slice sums to 0",
        one_live and left_slice and not_zero,
    )
    kernel_values = {
        orthogonal(height, direction, left, right)
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
    }
    factor_values = {1 + KAPPA * value for value in kernel_values}
    on_support = all(
        cross(height, direction, left, right, True) == orthogonal(height, direction, left, right)
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
        if orthogonal(height, direction, left, right) != 0
    )
    disjoint = all(
        orthogonal(height, direction, left, right) * parallel(height, direction, left, right) == 0
        and orthogonal(height, direction, left, right) * oblique(height, direction, left, right) == 0
        and orthogonal(height, direction, left, right) * swapped_dot(height, direction, left, right) == 0
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
    )
    checks.check(
        "at coefficient 1/2 each orthogonal swapped cross takes values 1/2, 1, and 3/2",
        kernel_values == {-1, 0, 1}
        and factor_values == {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
        and on_support
        and disjoint,
    )
    far_end = all(
        sum(1 + KAPPA * orthogonal(height, direction, left, right) for right in records) == 48
        for direction in axis_steps
        for left in records
        for height in HEIGHTS
    )
    checks.check("every far-end sum equals 48", far_end)

    def twenty_four(left: tuple[int, int, int], right: tuple[int, int, int]) -> list[int]:
        values = []
        for height in HEIGHTS:
            for kind in KINDS:
                values.append(cap_kernel(kind, height, up, left, right))
            values.append(cross(height, up, left, right, False))
            values.append(cross(height, up, left, right, True))
            values.append(parallel(height, up, left, right))
            values.append(oblique(height, up, left, right))
            values.append(swapped_dot(height, up, left, right))
        return values

    separated = True
    for height in HEIGHTS:
        bonds = witness_bonds(height)
        weighted = [0] * 24
        new_sum = 0
        other_sum = 0
        rows_ok = True
        for (left, right, weight), expected in zip(bonds, EXPECTED):
            row = twenty_four(left, right)
            new_value = orthogonal(height, up, left, right)
            active = row[8 * (height - 1) : 8 * height]
            rows_ok = rows_ok and tuple(active) + (new_value,) == expected
            rows_ok = rows_ok and all(value == 0 for value in row[: 8 * (height - 1)])
            rows_ok = rows_ok and all(value == 0 for value in row[8 * height :])
            for index, value in enumerate(row):
                weighted[index] += weight * value
            new_sum += weight * new_value
            for other in HEIGHTS:
                if other != height:
                    other_sum += weight * orthogonal(other, up, left, right)
        separated = (
            separated
            and rows_ok
            and all(value == 0 for value in weighted)
            and new_sum == 2
            and other_sum == 0
            and all(point in records for left, right, _weight in bonds for point in (left, right))
        )
    idle = (1, 2, 3)
    idle_clear = all(value == 0 for value in twenty_four(idle, idle)) and all(
        orthogonal(height, up, idle, idle) == 0 for height in HEIGHTS
    )
    if not separated or not idle_clear:
        print(separated, idle_clear)
    checks.check(
        "three height quadruples separate each orthogonal swapped cross from the twenty-four kernels",
        separated and idle_clear,
    )

    def opposite_space(height: int) -> bool:
        lefts = [point for point in records if point[2] == height]
        rights = [point for point in records if point[2] == -height]
        index: dict[tuple[tuple[int, int, int], tuple[int, int, int]], int] = {}
        classes: list[list[tuple[tuple[int, int, int], tuple[int, int, int]]]] = []
        for left in lefts:
            for right in rights:
                if (left, right) in index:
                    continue
                members = []
                current = (left, right)
                for _ in range(4):
                    members.append(current)
                    current = (quarter(current[0]), quarter(current[1]))
                class_id = len(classes)
                classes.append(members)
                for member in members:
                    index[member] = class_id
        width = len(classes)
        equations = []
        for left in lefts:
            for right in rights:
                image = (half_turn_x(right), half_turn_x(left))
                row = [Fraction(0)] * width
                row[index[(left, right)]] += 1
                row[index[image]] -= 1
                equations.append(row)
        for right in rights:
            row = [Fraction(0)] * width
            for left in lefts:
                row[index[(left, right)]] += 1
            equations.append(row)

        def coordinate(evaluator) -> list[Fraction] | None:
            values: list[Fraction | None] = [None] * width
            for left in lefts:
                for right in rights:
                    value = Fraction(evaluator(left, right))
                    class_id = index[(left, right)]
                    if values[class_id] is None:
                        values[class_id] = value
                    elif values[class_id] != value:
                        return None
            return [value if value is not None else Fraction(0) for value in values]

        known = [
            coordinate(lambda left, right, kind=kind: cap_kernel(kind, height, up, left, right))
            for kind in KINDS
        ] + [
            coordinate(lambda left, right, swapped=swapped: cross(height, up, left, right, swapped))
            for swapped in (False, True)
        ] + [
            coordinate(lambda left, right: parallel(height, up, left, right)),
            coordinate(lambda left, right: oblique(height, up, left, right)),
            coordinate(lambda left, right: swapped_dot(height, up, left, right)),
        ]
        extra = coordinate(lambda left, right: orthogonal(height, up, left, right))
        if any(vector is None for vector in known) or extra is None:
            return False
        known_vectors = [vector for vector in known if vector is not None]
        inside = all(
            all(sum(equation[column] * vector[column] for column in range(width)) == 0 for equation in equations)
            for vector in known_vectors + [extra]
        )
        return (
            width == 16
            and rank(equations) == 6
            and width - rank(equations) == 10
            and rank(known_vectors) == 8
            and rank(known_vectors + [extra]) == 9
            and inside
        )

    checks.check(
        "each opposite-height pair has the orthogonal swapped cross at rank 9",
        all(opposite_space(height) for height in HEIGHTS),
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
