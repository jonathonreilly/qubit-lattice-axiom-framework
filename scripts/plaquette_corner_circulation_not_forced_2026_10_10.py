#!/usr/bin/env python3
"""Whether proper-cubic covariance forces a circulation on one square.

The four corners of one unit square take values in {0, 1, blank}. A
circulation assignment is an integer on each of the 81 colorings. It is
covariant when a corner-preserving proper isometry multiplies that integer
by the sign of the induced boundary permutation. No edge variable is
introduced, and no alternating sum of corner records is formed.
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
FREE_REPS = ("001b", "011b", "01bb")


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


def preserving_isometries(
    group: list[tuple[tuple[int, int, int], ...]],
) -> dict[tuple[tuple[int, ...], tuple[int, int, int]], tuple[int, ...]]:
    found: dict[tuple[tuple[int, ...], tuple[int, int, int]], tuple[int, ...]] = {}
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


def colorings() -> list[tuple[int, ...]]:
    return list(product((0, 1, BLANK), repeat=4))


def orbits(
    elements: list[tuple[tuple[int, ...], int]],
    all_colorings: list[tuple[int, ...]],
) -> list[set[tuple[int, ...]]]:
    pending = set(all_colorings)
    found = []
    while pending:
        start = min(pending)
        orbit: set[tuple[int, ...]] = set()
        stack = [start]
        while stack:
            coloring = stack.pop()
            if coloring in orbit:
                continue
            orbit.add(coloring)
            for perm, _chi in elements:
                stack.append(act(perm, coloring))
        pending -= orbit
        found.append(orbit)
    return found


def stabilizer_elements(
    elements: list[tuple[tuple[int, ...], int]],
    coloring: tuple[int, ...],
) -> list[tuple[tuple[int, ...], int]]:
    return [(perm, chi) for perm, chi in elements if act(perm, coloring) == coloring]


def generator(
    elements: list[tuple[tuple[int, ...], int]],
    rep: tuple[int, ...],
) -> dict[tuple[int, ...], int] | None:
    values: dict[tuple[int, ...], int] = {}
    for perm, chi in elements:
        image = act(perm, rep)
        previous = values.get(image)
        if previous is None:
            values[image] = chi
        elif previous != chi:
            return None
    if len(values) != len(elements):
        return None
    return values


def covariant(
    elements: list[tuple[tuple[int, ...], int]],
    values: dict[tuple[int, ...], int],
    all_colorings: list[tuple[int, ...]],
) -> bool:
    for coloring in all_colorings:
        current = values.get(coloring, 0)
        for perm, chi in elements:
            if values.get(act(perm, coloring), 0) != chi * current:
                return False
    return True


def main() -> None:
    checks = Checks()
    group = proper_group()
    closed = all(det(matrix) == 1 for matrix in group)
    for left in group:
        for right in group:
            product_matrix = tuple(
                tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
                for i in range(3)
            )
            closed = closed and product_matrix in group
    isometries = preserving_isometries(group)
    perm_characters: dict[tuple[int, ...], set[int]] = {}
    for perm in isometries.values():
        perm_characters.setdefault(perm, set()).add(character(perm))
    elements = []
    characters_ok = True
    for perm, chis in sorted(perm_characters.items()):
        characters_ok = characters_ok and chis == {character(perm)} and character(perm) in (-1, 1)
        elements.append((perm, character(perm)))
    checks.check(
        "the proper cubic group has 24 elements and exactly 8 preserve the square",
        len(group) == 24
        and closed
        and len(isometries) == 8
        and len(elements) == 8
        and characters_ok,
    )

    perm_to_chi = {perm: chi for perm, chi in elements}
    group_ok = True
    for left, left_chi in elements:
        for right, right_chi in elements:
            composed = compose(left, right)
            group_ok = group_ok and perm_to_chi.get(composed) == left_chi * right_chi
    plus = sum(chi == 1 for _perm, chi in elements)
    minus = sum(chi == -1 for _perm, chi in elements)
    checks.check(
        "those 8 form the dihedral action, four of each character, and the character is a homomorphism",
        group_ok
        and plus == 4
        and minus == 4
        and set(perm_to_chi) == set(POSITIVE_CYCLES + NEGATIVE_CYCLES),
    )

    all_colorings = colorings()
    coloring_orbits = orbits(elements, all_colorings)
    fixed_sum = 0
    fixed_counts = {1: [], -1: []}
    for perm, chi in elements:
        fixed = sum(1 for coloring in all_colorings if act(perm, coloring) == coloring)
        fixed_sum += fixed
        fixed_counts[chi].append(fixed)
    burnside = fixed_sum / len(elements)
    checks.check(
        "enumeration and the Burnside average both give 21 orbits of the 81 colorings",
        len(all_colorings) == 81
        and len(coloring_orbits) == 21
        and fixed_sum == 168
        and burnside == 21
        and sorted(fixed_counts[1]) == [3, 3, 9, 81]
        and sorted(fixed_counts[-1]) == [9, 9, 27, 27],
    )

    stabilizer_ok = True
    for orbit in coloring_orbits:
        for coloring in orbit:
            order = len(stabilizer_elements(elements, coloring))
            stabilizer_ok = stabilizer_ok and len(orbit) * order == 8
    checks.check(
        "orbit size times stabilizer order is 8 on every coloring",
        stabilizer_ok,
    )

    free = []
    killed = []
    for orbit in coloring_orbits:
        rep = min(orbit)
        stab = stabilizer_elements(elements, rep)
        if all(chi == 1 for _perm, chi in stab) and generator(elements, rep) is not None:
            free.append(orbit)
        else:
            killed.append(orbit)
    free_reps = tuple(text(min(orbit)) for orbit in sorted(free, key=min))
    checks.check(
        "the free orbits are 001b, 011b, and 01bb, each of size 8",
        free_reps == FREE_REPS
        and all(len(orbit) == 8 for orbit in free)
        and all(len(stabilizer_elements(elements, min(orbit))) == 1 for orbit in free),
    )

    killed_sizes: dict[int, int] = {}
    for orbit in killed:
        killed_sizes[len(orbit)] = killed_sizes.get(len(orbit), 0) + 1
    killed_colorings = sum(len(orbit) for orbit in killed)
    checks.check(
        "the other 18 orbits, 57 colorings, are killed, with sizes 1, 2, and 4",
        len(killed) == 18
        and killed_colorings == 57
        and killed_sizes == {1: 3, 2: 3, 4: 12}
        and killed_colorings + sum(len(orbit) for orbit in free) == 81,
    )

    quarter_fixed = []
    for perm, chi in elements:
        cycle_lengths = []
        seen: set[int] = set()
        for start in range(4):
            if start in seen:
                continue
            length = 0
            cursor = start
            while cursor not in seen:
                seen.add(cursor)
                cursor = perm[cursor]
                length += 1
            cycle_lengths.append(length)
        if chi == 1 and cycle_lengths == [4]:
            fixed = {coloring for coloring in all_colorings if act(perm, coloring) == coloring}
            quarter_fixed.append(fixed)
    constants = {
        (0, 0, 0, 0),
        (1, 1, 1, 1),
        (BLANK, BLANK, BLANK, BLANK),
    }
    checkerboard = (0, 1, 0, 1)
    checkerboard_killed = any(min(orbit) == checkerboard for orbit in killed)
    checks.check(
        "quarter-turns fix only the three constant colorings, and 0101 is killed",
        len(quarter_fixed) == 2
        and all(fixed == constants for fixed in quarter_fixed)
        and checkerboard_killed,
    )

    generators = []
    basis_ok = True
    for orbit in sorted(free, key=min):
        values = generator(elements, min(orbit))
        basis_ok = basis_ok and values is not None
        if values is not None:
            generators.append(values)
    identity_at_reps = True
    reps = [min(orbit) for orbit in sorted(free, key=min)]
    for row, values in enumerate(generators):
        for column, rep in enumerate(reps):
            identity_at_reps = identity_at_reps and values.get(rep, 0) == (1 if row == column else 0)
        basis_ok = basis_ok and covariant(elements, values, all_colorings)
    determined = True
    for coloring in all_colorings:
        support = [values.get(coloring, 0) for values in generators]
        nonzero = [entry for entry in support if entry != 0]
        if coloring in {item for orbit in killed for item in orbit}:
            determined = determined and nonzero == []
        else:
            determined = determined and nonzero in ([1], [-1]) and support.count(0) == 2
    checks.check(
        "the three generators are a basis and the rank is 3",
        basis_ok and identity_at_reps and determined and len(generators) == 3,
    )

    zero = {coloring: 0 for coloring in all_colorings}
    signs_ok = covariant(elements, zero, all_colorings)
    for values in generators:
        negative = {coloring: -entry for coloring, entry in values.items()}
        signs_ok = signs_ok and covariant(elements, negative, all_colorings)
        signs_ok = signs_ok and any(entry != 0 for entry in values.values())
        signs_ok = signs_ok and negative != values
    checks.check(
        "zero is covariant, and each generator disagrees with its negative",
        signs_ok,
    )

    by_rep = {text(rep): values for rep, values in zip(reps, generators)}
    one_blank_pair = by_rep["01bb"]
    recorded_pair = by_rep["001b"]
    checks.check(
        "the 01bb generator is not a sign flip of the 001b generator",
        one_blank_pair.get(reps[FREE_REPS.index("001b")], 0) == 0
        and recorded_pair.get(reps[FREE_REPS.index("001b")], 0) == 1
        and one_blank_pair != recorded_pair
        and {coloring: -entry for coloring, entry in one_blank_pair.items()} != recorded_pair,
    )

    free_colorings = {coloring for orbit in free for coloring in orbit}
    killed_colorings_set = {coloring for orbit in killed for coloring in orbit}
    swap_ok = True
    for coloring in all_colorings:
        swapped = tuple(BLANK if value == BLANK else 1 - value for value in coloring)
        swap_ok = swap_ok and ((coloring in free_colorings) == (swapped in free_colorings))
        swap_ok = swap_ok and ((coloring in killed_colorings_set) == (swapped in killed_colorings_set))
    checks.check(
        "swapping 0 with 1 and leaving blanks fixed preserves which orbits are free",
        swap_ok,
    )

    reversal_ok = True
    for coloring in killed_colorings_set:
        reversal_ok = reversal_ok and any(
            chi == -1 and act(perm, coloring) == coloring for perm, chi in elements
        )
    for coloring in free_colorings:
        reversal_ok = reversal_ok and not any(
            chi == -1 and act(perm, coloring) == coloring for perm, chi in elements
        )
    checks.check(
        "a coloring is killed exactly when a reversing isometry fixes it",
        reversal_ok and len(killed_colorings_set) == 57 and len(free_colorings) == 24,
    )

    print(
        "per_element: checked all 81 colorings and all 8 corner-preserving proper isometries"
    )
    print(
        "per_site: one supplied unit square; transport reads the same assignment on any coordinate unit square; no site was selected"
    )
    print(
        "per_mode: one circulation character, the sign of the induced boundary permutation; no edge flux was formed"
    )
    print(
        "per_block: the alphabet {0, 1, blank} on four corners; no bond factor and no deleted-blank menu"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")


if __name__ == "__main__":
    main()
