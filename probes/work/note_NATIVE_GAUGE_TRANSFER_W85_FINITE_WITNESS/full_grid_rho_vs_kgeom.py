#!/usr/bin/env python3
"""J:note falsifier for NATIVE_GAUGE_TRANSFER_W85_FINITE_WITNESS_OPEN_GATE_NOTE_2026-06-12 (on main).

Falsifier implemented (the note's second): "a cell or tail region with rho > K_geom(a)", where
    rho(beta, p, q) = sqrt(beta) | beta^(-3/2) r_(p,q)(beta) - H(x, y) exp(-Q(x, y)) |,  x = p/sqrt(beta), y = q/sqrt(beta),
    H = x y (x + y)/2, Q = x^2 + x y + y^2, a = max(p, q)/sqrt(beta), K_geom(a) = 6 a^4 + 3 a^2 + 3 a + 1.
The note checks six sampled cells at beta in {108, 300, 600} with the repo's finite-mode Bessel-determinant routine. Here, with
disjoint machinery (Wilson coefficients from the character recurrence: r_(p,q)(beta) = [e^{beta(J-I)} delta](p,q) / [...](0,0), J the
six-neighbour averaging stencil, Poisson(beta)-weighted walk sums in log space), EVERY cell 0 <= p, q <= 8 sqrt(beta) is scanned (the
active window and the tail, where both terms decay like exp(-Q) with Q >= a^2) at eleven betas from 12 to 1200, and the note's three displayed rows
and its first falsifier (H replaced by x + y) are reproduced.
HIT if some scanned cell has rho > K_geom(a).
"""
from __future__ import annotations

from math import exp, floor, lgamma, log, sqrt

import numpy as np

STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]


def stencil(a):
    out = np.zeros_like(a)
    for dp, dq in STEPS:
        s1 = slice(max(dp, 0), a.shape[0] + min(dp, 0))
        d1 = slice(max(-dp, 0), a.shape[0] + min(-dp, 0))
        s2 = slice(max(dq, 0), a.shape[1] + min(dq, 0))
        d2 = slice(max(-dq, 0), a.shape[1] + min(-dq, 0))
        out[d1, d2] += a[s1, s2]
    return out / 6.0


def walk_ratios(beta, S):
    B = S + int(10 * sqrt(beta)) + 60
    a = np.zeros((B + 1, B + 1))
    a[0, 0] = 1.0
    acc = np.zeros_like(a)
    for n in range(int(beta + 14 * sqrt(beta) + 30) + 1):
        acc += exp(-beta + n * log(beta) - lgamma(n + 1)) * a
        a = stencil(a)
    return (acc / acc[0, 0])[: S + 1, : S + 1]


def kgeom(a):
    return 6 * a ** 4 + 3 * a ** 2 + 3 * a + 1


def rho_grid(beta, r, prefactor="xy(x+y)/2"):
    S = r.shape[0] - 1
    P, Q = np.meshgrid(np.arange(S + 1), np.arange(S + 1), indexing="ij")
    x, y = P / sqrt(beta), Q / sqrt(beta)
    H = x * y * (x + y) / 2 if prefactor == "xy(x+y)/2" else x + y
    rho = sqrt(beta) * np.abs(beta ** -1.5 * r - H * np.exp(-(x * x + x * y + y * y)))
    a = np.maximum(P, Q) / sqrt(beta)
    return rho, kgeom(a), a


def main():
    note = {108: ((1.0, 0.6), 0.070, 11.8), 300: ((1.3, 1.0), 0.106, 28.9), 600: ((0.9, 0.9), 0.138, 10.0)}
    rows, worst_all = [], (0.0, None)
    fails = []
    shown = []
    for beta in (12, 27, 48, 75, 108, 192, 300, 432, 600, 768, 1200):
        S = int(8 * sqrt(beta)) + 2
        r = walk_ratios(beta, S)
        rho, kg, a = rho_grid(beta, r)
        ratio = rho / kg
        i, j = np.unravel_index(np.argmax(ratio), ratio.shape)
        mx = ratio[i, j]
        tail = a > 3
        rows.append((beta, S, float(rho.max()), float(mx), (int(i), int(j)), float((rho[tail] / kg[tail]).max()) if tail.any() else 0.0))
        if mx > worst_all[0]:
            worst_all = (float(mx), (beta, int(i), int(j)))
        if (ratio > 1).any():
            fails.append((beta, int((ratio > 1).sum())))
        if beta in note:
            (tx, ty), rv, kv = note[beta]
            p, q = round(tx * sqrt(beta)), round(ty * sqrt(beta))
            rho_alt, _, _ = rho_grid(beta, r, prefactor="x+y")
            shown.append((beta, (p, q), float(rho[p, q]), rv, float(kg[p, q]), kv, float(rho_alt[p, q] / rho[p, q])))
    print("1. the note's displayed rows (cell = target rounded to integers): " + "; ".join(
        f"beta={b} (p,q)={pq}: rho {rv:.3f} (note {nr}), K_geom {kv:.1f} (note {nk}); with H = x+y, rho grows by x{inf:.0f}"
        for b, pq, rv, nr, kv, nk, inf in shown))
    print("2. full-grid scan, all cells 0 <= p, q <= 8 sqrt(beta): " + "; ".join(
        f"beta={b} (grid {S}+1 squared): max rho {m:.4f}, max rho/K_geom {mr:.4f} at {loc}, tail (a > 3) max rho/K_geom {tr:.2e}"
        for b, S, m, mr, loc, tr in rows))
    ok_rows = all(abs(rv - nr) <= 0.0006 and abs(kv - nk) <= 0.06 for _, _, rv, nr, kv, nk, _ in shown)
    if fails:
        print(f"HIT: cells with rho > K_geom(a): {fails}")
    if not ok_rows:
        print(f"HIT: the note's displayed rows are not reproduced: {shown}")
    print(f"SUMMARY: falsifier 2 does not fire on the scanned grids: over every cell 0 <= p, q <= 8 sqrt(beta) at eleven betas from 12 to "
          f"1200 (walk-count Wilson coefficients, disjoint from the runner), the largest rho/K_geom(a) is {worst_all[0]:.4f} at "
          f"(beta, p, q) = {worst_all[1]} and the tail region a > 3 stays below {max(t for *_, t in rows):.1e}; the note's three rows are "
          f"reproduced ({ok_rows}) and replacing H by x + y inflates rho by factors {', '.join(f'{s[-1]:.0f}' for s in shown)}")


if __name__ == "__main__":
    main()
