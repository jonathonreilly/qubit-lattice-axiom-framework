"""T65 Test 1: isotropy of the count-of-steps geometry of a recorded adjacency.
1a/1b periodic unweighted, 1c graded, 1d aperiodic random geometric graph."""
import itertools, sys, time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import breadth_first_order, shortest_path

def octahedral_orbit(v):
    a = sorted(set(itertools.permutations(v)))
    out = set()
    for p in a:
        for s in itertools.product([1, -1], repeat=3):
            out.add(tuple(pi * si for pi, si in zip(p, s)))
    return sorted(out)

def aniso(S, weights=None):
    """A = R_out / r_in of conv(s / w_s); gauge function N(u)=1/rho(u)."""
    S = np.array(S, float)
    if weights is not None:
        S = S / np.array(weights, float)[:, None]
    hull = ConvexHull(S)
    r_in = np.min(-hull.equations[:, 3])          # distance of facets from origin
    R_out = np.max(np.linalg.norm(S, axis=1))
    return R_out / r_in

# orbit representatives, max-norm <= 3
reps = [(a, b, c) for a in range(4) for b in range(a + 1) for c in range(b + 1) if a > 0]
orbits = {r: octahedral_orbit(r) for r in reps}
print("orbit representatives (max-norm<=3):", len(reps))

# ---- 1a: degree <= 26, all unions of orbits from max-norm<=1
r1 = [r for r in reps if r[0] <= 1]
print("\n1a periodic unweighted, orbits of the 26-neighbour star:")
best1a = None
for k in range(1, len(r1) + 1):
    for sub in itertools.combinations(r1, k):
        S = [v for r in sub for v in orbits[r]]
        A = aniso(S) if len(S) >= 6 else np.inf
        # need full-dimensional hull
        print(f"  orbits {sub}  D={len(S):3d}  A={A:.4f}")
        if best1a is None or A < best1a[0]:
            best1a = (A, sub, len(S))
print("  best A at D<=26:", best1a)

# ---- 1b: min A vs degree, exhaustive over unions of orbits with max-norm<=3, D<=150
print("\n1b min anisotropy vs degree (unions of orbits, max-norm<=3, D<=150):")
sizes = {r: len(orbits[r]) for r in reps}
t0 = time.time()
bestByD = {}
def rec(i, chosen, D):
    global bestByD
    if i == len(reps):
        if D >= 6 and chosen:
            S = [v for r in chosen for v in orbits[r]]
            try:
                A = aniso(S)
            except Exception:
                return
            key = D
            if key not in bestByD or A < bestByD[key][0]:
                bestByD[key] = (A, tuple(chosen))
        return
    rec(i + 1, chosen, D)
    r = reps[i]
    if D + sizes[r] <= 150:
        rec(i + 1, chosen + [r], D + sizes[r])
rec(0, [], 0)
print("  scanned in %.1fs; distinct degrees: %d" % (time.time() - t0, len(bestByD)))
# running minimum: best A achievable with degree <= D
Ds = sorted(bestByD)
run = []
m = np.inf
for D in Ds:
    m = min(m, bestByD[D][0]); run.append((D, m))
for D in [6, 12, 14, 18, 20, 24, 26, 30, 36, 50, 60, 74, 90, 110, 130, 150]:
    mm = min([v for d, v in run if d <= D], default=np.nan)
    print(f"  D<={D:3d}: min A = {mm:.4f}")
xs = np.array([d for d, v in run if d >= 26]); ys = np.array([v - 1 for d, v in run if d >= 26])
p = -np.polyfit(np.log(xs), np.log(ys), 1)[0]
print(f"  fit A-1 ~ D^-p (D>=26 running minimum): p = {p:.2f}")

# ---- 1c: graded weights on the 26 star
print("\n1c graded weights (axis a, face-diagonal b, body-diagonal c integers 1..N):")
star = [v for r in [(1,0,0),(1,1,0),(1,1,1)] for v in octahedral_orbit(r)]
cls = np.array([np.count_nonzero(v) for v in star])   # 1 axis, 2 face, 3 body
for N in [1, 2, 3, 4, 6, 8, 12, 16]:
    best = (np.inf, None)
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for c in range(1, N + 1):
                w = np.where(cls == 1, a, np.where(cls == 2, b, c))
                A = aniso(star, w)
                if A < best[0] - 1e-12: best = (A, (a, b, c))
    print(f"  N={N:2d}: min A = {best[0]:.4f} at weights {best[1]}")
w = np.linalg.norm(np.array(star, float), axis=1)
print(f"  Euclid weights (1, sqrt2, sqrt3): A = {aniso(star, w):.4f}")
big = [v for r in reps for v in orbits[r]]
w = np.linalg.norm(np.array(big, float), axis=1)
print(f"  Euclid weights, all vectors max-norm<=3 (D={len(big)}): A = {aniso(big, w):.4f}")
print(f"  reference: NN only A = {aniso(orbits[(1,0,0)]):.4f} (sqrt3 = {3**.5:.4f})")

# ---- 1d: aperiodic random geometric graph
print("\n1d Poisson random geometric graph, periodic 3-torus:")
def rgg_aniso(k, L=34.0, seed=0, nsrc=6, dlo=8.0, dhi=14.0, half_angle_deg=20.0):
    rng = np.random.default_rng(seed)
    N = rng.poisson(L**3)
    P = rng.random((N, 3)) * L
    r = (3 * k / (4 * np.pi)) ** (1 / 3)
    from scipy.spatial import cKDTree
    tree = cKDTree(P, boxsize=L)
    pairs = tree.query_pairs(r, output_type='ndarray')
    A = csr_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(N, N))
    A = A + A.T
    dirs = {}
    for v in [(1,0,0),(0,1,0),(0,0,1)]: dirs.setdefault('axis', []).append(np.array(v, float))
    for v in [(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)]: dirs.setdefault('face', []).append(np.array(v, float)/2**.5)
    for v in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]: dirs.setdefault('body', []).append(np.array(v, float)/3**.5)
    cosmin = np.cos(np.deg2rad(half_angle_deg))
    acc = {k_: [] for k_ in dirs}
    comp = 0
    for s in range(nsrc):
        src = rng.integers(N)
        d = shortest_path(A, method='D', unweighted=True, directed=False, indices=src)
        disp = P - P[src]; disp -= L * np.round(disp / L)
        dist = np.linalg.norm(disp, axis=1)
        msk = (dist > dlo) & (dist < dhi) & np.isfinite(d)
        comp += msk.sum()
        for name, vs in dirs.items():
            for v in vs:
                for sgn in (1, -1):
                    c = (disp @ (sgn * v)) / np.maximum(dist, 1e-9)
                    sel = msk & (c > cosmin)
                    if sel.sum() > 20:
                        acc[name].append(np.mean(d[sel] / dist[sel]))
    means = {name: np.mean(v) for name, v in acc.items()}
    allv = np.concatenate([np.array(v) for v in acc.values()])
    return means, allv.max() / allv.min(), np.mean(allv)
for k in [8, 16, 26, 50]:
    means, Aval, mean = rgg_aniso(k)
    print(f"  mean degree {k:2d}: hops/dist by class {{axis {means['axis']:.3f}, face {means['face']:.3f}, body {means['body']:.3f}}}  A_RGG = {Aval:.3f}  (mean stretch {mean:.3f})")
print("  reference periodic NN Z^3: hops/dist axis 1.000, face 1.414, body 1.732")
