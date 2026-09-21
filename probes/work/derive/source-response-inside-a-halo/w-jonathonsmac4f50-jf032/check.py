#!/usr/bin/env python3
"""source-response-inside-a-halo, attempt 3 of 5: the drift does not vanish at the neutral scale,
and it points the wrong way.

No prior attempt existed on this problem at claim time.

Setting (blocks 39/40/41, as the unit states them): records move and carry their content; a site
is empty or holds one record; two neighbouring records weigh c*omega, a bond with an empty end
weighs 1.  Motion: a record hops to an EMPTY neighbour, choosing between its two positions in
proportion to the pair weights it would have there.  Gas: independent sites, density
rho(x) = rho + g x, contents uniform on the six axes.

  H1  the machinery, and the exclusion coefficient alone                exact, = -1
  H2  (a) the exact first-order drift coefficient                       exact in c,p,q,r
  H3  (b) at the neutral scale the drift is NOT zero                    exact, and why
  H4  (a) the scale c* at which the drift reverses                      exact
  H5  (c) accretion: the centre of mass of a cube of side m
  H6  (d) B inside A's halo, and why it is not a force law
"""
import sys
import sympy as sp

p, q, r, c = sp.symbols('p q r c', positive=True)
AX = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]   # the six contents AND directions
X = (0,0,0)

def om(a, b):
    if a == b: return p
    if a == tuple(-x for x in b): return q
    return r

def add(u, v): return tuple(u[i] + v[i] for i in range(3))
def adj(u, v): return add(u, tuple(-x for x in v)) in AX

def sites():
    """gas sites that can affect the hop: adjacent to the test record or to one of its targets"""
    S = set()
    for y in AX:
        S.add(y)
        for d in AX: S.add(add(y, d))
    S.discard(X)
    return sorted(S)

