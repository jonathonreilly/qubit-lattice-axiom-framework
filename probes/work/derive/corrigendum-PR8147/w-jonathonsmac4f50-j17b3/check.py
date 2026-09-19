#!/usr/bin/env python3
"""Corrigendum packet for PR #8147 (block 13, the causal Gaussian formation law): exact checks for ATTEMPT.md.

Block 13's T3: the stationary precision's symbol S_w(k) = |1 - w sum_j e^{-i k_j}|^2 = 1 - 2w sum cos k_j + w^2 (3 + 2 sum_{i<j}
cos(k_i - k_j)) (T3(i), correct); T3(ii) states that at g = 3w = 1, "along k = (u,u,u) the symbol is u^2 = K^2/9".
Checks:
 E1  the corrected formula for every gain: S_w(u,u,u) = (1 - g)^2 + 4g sin^2(u/2); at g = 1 it is 4 sin^2(u/2) = 2 - 2cos u
     (symbolic);
 E2  the original's failure: S(u,u,u) - u^2 has series -u^4/12 + u^6/360 + ...; S = 1, 2, 3, 4 at u = pi/3, pi/2, 2pi/3, pi (exact),
     against u^2 = pi^2/9, pi^2/4, 4pi^2/9, pi^2; S < u^2 at 200 points of (0, pi] (60 digits, labelled numerical); the domain on
     which the original holds is {0} (proof in ATTEMPT.md);
 E3  why block 13's runner passed: its D2 takes the level series to order 4 (terms through u^3), which is u^2; to order 6 it is
     u^2 - u^4/12 (the runner's own computation, re-run);
 E4  the transverse statement survives: on K = 0 the symbol is |k|^4/36 + O(|k|^6) (no fifth-order term; the sixth-order term is
     nonzero), and the level-direction leading term is K^2/9 (so the parabolic reading and T3(iii) are untouched);
 E5  the leading two-scale form K^2/9 + |k_perp|^4/36: the mixed term -K sum k_j^3 / 27 is of higher order under K ~ |k_perp|^2.
"""
import sys
import time

import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


u, w, e, q1, q2, K, lam = sp.symbols("u w epsilon q1 q2 K lambda", real=True)
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)


def S(wv, a, b, c):
    return 1 - 2 * wv * (sp.cos(a) + sp.cos(b) + sp.cos(c)) + wv ** 2 * (3 + 2 * (sp.cos(a - b) + sp.cos(a - c) + sp.cos(b - c)))


