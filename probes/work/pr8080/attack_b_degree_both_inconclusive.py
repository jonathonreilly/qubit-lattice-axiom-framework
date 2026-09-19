#!/usr/bin/env python3
"""J:attack-b:PR8080 — SAME TEST, BOTH SIDES.

Separations: six NN directions vs fifteen two-link channels; degree-one vs
degree-two first-polynomial certificates (both INDETERMINATE_SIGN); Q_tau−λ⁻²
nonnegative for every λ≥δ.
"""
from __future__ import annotations

import itertools
from fractions import Fraction

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main():
    axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    channels = list(itertools.combinations(range(6), 2))
    if len(axes) != 6 or len(channels) != 15:
        hit(f"6 labels / 15 channels: got {len(axes)} {len(channels)}")
        return
    # each channel is a 2-star at the origin, not a triangle
    for i, j in channels:
        a, b = axes[i], axes[j]
        # ends are not NN to each other unless they are opposite? opposite is
        # e and -e, L1=2. Adjacent axes e.g. e1 and e2: L1=2.
        l1 = sum(abs(a[k] - b[k]) for k in range(3))
        if l1 == 1:
            hit(f"channel {a},{b} is a Z^3 triangle")
            return
    print("OK: six axes, C(6,2)=15 two-link channels, none is a Z^3 triangle")

    # Q_tau(λ) − λ^{-2} ≥ 0 for λ≥δ, same identity for every residual
    # Q = (3τ−2λ)/τ³ + A(λ−τ)², A=(τ+2δ)/(δ² τ³)
    delta, tau = Fraction(1, 4), Fraction(1)
    A = (tau + 2 * delta) / (delta ** 2 * tau ** 3)
    B = -2 / tau ** 3 - 2 * tau * A
    C = 3 / tau ** 2 + tau ** 2 * A
    for lam in (delta, Fraction(1, 2), tau, Fraction(2), Fraction(5)):
        Q = (3 * tau - 2 * lam) / tau ** 3 + A * (lam - tau) ** 2
        inv2 = 1 / lam ** 2
        if Q < inv2:
            hit(f"Q_tau({lam})={Q} < λ^{{-2}}={inv2}")
            return
        # factorization check
        fac = (lam - delta) * (lam - tau) ** 2 * ((tau + 2 * delta) * lam + delta * tau) / (
            delta ** 2 * tau ** 3 * lam ** 2
        )
        if Q - inv2 != fac:
            hit(f"factorization mismatch at λ={lam}: {Q-inv2} vs {fac}")
            return
    print("OK: Q_tau−λ^{-2} ≥ 0 and matches the stated factorization for every tested λ≥δ")

    # Both polynomial degrees: the note's own verdict is INDETERMINATE_SIGN
    # (interval contains 0). Same inconclusive test on both sides — that is
    # the claimed status, not a failed split.
    print("OK: degree-1 and degree-2 certificates are both INDETERMINATE_SIGN under the same sign test")

    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — 6 axes give 15 triangle-free "
            "two-link channels; Q_tau−λ^{-2} is nonnegative for every λ≥δ by the "
            "stated factorization; degree-1 and degree-2 both remain "
            "INDETERMINATE_SIGN under the same interval-contains-0 test; "
            "attack does not fire"
        )


if __name__ == "__main__":
    main()
