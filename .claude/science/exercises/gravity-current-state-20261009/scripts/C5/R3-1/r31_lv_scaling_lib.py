"""R3-1 check 3b: scaling of the per-realization LV of the N=-3 orbit sum with kappa (denser grid,
64 directions u with rapidity <= 0.7, regression).  Reuses the enumeration of r31_lv_orbitsum.py.
Also: second shell N=-7 (orbit of (1,0,0,0)) for comparison; and the absolute LV kappa*std_u(S)."""
import numpy as np
from scipy.special import k1
import runpy, sys, io, contextlib

def shell(N, n0max):
    Mmax = 7 * n0max ** 2 + 10
    R2 = int(np.sqrt(Mmax)) + 1
    a = np.arange(-R2, R2 + 1, dtype=np.int32)
    A, Bb = np.meshgrid(a, a, indexing="ij")
    V = (A * A + Bb * Bb).ravel(); keep = V <= Mmax
    V, A, Bb = V[keep], A.ravel()[keep], Bb.ravel()[keep]
    o = np.argsort(V, kind="stable"); V, A, Bb = V[o], A[o], Bb[o]
    X = [[], [], [], []]
    for n0 in range(1, n0max + 1):
        m = 7 * n0 * n0 + N
        if m < 0: continue
        n1 = np.arange(-int(np.sqrt(m)), int(np.sqrt(m)) + 1)
        v = m - n1 * n1
        lo = np.searchsorted(V, v, "left"); hi = np.searchsorted(V, v, "right"); c = hi - lo
        if c.sum() == 0: continue
        idx = np.concatenate([np.arange(l, h) for l, h in zip(lo[c > 0], hi[c > 0])])
        X[0].append(np.full(len(idx), n0)); X[1].append(np.repeat(n1[c > 0], c[c > 0])); X[2].append(A[idx]); X[3].append(Bb[idx])
    X = [np.concatenate(x).astype(float) for x in X]; X[0] *= np.sqrt(7.0)
    assert np.allclose(-X[0]**2 + X[1]**2 + X[2]**2 + X[3]**2, N)
    return X

def boost(r, nhat):
    nhat = np.asarray(nhat, float); nhat /= np.linalg.norm(nhat)
    return np.array([np.cosh(r), *(np.sinh(r) * nhat)])

