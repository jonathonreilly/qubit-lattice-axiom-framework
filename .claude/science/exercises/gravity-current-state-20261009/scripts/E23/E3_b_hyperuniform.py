"""E3 (b): hyperuniform disordered point sets (density 1, periodic box), label-blind proper-distance coupling ('pd',
R3's kernel R = 1.8), bosons m2 = 1 and 0.04.  Exact E', E'' per realization and TT direction (e23_core).
  'pert'    : Gaussian-perturbed Z^3, iid displacement sd s per component (class-I hyperuniform: S(k) ~ k^2 s^2)
  'stealth' : stealthy hyperuniform, collective-coordinate ground states: minimise Phi = sum_{0<|k|<=K} |rho(k)|^2 from
              iid uniform starts (L-BFGS), chi = M/(3(N-1)) = 0.30; accepted when Phi/N < 1e-12 (S(k) = 0 for |k| <= K)
Hyperuniformity check: mean point S(k) over the smallest shells. Noise: per-direction sd * sqrt(N) vs box (S(0) estimator).
usage: python3 E3_b_hyperuniform.py pert s   |   python3 E3_b_hyperuniform.py stealth chi
"""
import numpy as np, sys, time
from scipy.optimize import minimize
import e23_core as c

kind, par = sys.argv[1], float(sys.argv[2])
rng = np.random.default_rng(int(1000 * par) + (7 if kind == 'stealth' else 3))
PLAN = {6: 80, 8: 60, 10: 40, 12: 20} if kind == 'pert' else {6: 40, 8: 24, 10: 12}
fns = [c.boson_fns(1.0), c.boson_fns(0.04)]


def kvecs(Lb, kmax):
    r = int(np.ceil(kmax * Lb / (2 * np.pi)))
    n = np.array([(a, b, d) for a in range(-r, r + 1) for b in range(-r, r + 1) for d in range(-r, r + 1)], float)
    k = 2 * np.pi * n / Lb; kk = np.linalg.norm(k, axis=1)
    half = (n[:, 0] > 0) | ((n[:, 0] == 0) & (n[:, 1] > 0)) | ((n[:, 0] == 0) & (n[:, 1] == 0) & (n[:, 2] > 0))
    return k[(kk > 1e-9) & (kk <= kmax + 1e-9) & half]


def stealthy(Lb, chi):
    N = Lb**3; M_target = chi * 3 * (N - 1)
    # choose K so that the half-ball holds ~M_target vectors
    K = 2 * np.pi / Lb
    while len(kvecs(Lb, K)) < M_target:
        K += 0.01
    Q = kvecs(Lb, K)

    def phi(x):
        X = x.reshape(N, 3); E = np.exp(1j * X @ Q.T); rho = E.sum(0)
        f = np.sum(np.abs(rho)**2)
        gr = -2 * np.imag(E * np.conj(rho)[None, :]) @ Q
        return f / N, gr.ravel() / N
    for attempt in range(6):
        x0 = rng.uniform(0, Lb, 3 * N)
        res = minimize(phi, x0, jac=True, method='L-BFGS-B', options={'maxiter': 40000, 'maxcor': 30, 'ftol': 1e-30, 'gtol': 1e-14})
        if res.fun < 1e-12:
            return np.mod(res.x.reshape(N, 3), Lb), len(Q) / (3 * (N - 1)), K, res.fun
    return np.mod(res.x.reshape(N, 3), Lb), len(Q) / (3 * (N - 1)), K, res.fun


def sk_small(X, Lb, nshell=2):
    out = []
    for sh in range(1, nshell + 1):
        ks = 2 * np.pi / Lb * sh * np.eye(3)
        out.append(np.mean([np.abs(np.exp(1j * X @ k).sum())**2 / len(X) for k in ks]))
    return out


for Lb, nr in PLAN.items():
    g = np.stack(np.meshgrid(*[np.arange(Lb)] * 3, indexing='ij'), -1).reshape(-1, 3).astype(float)
    t0 = time.time(); acc = []; sks = []; dmin = []; info = []
    for _ in range(nr):
        if kind == 'pert':
            X = np.mod(g + par * rng.standard_normal(g.shape), Lb)
        else:
            X, chi_eff, K, fval = stealthy(Lb, par); info.append((chi_eff, K, fval))
        I, J, D = c.pairs_sparse(X, Lb, 'pd')
        out, _ = c.derivs(len(X), I, J, D, 'pd', fns); acc.append(out)
        sks.append(sk_small(X, Lb))
        Dm = X[None] - X[:, None]; Dm -= Lb * np.round(Dm / Lb); d = np.sqrt((Dm**2).sum(-1)); np.fill_diagonal(d, 9)
        dmin.append(d.min())
    A = np.array(acc); N = Lb**3
    np.save(f"E3_b_{kind}_{par}_L{Lb}.npy", A)
    extra = f" chi_eff={np.mean([i[0] for i in info]):.3f} K={info[0][1]:.2f} max Phi/N={max(i[2] for i in info):.1e}" if info else ""
    print(f"== {kind} par={par} L={Lb} N={N} n={nr} [{time.time()-t0:.0f}s] S(k1)={np.mean([s[0] for s in sks]):.4f} "
          f"S(k2)={np.mean([s[1] for s in sks]):.4f} <d_min>={np.mean(dmin):.3f}{extra}", flush=True)
    for k, fn in enumerate(['boson_m2=1', 'boson_m2=0.04']):
        msg = [f"   {fn:14s}"]
        for ch, idx in c.CH.items():
            st = A[:, k, idx, 1]; ss = A[:, k, idx, 0]; sd = st.std(ddof=1); sdN = sd * np.sqrt(N)
            msg.append(f"{ch}: mean {st.mean():+.5f}+-{st.mean(axis=1).std(ddof=1)/np.sqrt(nr):.5f} sd*sqrtN {sdN:.4f}+-{sdN/np.sqrt(2*(nr-1)):.4f}"
                       f" stress_sd*sqrtN {ss.std(ddof=1)*np.sqrt(N):.4f}")
        print(" | ".join(msg), flush=True)
