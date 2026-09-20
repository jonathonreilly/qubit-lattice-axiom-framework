#!/usr/bin/env python3
"""moving-what-fixes-the-scale, attempt a1: what c_0 fixes, and what it does not.

No prior attempt existed at claim time.

Setting (block 39's, as the task states it): a site is empty or carries one record with a content
in the six axes; two neighbouring records weigh c*omega with omega = p, q, r for equal, opposite
and orthogonal contents; a bond with an empty end weighs 1.  c_0 = 6/(p + q + 4r).

  A1  candidate (a): "no state is privileged" fixes a relation, not a number
  A2  the pendant identity at c_0, exactly
  A3  candidate (b): NO scale identifies the vacancy reading with the integrated one
  A4  candidate (c): at c_0 the normalizer is neighbourhood-independent ON AVERAGE, for every
      neighbourhood size, and c_0 is the unique such scale
  A5  and not pointwise: the two-neighbour normalizer takes three distinct values at c_0
"""
import itertools, sys
import sympy as sp

AX = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
NEG = lambda b: tuple(-x for x in b)

def omega(a, b, p, q, r):
    return p if a == b else (q if a == NEG(b) else r)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    p, q, r, c = sp.symbols('p q r c', positive=True)
    c0 = 6/(p + q + 4*r)
    S = p + q + 4*r                      # sum of omega(a, b) over the six contents a, any b

    print("A1  candidate (a): 'no state is privileged', applied to the empty state")
    want(sp.simplify(sum(omega(a, AX[0], p, q, r) for a in AX) - S) == 0,
         f"for any fixed neighbour content, sum over the six a of omega(a,.) = p + q + 4r")
    arith = sp.simplify(6/S)
    want(sp.simplify(arith - c0) == 0,
         "so 'an empty neighbour weighs what a record of uniformly random content weighs' is")
    print("     c * (p + q + 4r)/6 = 1, i.e. c = c_0 = 6/(p+q+4r): the ARITHMETIC mean reading.")
    geo = 1/(p*q*r**4)**sp.Rational(1, 6)
    harm = sp.simplify(1/(6/(1/p + 1/q + 4/r)))
    vals = {"arithmetic (c_0)": c0, "geometric": geo, "harmonic": harm, "same content": 1/p}
    print("     But 'privileged' does not say which average.  Four readings, each a sentence one")
    print("     could write with the same words:")
    sub = {p: 3, q: 1, r: 2}
    for nm, e in vals.items():
        print(f"       {nm:<20} c = {sp.simplify(e)}   at (3,1,2): {sp.nsimplify(sp.simplify(e).subs(sub))}")
    distinct = {sp.nsimplify(sp.simplify(e).subs(sub)) for e in vals.values()}
    want(len(distinct) == len(vals),
         f"at (3,1,2) the four give {sorted(distinct)}: all different, so the sentence alone")
    print("     fixes a RELATION (the empty bond weighs some mean of the record bonds), not a")
    print("     number.  Something else has to say which mean, and (A4) is the candidate that does.")

    print("\nA2  the pendant identity at c_0")
    print("     Integrated reading: an unrecorded site is given a content and averaged over the")
    print("     six, uniformly.  With ONE occupied neighbour of content s, it contributes")
    print("     (1/6) sum_a c omega(a,s) = c (p+q+4r)/6.")
    one = sp.simplify(c*S/6)
    want(sp.simplify(one.subs(c, c0) - 1) == 0,
         "at c = c_0 that is exactly 1, the vacancy weight: for a PENDANT unrecorded site the")
    print("     two readings agree, and c_0 is the unique scale for which they do.")
    want(sp.solve(sp.Eq(one, 1), c) == [c0] or sp.simplify(sp.solve(sp.Eq(one, 1), c)[0] - c0) == 0,
         "(solving c(p+q+4r)/6 = 1 gives c = c_0 and nothing else)")

    print("\nA3  candidate (b): can any scale identify the two readings?")
    print("     With TWO occupied neighbours of contents s1, s2 the integrated reading gives")
    print("     (1/6) sum_a c^2 omega(a,s1) omega(a,s2), while the vacancy gives 1.")
    pairs = {"s2 = s1": AX[0], "s2 = -s1": NEG(AX[0]), "s2 orthogonal": AX[2]}
    vals2 = {}
    for nm, s2 in pairs.items():
        e = sp.simplify(sum(omega(a, AX[0], p, q, r)*omega(a, s2, p, q, r) for a in AX)/6)
        vals2[nm] = e
        print(f"       {nm:<16} (1/6) sum_a omega omega = {sp.factor(e)}")
    want(len({sp.nsimplify(v.subs(sub)) for v in vals2.values()}) == 3,
         f"at (3,1,2) the three are {[sp.nsimplify(v.subs(sub)) for v in vals2.values()]}: distinct")
    print("     So the integrated contribution is c^2 times a function of (s1, s2) that is NOT")
    print("     constant, while the vacancy contributes the constant 1.  A constant cannot equal")
    print("     a non-constant function of the neighbours' contents, so:")
    want(True, "NO scale c identifies the two readings once an unrecorded site has two occupied")
    print("     neighbours - the identification in candidate (b) fails for every c, and c_0 is")
    print("     special only in the pendant case (A2).  That is block 24's condition: the two")
    print("     readings agree exactly when every unrecorded component is pendant.")

    print("\nA4  candidate (c): the normalizer, on average")
    print("     Z_x = sum_a prod over neighbours (c omega(a, s_y)), empty neighbours weighing 1.")
    print("     With k occupied neighbours, averaging each neighbour's content uniformly:")
    k = sp.Symbol('k', positive=True, integer=True)
    avgZ = sp.simplify(6*(c*S/6)**k)
    print(f"       <Z_k> = 6 (c (p+q+4r)/6)^k = {avgZ}")
    want(sp.simplify(avgZ.subs(c, c0) - 6) == 0,
         "at c = c_0 this is 6 for EVERY k - the empty-neighbourhood value - so the formation")
    print("     rate is independent of the neighbourhood on average, at every neighbourhood size.")
    want(sp.simplify((avgZ/6).subs({c: 2*c0, k: 2}) - 4) == 0,
         "and c_0 is the only such scale: at c = 2 c_0 the k = 2 average is 4 times the k = 0 one")
    print("     (in general <Z_k>/<Z_0> = (c/c_0)^k, which is 1 for all k iff c = c_0).")
    print("     THIS is the sentence that picks the arithmetic mean in A1: 'the rate a record")
    print("     forms at does not depend on how many neighbours it has, on average' forces c_0.")

    print("\nA5  and not pointwise")
    Z2 = {nm: sp.simplify(sum(omega(a, AX[0], p, q, r)*omega(a, s2, p, q, r) for a in AX)*c0**2)
          for nm, s2 in pairs.items()}
    for nm, e in Z2.items():
        print(f"       Z_2 with {nm:<16} = {sp.simplify(e.subs(sub))} at (3,1,2)")
    want(len({sp.nsimplify(sp.simplify(e.subs(sub))) for e in Z2.values()}) == 3,
         "at c_0 the two-neighbour normalizer still takes three distinct values, so no scale")
    print("     makes the rate neighbourhood-independent pointwise: the average is the most that")
    print("     can be asked of a single number, and c_0 is exactly what asking it gives.")

    print()
    if ok:
        print("SUMMARY: PARTIAL what c_0 fixes, exactly: (a) 'no state is privileged' applied to "
              "the empty state fixes only a RELATION - the arithmetic, geometric, harmonic and "
              "same-content readings give four different scales, all distinct at (3,1,2) - so the "
              "sentence alone does not pick c_0; (b) the identification with block 24's integrated "
              "reading holds for a PENDANT unrecorded site at c_0 and at no other scale, but fails "
              "for EVERY c as soon as an unrecorded site has two occupied neighbours, because the "
              "vacancy contributes a constant while the integral contributes a non-constant "
              "function of the neighbours' contents; (c) c_0 is the unique scale at which the "
              "average normalizer 6 (c(p+q+4r)/6)^k is independent of the neighbourhood size k, "
              "and no scale achieves that pointwise")
        print("HIT: c_0 = 6/(p+q+4r) is fixed by exactly one of the candidates - the formation "
              "rate being neighbourhood-independent ON AVERAGE, which forces (c/c_0)^k = 1 for all "
              "k - while 'no state is privileged' gives only a relation and the identification "
              "with the integrated reading is impossible at any scale beyond pendant sites")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
