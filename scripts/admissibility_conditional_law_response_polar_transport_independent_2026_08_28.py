#!/usr/bin/env python3
"""Independent Fraction checker for conditional-law polar transport.

This checker shares no implementation path with the primary SymPy runner.
"""

from __future__ import annotations

from fractions import Fraction as F
import itertools


AUDIT_TIMEOUT_SEC = 120


Vector = tuple[F, F, F]
Matrix = tuple[tuple[F, F, F], tuple[F, F, F], tuple[F, F, F]]


ZERO: Vector = (F(0), F(0), F(0))
E1: Vector = (F(1), F(0), F(0))
E2: Vector = (F(0), F(1), F(0))
E3: Vector = (F(0), F(0), F(1))
ATOMS: tuple[Vector, ...] = (ZERO, E1, tuple(-x for x in E1), E2,
                             tuple(-x for x in E2), E3,
                             tuple(-x for x in E3))


def dot(left: Vector, right: Vector) -> F:
    return sum((a * b for a, b in zip(left, right)), F(0))


def interaction(left: Vector, right: Vector) -> F:
    return dot(left, right) / ((1 + dot(left, left))
                               * (1 + dot(right, right)))


def weights(neighbors: tuple[Vector, ...], sign: int,
            quadratic: bool = False) -> tuple[F, ...]:
    raw = []
    for atom in ATOMS:
        value = F(1)
        for neighbor in neighbors:
            d = interaction(atom, neighbor)
            value *= 2 + (d * d if quadratic else sign * d)
        raw.append(value)
    total = sum(raw, F(0))
    return tuple(value / total for value in raw)


def outer(left: Vector, right: Vector) -> Matrix:
    return tuple(tuple(a * b for b in right) for a in left)  # type: ignore[return-value]


def matrix_sum(matrices: tuple[Matrix, ...]) -> Matrix:
    return tuple(tuple(sum((matrix[i][j] for matrix in matrices), F(0))
                       for j in range(3)) for i in range(3))  # type: ignore[return-value]


def scale(matrix: Matrix, value: F) -> Matrix:
    return tuple(tuple(value * entry for entry in row)
                 for row in matrix)  # type: ignore[return-value]


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] + right[i][j] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum((left[i][k] * right[k][j] for k in range(3)), F(0))
                       for j in range(3)) for i in range(3))  # type: ignore[return-value]


def rational_rank(rows: tuple[tuple[F, ...], ...]) -> int:
    matrix = [list(row) for row in rows]
    rank = 0
    if not matrix:
        return rank
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix))
                      if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [entry / pivot_value for entry in matrix[rank]]
        for i in range(len(matrix)):
            if i == rank or not matrix[i][column]:
                continue
            factor = matrix[i][column]
            matrix[i] = [entry - factor * pivot_entry
                         for entry, pivot_entry in zip(matrix[i], matrix[rank])]
        rank += 1
    return rank


