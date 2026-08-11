"""Every orbit of the physical cell cutting pair action has table rank 144.

Standalone exact runner. It rebuilds the unit four-cube cell object from scratch:
the sixteen corners, the five-corner unit-determinant pieces at the adjacency cost
floor, the cuttings by them, the pieces that occur, and the eight-piece covers.
The group of 384 signed coordinate maps is built by permuting the four coordinates
and flipping any of them, and it is transitive on the 192 pieces and on the 192
covers with point stabilisers of order two.

The subject of this cycle is the action of that group on the 36864 pairs made of
one piece and one cover. Twelve non-identity maps fix a piece and four fix a
cover, and the two sets are disjoint, so no non-identity map fixes a pair: the
action is free, with exactly 96 orbits each of the full size 384. Read as a zero
and one table over covers by pieces, every orbit carries two ones in each row and
two in each column, and its bipartite graph splits into 48 cycles of length eight,
because the 48 products of a piece stabiliser generator with a cover stabiliser
generator all have order exactly four. Each cycle contributes the 4 by 4 block
with ones on the diagonal and on the cyclic superdiagonal, of determinant zero
and with a unimodular leading 3 by 3 minor. So the rank 144 and the nullity 48
of every one of the 96 tables follow in every characteristic from a single 4 by 4
determinant, with no 192 by 192 elimination anywhere, and the kernel is exhibited
rather than inferred. Two rejectors show the gates discriminate.

All work is exact over the integers and two fixed primes; no floating point enters
any gate and no constant is fitted.

Output: one line per gate, two summary lines, then the total line."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

PRIME = 1000003
PRIME2 = 1000033
SEED = 3

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


def rank_modp(Mx, p):
    A = np.mod(np.array(Mx, dtype=np.int64), p)
    nr, nc = A.shape
    r = 0
    for c in range(nc):
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        piv = r + int(nz[0])
        if piv != r:
            tmp = A[r].copy()
            A[r] = A[piv]
            A[piv] = tmp
        iv = pow(int(A[r, c]), p - 2, p)
        A[r] = np.mod(A[r] * iv, p)
        if r + 1 < nr:
            A[r + 1:] = np.mod(A[r + 1:] - np.outer(A[r + 1:, c], A[r]), p)
        r += 1
        if r == nr:
            break
    return int(r)


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

COMP = []
CLOSED = True
for a in MAPS:
    row = []
    for b in MAPS:
        j = MIDX.get(tuple(a[b[c]] for c in range(16)))
        if j is None:
            CLOSED = False
            j = IDG
        row.append(j)
    COMP.append(row)
NPROD = NGRP * NGRP

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

STABP = [e for e in range(NGRP) if PERM[e][0] == 0]
STABC = [e for e in range(NGRP) if CPERM[e][0] == 0]
EPP = [e for e in STABP if e != IDG][0]
ECC = [e for e in STABC if e != IDG][0]
SQP = (COMP[EPP][EPP] == IDG)
SQC = (COMP[ECC][ECC] == IDG)

FIXP = [sum(1 for i in range(NPI) if p[i] == i) for p in PERM]
FIXC = [sum(1 for i in range(NCOV) if q[i] == i) for q in CPERM]

# ------------------------------------------------------------------
# 3. the object and the group, re-established from the base
# ------------------------------------------------------------------

PCNSET = sorted(set(PCN))
PCN0 = PCNSET[0]
CUTSZ = SIZES[0]
COVSZ = BRS[0]
LHS = CUTSZ * NS
RHS = PCN0 * NPI

gate(len(SIZES) == 1 and len(PCNSET) == 1 and NS > 0 and 0 < NPI <= NKEPT <= NCAND
     and NPI == len(USED) and NPI == len(POS) and LHS == RHS,
     "C0",
     "cell {0} unit-det, {1} at cost floor {2}, {3} cuttings of {4}, {5} pieces, {6} each, {7}={8}".format(
         nd(NCAND), nd(NKEPT), nd(FLOOR), nd(NS), nd(CUTSZ), nd(NPI), nd(PCN0), nd(LHS), nd(RHS)))

gate(len(BRS) == 1 and COVEXACT and NCOV > 0 and COVSZ * PCN0 == NS,
     "C1",
     "covers {0}, each of {1} pieces, each meets every cutting once, {1} x {2} = {3}".format(
         nd(NCOV), nd(COVSZ), nd(PCN0), nd(NS)))

gate(GDISTINCT and CLOSED and KEEPS and COVKEEP and PBIJ and PDIST and PIDOK and CBIJ
     and CDIST and len(ORBP) == NPI and len(ORBC) == NCOV,
     "C2",
     "group {0} distinct maps shut under composition, {0} bijections each side, one orbit of {1} on each".format(
         nd(NGRP), nd(NPI)))

gate(len(STABP) == 2 and len(STABC) == 2 and SQP and SQC and EPP != IDG and ECC != IDG,
     "C3",
     "both point stabilisers have order 2 and the non-identity element of each squares to the identity")

# ------------------------------------------------------------------
# 4. the action on the piece and cover pairs is free
# ------------------------------------------------------------------

SETP = [e for e in range(NGRP) if e != IDG and FIXP[e] > 0]
SETC = [e for e in range(NGRP) if e != IDG and FIXC[e] > 0]
NFP = len(SETP)
NFC = len(SETC)

gate(NFP == 12 and NFC == 4 and not (set(SETP) & set(SETC)),
     "C4",
     "{0} non-identity maps fix at least one piece, {1} fix at least one cover, the two sets are disjoint".format(
         nd(NFP), nd(NFC)))

FXP = sorted(set(FIXP[e] for e in SETP))
FXC = sorted(set(FIXC[e] for e in SETC))
INVOK = all(COMP[e][e] == IDG for e in SETP + SETC)

gate(len(FXP) == 1 and len(FXC) == 1 and FXP[0] * NFP == NPI and FXC[0] * NFC == NCOV and INVOK,
     "C5",
     "each of the {0} fixes {1} pieces, each of the {2} fixes {3} covers, all {4} are involutions".format(
         nd(NFP), nd(FXP[0]), nd(NFC), nd(FXC[0]), nd(NFP + NFC)))

BOTH = [e for e in range(NGRP) if e != IDG and FIXP[e] > 0 and FIXC[e] > 0]

gate(len(BOTH) == 0,
     "C6",
     "over all {0} non-identity maps none fixes both a piece and a cover".format(nd(NGRP - 1)))

NPAIR = NPI * NCOV
WHICH = [-1] * NPAIR
ORBS = []
for s in range(NPAIR):
    if WHICH[s] >= 0:
        continue
    i0, j0 = divmod(s, NCOV)
    mem = set()
    for e in range(NGRP):
        mem.add(PERM[e][i0] * NCOV + CPERM[e][j0])
    kk = len(ORBS)
    for x in mem:
        WHICH[x] = kk
    ORBS.append(sorted(mem))

NORB = len(ORBS)
OSZ = sorted(set(len(o) for o in ORBS))

gate(len(OSZ) == 1 and OSZ[0] == NGRP and NORB * NGRP == NPAIR and min(WHICH) >= 0,
     "C7",
     "the pair action is free: {0} orbits of the full size {1}, {0} x {1} = {2} pairs".format(
         nd(NORB), nd(NGRP), nd(NPAIR)))

# ------------------------------------------------------------------
# 5. every orbit table carries two ones per row and per column
# ------------------------------------------------------------------

ROWSA = []
COLSA = []
REG = True
for o in ORBS:
    rw = [[] for _ in range(NCOV)]
    cl = [[] for _ in range(NPI)]
    for x in o:
        i, j = divmod(x, NCOV)
        rw[j].append(i)
        cl[i].append(j)
    if any(len(z) != 2 for z in rw) or any(len(z) != 2 for z in cl):
        REG = False
    ROWSA.append(rw)
    COLSA.append(cl)

gate(REG,
     "C8",
     "each of the {0} orbit tables carries 2 ones in every one of its {1} rows and 2 in every one of its {2} columns".format(
         nd(NORB), nd(NCOV), nd(NPI)))

PGEN = []
CGEN = []
UNIQG = True
for i in range(NPI):
    c = [e for e in range(NGRP) if e != IDG and PERM[e][i] == i]
    if len(c) != 1:
        UNIQG = False
        c = [IDG]
    PGEN.append(c[0])
for j in range(NCOV):
    c = [e for e in range(NGRP) if e != IDG and CPERM[e][j] == j]
    if len(c) != 1:
        UNIQG = False
        c = [IDG]
    CGEN.append(c[0])

PAIROK = True
for kk in range(NORB):
    rw = ROWSA[kk]
    cl = COLSA[kk]
    for j in range(NCOV):
        a, b = rw[j]
        if a == b or PERM[CGEN[j]][a] != b or PERM[CGEN[j]][b] != a:
            PAIROK = False
    for i in range(NPI):
        a, b = cl[i]
        if a == b or CPERM[PGEN[i]][a] != b or CPERM[PGEN[i]][b] != a:
            PAIROK = False

gate(UNIQG and PAIROK,
     "C9",
     "each point has a unique non-identity fixer; it swaps the two pieces of its row and the two covers of its column")

# ------------------------------------------------------------------
# 6. every cycle has length twice the order of the product
# ------------------------------------------------------------------

ORDG = []
for e in range(NGRP):
    o = 1
    y = e
    while y != IDG and o <= NGRP:
        y = COMP[y][e]
        o += 1
    ORDG.append(o)


def msetstr(vals):
    parts = []
    for v in sorted(set(vals)):
        parts.append("{0}x{1}".format(nd(vals.count(v)), nd(v)))
    return " ".join(parts)


PGD = sorted(set(PGEN))
CGD = sorted(set(CGEN))
PRODO = [ORDG[COMP[a][b]] for a in PGD for b in CGD]

gate(len(PGD) == NFP and len(CGD) == NFC and len(PRODO) == NFP * NFC
     and sorted(set(PRODO)) == [4],
     "C10",
     "{0} piece gens by {1} cover gens is {2} products, order multiset {3}".format(
         nd(len(PGD)), nd(len(CGD)), nd(len(PRODO)), msetstr(PRODO)))

INVS = [e for e in range(NGRP) if e != IDG and COMP[e][e] == IDG]
PRODO2 = [ORDG[COMP[a][b]] for a in PGD for b in INVS]
OD2 = sorted(set(PRODO2))

gate(len(PRODO2) == len(PGD) * len(INVS) and any(v != 4 for v in PRODO2) and 4 in OD2,
     "C11",
     "rejector: {0} gens by all {1} involutions is {2} products of orders {3}, so order 4 is not automatic".format(
         nd(len(PGD)), nd(len(INVS)), nd(len(PRODO2)), " ".join(nd(v) for v in OD2)))

CYCA = []
CYCOK = True
CLENS = set()
CPTS = set()
TOTC = 0
TOTE = 0
for kk in range(NORB):
    rw = ROWSA[kk]
    cl = COLSA[kk]
    vis = set()
    lst = []
    for s in ORBS[kk]:
        if s in vis:
            continue
        i0, j0 = divmod(s, NCOV)
        eds = []
        ci = i0
        cj = j0
        ph = 0
        while True:
            eds.append(ci * NCOV + cj)
            if ph == 0:
                a, b = rw[cj]
                ci = b if a == ci else a
            else:
                a, b = cl[ci]
                cj = b if a == cj else a
            ph = 1 - ph
            if ci == i0 and cj == j0 and ph == 0:
                break
            if len(eds) > 2 * NGRP:
                CYCOK = False
                break
        pcs = [divmod(eds[t], NCOV)[0] for t in range(0, len(eds), 2)]
        cvs = [divmod(eds[t], NCOV)[1] for t in range(0, len(eds), 2)]
        if len(set(eds)) != len(eds) or 2 * len(set(pcs)) != len(eds) or 2 * len(set(cvs)) != len(eds):
            CYCOK = False
        for x in eds:
            vis.add(x)
        CLENS.add(len(eds))
        TOTE += len(eds)
        lst.append((pcs, cvs))
    CPTS.add(len(lst))
    TOTC += len(lst)
    CYCA.append(lst)

CPT = sorted(CPTS)[0]
CL = sorted(CLENS)[0]

gate(CYCOK and CLENS == set([8]) and len(CPTS) == 1 and CPT * CL == NGRP
     and TOTC == NORB * CPT and TOTE == NPAIR,
     "C12",
     "every component is a cycle of length {0}: {1} per table, {2} x {1} = {3} cycles in all".format(
         nd(CL), nd(CPT), nd(NORB), nd(TOTC)))

C13OK = True
for kk in range(NORB):
    for (pcs, cvs) in CYCA[kk]:
        base = min(pcs[t] * NCOV + cvs[t] for t in range(len(pcs)))
        i0, j0 = divmod(base, NCOV)
        if 2 * len(pcs) != 2 * ORDG[COMP[PGEN[i0]][CGEN[j0]]]:
            C13OK = False

gate(C13OK,
     "C13",
     "each of the {0} cycles has length twice the order of the product of the two generators at its base pair".format(
         nd(TOTC)))

# ------------------------------------------------------------------
# 7. rank 144 and nullity 48 in every characteristic
# ------------------------------------------------------------------


def detint(Mi):
    n = len(Mi)
    tot = 0
    for pm in itertools.permutations(range(n)):
        sg = 1
        for a in range(n):
            for b in range(a + 1, n):
                if pm[a] > pm[b]:
                    sg = -sg
        pr = 1
        for a in range(n):
            pr *= Mi[a][pm[a]]
        tot += sg * pr
    return tot


A4 = [[1 if (c == r or c == ((r + 1) & 3)) else 0 for c in range(4)] for r in range(4)]
A3 = [row[0:3] for row in A4[0:3]]
D4 = detint(A4)
D3 = detint(A3)

gate(D4 == 0 and D3 == 1,
     "C14",
     "block det {0} so rank at most 3, leading 3 by 3 minor det {1} so rank at least 3: rank 3 nullity 1 over every field".format(
         nd(D4), nd(D3)))

A4A = np.array(A4, dtype=np.int64)
SUMALL = np.zeros((NCOV, NPI), dtype=np.int64)
BLKOK = True
KEROK = True
DISJ = True
RK1 = []
RK2 = []
for kk in range(NORB):
    Mt = np.zeros((NCOV, NPI), dtype=np.int64)
    for x in ORBS[kk]:
        i, j = divmod(x, NCOV)
        Mt[j, i] = 1
    SUMALL += Mt
    V = np.zeros((NPI, len(CYCA[kk])), dtype=np.int64)
    pmark = np.zeros(NPI, dtype=np.int64)
    cmark = np.zeros(NCOV, dtype=np.int64)
    for t in range(len(CYCA[kk])):
        pcs, cvs = CYCA[kk][t]
        ia = np.array(pcs, dtype=np.int64)
        ja = np.array(cvs, dtype=np.int64)
        if not np.array_equal(Mt[ja][:, ia], A4A):
            BLKOK = False
        if int(Mt[ja].sum()) != CL or int(Mt[:, ia].sum()) != CL:
            BLKOK = False
        for u in range(len(pcs)):
            V[pcs[u], t] = 1 if (u & 1) == 0 else -1
        pmark[ia] += 1
        cmark[ja] += 1
    if not (Mt.dot(V) == 0).all():
        KEROK = False
    if not ((pmark == 1).all() and (cmark == 1).all()):
        DISJ = False
    RK1.append(rank_modp(Mt, PRIME))
    RK2.append(rank_modp(Mt, PRIME2))
    Mt = None
    V = None

gate(BLKOK,
     "C15",
     "on each cycle the 4 by 4 submatrix is that block exactly, and its rows and columns carry no ones outside it")

RANKDER = CPT * 3
NULLDER = CPT * 1

gate(RANKDER + NULLDER == NPI and RANKDER == 3 * NULLDER and NULLDER == CPT,
     "C16",
     "{0} blocks of rank 3 give rank {1} and nullity {2} = {3} - {1} for all {4} tables, no large elimination".format(
         nd(CPT), nd(RANKDER), nd(NULLDER), nd(NPI), nd(NORB)))

gate(KEROK and DISJ,
     "C17",
     "the alternating vector on each of the {0} cycles is annihilated exactly; the {1} per table have disjoint supports".format(
         nd(TOTC), nd(CPT)))

gate(all(v == RANKDER for v in RK1) and all(v == RANKDER for v in RK2)
     and len(RK1) + len(RK2) == 2 * NORB,
     "C18",
     "real elimination gives rank {0} for all {1} tables at both primes, {2} measurements".format(
         nd(RANKDER), nd(NORB), nd(2 * NORB)))

M0 = np.zeros((NCOV, NPI), dtype=np.int64)
for x in ORBS[0]:
    i, j = divmod(x, NCOV)
    M0[j, i] = 1
R0 = rank_modp(M0, PRIME)
SRC = int(np.nonzero(M0[0])[0][0])
DST = int(np.nonzero(M0[0] == 0)[0][0])
M0[0, SRC] = 0
M0[0, DST] = 1
BAD = (not (M0.sum(axis=0) == 2).all()) or (not (M0.sum(axis=1) == 2).all())
RP = rank_modp(M0, PRIME)
M0 = None

gate(R0 == RANKDER and BAD and RP != RANKDER,
     "C19",
     "rejector: moving one entry along a row breaks two-regularity and the rank moves from {0} to {1}".format(
         nd(R0), nd(RP)))

# ------------------------------------------------------------------
# 8. the sum of the orbit tables and the cover by piece incidence
# ------------------------------------------------------------------

gate(bool((SUMALL == 1).all()),
     "C20",
     "the {0} orbit tables sum entrywise to the all ones {1} by {2} matrix".format(
         nd(NORB), nd(NCOV), nd(NPI)))

INC = np.zeros((NCOV, NPI), dtype=np.int64)
for j in range(NCOV):
    for i in COVSET[j]:
        INC[j, i] = 1
IORB = sorted(set(WHICH[i * NCOV + j] for j in range(NCOV) for i in COVSET[j]))
SUM4 = np.zeros((NCOV, NPI), dtype=np.int64)
for kk in IORB:
    for x in ORBS[kk]:
        i, j = divmod(x, NCOV)
        SUM4[j, i] += 1

gate(len(IORB) == 4 and np.array_equal(SUM4, INC),
     "C21",
     "the cover by piece incidence is exactly the entrywise sum of {0} of the {1} orbit tables".format(
         nd(len(IORB)), nd(NORB)))

IR1 = rank_modp(INC, PRIME)
IR2 = rank_modp(INC, PRIME2)

gate(IR1 == 105 and IR2 == 105 and NPI - IR1 == 87 and RANKDER - IR1 == 39,
     "C22",
     "incidence rank {0} at both primes, kernel {1} = {2} - {0}, excess {3} = {4} - {0}".format(
         nd(IR1), nd(NPI - IR1), nd(NPI), nd(RANKDER - IR1), nd(RANKDER)))

TT = []
FR1 = []
for kk in IORB:
    Mt = np.zeros((NCOV, NPI), dtype=np.int64)
    for x in ORBS[kk]:
        i, j = divmod(x, NCOV)
        Mt[j, i] = 1
    TT.append(Mt)
    FR1.append(rank_modp(Mt, PRIME))
PS = []
for a in range(len(TT)):
    for b in range(a + 1, len(TT)):
        PS.append(rank_modp(TT[a] + TT[b], PRIME))
PS = sorted(PS)
TT = None

gate(all(v == RANKDER for v in FR1) and len(FR1) == len(IORB) and len(PS) == 6,
     "C23",
     "each of the {0} summands alone has rank {1}; the {2} two-element sums measure {3}".format(
         nd(len(IORB)), nd(RANKDER), nd(len(PS)), " ".join(nd(v) for v in PS)))

emit("group {0}, orbits {1}, cycles {2}, every orbit table rank {3}, incidence rank {4}".format(
    nd(NGRP), nd(NORB), nd(TOTC), nd(RANKDER), nd(IR1)))
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
MBS = RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RSS / 1024.0
emit("elapsed {0} s, peak resident {1} MB".format(
    nd("{0:.1f}".format(time.time() - T0)), nd("{0:.1f}".format(MBS))))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
sys.exit(0 if STAT[1] == 0 else 1)
