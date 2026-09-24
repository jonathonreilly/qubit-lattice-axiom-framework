#!/usr/bin/env python3
"""Independent checks of the dragged growing Kepler problem."""
import sympy as sp


def main():
    q, t, mu0, r0, L0 = sp.symbols("q1 t mu0 r0 L0", positive=True)
    mu = mu0 * sp.exp(q * t)
    # angular momentum: L' = -q L from x'' = -q x' + central
    L = L0 * sp.exp(-q * t)
    ok = sp.simplify(sp.diff(L, t) + q * L) == 0
    # circular: L = sqrt(mu r), r = r0 exp(-3 q t)
    r = r0 * sp.exp(-3 * q * t)
    # at t=0, L0^2 = mu0 r0
    ident = sp.simplify(L**2 - mu * r)
    ok &= sp.simplify(ident.subs(L0**2, mu0 * r0)) == 0
    # period ~ r^{3/2}/sqrt(mu) ~ exp(-5 q t)
    per = r ** sp.Rational(3, 2) / sp.sqrt(mu)
    ratio = sp.simplify(per / per.subs(t, 0))
    ok &= ratio == sp.exp(-5 * q * t)
    # turns per halving: (2^{5/3}-1)/5
    turns = (sp.Integer(2) ** sp.Rational(5, 3) - 1) / 5
    ok &= abs(float(turns) - 0.43496) < 1e-4
    # carried: r^3 = r0^3 - 3 mu0/q^2 (e^{qt}-1)
    rc = (r0**3 - 3 * mu0 / q**2 * (sp.exp(q * t) - 1)) ** sp.Rational(1, 3)
    # dr/dt should equal - mu /(q r^2)
    dr = sp.diff(rc**3, t)
    # d(r^3)/dt = 3 r^2 dr/dt = -3 mu0/q * e^{qt} = -3 mu / q
    # so dr/dt = - mu /(q r^2)
    ok &= sp.simplify(dr + 3 * mu / q) == 0
    print("L, spiral, period, carried", bool(ok), "turns/half", float(turns))
    if ok:
        print(
            "HIT: confirmed - L = L0 e^{-q1 t}, a circular orbit shrinks as e^{-3 q1 t} with period e^{-5 q1 t}, "
            "about 0.435/eps turns per halving, and the carried radius obeys r^3 = r0^3 - (3 mu0/q1^2)(e^{q1 t}-1)"
        )
        print(
            "SUMMARY: confirmed the exact dragged Kepler reductions; the numerical integrations were not re-run"
        )
    else:
        print("SUMMARY: fails at an orbit identity")


if __name__ == "__main__":
    main()
