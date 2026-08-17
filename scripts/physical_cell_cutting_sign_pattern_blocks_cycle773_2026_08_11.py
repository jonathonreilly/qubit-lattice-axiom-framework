"""The sign patterns of the sixteen flips split every rank in the cell cutting family.

Standalone exact runner. It rebuilds the unit four-cube cell object from scratch:
the sixteen corners, the five-corner unit-determinant pieces at the adjacency cost
floor, the cuttings by them, the 192 pieces that occur, and the 192 eight-piece
covers. The group of 384 signed coordinate maps is built by permuting the four
coordinates and flipping any of them; it acts freely on the 36864 pairs made of one
piece and one cover, giving 96 orbits of size 384, each read as a zero and one table
over covers by pieces.

The sixteen pure flips form a subgroup that acts freely on the 192 pieces with 12
orbits, so each of the 16 sign patterns of the four axes carries a block of dimension
12, and the 16 blocks fill all 192 piece coordinates. When the kernel of a table is
held by the flips, its rank is the sum of its 16 per-block ranks. This cycle uses that
identity to split every rank in the family: one orbit table splits as 12, 12, 10, 6, 0
by pattern weight, the cover incidence as 9, 9, 6, 6, 0, and the drop of 39 between
them sits entirely in the blocks of weight at most two. The nullity 48 of one table is
recovered without linear algebra from the axis pair that holds each of its 48 cycles.

All work is exact over the integers and two fixed primes; no floating point enters any
gate and no constant is fitted. Three checks are rejectors and three are honest negatives.

Output: one line per gate, one summary line, a resource line, then the total line."""

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

# ------------------------------------------------------------------
# 4. the flips, the two labels, the incidence, and its two parts
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

# the cover incidence, the orbits it is made of, and the split by the two labels
INC = np.array(BROW, dtype=np.int64)
IORB = sorted(set(WHICH[i * NCOV + j] for j in range(NCOV) for i in CS[j]))
ISUM = sum(TAB[k] for k in IORB)
UM = np.zeros((NCOV, NPI), dtype=np.int64)
VM = np.zeros((NCOV, NPI), dtype=np.int64)
for j in range(NCOV):
    for i in CS[j]:
        if CAX[j] in PPR[i]:
            UM[j, i] = 1
        else:
            VM[j, i] = 1

# ------------------------------------------------------------------
# 5. the sixteen sign patterns and their blocks
# ------------------------------------------------------------------

FLIPS = FLP
FW = [DESC[e][1] for e in FLIPS]
NFL = len(FLIPS)
ORBF = [sorted(set(PERM[e][i0] for e in FLIPS)) for i0 in REPF]
WT = [popc(s) for s in range(16)]
CSIZE = [sum(1 for s in range(16) if WT[s] == w) for w in range(5)]
BBC = {}


def blockbasis(s, p):
    """The basis of the block of sign pattern s over the field with p elements:
    one vector per flip orbit of pieces, carrying at the image of the orbit
    representative under the flip f the sign of s at f, which is plus one when
    the overlap of s and f is even and p - 1 when it is odd."""
    key = (s, p)
    if key not in BBC:
        B = np.zeros((len(REPF), NPI), dtype=np.int64)
        for t, i0 in enumerate(REPF):
            for u in range(NFL):
                B[t, PERM[FLIPS[u]][i0]] = 1 if (popc(s & FW[u]) & 1) == 0 else p - 1
        BBC[key] = B
    return BBC[key]


def blockrank(X, s, p):
    """Rank of X restricted to the block of s, as the rank of the product of X
    with the transpose of the block basis."""
    return rrank(np.mod(np.dot(np.mod(X, p), blockbasis(s, p).T), p), p)


def blockvec(X, p):
    return [blockrank(X, s, p) for s in range(16)]


def profile(X, p):
    """Per-block ranks by pattern weight, whether the value is constant inside
    each weight class, and the total recomposed over all sixteen patterns."""
    bv = blockvec(X, p)
    cls = [[bv[s] for s in range(16) if WT[s] == w] for w in range(5)]
    con = all(len(set(c)) == 1 for c in cls)
    pf = [c[0] for c in cls]
    tot = sum(len(cls[w]) * pf[w] for w in range(5))
    return pf, con, tot


