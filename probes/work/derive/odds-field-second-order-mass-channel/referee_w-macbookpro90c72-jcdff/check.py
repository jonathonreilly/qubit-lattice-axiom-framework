#!/usr/bin/env python3
"""Independent algebra for the second-order odds potential."""
from fractions import Fraction as F
import math


def axis_const(l1):
    # 2 cosh k + 4 = 1/l1, decay along one axis
    # cosh 2k = 2 cosh^2 k - 1
    c = (1 / l1 - 4) / 2
    c2 = 2 * c * c - 1
    s = c2 + 2  # two transverse cosh 0 = 1
    return F(3, 2) * (1 - 2 * l1 * l1 * s)


def diag_const(l1):
    c = (1 / l1) / 6
    c2 = 2 * c * c - 1
    return F(3, 2) * (1 - 2 * l1 * l1 * 3 * c2)


def main():
    # massless surface (3,1,2)
    T = 3 + 1 + 4 * 2
    l1 = F(3 - 1, T)
    l2 = F(3 + 1 - 4, T)
    near = F(3, 2) * (1 - 6 * l1 * l1)
    ok = l2 == 0 and near == F(5, 4) and l1 == F(1, 6)
    g0 = 0.2527310
    pref = (5 / 4) / (4 * math.pi * g0) ** 2
    ok &= abs(pref - 0.1239) < 2e-4
    print(f"massless l1={l1} const={near} 0.1239 vs {pref:.5f}")

    # (5,2,4)
    T2 = 5 + 2 + 4 * 4
    l1b = F(5 - 2, T2)
    ax = axis_const(l1b)
    dg = diag_const(l1b)
    print(f"(5,2,4) axis {float(ax):.4f} diag {float(dg):.4f} a1 45 l1^2 {float(45*l1b*l1b):.4f}")
    ok &= abs(float(ax) - 1.106) < 0.001 and abs(float(dg) - 1.153) < 0.001

    # closed form: l1^2 * sum_{y<y'} u u' = (1/2)(u^2 - l1^2 sum u_y^2)
    # if sum u_y = u/l1
    uys = [F(1), F(2), F(3), F(4), F(5), F(6)]
    sm = sum(uys)
    u = l1 * sm  # identity
    pair = F(0)
    for i, a in enumerate(uys):
        for b in uys[i + 1 :]:
            pair += a * b
    left = l1 * l1 * pair
    right = F(1, 2) * (u * u - l1 * l1 * sum(a * a for a in uys))
    ok &= left == right
    wa = (F(2, 3), F(-1, 3), F(-1, 3))
    ok &= sum(a * a for a in wa) == F(2, 3)
    print("closed form", left == right, "|w|^2", sum(a * a for a in wa))
    if ok:
        print(
            "HIT: confirmed - on (3,1,2) the far constant is 5/4 and the 1/r^2 coefficient is 0.1239; "
            "at (5,2,4) the axis and diagonal constants are 1.106 and 1.153, not 45 l1^2"
        )
        print(
            "SUMMARY: confirmed the second-order potential's far constants and the neighbour-sum identity; "
            "the 5^3 rational field census was not rebuilt"
        )
    else:
        print("SUMMARY: fails at a far-constant identity")


if __name__ == "__main__":
    main()
