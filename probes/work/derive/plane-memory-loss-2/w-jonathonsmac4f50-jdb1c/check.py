#!/usr/bin/env python3
"""plane-memory-loss-2, attempt 3 of 4: the task's GIVEN (2) is false, and Route A's cost is
bounded below by an explicit constant - proved, not extrapolated.

Provenance: the two prior attempts (a1 w-jonathonsmac4f50-jd237, a4 w-jonathonsmac4f50-j5926)
are by the same model family, machine and running worker as this one.  I do not re-run either
route.  a4 closes Route A by EXTRAPOLATING the cone's conductance from eight exact values; a1
exhibits a Polya-urn unit flow with energies bounded by 2T/(T+1).  The task's GIVEN (2) asserts
the opposite conclusion - that the minimum space-time twist cost is exactly 1/sum_{k<T}P_k and
tends to 0.  Both cannot hold.  This attempt settles it in closed form.

  C1  the Polya-urn flow: uniform marginals on each level                exact
  C2  it is a unit flow: conservation at every site                      exact
  C3  its level energy is exactly 1/((m+1)(m+3))                         proved symbolically
  C4  hence E_T = 3/4 - (1/2)(1/(T+1) + 1/(T+2)) < 3/4 for every T       telescoped
  C5  Thomson: min energy = conductance >= 4/3, uniformly in T           vs a4's exact values
  C6  where 1/sum P_k comes from, and why it proves nothing
"""
import sys
from fractions import Fraction as F
import sympy as sp

def comps(m):
    """the sites at level m: triples of non-negative integers summing to m"""
    return [(a, b, m - a - b) for a in range(m + 1) for b in range(m + 1 - a)]

def N(m):
    return (m + 1)*(m + 2)//2

def polya_level(m):
    """the Polya-urn unit flow's edge flows out of level m, as a dict site -> (f_1,f_2,f_3)"""
    return {n: tuple(F(1, N(m))*F(n[j] + 1, m + 3) for j in range(3)) for n in comps(m)}

def srw_levels(T):
    """the uniform-splitting (simple-random-walk) flow's site masses, level by level"""
    cur = {(0, 0, 0): F(1)}
    out = [cur]
    for m in range(T):
        nxt = {}
        for n, v in cur.items():
            for j in range(3):
                t = tuple(n[k] + (1 if k == j else 0) for k in range(3))
                nxt[t] = nxt.get(t, F(0)) + v/3
        cur = nxt
        out.append(cur)
    return out

