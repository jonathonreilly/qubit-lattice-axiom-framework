"""C5: frame-sensitive (angle-seeing) fermion sea on frozen point sets, label-blind couplings.

H = sum_{i!=j} w(d_ij) * i (alpha . n_ij) c_i^dag c_j  +  m sum_i beta c_i^dag c_i   (4-component Dirac)
where v_ij = exp(t h/2)(x_j - x_i) is the bond in an orthonormal frame of the metric g = exp(t h),
d = |v|, n = v/d, w = (1 - d^2/R^2)^4_+ (pairs recomputed from proper distance at every t).
Filled-sea energy per site E = -1/2 sum |lambda| / N. E''(0) by 3-point finite differences (t = 2e-3).
Prediction: crystal / hard-core nonzero; uniform iid zero in the ensemble mean (pushforward lemma covers
any construction that uses only orthonormal-frame bond vectors).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
import c2_pointset_shear_modulus as c2
rng = np.random.default_rng(4242)
R, m = 1.8, 1.0
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
alpha = [np.block([[Z2, s], [s, Z2]]) for s in (s1, s2, s3)]
beta = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)

def expm_sym(h, t):
    ev, U = np.linalg.eigh(h); return U @ np.diag(np.exp(t*ev)) @ U.T

def energy(X, Lb, h, t):
    n = len(X)
    D = X[None, :, :] - X[:, None, :]; D -= Lb*np.round(D/Lb)
    V = D @ expm_sym(h, t/2).T
    d2 = np.einsum('ijk,ijk->ij', V, V)
    I, J = np.nonzero((d2 < R**2) & (d2 > 0))
    d = np.sqrt(d2[I, J]); nv = V[I, J]/d[:, None]; w = (1 - d**2/R**2)**4
    Hm = np.zeros((4*n, 4*n), complex)
    blk = 1j*w[:, None, None]*sum(nv[:, a, None, None]*alpha[a][None] for a in range(3))
    for p in range(len(I)):
        i, j = I[p], J[p]; Hm[4*i:4*i+4, 4*j:4*j+4] += blk[p]
    for i in range(n): Hm[4*i:4*i+4, 4*i:4*i+4] += m*beta
    assert np.allclose(Hm, Hm.conj().T)
    lam = np.linalg.eigvalsh(Hm)
    return -0.5*np.sum(np.abs(lam))/n

def hess(X, Lb, t=2e-3):
    out = {}
    for ch in ('E_g', 'T_2g'):
        vals = []
        for h in c2.H[ch][:2]:
            e0 = energy(X, Lb, h, 0); ep = energy(X, Lb, h, t); em = energy(X, Lb, h, -t)
            vals.append((ep - 2*e0 + em)/t**2)
        out[ch] = np.mean(vals)
    return out

if __name__ == '__main__':
    Lb = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    nreal = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    N = Lb**3
    g = np.stack(np.meshgrid(*[np.arange(Lb)]*3, indexing='ij'), -1).reshape(-1, 3).astype(float)
    # step-size check on the crystal
    print(f"box {Lb} N={N}; crystal t=2e-3:", {k: round(v, 6) for k, v in hess(g, Lb, 2e-3).items()},
          " t=4e-3:", {k: round(v, 6) for k, v in hess(g, Lb, 4e-3).items()}, flush=True)
    for name, gen in [('hard-core RSA d0=0.80', lambda: c2.rsa(N, Lb, 0.80)),
                      ('uniform iid', lambda: rng.uniform(0, Lb, (N, 3)))]:
        t0 = time.time(); acc = {'E_g': [], 'T_2g': []}
        for _ in range(nreal):
            o = hess(gen(), Lb)
            for k in acc: acc[k].append(o[k])
        msg = " | ".join(f"{k}: {np.mean(v):+.5f} +- {np.std(v, ddof=1)/np.sqrt(len(v)):.5f}" for k, v in acc.items())
        print(f"{name:24s} {msg}   [{time.time()-t0:.0f}s, n={nreal}]", flush=True)
