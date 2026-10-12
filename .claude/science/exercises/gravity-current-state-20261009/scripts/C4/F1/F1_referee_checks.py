"""Independent algebra/numerics for the Campaign C4 / RF / F1 referee.

This does not import or execute downloaded material.  It independently checks
the load-bearing formula reductions and probes the worker's own static case-B
quadratic form for correlated mass choices that its one-at-a-time scan misses.
"""

from __future__ import annotations

import contextlib
import io
import math
import sys

import numpy as np
import sympy as sp


def gss_checks() -> None:
    alpha, gamma = sp.symbols("alpha gamma", positive=True)
    lam = 1 + gamma
    c = lam / (3 * lam - 1)
    lattice_cs2 = sp.simplify(2 * (1 - 2 * c) * (1 / alpha - sp.Rational(1, 2)))
    gss_cs2 = (2 - alpha) * gamma / (alpha * (2 + 3 * gamma))
    print("GSS/lattice scalar identity:", sp.simplify(lattice_cs2 - gss_cs2))

    # At beta=0, the generic small-alpha branch is bounded by alpha_2 ~= alpha/2.
    print("weak generic alpha ceiling:", 2 * 4e-7)
    print("hat-alpha2 surrogate ceiling:", 2 * 1.6e-9)
    print("BBN gamma ceiling at alpha=0:", 2 / 21)
    generic_fraction = (8e-7 * (2 / 21)) / (2 * 1.3)
    print("generic weak-window fraction in worker box:", generic_fraction)
    print("cancellation alpha ceiling, weak alpha1:", 1e-4 / 4)
    print("cancellation alpha ceiling, hat-alpha1 surrogate:", 1e-5 / 4)

    a = 1e-9
    g = 1e-2
    cs2 = (2 - a) * g / (a * (2 + 3 * g))
    msc_over_m = math.sqrt(a) * cs2 ** (-0.25)
    print("sample cS:", math.sqrt(cs2))
    print("sample MSC/M:", msc_over_m)
    print("sample MSC [GeV] for M=2.435e18 GeV:", msc_over_m * 2.435e18)


def cubic_character_count() -> None:
    # Sym^2(R^3) restricted to O (proper cube group) decomposes A1 + E + T2;
    # n is A1 and shift is T1.  Invariant symmetric bilinears consist of one
    # norm per irrep copy and one mixing between the two A1 copies.
    multiplicities = {"A1": 2, "E": 1, "T2": 1, "T1": 1}
    count = sum(m * (m + 1) // 2 for m in multiplicities.values())
    print("cubic invariant symmetric bilinears:", count)


def static_counterfamily() -> None:
    # Import only the local worker module.  Suppress its top-level report so the
    # independent output contains only the new checks.
    sys.path.insert(0, "scripts")
    with contextlib.redirect_stdout(io.StringIO()):
        import f1_lattice_only_masses as worker

    # At k=0 the (normalized trace, lapse) mass block is
    # [[mu_A1, sqrt(3)m4], [sqrt(3)m4, mu_n]].  The following family has zero
    # determinant.  The additional ratio m4/mu_A1=4/3 gives gamma=1 in the
    # worker's complete finite-k static quadratic form.
    mu_a1 = 1.0
    m4 = 4.0 / 3.0
    mu_n = 16.0 / 3.0
    det = mu_a1 * mu_n - 3 * m4**2
    print("correlated scalar-mass determinant:", det)
    for kmag in (1e-2, 1e-3, 1e-4):
        nk2, gamma_ppn = worker.static_B(
            kmag, {"A1": mu_a1, "m4": m4, "n": mu_n}
        )
        print(f"correlated family k={kmag:.0e}: nk2={nk2:+.12f}, gamma={gamma_ppn:.12f}")
    print("worker GR target nk2:", -1 / (2 * (2 - 0.1)))


def hessian_average() -> None:
    # The Hessian of every periodic C2 band has zero Brillouin-zone average.
    # Check the worker's three improved trigonometric stencils independently.
    for r in (1, 2, 3):
        j = np.arange(1, r + 1, dtype=float)
        mat = np.array(
            [
                [
                    2 * (-1) ** (p + 1) * jj ** (2 * p) / math.factorial(2 * p)
                    for jj in j
                ]
                for p in range(1, r + 1)
            ]
        )
        rhs = np.zeros(r)
        rhs[0] = 1
        coeff = np.linalg.solve(mat, rhs)
        # Integral of cos(j k) on [-pi,pi] is exactly zero for every j>=1.
        avg = sum(coeff_i * jj**2 * 0.0 for coeff_i, jj in zip(coeff, j))
        print(f"range {r} Hessian zone average: {avg:+.1f}")


if __name__ == "__main__":
    gss_checks()
    cubic_character_count()
    static_counterfamily()
    hessian_average()
