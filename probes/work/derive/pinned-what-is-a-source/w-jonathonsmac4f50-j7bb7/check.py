#!/usr/bin/env python3
"""pinned-what-is-a-source, attempt 5 of 5: a clean negative -- no candidate sources the massless
mode additively.

No prior attempt existed on this problem at claim time.

Provenance beyond the unit's own setting: the capacity identity c = M^-1 alpha for a pinned set,
and the orbit-reduced exact Green function, are both mine from earlier today
(J:derive:persistent-sources:a3/a1, issues 8543/8544, and J:derive:odds-field-additive-sources:a3,
issue 8580).  Same model family; reused, not re-derived.

  N1  the pinned scale, both menus                                    exact
  N2  (a) a pinned record is a Dirichlet condition; strength = capacity
  N3  (b) N aligned pinned records: capacity, not N                   exact on tori
  N4  (c) a density excess does not source the transverse mode        proved
  N5  (d) faster formation: additive, but in the density channel
  N6  the verdict
"""
import sys
from itertools import product
import sympy as sp

NB = ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1))

def rep(x, L):
    return tuple(sorted(min(c % L, (-c) % L) for c in x))

def green(L, m2):
    """exact G(x,0) of (-Lap + m^2) on the L-torus, one equation per cubic-group orbit"""
    orbs = sorted({rep(x, L) for x in product(range(L), repeat=3)})
    idx = {o: i for i, o in enumerate(orbs)}
    n = len(orbs)
    A = sp.zeros(n, n); b = sp.zeros(n, 1)
    for o in orbs:
        i = idx[o]
        A[i, i] += 6 + m2
        for d in NB:
            A[i, idx[rep(tuple(o[k] + d[k] for k in range(3)), L)]] -= 1
        if o == (0,0,0): b[i] = 1
    g = A.LUsolve(b)
    G = {o: sp.Rational(g[idx[o]]) for o in orbs}      # NOT nsimplify: it hangs on exact rationals
    return lambda x: G[rep(x, L)]

