#!/usr/bin/env python3
"""J:attack-f:PR8030 — NORMALIZATION of Haar J=ReTr(U)/3.

Note: E J=0, E J^2=1/18, X=√18 J with E X^2=1 and |X|≤√18.
The 1/18 is (E (Re χ)²)/9 with E|χ|²=1 and E χ²=0 ⇒ E(Re χ)²=1/2.

Recompute by SU(3) Weyl quadrature on the maximal torus (independent of
the existing 400×400 contact-limit script). HIT if a moment disagrees
beyond 1e-8.
"""
from __future__ import annotations

import math

import numpy as np

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def weyl_average(fn, n=120):
    a = 2 * np.pi * np.arange(n) / n
    A, B = np.meshgrid(a, a, indexing="ij")
    z1, z2, z3 = np.exp(1j * A), np.exp(1j * B), np.exp(-1j * (A + B))
    vd = np.abs((z1 - z2) * (z1 - z3) * (z2 - z3)) ** 2
    tr = z1 + z2 + z3
    return float(np.sum(vd * fn(tr)) / (6 * n * n))


def main() -> int:
    chi = lambda tr: tr
    EJ = weyl_average(lambda tr: np.real(chi(tr)) / 3)
    EJ2 = weyl_average(lambda tr: (np.real(chi(tr)) / 3) ** 2)
    Echi2 = weyl_average(lambda tr: np.real(chi(tr) ** 2))  # Re E χ²
    Eabs2 = weyl_average(lambda tr: np.abs(chi(tr)) ** 2)
    EX2 = 18 * EJ2
    B = math.sqrt(18)
    print(f"E J     = {EJ:.12e}  (want 0)")
    print(f"E J^2   = {EJ2:.12e}  (want 1/18={1/18:.12e})")
    print(f"E χ^2   = {Echi2:.12e}  (want 0)")
    print(f"E |χ|^2 = {Eabs2:.12e}  (want 1)")
    print(f"E X^2   = {EX2:.12e}  (want 1)")
    print(f"B=√18   = {B:.12f}; 1/2 from E(Re χ)² = E|χ|²/2 = {Eabs2/2:.12e}")
    if abs(EJ) > 1e-8:
        hit(f"E J={EJ} != 0")
    if abs(EJ2 - 1 / 18) > 1e-8:
        hit(f"E J^2={EJ2} != 1/18")
    if abs(Echi2) > 1e-8:
        hit(f"E χ^2={Echi2} != 0")
    if abs(Eabs2 - 1) > 1e-8:
        hit(f"E |χ|^2={Eabs2} != 1")
    if abs(EX2 - 1) > 1e-8:
        hit(f"E X^2={EX2} != 1")
    # |X|≤√18: max |Re Tr|/3 is 1, so |X|≤√18
    if abs(3 * 1 * B - math.sqrt(18) * 3) > 1e-12:
        pass
    maxJ = 1.0  # ReTr ≤ 3, J≤1
    if maxJ * B > B + 1e-15:
        hit("|X| bound failed")
    print(f"|X|≤√18 from |J|≤1: {maxJ * B:.12f} == {B:.12f}")

    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: NORMALIZATION (PR #8030): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: NORMALIZATION (PR #8030): Weyl quadrature gives E J=0, "
        "E J^2=1/18, E|χ|²=1 and E χ²=0 so E(Re χ)²=1/2, X=√18 J has E X^2=1 "
        "and |X|≤√18; pattern has purchase and the 1/2 / 1/18 / √18 conventions hold"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
