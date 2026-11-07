"""Kill test for library/a3-response.md (Lemma T, Theorem FL, Lemma C exactness), d = 2.

The proofs in Sections 2-4 are dimension-free in structure; a d = 2 run can refute
them, it cannot prove anything.  Registered criteria, written before the first run:

T1  single-level biorthogonality of the bumps phi_c: max |q_c'(phi_c) - delta_cc'| over
    pairs of the same level < 1e-12.                          FAIL refutes Lemma T (single level).
T2  full right inverse: max |q(T beta) - beta| < 1e-10 for 5 random beta.  FAIL refutes Lemma T.
T2b every non-zero cross-level reading |q_c'(phi_c)| > 1e-12 with level(c') != level(c)
    has c fine (level 1), c' an OUTWARD level-2 row.            FAIL refutes the triangularity claim.
T3  decay: unit datum at one row; f(t) := sum_{p: psi(p) >= t} |dA(p)|^2, psi = d_B-distance
    from the double block of the datum row.  PASS if f(t_h)/f(0) <= 1e-3 at t_h = t_max/2
    and a least-squares fit of log f on [1, t_h] has negative slope with R^2 > 0.9.
    FAIL (refutes FL) if f(t_h)/f(0) > 0.1.
T4  exactness: at the saddle solution max |Pi delta A| < 1e-8 and max |q(A) - B| < 1e-10.

Geometry: torus N x N, N = 81, L = 3; Omega_0 = Omega_1 = torus, Omega_2 = union of the
level-2 blocks (side 9) with centres in {27, 36, 45}^2; no layer 0.  Stops above 2 GB RSS.
"""
import sys, json, resource, heapq
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

N, L = 81, 3
s1, s2 = 3, 9
m1, m2 = 1, 4

def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1e9 if sys.platform == 'darwin' else r / 1e6

def guard():
    if rss_gb() > 2.0:
        print('RSS above 2 GB, stopping'); sys.exit(2)

def bid(x, y, mu):            # bond from (x,y) in direction mu
    return 2 * ((x % N) * N + (y % N)) + mu
def sid(x, y):
    return (x % N) * N + (y % N)
NB, NS = 2 * N * N, N * N

cent2 = [27, 36, 45]
def in_omega2(x, y):
    x %= N; y %= N
    for cx in cent2:
        for cy in cent2:
            if abs(x - cx) <= m2 and abs(y - cy) <= m2:
                return True
    return False
om2 = np.array([[in_omega2(x, y) for y in range(N)] for x in range(N)])

# ---- rows ----
rows = []   # (level, y=(yx,yy), mu, kind)
for yx in range(0, N, s1):
    for yy in range(0, N, s1):
        for mu in range(2):
            zx, zy = (yx + s1 * (mu == 0)) % N, (yy + s1 * (mu == 1)) % N
            if not om2[yx, yy] and not om2[zx, zy]:
                rows.append((1, (yx, yy), mu, 'int'))
for yx in range(0, N, s2):
    for yy in range(0, N, s2):
        for mu in range(2):
            zx, zy = (yx + s2 * (mu == 0)) % N, (yy + s2 * (mu == 1)) % N
            a, b = om2[yx, yy], om2[zx, zy]
            if a or b:
                rows.append((2, (yx, yy), mu, 'int' if (a and b) else 'out'))
NR = len(rows)

def row_vec(r):
    lev, (yx, yy), mu, _ = r
    s, m = (s1, m1) if lev == 1 else (s2, m2)
    v = {}
    for dx in range(-m, m + 1):
        for dy in range(-m, m + 1):
            x0, y0 = yx + dx, yy + dy
            for t in range(s):
                x, y = (x0 + t, y0) if mu == 0 else (x0, y0 + t)
                k = bid(x, y, mu)
                v[k] = v.get(k, 0.0) + 1.0 / s**2
    return v

Qm = sp.lil_matrix((NR, NB))
for i, r in enumerate(rows):
    for k, w in row_vec(r).items():
        Qm[i, k] += w
