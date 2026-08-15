"""Physical cell cutting: the pinned pair, the whole symmetry fixing each exceptional cutting, and the weight-eight directions.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, and the sixteen-letter facet alphabet on the two slots of axis zero. Nothing outside that finite object enters any gate.

Earlier cycles linearized every wall fiber: rows are the two-orbits of the 400 kept pieces under that fiber's fold, the fold-held cuttings
are weight-twelve vectors on the rows that occur, the exact cover condition is an all-ones linear system whose solution set is one coset of
the kernel, and the 48 fiber systems are one instance carried in 48 labellings of the rows. The prior cycle isolated a dominant exchange
pairing twelve of the fourteen held cuttings and stranding two of them. This cycle reads the anatomy of those two: the full weight census of
the kernel, the light span of the weight-four and weight-six vectors, the profile of the nine weight-eight vectors, the complete block-level
self-equivalence search and its action on the stranded pair, the equivariant split of the dominant pairing, and the labelling-level classes
of the wall. Gates G1 to G10, one line each with a few detail lines, then the total line. Any failure exits nonzero.
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


def pshow(d):
    return "{" + ", ".join("({0},{1}): {2}".format(k[0], k[1], d[k]) for k in sorted(d)) + "}"


def cshow(k):
    return "{" + ", ".join("{0}: {1}".format(a, b) for a, b in k) + "}"


def popc(x):
    return bin(x).count("1")


def only(s):
    return sorted(s)[0] if len(s) == 1 else None


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


def image(v, pi):
    w = 0
    while v:
        low = v & (-v)
        w |= (1 << pi[low.bit_length() - 1])
        v ^= low
    return w


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

# ================================================================ the fold of every fiber

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


# ================================================================ the frozen anchors, measured independently of this run

KWC = {0: 1, 4: 4, 6: 1, 8: 9, 10: 5, 12: 13, 14: 16, 16: 17, 18: 30, 20: 31,
       22: 44, 24: 40, 26: 24, 28: 12, 30: 7, 32: 1, 34: 1}
OVA = {0: 5, 1: 1}
DWA = {6: 1, 8: 5}
W8A = {(0, 1): 3, (1, 0): 2, (2, 0): 2, (2, 1): 2}
DEG3 = {0: 1, 1: 4, 2: 9}
EUANC = {(50, 100, 100, 100): 8, (100, 100, 100, 100): 32, (100, 100, 100, 175): 8}
FDANC = {((0, 2), (1, 4), (2, 2)): 2, ((0, 4), (2, 4)): 1, ((1, 8),): 3}
LPA = [(2, 12), (4, 14), (5, 13), (7, 11)]
HPA = [(2, 3), (4, 7), (10, 11), (12, 13)]

# ================================================================ the per-fiber work, everything rebuilt at every fiber

INSOK = 0
SHAPES = set()
CVRT = 0
KWCENS = set()
OVCENS = set()
DWCENS = set()
SPANSZ = set()
LITOK = 0
W8CENS = set()
W8OK = 0
DEGCENS = set()
DEGX = set()
G6OK = 0
FIXCNT = set()
SYMOK = 0
FIXOK = 0
EQVOK = 0
EUSZ = Counter()
CLS = [None] * NF

for f in range(NF):
    fi = FIDX[FOLD[f]]
    mpk = MPKS[fi]
    oi = OIDX[fi]
    orbs = ORBS[fi]
    held = [c for c in FL[f] if frozenset(mpk[t] for t in SOLS[c]) == CSET[c]]
    raw = []
    u12 = 0
    for c in held:
        s = set(SOLS[c])
        rr = frozenset(oi[t] for t in s)
        if len(rr) == 12 and all(orbs[i][0] in s and orbs[i][1] in s for i in rr):
            u12 += 1
        raw.append(rr)
    nh = len(raw)
    rowg = sorted(set().union(*raw))
    nr = len(rowg)
    rpos = {r: i for i, r in enumerate(rowg)}
    vecs = [sum(1 << rpos[r] for r in rr) for rr in raw]
    sup = [MASK[orbs[rowg[i]][0]] | MASK[orbs[rowg[i]][1]] for i in range(nr)]
    pat = []
    for p in range(NPTS):
        q = 0
        for i in range(nr):
            if (sup[i] >> p) & 1:
                q |= (1 << i)
        pat.append(q)
    red, piv = rref(pat, nr)
    rk = len(red)
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
    kern = [0]
    for b in kb:
        kern = kern + [x ^ b for x in kern]
    kset = frozenset(kern)
    coset = [vecs[0] ^ x for x in kern]
    cset = frozenset(coset)
    heldset = frozenset(vecs)
    vidx = {vecs[i]: i for i in range(nh)}
    cvr = sum(1 for v in vecs if all(popc(q & v) == 1 for q in pat))
    CVRT += cvr
    evenk = all((popc(x) & 1) == 0 for x in kern)
    SHAPES.add((nh, u12, nr, rk, len(kb), len(kset), len(heldset)))
    if (nh == 14 and u12 == nh and nr == 40 and rk == 32 and len(kb) == 8 and len(kset) == 2 ** len(kb)
            and evenk and cvr == nh and len(heldset) == nh and set(popc(v) for v in vecs) == set([12])):
        INSOK += 1

    # ---- G3 the full weight census of the kernel
    kwc = Counter(popc(x) for x in kern)
    KWCENS.add(tuple(sorted(kwc.items())))

    # ---- G4 the light vectors and their span
    k4 = sorted(x for x in kern if popc(x) == 4)
    k6 = sorted(x for x in kern if popc(x) == 6)
    k8 = sorted(x for x in kern if popc(x) == 8)
    ovc = Counter()
    dwc = Counter()
    ovp = []
    for a, b in itertools.combinations(k4, 2):
        ovc[popc(a & b)] += 1
        dwc[popc(a ^ b)] += 1
        if a & b:
            ovp.append((a, b))
    span = set([0])
    for b in k4 + k6:
        span = span | set(x ^ b for x in span)
    spanset = frozenset(span)
    OVCENS.add(tuple(sorted(ovc.items())))
    DWCENS.add(tuple(sorted(dwc.items())))
    SPANSZ.add(len(spanset))
    if (len(k4) == 4 and len(k6) == 1 and len(k8) == 9 and len(ovp) == 1
            and popc(ovp[0][0] & ovp[0][1]) == 1 and (ovp[0][0] ^ ovp[0][1]) == k6[0]
            and len(spanset) == 16 and dict(ovc) == OVA and dict(dwc) == DWA):
        LITOK += 1

    # ---- the pairs of held cuttings, their differences and the minimal-exchange graph
    dmult = Counter()
    dpair = {}
    edges = []
    npr = 0
    for a, b in itertools.combinations(range(nh), 2):
        npr += 1
        it = popc(vecs[a] & vecs[b])
        dv = vecs[a] ^ vecs[b]
        dmult[dv] += 1
        dpair.setdefault(dv, []).append((a, b))
        if it == 10:
            edges.append((a, b))
    adj = [[] for _ in range(nh)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    deg = Counter(len(adj[i]) for i in range(nh))
    DEGCENS.add(tuple(sorted(deg.items())))

    # ---- G5 the profile of the weight-eight vectors
    prof = Counter()
    for x in k8:
        prof[(dmult.get(x, 0), 1 if x in spanset else 0)] += 1
    W8CENS.add(tuple(sorted(prof.items())))
    if len(k8) == 9 and npr == 91 and dict(prof) == W8A:
        W8OK += 1

    # ---- equal-union exchanges over the rows, point sets compared as point sets
    ug = {}
    for i, j in itertools.combinations(range(nr), 2):
        if sup[i] & sup[j]:
            continue
        ug.setdefault(sup[i] | sup[j], []).append((i, j))
    eu = []
    for u in ug:
        for pa, pb in itertools.combinations(ug[u], 2):
            if len(set(pa) | set(pb)) == 4:
                eu.append((pa, pb, popc(u)))
    spl = {}
    for pa, pb, usz in eu:
        ma = (1 << pa[0]) | (1 << pa[1])
        mb = (1 << pb[0]) | (1 << pb[1])
        spl[ma | mb] = (ma, mb, usz)
    brk = {}
    for dv in sorted(spl):
        ma, mb, usz = spl[dv]
        brk[dv] = sum(1 for w in vecs if (w & dv) not in (0, ma, mb))
    usz4 = tuple(sorted(v[2] for v in spl.values()))
    EUSZ[usz4] += 1
    CLS[f] = usz4

    # ---- G6 the dominant exchange, the exceptional pair, and the two multiplicity-one weight-eight vectors
    mx = max(dmult.values())
    dom = [x for x in dmult if dmult[x] == mx]
    exc = []
    dgs = ()
    if mx == 6 and len(dom) == 1 and dom[0] in spl:
        ma, mb, usz = spl[dom[0]]
        exc = sorted(i for i in range(nh) if (vecs[i] & dom[0]) not in (0, ma, mb))
        if len(exc) == 2:
            dgs = tuple(sorted(len(adj[i]) for i in exc))
    DEGX.add(dgs)
    de = 0
    if len(exc) == 2:
        de = vecs[exc[0]] ^ vecs[exc[1]]
    m1 = sorted(x for x in k8 if dmult.get(x, 0) == 1)
    if len(exc) == 2 and dgs == (0, 1) and len(m1) == 2 and de in m1:
        iso = exc[0] if len(adj[exc[0]]) == 0 else exc[1]
        oth = [x for x in m1 if x != de]
        op = dpair[oth[0]][0] if len(oth) == 1 and len(dpair[oth[0]]) == 1 else None
        if (popc(de) == 8 and dpair[de] == [tuple(exc)] and op is not None and iso in op
                and sorted(len(adj[i]) for i in op) == [0, 2]
                and de not in spanset and oth[0] not in spanset):
            G6OK += 1

    # ---- G7 the complete self-equivalence search and its action on the exceptional pair
    aut = eqsearch(tuple(vecs), tuple(vecs), nr, True)
    idt = tuple(range(nh))
    ntr = [s for s in aut if s != idt]
    pm = ntr[0] if (len(aut) == 2 and idt in aut and len(ntr) == 1) else None
    if pm is not None:
        fx = sum(1 for i in range(nh) if pm[i] == i)
        tc = sum(1 for i in range(nh) if pm[i] != i and pm[pm[i]] == i)
        FIXCNT.add((fx, tc // 2))
        if (fx == 10 and tc == 4 and all(pm[pm[i]] == i for i in range(nh))
                and len(exc) == 2 and pm[exc[0]] == exc[0] and pm[exc[1]] == exc[1]):
            SYMOK += 1

    # ---- G8 the coordinate-level action of that self-equivalence
    clean = [dv for dv in sorted(spl) if brk[dv] == 0]
    tgt = list(k4) + list(k6) + list(dom) + ([de] if len(exc) == 2 else [])
    npair = 0
    fixed = 0
    if len(clean) == 1 and pm is not None:
        ma, mb, usz = spl[clean[0]]
        aa = [i for i in range(nr) if (ma >> i) & 1]
        bl = [i for i in range(nr) if (mb >> i) & 1]
        for tw in (0, 1):
            pi = list(range(nr))
            pi[aa[0]] = bl[tw]
            pi[bl[tw]] = aa[0]
            pi[aa[1]] = bl[1 - tw]
            pi[bl[1 - tw]] = aa[1]
            imb = [image(v, pi) for v in vecs]
            if frozenset(imb) != heldset:
                continue
            if frozenset(image(x, pi) for x in kern) != kset:
                continue
            if frozenset(image(x, pi) for x in coset) != cset:
                continue
            if tuple(vidx[y] for y in imb) != pm:
                continue
            npair += 1
            if len(tgt) == 7 and all(image(x, pi) == x for x in tgt):
                fixed += 1
    if npair == 2 and fixed == 2:
        FIXOK += 1

    # ---- G9 the equivariant split of the dominant pairing
    if len(exc) == 2 and len(dom) == 1 and pm is not None:
        rest = [i for i in range(nh) if i not in exc]
        p6 = []
        seen6 = set()
        for i in rest:
            if i in seen6:
                continue
            j = vidx.get(vecs[i] ^ dom[0])
            if j is None or j in exc or j == i:
                p6 = []
                break
            seen6.add(i)
            seen6.add(j)
            p6.append(tuple(sorted((i, j))))
        if len(p6) == 6 and len(seen6) == 12:
            fixp = 0
            movp = []
            for pr in p6:
                im = tuple(sorted((pm[pr[0]], pm[pr[1]])))
                if im == pr:
                    fixp += 1
                else:
                    movp.append((pr, im))
            moved = sorted(i for i in range(nh) if pm[i] != i)
            un = sorted(set(x for pr, im in movp for x in pr))
            if (fixp == 4 and len(movp) == 2 and movp[0][1] == movp[1][0]
                    and movp[1][1] == movp[0][0] and moved == un and len(moved) == 4):
                EQVOK += 1

SH = only(SHAPES) or (0, 0, 0, 0, 0, 0, 0)
KW3 = dict(only(KWCENS)) if len(KWCENS) == 1 else {}
OVC = dict(only(OVCENS)) if len(OVCENS) == 1 else {}
DWC = dict(only(DWCENS)) if len(DWCENS) == 1 else {}
W8C = dict(only(W8CENS)) if len(W8CENS) == 1 else {}
DEGC = dict(only(DEGCENS)) if len(DEGCENS) == 1 else {}
DG = only(DEGX) or ()
FX = only(FIXCNT) or (0, 0)
SPZ = only(SPANSZ)
SPZ = SPZ if SPZ is not None else 0
IN8 = W8C.get((0, 1), 0) + W8C.get((2, 1), 0)
OU8 = W8C.get((1, 0), 0) + W8C.get((2, 0), 0)

# ================================================================ the labelling level of the wall

CLASSES = sorted(EUSZ)
CLSI = [CLASSES.index(CLS[f]) for f in range(NF)]
FCEN = Counter()
for gi in range(len(DIST)):
    FCEN[tuple(sorted(Counter(CLSI[f] for f in range(NF) if FIDX[FOLD[f]] == gi).items()))] += 1
ESET = set(E36)
SWOK = all((b, a) in ESET for a, b in E36)
DIAG = sum(1 for a, b in E36 if a == b)
LGT = set(E36[f] for f in range(NF) if CLSI[f] == 0)
HVY = set(E36[f] for f in range(NF) if CLSI[f] == len(CLASSES) - 1)
LSW = len(LGT) == 8 and all((b, a) in LGT for a, b in LGT)
HSW = len(HVY) == 8 and all((b, a) in HVY for a, b in HVY)
LUP = sorted(set(tuple(sorted(e)) for e in LGT))
HUP = sorted(set(tuple(sorted(e)) for e in HVY))
EUS = "; ".join(" ".join(str(x) for x in k) + " at " + str(EUSZ[k]) for k in sorted(EUSZ))
FCS = "; ".join(cshow(k) + " at " + str(FCEN[k]) for k in sorted(FCEN))
LUS = " ".join("({0},{1})".format(a, b) for a, b in LUP)
HUS = " ".join("({0},{1})".format(a, b) for a, b in HUP)

# ================================================================ G2 the linear instance, regated at every fiber

gate(NORB == set([200]) and SING == 0 and OVL == 0 and FOLDOK and INSOK == NF
     and SH == (14, 14, 40, 32, 8, 256, 14) and CVRT == NF * 14, "G2",
     "at all {0} fibers: {1} two-orbits, {2} held cuttings each a union of {3} of {4} rows, rank {5}, kernel dimension {6}"
     .format(NF, only(NORB), SH[0], 12, SH[2], SH[3], SH[4]))
emit("G2 detail: all {0} kernel vectors have even weight and each of the {1} held cuttings covers every one of the {2} points once"
     .format(SH[5], CVRT, NPTS))

# ================================================================ G3 the weight census of the kernel

gate(len(KWCENS) == 1 and KW3 == KWC and len(KW3) == 17 and sum(KW3.values()) == 256, "G3",
     "the kernel weight census takes {0} distinct value over the {1} fibers, with {2} weights totalling {3}"
     .format(len(KWCENS), NF, len(KW3), sum(KW3.values())))
emit("G3 detail: " + dshow(KW3))

# ================================================================ G4 the light vectors and their span

gate(LITOK == NF and len(OVCENS) == 1 and OVC == OVA and len(DWCENS) == 1 and DWC == DWA
     and len(SPANSZ) == 1 and SPZ == 16, "G4",
     "among the {0} pairs of the {1} weight {1} kernel vectors exactly {2} pair overlaps, in exactly {2} row, at all {3} fibers"
     .format(6, 4, 1, NF))
emit("G4 detail: overlap census {0} and pair difference weight census {1}, each {2} distinct value over the {3} fibers"
     .format(dshow(OVC), dshow(DWC), len(OVCENS), NF))
emit("G4 detail: the overlapping pair differs by the unique weight {0} kernel vector; the light span of those {1} vectors has {2} members"
     .format(6, 5, SPZ))

# ================================================================ G5 the profile of the weight-eight vectors

gate(W8OK == NF and len(W8CENS) == 1 and W8C == W8A, "G5",
     "each of the {0} weight {1} kernel vectors is classed by its multiplicity over the {2} held pairs and its light span membership"
     .format(9, 8, 91))
emit("G5 detail: the profile census by (multiplicity, membership) is {0}, with {1} meaning inside, at {2} of {2} fibers"
     .format(pshow(W8C), 1, NF))
emit("G5 detail: so {0} of the {1} lie inside the light span and {2} outside, and every multiplicity {3} weight {4} vector is inside"
     .format(IN8, 9, OU8, 0, 8))

# ================================================================ G6 the exceptional pair and the two light-outside directions

gate(G6OK == NF and len(DEGCENS) == 1 and DEGC == DEG3 and len(DEGX) == 1 and DG == (0, 1), "G6",
     "the minimal exchange graph, the pairs sharing {0} of their {1} rows, has degree census {2} at all {3} fibers"
     .format(10, 12, dshow(DEGC), NF))
emit("G6 detail: the dominant difference, of multiplicity {0}, breaks exactly {1} held cuttings, of graph degrees {2} and {3}"
     .format(6, 2, DG[0], DG[1]))
emit("G6 detail: their difference has weight {0} and multiplicity {1}, realized by that pair alone; the other multiplicity {1} weight {0}"
     .format(8, 1))
emit("G6 detail: vector is realized by exactly {0} pair, joining the degree {1} cutting to a degree {2} one; both lie outside the light span"
     .format(1, 0, 2))

# ================================================================ G7 the complete symmetry pins each exceptional cutting

gate(SYMOK == NF and len(FIXCNT) == 1 and FX == (10, 2), "G7",
     "the complete block-level self-equivalence search returns exactly {0} elements at {1} of {1} fibers"
     .format(2, NF))
emit("G7 detail: the nontrivial one fixes each of the {0} exceptional cuttings, and its cycle structure on the {1} held cuttings is"
     .format(2, 14))
emit("G7 detail: {0} fixed points and {1} two-cycles, {2} distinct value over the {3} fibers"
     .format(FX[0], FX[1], len(FIXCNT), NF))

# ================================================================ G8 the same symmetry at the level of the rows

gate(FIXOK == NF, "G8",
     "on the {0} row coordinates the nontrivial self-equivalence fixes as vectors all {1} anchored kernel directions, at {2} of {2} fibers"
     .format(40, 7, NF))
emit("G8 detail: the {0} weight {0} vectors, the weight {1} vector, the dominant difference, and the exceptional pair difference of weight {2}"
     .format(4, 6, 8))

# ================================================================ G9 the equivariant split of the dominant pairing

gate(EQVOK == NF, "G9",
     "the dominant difference pairs the {0} non-exceptional held cuttings into {1} pairs at all {2} fibers"
     .format(12, 6, NF))
emit("G9 detail: the nontrivial self-equivalence fixes {0} of those pairs as sets and exchanges the other {1} with each other, and its {2}"
     .format(4, 2, 4))
emit("G9 detail: moved cuttings are exactly the union of the {0} exchanged pairs".format(2))

# ================================================================ G10 the labelling level of the wall

gate(dict(EUSZ) == EUANC and dict(FCEN) == FDANC and SWOK and DIAG == 0 and LSW and HSW
     and LUP == LPA and HUP == HPA, "G10",
     "the union size class of a fiber takes {0} values over the {1} fibers, and the per fold class census multiset is anchored"
     .format(len(EUSZ), NF))
emit("G10 detail: the four union sizes read {0}".format(EUS))
emit("G10 detail: classes are numbered {0} light, {1} middle, {2} heavy by union size; the per fold census multiset reads"
     .format(0, 1, 2))
emit("G10 detail: " + FCS)
emit("G10 detail: the {0} wall entries are closed under the letter swap, with {1} diagonal entries, and so is each extreme class"
     .format(NF, DIAG))
emit("G10 detail: light letter pairs {0}; heavy letter pairs {1}".format(LUS, HUS))

# ================================================================ totals

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
