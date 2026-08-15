"""Physical cell cutting: the free fold reduction, full-group rigidity, the parity reduction, and quotient structure at the interface wall.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, the slot-preserving subgroup of order ninety-six for axis zero, and the sixteen-letter facet alphabet. Nothing outside
that finite object enters any gate.

The target of this cycle is again the evenness of the 48 stubborn interface fibers, the entry-36 orbit of the interface reading. The cover
action is extended to the whole cell group and the fold element of each stubborn fiber is exhibited: widening the group from ninety-six to
384 adds no element, the fold acts freely on corners, on kept pieces and on used pieces, and it therefore folds each stubborn fiber onto a
smaller invariant set with no fixed piece anywhere. That reduction, two refutations that keep it honest, the distance structure of the
folded set, and the letter-functional quotient that sees the heavy letters but not the wall are the content of the gates below.

Gates G1 to G14, one line each with a few detail lines, then a resource line and the total line. Any failure exits nonzero."""

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


def cshow(d):
    return " ".join("{0}:{1}".format(k, d[k]) for k in sorted(d))


def lshow(v):
    return "[" + ",".join("{0}".format(x) for x in v) + "]"


def pc(x):
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
NCOR = len(set(len(KEPT[t]) for t in USED))
CORNS = sorted(set(len(KEPT[t]) for t in USED))[0]

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
NONSW = [g for g in STAB if not (g[1] & 1)]
SWAPS = [g for g in STAB if (g[1] & 1)]
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


# ================================================================ G1 the declared object

gate(len(CAND) == 2672 and FLOOR == 6 and len(KEPT) == 400 and NS == 15800 and PSIZE == 1 and CSIZE == 24
     and NU == 192 and NCOR == 1 and CORNS == 5 and len(G384) == 384 and len(STAB) == 96 and PBAD == 0, "G1",
     "{0} five-corner unit-volume pieces, cost floor {1}, {2} kept, {3} cuttings of {4}, {5} used, cell group {6}, slot subgroup {7}"
     .format(len(CAND), FLOOR, len(KEPT), NS, CSIZE, NU, len(G384), len(STAB)))

# ================================================================ G2 the alphabet and the wall

