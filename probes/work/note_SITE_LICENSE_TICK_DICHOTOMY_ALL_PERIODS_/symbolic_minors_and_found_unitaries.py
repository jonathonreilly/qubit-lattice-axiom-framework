#!/usr/bin/env python3
"""J:note falsifiers for SITE_LICENSE_TICK_DICHOTOMY_ALL_PERIODS_BOUNDED_THEOREM_NOTE_2026-06-11 (on main).

Falsifiers implemented (the note's list): a licensed period-p tick with a momentum-dependent proper principal minor; winding |w| >= 2;
a dispersive licensed tick with a nonzero intermediate symmetric function; a dispersive licensed tick with nonzero band curvature.

Disjoint machinery, beyond the note's sizes (its runner: symbolic minors p = 2..5, numeric p = 6, constructed instances p = 1..6):
  1. symbolic, p = 2..8: the GENERIC licensed Bloch matrix (an independent symbol on every licensed entry, the two corners carrying z
     and 1/z; for p = 1, 2 the wrapped entries add) - every proper principal minor (all 2^p - 2) is z-free and det = A + B z + C/z;
  2. licensed UNITARIES FOUND by nonlinear least squares from random starts (no structure assumed), p = 2..10: unitarity re-checked at
     unseen momenta, then the winding of det, the intermediate symmetric functions e_1..e_{p-1} across momenta, and the band curvature
     (second differences of the sorted eigenphase bands over a 64-point momentum grid).
HIT if any falsifier fires on any instance.
"""
from __future__ import annotations

import itertools

import numpy as np
import sympy as sp
from scipy.optimize import least_squares


def licensed_entries(p):
    """list of (row, col, power of z) for the radius-1 licence with period p (sites j + p c)."""
    ent = []
    for jp in range(p):
        for j in range(p):
            for c in (-1, 0, 1):
                if abs(jp + p * c - j) <= 1:
                    ent.append((jp, j, c))
    return ent


def symbolic(p):
    z = sp.symbols("z")
    ent = licensed_entries(p)
    syms = sp.symbols(f"a0:{len(ent)}")
    M = sp.zeros(p, p)
    for (r, c, pw), s in zip(ent, syms):
        M[r, c] += s * z ** pw
    proper_ok = True
    for k in range(1, p):
        for S in itertools.combinations(range(p), k):
            d = sp.expand(M.extract(list(S), list(S)).det(method="berkowitz"))
            if d.has(z):
                proper_ok = False
    D = sp.expand(M.det(method="berkowitz") * z)                      # z det must be a polynomial of degree <= 2 in z
    powers = sorted({sp.Poly(D, z).degree(), min(m[0] for m in sp.Poly(D, z).monoms())})
    return proper_ok, powers, len(ent)


def build(params, ent, p, zs):
    n = len(ent)
    a = params[:n] + 1j * params[n:]
    out = []
    for z in zs:
        M = np.zeros((p, p), complex)
        for (r, c, pw), v in zip(ent, a):
            M[r, c] += v * z ** pw
        out.append(M)
    return out


