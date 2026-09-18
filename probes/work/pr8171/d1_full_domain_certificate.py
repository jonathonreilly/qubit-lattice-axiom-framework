#!/usr/bin/env python3
"""J:falsifier:PR8171 - block 27 (PR #8171), falsifier bullet 3 (D1): "A(delta)/delta outside [1/3 - delta^2/45, 1/3) at some delta > 0",
A(x) = coth x - 1/x.  The runner checks the series and the bounds at rational points; here the statement (T4) is tested on the whole
half-line (0, oo), exactly, by machinery disjoint from the runner's:
  (a) (0, 3]: the Taylor series A(x)/x = sum_{n>=1} c_n x^{2n-2}, c_n = 2^{2n} B_{2n}/(2n)! (exact Bernoulli numbers), so
      g(x) := A(x)/x - 1/3 + x^2/45 = sum_{n>=3} c_n x^{2n-2}; the signs of c_n alternate from c_3 = 2/945 > 0, and the terms decrease in
      modulus for every x <= 3 (checked exactly for n = 3..N, and beyond N from |B_{2n}| = 2 (2n)! zeta(2n)/(2 pi)^{2n} with
      1 <= zeta(2n) <= 1 + 2^{2-2n}); hence c_3 x^4 - |c_4| x^6 <= g(x) <= c_3 x^4, which puts A(x)/x in [1/3 - x^2/45, 1/3) on (0, 3]
      as soon as 2/945 - x^2/4725 > 0 and x^2/45 - 2x^4/945 > 0 there;
  (b) [3, sqrt 15]: on each cell [a, b] of a rational grid, A(x) >= coth b - 1/a and A(x) <= coth a - 1/b (both terms monotone), with
      coth enclosed by exact exponential series bounds, so A(x)/x >= (coth b - 1/a)/b and <= (coth a - 1/b)/a; the lower bound is compared
      with 1/3 - a^2/45 and the upper bound with 1/3, exactly;
  (c) [sqrt 15, oo): 1/3 - x^2/45 <= 0 < A(x)/x and A(x)/x < 1/x <= 1/sqrt 15 < 1/3 (0 < A < 1 from coth x > 1/x and coth x > 1 ... used
      only through the exact inequalities e^{2x} > 1 + 2x + 2x^2);
  (d) an independent dense scan: 200000 points on (0, 100] (logarithmic) with 40-digit mpmath arithmetic.
HIT if any cell or point violates [1/3 - x^2/45, 1/3).  Exact rationals for (a)-(c); deterministic.
"""
import sys
import time
from fractions import Fraction as Fr

import sympy as sp
import mpmath as mp

N_EXACT = 80                        # coefficients c_n checked exactly for n <= N_EXACT
GRID = Fr(1, 200)                   # cell width on [3, sqrt 15]
X_SERIES = Fr(3)                    # the series region (0, X_SERIES]


def c_coef(n):
    return Fr(2) ** (2 * n) * Fr(sp.bernoulli(2 * n)) / Fr(sp.factorial(2 * n))


def exp_bounds(x, n=None):
    """exact rational enclosure of e^x for rational x >= 0: partial sum and partial sum + geometric tail bound."""
    n = n if n is not None else int(3 * x) + 40
    s, term = Fr(0), Fr(1)
    for k in range(n + 1):
        s += term
        term = term * x / (k + 1)
    assert x < n + 2
    return s, s + term / (1 - x / (n + 2))


def coth_bounds(x):
    lo, hi = exp_bounds(2 * x)
    return (hi + 1) / (hi - 1), (lo + 1) / (lo - 1)       # coth = (E + 1)/(E - 1), decreasing in E


def part_a():
    c = {n: c_coef(n) for n in range(1, N_EXACT + 2)}
    ok_first = c[1] == Fr(1, 3) and c[2] == Fr(-1, 45) and c[3] == Fr(2, 945) and c[4] == Fr(-1, 4725)
    alt = all((c[n] > 0) == (n % 2 == 1) for n in range(3, N_EXACT + 2))
    x2 = X_SERIES ** 2
    dec = all(abs(c[n + 1]) * x2 < abs(c[n]) for n in range(3, N_EXACT + 1))
    # beyond N_EXACT: |c_{n+1}| x^2/|c_n| = x^2 zeta(2n+2)/(pi^2 zeta(2n)) <= x^2 (1 + 2^{-2n})/pi^2 with pi^2 > 9.869 (pi > 3.1415)
    tail_ratio = x2 * (1 + Fr(1, 2 ** (2 * N_EXACT))) / (Fr(31415, 10000) ** 2)
    ok_tail = tail_ratio < 1
    # bounds on (0, 3]: g >= x^4 (2/945 - x^2/4725) > 0 needs x^2 < 10; A/x < 1/3 needs x^2/45 - 2x^4/945 > 0, i.e. x^2 < 10.5
    ok_bounds = x2 < 10 and x2 < Fr(21, 2)
    print(f"[a] series region (0, {X_SERIES}]: c_1..c_4 = {c[1]}, {c[2]}, {c[3]}, {c[4]} (as stated: {ok_first}); signs alternate for n = 3..{N_EXACT + 1}: "
          f"{alt}; |c_(n+1)| x^2 < |c_n| at x = {X_SERIES} for n = 3..{N_EXACT}: {dec}; tail ratio bound beyond n = {N_EXACT}: "
          f"{float(tail_ratio):.4f} < 1: {ok_tail}; x^2 = {x2} < 10: {ok_bounds}")
    return ok_first and alt and dec and ok_tail and ok_bounds


