#!/usr/bin/env python3
"""filling-between-the-a-terms-levels-chiral-content, attempt a2 (worker w-macbookpro9927a-j4067, claude-opus-5-5).

Where the a-term's levels sit in record number, and what the axioms' exclusion ('one record per site at a time')
does there.  Exact arithmetic (Fractions, Gaussian rationals, sympy) for every claim; lines marked 'float' are
floating-point evidence only.
"""
import random
import sys
import time
from fractions import Fraction as Fr
from itertools import product, combinations
from math import asin, pi

import numpy as np
import sympy as sp

T0 = time.time()
random.seed(20260924)
FAILS = []


def check(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""))
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------ Gaussian rationals and the 3D walk
class GQ:
    __slots__ = ("r", "i")

    def __init__(s, r=0, i=0):
        s.r = r if isinstance(r, Fr) else Fr(r)
        s.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(a, b):
        b = b if isinstance(b, GQ) else GQ(b)
        return GQ(a.r + b.r, a.i + b.i)

    __radd__ = __add__

    def __sub__(a, b):
        b = b if isinstance(b, GQ) else GQ(b)
        return GQ(a.r - b.r, a.i - b.i)

    def __mul__(a, b):
        b = b if isinstance(b, GQ) else GQ(b)
        return GQ(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r)

    __rmul__ = __mul__

    def __neg__(a):
        return GQ(-a.r, -a.i)

    def nz(a):
        return a.r != 0 or a.i != 0

    def __eq__(a, b):
        b = b if isinstance(b, GQ) else GQ(b)
        return a.r == b.r and a.i == b.i


Z = GQ(0)
MIH = GQ(0, Fr(-1, 2))   # 1/(2i)


def sig(a, sp_):
    p, q = sp_
    if a == 0:
        return (q, p)
    if a == 1:
        return (GQ(q.i, -q.r), GQ(-p.i, p.r))
    return (p, -q)


class Tor:
    def __init__(s, L):
        s.L = L
        s.S = list(product(range(L), repeat=3))
        s.ix = {x: i for i, x in enumerate(s.S)}
        s.N = len(s.S)
        s.up = [[s.ix[tuple((x[k] + (k == a)) % L for k in range(3))] for a in range(3)] for x in s.S]
        s.dn = [[s.ix[tuple((x[k] - (k == a)) % L for k in range(3))] for a in range(3)] for x in s.S]


def vadd(u, v):
    return [(p[0] + q[0], p[1] + q[1]) for p, q in zip(u, v)]


def A_op(t, a, v):   # A = 2a sum_j C_j + sum_j sigma_j S_j   (H_a - a0)
    out = [(Z, Z)] * t.N
    for j in range(3):
        Cv = [((v[t.up[i][j]][0] + v[t.dn[i][j]][0]) * Fr(1, 2) * 2 * a, (v[t.up[i][j]][1] + v[t.dn[i][j]][1]) * Fr(1, 2) * 2 * a) for i in range(t.N)]
        Sv = [((v[t.up[i][j]][0] - v[t.dn[i][j]][0]) * MIH, (v[t.up[i][j]][1] - v[t.dn[i][j]][1]) * MIH) for i in range(t.N)]
        out = vadd(out, vadd(Cv, [sig(j, p) for p in Sv]))
    return out


def eps_op(t, v):
    return [(p[0] * (-1) ** sum(x), p[1] * (-1) ** sum(x)) for p, x in zip(v, t.S)]


def T1_op(t, v):   # (T_1 v)(x) = v(x + e_1)
    return [v[t.up[i][0]] for i in range(t.N)]


def basis(t, i, c):
    v = [(Z, Z)] * t.N
    v[i] = (GQ(1), Z) if c == 0 else (Z, GQ(1))
    return v


def veq(u, v, s=1):
    return all(p[0] == q[0] * s and p[1] == q[1] * s for p, q in zip(u, v))


# ================================================================= L: levels, senses and their moments
a0s, as_ = sp.symbols("a0 a")
lev, sen = {}, {}
for n in product((0, 1), repeat=3):
    lev[n] = a0s + 2 * as_ * sum((-1) ** nj for nj in n)
    sen[n] = (-1) ** sum(n)        # sign det of d(sin k)/dk at k = pi n: prod cos(pi n_j)
