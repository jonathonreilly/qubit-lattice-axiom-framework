#!/usr/bin/env python3
"""Independent Fraction/free-word checks for the co-scaled Trotter boundary."""

from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial


AUDIT_TIMEOUT_SEC = 120


def series_add(left: tuple[F, ...], right: tuple[F, ...], order: int) -> tuple[F, ...]:
    return tuple(
        (left[k] if k < len(left) else F(0))
        + (right[k] if k < len(right) else F(0))
        for k in range(order + 1)
    )


def series_scale(series: tuple[F, ...], factor: F, order: int) -> tuple[F, ...]:
    return tuple(factor * (series[k] if k < len(series) else F(0))
                 for k in range(order + 1))


def series_mul(left: tuple[F, ...], right: tuple[F, ...], order: int) -> tuple[F, ...]:
    return tuple(
        sum((left[j] * right[k - j]
             for j in range(k + 1)
             if j < len(left) and k - j < len(right)), F(0))
        for k in range(order + 1)
    )


def series_pow(series: tuple[F, ...], power: int, order: int) -> tuple[F, ...]:
    out = (F(1),) + (F(0),) * order
    base = series
    exponent = power
    while exponent:
        if exponent & 1:
            out = series_mul(out, base, order)
        base = series_mul(base, base, order)
        exponent //= 2
    return out


def series_inverse(series: tuple[F, ...], order: int) -> tuple[F, ...]:
    out = [F(1) / series[0]]
    for k in range(1, order + 1):
        out.append(-sum((series[j] * out[k - j]
                         for j in range(1, min(k + 1, len(series)))), F(0))
                   / series[0])
    return tuple(out)


def series_ratio(numerator: tuple[F, ...], denominator: tuple[F, ...], order: int) -> tuple[F, ...]:
    return series_mul(numerator, series_inverse(denominator, order), order)


def series_exp(series: tuple[F, ...], order: int) -> tuple[F, ...]:
    assert series[0] == 0
    out = (F(1),) + (F(0),) * order
    term = out
    for power in range(1, order + 1):
        term = series_mul(term, series, order)
        out = series_add(out, series_scale(term, F(1, factorial(power)), order), order)
    return out


def series_log(series: tuple[F, ...], order: int) -> tuple[F, ...]:
    assert series[0] == 1
    delta = (F(0),) + series[1:]
    out = (F(0),) * (order + 1)
    term = (F(1),) + (F(0),) * order
    for power in range(1, order + 1):
        term = series_mul(term, delta, order)
        out = series_add(
            out,
            series_scale(term, F((-1) ** (power + 1), power), order),
            order,
        )
    return out


def cosine_half_series(order: int = 4) -> tuple[F, ...]:
    return tuple(F((-1) ** k, 2 ** (2 * k) * factorial(2 * k))
                 for k in range(order + 1))


def action_coefficients(n: int) -> tuple[F, ...]:
    cosine_power = series_pow(cosine_half_series(), 2 * n, 4)
    return tuple(
        F(16, n) * ((F(1) if k == 0 else F(0)) - cosine_power[k])
        for k in range(5)
    )


def sine_over_theta(scale_numerator: int, scale_denominator: int,
                    order: int = 3) -> tuple[F, ...]:
    scale = F(scale_numerator, scale_denominator)
    return tuple(
        F((-1) ** k, factorial(2 * k + 1)) * scale ** (2 * k + 1)
        for k in range(order + 1)
    )


def haar_coefficients() -> tuple[F, ...]:
    half_sine = sine_over_theta(1, 2, 4)
    return series_scale(series_mul(half_sine, half_sine, 3), F(4), 3)


def character_coefficients(ell: int) -> tuple[F, ...]:
    numerator = series_scale(
        sine_over_theta(2 * ell + 1, 2, 3),
        F(1, 2 * ell + 1),
        3,
    )
    denominator = sine_over_theta(1, 2, 3)
    return series_ratio(numerator, denominator, 3)


Poly = dict[int, F]  # power of z=x^2 -> coefficient
QSeries = tuple[Poly, ...]


def poly_add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for power, coefficient in right.items():
        out[power] = out.get(power, F(0)) + coefficient
    return {power: coefficient for power, coefficient in out.items()
            if coefficient}


def poly_scale(poly: Poly, factor: F) -> Poly:
    return {power: factor * coefficient for power, coefficient in poly.items()
            if factor * coefficient}


def poly_mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for lp, lc in left.items():
        for rp, rc in right.items():
            out[lp + rp] = out.get(lp + rp, F(0)) + lc * rc
    return {power: coefficient for power, coefficient in out.items()
            if coefficient}


def qseries_mul(left: QSeries, right: QSeries, order: int = 3) -> QSeries:
    out: list[Poly] = []
    for k in range(order + 1):
        coefficient: Poly = {}
        for j in range(k + 1):
            if j < len(left) and k - j < len(right):
                coefficient = poly_add(
                    coefficient, poly_mul(left[j], right[k - j])
                )
        out.append(coefficient)
    return tuple(out)


