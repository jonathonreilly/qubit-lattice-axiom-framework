#!/usr/bin/env python3
"""Shapes, nesting and random record patterns (confined to a central disc of an L=40 torus).
For every locked site P and every free plaquette centre Q in the disc:
  rho_A   = rotation number around the point from the items' sub-step paths (all items, R=17)
  rho_S   = rotation number around the point from the full-cycle chords s -> pi[s] only
  mu      = rho_A - rho_S  (winding of the closed loops 'path + chord back')
Predictions (derivation D6-D8): rho_A = -1 everywhere (any pattern); rho_S = -1 at record
points with mu = 0; rho_S = 0 at open points whose only encircling loop is their own plaquette loop."""
import numpy as np, math, time
from cyc2d import *

t0 = time.time()
L = 64; C = 32.0; Rdisc = 9.0; Rsum = 29.0
xs, ys = coords(L)
rng = np.random.default_rng(11)

def disc_mask():
    return (xs - C) ** 2 + (ys - C) ** 2 <= Rdisc ** 2

def pattern(kind):
    lk = np.zeros(L * L, bool)
    if kind == "Lshape":
        lk |= box(L, 26, 26, 9, 3); lk |= box(L, 26, 29, 3, 6)
    elif kind == "plus":
        lk |= box(L, 30, 25, 3, 13); lk |= box(L, 25, 30, 13, 3)
    elif kind == "staircase":
        for k in range(8):
            lk |= box(L, 26 + k, 26 + k, 3, 1)
    elif kind == "shell+cavity+island":
        lk |= box(L, 24, 24, 16, 16); lk &= ~box(L, 26, 26, 12, 12); lk |= box(L, 30, 30, 4, 4)
    elif kind == "two islands":
        lk |= box(L, 25, 29, 4, 5); lk |= box(L, 34, 28, 5, 4)
    elif kind.startswith("random 0"):
        dens = float(kind.split()[1])
        lk = (rng.random(L * L) < dens) & disc_mask()
    elif kind == "random rects":
        for _ in range(5):
            w, h = rng.integers(1, 6, 2); x0, y0 = rng.integers(25, 36, 2)
            lk |= box(L, int(x0), int(y0), int(w), int(h))
        lk &= disc_mask()
    return lk

def rho_at(pi, path, c):
    rA = rho_paths(L, path, c, Rsum)
    rS, mx = rho_straight(L, pi, c)
    return rA, rS, mx

kinds = ["Lshape", "plus", "staircase", "shell+cavity+island", "two islands",
         "random rects", "random 0.08", "random 0.25", "random 0.5"]
for kind in kinds:
    lk = pattern(kind)
    pi, path = run_cycle(L, lk)
    mv = np.nonzero(pi != np.arange(L * L))[0]
    far = np.all((xs[mv] - C) ** 2 + (ys[mv] - C) ** 2 < (Rsum - 4) ** 2)
    orb = orbits(pi)
    hist_rec, hist_open, amb = {}, {}, 0
    for P in np.nonzero(lk)[0]:
        rA, rS, mx = rho_at(pi, path, (float(xs[P]), float(ys[P])))
        if mx > 0.9 * math.pi: amb += 1; continue
        key = "(%+.6g,%+.6g,%+.6g)" % (round(rA, 6) + 0.0, round(rS, 6) + 0.0, round(rA - rS, 6) + 0.0)
        hist_rec[key] = hist_rec.get(key, 0) + 1
    for qx in np.arange(C - Rdisc, C + Rdisc) + 0.5:
        for qy in np.arange(C - Rdisc, C + Rdisc) + 0.5:
            rA, rS, mx = rho_at(pi, path, (qx, qy))
            if mx > 0.9 * math.pi: amb += 1; continue
            key = "(%+.6g,%+.6g,%+.6g)" % (round(rA, 6) + 0.0, round(rS, 6) + 0.0, round(rA - rS, 6) + 0.0)
            hist_open[key] = hist_open.get(key, 0) + 1
    print(f"{kind}: locked={int(lk.sum())} moved={len(mv)} (all inside sum radius: {far}) "
          f"orbit lengths={sorted(len(o) for o in orb)[:12]}{'...' if len(orb)>12 else ''}")
    print(f"   record sites (rho_A, rho_S, mu): {hist_rec}")
    print(f"   plaquette centres (rho_A, rho_S, mu): {hist_open}   ambiguous chords skipped: {amb}")
print(f"time {time.time()-t0:.1f}s")
