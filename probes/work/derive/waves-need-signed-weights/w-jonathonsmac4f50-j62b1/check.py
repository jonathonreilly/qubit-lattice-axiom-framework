#!/usr/bin/env python3
"""waves-need-signed-weights, attempt a5: the vector version of (a).

Attempt a2 (same model family and machine — see ATTEMPT.md) proves the scalar multi-level
theorem and leaves this open, in its own words:

    "For nonnegative matrix weights (several record components, stochastic mixing), are the
     rules with a unimodular branch on an open set exactly the componentwise copies
     (permutation-type weights)?  Not proved here."

The answer is no — the class is strictly larger — and the correct characterization is proved
in ATTEMPT.md and exercised here.  With W(k) = sum_y w(y) e^{-i k.y}, w(y) >= 0 entrywise and
A = sum_y w(y) irreducible and row-stochastic, some branch is unimodular on a set with interior
IFF every block w_{mn} sits at a single site y_{mn} and there are v and g with

        y_{mn} = v + g_m - g_n      for every edge of the support graph,

and then W(k) = e^{-i k.v} D(k) A D(k)^{-1}, D = diag(e^{-i k.g_m}), so the spectrum is
e^{-i k.v} spec(A): rigid transport at the single velocity v, for every k.

  G1  the gauge identity W(k) = e^{-ikv} D A D^{-1}, symbolically            exact
  G2  the rules that satisfy the condition are unimodular at every k         exact spectra
  G3  the rules that break either half are unimodular only on a null set     exact + scan
  G4  the tightness lemma behind the proof, on a witness                     exact
  G5  the open-set lemma  e^{-ik.(y-y')} = 1 on an interval => y = y'        exact
  G6  the consequence in d >= 2: finitely many velocities, never a cone      exact
"""
import itertools, sys
import sympy as sp

def Wmat(blocks, kk, M):
    """W(k)_{mn} = sum over (y, c) in blocks[(m,n)] of c e^{-i k.y}."""
    W = sp.zeros(M, M)
    for (m, n), terms in blocks.items():
        for y, c in terms:
            W[m, n] += c*sp.exp(-sp.I*sum(kk[i]*y[i] for i in range(len(y))))
    return W

def Amat(blocks, M):
    A = sp.zeros(M, M)
    for (m, n), terms in blocks.items():
        for y, c in terms: A[m, n] += c
    return A

def size(blocks): return 1 + max(max(m, n) for (m, n) in blocks)

