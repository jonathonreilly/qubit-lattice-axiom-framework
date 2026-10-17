import sys, itertools, time
import numpy as np
sys.argv = [sys.argv[0], '4']
exec(open('spin.py').read())
from collections import Counter, defaultdict
def solve_multi(M, T):
    """M: (rows=eqs) x (cols=vars); T: eqs x k. Returns vars x k solution or None column-wise."""
    A = np.concatenate([M, T], axis=1).astype(np.uint8) % 2; m, nv = M.shape; piv = []; r = 0
    for c in range(nv):
        p = next((i for i in range(r, m) if A[i, c]), None)
        if p is None: continue
        A[[r, p]] = A[[p, r]]; rows = np.nonzero(A[:, c])[0]; rows = rows[rows != r]; A[rows] ^= A[r]; piv.append(c); r += 1
        if r == m: break
    ok = ~A[r:, nv:].any(axis=0)
    W = np.zeros((nv, T.shape[1]), np.uint8)
    for i, c in enumerate(piv): W[c] = A[i, nv:]
    return W, ok
def valid(G):
    M = np.array([np.concatenate([g[0], g[1]]) for g in G]); r, N = c1.f2_rank_and_null(M)
    for c in N:
        R_ = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
        for i in np.nonzero(c)[0]: R_ = mulp(R_, G[i])
        if R_[2] % 4: return False
    return True
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
summary = Counter()
for h, ords in classes.items():
    o = ords[0]
    stab = [Mr for Mr in O if H[bk.rot_order(Mr, o)] == h]
    for signs in itertools.product((0, 1), repeat=3):
        G, lab = gens(o, signs)
        Mg = np.array([np.concatenate([g[0], g[1]]) for g in G]).T
        for Mr in stab:
            perm = perm_of(Mr)
            imgs = [apply_perm(g, perm) for g in G]
            T = np.array([np.concatenate([im[0], im[1]]) for im in imgs]).T
            Wsol, ok = solve_multi(Mg, T)
            assert ok.all()
            bad = 0
            for j, im in enumerate(imgs):
                R_ = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
                for i in np.nonzero(Wsol[:, j])[0]: R_ = mulp(R_, G[i])
                bad += int(R_[2] != im[2])
            summary[(24 // len(stab), signs, bk.kind(Mr), bad > 0)] += 1
for k in sorted(summary): print(k, summary[k])
