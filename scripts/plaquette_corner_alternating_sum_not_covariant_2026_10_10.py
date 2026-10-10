#!/usr/bin/env python3
"""Whether one alternating corner sum is a covariant square circulation.

The four corners of one unit square take values in {0, 1, blank}. The
assignment is the alternating sum of those four values in boundary order,
with blank counted as 0. Covariance uses the boundary-sign character of
the eight corner-preserving proper isometries. The sum is not adopted as
a flux, and it is not expanded on the free orbits.
"""

from __future__ import annotations

from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120

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
SIGNS = (1, -1, 1, -1)
REVERSAL = (
    (
        (0, 1, 0),
        (1, 0, 0),
        (0, 0, -1),
    ),
    (0, 0, 0),
)
QUARTER_TURN = (
    (
        (0, -1, 0),
        (1, 0, 0),
        (0, 0, 1),
    ),
    (1, 0, 0),
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


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = 0
    for left in range(4):
        for right in range(left + 1, 4):
            if perm[left] > perm[right]:
                inversions += 1
    return -1 if inversions % 2 else 1


def number(value: int) -> int:
    if value == BLANK:
        return 0
    return value


def alternating(coloring: tuple[int, ...]) -> int:
    return sum(SIGNS[index] * number(coloring[index]) for index in range(4))


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


def main() -> None:
    checks = Checks()
    group = proper_group()
    isometries = preserving_isometries(group)
    reversal_perm = isometries.get(REVERSAL)
    quarter_perm = isometries.get(QUARTER_TURN)
    reversal_count = sum(key == REVERSAL for key in isometries)
    quarter_count = sum(key == QUARTER_TURN for key in isometries)
    reversal_images = None
    if reversal_perm is not None:
        reversal_images = tuple(translate(apply(REVERSAL[0], corner), REVERSAL[1]) for corner in CORNERS)
    checks.check(
        "the reversal x -> Rx with R swapping x and y and sending z to -z is one corner-preserving proper isometry",
        len(group) == 24
        and all(det(matrix) == 1 for matrix in group)
        and reversal_count == 1
        and reversal_perm == (0, 3, 2, 1)
        and character(reversal_perm) == -1
        and reversal_images == ((0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)),
    )

    elements = []
    seen = set()
    for perm in isometries.values():
        if perm not in seen:
            seen.add(perm)
            elements.append((perm, character(perm)))
    perm_to_chi = {perm: chi for perm, chi in elements}
    homomorphism = True
    for left, left_chi in elements:
        for right, right_chi in elements:
            homomorphism = homomorphism and perm_to_chi.get(compose(left, right)) == left_chi * right_chi
    checks.check(
        "those eight maps are the boundary cycles, four of each character, and the character is a homomorphism",
        len(isometries) == 8
        and set(perm_to_chi) == set(POSITIVE_CYCLES + NEGATIVE_CYCLES)
        and sum(chi == 1 for chi in perm_to_chi.values()) == 4
        and sum(chi == -1 for chi in perm_to_chi.values()) == 4
        and homomorphism
        and all(chi in (-1, 1) for chi in perm_to_chi.values()),
    )

    witness = (0, 1, 0, 1)
    witness_value = alternating(witness)
    witness_image = act(reversal_perm, witness) if reversal_perm is not None else None
    witness_image_value = alternating(witness_image) if witness_image is not None else None
    required = character(reversal_perm) * witness_value if reversal_perm is not None else None
    checks.check(
        "the reversal fixes 0101, whose alternating sum is -2 rather than the required +2",
        witness_image == witness
        and text(witness) == "0101"
        and witness_value == -2
        and witness_image_value == -2
        and required == 2
        and witness_image_value != required,
    )

    all_colorings = list(product((0, 1, BLANK), repeat=4))
    fixed = [
        coloring
        for coloring in all_colorings
        if reversal_perm is not None and act(reversal_perm, coloring) == coloring
    ]
    nonzero_fixed = [coloring for coloring in fixed if alternating(coloring) != 0]
    fixed_fail = all(
        alternating(act(reversal_perm, coloring)) != character(reversal_perm) * alternating(coloring)
        for coloring in nonzero_fixed
    ) if reversal_perm is not None else False
    checks.check(
        "the reversal fixes 27 colorings, and the alternating sum is nonzero on 18 of them",
        len(all_colorings) == 81
        and len(fixed) == 27
        and len(nonzero_fixed) == 18
        and witness in nonzero_fixed
        and fixed_fail,
    )

    checks.check(
        "the sign of the corner permutation does not repair the witness",
        reversal_perm is not None
        and permutation_sign(reversal_perm) == -1
        and witness_image_value == witness_value
        and witness_image_value != permutation_sign(reversal_perm) * witness_value,
    )

    quarter_coloring = (1, 0, 0, 0)
    quarter_value = alternating(quarter_coloring)
    quarter_image = act(quarter_perm, quarter_coloring) if quarter_perm is not None else None
    quarter_image_value = alternating(quarter_image) if quarter_image is not None else None
    quarter_required = character(quarter_perm) * quarter_value if quarter_perm is not None else None
    checks.check(
        "the quarter turn sends the alternating sum of 1000 from 1 to -1",
        quarter_count == 1
        and quarter_perm == (1, 2, 3, 0)
        and character(quarter_perm) == 1
        and text(quarter_coloring) == "1000"
        and quarter_value == 1
        and quarter_image_value == -1
        and quarter_required == 1
        and quarter_image_value != quarter_required,
    )

    values = [alternating(coloring) for coloring in all_colorings]
    blank_pairs = {(0, 0), (1, 1), (BLANK, 0)}
    numeric_ok = all(number(color) == image for color, image in blank_pairs)
    checks.check(
        "blank counts as 0, the alphabet is unchanged, and the sum is not identically zero",
        numeric_ok
        and set(product((0, 1, BLANK), repeat=1)) == {(0,), (1,), (BLANK,)}
        and all(isinstance(value, int) and -2 <= value <= 2 for value in values)
        and any(value != 0 for value in values)
        and 0 in values,
    )

    failures = 0
    identity_failures = 0
    witness_seen = False
    for perm, chi in elements:
        for coloring in all_colorings:
            image_value = alternating(act(perm, coloring))
            current = alternating(coloring)
            if image_value != chi * current:
                failures += 1
                if perm == reversal_perm and coloring == witness:
                    witness_seen = True
            if perm == (0, 1, 2, 3) and image_value != current:
                identity_failures += 1
    checks.check(
        "the assignment fails on 192 pairs, including the reversal of 0101",
        failures == 192 and identity_failures == 0 and witness_seen and required != witness_value,
    )

    print(
        "witness_isometry: R = [[0, 1, 0], [1, 0, 0], [0, 0, -1]], b = (0, 0, 0), "
        "perm = (0, 3, 2, 1), chi = -1"
    )
    print(
        "witness_coloring: 0101, value = -2, image = 0101, image_value = -2, required = 2"
    )
    print(
        "per_element: one reversal, one coloring, and the eight boundary characters; "
        f"{failures} failing pairs, with no coefficient triple emitted"
    )
    print(
        "per_site: one supplied unit square; the sum is not read on a second square; no site was selected"
    )
    print(
        "per_mode: the circulation character already defined; the alternating sum was not adopted as a flux"
    )
    print(
        "per_block: alphabet {0, 1, blank}; blank counts as 0 only inside this sum; no fourth color"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")


if __name__ == "__main__":
    main()
