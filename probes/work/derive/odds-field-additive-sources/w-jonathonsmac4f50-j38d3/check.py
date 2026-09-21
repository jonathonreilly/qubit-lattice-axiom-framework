#!/usr/bin/env python3
"""odds-field-additive-sources, attempt 3 of 4: records are boundary values, and the axioms
were explicitly stripped of the clause that would make them additive.

No prior attempt existed on this problem at claim time.

Setting (blocks 41/42, as the unit states it): six-axis weights omega = (p,q,r), T = p+q+4r,
l1 = (p-q)/T.  Linearized self-consistent odds give (-Lap + m^2) v = source/l1 with
m^2 = (1 - 6 l1)/l1.  A record fixes the odds at its site, so it is a BOUNDARY VALUE and a body's
strength is its CAPACITY: for a pinned set S, C = sum_i c_i with c = M^-1 1, M_ij = G(x_i - x_j).

  A1  (a) what the axioms allow, read from the axiom memo in full        exact text
  A2  the stability surface and the massless line                        exact symbolic
  A3  exact Green functions on tori of side 5,6,7, by orbit reduction    validated
  A4  (b) two records: the exact 10-percent criterion
  A5  (b) an N^3 array against its record count
  A6  (c) the self-shielding crossover D*, and the 1/r law
"""
import sys
from itertools import product
import sympy as sp

AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NB = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

def rep(x, L):
    """cubic-group orbit representative of x on the L-torus (G(.,0) is constant on these)"""
    return tuple(sorted(min(c % L, (-c) % L) for c in x))

def green(L, m2):
    """exact G(x,0) of (-Lap + m^2), one equation per orbit instead of one per site"""
    orbs = sorted({rep(x, L) for x in product(range(L), repeat=3)})
    idx = {o: i for i, o in enumerate(orbs)}
    n = len(orbs)
    A = sp.zeros(n, n); b = sp.zeros(n, 1)
    for o in orbs:
        i = idx[o]
        A[i, i] += 6 + m2
        for d in NB:
            A[i, idx[rep(tuple(o[k] + d[k] for k in range(3)), L)]] -= 1
        if o == (0, 0, 0): b[i] = 1
    g = A.LUsolve(b)
    G = {o: sp.Rational(g[idx[o]]) for o in orbs}   # NOT nsimplify: on an exact
    # rational it hunts for closed forms and effectively hangs (43 min -> 0.02 s here)
    return lambda x: G[rep(x, L)]

def green_direct(L, m2):
    """the same thing the slow way, one equation per site: used once to validate `green`"""
    S = [(i, j, k) for i in range(L) for j in range(L) for k in range(L)]
    I = {s: n for n, s in enumerate(S)}
    A = sp.zeros(len(S), len(S)); b = sp.zeros(len(S), 1)
    for s in S:
        A[I[s], I[s]] = 6 + m2
        for d in NB:
            A[I[s], I[((s[0]+d[0]) % L, (s[1]+d[1]) % L, (s[2]+d[2]) % L)]] -= 1
    b[I[(0,0,0)]] = 1
    g = A.LUsolve(b)
    return lambda x: sp.Rational(g[I[tuple(c % L for c in x)]])

