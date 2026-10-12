"""K1 (kill agent, F1a): is the per-configuration TT random part white (S(q->0) != 0)?
Also: the FIRST-order per-configuration TT stress (a random tadpole), which R3 did not report.

Toy = R3's C2 model exactly (couplings from current proper distances only, so Lemma A applies):
  w(d_g) = (1 - d_g^2/R^2)^4_+, R = 1.8, scalar H = Lap_g + m^2, E = sum_n 1/2 sqrt(lam_n + m^2).
  g = exp(t h), h traceless, tr h^2 = 1.  Frozen iid uniform ("Poisson", fixed N) sites, periodic box,
  density 1.  Exact first and second t-derivatives at t = 0 from eigen-perturbation theory.
Quantities per realization and PER DIRECTION (R3 reported the 5-direction rotation average, which
  hides part of the single-direction noise):
  tau_d = (dE/dt)/N   (TT stress per site; ensemble mean 0 by isotropy)
  s_d   = (d2E/dt2)/N (TT stiffness per site; ensemble mean 0 by Lemma A up to torus shape)
White noise at q -> 0  <=>  sd * sqrt(N) -> const != 0.  A conserved-current structure
  (local density = divergence) would make the periodic-box q = 0 sum vanish: sd*sqrt(N) -> 0.
Pre-stated reading: WHITE if the fitted exponent of sd vs N is -0.5 within 2 SE (and sd*sqrt(N)
  shows no downward trend > 3 SE between the smallest and the largest box); SUPPRESSED if exponent < -0.65.
"""
import numpy as np, sys, time
import scipy.sparse as sps
rng = np.random.default_rng(int(sys.argv[3]) if len(sys.argv) > 3 else 4242)
R = 1.8
m2 = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0

def dirs():
    E = [np.diag([1., -1, 0])/np.sqrt(2), np.diag([1., 1, -2])/np.sqrt(6)]
    T = []
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1/np.sqrt(2); T.append(M)
    return E, T
EH, TH = dirs()

def lap(n, I, J, w):
    Lm = np.zeros((n, n))
    np.add.at(Lm, (I, J), -w); np.add.at(Lm, (J, I), -w)
    deg = np.zeros(n); np.add.at(deg, I, w); np.add.at(deg, J, w)
    Lm[np.diag_indices(n)] += deg
    return Lm

def slap(n, I, J, w):
    deg = np.zeros(n); np.add.at(deg, I, w); np.add.at(deg, J, w)
    rows = np.concatenate([I, J, np.arange(n)]); cols = np.concatenate([J, I, np.arange(n)])
    vals = np.concatenate([-w, -w, deg])
    return sps.csr_matrix((vals, (rows, cols)), shape=(n, n))

def derivs(X, Lb):
    n = len(X)
    D = X[None, :, :] - X[:, None, :]; D -= Lb*np.round(D/Lb)
    d2 = np.einsum('ijk,ijk->ij', D, D)
    iu = np.triu_indices(n, 1); msk = d2[iu] < R**2
    I, J, Dp = iu[0][msk], iu[1][msk], D[iu][msk]
    s = np.einsum('pk,pk->p', Dp, Dp)/R**2
    w = (1-s)**4; ws = -4*(1-s)**3; wss = 12*(1-s)**2
    lam, V = np.linalg.eigh(lap(n, I, J, w)); lam = np.clip(lam, 0, None)
    f1 = 0.25/np.sqrt(lam + m2); f2 = -0.125/(lam + m2)**1.5
    dl = lam[:, None] - lam[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        F = (f1[:, None] - f1[None, :])/dl
    deg = np.abs(dl) < 1e-10
    F[deg] = (-0.125/(0.5*(lam[:, None]+lam[None, :]) + m2)**1.5)[deg]
    out = []
    for h in EH + TH:
        # d_g^2 = dx^T exp(t h) dx -> first deriv dx^T h dx, second dx^T h^2 dx
        sp = np.einsum('pi,ij,pj->p', Dp, h, Dp)/R**2
        spp = np.einsum('pi,ij,pj->p', Dp, h@h, Dp)/R**2
        L1 = slap(n, I, J, ws*sp); L2 = slap(n, I, J, wss*sp**2 + ws*spp)
        A1 = V.T @ (L1 @ V)
        diagA2 = np.sum(V*(L2 @ V), axis=0)
        e1 = np.sum(f1*np.diag(A1))
        e2 = np.sum(f1*diagA2) + np.sum(A1**2*F)
        out.append((e1/n, e2/n))
    return np.array(out)   # 5 x 2

if __name__ == '__main__':
    plan = {6: 300, 8: 160, 10: 80, 12: 40, 14: 20}
    if len(sys.argv) > 2: plan = {int(k): int(v) for k, v in (kv.split(':') for kv in sys.argv[2].split(','))}
    print(f"R={R} m2={m2}  (per-direction stats; 5 TT directions pooled per realization)")
    rows = []
    for Lb, nr in plan.items():
        N = Lb**3; t0 = time.time(); acc = []
        for _ in range(nr):
            acc.append(derivs(rng.uniform(0, Lb, (N, 3)), Lb))
        a = np.array(acc)                   # nr x 5 x 2
        tau = a[:, :, 0].ravel(); st = a[:, :, 1].ravel()
        # SE of sd: use realization blocks (directions in one realization are correlated)
        def sd_and_se(x2d):
            sd = x2d.std(ddof=1); n_eff = x2d.shape[0]
            return sd, sd/np.sqrt(2*max(n_eff-1,1))
        sdt, set_ = sd_and_se(a[:, :, 0]); sds, ses = sd_and_se(a[:, :, 1])
        rows.append((N, sdt, set_, sds, ses))
        print(f"box {Lb:2d} N={N:5d} n={nr:3d}: stress mean {tau.mean():+.2e} sd {sdt:.5f} sd*sqrtN {sdt*np.sqrt(N):.4f}+-{set_*np.sqrt(N):.4f} | "
              f"stiff mean {st.mean():+.5f}+-{st.std(ddof=1)/np.sqrt(len(st)):.5f} sd {sds:.5f} sd*sqrtN {sds*np.sqrt(N):.4f}+-{ses*np.sqrt(N):.4f}  [{time.time()-t0:.0f}s]", flush=True)
    r = np.array(rows)
    for col, name in [(1, 'stress'), (3, 'stiffness')]:
        x = np.log(r[:, 0]); y = np.log(r[:, col]); wts = (r[:, col]/r[:, col+1])**2
        A = np.vstack([np.ones_like(x), x]).T; W = np.diag(wts)
        cov = np.linalg.inv(A.T @ W @ A); beta = cov @ A.T @ W @ y
        print(f"fit sd ~ N^p for {name}: p = {beta[1]:+.3f} +- {np.sqrt(cov[1,1]):.3f}  (white noise: -0.5)")
