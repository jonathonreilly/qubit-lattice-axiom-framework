#!/usr/bin/env python3
"""Source-only spectral reflection and full-affine counterexample.

The legacy filename is retained. The former universal microscopic selector
impossibility claim is withdrawn: source-only sign blindness neither extends
to H_base+H_src nor rules out a selected magnitude or a unique point on d>=0.
"""
from __future__ import annotations

import numpy as np
import sympy as sp
from frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary import (
    h_base, tm, tdelta, tq,
)


def main() -> int:
    passed = failed = 0

    def check(name: str, condition: bool) -> None:
        nonlocal passed, failed
        passed += bool(condition)
        failed += not bool(condition)
        print(f"[{'PASS' if condition else 'FAIL'}] {name}")

    # Exact entries independently specified, then compared with production helpers.
    M = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    D = sp.Matrix([[0, -1, 1], [-1, 1, 0], [1, 0, -1]])
    Q = sp.ones(3) - sp.eye(3)
    R = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    for name, exact, helper in [("T_m", M, tm), ("T_delta", D, tdelta), ("T_q", Q, tq)]:
        check(f"{name} matches supplied chart", np.allclose(np.array(exact).astype(complex), helper()))
    check("R is an orthogonal involution", R.T * R == sp.eye(3) and R * R == sp.eye(3))
    check("R fixes T_m and T_q", R*M*R.T == M and R*Q*R.T == Q)
    check("R reverses T_delta", R*D*R.T == -D)
    m, d, q = sp.symbols("m d q", real=True)
    S = m*M + d*D + q*Q
    check("Exact source-only similarity for all m,d,q", R*S*R.T == S.subs(d, -d))
    check("Source quadratic identity", sp.expand(sp.trace(S**2) - (3*m*m+6*d*d+6*q*q+4*m*q)) == 0)
    check("Source determinant is even", sp.expand(S.det()-S.subs(d,-d).det()) == 0)
    # All spectral functions inherit similarity; no finite random sample is the proof.
    B = sp.Matrix([[0, sp.sqrt(sp.Rational(8,3)), -sp.sqrt(sp.Rational(8,3))-sp.I/2],
                   [sp.sqrt(sp.Rational(8,3)), 0, -sp.sqrt(8)/3],
                   [-sp.sqrt(sp.Rational(8,3))+sp.I/2, -sp.sqrt(8)/3, 0]])
    check("Exact H_base matches chart", np.allclose(np.array(B).astype(complex), h_base()))
    H = B + S
    difference = sp.simplify(sp.trace(H**2)-sp.trace(H.subs(d,-d)**2))
    check("Full-affine trace-square counterexample", sp.simplify(difference+32*sp.sqrt(6)*d/3) == 0 and difference != 0)
    print(f"tr(H(d)^2)-tr(H(-d)^2) = {difference}")
    # A cyclic doublet alone permits odd cubic invariant contractions.
    x, y = sp.symbols("x y", real=True)
    cubic = x**3 - 3*x*y**2
    xr, yr = -x/2-sp.sqrt(3)*y/2, sp.sqrt(3)*x/2-y/2
    check("Z3 permits cubic doublet invariants", sp.simplify(xr**3-3*xr*yr**2-cubic) == 0)
    check("Such a cubic can be odd on a fixed line", cubic.subs(y,0) == x**3)
    print("Similarity proves source-only spectral sign blindness, not selector impossibility.")
    print("No chiral Ward, global gauge equivalence, or physical source-selection claim is tested.")
    print(f"TOTAL: PASS = {passed}, FAIL = {failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
