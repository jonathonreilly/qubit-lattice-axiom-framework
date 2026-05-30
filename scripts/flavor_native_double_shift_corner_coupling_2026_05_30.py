#!/usr/bin/env python3
"""Finite corner-cube checks for the native double-shift coupling.

The runner verifies:
  F1: each single bit flip projects to zero on the Hamming-weight-1 triplet;
  F2: the S3-symmetric sum of double bit flips projects to J-I;
  F3: Y=aI+b(J-I) has spectrum {a+2b,a-b,a-b};
  F4: for positive square-root masses in that symmetric form,
      Q = 1/3 + (2/3)(b/a)^2, so Q=2/3 iff (b/a)^2=1/2.
"""

from __future__ import annotations

import itertools
import numpy as np


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main() -> int:
    corners = list(itertools.product([0, 1], repeat=3))
    idx = {c: i for i, c in enumerate(corners)}

    def flip(c, mus):
        c = list(c)
        for m in mus:
            c[m] ^= 1
        return tuple(c)

    def shift(mus):
        mat = np.zeros((8, 8))
        for c in corners:
            mat[idx[flip(c, mus)], idx[c]] = 1
        return mat

    hw1 = [idx[c] for c in corners if sum(c) == 1]
    P = np.zeros((3, 8))
    for row, i in enumerate(hw1):
        P[row, i] = 1

    I = np.eye(3)
    J = np.ones((3, 3))
    B = J - I

    passed = []
    single_zero = all(np.allclose(P @ shift([mu]) @ P.T, 0) for mu in range(3))
    passed.append(check("single shifts project to zero on hw=1", single_zero))

    double_sum = P @ (shift([1, 2]) + shift([2, 0]) + shift([0, 1])) @ P.T
    passed.append(check("sum of double shifts projects to J-I", np.allclose(double_sum, B),
                        f"projection=\n{double_sum}"))

    a, b = 1.3, 0.4
    eig = np.linalg.eigvalsh(a * I + b * B)
    expected = np.sort([a + 2 * b, a - b, a - b])
    passed.append(check("spectrum of aI+b(J-I) is {a+2b,a-b,a-b}",
                        np.allclose(np.sort(eig), expected),
                        f"eig={np.sort(eig)}, expected={expected}"))

    def koide_q(square_roots):
        masses = square_roots ** 2
        return float(np.sum(masses) / np.sum(square_roots) ** 2)

    ok_q = True
    for ratio in [0.0, 0.25, 0.5, 0.9]:
        a = 2.0
        b = ratio * a
        y = np.array([a + 2 * b, a - b, a - b])
        ok_q &= abs(koide_q(y) - (1.0 / 3.0 + (2.0 / 3.0) * ratio ** 2)) < 1e-12
    target_ratio = 2 ** -0.5
    ok_q &= abs((1.0 / 3.0 + (2.0 / 3.0) * target_ratio ** 2) - 2.0 / 3.0) < 1e-12
    passed.append(check("Q formula and Q=2/3 iff (b/a)^2=1/2", ok_q))

    print(f"SCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
