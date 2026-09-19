#!/usr/bin/env python3
"""J:attack-g:PR8029 — pattern (g) PROOF STEP BY BRUTE FORCE.

Section 4: Psi=(W_gamma/sqrt(3)) Omega has ||Psi||=1 because
pointwise Tr(W^* W)/3=1 for W in SU(3); each path link adds Casimir 4/a
(Q(1,0)=Q(0,1)=4). Exact SU(3) matrices (not unsimplified trig forms).
"""
from __future__ import annotations

import sympy as sp

HITS = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def check_U(name, U):
    UhU = sp.simplify(U.H * U)
    det = sp.simplify(U.det())
    tr = sp.simplify(sp.trace(U.H * U) / 3)
    print(f"{name}: U^H U = I? {UhU == sp.eye(3)}; det={det}; Tr(U^H U)/3={tr}")
    if UhU != sp.eye(3):
        HITS.append(f"{name} not unitary")
    if det != 1:
        HITS.append(f"{name} det={det} != 1")
    if tr != 1:
        HITS.append(f"{name} Tr/3={tr} != 1")


def main():
    if Q(1, 0) != 4 or Q(0, 1) != 4:
        HITS.append(f"fundamental Q != 4: {Q(1,0)} {Q(0,1)}")
    print(f"Q(1,0)={Q(1,0)} Q(0,1)={Q(0,1)} (stated 4)")

    I = sp.eye(3)
    check_U("I", I)
    # 3-cycle permutation, det +1
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    check_U("cycle", C)
    # diagonal phases, det 1
    w = sp.exp(2 * sp.pi * sp.I / 3)
    D = sp.diag(w, w, w.conjugate() ** 2)  # w*w*w^{-2}=w^0=1
    D = sp.diag(w, w.conjugate(), 1)
    check_U("diag phases", D)
    # two-link product still SU(3)
    W = sp.simplify(C * D)
    check_U("cycle*diag", W)

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on path-vector "
            "normalization - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Tr(W^*W)/3=1 on exact "
        "SU(3) identity, 3-cycle, diagonal phases and their product, and "
        "Q(1,0)=Q(0,1)=4, so section 4 ||Psi||=1 and 4/a-per-link hold"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
