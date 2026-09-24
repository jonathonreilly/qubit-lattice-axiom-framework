#!/usr/bin/env python3
"""moving-records-and-the-balance-of-the-two-charges, attempt a2 (worker w-macbookpro9927a-j30ab, claude-opus-5-5).

Records that move, and block 110's two charges of block 60's curvature member.  Exact rational arithmetic for every
claim (Fractions, sympy); the lines marked 'float' are a floating-point simulation, evidence only.
"""
import math
import random
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations, product

import numpy as np
import sympy as sp
from numba import njit

T0 = time.time()
random.seed(9924)
FAILS = []


def check(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""))
    if not ok:
        FAILS.append(tag)


class Tor:
    def __init__(s, L):
        s.L = L
        s.S = list(product(range(L), repeat=3))
        s.ix = {x: i for i, x in enumerate(s.S)}
        s.N = len(s.S)
        s.nb = [[s.ix[tuple((x[k] + d * (k == a)) % L for k in range(3))] for a in range(3) for d in (1, -1)] for x in s.S]


def moves(t, C):   # all (x, y, C') with x in C, y an empty neighbour of x
    occ = set(C)
    for x in C:
        for y in t.nb[x]:
            if y not in occ:
                Cp = tuple(sorted((occ - {x}) | {y}))
                yield x, y, Cp


# ================================================================= T1: crossing at the member's factor is blind to the fields
t3 = Tor(3)
s_ = [Fr(random.randint(3, 9), 5) for _ in range(t3.N)]          # w = s^2, so sqrt(w_x w_y) = s_x s_y is rational
chi = [Fr(random.randint(5, 11), 7) for _ in range(t3.N)]
w = [v * v for v in s_]
omega = {d: Fr(random.randint(1, 9), 4) for d in product(range(3), repeat=3)}   # an even pair weight: omega(d) = omega(-d)
for d in list(omega):
    omega[tuple((-c) % 3 for c in d)] = omega[d]


def W(C):
    r = Fr(1)
    for a, b in combinations(C, 2):
        xa, xb = t3.S[a], t3.S[b]
        r *= omega[tuple((xa[k] - xb[k]) % 3 for k in range(3))]
    return r


def rate_cross(C, x, y, Cp):    # the member's crossing factor times block 95's heat-bath factor (symmetric proposals)
    return s_[x] * s_[y] / (chi[x] * chi[y]) * W(Cp) / (W(C) + W(Cp)) / 6


def rate_site(C, x, y, Cp):     # block 97: timed by the site it leaves (a = 1)
    return w[x] * W(Cp) / (W(C) + W(Cp)) / 6


okB = okS = True
confs = list(combinations(range(t3.N), 3))
for C in confs[:900]:
    for x, y, Cp in moves(t3, C):
        okB &= W(C) * rate_cross(C, x, y, Cp) == W(Cp) * rate_cross(Cp, y, x, C)
        pi = lambda D: W(D) / math.prod(w[z] for z in D)
        okS &= pi(C) * rate_site(C, x, y, Cp) == pi(Cp) * rate_site(Cp, y, x, C)
check("T1 field-blind crossing", okB and okS, "3 records on 3^3, random rational clocks w = s^2, lengths chi and even pair "
      "weight W: at the crossing factor sqrt(w_x w_y)/(chi_x chi_y), pi(C) proportional to W(C) balances every move "
      "(the fields drop out); timed by the leaving site (block 97) the law is W(C)/prod w_z instead")

# T1b: fields that follow the configuration (first order, even kernels): the forward/backward log-rate ratio vanishes
G3 = sp.zeros(27)
for i in range(27):
    G3[i, i] = 6
    for j in t3.nb[i]:
        G3[i, j] -= 1
P0 = sp.eye(27) - sp.ones(27, 27) / 27
Ginv = (G3 + sp.ones(27, 27) / 27).inv() - sp.ones(27, 27) / 27      # mean-zero inverse of the lattice Laplacian
Uk = [Fr(str(Ginv[0, j])) for j in range(27)]                        # G(0 -> j): translation-invariant, even
Fk = [Fr(2, 3 + sum(min(c, 3 - c) ** 2 for c in t3.S[j])) for j in range(27)]              # even: depends on |d| only


def kern(Kv, a, b):
    xa, xb = t3.S[a], t3.S[b]
    return Kv[t3.ix[tuple((xb[k] - xa[k]) % 3 for k in range(3))]]


def fields(C, z):
    return sum(kern(Uk, z, r) for r in C), sum(kern(Fk, z, r) for r in C)


okF = True
for C in confs[:400]:
    for x, y, Cp in moves(t3, C):
        ux, px = fields(C, x)
        uy, py = fields(C, y)
        uy2, py2 = fields(Cp, y)
        ux2, px2 = fields(Cp, x)
        fwd = (ux + uy) / 2 - (px + py)
        bwd = (uy2 + ux2) / 2 - (py2 + px2)
        okF &= fwd == bwd