def wsum(pf):
    return sum(CSIZE[w] * pf[w] for w in range(5))


def nullbasis(X, p):
    """A basis of the null space of X over the field with p elements."""
    R, piv = rref_modp(X, p)
    ps = set(piv)
    free = [c for c in range(X.shape[1]) if c not in ps]
    B = np.zeros((len(free), X.shape[1]), dtype=np.int64)
    for a, f in enumerate(free):
        B[a, f] = 1
        for r, c in enumerate(piv):
            if R[r, f]:
                B[a, c] = p - int(R[r, f])
    return B


# ------------------------------------------------------------------
# 6. the cycles of a table, their holders, and the axis pair labelling
# ------------------------------------------------------------------

SUPS = []
SIDX = []
for k in range(NORB):
    ss = [frozenset(int(x) for x in np.nonzero(KER[k][t])[0])
          for t in range(KER[k].shape[0])]
    SUPS.append(ss)
    SIDX.append(dict((y, t) for t, y in enumerate(ss)))
CYN = sorted(set(len(ss) for ss in SUPS))
SUPN = sorted(set(len(y) for ss in SUPS for y in ss))

IMG = []
IMGBAD = 0
for k in range(NORB):
    rows = []
    for t in range(len(SUPS[k])):
        r = []
        for u in range(NFL):
            pe = PERM[FLIPS[u]]
            q = SIDX[k].get(frozenset(pe[i] for i in SUPS[k][t]), -1)
            if q < 0:
                IMGBAD += 1
            r.append(q)
        rows.append(r)
    IMG.append(rows)

CLZ = []
NCLS = set()
CLSZS = set()
for k in range(NORB):
    lab = [-1] * len(SUPS[k])
    nc = 0
    for t in range(len(SUPS[k])):
        if lab[t] >= 0:
            continue
        mem = set(IMG[k][t])
        for x in mem:
            lab[x] = nc
        CLSZS.add(len(mem))
        nc += 1
    NCLS.add(nc)
    CLZ.append(lab)

HSZ = set()
HPBAD = 0
STBAD = 0
PMSK = []
for k in range(NORB):
    pm = []
    for t in range(len(SUPS[k])):
        hold = [u for u in range(NFL) if IMG[k][t][u] == t]
        HSZ.add(len(hold))
        msk = 0
        for u in hold:
            msk |= FW[u]
        sub = set(w for w in range(16) if (w & msk) == w)
        if popc(msk) != 2 or set(FW[u] for u in hold) != sub:
            HPBAD += 1
        i0 = min(SUPS[k][t])
        ims = set(PERM[FLIPS[u]][i0] for u in hold)
        if ims != set(SUPS[k][t]) or len(ims) != len(hold):
            STBAD += 1
        pm.append(msk)
    PMSK.append(pm)

CLPBAD = 0
CLPM = []
FIB = set()
NPRS = set()
for k in range(NORB):
    d = {}
    for t in range(len(SUPS[k])):
        d.setdefault(CLZ[k][t], set()).add(PMSK[k][t])
    pmk = []
    cnt = {}
    for c in sorted(d):
        if len(d[c]) != 1:
            CLPBAD += 1
        v = sorted(d[c])[0]
        pmk.append(v)
        cnt[v] = cnt.get(v, 0) + 1
    CLPM.append(pmk)
    FIB.update(cnt.values())
    NPRS.add(len(cnt))

K0 = 0
EQF = 0
NEQ = 0
for e in range(NGRP):
    for t in range(len(SUPS[K0])):
        NEQ += 1
        q = SIDX[K0].get(frozenset(PERM[e][i] for i in SUPS[K0][t]), -1)
        if q < 0:
            EQF += 1
            continue
        im = 0
        for a in range(4):
            if (PMSK[K0][t] >> a) & 1:
                im |= (1 << AXM[e][a])
        if PMSK[K0][q] != im:
            EQF += 1

