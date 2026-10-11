# G1 check 1: number of connected components of level sets of
# Omega_K(q) = eps(q) + eps(K-q) on T^d, for TB and lattice KG.
# Grid-cell contour labelling with periodic wrap. Also tests whether, when there
# are 2 components, q -> K-q swaps them (needed for the fibre argument).
import numpy as np, sys
from scipy import ndimage
rng = np.random.default_rng(7)
def eps_tb(k): return -np.sum(np.cos(k), axis=0)
def eps_kg(m):
    return lambda k: np.sqrt(m*m + 2*np.sum(1-np.cos(k), axis=0))
def periodic_label(mask):
    d = mask.ndim
    st = np.ones((3,)*d, bool)
    lab, n = ndimage.label(mask, structure=st)
    parent = list(range(n+1))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[b] = a
    N = mask.shape[0]
    for ax in range(d):
        A = np.take(lab, 0, axis=ax); B = np.take(lab, N-1, axis=ax)
        # neighbours across the wrap including diagonals
        for sh in ([0] if d == 1 else [(s) for s in np.ndindex(*(3,)*(d-1))]):
            Bs = B
            if d > 1:
                for j, s in enumerate(sh):
                    Bs = np.roll(Bs, s-1, axis=j)
            sel = (A > 0) & (Bs > 0)
            for a, b in zip(A[sel], Bs[sel]):
                union(int(a), int(b))
    roots = {find(i) for i in range(1, n+1)}
    relab = np.zeros(n+1, int)
    for i in range(1, n+1): relab[i] = find(i)
    return relab[lab], len(roots)
def count(eps, d, N, K, E):
    g = np.linspace(-np.pi, np.pi, N, endpoint=False)
    Q = np.array(np.meshgrid(*([g]*d), indexing='ij'))
    Kb = K.reshape((d,)+(1,)*d)
    W = eps(Q) + eps(Kb - Q) - E
    # cell straddle test using corners (periodic)
    mn = W.copy(); mx = W.copy()
    for off in np.ndindex(*(2,)*d):
        Ws = W
        for ax, o in enumerate(off):
            if o: Ws = np.roll(Ws, -1, axis=ax)
        mn = np.minimum(mn, Ws); mx = np.maximum(mx, Ws)
    mask = (mn <= 0) & (mx >= 0)
    lab, n = periodic_label(mask)
    swapped = None
    if n == 2:
        # pick a contour cell q0, check label of K - q0
        idx = np.argwhere(lab > 0)[0]
        q0 = g[idx]
        q1 = (K - q0 + np.pi) % (2*np.pi) - np.pi
        j = np.round((q1 + np.pi) / (2*np.pi) * N).astype(int) % N
        # search a small neighbourhood for a contour cell
        labs = set()
        for off in np.ndindex(*(5,)*d):
            jj = tuple((j + np.array(off) - 2) % N)
            if lab[jj] > 0: labs.add(lab[jj])
        swapped = (lab[tuple(idx)] not in labs) if labs else None
    return n, swapped
def run(name, eps, d, N, nK, nE):
    hist = {}; bad = 0
    for _ in range(nK):
        K = rng.uniform(-np.pi, np.pi, d)
        g = np.linspace(-np.pi, np.pi, 64 if d == 2 else 24, endpoint=False)
        Q = np.array(np.meshgrid(*([g]*d), indexing='ij'))
        Om = eps(Q) + eps(K.reshape((d,)+(1,)*d) - Q)
        lo, hi = Om.min(), Om.max()
        for E in lo + (hi-lo)*rng.uniform(0.03, 0.97, nE):
            n, sw = count(eps, d, N, K, E)
            hist[n] = hist.get(n, 0) + 1
            if n == 2 and sw is False: bad += 1
    print(f"{name}: component-count histogram {dict(sorted(hist.items()))}; "
          f"2-component cases not swapped by q->K-q: {bad}", flush=True)
run("TB d=2", eps_tb, 2, 256, 40, 12)
run("KG m=1 d=2", eps_kg(1.0), 2, 256, 40, 12)
run("KG m=0.2 d=2", eps_kg(0.2), 2, 256, 40, 12)
run("KG m=0 d=2", eps_kg(0.0), 2, 256, 40, 12)
run("TB d=3", eps_tb, 3, 48, 10, 6)
run("KG m=1 d=3", eps_kg(1.0), 3, 48, 10, 6)
run("KG m=0.2 d=3", eps_kg(0.2), 3, 48, 10, 6)
