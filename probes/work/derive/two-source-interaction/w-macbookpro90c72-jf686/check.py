#!/usr/bin/env python3
"""two-source-interaction, attempt 1 (worker w-macbookpro90c72-jf686).

Linear light-cone 7-neighbour law: chi=7/E, C=7/(2E(1-E/14)), FDR fails
(chi/C=1+phi); unlike-pin energy 128 a^2/147 on L=4.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import product

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAILS += 1
        print(f"FAIL: {tag} {msg}")


COS = [1, 0, -1, 0]  # cos(n * pi/2) for n=0,1,2,3


def E_of(n):
    return 2 * sum(1 - COS[nj] for nj in n)


def section_a():
    ok = True
    n_nz = 0
    for n in product(range(4), repeat=3):
        e = E_of(n)
        ph = 1 - e / F(7)
        # phi = (1 + 2 sum cos)/7
        ph2 = (1 + 2 * sum(COS[nj] for nj in n)) / F(7)
        ok = ok and ph == ph2
        if e == 0:
            ok = ok and ph == 1
            continue
        n_nz += 1
        chi = 1 / (1 - ph)
        C = 1 / (1 - ph ** 2)
        ok = ok and chi == F(7) / e
        ok = ok and C == F(7) / (2 * e * (1 - e / F(14)))
        ok = ok and chi / C == 1 + ph
    check("A1", ok and n_nz == 63,
          "L=4: phi=1-E/7; chi=7/E; C=7/(2E(1-E/14)) on all 63 nonzero modes")
    check("A2", ok, "naive FDR fails: chi/C = 1+phi on every nonzero L=4 mode")


def section_b():
    L = 4
    G0 = F(0)
    Gr = F(0)
    for n in product(range(L), repeat=3):
        e = E_of(n)
        if e == 0:
            continue
        C = F(7) / (2 * e * (1 - e / F(14)))
        G0 += C
        Gr += C * COS[n[0]]  # site e_1
    G0 /= L ** 3
    Gr /= L ** 3
    ok = G0 == F(18179, 15360) and Gr == F(539, 15360)
    ok = ok and G0 - Gr == F(147, 128)
    # (1/2) a^T C_SS^{-1} a / a^2 = 1/(G0-Gr) wait:
    # a^T inv a = 2 a^2 / (G0-Gr), energy = a^T inv a / 2 = a^2/(G0-Gr)
    # 1/(147/128) = 128/147
    energy_over_a2 = 1 / (G0 - Gr)
    ok = ok and energy_over_a2 == F(128, 147)
    check("B1", ok,
          f"L=4 unlike pins at distance e_1: G(0)={G0}, G(e1)={Gr}, "
          f"energy = 128 a^2/147")
    check("B2", G0 > Gr,
          "G(e1)>0 and G(0)>G(e1): like pins (once regularized) would be attractive")


def main():
    section_a()
    section_b()
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT a finite check - {FAILS} FAIL tags")
        return 1
    print(
        "HIT: new exact partial: linear 7-neighbour light-cone law has chi=7/E and "
        "C=7/(2E(1-E/14)) on every nonzero L=4 mode; naive FDR fails (chi/C=1+phi); "
        "unlike-pin Gaussian energy on L=4 at distance e_1 is 128 a^2/147; like pins "
        "are IR-divergent on the massless torus; G(e1)>0 so regularized like pins attract"
    )
    print(
        "SUMMARY: PARTIAL linear two-source theory: FDR fails with chi/C=1+phi; unlike "
        "energy 128 a^2/147 on L=4; like pins IR-divergent; nonlinear 1/r not claimed"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
