#!/usr/bin/env python3
"""J:attack-b:PR8143 — SAME TEST, BOTH SIDES.

Separations: (i) f_B clip vs f_S at tr(ρP)=1/4 (Born 1/4 vs 1/(1+e^{8/3}));
(ii) corridor blanks vs guards/outside under the same rate λ.
"""
from __future__ import annotations

from fractions import Fraction
from math import exp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def h(t: float) -> float:
    return exp(-1.0 / t) if t > 0 else 0.0


def f_S(x: float) -> float:
    return h(x) / (h(x) + h(1.0 - x))


def f_B(x: float) -> float:
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    return x


def main():
    x = 0.25
    born = f_B(x)
    smooth = f_S(x)
    stated = 1.0 / (1.0 + exp(8.0 / 3.0))
    if abs(born - 0.25) > 1e-15:
        hit(f"f_B(1/4)={born} != 1/4")
        return
    if abs(smooth - stated) > 1e-12:
        hit(f"f_S(1/4)={smooth} != 1/(1+e^{{8/3}})={stated}")
        return
    if abs(smooth - born) < 1e-9:
        hit("f_S and f_B agree at tr=1/4; the stated split is empty")
        return
    # same kernel (1) uses f(x_ij) as the P-atom; only f differs
    print(
        f"OK: same kernel (1) at tr(ρP)=1/4: f_B gives {born}, "
        f"f_S gives {smooth} = 1/(1+exp(8/3)); they differ"
    )

    # |C|=1+5L: T has 3L blanks; seed nonzero 1+2L; total 1+5L
    for L in range(1, 9):
        T = 3 * L
        seed_nz = 1 + 2 * L  # a0 + L programs + L markers
        C = T + seed_nz
        if C != 1 + 5 * L:
            hit(f"|C| for L={L} is {C} != 1+5L={1+5*L}")
            return
    print("OK: |C|=3L+(1+2L)=1+5L for L=1..8")

    # Rate λ: intended contexts (c,q,u,v) = (1,1,0,0), (0,0,1,0), (0,0,1,1)
    # give λ=1; empty/zero-only (0,0,0,0) gives λ=0. Same formula (2).
    def psi_u(u: float) -> float:
        # psi(u)=h(1-u)/[h(1-u)+h(u-1/4)]
        return h(1.0 - u) / (h(1.0 - u) + h(u - 0.25))

    def lam(c, q, u, v):
        Dm = (c - 1) ** 2 + (q - 1) ** 2 + u ** 2 + v ** 2
        Dc = c ** 2 + q ** 2 + (u - 1) ** 2 + v ** 2
        Dr = c ** 2 + q ** 2 + (u - 1) ** 2 + (v - 1) ** 2
        a = psi_u(Dm) + psi_u(Dc) + psi_u(Dr)
        return a / (a + (a - 1) ** 2)

    on = [lam(1, 1, 0, 0), lam(0, 0, 1, 0), lam(0, 0, 1, 1)]
    off = [lam(0, 0, 0, 0), lam(1, 0, 0, 0), lam(0, 1, 0, 0), lam(0, 0, 0, 1)]
    if any(abs(x - 1.0) > 1e-12 for x in on):
        hit(f"intended contexts do not all have λ=1: {on}")
        return
    if any(abs(x) > 1e-12 for x in off):
        hit(f"empty/program-alone/marker-alone do not all have λ=0: {off}")
        return
    print("OK: same rate (2): corridor contexts λ=1, empty/program/marker-alone λ=0")

    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — kernel (1) at tr=1/4 "
            "gives f_B=1/4 vs f_S=1/(1+e^{8/3}); rate (2) gives λ=1 on the three "
            "corridor contexts and λ=0 on empty/program/marker-alone; |C|=1+5L; "
            "the splits are live under the identical formulae; attack does not fire"
        )


if __name__ == "__main__":
    main()
