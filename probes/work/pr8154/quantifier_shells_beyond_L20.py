#!/usr/bin/env python3
"""J:attack-d:PR8154 — QUANTIFIER SCOPE.

H2(a) shell counts 8j (j<L) and 4L-1 (j=L) are for every even-side torus
side 2L. Attack-g executed L=2..20. Extra L=21..32, plus the harmonic
lower bound sum_{n!=0} 1/|n|^2 >= 4 H_{L-1}. HIT if a count or the
inequality fails inside the stated all-L range.
"""
from __future__ import annotations

from fractions import Fraction as F

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def harmonic(m: int) -> F:
    return sum((F(1, k) for k in range(1, m + 1)), F(0))


def main() -> int:
    for L in range(21, 33):
        rng = range(-L + 1, L + 1)
        buckets = {}
        s = F(0)
        for n1 in rng:
            for n2 in rng:
                if n1 == 0 and n2 == 0:
                    continue
                j = max(abs(n1), abs(n2))
                buckets[j] = buckets.get(j, 0) + 1
                s += F(1, n1 * n1 + n2 * n2)
        for j in range(1, L):
            n = buckets.get(j, 0)
            if n != 8 * j:
                hit(f"L={L} j={j}: |shell|={n} != 8j={8 * j}")
        nL = buckets.get(L, 0)
        if nL != 4 * L - 1:
            hit(f"L={L} j=L: |shell|={nL} != 4L-1={4 * L - 1}")
        lo = 4 * harmonic(L - 1)
        ok = s >= lo
        print(f"L={L} j=L shell={nL} (4L-1={4 * L - 1}); sum 1/|n|^2={s} >= 4 H_{L-1}={lo}: {ok}")
        if not ok:
            hit(f"L={L}: sum 1/|n|^2={s} < 4 H_{L-1}={lo}")
    if HITS:
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - H2 shell counts 8j "
        "and 4L-1 and the bound sum 1/|n|^2 >= 4 H_{L-1} hold for every extra "
        "L=21..32 beyond the executed L<=20"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