def response_jacobian(sign: int) -> Matrix:
    """Differentiate the normalized seven-atom conditional at b=0 exactly."""
    total_weight = F(7 * 2**6)
    columns = []
    for direction in range(3):
        column = []
        for output in range(3):
            numerator_derivative = F(0)
            for atom in ATOMS:
                raw_derivative = (F(2**5 * sign) * atom[direction]
                                  / (1 + dot(atom, atom)))
                numerator_derivative += atom[output] * raw_derivative
            column.append(numerator_derivative / total_weight)
        columns.append(tuple(column))
    return tuple(tuple(columns[j][i] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def determinant(matrix: Matrix) -> F:
    a, b, c = matrix
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def cross_moment(pairs: tuple[tuple[Vector, Vector], ...]) -> Matrix:
    return scale(matrix_sum(tuple(outer(left, right) for left, right in pairs)),
                 F(1, len(pairs)))


def independent_facts() -> dict[str, bool]:
    identity: Matrix = ((F(1), F(0), F(0)),
                        (F(0), F(1), F(0)),
                        (F(0), F(0), F(1)))
    minus_identity = scale(identity, F(-1))
    zero_matrix = scale(identity, F(0))
    zero_neighbors = (ZERO,) * 6
    one_neighbor = (E1,) + (ZERO,) * 5
    uniform = weights(zero_neighbors, 1)
    quadratic = weights(one_neighbor, 1, quadratic=True)
    jacobian_plus = response_jacobian(1)
    jacobian_minus = response_jacobian(-1)
    response_plus = add(jacobian_plus, transpose(jacobian_plus))
    response_minus = add(jacobian_minus, transpose(jacobian_minus))
    directed: Matrix = ((F(1), F(2), F(0)),
                        (F(0), F(1), F(1)),
                        (F(1), F(0), F(1)))
    reverse: Matrix = ((F(2), F(0), F(1)),
                       (F(1), F(1), F(0)),
                       (F(0), F(1), F(2)))
    cross = add(directed, transpose(reverse))
    reverse_cross = add(reverse, transpose(directed))
    left_frame: Matrix = ((F(0), F(-1), F(0)),
                          (F(1), F(0), F(0)),
                          (F(0), F(0), F(1)))
    right_frame: Matrix = ((F(1), F(0), F(0)),
                           (F(0), F(0), F(-1)),
                           (F(0), F(1), F(0)))
    transformed_directed = multiply(multiply(left_frame, directed),
                                    transpose(right_frame))
    transformed_reverse = multiply(multiply(right_frame, reverse),
                                   transpose(left_frame))
    transformed_cross = add(transformed_directed,
                            transpose(transformed_reverse))
    covariant_cross = multiply(multiply(left_frame, cross),
                               transpose(right_frame))
    half_turn_minus_identity: Matrix = ((F(0), F(0), F(0)),
                                        (F(0), F(-2), F(0)),
                                        (F(0), F(0), F(-2)))
    stabilizer_rows = []
    for output in range(3):
        for column in range(3):
            row = [F(0)] * 9
            for inner in range(3):
                row[inner * 3 + column] = half_turn_minus_identity[output][inner]
            stabilizer_rows.append(tuple(row))
    axis = ATOMS[1:]
    product = tuple(itertools.product(axis, axis))
    aligned = tuple((vector, vector) for vector in axis)
    antipodal = tuple((vector, tuple(-x for x in vector)) for vector in axis)
    axis_second = scale(matrix_sum(tuple(outer(v, v) for v in axis)), F(1, 6))
    return {
        "seven atoms normalize at zero context": uniform == (F(1, 7),) * 7,
        "positive Jacobian is derived": jacobian_plus == scale(identity, F(1, 14)),
        "negative Jacobian is derived": jacobian_minus == scale(identity, F(-1, 14)),
        "positive cross-object determinant": determinant(response_plus) == F(1, 343),
        "negative cross-object determinant": determinant(response_minus) == F(-1, 343),
        "proper and improper polar representatives": determinant(identity) == 1 and determinant(minus_identity) == -1,
        "reciprocal reversal is the adjoint identity": reverse_cross == transpose(cross),
        "independent endpoint covariance": transformed_cross == covariant_cross,
        "nontrivial endpoint stabilizer imposes six constraints": rational_rank(tuple(stabilizer_rows)) == 6,
        "quadratic aligned weights": quadratic[1:3] == (F(33, 226), F(33, 226)),
        "quadratic other weights": all(quadratic[i] == F(16, 113) for i in (0, 3, 4, 5, 6)),
        "axis second moment": axis_second == scale(identity, F(1, 3)),
        "independent coupling is singular": cross_moment(product) == zero_matrix,
        "aligned coupling polar carrier": cross_moment(aligned) == scale(identity, F(1, 3)),
        "antipodal coupling polar carrier": cross_moment(antipodal) == scale(identity, F(-1, 3)),
    }


def main() -> int:
    facts = independent_facts()
    failures = 0
    for name, condition in facts.items():
        print(f"[{'PASS' if condition else 'FAIL'}] {name}")
        failures += int(not condition)
    print(f"TOTAL: PASS={len(facts)-failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
