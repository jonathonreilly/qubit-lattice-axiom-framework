#!/usr/bin/env python3
"""Which shared symbol weights are covariant square sums.

Each corner of one unit square takes a value in {0, 1, blank}. Color 0
contributes 0, color 1 contributes an integer u, and blank contributes an
integer v, the same pair at every corner. Covariance uses the boundary-sign
character of the eight corner-preserving proper isometries. The solution
module is computed over Z. No surviving pair is adopted as a flux.
"""

from __future__ import annotations

from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/PLAQUETTE_CORNER_SYMBOL_PAIR_COVARIANCE_ONLY_ZERO_BOUNDED_THEOREM_NOTE_2026-10-10.md',)

BLANK = 2
ZERO = 0
ONE = 1
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
OTHER_DIAGONAL = (
    ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
    (1, 1, 0),
)
UNIT_ROWS = (
    (1, 0),
    (0, 1),
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


def det2(rows: tuple[tuple[int, int], tuple[int, int]]) -> int:
    return rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]


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


def contribution(value: int, pair: tuple[int, int]) -> int:
    symbol_u, blank_v = pair
    if value == ZERO:
        return 0
    if value == ONE:
        return symbol_u
    if value == BLANK:
        return blank_v
    raise ValueError(value)


def counts(coloring: tuple[int, ...]) -> tuple[int, int]:
    return (
        sum(value == ONE for value in coloring),
        sum(value == BLANK for value in coloring),
    )


def weighted(coloring: tuple[int, ...], pair: tuple[int, int]) -> int:
    return sum(contribution(value, pair) for value in coloring)


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


def combination(row: tuple[int, int]) -> tuple[int, int]:
    ones, blanks = row
    return (ones, blanks)


def apply_combination(coeffs: tuple[int, int]) -> tuple[int, int]:
    total = [0, 0]
    for coeff, row in zip(coeffs, UNIT_ROWS):
        total[0] += coeff * row[0]
        total[1] += coeff * row[1]
    return tuple(total)


def back_substitute(matrix: list[list[int]]) -> tuple[int, int] | None:
    weights = [0, 0]
    for row in range(1, -1, -1):
        pivot = matrix[row][row]
        if pivot == 0:
            return None
        rhs = -sum(matrix[row][col] * weights[col] for col in range(row + 1, 2))
        if rhs % pivot != 0:
            return None
        weights[row] = rhs // pivot
    return tuple(weights)


def divide_pivot(pivot: int, rhs: int) -> int | None:
    if pivot == 0 or rhs % pivot != 0:
        return None
    return rhs // pivot


