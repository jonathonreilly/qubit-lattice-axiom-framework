# candidate principle: reading = Euclidean (edge-length) Moore-Penrose dual of the line map, on all or on site-incident edges
from common import *
M0 = Dc.line_map(np.zeros(4)).real; Ls = strain_metric(Dc, np.zeros(4)).real
cls = {}
for (t1, t2, rel), c in Dc.ekey.items(): cls[c] = (t1, t2, round(float(np.linalg.norm(Dc.evec[c])), 4))
from collections import Counter
print("edge classes (type pair kinds, length):", Counter((min(1, t1) if t1 < 2 else 2, min(1, t2) if t2 < 2 else 2, l) for t1, t2, l in cls.values()))
Lp = np.linalg.pinv(M0)
print("|Lstrain - M^+_all72| / |Lstrain| =", np.linalg.norm(Ls - Lp) / np.linalg.norm(Ls))
used = np.where(np.abs(Ls).sum(0) > 1e-12)[0]; print("edges used by strain metric:", len(used))
Lu = np.zeros_like(Ls); Lu[:, used] = np.linalg.pinv(M0[used]); print("|Lstrain - M^+_used| / |Ls| =", np.linalg.norm(Ls - Lu) / np.linalg.norm(Ls))
# weighted pinv on used edges: weight w_e = l_e^p
le = np.array([np.linalg.norm(Dc.evec[c]) for c in range(Dc.E)])
for p in (-2, -1, 0, 1, 2):
    Wt = np.diag(le[used] ** p); Lw = np.zeros_like(Ls); Lw[:, used] = np.linalg.solve(M0[used].T @ Wt @ M0[used], M0[used].T @ Wt)
    print(f"weighted pinv w=l^{p}: misfit {np.linalg.norm(Ls - Lw)/np.linalg.norm(Ls):.2e}")
# is the Euclidean all-72 dual blind to non-site displacements at k != 0 (Bloch version)?
k = np.array([0.03, -0.02, 0.01, 0.025]); M = Dc.line_map(k); Lk = np.linalg.pinv(M); G = Dc.gauge(k)
print("M^+(k) blind to non-site:", np.abs(Lk @ np.hstack([G[:, 4*t:4*t+4] for t in range(1, 8)])).max(), " vs |M^+ G_site|", np.abs(Lk @ G[:, :4]).max())
