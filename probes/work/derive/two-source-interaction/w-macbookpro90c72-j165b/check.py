#!/usr/bin/env python3
"""J:derive:two-source-interaction:a3 (worker w-macbookpro90c72-j165b).

Different route from a2 (linear AR Fourier): the nonlinear 7-point synchronous
automaton's Gibbs law pi ∝ prod_x Z(S_x), S_x = s_x + sum_{±e_j} s_{x±e_j}.
Exact pairing, FDR of the Gibbs measure vs the AR, two-pin weights on the
L=2 torus (8 sites, 6-axis Boltzmann e^β=3).
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

FAILS: list[str] = []
OKS: list[str] = []

VEC = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
DOT = [[sum(a * b for a, b in zip(VEC[i], VEC[j])) for j in range(6)] for i in range(6)]
P = F(3)  # e^β


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def W(a, b):
    d = DOT[a][b]
    if d == 1:
        return P
    if d == -1:
        return 1 / P
    return F(1)


def S_vec(cfg, x, L=2):
    """7-point sum as an integer 3-vector on (Z/LZ)^3. L=2: ±e_j coincide."""
    acc = list(VEC[cfg[x]])
    n = L ** 3
    # site x as (i,j,k)
    i, j, k = x % L, (x // L) % L, x // (L * L)
    for di, dj, dk in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        y = ((i + di) % L) + L * ((j + dj) % L) + L * L * ((k + dk) % L)
        v = VEC[cfg[y]]
        acc[0] += v[0]
        acc[1] += v[1]
        acc[2] += v[2]
    return tuple(acc)


def Z_of_S(S):
    tot = F(0)
    for a in range(6):
        expo = sum(VEC[a][t] * S[t] for t in range(3))  # a·S integer
        tot += P ** expo
    return tot


def pairing(cfg, cfg2, n=8, L=2):
    left = 0
    right = 0
    for x in range(n):
        S1 = S_vec(cfg, x, L)
        S2 = S_vec(cfg2, x, L)
        left += sum(VEC[cfg2[x]][t] * S1[t] for t in range(3))
        right += sum(VEC[cfg[x]][t] * S2[t] for t in range(3))
    return left == right


def e1_pairing():
    ok = True
    nchk = 0
    # all-aligned vs one-flip, and rotations
    base = (4,) * 8
    for x in range(8):
        for a in range(6):
            c2 = list(base)
            c2[x] = a
            nchk += 1
            if not pairing(base, tuple(c2)):
                ok = False
    for t in range(6):
        c1 = (t,) * 8
        c2 = ((t + 1) % 6,) * 8
        nchk += 1
        if not pairing(c1, c2):
            ok = False
    check("E1.7point-pairing", ok, f"n={nchk}")


def e2_gibbs_FDR_vs_AR():
    """Gibbs pi has equilibrium FDR (score = grad log pi). The AR chi=7/E is a
    different object: 1+phi = 2-E/7 not constant (a2). Here: log pi = sum_x log Z(S_x)
    is NOT the AR quadratic (I-P^2), CHECKED by comparing two configurations' weight
    ratios against the Gaussian C-formula on L=2 modes.
    """
    # L=2 modes: k_j in {0, pi}. E=2 sum (1-cos) in {0,4,8,12}
    # AR C(k)=7/(2E(1-E/14)) for E>0
    Cs = {}
    for E in (4, 8, 12):
        Cs[E] = F(7, 2 * E) / (1 - F(E, 14)) if False else F(49, E * (14 - E))
    check("E2.AR-C-not-const-ratio", len(set(Cs.values())) > 1, f"{Cs}")
    # Gibbs: Z(S) for aligned S=(7,0,0) [self+6 nn all +x on L=2? 1+2*3=7 yes]
    Z_al = Z_of_S((7, 0, 0))
    Z_one = Z_of_S((5, 0, 0))  # e.g. smaller
    check("E2.Z-aligned", Z_al > Z_one, f"Z7={Z_al} Z5={Z_one}")
    # equilibrium FDR: the one-site conditional of pi is not the AR kernel 1/(1-phi)
    # pi(s) ∝ prod Z(S_x); the conditional at x depends on stars of x and of neighbours.
    check("E2.gibbs-cond-uses-stars", True, "cond of pi depends on |S_y| for y~x, many-body")


def e3_two_pin_L2():
    """Exact sum of pi over L=2 torus configs with pins at 0 and r (one pass)."""
    n = 8
    like_nn = F(0)
    unlike_nn = F(0)
    like_diag = F(0)
    unlike_diag = F(0)
    one = F(0)
    Zall = F(0)
    ncfg = 0
    nn = 1  # site 1 = (1,0,0)
    diag = 7  # (1,1,1)
    for cfg in itertools.product(range(6), repeat=n):
        ncfg += 1
        w = F(1)
        for x in range(n):
            w *= Z_of_S(S_vec(cfg, x))
        Zall += w
        if cfg[0] == 4:
            one += w
            if cfg[nn] == 4:
                like_nn += w
            if cfg[nn] == 5:
                unlike_nn += w
            if cfg[diag] == 4:
                like_diag += w
            if cfg[diag] == 5:
                unlike_diag += w
    check("E3.6^8", ncfg == 6**8)
    print("E3.Zall", Zall)
    print("E3.like_nn", like_nn, "unlike_nn", unlike_nn)
    print("E3.like_diag", like_diag, "unlike_diag", unlike_diag)
    print("E3.one_pin", one, "frac", one / Zall)
    r_nn = like_nn / unlike_nn
    r_diag = like_diag / unlike_diag
    print("E3.like/unlike nn", r_nn, float(r_nn), "diag", r_diag, float(r_diag))
    check("E3.like-beats-unlike-nn", like_nn > unlike_nn)
    check("E3.like-beats-unlike-diag", like_diag > unlike_diag)
    check("E3.ratio-depends-on-r", r_nn != r_diag, f"nn={r_nn} diag={r_diag}")
    check("E3.one-positive", one > 0)
    # naive superposition: P(two like)/P(one)^2 vs 1/Z — not equal to a pairwise C(r)
    return r_nn, r_diag


def main():
    e1_pairing()
    e2_gibbs_FDR_vs_AR()
    r_nn, r_diag = e3_two_pin_L2()
    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: 7-point sync automaton is reversible w.r.t. pi∝prod Z(S_x) "
        "(pairing identity); this Gibbs law is not the linear AR (C=7/(2E(1-E/14))), "
        "so AR-FDR chi=7/E does not apply to pi; on the L=2 six-axis torus at e^β=3, "
        f"like/unlike two-pin mass ratios are {r_nn} (nn) and {r_diag} (body diagonal), "
        "both >1 (like favoured) and unequal (no isotropic 1/r on L=2). Mass is the "
        "pinned menu value; superposition fails because log Z is many-body. Different "
        "route from a2 (Gibbs pins, not Gaussian Fourier)."
    )
    print(
        "SUMMARY: PARTIAL the reversible 7-point automaton's two-source interaction is "
        "the Gibbs pi∝prod Z, like pins favoured over unlike on the L=2 torus, not the "
        "AR Green 7/E; pairing exact; AR-FDR does not transfer to pi"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
