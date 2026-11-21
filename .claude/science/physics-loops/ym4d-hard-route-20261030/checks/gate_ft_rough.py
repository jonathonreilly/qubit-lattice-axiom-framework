#!/usr/bin/env python3
"""Exact checks for the rough tier of Lemma 14.15(c), (GS_j)(e3), Theorems 14.1b, 14.1c, Lemma 14.15(b).
Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nice -n 10 python3 ft_rough.py
"""
import heapq
import itertools
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl
from scipy.special import erf


# ---------------------------------------------------------------------------
# R1. First passage on a fine lattice below a coarse pattern.
def fine_first_passage(rough_coarse, L, c, Rcoarse):
    """0-1 Dijkstra in 2D embedding. A fine site below a rough coarse cell costs 0, otherwise 1.
    Returns the least number of regular fine cells on a nearest-neighbour path from fine site c
    to the outside of the sup-ball of radius Rcoarse*L around c."""
    R = Rcoarse * L

    def coarse(p):
        return (int(np.floor((p[0] + L // 2) / L)), int(np.floor((p[1] + L // 2) / L)))

    dist = {c: 0}
    pq = [(0, c)]
    while pq:
        d, p = heapq.heappop(pq)
        if d > dist.get(p, 10**9):
            continue
        if max(abs(p[0] - c[0]), abs(p[1] - c[1])) > R:
            return d
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (p[0] + dx, p[1] + dy)
            w = 0 if coarse(q) in rough_coarse else 1
            nd = d + w
            if nd < dist.get(q, 10**9):
                dist[q] = nd
                heapq.heappush(pq, (nd, q))
    return None


def coarse_D(rough_coarse, m):
    """Least number of regular coarse cells on a path from (0,0) to outside the sup-ball of radius m."""
    dist = {(0, 0): 0}
    pq = [(0, (0, 0))]
    while pq:
        d, p = heapq.heappop(pq)
        if d > dist[p]:
            continue
        if max(abs(p[0]), abs(p[1])) > m:
            return d
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (p[0] + dx, p[1] + dy)
            w = 0 if q in rough_coarse else 1
            nd = d + w
            if nd < dist.get(q, 10**9):
                dist[q] = nd
                heapq.heappush(pq, (nd, q))


print("R1. Children of rough coarse cells non-regular, the rest regular. Compare d_V with (L/2) r_k - C of line 840.")
print("   pattern       L    m   D(coarse)  d_V(fine)  (L/2)D  N'")
for L in [5, 9, 15]:
    for m in [6, 12]:
        stair = {(t, t) for t in range(0, m + 2)}
        checker = {(a, b) for a in range(-m - 2, m + 3) for b in range(-m - 2, m + 3) if (a + b) % 2 == 0}
        # thin regular shells of one coarse cell, rough between: pattern of concentric squares
        shells = {
            (a, b)
            for a in range(-m - 2, m + 3)
            for b in range(-m - 2, m + 3)
            if max(abs(a), abs(b)) % 2 == 0
        }
        for name, pat in (("diagonal", stair), ("checkerboard", checker), ("shells", shells)):
            D = coarse_D(pat, m)
            dv = fine_first_passage(pat, L, (0, 0), m)
            Np = sum(1 for p in pat if max(abs(p[0]), abs(p[1])) <= m)
            print(f"   {name:12s} {L:3d}  {m:3d}  {D:6d}     {dv:6d}    {L/2*D:7.1f}  {Np}")
print("   diagonal: d_V = D (a clipped regular cell costs one fine cell), so (L/2) r_k fails by the factor L/2.")
print("   shells: d_V = (L) D here because crossing is straight; a pierced column or lift tail removes it (see report).")


# ---------------------------------------------------------------------------
# R2. Output of the class on the diagonal staircase: LHS/RHS of (K3) from the explicit input of the report.
print("R2. Staircase: ratio of the output of h to the (K3) bound, from the explicit e_c of the report")
kappa = 1.6 / 8  # c_F = 1.6 per coarse cell, the rate seen in E2 of Text 13
for L, CN, p, cg in [(9, 2, 8, 0.1), (27, 2, 8, 0.1), (81, 3, 12, 0.1)]:
    m = 1
    while np.log(float(L)) * p + CN * np.log(L**4 * m) - kappa * m > 0:
        m += 1
    lhs = np.log(L**4) + np.log(cg) + p * np.log(L) - kappa * m + CN * np.log(L**4 * m)
    rhs = np.log(0.25) + p * np.log(L) - kappa * m + CN * np.log(2 + m)
    print(f"   L={L:3d} C={CN} p={p:2d}: smallest m with chi<1 is {m}, log(LHS/RHS) = {lhs-rhs:.2f}  (= log(4 c_g L^(4+4C) (m/(m+2))^C))")


# ---------------------------------------------------------------------------
# R3. (GS_j)(e3) in a free theory. Gaussian scalar on a 2D torus, block-average constraint (L=3). Mean shift is
# independent of x, covariance is 1/x, so TV of the one-site marginal = erf(sqrt(x) s / (2 sqrt(2) sigma_1)).
print("R3. (e3) in the free theory: TV between marginals at the block centre, W_1, W_2 agree on Q'_m")
L = 3
T = 27 * 3  # fine sites per side, 27 coarse
n = T * T


def idx(i, j):
    return (i % T) * T + (j % T)


rows, cols, vals = [], [], []
for i in range(T):
    for j in range(T):
        a = idx(i, j)
        for b in (idx(i + 1, j), idx(i, j + 1)):
            rows += [a, a, b, b]
            cols += [a, b, a, b]
            vals += [1.0, -1.0, -1.0, 1.0]
A = sp.csr_matrix((vals, (rows, cols)), shape=(n, n))
# constraint: block averages
Tc = T // L
Qr, Qc, Qv = [], [], []
for i in range(T):
    for j in range(T):
        Qr.append(((i // L) % Tc) * Tc + ((j // L) % Tc))
        Qc.append(idx(i, j))
        Qv.append(1.0 / L**2)
Q = sp.csr_matrix((Qv, (Qr, Qc)), shape=(Tc * Tc, n))
# zero mode fixed by the constraint at q=0
KKT = sp.bmat([[A, Q.T], [Q, None]], format="csc")
lu = spl.splu(KKT + 1e-12 * sp.eye(KKT.shape[0], format="csc"))


def lift(w):
    rhs = np.concatenate([np.zeros(n), w])
    return lu.solve(rhs)[:n]


# variance of the fibre at the centre site: solve with a unit source
site = idx(T // 2 // L * L + 1, T // 2 // L * L + 1)
src = np.zeros(n + Tc * Tc)
src[site] = 1.0
g = lu.solve(src)[:n]
var1 = g[site]
cx = (T // 2 // L)
ms = [1, 2, 3, 4, 5, 6, 8]
print("   m    shift(m)     Mahalanobis*sqrt(x)^-1   TV at x=4, 100, 10^4, 10^6              C e^{-c_F m} fit from x=4")
shift = {}
for m in ms:
    w1 = np.zeros(Tc * Tc)
    # W_2 differs from W_1 outside Q'_m by a unit-size coarse field on the shell m+1 (a dipole of flux, flux of order 1)
    w2 = np.zeros(Tc * Tc)
    for a in range(Tc):
        for b in range(Tc):
            da = min(abs(a - cx), Tc - abs(a - cx))
            db = min(abs(b - cx), Tc - abs(b - cx))
            if max(da, db) == m + 1:
                w2[a * Tc + b] = 1.0 if (a + b) % 2 == 0 else -1.0
    s = abs(lift(w2)[site] - lift(w1)[site])
    shift[m] = s
    d = s / np.sqrt(var1)
    tv = [erf(np.sqrt(x) * d / (2 * np.sqrt(2))) for x in (4.0, 100.0, 1e4, 1e6)]
    print(f"   {m:2d}  {s:.3e}    {d:.3e}             " + "  ".join(f"{t:.4f}" for t in tv))
rates = [np.log(shift[ms[i]] / shift[ms[i + 1]]) / (ms[i + 1] - ms[i]) for i in range(len(ms) - 1)]
print("   fitted decay rate per coarse cell:", ", ".join(f"{r:.2f}" for r in rates))
print("   So at fixed m TV -> 1 as x -> infinity: no C_n exp(-c_F d') with C_n free of x. (e3) must carry sqrt(x).")


# ---------------------------------------------------------------------------
# R4. The (G1') sup recursion of Prop. 14.8, line 710: bands f_0 = 2 > f_1 > ... > f_h <= eps_0.
print("R4. Recursion of line 710: u_{j+1}(f_i) <= A + L^4 u_j(f_{i+1}) + q u_j(2), with u(f_h) regular")
for L, h, q in [(9, 2, 1 / 8), (27, 2, 1 / 8), (27, 3, 1 / 8), (27, 2, 27.0 ** (-4 * 2) / 8)]:
    u = np.zeros(h + 1)
    A = 1.0
    hist = []
    for j in range(60):
        new = np.zeros(h + 1)
        for i in range(h):
            new[i] = A + L**4 * u[i + 1] + q * u[0]
        # regular parent: rare children have mean tiny against 1/8, take L^-12 q; if even this is q the growth is larger
        new[h] = A + q * L ** (-12.0) * u[0]
        u = new
        hist.append(u[0])
    growth = (hist[-1] / hist[-21]) ** (1 / 20)  # geometric mean, the modes come in +- pairs
    print(f"   L={L:3d} h={h} q={q:.3g}: U_60 = {hist[-1]:.3e}, mean growth per level {growth:.3f}  (L^2/sqrt(8) = {L**2/np.sqrt(8):.1f})")
print("   With q = 1/8 the top band grows geometrically in j. It closes only with q <= c L^(-4 h).")


# ---------------------------------------------------------------------------
# R5. Law of total cumulance, the partition sum in Theorem 14.1b, the one-step formula in Theorem 14.1c.
def partitions(s):
    s = list(s)
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for p in partitions(rest):
        yield [[first]] + p
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]


def cumulant(values, prob, idxs):
    """Joint cumulant of values[i] for i in idxs under prob."""
    total = 0.0
    for pi in partitions(idxs):
        m = len(pi)
        sign = (-1) ** (m - 1) * np.prod(range(1, m)) if m > 1 else 1.0
        term = 1.0
        for B in pi:
            term *= np.sum(prob * np.prod([values[i] for i in B], axis=0))
        total += sign * term
    return total


rng = np.random.default_rng(1)
N = 64
prob = rng.random(N)
prob /= prob.sum()
X = {i: rng.normal(size=N) for i in range(4)}
coarse = rng.integers(0, 8, N)
finer = coarse * 2 + rng.integers(0, 2, N)  # a refinement, so sigma(coarse) is inside sigma(finer)


def cond(values, labels, idxs):
    out = np.zeros(N)
    for lab in np.unique(labels):
        mask = labels == lab
        p = prob[mask] / prob[mask].sum()
        v = {i: values[i][mask] for i in idxs}
        out[mask] = cumulant(v, p, list(idxs))
    return out


for I in ([0, 1], [0, 1, 2], [0, 1, 2, 3]):
    lhs = cumulant(X, prob, I)
    rhs = 0.0
    for pi in partitions(I):
        Y = {b: cond(X, coarse, B) for b, B in enumerate(pi)}
        rhs += cumulant(Y, prob, list(range(len(pi))))
    print(f"R5. total cumulance |I|={len(I)}: lhs={lhs:+.12f} rhs={rhs:+.12f} diff={lhs-rhs:+.1e}")
# one-step conditional form
I = [0, 1, 2]
lhs = cond(X, coarse, I)
rhs = np.zeros(N)
for pi in partitions(I):
    Yf = {b: cond(X, finer, B) for b, B in enumerate(pi)}
    rhs += cond(Yf, coarse, list(range(len(pi))))
print(f"R5. one-step conditional formula of Theorem 14.1c: max diff = {np.abs(lhs-rhs).max():.1e}")
# C_m and the Hoelder bound at m = 2,3,4
for m in (2, 3, 4):
    Cm = sum(np.prod(range(1, len(p))) if len(p) > 1 else 1 for p in partitions(range(m)))
    print(f"    C_{m} = {int(Cm)}")


# ---------------------------------------------------------------------------
# R6. Schur step of Lemma 14.15(b): Lambda^2 R^4 under the hyperoctahedral group B_4 is absolutely irreducible.
group = []
for perm in itertools.permutations(range(4)):
    for signs in itertools.product((1, -1), repeat=4):
        M = np.zeros((4, 4))
        for i, pi in enumerate(perm):
            M[pi, i] = signs[i]
        group.append(M)
pairs = list(itertools.combinations(range(4), 2))


def wedge(M):
    W = np.zeros((6, 6))
    for a, (i, j) in enumerate(pairs):
        for b, (k, l) in enumerate(pairs):
            W[a, b] = M[i, k] * M[j, l] - M[i, l] * M[j, k]
    return W


chars = np.array([np.trace(wedge(M)) for M in group])
print(f"R6. |B_4| = {len(group)}, <chi,chi> on Lambda^2 R^4 = {np.mean(chars**2):.6f} (1 = absolutely irreducible)")
# orientation-preserving subgroup: reducible, so reflections are needed
det = np.array([np.linalg.det(M) for M in group])
print(f"    rotation subgroup: <chi,chi> = {np.mean(chars[det>0]**2):.6f} (2 means self-dual plus anti-self-dual; reflections are required)")


# ---------------------------------------------------------------------------
# R7. Proposition 14.7, direct enumeration.
p_, kappa_, d_ = 0.8, 0.4, 1.3
c_ = (p_**2 - (1 - p_) ** 2) / (p_**2 + (1 - p_) ** 2)
delta_ = -d_ / c_
alpha = {0: d_, 1: -d_}


def P_w(w, eta):
    return p_ if w == eta else 1 - p_


res = {}
for wp, wm in itertools.product((0, 1), repeat=2):
    num = den = 0.0
    numm = 0.0
    for eta in (0, 1):
        chi = 1 - 2 * eta
        wgt = 0.5 * P_w(wp, eta) * P_w(wm, eta)
        den += wgt
        num += wgt * (alpha[wp] + delta_ * chi)
        numm += wgt * (alpha[wm] + delta_ * chi)
    res[(wp, wm)] = (num / den, numm / den)
print("R7. Prop 14.7: y_+ at (0,0),(1,1),(0,1),(1,0):", [round(res[k][0], 10) for k in [(0, 0), (1, 1), (0, 1), (1, 0)]])
print("    y_+ + y_- identically zero:", max(abs(sum(res[k])) for k in res))
