"""The 96 orbit tables of the physical cell cutting carry exactly two kernels.

Standalone exact runner. It rebuilds the unit four-cube cell object from scratch:
the sixteen corners, the five-corner unit-determinant pieces at the adjacency cost
floor, the cuttings by them, the 192 pieces that occur, and the 192 eight-piece
covers. The group of 384 signed coordinate maps is built by permuting the four
coordinates and flipping any of them; it acts freely on the 36864 pairs made of one
piece and one cover, giving 96 orbits of size 384, each read as a zero and one table
over covers by pieces.

The finite question is what those 96 tables have in common. Each table splits into 48
cycles of length eight whose alternating vectors span its kernel. Reducing the 96
kernels to canonical form leaves exactly two subspaces of dimension 48, so the 96
tables carry a two-valued colour. The two kernels span 84 and meet in the 12
dimensional sign-anti-invariant space of the sixteen pure flips, which every table
kills. Over the primary field each kernel is a submodule for the whole group, so
stacking all 48 tables of one colour keeps rank 144 while every cross-colour stack
jumps to 180.

The colour then gets a closed form: each cover has a unique non-identity fixer, a
single flip naming one axis; each piece names the two axes whose corner counts are
nearest to balanced; and the colour of an orbit says whether the cover axis lies in
the piece pair. The two colour sums are constant on a 4 by 6 grid of blocks and have
rank 4. The cover incidence table is the entrywise sum of four orbits, three of one
colour and one of the other, and its rank is 105.

Integer identities are checked directly. Modular row-space and rank claims use the
primary field of order 1000003; the field of order 1000033 is a replication control
for the explicitly named gates. No floating point enters any gate and no constant is
fitted. Reverted in-memory mutations exercise every load-bearing check family.

Output: one line per gate, two summary lines, then the total line."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

PRIME = 1000003
PRIME2 = 1000033
AUDIT_TIMEOUT_SEC = 300

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

# The generic sample makes the cover search exhaustive inside the declared candidate
# class.  This independent exact certificate establishes that every selected cover is
# a genuine cutting.  Every co-occurring pair of full-dimensional simplices is weakly
# separated by an integer normal in {-1,0,1}^4, hence their strict interiors are
# disjoint.  Each of the 24 simplices has normalized volume one and is contained in the
# cube, so their normalized volumes sum to the cube's normalized volume 24.
CO_PAIRS = sorted(set(pair for cutting in CUT
                      for pair in itertools.combinations(cutting, 2)))
SEP_NORMALS = np.array(
    [a for a in itertools.product((-1, 0, 1), repeat=4) if any(a)],
    dtype=np.int64,
)
SEP_DOTS = np.dot(np.array(CORN, dtype=np.int64), SEP_NORMALS.T)
PIECE_VERTICES = np.array([KEPT[USED[i]] for i in range(NPI)], dtype=np.int64)
SEP_LO = SEP_DOTS[PIECE_VERTICES].min(axis=1)
SEP_HI = SEP_DOTS[PIECE_VERTICES].max(axis=1)


def vertex_sets_separated(a, b):
    """Whether one of the 80 exact integer normals weakly separates two simplices."""
    av = SEP_DOTS[np.array(a, dtype=np.int64)]
    bv = SEP_DOTS[np.array(b, dtype=np.int64)]
    return bool(np.any((av.max(axis=0) <= bv.min(axis=0))
                       | (bv.max(axis=0) <= av.min(axis=0))))


PAIR_SEPARATED = all(
    bool(np.any((SEP_HI[i] <= SEP_LO[j]) | (SEP_HI[j] <= SEP_LO[i])))
    for i, j in CO_PAIRS
)
VOLUME_CLOSED = (SIZES == [24] and all(abs(det4(
    [[CORN[KEPT[USED[i]][j + 1]][r] - CORN[KEPT[USED[i]][0]][r]
      for j in range(4)] for r in range(4)])) == 1 for i in range(NPI)))

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
# 3. the pair action, its orbits, and the kernel of each orbit table
# ------------------------------------------------------------------

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
FSTAB = set()
for o in ORBS:
    i0, j0 = divmod(o[0], NCOV)
    FSTAB.add(sum(1 for e in range(NGRP)
                  if PERM[e][i0] == i0 and CPERM[e][j0] == j0))

TAB = []
for o in ORBS:
    M = np.zeros((NCOV, NPI), dtype=np.int64)
    for x in o:
        i, j = divmod(x, NCOV)
        M[j, i] = 1
    TAB.append(M)

TRS = set()
TCS = set()
for M in TAB:
    TRS.update(int(v) for v in M.sum(axis=1))
    TCS.update(int(v) for v in M.sum(axis=0))


def cycles_of(k):
    """Walk the bipartite graph of orbit table k. Return the cycle lengths and,
    for each cycle, the vector that is plus and minus one alternately on the
    pieces the cycle visits and zero elsewhere."""
    M = TAB[k]
    rw = [list(np.nonzero(M[j])[0]) for j in range(NCOV)]
    cl = [list(np.nonzero(M[:, i])[0]) for i in range(NPI)]
    seen = set()
    lens = []
    vecs = []
    for x in ORBS[k]:
        if x in seen:
            continue
        i0, j0 = divmod(x, NCOV)
        ed = []
        ci = i0
        cj = j0
        ph = 0
        while True:
            ed.append(ci * NCOV + cj)
            if ph == 0:
                a, b = rw[cj]
                ci = int(b) if int(a) == ci else int(a)
            else:
                a, b = cl[ci]
                cj = int(b) if int(a) == cj else int(a)
            ph = 1 - ph
            if ci == i0 and cj == j0 and ph == 0:
                break
        for y in ed:
            seen.add(y)
        lens.append(len(ed))
        v = np.zeros(NPI, dtype=np.int64)
        u = 0
        for t in range(0, len(ed), 2):
            v[divmod(ed[t], NCOV)[0]] = 1 if (u & 1) == 0 else -1
            u += 1
        vecs.append(v)
    return lens, np.array(vecs, dtype=np.int64)


CY = [cycles_of(k) for k in range(NORB)]
KER = [c[1] for c in CY]
CYLEN = sorted(set(t for c in CY for t in c[0]))
NCYC = sum(len(c[0]) for c in CY)
ANNZ = all(not TAB[k].dot(KER[k].T).any() for k in range(NORB))
SUPP = all(bool((np.abs(KER[k]).sum(axis=0) <= 1).all())
           and int(np.abs(KER[k]).sum()) == KER[k].shape[0] * 4
           for k in range(NORB))


def rref_modp(M, p):
    """Row reduced echelon form of M over the field with p elements, done as one
    vectorised update of every nonzero row per pivot. Returns the reduced rows
    and the pivot columns."""
    A = np.mod(np.array(M, dtype=np.int64), p)
    nr, nc = A.shape
    r = 0
    piv = []
    for c in range(nc):
        if r >= nr:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            tmp = A[r].copy()
            A[r] = A[pr]
            A[pr] = tmp
        A[r] = np.mod(A[r] * pow(int(A[r, c]), p - 2, p), p)
        col = A[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            A[nzr] = np.mod(A[nzr] - np.outer(col[nzr], A[r]), p)
        piv.append(c)
        r += 1
    return A[:r], piv


def rrank(M, p):
    return rref_modp(M, p)[0].shape[0]


def in_span(R, piv, v, p):
    """Is v in the row space of the reduced form R with pivot columns piv."""
    w = np.mod(np.array(v, dtype=np.int64), p)
    return not np.mod(w - np.dot(w[list(piv)], R), p).any()


RK1 = [rref_modp(KER[k], PRIME) for k in range(NORB)]
RK2 = [rref_modp(KER[k], PRIME2) for k in range(NORB)]
LAB1 = {}
LAB2 = {}
KCLS = []
KCL2 = []
for k in range(NORB):
    KCLS.append(LAB1.setdefault(RK1[k][0].tobytes(), len(LAB1)))
    KCL2.append(LAB2.setdefault(RK2[k][0].tobytes(), len(LAB2)))
KDIM = sorted(set(RK1[k][0].shape[0] for k in range(NORB)))
KDIM2 = sorted(set(RK2[k][0].shape[0] for k in range(NORB)))
CSZ = sorted(KCLS.count(v) for v in sorted(set(KCLS)))
SAMESPLIT = (KCLS == KCL2 or KCLS == [1 - v for v in KCL2])
I0 = KCLS.index(0)
I1 = KCLS.index(1)
IX0 = [k for k in range(NORB) if KCLS[k] == 0]
IX1 = [k for k in range(NORB) if KCLS[k] == 1]

# ------------------------------------------------------------------
# 4. the flips, the two labels, and the two colour sums
# ------------------------------------------------------------------

AXM = []
for m in MAPS:
    b0 = m[0]
    AXM.append(tuple((b0 ^ m[1 << a]).bit_length() - 1 for a in range(4)))
AXOK = all(sorted(r) == [0, 1, 2, 3] for r in AXM)

FLP = [e for e in range(NGRP) if AXM[e] == (0, 1, 2, 3)]
EPS = [1 if (bin(DESC[e][1]).count("1") & 1) == 0 else -1 for e in FLP]
FLPFREE = all(sum(1 for i in range(NPI) if PERM[e][i] == i) == 0
              for e in FLP if e != IDG)
REPF = []
seenf = set()
for i in range(NPI):
    if i in seenf:
        continue
    for e in FLP:
        seenf.add(PERM[e][i])
    REPF.append(i)
SV = []
TV = []
for i in REPF:
    a = np.zeros(NPI, dtype=np.int64)
    b = np.zeros(NPI, dtype=np.int64)
    for u, e in enumerate(FLP):
        a[PERM[e][i]] = EPS[u]
        b[PERM[e][i]] = 1
    SV.append(a)
    TV.append(b)
SV = np.array(SV, dtype=np.int64)
TV = np.array(TV, dtype=np.int64)
SANTI = all(np.array_equal(SV[:, list(PERM[e])], EPS[u] * SV)
            for u, e in enumerate(FLP))
TINV = all(np.array_equal(TV[:, list(PERM[e])], TV) for e in FLP)

CAX = []
CFIX = set()
CPURE = True
for j in range(NCOV):
    st = [e for e in range(NGRP) if e != IDG and CPERM[e][j] == j]
    CFIX.add(len(st))
    if len(st) != 1:
        CAX.append(0)
        CPURE = False
        continue
    e = st[0]
    if AXM[e] != (0, 1, 2, 3) or bin(DESC[e][1]).count("1") != 1:
        CPURE = False
    CAX.append(DESC[e][1].bit_length() - 1)

PPR = []
PNAX = set()
for i in range(NPI):
    S = KEPT[USED[i]]
    ks = [sum(1 for c in S if (c >> a) & 1) for a in range(4)]
    pr = [min(k, 5 - k) for k in ks]
    mx = max(pr)
    t = tuple(a for a in range(4) if pr[a] == mx)
    PNAX.add(len(t))
    PPR.append(t)

A = sum(TAB[k] for k in IX0)
B = sum(TAB[k] for k in IX1)
CTRL = sum(TAB[k] for k in range(48))

# ------------------------------------------------------------------
# 5. the gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and PCSET == [1975] and GENERIC
     and SIZES[0] * NS == NPI * PCSET[0], "C0",
     "cell {0} unit-det pieces, {1} at cost floor {2}, {3} cuttings of {4}, {5} pieces used, {6} cuttings each, {7} = {8}".format(
         nd(NCAND), nd(NKEPT), nd(FLOOR), nd(NS), nd(SIZES[0]), nd(NPI),
         nd(PCSET[0]), nd(SIZES[0] * NS), nd(NPI * PCSET[0])))

gate(len(CO_PAIRS) == 15168 and len(SEP_NORMALS) == 80 and PAIR_SEPARATED
     and VOLUME_CLOSED, "C0X",
     "exact geometry: {0} co-pairs separated by {1} integer normals; each cutting has normalized volume {2}".format(
         nd(len(CO_PAIRS)), nd(len(SEP_NORMALS)), nd(SIZES[0])))

gate(NCOV == 192 and BRS == [8] and COVEXACT and BRS[0] * PCSET[0] == NS
     and len(set(CS)) == NCOV, "C1",
     "covers {0}, each of {1} pieces, each meeting every cutting exactly once, {1} x {2} = {3}".format(
         nd(NCOV), nd(BRS[0]), nd(PCSET[0]), nd(BRS[0] * PCSET[0])))

gate(GDISTINCT and CLOSED and PBIJ and PDIST and PIDOK and CBIJ and CDIST
     and len(ORBP) == NPI and len(ORBC) == NCOV and FSTAB == set([1])
     and NORB == 96 and OSZ == [NGRP] and NORB * NGRP == NPAIR, "C2",
     "maps {0} distinct and shut, {0} piece and cover bijections, one orbit of {1} each, free: {2} x {0} = {3}".format(
         nd(NGRP), nd(NPI), nd(NORB), nd(NPAIR)))

gate(TRS == set([2]) and TCS == set([2]) and CYLEN == [8] and NCYC == 4608
     and ANNZ and SUPP, "C3",
     "every table {0}-regular, {1} cycles all of length {2}, the alternating vectors die over Z, supports disjoint".format(
         nd(2), nd(NCYC), nd(CYLEN[0])))

gate(len(LAB1) == 2 and len(LAB2) == 2 and KDIM == [48] and KDIM2 == [48]
     and CSZ == [48, 48] and SAMESPLIT, "C4",
     "canonical kernels give {0} subspaces of dim {1}, class sizes {2} and {3}, same split at {4} and {5}".format(
         nd(len(LAB1)), nd(KDIM[0]), nd(CSZ[0]), nd(CSZ[1]), nd(PRIME), nd(PRIME2)))

TDIST = (len(set(TAB[k].tobytes() for k in range(NORB))) == NORB)
SIGS = set(RK1[k][0].tobytes() for k in range(NORB))
NEWS = 0
KEEPD = 0
NTRY = 20
for t in range(1, NTRY + 1):
    Kx = KER[I0].copy()
    tmp = Kx[:, 0].copy()
    Kx[:, 0] = Kx[:, t]
    Kx[:, t] = tmp
    Rx = rref_modp(Kx, PRIME)[0]
    if Rx.shape[0] == KDIM[0]:
        KEEPD += 1
    if Rx.tobytes() not in SIGS:
        NEWS += 1
gate(TDIST and KEEPD == NTRY and NEWS == NTRY, "C5",
     "rejector: the {0} tables are pairwise distinct, and {1} piece-swapped kernels keep dim {2} yet match neither class".format(
         nd(NORB), nd(NEWS), nd(KDIM[0])))

JN = [rrank(np.vstack([KER[I0], KER[I1]]), q) for q in (PRIME, PRIME2)]
MT = KDIM[0] + KDIM[0] - JN[0]
gate(JN == [84, 84] and MT == 12, "C6",
     "the two kernels span {0} at both primes, so they meet in {1} + {1} - {0} = {2}".format(
         nd(JN[0]), nd(KDIM[0]), nd(MT)))

SVR = rrank(SV, PRIME)
SIN = all(rrank(np.vstack([KER[k], SV]), PRIME) == KDIM[0] for k in range(NORB))
SKILL = all(not TAB[k].dot(SV.T).any() for k in range(NORB))
gate(len(FLP) == 16 and FLPFREE and len(REPF) == 12 and SANTI and SVR == 12
     and SIN and SKILL, "C7",
     "{0} flips act freely with {1} piece orbits; primary-field sign rank {2}, inside every kernel; killed over Z by all {3}".format(
         nd(len(FLP)), nd(len(REPF)), nd(SVR), nd(NORB)))

TVR = rrank(TV, PRIME)
TMEET = set(rrank(np.vstack([KER[k], TV]), PRIME) - KDIM[0] for k in range(NORB))
TALIVE = sum(1 for k in range(NORB) if TAB[k].dot(TV.T).any())
gate(TINV and TVR == 12 and TMEET == set([12]) and TALIVE == NORB, "C8",
     "rejector: the invariant space also has rank {0} but meets every kernel in {1}, and all {2} tables leave it alive".format(
         nd(TVR), nd(0), nd(TALIVE)))


def shut_of(gens):
    have = set([IDG])
    fr = [IDG]
    while fr:
        x = fr.pop()
        for q in gens:
            y = COMP[q][x]
            if y not in have:
                have.add(y)
                fr.append(y)
    return have


GENS = []
CUR = set([IDG])
for e in range(NGRP):
    if e in CUR:
        continue
    GENS.append(e)
    CUR = shut_of(GENS)
    if len(CUR) == NGRP:
        break
NGEN = len(GENS)
SOUT = 0
SCHK = 0
for kk in (I0, I1):
    RR, PV = RK1[kk]
    for g in GENS:
        pg = list(PERM[g])
        for v in KER[kk]:
            SCHK += 1
            if not in_span(RR, PV, v[pg], PRIME):
                SOUT += 1
gate(len(CUR) == NGRP and NGEN == 7 and SCHK == 672 and SOUT == 0, "C9",
     "{0} maps generate all {1}; at the primary prime {2} images of {3} kernel vectors stay inside, {4} outside".format(
         nd(NGEN), nd(NGRP), nd(SCHK), nd(2 * KDIM[0]), nd(SOUT)))

KDROP = KER[I0][1:]
RD, PD = rref_modp(KDROP, PRIME)
ESC = 0
ECHK = 0
for g in GENS:
    pg = list(PERM[g])
    for v in KDROP:
        ECHK += 1
        if not in_span(RD, PD, v[pg], PRIME):
            ESC += 1
gate(RD.shape[0] == 47 and ECHK == 329 and ESC == 5, "C10",
     "rejector: dropping one basis vector leaves rank {0}, and {1} of its {2} generator images fall outside".format(
         nd(RD.shape[0]), nd(ESC), nd(ECHK)))

S0 = np.vstack([TAB[k] for k in IX0])
S1 = np.vstack([TAB[k] for k in IX1])
ST0 = rrank(S0, PRIME)
ST1 = rrank(S1, PRIME)
SING = sorted(set(rrank(TAB[k], PRIME) for k in range(NORB)))
gate(S0.shape[0] == 9216 and ST0 == 144 and ST1 == 144 and SING == [144], "C11",
     "at the primary prime, either colour stacks to {0} rows of rank {1}, equal to all {2} single-table ranks".format(
         nd(S0.shape[0]), nd(ST0), nd(NORB)))

XR = set()
NX = 0
for a in IX0:
    for b in IX1:
        NX += 1
        XR.add(rrank(np.vstack([TAB[a], TAB[b]]), PRIME))
SR = set()
NSP = 0
for IXC in (IX0, IX1):
    for u in range(len(IXC)):
        for w in range(u + 1, len(IXC)):
            NSP += 1
            SR.add(rrank(np.vstack([TAB[IXC[u]], TAB[IXC[w]]]), PRIME))
gate(XR == set([180]) and NX == 2304 and NPI - 180 == MT
     and SR == set([144]) and NSP == 2256, "C12",
     "at the primary prime, {0} cross stacks rank {1} = {2} - {3}; {4} same-colour pairs stay at {5}".format(
         nd(NX), nd(180), nd(NPI), nd(MT), nd(NSP), nd(144)))

JALL = np.ones((NCOV, NPI), dtype=np.int64)
CRK = rrank(CTRL, PRIME)
CRC = sorted(set(int(v) for v in CTRL.sum(axis=1))
             | set(int(v) for v in CTRL.sum(axis=0)))
ARC = sorted(set(int(v) for v in A.sum(axis=1)) | set(int(v) for v in A.sum(axis=0))
             | set(int(v) for v in B.sum(axis=1)) | set(int(v) for v in B.sum(axis=0)))
Z01 = bool((A <= 1).all() and (B <= 1).all() and (CTRL <= 1).all())
gate(np.array_equal(A + B, JALL) and Z01 and ARC == [96] and CRC == [96]
     and CRK == 133, "C13",
     "A + B all ones, all row and column sums {0}; the index-order split shares that yet has rank {1}, so regularity alone gives nothing".format(
         nd(ARC[0]), nd(CRK)))

PA = [list(PERM[e]) for e in range(NGRP)]
QA = [list(CPERM[e]) for e in range(NGRP)]
COVB = sum(1 for e in range(NGRP)
           if not np.array_equal(A[QA[e]][:, PA[e]], A)
           or not np.array_equal(B[QA[e]][:, PA[e]], B))
ASW = A.copy()
tmp = ASW[:, 0].copy()
ASW[:, 0] = ASW[:, 1]
ASW[:, 1] = tmp
CBAD = sum(1 for e in range(NGRP) if not np.array_equal(ASW[QA[e]][:, PA[e]], ASW))
gate(COVB == 0 and CBAD == 382, "C14",
     "A and B are covariant on all {0} pairs under all {1} maps; swapping two pieces in A breaks that for {2} of them".format(
         nd(NPAIR), nd(NGRP), nd(CBAD)))

RA = [rrank(A, q) for q in (PRIME, PRIME2)]
RB = [rrank(B, q) for q in (PRIME, PRIME2)]
RAB = [rrank(np.vstack([A, B]), q) for q in (PRIME, PRIME2)]
gate(RA == [4, 4] and RB == [4, 4] and NPI - RA[0] == 188
     and RAB == [4, 4], "C15",
     "rank A = rank B = {0} at both primes, nullity {1}, and A stacked on B still measures {2}".format(
         nd(RA[0]), nd(NPI - RA[0]), nd(RAB[0])))

AK = all(not X.dot(KER[k].T).any() for X in (A, B) for k in (I0, I1))
CMISS = sorted(set(int((CTRL.dot(KER[k].T) != 0).any(axis=0).sum()) for k in (I0, I1)))
gate(AK and CMISS == [48], "C16",
     "A and B kill all {0} kernel basis vectors over Z, while the index-order control fails on all {1} of each class".format(
         nd(2 * KDIM[0]), nd(CMISS[0])))


def blocks_of(X):
    rw = {}
    cl = {}
    for j in range(NCOV):
        rw.setdefault(X[j].tobytes(), []).append(j)
    for i in range(NPI):
        cl.setdefault(X[:, i].tobytes(), []).append(i)
    return rw, cl


RWA, CLA = blocks_of(A)
RWB, CLB = blocks_of(B)
RSZ = sorted(set(len(v) for v in RWA.values()) | set(len(v) for v in RWB.values()))
CSZ2 = sorted(set(len(v) for v in CLA.values()) | set(len(v) for v in CLB.values()))
CONST = True
for X, rw, cl in ((A, RWA, CLA), (B, RWB, CLB)):
    for r in rw.values():
        for c in cl.values():
            blk = X[np.ix_(r, c)]
            if int(blk.min()) != int(blk.max()):
                CONST = False
gate(len(RWA) == 4 and len(RWB) == 4 and len(CLA) == 6 and len(CLB) == 6
     and RSZ == [48] and CSZ2 == [32] and CONST, "C17",
     "A and B each have {0} distinct rows of {1} covers and {2} distinct columns of {3} pieces, constant on all {4} blocks".format(
         nd(len(RWA)), nd(RSZ[0]), nd(len(CLA)), nd(CSZ2[0]), nd(len(RWA) * len(CLA))))


def pattern_of(X, rw, cl):
    rk = sorted(rw.values(), key=lambda z: z[0])
    ck = sorted(cl.values(), key=lambda z: z[0])
    return np.array([[int(X[r[0], c[0]]) for c in ck] for r in rk], dtype=np.int64)


PATA = pattern_of(A, RWA, CLA)
PATB = pattern_of(B, RWB, CLB)
PONE = sorted(set([int(PATA.sum()), int(PATB.sum())]))
PRS = sorted(set(int(v) for v in PATA.sum(axis=1))
             | set(int(v) for v in PATB.sum(axis=1)))
PCM = sorted(set(int(v) for v in PATA.sum(axis=0))
             | set(int(v) for v in PATB.sum(axis=0)))
PRK = sorted(set([rank_modp(PATA, PRIME), rank_modp(PATB, PRIME),
                  rank_modp(PATA, PRIME2), rank_modp(PATB, PRIME2)]))
PATDET = abs(det4(PATA[:, :4].tolist()))
gate(PONE == [12] and PRS == [3] and PCM == [2] and PRK == [4]
     and PATDET == 2
     and np.array_equal(PATA + PATB, np.ones((4, 6), dtype=np.int64)), "C18",
     "each {0} by {1} pattern has {2}/{3} ones, row sums {4}, column sums {5}, exact rank {6} from a determinant-2 minor".format(
         nd(PATA.shape[0]), nd(PATA.shape[1]), nd(PONE[0]),
         nd(PATA.shape[0] * PATA.shape[1]), nd(PRS[0]), nd(PCM[0]), nd(PRK[0])))

BPRES = [e for e in range(NGRP)
         if all(CAX[CPERM[e][j]] == CAX[j] for j in range(NCOV))
         and all(PPR[PERM[e][i]] == PPR[i] for i in range(NPI))]
gate(len(BPRES) == 16 and set(BPRES) == set(FLP), "C19",
     "exactly {0} of the {1} maps hold every row and column block, and they are exactly the {0} pure flips".format(
         nd(len(BPRES)), nd(NGRP)))

CAXP = {}
for j in range(NCOV):
    CAXP.setdefault(CAX[j], []).append(j)
RWSET = set(tuple(v) for v in RWA.values())
gate(CFIX == set([1]) and CPURE and len(CAXP) == 4
     and sorted(len(v) for v in CAXP.values()) == [48, 48, 48, 48]
     and set(tuple(v) for v in CAXP.values()) == RWSET, "C20",
     "each cover has one non-identity fixer, a single flip; its axis takes {0} values of {1} covers, and those are the row blocks".format(
         nd(len(CAXP)), nd(NCOV // len(CAXP))))

PPRP = {}
for i in range(NPI):
    PPRP.setdefault(PPR[i], []).append(i)
CLSET = set(tuple(v) for v in CLA.values())
gate(PNAX == set([2]) and len(PPRP) == 6
     and sorted(len(v) for v in PPRP.values()) == [32] * 6
     and set(tuple(v) for v in PPRP.values()) == CLSET, "C21",
     "min(k, {0} - k) peaks on exactly {1} axes per piece; the pair takes {2} values of {3} pieces, and those are the column blocks".format(
         nd(5), nd(2), nd(len(PPRP)), nd(NPI // len(PPRP))))

GCOL = [-1] * NORB
GOK = True
for j in range(NCOV):
    for i in range(NPI):
        b = 1 if CAX[j] in PPR[i] else 0
        k = WHICH[i * NCOV + j]
        if GCOL[k] < 0:
            GCOL[k] = b
        elif GCOL[k] != b:
            GOK = False
AGREE = sum(1 for j in range(NCOV) for i in range(NPI)
            if GCOL[WHICH[i * NCOV + j]] == KCLS[WHICH[i * NCOV + j]])
GSPL = sorted([GCOL.count(0), GCOL.count(1)])
gate(GOK and GSPL == [48, 48] and (AGREE == 0 or AGREE == NPAIR), "C22",
     "axis-in-pair is constant on all {0} orbits and splits {1}/{2}; it meets the kernel class on {3} of {4} pairs, so equal up to naming".format(
         nd(NORB), nd(GSPL[0]), nd(GSPL[1]), nd(AGREE), nd(NPAIR)))

SHIFTP = [tuple(sorted(((a + 1) & 3) for a in PPR[i])) for i in range(NPI)]
SHIFTC = [((CAX[j] + 1) & 3) for j in range(NCOV)]
D1 = 0
D2 = 0
for j in range(NCOV):
    for i in range(NPI):
        b = GCOL[WHICH[i * NCOV + j]]
        if (1 if CAX[j] in SHIFTP[i] else 0) != b:
            D1 += 1
        if (1 if SHIFTC[j] in PPR[i] else 0) != b:
            D2 += 1
gate(D1 == 24576 and D2 == 24576, "C23",
     "rejector: shifting every piece pair by one axis disagrees on {0} of {1} pairs, and shifting every cover axis on {2}".format(
         nd(D1), nd(NPAIR), nd(D2)))

LB1 = set()
LB2 = set()
for i in range(NPI):
    S = KEPT[USED[i]]
    LB1.add(sum(1 for a in range(5) for b in range(a + 1, 5)
                if bin(S[a] ^ S[b]).count("1") == 1))
    LB2.add(tuple(sorted(bin(DESC[e][1]).count("1")
                         for e in range(NGRP) if e != IDG and PERM[e][i] == i)))
gate(len(LB1) == 1 and len(LB2) == 3, "C24",
     "bounded fibres: the adjacent-corner statistic is constant and fixer weight has {1} fibres; the geometric label has {2}".format(
         nd(len(LB1)), nd(len(LB2)), nd(len(PPRP))))

EF1 = sum(1 for e in range(NGRP) for j in range(NCOV)
          if CAX[CPERM[e][j]] != AXM[e][CAX[j]])
EF2 = sum(1 for e in range(NGRP) for i in range(NPI)
          if PPR[PERM[e][i]] != tuple(sorted(AXM[e][a] for a in PPR[i])))
gate(AXOK and EF1 == 0 and EF2 == 0 and NGRP * NCOV == 73728, "C25",
     "both labels are equivariant for the axis action: {0} failures in {1} cover checks and {0} in {1} piece checks".format(
         nd(EF1), nd(NGRP * NCOV)))

EF3 = sum(1 for e in range(NGRP) for i in range(NPI)
          if SHIFTP[PERM[e][i]] != tuple(sorted(AXM[e][a] for a in SHIFTP[i])))
gate(EF3 == 57344, "C26",
     "rejector: the piece label shifted by one axis fails equivariance on {0} of the same {1} checks".format(
         nd(EF3), nd(NGRP * NPI)))

IC1 = set()
IC2 = set()
for j in range(NCOV):
    IC1.add((len(CS[j]), sum(1 for t in CS[j] if CAX[j] in PPR[t])))
for i in range(NPI):
    cj = [j for j in range(NCOV) if i in COVSET[j]]
    IC2.add((len(cj), sum(1 for j in cj if CAX[j] in PPR[i])))
gate(IC1 == set([(8, 6)]) and IC2 == set([(8, 6)]), "C27",
     "every cover holds {0} pieces of which {1} carry its axis, and every piece lies in {0} covers of which {1} carry the axis".format(
         nd(8), nd(6)))

IORB = sorted(set(WHICH[i * NCOV + j] for j in range(NCOV) for i in CS[j]))
ICOL = sorted(KCLS[k] for k in IORB)
INC = np.array(BROW, dtype=np.int64)
ISUM = sum(TAB[k] for k in IORB)
gate(len(IORB) == 4 and np.array_equal(INC, ISUM)
     and sorted([ICOL.count(0), ICOL.count(1)]) == [1, 3], "C28",
     "the incidence table is the entrywise sum of exactly {0} orbits, {1} of one colour and {2} of the other".format(
         nd(len(IORB)), nd(3), nd(1)))

IST = rrank(np.vstack([TAB[k] for k in IORB]), PRIME)
IR = [rrank(INC, q) for q in (PRIME, PRIME2)]
gate(IST == 180 and IR == [105, 105] and NPI - IR[0] == 87, "C29",
     "at the primary prime their stack ranks {1}; their sum ranks {2} at both primes, and {3} - {2} = {4}".format(
         nd(len(IORB)), nd(IST), nd(IR[0]), nd(NPI), nd(NPI - IR[0])))

PROF = {}
for j in range(NCOV):
    cj = [set(KEPT[USED[t]]) for t in CS[j]]
    for i in range(NPI):
        Si = set(KEPT[USED[i]])
        pf = tuple(sorted(len(Si & c) for c in cj))
        PROF.setdefault(pf, set()).add(GCOL[WHICH[i * NCOV + j]])
BOTH = sum(1 for v in PROF.values() if len(v) == 2)
gate(len(PROF) == 25 and BOTH == 21, "C30",
     "bounded fibres: the shared-corner profile takes {0} values and {1} fibres contain both observed colours".format(
         nd(len(PROF)), nd(BOTH)))

# ------------------------------------------------------------------
# 6. reverted in-memory mutations for each load-bearing family
# ------------------------------------------------------------------

# Geometry: the generic sample misses this exact overlap.  The point is strictly
# interior to both simplices, and the exact separator predicate rejects the pair.
BAD_GEO_A = KDX[(0, 1, 2, 4, 8)]
BAD_GEO_B = KDX[(0, 1, 3, 7, 15)]
BAD_POINT = (FR(4, 11), FR(3, 11), FR(2, 11), FR(1, 11))


def strict_inside(t, point):
    return all(sum(FR(a[k]) * point[k] for k in range(4)) + FR(b) > 0
               for a, b in BARY[t][2])


BAD_SAMPLE_DISJOINT = not (MASK[BAD_GEO_A] & MASK[BAD_GEO_B])
BAD_INTERIOR_OVERLAP = strict_inside(BAD_GEO_A, BAD_POINT) \
    and strict_inside(BAD_GEO_B, BAD_POINT)
GEOMETRY_MUT_REJECT = (PAIR_SEPARATED and BAD_SAMPLE_DISJOINT
                       and BAD_INTERIOR_OVERLAP
                       and not vertex_sets_separated(KEPT[BAD_GEO_A],
                                                     KEPT[BAD_GEO_B]))

# Group/stabilizer: duplicate one image of a copied non-identity stabilizer.
def action_gate(p):
    return (sorted(p) == list(range(NPI)) and p[0] == 0
            and all(p[p[i]] == i for i in range(NPI)))


BAD_ACTION = list(PERM[EPP])
BAD_ACTION[1] = BAD_ACTION[2]
GROUP_MUT_REJECT = action_gate(PERM[EPP]) and not action_gate(BAD_ACTION)

# Cycle/kernel: change one nonzero coordinate of a copied alternating basis.
def kernel_gate(k, basis):
    return (basis.shape == (48, NPI) and not TAB[k].dot(basis.T).any()
            and rrank(basis, PRIME) == 48)


BAD_KERNEL = KER[I0].copy()
BAD_KERNEL[0, int(np.nonzero(BAD_KERNEL[0])[0][0])] += 1
KERNEL_MUT_REJECT = kernel_gate(I0, KER[I0]) and not kernel_gate(I0, BAD_KERNEL)

# Meet/submodule and stack: independently corrupt copied sign and stack data.
BAD_SIGN = SV.copy()
BAD_SIGN[0, int(np.nonzero(BAD_SIGN[0])[0][0])] += 1
MEET_MUT_REJECT = (SKILL and not all(not TAB[k].dot(BAD_SIGN.T).any()
                                     for k in range(NORB)))

GOOD_MODULE_IMAGE = KER[I0][0][list(PERM[GENS[0]])]
BAD_MODULE_IMAGE = GOOD_MODULE_IMAGE.copy()
BAD_MODULE_IMAGE[int(np.nonzero(BAD_MODULE_IMAGE)[0][0])] += 1
MODULE_MUT_REJECT = (in_span(RK1[I0][0], RK1[I0][1], GOOD_MODULE_IMAGE,
                             PRIME)
                     and not in_span(RK1[I0][0], RK1[I0][1],
                                     BAD_MODULE_IMAGE, PRIME))

BAD_STACK = S0.copy()
BAD_STACK[0, 0] = 1 - BAD_STACK[0, 0]
STACK_MUT_REJECT = (not S0.dot(KER[I0].T).any()
                    and bool(BAD_STACK.dot(KER[I0].T).any()))

# Block/axis/pair label: move one copied piece to a shifted pair and rerun the
# class-size, block, and equivariance predicates.
def label_gate(pairs):
    cls = {}
    for i, pair in enumerate(pairs):
        cls.setdefault(pair, []).append(i)
    if len(cls) != 6 or sorted(len(v) for v in cls.values()) != [32] * 6:
        return False
    if set(tuple(v) for v in cls.values()) != CLSET:
        return False
    return all(pairs[PERM[e][i]] == tuple(sorted(AXM[e][a] for a in pairs[i]))
               for e in range(NGRP) for i in range(NPI))


BAD_LABEL = list(PPR)
BAD_LABEL[0] = tuple(sorted(((a + 1) & 3) for a in BAD_LABEL[0]))
LABEL_MUT_REJECT = label_gate(PPR) and not label_gate(BAD_LABEL)

# Incidence/rank family: flip one copied incidence entry and rerun the exact
# orbit-decomposition and regularity predicate used before the modular rank read.
def incidence_gate(X):
    return (np.array_equal(X, ISUM)
            and sorted(set(int(v) for v in X.sum(axis=0))) == [8]
            and sorted(set(int(v) for v in X.sum(axis=1))) == [8])


BAD_INCIDENCE = INC.copy()
BAD_INCIDENCE[0, 0] = 1 - BAD_INCIDENCE[0, 0]
INCIDENCE_MUT_REJECT = (incidence_gate(INC)
                        and not incidence_gate(BAD_INCIDENCE))

gate(GEOMETRY_MUT_REJECT, "M0",
     "geometry mutation: a sample-disjoint pair sharing (4,3,2,1)/11 is rejected by exact separation")
gate(GROUP_MUT_REJECT, "M1",
     "group mutation: a copied stabilizer with one duplicate image fails bijection and involution")
gate(KERNEL_MUT_REJECT, "M2",
     "kernel mutation: one changed copied cycle-vector entry fails integer annihilation")
gate(MEET_MUT_REJECT and MODULE_MUT_REJECT and STACK_MUT_REJECT, "M3",
     "meet, module, and stack mutations: copied sign, image, and table corruptions all fail their predicates")
gate(LABEL_MUT_REJECT, "M4",
     "label mutation: one shifted copied piece label fails block size and equivariance")
gate(INCIDENCE_MUT_REJECT, "M5",
     "incidence mutation: one flipped copied entry fails orbit decomposition and regularity")

emit("two kernels of dim {0} meeting in {1}, join {2}, either colour stack rank {3}, colour sums rank {4}, incidence rank {5}".format(
    nd(KDIM[0]), nd(MT), nd(JN[0]), nd(ST0), nd(RA[0]), nd(IR[0])))
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
MBS = RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RSS / 1024.0
emit("elapsed {0} s, peak resident {1} MB".format(nd(int(time.time() - T0)), nd(int(MBS))))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
sys.exit(0 if STAT[1] == 0 else 1)
