#!/usr/bin/env python3
"""J:attack-b:PR8170 — same φ(0) gain test; do not re-find the exponent-vs-gamma HIT.

The linearized 3-predecessor kernel is claimed to have gain one: φ(0)=1.
Apply the same φ(0) test to the 3-pred stencil and to a 2-pred 2D stencil.
HIT if 3-pred φ(0)!=1, or if the note's gain-one claim is unique to 3-pred
while 2-pred also has φ(0)=1 *and* the note treats 2-pred as lacking gain one
(it does not). This unit only checks the 3-pred identity literally.
"""
from __future__ import annotations

import sympy as sp


def main():
    hits = []
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi3 = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    g3 = sp.simplify(phi3.subs({k1: 0, k2: 0}))
    print(f"3-pred φ(0)={g3}")
    if g3 != 1:
        hits.append(f"HIT: 3-pred φ(0)={g3} != 1")
        print(hits[-1])
    phi2 = (1 + sp.exp(sp.I * k1)) / 2
    g2 = sp.simplify(phi2.subs({k1: 0}))
    print(f"2-pred φ(0)={g2}")
    # both have gain one; the note's 3D formation stencil is the 3-pred one
    if hits:
        print("SUMMARY: 3-pred gain-one test fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known exponent-vs-gamma "
        "HIT — 3-pred φ(0)=1 (gain one) holds; a 2-pred stencil also has φ(0)=1, which "
        "the note does not claim to lack"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