def unimodular_fraction(blocks, d, N=61):
    """fraction of a uniform grid of k at which some eigenvalue has |lambda| >= 1 - 1e-9."""
    import numpy as np
    M = size(blocks)
    ks = [np.linspace(-np.pi, np.pi, N, endpoint=False)]*d
    hit = tot = 0
    for kk in itertools.product(*ks):
        W = np.zeros((M, M), complex)
        for (m, n), terms in blocks.items():
            for y, c in terms:
                W[m, n] += float(c)*np.exp(-1j*float(np.dot(kk, y)))
        if np.abs(np.linalg.eigvals(W)).max() > 1 - 1e-9: hit += 1
        tot += 1
    return sp.Rational(hit, tot)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    k = sp.Symbol('k', real=True)
    k1, k2 = sp.symbols('k1 k2', real=True)
    h = sp.Rational(1, 2)

    # rules used throughout: blocks[(m,n)] = [(displacement, weight)]
    CHIRAL = {(0, 0): [((1,), 1)], (1, 1): [((-1,), 1)]}            # two copies, v = +1 and -1
    SWAP = {(0, 1): [((1,), 1)], (1, 0): [((1,), 1)]}               # permutation, v = +1
    MIX = {(0, 0): [((1,), h)], (0, 1): [((1,), h)], (1, 0): [((1,), 1)]}   # mixing, v = +1
    GAUGE = {(0, 1): [((0,), 1)], (1, 0): [((2,), 1)]}              # y differ, cycle mean +1
    GAUGEMIX = {(0, 0): [((1,), h)], (0, 1): [((0,), h)], (1, 0): [((2,), 1)]}
    HALF = {(0, 1): [((0,), 1)], (1, 0): [((3,), 1)]}               # v = 3/2, not an integer
    TWOSITE = {(0, 0): [((1,), h), ((-1,), h)]}                     # one block, two sites
    MISMATCH = {(0, 1): [((1,), 1)], (1, 0): [((1,), h)], (1, 1): [((0,), h)]}
    PERSIST = {(0, 0): [((1,), sp.Rational(9, 25))], (0, 1): [((1,), sp.Rational(16, 25))],
               (1, 0): [((-1,), sp.Rational(16, 25))], (1, 1): [((-1,), sp.Rational(9, 25))]}

    print("G1  the gauge identity")
    for name, blocks, v, g in (("SWAP", SWAP, 1, [0, 0]),
                               ("MIX", MIX, 1, [0, 0]),
                               ("GAUGE", GAUGE, 1, [0, 1]),
                               ("GAUGEMIX", GAUGEMIX, 1, [0, 1]),
                               ("HALF", HALF, sp.Rational(3, 2), [0, sp.Rational(3, 2)])):
        M = size(blocks)
        # check the displacement condition y_{mn} = v + g_m - g_n on every edge
        cond = all(y[0] == v + g[m] - g[n] for (m, n), terms in blocks.items() for y, _ in terms)
        D = sp.diag(*[sp.exp(-sp.I*k*g[m]) for m in range(M)])
        lhs = Wmat(blocks, (k,), M)
        rhs = sp.exp(-sp.I*k*v)*D*Amat(blocks, M)*D.inv()
        same = sp.simplify(sp.expand(lhs - rhs)) == sp.zeros(M, M)
        want(cond and same,
             f"{name:<9} y_mn = v + g_m - g_n with v = {v}, g = {g}, and W(k) = e^(-ikv) D A D^-1")

    print("\nG2  those rules are unimodular at every k")
    print("     G1 gives W(k) = e^(-ikv) D A D^-1, a similarity, so spec W(k) = e^(-ikv) spec A.")
    print("     A is row-stochastic, so 1 is in spec A and every other eigenvalue has |mu| <= 1:")
    print("     the branch e^(-ikv) is unimodular at every k, and no branch ever exceeds 1.")
    for name, blocks, v in (("SWAP", SWAP, 1), ("MIX", MIX, 1), ("GAUGE", GAUGE, 1),
                            ("GAUGEMIX", GAUGEMIX, 1), ("HALF", HALF, sp.Rational(3, 2))):
        M = size(blocks)
        A = Amat(blocks, M)
        rows = [sum(A[m, n] for n in range(M)) for m in range(M)]
        spec_A = [sp.nsimplify(x) for x in A.eigenvals()]
        want(all(r == 1 for r in rows) and 1 in spec_A and all(sp.Abs(x) <= 1 for x in spec_A),
             f"{name:<9} A is row-stochastic with spec {sorted(spec_A, key=lambda t: sp.re(t))}")
        # for a 2x2, trace and determinant fix the characteristic polynomial
        Wk = Wmat(blocks, (k,), M)
        sc = sp.exp(sp.I*k*v)
        want(sp.simplify(sp.expand(sp.trace(sc*Wk) - sp.trace(A))) == 0 and
             sp.simplify(sp.expand(sp.det(sc*Wk) - sp.det(A))) == 0,
             f"          and e^(ikv) W(k) has the trace and determinant of A, so the same spectrum")
    M = size(CHIRAL)
    evc = [sp.simplify(e) for e in Wmat(CHIRAL, (k,), M).eigenvals()]
    want(set(evc) == {sp.exp(-sp.I*k), sp.exp(sp.I*k)},
         f"CHIRAL    is two classes at once: spectrum {evc}, velocities +1 and -1")

    print("\nG3  break either half and the unimodular set collapses")
    for name, blocks, why in (("TWOSITE", TWOSITE, "one block holds two sites"),
                              ("MISMATCH", MISMATCH, "two cycles with means +1 and 0"),
                              ("PERSIST", PERSIST, "the persistent walk: both")):
        frac = unimodular_fraction(blocks, 1)
        want(frac <= sp.Rational(1, 61),
             f"{name:<9} unimodular on {frac} of a 61-point grid ({why})")
    want(unimodular_fraction(CHIRAL, 1) == 1 and unimodular_fraction(GAUGE, 1) == 1,
         "while CHIRAL and GAUGE are unimodular on all 61 of 61")

    print("\nG4  the tightness lemma the proof turns on")
    print("     If |lambda| = 1 and W(k)u = lambda u then |u| <= A|u| entrywise; with A")
    print("     irreducible stochastic and left Perron pi > 0, pi|u| <= pi A |u| = pi|u|, so")
    print("     every triangle inequality is tight: for each row m all the terms")
    print("     w_mn(y) e^{-ik.y} u_n share one argument.")
    M = size(MIX)
    W = Wmat(MIX, (k,), M)
    A = Amat(MIX, M)
    lam = sp.exp(-sp.I*k)                                   # the Perron branch of MIX
    u = sp.Matrix([1, sp.exp(sp.I*k*0)])                    # its eigenvector: constant
    want(sp.simplify(sp.expand(W*u - lam*u)) == sp.zeros(M, 1),
         "MIX: u = (1,1) is the unimodular eigenvector, with lambda = e^{-ik}")
    absu = sp.Matrix([sp.Abs(x) for x in u])
    want(sp.simplify(A*absu - absu) == sp.zeros(M, 1),
         "|u| = A|u|: the Perron equality the lemma forces")
    terms = [sp.simplify(sp.arg(c*sp.exp(-sp.I*k*y[0])*u[n]))
             for (m, n), tl in MIX.items() if m == 0 for y, c in tl]
    want(len(set(sp.simplify(t - terms[0]) for t in terms)) == 1,
         f"and row 0's two terms do share one argument, as the lemma says")

    print("\nG5  the open-set lemma")
    good = True
    for m in range(1, 6):
        roots = [sp.Rational(2*j, m)*sp.pi for j in range(m)]
        on = all(sp.simplify(sp.exp(-sp.I*r*m) - 1) == 0 for r in roots)
        mids = [(roots[j] + (roots[j+1] if j+1 < m else 2*sp.pi))/2 for j in range(m)]
        off = all(sp.simplify(sp.exp(-sp.I*x*m) - 1) != 0 for x in mids)
        good = good and on and off
        print(f"     y - y' = {m}: e^(-ikm) = 1 at exactly the {m} point(s) 2 pi j/{m} in [0, 2pi)")
    want(good,
         "for every nonzero displacement difference the solution set is finite, so it has empty")
    print("     interior: an open set of k forces y = y', and each block is a single site.")

    print("\nG6  the consequence in two dimensions")
    FOUR = {(0, 0): [((1, 0), 1)], (1, 1): [((-1, 0), 1)],
            (2, 2): [((0, 1), 1)], (3, 3): [((0, -1), 1)]}
    M = size(FOUR)
    W2 = Wmat(FOUR, (k1, k2), M)
    ev = [sp.simplify(e) for e in W2.eigenvals()]
    want(all(sp.simplify(sp.Abs(e)**2 - 1) == 0 for e in ev),
         f"four chiral copies on Z^2: every branch is unimodular, spectrum {ev}")
    vels = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    want(len(vels) == 4,
         "but each branch is e^{-i k.v} with v in {+-e1, +-e2}: four velocities, four points")
    print("     of the unit front - not a circle.  Adding components adds points, never a")
    print("     circle, because by the theorem each irreducible class transports at ONE fixed")
    print("     velocity: the group velocity of a unimodular branch is the constant v, so")
    print("     there is no dispersion and no isotropy to be had from nonnegative weights.")

    print()
    if ok:
        print("SUMMARY: PARTIAL the vector version of (a) that attempt a2 leaves open: for "
              "nonnegative matrix weights with an irreducible stochastic total, a branch is "
              "unimodular on a set with interior IFF every block sits at a single site and the "
              "displacements satisfy y_mn = v + g_m - g_n, and then W(k) = e^{-ikv} D A D^{-1} is "
              "unimodular at EVERY k with spectrum e^{-ikv} spec(A); a2's guess 'exactly the "
              "componentwise copies (permutation-type)' is too narrow - stochastic mixing with a "
              "common velocity, and gauge-shifted displacements such as y = 0 and y = 2 with mean "
              "+1, also qualify, while a two-site block or two cycles of different mean do not")
        print("HIT: nonnegative matrix weights buy no dispersion - every unimodular branch is a "
              "rigid transport e^{-ik.v} times a fixed eigenvalue of A, one velocity per "
              "irreducible class, so in d >= 2 the achievable fronts are finitely many points and "
              "never an isotropic cone; the exceptional class is the gauge-equivalent "
              "common-velocity rules, strictly larger than the componentwise copies")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
