#!/usr/bin/env python3
"""moving-what-fixes-the-scale, attempt 2 of 5: how far the c_0 identity actually reaches.

Provenance: both prior attempts are BY ME, same model family, machine and running worker: a1
(w-jonathonsmac4f50-j882f) settled (a), (c) and the second half of (b); a5
(w-jonathonsmac4f50-jc532, issue 8534) showed c_0 is the unique scale at which the 7-state
transfer operator is singular, with kernel u - sqrt(6) e_empty.  a5's section 4 item 1 asked for
the one thing that would make that a principle rather than a restatement: say what is wrong with
c /= c_0 without circularity.  The answer is to ask how far the redundancy extends, and it stops
at one bond.

  R1  the degree-j test: an empty site against an averaged record       exact
  R2  degree 1 - equality, and it is exactly c_0                        exact
  R3  degree 2 - pointwise failure, and what the gap is                 exact
  R4  degree j - equality on average over the neighbours' contents, always
  R5  the non-circular statement, and the accident at (3,1,2)
"""
import sys
import sympy as sp

AX = [0, 1, 2, 3, 4, 5]          # +e1,-e1,+e2,-e2,+e3,-e3
def opp(a):
    return a ^ 1

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    p, q, r, c = sp.symbols('p q r c', positive=True)
    c0 = 6/(p + q + 4*r)
    om = lambda a, s: p if s == a else (q if s == opp(a) else r)

    print("R1  the test that makes 'no state is privileged' checkable")
    print("     An empty site is NOT privileged if the law cannot tell it from a record whose")
    print("     content has been averaged away.  For a site x with j occupied neighbours carrying")
    print("     contents a_1..a_j, the two readings weigh")
    print("       empty:            1        (every bond with an empty end weighs 1)")
    print("       averaged record:  c^j (1/6) sum_s prod_i omega(a_i, s)")
    print("     so the question is for which c and which j the two agree.  This is a statement")
    print("     about the measure, not about an operator, so it cannot be circular with a5's")
    print("     determinant.")

    print("\nR2  degree 1: equality, and it happens at exactly one scale")
    d1 = c*sum(om(0, s) for s in AX)/6
    want(sp.simplify(d1 - c*(p + q + 4*r)/6) == 0,
         "     with one occupied neighbour the averaged record weighs c(p+q+4r)/6, so equality")
    sol = sp.solve(sp.Eq(d1, 1), c)
    want(len(sol) == 1 and sp.simplify(sol[0] - c0) == 0,
         f"     with the empty reading holds at c = 6/(p+q+4r) = c_0, and at no other scale")

    print("\nR3  degree 2: the identity fails pointwise, and the gap is a covariance")
    print("     With two occupied neighbours carrying a and b, the averaged record weighs")
    print("     c^2 (1/6) sum_s omega(a,s) omega(b,s), which depends on the PAIR:")
    pairs = {"equal": 0, "opposite": 1, "orthogonal": 2}
    vals = {}
    for nm, bb in pairs.items():
        S = sum(om(0, s)*om(bb, s) for s in AX)
        vals[nm] = sp.simplify(S)
        print(f"       {nm:11s}: sum_s omega(a,s) omega(b,s) = {sp.factor(vals[nm])}")
    want(sp.simplify(vals["equal"] - (p**2 + q**2 + 4*r**2)) == 0 and
         sp.simplify(vals["opposite"] - (2*p*q + 4*r**2)) == 0 and
         sp.simplify(vals["orthogonal"] - (2*r*(p + q) + 2*r**2)) == 0,
         "     the three pair types give three different sums, so no single c can match all")
    print("     three against the empty reading's 1 unless the sums coincide, i.e. unless")
    want(sp.simplify(vals["equal"].subs({q: p, r: p}) - vals["opposite"].subs({q: p, r: p})) == 0
         and sp.simplify(vals["equal"].subs({q: p, r: p})
                         - vals["orthogonal"].subs({q: p, r: p})) == 0,
         "     p = q = r, where all three collapse to 6p^2 - the trivial rule")
    print("     The gap between any two of them is the content covariance of omega(a,.) and")
    print("     omega(b,.), which is what the shared empty site correlates; a1 found the same")
    print("     obstruction from block 24's side, on a bridge.")

    print("\nR4  degree j: equality holds on average over the neighbours' contents, at every j")
    print("     Average the degree-j test over the contents of the neighbours themselves:")
    print("       c^j (1/6)^j sum_{a_1..a_j} (1/6) sum_s prod_i omega(a_i,s)")
    print("       = c^j (1/6) sum_s prod_i [ (1/6) sum_{a_i} omega(a_i,s) ]")
    print("       = c^j (1/6) sum_s [ (p+q+4r)/6 ]^j  =  [ c (p+q+4r)/6 ]^j,")
    inner = sp.simplify(sum(om(a, 0) for a in AX)/6)
    want(sp.simplify(inner - (p + q + 4*r)/6) == 0,
         "     because sum_a omega(a,s) = p+q+4r for EVERY s (the rule is doubly stochastic in")
    print("       that sense).  So the averaged identity is [c(p+q+4r)/6]^j, which is 1 at c_0")
    for j in (1, 2, 3, 6):
        expr = sp.simplify((c*(p + q + 4*r)/6)**j).subs(c, c0)
        want(sp.simplify(expr - 1) == 0,
             f"     j = {j}: the fully averaged weight is exactly 1 at c_0")
    print("     for every j - so the redundancy is exact at every degree ON AVERAGE, and exact")
    print("     pointwise only at j <= 1.")

    print("\nR5  what that says, and one accident")
    print("     The non-circular statement a5 asked for is therefore:")
    print("       c_0 is the unique scale at which an empty site weighs what an averaged record")
    print("       weighs, and at c_0 that identity is exact for a site with at most ONE occupied")
    print("       neighbour and exact only in mean for more.  'No state is privileged' is a")
    print("       one-bond statement; it does not extend to a site that joins two records,")
    print("       because such a site correlates their contents and an empty site does not.")
    sub = {p: 3, q: 1, r: 2}
    c0v = sp.nsimplify(c0.subs(sub))
    print(f"     At (p,q,r) = (3,1,2), c_0 = {c0v}, the three degree-2 weights are:")
    hits = []
    for nm in pairs:
        v = sp.nsimplify((c0v**2*vals[nm]/6).subs(sub))
        hits.append((nm, v))
        print(f"       {nm:11s}: {v} = {float(v):.6f}")
    want(any(v == 1 for _, v in hits) and any(v != 1 for _, v in hits),
         "     and the ORTHOGONAL one is exactly 1 while the others are not.  That is NOT an")
    print("     accident of this triple.  The orthogonal weight equals 1 iff")
    cond = sp.simplify(sp.expand(12*r*(p + q + r) - (p + q + 4*r)**2))
    want(sp.simplify(cond + (p + q - 2*r)**2) == 0,
         f"       12r(p+q+r) - (p+q+4r)^2 = -(p+q-2r)^2,   so iff  p + q = 2r  exactly")
    print("     - a scale-free condition on the weights, and the SAME one that appears in")
    print("     issue 8534 as the side condition bond-plane reflection positivity needs beyond")
    print("     c >= c_0.  Two of the lane's three standard triples sit exactly on it:")
    for tri in [(3, 1, 2), (5, 2, 4), (7, 3, 5), (4, 1, 1)]:
        s2 = {p: tri[0], q: tri[1], r: tri[2]}
        on = sp.simplify(cond.subs(s2)) == 0
        want(on == (tri[0] + tri[1] - 2*tri[2] == 0),
             f"       {tri}: p+q-2r = {tri[0]+tri[1]-2*tri[2]}, "
             f"orthogonal weight {'= 1' if on else '/= 1'}")
    print("     So the degree-2 identity is not fixed by the scale at all: one of its three")
    print("     branches is fixed by the weights, on the surface p + q = 2r.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on what fixes the binding scale: testing 'an empty site is not "
              "privileged' as a statement about the MEASURE rather than the operator - an empty "
              "site weighs 1, an averaged record with j occupied neighbours weighs "
              "c^j (1/6) sum_s prod_i omega(a_i,s) - the two agree at j = 1 at exactly one scale, "
              "c = 6/(p+q+4r) = c_0, and at j = 2 the averaged-record weight takes three "
              "different values on the equal, opposite and orthogonal pairs "
              "(p^2+q^2+4r^2, 2pq+4r^2, 2r(p+q)+2r^2), so no scale can match all three unless "
              "p = q = r; averaging instead over the NEIGHBOURS' contents gives exactly "
              "[c(p+q+4r)/6]^j, which is 1 at c_0 for every j, because sum_a omega(a,s) = p+q+4r "
              "for every s; so the redundancy is exact at every degree in mean and exact "
              "pointwise only at degree one, and the orthogonal degree-2 weight equals 1 exactly on the "
              "surface p + q = 2r, since 12r(p+q+r) - (p+q+4r)^2 = -(p+q-2r)^2 - the same "
              "scale-free condition that issue 8534 found bond-plane reflection positivity needs "
              "beyond c >= c_0 - and this holds at (3,1,2) and "
              "(7,3,5) where p+q = 2r holds, and not at (5,2,4) or (4,1,1)")
        print("HIT: 'no state is privileged' is a ONE-BOND statement: c_0 is the unique scale at "
              "which an empty site weighs what a content-averaged record weighs, that identity is "
              "exact for a site with at most one occupied neighbour, and for more neighbours it "
              "holds only in mean - exactly [c(p+q+4r)/6]^j at every degree j, but pointwise "
              "different on the equal, opposite and orthogonal pairs, the gap being the content "
              "covariance that a shared empty site cannot reproduce; one of the three degree-2 "
              "branches is fixed not by the scale but by the weights, on the surface p + q = 2r "
              "where 12r(p+q+r) - (p+q+4r)^2 = -(p+q-2r)^2 vanishes, which is the same condition "
              "reflection positivity needs in issue 8534; this is the non-circular "
              "form of a5's determinant statement, phrased about the measure instead of the "
              "operator, and it says the principle cannot fix the scale by itself beyond degree "
              "one")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
