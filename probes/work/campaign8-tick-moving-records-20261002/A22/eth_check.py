#!/usr/bin/env python3
"""A22 task 3 (supplied toy): are the Floquet eigenstates 'infinite temperature' (heated) or structured (prethermal)?
Same model as heat2.py (ring L, half filling).  For each step U(theta) (theta = pi/2: A19-type full-swap round + diagonal
interactions), diagonalise U and report, over all Floquet eigenstates, the spread of the H0 energy density
<H0>/L (structured => wide spread ~ the H0 spectrum; heated => all near the infinite-temperature value)
and of the local observable O = (1/L) sum n_s n_{s+1}."""
import sys, numpy as np, os
from itertools import combinations
L = int(sys.argv[1]); thetas = [float(x) for x in sys.argv[2].split(",")]; vs = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
m = 0.3; Jz = 0.5 * vs; J2 = 0.7 * vs; wo = 1 - 2 * m / np.pi
st = np.array(sorted(sum(1 << (L - 1 - s) for s in c) for c in combinations(range(L), L // 2)), dtype=np.int64)
D = st.size
bits = (st[:, None] >> (L - 1 - np.arange(L))[None, :]) & 1
Vd = (Jz * sum(bits[:, s] * bits[:, (s + 1) % L] for s in range(L)) + J2 * sum(bits[:, s] * bits[:, (s + 2) % L] for s in range(L))).astype(float)
bw = np.array([1.0 if s % 2 == 0 else wo for s in range(L)])
perms = []
for s in range(L):
    t = (s + 1) % L; bs, bt = bits[:, s], bits[:, t]
    perms.append(np.searchsorted(st, st ^ (((bs ^ bt) << (L - 1 - s)) | ((bs ^ bt) << (L - 1 - t)))))
H0 = np.diag(Vd).astype(complex)
for s in range(L):
    P = np.zeros((D, D)); P[np.arange(D), perms[s]] = 1.0; H0 += bw[s] * P
Od = sum(bits[:, s] * bits[:, (s + 1) % L] for s in range(L)) / L
ev = np.linalg.eigvalsh(H0)
print(f"L={L} dim={D} V-scale={vs}: H0 spectrum per site [{ev[0]/L:.3f}, {ev[-1]/L:.3f}], infinite-T <H0>/L = {np.trace(H0).real/D/L:.3f}, <O>_inf = {Od.mean():.4f}")
for th in thetas:
    U = np.eye(D, dtype=complex)
    for par, a in ((0, th), (1, th * wo)):
        for s in range(par, L, 2):
            U = np.cos(a) * U - 1j * np.sin(a) * U[perms[s], :]
    U = np.exp(-1j * th * Vd)[:, None] * U
    w, Vecs = np.linalg.eig(U)
    # orthonormalise within near-degenerate groups is not needed for expectation spreads at generic theta
    e = np.einsum("ik,ij,jk->k", Vecs.conj(), H0, Vecs).real / np.sum(np.abs(Vecs) ** 2, 0) / L
    o = (np.abs(Vecs) ** 2 * Od[:, None]).sum(0) / np.sum(np.abs(Vecs) ** 2, 0)
    print(f"  theta={th:.4f}: Floquet eigenstates <H0>/L: sd {e.std():.4f} (range {e.min():.3f}..{e.max():.3f});  <O>: sd {o.std():.4f}")
