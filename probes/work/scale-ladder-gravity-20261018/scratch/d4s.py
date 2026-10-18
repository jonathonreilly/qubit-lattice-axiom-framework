import sys, itertools, numpy as np
sys.path.insert(0, '.')
from d4q import Lsym, C, HC, eidx
vec = lambda H: np.array([H[a, b] for a, b in HC])
SIGNS = [np.array([1, *s]) for s in itertools.product([1, -1], repeat=3)]
def body_reading(k):
    """8 rows: q_s = 4 delta l along the hypercube diagonal s through the centre vertex (type 1)."""
    k = np.asarray(k, complex); R = np.zeros((8, C.E), complex)
    for r, s in enumerate(SIGNS):
        v0 = tuple(int(x) for x in (1 - s)//2); v1 = tuple(int(x) for x in (1 - s)//2 + s)
        for a, b in ((v0, 0), ((0,0,0,0), 1)), (((0,0,0,0), 1), (v1, 0)):
            pass
        for (p, q) in (((v0, 0), ((0,0,0,0), 1)), (((0,0,0,0), 1), (v1, 0))):
            c, anc = eidx(p, q); R[r, c] += 4*np.exp(1j*k @ anc)
    return R
def body_from_h(): return np.array([[ (s[a]*s[b]*(2 if a != b else 1)) for (a, b) in HC] for s in SIGNS], float)
B0 = body_from_h()
# consistency on constant metrics
print("body reading exact on constant metrics:", np.abs(body_reading(np.zeros(4)) @ C.line_map(np.zeros(4)) - B0).max())
G = C.gauge(np.array([0.3, -0.2, 0.1, 0.25])); print("body reading blind to non-site displacements:", np.abs(body_reading(np.array([0.3, -0.2, 0.1, 0.25])) @ np.hstack([G[:, 4*t:4*t+4] for t in range(1, 8)])).max())
for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0.012, -0.009, 0.013, 0.004])]:
    Q = C.Q(kk); w, V = np.linalg.eigh(0.5*(Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    A = np.hstack([C.line_map(kk), C.gauge(kk)]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
    for j in range(2):
        p = partners[:, j]; hf = Lsym(kk) @ p; qb = body_reading(kk) @ p
        print(f"k={kk} partner {j}: face reading h = {np.round(hf.real, 3)}; body reading q_s = {np.round(qb.real, 3)}; face-implied q_s = {np.round((B0 @ hf).real, 3)}")
