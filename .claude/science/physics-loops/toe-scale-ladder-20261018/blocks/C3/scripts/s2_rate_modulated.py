"""C3 / s2: state-dependent (rate-modulated) covariant formation clocks.

Graphical construction: every site carries a Poisson process of rate LMAX with
iid marks (V,U) uniform; at a point (x,t,V,U) with x blank, x forms iff
V <= lam(eta_x(t-))/LMAX, with content Phi(eta_x(t-),U) ~ r(.|eta).  A point is
'sure' if V <= LMIN/LMAX; sigma_x = first sure point ~ Exp(LMIN); the
'relevant' points of x are those in [0, sigma_x].

Checks
 (a) exact (sympy): int_{t0>...>tn>0} prod_k LMAX e^{-LMIN t_k} dt = kappa^(n+1)/(n+1)!.
 (b) Monte Carlo: on a path of n+1 DISTINCT sites the expected number of
     decreasing chains of relevant points equals kappa^(n+1)/(n+1)! (Lemma C1
     holds with equality on a fixed path).
 (c) finite 4-cycle: exact final-record law of the Markov jump process
     (embedded-chain recursion) vs forward graphical-construction Monte Carlo
     (independent implementation), all 16 atoms within 4 SE.
 (d) Z^1 infinite volume: lazy backward exploration (the coding map of
     Theorem C) agrees with forward simulation on a ring whenever the explored
     reach stays inside the ring; reach tail below 2 kappa^(n+1)/(n+1)!.
 (e) observation only: Cov(xi_0, xi_r) for an eager copy rule, kappa = 5.
"""
import math, random, sys, os, itertools
from fractions import Fraction as Fr
import sympy as sp
sys.path.insert(0, os.path.dirname(__file__))
from c3_common import Checker

C = Checker("s2")

# ---------- (a) exact integral ----------
lam, mu = sp.symbols('lambda mu', positive=True)
for n in range(0, 5):
    ts = sp.symbols(f't0:{n+1}', positive=True)
    # integrate innermost t_n from 0..t_{n-1}, ..., t_0 from 0..oo
    expr = sp.Integer(1)
    for k in range(n + 1):
        expr *= lam * sp.exp(-mu * ts[k])
    for k in range(n, 0, -1):
        expr = sp.integrate(expr, (ts[k], 0, ts[k - 1]))
    expr = sp.simplify(sp.integrate(expr, (ts[0], 0, sp.oo)))
    target = (lam / mu) ** (n + 1) / sp.factorial(n + 1)
    C.check(f"(a) n={n}: ordered integral = kappa^(n+1)/(n+1)!", sp.simplify(expr - target) == 0, str(expr))

# ---------- helpers ----------
def relevant_points(rng, LMAX, LMIN):
    """Poisson(LMAX) points with marks (t,V,U) up to and including the first sure one."""
    pts = []
    t = 0.0
    while True:
        t += rng.expovariate(LMAX)
        V = rng.random(); U = rng.random()
        pts.append((t, V, U))
        if V <= LMIN / LMAX:
            return pts

# ---------- (b) chain counts on a path of distinct sites ----------
rng = random.Random(7)
LMAX, LMIN = 3.0, 1.0
kappa = LMAX / LMIN
NS = 60000
for n in range(0, 5):
    s = 0.0; s2 = 0.0
    for _ in range(NS):
        P = [sorted(p[0] for p in relevant_points(rng, LMAX, LMIN)) for _ in range(n + 1)]
        # number of chains t0 > t1 > ... > tn, t_k in P[k]; DP from the far end
        w = [1.0] * len(P[n])          # chains starting at a point of site n (length 0)
        for k in range(n - 1, -1, -1):
            nxt, nw = P[k + 1], w
            w = [sum(nw[j] for j, tt in enumerate(nxt) if tt < t) for t in P[k]]
        c = sum(w)
        s += c; s2 += c * c
    m = s / NS; se = math.sqrt(max(s2 / NS - m * m, 1e-12) / NS)
    target = kappa ** (n + 1) / math.factorial(n + 1)
    C.check(f"(b) n={n}: E#chains={m:.4f}+-{se:.4f} vs kappa^(n+1)/(n+1)!={target:.4f}", abs(m - target) <= 4 * se)

