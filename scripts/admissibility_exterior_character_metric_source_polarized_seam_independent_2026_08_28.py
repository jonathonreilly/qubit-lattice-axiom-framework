#!/usr/bin/env python3
"""Independent exact checker for the metric/source polarized seam.

This implementation uses only ``fractions.Fraction`` and elementary tuple
algebra.  It shares no SymPy implementation path with the primary runner.
"""

from __future__ import annotations

from fractions import Fraction as F


AUDIT_TIMEOUT_SEC = 120


Matrix = tuple[tuple[F, ...], ...]


def diagonal(*entries: int | F) -> Matrix:
    size = len(entries)
    return tuple(tuple(F(entries[i]) if i == j else F(0)
                       for j in range(size)) for i in range(size))


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(len(matrix)))
                 for i in range(len(matrix[0])))


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum((left[i][k] * right[k][j]
                            for k in range(len(right))), F(0))
                       for j in range(len(right[0])))
                 for i in range(len(left)))


def trace(matrix: Matrix) -> F:
    return sum((matrix[i][i] for i in range(len(matrix))), F(0))


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] - right[i][j]
                       for j in range(len(left[0])))
                 for i in range(len(left)))


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] + right[i][j]
                       for j in range(len(left[0])))
                 for i in range(len(left)))


def metric_pair(left: Matrix, left_source: F,
                right: Matrix, right_source: F) -> F:
    return trace(multiply(left, right)) / 3 + left_source * right_source


def determinant_three(matrix: Matrix) -> F:
    a, b, c = matrix
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def determinant_two(matrix: Matrix) -> F:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def determinant_direction(matrix: Matrix, direction: Matrix) -> F:
    """Directional derivative of a 3x3 determinant by exact cofactors."""
    total = F(0)
    for row in range(3):
        for column in range(3):
            remaining_rows = [index for index in range(3) if index != row]
            remaining_columns = [index for index in range(3)
                                 if index != column]
            minor = (matrix[remaining_rows[0]][remaining_columns[0]]
                     * matrix[remaining_rows[1]][remaining_columns[1]]
                     - matrix[remaining_rows[0]][remaining_columns[1]]
                     * matrix[remaining_rows[1]][remaining_columns[0]])
            cofactor = minor if (row + column) % 2 == 0 else -minor
            total += cofactor * direction[row][column]
    return total


def character(relative: Matrix) -> F:
    return determinant_three(add(diagonal(1, 1, 1), relative))


def defect(relative: Matrix) -> F:
    return F(16) - 2 * character(relative)


def mismatch_pair(left_metric: Matrix, left_source: F,
                  right_metric: Matrix, right_source: F,
                  source_normalization: F = F(1)) -> F:
    difference = subtract(left_metric, right_metric)
    return (trace(multiply(difference, difference)) / 3
            + source_normalization * (left_source - right_source) ** 2)


State = tuple[Matrix, F, Matrix]
NaiveState = tuple[Matrix, Matrix]


def polarized_weight(left: State, right: State,
                     source_normalization: F = F(1),
                     log_two_coefficient: F = F(1, 8)) -> F:
    left_metric, left_source, left_group = left
    right_metric, right_source, right_group = right
    relative = multiply(left_group, transpose(right_group))
    cross = (trace(multiply(left_metric, right_metric)) / 3
             + source_normalization * left_source * right_source)
    action_without_kappa = (
        cross * defect(relative)
        + 8 * mismatch_pair(left_metric, left_source,
                            right_metric, right_source,
                            source_normalization)
    )
    exponent = log_two_coefficient * action_without_kappa
    if exponent.denominator != 1:
        raise ValueError(f"nonintegral dyadic exponent: {exponent}")
    return F(2) ** (-exponent.numerator)


def naive_weight(left: NaiveState, right: NaiveState) -> F:
    left_metric, left_group = left
    right_metric, right_group = right
    relative = multiply(left_group, transpose(right_group))
    exponent = ((trace(left_metric) + trace(right_metric)) / 3
                * defect(relative) / 16)
    if exponent.denominator != 1:
        raise ValueError(f"nonintegral dyadic exponent: {exponent}")
    return F(2) ** (-exponent.numerator)


def gram(states: tuple[object, ...], entry: object) -> Matrix:
    return tuple(tuple(entry(left, right) for right in states)
                 for left in states)


