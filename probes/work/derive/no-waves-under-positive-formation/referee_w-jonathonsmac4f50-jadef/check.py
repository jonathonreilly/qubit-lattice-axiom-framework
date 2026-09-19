#!/usr/bin/env python3
"""Referee of J:derive:no-waves-under-positive-formation:a1 (author w-macbookpro90c72-jf118, grok-4.6); referee
w-jonathonsmac4f50-jadef (claude-opus-5). Independent machinery (sympy, numpy roots), none of the author's code.

N1  step 1: lambda^2 - a lambda - (1 - a) = 0 has roots 1 and a - 1 = -b (discriminant (a - 2)^2)
N2  step 2: a = b = 1/2, phi = pi: lambda^2 - lambda/2 + 1/2 = 0, discriminant -7/4, |lambda|^2 = 1/2
N3  the general two-level positive statement, which steps 1-2 only instantiate: for z^2 = A z + B with |A| <= a, |B| <= b,
    a + b = 1, a, b > 0 (A, B positive character sums), every root has |z| <= 1 (if |z| > 1 then |z|^2 <= a|z| + b < |z|^2), and for
    the attempt's family A = a, B = b e^{i phi} equality |z| = 1 forces z = e^{i phi} = 1, i.e. phi = 0 (mod 2 pi); checked on a grid
    of 40 values of a and 360 phases by numerical roots
N4  step 3: 'lambda = e^{i c |k|}' is not the multiplier of any finite-range kernel: a finite-range multiplier is a trigonometric
    polynomial, smooth at k = 0, while e^{i c |k|} has one-sided derivatives +ic and -ic there
N5  the task's named exception keeps the records real: theta_{t+1} = 2 theta_t - theta_{t-1} + c^2 (Delta theta)_t (gain one, weight -1
    on the earlier level) has |z| = 1 exactly and arg z = c k + O(k^3); so unitary (complex) weights are not the weakest change that
    gives waves - dropping positivity alone does, with real records
"""
from __future__ import annotations

import sys

import sympy as sp


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    a, lam = sp.symbols("a lambda")
    roots = sp.solve(lam ** 2 - a * lam - (1 - a), lam)
    disc = sp.expand(a ** 2 + 4 * (1 - a))
    ok = set(sp.simplify(r) for r in roots) == {sp.Integer(1), a - 1} and sp.expand(disc - (a - 2) ** 2) == 0
    check("N1", ok, f"roots of lambda^2 - a lambda - (1 - a): {roots}; discriminant (a - 2)^2")

    p = lam ** 2 - lam / 2 + sp.Rational(1, 2)
    r2 = sp.solve(p, lam)
    ok = sp.discriminant(p, lam) == -sp.Rational(7, 4) and all(sp.simplify(sp.Abs(r) ** 2 - sp.Rational(1, 2)) == 0 for r in r2)
    check("N2", ok, "a = b = 1/2, phi = pi: discriminant -7/4 and |lambda|^2 = 1/2 for both roots")

    try:
        import numpy as np
        ok = True
        unimod = []
        for ia in range(1, 41):
            av = ia / 41
            bv = 1 - av
            for j in range(360):
                ph = 2 * np.pi * j / 360
                rts = np.roots([1, -av, -bv * np.exp(1j * ph)])
                mx = max(abs(rts))
                ok = ok and mx <= 1 + 1e-12
                if mx > 1 - 1e-9:
                    unimod.append(j)
        ok = ok and set(unimod) == {0}
    except Exception:
        ok = False
    check("N3", ok, "for 40 values of a in (0, 1) and 360 phases, every root of lambda^2 = a lambda + b e^{i phi} has |lambda| <= 1, with "
          "|lambda| = 1 only at phi = 0 (the root 1): the general statement is true (proof: |z| > 1 would give |z|^2 <= a|z| + b < |z|^2; "
          "equality forces z = e^{i phi} = 1), but steps 1-2 only instantiate it at two points")

    k, c = sp.symbols("k c", positive=True)
    f = lambda x: sp.exp(sp.I * c * sp.Abs(x))
    h = sp.symbols("h", positive=True)
    right = sp.limit((f(h) - f(0)) / h, h, 0, "+")          # derivative from the right
    left = sp.limit((f(0) - f(-h)) / h, h, 0, "+")          # derivative from the left
    ok = sp.simplify(right - sp.I * c) == 0 and sp.simplify(left + sp.I * c) == 0
    check("N4", ok, f"f(k) = e^(i c |k|) has right derivative {right} and left derivative {left} at k = 0: not differentiable, so not the "
          "multiplier of a finite-range (or first-moment) kernel, which is smooth; |e^{ik}| = 1 (step 3) exhibits no kernel with linear "
          "dispersion")

    z = sp.symbols("z")
    cc = sp.Rational(1, 2)
    b = 2 - 4 * cc ** 2 * sp.sin(k / 2) ** 2
    poly = z ** 2 - b * z + 1
    disc_ok = all(sp.simplify((b ** 2 - 4).subs(k, sp.pi * n / 12)) <= 0 for n in range(25))
    argz = sp.acos(b / 2)
    ser = sp.series(argz, k, 0, 4).removeO()
    wsum = (2 - 2 * cc ** 2) + 2 * cc ** 2 - 1
    ok = disc_ok and sp.Poly(poly, z).coeffs()[-1] == 1 and wsum == 1 and sp.simplify(ser - (k / 2 - sp.Rational(1, 64) * k ** 3)) == 0
    check("N5", ok, "the discrete wave equation (weights 2 - 2c^2, c^2, c^2 on level t and -1 on level t - 1, gain one, real records) has "
          "roots with product 1 and non-positive discriminant, so |z| = 1, and arg z = k/2 - k^3/64 + O(k^5) at c = 1/2: exact waves with "
          "real weights, dropping only positivity - a weaker change than unitary complex weights")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 3 - 'unitary phases are the weakest wave-producing drop of positivity' does not follow: step 3 shows only "
          "|e^{ik}| = 1, 'lambda = e^{i c |k|}' is not the multiplier of any finite-range kernel, and a single negative real weight on the "
          "earlier level (the discrete wave equation, real records) already gives exact waves with |z| = 1 and linear dispersion. Steps 1-2 "
          "hold as instances; the general positive two-level statement (spectral radius 1 only at the uniform mode) is true, with a two-line "
          "proof the attempt does not give, and is confirmed on a grid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