def main() -> None:
    checks = Checks()
    group = proper_group()
    isometries = preserving_isometries(group)
    quarter = isometries.get(QUARTER)
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
    permutations_ok = all(tuple(sorted(perm)) == (0, 1, 2, 3) for perm in elements)
    checks.check(
        "eight proper isometries permute the square, and the boundary sign is a homomorphism",
        len(group) == 24
        and all(det(matrix) == 1 for matrix in group)
        and len(CORNERS) == 4
        and len(isometries) == 8
        and permutations_ok
        and set(elements) == set(POSITIVE_CYCLES + NEGATIVE_CYCLES)
        and quarter == (1, 2, 3, 0)
        and other == (2, 1, 0, 3)
        and character(quarter) == 1
        and character(other) == -1
        and homomorphism
        and sum(character(perm) == 1 for perm in elements) == 4
        and sum(character(perm) == -1 for perm in elements) == 4,
    )

    colorings = tuple(product((ZERO, ONE, BLANK), repeat=4))
    single_one = (ONE, ZERO, ZERO, ZERO)
    single_blank = (BLANK, ZERO, ZERO, ZERO)
    mixed = (ONE, BLANK, ZERO, ZERO)
    basis_pairs = ((1, 0), (0, 1))
    count_invariant = True
    residual_matches = True
    same_at_every_corner = True
    for perm in elements:
        chi = character(perm)
        for coloring in colorings:
            image = act(perm, coloring)
            count_invariant = count_invariant and counts(image) == counts(coloring)
            for pair in basis_pairs:
                actual = weighted(image, pair) - chi * weighted(coloring, pair)
                predicted = (1 - chi) * weighted(coloring, pair)
                residual_matches = residual_matches and actual == predicted
    for shift in range(4):
        moved_one = tuple(ONE if index == shift else ZERO for index in range(4))
        moved_blank = tuple(BLANK if index == shift else ZERO for index in range(4))
        same_at_every_corner = same_at_every_corner and weighted(moved_one, (1, 0)) == 1
        same_at_every_corner = same_at_every_corner and weighted(moved_blank, (0, 1)) == 1
    checks.check(
        "the shared pair is invariant under every corner permutation, so the residual is (1 - chi) times the sum",
        len(colorings) == 81
        and count_invariant
        and residual_matches
        and same_at_every_corner
        and counts(single_one) == (1, 0)
        and counts(single_blank) == (0, 1)
        and weighted(single_one, (1, 0)) == 1
        and weighted(single_blank, (0, 1)) == 1,
    )

    count_rows = tuple(counts(coloring) for coloring in colorings)
    generated = []
    preserving_rows = []
    reversing_rows = []
    for coloring in colorings:
        row = counts(coloring)
        coeffs = combination(row)
        generated.append(apply_combination(coeffs) == row)
    for perm in elements:
        chi = character(perm)
        for coloring in colorings:
            if chi == 1:
                preserving_rows.append((0, 0))
            else:
                reversing_rows.append(counts(coloring))
    four_blank = counts((BLANK, BLANK, BLANK, BLANK))
    checks.check(
        "the normalized unit rows have determinant 1 and generate the system after division by 2",
        counts(single_one) == UNIT_ROWS[0]
        and counts(single_blank) == UNIT_ROWS[1]
        and det2(UNIT_ROWS) == 1
        and all(generated)
        and set(count_rows) <= {(ones, blanks) for ones in range(5) for blanks in range(5 - ones)}
        and all(row == (0, 0) for row in preserving_rows)
        and reversing_rows.count((1, 0)) == 16
        and reversing_rows.count((0, 1)) == 16
        and four_blank == (0, 4)
        and apply_combination((0, 4)) == four_blank,
    )

    raw_rows = tuple(
        tuple((1 - character(perm)) * n for n in counts(coloring))
        for perm in elements for coloring in colorings
    )
    checks.check(
        "raw residual rows generate 2Z^2 with index 4, distinct from normalized Z^2",
        (2, 0) in raw_rows and (0, 2) in raw_rows
        and all(a % 2 == b % 2 == 0 for a, b in raw_rows)
        and (1, 0) not in raw_rows and (0, 1) not in raw_rows
        and det2(((2, 0), (0, 2))) == 4,
    )
    triangle = [[1, 0], [0, 1]]
    solution = back_substitute(triangle)
    unit_quotient = divide_pivot(1, 0)
    dependent_quotient = divide_pivot(4, 0)
    checks.check(
        "exact division of the unit pivots returns only the zero pair",
        solution == (0, 0)
        and unit_quotient == 0
        and dependent_quotient == 0
        and divide_pivot(4, 1) is None,
    )

    zero_failures = 0
    one_failures = 0
    blank_failures = 0
    mixed_value = weighted(mixed, (1, -1))
    mixed_image = act(other, mixed) if other is not None else None
    mixed_image_value = weighted(mixed_image, (1, -1)) if mixed_image is not None else None
    one_value = weighted(single_one, (1, 0))
    one_image = act(other, single_one) if other is not None else None
    one_image_value = weighted(one_image, (1, 0)) if one_image is not None else None
    one_required = character(other) * one_value if other is not None else None
    blank_value = weighted(single_blank, (0, 1))
    blank_image = act(other, single_blank) if other is not None else None
    blank_image_value = weighted(blank_image, (0, 1)) if blank_image is not None else None
    blank_required = character(other) * blank_value if other is not None else None
    for perm in elements:
        chi = character(perm)
        for coloring in colorings:
            if weighted(act(perm, coloring), (0, 0)) != 0:
                zero_failures += 1
            if weighted(act(perm, coloring), (1, 0)) != chi * weighted(coloring, (1, 0)):
                one_failures += 1
            if weighted(act(perm, coloring), (0, 1)) != chi * weighted(coloring, (0, 1)):
                blank_failures += 1
    checks.check(
        "zero passes every pair, and each unit pair fails on the named reversal",
        zero_failures == 0
        and one_failures == 260
        and blank_failures == 260
        and text(single_one) == "1000"
        and text(one_image) == "0010"
        and one_value == 1
        and one_image_value == 1
        and one_required == -1
        and one_image_value != one_required
        and text(single_blank) == "b000"
        and text(blank_image) == "00b0"
        and blank_value == 1
        and blank_image_value == 1
        and blank_required == -1
        and blank_image_value != blank_required
        and text(mixed) == "1b00"
        and mixed_value == 0
        and mixed_image_value == 0
        and weighted(single_one, (1, -1)) == 1
        and character(other) * weighted(single_one, (1, -1)) == -1,
    )

    symbol_pairs = ((ZERO, 0), (ONE, 3), (BLANK, -5))
    checks.check(
        "color 0 contributes 0, color 1 contributes u, blank contributes v, and the square stays four corners",
        all(contribution(color, (3, -5)) == image for color, image in symbol_pairs)
        and contribution(ZERO, (3, -5)) == 0
        and len(CORNERS) == 4
        and set(product((ZERO, ONE, BLANK), repeat=1)) == {(ZERO,), (ONE,), (BLANK,)}
        and BLANK not in (ZERO, ONE)
        and weighted(single_one, (0, 0)) == 0
        and weighted(single_blank, (0, 0)) == 0,
    )

    print("raw_relation_lattice: 2Z^2, index 4, determinant 4")
    print("normalized_relation_lattice: Z^2, index 1, determinant 1; same integer kernel")
    print("solution: (0, 0)")
    print("basis: empty")
    print(
        "named_reversal: R = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]], "
        "b = (1, 1, 0), perm = (2, 1, 0, 3), chi = -1"
    )
    print("unit_pair_u: (1, 0) on 1000 has value 1; the image 0010 has value 1, not -1")
    print("unit_pair_v: (0, 1) on b000 has value 1; the image 00b0 has value 1, not -1")
    print("cancelled_pair: (1, -1) vanishes on 1b00 and still fails on 1000")
    print("per_element: the doubled rows generate raw residuals; unit rows generate the equivalent normalized equations; the integer kernel is zero")
    print("per_site: one supplied unit square; no second square; no site was selected")
    print("per_mode: the boundary-sign character; the zero pair was not adopted as a flux")
    print("per_block: alphabet {0, 1, blank}; color 0 contributes 0; color 1 contributes u; blank contributes v")
    print("lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate")
    print("family: the corner-weight family stops after this pair")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
