#!/usr/bin/env python3
"""J:attack-g:PR8170 — brute-force T3's algebraic identity paragraph.

Note (T3 proof): 1-u = (4/9)[sin²(θ1/2)+sin²(θ2/2)+sin²((θ1-θ2)/2)] with
u = (3+2cos θ1+2cos θ2+2cos(θ1-θ2))/9; Q=θᵀMθ, M=(1/9)[[2,-1],[-1,2]],
det M=1/27, Q≥|θ|²/9; W=(1/108)(θ1⁴+θ2⁴+(θ1-θ2)⁴) and (θ1-θ2)⁴≤8(θ1⁴+θ2⁴)
so W≤|θ|⁴/12; Gaussian integrals
  (2π)^{-2}∫ e^{-kQ} = 3√3/(4πk),
  ∫ e^{-kQ} Q² = (3√3 π/k)(2/k²),
  ∫ e^{-k|θ|²/9} |θ|⁴ = 1458π/k³;
numerical comparisons 121.5 e/(4π)<27, 3√3/(2π)<1, 6√3/(4π)<5/2,
4√12/(9π²)≥1/7, 3/√2<π; D1 trinomial p_k by path enumeration at small k.
"""
from __future__ import annotations

import itertools
import sys
from collections import Counter
from fractions import Fraction as Fr
from math import comb

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    t1, t2 = sp.symbols("theta1 theta2", real=True)
    u = (3 + 2 * sp.cos(t1) + 2 * sp.cos(t2) + 2 * sp.cos(t1 - t2)) / 9
    rhs = (
        (4 * sp.Rational(1, 9))
        * (
            sp.sin(t1 / 2) ** 2
            + sp.sin(t2 / 2) ** 2
            + sp.sin((t1 - t2) / 2) ** 2
        )
    )
    if sp.simplify(sp.trigsimp(1 - u - rhs)) != 0:
        return hits("1-u identity fails identically")
    print("1-u identity: True")

    M = sp.Matrix([[2, -1], [-1, 2]]) / 9
    if sp.simplify(M.det() - sp.Rational(1, 27)) != 0:
        return hits("det M != 1/27")
    th = sp.Matrix([t1, t2])
    Q = (t1**2 + t2**2 + (t1 - t2) ** 2) / 9
    q_mat = (th.T * M * th)[0]
    if sp.expand(q_mat - Q) != 0:
        return hits("Q is not theta^T M theta")
    ev = sorted(sp.simplify(e) for e in M.eigenvals())
    if ev != [sp.Rational(1, 9), sp.Rational(1, 3)]:
        return hits(f"M eigenvalues {ev} != {{1/9, 1/3}}")
    # Q - |θ|²/9 = (t1²+t2²+(t1-t2)²)/9 - (t1²+t2²)/9 = (t1-t2)²/9 ≥ 0
    gap = sp.expand(Q - (t1**2 + t2**2) / 9)
    if sp.simplify(gap - (t1 - t2) ** 2 / 9) != 0:
        return hits("Q >= |theta|^2/9 identity fails")
    print(f"M det=1/27, ev={ev}, Q>=|theta|^2/9: True")

    a, b = sp.symbols("a b", real=True)
    poly = sp.expand(8 * (a**4 + b**4) - (a - b) ** 4)
    # 7a^4 + 4 a^3 b - 6 a^2 b^2 + 4 a b^3 + 7 b^4 = 7(a+b)^2 (a^2 - (6/7)ab + b^2) wait:
    # rewrite as quadratic form in (a^2, ab, b^2) SOS via exact:
    # poly = 7(a^2 - (2/7)ab wait. Direct: poly = (a+b)^2 (7a^2 - 10ab + 7b^2)? check:
    cand = (a + b) ** 2 * (7 * a**2 - 10 * a * b + 7 * b**2)
    # 7(a^4+b^4)+4ab(a^2+b^2)-6a^2b^2 vs. Better: complete the square in t=b/a.
    # f(t)=7+4t-6t^2+4t^3+7t^4; 7(t^2+1)^2 + 4t(t^2+1) - 20 t^2 — use Sturm/exact min.
    t = sp.symbols("t")
    f = 7 + 4 * t - 6 * t**2 + 4 * t**3 + 7 * t**4
    # f' = 4 - 12 t + 12 t^2 + 28 t^3 = 4(1 - 3t + 3 t^2 + 7 t^3)
    df = sp.diff(f, t)
    crit = sp.real_roots(df)
    vals = [sp.simplify(f.subs(t, r)) for r in crit] + [f.subs(t, 0), f.subs(t, 1), f.subs(t, -1)]
    # f(-1)=7-4-6-4+7=0; that is the min on R if all other values ≥0.
    if any(sp.simplify(v) < 0 for v in vals):
        return hits("(theta1-theta2)^4 <= 8(theta1^4+theta2^4) fails")
    if sp.simplify(f.subs(t, -1)) != 0:
        return hits("equality case t=-1 of the degree-4 bound is not 0")
    # W ≤ (1/12)(θ1^4+θ2^4) from the 8-bound, and that ≤ |θ|^4/12
    W = (a**4 + b**4 + (a - b) ** 4) / 108
    upper = (a**4 + b**4) / 12
    if sp.expand(upper - W) != sp.expand((8 * (a**4 + b**4) - (a - b) ** 4) / 108):
        return hits("W vs (1/12)(a^4+b^4) algebra mismatch")
    r4 = (a**2 + b**2) ** 2
    if sp.expand(r4 - (a**4 + b**4)) != sp.expand(2 * a**2 * b**2):
        return hits("|theta|^4 >= a^4+b^4 fails")
    print("(theta1-theta2)^4 <= 8(theta1^4+theta2^4) and W<=|theta|^4/12: True")

    k = sp.symbols("k", positive=True)
    detM = sp.Rational(1, 27)
    gauss_Q = sp.pi / sp.sqrt(k**2 * detM)  # ∫ e^{-k θ^T M θ} dθ
    if sp.simplify(gauss_Q - 3 * sp.sqrt(3) * sp.pi / k) != 0:
        return hits("∫ e^{-kQ} dθ != 3√3 π / k")
    scaled = gauss_Q / (4 * sp.pi**2)
    if sp.simplify(scaled - 3 * sp.sqrt(3) / (4 * sp.pi * k)) != 0:
        return hits("(2π)^{-2} ∫ e^{-kQ} != 3√3/(4π k)")
    # ∫ e^{-φ^T M φ} (φ^T M φ)^2 dφ = 2π / sqrt(det M) = 6√3 π  (2D formula)
    gauss_Q2_phi = 2 * sp.pi / sp.sqrt(detM)
    if sp.simplify(gauss_Q2_phi - 6 * sp.sqrt(3) * sp.pi) != 0:
        return hits("2D Q^2 Gaussian prefactor != 6√3 π")
    # ∫ e^{-kQ} Q^2 dθ = k^{-3} * that
    gauss_Q2 = gauss_Q2_phi / k**3
    stated_Q2 = (3 * sp.sqrt(3) * sp.pi / k) * (2 / k**2)
    if sp.simplify(gauss_Q2 - stated_Q2) != 0:
        return hits("∫ e^{-kQ} Q^2 != (3√3 π/k)(2/k^2)")
    alpha = k / 9
    # polar: 2π ∫ e^{-α r^2} r^5 dr = 2π / α^3 = 1458 π / k^3
    r4_int = 2 * sp.pi / alpha**3
    if sp.simplify(r4_int - 1458 * sp.pi / k**3) != 0:
        return hits("∫ e^{-k|θ|^2/9} |θ|^4 != 1458π/k^3")
    print("Gaussian integrals (exact): True")

    # e from 1/n!; remainder after N is < term_N * 1/(N) for N>=2
    s, term = Fr(0), Fr(1)
    for n in range(0, 24):
        s += term
        term = term / (n + 1)
    e_lo, e_hi = s, s + term
    # Machin: π/4 = 4 arctan(1/5) - arctan(1/239); alternating remainder < next term
    def arctan_encl(x: Fr, nterms: int) -> tuple[Fr, Fr]:
        tot, t, sgn = Fr(0), Fr(x), Fr(1)
        for n in range(nterms):
            tot += sgn * t / (2 * n + 1)
            t *= x * x
            sgn = -sgn
        # next term would be sgn * t / (2 nterms + 1); remainder has that sign and smaller abs
        nxt = t / (2 * nterms + 1)
        lo, hi = (tot - nxt, tot) if sgn < 0 else (tot, tot + nxt)
        return lo, hi

    a5_lo, a5_hi = arctan_encl(Fr(1, 5), 12)
    a239_lo, a239_hi = arctan_encl(Fr(1, 239), 4)
    pi_lo, pi_hi = 16 * a5_lo - 4 * a239_hi, 16 * a5_hi - 4 * a239_lo
    s3_lo, s3_hi = Fr(173205, 10**5), Fr(173206, 10**5)
    if not (s3_lo**2 < 3 < s3_hi**2):
        return hits("sqrt3 enclosure 173205/10^5 failed")
    if not (9 * e_hi < 8 * pi_lo):
        return hits("121.5 e/(4π) < 27 fails (9e < 8π)")
    # 3√3/(2π) < 1  <=>  π² > 27/4
    if not (pi_lo**2 > Fr(27, 4)):
        return hits("3√3/(2π) < 1 fails")
    # 6√3/(4π) < 5/2  <=>  π² > 27/25
    if not (pi_lo**2 > Fr(27, 25)):
        return hits("6√3/(4π) < 5/2 fails")
    # 4√12/(9π²) ≥ 1/7  <=>  56 √3 ≥ 9 π²
    if not (56 * s3_lo >= 9 * pi_hi**2):
        return hits("4√12/(9π²) >= 1/7 fails")
    # |θ|≤3/√2 < π on {Q≤1/2}: π² > 9/2
    if not (pi_lo**2 > Fr(9, 2)):
        return hits("3/√2 < π fails")
    # ρ=(12/k)^{1/4} => k ρ^4 / 12 = 1
    rho4 = 12 / k
    if sp.simplify(k * rho4 / 12 - 1) != 0:
        return hits("k ρ^4/12 != 1")
    print("numerical comparisons (exact enclosures): True")

    # D1: trinomial form of p_k by path enumeration
    steps = ((0, 0), (-1, 0), (0, -1))
    for kk in range(1, 8):
        counts: Counter[tuple[int, int]] = Counter()
        for path in itertools.product(steps, repeat=kk):
            y = (sum(p[0] for p in path), sum(p[1] for p in path))
            counts[y] += 1
        n = 3**kk
        if sum(counts.values()) != n:
            return hits(f"path count != 3^{kk}")
        Pk = Fr(0)
        for (i, j), c in counts.items():
            b, c2 = -i, -j
            a = kk - b - c2
            if a < 0 or b < 0 or c2 < 0:
                return hits(f"path landed outside the trinomial support at k={kk} y={(i,j)}")
            multi = comb(kk, b) * comb(kk - b, c2)  # k! / (a! b! c!)
            if c != multi:
                return hits(
                    f"p_k({i},{j}) count {c} != multinomial {multi} at k={kk}"
                )
            Pk += Fr(c, n) ** 2
        # closed form P_k = 9^{-k} sum_j C(k,j)^2 C(2j,j)
        closed = Fr(sum(comb(kk, j) ** 2 * comb(2 * j, j) for j in range(kk + 1)), 9**kk)
        if Pk != closed:
            return hits(f"P_{kk} enumerated {Pk} != Vandermonde form {closed}")
        print(f"k={kk} P_k={Pk} trinomial+Vandermonde: True")

    print(
        "SUMMARY: pattern has no purchase on this note: T3 1-u identity, M/det/Q/W "
        "algebra, Gaussian integrals, the stated numerical comparisons, and the "
        "trinomial p_k (k=1..7) all hold exactly as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
