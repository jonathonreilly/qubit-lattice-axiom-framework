#!/usr/bin/env python3
# b4b55_1 -- exact finite-group check of Lemma AVG (BFT4B55 section 3).
# Criteria: checks/b4b55_1_criteria.md (written before this script). Exact arithmetic only (int / Fraction).
# The gauge g in G^S acts on EVERY link with an endpoint in S (extended by the identity elsewhere) and each polymer
# function is evaluated on the FULL configuration, so locality (P3) is not built into the averaging.
from fractions import Fraction
from itertools import product
import random
import sys
import time

T0 = time.time()
# ---------------- the group S_3 as index tables ----------------
G = [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0), (2, 0, 1)]
IDX = {p: i for i, p in enumerate(G)}
ID = IDX[(0, 1, 2)]
TRANSP01 = IDX[(1, 0, 2)]      # the transposition (0 1)
CYC = IDX[(1, 2, 0)]           # 0->1->2->0


def _comp(p, q):               # (p o q)(i) = p(q(i))
    return (p[q[0]], p[q[1]], p[q[2]])


def _inv(p):
    r = [0, 0, 0]
    for i in range(3):
        r[p[i]] = i
    return tuple(r)


MUL = [[IDX[_comp(G[i], G[j])] for j in range(6)] for i in range(6)]
INV = [IDX[_inv(G[i])] for i in range(6)]
MAT = [[[1 if G[g][c] == r else 0 for c in range(3)] for r in range(3)] for g in range(6)]   # MAT[g][r][c]
CHI = [sum(1 for i in range(3) if G[g][i] == i) for g in range(6)]
# sanity of the tables (matrix representation is a homomorphism)
for a in range(6):
    for b in range(6):
        for r in range(3):
            for c in range(3):
                assert MAT[MUL[a][b]][r][c] == sum(MAT[a][r][s] * MAT[b][s][c] for s in range(3))

# ---------------- the 3x3 periodic lattice ----------------
NS = 3
SITES = [(x, y) for x in range(NS) for y in range(NS)]
LINKS = [(x, y, mu) for x in range(NS) for y in range(NS) for mu in (0, 1)]


def site(x, y):
    return (x % NS, y % NS)


def link(x, y, mu):
    return (x % NS, y % NS, mu)


def tail(l):
    return (l[0], l[1])


def head(l):
    return site(l[0] + (1 if l[2] == 0 else 0), l[1] + (1 if l[2] == 1 else 0))


def edges(s):                  # bottom, right, top, left of the plaquette with lower-left corner s
    x, y = s
    return (link(x, y, 0), link(x + 1, y, 1), link(x, y + 1, 0), link(x, y, 1))


def Up(U, s):
    b, r, t, l = edges(s)
    return MUL[MUL[MUL[U[b]][U[r]]][INV[U[t]]]][INV[U[l]]]


def Pp(U, s):
    b, r, t, l = edges(s)
    return MUL[MUL[U[b]][U[r]]][INV[U[t]]]


def Cp(U, s):
    return INV[U[edges(s)[3]]]


def h(q):
    return MAT[q][0][0] + 2 * MAT[q][1][0] + 3 * MAT[q][2][1]


def h2(q):
    return MAT[q][2][0] + MAT[q][0][2]


def Tterm(U, s):
    return MAT[Pp(U, s)][0][1] * MAT[Cp(U, s)][1][0]


TSET = [(0, 0), (1, 1), (2, 2)]


def minus_e0(s):
    return site(s[0] - 1, s[1])


def plus_e0(s):
    return site(s[0] + 1, s[1])


def E(U):
    tot = 0
    for s in SITES:
        u = Up(U, s)
        tot += CHI[u] + 2 * CHI[MUL[u][u]]
    return tot


def R_plaq(U, s, drop_top=False):
    b, r, t, l = edges(s)
    u = Up(U, s)
    val = CHI[u] + 2 * CHI[MUL[u][u]] + h(U[b]) + h(U[l]) - h(U[r])
    if not drop_top:
        val -= h(U[t])
    if s in TSET:
        val += Tterm(U, s)
    if minus_e0(s) in TSET:
        val -= h2(U[r])
    return val


def R_dom(U, q):
    r2 = edges(plus_e0(q))[1]
    return -Tterm(U, q) + h2(U[r2])


def support_sites(supp):
    S = []
    for l in supp:
        for v in (tail(l), head(l)):
            if v not in S:
                S.append(v)
    return S


# polymers: (name, declared support links, function of the full configuration)
POLY = []
for s in SITES:
    POLY.append(("P" + str(s), list(edges(s)), (lambda U, s=s: R_plaq(U, s))))
