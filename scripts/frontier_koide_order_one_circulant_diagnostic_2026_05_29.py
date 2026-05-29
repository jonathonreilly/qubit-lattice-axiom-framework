#!/usr/bin/env python3
"""Bounded diagnostic: C_3-circulant order-one does not select Koide r=1/2."""

from __future__ import annotations

import sys

import numpy as np
from sympy import Matrix, eye, simplify, symbols, zeros

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def main() -> int:
    section("Symbolic C_3-circulant algebra")
    r = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    i3 = eye(3)
    a, b, c = symbols("a b c")
    x, y, z = symbols("x y z")
    m = a * i3 + b * r + c * (r**2)
    alg = x * i3 + y * r + z * (r**2)
    check("M commutes with every C_3-circulant algebra element", simplify(m * alg - alg * m) == zeros(3))

    d = Matrix.vstack(Matrix.hstack(zeros(3), m), Matrix.hstack(m.T, zeros(3)))
    pi_alg = Matrix.vstack(Matrix.hstack(alg, zeros(3)), Matrix.hstack(zeros(3), alg))
    inner = simplify(d * pi_alg - pi_alg * d)
    check("[D, pi(A)] vanishes identically", inner == zeros(6))

    section("Distinct-r witnesses")
    rn = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    i3n = np.eye(3, dtype=complex)
    j = np.block([[np.zeros((3, 3)), i3n], [-i3n, np.zeros((3, 3))]])

    def pi(vec: tuple[complex, complex, complex]) -> np.ndarray:
        alpha, beta, gamma = vec
        a_mat = alpha * i3n + beta * rn + gamma * (rn @ rn)
        return np.block([[a_mat, np.zeros((3, 3))], [np.zeros((3, 3)), a_mat]])

    def pi_opp(vec: tuple[complex, complex, complex]) -> np.ndarray:
        p = pi(vec)
        return j @ p.conj() @ np.linalg.inv(j)

    probes = [(1, 0, 0), (0, 1, 0), (0.3 + 0.2j, 0.7, 0.1j), (1, 1j, 0.5)]
    for ratio in [0.05, 0.20, 0.50, 1.00, 2.00, 5.00]:
        bval = ratio**0.5
        mn = i3n + bval * rn
        d_num = np.block([[np.zeros((3, 3)), mn], [mn.conj().T, np.zeros((3, 3))]])
        max_resid = 0.0
        for av in probes:
            comm = d_num @ pi(av) - pi(av) @ d_num
            for bv in probes:
                resid = comm @ pi_opp(bv) - pi_opp(bv) @ comm
                max_resid = max(max_resid, float(np.max(np.abs(resid))))
        check(f"r={ratio:g} satisfies order-one in this route", max_resid < 1e-10, f"max={max_resid:.2e}")

    section("Summary")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("C_3-circulant order-one is vacuous on this route, so it does not select r=1/2.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
