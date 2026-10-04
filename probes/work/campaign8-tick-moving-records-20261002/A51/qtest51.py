"""A51 qtest51: unit test of releig_q (quotient eigen-solver) on random matrices against brute-force minimisation."""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from anal51 import releig_q
from scipy.optimize import minimize
rng = np.random.default_rng(5); n = 6
A = rng.normal(size=(n, n)); C = A @ A.T + 0.1 * np.eye(n)
B = rng.normal(size=(n, n)); G = B @ B.T; W = rng.normal(size=(n, 2))
GW = G @ W; Gp = G - GW @ np.linalg.solve(W.T @ GW, GW.T)          # rank n-2
lam, V = releig_q(C, Gp)
f = lambda c: (c @ C @ c) / max(c @ Gp @ c, 1e-14)
best = min(minimize(f, rng.normal(size=n), method="Nelder-Mead", options=dict(maxiter=20000, xatol=1e-10, fatol=1e-12)).fun for _ in range(20))
print(f"releig_q lam_min {lam[0]:.8f}; brute force {best:.8f}; ratio check at returned vector {f(V[:, 0]):.8f}")
# singular C null direction (Casimir-like: zero variance, zero covariance)
C2 = C.copy(); u = W[:, 0] / np.linalg.norm(W[:, 0]); Pp = np.eye(n) - np.outer(u, u); C2 = Pp @ C @ Pp
G2 = G - np.outer(G @ u, G @ u) / (u @ G @ u)
lam2, V2 = releig_q(C2, G2); print(f"zero-variance null direction: lam_min {lam2[0]:.6f} (finite, no blow-up)")
