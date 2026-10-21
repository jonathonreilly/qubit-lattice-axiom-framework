"""R1: XOR coding radius on Z, by a different method from the author.

XOR rule is linear over F_2: xi_0 = <c, U> with a coefficient vector c that
depends only on the relative clock order.  For a window pattern (relative
order on B(0,m), marks on B(0,m)) the set of achievable xi_0 over admissible
extensions on B(0,K) (outer exterior later than everything, a positive-
probability event under any continuous clock law) is {0,1} if some extension
has a nonzero coefficient outside B(0,m); else the set of <c_W,U_W>.
Exact rationals.  P(R>=m+1) >= fraction of non-determined patterns;
P(R>=m+1) <= P(L>=m) (R<=L+1).  m = 1,2,3 with K = m+1.
"""
import itertools, math
from fractions import Fraction as F
from rv_common import Checks
C = Checks("r1")

def coeff_vector(rank, sites):
    # rank[i] = clock rank of sites[i]; returns c(0) as bitmask over sites
    idx = {s: i for i, s in enumerate(sites)}
    c = {}
    for i in sorted(range(len(sites)), key=lambda i: rank[i]):
        s = sites[i]
        e = [idx[y] for y in (s-1, s+1) if y in idx and rank[idx[y]] < rank[i]]
        if e:
            v = 0
            for j in e: v ^= c[j]
            c[i] = v
        else:
            c[i] = 1 << i
    return c[idx[0]]

def L_ge(rank, sites, m):
    # longest strictly decreasing nearest-neighbour path from 0 >= m ?
    idx = {s: i for i, s in enumerate(sites)}
    best = {}
    for i in sorted(range(len(sites)), key=lambda i: rank[i]):
        s = sites[i]
        e = [idx[y] for y in (s-1, s+1) if y in idx and rank[idx[y]] < rank[i]]
        best[i] = 1 + max(best[j] for j in e) if e else 0
    return best[idx[0]] >= m

for m in (1, 2, 3):
    K = m + 1
    sites = list(range(-K, K+1))
    W = [i for i, s in enumerate(sites) if abs(s) <= m]
    Wmask = sum(1 << i for i in W)
    Emask = ((1 << len(sites)) - 1) & ~Wmask
    pats = {}
    Lcount = 0
    nperm = 0
    for rank in itertools.permutations(range(len(sites))):
        nperm += 1
        c = coeff_vector(rank, sites)
        key = tuple(sorted(W, key=lambda i: rank[i]))
        pats.setdefault(key, set()).add(c)
        if L_ge(rank, sites, m): Lcount += 1
    PL = F(Lcount, nperm)
    nondet = 0
    for key, cs in pats.items():
        anyE = any(c & Emask for c in cs)
        for u in range(1 << len(sites)):
            if u & Emask: continue
            if anyE:
                nondet += 1; continue
            vals = {bin(c & u).count("1") & 1 for c in cs}
            if len(vals) == 2: nondet += 1
    total = math.factorial(len(W)) * 2 ** len(W)
    PR = F(nondet, total)
    exactL = F(2, math.factorial(m+1)) - F(1, (2*m+1) * math.factorial(m)**2)
    mapb = F(2, math.factorial(m+2))   # map: P(R>=n) <= 2d(2d-1)^(n-1)/(n+1)! at n=m+1, d=1
    C.ok(f"m={m}: P(L>=m) by enumeration = {PL} equals closed form {exactL}", PL == exactL)
    C.ok(f"m={m}: non-determined fraction on B(0,{m}) = {PR} equals P(L>=m), so P(R>={m+1}) = {PR} exactly", PR == PL)
    C.ok(f"m={m}: P(R>={m+1}) = {PR} > map bound 2/{m+2}! = {mapb}  (map's R-statement false)", PR > mapb)
    C.ok(f"m={m}: corrected bound P(R>={m+1}) <= 2/{m+1}! = {F(2, math.factorial(m+1))} holds", PR <= F(2, math.factorial(m+1)))
C.done()
