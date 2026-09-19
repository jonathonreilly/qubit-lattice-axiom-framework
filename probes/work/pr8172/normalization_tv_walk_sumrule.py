#!/usr/bin/env python3
"""J:attack-f:PR8172 — NORMALIZATION.

No Fourier / 2π / conjugation / structure factor in the map-of-memory note.
The 1/2 and sum-rule factors that are present: TV=(1/2)Σ|μ-ν| in T1's c,
D_0=2 the chordal diameter, p_t = t!/(n1! n2! n3! 3^t) with Σ p_t = 1,
and T2's box /2. Recomputed at small size by brute force.

Do not re-find the known 4.05 vs 6671/1728 island-ratio HIT.
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product
from math import factorial

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def tv(mu: list[Fr], nu: list[Fr]) -> Fr:
    return Fr(1, 2) * sum(abs(a - b) for a, b in zip(mu, nu))


def main() -> int:
    # --- TV 1/2 convention (T1's c) ---
    u = [Fr(1, 6)] * 6
    if tv(u, u) != 0:
        hit(f"TV(uniform,uniform)={tv(u, u)} != 0")
    e0 = [Fr(1), 0, 0, 0, 0, 0]
    e1 = [0, Fr(1), 0, 0, 0, 0]
    if tv(e0, e1) != 1:
        hit(f"TV of distinct point masses = {tv(e0, e1)} != 1 (1/2 convention)")
    # without the 1/2 the uniqueness 3c<1 would use a different scale
    raw = sum(abs(a - b) for a, b in zip(e0, e1))
    if raw != 2:
        hit(f"raw L1 of point masses {raw} != 2")
    print(f"TV 1/2: TV(u,u)=0 TV(e0,e1)={tv(e0, e1)} raw L1={raw}")

    # six-axis forgotten memory is 1/6 (uniform)
    if sum(u) != 1:
        hit(f"uniform 1/6 does not sum to 1: {sum(u)}")
    print("six-axis uniform 1/6 sums to 1")

    # --- chordal diameter D_0 = 2 ---
    e = (Fr(0), Fr(0), Fr(1))
    antip = (Fr(0), Fr(0), Fr(-1))
    chord = sum((e[i] - antip[i]) ** 2 for i in range(3))
    # |e-(-e)|^2 = 4, so |e-(-e)| = 2
    if chord != 4:
        hit(f"|e-(-e)|^2 = {chord} != 4")
    print("chordal diameter of S^2: |e-(-e)|=2, so D_0=2*1_{x=x0} uses the max")

    # --- p_t sum rule by enumerating 3^t walks ---
    for t in range(0, 7):
        counts: dict[tuple[int, int, int], int] = {}
        for walk in product((0, 1, 2), repeat=t):
            n = [0, 0, 0]
            for s in walk:
                n[s] += 1
            key = (n[0], n[1], n[2])
            counts[key] = counts.get(key, 0) + 1
        tot = 3**t
        acc = Fr(0)
        for (n1, n2, n3), c in counts.items():
            p = Fr(c, tot)
            want = Fr(factorial(t), factorial(n1) * factorial(n2) * factorial(n3) * tot)
            if p != want:
                hit(f"p_{t}({n1},{n2},{n3})={p} != multinomial/3^t={want}")
                break
            acc += p
        if acc != 1:
            hit(f"Σ p_{t} = {acc} != 1 (3^{t}={tot} walks)")
        print(f"t={t}: {tot} walks, Σ p_t = {acc} (exactly 1)")

    # T3 factor: 2 (β/√3)^t 3^t = 2 (√3 β)^t
    b, t = sp.symbols("beta t", positive=True)
    left = 2 * (b / sp.sqrt(3)) ** t * 3**t
    right = 2 * (sp.sqrt(3) * b) ** t
    if sp.simplify(left - right) != 0:
        hit("2(β/√3)^t 3^t != 2(√3 β)^t")
    else:
        print("T3: 2(β/√3)^t 3^t = 2(√3 β)^t")

    # T2 box 1/2: (D+1)(6D+5)(6D+4)/2 is an integer and <= 18(D+1)^3
    for D in range(0, 21):
        box = (D + 1) * (6 * D + 5) * (6 * D + 4)
        if box % 2 != 0:
            hit(f"T2 box numerator odd at D={D}")
            break
        box //= 2
        cap = 18 * (D + 1) ** 3
        if box > cap:
            hit(f"T2 box {box} > 18(D+1)^3={cap} at D={D}")
            break
    print("T2 box (D+1)(6D+5)(6D+4)/2 integer and <= 18(D+1)^3 for D=0..20")

    if HITS:
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — no Fourier/2π/conjugation in this "
        "note; TV 1/2, six-axis 1/6, chordal D_0=2, p_t=t!/(n1!n2!n3! 3^t) "
        "sums to 1 on all 3^t walks t=0..6, 2(β/√3)^t 3^t=2(√3 β)^t, and "
        "T2's box /2, all recompute exactly; attack does not fire (not the "
        "known 4.05 island-ratio HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
