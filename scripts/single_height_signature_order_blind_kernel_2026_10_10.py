#!/usr/bin/env python3
"""Order-blind kernels supported on one height signature."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md']


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


def bond_key(direction, left, right):
    forward = (direction, left, right)
    backward = (negate(direction), right, left)
    return tuple(sorted((forward, backward)))


def signature(direction, left, right) -> tuple[int, int]:
    forward = (dot(left, direction), dot(right, direction))
    backward = (-forward[1], -forward[0])
    return min(forward, backward)


def rref(rows: list[list[Fraction]], width: int) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [[Fraction(value) for value in row] for row in rows]
    pivots = []
    rank_now = 0
    for col in range(width):
        pivot = next((i for i in range(rank_now, len(matrix)) if matrix[i][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for i in range(len(matrix)):
            if i != rank_now and matrix[i][col] != 0:
                factor = matrix[i][col]
                matrix[i] = [matrix[i][j] - factor * matrix[rank_now][j] for j in range(width)]
        pivots.append(col)
        rank_now += 1
    return matrix[:rank_now], pivots


def kernel_basis(rows: list[tuple[int, ...]], width: int) -> list[list[Fraction]]:
    reduced, pivots = rref([list(row) for row in rows], width)
    basis = []
    for free in [col for col in range(width) if col not in pivots]:
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = Fraction(1)
        for pivot_index, pivot_col in enumerate(pivots):
            vector[pivot_col] = -reduced[pivot_index][free]
        basis.append(vector)
    return basis


def cap(point, direction, level: int) -> int:
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    if point[axis] != direction[axis] * level:
        return 0
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def sign_of(value: int) -> int:
    if value == 0:
        return 0
    return 1 if value > 0 else -1


def cross_raw(orientation: int, swapped: bool, height: int, left, right) -> int:
    if left[2] != orientation * height or right[2] != -orientation * height:
        return 0
    matched = abs(left[0]) == abs(right[0]) and abs(left[1]) == abs(right[1])
    crossed = abs(left[0]) == abs(right[1]) and abs(left[1]) == abs(right[0])
    if swapped and not crossed:
        return 0
    if not swapped and not matched:
        return 0
    value = sign_of(left[0] * right[1] - left[1] * right[0])
    if orientation == -1 and swapped:
        return -value
    return value


def substituted(coeffs: list[Fraction], replace_x: bool) -> tuple[Fraction, Fraction, Fraction]:
    """Restrict x=-z or y=-z and return coefficients of y^2, z^2, yz or x^2, z^2, xz."""
    xx, yy, zz, xy, xz, yz = coeffs
    if replace_x:
        return yy, xx + zz - xz, -xy + yz
    return xx, yy + zz - yz, -xy + xz


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6)
    upward = (0, 0, 1)
    carriers = {
        direction: [matrix for matrix in group if apply(matrix, upward) == direction]
        for direction in axis_steps
    }

    image_of: dict[tuple, int] = {}
    sig_of: dict[int, tuple[int, int]] = {}
    for direction in axis_steps:
        for left in orbit:
            for right in orbit:
                images = frozenset(
                    bond_key(apply(matrix, direction), apply(matrix, left), apply(matrix, right))
                    for matrix in group
                )
                if images not in image_of:
                    image_of[images] = len(sig_of)
                    sample = min(next(iter(images)))
                    sig_of[image_of[images]] = signature(*sample)
                image_of[(direction, left, right)] = image_of[images]
    dimension = len(sig_of)
    by_sig: dict[tuple[int, int], list[int]] = defaultdict(list)
    for index, sig in sig_of.items():
        by_sig[sig].append(index)
    signatures = sorted(by_sig)
    checks.check("height signatures number 21", len(signatures) == 21)
    checks.check(
        "each height signature has four bond orbits",
        all(len(by_sig[sig]) == 4 for sig in signatures),
    )
    checks.check("the signatures partition the 84 bond orbits", dimension == 84)

    slice_rows = []
    seen_rows = set()
    for direction in axis_steps:
        for right in orbit:
            row = [0] * dimension
            for left in orbit:
                row[image_of[(direction, left, right)]] += 1
            key = tuple(row)
            if key not in seen_rows:
                seen_rows.add(key)
                slice_rows.append(key)
    checks.check("six distinct slice rows", len(slice_rows) == 6)

    bases: dict[tuple[int, int], list[list[Fraction]]] = {}
    kernel_dims = []
    for sig in signatures:
        columns = by_sig[sig]
        local = []
        for row in slice_rows:
            packed = tuple(row[index] for index in columns)
            if any(packed):
                local.append(packed)
        bases[sig] = kernel_basis(list(set(local)), len(columns))
        kernel_dims.append(len(bases[sig]))
    checks.check("each signature has kernel dimension 3", kernel_dims == [3] * 21)
    opposite = [sig for sig in signatures if sig[0] == -sig[1]]
    others = [sig for sig in signatures if sig[0] != -sig[1]]
    same_height = [sig for sig in others if sig[0] == sig[1]]
    unequal = [sig for sig in others if sig[0] != sig[1]]
    checks.check("six signatures have opposite heights", len(opposite) == 6)
    checks.check("three signatures have equal heights", len(same_height) == 3)
    checks.check("twelve signatures have unequal non-opposite heights", len(unequal) == 12)

    def embed(sig: tuple[int, int], local: list[Fraction]) -> list[Fraction]:
        coords = [Fraction(0) for _ in range(dimension)]
        for local_index, value in enumerate(local):
            coords[by_sig[sig][local_index]] = value
        return coords

    def tables_for(sig: tuple[int, int]):
        stored = []
        for local in bases[sig]:
            coords = embed(sig, local)
            table = [[[Fraction(0) for _ in orbit] for _ in orbit] for _ in axis_steps]
            for d_i, direction in enumerate(axis_steps):
                for a_i, left in enumerate(orbit):
                    for b_i, right in enumerate(orbit):
                        table[d_i][a_i][b_i] = coords[image_of[(direction, left, right)]]
            stored.append(table)
        return stored

    def quadric_rows(sig: tuple[int, int]) -> list[list[Fraction]]:
        values = tables_for(sig)
        rows = []
        seen = set()
        for d_i in range(6):
            for e_i in range(d_i + 1, 6):
                for b_i in range(24):
                    for c_i in range(24):
                        grams = [[Fraction(0) for _ in range(3)] for _ in range(3)]
                        for a_i in range(24):
                            left_vals = [values[p][d_i][a_i][b_i] for p in range(3)]
                            right_vals = [values[p][e_i][a_i][c_i] for p in range(3)]
                            if not any(left_vals) or not any(right_vals):
                                continue
                            for p in range(3):
                                if left_vals[p] == 0:
                                    continue
                                for q in range(3):
                                    if right_vals[q]:
                                        grams[p][q] += left_vals[p] * right_vals[q]
                        coeffs = [
                            grams[0][0],
                            grams[1][1],
                            grams[2][2],
                            grams[0][1] + grams[1][0],
                            grams[0][2] + grams[2][0],
                            grams[1][2] + grams[2][1],
                        ]
                        key = tuple(coeffs)
                        if any(coeffs) and key not in seen:
                            seen.add(key)
                            rows.append(coeffs)
        return rows

    opposite_rank = []
    unequal_pivots = []
    same_rows = []
    for sig in opposite:
        reduced, pivots = rref(quadric_rows(sig), 6)
        opposite_rank.append(len(reduced))
    for sig in unequal:
        _, pivots = rref(quadric_rows(sig), 6)
        unequal_pivots.append(pivots)
    for sig in same_height:
        reduced, _ = rref(quadric_rows(sig), 6)
        same_rows.append(reduced)
    checks.check("each opposite signature has pair-moment rank 0", opposite_rank == [0] * 6)
    checks.check(
        "each unequal signature has a full-rank pair-moment quadric",
        unequal_pivots == [list(range(6))] * 12,
    )
    expected_same = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(-1)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(-1), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(1), Fraction(1)],
    ]
    checks.check(
        "each equal-height signature has the same three quadrics",
        same_rows == [expected_same, expected_same, expected_same],
    )

    def product_form() -> list[Fraction]:
        # (x+z)(y+z) = xy + xz + yz + z^2
        return [Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(1), Fraction(1)]

    checks.check("the third quadric is (x+z)(y+z)", expected_same[2] == product_form())
    left_case = [substituted(row, True) for row in expected_same]
    right_case = [substituted(row, False) for row in expected_same]
    checks.check(
        "setting x=-z yields -2yz, y^2+z^2, and 0",
        left_case
        == [
            (Fraction(0), Fraction(0), Fraction(-2)),
            (Fraction(1), Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(0)),
        ],
    )
    checks.check(
        "setting y=-z yields x^2+z^2",
        right_case[0] == (Fraction(1), Fraction(1), Fraction(0)),
    )
    checks.check(
        "y^2+z^2 and x^2+z^2 have rank 2",
        rref([[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]], 2)[1] == [0, 1],
    )

    def live_directions(sig: tuple[int, int]) -> set[int]:
        values = tables_for(sig)
        found = set()
        for a_i in range(24):
            for d_i in range(6):
                if any(values[p][d_i][a_i][b_i] for p in range(3) for b_i in range(24)):
                    found.add((a_i, d_i))
        per_record = []
        for a_i in range(24):
            per_record.append(sum(1 for d_i in range(6) if (a_i, d_i) in found))
        return set(per_record)

    checks.check(
        "each opposite signature activates one direction on every record",
        all(live_directions(sig) == {1} for sig in opposite),
    )
    checks.check(
        "each other signature activates two directions on every record",
        all(live_directions(sig) == {2} for sig in others),
    )

    def kernel_cross(orientation: int, swapped: bool, height: int, direction, left, right) -> int:
        inverse = transpose(carriers[direction][0])
        return cross_raw(orientation, swapped, height, apply(inverse, left), apply(inverse, right))

    def cap_kernel(level: int, direction, left, right) -> int:
        return cap(left, direction, level) * cap(right, negate(direction), level)

    def vector_from(function) -> list[Fraction]:
        coords = [None] * dimension
        for direction in axis_steps:
            for left in orbit:
                for right in orbit:
                    value = function(direction, left, right)
                    index = image_of[(direction, left, right)]
                    if coords[index] is None:
                        coords[index] = Fraction(value)
                    elif coords[index] != value:
                        raise SystemExit("explicit kernel is not constant on a bond orbit")
        return [Fraction(0) if value is None else value for value in coords]

    explicit = []
    for level in (-3, -2, -1, 1, 2, 3):
        explicit.append(vector_from(lambda d, a, b, level=level: cap_kernel(level, d, a, b)))
    for orientation in (1, -1):
        for swapped in (False, True):
            for height in (1, 2, 3):
                explicit.append(
                    vector_from(
                        lambda d, a, b, orientation=orientation, swapped=swapped, height=height: kernel_cross(
                            orientation, swapped, height, d, a, b
                        )
                    )
                )
    checks.check("eighteen explicit kernels", len(explicit) == 18)
    reduced_explicit, _ = rref(explicit, dimension)
    checks.check("the eighteen explicit kernels are independent", len(reduced_explicit) == 18)
    outside_support = False
    for vector in explicit:
        for index, value in enumerate(vector):
            if value and sig_of[index] not in opposite:
                outside_support = True
    checks.check("the eighteen kernels are supported on opposite heights", not outside_support)

    spanned = True
    explicit_rank = len(reduced_explicit)
    for sig in opposite:
        for local in bases[sig]:
            stacked = explicit + [embed(sig, local)]
            rank_now = len(rref(stacked, dimension)[0])
            if rank_now != explicit_rank:
                spanned = False
    checks.check("opposite signature kernels lie in the eighteen", spanned)

    def first_moment(sig: tuple[int, int]):
        values = tables_for(sig)[0]
        for d_i in range(6):
            for e_i in range(d_i + 1, 6):
                for b_i, right in enumerate(orbit):
                    for c_i, other in enumerate(orbit):
                        total = sum(
                            values[d_i][a_i][b_i] * values[e_i][a_i][c_i] for a_i in range(24)
                        )
                        if total != 0:
                            return axis_steps[d_i], axis_steps[e_i], right, other, total
        return None

    unequal_witness = first_moment(unequal[0])
    same_witness = first_moment(same_height[0])
    checks.check(
        "the height pair (-3, -2) has witness moment -1",
        unequal_witness
        == ((-1, 0, 0), (0, -1, 0), (-3, 1, -2), (-3, 2, 1), Fraction(-1)),
    )
    checks.check(
        "the height pair (-3, -3) has witness moment 1",
        same_witness
        == ((-1, 0, 0), (1, 0, 0), (-3, -2, -1), (-3, -2, -1), Fraction(1)),
    )
    if unequal_witness is not None:
        print(
            "UNEQUAL_WITNESS",
            unequal[0],
            unequal_witness[0],
            unequal_witness[1],
            unequal_witness[2],
            unequal_witness[3],
            unequal_witness[4],
        )
    if same_witness is not None:
        print(
            "SAME_WITNESS",
            same_height[0],
            same_witness[0],
            same_witness[1],
            same_witness[2],
            same_witness[3],
            same_witness[4],
        )
    checks.check("a one-signature stand-in is not the full bond space", dimension != 1)

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
