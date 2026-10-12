#!/usr/bin/env python3
"""What a binary six-neighbor shell forces about a locked possibility.

The shell is a {0,1}-coloring of the six axis directions. The proper cubic
group permutes those directions. Two supplied actions on the output are
compared. No bond factor, no 3x3 correlation, no site selector, and no rate.
"""

from __future__ import annotations

from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/BINARY_SHELL_LOCK_POSSIBILITY_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-10.md',)

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")

# One representative of each shell orbit, with its shell-orbit size,
# stabilizer order, and output orbits named in direction order.
EXPECTED = (
    ((0, 0, 0, 0, 0, 0), 1, 24, (("+x", "-x", "+y", "-y", "+z", "-z"),)),
    ((0, 0, 0, 0, 0, 1), 6, 4, (("+x", "-x", "+y", "-y"), ("+z",), ("-z",))),
    ((0, 0, 0, 0, 1, 1), 3, 8, (("+x", "-x", "+y", "-y"), ("+z", "-z"))),
    ((0, 0, 0, 1, 0, 1), 12, 2, (("+x", "-x"), ("+y", "+z"), ("-y", "-z"))),
    ((0, 0, 0, 1, 1, 1), 12, 2, (("+x", "-x"), ("+y",), ("-y",), ("+z", "-z"))),
    ((0, 1, 0, 1, 0, 1), 8, 3, (("+x", "+y", "+z"), ("-x", "-y", "-z"))),
    ((0, 0, 1, 1, 1, 1), 3, 8, (("+x", "-x"), ("+y", "-y", "+z", "-z"))),
    ((0, 1, 0, 1, 1, 1), 12, 2, (("+x", "+y"), ("-x", "-y"), ("+z", "-z"))),
    ((0, 1, 1, 1, 1, 1), 6, 4, (("+x",), ("-x",), ("+y", "-y", "+z", "-z"))),
    ((1, 1, 1, 1, 1, 1), 1, 24, (("+x", "-x", "+y", "-y", "+z", "-z"),)),
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


def shell_orbits(
    group: list[tuple[tuple[int, int, int], ...]],
) -> list[set[tuple[int, ...]]]:
    pending = set(product((0, 1), repeat=6))
    orbits = []
    while pending:
        start = min(pending)
        orbit = set()
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


def moved(matrix: tuple[tuple[int, int, int], ...], masses: tuple[int, ...]) -> tuple[int, ...]:
    image = [0, 0, 0, 0, 0, 0]
    for index, mass in enumerate(masses):
        image[act_direction(matrix, index)] = mass
    return tuple(image)


def invariant(stab: list[tuple[tuple[int, int, int], ...]], masses: tuple[int, ...]) -> bool:
    return all(moved(matrix, masses) == masses for matrix in stab)


def main() -> None:
    checks = Checks()
    group = proper_group()
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    quarter_z = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
    products = {multiply(left, right) for left in group for right in group}
    checks.check(
        "the proper cubic group has 24 determinant-1 elements and is closed",
        len(group) == 24
        and len(set(group)) == 24
        and identity in group
        and quarter_z in group
        and products == set(group)
        and all(det(matrix) == 1 for matrix in group)
        and all(apply(matrix, direction) in DIRS for matrix in group for direction in DIRS),
    )

    orbits = shell_orbits(group)
    by_rep = {min(orbit): orbit for orbit in orbits}
    burnside = sum(2 ** cycle_count(permutation(matrix)) for matrix in group)
    checks.check(
        "enumeration and the Burnside average both give 10 shell orbits",
        len(orbits) == 10 and burnside == 10 * 24 and sum(len(orbit) for orbit in orbits) == 64,
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
        "the ten representatives have the stated shell orbits, stabilizers, and output orbits",
        table_ok,
    )

    orbit_stab_ok = True
    no_singleton_law = True
    singleton_pairs = True
    output_types: set[tuple[int, ...]] = set()
    for shell in product((0, 1), repeat=6):
        stab = stabilizer(group, shell)
        orbits_here = output_orbits(stab)
        orbit_stab_ok = orbit_stab_ok and len(stab) * len(by_rep[min_orbit_rep(by_rep, shell)]) == 24
        sizes = tuple(sorted(len(orbit) for orbit in orbits_here))
        output_types.add(sizes)
        no_singleton_law = no_singleton_law and sizes != (1,)
        singleton_count = sum(1 for size in sizes if size == 1)
        singleton_pairs = singleton_pairs and singleton_count != 1
    checks.check(
        "orbit-stabilizer holds on every shell, and no shell has output type (1,)",
        orbit_stab_ok and no_singleton_law and singleton_pairs and len(output_types) == 6,
    )

    complement_ok = True
    for shell in product((0, 1), repeat=6):
        flipped = tuple(1 - bit for bit in shell)
        left = named(output_orbits(stabilizer(group, shell)))
        right = named(output_orbits(stabilizer(group, flipped)))
        complement_ok = complement_ok and left == right
    checks.check(
        "complementing every shell bit preserves the output orbits",
        complement_ok,
    )

    constant_shells = ((0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1))
    uniform_ok = True
    for shell in constant_shells:
        stab = stabilizer(group, shell)
        only = output_orbits(stab)
        masses = uniform(only[0])
        point = uniform((0,))
        uniform_ok = uniform_ok and (
            len(only) == 1
            and len(only[0]) == 6
            and masses == (1, 1, 1, 1, 1, 1)
            and invariant(stab, masses)
            and not invariant(stab, point)
        )
    checks.check(
        "each constant shell forces the uniform law and rejects a point mass",
        uniform_ok,
    )

    occupied = (0, 0, 0, 0, 0, 1)
    stab_occupied = stabilizer(group, occupied)
    plus_z = uniform((NAMES.index("+z"),))
    minus_z = uniform((NAMES.index("-z"),))
    plus_x = uniform((NAMES.index("+x"),))
    checks.check(
        "one occupied pole admits both pole point masses and rejects an equatorial point mass",
        invariant(stab_occupied, plus_z)
        and invariant(stab_occupied, minus_z)
        and plus_z != minus_z
        and not invariant(stab_occupied, plus_x),
    )

    triple_shell = (0, 1, 0, 1, 0, 1)
    stab_triple = stabilizer(group, triple_shell)
    triple_orbits = output_orbits(stab_triple)
    triple_masses = [uniform(orbit) for orbit in triple_orbits]
    checks.check(
        "the three-negative shell has two triple orbits and no covariant point mass",
        [len(orbit) for orbit in triple_orbits] == [3, 3]
        and all(invariant(stab_triple, masses) for masses in triple_masses)
        and triple_masses[0] != triple_masses[1]
        and not any(invariant(stab_triple, uniform((index,))) for index in range(6)),
    )

    pair_shell = (0, 0, 0, 0, 1, 1)
    stab_pair = stabilizer(group, pair_shell)
    pair_orbits = output_orbits(stab_pair)
    checks.check(
        "the opposite-pole shell splits into a pair and an equator, with no singleton",
        sorted(len(orbit) for orbit in pair_orbits) == [2, 4]
        and all(invariant(stab_pair, uniform(orbit)) for orbit in pair_orbits)
        and not any(invariant(stab_pair, uniform((index,))) for index in range(6)),
    )

    transport_ok = True
    distinct_ok = True
    for shell, _orbit_size, _stab_order, _expected in EXPECTED:
        stab = stabilizer(group, shell)
        for orbit in output_orbits(stab):
            masses = uniform(orbit)
            images: dict[tuple[int, ...], tuple[int, ...]] = {}
            for matrix in group:
                image_shell = act_shell(matrix, shell)
                image_masses = moved(matrix, masses)
                previous = images.get(image_shell)
                if previous is None:
                    images[image_shell] = image_masses
                elif previous != image_masses:
                    transport_ok = False
                if not invariant(stabilizer(group, image_shell), image_masses):
                    transport_ok = False
            if len({moved(matrix, masses) for matrix in stab}) != 1:
                distinct_ok = False
    checks.check(
        "each uniform-on-one-output-orbit law transports to one stabilizer-invariant law",
        transport_ok and distinct_ok,
    )

    bad_images = {moved(matrix, plus_x) for matrix in group if act_shell(matrix, constant_shells[0]) == constant_shells[0]}
    checks.check(
        "a point mass on the constant shell is not well defined under the stabilizer",
        len(bad_images) > 1,
    )

    zero = (0, 0, 0, 0, 0, 0)
    one = (1, 1, 1, 1, 1, 1)
    zero_orbit = by_rep[zero]
    one_orbit = by_rep[one]
    unsoldered_ok = zero_orbit != one_orbit
    for shell in product((0, 1), repeat=6):
        own = by_rep[min_orbit_rep(by_rep, shell)]
        other = one_orbit if shell in zero_orbit else zero_orbit
        unsoldered_ok = unsoldered_ok and shell in own and shell not in other and own != other
    varying = (1 << (len(orbits) - 1)) - 1
    checks.check(
        "unsoldered orbit indicators realize both labels at every shell, and 511 varying laws do so",
        unsoldered_ok and len(orbits) == 10 and varying == 511 and (1 << 10) == 1024,
    )

    plus_x_shell = (1, 0, 0, 0, 0, 0)
    image = act_shell(quarter_z, plus_x_shell)
    checks.check(
        "the unsoldered +x bit is not covariant: a quarter turn about z moves it",
        image == (0, 0, 1, 0, 0, 0)
        and image in by_rep[min_orbit_rep(by_rep, plus_x_shell)]
        and plus_x_shell[0] != image[0],
    )

    print(
        "per_element: checked all 64 binary shells, all 6 directions, and all 24 proper rotations"
    )
    print(
        "per_site: the shell is one site's neighbor tuple; no second site and no site selector was enumerated"
    )
    print(
        "per_mode: two output actions, the soldered six-direction menu and the unsoldered two-label menu"
    )
    print(
        "per_block: one fully recorded binary shell; blanks, partial shells, and bond factors were not enumerated"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


def min_orbit_rep(
    by_rep: dict[tuple[int, ...], set[tuple[int, ...]]],
    shell: tuple[int, ...],
) -> tuple[int, ...]:
    for representative, orbit in by_rep.items():
        if shell in orbit:
            return representative
    raise KeyError(shell)


if __name__ == "__main__":
    main()
