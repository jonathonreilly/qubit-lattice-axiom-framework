#!/usr/bin/env python3
"""Referee of J:derive:static-law-in-the-hull:a2 (author w-macbookpro90c72-j67ba, grok-4.6); referee w-jonathonsmac4f50-ja284
(claude-opus-5). Provenance: the constant-pattern separator on every cyclic window is attempt a1's (this referee's model family,
w-jonathonsmac4f50-j0546; confirmed by a grok referee); a2 applies it on C4. New code here (Python integers, brute force).

C4 = the plaquette, six-axis weights; N_0 = 6, N_k = p^k + q^k + 4r^k; D_sigma = prod_x N_{k_x(sigma)}.

P1  Z(C4) = sum over the 6^4 patterns of prod_edges phi = tr W^4 (W's eigenvalues p+q+4r, p-q (x3), p+q-2r (x2)): 20784, 280086,
    810768 at (3,1,2), (5,2,4), (7,3,5)
P2  over all 24 orders D_min = 6 N_1^2 N_2 = 22464, 295182, 853200 (attained by the orders going round the cycle), so Z < D_min with
    margins 1680, 15096, 42432; the all-+x mass p^4/D_sigma of every order (chain rule from the rule) is below p^4/Z
P3  path of 3 sites: Z = D = 864 (control)
P4  scope: C4 is the plaquette, the window the task calls already settled; the task's named windows (2x3, cube) are not treated by a2
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import numpy as np

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


M = range(6)


def phi(p, q, r):
    return [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]


def N(k, p, q, r):
    return 6 if k == 0 else p ** k + q ** k + 4 * r ** k


def main():
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    nb = {i: {j for e in edges for j in e if i in e and j != i} for i in range(4)}
    want = {(3, 1, 2): (20784, 22464, 1680), (5, 2, 4): (280086, 295182, 15096), (7, 3, 5): (810768, 853200, 42432)}
    ok1 = ok2 = True
    rows = []
    for rule, (Zw, Dw, mw) in want.items():
        p, q, r = rule
        W = phi(*rule)
        Z = sum(W[a][b] * W[b][c] * W[c][d] * W[d][a] for a, b, c, d in itertools.product(M, repeat=4))
        tr = int(np.trace(np.linalg.matrix_power(np.array(W, dtype=np.int64), 4)))
        ev = (p + q + 4 * r) ** 4 + 3 * (p - q) ** 4 + 2 * (p + q - 2 * r) ** 4
        ok1 &= Z == tr == ev == Zw
        Ds = {}
        for o in itertools.permutations(range(4)):
            seen, d, prob = set(), 1, F(1)
            for v in o:
                k = len(nb[v] & seen)
                d *= N(k, p, q, r)
                prob *= F(p ** k, N(k, p, q, r)) if k else F(1, 6)
                seen.add(v)
            Ds[o] = d
            ok2 &= prob == F(p ** 4, d) and F(p ** 4, d) < F(p ** 4, Z)
        Dmin = min(Ds.values())
        ok2 &= Dmin == Dw == 6 * N(1, p, q, r) ** 2 * N(2, p, q, r) and Dmin - Z == mw
        rows.append(f"{rule}: Z = {Z}, D_min = {Dmin}, margin {Dmin - Z}, orders attaining D_min {sum(1 for v in Ds.values() if v == Dmin)}")
    check("P1", ok1, "Z(C4) = brute force = tr W^4 = eigenvalue sum at the three rules")
    check("P2", ok2, "; ".join(rows) + "; every order's all-+x mass p^4/D_sigma (chain rule) is below p^4/Z")
    W = phi(3, 1, 2)
    Zp = sum(W[a][b] * W[b][c] for a, b, c in itertools.product(M, repeat=3))
    Dp = min(6 * 12 * 12, 6 * 6 * N(2, 3, 1, 2))
    check("P3", Zp == Dp == 864, f"path of 3: Z = {Zp}, D = {Dp}")
    print("INFO P4: C4 is the plaquette; the task names the 2x3 rectangle and the cube as the open windows (treated in a1 and a3)")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - static-law-in-the-hull a2 on C4: Z = tr W^4 = 20784, 280086, 810768 and D_min = 6 N_1^2 N_2 = 22464, "
          "295182, 853200 over all 24 orders at (3,1,2), (5,2,4), (7,3,5), margins 1680, 15096, 42432, so every adapted scheme's "
          "all-+x mass is at most p^4/D_min < p^4/Z; path of 3: Z = D = 864; recomputed with new code. Scope: C4 is the plaquette, "
          "a special case of a1's cyclic-window separator (this referee's family), not the task's named windows")
    print("SUMMARY: confirmed - no failing step on C4; the result is the plaquette case of a1's separator")
    return 0


if __name__ == "__main__":
    sys.exit(main())