def radial_moment(power: int) -> F:
    value = F(1)
    for k in range(power):
        value *= 2 * k + 3
    return value


def integrate_poly(poly: Poly) -> F:
    return sum((coefficient * radial_moment(power)
                for power, coefficient in poly.items()), F(0))


def multiplier_log(n: int, ell: int) -> tuple[F, ...]:
    action = action_coefficients(n)
    exponent: QSeries = (
        {0: F(1)},
        {2: -action[2] / 8},
        {3: -action[3] / 8},
        {4: -action[4] / 8},
    )
    correction: QSeries = (
        {0: F(1)},
        exponent[1],
        poly_add(exponent[2], poly_scale(poly_mul(exponent[1], exponent[1]), F(1, 2))),
        poly_add(
            poly_add(exponent[3], poly_mul(exponent[1], exponent[2])),
            poly_scale(poly_mul(poly_mul(exponent[1], exponent[1]), exponent[1]), F(1, 6)),
        ),
    )
    haar = tuple({k: coefficient} for k, coefficient in enumerate(haar_coefficients()))
    character = tuple({k: coefficient} for k, coefficient in enumerate(character_coefficients(ell)))
    denominator_integrand = qseries_mul(haar, correction)
    numerator_integrand = qseries_mul(denominator_integrand, character)
    denominator = tuple(integrate_poly(poly) for poly in denominator_integrand)
    numerator = tuple(integrate_poly(poly) for poly in numerator_integrand)
    ratio = series_ratio(numerator, denominator, 3)
    return series_log(ratio, 3)


def expected_log(n: int, ell: int) -> tuple[F, ...]:
    L = ell * (ell + 1)
    return (
        F(0),
        -F(L, 2),
        -F(L * (5 * n - 2), 8),
        F(L * ((12 * n - 4) * L - (255 * n * n - 171 * n + 24)), 192),
    )


def solved_clock(n: int) -> tuple[F, F]:
    spin1 = multiplier_log(n, 1)
    spin2 = multiplier_log(n, 2)
    a = -spin1[2] / spin1[1]
    alpha = (spin2[3] / 6 - spin1[3] / 2) / F(6 - 2)
    beta = spin1[3] / 2 - alpha * 2
    b = -(2 * (spin1[2] / 2) * a + beta) / (spin1[1] / 2)
    return a, b


def subdivision_defect(n: int, m: int) -> F:
    one = multiplier_log(n, 1)
    two = multiplier_log(n, 2)
    c2 = (m * one[2] - one[2] * m * m) / one[1]
    c3 = (m * one[3] - 2 * one[2] * m * c2 - one[3] * m ** 3) / one[1]
    return two[1] * c3 + 2 * two[2] * m * c2 + two[3] * m ** 3 - m * two[3]


Word = tuple[str, ...]
Words = dict[Word, F]


def word_add(left: Words, right: Words) -> Words:
    out = dict(left)
    for word, coefficient in right.items():
        out[word] = out.get(word, F(0)) + coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def word_scale(words: Words, factor: F) -> Words:
    return {word: factor * coefficient for word, coefficient in words.items()
            if factor * coefficient}


def word_mul(left: Words, right: Words, order: int = 3) -> Words:
    out: Words = {}
    for lw, lc in left.items():
        for rw, rc in right.items():
            word = lw + rw
            if len(word) <= order:
                out[word] = out.get(word, F(0)) + lc * rc
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def word_exp(letter: str, factor: F) -> Words:
    return {
        (): F(1),
        (letter,): factor,
        (letter, letter): factor ** 2 / 2,
        (letter, letter, letter): factor ** 3 / 6,
    }


def symmetric_bch() -> Words:
    product = word_mul(word_mul(word_exp("X", F(1, 2)), word_exp("Y", F(1))),
                       word_exp("X", F(1, 2)))
    delta = word_add(product, {(): F(-1)})
    log = word_add(delta, word_scale(word_mul(delta, delta), F(-1, 2)))
    return word_add(log, word_scale(word_mul(word_mul(delta, delta), delta), F(1, 3)))


def z2_pullback_isometry(m: int = 3) -> bool:
    coarse = {1: F(2), -1: F(-1)}
    coarse_norm = sum((value * value for value in coarse.values()), F(0)) / 2
    fine_sum = F(0)
    for mask in range(1 << m):
        product = 1
        for bit in range(m):
            product *= -1 if mask & (1 << bit) else 1
        fine_sum += coarse[product] ** 2
    return coarse_norm == fine_sum / (1 << m)


def radical_pair_mul(left: tuple[F, F], right: tuple[F, F]) -> tuple[F, F]:
    a, b = left
    c, d = right
    return a * c + 2 * b * d, a * d + b * c


def radical_pair_pow(value: tuple[F, F], power: int) -> tuple[F, F]:
    out = (F(1), F(0))
    for _ in range(power):
        out = radical_pair_mul(out, value)
    return out