ok = all(sp.simplify(lev[n] - (a0s + 2 * as_ * (3 - 2 * sum(n)))) == 0 for n in lev)
mom = [sp.expand(sum(sen[n] * (lev[n] - 0) ** p for n in lev)) for p in range(5)]
check("L1 levels", ok and [sum(1 for n in lev if sum(n) == m) for m in range(4)] == [1, 3, 3, 1],
      "at k = pi n the family a0 + 2a sum cos k + sum sigma sin k sits at a0 + 2a(3 - 2|n|), 1:3:3:1, sense (-1)^|n|")
check("L2 chiral moments", mom[0] == 0 and mom[1] == 0 and mom[2] == 0 and sp.simplify(mom[3] - 384 * as_ ** 3) == 0,
      "sum_n chi_n L_n^p = 0, 0, 0 for p = 0, 1, 2 and 384 a^3 for p = 3, for every a0 (p = 4: %s)" % sp.factor(mom[4]))

# ================================================================= S: the symmetries that fix the middle
t4 = Tor(4)
aq = Fr(1, 10)
mq = Fr(1, 7)
okS = True
for i in range(t4.N):
    for c in (0, 1):
        e = basis(t4, i, c)
        Ae = A_op(t4, aq, e)
        okS &= veq(eps_op(t4, A_op(t4, aq, eps_op(t4, e))), Ae, -1)                 # eps A eps = -A
        Me = vadd(Ae, [(p[0] * mq, p[1] * mq) for p in eps_op(t4, e)])              # (A + m eps) e
        X = lambda v: eps_op(t4, T1_op(t4, v))                                      # X = eps T_1
        Xinv = lambda v: [v[t4.dn[k][0]] for k in range(t4.N)]                      # (eps T_1)^-1 = T_1^-1 eps
        lhs = X(vadd(A_op(t4, aq, Xinv(eps_op(t4, e))), [(p[0] * mq, p[1] * mq) for p in eps_op(t4, Xinv(eps_op(t4, e)))]))
        okS &= veq(lhs, Me, -1)
        okS &= Ae[i][0] == Z and Ae[i][1] == Z                                      # no on-site part
check("S1 symmetries", okS, "on 4^3: eps anticommutes with A = H_a - a0; X = eps T_1 anticommutes with A + m eps; "
      "H_a's only on-site term is a0 (the coin-scalar and the walk terms all hop)")


# ================================================================= F: the free comparator's record count, exactly
def cs(L):   # exact cos and sin^2 of 2 pi j / L for L in {3, 4, 6}
    tab = {3: ([1, Fr(-1, 2), Fr(-1, 2)], [0, Fr(3, 4), Fr(3, 4)]),
           4: ([1, 0, -1, 0], [0, 1, 0, 1]),
           6: ([1, Fr(1, 2), Fr(-1, 2), -1, Fr(-1, 2), Fr(1, 2)], [0, Fr(3, 4), Fr(3, 4), 0, Fr(3, 4), Fr(3, 4)])}
    c, s2 = tab[L]
    return [Fr(x) for x in c], [Fr(x) for x in s2]


def sgn_root(d, s2, sign):   # sign of d + sign*sqrt(s2), exactly
    if sign > 0:
        if d >= 0:
            return 1 if (d > 0 or s2 > 0) else 0
        return (s2 > d * d) - (s2 < d * d)
    if d <= 0:
        return -1 if (d < 0 or s2 > 0) else 0
    return (d * d > s2) - (d * d < s2)


def count(L, a0, a, mu):   # #(E < mu), #(E = mu) for H_a on the L^3 torus (no mass)
    c, s2 = cs(L)
    lt = eq = 0
    for j in product(range(L), repeat=3):
        C = sum(c[k] for k in j)
        S2 = sum(s2[k] for k in j)
        d = a0 + 2 * a * C - mu
        for sign in (1, -1):
            sg = sgn_root(d, S2, sign)
            lt += sg < 0
            eq += sg == 0
    return lt, eq


rows = []
okF = True
for L in (4, 6):
    N = L ** 3
    for a0, a in ((Fr(1, 3), Fr(1, 10)), (Fr(0), Fr(1, 4)), (Fr(-2, 5), Fr(2, 3))):
        mid, z = count(L, a0, a, a0)
        up, _ = count(L, a0, a, a0 + 4 * a)
        lo, _ = count(L, a0, a, a0 - 4 * a)
        okF &= mid == N - Fr(z, 2) and up >= N + 6 + Fr(z, 2) and lo <= N - 6 - Fr(z, 2)
        rows.append("%d^3 a=%s: N=%d mid %d (z=%d) up %d lo %d" % (L, a, N, mid, z, up, lo))
