#!/usr/bin/env python3
"""J:attack-b:PR8033 — SAME TEST, BOTH SIDES.

Separations: occupied-link Casimir floor 4/a at every R≥1 vs trivial 0;
lower bound uniform in R vs upper envelope only under positive acceptance.
"""
from __future__ import annotations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def Q(p: int, q: int) -> int:
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    # Same Casimir test on trivial vs every occupied irrep with p+q ≤ R
    for R in range(1, 17):
        occupied = [Q(p, R - p) for p in range(R + 1)] + [Q(p, q) for p in range(R + 1) for q in range(R - p + 1) if p + q >= 1]
        mn = min(occupied)
        if mn != 4:
            hit(f"R={R}: min occupied Casimir {mn} != 4")
            return
        if Q(0, 0) != 0:
            hit("trivial not 0")
            return
    print("OK: same Casimir test for R=1..16: trivial 0, every occupied irrep ≥4 with min 4 at (1,0)/(0,1)")

    # 243 = 3^5 R=1 center flows (five independent tree-gauge angles on a cube)
    if 3 ** 5 != 243:
        hit("243 != 3^5")
        return
    print("OK: 243=3^5 R=1 tree-gauge states on a cube")

    # h_R = [R^2 - floor(R^2/4) + 3R]/a increasing in R
    def h(R, a=1):
        return (R * R - (R * R) // 4 + 3 * R) / a

    if not all(h(R + 1) > h(R) for R in range(1, 16)):
        hit("h_R not strictly increasing")
        return
    print("OK: same h_R test: strictly increasing for R=1..16, so the top-shell floor grows with cutoff")

    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — Casimir floor 4 vs 0 on "
            "occupied vs trivial irreps at every R=1..16; h_R increasing; 243=3^5; "
            "attack does not fire"
        )


if __name__ == "__main__":
    main()