Qm = Qm.tocsr()
ROWIDX = {r: i for i, r in enumerate(rows)}
rows_index = ROWIDX

# ---- bumps (Lemma T in d = 2) ----
def profile_g(s, one_sided_sign=0):
    W = (s - 1) // 4
    g = {0: 1.0}
    if W >= 1:
        b = (W + 1) / (3 * W + 1)
        for w in range(1, 2 * W + 1):
            val = 1.0 if w <= W else -b
            if one_sided_sign >= 0: g[w] = val
            if one_sided_sign <= 0: g[-w] = val
    return g

def bump(r):
    lev, (yx, yy), mu, kind = r
    s, m = (s1, m1) if lev == 1 else (s2, m2)
    # one-sided toward the Omega_2 end for outward level-2 rows
    sign = 0
    if lev == 2 and kind == 'out':
        zx, zy = (yx + s * (mu == 0)) % N, (yy + s * (mu == 1)) % N
        sign = -1 if om2[yx, yy] else +1   # keep the side of the coarse pillar
    g = profile_g(s, sign)
    v = {}
    for w, gv in g.items():
        for dt in range(-m, m + 1):          # transverse
            h1 = (m + 1 - abs(dt)) / (m + 1)
            u = yx + m + w if mu == 0 else yy + m + w   # longitudinal coordinate of the bond
            if mu == 0: x, y = u, yy + dt
            else:       x, y = yx + dt, u
            k = bid(x, y, mu)
            v[k] = v.get(k, 0.0) + gv * h1
    vec = np.zeros(NB)
    for k, w in v.items(): vec[k] += w
    qv = np.asarray(Qm[ROWIDX[r]] @ vec).ravel()[0]
    return vec / float(qv)

Phi = np.zeros((NB, NR))
for i, r in enumerate(rows):
    Phi[:, i] = bump(r)
guard()
G = np.asarray(Qm @ Phi)        # G[c', c] = q_c'(phi_c)
lev = np.array([r[0] for r in rows]); kind = np.array([r[3] for r in rows])
same = lev[:, None] == lev[None, :]
E = G - np.eye(NR)
t1 = float(np.max(np.abs(E[same])))
cross = np.argwhere((~same) & (np.abs(G) > 1e-12))
t2b_ok = all(lev[c] == 1 and lev[cp] == 2 and kind[cp] == 'out' for cp, c in cross)
# triangular correction
fine = np.where(lev == 1)[0]; coarse_out = np.where((lev == 2) & (kind == 'out'))[0]
def T(beta):
    bt = beta.copy()
    corr = G[np.ix_(coarse_out, fine)] @ beta[fine]
    bt[coarse_out] = beta[coarse_out] - corr
    return Phi @ bt
rng = np.random.default_rng(1)
t2 = max(float(np.max(np.abs(Qm @ T(b) - b))) for b in rng.standard_normal((5, NR)))

# ---- operators d (bonds->plaquettes), delta (bonds->sites), Pi ----
dmat = sp.lil_matrix((NS, NB))
for x in range(N):
    for y in range(N):
        p = sid(x, y)   # plaquette at (x,y): +b(x,y,0) +b(x+1,y,1) -b(x,y+1,0) -b(x,y,1)
        dmat[p, bid(x, y, 0)] += 1; dmat[p, bid(x + 1, y, 1)] += 1
        dmat[p, bid(x, y + 1, 0)] -= 1; dmat[p, bid(x, y, 1)] -= 1
dmat = dmat.tocsr()
d0 = sp.lil_matrix((NB, NS))
for x in range(N):
    for y in range(N):
        for mu in range(2):
            x2, y2 = (x + (mu == 0), y + (mu == 1))
            d0[bid(x, y, mu), sid(x2, y2)] += 1; d0[bid(x, y, mu), sid(x, y)] -= 1
d0 = d0.tocsr(); delta = d0.T.tocsr()
# pillars: level-1 blocks in layer 1 (centres in 3Z^2 not in Omega_2), level-2 blocks in Omega_2
pillar = -np.ones(NS, dtype=int); pid = 0
for yx in range(0, N, s1):
    for yy in range(0, N, s1):
        if not om2[yx, yy]:
            for dx in range(-m1, m1 + 1):
                for dy in range(-m1, m1 + 1):
                    pillar[sid(yx + dx, yy + dy)] = pid
            pid += 1
