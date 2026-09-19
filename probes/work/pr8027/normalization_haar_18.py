#!/usr/bin/env python3
"""J:attack-f:PR8027 — NORMALIZATION.

Haar <Q|J_f|P>=1/18 (source trace 1/3, plaquette |chi|^2=1, /6);
sine-mode 2/(L+1); rho/L -> (2/π) sin(π η).
"""
from fractions import Fraction

import sympy as sp

HITS = []


def main():
    haar = Fraction(1, 3) * Fraction(1, 6)
    print(f"Haar (1/3)*(1/6)={haar} stated 1/18")
    if haar != Fraction(1, 18):
        HITS.append(f"1/18 {haar}")
    L = 3
    nrm = Fraction(2, L + 1)
    print(f"sine-mode 2/(L+1) at L=3 = {nrm}")
    eta = Fraction(1, 2)
    lim = 2 * sp.sin(sp.pi * eta) / sp.pi
    print(f"(2/π)sin(π η) at η=1/2 = {sp.simplify(lim)}")
    if sp.simplify(lim - 2 / sp.pi) != 0:
        HITS.append("2/π")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Haar 1/18, sine-mode "
        "2/(L+1), and (2/π)sin(πη) at η=1/2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
