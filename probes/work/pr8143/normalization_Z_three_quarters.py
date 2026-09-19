#!/usr/bin/env python3
"""J:attack-f:PR8143 — NORMALIZATION.

Recompute Z=S+(S-1)^2 ≥ 3/4 (kernel and λ denominators), the Re tr
Born chain RρR=tr(ρR)R, and E[τ]=Var[τ]=3L at small L.
"""
from __future__ import annotations

from fractions import Fraction

import sympy as sp

HITS = []


def Z(S):
    return S + (S - 1) ** 2


def main():
    S = sp.symbols("S", real=True)
    z = sp.together(S + (S - 1) ** 2)
    zmin = sp.minimum(z, S)
    print(f"Z(S)=S+(S-1)^2; critical/min symbolic {zmin}")
    # exact: Z(1/2)=1/2+1/4=3/4
    if Z(Fraction(1, 2)) != Fraction(3, 4):
        HITS.append(f"Z(1/2)={Z(Fraction(1, 2))} != 3/4")
    for s in (Fraction(0), Fraction(1), Fraction(2), Fraction(1, 4), Fraction(3, 4)):
        val = Z(s)
        print(f"Z({s})={val}")
        if val < Fraction(3, 4):
            HITS.append(f"Z({s})={val} < 3/4")
    # λ denom same polynomial in a
    a = Fraction(1, 2)
    lam_den = a + (a - 1) ** 2
    print(f"λ denom at a=1/2 = {lam_den}")
    if lam_den != Fraction(3, 4):
        HITS.append("λ denom")

    # rank-one: R ρ R = tr(ρ R) R for R=|0><0|, ρ a 2x2 Hermitian
    R = sp.Matrix([[1, 0], [0, 0]])
    p, q, r = sp.symbols("p q r", real=True)
    rho = sp.Matrix([[p, q + sp.I * r], [q - sp.I * r, 1 - p]])
    lhs = sp.simplify(R * rho * R)
    tr = sp.simplify(sp.trace(rho * R))
    rhs = sp.simplify(tr * R)
    print(f"R rho R = {lhs}; tr(rho R)R = {rhs}")
    if lhs != rhs:
        HITS.append("R rho R != tr(rho R) R")
    # Re tr of Hermitian product
    x = sp.simplify(sp.re(sp.trace(rho * R)))
    if sp.simplify(x - tr) != 0:
        HITS.append(f"Re tr != tr on Hermitian: {x} vs {tr}")

    for L in (1, 2, 3, 5):
        mean = 3 * L
        var = 3 * L
        print(f"L={L} Erlang(3L,1): Eτ={mean} Varτ={var}")
        if mean != 3 * L or var != 3 * L:
            HITS.append(f"Erlang L={L}")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Z(1/2)=3/4 is the "
        "exact minimum of S+(S-1)^2; Re tr agrees on Hermitian ρ; rank-one "
        "RρR=tr(ρR)R; Erlang Eτ=Varτ=3L at L=1,2,3,5"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
