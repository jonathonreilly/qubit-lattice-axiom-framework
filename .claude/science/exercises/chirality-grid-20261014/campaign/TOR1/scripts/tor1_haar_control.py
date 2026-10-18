"""TOR-1 geometry control (F5): Wilson fermions (m = 0.05) with beta_g = 0 and NO admissibility cut (Haar crossing links). The
Wilson r = 1 determinant is a trigonometric polynomial of degree <= 1 in every link, so a 4-point trapezoid per crossing link is
exact; link-reflection positivity of Wilson fermions at beta = 0 (Osterwalder-Seiler) then demands a PSD kernel to roundoff.
Same pool, same joined geometry as tor1_kernel.py.  usage: python3 tor1_haar_control.py pool Lt"""
import sys, time
import numpy as np
from tor1_geom import *
fn, Lt = sys.argv[1], int(sys.argv[2]); S = Torus(4, Lt); T = Lt // 2; t0 = time.time()
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]; k = len(U)
g = 2 * np.pi * np.arange(4) / 4
grid = np.stack(np.meshgrid(*([g] * 7), indexing='ij'), -1).reshape(-1, 7)      # phi_1..3, chi_0..3 (phi_0 = 0)
def fields(ua, ub):
    A, _ = entry_fields(S, ua, ub, 1, 1); A0 = A[0]
    A = np.repeat(A0[None], len(grid), 0)
    A[:, S.key[('t', 0, 0)]] = 0.0
    for x in range(1, 4): A[:, S.key[('t', x, 0)]] = grid[:, x - 1]
    for x in range(4): A[:, S.key[('t', x, T)]] = grid[:, 3 + x]
    return A
L = np.zeros((k, k), complex)
for a in range(k):
    for b in range(a, k):
        A = fields(U[a], U[b]); l = np.concatenate([wilson_logdet(S, A[c:c+512], 0.05) for c in range(0, len(A), 512)])
        lm = l.real.max(); L[a, b] = lm + np.log(np.mean(np.exp(l - lm)) + 0j); L[b, a] = np.conj(L[a, b])
d = L.diagonal().real; Z = np.exp(L - 0.5 * (d[:, None] + d[None, :])); ev = np.linalg.eigvalsh(0.5 * (Z + Z.conj().T))
print(f"Wilson m=0.05, Haar crossing (no cut), {len(grid)} nodes/entry: lam_min {ev[0]:+.3e} max {ev[-1]:.4f} max|Im Z| {np.abs(Z.imag).max():.1e} "
      f"max|Im ln diag| {np.abs(L.diagonal().imag).max():.1e} [{time.time()-t0:.0f}s]")
# exactness check: 4-point vs 6-point trapezoid on one entry
g6 = 2 * np.pi * np.arange(6) / 6; sub = np.stack(np.meshgrid(*([g6] * 7), indexing='ij'), -1).reshape(-1, 7)
grid_save = grid; grid = sub; A = fields(U[0], U[1]); l = np.concatenate([wilson_logdet(S, A[c:c+512], 0.05) for c in range(0, len(A), 512)])
lm = l.real.max(); v6 = lm + np.log(np.mean(np.exp(l - lm)) + 0j)
print(f"entry (0,1): 4-point {L[0,1]:.12f} vs 6-point {v6:.12f}; |diff| {abs(L[0,1]-v6):.1e} [{time.time()-t0:.0f}s]")
