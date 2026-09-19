#!/usr/bin/env python3
"""Referee of J:derive:lightcone-sixaxis-order:a2 (author w-macbookpro90c72-j848f, grok-4.6); referee w-jonathonsmac4f50-j6136
(claude-opus-5). Independent code (exact integers and Fractions); nothing from the author's check.py. Disclosure: this referee's model
family refereed attempt a3 of this problem (grok) and found the sublattice factorization of the neighbour-only synchronous law in the
re-recording a2 referee (referee_w-jonathonsmac4f50-j50b9).

Six-axis weights W = p (same), q (antipodal), r (orthogonal) on the ring C4. The task's light-cone rule forms the record at x from x and
x +- 1 (the site included): pi ~ prod_x Z(s_{x-1}, s_x, s_{x+1}). The attempt's C4 law omits the site: pi ~ prod_x Z(s_{x-1}, s_{x+1}).

S1  step 2 holds: the neighbour-only synchronous kernel on C4 is symmetric on all 1296^2 pairs (reversible without the site)
S2  step 1's numbers are those of the self-less law: one orthogonal defect 144/169, one antipodal 121/169 at (3,1,2), decreasing at p = 5, 10
S3  under that law the two sublattices of C4 are independent: the staggered configuration (a, b, a, b) has exactly the weight of (a, a, a, a)
    for b orthogonal or antipodal, and 36 configurations share the maximal weight, so single-flip costs below 1 do not single out six
    aligned laws
S4  under the task's light-cone law (site included) exactly the 6 aligned configurations are maximal, and the one-defect ratios are
    (13/15)^3 = 2197/3375 (orthogonal) and (11/15)^3 = 1331/3375 (antipodal) at (3,1,2), the staggered one (13/15)^4
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


def weights(p, q, r):
    return [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]


def laws(p, q, r):
    W = weights(p, q, r)
    Z2 = lambda a, b: sum(W[v][a] * W[v][b] for v in M)
    Z3 = lambda a, b, c: sum(W[v][a] * W[v][b] * W[v][c] for v in M)
    confs = list(itertools.product(M, repeat=4))
    selfless = {c: Z2(c[3], c[1]) * Z2(c[0], c[2]) * Z2(c[1], c[3]) * Z2(c[2], c[0]) for c in confs}
    withself = {c: Z3(c[3], c[0], c[1]) * Z3(c[0], c[1], c[2]) * Z3(c[1], c[2], c[3]) * Z3(c[2], c[3], c[0]) for c in confs}
    return confs, selfless, withself


def main():
    W = np.array(weights(3, 1, 2), dtype=np.int64)
    C = np.array(list(itertools.product(M, repeat=4)), dtype=np.int64)
    K = np.ones((len(C), len(C)), dtype=np.int64)
    for x in range(4):
        for y in ((x - 1) % 4, (x + 1) % 4):
            K *= W[C[:, x][None, :], C[:, y][:, None]]
    check("S1", bool((K == K.T).all()), "neighbour-only synchronous kernel on C4 symmetric on all 1296^2 pairs")

    rows, ok, prev = [], True, None
    for p in (3, 5, 10):
        confs, sl, ws = laws(p, 1, 2)
        a = (0, 0, 0, 0)
        orth, anti = F(sl[(2, 0, 0, 0)], sl[a]), F(sl[(1, 0, 0, 0)], sl[a])
        if p == 3:
            ok &= (orth, anti) == (F(144, 169), F(121, 169))
        if prev:
            ok &= orth < prev[0] and anti < prev[1]
        prev = (orth, anti)
        rows.append(f"p = {p}: orth {orth}, anti {anti}")
    check("S2", ok, "self-less C4 one-defect ratios " + "; ".join(rows))

    confs, sl, ws = laws(3, 1, 2)
    a = (0, 0, 0, 0)
    mx = max(sl.values())
    nmax = sum(1 for c in confs if sl[c] == mx)
    stag = (sl[(0, 2, 0, 2)] == sl[a], sl[(0, 1, 0, 1)] == sl[a])
    fact = all(sl[c] == (sum(weights(3, 1, 2)[v][c[1]] * weights(3, 1, 2)[v][c[3]] for v in M) ** 2)
               * (sum(weights(3, 1, 2)[v][c[0]] * weights(3, 1, 2)[v][c[2]] for v in M) ** 2) for c in confs)
    check("S3", nmax == 36 and all(stag) and fact, f"self-less law = Z(s1,s3)^2 Z(s0,s2)^2 (independent sublattices): {fact}; staggered "
          f"(a,b,a,b) weight equals the aligned weight for b orthogonal / antipodal: {stag}; {nmax} configurations share the maximal weight")

    mxw = max(ws.values())
    nmaxw = sum(1 for c in confs if ws[c] == mxw)
    aligned = all(ws[(v, v, v, v)] == mxw for v in M)
    o, an, st = F(ws[(2, 0, 0, 0)], ws[a]), F(ws[(1, 0, 0, 0)], ws[a]), F(ws[(0, 2, 0, 2)], ws[a])
    ok = nmaxw == 6 and aligned and o == F(13, 15) ** 3 and an == F(11, 15) ** 3 and st == F(13, 15) ** 4
    check("S4", ok, f"light-cone law (site included): {nmaxw} maximal configurations, the aligned ones: {aligned}; one orthogonal defect {o}, "
          f"one antipodal {an}, staggered {st}")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 1 - the C4 ratios 144/169 and 121/169 are those of the law without the site, pi ~ prod Z(s_{x-1}, s_{x+1}), "
          "not of the task's light-cone rule (record at x from x and x +- e_j), whose C4 ratios are (13/15)^3 and (11/15)^3; and under the "
          "self-less law the two sublattices are independent (the staggered configuration weighs exactly as much as the aligned one, 36 "
          "maximal configurations on C4), so the single-flip costs do not point to six aligned laws. Step 2 (reversibility without the "
          "site) holds; the attempt states correctly that no Peierls bound on Z^3 is proved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