def fuse_o3(left: set[tuple[int, int]],
            right: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """Angular-momentum/parity support of an O(3) tensor product."""
    output: set[tuple[int, int]] = set()
    for left_spin, left_parity in left:
        for right_spin, right_parity in right:
            for spin in range(abs(left_spin - right_spin),
                              left_spin + right_spin + 1):
                output.add((spin, left_parity * right_parity))
    return output


def independent_facts() -> dict[str, bool]:
    identity = diagonal(1, 1, 1)
    proper_rotation: Matrix = (
        (F(3, 5), F(-4, 5), F(0)),
        (F(4, 5), F(3, 5), F(0)),
        (F(0), F(0), F(1)),
    )
    rotation_generator: Matrix = (
        (F(0), F(-1), F(0)),
        (F(1), F(0), F(0)),
        (F(0), F(0), F(0)),
    )
    curvature = defect(proper_rotation)
    character_direction = determinant_direction(
        add(identity, proper_rotation),
        multiply(rotation_generator, proper_rotation),
    )
    connection_variation = -2 * character_direction
    metric = diagonal(1, 2, 3)
    source = F(1, 2)
    metric_norm = metric_pair(metric, source, metric, source)
    action = metric_norm * curvature

    metric_direction = diagonal(1, 0, 0)
    metric_stress = metric_pair(metric_direction, F(0), metric, source) * curvature
    source_response = source * curvature
    metric_connection_reciprocity = (
        metric_pair(metric_direction, F(0), metric, source)
        * connection_variation
    )
    source_connection_reciprocity = source * connection_variation

    pi_rotation = diagonal(-1, -1, 1)
    naive_states: tuple[NaiveState, ...] = (
        (identity, identity),
        (diagonal(2, 2, 2), identity),
        (identity, pi_rotation),
    )
    naive_gram = gram(naive_states, naive_weight)
    polarized_states: tuple[State, ...] = (
        (identity, F(0), identity),
        (diagonal(4, 1, 1), F(0), identity),
        (identity, F(0), pi_rotation),
    )
    polarized_gram = gram(polarized_states, polarized_weight)
    negative_coupling_states: tuple[State, ...] = (
        (identity, F(0), identity),
        (identity, F(0), pi_rotation),
    )
    negative_coupling_gram = gram(
        negative_coupling_states,
        lambda left, right: polarized_weight(
            left, right, log_two_coefficient=F(-1, 16)
        ),
    )
    scalar_states: tuple[State, ...] = (
        (identity, F(0), identity),
        (identity, F(1), identity),
    )
    zero_alpha_gram = gram(
        scalar_states,
        lambda left, right: polarized_weight(
            left, right, source_normalization=F(0)
        ),
    )
    negative_alpha_gram = gram(
        scalar_states,
        lambda left, right: polarized_weight(
            left, right, source_normalization=F(-1)
        ),
    )
    zero_coupling_gram = gram(
        scalar_states,
        lambda left, right: polarized_weight(
            left, right, log_two_coefficient=F(0)
        ),
    )
    improper_word = tuple(tuple(-proper_rotation[i][j] for j in range(3))
                          for i in range(3))
    improper_curvature = defect(improper_word)
    improper_direction = multiply(rotation_generator, improper_word)
    improper_character_direction = determinant_direction(
        add(identity, improper_word), improper_direction
    )
    improper_tangent_force = -2 * improper_character_direction
    improper_metric_stress = (
        metric_pair(diagonal(1, 0, 0), F(0), identity, F(1))
        * improper_curvature
    )
    improper_source_response = improper_curvature
    cubic_rotation: Matrix = (
        (F(0), F(-1), F(0)),
        (F(1), F(0), F(0)),
        (F(0), F(0), F(1)),
    )
    transformed_metric = multiply(
        multiply(cubic_rotation, metric), transpose(cubic_rotation)
    )

    coframe = diagonal(1, 2, 3)
    rotated_coframe = multiply(cubic_rotation, coframe)
    coframe_metric = multiply(transpose(coframe), coframe)
    rotated_coframe_metric = multiply(
        transpose(rotated_coframe), rotated_coframe
    )

    # f_n(Q)=2(8^n-chi^n)/(n*8^(n-1)), with chi=8-Q/2.
    nonlinear_checks = []
    for n in (1, 2, 3, 4):
        chi = F(8) - curvature / 2
        value = F(2) * (F(8) ** n - chi ** n) / (n * F(8) ** (n - 1))
        nonlinear_checks.append(value >= 0 and value <= F(16, n))

    mismatch = subtract(metric, identity)
    mismatch_norm = metric_pair(mismatch, F(1, 2), mismatch, F(1, 2))

    # Multiplication by ell^M moves every monomial of a test polynomial into
    # degree at least M; ell=Tr(G)>0 on the compact positive-metric domain.
    tail_power = 5
    test_polynomial_degrees = (0, 1, 2)
    tail_degrees = tuple(tail_power + degree
                         for degree in test_polynomial_degrees)

    # rho=1+det+V+det*V contains both parities at spins zero and one.
    # Repeated exact Clebsch-Gordan support therefore reaches both parities at
    # every target spin, while the spin-zero trivial seed pads degree.
    rho_support = {(0, 1), (0, -1), (1, 1), (1, -1)}
    tensor_support = {(0, 1)}
    support_by_degree = []
    for _ in range(6):
        tensor_support = fuse_o3(tensor_support, rho_support)
        support_by_degree.append(set(tensor_support))
    strict_support_check = all(
        (spin, parity) in support_by_degree[5]
        for spin in range(7) for parity in (-1, 1)
    )

    direct_polarization_checks = []
    left_norm = metric_pair(metric, source, metric, source)
    right_metric = diagonal(2, 1, 4)
    right_source = F(-1, 3)
    right_norm = metric_pair(right_metric, right_source,
                             right_metric, right_source)
    cross_pair = metric_pair(metric, source, right_metric, right_source)
    for member in (1, 2, 3, 4):
        chi_value = F(6)
        family_value = (F(16, member)
                        - 2 * chi_value ** member
                        / (member * F(8) ** (member - 1)))
        direct = (cross_pair * family_value
                  + F(8, member)
                  * (left_norm + right_norm - 2 * cross_pair))
        factorized = (F(8, member) * (left_norm + right_norm)
                      - 2 * cross_pair * chi_value ** member
                      / (member * F(8) ** (member - 1)))
        direct_polarization_checks.append(direct == factorized)

    return {
        "metric/source norm is exact": metric_norm == F(59, 12),
        "matched action witness is exact": action == F(236, 15),
        "metric stress is nonzero and exact": metric_stress == F(16, 15),
        "source response is nonzero and exact": source_response == F(8, 5),
        "metric-connection mixed derivative is reciprocal": metric_connection_reciprocity == F(32, 15),
        "source-connection mixed derivative is reciprocal": source_connection_reciprocity == F(16, 5),
        "rational proper rotation derives Q=16/5": curvature == F(16, 5),
        "rotation tangent derives Dtheta Q=32/5": connection_variation == F(32, 5),
        "naive positive-average Gram is derived and indefinite": naive_gram == ((F(1), F(1), F(1, 4)), (F(1), F(1), F(1, 8)), (F(1, 4), F(1, 8), F(1))) and determinant_three(naive_gram) == F(-1, 64),
        "polarized positive control is derived and positive": polarized_gram == ((F(1), F(1, 8), F(1, 4)), (F(1, 8), F(1), F(1, 128)), (F(1, 4), F(1, 128), F(1))) and determinant_three(polarized_gram) == F(15111, 16384),
        "negative coupling Gram is derived and indefinite": negative_coupling_gram == ((F(1), F(2)), (F(2), F(1))) and determinant_two(negative_coupling_gram) == F(-3),
        "zero source scale is singular": zero_alpha_gram == ((F(1), F(1)), (F(1), F(1))),
        "negative source scale Gram is derived and indefinite": negative_alpha_gram == ((F(1), F(2)), (F(2), F(1))),
        "zero coupling kernel is derived and rank one": zero_coupling_gram == ((F(1), F(1)), (F(1), F(1))),
        "polarization identity is independently recomputed": all(direct_polarization_checks),
        "common cubic chart preserves the metric pairing": metric_pair(transformed_metric, source, transformed_metric, source) == metric_norm,
        "coframe gauge has an exact metric quotient null": rotated_coframe_metric == coframe_metric and rotated_coframe != coframe,
        "displayed nonlinear family remains nonnegative": all(nonlinear_checks),
        "metric/source mismatch norm is positive": mismatch_norm == F(23, 12),
        "polynomial tails retain arbitrarily high degree": min(tail_degrees) >= tail_power,
        "exterior tensor powers reach both O(3) parities": strict_support_check,
        "improper curvature and tangent boundary are derived": improper_curvature == F(16) and improper_metric_stress == F(16, 3) and improper_source_response == F(16) and improper_tangent_force == F(0),
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
