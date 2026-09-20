#!/usr/bin/env python3
"""ordering-threshold-down, attempt 2 of 5: the three deviations have no fixed order.

Provenance: three prior attempts exist.  Two (w-jonathonsmac4f50-j8265, -jc31e) are by the same
model family, machine and running worker; j8265 is MINE, and derived the general noise map used
below.  The third (w-macbookpro90c72-jaf39) is from another machine.  I re-run none of their
routes.  j8265's section 4 item 2 says block 30's note "should carry the domain p >= q"; this
attempt works out exactly which comparisons that domain is hiding, and finds that every one of
the three deviations is the largest somewhere.

  O1  the noise map, restated                                            exact
  O2  d2 - d1 has the sign of p - q, exactly                             proved
  O3  d3 - d2 factors, and vanishes exactly at q = r                     proved
  O4  each of d1, d2, d3 is the maximum somewhere                        exact witnesses
  O5  what survives inside the lane's own regime p > q
"""
import sys
import sympy as sp

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    p, q, r = sp.symbols('p q r', positive=True)

    print("O1  the noise map of the level automaton (from attempt j8265)")
    d1 = (q**3 + 4*r**3)/(p**3 + q**3 + 4*r**3)
    d2 = (p*q**2 + 4*r**3)/(p**2*q + p*q**2 + 4*r**3)
    d3 = ((q**2*r + p*r**2 + q*r**2 + 2*r**3)
          / (p**2*r + q**2*r + p*r**2 + q*r**2 + 2*r**3))
    print("     d1 = (q^3 + 4r^3)/(p^3 + q^3 + 4r^3)")
    print("     d2 = (pq^2 + 4r^3)/(p^2 q + pq^2 + 4r^3)")
    print("     d3 = (q^2 r + pr^2 + qr^2 + 2r^3)/(p^2 r + q^2 r + pr^2 + qr^2 + 2r^3)")
    for d, nm in [(d1, "d1"), (d2, "d2"), (d3, "d3")]:
        want(sp.simplify(d.subs({q: p, r: p}) - sp.Rational(5, 6)) == 0,
             f"     {nm} = 5/6 at p = q = r, the unbiased rule")

    print("\nO2  d2 - d1 has exactly the sign of p - q")
    n21 = sp.factor(sp.numer(sp.together(sp.simplify(d2 - d1))))
    want(sp.simplify(n21 - p**2*(p - q)*(p*q**2 + q**3 + 4*r**3)) == 0,
         f"     numerator of d2 - d1 is p^2 (p - q)(p q^2 + q^3 + 4 r^3)")
    print("     Both denominators and the bracket are positive for positive weights, so")
    print("       d2 > d1  <=>  p > q,   d2 = d1  <=>  p = q,   d2 < d1  <=>  p < q.")
    print("     That is precisely the domain j8265 asked block 30's note to carry, and it is an")
    print("     equivalence, not a sufficient condition.")

    print("\nO3  d3 - d2 factors too, and its zero set is q = r")
    n32 = sp.factor(sp.numer(sp.together(sp.simplify(d3 - d2))))
    want(sp.simplify(n32 + p**2*(q - r)*(p*q - q**2 - 2*q*r - 4*r**2)) == 0,
         f"     numerator of d3 - d2 is -p^2 (q - r)(p q - q^2 - 2 q r - 4 r^2)")
    print("     so d3 = d2 exactly on q = r, or on the surface p q = q^2 + 2 q r + 4 r^2.")
    for tri in [(10, 1, 1), (4, 1, 1)]:
        s = {p: tri[0], q: tri[1], r: tri[2]}
        want(sp.simplify(d3.subs(s) - d2.subs(s)) == 0,
             f"     {tri} has q = r, and indeed d2 = d3 = {sp.nsimplify(d2.subs(s))}")

    print("\nO4  each of the three is the maximum somewhere")
    rows = []
    for tri in [(3, 1, 2), (5, 2, 4), (7, 3, 5), (3, 2, 1), (1, 3, 2), (2, 1, 3)]:
        s = {p: tri[0], q: tri[1], r: tri[2]}
        v = [sp.nsimplify(d.subs(s)) for d in (d1, d2, d3)]
        mx = max(range(3), key=lambda i: v[i])
        rows.append((tri, v, mx))
        print(f"       {tri}: d1 = {float(v[0]):.5f}  d2 = {float(v[1]):.5f}  "
              f"d3 = {float(v[2]):.5f}   -> max is d{mx+1}")
    want(sorted({mx for _, _, mx in rows}) == [0, 1, 2],
         "     all three indices occur as the maximum, so NO fixed one of d1, d2, d3 dominates")
    print("     the others over the whole positive octant.  Any argument that names one of them")
    print("     as the noise parameter is domain-restricted, and the domain is explicit above.")
    for tri, v, mx in rows:
        if mx == 0:
            want(tri[0] < tri[1],
                 f"     and where d1 is the maximum, {tri}, the weights have p < q - consistent")
    print("       with O2, since d1 > d2 requires exactly p < q.")

    print("\nO5  inside the lane's own regime")
    print("     Every triple this lane works with has p > q (the equal-axis weight is the")
    print("     ordering preference), so by O2 d2 > d1 there, always, and d1 is never the")
    print("     maximum.  The live competition is d2 against d3, decided by O3's two factors:")
    for tri in [(3, 1, 2), (5, 2, 4), (7, 3, 5), (3, 2, 1)]:
        s = {p: tri[0], q: tri[1], r: tri[2]}
        f1 = tri[1] - tri[2]
        f2 = sp.simplify((p*q - q**2 - 2*q*r - 4*r**2).subs(s))
        bigger = "d3" if sp.simplify(d3.subs(s) - d2.subs(s)) > 0 else "d2"
        want((bigger == "d3") == (f1*f2 < 0),
             f"     {tri}: q - r = {f1}, pq - q^2 - 2qr - 4r^2 = {f2}, product "
             f"{'<' if f1*f2 < 0 else '>='} 0, and the larger is {bigger}")
    print("     So within p > q the ordering of d2 and d3 still flips - at (3,1,2) it is d2, at")
    print("     (3,2,1) it is d3 - and a two-level domination that assigns a fixed role to each")
    print("     must either take the maximum or carry q < r as a hypothesis.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on the ordering-threshold noise map: the three deviations have no "
              "fixed order on the positive octant.  Exactly, the numerator of d2 - d1 is "
              "p^2 (p - q)(p q^2 + q^3 + 4 r^3), so d2 > d1 if and only if p > q - an equivalence, "
              "which is the domain attempt j8265 asked block 30's note to carry; the numerator of "
              "d3 - d2 is -p^2 (q - r)(p q - q^2 - 2 q r - 4 r^2), so d2 = d3 exactly on q = r or "
              "on p q = q^2 + 2 q r + 4 r^2, verified at (10,1,1) and (4,1,1); and each of d1, d2, "
              "d3 is the strict maximum somewhere - d2 at (3,1,2), d3 at (3,2,1), d1 at (1,3,2) - "
              "with d1 maximal only where p < q, consistent with the first factorization; inside "
              "the lane's own regime p > q the deviation d1 is never the maximum, but d2 against "
              "d3 still flips between (3,1,2) and (3,2,1)")
        print("HIT: d2 - d1 and d3 - d2 both factor, giving d2 > d1 exactly when p > q and "
              "d3 = d2 exactly on q = r or p q = q^2 + 2 q r + 4 r^2, and all three deviations "
              "are attained as the maximum at explicit triples - so no fixed one of d1, d2, d3 "
              "dominates the noise map, any domination argument naming one of them is "
              "domain-restricted with the domain now explicit, and the condition p >= q that "
              "block 30's note was asked to carry is exactly the d2 > d1 comparison, an "
              "equivalence rather than a sufficient condition")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
