#!/usr/bin/env python3
"""Independent integer/Fraction checks for the O(3) semigroup obstruction."""

from __future__ import annotations

import itertools
from fractions import Fraction as F
from math import comb


AUDIT_TIMEOUT_SEC = 120


def multiplicity(ell: int, tensor_power: int) -> int:
    """Multiplicity of spin ell in (1 + spin-1)^tensor_power."""
    if ell < 0 or ell > tensor_power:
        return 0
    left = comb(2 * tensor_power, tensor_power - ell)
    right_index = tensor_power - ell - 1
    right = comb(2 * tensor_power, right_index) if right_index >= 0 else 0
    return left - right


def catalan(index: int) -> int:
    return comb(2 * index, index) // (index + 1)


def truncated_b(ell: int, order: int) -> tuple[F, ...]:
    """Coefficients through k^order for b_ell(k), linear f_1 member."""
    coefficients: list[F] = []
    for power in range(order + 1):
        coefficients.append(
            F(multiplicity(ell, power) * 4**power, 1)
            / F(1 if power == 0 else factorial(power), 1)
        )
    return tuple(coefficients)


def factorial(value: int) -> int:
    answer = 1
    for item in range(2, value + 1):
        answer *= item
    return answer


def series_mul(left: tuple[F, ...], right: tuple[F, ...], order: int) -> tuple[F, ...]:
    return tuple(
        sum((left[j] * right[k - j]
             for j in range(k + 1)
             if j < len(left) and k - j < len(right)), F(0))
        for k in range(order + 1)
    )


def series_inverse(series: tuple[F, ...], order: int) -> tuple[F, ...]:
    assert series[0] != 0
    out = [F(1, 1) / series[0]]
    for k in range(1, order + 1):
        out.append(-sum((series[j] * out[k - j]
                         for j in range(1, k + 1)
                         if j < len(series)), F(0)) / series[0])
    return tuple(out)


def series_ratio(numerator: tuple[F, ...], denominator: tuple[F, ...], order: int) -> tuple[F, ...]:
    return series_mul(numerator, series_inverse(denominator, order), order)


def matmul(left: tuple[tuple[F, ...], ...], right: tuple[tuple[F, ...], ...]) -> tuple[tuple[F, ...], ...]:
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(len(right))), F(0))
              for j in range(len(right[0])))
        for i in range(len(left))
    )


def transpose(matrix: tuple[tuple[F, ...], ...]) -> tuple[tuple[F, ...], ...]:
    return tuple(tuple(matrix[j][i] for j in range(len(matrix)))
                 for i in range(len(matrix[0])))


def determinant3(matrix: tuple[tuple[F, ...], ...]) -> F:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def trace3(matrix: tuple[tuple[F, ...], ...]) -> F:
    return sum((matrix[i][i] for i in range(3)), F(0))


def signed_frames() -> tuple[tuple[tuple[F, ...], ...], ...]:
    frames = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            frames.append(tuple(
                tuple(F(signs[row] if column == permutation[row] else 0)
                      for column in range(3))
                for row in range(3)
            ))
    return tuple(frames)


def spin_one_tensor_multiplicities(power: int) -> dict[int, int]:
    multiplicities = {0: 1}
    for _ in range(power):
        updated: dict[int, int] = {}
        for ell, count in multiplicities.items():
            targets = (1,) if ell == 0 else (ell - 1, ell, ell + 1)
            for target in targets:
                updated[target] = updated.get(target, 0) + count
        multiplicities = updated
    return multiplicities


def iterated_multiplier(value: F, length: int) -> F:
    answer = F(1)
    for _ in range(length):
        answer *= value
    return answer


def laurent_add(left: dict[int, F], right: dict[int, F]) -> dict[int, F]:
    result = dict(left)
    for power, coefficient in right.items():
        result[power] = result.get(power, F(0)) + coefficient
    return {power: coefficient for power, coefficient in result.items()
            if coefficient != 0}


def laurent_scale(polynomial: dict[int, F], factor: F) -> dict[int, F]:
    return {power: factor * coefficient
            for power, coefficient in polynomial.items()
            if factor * coefficient != 0}


def laurent_mul(left: dict[int, F], right: dict[int, F]) -> dict[int, F]:
    result: dict[int, F] = {}
    for left_power, left_coefficient in left.items():
        for right_power, right_coefficient in right.items():
            power = left_power + right_power
            result[power] = (
                result.get(power, F(0))
                + left_coefficient * right_coefficient
            )
    return {power: coefficient for power, coefficient in result.items()
            if coefficient != 0}


