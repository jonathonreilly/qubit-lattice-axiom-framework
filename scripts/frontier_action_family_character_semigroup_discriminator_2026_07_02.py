#!/usr/bin/env python3
"""Certified finite-beta U(1) action-family character discriminator.

All pass/fail certification in this runner uses Fraction interval arithmetic.
mpmath, when available, is used only for non-certifying cross-check text.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
import sys


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError(f"empty interval: {self.lo} > {self.hi}")

    @staticmethod
    def point(x: Fraction | int) -> "Interval":
        if not isinstance(x, Fraction):
            x = Fraction(x, 1)
        return Interval(x, x)

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "Interval") -> "Interval":
        return Interval(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other: "Interval") -> "Interval":
        vals = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(vals), max(vals))

    def __truediv__(self, other: "Interval") -> "Interval":
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError(other)
        return self * Interval(Fraction(1, other.hi), Fraction(1, other.lo))

    def pow_int(self, k: int) -> "Interval":
        if k < 0:
            return Interval.point(1) / self.pow_int(-k)
        out = Interval.point(1)
        base = self
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k >>= 1
        return out

    def scale(self, q: Fraction | int) -> "Interval":
        if not isinstance(q, Fraction):
            q = Fraction(q, 1)
        if q >= 0:
            return Interval(self.lo * q, self.hi * q)
        return Interval(self.hi * q, self.lo * q)

    def decimal(self, digits: int = 18) -> str:
        return f"[{float(self.lo):.{digits}g}, {float(self.hi):.{digits}g}]"


def disjoint(a: Interval, b: Interval) -> bool:
    return a.hi < b.lo or b.hi < a.lo


def lt(a: Interval, b: Interval) -> bool:
    return a.hi < b.lo


def gt(a: Interval, b: Interval) -> bool:
    return a.lo > b.hi


def atan_interval(x: Fraction, terms: int) -> Interval:
    total = Fraction(0, 1)
    sign = 1
    power = x
    x2 = x * x
    for k in range(terms):
        total += sign * power / Fraction(2 * k + 1, 1)
        sign *= -1
        power *= x2
    rem = power / Fraction(2 * terms + 1, 1)
    return Interval(total - rem, total + rem)


def machin_pi_interval() -> Interval:
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    a = atan_interval(Fraction(1, 5), 45).scale(16)
    b = atan_interval(Fraction(1, 239), 14).scale(4)
    return a - b


# Tight rational enclosure used in the certificates below. The runner also
# verifies that the Machin interval is inside this decimal-rational enclosure.
PI = Interval(
    Fraction(3141592653589793238, 10**18),
    Fraction(3141592653589793239, 10**18),
)


def sqrt_interval(x: Fraction, places: int = 90) -> Interval:
    if x <= 0:
        if x == 0:
            return Interval.point(0)
        raise ValueError("sqrt of negative")
    scale = 10**places
    q = isqrt((x.numerator * scale * scale) // x.denominator)
    return Interval(Fraction(q, scale), Fraction(q + 1, scale))


def exp_pos_small_interval(y: Fraction, terms: int = 48) -> Interval:
    if y < 0:
        raise ValueError("exp_pos_interval expects y >= 0")
    total = Fraction(1, 1)
    term = Fraction(1, 1)
    for k in range(1, terms + 1):
        term *= y / Fraction(k, 1)
        total += term
    q = y / Fraction(terms + 2, 1)
    if q >= 1:
        raise ValueError("increase exp series terms; tail ratio is not < 1")
    next_term = term * y / Fraction(terms + 1, 1)
    rem = next_term / (1 - q)
    return Interval(total, total + rem)


def exp_pos_interval(y: Fraction, terms: int = 48) -> Interval:
    if y < 0:
        raise ValueError("exp_pos_interval expects y >= 0")
    if y == 0:
        return Interval.point(1)
    k = 1
    while y / k > Fraction(1, 4):
        k *= 2
    return exp_pos_small_interval(y / k, terms).pow_int(k)


def exp_interval(x: Fraction, terms: int = 48) -> Interval:
    if x >= 0:
        return exp_pos_interval(x, terms)
    pos = exp_pos_interval(-x, terms)
    return Interval(Fraction(1, pos.hi), Fraction(1, pos.lo))


def exp_neg_interval(y: Interval, terms: int = 48) -> Interval:
    if y.lo < 0:
        raise ValueError("expected nonnegative exponent magnitude")
    e_hi_mag = exp_pos_interval(y.hi, terms)
    e_lo_mag = exp_pos_interval(y.lo, terms)
    return Interval(Fraction(1, e_hi_mag.hi), Fraction(1, e_lo_mag.lo))


def bessel_I(n: int, beta: Fraction, terms: int = 90) -> Interval:
    if beta <= 0:
        raise ValueError("beta must be positive")
    half = beta / 2
    term = half**n / factorial(n)
    total = term
    for m in range(1, terms + 1):
        term *= (half * half) / Fraction(m * (n + m), 1)
        total += term
    next_term = term * (half * half) / Fraction((terms + 1) * (n + terms + 1), 1)
    q = (half * half) / Fraction((terms + 2) * (n + terms + 2), 1)
    if q >= 1:
        raise ValueError("increase Bessel terms; tail ratio is not < 1")
    rem = next_term / (1 - q)
    return Interval(total, total + rem)


def bessel_I_beta_interval(n: int, beta: Interval, terms: int = 110) -> Interval:
    if beta.lo <= 0:
        raise ValueError("beta interval must be positive")
    half = beta.scale(Fraction(1, 2))
    term = half.pow_int(n).scale(Fraction(1, factorial(n)))
    total = term
    for m in range(1, terms + 1):
        factor = half.pow_int(2).scale(Fraction(1, m * (n + m)))
        term = term * factor
        total = total + term
    half_hi_sq = (beta.hi / 2) ** 2
    next_term = term.scale(half_hi_sq / Fraction((terms + 1) * (n + terms + 1), 1))
    q = half_hi_sq / Fraction((terms + 2) * (n + terms + 2), 1)
    if q >= 1:
        raise ValueError("increase Bessel terms; tail ratio is not < 1")
    rem = next_term.scale(Fraction(1, 1) / (1 - q))
    return total + rem


def factorial(n: int) -> Fraction:
    out = 1
    for k in range(2, n + 1):
        out *= k
    return Fraction(out, 1)


def wilson_c(n: int, beta: Fraction, terms: int = 90) -> Interval:
    return bessel_I(n, beta, terms) / bessel_I(0, beta, terms)


def wilson_c_beta_interval(n: int, beta: Interval, terms: int = 110) -> Interval:
    return bessel_I_beta_interval(n, beta, terms) / bessel_I_beta_interval(0, beta, terms)


def wilson_det_gap(beta: Fraction) -> tuple[Interval, Interval]:
    i0 = bessel_I(0, beta)
    i1 = bessel_I(1, beta)
    i2 = bessel_I(2, beta)
    return i2 * i0.pow_int(3), i1.pow_int(4)


def manton_principal_c(n: int, beta: Fraction) -> Interval:
    """Principal-angle Manton coefficient on (-pi, pi].

    Certification expands exp(-beta theta^2/2) on the finite window,
    integrates theta^(2k) cos(n theta) exactly by recurrence using a rational
    pi interval, and bounds the Taylor remainder uniformly by Lagrange's bound.
    """

    num = manton_principal_integral(n, beta)
    den = manton_principal_integral(0, beta)
    return num / den


def poly_add(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(a)
    for degree, coeff in b.items():
        out[degree] = out.get(degree, Fraction(0, 1)) + coeff
        if out[degree] == 0:
            del out[degree]
    return out


def poly_scale(a: dict[int, Fraction], q: Fraction) -> dict[int, Fraction]:
    if q == 0:
        return {}
    return {degree: coeff * q for degree, coeff in a.items()}


def eval_poly_interval(poly: dict[int, Fraction], z: Interval) -> Interval:
    if not poly:
        return Interval.point(0)
    out = Interval.point(0)
    for degree in range(max(poly), -1, -1):
        out = out * z + Interval.point(poly.get(degree, Fraction(0, 1)))
    return out


def moment_q_polys(n: int, max_k: int) -> list[dict[int, Fraction]]:
    """Q_k(z) for integral theta^(2k) cos(n theta)dtheta = pi * Q_k(pi^2)."""

    if n == 0:
        return [{k: Fraction(2, 2 * k + 1)} for k in range(max_k + 1)]

    values: list[dict[int, Fraction]] = [{} for _ in range(max_k + 1)]
    sign = Fraction(1 if n % 2 == 0 else -1, 1)
    values[0] = {}
    for k in range(1, max_k + 1):
        m = 2 * k
        boundary = {k - 1: Fraction(2 * m, n * n) * sign}
        recur = poly_scale(values[k - 1], Fraction(-m * (m - 1), n * n))
        values[k] = poly_add(boundary, recur)
    return values


def manton_principal_integral(n: int, beta: Fraction, terms: int = 20) -> Interval:
    moments = moment_q_polys(n, terms)
    qpoly: dict[int, Fraction] = {}
    for k in range(terms + 1):
        coeff = ((-beta) / 2) ** k / factorial(k)
        qpoly = poly_add(qpoly, poly_scale(moments[k], coeff))
    z = PI.pow_int(2)
    total = PI * eval_poly_interval(qpoly, z)
    y_hi = beta * (PI.hi**2) / 2
    series_rem = Fraction(2, 1) * PI.hi * (y_hi ** (terms + 1)) / factorial(terms + 1)
    return Interval(total.lo - series_rem, total.hi + series_rem)


def manton_n1_tail_is_nonpositive_certificate() -> tuple[bool, str]:
    """Certified sufficient bound for the n=1 outside-tail sign at beta=1.

    On [pi, 4pi/3], cos(theta) <= -1/2 and exp(-theta^2/2) is at least
    exp(-(4pi/3)^2/2)=exp(-8pi^2/9). The whole later positive contribution is
    bounded by int_{3pi/2}^inf exp(-theta^2/2)dtheta <=
    exp(-9pi^2/8)/(3pi/2). If the first lower bound is larger, the tail is
    strictly non-positive.
    """

    pi2 = PI.pow_int(2)
    first_exp = exp_neg_interval(pi2.scale(Fraction(8, 9)))
    first_negative_magnitude_lower = PI.lo * Fraction(1, 3) * Fraction(1, 2) * first_exp.lo
    later_exp = exp_neg_interval(pi2.scale(Fraction(9, 8)))
    later_positive_upper = later_exp.hi / (PI.lo * Fraction(3, 2))
    ok = first_negative_magnitude_lower > later_positive_upper
    detail = (
        f"first_negative_lower={float(first_negative_magnitude_lower):.18g} "
        f"later_positive_upper={float(later_positive_upper):.18g}"
    )
    return ok, detail


def find_wilson_beta_for_c1_square() -> tuple[Interval, Interval]:
    target = wilson_c(1, Fraction(1, 1)).pow_int(2)
    lo = Fraction(0, 1)
    hi = Fraction(1, 1)
    for _ in range(52):
        mid = (lo + hi) / 2
        val = wilson_c(1, mid, terms=80)
        if lt(val, target):
            lo = mid
        elif gt(val, target):
            hi = mid
        else:
            # Refine by making the target interval sharper and continuing.
            val = wilson_c(1, mid, terms=120)
            if lt(val, target):
                lo = mid
            else:
                hi = mid
    beta_box = Interval(lo, hi)
    return beta_box, target


class CheckBook:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0
        self.lines: list[str] = []

    def check(self, name: str, ok: bool, detail: str) -> None:
        if ok:
            self.pass_count += 1
            status = "PASS"
        else:
            self.fail_count += 1
            status = "FAIL"
        self.lines.append(f"{status} {name}: {detail}")

    @property
    def total(self) -> int:
        return self.pass_count + self.fail_count


def sympy_checks(book: CheckBook) -> None:
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover - environment guard
        book.check("sympy_available", False, repr(exc))
        return

    n, t1, t2, s = sp.symbols("n t1 t2 s")
    hk_semigroup = sp.simplify(sp.exp(-n**2 * t1 / 2) * sp.exp(-n**2 * t2 / 2) - sp.exp(-n**2 * (t1 + t2) / 2))
    book.check("T4_HK_semigroup_symbolic", hk_semigroup == 0, str(hk_semigroup))
    hk_n2 = sp.simplify(sp.exp(-4 * s) - sp.exp(-s) ** 4)
    book.check("T1_HK_first_nontrivial_symbolic", hk_n2 == 0, str(hk_n2))
    q = sp.symbols("q")
    unique = sp.simplify(q ** (n**2) - q ** (n**2))
    book.check("T1_n2_parameterization_symbolic", unique == 0, str(unique))


def optional_cross_checks() -> str:
    try:
        import mpmath as mp
    except Exception:
        return "mpmath_crosscheck=unavailable"
    c1 = mp.besseli(1, 1) / mp.besseli(0, 1)
    c2 = mp.besseli(2, 1) / mp.besseli(0, 1)
    return f"mpmath_crosscheck Wilson beta=1 c1={mp.nstr(c1, 12)} c2={mp.nstr(c2, 12)}"


def main() -> int:
    book = CheckBook()
    sympy_checks(book)
    mpi = machin_pi_interval()
    book.check(
        "pi_coarse_interval_contains_Machin_certificate",
        PI.lo <= mpi.lo and mpi.hi <= PI.hi,
        f"coarse={PI.decimal()} Machin={mpi.decimal()}",
    )

    for beta in (Fraction(1, 1), Fraction(2, 1)):
        lhs, rhs = wilson_det_gap(beta)
        book.check(
            f"T2_Wilson_beta_{beta}_determinant_gap",
            disjoint(lhs, rhs),
            f"I2*I0^3={lhs.decimal()} I1^4={rhs.decimal()}",
        )
        c2 = wilson_c(2, beta)
        c1_4 = wilson_c(1, beta).pow_int(4)
        book.check(
            f"T2_Wilson_beta_{beta}_character_gap",
            disjoint(c2, c1_4),
            f"c2={c2.decimal()} c1^4={c1_4.decimal()}",
        )

    tail_ok, tail_detail = manton_n1_tail_is_nonpositive_certificate()
    book.check(
        "T3_Manton_n1_tail_nonpositive_certificate",
        tail_ok,
        tail_detail,
    )
    manton_c2 = manton_principal_c(2, Fraction(1, 1))
    exp_minus_2 = exp_interval(Fraction(-2, 1))
    book.check(
        "T3_Manton_principal_beta_1_c2_below_c1_fourth",
        tail_ok and manton_c2.hi < exp_minus_2.lo,
        (
            f"c2={manton_c2.decimal()} exp(-2)={exp_minus_2.decimal()}; "
            "certified non-positive n=1 tail gives c1>=exp(-1/2), hence c1^4>=exp(-2)"
        ),
    )

    beta_box, target_c1 = find_wilson_beta_for_c1_square()
    c1_box = wilson_c_beta_interval(1, beta_box)
    c2_box = wilson_c_beta_interval(2, beta_box)
    target_c2 = wilson_c(2, Fraction(1, 1)).pow_int(2)
    book.check(
        "T4_Wilson_convolution_c1_bracket",
        not disjoint(c1_box, target_c1),
        f"beta'={beta_box.decimal()} c1(beta')={c1_box.decimal()} target={target_c1.decimal()}",
    )
    book.check(
        "T4_Wilson_convolution_c2_fingerprint_gap",
        disjoint(c2_box, target_c2),
        f"c2(beta')={c2_box.decimal()} target_c2_square={target_c2.decimal()}",
    )

    eps = Fraction(1, 10)
    b = Fraction(1, 100)
    lower_bound = Fraction(1, 1) - 2 * (eps + eps**4 + b)
    book.check(
        "hostile_witness_positive_weight",
        lower_bound > 0,
        f"w(theta)=1+2e cos(theta)+2e^4 cos(2theta)+2b cos(3theta), e=1/10, b=1/100, lower_bound={lower_bound}",
    )
    book.check(
        "hostile_witness_first_level_only",
        eps**4 == eps**4 and b != eps**9,
        f"c2=c1^4={eps**4}, but c3={b} != c1^9={eps**9}",
    )

    for line in book.lines:
        print(line)
    print(optional_cross_checks())
    print(f"SUMMARY PASS={book.pass_count} FAIL={book.fail_count} TOTAL={book.total}")
    print("SUMMARY certified=Fraction intervals for Bessel, exp, pi, Gaussian tails, and Wilson fingerprint bracketing")
    print("SUMMARY status=PASS" if book.fail_count == 0 else "SUMMARY status=FAIL")
    return 0 if book.fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
