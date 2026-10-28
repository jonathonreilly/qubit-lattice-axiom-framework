"""c21: exact checks for the cluster-expansion theorem (criteria: checks/c21_criteria.md, written before this script).

Part G: Penrose partition, rho^T = (-1)^{n-1} #Penrose trees, tree-graph bound (323), rho^T(K_n).
Part M: Mayer grouping (Dimock I (300)-(301)) and integration (308) by direct polymer enumeration.
Part S: polymer-gas exponentiation (311)-(312), truncated series vs exact Moebius-inverted log.
Part I: Ising instance for the kappa-dependence of c_0.
"""
import itertools
import math
import random
import resource
import time

import numpy as np

T0 = time.time()
OK = {}


def report(name, cond, info=""):
    OK[name] = bool(cond)
    print(f"{name}: {'PASS' if cond else 'FAIL'} {info}")


# ---------------------------------------------------------------- Part G: graphs
def connected(n, edges):
    if n == 1:
        return True
    adj = {i: [] for i in range(n)}
    for (a, b) in edges:
        adj[a].append(b); adj[b].append(a)
    seen = {0}; st = [0]
    while st:
        v = st.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); st.append(w)
    return len(seen) == n


def bfs_depth(n, edges):
    adj = {i: [] for i in range(n)}
    for (a, b) in edges:
        adj[a].append(b); adj[b].append(a)
    d = {0: 0}; frontier = [0]
    while frontier:
        nxt = []
        for v in frontier:
            for w in adj[v]:
                if w not in d:
                    d[w] = d[v] + 1; nxt.append(w)
        frontier = nxt
    return d, adj


def tree_of(n, G):
    """Penrose map G -> T(G): parent(j) = smallest-label neighbour at depth d(j)-1."""
    d, adj = bfs_depth(n, G)
    T = set()
    for j in range(1, n):
        p = min(i for i in adj[j] if d[i] == d[j] - 1)
        T.add((min(p, j), max(p, j)))
    return frozenset(T)


def admissible(n, g, T):
    d, adj = bfs_depth(n, T)
    par = {}
    for j in range(1, n):
        par[j] = [i for i in adj[j] if d[i] == d[j] - 1][0]
    R = []
    for (i, j) in g:
        if (i, j) in T:
            continue
        if d[i] == d[j]:
            R.append((i, j))
        elif d[j] == d[i] + 1 and i > par[j]:
            R.append((i, j))
        elif d[i] == d[j] + 1 and j > par[i]:
            R.append((i, j))
    return R


def graph_data(n, g):
    g = list(g)
    rho = 0; trees = []
    for mask in range(1 << len(g)):
        G = [g[i] for i in range(len(g)) if mask >> i & 1]
        if connected(n, G):
            rho += (-1) ** len(G)
            if len(G) == n - 1:
                trees.append(frozenset(G))
    return rho, trees


def check_graph(n, g, partition=False):
    rho, trees = graph_data(n, g)
    pen = sum(1 for T in trees if not admissible(n, g, T))
    ok1 = rho == (-1) ** (n - 1) * pen
    ok2 = abs(rho) <= len(trees)
    ok4 = True
    if partition:
        gl = list(g)
        for mask in range(1 << len(gl)):
            G = frozenset(gl[i] for i in range(len(gl)) if mask >> i & 1)
            if not connected(n, G):
                continue
            T = tree_of(n, G)
            R = set(admissible(n, g, T))
            if not (T <= G and G <= (T | R)):
                ok4 = False
        for T in trees:
            R = admissible(n, g, T)
            for k in range(len(R) + 1):
                for S in itertools.combinations(R, k):
                    if tree_of(n, T | frozenset(S)) != T:
                        ok4 = False
    return rho, len(trees), ok1, ok2, ok4


