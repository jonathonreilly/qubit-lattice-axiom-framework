#!/usr/bin/env python3
"""Independent checks for corrigendum-PR8174 a1.

Closed forms from the six-axis menu, the two sign identities, and the 1..7 census.
"""
import itertools
from fractions import Fraction as F

import sympy as sp

FAILS = []


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def weights(p, q, r, preds):
    """phi on the six states. preds are labels in {0,1,2,3,4,5}: even/odd are opposites."""
    def phi(u, v):
        if u == v:
            return p
        if u // 2 == v // 2:
            return q
        return r
    def w(u):
        val = 1
        for v in preds:
            val *= phi(u, v)
        return val
    total = sum(w(u) for u in range(6))
    return total, total - w(0)


def main():
    p, q, r = sp.symbols("p q r", positive=True)
    # kernel closed forms, a = state 0
    D1k, num1 = weights(p, q, r, (0, 0, 0))
    D2k, num2 = weights(p, q, r, (0, 0, 1))
    D3k, num3 = weights(p, q, r, (0, 0, 2))
    D1 = p ** 3 + q ** 3 + 4 * r ** 3
    D2 = p * q * (p + q) + 4 * r ** 3
    D3 = r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3
    ok("forms", sp.expand(D1k - D1) == 0 and sp.expand(num1 - (q ** 3 + 4 * r ** 3)) == 0
       and sp.expand(D2k - D2) == 0 and sp.expand(num2 - (p * q ** 2 + 4 * r ** 3)) == 0
       and sp.expand(D3k - D3) == 0 and sp.expand(num3 - (r * q ** 2 + r ** 2 * (p + q) + 2 * r ** 3)) == 0,
       "D1, D2, D3 and the dissent masses match the six-axis kernel")

    g = r * p ** 2 + (q ** 2 + q * r + 2 * r ** 2) * p - (q ** 3 + 4 * r ** 3)
    id2 = sp.expand(p * D2 - q * D1 - (p - q) * (q ** 2 * (p + q) + 4 * r ** 3))
    id3 = sp.expand(p * D3 - r * D1 - r * g)
    ok("signs", id2 == 0 and id3 == 0, "p D2 - q D1 = (p-q)(q^2(p+q)+4r^3) and p D3 - r D1 = r g")

    gq = sp.factor(sp.expand(g.subs(p, q)))
    gstrip = sp.factor(sp.expand(g.subs(p, q - 2 * r)))
    ok("boundary", gq == 2 * r * (q + 2 * r) * (q - r) and gstrip == -4 * r ** 2 * (q + r),
       "g(q)=2r(q+2r)(q-r) and g(q-2r)=-4r^2(q+r)")
    dg = sp.diff(g, p)
    ok("root", sp.expand(dg - (2 * r * p + q ** 2 + q * r + 2 * r ** 2)) == 0 and g.subs(p, 0) == -(q ** 3 + 4 * r ** 3),
       "g increases from a negative value at p=0, so it has one positive root")

    # point and census
    def nums(pp, qq, rr):
        pp, qq, rr = F(pp), F(qq), F(rr)
        d1 = (qq ** 3 + 4 * rr ** 3) / (pp ** 3 + qq ** 3 + 4 * rr ** 3)
        d2 = (pp * qq ** 2 + 4 * rr ** 3) / (pp * qq * (pp + qq) + 4 * rr ** 3)
        d3 = (rr * qq ** 2 + rr ** 2 * (pp + qq) + 2 * rr ** 3) / (rr * (pp ** 2 + qq ** 2) + rr ** 2 * (pp + qq) + 2 * rr ** 3)
        gg = rr * pp ** 2 + (qq ** 2 + qq * rr + 2 * rr ** 2) * pp - (qq ** 3 + 4 * rr ** 3)
        return d1, d2, d3, gg
    d1, d2, d3, gg = nums(1, 2, 1)
    ok("point", d1 == F(12, 13) and d2 == F(4, 5) and d3 == F(9, 10) and gg == -3,
       "at (1,2,1), d1=12/13 > 9/10 = max(d2,d3)")

    fail = 0
    mismatch = 0
    for pp, qq, rr in itertools.product(range(1, 8), repeat=3):
        d1, d2, d3, gg = nums(pp, qq, rr)
        bad = d1 > max(d2, d3)
        pred = pp < qq and gg < 0
        fail += bad
        mismatch += bad != pred
    ok("census", fail == 127 and mismatch == 0, f"{fail} of 343 triples fail, exactly where p<q and g<0")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent algebra did not match")
        return
    print(
        "HIT: confirmed - d1 > max(d2,d3) exactly when p<q and g<0, so the clause holds on p >= min(q,p*)"
    )
    print(
        "SUMMARY: confirmed the kernel closed forms, both sign identities, g(q) and g(q-2r), "
        "the point (1,2,1), and the count 127/343"
    )


if __name__ == "__main__":
    main()
