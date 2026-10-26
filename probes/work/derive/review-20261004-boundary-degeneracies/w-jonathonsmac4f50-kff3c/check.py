#!/usr/bin/env python3
"""review-20261004-boundary-degeneracies :: the zone-centre merger u = kappa^2 = P/4 on the boundary J_z = J_x + J_y, J_x != J_y.

Supplied model (NOT an axiom): four-site Bloch matrix H(f) = i M(f) of the landed composite-site network comparator, u = +1 sector, landed hopping-sign convention.
The 18 network terms below are the embedded data of the landed boundary-census runner (read from main at 2868a0c4); P = Jx Jy, s = Jx + Jy, u = kappa^2.

What this script does (all finite claims in exact Gaussian-rational arithmetic; floats are labelled FLOAT):
  S1  EXACT symbolic in (Jx, Jy, kappa) at J_z = s: H(0) spectrum, kernel, complement block C(0); exact Laurent Schur numerator Num = detC (A - B C^-1 B^dag), Pauli
      components, exact Taylor jets with weights (x:1; y,z:4); independent jet of det H from the full 4x4 determinant; the line identity det H = 16 q(c)^2.
  S2  EXACT: at u = P/4 the jets are Num = -16 s^2 d_lead + G (G of weight >= 6), N0 of weight >= 9, d_lead = (2 Jy y - s z, P x^4/(4 s), -8 kappa y); at u != P/4
      the weight-(1;2,2) leading map d_y = (P-4u) x^2/s ... and at u = P/4 that weight-(1;2,2) jet has the whole x-axis as zero set (why quartic weights are needed).
  S3  EXACT rational: explicit isolating quasi-balls at anisotropic fixtures with u = P/4 exactly (both orders of Jx, Jy), with the complementary gap of C.
  S4  EXACT rational: a UNIFORM explicit radius along the whole curve u = P/4, J_z = s, for every ratio Jx/Jy in [1/m, m] (m = 2, 5, 10), by homogeneity (degree 3) and
      majorants of the reduced coefficient polynomials.
  S5  EXACT: the nonisolated set just above the merger: for u > P/4 the line pair cos x0 = P/(2u) - 1 has x0 -> 0 (so no radius survives u -> P/4+).
  S6  FLOAT diagnostics: numpy Bloch matrix vs the exact Laurent objects, middle gap on the certified ball, Fukui Chern number of the two lowest bands on a certified
      quasi-sphere (expected 0).
Runtime: well under 10 minutes, one process.
"""
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import random
from fractions import Fraction as Fr
from math import factorial

import numpy as np
import sympy as sp
from sympy import QQ_I
from sympy.polys.rings import ring

T0 = time.time()
PASS = 0
FAIL = 0
HITS = []


def check(ok, label, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + detail) if detail else ""), flush=True)


# ------------------------------------------------------------------------------------------------ network data (embedded, from the landed census runner)
TERMS = [(0, 1, (-1, 0, 0), "y"), (0, 1, (0, 0, 0), "x"), (0, 3, (0, 0, -1), "z"), (1, 1, (-1, 0, 0), "odd"), (1, 3, (1, 0, -1), "odd"),
         (3, 1, (0, 0, 1), "odd"), (0, 0, (1, 0, 0), "odd"), (0, 2, (-1, 0, 0), "odd"), (2, 0, (0, 0, 0), "odd"), (2, 3, (0, -1, 0), "y"),
         (2, 3, (0, 0, 0), "x"), (2, 1, (0, 0, 0), "z"), (3, 3, (0, -1, 0), "odd"), (3, 1, (0, 1, 0), "odd"), (1, 3, (0, 0, 0), "odd"),
         (2, 2, (0, 1, 0), "odd"), (2, 0, (0, -1, 1), "odd"), (0, 2, (0, 0, -1), "odd")]
# theta = 2 pi f = x (1,-1,0) + y (1,1,0) + z (0,0,1): theta1 = x + y, theta2 = y - x, theta3 = z.  Mode m: m.theta = (m1-m2) x + (m1+m2) y + m3 z.
WTS = (1, 4, 4)      # weights of x, y, z for the u = P/4 jets
NT = 12              # Taylor degree (total degree in x,y,z)

R, Jx, Jy, kk = ring("Jx,Jy,k", QQ_I)
ONE = R(1)
IU = QQ_I(0, 1)
HALF = QQ_I(1, 0) / 2


def fr(v):
    return Fr(int(v.numerator), int(v.denominator))


def cabs(c):
    """|Re| + |Im| of a Gaussian rational (upper bound of the modulus), as Fraction."""
    return abs(fr(c.x)) + abs(fr(c.y))


# ---------------- Laurent polynomials in z1,z2,z3 with coefficients in R: dict {(m1,m2,m3): R-element}
def lcl(d):
    return {m: c for m, c in d.items() if c}


def ladd(a, b, sgn=1):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, R(0)) + sgn * c
    return lcl(out)


def lmul(a, b):
    out = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = (m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2])
            out[m] = out.get(m, R(0)) + c1 * c2
    return lcl(out)


def lscale(a, c):
    return lcl({m: v * c for m, v in a.items()})


def conjc(p):
    return R.from_dict({mon: QQ_I(c.x, -c.y) for mon, c in p.items()}) if p else p


def lconj(a):
    return {(-m[0], -m[1], -m[2]): conjc(c) for m, c in a.items()}


def build_H(Jz_expr):
    amp = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz_expr, "odd": 2 * kk}
    H = [[{} for _ in range(4)] for _ in range(4)]
    for a, b, n, kd in TERMS:
        # M[a,b] += amp z^n, M[b,a] -= amp z^-n; H = i M
        H[a][b] = ladd(H[a][b], {n: IU * amp[kd]})
        nn = (-n[0], -n[1], -n[2])
        H[b][a] = ladd(H[b][a], {nn: -IU * amp[kd]})
    return H


