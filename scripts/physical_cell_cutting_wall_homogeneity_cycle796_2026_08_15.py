"""Physical cell cutting: the wall action is exactly the first-axis cell maps, the fold is the entry stabilizer, the split is frame stable.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, and the sixteen-letter facet alphabet on the two slots of axis zero. Nothing outside that finite object enters any gate.

Earlier cycles built the wall of 48 interface entries of value 36, gave every entry a fold that holds its fiber setwise, and linearized each
fiber: rows are the two-orbits of the 400 kept pieces under that fold, the fold-held cuttings are weight-twelve vectors on the rows that
occur, and the exact cover condition is an all-ones linear system. This cycle asks which cell maps move the wall itself. It tests every one
of the 384 maps for a well-defined induced map on the 48 entries, reads the orbit and the stabilizers of the acting set, identifies each
stabilizer with that fiber's own fold as computed by the separate per-fiber search, transports folds by conjugation, and rebuilds every
fiber instance on a second generic sample frame to separate a property of the instance from a property of how it is embedded relative to
the transfer frame. Gates G1 to G10, one line each with a few detail lines, then the total line. Any failure exits nonzero.
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
OFFS2 = (3, 5, 6, 7)
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


def rref(rows, ncols):
    mat = [r for r in rows if r]
    piv = []
    r = 0
    for c in range(ncols):
        p = -1
        for i in range(r, len(mat)):
            if (mat[i] >> c) & 1:
                p = i
                break
        if p < 0:
            continue
        mat[r], mat[p] = mat[p], mat[r]
        for i in range(len(mat)):
            if i != r and ((mat[i] >> c) & 1):
                mat[i] ^= mat[r]
        piv.append(c)
        r += 1
    return mat[:r], piv


# ================================================================ G1 the declared object, the alphabet and the wall

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
FSZ = sorted(set(len(FIB[kj]) for kj in E36))

gate(len(CAND) == 2672 and FLOOR == 6 and NK == 400 and NS == 15800 and PSIZE == 1 and CSIZE == 24 and NU == 192
     and len(G384) == 384 and NL == 16 and TRC == 2000 and N36 == 48 and NF == 48 and FSZ == [36], "G1",
     "{0} pieces, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, cell group {6}, {7} letters, trace {8}, {9} entries at {10}"
     .format(len(CAND), FLOOR, NK, NS, CSIZE, NU, len(G384), NL, TRC, N36, 36))

# ================================================================ the fold of every fiber, by the independent per-fiber search

FL = [FIB[kj] for kj in E36]
FS = [set(F) for F in FL]
WALL = sorted(set(c for F in FL for c in F))
POSW = {c: i for i, c in enumerate(WALL)}
FOLD = [None] * NF
STCNT = [0] * NF
DEFECT = 0
for g in G384:
    mp = piecemap(g, USED)
    if len(set(mp.values())) != NU:
        DEFECT += 1
    img = [SIDX[frozenset(mp[t] for t in SOLS[c])] for c in WALL]
    for f in range(NF):
        S = FS[f]
        ok = True
        for c in FL[f]:
            if img[POSW[c]] not in S:
                ok = False
                break
        if ok:
            STCNT[f] += 1
            if g != GID:
                FOLD[f] = g

DIST = sorted(set(FOLD))
FIDX = {g: i for i, g in enumerate(DIST)}
FOLDOK = DEFECT == 0 and set(STCNT) == set([2]) and all(compose(g, g) == GID for g in DIST)

# ================================================================ the two-orbit table of each fold

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

# ================================================================ the fiber instance, rebuilt on any sample frame

MEMB = [len(o) for o in ORBS]


def instance(f, MX):
    """Rebuild fiber f from the two-orbits of its fold: held cuttings as row vectors, point supports of the rows on the given frame,
    the kernel dimension of the incidence system, the equal-union exchanges of the rows, and the broken count of each exchange."""
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
    pat = []
    for p in range(NPTS):
        q = 0
        for i in range(nr):
            if (sup[i] >> p) & 1:
                q |= (1 << i)
        pat.append(q)
    red, piv = rref(pat, nr)
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
                spl[ma | mb] = (ma, mb, popc(u))
    brk = Counter()
    for dv in spl:
        ma, mb, usz = spl[dv]
        for w in vecs:
            x = w & dv
            if x != 0 and x != ma and x != mb:
                brk[dv] += 1
    tab = tuple(sorted((brk[dv], spl[dv][2]) for dv in spl))
    return {"held": held, "rowg": rowg, "nr": nr, "orbs": orbs, "vecs": vecs,
            "kdim": nr - len(piv), "spl": spl, "brk": brk, "tab": tab}


def dvpieces(d, dv):
    ps = set()
    for i in range(d["nr"]):
        if (dv >> i) & 1:
            ps |= set(d["orbs"][d["rowg"][i]])
    return frozenset(ps)


# ================================================================ G2 which cell maps act on the wall at all

EIDX = dict((e, i) for i, e in enumerate(E36))
ACT = []
FAIL0 = 0
FAILR = 0
ACTR = 0
for g in G384:
    pmp = piecemap(g, USED)
    em = [-1] * NF
    okg = True
    for f in range(NF):
        tgt = set()
        for c in FL[f]:
            j = SIDX.get(frozenset(pmp[t] for t in SOLS[c]))
            if j is None:
                okg = False
                break
            tgt.add(PAIROF[j])
        if not okg or len(tgt) != 1:
            okg = False
            break
        te = sorted(tgt)[0]
        if te not in EIDX:
            okg = False
            break
        em[f] = EIDX[te]
    if okg:
        ACT.append((g, tuple(em)))
        if g[0][0] != 0:
            ACTR += 1
    elif g[0][0] == 0:
        FAIL0 += 1
    else:
        FAILR += 1

NA = len(ACT)
EMOF = dict(ACT)
IDEM = tuple(range(NF))
NPAIR = NA * NA
CLOSN = 0
FWD = 0
REV = 0
for g, eg in ACT:
    for h, eh in ACT:
        ec = EMOF.get(compose(g, h))
        if ec is None:
            continue
        CLOSN += 1
        if ec == tuple(eg[eh[f]] for f in range(NF)):
            FWD += 1
        if ec == tuple(eh[eg[f]] for f in range(NF)):
            REV += 1
IDOK = EMOF.get(GID) == IDEM
ONEOR = (FWD == NPAIR) != (REV == NPAIR)
ORIENT = "em[g after h] = em[g] after em[h]" if FWD == NPAIR else "em[g after h] = em[h] after em[g]"

gate(NA == 96 and FAIL0 == 0 and FAILR == 288 and ACTR == 0 and CLOSN == NPAIR and NPAIR == 9216 and IDOK and ONEOR, "G2",
     "exactly {0} of the {1} cell maps induce a well-defined map on the {2} wall entries: every map fixing the first axis acts, {3} fail"
     .format(NA, len(G384), NF, FAILR))
emit("G2 detail: {0} first-axis maps fail and {1} maps moving the first axis act; the identity induces the identity"
     .format(FAIL0, ACTR))
emit("G2 detail: one ordering holds, {0}, at {1} of {2} pairs, all of them acting maps; the other ordering holds at {3}"
     .format(ORIENT, FWD if FWD == NPAIR else REV, NPAIR, REV if FWD == NPAIR else FWD))

# ================================================================ G3 one orbit

par = list(range(NF))


def findp(a):
    while par[a] != a:
        par[a] = par[par[a]]
        a = par[a]
    return a


for g, em in ACT:
    for f in range(NF):
        a, b = findp(f), findp(em[f])
        if a != b:
            par[a] = b
OSZ = sorted(Counter(findp(f) for f in range(NF)).values())

gate(OSZ == [NF] and NF == 48, "G3",
     "the acting maps carry the {0} wall entries in one orbit of size {1}: every entry is carried to every other entry"
     .format(NF, OSZ[0]))

# ================================================================ G4 and G5 stabilizers, and the fold

STORD = Counter()
STFOLD = 0
for f in range(NF):
    els = [g for g, em in ACT if em[f] == f]
    STORD[len(els)] += 1
    nt = [g for g in els if g != GID]
    if len(nt) == 1 and nt[0] == FOLD[f]:
        STFOLD += 1

gate(dict(STORD) == {2: 48} and NF * 2 == NA, "G4",
     "within the acting {0} every entry has a stabilizer of order exactly 2, census {1}, so {2} x 2 = {3}"
     .format(NA, dshow(STORD), NF, NF * 2))

D1 = [instance(f, MASK) for f in range(NF)]
NHELD = sorted(set(len(d["held"]) for d in D1))
NROW = sorted(set(d["nr"] for d in D1))
NWT = sorted(set(popc(v) for d in D1 for v in d["vecs"]))
KD1 = sorted(set(d["kdim"] for d in D1))

gate(STFOLD == NF and NF == 48 and FOLDOK and len(DIST) == 6 and NHELD == [14] and NROW == [40]
     and NWT == [12] and sorted(NORB) == [200] and KD1 == [8], "G5",
     "at {0} of {1} entries the unique nontrivial stabilizer element equals that entry's fold from the separate per-fiber search"
     .format(STFOLD, NF))
emit("G5 detail: that search holds each fiber setwise under exactly {0} of the {1} cell maps and returns {2} distinct folds, all involutions"
     .format(sorted(set(STCNT))[0], len(G384), len(DIST)))
emit("G5 detail: each entry carries {0} cuttings, {1} of them held by its fold, each a union of {2} of the {3} rows over {4} two-orbits"
     .format(36, NHELD[0], NWT[0], NROW[0], sorted(NORB)[0]))

# ================================================================ G6 fold transport

INV = {}
for g, em in ACT:
    for k in G384:
        if compose(g, k) == GID and compose(k, g) == GID:
            INV[g] = k
            break
TRT = 0
TRN = 0
for g, em in ACT:
    for f in range(NF):
        TRT += 1
        if FOLD[em[f]] == compose(compose(g, FOLD[f]), INV[g]):
            TRN += 1

gate(TRN == TRT and TRT == 4608 and len(INV) == NA, "G6",
     "fold transport holds at {0} of {1} pairs: the fold of the image entry is the conjugate of the fold by the acting map, over {2} x {3}"
     .format(TRN, TRT, NA, NF))
emit("G6 detail: each acting map's inverse is found by search over the {0} cell maps, never assumed".format(len(G384)))

# ================================================================ G7 the six folds are one class

CJ = set(compose(compose(g, DIST[0]), INV[g]) for g, em in ACT)
SERVE = sorted(Counter(FOLD).values())

gate(CJ == set(DIST) and len(CJ) == 6 and SERVE == [8] * 6 and 6 * 8 == NF, "G7",
     "the {0} distinct folds are one conjugacy class inside the acting {1}, and each serves {2} fibers: census {3}, {4} = {0} x {2}"
     .format(len(DIST), NA, SERVE[0], SERVE, NF))

# ================================================================ G9 the intrinsic classes on the first frame (computed before G8)

KEY1 = [tuple(sorted(v[2] for v in D1[f]["spl"].values())) for f in range(NF)]
PART = {}
for f in range(NF):
    PART.setdefault(KEY1[f], []).append(f)
ORD = sorted(PART)
CLS = [ORD.index(KEY1[f]) for f in range(NF)]
SIZES = [len(PART[k]) for k in ORD]
LETT = [sorted(set(tuple(sorted(E36[f])) for f in PART[k])) for k in ORD]
LCEN = [sorted(Counter(tuple(sorted(E36[f])) for f in PART[k]).values()) for k in ORD]
TABS = [sorted(set(D1[f]["tab"] for f in PART[k])) for k in ORD]
MUL25 = all(divmod(u, 25)[1] == 0 for k in ORD for u in k)
ANCT = [[((0, 100), (2, 50), (4, 100), (6, 100))],
        [((0, 100), (2, 100), (4, 100), (6, 100))],
        [((0, 100), (2, 175), (4, 100), (6, 100))]]
LANC = [(2, 12), (4, 14), (5, 13), (7, 11)]
HANC = [(2, 3), (4, 7), (10, 11), (12, 13)]

# ================================================================ G8 explicit transport across the classes, searched

SRC = [f for f in range(NF) if E36[f] == (2, 12)]
SRC = SRC[0] if len(SRC) == 1 else -1
HIT = [None, None, None]
for g, em in ACT:
    c = CLS[em[SRC]]
    if HIT[c] is None:
        HIT[c] = (g, em[SRC])
REP = []
for c in (1, 2):
    g, tf = HIT[c]
    pmp = piecemap(g, USED)
    d0 = D1[SRC]
    d1 = D1[tf]
    him = set(SIDX.get(frozenset(pmp[t] for t in SOLS[cc])) for cc in d0["held"])
    hok = him == set(d1["held"])
    p2d = dict((dvpieces(d1, dv), dv) for dv in d1["spl"])
    mt = []
    for dv in d0["spl"]:
        w = p2d.get(frozenset(pmp[t] for t in dvpieces(d0, dv)))
        if w is None:
            mt = None
            break
        mt.append((d0["brk"][dv], d1["brk"][w], d0["spl"][dv][2], d1["spl"][w][2]))
    cj1 = compose(compose(g, FOLD[SRC]), INV[g]) == FOLD[tf]
    cj2 = compose(compose(INV[g], FOLD[SRC]), g) == FOLD[tf]
    REP.append((g, tf, hok, sorted(mt) if mt is not None else None, cj1, cj2))

BR0 = sorted([(0, 0, 100, 100), (2, 2, 50, 100), (4, 4, 100, 100), (6, 6, 100, 100)])
BR2 = sorted([(0, 0, 100, 100), (2, 2, 50, 175), (4, 4, 100, 100), (6, 6, 100, 100)])
G8OK = (SRC >= 0 and CLS[SRC] == 0 and len(REP) == 2
        and all(r[2] and r[4] and r[5] for r in REP)
        and REP[0][3] == BR0 and REP[1][3] == BR2)

gate(G8OK, "G8",
     "searched transport out of the light entry with letter pair {0}: the first acting map reaching each of the other two classes carries"
     .format(tuple(sorted(E36[SRC]))))
for i in (0, 1):
    g, tf, hok, mt, cj1, cj2 = REP[i]
    emit("G8 detail: {0} takes the {1} held cuttings onto those of entry {2}, broken {3} union {4} -> {5}, broken {6} {7} -> {7}"
         .format(g, len(D1[SRC]["held"]), tuple(sorted(E36[tf])), mt[1][0], mt[1][2], mt[1][3],
                 tuple(x[0] for x in mt if x[0] != mt[1][0]), mt[0][2]))
emit("G8 detail: for both maps the conjugate of the source fold is the target fold, in either ordering of the acting map and its inverse")

# ================================================================ G9 headline

gate(SIZES == [8, 32, 8] and len(ORD) == 3 and set(LETT[0]) == set(LANC) and set(LETT[2]) == set(HANC)
     and LCEN[0] == [2] * 4 and LCEN[2] == [2] * 4 and TABS == ANCT and MUL25, "G9",
     "the {0} entries split by the sorted four-tuple of exchange union sizes into {1} light, {2} middle and {3} heavy"
     .format(NF, SIZES[0], SIZES[1], SIZES[2]))
emit("G9 detail: light letter pairs {0}; heavy letter pairs {1}, each on {2} entries"
     .format(LETT[0], LETT[2], 2))
emit("G9 detail: the broken {0}, {1} and {2} exchanges have union {3} at all {4} entries; the broken {5} exchange has union {6}, {3}, {7}"
     .format(0, 4, 6, 100, NF, 2, 50, 175))
emit("G9 detail: every union size is a multiple of {0}: {1} = {2} x {0}, {3} = {4} x {0}, {5} = {6} x {0}"
     .format(25, 50, 2, 100, 4, 175, 7))

# ================================================================ G10 the second generic frame

MASK2 = buildmask(OFFS2)
PC2 = [popc(m) for m in MASK2]
BADC = 0
for s in SOLS:
    m = 0
    tot = 0
    for t in s:
        m |= MASK2[t]
        tot += PC2[t]
    if m != UNIV or tot != NPTS:
        BADC += 1
D2 = [instance(f, MASK2) for f in range(NF)]
KD2 = sorted(set(d["kdim"] for d in D2))
NEX2 = sorted(set(len(d["spl"]) for d in D2))
SUPOK = sum(1 for f in range(NF) if sorted(D2[f]["spl"]) == sorted(D1[f]["spl"]))
HALFOK = sum(1 for f in range(NF)
             if all(set(D2[f]["spl"][dv][:2]) == set(D1[f]["spl"][dv][:2]) for dv in D1[f]["spl"]))
KEY2 = [tuple(sorted(v[2] for v in D2[f]["spl"].values())) for f in range(NF)]
TABOK = sum(1 for f in range(NF) if D2[f]["tab"] == D1[f]["tab"])
PART2 = {}
for f in range(NF):
    PART2.setdefault(KEY2[f], []).append(f)
SIZ2 = [len(PART2[k]) for k in sorted(PART2)]

gate(BADC == 0 and KD2 == [8] and NEX2 == [4] and SUPOK == NF and HALFOK == NF and KEY2 == KEY1
     and TABOK == NF and SIZ2 == SIZES and sorted(PART2) == ORD, "G10",
     "second generic frame, per-axis offsets {0} in place of {1}: {2} of the {3} cuttings fail to cover the {4} points once"
     .format(OFFS2, OFFS, BADC, NS, NPTS))
emit("G10 detail: at all {0} fibers the kernel dimension is {1} and there are exactly {2} equal-union exchanges, and the exchange supports"
     .format(NF, KD2[0], NEX2[0]))
emit("G10 detail: and their half-splits are identical to the first frame at {0} of {0} fibers; the class split is identical, {1} / {2} / {3}"
     .format(NF, SIZ2[0], SIZ2[1], SIZ2[2]))
emit("G10 detail: and the broken-count and union-size table matches the first frame at {0} of {0} fibers, class by class".format(NF))

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
