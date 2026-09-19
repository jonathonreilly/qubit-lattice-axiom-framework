#!/usr/bin/env python3
"""J:attack-d:PR8180 — QUANTIFIER SCOPE on T3's bound for every nonzero mode.

Not the known T1 conjugation HIT, kernel_sim shells, or D2 non-product HIT.

T3: for every nonzero mode on |k_i|≤π,
  |φ|^s = u^{s/2} ≤ exp(-(1-u)s/2) ≤ exp(-2|k|^2 s/(9π²))
via log(1-y)≤-y and 1-u ≥ 4|k|^2/(9π²). Executed on tiny tori L=3,4 (cosine
characters). Check every mode of L=3..8, folded to the square.
"""
from __future__ import annotations

import mpmath as mp

HITS = []
mp.mp.dps = 40


def fold(k):
    pi = mp.pi
    while k > pi:
        k -= 2 * pi
    while k < -pi:
        k += 2 * pi
    return k


def one_minus_u(k1, k2):
    return (2 * (3 - mp.cos(k1) - mp.cos(k2) - mp.cos(k1 - k2))) / 9


def main():
    pi = mp.pi
    tol = mp.mpf("1e-25")
    for L in range(3, 9):
        nfail = 0
        nmode = 0
        worst = None
        for n1 in range(L):
            for n2 in range(L):
                if n1 == 0 and n2 == 0:
                    continue
                nmode += 1
                k1 = fold(2 * pi * n1 / L)
                k2 = fold(2 * pi * n2 / L)
                y = one_minus_u(k1, k2)
                rhs = 4 * (k1 * k1 + k2 * k2) / (9 * pi * pi)
                if y < 0 or y > 1:
                    HITS.append(f"L={L} k=({n1},{n2}) 1-u={y} not in [0,1]")
                    nfail += 1
                    continue
                if y + tol < rhs:
                    nfail += 1
                    gap = rhs - y
                    if worst is None or gap > worst[0]:
                        worst = (gap, L, n1, n2, y, rhs)
                # log(1-y) <= -y
                if y < 1 - mp.mpf("1e-20"):
                    if mp.log(1 - y) > -y + tol:
                        HITS.append(f"log(1-y)>-y at L={L} ({n1},{n2})")
                for s in (1, 2, 4, 8):
                    lhs = (1 - y) ** (mp.mpf(s) / 2)
                    bound = mp.e ** (-2 * (k1 * k1 + k2 * k2) * s / (9 * pi * pi))
                    if lhs > bound + mp.mpf("1e-18"):
                        HITS.append(
                            f"|phi|^{s} > T3 bound at L={L} ({n1},{n2}): {lhs} > {bound}"
                        )
                        break
        print(f"L={L} modes={nmode} 1-u>=4|k|^2/(9π²) fails={nfail}")
        if worst:
            print(f"  worst gap={worst[0]} at L={worst[1]} n={worst[2],worst[3]} y={worst[4]} rhs={worst[5]}")
            HITS.append(
                f"1-u < 4|k|^2/(9π²) at L={worst[1]} n=({worst[2]},{worst[3]})"
            )

    # T2 quadratic form eigenvalues, every direction on the unit circle
    M11, M12, M22 = mp.mpf("2") / 9, mp.mpf("-1") / 9, mp.mpf("2") / 9
    eigs = []
    for t in range(0, 360, 5):
        th = t * pi / 180
        c, s = mp.cos(th), mp.sin(th)
        q = M11 * c * c + 2 * M12 * c * s + M22 * s * s
        eigs.append(q)
    mn, mx = min(eigs), max(eigs)
    print(f"k^T M k on the circle: min={mn} max={mx} stated 1/9 and 1/3")
    if mn < mp.mpf(1) / 9 - mp.mpf("1e-20") or mx > mp.mpf(1) / 3 + mp.mpf("1e-20"):
        HITS.append(f"M eigenvalues off: min={mn} max={mx}")

    if HITS:
        print("HIT: " + "; ".join(HITS[:6]))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS[:4]))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - T3's 1-u≥4|k|^2/(9π²) "
        "and |φ|^s≤exp(-2|k|^2 s/(9π²)) hold for every nonzero mode of L=3..8 "
        "(equality of 1-u at (π,π)); M's eigenvalues stay in [1/9,1/3]; not the "
        "known T1 conjugation or kernel_sim shell HITs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
