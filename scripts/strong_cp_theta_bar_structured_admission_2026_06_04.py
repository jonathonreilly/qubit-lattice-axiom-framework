#!/usr/bin/env python3
"""Finite checks for the Strong-CP theta_bar structured open gate.

The runner verifies form-degree, O_h pseudoscalar, K-real circulant, chiral
basis-shift, and AC_phi_lambda overlap facts. It does not change premise
policy, close theta, or prove a Strong-CP solution.
"""

from __future__ import annotations

import itertools
from math import comb

import numpy as np


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def cubic_levi_civita() -> np.ndarray:
    eps = np.zeros((3, 3, 3))
    for i, j, k in itertools.permutations(range(3)):
        eps[i, j, k] = np.sign((j - i) * (k - i) * (k - j))
    return eps


def signed_permutation_group() -> list[np.ndarray]:
    out: list[np.ndarray] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for a in range(3):
                R[a, perm[a]] = signs[a]
            out.append(R)
    return out


def transform_epsilon(R: np.ndarray, eps: np.ndarray) -> np.ndarray:
    return np.einsum("ai,bj,ck,ijk->abc", R, R, R, eps)


def main() -> int:
    passed: list[bool] = []

    passed.append(
        check(
            "form-degree check: C(3,4)=0 and C(4,4)=1",
            comb(3, 4) == 0 and comb(4, 4) == 1,
            "bare four-form writing has no components on a three-dimensional slice",
        )
    )

    eps = cubic_levi_civita()
    oh = signed_permutation_group()
    oh_ok = all(np.allclose(transform_epsilon(R, eps), np.linalg.det(R) * eps) for R in oh)
    passed.append(
        check(
            "O_h pseudoscalar law: R R R epsilon = det(R) epsilon",
            oh_ok and len(oh) == 48,
            f"verified on {len(oh)} signed-permutation matrices; full gauge-measure premise is not derived",
        )
    )

    max_im = 0.0
    for a, b in [(1.3, 0.5 + 0.4j), (0.7, 0.9 - 0.2j), (2.0, 0.3 + 1.1j)]:
        M = a * I3 + b * C + np.conj(b) * C.conj().T
        max_im = max(max_im, abs(np.imag(np.linalg.det(M))))
    passed.append(
        check(
            "K-real C_3 circulant determinant is real in the tested samples",
            max_im < 1e-12,
            f"max|Im det| = {max_im:.2e}",
        )
    )

    a, b = 1.3, 0.5
    M = a * I3 + b * (C + C.conj().T)
    alpha = 0.31
    n = 3
    Mrot = np.exp(2j * alpha) * M
    shift = np.angle(np.linalg.det(Mrot)) - np.angle(np.linalg.det(M))
    passed.append(
        check(
            "axial rotation shifts arg det by 2*n*alpha and breaks Hermiticity",
            abs(((shift - 2 * n * alpha + np.pi) % (2 * np.pi)) - np.pi) < 1e-9
            and not np.allclose(Mrot, Mrot.conj().T),
            f"shift={shift:.4f}; expected={2 * n * alpha:.4f}",
        )
    )

    ims = [
        abs(
            np.imag(
                np.linalg.det(
                    a * I3 + (r * np.exp(1j * t)) * C + np.conj(r * np.exp(1j * t)) * C.conj().T
                )
            )
        )
        for a in (1.0,)
        for r in (0.6,)
        for t in np.linspace(0, 2 * np.pi, 24)
    ]
    passed.append(
        check(
            "AC_phi_lambda overlap: same conjugate-symmetric C_3 circulant has Im det = 0",
            max(ims) < 1e-12,
            f"max|Im det| over coupling circle = {max(ims):.2e}",
        )
    )

    Mc = 1.0 * I3 + (0.5 + 0.4j) * C + (0.5 + 0.7j) * C.conj().T
    passed.append(
        check(
            "holomorphic gate is real: c != conj(b) gives nonzero Im det in this sample",
            abs(np.imag(np.linalg.det(Mc))) > 1e-3,
            f"Im det = {np.imag(np.linalg.det(Mc)):.4f}",
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("FINDING: the runner supports a structured open gate for theta_bar.")
    print("It verifies finite form-degree, O_h pseudoscalar, and C_3 circulant facts;")
    print("it does not close the Strong-CP open problem or change premise policy,")
    print("or establish a Strong-CP solution. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
