#!/usr/bin/env python3
"""J:derive:lightcone-formation:a3 (worker w-macbookpro90c72-j05f1, grok-4.6).

Different route from grok a2/a5/a6 (FSS, Dobrushin): Peierls defect costs of 7-stencil pi
on the 2x2x2 cube for six-axis (p,1,2), plus the symmetric-phi product identity.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def phi(a, b, p, q, r):
    if a == b:
        return p
    if a ^ 1 == b:
        return q
    return r


def e_identity():
    p, q, r = 5, 1, 2
    L = 3

    def N7(x):
        return [x, (x + 1) % L, (x - 1) % L]

    def prod_form(s, sp):
        tot = 1
        for x in range(L):
            for y in N7(x):
                tot *= phi(sp[x], s[y], p, q, r)
        return tot

    bad = 0
    for s in itertools.product(range(6), repeat=L):
        for sp in itertools.product(range(6), repeat=L):
            if prod_form(s, sp) != prod_form(sp, s):
                bad += 1
    ok("I.1 7-stencil product identity exhaustive on C3 six-axis (5,1,2)", bad == 0, f"n={6**6}")


def cube_weight(conf, p, q, r):
    N = [[i ^ (1 << b) for b in range(3)] for i in range(8)]

    def slots(x):
        out = [conf[x]]
        for y in N[x]:
            out.extend([conf[y], conf[y]])
        return out

    def Zx(x):
        sl = slots(x)
        tot = 0
        for s in range(6):
            w = 1
            for v in sl:
                w *= phi(s, v, p, q, r)
            tot += w
        return tot

    tot = 1
    for x in range(8):
        tot *= Zx(x)
    return tot


def e_peierls():
    q, r = 1, 2
    ratios = {}
    for p in (3, 5, 10, 20):
        Wa = cube_weight((0,) * 8, p, q, r)
        Wf = cube_weight((1,) + (0,) * 7, p, q, r)  # antipodal
        Wo = cube_weight((2,) + (0,) * 7, p, q, r)  # orthogonal
        ra = F(Wf, Wa)
        ro = F(Wo, Wa)
        ratios[p] = (ra, ro)
        ok(f"P.p={p} antipodal-flip/const < 1", ra < 1, str(ra))
        ok(f"P.p={p} orthogonal-flip/const < 1", ro < 1, str(ro))
    # ratios decrease in p
    ok("P.antipodals decrease in p", ratios[3][0] > ratios[5][0] > ratios[10][0] > ratios[20][0])
    ok("P.orthogonals decrease in p", ratios[3][1] > ratios[5][1] > ratios[10][1] > ratios[20][1])
    # six constants equal
    p = 5
    Ws = [cube_weight(tuple([a] * 8), p, q, r) for a in range(6)]
    ok("P.six constants equal at p=5", len(set(Ws)) == 1)
    return ratios


def main():
    e_identity()
    e_peierls()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL 7-stencil six-axis product identity holds exhaustively on C3 at (5,1,2); "
        "on the 2x2x2 cube, pi-weight ratios of a one-site antipodal or orthogonal flip to a constant "
        "are strictly less than 1 at p=3,5,10,20 on (p,1,2) and decrease in p. A Peierls cost is already "
        "positive at p=3 (L=2 degenerate stencil). This is not an FSS/LRO proof (those are grok a2) and "
        "not a Dobrushin threshold (a5)."
    )
    print(
        "HIT: 7-stencil light-cone pi for six-axis (p,1,2) has a strictly positive Peierls cost for a "
        "one-site defect on the cube at p=3,5,10,20 (antipodal and orthogonal flips lighter than a "
        "constant, ratios decreasing in p); product identity exhaustive on C3. Infinite-volume contour "
        "sum and sphere FSS are not claimed here."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
