"""E2-0 validation: (1) real-space crystal vs k-space (both couplings, boson + fermion);
(2) finite-difference check of the exact Hessian on one diluted realization (both couplings, boson + fermion);
(3) small-p analytic slope (isolated-pair expansion) for both couplings."""
import numpy as np, os
os.environ.setdefault('OMP_NUM_THREADS', '4')
import e23_core as c

m2 = 1.0
MU, TF = {'pd': 2.0, 'nn': 6.0}, 0.1     # fermion sea: H = L_g, mu fixed, smearing T (supplied)
rng = np.random.default_rng(1)
Lb = 8
g = np.stack(np.meshgrid(*[np.arange(Lb)] * 3, indexing='ij'), -1).reshape(-1, 3).astype(float)

for mode in ['pd', 'nn']:
    fb = c.boson_fns(m2); ff = c.fermion_fns(MU[mode], TF)
    I, J, D = c.pairs(g, Lb, mode)
    out, lam = c.derivs(len(g), I, J, D, mode, [fb, ff])
    for k, name in enumerate(['boson', 'fermion']):
        ks = c.kspace_Z3(mode, [fb, ff][k], M=Lb)
        ks64 = c.kspace_Z3(mode, [fb, ff][k], M=64)
        rs = {ch: (out[k, idx, 0].mean(), out[k, idx, 1].mean()) for ch, idx in c.CH.items()}
        print(f"[{mode}] {name}: real-space L={Lb}: E_g {rs['E_g'][1]:+.7f} T_2g {rs['T_2g'][1]:+.7f} | k-space M={Lb}: "
              f"{ks['E_g'][1]:+.7f} {ks['T_2g'][1]:+.7f} | k-space M=64: {ks64['E_g'][1]:+.7f} {ks64['T_2g'][1]:+.7f}"
              f" | stress {rs['E_g'][0]:+.1e} {rs['T_2g'][0]:+.1e}")

# FD check on a diluted realization (p = 0.7): pairs/weights recomputed at metric exp(t h)
X = g[rng.random(len(g)) < 0.7]
for mode in ['pd', 'nn']:
    I, J, D = c.pairs(X, Lb, mode)
    out, _ = c.derivs(len(X), I, J, D, mode, [c.boson_fns(m2)])
    for d in [0, 2]:
        h = c.DIRS[d]; t = 2e-3
        e = [c.energy_total(X, Lb, mode, c.expm_sym(h, s * t), m2) for s in (-2, -1, 0, 1, 2)]
        fd2 = (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * t**2)
        fd1 = (e[0] - 8 * e[1] + 8 * e[3] - e[4]) / (12 * t)
        print(f"FD [{mode}] p=0.7 dir {d}: E' exact {out[0, d, 0]:+.9f} fd {fd1:+.9f} | E'' exact {out[0, d, 1]:+.9f} fd {fd2:+.9f}")

# fermion FD (grand potential), pd, p = 0.7
def omega(X, Lb, mode, G, mu, T):
    n = len(X); I, J, D = c.pairs(X, Lb, mode, G=G)
    s = np.einsum('pi,ij,pj->p', D, G, D); w = c.kernel(mode, s)[0]
    lam = np.clip(np.linalg.eigvalsh(c.lap_dense(n, I, J, w)), 0, None)
    return np.sum(-T * np.logaddexp(0, -(lam - mu) / T)) / n
for mode in ['pd', 'nn']:
    I, J, D = c.pairs(X, Lb, mode)
    out, _ = c.derivs(len(X), I, J, D, mode, [c.fermion_fns(MU[mode], TF)])
    h = c.DIRS[2]; t = 2e-3
    e = [omega(X, Lb, mode, c.expm_sym(h, s * t), MU[mode], TF) for s in (-2, -1, 0, 1, 2)]
    fd2 = (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * t**2)
    print(f"FD fermion [{mode}] p=0.7 T_2g dir: E'' exact {out[0, 2, 1]:+.9f} fd {fd2:+.9f}")

# small-p slope: per present site, E''/N = (p/2) sum_{n != 0} d^2/dt^2 eps(w(|n|_g)) + O(p^2),
# eps(w) = 1/2 (sqrt(2w + m2) - sqrt(m2))  (isolated pair: eigenvalues 0 and 2w)
def eps_dd(w, w1, w2):
    e1 = 0.5 / np.sqrt(2 * w + m2); e2 = -0.5 / (2 * w + m2)**1.5
    return e1 * w2 + e2 * w1**2
for mode in ['pd', 'nn']:
    ns = np.array([(a, b, cc) for a in range(-2, 3) for b in range(-2, 3) for cc in range(-2, 3) if (a, b, cc) != (0, 0, 0)], float)
    s = np.einsum('pk,pk->p', ns, ns)
    ns = ns[(s < c.R_PD**2) if mode == 'pd' else (np.abs(s - 1) < 1e-9)]
    s = np.einsum('pk,pk->p', ns, ns)
    w, w1s, w2s = c.kernel(mode, s)
    res = {}
    for ch, idx in c.CH.items():
        v = []
        for d in idx:
            h = c.DIRS[d]
            sp = np.einsum('pi,ij,pj->p', ns, h, ns); spp = np.einsum('pi,ij,pj->p', ns, h @ h, ns)
            v.append(0.5 * np.sum(eps_dd(w, w1s * sp, w2s * sp**2 + w1s * spp)))
        res[ch] = np.mean(v)
    print(f"small-p slope [{mode}] boson: E''/N ~ p * ({res['E_g']:+.6f} E_g, {res['T_2g']:+.6f} T_2g)  (EXACT isolated-pair term)")