PIMG = set(tuple(sorted((AXM[e][0], AXM[e][1]))) for e in range(NGRP))

# closed form and the rejector rule, per table and per sign pattern
CFV = []
RJV = []
for k in range(NORB):
    CFV.append([sum(1 for m in CLPM[k] if (m & s) == m) for s in range(16)])
    RJV.append([sum(1 for m in CLPM[k] if (m & s) != 0) for s in range(16)])


def byweight(v):
    cls = [[v[s] for s in range(16) if WT[s] == w] for w in range(5)]
    return [c[0] for c in cls], all(len(set(c)) == 1 for c in cls)


# ------------------------------------------------------------------
# 7. the gates
# ------------------------------------------------------------------

NSLOT = NS * SIZES[0]
NSLOT2 = NPI * PCSET[0]
gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and PCSET == [1975] and GENERIC
     and NSLOT == 379200 and NSLOT2 == 379200, "D0",
     "the cell has {0} unit-determinant subsets, {1} at cost floor {2}, {3} cuttings of {4}, {5} pieces in {6} each, {7} slots both ways".format(
         nd(NCAND), nd(NKEPT), nd(FLOOR), nd(NS), nd(SIZES[0]), nd(NPI),
         nd(PCSET[0]), nd(NSLOT)))

gate(NCOV == 192 and BRS == [8] and COVEXACT
     and BRS[0] * PCSET[0] == NS, "D1",
     "the {0} covers hold {1} pieces each and meet every cutting exactly once, and {1} times {2} is the cutting count {3}".format(
         nd(NCOV), nd(BRS[0]), nd(PCSET[0]), nd(NS)))

gate(NGRP == 384 and GDISTINCT and CLOSED and KEEPS and COVKEEP and PBIJ and PDIST
     and PIDOK and CBIJ and CDIST and len(ORBP) == NPI and len(ORBC) == NCOV
     and NPAIR == 36864 and FSTAB == set([1]) and NORB == 96 and OSZ == [384], "D2",
     "the {0} maps close under composition, act transitively on pieces and covers, and freely on the {1} pairs: {2} orbits of {0}".format(
         nd(NGRP), nd(NPAIR), nd(NORB)))

FSUB = all(COMP[a][b] in FLIPS for a in FLIPS for b in FLIPS)
BDIM = sorted(set(rrank(blockbasis(s, q), q)
                  for s in range(16) for q in (PRIME, PRIME2)))
BSTK = [rrank(np.vstack([blockbasis(s, q) for s in range(16)]), q)
        for q in (PRIME, PRIME2)]
gate(NFL == 16 and FSUB and FLPFREE and AXOK and len(REPF) == 12
     and sorted(set(len(o) for o in ORBF)) == [16] and BDIM == [12]
     and BSTK == [192, 192], "D3",
     "the {0} flips form a subgroup free on the {1} pieces with {2} orbits; each block has dimension {2}, and all {0} stack to {1}, both primes".format(
         nd(NFL), nd(NPI), nd(len(REPF))))

STK = np.vstack([blockbasis(s, PRIME) for s in range(16)])
COVC = int((STK != 0).any(axis=0).sum())
SGC = sorted(set(int((blockbasis(s, PRIME) != 0).any(axis=0).sum())
                 for s in range(16)))
IDT = np.array_equal(blockbasis(0, PRIME), np.mod(TV, PRIME))
IDS = np.array_equal(blockbasis(15, PRIME), np.mod(SV, PRIME))
gate(16 * len(REPF) == NPI and COVC == NPI and SGC == [NPI] and IDT and IDS
     and TINV and SANTI, "D4",
     "{0} blocks times {1} is {2}, the piece count; each block is nonzero in every coordinate; weight {3} is the invariant and weight {4} the sign space".format(
         nd(16), nd(len(REPF)), nd(NPI), nd(0), nd(4)))

SLR = [i for o in ORBF for i in o[:4]]
SLICE = np.zeros((len(SLR), NPI), dtype=np.int64)
for a, i in enumerate(SLR):
    SLICE[a, i] = 1
