#!/usr/bin/env python3
"""Referee of J:derive:re-recording:a3 (author w-macbookpro90c72-j3a06, grok-4.6); referee w-jonathonsmac4f50-j4469
(claude-opus-5). Independent code (exact Fractions); nothing from the author's check.py. Disclosure: this referee's model family
refereed attempts a1 and a2 of this problem (both grok).

Two sites, one bond, six-axis weights W = p (same), q (antipodal), r (orthogonal), (p, q, r) = (3, 1, 2); rule
K(v | a) = W(v, a) / Z(a), Z(a) = sum_v W(v, a).

T1  asynchronous heat-bath (each site with probability 1/2): rows sum to 1, mu P = mu, detailed balance on all 36^2 pairs for
    mu(s0, s1) = W(s0, s1)/72; P^2 > 0 entrywise, so mu is the unique stationary law
T2  synchronous P((s0,s1) -> (s0',s1')) = K(s0'|s1) K(s1'|s0): rows sum to 1, pi P = pi, detailed balance for pi ~ Z(s0) Z(s1);
    P > 0, so pi is unique
T3  TV(mu, pi) = 1/12; both one-site marginals are 1/6
T4  beyond the attempt: Z(a) = p + q + 4r for every a (the menu's cube symmetry), so pi is exactly the uniform product law on 36
    states at every (p, q, r) > 0 - the synchronous law carries no bond correlation at all; TV(mu, pi) = (1/144) sum |W - 2| is the
    general form at (3,1,2), and the same holds at (5,2,4), (1,3,2) with their own values
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


M = range(6)


def run(p, q, r):
    W = [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]
    Z = [sum(W[v][a] for v in M) for a in M]
    K = [[F(W[v][a], Z[a]) for v in M] for a in M]          # K[a][v] = K(v | a)
    S = list(itertools.product(M, repeat=2))
    tot = sum(W[a][b] for a, b in S)
    mu = {s: F(W[s[0]][s[1]], tot) for s in S}
    Zpi = sum(Z[a] * Z[b] for a, b in S)
    pi = {s: F(Z[s[0]] * Z[s[1]], Zpi) for s in S}
    Pas = {(s, t): F(0) for s in S for t in S}
    for s in S:
        for v in M:
            Pas[(s, (v, s[1]))] += F(1, 2) * K[s[1]][v]
            Pas[(s, (s[0], v))] += F(1, 2) * K[s[0]][v]
    Psy = {(s, t): K[s[1]][t[0]] * K[s[0]][t[1]] for s in S for t in S}
    return W, Z, S, mu, pi, Pas, Psy


def main():
    W, Z, S, mu, pi, Pas, Psy = run(3, 1, 2)
    rows = all(sum(Pas[(s, t)] for t in S) == 1 for s in S)
    stat = all(sum(mu[s] * Pas[(s, t)] for s in S) == mu[t] for t in S)
    db = all(mu[s] * Pas[(s, t)] == mu[t] * Pas[(t, s)] for s in S for t in S)
    P2pos = all(sum(Pas[(s, m)] * Pas[(m, t)] for m in S) > 0 for s in S for t in S)
    check("T1", rows and stat and db and P2pos, f"async: rows {rows}, mu P = mu {stat}, detailed balance on 1296 pairs {db}, "
          f"P^2 > 0 {P2pos} (mu unique)")
    rows = all(sum(Psy[(s, t)] for t in S) == 1 for s in S)
    stat = all(sum(pi[s] * Psy[(s, t)] for s in S) == pi[t] for t in S)
    db = all(pi[s] * Psy[(s, t)] == pi[t] * Psy[(t, s)] for s in S for t in S)
    pos = all(v > 0 for v in Psy.values())
    check("T2", rows and stat and db and pos, f"sync: rows {rows}, pi P = pi {stat}, detailed balance {db}, P > 0 {pos}")
    tv = sum(abs(mu[s] - pi[s]) for s in S) / 2
    marg = {F(sum(mu[s] for s in S if s[0] == a)) for a in M} | {F(sum(pi[s] for s in S if s[0] == a)) for a in M}
    check("T3", tv == F(1, 12) and marg == {F(1, 6)}, f"TV(mu, pi) = {tv}; one-site marginals {marg}")
    rows4 = []
    ok4 = len(set(Z)) == 1 and all(v == F(1, 36) for v in pi.values())
    for pqr in ((5, 2, 4), (1, 3, 2), (7, 1, 1)):
        W2, Z2, S2, mu2, pi2, _, _ = run(*pqr)
        ok4 &= len(set(Z2)) == 1 and all(v == F(1, 36) for v in pi2.values())
        rows4.append(f"{pqr}: Z = {Z2[0]}, TV(mu, pi) = {sum(abs(mu2[s] - pi2[s]) for s in S2) / 2}")
    check("T4", ok4, f"Z(a) = p + q + 4r for every a, so pi is uniform on the 36 states (no bond correlation) at (3,1,2) (Z = {Z[0]}) "
          "and at " + "; ".join(rows4))

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - re-recording a3 on one bond at (3,1,2): async heat-bath reversible with unique stationary law mu ~ W "
          "(rows, mu P = mu, detailed balance on 1296 pairs, P^2 > 0), synchronous chain reversible with unique pi ~ Z(s0) Z(s1) "
          "(P > 0), TV(mu, pi) = 1/12, uniform one-site marginals; recomputed with independent exact code. Beyond the claim: Z is "
          "constant on the six-axis menu, so pi is the uniform product law - the synchronous law carries no bond correlation")
    print("SUMMARY: confirmed - no failing step; the synchronous one-bond law is uniform, which makes (c)'s non-transfer immediate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
