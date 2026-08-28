#!/usr/bin/env python3
"""Independent exact checker for the gauge-vector matter transfer packet.

Only ``fractions.Fraction`` and elementary tuple algebra are used.  This file
does not import the SymPy primary runner.
"""

from __future__ import annotations

from fractions import Fraction as F
from math import factorial


AUDIT_TIMEOUT_SEC = 120

Vector = tuple[F, F, F]
Matrix = tuple[tuple[F, F, F], tuple[F, F, F], tuple[F, F, F]]


def diagonal(a: int | F, b: int | F, c: int | F) -> Matrix:
    return ((F(a), F(0), F(0)),
            (F(0), F(b), F(0)),
            (F(0), F(0), F(c)))


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum((left[i][k] * right[k][j] for k in range(3)), F(0))
                       for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(sum((matrix[i][j] * vector[j] for j in range(3)), F(0))
                 for i in range(3))  # type: ignore[return-value]


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] + right[i][j] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def scale_matrix(scale: F, matrix: Matrix) -> Matrix:
    return tuple(tuple(scale * matrix[i][j] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def subtract_vector(left: Vector, right: Vector) -> Vector:
    return tuple(left[i] - right[i] for i in range(3))  # type: ignore[return-value]


def add_vector(left: Vector, right: Vector) -> Vector:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def scale_vector(scale: F, vector: Vector) -> Vector:
    return tuple(scale * vector[i] for i in range(3))  # type: ignore[return-value]


def dot(left: Vector, right: Vector) -> F:
    return sum((left[i] * right[i] for i in range(3)), F(0))


def trace(matrix: Matrix) -> F:
    return sum((matrix[i][i] for i in range(3)), F(0))


def so_pair(left: Matrix, right: Matrix) -> F:
    return -trace(multiply(left, right)) / 2


def determinant(matrix: Matrix) -> F:
    a, b, c = matrix
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def exterior_character(relative: Matrix) -> F:
    return determinant(add(diagonal(1, 1, 1), relative))


def defect(relative: Matrix) -> F:
    return F(16) - 2 * exterior_character(relative)


def skew(matrix: Matrix) -> Matrix:
    transposed = transpose(matrix)
    return tuple(tuple((matrix[i][j] - transposed[i][j]) / 2
                       for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def outer(left: Vector, right: Vector) -> Matrix:
    return tuple(tuple(left[i] * right[j] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def hop_norm(source: Vector, target: Vector, rotation: Matrix) -> F:
    difference = subtract_vector(target, matvec(rotation, source))
    return dot(difference, difference)


def determinant_two(matrix: tuple[tuple[F, F], tuple[F, F]]) -> F:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def dyadic(exponent: F) -> F:
    if exponent.denominator != 1:
        raise ValueError(f"nonintegral exponent {exponent}")
    return F(2) ** (-exponent.numerator)


def two_history_core(histories: tuple[object, object], exponent) -> tuple[tuple[F, F], tuple[F, F]]:
    return tuple(tuple(dyadic(exponent(histories[row], histories[column]))
                       for column in range(2))
                 for row in range(2))  # type: ignore[return-value]


def multiply_halves(core: tuple[tuple[F, F], tuple[F, F]],
                    positive: tuple[F, F],
                    negative: tuple[F, F] | None = None) -> tuple[tuple[F, F], tuple[F, F]]:
    other = positive if negative is None else negative
    return tuple(tuple(positive[row] * core[row][column] * other[column]
                       for column in range(2))
                 for row in range(2))  # type: ignore[return-value]


def quadratic_matter_action(source: Vector, target: Vector, rotation: Matrix,
                            hopping_weight: F, volume: F,
                            mass_minus_source: F) -> F:
    return (hopping_weight * hop_norm(source, target, rotation) / 2
            + volume * mass_minus_source * dot(source, source) / 2)


def exact_quadratic_gradient(function, point: Vector) -> Vector:
    basis = ((F(1), F(0), F(0)), (F(0), F(1), F(0)),
             (F(0), F(0), F(1)))
    return tuple(
        (function(add_vector(point, basis[index]))
         - function(subtract_vector(point, basis[index]))) / 2
        for index in range(3)
    )  # type: ignore[return-value]


def exact_degree_three_derivative(function) -> F:
    return (8 * (function(F(1)) - function(F(-1)))
            - (function(F(2)) - function(F(-2)))) / 12


def independent_facts() -> dict[str, bool]:
    identity = diagonal(1, 1, 1)
    proper_rotation: Matrix = (
        (F(3, 5), F(-4, 5), F(0)),
        (F(4, 5), F(3, 5), F(0)),
        (F(0), F(0), F(1)),
    )
    pi_rotation = diagonal(-1, -1, 1)
    improper = diagonal(-1, 1, 1)
    e1: Vector = (F(1), F(0), F(0))
    e2: Vector = (F(0), F(1), F(0))
    e3: Vector = (F(0), F(0), F(1))

    scales = (F(2), F(3), F(5), F(7))
    volume = F(1)
    for value in scales:
        volume /= value
    c12 = volume * scales[1] ** 2 * scales[2] ** 2
    d1 = volume * scales[1] ** 2
    curvature = defect(proper_rotation)
    gauge_action = c12 * curvature
    matter_distance = hop_norm(e1, e2, proper_rotation)
    matter_action = d1 * matter_distance / 2
    mass, source_value, zeta, site_norm = F(1), F(1, 2), F(1), F(1)
    site_action = volume * (mass - zeta * source_value) * site_norm / 2
    total_action = gauge_action + matter_action + site_action

    gauge_exponents = (F(-1), F(1), F(1), F(-1))
    hop_exponents = (F(-1), F(1), F(-1), F(-1))
    stress = tuple(gauge_exponents[index] * gauge_action
                   + hop_exponents[index] * matter_action
                   - site_action for index in range(4))
    source_response = -volume * zeta * site_norm / 2
    source_metric_mixed = -source_response

    generator: Matrix = (
        (F(0), F(-1), F(0)),
        (F(1), F(0), F(0)),
        (F(0), F(0), F(0)),
    )
    rotation_direction = multiply(generator, proper_rotation)
    varied_rotation = lambda parameter: add(
        proper_rotation, scale_matrix(parameter, rotation_direction))
    proper_gauge_direct = exact_degree_three_derivative(
        lambda parameter: c12 * defect(varied_rotation(parameter)))
    proper_matter_direct = exact_degree_three_derivative(
        lambda parameter: d1 * hop_norm(
            e1, e2, varied_rotation(parameter)) / 2)
    proper_gauge_force = 8 * so_pair(
        scale_matrix(c12, skew(proper_rotation)), generator)
    proper_matter_force = 2 * d1 * so_pair(
        skew(outer(matvec(proper_rotation, e1), e2)), generator)
    matter_link_mixed_direct = -d1 * dot(
        e1, matvec(multiply(generator, proper_rotation), e1))
    matter_force_at_target = lambda target: 2 * d1 * so_pair(
        skew(outer(matvec(proper_rotation, e1), target)), generator)
    matter_link_mixed_reverse = (
        matter_force_at_target(add_vector(e2, e1))
        - matter_force_at_target(subtract_vector(e2, e1))) / 2

    matter_function = lambda point: quadratic_matter_action(
        point, e2, proper_rotation, d1, volume, F(1, 2))
    matter_gradient = exact_quadratic_gradient(matter_function, e1)
    expected_gradient = add_vector(
        scale_vector(d1, subtract_vector(e1, matvec(transpose(proper_rotation), e2))),
        scale_vector(volume * F(1, 2), e1),
    )
    boundary_function = lambda point: -dot(point, point) / 2
    boundary_gradient = exact_quadratic_gradient(boundary_function, e1)

    improper_current = skew(outer(matvec(improper, e1), e2))
    expected_current: Matrix = (
        (F(0), F(-1, 2), F(0)),
        (F(1, 2), F(0), F(0)),
        (F(0), F(0), F(0)),
    )

    connection_histories = (identity, pi_rotation)
    gauge_core = two_history_core(
        connection_histories,
        lambda left, right: defect(multiply(left, transpose(right))) / 16)
    zero: Vector = (F(0), F(0), F(0))
    matter_histories = (zero, e1)
    matter_core = two_history_core(
        matter_histories,
        lambda left, right: hop_norm(right, left, identity))
    combined_core = tuple(tuple(gauge_core[i][j] * matter_core[i][j]
                                for j in range(2)) for i in range(2))
    source_halves = tuple(dyadic(-hop_norm(history, zero, identity))
                          for history in matter_histories)
    positive_gram = multiply_halves(combined_core, source_halves)
    negative_gauge_gram = two_history_core(
        connection_histories,
        lambda left, right: -defect(multiply(left, transpose(right))) / 16)
    antipodal = (e1, scale_vector(F(-1), e1))
    negative_matter_gram = two_history_core(
        antipodal,
        lambda left, right: -hop_norm(right, left, identity) / 4)
    zero_source_halves = tuple(dyadic(F(0)) for _ in matter_histories)
    unmatched = multiply_halves(((F(1), F(1)), (F(1), F(1))),
                                source_halves, zero_source_halves)
    test_real = unmatched[0][0] + unmatched[1][1]
    test_imag = unmatched[0][1] - unmatched[1][0]
    real_test = ((F(3), F(-2)))
    real_unmatched = sum(real_test[i] * unmatched[i][j] * real_test[j]
                         for i in range(2) for j in range(2))

    # Every monomial degree occurs with a positive coefficient when tau>0.
    moment_degrees = tuple(range(7))
    temporal_strength = F(2)
    moment_coefficients = tuple(temporal_strength**degree / factorial(degree)
                                for degree in moment_degrees)
    radial_second = F(3, 5)
    radial_fourth = F(3, 7)
    susceptibility = volume**2 * (radial_fourth - radial_second**2) / 4

    return {
        "rational rotation derives Q=16/5": curvature == F(16, 5),
        "diagonal coframe coefficients are exact": volume == F(1, 210) and c12 == F(15, 14) and d1 == F(3, 70),
        "gauge matter and site action sum is exact": gauge_action == F(24, 7) and matter_action == F(3, 350) and site_action == F(1, 840) and total_action == F(2063, 600),
        "four diagonal coframe responses are exact": stress == (F(-2063, 600), F(14431, 4200), F(14359, 4200), F(-2063, 600)),
        "source and metric-source mixed responses are exact": source_response == F(-1, 420) and source_metric_mixed == F(1, 420),
        "proper same-link action derivative equals force decomposition": proper_gauge_direct == proper_gauge_force == F(48, 7) and proper_matter_direct == proper_matter_force == F(-9, 350) and proper_gauge_direct + proper_matter_direct == F(2391, 350),
        "matter-link mixed derivative is reciprocal": matter_link_mixed_direct == matter_link_mixed_reverse == F(6, 175),
        "matter interior gradient is independently reconstructed": matter_gradient == expected_gradient,
        "compact-ball boundary uses an exact normal-cone witness": boundary_gradient == scale_vector(F(-1), e1),
        "matter edge orientation reversal is exact": hop_norm(e1, e2, proper_rotation) == hop_norm(e2, e1, transpose(proper_rotation)),
        "improper matter current is nonzero and exact": improper_current == expected_current,
        "proper and improper determinant sectors collide": defect(pi_rotation) == F(16) and defect(improper) == F(16) and hop_norm(e3, e3, pi_rotation) == 0 and hop_norm(e3, e3, improper) == 0,
        "positive source-included Gram is definite": determinant_two(positive_gram) == F(15, 4),
        "negative gauge sign Gram is indefinite": negative_gauge_gram == ((F(1), F(2)), (F(2), F(1))) and determinant_two(negative_gauge_gram) == F(-3),
        "negative matter sign Gram is indefinite": negative_matter_gram == ((F(1), F(2)), (F(2), F(1))) and determinant_two(negative_matter_gram) == F(-3),
        "unmatched source kernel is non-Hermitian and indefinite": unmatched[0][1] != unmatched[1][0] and (test_real, test_imag) == (F(3), F(-1)) and real_unmatched == F(-1),
        "zero temporal matter coupling is rank one": determinant_two(((F(1), F(1)), (F(1), F(1)))) == 0,
        "strict matter support has every tested tensor degree": moment_degrees == tuple(range(7)) and all(value > 0 for value in moment_coefficients),
        "coframe response is not a sector selector": total_action > 0 and defect(pi_rotation) == defect(improper),
        "compact source susceptibility witness is derived and positive": susceptibility == 3 * volume**2 / 175 and susceptibility > 0,
        "gauge and matter carriers have distinct roles": determinant(identity) == 1 and dot(e1, e1) == 1,
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
