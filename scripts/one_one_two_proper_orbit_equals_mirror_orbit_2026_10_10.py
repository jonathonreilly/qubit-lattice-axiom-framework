#!/usr/bin/env python3
"""Proper orbit of the record (1, 1, 2) against one improper mirror.

The comparison is the signed-permutation action already used for (0, 1, 2).
The proper cubic matrices are the determinant +1 elements. The full set has
48 elements. This count does not select a law, a mass, a site, or a rate,
and it does not enumerate the orbit of (1, 2, 2).
"""

from __future__ import annotations

from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120

SEED = (1, 1, 2)
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
# Swap of the two axes that carry absolute value 1. Improper, and it fixes SEED.
UNIT_SWAP = ((0, 1, 0), (1, 0, 0), (0, 0, 1))
# The improper mirror that fixes (0, 1, 2). It does not fix SEED.
ZERO_AXIS_MIRROR = ((-1, 0, 0), (0, 1, 0), (0, 0, 1))
# Even permutation, positive signs: (1, 1, 2) -> (2, 1, 1).
CYCLE = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
# Proper 180 degree rotation about (1, 1, 0): (1, 1, 2) -> (1, 1, -2).
SIGN_FLIP = ((0, 1, 0), (1, 0, 0), (0, 0, -1))


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


def det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def apply(
    matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def matmul(
    left: tuple[tuple[int, int, int], ...],
    right: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def transpose(
    matrix: tuple[tuple[int, int, int], ...]
) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def signed_permutations() -> list[tuple[tuple[int, int, int], ...]]:
    group = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            rows = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                rows[i][perm[i]] = signs[i]
            group.append(tuple(tuple(row) for row in rows))
    return group


def absolute_patterns() -> set[tuple[int, int, int]]:
    patterns = set()
    for axis in range(3):
        for signs in product((1, -1), repeat=3):
            vector = [0, 0, 0]
            vector[axis] = 2 * signs[axis]
            for other in range(3):
                if other != axis:
                    vector[other] = signs[other]
            patterns.add(tuple(vector))
    return patterns


def main() -> None:
    checks = Checks()
    full = signed_permutations()
    full_set = set(full)
    proper = [matrix for matrix in full if det3(matrix) == 1]
    improper = [matrix for matrix in full if det3(matrix) == -1]
    proper_set = set(proper)

    closed = all(matmul(left, right) in full_set for left in full for right in full)
    inverses = all(matmul(matrix, transpose(matrix)) == IDENTITY for matrix in full)
    proper_closed = all(matmul(left, right) in proper_set for left in proper for right in proper)
    proper_inverses = all(transpose(matrix) in proper_set for matrix in proper)
    checks.check(
        "signed permutations form a group of order 48, with a determinant +1 subgroup of order 24",
        len(full) == 48
        and len(full_set) == 48
        and len(proper) == 24
        and len(proper_set) == 24
        and len(improper) == 24
        and IDENTITY in proper_set
        and closed
        and inverses
        and proper_closed
        and proper_inverses
        and all(det3(matrix) == 1 for matrix in proper)
        and all(det3(matrix) == -1 for matrix in improper),
    )

    proper_orbit = {apply(matrix, SEED) for matrix in proper}
    full_orbit = {apply(matrix, SEED) for matrix in full}
    checks.check(
        "proper orbit of (1, 1, 2) has 24 points and equals the full signed-permutation orbit",
        len(proper_orbit) == 24 and proper_orbit == full_orbit,
    )

    transported = all(
        det3(matmul(matrix, UNIT_SWAP)) == 1
        and apply(matmul(matrix, UNIT_SWAP), SEED) == apply(matrix, SEED)
        for matrix in improper
    )
    checks.check(
        "one improper mirror fixes (1, 1, 2) and carries every improper image into the proper orbit",
        UNIT_SWAP in full_set
        and det3(UNIT_SWAP) == -1
        and apply(UNIT_SWAP, SEED) == SEED
        and transported
        and all(apply(matmul(matrix, UNIT_SWAP), SEED) in proper_orbit for matrix in improper),
    )

    patterns = absolute_patterns()
    checks.check(
        "the orbit is exactly the 24 vectors whose absolute values are 1, 1, and 2",
        patterns == proper_orbit
        and len(patterns) == 24
        and all(sorted(abs(entry) for entry in vector) == [1, 1, 2] for vector in proper_orbit),
    )

    old_image = apply(ZERO_AXIS_MIRROR, SEED)
    checks.check(
        "a proper cycle moves the 2 and a proper matrix flips its sign; the (0, 1, 2) mirror does not fix this seed",
        CYCLE in proper_set
        and apply(CYCLE, SEED) == (2, 1, 1)
        and SIGN_FLIP in proper_set
        and det3(SIGN_FLIP) == 1
        and apply(SIGN_FLIP, SEED) == (1, 1, -2)
        and ZERO_AXIS_MIRROR in full_set
        and det3(ZERO_AXIS_MIRROR) == -1
        and old_image == (-1, 1, 2)
        and old_image != SEED
        and old_image in proper_orbit,
    )

    stabilizer = [matrix for matrix in full if apply(matrix, SEED) == SEED]
    proper_stabilizer = [matrix for matrix in stabilizer if det3(matrix) == 1]
    checks.check(
        "the stabilizer has order 2 with exactly one proper element, and no orbit coordinate is 0",
        len(stabilizer) == 2
        and proper_stabilizer == [IDENTITY]
        and UNIT_SWAP in stabilizer
        and all(0 not in vector for vector in proper_orbit)
        and (0, 1, 2) not in proper_orbit,
    )

    print("seed: (1, 1, 2)")
    print("proper_orbit_size: 24")
    print("full_orbit_size: 24")
    print("orbits_equal: true")
    print("chiral_pair: false")
    print("mirror: [[0, 1, 0], [1, 0, 0], [0, 0, 1]], det -1, fixes (1, 1, 2)")
    print("stabilizer_order: 2")
    print("proper_stabilizer_order: 1")
    print("selected_law: none")
    print("mass_density: not identified")
    print("per_element: one improper mirror in the stabilizer; every improper image is already proper")
    print("per_site: one record triple; no site was selected")
    print("per_mode: set equality of two orbits; the equality was not adopted as a law")
    print("per_block: absolute values 1, 1, 2; the orbit of (1, 2, 2) was not enumerated")
    print("lattice_wide: checked and not executed — no infinite lattice, no formation site, and no formation rate")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
