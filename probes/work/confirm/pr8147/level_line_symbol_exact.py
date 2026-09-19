#!/usr/bin/env python3
"""J:confirm:J-attack-g-PR8147 -- independent test of block 13's T3(ii) level-line sentence (PR #8147).

Statement tested (note, Theorem T3(ii)): "At g = 1 (w = 1/3), along k = (u,u,u) the symbol is u^2 = K^2/9 with
K = sum k_j, and on the transverse plane K = 0 it is |k|^4/36 + O(|k|^6)". The symbol is the note's T3(i) form
S(k) = 1 - 2w sum cos k_j + w^2 (3 + 2 sum_{i<j} cos(k_i - k_j)).

Machinery (the finder simplified |1 - w sum e^{-ik_j}|^2 in sympy at three points):
  1. the T3(i) cosine form restricted to the line by hand: at w = 1/3 it is 1 - 2 cos u + (1/9)(3 + 6) = 2 - 2 cos u,
     checked in exact rational arithmetic at the twelve points u = 2 pi m/12 (cos in Q(sqrt 3)), against u^2;
  2. a proof-by-inequality that S(u,u,u) < u^2 for every 0 < |u| <= pi: S/u^2 = (sin(u/2)/(u/2))^2 < 1, checked on a
     fine grid with mpmath at 50 digits;
  3. the series: S(u,u,u) = u^2 - u^4/12 + u^6/360 - ... (so K^2/9 is the leading term only), and the transverse
     clause |k|^4/36 + O(|k|^6) checked to sixth order, to show only the level clause lacks its remainder.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def symbol_cos_form(w, k1, k2, k3):
    return 1 - 2 * w * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) + w ** 2 * (3 + 2 * (sp.cos(k1 - k2) + sp.cos(k1 - k3) + sp.cos(k2 - k3)))


def main():
    w = sp.Rational(1, 3)
    u = sp.Symbol("u", real=True)
    line = sp.simplify(symbol_cos_form(w, u, u, u))
    closed_ok = sp.simplify(line - (2 - 2 * sp.cos(u))) == 0
    print(f"1. T3(i) cosine form on the line at w = 1/3: {line}; equals 2 - 2 cos u: {closed_ok}")
    diffs = []
    for m in range(1, 13):
        val = 2 * sp.pi * m / 12
        S = sp.nsimplify(sp.simplify(line.subs(u, val)))
        gap = sp.N(S - val ** 2, 20)
        diffs.append((m, S, gap))
    print("   exact S at u = 2 pi m/12 against u^2: " + "; ".join(f"m={m}: S={S}, S-u^2={float(g):.6f}" for m, S, g in diffs))

    mp.mp.dps = 50
    worst_ratio = mp.mpf(0)
    n = 4000
    for i in range(1, n + 1):
        x = mp.pi * i / n
        S = 2 - 2 * mp.cos(x)
        r = S / x ** 2
        worst_ratio = max(worst_ratio, r)
    print(f"2. max over 0 < u <= pi of S(u,u,u)/u^2 on a {n}-point grid (50 digits): {mp.nstr(worst_ratio, 20)} (< 1: S < u^2 there)")

    ser = sp.series(line, u, 0, 8).removeO()
    print(f"3. S(u,u,u) = {sp.expand(ser)} + O(u^8)")
    q1, q2, e = sp.symbols("q1 q2 epsilon", real=True)
    trans = sp.series(symbol_cos_form(w, e * q1, e * q2, -e * (q1 + q2)), e, 0, 7).removeO()
    k2 = e ** 2 * (q1 ** 2 + q2 ** 2 + (q1 + q2) ** 2)
    quartic_ok = sp.simplify(sp.expand(trans).coeff(e, 4) * e ** 4 - k2 ** 2 / 36) == 0
    has6 = sp.simplify(sp.expand(trans).coeff(e, 6)) != 0
    print(f"   transverse plane: order-4 term equals |k|^4/36: {quartic_ok}; a nonzero order-6 term is present (stated as O(|k|^6)): {has6}")

    exact_false = all(abs(float(g)) > 1e-9 for m, S, g in diffs if m < 12)
    if closed_ok and exact_false and worst_ratio < 1 and quartic_ok:
        print(f"HIT: confirmed - T3(ii)'s sentence 'along k = (u,u,u) the symbol is u^2 = K^2/9' is exact-false: the T3(i) symbol at "
              f"w = 1/3 is 2 - 2 cos u = 4 sin^2(u/2) on the line, e.g. S = 1 at u = pi/3, 3 at 2pi/3, 4 at pi (u^2 = 1.097, 4.386, "
              f"9.870), and S < u^2 for every 0 < |u| <= pi (max S/u^2 on the grid {mp.nstr(worst_ratio, 8)}); the series is "
              f"u^2 - u^4/12 + u^6/360 - ..., so K^2/9 is the leading term only, while the transverse clause carries its O(|k|^6)")
        print("SUMMARY: confirmed - the level-direction clause of T3(ii) omits its remainder (the claim_scope's 'expansion' and the "
              "runner's D2 series check are the correct reading); exact level-line symbol 4 sin^2(u/2) = u^2 - u^4/12 + O(u^6)")
    else:
        print(f"SUMMARY: not reproduced - closed form {closed_ok}, exact gaps {exact_false}, ratio {worst_ratio}")


if __name__ == "__main__":
    main()
