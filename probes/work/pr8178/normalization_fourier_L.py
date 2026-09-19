#!/usr/bin/env python3
"""J:attack-f:PR8178 — NORMALIZATION of torus Fourier conjugation.

Stated DFT: θ̂_k = L^{-1} Σ_x e^{-ik·x} θ_x.
Stated P: Pθ_x = (θ_x + θ_{x-e1} + θ_{x-e2})/3.
Stated φ: (1 + e^{ik1} + e^{ik2})/3.
The shift theorem for that DFT gives multiplier (1 + e^{-ik1} + e^{-ik2})/3,
the conjugate. They agree at L=2 (k=π) and differ at L=3.

Do not re-find the known lag-25 D1 HIT. |φ|² (hence T1.2–T1.3) is the same.
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product

import sympy as sp

I = sp.I
pi = sp.pi


def hat(field, n1, n2, L):
    acc = 0
    k1 = 2 * pi * n1 / L
    k2 = 2 * pi * n2 / L
    for x1 in range(L):
        for x2 in range(L):
            acc += sp.exp(-I * (k1 * x1 + k2 * x2)) * field[(x1, x2)]
    return sp.simplify(acc / L)


def apply_P(field, L):
    out = {}
    for x1 in range(L):
        for x2 in range(L):
            out[(x1, x2)] = (
                field[(x1, x2)]
                + field[((x1 - 1) % L, x2)]
                + field[(x1, (x2 - 1) % L)]
            ) / 3
    return out


def phi_plus(n1, n2, L):
    k1 = 2 * pi * n1 / L
    k2 = 2 * pi * n2 / L
    return (1 + sp.exp(I * k1) + sp.exp(I * k2)) / 3


def phi_minus(n1, n2, L):
    k1 = 2 * pi * n1 / L
    k2 = 2 * pi * n2 / L
    return (1 + sp.exp(-I * k1) + sp.exp(-I * k2)) / 3


def mag2(z):
    return sp.simplify(sp.expand_complex(sp.conjugate(z) * z))


def main() -> int:
    hits = []
    # Parseval / L^{-1} convention on a delta (holds)
    for L in (2, 3, 4):
        delta = {
            (x1, x2): (1 if (x1, x2) == (0, 0) else 0)
            for x1 in range(L)
            for x2 in range(L)
        }
        hats = {(n1, n2): hat(delta, n1, n2, L) for n1, n2 in product(range(L), repeat=2)}
        lhs = sp.simplify(sum(mag2(h) for h in hats.values()))
        print(f"L={L} Parseval Σ|θ̂_delta|²={lhs} (want 1); |θ̂|^2={mag2(hats[(0,0)])} (want 1/L^2={Fr(1, L*L)})")
        if sp.simplify(lhs - 1) != 0:
            hits.append(f"Parseval fails at L={L}")
        if sp.simplify(mag2(hats[(0, 0)]) - Fr(1, L * L)) != 0:
            hits.append(f"L^{{-1}} convention fails at L={L}")
        mean = sp.Integer(1) / (L * L)
        bar = sp.simplify(hats[(0, 0)] / L)
        if sp.simplify(bar - mean) != 0:
            hits.append(f"θ̄=θ̂_0/L fails at L={L}")

    # conjugation: (P delta)^_k vs φ_± * θ̂_k
    mismatches_plus = []
    mismatches_minus = []
    for L in (2, 3, 4):
        delta = {
            (x1, x2): (1 if (x1, x2) == (0, 0) else 0)
            for x1 in range(L)
            for x2 in range(L)
        }
        Pd = apply_P(delta, L)
        hats = {(n1, n2): hat(delta, n1, n2, L) for n1, n2 in product(range(L), repeat=2)}
        for n1, n2 in product(range(L), repeat=2):
            hp = hat(Pd, n1, n2, L)
            pp = sp.simplify(phi_plus(n1, n2, L) * hats[(n1, n2)])
            pm = sp.simplify(phi_minus(n1, n2, L) * hats[(n1, n2)])
            if sp.simplify(hp - pp) != 0:
                mismatches_plus.append((L, n1, n2))
            if sp.simplify(hp - pm) != 0:
                mismatches_minus.append((L, n1, n2))
    print(f"stated φ=(1+e^{{+ik}})/3 mismatches: {len(mismatches_plus)} modes")
    print(f"shift φ=(1+e^{{-ik}})/3 mismatches: {len(mismatches_minus)} modes")
    print("plus mismatches:", mismatches_plus[:8])

    # exact witness L=3 n=(0,1)
    L, n1, n2 = 3, 0, 1
    pp = sp.expand_complex(sp.simplify(phi_plus(n1, n2, L)))
    pm = sp.expand_complex(sp.simplify(phi_minus(n1, n2, L)))
    print(f"L=3 n=(0,1): φ_+={pp}  φ_-={pm}  |φ_+|²={mag2(phi_plus(n1,n2,L))} |φ_-|²={mag2(phi_minus(n1,n2,L))}")
    want_plus = sp.Rational(1, 2) + sp.sqrt(3) * I / 6
    want_minus = sp.Rational(1, 2) - sp.sqrt(3) * I / 6
    if sp.simplify(pp - want_plus) != 0 or sp.simplify(pm - want_minus) != 0:
        hits.append(f"witness values drifted: +{pp} -{pm}")
    if mag2(phi_plus(n1, n2, L)) != mag2(phi_minus(n1, n2, L)):
        hits.append("|φ_+|² != |φ_-|² (u-formulas would split)")

    if mismatches_plus and not mismatches_minus:
        hits.append(
            "T1.1 conjugation: stated DFT e^{-ik·x} with Pθ_x=(θ_x+θ_{x-e1}+θ_{x-e2})/3 "
            "multiplies by (1+e^{-ik1}+e^{-ik2})/3, not the stated "
            "(1+e^{+ik1}+e^{+ik2})/3; they agree at L=2 (k=π) and differ at "
            f"L=3 n=(0,1) where φ_+={want_plus} and φ_-={want_minus}; |φ|² is equal"
        )
    elif mismatches_minus:
        hits.append(f"shift-theorem φ_- also fails on {mismatches_minus[:3]}")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: pattern (f) NORMALIZATION; " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — L^{{-1}} DFT Parseval and "
        "θ̄=θ̂_0/L hold; stated φ matches the DFT shift; attack does not fire "
        "(not the known lag-25 D1 HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