for q in TSET:
    supp = list(edges(q))
    for l in edges(plus_e0(q)):
        if l not in supp:
            supp.append(l)
    POLY.append(("D" + str(q), supp, (lambda U, q=q: R_dom(U, q))))
assert all(len(p[1]) == 4 for p in POLY[:9]) and all(len(p[1]) == 7 for p in POLY[9:])
assert all(len(support_sites(p[1])) == 6 for p in POLY[9:])


def gauge_full(U, g):          # g: dict site -> index (all sites)
    return {l: MUL[MUL[g[tail(l)]][U[l]]][INV[g[head(l)]]] for l in LINKS}


def avg(f, U, S, consts_only=False):
    """Average f(U^g) over g in G^S (identity off S); g acts on every link with an endpoint in S."""
    S = list(S)
    pos = {v: i for i, v in enumerate(S)}
    inc = [l for l in LINKS if tail(l) in pos or head(l) in pos]
    ti = [pos.get(tail(l)) for l in inc]
    hi = [pos.get(head(l)) for l in inc]
    tot = 0
    cnt = 0
    it = ([c] * len(S) for c in range(6)) if consts_only else product(range(6), repeat=len(S))
    for gs in it:
        V = dict(U)
        for l, a, b in zip(inc, ti, hi):
            x = U[l]
            if a is not None:
                x = MUL[gs[a]][x]
            if b is not None:
                x = MUL[x][INV[gs[b]]]
            V[l] = x
        tot += f(V)
        cnt += 1
    return Fraction(tot, cnt)


def predicted(name, U):
    kind, lab = name[0], eval(name[1:])
    if kind == "P":
        s = lab
        u = Up(U, s)
        val = Fraction(CHI[u] + 2 * CHI[MUL[u][u]])
        if s in TSET:
            val += Fraction(CHI[u], 9)
        if minus_e0(s) in TSET:
            val -= Fraction(2, 3)
        return val
    q = lab
    return -Fraction(CHI[Up(U, q)], 9) + Fraction(2, 3)


def predicted_K4(name, U):     # control: wrong coefficient 1/8
    kind, lab = name[0], eval(name[1:])
    if kind == "P":
        s = lab
        u = Up(U, s)
        val = Fraction(CHI[u] + 2 * CHI[MUL[u][u]])
        if s in TSET:
            val += Fraction(CHI[u], 8)
        if minus_e0(s) in TSET:
            val -= Fraction(2, 3)
        return val
    q = lab
    return -Fraction(CHI[Up(U, q)], 8) + Fraction(2, 3)


# ---------------- configurations and gauges ----------------
CONF = {}
CONF["A"] = {l: ID for l in LINKS}
C = {l: ID for l in LINKS}
C[link(0, 0, 0)] = TRANSP01
CONF["C"] = C
for nm, seed in (("R1", 101), ("R2", 202), ("R3", 303)):
    rng = random.Random(seed)
    CONF[nm] = {l: rng.randrange(6) for l in LINKS}
GSEEDS = {"A": (1, 2), "C": (1, 2), "R1": (108, 112), "R2": (209, 213), "R3": (310, 314)}
GAUGES = {}
for nm, (s1, s2) in GSEEDS.items():
    gl = []
    for sd in (s1, s2):
        rng = random.Random(sd)
        gl.append({v: rng.randrange(6) for v in SITES})
    GAUGES[nm] = gl
for nm in CONF:            # the tested gauges must be non-constant (K3 needs this)
    for g in GAUGES[nm]:
        assert len(set(g.values())) > 1, "constant test gauge"

out = []


def say(*a):
    s = " ".join(str(x) for x in a)
    out.append(s)
    print(s)


say("b4b55_1 -- Lemma AVG exact check (S_3, 3x3 periodic 2D lattice)")
say("polymers:", [p[0] for p in POLY])

# ---------------- P0 / P1 / P4 ----------------
RBAR = {}
P0 = True
P1 = True
P4 = True
K4_fired = False
for nm, U in CONF.items():
    e = E(U)
    s_in = sum(f(U) for (_, _, f) in POLY)
    ok0 = (s_in == e)
    P0 &= ok0
    tot = Fraction(0)
    for (name, supp, f) in POLY:
        rb = avg(f, U, support_sites(supp))
        RBAR[(nm, name)] = rb
        tot += rb
        pr = predicted(name, U)
        if rb != pr:
            P4 = False
            say("  P4 MISMATCH", nm, name, rb, pr)
        if rb != predicted_K4(name, U):
            K4_fired = True
    ok1 = (tot == e)
    P1 &= ok1
    say("config", nm, "E =", e, "| sum R =", s_in, "P0", ok0, "| sum Rbar =", tot, "P1", ok1)
