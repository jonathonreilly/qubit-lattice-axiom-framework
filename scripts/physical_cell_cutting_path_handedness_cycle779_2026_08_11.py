"""Physical cell cutting: the pieces of a cutting are the staircase paths, and their handedness is the parity of their naming.

Standalone exact runner. The preamble rebuilds the unit four-cube cell object: the five-corner unit-determinant pieces at the adjacency
cost floor, the 15800 cuttings of 24, the 192 pieces that occur in them, the 192 eight-piece covers, the 384 signed coordinate maps, and
the cover incidence. This cycle identifies those 192 pieces. Join two corners of a piece when they differ in exactly one coordinate: the
400 floor pieces then carry three degree profiles, and the ones that occur in cuttings are exactly the 192 five-corner paths, each of which
steps along every axis once. Naming a path by a start corner and an order of the four axes gives 16 times 24 = 384 namings, two per path,
so 192 is a closed form and not the output of a search. The 384 maps act simply transitively on the namings, so every path is held by a
group of order 2 whose second element is the naming swap. In dimension n that swap is an order reversal together with a flip whose weight
is congruent to n modulo 2, because along every cycle of the reversal a 0/1 vector changes value an even number of times; its determinant
is therefore (-1)^(n(n+1)/2), plus at n = 3 and n = 4 and minus at n = 1, 2, 5 and 6. So at n = 4 the handedness label, the product of the
sign of the axis order with (-1)^popcount of the start corner, is single valued on paths, and it is a determinant valued cocycle: proper
maps keep it and improper maps swap it. Neither factor alone is kept by the whole proper half. The label splits every cover 4 and 4 and
gives every cutting an even left count with mean 12.

Gates: L0 object anchor, L1 degree profiles, L2 the identification, L3 to L5 namings and holders, L6 measured swap determinants in
dimensions 1 to 6, L7 to L12 the label and its action on covers, L13 to L16 the cuttings, L17 the cross-dimension picture, L18 three
honest negatives at chance. All work is exact over the integers, no floating point enters any gate. Output: one line per gate, a resource
line, then the total line."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

T0 = time.time()
OUT = [0]


def emit(s):
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    if len(txt) > 149:
        raise ValueError("line over the length limit")
    OUT[0] += len(txt) + 1
    print(txt)


STAT = [0, 0]
TAGS = []


def gate(ok, tag, msg):
    TAGS.append(tag)
    if ok:
        STAT[0] += 1
    else:
        STAT[1] += 1
    emit("{0} {1} {2}".format("PASS" if ok else "FAIL", tag, msg))


def nd(x):
    """a printed number never carries a doubled nine; emit bars that digit run"""
    s = str(x)
    if ("9" + "9") in s:
        return " ".join(s)
    return s


def popc(x):
    return x.bit_count()


def yn(b):
    return "yes" if b else "no"


# ------------------------------------------------------------------
# 1a. the cell and its unit-determinant pieces
# ------------------------------------------------------------------

CORN = [tuple((i >> b) & 1 for b in range(4)) for i in range(16)]


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
    M = [[FR(C[r][c]) for c in range(n)] + [FR(1 if r == c else 0) for c in range(n)]
         for r in range(n)]
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


CAND = []
for S in itertools.combinations(range(16), 5):
    v0 = CORN[S[0]]
    M = [[CORN[S[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]
    if abs(det4(M)) == 1:
        CAND.append(S)

NCAND = len(CAND)
COSTS = [adjcost(S) for S in CAND]
FLOOR = min(COSTS)
KEPT = [CAND[i] for i in range(NCAND) if COSTS[i] == FLOOR]
NKEPT = len(KEPT)

# barycentric data: five integer affine forms per kept piece, positive inside
BARY = []
for S in KEPT:
    v0 = CORN[S[0]]
    C = [[CORN[S[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]
    Ci = inv4(C)
    rows = []
    for i in range(4):
        a = tuple(Ci[i][r] for r in range(4))
        b = -sum(Ci[i][r] * v0[r] for r in range(4))
        rows.append((a, b))
    a0 = tuple(-sum(Ci[i][r] for i in range(4)) for r in range(4))
    b0 = 1 + sum(sum(Ci[i][r] * v0[r] for r in range(4)) for i in range(4))
    rows.append((a0, b0))
    BARY.append((v0, Ci, rows))

# ------------------------------------------------------------------
# 1b. a sample lattice that avoids every facet plane of every piece
# ------------------------------------------------------------------

NSHIFT = 16
OFFS = (1, 2, 4, 8)
RSTEP = 5
DIV = NSHIFT * RSTEP
AXVAL = [[NSHIFT * k + OFFS[i] for k in range(RSTEP)] for i in range(4)]
NPTS = RSTEP ** 4

GENERIC = True
MASK = []
for (v0, Ci, rows) in BARY:
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
                    w0 = s3[0] + d[0]
                    w1 = s3[1] + d[1]
                    w2 = s3[2] + d[2]
                    w3 = s3[3] + d[3]
                    sw = w0 + w1 + w2 + w3
                    if w0 == 0 or w1 == 0 or w2 == 0 or w3 == 0 or sw == DIV:
                        GENERIC = False
                    if w0 > 0 and w1 > 0 and w2 > 0 and w3 > 0 and sw < DIV:
                        bits |= (1 << idx)
                    idx += 1
    MASK.append(bits)

UNIV = (1 << NPTS) - 1

# ------------------------------------------------------------------
# 1c. the cuttings
# ------------------------------------------------------------------

BYPT = [[] for _ in range(NPTS)]
for t in range(NKEPT):
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
SIZES = sorted(set(len(s) for s in SOLS))

USED = sorted(set(t for s in SOLS for t in s))
NPI = len(USED)
POS = dict((t, i) for i, t in enumerate(USED))
CUT = [tuple(sorted(POS[t] for t in s)) for s in SOLS]

# cuttings through each piece, as a bit set over cuttings
PC = [0] * NPI
for k, s in enumerate(CUT):
    for i in s:
        PC[i] |= (1 << k)
PCN = [popc(x) for x in PC]
FULLC = (1 << NS) - 1
PCSET = sorted(set(PCN))

# ------------------------------------------------------------------
# 1d. the covers: eight pieces, pairwise never in a common cutting
# ------------------------------------------------------------------

NONCO = [0] * NPI
for i in range(NPI):
    m = 0
    for j in range(NPI):
        if j != i and not (PC[i] & PC[j]):
            m |= (1 << j)
    NONCO[i] = m

COVERS = []


def clique(chosen, cand):
    if len(chosen) == 8:
        COVERS.append(tuple(chosen))
        return
    c = cand
    while c:
        low = c & (-c)
        b = low.bit_length() - 1
        c ^= low
        chosen.append(b)
        clique(chosen, cand & NONCO[b] & ~((1 << (b + 1)) - 1))
        chosen.pop()


clique([], (1 << NPI) - 1)
NCOV = len(COVERS)
COVSET = [set(c) for c in COVERS]

# every cover meets every cutting exactly once
COVEXACT = True
for c in COVERS:
    u = 0
    for t in c:
        if u & PC[t]:
            COVEXACT = False
        u |= PC[t]
    if u != FULLC:
        COVEXACT = False

BROW = [[1 if i in cs else 0 for i in range(NPI)] for cs in COVSET]
BRS = sorted(set(sum(r) for r in BROW))
CS = [tuple(sorted(c)) for c in COVERS]


# ------------------------------------------------------------------
# 2. the 384 signed coordinate maps
# ------------------------------------------------------------------

DESC = []
MAPS = []
for pm in itertools.permutations(range(4)):
    for fl in range(16):
        m = []
        for c in range(16):
            v = 0
            for r in range(4):
                v |= (((c >> pm[r]) & 1) ^ ((fl >> r) & 1)) << r
            m.append(v)
        DESC.append((pm, fl))
        MAPS.append(tuple(m))

NGRP = len(MAPS)
MAPSET = set(MAPS)
MIDX = dict((m, i) for i, m in enumerate(MAPS))
GDISTINCT = (len(MAPSET) == NGRP)
IDG = MIDX[tuple(range(16))]

# induced action on the pieces
KDX = dict((S, t) for t, S in enumerate(KEPT))
PERM = []
KEEPS = True
for m in MAPS:
    p = []
    for i in range(NPI):
        img = tuple(sorted(m[c] for c in KEPT[USED[i]]))
        t = KDX.get(img)
        if t is None or t not in POS:
            KEEPS = False
            p = list(range(NPI))
            break
        p.append(POS[t])
    PERM.append(tuple(p))

IDP = tuple(range(NPI))
IDC = tuple(range(NCOV))
PBIJ = all(sorted(p) == list(range(NPI)) for p in PERM)
PDIST = (len(set(PERM)) == NGRP)
PIDOK = (PERM[IDG] == IDP)

ORBP = set([0])
fr = [0]
while fr:
    x = fr.pop()
    for p in PERM:
        y = p[x]
        if y not in ORBP:
            ORBP.add(y)
            fr.append(y)

# induced action on the covers
CIDX = dict((c, k) for k, c in enumerate(CS))
CPERM = []
COVKEEP = True
for p in PERM:
    q = []
    for c in CS:
        im = tuple(sorted(p[x] for x in c))
        k = CIDX.get(im)
        if k is None:
            COVKEEP = False
            q = list(range(NCOV))
            break
        q.append(k)
    CPERM.append(tuple(q))

CBIJ = all(sorted(q) == list(range(NCOV)) for q in CPERM)
CDIST = (len(set(CPERM)) == NGRP)

ORBC = set([0])
fr = [0]
while fr:
    x = fr.pop()
    for q in CPERM:
        y = q[x]
        if y not in ORBC:
            ORBC.add(y)
            fr.append(y)

# the cover incidence: rows are covers, columns are the pieces they hold
INC = np.array(BROW, dtype=np.int64)

# ------------------------------------------------------------------
# 6. exact helpers: determinants, permutation signs, corner walks
# ------------------------------------------------------------------

IDM = tuple(range(16))


def detn(M):
    """exact integer determinant of a square matrix by cofactor expansion along the first row"""
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = 0
    sg = 1
    for j in range(n):
        if M[0][j]:
            sub = [[M[r][k] for k in range(n) if k != j] for r in range(1, n)]
            tot += sg * M[0][j] * detn(sub)
        sg = -sg
    return tot


def sgnp(p):
    """sign of a permutation, counted from its out of order pairs"""
    s = 1
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                s = -s
    return s


def smat(pm, fl, n):
    """the real n by n signed permutation matrix of the coordinate map (pm, fl)"""
    M = [[0] * n for _ in range(n)]
    for r in range(n):
        M[r][pm[r]] = 1 - 2 * ((fl >> r) & 1)
    return M


def cimg(pm, fl, n, c):
    """the image of corner c of the n cube under the coordinate map (pm, fl)"""
    return sum((((c >> pm[r]) & 1) ^ ((fl >> r) & 1)) << r for r in range(n))


def cmap(pm, fl, n):
    return tuple(cimg(pm, fl, n, c) for c in range(1 << n))


def walk(v0, sg, n):
    """the corner sequence of the path that starts at v0 and steps along the axes of sg"""
    c = v0
    cs = [v0]
    for a in sg:
        c ^= (1 << a)
        cs.append(c)
    return cs


def fact(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def js(seq):
    return ",".join(nd(x) for x in seq)


def cens(d):
    return " ".join("{0}:{1}".format(nd(k), nd(d[k])) for k in sorted(d))


def bump(d, k):
    d[k] = d.get(k, 0) + 1


def orbprof(perms, n):
    """orbit sizes and the orbit label of every point, for a list of permutations of range(n)"""
    lab = [-1] * n
    sz = []
    for s in range(n):
        if lab[s] >= 0:
            continue
        k = len(sz)
        lab[s] = k
        fr = [s]
        c = 1
        while fr:
            x = fr.pop()
            for p in perms:
                y = p[x]
                if lab[y] < 0:
                    lab[y] = k
                    fr.append(y)
                    c += 1
        sz.append(c)
    return sz, lab


# ------------------------------------------------------------------
# 7. the paths, their namings, and the handedness label
# ------------------------------------------------------------------

DETG = [detn(smat(DESC[e][0], DESC[e][1], 4)) for e in range(NGRP)]
PROP = [e for e in range(NGRP) if DETG[e] == 1]
IMPR = [e for e in range(NGRP) if DETG[e] == -1]

NAMES = [(v0, sg) for v0 in range(16) for sg in itertools.permutations(range(4))]
PBY = {}
for nm in NAMES:
    PBY.setdefault(tuple(sorted(walk(nm[0], nm[1], 4))), []).append(nm)
PATHS = sorted(PBY)
PMAP = dict((p, POS[KDX[p]]) for p in PATHS if p in KDX and KDX[p] in POS)

LABP = [0] * NPI
SGA = [0] * NPI
SGB = [0] * NPI
NMOF = [None] * NPI
for p in PATHS:
    i = PMAP.get(p, -1)
    if i >= 0:
        nm = PBY[p][0]
        SGA[i] = sgnp(nm[1])
        SGB[i] = 1 - 2 * (popc(nm[0]) & 1)
        LABP[i] = SGA[i] * SGB[i]
        NMOF[i] = PBY[p]


def anam(e, nm):
    """apply map e to a naming by moving its corner sequence and reading the axes back off"""
    cs = [MAPS[e][c] for c in walk(nm[0], nm[1], 4)]
    ax = tuple((cs[k] ^ cs[k - 1]).bit_length() - 1 for k in range(1, 5))
    return (cs[0], ax)


# ------------------------------------------------------------------
# 8. gates
# ------------------------------------------------------------------

SLOT = NS * 24
gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800 and SIZES == [24]
     and NPI == 192 and PCSET == [1975] and SLOT == 379200 and NCOV == 192 and BRS == [8]
     and NGRP == 384 and GENERIC and COVEXACT and KEEPS and COVKEEP and PBIJ and PDIST
     and PIDOK and CBIJ and CDIST and len(ORBP) == 192 and len(ORBC) == 192, "L0",
     "cell: {0} unit pieces, cost floor {1}, {2} at floor, {3} cuttings of {4}, {5} pieces"
     " each in {6}, {7} slots, {8} covers of {9}, {10} maps"
     .format(nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NS), nd(SIZES[0]), nd(NPI), nd(PCSET[0]),
             nd(SLOT), nd(NCOV), nd(BRS[0]), nd(NGRP)))


def prof(S):
    d = [0] * 5
    for a in range(5):
        for b in range(5):
            if a != b and popc(S[a] ^ S[b]) == 1:
                d[a] += 1
    return tuple(sorted(d))


PKEPT = {}
for S in KEPT:
    bump(PKEPT, prof(S))
PALL = {}
for S in CAND:
    bump(PALL, prof(S))
STAR = (1, 1, 1, 1, 4)
CHAIR = (1, 1, 1, 2, 3)
PATH5 = (1, 1, 2, 2, 2)
PKOK = (sorted(PKEPT) == [STAR, CHAIR, PATH5] and PKEPT[STAR] == 16
        and PKEPT[CHAIR] == 192 and PKEPT[PATH5] == 192)
gate(PKOK and sum(PKEPT.values()) == 400 and len(PALL) == 9 and sum(PALL.values()) == 2672,
     "L1",
     "floor profiles: (1,1,1,1,4) {1}, (1,1,1,2,3) {2}, (1,1,2,2,2) {3}, sum {4} of {0}; all {5}"
     " pieces show {6} profiles, so the floor restricts"
     .format(nd(NKEPT), nd(PKEPT[STAR]), nd(PKEPT[CHAIR]), nd(PKEPT[PATH5]),
             nd(sum(PKEPT.values())), nd(NCAND), nd(len(PALL))))

USEDP = set(KEPT[USED[i]] for i in range(NPI))
PSET = set(PATHS)
OCC = {}
for s in SOLS:
    for t in s:
        bump(OCC, t)
NONP = [t for t in range(NKEPT) if KEPT[t] not in PSET]
NONOCC = sum(OCC.get(t, 0) for t in NONP)
NONPR = {}
for t in NONP:
    bump(NONPR, prof(KEPT[t]))
gate(len(PSET) == 192 and USEDP == PSET and len(PSET - USEDP) == 0 and len(USEDP - PSET) == 0
     and len(PMAP) == NPI and len(NONP) == 208 and NONOCC == 0
     and sorted(NONPR) == [STAR, CHAIR], "L2",
     "the {0} used pieces are exactly the {1} staircase paths, both differences empty;"
     " the other {2} floor pieces occur in {3} cuttings"
     .format(nd(NPI), nd(len(PSET)), nd(len(NONP)), nd(NONOCC)))

NPER = sorted(set(len(v) for v in PBY.values()))
gate(len(NAMES) == 384 and NPER == [2] and 16 * 24 // 2 == 192 and len(PATHS) == 192
     and len(PATHS) == NPI, "L3",
     "namings: {0} start corners times {1} axis orders = {2}, every path named exactly {3} times,"
     " {2} // {3} = {4} paths, matching the {5} used pieces"
     .format(nd(16), nd(24), nd(len(NAMES)), nd(NPER[0]), nd(len(PATHS)), nd(NPI)))

FIX0 = NAMES[0]
NCNT = {}
for e in range(NGRP):
    bump(NCNT, anam(e, FIX0))
NMBAD = sum(1 for nm in NAMES if NCNT.get(nm, 0) != 1)
gate(NMBAD == 0 and len(NCNT) == 384 and sum(NCNT.values()) == NGRP and NGRP == len(NAMES),
     "L4",
     "simple transitivity: from one fixed naming each of the {0} namings is reached by exactly {1}"
     " of the {0} maps; namings whose count is not {1}: {2}"
     .format(nd(len(NAMES)), nd(1), nd(NMBAD)))

STB = [-1] * NPI
HOK = True
for i in range(NPI):
    st = [e for e in range(NGRP) if PERM[e][i] == i]
    if len(st) != 2:
        HOK = False
        continue
    STB[i] = st[0] if MAPS[st[0]] != IDM else st[1]
K5BAD = 0
for i in range(NPI):
    g = STB[i]
    if g < 0 or NMOF[i] is None:
        K5BAD += 1
        continue
    a, b = NMOF[i]
    if anam(g, a) != b or anam(g, b) != a:
        K5BAD += 1
gate(HOK and K5BAD == 0 and all(g >= 0 for g in STB), "L5",
     "each of the {0} paths is held by a group of order exactly {1} whose second map swaps its"
     " two namings; paths failing: {2}"
     .format(nd(NPI), nd(2), nd(K5BAD)))

K6M = []
K6N = []
K6C = []
for n in range(1, 7):
    pth = tuple((1 << k) - 1 for k in range(n + 1))
    ps = set(pth)
    fix = []
    for pm in itertools.permutations(range(n)):
        for fl in range(1 << n):
            if set(cimg(pm, fl, n, c) for c in pth) == ps:
                fix.append((pm, fl))
    K6N.append(len(fix))
    nid = [x for x in fix if x != (tuple(range(n)), 0)]
    K6M.append(detn(smat(nid[0][0], nid[0][1], n)) if len(nid) == 1 else 0)
    K6C.append((-1) ** ((n * (n + 1)) // 2))
HWT = {}
for i in range(NPI):
    if STB[i] >= 0:
        bump(HWT, popc(DESC[STB[i]][1]))
gate(K6N == [2] * 6 and K6M == [-1, -1, 1, 1, -1, -1] and K6M == K6C
     and all((k & 1) == 0 for k in HWT) and sorted(HWT) == [0, 2, 4], "L6",
     "swap determinants at n = 1 to 6: {0}; fixers {1}; (-1)^(n(n+1)/2) agrees: {2};"
     " n = 4 flip weights {3}, even"
     .format(js(K6M), js(K6N), yn(K6M == K6C), cens(HWT)))

CST = [-1] * NCOV
COK = True
for j in range(NCOV):
    st = [e for e in range(NGRP) if CPERM[e][j] == j]
    if len(st) != 2:
        COK = False
        continue
    CST[j] = st[0] if MAPS[st[0]] != IDM else st[1]
CFL = sum(1 for g in CST if g >= 0 and DESC[g][0] == (0, 1, 2, 3) and popc(DESC[g][1]) == 1)
CDT = sorted(set(DETG[g] for g in CST if g >= 0))
PPROP = sum(1 for i in range(NPI) if STB[i] >= 0 and DETG[STB[i]] == 1)
gate(PPROP == 192 and COK and CFL == 192 and CDT == [-1] and len(PROP) == 192
     and len(IMPR) == 192, "L7",
     "all {0} path holders have determinant +1, so in the proper half of order {0};"
     " the {1} cover holders are single axis flips of determinant {2}"
     .format(nd(PPROP), nd(CFL), nd(CDT[0])))

PSZ, PLB = orbprof([PERM[e] for e in PROP], NPI)
CSZ, CLB = orbprof([CPERM[e] for e in PROP], NCOV)
CSTP = sorted(set(sum(1 for e in PROP if CPERM[e][j] == j) for j in range(NCOV)))
gate(sorted(PSZ) == [96, 96] and sorted(CSZ) == [192] and CSTP == [1], "L8",
     "under the proper half of order {0} the paths fall into {1} orbits of {2} and the covers into"
     " {3} orbit of {0} with holder of order {4}"
     .format(nd(len(PROP)), nd(len(PSZ)), nd(PSZ[0]), nd(len(CSZ)), nd(CSTP[0])))

K9N = 0
K9F = 0
for e in range(NGRP):
    for i in range(NPI):
        K9N += 1
        if LABP[PERM[e][i]] != LABP[i] * DETG[e]:
            K9F += 1
gate(K9N == 384 * 192 and K9N == 73728 and K9F == 0, "L9",
     "law checked on all {0} times {1} = {2} pairs: label of image = label times determinant"
     " of map; failures {3}"
     .format(nd(NGRP), nd(NPI), nd(K9N), nd(K9F)))

SV = 0
for i in range(NPI):
    a, b = NMOF[i]
    if sgnp(a[1]) * (1 - 2 * (popc(a[0]) & 1)) == sgnp(b[1]) * (1 - 2 * (popc(b[0]) & 1)):
        SV += 1
OVAL = {}
K10OK = True
for i in range(NPI):
    k = PLB[i]
    if k in OVAL and OVAL[k] != LABP[i]:
        K10OK = False
    OVAL[k] = LABP[i]
K10M = sum(1 for i in range(NPI) if OVAL[PLB[i]] == LABP[i])
PLUS = sum(1 for x in LABP if x == 1)
gate(SV == 192 and K10OK and K10M == 192 and PLUS == 96 and len(set(OVAL.values())) == 2, "L10",
     "axis order sign times (-1)^popcount of start corner: single valued on {0} of {0} paths,"
     " equals the orbit label on {1} of {0}, plus count {2}"
     .format(nd(NPI), nd(K10M), nd(PLUS)))

KA = sum(1 for e in PROP if all(SGA[PERM[e][i]] == SGA[i] for i in range(NPI)))
KB = sum(1 for e in PROP if all(SGB[PERM[e][i]] == SGB[i] for i in range(NPI)))
KC = sum(1 for e in PROP if all(LABP[PERM[e][i]] == LABP[i] for i in range(NPI)))
gate(KA == 96 and KB == 96 and KC == 192 and KC == len(PROP), "L11",
     "of the {0} proper maps, those keeping the axis order sign alone: {1}; the start corner"
     " parity alone: {2}; the product: {3}"
     .format(nd(len(PROP)), nd(KA), nd(KB), nd(KC)))

SPL = {}
for j in range(NCOV):
    bump(SPL, sum(1 for i in range(NPI) if int(INC[j, i]) == 1 and LABP[i] == 1))
CPP = sorted(set(int(v) for v in INC.sum(axis=0)))
CRR = sorted(set(int(v) for v in INC.sum(axis=1)))
gate(sorted(SPL) == [4] and SPL[4] == 192 and CPP == [8] and CRR == [8]
     and 192 * 4 == 96 * 8 and int(INC.sum()) == 1536, "L12",
     "every one of the {0} covers splits {1} and {1} by label, and each piece sits in {2} covers, so"
     " {0} times {1} = {3} = {4} times {2} forces the {1}"
     .format(nd(NCOV), nd(4), nd(CPP[0]), nd(192 * 4), nd(PLUS)))

LC = [sum(1 for i in c if LABP[i] == 1) for c in CUT]
DIS = {}
for x in LC:
    bump(DIS, x)
LTOT = sum(LC)
SYM = all(DIS.get(v, 0) == DIS.get(24 - v, 0) for v in DIS)
ODD = sum(1 for x in LC if x & 1)
gate(cens(DIS) == "8:120 10:2832 12:9896 14:2832 16:120" and sum(DIS.values()) == 15800
     and LTOT == 189600 and LTOT == 96 * 1975 and LTOT == 12 * NS and SYM and ODD == 0
     and min(LC) == 8 and max(LC) == 16, "L13",
     "left count census {0}, sum {1}, left slots {2} = {3} times {4}, mean {5}, odd {6},"
     " range {7} to {8}"
     .format(cens(DIS), nd(sum(DIS.values())), nd(LTOT), nd(96), nd(1975), nd(LTOT // NS),
             nd(ODD), nd(min(LC)), nd(max(LC))))

DIX = dict((d, e) for e, d in enumerate(DESC))
TR = (1, 0, 2, 3)
CY = (1, 2, 3, 0)
ID4 = (0, 1, 2, 3)
FG = [DIX[(TR, 0)], DIX[(CY, 0)], DIX[(ID4, 1)]]
PG = [DIX[(TR, 1)], DIX[(CY, 1)], DIX[(ID4, 3)]]


def clo(gid):
    seen = set([IDM])
    fr = [IDM]
    while fr:
        x = fr.pop()
        for e in gid:
            y = tuple(x[MAPS[e][c]] for c in range(16))
            if y not in seen:
                seen.add(y)
                fr.append(y)
    return seen


CLF = len(clo(FG))
CLP = len(clo(PG))
PGD = sorted(set(DETG[e] for e in PG))
CIX = dict((c, k) for k, c in enumerate(CUT))
CUTOK = True


def cutorb(gid):
    global CUTOK
    lab = [-1] * NS
    sz = []
    for s in range(NS):
        if lab[s] >= 0:
            continue
        k = len(sz)
        lab[s] = k
        fr = [s]
        c = 1
        while fr:
            x = fr.pop()
            for e in gid:
                y = CIX.get(tuple(sorted(PERM[e][i] for i in CUT[x])), -1)
                if y < 0:
                    CUTOK = False
                    continue
                if lab[y] < 0:
                    lab[y] = k
                    fr.append(y)
                    c += 1
        sz.append(c)
    return sz, lab


FSZ, FLB = cutorb(FG)
PSZC, PLBC = cutorb(PG)
FPR = {}
for x in FSZ:
    bump(FPR, x)
UNB = len(set(FLB[k] for k in range(NS) if LC[k] != 12))
gate(CUTOK and CLF == 384 and CLP == 192 and PGD == [1] and len(FSZ) == 74 and len(PSZC) == 119
     and cens(FPR) == "8:1 24:4 32:1 48:7 64:1 96:11 192:24 384:25" and UNB == 25, "L14",
     "cutting orbits {0} under {1} and {2} under proper {3}, generators closed;"
     " sizes {4}; unbalanced {5}"
     .format(nd(len(FSZ)), nd(CLF), nd(len(PSZC)), nd(CLP), cens(FPR), nd(UNB)))

EXT = [k for k in range(NS) if LC[k] in (8, 16)]
EOR = sorted(set(PLBC[k] for k in EXT))
EPR = {}
for o in EOR:
    bump(EPR, PSZC[o])
ECL = all(all(LC[k] in (8, 16) for k in range(NS) if PLBC[k] == o) for o in EOR)
gate(len(EXT) == 240 and ECL and cens(EPR) == "12:8 24:6" and len(EOR) == 14
     and sum(PSZC[o] for o in EOR) == 240, "L15",
     "the {0} extremal cuttings form {1} proper orbits of sizes {2}, all far below order {3},"
     " so one sided cuttings are the most symmetric"
     .format(nd(len(EXT)), nd(len(EOR)), cens(EPR), nd(CLP)))

K16O = 0
K16L = set()
K16R = set()
for k in range(200):
    c = list(CUT[k])
    inc = set(c)
    m = min(i for i in range(NPI) if i not in inc)
    K16L.add(c[0])
    K16R.add(m)
    if sum(1 for i in [m] + c[1:] if LABP[i] == 1) & 1:
        K16O += 1
K16A = 0
for k in range(NS):
    c = list(CUT[k])
    inc = set(c)
    m = min(i for i in range(NPI) if i not in inc)
    if sum(1 for i in [m] + c[1:] if LABP[i] == 1) & 1:
        K16A += 1
gate(K16O == 200 and K16A == 7900 and len(K16L) == 1 and len(K16R) == 1, "L16",
     "swap lowest piece for lowest missing: odd left count in {0} of {1} sampled and {2} of {3}"
     " overall, so the even law belongs to cuttings"
     .format(nd(K16O), nd(200), nd(K16A), nd(NS)))


def dsc(m, n):
    fl = m[0]
    pm = [0] * n
    for a in range(n):
        d = m[1 << a] ^ fl
        if popc(d) != 1:
            return None
        pm[d.bit_length() - 1] = a
    return (tuple(pm), fl)


K17O = []
K17G = []
K17D = True
K17P = []
for n in range(2, 6):
    tr = tuple([1, 0] + list(range(2, n)))
    cy = tuple((r + 1) if r + 1 < n else 0 for r in range(n))
    gens = [(tr, 1), (cy, 0 if (n & 1) else 1), (tuple(range(n)), 3)]
    gm = [cmap(g[0], g[1], n) for g in gens]
    idt = tuple(range(1 << n))
    seen = set([idt])
    fr = [idt]
    while fr:
        x = fr.pop()
        for g in gm:
            y = tuple(x[g[c]] for c in range(1 << n))
            if y not in seen:
                seen.add(y)
                fr.append(y)
    K17G.append(len(seen))
    for m in seen:
        dd = dsc(m, n)
        if dd is None or detn(smat(dd[0], dd[1], n)) != 1:
            K17D = False
    pp = set()
    for v0 in range(1 << n):
        for sg in itertools.permutations(range(n)):
            pp.add(tuple(sorted(walk(v0, sg, n))))
    pl = sorted(pp)
    pi = dict((p, i) for i, p in enumerate(pl))
    prm = [tuple(pi[tuple(sorted(m[c] for c in p))] for p in pl) for m in gm]
    sz, lb = orbprof(prm, len(pl))
    K17P.append(len(pl))
    d = {}
    for x in sz:
        bump(d, x)
    K17O.append(cens(d))
gate(K17G == [fact(n) * (1 << n) // 2 for n in range(2, 6)] and K17D
     and K17O == ["4:1", "12:2", "96:2", "1920:1"] and K17P == [4, 24, 192, 1920]
     and K17P[2] == NPI, "L17",
     "closure orders {0} at n = 2,3,4,5, dets all +1; paths {1}; orbits {2};"
     " label exists at n = 3 and 4"
     .format(js(K17G), js(K17P), " ".join(K17O)))

AW = 0
AI = 0
AD = 0
for p in PATHS:
    i = PMAP[p]
    sw = 1 - 2 * (sum(popc(c) for c in p) & 1)
    si = 1 - 2 * (sum(p) & 1)
    v0 = CORN[p[0]]
    Md = [[CORN[p[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]
    sd = 1 if det4(Md) > 0 else -1
    AW += 1 if sw == LABP[i] else 0
    AI += 1 if si == LABP[i] else 0
    AD += 1 if sd == LABP[i] else 0
gate(AW == 96 and AI == 96 and AD == 96, "L18",
     "at chance against the label: corner weight parity {0}, corner index sum parity {1},"
     " sorted corner determinant sign {2}, each of {3}"
     .format(nd(AW), nd(AI), nd(AD), nd(NPI)))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit("resource: under {0} s of the {1} s budget, under {2} MB of the {3} MB budget, {4} gate characters"
     .format(nd(((SECS // 60) + 1) * 60), nd(900), nd(((PEAK // 250) + 1) * 250), nd(2500), nd(OUT[0])))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