SPF, SCON, STOT = profile(SLICE, PRIME)
SRK = rrank(SLICE, PRIME)
gate(SPF == [12, 12, 12, 12, 12] and SCON and STOT == 192 and SRK == 48
     and STOT != SRK, "D5",
     "rejector: a {0} row coordinate slice has per-block rank {1} in every block and is constant by weight, yet recomposes to {2}, not its rank {3}".format(
         nd(len(SLR)), nd(SPF[0]), nd(STOT), nd(SRK)))

HOLD0 = all(np.array_equal(INC[list(CPERM[e])][:, list(PERM[e])], INC)
            for e in FLIPS)
MSW = INC.copy()
c0 = REPF[0]
c1 = REPF[1]
MSW[:, [c0, c1]] = MSW[:, [c1, c0]]
HBRK = sum(1 for e in FLIPS
           if not np.array_equal(MSW[list(CPERM[e])][:, list(PERM[e])], MSW))
SWP, SWC, SWT = profile(MSW, PRIME)
SWR = rrank(MSW, PRIME)
gate(HOLD0 and HBRK > 0 and SWR == 105 and SWT != 105, "D6",
     "rejector: swapping two pieces of the incidence breaks the hold of {0} of the {1} flips; the rank is still {2} but the total recomposes to {3}".format(
         nd(HBRK), nd(NFL), nd(SWR), nd(SWT)))

gate(TRS == set([2]) and TCS == set([2]) and CYLEN == [8] and CYN == [48]
     and SUPN == [4] and NCYC == NORB * 48 and ANNZ and SUPP and IMGBAD == 0
     and NCLS == set([12]) and CLSZS == set([4]), "D7",
     "each table is {0} regular with {1} cycles of length {2} on {3} pieces each, and the flips give {4} classes of {5} cycles, on all {6} tables".format(
         nd(2), nd(CYN[0]), nd(CYLEN[0]), nd(SUPN[0]), nd(sorted(NCLS)[0]),
         nd(sorted(CLSZS)[0]), nd(NORB)))

gate(HSZ == set([4]) and HPBAD == 0 and STBAD == 0 and CLPBAD == 0
     and EQF == 0 and NEQ == 18432, "D8",
     "each cycle is held by {0} flips, those of an axis pair, simply transitive on its {0} pieces; the pair label survives {1} maps, {2} of {3} fail".format(
         nd(sorted(HSZ)[0]), nd(NGRP), nd(EQF), nd(NEQ)))

