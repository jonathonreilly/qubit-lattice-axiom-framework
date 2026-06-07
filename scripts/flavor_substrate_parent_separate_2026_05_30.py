#!/usr/bin/env python3
"""Finite tensor/parity boundary for the flavor substrate-parent route."""

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
    I3 = np.eye(3)
    J = np.ones((3, 3))
    Gchi = (2 / 3) * J - I3
    G_U1 = (C - C.T) / np.sqrt(3)
    h = np.array([1, -1, 0.0])
    H_chi = (np.outer(h, np.ones(3)) + np.outer(np.ones(3), h)) / 3
    sx = np.array([[0, 1], [1, 0]], float)
    I2 = np.eye(2)
    G6 = np.kron(I2, Gchi)
    K = np.kron(I2, G_U1) + np.kron(sx, H_chi)

    passed = []
    even = (K + G6 @ K @ G6) / 2
    odd = (K - G6 @ K @ G6) / 2
    passed.append(
        check(
            "D1 coin-blind grading forces K into even value slot plus odd chiral slot",
            np.allclose(even, np.kron(I2, G_U1)) and np.allclose(odd, np.kron(sx, H_chi)),
        )
    )
    passed.append(
        check(
            "D2 value side commutes with Gamma_chi and C; chiral side anticommutes with Gamma_chi",
            np.allclose(G_U1 @ Gchi - Gchi @ G_U1, 0)
            and np.allclose(G_U1 @ C - C @ G_U1, 0)
            and np.linalg.norm(H_chi @ Gchi + Gchi @ H_chi) < 1e-9
            and np.linalg.norm(H_chi @ C - C @ H_chi) > 1e-6,
        )
    )

    omega = np.exp(2j * np.pi / 3)
    d = np.diag([1, omega])
    order3 = np.allclose(np.linalg.matrix_power(d, 3), np.eye(2)) and not np.allclose(
        d @ d, np.eye(2)
    )
    passed.append(
        check(
            "D3 diag(1,omega) has order 3 and determinant omega",
            order3 and abs(np.linalg.det(d) - omega) < 1e-9,
        )
    )

    z2_candidates = [np.eye(2), -np.eye(2), np.diag([1, -1]), np.diag([-1, 1])]
    passed.append(
        check(
            "D4 diag(1,omega) is not one of the supplied Z2 spin-factor charges",
            all(not np.allclose(d, z) for z in z2_candidates),
        )
    )

    source = (ROOT / "docs/FLAVOR_SUBSTRATE_PARENT_SEPARATE_NOTE_2026-05-30.md").read_text()
    passed.append(
        check(
            "D5 source guard: native/non-native status and only-way theorem are left open",
            "does not prove an \"only way\" folding theorem" in source
            and "does not decide whether `diag(1,omega)` is native" in source
            and "It does not classify\nall possible" in source,
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("VERDICT: on the supplied Z2 spin-factor reading, the naive lift splits")
    print("into separate value and chirality slots. Unification on this route")
    print("requires an order-3 complex charge diag(1,omega), but this runner does")
    print("not decide that charge's native status in full complex M2(C).")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