def drift_coeff(exclusion=True, weights=True):
    """coefficient of g in the mean drift along x, to first order in the gas density.

    <drift> = sum_s rho(s) D(s) + O(rho^2) with D(empty) = 0; rho(s) = rho + g s_x, and the
    rho-part cancels by isotropy, leaving g * sum_s s_x <D_x(s)> averaged over both contents."""
    tot = sp.Integer(0)
    for t in AX:                                   # the test record's content
        for s in sites():                          # the one gas record's position
            for a in AX:                           # its content
                D = sp.Integer(0)
                for y in AX:                       # candidate targets
                    if exclusion and y == s: continue          # the target must be empty
                    if weights:
                        Wx = c*om(t, a) if adj(X, s) else sp.Integer(1)
                        Wy = c*om(t, a) if adj(y, s) else sp.Integer(1)
                    else:
                        Wx = Wy = sp.Integer(1)
                    D += y[0]*Wy/(Wx + Wy)
                tot += sp.Rational(1, 36)*s[0]*D
    return sp.simplify(tot)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("H1  the machinery, and exclusion on its own")
    print("     A record at x hops to an empty neighbour y with weight W(y)/(W(x)+W(y)), where")
    print("     W(z) is the product of pair weights z would have against the RECORDED neighbours")
    print("     of z (x itself is vacated, so it does not count in W(y)).  To first order in the")
    print("     gas density only one gas record matters at a time, and the isotropic part of the")
    print("     density cancels, so the drift is g times sum_s s_x <D_x(s)>.")
    print("     With the weights switched off, only the blocking of an occupied target survives:")
    excl = drift_coeff(exclusion=True, weights=False)
    want(sp.simplify(excl + 1) == 0,
         f"       exclusion coefficient = {excl}, exactly -1, independent of c, p, q, r")
    print("     and that is checkable by hand: a gas record on a target blocks that hop, so")
    print("     D_x(s) = -s_x/2 for s a neighbour, giving -(1/2) sum_{s in AX} s_x^2 = -1.")
    print("     Blocking alone therefore pushes the test record DOWN the gradient.")

    print("\nH2  (a) the full first-order drift coefficient")
    full = drift_coeff()
    num, den = sp.fraction(sp.cancel(full))
    print(f"     coefficient of g  =  ({sp.expand(num)}) / ({sp.factor(den)})")
    want(sp.simplify(sp.cancel(full) - sp.cancel(
         (18*c**3*p*q*r - 10*c**2*p*q + 11*c**2*p*r + 11*c**2*q*r
          - 17*c*p - 17*c*q + 4*c*r - 24)/(3*(c*p + 1)*(c*q + 1)*(c*r + 1)))) == 0,
         "     - an exact rational function of c and the six-axis weights")

    print("\nH3  (b) the drift at the neutral scale")
    print("     The unit expects zero here, on the ground that a record 'binds to nothing without")
    print("     a cycle' at c_0.  It is not zero.  At c_0 = 6/(p+q+4r):")
    rows = []
    for tri in [(3,1,2), (12,1,2), (5,2,4), (7,3,5)]:
        sub = {p: tri[0], q: tri[1], r: tri[2]}
        c0 = sp.Rational(6, tri[0] + tri[1] + 4*tri[2])
        val = sp.nsimplify(sp.cancel(full.subs(sub)).subs(c, c0))
        wt = sp.nsimplify(sp.cancel(drift_coeff(exclusion=False).subs(sub)).subs(c, c0))
        rows.append((tri, c0, val, wt))
        want(val < 0,
             f"       {tri}: c_0 = {c0}, drift coefficient = {val} = {float(val):+.6f}  (< 0)")
    print("     and the part that is NOT blocking is also nonzero at c_0:")
    for tri, c0, val, wt in rows:
        print(f"       {tri}: weights-only part = {wt} = {float(wt):+.6f}")
    want(all(w != 0 for _, _, _, w in rows),
         "     so neither cause vanishes at the neutral scale.")
    print("     WHY.  <c_0 omega> = 1 over uniform contents, which is what makes a random-content")
    print("     neighbour weigh what a void weighs.  But the hop uses phi/(1+phi) with")
    print("     phi = c_0 omega, and that function is CONCAVE, so <phi/(1+phi)> < 1/2 = the value")
    print("     at the mean.  A neighbouring record therefore lowers the chance of hopping TOWARDS")
    print("     it even when it weighs one on average.  'No binding without a cycle' is a")
    print("     statement about the static measure; the drift in a gradient is a non-equilibrium")
    print("     kinetic asymmetry, and it survives the absence of binding.")

    print("\nH4  (a) the scale at which the drift reverses")
    print("     The coefficient's denominator is positive, so the sign is the numerator's:")
    for tri in [(3,1,2), (12,1,2), (5,2,4), (7,3,5)]:
        sub = {p: tri[0], q: tri[1], r: tri[2]}
        c0 = sp.Rational(6, tri[0] + tri[1] + 4*tri[2])
        nm = sp.Poly(sp.expand(sp.numer(sp.cancel(full.subs(sub)))), c)
        rts = [x for x in sp.real_roots(nm) if x > 0]
        want(len(rts) >= 1 and float(rts[0]) > float(c0),
             f"       {tri}: c_0 = {float(c0):.4f}, drift reverses at c* = {float(rts[0]):.6f}, "
             f"c*/c_0 = {float(rts[0]/c0):.4f}")
    print("     So the answer to 'towards higher density?' is: only above c*, which on every")
    print("     triple tested lies 1.4 to 2.1 times the neutral scale.  At and just above c_0 a")
    print("     free record drifts AWAY from density; it is attracted only well into the binding")
    print("     regime.  Below c* the gas is dispersive, not accretive.")

    print("\nH5  (c) accretion: the centre of mass of a held cube of side m")
    print("     Let the cube capture gas at a rate proportional to the local density on each face,")
    print("     with constant kappa.  The two x-faces sit at +-m/2 and see rho +- g m/2, so")
    m, kap, g, rho = sp.symbols('m kappa g rho', positive=True)
    dMX = sp.simplify(m**2*kap*((rho + g*m/2)*(m/2) + (rho - g*m/2)*(-m/2)))
    want(sp.simplify(dMX - kap*g*m**4/2) == 0,
         f"       d(M X_cm)/dt = {dMX} = kappa g m^4 / 2")
    vcm = sp.simplify(dMX/m**3)
    want(sp.simplify(vcm - kap*g*m/2) == 0,
         f"       and with M = m^3, the centre of mass moves at {vcm} = kappa g m / 2")
    print("     LINEAR in the side m, i.e. proportional to (record count)^(1/3).  A lump therefore")
    print("     drifts up the gradient even where a single record drifts down: accretion and hop")
    print("     asymmetry are different mechanisms with different signs and different sizes.")

    print("\nH6  (d) B inside A's halo, and what kind of law this is")
    Q, R, kk = sp.symbols('Q R kappa', positive=True)
    print("     Block 41's halo is u = Q G / kappa with G the lattice Green function, ~ 1/(4 pi R)")
    print("     at large R, so the gradient B sits in is")
    gR = sp.simplify(sp.diff(Q/(4*sp.pi*kk*R), R))
    want(sp.simplify(gR + Q/(4*sp.pi*kk*R**2)) == 0,
         f"       g(R) = d/dR [Q/(4 pi kappa R)] = {gR},  so |g| = Q/(4 pi kappa R^2)")
    print("     Feeding that into H5, a cube of side m at distance R from a producer of strength Q")
    print("       v_B  =  kappa g m / 2  =  Q m / (8 pi R^2),")
    print("     so the velocity goes as ONE OVER R SQUARED, linearly in A's production Q_A, and")
    print("     linearly in B's linear size (the cube root of its record count).")
    print("     SYMMETRY: v_B depends on (Q_A, m_B) and v_A on (Q_B, m_A).  These agree only if")
    print("     production is proportional to size for both bodies.  In general the law is NOT")
    print("     symmetric under exchanging A and B - there is no single 'mass' that plays both")
    print("     roles, because the source strength Q and the response size m are different")
    print("     attributes of a lump.")
    print("     AND IT IS NOT A FORCE LAW.  v proportional to g is overdamped: the velocity is")
    print("     set by the local gradient, with no memory.  A force law with inertia needs a")
    print("     conserved momentum to accelerate, and block 41's result (1) is that the ONLY local")
    print("     additive invariant density is the occupancy - there is no momentum density in the")
    print("     model to carry inertia.  Getting one would mean adding a conserved vector density,")
    print("     which is new axiom content, not a consequence of the present clauses.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on the response inside a halo: the first-order drift of a free "
              "test record in a gas with density gradient g is exactly "
              "g(18c^3 pqr - 10c^2 pq + 11c^2 pr + 11c^2 qr - 17cp - 17cq + 4cr - 24)/"
              "(3(cp+1)(cq+1)(cr+1)), of which the blocking of occupied targets contributes "
              "exactly -1 independently of c, p, q and r.  At the neutral scale this is NEGATIVE "
              "on every triple tested - -26/45 sort of magnitudes, specifically the coefficient is "
              "negative at (3,1,2), (12,1,2), (5,2,4) and (7,3,5) - so contrary to the unit's "
              "expectation a single test record does NOT have zero drift at the neutral scale: it "
              "drifts AWAY from density.  Both causes survive at c_0: blocking, and the concavity "
              "of phi/(1+phi), which makes <phi/(1+phi)> < 1/2 even though <c_0 omega> = 1.  The "
              "drift reverses to up-gradient only above a scale c* which is 1.38 to 2.09 times "
              "c_0 on the triples tested.  A held cube of side m instead drifts up the gradient at "
              "kappa g m / 2, linear in the side; combined with the halo u = QG/kappa this gives "
              "v_B = Q_A m_B/(8 pi R^2), one over R squared, linear in A's production and in B's "
              "linear size, hence NOT symmetric under exchanging A and B")
        print("HIT: contrary to the expectation that a test record has zero drift at the neutral "
              "scale because it binds to nothing without a cycle, the exact first-order drift "
              "coefficient is negative at c_0 on every triple tested - the record drifts AWAY "
              "from higher density - and it stays negative until a reversal scale c* that is 1.38 "
              "to 2.09 times c_0; the blocking of occupied targets contributes exactly -1 "
              "independently of all four parameters, and the remaining part is nonzero at c_0 "
              "because the hop uses the concave phi/(1+phi) so <phi/(1+phi)> < 1/2 even where "
              "<c_0 omega> = 1, which is the difference between a statement about the static "
              "measure and a kinetic asymmetry out of equilibrium; a held cube of side m instead "
              "drifts UP the gradient at kappa g m/2, so inside a halo u = QG/kappa the velocity "
              "of B is Q_A m_B/(8 pi R^2) - one over R squared but linear in A's production and "
              "in B's linear size separately, so the law is not symmetric in A and B, and being "
              "overdamped it is not a force law at all")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
