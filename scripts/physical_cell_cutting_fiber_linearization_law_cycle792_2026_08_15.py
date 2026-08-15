"""Physical cell cutting: every wall fiber cover problem is one coset minimum-weight problem over the field with two elements.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, and the sixteen-letter facet alphabet on the two slots of axis zero. Nothing outside that finite object enters any gate.

The previous cycle settled the group side on a single fiber. This cycle takes the linear side on all 48 of them. For each fiber the fold is
its unique nontrivial setwise holder, the rows are the two-orbits of the 400 kept pieces under that fold, the fold-held cuttings become
vectors over the field with two elements, and the exact cover condition becomes an all-ones linear system whose solution set is one coset of
the kernel. Gates G1 to G12, one line each with a few detail lines, then the total line. Any failure exits nonzero.
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

ALLK = sorted({d[k] for d in KEYF for k in d}, key=lambda f: sorted(sorted(t) for t in f))
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

# ================================================================ G2 the fold of every fiber

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
SERVE = dict(sorted(Counter(Counter(FOLD).values()).items()))
INVOL = sum(1 for g in DIST if compose(g, g) == GID and g != GID)
GREP = ((0, 3, 2, 1), 15)

gate(DEFECT == 0 and set(STCNT) == set([2]) and len(WALL) == 1728 and len(DIST) == 6 and SERVE == {8: 6}
     and INVOL == 6 and GREP in DIST, "G2",
     "each of the {0} fibers is held setwise by exactly {1} of the {2} cell maps; the {0} folds are {3} distinct involutions, census {4}"
     .format(NF, sorted(set(STCNT))[0], len(G384), len(DIST), dshow(SERVE)))

# ================================================================ G3 the two-orbit table of each fold

MPKS = []
ORBS = []
OIDX = []
SING = 0
OVL = 0
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
        if u == t:
            SING += 1
        if MASK[t] & MASK[u]:
            OVL += 1
        orbs.append((t, u))
    oi = {}
    for i in range(len(orbs)):
        oi[orbs[i][0]] = i
        oi[orbs[i][1]] = i
    MPKS.append(mpk)
    ORBS.append(orbs)
    OIDX.append(oi)
    NORB.add(len(orbs))

gate(len(MPKS) == 6 and NORB == set([200]) and SING == 0 and OVL == 0, "G3",
     "each of the {0} folds cuts the {1} kept pieces into {2} two-orbits, with {3} singletons and {4} interior overlaps inside an orbit"
     .format(len(DIST), NK, sorted(NORB)[0], SING, OVL))

# ================================================================ the per-fiber linear systems

GFIBS = [f for f in range(NF) if FOLD[f] == GREP]
REPF = GFIBS[0]
RPAIR = E36[REPF]
CEN8 = {12: 14, 14: 11, 16: 37, 18: 29, 20: 55, 22: 45, 24: 51, 26: 11, 28: 3}

HELD = []
ROWN = set()
UNI12 = 0
G4PT = 0
BARE = 0
RKS = set()
KOK = 0
KEVEN = 0
SPAN = 0
COSET1 = 0
CENS = set()
MINOK = 0
COVOK = 0
NCOV = set()
TCAND = 0
TPASS = 0
ROWKEY = []
REPCEN = {}

for f in range(NF):
    fi = FIDX[FOLD[f]]
    mpk = MPKS[fi]
    oi = OIDX[fi]
    orbs = ORBS[fi]
    held = [c for c in FL[f] if frozenset(mpk[t] for t in SOLS[c]) == CSET[c]]
    HELD.append(frozenset(held))
    raw = []
    for c in held:
        s = set(SOLS[c])
        rr = frozenset(oi[t] for t in s)
        if len(rr) == 12 and all(orbs[i][0] in s and orbs[i][1] in s for i in rr):
            UNI12 += 1
        raw.append(rr)
    rowg = sorted(set().union(*raw))
    nr = len(rowg)
    ROWN.add(nr)
    ROWKEY.append((fi, frozenset(rowg)))
    rpos = {r: i for i, r in enumerate(rowg)}
    vecs = []
    for rr in raw:
        v = 0
        for r in rr:
            v |= (1 << rpos[r])
        vecs.append(v)
    sup = [MASK[orbs[rowg[i]][0]] | MASK[orbs[rowg[i]][1]] for i in range(nr)]
    pat = []
    for p in range(NPTS):
        q = 0
        for i in range(nr):
            if (sup[i] >> p) & 1:
                q |= (1 << i)
        pat.append(q)
    BARE += sum(1 for q in pat if q == 0)
    for v in vecs:
        if all(popc(q & v) == 1 for q in pat):
            G4PT += 1
    if f == REPF:
        REPCEN = dict(sorted(Counter(popc(q) for q in pat).items()))
    red, piv = rref(pat, nr)
    rk = len(red)
    RKS.add((nr, rk, nr - rk))
    pset = set(piv)
    kb = []
    for fc in range(nr):
        if fc in pset:
            continue
        v = (1 << fc)
        for i in range(rk):
            if (red[i] >> fc) & 1:
                v |= (1 << piv[i])
        kb.append(v)
    if len(kb) == nr - rk and all(all((popc(q & v) & 1) == 0 for q in pat) for v in kb):
        KOK += 1
    kern = [0]
    for b in kb:
        kern = kern + [x ^ b for x in kern]
    if len(set(kern)) == 2 ** len(kb) and all((popc(x) & 1) == 0 for x in kern):
        KEVEN += 1
    x1 = vecs[0]
    diffs = [x1 ^ vecs[k] for k in range(1, len(vecs))]
    dred, dpiv = rref(diffs, nr)
    if all(all((popc(q & d) & 1) == 0 for q in pat) for d in diffs) and len(dred) == nr - rk:
        SPAN += 1
    coset = [x1 ^ x for x in kern]
    odd = 0
    cov = set()
    for x in coset:
        cnt = [popc(q & x) for q in pat]
        if all((c & 1) == 1 for c in cnt):
            odd += 1
        if all(c == 1 for c in cnt):
            cov.add(x)
    if odd == len(coset):
        COSET1 += 1
    cen = dict(sorted(Counter(popc(x) for x in coset).items()))
    CENS.add(tuple(sorted(cen.items())))
    if min(cen) == 12 and set(x for x in coset if popc(x) == 12) == set(vecs):
        MINOK += 1
    if cov == set(vecs):
        COVOK += 1
    NCOV.add(len(cov))
    sv = set(vecs)
    for d in diffs:
        TCAND += 1
        if set(x ^ d for x in sv) == sv:
            TPASS += 1

NH = sorted(set(len(h) for h in HELD))
NR = sorted(ROWN)[0]
RKT = sorted(RKS)[0]
CEN1 = dict(sorted(CENS)[0]) if len(CENS) == 1 else {}

gate(NH == [14] and UNI12 == 48 * 14 and ROWN == set([40]) and G4PT == 48 * 14 and BARE == 0
     and REPCEN == {2: 235, 3: 108, 4: 186, 5: 64, 6: 32}, "G4",
     "at all {0} fibers the fold holds {1} cuttings, each an exact union of {2} two-orbits, and {3} rows occur"
     .format(NF, NH[0], 12, NR))
emit("G4 detail: all {0} held cuttings cover each of the {1} sample points exactly once, and {2} points are left uncovered"
     .format(G4PT, NPTS, BARE))
emit("G4 detail: the sample fiber at letter pair ({0},{1}) has rows-per-point census {2}"
     .format(RPAIR[0], RPAIR[1], dshow(REPCEN)))

gate(len(RKS) == 1 and RKT == (40, 32, 8), "G5",
     "the {0} by {1} incidence over the field with two elements has rank {2} and kernel dimension {3} at every fiber, {4} distinct tuple"
     .format(NPTS, RKT[0], RKT[1], RKT[2], len(RKS)))

gate(KOK == 48 and KEVEN == 48, "G6",
     "the kernel basis of {0} vectors annihilates the incidence at {1} of {2} fibers; all {3} kernel vectors have even weight at {4} of {2}"
     .format(RKT[2], KOK, NF, 2 ** RKT[2], KEVEN))

gate(SPAN == 48 and COSET1 == 48, "G7",
     "the {0} differences lie in the kernel and span dimension {1} at {2} of {3} fibers; all {4} coset members solve the all-ones system"
     .format(14 - 1, RKT[2], SPAN, NF, 2 ** RKT[2]))

gate(len(CENS) == 1 and CEN1 == CEN8 and sum(CEN1.values()) == 256 and min(CEN1) == 12, "G8",
     "the {0} fibers carry {1} distinct coset weight census, of total {2} and minimum weight {3}"
     .format(NF, len(CENS), sum(CEN1.values()), min(CEN1)))
emit("G8 detail: that one census is {0}".format(dshow(CEN1)))

gate(MINOK == 48 and COVOK == 48 and NCOV == set([14]), "G9",
     "the minimum-weight members and the exact covers of the coset are both exactly the {0} held cuttings at {1} of {2} fibers"
     .format(NH[0], COVOK, NF))
emit("G9 detail: every exact cover of a {0}-row instance solves the all-ones system, so each instance has exactly {1} exact covers"
     .format(NR, sorted(NCOV)[0]))

gate(TCAND == 48 * 13 and TPASS == 0, "G10",
     "the complete candidate list of {0} nonzero translations per fiber, {1} tests over the {2} fibers, gives {3} preserved systems"
     .format(13, TCAND, NF, TPASS))

# ================================================================ G11 the same refutation at the native level

fi = FIDX[GREP]
mpk = MPKS[fi]
orbs = ORBS[fi]
oi = OIDX[fi]
NAT = [c for c in range(NS) if frozenset(mpk[t] for t in SOLS[c]) == CSET[c]]
NVEC = []
NUOK = 0
for c in NAT:
    s = set(SOLS[c])
    rr = frozenset(oi[t] for t in s)
    if len(rr) == 12 and all(orbs[i][0] in s and orbs[i][1] in s for i in rr):
        NUOK += 1
    v = 0
    for r in rr:
        v |= (1 << r)
    NVEC.append(v)
NSV = set(NVEC)
NDIFF = [NVEC[0] ^ NVEC[k] for k in range(1, len(NVEC))]
NPASS = sum(1 for d in NDIFF if set(x ^ d for x in NSV) == NSV)

gate(len(NAT) == 336 and NUOK == 336 and len(NSV) == 336 and len(NDIFF) == 335 and NPASS == 0, "G11",
     "the sample fold holds {0} of the {1} cuttings, each a union of {2} of its {3} two-orbits; {4} candidates give {5} preserved systems"
     .format(len(NAT), NS, 12, len(orbs), len(NDIFF), NPASS))

# ================================================================ G12 the forty-eight instances are distinct objects

UNIH = set()
for h in HELD:
    UNIH |= set(h)
INTC = Counter()
WPAIR = 0
for g in DIST:
    fs = [f for f in range(NF) if FOLD[f] == g]
    for a, b in itertools.combinations(fs, 2):
        INTC[len(ROWKEY[a][1] & ROWKEY[b][1])] += 1
        WPAIR += 1
ICEN = dict(sorted(INTC.items()))

gate(len(set(ROWKEY)) == 48 and len(set(HELD)) == 48 and len(UNIH) == 672 and WPAIR == 168
     and ICEN == {12: 24, 14: 24, 18: 48, 20: 24, 22: 48}, "G12",
     "{0} distinct fold and row-set pairs, {1} distinct solution systems, {2} cuttings in the union, {3} within-fold fiber pairs"
     .format(len(set(ROWKEY)), len(set(HELD)), len(UNIH), WPAIR))
emit("G12 detail: the within-fold row-set intersection census is {0}, never {1} at any pair".format(dshow(ICEN), NR))

# ================================================================ totals

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
