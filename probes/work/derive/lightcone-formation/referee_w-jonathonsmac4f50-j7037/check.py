#!/usr/bin/env python3
"""Referee of J:derive:lightcone-formation:a1 (author w-macbookpro90c72-j5bbf, grok-4.6); referee w-jonathonsmac4f50-j7037
(claude-opus-5). Independent code (exact Fractions and integers); nothing from the author's check.py. Disclosure: this referee's
model family refereed attempts a2, a5 and a6 of this problem (all grok).

L1  (a) the synchronous product-kernel chain on a 3-site ring with the symmetric stencil {x, x +- 1}, six-axis weights (3,1,2): the
    kernel K(s, s') = prod_x prod_{n in N(x)} W(s'_x, s_n) is symmetric on all 216^2 pairs, so the chain is reversible w.r.t.
    pi ~ prod_x Z_x(s), Z_x = sum_v prod_n W(v, s_n); pi differs from the static nearest-neighbour law (TV printed)
L2  (c) C = 7 sigma^2/(2E(1 - E/14)) lies in [7 sigma^2/(2E), 49 sigma^2/(2E)] for 0 < E <= 12 (1 - E/14 in [1/7, 1)); on the L = 4
    torus the values are 49/24, 49/40, 49/48 at E = 2, 4, 6, 8, 10, 12 as stated
L3  (d) the seven-predecessor six-axis kernel at (3,1,2): the largest one-slot total variation over all 6^6 environments and all flips is
    c = 270/989 (an antipodal flip), so 7c = 1890/989 > 1 and the naive Dobrushin bound does not give uniqueness there
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
Wl = [[3 if a == b else (1 if b == (a ^ 1) else 2) for b in M] for a in M]


def main():
    n = 3
    nb = {x: [x, (x + 1) % n, (x - 1) % n] for x in range(n)}
    confs = list(itertools.product(M, repeat=n))
    Wn = np.array(Wl, dtype=np.int64)
    C = np.array(confs, dtype=np.int64)
    K = np.ones((len(confs), len(confs)), dtype=np.int64)
    for x in range(n):
        for y in nb[x]:
            K *= Wn[C[:, x][None, :], C[:, y][:, None]]
    sym = bool((K == K.T).all())
    Zx = np.ones(len(confs), dtype=np.int64)
    for x in range(n):
        t = np.ones((len(confs), 6), dtype=np.int64)
        for y in nb[x]:
            t *= Wn[:, C[:, y]].T
        Zx *= t.sum(1)
    rows = bool((K.sum(1) == Zx).all())
    pi = [F(int(z), int(Zx.sum())) for z in Zx]
    ws = [Wl[c[0]][c[1]] * Wl[c[1]][c[2]] * Wl[c[2]][c[0]] for c in confs]
    mu = [F(w, sum(ws)) for w in ws]
    tv = sum(abs(a - b) for a, b in zip(pi, mu)) / 2
    check("L1", sym and rows and tv > 0, f"3-ring, stencil {{x, x+-1}}: K symmetric on 216^2 pairs ({sym}), rows sum to prod Z_x ({rows}); "
          f"TV(pi, static nearest-neighbour law) = {tv} = {float(tv):.4f}")

    vals = {E: F(7, 2 * E) / (1 - F(E, 14)) for E in range(1, 13)}
    env = all(F(7, 2 * E) <= v <= F(49, 2 * E) for E, v in vals.items())
    l4 = {E: vals[E] for E in (2, 4, 6, 8, 10, 12)}
    ok = env and l4 == {2: F(49, 24), 4: F(49, 40), 6: F(49, 48), 8: F(49, 48), 10: F(49, 40), 12: F(49, 24)}
    check("L2", ok, f"envelope holds for E = 1..12; L = 4 values {l4}")

    rest = np.array(list(itertools.product(M, repeat=6)), dtype=np.int64)
    w = np.ones((len(rest), 6), dtype=np.int64)
    for j in range(6):
        w *= Wn[:, rest[:, j]].T
    best, arg = F(0), None
    for a2 in (1, 2):
        na, nb2 = Wn[:, 0][None, :] * w, Wn[:, a2][None, :] * w
        Za, Zb = na.sum(1), nb2.sum(1)
        num = np.abs(na * Zb[:, None] - nb2 * Za[:, None]).sum(1)
        for i in range(len(rest)):
            v = F(int(num[i]), 2 * int(Za[i]) * int(Zb[i]))
            if v > best:
                best, arg = v, ("antipodal" if a2 == 1 else "orthogonal", tuple(int(t) for t in rest[i]))
    check("L3", best == F(270, 989) and 7 * best == F(1890, 989) and arg[0] == "antipodal",
          f"c = {best} = {float(best):.6f} ({arg[0]} flip, environment {arg[1]}); 7c = {7 * best} = {float(7 * best):.4f} > 1")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - lightcone-formation a1: the symmetric-stencil synchronous chain is reversible w.r.t. pi ~ prod Z_x (kernel symmetry "
          "on every pair of a 3-ring instance), pi is not the static nearest-neighbour law, the linear kernel obeys 7 sigma^2/(2E) <= C <= "
          "49 sigma^2/(2E) with the L = 4 values 49/24, 49/40, 49/48, and the seven-predecessor six-axis one-slot constant at (3,1,2) is "
          "c = 270/989 exactly (antipodal flip), 7c = 1890/989 > 1; recomputed independently. The attempt correctly leaves RP/LRO for pi open")
    print("SUMMARY: confirmed - no failing step in the modest claims (a), (c), (d)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
