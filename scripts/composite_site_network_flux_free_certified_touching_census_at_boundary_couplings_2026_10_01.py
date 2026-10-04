"""Node census of the supplied composite-network comparator at rational BOUNDARY couplings with Jx != Jy: Jz = Jx + Jy (degenerate point Gamma = (0,0,0)) and Jz = Jx - Jy
(degenerate point M = (1/2,1/2,0)).  There D = det M vanishes to fourth order at the degenerate point (semi-Dirac Pauli vector, singular Hessian), so the convexity box of the generic
census does not apply to it; it is excluded by an explicit Taylor-Lagrange quasi-ball (the zone-centre remainder method, adapted to Jx != Jy at rational couplings).

Supplied model: four-site Bloch matrix H(f) = i M(f); M(z) = sum over terms (a, b, n, t): M[a,b] += t z^n, M[b,a] -= t z^(-n), z_j = exp(2 pi i f_j); a middle-band touching is a zero of
D = det M (spec H = {+-l1, +-l2}, D = (l1 l2)^2).  Couplings (Jx, Jy, Jz; kappa), s = Jx + Jy, P = Jx Jy, u = kappa^2, E2 = 16 Jz^2.  Default run (seven couplings):
  G1 (6/5, 4/5, 2; 2/5)  u < P/4        G2 (6/5, 4/5, 2; 3/5)  P/4 < u < P/2        G3 (6/5, 4/5, 2; 4/5)  u > P/2        G4 (3/2, 1/2, 2; 3/4)  u > P/2
  M1 (6/5, 4/5, 2/5; 3/10)  no off-plane orbit      M2 (6/5, 4/5, 2/5; 3/5)  off-plane orbit      M3 (3/2, 1/2, 1; 3/2)  off-plane orbit.
Supplementary couplings (python3 bcensus_runner.py -n X1,X2): X1 (6/5, 4/5, 2; 7/10) just above u = P/2, X2 (6/5, 4/5, 2/5; 4/5).   -a runs all nine.
For each coupling:
  (1) BALL (exact Gaussian-rational arithmetic, Fractions, directed roundings): with theta - theta_b = x (1,-1,0) + y (1,1,0) + z (0,0,1), weights x:1, y,z:2, N^4 = x^4 + y^2 + z^2, the
      E = 0 Schur complement of H on ker H(0) gives Num = detC S (Laurent polynomials; det Num = detC det H exactly), Num = -E2 d_lead + G, d_lead = (2 Jy y - s z, a x^2, -8 kappa y), a = (P - 4u)/s
      at Gamma and (-2 Jy y - (Jx - Jy) z, a x^2, 4 kappa (2y - z)), a = -(P + 4u)/(Jx - Jy) at M; exact degree-12 Taylor coefficients show weight(G) >= 4, weight(N0) >= 5, weight(detC + E2) >= 2;
      Lagrange remainder bounds give K_G, K_0, K_Delta (exact rationals); (A) K_Delta rho^2 < E2, (B) K_G rho^2 < E2 s, (C) K_0 rho^3 + K_G rho^2 < E2 s with |d_lead| >= s N^2.  Then on 0 < N <= rho:
      detC < 0, Num has no zero and the homotopy -E2 d_lead + t G stays nonzero, |N0| < |Num|, so det H > 0: the degenerate point is the unique zero of D in the ball; deg = deg(d_lead/|d_lead|) = 0
      because d_y = a x^2 has the sign of a != 0 (omits a point of S^2).
  (2) EXACT (rings Q[alpha, t, d, i]/(...) off-plane orbit, Q[alpha, t, i]/(...) line factor): M has rank 2 at each node, Qp = a2 1 + M^2 is a rank-2 projector times a2, T = Im Tr(P d1H P d2H P d3H) is a
      ring element; the minimal polynomial Q of alpha = cos 2 pi f3 (PSLQ at 800 digits) is verified irreducible; relation identities of the orbit verified exactly.
  (3) INTERVAL (mpmath.iv at 300 bits, outward rounding): signs of T at all nodes, line charges against the closed form -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/Jz^3, Hessian-positive-definite boxes.
  (4) INTERVAL: clearing of the torus by dyadic cubes with the outward-rounded second-order Taylor lower bound of D; an uncleared cube lying inside a node box or inside the ball (inclusion tests
      with upward-rounded doubles) is accepted, every other one is split; the run ends when no cube is left outside the regions.  Cubes touching the degenerate point are uncleared (D = 0 there):
      their accepted ones lie inside the ball in all eight octants, a neighbourhood of the point.
Tiers: EXACT = rational / Gaussian-rational / ring arithmetic; INTERVAL = mpmath.iv or outward-rounded doubles; FLOAT lines (Laurent objects against a numpy Schur complement, solid angle and Fukui
flux of the two lowest bands on the quasi-sphere, sampled bounds, torus search) are consistency diagnostics.  The band reading of the degree of the Pauli map is an argument, not a machine proof.
Prints [PASS]/[FAIL] lines and TOTAL: PASS=N FAIL=M.   Run: nice -n 15 python3 bcensus_runner.py   (single process; -v long form; -n G2,M1 subset; -a all nine couplings)."""
AUDIT_TIMEOUT_SEC = 300
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import math
import itertools
import functools
from fractions import Fraction as Fr
from math import factorial, isqrt
import numpy as np
import sympy as sp
import mpmath as mp
from mpmath import iv
from mpmath.libmp import to_rational
from sympy import QQ, QQ_I

T0 = time.time()
VERBOSE = "-v" in sys.argv
PASS = 0
FAIL = 0
OUT_BYTES = 0

def emit(s):
    global OUT_BYTES
    OUT_BYTES += len(s) + 1
    print(s, flush=True)

def vemit(s):
    if VERBOSE: emit(s)

def check(ok, label, detail):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    emit("[%s] %s: %s" % ("PASS" if ok else "FAIL", label, detail))

# ---------------------------------------------------------------- embedded data
TERMS = [(0, 1, (-1, 0, 0), "y"), (0, 1, (0, 0, 0), "x"), (0, 3, (0, 0, -1), "z"), (1, 1, (-1, 0, 0), "odd"), (1, 3, (1, 0, -1), "odd"),
         (3, 1, (0, 0, 1), "odd"), (0, 0, (1, 0, 0), "odd"), (0, 2, (-1, 0, 0), "odd"), (2, 0, (0, 0, 0), "odd"), (2, 3, (0, -1, 0), "y"),
         (2, 3, (0, 0, 0), "x"), (2, 1, (0, 0, 0), "z"), (3, 3, (0, -1, 0), "odd"), (3, 1, (0, 1, 0), "odd"), (1, 3, (0, 0, 0), "odd"),
         (2, 2, (0, 1, 0), "odd"), (2, 0, (0, -1, 1), "odd"), (0, 2, (0, 0, -1), "odd")]
COUPLINGS = {  # (Jx, Jy, Jz, kappa) exact rationals
    "G1": (Fr(6, 5), Fr(4, 5), Fr(2, 1), Fr(2, 5)),
    "G2": (Fr(6, 5), Fr(4, 5), Fr(2, 1), Fr(3, 5)),
    "G3": (Fr(6, 5), Fr(4, 5), Fr(2, 1), Fr(4, 5)),
    "G4": (Fr(3, 2), Fr(1, 2), Fr(2, 1), Fr(3, 4)),
    "M1": (Fr(6, 5), Fr(4, 5), Fr(2, 5), Fr(3, 10)),
    "M2": (Fr(6, 5), Fr(4, 5), Fr(2, 5), Fr(3, 5)),
    "M3": (Fr(3, 2), Fr(1, 2), Fr(1, 1), Fr(3, 2)),
    "X1": (Fr(6, 5), Fr(4, 5), Fr(2, 1), Fr(7, 10)),
    "X2": (Fr(6, 5), Fr(4, 5), Fr(2, 5), Fr(4, 5)),
}
DEFAULT = ("G1", "G2", "G3", "G4", "M1", "M2", "M3")
KIND = {"G1": "G", "G2": "G", "G3": "G", "G4": "G", "X1": "G", "M1": "M", "M2": "M", "M3": "M", "X2": "M"}   # G: Jz = Jx + Jy, base point Gamma; M: Jz = Jx - Jy, base point (1/2, 1/2, 0)
BALL = {"G1": Fr(236, 1000), "G2": Fr(236, 1000), "G3": Fr(34, 100), "G4": Fr(35, 100), "M1": Fr(29, 100), "M2": Fr(20, 100), "M3": Fr(175, 1000),
        "X1": Fr(30, 100), "X2": Fr(15, 100)}   # rho of the quasi-ball N <= rho
# off-plane orbits found by PSLQ (800 digits): integer polynomial Q of alpha = cos 2 pi f3 (descending), relation lists (ascending powers, (num, den)) for
# sigma = c1 + c2, pi = c1 c2, r12 = s1 s2, w = s3 (s1 + s2), and one image (ts, ds, 8-digit centre of (f1, f2, f3) over 1e8), ts = sign s3, ds = sign (c1 - c2)
OFF = {
    "G3": [
        dict(Q=[273, -1225, 2171, -931],
             image=(1, 1, (19829121, 77230185, 14547274)),
             rel={
                 "sigma": [(263, 200), (-42, 25), (91, 200)],
                 "pi": [(287, 4800), (-1, 75), (-91, 4800)],
                 "r12": [(-7147, 4800), (673, 600), (-1729, 4800)],
                 "w": [(373, 600), (-239, 150), (511, 600)],
             }),
    ],
    "G4": [
        dict(Q=[4455, -29655, 67869, -36005],
             image=(1, 1, (17882077, 74382969, 11576508)),
             rel={
                 "sigma": [(6761, 4536), (-185, 108), (55, 168)],
                 "pi": [(-10285, 95256), (409, 2268), (-275, 3528)],
                 "r12": [(-163735, 95256), (3091, 2268), (-1265, 3528)],
                 "w": [(3391, 6804), (-211, 162), (185, 252)],
             }),
    ],
    "M2": [
        dict(Q=[-6615, -55167, 50702, 290526, -597815, 202145],
             image=(1, 1, (97019541, 55582994, 17881253)),
             rel={
                 "sigma": [(589034585, 1029406208), (-2185662965, 1544109312), (98689729, 193013664), (-72009833, 514703104), (-26523945, 1029406208)],
                 "pi": [(-52109261593, 37058623488), (24550267475, 18529311744), (-289559827, 514703104), (369568213, 2058812416), (129894345, 4117624832)],
                 "r12": [(-20836105925, 407644858368), (81716460295, 203822429184), (-1802641635, 5661734144), (285532289, 22646936576), (294008085, 45293873152)],
                 "w": [(6985665935, 8492601216), (-17472363805, 4246300608), (941283325, 353858384), (-276950961, 1415433536), (-190055565, 2830867072)],
             }),
    ],
    "M3": [
        dict(Q=[-4104, -11355, 12040, -6396, -38998, -6587],
             image=(1, 1, (96162096, 66394380, 27814568)),
             rel={
                 "sigma": [(2278837304, 26785366681), (-1089718096420, 562492700301), (76419958996, 80356100043), (-39865021328, 187497566767), (-31990078080, 187497566767)],
                 "pi": [(-16855543889, 6026707503225), (21410122359364, 8437390504515), (-7246092946796, 4687439169175), (2697230864464, 4687439169175), (1649175338304, 4687439169175)],
                 "r12": [(2596290320584, 6026707503225), (9382440551416, 8437390504515), (-4395442027624, 4687439169175), (193612275688, 669634167025), (840177490176, 4687439169175)],
                 "w": [(-580961988274, 401780500215), (-1005262387138, 562492700301), (1536509372782, 937487833835), (-351188481078, 937487833835), (-255630288528, 937487833835)],
             }),
    ],
    "X1": [
        dict(Q=[655473, -3805585, 8030351, -4814191],
             image=(1, 1, (24158714, 74719684, 3714643)),
             rel={
                 "sigma": [(757013, 533120), (-1239, 680), (4459, 10880)],
                 "pi": [(-3224923, 12794880), (41843, 114240), (-29029, 261120)],
                 "r12": [(-27720277, 12794880), (183677, 114240), (-109291, 261120)],
                 "w": [(498607, 399840), (-54209, 24990), (7441, 8160)],
             }),
    ],
    "X2": [
        dict(Q=[-1225, -11550, 5259, 44698, -78290, 20900],
             image=(1, 1, (93381703, 56468652, 19654767)),
             rel={
                 "sigma": [(35157485, 84062844), (-1206691471, 840628440), (445235927, 840628440), (-57503285, 336251376), (-8668345, 336251376)],
                 "pi": [(-410136575, 336251376), (4414411411, 3362513760), (-239325049, 420314220), (310453535, 1345005504), (44198245, 1345005504)],
                 "r12": [(45810823, 336251376), (581957809, 3362513760), (-279120827, 840628440), (88574465, 1345005504), (14699755, 1345005504)],
                 "w": [(-334576, 7005237), (-102299144, 35026185), (694202309, 280209480), (-9858275, 28020948), (-3873695, 56041896)],
             }),
    ],
}
NAMES = tuple(COUPLINGS.keys())
# node-box half-width in f units, as an integer over 10^8 (theta radius rho = 2 pi * value); default 5000
BOXRF = {"G1": 1000, "G2": 1000, "G3": 1000, "G4": 1000, "M1": 1000, "M2": 1000, "M3": 1000, "X1": 450, "X2": 1000}
CONTROL_AT = "G3"
E8 = 10 ** 8
KMAX = 25
BOXBIG = 1000000                                  # control: half-width 1e-2 (f units, over 1e8) at which the Hessian test must fail

