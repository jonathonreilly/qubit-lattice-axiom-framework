#!/usr/bin/env python3
"""J:attack-e:PR8156 — pattern (e) SAMPLED EVIDENCE.

C1 checks 1-cos u ≥ 11 u^2/24 at 21 points of [-1,1] and 1-cos u ≥ 2u^2/π^2
at 21 points of [-π,π]. C3 checks 1-φ ≥ (11/72)|k|^2 at four wavevectors with
|k|_∞≤1 and ≥ 2/(3π^2) at five with |k|_∞>1.

Instead of more samples: a dense grid plus coordinate hill-climb, looking
for a point in the stated range where an inequality fails. HIT if a witness
in range has a negative margin (beyond cancellation at the origin).
"""
from __future__ import annotations

import math
from itertools import product

import numpy as np

HITS: list[str] = []
RNG = np.random.default_rng(8156)


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def hillclimb_1d(fun, lo, hi, starts, steps=80, step0=None):
    """Maximize fun (so we feed it the negative margin)."""
    step0 = (hi - lo) / 20 if step0 is None else step0
    best_x, best_v = None, -np.inf
    for x0 in starts:
        x = float(np.clip(x0, lo, hi))
        step = step0
        v = fun(x)
        for _ in range(steps):
            improved = False
            for dx in (step, -step):
                y = float(np.clip(x + dx, lo, hi))
                vy = fun(y)
                if vy > v:
                    x, v = y, vy
                    improved = True
                    break
            if not improved:
                step *= 0.5
                if step < 1e-16 * (1 + abs(hi - lo)):
                    break
        if v > best_v:
            best_x, best_v = x, v
    return best_x, best_v


def margin_quart(u):
    if abs(u) < 1e-12:
        return 0.0
    return (1.0 - math.cos(u)) - (11.0 / 24.0) * u * u


def margin_chord(u):
    if abs(u) < 1e-12:
        return 0.0
    return (1.0 - math.cos(u)) - (2.0 * u * u) / (math.pi ** 2)


def phi(k):
    return (math.cos(k[0]) + math.cos(k[1]) + math.cos(k[2])) / 3.0


def margin_small(k):
    r2 = k[0] ** 2 + k[1] ** 2 + k[2] ** 2
    return (1.0 - phi(k)) - (11.0 / 72.0) * r2


def margin_large(k):
    return (1.0 - phi(k)) - 2.0 / (3.0 * math.pi ** 2)


def hillclimb_3d(fun, box, starts, steps=60):
    lo, hi = box
    best_k, best_v = None, -np.inf
    for k0 in starts:
        k = np.clip(np.array(k0, dtype=float), lo, hi)
        step = 0.15 * (hi - lo)
        v = fun(k)
        for _ in range(steps):
            improved = False
            for i in range(3):
                for s in (step, -step):
                    cand = k.copy()
                    cand[i] = float(np.clip(k[i] + s, lo, hi))
                    vc = fun(cand)
                    if vc > v:
                        k, v = cand, vc
                        improved = True
            if not improved:
                step *= 0.5
                if step < 1e-12:
                    break
        if v > best_v:
            best_k, best_v = k, v
    return best_k, best_v