check("T1b configuration-following fields", okF, "u = sum G(z - r) (the torus kernel) and phi = sum Phi(z - r) (an even kernel): "
      "at first order log k_xy(C) = log k_yx(C') for every move, so the stationary law stays W(C): no clump binds")


# ================================================================= T2: the clause is not fixed by block 60 T2's derivatives
def charges(C, wv, cv, m, mu, K=1):
    """block 110 T2(b): P = sum (e + 2 tau)/(8K chi), Q = sum e/(8K w chi); records' e, tau from the activity clause
    H = sum_{x in C} m w_x + mu sum_{bonds with one end occupied} (1/2) sqrt(w_x w_y)/(chi_x chi_y)  (mu = 0: rest only)."""
    occ = set(C)
    tau = [Fr(0)] * t3.N
    for x in range(t3.N):
        for y in t3.nb[x]:
            if (x in occ) != (y in occ):
                tau[x] += mu * Fr(1, 2) * Fr(1, 2) * cv_rate(wv, cv, x, y)   # half of the bond's term, at each end
    e = [(m * wv[x] if x in occ else Fr(0)) + tau[x] for x in range(t3.N)]
    Pc = sum((e[x] + 2 * tau[x]) / (8 * K * cv[x]) for x in range(t3.N))
    Qc = sum(e[x] / (8 * K * wv[x] * cv[x]) for x in range(t3.N))
    return Pc, Qc, e, tau


def cv_rate(wv, cv, x, y):
    return sp_sqrt(wv[x] * wv[y]) / (cv[x] * cv[y])


def sp_sqrt(q):
    r = sp.sqrt(sp.Rational(q.numerator, q.denominator))
    return Fr(str(r)) if r.is_Rational else Fr(str(sp.nsimplify(r)))


# weak fields: w = (1 - eps)^2 at the records, chi = 1 + eps' there, 1 elsewhere; rational square roots
C0 = (0, 1, 3)
eps = Fr(1, 20)
wv = [Fr(1)] * t3.N
cv = [Fr(1)] * t3.N
for z in C0:
    wv[z] = (1 - eps) ** 2
    cv[z] = 1 + eps / 2
PR, QR, _, _ = charges(C0, wv, cv, Fr(1), Fr(0))
PA, QA, eA, tA = charges(C0, wv, cv, Fr(1), Fr(1))
# homogeneity demanded by block 110 T2(e): degree 1 in the rates; the hop part degree -2 in the lengths
lam_, s2, wx, wy, cx, cy = sp.symbols("lam s w_x w_y c_x c_y", positive=True)
kap = sp.sqrt(wx * wy) / (cx * cy)
hom = (sp.simplify(kap.subs({wx: lam_ * wx, wy: lam_ * wy}) - lam_ * kap) == 0
       and sp.simplify(kap.subs({cx: s2 * cx, cy: s2 * cy}) - kap / s2 ** 2) == 0)
check("T2 two admissible clauses", PR < QR and PA > QA and hom,
      "on the same three records with clocks (1 - 1/20)^2 and lengths 1 + 1/40: rest only gives P - Q = %s < 0, the "
      "activity at the crossing factor gives P - Q = %s > 0; both energies have block 110 T2(e)'s homogeneity, so "
      "block 60 T2's derivatives do not fix a record's (e, tau)" % (PR - QR, PA - QA))


# ================================================================= T3: no record-layer virial: P/Q - 1 = 2<sum tau>/<sum e> > 0
def bond_count(t, C):   # B = number of bonds with exactly one end occupied
    occ = set(C)
    return sum(1 for x in C for y in t.nb[x] if y not in occ)


def weak_ratio(meanB, n, m, mu):   # at weak field each occupied-empty bond carries mu/2, a quarter at each end: sum tau = mu B / 2
    stau = mu * meanB / 2
    return 1 + 2 * stau / (m * n + stau)


okU = True
rows = []
for n in (2, 3):
    cs = list(combinations(range(t3.N), n))
    meanB = Fr(sum(bond_count(t3, C) for C in cs), len(cs))
    okU &= meanB == Fr(6 * n * (t3.N - n), t3.N - 1)
    rows.append("N=%d: <B> = %s, P/Q = %s" % (n, meanB, weak_ratio(meanB, n, 1, 1)))
# the clocked gas's own law (block 95 T2, timed by the leaving site): pi(C) ~ exp(6 g sum_pairs G); rational weights q^(k)
den = sp.ilcm(*[sp.Rational(str(Ginv[0, j])).q for j in range(27)])
qv = Fr(3, 2)
gas = []
for n in (2, 3):
    cs = list(combinations(range(t3.N), n))
    num = Fr(0)
    Z = Fr(0)
    for C in cs:
        ex = sum(int(sp.Rational(str(Ginv[a, b])) * den) for a, b in combinations(C, 2))
        wt = qv ** ex
        Z += wt
        num += wt * bond_count(t3, C)
    meanB = num / Z
    gas.append((n, meanB, weak_ratio(meanB, n, 1, 1)))
