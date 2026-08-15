"""Physical cell cutting: the letter action, the orbit census of the interface matrix, the piece-size quantum, and class as composition.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, and the sixteen-letter facet alphabet on the two slots of axis zero. Nothing outside that finite object enters any gate.

The previous cycle showed that exactly the 96 cell maps fixing the first axis carry the wall of 48 interface entries of value 36 to itself,
transitively, with each entry stabilizer of order 2 equal to that fiber's fold. This cycle reads the letter level. Every cell map is tested
for an induced letter map: a permutation of the 16 letters together with a slot-swap flag, with both flag values tried. The assignment is
tested for uniqueness, for the flag law, for faithfulness, for its kernel, and for the homomorphism property at every ordered pair of acting
maps. The induced action on the 256 ordered letter pairs is decomposed into orbits, the interface matrix is tested for constancy on each,
the wall is identified with a single orbit and drawn as a graph, every kept piece is tested for a point count that is a multiple of five,
every cutting for one and the same unit profile, and the light, middle and heavy classes of the previous cycle are matched against the
piece-size composition of the distinguished exchange. A product-structure hypothesis for the union sizes is tested and refuted.
Gates G1 to G10, one line each with a few detail lines, then the total line. Any failure exits nonzero.
"""

import itertools
import sys
from collections import Counter
from fractions import Fraction as FRA

AUDIT_TIMEOUT_SEC = 900

OUT = [0]


def emit(s):
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    if len(txt) > 148:
        raise ValueError("output line over the length limit")
    OUT[0] += len(txt) + 1
    if OUT[0] >= 5800:
        raise ValueError("output over the character budget")
    print(txt)


STAT = [0, 0]


def gate(ok, tag, msg):
    if ok:
        STAT[0] += 1
    else:
        STAT[1] += 1
    emit("{0} {1} {2}".format("PASS" if ok else "FAIL", tag, msg))


def dshow(d):
    return "{" + ", ".join("{0}: {1}".format(k, d[k]) for k in sorted(d)) + "}"


def popc(x):
    return bin(x).count("1")


# ---------------------------------------------------------------- the object

CORN = [tuple((i >> b) & 1 for b in range(4)) for i in range(16)]
CIDX = {c: i for i, c in enumerate(CORN)}


def det4(M):
    tot = 0
    cols = (0, 1, 2, 3)
    for c in itertools.combinations(cols, 2):
        rest = tuple(x for x in cols if x not in c)
        a = M[0][c[0]] * M[1][c[1]] - M[0][c[1]] * M[1][c[0]]
        b = M[2][rest[0]] * M[3][rest[1]] - M[2][rest[1]] * M[3][rest[0]]
        tot += ((-1) ** (c[0] + c[1] + 1)) * a * b
    return tot


def inv4(C):
    n = 4
    M = [[FRA(C[r][c]) for c in range(n)] + [FRA(1 if r == c else 0) for c in range(n)] for r in range(n)]
    for c in range(n):
        p = -1
        for r in range(c, n):
            if M[r][c] != 0:
                p = r
                break
        if p < 0:
            return None
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                fq = M[r][c]
                M[r] = [M[r][k] - fq * M[c][k] for k in range(2 * n)]
    out = []
    for r in range(n):
        row = []
        for c in range(n, 2 * n):
            v = M[r][c]
            if v.denominator != 1:
                return None
            row.append(int(v))
        out.append(row)
    return out


def adjcost(S):
    bad = 0
    for a, b in itertools.combinations(S, 2):
        d = sum(abs(CORN[a][r] - CORN[b][r]) for r in range(4))
        if d > 1:
            bad += 1
    return bad


CAND = [S for S in itertools.combinations(range(16), 5)
        if abs(det4([[CORN[S[j + 1]][r] - CORN[S[0]][r] for j in range(4)] for r in range(4)])) == 1]
COSTS = [adjcost(S) for S in CAND]
FLOOR = min(COSTS)
KEPT = [CAND[i] for i in range(len(CAND)) if COSTS[i] == FLOOR]

