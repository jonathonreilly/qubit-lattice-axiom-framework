#!/usr/bin/env python3
"""Zone centre Gamma of the supplied flux-free composite-network comparator (J_x = J_y = 1, J_z = 2, odd term kappa): rigorous local statements.

Supplied model, not an axiom of the framework.  H(f) = i M(f) (four-site Bloch matrix, landed network rules rebuilt below), theta = 2 pi f =
x (1,-1,0) + y (1,1,0) + z (0,0,1).  H(0) has spectrum {0,0,+-8}.  All proofs use exact rational arithmetic (python Fractions, sympy QQ_I[kappa]);
square roots are rounded in the direction that keeps every inequality valid.  The FLOAT blocks are consistency diagnostics and carry the tag FLOAT.

Objects (all exact Laurent polynomials in e^{ix}, e^{iy}, e^{iz} with coefficients in Q(i)[kappa]):
  blocks of T^T H T, T = [W U]/sqrt2, W = {(1,0,-1,0),(0,1,0,-1)} (kernel of H(0)), U = {(1,0,1,0),(0,1,0,1)};  C = U-block (2x2), detC = det C,
  Num = detC * S with S = A - B C^-1 B^+ the E = 0 Schur complement; Pauli components (Nx, Ny, Nz, N0) of Num, so that  D = N/detC,  d0 = N0/detC.
  Exact identity  det(Num) = detC * det H  gives  det H = (|N|^2 - N0^2)/(-detC).
Method for a neighbourhood: weights x:1, (y,z):w; quasi-norm N (N^4 = x^4+y^2+z^2 for w = 2, N^8 = x^8+y^2+z^2 for w = 4).  The leading map d_lead is quasi-homogeneous,
Num = -64 d_lead + G, with G of weight >= Lw (exact Taylor coefficients, total degree <= 12, symbolic kappa).  Bound |G| <= K N^Lw on N <= rho via the exact
Taylor polynomial plus the Lagrange remainder  |e^{i phi} - T_n| <= |phi|^{n+1}/(n+1)!  summed over Fourier modes.  Conditions (A)-(D):
  (A) K_Delta rho^2 < 64 (Delta = detC + 64): detC < 0 on the ball;  (B) K_G rho^eG < 64 s: Num never vanishes except at 0 and the homotopy
  Num_t = -64 d_lead + t G stays nonzero;  (C) N0 < |N|: det H > 0 and H has two negative and two positive eigenvalues;  (D) |R| < 64|d_lead|^2 for R = det H - 64|d_lead|^2.
Here |d_lead| >= s N^wl.  Consequences: Gamma is an isolated zero of det H and of the Pauli map; deg(D/|D|) on every sphere N = r <= rho equals deg(d_lead/|d_lead|) = 0
(d_lead omits a point of S^2); the exact parity N(-theta) = (-Nx, Ny, -Nz) gives degree 0 on every inversion-symmetric zero-free sphere by itself.
Exact axis facts (section 7): on theta = x(1,-1,0) one has Nx = Nz = N0 = 0, detC = -4(cos x+3)^2, D_y = 4(cos x-1)(2k^2(cos x+1)-1)/(cos x+3), so the nodes
cos x0 = 1/(2k^2) - 1 are exact zeros of D; charges from the exact Jacobian determinant in the rational parameter t, kappa = (t^2+1)/(4t).
Prints TOTAL: PASS=N FAIL=M.   GAMREM_VERBOSE=1 prints extra detail lines.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import time
from fractions import Fraction as Fr
from math import factorial, isqrt

import numpy as np
import sympy as sp
from sympy import QQ, QQ_I
from sympy.polys.rings import ring

AUDIT_TIMEOUT_SEC = 120
VERBOSE = os.environ.get("GAMREM_VERBOSE") == "1"
RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def vprint(*a):
    if VERBOSE:
        print("   ", *a, flush=True)


# ------------------------------------------------------------------------------------------------ network terms (landed rules, rebuilt)
AX = {"x": 0, "y": 1, "z": 2}


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s_ in (-1, 1):
            q = list(p); q[a] += s_; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce(p):
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(int(v) for v in np.subtract(n2, n1)), 2.0 * kappa))
    return out


_KIND = {2.0: "x", 6.0: "y", 14.0: "z", 0.6: "odd"}          # amplitudes tagged by running terms() at J = (1,3,7), kappa = 0.3
TERMS = [(int(a), int(b), tuple(int(v) for v in n), _KIND[round(float(t), 9)]) for (a, b, n, t) in terms((1.0, 3.0, 7.0), 0.3)]
assert len(TERMS) == 18

# ------------------------------------------------------------------------------------------------ exact Laurent polynomials over Q(i)[kappa]
R, kk = ring("k", QQ_I)
I_ = R(QQ_I(0, 1))


def Rc(n, d=1):
    return R(QQ_I(QQ(n, d), QQ(0)))


class LP(dict):
    """Laurent polynomial in (Zx, Zy, Zz) = (e^{ix}, e^{iy}, e^{iz}): {(a,b,c): coefficient in Q(i)[kappa]}"""

    def __add__(s, o):
        r = LP(s)
        for key, v in o.items():
            w_ = r.get(key, R.zero) + v
            if w_ == 0:
                r.pop(key, None)
            else:
                r[key] = w_
        return r

    def __neg__(s):
        return LP({key: -v for key, v in s.items()})

    def __sub__(s, o):
        return s + (-o)

    def __mul__(s, o):
        if not isinstance(o, LP):
            return LP({key: v * o for key, v in s.items() if v * o != 0})
        r = {}
        for k1, v1 in s.items():
            for k2, v2 in o.items():
                key = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
                r[key] = r.get(key, R.zero) + v1 * v2
        return LP({key: v for key, v in r.items() if v != 0})


AMP = {"x": R(2), "y": R(2), "z": R(4), "odd": 2 * kk}      # 2 J_x, 2 J_y, 2 J_z (J = 1, 1, 2), 2 kappa
Hm = [[LP() for _ in range(4)] for _ in range(4)]
for (a_, b_, n_, kind_) in TERMS:
    t_ = AMP[kind_]
    fr = (n_[0] - n_[1], n_[0] + n_[1], n_[2])              # phase n.theta = (n1-n2) x + (n1+n2) y + n3 z
    Hm[a_][b_] = Hm[a_][b_] + LP({fr: I_ * t_})
    Hm[b_][a_] = Hm[b_][a_] + LP({(-fr[0], -fr[1], -fr[2]): -I_ * t_})
hq = R(QQ_I(QQ(1, 2), QQ(0)))
Wv = [(1, 0, -1, 0), (0, 1, 0, -1)]
Uv = [(1, 0, 1, 0), (0, 1, 0, 1)]


def blk(X, Y):
    out = [[LP(), LP()], [LP(), LP()]]
    for i in range(2):
        for j in range(2):
            acc = LP()
            for p in range(4):
                for q in range(4):
                    c = X[i][p] * Y[j][q]
                    if c != 0:
                        acc = acc + Hm[p][q] * R(QQ_I(c, 0)) * hq
            out[i][j] = acc
    return out


At, Bt, Ct, Bdt = blk(Wv, Wv), blk(Wv, Uv), blk(Uv, Uv), blk(Uv, Wv)
detC = Ct[0][0] * Ct[1][1] - Ct[0][1] * Ct[1][0]
adjC = [[Ct[1][1], -Ct[0][1]], [-Ct[1][0], Ct[0][0]]]


def mm(X, Y):
    return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)] for i in range(2)]


BadjBd = mm(mm(Bt, adjC), Bdt)
Nm = [[detC * At[i][j] - BadjBd[i][j] for j in range(2)] for i in range(2)]


def comb(pairs):
    out = LP()
    for l_, c_ in pairs:
        out = out + l_ * c_
    return out


Nx = comb([(Nm[0][1], hq), (Nm[1][0], hq)])
Ny = comb([(Nm[0][1], I_ * hq), (Nm[1][0], -I_ * hq)])
Nz = comb([(Nm[0][0], hq), (Nm[1][1], -hq)])
N0 = comb([(Nm[0][0], hq), (Nm[1][1], hq)])


def perm_sign(p):
    s_ = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s_ = -s_
    return s_


import itertools

detH = LP()
for p_ in itertools.permutations(range(4)):
    term = LP({(0, 0, 0): R(QQ_I(perm_sign(p_), 0))})
    for i in range(4):
        term = term * Hm[i][p_[i]]
    detH = detH + term
LPS = {"Nx": Nx, "Ny": Ny, "Nz": Nz, "N0": N0, "detC": detC, "detH": detH}


# ------------------------------------------------------------------------------------------------ exact helpers
def to_fr(q):
    return Fr(int(q.numerator), int(q.denominator))


def coef_polylist(v):
    return [(m, to_fr(co.x), to_fr(co.y)) for (m,), co in v.terms()]


def evalc(v, kap):
    re = Fr(0); im = Fr(0)
    for m, a, b in coef_polylist(v):
        re += a * kap ** m; im += b * kap ** m
    return re, im


def up_sqrt(fr):
    P, Q = fr.numerator, fr.denominator
    return Fr(isqrt(P * Q) + 1, Q)


def lo_root(fr, n):
    """rational r <= fr^(1/n) (floor of the integer n-th root of P Q^(n-1), over Q)"""
    P, Q = fr.numerator, fr.denominator
    M = P * Q ** (n - 1)
    lo, hi = 0, 1
    while hi ** n <= M:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** n <= M:
            lo = mid
        else:
            hi = mid
    return Fr(lo, Q)


def absmod(re, im):
    if im == 0:
        return abs(re)
    if re == 0:
        return abs(im)
    return abs(re) + abs(im)                                   # upper bound of the complex modulus


def modc(v, kap, abs_coeffs):
    if abs_coeffs:
        return sum(absmod(a, b) * kap ** m for m, a, b in coef_polylist(v))
    re, im = evalc(v, kap)
    return abs(re) if im == 0 else (abs(im) if re == 0 else up_sqrt(re * re + im * im))


def taylor_coeffs(l, n):
    """exact Taylor coefficients (total degree <= n) at 0 in (x,y,z) of the real-analytic function sum_nu c_nu e^{i nu.(x,y,z)}"""
    out = {}
    ipow = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    items = list(l.items())
    for p in range(n + 1):
        for q in range(n + 1 - p):
            for r in range(n + 1 - p - q):
                s_ = R.zero
                for key, v in items:
                    f = key[0] ** p * key[1] ** q * key[2] ** r
                    if f:
                        s_ = s_ + v * f
                if s_ == 0:
                    continue
                ip = ipow[(p + q + r) % 4]
                den = factorial(p) * factorial(q) * factorial(r)
                out[(p, q, r)] = s_ * R(QQ_I(QQ(ip[0], den), QQ(ip[1], den)))
    return out


def sub_poly(tc, P):
    g = dict(tc)
    for key, v in P.items():
        w_ = g.get(key, R.zero) - v
        if w_ == 0:
            g.pop(key, None)
        else:
            g[key] = w_
    return g


def spec(g, kap):
    out = {}
    for key, v in g.items():
        re, im = evalc(v, kap)
        assert im == 0
        if re != 0:
            out[key] = re
    return out


def wt(key, w):
    return key[0] + w * (key[1] + key[2])


NTAY = 12


def Kbound(l, g, w, Lw, n, rho, kap, abs_coeffs):
    """K with |F - P| <= K N^Lw on N <= rho (rho <= 1); g = Taylor(F) - P (every weight < Lw must vanish); abs_coeffs: kappa-polynomial bound valid for 0 < kappa <= kap."""
    if not abs_coeffs:
        g = spec(g, kap)
    assert all(wt(key, w) >= Lw for key in g), "low-weight coefficient present"
    assert n + 1 >= Lw and rho <= 1
    tot = Fr(0)
    for key, v in g.items():
        if abs_coeffs:
            for m, a, b in coef_polylist(v):
                assert b == 0
                tot += abs(a) * kap ** m * rho ** (wt(key, w) - Lw)
        else:
            tot += abs(v) * rho ** (wt(key, w) - Lw)
    rem_fac = rho ** (n + 1 - Lw) / factorial(n + 1)
    for (a, b, c), v in l.items():
        base = (abs(a) + (abs(b) + abs(c)) * rho ** (w - 1)) ** (n + 1)
        tot += modc(v, kap, abs_coeffs) * base * rem_fac
    return tot


def Kpoly(l, g, w, Lw, n):
    """kappa-polynomial (nonnegative coefficients) for rho = 1"""
    assert all(wt(key, w) >= Lw for key in g)
    out = {}
    for key, v in g.items():
        for m, a, b in coef_polylist(v):
            assert b == 0
            out[m] = out.get(m, Fr(0)) + abs(a)
    for (a, b, c), v in l.items():
        base = Fr((abs(a) + abs(b) + abs(c)) ** (n + 1), factorial(n + 1))
        for m, a_, b_ in coef_polylist(v):
            out[m] = out.get(m, Fr(0)) + absmod(a_, b_) * base
    return out


def peval(poly, kap):
    return sum(c * kap ** m for m, c in poly.items())


# ------------------------------------------------------------------------------------------------ leading data
a_ = Rc(1, 2) - 2 * kk ** 2                                       # a = (1 - 4 kappa^2)/2
# generic kappa, weights (1,2,2): d_lead = (2(y-z), a x^2, -8 kappa y); Num_lead = -64 d_lead; P4 = 64 |d_lead|^2
PL_GEN = {"Nx": {(0, 1, 0): -128 * Rc(1), (0, 0, 1): 128 * Rc(1)}, "Ny": {(2, 0, 0): -64 * a_}, "Nz": {(0, 1, 0): 512 * kk}}
P4 = {(0, 2, 0): 64 * (4 + 64 * kk ** 2), (0, 1, 1): -512 * Rc(1), (0, 0, 2): 256 * Rc(1), (4, 0, 0): 64 * a_ * a_}
# kappa = 1/2, weights (1,4,4): d_lead = (2(y-z), x^4/8, -4y); P8 = 64 |d_lead|^2
PL_HALF = {"Nx": {(0, 1, 0): -128 * Rc(1), (0, 0, 1): 128 * Rc(1)}, "Ny": {(4, 0, 0): -8 * Rc(1)}, "Nz": {(0, 1, 0): 256 * Rc(1)}}
P8 = {(0, 2, 0): 1280 * Rc(1), (0, 1, 1): -512 * Rc(1), (0, 0, 2): 256 * Rc(1), (8, 0, 0): Rc(1)}
CASES = {"gen": dict(w=2, wl=2, LwG=4, Lw0=5, LwC=2, LwR=6, PL=PL_GEN, PP=P4),
         "half": dict(w=4, wl=4, LwG=6, Lw0=9, LwC=2, LwR=10, PL=PL_HALF, PP=P8)}
TC = {nm: taylor_coeffs(l, NTAY) for nm, l in LPS.items()}
GG = {}
for cs, cf in CASES.items():
    GG[cs] = dict(G={nm: sub_poly(TC[nm], cf["PL"][nm]) for nm in ("Nx", "Ny", "Nz")}, g0=TC["N0"],
                  gC=sub_poly(TC["detC"], {(0, 0, 0): -64 * Rc(1)}), gR=sub_poly(TC["detH"], cf["PP"]))


def all_K(cs, rho, kap, ab):
    cf, gg = CASES[cs], GG[cs]
    KG = {nm: Kbound(LPS[nm], gg["G"][nm], cf["w"], cf["LwG"], NTAY, rho, kap, ab) for nm in gg["G"]}
    K0 = Kbound(N0, gg["g0"], cf["w"], cf["Lw0"], NTAY, rho, kap, ab)
    KC = Kbound(detC, gg["gC"], cf["w"], cf["LwC"], NTAY, rho, kap, ab)
    KR = Kbound(detH, gg["gR"], cf["w"], cf["LwR"], NTAY, rho, kap, ab)
    return KG, K0, KC, KR


def s_lead(cs, k1, k2):
    """rational s with |d_lead| >= s N^wl on the whole ball, for kappa in [k1, k2] (1/2 outside [k1,k2] for the generic case)"""
    if cs == "half":
        return Fr(1, 8)                                           # |d_lead|^2 >= N^8/64
    assert not (k1 <= Fr(1, 2) <= k2)
    amin = min(abs(1 - 4 * k1 * k1), abs(1 - 4 * k2 * k2)) / 2
    lam = 32 * k1 * k1 / (1 + 8 * k1 * k1)                       # lambda_min([[4+64k^2,-4],[-4,4]]) >= det/trace
    return min(amin, lo_root(lam, 2))


def conds(cs, rho, k1, k2, ab):
    try:
        return conds_raw(cs, rho, k1, k2, ab)
    except AssertionError as e_:                                   # a violated weight/leading-term identity is a failed check, not a crash
        vprint("assertion in conds:", e_)
        return False, False, False, False, dict(KG=0.0, K0=0.0, KC=0.0, KR=0.0, s=0.0)


def conds_raw(cs, rho, k1, k2, ab):
    cf = CASES[cs]
    KG, K0, KC, KR = all_K(cs, rho, k2, ab)
    s_ = s_lead(cs, k1, k2)
    KGn = up_sqrt(sum(v * v for v in KG.values()))
    eG = cf["LwG"] - cf["wl"]; e0 = cf["Lw0"] - cf["wl"]; eR = cf["LwR"] - 2 * cf["wl"]
    A = KC * rho ** 2 < 64
    B = KGn * rho ** eG < 64 * s_
    C = K0 * rho ** e0 + KGn * rho ** eG < 64 * s_
    D = KR * rho ** eR < 64 * s_ * s_
    return A, B, C, D, dict(KG=float(KGn), K0=float(K0), KC=float(KC), KR=float(KR), s=float(s_))


# ================================================================================================ 0. exact structure
Hz = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        Hz[i, j] = sum((v.as_expr() for v in Hm[i][j].values()), sp.Integer(0))
M0 = sp.Matrix([[0, 1, 0, 1], [-1, 0, -1, 0], [0, 1, 0, 1], [-1, 0, -1, 0]])
lam = sp.Symbol("lam")
Pk = sp.Matrix([[1, 0, -1, 0], [0, 1, 0, -1], [-1, 0, 1, 0], [0, -1, 0, 1]]) / 2
check("0: 18 network terms rebuilt; H(0) = 4i M0, spectrum {0,0,+-8}, H(0)^2 = 64 (1-P) for every kappa",
      sp.simplify(Hz - 4 * sp.I * M0) == sp.zeros(4, 4) and sp.expand(Hz.charpoly(lam).as_expr() - lam ** 2 * (lam ** 2 - 64)) == 0
      and (Hz * Hz - 64 * (sp.eye(4) - Pk)) == sp.zeros(4, 4))


def at0(l):
    s_ = R.zero
    for v in l.values():
        s_ = s_ + v
    return s_


def conjc(v):
    r = R.zero
    for (m,), co in v.terms():
        r = r + R(QQ_I(co.x, -co.y)) * kk ** m
    return r


def is_real(l):
    return all(l.get((-k_[0], -k_[1], -k_[2]), R.zero) == conjc(v) for k_, v in l.items())


def parity(l, sgn):
    return all(l.get((-k_[0], -k_[1], -k_[2]), R.zero) == (v if sgn > 0 else -v) for k_, v in l.items())


dN = Nm[0][0] * Nm[1][1] - Nm[0][1] * Nm[1][0]
check("1a: exact: Num(0) = 0, detC(0) = -64, Laurent identity det(Num) = detC*detH (symbolic kappa)",
      all(at0(l) == 0 for l in (Nx, Ny, Nz, N0)) and at0(detC) == R(QQ_I(-64, 0)) and (dN - detC * detH) == LP(),
      f"Laurent terms Nx {len(Nx)} Ny {len(Ny)} Nz {len(Nz)} N0 {len(N0)} detC {len(detC)} detH {len(detH)}")
check("1b: exact: all real; Nx, Nz, N0 odd, Ny, detC, detH even => D(-th) = (-Dx, Dy, -Dz)(th), d0 odd",
      all(is_real(l) for l in LPS.values()) and all(parity(l, -1) for l in (Nx, Nz, N0)) and all(parity(l, 1) for l in (Ny, detC, detH)))

# ================================================================================================ 2. exact Taylor structure (symbolic kappa)
def wmin(g, w):
    return min([wt(key, w) for key in g], default=99)


g_gen, g_half = GG["gen"], GG["half"]
check("2a: generic k, weights (1,2,2): Num = -64 d_lead + G, d_lead = (2(y-z), (1-4k^2)x^2/2, -8k y); wt(G)>=4, wt(N0)>=5, wt(detC+64)>=2",
      all(wmin(g_gen["G"][nm], 2) >= 4 for nm in g_gen["G"]) and wmin(g_gen["g0"], 2) >= 5 and wmin(g_gen["gC"], 2) >= 2,
      f"G {[wmin(g_gen['G'][nm], 2) for nm in ('Nx', 'Ny', 'Nz')]} N0 {wmin(g_gen['g0'], 2)} Delta {wmin(g_gen['gC'], 2)}")
R6 = {(6, 0, 0): Rc(-8, 3) * (64 * kk ** 4 - 20 * kk ** 2 + 1), (2, 2, 0): -32 * (84 * kk ** 2 + 1), (2, 1, 1): 128 * (8 * kk ** 2 + 1), (2, 0, 2): -64 * (8 * kk ** 2 + 1)}
w6 = {key: v for key, v in g_gen["gR"].items() if wt(key, 2) == 6}
check("2b: generic k: det H = 64|d_lead|^2 + R, wt(R) >= 6 (no weight 5); weight-6 part of R explicit (4 monomials)",
      wmin(g_gen["gR"], 2) >= 6 and sub_poly(w6, R6) == {} and sub_poly(R6, w6) == {}, "x^6: -(8/3)(4k^2-1)(16k^2-1)")
check("2c: k = 1/2, weights (1,4,4): d_lead = (2(y-z), x^4/8, -4y); wt(G)>=6, wt(N0)>=9, wt(det H - 64|d_lead|^2)>=10",
      all(wmin(spec(g_half["G"][nm], Fr(1, 2)), 4) >= 6 for nm in g_half["G"]) and wmin(spec(g_half["g0"], Fr(1, 2)), 4) >= 9
      and wmin(spec(g_half["gR"], Fr(1, 2)), 4) >= 10 and wmin(spec(g_half["gC"], Fr(1, 2)), 4) >= 2,
      f"G {[wmin(spec(g_half['G'][nm], Fr(1, 2)), 4) for nm in ('Nx', 'Ny', 'Nz')]} N0 {wmin(spec(g_half['g0'], Fr(1, 2)), 4)} R {wmin(spec(g_half['gR'], Fr(1, 2)), 4)}")

eps_ = sp.Symbol("eps"); xs_, ys_, zs_, ks_ = sp.symbols("x y z k")


def poly_wt(tc, maxwt):
    tot = 0
    for (p, q, r), v in tc.items():
        if wt((p, q, r), 2) <= maxwt:
            tot += sp.expand(v.as_expr()) * xs_ ** p * ys_ ** q * zs_ ** r * eps_ ** wt((p, q, r), 2)
    return sp.expand(tot)


dCs = poly_wt(TC["detC"], 4)
landed = {"Nx": 2 * eps_ ** 2 * (ys_ - zs_) + eps_ ** 4 * (-7 * ks_ ** 2 * xs_ ** 2 * ys_ / 2 + 5 * ks_ ** 2 * xs_ ** 2 * zs_ / 2 - xs_ ** 2 * ys_ / 8 - xs_ ** 2 * zs_ / 8),
          "Ny": eps_ ** 2 * (1 - 4 * ks_ ** 2) / 2 * xs_ ** 2 + eps_ ** 4 * (5 * ks_ ** 2 * xs_ ** 4 / 12 + xs_ ** 4 / 48 + ys_ ** 2 - zs_ ** 2 / 2),
          "Nz": -8 * ks_ * ys_ * eps_ ** 2 + eps_ ** 4 * (ks_ * xs_ ** 2 * ys_ / 2 + ks_ * xs_ ** 2 * zs_ / 2), "N0": sp.Integer(0)}
ser_ok = all(sp.expand(sp.series(poly_wt(TC[nm], 4) / dCs, eps_, 0, 5).removeO() - landed[nm]) == 0 for nm in ("Nx", "Ny", "Nz", "N0"))
check("2d: exact: series of Num/detC to weight 4 equals the landed Brillouin-Wigner Pauli vector (weights 2 and 4; d0 = 0)", ser_ok,
      "d_y weight 4: (20k^2+1)/48 x^4 + y^2 - z^2/2")

# ================================================================================================ 3. generic kappa: explicit neighbourhoods
RHO = {"k = 1/4": (Fr(1, 4), Fr(1, 4), False, Fr(37, 100), Fr(13, 100)),
       "k = 1": (Fr(1), Fr(1), False, Fr(19, 50), Fr(17, 100)),
       "k = 2": (Fr(2), Fr(2), False, Fr(13, 50), Fr(1, 10)),
       "k in [1/10,2/5]": (Fr(1, 10), Fr(2, 5), True, Fr(23, 100), Fr(47, 1000)),
       "k in [3/5,3]": (Fr(3, 5), Fr(3), True, Fr(31, 500), Fr(19, 2500))}
flags_gen = {}
for nm, (k1, k2, ab, rN, rD) in RHO.items():
    cN = conds("gen", rN, k1, k2, ab); cD = conds("gen", rD, k1, k2, ab)
    ok = cN[0] and cN[1] and cN[2] and cD[0] and cD[3]
    flags_gen[nm] = ok
    check(f"3: {nm}: rho_N = {float(rN):g} (conds A,B,C), rho_D = {float(rD):g} (A,D)", ok,
          f"K_G={cN[4]['KG']:.0f} K_N0={cN[4]['K0']:.0f} s={cN[4]['s']:.3f} K_R={cD[4]['KR']:.0f}")

# all-kappa formula: published constants (rounded up) dominate the exact kappa-polynomials
w_, cfg = 2, CASES["gen"]
PUB = {"Gx": {0: 294, 2: 1446}, "Gy": {0: 174, 2: 1340}, "Gz": {1: 877, 3: 231}, "N0": {1: 115, 3: 268}, "dC": {0: 75, 2: 16}, "R": {0: 1105, 2: 20480, 4: 3007}}
try:
    KP = {"Gx": Kpoly(Nx, g_gen["G"]["Nx"], w_, 4, NTAY), "Gy": Kpoly(Ny, g_gen["G"]["Ny"], w_, 4, NTAY), "Gz": Kpoly(Nz, g_gen["G"]["Nz"], w_, 4, NTAY),
          "N0": Kpoly(N0, g_gen["g0"], w_, 5, NTAY), "dC": Kpoly(detC, g_gen["gC"], w_, 2, NTAY), "R": Kpoly(detH, g_gen["gR"], w_, 6, NTAY)}
    dom = all(set(KP[nm]) <= set(PUB[nm]) and all(KP[nm][m] <= PUB[nm][m] for m in KP[nm]) for nm in PUB)
except AssertionError:
    KP = {}; dom = False


def rho_formula(kap):
    """rho(kappa) = min{1, sqrt(64/K_dC), sqrt(32 s/Lam), (16 s/K_N0)^(1/3), sqrt(32 s^2/K_R)}, Lam = K_Gx+K_Gy+K_Gz, s = min(|1-4k^2|/2, sqrt(32k^2/(1+8k^2)))"""
    s_ = min(abs(1 - 4 * kap * kap) / 2, lo_root(32 * kap * kap / (1 + 8 * kap * kap), 2))
    pe = {nm: peval(PUB[nm], kap) for nm in PUB}
    Lam = pe["Gx"] + pe["Gy"] + pe["Gz"]
    return min(Fr(1), lo_root(64 / pe["dC"], 2), lo_root(32 * s_ / Lam, 2), lo_root(16 * s_ / pe["N0"], 3), lo_root(32 * s_ * s_ / pe["R"], 2))


GRID = [Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(2, 5), Fr(9, 20), Fr(99, 200), Fr(101, 200), Fr(11, 20), Fr(3, 5), Fr(1), Fr(3, 2), Fr(2), Fr(3), Fr(5), Fr(10), Fr(50)]
gr_ok = []
for kp in GRID:
    rf = rho_formula(kp)
    c = conds("gen", rf, kp, kp, False)
    gr_ok.append(c[0] and c[1] and c[2] and c[3])
vprint("rho(kappa) grid:", {str(kp): float(rho_formula(kp)) for kp in GRID})
check("3c: every k > 0, k != 1/2: radius rho(k) = min{1,(64/Kd)^.5,(32s/Lam)^.5,(16s/K0)^(1/3),(32s^2/KR)^.5} from rounded-up k-polynomials",
      dom and all(gr_ok), f"constants dominate exact polynomials: {dom}; A-D re-verified at {len(GRID)} kappa in [1/20,50]; rho(1/4,1,2)="
      + ",".join(f"{float(rho_formula(kp)):.3g}" for kp in (Fr(1, 4), Fr(1), Fr(2))))

# ================================================================================================ 4. kappa = 1/2
kh = Fr(1, 2)
cNh = conds("half", Fr(1, 5), kh, kh, False); cDh = conds("half", Fr(27, 1000), kh, kh, False)
okh = cNh[0] and cNh[1] and cNh[2] and cDh[0] and cDh[3]
check("4: k = 1/2, weights (1,4,4), ball x^8+y^2+z^2 <= rho^8: rho_N = 0.2 (A,B,C), rho_D = 0.027 (A,D)",
      okh, f"K_G={cNh[4]['KG']:.0f} K_N0={cNh[4]['K0']:.0f} s=1/8 K_R={cDh[4]['KR']:.0f}")

# ================================================================================================ 5. degree
a_sign = {nm: [(1 - 4 * kv * kv) / 2 for kv in (k1, k2)] for nm, (k1, k2, ab, rN, rD) in RHO.items()}
fixed = all((v[0] > 0 and v[1] > 0) or (v[0] < 0 and v[1] < 0) for v in a_sign.values())
check("5a: d_lead omits a point of S^2 (d_y = a x^2 has the sign of a, fixed on each kappa range above; x^4/8 >= 0 at 1/2): degree 0",
      fixed and all(kp != Fr(1, 2) for kp in GRID))
hom_ok = all(flags_gen.values()) and okh
check("5b: homotopy -64 d_lead + t G stays nonzero on 0<N<=rho (B); detC<0 (A) => deg(D/|D|) = deg(d_lead/|d_lead|) = 0 on every sphere N = r <= rho",
      hom_ok)
check("5c: parity alone: D(-th) = diag(-1,1,-1) D(th) (det +1), antipodal map has degree -1 => degree 0 on any zero-free inversion-symmetric sphere",
      all(parity(l, -1) for l in (Nx, Nz, N0)) and all(parity(l, 1) for l in (Ny, detC)))
check("5d: (A),(C): H = L^+ diag(S,C) L has signature (2,2) on the balls; Chern number of the two lowest bands on a sphere = +-deg(D/|D|) = 0",
      hom_ok)


# ================================================================================================ 6. FLOAT diagnostics
def Hnum(xyz, kappa):
    x_, y_, z_ = xyz[:, 0], xyz[:, 1], xyz[:, 2]
    th = np.stack([x_ + y_, -x_ + y_, z_], 1)
    amp = {"x": 2.0, "y": 2.0, "z": 4.0, "odd": 2.0 * kappa}
    M = np.zeros((len(xyz), 4, 4), complex)
    for (a, b, n, kind) in TERMS:
        ph = np.exp(1j * (th @ np.array(n, float)))
        M[:, a, b] += amp[kind] * ph
        M[:, b, a] -= amp[kind] * np.conj(ph)
    return 1j * M


Wn = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]], float) / np.sqrt(2)
Un = np.array([[1, 0], [0, 1], [1, 0], [0, 1]], float) / np.sqrt(2)


def schur_num(xyz, kappa):
    H = Hnum(xyz, kappa)
    A = np.einsum("ia,mij,jb->mab", Wn, H, Wn); B = np.einsum("ia,mij,jb->mab", Wn, H, Un); C = np.einsum("ia,mij,jb->mab", Un, H, Un)
    S = A - B @ np.linalg.inv(C) @ np.conj(np.transpose(B, (0, 2, 1)))
    d0 = ((S[:, 0, 0] + S[:, 1, 1]) / 2).real
    dz = ((S[:, 0, 0] - S[:, 1, 1]) / 2).real
    dx = ((S[:, 0, 1] + S[:, 1, 0]) / 2).real
    dy = (1j * (S[:, 0, 1] - S[:, 1, 0]) / 2).real
    dC = np.linalg.det(C).real
    return np.stack([dx, dy, dz], 1), d0, dC, np.linalg.det(H).real


def lp_num(l, kappa, xyz):
    keys = np.array(list(l.keys()), float)
    co = np.array([sum((complex(a) + 1j * complex(b)) * kappa ** m for m, a, b in coef_polylist(v)) for v in l.values()], complex)
    return (np.exp(1j * (xyz @ keys.T)) @ co).real


rng = np.random.default_rng(7)
dev = 0.0
for kv in (0.25, 1.0, 2.0, 0.5):
    pts = rng.uniform(-0.3, 0.3, (200, 3)) * np.array([1, 0.2, 0.2])
    Dn, d0n, dCn, dHn = schur_num(pts, kv)
    dev = max(dev, np.max(np.abs(lp_num(detC, kv, pts) - dCn)), np.max(np.abs(lp_num(detH, kv, pts) - dHn)),
              np.max(np.abs(lp_num(Nx, kv, pts) - dCn * Dn[:, 0])), np.max(np.abs(lp_num(Ny, kv, pts) - dCn * Dn[:, 1])),
              np.max(np.abs(lp_num(Nz, kv, pts) - dCn * Dn[:, 2])), np.max(np.abs(lp_num(N0, kv, pts) - dCn * d0n)))
check("6a FLOAT: Laurent objects vs direct numpy Schur complement, 800 random points, kappa = 1/4, 1, 2, 1/2", dev < 1e-9, f"max deviation {dev:.1e}")


def quasi_sphere(rho, w, m_th, m_ph):
    th = np.linspace(0, np.pi, m_th + 1)[:, None] * np.ones((1, m_ph + 1))
    ph = np.ones((m_th + 1, 1)) * np.linspace(0, 2 * np.pi, m_ph + 1)[None, :]
    p_, q_, s2 = np.cos(th), np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph)
    return np.stack([rho * np.sign(p_) * np.abs(p_) ** (1.0 / w), rho ** w * q_, rho ** w * s2], -1)


def solid_degree(F, m_th=120, m_ph=240):
    """degree of F/|F| from a triangulated surface grid F (m_th+1, m_ph+1, 3) via signed spherical triangle areas; returns (sum/4pi, max edge angle)"""
    U = F / np.linalg.norm(F, axis=-1, keepdims=True)
    a, b, c, d = U[:-1, :-1], U[1:, :-1], U[1:, 1:], U[:-1, 1:]

    def om(p, q, r):
        num = np.einsum("...i,...i", p, np.cross(q, r))
        den = 1 + np.einsum("...i,...i", p, q) + np.einsum("...i,...i", q, r) + np.einsum("...i,...i", r, p)
        return 2 * np.arctan2(num, den)

    tot = om(a, b, c).sum() + om(a, c, d).sum()
    edge = max(np.arccos(np.clip(np.einsum("...i,...i", a, b), -1, 1)).max(), np.arccos(np.clip(np.einsum("...i,...i", a, d), -1, 1)).max())
    return tot / (4 * np.pi), edge


degs = []
for kv, rv, w in ((0.25, 0.37, 2), (1.0, 0.38, 2), (2.0, 0.26, 2), (0.5, 0.2, 4), (0.6, 0.062, 2), (0.55, float(rho_formula(Fr(11, 20))), 2)):
    sph = quasi_sphere(rv, w, 120, 240)
    Dn, d0n, dCn, dHn = schur_num(sph.reshape(-1, 3), kv)
    dg, edge = solid_degree(Dn.reshape(sph.shape), 120, 240)
    degs.append((kv, dg, edge, float(np.max(np.abs(d0n) / np.linalg.norm(Dn, axis=1))), float(dCn.max())))
vprint("float degrees (kappa, deg, max edge angle, max |d0|/|D|, max detC):", degs)
check("6b FLOAT: solid-angle degree of D/|D| (120x240) on proven spheres, kappa = 1/4, 1, 2, 1/2, 0.6, 0.55; |d0|<|D|, detC<0",
      all(abs(dg) < 1e-6 and edge < 1.2 and r0 < 1 and mx < 0 for (kv, dg, edge, r0, mx) in degs),
      "deg max |.| = " + f"{max(abs(t[1]) for t in degs):.0e}; max |d0|/|D| = {max(t[3] for t in degs):.1e}")

pos = True; mxr = 0.0; hneg = True
for kv, k1, k2, rN, rD, w in ((0.25, 0.25, 0.25, 0.37, 0.13, 2), (1.0, 1, 1, 0.38, 0.17, 2), (2.0, 2, 2, 0.26, 0.1, 2), (0.5, 0.5, 0.5, 0.2, 0.027, 4)):
    ss = quasi_sphere(rN, w, 20, 40).reshape(-1, 3) * rng.uniform(0.2, 1.0, (21 * 41, 1))
    Hh = Hnum(ss, kv)
    ev = np.linalg.eigvalsh(Hh)
    hneg = hneg and bool(np.all(ev[:, 1] < 0) and np.all(ev[:, 2] > 0))
    Dn, d0n, dCn, dHn = schur_num(ss, kv)
    pos = pos and bool(np.all(dHn > 0))
    p4 = 64 * ((2 * (ss[:, 1] - ss[:, 2])) ** 2 + ((1 - 4 * kv ** 2) / 2 * ss[:, 0] ** 2) ** 2 + (8 * kv * ss[:, 1]) ** 2) if w == 2 else \
        64 * ((2 * (ss[:, 1] - ss[:, 2])) ** 2 + (ss[:, 0] ** 4 / 8) ** 2 + (4 * ss[:, 1]) ** 2)
    nn = (ss[:, 0] ** 4 + ss[:, 1] ** 2 + ss[:, 2] ** 2) ** 0.25 if w == 2 else (ss[:, 0] ** 8 + ss[:, 1] ** 2 + ss[:, 2] ** 2) ** 0.125
    sel = nn <= rD
    if sel.any():
        mxr = max(mxr, float(np.max(np.abs(dHn[sel] - p4[sel]) / p4[sel])))
check("6c FLOAT: random points in the proven balls: det H > 0, eigenvalues (-,-,+,+); |R|/(64|d_lead|^2) < 1 (direct balls)",
      pos and hneg and mxr < 1, f"max |R|/P_lead = {mxr:.2e}")

def tay_num(tc, kappa, xyz):
    tot = np.zeros(len(xyz))
    for (p, q, r), v in tc.items():
        re, im = evalc(v, Fr(kappa).limit_denominator(10 ** 6))
        tot += float(re) * xyz[:, 0] ** p * xyz[:, 1] ** q * xyz[:, 2] ** r
    return tot


worst_lem = 0.0; worst_G = 0.0
for kv, rN, w, cs in ((Fr(1), Fr(19, 50), 2, "gen"), (Fr(1, 4), Fr(37, 100), 2, "gen"), (Fr(1, 2), Fr(1, 5), 4, "half")):
    cf = CASES[cs]
    big = rng.uniform(-0.9, 0.9, (300, 3))                       # large arguments: the Taylor remainder is far above rounding noise there
    for nm in ("Nx", "Ny", "Nz", "N0", "detC", "detH"):
        l = LPS[nm]
        F = lp_num(l, float(kv), big)
        T = tay_num(TC[nm], float(kv), big)
        keys = np.array(list(l.keys()), float)
        cm = np.array([float(modc(v, kv, False)) for v in l.values()])
        bound = (cm[None, :] * np.abs(big @ keys.T) ** (NTAY + 1)).sum(1) / factorial(NTAY + 1)
        worst_lem = max(worst_lem, float(np.max(np.abs(F - T) / (bound + 1e-9))))
    uu = rng.uniform(-1, 1, (300, 3)); uu = uu / np.maximum(1, np.linalg.norm(uu, axis=1, keepdims=True))
    pts = np.stack([float(rN) * uu[:, 0], float(rN) ** w * uu[:, 1], float(rN) ** w * uu[:, 2]], 1)
    nrm = (pts[:, 0] ** (2 * w) + pts[:, 1] ** 2 + pts[:, 2] ** 2) ** (1.0 / (2 * w))
    try:
        KG_, K0_, KC_, KR_ = all_K(cs, rN, kv, False)
    except AssertionError:
        worst_G = float("inf")
        continue
    for nm in ("Nx", "Ny", "Nz"):
        lead = {"Nx": -128 * (pts[:, 1] - pts[:, 2]), "Ny": (-64 * (1 - 4 * float(kv) ** 2) / 2 * pts[:, 0] ** 2) if cs == "gen" else -8 * pts[:, 0] ** 4,
                "Nz": (512 * float(kv) * pts[:, 1]) if cs == "gen" else 256 * pts[:, 1]}[nm]
        Gn = lp_num(LPS[nm], float(kv), pts) - lead
        worst_G = max(worst_G, float(np.max(np.abs(Gn) / nrm ** cf["LwG"] / float(KG_[nm]))))
check("6d FLOAT: |F - T_12 F| <= sum |c||nu.theta|^13/13! at 900 large-argument samples; |G_i|/(N^Lw K_i) < 1 in the balls",
      worst_lem <= 1 and worst_G < 1, f"max remainder ratio {worst_lem:.2e}; max |G|/(K N^Lw) = {worst_G:.2e}")

# ================================================================================================ 7. the pair born at Gamma (kappa > 1/2)
kS, w_s, t_s = sp.symbols("k w t", positive=True)
cw_ = (w_s + 1 / w_s) / 2
claim = 16 * (cw_ - 1) ** 2 * (4 * kS ** 2 * (cw_ + 1) - 2) ** 2

def axis_of(l):
    return sum((v.as_expr().subs(sp.Symbol("k"), kS) * w_s ** key[0] for key, v in l.items()), sp.Integer(0))


axl = {nm: sp.expand(axis_of(LPS[nm])) for nm in LPS}
Mz = sp.zeros(4, 4)
for (a, b, n, kind) in TERMS:
    tt = {"x": 2, "y": 2, "z": 4, "odd": 2 * kS}[kind]
    mon = w_s ** (n[0] - n[1])
    Mz[a, b] += tt * mon; Mz[b, a] -= tt / mon
Dy_axis = 4 * (cw_ - 1) * (2 * kS ** 2 * (cw_ + 1) - 1) / (cw_ + 3)
check("7a: exact on theta = x(1,-1,0): Nx = Nz = N0 = 0, detC = -4(cos x+3)^2, D_y = 4(cos x-1)(2k^2(cos x+1)-1)/(cos x+3); "
      "det H = 16(cos x-1)^2(4k^2(cos x+1)-2)^2 (Laurent + independent sympy det)",
      all(sp.simplify(axl[nm]) == 0 for nm in ("Nx", "Nz", "N0")) and sp.simplify(axl["detC"] + 4 * (cw_ + 3) ** 2) == 0 and sp.simplify(axl["Ny"] - Dy_axis * axl["detC"]) == 0
      and sp.expand(axl["detH"] - claim) == 0 and sp.simplify(sp.expand(sp.expand(Mz.det(method="berkowitz")) - claim)) == 0)
mS = sp.sqrt(4 * kS ** 2 - 1)
chk_tan = sp.simplify((1 - mS ** 2) / (1 + mS ** 2) - (1 / (2 * kS ** 2) - 1))
check("7b: second double root cos x0 = 1/(2k^2)-1 <=> tan(x0/2) = sqrt(4k^2-1): real and != 0 iff k > 1/2; f = +-(x0/2pi)(1,-1,0)",
      chk_tan == 0)
# exact rational parametrisation kappa = (t^2+1)/(4t), tan(x0/2) = (t^2-1)/(2t), e^{i x0} = -((1+it)/(1-it))^2
kap_t = (t_s ** 2 + 1) / (4 * t_s)
zeta = -((1 + sp.I * t_s) / (1 - sp.I * t_s)) ** 2
m_t = (t_s ** 2 - 1) / (2 * t_s)
c0 = 1 / (2 * kap_t ** 2) - 1
s0 = m_t / (2 * kap_t ** 2)
par_ok = sp.simplify(m_t ** 2 - (4 * kap_t ** 2 - 1)) == 0 and sp.simplify(zeta - (c0 + sp.I * s0)) == 0


def evl(l, d=(0, 0, 0), kapv=None, zet=None):
    """sum_nu (i nu)^d c_nu(kappa) zeta^a : value (d = 0) or partial derivative of the Laurent polynomial at (x0, 0, 0), e^{i x0} = zet"""
    kapv = kap_t if kapv is None else kapv
    zet = zeta if zet is None else zet
    tot = 0
    for (a, b, c), v in l.items():
        fac = (sp.I * a) ** d[0] * (sp.I * b) ** d[1] * (sp.I * c) ** d[2]
        if fac == 0:
            continue
        tot += v.as_expr().subs(sp.Symbol("k"), kapv) * fac * zet ** a
    return tot


def simp(e):
    return sp.factor(sp.simplify(sp.together(e)))


vals = {nm: simp(evl(LPS[nm])) for nm in ("Nx", "Ny", "Nz", "N0", "detC")}
Jm = sp.zeros(3, 3)
for i, nm in enumerate(("Nx", "Ny", "Nz")):
    for j in range(3):
        d = [0, 0, 0]; d[j] = 1
        Jm[i, j] = simp(evl(LPS[nm], tuple(d)))
detJN = simp(Jm.det())
detJD = simp(detJN / vals["detC"] ** 3)
formula = 256 * kap_t * m_t ** 3 * (1 - 2 * kap_t ** 2) / (4 * kap_t ** 2 + 1) ** 2
check("7c: exact, k = (t^2+1)/(4t), t > 1: at +x0(1,-1,0): Nx = Ny = Nz = N0 = 0 (S = 0, dim ker H = 2), detC < 0",
      par_ok and all(vals[nm] == 0 for nm in ("Nx", "Ny", "Nz", "N0")) and sp.simplify(vals["detC"] + 16 * (t_s ** 4 + 6 * t_s ** 2 + 1) ** 2 / (t_s ** 2 + 1) ** 4) == 0,
      "detC = -16(t^4+6t^2+1)^2/(t^2+1)^4")
check("7d: exact det J_D(+x0) = 256 k (4k^2-1)^(3/2) (1-2k^2)/(4k^2+1)^2; zero at k = 1/2 and 1/sqrt2; -x0 gives the negative",
      sp.simplify(detJD - formula) == 0, "t-form -16 (t^2-1)^3 (t^2+1)(t^4-6t^2+1)/(t^2 (t^4+6t^2+1)^2)")
# exact sign samples (rational t, exact Gaussian rational arithmetic)
sg = []
for tv in (Fr(101, 100), Fr(6, 5), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3), Fr(10)):
    tt_ = sp.Rational(tv.numerator, tv.denominator)
    kv_ = (tt_ ** 2 + 1) / (4 * tt_)
    z_ = -((1 + sp.I * tt_) / (1 - sp.I * tt_)) ** 2
    Jq = sp.zeros(3, 3)
    for i, nm in enumerate(("Nx", "Ny", "Nz")):
        for j in range(3):
            d = [0, 0, 0]; d[j] = 1
            Jq[i, j] = sp.expand(evl(LPS[nm], tuple(d), kv_, z_))
    dcq = sp.expand(evl(detC, (0, 0, 0), kv_, z_))
    val = sp.expand(Jq.det() / dcq ** 3)
    assert sp.im(val) == 0
    sg.append((float(kv_), int(sp.sign(sp.re(val))), int(sp.sign(1 - 2 * kv_ ** 2))))
check("7e: charge at +x0 = sign det J_D: +1 for 1/2 < k < 1/sqrt2, -1 beyond (exact at 7 rational kappa); -x0 opposite",
      all(a == b for (_, a, b) in sg), "kappa:charge " + " ".join(f"{kv:.4f}:{s1:+d}" for kv, s1, s2 in sg))
hh = sp.Symbol("s", positive=True)
ser = sp.series(2 * sp.atan(2 * hh * sp.sqrt(1 + hh ** 2)), hh, 0, 6).removeO()
check("7f: x0 = 2 arctan sqrt(4k^2-1) = 4 s - (10/3) s^3 + ..., s = sqrt(k - 1/2): leading x0 = 4 sqrt(k-1/2), det J_D = 128 (k-1/2)^(3/2)+..",
      sp.expand(ser.coeff(hh, 1) - 4) == 0 and sp.expand(ser.coeff(hh, 3) + sp.Rational(10, 3)) == 0 and sp.expand(ser.coeff(hh, 2)) == 0,
      f"series {sp.expand(ser)}")

# FLOAT pair: kernel, triple product, node degree, location
def Hd(th, kappa):
    amp = {"x": 2.0, "y": 2.0, "z": 4.0, "odd": 2.0 * kappa}
    M = np.zeros((4, 4), complex); dM = [np.zeros((4, 4), complex) for _ in range(3)]
    for (a, b, n, kind) in TERMS:
        ph = np.exp(1j * np.dot(n, th)); t_ = amp[kind]
        M[a, b] += t_ * ph; M[b, a] -= t_ * np.conj(ph)
        for l_ in range(3):
            dM[l_][a, b] += t_ * ph * 1j * n[l_]; dM[l_][b, a] -= t_ * np.conj(ph) * (-1j * n[l_])
    return 1j * M, [1j * d_ for d_ in dM]


fl_ok = True; info = []
for kv in (0.55, 0.6, 0.68, 0.75, 1.0):
    x0 = 2 * np.arctan(np.sqrt(4 * kv ** 2 - 1)); ex = np.sign(1 - 2 * kv ** 2)
    for sgn in (1, -1):
        th = sgn * x0 * np.array([1.0, -1.0, 0.0])
        H, dH = Hd(th, kv)
        evh, V = np.linalg.eigh(H)
        P = V[:, 1:3] @ V[:, 1:3].conj().T
        T = np.trace(P @ dH[0] @ P @ dH[1] @ P @ dH[2]).imag
        fl_ok = fl_ok and abs(evh[1]) < 1e-9 and abs(evh[2]) < 1e-9 and np.sign(T) == sgn * ex and abs(evh[0] + 8) < 1e-9
        info.append((kv, sgn, T))
dgn = []
for kv, sgn in ((0.55, 1), (0.55, -1), (0.6, 1)):
    x0 = 2 * np.arctan(np.sqrt(4 * kv ** 2 - 1))
    g_ = np.linspace(0, np.pi, 121)[:, None] * np.ones((1, 241)); h_ = np.ones((121, 1)) * np.linspace(0, 2 * np.pi, 241)[None, :]
    rr = 0.04
    sp_ = np.stack([sgn * x0 + rr * np.cos(g_), rr * np.sin(g_) * np.cos(h_), rr * np.sin(g_) * np.sin(h_)], -1)
    Dn, d0n, dCn, dHn = schur_num(sp_.reshape(-1, 3), kv)
    dgn.append(solid_degree(Dn.reshape(sp_.shape), 120, 240)[0])
check("7g FLOAT: kappa = .55,.6,.68,.75,1: eigenvalues at +-x0 are (-8,0,0,8), Im Tr(P d1H P d2H P d3H) sign = +-(1-2k^2); node degrees .55 (+x0,-x0), .6 (+x0)",
      fl_ok and abs(dgn[0] - 1) < 1e-6 and abs(dgn[1] + 1) < 1e-6 and abs(dgn[2] - 1) < 1e-6,
      "degrees " + ",".join(f"{d_:+.3f}" for d_ in dgn) + "; triple products at +x0: " + " ".join(f"{T:+.2f}" for (kv, sgn, T) in info if sgn == 1))
dl = 1e-4
for kv in (0.5 + dl,):
    x0n = 2 * np.arctan(np.sqrt(4 * kv ** 2 - 1)); lead = 4 * np.sqrt(kv - 0.5)
chkx = abs(x0n / lead - (1 - 5 * dl / 6)) < 1e-6
xg = [(kv, 2 * np.arctan(np.sqrt(4 * kv ** 2 - 1))) for kv in (0.55, 0.6, 0.68)]
cons = all(float(rho_formula(Fr(kv).limit_denominator(1000))) < x for kv, x in xg)
check("7h FLOAT: x0/(4 sqrt(k-1/2)) = 1 - (5/6)(k-1/2) to 1e-6 at k-1/2 = 1e-4; proven radius rho(k) < x0(k) at k = .55,.6,.68",
      chkx and cons, f"x0 = {','.join(f'{x:.3f}' for kv, x in xg)}; rho = " + ",".join(f"{float(rho_formula(Fr(kv).limit_denominator(1000))):.4f}" for kv, x in xg))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}   ({time.time() - T0:.0f} s)")
