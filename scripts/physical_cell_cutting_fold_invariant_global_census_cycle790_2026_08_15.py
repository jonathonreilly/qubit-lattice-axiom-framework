"""Physical cell cutting: the fold census, the fold-invariant global held set, its derived evenness, and the quotient enumeration.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, the slot-preserving subgroup of order ninety-six for axis zero, and the sixteen-letter facet alphabet. Nothing outside
that finite object enters any gate.

The previous cycle showed that each of the 48 stubborn interface fibers carries exactly one nontrivial setwise stabilizer, its fold, and
that the fold holds 14 of the fiber's 36 cuttings. This cycle drops the per-fiber framing and counts globally: how many distinct folds serve
the 48 fibers, how many cuttings of the whole cell a fold holds, what the centralizer of a fold does to that global held set, and whether
the same set can be enumerated natively in the quotient of the kept pieces by the fold. The evenness of the global count is the target.

Gates G1 to G12, one line each with a few detail lines, then a resource line and the total line. Any failure exits nonzero."""

import itertools
import sys
import time
import resource
from collections import Counter
from fractions import Fraction as FRA

AUDIT_TIMEOUT_SEC = 900

T0 = time.time()
OUT = [0]


def emit(s):
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    if len(txt) > 148:
        raise ValueError("output line over the length limit")
    OUT[0] += len(txt) + 1
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


def pshow(v):
    return " ".join("({0},{1})".format(a, b) for (a, b) in v)


def gshow(v):
    return " ".join("({0},{1},{2},{3})/{4}".format(g[0][0], g[0][1], g[0][2], g[0][3], g[1]) for g in v)


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
                f = M[r][c]
                M[r] = [M[r][k] - f * M[c][k] for k in range(2 * n)]
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
AXVAL = [[NSHIFT * k + OFFS[i] for k in range(RSTEP)] for i in range(4)]
NPTS = RSTEP ** 4
MASK = []
for (v0, Ci) in BARY:
    off = [sum(Ci[i][c] * DIV * v0[c] for c in range(4)) for i in range(4)]
    col = [[[Ci[i][ax] * u for i in range(4)] for u in AXVAL[ax]] for ax in range(4)]
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
    MASK.append(bits)
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

FACE = {}
for t in USED:
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

ALLK = sorted({d[k] for d in KEYF for k in d}, key=lambda f: sorted(sorted(t) for t in f))
KN = {k: i for i, k in enumerate(ALLK)}
KEY = [{k: KN[v] for k, v in d.items()} for d in KEYF]
NL = len(ALLK)

STAB = [(p, m) for (p, m) in G384 if p[0] == 0]
GID = ((0, 1, 2, 3), 0)


def actcorner(g, v):
    p, m = g
    x = CORN[v]
    return CIDX[tuple(x[p[i]] ^ ((m >> p[i]) & 1) for i in range(4))]


def act3(g, pt):
    p, m = g
    return tuple(pt[p[i + 1] - 1] ^ ((m >> p[i + 1]) & 1) for i in range(3))


PSI = {}
PBAD = 0
for g in STAB:
    ps = tuple(KN[frozenset(frozenset(act3(g, v) for v in tet) for tet in ALLK[li])] for li in range(16))
    if sorted(ps) != list(range(16)):
        PBAD += 1
    PSI[g] = ps

PCACHE = {}


def permof(g):
    if g not in PCACHE:
        mp = {t: KIDX[frozenset(actcorner(g, v) for v in KEPT[t])] for t in USED}
        PCACHE[g] = [SIDX[frozenset(mp[t] for t in s)] for s in SOLS]
    return PCACHE[g]


def compose(a, b):
    p, m = a
    q, n = b
    r = tuple(q[p[i]] for i in range(4))
    k = n
    for j in range(4):
        if (m >> j) & 1:
            k ^= (1 << q[j])
    return (r, k)


def cycen(img, pos, dom):
    cc = Counter()
    seen = set()
    for i in range(len(dom)):
        if i in seen:
            continue
        x = i
        n = 0
        while True:
            seen.add(x)
            x = pos[img[x]]
            n += 1
            if x == i:
                break
        cc[n] += 1
    return dict(sorted(cc.items()))


