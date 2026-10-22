AUDIT_INPUT_PATHS = ('docs/EDGE_AND_SQUARE_GRAPH_WEIGHT_HAS_NO_CUBIC_ORDERED_PHASE_BOUNDED_NO_GO_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Ruleset B4 dimension test: does a graph with weight E = a*edges - b*(4-cycles)
order into a cubic lattice (degree 6, spectral dimension ~3) over a finite window
of b/a?  Exact single-move and ground-state bounds, plus seeded Metropolis
edge-toggle Monte Carlo (with and without a hard degree cap as a control).
Self-contained: numpy only.  Seeded.  Stdout < 6000 chars.
"""
AUDIT_TIMEOUT_SEC = 120

import sys
import time
import math
import numpy as np

T0 = time.time()
PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS" if ok else "FAIL") + ": " + name + (" | " + detail if detail else ""))


# ---------------------------------------------------------------- graphs
def torus(dims):
    n = int(np.prod(dims))
    A = np.zeros((n, n), dtype=np.int8)
    coords = np.array(np.unravel_index(np.arange(n), dims)).T
    for ax, L in enumerate(dims):
        c2 = coords.copy()
        c2[:, ax] = (c2[:, ax] + 1) % L
        j = np.ravel_multi_index(c2.T, dims)
        A[np.arange(n), j] = 1
        A[j, np.arange(n)] = 1
    np.fill_diagonal(A, 0)
    return A


def count_c4(A):
    """Number of 4-cycles = [tr A^4 - 2 sum d^2 + sum d] / 8 (exact, any simple graph)."""
    M = A.astype(np.int64)
    d = M.sum(1)
    A2 = M @ M
    return int((np.trace(A2 @ A2) - 2 * (d * d).sum() + d.sum()) // 8)


def giant(A):
    n = A.shape[0]
    seen = np.zeros(n, bool)
    best = []
    for s in range(n):
        if seen[s]:
            continue
        comp = [s]
        seen[s] = True
        k = 0
        while k < len(comp):
            for y in np.flatnonzero(A[comp[k]]):
                if not seen[y]:
                    seen[y] = True
                    comp.append(int(y))
            k += 1
        if len(comp) > len(best):
            best = comp
    return np.array(sorted(best))


def spectral_dim(A, t1=4, t2=12):
    """Lazy-walk return probability on the giant component, zero mode removed:
    d_s = -2 dln(P(t)-1/n)/dln t between t1 and t2."""
    g = giant(A)
    n = len(g)
    if n < 12:
        return float("nan"), n
    B = A[np.ix_(g, g)].astype(float)
    d = B.sum(1)
    S = B / np.sqrt(np.outer(d, d))           # symmetric normalised adjacency
    w = np.linalg.eigvalsh(S)
    lam = 0.5 * (1.0 + w)                     # lazy-walk eigenvalues
    lam = np.sort(lam)[:-1]                   # drop stationary mode
    P = lambda t: (lam ** t).sum() / n
    p1, p2 = P(t1), P(t2)
    if p1 <= 0 or p2 <= 0:
        return float("nan"), n
    return -2.0 * math.log(p2 / p1) / math.log(t2 / t1), n


def hausdorff_slope(A):
    """Mean ball volume B(r) on the giant component, slope dlnB/dln r for r=1..3."""
    g = giant(A)
    if len(g) < 12:
        return float("nan"), [0, 0, 0]
    B = A[np.ix_(g, g)].astype(np.int64)
    R = np.eye(len(g), dtype=np.int64)
    I1 = R + B
    vols = []
    for _ in range(3):
        R = np.minimum(R @ I1, 1)
        vols.append(float(R.sum(1).mean()))
    sl = np.polyfit(np.log([1, 2, 3]), np.log(vols), 1)[0]
    return float(sl), [round(v, 1) for v in vols]


# ---------------------------------------------------------------- Metropolis
def p3(A, u, v):
    """Paths u-x-y-v with x,y distinct from u,v (graph taken without edge uv) =
    number of 4-cycles created/destroyed by toggling uv."""
    nu = np.flatnonzero(A[u]); nu = nu[nu != v]
    nv = np.flatnonzero(A[v]); nv = nv[nv != u]
    if len(nu) == 0 or len(nv) == 0:
        return 0
    return int(A[np.ix_(nu, nv)].sum())


def metropolis(A, a, b, Tsched, rng, cap=None):
    n = A.shape[0]
    deg = A.sum(1).astype(int)
    m = int(deg.sum() // 2)
    c4 = count_c4(A)
    nmov = len(Tsched)
    U = rng.integers(0, n, nmov)
    V = rng.integers(0, n - 1, nmov)
    V = V + (V >= U)
    R = rng.random(nmov)
    acc = 0
    for k in range(nmov):
        u, v, T = int(U[k]), int(V[k]), Tsched[k]
        if A[u, v]:
            P = p3(A, u, v)
            dE = -a + b * P
            if dE <= 0 or R[k] < math.exp(-dE / T):
                A[u, v] = A[v, u] = 0
                deg[u] -= 1; deg[v] -= 1; m -= 1; c4 -= P; acc += 1
        else:
            if cap is not None and (deg[u] >= cap or deg[v] >= cap):
                continue
            P = p3(A, u, v)
            dE = a - b * P
            if dE <= 0 or R[k] < math.exp(-dE / T):
                A[u, v] = A[v, u] = 1
                deg[u] += 1; deg[v] += 1; m += 1; c4 += P; acc += 1
    return m, c4, acc


def octa_frac(A):
    """Local cubic order: fraction of vertices of degree 2D whose neighbours, joined when they
    share a square through v, form the cross-polytope link of Z^D (each neighbour joined to
    all but its opposite).  Z^3 -> 1; random regular graphs -> 0."""
    n = A.shape[0]; M = A.astype(np.int64); A2 = M @ M
    cnt = 0
    for v in range(n):
        nb = np.flatnonzero(A[v]); k = len(nb)
        if k < 4 or k % 2:
            continue
        S = (A2[np.ix_(nb, nb)] - 1) > 0
        np.fill_diagonal(S, False)
        if (S.sum(1) == k - 2).all() and (A2[np.ix_(nb, nb)][S] == 2).all():
            cnt += 1
    return cnt / n


def rand_regular(n, k, rng, nsw=20000):
    """Circulant start, then degree-preserving double-edge swaps."""
    A = np.zeros((n, n), np.int8)
    for i in range(n):
        for j in range(1, k // 2 + 1):
            A[i, (i + j) % n] = A[(i + j) % n, i] = 1
    for t in range(nsw):
        if t % 500 == 0:
            e = np.argwhere(np.triu(A, 1))
        (p, q), (x, y) = e[rng.integers(len(e))], e[rng.integers(len(e))]
        if len({p, q, x, y}) < 4 or A[p, y] or A[x, q] or not A[p, q] or not A[x, y]:
            continue
        A[p, q] = A[q, p] = A[x, y] = A[y, x] = 0
        A[p, y] = A[y, p] = A[x, q] = A[q, x] = 1
    return A


def measure(A):
    n = A.shape[0]
    d = A.sum(1)
    ds, ng = spectral_dim(A)
    dh, _ = hausdorff_slope(A)
    return dict(k=d.mean(), kmax=int(d.max()), c4v=count_c4(A) / n, ds=ds, dh=dh,
                g=ng, f6=float((d == 6).mean()), oc=octa_frac(A))


def fmt(r):
    return ("<k>=%5.2f kmax=%3d C4/v=%8.2f giant=%3d ds=%5.2f dH=%4.2f cub=%.2f"
            % (r["k"], r["kmax"], r["c4v"], r["g"], r["ds"], r["dh"], r["oc"]))


def is_cubic_like(r):
    # degree ~6, ds in the Z^3-torus band, AND local cubic order (ds alone is fooled, see 0.)
    return abs(r["k"] - 6) < 0.6 and 2.4 < r["ds"] < 4.0 and r["oc"] > 0.7


print("== Ruleset B4: E = a*#edges - b*#(4-cycles); a = 1")
# ---------------------------------------------------------------- 0. estimator calibration
print("-- 0. estimator calibration on exact tori")
cal = {}
for name, dims in [("Z1 ring 216", (216,)), ("Z2 15x15", (15, 15)), ("Z3 6^3", (6, 6, 6)),
                   ("Z4 4^4", (4, 4, 4, 4))]:
    A = torus(dims)
    ds, _ = spectral_dim(A)
    dh, vols = hausdorff_slope(A)
    cal[name] = (ds, dh)
    print("   %-12s ds=%.2f dH-slope=%.2f B(1..3)=%s" % (name, ds, dh, vols))
order_ok = cal["Z1 ring 216"][0] < cal["Z2 15x15"][0] < cal["Z3 6^3"][0] < cal["Z4 4^4"][0]
check("spectral-dimension estimator orders Z1<Z2<Z3<Z4", order_ok)
check("Z3 6^3 torus reads ds in [2.4,3.6]", 2.4 < cal["Z3 6^3"][0] < 3.6, "ds=%.2f" % cal["Z3 6^3"][0])
Z35 = measure(torus((5, 5, 5)))
RR6 = measure(rand_regular(125, 6, np.random.default_rng(7)))
print("   Z3 5^3        %s" % fmt(Z35))
print("   rand 6-reg 125 %s" % fmt(RR6))
check("local cubic order: Z3 5^3 -> 1, random 6-regular -> 0", Z35["oc"] == 1.0 and RR6["oc"] < 0.05)

# ---------------------------------------------------------------- 1. exact single-move window
print("-- 1. single-toggle stability of the cubic lattice (6^3 torus, exact)")
A = torus((6, 6, 6))
M = A.astype(np.int64)
A3 = M @ M @ M
d = M.sum(1)
E = M.astype(bool)
non = ~E & ~np.eye(len(d), dtype=bool)
sq_edge = (A3 - (d[:, None] + d[None, :] - 1))[E]          # triangle-free: squares per edge
p3_non = A3[non]                                            # paths of length 3 between non-neighbours
c4 = count_c4(A)
check("4-cycle formula: C4/vertex = 3 on Z^3", c4 == 3 * 216, "C4=%d" % c4)
check("every lattice edge lies in exactly 4 squares", sq_edge.min() == 4 and sq_edge.max() == 4)
check("max new 4-cycles from one added edge = 6 (body diagonal)", p3_non.max() == 6)
# removal stable iff -a + 4b >= 0 ; addition stable iff a - 6b >= 0
bl, bu = 1 / 4, 1 / 6
check("THEOREM: stability needs b/a >= 1/4 AND b/a <= 1/6: window EMPTY", bl > bu,
      "remove: b/a>=%.4f, add: b/a<=%.4f" % (bl, bu))

# ---------------------------------------------------------------- 2. exact ground-state bounds
print("-- 2. ground-state bounds (exact)")
# squares through edge uv <= (d_u-1)(d_v-1); C4 = (1/4) sum_e s_e
for N in (64, 125, 216):
    EK = lambda b: N * (N - 1) / 2 - b * 3 * math.comb(N, 4)
    EL = lambda b: 3 * N * (1 - b)
    # smallest b with E(K_N) < min(E_lattice, 0)
    bstar = (N * (N - 1) / 2) / (3 * math.comb(N, 4))
    print("   N=%3d: complete graph K_N beats empty AND lattice for b/a > %.2e" % (N, bstar))
check("uncapped: K_N wins for b/a > 4/((N-2)(N-3)) -> 0, non-extensive collapse",
      (216 * 215 / 2) / (3 * math.comb(216, 4)) < 1e-4)
# cap c: s_e <= (c-1)^2, edges/vertex <= c/2 => E/N >= e (a - b (c-1)^2/4), e in [0, c/2]
c = 6
bc = 4 / (c - 1) ** 2
print("   cap %d: ground state = empty for b/a < %.3f, disjoint K_{6,6} for b/a > %.3f" % (c, bc, bc))
print("   per vertex: K66 = %.2f*b vs lattice = 3b (C4 per vertex 18.75 vs 3)" % (225 / 12))
K66 = np.zeros((12, 12), np.int8); K66[:6, 6:] = 1; K66[6:, :6] = 1
check("K_{6,6} has (c-1)^2=25 squares per edge, C4=225", count_c4(K66) == 225)
check("THEOREM (cap 6): lattice is never the ground state for any b/a>0", 225 / 12 > 3)
print("   cap 6 metastability: additions blocked at degree 6, so lattice is a LOCAL min iff b/a>=1/4;")
print("   for Z^d with cap 2d the same holds iff b/a>=1/(2(d-1)): the cap, not B4, picks d.")

# ---------------------------------------------------------------- 3. Monte Carlo
rng = np.random.default_rng(20261022)
bs = [0.05, 0.12, 0.2, 0.3, 0.6, 1.2]
print("-- 3a. uncapped, start = 5^3 cubic torus, fixed T=0.15, 6 sweeps of all pairs")
N = 125; npair = N * (N - 1) // 2
res_lat = {}
for b in bs:
    A = torus((5, 5, 5))
    metropolis(A, 1.0, b, np.full(6 * npair, 0.15), rng)
    r = measure(A); res_lat[b] = r
    print("   b/a=%.2f %s" % (b, fmt(r)))
check("uncapped lattice start: no b/a keeps a cubic-like phase",
      not any(is_cubic_like(r) for r in res_lat.values()))

print("-- 3b. uncapped, start = random graph <k>=6, anneal T 2->0.15, N=64, 25 sweeps")
N = 64; npair = N * (N - 1) // 2
res_rand = {}
for b in bs:
    A = (rng.random((N, N)) < 6 / (N - 1)).astype(np.int8)
    A = np.triu(A, 1); A = (A + A.T).astype(np.int8)
    metropolis(A, 1.0, b, np.geomspace(2.0, 0.15, 25 * npair), rng)
    r = measure(A); res_rand[b] = r
    print("   b/a=%.2f %s" % (b, fmt(r)))
check("uncapped random start: no b/a reaches degree~6 with ds~3",
      not any(is_cubic_like(r) for r in res_rand.values()))
dense = [b for b, r in res_rand.items() if r["kmax"] > 20]
sparse = [b for b, r in res_rand.items() if r["k"] < 1.0]
check("uncapped phases are only 'empty' (small b) or 'dense clump' (large b)",
      len(dense) + len(sparse) == len(bs), "empty at %s, clump at %s" % (sparse, dense))

print("-- 3c. CONTROL cap=6, start = 5^3 torus, T=0.15, 6 sweeps")
N = 125; npair = N * (N - 1) // 2
res_cl = {}
for b in [0.12, 0.2, 0.3, 0.6, 1.2]:
    A = torus((5, 5, 5))
    metropolis(A, 1.0, b, np.full(6 * npair, 0.15), rng, cap=6)
    r = measure(A); res_cl[b] = r
    print("   b/a=%.2f %s" % (b, fmt(r)))
meta = [b for b, r in res_cl.items() if is_cubic_like(r)]
check("cap 6: lattice survives only at b/a >= 1/4 (metastable; b=0.3 melts at T=0.15)",
      len(meta) > 0 and all(b >= 0.25 for b in meta), "survives at %s" % meta)

print("-- 3d. CONTROL cap=6, random start (cap-pruned <k>~6), anneal T 2b->0.1b, N=64, 300 sweeps")
N = 64; npair = N * (N - 1) // 2
res_cr = {}
for b in [0.4, 1.2]:
    A = (rng.random((N, N)) < 6 / (N - 1)).astype(np.int8)
    A = np.triu(A, 1); A = (A + A.T).astype(np.int8)
    for i in range(N):
        nb = np.flatnonzero(A[i])
        if len(nb) > 6:
            for j in rng.choice(nb, len(nb) - 6, replace=False):
                A[i, j] = A[j, i] = 0
    metropolis(A, 1.0, b, np.geomspace(2.0 * b, 0.1 * b, 300 * npair), rng, cap=6)
    r = measure(A); res_cr[b] = r
    print("   b/a=%.2f %s" % (b, fmt(r)))
check("cap 6 from disorder: annealing never finds local cubic order (cub < 0.05)",
      all(r["oc"] < 0.05 for r in res_cr.values()))
check("cap 6 from disorder: C4/vertex > 2x lattice (flows toward K_{6,6} ground state)",
      all(r["c4v"] > 6 for r in res_cr.values()),
      "C4/v = %s (lattice 3, K66 18.75)" % [round(r["c4v"], 1) for r in res_cr.values()])

print("-- 3e. CONTROL: the cap picks the dimension (lattice start, b/a=1.2, T=0.15, 6 sweeps; 1.5 for 5^4)")
res_cap = {}
for cap, dims in [(4, (11, 11)), (6, (5, 5, 5)), (8, (5, 5, 5, 5))]:
    A = torus(dims); N = A.shape[0]
    metropolis(A, 1.0, 1.2, np.full(6 * N * (N - 1) // 2 // (4 if N > 300 else 1), 0.15), rng, cap=cap)
    r = measure(A); res_cap[cap] = r
    print("   cap=%d Z^%d start: %s" % (cap, len(dims), fmt(r)))
check("each cap c keeps Z^(c/2) metastable with ds ordered by c (cap inserts d)",
      all(res_cap[c]["oc"] > 0.9 for c in res_cap)
      and res_cap[4]["ds"] < res_cap[6]["ds"] < res_cap[8]["ds"],
      "ds = %s" % [round(res_cap[c]["ds"], 2) for c in (4, 6, 8)])

print("-- verdict: B4 gives NO cubic phase: the lattice is not even a local minimum of B4")
print("   (window empty, exact), ground states are empty or non-geometric clumps/bicliques;")
print("   a degree cap makes the lattice metastable only, and the cap value inserts d.")
el = time.time() - T0
check("runtime under 90 s", el < 90, "%.1f s" % el)
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