def isqrt_frac_hi(q):
    """a rational upper bound of sqrt(q)."""
    x = Fr(int(float(q) ** 0.5 * 10 ** 6) + 1, 10 ** 6)
    while x * x < q:
        x += Fr(1, 10 ** 6)
    return x


def part_b():
    s15 = isqrt_frac_hi(Fr(15))
    a = X_SERIES
    cells = bad = 0
    worst_lo, worst_hi = None, None
    while a < s15:
        b = min(a + GRID, s15)
        cb_lo, _ = coth_bounds(b)
        _, ca_hi = coth_bounds(a)
        low = (cb_lo - 1 / a) / b                           # A(x)/x >= (coth b - 1/a)/b  on [a, b]
        up = (ca_hi - 1 / b) / a                            # A(x)/x <= (coth a - 1/b)/a  on [a, b]
        need_lo = Fr(1, 3) - a * a / 45                     # 1/3 - x^2/45 <= 1/3 - a^2/45 on [a, b]
        cells += 1
        m_lo, m_hi = low - need_lo, Fr(1, 3) - up
        if m_lo <= 0 or m_hi <= 0:
            bad += 1
        worst_lo = m_lo if worst_lo is None or m_lo < worst_lo else worst_lo
        worst_hi = m_hi if worst_hi is None or m_hi < worst_hi else worst_hi
        a = b
    print(f"[b] interval region [{X_SERIES}, sqrt 15 <= {float(s15):.6f}]: {cells} cells of width {GRID}: {bad} failing; smallest margins "
          f"A/x - (1/3 - x^2/45) >= {float(worst_lo):.6f}, 1/3 - A/x >= {float(worst_hi):.6f}")
    return bad == 0, s15


def part_c(s15):
    # x >= sqrt 15: 1/3 - x^2/45 <= 0; A(x) > 0 since e^{2x} > 1 + 2x + 2x^2 gives coth x > 1/x (exact inequality, shown symbolically);
    # A(x)/x < 1/x <= 1/sqrt 15 < 1/3 since A < 1 (coth x - 1 = 2/(e^{2x} - 1) < 1/x)
    x = sp.symbols("x", positive=True)
    e = 1 + 2 * x + 2 * x ** 2
    # coth x > 1/x  <=>  x (E + 1) > E - 1 with E = e^{2x}  <=>  E (x - 1) + x + 1 > 0: for x >= 1 obvious; x >= sqrt 15 > 1 here
    ok1 = s15 > 1
    # 2/(E - 1) < 1/x <=> E > 2x + 1, implied by E > 1 + 2x + 2x^2
    ok2 = sp.simplify(e - (2 * x + 1)) == 2 * x ** 2
    ok3 = Fr(1) / (s15 - Fr(1, 10 ** 6)) < Fr(1, 3) and Fr(1, 3) - s15 * s15 / 45 <= Fr(1, 10 ** 5)
    print(f"[c] tail region [sqrt 15, oo): lower bound non-positive there, A(x)/x < 1/sqrt 15 = {1 / 15 ** 0.5:.6f} < 1/3: {ok1 and ok2 and ok3}")
    return ok1 and ok2 and ok3


def part_d():
    mp.mp.dps = 40
    n = 200000
    lo, hi = mp.mpf("1e-4"), mp.mpf(100)
    worst_l, worst_u, arg_l = None, None, None
    fails = 0
    r = (hi / lo) ** (mp.mpf(1) / (n - 1))
    x = lo
    for i in range(n):
        A = mp.coth(x) - 1 / x
        v = A / x
        ml = v - (mp.mpf(1) / 3 - x * x / 45)
        mu = mp.mpf(1) / 3 - v
        if ml < 0 or mu <= 0:
            fails += 1
        if worst_l is None or ml < worst_l:
            worst_l, arg_l = ml, x
        if worst_u is None or mu < worst_u:
            worst_u = mu
        x = x * r
    print(f"[d] dense scan: {n} points on [1e-4, 100] (40 digits): {fails} violations; smallest lower margin {mp.nstr(worst_l, 6)} at x = "
          f"{mp.nstr(arg_l, 6)} (the series predicts 2x^4/945 there: {mp.nstr(2 * arg_l ** 4 / 945, 6)}); smallest upper margin {mp.nstr(worst_u, 6)}")
    return fails == 0


def main():
    t0 = time.time()
    a = part_a()
    b, s15 = part_b()
    c = part_c(s15)
    d = part_d()
    print(f"[time] {time.time() - t0:.0f}s")
    if not (a and b and c):
        print("HIT: D1 - the exact certificate of A(delta)/delta in [1/3 - delta^2/45, 1/3) fails in region(s): "
              + ", ".join(n for n, ok in (("(0, 3]", a), ("[3, sqrt 15]", b), ("[sqrt 15, oo)", c)) if not ok))
    if not d:
        print("HIT: D1 - the dense 40-digit scan finds A(delta)/delta outside [1/3 - delta^2/45, 1/3)")
    print(f"SUMMARY: D1 on the whole half-line: series region (0, 3] {'certified' if a else 'NOT certified'} (exact Bernoulli coefficients to n = "
          f"{N_EXACT + 1}, alternating and decreasing); [3, sqrt 15] {'certified' if b else 'NOT certified'} by exact interval cells; "
          f"[sqrt 15, oo) {'certified' if c else 'NOT certified'}; dense scan {'clean' if d else 'VIOLATED'}; falsifier "
          f"{'does not fire' if (a and b and c and d) else 'FIRES'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