# ---------------------------------------------------------------- the degenerate point: exact Laurent polynomials over Q(i), Schur complement on ker H(0), Taylor-Lagrange ball
NTAY = 12
def gq(a, b=0):
    a = Fr(a); b = Fr(b)
    return QQ_I(QQ(a.numerator, a.denominator), QQ(b.numerator, b.denominator))
ZERO = gq(0)
def to_fr(q): return Fr(int(q.numerator), int(q.denominator))
def up_sqrt(fr):
    P_, Q_ = fr.numerator, fr.denominator
    return Fr(isqrt(P_ * Q_) + 1, Q_)                       # >= sqrt(fr)
def lo_root(fr, n):
    """rational r <= fr^(1/n): floor of the integer n-th root of P Q^(n-1), over Q"""
    P_, Q_ = fr.numerator, fr.denominator
    M_ = P_ * Q_ ** (n - 1)
    lo, hi = 0, 1
    while hi ** n <= M_: hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** n <= M_: lo = mid
        else: hi = mid
    return Fr(lo, Q_)
def modq(v):
    """upper bound of the modulus of a Gaussian rational"""
    re, im = to_fr(v.x), to_fr(v.y)
    if im == 0: return abs(re)
    if re == 0: return abs(im)
    return up_sqrt(re * re + im * im)

class LP(dict):
    """Laurent polynomial in (e^{ix}, e^{iy}, e^{iz}): {(a, b, c): Gaussian rational}"""
    def __add__(s, o):
        r = LP(s)
        for key, v in o.items():
            w_ = r.get(key, ZERO) + v
            if w_ == ZERO: r.pop(key, None)
            else: r[key] = w_
        return r
    def __neg__(s): return LP({k: -v for k, v in s.items()})
    def __sub__(s, o): return s + (-o)
    def __mul__(s, o):
        if not isinstance(o, LP):
            return LP({k: v * o for k, v in s.items() if v * o != ZERO})
        r = {}
        for k1, v1 in s.items():
            for k2, v2 in o.items():
                key = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
                r[key] = r.get(key, ZERO) + v1 * v2
        return LP({k: v for k, v in r.items() if v != ZERO})

WV = [(1, 0, -1, 0), (0, 1, 0, -1)]                           # ker H(0) (both Gamma at Jz = Jx + Jy and M at Jz = Jx - Jy > 0)
UV = [(1, 0, 1, 0), (0, 1, 0, 1)]

def build_laurent(J, kind):
    """H = iM as 4x4 Laurent polynomials, theta - theta_b = x (1,-1,0) + y (1,1,0) + z (0,0,1), i.e. phase n.theta = (n1 - n2) x + (n1 + n2) y + n3 z; at M (theta_b = (pi, pi, 0))
    each term carries (-1)^(n1 + n2)."""
    jx, jy, jz, kp = J
    amp = {"x": 2 * jx, "y": 2 * jy, "z": 2 * jz, "odd": 2 * kp}
    Hm = [[LP() for _ in range(4)] for _ in range(4)]
    for (a, b, n, kd) in TERMS:
        sg = (-1 if (n[0] + n[1]) % 2 else 1) if kind == "M" else 1
        t = gq(amp[kd] * sg)
        fr = (n[0] - n[1], n[0] + n[1], n[2])
        Hm[a][b] = Hm[a][b] + LP({fr: gq(0, 1) * t})
        Hm[b][a] = Hm[b][a] + LP({(-fr[0], -fr[1], -fr[2]): gq(0, -1) * t})
    return Hm

def at0(l):
    s_ = ZERO
    for v in l.values(): s_ = s_ + v
    return s_

def schur_laurent(Hm):
    """blocks of T^T H T, T = [W U]/sqrt 2; Num = detC A - B adj(C) B^+ (2x2 hermitian), Pauli components (Nx, Ny, Nz, N0), detC, det H (24-term Laurent expansion), det Num."""
    hq = gq(Fr(1, 2))
    def blk(X, Y):
        out = [[LP(), LP()], [LP(), LP()]]
        for i in range(2):
            for j in range(2):
                acc = LP()
                for p in range(4):
                    for q in range(4):
                        c = X[i][p] * Y[j][q]
                        if c != 0: acc = acc + Hm[p][q] * (gq(c) * hq)
                out[i][j] = acc
        return out
    At, Bt, Ct, Bdt = blk(WV, WV), blk(WV, UV), blk(UV, UV), blk(UV, WV)
    detC = Ct[0][0] * Ct[1][1] - Ct[0][1] * Ct[1][0]
    adjC = [[Ct[1][1], -Ct[0][1]], [-Ct[1][0], Ct[0][0]]]
    mm = lambda X, Y: [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)] for i in range(2)]
    BadjBd = mm(mm(Bt, adjC), Bdt)
    Nm = [[detC * At[i][j] - BadjBd[i][j] for j in range(2)] for i in range(2)]
    def comb(pairs):
        out = LP()
        for l_, c_ in pairs: out = out + l_ * c_
        return out
    I_ = gq(0, 1)
    objs = dict(Nx=comb([(Nm[0][1], hq), (Nm[1][0], hq)]), Ny=comb([(Nm[0][1], I_ * hq), (Nm[1][0], -I_ * hq)]),
                Nz=comb([(Nm[0][0], hq), (Nm[1][1], -hq)]), N0=comb([(Nm[0][0], hq), (Nm[1][1], hq)]), detC=detC)
    detH = LP()
    for p_ in itertools.permutations(range(4)):
        sg = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if p_[i] > p_[j]: sg = -sg
        term = LP({(0, 0, 0): gq(sg)})
        for i in range(4): term = term * Hm[i][p_[i]]
        detH = detH + term
    objs["detH"] = detH
    detNum = Nm[0][0] * Nm[1][1] - Nm[0][1] * Nm[1][0]
    return objs, detNum

def taylor_coeffs(l, n):
    """exact Taylor coefficients (total degree <= n) at 0 in (x, y, z) of sum_nu c_nu e^{i nu.(x,y,z)}"""
    out = {}
    ipow = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    items = list(l.items())
    for p in range(n + 1):
        for q in range(n + 1 - p):
            for r in range(n + 1 - p - q):
                s_ = ZERO
                for key, v in items:
                    f = key[0] ** p * key[1] ** q * key[2] ** r
                    if f: s_ = s_ + v * gq(f)
                if s_ == ZERO: continue
                ip = ipow[(p + q + r) % 4]
                den = factorial(p) * factorial(q) * factorial(r)
                out[(p, q, r)] = s_ * gq(Fr(ip[0], den), Fr(ip[1], den))
    return out

def real_tc(tc):
    out = {}
    for k, v in tc.items():
        assert v.y == ZERO.y, "complex Taylor coefficient"
        out[k] = to_fr(v.x)
    return out

def wt(key, w=2): return key[0] + w * (key[1] + key[2])

def lead_forms(J, kind):
    """d_lead = (d_x, d_y, d_z) as {monomial: coefficient}, the coefficient a of x^2 in d_y, and the 2x2 matrix A of (y, z) -> (d_x, d_z)"""
    jx, jy, jz, kp = J
    s = jx + jy; P = jx * jy; u = kp * kp
    if kind == "G":      # Jz = Jx + Jy, Gamma
        a = (P - 4 * u) / s
        d = {"Nx": {(0, 1, 0): 2 * jy, (0, 0, 1): -s}, "Ny": {(2, 0, 0): a}, "Nz": {(0, 1, 0): -8 * kp}}
        A = [[2 * jy, -s], [-8 * kp, Fr(0)]]
    else:                # Jz = Jx - Jy > 0, M
        a = -(P + 4 * u) / (jx - jy)
        d = {"Nx": {(0, 1, 0): -2 * jy, (0, 0, 1): -(jx - jy)}, "Ny": {(2, 0, 0): a}, "Nz": {(0, 1, 0): 8 * kp, (0, 0, 1): -4 * kp}}
        A = [[-2 * jy, -(jx - jy)], [8 * kp, -4 * kp]]
    return a, d, A

def Kbound(l, g, Lw, rho, n=NTAY, w=2):
    """K with |F - P| <= K N^Lw on N <= rho (rho <= 1): g = Taylor_n(F) - P (every weight < Lw must vanish; assertion) plus the Lagrange remainder
    |e^{i phi} - T_n(phi)| <= |phi|^(n+1)/(n+1)!, |phi| <= N (|a| + (|b| + |c|) rho^(w-1)); exact rationals, square roots rounded up."""
    assert all(wt(key, w) >= Lw for key in g), "low-weight coefficient present"
    assert n + 1 >= Lw and rho <= 1
    tot = Fr(0)
    for key, v in g.items():
        tot += abs(v) * rho ** (wt(key, w) - Lw)
    rem_fac = rho ** (n + 1 - Lw) / factorial(n + 1)
    for (a, b, c), v in l.items():
        base = (abs(a) + (abs(b) + abs(c)) * rho ** (w - 1)) ** (n + 1)
        tot += modq(v) * base * rem_fac
    return tot

def ball_conditions(L, GG, E2, s, rho):
    """conditions (A) K_D rho^2 < E2, (B) K_G rho^2 < E2 s, (C) K_0 rho^3 + K_G rho^2 < E2 s; weight assertions are caught and reported as failure."""
    try:
        KG = {nm: Kbound(L[nm], GG[nm], 4, rho) for nm in ("Nx", "Ny", "Nz")}
        K0 = Kbound(L["N0"], GG["N0"], 5, rho)
        KC = Kbound(L["detC"], GG["detC"], 2, rho)
    except AssertionError:
        return False, False, False, dict(KG=0.0, K0=0.0, KC=0.0)
    KGn = up_sqrt(sum(v * v for v in KG.values()))
    return (KC * rho ** 2 < E2, KGn * rho ** 2 < E2 * s, K0 * rho ** 3 + KGn * rho ** 2 < E2 * s,
            dict(KG=float(KGn), K0=float(K0), KC=float(KC)))

