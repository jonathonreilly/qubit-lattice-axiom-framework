"""C3 / s1: iid-clock decreasing paths and coding radius (exact + Monte Carlo).

Checks
 (a) Z^1: exact P(L>=n) by enumerating all (2n+1)! orders of the window [-n,n]
     against the closed form 2/(n+1)! - 1/((2n+1)(n!)^2), and against the
     union bound D(D-1)^(n-1)/(n+1)! (D=2).
 (b) Z^2, Z^3: exact self-avoiding-walk counts c_n, c_n <= D(D-1)^(n-1), and the
     exact expected number of decreasing SAWs c_n/(n+1)! (an exact identity for
     iid continuous clocks: each SAW of n edges is decreasing w.p. 1/(n+1)!).
 (c) Z^2, Z^3: Monte Carlo P(L>=n) (n=1..5) below the union bound; exact
     P(L>=1) = 1 - 1/(D+1).
 (d) Coding radius off-by-one: for the XOR copy rule on Z^1 (menu {0,1};
     no earlier neighbour -> own mark bit; else XOR of earlier neighbours'
     records), exact lower bounds on P(R>=2), P(R>=3) by exhaustive
     enumeration of window extensions, compared with the map's proposed
     P(R>=n) <= 2d(2d-1)^(n-1)/(n+1)! and with the corrected
     P(R>=n+1) <= P(L>=n).
L(x) := length of the longest strictly-decreasing-time self-avoiding path from x.
R(x) := smallest m such that the iid data on the ball B(x,m) determines xi_x.
"""
import itertools, math, random, sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(__file__))
from c3_common import Checker

C = Checker("s1")

# ---------- (a) Z^1 exact ----------
def L_ge_n_1d_exact(n):
    sites = list(range(-n, n + 1))
    idx = {s: i for i, s in enumerate(sites)}
    cnt = 0
    tot = 0
    for perm in itertools.permutations(range(2 * n + 1)):
        T = perm
        tot += 1
        right = all(T[idx[k]] > T[idx[k + 1]] for k in range(0, n))
        left = all(T[idx[-k]] > T[idx[-k - 1]] for k in range(0, n))
        if right or left:
            cnt += 1
    return F(cnt, tot)

for n in range(1, 5):
    ex = L_ge_n_1d_exact(n)
    closed = F(2, math.factorial(n + 1)) - F(1, (2 * n + 1) * math.factorial(n) ** 2)
    bound = F(2 * 1 ** (n - 1), math.factorial(n + 1))
    C.check(f"Z1 n={n}: enumerated P(L>=n)={ex} equals closed form", ex == closed, f"closed={closed}")
    C.check(f"Z1 n={n}: P(L>=n) <= 2/(n+1)! = {bound}", ex <= bound)

# ---------- (b) SAW counts ----------
def saw_counts(d, nmax):
    dirs = []
    for i in range(d):
        e = [0] * d; e[i] = 1; dirs.append(tuple(e))
        e = [0] * d; e[i] = -1; dirs.append(tuple(e))
    counts = [0] * (nmax + 1)
    origin = tuple([0] * d)
    visited = {origin}
    def rec(pos, k):
        counts[k] += 1
        if k == nmax:
            return
        for e in dirs:
            q = tuple(p + de for p, de in zip(pos, e))
            if q not in visited:
                visited.add(q); rec(q, k + 1); visited.remove(q)
    rec(origin, 0)
    return counts

known = {2: [1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100],
         3: [1, 6, 30, 150, 726, 3534, 16926, 81390]}
for d, nmax in ((2, 10), (3, 7)):
    D = 2 * d
    c = saw_counts(d, nmax)
    C.check(f"Z{d}: SAW counts c_0..c_{nmax} match OEIS (A001411/A001412)", c == known[d], str(c))
    ok = all(c[n] <= D * (D - 1) ** (n - 1) for n in range(1, nmax + 1))
    C.check(f"Z{d}: c_n <= D(D-1)^(n-1) for n<=nmax", ok)
    rows = []
    for n in range(1, nmax + 1):
        rows.append(f"n={n}: E#dec={float(F(c[n], math.factorial(n+1))):.3e} bound={float(F(D*(D-1)**(n-1), math.factorial(n+1))):.3e}")
    print(f"  Z{d} exact expected decreasing SAW counts c_n/(n+1)!:\n   " + "\n   ".join(rows))

