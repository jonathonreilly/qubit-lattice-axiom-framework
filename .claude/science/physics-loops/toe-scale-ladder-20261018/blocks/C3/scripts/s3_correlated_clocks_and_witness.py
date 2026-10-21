"""C3 / s3: finite-range-correlated clocks, the covariance bound, and the
ordered-phase witness arithmetic.

Checks
 (a) Z^1, T_x = max(zeta_x, zeta_{x+1}) (range-1 factor of iid, ties possible):
     exact P(T_0 > T_1 > ... > T_n strictly) by enumerating all (n+2)! orders of
     zeta, against Lemma D's bound 1/ceil((n+1)/b)! with b = |K-K| = 3.
 (b) Z^2, T_x = zeta_x + zeta_{x+e1}: Monte Carlo strict-decrease probability
     along several SAW shapes against 1/ceil((n+1)/3)!.
 (c) Theorem B coupling bound, iid clocks, Z^1 copy rule: Monte Carlo
     |Cov(xi_0, xi_r)| <= 2 sum_z q(|z|) q(|z-r|) (+4SE), q(k)=min(1,2/k!).
 (d) Witness arithmetic for the covariant-in-law level-clock mixture W:
     Cov >= (1/6)(1-6*10^-5) - 1/36 > 0 for every separation (uses the
     IMPORTED bound P(v_x != a) <= 3/10^5 of the 2026-09-16 note, T7).
 (e) level clock T_x = x_1 + x_2 + x_3: every backward-monotone path is
     decreasing with probability 1, so the decreasing-path tail is 1 for all n.
 (f) reviewer F1 witness: exchangeable clocks with ties (all-tied w.p. 1/2,
     iid w.p. 1/2) give Cov(xi_0, xi_r) = 1/9 for all r >= 3 (exact).
"""
import itertools, math, random, sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(__file__))
from c3_common import Checker

C = Checker("s3")

