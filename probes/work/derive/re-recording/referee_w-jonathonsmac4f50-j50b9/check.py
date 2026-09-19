#!/usr/bin/env python3
"""Referee of J:derive:re-recording:a2 (author w-macbookpro90c72-je4a9, grok-4.6); referee w-jonathonsmac4f50-j50b9
(claude-opus-5). Independent code (exact integers and Fractions; numpy integer arrays for the 1296 x 1296 kernels); nothing from
the author's check.py. Disclosure: this referee's model family refereed attempt a1 of this problem (referee_w-jonathonsmac4f50-
jf4b6, a grok attempt).

Setting: the cycle C4 (sites 0..3, neighbours i +- 1), six-axis menu with pair weight W(a, b) = p (same), q (antipodal), r
(orthogonal), (p, q, r) = (3, 1, 2); re-recording rule K(v | s) ~ prod_{n in N(x)} W(v, s_n) over the CURRENT neighbours.

R1  static law mu ~ prod_edges W: Z = tr W^4 = 20784 (W's eigenvalues 12, 2 (x3), 0 (x2)); mu(all +x) = 81/20784 = 27/6928
R2  asynchronous re-recording (one site, any rates): detailed balance with mu for every configuration, site and new value (exact)
R3  synchronous re-recording: the kernel K(s, s') = prod_x prod_{n in N(x)} W(s'_x, s_n) is symmetric on all 1296^2 pairs (so the
    chain is reversible w.r.t. pi ~ prod_x Z_x(s), Z_x(s) = sum_v prod_n W(v, s_n)); rows of P sum to 1; P > 0 entrywise, so pi
    is its unique stationary law; pi(all +x) = 26^4 / 20784^2 = 28561/26998416 != 27/6928
R4  the vector pairing sum_x s'_x.S_x(s) = sum_x s_x.S_x(s') on C4 on a grid of pairs (the exponential-rule form of R3's symmetry)
R5  beyond the attempt: on a bipartite window the neighbour-only synchronous law factorizes, pi(s) = f(s_even) g(s_odd): on C4
    the two sublattices are independent under pi, so pi(s_0 = s_1 = +x) = 1/36 exactly (no nearest-neighbour correlation) while
    mu(s_0 = s_1 = +x) = 73/1732 > 1/36; the all-+x mass is the square of the pair mass 676/20784
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


M = range(6)                                   # 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z
p, q, r = 3, 1, 2
W = [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]
N4 = 4
nbr = {i: ((i - 1) % N4, (i + 1) % N4) for i in range(N4)}
confs = list(itertools.product(M, repeat=N4))


def main():
    # R1
    Zs = sum(W[c[0]][c[1]] * W[c[1]][c[2]] * W[c[2]][c[3]] * W[c[3]][c[0]] for c in confs)
    Wn = np.array(W, dtype=np.int64)
    tr4 = int(np.trace(np.linalg.matrix_power(Wn, 4)))
    mu_all = F(p ** 4, Zs)
    ev = sorted(int(round(e)) + 0 for e in np.linalg.eigvalsh(Wn.astype(float)))
    check("R1", Zs == tr4 == 20784 and mu_all == F(27, 6928),
          f"static Z = {Zs} = tr W^4 (eigenvalues {ev}); mu(all +x) = {mu_all}")

    # R2
    def mu_w(c):
        return W[c[0]][c[1]] * W[c[1]][c[2]] * W[c[2]][c[3]] * W[c[3]][c[0]]
    ok = True
    for c in confs:
        for x in range(N4):
            a, b = nbr[x]
            Zx = sum(W[v][c[a]] * W[v][c[b]] for v in M)
            for v in M:
                c2 = list(c)
                c2[x] = v
                c2 = tuple(c2)
                lhs = F(mu_w(c)) * F(W[v][c[a]] * W[v][c[b]], Zx)
                rhs = F(mu_w(c2)) * F(W[c[x]][c[a]] * W[c[x]][c[b]], Zx)
                ok &= lhs == rhs
    check("R2", ok, "asynchronous heat-bath re-recording: mu(s) P_x(s -> s^{x,v}) = mu(s^{x,v}) P_x(s^{x,v} -> s) for all 1296 "
          "configurations, 4 sites, 6 values (exact), so the static law is its stationary law at any clock rates")

    # R3
    C = np.array(confs)
    Wa = np.array(W, dtype=np.int64)
    K = np.ones((len(confs), len(confs)), dtype=np.int64)
    for x in range(N4):
        a, b = nbr[x]
        K *= Wa[C[:, x][None, :], C[:, a][:, None]] * Wa[C[:, x][None, :], C[:, b][:, None]]
    sym = bool((K == K.T).all())
    Zx = np.ones(len(confs), dtype=np.int64)
    for x in range(N4):
        a, b = nbr[x]
        Zx *= (Wa[:, C[:, a]] * Wa[:, C[:, b]]).sum(axis=0)
    rows = bool((K.sum(axis=1) == Zx).all())
    pos = bool((K > 0).all())
    pi_w = Zx
    Zpi = int(pi_w.sum())
    iall = confs.index((0, 0, 0, 0))
    pi_all = F(int(pi_w[iall]), Zpi)
    check("R3", sym and rows and pos and pi_all == F(28561, 26998416) and pi_all != mu_all,
          f"synchronous kernel K(s, s') symmetric on all 1296^2 pairs: {sym}; row sums = prod_x Z_x(s): {rows}; P > 0: {pos}; "
          f"pi normalizer {Zpi} = 20784^2: {Zpi == 20784 ** 2}; pi(all +x) = {pi_all} != {mu_all}")

    # R4
    vec = {0: (1, 0, 0), 1: (-1, 0, 0), 2: (0, 1, 0), 3: (0, -1, 0), 4: (0, 0, 1), 5: (0, 0, -1)}

    def S(c, x):
        a, b = nbr[x]
        return tuple(vec[c[a]][k] + vec[c[b]][k] for k in range(3))
    ok, npairs = True, 0
    for i in range(0, len(confs), 7):
        for j in range(0, len(confs), 11):
            c, c2 = confs[i], confs[j]
            lhs = sum(sum(vec[c2[x]][k] * S(c, x)[k] for k in range(3)) for x in range(N4))
            rhs = sum(sum(vec[c[x]][k] * S(c2, x)[k] for k in range(3)) for x in range(N4))
            ok &= lhs == rhs
            npairs += 1
    check("R4", ok, f"vector pairing sum_x s'_x.S_x(s) = sum_x s_x.S_x(s') on C4 (every 7th x every 11th configuration, {npairs} pairs)")

    # R5
    pair = [[sum(W[v][a] * W[v][b] for v in M) for b in M] for a in M]          # Z(a, b) = (W^2)(a, b)
    ok = True
    for c in confs:
        ok &= int(pi_w[confs.index(c)]) == (pair[c[1]][c[3]] ** 2) * (pair[c[0]][c[2]] ** 2)
    pi01 = F(sum(int(pi_w[i]) for i, c in enumerate(confs) if c[0] == 0 and c[1] == 0), Zpi)
    mu01 = F(sum(mu_w(c) for c in confs if c[0] == 0 and c[1] == 0), Zs)
    pair_mass = F(pair[0][0] ** 2, sum(pair[a][b] ** 2 for a in M for b in M))
    ok &= pi01 == F(1, 36) and mu01 > F(1, 36) and pi_all == pair_mass ** 2
    check("R5", ok, f"pi(s) = Z(s1,s3)^2 Z(s0,s2)^2 for every configuration: the sublattices {{0,2}} and {{1,3}} are independent "
          f"under pi; pi(s0 = s1 = +x) = {pi01}, mu(s0 = s1 = +x) = {mu01} = {float(mu01):.5f} > 1/36; pi(all +x) = "
          f"({pair_mass})^2")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - re-recording a2 on C4 at (3,1,2): static mu(all +x) = 27/6928 (Z = tr W^4 = 20784) and the synchronous "
          "law pi(all +x) = 28561/26998416 (exact 6^4 sums), distinct; the synchronous kernel's pairing symmetry holds on all "
          "1296^2 pairs (reversible, P > 0, pi its unique stationary law) and asynchronous re-recording satisfies detailed balance "
          "with mu exactly; recomputed with independent code. Beyond the claim: on this bipartite window pi factorizes over the "
          "two sublattices (pi(s0 = s1 = +x) = 1/36, no nearest-neighbour correlation, against 73/1732 for mu)")
    print("SUMMARY: confirmed - the C4 masses, the synchronous pairing and the async/static identity survive; the synchronous law "
          "is a product over sublattices on bipartite windows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
