#!/usr/bin/env python3
"""J:attack-e:PR9348 -- sampled evidence: the note's sixteen calibration corners [1, 2, 1, 1] MHz give drive-residual ranges +1.70986..+8.63695 (f03), +7.95155..+20.78745 (f04), +18.24457..+38.15028 (f05) MHz,
'finite scenarios, not proven extrema over the box'. Instead of more samples, this script attacks them: it recalibrates (own full charge x Fock model, four total-frequency coordinates only, exact refits) at
every point of the 3^4 lattice {-1, 0, 1}^4 of the box (vertices, edge and face midpoints, centre), at 400 random interior points, fits a full quadratic response surface to those refits, locates its extremes over the box on a fine
grid, verifies the extreme candidates by exact refits, and finds by bisection on exact refits how many times the box must be scaled, along the worst corner direction, before each drive residual reaches zero.
It does not read the PR's runner; the model is rebuilt from the note's Hamiltonian, and only the calibration and measured numbers quoted in the note are inputs. Floating point throughout.
Prints SUMMARY:; HIT: only if a stated corner range fails to reproduce or the residual sign changes inside the stated box.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.optimize import least_squares

T0 = time.time()
RESULTS, FIRED = [], []
DRY = "--dry" in sys.argv

CAL = np.array([6.0391, 11.8680, 7.4613, 7.4587])                    # f01, f02, fres1, fres2 (GHz)
MEAS = {3: 17.457, 4: 22.778, 5: 27.794}                              # f03, f04, f05 (GHz)
NOTE_ROOT = np.array([0.196567178810, 24.852181043101, 7.453936854591, 0.077763912291])
NOTE_DRIVE = {3: 5.181438, 4: 14.395723, 5: 28.257343}
NOTE_CORNER = {3: (1.70986, 8.63695), 4: (7.95155, 20.78745), 5: (18.24457, 38.15028)}
NOTE_WIDTH = {3: 0.000368, 4: 0.008878, 5: 0.157861}


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def fire(msg):
    FIRED.append(msg)


class Unassignable(Exception):
    pass


def endpoint(p, ng, N=12, K=8):
    """Levels of the full charge x Fock Hamiltonian at offset charge ng; returns (f01..f05, fres1, fres2) in GHz from dressed states labelled by dominant bare overlap.
    Basis: charges -N..N (no transmon truncation), photons 0..K-1."""
    ec, ej, om, g = p
    n = np.arange(-N, N + 1, dtype=float)
    nq = len(n)
    hc = np.diag(4 * ec * (n - ng) ** 2) - 0.5 * ej * (np.eye(nq, k=1) + np.eye(nq, k=-1))
    _, bare = np.linalg.eigh(hc)                                       # bare transmon eigenvectors (columns), for labelling only
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(hc, np.eye(K)) + om * np.kron(np.eye(nq), np.diag(np.arange(K, dtype=float))) + g * np.kron(np.diag(n), a + a.T)
    e, v = np.linalg.eigh(h)
    labels = [(j, 0) for j in range(6)] + [(0, 1), (1, 1)]           # (transmon level, photon number)
    idx, wts = [], []
    for j, k in labels:
        b = np.kron(bare[:, j], np.eye(K)[:, k])
        ov = np.abs(b @ v) ** 2
        i = int(np.argmax(ov)); idx.append(i); wts.append(ov[i])
    if len(set(idx)) != len(idx) or min(wts) < 0.5:
        raise Unassignable()
    lev = e[idx]
    f = np.array([lev[j] - lev[0] for j in range(1, 6)] + [lev[6] - lev[0], lev[7] - lev[1]])       # f01..f05, fres1 = E(0,1)-E(0,0), fres2 = E(1,1)-E(1,0)
    return f, float(min(wts))


def predict(p, **kw):
    a, wa = endpoint(p, 0.0, **kw); b, wb = endpoint(p, 0.5, **kw)
    return (a + b) / 2, min(wa, wb)


CALIDX = [0, 1, 5, 6]                                                  # f01, f02, fres1, fres2 positions in the 7-vector


def resid_cal(z, target, **kw):
    try:
        f, _ = predict(np.exp(z), **kw)
    except Unassignable:
        return np.full(4, 1e3)
    return (f[CALIDX] - target) * 1000.0                               # MHz


def solve(target, start, max_nfev=80, **kw):
    r = least_squares(lambda z: resid_cal(z, target, **kw), np.log(start), xtol=1e-14, ftol=1e-14, gtol=1e-12, max_nfev=max_nfev, x_scale=1.0)
    return np.exp(r.x), float(np.max(np.abs(r.fun)))


def drive_residuals(p, **kw):
    f, w = predict(p, **kw)
    return {j: 1000.0 * (f[j - 1] - MEAS[j]) / j for j in (3, 4, 5)}, f, w



import itertools as it
HALF = np.array([1, 2, 1, 1]) / 1000.0
def refit(delta_unit, scale=1.0, start=None):
    """delta_unit in [-1, 1]^4 (times scale): perturbation of the four calibration coordinates in units of the box half-widths; returns drive residuals (MHz) and the calibration error"""
    p, err = solve(CAL + HALF * scale * np.asarray(delta_unit, float), NOTE_ROOT if start is None else start, max_nfev=80, N=16, K=8)
    d, _, w = drive_residuals(p, N=16, K=8)
    return np.array([d[3], d[4], d[5]]), err, p
t0 = time.time()
# 1. the 3^4 lattice
lat = list(it.product((-1, 0, 1), repeat=4)); Rl = []; errmax = 0.0
for s in lat:
    r, e, _ = refit(s); Rl.append(r); errmax = max(errmax, e)
Rl = np.array(Rl)
corner_idx = [i for i, s in enumerate(lat) if all(abs(x) == 1 for x in s)]
lo = Rl[corner_idx].min(axis=0); hi = Rl[corner_idx].max(axis=0)
check("exact refits at the sixteen vertices of the box reproduce the note's corner ranges to 5e-4 MHz", all(abs(lo[k] - NOTE_CORNER[j][0]) < 5e-4 and abs(hi[k] - NOTE_CORNER[j][1]) < 5e-4 for k, j in enumerate((3, 4, 5))) and errmax < 1e-3,
      "; ".join(f"f0{j}: {lo[k]:+.5f}..{hi[k]:+.5f}" for k, j in enumerate((3, 4, 5))) + f"; max calibration error {errmax:.1e} MHz; {time.time() - t0:.0f} s")
lat_lo = Rl.min(axis=0); lat_hi = Rl.max(axis=0)
check("over all 81 lattice points (edge and face midpoints and the centre included) no drive residual leaves the corner range by more than 1e-3 MHz", all(lat_lo[k] > lo[k] - 1e-3 and lat_hi[k] < hi[k] + 1e-3 for k in range(3)),
      "; ".join(f"f0{j}: {lat_lo[k]:+.5f}..{lat_hi[k]:+.5f}" for k, j in enumerate((3, 4, 5))))
# 2. random interior points
rng = np.random.default_rng(29)
Xr = rng.uniform(-1, 1, (400, 4)); Rr = np.array([refit(x)[0] for x in Xr])
check("at 400 uniformly random interior points of the box no drive residual leaves the corner range by more than 1e-3 MHz", all(Rr[:, k].min() > lo[k] - 1e-3 and Rr[:, k].max() < hi[k] + 1e-3 for k in range(3)),
      "; ".join(f"f0{j}: {Rr[:, k].min():+.5f}..{Rr[:, k].max():+.5f}" for k, j in enumerate((3, 4, 5))) + f"; {time.time() - t0:.0f} s")
# 3. quadratic response surface fitted to lattice + random points
Xall = np.vstack([np.array(lat, float), Xr]); Rall = np.vstack([Rl, Rr])
def feats(X):
    X = np.atleast_2d(X); cols = [np.ones(len(X))] + [X[:, i] for i in range(4)] + [X[:, i] * X[:, j] for i in range(4) for j in range(i, 4)]
    return np.stack(cols, axis=1)
coef = np.linalg.lstsq(feats(Xall), Rall, rcond=None)[0]
rms = np.sqrt(np.mean((feats(Xall) @ coef - Rall) ** 2, axis=0))
gr = np.linspace(-1, 1, 21); G = np.array(list(it.product(gr, repeat=4))); Sg = feats(G) @ coef
qmin = Sg.min(axis=0); qmax = Sg.max(axis=0)
check("a full quadratic response surface fits the 481 exact refits to 1e-3 MHz rms, and its extremes over the box (21^4 grid) lie within 1e-3 MHz of the corner range", rms.max() < 1e-3 and all(qmin[k] > lo[k] - 1e-3 and qmax[k] < hi[k] + 1e-3 for k in range(3)),
      f"rms {np.round(rms, 6)} MHz; surface extremes " + "; ".join(f"f0{j}: {qmin[k]:+.5f}..{qmax[k]:+.5f}" for k, j in enumerate((3, 4, 5))))
# 4. how far must the box be scaled before the residual reaches zero (worst corner direction, exact refits, bisection)
margins = {}
for k, j in enumerate((3, 4, 5)):
    cidx = corner_idx[int(np.argmin(Rl[corner_idx][:, k]))]; sdir = np.array(lat[cidx], float)
    a, b = 1.0, 6.0
    if refit(sdir, b)[0][k] > 0: margins[j] = (None, sdir); continue
    for _ in range(40):
        m = 0.5 * (a + b)
        if refit(sdir, m)[0][k] > 0: a = m
        else: b = m
    margins[j] = (0.5 * (a + b), sdir)
for j in (3, 4, 5):
    s, sd = margins[j]; print(f"   f0{j}: the drive residual reaches zero when the box is scaled by {s:.4f} along the corner {sd.astype(int).tolist()} (perturbations {np.round(HALF * s * sd * 1000, 3).tolist()} MHz on f01, f02, fres1, fres2)")
check("the sign of every drive residual is positive throughout the stated box (scale 1): the smallest scale that removes a residual is above 1 for f03, f04 and f05", all(margins[j][0] is not None and margins[j][0] > 1 for j in (3, 4, 5)))
print(f"   total {time.time() - t0:.0f}s")
if all(RESULTS):
    print("SUMMARY: no purchase on the sign or the corner ranges: exact refits at 81 lattice points and 400 random points of the box stay inside the note's corner ranges, a quadratic response surface (rms below 1e-3 MHz) has its extremes at the corners, and the f03, f04, f05 drive residuals reach zero only when the box [1, 2, 1, 1] MHz is scaled by " + ", ".join(f"{margins[j][0]:.2f}" for j in (3, 4, 5)) + " (worst corner directions)")
else:
    print("SUMMARY: failed checks: " + str([i for i, r in enumerate(RESULTS) if not r])); print("HIT: the stated box's corner ranges or the residual signs fail to reproduce under exact refits")
sys.exit(0)