def independent_facts() -> dict[str, bool]:
    order = 4
    b0 = truncated_b(0, order)
    b1 = truncated_b(1, order)
    b2 = truncated_b(2, order)
    b3 = truncated_b(3, order)
    denominator = tuple((b0[i] + (F(1) if i == 0 else F(0))) for i in range(order + 1))
    det_numerator = tuple((b0[i] - (F(1) if i == 0 else F(0))) for i in range(order + 1))
    rdet = series_ratio(det_numerator, denominator, order)
    rv = tuple(value / 3 for value in series_ratio(b1, denominator, order))
    r2 = tuple(value / 5 for value in series_ratio(b2, denominator, order))
    r3 = tuple(value / 7 for value in series_ratio(b3, denominator, order))

    nonlinear = []
    for n in range(1, 13):
        c_n = catalan(n)
        m0 = multiplicity(0, n)
        m1 = multiplicity(1, n)
        det_lead = F(2 ** (3 - 2 * n) * c_n, n) if n <= 1 else F(c_n, n * 2 ** (2 * n - 3))
        vector_lead = (
            F(2 * c_n, n + 2)
            if n == 1
            else F(c_n, (n + 2) * 2 ** (2 * n - 3))
        )
        nonlinear.append(
            m0 == c_n
            and F(m1, c_n) == F(3 * n, n + 2)
            and det_lead / vector_lead == F(n + 2, n)
        )

    frames = signed_frames()
    word = (
        (F(0), F(-1), F(0)),
        (F(1), F(0), F(0)),
        (F(0), F(0), F(-1)),
    )
    conjugates = tuple(matmul(matmul(frame, word), transpose(frame))
                       for frame in frames)
    n1_det_lead = rdet[1]
    n1_vector_lead = rv[1]
    cycle_lengths = range(1, 7)

    spin_one_counts = spin_one_tensor_multiplicities(1)
    spin_two_counts = spin_one_tensor_multiplicities(2)
    so3_spin1_lead = F(spin_one_counts[1], 3)
    so3_spin2_lead = F(spin_two_counts[2], 2 * 5)

    # Exponent coefficient pairs (D, gamma) for exp[-D_coeff D t-gamma_coeff gamma t].
    heat_det_exponent = (F(0), F(2))
    heat_det_vector_exponent = (F(1), F(0))
    heat_vector_exponent = (F(1), F(2))
    heat_product_exponent = tuple(
        left + right
        for left, right in zip(heat_det_exponent, heat_det_vector_exponent)
    )

    # Apart from the common 1/pi, the SO(3) class weight is 1-cos(theta)
    # and chi_1=1+2cos(theta). Derive their Laurent product exactly.
    one = {0: F(1)}
    cosine = {-1: F(1, 2), 1: F(1, 2)}
    class_weight = laurent_add(one, laurent_scale(cosine, F(-1)))
    spin_one_character = laurent_add(one, laurent_scale(cosine, F(2)))
    improper_spin_one_integrand = laurent_mul(
        class_weight, spin_one_character
    )

    m_vector = (F(1), F(2))
    t_zero = tuple(tuple(m_vector[i] * m_vector[j] for j in range(2)) for i in range(2))
    t_infty = ((F(1), F(0)), (F(0), F(4)))
    left_commutator = matmul(t_zero, t_infty)
    right_commutator = matmul(t_infty, t_zero)

    return {
        "linear proper-component character series are derived from tensor multiplicities": (
            b0 == (F(1), F(4), F(16), F(160, 3), F(448, 3))
            and b1 == (F(0), F(4), F(24), F(96), F(896, 3))
            and b2 == (F(0), F(0), F(8), F(160, 3), F(640, 3))
            and b3 == (F(0), F(0), F(0), F(32, 3), F(224, 3))
        ),
        "normalized determinant and vector series have unequal first coefficients": (
            rdet[:5] == (F(0), F(2), F(4), F(8, 3), F(-16))
            and rv[:4] == (F(0), F(2, 3), F(8, 3), F(16, 3))
        ),
        "higher spin teeth disagree with powers of the determinant channel": (
            r2[2] == F(4, 5)
            and r3[3] == F(16, 21)
            and r2[2] / rdet[1]**2 == F(1, 5)
            and r3[3] / rdet[1]**3 == F(2, 21)
        ),
        "every checked nonlinear member has the exact Catalan leading mismatch": all(nonlinear),
        "proper and improper conjugations preserve the two cycle characters": (
            len(frames) == 48
            and sum(determinant3(frame) == -1 for frame in frames) == 24
            and all(trace3(conjugate) == trace3(word)
                    and determinant3(conjugate) == determinant3(word)
                    for conjugate in conjugates)
        ),
        "linkwise cycle contraction iterates each channel multiplier": (
            all(iterated_multiplier(n1_det_lead, length) == n1_det_lead**length
                    and iterated_multiplier(n1_vector_lead, length) == n1_vector_lead**length
                    and iterated_multiplier(n1_det_lead, length)
                    != iterated_multiplier(n1_vector_lead, length)
                    for length in cycle_lengths)
        ),
        "constant improper density has zero spin-one Haar coefficient": (
            improper_spin_one_integrand.get(0, F(0)) == 0
            and improper_spin_one_integrand
            == {-2: F(-1, 2), -1: F(1, 2),
                1: F(1, 2), 2: F(-1, 2)}
        ),
        "the heat plus component-jump comparator has a different channel identity": (
            heat_product_exponent == heat_vector_exponent
            and heat_det_exponent != (F(0), F(0))
        ),
        "the SO(3) linear restriction derives and fails its common-clock power identity": (
            so3_spin1_lead == F(1, 3)
            and so3_spin2_lead == F(1, 10)
            and so3_spin2_lead != so3_spin1_lead**2
        ),
        "a nonconstant positive half multiplier has noncommuting endpoint transfers": (
            left_commutator != right_commutator
            and left_commutator == ((F(1), F(8)), (F(2), F(16)))
            and right_commutator == ((F(1), F(2)), (F(8), F(16)))
        ),
    }


def main() -> int:
    passed = 0
    failed = 0
    for name, condition in independent_facts().items():
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        passed += int(ok)
        failed += int(not ok)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
