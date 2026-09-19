#!/usr/bin/env python3
"""J:attack-d:PR8153 — QUANTIFIER SCOPE on 2(1-cos theta) <= theta^2 on [0,pi].

Typical H1/Bogoliubov E(k)=sum 2(1-cos k_i) <= |k|^2. HIT if the inequality
fails at a point in [0,pi].
"""
from __future__ import annotations

import sympy as sp

th = sp.symbols("theta", positive=True)
f = th ** 2 - 2 * (1 - sp.cos(th))
ser = sp.series(f, th, 0, 8).removeO()


def main():
    hits = []
    print(f"series theta^2-2(1-cos)={ser}")
    pts = [sp.pi / n for n in (1, 2, 3, 4, 6, 8, 12)] + [sp.Rational(1, 10), 1]
    for p in pts:
        val = f.subs(th, p).evalf(30)
        print(f"f({p})={val}")
        if val < 0:
            hits.append(f"fails at {p}: {val}")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8153): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: QUANTIFIER SCOPE on 2(1-cos theta)<=theta^2 on [0,pi] "
            "(PR #8153): nonnegative at the tested points and series starts "
            "theta^4/12; no in-range failure"
        )


if __name__ == "__main__":
    main()