gate(len(PIMG) == 6 and NPRS == set([6]) and FIB == set([2])
     and sorted(NCLS)[0] // len(PIMG) == 2, "D9",
     "the axis maps reach all {0} pairs from one, so each pair takes {1} of {2} classes; every measured fibre is {3}, on all {4} tables".format(
         nd(len(PIMG)), nd(sorted(NCLS)[0] // len(PIMG)), nd(sorted(NCLS)[0]),
         nd(sorted(FIB)[0]), nd(NORB)))

BV = [blockvec(TAB[k], PRIME) for k in range(NORB)]
CFPF, CFCON = byweight(CFV[0])
CFTOT = wsum(CFPF)
CFSAME = all(CFV[k] == [12 - x for x in BV[k]] for k in range(NORB))
NUL = sorted(set(NPI - rrank(TAB[k], PRIME) for k in range(NORB)))
gate(CFPF == [0, 0, 2, 6, 12] and CFCON and CFTOT == 48 and CFSAME
     and NUL == [48], "D10",
     "classes whose pair sits inside the pattern: {0} by weight, summing to {1}, equal to the per-block kernel of all {2} tables".format(
         nd(CFPF), nd(CFTOT), nd(NORB)))

RJPF, RJCON = byweight(RJV[0])
RJTOT = wsum(RJPF)
gate(RJPF == [0, 6, 10, 12, 12] and RJTOT == 144 and RJTOT != NUL[0]
     and all(RJV[k] != [12 - x for x in BV[k]] for k in range(NORB)), "D11",
     "rejector: asking only that the pattern meet the pair gives {0}, a nullity of {1}, not the measured {2}, on every table".format(
         nd(RJPF), nd(RJTOT), nd(NUL[0])))

TPF, TCON, TTOT = profile(TAB[K0], PRIME)
TSAME = all(BV[k] == BV[K0] for k in range(NORB))
gate(TPF == [12, 12, 10, 6, 0] and TCON and TTOT == 144 and TSAME
     and TTOT == rrank(TAB[K0], PRIME), "D12",
     "one orbit table has per-block rank {0} by weight, recomposing to its rank {1}, and all {2} tables agree".format(
         nd(TPF), nd(TTOT), nd(NORB)))

B2 = sorted(set(rrank(np.vstack([blockbasis(s, 2) for s in range(16)]), 2)
                for s in range(1)))
R2 = sorted(set(rank_modp(TAB[k], 2) for k in range(NORB)))
gate(B2 == [12] and R2 == [144], "D13",
     "honest negative: at characteristic {0} the {1} blocks collapse to rank {2}, so the route is silent; measured directly each table has rank {3}".format(
         nd(2), nd(16), nd(B2[0]), nd(R2[0])))

MPF = {}
MCON = {}
MTOT = {}
MRK = {}
for q in (PRIME, PRIME2):
    MPF[q], MCON[q], MTOT[q] = profile(INC, q)
    MRK[q] = rrank(INC, q)
MKD = [12 - x for x in MPF[PRIME]]
MKD2 = [12 - x for x in MPF[PRIME2]]
MKER = NPI - MRK[PRIME]
gate(MRK[PRIME] == 105 and MRK[PRIME2] == 105 and MKER == 87
     and MKD == [3, 3, 6, 6, 12] and MKD2 == [3, 3, 6, 6, 12]
     and MCON[PRIME] and MCON[PRIME2] and NPI - MTOT[PRIME] == 87
     and NPI - MTOT[PRIME2] == 87, "D14",
     "the incidence kernel is {0} with per-block dimensions {1} by weight, constant in each class, recomposing to {0} at both primes".format(
         nd(MKER), nd(MKD)))

UPF, UCON, UTOT = profile(UM, PRIME)
VPF, VCON, VTOT = profile(VM, PRIME)
UKD = [12 - x for x in UPF]
VKD = [12 - x for x in VPF]
UKER = NPI - rrank(UM, PRIME)
VKER = NPI - rrank(VM, PRIME)
gate(UKER == 78 and UKD == [2, 2, 4, 8, 12] and NPI - UTOT == 78 and UCON
     and VKER == 48 and VKD == [0, 0, 2, 6, 12] and NPI - VTOT == 48 and VCON,
     "D15",
     "the axis-in-pair part has kernel {0} with per-block {1}, and the other part kernel {2} with {3}, each recomposing".format(
         nd(UKER), nd(UKD), nd(VKER), nd(VKD)))

VIDX = [k for k in range(NORB) if np.array_equal(TAB[k], VM)]
UPART = [k for k in IORB if k not in VIDX]
gate(len(VIDX) == 1 and VIDX[0] in IORB and VPF == TPF and len(UPART) == 3
     and np.array_equal(UM, sum(TAB[k] for k in UPART))
     and np.array_equal(UM + VM, INC), "D16",
     "the second part is one of the {0} tables and its per-block profile is the single-table one; the first part is the other {1} of the {2} orbits".format(
         nd(NORB), nd(len(UPART)), nd(len(IORB))))

gate(MPF[PRIME] == [9, 9, 6, 6, 0] and MTOT[PRIME] == 105
     and UPF == [10, 10, 8, 4, 0] and UTOT == 114
     and VPF == [12, 12, 10, 6, 0] and VTOT == 144
     and UTOT == rrank(UM, PRIME) and VTOT == rrank(VM, PRIME), "D17",
     "per-block ranks by weight: incidence {0} to {1}, first part {2} to {3}, second part {4} to {5}".format(
         nd(MPF[PRIME]), nd(MTOT[PRIME]), nd(UPF), nd(UTOT), nd(VPF), nd(VTOT)))

DTM = [TPF[w] - MPF[PRIME][w] for w in range(5)]
DTW = wsum(DTM)
gate(DTM == [3, 3, 4, 0, 0] and DTW == 39 and DTW == TTOT - MTOT[PRIME]
     and DTM[3] == 0 and DTM[4] == 0, "D18",
     "single table minus incidence is {0} by weight, weighting to {1} = {2} - {3}, and it vanishes in both blocks of weight above {4}".format(
         nd(DTM), nd(DTW), nd(TTOT), nd(MTOT[PRIME]), nd(2)))

DTU = [TPF[w] - UPF[w] for w in range(5)]
DUM = [UPF[w] - MPF[PRIME][w] for w in range(5)]
WTU = wsum(DTU)
WUM = wsum(DUM)
gate(DTU == [2, 2, 2, 2, 0] and WTU == 30 and DUM == [1, 1, 2, -2, 0]
     and WUM == 9 and WTU + WUM == DTW and DUM[3] < 0, "D19",
     "two steps: {0} weighting {1}, then {2} weighting {3}, together {4}; the weight {5} entry rises, so it is not monotone".format(
         nd(DTU), nd(WTU), nd(DUM), nd(WUM), nd(WTU + WUM), nd(3)))

OUTI = [k for k in range(NORB) if k not in IORB]
RA = OUTI[:4]
RB = IORB[:3] + OUTI[:1]
RRK = []
RDR = []
RCN = []
for R in (RA, RB):
    W = sum(TAB[k] for k in R)
    WPF, WCON, WTOT = profile(W, PRIME)
    RRK.append(rrank(W, PRIME))
    RDR.append([TPF[w] - WPF[w] for w in range(5)])
    RCN.append(WCON)
TWM = sum(TAB[k] for k in RA)
MROW = set(tuple(int(v) for v in INC[j]) for j in range(NCOV))
TWCV = sum(1 for j in range(NCOV) if tuple(int(v) for v in TWM[j]) in MROW)
TWEN = sorted(set(int(v) for v in TWM.reshape(-1)))
TWRS = sorted(set(int(v) for v in TWM.sum(axis=1)))
TWCS = sorted(set(int(v) for v in TWM.sum(axis=0)))
KI4 = nullbasis(INC, PRIME)
KT4 = nullbasis(TWM, PRIME)
KMEET = KI4.shape[0] + KT4.shape[0] - rrank(np.vstack([KI4, KT4]), PRIME)
gate(len(RA) == 4 and not set(RA) & set(IORB) and RCN[0]
     and TWCV == 0 and TWEN == [0, 1] and TWRS == [8] and TWCS == [8]
     and RRK[0] == 105 and RDR[0] == [3, 3, 4, 0, 0]
     and wsum(RDR[0]) == 39, "D20",
     "honest negative: the next {0} tables sum to a zero-one table with {1} of {2} rows a cover, yet rank {3}, drop {4}, weight {5}".format(
         nd(len(RA)), nd(TWCV), nd(NCOV), nd(RRK[0]), nd(RDR[0]),
         nd(wsum(RDR[0]))))

gate(KI4.shape[0] == 87 and KT4.shape[0] == 87 and KMEET == 33
     and len(RB) == 4 and RB != IORB and len(set(RB) & set(IORB)) == 3
     and RRK[1] == 93 and RDR[1] == [3, 3, 4, 3, 0], "D21",
     "both kernels have dimension {0} but meet in {1}, so the kernel space separates them; swapping one part gives rank {2}, drop {3}".format(
         nd(KT4.shape[0]), nd(KMEET), nd(RRK[1]), nd(RDR[1])))

SFOUR = np.vstack([TAB[k] for k in IORB])
SR4 = [rrank(SFOUR, q) for q in (PRIME, PRIME2)]
CKD = NPI - SR4[0]
CPF, CCON, CTOT = profile(SFOUR, PRIME)
CKV = [12 - x for x in CPF]
gate(len(IORB) == 4 and np.array_equal(INC, ISUM) and CKD == 12
     and CKV == [0, 0, 0, 0, 12] and NPI - CTOT == 12, "D22",
     "the incidence is the entrywise sum of exactly {0} orbit tables whose common kernel is {1}, with per-block dimensions {2}".format(
         nd(len(IORB)), nd(CKD), nd(CKV)))

BAS = blockbasis(15, PRIME)
MF22 = int(np.count_nonzero(np.mod(np.dot(INC, BAS.T), PRIME)))
PF22 = sum(int(np.count_nonzero(np.mod(np.dot(TAB[k], BAS.T), PRIME)))
           for k in IORB)
gate(MF22 == 0 and PF22 == 0 and SANTI and IDS
     and rrank(BAS, PRIME) == 12, "D23",
     "that common kernel is the all-axes block, the space where every flip acts by its sign; the incidence kills all {0} of it, {1} failures".format(
         nd(rrank(BAS, PRIME)), nd(MF22)))

KM = nullbasis(INC, PRIME)
KMOK = not np.mod(np.dot(INC, KM.T), PRIME).any()
CUR = BAS
EXT = []
for a in range(KM.shape[0]):
    if rrank(np.vstack([CUR, KM[a:a + 1]]), PRIME) > CUR.shape[0]:
        CUR = np.vstack([CUR, KM[a:a + 1]])
        EXT.append(KM[a])
EXA = np.array(EXT, dtype=np.int64)
KILL4 = sum(1 for a in range(EXA.shape[0])
            if any(not np.mod(np.dot(TAB[k], EXA[a]), PRIME).any() for k in IORB))
gate(KM.shape[0] == 87 and KMOK and EXA.shape[0] == 75 and KILL4 == 0
     and rrank(CUR, PRIME) == 87 and KM.shape[0] - CKD == EXA.shape[0], "D24",
     "the remaining {0} = {1} - {2} kernel dimensions are killed by the sum and by no single part: {3} of {0} are killed by even one of the {4}".format(
         nd(EXA.shape[0]), nd(KM.shape[0]), nd(CKD), nd(KILL4), nd(len(IORB))))

gate(SR4 == [180, 180] and NPI - SR4[0] == CKD and SR4[0] == CTOT, "D25",
     "the stack of those {0} parts has rank {1} at both primes, which is {2} - {3}".format(
         nd(len(IORB)), nd(SR4[0]), nd(NPI), nd(CKD)))

KSEP = not np.array_equal(RK1[I0][0], RK1[I1][0])
KP0 = [12 - x for x in byweight(BV[I0])[0]]
KP1 = [12 - x for x in byweight(BV[I1])[0]]
gate(len(CSZ) == 2 and CSZ == [48, 48] and KDIM == [48] and KDIM2 == [48]
     and SAMESPLIT and KSEP and KP0 == KP1 and KP0 == [0, 0, 2, 6, 12], "D26",
     "honest negative: the {0} tables hold {1} kernels of dimension {2}, {3} each, but both give per-block {4}, which cannot separate them".format(
         nd(NORB), nd(len(CSZ)), nd(KDIM[0]), nd(CSZ[0]), nd(KP0)))

NDIST = len(set(tuple(v) for v in BV))
gate(NDIST == 1 and TSAME and TPF == [12, 12, 10, 6, 0], "D27",
     "all {0} tables carry the same vector of {1} per-block ranks, {2} distinct in all, so the split is uniform across the family".format(
         nd(NORB), nd(16), nd(NDIST)))

emit("{0} blocks of {1}: one table {2}, incidence {3}, drop {4} in the blocks of weight at most {5}, kernel {6} splitting {7} and {8}".format(
    nd(16), nd(len(REPF)), nd(TTOT), nd(MTOT[PRIME]), nd(DTW), nd(2),
    nd(MKER), nd(CKD), nd(EXA.shape[0])))
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
MBS = RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RSS / 1024.0
emit("elapsed {0} s, peak resident {1} MB".format(nd(int(time.time() - T0)), nd(int(MBS))))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
sys.exit(0 if STAT[1] == 0 else 1)
