#!/usr/bin/env python3
"""persistent-sources, attempt 3 of 5: two pinned sources do not superpose.

Provenance: two prior attempts exist (w-jonathonsmac4f50-j09ae, -jd96c), both the same model
family, machine and running worker as this one.  I re-run neither.  Both leave (a) - the
two-source linear problem - and go after the nonlinear coefficient instead.  This attempt does
(a) exactly.

Everything below is computed in exact rational arithmetic on a finite torus with a small killing
rate, which makes G = (I - P)^-1 exist without appealing to transience; the structural statements
do not depend on the killing.

  T1  the light-cone stencil, and its Green function                    exact
  T2  one pinned source: the mean is alpha G(y-x)/G(0)                  exact
  T3  two pinned sources: c = M^-1 alpha with M the 2x2 Green matrix    exact
  T4  superposition FAILS, and the exact screening factor               exact
  T5  the equal-charge case, and what it says about the interaction
"""
import sys
from fractions import Fraction as F
from itertools import product
import sympy as sp

L = 4                                   # 4x4x4 torus
SITES = [(i, j, k) for i in range(L) for j in range(L) for k in range(L)]
IDX = {s: n for n, s in enumerate(SITES)}
NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def build(kill):
    """I - P for the 7-point light-cone stencil (self + 6 neighbours, weight 1/7 each),
    damped by (1 - kill) so that the inverse exists on the torus."""
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
    print(f"T1  the stencil and its Green function on a {L}x{L}x{L} torus, killing {kill}")
    print("     The light-cone formation map averages a site and its six neighbours with weight")
    print("     1/7 each; that is the P whose symbol gives the unit's static response 7/E(k),")
    print("     since 1 - P(k) = (6 - 2 sum_a cos k_a)/7 = E(k)/7.")
    A = build(kill)
    G = A.inv()
    g0 = sp.nsimplify(G[0, 0])
    want(all(sp.simplify(G[i, i] - g0) == 0 for i in range(0, len(SITES), 7)),
         f"     G is translation invariant: G(0) = {g0} = {float(g0):.9f} at every site checked")
    want(all(sp.simplify(G[i, j] - G[j, i]) == 0
             for i in range(0, len(SITES), 13) for j in range(0, len(SITES), 11)),
         "     and symmetric, as the detailed-balance of the stencil requires")

    x1, x2 = (0, 0, 0), (2, 0, 0)
    d12 = sp.nsimplify(G[IDX[x1], IDX[x2]])
    print(f"     G(0) = {float(g0):.9f},  G(x1-x2) = {d12} = {float(d12):.9f} for the pair")
    print(f"     x1 = {x1}, x2 = {x2}")

    print("\nT2  one pinned source")
    print("     A source pinned at every level is not a conditioning of the stationary law; the")
    print("     pinned process's stationary mean m solves (I - P) m = c e_x with the single")
    print("     unknown c fixed by m(x) = alpha, so m(y) = alpha G(y - x)/G(0).  Checked:")
    alpha = sp.Rational(3, 2)
    c1 = alpha/g0
    m1 = sp.Matrix([c1*G[IDX[y], IDX[x1]] for y in SITES])
    want(sp.simplify(m1[IDX[x1]] - alpha) == 0,
         f"     the solution takes the pinned value: m(x1) = {sp.nsimplify(m1[IDX[x1]])} = alpha")
    res = A*m1
    want(all(sp.simplify(res[IDX[y]]) == 0 for y in SITES if y != x1),
         "     and (I - P) m vanishes at every unpinned site, so m is the stationary mean")

    print("\nT3  two pinned sources")
    print("     With two pinned sites the ansatz is m(y) = c1 G(y-x1) + c2 G(y-x2), and the two")
    print("     pinning conditions give the 2x2 system M c = alpha with M = [[G(0), G(d)],")
    print("     [G(d), G(0)]].  So c = M^-1 alpha, NOT c_i = alpha_i/G(0).")
    M = sp.Matrix([[g0, d12], [d12, g0]])
    a1, a2 = sp.Rational(3, 2), sp.Rational(1, 2)
    cc = M.inv()*sp.Matrix([a1, a2])
    m2 = sp.Matrix([cc[0]*G[IDX[y], IDX[x1]] + cc[1]*G[IDX[y], IDX[x2]] for y in SITES])
    want(sp.simplify(m2[IDX[x1]] - a1) == 0 and sp.simplify(m2[IDX[x2]] - a2) == 0,
         f"     both pinning conditions hold exactly: m(x1) = {a1}, m(x2) = {a2}")
    res2 = A*m2
    want(all(sp.simplify(res2[IDX[y]]) == 0 for y in SITES if y not in (x1, x2)),
         "     and (I - P) m vanishes off the two pinned sites")

    print("\nT4  superposition fails, exactly")
    print("     The naive superposition of the two single-source solutions is")
    print("       m_naive(y) = a1 G(y-x1)/G(0) + a2 G(y-x2)/G(0),")
    print("     which pins nothing: it overshoots at each source by the other's tail.")
    mn = sp.Matrix([a1*G[IDX[y], IDX[x1]]/g0 + a2*G[IDX[y], IDX[x2]]/g0 for y in SITES])
    over1 = sp.nsimplify(mn[IDX[x1]] - a1)
    want(sp.simplify(over1 - a2*d12/g0) == 0 and over1 != 0,
         f"     m_naive(x1) - a1 = a2 G(d)/G(0) = {over1} = {float(over1):.9f} /= 0")
    ratio = sp.nsimplify(cc[0]/(a1/g0))
    want(sp.simplify(ratio - 1) != 0,
         f"     and the true charge is reduced: c1 / (a1/G(0)) = {float(ratio):.9f} /= 1")
    print("     The exact statement is c = M^-1 alpha with M the Green matrix of the pinned set,")
    print("     so the single-source formula alpha G/G(0) is the one-source case of a linear")
    print("     solve whose size is the number of sources; it does not superpose.")

    print("\nT5  equal charges, and the interaction")
    ce = M.inv()*sp.Matrix([alpha, alpha])
    want(sp.simplify(ce[0] - alpha/(g0 + d12)) == 0 and sp.simplify(ce[0] - ce[1]) == 0,
         f"     for equal charges c1 = c2 = alpha/(G(0) + G(d)) exactly")
    scr = sp.nsimplify(g0/(g0 + d12))
    want(sp.simplify(ce[0] - (alpha/g0)*scr) == 0,
         f"     i.e. each charge is SCREENED by the factor G(0)/(G(0)+G(d)) = "
         f"{float(scr):.9f} < 1")
    print("     - two like sources each need LESS charge to hold their pinned value, because")
    print("     each sits in the other's field.  With opposite charges the same algebra gives")
    co = M.inv()*sp.Matrix([alpha, -alpha])
    anti = sp.nsimplify(g0/(g0 - d12))
    want(sp.simplify(co[0] - (alpha/g0)*anti) == 0 and anti > 1,
         f"     the factor G(0)/(G(0)-G(d)) = {float(anti):.9f} > 1: opposite sources need MORE.")
    print("     Both factors are exact and depend on the separation only through G(d), so the")
    print("     whole two-source interaction of the linear pinned process is carried by the")
    print("     single number G(d)/G(0).")

    print()
    if ok:
        print(f"SUMMARY: PARTIAL for (a), the linear light-cone process with sites pinned at every "
              f"level: the stationary mean with a pinned set S is m(y) = sum_i c_i G(y - x_i) with "
              f"c = M^-1 alpha and M_ij = G(x_i - x_j) the Green matrix of S, so the refereed "
              f"one-source formula alpha G(y-x)/G(0) is the |S| = 1 case of a linear solve and does "
              f"NOT superpose; verified exactly on a {L}x{L}x{L} torus with the 7-point stencil "
              f"(1 - P(k) = E(k)/7) and killing {kill}, where G(0) = {float(g0):.9f} and "
              f"G(d) = {float(d12):.9f} at separation 2: the naive superposition overshoots the "
              f"first pinning condition by exactly a2 G(d)/G(0) = {float(over1):.9f}, for equal "
              f"charges the true coefficient is alpha/(G(0)+G(d)), a screening factor "
              f"G(0)/(G(0)+G(d)) = {float(scr):.9f} < 1, and for opposite charges it is "
              f"G(0)/(G(0)-G(d)) = {float(anti):.9f} > 1")
        print(f"HIT: for the linear light-cone process the two-source pinned problem is an exact "
              f"2x2 solve in the Green matrix - c = M^-1 alpha with M = [[G(0), G(d)],[G(d), "
              f"G(0)]] - so like sources are screened by G(0)/(G(0)+G(d)) < 1 and opposite "
              f"sources anti-screened by G(0)/(G(0)-G(d)) > 1, the entire interaction being "
              f"carried by the single ratio G(d)/G(0); the refereed single-source formula "
              f"alpha G(y-x)/G(0) therefore does not superpose, and the naive sum overshoots each "
              f"pinning condition by the other charge's tail, exactly a2 G(d)/G(0)")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
