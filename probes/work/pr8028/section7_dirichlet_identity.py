#!/usr/bin/env python3
"""J:attack-g:PR8028 — pattern (g) PROOF STEP BY BRUTE FORCE.

Section 7 of the uniform static-source note asserts a finite identity for the
open-line trial: with Tr(T_A T_B)=delta_AB,
  (3/(2a)) (1/3) sum_A Tr[(D^A U)^dagger D^A U] = (3/(2a))(8/3) = 4/a,
and pointwise sum_{ab} |U_ab|^2 = 3 for U in SU(3), so the extra kinetic per
path link is 4/a. Also section 1: every nontrivial irrep costs at least 4/a
because Q(p,q)=p^2+pq+q^2+3p+3q, Q>=4 off (0,0).

Verify those identities literally with Gell-Mann/sqrt(2) generators and the
integer Casimir Q on a finite (p,q) grid. HIT if any equality fails.
"""
from __future__ import annotations

from fractions import Fraction as F

import numpy as np
import sympy as sp

HITS = []


def gell_mann_over_sqrt2():
    s2 = sp.sqrt(2)
    lam = []
    lam.append(sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]))
    lam.append(sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]]))
    lam.append(sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3))
    return [L / s2 for L in lam]


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    Ts = gell_mann_over_sqrt2()
    print(f"n_generators={len(Ts)}")
    # Tr(T_A T_B) = delta_AB
    for a, A in enumerate(Ts):
        for b, B in enumerate(Ts):
            tr = sp.simplify(sp.trace(A * B))
            want = 1 if a == b else 0
            if tr != want:
                HITS.append(f"Tr(T_{a} T_{b})={tr} != {want}")
    print("Tr(T_A T_B)=delta: ", "FAIL" if any("Tr(T_" in h for h in HITS) else "ok")

    # sum_A Tr(T_A^dagger T_A) = 8
    s = sum(sp.simplify(sp.trace(A.H * A)) for A in Ts)
    print(f"sum_A Tr(T_A^H T_A)={s}")
    if s != 8:
        HITS.append(f"sum_A Tr(T^H T)={s} != 8")

    # note: (3/(2a))*(1/3)*8 = 4/a
    coeff = F(3, 2) * F(1, 3) * 8
    print(f"(3/2)*(1/3)*8={coeff} (stated 4)")
    if coeff != 4:
        HITS.append(f"(3/2)*(1/3)*8={coeff} != 4")

    # U in SU(3): sum_ab |U_ab|^2 = 3, and sum_A Tr((T_A U)^H (T_A U))=8
    th, ph, ps = sp.symbols("th ph ps", real=True)
    # a concrete SU(3) element: diag(e^{i th}, e^{i ph}, e^{-i(th+ph)}) * a Givens rotation
    c, s_ = sp.cos(th), sp.sin(th)
    R = sp.Matrix([[c, s_, 0], [-s_, c, 0], [0, 0, 1]])
    D = sp.diag(sp.exp(sp.I * ph), sp.exp(sp.I * ps), sp.exp(-sp.I * (ph + ps)))
    U = sp.simplify(R * D)
    # det 1, U^H U = I at a numeric point
    Unum = U.subs({th: sp.pi / 5, ph: sp.pi / 7, ps: sp.pi / 11})
    fro2 = sp.simplify(sum(sp.Abs(Unum[i, j]) ** 2 for i in range(3) for j in range(3)))
    print(f"sum_ab |U_ab|^2 at a numeric SU(3) point = {fro2} (stated 3)")
    if fro2 != 3:
        HITS.append(f"Frobenius^2={fro2} != 3")
    extra = sum(sp.simplify(sp.trace((A * Unum).H * (A * Unum))) for A in Ts)
    extra = sp.simplify(extra)
    print(f"sum_A Tr((T_A U)^H (T_A U))={extra} (stated 8)")
    if extra != 8:
        HITS.append(f"path-link Dirichlet extra={extra} != 8")

    # Casimir floor: Q>=4 off (0,0), equality at (1,0) and (0,1)
    floor_ok = True
    eq_at = []
    for p in range(0, 8):
        for q in range(0, 8):
            v = Q(p, q)
            if (p, q) == (0, 0):
                if v != 0:
                    HITS.append("Q(0,0)!=0")
                    floor_ok = False
            else:
                if v < 4:
                    HITS.append(f"Q({p},{q})={v}<4")
                    floor_ok = False
                if v == 4:
                    eq_at.append((p, q))
    print(f"Q>=4 off (0,0) on 8x8: {floor_ok}; equality at {eq_at}")
    if set(eq_at) != {(1, 0), (0, 1)}:
        HITS.append(f"Q=4 at {eq_at}, not exactly (1,0) and (0,1)")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on section 7 "
            "Dirichlet 8/3 identity and Casimir floor - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - section 7's identities "
        "sum_A Tr(T_A^H T_A)=8, (3/2)(1/3)8=4, Frobenius^2=3 on SU(3), and "
        "Q(p,q)>=4 off (0,0) with equality only at the two fundamentals, all hold "
        "by exact enumeration"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