def conj_lp(v): return QQ_I(v.x, -v.y)
def is_real_lp(l): return all(l.get((-k_[0], -k_[1], -k_[2]), ZERO) == conj_lp(v) for k_, v in l.items())

def poly_sumsq(lead):
    out = {}
    for comp in lead.values():
        for k1, c1 in comp.items():
            for k2, c2 in comp.items():
                key = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
                out[key] = out.get(key, Fr(0)) + c1 * c2
    return out

def fourier_to_laurent(aD, kind):
    """Fourier coefficients of D = det M (phases e^{i k.theta_total}) in the frame (x, y, z) around the base point: key (k1 - k2, k1 + k2, k3), sign (-1)^(k1 + k2) at M"""
    out = LP()
    for k, v in aD.items():
        key = (k[0] - k[1], k[0] + k[1], k[2])
        sg = -1 if (kind == "M" and (k[0] + k[1]) % 2) else 1
        out[key] = out.get(key, ZERO) + gq(v * sg)
    return out

def lp_num(l, xyz):
    """FLOAT value of a real Laurent polynomial at the points xyz = (x, y, z)"""
    keys = np.array(list(l.keys()), float)
    co = np.array([complex(float(to_fr(v.x)), float(to_fr(v.y))) for v in l.values()], complex)
    return (np.exp(1j * (xyz @ keys.T)) @ co).real

def ball_kfloat(objs, lead, E2, ks, s, rho, seed=5):
    """FLOAT: |Num + E2 d_lead| <= K_G N^4, |N0| <= K_0 N^5, |detC + E2| <= K_D N^2 and |d_lead| >= s N^2 at random points of the quasi-ball (N between rho/2 and rho);
    returns the largest ratio |F - P| / (K N^Lw) resp. s N^2 / |d_lead| (must be < 1; double precision with absolute tolerance 1e-11)."""
    rng = np.random.default_rng(seed)
    r_ = float(rho)
    a, b, c = (rng.uniform(-1, 1, 4000) for _ in range(3))
    sc = 1.0 / np.maximum(1.0, (a ** 4 + b ** 2 + c ** 2) ** 0.25)
    pts = np.stack([r_ * a * sc, r_ ** 2 * b * sc ** 2, r_ ** 2 * c * sc ** 2], 1)
    N = (pts[:, 0] ** 4 + pts[:, 1] ** 2 + pts[:, 2] ** 2) ** 0.25
    pts = pts[N >= r_ / 2]; N = N[N >= r_ / 2]
    def poly(d): return sum(float(cf) * pts[:, 0] ** k[0] * pts[:, 1] ** k[1] * pts[:, 2] ** k[2] for k, cf in d.items())
    G = np.sqrt(sum((lp_num(objs[nm], pts) + float(E2) * poly(lead[nm])) ** 2 for nm in ("Nx", "Ny", "Nz")))
    r1 = np.max(np.maximum(G - 1e-11, 0) / (ks["KG"] * N ** 4))
    r2 = np.max(np.maximum(np.abs(lp_num(objs["N0"], pts)) - 1e-11, 0) / (ks["K0"] * N ** 5))
    r3 = np.max(np.maximum(np.abs(lp_num(objs["detC"], pts) + float(E2)) - 1e-11, 0) / (ks["KC"] * N ** 2))
    dl = np.sqrt(sum(poly(lead[nm]) ** 2 for nm in ("Nx", "Ny", "Nz")))
    r4 = float(s) / float(np.min(dl / N ** 2))
    return float(max(r1, r2, r3, r4)), len(pts)

def hnum(J, kind, xyz):
    """FLOAT: H = iM at the points xyz = (x, y, z) around the base point (numpy)"""
    jx, jy, jz, kp = (float(v) for v in J)
    amp = {"x": 2 * jx, "y": 2 * jy, "z": 2 * jz, "odd": 2 * kp}
    th = np.stack([xyz[:, 0] + xyz[:, 1], -xyz[:, 0] + xyz[:, 1], xyz[:, 2]], 1)
    M = np.zeros((len(xyz), 4, 4), complex)
    for (a, b, n, kd) in TERMS:
        sg = (-1.0 if (n[0] + n[1]) % 2 else 1.0) if kind == "M" else 1.0
        ph = np.exp(1j * (th @ np.array(n, float)))
        M[:, a, b] += sg * amp[kd] * ph; M[:, b, a] -= sg * amp[kd] * np.conj(ph)
    return 1j * M

def sphere_grid(center, radii, m_th, m_ph):
    """grid (m_th + 1, m_ph + 1, 3) on the ellipsoid center + (r0 cos t, r1 sin t cos p, r2 sin t sin p)"""
    th = np.linspace(0, np.pi, m_th + 1)[:, None] * np.ones((1, m_ph + 1))
    ph = np.ones((m_th + 1, 1)) * np.linspace(0, 2 * np.pi, m_ph + 1)[None, :]
    return np.stack([center[0] + radii[0] * np.cos(th), center[1] + radii[1] * np.sin(th) * np.cos(ph), center[2] + radii[2] * np.sin(th) * np.sin(ph)], -1)

def fukui_grid(J, kind, grid):
    """FLOAT Fukui-Hatsugai-Suzuki flux of the two lowest bands of H through the closed surface grid (m_th + 1, m_ph + 1, 3): returns (flux/2 pi, max |plaquette phase|, min gap E3 - E2)."""
    sh = grid.shape
    ev, V = np.linalg.eigh(hnum(J, kind, grid.reshape(-1, 3)))
    gap = float(np.min(ev[:, 2] - ev[:, 1]))
    Vl = V[:, :, :2].reshape(sh[0], sh[1], 4, 2)
    def link(Va, Vb):
        O = np.einsum("...ia,...ib->...ab", np.conj(Va), Vb)
        dd = O[..., 0, 0] * O[..., 1, 1] - O[..., 0, 1] * O[..., 1, 0]
        return dd / np.abs(dd)
    fl = np.angle(link(Vl[:-1, :-1], Vl[1:, :-1]) * link(Vl[1:, :-1], Vl[1:, 1:]) * link(Vl[1:, 1:], Vl[:-1, 1:]) * link(Vl[:-1, 1:], Vl[:-1, :-1]))
    return float(fl.sum() / (2 * np.pi)), float(np.abs(fl).max()), gap

def ball_float(J, kind, objs, rho, seed=11):
    """FLOAT diagnostic: Laurent Pauli objects against a direct numpy Schur complement at random points of the ball (max |difference|), the solid-angle degree of D/|D| on the
    quasi-sphere N = rho (D = Num/detC), and the Fukui flux (Chern number) of the two lowest bands of the actual H through that sphere."""
    Wn = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]], float) / np.sqrt(2)
    Un = np.array([[1, 0], [0, 1], [1, 0], [0, 1]], float) / np.sqrt(2)
    def schur(xyz):
        H = hnum(J, kind, xyz)
        A = np.einsum("ia,mij,jb->mab", Wn, H, Wn); B = np.einsum("ia,mij,jb->mab", Wn, H, Un); C = np.einsum("ia,mij,jb->mab", Un, H, Un)
        S = A - B @ np.linalg.inv(C) @ np.conj(np.transpose(B, (0, 2, 1)))
        d0 = ((S[:, 0, 0] + S[:, 1, 1]) / 2).real; dz = ((S[:, 0, 0] - S[:, 1, 1]) / 2).real
        dx = ((S[:, 0, 1] + S[:, 1, 0]) / 2).real; dy = (1j * (S[:, 0, 1] - S[:, 1, 0]) / 2).real
        return np.stack([dx, dy, dz], 1), d0, np.linalg.det(C).real
    lpn = lp_num
    rng = np.random.default_rng(seed)
    r_ = float(rho)
    uu = rng.uniform(-1, 1, (300, 3)); uu = uu / np.maximum(1, np.linalg.norm(uu, axis=1, keepdims=True))
    pts = np.stack([r_ * uu[:, 0], r_ ** 2 * uu[:, 1], r_ ** 2 * uu[:, 2]], 1)
    Dn, d0n, dCn = schur(pts)
    dev = max(float(np.max(np.abs(lpn(objs["detC"], pts) - dCn))),
              max(float(np.max(np.abs(lpn(objs[nm], pts) - dCn * Dn[:, i]))) for i, nm in enumerate(("Nx", "Ny", "Nz"))),
              float(np.max(np.abs(lpn(objs["N0"], pts) - dCn * d0n))))
    m_th, m_ph = 80, 160
    # quasi-sphere N = rho, parametrised so that x^4 + y^2 + z^2 = rho^4
    th = np.linspace(0, np.pi, m_th + 1)[:, None] * np.ones((1, m_ph + 1))
    ph = np.ones((m_th + 1, 1)) * np.linspace(0, 2 * np.pi, m_ph + 1)[None, :]
    p_, q_, s2 = np.cos(th), np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph)
    sph = np.stack([r_ * np.sign(p_) * np.abs(p_) ** 0.5, r_ ** 2 * q_, r_ ** 2 * s2], -1)
    Dn, d0n, dCn = schur(sph.reshape(-1, 3))
    F = Dn.reshape(sph.shape)
    U = F / np.linalg.norm(F, axis=-1, keepdims=True)
    a_, b_, c_, d_ = U[:-1, :-1], U[1:, :-1], U[1:, 1:], U[:-1, 1:]
    def om(p, q, r):
        num = np.einsum("...i,...i", p, np.cross(q, r))
        den = 1 + np.einsum("...i,...i", p, q) + np.einsum("...i,...i", q, r) + np.einsum("...i,...i", r, p)
        return 2 * np.arctan2(num, den)
    deg = float((om(a_, b_, c_).sum() + om(a_, c_, d_).sum()) / (4 * np.pi))
    chern, maxfl, gap = fukui_grid(J, kind, sph)
    return dev, deg, float(np.max(dCn)), chern, maxfl, gap