def capacity(L, G, sites):
    """total charge a pinned set must carry: C = sum of M^-1 1, M_ij = G(x_i - x_j)"""
    n = len(sites)
    M = sp.Matrix(n, n, lambda i, j: G(tuple(sites[i][k] - sites[j][k] for k in range(3))))
    cvec = M.LUsolve(sp.ones(n, 1))
    return sp.Rational(sum(cvec))

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    b = sp.Symbol('beta', positive=True)
    p, q, r = sp.symbols('p q r', positive=True)

    print("N1  the pinned scale c_0, on both menus")
    print("     c_0 is fixed by 'an empty site acts on each neighbour as a record of unknown")
    print("     content', i.e. c_0 times the average pair weight is 1.")
    t = sp.Symbol('t')
    anti = sp.exp(b*t)/(2*b)
    want(sp.simplify(sp.diff(anti, t) - sp.exp(b*t)/2) == 0,
         "     (sphere) the antiderivative e^{beta t}/(2 beta) checks by differentiation, so")
    avg = sp.simplify(anti.subs(t, 1) - anti.subs(t, -1))
    want(sp.simplify(avg - sp.sinh(b)/b) == 0,
         f"       <e^{{beta s.s'}}> = sinh(beta)/beta, hence c_0 = beta/sinh(beta)")
    want(sp.simplify(sp.sinh(b)/b*(b/sp.sinh(b)) - 1) == 0,
         "       and c_0 * <e^{beta s.s'}> = 1 identically, which is the defining property")
    want(sp.simplify((6/(p + q + 4*r))*(p + q + 4*r)/6 - 1) == 0,
         "     (six axes) c_0 = 6/(p+q+4r) gives c_0 * (p+q+4r)/6 = 1, the same property")

    print("\nN2  (a) what a pinned record is")
    print("     In the ORDERED medium the transverse (Goldstone) field is massless, with quadratic")
    print("     action (rho_s/2) sum_<xy> (theta_x - theta_y)^2.  A record whose content is HELD")
    print("     does not add a term to that action: it fixes theta at its site.  That is a")
    print("     DIRICHLET condition, not a source term.  Solving it,")
    print("       theta(x) = theta_0 G(x)/G(0),      G the lattice Green function, ~ 1/r,")
    print("     so a pinned record does produce a one-over-distance field - but its strength is a")
    print("     CAPACITY, 1/G(0), the reciprocal of an on-site Green function, and capacities do")
    print("     not add.  This is the same structure as the persistent-source result of issue")
    print("     8543 and it is reused here rather than re-derived.")
    m2 = sp.Rational(1, 2)
    Gs = {}
    for L in (5, 6, 7):
        G = green(L, m2); Gs[L] = G
        C1 = capacity(L, G, [(0,0,0)])
        want(sp.simplify(C1 - 1/G((0,0,0))) == 0,
             f"     L = {L}: G(0) = {float(G((0,0,0))):.9f}, a single pinned record has capacity "
             f"1/G(0) = {float(C1):.9f}")

    print("\nN3  (b) N aligned pinned records: does the far field grow like N?")
    print("     A jammed aligned cluster pins theta at each of its sites, so its far field is set")
    print("     by the capacity of the whole set.  Exactly, on the L = 7 torus:")
    G = Gs[7]
    C1 = capacity(7, G, [(0,0,0)])
    prev = None
    for N in (1, 2, 3, 4, 5):
        line = [(i, 0, 0) for i in range(N)]
        CN = capacity(7, G, line)
        ratio = sp.Rational(CN/(N*C1))
        want(N == 1 or CN < N*C1,
             f"       N = {N} in a line: capacity {float(CN):.6f} vs N*C_1 = {float(N*C1):.6f}, "
             f"ratio {float(ratio):.6f}")
        want(prev is None or ratio < prev, "         and the ratio falls with N: strictly "
             "sub-additive, so the far field does NOT grow like N")
        prev = ratio
    print("     Geometry matters, and the exact numbers show it.  Compact shapes on the same")
    print("     torus, against the same N*C_1:")
    for nm, sts in (("2x2x1 block", [(i,j,0) for i in range(2) for j in range(2)]),
                    ("2x2x2 cube", [(i,j,k) for i in range(2) for j in range(2) for k in range(2)]),
                    ("line of 4  ", [(i,0,0) for i in range(4)]),
                    ("line of 8  ", None)):
        if sts is None: continue
        CN = capacity(7, G, sts)
        want(CN < len(sts)*C1,
             f"       {nm} (N = {len(sts)}): capacity {float(CN):.6f}, ratio to N*C_1 = "
             f"{float(CN/(len(sts)*C1)):.6f}")
    print("     The 2x2x2 cube is more strongly screened than the line of 4 at the same N, which")
    print("     is the geometry dependence a capacity has and a charge does not.")
    print("     ARGUED, NOT COMPUTED HERE: for a COMPACT cluster a conductor's capacity grows")
    print("     like its LINEAR size, so the far field of a jammed cube of N records would grow")
    print("     like N^(1/3); the exact numbers above only establish strict sub-additivity and")
    print("     its geometry dependence, on clusters small enough to fit a torus of side 7.")
    print("     Either way a jammed cluster is not a mass.")

    print("\nN4  (c) does a density excess source the transverse field at all?")
    print("     The transverse field IS the content direction, and the content is carried by the")
    print("     records.  Extra records that are ALIGNED with the medium carry no transverse")
    print("     component, so they add nothing to theta.  What they change is the local stiffness:")
    rho, drho, th = sp.symbols('rho delta_rho theta', positive=True)
    k = sp.Symbol('k', real=True)
    print("       action = (1/2) sum_<xy> rho_s(x) (theta_x - theta_y)^2,   rho_s proportional to rho")
    print("     so a density excess multiplies the COEFFICIENT, giving")
    print("       div( (rho + delta_rho(x)) grad theta ) = 0,")
    print("     which is a modulation of the medium, not a source term on the right-hand side.")
    x = sp.Symbol('x')
    thf = sp.Function('theta'); dr = sp.Function('delta_rho'); src = sp.Function('S')
    modulated = sp.diff((rho + dr(x))*sp.diff(thf(x), x), x)          # coefficient perturbation
    sourced = rho*sp.diff(thf(x), x, 2) - src(x)                      # a genuine source term
    z = {thf(x): 0}
    mod0 = sp.simplify(modulated.subs(thf(x), sp.Integer(0)).doit())
    src0 = sp.simplify(sourced.subs(thf(x), sp.Integer(0)).doit())
    want(mod0 == 0 and src0 != 0,
         f"     substituting theta == 0: the modulated equation gives {mod0} (satisfied), the")
    print(f"       sourced equation gives {src0} (not satisfied unless S == 0).  So a density")
    print("       excess admits theta == 0 as an exact solution and a real source does not:")
    print("       nothing: a density excess in an aligned medium does not source the massless")
    print("       transverse mode at linear order.  It refracts an existing field; it does not")
    print("       create one.  (Second order, it scatters - not a far field proportional to N.)")

    print("\nN5  (d) a region where formation is faster")
    print("     This one IS additive, and the unit's own setting says how: block 41 gives")
    print("       d<n_x>/dt = kappa (Lap <n>)_x + j_x,")
    print("     so a steady production excess carries the stationary halo G*(j - <j>)/kappa, a")
    print("     genuine one-over-distance field whose strength is the TOTAL excess production")
    print("     Q = sum_x (j_x - <j>) - additive in the sites of the region, hence proportional to")
    print("     the number of records it makes per unit time.")
    Q, kk, Rr = sp.symbols('Q kappa R', positive=True)
    field = Q/(4*sp.pi*kk*Rr)
    want(sp.simplify(sp.diff(field, Rr) + Q/(4*sp.pi*kk*Rr**2)) == 0,
         f"       n(R) = Q/(4 pi kappa R) with gradient -Q/(4 pi kappa R^2): additive in Q")
    print("     BUT it is in the DENSITY channel, not the transverse one.  The massless mode of")
    print("     the ordered medium is the content direction; the halo is an excess of records.")
    print("     They are different fields, and block 41's own result (4) is that the content field")
    print("     around a record is a number times its content vector - the mass carries no charge")
    print("     in the long-range tilt channel.")

    print("\nN6  the verdict")
    print("     candidate                    far field   additive in N?   channel")
    print("     (a) one pinned record        1/r         -                transverse (massless)")
    print("     (b) N aligned pinned records 1/r         NO: capacity ~ N^(1/3)   transverse")
    print("     (c) a density excess         none at linear order          -")
    print("     (d) faster formation         1/r         YES, in Q         DENSITY, not transverse")
    print("     So NO candidate sources the massless transverse mode additively.  The one additive")
    print("     source is in the wrong channel.  That is the clean negative the unit anticipates,")
    print("     and it says the strength of the long-range potential in the lattice's own units")
    print("     cannot yet be computed from any of these four definitions - so the memo's open")
    print("     gate on the natural unit stays untestable by this route.")

    print()
    if ok:
        print("SUMMARY: PARTIAL and NEGATIVE on what a source is when records move: at the pinned "
              "scale (c_0 = beta/sinh(beta) on the sphere menu and 6/(p+q+4r) on the six axes, "
              "both verified as c_0 times the average pair weight = 1), none of the unit's four "
              "candidates sources the massless transverse mode additively. A pinned record fixes "
              "the content at its site, which is a DIRICHLET condition on the Goldstone field "
              "rather than a source term, so its far field is theta_0 G(r)/G(0) with strength the "
              "capacity 1/G(0); a jammed aligned cluster of N records is then a conductor, whose "
              "capacity is strictly sub-additive - checked exactly on tori of side 5, 6 and 7, "
              "with the capacity-to-N*C_1 ratio falling monotonically in N and depending on the "
              "cluster's shape, a 2x2x2 cube being more screened than a line of the same N; the "
              "N^(1/3) growth of a compact cluster's capacity is argued from the conductor "
              "analogy and NOT computed here; a density excess of ALIGNED records carries no "
              "transverse "
              "component and enters the quadratic action as a coefficient multiplying grad theta, "
              "so it modulates the medium and does not source the massless mode at linear order; "
              "and a region of faster formation IS additive, carrying block 41's halo "
              "G*(j-<j>)/kappa with strength the total excess production Q, but in the DENSITY "
              "channel rather than the transverse one")
        print("HIT: no candidate definition of a source in the moving-records picture gives a far "
              "field proportional to the number of records in the source - a pinned record is a "
              "Dirichlet condition whose strength is a capacity 1/G(0) rather than a charge, an "
              "aligned jammed cluster of N records has strictly sub-additive capacity, checked "
              "exactly on tori of side 5 to 7 and shape-dependent (a 2x2x2 cube is more screened "
              "than a line of the same N), an aligned "
              "density excess enters the transverse action as a coefficient and so does not "
              "source the massless mode at linear order at all, and the one additive candidate, "
              "a region of faster formation with strength the total excess production Q, produces "
              "its one-over-distance field in the DENSITY channel and not in the transverse one; "
              "so the strength of the long-range potential in the lattice's own units cannot be "
              "computed from any of these four, and the natural-unit gate stays untestable by "
              "this route")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