def cone_conductance(T):
    """exact minimum Dirichlet energy on the backward cone, theta = 1 at the apex, 0 on level 0.

    The cone's edges join level m to level m+1 only, so the network is layered and the interior
    levels can be eliminated one at a time.  Elimination of a layer with conductance matrix S to
    the next layer is exact rational Gaussian elimination; the result is the effective
    conductance between apex and base."""
    # potentials: level 0 = base (theta 0) ... level T = apex (single site, theta 1)
    # eliminate from the base upward.  Represent the reduced network seen from level m as a
    # symmetric matrix A_m over that level's sites (Laplacian of the eliminated part) plus the
    # direct unit conductances to level m+1.
    sites = [comps(T - m) for m in range(T + 1)]        # level m has |n| = T - m
    # start at level 0 (base, |n| = T): all grounded, so the Schur complement seen by level 1 is
    # just the diagonal of the number of edges down to the base.
    idx = {s: i for i, s in enumerate(sites[0])}
    A = None
    for m in range(1, T + 1):
        here = sites[m]
        hidx = {s: i for i, s in enumerate(here)}
        below = sites[m - 1]
        bidx = {s: i for i, s in enumerate(below)}
        n_h, n_b = len(here), len(below)
        # edges: site n at level m (|n| = T-m) joins n + e_j at level m-1 (|n| = T-m+1)
        Bm = [[F(0)]*n_b for _ in range(n_h)]
        for s in here:
            for j in range(3):
                t = tuple(s[k] + (1 if k == j else 0) for k in range(3))
                Bm[hidx[s]][bidx[t]] += F(1)
        deg = [sum(Bm[i]) for i in range(n_h)]
        if A is None:                                   # level 0 is grounded
            A = sp.Matrix(n_h, n_h, lambda i, j: deg[i] if i == j else F(0))
        else:
            # A is the conductance matrix (Laplacian of the eliminated part) on `below`
            Bmat = sp.Matrix(n_h, n_b, lambda i, j: sp.Rational(Bm[i][j]))
            Ddiag = sp.Matrix(n_b, n_b, lambda i, j: sum(Bm[k][i] for k in range(n_h))
                              if i == j else 0)
            M = A + Ddiag
            S = Bmat*M.inv()*Bmat.T
            Dh = sp.Matrix(n_h, n_h, lambda i, j: sp.Rational(deg[i]) if i == j else 0)
            A = Dh - S
    return sp.nsimplify(A[0, 0])

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    m = sp.Symbol('m', nonnegative=True, integer=True)

    print("C1  the Polya-urn flow has uniform marginals on every level")
    print("     The urn starts with one ball of each of three colours; drawing colour j and")
    print("     returning it with another of its colour moves the site n to n + e_j with")
    print("     probability (n_j+1)/(m+3) at level m.  Its law at level m is uniform on the")
    print("     N(m) = (m+1)(m+2)/2 sites of that level:")
    cur = {(0, 0, 0): F(1)}
    for lev in range(9):
        want(all(v == F(1, N(lev)) for v in cur.values()) and len(cur) == N(lev),
             f"     level {lev}: all {len(cur)} sites carry mass 1/{N(lev)}")
        nxt = {}
        for n, v in cur.items():
            for j in range(3):
                t = tuple(n[k] + (1 if k == j else 0) for k in range(3))
                nxt[t] = nxt.get(t, F(0)) + v*F(n[j] + 1, lev + 3)
        cur = nxt

    print("\nC2  it is a unit flow from the apex to the base")
    for lev in range(7):
        fl = polya_level(lev)
        tot = sum(sum(v) for v in fl.values())
        inflow = {}
        for n, v in fl.items():
            for j in range(3):
                t = tuple(n[k] + (1 if k == j else 0) for k in range(3))
                inflow[t] = inflow.get(t, F(0)) + v[j]
        nxt = polya_level(lev + 1)
        cons = all(sum(nxt[t]) == inflow[t] for t in inflow)
        want(tot == 1 and cons,
             f"     level {lev}: total flow out = 1, and every site's inflow equals its outflow")

    print("\nC3  its level energy is exactly 1/((m+1)(m+3))")
    Msym = (m + 1)*(m + 2)/2
    Ssym = (m + 2)*(m + 1)*(m + 2)*(2*m + 3)/6 - Msym**2   # sum over the level of (n_1+1)^2
    esym = sp.simplify(3*Ssym/(Msym**2*(m + 3)**2))
    want(sp.simplify(esym - 1/((m + 1)*(m + 3))) == 0,
         "     symbolically: 3 * sum (n_1+1)^2 / (N(m)(m+3))^2 = 1/((m+1)(m+3)), where the sum")
    print("       over the level of (n_1+1)^2 is sum_{a=0..m} (a+1)^2 (m+1-a), evaluated in")
    print("       closed form.  Verified term by term against the flow itself:")
    for lev in (0, 1, 2, 3, 7, 12, 20):
        e = sum(sum(x*x for x in v) for v in polya_level(lev).values())
        want(e == F(1, (lev + 1)*(lev + 3)),
             f"     level {lev}: energy {e} = 1/({lev+1}*{lev+3})")

    print("\nC4  so the flow's total energy telescopes, and is bounded by 3/4")
    T = sp.Symbol('T', positive=True, integer=True)
    closed = sp.Rational(3, 4) - (sp.Rational(1, 2))*(1/(T + 1) + 1/(T + 2))
    want(sp.simplify(sp.summation(1/((m + 1)*(m + 3)), (m, 0, T - 1)) - closed) == 0,
         "     E_T = sum_{m<T} 1/((m+1)(m+3)) = 3/4 - (1/2)(1/(T+1) + 1/(T+2)) by partial")
    print("       fractions, hence E_T < 3/4 for EVERY T, with E_T increasing to 3/4.")
    for Tv in (1, 5, 20, 40):
        e = sum(F(1, (k + 1)*(k + 3)) for k in range(Tv))
        want(e == F(3, 4) - F(1, 2)*(F(1, Tv + 1) + F(1, Tv + 2)) and e < F(3, 4),
             f"     T = {Tv}: E_T = {e} = {float(e):.6f} < 3/4")

    print("\nC5  Thomson's principle: the minimum twist energy is bounded BELOW, uniformly in T")
    print("     The order-beta cost of a site-wise twist is the quadratic Dirichlet form on the")
    print("     backward cone with theta = theta_0 at the apex and 0 on level 0.  Its minimum is")
    print("     theta_0^2 times the effective conductance C_T, and C_T = 1/R_T with R_T the")
    print("     effective resistance, which by Thomson's principle is the minimum energy over")
    print("     unit flows - so ANY unit flow bounds it above:")
    print("       R_T <= E_T < 3/4   ==>   C_T > 4/3   for every T.")
    print("     Checked against the conductance computed directly by layer elimination:")
    prior = {1: sp.Rational(3), 2: sp.Rational(9, 4), 3: sp.Rational(117, 59),
             4: sp.Rational(2595, 1408), 5: sp.Rational(369612, 210437)}
    for Tv in (1, 2, 3, 4, 5):
        Cv = cone_conductance(Tv)
        Ev = sum(F(1, (k + 1)*(k + 3)) for k in range(Tv))
        agree = (Tv not in prior) or sp.simplify(Cv - prior[Tv]) == 0
        want(Cv > sp.Rational(4, 3) and sp.Rational(Ev.numerator, Ev.denominator)*Cv >= 1
             and agree,
             f"     T = {Tv}: C_T = {Cv} = {float(Cv):.6f} > 4/3, and R_T = 1/C_T = "
             f"{float(1/Cv):.6f} <= E_T = {float(Ev):.6f} as Thomson requires"
             + (f", matching attempt a4's exact value" if Tv in prior else ""))
    print("     The first four agree with attempt a4's independently computed conductances, so")
    print("     its table is confirmed; what it could not do was rule out a slow decay to 0,")
    print("     which C_T > 4/3 now does outright.  a4's extrapolated limit 1.38 sits above 4/3.")

    print("\nC6  where 1/sum_k P_k comes from, and why it settles nothing")
    print("     The uniform-splitting flow - split equally three ways at every site, i.e. the")
    print("     simple random walk on the cone - is also a unit flow, and its energy is")
    print("     (1/3) sum_{m<T} P_m with P_m the collision probability of that walk at level m:")
    lev = srw_levels(30)
    for Tv in (1, 3, 10, 30):
        e = F(0)
        for mm in range(Tv):
            e += sum((v/3)**2 * 3 for v in lev[mm].values())
        pk = sum(sum(v*v for v in lev[mm].values()) for mm in range(Tv))
        want(e == pk/3,
             f"     T = {Tv}: uniform-splitting energy = {float(e):.6f} = (1/3) sum P_m")
    print("     P_m ~ c/m by the local limit theorem for the plane walk, so this energy grows")
    print("     like (c/3) log T.  Numerically, against the Polya flow's bounded energy:")
    for Tv in (1, 3, 10, 30):
        e = sum(sum((v/3)**2*3 for v in lev[mm].values()) for mm in range(Tv))
        ep = sum(F(1, (k + 1)*(k + 3)) for k in range(Tv))
        print(f"       T = {Tv:2d}:  uniform-splitting {float(e):.6f}   Polya {float(ep):.6f}   "
              f"1/sum_k P_k = {float(1/(3*e)):.6f}")
    esrw30 = sum(sum((v/3)**2*3 for v in lev[mm].values()) for mm in range(30))
    ep30 = sum(F(1, (k + 1)*(k + 3)) for k in range(30))
    want(esrw30 > ep30,
         "     the uniform-splitting flow is the WORSE of the two: its energy is an upper bound")
    print("       on R_T that diverges, so its reciprocal 3/sum_k P_m is a LOWER bound on the")
    print("       conductance that tends to 0 - true, and vacuous.  The task's GIVEN (2) reads")
    print("       that vacuous lower bound as the value of the minimum.  The minimum is the")
    print("       conductance, and the Polya flow bounds it below by 4/3 for every T.")
    want(sp.limit(closed, T, sp.oo) == sp.Rational(3, 4),
         "     E_T -> 3/4, so the bound C_T > 4/3 cannot be improved by this flow beyond 4/3")

    print()
    if ok:
        print("SUMMARY: PARTIAL on the backward cone of the 2+1 sphere law: the Polya-urn unit "
              "flow (uniform on every level, step probability (n_j+1)/(m+3)) has level energy "
              "exactly 1/((m+1)(m+3)), proved in closed form, so its total energy telescopes to "
              "E_T = 3/4 - (1/2)(1/(T+1) + 1/(T+2)) < 3/4 for every T; by Thomson's principle the "
              "cone's effective resistance is R_T <= E_T < 3/4 and its conductance - which is the "
              "minimum order-beta cost of a space-time twist reaching theta_0 at the apex, per "
              "theta_0^2 - satisfies C_T > 4/3 uniformly in T, confirmed against exact layer-"
              "elimination values C_1..C_5 = 3, 9/4, 117/59, 2595/1408, ... that reproduce attempt "
              "a4's table; the uniform-splitting flow, by contrast, has energy (1/3) sum_{m<T} P_m "
              "which diverges like log T, so 1/sum_k P_k is the reciprocal of a divergent upper "
              "bound on R_T - a lower bound on the conductance that tends to 0")
        print("HIT: the task's GIVEN (2) is false as stated - the minimum space-time twist cost is "
              "NOT 1/sum_{k<T}P_k and does not tend to 0; it is the cone's conductance, which is "
              "bounded below by 4/3 for every T by the Polya-urn flow's exactly telescoping energy "
              "E_T = 3/4 - (1/2)(1/(T+1) + 1/(T+2)), so Route A's cost is Theta(1) with an "
              "explicit constant and the route is closed by a proof rather than by attempt a4's "
              "extrapolation; 1/sum_k P_k is a lower bound on the conductance read as its value")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
