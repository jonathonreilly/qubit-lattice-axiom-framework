"""R4-3 check B2 (saves arrays; adds kappa=0.035): does the per-realization (automorphic) LV of LRL orbit sums survive the
Lorentz-invariant moment conditions that turn a finite-shell retarded kernel into a d'Alembertian?

Object (as R3-1 sec 4.3, in the forward tube p = i*kappa*u):
  S_N(u,kappa) = sum_{x in L7, x^2 = N, x0 > 0} exp(-kappa * w(u,x)),  w = u0 x0 - u.x  (> 0)
Exact LI part (equidistribution): S_N^LI = nu_N * 4 pi K1(kappa tau_N)/(kappa tau_N), tau_N = sqrt(-N).
K1(z)/z = 1/z^2 + (1/2)[ln(z/2) + g - 1/2] + (z^2/16)[ln(z/2) + g - 5/4] + O(z^4 ln z).
Moment conditions on weights w_N (kill 1/k^2, ln k, const, k^2 ln k / k^2 const):
  sum w nu tau^-2 = 0, sum w nu = 0, sum w nu ln tau = 0, sum w nu tau^2 = 0,
  normalisation sum w nu tau^2 ln tau = 1  =>  LI part of sum_N w_N S_N  ~ (pi/4) kappa^2 + O(k^4 ln k).
LV part: std over directions u of sum_N w_N S_N(u,kappa)  (the LI part is u-independent, so the std does
not depend on the accuracy of nu_N).
Also: best weights over all available shells that minimise the LV subject to the 4 LI conditions + norm.
"""
import numpy as np, time
from scipy.special import k1

def shell(N, n0max):  # copied from R3-1 r31_lv_scaling_lib.py (future sheet, x0 = sqrt7 n0 > 0)
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
    if not X[0]: return None
    X = [np.concatenate(x).astype(float) for x in X]; X[0] *= np.sqrt(7.0)
    assert np.allclose(-X[0]**2 + X[1]**2 + X[2]**2 + X[3]**2, N)
    return np.array(X)

def boost(r, nhat):
    nhat = np.asarray(nhat, float); nhat /= np.linalg.norm(nhat)
    return np.array([np.cosh(r), *(np.sinh(r) * nhat)])

t0 = time.time()
rng = np.random.default_rng(2026)
us = np.array([boost(0.7 * rng.uniform() ** (1 / 3), rng.normal(size=3)) for _ in range(32)])
Umink = us * np.array([1, -1, -1, -1])            # w = Umink @ X
kaps = np.array([0.8, 0.56, 0.4, 0.28, 0.2, 0.14, 0.1, 0.07, 0.05, 0.035])
n0max = 520
Xmax = np.sqrt(7.0) * n0max
print(f"n0max={n0max}, truncation margin at kappa={kaps.min()}: {kaps.min()*np.exp(-0.7)*Xmax:.1f} (e-folds)")
Ns, nus, S = [], [], []
for N in range(-1, -13, -1):
    X = shell(N, n0max)
    if X is None: continue
    tau = np.sqrt(-N)
    TE = np.sqrt((X * X).sum(0)); Rcut = 0.5 * np.arccosh(Xmax**2 / tau**2)
    nu = (TE <= Xmax).sum() / (np.pi * (np.sinh(2 * Rcut) - 2 * Rcut))   # R3-1's density estimator
    SN = np.zeros((len(kaps), len(us)))
    for c0 in range(0, X.shape[1], 400000):
        W = Umink @ X[:, c0:c0 + 400000]
        for i, k in enumerate(kaps):
            SN[i] += np.exp(-k * W).sum(1)
    SLI = nu * 4 * np.pi * k1(kaps * tau) / (kaps * tau)
    Ns.append(N); nus.append(nu); S.append(SN)
    rel = SN.std(1) / SN.mean(1)
    print(f"shell N={N:3d}: {X.shape[1]:8d} pts  nu={nu:.5f}  mean_u S/S_LI at k=.8,.2,.05: "
          f"{SN.mean(1)[0]/SLI[0]:.4f} {SN.mean(1)[4]/SLI[4]:.4f} {SN.mean(1)[-1]/SLI[-1]:.4f}  "
          f"rel LV (k=.8..0.05): {' '.join(f'{r:.1e}' for r in rel)}   [{time.time()-t0:.0f}s]", flush=True)
Ns = np.array(Ns); nus = np.array(nus); S = np.array(S)   # S[shell, kappa, u]
taus = np.sqrt(-Ns)

np.savez("r43_S_arrays.npz", Ns=Ns, nus=nus, S=S, kaps=kaps, us=us, n0max=n0max)
print("saved r43_S_arrays.npz", flush=True)
