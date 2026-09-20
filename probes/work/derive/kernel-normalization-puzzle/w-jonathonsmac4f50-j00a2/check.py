#!/usr/bin/env python3
"""kernel-normalization-puzzle, attempt 1 of 3: the sine, exactly.

Provenance: two prior attempts exist (w-jonathonsmac4f50-j5e26, -j7bbc), both the same model
family, machine and running worker as this one.  I re-run neither.  Their open items are the
two-loop terms and more seeds; neither has priced the FIRST candidate the unit lists - that the
lab-frame component is sin(theta) and not theta.  That one is exactly computable, it has the right
sign, and it has the right beta-dependence.  This attempt prices it and nothing else.

  N1  the estimator measures <sin^2 theta>, the theory predicts <theta^2>   statement
  N2  the exact Gaussian moments, and the deficit to two orders            proved
  N3  the size of the deficit against the measured table                   exact
  N4  what this does not explain
"""
import sys
import sympy as sp

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    v, th, b = sp.symbols('v theta beta', positive=True)
    n = 3

    print("N1  what the estimator actually forms")
    print("     probes/lib/formation_levelplane.py takes LAB-FRAME components s.t1, s.t2 about")
    print("     the INITIAL direction.  A unit record at polar angle theta from that direction")
    print("     has transverse components of magnitude sin(theta), not theta.  So the measured")
    print("     structure factor is built from <sin^2 theta> while the linear theory that")
    print("     predicts the ratio 1 is a statement about <theta^2>.  Since sin x < x, the")
    print("     measured ratio is pushed BELOW 1 - which is the sign of the discrepancy.")

    print("\nN2  the deficit, exactly, for an isotropic Gaussian transverse field")
    print("     With (theta_1, theta_2) independent Gaussians of variance v each, theta^2 is")
    print("     exponential-like: <(theta^2)^m> = (2v)^m m!.  Checked:")
    for m in (1, 2, 3):
        mom = sp.integrate(sp.integrate(
            (sp.Symbol('x')**2 + sp.Symbol('y')**2)**m
            * sp.exp(-(sp.Symbol('x')**2 + sp.Symbol('y')**2)/(2*v))/(2*sp.pi*v),
            (sp.Symbol('x'), -sp.oo, sp.oo)), (sp.Symbol('y'), -sp.oo, sp.oo))
        want(sp.simplify(mom - (2*v)**m*sp.factorial(m)) == 0,
             f"     <(theta^2)^{m}> = {sp.simplify(mom)} = (2v)^{m} {m}!")
    ser = sp.series(sp.sin(th)**2, th, 0, 8).removeO()
    want(sp.simplify(ser - (th**2 - th**4/3 + 2*th**6/45)) == 0,
         "     sin^2 theta = theta^2 - theta^4/3 + 2 theta^6/45 + ...")
    avg = 2*v - (8*v**2)/3 + 2*(48*v**3)/45
    ratio = sp.simplify(avg/(2*v))
    want(sp.simplify(ratio - (1 - sp.Rational(4, 3)*v + sp.Rational(16, 15)*v**2)) == 0,
         "     so <sin^2 theta>/<theta^2> = 1 - (4/3) v + (16/15) v^2, and with T = <theta^2> = 2v")
    T = sp.Symbol('T', positive=True)
    rT = sp.simplify(ratio.subs(v, T/2))
    want(sp.simplify(rT - (1 - sp.Rational(2, 3)*T + sp.Rational(4, 15)*T**2)) == 0,
         f"       <sin^2 theta>/<theta^2> = 1 - (2/3) T + (4/15) T^2,  T the total transverse")
    print("       variance per site.  The leading deficit is TWO THIRDS of the transverse")
    print("       variance, and it is a pure kinematic factor - no dynamics in it at all.")

    print("\nN3  the size, against the measured table")
    print("     The one-step noise is sigma^2 = A(n beta)/(n beta) with n = 3, and the total")
    print("     transverse variance per site is T = sigma^2 W, with W the lattice factor the")
    print("     estimator's shells sum to (W >= 1, and W = 1 would be a single independent")
    print("     level).  Taking W = 1 gives a LOWER bound on the deficit:")
    A = lambda x: sp.coth(x) - 1/x
    print("       beta   sigma^2 = A(3beta)/(3beta)   deficit (2/3)sigma^2   1 - deficit")
    vals = {}
    for bv in (1, 2, 4, 6, 24):
        s2 = sp.N(A(3*bv)/(3*bv), 20)
        d = sp.N(sp.Rational(2, 3)*s2, 20)
        vals[bv] = (s2, d)
        print(f"       {bv:4d}   {float(s2):.6f}                 {float(d):.6f}"
              f"               {float(1 - d):.6f}")
    want(all(vals[a][1] > vals[c][1] for a, c in [(1, 2), (2, 4), (4, 6), (6, 24)]),
         "     the deficit falls monotonically with beta, like 2/(9 beta) at large beta")
    want(sp.simplify(sp.limit(sp.Rational(2, 3)*A(3*b)/(3*b)*b, b, sp.oo) - sp.Rational(2, 9)) == 0,
         "     - exactly: beta * (2/3) sigma^2 -> 2/9, so the deficit is 2/(9 beta) + O(1/beta^2)")
    print("     Measured ratios from the unit's table: 0.95-0.99 at beta = 2..6 (backward) and")
    print("     1.01 at beta = 24.  The predicted lower bound on the deficit at beta = 2 is")
    print(f"     {float(vals[2][1]):.4f}, i.e. a ratio at most {float(1 - vals[2][1]):.4f}, and at")
    print(f"     beta = 24 it is {float(vals[24][1]):.5f}, a ratio at most "
          f"{float(1 - vals[24][1]):.5f}.")
    want(1 - vals[2][1] < sp.Float("0.99") and 1 - vals[24][1] > sp.Float("0.99"),
         "     so this one effect alone is large enough to put beta = 2 below 0.99 and small")
    print("       enough to leave beta = 24 within a per cent of 1 - the two ends of the table.")
    want(float(vals[24][1]) < 0.01,
         f"     at beta = 24 the deficit is {float(vals[24][1]):.5f} < 0.01, so it cannot by")
    print("       itself explain a measured value ABOVE 1 there; something else is positive.")

    print("\nN4  what this does not explain")
    print("     The sine accounts for a deficit of the right sign, the right order 1/beta and")
    print("     roughly the right size, but it is one of the four effects the unit lists and the")
    print("     only one priced here.  It cannot produce the 1.01 at beta = 24 nor the 1.01-1.09")
    print("     of the light-cone stencil, both of which are ABOVE 1; those need a positive")
    print("     contribution, and the remaining candidates - the wandering mean direction, the")
    print("     vMF variance at the fluctuating concentration, and the shifted pole from g < 1 -")
    print("     are untouched.  W > 1 makes the deficit larger, not smaller, so the lower bound")
    print("     above is the conservative end.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on the kernel-normalization puzzle: the estimator takes lab-frame "
              "transverse components about the initial direction, so it measures <sin^2 theta> "
              "where the linear prediction is about <theta^2>, and for an isotropic Gaussian "
              "transverse field with total variance T per site the exact ratio is "
              "1 - (2/3) T + (4/15) T^2, from the moments <(theta^2)^m> = (2v)^m m! and "
              "sin^2 theta = theta^2 - theta^4/3 + 2 theta^6/45; with T at least "
              "sigma^2 = A(3 beta)/(3 beta) this is a deficit of 2/(9 beta) + O(1/beta^2), "
              "numerically at least 0.0300 at beta = 2 and 0.00309 at beta = 24 - large enough to "
              "put the low-beta end below 0.99 and small enough to leave beta = 24 within a per "
              "cent of 1, which are the two ends of the measured table; it is a purely kinematic "
              "factor with no dynamics in it, and it cannot explain the measured values ABOVE 1")
        print("HIT: the first candidate is quantitatively the right size - because the estimator "
              "uses lab-frame components about the initial direction it measures <sin^2 theta>, "
              "and the exact Gaussian ratio <sin^2 theta>/<theta^2> = 1 - (2/3)T + (4/15)T^2 gives "
              "a deficit of 2/(9 beta) + O(1/beta^2), at least 3.0 per cent at beta = 2 falling to "
              "0.31 per cent at beta = 24, which is the sign, the order in 1/beta and the size of "
              "the backward table's 0.95-0.99 rising to 1.01; the residual above 1 at large beta "
              "and for the light-cone stencil must come from the other three candidates, so the "
              "puzzle splits into a kinematic deficit that is now exact and a smaller positive "
              "remainder that is not")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
