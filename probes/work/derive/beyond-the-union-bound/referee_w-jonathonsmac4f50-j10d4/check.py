#!/usr/bin/env python3
"""Referee of J:derive:beyond-the-union-bound:a4 (author w-macbookpro90c72-j5968, grok-4.6); referee w-jonathonsmac4f50-j10d4
(claude-opus-5). Independent code (exact Fractions, integer power series, brute-force tree enumeration); nothing from the author's
check.py. Disclosure: this referee's model family wrote attempt a1-series work on this problem (w-jonathonsmac4f50-jae8a, the
refinement-history count, p >= 84 on (p,1,2)), a different route; a4 does not build on it.

Block 30's typed tree: a U-node has three up-slots (directions 1, 2, 3); U = (1 + xU)^3 at y = 0. Diamond: a node with up-children in
directions i and j whose i-child has an up-j child and whose j-child has an up-i child (both reach v + e_i + e_j).

X1  allowed occupancy pairs 48 of 64 and triples 216 of 512 (own diamond test)
X2  step 3's system (a1 = xU, a2 = x^2(U^2 - P^2), a3 = x^3 sum_allowed A_s A_t A_r) as integer power series reproduces the brute-force
    counts of diamond-free direction-labelled trees for n = 1..7 nodes (1, 3, 12, 55, 270, ...), and every tree whose lattice embedding
    is injective is diamond-free (injective counts <= diamond-free counts <= all counts)
X3  step 4: (a1, a2, a3) = (12/25, 1/5, 2/25) is a super-solution at x = 3/20 > 4/27 (U = 78/25, margins 3/250, 107/62500,
    508933/125000000); D = 72 >= (1 + xU)^2(1 + 3x 72) (margin 6937/312500); R = (1 + xU)^3(1 + 216 x) = 8254954121/78125000
X4  step 5: max_t t^2(3/20 - t) = 1/2000 at t = 1/10; on (p,1,2) eps2(4003) > 1/2000 > eps2(4004) = 729/1458185; t + eps2/t^2 < 3/20;
    eps1 R = 24764862363/455910455234375000 < 1e-7
X5  step 6: on S = {0, -e1, -e2, -e1-e2}, w(S) = eps1 eps2^2 = 1587/3696187 > (eps1 eps2)^2 = 4761/933119209 at p = 14
X6  the ASSUMED y > 0 extension: at p = 4004, t = 1/10, y = eps1/t^3; D = 72 has relative margin 3.08e-4, below the factor
    (1 + yF)^6 - 1 >= 6 y R = 3.27e-4 that multiplies D's right side, so D = 72 alone does not carry over; D = 80 with F = 120 does
    (checked as a super-solution of D <- (1+xU)^2(1+3xD)(1+yF)^6, F <- (1+xU)^3(1+3xD)(1+yF)^5 with the thinned U-system's right sides
    multiplied by (1 + yF)^6)
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


def diamond_pair(s, t, i, j):
    """child in direction i has occupancy set s, child in direction j has set t: diamond iff j in s and i in t"""
    return (j in s) and (i in t)


SUBSETS = [frozenset(c) for k in range(4) for c in itertools.combinations((1, 2, 3), k)]


def allowed_pair(s, t):
    return not diamond_pair(s, t, 1, 2)


def allowed_triple(s, t, r):
    return not (diamond_pair(s, t, 1, 2) or diamond_pair(s, r, 1, 3) or diamond_pair(t, r, 2, 3))


def trees(n):
    """direction-labelled trees with n nodes: tuple (c1, c2, c3), each None or a subtree"""
    if n == 1:
        return [(None, None, None)]
    out = []
    for split in itertools.product(range(n), repeat=3):
        if sum(split) != n - 1:
            continue
        opts = [[None] if k == 0 else trees(k) for k in split]
        for combo in itertools.product(*opts):
            out.append(tuple(combo))
    return out


def has_diamond(t):
    kids = {d + 1: t[d] for d in range(3) if t[d] is not None}
    for i, j in itertools.combinations(sorted(kids), 2):
        ci, cj = kids[i], kids[j]
        if ci[j - 1] is not None and cj[i - 1] is not None:
            return True
    return any(has_diamond(c) for c in kids.values())


def sites(t, pos=(0, 0, 0)):
    out = [pos]
    for d in range(3):
        if t[d] is not None:
            q = list(pos)
            q[d] += 1
            out += sites(t[d], tuple(q))
    return out


def series_mul(a, b, N):
    out = [0] * N
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:N - i]):
                out[i + j] += x * y
    return out


def main():
    pairs = sum(1 for s in SUBSETS for t in SUBSETS if allowed_pair(s, t))
    triples = sum(1 for s in SUBSETS for t in SUBSETS for r in SUBSETS if allowed_triple(s, t, r))
    check("X1", pairs == 48 and triples == 216, f"allowed pairs {pairs}/64, triples {triples}/512")

    N = 7
    counts = {}
    for n in range(1, N + 1):
        ts = trees(n)
        df = sum(1 for t in ts if not has_diamond(t))
        inj = sum(1 for t in ts if len(set(sites(t))) == n)
        injdf = all(not has_diamond(t) for t in ts if len(set(sites(t))) == n)
        counts[n] = (len(ts), df, inj, injdf)
    # power series in x (index = number of edges); A_S depends on |S| by symmetry: a0 = 1, a1, a2, a3
    one = [1] + [0] * (N - 1)
    a1 = a2 = a3 = [0] * N
    for _ in range(N + 1):
        U = [one[k] + 3 * a1[k] + 3 * a2[k] + a3[k] for k in range(N)]
        P = [a1[k] + 2 * a2[k] + a3[k] for k in range(N)]
        A = {0: one, 1: a1, 2: a2, 3: a3}
        n1 = [0] + U[:N - 1]
        UU, PP = series_mul(U, U, N), series_mul(P, P, N)
        n2 = [0, 0] + [UU[k] - PP[k] for k in range(N - 2)]
        phi = [0] * N
        for s in SUBSETS:
            for t in SUBSETS:
                for r in SUBSETS:
                    if allowed_triple(s, t, r):
                        term = series_mul(series_mul(A[len(s)], A[len(t)], N), A[len(r)], N)
                        phi = [phi[k] + term[k] for k in range(N)]
        n3 = [0, 0, 0] + phi[:N - 3]
        a1, a2, a3 = n1, n2, n3
    U = [one[k] + 3 * a1[k] + 3 * a2[k] + a3[k] for k in range(N)]
    ok = all(U[n - 1] == counts[n][1] for n in range(1, N + 1)) and all(c[2] <= c[1] <= c[0] and c[3] for c in counts.values())
    check("X2", ok, "series U = " + str(U) + " = diamond-free counts " + str([counts[n][1] for n in range(1, N + 1)]) + "; all "
          + str([counts[n][0] for n in range(1, N + 1)]) + ", injective " + str([counts[n][2] for n in range(1, N + 1)])
          + "; every injective tree is diamond-free")

    x = F(3, 20)
    b1, b2, b3 = F(12, 25), F(1, 5), F(2, 25)

    def rhs(b1, b2, b3, fac=F(1)):
        U = 1 + 3 * b1 + 3 * b2 + b3
        P = b1 + 2 * b2 + b3
        A = {0: F(1), 1: b1, 2: b2, 3: b3}
        phi = sum((A[len(s)] * A[len(t)] * A[len(r)] for s in SUBSETS for t in SUBSETS for r in SUBSETS if allowed_triple(s, t, r)), F(0))
        return U, fac * x * U, fac * x * x * (U * U - P * P), fac * x ** 3 * phi
    U, r1, r2, r3 = rhs(b1, b2, b3)
    Dbar = F(72)
    Drhs = (1 + x * U) ** 2 * (1 + 3 * x * Dbar)
    Rbar = (1 + x * U) ** 3 * (1 + 3 * x * Dbar)
    ok = (U == F(78, 25) and b1 - r1 == F(3, 250) and b2 - r2 == F(107, 62500) and b3 - r3 == F(508933, 125000000) and x > F(4, 27)
          and Dbar - Drhs == F(6937, 312500) and Rbar == F(8254954121, 78125000))
    check("X3", ok, f"U = {U}; margins {b1 - r1}, {b2 - r2}, {b3 - r3}; D margin {Dbar - Drhs}; R = {Rbar} = {float(Rbar):.6f}")

    def d1(p):
        return F(33, p ** 3 + 33)

    def d2(p):
        return F(p + 32, p * (p + 1) + 32)

    def d3(p):
        return F(2 * p + 11, p * p + 2 * p + 11)
    e2 = lambda p: max(d2(p), d3(p))
    t = F(1, 10)
    tt = [F(k, 1000) for k in range(1, 150)]
    mx = max(s * s * (x - s) for s in tt)
    ok = (mx == F(1, 2000) and t * t * (x - t) == F(1, 2000) and e2(4003) > F(1, 2000) > e2(4004) and e2(4004) == F(729, 1458185)
          and t + e2(4004) / t ** 2 < x and d1(4004) * Rbar == F(24764862363, 455910455234375000) and d1(4004) * Rbar < F(1, 10 ** 7))
    check("X4", ok, f"max t^2(3/20 - t) on a 1/1000 grid = {mx} at t = 1/10; eps2(4003) = {e2(4003)}, eps2(4004) = {e2(4004)}; "
          f"t + eps2/t^2 = {t + e2(4004) / t ** 2}; eps1 R = {float(d1(4004) * Rbar):.4e}")

    p = 14
    e1, e2p = d1(p), e2(p)
    wS, prod = e1 * e2p ** 2, (e1 * e2p) ** 2
    check("X5", wS == F(1587, 3696187) and prod == F(4761, 933119209) and wS > prod, f"w(S) = {wS} > product {prod}")

    y = d1(4004) / t ** 3
    xs = t + e2(4004) / t ** 2
    rel_margin = (Dbar - Drhs) / Dbar
    need = 6 * y * Rbar
    D2, F2 = F(80), F(120)
    fac6, fac5 = (1 + y * F2) ** 6, (1 + y * F2) ** 5
    U2, s1, s2, s3 = rhs(b1, b2, b3, fac6)
    xsave = x
    ok_super = (b1 >= s1 and b2 >= s2 and b3 >= s3 and D2 >= (1 + xsave * U2) ** 2 * (1 + 3 * xsave * D2) * fac6
                and F2 >= (1 + xsave * U2) ** 3 * (1 + 3 * xsave * D2) * fac5)
    check("X6", rel_margin < need and ok_super, f"at p = 4004, t = 1/10, y = {float(y):.3e}: D = 72 relative margin {float(rel_margin):.3e} < "
          f"6 y R = {float(need):.3e}; (a1, a2, a3) = (12/25, 1/5, 2/25), D = 80, F = 120 is a super-solution at x = 3/20 with the "
          f"(1 + yF)^6 and (1 + yF)^5 factors: {ok_super}")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - beyond-the-union-bound a4: the diamond-free lift is valid (every injective lattice tree is diamond-free) and its "
          "U-system (48 allowed pairs, 216 allowed triples) reproduces the brute-force diamond-free tree counts for n <= 7; (12/25, 1/5, 2/25) "
          "is an exact super-solution at x = 3/20 > 4/27 with U = 78/25, D = 72, R = 8254954121/78125000; the ceiling becomes eps2 < 1/2000, "
          "first met on (p,1,2) at p = 4004 (eps2 = 729/1458185); the overlapping-cone product fails on the diamond animal (1587/3696187 > "
          "4761/933119209 at p = 14). Correction to the ASSUMED y > 0 step: D = 72's relative margin 3.1e-4 is below 6yR = 3.3e-4 at "
          "p = 4004, so the stated certificate does not carry over as is; D = 80, F = 120 with the same (a1, a2, a3) does")
    print("SUMMARY: confirmed - the y = 0 domain statement, the ceiling arithmetic and the set-count no-go survive; the y > 0 step needs a "
          "larger D than stated (D = 80 works)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