def schur(H):
    Kv = [[1, 0, -1, 0], [0, 1, 0, -1]]
    Cv = [[1, 0, 1, 0], [0, 1, 0, 1]]

    def blk(u, v):
        out = [[{} for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                acc = {}
                for a in range(4):
                    for b in range(4):
                        co = u[i][a] * v[j][b]
                        if co and H[a][b]:
                            acc = ladd(acc, lscale(H[a][b], HALF * co))
                out[i][j] = acc
        return out
    A, B, C = blk(Kv, Kv), blk(Kv, Cv), blk(Cv, Cv)
    detC = ladd(lmul(C[0][0], C[1][1]), lmul(C[0][1], C[1][0]), -1)
    adj = [[C[1][1], lscale(C[0][1], R(-1))], [lscale(C[1][0], R(-1)), C[0][0]]]
    Bd = [[lconj(B[j][i]) for j in range(2)] for i in range(2)]

    def mm(X, Y):
        return [[ladd(lmul(X[i][0], Y[0][j]), lmul(X[i][1], Y[1][j])) for j in range(2)] for i in range(2)]
    BAB = mm(mm(B, adj), Bd)
    Num = [[ladd(lmul(detC, A[i][j]), BAB[i][j], -1) for j in range(2)] for i in range(2)]
    N0 = lscale(ladd(Num[0][0], Num[1][1]), HALF)
    Nz = lscale(ladd(Num[0][0], Num[1][1], -1), HALF)
    Nx = lscale(ladd(Num[0][1], Num[1][0]), HALF)
    Ny = lscale(ladd(Num[1][0], Num[0][1], -1), QQ_I(0, -1) * HALF)
    return {"A": A, "B": B, "C": C, "detC": detC, "Num": Num, "Nx": Nx, "Ny": Ny, "Nz": Nz, "N0": N0}


def ldet4(H):
    """Leibniz determinant of the 4x4 Laurent matrix."""
    from itertools import permutations
    tot = {}
    for perm in permutations(range(4)):
        sgn = 1
        p = list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if p[i] > p[j]:
                    sgn = -sgn
        term = {(0, 0, 0): ONE}
        for i in range(4):
            if not H[i][p[i]]:
                term = {}
                break
            term = lmul(term, H[i][p[i]])
        tot = ladd(tot, term, sgn)
    return tot


def taylor(Lc, nmax=NT):
    """Exact Taylor coefficients of sum_m c_m exp(i m.theta) in (x,y,z): dict (i,j,l) -> R-element, total degree <= nmax."""
    out = {}
    pw = {}
    for (m1, m2, m3), c in Lc.items():
        a, b, d = m1 - m2, m1 + m2, m3
        for n in range(nmax + 1):
            ph = [QQ_I(1, 0), QQ_I(0, 1), QQ_I(-1, 0), QQ_I(0, -1)][n % 4]
            for i in range(n + 1):
                for j in range(n - i + 1):
                    l = n - i - j
                    f = Fr(1, factorial(i) * factorial(j) * factorial(l)) * (a ** i) * (b ** j) * (d ** l)
                    if f == 0:
                        continue
                    key = (i, j, l)
                    out[key] = out.get(key, R(0)) + c * ph * (QQ_I(f.numerator, 0) / QQ_I(f.denominator, 0))
    return {k_: v for k_, v in out.items() if v}


def wt(key):
    return key[0] * WTS[0] + key[1] * WTS[1] + key[2] * WTS[2]


def isreal_poly(p):
    return all(c.y == 0 for c in p.values())


def mod_rel(p):
    """Reduce kappa^2 -> P/4 = Jx Jy/4 in an R element: result has k-degree <= 1."""
    out = R(0)
    for (a, b, l), c in p.items():
        q, r_ = divmod(l, 2)
        out += R.from_dict({(a + q, b + q, r_): c / QQ_I(4 ** q, 0)})
    return out


def evalR(p, vals):
    """Evaluate an R element at (Jx, Jy, k) = vals (Fractions): returns (re, im) Fractions."""
    re_, im_ = Fr(0), Fr(0)
    for (a, b, l), c in p.items():
        mon = vals[0] ** a * vals[1] ** b * vals[2] ** l
        re_ += fr(c.x) * mon
        im_ += fr(c.y) * mon
    return re_, im_


def absR(p, vals):
    """Upper bound of |p| at nonnegative bound values vals: sum |coefficient| * monomial."""
    t = Fr(0)
    for (a, b, l), c in p.items():
        t += cabs(c) * vals[0] ** a * vals[1] ** b * vals[2] ** l
    return t


# ================================================================================================ S1: exact symbolic structure at J_z = s
print("== S1/S2 exact symbolic jets at J_z = Jx + Jy (weights x:1; y,z:4)", flush=True)
Jz_s = Jx + Jy
H = build_H(Jz_s)
herm = all(H[i][j] == lconj(H[j][i]) for i in range(4) for j in range(4))
check(herm, "S1.0 Bloch matrix H is Hermitian as an exact Laurent matrix (symbolic Jx,Jy,k)")

# H(0)
H0 = sp.zeros(4, 4)
Jxs, Jys, ks = sp.symbols("Jx Jy k", positive=True)
for i in range(4):
    for j in range(4):
        tot = R(0)
        for m, c in H[i][j].items():
            tot = tot + c
        H0[i, j] = sp.sympify(tot.as_expr())
lam = sp.Symbol("lam")
cp = sp.factor((H0 - lam * sp.eye(4)).det())
s_ = sp.Symbol("Jx") + sp.Symbol("Jy")
check(sp.simplify(cp - lam ** 2 * (lam ** 2 - 16 * s_ ** 2)) == 0, "S1.1 charpoly of H(0) at J_z = s is lam^2 (lam^2 - 16 s^2): spectrum {0,0,+-4s}, no kappa dependence",
      str(cp))
Kv = sp.Matrix([[1, 0], [0, 1], [-1, 0], [0, -1]])
check(sp.simplify(H0 * Kv) == sp.zeros(4, 2), "S1.2 ker H(0) = span{(1,0,-1,0),(0,1,0,-1)} exactly (all couplings)")

S = schur(H)
# C(0) eigenvalues
C0 = sp.Matrix(2, 2, lambda i, j: sp.sympify(sum((c for c in S["C"][i][j].values()), R(0)).as_expr()))
ev = sorted([sp.simplify(e) for e in C0.eigenvals().keys()], key=str)
check(sp.simplify(C0.charpoly(lam).as_expr() - (lam ** 2 - 16 * s_ ** 2)) == 0, "S1.3 complement block C(0) has eigenvalues +-4s (gap 4s, kappa-independent)", str(ev))

# Pauli reality, jets
TC = {}
for nm in ("Nx", "Ny", "Nz", "N0"):
    TC[nm] = taylor(S[nm])
real_ok = all(isreal_poly(v) for nm in TC for v in TC[nm].values())
check(real_ok, "S1.4 all Taylor coefficients of the Pauli components Nx,Ny,Nz,N0 are real (Num is Hermitian-valued)")
TCd = taylor(S["detC"])
check(isreal_poly(TCd.get((0, 0, 0), R(0))) and TCd[(0, 0, 0)] == -16 * (Jx + Jy) ** 2, "S1.5 detC(0) = -16 s^2 exactly = -E2 (E2 = 16 J_z^2)")

# generic-kappa jets in weights (1;4,4): list the lowest weights
def lowest(nm, wmax):
    return {k_: v for k_, v in TC[nm].items() if wt(k_) < wmax}


E2 = 16 * (Jx + Jy) ** 2
# (a) generic kappa: nonzero Taylor monomials of weight < 4
low_all = {nm: lowest(nm, 4) for nm in TC}
expect_Ny_x2 = 16 * (Jx + Jy) * (4 * kk ** 2 - Jx * Jy)
check(set(low_all["Nx"]) == set() and set(low_all["Nz"]) == set() and set(low_all["N0"]) == set()
      and set(low_all["Ny"]) == {(2, 0, 0)} and low_all["Ny"][(2, 0, 0)] == expect_Ny_x2,
      "S2.1 generic kappa: below weight 4 the only Pauli jet term is N_y = 16 s (4 kappa^2 - P) x^2 (so N_y x^2 coefficient vanishes exactly on u = P/4)")
# (b) weight-4 part, exact, generic kappa
w4 = {nm: {k_: v for k_, v in TC[nm].items() if wt(k_) == 4} for nm in TC}
exp_w4 = {"Nx": {(0, 1, 0): -32 * (Jx + Jy) ** 2 * Jy, (0, 0, 1): 16 * (Jx + Jy) ** 3},
          "Nz": {(0, 1, 0): 128 * kk * (Jx + Jy) ** 2},
          "N0": {}}
okw4 = (w4["Nx"] == exp_w4["Nx"] and w4["Nz"] == exp_w4["Nz"] and w4["N0"] == {})
check(okw4, "S2.2 weight-4 jet: N_x = -16 s^2 (2 Jy y - s z), N_z = 128 kappa s^2 y; N_0 has no weight-4 term (exact, symbolic, any kappa)")
# N_y weight 4, exact
ny4 = w4["Ny"]
check(set(ny4) == {(4, 0, 0)}, "S2.3a N_y weight-4 part is the single monomial x^4")
c4 = ny4[(4, 0, 0)]
expect_c4 = -QQ_I(4, 0) / 3 * (-Jx ** 2 * Jy - 4 * Jx * Jy ** 2 + 16 * Jx * kk ** 2 + 28 * Jy * kk ** 2)
check(c4 == expect_c4, "S2.3b N_y x^4 coefficient = -(4/3)(-Jx^2 Jy - 4 Jx Jy^2 + 16 Jx k^2 + 28 Jy k^2) for all couplings")
c4red = mod_rel(c4)
check(c4red == -QQ_I(4, 0) * (Jx * Jy) * (Jx + Jy), "S2.3c on u = P/4 the x^4 coefficient reduces to -4 P s (so N_y = -16 s^2 * [P/(4 s)] x^4 = -E2 d_y)")

# (c) at u = P/4: all weight < 6 Taylor terms (degree <= 12) after the relation
red = {nm: {k_: mod_rel(v) for k_, v in TC[nm].items()} for nm in TC}
red = {nm: {k_: v for k_, v in red[nm].items() if v} for nm in red}
lead = {"Nx": {(0, 1, 0): -32 * (Jx + Jy) ** 2 * Jy, (0, 0, 1): 16 * (Jx + Jy) ** 3},
        "Ny": {(4, 0, 0): -QQ_I(4, 0) * Jx * Jy * (Jx + Jy)},
        "Nz": {(0, 1, 0): 128 * kk * (Jx + Jy) ** 2}}
ok6 = True
for nm in ("Nx", "Ny", "Nz"):
    low = {k_: v for k_, v in red[nm].items() if wt(k_) < 6}
    ok6 = ok6 and (low == {k_: mod_rel(v) for k_, v in lead[nm].items()})
check(ok6, "S2.4 u = P/4: N = -16 s^2 d_lead + G with d_lead = (2 Jy y - s z, P x^4/(4s), -8 kappa y) and G of weight >= 6 (all monomials of total degree <= 12; exact)")
n0low = {k_ for k_ in red["N0"] if wt(k_) < 9}
check(n0low == set(), "S2.5 N_0 has weight >= 9 (no monomial of weight < 9 up to total degree 12), exact, symbolic",
      "lowest: " + str(sorted(wt(k_) for k_ in red["N0"])[:3]))
n0_9 = {k_: v for k_, v in TC["N0"].items() if wt(k_) == 9}
check(set(n0_9) == {(1, 0, 2), (1, 1, 1)}, "S2.6a N_0 weight-9 part is supported on x z^2 and x y z")
check(n0_9[(1, 0, 2)] == 8 * kk * (Jx + Jy) ** 2 and n0_9[(1, 1, 1)] == 16 * kk * (Jx + Jy) * Jy,
      "S2.6b N_0 weight 9 = 8 kappa s x z (s z + 2 Jy y), exact symbolic (no relation needed)")

# (d) weights (1;2,2) at u = P/4: the leading jet has the x-axis as zero set; the x^4 term is invisible
red22 = {nm: {k_: mod_rel(v) for k_, v in TC[nm].items()} for nm in ("Nx", "Ny", "Nz")}
w22 = lambda key: key[0] + 2 * (key[1] + key[2])
low22 = {nm: {k_: v for k_, v in red22[nm].items() if v and w22(k_) <= 2} for nm in red22}
check(low22["Ny"] == {} and low22["Nx"] == {(0, 1, 0): lead["Nx"][(0, 1, 0)], (0, 0, 1): lead["Nx"][(0, 0, 1)]} and low22["Nz"] == {(0, 1, 0): lead["Nz"][(0, 1, 0)]},
      "S2.7 weights (1;2,2) at u = P/4: leading jet has N_y == 0, so it vanishes on the whole x-axis (y=z=0): the generic-u ball method (d_y = a x^2, a=(P-4u)/s) does not apply")

# (e) detH jet from the independent full 4x4 determinant
dH = ldet4(H)
TCh = taylor(dH)
check(all(isreal_poly(v) for v in TCh.values()), "S2.8a det H (Leibniz 4x4 Laurent determinant) has real Taylor coefficients")
redh = {k_: mod_rel(v) for k_, v in TCh.items()}
redh = {k_: v for k_, v in redh.items() if v}
low_h = {k_: v for k_, v in redh.items() if wt(k_) < 8}
check(low_h == {}, "S2.8b u = P/4: det H has no Taylor monomial of weight < 8 (degree <= 12): fourth order in the weight-4 sense")
# 16 s^2 |d_lead|^2 with d = (2Jy y - s z, P x^4/(4s), -8k y):  s^2 * 16 * [ (2Jy y - s z)^2 + (P x^4/(4 s))^2 + 64 k^2 y^2 ]
# expressed polynomially: 16 s^2 (2Jy y - s z)^2 + P^2 x^8 + 1024 k^2 s^2 y^2
w8 = {k_: v for k_, v in redh.items() if wt(k_) == 8}
expect_w8 = {}
def addm(dd, key, val):
    dd[key] = dd.get(key, R(0)) + val
addm(expect_w8, (0, 2, 0), 16 * (Jx + Jy) ** 2 * 4 * Jy ** 2)
addm(expect_w8, (0, 1, 1), 16 * (Jx + Jy) ** 2 * (-4) * Jy * (Jx + Jy))
addm(expect_w8, (0, 0, 2), 16 * (Jx + Jy) ** 2 * (Jx + Jy) ** 2)
addm(expect_w8, (8, 0, 0), (Jx * Jy) ** 2)
addm(expect_w8, (0, 2, 0), 1024 * mod_rel(kk ** 2) * (Jx + Jy) ** 2)
expect_w8 = {k_: mod_rel(v) for k_, v in expect_w8.items()}
expect_w8 = {k_: v for k_, v in expect_w8.items() if v}
# the x^8 coefficient: det H = (N0^2 - |N|^2)/detC ~ E2 |d_lead|^2 with N_y = -E2 d_y -> E2 * (P/(4s))^2 x^8 * ... compare numerically below instead of assuming
match = (set(w8) == set(expect_w8)) and all(w8[k_] == expect_w8[k_] for k_ in w8)
check(match, "S2.8c u = P/4: weight-8 jet of det H equals 16 s^2 |d_lead|^2 (exact, from the full 4x4 determinant)",
      "" if match else str({k_: (w8.get(k_), expect_w8.get(k_)) for k_ in set(w8) | set(expect_w8) if w8.get(k_) != expect_w8.get(k_)}))

# (f) line identity at u = P/4: det H on f = (x_f, 1-x_f, 0): theta = x (1,-1,0), det H = 16 q(c)^2 with q = 4u c^2 - 2Pc - S - 4u; at J_z = s, u = P/4: q = P (c-1)^2
cc = sp.Symbol("c")
Pq = Jxs * Jys
Sq = Jxs ** 2 + Jys ** 2 - (Jxs + Jys) ** 2
q_gen = 4 * ks ** 2 * cc ** 2 - 2 * Pq * cc - Sq - 4 * ks ** 2
q_fact = sp.factor(q_gen)
check(sp.simplify(q_gen - (cc - 1) * (4 * ks ** 2 * (cc + 1) - 2 * Pq)) == 0, "S2.9a on J_z = s: q(c) = (c-1)(4u(c+1) - 2P) (landed identity re-derived)")
q_Pq4 = sp.simplify(q_gen.subs(ks, sp.sqrt(Pq) / 2))
check(sp.simplify(q_Pq4 - Pq * (cc - 1) ** 2) == 0, "S2.9b at u = P/4: q = P (c-1)^2, a double root at c = 1 (Gamma): det H = 16 P^2 (1 - cos x)^4 on the line, order x^8")
# verify det H on the line theta = x(1,-1,0) (t = e^{ix}: z1 = t, z2 = 1/t, z3 = 1) from the exact Laurent determinant, as Laurent polynomials in t over R
def line_restrict(Lc):
    out = {}
    for m, c in Lc.items():
        out[m[0] - m[1]] = out.get(m[0] - m[1], R(0)) + c
    return {n: v for n, v in out.items() if v}


def tmul(a, b):
    out = {}
    for n1, c1 in a.items():
        for n2, c2 in b.items():
            out[n1 + n2] = out.get(n1 + n2, R(0)) + c1 * c2
    return {n: v for n, v in out.items() if v}


dHl = line_restrict(dH)
# c = (t + 1/t)/2 ;  q = (c-1)(4k^2 (c+1) - 2P)
cm1 = {1: R(1) * QQ_I(1, 0) / 2, -1: R(1) * QQ_I(1, 0) / 2, 0: R(-1)}
cp1 = {1: R(1) * QQ_I(1, 0) / 2, -1: R(1) * QQ_I(1, 0) / 2, 0: R(1)}
fac2 = {n: 4 * kk ** 2 * v for n, v in cp1.items()}
fac2[0] = fac2.get(0, R(0)) - 2 * Jx * Jy
q_t = tmul(cm1, {n: v for n, v in fac2.items() if v})
target_t = {n: 16 * v for n, v in tmul(q_t, q_t).items()}
check(dHl == target_t, "S2.9c exact (symbolic Jx,Jy,k, any kappa): det H(x(1,-1,0)) from the full 4x4 Laurent determinant = 16 q(c)^2, q = (c-1)(4k^2 (c+1) - 2 Jx Jy) at J_z = s (landed line identity re-derived)")
red_dHl = {n: mod_rel(v) for n, v in dHl.items()}
tgt_P = tmul({1: R(1) * QQ_I(1, 0), -1: R(1) * QQ_I(1, 0), 0: R(-2)}, {1: R(1) * QQ_I(1, 0), -1: R(1) * QQ_I(1, 0), 0: R(-2)})
tgt_P = tmul(tgt_P, tgt_P)           # (t + 1/t - 2)^4 = (2c-2)^4 = 16 (c-1)^4
tgt_P = {n: (Jx * Jy) ** 2 * v for n, v in tgt_P.items()}
tgt_P = {n: mod_rel(v) for n, v in tgt_P.items()}
check({n: v for n, v in red_dHl.items() if v} == {n: v for n, v in tgt_P.items() if v},
      "S2.9d exact: at u = P/4 that equals P^2 (t + 1/t - 2)^4 = 16 P^2 (1 - cos x)^4 (a zero of order 8 in x along the axis, Gamma the only zero on the axis)")

# ================================================================================================ ball machinery (exact rational)
def laurent_numeric(Lc, vals):
    """Numeric Laurent: dict m -> (re,im) Fractions."""
    out = {}
    for m, c in Lc.items():
        out[m] = evalR(c, vals)
    return out


def mu(m):
    return abs(m[0] - m[1]) + abs(m[0] + m[1]) + abs(m[2])


def lagrange_const(Lc, vals):
    tot = Fr(0)
    for m, c in Lc.items():
        re_, im_ = evalR(c, vals)
        tot += (abs(re_) + abs(im_)) * Fr(mu(m) ** (NT + 1), factorial(NT + 1))
    return tot


def lagrange_const_major(Lc, vals):
    tot = Fr(0)
    for m, c in Lc.items():
        tot += absR(c, vals) * Fr(mu(m) ** (NT + 1), factorial(NT + 1))
    return tot


def tail_const(tc_funcs, wmin, rho, lag):
    """K with |X - (Taylor terms of weight < wmin)| <= K r^wmin for 0 < r <= rho <= 1.  tc_funcs: dict key->|coef| (Fractions)."""
    tot = Fr(0)
    for key, a in tc_funcs.items():
        w = wt(key)
        if w >= wmin:
            tot += a * rho ** (w - wmin)
    return tot + lag * rho ** (NT + 1 - wmin)


def make_vals_exact(Tcs, vals):
    """exact evaluation of taylor coefficient dict at vals -> real Fractions (assert imaginary part 0)."""
    out = {}
    for key, p in Tcs.items():
        re_, im_ = evalR(p, vals)
        assert im_ == 0, "imaginary Taylor coefficient"
        if re_ != 0:
            out[key] = re_
    return out


def lam_lower(a_c, b, p, e):
    """exact lower bound lambda with |d_lead|^2 >= lambda r^8, d_lead = (a_c y - b z, p x^4, -e y)."""
    cands = [p * p, e * e]
    cands.append(b * b * e * e / (a_c * a_c + e * e))
    return min(cands)


def ball_certificate(name, Jx_v, Jy_v, k_v, rho_candidates):
    """Return dict with the largest passing rho in rho_candidates (exact rational conditions) or None."""
    vals = (Jx_v, Jy_v, k_v)
    s_v = Jx_v + Jy_v
    P_v = Jx_v * Jy_v
    assert k_v * k_v * 4 == P_v, "not on u = P/4"
    E2_v = 16 * s_v * s_v
    # exact numeric Taylor coefficients (Pauli comps and N0), identities S2.4/S2.5 already proved symbolically; re-verify numerically
    tcn = {nm: make_vals_exact(TC[nm], vals) for nm in TC}
    lead_v = {"Nx": {(0, 1, 0): -E2_v * 2 * Jy_v, (0, 0, 1): E2_v * s_v},
              "Ny": {(4, 0, 0): -E2_v * P_v / (4 * s_v)},
              "Nz": {(0, 1, 0): E2_v * 8 * k_v}}
    ok_lead = all({k_: v for k_, v in tcn[nm].items() if wt(k_) < 6} == lead_v[nm] for nm in lead_v)
    ok_n0 = all(wt(k_) >= 9 for k_ in tcn["N0"])
    # Lagrange constants on the exact Laurent polynomials
    lag = {nm: lagrange_const(S[nm], vals) for nm in ("Nx", "Ny", "Nz", "N0")}
    # leading map data (E2 d_lead):  d_lead = (2Jy y - s z, P x^4/(4 s), -8 k y)
    a_c, b_, p_, e_ = 2 * Jy_v, s_v, P_v / (4 * s_v), 8 * k_v
    lam_ = lam_lower(a_c, b_, p_, e_)
    # complementary block: |C(theta) - C(0)|_F <= r * sum |c_m| mu_m  over entries (|e^{i phi}-1| <= |phi|)
    KC = Fr(0)
    for i in range(2):
        for j in range(2):
            for m, c in S["C"][i][j].items():
                if m == (0, 0, 0) and False:
                    continue
                re_, im_ = evalR(c, vals)
                KC += (abs(re_) + abs(im_)) * mu(m)
    best = None
    for rho in rho_candidates:
        KG = Fr(0)
        for nm in ("Nx", "Ny", "Nz"):
            tcabs = {k_: abs(v) for k_, v in tcn[nm].items()}
            KG += tail_const(tcabs, 6, rho, lag[nm])
        tc0 = {k_: abs(v) for k_, v in tcn["N0"].items()}
        K0 = tail_const(tc0, 9, rho, lag["N0"])
        gap = 4 * s_v - KC * rho                            # lower bound of |eigenvalues of C| (Weyl)
        # |d_lead| >= sqrt(lam) r^4  =>  use lam_ with squares: need  (E2^2 lam) > (KG rho^2 + K0 rho^5)^2 ... implement as linear inequality via squaring
        # (C): K0 r^9 < |N| with |N| >= E2 sqrt(lam) r^4 - KG r^6.  Want  KG rho^2 + K0 rho^5 < E2 sqrt(lam).
        lhs = KG * rho ** 2 + K0 * rho ** 5
        ok_ball = (lhs * lhs < E2_v * E2_v * lam_) and gap > 0 and rho <= 1
        if ok_ball and ok_lead and ok_n0:
            best = {"rho": rho, "KG": KG, "K0": K0, "KC": KC, "gap": gap, "lam": lam_, "lhs": lhs, "E2": E2_v}
            break
    return best, ok_lead, ok_n0


# ================================================================================================ S3: fixtures
print("== S3 explicit isolating quasi-balls at u = P/4 fixtures", flush=True)
cands = [Fr(n, 1000) for n in range(1000, 0, -1)]
FIX = {
    "F1 (9/5,1/5,2;3/10)": (Fr(9, 5), Fr(1, 5), Fr(3, 10)),
    "F1' (1/5,9/5,2;3/10)": (Fr(1, 5), Fr(9, 5), Fr(3, 10)),
    "F2 (2,1/2,5/2;1/2)": (Fr(2), Fr(1, 2), Fr(1, 2)),
    "F2' (1/2,2,5/2;1/2)": (Fr(1, 2), Fr(2), Fr(1, 2)),
    "F3 (4,1,5;1)": (Fr(4), Fr(1), Fr(1)),
    "F4 (1,1,2;1/2) equal in-plane control": (Fr(1), Fr(1), Fr(1, 2)),
}
FIXRES = {}
for nm, (a_, b_, k_v) in FIX.items():
    res, ok_lead, ok_n0 = ball_certificate(nm, a_, b_, k_v, cands)
    FIXRES[nm] = res
    check(ok_lead and ok_n0, "S3.%s jets at this coupling equal the symbolic ones (weight<6 = -E2 d_lead; N0 weight>=9)" % nm.split()[0])
    check(res is not None, "S3.%s explicit radius: det C<0 (complement gap), no zero of Num, |N0|<|N|, so Gamma is the unique zero of det H in the quasi-ball" % nm.split()[0],
          ("rho = %s (x <= rho, |y|,|z| <= rho^4), C gap >= %s of 4s = %s, K_G = %s, K_0 = %s, lam = %s" % (
              res["rho"], float(res["gap"]), 4 * (a_ + b_), float(res["KG"]), float(res["K0"]), res["lam"])) if res else "no radius in grid")

# ================================================================================================ S4: uniform radius along the curve
print("== S4 uniform explicit radius along u = P/4, J_z = s (ratio Jx/Jy in [1/m, m])", flush=True)
# homogeneity: every Pauli Taylor coefficient and every Laurent coefficient is homogeneous of degree 3 in (Jx,Jy,k) (Num), degree 1 for C
def homog_deg(p):
    ds = {a + b + l for (a, b, l) in p.keys()}
    return ds


hd_num = set()
for nm in ("Nx", "Ny", "Nz", "N0"):
    for m, c in S[nm].items():
        hd_num |= homog_deg(c)
hd_C = set()
for i in range(2):
    for j in range(2):
        for m, c in S["C"][i][j].items():
            hd_C |= homog_deg(c)
check(hd_num == {3} and hd_C == {1}, "S4.0 homogeneity (exact): every coefficient of Num is of degree exactly 3 and of C of degree exactly 1 in (Jx,Jy,kappa); H(lambda J) = lambda H, so the sign pattern and zero set depend only on the ratio Jx:Jy:kappa")

red_lau = {nm: {m: mod_rel(c) for m, c in S[nm].items()} for nm in ("Nx", "Ny", "Nz", "N0")}
red_tc = {nm: {k_: v for k_, v in red[nm].items()} for nm in ("Nx", "Ny", "Nz", "N0")}


def family_certificate(m_ratio, cand):
    """s = 1, Jx in [a0, 1-a0], a0 = 1/(1+m): majorant evaluation at Jx=Jy=1, k=1/4  (all |monomials| <= bounds)."""
    a0 = Fr(1, 1 + m_ratio)
    P0 = a0 * (1 - a0)
    bound = (Fr(1), Fr(1), Fr(1, 4))
    E2_v = Fr(16)
    # majorants of Taylor coefficients (reduced polynomials c0 + c1 k)
    tcm = {nm: {k_: absR(v, bound) for k_, v in red_tc[nm].items()} for nm in red_tc}
    lagm = {nm: Fr(0) for nm in red_lau}
    for nm in red_lau:
        t = Fr(0)
        for m, c in red_lau[nm].items():
            t += absR(c, bound) * Fr(mu(m) ** (NT + 1), factorial(NT + 1))
        lagm[nm] = t
    KC = Fr(0)
    for i in range(2):
        for j in range(2):
            for m, c in S["C"][i][j].items():
                KC += absR(c, bound) * mu(m)
    # leading map lower bound over the family: p = P/4 >= P0/4, e^2 = 16 P >= 16 P0, a_c = 2 Jy <= 2 (b=1)
    p_lo, e2_lo = P0 / 4, 16 * P0
    lam_ = min(p_lo * p_lo, e2_lo, e2_lo / (4 + e2_lo))
    for rho in cand:
        KG = sum((tail_const({k_: v for k_, v in tcm[nm].items()}, 6, rho, lagm[nm]) for nm in ("Nx", "Ny", "Nz")), Fr(0))
        K0 = tail_const(tcm["N0"], 9, rho, lagm["N0"])
        lhs = KG * rho ** 2 + K0 * rho ** 5
        gap = 4 - KC * rho
        if lhs * lhs < E2_v * E2_v * lam_ and gap > 0:
            return {"rho": rho, "KG": KG, "K0": K0, "KC": KC, "gap": gap, "lam": lam_, "a0": a0}
    return None


FAMRES = {}
cands_f = [Fr(n, 20000) for n in range(20000, 0, -1)]
cands_f = [c_ for c_ in cands_f if c_ == Fr(c_.numerator, c_.denominator)]
for m_ in (2, 5, 10):
    t1 = time.time()
    res = family_certificate(m_, [Fr(n, 2000) for n in range(2000, 0, -1)] + [Fr(n, 200000) for n in range(1999, 0, -1)])
    FAMRES[m_] = res
    check(res is not None, "S4.m=%d uniform radius for every (Jx,Jy) with s=1, Jx/Jy in [1/%d,%d], kappa=sqrt(P)/2, J_z = s" % (m_, m_, m_),
          ("rho = %s ~ %.5f; gap of C >= %.4f (of 4); lam >= %.3e; K_G=%.3e K_0=%.3e [%.0fs]" % (res["rho"], float(res["rho"]), float(res["gap"]), float(res["lam"]),
           float(res["KG"]), float(res["K0"]), time.time() - t1)) if res else "none")

# ================================================================================================ S5: the nonisolated set just above the merger
print("== S5 the nonisolated set for u slightly above P/4 (exact)", flush=True)
# line zero of q: c2 = P/(2u) - 1 in (-1,1) iff u > P/4; x0 = arccos(c2) -> 0 as u -> P/4+.  Check with the exact Laurent determinant that det H vanishes there (u = P(1+d)/4).
Ps, us = sp.symbols("P u", positive=True)
check(dHl == target_t, "S5.1 exact (symbolic): det H on the axis (1,-1,0) is 16 [(c-1)(4u(c+1) - 2P)]^2 at J_z = s, so besides c=1 (Gamma) the axis zero is c2 = P/(2u) - 1, in (-1,1) iff u > P/4")
# explicit: for u = P(1+d)/4 the zero lies at x0 with 1 - cos x0 = 2 d/(1+d)  (c2 = P/(2u) - 1 = 2/(1+d) - 1)
ok_x0 = True
for dnum in (Fr(1, 10), Fr(1, 100), Fr(1, 10000), Fr(1, 1000000)):
    # c2 = 2/(1+d)-1 = (1-d)/(1+d);  1-c2 = 2d/(1+d)
    c2 = (1 - dnum) / (1 + dnum)
    ok_x0 = ok_x0 and (1 - c2 == 2 * dnum / (1 + dnum)) and (c2 < 1) and (c2 > -1)
check(ok_x0, "S5.2 for u = (1+d) P/4, d>0, the line zero cos x0 = (1-d)/(1+d) exists in (-1,1), 1 - cos x0 = 2d/(1+d) -> 0: x0 ~ 2 sqrt(d) as d -> 0+ (so every punctured quasi-ball of radius rho contains a pair of other zeros once 2 sqrt(d) < rho: the isolating radius cannot be uniform in u -> P/4+)")
# check the pair is a zero of the true Bloch matrix at an irrational-free rational point of the family: pick d with (1-d)/(1+d) = cos x0, use mpmath to evaluate smallest |eig| at x0 (FLOAT diagnostic)
import mpmath as mp
mp.mp.dps = 40


def bloch_numeric(Jx_v, Jy_v, Jz_v, k_v, f):
    """numpy-free exact-ish Bloch matrix via mpmath from TERMS (f = (f1,f2,f3))."""
    amp = {"x": 2 * Jx_v, "y": 2 * Jy_v, "z": 2 * Jz_v, "odd": 2 * k_v}
    M = mp.zeros(4, 4)
    for a, b, n, kd in TERMS:
        ph = mp.e ** (2j * mp.pi * (n[0] * f[0] + n[1] * f[1] + n[2] * f[2]))
        M[a, b] += amp[kd] * ph
        M[b, a] -= amp[kd] * mp.conj(ph)
    return 1j * M


Jxv, Jyv = mp.mpf(9) / 5, mp.mpf(1) / 5
Pv = Jxv * Jyv
dd = mp.mpf(1) / 100
kv = mp.sqrt(Pv * (1 + dd)) / 2
c2v = (1 - dd) / (1 + dd)
x0 = mp.acos(c2v)
fl = (x0 / (2 * mp.pi), 1 - x0 / (2 * mp.pi), 0)
Hn = bloch_numeric(Jxv, Jyv, Jxv + Jyv, kv, fl)
evs = sorted([abs(e) for e in mp.eigh(Hn, eigvals_only=True)])
check(evs[0] < mp.mpf(10) ** -30 and evs[1] < mp.mpf(10) ** -30, "S5.3 (40-digit) at (9/5,1/5,2), u = 1.01 P/4: the line point x0 = arccos((1-d)/(1+d)) has two zero levels: a touching inside radius ~ 2 sqrt(d) = 0.2 of Gamma",
      "smallest |levels| = %s, %s; x0 = %s" % (mp.nstr(evs[0], 3), mp.nstr(evs[1], 3), mp.nstr(x0, 6)))

# ---- controls (each must fail as it should)
vals_c = (Fr(9, 5), Fr(1, 5), Fr(601, 2000))        # kappa slightly above sqrt(P)/2 = 3/10
d_c = vals_c[2] ** 2 / (vals_c[0] * vals_c[1] / 4) - 1
tcn_c = make_vals_exact(TC["Ny"], vals_c)
check(tcn_c.get((2, 0, 0), 0) != 0, "S5.4 CONTROL: at kappa = 601/2000 (u = (1+d) P/4, d = %s) the weight-2 term of N_y is non-zero, so the u = P/4 jet identity (S2.4) correctly fails" % float(d_c))
x0c = mp.acos((1 - mp.mpf(d_c.numerator) / d_c.denominator) / (1 + mp.mpf(d_c.numerator) / d_c.denominator))
rho_F1 = FIXRES["F1 (9/5,1/5,2;3/10)"]["rho"]
Hn_c = bloch_numeric(mp.mpf(9) / 5, mp.mpf(1) / 5, mp.mpf(2), mp.mpf(601) / 2000, (x0c / (2 * mp.pi), 1 - x0c / (2 * mp.pi), 0))
evc = sorted([abs(e) for e in mp.eigh(Hn_c, eigvals_only=True)])
check(evc[1] < mp.mpf(10) ** -30 and x0c < mp.mpf(rho_F1.numerator) / rho_F1.denominator,
      "S5.5 CONTROL: at that kappa another touching sits at x0 = %s < rho = %s of the u = P/4 ball (so the u = P/4 radius cannot be reused off the curve)" % (mp.nstr(x0c, 5), rho_F1))
vals1 = (Fr(9, 5), Fr(1, 5), Fr(3, 10))
tc1 = {nm: make_vals_exact(TC[nm], vals1) for nm in ("Nx",)}
wrong_lead = {(0, 1, 0): -16 * 4 * 2 * vals1[0], (0, 0, 1): 16 * 4 * 2}   # Jx in place of Jy
check({k_: v for k_, v in tc1["Nx"].items() if wt(k_) < 6} != wrong_lead, "S5.6 CONTROL: swapping Jy -> Jx in d_lead is detected (the leading map is not symmetric in the in-plane couplings)")
# sphere radius control: the certificate conditions fail for a radius far above the certified one (exact inequalities, F1)
res_big, _, _ = ball_certificate("F1big", Fr(9, 5), Fr(1, 5), Fr(3, 10), [Fr(1, 2)])
check(res_big is None, "S5.7 CONTROL: the same exact inequalities fail at rho = 1/2 for F1 (no certificate beyond the stated radius)")

# ================================================================================================ S6: FLOAT diagnostics
print("== S6 float diagnostics (consistency only)", flush=True)


def Hnum(Jx_v, Jy_v, Jz_v, k_v, th):
    th = np.asarray(th, float)
    amp = {"x": 2 * Jx_v, "y": 2 * Jy_v, "z": 2 * Jz_v, "odd": 2 * k_v}
    M = np.zeros((4, 4), complex)
    for a, b, n, kd in TERMS:
        ph = np.exp(1j * (n[0] * th[0] + n[1] * th[1] + n[2] * th[2]))
        M[a, b] += amp[kd] * ph
        M[b, a] -= amp[kd] * np.conj(ph)
    return 1j * M


def theta_of(x, y, z):
    return (x + y, y - x, z)


def lau_eval(Lc, vals, x, y, z):
    tot = 0j
    th = theta_of(x, y, z)
    for m, c in Lc.items():
        re_, im_ = evalR(c, vals)
        tot += (float(re_) + 1j * float(im_)) * np.exp(1j * (m[0] * th[0] + m[1] * th[1] + m[2] * th[2]))
    return tot


rng = random.Random(7)
Jxf, Jyf, kf = Fr(9, 5), Fr(1, 5), Fr(3, 10)
valsf = (Jxf, Jyf, kf)
rho_f = FIXRES["F1 (9/5,1/5,2;3/10)"]["rho"]
mx_err = 0.0
min_gap = 1e9
ratio_dev = 0.0
for _ in range(300):
    r_ = float(rho_f) * rng.random() ** 0.5
    X, Y, Z = rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-1, 1)
    mmax = max(abs(X), abs(Y), abs(Z))
    x, y, z = r_ * X / mmax, r_ ** 4 * Y / mmax, r_ ** 4 * Z / mmax
    Hm = Hnum(float(Jxf), float(Jyf), float(Jxf + Jyf), float(kf), theta_of(x, y, z))
    ev_ = np.linalg.eigvalsh(Hm)
    min_gap = min(min_gap, min(abs(ev_[1]), abs(ev_[2])))
    dH_n = float(np.prod(ev_))
    N = np.array([lau_eval(S[nm], valsf, x, y, z) for nm in ("Nx", "Ny", "Nz", "N0")])
    dC = lau_eval(S["detC"], valsf, x, y, z)
    pred = (N[3].real ** 2 - (N[0].real ** 2 + N[1].real ** 2 + N[2].real ** 2)) / dC.real
    mx_err = max(mx_err, abs(pred - dH_n) / max(abs(dH_n), 1e-300))
    d_lead_sq = (2 * float(Jyf) * y - float(Jxf + Jyf) * z) ** 2 + (float(Jxf * Jyf) * x ** 4 / (4 * float(Jxf + Jyf))) ** 2 + (8 * float(kf) * y) ** 2
    ratio_dev = max(ratio_dev, abs(dH_n / (16 * float(Jxf + Jyf) ** 2 * d_lead_sq) - 1)) if d_lead_sq > 0 else ratio_dev
check(mx_err < 1e-6, "S6.1 FLOAT: det H from numpy Bloch eigenvalues equals (N0^2 - |N|^2)/detC from the exact Laurent objects at 300 random points of the certified ball (F1)", "max rel err %.2e" % mx_err)
check(min_gap > 0, "S6.2 FLOAT: middle levels are non-zero at those points (smallest |middle level| %.3e)" % min_gap)
check(ratio_dev < 0.5, "S6.3 FLOAT: det H / (16 s^2 |d_lead|^2) is within 50%% of 1 at those points (max deviation %.3f; sanity of the jet at the certified radius)" % ratio_dev)

# Fukui Chern number of the two lowest bands on the boundary of the certified quasi-ball (box faces), F1, radius a bit below certified
def fukui_box(Jx_v, Jy_v, k_v, rho, n=26):
    pts = {}
    def U(th):
        Hm = Hnum(Jx_v, Jy_v, Jx_v + Jy_v, k_v, th)
        w, v = np.linalg.eigh(Hm)
        return v[:, :2]
    total = 0.0
    maxph = 0.0
    faces = []
    g = np.linspace(-1, 1, n + 1)
    for axis in range(3):
        for sgn in (-1, 1):
            faces.append((axis, sgn))
    for axis, sgn in faces:
        other = [a for a in range(3) if a != axis]
        grid = {}
        for i in range(n + 1):
            for j in range(n + 1):
                c = [0.0, 0.0, 0.0]
                c[axis] = sgn * 1.0
                c[other[0]] = g[i]
                c[other[1]] = g[j]
                x, y, z = rho * c[0], rho ** 4 * c[1], rho ** 4 * c[2]
                grid[(i, j)] = U(theta_of(x, y, z))
        # orientation: outward normal e_axis * sgn
        orient = sgn * (1 if (other[0], other[1]) in ((1, 2), (2, 0), (0, 1)) else -1)
        for i in range(n):
            for j in range(n):
                u1, u2, u3, u4 = grid[(i, j)], grid[(i + 1, j)], grid[(i + 1, j + 1)], grid[(i, j + 1)]
                prod = np.linalg.det(u1.conj().T @ u2) * np.linalg.det(u2.conj().T @ u3) * np.linalg.det(u3.conj().T @ u4) * np.linalg.det(u4.conj().T @ u1)
                ph = np.angle(prod)
                maxph = max(maxph, abs(ph))
                total += orient * ph
    return total / (2 * np.pi), maxph


for nm_f, fx in (("F1", (0.0 + 9 / 5, 1 / 5, 3 / 10)), ("F2'", (0.5, 2.0, 0.5))):
    rho_use = float(FIXRES["F1 (9/5,1/5,2;3/10)"]["rho"]) if nm_f == "F1" else float(FIXRES["F2' (1/2,2,5/2;1/2)"]["rho"])
    cn, mph = fukui_box(fx[0], fx[1], fx[2], rho_use)
    check(abs(cn) < 1e-9 and mph < 1.0, "S6.%s FLOAT: Fukui Chern number of the two lowest bands on the quasi-sphere (rho = %s) is %.2e (integer 0 expected); max plaquette phase %.3f < 1 (resolved)" % (nm_f, rho_use, cn, mph))

# ================================================================================================ summary
TOTAL = PASS + FAIL
print("elapsed %.1fs" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
min_rho = {k_: str(v["rho"]) for k_, v in FIXRES.items() if v}
fam = {m_: str(v["rho"]) for m_, v in FAMRES.items() if v}
if FAIL == 0:
    print("HIT: scoped result for the supplied comparator only: at u = kappa^2 = P/4 on J_z = Jx + Jy with Jx != Jy the zone centre is the unique zero of det H in explicit quasi-balls (x <= rho, |y|,|z| <= rho^4; rho %s at the six fixtures, uniform rho = %s for Jx/Jy in [1/5,5] and %s for [1/10,10]) with complement gap > 0 and occupied-bundle Chern number 0 on every quasi-sphere inside; the census runner's weights (1;2,2) leave the whole x-axis as zero set of the leading jet, and any radius shrinks like 2 sqrt(u/(P/4) - 1) as u -> P/4+." % (sorted(min_rho.values()), fam.get(5), fam.get(10)))
print("SUMMARY: exact weighted jets, complement gap, explicit punctured-ball isolation and a zero occupied-bundle Chern number at the u = P/4 zone-centre merger for Jx != Jy (fixtures and a uniform curve family), plus the exact pair that makes any such radius shrink as u -> P/4+; scope is the supplied comparator only.")
sys.exit(0 if FAIL == 0 else 1)
