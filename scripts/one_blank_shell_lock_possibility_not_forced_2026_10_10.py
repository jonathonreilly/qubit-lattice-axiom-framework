#!/usr/bin/env python3
"""What one blank six-neighbor shell forces about a locked direction.

Exactly one axis direction is blank. The other five are in {0,1}. The
proper cubic group permutes the six directions. The output menu is the
same six directions. No bond factor, no 3x3 correlation, no unsoldered
label, no site selector, and no rate.
"""

from __future__ import annotations

from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120

BLANK = 2
DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")

# One lexicographic representative of each orbit. Blank is 2. Columns are
# the shell, its orbit size, its stabilizer order, and the output orbits.
EXPECTED = (
    ((0, 0, 0, 0, 0, 2), 6, 4, (("+x", "-x", "+y", "-y"), ("+z",), ("-z",))),
    ((0, 0, 0, 0, 1, 2), 6, 4, (("+x", "-x", "+y", "-y"), ("+z",), ("-z",))),
    ((0, 0, 0, 1, 0, 2), 24, 1, (("+x",), ("+y",), ("+z",), ("-x",), ("-y",), ("-z",))),
    ((0, 0, 0, 1, 1, 2), 24, 1, (("+x",), ("+y",), ("+z",), ("-x",), ("-y",), ("-z",))),
    ((0, 0, 0, 2, 1, 1), 12, 2, (("+x", "-x"), ("+y",), ("+z", "-z"), ("-y",))),
    ((0, 0, 1, 1, 1, 2), 12, 2, (("+x", "-x"), ("+y", "-y"), ("+z",), ("-z",))),
    ((0, 1, 0, 1, 0, 2), 24, 1, (("+x",), ("+y",), ("+z",), ("-x",), ("-y",), ("-z",))),
    ((0, 1, 0, 1, 1, 2), 24, 1, (("+x",), ("+y",), ("+z",), ("-x",), ("-y",), ("-z",))),
    ((0, 1, 0, 2, 1, 1), 24, 1, (("+x",), ("+y",), ("+z",), ("-x",), ("-y",), ("-z",))),
    ((0, 1, 1, 1, 1, 2), 24, 1, (("+x",), ("+y",), ("+z",), ("-x",), ("-y",), ("-z",))),
    ((0, 2, 1, 1, 1, 1), 6, 4, (("+x",), ("+y", "-y", "+z", "-z"), ("-x",))),
    ((1, 1, 1, 1, 1, 2), 6, 4, (("+x", "-x", "+y", "-y"), ("+z",), ("-z",))),
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


def transpose(matrix: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def direction_index(vector: tuple[int, int, int]) -> int:
    return DIRS.index(vector)


def multiply(
    left: tuple[tuple[int, int, int], ...],
    right: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def act_shell(
    matrix: tuple[tuple[int, int, int], ...],
    shell: tuple[int, ...],
) -> tuple[int, ...]:
    inverse = transpose(matrix)
    return tuple(shell[direction_index(apply(inverse, direction))] for direction in DIRS)


def act_direction(matrix: tuple[tuple[int, int, int], ...], index: int) -> int:
    return direction_index(apply(matrix, DIRS[index]))


def permutation(matrix: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    return tuple(act_direction(matrix, index) for index in range(6))


def cycle_count(perm: tuple[int, ...]) -> tuple[int, int]:
    seen: set[int] = set()
    count = 0
    fixed = 0
    for start in range(6):
        if start in seen:
            continue
        count += 1
        length = 0
        cursor = start
        while cursor not in seen:
            seen.add(cursor)
            cursor = perm[cursor]
            length += 1
        if length == 1:
            fixed += 1
    return count, fixed


def one_blank_shells() -> list[tuple[int, ...]]:
    shells = []
    for blank in range(6):
        for bits in product((0, 1), repeat=5):
            shell = [0] * 6
            cursor = 0
            for index in range(6):
                if index == blank:
                    shell[index] = BLANK
                else:
                    shell[index] = bits[cursor]
                    cursor += 1
            shells.append(tuple(shell))
    return shells


def shell_orbits(
    group: list[tuple[tuple[int, int, int], ...]],
    shells: list[tuple[int, ...]],
) -> list[set[tuple[int, ...]]]:
    pending = set(shells)
    orbits = []
    while pending:
        start = min(pending)
        orbit: set[tuple[int, ...]] = set()
        stack = [start]
        while stack:
            shell = stack.pop()
            if shell in orbit:
                continue
            orbit.add(shell)
            for matrix in group:
                stack.append(act_shell(matrix, shell))
        pending -= orbit
        orbits.append(orbit)
    return orbits


def stabilizer(
    group: list[tuple[tuple[int, int, int], ...]],
    shell: tuple[int, ...],
) -> list[tuple[tuple[int, int, int], ...]]:
    return [matrix for matrix in group if act_shell(matrix, shell) == shell]


def output_orbits(
    stab: list[tuple[tuple[int, int, int], ...]],
) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    orbits = []
    for start in range(6):
        if start in seen:
            continue
        orbit: set[int] = set()
        stack = [start]
        while stack:
            index = stack.pop()
            if index in orbit:
                continue
            orbit.add(index)
            for matrix in stab:
                stack.append(act_direction(matrix, index))
        seen |= orbit
        orbits.append(tuple(sorted(orbit)))
    return orbits


def named(orbits: list[tuple[int, ...]]) -> tuple[tuple[str, ...], ...]:
    return tuple(sorted(tuple(NAMES[index] for index in orbit) for orbit in orbits))


def uniform(orbit: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(1 if index in orbit else 0 for index in range(6))


def support_size(masses: tuple[int, ...]) -> int:
    return sum(masses)


def moved(matrix: tuple[tuple[int, int, int], ...], masses: tuple[int, ...]) -> tuple[int, ...]:
    image = [0, 0, 0, 0, 0, 0]
    for index, mass in enumerate(masses):
        image[act_direction(matrix, index)] = mass
    return tuple(image)


def invariant(stab: list[tuple[tuple[int, int, int], ...]], masses: tuple[int, ...]) -> bool:
    return all(moved(matrix, masses) == masses for matrix in stab)


def antipode(index: int) -> int:
    return index ^ 1


def opposite_pairs(shell: tuple[int, ...], blank: int) -> tuple[tuple[int, int], tuple[int, int]]:
    pairs = []
    for index in range(6):
        partner = antipode(index)
        if index < partner and index != blank and partner != blank:
            pairs.append((shell[index], shell[partner]))
    return pairs[0], pairs[1]


def main() -> None:
    checks = Checks()
    group = proper_group()
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    quarter_z = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
    half_z = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
    three_z = ((0, 1, 0), (-1, 0, 0), (0, 0, 1))
    products = {multiply(left, right) for left in group for right in group}
    checks.check(
        "the proper cubic group has 24 determinant-1 elements and is closed",
        len(group) == 24
        and len(set(group)) == 24
        and identity in group
        and quarter_z in group
        and half_z in group
        and three_z in group
        and products == set(group)
        and all(det(matrix) == 1 for matrix in group)
        and all(apply(matrix, direction) in DIRS for matrix in group for direction in DIRS),
    )

    axis_ok = True
    for index, direction in enumerate(DIRS):
        fixers = [matrix for matrix in group if apply(matrix, direction) == direction]
        axis_ok = axis_ok and (
            len(fixers) == 4
            and all(apply(matrix, DIRS[antipode(index)]) == DIRS[antipode(index)] for matrix in fixers)
        )
    plus_z = DIRS[NAMES.index("+z")]
    minus_z = DIRS[NAMES.index("-z")]
    z_fixers = [matrix for matrix in group if apply(matrix, plus_z) == plus_z]
    checks.check(
        "four proper rotations fix each direction, and each of those fixes its antipode",
        axis_ok
        and set(z_fixers) == {identity, quarter_z, half_z, three_z}
        and all(apply(matrix, minus_z) == minus_z for matrix in z_fixers)
        and len({apply(matrix, plus_z) for matrix in group}) == 6,
    )

    shells = one_blank_shells()
    orbits = shell_orbits(group, shells)
    by_rep = {min(orbit): orbit for orbit in orbits}
    burnside = 0
    for matrix in group:
        count, fixed = cycle_count(permutation(matrix))
        if fixed:
            burnside += fixed * (2 ** (count - 1))
    stab_sum = sum(len(stabilizer(group, shell)) for shell in shells)
    checks.check(
        "enumeration and the Burnside average both give 12 orbits of the 192 shells",
        len(shells) == 192
        and len(set(shells)) == 192
        and all(shell.count(BLANK) == 1 for shell in shells)
        and len(orbits) == 12
        and burnside == 12 * 24
        and stab_sum == burnside
        and sum(len(orbit) for orbit in orbits) == 192,
    )

    table_ok = True
    for shell, orbit_size, stab_order, expected_orbits in EXPECTED:
        stab = stabilizer(group, shell)
        found = named(output_orbits(stab))
        table_ok = table_ok and (
            shell in by_rep
            and len(by_rep[shell]) == orbit_size
            and len(stab) == stab_order
            and orbit_size * stab_order == 24
            and found == tuple(sorted(expected_orbits))
        )
    checks.check(
        "the twelve representatives have the stated shell orbits, stabilizers, and output orbits",
        table_ok and set(by_rep) == {shell for shell, *_rest in EXPECTED},
    )

    class_ok = True
    type_counts = {(4, 1, 1): 0, (2, 2, 1, 1): 0, (1, 1, 1, 1, 1, 1): 0}
    orbit_stab_ok = True
    for shell in shells:
        blank = shell.index(BLANK)
        stab = stabilizer(group, shell)
        orbits_here = output_orbits(stab)
        sizes = tuple(sorted((len(orbit) for orbit in orbits_here), reverse=True))
        left, right = opposite_pairs(shell, blank)
        monochrome = left[0] == left[1] and right[0] == right[1]
        if monochrome and left[0] == right[0]:
            predicted = 4
        elif monochrome:
            predicted = 2
        else:
            predicted = 1
        singletons = [orbit for orbit in orbits_here if len(orbit) == 1]
        class_ok = class_ok and (
            len(stab) == predicted
            and (blank,) in orbits_here
            and (antipode(blank),) in orbits_here
            and len(singletons) != 1
            and sizes != (1,)
            and len(orbits_here) >= 3
            and sizes in type_counts
        )
        if sizes in type_counts and class_ok:
            type_counts[sizes] += 1
        own = next(orbit for orbit in orbits if shell in orbit)
        orbit_stab_ok = orbit_stab_ok and len(stab) * len(own) == 24
    checks.check(
        "every shell stabilizer fixes the blank and its antipode, and the three output types partition the shells",
        class_ok
        and orbit_stab_ok
        and type_counts[(4, 1, 1)] == 24
        and type_counts[(2, 2, 1, 1)] == 24
        and type_counts[(1, 1, 1, 1, 1, 1)] == 144,
    )

    constant_equator = (0, 0, 0, 0, 0, 2)
    stab_equator = stabilizer(group, constant_equator)
    equator_orbits = output_orbits(stab_equator)
    blank_mass = uniform((constant_equator.index(BLANK),))
    anti_mass = uniform((antipode(constant_equator.index(BLANK)),))
    equatorial_mass = uniform((NAMES.index("+x"),))
    checks.check(
        "a constant equator admits both pole point masses and rejects an equatorial point mass",
        sorted(len(orbit) for orbit in equator_orbits) == [1, 1, 4]
        and blank_mass != anti_mass
        and invariant(stab_equator, blank_mass)
        and invariant(stab_equator, anti_mass)
        and support_size(blank_mass) == 1
        and not invariant(stab_equator, equatorial_mass)
        and any(support_size(uniform(orbit)) == 4 for orbit in equator_orbits),
    )

    split_pairs = (0, 0, 1, 1, 1, 2)
    stab_pairs = stabilizer(group, split_pairs)
    pair_orbits = output_orbits(stab_pairs)
    checks.check(
        "unequal opposite pairs admit both pole point masses and reject an equatorial point mass",
        sorted(len(orbit) for orbit in pair_orbits) == [1, 1, 2, 2]
        and invariant(stab_pairs, uniform((split_pairs.index(BLANK),)))
        and invariant(stab_pairs, uniform((antipode(split_pairs.index(BLANK)),)))
        and not invariant(stab_pairs, uniform((NAMES.index("+x"),)))
        and any(support_size(uniform(orbit)) == 2 for orbit in pair_orbits),
    )

    trivial = (0, 0, 0, 1, 0, 2)
    stab_trivial = stabilizer(group, trivial)
    trivial_points = [uniform((index,)) for index in range(6)]
    checks.check(
        "a trivial stabilizer admits all six point masses and does not identify them",
        len(stab_trivial) == 1
        and all(invariant(stab_trivial, masses) for masses in trivial_points)
        and len(set(trivial_points)) == 6
        and support_size(trivial_points[0]) == 1,
    )

    pair_ok = True
    for shell in shells:
        blank = shell.index(BLANK)
        stab = stabilizer(group, shell)
        on_blank = uniform((blank,))
        on_anti = uniform((antipode(blank),))
        pair_ok = pair_ok and (
            on_blank != on_anti
            and invariant(stab, on_blank)
            and invariant(stab, on_anti)
            and len(output_orbits(stab)) >= 3
        )
    checks.check(
        "no one-blank shell has a unique invariant law, and both pole point masses are invariant",
        pair_ok,
    )

    complement_ok = True
    for shell in shells:
        flipped = tuple(BLANK if value == BLANK else 1 - value for value in shell)
        left = named(output_orbits(stabilizer(group, shell)))
        right = named(output_orbits(stabilizer(group, flipped)))
        complement_ok = complement_ok and shell.count(BLANK) == flipped.count(BLANK) and left == right
    checks.check(
        "swapping 0 with 1 and leaving the blank fixed preserves the output orbits",
        complement_ok,
    )

    transport_ok = True
    for shell in shells:
        blank = shell.index(BLANK)
        for masses in (uniform((blank,)), uniform((antipode(blank),))):
            images: dict[tuple[int, ...], tuple[int, ...]] = {}
            for matrix in group:
                image_shell = act_shell(matrix, shell)
                image_masses = moved(matrix, masses)
                previous = images.get(image_shell)
                if previous is None:
                    images[image_shell] = image_masses
                elif previous != image_masses:
                    transport_ok = False
                if image_shell.count(BLANK) != 1:
                    transport_ok = False
                if not invariant(stabilizer(group, image_shell), image_masses):
                    transport_ok = False
                if masses == uniform((blank,)) and image_masses != uniform((image_shell.index(BLANK),)):
                    transport_ok = False
                if masses == uniform((antipode(blank),)) and image_masses != uniform(
                    (antipode(image_shell.index(BLANK)),)
                ):
                    transport_ok = False
    checks.check(
        "the blank point mass and the antipode point mass each transport to one covariant law",
        transport_ok,
    )

    orbit_transport_ok = True
    for shell, _orbit_size, _stab_order, _expected in EXPECTED:
        stab = stabilizer(group, shell)
        for orbit in output_orbits(stab):
            masses = uniform(orbit)
            images = {}
            for matrix in group:
                image_shell = act_shell(matrix, shell)
                image_masses = moved(matrix, masses)
                previous = images.get(image_shell)
                if previous is None:
                    images[image_shell] = image_masses
                elif previous != image_masses:
                    orbit_transport_ok = False
                if not invariant(stabilizer(group, image_shell), image_masses):
                    orbit_transport_ok = False
            if len({moved(matrix, masses) for matrix in stab}) != 1:
                orbit_transport_ok = False
    checks.check(
        "each uniform-on-one-output-orbit law transports to one stabilizer-invariant law",
        orbit_transport_ok,
    )

    bad_images = {
        moved(matrix, equatorial_mass)
        for matrix in group
        if act_shell(matrix, constant_equator) == constant_equator
    }
    checks.check(
        "an equatorial point mass on the constant-equator shell is not well defined under the stabilizer",
        len(bad_images) > 1,
    )

    print(
        "per_element: checked all 192 one-blank shells, all 6 directions, and all 24 proper rotations"
    )
    print(
        "per_site: the shell is one site's neighbor tuple; no second site and no site selector was enumerated"
    )
    print(
        "per_mode: one output action, the soldered six-direction menu; the unsoldered two-label menu was not enumerated"
    )
    print(
        "per_block: exactly one blank direction; fully recorded binary shells and shells with two or more blanks were not enumerated"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")


if __name__ == "__main__":
    main()
