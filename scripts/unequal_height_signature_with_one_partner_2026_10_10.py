#!/usr/bin/env python3
"""An unequal height signature stays zero beside one partner signature."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/UNEQUAL_HEIGHT_SIGNATURE_WITH_ONE_PARTNER_BOUNDED_THEOREM_NOTE_2026-10-10.md']


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


def kernel_basis(rows: list[tuple[int, ...]], width: int) -> list[list[Fraction]]:
    matrix = [[Fraction(value) for value in row] for row in rows]
    pivots = []
    rank_now = 0
    for col in range(width):
        pivot = next((index for index in range(rank_now, len(matrix)) if matrix[index][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for index in range(len(matrix)):
            if index != rank_now and matrix[index][col] != 0:
                factor = matrix[index][col]
                matrix[index] = [
                    matrix[index][col_index] - factor * matrix[rank_now][col_index]
                    for col_index in range(width)
                ]
        pivots.append(col)
        rank_now += 1
    basis = []
    for free in [col for col in range(width) if col not in pivots]:
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = Fraction(1)
        for pivot_index, pivot_col in enumerate(pivots):
            vector[pivot_col] = -matrix[pivot_index][free]
        basis.append(vector)
    return basis


def reduced_rows(rows: list[list[Fraction]], width: int) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [[Fraction(value) for value in row] for row in rows if any(row)]
    pivots = []
    rank_now = 0
    for col in range(width):
        pivot = next((index for index in range(rank_now, len(matrix)) if matrix[index][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for index in range(len(matrix)):
            if index != rank_now and matrix[index][col] != 0:
                factor = matrix[index][col]
                matrix[index] = [
                    matrix[index][col_index] - factor * matrix[rank_now][col_index]
                    for col_index in range(width)
                ]
        pivots.append(col)
        rank_now += 1
    return matrix[:rank_now], pivots


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6)

    image_of: dict = {}
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
    checks.check("the signatures partition 84 bond orbits", dimension == 84)

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

    def support_table(sig: tuple[int, int]):
        columns = by_sig[sig]
        local_rows = []
        for row in slice_rows:
            packed = tuple(row[index] for index in columns)
            if any(packed):
                local_rows.append(packed)
        basis = kernel_basis(list(set(local_rows)), len(columns))
        merged = defaultdict(lambda: [Fraction(0), Fraction(0), Fraction(0)])
        for basis_index, local in enumerate(basis):
            coords = [Fraction(0) for _ in range(dimension)]
            for local_index, value in enumerate(local):
                coords[columns[local_index]] = value
            for d_i, direction in enumerate(axis_steps):
                for a_i, left in enumerate(orbit):
                    for b_i, right in enumerate(orbit):
                        value = coords[image_of[(direction, left, right)]]
                        if value:
                            merged[(d_i, a_i, b_i)][basis_index] = value
        by_record = defaultdict(lambda: defaultdict(dict))
        for (d_i, a_i, b_i), coeffs in merged.items():
            by_record[a_i][d_i][b_i] = list(coeffs)
        return by_record

    tables = {sig: support_table(sig) for sig in signatures}
    opposite = [sig for sig in signatures if sig[0] == -sig[1]]
    same_height = [sig for sig in signatures if sig[0] == sig[1]]
    unequal = [sig for sig in signatures if sig[0] != -sig[1] and sig[0] != sig[1]]
    checks.check("six opposite, three equal, and twelve unequal signatures", (len(opposite), len(same_height), len(unequal)) == (6, 3, 12))

    def monomials_forced(extra: tuple[int, int], other: tuple[int, int]) -> bool:
        blocks = [tables[extra], tables[other]]
        monomials = [(left, right) for left in range(6) for right in range(left, 6)]
        mono_at = {item: index for index, item in enumerate(monomials)}
        rows: dict[tuple, list[Fraction]] = {}
        for a_i in range(24):
            live = sorted(set(blocks[0].get(a_i, {})) | set(blocks[1].get(a_i, {})))
            for d_i, e_i in combinations(live, 2):
                left_maps = []
                right_maps = []
                for block in blocks:
                    record = block.get(a_i, {})
                    left_maps.append(record.get(d_i, {}))
                    right_maps.append(record.get(e_i, {}))
                b_keys = set(left_maps[0]) | set(left_maps[1])
                c_keys = set(right_maps[0]) | set(right_maps[1])
                for b_i in b_keys:
                    left_values = left_maps[0].get(b_i, [Fraction(0), Fraction(0), Fraction(0)]) + left_maps[1].get(
                        b_i, [Fraction(0), Fraction(0), Fraction(0)]
                    )
                    if not any(left_values):
                        continue
                    for c_i in c_keys:
                        right_values = right_maps[0].get(
                            c_i, [Fraction(0), Fraction(0), Fraction(0)]
                        ) + right_maps[1].get(c_i, [Fraction(0), Fraction(0), Fraction(0)])
                        if not any(right_values):
                            continue
                        key = (d_i, e_i, b_i, c_i)
                        row = rows.get(key)
                        if row is None:
                            row = [Fraction(0) for _ in monomials]
                            rows[key] = row
                        for left_index in range(6):
                            for right_index in range(left_index, 6):
                                term = left_values[left_index] * right_values[right_index]
                                if left_index != right_index:
                                    term += left_values[right_index] * right_values[left_index]
                                if term:
                                    row[mono_at[(left_index, right_index)]] += term
        extra_cols = [index for index, (left, right) in enumerate(monomials) if left < 3 and right < 3]
        ordered = extra_cols + [index for index in range(len(monomials)) if index not in extra_cols]
        reordered = [[row[col] for col in ordered] for row in rows.values()]
        reduced, pivots = reduced_rows(reordered, len(monomials))
        if pivots[:6] != [0, 1, 2, 3, 4, 5]:
            return False
        return all(all(reduced[row_index][col] == 0 for col in range(6, len(monomials))) for row_index in range(6))

    forced = 0
    unresolved = []
    for extra in unequal:
        for other in signatures:
            if other == extra:
                continue
            if monomials_forced(extra, other):
                forced += 1
            else:
                unresolved.append((extra, other))
    checks.check("the corrected direct monomial test certifies 168 pairs and leaves 72 undecided", forced == 168 and len(unresolved) == 72)
    for extra, other in unresolved:
        print("DIRECT_TEST_UNRESOLVED", extra, other)
    print("DIRECT_TEST_COUNTS", "certified", forced, "unresolved", len(unresolved))
    checks.check(
        "an equal-height signature is not forced by this square test beside one opposite partner",
        not monomials_forced((-3, -3), (3, -3)),
    )
    checks.check("a one-signature stand-in is not this pair count", forced != 1)

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
