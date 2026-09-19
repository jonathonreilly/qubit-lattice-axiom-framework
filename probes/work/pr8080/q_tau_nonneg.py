#!/usr/bin/env python3
"""J:attack-d:PR8080 — QUANTIFIER SCOPE on Q_tau(lambda)-lambda^{-2} >= 0 for lambda>=delta.

Note: Q_tau(lambda)=(3 tau-2 lambda)/tau^3 + A (lambda-tau)^2,
A=(tau+2 delta)/(delta^2 tau^3), claimed nonnegative for every lambda>=delta>0,
tau>0, via the displayed factorization.
HIT if the factorization fails or the difference is negative at a point in range.
"""
from __future__ import annotations

from fractions import Fraction as F

import sympy as sp

lam, tau, delta = sp.symbols("lambda tau delta", positive=True)
A = (tau + 2 * delta) / (delta ** 2 * tau ** 3)
Q = (3 * tau - 2 * lam) / tau ** 3 + A * (lam - tau) ** 2
claimed = (lam - delta) * (lam - tau) ** 2 * ((tau + 2 * delta) * lam + delta * tau) / (
    delta ** 2 * tau ** 3 * lam ** 2
)
diff = sp.together(sp.simplify(Q - 1 / lam ** 2 - claimed))


def eval_Q(lv, tv, dv):
    Av = (tv + 2 * dv) / (dv ** 2 * tv ** 3)
    return (3 * tv - 2 * lv) / tv ** 3 + Av * (lv - tv) ** 2


def main():
    hits = []
    print(f"Q - 1/lam^2 - claimed = {diff}")
    if diff != 0:
        hits.append(f"factorization residual {diff}")
    # points in range lambda>=delta
    pts = [
        (F(1), F(1), F(1)),
        (F(2), F(1), F(1)),
        (F(1, 2), F(3), F(1, 4)),
        (F(10), F(1, 5), F(1, 10)),
        (F(1), F(10), F(1)),
    ]
    for lv, tv, dv in pts:
        if lv < dv:
            continue
        q = eval_Q(lv, tv, dv)
        inv = 1 / lv ** 2
        gap = q - inv
        print(f"lam={lv} tau={tv} delta={dv} Q-1/lam^2={gap}")
        if gap < 0:
            hits.append(f"negative at lam={lv} tau={tv} delta={dv} gap={gap}")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8080): " + "; ".join(hits[:3]))
    else:
        print(
            "SUMMARY: QUANTIFIER SCOPE on Q_tau(lambda)-lambda^{-2}>=0 for lambda>=delta "
            "(PR #8080): the displayed factorization is an identity and the difference "
            "is nonnegative at the tested interior points; the forall holds as written"
        )


if __name__ == "__main__":
    main()
