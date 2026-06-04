#!/usr/bin/env python3
"""Finite conditional algebra for the flavor retention-law scope repair.

The runner deliberately removes the old hard-coded R1 assertion that A2 is
structure-locality only and that source-locality is independent. It checks only
the executable algebra that remains in the packet:

* C3 invariance forces an onsite diagonal source to be scalar;
* the supplied Q(z) values give Q(0)=2/3 and Q(-1/3)=1;
* the displayed Z/S_Q1 coefficients match the finite matrices;
* diagonal onsite operators intersect the circulant algebra only in scalars,
  while diagonal compression discards a sample off-diagonal circulant mass
  splitting.

No A2-to-source-locality bridge is claimed by this runner.
"""

import numpy as np
import sympy as sp


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    i3 = np.eye(3)
    c_np = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)
    passed = []

    a, b, c = sp.symbols("a b c")
    c3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    d = sp.diag(a, b, c)
    c3_forced = sp.solve(list(c3 * d * c3.inv() - d), [a, b], dict=True)
    q = lambda z: sp.Rational(2, 3) / (1 + z)
    passed.append(check(
        "R2a C3-invariant onsite diagonal sources are scalar; supplied Q gives Q(0)=2/3 and Q(-1/3)=1",
        bool(c3_forced) and c3_forced[0].get(a) == c and c3_forced[0].get(b) == c
        and q(0) == sp.Rational(2, 3) and q(sp.Rational(-1, 3)) == 1,
        f"solve -> {c3_forced[0] if c3_forced else None}; Q(0)={q(0)}, Q(-1/3)={q(sp.Rational(-1, 3))}",
    ))

    z_op = 2 * (np.ones((3, 3)) / 3.0) - i3
    s_q1 = i3 - z_op / 3.0
    passed.append(check(
        "R2b Z=2P_+-I and S_Q1=I-Z/3 have the displayed d=3 coefficients",
        np.allclose(z_op @ z_op, i3)
        and abs(s_q1[0, 0] - 10 / 9) < 1e-9
        and abs(s_q1[0, 1] + 2 / 9) < 1e-9,
        "diag(S_Q1)=10/9 and offdiag(S_Q1)=-2/9=-2/d^2",
    ))

    x, y, z = sp.symbols("x y z")
    diag_xyz = sp.diag(x, y, z)
    intersection = sp.solve(list(c3 * diag_xyz - diag_xyz * c3), [x, y], dict=True)
    passed.append(check(
        "R3a onsite diagonal algebra intersects the C3 circulant algebra only in scalars",
        bool(intersection) and intersection[0].get(x) == z and intersection[0].get(y) == z,
        f"D intersect circulant solve -> {intersection[0] if intersection else None}",
    ))

    h = i3 + 0.6 * c_np + 0.6 * c_np.T
    offdiag = h - np.diag(np.diag(h))
    h_onsite = np.diag(np.diag(h))
    offdiag_values = sorted(float(v) for v in set(np.round(offdiag[~np.eye(3, dtype=bool)], 3)))
    passed.append(check(
        "R3b sample circulant mass splitting is off-diagonal and onsite descent erases it to a scalar",
        np.any(np.abs(offdiag) > 1e-12) and np.allclose(h_onsite, h_onsite[0, 0] * i3),
        f"offdiag entries include {offdiag_values}; descent={h_onsite[0,0]:.1f}*I",
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: BOUNDED-SUPPORT finite conditional algebra only. If an extra source-locality/readout")
    print("premise selects onsite diagonal sources, the displayed algebra gives Q=2/3; the projected")
    print("z=-1/3 domain gives Q=1. The runner does not prove A2-to-source-locality and does not claim")
    print("that the missing source-locality bridge is accepted.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
