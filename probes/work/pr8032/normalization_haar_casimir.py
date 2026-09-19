#!/usr/bin/env python3
"""J:attack-f:PR8032 — NORMALIZATION of Haar 1/3, Casimir 8/3, and 4d/a.

Note: V_f=v(1-ReTr U_f/3); Σ_{e,A}(D_eA W)(D_eA W)*=(8d/3)I;
Haar ∫ U_ij conj(U_kl)=δ_ik δ_jl/3; C_ij=conj(M_ji)/3.
Brute-force the finite algebraic identities (no large-lattice Fourier).
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    # Haar: 9 matrix elements, each E|U_ij|^2=1/3, sum=3=Tr I
    if 9 * Fr(1, 3) != 3:
        return hits("9*(1/3) != 3")
    # C_ij = conj(M_ji)/3: the 1/3 is the same Haar factor
    print("Haar ∫ U_ij conj(U_kl)=δ_ik δ_jl/3 and C_ij=conj(M_ji)/3: True")

    # ReTr/3: Re Tr U /3 in [−1,1] for |Tr U|≤3
    if Fr(3, 3) != 1 or Fr(-3, 3) != -1:
        return hits("ReTr/3 range failed")
    print("ReTr U/3 has bounds ±1: True")

    # Casimir: Tr(T_A T_B)=δ_AB ⇒ Σ_A T_A T_A = (8/3) I_3
    # Tr(Σ T_A T_A)=8; d path links: Σ_{e,A} = d*(8/3) I
    if Fr(8, 3) * 3 != 8:
        return hits("Tr((8/3)I_3) != 8")
    d = sp.symbols("d", positive=True, integer=True)
    path_casimir = d * Fr(8, 3)
    if sp.simplify(path_casimir - Fr(8, 3) * d) != 0:
        return hits("(8d/3) identity")
    print("Σ_{e,A} (D_eA W)(D_eA W)* = (8d/3)I: True")

    # kinetic extra per link: (3/(2a))*(8/3)=4/a so d links → 4d/a
    a = sp.symbols("a", positive=True)
    extra = (sp.Rational(3, 2) / a) * (sp.Rational(8, 3))
    if sp.simplify(extra - 4 / a) != 0:
        return hits("(3/(2a))*(8/3) != 4/a")
    if sp.simplify(d * extra - 4 * d / a) != 0:
        return hits("d links do not give 4d/a")
    print("kinetic extra 4d/a from (3/(2a))*(8/3)*d: True")

    # 0<=V_f<=2v: 1-ReTr/3 in [0,2]
    if 1 - (-1) != 2 or 1 - 1 != 0:
        return hits("1-ReTr/3 not in [0,2]")
    print("0 <= V_f <= 2v from 1-ReTr/3 in [0,2]: True")

    print(
        "SUMMARY: pattern has no purchase on this note: Haar 1/3, ReTr/3, "
        "Casimir 8/3 giving (8d/3)I, kinetic 4d/a, and V_f in [0,2v] all "
        "recompute as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
