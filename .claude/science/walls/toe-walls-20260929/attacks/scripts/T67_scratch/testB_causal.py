"""T67 Test B: does a covariant formation clause on Z^3 give a Lorentzian-like event set?

Events = records (one per site, AX:79-80).  Dependency order: x < y iff there is a nearest-neighbour
path x = z0, z1, ..., zn = y with strictly increasing formation times (later record's odds depend on
earlier neighbours' records; Admissibility is nearest-neighbour).
Pre-registration: PREREG.md (B1, B2, B3).
"""
import numpy as np, time, sys
from numba import njit
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

OUT = []


def P(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.append(s)


def nbr_table(L):
    N = L ** 3
    idx = np.arange(N).reshape(L, L, L)
    tab = np.empty((N, 6), np.int64)
    for j, (ax, sh) in enumerate([(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]):
        tab[:, j] = np.roll(idx, sh, axis=ax).ravel()
    return tab


@njit(cache=True)
def sweep(order, rank, nbr, s, reach):
    N = order.shape[0]
    reach[:] = False
    reach[s] = True
    cnt = 1
    for r in range(rank[s] + 1, N):
        y = order[r]
        for j in range(6):
            if reach[nbr[y, j]]:
                reach[y] = True
                cnt += 1
                break
    return cnt


def displacement(L, s, ys):
    cs = np.array(np.unravel_index(s, (L, L, L)))
    cy = np.array(np.unravel_index(ys, (L, L, L)))
    d = cy - cs[:, None]
    d = (d + L // 2) % L - L // 2
    return d  # 3 x n


# ------------------------------------------------------------------ B1 + B2: iid clock
def run_iid(L, nsrc, rng):
    N = L ** 3
    t = rng.exponential(1.0, N)
    order = np.argsort(t)
    rank = np.empty(N, np.int64)
    rank[order] = np.arange(N)
    nbr = nbr_table(L)
    reach = np.zeros(N, np.bool_)
    sizes, ext1, extinf = [], [], []
    srcs = rng.choice(N, nsrc, replace=False)
    for s in srcs:
        c = sweep(order, rank, nbr, s, reach)
        ys = np.nonzero(reach)[0]
        d = displacement(L, s, ys)
        sizes.append(c)
        ext1.append(np.abs(d).sum(0).max())
        extinf.append(np.abs(d).max())
    return t, np.array(sizes), np.array(ext1), np.array(extinf)


P("== B1: event density of the iid Exp(1) clock (one permanent record per site) ==")
rng = np.random.default_rng(7)
t = rng.exponential(1.0, 200000)
edges = np.arange(0, 8.5, 1.0)
h, _ = np.histogram(t, bins=edges)
dens = h / len(t)
for a, b, x in zip(edges[:-1], edges[1:], dens):
    P(f"  t in [{a:.0f},{b:.0f}): events per site per unit time = {x:.4f}  (exp(-t) prediction {np.exp(-a)-np.exp(-b):.4f})")
P("  => the event density is not stationary: it is bounded by the site density (N events <= N sites) and decays as exp(-t).")

P("\n== B2: causal futures of the iid clock (only the order of labels matters, so rate-independent) ==")
for L in [24, 48, 72]:
    rng = np.random.default_rng(100 + L)
    t0 = time.time()
    _, sizes, e1, einf = run_iid(L, 300 if L < 72 else 200, rng)
    P(f"  L={L:3d}: future size mean {sizes.mean():8.1f}, max {sizes.max():7d}; max L1 extent: mean {e1.mean():5.2f}, max {e1.max():3d}; "
      f"max Linf extent: max {einf.max():3d}  ({time.time()-t0:.1f}s)")
mu = 4.684
P(f"  first-moment scale: e*mu(Z^3 SAW connective constant 4.684) = {np.e*mu:.1f}  (expected number of increasing self-avoiding paths of n steps <= 6*5^(n-1)/n!)")
for n in [10, 15, 20, 25, 30]:
    from math import factorial
    P(f"    n={n:2d}: 6*5^(n-1)/n! = {6*5**(n-1)/factorial(n):.3e}")

# ------------------------------------------------------------------ B3: nucleation clause
P("\n== B3: nucleation clause: rate eps of spontaneous formation + rate 1 per recorded neighbour (Richardson/FPP with sources) ==")


def run_nucleation(L, eps, nsrc, rng):
    N = L ** 3
    nbr = nbr_table(L)
    # undirected edge weights Exp(1); each site has 3 "forward" edges shared with neighbours
    W = rng.exponential(1.0, (N, 3))
    rows, cols, vals = [], [], []
    src_id = N
    X = rng.exponential(1.0 / eps, N)
    ii = np.arange(N)
    for a in range(3):
        j = nbr[:, 2 * a]  # +1 neighbour along axis a
        rows += [ii, j]; cols += [j, ii]; vals += [W[:, a], W[:, a]]
    rows.append(np.full(N, src_id)); cols.append(ii); vals.append(X)
    G = csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N + 1, N + 1))
    dist = dijkstra(G, directed=True, indices=src_id)
    T = dist[:N]
    order = np.argsort(T)
    rank = np.empty(N, np.int64)
    rank[order] = np.arange(N)
    reach = np.zeros(N, np.bool_)
    res = []
    # sources: random interior events
    srcs = rng.choice(N, nsrc, replace=False)
    for s in srcs:
        c = sweep(order, rank, nbr, s, reach)
        ys = np.nonzero(reach)[0]
        later = np.nonzero(T > T[s])[0]
        d_f = displacement(L, s, ys)
        d_l = displacement(L, s, later)
        res.append((s, c, len(later), d_f, d_l, T[ys] - T[s], T[later] - T[s]))
    return T, res


def classify(d):
    a = np.sort(np.abs(d), axis=0)[::-1].astype(float)  # 3 x n, descending
    m = np.maximum(a[0], 1e-9)
    b, c = a[1] / m, a[2] / m
    cls = np.full(d.shape[1], -1)
    cls[(b <= 0.25) & (c <= 0.25)] = 0   # axis
    cls[(b >= 0.75) & (c <= 0.25)] = 1   # face diagonal
    cls[(b >= 0.75) & (c >= 0.75)] = 2   # body diagonal
    return cls


L = 80
for eps in [2e-5]:
    rng = np.random.default_rng(555)
    t0 = time.time()
    T, res = run_nucleation(L, eps, 60, rng)
    P(f"  L={L}, eps={eps}: formation time range {T.min():.2f} .. {T.max():.2f}; ({time.time()-t0:.1f}s)")
    fut_frac_all, fut_frac_ball = [], []
    stats = {r: {0: [], 1: [], 2: []} for r in (6, 9, 12)}
    tot = {r: {0: [], 1: [], 2: []} for r in (6, 9, 12)}
    for (s, c, nl, d_f, d_l, dt_f, dt_l) in res:
        fut_frac_all.append(c / max(nl, 1))
        r1_f = np.abs(d_f).max(0)
        r1_l = np.abs(d_l).max(0)
        cf, cl = classify(d_f), classify(d_l)
        inball = r1_l <= 12
        fut_frac_ball.append(np.mean(np.isin(np.arange(len(dt_l))[inball], [])) if False else 0.0)
        for r in (6, 9, 12):
            for k in (0, 1, 2):
                sel_l = (cl == k) & (r1_l >= r - 1) & (r1_l <= r + 1)
                sel_f = (cf == k) & (r1_f >= r - 1) & (r1_f <= r + 1)
                if sel_l.sum() >= 3:
                    tot[r][k].append(sel_f.sum() / sel_l.sum())
                    if sel_f.sum() > 0:
                        stats[r][k].append(np.min(dt_f[sel_f]))
    P(f"  future size / number of later events (global): median {np.median(fut_frac_all):.3f}, mean {np.mean(fut_frac_all):.3f}")
    names = {0: "axis", 1: "face-diag", 2: "body-diag"}
    for r in (6, 9, 12):
        for k in (0, 1, 2):
            if tot[r][k]:
                P(f"    shell |d|_inf~{r:2d} {names[k]:9s}: P(later event is in future) median {np.median(tot[r][k]):.3f}; earliest future dt median {np.median(stats[r][k]) if stats[r][k] else float('nan'):.3f}")

# ---- B3 robustness: other nucleation rates
for eps in [2e-6, 2e-4]:
    rng = np.random.default_rng(556)
    T, res = run_nucleation(80, eps, 60, rng)
    fut = [c / max(nl, 1) for (s_, c, nl, *_r) in res]
    sizes = [c for (s_, c, nl, *_r) in res]
    ext = [np.abs(d_f).max() for (s_, c, nl, d_f, *_r) in res]
    P(f"  eps={eps}: future/later-events median {np.median(fut):.4f}; future size median {np.median(sizes):.0f}, max {max(sizes)}; max Linf extent of any future: {max(ext)}")

# ------------------------------------------------------------------ B3b: deterministic NN front (control: harness sees macroscopic cones)
P("\n== B3b: deterministic nearest-neighbour front from one seed: T = graph distance + tiny jitter (control) ==")
L = 81
N = L ** 3
rng = np.random.default_rng(99)
idx = np.arange(N).reshape(L, L, L)
c0 = L // 2
gx, gy, gz = np.meshgrid(np.arange(L) - c0, np.arange(L) - c0, np.arange(L) - c0, indexing="ij")
T = (np.abs(gx) + np.abs(gy) + np.abs(gz)).astype(float).ravel() + 1e-7 * rng.random(N)
nbr = nbr_table(L)
order = np.argsort(T); rank = np.empty(N, np.int64); rank[order] = np.arange(N)
reach = np.zeros(N, np.bool_)
acc = {k: [] for k in (0, 1, 2)}
speeds = {k: [] for k in (0, 1, 2)}
prob = {k: [] for k in (0, 1, 2)}
for _ in range(80):
    off = rng.integers(-12, 13, 3)
    if np.abs(off).max() < 4:
        continue
    s = int(idx[c0 + off[0], c0 + off[1], c0 + off[2]])
    sweep(order, rank, nbr, s, reach)
    ys = np.nonzero(reach)[0]
    later = np.nonzero(T > T[s])[0]
    d_f = displacement(L, s, ys); d_l = displacement(L, s, later)
    inr = np.abs(d_l).max(0) <= 12
    cl = classify(d_l); cf = classify(d_f)
    for k in (0, 1, 2):
        r = 9
        sel_l = (cl == k) & (np.abs(d_l).max(0) >= r - 1) & (np.abs(d_l).max(0) <= r + 1)
        sel_f = (cf == k) & (np.abs(d_f).max(0) >= r - 1) & (np.abs(d_f).max(0) <= r + 1)
        if sel_l.sum() > 0:
            prob[k].append(sel_f.sum() / sel_l.sum())
        if sel_f.sum() > 0:
            dtm = np.min((T[ys] - T[s])[sel_f])
            eu = np.sqrt((d_f[:, sel_f] ** 2).sum(0))
            j = np.argmin((T[ys] - T[s])[sel_f])
            speeds[k].append(eu[j] / dtm)
names = {0: "axis", 1: "face-diag", 2: "body-diag"}
for k in (0, 1, 2):
    P(f"  {names[k]:9s}: P(later event in future) mean {np.mean(prob[k]):.3f}; Euclidean speed of earliest future event r/dt = {np.mean(speeds[k]):.3f} (taxicab prediction {[1,1/np.sqrt(2),1/np.sqrt(3)][k]:.3f})")
P("  => a macroscopic cone exists only for a deterministic NN front, and its shape is the taxicab (L1) orthant, not a round Lorentz cone.")

open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T67_scratch/testB_output.txt", "w").write("\n".join(OUT) + "\n")