g1 = g2 = g4 = True
count = 0
for n in range(2, 6):
    pairs = list(itertools.combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        g = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        if not connected(n, g):
            continue
        _, _, a, b, c = check_graph(n, g, partition=True)
        g1 &= a; g2 &= b; g4 &= c; count += 1
rng = random.Random(20261027)
pairs6 = list(itertools.combinations(range(6), 2))
samples = [pairs6]
while len(samples) < 301:
    g = [e for e in pairs6 if rng.random() < 0.5]
    if connected(6, g):
        samples.append(g)
for g in samples:
    _, _, a, b, _ = check_graph(6, g)
    g1 &= a; g2 &= b
print(f"Part G: {count} connected labelled graphs with n <= 5 (with partition test), 301 graphs with n = 6")
report("G1 rho^T = (-1)^(n-1) #Penrose", g1)
report("G2 |rho^T| <= #spanning trees (323)", g2)
g3 = True; vals = []
for n in range(2, 7):
    rho, nt, _, _, _ = check_graph(n, list(itertools.combinations(range(n), 2)))
    vals.append((n, rho, nt)); g3 &= rho == (-1) ** (n - 1) * math.factorial(n - 1)
report("G3 rho^T(K_n) = (-1)^(n-1)(n-1)!", g3, str(vals))
report("G4 Penrose partition (n <= 5)", g4)
RHO_TABLE = {}


def rhoT(nv, edges):
    key = (nv, frozenset(edges))
    if key not in RHO_TABLE:
        if not connected(nv, edges):
            RHO_TABLE[key] = 0
        else:
            RHO_TABLE[key] = graph_data(nv, edges)[0]
    return RHO_TABLE[key]


# ---------------------------------------------------------------- lattice: 2 x 3 grid
R_, C_ = 2, 3
SITES = [(r, c) for r in range(R_) for c in range(C_)]
NS = len(SITES)
IDX = {s: i for i, s in enumerate(SITES)}
NN = [(IDX[(r, c)], IDX[(r, c + 1)]) for r in range(R_) for c in range(C_ - 1)] + \
     [(IDX[(0, c)], IDX[(1, c)]) for c in range(C_)]
SQUARES = [(IDX[(0, c)], IDX[(0, c + 1)], IDX[(1, c + 1)], IDX[(1, c)]) for c in range(C_ - 1)]
FULL = (1 << NS) - 1


def bits(m):
    return [i for i in range(NS) if m >> i & 1]


def face_connected(m):
    if m == 0:
        return False
    s = bits(m); seen = {s[0]}; st = [s[0]]
    adj = {i: set() for i in range(NS)}
    for a, b in NN:
        adj[a].add(b); adj[b].add(a)
    while st:
        v = st.pop()
        for w in adj[v]:
            if (m >> w & 1) and w not in seen:
                seen.add(w); st.append(w)
    return len(seen) == len(s)


CONN = [m for m in range(1, FULL + 1) if face_connected(m)]

# ---------------------------------------------------------------- Part M
VALS = np.array([-1.0, 0.0, 1.0]); PROB = np.array([0.3, 0.3, 0.4])
CONF = np.array(list(itertools.product(range(3), repeat=NS)))
PHI = VALS[CONF]                      # (729, 6)
W = np.prod(PROB[CONF], axis=1)       # weights
POLY = []                              # (mask, H array over configs)
for i in range(NS):
    POLY.append((1 << i, 0.03 * PHI[:, i] + 0.02 * PHI[:, i] ** 2))
for a, b in NN:
    POLY.append(((1 << a) | (1 << b), 0.03 * PHI[:, a] * PHI[:, b] + 0.02 * PHI[:, a] ** 2 * PHI[:, b]))
for sq in SQUARES:
    m = sum(1 << i for i in sq)
    POLY.append((m, 0.03 * PHI[:, sq[0]] * PHI[:, sq[1]] * PHI[:, sq[2]] * PHI[:, sq[3]] + 0.01 * PHI[:, sq[0]] ** 2))
NP = len(POLY)
F = [np.expm1(h) for (_, h) in POLY]
PM = [m for (m, _) in POLY]

K = {}
for coll in range(1, 1 << NP):
    members = [i for i in range(NP) if coll >> i & 1]
    # overlap-connectivity of the collection
    seen = {members[0]}; st = [members[0]]
    while st:
        v = st.pop()
        for w in members:
            if w not in seen and (PM[v] & PM[w]):
                seen.add(w); st.append(w)
    if len(seen) != len(members):
        continue
    Y = 0; prod = np.ones(len(W))
    for i in members:
        Y |= PM[i]; prod = prod * F[i]
    K[Y] = K.get(Y, 0) + prod


def disjoint_sum(S, act, memo):
    """Sum over families of pairwise disjoint Y (keys of act) inside S of the product of act[Y]."""
    if S == 0:
        return 1.0
    if S in memo:
        return memo[S]
    s0 = S & -S
    tot = disjoint_sum(S & ~s0, act, memo)
    for Y, v in act.items():
        if (Y & s0) and (Y & ~S) == 0:
            tot = tot + v * disjoint_sum(S & ~Y, act, memo)
    memo[S] = tot
    return tot


m1 = 0.0
memo = {}
for Z in range(FULL + 1):
    lhs = np.ones(len(W))
    for (m, _), f in zip(POLY, F):
        if (m & ~Z) == 0:
            lhs = lhs * (1 + f)
    rhs = disjoint_sum(Z, K, memo)
    m1 = max(m1, float(np.max(np.abs(lhs - rhs) / np.abs(lhs))))
report("M1 Mayer grouping identity, all Z and phi", m1 <= 1e-12, f"max rel err {m1:.2e}")
report("M2 K(Y) supported on connected Y", all(face_connected(Y) for Y in K), f"{len(K)} sets Y with K != 0")
KS = {Y: float(np.dot(W, v)) for Y, v in K.items()}
XI = {}
for Z in range(FULL + 1):
    ex = np.zeros(len(W))
    for (m, h) in POLY:
        if (m & ~Z) == 0:
            ex = ex + h
    XI[Z] = float(np.dot(W, np.exp(ex)))
m3 = 0.0; memo2 = {}
for Z in range(FULL + 1):
    rhs = disjoint_sum(Z, KS, memo2)
    m3 = max(m3, abs(XI[Z] - rhs) / abs(XI[Z]))
report("M3 integration step (308)", m3 <= 1e-12, f"max rel err {m3:.2e}")

# ---------------------------------------------------------------- Part S
def moebius(logxi, Y):
    tot = 0.0
    sub = Y
    while True:
        tot += (-1) ** (bin(Y).count("1") - bin(sub).count("1")) * logxi[sub]
        if sub == 0:
            break
        sub = (sub - 1) & Y
    return tot


LOGXI = {Z: math.log(v) for Z, v in XI.items()}
HM = {Y: moebius(LOGXI, Y) for Y in range(1, FULL + 1)}
s1 = max(abs(HM[Y]) for Y in HM if not face_connected(Y))
report("S1 H#_Moeb vanishes off connected Y", s1 <= 1e-13, f"max {s1:.2e}")
ACT = [(Y, KS.get(Y, 0.0)) for Y in CONN]
ACT = [(Y, v) for (Y, v) in ACT if v != 0.0]
series = {N: {Y: 0.0 for Y in CONN} for N in range(1, 5)}
contrib = {n: {} for n in range(1, 5)}
for n in range(1, 5):
    for tup in itertools.product(range(len(ACT)), repeat=n):
        Ys = [ACT[i][0] for i in tup]
        U = 0
        for y in Ys:
            U |= y
        edges = [(a, b) for a in range(n) for b in range(a + 1, n) if Ys[a] & Ys[b]]
        r = rhoT(n, edges)
        if r == 0:
            continue
        val = r * math.prod(ACT[i][1] for i in tup) / math.factorial(n)
        contrib[n][U] = contrib[n].get(U, 0.0) + val
for N in range(1, 5):
    for Y in CONN:
        series[N][Y] = sum(contrib[n].get(Y, 0.0) for n in range(1, N + 1))
errs = [max(abs(series[N][Y] - HM[Y]) for Y in CONN) for N in range(1, 5)]
maxH = max(abs(HM[Y]) for Y in CONN)
report("S2 err_{N+1} <= 0.5 err_N", all(errs[i + 1] <= 0.5 * errs[i] for i in range(3)),
       "errs " + " ".join(f"{e:.2e}" for e in errs) + f" (max|H#| {maxH:.2e}; {len(ACT)} activities)")
report("S3 err_4 <= 1e-6", errs[3] <= 1e-6)
tot4 = sum(series[4].values())
print(f"  sum_Y H#_<=4(Y) = {tot4:.12e}, log Xi(grid) = {LOGXI[FULL]:.12e}")

# ---------------------------------------------------------------- Part I
def ising_H(h, Y):
    s = bits(Y)
    logxi = {}
    sub = Y
    while True:
        ss = bits(sub)
        bonds = [(a, b) for (a, b) in NN if (sub >> a & 1) and (sub >> b & 1)]
        tot = 0.0
        for sig in itertools.product((-1, 1), repeat=len(ss)):
            sv = dict(zip(ss, sig))
            tot += math.exp(h * sum(sv[a] * sv[b] for a, b in bonds))
        logxi[sub] = math.log(tot / 2 ** len(ss)) if ss else 0.0
        if sub == 0:
            break
        sub = (sub - 1) & Y
    return moebius(logxi, Y)


Y6 = FULL
Y4 = sum(1 << i for i in SQUARES[0])
Ydis = (1 << IDX[(0, 0)]) | (1 << IDX[(1, 2)])

# [S11 reporting fix, criteria addendum]: the ratios are computed in 60-digit arithmetic; the double-precision value
# enters only through a bound check (its 4th digit is cancellation noise, REVIEW_S9_S10 fix 1).
import mpmath
mpmath.mp.dps = 60


def ising_H_mp(h, Y, bonds_on=None):
    hm = mpmath.mpf(h)
    logxi = {}
    sub = Y
    while True:
        ss = bits(sub)
        bonds = [(a, b) for (a, b) in (NN if bonds_on is None else bonds_on) if (sub >> a & 1) and (sub >> b & 1)]
        tot = mpmath.mpf(0)
        for sig in itertools.product((-1, 1), repeat=len(ss)):
            sv = dict(zip(ss, sig))
            tot += mpmath.exp(hm * sum(sv[a] * sv[b] for a, b in bonds))
        logxi[sub] = mpmath.log(tot / 2 ** len(ss)) if ss else mpmath.mpf(0)
        if sub == 0:
            break
        sub = (sub - 1) & Y
    return moebius(logxi, Y)


i1 = i2 = True; i3 = 0.0; rows = []; dmax = 0.0
for h in (0.01, 0.03, 0.1):
    r6 = abs(ising_H_mp(h, Y6)) / mpmath.mpf(h) ** 6
    r4 = abs(ising_H_mp(h, Y4)) / mpmath.mpf(h) ** 4
    d6 = abs(abs(ising_H(h, Y6)) / h ** 6 - float(r6))
    d4 = abs(abs(ising_H(h, Y4)) / h ** 4 - float(r4))
    dmax = max(dmax, d6, d4)
    rows.append((h, float(r6), float(r4)))
    i1 &= 0.9 <= r6 <= 1.1; i2 &= 0.9 <= r4 <= 1.1
    i3 = max(i3, abs(ising_H(h, Ydis)))
report("I1 |H#(Y6)|/h^6 in [0.9,1.1]", i1, " ".join(f"h={h}: {r6:.4f}" for h, r6, _ in rows) + " (60-digit)")
report("I2 |H#(Y4)|/h^4 in [0.9,1.1]", i2, " ".join(f"h={h}: {r4:.4f}" for h, _, r4 in rows) + " (60-digit)")
print(f"  double-precision ratios agree with the 60-digit ones to within 1e-3: {dmax <= 1e-3}")
report("I3 disconnected Y gives 0", i3 <= 1e-15, f"max {i3:.1e}")

# I4: the six-bond finite difference (only the six outer bonds of Y6 switched on/off)
by_rc = {v: k for k, v in IDX.items()}
OUTER = [b for b in NN if not ({by_rc[b[0]][1], by_rc[b[1]][1]} == {1} and by_rc[b[0]][0] != by_rc[b[1]][0])]
assert len(OUTER) == 6, OUTER
i4 = True; rel = []
for h in (0.01, 0.03, 0.1):
    Dmp = mpmath.mpf(0); Dd = 0.0
    for S in itertools.product((0, 1), repeat=6):
        on = [b for b, s_ in zip(OUTER, S) if s_]
        sg = (-1) ** (6 - sum(S))
        tot = mpmath.mpf(0); totd = 0.0
        for sig in itertools.product((-1, 1), repeat=NS):
            e = sum(sig[a] * sig[b] for a, b in on)
            tot += mpmath.exp(mpmath.mpf(h) * e); totd += math.exp(h * e)
        Dmp += sg * mpmath.log(tot / 2 ** NS); Dd += sg * math.log(totd / 2 ** NS)
    exact = mpmath.log(1 + mpmath.tanh(mpmath.mpf(h)) ** 6)
    i4 &= abs(Dmp - exact) <= mpmath.mpf(10) ** -40
    rel.append(abs(Dd - float(Dmp)) / float(Dmp))
report("I4 six-bond difference = log(1+tanh(h)^6)", i4,
       f"(60-digit, h = 0.01, 0.03, 0.1); double-precision relative error <= 0.05: {max(rel) <= 0.05}")

peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print(f"c21: {sum(OK.values())}/{len(OK)} PASS; {'PASS' if all(OK.values()) else 'FAIL'}; "
      f"time {time.time() - T0:.1f} s, peak RSS {peak:.0f} MB")
