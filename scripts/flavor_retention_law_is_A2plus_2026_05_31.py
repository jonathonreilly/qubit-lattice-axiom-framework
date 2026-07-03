#!/usr/bin/env python3
"""Finite supplied-onsite algebra for the flavor retention-law boundary."""

from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


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
    passed.append(
        check(
            "R1 C3-invariant onsite diagonal sources are scalar",
            bool(c3_forced)
            and c3_forced[0].get(a) == c
            and c3_forced[0].get(b) == c,
            f"solve -> {c3_forced[0] if c3_forced else None}",
        )
    )
    passed.append(
        check(
            "R2 supplied Q(z) coordinates give Q(0)=2/3 and Q(-1/3)=1",
            q(0) == sp.Rational(2, 3) and q(sp.Rational(-1, 3)) == 1,
            f"Q(0)={q(0)}, Q(-1/3)={q(sp.Rational(-1, 3))}",
        )
    )

    z_op = 2 * (np.ones((3, 3)) / 3.0) - i3
    s_q1 = i3 - z_op / 3.0
    passed.append(
        check(
            "R3 Z=2P_+-I and S_Q1=I-Z/3 have the displayed d=3 coefficients",
            np.allclose(z_op @ z_op, i3)
            and abs(s_q1[0, 0] - 10 / 9) < 1e-9
            and abs(s_q1[0, 1] + 2 / 9) < 1e-9,
            "diag(S_Q1)=10/9 and offdiag(S_Q1)=-2/9",
        )
    )

    x, y, z = sp.symbols("x y z")
    diag_xyz = sp.diag(x, y, z)
    intersection = sp.solve(list(c3 * diag_xyz - diag_xyz * c3), [x, y], dict=True)
    passed.append(
        check(
            "R4 onsite diagonal algebra intersects the C3 circulant algebra only in scalars",
            bool(intersection)
            and intersection[0].get(x) == z
            and intersection[0].get(y) == z,
            f"solve -> {intersection[0] if intersection else None}",
        )
    )

    h = i3 + 0.6 * c_np + 0.6 * c_np.T
    offdiag = h - np.diag(np.diag(h))
    h_onsite = np.diag(np.diag(h))
    passed.append(
        check(
            "R5 diagonal onsite descent erases sample off-diagonal circulant splitting",
            np.any(np.abs(offdiag) > 1e-12)
            and np.allclose(h_onsite, h_onsite[0, 0] * i3),
            f"descent={h_onsite[0, 0]:.1f}*I",
        )
    )

    source = (ROOT / "docs/FLAVOR_RETENTION_LAW_IS_A2PLUS_NOTE_2026-05-31.md").read_text()
    guard_ok = (
        "not physical mass\n   predictions" in source
        and "does not select onsite\nsources as the physical readout surface" in source
        and "not a\nframework-native charged-lepton value" in source
        and "does not add a new axiom" in source
    )
    passed.append(
        check(
            "R6 source guards keep Q values as supplied coordinates and source-locality open",
            guard_ok,
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("VERDICT: bounded support for finite supplied-onsite algebra only.")
    print("Q(0)=2/3 is a coordinate value of the supplied Q(z) formula, not a")
    print("framework-native charged-lepton value. The physical source-locality/")
    print("readout bridge remains open.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
