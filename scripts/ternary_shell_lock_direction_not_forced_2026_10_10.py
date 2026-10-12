#!/usr/bin/env python3
"""Which ternary six-neighbor shells force one locked direction.

Each of the six axis directions is in {0, 1, blank}. The proper cubic
group permutes the six directions. The output menu is those same six
directions. No bond factor, no 3x3 correlation, no deleted-blank menu,
no site selector, and no rate.
"""

from __future__ import annotations

from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/TERNARY_SHELL_LOCK_DIRECTION_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-10.md',)

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
CONSTANTS = (
    (0, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1),
    (BLANK, BLANK, BLANK, BLANK, BLANK, BLANK),
)
# Descending output-orbit sizes. Counts are shells, not orbits.
TYPE_COUNTS = {
    (6,): 3,
    (4, 2): 18,
    (3, 3): 24,
    (4, 1, 1): 54,
    (2, 2, 2): 114,
    (2, 2, 1, 1): 108,
    (1, 1, 1, 1, 1, 1): 408,
}
SINGLETON_COUNTS = {0: 159, 2: 162, 6: 408}


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


def cycle_count(perm: tuple[int, ...]) -> int:
    seen: set[int] = set()
    count = 0
    for start in range(6):
        if start in seen:
            continue
        count += 1
        cursor = start
        while cursor not in seen:
            seen.add(cursor)
            cursor = perm[cursor]
    return count


