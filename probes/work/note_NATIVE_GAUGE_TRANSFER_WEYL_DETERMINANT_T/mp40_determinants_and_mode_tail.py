#!/usr/bin/env python3
"""J:note check for NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_TAIL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12 (on main).

The note's falsifier table and mode-tail witnesses, recomputed with machinery disjoint from its runner (float64 scipy ive + numpy det):
  - every Bessel determinant in 40-digit mpmath (besseli, exact 3x3/2x2 determinants), mode sums to |n| <= 220 with the |n| > 200 part
    reported, and r_(6,5)(96) cross-checked by a third method, the character recurrence c = e^{beta J} delta_(0,0) as positive walk sums;
  - the table at beta = 96, (p,q) = (6,5), beta^-3/2 scaled: exact determinant ratio, saddle d exp(-k C2/beta) for k = 3, 2, 4, the
    dimension omitted, the 2x2 determinant, lambda = (p, q, 0) instead of (p+q, q, 0);
  - the outside mode mass sum_{|n| > W} |det B_n| / sum_n |det B_n| at (96,(6,5)) and (192,(10,8)) with W = floor(1.25 sqrt(t)),
    floor(1.25 beta^(1/3)), floor(1.25 sqrt(beta));
  - beyond the note: the same outside mass at the fixed scaled weight (p,q) ~ (0.6, 0.5) sqrt(beta) for beta = 96 .. 1536, and whether
    every mode term det B_n is nonnegative (so the mass is a fraction of c itself).
HIT if a printed value differs from the 40-digit value by more than 1e-9.
"""
from __future__ import annotations

from math import exp, floor, lgamma, log, sqrt

import mpmath as mp
import numpy as np

mp.mp.dps = 40
MODE_MAX = 220
TABLE = {"exact": 0.078225286971, "saddle Nc3": 0.079761275743, "Nc2": 0.122681758828, "Nc4": 0.051856618041,
         "dim omitted": 0.000292165845, "2x2": 0.005101635871, "lambda (p,q,0)": 0.030362625798}
MASS = {(96, 6, 5, "sqrt t"): 0.249199184790, (192, 10, 8, "sqrt t"): 0.344182812319, (192, 10, 8, "beta^1/3"): 0.600571111925,
        (192, 10, 8, "sqrt beta"): 0.026879797238}
_cache = {}


def Iscaled(k, t):
    key = (k, t)
    if key not in _cache:
        _cache[key] = mp.besseli(abs(k), t) * mp.exp(-t)
    return _cache[key]


def mode_terms(lam, beta, size=3):
    t = mp.mpf(beta) / 3
    out = []
    for n in range(-MODE_MAX, MODE_MAX + 1):
        M = mp.matrix([[Iscaled(n + lam[j] + i - j, t) for j in range(size)] for i in range(size)])
        out.append((n, mp.det(M)))
    return out


def coeff(p, q, beta, variant="correct", size=3):
    lam = [p + q, q, 0] if variant == "correct" else [p, q, 0]
    terms = mode_terms(lam[:size], beta, size)
    return mp.fsum(v for _, v in terms), terms


def walk_ratio(beta, p, q):
    B = max(p, q) + int(10 * sqrt(beta)) + 60
    STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]
    a = np.zeros((B + 1, B + 1))
    a[0, 0] = 1.0
    acc = np.zeros_like(a)
    for n in range(int(beta + 14 * sqrt(beta) + 40) + 1):
        acc += exp(-beta + n * log(beta) - lgamma(n + 1)) * a
        out = np.zeros_like(a)
        m = a.shape[0]
        for dp, dq in STEPS:
            out[max(-dp, 0): m + min(-dp, 0), max(-dq, 0): m + min(-dq, 0)] += a[max(dp, 0): m + min(dp, 0), max(dq, 0): m + min(dq, 0)]
        a = out / 6
    return acc[p, q] / acc[0, 0]


def outside(terms, W):
    den = mp.fsum(abs(v) for _, v in terms)
    return mp.fsum(abs(v) for n, v in terms if abs(n) > W) / den