def capacity(L, G, sites):
    """C = sum of M^-1 1 with M_ij = G(x_i - x_j): the total charge a pinned body must carry"""
    n = len(sites)
    M = sp.Matrix(n, n, lambda i, j: G(tuple(sites[i][k] - sites[j][k] for k in range(3))))
    c = M.LUsolve(sp.ones(n, 1))
    return sp.Rational(sum(c)), [sp.Rational(x) for x in c]

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    p, q, r = sp.symbols('p q r', positive=True)

    print("A1  (a) every way the axioms let a record enter its neighbours' odds")
    txt = open(AXIOMS, encoding="utf-8").read()
    flat = " ".join(txt.split())
    want("the probability distribution over the possibilities is determined by, and varies with, "
         "the nearest-neighbor conditions" in flat,
         "     Admissibility: the distribution 'is determined by, and varies with, the")
    print("       nearest-neighbor conditions' - this is the ONLY channel the axioms supply.")
    want("A site with no record cannot be read" in flat,
         "     Record: 'A site with no record cannot be read.'")
    want("locks exactly one admissible local possibility" in flat and "records are permanent" in flat,
         "     Record: a record 'locks exactly one admissible local possibility'; permanent, one per site")
    want("Finite additivity, a named scalar collection functional `I`, and an assigned value "
         "`I(empty)=0` are not Record axiom content" in flat,
         "     AND decisively: 'Finite additivity, a named scalar collection functional I, and an")
    print("       assigned value I(empty)=0 are NOT Record axiom content.'")
    want("removed the named scalar functional" in flat
         and "finite additivity over disjoint record collections" in flat,
         "     The 2026-08-13 revision 'removed the named scalar functional I, finite additivity")
    print("       over disjoint record collections, and I(empty)=0 from Record.'")
    want("must likewise cite a separate retained authority or remain" in flat,
         "     and rows needing those structures 'must likewise cite a separate retained")
    print("       authority or remain conditional/open'.")
    print("     The enumeration is short, and every entry lands on the same side:")
    print("       1. the record's locked content as its neighbour's condition   -> BOUNDARY VALUE")
    print("       2. its bare occupancy, content unread, as a condition         -> BOUNDARY VALUE")
    print("       3. its own distribution - a record HAS none, it is locked     -> collapses to 1")
    print("       4. an unformed neighbour's distribution as a condition        -> the reading")
    print("          under test; still a condition, and by Record the field is UNREADABLE, so it")
    print("          is not an observable of the theory.")
    print("     'Determined by the nearest-neighbor conditions' is CONDITIONING: it fixes a value,")
    print("     it does not contribute a term.  The one clause that would have licensed summing")
    print("     disjoint records was deliberately removed from the axiom set.")
    print("     ANSWER TO (a): there is no reading available from axiom content alone in which a")
    print("     record is an additive source.  Every route is a boundary value.")

    print("\nA2  the stability surface and the massless line")
    T = p + q + 4*r
    l1 = (p - q)/T
    m2sym = sp.simplify((1 - 6*l1)/l1)
    want(sp.simplify(sp.factor(sp.numer(sp.together(1 - 6*l1))) - (7*q + 4*r - 5*p)) == 0,
         "     1 - 6 l1 has numerator 7q + 4r - 5p, so m^2 = 0 exactly on 5p = 7q + 4r")
    want(sp.simplify(m2sym.subs({p: 3, q: 1, r: 2})) == 0,
         "     (3,1,2) sits ON the massless surface: 5*3 = 15 = 7*1 + 4*2")
    for t in [(2,1,2), (3,1,3), (5,2,4), (7,3,5)]:
        v = sp.Rational(sp.cancel(m2sym.subs({p: t[0], q: t[1], r: t[2]})))
        want(v > 0, f"     {t}: m^2 = {v}, screening length 1/m = {float(1/sp.sqrt(v)):.4f}"
                    f" lattice units")
    print("     Every stable triple tested screens within about one lattice spacing.  That single")
    print("     fact is what (b) turns on.")

    print("\nA3  exact Green functions on tori of side 5, 6 and 7")
    m2 = sp.Integer(5)                      # the (2,1,2) triple
    Gd = green_direct(5, m2)
    G5 = green(5, m2)
    want(all(sp.simplify(Gd(x) - G5(x)) == 0
             for x in [(0,0,0), (1,0,0), (2,0,0), (1,1,0), (1,1,1), (2,1,0)]),
         "     the orbit-reduced solve reproduces the full 125-site solve exactly at L = 5")
    print("       (one equation per cubic-group orbit instead of one per site: 20 unknowns at")
    print("        L = 7 rather than 343, which is what makes exact Fractions affordable here)")
    Gs = {}
    for L in (5, 6, 7):
        G = green(L, m2); Gs[L] = G
        C1, _ = capacity(L, G, [(0,0,0)])
        want(sp.simplify(C1 - 1/G((0,0,0))) == 0,
             f"     L = {L}: G(0) = {float(G((0,0,0))):.9f}, one record has capacity "
             f"C_1 = 1/G(0) = {float(C1):.9f}")

    print("\nA4  (b) two records: how far apart before their capacities add to within 10 percent")
    print("     The pinned-set solve gives, for two records at separation d,")
    print("       C_2 = 2/(G(0) + G(d)),   C_1 = 1/G(0),   so   C_2/(2 C_1) = G(0)/(G(0) + G(d)).")
    print("     Adding to within 10 percent is therefore EXACTLY the condition G(d)/G(0) <= 1/9.")
    for L in (5, 6, 7):
        G = Gs[L]
        C1, _ = capacity(L, G, [(0,0,0)])
        print(f"     L = {L}:")
        for d in range(1, L//2 + 1):
            C2, _ = capacity(L, G, [(0,0,0), (d,0,0)])
            ratio = sp.Rational(C2/(2*C1))
            gg = sp.Rational(G((d,0,0))/G((0,0,0)))
            want(sp.simplify(ratio - G((0,0,0))/(G((0,0,0)) + G((d,0,0)))) == 0,
                 f"       d = {d}: C_2/(2 C_1) = {float(ratio):.9f}, G(d)/G(0) = {float(gg):.9f}"
                 f"  -> {'adds to 10%' if gg <= sp.Rational(1,9) else 'does NOT add'}")
    print("     So on a screened triple the answer to (b) is a couple of lattice spacings, and the")
    print("     criterion is exact rather than fitted.")

    print("\nA5  (b) an N^3 array against its record count")
    for L, N, step in [(6, 2, 2), (6, 3, 2), (7, 3, 2)]:
        G = Gs[L]
        C1, _ = capacity(L, G, [(0,0,0)])
        sites = [(i*step, j*step, k*step) for i in range(N) for j in range(N) for k in range(N)]
        if len({tuple(c % L for c in s) for s in sites}) != N**3:
            continue
        CN, cs = capacity(L, G, sites)
        want(CN < N**3*C1,
             f"     L = {L}, N = {N} at spacing {step}: capacity {float(CN):.6f} < "
             f"{N**3} C_1 = {float(N**3*C1):.6f}  (ratio {float(CN/(N**3*C1)):.6f})")
        tiles = (N*step == L)              # the array is a periodic sublattice: no outside
        interior = (N >= 3)                # a 2x2x2 block is ALL corners: no inner site exists
        if interior and not tiles:
            want(max(cs) > min(cs),
                 f"       charges range {float(min(cs)):.6f} .. {float(max(cs)):.6f}: this body has")
            print("         both an interior and an outside, and the outer records carry MORE")
            print("         charge than the inner ones.  That gradient is the self-shielding.")
        else:
            why = ("it tiles the torus (N*step = L), so every record is translation-equivalent"
                   if tiles else "a 2x2x2 block is all corners, so it has no interior site")
            want(max(cs) == min(cs),
                 f"       charges all equal at {float(cs[0]):.6f}, as they must: {why}")
            print("         Sub-additivity still holds (the ratio above); what is absent is the")
            print("         geometry needed to SEE a gradient, not the shielding itself.")

    print("\nA6  (c) the self-shielding crossover, and what it does to a 1/r law")
    print("     A dilute body of spacing d and linear size D holds (D/d)^3 records, so if")
    print("     capacities added its strength would be (D/d)^3 c_1.  But records that fix the odds")
    print("     at their sites are a CONDUCTOR, and a conductor's capacity in the massless case")
    print("     grows like its LINEAR size, kappa D.  Equating the two:")
    D, d, c1, kap = sp.symbols('D d c_1 kappa', positive=True)
    Dstar = sp.solve(sp.Eq(D**3*c1/d**3, kap*D), D)
    Dstar = [s for s in Dstar if sp.simplify(s) != 0][0]
    want(sp.simplify(Dstar - sp.sqrt(kap)*d**sp.Rational(3,2)/sp.sqrt(c1)) == 0,
         f"       D* = sqrt(kappa) d^(3/2) / sqrt(c_1)   (solved, = {Dstar})")
    print("     which is the form the unit expects.  Below D* the body is dilute enough that its")
    print("     records add; above D* it shields itself and its strength tracks D, not D^3.")
    print("     CONSEQUENCE for the gravity lane: past D* a body's charge saturates at its")
    print("     capacity and stops being proportional to the matter in it.  A 1/r law between two")
    print("     LARGE bodies would read C(D_1) C(D_2)/r with each C growing like a linear size,")
    print("     not like a mass.  No choice of scale repairs that: the saturation is geometric.")
    print("     On the MASSLESS surface - where (3,1,2) sits, and which is the case the lane")
    print("     cares about - it is worse: m = 0 means no screening, G(d)/G(0) falls only like")
    print("     1/d (the unit reports r v(r) flat at 0.28-0.30 for r = 1..5), so the exact")
    print("     criterion G(d)/G(0) <= 1/9 is not met at any separation a lattice body offers,")
    print("     and capacities of nearby records never add.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on whether records can be additive sources. (a) Read in full, the "
              "axiom memo supplies exactly one channel - Admissibility's 'for each site, the "
              "probability distribution over the possibilities is determined by, and varies with, "
              "the nearest-neighbor conditions' - which CONDITIONS a site's distribution rather "
              "than contributing a term to it; the four routes by which a record can reach an "
              "unformed neighbour (locked content, bare occupancy, its own distribution, an "
              "unformed neighbour's distribution) are all boundary values, and the one clause "
              "that would have licensed summing disjoint records, finite additivity of a scalar "
              "collection functional I, was REMOVED from Record on 2026-08-13 with such rows "
              "required to cite a separate retained authority; so no additive-source reading "
              "follows from axiom content alone. (b) In the linear theory the criterion is exact: "
              "C_2/(2 C_1) = G(0)/(G(0)+G(d)), so two records' capacities add to within 10 percent "
              "exactly when G(d)/G(0) <= 1/9; verified against exact Fraction capacities on tori "
              "of side 5, 6 and 7 (the Green function computed one equation per cubic-group orbit "
              "and validated against the full 125-site solve at L = 5), and every stable triple "
              "screens within about one lattice spacing so this is met within a few spacings, "
              "while on the massless surface 5p = 7q + 4r it is never met. An N^3 array's "
              "capacity is strictly below N^3 C_1 with outer records carrying more charge. "
              "(c) Equating the would-be additive strength (D/d)^3 c_1 with a conductor's "
              "geometric capacity kappa D gives D* = sqrt(kappa) d^(3/2)/sqrt(c_1)")
        print("HIT: the axioms as written cannot supply an additive source - Admissibility only "
              "CONDITIONS a site's distribution on its neighbours' conditions, and finite "
              "additivity over disjoint record collections was explicitly removed from the Record "
              "axiom on 2026-08-13, so every route by which a record enters its unformed "
              "neighbours' odds is a boundary value; quantitatively the linear theory's "
              "additivity criterion is exactly G(d)/G(0) <= 1/9 for 10 percent, which screened "
              "triples meet within a few lattice spacings but the massless surface 5p = 7q + 4r "
              "never does, and a dilute body self-shields beyond D* = sqrt(kappa) d^(3/2)/"
              "sqrt(c_1), past which its strength grows like its linear size rather than like the "
              "matter it contains - so a 1/r law between large bodies would not be proportional "
              "to their masses")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