def ball_check(name, aD, rho=None, tweak=None):
    """exact analysis of the degenerate point (see the module docstring); returns dict(ok, rho, detail, ...).  `tweak` (controls) perturbs the leading coefficient a."""
    J = COUPLINGS[name]; kind = KIND[name]
    rho = BALL[name] if rho is None else rho
    jx, jy, jz, kp = J
    E2 = 16 * jz * jz
    Hm = build_laurent(J, kind)
    H0 = [[at0(Hm[i][j]) for j in range(4)] for i in range(4)]
    W_ = [[gq(c) for c in w] for w in WV]
    kerok = all(sum((H0[i][j] * W_[a][j] for j in range(4)), ZERO) == ZERO for i in range(4) for a in range(2))
    Pk = [[gq(Fr(sum(WV[a][i] * WV[a][j] for a in range(2)), 2)) for j in range(4)] for i in range(4)]
    H2 = [[sum((H0[i][k] * H0[k][j] for k in range(4)), ZERO) for j in range(4)] for i in range(4)]
    sq_ok = all(H2[i][j] == gq(E2) * (gq(1 if i == j else 0) - Pk[i][j]) for i in range(4) for j in range(4))
    objs, detNum = schur_laurent(Hm)
    detC, detH = objs["detC"], objs["detH"]
    id_ok = (detNum - detC * detH) == LP()
    base_ok = at0(detC) == gq(-E2) and all(at0(objs[nm]) == ZERO for nm in ("Nx", "Ny", "Nz", "N0"))
    fou_ok = fourier_to_laurent(aD, kind) == detH
    real_ok = all(is_real_lp(l) for l in objs.values())
    a, lead, A = lead_forms(J, kind)
    if tweak: a = a * tweak; lead["Ny"] = {(2, 0, 0): a}
    TR = {nm: real_tc(taylor_coeffs(objs[nm], NTAY)) for nm in objs}
    GG = {}
    for nm in ("Nx", "Ny", "Nz"):
        g = dict(TR[nm])
        for key, v in lead[nm].items():
            g[key] = g.get(key, Fr(0)) + E2 * v                    # Num = -E2 d_lead + G
            if g[key] == 0: g.pop(key)
        GG[nm] = g
    GG["N0"] = TR["N0"]
    gC = dict(TR["detC"]); gC[(0, 0, 0)] = gC.get((0, 0, 0), Fr(0)) + E2
    if gC[(0, 0, 0)] == 0: gC.pop((0, 0, 0))
    GG["detC"] = gC
    gR = dict(TR["detH"])
    for key, v in poly_sumsq(lead).items():
        gR[key] = gR.get(key, Fr(0)) - E2 * v                      # det H = E2 |d_lead|^2 + R
        if gR[key] == 0: gR.pop(key)
    wmin = lambda g: min([wt(k) for k in g], default=99)
    wts = (min(wmin(GG[nm]) for nm in ("Nx", "Ny", "Nz")), wmin(GG["N0"]), wmin(GG["detC"]), wmin(gR))
    wts_ok = wts[0] >= 4 and wts[1] >= 5 and wts[2] >= 2 and wts[3] >= 6
    detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    lam = detA ** 2 / sum(A[i][j] ** 2 for i in range(2) for j in range(2))      # lambda_min(A^T A) >= det/trace
    m_ = min(a * a, lam)
    s = lo_root(m_ * 10 ** 12, 2) / 10 ** 6 if m_ > 0 else Fr(0)                  # s^2 <= min(a^2, lambda_min), |d_lead| >= s N^2
    cA, cB, cC, ks = ball_conditions(objs, GG, E2, s, rho)
    deg_ok = a != 0 and s > 0
    dev, fdeg, dcmax, chern, maxfl, gap = ball_float(J, kind, objs, rho)
    kfl, npts = ball_kfloat(objs, lead, E2, ks, s, rho)
    ok = kfl < 0.9999 and kerok and sq_ok and id_ok and base_ok and fou_ok and real_ok and wts_ok and cA and cB and cC and deg_ok and abs(fdeg) < 1e-6 and dev < 1e-8 and dcmax < 0 and abs(chern) < 1e-6 and maxfl < 2.5 and gap > 0
    return dict(ok=ok, rho=rho, ks=ks, s=s, a=a, wts=wts, flags=(kerok, sq_ok, id_ok, base_ok, fou_ok, real_ok, wts_ok, cA, cB, cC, deg_ok),
                dev=dev, fdeg=fdeg, E2=E2, kind=kind, kfl=kfl, chern=chern, maxfl=maxfl, gap=gap)

# ---------------------------------------------------------------- exact tower arithmetic
class Field:
    """K = Q[alpha]/(q), q given by integer coefficients in ascending order (degree n >= 1); elements are tuples of Fractions."""
    def __init__(self, q_asc):
        self.n = len(q_asc) - 1
        lead = Fr(q_asc[-1])
        self.mon = [Fr(c) / lead for c in q_asc]
    def zero(self): return tuple(Fr(0) for _ in range(self.n))
    def one(self): return tuple([Fr(1)] + [Fr(0)] * (self.n - 1))
    def const(self, c): return tuple([Fr(c)] + [Fr(0)] * (self.n - 1))
    def alpha(self):
        if self.n == 1: return (-self.mon[0],)
        return tuple([Fr(0), Fr(1)] + [Fr(0)] * (self.n - 2))
    def add(self, a, b): return tuple(x + y for x, y in zip(a, b))
    def sub(self, a, b): return tuple(x - y for x, y in zip(a, b))
    def neg(self, a): return tuple(-x for x in a)
    def smul(self, c, a): return tuple(Fr(c) * x for x in a)
    def mul(self, a, b):
        n = self.n
        prod = [Fr(0)] * (2 * n - 1)
        for i, x in enumerate(a):
            if x == 0: continue
            for j, y in enumerate(b):
                if y != 0: prod[i + j] += x * y
        for k in range(2 * n - 2, n - 1, -1):
            c = prod[k]
            if c != 0:
                for j in range(n + 1):
                    prod[k - n + j] -= c * self.mon[j]
        return tuple(prod[:n])
    def is_zero(self, a): return all(x == 0 for x in a)
    def poly(self, coeffs_asc):
        r = self.zero(); p = self.one()
        for c in coeffs_asc:
            r = self.add(r, self.smul(c, p)); p = self.mul(p, self.alpha())
        return r
    def inv(self, a):
        x = sp.symbols("x")
        qa = sp.Poly(sum(sp.Rational(c.numerator, c.denominator) * x**j for j, c in enumerate(self.mon)), x)
        pa = sp.Poly(sum(sp.Rational(c.numerator, c.denominator) * x**j for j, c in enumerate(a)), x)
        s, t, g = sp.gcdex(pa, qa)
        assert g.degree() == 0, "element not invertible"
        res = (s * (1 / g.as_expr())).rem(qa)
        co = res.all_coeffs()[::-1]
        co = [Fr(int(sp.Rational(c).p), int(sp.Rational(c).q)) for c in co] + [Fr(0)] * (self.n - len(co))
        return tuple(co[:self.n])

class Ring:
    """R = K[t, d, i]/(t^2 - T, d^2 - Dc, i^2 + 1); elements are dicts {(et, ed, ei): K-element}."""
    def __init__(self, K, T, Dc):
        self.K, self.T, self.Dc = K, T, Dc
    def zero(self): return {}
    def lift(self, k): return {(0, 0, 0): k}
    def gen(self, which):
        return {{"t": (1, 0, 0), "d": (0, 1, 0), "i": (0, 0, 1)}[which]: self.K.one()}
    def clean(self, a): return {k: v for k, v in a.items() if not self.K.is_zero(v)}
    def add(self, a, b):
        r = dict(a)
        for k, v in b.items():
            r[k] = self.K.add(r[k], v) if k in r else v
        return self.clean(r)
    def sub(self, a, b): return self.add(a, self.smul(-1, b))
    def smul(self, c, a): return {k: self.K.smul(c, v) for k, v in a.items()}
    def kmul(self, kel, a): return self.clean({k: self.K.mul(kel, v) for k, v in a.items()})
    def mul(self, a, b):
        r = {}
        K = self.K
        for k1, v1 in a.items():
            for k2, v2 in b.items():
                v = K.mul(v1, v2)
                et, ed, ei = k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2]
                if et == 2: v = K.mul(v, self.T); et = 0
                if ed == 2: v = K.mul(v, self.Dc); ed = 0
                if ei == 2: v = K.neg(v); ei = 0
                key = (et, ed, ei)
                r[key] = K.add(r[key], v) if key in r else v
        return self.clean(r)
    def is_zero(self, a): return len(self.clean(a)) == 0

# ---------------------------------------------------------------- symbolic Bloch matrix (couplings symbolic) and exact Fourier data
Jx, Jy, Jz, kap = sp.symbols("Jx Jy Jz kappa", positive=True)
z1, z2, z3 = sp.symbols("z1 z2 z3")

def srat(q):
    q = Fr(q); return sp.Rational(q.numerator, q.denominator)

def build_M_sym():
    amp = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kap}
    M = sp.zeros(4, 4)
    for (a, b, n, kind) in TERMS:
        mon = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += amp[kind] * mon
        M[b, a] -= amp[kind] / mon
    return M

def build_M(J):
    """M at exact rational couplings J = (Jx, Jy, Jz, kappa)"""
    return build_M_sym().subs({Jx: srat(J[0]), Jy: srat(J[1]), Jz: srat(J[2]), kap: srat(J[3])}).applyfunc(sp.expand)

def fourier_sym(expr):
    """Fourier coefficients {k: a_k(couplings)} of a Laurent polynomial with exponents in [-3, 3]"""
    P = sp.Poly(sp.expand(sp.expand(expr) * z1**3 * z2**3 * z3**3), z1, z2, z3)
    return {(a - 3, b - 3, c - 3): v for (a, b, c), v in P.terms()}

def tcoeffs(expr):
    """exact Fourier coefficients {k: a_k} (Fractions) of a Laurent polynomial with rational coefficients"""
    return {k: Fr(int(sp.Rational(v).p), int(sp.Rational(v).q)) for k, v in fourier_sym(expr).items()}

def sym_setup():
    """symbolic checks (a): M anti-Hermitian on the torus, char poly mu^4 + a2 mu^2 + D (no mu^3, mu^1 term); returns (ok, Fourier dicts of D and a2 in the couplings)"""
    Ms = build_M_sym()
    mu = sp.symbols("mu")
    Minv = Ms.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True)
    ah = (Ms + Minv.T).applyfunc(sp.expand) == sp.zeros(4, 4)
    cp = sp.Poly(sp.expand((mu * sp.eye(4) - Ms).det(method="berkowitz")), mu)
    co = {e[0]: sp.expand(c) for e, c in cp.terms()}
    ok = ah and co.get(3, 0) == 0 and co.get(1, 0) == 0 and co[4] == 1
    return ok, fourier_sym(co[0]), fourier_sym(co[2])

def coeffs_at(J, dd):
    sub = {Jx: srat(J[0]), Jy: srat(J[1]), Jz: srat(J[2]), kap: srat(J[3])}
    out = {}
    for k, v in dd.items():
        r = sp.Rational(sp.expand(v.subs(sub)))
        if r != 0: out[k] = Fr(int(r.p), int(r.q))
    return out

# ---------------------------------------------------------------- the off-plane orbit and line points in their rings
def offplane_point(orb, q5=None, flip_s2=False):
    """Ring R and point (z, zi) of the off-plane orbit `orb` (dict Q, rel); relation identities returned as a flag."""
    q5 = orb["Q"] if q5 is None else q5
    rel = {kq: [Fr(n, d) for (n, d) in orb["rel"][kq]] for kq in orb["rel"]}
    K = Field(list(reversed(q5)))
    sigma = K.poly(rel["sigma"]); pi_ = K.poly(rel["pi"]); r12 = K.poly(rel["r12"]); w = K.poly(rel["w"])
    alpha = K.alpha()
    T = K.sub(K.one(), K.mul(alpha, alpha))
    Dc = K.sub(K.mul(sigma, sigma), K.smul(4, pi_))
    R = Ring(K, T, Dc)
    t, d, I = R.gen("t"), R.gen("d"), R.gen("i")
    half = Fr(1, 2)
    c3 = R.lift(alpha); s3 = t
    c1 = R.smul(half, R.add(R.lift(sigma), d)); c2 = R.smul(half, R.sub(R.lift(sigma), d))
    winv = K.inv(w); Tinv = K.inv(T)
    sp_ = R.kmul(K.mul(w, Tinv), t)
    sm_ = R.kmul(K.neg(K.mul(sigma, winv)), R.mul(d, t))
    s1 = R.smul(half, R.add(sp_, sm_)); s2 = R.smul(half, R.sub(sp_, sm_))
    if flip_s2: s2 = R.smul(-1, s2)
    one = R.lift(K.one())
    rel_ok = (R.is_zero(R.sub(R.mul(c1, c2), R.lift(pi_))) and R.is_zero(R.sub(R.mul(s1, s2), R.lift(r12)))
              and R.is_zero(R.sub(R.mul(s3, R.add(s1, s2)), R.lift(w)))
              and R.is_zero(R.sub(R.add(R.mul(c1, c1), R.mul(s1, s1)), one)) and R.is_zero(R.sub(R.add(R.mul(c2, c2), R.mul(s2, s2)), one))
              and R.is_zero(R.sub(R.add(R.mul(c3, c3), R.mul(s3, s3)), one)))
    z = [R.add(c1, R.mul(I, s1)), R.add(c2, R.mul(I, s2)), R.add(c3, R.mul(I, s3))]
    zi = [R.sub(c1, R.mul(I, s1)), R.sub(c2, R.mul(I, s2)), R.sub(c3, R.mul(I, s3))]
    return R, z, zi, rel_ok, rel, q5

