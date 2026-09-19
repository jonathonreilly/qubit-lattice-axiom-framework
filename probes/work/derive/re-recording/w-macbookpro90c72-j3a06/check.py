#!/usr/bin/env python3
"""J:derive:re-recording:a3 (worker w-macbookpro90c72-j3a06).

Different route from a4 (algebraic pairing + TV on C4/T2x2) and a1 (Gamma_6
spectrum): build the exact 36-state transition matrices of async and sync
re-recording on the two-site edge, over Q, and check stationarity.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

FAILS: list[str] = []
OKS: list[str] = []
M = range(6)


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def Wmat(p, q, r):
    W = [[None] * 6 for _ in M]
    for a, b in itertools.product(M, repeat=2):
        if a == b:
            W[a][b] = p
        elif a == (b ^ 1):
            W[a][b] = q
        else:
            W[a][b] = r
    return W


def K(W, s, neigh):
    """K(s | single neighbour)."""
    z = sum(W[a][neigh] for a in M)
    return W[s][neigh] / z


def Z(W, neigh):
    return sum(W[a][neigh] for a in M)


def main():
    W = Wmat(F(3), F(1), F(2))
    states = list(itertools.product(M, repeat=2))
    N = len(states)
    check("E0.N36", N == 36)
    idx = {s: i for i, s in enumerate(states)}

    # static: mu ∝ W(s0,s1)
    mu = [W[s0][s1] for s0, s1 in states]
    Zst = sum(mu)
    mu = [m / Zst for m in mu]

    # async generator-style kernel: pick site 0 or 1 with equal rate 1/2, redraw
    P_as = [[F(0)] * N for _ in range(N)]
    for s in states:
        i = idx[s]
        s0, s1 = s
        for a in M:
            j = idx[(a, s1)]
            P_as[i][j] += F(1, 2) * K(W, a, s1)
        for b in M:
            j = idx[(s0, b)]
            P_as[i][j] += F(1, 2) * K(W, b, s0)
    # rows sum to 1
    ok_row = all(sum(P_as[i]) == 1 for i in range(N))
    check("E1.async-stochastic", ok_row)
    # mu P = mu
    muP = [sum(mu[i] * P_as[i][j] for i in range(N)) for j in range(N)]
    check("E1.async-stationarity", muP == mu)
    # detailed balance
    ok_db = True
    for i, j in itertools.product(range(N), repeat=2):
        if mu[i] * P_as[i][j] != mu[j] * P_as[j][i]:
            ok_db = False
    check("E1.async-DB", ok_db)

    # sync: P(s→s') = K(s0'|s1) K(s1'|s0)
    P_sy = [[F(0)] * N for _ in range(N)]
    for s in states:
        i = idx[s]
        s0, s1 = s
        for s0p, s1p in states:
            P_sy[i][idx[(s0p, s1p)]] = K(W, s0p, s1) * K(W, s1p, s0)
    check("E2.sync-stochastic", all(sum(P_sy[i]) == 1 for i in range(N)))
    # pi ∝ Z(s1) Z(s0)
    pi = [Z(W, s1) * Z(W, s0) for s0, s1 in states]
    Zpi = sum(pi)
    pi = [x / Zpi for x in pi]
    piP = [sum(pi[i] * P_sy[i][j] for i in range(N)) for j in range(N)]
    check("E2.sync-stationarity", piP == pi)
    ok_db2 = True
    for i, j in itertools.product(range(N), repeat=2):
        if pi[i] * P_sy[i][j] != pi[j] * P_sy[j][i]:
            ok_db2 = False
    check("E2.sync-DB", ok_db2)
    # distinct laws
    tv = sum(abs(mu[i] - pi[i]) for i in range(N)) / 2
    check("E3.TV-positive", tv > 0, f"TV={tv}")
    print("E3.TV(static,sync)=", tv, float(tv))
    # transfer: uniqueness of static transfers to async (same mu); not to sync
    check("E4.mu-neq-pi", mu != pi)
    # one-site marginal of both: by symmetry uniform? 2-site edge, static
    # P(s0=a) = sum_b W(a,b) / Zst
    marg_st = [F(0)] * 6
    marg_sy = [F(0)] * 6
    for (s0, s1), i in idx.items():
        marg_st[s0] += mu[i]
        marg_sy[s0] += pi[i]
    check("E5.static-marginal-uniform", all(marg_st[a] == F(1, 6) for a in M), f"{marg_st[0]}")
    check("E5.sync-marginal-uniform", all(marg_sy[a] == F(1, 6) for a in M), f"{marg_sy[0]}")

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        f"HIT: PARTIAL: on the two-site edge, exact 36x36 matrices over Q: async "
        f"heat-bath is reversible w.r.t. the static law (DB and mu P=mu); sync is "
        f"reversible w.r.t. pi∝Z(s0)Z(s1) (DB and pi P=pi); TV(static,sync)={tv}≠0; "
        f"one-site marginals are both uniform. Uniqueness/kernel of the static law "
        f"transfer to async, not to sync. Route: transition matrices, not pairing-only."
    )
    print(
        f"SUMMARY: PARTIAL exact 36-state proof that async re-recording has the static "
        f"law and sync has pi∝prod Z, with TV={tv} on the edge; transfer only for async"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
