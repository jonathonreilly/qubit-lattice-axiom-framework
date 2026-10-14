"""V1: explicit admissible pool on the T22 slice, no FFT, kernel from the INDEPENDENT builder on explicit links with a
random gauge transform per member, plus the closed form; full matrix eigenvalues. Pool = {R_a} x {X0_s = 2 pi s/N},
P = Q = 0 (phi = (-R/2, R/2, R/2, -R/2)), Y0 = 0 for all members (column Wilson lines matched).
Usage: python v1_direct_pool.py M N [DELTA]"""
import sys, time, resource, numpy as np
from t22lib import *
Mr = int(sys.argv[1]); N = int(sys.argv[2]); delta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.6
rng = np.random.default_rng(2026)
r = 2 * (delta - 0.05)
Rs = np.linspace(-r, r, Mr)
cfg = np.array([(R, 2 * np.pi * s / N) for R in Rs for s in range(N)])
R, X0 = cfg.T
p00, p10, p01 = -R / 2, R / 2, R / 2
L = build_links(p00, p10, p01, X0, 0 * X0, rng=rng)
I = invariants(L)
print(f"pool {len(L)} configs (M={Mr} R-values x N={N} X0-values); max|plaquette| {max(np.abs(I[k]).max() for k in ('p00','p10','p01','p11')):.4f}; "
      f"max|Y0|,|Y1| {np.abs(I['Y0']).max():.1e},{np.abs(I['Y1']).max():.1e}", flush=True)
t0 = time.time()
Kc = kernel_matrix_closed(L, delta)
Ki = kernel_matrix_indep(L, delta)
evc = np.linalg.eigvalsh(Kc); evi, V = np.linalg.eigh(Ki)
k = len(L); E = k * np.abs(Kc - Ki).max() + k * 1e-15 * np.abs(Ki).max()
print(f"closed: lam_min {evc[0]:+.6e} lam_max {evc[-1]:.6e} | indep: lam_min {evi[0]:+.6e} (rel {evi[0]/evi[-1]:+.4e}) | "
      f"max|Kc-Ki| {np.abs(Kc-Ki).max():.1e} | E {E:.1e} | negative eigenvalues: {(evi < -10*E).sum()}")
v = V[:, 0].reshape(Mr, N)
# structure of the negative eigenvector: dominant ring momentum per R-row
F = np.fft.fft(v, axis=1); pw = (np.abs(F) ** 2).sum(0); j = int(np.argmax(pw))
print(f"negative eigenvector: ring-momentum power peaks at j = {j} (|j| = {min(j, N-j)}), fraction {pw[j]/pw.sum():.3f}+{pw[(N-j)%N]/pw.sum():.3f} (+-j)")
print("profile over R of |F_j|:", np.round(np.abs(F[:, j]) / np.abs(F[:, j]).max(), 3))
print(f"RESULT V1 M={Mr} N={N} delta={delta}: indep lam_min {evi[0]:+.4e} rel {evi[0]/evi[-1]:+.3e} E {E:.1e} converged-negative {evi[0] < -10*E} "
      f"| {time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
np.save(f"pool_V1_M{Mr}_N{N}.npy", L)