def fixed_directions(matrix: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    return tuple(index for index in range(6) if act_direction(matrix, index) == index)


def antipode(index: int) -> int:
    return index ^ 1


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


def output_type(orbits: list[tuple[int, ...]]) -> tuple[int, ...]:
    return tuple(sorted((len(orbit) for orbit in orbits), reverse=True))


def uniform(orbit: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(1 if index in orbit else 0 for index in range(6))


def moved(matrix: tuple[tuple[int, int, int], ...], masses: tuple[int, ...]) -> tuple[int, ...]:
    image = [0, 0, 0, 0, 0, 0]
    for index, mass in enumerate(masses):
        image[act_direction(matrix, index)] = mass
    return tuple(image)


def invariant(stab: list[tuple[tuple[int, int, int], ...]], masses: tuple[int, ...]) -> bool:
    return all(moved(matrix, masses) == masses for matrix in stab)


def shell_text(shell: tuple[int, ...]) -> str:
    return "".join("b" if value == BLANK else str(value) for value in shell)


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

    fixed_ok = fixed_directions(identity) == tuple(range(6))
    for matrix in group:
        fixed = fixed_directions(matrix)
        if matrix == identity:
            continue
        fixed_ok = fixed_ok and len(fixed) in (0, 2)
        if len(fixed) == 2:
            fixed_ok = fixed_ok and antipode(fixed[0]) == fixed[1]
    z_fixers = [matrix for matrix in group if act_direction(matrix, NAMES.index("+z")) == NAMES.index("+z")]
    checks.check(
        "every non-identity rotation fixes at most one antipodal pair",
        fixed_ok
        and set(z_fixers) == {identity, quarter_z, half_z, three_z}
        and all(act_direction(matrix, NAMES.index("-z")) == NAMES.index("-z") for matrix in z_fixers)
        and len({act_direction(matrix, NAMES.index("+z")) for matrix in group}) == 6,
    )

    shells = list(product((0, 1, BLANK), repeat=6))
    orbits = shell_orbits(group, shells)
    by_rep = {min(orbit): orbit for orbit in orbits}
    burnside = sum(3 ** cycle_count(permutation(matrix)) for matrix in group)
    orbit_stab_ok = True
    for shell in shells:
        own = next(orbit for orbit in orbits if shell in orbit)
        orbit_stab_ok = orbit_stab_ok and len(stabilizer(group, shell)) * len(own) == 24
    checks.check(
        "enumeration and the Burnside average both give 57 orbits of the 729 shells",
        len(shells) == 729
        and len(set(shells)) == 729
        and len(orbits) == 57
        and burnside == 57 * 24
        and burnside == 1368
        and sum(len(orbit) for orbit in orbits) == 729
        and orbit_stab_ok,
    )

    found_types: dict[tuple[int, ...], int] = {}
    type_ok = True
    for shell in shells:
        sizes = output_type(output_orbits(stabilizer(group, shell)))
        found_types[sizes] = found_types.get(sizes, 0) + 1
        type_ok = type_ok and sum(sizes) == 6 and sizes != (1,)
    checks.check(
        "seven output types partition the shells, and none has type (1,)",
        type_ok and found_types == TYPE_COUNTS and (1,) not in found_types,
    )

    singleton_found = {0: 0, 2: 0, 6: 0}
    singleton_ok = True
    for shell in shells:
        stab = stabilizer(group, shell)
        orbits_here = output_orbits(stab)
        singletons = tuple(orbit[0] for orbit in orbits_here if len(orbit) == 1)
        count = len(singletons)
        singleton_ok = singleton_ok and count in SINGLETON_COUNTS
        if count in singleton_found:
            singleton_found[count] += 1
        singleton_ok = singleton_ok and all(antipode(index) in singletons for index in singletons)
        singleton_ok = singleton_ok and (count == 6) == (len(stab) == 1)
        singleton_ok = singleton_ok and count != 1
    checks.check(
        "singleton output orbits are an antipodal pair, all six, or none",
        singleton_ok and singleton_found == SINGLETON_COUNTS,
    )

    unique = []
    unique_ok = True
    for shell in shells:
        stab = stabilizer(group, shell)
        orbits_here = output_orbits(stab)
        if len(orbits_here) == 1:
            unique.append(shell)
            reached = {act_direction(matrix, 0) for matrix in stab}
            unique_ok = unique_ok and (
                len(orbits_here[0]) == 6
                and len(stab) == 24
                and reached == set(range(6))
                and output_type(orbits_here) == (6,)
            )
    checks.check(
        "the unique-invariant shells are exactly 000000, 111111, and bbbbbb",
        unique_ok
        and set(unique) == set(CONSTANTS)
        and len(unique) == 3
        and [shell_text(shell) for shell in unique] == ["000000", "111111", "bbbbbb"],
    )

    uniform_mass = (1, 1, 1, 1, 1, 1)
    point = uniform((0,))
    constant_ok = True
    for shell in CONSTANTS:
        stab = stabilizer(group, shell)
        constant_ok = constant_ok and (
            by_rep[shell] == {shell}
            and invariant(stab, uniform_mass)
            and not invariant(stab, point)
            and len({moved(matrix, point) for matrix in stab}) == 6
        )
    checks.check(
        "each constant shell forces the uniform law and rejects a point mass",
        constant_ok and len({min(by_rep[shell]) for shell in CONSTANTS}) == 3,
    )

    partial_blanks = [shell for shell in shells if 1 <= shell.count(BLANK) <= 5]
    partial_ok = all(len(output_orbits(stabilizer(group, shell))) >= 2 for shell in partial_blanks)
    checks.check(
        "no shell with one through five blanks has a unique invariant law",
        partial_ok
        and len(partial_blanks) == 664
        and sum(1 for shell in unique if shell.count(BLANK) == 0) == 2
        and sum(1 for shell in unique if shell.count(BLANK) == 6) == 1,
    )

    five_blank = [shell for shell in shells if shell.count(BLANK) == 5]
    witness = (BLANK, BLANK, BLANK, BLANK, 0, BLANK)
    witness_stab = stabilizer(group, witness)
    witness_orbits = output_orbits(witness_stab)
    plus_z = uniform((NAMES.index("+z"),))
    minus_z = uniform((NAMES.index("-z"),))
    plus_x = uniform((NAMES.index("+x"),))
    five_types = {output_type(output_orbits(stabilizer(group, shell))) for shell in five_blank}
    checks.check(
        "a single recorded direction leaves its blank antipode as a second point mass",
        five_types == {(4, 1, 1)}
        and len(five_blank) == 12
        and witness in five_blank
        and shell_text(witness) == "bbbb0b"
        and sorted(len(orbit) for orbit in witness_orbits) == [1, 1, 4]
        and invariant(witness_stab, plus_z)
        and invariant(witness_stab, minus_z)
        and plus_z != minus_z
        and not invariant(witness_stab, plus_x),
    )

    swap_ok = True
    for shell in shells:
        flipped = tuple(BLANK if value == BLANK else 1 - value for value in shell)
        left = output_type(output_orbits(stabilizer(group, shell)))
        right = output_type(output_orbits(stabilizer(group, flipped)))
        swap_ok = swap_ok and left == right
    checks.check(
        "swapping 0 with 1 and leaving blanks fixed preserves the output type",
        swap_ok,
    )

    mono_ok = True
    for shell in shells:
        orbits_here = output_orbits(stabilizer(group, shell))
        for orbit in orbits_here:
            colors = {shell[index] for index in orbit}
            mono_ok = mono_ok and len(colors) == 1
        mono_ok = mono_ok and len(orbits_here) >= len(set(shell))
    checks.check(
        "every output orbit is monochromatic, so one orbit requires one color",
        mono_ok,
    )

    def nonblank(shell: tuple[int, ...]) -> int:
        return next(index for index, value in enumerate(shell) if value != BLANK)

    def on_antipode(shell: tuple[int, ...]) -> int:
        return antipode(nonblank(shell))

    def transports(selector) -> bool:
        ok = True
        for shell in five_blank:
            masses = uniform((selector(shell),))
            images: dict[tuple[int, ...], tuple[int, ...]] = {}
            for matrix in group:
                image_shell = act_shell(matrix, shell)
                image_masses = moved(matrix, masses)
                previous = images.get(image_shell)
                if previous is None:
                    images[image_shell] = image_masses
                elif previous != image_masses:
                    ok = False
                if image_masses != uniform((selector(image_shell),)):
                    ok = False
                if not invariant(stabilizer(group, image_shell), image_masses):
                    ok = False
            if len(images) != 6:
                ok = False
        return ok

    checks.check(
        "on five-blank shells both pole point masses transport, and they disagree",
        transports(nonblank)
        and transports(on_antipode)
        and all(uniform((nonblank(shell),)) != uniform((on_antipode(shell),)) for shell in five_blank),
    )

    print(
        "per_element: checked all 729 ternary shells, all 6 directions, and all 24 proper rotations"
    )
    print(
        "per_site: the shell is one site's neighbor tuple; no second site and no site selector was enumerated"
    )
    print(
        "per_mode: one output action, the soldered six-direction menu; blanks stay colors on that menu"
    )
    print(
        "per_block: the full alphabet {0, 1, blank}; no bond factor and no deleted-blank menu"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
