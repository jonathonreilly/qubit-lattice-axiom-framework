import sys, pickle, itertools, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.')
import regge_generic as RG
from r2c import comp_inv
from rp import rp_matrix
HC = [(0,0),(1,1),(2,2),(3,3),(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]; itt, ixx = 3, 0
C = pickle.load(open('canon_1.pkl', 'rb'))
site = [i for i, o in enumerate(C.OFF) if np.allclose(o, 0)][0]
print("types", len(C.types), "edges", C.E, "site type", site, "offsets", [tuple(o) for o in C.OFF][:6], "...")
def G_nonsite(k):
    G = C.gauge(k); return np.hstack([G[:, 4*t:4*t+4] for t in range(len(C.types)) if t != site])
def reading(k, W=None):
    A = np.hstack([C.line_map(k), G_nonsite(k)]); n = A.shape[1]
    W = np.eye(C.E) if W is None else W
    X = np.linalg.solve(A.conj().T @ W @ A, A.conj().T @ W)        # left inverse of A
    return X[:10]
rng = np.random.default_rng(0); Wr = np.diag(rng.uniform(0.2, 5, C.E))
# consistency of the readings
k = np.array([0.3, -0.2, 0.1, 0.25])
for lab, W in (('plain', None), ('random weights', Wr)):
    L = reading(k, W); print(f"reading {lab}: |L G_nonsite| {np.abs(L @ G_nonsite(k)).max():.0e}, |L M - 1| {np.abs(L @ C.line_map(k) - np.eye(10)).max():.0e}")
# static responses
for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0]), np.array([0.01, -0.007, 0.012, 0.0])]:
    row = []
    for lab, W in (('plain', None), ('random', Wr)):
        L = reading(kk, W); T = np.zeros(10); T[itt] = 1.0
        x = comp_inv(C.Q(kk), C.gauge(kk), L.conj().T @ T); h = L @ x; k2 = kk @ kk
        row.append(f"{lab}: h_tt k^2 {h[itt].real*k2:+.4f}, h_xx/h_tt {(h[ixx]/h[itt]).real:+.4f}")
    print(f"|k|={np.linalg.norm(kk):.3f}: " + " | ".join(row))
