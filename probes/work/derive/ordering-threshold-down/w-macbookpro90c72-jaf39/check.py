#!/usr/bin/env python3
"""Exact checks for ordering-threshold-down, attempt 1 (w-macbookpro90c72-jaf39).

Every claim below is finite and is verified in exact arithmetic (Fraction / int /
sympy).  Nothing is evaluated in floating point except for printing.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import sympy as sp

OUT, FAIL = [], 0


def check(tag, ok, msg):
    global FAIL
    if not ok:
        FAIL += 1
    OUT.append("%s %s %s" % (tag, msg, "ok" if ok else "FAIL"))


# ---------------------------------------------------------------- deviations
# block 30 / PR #8174, runner family B:
#   d1 = 1 - K(a|a,a,a), d2 = 1 - K(a|a,a,-a), d3 = 1 - K(a|a,a,b).
def devs(p, q, r):
    p, q, r = F(p), F(q), F(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def e12(p):
    d1, d2, d3 = devs(p, 1, 2)
    return d1, max(d2, d3)


# ------------------------------------------------------- D1: (p,1,2) numerators
p = sp.symbols("p", positive=True)
d1s = 1 - p ** 3 / (p ** 3 + 1 + 32)
d2s = 1 - p ** 2 / (p * (p + 1) + 32)
d3s = 1 - 2 * p ** 2 / (2 * (p ** 2 + 1) + 4 * (p + 1) + 16)
gen = [sp.simplify(a - b) for a, b in
       ((d1s, sp.Rational(33) / (p ** 3 + 33)),
        (d2s, (p + 32) / (p ** 2 + p + 32)),
        (d3s, (2 * p + 11) / (p ** 2 + 2 * p + 11)))]
nums = [sp.factor(sp.numer(sp.together(a - b))) for a, b in
        ((d2s, d1s), (d3s, d1s), (d2s, d3s))]
want = [sp.factor(x) for x in (p ** 2 * (p - 1) * (p + 33),
                               p ** 2 * (2 * p ** 2 + 11 * p - 33),
                               p ** 2 * (21 - p))]
check("D1", all(g == 0 for g in gen) and all(sp.simplify(a - b) == 0 for a, b in zip(nums, want)),
      "(p,1,2) nums p^2(p-1)(p+33), p^2(2p^2+11p-33), p^2(21-p)")

# ------------------------------------------------ D2: T1(a) on the lines / (1,2,1)
line_ok = all(devs(v, 1, 2)[0] <= max(devs(v, 1, 2)[1:]) for v in range(1, 400))
a, b, c = devs(1, 2, 1)
check("D2", line_ok and a == F(12, 13) and max(b, c) == F(9, 10) and a > max(b, c),
      "d1<=max(d2,d3) on (p,1,2) p<400; (1,2,1) d1=12/13>9/10: not attractive")

# ---------------------------------------------------------- M1: monotonicity
def mono(x1, x2):
    # f(n,U) = 1{n>=2} + 1{n=1}1{U<x2} + 1{n=0}1{U<x1}; test every order cell of U
    for u in (F(0), min(x1, x2), (x1 + x2) / 2, max(x1, x2), F(1)):
        f = [int(u < x1), int(u < x2), 1, 1]
        if any(f[i] > f[i + 1] for i in range(3)):
            return False
    return True


check("M1", all(mono(*e12(v)) for v in range(1, 60)) and not mono(devs(1, 2, 1)[0], max(devs(1, 2, 1)[1:]))
      and mono(F(1, 3), F(1, 2)) and not mono(F(1, 2), F(1, 3)),
      "f(n,U) nondecreasing in n for all U iff e1<=e2")


# ------------------------------- G1: the exact r-extraction for the refined alphabet
e2s, ws, rs = sp.symbols("e2 w r", positive=True)
g = e2s * rs + 2 * e2s + 2 * ws
check("G1", all(sp.expand(sp.expand(g ** (3 * R)).coeff(rs, R)
                          - comb(3 * R, R) * e2s ** R * (2 * e2s + 2 * ws) ** (2 * R)) == 0
                for R in range(1, 7)),
      "[r^R](e2 r+2e2+2w)^3R = C(3R,R) e2^R (2e2+2w)^2R, R=1..6")

# ------------------------------------------- G2: the two-sided bound on C(3R,R)
check("G2", all(F(27, 4) ** R / (3 * R + 1) <= comb(3 * R, R) <= F(27, 4) ** R
                for R in range(1, 201)),
      "(27/4)^R/(3R+1) <= C(3R,R) <= (27/4)^R, R<=200")

# ------------------- G3: w=1 reproduces 27 e2 < 1, first true at p = 58 on (p,1,2)
old = [27 * e12(v)[1] < 1 for v in (57, 58)]
check("G3", old == [False, True] and devs(57, 1, 2)[2] == F(125, 3374) and devs(58, 1, 2)[2] == F(127, 3491)
      and 27 * 125 > 3374 and 27 * 127 < 3491,
      "27e2<1 first at p=58: d3(57)=125/3374, d3(58)=127/3491")

# ----------------------------------------------------- P1: the price sheet, exact
SHEET = [(58, F(9726, 10000)), (40, F(7757, 10000)), (20, F(4523, 10000)),
         (14, F(2513, 10000)), (13, F(2093, 10000)), (11, F(1136, 10000))]


def star(v, w):                                  # the criterion 27 e2 (e2+w)^2 < 1
    return 27 * e12(v)[1] * (e12(v)[1] + w) ** 2 < 1


check("P1", all(star(v, w) and not star(v, w + F(2, 10000)) for v, w in SHEET),
      "w<.9726/.7757/.4523/.2513/.2093/.1136 at p=58/40/20/14/13/11 (tight to 1e-4)")

# ------------------------------------- F1: the floor w = e2 gives 108 e2^3 < 1, p>=14
floor_ok = all(star(v, e12(v)[1]) == (108 * e12(v)[1] ** 3 < 1) for v in range(1, 200))
first14 = [108 * e12(v)[1] ** 3 < 1 for v in (13, 14)]
check("F1", floor_ok and first14 == [False, True] and e12(13)[1] == F(45, 214) and e12(14)[1] == F(23, 121)
      and 108 * 45 ** 3 == 9841500 > 214 ** 3 == 9800344 and 108 * 23 ** 3 == 1314036 < 121 ** 3 == 1771561,
      "w=e2 -> 108e2^3<1 iff p>=14: 108*45^3>214^3, 108*23^3<121^3")

# --------------------------------- F2: the unconditional bootstrap w = e1 is refuted
boot = [star(v, e12(v)[0]) for v in (9, 10)]
check("F2", boot == [False, True] and e12(10)[0] == F(33, 1033) and e12(10)[1] == F(42, 142),
      "w=e1 first holds at p=10, below the located (10.5,11): refuted")

# ---------------------------------------------------------------- the true cone
# Backward cone of x at level T.  Depth-m site (a,b,c), a+b+c=m, denotes
# x-(a,b,c); its three predecessors are (a+1,b,c),(a,b+1,c),(a,b,c+1) at depth
# m+1.  Depth T is level 0 and is all-0 (the maximally wrong start).  The joint
# law of each layer is propagated exactly, layer by layer, with Fractions.
def layer(m):
    return sorted((a, b, m - a - b) for a in range(m + 1) for b in range(m + 1 - a))

def step(dist, m, x1, x2, joint=False):
    lo, hi = layer(m), layer(m + 1)
    idx = {s: i for i, s in enumerate(hi)}
    pr3 = [[idx[(z[0] + 1, z[1], z[2])], idx[(z[0], z[1] + 1, z[2])],
            idx[(z[0], z[1], z[2] + 1)]] for z in lo]
    combos = list(product((0, 1), repeat=len(lo)))
    out = {}
    for s, pw in dist.items():
        ps = []
        for i, j, k in pr3:
            n = s[i] + s[j] + s[k]
            ps.append(F(1) if n >= 2 else (x2 if n == 1 else x1))
        for t in combos:
            wt = pw
            for v, qq in zip(t, ps):
                wt *= qq if v else 1 - qq
                if wt == 0:
                    break
            if wt:
                key = (s, t) if joint else t
                out[key] = out.get(key, 0) + wt
    return out

def cone(T, x1, x2, keep=None):
    dist, saved = {tuple([0] * len(layer(T))): F(1)}, None
    for m in range(T - 1, -1, -1):
        if m == keep:
            saved = step(dist, m, x1, x2, joint=True)
            dist = {}
            for (s, t), wt in saved.items():
                dist[t] = dist.get(t, 0) + wt
        else:
            dist = step(dist, m, x1, x2)
    return dist[(1,)], saved

PS = {v: [cone(T, *e12(v))[0] for T in (1, 2, 3, 4)] for v in (11, 14, 58, 84)}

# C1: the exhaustive small-cone law, T = 1..4, against the closed form at T = 2
E1, E2 = sp.symbols("E1 E2", positive=True)
P2f = E1 * (1 - E1) ** 3 + 3 * E2 * E1 * (1 - E1) ** 2 + 3 * E1 ** 2 * (1 - E1) + E1 ** 3
def sub(x, v):
    return x.subs({E1: sp.Rational(*e12(v)[0].as_integer_ratio()),
                   E2: sp.Rational(*e12(v)[1].as_integer_ratio())})
check("C1", all(P[0] == e12(v)[0] and sp.Rational(*P[1].as_integer_ratio()) == sub(P2f, v)
                and all(P[i] <= P[i + 1] for i in range(3)) for v, P in PS.items()),
      "cone P_T exact T<=4 at p=11/14/58/84: P_1=e1, P_2 closed form, increasing")

# C2: at a coincident pole the per-charge price does NOT dominate the truth.
# True e1e2 coefficient of P_2 is 3; the refined R=1 weight is 12 e1 e2 (e2+w)^2.
# 48 e1 e2^3 < 3 e1 e2 iff e2 < 1/4 iff 4(p+32) < p^2+p+32 iff p^2-3p-96 > 0 iff p >= 12.
c2 = [(12 * e12(v)[0] * e12(v)[1] * (2 * e12(v)[1]) ** 2 < 3 * e12(v)[0] * e12(v)[1])
      == (v >= 12) for v in range(1, 21)]
check("C2", sp.expand(P2f).coeff(E1, 1).coeff(E2, 1) == 3 and all(c2)
      and 11 ** 2 - 3 * 11 - 96 == -8 and 12 ** 2 - 3 * 12 - 96 == 12,
      "coincident pole: refined 48 e1 e2^3 < true 3 e1 e2 iff p>=12 (p^2-3p-96>0)")

# C3: the floor, and the direction of the correlation, inside the true T=4 cone.
# y=(1,0,0) and z=(0,1,0) are siblings; their only shared predecessor is c=(1,1,0).
L2, L1 = layer(2), layer(1)
ic, iz = L2.index((1, 1, 0)), L1.index((0, 1, 0))
C3 = []
for v in (13, 14, 58, 84):
    J = cone(4, *e12(v), keep=1)[1]
    pc = sum(w for (s, _), w in J.items() if s[ic] == 1)
    pcz = sum(w for (s, t), w in J.items() if s[ic] == 1 and t[iz] == 1)
    pz = sum(w for (_, t), w in J.items() if t[iz] == 1)
    C3.append(pcz / pc >= e12(v)[1] > pz)
check("C3", all(C3), "T=4 cone: P(z=1|c=1) >= e2 > P(z=1) at p=13/14/58/84")

print("\n".join(OUT))
print("TOTAL %d checks, %d ok, %d fail" % (len(OUT), len(OUT) - FAIL, FAIL))
print("SUMMARY: ROUTE FAILS AT S3 (the prices do not multiply: the uncharged "
      "predecessor's witness shares the pole's predecessor c, so BK is denied and "
      "FKG runs the wrong way); PARTIAL: the exact criterion 27 e2 (e2+w)^2 < 1 for "
      "the refinement sum, its price sheet, the forced floor w >= e2 (ceiling "
      "p >= 14), and e1 <= e2 <=> monotonicity of eta'.")
print("HIT: on (p,1,2) block 30's T1(a) is exactly attractiveness of eta'; charging "
      "e2 per amplification and w per deterministic move gives 27 e2 (e2+w)^2 < 1 "
      "(w=1 recovers p>=58); the shared predecessor forces w >= e2, so this lever "
      "stops at 108 e2^3 < 1, p >= 14, and the bootstrap w = e1 is refuted.")
raise SystemExit(1 if FAIL else 0)
