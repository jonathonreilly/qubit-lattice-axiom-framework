#!/usr/bin/env python3
"""Independent algebra for the light-cone 7-stencil kernel."""
import sympy as sp


def main():
    c1, c2, c3 = sp.symbols("c1 c2 c3", real=True)
    E = 2 * (1 - c1) + 2 * (1 - c2) + 2 * (1 - c3)
    phi = (1 + 2 * (c1 + c2 + c3)) / 7
    ok = sp.simplify(phi - (1 - E / 7)) == 0
    chi = sp.simplify(1 / (1 - phi))
    ok &= sp.simplify(chi - 7 / E) == 0
    C_over = sp.simplify(1 / (1 - phi**2))
    alt = sp.simplify(sp.Rational(7, 2) * (1 / E + 1 / (14 - E)))
    ok &= sp.simplify(C_over - alt) == 0
    ratio = sp.simplify(C_over / (7 / E))
    ok &= sp.simplify(ratio - 7 / (14 - E)) == 0
    longwave = sp.limit(ratio, c1, 1)
    longwave = sp.simplify(longwave.subs({c2: 1, c3: 1}))
    ok &= longwave == sp.Rational(1, 2)
    # corner cos = -1, E=12
    corner = sp.simplify(ratio.subs({c1: -1, c2: -1, c3: -1}))
    ok &= corner == sp.Rational(7, 2)
    # geometric remainder
    R = sp.symbols("R", integer=True, nonnegative=True)
    tail = sp.summation((sp.Rational(1, 14)) * (sp.Rational(6, 7)) ** sp.symbols("n"), (sp.symbols("n"), R, sp.oo))
    ok &= sp.simplify(tail - sp.Rational(1, 2) * (sp.Rational(6, 7)) ** R) == 0
    print("identities", bool(ok), "corner", corner)
    if ok:
        print(
            "HIT: confirmed - phi = 1-E/7, chi = 7/E, C/sigma^2 = (7/2)(1/E+1/(14-E)), "
            "and the ratio is 7/(14-E), equal to 1/2 at long wavelength and 7/2 at the zone corner"
        )
        print(
            "SUMMARY: confirmed the light-cone kernel algebra and the exponential remainder bound; "
            "the numerical roots of A(7 beta)=beta and =2 beta were not recomputed"
        )
    else:
        print("SUMMARY: fails at a kernel identity")


if __name__ == "__main__":
    main()
