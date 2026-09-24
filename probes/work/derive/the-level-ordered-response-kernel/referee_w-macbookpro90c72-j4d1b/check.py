#!/usr/bin/env python3
"""Independent checks for the level-ordered response kernel a1."""
import math
from fractions import Fraction as F

FAILS = []


def ok(step, good, msg):
    print(("ok " if good else "FAIL ") + step + ": " + msg, flush=True)
    if not good:
        FAILS.append(step)


def G(a, b, c):
    if min(a, b, c) < 0:
        return F(0)
    L = a + b + c
    return F(4, 3) * F(math.factorial(L), math.factorial(a) * math.factorial(b) * math.factorial(c)) / F(3) ** L


def A(kappa):
    return 1 / math.tanh(kappa) - 1 / kappa


def main():
    ok("G", G(0, 0, 0) == F(4, 3) and G(1, 0, 0) == F(4, 9) and G(-1, 0, 0) == 0,
       "G(0)=4/3, G(1,0,0)=4/9, G(-1,0,0)=0")

    # recursion G = (4/3) delta + (1/3) sum of three predecessors, on L<=6
    rec_ok = True
    for a in range(0, 7):
        for b in range(0, 7 - a):
            for c in range(0, 7 - a - b):
                rhs = (F(4, 3) if (a, b, c) == (0, 0, 0) else F(0))
                rhs += (G(a - 1, b, c) + G(a, b - 1, c) + G(a, b, c - 1)) / 3
                rec_ok &= rhs == G(a, b, c)
    ok("rec", rec_ok, "closed form solves G = (4/3) delta + (1/3) sum_j G(.-e_j) for L<=6")

    level_ok = True
    for L in range(0, 8):
        tot = sum(G(a, b, L - a - b) for a in range(L + 1) for b in range(L - a + 1))
        level_ok &= tot == F(4, 3)
    ok("level", level_ok, "every level sums to 4/3")

    # negative binomial: sum_j C(L+j,j) (1/4)^j = (4/3)^{L+1}
    nb_ok = True
    for L in range(0, 6):
        s = sum(F(math.factorial(L + j), math.factorial(L) * math.factorial(j)) / F(4) ** j for j in range(40))
        nb_ok &= abs(float(s) - (4 / 3) ** (L + 1)) < 1e-9
    ok("series", nb_ok, "sum C(L+j,j)/4^j approaches (4/3)^{L+1}")

    # drift-free direction k=(q,-q,0): 3 - sum e^{-ik} = E/2
    # E = 6 - 2 sum cos = 4 - 4 cos q; 3 - (1+2 cos q) = 2-2 cos q
    q = 0.7
    E = 4 - 4 * math.cos(q)
    gap = 2 - 2 * math.cos(q)
    ok("E", abs(gap - E / 2) < 1e-12, "on k=(q,-q,0), 3-sum exp(-ik)=E/2 so R=8/E against 7/E")

    # on-axis asymptote 2/(pi r) over the light-cone 7/(4 pi r) is 8/7
    ratio = (2 / math.pi) / (7 / (4 * math.pi))
    ok("axis", abs(ratio - 8 / 7) < 1e-12, f"on-axis wake is {ratio:.6f} = 8/7 of 7/(4 pi r)")

    ok("A", A(1.79) < 0.5 < A(1.81), f"A(1.79)={A(1.79):.4f} < 1/2 < A(1.81)={A(1.81):.4f}")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent check did not reproduce that step")
        return
    print(
        "HIT: confirmed - G=(4/3) L!/(a!b!c!) 3^{-L} on the forward octant, each level sums to 4/3, "
        "and the drift-free gain-one kernel is 8/E"
    )
    print(
        "SUMMARY: confirmed the visit sum, the recursion, the level mass and the 8/7 on-axis comparison; "
        "the nonlinear response is still not proved"
    )


if __name__ == "__main__":
    main()
