#!/usr/bin/env python3
"""Every rational mixture of one opposite-height basis has product mean 1."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

AUDIT_TIMEOUT_SEC = 180

HEIGHTS = (1, 2, 3)
KERNELS = (
    "chi",
    "ts",
    "prod",
    "matched",
    "swapped",
    "parallel",
    "oblique",
    "swapped_dot",
    "orthogonal",
    "scaled",
)
UNIT_VALUES = {-1, 0, 1}
SCALED_VALUES = {-2, -1, 0, 1, 2}
WITNESS_VALUES = {
    Fraction(29, 32),
    Fraction(15, 16),
    Fraction(31, 32),
    Fraction(1),
    Fraction(33, 32),
    Fraction(17, 16),
    Fraction(19, 16),
}
WITNESS = tuple(Fraction(1, 32) for _ in KERNELS)
NONPOSITIVE = (Fraction(2),) + (Fraction(0),) * 9
INTEGER_BOX = tuple(Fraction(index) for index in range(1, 11))


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
    first, second, third = matrix
    return (
        first[0] * (second[1] * third[2] - second[2] * third[1])
        - first[1] * (second[0] * third[2] - second[2] * third[0])
        + first[2] * (second[0] * third[1] - second[1] * third[0])
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
    return tuple(sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3))


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [[matrix[row][col] for row in range(3)] for col in range(3)]


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


def seed_cross(height: int, left: tuple[int, int, int], right: tuple[int, int, int], swapped: bool) -> int:
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


def seed_scaled(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    cross = x_coord * y_prime - y_coord * x_prime
    dot_product = x_coord * x_prime + y_coord * y_prime
    if cross == 0 or dot_product == 0:
        return 0
    signed = -1 if cross * dot_product > 0 else 1
    matched = abs(x_coord) == abs(x_prime) and abs(y_coord) == abs(y_prime)
    swapped = abs(x_coord) == abs(y_prime) and abs(y_coord) == abs(x_prime)
    if matched and dot_product > 0:
        return 2 * signed
    if swapped:
        return signed
    return 0


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


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    records = alphabet()
    positive = {apply(matrix, (1, 2, 3)) for matrix in group}
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
    chirality = {point: (1 if point in positive else -1) for point in records}
    record_index = {point: index for index, point in enumerate(records)}
    direction_index = {direction: index for index, direction in enumerate(axis_steps)}
    count = len(records)

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

    def cap_kernel(kind: str, height: int, direction: tuple[int, int, int], left, right) -> int:
        return cap_sign(kind, height, direction, left) * cap_sign(kind, height, negate(direction), right)

    def transported(seed, height: int, direction: tuple[int, int, int], left, right) -> int:
        inverse = transpose(frames[direction][0])
        return seed(height, apply(inverse, left), apply(inverse, right))

    def raw_kernel(name: str, height: int, direction, left, right) -> int:
        if name == "chi":
            return cap_kernel("chi", height, direction, left, right)
        if name == "ts":
            return cap_kernel("ts", height, direction, left, right)
        if name == "prod":
            return cap_kernel("prod", height, direction, left, right)
        if name == "matched":
            return transported(lambda level, a, b: seed_cross(level, a, b, False), height, direction, left, right)
        if name == "swapped":
            return transported(lambda level, a, b: seed_cross(level, a, b, True), height, direction, left, right)
        if name == "parallel":
            return transported(seed_parallel, height, direction, left, right)
        if name == "oblique":
            return transported(seed_oblique, height, direction, left, right)
        if name == "swapped_dot":
            return transported(seed_swapped, height, direction, left, right)
        if name == "orthogonal":
            return transported(seed_orthogonal, height, direction, left, right)
        return transported(seed_scaled, height, direction, left, right)

    tables: dict[int, list[list[list[list[int]]]]] = {}
    for height in HEIGHTS:
        tables[height] = [
            [[[0 for _ in records] for _ in records] for _ in KERNELS] for _ in axis_steps
        ]
        for direction in axis_steps:
            dir_id = direction_index[direction]
            for left in records:
                if dot(left, direction) != height:
                    continue
                left_id = record_index[left]
                for right in records:
                    if dot(right, direction) != -height:
                        continue
                    right_id = record_index[right]
                    for kernel_id, name in enumerate(KERNELS):
                        tables[height][dir_id][kernel_id][left_id][right_id] = raw_kernel(
                            name, height, direction, left, right
                        )

    def entry(height: int, direction, kernel_id: int, left, right) -> int:
        return tables[height][direction_index[direction]][kernel_id][record_index[left]][record_index[right]]

    value_sets = {name: set() for name in KERNELS}
    bond_symmetric = True
    column_zero = True
    soldered = True
    one_live = True
    some_live = False
    overlap = False
    split = False
    overlap_bond: tuple | None = None
    split_bond: tuple | None = None
    for height in HEIGHTS:
        for direction in axis_steps:
            for left in records:
                for right in records:
                    values = [
                        entry(height, direction, kernel_id, left, right) for kernel_id in range(len(KERNELS))
                    ]
                    for name, value in zip(KERNELS, values):
                        value_sets[name].add(value)
                    if any(value != 0 for value in values):
                        some_live = True
                    if values[0] != 0 and values[9] == 0:
                        split = True
                        if split_bond is None:
                            split_bond = (height, direction, left, right, values[0], values[9])
                    if values[0] != 0 and values[9] != 0:
                        overlap = True
                        if overlap_bond is None:
                            overlap_bond = (height, direction, left, right, values[0], values[9])
        for left in records:
            live = 0
            for direction in axis_steps:
                if any(
                    entry(height, direction, kernel_id, left, right)
                    for kernel_id in range(len(KERNELS))
                    for right in records
                ):
                    live += 1
            if live > 1:
                one_live = False
        for direction in axis_steps:
            opposite = negate(direction)
            for kernel_id in range(len(KERNELS)):
                for left in records:
                    for right in records:
                        if entry(height, direction, kernel_id, left, right) != entry(
                            height, opposite, kernel_id, right, left
                        ):
                            bond_symmetric = False
                for right in records:
                    if sum(entry(height, direction, kernel_id, left, right) for left in records) != 0:
                        column_zero = False
    for matrix in group:
        for direction in axis_steps:
            image = apply(matrix, direction)
            for left_id, left in enumerate(records):
                image_left = record_index[apply(matrix, left)]
                for right_id, right in enumerate(records):
                    image_right = record_index[apply(matrix, right)]
                    for height in HEIGHTS:
                        source = tables[height][direction_index[direction]]
                        rotated = tables[height][direction_index[image]]
                        for kernel_id in range(len(KERNELS)):
                            if rotated[kernel_id][image_left][image_right] != source[kernel_id][left_id][right_id]:
                                soldered = False
    checks.check(
        "each basis kernel is soldered, bond-symmetric, and slice-zero",
        soldered and bond_symmetric and column_zero and one_live and some_live,
    )
    checks.check(
        "the ten kernels take the stated values and overlap on one bond",
        all(value_sets[name] == UNIT_VALUES for name in KERNELS[:-1])
        and value_sets["scaled"] == SCALED_VALUES
        and overlap
        and split
        and overlap_bond is not None
        and split_bond is not None,
    )

    def moments(
        coefficients: tuple[Fraction, ...],
    ) -> tuple[bool, bool, set[Fraction], Fraction, Fraction]:
        denominator = coefficients[0].denominator
        for coefficient in coefficients[1:]:
            denominator = max(denominator, coefficient.denominator)
        scaled_coefficients = [int(coefficient * denominator) for coefficient in coefficients]
        values: set[Fraction] = set()
        one_ok = True
        two_ok = True
        sample_one = Fraction(0)
        sample_two = Fraction(0)
        sample_direction = direction_index[axis_steps[-1]]
        sample_right = record_index[(1, 2, -3)]
        second_direction = direction_index[axis_steps[0]]
        second_right = record_index[(2, 1, 3)]
        numerator_target = count * denominator
        pair_target = count * denominator * denominator
        for height in HEIGHTS:
            planes = []
            for direction in axis_steps:
                plane = [[denominator for _ in range(count)] for _ in range(count)]
                for kernel_id, coefficient in enumerate(scaled_coefficients):
                    if coefficient == 0:
                        continue
                    kernel = tables[height][direction_index[direction]][kernel_id]
                    for left_id in range(count):
                        row = kernel[left_id]
                        out = plane[left_id]
                        for right_id in range(count):
                            out[right_id] += coefficient * row[right_id]
                planes.append(plane)
                for right_id in range(count):
                    total = 0
                    for left_id in range(count):
                        value = plane[left_id][right_id]
                        values.add(Fraction(value, denominator))
                        total += value
                    if total != numerator_target:
                        one_ok = False
                    if height == 3 and direction_index[direction] == sample_direction and right_id == sample_right:
                        sample_one = Fraction(total, numerator_target)
            for first, second in combinations(range(len(axis_steps)), 2):
                left_plane = planes[first]
                right_plane = planes[second]
                for right_a in range(count):
                    for right_b in range(count):
                        total = 0
                        for left_id in range(count):
                            total += left_plane[left_id][right_a] * right_plane[left_id][right_b]
                        if total != pair_target:
                            two_ok = False
                        if (
                            height == 3
                            and first == second_direction
                            and second == sample_direction
                            and right_a == second_right
                            and right_b == sample_right
                        ):
                            sample_two = Fraction(total, pair_target)
        return one_ok, two_ok, values, sample_one, sample_two

    witness_one, witness_two, witness_values, witness_sample_one, witness_sample_two = moments(WITNESS)
    nonpositive_one, nonpositive_two, nonpositive_values, _, _ = moments(NONPOSITIVE)
    integer_one, integer_two, _, integer_sample_one, integer_sample_two = moments(INTEGER_BOX)
    far_end = True
    for height in HEIGHTS:
        for direction in axis_steps:
            for left_id in range(count):
                total = Fraction(0)
                for right_id in range(count):
                    total += sum(
                        (WITNESS[kernel_id] * tables[height][direction_index[direction]][kernel_id][left_id][right_id])
                        for kernel_id in range(len(KERNELS))
                    )
                if total != 0:
                    far_end = False
    checks.check(
        "the equal-coefficient mixture is strictly positive and every one- and two-neighbour mean is 1",
        witness_one
        and witness_two
        and witness_values == WITNESS_VALUES
        and witness_sample_one == 1
        and witness_sample_two == 1
        and far_end,
    )
    checks.check(
        "coefficient 2 on the chirality cap is not strictly positive and still has those means equal to 1",
        nonpositive_one
        and nonpositive_two
        and nonpositive_values == {Fraction(-1), Fraction(1), Fraction(3)},
    )
    checks.check(
        "the integer coefficient box 1 through 10 has every one- and two-neighbour mean equal to 1",
        integer_one and integer_two and integer_sample_one == 1 and integer_sample_two == 1,
    )
    print(f"OVERLAP bond {overlap_bond}")
    print(f"SPLIT bond {split_bond}")
    print(
        "WITNESS coefficients "
        + " ".join(f"{name}={coefficient}" for name, coefficient in zip(KERNELS, WITNESS))
    )
    print("WITNESS values " + " ".join(str(value) for value in sorted(witness_values)))
    print(f"WITNESS sample moments {witness_sample_one} {witness_sample_two}")
    print(
        "INTEGER coefficients "
        + " ".join(f"{name}={coefficient}" for name, coefficient in zip(KERNELS, INTEGER_BOX))
    )
    print(f"INTEGER sample moments {integer_sample_one} {integer_sample_two}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
