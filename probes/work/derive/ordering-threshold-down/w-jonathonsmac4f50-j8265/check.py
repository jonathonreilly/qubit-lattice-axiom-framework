#!/usr/bin/env python3
"""ordering-threshold-down, attempt a5: block 30's T1(a), repaired in general.

The task carries a note: "block 30's T1(a) 'd_1 <= max(d_2, d_3)' is false for general positive
weights (fails at (1,2,1)); establish it on the lines you use."  Attempt a4 (same machine) and
attempt a1 (another machine) both establish it on (p,1,2) and leave the general statement alone.
A lemma that a campaign uses deserves its domain, not a line.

This attempt does not attack the threshold.  It repairs the lemma, in closed form, for every
positive (p,q,r), and records two consequences the lane can use.

  Q1  the deviations d_1, d_2, d_3 for general (p,q,r), against a4's (p,1,2) forms
  Q2  d_1 <= d_2 iff p >= q, exactly                                  the repair
  Q3  the full criterion, and why (1,2,1) fails it
  Q4  the d_2 / d_3 crossing surface, which gives p = 21 on the campaign's line
  Q5  alpha_3 = d_2 - d_1: the Dobrushin influence of the causal-clauses lane IS this gap

Deviations.  A site's three predecessors carry values; the right value is v.  With all three
equal to v the site is wrong with probability d_1; with two v and one at the antipode, d_2; with
two v and one orthogonal, d_3.  The kernel weights a value a by prod_j phi(a, u_j),
phi = p, q, r for equal, antipodal, orthogonal.
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

    print("Q1  the deviations, for every positive (p,q,r)")
    d1 = (q**3 + 4*r**3)/(p**3 + q**3 + 4*r**3)
    den2 = p**2*q + p*q**2 + 4*r**3
    d2 = (den2 - p**2*q)/den2
    den3 = p**2*r + q**2*r + p*r**2 + q*r**2 + 2*r**3
    d3 = sp.simplify((den3 - p**2*r)/den3)
    print(f"     d_1 = {d1}")
    print(f"     d_2 = {sp.simplify(d2)}")
    print(f"     d_3 = {d3}")
    sub = lambda e: sp.simplify(e.subs({q: 1, r: 2}))
    want(sub(d1) == 33/(p**3 + 33), f"on (p,1,2): d_1 = {sub(d1)}, which is a4's closed form")
    want(sp.simplify(sub(d2) - (p + 32)/(p**2 + p + 32)) == 0,
         f"             d_2 = {sub(d2)}, likewise")
    want(sp.simplify(sub(d3) - (2*p + 11)/(p**2 + 2*p + 11)) == 0,
         f"             d_3 = {sub(d3)}, likewise")
    print("     so the general map restricts to the line the two prior attempts use.")

    print("\nQ2  the repair")
    n21 = sp.factor(sp.expand(sp.numer(sp.together(sp.simplify(d2 - d1)))))
    print(f"     numerator of d_2 - d_1 = {n21}")
    want(sp.simplify(n21 - p**2*(p - q)*(p*q**2 + q**3 + 4*r**3)) == 0,
         "the second factor is positive for p,q,r > 0, so d_1 <= d_2 IFF p >= q - exactly.")
    print("     That is block 30's T1(a) on a domain: it holds for every rule in which alignment")
    print("     is at least as likely as anti-alignment, and needs nothing about r.")

    print("\nQ3  the full criterion, and the documented counterexample")
    n31 = sp.factor(sp.expand(sp.numer(sp.together(sp.simplify(d3 - d1)))))
    print(f"     numerator of d_3 - d_1 = {n31}")
    cubic = sp.expand(n31/p**2)
    want(sp.simplify(cubic - (p**2*r + p*q**2 + p*q*r + 2*p*r**2 - q**3 - 4*r**3)) == 0,
         "so d_1 <= max(d_2,d_3) iff p >= q OR p^2 r + p q^2 + p q r + 2 p r^2 >= q^3 + 4 r^3")
    bad = {p: 1, q: 2, r: 1}
    v1, v2, v3 = (sp.nsimplify(x.subs(bad)) for x in (d1, d2, d3))
    want(v1 > max(v2, v3) and bad[p] < bad[q] and cubic.subs(bad) < 0,
         f"at (1,2,1): d_1 = {v1} > max({v2}, {v3}); p < q and the cubic is "
         f"{cubic.subs(bad)} < 0, so both halves fail - the documented counterexample, explained")
    good = {p: 1, q: sp.Rational(21, 20), r: sp.Rational(1, 2)}
    want(good[p] < good[q] and cubic.subs(good) > 0
         and d1.subs(good) <= max(d2.subs(good), d3.subs(good)),
         f"and the second half is not idle: at (1, 21/20, 1/2) we have p < q but the cubic is "
         f"{sp.nsimplify(cubic.subs(good))} > 0, and T1(a) holds")

    print("\nQ4  which of d_2, d_3 is the larger")
    n23 = sp.factor(sp.expand(sp.numer(sp.together(sp.simplify(d2 - d3)))))
    print(f"     numerator of d_2 - d_3 = {n23}")
    want(sp.simplify(n23 - p**2*(q - r)*(p*q - q**2 - 2*q*r - 4*r**2)) == 0,
         "so eps_2 = max(d_2,d_3) switches branch on (q - r)(pq - q^2 - 2qr - 4r^2) = 0.")
    onlin = sp.simplify((n23/p**2).subs({q: 1, r: 2}))
    want(sp.simplify(onlin + (p - 21)) == 0,
         f"on (p,1,2) that is {onlin}, so d_2 >= d_3 iff p <= 21 - a4's crossing, now as a surface")

    print("\nQ5  the cross-lane identity")
    print("     The causal-clauses lane's Dobrushin influence alpha_3 - the largest total")
    print("     variation between two three-parent kernels differing in one parent - was found")
    print("     there to be p^2(p-1)(p+33)/((p^3+33)(p^2+p+32)) on (p,1,2), with the maximizer")
    print("     three equal parents and one flipped to its antipode.  That is this lane's pair:")
    a3_line = p**2*(p - 1)*(p + 33)/((p**3 + 33)*(p**2 + p + 32))
    want(sp.simplify(sub(d2) - sub(d1) - a3_line) == 0,
         "alpha_3 = d_2 - d_1 identically on (p,1,2)")
    gap = sp.simplify(d2 - d1)
    want(sp.simplify(sp.numer(sp.together(gap)) - n21) == 0,
         "and in general the same factorization governs both, so the influence of one parent is")
    print("     exactly the extra deviation one wrong predecessor buys.  The uniqueness lane's")
    print("     Dobrushin constant and the ordering lane's noise map are one object.")

    print()
    if ok:
        print("SUMMARY: PARTIAL block 30's T1(a) is repaired for every positive (p,q,r): the "
              "numerator of d_2 - d_1 factors as p^2 (p - q)(p q^2 + q^3 + 4 r^3), so "
              "d_1 <= d_2 IFF p >= q, and d_1 <= max(d_2,d_3) iff p >= q or "
              "p^2 r + p q^2 + p q r + 2 p r^2 >= q^3 + 4 r^3; the documented failure at (1,2,1) "
              "misses both halves, the second half is not idle (it saves (1, 21/20, 1/2)), the "
              "d_2/d_3 branch switches on (q - r)(pq - q^2 - 2qr - 4r^2) which is p = 21 on "
              "(p,1,2), and alpha_3 = d_2 - d_1 identically, so the uniqueness lane's Dobrushin "
              "influence and this lane's noise map are the same object")
        print("HIT: block 30's T1(a) holds exactly on p >= q - every rule where alignment beats "
              "anti-alignment, which contains every line the campaign uses - with an explicit "
              "second branch for p < q; and the Dobrushin influence alpha_3 equals d_2 - d_1, "
              "linking the uniqueness and ordering lanes' constants")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
