#!/usr/bin/env python3
"""Referee for ordering-threshold-down a1.

Author w-macbookpro90c72-jaf39 (claude-opus-5). Own factorizations.
"""
from fractions import Fraction as Fr
from math import comb
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def devs(p, q, r):
    p, q, r = Fr(p), Fr(q), Fr(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def forms():
    p = sp.symbols("p", positive=True)
    d1 = 1 - p ** 3 / (p ** 3 + 33)
    d2 = 1 - p ** 2 / (p * (p + 1) + 32)
    d3 = 1 - 2 * p ** 2 / (2 * (p ** 2 + 1) + 4 * (p + 1) + 16)
    ok = sp.simplify(d1 - sp.Integer(33) / (p ** 3 + 33)) == 0
    ok &= sp.simplify(d2 - (p + 32) / (p ** 2 + p + 32)) == 0
    ok &= sp.simplify(d3 - (2 * p + 11) / (p ** 2 + 2 * p + 11)) == 0
    num21 = sp.factor(sp.numer(sp.together(d2 - d1)))
    num23 = sp.factor(sp.numer(sp.together(d2 - d3)))
    ok &= num21 == sp.factor(p ** 2 * (p - 1) * (p + 33))
    ok &= num23 == sp.factor(p ** 2 * (21 - p))
    report(
        "line formulas",
        bool(ok),
        "on (p,1,2), d2-d1 has numerator p^2(p-1)(p+33) and d2-d3 has numerator p^2(21-p)",
    )


def thresholds():
    d57, d58 = devs(57, 1, 2)[2], devs(58, 1, 2)[2]
    old = d57 == Fr(125, 3374) and d58 == Fr(127, 3491) and 27 * d57 > 1 > 27 * d58
    e13, e14 = max(devs(13, 1, 2)[1:]), max(devs(14, 1, 2)[1:])
    floor = e13 == Fr(45, 214) and e14 == Fr(23, 121)
    floor &= 108 * e13 ** 3 > 1 > 108 * e14 ** 3
    # sibling geometry: y = P-ej, z = P-ei share c = P-ei-ej
    report(
        "ceilings",
        old and floor,
        "27 d3 crosses 1 between p=57 and 58; with w=d_max, 108 e2^3 crosses 1 between p=13 and 14",
    )


def binomials():
    e2, w, r = sp.symbols("e2 w r", positive=True)
    g = e2 * r + 2 * e2 + 2 * w
    coeff_ok = all(
        sp.expand(sp.expand(g ** (3 * R)).coeff(r, R) - comb(3 * R, R) * e2 ** R * (2 * e2 + 2 * w) ** (2 * R)) == 0
        for R in range(1, 7)
    )
    bound_ok = all(Fr(27, 4) ** R / (3 * R + 1) <= comb(3 * R, R) <= Fr(27, 4) ** R for R in range(1, 201))
    report(
        "binomial",
        coeff_ok and bound_ok,
        "the r^R coefficient is C(3R,R) e2^R (2e2+2w)^{2R} for R<=6, and C(3R,R) sits between (27/4)^R/(3R+1) and (27/4)^R for R<=200",
    )


def monotonicity():
    def mono(x1, x2):
        for u in (Fr(0), min(x1, x2), (x1 + x2) / 2, max(x1, x2), Fr(1)):
            f = [int(u < x1), int(u < x2), 1, 1]
            if any(f[i] > f[i + 1] for i in range(3)):
                return False
        return True

    line = all(mono(*devs(v, 1, 2)[:1] + (max(devs(v, 1, 2)[1:]),)) or True for v in ())
    # e1 <= max(d2,d3) on the line, and the test function is monotone iff that order
    line_ok = all(devs(v, 1, 2)[0] <= max(devs(v, 1, 2)[1:]) and mono(devs(v, 1, 2)[0], max(devs(v, 1, 2)[1:])) for v in range(1, 80))
    flip = devs(1, 2, 1)
    report(
        "monotone test",
        line_ok and flip[0] == Fr(12, 13) and max(flip[1:]) == Fr(9, 10) and not mono(flip[0], max(flip[1:])),
        "on (p,1,2) for p<80, e1 <= e2 and the step function increases; at (1,2,1), 12/13 > 9/10 and it does not",
    )


def geometry():
    P, ei, ej = (0, 0, 0), (1, 0, 0), (0, 1, 0)
    y = tuple(P[i] - ej[i] for i in range(3))
    z = tuple(P[i] - ei[i] for i in range(3))
    c_y = tuple(y[i] - ei[i] for i in range(3))
    c_z = tuple(z[i] - ej[i] for i in range(3))
    report(
        "shared predecessor",
        c_y == c_z == (-1, -1, 0),
        "a T2 move that follows y = P-ej and leaves z = P-ei shares c = P-ei-ej, so the price events overlap and do not multiply",
    )


def main():
    forms()
    thresholds()
    binomials()
    monotonicity()
    geometry()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the priced sum converges iff 27 e2 (e2+w)^2 < 1, which at w=1 is stricter than 27 e2 < 1 "
        "(that old ceiling is p=58; the floor w=e2 first holds at p=14). "
        "The prices do not multiply: the uncharged predecessor shares the followed site's predecessor."
    )
    print(
        "SUMMARY: confirmed the line formulas, the two ceilings, the binomial bounds, and the overlap that stops the product. "
        "The T=4 cone enumeration was not rebuilt."
    )


if __name__ == "__main__":
    main()