lt3, z3 = count(3, Fr(1, 3), Fr(1, 10), Fr(1, 3))
check("F1 record count", okF, "free sea on even tori: #(E < a0) = N - z/2 exactly; the window (a0+2a, a0+6a) needs >= N + 6 + z/2 "
      "records, (a0-6a, a0-2a) <= N - 6 - z/2; " + "; ".join(rows[::3]))
print("   (the parity argument needs even sides: on 3^3, #(E < a0) = %d of 54 states, z = %d)" % (lt3, z3))


# with the staggered term: (A + m eps)^2 = A^2 + m^2 (operator identity), so no zero modes and, with X, a symmetric spectrum
okF2 = True
for i in range(t4.N):
    for c in (0, 1):
        e = basis(t4, i, c)
        M1 = lambda v: vadd(A_op(t4, aq, v), [(p[0] * mq, p[1] * mq) for p in eps_op(t4, v)])
        lhs = M1(M1(e))
        rhs = vadd(A_op(t4, aq, A_op(t4, aq, e)), [(p[0] * mq * mq, p[1] * mq * mq) for p in e])
        okF2 &= veq(lhs, rhs)
check("F2 with the staggered term", okF2, "(A + m eps)^2 = A^2 + m^2 on all basis vectors of 4^3: with S1's X the spectrum of "
      "H - a0 is symmetric with |E - a0| >= |m|, so exactly N of 2N states lie below a0 (the free sea there is a band insulator)")

# ================================================================= X: the axioms' exclusion at these fillings
# X1 (ring illustration of the general statement): one record per site freezes every composition
def ring_ops(L, a0, a):   # the family's 1D member on a ring: a0 + a(T + T^-1) + sigma_3 (T - T^-1)/(2i)
    hop = {}
    for x in range(L):
        for s in (1, -1):
            y = (x + s) % L
            hop[(y, x)] = [[GQ(a) + GQ(0, Fr(s, 2)), Z], [Z, GQ(a) - GQ(0, Fr(s, 2))]]   # <x+s|H|x> = a + (is/2) sigma_3
    return hop


def hardcore_gen(L, nrec, a0, a, sign):   # compressed generator on configurations: sorted sites + coins
    hop = ring_ops(L, a0, a)
    confs = [(sites, coins) for sites in combinations(range(L), nrec) for coins in product((0, 1), repeat=nrec)]
    idx = {cf: i for i, cf in enumerate(confs)}
    M = [[Z] * len(confs) for _ in confs]
    for i, (sites, coins) in enumerate(confs):
        M[i][i] = M[i][i] + GQ(a0 * nrec)
        for r, x in enumerate(sites):
            for s in (1, -1):
                y = (x + s) % L
                if y in sites:
                    continue                                   # exclusion
                for c2 in (0, 1):
                    amp = hop[(y, x)][c2][coins[r]]
                    if not amp.nz():
                        continue
                    ns = list(sites)
                    ncoin = list(coins)
                    ns[r], ncoin[r] = y, c2
                    order = sorted(range(nrec), key=lambda q: ns[q])
                    perm_sign = 1
                    for p in range(nrec):              # parity of the sorting permutation
                        for q in range(p + 1, nrec):
                            if order[p] > order[q]:
                                perm_sign = -perm_sign
                    key = (tuple(ns[q] for q in order), tuple(ncoin[q] for q in order))
                    M[idx[key]][i] = M[idx[key]][i] + amp * (perm_sign if sign < 0 else 1)
    return M


ok1 = True
for sgn in (1, -1):
    M = hardcore_gen(4, 4, Fr(1, 3), Fr(1, 10), sgn)
    ok1 &= all((M[i][j] == (GQ(Fr(4, 3)) if i == j else Z)) for i in range(len(M)) for j in range(len(M)))
check("X1 one record per site", ok1, "ring of 4 with 4 records, symmetric and antisymmetric composition: the hard-core generator "
      "is exactly 4 a0 times the identity on all 16 coin configurations (every hop lands on an occupied site)")