# ---------- model used in (c),(d) ----------
def lam_rate(eta):          # eta: list of formed neighbour contents (0/1)
    n1 = sum(1 for a in eta if a == 1); n0 = len(eta) - n1
    return 1.0 + 2.0 * n1 + 0.5 * n0
def r1(eta):               # P(content 1 | eta), Polya-like
    n1 = sum(1 for a in eta if a == 1); n0 = len(eta) - n1
    return (1.0 + n1) / (2.0 + n0 + n1)
LMIN_C, LMAX_C = 1.0, 5.0   # on a cycle each site has <= 2 neighbours: lam in [1,5]

# ---------- (c) exact 4-cycle law vs graphical MC ----------
N4 = 4
nbr = {x: [(x - 1) % N4, (x + 1) % N4] for x in range(N4)}
def lam_rate_F(eta):
    n1 = sum(1 for a in eta if a == 1); n0 = len(eta) - n1
    return Fr(1) + 2 * n1 + Fr(1, 2) * n0
def r1_F(eta):
    n1 = sum(1 for a in eta if a == 1); n0 = len(eta) - n1
    return Fr(1 + n1, 2 + n0 + n1)
from functools import lru_cache
@lru_cache(maxsize=None)
def exact_law(state):       # state: tuple of None/0/1 -> dict final config -> prob
    blanks = [x for x in range(N4) if state[x] is None]
    if not blanks:
        return {state: Fr(1)}
    rates = {x: lam_rate_F([state[y] for y in nbr[x] if state[y] is not None]) for x in blanks}
    tot = sum(rates.values())
    out = {}
    for x in blanks:
        eta = [state[y] for y in nbr[x] if state[y] is not None]
        p1 = r1_F(eta)
        for a, pa in ((1, p1), (0, 1 - p1)):
            if pa == 0: continue
            ns = list(state); ns[x] = a
            for k, v in exact_law(tuple(ns)).items():
                out[k] = out.get(k, 0) + rates[x] / tot * pa * v
    return out
law = exact_law(tuple([None] * N4))
C.check("(c) exact 4-cycle law normalised", sum(law.values()) == 1)

def forward_sim(data, sites, nbrf):
    """data[x] = relevant points; process all points in global time order."""
    ev = sorted((t, x, V, U) for x in sites for (t, V, U) in data[x])
    st = {x: None for x in sites}
    for t, x, V, U in ev:
        if st[x] is not None: continue
        eta = [st[y] for y in nbrf(x) if y in st and st[y] is not None]
        if V <= lam_rate(eta) / LMAX_C:
            st[x] = 1 if U <= r1(eta) else 0
    return st
rng = random.Random(11)
NS = 60000
cnt = {}
for _ in range(NS):
    data = {x: relevant_points(rng, LMAX_C, LMIN_C) for x in range(N4)}
    st = forward_sim(data, range(N4), lambda x: nbr[x])
    assert all(v is not None for v in st.values())   # every site forms by sigma_x
    key = tuple(st[x] for x in range(N4))
    cnt[key] = cnt.get(key, 0) + 1
worst = 0.0
okall = True
for key, p in law.items():
    ph = cnt.get(key, 0) / NS
    se = math.sqrt(max(float(p) * (1 - float(p)), 1e-9) / NS)
    z = abs(ph - float(p)) / se
    worst = max(worst, z)
    okall &= z <= 4
C.check(f"(c) graphical MC matches exact jump-chain law on all {len(law)} atoms (max |z|={worst:.2f} <= 4)", okall)

# ---------- (d) backward exploration on Z^1 ----------
class LazyZ:
    def __init__(self, rng, LMAX, LMIN):
        self.rng, self.LMAX, self.LMIN = rng, LMAX, LMIN
        self.data = {}
    def pts(self, x):
        if x not in self.data:
            self.data[x] = relevant_points(self.rng, self.LMAX, self.LMIN)
        return self.data[x]