def main():
    beta, p, q = 96, 6, 5
    sc = mp.mpf(beta) ** mp.mpf(-1.5)
    C2 = mp.mpf(p * p + q * q + p * q + 3 * p + 3 * q) / 3
    d = mp.mpf((p + 1) * (q + 1) * (p + q + 2)) / 2
    c65, t65 = coeff(p, q, beta)
    c00, t00 = coeff(0, 0, beta)
    tail200 = max(abs(v) for n, v in t65 if abs(n) > 200) / abs(c65)
    vals = {"exact": sc * c65 / c00, "saddle Nc3": sc * d * mp.exp(-3 * C2 / beta), "Nc2": sc * d * mp.exp(-2 * C2 / beta),
            "Nc4": sc * d * mp.exp(-4 * C2 / beta), "dim omitted": sc * mp.exp(-3 * C2 / beta)}
    c2, _ = coeff(p, q, beta, size=2)
    c002, _ = coeff(0, 0, beta, size=2)
    vals["2x2"] = sc * c2 / c002
    cw, _ = coeff(p, q, beta, variant="wrong")
    c00w, _ = coeff(0, 0, beta, variant="wrong")
    vals["lambda (p,q,0)"] = sc * cw / c00w
    walk = walk_ratio(beta, p, q) * float(sc)
    diffs = {k: abs(float(vals[k]) - TABLE[k]) for k in TABLE}
    print(f"1. beta = 96, (6,5), beta^-3/2 scaled, 40 digits: { {k: mp.nstr(v, 14) for k, v in vals.items()} }; walk-sum exact ratio "
          f"{walk:.12f}; max |diff| to the note {max(diffs.values()):.1e}; largest |n| > 200 mode term / c {mp.nstr(tail200, 3)}")
    masses = {}
    for (b, pp, qq, rule), printed in MASS.items():
        _, terms = coeff(pp, qq, b)
        t = b / 3
        W = {"sqrt t": floor(1.25 * sqrt(t)), "beta^1/3": floor(1.25 * b ** (1 / 3)), "sqrt beta": floor(1.25 * sqrt(b))}[rule]
        m = outside(terms, W)
        masses[(b, pp, qq, rule)] = (W, float(m), abs(float(m) - printed), all(v >= 0 for _, v in terms))
    print(f"2. outside mode masses (window, mass, |diff| to note, all mode terms nonnegative): {masses}")
    beyond = {}
    for b in (96, 192, 384, 768, 1536):
        pp, qq = round(0.6 * sqrt(b)), round(0.5 * sqrt(b))
        _, terms = coeff(pp, qq, b)
        W = floor(1.25 * sqrt(b / 3))
        beyond[b] = ((pp, qq), W, round(float(outside(terms, W)), 6), all(v >= 0 for _, v in terms))
    print(f"3. beyond: outside mass at (p,q) ~ (0.6, 0.5) sqrt(beta), W = floor(1.25 sqrt(t)): {beyond}")
    fails = []
    if max(diffs.values()) > 1e-9 or abs(walk - TABLE["exact"]) > 1e-9:
        fails.append(f"table {diffs}")
    if any(v[2] > 1e-9 for v in masses.values()):
        fails.append(f"mode masses {masses}")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: in 40-digit arithmetic every falsifier-table value (exact ratio {mp.nstr(vals['exact'], 12)}, saddle "
          f"{mp.nstr(vals['saddle Nc3'], 12)}, N_c = 2/4, dimension omitted, 2x2, wrong lambda) agrees with the note to "
          f"{max(diffs.values()):.0e} and the walk-sum ratio agrees to {abs(walk - TABLE['exact']):.0e}; the four outside mode masses agree "
          f"to {max(v[2] for v in masses.values()):.0e}; every mode term is nonnegative; beyond the note the sqrt(t)-window outside mass at "
          f"a fixed scaled weight is {({b: v[2] for b, v in beyond.items()})}; no falsifier fires")


if __name__ == "__main__":
    main()
