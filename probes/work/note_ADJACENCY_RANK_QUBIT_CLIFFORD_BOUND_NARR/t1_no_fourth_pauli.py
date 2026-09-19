#!/usr/bin/env python3
"""J:note:ADJACENCY_RANK — T1 falsifier: 4th anticommuting element of M_2(C).

Pauli sigma_1,2,3 mutually anticommute. The real-linear map
X |-> ({X,s1},{X,s2},{X,s3}) : R^8 -> R^12 (8 real coords of 2x2 complex)
has nullspace 0. HIT if a nonzero X anticommutes with all three.
"""
from __future__ import annotations

import numpy as np

HITS: list[str] = []

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = (s1, s2, s3)


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def ac(A, B):
    return A @ B + B @ A


def pack(M):
    return np.concatenate([M.real.ravel(), M.imag.ravel()])


def unpack(v):
    r, i = v[:4].reshape(2, 2), v[4:].reshape(2, 2)
    return r + 1j * i


def main() -> int:
    # Pauli anticommutation
    for a in range(3):
        for b in range(a + 1, 3):
            C = ac(PAULI[a], PAULI[b])
            n = np.max(np.abs(C))
            print(f"{{s{a+1},s{b+1}}} maxabs={n}")
            if n > 1e-12:
                hit(f"Pauli {a+1},{b+1} do not anticommute")
        sq = PAULI[a] @ PAULI[a]
        if np.max(np.abs(sq - np.eye(2))) > 1e-12:
            hit(f"s{a+1}^2 != I")

    # 8 real parameters of X in M_2(C)
    rows = []
    for k in range(8):
        e = np.zeros(8)
        e[k] = 1.0
        X = unpack(e)
        block = [pack(ac(X, s)) for s in PAULI]
        rows.append(np.concatenate(block))
    A = np.array(rows).T  # 12 x 8
    # SVD nullspace
    _, s, vh = np.linalg.svd(A, full_matrices=True)
    print(f"map R^8->R^12 singular values {s}")
    if np.min(s) < 1e-10:
        hit(f"nullspace: min singular value {np.min(s)}")
    print(f"rank ~ {np.sum(s > 1e-10)} / 8")

    # hostile witness gamma2' = (s1+s2)/sqrt(2) is s.a. unitary but does not
    # anticommute with s1
    g = (s1 + s2) / np.sqrt(2)
    print(f"hostile (s1+s2)/sqrt2: {{g,s1}} maxabs={np.max(np.abs(ac(g, s1)))}")
    if np.max(np.abs(ac(g, s1))) < 1e-12:
        hit("hostile witness unexpectedly anticommutes with s1")

    if HITS:
        print("SUMMARY: T1 falsifier FIRED - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: T1 no 4th anticommuting element of M_2(C): Pauli frame "
        "anticommutes, the 8-real-parameter map to three anticommutators has "
        "full rank 8; hostile (s1+s2)/sqrt2 does not anticommute with s1; "
        "falsifier does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