# ---------- (c) Monte Carlo P(L>=n) in Z^2, Z^3 ----------
def has_dec_path(T, d, n):
    D = 2 * d
    dirs = []
    for i in range(d):
        e = [0] * d; e[i] = 1; dirs.append(tuple(e))
        e = [0] * d; e[i] = -1; dirs.append(tuple(e))
    origin = tuple([0] * d)
    def get(p):
        if p not in T:
            T[p] = random.random()
        return T[p]
    def rec(pos, k):
        if k == n:
            return True
        tp = get(pos)
        for e in dirs:
            q = tuple(a + b for a, b in zip(pos, e))
            if get(q) < tp and rec(q, k + 1):
                return True   # strictly decreasing => automatically self-avoiding
        return False
    return rec(origin, 0)

random.seed(20261018)
NS = 20000
for d in (2, 3):
    D = 2 * d
    for n in range(1, 6):
        hits = 0
        for _ in range(NS):
            if has_dec_path({}, d, n):
                hits += 1
        p = hits / NS
        se = math.sqrt(max(p * (1 - p), 1.0 / NS) / NS)
        bound = D * (D - 1) ** (n - 1) / math.factorial(n + 1)
        C.check(f"MC Z{d} n={n}: P(L>=n)={p:.4f}+-{se:.4f} <= min(1,bound={bound:.4f}) (+4SE)",
                p <= min(1.0, bound) + 4 * se)
        if n == 1:
            exact = 1 - 1 / (D + 1)
            C.check(f"MC Z{d} n=1 agrees with exact 1-1/(D+1)={exact:.4f} within 4SE", abs(p - exact) <= 4 * se)

# ---------- (d) coding radius of the XOR rule on Z^1 ----------
def xi0_window(order, marks, sites):
    """Records on a finite window with blank exterior (an admissible extension:
    exterior clocks later than everything in the window)."""
    pos = {s: i for i, s in enumerate(sites)}
    rank = {s: order[i] for i, s in enumerate(sites)}
    rec = {}
    for s in sorted(sites, key=lambda s: rank[s]):
        earlier = [y for y in (s - 1, s + 1) if y in rank and rank[y] < rank[s]]
        if earlier:
            v = 0
            for y in earlier:
                v ^= rec[y]
            rec[s] = v
        else:
            rec[s] = marks[pos[s]]
    return rec[0]

def coding_lower_bound(m, W):
    sites = list(range(-W, W + 1))
    ball = [s for s in sites if abs(s) <= m]
    bidx = [sites.index(s) for s in ball]
    classes = {}
    for order in itertools.permutations(range(len(sites))):
        brank = tuple(sorted(range(len(ball)), key=lambda i: order[bidx[i]]))
        for mk in range(2 ** len(sites)):
            marks = [(mk >> i) & 1 for i in range(len(sites))]
            key = (brank, tuple(marks[i] for i in bidx))
            v = xi0_window(order, marks, sites)
            classes.setdefault(key, set()).add(v)
    nonconst = sum(1 for k, v in classes.items() if len(v) > 1)
    total = math.factorial(len(ball)) * 2 ** len(ball)
    assert len(classes) == total
    return F(nonconst, total)

lb2 = coding_lower_bound(1, 3)
L1 = F(2, 3)        # exact P(L>=1) on Z^1
map2 = F(2 * 1, math.factorial(3))   # map's proposed bound at n=2: 2d(2d-1)^(n-1)/(n+1)! with d=1
C.check(f"XOR rule: exact lower bound P(R>=2) >= {lb2} equals corrected upper bound P(L>=1)=2/3 (so P(R>=2)=2/3 exactly)", lb2 == L1)
C.check(f"XOR rule: P(R>=2)=2/3 EXCEEDS the map's proposed P(R>=2)<=2/3!={map2} (map constant is the L-tail, off by one for R)", lb2 > map2)
lb3 = coding_lower_bound(2, 3)
L2 = F(2, 6) - F(1, 5 * 4)
map3 = F(2, math.factorial(4))
C.check(f"XOR rule: lower bound P(R>=3) >= {lb3} (window [-3,3]) is <= corrected bound P(L>=2)={L2}", lb3 <= L2)
C.check(f"XOR rule: P(R>=3) >= {lb3} EXCEEDS map's proposed 2/4!={map3}", lb3 > map3)

C.finish()