okG = all(r > 1 for _, _, r in gas) and all(mb < Fr(6 * n * (27 - n), 26) for n, mb, _ in gas)
check("T3 no record virial", okU and okG,
      "activity clause at weak field (m = mu = 1): uniform law " + "; ".join(rows) + "; clocked gas with q = e^(6g/%s) = 3/2: "
      % den + "; ".join("N=%d: <B> = %.4f, P/Q = %.4f" % (n, float(b), float(r)) for n, b, r in gas) +
      " -- above 1 whenever a record can move")


# ================================================================= N (float, evidence): larger clocked-gas clumps
@njit(cache=False)
def sim(G, L, lam, n, steps, seed):
    np.random.seed(seed)
    V = L * L * L
    occ = -np.ones(V, dtype=np.int64)
    pos = np.zeros((n, 3), dtype=np.int64)
    c0 = L // 2
    k = 0
    side = int(np.ceil(n ** (1 / 3)))
    for a in range(side):
        for b in range(side):
            for cc in range(side):
                if k < n:
                    x, y, z = (c0 + a) % L, (c0 + b) % L, (c0 + cc) % L
                    occ[x * L * L + y * L + z] = k
                    pos[k, 0], pos[k, 1], pos[k, 2] = x, y, z
                    k += 1
    dirs = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    sw = 0.0
    sB = 0.0
    for t in range(steps):
        logw = np.zeros(n)
        for i in range(n):
            acc = 0.0
            for j in range(n):
                acc += G[(pos[i, 0] - pos[j, 0]) % L, (pos[i, 1] - pos[j, 1]) % L, (pos[i, 2] - pos[j, 2]) % L]
            logw[i] = 6 * lam * acc
        R = np.zeros(n * 6)
        tot = 0.0
        B = 0
        for i in range(n):
            for e in range(6):
                s = ((pos[i, 0] + dirs[e, 0]) % L) * L * L + ((pos[i, 1] + dirs[e, 1]) % L) * L + (pos[i, 2] + dirs[e, 2]) % L
                if occ[s] < 0:
                    R[i * 6 + e] = math.exp(logw[i]) / 12.0
                    tot += R[i * 6 + e]
                    B += 1
        h = 1.0 / tot
        if t > steps // 5:
            sw += h
            sB += h * B
        r = np.random.random() * tot
        acc = 0.0
        for q in range(n * 6):
            acc += R[q]
            if acc >= r:
                break
        i, e = q // 6, q % 6
        s0 = pos[i, 0] * L * L + pos[i, 1] * L + pos[i, 2]
        nx, ny, nz = (pos[i, 0] + dirs[e, 0]) % L, (pos[i, 1] + dirs[e, 1]) % L, (pos[i, 2] + dirs[e, 2]) % L
        occ[s0] = -1
        occ[nx * L * L + ny * L + nz] = i
        pos[i, 0], pos[i, 1], pos[i, 2] = nx, ny, nz
    return sB / sw


def zero_mean_kernel(L):
    kk = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(kk, kk, kk, indexing="ij")
    E = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    E[0, 0, 0] = 1.0
    inv = 1.0 / E
    inv[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(inv))


L = 8
Gf = zero_mean_kernel(L)
out = []
for g in (0.0, 1.0, 3.0):
    mB = sim(Gf, L, -g, 27, 60000, 7)
    out.append("g=%.0f: <B>/N=%.2f, P/Q=%.3f" % (g, mB / 27, 1 + 2 * (mB / 2) / (27 + mB / 2)))
print("N1 (float, evidence) clocked gas on 8^3, 27 records, activity clause m = mu = 1: " + "; ".join(out))

print("time %.0f s" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL. (a) needs a new clause: block 60 T2's sources are derivatives of a content energy, and records "
      "have none; the rest-only and the crossing-factor activity energies both meet block 110 T2(e)'s homogeneity yet give "
      "P - Q of opposite signs on the same records (exact). Records that cross bonds at the member's own factor sqrt(w_x "
      "w_y)/(chi_x chi_y) are blind to the fields: pi ~ W(C) for any fixed clocks and lengths, and at first order for "
      "fields that follow the records, so no clump binds in its own field. (b) Under the activity clause, at weak field "
      "P/Q = 1 + 2<sum tau>/<sum e> with sum tau = mu <B>/2, B the occupied-empty bonds: above 1 for every law in which "
      "a record can move (uniform and clocked-gas laws exact on 3^3; 8^3 simulated): no record-layer virial. (c) P = Q at "
      "weak field needs a hop energy that vanishes with the field.")
print("HIT: a record's (e, tau) is not fixed by block 60 T2: two admissible record energies give opposite signs of P - Q "
      "on the same configuration; records crossing at the member's factor sqrt(w_x w_y)/(chi_x chi_y) have a field-blind "
      "stationary law W(C), so they cannot form a clump in their own field; and under the crossing-factor activity clause "
      "P/Q - 1 = 2<sum tau>/<sum e> > 0 at weak field for every movable record gas")