# ================================================================ G1 the declared object and the composition rule

IDXA = (0, 5, 17, 33, 64, 97, 128, 150, 191, 200, 233, 255, 260, 288, 300, 319, 340, 355, 370, 383)
IDXB = (383, 370, 355, 340, 319, 300, 288, 260, 255, 233, 200, 191, 150, 128, 97, 64, 33, 17, 5, 0)
CBAD = 0
for i in range(len(IDXA)):
    ca, cb = G384[IDXA[i]], G384[IDXB[i]]
    cc = compose(ca, cb)
    for v in range(len(CORN)):
        if actcorner(cc, v) != actcorner(ca, actcorner(cb, v)):
            CBAD += 1

gate(len(CAND) == 2672 and FLOOR == 6 and NK == 400 and NS == 15800 and PSIZE == 1 and CSIZE == 24 and NU == 192
     and len(G384) == 384 and len(STAB) == 96 and PBAD == 0 and CBAD == 0 and len(IDXA) == 20, "G1",
     "{0} pieces, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, cell group {6}, slot subgroup {7}, {8} composition pairs clean"
     .format(len(CAND), FLOOR, NK, NS, CSIZE, NU, len(G384), len(STAB), len(IDXA)))

# ================================================================ G2 the alphabet and the wall

MULT = [Counter(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
NSLOT = len(MULT)
MSAME = all(m == MULT[0] for m in MULT)
MCEN = dict(sorted(Counter(MULT[0].values()).items()))
PAIROF = [(KEY[i][(0, 0)], KEY[i][(0, 1)]) for i in range(NS)]
JC = Counter(PAIROF)
TR = [[JC[(x, y)] for y in range(NL)] for x in range(NL)]
TRC = sum(TR[x][x] for x in range(NL))
N36 = sum(1 for x in range(NL) for y in range(NL) if TR[x][y] == 36)
FIB = {}
for i in range(NS):
    FIB.setdefault(PAIROF[i], []).append(i)
E36 = sorted(kj for kj in FIB if TR[kj[0]][kj[1]] == 36)
FSZ = sorted(set(len(FIB[kj]) for kj in E36))
NF = len(E36)
WSZ = FSZ[0]

gate(NL == 16 and MSAME and NSLOT == 8 and MCEN == {862: 12, 1364: 4} and TRC == 2000
     and N36 == 48 and NF == 48 and FSZ == [36], "G2",
     "{0} letters on each of {1} slots, multiplicity census {2}, trace {3}, {4} entries at {5}, {6} fibers of {5} cuttings"
     .format(NL, NSLOT, dshow(MCEN), TRC, N36, WSZ, NF))

# ================================================================ G3 the fold census over the whole cell group

FL = [FIB[kj] for kj in E36]
FS = [set(F) for F in FL]
FOLD = [None] * NF
STCNT = [0] * NF
DEFECT = 0
for g in G384:
    pm = permof(g)
    PCACHE.clear()
    if len(set(pm)) != NS:
        DEFECT += 1
    for f in range(NF):
        S = FS[f]
        ok = True
        for c in FL[f]:
            if pm[c] not in S:
                ok = False
                break
        if ok:
            STCNT[f] += 1
            if g != GID:
                FOLD[f] = g

DIST = sorted(set(FOLD))
SERVE = dict(sorted(Counter(Counter(FOLD).values()).items()))
TRP = Counter()
STRUCT = 0
for (p, m) in DIST:
    mv = [i for i in (1, 2, 3) if p[i] != i]
    if p[0] != 0 or len(mv) != 2:
        continue
    a, b = mv[0], mv[1]
    if p[a] != b or p[b] != a or not (m & 1):
        continue
    if ((m >> a) & 1) != ((m >> b) & 1):
        continue
    STRUCT += 1
    TRP[(a, b)] += 1
TCEN = dict(sorted(Counter(TRP.values()).items()))

gate(DEFECT == 0 and set(STCNT) == set([2]) and len(DIST) == 6 and SERVE == {8: 6} and STRUCT == 6
     and len(TRP) == 3 and TCEN == {2: 3}, "G3",
     "the {0} fiber folds are {1} distinct maps, census {2}; each holds axis 0, swaps two of axes 1 2 3, {3} masks per swap, all side-swapping"
     .format(NF, len(DIST), dshow(SERVE), sorted(TRP.values())[0]))
emit("G3 detail: the folds are {0}".format(gshow(DIST)))

# ================================================================ G4 the global held set of the sample fold

GREP = ((0, 3, 2, 1), 15)
GPM = permof(GREP)
PCACHE.clear()
FIX = [c for c in range(NS) if GPM[c] == c]
NFIX = len(FIX)
POSF = {c: i for i, c in enumerate(FIX)}
ENTCEN = dict(sorted(Counter(TR[PAIROF[c][0]][PAIROF[c][1]] for c in FIX).items()))
PCNT = Counter(PAIROF[c] for c in FIX)
PCEN = dict(sorted(Counter(PCNT.values()).items()))
GFIBS = [f for f in range(NF) if FOLD[f] == GREP]
GHELD = [sum(1 for c in FL[f] if GPM[c] == c) for f in GFIBS]

gate(GREP in DIST and NFIX == 336 and ENTCEN == {36: 112, 100: 92, 104: 36, 200: 96} and len(PCNT) == 16
     and PCEN == {10: 2, 14: 8, 18: 2, 36: 2, 48: 2} and len(GFIBS) == 8 and set(GHELD) == set([14])
     and sum(GHELD) == 112, "G4",
     "the sample fold holds {0} of the {1} cuttings, entry census {2}, spread over {3} letter pairs"
     .format(NFIX, NS, dshow(ENTCEN), len(PCNT)))
emit("G4 detail: per-pair count census {0}; the {1} fibers this fold serves hold {2} each, {3} in all"
     .format(dshow(PCEN), len(GFIBS), sorted(set(GHELD))[0], sum(GHELD)))

# ================================================================ G5 the same census for all six folds

SAME = 0
for g in DIST:
    pmx = permof(g)
    PCACHE.clear()
    fx = [c for c in range(NS) if pmx[c] == c]
    ec = dict(sorted(Counter(TR[PAIROF[c][0]][PAIROF[c][1]] for c in fx).items()))
    if len(fx) == NFIX and ec == ENTCEN:
        SAME += 1

gate(SAME == 6 and len(DIST) == 6, "G5",
     "all {0} folds hold {1} cuttings with the same entry census {2}"
     .format(len(DIST), NFIX, dshow(ENTCEN)))

# ================================================================ G6 the remainder outside the wall fibers

WALLC = set(c for f in GFIBS for c in FL[f])
WCUT = sorted(WALLC)
REM = [c for c in FIX if c not in WALLC]
RCNT = Counter(PAIROF[c] for c in REM)
ROBS = sorted((TR[a][b], (a, b), v) for (a, b), v in RCNT.items())
RSPEC = sorted([(200, (1, 1), 48), (200, (15, 15), 48), (100, (3, 3), 36), (100, (14, 14), 36),
                (100, (5, 5), 10), (100, (10, 10), 10), (104, (6, 8), 18), (104, (8, 6), 18)])
REVEN = all(not (v & 1) for v in RCNT.values())

gate(len(REM) == 224 and ROBS == RSPEC and REVEN and len(RCNT) == 8, "G6",
     "outside the {0} wall fibers the fold holds {1} cuttings on {2} letter pairs, every per-pair count even"
     .format(len(GFIBS), len(REM), len(RCNT)))
emit("G6 detail: entry {0} pairs (1,1) and (15,15) hold {1} each; entry {2} pairs (3,3) and (14,14) hold {3}, (5,5) and (10,10) hold {4}"
     .format(200, 48, 100, 36, 10))
emit("G6 detail: entry {0} pairs (6,8) and (8,6) hold {1} each, so the remainder splits as {2} plus {3} plus {4} plus {5}"
     .format(104, 18, 96, 72, 20, 36))

# ================================================================ G7 the centralizer of the sample fold

CEN = sorted(h for h in G384 if compose(h, GREP) == compose(GREP, h))
CSETG = set(CEN)
CCLOSED = all(compose(a, b) in CSETG for a in CEN for b in CEN)
AX0 = [h for h in CEN if h[0][0] == 0]
FIXS = set(FIX)
HIMG = {}
WIMG = None
HOLDS = 0
for h in CEN:
    pmx = permof(h)
    PCACHE.clear()
    HIMG[h] = [pmx[c] for c in FIX]
    if h == ((0, 1, 2, 3), 1):
        WIMG = [pmx[c] for c in WCUT]
    if set(HIMG[h]) == FIXS:
        HOLDS += 1

gate(len(CEN) == 32 and CCLOSED and len(AX0) == 16 and HOLDS == 32, "G7",
     "the centralizer of the sample fold has order {0}, closed under composition, {1} members hold axis 0, all {0} hold the {2} cuttings"
     .format(len(CEN), len(AX0), NFIX))

# ================================================================ G8 centralizer orbits on the held set

PAR = list(range(NFIX))


def find(a):
    while PAR[a] != a:
        PAR[a] = PAR[PAR[a]]
        a = PAR[a]
    return a


for h in CEN:
    im = HIMG[h]
    for i in range(NFIX):
        ra, rb = find(i), find(POSF[im[i]])
        if ra != rb:
            PAR[ra] = rb
ORB = Counter(find(i) for i in range(NFIX))
OCEN = dict(sorted(Counter(ORB.values()).items()))

gate(len(ORB) == 31 and OCEN == {4: 4, 8: 14, 16: 13} and sum(ORB.values()) == NFIX, "G8",
     "the centralizer has {0} orbits on the {1} held cuttings, size census {2}"
     .format(len(ORB), NFIX, dshow(OCEN)))

# ================================================================ G9 the side flip pairs the held set freely

SFL = ((0, 1, 2, 3), 1)
SCOMM = all(compose(SFL, g) == compose(g, SFL) for g in DIST)
SIMG = HIMG[SFL]
SFIX = sum(1 for i in range(NFIX) if SIMG[i] == FIX[i])
SCYC = cycen(SIMG, POSF, FIX)
FREEH = []
PURE2 = []
for h in CEN:
    im = HIMG[h]
    if sum(1 for i in range(NFIX) if im[i] == FIX[i]) == 0:
        FREEH.append(h)
        if cycen(im, POSF, FIX) == {2: NFIX // 2}:
            PURE2.append(h)

gate(SCOMM and SFL in CEN and SFIX == 0 and SCYC == {2: NFIX // 2} and len(FREEH) == 12 and len(PURE2) == 4, "G9",
     "the axis-0 side flip commutes with all {0} folds and pairs the {1} held cuttings with no fixed member, cycle census {2}"
     .format(len(DIST), NFIX, dshow(SCYC)))
emit("G9 detail: {0} of the {1} centralizer members hold no cutting of the {2} and {3} of those are pure two-cycles, so the global count is even"
     .format(len(FREEH), len(CEN), NFIX, len(PURE2)))

# ================================================================ G10 per-fiber rigidity persists

REPF = GFIBS[0]
R14 = frozenset(c for c in FL[REPF] if GPM[c] == c)
HOLD14 = [h for h in CEN if frozenset(HIMG[h][POSF[c]] for c in R14) == R14]
F14 = dict((f, frozenset(c for c in FL[f] if GPM[c] == c)) for f in GFIBS)
BACK = dict((F14[f], f) for f in GFIBS)
HITC = Counter()
ONTO = 0
for h in AX0:
    img = frozenset(HIMG[h][POSF[c]] for c in R14)
    if img in BACK:
        ONTO += 1
        HITC[BACK[img]] += 1
POSW = {c: i for i, c in enumerate(WCUT)}
FIBOF = {}
for f in GFIBS:
    for c in FL[f]:
        FIBOF[c] = f
SPERM = {}
SWELL = 0
for f in GFIBS:
    tg = set(FIBOF.get(WIMG[POSW[c]], -1) for c in FL[f])
    if len(tg) == 1:
        SWELL += 1
    SPERM[f] = sorted(tg)[0]
SFIXF = sum(1 for f in GFIBS if SPERM[f] == f)
STWO = sum(1 for f in GFIBS if SPERM[f] != f and SPERM[SPERM[f]] == f)
SPAIRS = sorted((E36[f], E36[SPERM[f]]) for f in GFIBS if f < SPERM[f])
PMAP = {}
PWELL = True
for c in FIX:
    a, b = PAIROF[c], PAIROF[SIMG[POSF[c]]]
    if a in PMAP and PMAP[a] != b:
        PWELL = False
    PMAP[a] = b
SSTAB = sorted(p for p in PMAP if PMAP[p] == p)
SPOK = 0
for p in SSTAB:
    mem = [c for c in FIX if PAIROF[c] == p]
    if not (len(mem) & 1) and sum(1 for c in mem if SIMG[POSF[c]] == c) == 0:
        SPOK += 1

gate(HOLD14 == [GID, GREP] and len(R14) == 14 and len(AX0) == 16 and ONTO == 16 and set(HITC.values()) == set([2])
     and len(HITC) == 8 and SWELL == 8 and SFIXF == 0 and STWO == 8 and len(SPAIRS) == 4 and PWELL
     and len(SSTAB) == 6 and SPOK == 6, "G10",
     "only {0} centralizer members hold the sample fiber's {1} cuttings; the {2} axis-0 members hit each of the {3} fibers {4} times"
     .format(len(HOLD14), len(R14), len(AX0), len(HITC), sorted(set(HITC.values()))[0]))
emit("G10 detail: the side flip pairs the fibers {0}, holding none of the {1}"
     .format(" ".join("({0},{1})-({2},{3})".format(x[0][0], x[0][1], x[1][0], x[1][1]) for x in SPAIRS), len(GFIBS)))
emit("G10 detail: {0} of the {1} letter pairs are held by the side flip, {2}, each with an even count and none fixed"
     .format(len(SSTAB), len(PCNT), pshow(SSTAB)))

# ================================================================ G11 the quotient enumeration

MPK = dict((t, KIDX[frozenset(actcorner(GREP, v) for v in KEPT[t])]) for t in range(NK))
ORBS = []
SING = 0
OVL = 0
SEEN = set()
for t in range(NK):
    if t in SEEN:
        continue
    u = MPK[t]
    SEEN.add(t)
    SEEN.add(u)
    if u == t:
        SING += 1
    if MASK[t] & MASK[u]:
        OVL += 1
    ORBS.append((t, u))
OM = [MASK[a] | MASK[b] for (a, b) in ORBS]
OBY = [[] for _ in range(NPTS)]
for i in range(len(ORBS)):
    mm = OM[i]
    while mm:
        low = mm & (-mm)
        OBY[low.bit_length() - 1].append(i)
        mm ^= low
QS = []


def qsearch(cov, ch):
    if cov == UNIV:
        QS.append(tuple(ch))
        return
    fr = UNIV & (~cov)
    p = (fr & (-fr)).bit_length() - 1
    for i in OBY[p]:
        m = OM[i]
        if m & cov:
            continue
        ch.append(i)
        qsearch(cov | m, ch)
        ch.pop()


qsearch(0, [])
QSIZE = sorted(set(len(s) for s in QS))
QP = set(frozenset(x for i in s for x in ORBS[i]) for s in QS)
FP = set(CSET[c] for c in FIX)

gate(len(ORBS) == 200 and SING == 0 and OVL == 0 and len(QS) == 336 and QSIZE == [12] and len(QP) == len(QS)
     and QP == FP, "G11",
     "the {0} kept pieces give {1} two-orbits, no singleton and no overlap; the cover of the {2} sample points has {3} solutions of {4}"
     .format(NK, len(ORBS), NPTS, len(QS), QSIZE[0]))
emit("G11 detail: the {0} quotient solutions are exactly the {1} cuttings the fold holds, as sets of pieces"
     .format(len(QP), NFIX))

# ================================================================ G12 the two readings agree on letter pairs

QPC = Counter(PAIROF[SIDX[q]] for q in QP)
QCEN = dict(sorted(Counter(QPC.values()).items()))

gate(QPC == PCNT and QCEN == PCEN and len(QPC) == 16, "G12",
     "the {0} quotient solutions carry the same {1} letter pairs with count census {2}"
     .format(len(QP), len(QPC), dshow(QCEN)))

# ================================================================ totals

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
emit("resource: under {0} s, under {1} MB".format(((int(time.time() - T0) // 60) + 1) * 60, ((PEAK // 250) + 1) * 250))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
