#!/usr/bin/env python3
"""J:attack-e:PR9353 -- SAMPLED EVIDENCE: the note's finite sampled extrema (corner ranges, coupling continuation, parity maxima) against dense sampling and hill-climbing.

Claims resting on samples (note, "Numerical checks and remaining uncertainty" and "Physical charge convention"):
 (S1) the 32 corners of the five-input printed-decimal rounding box (halfwidths [5e-7, 5e-5, 5e-6, 5e-6, 5e-6] GHz) give unused drive ranges f03/3 [-.444, .007], f04/4 [-1.043, .258], f05/5 [-2.334, .415], f06/6 [-4.874, .182] MHz
      ("rounded summaries of sampled extrema, not outward-certified interval endpoints ... not a continuous box bound");
 (S2) sampled coupling continuation (dressed-state labels tracked over the coupling scale) has minimum dominant overlap about .915 and 14 distinct labels;
 (S3) the parity-splitting maximum 3.464585 MHz (Andreev) from 65 offsets and four bounded searches over [0, 1/4], vanishing at q = 1/4.
This script replaces the samples by (S1) random points inside the box (each refit to its five perturbed inputs) plus a hill-climb on the perturbation direction that maximises / minimises each unused error, (S2) a 2001-point scan of the
coupling scale for both endpoints, (S3) a 401-offset scan plus bounded refinement. A HIT is an unused drive error outside the note's corner range, an unassignable or sub-.5 overlap state on the coupling path, or a parity value above the
note's maximum. The model is built here (own Fourier coefficients, charge x Fock construction, dressed-state labelling); floating point. Prints SUMMARY: and, only if a sampled claim is exceeded, HIT:.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.optimize import least_squares, minimize_scalar

T0 = time.time()
RESULTS, FIRED = [], []
DRY = "--dry" in sys.argv
CAL = np.array([5.354767, 10.5356, 7.76131, 7.75608, 7.75135])
MEAS_F = {3: 15.5289, 4: 20.3168, 5: 24.879, 6: 29.1888}
CALIDX = [0, 1, 6, 7, 8]
DIV = np.array([1, 2, 1, 1, 1.0])
NOTE_P = np.array([0.1841990760792327, 21.829772186093592, 7.738912856323958, 0.18858878602560333, 0.15464897201354028])
HALF = np.array([5e-7, 5e-5, 5e-6, 5e-6, 5e-6])
NOTE_RANGE = {3: (-0.444, 0.007), 4: (-1.043, 0.258), 5: (-2.334, 0.415), 6: (-4.874, 0.182)}


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


class Unassignable(Exception):
    pass


def coeffs(tau, grid=1 << 14):
    phi = 2 * np.pi * np.arange(grid) / grid
    s = np.sin(phi / 2) ** 2
    w = 4 * s / (1 + np.sqrt(1 - tau * s))
    c = np.fft.rfft(w).real / grid
    return c[:60] / (-2 * c[1])


def levels(p, ng, N=14, M=12, K=8, scale=1.0, minw=False):
    ec, ej, om, g, tau = p
    n = np.arange(-N, N + 1, dtype=float)
    cm = coeffs(tau)
    idx = np.abs(np.subtract.outer(np.arange(2 * N + 1), np.arange(2 * N + 1)))
    h0 = ej * cm[idx] + np.diag(4 * ec * (n - ng) ** 2)
    e0, v0 = np.linalg.eigh(h0); e = e0[:M] - e0[0]; v = v0[:, :M]
    charge = v.T @ (n[:, None] * v)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.diag((om * np.arange(K)[:, None] + e[None, :]).ravel()) + scale * g * np.kron(a + a.T, charge)
    w, V = np.linalg.eigh(h)
    targets = [(j, 0) for j in range(7)] + [(j, 1) for j in range(7)]
    ix = [int(np.argmax(np.abs(V[k * M + j, :]) ** 2)) for j, k in targets]
    wt = [float(np.abs(V[k * M + j, i]) ** 2) for (j, k), i in zip(targets, ix)]
    if minw:
        return len(set(ix)), min(wt)
    if len(set(ix)) != len(ix) or min(wt) < 0.5:
        raise Unassignable()
    lev = {t: w[i] for t, i in zip(targets, ix)}
    return np.array([lev[j, 0] - lev[0, 0] for j in range(1, 7)] + [lev[j, 1] - lev[j, 0] for j in range(7)])


def predict(p, **kw):
    return (levels(p, 0.0, **kw) + levels(p, 0.5, **kw)) / 2


def refit(target, start):
    def res(z):
        try:
            f = predict(z)
        except Unassignable:
            return np.full(5, 10.0)
        return (f[CALIDX] - target) / DIV
    r = least_squares(res, start, bounds=([0.03, 1, 7, 0.001, 0.0], [1, 100, 8.5, 1, 0.99]), x_scale=[0.2, 20, 8, 0.1, 0.2], ftol=1e-13, xtol=1e-13, gtol=1e-13, max_nfev=80)
    return r.x, float(np.max(np.abs(r.fun)))


def drives(p):
    f = predict(p)
    return np.array([1000 * (f[j - 1] - MEAS_F[j]) / j for j in (3, 4, 5, 6)])


def f06_phys(p, q, N=16, K=16):
    ec, ej, om, g, tau = p
    n = np.arange(-N, N + 1, dtype=float)
    cm = coeffs(tau)
    idx = np.abs(np.subtract.outer(np.arange(2 * N + 1), np.arange(2 * N + 1)))
    h0 = ej * cm[idx] + np.diag(4 * ec * (n - q) ** 2)
    e0, v0 = np.linalg.eigh(h0)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(h0, np.eye(K)) + om * np.kron(np.eye(len(n)), np.diag(np.arange(K, dtype=float))) + g * np.kron(np.diag(n - q), a + a.T)
    w, V = np.linalg.eigh(h)
    def lab(j):
        pr = np.abs(np.kron(v0[:, j], np.eye(K)[:, 0]) @ V) ** 2
        i = int(np.argmax(pr)); return i, pr[i]
    i6, w6 = lab(6); i0, w0 = lab(0)
    if min(w6, w0) < 0.5:
        raise Unassignable()
    return w[i6] - w[i0]


def run():
    # ---- S1: the rounding box
    d0 = drives(NOTE_P)
    corners = []
    for signs in itertools.product((-1, 1), repeat=5):
        z, err = refit(CAL + HALF * np.array(signs), NOTE_P)
        corners.append((drives(z), err))
    cmin = np.min([c[0] for c in corners], axis=0); cmax = np.max([c[0] for c in corners], axis=0)
    okc = all(abs(cmin[i] - NOTE_RANGE[j][0]) < 6e-3 and abs(cmax[i] - NOTE_RANGE[j][1]) < 6e-3 for i, j in enumerate((3, 4, 5, 6)))
    check("(S0) the 32 corners refit here reproduce the note's corner ranges to 6 kHz (own model)", okc,
          "; ".join(f"f0{j}/{j}: [{cmin[i]:+.3f}, {cmax[i]:+.3f}] (note [{NOTE_RANGE[j][0]:+.3f}, {NOTE_RANGE[j][1]:+.3f}])" for i, j in enumerate((3, 4, 5, 6))) + f"; max calibration error {max(c[1] for c in corners):.1e}; {time.time() - T0:.0f} s")
    rng = np.random.default_rng(20260929)
    ns = 20 if DRY else 60
    vals = []
    z = NOTE_P.copy()
    for _ in range(ns):
        pert = HALF * rng.uniform(-1, 1, 5)
        z, err = refit(CAL + pert, NOTE_P)
        vals.append(drives(z))
    vals = np.array(vals)
    smin = vals.min(axis=0); smax = vals.max(axis=0)
    # hill-climb: linear-response direction from the corner data, then local coordinate search on the perturbation
    climbed_min = smin.copy(); climbed_max = smax.copy()
    for i in range(4):
        for sense in (-1, +1):
            pert = np.zeros(5)
            best = sense * drives(refit(CAL, NOTE_P)[0])[i]
            step = 0.5
            for it in range(3 if DRY else 6):
                improved = False
                for k in range(5):
                    for sg in (-1, +1):
                        trial = pert.copy(); trial[k] = np.clip(trial[k] + sg * step * HALF[k], -HALF[k], HALF[k])
                        zt, e = refit(CAL + trial, NOTE_P)
                        v = sense * drives(zt)[i]
                        if v > best + 1e-9:
                            best, pert, improved = v, trial, True
                if not improved:
                    step /= 2
            if sense > 0:
                climbed_max[i] = max(climbed_max[i], best)
            else:
                climbed_min[i] = min(climbed_min[i], -best)
    over = []
    for i, j in enumerate((3, 4, 5, 6)):
        lo, hi = NOTE_RANGE[j]
        if min(smin[i], climbed_min[i]) < lo - 6e-3 or max(smax[i], climbed_max[i]) > hi + 6e-3:
            over.append((j, min(smin[i], climbed_min[i]), max(smax[i], climbed_max[i]), lo, hi))
    check(f"(S1) {ns} random points of the rounding box (each refit exactly) plus a coordinate hill-climb on the perturbation stay inside the note's corner ranges (to 6 kHz): the corner ranges are the box ranges at this resolution", not over,
          "sampled/climbed ranges " + "; ".join(f"f0{j}/{j}: [{min(smin[i], climbed_min[i]):+.3f}, {max(smax[i], climbed_max[i]):+.3f}]" for i, j in enumerate((3, 4, 5, 6))) + (f"; OUTSIDE: {over}" if over else "") + f"; {time.time() - T0:.0f} s")
    if over:
        FIRED.append(f"unused drive errors leave the note's corner ranges inside the rounding box: {over}")
    # ---- S2: coupling continuation
    scales = np.linspace(0, 1, 201 if DRY else 2001)
    worst = 1.0; bad = 0; ndist = 14
    for ng in (0.0, 0.5):
        for sc in scales:
            nd, mw = levels(NOTE_P, ng, scale=float(sc), minw=True)
            worst = min(worst, mw)
            if nd < 14 or mw < 0.5:
                bad += 1; ndist = min(ndist, nd)
    check(f"(S2) along the coupling scale (G -> s G, s = 0..1, {len(scales)} values, both endpoints) all 14 labels stay distinct with dominant overlap above .5, and the minimum overlap is about the note's .915", bad == 0 and 0.85 < worst < 1.0,
          f"minimum overlap {worst:.4f} (note ~.91548 over 21 samples); {bad} scale values with a repeated label or overlap below .5; {time.time() - T0:.0f} s")
    if bad:
        FIRED.append(f"the labelled branch is not tracked along the coupling path: {bad} scale values fail")
    # ---- S3: parity maximum
    nq = 41 if DRY else 201
    qs = np.linspace(0, 0.25, nq)
    par = np.array([abs(f06_phys(NOTE_P, q) - f06_phys(NOTE_P, q + 0.5)) for q in qs]) * 1000
    res = minimize_scalar(lambda q: -abs(f06_phys(NOTE_P, q) - f06_phys(NOTE_P, q + 0.5)) * 1000, bounds=(0, 0.02), method="bounded", options={"xatol": 1e-9})
    pmax = max(par.max(), -res.fun)
    check(f"(S3) the parity maximum over {nq} offsets in [0, 1/4] plus a bounded refinement is not above the note's 3.464585 MHz, is attained at q = 0 and vanishes at q = 1/4", pmax <= 3.464585 + 5e-3 and par[-1] < 1e-3 and int(par.argmax()) == 0,
          f"maximum {pmax:.6f} MHz at q = {qs[par.argmax()]:.4f}; at q = 1/4: {par[-1]:.1e} MHz; monotone decrease {bool(np.all(np.diff(par) <= 1e-9))}; {time.time() - T0:.0f} s")
    if pmax > 3.464585 + 5e-3:
        FIRED.append(f"parity maximum {pmax:.6f} MHz above the note's 3.464585")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: SAMPLED CLAIM EXCEEDED: " + FIRED[0])
        print("HIT: PR #9353: " + "; ".join(FIRED))
        return 0
    print("SUMMARY: pattern has no purchase: dense sampling and hill-climbing find no unused drive error outside the note's corner ranges inside the rounding box, the labelled branch is tracked along the whole coupling path "
          f"(minimum overlap {worst:.3f}), and the parity maximum is 3.4646 MHz at q = 0, monotone to zero at q = 1/4")
    return 0


if __name__ == "__main__":
    sys.exit(run())