BARY = []
for S in KEPT:
    v0 = CORN[S[0]]
    C = [[CORN[S[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]
    BARY.append((v0, inv4(C)))

NSHIFT, OFFS, RSTEP = 16, (1, 2, 4, 8), 5
DIV = NSHIFT * RSTEP
NPTS = RSTEP ** 4


def buildmask(offs):
    """Membership bitmasks of every kept piece on the sample points of one per-axis offset table, by exact integer barycentric tests."""
    axval = [[NSHIFT * k + offs[i] for k in range(RSTEP)] for i in range(4)]
    out = []
    for (v0, Ci) in BARY:
        off = [sum(Ci[i][c] * DIV * v0[c] for c in range(4)) for i in range(4)]
        col = [[[Ci[i][ax] * u for i in range(4)] for u in axval[ax]] for ax in range(4)]
        bits = 0
        idx = 0
        for a in col[0]:
            s1 = [a[i] - off[i] for i in range(4)]
            for b in col[1]:
                s2 = [s1[i] + b[i] for i in range(4)]
                for c in col[2]:
                    s3 = [s2[i] + c[i] for i in range(4)]
                    for d in col[3]:
                        w = [s3[i] + d[i] for i in range(4)]
                        sw = sum(w)
                        if all(x > 0 for x in w) and sw < DIV:
                            bits |= (1 << idx)
                        idx += 1
        out.append(bits)
    return out


MASK = buildmask(OFFS)
UNIV = (1 << NPTS) - 1

BYPT = [[] for _ in range(NPTS)]
for t in range(len(KEPT)):
    mm = MASK[t]
    while mm:
        low = mm & (-mm)
        BYPT[low.bit_length() - 1].append(t)
        mm ^= low

SOLS = []
sys.setrecursionlimit(10000)


def cover_search(cov, chosen):
    if cov == UNIV:
        SOLS.append(tuple(chosen))
        return
    free = UNIV & (~cov)
    p = (free & (-free)).bit_length() - 1
    for t in BYPT[p]:
        m = MASK[t]
        if m & cov:
            continue
        chosen.append(t)
        cover_search(cov | m, chosen)
        chosen.pop()


cover_search(0, [])
NS = len(SOLS)
USED = sorted(set(t for s in SOLS for t in s))
NU = len(USED)
SIDX = {frozenset(s): i for i, s in enumerate(SOLS)}
KIDX = {frozenset(S): t for t, S in enumerate(KEPT)}
CSET = [frozenset(s) for s in SOLS]
PSIZE = len(set(len(s) for s in SOLS))
CSIZE = sorted(set(len(s) for s in SOLS))[0]
NK = len(KEPT)

P4 = list(itertools.permutations(range(4)))
G384 = [(p, m) for p in P4 for m in range(16)]
GID = ((0, 1, 2, 3), 0)
FLIP1 = ((0, 1, 2, 3), 1)

FACE = {}
for t in range(NK):
    S = KEPT[t]
    for a in range(4):
        for c in (0, 1):
            F = [v for v in S if CORN[v][a] == c]
            if len(F) == 4:
                FACE[(t, a, c)] = frozenset(tuple(CORN[v][r] for r in range(4) if r != a) for v in F)

KEYF = []
for s in SOLS:
    d = {}
    for a in range(4):
        for c in (0, 1):
            d[(a, c)] = frozenset(FACE[(t, a, c)] for t in s if (t, a, c) in FACE)
    KEYF.append(d)

ALLK = sorted({d[k] for d in KEYF for k in d}, key=lambda fz: sorted(sorted(t) for t in fz))
KN = {k: i for i, k in enumerate(ALLK)}
KEY = [{k: KN[v] for k, v in d.items()} for d in KEYF]
NL = len(ALLK)


def actcorner(g, v):
    p, m = g
    x = CORN[v]
    return CIDX[tuple(x[p[i]] ^ ((m >> p[i]) & 1) for i in range(4))]


def compose(a, b):
    p, m = a
    q, n = b
    r = tuple(q[p[i]] for i in range(4))
    k = n
    for j in range(4):
        if (m >> j) & 1:
            k ^= (1 << q[j])
    return (r, k)


def piecemap(g, dom):
    return dict((t, KIDX[frozenset(actcorner(g, v) for v in KEPT[t])]) for t in dom)


def imgof(pmp, IMG, i):
    """Image cutting index of cutting i under the piece map pmp, cached in IMG so no cutting image is ever recomputed for one cell map."""
    j = IMG[i]
    if j < 0:
        j = SIDX[frozenset(pmp[t] for t in SOLS[i])]
        IMG[i] = j
    return j


# ---------------------------------------------- the alphabet, the interface matrix and the wall

PAIROF = [(KEY[i][(0, 0)], KEY[i][(0, 1)]) for i in range(NS)]
JC = Counter(PAIROF)
TRM = [[JC[(x, y)] for y in range(NL)] for x in range(NL)]
TRC = sum(TRM[x][x] for x in range(NL))
N36 = sum(1 for x in range(NL) for y in range(NL) if TRM[x][y] == 36)
FIB = {}
for i in range(NS):
    FIB.setdefault(PAIROF[i], []).append(i)
E36 = sorted(kj for kj in FIB if TRM[kj[0]][kj[1]] == 36)
NF = len(E36)
FL = [FIB[kj] for kj in E36]
FS = [set(F) for F in FL]
EIDX = dict((e, i) for i, e in enumerate(E36))
IDS = tuple(range(NL))

# ============================================== G1 the induced letter map of every cell map, both flag values tried

FOLD = [None] * NF
STCNT = [0] * NF
DEFECT = 0
EMAP = {}
LMAP = {}
NSOLC = Counter()
for g in G384:
    pmp = piecemap(g, USED)
    IMGB = [-1] * NS
    if len(set(pmp.values())) != NU:
        DEFECT += 1
    em = [-1] * NF
    for f in range(NF):
        tg = set()
        hold = True
        for c in FL[f]:
            j = imgof(pmp, IMGB, c)
            if j not in FS[f]:
                hold = False
            tg.add(PAIROF[j])
        if hold:
            STCNT[f] += 1
            if g != GID:
                FOLD[f] = g
        if len(tg) == 1:
            e = sorted(tg)[0]
            if e in EIDX:
                em[f] = EIDX[e]
    EMAP[g] = tuple(em)
    good = []
    for sw in (0, 1):
        sig = [-1] * NL
        bak = [-1] * NL
        ok = True
        for i in range(NS):
            a, b = PAIROF[i]
            u, v = PAIROF[imgof(pmp, IMGB, i)]
            if sw:
                u, v = v, u
            if sig[a] < 0 and bak[u] < 0:
                sig[a] = u
                bak[u] = a
            elif sig[a] != u:
                ok = False
                break
            if sig[b] < 0 and bak[v] < 0:
                sig[b] = v
                bak[v] = b
            elif sig[b] != v:
                ok = False
                break
        if ok and min(sig) >= 0:
            good.append((tuple(sig), sw))
    NSOLC[(g[0][0] == 0, len(good))] += 1
    if len(good) == 1:
        LMAP[g] = good[0]

FIXONE = NSOLC[(True, 1)]
FIXBAD = sum(NSOLC[k] for k in NSOLC if k[0] and k[1] != 1)
OTHNIL = NSOLC[(False, 0)]
OTHBAD = sum(NSOLC[k] for k in NSOLC if (not k[0]) and k[1] != 0)

gate(len(CAND) == 2672 and FLOOR == 6 and NK == 400 and NS == 15800 and PSIZE == 1 and CSIZE == 24 and NU == 192
     and len(G384) == 384 and NL == 16 and TRC == 2000 and N36 == 48 and NF == 48 and DEFECT == 0
     and FIXONE == 96 and FIXBAD == 0 and OTHNIL == 288 and OTHBAD == 0, "G1",
     "of the {0} cell maps exactly {1} induce a letter map, each with one flag value, and the other {2} induce none for either flag"
     .format(len(G384), FIXONE, OTHNIL))
emit("G1 detail: declared cell: {0} candidates, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, {6} letters, trace {7}"
     .format(len(CAND), FLOOR, NK, NS, CSIZE, NU, NL, TRC))

# ============================================== G2 the flag law, faithfulness, the kernel of the letter permutation

ACTG = [g for g in G384 if g[0][0] == 0]
SWOK = sum(1 for g in ACTG if g in LMAP and LMAP[g][1] == (g[1] & 1))
DISTP = len(set(LMAP[g] for g in ACTG if g in LMAP))
KER = sorted(g for g in ACTG if g in LMAP and LMAP[g][0] == IDS)
SIGIM = len(set(LMAP[g][0] for g in ACTG if g in LMAP))
KEROK = KER == [GID, FLIP1] and LMAP[GID][1] == 0 and LMAP[FLIP1][1] == 1

gate(len(ACTG) == 96 and SWOK == 96 and DISTP == 96 and len(KER) == 2 and KEROK and SIGIM == 48, "G2",
     "the flag is bit zero of the flip mask at all {0} acting maps, the {0} letter maps are pairwise distinct, and the kernel has size {1}"
     .format(len(ACTG), len(KER)))
emit("G2 detail: the kernel is the identity with flag {0} and the pure first-axis flip with flag {1}, so the permutation image has order {2}"
     .format(LMAP[GID][1], LMAP[FLIP1][1], SIGIM))

# ============================================== G3 the assignment is a homomorphism at every ordered pair

HOM = 0
for g in ACTG:
    sg, wg = LMAP[g]
    for h in ACTG:
        sh, wh = LMAP[h]
        e = LMAP.get(compose(g, h))
        if e is None:
            continue
        if e[0] == tuple(sg[sh[x]] for x in range(NL)) and e[1] == (wg ^ wh):
            HOM += 1

gate(HOM == 9216 and len(ACTG) * len(ACTG) == 9216, "G3",
     "at all {0} ordered pairs of acting maps the letter permutation composes in the order the maps are applied and the flags add"
     .format(HOM))

# ============================================== G4 the interface matrix is symmetric and equivariant

SYM = sum(1 for a in range(NL) for b in range(NL) if TRM[a][b] == TRM[b][a])
EQV = 0
for g in ACTG:
    sg, wg = LMAP[g]
    cc = 0
    for a in range(NL):
        for b in range(NL):
            ia, ib = (sg[b], sg[a]) if wg else (sg[a], sg[b])
            if TRM[ia][ib] == TRM[a][b]:
                cc += 1
    if cc == NL * NL:
        EQV += 1

gate(SYM == 256 and NL * NL == 256 and EQV == 96, "G4",
     "the interface matrix is symmetric at all {0} entries and equivariant under all {1} acting maps, with slots swapped when the flag is set"
     .format(SYM, EQV))

# ============================================== G5 the letters fall into two orbits

LPAR = list(range(NL))


def findl(a):
    while LPAR[a] != a:
        LPAR[a] = LPAR[LPAR[a]]
        a = LPAR[a]
    return a


for g in ACTG:
    sg = LMAP[g][0]
    for a in range(NL):
        ra, rb = findl(a), findl(sg[a])
        if ra != rb:
            LPAR[ra] = rb
LORB = {}
for a in range(NL):
    LORB.setdefault(findl(a), []).append(a)
LOS = sorted(LORB.values(), key=len, reverse=True)
BIG = sorted(LOS[0])
SML = sorted(LOS[1]) if len(LOS) > 1 else []
WLET = sorted(set(x for e in E36 for x in e))
NWLET = [a for a in range(NL) if a not in WLET]
RS = [sum(TRM[a]) for a in range(NL)]
RSB = sorted(set(RS[a] for a in BIG))
RSS = sorted(set(RS[a] for a in SML))
DGB = sorted(set(TRM[a][a] for a in BIG))
DGS = sorted(set(TRM[a][a] for a in SML))

gate(len(LOS) == 2 and len(BIG) == 12 and len(SML) == 4 and BIG == WLET and SML == NWLET
     and BIG == [0, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14] and SML == [1, 6, 8, 15]
     and RSB == [862] and RSS == [1364] and DGB == [100] and DGS == [200] and TRC == 2000 and NL == 16, "G5",
     "the {0} letters fall into exactly {1} orbits of sizes {2} and {3}, and the size {2} orbit is exactly the set of letters of the wall"
     .format(NL, len(LOS), len(BIG), len(SML)))
emit("G5 detail: row sums are {0} on the {1} wall letters {2} and {3} on the others {4}"
     .format(RSB[0], len(BIG), BIG, RSS[0], SML))
emit("G5 detail: diagonal entries are {0} on the wall letters and {1} on the others, and the trace is {2}"
     .format(DGB[0], DGS[0], TRC))

# ============================================== G6 the orbit census of the 256 ordered letter pairs

NP2 = NL * NL
PPAR = list(range(NP2))


def findp(a):
    while PPAR[a] != a:
        PPAR[a] = PPAR[PPAR[a]]
        a = PPAR[a]
    return a


for g in ACTG:
    sg, wg = LMAP[g]
    for a in range(NL):
        for b in range(NL):
            ia, ib = (sg[b], sg[a]) if wg else (sg[a], sg[b])
            ra, rb = findp(a * NL + b), findp(ia * NL + ib)
            if ra != rb:
                PPAR[ra] = rb
POR = {}
for k in range(NP2):
    POR.setdefault(findp(k), []).append(k)
ORBL = []
CONST = 0
for r in sorted(POR):
    mem = POR[r]
    vs = set(TRM[divmod(k, NL)[0]][divmod(k, NL)[1]] for k in mem)
    if len(vs) == 1:
        CONST += 1
    ORBL.append((len(mem), sorted(vs)[0], mem))
OV = sorted((s, v) for s, v, mem in ORBL)
VALS = sorted(set(v for s, v in OV))
OPV = Counter(v for s, v in OV)
ECEN = Counter(TRM[a][b] for a in range(NL) for b in range(NL))
WSUM = sum(v * ECEN[v] for v in ECEN)
ANCOV = [(4, 200), (12, 18), (12, 18), (12, 90), (12, 100), (12, 104), (48, 36), (48, 50), (48, 52), (48, 92)]
ANCEC = {18: 24, 36: 48, 50: 48, 52: 48, 90: 12, 92: 48, 100: 12, 104: 12, 200: 4}
O18 = [mem for s, v, mem in ORBL if v == 18]
TR18 = all(set(divmod(k, NL)[1] * NL + divmod(k, NL)[0] for k in mem) == set(mem) for mem in O18)
ED = sorted(sorted(set(tuple(sorted(divmod(k, NL))) for k in mem)) for mem in O18)
A18 = sorted(set(tuple(sorted((a, b))) for a in range(NL) for b in range(NL) if TRM[a][b] == 18))
E18OK = (len(O18) == 2 and TR18 and [len(e) for e in ED] == [6, 6] and not set(ED[0]) & set(ED[1])
         and sorted(set(ED[0]) | set(ED[1])) == A18 and len(A18) == 12)

gate(len(OV) == 10 and OV == ANCOV and CONST == 10 and len(VALS) == 9 and OPV[18] == 2
     and sorted(OPV[v] for v in VALS if v != 18) == [1] * 8 and dict(ECEN) == ANCEC and WSUM == 15800
     and sum(ECEN[v] for v in ECEN) == 256 and E18OK, "G6",
     "the {0} ordered letter pairs fall into exactly {1} orbits, the matrix is constant on each, and its {0} entries sum to {2}"
     .format(NP2, len(OV), WSUM))
emit("G6 detail: orbit sizes with their values {0}".format(OV))
emit("G6 detail: the value {0} alone carries {1} orbits, each held by the transpose, giving {2} unordered pairs each"
     .format(18, OPV[18], len(ED[0])))
emit("G6 detail: the first orbit at that value is {0}".format(ED[0]))
emit("G6 detail: the second orbit at that value is {0}".format(ED[1]))
emit("G6 detail: the value census over the {0} entries is {1}".format(NP2, dshow(ECEN)))

# ============================================== G7 the wall is the orbit at value 36, and a graph

W36 = set(a * NL + b for (a, b) in E36)
O36 = [set(mem) for s, v, mem in ORBL if v == 36]
PF = 0
for g in ACTG:
    sg, wg = LMAP[g]
    for f in range(NF):
        a, b = E36[f]
        ia, ib = (sg[b], sg[a]) if wg else (sg[a], sg[b])
        if EMAP[g][f] >= 0 and E36[EMAP[g][f]] == (ia, ib):
            PF += 1
UNW = sorted(set(tuple(sorted(e)) for e in E36))
DEG = Counter()
for (a, b) in UNW:
    DEG[a] += 1
    DEG[b] += 1
DEGV = sorted(set(DEG.values()))

gate(len(O36) == 1 and O36[0] == W36 and len(W36) == 48 and PF == 4608 and PF == len(ACTG) * NF
     and len(UNW) == 24 and sorted(DEG) == WLET and DEGV == [4], "G7",
     "the {0} wall entries at value {1} are exactly one orbit, and the letter pair formula gives the induced entry map at all {2} pairs"
     .format(len(W36), 36, PF))
emit("G7 detail: unordered the wall is {0} edges on the {1} wall letters, and every one of those letters has degree exactly {2}"
     .format(len(UNW), len(WLET), DEGV[0]))

# ============================================== G8 the piece-size quantum and the constant profile

PSZ = [popc(MASK[t]) for t in range(NK)]
UNIT = [0] * NK
DIVOK = 0
for t in range(NK):
    q, r = divmod(PSZ[t], 5)
    UNIT[t] = q
    if r == 0 and q * 5 == PSZ[t]:
        DIVOK += 1
CKEPT = Counter(UNIT)
CUSED = Counter(UNIT[t] for t in USED)
SPEC = sorted(CKEPT)
PROF = set(tuple(sorted(Counter(UNIT[t] for t in s).items())) for s in SOLS)
ONEP = sorted(PROF)[0]
TUNIT = sum(k * n for k, n in ONEP)

gate(DIVOK == NK and NK == 400 and SPEC == [1, 3, 7, 14] and sum(SPEC) == 25
     and dict(CKEPT) == {1: 24, 3: 176, 7: 176, 14: 24} and dict(CUSED) == {1: 8, 3: 88, 7: 88, 14: 8}
     and len(PROF) == 1 and ONEP == ((1, 1), (3, 11), (7, 11), (14, 1)) and TUNIT == 125
     and TUNIT * 5 == NPTS and NPTS == 625 and NS == 15800 and NU == 192, "G8",
     "every one of the {0} kept pieces has a point count of exactly {1} times its unit, and the unit spectrum {2} sums to {3}"
     .format(NK, 5, SPEC, sum(SPEC)))
emit("G8 detail: the unit census over the kept pieces is {0} and over the {1} used pieces is {2}"
     .format(dshow(CKEPT), NU, dshow(CUSED)))
emit("G8 detail: all {0} cuttings carry one and the same profile, {1} piece of unit {2}, {3} of unit {4}, {3} of unit {5}, {1} of unit {6}"
     .format(NS, 1, 1, 11, 3, 7, 14))
emit("G8 detail: that profile totals {0} units, that is {1} points, the whole sample grid".format(TUNIT, TUNIT * 5))

# ============================================== the fold two-orbit tables and the fiber instances

DIST = sorted(set(FOLD))
FIDX = {g: i for i, g in enumerate(DIST)}
MPKS = []
ORBS = []
OIDX = []
NORB = set()
for g in DIST:
    mpk = piecemap(g, range(NK))
    orbs = []
    seen = set()
    for t in range(NK):
        if t in seen:
            continue
        u = mpk[t]
        seen.add(t)
        seen.add(u)
        orbs.append((t, u))
    oi = {}
    for i in range(len(orbs)):
        oi[orbs[i][0]] = i
        oi[orbs[i][1]] = i
    MPKS.append(mpk)
    ORBS.append(orbs)
    OIDX.append(oi)
    NORB.add(len(orbs))


def instance(f, MX):
    """Rebuild fiber f from the two-orbits of its fold: the held cuttings as row vectors, the point supports of the rows on the given
    frame, the equal-union exchanges of the rows with their unions, and the broken count of each exchange."""
    fi = FIDX[FOLD[f]]
    mpk = MPKS[fi]
    oi = OIDX[fi]
    orbs = ORBS[fi]
    held = [c for c in FL[f] if frozenset(mpk[t] for t in SOLS[c]) == CSET[c]]
    raw = [frozenset(oi[t] for t in SOLS[c]) for c in held]
    rowg = sorted(set().union(*raw))
    nr = len(rowg)
    rpos = {r: i for i, r in enumerate(rowg)}
    vecs = [sum(1 << rpos[r] for r in rr) for rr in raw]
    sup = [MX[orbs[rowg[i]][0]] | MX[orbs[rowg[i]][1]] for i in range(nr)]
    ug = {}
    for i, j in itertools.combinations(range(nr), 2):
        if sup[i] & sup[j]:
            continue
        ug.setdefault(sup[i] | sup[j], []).append((i, j))
    spl = {}
    for u in ug:
        for pa, pb in itertools.combinations(ug[u], 2):
            if len(set(pa) | set(pb)) == 4:
                ma = (1 << pa[0]) | (1 << pa[1])
                mb = (1 << pb[0]) | (1 << pb[1])
                spl[ma | mb] = (ma, mb, popc(u), u)
    brk = Counter()
    for dv in spl:
        ma, mb, usz, uu = spl[dv]
        for w in vecs:
            x = w & dv
            if x != 0 and x != ma and x != mb:
                brk[dv] += 1
    return {"held": held, "rowg": rowg, "nr": nr, "orbs": orbs, "vecs": vecs, "spl": spl, "brk": brk, "sup": sup}


def halfprof(d, m):
    """The sorted unit profile of the four kept pieces carried by the two rows of one half of an equal-union exchange."""
    ps = []
    for i in range(d["nr"]):
        if (m >> i) & 1:
            ps.extend(UNIT[t] for t in d["orbs"][d["rowg"][i]])
    return tuple(sorted(ps))


D1 = [instance(f, MASK) for f in range(NF)]

# ============================================== G9 the class of a fiber is the piece-size composition of its distinguished exchange

NROW = sorted(set(d["nr"] for d in D1))
NEXC = sorted(set(len(d["spl"]) for d in D1))
EXPP = {50: ((1, 3, 3, 3), (1, 3, 3, 3)), 100: ((3, 3, 7, 7), (3, 3, 7, 7)), 175: ((7, 7, 7, 14), (7, 7, 7, 14))}
BADP = 0
NCHK = 0
B2 = {}
B2N = Counter()
for f in range(NF):
    d = D1[f]
    for dv in d["spl"]:
        ma, mb, usz, uu = d["spl"][dv]
        NCHK += 1
        if tuple(sorted((halfprof(d, ma), halfprof(d, mb)))) != EXPP.get(usz):
            BADP += 1
    two = sorted(dv for dv in d["spl"] if d["brk"][dv] == 2)
    B2N[len(two)] += 1
    if len(two) == 1:
        B2[f] = d["spl"][two[0]][2]
LANC = [(2, 12), (4, 14), (5, 13), (7, 11)]
HANC = [(2, 3), (4, 7), (10, 11), (12, 13)]
ANCU = {}
for f in range(NF):
    e = tuple(sorted(E36[f]))
    ANCU[f] = 50 if e in LANC else (175 if e in HANC else 100)
AGREE = sum(1 for f in range(NF) if f in B2 and B2[f] == ANCU[f])
CEN = Counter(B2[f] for f in B2)

gate(NROW == [40] and NEXC == [4] and BADP == 0 and NCHK == NF * 4 and dict(B2N) == {1: NF}
     and AGREE == NF and NF == 48 and dict(CEN) == {50: 8, 100: 32, 175: 8}
     and sorted(NORB) == [200] and sorted(set(len(d["held"]) for d in D1)) == [14], "G9",
     "over the {0} rows of every one of the {1} fibers, the half unit profiles of all {2} equal-union exchanges follow the union size"
     .format(NROW[0], NF, NCHK))
emit("G9 detail: union {0} gives halves {1}, union {2} gives {3}, union {4} gives {5}, with {6} exceptions"
     .format(50, EXPP[50][0], 100, EXPP[100][0], 175, EXPP[175][0], BADP))
emit("G9 detail: each fiber has exactly {0} exchange of broken count {1}, and its union size census over the {2} fibers is {3}"
     .format(1, 2, NF, dshow(CEN)))
emit("G9 detail: that census matches the light, middle and heavy letter pair lists of the previous cycle at {0} of {0} fibers".format(NF))

# ============================================== G10 the product-structure hypothesis, tested and refuted

AXP = sorted(itertools.combinations(range(4), 2))
CP = []
for (i, j) in AXP:
    tab = [0] * NPTS
    for p in range(NPTS):
        q, c3 = divmod(p, RSTEP)
        q, c2 = divmod(q, RSTEP)
        c0, c1 = divmod(q, RSTEP)
        cs = (c0, c1, c2, c3)
        tab[p] = cs[i] * RSTEP + cs[j]
    CP.append(tab)


def factorizes(supm, ap):
    """True when the point set factorizes as a base on the given axis pair times the full five by five square on the other two axes."""
    cnt = {}
    m = supm
    while m:
        low = m & (-m)
        k = CP[ap][low.bit_length() - 1]
        cnt[k] = cnt.get(k, 0) + 1
        m ^= low
    return len(cnt) > 0 and all(v == RSTEP * RSTEP for v in cnt.values())


FACU = 0
FACR = 0
NUT = 0
NRT = 0
for f in range(NF):
    d = D1[f]
    for dv in d["spl"]:
        uu = d["spl"][dv][3]
        for ap in range(len(AXP)):
            NUT += 1
            if factorizes(uu, ap):
                FACU += 1
    for i in range(d["nr"]):
        for ap in range(len(AXP)):
            NRT += 1
            if factorizes(d["sup"][i], ap):
                FACR += 1

CTRL = sum(1 for ap in range(len(AXP)) if factorizes(UNIV, ap))

gate(len(AXP) == 6 and RSTEP * RSTEP == 25 and FACU == 0 and FACR == 0 and NUT == NF * 4 * 6 and NRT == NF * 40 * 6
     and CTRL == len(AXP), "G10",
     "over all {0} axis pairs no exchange union factorizes as a base times the full {1} point square: {2} of {3} unions factorize"
     .format(len(AXP), RSTEP * RSTEP, FACU, NUT))
emit("G10 detail: and no single row support factorizes either, {0} of {1} tested, so the union sizes are piece-size accounting"
     .format(FACR, NRT))
emit("G10 detail: the same test on the whole sample grid returns a factorization on all {0} of {0} axis pairs, so the test can succeed"
     .format(CTRL))

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
