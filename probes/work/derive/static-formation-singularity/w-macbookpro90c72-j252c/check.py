#!/usr/bin/env python3
"""J:derive:static-formation-singularity:a2 -- exact checks.

Six-axis class-(P) rule at (p,q,r)=(3,1,2) on the 6-value menu with antipode s^1.
Static law mu(v)=W(v)/Z, W=prod_{edges} phi.  Formation law for an order:
nu(v)=prod_k r(v_{x_k}|recorded neighbours), r(s|A)=prod phi(s,.)/N(A).
All arithmetic below is exact (int / Fraction / isqrt); no floats enter any claim.
"""
import sys
from fractions import Fraction as F
from math import isqrt
from itertools import product, permutations

M = 6
PHI = [[3 if s == t else (1 if s == (t ^ 1) else 2) for t in range(M)] for s in range(M)]
_NC = {}


def Nf(ts):
    v = _NC.get(ts)
    if v is None:
        tot = 0
        for s in range(M):
            p = 1
            for t in ts:
                p *= PHI[s][t]
            tot += p
        _NC[ts] = tot
        v = tot
    return v


OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- S0 constants
Z1 = Nf((0,))
n2 = sorted({Nf((a, b)) for a in range(M) for b in range(M)})
n3 = sorted({Nf(tuple(sorted(t))) for t in product(range(M), repeat=3)})
n4 = sorted({Nf(tuple(sorted(t))) for t in product(range(M), repeat=4)})
need(Z1 == 12, "Z1")
need(n2 == [22, 24, 26], "N2 set")
need(min(n3) == 44 and max(n3) == 60, "N3 range")
need(min(n4) == 80 and max(n4) == 146, "N4 range")
need(Nf((0, 0)) == 26 and Nf((0, 1)) == 22 and Nf((0, 2)) == 24, "N2 values")
rec("ok S0 rule (3,1,2): Z1=%d, N2 in %s (equal/orth/antipodal=26/24/22), N3 in [%d,%d], N4 in [%d,%d]"
    % (Z1, n2, min(n3), max(n3), min(n4), max(n4)))


# ---------------------------------------------------------- window machinery
def mk(n, edges):
    adj = [[] for _ in range(n)]
    for (x, y) in edges:
        adj[x].append(y)
        adj[y].append(x)
    return adj


def predlist(order, adj):
    pos = {x: i for i, x in enumerate(order)}
    return [(x, tuple(sorted(y for y in adj[x] if pos[y] < pos[x]))) for x in order]


def Wof(v, edges):
    p = 1
    for (x, y) in edges:
        p *= PHI[v[x]][v[y]]
    return p


def Yof(v, pl):
    p = 1
    for (x, A) in pl:
        p *= Nf(tuple(sorted(v[y] for y in A)))
    return p


def nu_num_den(v, pl):
    num = 1
    den = 1
    for (x, A) in pl:
        for y in A:
            num *= PHI[v[x]][v[y]]
        den *= Nf(tuple(sorted(v[y] for y in A)))
    return num, den


# ------------------------------------------------- S1 fixed orders on cycle4
E4 = [(0, 1), (1, 2), (2, 3), (3, 0)]
adj4 = mk(4, E4)
cfg4 = list(product(range(M), repeat=4))
Z4 = sum(Wof(v, E4) for v in cfg4)
need(Z4 == 20784, "Z(2x2)=%d" % Z4)
allok = True
tvs = []
for order in permutations(range(4)):
    pl = predlist(order, adj4)
    tot = F(0)
    tv = F(0)
    for v in cfg4:
        num, den = nu_num_den(v, pl)
        W = Wof(v, E4)
        if num != W or den != Yof(v, pl):
            allok = False
        tot += F(num, den)
        tv += abs(F(W, Z4) - F(num, den))
    if tot != 1:
        allok = False
    tvs.append(tv / 2)
need(allok, "S1 fixed-order identity on cycle4")
need(min(tvs) == F(455, 31176), "min TV cycle4 = %s" % min(tvs))
rec("ok S1 cycle4: nu=W/Y and sum_v W/Y=1 for all 24 orders (so dnu/dmu=Z/Y, E_mu[Z/Y]=1, Z=E_nu[Y]); "
    "min_order TV=%s max=%s" % (min(tvs), max(tvs)))


# -------------------------------------------- S1b adapted (value-dependent)
def run_adapted(v, n, adj, rule):
    formed = []
    fs = set()
    num = 1
    den = 1
    for _ in range(n):
        x = rule(formed, v, fs, adj, n)
        A = [y for y in adj[x] if y in fs]
        for y in A:
            num *= PHI[v[x]][v[y]]
        den *= Nf(tuple(sorted(v[y] for y in A)))
        formed.append(x)
        fs.add(x)
    return num, den


def r1(formed, v, fs, adj, n):
    rem = [x for x in range(n) if x not in fs]
    if not formed:
        return rem[0]
    sv = sum(v[y] for y in formed)
    return min(rem, key=lambda x: ((x * 7 + sv * 5) % 11, x))


def r2(formed, v, fs, adj, n):
    rem = [x for x in range(n) if x not in fs]
    if not formed:
        return rem[-1]
    m = max(v[y] for y in formed)
    return min(rem, key=lambda x: ((x + m) % n, x))


def r3(formed, v, fs, adj, n):
    rem = [x for x in range(n) if x not in fs]
    if not formed:
        return rem[0]
    last = formed[-1]
    cand = [x for x in rem if x in adj[last]]
    if cand and v[last] % 2 == 0:
        return min(cand)
    return min(rem, key=lambda x: ((x * 3 + v[formed[0]]) % n, x))


