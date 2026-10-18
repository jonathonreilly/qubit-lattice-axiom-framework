import sys, itertools, numpy as np
sys.path.insert(0, '.')
from d4m import L, C, HC
vec = lambda H: np.array([H[a, b] for a, b in HC])
pats = {}
for sg in itertools.product([1, -1], repeat=3):
    u = np.array([1, *sg], float); pats[str(sg)] = vec(2*np.eye(4) - np.outer(u, u))
rng = np.random.default_rng(5)
for t in range(4):
    k = 0.02*rng.standard_normal(4)
    Q = C.Q(k); w, V = np.linalg.eigh(0.5*(Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    M = C.line_map(k); G = C.gauge(k); A = np.hstack([M, G]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
    H = L(k) @ partners                         # 10 x 2
    # gauge-reduce: remove continuum-like lattice gauge of the site metric (forward differences)
    Gs = np.array([vec(np.outer(np.exp(1j*k)-1, e) + np.outer(e, np.exp(1j*k)-1)) for e in np.eye(4)]).T
    Pr = np.eye(10) - Gs @ np.linalg.pinv(Gs)
    Hr = Pr @ H
    ov = {nm: np.linalg.norm(np.linalg.pinv(Hr) @ (Pr @ p)) * 0 + np.linalg.norm(Hr @ np.linalg.pinv(Hr) @ (Pr @ p))/np.linalg.norm(Pr @ p) for nm, p in pats.items()}
    print(f"k#{t}: fraction of each tilt pattern 2*1 - u u^T (u = (1,s1,s2,s3)) inside the partners' site-metric span:", {k_: round(v, 3) for k_, v in ov.items()})
