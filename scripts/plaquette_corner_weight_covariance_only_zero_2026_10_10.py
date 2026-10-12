#!/usr/bin/env python3
"""Which integer corner weights are covariant square circulations.

Each corner of one unit square takes a value in {0, 1, blank}. A weight
vector (w0, w1, w2, w3) defines the sum of wi times the numeric value at
corner i, with blank counted as 0. Covariance uses the boundary-sign
character of the eight corner-preserving proper isometries. The solution
module is computed over Z. No surviving weight is adopted as a flux.
"""

from __future__ import annotations

from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/PLAQUETTE_CORNER_WEIGHT_COVARIANCE_ONLY_ZERO_BOUNDED_THEOREM_NOTE_2026-10-10.md',)

BLANK = 2
CORNERS = (
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
)
CORNER_INDEX = {corner: index for index, corner in enumerate(CORNERS)}
POSITIVE_CYCLES = tuple((0, 1, 2, 3)[shift:] + (0, 1, 2, 3)[:shift] for shift in range(4))
NEGATIVE_CYCLES = tuple((0, 3, 2, 1)[shift:] + (0, 3, 2, 1)[:shift] for shift in range(4))
QUARTER = (
    ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    (1, 0, 0),
)
HALF_TURN = (
    ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    (1, 1, 0),
)
THREE_QUARTER = (
    ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
    (0, 1, 0),
)
OTHER_DIAGONAL = (
    ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
    (1, 1, 0),
)
NAMED_ROWS = (
    (-1, 1, 0, 0),
    (-1, 0, 1, 0),
    (-1, 0, 0, 1),
    (0, 0, 0, 2),
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


def det(matrix: tuple[tuple[int, int, int], ...]) -> int:
    first, second, third = matrix
    return (
        first[0] * (second[1] * third[2] - second[2] * third[1])
        - first[1] * (second[0] * third[2] - second[2] * third[0])
        + first[2] * (second[0] * third[1] - second[1] * third[0])
    )


def proper_group() -> list[tuple[tuple[int, int, int], ...]]:
    group = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0] for _ in range(3)]
            for axis in range(3):
                rows[axis][perm[axis]] = signs[axis]
            matrix = tuple(tuple(row) for row in rows)
            if det(matrix) == 1:
                group.append(matrix)
    return group


