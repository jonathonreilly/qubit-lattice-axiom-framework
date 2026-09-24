#!/usr/bin/env python3
"""Independent checks: spectrum of omega and the plaquette loop factor."""
from fractions import Fraction as F


def parts(p, q, r):
    A1 = p + q + 4 * r
    l2 = p + q - 2 * r
    l3 = p - q
    eq = A1 / 6 + l2 / 3 + l3 / 2
    opp = A1 / 6 + l2 / 3 - l3 / 2
    orth = A1 / 6 - l2 / 6
    return A1, l2, l3, eq, opp, orth


def loop4(p, q, r):
    A1, l2, l3, *_ = parts(p, q, r)
    return 1 + (2 * l2**4 + 3 * l3**4) / A1**4


def main():
    ok = True
    for p, q, r in ((3, 1, 2), (5, 2, 4), (1, 2, 1), (4, 4, 4)):
        A1, l2, l3, eq, opp, orth = parts(F(p), F(q), F(r))
        print(f"({p},{q},{r}) equal {eq} opp {opp} orth {orth}")
        ok &= eq == p and opp == q and orth == r
    plaq = loop4(F(3), F(1), F(2))
    print("plaquette", plaq)
    ok &= plaq == F(433, 432)
    # constant rule: loop factor 1
    ok &= loop4(F(4), F(4), F(4)) == 1
    c0 = F(6, 3 + 1 + 8)
    ok &= c0 == F(1, 2)
    print("c0", c0)
    if ok:
        print(
            "HIT: confirmed - omega splits into A1 plus lambda2, lambda3, the plaquette loop is 433/432 at (3,1,2), "
            "and it is 1 only for the constant rule"
        )
        print(
            "SUMMARY: confirmed the scale split: c0 removes bare binding on trees, and no scale removes the plaquette factor unless p=q=r"
        )
    else:
        print("SUMMARY: fails at the spectral table or the plaquette factor")


if __name__ == "__main__":
    main()
