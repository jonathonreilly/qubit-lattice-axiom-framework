#!/usr/bin/env python3
"""A18 noise3d: snapshot noise of a record-set pace in a homogeneous 3D wanderer gas (supplied toy, A6 dynamics).
Wanderers: lazy (1/2) hop to a uniform neighbour, exclusion, random contention winner; periodic L^3.
At S sample sites record k(t) = number of wanderers among m neighbourhood sites:
   m = 6   : nearest neighbours (the star minus the site)
   m = 124 : 5x5x5 cube minus the site
Report: mean and variance of k against Binomial(m,u) (product measure), and the integrated autocorrelation
time tau_int = 1/2 + sum_{s>=1} rho(s) of k and of the exponential response f = r^k (r = e^{1/(m u)}).
Dephasing rate of a rest phase mu * f per beat: Var(sum_t f) ~ T Var(f) 2 tau_int.
usage: noise3d.py u T  (defaults 0.04 6000)
"""
import os, sys, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np

u = float(sys.argv[1]) if len(sys.argv) > 1 else 0.04
T = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
L, S, BURN = 24, 216, 400
N = L ** 3
rng = np.random.default_rng(20261003)
I, J, K = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
FI, FJ, FK = I.ravel(), J.ravel(), K.ravel()
DI = np.array([1, -1, 0, 0, 0, 0]); DJ = np.array([0, 0, 1, -1, 0, 0]); DK = np.array([0, 0, 0, 0, 1, -1])


def step(occ):
    p = np.flatnonzero(occ)
    p = p[rng.random(len(p)) < 0.5]
    d = rng.integers(0, 6, size=len(p))
    t = (((FI[p] + DI[d]) % L) * L + (FJ[p] + DJ[d]) % L) * L + (FK[p] + DK[d]) % L
    ok = ~occ[t]
    p, t = p[ok], t[ok]
    perm = rng.permutation(len(t)); p, t = p[perm], t[perm]
    _, first = np.unique(t, return_index=True)
    occ[p[first]] = False; occ[t[first]] = True


# sample sites on a coarse grid (spacing 4), neighbourhood index lists
g = np.arange(0, L, 4)
SI, SJ, SK = [a.ravel() for a in np.meshgrid(g, g, g, indexing="ij")]
def nbhd(offsets):
    return np.stack([(((SI + a) % L) * L + (SJ + b) % L) * L + (SK + c) % L for a, b, c in offsets], axis=1)
off6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
off124 = [(a, b, c) for a in range(-2, 3) for b in range(-2, 3) for c in range(-2, 3) if (a, b, c) != (0, 0, 0)]
idx = {6: nbhd(off6), 124: nbhd(off124)}

occ = np.zeros(N, bool)
occ[rng.choice(N, size=int(round(u * N)), replace=False)] = True
for _ in range(BURN):
    step(occ)
rec = {m: np.empty((T, len(SI)), np.int16) for m in idx}
for t in range(T):
    step(occ)
    for m, ix in idx.items():
        rec[m][t] = occ[ix].sum(axis=1)


def tau_int(x):
    x = x - x.mean(axis=0)
    n = x.shape[0]
    f = np.fft.rfft(x, 2 * n, axis=0)
    ac = np.fft.irfft(np.abs(f) ** 2, axis=0)[:n].mean(axis=1)
    ac /= ac[0]
    W = 1
    tau = 0.5
    while W < n // 4:                      # automatic window (Sokal): stop when W >= 6 tau
        tau += ac[W]
        if W >= 6 * tau:
            break
        W += 1
    return tau, W


print("u = %.3f, L = %d, %d sample sites, %d ticks (after %d burn-in)" % (u, L, len(SI), T, BURN))
for m in (6, 124):
    k = rec[m].astype(float)
    r = np.exp(1.0 / (m * u))
    f = r ** k
    tk, Wk = tau_int(k)
    tf, Wf = tau_int(f)
    relvar_f = f.var() / f.mean() ** 2
    pred_relvar = ((1 + u * (r * r - 1)) / (1 + u * (r - 1)) ** 2) ** m - 1
    print("  m=%3d: <k> = %.4f (m u = %.4f)  Var k = %.4f (binomial %.4f)  tau_int(k) = %.2f ticks (window %d)"
          % (m, k.mean(), m * u, k.var(), m * u * (1 - u), tk, Wk))
    print("         f = e^{k/(m u)}: Var f/<f>^2 = %.4g (binomial %.4g)  tau_int(f) = %.2f ticks;  dephasing factor Var*2tau = %.4g"
          % (relvar_f, pred_relvar, tf, relvar_f * 2 * tf))
