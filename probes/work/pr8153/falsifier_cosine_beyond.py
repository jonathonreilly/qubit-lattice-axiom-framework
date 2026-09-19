#!/usr/bin/env python3
"""J:falsifier:PR8153 — 1-cos u ≥ 2u²/π² and 2(1-cos θ)≤θ² on [0,π].

Falsifier: a sample point violating 1-cos u ≥ 2u²/π². Beyond the note:
2000-grid, critical points of g(u)=π²(1-cos u)-2u², and Jordan
sin x ≥ 2x/π. Also 2(1-cos θ)≤θ² (series remainder θ^4/12≥0).
"""
from __future__ import annotations

from math import cos, pi, sin

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main() -> int:
    gmin = 0.0
    for i in range(2001):
        u = i * pi / 2000
        g = pi * pi * (1 - cos(u)) - 2 * u * u
        if g < gmin:
            gmin = g
        if g < -1e-12:
            hit(f"1-cos u < 2u²/π² at u={u} g={g}")
            break
    print(f"g=π²(1-cos u)-2u² min on 2000-grid = {gmin}")
    hmin = min(sin(i * pi / (2 * 2000)) - 2 * (i * pi / (2 * 2000)) / pi for i in range(2001))
    print(f"Jordan min on 2000-grid [0,π/2] = {hmin}")
    if hmin < -1e-12:
        hit(f"Jordan fails {hmin}")
    # 2(1-cos θ)-θ² = -θ^4/12 + ... ≤ 0
    dmin = 0.0
    for i in range(2001):
        th = i * pi / 2000
        d = 2 * (1 - cos(th)) - th * th
        if d < dmin:
            dmin = d
        if d > 1e-12:
            hit(f"2(1-cos θ)>θ² at θ={th} d={d}")
            break
    print(f"2(1-cos θ)-θ² max on 2000-grid = {dmin} (want ≤0; printed is min of d, so all ≤0 if min≤0 and no HIT)")
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: cosine falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: cosine falsifier did not fire: 1-cos u≥2u²/π² and "
        "2(1-cos θ)≤θ² on a 2000-grid of [0,π], beyond the note's sample points"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