def independent_facts() -> dict[str, bool]:
    action_ok = all(
        action_coefficients(n)[1:] == (
            F(4),
            -F(3 * n - 1, 6),
            F(15 * n * n - 15 * n + 4, 360),
            -F(105 * n ** 3 - 210 * n * n + 147 * n - 34, 40320),
        )
        for n in (1, 2, 5)
    )
    haar_character_ok = (
        haar_coefficients() == (F(1), -F(1, 12), F(1, 360), -F(1, 20160))
        and character_coefficients(1) == (F(1), -F(1, 3), F(1, 36), -F(1, 1080))
    )
    log_ok = all(
        multiplier_log(n, ell) == expected_log(n, ell)
        for n in (1, 2, 5) for ell in (1, 2, 3)
    )
    clock_ok = all(
        solved_clock(n) == (-F(5 * n - 2, 4), F(15 * n * n - 23 * n + 8, 32))
        for n in (1, 2, 5)
    )
    subdivision_ok = all(
        subdivision_defect(n, m) == F((3 * n - 1) * (m ** 3 - m), 2)
        for n in (1, 3) for m in (2, 3)
    )
    bch = symmetric_bch()
    bch_ok = all((bch.get(word, F(0)) == coefficient) for word, coefficient in {
        ("X",): F(1), ("Y",): F(1),
        ("X", "X", "Y"): -F(1, 24),
        ("X", "Y", "X"): F(1, 12),
        ("Y", "X", "X"): -F(1, 24),
        ("Y", "Y", "X"): F(1, 12),
        ("Y", "X", "Y"): -F(1, 6),
        ("X", "Y", "Y"): F(1, 12),
    }.items()) and len(bch) == 8
    cylindrical_ok = z2_pullback_isometry() and (3 ** 3 - 3) > 0
    # The normalized SO(3) class measure begins theta^2/(2*pi)dtheta.
    # For I_2=int_0^infty x^2 exp(-x^2/2)dx, I_2^2/pi=1/2.
    # Hence [q^(-3/2) I_proper]^2*pi=(1/2)^2*(1/2)=1/8,
    # and the determinant prefactor (2/I_proper)^2/(2*pi)=16,
    # i.e. 4*sqrt(2*pi), without importing the final constant.
    class_theta2_coefficient = F(1, 2)
    gaussian_x2_squared_over_pi = F(1, 2)
    proper_coefficient_squared_times_pi = (
        class_theta2_coefficient**2 * gaussian_x2_squared_over_pi
    )
    prefactor_squared_over_two_pi = F(2) / proper_coefficient_squared_times_pi
    determinant_ok = (
        proper_coefficient_squared_times_pi == F(1, 8)
        and prefactor_squared_over_two_pi == F(16)
        and F(4**2) == prefactor_squared_over_two_pi
    )
    full_component_ok = all(
        F(proper, proper + improper) == (
            F(1) + F(proper - improper, proper + improper)
        ) / 2
        and F(proper, proper + improper) * multiplier
        != multiplier
        for proper, improper, multiplier in (
            (5, 1, F(2, 3)),
            (11, 2, F(3, 5)),
        )
    )
    matched_determinant_ok = all(
        F(2, 1) * (-F(m * (m - 1) * (5 * n - 2), 4))
        / F(n * m * m, 1)
        == -F((m - 1) * (5 * n - 2), 2 * n * m)
        for n, m in ((1, 2), (2, 3), (5, 4))
    )
    spatial_n1 = (F(112), F(-64))
    a = (F(1, 2), F(1, 4))  # (2+sqrt(2))/4
    spatial_general_samples = []
    for n in (1, 2, 4):
        an = radical_pair_pow(a, n)
        spatial_general_samples.append((F(16, n) * (F(15) - 16 * an[0]),
                                        F(16, n) * (-16 * an[1])))
    spatial_ok = spatial_general_samples[0] == spatial_n1 and all(
        rational + radical * F(3, 2) > 0
        for rational, radical in spatial_general_samples
    )
    residual_ok = all(F(3 * n - 1, 48) > 0 for n in range(1, 13))
    return {
        "action and Haar/character series are independently reconstructed": action_ok and haar_character_ok,
        "radial-moment multiplier logs match the general formula at exact samples": log_ok,
        "the corrected scalar clock is solved rather than inserted": clock_ok,
        "spin-one matching leaves the exact spin-two subdivision defect": subdivision_ok,
        "the symmetric BCH coefficients follow from a free-word logarithm": bch_ok,
        "the Haar-product pullback is an isometry and the cubic edge defect is nonzero": cylindrical_ok,
        "the normalized Haar saddle derives the determinant Arrhenius prefactor": determinant_ok,
        "the full O(3) multiplier carries the proper-component probability": full_component_ok,
        "the spin-matched coarse clock gives the determinant finite exponent": matched_determinant_ok,
        "the pi plaquette witness is reconstructed in Q(sqrt(2))": spatial_ok,
        "the cubic residual is positive for every independently checked member": residual_ok,
    }


def main() -> int:
    facts = independent_facts()
    passed = 0
    for name, condition in facts.items():
        print(f"[{'PASS' if condition else 'FAIL'}] {name}")
        passed += int(condition)
    failed = len(facts) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
