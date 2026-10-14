"""V4: the W0-matched octahedron grid pool (X0 = Y0 = 0 for all members; P2-type; t22_ring.py oct 0.15 1 1) rebuilt as
explicit links with a random gauge per member and evaluated with the INDEPENDENT builder."""
import numpy as np, time, resource
from t22lib import *
d = 0.6; h = 0.15; r = 2 * (d - 0.05); rng = np.random.default_rng(99)
ax = np.arange(-np.floor(r / h) * h, r + 1e-9, h)
G = np.array([(p, q, s) for p in ax for q in ax for s in ax if abs(p) + abs(q) + abs(s) <= r + 1e-12])
P, Q, R = G.T; p00, p10, p01 = (P + Q - R) / 2, (P - Q + R) / 2, (-P + Q + R) / 2
L = build_links(p00, p10, p01, 0 * P, 0 * P, rng=rng)
t0 = time.time(); Ki = kernel_matrix_indep(L, d); Kc = kernel_matrix_closed(L, d)
ei = np.linalg.eigvalsh(Ki); ec = np.linalg.eigvalsh(Kc); k = len(L); E = k * np.abs(Ki - Kc).max() + k * 1e-15 * ei[-1]
I = invariants(L)
print(f"RESULT V4 W0-matched oct grid h={h}: {k} configs, max|plaq| {max(np.abs(I[x]).max() for x in ('p00','p10','p01','p11')):.4f}, max|X0|,|Y0| "
      f"{np.abs(I['X0']).max():.1e},{np.abs(I['Y0']).max():.1e} | indep lam_min {ei[0]:+.5e} closed {ec[0]:+.5e} rel {ei[0]/ei[-1]:+.3e} | E {E:.1e} | "
      f"neg-converged {ei[0] < -10*E} | #neg {(ei < -10*E).sum()} | {time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