def line_point(qfac_asc):
    """Ring R over K = Q[alpha]/(qfac) and the line point z = (alpha + i t, alpha - i t, 1), t^2 = 1 - alpha^2."""
    K = Field(qfac_asc)
    alpha = K.alpha()
    T = K.sub(K.one(), K.mul(alpha, alpha))
    R = Ring(K, T, K.one())
    t, I = R.gen("t"), R.gen("i")
    c = R.lift(alpha); one = R.lift(K.one())
    z = [R.add(c, R.mul(I, t)), R.sub(c, R.mul(I, t)), one]
    zi = [R.sub(c, R.mul(I, t)), R.add(c, R.mul(I, t)), one]
    return R, z, zi

# ---------------------------------------------------------------- exact root isolation
def roots_in_unit(coeffs_desc):
    """Enclosures (iv, from exact rational isolating intervals of width <= 1e-50) of ALL real roots of the integer polynomial in [-1, 1];
    asserts that no isolating interval straddles +-1."""
    x = sp.symbols("x")
    deg = len(coeffs_desc) - 1
    P = sp.Poly(sum(c * x ** (deg - j) for j, c in enumerate(coeffs_desc)), x)
    out = []
    for (a_, b_), _m in P.intervals(eps=sp.Rational(1, 10**50)):
        a_ = sp.Rational(a_); b_ = sp.Rational(b_)
        assert not (a_ < -1 < b_ or a_ < 1 < b_ or a_ == b_ and abs(a_) == 1), "root at the boundary"
        if a_ >= -1 and b_ <= 1:
            lo, hi = Fr(int(a_.p), int(a_.q)), Fr(int(b_.p), int(b_.q))
            Xlo = fr_iv(lo); Xhi = fr_iv(hi)
            X = iv.make_mpf((Xlo._mpi_[0], Xhi._mpi_[1]))
            assert lo_fr(X) <= lo and hi_fr(X) >= hi
            out.append(X)
    return out

