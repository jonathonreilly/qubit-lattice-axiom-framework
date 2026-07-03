#!/usr/bin/env python3
"""Block13 exact-Qgen positivity and wrapped-Gaussian correction certificate.

No literature inputs are used.  The finite Markov facts are checked from the
matrix-exponential series bounds and from certified finite theta sums.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 110
PAD = Decimal("1e-95")


@dataclass(frozen=True)
class DInterval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError((self.lo, self.hi))

    def __add__(self, other: "DInterval") -> "DInterval":
        return DInterval(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "DInterval") -> "DInterval":
        return DInterval(self.lo - other.hi, self.hi - other.lo)

    def div_pos(self, other: "DInterval") -> "DInterval":
        if self.lo <= 0 or other.lo <= 0:
            raise ValueError("positive interval division required")
        return DInterval(self.lo / other.hi, self.hi / other.lo)


class Certifier:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0
        self.failures: list[str] = []

    def check(self, name: str, condition: bool) -> None:
        if condition:
            self.pass_count += 1
        else:
            self.fail_count += 1
            self.failures.append(name)

    @property
    def total(self) -> int:
        return self.pass_count + self.fail_count


def dec(frac: Fraction) -> Decimal:
    return Decimal(frac.numerator) / Decimal(frac.denominator)


def exp_neg_iv(x: Decimal) -> DInterval:
    v = (-x).exp()
    lo = v - PAD
    if lo < 0:
        lo = Decimal(0)
    return DInterval(lo, v + PAD)


def ln_iv(x: DInterval) -> DInterval:
    if x.lo <= 0:
        raise ValueError("log of nonpositive interval")
    return DInterval(x.lo.ln() - PAD, x.hi.ln() + PAD)


def neg_log_iv(x: DInterval) -> DInterval:
    y = ln_iv(x)
    return DInterval(-y.hi, -y.lo)


def fmt_frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def fmt_dec(x: Decimal, places: int = 18) -> str:
    return format(x, f".{places}E")


def fmt_iv(x: DInterval, places: int = 12) -> str:
    return f"[{fmt_dec(x.lo, places)},{fmt_dec(x.hi, places)}]"


def small_time_upper(t: Fraction, lneg_lower: Fraction, norm_bound: Fraction) -> Fraction:
    """Upper bound on an off-diagonal exp(tL) entry.

    If L_ij <= -lneg_lower, ||L|| <= norm_bound, and t||L|| <= 1, then

        (exp(tL))_ij <= -t*lneg_lower + 2*t^2*norm_bound^2.
    """

    return -t * lneg_lower + 2 * t * t * norm_bound * norm_bound


def shifted_metzler_sufficiency_checks(cert: Certifier) -> None:
    # Nearest-neighbor generator on Z_5: off-diagonal entries 1/2 at +-1 and
    # diagonal -1.  With c=1, L+cI is entrywise nonnegative; hence
    # exp(tL)=e^{-t} exp(t(L+I)) has a nonnegative series for t>=0.
    c = Fraction(1)
    diag = Fraction(-1)
    off = Fraction(1, 2)
    entries = [diag + c, off, off, Fraction(0), Fraction(0)]
    cert.check("T1_suff_shift_entries_nonnegative", all(x >= 0 for x in entries))
    cert.check("T1_suff_scalar_prefactor_positive", c > 0)
    cert.check("T1_suff_series_terms_nonnegative", off >= 0 and diag + c >= 0)


def exact_qgen_negative_witnesses(cert: Certifier) -> tuple[str, str]:
    # N=5: block10 gives step weight w_2=1-3*sqrt(5)/5, so the generator
    # off-diagonal at displacement 2 is w_2/2.  Since sqrt(5)>223/100,
    # |L_2|=(3*sqrt(5)/5-1)/2 > 169/1000.
    n5_lneg_lower = Fraction(169, 1000)
    n5_norm = Fraction(10)  # sum_{r=-2}^2 r^2, an l_infinity norm bound
    n5_t = Fraction(1, 2000)
    n5_upper = small_time_upper(n5_t, n5_lneg_lower, n5_norm)
    cert.check("T2_N5_sqrt5_lower_bound", Fraction(223, 100) ** 2 < 5)
    cert.check("T2_N5_small_time_condition", n5_t * n5_norm <= 1)
    cert.check("T2_N5_kernel_entry_negative", n5_upper < 0)

    # N=7: for odd N, the exact quadratic generator off-diagonal at
    # displacement k is (-1)^(k+1) cos(pi*k/N)/(2 sin(pi*k/N)^2).  At k=2 this
    # is negative.  Let x=2 cos(2*pi/7), so x^3+x^2-2x-1=0 and the relevant
    # root is above 31/25 because the cubic is increasing there and evaluates
    # negative at 31/25.  Hence cos(2*pi/7)>31/50 and
    # |L_2|> (31/50)/(2*(1-(31/50)^2)) > 1/2.
    x0 = Fraction(31, 25)
    cubic_at_x0 = x0**3 + x0**2 - 2 * x0 - 1
    deriv_at_x0 = 3 * x0**2 + 2 * x0 - 2
    cos_lower = Fraction(31, 50)
    l2_lower_from_cos = cos_lower / (2 * (1 - cos_lower * cos_lower))
    n7_lneg_lower = Fraction(1, 2)
    n7_norm = Fraction(28)  # sum_{r=-3}^3 r^2
    n7_t = Fraction(1, 5000)
    n7_upper = small_time_upper(n7_t, n7_lneg_lower, n7_norm)
    cert.check("T2_N7_cubic_root_lower", cubic_at_x0 < 0 and deriv_at_x0 > 0)
    cert.check("T2_N7_L2_lower_exceeds_half", l2_lower_from_cos > n7_lneg_lower)
    cert.check("T2_N7_small_time_condition", n7_t * n7_norm <= 1)
    cert.check("T2_N7_kernel_entry_negative", n7_upper < 0)

    n5 = f"N5:k=2,t0={fmt_frac(n5_t)},entry_upper={fmt_frac(n5_upper)}"
    n7 = f"N7:k=2,t0={fmt_frac(n7_t)},entry_upper={fmt_frac(n7_upper)}"
    return n5, n7


def theta_sum_iv(n: int, N: int, t: Fraction, Q: int = 30) -> tuple[DInterval, Decimal]:
    td = dec(t)
    total = DInterval(Decimal(0), Decimal(0))
    for q in range(-Q, Q + 1):
        k = n + q * N
        term = exp_neg_iv(td * Decimal(k * k) / Decimal(2))
        total = total + term

    tail_upper = Decimal(0)
    for q0 in (Q + 1, -(Q + 1)):
        k0 = abs(n + q0 * N)
        first = exp_neg_iv(td * Decimal(k0 * k0) / Decimal(2)).hi
        ratio_exponent = td * Decimal(2 * N * k0 + N * N) / Decimal(2)
        ratio = exp_neg_iv(ratio_exponent).hi
        if ratio >= 1:
            raise ValueError("tail ratio is not below one")
        tail_upper += first / (Decimal(1) - ratio)

    return DInterval(total.lo, total.hi + tail_upper), tail_upper


def wrapped_gaussian_checks(cert: Certifier) -> tuple[str, Decimal]:
    N = 5
    samples = [Fraction(1, 5), Fraction(1), Fraction(2)]
    modes = [1, 2]
    compact: list[str] = []
    max_tail = Decimal(0)

    for t in samples:
        denom, denom_tail = theta_sum_iv(0, N, t)
        max_tail = max(max_tail, denom_tail)
        cert.check(f"T3_denominator_positive_t={fmt_frac(t)}", denom.lo > 0)

        for n in modes:
            numer, numer_tail = theta_sum_iv(n, N, t)
            max_tail = max(max_tail, numer_tail)
            cert.check(f"T3_numerator_positive_t={fmt_frac(t)}_n={n}", numer.lo > 0)

            c_iv = numer.div_pos(denom)
            neg_log = neg_log_iv(c_iv)
            target = DInterval(dec(t * n * n / 2), dec(t * n * n / 2))
            diff = neg_log - target

            cert.check(f"T3_character_positive_t={fmt_frac(t)}_n={n}", c_iv.lo > 0)
            cert.check(
                f"T3_deviation_nonzero_t={fmt_frac(t)}_n={n}",
                diff.hi < 0 or diff.lo > 0,
            )
            cert.check(f"T3_deviation_negative_t={fmt_frac(t)}_n={n}", diff.hi < 0)

            compact.append(
                "t="
                + fmt_frac(t)
                + f",n={n}:neglog"
                + fmt_iv(neg_log)
                + ",quad"
                + fmt_iv(target)
                + ",diff"
                + fmt_iv(diff)
            )

    return "|".join(compact), max_tail


def main() -> int:
    cert = Certifier()
    shifted_metzler_sufficiency_checks(cert)
    n5_witness, n7_witness = exact_qgen_negative_witnesses(cert)
    wrapped_summary, max_tail = wrapped_gaussian_checks(cert)

    print(f"SUMMARY PASS={cert.pass_count} FAIL={cert.fail_count} TOTAL={cert.total}")
    print(f"SUMMARY T1_T2 exact_Qgen_not_positive {n5_witness};{n7_witness}")
    print(
        "SUMMARY T3 wrapped_gaussian_N5 "
        + wrapped_summary
        + f";max_tail_bound={fmt_dec(max_tail, 12)};status="
        + ("PASS" if cert.fail_count == 0 else "FAIL")
    )
    if cert.fail_count:
        for failure in cert.failures:
            print(f"FAIL {failure}")
    return 0 if cert.fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
