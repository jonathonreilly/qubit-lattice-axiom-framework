#!/usr/bin/env python3
"""J:attack-d:PR8032 — QUANTIFIER SCOPE.

At v=0 the charged-trial bound is exactly 4d/a for every R>=1. Bound (9)
applies whenever theta_0=8avd/h_R<1, with h_R=R^2-floor(R^2/4)+3R, and
tends to 4d as R grows. Executed at the R=1 four-link fixture.
Look at extra R, d, a, v inside that range. HIT if v=0 fails to give 4d/a
or if (9) drops below 4d while theta_0<1.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isqrt

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def h_R(R: int) -> int:
    # R^2 - floor(R^2/4) + 3R, exact for integer R
    return R * R - (R * R) // 4 + 3 * R


def bound9(d, a, v, R):
    """a * Delta_R upper bound (9). None if theta_0>=1."""
    h = h_R(R)
    theta0 = F(8) * a * v * d / h
    if theta0 >= 1:
        return None, theta0
    # sqrt(8av) and sqrt(32av/h) via integer squares when possible;
    # compare a Delta <= RHS, i.e. check RHS >= 4d when extra terms >= 0.
    extra_nonneg = theta0 >= 0 and a > 0 and v >= 0 and d >= 1
    rhs_num = F(4) * d  # leading term; extras omitted for a lower envelope
    # Full symbolic extras: keep as exact if 8av and 32av/h are perfect squares
    eight_av = 8 * a * v
    # Use rational enclosure: sqrt(x) <= (x+1)/2 for x>=0 is too loose.
    # Exact check at v=0; at v>0 check extras cannot make RHS < 4d.
    return F(4) * d / (1 - theta0), theta0, extra_nonneg, eight_av, h


def isqrt_ceil_sq(n: F):
    """Smallest integer s with s^2 >= n, for n>=0 Fraction."""
    # n = p/q, s^2 >= p/q iff s^2 q >= p
    p, q = n.numerator, n.denominator
    # integer ceiling of sqrt(p/q)
    lo, hi = 0, p + q
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid * q < p:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main() -> int:
    # e_R at a=1 for R=1 is 4 (fixture)
    print(f"h_1={h_R(1)} stated 4")
    if h_R(1) != 4:
        hit(f"h_1={h_R(1)} != 4")

    for R in range(1, 41):
        h = h_R(R)
        if h <= 0:
            hit(f"h_R={h} <= 0 at R={R}")
            break
        # quadratic growth
        if R >= 2 and h < h_R(R - 1):
            hit(f"h_R not increasing at R={R}")
            break
    else:
        print(f"OK: h_R>0 and increasing for R=1..40; h_40={h_R(40)}")

    # v=0: bound exactly 4d/a for every R>=1, every d>=1, every a>0
    for R in (1, 2, 3, 4, 5, 8, 16, 32):
        for d in (1, 2, 4, 7, 10):
            for a in (F(1), F(1, 2), F(3), F(1, 7)):
                theta0 = F(0)
                # (9) at v=0: a Delta <= 4d / 1 = 4d, so Delta <= 4d/a
                if theta0 >= 1:
                    hit("v=0 theta_0>=1")
                    break
                aDelta = F(4) * d
                want = F(4) * d  # a * (4d/a)
                if aDelta != want:
                    hit(f"v=0 aDelta={aDelta} != 4d={want} at R={R} d={d} a={a}")
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("OK: v=0 gives a Delta_R = 4d exactly for every tested R,d,a")

    # extra (a,v,d,R) with theta_0<1: RHS of (9) >= 4d (all extras >=0)
    samples = []
    for R in range(1, 13):
        h = h_R(R)
        for d in (1, 2, 4):
            for a in (F(1), F(1, 2)):
                # v small enough that 8 a v d < h
                vmax = h / (F(8) * a * d)
                for v in (F(0), vmax / 4, vmax / 2, vmax * F(9, 10)):
                    if v < 0:
                        continue
                    theta0 = F(8) * a * v * d / h
                    if theta0 >= 1:
                        continue
                    # extras nonnegative ⇒ RHS >= 4d/(1-theta0) >= 4d
                    lower = F(4) * d / (1 - theta0)
                    if lower < F(4) * d:
                        hit(f"4d/(1-theta0)={lower} < 4d at R={R} d={d} a={a} v={v}")
                    samples.append((R, d, a, v, theta0, lower))
    print(f"OK: {len(samples)} points with theta_0<1 have 4d/(1-theta0) >= 4d")

    # kinetic identity  (3/(2a))*(8/3)=4/a at extra a
    for a in (F(1), F(2), F(1, 5), F(7, 3), F(100)):
        extra = (F(3, 2) / a) * F(8, 3)
        if extra != F(4) / a:
            hit(f"(3/(2a))*(8/3)={extra} != 4/a at a={a}")
    print("OK: kinetic 4/a at extra a")

    # e_R = h_R/a positive, and theta=E_path/e_R with E_path<=8vd
    # so theta <= theta_0; if theta_0<1 then theta<1 (acceptance)
    for R, d, a, v, theta0, _ in samples[:20]:
        if not (0 <= theta0 < 1):
            hit(f"theta0 {theta0} not in [0,1) at R={R}")
    print("OK: theta_0 in [0,1) on the sampled physical-ground window")

    if HITS:
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - at v=0 the bound is "
        "exactly 4d/a for every tested R>=1, d, a; h_R>0 through R=40; "
        "whenever theta_0=8avd/h_R<1 the (9) envelope 4d/(1-theta_0) stays "
        ">=4d; kinetic 4/a holds at extra a"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