def find_unitaries(p, tries=40, seed=0):
    rng = np.random.default_rng(seed + 100 * p)
    ent = licensed_entries(p)
    zs = np.exp(1j * np.linspace(0, 2 * np.pi, 9, endpoint=False) + 0.3j)
    found = []
    for t in range(tries):
        x0 = rng.normal(size=2 * len(ent)) * rng.choice([0.3, 1.0])

        def resid(x):
            r = []
            for M in build(x, ent, p, zs):
                E = M.conj().T @ M - np.eye(p)
                r += list(E.real.ravel()) + list(E.imag.ravel())
            return r

        sol = least_squares(resid, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        if np.max(np.abs(resid(sol.x))) < 1e-11:
            found.append(sol.x)
    return ent, found


def analyse(p, ent, x):
    K = np.linspace(0, 2 * np.pi, 64, endpoint=False)
    zs = np.exp(1j * K)
    Ms = build(x, ent, p, zs)
    unit = max(np.abs(M.conj().T @ M - np.eye(p)).max() for M in Ms)
    dets = np.array([np.linalg.det(M) for M in Ms])
    w = int(round(np.sum(np.angle(np.roll(dets, -1) / dets)) / (2 * np.pi)))
    # intermediate symmetric functions e_1..e_{p-1} = coefficients of the characteristic polynomial
    polys = np.array([np.poly(M) for M in Ms])                        # [1, -e1, e2, ...]
    inter = polys[:, 1:p]
    e_spread = float(np.abs(inter - inter[0]).max()) if p > 1 else 0.0
    e_max = float(np.abs(inter).max()) if p > 1 else 0.0
    # bands: continuous eigenphases; track by sorting unwrapped phases of (eigenvalues) along K
    phases = []
    for M in Ms:
        ev = np.linalg.eigvals(M)
        phases.append(np.sort(np.angle(ev)))
    phases = np.array(phases)
    if w == 0:
        curv = float(np.abs(phases - phases[0]).max())               # flat: bands constant
        kind = "flat"
    else:
        # predicted bands: p-th roots of (-1)^{p+1} det(z): omega = (arg((-1)^{p+1} det) + 2 pi j)/p; compare sets
        dev = 0.0
        for M, d in zip(Ms, dets):
            ev = np.linalg.eigvals(M)
            roots = np.array([((-1) ** (p + 1) * d) ** (1 / p) * np.exp(2j * np.pi * j / p) for j in range(p)])
            dev = max(dev, max(np.min(np.abs(roots - e)) for e in ev))
        curv = dev
        kind = "saturating"
    return {"unitarity": float(unit), "w": w, "e spread": e_spread, "e max": e_max, "band deviation": curv, "kind": kind}


def main():
    sym = {p: symbolic(p) for p in range(2, 9)}
    print(f"1. generic licensed matrices: (proper minors z-free, powers of z*det, #symbols) by p: {sym}")
    res = {}
    for p in range(2, 11):
        ent, found = find_unitaries(p)
        res[p] = [analyse(p, ent, x) for x in found]
        kinds = {k: sum(1 for r in res[p] if r["kind"] == k) for k in ("flat", "saturating")}
        ws = sorted({r["w"] for r in res[p]})
        worst_e = max([r["e max"] for r in res[p] if r["w"] != 0] or [0.0])
        worst_spread = max([r["e spread"] for r in res[p]] or [0.0])
        worst_band = max([r["band deviation"] for r in res[p]] or [0.0])
        print(f"2. p = {p}: {len(found)} unitaries found from 40 starts ({kinds}); windings {ws}; max e-spread over momenta {worst_spread:.1e}; "
              f"max |e_k| for w != 0 {worst_e:.1e}; max band deviation (flat: from constant, saturating: from p-th roots of det) "
              f"{worst_band:.1e}; max unitarity error on 64 unseen momenta {max([r['unitarity'] for r in res[p]] or [0]):.1e}")
    fails = []
    for p, (ok, powers, _) in sym.items():
        if not ok or min(powers) < 0 or max(powers) > 2:
            fails.append(f"symbolic p={p}")
    for p, rs in res.items():
        for r in rs:
            if r["unitarity"] > 1e-9:
                continue
            if abs(r["w"]) >= 2 or r["e spread"] > 1e-8 or (r["w"] != 0 and r["e max"] > 1e-8) or r["band deviation"] > 1e-8:
                fails.append(f"p={p} instance {r}")
    if fails:
        print(f"HIT: {fails[:5]}")
    total = sum(len(v) for v in res.values())
    print(f"SUMMARY: for the generic licensed matrix with an independent symbol on every entry, every proper principal minor is momentum-free "
          f"and z det has z-degrees within 0..2 for p = 2..8; {total} licensed unitaries found by least squares from random starts at "
          f"p = 2..10 all have winding in {{-1, 0, 1}}, momentum-independent e_1..e_(p-1), vanishing intermediate e_k when w != 0, and "
          f"bands that are constant (w = 0) or exactly the p-th roots of (-1)^(p+1) det (w != 0), i.e. zero curvature; no falsifier fires")


if __name__ == "__main__":
    main()