say("P0 (input identity):", P0)
say("P1 (AVG (c) identity):", P1)
say("P4 (hand prediction chi/9, 2/3):", P4)

# ---------------- P2, P5(a), K1, K3 ----------------
P2 = True
P5a = False
K1_fired = False
K3_fired = False
for nm, U in CONF.items():
    for gi, g in enumerate(GAUGES[nm]):
        Ug = gauge_full(U, g)
        for (name, supp, f) in POLY:
            S = support_sites(supp)
            rbg = avg(f, Ug, S)
            if rbg != RBAR[(nm, name)]:
                P2 = False
                say("  P2 MISMATCH", nm, gi, name, rbg, RBAR[(nm, name)])
            if f(Ug) != f(U):
                P5a = True
            # K3: constant gauges only
            if avg(f, Ug, S, consts_only=True) != avg(f, U, S, consts_only=True):
                K3_fired = True
            # K1: Tset plaquettes, drop the site s + e1
            if name[0] == "P" and eval(name[1:]) in TSET:
                s = eval(name[1:])
                S1 = [v for v in S if v != site(s[0], s[1] + 1)]
                assert len(S1) == len(S) - 1
                if avg(f, Ug, S1) != avg(f, U, S1):
                    K1_fired = True
say("P2 (AVG (b) invariance under non-constant gauges):", P2)
say("P5(a) (some input piece is NOT invariant):", P5a)

# ---------------- P3 locality ----------------
P3 = True
for nm, U in CONF.items():
    for (name, supp, f) in POLY:
        outside = [l for l in LINKS if l not in supp]
        l0 = outside[0]
        U2 = dict(U)
        U2[l0] = MUL[U[l0]][CYC]
        assert U2[l0] != U[l0]
        if avg(f, U2, support_sites(supp)) != RBAR[(nm, name)]:
            P3 = False
            say("  P3 MISMATCH", nm, name)
say("P3 (AVG (a) locality):", P3)

# ---------------- P5(b) ----------------
p00 = "P(0, 0)"
uA = Up(CONF["A"], (0, 0))
uC = Up(CONF["C"], (0, 0))
dA = RBAR[("A", p00)] - (CHI[uA] + 2 * CHI[MUL[uA][uA]])
dC = RBAR[("C", p00)] - (CHI[uC] + 2 * CHI[MUL[uC][uC]])
P5b = (dA != dC)
say("P5(b) (non-constant invariant correction for P(0,0)): A ->", dA, " C ->", dC, ":", P5b)

# ---------------- P6 bound ----------------
s0 = (0, 0)
fP = [p for p in POLY if p[0] == p00][0]
supp0 = fP[1]
S0 = support_sites(supp0)
maxR = 0
maxRbar = Fraction(0)
base = {l: ID for l in LINKS}
for vals in product(range(6), repeat=4):
    U = dict(base)
    for l, v in zip(supp0, vals):
        U[l] = v
    r = fP[2](U)
    maxR = max(maxR, abs(r))
    rb = avg(fP[2], U, S0)
    if abs(rb) > maxRbar:
        maxRbar = abs(rb)
P6 = (maxRbar <= maxR)
say("P6 (bound) over 1296 local configs of P(0,0): max|Rbar| =", maxRbar, " max|R| =", maxR, ":", P6)

# ---------------- K2 ----------------
K2_fired = False
for nm, U in CONF.items():
    s_bad = 0
    for (name, supp, f) in POLY:
        if name == "P(1, 0)":
            s_bad += R_plaq(U, (1, 0), drop_top=True)
        else:
            s_bad += f(U)
    if s_bad != E(U):
        K2_fired = True
say("K1 (drop site s+e1 from a Tset average) fires (P2 fails):", K1_fired)
say("K2 (drop -h(top) of P(1,0)) fires (P0 fails):", K2_fired)
say("K3 (constant gauges only) fires (P2 fails):", K3_fired)
say("K4 (coefficient 1/8) fires (P4 fails):", K4_fired)

gates = P0 and P1 and P2 and P3 and P4 and P5a and P5b and P6
controls = K1_fired and K2_fired and K3_fired and K4_fired
say("GATES:", gates, " CONTROLS:", controls)
say("OVERALL:", "PASS" if (gates and controls) else "FAIL")
sys.stderr.write("elapsed %.1f s\n" % (time.time() - T0))
