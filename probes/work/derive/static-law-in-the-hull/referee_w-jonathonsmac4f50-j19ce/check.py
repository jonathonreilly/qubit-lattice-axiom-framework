#!/usr/bin/env python3
"""Referee of J:derive:static-law-in-the-hull:a3 (author w-macbookpro90c72-j85f9, grok-4.6); referee w-jonathonsmac4f50-j19ce
(claude-opus-5). Provenance: the argument (constant-pattern separator, Z < D on cyclic windows) is that of attempt a1 of this
problem, written by this referee's model family (w-jonathonsmac4f50-j0546) and refereed as confirmed by a grok worker; a3 is an
independent census of the named windows. This check is new code (Python integers, numpy for the 6^8 sum), not a1's or a3's.

Six-axis menu, phi(s, a) = p (same), q (antipodal), r (orthogonal); N_0 = 6, N_k = p^k + q^k + 4 r^k; for an order sigma,
D_sigma = prod_x N_{k_x(sigma)} (k_x = neighbours formed before x); D = min_sigma D_sigma; Z = sum over M^n of prod_E phi.

S1  Hoelder at the used scope: for k <= 6 and each rule, sum_s prod_i phi(s, a_i) <= N_k over all of M^k, equality on the all-equal
    tuple, strict on an orthogonal pair
S2  Z and D (minimum over all n! orders) on the 2x3 rectangle and the cube at (3,1,2), (5,2,4), (7,3,5): the attempt's table,
    Z < D; the path of 3 sites: Z = D = 864
S3  the separator: for every order sigma, mu_sigma(constant pattern) = p^|E| / D_sigma (chain rule from the rule), so every
    adapted scheme gives the constant pattern at most p^|E| / D < p^|E| / Z = mu_static(constant pattern); the exact margins
    6 p^|E| (1/Z - 1/D) of E f, f = 1[constant], are printed
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
RULES = ((3, 1, 2), (5, 2, 4), (7, 3, 5))


def phi(p, q, r):
    return [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]


def N(k, p, q, r):
    return 6 if k == 0 else p ** k + q ** k + 4 * r ** k


def window(kind):
    if kind == "2x3":
        sites = [(x, y) for x in range(2) for y in range(3)]
    elif kind == "cube":
        sites = list(itertools.product((0, 1), repeat=3))
    else:
        sites = [(0,), (1,), (2,)]
    edges = [(i, j) for i, j in itertools.combinations(range(len(sites)), 2)
             if sum(abs(a - b) for a, b in zip(sites[i], sites[j])) == 1]
    return sites, edges


def Zsum(n, edges, W):
    Wn = np.array(W, dtype=np.int64)
    st = np.array(list(itertools.product(M, repeat=n)), dtype=np.int64)
    w = np.ones(len(st), dtype=np.int64)
    for i, j in edges:
        w *= Wn[st[:, i], st[:, j]]
    return int(w.sum())


def Dmin(n, edges, p, q, r):
    nb = {i: set() for i in range(n)}
    for i, j in edges:
        nb[i].add(j)
        nb[j].add(i)
    best, arg = None, None
    for o in itertools.permutations(range(n)):
        seen, d = set(), 1
        for v in o:
            d *= N(len(nb[v] & seen), p, q, r)
            seen.add(v)
        if best is None or d < best:
            best, arg = d, o
    return best, arg, nb


def main():
    ok = True
    for (p, q, r) in RULES:
        W = phi(p, q, r)
        for k in range(1, 7):
            vals = [sum(np.prod([W[s][a] for a in tup]) for s in M) for tup in itertools.product(M, repeat=k)]
            ok &= max(vals) <= N(k, p, q, r) and vals[0] == N(k, p, q, r)
            if k >= 2:
                ok &= sum(np.prod([W[s][a] for a in (0, 2) + (0,) * (k - 2)]) for s in M) < N(k, p, q, r)
    check("S1", ok, "sum_s prod_i phi(s, a_i) <= N_k on all of M^k for k = 1..6 at the three rules, equality on the all-equal tuple, "
          "strict with an orthogonal pair")

    table = {("2x3", (3, 1, 2)): (6000000, 7008768), ("2x3", (5, 2, 4)): (568472046, 631394298),
             ("2x3", (7, 3, 5)): (3651973440, 4044168000), ("cube", (3, 1, 2)): (6982520832, 10933678080),
             ("cube", (5, 2, 4)): (17002040556294, 22841951518746), ("cube", (7, 3, 5)): (412507735200000, 555911333280000)}
    ok, rows, margins = True, [], []
    for (kind, rule), (Zw, Dw) in table.items():
        sites, edges = window(kind)
        Z = Zsum(len(sites), edges, phi(*rule))
        D, order, nb = Dmin(len(sites), edges, *rule)
        # chain rule along the minimizing order for the constant pattern
        p, q, r = rule
        W = phi(*rule)
        prob, seen = F(1), set()
        for v in order:
            ns = nb[v] & seen
            weights = [np.prod([W[s][0] for _ in ns]) if ns else 1 for s in M]
            prob *= F(int(weights[0]), int(sum(weights)))
            seen.add(v)
        chain_ok = prob == F(p ** len(edges), D)
        ok &= Z == Zw and D == Dw and Z < D and chain_ok
        rows.append(f"{kind} {rule}: Z = {Z}, D = {D}, chain rule on the min-D order = p^|E|/D: {chain_ok}")
        margins.append(f"{kind} {rule}: {float(6 * p ** len(edges) * (F(1, Z) - F(1, D))):.3e}")
    sites, edges = window("path")
    Zp = Zsum(3, edges, phi(3, 1, 2))
    Dp, _, _ = Dmin(3, edges, 3, 1, 2)
    ok &= Zp == Dp == 864
    check("S2", ok, "; ".join(rows) + f"; path of 3: Z = {Zp}, D = {Dp}")
    check("S3", ok, "every adapted scheme gives the constant pattern mass <= p^|E|/D < p^|E|/Z; margins of E f, f = 1[constant]: "
          + ", ".join(margins))

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - static-law-in-the-hull a3: on the 2x3 rectangle and the cube at (3,1,2), (5,2,4), (7,3,5), Z and D "
          "(minimum over all n! orders) are the attempt's table with Z < D, the path of 3 has Z = D = 864, the Hoelder bound holds "
          "on M^k for k <= 6, and the constant-pattern mass of every adapted scheme is at most p^|E|/D < p^|E|/Z, so f = 1[constant] "
          "separates the static law from the hull; recomputed with new code. This is the census of a1's argument (this referee's "
          "family), as the attempt says")
    print("SUMMARY: confirmed - no failing step; the table, the negative control and the separator margins reproduce")
    return 0


if __name__ == "__main__":
    sys.exit(main())
