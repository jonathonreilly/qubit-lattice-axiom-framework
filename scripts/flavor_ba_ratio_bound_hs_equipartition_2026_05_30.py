#!/usr/bin/env python3
"""Finite checks for the corner-coupling positivity bound, HS characterization,
and spectral Koide readout derivation."""

from __future__ import annotations

import numpy as np
import sympy as sp


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main() -> int:
    I = np.eye(3)
    J = np.ones((3, 3))
    B = J - I
    passed = []

    a, b = 1.7, 0.3
    eig = np.linalg.eigvalsh(a * I + b * B)
    expected = np.sort([a + 2 * b, a - b, a - b])
    passed.append(check("eigenvalues are a+2b and a-b doublet",
                        np.allclose(np.sort(eig), expected),
                        f"eig={np.sort(eig)}, expected={expected}"))

    ratios = np.linspace(-0.75, 1.25, 41)
    ok_bound = True
    for r in ratios:
        vals = np.array([1 + 2 * r, 1 - r, 1 - r])
        psd = bool(np.all(vals >= -1e-12))
        ok_bound &= (psd == (-0.5 <= r <= 1.0))
    passed.append(check("PSD with a>0 iff -1/2 <= b/a <= 1", ok_bound))

    tr_i = float(np.trace(I @ I))
    tr_b = float(np.trace(B @ B))
    ratio = (tr_i / tr_b) ** 0.5
    ok_hs = abs(tr_i - 3.0) < 1e-12 and abs(tr_b - 6.0) < 1e-12
    ok_hs &= abs(ratio - 2 ** -0.5) < 1e-12
    passed.append(check("HS equipartition gives b/a=1/sqrt(2)", ok_hs,
                        f"Tr(I^2)={tr_i}, Tr((J-I)^2)={tr_b}, ratio={ratio}"))

    aa, bb = sp.symbols("a b", nonzero=True)
    singlet = aa + 2 * bb
    doublet = aa - bb
    spectral_q = sp.factor((singlet ** 2 + 2 * doublet ** 2) / (singlet + 2 * doublet) ** 2)
    displayed_q = sp.Rational(1, 3) + sp.Rational(2, 3) * (bb / aa) ** 2
    passed.append(check(
        "symmetric-form spectral Koide readout derives Q=1/3+(2/3)(b/a)^2",
        sp.simplify(spectral_q - displayed_q) == 0,
        f"Q_spectral={spectral_q}",
    ))

    var_ratio = (1.0 / tr_b) / (1.0 / tr_i)
    q_equipartition = float(displayed_q.subs({bb / aa: 2 ** -0.5}))
    ok_q = abs(var_ratio - 0.5) < 1e-12
    ok_q &= abs(q_equipartition - 2.0 / 3.0) < 1e-12
    passed.append(check("formal HS Gaussian variance ratio gives Q=2/3", ok_q,
                        f"<b^2>/<a^2>={var_ratio}, Q={q_equipartition}"))

    print(f"SCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
