"""Physical cell cutting: four minimal exchanges at every wall fiber, exactly one of them clean,
and the parity of fourteen carried down to two exceptional cuttings.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, and the sixteen-letter facet alphabet on the two slots of axis zero. Nothing outside that finite object enters any gate.

Earlier cycles linearized every wall fiber: rows are the two-orbits of the 400 kept pieces under that fiber's fold, the fold-held cuttings
are weight-twelve vectors on the rows that occur, the exact cover condition is an all-ones linear system whose solution set is one coset of
the kernel, and the 48 fiber systems are one instance carried in 48 labellings of the rows. This cycle reads the exchange structure of that
instance and regates the linear form it stands on. It builds the graph of held pairs sharing ten of their twelve rows, identifies the edge
differences with the weight-four kernel vectors, enumerates the equal-union splittings of the rows that realize them, checks that the held
set is closed under all four toggles, isolates the single clean exchange whose toggle is the whole nontrivial symmetry of the instance by a
complete block-level search, and runs the parity descent over all nonzero kernel vectors. Gates G1 to G10, one line each with a few detail
lines, then the total line. Any failure exits nonzero.
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


# ================================================================ the per-fiber work, everything rebuilt at every fiber

PAIR8 = {0: 12, 1: 6, 2: 10, 3: 14, 4: 4, 5: 14, 6: 4, 7: 5, 8: 10, 9: 1, 10: 11}
DEG3 = {0: 1, 1: 4, 2: 9}
SIZ3 = [1, 2, 3, 4, 4]
EDC4 = {1: 1, 2: 2, 6: 1}
MOV6 = {2: 1, 4: 2, 12: 1}
BRK6 = {0: 1, 2: 1, 4: 1, 6: 1}

INSOK = 0
SHAPES = set()
CVRT = 0
PAIRSET = set()
GRAPHS = set()
CYCOK = 0
DIFOK = 0
EDCENS = set()
ALLCENS = set()
EUOK = 0
EUSZ = Counter()
EUANC = {(50, 100, 100, 100): 8, (100, 100, 100, 100): 32, (100, 100, 100, 175): 8}
REMEQ = 0
REMSZ = Counter()
RMANC = {120: 8, 150: 32, 205: 8}
TOGOK = 0
MOVCENS = set()
BRKCENS = set()
CLNOK = 0
LEMOK = 0
FIXCNT = set()
SYMOK = 0
PAROK = 0
RSHARE = set()
DEGX = set()
MAXM = set()

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
    onec = all(all((popc(q & x) & 1) == 1 for q in pat) for x in coset)
    SHAPES.add((nh, u12, nr, rk, len(kb), len(kset), len(cset), len(heldset)))
    if (nh == 14 and u12 == nh and nr == 40 and rk == 32 and len(kb) == 8 and len(kset) == 2 ** len(kb)
            and len(cset) == len(kset) and evenk and onec and cvr == nh and len(heldset) == nh
            and set(popc(v) for v in vecs) == set([12])):
        INSOK += 1

    # ---- pairs, the minimal-exchange graph, and the differences
    pcen = Counter()
    dmult = Counter()
    edges = []
    nine = None
    inker = 0
    for a, b in itertools.combinations(range(nh), 2):
        it = popc(vecs[a] & vecs[b])
        pcen[it] += 1
        dv = vecs[a] ^ vecs[b]
        dmult[dv] += 1
        if dv in kset:
            inker += 1
        if it == 10:
            edges.append((a, b))
        if it == 9:
            nine = (a, b)
    PAIRSET.add(tuple(sorted(pcen.items())))
    adj = [[] for _ in range(nh)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    deg = Counter(len(adj[i]) for i in range(nh))
    seenv = set()
    comps = []
    for i in range(nh):
        if i in seenv:
            continue
        stack = [i]
        seenv.add(i)
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if v not in seenv:
                    seenv.add(v)
                    stack.append(v)
        comps.append(set(comp))
    sizes = sorted(len(c) for c in comps)
    GRAPHS.add((len(edges), tuple(sorted(deg.items())), tuple(sizes)))
    big = [c for c in comps if len(c) == 4]
    if len(big) == 2 and all(sum(1 for a, b in edges if a in c and b in c) == 4
                             and all(len(adj[u]) == 2 for u in c) for c in big):
        CYCOK += 1
    k4 = sorted(x for x in kern if popc(x) == 4)
    k6 = sorted(x for x in kern if popc(x) == 6)
    edm = Counter()
    for a, b in edges:
        edm[vecs[a] ^ vecs[b]] += 1
    edc = Counter(edm.values())
    EDCENS.add(tuple(sorted(edc.items())))
    ALLCENS.add(tuple(sorted(Counter(dmult.values()).items())))
    ndf = vecs[nine[0]] ^ vecs[nine[1]] if nine is not None else 0
    if (inker == nh * (nh - 1) // 2 and len(edges) == 11 and all(popc(d) == 4 for d in edm)
            and sorted(edm) == k4 and len(k4) == 4 and len(k6) == 1 and popc(ndf) == 6 and ndf == k6[0]):
        DIFOK += 1

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
    r1 = 0
    r2 = 0
    if nine is not None:
        for i in range(nr):
            if (vecs[nine[0]] >> i) & 1 and not ((vecs[nine[1]] >> i) & 1):
                r1 |= sup[i]
            if (vecs[nine[1]] >> i) & 1 and not ((vecs[nine[0]] >> i) & 1):
                r2 |= sup[i]
    eqok = True
    for pa, pb, usz in eu:
        if sup[pa[0]] & sup[pa[1]]:
            eqok = False
        if sup[pb[0]] & sup[pb[1]]:
            eqok = False
        if (sup[pa[0]] | sup[pa[1]]) != (sup[pb[0]] | sup[pb[1]]):
            eqok = False
    EUSZ[tuple(sorted(v[2] for v in spl.values()))] += 1
    if len(eu) == 4 and len(spl) == 4 and sorted(spl) == k4 and eqok:
        EUOK += 1
    if r1 == r2:
        REMEQ += 1
    REMSZ[popc(r1) if r1 == r2 else -1] += 1

    # ---- the four toggles
    mov = Counter()
    brk = Counter()
    dis = Counter()
    outside = 0
    for dv in sorted(spl):
        ma, mb, usz = spl[dv]
        for w in vecs:
            x = w & dv
            if x == ma or x == mb:
                mov[dv] += 1
                if (w ^ dv) not in heldset:
                    outside += 1
            elif x == 0:
                dis[dv] += 1
            else:
                brk[dv] += 1
    inside = {}
    for dv in dmult:
        inside[dv] = sum(1 for w in vecs if (w ^ dv) in heldset)
    im2 = all(inside[dv] == 2 * dmult[dv] for dv in dmult)
    mm = [dv for dv in sorted(spl) if dmult[dv] == 6]
    MOVCENS.add(tuple(sorted(Counter(mov[dv] for dv in sorted(spl)).items())))
    BRKCENS.add(tuple(sorted(Counter(brk[dv] for dv in sorted(spl)).items())))
    if (outside == 0 and im2 and len(mm) == 1 and dis[mm[0]] == 0
            and all(mov[dv] == 2 * dmult[dv] for dv in sorted(spl))):
        TOGOK += 1

    # ---- the clean exchange
    clean = [dv for dv in sorted(spl) if brk[dv] == 0]
    cok = len(clean) == 1 and dmult[clean[0]] == 2 and mov[clean[0]] == 4
    if cok:
        CLNOK += 1

    # ---- the lemma witness: both half-pairings of the clean exchange
    lem = 0
    bperm = None
    if clean:
        cd = clean[0]
        ma, mb, usz = spl[cd]
        aa = [i for i in range(nr) if (ma >> i) & 1]
        bb = [i for i in range(nr) if (mb >> i) & 1]
        for tw in (0, 1):
            pi = list(range(nr))
            pi[aa[0]] = bb[tw]
            pi[bb[tw]] = aa[0]
            pi[aa[1]] = bb[1 - tw]
            pi[bb[1 - tw]] = aa[1]
            imb = [image(v, pi) for v in vecs]
            okb = frozenset(imb) == heldset
            okk = frozenset(image(x, pi) for x in kern) == kset
            okc = frozenset(image(x, pi) for x in coset) == cset
            if okb and okk and okc:
                pm = tuple(vidx[y] for y in imb)
                fx = sum(1 for i in range(nh) if pm[i] == i)
                tc = sum(1 for i in range(nh) if pm[i] != i and pm[pm[i]] == i)
                if fx == 10 and tc == 4 and all(pm[pm[i]] == i for i in range(nh)):
                    lem += 1
                    if bperm is None:
                        bperm = pm
                    elif bperm != pm:
                        bperm = ()
                    FIXCNT.add((fx, tc // 2))
    if lem == 2 and bperm:
        LEMOK += 1

    # ---- the complete self-equivalence search at this fiber
    aut = eqsearch(tuple(vecs), tuple(vecs), nr, True)
    idt = tuple(range(nh))
    ntr = [s for s in aut if s != idt]
    if len(aut) == 2 and idt in aut and len(ntr) == 1 and bperm and ntr[0] == bperm:
        SYMOK += 1

    # ---- the parity descent over every nonzero kernel vector
    ev = 0
    mx = 0
    hi = []
    for x in kern:
        if x == 0:
            continue
        ins = sum(1 for w in vecs if (w ^ x) in heldset)
        if (ins & 1) == 0 and ins == 2 * dmult.get(x, 0):
            ev += 1
        if dmult.get(x, 0) > mx:
            mx = dmult.get(x, 0)
        if dmult.get(x, 0) >= 7:
            hi.append(x)
    dom = [x for x in kern if x != 0 and dmult.get(x, 0) == mx]
    MAXM.add((mx, len(dom), len(hi)))
    exc = []
    brkset = []
    rsh = -1
    dgs = ()
    if len(dom) == 1 and dom[0] in spl:
        dv = dom[0]
        ma, mb, usz = spl[dv]
        exc = sorted(i for i in range(nh) if (vecs[i] ^ dv) not in heldset)
        brkset = sorted(i for i in range(nh) if (vecs[i] & dv) not in (0, ma, mb))
        if len(exc) == 2:
            rsh = popc(vecs[exc[0]] & vecs[exc[1]])
            dgs = tuple(sorted(len(adj[i]) for i in exc))
    RSHARE.add(rsh)
    DEGX.add(dgs)
    if (ev == len(kern) - 1 and mx == 6 and len(dom) == 1 and not hi and len(exc) == 2
            and exc == brkset and dgs == (0, 1) and nh - 2 * mx == 2):
        PAROK += 1

SH = only(SHAPES) or (0, 0, 0, 0, 0, 0, 0, 0)
PC = dict(only(PAIRSET)) if len(PAIRSET) == 1 else {}
GR = only(GRAPHS) or (0, (), ())
EDC = dict(only(EDCENS)) if len(EDCENS) == 1 else {}
ALC = dict(only(ALLCENS)) if len(ALLCENS) == 1 else {}
MOC = dict(only(MOVCENS)) if len(MOVCENS) == 1 else {}
BRC = dict(only(BRKCENS)) if len(BRKCENS) == 1 else {}
EUS = "; ".join(" ".join(str(x) for x in k) + " at " + str(EUSZ[k]) for k in sorted(EUSZ))
RMS = "; ".join(str(k) + " at " + str(REMSZ[k]) for k in sorted(REMSZ))
MX = only(MAXM) or (0, 0, 0)
RS = only(RSHARE)
RS = RS if RS is not None else -1
DG = only(DEGX) or ()
FX = only(FIXCNT) or (0, 0)

# ================================================================ G2 the linear instance, regated at every fiber

gate(NORB == set([200]) and SING == 0 and OVL == 0 and FOLDOK and INSOK == NF and SH == (14, 14, 40, 32, 8, 256, 256, 14)
     and CVRT == NF * 14 and len(PAIRSET) == 1 and PC == PAIR8, "G2",
     "at all {0} fibers: {1} two-orbits, {2} held cuttings each a union of {3} rows, {4} rows occur, rank {5}, kernel dimension {6}"
     .format(NF, only(NORB), SH[0], 12, SH[2], SH[3], SH[4]))
emit("G2 detail: all {0} kernel vectors have even weight, all {0} coset members solve the all ones system, and each of the {1} held"
     .format(SH[5], CVRT))
emit("G2 detail: cuttings covers every one of the {0} sample points exactly once; the fold of each fiber is one of {1} cell maps"
     .format(NPTS, 2))
emit("G2 detail: the pairwise shared-row census over the {0} pairs takes {1} distinct value over the {2} fibers, and reads"
     .format(sum(PC.values()), len(PAIRSET), NF))
emit("G2 detail: " + dshow(PC))

# ================================================================ G3 the minimal-exchange graph

gate(len(GRAPHS) == 1 and GR[0] == 11 and dict(GR[1]) == DEG3 and list(GR[2]) == SIZ3 and CYCOK == NF, "G3",
     "minimal exchanges, the pairs sharing {0} of their {1} rows, form a graph with {2} edges at every one of the {3} fibers"
     .format(10, 12, GR[0], NF))
emit("G3 detail: degree census {0}, five components of sizes {1}, and both components of size {2} are closed cycles of {2} edges"
     .format(dshow(dict(GR[1])), list(GR[2]), 4))

# ================================================================ G4 the differences are the light kernel vectors

gate(DIFOK == NF and len(EDCENS) == 1 and EDC == EDC4 and len(ALLCENS) == 1, "G4",
     "every pair difference lies in the kernel; the {0} edge differences have weight {1} and take {2} distinct values, census {3}"
     .format(GR[0], 4, sum(EDC.values()), dshow(EDC)))
emit("G4 detail: those {0} values are exactly the {0} kernel vectors of weight {1}, and the unique pair sharing {2} rows differs by"
     .format(4, 4, 9))
emit("G4 detail: the unique kernel vector of weight {0}; all of this holds at {1} of {1} fibers".format(6, NF))
emit("G4 detail: the multiplicity census of all distinct differences over the {0} pairs takes {1} distinct value over the {2} fibers,"
     .format(sum(PC.values()), len(ALLCENS), NF))
emit("G4 detail: and reads " + dshow(ALC))

# ================================================================ G5 the equal-union exchanges

gate(EUOK == NF and REMEQ == NF and dict(EUSZ) == EUANC and dict(REMSZ) == RMANC, "G5",
     "over the {0} rows there are exactly {1} equal-union exchanges at {2} of {3} fibers, and the union-size census over the fibers is anchored"
     .format(SH[2], 4, EUOK, NF))
emit("G5 detail: the {0} supports are exactly the {0} kernel vectors of weight {0} and each half is a disjoint pair of rows with equal"
     .format(4))
emit("G5 detail: union, at {0} of {1} fibers; the four union sizes read {2}".format(EUOK, NF, EUS))
emit("G5 detail: the two three-row remainders of the pair sharing {0} rows have equal point union at {1} of {2} fibers,"
     .format(9, REMEQ, NF))
emit("G5 detail: of sizes {0}".format(RMS))

# ================================================================ G6 the held set is closed under all four toggles

gate(TOGOK == NF and len(MOVCENS) == 1 and len(BRKCENS) == 1 and MOC == MOV6 and BRC == BRK6, "G6",
     "for all {0} exchanges every held cutting meeting a full half toggles to another held cutting, {1} images outside, at {2} fibers"
     .format(4, 0, NF))
emit("G6 detail: the moved census is {0} and the broken census is {1}, each {2} distinct value over the {3} fibers"
     .format(dshow(MOC), dshow(BRC), len(MOVCENS), NF))
emit("G6 detail: inside(d) equals {0} times the multiplicity of d for every distinct pair difference, and the multiplicity {1}"
     .format(2, 6))
emit("G6 detail: exchange meets all {0} held cuttings, none disjoint from its {1} rows".format(14, 4))

# ================================================================ G7 exactly one exchange is clean

gate(CLNOK == NF, "G7",
     "exactly {0} of the {1} exchanges is clean, with broken count {2}; it has multiplicity {3} and moves {4} cuttings, at {5} of {5} fibers"
     .format(1, 4, 0, 2, 4, NF))

# ================================================================ G8 the clean exchange extends to the coordinates

gate(LEMOK == NF and len(FIXCNT) == 1 and FX == (10, 2), "G8",
     "both half-pairings of the clean exchange carry the {0} held cuttings, the {1} kernel vectors and the {1} coset members onto themselves"
     .format(SH[0], SH[5]))
emit("G8 detail: each is a product of two transpositions of the {0} coordinates, and the induced block permutation fixes {1} blocks"
     .format(SH[2], FX[0]))
emit("G8 detail: identically as sets and has {0} two-cycles, the same permutation for either pairing, at {1} of {1} fibers"
     .format(FX[1], NF))

# ================================================================ G9 that toggle is the whole symmetry

gate(SYMOK == NF, "G9",
     "the complete block-level self-equivalence search returns exactly {0} at {1} of {1} fibers, and the nontrivial one is the clean toggle"
     .format(2, NF))

# ================================================================ G10 the parity descent

gate(PAROK == NF and len(MAXM) == 1 and MX == (6, 1, 0) and len(RSHARE) == 1 and RS >= 0 and len(DEGX) == 1 and DG == (0, 1),
     "G10", "over all {0} nonzero kernel vectors inside(d) is even and equals {1} times the multiplicity of d, at {2} of {2} fibers"
     .format(SH[5] - 1, 2, NF))
emit("G10 detail: the maximum multiplicity is {0}, attained by exactly {1} kernel vector, and {2} vector attains {3} or more"
     .format(MX[0], MX[1], MX[2], 7))
emit("G10 detail: so the evaders at the maximum number {0}, exactly the dominant exchange's broken pair, of graph degrees {1}"
     .format(SH[0] - 2 * MX[0], list(DG)))
emit("G10 detail: the two exceptional cuttings share {0} rows, {1} distinct value over the {2} fibers; {3} = {4} pairs + {5}"
     .format(RS, len(RSHARE), NF, SH[0], MX[0], SH[0] - 2 * MX[0]))

# ================================================================ totals

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
