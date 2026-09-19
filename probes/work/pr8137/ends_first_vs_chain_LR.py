#!/usr/bin/env python3
"""J:attack-b:PR8137 — SAME TEST, BOTH SIDES on Theorem 1 orders.

Ends-first (L,R,M) vs chain (L,M,R): identical test = the (L,R) joint.
Independent kernel: both orders give mu_0 x mu_0. Varying two-state Haar-square
kernel: ends-first is independent, chain is K^2 != mu_0.
HIT if the two orders have the same (L,R) law for a varying kernel, or different
laws for the independent kernel.
"""
from __future__ import annotations

from fractions import Fraction as F

PLUS, MINUS = "+", "-"
STATES = (PLUS, MINUS)
MU0 = {PLUS: F(1, 2), MINUS: F(1, 2)}


def k_indep(s, t):
    return F(1, 2)


def k_var(s, t):
    # symmetric, varies: P(same)=2/3
    return F(2, 3) if s == t else F(1, 3)


def joint_LR(K, order):
    """Exact P(L,R) on the 3-path L—M—R under a sequential order."""
    out = {(a, b): F(0) for a in STATES for b in STATES}
    for L in STATES:
        for M in STATES:
            for R in STATES:
                if order == "ends":
                    # L, R then M: L~mu0, R~mu0, M~K(.|L)*K(.|R) normalized
                    wL, wR = MU0[L], MU0[R]
                    num = K(M, L) * K(M, R)
                    den = sum(K(s, L) * K(s, R) for s in STATES)
                    w = wL * wR * (num / den)
                else:
                    # chain L, M, R: L~mu0, M~K(.|L), R~K(.|M)
                    w = MU0[L] * K(M, L) * K(R, M)
                out[(L, R)] += w
    return out


def tv(p, q):
    return sum(abs(p[k] - q[k]) for k in p) / 2


def main():
    hits = []
    for name, K in (("indep", k_indep), ("var", k_var)):
        pe, pc = joint_LR(K, "ends"), joint_LR(K, "chain")
        d = tv(pe, pc)
        print(f"{name}: TV(ends, chain)={d}")
        print(f"  ends {pe}")
        print(f"  chain {pc}")
        if name == "indep" and d != 0:
            hits.append(f"independent kernel order-dependent TV={d}")
        if name == "var" and d == 0:
            hits.append("varying kernel (L,R) identical on both orders")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: SAME TEST BOTH SIDES (PR #8137): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: SAME TEST BOTH SIDES on (L,R) under ends-first vs chain "
            "(PR #8137): independent kernel TV=0; varying two-state kernel TV>0; "
            "the order-dependence separation holds as written"
        )


if __name__ == "__main__":
    main()