for cx in range(0, N, s2):
    for cy in range(0, N, s2):
        if om2[cx, cy]:
            for dx in range(-m2, m2 + 1):
                for dy in range(-m2, m2 + 1):
                    pillar[sid(cx + dx, cy + dy)] = pid
            pid += 1
assert (pillar >= 0).all()
cnt = np.bincount(pillar)
Avg = sp.csr_matrix((1.0 / cnt[pillar], (pillar, np.arange(NS))), shape=(pid, NS))
Ext = sp.csr_matrix((np.ones(NS), (np.arange(NS), pillar)), shape=(NS, pid))
Pi = sp.identity(NS, format='csr') - Ext @ Avg
Kop = (dmat.T @ dmat + delta.T @ Pi @ delta).tocsr()
Sad = sp.bmat([[Kop, Qm.T], [Qm, None]], format='csc')
guard()

# ---- d_B distances on sites (Dijkstra, edge cost 1/s at the finer end) ----
scale = np.where(om2.ravel(), s2, s1).astype(float)
def dist_from(srcs):
    D = np.full(NS, np.inf); hq = []
    for s_ in srcs: D[s_] = 0.0; heapq.heappush(hq, (0.0, s_))
    while hq:
        dd, u = heapq.heappop(hq)
        if dd > D[u]: continue
        x, y = divmod(u, N)
        for ex, ey in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = sid(x + ex, y + ey)
            nd = dd + 1.0 / min(scale[u], scale[v])
            if nd < D[v]: D[v] = nd; heapq.heappush(hq, (nd, v))
    return D

def run_datum(ri):
    B = np.zeros(NR); B[ri] = 1.0
    rhs = np.concatenate([np.zeros(NB), B])
    sol = spla.spsolve(Sad, rhs); guard()
    A = sol[:NB]
    t4a = float(np.max(np.abs(Pi @ (delta @ A)))); t4b = float(np.max(np.abs(Qm @ A - B)))
    F = dmat @ A
    srcs = sorted({k // 2 for k in row_vec(rows[ri]).keys()})
    D = dist_from(srcs)
    psi = D            # plaquette at (x,y) located at its base site
    order = np.argsort(psi)
    tmax = float(psi.max()); th = tmax / 2
    def f(t): return float(np.sum(F[psi >= t] ** 2))
    f0 = f(0.0); ratio = f(th) / f0
    ts = np.linspace(1.0, th, 20); fs = np.array([f(t) for t in ts])
    ok = fs > 1e-25
    sl, ic = np.polyfit(ts[ok], np.log(fs[ok]), 1)
    pred = sl * ts[ok] + ic; ssr = np.sum((np.log(fs[ok]) - pred) ** 2)
    sst = np.sum((np.log(fs[ok]) - np.log(fs[ok]).mean()) ** 2); r2 = 1 - ssr / sst
    return dict(row=list(map(str, rows[ri])), t4_PiDeltaA=t4a, t4_rows=t4b, tmax=tmax,
                ratio_at_half=ratio, slope=float(sl), R2=float(r2))

r_fine = rows_index[(1, (6, 6), 0, 'int')]
cands = [i for i, r in enumerate(rows) if r[0] == 2 and r[3] == 'int']
r_coarse = cands[len(cands) // 2]
r_out = [i for i, r in enumerate(rows) if r[0] == 2 and r[3] == 'out'][0]
res = dict(NR=NR, T1_maxerr_same_level=t1, T2b_triangular=bool(t2b_ok), n_cross=int(len(cross)),
           T2_maxerr=t2, runs=[run_datum(r_fine), run_datum(r_coarse), run_datum(r_out)],
           rss_gb=rss_gb())
print(json.dumps(res, indent=1))
json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else 'fl_killtest_results.json', 'w'), indent=1)