def line_quadratic(J, kind):
    """q(c) = 4k^2 c^2 - 2 Jx Jy c + Jz^2 - Jx^2 - Jy^2 - 4k^2 over Z.  On Jz = Jx + Jy (kind G) the root c = 1 of q is the degenerate point Gamma, on Jz = Jx - Jy (kind M) the root c = -1
    is the point M: that factor c -/+ 1 is removed (`removed`: present with multiplicity one).  Returns (integer coefficients, number of distinct roots in [-1, 1] of the remaining factors,
    integer coefficient lists (descending) of the remaining irreducible factors that have a root in [-1, 1], removed)."""
    jx, jy, jz, kk = J
    cf = [4 * kk * kk, -2 * jx * jy, jz * jz - jx * jx - jy * jy - 4 * kk * kk]
    den = functools.reduce(lambda a, b: a * b // math.gcd(a, b), (c.denominator for c in cf), 1)
    ci = [int(c * den) for c in cf]
    c_ = sp.symbols("c")
    P = sp.Poly(ci[0] * c_**2 + ci[1] * c_ + ci[2], c_)
    bpoly = sp.Poly(c_ - 1 if kind == "G" else c_ + 1, c_)
    facs = []; nroots = 0; removed = False
    for fpoly, mult in sp.factor_list(P.as_expr())[1]:
        fp = sp.Poly(fpoly, c_)
        if fp == bpoly or fp == -bpoly:
            removed = (mult == 1)
            continue
        k_ = fp.count_roots(-1, 1)
        if k_ >= 1:
            assert mult == 1
            cs = [int(v) for v in fp.all_coeffs()]
            g = functools.reduce(math.gcd, cs)
            facs.append([v // g for v in cs])
            nroots += k_
    return ci, nroots, facs, removed

# ---------------------------------------------------------------- exact analysis of a point of the torus given by (cos, sin) ring elements
def make_eval(R, z, zi):
    one = R.lift(R.K.one())
    pw = {}
    def pw_get(j, e):
        if e == 0: return one
        if (j, e) not in pw:
            base = z[j] if e > 0 else zi[j]
            r = one
            for _ in range(abs(e)): r = R.mul(r, base)
            pw[(j, e)] = r
        return pw[(j, e)]
    def eval_laurent(expr):
        P = sp.Poly(sp.expand(sp.expand(expr) * z1**3 * z2**3 * z3**3), z1, z2, z3)
        out = R.zero()
        for (a_, b_, c_), co in P.terms():
            term = R.mul(R.mul(pw_get(0, a_ - 3), pw_get(1, b_ - 3)), pw_get(2, c_ - 3))
            out = R.add(out, R.smul(Fr(int(co.p), int(co.q)), term))
        return out
    return eval_laurent

def node_exact(Mr, R, z, zi):
    """Exact ring analysis at the point z = (cos + i sin).  Returns (flags, data)."""
    K = R.K
    ev = make_eval(R, z, zi)
    Mv = [[ev(Mr[a_, b_]) for b_ in range(4)] for a_ in range(4)]
    Nv = []
    for zj in (z1, z2, z3):
        Nj = Mr.applyfunc(lambda e: sp.expand(zj * sp.diff(e, zj)))
        Nv.append([[ev(Nj[a_, b_]) for b_ in range(4)] for a_ in range(4)])
    mm = R.mul
    def det3(rows, cols):
        m = [[Mv[r][c] for c in cols] for r in rows]
        t1 = mm(m[0][0], R.sub(mm(m[1][1], m[2][2]), mm(m[1][2], m[2][1])))
        t2 = mm(m[0][1], R.sub(mm(m[1][0], m[2][2]), mm(m[1][2], m[2][0])))
        t3 = mm(m[0][2], R.sub(mm(m[1][0], m[2][1]), mm(m[1][1], m[2][0])))
        return R.add(R.sub(t1, t2), t3)
    nz = sum(0 if R.is_zero(det3(rr, cc)) else 1 for rr in itertools.combinations(range(4), 3) for cc in itertools.combinations(range(4), 3))
    det = R.zero()
    for c in range(4):
        cols = [x_ for x_ in range(4) if x_ != c]
        det = R.add(det, R.smul(1 if c % 2 == 0 else -1, R.mul(Mv[0][c], det3((1, 2, 3), cols))))
    tr = R.zero()
    for a_ in range(4): tr = R.add(tr, Mv[a_][a_])
    a2 = R.zero()
    for a_, b_ in itertools.combinations(range(4), 2):
        a2 = R.add(a2, R.sub(R.mul(Mv[a_][a_], Mv[b_][b_]), R.mul(Mv[a_][b_], Mv[b_][a_])))
    def mmul(A, B):
        return [[functools.reduce(R.add, [R.mul(A[i][k], B[k][j]) for k in range(4)], R.zero()) for j in range(4)] for i in range(4)]
    M2 = mmul(Mv, Mv)
    Qp = [[R.add(M2[i][j], a2 if i == j else R.zero()) for j in range(4)] for i in range(4)]
    Q2 = mmul(Qp, Qp); MQ = mmul(Mv, Qp)
    trQ = R.zero()
    for i in range(4): trQ = R.add(trQ, Qp[i][i])
    A1, A2_, A3 = (mmul(Qp, Nv[j]) for j in range(3))
    A12 = mmul(A1, A2_)
    trace = R.zero()
    for i in range(4):
        for k in range(4):
            trace = R.add(trace, R.mul(A12[i][k], A3[k][i]))
    flags = dict(minors=(nz == 0), det=R.is_zero(det), tr=R.is_zero(tr), a2K=(set(a2.keys()) <= {(0, 0, 0)} and not R.is_zero(a2)),
                 Q2=all(R.is_zero(R.sub(Q2[i][j], R.mul(a2, Qp[i][j]))) for i in range(4) for j in range(4)),
                 MQ=all(R.is_zero(MQ[i][j]) for i in range(4) for j in range(4)),
                 trQ=R.is_zero(R.sub(trQ, R.smul(2, a2))))
    return flags, dict(a2=a2.get((0, 0, 0), K.zero()), trace=trace, nz=nz)

# ---------------------------------------------------------------- interval helpers (mpmath.iv, outward rounding)
def lo_fr(xv):
    p, q = to_rational(xv._mpi_[0]); return Fr(p, q)
def hi_fr(xv):
    p, q = to_rational(xv._mpi_[1]); return Fr(p, q)
def fr_iv(q):
    q = Fr(q); return iv.mpf(q.numerator) / iv.mpf(q.denominator)
def up_abs(xv): return max(abs(lo_fr(xv)), abs(hi_fr(xv)))

def kval(el, X):
    s_ = iv.mpf(0)
    for cf in reversed(el): s_ = s_ * X + fr_iv(cf)
    return s_

def ring_iv(elem, X, tval, dval):
    re = iv.mpf(0); im = iv.mpf(0)
    for (et, ed, ei), el in elem.items():
        val = kval(el, X) * (tval ** et) * (dval ** ed)
        if ei == 0: re += val
        else: im += val
    return re, im

def charge_iv(trace, a2el, X, tval, dval):
    """T = Im Tr(P d1H P d2H P d3H) = -8 pi^3 Im Tr(Qp N Qp N Qp N)/a2^3 as an iv enclosure."""
    re, im = ring_iv(trace, X, tval, dval)
    a2v = kval(a2el, X)
    return -8 * iv.pi ** 3 * im / a2v ** 3, a2v, re

def offplane_iv(X, rel, tsign, dsign):
    """iv enclosures of ((c1, s1), (c2, s2), (c3, s3)) at the root X for the image (tsign, dsign) and the positivity flags of t^2, d^2."""
    sigma, pi_, w = (kval(rel[k], X) for k in ("sigma", "pi", "w"))
    T = 1 - X * X; Dc = sigma * sigma - 4 * pi_
    if not (lo_fr(T) > 0 and lo_fr(Dc) > 0): return None
    t = tsign * iv.sqrt(T); d = dsign * iv.sqrt(Dc)
    c1 = (sigma + d) / 2; c2 = (sigma - d) / 2
    sp_ = w * t / T; sm_ = -sigma * d * t / w
    return [(c1, (sp_ + sm_) / 2), (c2, (sp_ - sm_) / 2), (X, t)]

def dev_arc(zst, f0):
    """Upper bound (Fraction) of max_j |theta*_j - theta0_j| (arc), theta0 = 2 pi f0/10^8, from the enclosures of cos, sin of theta*_j:
    arc <= (pi/2) chord."""
    PI = iv.pi
    out = Fr(0)
    for (cj, sj), n in zip(zst, f0):
        th = 2 * PI * fr_iv(Fr(n, E8))
        dc = cj - iv.cos(th); ds = sj - iv.sin(th)
        out = max(out, up_abs(PI / 2 * iv.sqrt(dc * dc + ds * ds)))
    return out

def hess_box(aD, aA, f0, rf, zst):
    """Hessian-PD certificate of D on the theta-box of half-width rho = 2 pi rf around f0 (rf: Fraction in f units).
    Returns dict(pivmin, eta, dev, rho, a2low)."""
    PI = iv.pi
    rho_iv = 2 * PI * fr_iv(rf)
    rho = hi_fr(rho_iv)
    rho_lower = lo_fr(rho_iv)  # Inward bound for containment; upper bound for Hessian variation.
    th0 = [2 * PI * fr_iv(Fr(n, E8)) for n in f0]
    S = [[Fr(0)] * 3 for _ in range(3)]
    Hiv = [[iv.mpf(0)] * 3 for _ in range(3)]
    for kk in aD:
        arg = sum((kk[j] * th0[j] for j in range(3)), iv.mpf(0))
        cs = iv.cos(arg); a = fr_iv(aD[kk]); l1k = sum(abs(q) for q in kk)
        for i in range(3):
            for j in range(i, 3):
                Hiv[i][j] = Hiv[i][j] - a * (kk[i] * kk[j]) * cs
                S[i][j] += abs(aD[kk]) * abs(kk[i] * kk[j]) * l1k
    Hmid = [[Fr(0)] * 3 for _ in range(3)]
    ss = Fr(0)
    for i in range(3):
        for j in range(i, 3):
            mid = (lo_fr(Hiv[i][j]) + hi_fr(Hiv[i][j])) / 2
            rad = (hi_fr(Hiv[i][j]) - lo_fr(Hiv[i][j])) / 2
            Hmid[i][j] = Hmid[j][i] = mid
            ss += (1 if i == j else 2) * (rad + rho * S[i][j]) ** 2
    N_ = (ss.numerator * 10 ** 40) // ss.denominator
    eta = Fr(math.isqrt(N_) + 1, 10 ** 20)            # >= sqrt(ss)  (Frobenius bound of the change of the Hessian over the box)
    Lm = [[Hmid[i][j] - (eta if i == j else 0) for j in range(3)] for i in range(3)]
    piv = []
    for i in range(3):
        p = Lm[i][i]; piv.append(p)
        if p <= 0: break
        for r in range(i + 1, 3):
            fct = Lm[r][i] / p
            for cc in range(i, 3): Lm[r][cc] -= fct * Lm[i][cc]
    pd = len(piv) == 3 and all(p > 0 for p in piv)
    dev = dev_arc(zst, f0)
    a2c = iv.mpf(0); lip = Fr(0)
    for kk in aA:
        arg = sum((kk[j] * th0[j] for j in range(3)), iv.mpf(0))
        a2c += fr_iv(aA[kk]) * iv.cos(arg)
        lip += abs(aA[kk]) * sum(abs(q) for q in kk) * rho
    a2low = lo_fr(a2c) - lip
    return dict(pd=pd, pivmin=min(piv), eta=eta, dev=dev, rho=rho, rho_lower=rho_lower, a2low=a2low)

# ---------------------------------------------------------------- torus clearing with outward-rounded double intervals
DN, UP = -np.inf, np.inf
def rd(x): return np.nextafter(x, DN)
def ru(x): return np.nextafter(x, UP)
def f_dn(x): return float(np.nextafter(float(x), DN))      # float(Fraction) is the nearest double; one ulp down is below it
def f_up(x): return float(np.nextafter(float(x), UP))
def cint(fr):
    return (0.0, 0.0) if fr == 0 else (f_dn(fr), f_up(fr))

class Taylor:
    """Second-order Taylor lower bound of D(theta) = sum a_k cos(k.theta) over dyadic cubes (f-cubes of half-width 2^-(level+1))."""
    def __init__(self, aD):
        assert all(aD.get(tuple(-q for q in k)) == v for k, v in aD.items()), "D not inversion symmetric"
        self.KS = np.array(list(aD.keys()), dtype=np.int64)
        KSl = self.KS.tolist(); A_ = [aD[tuple(k)] for k in KSl]
        self.NT = len(KSl)
        self.QC = [("c", [cint(a) for a in A_])]
        for j in range(3):
            self.QC.append(("s", [cint(-a * k[j]) for a, k in zip(A_, KSl)]))
        for j in range(3):
            for l in range(j, 3):
                self.QC.append(("c", [cint(-a * k[j] * k[l]) for a, k in zip(A_, KSl)]))
        self.R3 = f_up(sum(abs(a) * sum(abs(q) for q in k) ** 3 for a, k in zip(A_, KSl)) / 6)
        iv.prec = 120
        self.TWOPI_UP = float(ru(float((2 * iv.pi).b)))
        iv.prec = 300
    @staticmethod
    def table(ms, N):
        iv.prec = 120
        cl = np.empty(len(ms)); ch = np.empty(len(ms)); sl = np.empty(len(ms)); sh = np.empty(len(ms))
        two_pi = 2 * iv.pi
        for i, m in enumerate(ms.tolist()):
            a = two_pi * iv.mpf(m) / iv.mpf(N)
            c, s = iv.cos(a), iv.sin(a)
            cl[i] = float(rd(float(c.a))); ch[i] = float(ru(float(c.b))); sl[i] = float(rd(float(s.a))); sh[i] = float(ru(float(s.b)))
        iv.prec = 300
        return cl, ch, sl, sh
    def lower_bound(self, idx, k):
        N = 2 ** (k + 1)
        m = ((2 * idx + 1) @ self.KS.T) % N
        ums = np.unique(m)
        cl, ch, sl, sh = self.table(ums, N)
        pos = np.searchsorted(ums, m)
        Cc = (cl[pos], ch[pos]); Ss = (sl[pos], sh[pos])
        n = len(idx)
        res = []
        for kind, co in self.QC:
            accl = np.zeros(n); acch = np.zeros(n)
            src = Cc if kind == "c" else Ss
            for t in range(self.NT):
                tl, th = co[t]
                if tl == 0 and th == 0: continue
                xl, xh = src[0][:, t], src[1][:, t]
                p = np.stack([tl * xl, tl * xh, th * xl, th * xh])
                accl = rd(accl + rd(p.min(axis=0))); acch = ru(acch + ru(p.max(axis=0)))
            res.append((accl, acch))
        rho = ru(self.TWOPI_UP * 2.0 ** (-(k + 1)))
        absmax = lambda pr: np.maximum(np.abs(pr[0]), np.abs(pr[1]))
        g1 = ru(ru(absmax(res[1]) + absmax(res[2])) + absmax(res[3]))
        hs = [absmax(r) for r in res[4:10]]                       # H00 H01 H02 H11 H12 H22
        hsum = ru(ru(ru(hs[0] + hs[3]) + hs[5]) + ru(2 * ru(ru(hs[1] + hs[2]) + hs[4])))
        quad = ru(ru(0.5 * ru(rho * rho)) * hsum)
        lin = ru(rho * g1)
        rem = ru(self.R3 * ru(rho * ru(rho * rho)))
        return rd(rd(rd(res[0][0] - lin) - quad) - rem)


def twopi_up():
    iv.prec = 120
    v = float(ru(float((2 * iv.pi).b)))
    iv.prec = 300
    return v
TWOPI_UP = twopi_up()

def ball_inside(idx, k, kind, rho4):
    """Cubes idx (level k: f-half-width h = 2^-(k+1), centre (2 idx + 1) h) lying inside the quasi-ball N^4 = x^4 + y^2 + z^2 <= rho^4 around the base point (Gamma for kind G, (1/2,1/2,0) for M),
    theta - theta_b = x (1,-1,0) + y (1,1,0) + z (0,0,1).  With m_j the centre offsets in units u = 2 pi h (exact integers) the cube lies in |x| <= u (|m1 - m2|/2 + 1), |y| <= u (|m1 + m2|/2 + 1),
    |z| <= u (|m3| + 1); every double operation rounds upward and 2 pi is replaced by a double above it."""
    L = 2 ** (k + 1)
    fb = (0, 0, 0) if kind == "G" else (L // 2, L // 2, 0)
    m = []
    for j in range(3):
        v = (2 * idx[:, j] + 1 - fb[j]) % L
        m.append(np.where(v > L // 2, v - L, v))
    u = ru(TWOPI_UP / L)
    a1 = np.abs(m[0] - m[1]) / 2.0 + 1.0; a2 = np.abs(m[0] + m[1]) / 2.0 + 1.0; a3 = np.abs(m[2]) + 1.0
    X1 = ru(u * a1); X2 = ru(u * a2); X3 = ru(u * a3)
    X1s = ru(X1 * X1)
    bound = ru(ru(ru(X1s * X1s) + ru(X2 * X2)) + ru(X3 * X3))
    return bound <= rho4

def ball_rho4(rho):
    return f_dn(Fr(rho) ** 4)                                # double below rho^4

def corner_octants(idx, k, kind):
    """octants (sign patterns of the centre offsets) of those cubes in `idx` that touch the base point of the ball (all |m_j| = 1)"""
    L = 2 ** (k + 1)
    fb = (0, 0, 0) if kind == "G" else (L // 2, L // 2, 0)
    m = []
    for j in range(3):
        v = (2 * idx[:, j] + 1 - fb[j]) % L
        m.append(np.where(v > L // 2, v - L, v))
    sel = (np.abs(m[0]) == 1) & (np.abs(m[1]) == 1) & (np.abs(m[2]) == 1)
    return set(zip(np.sign(m[0][sel]).tolist(), np.sign(m[1][sel]).tolist(), np.sign(m[2][sel]).tolist()))

def inside_control(kind, rho, seed=3, per_level=1500):
    """FLOAT control of ball_inside: random dyadic cubes (levels 6-12) around the ball boundary; N^4 = x^4 + y^2 + z^2 is convex, so its maximum over a cube is attained at a vertex;
    ball_inside must never accept a cube whose vertex maximum exceeds rho^4.  Returns (cubes, accepted, violations)."""
    rng = np.random.default_rng(seed)
    r_ = float(rho); rho4 = ball_rho4(rho)
    fb = np.array([0.0, 0.0, 0.0]) if kind == "G" else np.array([0.5, 0.5, 0.0])
    n = acc = viol = 0
    for k in range(6, 13):
        a, b, c = (rng.uniform(-1.2, 1.2, per_level) for _ in range(3))
        x, y, z = r_ * a, r_ ** 2 * b, r_ ** 2 * c
        th = np.stack([x + y, -x + y, z], 1)
        f = (fb + th / (2 * np.pi)) % 1.0
        idx = np.minimum(np.floor(f * 2 ** k).astype(np.int64), 2 ** k - 1)
        ins = ball_inside(idx, k, kind, rho4)
        vmax = np.zeros(len(idx))
        for e in itertools.product((0, 1), repeat=3):
            fv = (idx + np.array(e)) / 2.0 ** k
            tv = 2 * np.pi * (((fv - fb + 0.5) % 1.0) - 0.5)
            xv = (tv[:, 0] - tv[:, 1]) / 2; yv = (tv[:, 0] + tv[:, 1]) / 2
            vmax = np.maximum(vmax, xv ** 4 + yv ** 2 + tv[:, 2] ** 2)
        n += len(idx); acc += int(ins.sum()); viol += int((ins & (vmax > float(Fr(rho) ** 4) * (1 + 1e-9))).sum())
    return n, acc, viol

def clear_torus(tay, boxes, balls=(), k0=3, kmax=21, chunk=10000):
    """boxes: list of (f0 ints over 1e8, rf int over 1e8); balls: list of (kind, rho^4 as a double below).  Dyadic cubes are cleared when the lower bound is positive; an uncleared cube
    that lies inside a box or ball is accepted and not refined further; every other uncleared cube is split.  Returns dict(level, uncleared, outside, cubes, accepted, corner)
    where `corner` is [level] once cubes touching the ball's base point have been accepted inside the ball in all eight octants (their union is a neighbourhood of the base point)."""
    cur = np.array(list(itertools.product(range(2 ** k0), repeat=3)), dtype=np.int64)
    k = k0; total = 0; accepted = 0; unc_total = 0; corner = []; octs = set()
    off = np.array(list(itertools.product((0, 1), repeat=3)), dtype=np.int64)
    while True:
        keep = []
        for s0 in range(0, len(cur), chunk):
            c = cur[s0:s0 + chunk]
            Lb = tay.lower_bound(c, k)
            keep.append(c[~(Lb > 0)])
        unc = np.concatenate(keep) if keep else np.zeros((0, 3), dtype=np.int64)
        total += len(cur); unc_total += len(unc)
        L = (2 ** (k + 1)) * E8
        inside = np.zeros(len(unc), dtype=bool)
        for (nj, rj) in boxes:
            ok = np.ones(len(unc), dtype=bool)
            for a in range(3):
                diff = ((2 * unc[:, a] + 1) * E8 - nj[a] * 2 ** (k + 1)) % L
                diff = np.where(diff > L // 2, diff - L, diff)
                ok &= (np.abs(diff) + E8 <= rj * 2 ** (k + 1))
            inside |= ok
        for (kd, rho4) in balls:
            ib = ball_inside(unc, k, kd, rho4)
            inside |= ib
            octs |= corner_octants(unc[ib], k, kd)
            if len(octs) == 8 and not corner: corner.append(k)
        outside = int((~inside).sum()); accepted += int(inside.sum())
        vemit("   level %2d: cubes %7d uncleared %6d (inside the regions %6d, outside %6d) (%.1f s)" % (k, len(cur), len(unc), int(inside.sum()), outside, time.time() - T0))
        if outside == 0 or k == kmax:
            return dict(level=k, uncleared=unc_total, outside=outside, cubes=total, accepted=accepted, corner=corner)
        unc = unc[~inside]
        cur = (2 * unc[:, None, :] + off[None, :, :]).reshape(-1, 3)
        k += 1
# ---------------------------------------------------------------- float diagnostic: T from numpy at the node
def float_T(J, f):
    """FLOAT diagnostic: T = Im Tr(P d1H P d2H P d3H), P the projector on the eigenvalues |E| < 1e-6 of H(f) (numpy); returns (T, kernel dim)."""
    jx, jy, jz, kk = (float(v) for v in J)
    amp = {"x": 2 * jx, "y": 2 * jy, "z": 2 * jz, "odd": 2 * kk}
    f = np.asarray(f, dtype=float)
    def Hd(dj=None):
        M = np.zeros((4, 4), dtype=complex)
        for (a, b, n, kind) in TERMS:
            ph = np.exp(2j * np.pi * float(np.dot(f, n)))
            if dj is None:
                M[a, b] += amp[kind] * ph; M[b, a] -= amp[kind] * np.conj(ph)
            else:
                w = amp[kind] * 2j * np.pi * n[dj]
                M[a, b] += w * ph; M[b, a] += w * np.conj(ph)
        return 1j * M
    ev, V = np.linalg.eigh(Hd())
    W = V[:, np.abs(ev) < 1e-6]
    P = W @ W.conj().T
    D = [Hd(j) for j in range(3)]
    return float(np.trace(P @ D[0] @ P @ D[1] @ P @ D[2]).imag), W.shape[1]

def f_from_iv(zst):
    out = []
    for (cj, sj) in zst:
        ang = math.atan2(float(sj.mid), float(cj.mid)) / (2 * math.pi)
        out.append(ang % 1.0)
    return out

def sgn_iv(v):
    return 1 if lo_fr(v) > 0 else (-1 if hi_fr(v) < 0 else 0)

def image_centre(base, base_signs, ts, ds):
    """8-digit centre of the image (ts, ds) of the orbit point whose centre `base` has signs base_signs: t -> -t is f -> -f, d -> -d is f1 <-> f2."""
    n = list(base)
    if ds != base_signs[1]: n[0], n[1] = n[1], n[0]
    if ts != base_signs[0]: n = [(-v) % E8 for v in n]
    return tuple(n)


def sgn_str(vals):
    return "".join("+" if v > 0 else ("-" if v < 0 else "0") for v in vals)
def classify_roots(R, q5, cen):
    """All real roots X of Q in [-1,1]: a root with t^2 = 1 - X^2 > 0 and d^2 = sigma^2 - 4 pi > 0 (iv, strict) is a real orbit and must match the listed centre
    `cen` (|X - cos 2 pi f3| < 1e-6); roots with a definitely negative t^2 or d^2 are not real points; roots of undecided sign or real unlisted orbits count as unlisted.
    Returns (matched [(X, t^2, d^2)], unlisted, number of real roots)."""
    a_c = math.cos(2 * math.pi * cen[2] / E8)
    Xs = roots_in_unit(q5)
    matched = []; unl = 0
    for X in Xs:
        Tt = kval(R.T, X); Dd = kval(R.Dc, X)
        real = lo_fr(Tt) > 0 and lo_fr(Dd) > 0
        nonreal = hi_fr(Tt) < 0 or hi_fr(Dd) < 0
        if nonreal: continue
        if not real or abs(float(X.mid) - a_c) > 1e-6:
            unl += 1; continue
        matched.append((X, Tt, Dd))
    return matched, unl, len(Xs)

def line_pred_b(J, kind):
    """predicted charges of the line nodes (x, 1-x, 0), x < 1/2, from the line-node classification of the supplied-model notes: on Jz = Jx + Jy the line has one node besides Gamma, c2 = cos 2 pi x = P/(2u) - 1, iff u > P/4, with
    charge sign(c2) (+1 for P/4 < u < P/2, -1 for u > P/2); on Jz = Jx - Jy there is no line node besides M.  None if undecided."""
    jx, jy, jz, kk = J
    P = jx * jy; u = kk * kk
    if kind == "M" or u <= P / 4: return ()
    c2 = P / (2 * u) - 1
    if c2 == 0: return None
    return (1 if c2 > 0 else -1,)

def census(name, ctx):
    """Exact/interval census at coupling `name`; returns dict(nodes, ...)."""
    J = COUPLINGS[name]; kind = KIND[name]
    jx, jy, jz, kp = J
    iv.prec = 300; mp.mp.prec = 300
    Mr = build_M(J)
    aD = coeffs_at(J, ctx["D"]); aA = coeffs_at(J, ctx["A"])
    rf = Fr(BOXRF.get(name, 5000), E8)
    # ---------------- the degenerate point: exact Taylor-Lagrange quasi-ball
    bl = ball_check(name, aD)
    ks = bl["ks"]
    check(ctx["ok"] and bl["ok"], name + " ball",
          "rho %.3f, A,B,C hold (K_G %.0f K_0 %.1f K_D %.1f s %.3f), weights %s, det H = D, zero unique, deg 0; FLOAT %.0e, %.0e, Chern %.0e, |G|/K %.3f" % (
              float(bl["rho"]), ks["KG"], ks["K0"], ks["KC"], float(bl["s"]), "ok" if bl["wts"] == (4, 5, 2, 6) else str(bl["wts"]), bl["dev"], abs(bl["fdeg"]), abs(bl["chern"]), bl["kfl"]))
    nodes = []                                  # dict(kind, label, f0, sign, T, zst)
    x_ = sp.symbols("x")
    # ---------------- off-plane orbits: exact ring step, root classification, charges
    ex_off = True; off_txt = []; unlisted = 0; pat_ok = True
    for oi, orb in enumerate(OFF.get(name, [])):
        R, z, zi, rel_ok, rel, q5 = offplane_point(orb)
        Qx = sum(c * x_**(len(q5) - 1 - j) for j, c in enumerate(q5))
        fl = sp.factor_list(Qx)
        irr = len(fl[1]) == 1 and fl[1][0][1] == 1
        flags, dat = node_exact(Mr, R, z, zi)
        struct = set(dat["trace"].keys()) == {(1, 1, 1)}
        ex_off = ex_off and irr and rel_ok and all(flags.values()) and struct
        ts0, ds0, cen = orb["image"]
        matched, unl, nroots_off = classify_roots(R, q5, cen)
        unlisted += unl
        nmatch = len(matched)
        for (X, Tt, Dd) in matched:
            first = len(nodes)
            for ts in (1, -1):
                for ds in (1, -1):
                    Tv, a2v, re = charge_iv(dat["trace"], dat["a2"], X, ts * iv.sqrt(Tt), ds * iv.sqrt(Dd))
                    zst = offplane_iv(X, rel, ts, ds)
                    f0 = image_centre(cen, (ts0, ds0), ts, ds)
                    nodes.append(dict(kind="off", label="o%d(t,d)=(%+d,%+d)" % (oi, ts, ds), f0=f0, sign=sgn_iv(Tv), T=Tv, zst=zst, a2=a2v))
            sg = [n["sign"] for n in nodes[first:]]
            pat_ok = pat_ok and (sg[0] == sg[3] != 0 and sg[1] == sg[2] == -sg[0])
        ex_off = ex_off and nmatch == 1
        off_txt.append("%d" % (len(q5) - 1))
    # ---------------- line nodes: exact ring step per irreducible factor, charges, closed form
    ci, nline, facs, removed = line_quadratic(J, kind)
    nroot_fac = 0; ex_line = True; cf_ok = True; lpat_ok = True; line_txt = []
    for fi, cs in enumerate(facs):
        qasc = list(reversed(cs))
        RL, zL, ziL = line_point(qasc)
        flagsL, datL = node_exact(Mr, RL, zL, ziL)
        structL = set(datL["trace"].keys()) == {(1, 0, 1)}
        ex_line = ex_line and all(flagsL.values()) and structL
        TtL_el = RL.T
        for XL in roots_in_unit(cs):
            nroot_fac += 1
            TtL = kval(TtL_el, XL)
            x0 = int(round(math.acos(float(XL.mid)) / (2 * math.pi) * E8))
            first = len(nodes)
            for ts in (1, -1):
                TvL, a2L, reL = charge_iv(datL["trace"], datL["a2"], XL, ts * iv.sqrt(TtL), iv.mpf(1))
                s_ = ts * iv.sqrt(TtL)
                zst = [(XL, s_), (XL, -s_), (iv.mpf(1), iv.mpf(0))]
                f0 = (x0, E8 - x0, 0) if ts == 1 else (E8 - x0, x0, 0)
                nodes.append(dict(kind="line", label="line%d(%+d)" % (fi, ts), f0=f0, sign=sgn_iv(TvL), T=TvL, zst=zst, a2=a2L, cval=float(XL.mid), ts=ts))
            c_ = XL
            qp = 8 * fr_iv(kp * kp) * c_ - 2 * fr_iv(jx * jy)
            Fc = (fr_iv(jx * jy * (jx + jy + jz)) * c_ * c_ + fr_iv((jx + jy) * (jx * jx + jy * jy + jz * (jx + jy))) * c_
                  + fr_iv((jx + jz) * (jy + jz) * (jx + jy - jz)))
            Tcl = -32 * iv.pi ** 3 * fr_iv(kp) * qp * Fc * iv.sqrt(1 - c_ * c_) / fr_iv(jz ** 3)
            diff = nodes[first]["T"] - Tcl
            cf_ok = cf_ok and up_abs(diff) < Fr(1, 10 ** 30) * abs(lo_fr(nodes[first]["T"]))
            lpat_ok = lpat_ok and nodes[first]["sign"] == -nodes[first + 1]["sign"] != 0
        line_txt.append("%d" % (len(cs) - 1))
    ex_line = ex_line and nline == nroot_fac and removed
    nlin = sum(1 for n in nodes if n["kind"] == "line"); noff = len(nodes) - nlin
    cf_txt = ("ok" if cf_ok else "WRONG") if nlin else "n/a"
    ex_ok = ctx["ok"] and ex_off and ex_line and unlisted == 0
    ex_txt = "exact %s (%s%s%s)" % ("ok" if ex_ok else "FAIL", ("orbit Q deg %s irr; " % off_txt[0] if off_txt else ""), ("line deg %s; " % line_txt[0] if line_txt else ""),
                                    "c%s1 removed %s, unlisted %d" % ("-" if kind == "G" else "+", removed, unlisted))
    # ---------------- interval: boxes
    box_ok = True; pivs = []; devs = []; a2s = []
    for nd in nodes:
        hb = hess_box(aD, aA, nd["f0"], rf, nd["zst"])
        nd["hb"] = hb
        okb = hb["pd"] and hb["dev"] <= hb["rho_lower"] and hb["a2low"] > 0
        box_ok = box_ok and okb
        pivs.append(float(hb["pivmin"])); devs.append(float(hb["dev"])); a2s.append(float(hb["a2low"]))
        vemit("   box %s %s f0=%s pivmin %.4g eta %.4g dev %.3g rho %.3g a2low %.4g sign %+d |T| %s" % (
            nd["kind"], nd["label"], nd["f0"], float(hb["pivmin"]), float(hb["eta"]), float(hb["dev"]), float(hb["rho"]), float(hb["a2low"]), nd["sign"],
            mp.nstr(abs(mp.mpf(nd["T"].mid)), 9)))
    disj = True
    for a_, b_ in itertools.combinations(nodes, 2):
        dist = max(min((p - q) % E8, (q - p) % E8) for p, q in zip(a_["f0"], b_["f0"]))
        disj = disj and Fr(dist, E8) > 2 * rf
    nz = all(n["sign"] != 0 for n in nodes)
    total = sum(n["sign"] for n in nodes)                                     # the degenerate point has local degree 0
    lx = sorted([n for n in nodes if n["kind"] == "line" and n["ts"] == 1], key=lambda n: n["cval"])
    pred = line_pred_b(J, kind)
    otri_txt = ""; otri_ok = True
    if pred is not None:
        otri_ok = tuple(n["sign"] for n in lx) == pred
        otri_txt = ", classification %s" % ("ok" if otri_ok else "WRONG")
    offs = [n["sign"] for n in nodes if n["kind"] == "off"]; lins = [n["sign"] for n in nodes if n["kind"] == "line"]
    if nodes:
        check(ex_ok and nz and pat_ok and lpat_ok and cf_ok and box_ok and disj and otri_ok, name + " nodes",
              "%s; charges off %s line %s (closed form %s%s); %d boxes hw %g, pivmin %.3g, disjoint %s" % (
                  ex_txt, sgn_str(offs) or "-", sgn_str(lins) or "-", cf_txt, otri_txt.replace(", classification", ", class"), len(nodes), float(rf), min(pivs), disj))
    else:
        check(ex_ok and otri_ok, name + " nodes", "%s; no node besides the degenerate point%s" % (ex_txt, otri_txt.replace(", classification", ", class")))
    # ---------------- interval: clearing with the ball
    tay = Taylor(aD)
    boxes = [(nd["f0"], BOXRF.get(name, 5000)) for nd in nodes]
    balls = [(kind, ball_rho4(bl["rho"]))]
    t1 = time.time()
    clr = clear_torus(tay, boxes, balls, kmax=KMAX)
    corner_ok = len(clr["corner"]) > 0
    clr_ok = clr["outside"] == 0 and clr["accepted"] > 0 and corner_ok
    # ---------------- float cross-check
    errs = []
    for nd in nodes:
        fnode = f_from_iv(nd["zst"])
        Tf, kd = float_T(J, fnode)
        Te = float(nd["T"].mid)
        errs.append(abs(Tf - Te) / abs(Te) if kd == 2 else 1.0)
    ferr = max(errs) if errs else 0.0
    check(clr_ok and box_ok and total == 0 and nz and ferr < 1e-8, name + " census",
          "D > 0 off boxes, ball: level %d, %d cubes, %d unclear (%d in regions, %d out), octants by %s, %.0f s; %d off + %d line + deg-pt (0): sum %+d, FLOAT T %.0e" % (
              clr["level"], clr["cubes"], clr["uncleared"], clr["accepted"], clr["outside"], ("level %d" % clr["corner"][0]) if clr["corner"] else "none", time.time() - t1, noff, nlin, total, ferr))
    return dict(nodes=nodes, tay=tay, boxes=boxes, balls=balls, aD=aD, aA=aA, clr=clr, Mr=Mr, name=name, facs=facs, ctx=ctx)

def controls(res):
    """negative controls and enclosure sanity checks at the coupling of `res`"""
    name = res["name"]
    nodes, tay, boxes, balls = res["nodes"], res["tay"], res["boxes"], res["balls"]
    lvl = res["clr"]["level"]
    r1 = clear_torus(tay, boxes[1:], balls, kmax=lvl)
    r2 = clear_torus(tay, boxes, [], kmax=lvl)
    check(r1["outside"] > 0 and r2["outside"] > 0, "control removal", "%s: box removed: %d cubes out; ball removed: %d out (level %d, as they should)" % (name, r1["outside"], r2["outside"], r1["level"]))
    Mr = res["Mr"]
    orb = OFF[name][0]
    q5w = list(orb["Q"]); q5w[-1] += 1
    Rw, zw, ziw, relw, _, _ = offplane_point(orb, q5=q5w)
    fw, _ = node_exact(Mr, Rw, zw, ziw)
    Rf, zf, zif, relf, _, _ = offplane_point(orb, flip_s2=True)
    ff, _ = node_exact(Mr, Rf, zf, zif)
    cs = list(res["facs"][0]); cs[-1] += 1
    RL, zL, ziL = line_point(list(reversed(cs)))
    fL, _ = node_exact(Mr, RL, zL, ziL)
    check(not fw["det"] and not fw["minors"] and not ff["det"] and not ff["minors"] and not fL["minors"], "control exact",
          "%s: Q + 1, s2 flipped, line factor + 1: det M, minors nonzero (as should)" % name)
    R0, _, _, _, _, q50 = offplane_point(orb)
    cen_bad = (orb["image"][2][0], orb["image"][2][1], (orb["image"][2][2] + 30000000) % E8)
    mt, ul, _n = classify_roots(R0, q50, cen_bad)
    check(len(mt) == 0 and ul == 1, "control unlisted", "%s: wrong centre: matched %d, unlisted %d (detected)" % (name, len(mt), ul))
    nd = nodes[0]
    f0 = (nd["f0"][0] + 40000, nd["f0"][1], nd["f0"][2])
    hb = hess_box(res["aD"], res["aA"], f0, Fr(BOXRF.get(name, 5000), E8), nd["zst"])
    hbc = hess_box(res["aD"], res["aA"], nd["f0"], Fr(BOXBIG, E8), nd["zst"])
    check(hb["dev"] > hb["rho"] and not hbc["pd"], "control box geometry",
          "%s: centre moved 4e-4: arc %.3g > rho %.3g; hw %g: pivmin %.3g (as they should)" % (name, float(hb["dev"]), float(hb["rho"]), BOXBIG / E8, float(hbc["pivmin"])))
    # ball controls at both base points: radius beyond the proven one, and a wrong leading coefficient
    bc = []
    for nm_ in ("G3", "M3"):
        aDn = coeffs_at(COUPLINGS[nm_], res["ctx"]["D"])
        b1 = ball_check(nm_, aDn, rho=Fr(1, 2))
        b2 = ball_check(nm_, aDn, tweak=Fr(3, 2))
        bc.append((nm_, b1["flags"][7:10], b2["flags"][6], b1["ok"] or b2["ok"]))
    check(not any(b[3] for b in bc) and all(not all(b[1]) for b in bc) and all(not b[2] for b in bc), "control ball",
          "rho 0.5: A,B,C = %s; a -> 3a/2: weights %s (as they should)" % (
              ", ".join("%s %s" % (b[0], "".join("T" if f else "F" for f in b[1])) for b in bc), ", ".join("%s %s" % (b[0], "T" if b[2] else "F") for b in bc)))
    J2 = COUPLINGS["G2"]; x0 = math.acos(float(J2[0] * J2[1] / (2 * J2[3] ** 2) - 1))          # G2 line node (x0, -x0, 0) in theta: x = +-x0
    fx = [fukui_grid(J2, "G", sphere_grid((sg * x0, 0.0, 0.0), (0.15, 0.15, 0.15), 60, 120)) for sg in (1, -1)]
    check(all(abs(abs(f[0]) - 1) < 1e-6 and f[2] > 0 for f in fx) and abs(fx[0][0] + fx[1][0]) < 1e-6, "control Fukui",
          "flux code on spheres around the two G2 line nodes: %+.3f, %+.3f (plaq. %.1f; as it should)" % (fx[0][0], fx[1][0], max(f[1] for f in fx)))
    ic = [inside_control("G", BALL["G3"]), inside_control("M", BALL["M3"])]
    check(all(r[2] == 0 and r[1] > 0 for r in ic), "control inside", "ball_inside vs vertex max of N^4: %d cubes, %d accepted, %d violations (FLOAT)" % (
        sum(r[0] for r in ic), sum(r[1] for r in ic), sum(r[2] for r in ic)))
    mp.mp.dps = 50
    ms = np.arange(0, 256, 7)
    cl, ch, sl, sh = Taylor.table(ms, 256)
    miss = 0
    for i, m in enumerate(ms.tolist()):
        cc = mp.cos(2 * mp.pi * m / 256); ss = mp.sin(2 * mp.pi * m / 256)
        miss += not (cl[i] <= cc <= ch[i] and sl[i] <= ss <= sh[i])
    rng = np.random.default_rng(1)
    viol = 0; ncub = 0
    KS = tay.KS; aDf = np.array([float(res["aD"][tuple(k)]) for k in KS.tolist()])
    for k in (3, 5, 8):
        idx = rng.integers(0, 2 ** k, size=(150, 3))
        Lb = tay.lower_bound(idx, k)
        for j in range(len(idx)):
            fc = (2 * idx[j] + 1) / 2.0 ** (k + 1)
            pts = fc + (rng.random((12, 3)) - 0.5) * 2.0 ** (-k)
            Dv = (aDf[None, :] * np.cos(2 * np.pi * pts @ KS.T)).sum(axis=1)
            viol += int((Dv < Lb[j] - 1e-9).sum()); ncub += 1
    check(miss == 0 and viol == 0, "control enclosures", "iv table vs 50-digit cos, sin at %d phases; Taylor bound <= sampled D on %d cubes, %d violations (FLOAT)" % (len(ms), ncub, viol))
    a3 = Fr(6, 25)
    tsyn = Taylor({(1, 0, 0): Fr(1, 2), (-1, 0, 0): Fr(1, 2), (3, 0, 0): a3 / 2, (-3, 0, 0): a3 / 2})
    ks = 4; rho_s = float(tsyn.TWOPI_UP * 2.0 ** (-(ks + 1)))
    wv = -9.0; wn = -9.0
    for i1 in range(2 ** ks):
        Lb = float(tsyn.lower_bound(np.array([[i1, 0, 0]]), ks)[0])
        thv = 2 * np.pi * ((2 * i1 + 1) / 2.0 ** (ks + 1) + np.linspace(-1, 1, 4001) / 2.0 ** (ks + 1))
        tm = float((np.cos(thv) + float(a3) * np.cos(3 * thv)).min())
        wv = max(wv, Lb - tm); wn = max(wn, Lb + tsyn.R3 * rho_s ** 3 - tm)
    check(wv <= 0 and wn > 1e-3, "control remainder", "D = cos t + 0.24 cos 3t: bound <= sampled min (excess %.2g); remainder dropped: above by %.2g (FLOAT)" % (wv, wn))

def main():
    names = DEFAULT
    if "-a" in sys.argv: names = NAMES
    if "-n" in sys.argv: names = tuple(sys.argv[sys.argv.index("-n") + 1].split(","))
    ok, Dsym, Asym = sym_setup()
    ctx = dict(ok=ok, D=Dsym, A=Asym)
    check(ok, "symbolic", "M + M(1/z)^T = 0, char poly mu^4 + a2 mu^2 + D (symbolic): spec H = {+-l1, +-l2}")
    ctrl = None; allres = {}
    for name in names:
        r = census(name, ctx)
        allres[name] = r
        if name == CONTROL_AT: ctrl = r
        vemit("   [%s] t = %.1f s" % (name, time.time() - T0))
    if ctrl is not None: controls(ctrl)
    check(VERBOSE or OUT_BYTES + 260 < 5000, "stdout budget", "%d bytes so far, limit 5000" % OUT_BYTES)
    emit("[INFO] runtime %.1f s (AUDIT_TIMEOUT_SEC = %d), stdout %d bytes" % (time.time() - T0, AUDIT_TIMEOUT_SEC, OUT_BYTES + 60))
    emit("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))

if __name__ == "__main__":
    main()

# A failed scientific check must fail the bounded execution.
raise SystemExit(1 if FAIL else 0)
