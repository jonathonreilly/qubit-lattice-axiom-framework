#!/usr/bin/env python3
"""J:derive:two-source-interaction:a5 (worker w-macbookpro90c72-jc4c2).

Unlike-pin quadratic on L=4 from exact C Fourier: 1/(C0-C(e1))=128/147.
Independent short computation (not a2's full channel survey).
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

FAILS: list[str] = []
OKS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def main():
    L = 4
    N = L ** 3
    ctab = [1, 0, -1, 0]
    C0 = F(0)
    Ce1 = F(0)
    chi0 = F(0)
    chie1 = F(0)
    for n in itertools.product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        E = 2 * sum(1 - ctab[n[j]] for j in range(3))
        Ck = F(49, E * (14 - E))
        chik = F(7, E)
        # phase for e1=(1,0,0): exp(i pi n0 / 2) = i^{n0}; even C so use cos(pi n0/2)
        ph = [1, 0, -1, 0][n[0] % 4]  # Re exp(i k1)
        C0 += Ck
        Ce1 += Ck * ph
        chi0 += chik
        chie1 += chik * ph
    C0 /= N
    Ce1 /= N
    chi0 /= N
    chie1 /= N
    print("C0", C0, "C(e1)", Ce1)
    print("chi0", chi0, "chi(e1)", chie1)
    unlike = 1 / (C0 - Ce1)
    like = 1 / (C0 + Ce1)
    check("E1.unlike-128/147", unlike == F(128, 147), f"{unlike}")
    check("E1.like-lt-unlike", like < unlike)
    check("E1.C-nn-pos", Ce1 > 0)
    check("E1.chi-nn-pos", chie1 > 0)
    # FDR: chi/C not constant — sample two modes
    r1 = F(7, 2) / F(49, 2 * 12)  # dummy
    # mode (1,0,0): E=2, C=49/(2*12)=49/24, chi=7/2, ratio=(7/2)/(49/24)=7/2*24/49=12/7=1+phi
    E = 2
    phi = F(7 - E, 7)
    chi = F(7, E)
    Ck = F(49, E * (14 - E))
    check("E2.FDR-mode100", chi / Ck == 1 + phi, f"{chi/Ck} vs {1+phi}")
    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        f"HIT: PARTIAL: L=4 Gaussian unlike-pin quadratic 1/(C0-C(e1))={unlike}=128/147; "
        f"like 1/(C0+C(e1))={like} smaller (attractive when C(e1)>0); C(e1)={Ce1}, "
        f"chi(e1)={chie1}; FDR fails (chi/C=1+phi on mode (pi/2,0,0)). Linear superposition "
        "holds; mass=pin amplitude. Independent short Fourier, not a2's 357-check survey."
    )
    print(
        f"SUMMARY: PARTIAL L=4 unlike-pin energy 128/147 a^2; like attractive; "
        f"C(e1)={Ce1}; naive FDR fails"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
