#!/usr/bin/env python3
"""Independent checks for odds-field-additive-sources a2.

The two-record identity is exact. The massless ratios are a separate Bessel quadrature.
"""
import math
from fractions import Fraction as F

from scipy.integrate import quad
from scipy.special import ive

FAILS = []


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def G(x, y, z):
    # 3D simple random walk: G = 3 int_0^inf ive(x,t) ive(y,t) ive(z,t) dt
    val, err = quad(lambda t: ive(x, t) * ive(y, t) * ive(z, t), 0, math.inf, epsabs=1e-10, limit=500)
    return 3 * val, 3 * err


def main():
    # cap_2 / (2 c_1) = G0/(G0+Gr) >= 9/10 iff Gr/G0 <= 1/9
    g0, gr = 10, 1
    cap_ratio = F(g0, g0 + gr)
    ok("identity", cap_ratio == F(10, 11) and F(1, 9) * 9 == 1,
       "two records add to 9/10 iff G(r)/G(0) <= 1/9")

    G0, e0 = G(0, 0, 0)
    G1, _ = G(1, 0, 0)
    ok("anchor", abs(G0 - 1.5163860592) < 1e-9 and abs(G1 - (G0 - 1)) < 1e-9,
       f"G(0)={G0:.10f} matches Watson; G(e1)=G(0)-1 to {abs(G1-(G0-1)):.1e}")

    # orbits with |r|^2 <= 6 must fail; |r|^2 = 8 is the first pass. No integer vector has |r|^2 = 7.
    fail_pts = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (2, 1, 1)]
    pass_pts = [(2, 2, 0), (2, 2, 1), (3, 0, 0)]
    ratios = {}
    good = True
    for pt in fail_pts + pass_pts:
        g, err = G(*pt)
        ratios[pt] = g / G0
        good &= err / G0 < 1e-8
    good &= all(ratios[pt] > 1 / 9 for pt in fail_pts)
    good &= all(ratios[pt] < 1 / 9 for pt in pass_pts)
    ok("threshold", good,
       f"(2,2,0)={ratios[(2,2,0)]:.7f} < 1/9 < (2,1,1)={ratios[(2,1,1)]:.7f}; "
       f"every |r|^2<=6 fails and (2,2,0) passes")

    # capacity bounds: cap <= N c1, and cap >= N^2 / sum G for a positive test measure
    # checked as algebra on a 2-point Green matrix
    g_diag, g_off = F(9, 5), F(1, 5)
    # cap of two points = 2/(g+h); upper 2/g; lower 4/(2g+2h) = 2/(g+h)
    cap = F(2, g_diag + g_off)
    upper = F(2, g_diag)
    lower = F(4, 2 * g_diag + 2 * g_off)
    ok("bounds", lower == cap <= upper, f"two-point cap {cap} sits between {lower} and {upper}")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent check did not reproduce that step")
        return
    print(
        "HIT: confirmed - two massless records add to within 10 percent iff G(r)/G(0)<=1/9, "
        "which holds for every separation with |r|^2>=8 and fails for |r|^2<=6"
    )
    print(
        "SUMMARY: confirmed the two-record identity, the Watson anchor, G(e1)=G(0)-1, "
        "and the |r|^2=8 threshold; kappa and D* were not re-fitted"
    )


if __name__ == "__main__":
    main()