MULT = [Counter(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
NSLOT = len(MULT)
MSAME = all(m == MULT[0] for m in MULT)
MCEN = dict(sorted(Counter(MULT[0].values()).items()))
HEAVY = sorted(k for k in range(NL) if MULT[0][k] == 1364)
JC = Counter((KEY[i][(0, 0)], KEY[i][(0, 1)]) for i in range(NS))
TR = [[JC[(x, y)] for y in range(NL)] for x in range(NL)]
TRC = sum(TR[x][x] for x in range(NL))
N36 = sum(1 for x in range(NL) for y in range(NL) if TR[x][y] == 36)
FIB = {}
for i in range(NS):
    FIB.setdefault((KEY[i][(0, 0)], KEY[i][(0, 1)]), []).append(i)
E36 = sorted(kj for kj in FIB if TR[kj[0]][kj[1]] == 36)
FSZ = sorted(set(len(FIB[kj]) for kj in E36))
NF = len(E36)
WSZ = FSZ[0]

gate(NL == 16 and MSAME and NSLOT == 8 and MCEN == {862: 12, 1364: 4} and len(HEAVY) == 4
     and TRC == 2000 and N36 == 48 and NF == 48 and FSZ == [36], "G2",
     "{0} letters on each of {1} slots, multiplicity census {2}, trace {3}, {4} entries at {5}, {6} fibers of {5} cuttings"
     .format(NL, NSLOT, dshow(MCEN), TRC, N36, WSZ, NF))

# ================================================================ G3 the whole cell group on the cuttings

FL = [FIB[kj] for kj in E36]
FS = [set(F) for F in FL]
POS = [dict((c, x) for x, c in enumerate(F)) for F in FL]
REPI = 0
SSET = set(STAB)
STCNT = [0] * NF
NTRIV = [[] for _ in range(NF)]
REPIMG = []
DEFECT = 0
for g in G384:
    pm = permof(g)
    PCACHE.clear()
    if len(set(pm)) != NS:
        DEFECT += 1
    REPIMG.append([pm[c] for c in FL[REPI]])
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
                NTRIV[f].append((g, [POS[f][pm[c]] for c in FL[f]]))

SCEN = dict(sorted(Counter(STCNT).items()))
NONE1 = sum(1 for f in range(NF) if len(NTRIV[f]) == 1)
INSUB = sum(1 for f in range(NF) for (g, im) in NTRIV[f] if g in SSET)
SIDESW = sum(1 for f in range(NF) for (g, im) in NTRIV[f] if g[0][0] == 0 and (g[1] & 1))

gate(DEFECT == 0 and SCEN == {2: 48} and NONE1 == 48 and INSUB == 48 and SIDESW == 48, "G3",
     "all {0} maps permute the {1} cuttings, {2} defects; setwise fiber stabilizer census {3}, all inside the {4}, side-swapping {5} of {6}"
     .format(len(G384), NS, DEFECT, dshow(SCEN), len(STAB), SIDESW, NF))

# ================================================================ G4 the fold on corners, kept pieces, used pieces

GS = [NTRIV[f][0][0] for f in range(NF)]
IMG = [NTRIV[f][0][1] for f in range(NF)]
US = set(USED)
NK = len(KEPT)
CTYPE = Counter()
CFIX = Counter()
KFIX = Counter()
KORB = Counter()
UORB = Counter()
UCLOSED = 0
MPS = []
for f in range(NF):
    g = GS[f]
    cyc = Counter()
    seen = set()
    for v in range(len(CORN)):
        if v in seen:
            continue
        x = v
        n = 0
        while True:
            seen.add(x)
            x = actcorner(g, x)
            n += 1
            if x == v:
                break
        cyc[n] += 1
    CTYPE[tuple(sorted(cyc.items()))] += 1
    CFIX[cyc.get(1, 0)] += 1
    mp = dict((t, KIDX[frozenset(actcorner(g, v) for v in KEPT[t])]) for t in range(NK))
    MPS.append(mp)
    KFIX[sum(1 for t in range(NK) if mp[t] == t)] += 1
    KORB[len(set(frozenset((t, mp[t])) for t in range(NK)))] += 1
    UORB[len(set(frozenset((t, mp[t])) for t in USED))] += 1
    if all(mp[t] in US for t in USED):
        UCLOSED += 1


def cyshow(d):
    return "{" + ", ".join("({0}, {1}): {2}".format(k[0][0], k[0][1], d[k]) for k in sorted(d)) + "}"


CT1 = len(CTYPE) == 1 and len(sorted(CTYPE)[0]) == 1
gate(CT1 and sorted(CTYPE)[0] == ((2, 8),) and CTYPE[((2, 8),)] == 48 and CFIX == {0: 48} and KFIX == {0: 48}
     and KORB == {200: 48} and UORB == {96: 48} and UCLOSED == 48, "G4",
     "corner cycle types {0} at {1} fixed corners; fixed kept pieces {2}; {3} kept and {4} used two-orbits, used set closed {5} of {6}"
     .format(cyshow(CTYPE), sorted(CFIX)[0], dshow(KFIX), sorted(KORB)[0], sorted(UORB)[0], UCLOSED, NF))

# ================================================================ G5 the parity reduction on each fiber

FIXC = Counter()
TWOC = Counter()
LONG = 0
FIXSETS = []
for f in range(NF):
    im = IMG[f]
    n = len(im)
    fx = [x for x in range(n) if im[x] == x]
    tw = 0
    for x in range(n):
        if im[x] != x:
            if im[im[x]] == x:
                tw += 1
            else:
                LONG += 1
    FIXC[len(fx)] += 1
    TWOC[tw // 2] += 1
    FIXSETS.append([FL[f][x] for x in fx])
ALLFIX = [c for F in FIXSETS for c in F]
NFIX = sorted(FIXC)[0]
NTWO = sorted(TWOC)[0]

gate(FIXC == {14: 48} and TWOC == {11: 48} and LONG == 0 and len(ALLFIX) == 672 and len(set(ALLFIX)) == 672
     and WSZ == NFIX + 2 * NTWO, "G5",
     "each fold fixes {0} of its {1} cuttings and pairs the rest, {1} = {0} + 2 x {2}; census {3}; {4} folded cuttings, all distinct"
     .format(NFIX, WSZ, NTWO, dshow(FIXC), len(ALLFIX)))

# ================================================================ G6 no fixed piece inside a folded cutting

PFIX = Counter()
PSWAP = Counter()
for f in range(NF):
    mp = MPS[f]
    for c in FIXSETS[f]:
        s = SOLS[c]
        PFIX[sum(1 for t in s if mp[t] == t)] += 1
        PSWAP[len(set(frozenset((t, mp[t])) for t in s))] += 1

gate(PFIX == {0: 672} and PSWAP == {12: 672}, "G6",
     "each of the {0} folded cuttings splits into {1} swapped piece-pairs with no fixed piece: censuses {2} and {3}"
     .format(len(ALLFIX), sorted(PSWAP)[0], dshow(PFIX), dshow(PSWAP)))

# ================================================================ G7 no free element on any fiber

FREEF = 0
for f in range(NF):
    for (g, im) in NTRIV[f]:
        if all(im[x] != x for x in range(len(im))):
            FREEF += 1
            break

gate(FREEF == 0 and set(STCNT) == set([2]), "G7",
     "each fiber is held setwise by {0} of the {1} maps and no more; fibers carrying a fold with no fixed cutting: {2} of {3}"
     .format(sorted(set(STCNT))[0], len(G384), FREEF, NF))

# ================================================================ G8 rigidity of the folded set

RFIX = FIXSETS[REPI]
RFIXS = set(RFIX)
SRC = FL[REPI]
KEEPFIX = 0
ACTID = 0
for gi in range(len(G384)):
    im = REPIMG[gi]
    imgset = set(im[x] for x in range(len(SRC)) if SRC[x] in RFIXS)
    if imgset == RFIXS:
        KEEPFIX += 1
        if all(im[x] == SRC[x] for x in range(len(SRC)) if SRC[x] in RFIXS):
            ACTID += 1
SUP = set()
INTER = None
for c in RFIX:
    s = set(SOLS[c])
    SUP |= s
    INTER = s if INTER is None else (INTER & s)

gate(KEEPFIX == 2 and ACTID == 2 and len(RFIX) == 14 and len(SUP) == 80 and len(INTER) == 0, "G8",
     "on the sample fiber {0} of the {1} maps hold the {2} folded cuttings and both act as the identity on them; support {3}, common part {4}"
     .format(KEEPFIX, len(G384), len(RFIX), len(SUP), len(INTER)))

# ================================================================ G9 distances inside the folded set

RSETS = [CSET[c] for c in RFIX]
DC = Counter()
PAIR12 = []
DISJ = 0
for x in range(len(RFIX)):
    for y in range(x + 1, len(RFIX)):
        sh = len(RSETS[x] & RSETS[y])
        DC[2 * CSIZE - 2 * sh] += 1
        if 2 * CSIZE - 2 * sh == 12:
            PAIR12.append((x, y, sh))
        if sh == 0:
            DISJ += 1
NPAIR = len(RFIX) * (len(RFIX) - 1) // 2
MPREP = MPS[REPI]
SP = [set(frozenset((t, MPREP[t])) for t in SOLS[c]) for c in RFIX]
ALLSP = set()
for s in SP:
    ALLSP |= s
AVAIL = len(set(frozenset((t, MPREP[t])) for t in USED))
SH12 = PAIR12[0][2] if len(PAIR12) == 1 else -1
SW12 = len(SP[PAIR12[0][0]] & SP[PAIR12[0][1]]) if len(PAIR12) == 1 else -1
DTARG = {8: 11, 12: 1, 16: 10, 20: 5, 24: 4, 28: 14, 32: 4, 36: 14, 40: 10, 44: 6, 48: 12}

gate(dict(DC) == DTARG and sum(DC.values()) == NPAIR and NPAIR == 91 and len(PAIR12) == 1 and SH12 == 18
     and SW12 == 9 and DISJ == 12 and len(ALLSP) == 40 and AVAIL == 96, "G9",
     "exchange distances over the {0} folded pairs: {1}".format(NPAIR, cshow(DC)))
emit("G9 detail: the one distance-{0} pair shares {1} pieces and {2} of {3} swapped pairs; {4} pairs fully apart; {5} swapped pairs of {6}"
     .format(12, SH12, SW12, sorted(PSWAP)[0], DISJ, len(ALLSP), AVAIL))

# ================================================================ G10 joint frame classes on the folded set

FRM0 = []
FRM1 = []
for s in SOLS:
    FRM0.append(frozenset(t for t in s if (t, 0, 0) in FACE))
    FRM1.append(frozenset(t for t in s if (t, 0, 1) in FACE))
JOINT = [(FRM0[i], FRM1[i]) for i in range(NS)]

CLSN = Counter()
SIZEMS = Counter()
ODDCL = Counter()
CROSS = Counter()
FIXDIST = Counter()
INSIDE = 0
WELLDEF = 0
for f in range(NF):
    F = FL[f]
    im = IMG[f]
    cls = {}
    order = []
    for c in F:
        k = JOINT[c]
        if k not in cls:
            cls[k] = len(order)
            order.append(k)
    lab = [cls[JOINT[c]] for c in F]
    nc = len(order)
    CLSN[nc] += 1
    sizes = Counter(lab)
    SIZEMS[tuple(sorted(sizes.values()))] += 1
    ODDCL[sum(1 for v in sizes.values() if v & 1)] += 1
    cmap = {}
    ok = True
    for x in range(len(F)):
        a = lab[x]
        b = lab[im[x]]
        if a in cmap and cmap[a] != b:
            ok = False
        cmap[a] = b
    if ok:
        WELLDEF += 1
    fo = so = fe = se = 0
    for a in range(nc):
        odd = sizes[a] & 1
        if cmap[a] == a:
            fo, fe = (fo + 1, fe) if odd else (fo, fe + 1)
        else:
            so, se = (so + 1, se) if odd else (so, se + 1)
    CROSS[(fo, so, fe, se)] += 1
    fixin = Counter()
    fixcls = set()
    for x in range(len(F)):
        if im[x] == x:
            fixin[lab[x]] += 1
            fixcls.add(lab[x])
    FIXDIST[tuple(sorted(Counter(fixin.get(a, 0) for a in range(nc)).items()))] += 1
    if all(cmap[a] == a for a in fixcls):
        INSIDE += 1
SMS = sorted(SIZEMS)[0]
CRS = sorted(CROSS)[0]
FDD = dict(sorted(FIXDIST)[0])

gate(CLSN == {14: 48} and len(SIZEMS) == 1 and SMS == (1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 5, 5, 5) and ODDCL == {8: 48}
     and len(CROSS) == 1 and CRS == (4, 4, 2, 4) and WELLDEF == 48 and len(FIXDIST) == 1
     and FDD == {0: 8, 1: 1, 2: 2, 3: 3} and INSIDE == 48, "G10",
     "in all {0} fibers {1} joint frame classes of sizes {2}, {3} of them odd, split ({4}, {5}, {6}, {7})"
     .format(NF, sorted(CLSN)[0], lshow(SMS), sorted(ODDCL)[0], CRS[0], CRS[1], CRS[2], CRS[3]))
emit("G10 detail: folded cuttings per class {0}; the class map is well defined in {1} fibers, each folded cutting in a held class"
     .format(dshow(FDD), WELLDEF))

# ================================================================ G11 the degree-parity refutation

NV = 25
EXACT = [0] * NV
ATL = [0] * (NV + 1)
MAXODD = 0
DEG0 = set()
for f in range(NF):
    FX = FIXSETS[f]
    n = len(FX)
    sets = [CSET[c] for c in FX]
    cnt = [Counter() for _ in range(n)]
    for x in range(n):
        for y in range(x + 1, n):
            sh = len(sets[x] & sets[y])
            cnt[x][sh] += 1
            cnt[y][sh] += 1
    suf = []
    for c in cnt:
        acc = 0
        row = [0] * (NV + 1)
        for v in range(NV - 1, -1, -1):
            acc += c.get(v, 0)
            row[v] = acc
        suf.append(row)
    for v in range(NV):
        no = sum(1 for x in range(n) if cnt[x].get(v, 0) & 1)
        if no == n:
            EXACT[v] += 1
        MAXODD = max(MAXODD, no)
    for v in range(NV):
        no = sum(1 for x in range(n) if suf[x][v] & 1)
        if no == n:
            ATL[v] += 1
        if v >= 1:
            MAXODD = max(MAXODD, no)
    DEG0 |= set(suf[x][0] for x in range(n))
NRULE = NV + NV - 1

gate(max(EXACT) == 0 and max(ATL[1:]) == 0 and ATL[0] == 48 and DEG0 == set([13]) and MAXODD == 10, "G11",
     "{0} shared-count rules on the {1} folded cuttings all pass {2} of {3} fibers; the at-least-zero rule passes {3} of {3} at degree {4}"
     .format(NRULE, len(RFIX), max(EXACT), NF, sorted(DEG0)[0]))
emit("G11 detail: the at-least-zero rule is the complete graph, tautological and excluded; the best other rule makes {0} of {1} degrees odd"
     .format(MAXODD, len(RFIX)))

# ================================================================ G12 the letter-tetra incidence and its left kernel

TALL = sorted(set(tet for L in ALLK for tet in L), key=lambda ff: sorted(ff))
NT = len(TALL)
AM = [[1 if TALL[a] in ALLK[k] else 0 for a in range(NT)] for k in range(NL)]
RSUM = sorted(set(sum(r) for r in AM))
CSUM = sorted(set(sum(AM[k][a] for k in range(NL)) for a in range(NT)))
ROWS = []
for k in range(NL):
    r = 0
    for a in range(NT):
        if AM[k][a]:
            r |= (1 << a)
    ROWS.append(r)
BASIS = {}
KER = []
for k in range(NL):
    x, tg = ROWS[k], 1 << k
    while x:
        b = x.bit_length() - 1
        if b in BASIS:
            x ^= BASIS[b][0]
            tg ^= BASIS[b][1]
        else:
            BASIS[b] = (x, tg)
            x = 0
            break
    else:
        KER.append(tg)
RKA = len(BASIS)
FUNCS = []
for mask in range(1 << len(KER)):
    v = 0
    for b in range(len(KER)):
        if (mask >> b) & 1:
            v ^= KER[b]
    FUNCS.append(v)
MISS = 0
for v in FUNCS:
    acc = 0
    for k in range(NL):
        if (v >> k) & 1:
            acc ^= ROWS[k]
    if acc != 0:
        MISS += 1
SIG = dict((k, tuple((u >> k) & 1 for u in KER)) for k in range(NL))
CLS = {}
for k in range(NL):
    CLS.setdefault(SIG[k], []).append(k)
CLASSES = sorted(CLS.values())
SING = [c[0] for c in CLASSES if len(c) == 1]
PAIRS = [c for c in CLASSES if len(c) == 2]

gate(NT == 24 and RSUM == [6] and CSUM == [4] and RKA == 10 and len(KER) == 6 and len(FUNCS) == 64
     and len(set(FUNCS)) == 64 and MISS == 0 and len(CLASSES) == 10 and len(PAIRS) == 6 and SING == HEAVY, "G12",
     "incidence {0} by {1}, row sums {2}, column sums {3}, rank {4} over two elements, kernel dimension {5}, {6} functionals, {7} letter types"
     .format(NL, NT, RSUM[0], CSUM[0], RKA, len(KER), len(FUNCS), len(CLASSES)))
emit("G12 detail: types {0} and singletons {1}, exactly the {2} letters of multiplicity {3}"
     .format(" ".join("+".join("{0}".format(k) for k in c) for c in PAIRS), lshow(SING), len(SING), 1364))

# ================================================================ G13 the kernel under the folds

PSIL = [PSI[GS[f]] for f in range(NF)]
NDIST = len(set(PSIL))
KSET = set(FUNCS)
INV = 0
for ps in PSIL:
    if all(sum(1 << ps[k] for k in range(NL) if (u >> k) & 1) in KSET for u in FUNCS):
        INV += 1
PAR = dict((u, u) for u in FUNCS)


def find(a):
    while PAR[a] != a:
        PAR[a] = PAR[PAR[a]]
        a = PAR[a]
    return a


for ps in PSIL:
    for u in FUNCS:
        w = sum(1 << ps[k] for k in range(NL) if (u >> k) & 1)
        ra, rb = find(u), find(w)
        if ra != rb:
            PAR[ra] = rb
ORB = Counter(find(u) for u in FUNCS)
OCEN = dict(sorted(Counter(ORB.values()).items()))
FIXALL = sum(1 for u in FUNCS if all(sum(1 << ps[k] for k in range(NL) if (u >> k) & 1) == u for ps in PSIL))

gate(INV == 48 and NDIST == 6 and OCEN == {1: 2, 3: 2, 4: 2, 6: 2, 12: 3} and len(ORB) == 11 and FIXALL == 2, "G13",
     "all {0} folds hold the kernel and induce {1} distinct letter maps; orbit census {2}, {3} orbits, {4} held pointwise"
     .format(INV, NDIST, dshow(OCEN), len(ORB), FIXALL))

# ================================================================ G14 pair orbits and the kernel signature

CLSID = {}
for ci, c in enumerate(CLASSES):
    for k in c:
        CLSID[k] = ci
PARP = {}
for k in range(NL):
    for j in range(NL):
        PARP[(k, j)] = (k, j)


def findp(a):
    while PARP[a] != a:
        PARP[a] = PARP[PARP[a]]
        a = PARP[a]
    return a


for g in NONSW:
    ps = PSI[g]
    for k in range(NL):
        for j in range(NL):
            ra, rb = findp((k, j)), findp((ps[k], ps[j]))
            if ra != rb:
                PARP[ra] = rb
GRP = {}
for k in range(NL):
    for j in range(NL):
        GRP.setdefault(findp((k, j)), []).append((k, j))
ROWSIG = []
for r in GRP:
    mem = GRP[r]
    vals = sorted(set(TR[a][b] for (a, b) in mem))
    ss = tuple(sorted(set(tuple(sorted((CLSID[a], CLSID[b]))) for (a, b) in mem)))
    ROWSIG.append((vals[0], len(vals), len(mem), ss))
SIGSET = set(r[3] for r in ROWSIG)
S36 = [r for r in ROWSIG if r[0] == 36]
S52 = [r for r in ROWSIG if r[0] == 52]
S90 = [r for r in ROWSIG if r[0] == 90]
S100 = [r for r in ROWSIG if r[0] == 100]
SHARE36 = sorted((r[0], r[2]) for r in ROWSIG if r[3] == S36[0][3]) if S36 else []
ONEVAL = all(r[1] == 1 for r in ROWSIG)

gate(len(GRP) == 12 and ONEVAL and len(S36) == 1 and S36[0][2] == 48 and len(SIGSET) == 7
     and S36[0][3] == S52[0][3] and S90[0][3] == S100[0][3] and SHARE36 == [(36, 48), (52, 48)], "G14",
     "{0} pair orbits under the {1} side-preserving letter maps, the {2} wall entries one orbit; {3} distinct kernel signatures"
     .format(len(GRP), len(NONSW), S36[0][2], len(SIGSET)))
emit("G14 detail: the wall signature is shared with the entry-{0} orbit and entry-{1} matches entry-{2}, so the wall is not singled out"
     .format(S52[0][0], S90[0][0], S100[0][0]))

# ================================================================ totals

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
emit("resource: under {0} s, under {1} MB".format(((int(time.time() - T0) // 60) + 1) * 60, ((PEAK // 250) + 1) * 250))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
