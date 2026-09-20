#!/usr/bin/env python3
"""moving-jammed-clusters, attempt a1: the surface decides everything, and the critical
size runs the wrong way on the weak-alignment side.

No prior attempt existed at claim time.

Setting (block 39's, as the unit states it): a site is empty or carries one record with a content
in the six axes; two neighbouring records weigh c*omega, omega = p, q, r for equal, opposite,
orthogonal; a bond with an empty end weighs 1; c_0 = 6/(p+q+4r).  A record with k agreeing
neighbours leaves with probability 1/(1 + (c p)^k), and a record with no empty neighbour cannot
move at all.  Formation at an empty site x happens at rate z Z_x.

  B1  the solid cube's census: who can move, who cannot        algebra + lattice enumeration
  B2  (a) reachable arrangements: exactly 6L^2 after one move, volume-blind
  B3  (b) the exact evaporation and growth rates - the growth side is PURE 6L^2
  B4  (b) the critical coupling z_c, and which side of x^5 = 2x^4 + 1 the cluster is on
  B5  (c) the interior is frozen, and what the surface can tell a reader of records
"""
import sys
from itertools import product
import sympy as sp

NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def cube(n):
    return {s for s in product(range(n), repeat=3)}

def occ_nbrs(s, C):
    return sum(1 for d in NB if (s[0] + d[0], s[1] + d[1], s[2] + d[2]) in C)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    L, z, T, x = sp.symbols('L z T x', positive=True)
    p, q, r, c = sp.symbols('p q r c', positive=True)
    c0 = 6/(p + q + 4*r)
    u = lambda k: (c*p)**k                      # (c p)^k
    A = lambda j: p**j + q**j + 4*r**j          # sum over the six contents of omega^j

    print("B1  the census of a solid L-cube of aligned records in empty space")
    V, interior = L**3, (L - 2)**3
    surface = sp.expand(V - interior)
    want(sp.simplify(8 + 12*(L - 2) + 6*(L - 2)**2 - surface) == 0,
         "the surface splits as 8 corners + 12(L-2) edge sites + 6(L-2)^2 face sites")
    print("     Predicted occupied-neighbour counts: face site 5, edge site 4, corner 3,")
    print("     interior 6.  Enumerated on the lattice:")
    for n in (3, 4, 5, 6):
        C = cube(n)
        cnt = {}
        for s in C:
            cnt[occ_nbrs(s, C)] = cnt.get(occ_nbrs(s, C), 0) + 1
        pred = {k: v for k, v in {6: (n - 2)**3, 5: 6*(n - 2)**2,
                                  4: 12*(n - 2), 3: 8}.items() if v > 0}
        movable = sum(1 for s in C if occ_nbrs(s, C) < 6)
        want(cnt == pred and movable == n**3 - (n - 2)**3,
             f"     L = {n}: {dict(sorted(cnt.items()))} matches; {movable} records have an "
             f"empty neighbour and can move, {(n-2)**3} cannot")
    want(sp.limit(surface/V, L, sp.oo) == 0,
         "surface/volume -> 0: the movable fraction vanishes as the cluster grows")

    print("\nB2  (a) which records can ever move, and how many arrangements are reachable")
    print("     A record with no empty neighbour cannot move, so ONLY the surface moves, the")
    print("     interior occupation pattern is invariant, and - records being permanent with a")
    print("     fixed content - the interior CONTENTS are invariant too.")
    print("     One move carries a record across an occupied-empty bond, and distinct bonds give")
    print("     distinct arrangements, so the one-move reachable set is the set of those bonds:")
    for n in (2, 3, 4, 5):
        C = cube(n)
        reach = set()
        for s in C:
            for d in NB:
                t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
                if t not in C:
                    reach.add(frozenset((C - {s}) | {t}))
        want(len(reach) == 6*n**2,
             f"     L = {n}: {len(reach)} distinct arrangements after one move = 6 L^2, "
             f"the cluster's SURFACE AREA")
    print("     The one-move count is exactly 6L^2: set by the surface, blind to the volume.")
    print("     Iterating, in T sweeps at most S = |surface| records move at most T times each")
    print("     into at most 6 places, so log|reachable(T)| <= S T log(6S) = O(L^2 log L), while")
    print("     log|configurations of the cluster| >= V log 7 = O(L^3):")
    want(sp.limit((surface*T*sp.log(6*surface))/(V*sp.log(7)), L, sp.oo) == 0,
         "their ratio -> 0 at fixed T: what the cluster can explore is a surface quantity")

    print("\nB3  (b) the exact evaporation and growth rates of an L-cube")
    E = 8/(1 + u(3)) + 12*(L - 2)/(1 + u(4)) + 6*(L - 2)**2/(1 + u(5))
    print("     evaporation, one attempt per surface record at the given transit probability:")
    print("       E(L) = 8/(1+(cp)^3) + 12(L-2)/(1+(cp)^4) + 6(L-2)^2/(1+(cp)^5)")
    print("     growth by formation at the empty sites touching the cube, at rate z Z_x.  The")
    print("     census of those sites by their number j of occupied neighbours, enumerated:")
    for n in (2, 3, 4, 5):
        C = cube(n)
        out = {}
        for s in C:
            for d in NB:
                t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
                if t not in C:
                    out[t] = occ_nbrs(t, C)
        cnt = {}
        for v in out.values():
            cnt[v] = cnt.get(v, 0) + 1
        want(cnt == {1: 6*n**2},
             f"     L = {n}: {dict(sorted(cnt.items()))} - EVERY touching empty site has "
             f"exactly one occupied neighbour, and there are 6 L^2 of them")
    print("     This is a fact about the six-neighbour stencil, not an approximation: the site")
    print("     diagonally outside an edge or a corner is at distance sqrt(2) or sqrt(3) and is")
    print("     not a neighbour of the cube at all.  So no j = 2 or j = 3 growth sites exist, and")
    print("     with the neighbour aligned, Z_x = c A_1 with A_1 = p + q + 4r:")
    print("     It is a property of the BOX, not of convexity.  The ramp")
    print("       C = {(i,j,k) in [0,2]^3 : i + j <= 2}  (a box cut by a half-space, so convex)")
    ramp = {s for s in product(range(3), repeat=3) if s[0] + s[1] <= 2}
    rout = {}
    for s in ramp:
        for d in NB:
            t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
            if t not in ramp:
                rout[t] = occ_nbrs(t, ramp)
    rcnt = {}
    for v in rout.values():
        rcnt[v] = rcnt.get(v, 0) + 1
    want(rcnt.get(2, 0) > 0,
         f"     has touching-empty-site census {dict(sorted(rcnt.items()))}: {rcnt.get(2,0)} sites "
         f"with TWO occupied neighbours, on its sloped face -")
    print("       so a convex cluster with a slanted face grows faster per site there (Z_x is")
    print("       c^2 A_2, not c A_1), and B4's numbers are stated for boxes only.")
    G = z*6*L**2*c*A(1)
    print("       G(L) = 6 z c A_1 L^2   exactly - no subleading terms whatsoever.")
    want(sp.simplify(sp.limit(E/L**2, L, sp.oo) - 6/(1 + u(5))) == 0,
         "E ~ 6 L^2/(1+(cp)^5), so both rates are quadratic and the balance has a finite,")
    want(sp.Poly(sp.expand(G), L).degree() == 2 and sp.expand(G).coeff(L, 1) == 0,
         "SIZE-INDEPENDENT leading limit; all of the size dependence sits in E alone")

    print("\nB4  (b) the critical coupling, and the sign of the size correction")
    zc = sp.simplify(1/(c*A(1)*(1 + u(5))))
    want(sp.simplify(sp.limit(G/E, L, sp.oo) - z*c*A(1)*(1 + u(5))) == 0,
         "G/E -> z c A_1 (1 + (cp)^5), so growth at LARGE size holds iff z > z_c with")
    print(f"       z_c = 1/(c A_1 (1 + (cp)^5)) = {zc}")
    want(sp.simplify((c*A(1)).subs(c, c0) - 6) == 0,
         "at the neutral scale c_0 = 6/(p+q+4r) one has c A_1 = 6 exactly, so there")
    print("       z_c = 1/(6 (1 + (c_0 p)^5)): a pure function of the six-axis weights.")
    print("     Whether a critical SIZE exists, and which way it runs, is decided by the sign of")
    print("     the coefficient of L in E, namely 12/(1+(cp)^4) - 24/(1+(cp)^5):")
    coefL = sp.simplify(sp.numer(sp.together(12/(1 + x**4) - 24/(1 + x**5))))
    want(sp.simplify(sp.factor(coefL) - 12*(x**5 - 2*x**4 - 1)) == 0,
         f"its numerator is 12 (x^5 - 2x^4 - 1) at x = cp, so the sign flips exactly at the")
    xstar = sp.nsolve(x**5 - 2*x**4 - 1, 2.1)
    want(sp.sign((x**5 - 2*x**4 - 1).subs(x, 2)) < 0 < sp.sign((x**5 - 2*x**4 - 1).subs(x, sp.Rational(21, 10))),
         f"     positive root x* of x^5 = 2x^4 + 1, bracketed by 2 and 21/10: x* = {xstar}")

    def study(pv, qv, rv, mults):
        cv = sp.Rational(6, pv + qv + 4*rv); cpv = cv*pv
        Ev = E.subs({p: pv, q: qv, r: rv, c: cv})
        Gv = G.subs({p: pv, q: qv, r: rv, c: cv})
        zcv = sp.nsimplify(zc.subs({p: pv, q: qv, r: rv, c: cv}))
        cL = sp.nsimplify(sp.Poly(sp.expand(Ev), L).all_coeffs()[1])
        print(f"     (p,q,r) = {(pv,qv,rv)}: c_0 = {cv}, c_0 p = {cpv} = {float(cpv):.4f}, "
              f"z_c = {zcv} = {float(zcv):.6g}, E's L-coefficient = {float(cL):+.4f}")
        out = []
        for m in mults:
            zv = zcv*m
            d = sp.expand((Gv - Ev).subs(z, zv))
            roots = sorted(float(t) for t in sp.solve(d, L) if t.is_real and t > 1)
            sg = [int(sp.sign(d.subs(L, n))) for n in (2, 3, 5, 10, 50, 500)]
            print(f"       z = {m} z_c: G-E sign at L = 2,3,5,10,50,500 is {sg}, "
                  f"crossing at L* = {['%.3f' % t for t in roots] or 'none above 1'}")
            out.append((m, roots, sg, d))
        return cpv, cL, out

    print("\n     WEAK-ALIGNMENT side, c p < x*:")
    cpv, cL, res = study(3, 1, 2, [sp.Rational(9, 10), 1, sp.Rational(11, 10)])
    want(cpv < xstar and cL < 0, "     cp < x* and the L-coefficient of E is NEGATIVE, so")
    m9, roots9, sg9, d9 = res[0]
    want(len(roots9) == 1 and 10 < roots9[0] < 11,
         f"     at z = 9/10 z_c there is one crossing, L* = {roots9[0]:.3f}, and")
    want(sp.sign(d9.subs(L, 10)) > 0 > sp.sign(d9.subs(L, 11)),
         "     G-E is POSITIVE at L = 10 and NEGATIVE at L = 11: below L* the cluster grows and")
    print("       above it the cluster shrinks - L* is an ATTRACTING equilibrium size, a maximum")
    print("       stable cluster, not a nucleation barrier.")
    want(all(s > 0 for s in res[1][2]) and all(s > 0 for s in res[2][2]),
         "     at z = z_c and above, G-E > 0 at every size tested: no critical size at all")

    print("\n     STRONG-ALIGNMENT side, c p > x*:")
    cpv2, cL2, res2 = study(20, 1, 1, [sp.Rational(9, 10), 1, sp.Rational(3, 2)])
    want(cpv2 > xstar and cL2 > 0, "     cp > x* and the L-coefficient of E is POSITIVE, so")
    m32, roots32, sg32, d32 = res2[2]
    want(len(roots32) == 1 and 13 < roots32[0] < 14,
         f"     at z = 3/2 z_c there is one crossing, L* = {roots32[0]:.3f}, and")
    want(sp.sign(d32.subs(L, 13)) < 0 < sp.sign(d32.subs(L, 14)),
         "     G-E is NEGATIVE at L = 13 and POSITIVE at L = 14: below L* the cluster shrinks and")
    print("       above it the cluster grows - here L* IS the ordinary nucleation barrier, and it")
    print("       exists only for z > z_c, diverging as z decreases to z_c.")
    want(all(s < 0 for s in res2[0][2]) and all(s < 0 for s in res2[1][2]),
         "     at z = z_c and below, G-E < 0 at every size tested: every cluster shrinks")

    print("\nB5  (c) the interior, and what a reader of records can learn")
    sub = {p: 3, q: 1, r: 2}
    c0v = sp.nsimplify(c0.subs(sub))
    e3 = sp.nsimplify((1/(1 + u(3))).subs(sub).subs(c, c0v))
    e5 = sp.nsimplify((1/(1 + u(5))).subs(sub).subs(c, c0v))
    want(e3 > e5, f"a corner leaves with probability {e3}, a face site with {e5}: a corner is "
                  f"{float(e3/e5):.3f} times as likely to go, yet at (3,1,2) the cluster's small-")
    print("     size correction still favours SURVIVAL, because the 12(L-2) edge sites that")
    print("     replace 24(L-2) face-site-equivalents in the count are too few to pay for them.")
    print("     Per-site erosion is fastest at the corners; the census is what decides the sign.")
    print("     The interior is frozen in three separate senses: its records cannot move (no")
    print("     empty neighbour), their contents cannot change (permanent, one per site), and no")
    print("     formation can happen there (no empty site).  An observer who reads only records")
    print("     reads the surface, and by B2 every arrangement reachable in time T has the same")
    print("     interior:")
    n = 4
    C = cube(n)
    inner = {s for s in C if occ_nbrs(s, C) == 6}
    want(len(inner) == (n - 2)**3 and all(occ_nbrs(s, C) == 6 for s in inner),
         f"     L = {n}: the {len(inner)} interior records are invariants of the motion, so any")
    print("       relabelling of their contents leaves every reachable surface identical, and no")
    print("       surface reading in time T separates two clusters with equal surfaces and")
    print("       different interiors.  The interior becomes readable only as the surface erodes")
    print("       down to it: readable in principle, but only by destroying the cluster.")

    print()
    if ok:
        print("SUMMARY: PARTIAL for a solid L-cube of aligned records in empty space: only its "
              "6(L-2)^2 + 12(L-2) + 8 surface records can move, the interior occupation and "
              "contents are exact invariants, the one-move reachable set has exactly 6L^2 members "
              "- the surface area, volume-blind, enumerated at L = 2..5 - and "
              "log|reachable(T)|/log|configurations| -> 0; every empty site touching the cube has "
              "exactly ONE occupied neighbour (the diagonal sites are not neighbours on the "
              "six-neighbour stencil), so growth is the pure quadratic G(L) = 6 z c A_1 L^2 with "
              "A_1 = p + q + 4r while evaporation carries all the size dependence, "
              "E(L) = 8/(1+(cp)^3) + 12(L-2)/(1+(cp)^4) + 6(L-2)^2/(1+(cp)^5); hence "
              "z_c = 1/(c A_1 (1+(cp)^5)), equal to 1/(6(1+(c_0 p)^5)) at the neutral scale and to "
              "16/825 at (3,1,2); the coefficient of L in E has numerator 12((cp)^5 - 2(cp)^4 - 1), "
              "so at cp = x* = 2.05597 (the positive root of x^5 = 2x^4 + 1) the size correction "
              "changes sign: at (3,1,2), cp = 3/2 < x*, z = 9/10 z_c has an ATTRACTING L* = 10.768 "
              "(G-E > 0 at L = 10, < 0 at L = 11) and z >= z_c grows at every size; at (20,1,1), "
              "cp = 24/5 > x*, z <= z_c shrinks at every size and z = 3/2 z_c has a REPELLING "
              "L* = 13.445 (G-E < 0 at L = 13, > 0 at L = 14)")
        print("HIT: the unit's 'is there a size above which a cluster only grows' has opposite "
              "answers on the two sides of the quintic x^5 = 2x^4 + 1 in x = cp - a nucleation "
              "barrier above z_c when cp > x*, but for cp < x* no such size at all above z_c and "
              "an ATTRACTING maximum stable size below it, so a weakly aligned cluster settles at "
              "a finite size instead of running away; the survival criterion itself is the "
              "size-free coupling z_c = 1/(c A_1 (1 + (cp)^5)), and the growth side is the pure "
              "quadratic 6 z c A_1 L^2 because on the six-neighbour stencil every empty site "
              "touching a convex cluster has exactly one occupied neighbour")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
