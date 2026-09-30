"""T65 Test 1 addenda (run after seeing the first output; changes disclosed in RESULTS.md):
 (i) ball-shaped unweighted generating sets: A(D) scaling with degree (the first 1b plateaued
     because vectors were capped at max-norm 3);
 (ii) real-valued 3-parameter weights on the 26 star: the floor of A;
 (iii) aperiodic RGG with a line-averaged estimator (13 direction lines, +/- pooled,
     40 sources, bootstrap over sources), with a Z^3 NN graph run through the SAME estimator
     as a control that must show ~1.73."""
import itertools
import numpy as np
from scipy.spatial import ConvexHull, cKDTree
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

def aniso(S, w=None):
    S = np.array(S, float)
    if w is not None: S = S / np.array(w, float)[:, None]
    h = ConvexHull(S)
    return np.max(np.linalg.norm(S, axis=1)) / np.min(-h.equations[:, 3])

print("(i) unweighted ball sets {v in Z^3 : 0<|v|^2<=m}: degree D and anisotropy A")
rows = []
for m in [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 24, 30, 40, 60, 100, 200, 400]:
    R = int(np.floor(np.sqrt(m)))
    S = [v for v in itertools.product(range(-R, R + 1), repeat=3) if 0 < sum(x * x for x in v) <= m]
    rows.append((m, len(S), aniso(S)))
    print(f"  m={m:4d}  D={len(S):5d}  A={rows[-1][2]:.4f}")
D = np.array([r[1] for r in rows if r[1] >= 26]); A = np.array([r[2] - 1 for r in rows if r[1] >= 26])
p = -np.polyfit(np.log(D), np.log(A), 1)[0]
print(f"  fit A-1 ~ D^-p over D>=26: p = {p:.2f}")
for target in [0.05, 0.01]:
    ok = [r for r in rows if r[2] - 1 <= target]
    print(f"  smallest ball set with A<={1+target}: {ok[0] if ok else 'not reached (D up to %d)' % rows[-1][1]}")

print("\n(ii) real weights (a,b,c) on the 26-star: floor of A")
star = [v for v in itertools.product([-1, 0, 1], repeat=3) if any(v)]
cls = np.array([np.count_nonzero(v) for v in star])
f = lambda x: aniso(star, np.where(cls == 1, 1.0, np.where(cls == 2, np.exp(x[0]), np.exp(x[1]))))
best = min((minimize(f, x0, method='Nelder-Mead') for x0 in [(0.3, 0.5), (0.0, 0.0), (0.6, 0.9)]), key=lambda r: r.fun)
print(f"  min over continuous weights: A = {best.fun:.4f} at (1, {np.exp(best.x[0]):.3f}, {np.exp(best.x[1]):.3f})")

print("\n(iii) line-averaged hop/Euclid anisotropy, 13 lines, 40 sources")
lines = [np.array(v, float) / np.linalg.norm(v) for v in
         [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1),(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]]
cosmin = np.cos(np.deg2rad(20))
def estimate(P, L, A, nsrc, rng, dlo=8.0, dhi=14.0):
    N = len(P)
    per_src = np.full((nsrc, len(lines)), np.nan)
    for s in range(nsrc):
        src = rng.integers(N)
        d = shortest_path(A, method='D', unweighted=True, directed=False, indices=src)
        disp = P - P[src]; disp -= L * np.round(disp / L)
        dist = np.linalg.norm(disp, axis=1)
        msk = (dist > dlo) & (dist < dhi) & np.isfinite(d)
        for i, v in enumerate(lines):
            c = np.abs(disp @ v) / np.maximum(dist, 1e-9)       # +/- pooled
            sel = msk & (c > cosmin)
            if sel.sum() > 20: per_src[s, i] = np.mean(d[sel] / dist[sel])
    return per_src
def summarize(per_src, rng):
    m = np.nanmean(per_src, axis=0); Aval = m.max() / m.min()
    boots = []
    for _ in range(200):
        idx = rng.integers(0, per_src.shape[0], per_src.shape[0]); mb = np.nanmean(per_src[idx], axis=0)
        boots.append(mb.max() / mb.min())
    return Aval, np.std(boots), m
# control: periodic Z^3 nearest-neighbour graph through the same estimator
L = 34; g = np.arange(L)
P = np.array(list(itertools.product(g, g, g)), float)
idx = lambda x, y, z: (x % L) * L * L + (y % L) * L + (z % L)
rows_, cols_ = [], []
for x, y, z in itertools.product(g, g, g):
    for dx, dy, dz in [(1,0,0),(0,1,0),(0,0,1)]:
        rows_.append(idx(x, y, z)); cols_.append(idx(x + dx, y + dy, z + dz))
Az = csr_matrix((np.ones(len(rows_)), (rows_, cols_)), shape=(L**3, L**3)); Az = Az + Az.T
rng = np.random.default_rng(5)
ps = estimate(P, L, Az, 40, rng); Aval, sd, m = summarize(ps, rng)
print(f"  control Z^3 NN graph: A = {Aval:.3f} +/- {sd:.3f}   (axis mean {m[:3].mean():.3f}, face {m[3:9].mean():.3f}, body {m[9:].mean():.3f}; exact 1, 1.414, 1.732)")
for k in [8, 16, 26, 50]:
    rng = np.random.default_rng(100 + k)
    Lr = 34.0; N = rng.poisson(Lr**3); Pr = rng.random((N, 3)) * Lr
    r = (3 * k / (4 * np.pi)) ** (1 / 3)
    pairs = cKDTree(Pr, boxsize=Lr).query_pairs(r, output_type='ndarray')
    Ar = csr_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(N, N)); Ar = Ar + Ar.T
    ps = estimate(Pr, Lr, Ar, 40, rng); Aval, sd, m = summarize(ps, rng)
    print(f"  RGG mean degree {k:2d}: A = {Aval:.3f} +/- {sd:.3f}   (axis mean {m[:3].mean():.3f}, face {m[3:9].mean():.3f}, body {m[9:].mean():.3f})")
