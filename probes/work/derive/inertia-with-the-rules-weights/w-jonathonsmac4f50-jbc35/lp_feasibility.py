"""numeric feasibility: 4^3 torus, three records, translation-reduced; unknown move/exchange rates by covariant range-1 environment; LP for positivity."""
import itertools, sys, time
import numpy as np
from fractions import Fraction as F
from scipy.sparse import coo_matrix, csr_matrix, hstack, identity
from scipy.optimize import linprog
L, n = 4, 3

def solve(pqr):
    global Wm, S_
    S_ = pqr[0] + pqr[1] + 4 * pqr[2]
    E = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    Wm = [[6 / S_ * (pqr[0] if a == b else pqr[1] if a == (b ^ 1) else pqr[2]) for b in range(6)] for a in range(6)]
    rots = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            R = np.array([[signs[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)])
            if round(np.linalg.det(R)) == 1: rots.append(R)
    IDX = {e: i for i, e in enumerate(E)}
    ROTC = [[IDX[tuple(int(v) for v in R @ np.array(E[d]))] for d in range(6)] for R in rots]
    def rel(x, y):
        return tuple(((y[i] - x[i] + L // 2) % L) - L // 2 for i in range(3))     # representative in {-2,-1,0,1}
    def l1(v): return sum(abs(t) for t in v)
    def add(x, d): return tuple((x[i] + E[d][i]) % L for i in range(3))
    def nbrs(x): return [add(x, d) for d in range(6)]
    def mu(cfg):
        v = 1.0
        for x, d in cfg.items():
            for y in nbrs(x):
                if y in cfg and x < y: v *= Wm[d][cfg[y]]
        return v
    def canon(cfg):
        best = None
        for x0 in cfg:                                   # translate each record to the origin, take the smallest
            k = tuple(sorted((tuple((z[i] - x0[i]) % L for i in range(3)), c) for z, c in cfg.items()))
            if best is None or k < best: best = k
        return best
    RV = [[tuple(int(v) for v in R @ np.array(u)) for u in itertools.product(range(-2, 2), repeat=3)] for R in rots]
    UIDX = {u: i for i, u in enumerate(itertools.product(range(-2, 2), repeat=3))}
    def envkey(kind, cfg, x, y):
        d = cfg[x]; dp = cfg.get(y)
        others = [(rel(x, z), c) for z, c in cfg.items() if z not in (x, y) and min(l1(rel(x, z)), l1(rel(y, z))) <= 1]
        best = None
        for ri, R in enumerate(rots):
            k = (kind, ROTC[ri][d], None if dp is None else ROTC[ri][dp], tuple(sorted((tuple(int(v) for v in R @ np.array(rz)), ROTC[ri][c]) for rz, c in others)))
            if best is None or k < best: best = k
        return best
    t0 = time.time()
    sites = list(itertools.product(range(L), repeat=3))
    reps = {}
    origin = (0, 0, 0)
    for pair in itertools.combinations([s for s in sites if s != origin], 2):
        occ = (origin,) + pair
        for cont in itertools.product(range(6), repeat=3):
            cfg = dict(zip(occ, cont))
            c = canon(cfg)
            if c not in reps: reps[c] = len(reps)
    pass  # print(f"{len(reps)} translation classes ({time.time()-t0:.0f}s)", flush=True)
    keys = {}; rows = []; cols = []; vals = []; b = np.zeros(len(reps))
    for c, i in reps.items():
        cfg = dict(c); m_c = mu(cfg)
        for x, d in cfg.items():
            y = add(x, d); kind = "move" if y not in cfg else "exch"
            new = dict(cfg)
            if kind == "move": del new[x]; new[y] = d
            else: new[x], new[y] = cfg[y], d
            j = reps[canon(new)]
            k = envkey(kind, cfg, x, y)
            if k[0] == "move" and k[3] == ():
                b[j] -= m_c; b[i] += m_c; continue
            if k not in keys: keys[k] = len(keys)
            rows += [j, i]; cols += [keys[k], keys[k]]; vals += [m_c, -m_c]
    A = coo_matrix((vals, (rows, cols)), shape=(len(reps), len(keys))).tocsr()
    pass  # print(f"{len(keys)} rate classes; assembling done ({time.time()-t0:.0f}s)", flush=True)
    nv = A.shape[1]
    c_obj = np.zeros(nv + 1); c_obj[-1] = -1
    Aeq = hstack([A, csr_matrix((A.shape[0], 1))]).tocsr()
    Aub = hstack([-identity(nv, format="csr"), csr_matrix(np.ones((nv, 1)))]).tocsr()
    res = linprog(c_obj, A_ub=Aub, b_ub=np.zeros(nv), A_eq=Aeq, b_eq=b, bounds=[(None, 20)] * (nv + 1), method="highs")
    return None if res.x is None else float(res.x[-1])
    print(f"(p,q,r)={pqr}: LP status {res.status} ({res.message[:60]}); max min-rate = {None if res.x is None else round(res.x[-1], 6)} ({time.time()-t0:.0f}s)", flush=True)