def main() -> int:
    # --- C1 quartic bound on [-1,1]: adversarial min of the margin ---
    grid = np.linspace(-1.0, 1.0, 4001)
    gvals = np.array([margin_quart(u) for u in grid])
    gmin = float(np.min(gvals[np.abs(grid) > 1e-8]))
    starts = list(grid[np.argsort(gvals)[:15]]) + list(RNG.uniform(-1, 1, 20))
    hx, hv = hillclimb_1d(lambda u: -margin_quart(u), -1.0, 1.0, starts)
    print(f"C1 quartic: grid min margin (away from 0)={gmin:.6e}; hill-climb worst at u={hx:.12f} margin={-hv:.6e}")
    if gmin < -1e-12 or -hv < -1e-12:
        hit(f"1-cos u < 11 u^2/24 on |u|<=1: u={hx} margin={-hv}")

    # --- C1 chord bound on [-pi,pi] ---
    gridp = np.linspace(-math.pi, math.pi, 8001)
    cvals = np.array([margin_chord(u) for u in gridp])
    cmin = float(np.min(cvals[np.abs(gridp) > 1e-8]))
    starts = list(gridp[np.argsort(cvals)[:15]]) + list(RNG.uniform(-math.pi, math.pi, 20))
    hx, hv = hillclimb_1d(lambda u: -margin_chord(u), -math.pi, math.pi, starts)
    print(f"C1 chord: grid min margin={cmin:.6e}; hill-climb worst at u={hx:.12f} margin={-hv:.6e}")
    if cmin < -1e-12 or -hv < -1e-12:
        hit(f"1-cos u < 2u^2/pi^2 on [-pi,pi]: u={hx} margin={-hv}")

    # --- C3 small box |k|_inf <= 1: 1-phi >= (11/72)|k|^2 ---
    axis = np.linspace(-1.0, 1.0, 21)
    worst_s = 0.0
    worst_sk = (0.0, 0.0, 0.0)
    for p in product(axis, repeat=3):
        m = margin_small(p)
        if m < worst_s:
            worst_s, worst_sk = m, p
    starts = [worst_sk] + [RNG.uniform(-1, 1, 3) for _ in range(40)]
    hk, hv = hillclimb_3d(lambda k: -margin_small(k), (-1.0, 1.0), starts)
    print(f"C3 small: 21^3 min margin={worst_s:.6e} at {worst_sk}; hill-climb worst {hk} margin={-hv:.6e}")
    if worst_s < -1e-12 or -hv < -1e-12:
        hit(f"1-phi < (11/72)|k|^2 in |k|_inf<=1 at {hk} margin={-hv}")

    # --- C3 large: |k|_inf in (1, pi], 1-phi >= 2/(3 pi^2) ---
    # adversarial: minimize 1-phi on the region |k|_inf > 1 inside [-pi,pi]^3
    # the bound is constant, so this is min (1-phi) vs 2/(3pi^2)
    bound = 2.0 / (3.0 * math.pi ** 2)
    axis_l = np.concatenate(
        [
            np.linspace(-math.pi, -1.0, 12, endpoint=False),
            np.linspace(1.0, math.pi, 12),
            np.linspace(-1.0, 1.0, 9),
        ]
    )
    worst_l = 1.0
    worst_lk = None
    nchecked = 0
    for p in product(axis_l, repeat=3):
        if max(abs(p[0]), abs(p[1]), abs(p[2])) <= 1.0:
            continue
        nchecked += 1
        m = 1.0 - phi(p)
        if m < worst_l:
            worst_l, worst_lk = m, p
    starts = [np.array(worst_lk)] + [RNG.uniform(-math.pi, math.pi, 3) for _ in range(50)]
    # project starts into the large region
    starts_l = []
    for s in starts:
        s = np.clip(s, -math.pi, math.pi)
        if max(abs(s)) <= 1.0:
            s[int(np.argmax(np.abs(s)))] = 1.0 + 1e-6 if s[int(np.argmax(np.abs(s)))] >= 0 else -1.0 - 1e-6
        starts_l.append(s)

    def fun_large(k):
        if max(abs(float(k[0])), abs(float(k[1])), abs(float(k[2]))) <= 1.0:
            return -np.inf
        return -margin_large(k)

    hk, hv = hillclimb_3d(fun_large, (-math.pi, math.pi), starts_l)
    print(
        f"C3 large: {nchecked} grid pts min(1-phi)={worst_l:.6e} vs bound {bound:.6e}; "
        f"hill-climb worst {hk} margin={-hv:.6e}"
    )
    if worst_l + 1e-12 < bound or -hv < -1e-12:
        hit(f"1-phi < 2/(3 pi^2) on |k|_inf>1 at {hk} 1-phi={-hv + bound} bound={bound}")

    # named sample points of C3, for the record
    pts_small = [(0.5, 1 / 3, -0.75), (1, 1, 1), (0, 0.9, 0), (-1, 0.2, 0.5)]
    pts_large = [
        (math.pi, 0, 0),
        (1.5, 0.5, 0),
        (2, 2, 2),
        (math.pi, math.pi, math.pi),
        (1.1, -math.pi / 2, math.pi / 3),
    ]
    print("C3 named small:", [margin_small(p) for p in pts_small])
    print("C3 named large:", [margin_large(p) for p in pts_large])

    if HITS:
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - adversarial grid plus "
        "hill-climb on C1's two cosine inequalities (4001+8001-point grids) and "
        "C3's two-region symbol (21^3 small box; large-region grid) finds no "
        "in-range witness below the stated bounds; the 21+21 sample points "
        "and nine sample wavevectors are not hiding a failure"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
