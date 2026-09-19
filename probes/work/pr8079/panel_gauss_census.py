#!/usr/bin/env python3
"""J:attack-g:PR8079 — pattern (g) PROOF STEP BY BRUTE FORCE.

The fifth-half-moment supplier states a finite census: 67 dyadic panels from
2^{-64} to 8, Gauss26 (degree 51) giving 1742 nodes and 3484 endpoint oracles,
and the Chebyshev tail summing to a radius below 1792 * 4^{-52}
(=(16/3)*42*8 * 4^{-52}). Distinct from the ellipse/Q5/15-defect falsifier.

HIT if any of those integer identities fails, or if EX^2 for X=6-2 sum_j cos
is not 42.
"""
from __future__ import annotations

from fractions import Fraction as F

HITS = []


def main():
    n_panels = (2 - (-64)) + 1
    print(f"dyadic panels k=-64..2: {n_panels} (stated 67)")
    if n_panels != 67:
        HITS.append(f"panel count {n_panels} != 67")

    gauss_n = 26
    deg = 2 * gauss_n - 1
    print(f"Gauss{gauss_n} exactness degree {deg} (stated 51)")
    if deg != 51:
        HITS.append(f"Gauss26 degree {deg} != 51")

    nodes = 67 * 26
    print(f"67*26 nodes={nodes} (stated 1742)")
    if nodes != 1742:
        HITS.append(f"nodes {nodes} != 1742")

    oracles = 1742 * 2
    print(f"1742*2 oracles={oracles} (stated 3484)")
    if oracles != 3484:
        HITS.append(f"oracles {oracles} != 3484")

    pre = F(16, 3) * 42 * 8
    print(f"(16/3)*42*8={pre} (stated 1792)")
    if pre != 1792:
        HITS.append(f"prefactor {pre} != 1792")

    # sum of panel starts 2^{-64}+...+2^{2} = 8 - 2^{-64} < 8, so strictly below 1792
    s = F(2) ** 3 - F(2) ** (-64)
    print(f"sum of panel left endpoints={s} < 8")
    if not (s < 8):
        HITS.append("geometric sum of panel starts is not < 8")

    # EX and EX^2 for X=6-2(cos1+cos2+cos3) on the torus, exact
    # E cos=0, E cos_i cos_j=0 (i!=j), E cos^2=1/2
    M1 = 6
    M2 = 36 + 4 * (3 * F(1, 2))  # 36 + 4*E[(sum cos)^2]=36+4*(3/2)=42
    print(f"M1={M1} M2={M2} (stated 6, 42)")
    if M1 != 6 or M2 != 42:
        HITS.append(f"moments M1={M1} M2={M2}")

    # low-piece polynomial integral L=int_0^eps (42-6t^2+t^4) dt
    eps = F(1, 2) ** 64
    L = 42 * eps - 2 * eps**3 + eps**5 / 5
    L_stated = 42 * eps - 2 * eps**3 + eps**5 / 5
    print(f"L identity tautological {L==L_stated}; L={L}")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on the 67-panel/"
            "Gauss26 census and 1792 tail prefactor - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - 67 dyadic panels, "
        "Gauss26 degree 51, 67*26=1742 nodes, 3484 oracles, (16/3)*42*8=1792, "
        "and EX^2=42 all hold exactly (not a re-check of the ellipse/Q5 falsifier)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
