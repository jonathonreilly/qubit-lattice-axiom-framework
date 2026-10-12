"""Born on-shell defect of the natural momentum P_j = 1/2{J_j,h} (symbol 1/2 sin 2k_j, scalar,
taste-universal slope 1) for interacting staggered fermions; plus a check that the Bloch
vectors used are eigenvectors of the real-space staggered h."""
import numpy as np, itertools
from s1_matrix_collision import *
from s1_shift_schur import lattice
rng = np.random.default_rng(77)
# eigenvector check
for d, L in ((2, 8), (3, 4)):
    model = Stag(d, 0.5, 'nn'); sites, h, S, T = lattice(d, L, 0.5)
    sarr = np.array(sites); worst = 0
    for _ in range(4):
        k = 2*np.pi*rng.integers(0, L, d)/L
        Um, Up, w = model.U(k)
        ps = (np.exp(1j*(sarr @ k))[:, None]*np.exp(1j*np.pi*(sarr @ model.As.T))) @ Up / np.sqrt(len(sites))
        worst = max(worst, np.linalg.norm(h @ ps - model.omega(k)[0]*ps))
    print(f"d={d}: ||h_realspace psi - omega psi|| max = {worst:.1e}")
for d in (2, 3):
    for inter in ('nn', 'cube'):
        for m in (0.5, 0.0):
            model = Stag(d, m, inter)
            procs = sample_processes(model, 1500 if d == 2 else 600, ALLCH, rng)
            lows = sample_processes(model, 300, [(1, 1, 1, 1)], rng, ball=0.35)
            for lab, pr in (('generic', procs), ('ee->ee in-states |k|<0.35 (out-states then also low)', lows)):
                num = den = 0; per = []
                for (s, k1, k2, k3, k4) in pr:
                    Us = []
                    for k, si in zip((k1, k2, k3, k4), s):
                        Um, Up, w = model.U(k); Us.append(Up if si > 0 else Um)
                    W = model.W((k1, k2, k3, k4), Us)
                    g = lambda k: 0.5*np.sin(2*k[0])
                    dg = g(k3) + g(k4) - g(k1) - g(k2)
                    num += (abs(dg)*np.linalg.norm(W))**2; den += np.linalg.norm(W)**2
                    per.append(abs(dg) if np.linalg.norm(W) > 1e-8 else 0)
                per = np.array(per)
                print(f"d={d} {inter} m={m} [{lab}, {len(pr)} procs]: W-weighted rms defect of 1/2 sin2k_x = {np.sqrt(num/den):.3e}; "
                      f"fraction of nonzero-amplitude processes with |defect|>1e-6: {np.mean(per > 1e-6):.3f}; max {per.max():.3f}")