def backward_record(Z, x0, lamf, rf, LMAX):
    memo = {}
    reached = set()
    sys.setrecursionlimit(100000)
    def state(y, t):
        """content of y at time t- (None if blank)."""
        for (s, V, U) in Z.pts(y):
            if s >= t:
                return None
            reached.add(y)
            key = (y, s)
            if key not in memo:
                eta = [state(z, s) for z in (y - 1, y + 1)]
                eta = [a for a in eta if a is not None]
                if V <= lamf(eta) / LMAX:
                    memo[key] = 1 if U <= rf(eta) else 0
                else:
                    memo[key] = None
            if memo[key] is not None:
                return memo[key]
        raise RuntimeError("unreachable: last relevant point is sure")
    v = state(x0, float('inf'))
    return v, reached

rng = random.Random(23)
NR, HALF = 400, 60
agree = True; inside = 0; reach_hist = []
for trial in range(NR):
    Z = LazyZ(rng, LMAX_C, LMIN_C)
    v, reached = backward_record(Z, 0, lam_rate, r1, LMAX_C)
    R = max(abs(y) for y in reached)
    reach_hist.append(R)
    if R + 1 < HALF:
        inside += 1
        sites = list(range(-HALF, HALF))
        for x in sites: Z.pts(x)
        ring = lambda x: [((x + 1 + HALF) % (2 * HALF)) - HALF, ((x - 1 + HALF) % (2 * HALF)) - HALF]
        st = forward_sim(Z.data, sites, ring)
        agree &= (st[0] == v)
C.check(f"(d) backward coding map == forward ring simulation at the origin ({inside}/{NR} trials with reach inside ring)", agree and inside == NR)
NB = 4000
rng = random.Random(29)
for trial in range(NB):
    Z = LazyZ(rng, LMAX_C, LMIN_C)
    _, reached = backward_record(Z, 0, lam_rate, r1, LMAX_C)
    reach_hist.append(max(abs(y) for y in reached))
kap = LMAX_C / LMIN_C
tot = len(reach_hist)
ok = True; rows = []
for n in range(1, 16):
    p = sum(1 for R in reach_hist if R >= n) / tot
    se = math.sqrt(max(p * (1 - p), 1 / tot) / tot)
    b = 2 * kap ** (n + 1) / math.factorial(n + 1)
    rows.append(f"n={n}: P(reach>=n)={p:.4f} bound={min(1,b):.3e}")
    ok &= p <= min(1.0, b) + 4 * se
print("  (d) reach tail, kappa=5, Z^1:\n   " + "\n   ".join(rows))
C.check("(d) reach tail below Lemma C1 bound 2 kappa^(n+1)/(n+1)! (+4SE) for n=1..15", ok)

# ---------- (e) observation: covariance decay with eager copy rule ----------
K = 5.0
lam_e = lambda eta: K if eta else 1.0
def r_e(eta):
    if not eta: return 0.5
    return sum(eta) / len(eta)     # copy a uniformly chosen formed neighbour's content
rng = random.Random(31)
NSE, RMAX = 6000, 10
acc = [[0.0, 0.0, 0.0] for _ in range(RMAX + 1)]
m0 = 0.0
for _ in range(NSE):
    Z = LazyZ(rng, K, 1.0)
    xs = [backward_record(Z, r, lam_e, r_e, K)[0] for r in range(RMAX + 1)]
    m0 += xs[0]
    for r in range(RMAX + 1):
        acc[r][0] += xs[0] * xs[r]; acc[r][1] += xs[r]
rows = []
for r in range(RMAX + 1):
    cov = acc[r][0] / NSE - (m0 / NSE) * (acc[r][1] / NSE)
    rows.append(f"r={r}: Cov={cov:+.4f}")
print("  (e) observation (not a check), eager copy rule kappa=5, MC SE ~ 0.006:\n   " + "\n   ".join(rows))

C.finish()
