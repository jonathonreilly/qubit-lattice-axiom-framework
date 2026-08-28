#!/usr/bin/env python3
"""Independent exact controls for the J_r temporal/spatial semigroup defect.

Only Python integers, ``Fraction``, finite sums, and elementary matrix
arithmetic are used.  This helper does not import the primary runner, SymPy,
NumPy, or a campaign scratch module.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product


AUDIT_TIMEOUT_SEC = 120

Matrix = tuple[tuple[F, ...], ...]
Vector = tuple[F, ...]


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][column] for row in range(len(matrix)))
                 for column in range(len(matrix[0])))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[row][k] * right[k][column]
                 for k in range(len(right))), F(0))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column]
              for column in range(len(left[0])))
        for row in range(len(left))
    )


def scale(scalar: F, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def identity(size: int) -> Matrix:
    return tuple(
        tuple(F(int(row == column)) for column in range(size))
        for row in range(size)
    )


def zero(rows: int, columns: int) -> Matrix:
    return tuple(tuple(F(0) for _ in range(columns)) for _ in range(rows))


def separated_cross_spectrum(matrix: Matrix) -> tuple[F, F, F]:
    """Spectrum of the fixture form [[a,0,c],[0,b,0],[c,0,a]]."""

    assert matrix[0][0] == matrix[2][2]
    assert matrix[0][1] == matrix[1][0] == 0
    assert matrix[1][2] == matrix[2][1] == 0
    assert matrix[0][2] == matrix[2][0]
    return (
        matrix[0][0] + matrix[0][2],
        matrix[0][0] - matrix[0][2],
        matrix[1][1],
    )


def separated_cross_norm(matrix: Matrix) -> F:
    return max(abs(value) for value in separated_cross_spectrum(matrix))


def diagonal_norm(matrix: Matrix) -> F:
    assert all(
        matrix[row][column] == 0
        for row in range(len(matrix))
        for column in range(len(matrix))
        if row != column
    )
    return max(abs(matrix[index][index]) for index in range(len(matrix)))


def semigroup_defect(operator: Matrix, isometry: Matrix) -> Matrix:
    """J* S^2 J - (J* S J)^2 in exact arithmetic."""

    adjoint = transpose(isometry)
    compressed = matmul(matmul(adjoint, operator), isometry)
    compressed_square = matmul(compressed, compressed)
    compressed_fine_square = matmul(
        matmul(adjoint, matmul(operator, operator)), isometry
    )
    return subtract(compressed_fine_square, compressed_square)


def factored_defect(operator: Matrix, isometry: Matrix) -> Matrix:
    """J* S (I-JJ*) S J, the positive defect factorization."""

    adjoint = transpose(isometry)
    projector = matmul(isometry, adjoint)
    complement = subtract(identity(len(projector)), projector)
    return matmul(
        matmul(matmul(matmul(adjoint, operator), complement), operator),
        isometry,
    )


def matrix_fixture() -> dict[str, object]:
    # J includes the two-dimensional coarse space as the first two axes.
    isometry: Matrix = (
        (F(1), F(0)),
        (F(0), F(1)),
        (F(0), F(0)),
    )
    projector = matmul(isometry, transpose(isometry))

    # The 1--3 block eigenvalues are 3/4 and 1/4; the remaining eigenvalue
    # is 1/3.  Thus S is a positive self-adjoint contraction.
    operator: Matrix = (
        (F(1, 2), F(0), F(1, 4)),
        (F(0), F(1, 3), F(0)),
        (F(1, 4), F(0), F(1, 2)),
    )
    defect = semigroup_defect(operator, isometry)
    factor = factored_defect(operator, isometry)

    # A finite-packet surrogate keeps the same diagonal data and halves the
    # sole retained-to-hidden amplitude.  Its eigenvalues are 5/8, 3/8, 1/3.
    packet: Matrix = (
        (F(1, 2), F(0), F(1, 8)),
        (F(0), F(1, 3), F(0)),
        (F(1, 8), F(0), F(1, 2)),
    )
    packet_defect = semigroup_defect(packet, isometry)

    # The difference has the same separated-cross form, while the two defect
    # matrices are diagonal.  Compute, rather than insert, both exact norms.
    operator_difference = subtract(operator, packet)
    defect_difference = subtract(defect, packet_defect)
    operator_distance = separated_cross_norm(operator_difference)
    defect_distance = diagonal_norm(defect_difference)

    normalization = F(3, 5)
    scaled_defect = semigroup_defect(scale(normalization, operator), isometry)

    # Deliberately preserve Range(J): the complement cannot receive S_0 J.
    range_preserving: Matrix = (
        (F(1, 2), F(0), F(0)),
        (F(0), F(1, 3), F(0)),
        (F(0), F(0), F(1, 4)),
    )
    range_defect = semigroup_defect(range_preserving, isometry)
    complement = subtract(identity(3), projector)

    return {
        "isometry": isometry,
        "projector": projector,
        "operator": operator,
        "packet": packet,
        "operator_spectrum": separated_cross_spectrum(operator),
        "packet_spectrum": separated_cross_spectrum(packet),
        "defect": defect,
        "factor": factor,
        "packet_defect": packet_defect,
        "operator_distance": operator_distance,
        "defect_distance": defect_distance,
        "normalization": normalization,
        "scaled_defect": scaled_defect,
        "range_defect": range_defect,
        "range_leak": matmul(matmul(complement, range_preserving), isometry),
    }


Z2 = (1, -1)
FINE_STATES = tuple(product(Z2, repeat=2))


def coarse_product(state: tuple[int, int]) -> int:
    return state[0] * state[1]


def pullback(coarse: dict[int, F]) -> dict[tuple[int, int], F]:
    return {state: coarse[coarse_product(state)] for state in FINE_STATES}


def conditional_pushforward(fine: dict[tuple[int, int], F]) -> dict[int, F]:
    # Each product fiber has two points under normalized Z_2 x Z_2 Haar.
    return {
        coarse: sum(
            (fine[state] for state in FINE_STATES
             if coarse_product(state) == coarse),
            F(0),
        ) / 2
        for coarse in Z2
    }


def conditional_project(fine: dict[tuple[int, int], F]) -> dict[tuple[int, int], F]:
    return pullback(conditional_pushforward(fine))


def fine_inner(left: dict[tuple[int, int], F],
               right: dict[tuple[int, int], F]) -> F:
    return sum((left[state] * right[state] for state in FINE_STATES), F(0)) / 4


def z2_conditional_fixture() -> dict[str, object]:
    fine_basis = tuple(
        {state: F(int(state == selected)) for state in FINE_STATES}
        for selected in FINE_STATES
    )
    coarse_basis = tuple(
        {coarse: F(int(coarse == selected)) for coarse in Z2}
        for selected in Z2
    )

    projector_idempotent = all(
        conditional_project(conditional_project(vector))
        == conditional_project(vector)
        for vector in fine_basis
    )
    projector_self_adjoint = all(
        fine_inner(left, conditional_project(right))
        == fine_inner(conditional_project(left), right)
        for left in fine_basis
        for right in fine_basis
    )
    isometry_left_inverse = all(
        conditional_pushforward(pullback(vector)) == vector
        for vector in coarse_basis
    )

    gamma_rows: list[tuple[int, F, F]] = []
    semigroup_rows: list[tuple[int, Matrix, Matrix]] = []
    for member in (1, 2, 3, 5, 8):
        potential = {1: F(0), -1: F(16, member)}
        fine_action = {
            state: potential[state[0]] + potential[state[1]]
            for state in FINE_STATES
        }
        fine_square = {state: value * value for state, value in fine_action.items()}
        mean = conditional_pushforward(fine_action)
        second = conditional_pushforward(fine_square)
        variance = {
            coarse: second[coarse] - mean[coarse] ** 2 for coarse in Z2
        }
        gamma_rows.append((member, variance[1], variance[-1]))

        compressed: Matrix = ((mean[1], F(0)), (F(0), mean[-1]))
        compressed_square: Matrix = matmul(compressed, compressed)
        compressed_fine_square: Matrix = (
            (second[1], F(0)),
            (F(0), second[-1]),
        )
        direct_defect = subtract(compressed_fine_square, compressed_square)
        variance_matrix: Matrix = (
            (variance[1], F(0)),
            (F(0), variance[-1]),
        )
        semigroup_rows.append((member, direct_defect, variance_matrix))

    return {
        "projector_idempotent": projector_idempotent,
        "projector_self_adjoint": projector_self_adjoint,
        "isometry_left_inverse": isometry_left_inverse,
        "gamma_rows": tuple(gamma_rows),
        "semigroup_rows": tuple(semigroup_rows),
    }


def main() -> int:
    matrix = matrix_fixture()
    z2 = z2_conditional_fixture()

    expected_defect: Matrix = ((F(1, 16), F(0)), (F(0), F(0)))
    expected_packet_defect: Matrix = ((F(1, 64), F(0)), (F(0), F(0)))
    expected_scaled = scale(matrix["normalization"] ** 2, expected_defect)

    checks = (
        (
            "rational isometry and conditional projector typing",
            matmul(transpose(matrix["isometry"]), matrix["isometry"])
            == identity(2)
            and matrix["projector"] == ((F(1), F(0), F(0)),
                                         (F(0), F(1), F(0)),
                                         (F(0), F(0), F(0))),
        ),
        (
            "self-adjoint positive contraction fixture",
            matrix["operator"] == transpose(matrix["operator"])
            and matrix["packet"] == transpose(matrix["packet"])
            and matrix["operator_spectrum"] == (F(3, 4), F(1, 4), F(1, 3))
            and matrix["packet_spectrum"] == (F(5, 8), F(3, 8), F(1, 3))
            and all(0 <= value <= 1 for value in matrix["operator_spectrum"])
            and all(0 <= value <= 1 for value in matrix["packet_spectrum"]),
        ),
        (
            "J* S^2 J minus (J* S J)^2 factorization",
            matrix["defect"] == matrix["factor"] == expected_defect,
        ),
        (
            "semigroup defect is positive and nonzero",
            matrix["defect"][0][0] > 0
            and matrix["defect"][1][1] >= 0
            and matrix["defect"][0][1] == matrix["defect"][1][0] == 0,
        ),
        (
            "Q=J J* is the exact conditional-expectation projector",
            z2["projector_idempotent"]
            and z2["projector_self_adjoint"]
            and z2["isometry_left_inverse"],
        ),
        (
            "two-cell Z2 conditional variances for several n",
            all(
                gamma_plus == F(256, member * member) and gamma_minus == 0
                for member, gamma_plus, gamma_minus in z2["gamma_rows"]
            ),
        ),
        (
            "conditional variance equals the compressed semigroup defect",
            all(direct == variance
                for _member, direct, variance in z2["semigroup_rows"]),
        ),
        (
            "generated interaction is nonconstant on the coarse Z2 carrier",
            all(gamma_plus != gamma_minus
                for _member, gamma_plus, gamma_minus in z2["gamma_rows"]),
        ),
        (
            "common scalar normalization scales the defect quadratically",
            matrix["scaled_defect"] == expected_scaled,
        ),
        (
            "nonzero scalar normalization cannot remove a nonzero defect",
            matrix["normalization"] != 0
            and matrix["scaled_defect"] != zero(2, 2),
        ),
        (
            "finite-packet defect and exact operator-distance fixture",
            matrix["packet_defect"] == expected_packet_defect
            and matrix["operator_distance"] == F(1, 8)
            and matrix["defect_distance"] == F(3, 64),
        ),
        (
            "finite-packet Lipschitz bound ||Def(S)-Def(S_K)|| <= 4||S-S_K||",
            matrix["defect_distance"] <= 4 * matrix["operator_distance"],
        ),
        (
            "range-preserving control has exactly zero defect",
            matrix["range_leak"] == zero(3, 2)
            and matrix["range_defect"] == zero(2, 2),
        ),
    )

    passed = 0
    for label, condition in checks:
        ok = bool(condition)
        passed += int(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")

    print("gamma:", ", ".join(
        f"n={member}:(+){gamma_plus},(-){gamma_minus}"
        for member, gamma_plus, gamma_minus in z2["gamma_rows"]
    ))
    failed = len(checks) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
