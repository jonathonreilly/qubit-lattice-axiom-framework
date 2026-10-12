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

rng = np.random.default_rng(11)
us = [boost(0.7 * rng.uniform() ** (1/3), rng.normal(size=3)) for _ in range(64)]
kaps = np.geomspace(0.8, 0.025, 13)
for N, n0max in [(-3, 760), (-7, 700)]:
    X = shell(N, n0max); tau = np.sqrt(-N); Xmax = np.sqrt(7.0) * n0max
    TE = np.sqrt(sum(x * x for x in X)); Rcut = 0.5 * np.arccosh(Xmax**2 / tau**2)
    nu = (TE <= Xmax).sum() / (np.pi * (np.sinh(2 * Rcut) - 2 * Rcut))
    print(f"\nshell N={N}: {len(X[0])} points, nu={nu:.6f}, x0max={Xmax:.0f}")
    rel, ab = [], []
    for kap in kaps:
        SLI = nu * 4 * np.pi * k1(kap * tau) / (kap * tau)
        Sv = np.array([np.exp(-kap * (u[0] * X[0] - u[1] * X[1] - u[2] * X[2] - u[3] * X[3])).sum() for u in us])
        r = Sv / Sv.mean() - 1.0
        rel.append(r.std()); ab.append(Sv.std())
        print(f"  kappa={kap:.4f} kappa*tau={kap*tau:.4f} margin={kap*np.exp(-0.7)*Xmax:6.1f}  mean S/S_LI={Sv.mean()/SLI:.5f}"
              f"  std_u(S)/mean={r.std():.3e}  kappa*std_u(S)={kap*Sv.std():.4e}")
    rel = np.array(rel); ab = np.array(ab)
    p = np.polyfit(np.log(kaps * tau), np.log(rel), 1)
    p2 = np.polyfit(np.log(kaps * tau), np.log(ab), 1)
    print(f"  regression: std_u(S)/mean ~ (kappa tau)^{p[0]:.3f} (prefactor {np.exp(p[1]):.3e});  std_u(S) ~ (kappa tau)^{p2[0]:.3f}")
    print(f"  LI part scales as (kappa tau)^-2 (K1(z)/z ~ 1/z^2); prediction for tempered spectrum: rel slope +1, abs slope -1")