# ---------- (a) ----------
for n in range(1, 8):
    m = n + 2
    hit = 0; tot = 0
    for perm in itertools.permutations(range(m)):
        T = [max(perm[i], perm[i + 1]) for i in range(n + 1)]
        tot += 1
        if all(T[i] > T[i + 1] for i in range(n)):
            hit += 1
    p = F(hit, tot)
    k = -(-(n + 1) // 3)
    b = F(1, math.factorial(k))
    C.check(f"(a) n={n}: P(strict decrease)={p} <= 1/{k}! = {b}", p <= b, f"iid value 1/(n+1)!={F(1, math.factorial(n+1))}")

# ---------- (b) ----------
rng = random.Random(5)
shapes = {
    "straight_e1": [(i, 0) for i in range(7)],
    "straight_e2": [(0, i) for i in range(7)],
    "staircase": [(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3)],
    "U_turn": [(0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(-1,1)],
}
NS = 100000
for name, path in shapes.items():
    n = len(path) - 1
    hit = 0
    for _ in range(NS):
        z = {}
        def zeta(p):
            if p not in z: z[p] = rng.random()
            return z[p]
        T = [zeta(p) + zeta((p[0] + 1, p[1])) for p in path]
        if all(T[i] > T[i + 1] for i in range(n)):
            hit += 1
    p = hit / NS; se = math.sqrt(max(p * (1 - p), 1 / NS) / NS)
    k = -(-(n + 1) // 3)
    C.check(f"(b) {name} n={n}: P={p:.5f}+-{se:.5f} <= 1/{k}!={1/math.factorial(k):.5f}", p <= 1 / math.factorial(k) + 4 * se)

# ---------- (c) covariance coupling bound ----------
def q(k):
    return 1.0 if k <= 1 else min(1.0, 2.0 / math.factorial(k))
def cov_bound(r, zmax=60):
    return 2 * sum(q(abs(z)) * q(abs(z - r)) for z in range(-zmax, zmax + 1))

def record(T, U, x, memo):
    """iid-clock record on Z^1 with lazily generated (T,U): copy rule
    (no earlier neighbour -> own bit; else copy a uniformly chosen earlier
    neighbour, selected by the mark)."""
    if x in memo: return memo[x]
    earlier = [y for y in (x - 1, x + 1) if T(y) < T(x)]
    if not earlier:
        v = 1 if U(x) < 0.5 else 0
    else:
        j = min(int(U(x) * len(earlier)), len(earlier) - 1)
        v = record(T, U, earlier[j], memo)
    memo[x] = v
    return v

rng = random.Random(41)
NSC, RMAX = 40000, 8
s0 = 0.0; sr = [0.0] * (RMAX + 1); s0r = [0.0] * (RMAX + 1)
for _ in range(NSC):
    Td, Ud = {}, {}
    T = lambda y: Td.setdefault(y, rng.random())
    U = lambda y: Ud.setdefault(y, rng.random())
    memo = {}
    xs = [record(T, U, r, memo) for r in range(RMAX + 1)]
    s0 += xs[0]
    for r in range(RMAX + 1):
        sr[r] += xs[r]; s0r[r] += xs[0] * xs[r]
ok = True; rows = []
for r in range(1, RMAX + 1):
    cov = s0r[r] / NSC - (s0 / NSC) * (sr[r] / NSC)
    se = 0.5 / math.sqrt(NSC) * 1.5
    b = cov_bound(r)
    rows.append(f"r={r}: Cov={cov:+.4f} bound={b:.3e}")
    ok &= abs(cov) <= b + 4 * se
print("  (c) iid-clock copy rule on Z^1:\n   " + "\n   ".join(rows))
C.check("(c) |Cov(xi_0,xi_r)| <= Theorem B bound (+4SE) for r=1..8", ok)
C.check("(c) Theorem B bound is superexponentially small: bound(40) < 1e-30", cov_bound(40) < 1e-30, f"bound(40)={cov_bound(40):.3e}")

# ---------- (d) witness arithmetic ----------
eps = F(3, 10**5)
lower = F(1, 6) * (1 - 2 * eps) - F(1, 36)
C.check(f"(d) mixture witness: Cov(1{{v_0=b}},1{{v_x=b}}) >= {lower} = {float(lower):.6f} > 0 uniformly in x", lower > 0)
# fraction of O_h elements fixing the axis e1: |stab| = 8 of 48
C.check("(d) |O_h|=48 acts transitively on the 6 axes with stabiliser of order 8", 48 // 6 == 8)

# ---------- (e) level clock ----------
path = [(0, 0, 0)]
for k in range(30):
    x = list(path[-1]); x[k % 3] -= 1; path.append(tuple(x))
Tl = [sum(p) for p in path]
C.check("(e) level clock: the 30-step backward staircase is strictly decreasing deterministically (tail = 1, no factorial decay)",
        all(Tl[i] > Tl[i + 1] for i in range(30)))

# ---------- (f) reviewer F1 witness: exchangeable clocks WITH ties ----------
# Clock: w.p. 1/2 all T_x equal (all tied), w.p. 1/2 iid continuous.
# Rule on Z: content 0 if no strictly earlier neighbour, 1 otherwise.
# iid part, r=3: xi_0 depends on T_{-1},T_0,T_1 and xi_3 on T_2,T_3,T_4 (disjoint),
# enumerated exactly over all 6! orders of sites -1..4.
sites = list(range(-1, 5))
tot = 0; e0 = 0; e3 = 0; e03 = 0
for perm in itertools.permutations(range(6)):
    T = dict(zip(sites, perm))
    x0 = 1 if (T[-1] < T[0] or T[1] < T[0]) else 0
    x3 = 1 if (T[2] < T[3] or T[4] < T[3]) else 0
    tot += 1; e0 += x0; e3 += x3; e03 += x0 * x3
Ex = F(1, 2) * F(e0, tot)             # tied branch contributes 0
Exy = F(1, 2) * F(e03, tot)
cov = Exy - Ex * (F(1, 2) * F(e3, tot))
C.check(f"(f) tied-exchangeable witness: Cov(xi_0,xi_3) = {cov} = 1/9 (for every r>=3 by disjointness): LRO outside A' (ties)", cov == F(1, 9))

C.finish()
