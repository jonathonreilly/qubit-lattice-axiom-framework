#!/usr/bin/env python3
"""J:attack-b:PR8178 — same |φ|² test on zero vs nonzero torus modes.

Do not re-find the known lag-25 D1 HIT.
T1: u=1 only at the zero mode; u<1 off zero. Same test: compute u=|φ|².
HIT if a nonzero mode has u=1 or the zero mode has u!=1.
"""
from __future__ import annotations

import cmath
import math


def u_of(k1, k2):
    phi = (1 + cmath.exp(1j * k1) + cmath.exp(1j * k2)) / 3
    return abs(phi) ** 2


def main():
    hits = []
    for L in (2, 3, 4, 8):
        z_u = None
        nz = []
        for n1 in range(L):
            for n2 in range(L):
                k1 = 2 * math.pi * n1 / L
                k2 = 2 * math.pi * n2 / L
                u = u_of(k1, k2)
                if (n1, n2) == (0, 0):
                    z_u = u
                else:
                    nz.append(u)
        print(f"L={L}: zero u={z_u:.12f} nonzero max={max(nz):.12f} min={min(nz):.12f}")
        if abs(z_u - 1) > 1e-12:
            hits.append(f"HIT: zero mode u={z_u} != 1 at L={L}")
            print(hits[-1])
        if max(nz) >= 1 - 1e-12:
            hits.append(f"HIT: a nonzero mode has u=1 at L={L}")
            print(hits[-1])
    if hits:
        print("SUMMARY: zero vs nonzero |φ|² test fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known lag-25 D1 HIT "
        "— the same |φ|² test gives u=1 at the zero mode and u<1 at every nonzero "
        "mode of L=2,3,4,8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