def main():
    # E1
    g = 3 * w
    lvl = S(w, u, u, u)
    e1 = sp.simplify(sp.expand_trig(lvl - ((1 - g) ** 2 + 4 * g * sp.sin(u / 2) ** 2))) == 0
    s1 = S(sp.Rational(1, 3), u, u, u)
    e1b = sp.simplify(s1 - 4 * sp.sin(u / 2) ** 2) == 0 and sp.simplify(s1 - (2 - 2 * sp.cos(u))) == 0
    # the modulus form, independently: |1 - 3w e^{-iu}|^2
    mod = sp.simplify(sp.expand_complex((1 - 3 * w * sp.exp(-sp.I * u)) * (1 - 3 * w * sp.exp(sp.I * u))) - lvl) == 0
    check("E1", e1 and e1b and mod, "S_w(u,u,u) = |1 - 3w e^{-iu}|^2 = (1 - g)^2 + 4g sin^2(u/2) for every w (g = 3w); at g = 1 it is 4 sin^2(u/2) = 2 - 2cos u")
    # E2
    ser = sp.series(s1 - u ** 2, u, 0, 9).removeO()
    e2a = sp.simplify(ser - (-u ** 4 / 12 + u ** 6 / 360 - u ** 8 / 20160)) == 0
    vals = {sp.pi / 3: 1, sp.pi / 2: 2, 2 * sp.pi / 3: 3, sp.pi: 4}
    e2b = all(sp.simplify(s1.subs(u, x) - v) == 0 for x, v in vals.items())
    import mpmath as mp
    mp.mp.dps = 60
    worst = max(mp.mpf(2) - 2 * mp.cos(mp.pi * j / 200) - (mp.pi * j / 200) ** 2 for j in range(1, 201))
    check("E2", e2a and e2b and worst < 0,
          "the original fails at every u != 0: S(u,u,u) - u^2 = -u^4/12 + u^6/360 - u^8/20160 + ...; S = 1, 2, 3, 4 at u = pi/3, pi/2, 2pi/3, pi "
          f"(against u^2 = pi^2/9, pi^2/4, 4pi^2/9, pi^2); numerical (60 digits): max over 200 points of (0, pi] of S - u^2 is {mp.nstr(worst, 6)} < 0")
    # E3: the runner's D2 series truncation
    ev = sp.Symbol("epsilon", real=True)
    runner_level = sp.series(s1.subs(u, ev), ev, 0, 4).removeO()
    fixed_level = sp.series(s1.subs(u, ev), ev, 0, 6).removeO()
    e3 = sp.simplify(runner_level - ev ** 2) == 0 and sp.simplify(fixed_level - (ev ** 2 - ev ** 4 / 12)) == 0
    check("E3", e3, "block 13's runner D2 computes sp.series(level, e, 0, 4), whose terms stop at e^3: it equals e^2 and the check passes; at order 6 "
          "the same series is e^2 - e^4/12, so the exact claim fails")
    # E4: the transverse plane and the level-direction leading term
    s13 = lambda a, b, c: S(sp.Rational(1, 3), a, b, c)
    tr = sp.expand(sp.series(s13(e * q1, e * q2, -e * (q1 + q2)), e, 0, 7).removeO())
    c4 = sp.simplify(tr.coeff(e, 4) - (q1 ** 2 + q1 * q2 + q2 ** 2) ** 2 / 9) == 0
    c5 = sp.simplify(tr.coeff(e, 5)) == 0
    c6 = sp.simplify(tr.coeff(e, 6)) != 0
    k4 = sp.simplify((2 * (q1 ** 2 + q1 * q2 + q2 ** 2)) ** 2 / 36 - (q1 ** 2 + q1 * q2 + q2 ** 2) ** 2 / 9) == 0
    lead = sp.simplify(sp.series(s13(e, e, e), e, 0, 3).removeO() - (3 * e) ** 2 / 9) == 0
    check("E4", c4 and c5 and c6 and k4 and lead,
          "on the transverse plane K = 0 the symbol is |k|^4/36 + O(|k|^6) (e^4 coefficient (q1^2 + q1 q2 + q2^2)^2/9 = |k|^4/36, no e^5 term, "
          "a nonzero e^6 term); along the level direction the leading term is K^2/9 (K = 3u): T3(ii)'s transverse clause, the parabolic "
          "reading and T3(iii) do not use the exact level value")
    # E5: the two-scale leading form
    lam_ = sp.Symbol("lam", positive=True)
    a1, a2 = sp.symbols("a1 a2", real=True)
    # k = (K/3)(1,1,1) + k_perp, k_perp = (a1, a2, -a1 - a2); parabolic scaling K = lam^2 Kt, k_perp = lam (a1, a2, -a1-a2)
    Kt = sp.Symbol("Kt", real=True)
    kk = [Kt * lam_ ** 2 / 3 + lam_ * a1, Kt * lam_ ** 2 / 3 + lam_ * a2, Kt * lam_ ** 2 / 3 - lam_ * (a1 + a2)]
    ser5 = sp.expand(sp.series(s13(*kk), lam_, 0, 5).removeO())
    kperp4 = (2 * (a1 ** 2 + a1 * a2 + a2 ** 2)) ** 2 / 36
    e5 = sp.simplify(ser5.coeff(lam_, 4) - (Kt ** 2 / 9 + kperp4)) == 0 and all(sp.simplify(ser5.coeff(lam_, m)) == 0 for m in range(0, 4))
    check("E5", e5, "under the parabolic scaling K = lam^2 Kt, k_perp = lam a, the symbol is lam^4 (Kt^2/9 + |a|^4/36) + O(lam^5): the stated "
          "leading form K^2/9 + |k_perp|^4/36 holds (as an expansion)")
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("corrigendum for PR #8147: T3(ii)'s level-line value is S(u,u,u) = 4 sin^2(u/2) = K^2/9 - K^4/972 + O(K^6) (K = 3u), and for every gain "
            "(1 - g)^2 + 4g sin^2(u/2); the stated u^2 holds only at u = 0 (as the leading term otherwise); the runner's D2 passed because its "
            "level series stops at order 3; the transverse clause, the leading parabolic form K^2/9 + |k_perp|^4/36, T3(i), T3(iii) and every "
            "later campaign note are unaffected")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S5, finite facts CHECKED here) " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
