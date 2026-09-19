#!/usr/bin/env python3
"""J:attack-e:PR8153 — SAMPLED EVIDENCE.

C1 executes 1-cos u ≥ 2u²/π² at sample points. Instead of more samples:
Jordan sin x ≥ 2x/π on [0,π/2] implies 1-cos u = 2 sin²(u/2) ≥ 2(u/π)²
on [0,π], plus a dense grid and critical-point scan of
g(u)=π²(1-cos u)-2u². HIT if g<0 anywhere in [0,π].
"""
from __future__ import annotations

from fractions import Fraction
from math import cos, pi, sin

HITS: list[str] = []


def g(u: float) -> float:
    return pi * pi * (1 - cos(u)) - 2 * u * u


def main() -> int:
    # Jordan: sin x ≥ 2x/π on [0, π/2], equality at 0 and π/2.
    # Check at endpoints and a mid point that the discrete samples of
    # h(x)=sin x - 2x/π stay nonnegative; then 1-cos u = 2 sin²(u/2) ≥ 2(u/π)².
    xs = [i * pi / (2 * 400) for i in range(401)]
    hmin = min(sin(x) - 2 * x / pi for x in xs)
    print(f"Jordan sin x - 2x/π min on 400-grid [0,π/2] = {hmin}")
    if hmin < -1e-15:
        HITS.append(f"Jordan sample min {hmin} < 0")
    # g at 0, π, and dense grid
    gmin = min(g(i * pi / 800) for i in range(801))
    print(f"g(u)=π²(1-cos u)-2u² min on 800-grid [0,π] = {gmin}")
    print(f"g(0)={g(0)} g(π)={g(pi)}")
    if gmin < -1e-12:
        HITS.append(f"g min {gmin} < 0 on the grid")
    # critical points of g: g'=π² sin u - 4u = 0. Scan sign changes of g'.
    def gp(u):
        return pi * pi * sin(u) - 4 * u

    crit = []
    for i in range(800):
        a, b = i * pi / 800, (i + 1) * pi / 800
        if gp(a) == 0:
            crit.append(a)
        elif gp(a) * gp(b) < 0:
            lo, hi = a, b
            for _ in range(60):
                m = (lo + hi) / 2
                if gp(lo) * gp(m) <= 0:
                    hi = m
                else:
                    lo = m
            crit.append((lo + hi) / 2)
    print(f"critical points of g: {len(crit)}")
    for u in crit:
        val = g(u)
        print(f"  u={u:.12f} g={val}")
        if val < -1e-12:
            HITS.append(f"g({u})={val} < 0")
    # exact endpoints: g(0)=0; g(π)=π²(1-(-1))-2π²=2π²-2π²=0
    if abs(g(0)) > 1e-15 or abs(g(pi)) > 1e-9:
        HITS.append(f"endpoint g(0)={g(0)} g(π)={g(pi)} not 0")
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: SAMPLED EVIDENCE (PR #8153): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8153): C1's 1-cos u≥2u²/π² is a proved "
        "Jordan consequence (equality at 0 and π), not a never/always from "
        "random samples; grid and critical-point scan of π²(1-cos u)-2u² stay "
        "nonnegative on [0,π]; pattern has purchase and does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
