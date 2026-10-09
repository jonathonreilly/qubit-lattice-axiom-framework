"""E3 (a2): long-wavelength noise of the local stiffness density on open patches (quasicrystal vs Poisson, same method).
Two estimators on interior sites (|x| < Rp - buf):
 (1) window variance: W(r) = sum_{|x_i - c| < r} (e''_i - mean) over balls of radius r with random centres inside the
     interior; report Var(W)/<n(r)>.  White noise (S(0) > 0): flat in r.  Hyperuniform (S(0) = 0): falls (~1/r or faster).
 (2) tapered structure factor S_F(k) = |sum_i (e''_i - mean) phi(x_i) e^{ik.x_i}|^2 / sum_i phi(x_i)^2, Gaussian taper
     phi = exp(-|x|^2/(2 w^2)), w = (Rp - buf)/2.5, averaged over k directions on shells |k| = 0.5 .. 3.
usage: python3 E3_a2_patch_noise.py file1.npz [file2.npz ...]"""
import numpy as np, sys
import e23_core as c
rng = np.random.default_rng(3)
for f in sys.argv[1:]:
    d = np.load(f); X, e2, Rp, buf = d['X'], d['e2'], float(d['Rp']), float(d['buf'])
    Ri = Rp - buf; m = np.linalg.norm(X, axis=1) < Ri
    Xi, Fi = X[m], e2[m] - e2[m].mean(0)          # 5 directions, centred
    print(f"== {f}: interior n={m.sum()}, Ri={Ri}")
    out = []
    for r in [0.75, 1.0, 1.5, 2.0, 2.5, 3.0]:
        if r > Ri - 1: break
        cs = rng.uniform(-(Ri - r), Ri - r, (6000, 3)); cs = cs[np.linalg.norm(cs, axis=1) < Ri - r][:3000]
        Ws, ns = [], []
        for cc in cs:
            sel = np.linalg.norm(Xi - cc, axis=1) < r
            Ws.append(Fi[sel].sum(0)); ns.append(sel.sum())
        Ws = np.array(Ws); out.append((r, np.mean(ns), (Ws**2).mean() / np.mean(ns)))
        print(f"   window r={r:4.2f} <n>={np.mean(ns):6.1f}  Var(W)/<n> = {(Ws**2).mean()/np.mean(ns):.3e}")
    w = Ri / 2.5; phi = np.exp(-np.einsum('ij,ij->i', Xi, Xi) / (2 * w**2))
    dirs = rng.standard_normal((200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    for k in [0.5, 0.75, 1.0, 1.5, 2.0, 3.0]:
        ph = np.exp(1j * k * Xi @ dirs.T)                       # n x 200
        S = np.abs((Fi[:, :, None] * (phi[:, None, None] * ph[:, None, :])).sum(0))**2 / np.sum(phi**2)
        print(f"   S_F(|k|={k:4.2f}) = {S.mean():.3e}   (per-site variance {np.mean(Fi**2):.3e}; taper resolution ~{1/w:.2f})")