def apply(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def translate(vector: tuple[int, int, int], shift: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(vector[i] + shift[i] for i in range(3))


def text(coloring: tuple[int, ...]) -> str:
    return "".join("b" if value == BLANK else str(value) for value in coloring)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(right[left[index]] for index in range(4))


def act(perm: tuple[int, ...], coloring: tuple[int, ...]) -> tuple[int, ...]:
    image = [0, 0, 0, 0]
    for index, value in enumerate(coloring):
        image[perm[index]] = value
    return tuple(image)


def character(perm: tuple[int, ...]) -> int:
    if perm in POSITIVE_CYCLES:
        return 1
    if perm in NEGATIVE_CYCLES:
        return -1
    return 0


def number(value: int) -> int:
    if value == BLANK:
        return 0
    return value


def weighted(coloring: tuple[int, ...], weights: tuple[int, int, int, int]) -> int:
    return sum(weights[index] * number(coloring[index]) for index in range(4))


def preserving_isometries(
    group: list[tuple[tuple[int, int, int], ...]],
) -> dict[tuple[tuple[tuple[int, int, int], ...], tuple[int, int, int]], tuple[int, ...]]:
    found: dict[tuple[tuple[tuple[int, int, int], ...], tuple[int, int, int]], tuple[int, ...]] = {}
    corner_set = set(CORNERS)
    for matrix in group:
        for source in CORNERS:
            for target in CORNERS:
                shift = tuple(target[i] - apply(matrix, source)[i] for i in range(3))
                images = []
                keeps_square = True
                for corner in CORNERS:
                    image = translate(apply(matrix, corner), shift)
                    if image not in corner_set:
                        keeps_square = False
                        break
                    images.append(CORNER_INDEX[image])
                if keeps_square:
                    found[(matrix, shift)] = tuple(images)
    return found


def equation_row(perm: tuple[int, ...], corner: int) -> tuple[int, int, int, int]:
    row = [0, 0, 0, 0]
    row[perm[corner]] += 1
    row[corner] -= character(perm)
    return tuple(row)


def triangular_form(
    rows: tuple[tuple[int, int, int, int], ...],
) -> list[list[int]]:
    matrix = [list(row) for row in rows]
    matrix[1] = [matrix[1][col] - matrix[0][col] for col in range(4)]
    matrix[2] = [matrix[2][col] - matrix[0][col] for col in range(4)]
    matrix[2] = [matrix[2][col] - matrix[1][col] for col in range(4)]
    return matrix


def four_det(rows: tuple[tuple[int, int, int, int], ...]) -> int:
    matrix = triangular_form(rows)
    off_diagonal = any(matrix[row][col] != 0 for row in range(4) for col in range(4) if col < row)
    if off_diagonal:
        return 0
    value = 1
    for index in range(4):
        value *= matrix[index][index]
    return value


def restore_named_rows(matrix: list[list[int]]) -> tuple[tuple[int, int, int, int], ...]:
    restored = [list(row) for row in matrix]
    restored[2] = [restored[2][col] + restored[1][col] for col in range(4)]
    restored[2] = [restored[2][col] + restored[0][col] for col in range(4)]
    restored[1] = [restored[1][col] + restored[0][col] for col in range(4)]
    return tuple(tuple(row) for row in restored)


def combination(row: tuple[int, int, int, int]) -> tuple[int, int, int, int] | None:
    first, second, third, fourth = row
    if (first + second + third + fourth) % 2:
        return None
    return (
        second,
        third,
        -first - second - third,
        (first + second + third + fourth) // 2,
    )


def apply_combination(coeffs: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    total = [0, 0, 0, 0]
    for coeff, row in zip(coeffs, NAMED_ROWS):
        for index in range(4):
            total[index] += coeff * row[index]
    return tuple(total)


def back_substitute(matrix: list[list[int]]) -> tuple[int, int, int, int] | None:
    weights = [0, 0, 0, 0]
    for row in range(3, -1, -1):
        pivot = matrix[row][row]
        if pivot == 0:
            return None
        rhs = -sum(matrix[row][col] * weights[col] for col in range(row + 1, 4))
        if rhs % pivot != 0:
            return None
        weights[row] = rhs // pivot
    return tuple(weights)


def main() -> None:
    checks = Checks()
    group = proper_group()
    isometries = preserving_isometries(group)
    quarter = isometries.get(QUARTER)
    half = isometries.get(HALF_TURN)
    three = isometries.get(THREE_QUARTER)
    other = isometries.get(OTHER_DIAGONAL)
    elements = []
    seen = set()
    for perm in isometries.values():
        if perm not in seen:
            seen.add(perm)
            elements.append(perm)
    perm_to_chi = {perm: character(perm) for perm in elements}
    homomorphism = all(
        perm_to_chi.get(compose(left, right)) == perm_to_chi[left] * perm_to_chi[right]
        for left in elements
        for right in elements
    )
    checks.check(
        "four named proper isometries induce the stated boundary permutations, and the character is a homomorphism",
        len(group) == 24
        and all(det(matrix) == 1 for matrix in group)
        and len(isometries) == 8
        and set(elements) == set(POSITIVE_CYCLES + NEGATIVE_CYCLES)
        and quarter == (1, 2, 3, 0)
        and half == (2, 3, 0, 1)
        and three == (3, 0, 1, 2)
        and other == (2, 1, 0, 3)
        and character(quarter) == 1
        and character(half) == 1
        and character(three) == 1
        and character(other) == -1
        and homomorphism
        and sum(character(perm) == 1 for perm in elements) == 4
        and sum(character(perm) == -1 for perm in elements) == 4,
    )

    rows = [equation_row(perm, corner) for perm in elements for corner in range(4)]
    patterns = {
        tuple(number(color) for color in coloring)
        for coloring in product((0, 1, BLANK), repeat=4)
    }
    single = (1, 0, 0, 0)
    single_image = act(other, single) if other is not None else None
    checks.check(
        "the single-one colorings produce 32 even-sum equations, and blank adds no new numeric pattern",
        len(rows) == 32
        and all(sum(row) % 2 == 0 for row in rows)
        and other is not None
        and equation_row(quarter, 0) == NAMED_ROWS[0]
        and equation_row(half, 0) == NAMED_ROWS[1]
        and equation_row(three, 0) == NAMED_ROWS[2]
        and equation_row(other, 3) == NAMED_ROWS[3]
        and patterns == set(product((0, 1), repeat=4))
        and single_image == (0, 0, 1, 0)
        and text(single) == "1000"
        and text(single_image) == "0010",
    )

    generated = []
    odd_rejected = combination((1, 0, 0, 0)) is None
    for row in rows:
        coeffs = combination(row)
        generated.append(coeffs is not None and apply_combination(coeffs) == row)
    checks.check(
        "those four rows have determinant -2 and generate every covariance equation over Z",
        four_det(NAMED_ROWS) == -2
        and odd_rejected
        and all(generated)
        and all(sum(row) % 2 == 0 for row in NAMED_ROWS),
    )

    triangle = triangular_form(NAMED_ROWS)
    restored = restore_named_rows(triangle)
    solution = back_substitute(triangle)
    checks.check(
        "exact division of the triangular system returns only the zero weight",
        triangle == [[-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, -1, 1], [0, 0, 0, 2]]
        and restored == NAMED_ROWS
        and solution == (0, 0, 0, 0)
        and (2 * 0) // 2 == 0,
    )

    colorings = tuple(product((0, 1, BLANK), repeat=4))
    zero_failures = 0
    constant = (1, 1, 1, 1)
    constant_value = weighted(single, constant)
    constant_image_value = weighted(single_image, constant) if single_image is not None else None
    constant_required = character(other) * constant_value if other is not None else None
    identity_matches = True
    basis_weights = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), constant)
    for perm in elements:
        chi = character(perm)
        for coloring in colorings:
            if weighted(act(perm, coloring), (0, 0, 0, 0)) != 0:
                zero_failures += 1
            for weights in basis_weights:
                predicted = sum(
                    number(coloring[index]) * (weights[perm[index]] - chi * weights[index])
                    for index in range(4)
                )
                actual = weighted(act(perm, coloring), weights) - chi * weighted(coloring, weights)
                identity_matches = identity_matches and actual == predicted
    checks.check(
        "zero passes every pair, and the constant weight fails on the named reversal of 1000",
        zero_failures == 0
        and len(colorings) == 81
        and constant_value == 1
        and constant_image_value == 1
        and constant_required == -1
        and constant_image_value != constant_required
        and identity_matches,
    )

    blank_pairs = ((0, 0), (1, 1), (BLANK, 0))
    checks.check(
        "blank counts as 0, zero counts as 0, and the alphabet still has three symbols",
        all(number(color) == image for color, image in blank_pairs)
        and set(product((0, 1, BLANK), repeat=1)) == {(0,), (1,), (BLANK,)}
        and BLANK not in (0, 1),
    )

    print("relation_lattice: even coordinate sum, index 2, determinant -2")
    print("solution: (0, 0, 0, 0)")
    print("basis: empty")
    print(
        "named_reversal: R = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]], "
        "b = (1, 1, 0), perm = (2, 1, 0, 3), chi = -1"
    )
    print(
        "constant_weight: (1, 1, 1, 1) on 1000 has value 1; the image 0010 has value 1, not -1"
    )
    print("per_element: four named rows generate the even-sum lattice; the integer kernel is zero")
    print("per_site: one supplied unit square; no second square; no site was selected")
    print("per_mode: the boundary-sign character; the zero weight was not adopted as a flux")
    print("per_block: alphabet {0, 1, blank}; blank counts as 0 only inside the weighted sum")
    print("lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
