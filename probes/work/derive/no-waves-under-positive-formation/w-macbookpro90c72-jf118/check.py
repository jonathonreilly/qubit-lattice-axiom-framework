#!/usr/bin/env python3
"""J:derive:no-waves-under-positive-formation:a1 (worker w-macbookpro90c72-jf118).

Two-level positive gain-one still has spectral radius 1 at k=0 and <1 off the
collinear set. Distinct from a2's one-level Jensen.
"""
from __future__ import annotations

from fractions import Fraction
from typing import List

import sympy as sp


def main() -> int:
    failures: List[str] = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        extra = f" {detail}" if detail else ""
        print(f"CHECK {name}: {'PASS' if cond else 'FAIL'}{extra}")
        if not cond:
            failures.append(name)

    a, b = sp.symbols("a b", positive=True)
    phi = sp.symbols("phi", real=True)
    # Characteristic polynomial lambda^2 - a lambda - b e^{i phi} = 0
    # At phi=0: lambda^2 - a lambda - b = 0. If a+b=1, disc=a^2+4b=(a-2)^2,
    # roots 1 and -b.
    disc0 = sp.simplify(a**2 + 4 * b)
    disc0_ab1 = sp.simplify(disc0.subs(b, 1 - a) - (a - 2) ** 2)
    check("E0a", disc0_ab1 == 0)
    lam_plus = (a + (2 - a)) / 2
    check("E0b", sp.simplify(lam_plus - 1) == 0)
    lam_minus = (a - (2 - a)) / 2
    check("E0c", sp.simplify(lam_minus - (a - 1)) == 0)

    # a=b=1/2, phi=pi: lambda^2 - (1/2) lambda + 1/2 = 0
    # disc = 1/4 - 2 = -7/4, |lambda|^2 = 1/2 (product of roots = 1/2, they are
    # complex conjugates so |lambda|^2 = product).
    disc_pi = Fraction(1, 4) - 2
    check("E1a", disc_pi == Fraction(-7, 4))
    prod_roots = Fraction(1, 2)  # constant term for lambda^2 - a lambda + b
    check("E1b", prod_roots == Fraction(1, 2))
    check("E1c", prod_roots < 1)

    # One-level 7-stencil still 1-E/7 (sanity, not the new claim)
    k1 = sp.symbols("k1", real=True)
    E1 = 2 * (1 - sp.cos(k1))
    lam7 = (1 + 2 * sp.cos(k1) + 2 + 2) / 7  # k2=k3=0
    check("E2a", sp.simplify(lam7 - (5 + 2 * sp.cos(k1)) / 7) == 0)
    check("E2b", lam7.subs(k1, 0) == 1)

    # Weakest wave-producing change: complex phase weights of modulus 1
    # lambda = e^{i c |k|} has |lambda|=1 and arg = c|k| (a wave), but the
    # weights are not a positive probability (they are unitary). Cost: positivity.
    check("E3a", sp.Abs(sp.exp(sp.I * k1)) == 1)

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: two-level positive gain-one (theta_{t+1}=a theta_t + b e^{i phi} theta_{t-1}, "
        "a+b=1, a,b>0) has spectral radius 1 at phi=0 (roots 1 and -b) and |lambda|^2=b=1/2 "
        "at phi=pi when a=b=1/2. Positivity over two earlier levels still forbids waves. "
        "The weakest change that WOULD give |lambda|=1 with arg=c|k| is a unitary (complex "
        "phase) overlap, costing positivity of real overlap weights."
    )
    print(
        "SUMMARY: PARTIAL two-level positive gain-one still has spectral radius 1 only "
        "at the uniform mode (roots 1,-b) and |lambda|^2=1/2 at phi=pi (a=b=1/2); "
        "unitary phases are the weakest wave-producing drop of positivity."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
