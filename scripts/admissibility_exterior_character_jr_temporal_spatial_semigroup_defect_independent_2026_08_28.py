#!/usr/bin/env python3
"""Independent exact controls for the J_r temporal/spatial semigroup defect.

Only Python integers, ``Fraction``, finite sums, and elementary matrix
arithmetic are used.  This helper does not import the primary runner, SymPy,
NumPy, or a campaign scratch module.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb, factorial


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


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column]
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


def general_r_response_fixture() -> dict[str, object]:
    """Independent conditioned-fiber response for r=2,...,7."""

    potential = {1: F(0), -1: F(2)}
    mean = F(1)
    centered = {1: -mean, -1: mean}
    rows: list[tuple[int, bool, bool, bool]] = []
    subset_independence = True

    for width in range(2, 8):
        states = tuple(product(Z2, repeat=width))
        fibers = {
            delta: tuple(state for state in states
                         if _product(state) == delta)
            for delta in Z2
        }

        if width <= 5:
            for delta in Z2:
                fiber = fibers[delta]
                for size in range(1, width):
                    for indices in combinations(range(width), size):
                        counts: dict[tuple[int, ...], int] = {}
                        for state in fiber:
                            key = tuple(state[index] for index in indices)
                            counts[key] = counts.get(key, 0) + 1
                        target = 2 ** (width - 1 - size)
                        subset_independence &= (
                            len(counts) == 2**size
                            and set(counts.values()) == {target}
                        )

        moments: dict[int, tuple[F, ...]] = {}
        variances: dict[int, F] = {}
        centered_convolution: dict[int, F] = {}
        for delta in Z2:
            actions = tuple(
                sum((potential[value] for value in state), F(0))
                for state in fibers[delta]
            )
            moments[delta] = tuple(
                F(1) if order == 0 else
                sum((value**order for value in actions), F(0)) / len(actions)
                for order in range(width + 1)
            )
            variances[delta] = moments[delta][2] - moments[delta][1] ** 2
            centered_convolution[delta] = sum(
                (_fraction_product(tuple(centered[value] for value in state))
                 for state in fibers[delta]),
                F(0),
            ) / len(fibers[delta])

        response: dict[int, F] = {}
        for delta in Z2:
            bracket = 2**width * moments[delta][width] - sum(
                (F(comb(width, order))
                 * moments[delta][order]
                 * moments[delta][width - order]
                 for order in range(width + 1)),
                F(0),
            )
            response[delta] = F((-1) ** width, factorial(width)) * bracket
        response_mean = sum(response.values(), F(0)) / 2
        response_nc = {
            delta: response[delta] - response_mean for delta in Z2
        }
        expected = {
            delta: F((-1) ** width * (2**width - 2))
            * centered_convolution[delta]
            for delta in Z2
        }
        variance_scalar = width == 2 or variances[1] == variances[-1]
        response_exact = response_nc == expected
        response_nonconstant = response_nc[1] != response_nc[-1]
        rows.append((width, variance_scalar, response_exact, response_nonconstant))

    return {
        "subset_independence": subset_independence,
        "rows": tuple(rows),
    }


def _product(values: tuple[int, ...]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def _fraction_product(values: tuple[F, ...]) -> F:
    result = F(1)
    for value in values:
        result *= value
    return result


Poly = dict[tuple[int, int], F]
PolyMatrix = tuple[tuple[Poly, ...], ...]


def _poly_add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, F(0)) + value
        if result[degree] == 0:
            del result[degree]
    return result


def _poly_mul(left: Poly, right: Poly, cutoff: int) -> Poly:
    result: Poly = {}
    for (epsilon_left, lambda_left), value_left in left.items():
        for (epsilon_right, lambda_right), value_right in right.items():
            degree = (epsilon_left + epsilon_right,
                      lambda_left + lambda_right)
            if degree[0] <= cutoff and degree[1] <= cutoff:
                result[degree] = result.get(degree, F(0)) + value_left * value_right
    return {degree: value for degree, value in result.items() if value}


def _poly_matrix_multiply(left: PolyMatrix, right: PolyMatrix,
                          cutoff: int) -> PolyMatrix:
    return tuple(
        tuple(
            _poly_sum(tuple(
                _poly_mul(left[row][middle], right[middle][column], cutoff)
                for middle in range(len(right))
            ))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def _poly_sum(values: tuple[Poly, ...]) -> Poly:
    result: Poly = {}
    for value in values:
        result = _poly_add(result, value)
    return result


def _poly_matrix_subtract(left: PolyMatrix, right: PolyMatrix) -> PolyMatrix:
    return tuple(
        tuple(_poly_add(left[row][column], {
            degree: -value for degree, value in right[row][column].items()
        }) for column in range(len(left[0])))
        for row in range(len(left))
    )


def _compress_poly_matrix(matrix: PolyMatrix,
                          states: tuple[tuple[int, ...], ...]) -> PolyMatrix:
    fiber_size = len(states) // 2
    fibers = {
        delta: tuple(index for index, state in enumerate(states)
                     if _product(state) == delta)
        for delta in Z2
    }
    return tuple(
        tuple({
            degree: value / fiber_size
            for degree, value in _poly_sum(tuple(
                matrix[left][right]
                for left in fibers[delta_left]
                for right in fibers[delta_right]
            )).items()
        } for delta_right in Z2)
        for delta_left in Z2
    )


def _poly_exp_half(action: int, cutoff: int) -> Poly:
    return {
        (order, order): F((-action) ** order, (2**order) * factorial(order))
        for order in range(cutoff + 1)
    }


def complete_step_response_fixture() -> tuple[tuple[int, F, F, F, F], ...]:
    """Formal Fraction check with a nontrivial C_epsilon between M halves."""

    rows: list[tuple[int, F, F, F, F]] = []
    for width in (3, 4):
        states = tuple(product(Z2, repeat=width))
        size = len(states)
        actions = tuple(sum(0 if value == 1 else 2 for value in state)
                        for state in states)
        multiplier: PolyMatrix = tuple(
            tuple(_poly_exp_half(actions[row], width) if row == column else {}
                  for column in range(size))
            for row in range(size)
        )
        temporal: PolyMatrix = tuple(
            tuple(
                ({(0, 0): F(1), (1, 0): F(-width, 7)} if row == column else
                 {(1, 0): F(1, 7)} if sum(
                     states[row][index] != states[column][index]
                     for index in range(width)
                 ) == 1 else {})
                for column in range(size)
            )
            for row in range(size)
        )
        step = _poly_matrix_multiply(
            _poly_matrix_multiply(multiplier, temporal, width),
            multiplier,
            width,
        )
        direct = _compress_poly_matrix(
            _poly_matrix_multiply(step, step, width), states
        )
        compressed = _compress_poly_matrix(step, states)
        staged = _poly_matrix_multiply(compressed, compressed, width)
        defect = _poly_matrix_subtract(direct, staged)
        plus = defect[0][0].get((width, width), F(0))
        minus = defect[1][1].get((width, width), F(0))
        mean = (plus + minus) / 2
        rows.append((width, plus - mean, minus - mean,
                     F(6 if width == 3 else 14),
                     F(-6 if width == 3 else -14)))
    return tuple(rows)


def _s3_multiply(left: tuple[int, ...],
                 right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(3))


def _s3_cycle_type(permutation: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(3):
        if start in seen:
            continue
        point = start
        length = 0
        while point not in seen:
            seen.add(point)
            length += 1
            point = permutation[point]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def s3_mixed_response_fixture() -> dict[str, object]:
    """Independent r=3 mixed kinetic/action response over normalized S3 Haar."""

    group = tuple(permutations(range(3)))
    group_index = {element: index for index, element in enumerate(group)}
    identity_element = (0, 1, 2)
    transpositions = tuple(
        element for element in group if _s3_cycle_type(element) == (2, 1)
    )
    potential = {
        element: F({(1, 1, 1): 0, (2, 1): 2, (3,): 5}[
            _s3_cycle_type(element)
        ])
        for element in group
    }
    width = 3
    states = tuple(product(group, repeat=width))

    def coarse_product_s3(state: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
        result = identity_element
        for element in state:
            result = _s3_multiply(element, result)
        return result

    fibers = {
        delta: tuple(row for row, state in enumerate(states)
                     if coarse_product_s3(state) == delta)
        for delta in group
    }
    isometry: Matrix = tuple(
        tuple(F(1, 6) if coarse_product_s3(state) == delta else F(0)
              for delta in group)
        for state in states
    )
    actions = tuple(
        sum((potential[element] for element in state), F(0))
        for state in states
    )
    means = tuple(
        sum((actions[row] for row in fibers[delta]), F(0)) / 36
        for delta in group
    )
    variances = tuple(
        sum(((actions[row] - means[group_index[delta]]) ** 2
             for row in fibers[delta]), F(0)) / 36
        for delta in group
    )
    centered = tuple(value - F(8) for value in actions)
    b_matrix: Matrix = tuple(
        tuple(centered[row] * isometry[row][column]
              for column in range(len(group)))
        for row in range(len(states))
    )

    def apply_fine_laplacian(matrix: Matrix) -> Matrix:
        rows: list[tuple[F, ...]] = []
        for row, state in enumerate(states):
            values = [F(width) * matrix[row][column]
                      for column in range(len(matrix[0]))]
            for coordinate in range(width):
                for transposition in transpositions:
                    neighbor = list(state)
                    neighbor[coordinate] = _s3_multiply(
                        transposition, neighbor[coordinate]
                    )
                    neighbor_row = states.index(tuple(neighbor))
                    for column in range(len(values)):
                        values[column] -= F(1, 3) * matrix[neighbor_row][column]
            rows.append(tuple(values))
        return tuple(rows)

    coarse_laplacian: Matrix = tuple(
        tuple(
            F(int(row == column))
            - sum((F(1, 3) * F(int(
                _s3_multiply(transposition, group[row]) == group[column]
            )) for transposition in transpositions), F(0))
            for column in range(len(group))
        )
        for row in range(len(group))
    )
    induced = matmul(
        matmul(transpose(isometry), apply_fine_laplacian(isometry)),
        identity(len(group)),
    )
    gamma = matmul(transpose(b_matrix), b_matrix)
    dirichlet = matmul(
        transpose(b_matrix), apply_fine_laplacian(b_matrix)
    )
    mixed_k = add(
        dirichlet,
        scale(F(29, 3), induced),
    )
    expected_k = add(
        scale(F(11), identity(len(group))),
        scale(F(47), coarse_laplacian),
    )
    mixed_coefficient = scale(F(-1), mixed_k)

    return {
        "fiber_sizes": tuple(len(fibers[delta]) for delta in group),
        "isometry": isometry,
        "means": means,
        "variances": variances,
        "coarse_laplacian": coarse_laplacian,
        "induced": induced,
        "gamma": gamma,
        "dirichlet": dirichlet,
        "mixed_k": mixed_k,
        "expected_k": expected_k,
        "mixed_coefficient": mixed_coefficient,
    }


def u1_carre_du_champ_fixture() -> dict[str, object]:
    """Exact Fourier control of the r>=3 scalar remainder mechanism.

    This is a one-edge U(1) differential-Casimir analogue, not an O(3)
    physics input.  Multiplication by cos(x_i) shifts one fine Fourier index
    by plus or minus one, while the fine Casimir is diagonal with eigenvalue
    sum_i k_i^2.
    """

    rows: list[tuple[int, int, F, F, F]] = []
    for width in (3, 4, 5):
        weights = tuple(F(index + 1) for index in range(width))
        gamma = sum((weight * weight for weight in weights), F(0)) / 2
        scalar_remainder = gamma
        for coarse_mode in range(-4, 5):
            amplitudes: dict[tuple[int, ...], F] = {}
            for coordinate, weight in enumerate(weights):
                for shift in (-1, 1):
                    fine_mode = [coarse_mode] * width
                    fine_mode[coordinate] += shift
                    key = tuple(fine_mode)
                    amplitudes[key] = amplitudes.get(key, F(0)) + weight / 2
            exact = sum(
                (amplitude * amplitude
                 * sum((index * index for index in fine_mode), 0)
                 for fine_mode, amplitude in amplitudes.items()),
                F(0),
            )
            induced_kinetic = F(width * coarse_mode * coarse_mode)
            predicted = gamma * induced_kinetic + scalar_remainder
            rows.append((width, coarse_mode, exact, predicted, gamma))
    return {
        "rows": tuple(rows),
        "exact_decomposition": all(exact == predicted
                                   for _r, _k, exact, predicted, _gamma in rows),
        "even_modes": all(
            next(exact for row_width, row_mode, exact, _predicted, _gamma in rows
                 if row_width == width and row_mode == mode)
            == next(exact for row_width, row_mode, exact, _predicted, _gamma in rows
                    if row_width == width and row_mode == -mode)
            for width in (3, 4, 5) for mode in range(5)
        ),
        "scalar_accumulation": all(
            gamma == sum(F(index * index, 2)
                         for index in range(1, width + 1))
            for width, _mode, _exact, _predicted, gamma in rows
        ),
    }


def main() -> int:
    matrix = matrix_fixture()
    z2 = z2_conditional_fixture()
    general = general_r_response_fixture()
    complete = complete_step_response_fixture()
    mixed = s3_mixed_response_fixture()
    carre = u1_carre_du_champ_fixture()

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
        (
            "conditioned product fibers are proper-subset Haar through r=5",
            general["subset_independence"],
        ),
        (
            "general-r variance is scalar for r>=3 and response is nonconstant",
            all(variance and nonconstant
                for _width, variance, _response, nonconstant in general["rows"]),
        ),
        (
            "general-r nonconstant response has exact (-1)^r(2^r-2) coefficient",
            all(response for _width, _variance, response, _nonconstant
                in general["rows"]),
        ),
        (
            "complete M C M step preserves the rth response coefficient",
            all(plus == expected_plus and minus == expected_minus
                for _width, plus, minus, expected_plus, expected_minus in complete),
        ),
        (
            "S3 normalized product fibers and induced kinetic intertwiner",
            set(mixed["fiber_sizes"]) == {36}
            and matmul(transpose(mixed["isometry"]), mixed["isometry"])
            == identity(6)
            and mixed["induced"] == scale(F(3), mixed["coarse_laplacian"]),
        ),
        (
            "S3 conditional mean and variance are fiber independent",
            set(mixed["means"]) == {F(8)}
            and set(mixed["variances"]) == {F(29, 3)}
            and mixed["gamma"] == scale(F(29, 3), identity(6)),
        ),
        (
            "S3 mixed quadratic response is -11 I -47 A_c",
            mixed["mixed_k"] == mixed["expected_k"]
            and mixed["mixed_coefficient"]
            == scale(F(-1), mixed["expected_k"]),
        ),
        (
            "S3 mixed response is non-scalar kinetic rather than multiplication",
            mixed["mixed_coefficient"] != scale(
                mixed["mixed_coefficient"][0][0], identity(6)
            )
            and any(mixed["mixed_coefficient"][row][column] != 0
                    for row in range(6) for column in range(6)
                    if row != column),
        ),
        (
            "S3 zero kinetic and common scalar controls preserve the boundary",
            scale(F(0), mixed["mixed_k"]) == zero(6, 6)
            and any((add(mixed["mixed_coefficient"], scale(F(7), identity(6))))[row][column] != 0
                    for row in range(6) for column in range(6)
                    if row != column),
        ),
        (
            "U1 differential-Casimir control has exact kinetic plus scalar remainder",
            carre["exact_decomposition"],
        ),
        (
            "U1 scalar remainder has no first-order Fourier drift",
            carre["even_modes"],
        ),
        (
            "U1 scalar remainder accumulates the disclosed coefficient squares",
            carre["scalar_accumulation"],
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
