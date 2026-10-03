#!/usr/bin/env python3
"""Lattice Ampere check on hinge-free periodic facets: record slab {(n.r) mod L in [0,w)} on an
L^3 torus.  Prediction (derivation D17): net items per cycle crossing the plane r_t = c near the
+n face = L (M x n)_t, near the -n face = -L (M x n)_t, with M the bulk loop-area vector per site."""
import numpy as np, time
from cyc3d import *

t0 = time.time()

def flux_vec(L, pi, axis, cval, region):
    xyz = np.array(coords3(L), dtype=float)
    mv = np.nonzero(pi != np.arange(L ** 3))[0]
    p0 = xyz[:, mv]
    dp = mi(xyz[:, pi[mv]] - p0, L)
    a0, da = p0[axis], dp[axis]
    nz = da != 0
    cv = a0 + mi(cval - a0, L)
    t = np.where(nz, (cv - a0) / np.where(nz, da, 1), -1)
    hit = nz & (t > 0) & (t < 1)
    pt = p0 + t[None] * dp
    sel = hit & region(pt)
    return int(np.sign(da[sel]).sum()), int(np.abs(dp).max(initial=0))

M = {"layer-z": np.array([0, 0, -1]), "C3-cycle": np.array([2, 2, 2])}
for name, sch in [("layer-z", LAYER_Z), ("C3-cycle", C3CYC)]:
    for n, L, w in [((1, 0, 0), 16, 4), ((0, 1, 0), 16, 4), ((0, 0, 1), 16, 4),
                    ((1, 0, 2), 32, 8), ((1, 2, 3), 48, 14), ((2, -1, 1), 32, 8)]:
        n = np.array(n)
        x, y, z = coords3(L)
        v = (n[0] * x + n[1] * y + n[2] * z) % L
        J = v < w
        pi, _ = run3(L, J, sch)
        half = (L - w) / 2.0
        plus = lambda p: ((n @ p - (w - 0.5)) % L) < half
        minus = lambda p: ((n @ p - (w - 0.5)) % L) >= half
        pred = L * np.cross(M[name], n)
        got_p, got_m = [], []
        for t in range(3):
            fp, dmax = flux_vec(L, pi, t, 0.3, plus)
            fm, _ = flux_vec(L, pi, t, 0.3, minus)
            got_p.append(fp); got_m.append(fm)
        ok = np.array_equal(got_p, pred) and np.array_equal(got_m, -pred)
        print(f"{name} slab n={tuple(n)} L={L}: +n face flux (x,y,z) = {tuple(got_p)}, -n face = {tuple(got_m)}; "
              f"predicted +n = {tuple(pred)} -> match {ok}; max |move| {dmax}")
print(f"time {time.time()-t0:.1f}s")
