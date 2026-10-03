"""A41 d5: local dimension of the E = 0 set of H6 (pi flux) at theta = pi/2 (det H6 <= 0 everywhere, zeros come as
pairs) and, as controls, theta = 0 (Kramers pairs, surface det N = 0) and theta = pi/4 (single band crossing).
At a zero k0 with zero-mode projector P (n0 states): first-order effective Hamiltonian A_j = P^dag dH6/dk_j P.
Decompose each A_j into identity + Pauli parts (n0 = 2) -> a 3 x 4 real matrix D; the number of independent
linear conditions for the zero to persist = rank of D restricted to the parts that must vanish (all 4 for n0=2:
both eigenvalues zero), so local dimension of the zero set (where both stay zero) = 3 - rank(D).
Also: is there a symmetry C = (sigma_y K) x 1 with C H6 C^-1 = -H6 at theta = pi/2 (pointwise E -> -E)?"""
import os, signal
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from scipy.optimize import minimize
from common import *
rng = np.random.default_rng(19)
PAU = [np.eye(2), SIG[0], SIG[1], SIG[2]]
for th in (np.pi / 2, 0.0, np.pi / 4, 7 * np.pi / 16):
    M = M_family(th)
    k = rng.uniform(-np.pi, np.pi, 3)
    Cw = np.kron(SIG[1], np.eye(3))      # C = (sigma_y x 1) K
    phs = np.abs(Cw @ H6(k, M).conj() @ Cw.conj().T + H6(k, M)).max()
    f = lambda kk: np.abs(np.linalg.eigvalsh(H6(kk, M))).min()
    ranks = []; n0s = []
    for _ in range(12):
        r = minimize(f, rng.uniform(-np.pi, np.pi, 3), method="Nelder-Mead", options=dict(xatol=1e-13, fatol=1e-16, maxiter=2500))
        if r.fun > 1e-10: continue
        k0 = r.x; e, V = np.linalg.eigh(H6(k0, M)); sel = np.abs(e) < 1e-7; n0 = int(sel.sum()); P = V[:, sel]
        A = [(P.conj().T @ ((H6(k0 + 1e-6 * E3[j], M) - H6(k0 - 1e-6 * E3[j], M)) / 2e-6) @ P) for j in range(3)]
        if n0 == 2:
            D = np.array([[np.real(np.trace(Pm @ Aj)) / 2 for Pm in PAU] for Aj in A])
        else:
            D = np.array([[np.real(np.trace(Aj))] for Aj in A])
        sv = np.linalg.svd(D, compute_uv=False); ranks.append(int(np.sum(sv > 1e-6 * sv.max()))); n0s.append(n0)
    print(f"theta={th/np.pi:.4f} pi: |C H6 C^-1 + H6| at a random k = {phs:.1e}; zeros found {len(ranks)}/12; zero-mode counts "
          f"{sorted(set(n0s))}; rank of first-order conditions {sorted(set(ranks))} -> local dimension of the zero set "
          f"{sorted(set(3 - r for r in ranks))}")
