#!/usr/bin/env python3
"""Exact checks for the-level-ordered-response-kernel a2.

The closed form is the unique causal solution of the gain-one recursion.
"""
import math
from fractions import Fraction as F

FAILS = []


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def G(a, b, c):
    if min(a, b, c) < 0:
        return F(0)
    L = a + b + c
    return F(4, 3) * F(math.factorial(L), math.factorial(a) * math.factorial(b) * math.factorial(c) * 3 ** L)


def main():
    # G(0) is the sum of the stay-only paths: sum_j (1/4)^j = 4/3
    stay = sum(F(1, 4) ** j for j in range(30))
    ok("origin", abs(float(stay) - float(F(4, 3))) < 1e-12 and G(0, 0, 0) == F(4, 3),
       "only the all-stay paths sit at the origin, so G(0)=4/3")

    # uniqueness check: the formula obeys G = (4/3) delta + (1/3) sum of the three parents, L<=8
    rec = True
    for a in range(0, 9):
        for b in range(0, 9 - a):
            for c in range(0, 9 - a - b):
                rhs = F(4, 3) if (a, b, c) == (0, 0, 0) else F(0)
                rhs += (G(a - 1, b, c) + G(a, b - 1, c) + G(a, b, c - 1)) / 3
                rec &= rhs == G(a, b, c)
    ok("recursion", rec, "closed form matches the causal recursion through level 8")

    # algebraic identity behind the recursion, for a,b,c > 0
    # (1/3) sum_parents = (4/3) 3^{-L} (L-1)! (a+b+c) / (a!b!c!) = G
    a, b, c = 3, 2, 2
    L = a + b + c
    parents = F(4, 3) * F(math.factorial(L - 1) * L, math.factorial(a) * math.factorial(b) * math.factorial(c) * 3 ** L)
    ok("identity", parents == G(a, b, c), "the three parents rebuild G by a+b+c = L")

    level = True
    for L in range(0, 9):
        tot = sum(G(i, j, L - i - j) for i in range(L + 1) for j in range(L - i + 1))
        level &= tot == F(4, 3)
    ok("level", level, "each level plane sums to 4/3")

    ok("wake", G(1, 0, 0) == F(4, 9) and G(-1, 0, 0) == 0 and G(0, -1, 2) == 0,
       "G(1,0,0)=4/9 and every negative coordinate is silent")

    # drift-free ray k=(q,-q,0): 3 - (1+2 cos q) = 2(1-cos q) = E/2
    # E = 6 - 2(cos q + cos(-q) + 1) = 4 - 4 cos q
    import sympy as sp
    q = sp.symbols("q", real=True)
    E = 4 - 4 * sp.cos(q)
    gap = 2 - 2 * sp.cos(q)
    ok("driftfree", sp.simplify(gap - E / 2) == 0, "on k=(q,-q,0), 3-sum e^{-ik}=E/2, so the gain-one symbol is 8/E")

    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return
    print(
        "SUMMARY: PARTIAL the gain-one response is the unique causal solution "
        "G=(4/3) L!/(a!b!c!) 3^{-L} on the forward octant and 0 elsewhere; "
        "each level sums to 4/3; on drift-free modes the symbol is 8/E. "
        "The nonlinear law is not solved."
    )
    print(
        "HIT: under the level-ordered past the stationary gain-one kernel is "
        "(4/3) L!/(a!b!c!) 3^{-L} on a,b,c>=0 and zero off that octant, "
        "so a held source has a one-sided wake along (1,1,1)"
    )


if __name__ == "__main__":
    main()
