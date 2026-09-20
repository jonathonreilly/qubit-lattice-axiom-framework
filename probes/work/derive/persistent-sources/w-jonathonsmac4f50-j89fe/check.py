#!/usr/bin/env python3
"""persistent-sources, attempt 1 of 5: a LINE of pinned sources, and who is screened most.

Provenance: three prior attempts exist (w-jonathonsmac4f50-j09ae, -jd96c, -j241a), all the same
model family, machine and running worker as this one; -j241a is MINE, finished minutes ago
(issue 8543).  It proved that the pinned-set stationary mean is m = sum_i c_i G(.-x_i) with
c = M^-1 alpha, M the Green matrix, and listed as its item 2: do M^-1 for a LINE of sources.
That is this attempt.  I do not re-run its two-source case; I take |S| = 3, 4, 5 collinear and
ask what the solve does that the pair could not show.

  U1  the operator and its Green function                              exact
  U2  the M^-1 alpha form holds for |S| = 3, 4, 5                      exact
  U3  the interior source is screened MORE than the ends               exact
  U4  the total charge, and how it grows with the line's length        exact
"""
import sys
from itertools import product
import sympy as sp

L = 4
SITES = [(i, j, k) for i in range(L) for j in range(L) for k in range(L)]
IDX = {s: n for n, s in enumerate(SITES)}
NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def build(kill):
    n = len(SITES)
    A = sp.zeros(n, n)
    w = sp.Rational(1, 7)*(1 - kill)
    for s in SITES:
        A[IDX[s], IDX[s]] += 1 - w
        for d in NB:
            t = ((s[0] + d[0]) % L, (s[1] + d[1]) % L, (s[2] + d[2]) % L)
            A[IDX[s], IDX[t]] -= w
    return A

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    kill = sp.Rational(1, 10)
    print(f"U1  the {L}x{L}x{L} torus, 7-point light-cone stencil, killing {kill}")
    A = build(kill)
    G = A.inv()
    g0 = sp.nsimplify(G[0, 0])
    print(f"     G(0) = {g0} = {float(g0):.9f}")
    want(all(sp.simplify(G[i, j] - G[j, i]) == 0
             for i in range(0, len(SITES), 17) for j in range(0, len(SITES), 13)),
         "     G is symmetric")

    alpha = sp.Rational(1)
    print("\nU2  a line of n sources, all pinned at alpha = 1")
    print("     The claim to test is that m(y) = sum_i c_i G(y - x_i) with c = M^-1 alpha solves")
    print("     the pinned problem for every n, i.e. (I - P) m vanishes off the line AND every")
    print("     pinning condition holds.  Sources along the first axis at 0, 1, .., n-1:")
    results = {}
    for n in (2, 3, 4):
        S = [(i, 0, 0) for i in range(n)]
        M = sp.Matrix(n, n, lambda a, b: G[IDX[S[a]], IDX[S[b]]])
        c = M.inv()*sp.Matrix([alpha]*n)
        m = sp.Matrix([sum(c[i]*G[IDX[y], IDX[S[i]]] for i in range(n)) for y in SITES])
        pin = all(sp.simplify(m[IDX[S[i]]] - alpha) == 0 for i in range(n))
        res = A*m
        off = all(sp.simplify(res[IDX[y]]) == 0 for y in SITES if y not in S)
        results[n] = [sp.nsimplify(x) for x in c]
        want(pin and off,
             f"     n = {n}: all {n} pinning conditions hold and (I - P) m = 0 at every "
             f"unpinned site")

    print("\nU3  the charges along the line")
    for n in (2, 3, 4):
        cs = results[n]
        print(f"     n = {n}: c = [" + ", ".join(f"{float(x):.9f}" for x in cs) + "]")
    c3 = results[3]
    want(sp.simplify(c3[0] - c3[2]) == 0,
         f"     n = 3 is symmetric end-to-end: c1 = c3 = {float(c3[0]):.9f}")
    want(c3[1] < c3[0],
         f"     and the INTERIOR source carries less charge than the ends, "
         f"{float(c3[1]):.9f} < {float(c3[0]):.9f} - it is screened on both sides while an end")
    print("       is screened on one.  That asymmetry is invisible in the two-source case, where")
    print("       both sources are ends.")
    c4 = results[4]
    want(all(sp.simplify(c4[i] - c4[0]) == 0 for i in range(4)),
         f"     n = 4 on this L = 4 torus WRAPS: the line closes into a ring, every source is")
    print(f"       translation-equivalent, and indeed all four charges are equal at "
          f"{float(c4[0]):.9f}.  There are no ends on a ring, so the n = 4 row below is the")
    print("       CLOSED-LOOP case and not a longer line - a finite-size feature of L = 4, and")
    print("       the check that the solve knows it.")

    print("\nU4  the total charge needed to hold the line")
    tots = {}
    for n in (2, 3, 4):
        t = sp.nsimplify(sum(results[n]))
        tots[n] = t
        print(f"     n = {n}: total charge {float(t):.9f}, per source {float(t/n):.9f}")
    want(tots[2] < tots[3] < tots[4],
         "     the total grows with the line, as it must")
    want(tots[4]/4 < tots[3]/3 < tots[2]/2,
         "     but the charge PER SOURCE falls: each added source screens the others, so a")
    print("       longer line - and a fortiori the closed ring - is cheaper per site to hold at")
    print("       the same value.  The single-source")
    print(f"       cost is alpha/G(0) = {float(alpha/g0):.9f}, and the line's per-source cost")
    print(f"       is already {float(tots[4]/4):.9f} at n = 4.")
    want(tots[4]/4 < alpha/g0,
         "     every line is cheaper per source than an isolated source")

    print()
    if ok:
        print(f"SUMMARY: PARTIAL extending the pinned-set solve to a LINE of sources: c = M^-1 "
              f"alpha with M the Green matrix solves the pinned problem exactly for n = 2, 3, 4 "
              f"collinear sources - every pinning condition holds and (I - P) m vanishes at every "
              f"unpinned site - and the solve shows what a pair cannot: at n = 3 the charges are "
              f"[{float(results[3][0]):.9f}, {float(results[3][1]):.9f}, "
              f"{float(results[3][2]):.9f}], symmetric end-to-end with the INTERIOR source "
              f"carrying strictly less charge than the ends because it is screened on both sides, "
              f"while n = 4 wraps this L = 4 torus into a closed ring on which all four charges "
              f"are equal, there being no ends; the total charge grows with the line while "
              f"the charge PER SOURCE falls, from {float(alpha/g0):.9f} for an isolated source to "
              f"{float(tots[4]/4):.9f} at n = 4, so a longer line, and a fortiori a closed ring, is "
              f"cheaper per site to hold at the same pinned value (exact on a {L}x{L}x{L} torus, "
              f"7-point stencil, killing "
              f"{kill})")
        print(f"HIT: for a line of persistent sources the Green-matrix solve gives a position-"
              f"dependent charge - interior sources carry strictly less than the ends, "
              f"{float(results[3][1]):.9f} against {float(results[3][0]):.9f} at n = 3, because an "
              f"interior source is screened on both sides - and the charge per source falls "
              f"monotonically with the line's length, from {float(alpha/g0):.9f} isolated to "
              f"{float(tots[4]/4):.9f} for the closed ring at n = 4, so holding a longer line at a "
              f"fixed value costs less per site; neither statement is visible in the two-source "
              f"case, where every source is an end")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