def r4(formed, v, fs, adj, n):
    rem = [x for x in range(n) if x not in fs]
    if not formed:
        return rem[0]
    # next = unformed site with the most recorded neighbours; ties by value parity
    return max(rem, key=lambda x: (sum(1 for y in adj[x] if y in fs),
                                   (v[formed[-1]] + x) % 5, -x))


E23 = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]   # 2x3 ladder, site=3r+c
adj23 = mk(6, E23)
cfg23 = list(product(range(M), repeat=6))
Z23 = sum(Wof(v, E23) for v in cfg23)
adok = True
for (nm, n, adj, edges, cfgs) in (("cycle4", 4, adj4, E4, cfg4), ("2x3", 6, adj23, E23, cfg23)):
    for rule in (r1, r2, r3, r4):
        tot = F(0)
        for v in cfgs:
            num, den = run_adapted(v, n, adj, rule)
            if num != Wof(v, edges):
                adok = False
            tot += F(num, den)
        if tot != 1:
            adok = False
need(adok, "S1b adapted identity")
rec("ok S1b adapted: 4 value-dependent strategies on cycle4 and on the 2x3 ladder (Z=%d): "
    "numerator=W and sum_v W/Y=1 exactly, so the identity covers the hull's generators" % Z23)


# ------------------------------------------------------- S2 forest dichotomy
def tree_ok(n, edges, order):
    adj = mk(n, edges)
    pl = predlist(order, adj)
    Z = sum(Wof(v, edges) for v in product(range(M), repeat=n))
    if Z != 6 * 12 ** (n - 1):
        return False, Z, None
    for v in product(range(M), repeat=n):
        num, den = nu_num_den(v, pl)
        if F(num, den) != F(Wof(v, edges), Z):
            return False, Z, None
    return True, Z, max(len(A) for (_, A) in pl)


trees = [("path3", 3, [(0, 1), (1, 2)], (0, 1, 2)),
         ("P4", 4, [(0, 1), (1, 2), (2, 3)], (0, 1, 2, 3)),
         ("star4", 4, [(0, 1), (0, 2), (0, 3)], (0, 1, 2, 3)),
         ("tree5", 5, [(0, 1), (1, 2), (2, 3), (2, 4)], (0, 1, 2, 3, 4)),
         ("comb6", 6, [(0, 1), (1, 2), (0, 3), (1, 4), (2, 5)], (0, 1, 2, 3, 4, 5))]
for (nm, n, E, o) in trees:
    good, Z, mx = tree_ok(n, E, o)
    need(good, "S2 forest %s" % nm)
    need(mx == 1, "S2 %s connected order" % nm)
rec("ok S2 forest: path3,P4,star4,tree5,comb6 with a connected order: every non-root has exactly 1 "
    "predecessor, Y=6*12^(n-1)=Z_W and nu=mu exactly on all 6^n configs")

# star4 with a NON-connected order: mu is still in the hull but this order is not a witness
adjs = mk(4, [(0, 1), (0, 2), (0, 3)])
pls = predlist((1, 2, 3, 0), adjs)
Zs = 6 * 12 ** 3
tv = F(0)
for v in product(range(M), repeat=4):
    num, den = nu_num_den(v, pls)
    tv += abs(F(Wof(v, [(0, 1), (0, 2), (0, 3)]), Zs) - F(num, den))
tv /= 2
need(tv > 0, "S2 star4 leaves-first")
rec("ok S2 sharpness: on the same forest star4 the leaves-first order (1,2,3,0) gives TV=%s>0, so the "
    "witness is the connected order, not the window alone" % tv)


# ============================================================== part 2 (S3-S8)
from math import lcm, log
import numpy as np   # floats ONLY locate positive test vectors; every claim below is an exact inequality


