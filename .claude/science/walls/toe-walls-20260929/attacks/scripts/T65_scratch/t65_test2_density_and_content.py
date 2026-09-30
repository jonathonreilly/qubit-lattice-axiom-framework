"""T65 Test 2: (2a) what a diluted Z^3 bond network carries as a coarse-grained metric;
(2b) helicity content of a q-independent polarisation tensor."""
import itertools
import numpy as np
from scipy.sparse import coo_matrix

# ---------- 2a ----------
classes = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)]
Lb = 12
V = Lb**3
def sid(x, y, z): return (x % Lb) * Lb * Lb + (y % Lb) * Lb + (z % Lb)
sites = list(itertools.product(range(Lb), repeat=3))
def build(qvec, rng):
    tails, heads, vec, cond = [], [], [], []
    for ci, v in enumerate(classes):
        w = 1.0 / (v[0]**2 + v[1]**2 + v[2]**2)
        keep = rng.random(V) >= qvec[ci]
        for i, (x, y, z) in enumerate(sites):
            if keep[i]:
                tails.append(sid(x, y, z)); heads.append(sid(x + v[0], y + v[1], z + v[2]))
                vec.append(v); cond.append(w)
    return np.array(tails), np.array(heads), np.array(vec, float), np.array(cond)
def sigma(qvec, rng):
    t, h, vec, c = build(qvec, rng)
    E = len(t)
    D = coo_matrix((np.r_[np.ones(E), -np.ones(E)], (np.r_[np.arange(E), np.arange(E)], np.r_[h, t])), shape=(E, V)).toarray()
    CV = c[:, None] * vec
    L = D.T @ (c[:, None] * D)
    B = D.T @ CV
    Lp = np.linalg.inv(L + np.ones((V, V)) / V)     # pseudo-inverse on the constant-free sector
    S = (vec.T @ CV - B.T @ Lp @ B) / V
    return S
rng = np.random.default_rng(11)
idx6 = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
def vec6(S): return np.array([S[i, j] for i, j in idx6])
S0 = np.mean([sigma(np.zeros(9), rng) for _ in range(1)], axis=0)
print("undiluted sigma0 diag:", np.round(np.diag(S0), 6), " offdiag max:", np.abs(S0 - np.diag(np.diag(S0))).max())
nsamp = 8
resp = {}
for q in (0.05, 0.10):
    R = np.zeros((6, 9))
    for ci in range(9):
        qv = np.zeros(9); qv[ci] = q
        Sm = np.mean([sigma(qv, rng) for _ in range(nsamp)], axis=0)
        R[:, ci] = vec6(Sm - S0) / q
    resp[q] = R
    sv = np.linalg.svd(R, compute_uv=False)
    print(f"q={q}: singular values of the 6x9 response: {np.round(sv, 4)}   rank(>1e-2 * max) = {(sv > 1e-2 * sv[0]).sum()}")
# alignment of each class response with -v v^T
print("cosine of each class response with -v v^T (q=0.10):")
for ci, v in enumerate(classes):
    vv = np.array(v, float); T = np.outer(vv, vv); tv = vec6(T)
    r = resp[0.10][:, ci]
    print(f"  class {v}: cos = {-(r @ tv) / (np.linalg.norm(r) * np.linalg.norm(tv)):.4f}  slope/w = {(-(r @ tv) / (tv @ tv)) * (v[0]**2+v[1]**2+v[2]**2):.3f}")
lin = np.linalg.norm(resp[0.10] - resp[0.05]) / np.linalg.norm(resp[0.05])
print(f"linearity: ||R(0.10) - R(0.05)|| / ||R(0.05)|| = {lin:.3f}")
# all classes diluted together at 0.1: compare with linear prediction
qv = np.full(9, 0.10)
Sm = np.mean([sigma(qv, rng) for _ in range(nsamp)], axis=0)
predv = vec6(S0) + resp[0.05].sum(axis=1) * 0.10
print(f"all classes at q=0.10: measured sigma diag {np.round(np.diag(Sm), 4)} ; linear prediction (sum of single-class responses) diag {np.round(predv[:3], 4)}; offdiag measured max {np.abs(Sm - np.diag(np.diag(Sm))).max():.4f}")

# ---------- 2b ----------
print("\n2b helicity content of a fixed polarisation tensor")
basis = []
for i in range(3):
    M = np.zeros((3, 3)); M[i, i] = 1; basis.append(M)
for i, j in [(0,1),(0,2),(1,2)]:
    M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1 / np.sqrt(2); basis.append(M)
def fractions(h, qh):
    P = np.eye(3) - np.outer(qh, qh)
    hTT = P @ h @ P - 0.5 * P * np.trace(P @ h)
    fTT = np.sum(hTT**2)
    u = P @ h @ qh
    f1 = 2 * np.sum(u**2)
    ft = np.sum(h**2)
    return fTT / ft, f1 / ft, (ft - fTT - f1) / ft
n = 3000
i = np.arange(n) + 0.5
phi = np.arccos(1 - 2 * i / n); th = np.pi * (1 + 5**0.5) * i
Q = np.c_[np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)]
def avg(h):
    f = np.array([fractions(h, q) for q in Q]); return f.mean(0), f.min(0), f.max(0)
rng = np.random.default_rng(3)
for name, h in [("e_xx - e_yy (traceless, E_g)", np.diag([1., -1., 0.]) / np.sqrt(2)),
                ("e_xy (traceless, T_2g)", basis[3]),
                ("trace delta/sqrt3", np.eye(3) / np.sqrt(3))] + \
               [("random traceless %d" % k, (lambda A: (A + A.T - 2 * np.trace(A) / 3 * np.eye(3)) / np.linalg.norm(A + A.T - 2 * np.trace(A) / 3 * np.eye(3)))(rng.normal(size=(3, 3)))) for k in range(3)]:
    m, lo, hi = avg(h)
    print(f"  {name:30s} mean (TT, +-1, 0) = ({m[0]:.4f}, {m[1]:.4f}, {m[2]:.4f});  min TT over q-hat = {lo[0]:.4f}, max TT = {hi[0]:.4f}")
