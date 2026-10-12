"""C2b: (1) finite-difference validation of the exact Hessian on one iid realization (label-blind:
pairs recomputed from proper distances at each t); (2) more statistics for iid sets at boxes 8, 10, 12,
with the rotation-averaged (5-direction) Hessian per realization."""
import numpy as np, sys, time
sys.path.insert(0, '.')
import c2_pointset_shear_modulus as c2
rng = np.random.default_rng(777)
R, m2 = c2.R, c2.m2

def energy(X, Lb, G):
    n = len(X)
    D = X[None, :, :] - X[:, None, :]; D -= Lb*np.round(D/Lb)
    d2 = np.einsum('ijk,kl,ijl->ij', D, G, D)
    iu = np.triu_indices(n, 1); s = d2[iu]/R**2; msk = s < 1
    w = (1 - s[msk])**4
    Lm = c2.lap(n, iu[0][msk], iu[1][msk], w)
    lam = np.clip(np.linalg.eigvalsh(Lm), 0, None)
    return np.sum(0.5*np.sqrt(lam + m2))/n

def expm_sym(h, t):
    ev, U = np.linalg.eigh(h); return U @ np.diag(np.exp(t*ev)) @ U.T

if __name__ == '__main__':
    Lb = 8; X = rng.uniform(0, Lb, (Lb**3, 3))
    an = c2.hessians(X, Lb)
    for ch in ['E_g', 'T_2g']:
        fds = []
        for h in c2.H[ch]:
            t = 2e-3
            e = [energy(X, Lb, expm_sym(h, s*t)) for s in (-2, -1, 0, 1, 2)]
            fds.append((-e[0] + 16*e[1] - 30*e[2] + 16*e[3] - e[4])/(12*t**2))
        print(f"FD check {ch}: analytic {an[ch][1]:+.8f}  finite-diff {np.mean(fds):+.8f}")
    # statistics: rotation-averaged Hessian (mean of the 6 directions; for an isotropic ensemble
    # E_g and T_2g means coincide)
    for Lb, nreal in [(8, 300), (10, 200), (12, 60)]:
        t0 = time.time(); vals = []
        for _ in range(nreal):
            o = c2.hessians(rng.uniform(0, Lb, (Lb**3, 3)), Lb)
            vals.append(0.4*o['E_g'][1] + 0.6*o['T_2g'][1])   # 2 E_g + 3 T_2g directions of 5
        a = np.array(vals)
        print(f"iid box {Lb:2d} N={Lb**3:5d}: rot-avg E''/N = {a.mean():+.6f} +- {a.std(ddof=1)/np.sqrt(len(a)):.6f}  (sd {a.std(ddof=1):.5f}, n={nreal}) [{time.time()-t0:.0f}s]", flush=True)
