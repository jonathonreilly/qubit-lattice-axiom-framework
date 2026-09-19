#!/usr/bin/env python3
"""J:attack-g:PR8147 — pattern (g) PROOF STEP BY BRUTE FORCE.

T3(ii) of the block 13 note states, as a finite trigonometric fact along the
level line, that at g=1 (w=1/3) 'along k=(u,u,u) the symbol is u^2 = K^2/9
with K = sum k_j'. The proof says 'expand to fourth order', but the statement
gives u^2 with no remainder (unlike the transverse clause, which has O(|k|^6)).

This script evaluates the note's own symbol
    S(k) = |1 - w * sum_j exp(-i k_j)|^2
at w=1/3, on the line k=(u,u,u), at exact finite u in {pi/3, pi/2, pi},
and compares it with u^2 and with the closed form 4 sin^2(u/2).
"""
from __future__ import annotations

import sympy as sp

HITS = []


def symbol(w, k):
    return sp.simplify(sp.expand_complex(sp.Abs(1 - w * sum(sp.exp(-sp.I * kj) for kj in k)) ** 2))


def main():
    w = sp.Rational(1, 3)
    # T3(i) trig identity at a generic point, as a sanity check of the formula
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    S = symbol(w, (k1, k2, k3))
    expanded = (
        1
        - 2 * w * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))
        + w**2 * (3 + 2 * (sp.cos(k1 - k2) + sp.cos(k1 - k3) + sp.cos(k2 - k3)))
    )
    ok_i = sp.simplify(S - expanded) == 0
    print("T3(i) |1-w sum exp(-i k)|^2 expansion identity:", ok_i)
    if not ok_i:
        HITS.append("T3(i) expansion identity fails")

    u = sp.symbols("u", real=True)
    kline = (u, u, u)
    S_line = sp.simplify(symbol(w, kline))
    closed = sp.simplify(4 * sp.sin(u / 2) ** 2)
    print(f"exact S(u,u,u) = {S_line}")
    print(f"4 sin^2(u/2)   = {closed}")
    ok_closed = sp.simplify(S_line - closed) == 0
    print(f"S(u,u,u) == 4 sin^2(u/2): {ok_closed}")
    if not ok_closed:
        HITS.append("S(u,u,u) is not 4 sin^2(u/2)")

    # Literal statement: S is u^2
    print("literal T3(ii): S(u,u,u) == u^2 at finite u")
    for val, name in ((sp.pi / 3, "pi/3"), (sp.pi / 2, "pi/2"), (sp.pi, "pi")):
        s = sp.simplify(S_line.subs(u, val))
        u2 = sp.simplify(val**2)
        sin2 = sp.simplify(closed.subs(u, val))
        eq_u2 = sp.simplify(s - u2) == 0
        eq_sin = sp.simplify(s - sin2) == 0
        print(f"  u={name}: S={s}  u^2={u2}  4sin^2={sin2}  S==u^2? {eq_u2}  S==4sin^2? {eq_sin}")
        if not eq_u2:
            HITS.append(f"u={name}: S={s} != u^2={u2}")
        if not eq_sin:
            HITS.append(f"u={name}: S={s} != 4 sin^2(u/2)={sin2}")

    # K^2/9 with K=sum k_j = 3u is identically u^2, so the same mismatch
    K2over9 = sp.simplify((3 * u) ** 2 / 9)
    print(f"K^2/9 on the line is {K2over9} (identically u^2)")

    if HITS:
        print(
            "HIT: T3(ii) states that along k=(u,u,u) the symbol is u^2 = K^2/9; "
            "the exact symbol is |1-e^{-iu}|^2 = 4 sin^2(u/2), which is not u^2 at "
            "u=pi/3, pi/2, pi. " + "; ".join(HITS)
        )
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on T3(ii) level-line "
            "symbol - the stated identity S(u,u,u)=u^2 fails at finite u; the exact "
            "value is 4 sin^2(u/2) (equals u^2 only through O(u^2))."
        )
        return 0
    print(
        "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on T3(ii) level-line "
        "symbol - S(u,u,u)=u^2 holds at the checked u; no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
