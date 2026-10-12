"""R4-3 check B: does the per-realization (automorphic) LV of LRL orbit sums survive the
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
kaps = np.array([0.8, 0.56, 0.4, 0.28, 0.2, 0.14, 0.1, 0.07, 0.05])
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
# pairwise correlation of the LV patterns at kappa = 0.1
P = S[:, 6, :] - S[:, 6, :].mean(1, keepdims=True)
C = np.corrcoef(P)
off = C[np.triu_indices(len(Ns), 1)]
print(f"\nLV-pattern correlations between shells at kappa=0.1: mean {off.mean():+.3f}, min {off.min():+.3f}, max {off.max():+.3f}")

def LIcomb(w):
    return (w[:, None] * nus[:, None] * 4 * np.pi * k1(np.outer(taus, kaps)) / np.outer(taus, kaps)).sum(0)

def report(w, label):
    Sw = (w[:, None, None] * S).sum(0)                  # [kappa, u]
    lv = Sw.std(1)
    li_exact = LIcomb(w)
    print(f"\n{label}: weights w = {np.array2string(w, precision=3, max_line_width=200)}  |w|_2={np.linalg.norm(w):.2f}")
    print("   kappa   LI(analytic)   (pi/4)k^2     std_u(S_w)    rel LV = std/LI    kappa*std")
    for i, k in enumerate(kaps):
        print(f"   {k:5.3f}  {li_exact[i]: .4e}   {np.pi/4*k*k: .4e}   {lv[i]:.4e}    {lv[i]/abs(li_exact[i]):.3e}       {k*lv[i]:.3e}")
    sl = np.polyfit(np.log(kaps[3:]), np.log(lv[3:] / np.abs(li_exact[3:])), 1)[0]
    sl2 = np.polyfit(np.log(kaps[3:]), np.log(lv[3:]), 1)[0]
    print(f"   log-slope (kappa<=0.28): rel LV ~ kappa^{sl:.2f};  abs LV ~ kappa^{sl2:.2f}")
    return lv / np.abs(li_exact)

# moment matrix
M = np.array([nus * taus**-2, nus, nus * np.log(taus), nus * taus**2])
nrm = nus * taus**2 * np.log(taus)
# (1) minimal 5-shell solutions
for pick in [[-1, -2, -3, -5, -7], [-2, -3, -5, -6, -7], [-3, -5, -7, -10, -11]]:
    idx = [list(Ns).index(p) for p in pick if p in Ns]
    if len(idx) < 5: continue
    A = np.vstack([M[:, idx], nrm[idx]]); b = np.array([0, 0, 0, 0, 1.0])
    w = np.zeros(len(Ns)); w[idx] = np.linalg.solve(A, b)
    report(w, f"5-shell d'Alembertian, shells {pick}")
# (2) min-norm over all shells
A = np.vstack([M, nrm]); b = np.array([0, 0, 0, 0, 1.0])
w = np.linalg.lstsq(A, b, rcond=None)[0]
report(w, f"min-norm over all {len(Ns)} shells")
# (3) LV-minimising weights subject to the constraints (try hard to cancel the automorphic part)
Pall = (S - S.mean(2, keepdims=True))                  # [shell, kappa, u]
# weight the kappa rows so that each kappa counts relative to (pi/4)k^2
Q = (Pall / (np.pi / 4 * kaps[None, :, None] ** 2)).reshape(len(Ns), -1)
H = Q @ Q.T
# minimise w^T H w subject to A w = b  (KKT)
nA = A.shape[0]
K = np.block([[2 * H, A.T], [A, np.zeros((nA, nA))]])
sol = np.linalg.solve(K, np.concatenate([np.zeros(len(Ns)), b]))
wopt = sol[:len(Ns)]
r_opt = report(wopt, f"LV-minimising (in-sample, 32 dirs x 9 kappas) over all {len(Ns)} shells")
# out-of-sample check of the optimised weights on 16 fresh directions at 3 kappas
rng2 = np.random.default_rng(99)
us2 = np.array([boost(0.7 * rng2.uniform() ** (1 / 3), rng2.normal(size=3)) for _ in range(16)])
U2 = us2 * np.array([1, -1, -1, -1])
k_oos = np.array([0.4, 0.1, 0.05])
S2 = np.zeros(len(k_oos) * 0 + len(k_oos))
lvo = np.zeros((len(k_oos), len(us2)))
for j, N in enumerate(Ns):
    if wopt[j] == 0: continue
    X = shell(int(N), n0max)
    for c0 in range(0, X.shape[1], 400000):
        W = U2 @ X[:, c0:c0 + 400000]
        for i, k in enumerate(k_oos):
            lvo[i] += wopt[j] * np.exp(-k * W).sum(1)
print("\nout-of-sample (16 fresh directions) for LV-minimising weights:")
for i, k in enumerate(k_oos):
    li = (wopt * nus * 4 * np.pi * k1(k * taus) / (k * taus)).sum()
    print(f"   kappa={k:.3f}: std_u/LI = {lvo[i].std()/abs(li):.3e}")
print(f"\ntotal time {time.time()-t0:.0f}s")
