#!/usr/bin/env python3
"""Exact checks for the proper-cubic finite-support kernel classification.

The runner classifies an explicitly supplied rational linear convolution
class. It does not derive linearity, convolution form, finite range,
proper-cubic covariance, or constant-annihilation from the framework axioms.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction as F


PASS = 0
FAIL = 0

Vec = tuple[int, int, int]
Mat3 = tuple[Vec, Vec, Vec]


def check(label: str, condition: bool, detail: object) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def rref(rows: list[list[F]]) -> tuple[list[list[F]], list[int]]:
    mat = [list(row) for row in rows]
    if not mat:
        return [], []
    pivots: list[int] = []
    pivot_row = 0
    for column in range(len(mat[0])):
        selected = next(
            (row for row in range(pivot_row, len(mat)) if mat[row][column]),
            None,
        )
        if selected is None:
            continue
        mat[pivot_row], mat[selected] = mat[selected], mat[pivot_row]
        scale = mat[pivot_row][column]
        mat[pivot_row] = [value / scale for value in mat[pivot_row]]
        for row in range(len(mat)):
            if row == pivot_row or not mat[row][column]:
                continue
            factor = mat[row][column]
            mat[row] = [
                left - factor * right
                for left, right in zip(mat[row], mat[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(mat):
            break
    return mat, pivots


def nullspace(rows: list[list[F]], columns: int) -> list[list[F]]:
    if not rows:
        return [
            [F(int(row == column)) for column in range(columns)]
            for row in range(columns)
        ]
    reduced, pivots = rref(rows)
    free_columns = [column for column in range(columns) if column not in pivots]
    basis: list[list[F]] = []
    for free in free_columns:
        vector = [F(0)] * columns
        vector[free] = F(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        basis.append(vector)
    return basis


def solve_exact(columns: list[list[F]], target: list[F]) -> list[F] | None:
    augmented = [
        [column[row] for column in columns] + [target[row]]
        for row in range(len(target))
    ]
    reduced, pivots = rref(augmented)
    unknowns = len(columns)
    if unknowns in pivots:
        return None
    solution = [F(0)] * unknowns
    for row, pivot in enumerate(pivots):
        solution[pivot] = reduced[row][unknowns]
    return solution


def signed_permutations() -> list[Mat3]:
    matrices: list[Mat3] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(
                    signs[row] * int(permutation[row] == column)
                    for column in range(3)
                )
                for row in range(3)
            )
            matrices.append(matrix)  # type: ignore[arg-type]
    return matrices


def determinant(matrix: Mat3) -> int:
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def apply(matrix: Mat3, vector: Vec) -> Vec:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def multiply(left: Mat3, right: Mat3) -> Mat3:
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def ball(radius_squared: int) -> list[Vec]:
    bound = int(radius_squared**0.5) + 1
    return sorted(
        (x, y, z)
        for x in range(-bound, bound + 1)
        for y in range(-bound, bound + 1)
        for z in range(-bound, bound + 1)
        if x * x + y * y + z * z <= radius_squared
    )


def burnside_count(group: list[Mat3], points: list[Vec]) -> int:
    fixed_pairs = sum(
        int(apply(matrix, point) == point)
        for matrix in group
        for point in points
    )
    quotient, remainder = divmod(fixed_pairs, len(group))
    if remainder:
        raise AssertionError("Burnside average is not integral")
    return quotient


def invariance_rows(group: list[Mat3], points: list[Vec]) -> list[list[F]]:
    index = {point: position for position, point in enumerate(points)}
    rows: list[list[F]] = []
    for matrix in group:
        for point in points:
            image = apply(matrix, point)
            if image == point:
                continue
            row = [F(0)] * len(points)
            row[index[image]] += F(1)
            row[index[point]] -= F(1)
            rows.append(row)
    return rows


def invariant_basis(group: list[Mat3], points: list[Vec]) -> list[list[F]]:
    return nullspace(invariance_rows(group, points), len(points))


def main() -> int:
    all_signed = signed_permutations()
    proper = [matrix for matrix in all_signed if determinant(matrix) == 1]
    proper_set = set(proper)
    identity: Mat3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    closure = all(
        multiply(left, right) in proper_set for left in proper for right in proper
    )
    check(
        "C1 exact proper cubic rotation group",
        len(all_signed) == 48
        and len(proper) == 24
        and identity in proper_set
        and closure
        and len({determinant(matrix) for matrix in all_signed}) == 2,
        {
            "signed_permutations": len(all_signed),
            "proper_rotations": len(proper),
            "closed": closure,
        },
    )

    range_one = ball(1)
    trivial_group = [identity]
    proper_orbits = burnside_count(proper, range_one)
    trivial_orbits = burnside_count(trivial_group, range_one)
    face_images = {apply(matrix, (1, 0, 0)) for matrix in proper}
    check(
        "C2 nearest-neighbour orbit decomposition",
        len(range_one) == 7
        and proper_orbits == 2
        and trivial_orbits == 7
        and face_images
        == {
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        },
        {
            "points": len(range_one),
            "proper_orbits": proper_orbits,
            "trivial_group_orbits": trivial_orbits,
            "face_orbit_size": len(face_images),
        },
    )

    table: dict[int, dict[str, int]] = {}
    for radius_squared in range(1, 7):
        points = ball(radius_squared)
        table[radius_squared] = {
            "points": len(points),
            "burnside_orbits": burnside_count(proper, points),
            "exact_nullity": len(invariant_basis(proper, points)),
        }
    agreement = all(
        row["burnside_orbits"] == row["exact_nullity"] for row in table.values()
    )
    check(
        "C3 Burnside orbit count equals independently solved exact nullity",
        agreement
        and table[1]["exact_nullity"] == 2
        and table[2]["exact_nullity"] == 3
        and len(invariant_basis(trivial_group, range_one)) == 7,
        table,
    )

    range_one_basis = invariant_basis(proper, range_one)
    index = {point: position for position, point in enumerate(range_one)}
    identity_vector = [F(0)] * len(range_one)
    identity_vector[index[(0, 0, 0)]] = F(1)
    laplacian_vector = [
        F(-6) if point == (0, 0, 0) else F(1) for point in range_one
    ]
    span_solutions = [
        solve_exact([identity_vector, laplacian_vector], basis_vector)
        for basis_vector in range_one_basis
    ]
    forward_vector = [F(0)] * len(range_one)
    forward_vector[index[(0, 0, 0)]] = F(-1)
    forward_vector[index[(1, 0, 0)]] = F(1)
    forward_in_span = (
        solve_exact([identity_vector, laplacian_vector], forward_vector) is not None
    )
    check(
        "C4 range-one invariant kernels are exactly span{I, Delta}",
        len(range_one_basis) == 2
        and all(solution is not None for solution in span_solutions)
        and solve_exact([identity_vector], laplacian_vector) is None
        and not forward_in_span,
        {
            "dimension": len(range_one_basis),
            "basis_coordinates": [
                None
                if solution is None
                else tuple(str(value) for value in solution)
                for solution in span_solutions
            ],
            "anisotropic_forward_difference_in_span": forward_in_span,
        },
    )

    zero_sum_range_one = nullspace(
        invariance_rows(proper, range_one) + [[F(1)] * len(range_one)],
        len(range_one),
    )
    range_two = ball(2)
    zero_sum_range_two = nullspace(
        invariance_rows(proper, range_two) + [[F(1)] * len(range_two)],
        len(range_two),
    )
    check(
        "C5 constant-annihilation leaves the Laplacian line only at range one",
        len(zero_sum_range_one) == 1
        and solve_exact(zero_sum_range_one, laplacian_vector) is not None
        and len(zero_sum_range_two) == 2
        and sum(identity_vector) != 0
        and sum(laplacian_vector) == 0,
        {
            "range_one_zero_sum_dimension": len(zero_sum_range_one),
            "range_two_zero_sum_dimension": len(zero_sum_range_two),
            "laplacian_sum": str(sum(laplacian_vector)),
        },
    )

    summary = {
        "authority": "none",
        "audit": "unset",
        "claim_type": "bounded_theorem",
        "fail_count": FAIL,
        "pass": FAIL == 0,
        "pass_count": PASS,
        "table": table,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    if FAIL:
        print("RESULT PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_FAILED")
        return 1
    print("RESULT PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_PASSES")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
