"""Physical cell cutting: the wall fiber systems are one instance, each fiber carrying it in its own labelling of the rows.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, and the sixteen-letter facet alphabet on the two slots of axis zero. Nothing outside that finite object enters any gate.

The previous cycle linearized every fiber: rows are the two-orbits of the 400 kept pieces under that fiber's fold, the fold-held cuttings
are weight-twelve vectors on the rows that occur, and the exact cover condition is an all-ones linear system whose solution set is one coset
of the kernel. This cycle asks whether the 48 systems are one object. It regates that linear form, gates the further invariants that are
single-valued over the fibers, runs a complete backtracking search for a relabelling of the rows carrying the sample fiber's instance onto
each of the others, counts every such relabelling, and checks that a one-block perturbation is honestly rejected. The search is complete at
the block level because the span of the differences is the kernel as a set, so a bijection of the blocks fixes the images of kernel and
coset. Gates G1 to G10, one line each with a few detail lines, then the total line. Any failure exits nonzero.
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

# ================================================================ the two-orbit table of each fold

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

# ================================================================ the per-fiber systems, rebuilt at every fiber

GFIBS = [f for f in range(NF) if FOLD[f] == GREP]
REPF = GFIBS[0]
RPAIR = E36[REPF]
KCEN8 = {0: 1, 4: 4, 6: 1, 8: 9, 10: 5, 12: 13, 14: 16, 16: 17, 18: 30, 20: 31,
         22: 44, 24: 40, 26: 24, 28: 12, 30: 7, 32: 1, 34: 1}
COVP8 = {1: 6, 2: 10, 3: 2, 4: 7, 6: 9, 8: 3, 10: 3}
PAIR8 = {0: 12, 1: 6, 2: 10, 3: 14, 4: 4, 5: 14, 6: 4, 7: 5, 8: 10, 9: 1, 10: 11}

HELD = []
ROWN = set()
UNI12 = 0
CVR = 0
BARE = 0
RKS = set()
KOK = 0
KEVEN = 0
SPAN = 0
COSET1 = 0
KCENS = set()
KCOLS = set()
CCOLS = set()
COVPS = set()
PAIRS = set()
SETK = 0
SETC = 0
INST = []
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
            CVR += 1
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
    if all(all((popc(q & x) & 1) == 1 for q in pat) for x in coset):
        COSET1 += 1
    spanset = set([0])
    for d in dred:
        spanset |= set(x ^ d for x in spanset)
    if spanset == set(kern):
        SETK += 1
    if set(x1 ^ s for s in spanset) == set(coset):
        SETC += 1
    KCENS.add(tuple(sorted(Counter(popc(x) for x in kern).items())))
    kc = Counter()
    cc = Counter()
    cov = Counter()
    for i in range(nr):
        kc[sum(1 for x in kern if (x >> i) & 1)] += 1
        cc[sum(1 for x in coset if (x >> i) & 1)] += 1
        cov[sum(1 for v in vecs if (v >> i) & 1)] += 1
    KCOLS.add(tuple(sorted(kc.items())))
    CCOLS.add(tuple(sorted(cc.items())))
    COVPS.add(tuple(sorted(cov.items())))
    pc = Counter(popc(vecs[a] & vecs[b]) for a, b in itertools.combinations(range(len(vecs)), 2))
    PAIRS.add(tuple(sorted(pc.items())))
    INST.append((tuple(vecs), tuple(kern), tuple(coset)))

NH = sorted(set(len(h) for h in HELD))
NR = sorted(ROWN)[0]
RKT = sorted(RKS)[0]
NKV = 2 ** RKT[2]

# ================================================================ G3 the linear form of every fiber, regated here

gate(len(MPKS) == 6 and NORB == set([200]) and SING == 0 and OVL == 0 and NH == [14] and UNI12 == 48 * 14
     and ROWN == set([40]) and CVR == 48 * 14 and BARE == 0 and len(RKS) == 1 and RKT == (40, 32, 8)
     and KOK == 48 and KEVEN == 48 and SPAN == 48 and COSET1 == 48, "G3",
     "at all {0} fibers: {1} two-orbits, {2} held cuttings each a union of {3}, {4} rows occur, rank {5}, kernel dimension {6}"
     .format(NF, sorted(NORB)[0], NH[0], 12, NR, RKT[1], RKT[2]))
emit("G3 detail: all {0} kernel vectors have even weight, the {1} differences span dimension {2}, and all {0} coset members solve all ones"
     .format(NKV, NH[0] - 1, RKT[2]))
emit("G3 detail: each of the {0} held cuttings covers every one of the {1} sample points exactly once, and {2} points lie in no row"
     .format(CVR, NPTS, BARE))
emit("G3 detail: the sample fiber at letter pair ({0},{1}) has rows-per-point census {2}"
     .format(RPAIR[0], RPAIR[1], dshow(REPCEN)))

# ================================================================ G4 the weight census of the kernel itself

KC1 = dict(sorted(KCENS)[0]) if len(KCENS) == 1 else {}
KK = sorted(KC1)

gate(len(KCENS) == 1 and KC1 == KCEN8 and sum(KC1.values()) == NKV and min(KC1) == 0 and max(KC1) == 34, "G4",
     "the kernel's own weight census takes {0} distinct value over the {1} fibers, of total {2} on {3} coordinates"
     .format(len(KCENS), NF, sum(KC1.values()), NR))
emit("G4 detail: that census begins " + "{" + ", ".join("{0}: {1}".format(k, KC1[k]) for k in KK[:9]) + ",")
emit("G4 detail: and continues " + ", ".join("{0}: {1}".format(k, KC1[k]) for k in KK[9:]) + "}")

# ================================================================ G5 the column profiles of kernel and coset

KP1 = dict(sorted(KCOLS)[0]) if len(KCOLS) == 1 else {}
CP1 = dict(sorted(CCOLS)[0]) if len(CCOLS) == 1 else {}

gate(len(KCOLS) == 1 and len(CCOLS) == 1 and KP1 == {128: 40} and CP1 == {128: 40}, "G5",
     "at every one of the {0} fibers each of the {1} coordinates is one on exactly {2} of the {3} kernel vectors and on {2} coset members"
     .format(NF, NR, 128, NKV))
emit("G5 detail: the kernel column profile is {0} and the coset column profile is {1}, {2} distinct value each"
     .format(dshow(KP1), dshow(CP1), len(KCOLS)))

# ================================================================ G6 the block invariants of the held cuttings

CV1 = dict(sorted(COVPS)[0]) if len(COVPS) == 1 else {}
PR1 = dict(sorted(PAIRS)[0]) if len(PAIRS) == 1 else {}
TOTI = sum(k * CV1[k] for k in CV1)
NPAIR = sum(PR1.values())

gate(len(COVPS) == 1 and len(PAIRS) == 1 and CV1 == COVP8 and PR1 == PAIR8 and sum(CV1.values()) == NR
     and TOTI == 168 and TOTI == 14 * 12 and NPAIR == 91, "G6",
     "the block invariants of the {0} held cuttings take {1} distinct value over the {2} fibers: total incidence {3} on {4} coordinates"
     .format(NH[0], len(COVPS), NF, TOTI, sum(CV1.values())))
emit("G6 detail: the per-coordinate cover profile is {0}, and {1} is {2} times {3}".format(dshow(CV1), TOTI, NH[0], 12))
emit("G6 detail: the pairwise support-intersection census over the {0} pairs is {1}".format(NPAIR, dshow(PR1)))

# ================================================================ G7 the set-level licence for a block-level search

gate(SETK == NF and SETC == NF, "G7",
     "at {0} of {1} fibers the span of the {2} differences equals the kernel as a set of {3}, and the affine hull of the {4} is the coset"
     .format(SETK, NF, NH[0] - 1, NKV, NH[0]))

# ================================================================ the complete search over block bijections


def patterns(blocks, nc):
    out = []
    for c in range(nc):
        p = 0
        for i in range(len(blocks)):
            if (blocks[i] >> c) & 1:
                p |= (1 << i)
        out.append(p)
    return out


def shape(blocks, nc):
    ct = Counter(patterns(blocks, nc))
    return sorted((popc(p), ct[p]) for p in ct)


def eqsearch(ba, bb, nc, findall):
    """Complete backtracking search for bijections of blocks carrying one instance onto another; empty list means NOT FOUND."""
    if len(ba) != len(bb) or sorted(popc(x) for x in ba) != sorted(popc(x) for x in bb):
        return []
    if shape(ba, nc) != shape(bb, nc):
        return []
    m = len(ba)
    ia = [[popc(ba[i] & ba[j]) for j in range(m)] for i in range(m)]
    ib = [[popc(bb[i] & bb[j]) for j in range(m)] for i in range(m)]
    if sorted(sorted(r) for r in ia) != sorted(sorted(r) for r in ib):
        return []
    capat = []
    cur = [0] * nc
    capat.append(Counter(cur))
    for k in range(m):
        for c in range(nc):
            if (ba[k] >> c) & 1:
                cur[c] |= (1 << k)
        capat.append(Counter(cur))
    asg = [-1] * m
    used = [False] * m
    res = []

    def bpat(k):
        ct = Counter()
        for c in range(nc):
            p = 0
            for i in range(k):
                if (bb[asg[i]] >> c) & 1:
                    p |= (1 << i)
            ct[p] += 1
        return ct

    def rec(k):
        if k == m:
            res.append(tuple(asg))
            return not findall
        for j in range(m):
            if used[j] or popc(ba[k]) != popc(bb[j]):
                continue
            good = True
            for i in range(k):
                if ia[k][i] != ib[j][asg[i]]:
                    good = False
                    break
            if not good:
                continue
            asg[k] = j
            used[j] = True
            if bpat(k + 1) == capat[k + 1] and rec(k + 1):
                used[j] = False
                asg[k] = -1
                return True
            used[j] = False
            asg[k] = -1
        return False

    rec(0)
    return sorted(res)


def witness(ba, bb, nc, sig):
    pa = patterns(ba, nc)
    pb = patterns(bb, nc)
    ga = {}
    gb = {}
    for c in range(nc):
        ga.setdefault(pa[c], []).append(c)
        gb.setdefault(pb[c], []).append(c)
    pi = [-1] * nc
    for p in sorted(ga):
        q = 0
        for i in range(len(sig)):
            if (p >> i) & 1:
                q |= (1 << sig[i])
        tg = gb.get(q, [])
        if len(tg) != len(ga[p]):
            return None
        for a, b in zip(sorted(ga[p]), sorted(tg)):
            pi[a] = b
    return pi if all(x >= 0 for x in pi) else None


def image(v, pi):
    w = 0
    while v:
        low = v & (-v)
        w |= (1 << pi[low.bit_length() - 1])
        v ^= low
    return w


# ================================================================ G8 the sample instance carries onto every other fiber

SAMP = INST[REPF]
OTHERS = [f for f in range(NF) if f != REPF]
FOUND = 0
VK = 0
VB = 0
VC = 0
for f in OTHERS:
    tgt = INST[f]
    sg = eqsearch(SAMP[0], tgt[0], NR, False)
    if not sg:
        continue
    FOUND += 1
    pi = witness(SAMP[0], tgt[0], NR, sg[0])
    if pi is None or sorted(pi) != list(range(NR)):
        continue
    if set(image(x, pi) for x in SAMP[1]) == set(tgt[1]):
        VK += 1
    if set(image(x, pi) for x in SAMP[0]) == set(tgt[0]):
        VB += 1
    if set(image(x, pi) for x in SAMP[2]) == set(tgt[2]):
        VC += 1

gate(FOUND == 47 and VK == 47 and VB == 47 and VC == 47, "G8",
     "a relabelling of the {0} coordinates is found at {1} of the {2} other fibers, each verified on kernel, blocks and coset"
     .format(NR, FOUND, len(OTHERS)))
emit("G8 detail: explicit images verify {0} kernel sets of {1}, {2} block sets of {3}, and {4} coset sets of {1}"
     .format(VK, NKV, VB, NH[0], VC))

# ================================================================ G9 the count of relabellings and the free action

AUT = eqsearch(SAMP[0], SAMP[0], NR, True)
IDT = tuple(range(NH[0]))
NTRIV = [s for s in AUT if s != IDT]
ALPHA = NTRIV[0] if len(NTRIV) == 1 else IDT
AUTOK = len(AUT) == 2 and IDT in AUT and len(NTRIV) == 1 and all(ALPHA[ALPHA[i]] == i for i in range(NH[0]))
CNT2 = 0
COMPOK = 0
for f in OTHERS:
    ss = eqsearch(SAMP[0], INST[f][0], NR, True)
    if len(ss) != 2:
        continue
    CNT2 += 1
    c0 = tuple(ss[0][ALPHA[i]] for i in range(NH[0]))
    c1 = tuple(ss[1][ALPHA[i]] for i in range(NH[0]))
    if c0 == ss[1] and c1 == ss[0]:
        COMPOK += 1

gate(AUTOK and CNT2 == 47 and COMPOK == 47, "G9",
     "exactly {0} relabellings at each of the {1} targets, matching the {0} symmetries of the sample instance, the identity and one involution"
     .format(len(AUT), CNT2))
emit("G9 detail: composing the nontrivial symmetry with either relabelling gives the other at {0} of {1} targets, freely and transitively"
     .format(COMPOK, len(OTHERS)))

# ================================================================ G10 the control target, honestly rejected

PATS = patterns(SAMP[0], NR)
B0 = SAMP[0][0]
UU = (B0 & (-B0)).bit_length() - 1
VV = -1
for c in range(NR):
    if not ((B0 >> c) & 1) and PATS[c] != PATS[UU]:
        VV = c
        break
FAKE = list(SAMP[0])
FAKE[0] = (B0 ^ (1 << UU)) | (1 << VV)
CTRL = eqsearch(SAMP[0], tuple(FAKE), NR, False)

gate(VV >= 0 and PATS[UU] != PATS[VV] and popc(FAKE[0]) == 12 and len(FAKE) == NH[0] and len(CTRL) == 0, "G10",
     "the control target moves one coordinate out of one block and another in; the same search entry point returns NOT FOUND, {0} found"
     .format(len(CTRL)))
emit("G10 detail: coordinate {0} leaves the first block and coordinate {1} enters it, the block staying at weight {2}"
     .format(UU, VV, popc(FAKE[0])))

# ================================================================ totals

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