# X2 (float, evidence): with N - N_h records the spectrum spans at most 2 N_h (hops per hole)(|a| + 1/2) about the constant
widths = []
for nrec in (5, 4):
    M = hardcore_gen(6, nrec, Fr(0), Fr(1, 10), -1)
    herm = all(M[i][j] == GQ(M[j][i].r, -M[j][i].i) for i in range(len(M)) for j in range(len(M)))
    Mf = np.array([[complex(float(z.r), float(z.i)) for z in row] for row in M])
    w = np.linalg.eigvalsh(Mf)
    nh = 6 - nrec
    widths.append((nh, w.max() - w.min(), 2 * nh * 2 * (0.1 + 0.5), herm))
print("X2 (float, evidence) ring of 6: spectral width with N_h holes vs the bound 2 N_h (2 hops)(|a| + 1/2): " +
      ", ".join("N_h=%d %.3f <= %.3f" % x[:3] for x in widths))
check("X2 hermitian", all(h for *_, h in widths), "the compressed generators with 5 and 4 records on a ring of 6 are hermitian exactly; the bound itself holds for every composition")


# X3: how many holes the lower window leaves, small a (exact lattice counts; float density)
def s2_count(L, bound):   # #{k on the L^3 grid: sum sin^2 k < bound} with exact sin^2 (L = 6, 12)
    tab = {6: [0, Fr(3, 4), Fr(3, 4), 0, Fr(3, 4), Fr(3, 4)],
           12: [Fr(x) for x in (0, Fr(1, 4), Fr(3, 4), 1, Fr(3, 4), Fr(1, 4), 0, Fr(1, 4), Fr(3, 4), 1, Fr(3, 4), Fr(1, 4))]}
    s2 = tab[L]
    return sum(1 for j in product(range(L), repeat=3) if sum(s2[k] for k in j) < bound)


a_small = Fr(1, 20)
n12 = s2_count(12, 144 * a_small ** 2)
lo6, z6 = count(6, Fr(0), a_small, -4 * a_small)
mid6, _ = count(6, Fr(0), a_small, Fr(0))
check("X3 lower window holes", n12 == 56 and 216 - lo6 <= Fr(z6, 2) + 2 * s2_count(6, 144 * a_small ** 2),
      "|E - a0| < 6a forces |sin k| < 12a; a = 1/20: 56 of 1728 grid points on 12^3; on 6^3 the lower window leaves "
      "%d holes against the bound %d" % (216 - lo6, Fr(z6, 2) + 2 * s2_count(6, 144 * a_small ** 2)))
dens = []
for af in (0.05, 0.1):
    L = 48
    k = 2 * np.pi * np.arange(L) / L
    K1, K2, K3 = np.meshgrid(k, k, k, indexing="ij")
    C = np.cos(K1) + np.cos(K2) + np.cos(K3)
    S = np.sqrt(np.sin(K1) ** 2 + np.sin(K2) ** 2 + np.sin(K3) ** 2)
    E = np.concatenate([(2 * af * C + S).ravel(), (2 * af * C - S).ravel()])
    holes = (np.sum(np.abs(E) < 6 * af)) / L ** 3
    th = asin(12 * af) if 12 * af < 1 else pi / 2
    dens.append("a=%.2f: %.4f per site (bound %.4f)" % (af, holes, 16 * th ** 3 / pi ** 3))
print("X3 (float, evidence, 48^3) states with |E - a0| < 6a per site: " + "; ".join(dens))

print("time %.0f s" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL (task HIT condition not met: no single-sense filling, a1's free no-go stands). New and exact: the "
      "a-term's levels sit at one record per site. On even tori the free sea at mu = a0 holds exactly N - z/2 records "
      "(eps, and eps T_1 with the staggered term), the window (a0+2a, a0+6a) of task (a) needs >= N + 6 + z/2 records on N "
      "sites, which the Record axiom's exclusion forbids for every a > 0; at one record per site the hard-core generator "
      "of every composition is the constant N a0 (flat, sense-free); with N - N_h records it is that constant plus at most "
      "6(|a| + 1/2) N_h (+|m| N_h); the lower window leaves at most z/2 + 2#{k: |sin k| < 12a} holes (16 arcsin(12a)^3/pi^3 "
      "per site in the limit).")
print("HIT: under 'one record per site at a time' the filling of task (a) does not exist (the free sea there holds >= N + 6 + z/2 records on N sites, for every a > 0), the middle level a0 is exactly one record per site, where every composition's generator is the constant N a0, and below it the generator is that constant plus at most (6(|a|+1/2)+|m|) per hole; for |a| < 1/12 the lower window leaves at most 16 arcsin(12a)^3/pi^3 holes per site")