def dp_sup(n, adj, term):
    """sup over ALL adapted strategies (next site = any function of the values already formed) of
    E_nu[term(v)], term a nonnegative integer.  V(pi)=max_x sum_s r(s|pi,x) V(pi+x:s).  Every r has
    denominator dividing L = lcm of the Nf values, so V(pi)*L^(#unformed) is an integer."""
    L = 1
    for d in range(max(len(a) for a in adj) + 1):
        for t in product(range(M), repeat=d):
            L = lcm(L, Nf(tuple(sorted(t))))
    AC = {}
    memo = {}

    def avec(vals):
        a = AC.get(vals)
        if a is None:
            N = Nf(vals)
            a = []
            for s in range(M):
                pr = 1
                for t in vals:
                    pr *= PHI[s][t]
                a.append(pr * L // N)
            AC[vals] = a
        return a

    def V(st):
        r = memo.get(st)
        if r is not None:
            return r
        if -1 not in st:
            r = term(st)
            memo[st] = r
            return r
        best = -1
        lst = list(st)
        for x in range(n):
            if st[x] != -1:
                continue
            a = avec(tuple(sorted(st[y] for y in adj[x] if st[y] != -1)))
            tot = 0
            for s in range(M):
                lst[x] = s
                tot += a[s] * V(tuple(lst))
            lst[x] = -1
            if tot > best:
                best = tot
        memo[st] = best
        return best

    return F(V(tuple([-1] * n)), L ** n), memo, L, avec


def rel(a, b):
    return 0 if a == b else (2 if a == (b ^ 1) else 1)      # 0 equal, 1 orthogonal, 2 antipodal


def isq_lo(num, den, D):
    """floor(D*sqrt(num/den))"""
    return isqrt(num * D * D // den)


def isq_hi(num, den, D):
    """ceil(D*sqrt(num/den))"""
    q = isqrt(num * D * D // den)
    return q if q * q * den == num * D * D else q + 1


# ------------------------------------ S3 exact TV to the FULL adapted hull on the 2x2
plA, plA2 = predlist((0, 1, 3, 2), adj4), predlist((2, 1, 3, 0), adj4)    # corners 0, 2
plB, plB2 = predlist((1, 0, 2, 3), adj4), predlist((3, 0, 2, 1), adj4)    # corners 1, 3
okc = True
cls = {}
E2 = set()
muE = nuAE = nuBE = tv3 = F(0)
for v in cfg4:
    W = Wof(v, E4)
    N1, N2 = Nf(tuple(sorted((v[0], v[2])))), Nf(tuple(sorted((v[1], v[3]))))
    YA, YB = Yof(v, plA), Yof(v, plB)
    okc &= YA == 864 * N2 == Yof(v, plA2) and YB == 864 * N1 == Yof(v, plB2)
    k = (rel(v[0], v[2]), rel(v[1], v[3]))
    cls[k] = cls.get(k, 0) + W
    mu, nb = F(W, Z4), (F(W, YA) + F(W, YB)) / 2
    tv3 += abs(mu - nb)
    if mu > nb:
        E2.add(v)
        muE += mu
        nuAE += F(W, YA)
        nuBE += F(W, YB)
        okc &= F(1, N1) + F(1, N2) < F(1728, Z4) and sorted((N1, N2)) in ([26, 26], [24, 26])
    else:
        okc &= sorted((N1, N2)) not in ([26, 26], [24, 26])
tv3 /= 2
need(okc, "S3 corner laws Y_A=864*N2, Y_B=864*N1 and Scheffe set")
need(cls == {(0, 0): 876, (0, 1): 2688, (1, 0): 2688, (0, 2): 492, (2, 0): 492, (1, 1): 9216,
             (1, 2): 1920, (2, 1): 1920, (2, 2): 492}, "S3 class weights")
need(muE == F(521, 1732) and nuAE == nuBE == F(1619, 5616), "S3 mu(E), nu(E)")
need(tv3 == F(30457, 2431728) == muE - (nuAE + nuBE) / 2, "S3 TV(mu,nubar)")
supE, memo4, L4, avec4 = dp_sup(4, adj4, lambda st: 1 if st in E2 else 0)
need(supE == F(1619, 5616), "S3 Bellman sup_H nu(E) = %s" % supE)
bell = True        # V(pi) >= sum_s r V(pi+x:s) for every unformed x, with equality at some x
for st, val in memo4.items():
    if -1 in st:
        lst, vals = list(st), []
        for x in range(4):
            if st[x] == -1:
                a = avec4(tuple(sorted(st[y] for y in adj4[x] if st[y] != -1)))
                tot = 0
                for s in range(M):
                    lst[x] = s
                    tot += a[s] * memo4[tuple(lst)]
                lst[x] = -1
                vals.append(tot)
        bell &= max(vals) == val
need(bell, "S3 Bellman table")
rec("ok S3 2x2 FULL hull: E={one diagonal pair equal, other not antipodal} (class weights 876,2688x2,492x2,"
    "9216,1920x2,492); mu(E)=%s, Bellman DP over 7^4 states sup_H nu(E)=%s=nu_A(E)=nu_B(E); nubar=(nu_A+nu_B)/2 "
    "in H has TV=%s=mu(E)-sup_H nu(E), so TV(mu,H_2x2)=%s exactly and 1_E is an optimal test"
    % (muE, supE, tv3, tv3))


# ------------------------------ S4 m disjoint plaquettes: exact hull sup of E-count tests
pa, pc = muE.numerator, muE.denominator          # p = mu(E)       = 521/1732
qa, qc = supE.numerator, supE.denominator        # q = sup_H nu(E) = 1619/5616


def tail(m, k, a, c):
    """sum_{j>=k} C(m,j) a^j (c-a)^(m-j), i.e. c^m * P(Bin(m,a/c) >= k), exact."""
    b, T, S, j = c - a, a ** m, 0, m
    while j >= k:
        S += T
        if j == 0:
            break
        T = T * j * b // ((m - j + 1) * a)             # exact: T_{j-1} = C(m,j-1) a^(j-1) b^(m-j+1)
        j -= 1
    return S


def gap_ge_half(m, k):
    """P(Bin(m,p)>=k) - P(Bin(m,q)>=k) >= 1/2, cross-multiplied."""
    return 2 * tail(m, k, pa, pc) * qc ** m - 2 * tail(m, k, qa, qc) * pc ** m >= pc ** m * qc ** m


def kstar(m):
    """least j with Bin(m,p)(j) >= Bin(m,q)(j); the ratio is increasing in j (p>q), so
    max_k [P_p(>=k)-P_q(>=k)] = TV(Bin(m,p),Bin(m,q)) is attained at k=kstar."""
    lo, hi = 0, m
    while lo < hi:
        j = (lo + hi) // 2
        if pa ** j * (pc - pa) ** (m - j) * qc ** m >= qa ** j * (qc - qa) ** (m - j) * pc ** m:
            hi = j
        else:
            lo = j + 1
    return lo


M1, K1 = 2410, 710
ks1, ks0 = kstar(M1), kstar(M1 - 1)
need(ks1 == K1 and gap_ge_half(M1, K1), "S4 TV>=1/2 at m=%d" % M1)
need(not gap_ge_half(M1 - 1, ks0), "S4 E-count tests fail at m=%d" % (M1 - 1))
# converse: nubar^{(x)m} is in H_m; BC(mu,nubar) = sum_class W*sqrt((N1+N2)/(1728*Z*N1*N2))
Dp = 10 ** 30
Slo = Shi = 0
for (i, j), Wc in cls.items():
    n1, n2 = (26, 24, 22)[i], (26, 24, 22)[j]
    Slo += Wc * isq_lo(n1 + n2, 1728 * Z4 * n1 * n2, Dp)
    Shi += Wc * isq_hi(n1 + n2, 1728 * Z4 * n1 * n2, Dp)
need(4 * Slo ** 1904 > 3 * Dp ** 1904, "S4 BC^(2*952) > 3/4")
need(4 * Shi ** 1906 <= 3 * Dp ** 1906, "S4 BC route stops at 953")
# closed form: TV(Bin,Bin) >= 1 - BC_b^m, BC_b = sqrt(pq)+sqrt((1-p)(1-q)) <= beta
bnum = isq_hi(pa * qa, pc * qc, Dp) + isq_hi((pc - pa) * (qc - qa), pc * qc, Dp)   # beta = bnum/Dp
need(10 ** 10 * (Dp - bnum) >= 943777 * Dp, "S4 1-beta >= 9.43777e-5")
need(2 * bnum ** 7345 <= Dp ** 7345 and 2 * bnum ** 7344 > Dp ** 7344, "S4 closed form reaches 1/2 at 7345")
rec("ok S4 m disjoint 2x2: multi-affine Bellman => sup_H E_nu G(1_E copies) = G^(q,..,q) for every nondecreasing "
    "G, q=%s; so TV(mu^m,H_m) >= TV(Bin(m,%s),Bin(m,q)) >= 1/2 at m=%d (k=%d; at m=%d the best k=%d fails); "
    "nubar^m in H_m and BC(mu,nubar)^1904 > 3/4 give TV<1/2 for m<=952 (BC route fails at 953): threshold in "
    "[953,%d] (a1: [496,9268]); closed form TV >= 1-beta^m with 1-beta >= 9.43777e-5 (1/2 from m=7345)"
    % (supE, muE, M1, K1, M1 - 1, ks0, M1))


# ------------------- S5 corner (monotone) orders on w x L strips and the 2x2xL tube
def N2f(a, b):
    return Nf(tuple(sorted((a, b))))


def N3f(a, b, c):
    return Nf(tuple(sorted((a, b, c))))


def geom(kind, w, L):
    """sites, edges and the corner order of a w x L strip (site=w*i+j, column i, row j) or of the
    2x2xL tube (site=4i+2a+b); the corner order is column-major / lex from site 0."""
    if kind == "strip":
        n = w * L
        E = [(w * i + j - 1, w * i + j) for i in range(L) for j in range(1, w)]
        E += [(w * (i - 1) + j, w * i + j) for i in range(1, L) for j in range(w)]
    else:
        n = 4 * L
        E = [(4 * i + x, 4 * i + y) for i in range(L) for (x, y) in ((0, 1), (0, 2), (1, 3), (2, 3))]
        E += [(4 * (i - 1) + x, 4 * i + x) for i in range(1, L) for x in range(4)]
    return n, E, tuple(range(n))


def strip_data(w):
    st = list(product(range(M), repeat=w))
    intra = [1] * len(st)
    for k, s in enumerate(st):
        for j in range(1, w):
            intra[k] *= PHI[s[j - 1]][s[j]]

    def row(i):
        t = st[i]
        Tr, Dr = [], []
        for k, s in enumerate(st):
            x, d = intra[k], 1
            for j in range(w):
                x *= PHI[t[j]][s[j]]
            for j in range(1, w):
                d *= N2f(t[j], s[j - 1])
            Tr.append(x)
            Dr.append(d)
        return Tr, Dr
    return st, row, intra, intra[:], 1, 6 * 12 ** (w - 1)


DT = 10 ** 15


def tube_data():
    st = list(product(range(M), repeat=4))           # (s00, s01, s10, s11)
    intra = [PHI[s[0]][s[1]] * PHI[s[0]][s[2]] * PHI[s[1]][s[3]] * PHI[s[2]][s[3]] for s in st]
    U0 = [isq_hi(intra[k] ** 2, N2f(s[1], s[2]), DT) for k, s in enumerate(st)]   # >= DT*intra/sqrt(den0)

    def row(i):
        t = st[i]
        Tr, Dr = [], []
        for k, s in enumerate(st):
            Tr.append(intra[k] * PHI[t[0]][s[0]] * PHI[t[1]][s[1]] * PHI[t[2]][s[2]] * PHI[t[3]][s[3]])
            Dr.append(N2f(s[0], t[1]) * N2f(s[0], t[2]) * N3f(s[1], s[2], t[3]))
        return Tr, Dr
    return st, row, intra, U0, DT, 864


def transfer_ok(kind, w, L, data):
    """exact: W = u0(col0) prod T and Y(corner order) = const0*den0(col0)*prod 12*den, on every config"""
    st, row, intra, U0, D0, const0 = data
    n, E, order = geom(kind, w, L)
    pl = predlist(order, mk(n, E))
    cw = len(st[0])
    ix = {s: k for k, s in enumerate(st)}
    rows = {}
    for v in product(range(M), repeat=n):
        c = [ix[tuple(v[cw * i:cw * (i + 1)])] for i in range(L)]
        Wt = intra[c[0]]
        Yt = const0 * (N2f(v[1], v[2]) if kind == "tube" else 1)
        for i in range(1, L):
            if c[i - 1] not in rows:
                rows[c[i - 1]] = row(c[i - 1])
            Tr, Dr = rows[c[i - 1]]
            Wt *= Tr[c[i]]
            Yt *= 12 * Dr[c[i]]
        if Wt != Wof(v, E) or Yt != Yof(v, pl):
            return False
    return True


need(transfer_ok("strip", 2, 3, strip_data(2)) and transfer_ok("strip", 3, 2, strip_data(3))
     and transfer_ok("strip", 2, 2, strip_data(2)), "S5 strip transfer representation")
# down-set fact: the 2x3 corner law summed over its last column is the 2x2 corner law
n23s, E23s, o23s = geom("strip", 2, 3)
n22s, E22s, o22s = geom("strip", 2, 2)
pl23s, pl22s = predlist(o23s, mk(n23s, E23s)), predlist(o22s, mk(n22s, E22s))
marg = {}
for v in product(range(M), repeat=6):
    a, b = nu_num_den(v, pl23s)
    marg[v[:4]] = marg.get(v[:4], F(0)) + F(a, b)
need(all(marg[v] == F(*nu_num_den(v, pl22s)) for v in cfg4), "S5 down-set marginal")
# tube: on the 2x2x3 tube the corner order's predecessor sets are exactly the lower neighbours, which is
# what tube_data's first-slice factor 864*N2(s01,s10) and step factor 12*N2*N2*N3 encode
nt, Et, ot = geom("tube", 2, 3)
want = {}
for i in range(3):
    for (x, low) in ((0, ()), (1, (0,)), (2, (0,)), (3, (1, 2))):
        want[4 * i + x] = tuple(sorted([4 * i + y for y in low] + ([4 * i + x - 4] if i else [])))
need(dict(predlist(ot, mk(nt, Et))) == want, "S5 tube predecessor sets")


def perron_int(A, it=3000):
    x = np.ones(A.shape[0])
    for _ in range(it):
        y = A @ x
        x = y / y.max()
    return [max(1, int(round(t * 1e12))) for t in x]


def certify(data):
    st, row, intra, U0, D0, const0 = data
    n = len(st)
    Tf, Df = np.zeros((n, n)), np.zeros((n, n))
    for i in range(n):
        Tr, Dr = row(i)
        Tf[i], Df[i] = Tr, Dr
    u, v = perron_int(Tf), perron_int(Tf / np.sqrt(Df))
    del Tf, Df
    lam = rho = None
    AC = {}
    for i in range(n):
        Tr, Dr = row(i)
        li = F(sum(a * b for a, b in zip(Tr, u)), u[i])
        tot = 0
        for a, d, b in zip(Tr, Dr, v):
            key = (a, d)
            c = AC.get(key)
            if c is None:
                c = isq_hi(a * a, d, DT)                  # >= DT*T/sqrt(den), exact ceiling
                AC[key] = c
            tot += c * b
        ri = F(tot, DT * v[i])
        lam = li if lam is None or li < lam else lam
        rho = ri if rho is None or ri > rho else rho
    r2 = rho * rho / (12 * lam)
    rn = -((-r2.numerator * 10 ** 12) // r2.denominator)  # ceil(r2 * 1e12)
    Uv = sum(a * b for a, b in zip(U0, v))
    K = F(Uv * Uv, D0 * D0 * min(v) ** 2) * F(max(u), const0 * sum(a * b for a, b in zip(intra, u)))
    return lam, rho, rn, K


def first_L(K, rn, thr):
    def ok(L):
        return K.numerator * rn ** (L - 1) * thr.denominator <= thr.numerator * K.denominator * 10 ** (12 * (L - 1))
    L = max(2, 1 + int(log(float(thr / K)) / log(rn / 1e12)))     # float start; ok() decides exactly
    while not ok(L):
        L += 1
    while L > 1 and ok(L - 1):
        L -= 1
    return L


lam1, rho1, rn1, K1w = certify(strip_data(1))
need(lam1 == rho1 == 12 and rn1 == 10 ** 12 and K1w == 1, "S5 w=1 sanity r^2=1, K=1")
S5 = {}
for (nm, data, w, Kh) in (("w2", strip_data(2), 2, 4), ("w3", strip_data(3), 3, 4), ("tube", tube_data(), 4, 8)):
    lam, rho, rn, K = certify(data)
    need(rn < 10 ** 12, "S5 %s r^2<1" % nm)
    S5[nm] = (lam, rho, rn, K, first_L(K, rn, F(1, 4)), first_L(K, rn, F(1, 4 * Kh)),
              first_L(K, rn, F(1, 10 ** 4 * Kh)), w)


def ceil4(x):
    c = -((-x.numerator * 10 ** 4) // x.denominator)
    return "%d.%04d" % divmod(c, 10 ** 4)


rec("ok S5 corner-order certificates BC_1^2 <= K*r2^(L-1) (w=1 sanity: r2=1, K=1 exactly); per geometry: "
    "1-r2 >= X e-12, K <=, first L where the certificate gives TV>=1/2 vs one corner law / vs the whole "
    "monotone hull / TV>=0.99 vs the hull: "
    + "; ".join("%s: %d, %s, %d/%d/%d" % (nm, 10 ** 12 - t[2], ceil4(t[3]), t[4], t[5], t[6])
                for nm, t in S5.items()))


# ------------------------------------------------ S6 the 2x2x2 cube (lex = corner order)
nC8, EC8, oC8 = geom("tube", 2, 2)                       # site 4x+2y+z
plC = predlist(oC8, mk(nC8, EC8))
inner = [(1, 3), (1, 5), (2, 3), (2, 6), (4, 5), (4, 6)]
need([A for _, A in plC] == [(), (0,), (0,), (1, 2), (0,), (1, 4), (2, 4), (3, 5, 6)]
     and sorted(tuple(sorted(e)) for e in EC8) == sorted([(0, 1), (0, 2), (0, 4), (3, 7), (5, 7), (6, 7)] + inner),
     "S6 cube predecessors/edges")
byY = {}
for w6 in product(range(M), repeat=6):
    v = (0,) + w6
    wt = N3f(v[1], v[2], v[4]) * N3f(v[3], v[5], v[6])  # v0 and v7 summed out
    for (a, b) in inner:
        wt *= PHI[v[a]][v[b]]
    Y = 10368 * N2f(v[1], v[2]) * N2f(v[1], v[4]) * N2f(v[2], v[4]) * N3f(v[3], v[5], v[6])
    byY[Y] = byY.get(Y, 0) + wt
ZC = sum(byY.values())
tvc = sum(abs(F(w, ZC) - F(w, Y)) for Y, w in byY.items()) / 2
need(ZC == 6982520832 and sum(F(w, Y) for Y, w in byY.items()) == 1, "S6 cube Z and normalisation")
need(tvc == F(1182193085, 23402354976), "S6 cube single-corner TV = a1's value")
mu_c, nu_c = F(6 * 3 ** 12, ZC), F(6 * 3 ** 12, 10368 * 26 ** 3 * 60)
# the 8-corner uniform mixture: by invariance of mu and convexity of TV it is the TV-closest point of the
# monotone hull.  Exact integer arithmetic in int64 (W <= 3^12, Y <= 1.1e10), configs with v0=0 times 6.
Pn = np.array(PHI, dtype=np.int64)
N2n = np.array([[N2f(a, b) for b in range(M)] for a in range(M)], dtype=np.int64)
N3n = np.array([[[N3f(a, b, c) for c in range(M)] for b in range(M)] for a in range(M)], dtype=np.int64)
V8 = np.array([(0,) + t for t in product(range(M), repeat=7)], dtype=np.int64)
W8 = np.ones(len(V8), dtype=np.int64)
for (a, b) in EC8:
    W8 *= Pn[V8[:, a], V8[:, b]]
Ys = np.stack([10368 * N2n[V8[:, 1 ^ m], V8[:, 2 ^ m]] * N2n[V8[:, 1 ^ m], V8[:, 4 ^ m]]
               * N2n[V8[:, 2 ^ m], V8[:, 4 ^ m]] * N3n[V8[:, 3 ^ m], V8[:, 5 ^ m], V8[:, 6 ^ m]]
               for m in range(8)], axis=1)
U8, inv8 = np.unique(Ys, axis=0, return_inverse=True)
Ws8 = np.zeros(len(U8), dtype=np.int64)
np.add.at(Ws8, inv8.ravel(), W8)
need(6 * int(W8.sum()) == ZC, "S6 cube Z (numpy)")
tv8 = muE8 = nuE8 = F(0)
nuk8 = [F(0)] * 8
for row, w in zip(U8.tolist(), Ws8.tolist()):
    mu_r = F(6 * w, ZC)
    nb_r = sum(F(6 * w, y) for y in row) / 8
    tv8 += abs(mu_r - nb_r)
    if mu_r > nb_r:
        muE8 += mu_r
        nuE8 += nb_r
        nuk8 = [a + F(6 * w, y) for a, y in zip(nuk8, row)]
tv8 /= 2
need(tv8 == muE8 - nuE8 and len(set(nuk8)) == 1 and tv8 < tvc, "S6 cube 8-corner mixture")
rec("ok S6 2x2x2: Z=%d, one corner law TV=%s (a1's value); all-equal event mu=%s vs corner law %s (gap %s); "
    "uniform 8-corner mixture (TV-closest point of the monotone hull): TV=%s, attained by E8={mu>nubar8} with "
    "mu(E8)=%s, nu_k(E8)=%s for every corner k" % (ZC, tvc, mu_c, nu_c, mu_c - nu_c, tv8, muE8, nuk8[0]))


# ------------------------------------------------------ S7 route no-go: the pointwise envelope
def yhat(v, n, adj):
    """min over ALL orders of Y(v): g(S) = min_{x in S} g(S-x) * Nf(v on nbrs(x) in S-x)"""
    g = [1] * (1 << n)
    for S in range(1, 1 << n):
        best = None
        for x in range(n):
            if S >> x & 1:
                R = S & ~(1 << x)
                val = g[R] * Nf(tuple(sorted(v[y] for y in adj[x] if R >> y & 1)))
                best = val if best is None or val < best else best
        g[S] = best
    return g[-1]


env = F(0)
yok = True
for v in cfg4:
    yh = yhat(v, 4, adj4)
    nmin = min(N2f(v[0], v[2]), N2f(v[1], v[3]))
    yok &= yh == min(36 * nmin * nmin, 864 * nmin)
    if yh > Z4:
        env += F(Wof(v, E4), Z4) * (1 - F(Z4, yh))
need(yok and env == F(876, 20784) * F(35, 468) and env < tv3, "S7 2x2 envelope")
yh23 = yhat((0,) * 6, 6, adj23)
need(yh23 == 7008768 > Z23, "S7 2x3 envelope positive")
st2, row2, intra2, _, _, _ = strip_data(2)
TG = np.zeros((36, 36))
TGi = []
for i, t in enumerate(st2):
    Tr, _ = row2(i)
    TGi.append([Tr[k] * 12 * min(N2f(t[1], s[0]), N2f(t[0], s[1])) for k, s in enumerate(st2)])
    TG[i] = TGi[-1]
vG = perron_int(TG)
rhoG = max(F(sum(a * b for a, b in zip(TGi[i], vG)), vG[i]) for i in range(36))
lam2 = S5["w2"][0]
need(rhoG < F(980098, 10 ** 6) * lam2 * lam2, "S7 rho(T.G) < 0.980098 lambda^2")
rec("ok S7 envelope: every nu in H has nu <= W/Yhat (Yhat = min over orders, subset DP), so TV(mu,H) >= "
    "E_mu(1-Z/Yhat)^+; 2x2: Yhat=min(36n^2,864n) at n=min(N1,N2) and the envelope is %s < %s (lossy); 2x3: "
    "Yhat(all equal)=%d > Z=%d so it is positive; 2xL: envelope <= 72 u0.(T.G)^(L-1)1/Z_L^2 with "
    "rho_up(T.G)/lambda_low^2 < 0.980098 exactly, so it decays and gives no uniform full-hull bound"
    % (env, tv3, yh23, Z23))


# ------------------------------- S8 the 2x3 ladder: monotone, fixed-order and FULL adapted hulls
BV = []                                                  # the 48 value maps preserving phi (antipode pairs)
for perm in permutations(range(3)):
    for flips in product(range(2), repeat=3):
        BV.append(tuple(2 * perm[i // 2] + ((i & 1) ^ flips[i // 2]) for i in range(6)))
need(all(PHI[g[s]][g[t]] == PHI[s][t] for g in BV for s in range(M) for t in range(M)), "S8 value symmetries")
GEO = [tuple(3 * rr + cc for rr in rs for cc in cs) for rs in ((0, 1), (1, 0)) for cs in ((0, 1, 2), (2, 1, 0))]
ix23 = {v: i for i, v in enumerate(cfg23)}
W23 = [Wof(v, E23) for v in cfg23]
Yc = [Yof(v, predlist((0, 1, 2, 3, 4, 5), adj23)) for v in cfg23]      # corner 0; corners 2,3,5 = reflections
PG = [[ix23[tuple(v[g[x]] for x in range(6))] for v in cfg23] for g in GEO]
need(all(W23[PG[k][i]] == W23[i] for k in range(4) for i in range(len(cfg23))), "S8 reflections are automorphisms")
E4s, muE4, nbE4, tv4 = set(), F(0), F(0), F(0)
for i, v in enumerate(cfg23):
    mu, nb = F(W23[i], Z23), sum(F(W23[i], Yc[PG[k][i]]) for k in range(4)) / 4
    tv4 += abs(mu - nb)
    if mu > nb:
        E4s.add(v)
        muE4 += mu
        nbE4 += nb
tv4 /= 2
need(tv4 == F(812090431, 41067000000) == muE4 - nbE4, "S8 corner mixture TV")
best = F(0)
seen = set()
for o in permutations(range(6)):                         # every fixed order (98 predecessor structures)
    pl = predlist(o, adj23)
    key = tuple(sorted(pl))
    if key in seen:
        continue
    seen.add(key)
    byy = {}
    for v in E4s:
        y = Yof(v, pl)
        byy[y] = byy.get(y, 0) + W23[ix23[v]]
    best = max(best, sum(F(w, y) for y, w in byy.items()))
need(len(seen) == 98 and best == nbE4, "S8 max over fixed orders of nu(E4)")
# value-dependent strategies: row 0 formed as the path 0,1,2; then the first site of row 1 is chosen from
# (v0,v1,v2) and the second from the value just formed.  Code per top-triple class: (k-3)*64 + bits,
# k = first site of row 1; bit s = 1 means "then site 4" after value s (read in the class representative).
TOPR = sorted({min(tuple(g[x] for x in t) for g in BV) for t in product(range(M), repeat=3)})
TOPC = {}
for ri, r in enumerate(TOPR):
    for g in BV:
        TOPC.setdefault(tuple(g[x] for x in r), (ri, [g.index(s) for s in range(M)]))
CODES = [[61, 64, 181, 62, 64, 62, 55, 64, 53, 183, 55], [61, 64, 63, 62, 64, 182, 55, 64, 183, 61, 63],
         [1, 64, 141, 62, 64, 190, 55, 64, 7, 63, 55], [61, 64, 63, 62, 64, 138, 55, 64, 183, 14, 55],
         [61, 64, 189, 62, 64, 142, 7, 64, 55, 15, 53], [61, 64, 141, 62, 64, 190, 55, 64, 7, 63, 61],
         [1, 64, 63, 62, 64, 55, 55, 64, 183, 181, 61], [61, 64, 189, 62, 64, 63, 55, 64, 55, 183, 63],
         [61, 64, 63, 2, 64, 142, 55, 64, 183, 15, 61], [61, 64, 63, 62, 64, 190, 55, 64, 183, 63, 63],
         [61, 64, 55, 62, 64, 62, 7, 64, 181, 183, 61], [61, 64, 189, 2, 64, 62, 54, 64, 55, 183, 55],
         [61, 64, 55, 62, 64, 62, 53, 64, 181, 183, 53], [1, 64, 15, 62, 64, 62, 55, 64, 135, 183, 53],
         [61, 64, 63, 62, 64, 14, 54, 64, 183, 135, 21], [1, 64, 189, 62, 64, 62, 55, 64, 55, 183, 21],
         [61, 64, 55, 62, 64, 62, 54, 64, 181, 183, 53], [61, 64, 141, 62, 64, 134, 55, 64, 7, 15, 31],
         [61, 64, 7, 62, 64, 54, 55, 64, 133, 181, 55]]
LAM = [F(5489, 50000), F(4618289, 20625000), F(84779, 17187500), F(1898, 15625), F(1405037, 34375000),
       F(8304691, 103125000), F(47371, 12890625), F(11910781, 206250000), F(2299127, 51562500),
       F(976159, 10312500), F(682763, 34375000), F(832573, 51562500), F(949, 15625), F(300317, 25781250),
       F(167, 4125000), F(417449, 10312500), F(4594079, 103125000), F(216547, 20625000), F(178679, 12890625)]
need(len(TOPR) == 11 and sum(LAM) == 1 and min(LAM) > 0, "S8 mixture weights")
BOT = {}
for (k, k2) in ((3, 4), (3, 5), (4, 3), (5, 4), (5, 3)):
    o = (0, 1, 2, k, k2, 12 - k - k2)
    BOT[(k, k2)] = [Yof(v, predlist(o, adj23)) for v in cfg23]


def strat_Y(code):
    """Y along the order this strategy realises on each configuration (each choice reads formed values only)"""
    out = []
    for i, v in enumerate(cfg23):
        ri, ginv = TOPC[v[:3]]
        c = code[ri]
        k = 3 + c // 64
        if k == 4:
            k2 = 3
        else:
            k2 = 4 if c >> ginv[v[k]] & 1 else 8 - k
        out.append(BOT[(k, k2)][i])
    return out


SY = [strat_Y(c) for c in CODES]
LY = 1
for y in {y for Ys in SY for y in Ys}:
    LY = lcm(LY, y)
DL = 1
for x in LAM:
    DL = lcm(DL, x.denominator)
need(all(sum(W23[i] * (LY // Ys[i]) for i in range(len(cfg23))) == LY for Ys in SY), "S8 strategies normalised")
AS = [[LY // y for y in Ys] for Ys in SY]
sv = [0] * len(cfg23)                                    # nu*(v) = W(v) sv(v) / (4 DL LY), symmetrised over GEO
for lam_, A in zip(LAM, AS):
    Lm = lam_.numerator * (DL // lam_.denominator)
    for i in range(len(cfg23)):
        sv[i] += Lm * (A[PG[0][i]] + A[PG[1][i]] + A[PG[2][i]] + A[PG[3][i]])
CT = 4 * DL * LY
tvs8 = F(sum(W23[i] * (CT - Z23 * sv[i]) for i in range(len(cfg23)) if CT > Z23 * sv[i]), Z23 * CT)
TIED = {"000222": F(23, 99), "000224": F(8473, 78408), "000232": F(1), "000242": F(7, 44),
        "001002": F(184339, 303264), "001211": F(0), "002012": F(36421, 50544), "002014": F(1837, 2592),
        "002041": F(0), "002203": F(43, 48), "002221": F(13, 108), "002321": F(37, 144),
        "002405": F(3109, 4752), "002421": F(5, 72), "002454": F(0), "010232": F(1), "010242": F(1, 44),
        "012203": F(1, 24), "012242": F(15361, 41184), "012425": F(95, 96), "020020": F(1), "020030": F(5, 11),
        "020040": F(0), "020121": F(2, 33), "020131": F(0), "020141": F(0), "020424": F(1), "020434": F(1),
        "021142": F(41, 48)}
fst = {}
tied_keys = set()
for i, v in enumerate(cfg23):
    if CT > Z23 * sv[i]:
        fst[v] = F(1)
    elif CT < Z23 * sv[i]:
        fst[v] = F(0)
    else:
        key = "".join(map(str, min(tuple(g[v[q[x]]] for x in range(6)) for g in BV for q in GEO)))
        tied_keys.add(key)
        fst[v] = TIED[key]
need(tied_keys == set(TIED), "S8 tied classes")
DF = 1
for x in TIED.values():
    DF = lcm(DF, x.denominator)
eta, _, _, _ = dp_sup(6, adj23, lambda st: int(fst[st] * DF))
eta /= DF
lb8 = sum(fst[v] * F(W23[i], Z23) for i, v in enumerate(cfg23)) - eta
need(lb8 == tvs8 < F(874, 1000) * tv4, "S8 exact full-hull TV on 2x3")
rec("ok S8 2x3: corner mixture TV=%s = TV to the monotone hull; E4={mu>nubar4} has max over all 720 fixed "
    "orders nu(E4)=%s=nubar4(E4), so no mixture of fixed orders is closer; a mixture of 19 value-dependent "
    "strategies (row 0 first, row 1 order read off the formed values; x4 reflections) has TV=%s, and a test "
    "f* with Bellman sup_H E_nu f*=%s gives the same lower bound: TV(mu,H_2x3)=%s exactly (< 0.874 x the "
    "fixed-order value)" % (tv4, nbE4, tvs8, eta, lb8))


# ------------------------------------------------------------------------------ report
def dec12(nm):
    x = 10 ** 12 - S5[nm][2]                              # 1 - r2 >= x * 1e-12, printed exactly
    s = "%d" % x
    return "%s.%se-%d" % (s[0], s[1:].rstrip("0") or "0", 12 - len(s) + 1)


print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "PARTIAL exact hull distances at (3,1,2): the full adapted hull on 2x2 and 2x3; the E-count threshold "
      "[953,%d] on disjoint plaquettes; exact corner-order certificates on 2xL, 3xL strips and the 2x2xL tube "
      "(KL per column, monotone hull, singularity on the half-infinite strip); 2x2x2 monotone hull TV=%s; route "
      "no-go: the pointwise envelope decays on 2xL." % (M1, tv8)))
if not FAIL:
    print("HIT: TV(static law, closed convex hull of all adapted formation laws) is exact on the 2x2 = %s (the "
          "corner mixture attains the Bellman lower bound; optimal test 1_E, E = one diagonal pair equal and the "
          "other not antipodal) and on the 2x3 = %s (19 value-dependent strategies vs a test with matching "
          "Bellman sup), below %s = TV to all 720 fixed orders." % (tv3, lb8, tv4))
    print("HIT: m disjoint plaquettes: every nondecreasing G of the m E-indicators has sup over the adapted hull "
          "of E_nu G = G^(q,...,q), q=%s (multi-affine Bellman), so TV >= TV(Bin(m,%s),Bin(m,q)) >= 1-beta^m "
          "with 1-beta >= 9.43777e-5; TV >= 1/2 at m=%d and TV < 1/2 for m <= 952." % (supE, muE, M1))
    print("HIT: corner-order laws on w x L strips (w=2,3) and the 2x2xL tube: exact Perron certificates "
          "BC^2 <= K*r2^(L-1) with 1-r2 >= %s, %s, %s give KL >= (L-1)(1-r2) - log K, TV >= 1/2 against the "
          "whole monotone hull for L >= %d, %d, %d, and mutual singularity on the half-infinite strip and tube."
          % (dec12("w2"), dec12("w3"), dec12("tube"), S5["w2"][5], S5["w3"][5], S5["tube"][5]))
sys.exit(1 if FAIL else 0)
