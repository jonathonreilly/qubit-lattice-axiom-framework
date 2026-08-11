"""Physical cell cutting: the top two weights are rigid, and an image label separates the twin.

Standalone exact runner. It rebuilds the unit four-cube cell object from scratch: the sixteen corners, the five-corner
unit-determinant pieces at the adjacency cost floor, the cuttings by them, the 192 pieces that occur, and the 192
eight-piece covers. The group of 384 signed coordinate maps, built by permuting the four coordinates and flipping any
of them, acts freely on the 36864 pairs of a piece and a cover, giving 96 orbits of size 384, each read as a zero and
one table over covers by pieces. The tables are pairwise disjoint and sum to the all-ones table, so every 4-subset of
them is a zero-one 8-regular member of a family of 3321960; the cover incidence is one member, the cycle 773 twin another.

The sixteen pure flips act freely on the 192 pieces with 12 orbits, so each of the 16 sign patterns of the four axes
carries a piece-side block of dimension 12, and the 16 blocks fill all 192 piece coordinates. This cycle 775 run asks
what those blocks force. At the all-signs pattern every table dies. At each weight-3 pattern every table has rank 6,
one and the same image, and one of exactly two kernels of dimension 6, which meet in 0 and are named by the cycle 772
colour. A sum of four tables therefore has rank at most 6 there, and when exactly one of the four carries the minority
colour the rank is exactly 6: the lone-minority theorem, proved here in prose and checked on a deterministic sweep of
1056 members. Both the cover incidence and the twin are lone-minority members, so the whole excess of one table over
the incidence, 39 dimensions, sits at weights 0, 1 and 2.

The cover side supplies the reason the top is rigid. Each cover is held by a single axis flip, so the cover-side block
of a weight-w pattern has dimension six times four less w; a table carries block into block, dies where that dimension
is 0, and fills it where it is 6. What the top weights cannot do is separate the incidence from the twin: the image of
a table at a weight-1 pattern gives a label with six values whose fibres over the weight-0 label hold two values each,
the twin carries the fibre swap of the incidence multiset, and 30720 of the 3321960 members carry that multiset.

All work is exact over the integers and two fixed primes; no floating point enters any gate and no constant is fitted.
Of the 35 gates, three are rejectors, six are honest negatives, and one gate is both. Output: one line per gate, three
extra measurement lines, one summary line, a resource line, then the total line."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

PRIME = 1000003
PRIME2 = 1000033

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
# 6. the four parts, the twin, and the block arithmetic they share
# ------------------------------------------------------------------

IPARTS = sorted(IORB)
OUTI = [k for k in range(NORB) if k not in IORB]
TPARTS = OUTI[:4]


def partsum(ks):
    """The entrywise sum of the orbit tables listed. Every member of the family
    below, and both swap rejectors, is built by this one path."""
    M = np.zeros((NCOV, NPI), dtype=np.int64)
    for k in ks:
        M = M + TAB[k]
    return M


def blk(X, s, p):
    """X cut down to the block of sign pattern s: covers by twelve."""
    return np.mod(np.dot(np.mod(X, p), blockbasis(s, p).T), p)


def imkey(B, p):
    """A canonical form of the image of a block restriction inside the cover
    space, returned as a byte string so that two images can be compared."""
    return rref_modp(B.T, p)[0].tobytes()


def meetdim(K1, K2, p):
    """dim K1 plus dim K2 less the rank of the two stacked: the meet dimension."""
    if K1.shape[0] == 0 or K2.shape[0] == 0:
        return 0
    return K1.shape[0] + K2.shape[0] - rrank(np.vstack([K1, K2]), p)


def labels(s, p):
    """The image label of each of the 96 orbits at sign pattern s, numbered by
    first appearance along the orbit order."""
    d = {}
    out = []
    for k in range(NORB):
        out.append(d.setdefault(imkey(blk(TAB[k], s, p), p), len(d)))
    return out


def sset(X):
    return sorted(set(int(v) for v in np.array(X).reshape(-1)))


def hist(vs):
    h = {}
    for v in vs:
        h[v] = h.get(v, 0) + 1
    return h


def hstr(h):
    return " ".join("{0}:{1}".format(nd(k), nd(h[k])) for k in sorted(h))


def sl(vs):
    """a list of small numbers printed compactly, slash separated"""
    return "/".join(nd(v) for v in vs)


def tl(ts):
    """a list of tuples printed compactly, one slashed group each"""
    return " ".join(sl(t) for t in ts)


def sizesof(lab):
    return sorted(hist(lab).values())


def nCr(n, r):
    """Binomial coefficient by exact integer arithmetic, no floating point."""
    v = 1
    for i in range(r):
        v = v * (n - i) // (i + 1)
    return v


def ceildiv(a, b):
    return 0 if b == 0 else (a + b - 1) // b


INCS = partsum(IPARTS)
TW = partsum(TPARTS)
TSUM = partsum(range(NORB))
ONES = np.ones((NCOV, NPI), dtype=np.int64)
TNZ = sorted(set(int(np.count_nonzero(TAB[k])) for k in range(NORB)))
FLAT = np.array([TAB[k].reshape(-1) for k in range(NORB)], dtype=np.int64)
GM = np.dot(FLAT, FLAT.T)
np.fill_diagonal(GM, 0)
OVLP = int(GM.max())
NFAM = nCr(NORB, 4)
NSLOT = NS * SIZES[0]
NSLOT2 = NPI * PCSET[0]
FILL = NORB * TNZ[0]
IRC = [sset(INCS), sset(INCS.sum(axis=1)), sset(INCS.sum(axis=0))]
TRC = [sset(TW), sset(TW.sum(axis=1)), sset(TW.sum(axis=0))]

ALLS = [s for s in range(16) if WT[s] == 4][0]
W3P = [s for s in range(16) if WT[s] == 3]
W1P = [s for s in range(16) if WT[s] == 1]
FIRST = [[s for s in range(16) if WT[s] == w][0] for w in range(5)]
BSHP = sorted(set(blockbasis(s, q).shape
                  for s in range(16) for q in (PRIME, PRIME2)))
BDIM = sorted(set(rrank(blockbasis(s, q), q)
                  for s in range(16) for q in (PRIME, PRIME2)))
BSTK = [rrank(np.vstack([blockbasis(s, q) for s in range(16)]), q)
        for q in (PRIME, PRIME2)]

# ------------------------------------------------------------------
# 7. the top two weights: ranks, images, kernels
# ------------------------------------------------------------------

W4R = set()
W4K = set()
for q in (PRIME, PRIME2):
    for k in range(NORB):
        B4 = blk(TAB[k], ALLS, q)
        W4R.add(rrank(B4, q))
        W4K.add(nullbasis(B4, q).shape[0])

W3R = set()
W3N = 0
for q in (PRIME, PRIME2):
    for s in W3P:
        for k in range(NORB):
            W3R.add(rrank(blk(TAB[k], s, q), q))
            W3N += 1

IMN = []
IMSTK = []
KRN = []
KRSZ = []
KRD = set()
KMEET = []
KSTK = []
PRC = []
PRD = []
KREP = {}
KSHIFT = KCLS[1:] + KCLS[:1]
for s in W3P:
    ims = {}
    krs = {}
    cls = []
    imb = []
    for k in range(NORB):
        B3 = blk(TAB[k], s, PRIME)
        ik = imkey(B3, PRIME)
        ims[ik] = ims.get(ik, 0) + 1
        imb.append(rref_modp(B3.T, PRIME)[0])
        K3 = nullbasis(B3, PRIME)
        KRD.add(K3.shape[0])
        kk = rref_modp(K3, PRIME)[0].tobytes()
        if kk not in krs:
            krs[kk] = len(krs)
        cls.append(krs[kk])
    IMN.append(len(ims))
    IMSTK.append(rrank(np.vstack(imb), PRIME))
    KRN.append(len(krs))
    KRSZ.append(sorted(hist(cls).values()))
    for v in (0, 1):
        KREP[(s, v)] = nullbasis(blk(TAB[KCLS.index(v)], s, PRIME), PRIME)
    KMEET.append(meetdim(KREP[(s, 0)], KREP[(s, 1)], PRIME))
    KSTK.append(rrank(np.vstack([KREP[(s, 0)], KREP[(s, 1)]]), PRIME))
    PRC.append(len(set(zip(cls, KCLS))))
    PRD.append(len(set(zip(cls, KSHIFT))))

# ------------------------------------------------------------------
# 8. the deterministic sweep of four-part members
# ------------------------------------------------------------------

MEM = set()
for st in range(1, 12):
    for a in range(NORB):
        MEM.add(tuple(sorted({a, divmod(a + st, NORB)[1], divmod(a + 2 * st, NORB)[1],
                              divmod(a + 3 * st, NORB)[1]})))
MEM = sorted(m for m in MEM if len(m) == 4)
NMEM = len(MEM)

BL3 = dict((s, [blk(TAB[k], s, PRIME) for k in range(NORB)]) for s in W3P)
LINOK = all(np.array_equal(np.mod(sum(BL3[s][k] for k in IPARTS), PRIME),
                           blk(INCS, s, PRIME)) for s in W3P)
HALL = {}
H22 = {}
EXC = 0
N31 = 0
N22 = 0
NSAME = 0
FAIL31 = 0
for m in MEM:
    c1 = sum(KCLS[k] for k in m)
    for s in W3P:
        Bm = np.mod(sum(BL3[s][k] for k in m), PRIME)
        r = rrank(Bm, PRIME)
        HALL[r] = HALL.get(r, 0) + 1
        if r > 6:
            EXC += 1
        if c1 == 1 or c1 == 3:
            mj = 0 if c1 == 1 else 1
            if r != 6 or meetdim(nullbasis(Bm, PRIME), KREP[(s, mj)], PRIME) != 0:
                FAIL31 += 1
        elif c1 == 2:
            H22[r] = H22.get(r, 0) + 1
    if c1 == 1 or c1 == 3:
        N31 += 1
    elif c1 == 2:
        N22 += 1
    else:
        NSAME += 1
MAXR = max(HALL)

CN = [KCLS.count(0), KCLS.count(1)]
FSAME = nCr(CN[0], 4) + nCr(CN[1], 4)
FLONE = nCr(CN[0], 3) * CN[1] + nCr(CN[1], 3) * CN[0]
FTWO = nCr(CN[0], 2) * nCr(CN[1], 2)
FTOT = FSAME + FLONE + FTWO

ICOL = sorted(KCLS[k] for k in IPARTS)
TCOL = sorted(KCLS[k] for k in TPARTS)
IMAJ = 0 if sum(ICOL) == 1 else 1
TMAJ = 0 if sum(TCOL) == 1 else 1

TRIP = []
for s in range(16):
    A1 = blk(INCS, s, PRIME)
    A2 = blk(TW, s, PRIME)
    TRIP.append((rrank(A1, PRIME), rrank(A2, PRIME),
                 meetdim(nullbasis(A1, PRIME), nullbasis(A2, PRIME), PRIME)))
TCL = [sorted(set(TRIP[s] for s in range(16) if WT[s] == w)) for w in range(5)]
TCON = all(len(c) == 1 for c in TCL)
PF = [c[0] for c in TCL]
RKI = sum(CSIZE[w] * PF[w][0] for w in range(5))
RKT = sum(CSIZE[w] * PF[w][1] for w in range(5))
MTOT = sum(CSIZE[w] * PF[w][2] for w in range(5))
P2I = profile(INCS, PRIME2)
P2T = profile(TW, PRIME2)
W3TRIP = sorted(set(TRIP[s] for s in W3P))

SPF = set()
SCON = True
for k in range(NORB):
    pk, ck, tk = profile(TAB[k], PRIME)
    SPF.add(tuple(pk))
    if not ck:
        SCON = False
SP1 = sorted(SPF)[0]
DROP = [SP1[w] - PF[w][0] for w in range(5)]
EXCESS = sum(CSIZE[w] * DROP[w] for w in range(5))
M4 = CSIZE[4] * PF[4][2]
M02 = CSIZE[0] * PF[0][2] + CSIZE[2] * PF[2][2]
M13 = CSIZE[1] * PF[1][2] + CSIZE[3] * PF[3][2]

# ------------------------------------------------------------------
# 9. the image label, its fibres, and what it separates
# ------------------------------------------------------------------

LW = [labels(FIRST[w], PRIME) for w in range(5)]
LSZ = [sizesof(LW[w]) for w in range(5)]
LN = [len(set(LW[w])) for w in range(5)]
JN = []
JSZ = []
for w in (0, 1, 2):
    jt = hist(list(zip(LW[w], KCLS)))
    JN.append(len(jt))
    JSZ.append(sorted(set(jt.values())))

FIB = {}
FIBOK = True
for k in range(NORB):
    if LW[1][k] in FIB and FIB[LW[1][k]] != LW[0][k]:
        FIBOK = False
    FIB[LW[1][k]] = LW[0][k]
INV = {}
for a in sorted(FIB):
    INV.setdefault(FIB[a], []).append(a)
FSZ = sorted(len(v) for v in INV.values())
SWP = {}
for b in INV:
    if len(INV[b]) == 2:
        SWP[INV[b][0]] = INV[b][1]
        SWP[INV[b][1]] = INV[b][0]
NOFIX = all(SWP[a] != a for a in SWP)
FIBTXT = " ".join("{0}({1})".format(nd(b), "".join(nd(a) for a in INV[b]))
                  for b in sorted(INV))

LW1 = [labels(s, PRIME) for s in W1P]
ONELAB = all(LW1[i] == LW1[0] for i in range(len(W1P)))
IMS = [tuple(sorted(L[k] for k in IPARTS)) for L in LW1]
TMS = [tuple(sorted(L[k] for k in TPARTS)) for L in LW1]
DISJ = all(not (set(IMS[i]) & set(TMS[i])) for i in range(len(W1P)))
ONEIM = len(set(IMS)) == 1
ONETM = len(set(TMS)) == 1
SWIM = tuple(sorted(SWP[v] for v in IMS[0]))

MULT = hist(IMS[0])
NARR = 1
for v in sorted(MULT):
    NARR = NARR * nCr(LSZ[1][0], MULT[v])
NBRU = 0
for c4 in itertools.combinations(LW[1], 4):
    if tuple(sorted(c4)) == IMS[0]:
        NBRU += 1
PPT = NARR * 1000 // NFAM

SWMEM = []
for i in range(4):
    for a in OUTI:
        SWMEM.append([k for k in IPARTS if k != IPARTS[i]] + [a])
NSW = len(SWMEM)
SWKEEP = sum(1 for m in SWMEM if tuple(sorted(LW[1][k] for k in m)) == IMS[0])
SWFORM = sum(LSZ[1][0] - MULT[LW[1][k]] for k in IPARTS)

DET = []
GRP = []
IHIST = {}
for w in (0, 1, 2):
    BW = [blk(TAB[k], FIRST[w], PRIME) for k in range(NORB)]
    gp = {}
    for m in MEM:
        key = tuple(sorted(LW[w][k] for k in m))
        rw = rrank(np.mod(sum(BW[k] for k in m), PRIME), PRIME)
        gg = gp.setdefault(key, {})
        gg[rw] = gg.get(rw, 0) + 1
    GRP.append(len(gp))
    DET.append(sum(1 for key in gp if len(gp[key]) == 1))
    if w == 1:
        IHIST = gp[IMS[0]]
IGSZ = sum(IHIST.values())


def pairprof(X, ax):
    """The multiset of overlaps of the rows, or of the columns, of X, taken over
    all unordered pairs of them."""
    G = np.dot(X, X.T) if ax == 0 else np.dot(X.T, X)
    n = G.shape[0]
    h = {}
    for i in range(n):
        for j in range(i + 1, n):
            v = int(G[i, j])
            h[v] = h.get(v, 0) + 1
    return h


PRI = pairprof(INCS, 0)
PRT = pairprof(TW, 0)
PCI = pairprof(INCS, 1)
PCT = pairprof(TW, 1)
NPAIRS = sum(PRI.values())

GIM = [rref_modp(blk(TAB[0], s, PRIME).T, PRIME)[0] for s in W3P]
GSTK = rrank(np.vstack(GIM), PRIME)
GDIM = sorted(set(g.shape[0] for g in GIM))

# ------------------------------------------------------------------
# 10. the two flip actions and the block dimensions they force
# ------------------------------------------------------------------

PFIX = sorted(set(sum(1 for i in range(NPI) if PERM[e][i] == i)
                  for e in FLIPS if e != IDG))
PORB = len(REPF)
PORBSZ = sorted(set(len(o) for o in ORBF))

CREP = []
seenc = set()
for j in range(NCOV):
    if j in seenc:
        continue
    for e in FLIPS:
        seenc.add(CPERM[e][j])
    CREP.append(j)
CORB = [sorted(set(CPERM[e][j0] for e in FLIPS)) for j0 in CREP]
CORBSZ = sorted(set(len(o) for o in CORB))
CSTAB = sorted(set(sum(1 for e in FLIPS if CPERM[e][j0] == j0) for j0 in CREP))
CMASK = hist([1 << CAX[j0] for j0 in CREP])
CMKEY = sorted(CMASK)
CMSZ = sorted(set(CMASK.values()))


def covbasis(s, p):
    """The basis of the cover-side block of sign pattern s: one vector per flip
    orbit of covers whose stabiliser carries the sign plus one at s, an orbit
    whose stabiliser carries minus one contributing nothing."""
    rows = []
    for j0 in CREP:
        if (s >> CAX[j0]) & 1:
            continue
        v = np.zeros(NCOV, dtype=np.int64)
        for u in range(NFL):
            v[CPERM[FLIPS[u]][j0]] = 1 if (popc(s & FW[u]) & 1) == 0 else p - 1
        rows.append(v)
    if not rows:
        return np.zeros((0, NCOV), dtype=np.int64)
    return np.array(rows, dtype=np.int64)


CDIM = []
CRK = []
CSPAN = []
CSAT = []
CONTN = 0
CONTBAD = 0
for s in range(16):
    CB = covbasis(s, PRIME)
    d0 = CB.shape[0]
    CDIM.append(d0)
    CRK.append((rrank(CB, PRIME), rrank(covbasis(s, PRIME2), PRIME2)))
    acc = np.zeros((0, NCOV), dtype=np.int64)
    sat = 0 if d0 == 0 else -1
    for k in range(NORB):
        IB = rref_modp(blk(TAB[k], s, PRIME).T, PRIME)[0]
        CONTN += 1
        if rrank(np.vstack([CB, IB]), PRIME) != d0:
            CONTBAD += 1
        acc = rref_modp(np.vstack([acc, IB]), PRIME)[0]
        if sat < 0 and acc.shape[0] == d0:
            sat = k + 1
    CSPAN.append(acc.shape[0])
    CSAT.append(sat)

CDOK = all(CDIM[s] == 6 * (4 - WT[s]) for s in range(16))
CRKOK = all(CRK[s] == (CDIM[s], CDIM[s]) for s in range(16))
CSPOK = all(CSPAN[s] == CDIM[s] for s in range(16))
CDW = [CDIM[FIRST[w]] for w in range(5)]
CDCON = all(len(set(CDIM[s] for s in range(16) if WT[s] == w)) == 1
            for w in range(5))
CSUM = sum(CDIM)
PSUM = 16 * PORB
CEIL = [min(PORB, CDW[w]) for w in range(5)]
SHORT = [CEIL[w] - SP1[w] for w in range(5)]
WCEIL = sum(CSIZE[w] * CEIL[w] for w in range(5))
WMEAS = wsum(list(SP1))
WGAP = WCEIL - WMEAS
GAPW = [w for w in range(5) if SHORT[w] > 0]
SATW = [CSAT[FIRST[w]] for w in range(5)]
SATCON = all(len(set(CSAT[s] for s in range(16) if WT[s] == w)) == 1
             for w in range(5))
SATLB = [ceildiv(CDW[w], SP1[w]) for w in range(5)]
UNDER = [w for w in range(5) if SP1[w] < CDW[w]]

# ------------------------------------------------------------------
# 11. the gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and PCSET == [1975] and GENERIC
     and NSLOT == 379200 and NSLOT2 == NSLOT and NCOV == 192 and BRS == [8]
     and COVEXACT, "F0",
     "{0} unit-determinant subsets, {1} at cost floor {2}, {3} cuttings of {4}, {5} pieces in {6} each, {7} slots, {5} covers of {8}".format(
         nd(NCAND), nd(NKEPT), nd(FLOOR), nd(NS), nd(SIZES[0]), nd(NPI),
         nd(PCSET[0]), nd(NSLOT), nd(BRS[0])))

gate(NORB == 96 and TNZ == [384] and OVLP == 0 and np.array_equal(TSUM, ONES)
     and FILL == NCOV * NPI and FILL == 36864 and NFAM == 3321960
     and IRC == [[0, 1], [8], [8]] and TRC == [[0, 1], [8], [8]]
     and np.array_equal(INC, INCS) and len(IPARTS) == 4, "F1",
     "{0} tables of {1} entries, pairwise disjoint, summing to the all-ones table ({2}); {3} members, the incidence one of them".format(
         nd(NORB), nd(TNZ[0]), nd(FILL), nd(NFAM)))

gate(CSIZE == [1, 4, 6, 4, 1] and BSHP == [(12, NPI)] and BDIM == [12]
     and BSTK == [192, 192], "F2",
     "the {0} sign patterns have weight sizes {1}, each piece-side block has {2} rows of rank {2}, and stacked they reach {3}, both primes".format(
         nd(16), nd(CSIZE), nd(12), nd(BSTK[0])))

gate(sorted(W4R) == [0] and sorted(W4K) == [12] and len(W4R) == 1
     and len(W4K) == 1, "F3",
     "at the all-signs pattern all {0} tables have rank {1} on the block and kernel {2} there, at both primes: the rank set is {3}".format(
         nd(NORB), nd(0), nd(12), nd(sorted(W4R))))

gate(sorted(W3R) == [6] and len(W3R) == 1 and W3N == 768
     and len(W3P) == 4, "F4",
     "at each of the {0} weight-{1} patterns all {2} tables have rank {3}: the set of all {4} measured ranks per prime is {5}".format(
         nd(len(W3P)), nd(3), nd(NORB), nd(6), nd(W3N // 2), nd(sorted(W3R))))

gate(IMN == [1, 1, 1, 1] and IMSTK == [6, 6, 6, 6] and len(set(IMN)) == 1
     and IMSTK[0] == sorted(W3R)[0], "F5",
     "at each weight-{0} pattern the {1} image keys collapse to {2}, and all {1} images stacked have rank {3}, the rank of one table".format(
         nd(3), nd(NORB), nd(IMN[0]), nd(IMSTK[0])))

gate(KRN == [2, 2, 2, 2] and KRSZ == [[48, 48]] * 4 and sorted(KRD) == [6]
     and len(KRD) == 1, "F6",
     "at each weight-{0} pattern there are exactly {1} kernels, each of dimension {2}, with class sizes {3}".format(
         nd(3), nd(KRN[0]), nd(sorted(KRD)[0]), nd(KRSZ[0])))

gate(PRC == [2, 2, 2, 2] and min(PRD) > 2 and PRD == [4, 4, 4, 4], "F7",
     "rejector: kernel class against colour gives {0} pairs at every weight-{1} pattern, against the colour shifted by one orbit {2}".format(
         nd(PRC[0]), nd(3), nd(PRD[0])))

gate(KMEET == [0, 0, 0, 0] and KSTK == [12, 12, 12, 12]
     and KSTK[0] == BDIM[0], "F8",
     "at each weight-{0} pattern the two kernels meet in {1} and stack to rank {2}, the full piece-side block dimension".format(
         nd(3), nd(KMEET[0]), nd(KSTK[0])))

gate(NMEM == 1056 and EXC == 0 and MAXR == 6 and LINOK
     and sum(HALL.values()) == NMEM * len(W3P), "F9",
     "over the {0} sweep members the weight-{1} rank of the sum is at most {2}"
     " with {3} exceptions; spread {4}".format(
         nd(NMEM), nd(3), nd(MAXR), nd(EXC), hstr(HALL)))

gate(N31 == 538 and FAIL31 == 0 and N31 + N22 + NSAME == NMEM
     and N31 > 0, "F10",
     "{0} of the {1} members have a lone minority colour; each has weight-{2} rank {3}"
     " and kernel meeting the majority kernel in {4}, {5} misses".format(
         nd(N31), nd(NMEM), nd(3), nd(6), nd(0), nd(FAIL31)))

gate(N22 == 369 and sorted(H22) != [6] and 6 in H22 and min(H22) < 6
     and sum(H22.values()) == N22 * len(W3P), "F11",
     "rejector: the {0} even-split members give weight-{1} ranks {2}, so an even split does not force rank {3}".format(
         nd(N22), nd(3), hstr(H22), nd(6)))

gate(CN == [48, 48] and FSAME == 389160 and FLONE == 1660416
     and FTWO == 1272384 and FTOT == NFAM and FLONE < NFAM, "F12",
     "honest negative: colour classes {0} and {0} give {1} same-colour, {2} lone-minority and {3} even-split members, total {4}".format(
         nd(CN[0]), nd(FSAME), nd(FLONE), nd(FTWO), nd(FTOT)))

gate(ICOL == [0, 0, 0, 1] and TCOL == [0, 1, 1, 1] and IMAJ != TMAJ
     and sum(ICOL) in (1, 3) and sum(TCOL) in (1, 3), "F13",
     "the incidence parts have colours {0} and the twin parts {1}: both are lone-minority members, with different majorities".format(
         nd(ICOL), nd(TCOL)))

gate(W3TRIP == [(6, 6, 0)] and len(W3TRIP) == 1, "F14",
     "honest negative: at all {0} weight-{1} patterns the two kernels are {2} and {2}"
     " meeting in {3}; the theorem gives {2} each, not the meet".format(
         nd(len(W3P)), nd(3), nd(6), nd(0)))

gate(TCON and PF == [(9, 9, 3), (9, 9, 0), (6, 6, 3), (6, 6, 0), (0, 0, 12)]
     and RKI == 105 and RKT == 105 and MTOT == 33 and P2I[1] and P2T[1]
     and P2I[0] == [9, 9, 6, 6, 0] and P2T[0] == [9, 9, 6, 6, 0]
     and P2I[2] == RKI and P2T[2] == RKT, "F15",
     "per weight the two ranks and their kernel meet are {0}, class-constant,"
     " recomposing to {1} and {1} with meet {2}".format(
         tl(PF), nd(RKI), nd(MTOT)))

gate(SPF == set([(12, 12, 10, 6, 0)]) and SCON and DROP == [3, 3, 4, 0, 0]
     and EXCESS == 39 and M4 == 12 and M02 == 21 and M13 == 0
     and M4 + M02 + M13 == MTOT, "F16",
     "one table profiles {0}; the drop to incidence is {1}, weighting to {2};"
     " of the meet {3} sit at weight {4}, {5} at {6} and {7}, {8} else".format(
         sl(SP1), sl(DROP), nd(EXCESS), nd(M4), nd(4), nd(M02), nd(0), nd(2),
         nd(M13)))

gate(LN == [3, 6, 3, 1, 1] and LSZ[0] == [32, 32, 32] and LSZ[1] == [16] * 6
     and LSZ[2] == [32, 32, 32] and LSZ[3] == [96] and LSZ[4] == [96], "F17",
     "the image label takes {0} values by weight from {1} up, with class sizes"
     " {2} at weight {3}, {4} at {5}, {6} at {7}".format(
         sl(LN), nd(0), sl(LSZ[0]), nd(0), sl(LSZ[1]), nd(1), sl(LSZ[2]),
         nd(2)))

gate(JN == [6, 12, 6] and JSZ == [[16], [8], [16]], "F18",
     "the label and the colour are independent: {0} joint classes of {1} at weight {2}, {3} of {4} at weight {5}, {6} of {1} at weight {7}".format(
         nd(JN[0]), nd(JSZ[0][0]), nd(0), nd(JN[1]), nd(JSZ[1][0]), nd(1),
         nd(JN[2]), nd(2)))

gate(LW[0] == LW[2] and LN[0] == LN[2] and len(LW[0]) == NORB, "F19",
     "the weight-{0} label and the weight-{1} label agree on all {2} orbits, so they are one map with {3} values".format(
         nd(0), nd(2), nd(NORB), nd(LN[0])))

gate(FIBOK and FSZ == [2, 2, 2] and len(INV) == 3 and NOFIX
     and len(SWP) == LN[1], "F20",
     "the weight-{0} label fixes the weight-{1} label and each of the {2} fibres holds {3} values: {4}".format(
         nd(1), nd(0), nd(len(INV)), nd(FSZ[0]), FIBTXT))

gate(ONELAB and ONEIM and ONETM and IMS[0] == (0, 0, 1, 2)
     and TMS[0] == (3, 4, 5, 5) and DISJ, "F21",
     "the {0} weight-{1} patterns give one and the same label; the incidence parts carry {2} and the twin parts {3}, disjoint".format(
         nd(len(W1P)), nd(1), nd(list(IMS[0])), nd(list(TMS[0]))))

gate(SWIM == TMS[0] and SWIM != IMS[0], "F22",
     "swapping each incidence label for its partner in the fibre gives {0}, exactly the twin multiset {1}".format(
         nd(list(SWIM)), nd(list(TMS[0]))))

gate(NARR == NBRU and NARR == 30720 and PPT == 9 and NARR < NFAM
     and NBRU > 0, "F23",
     "the members carrying the incidence label multiset number {0} by binomials and {0} by enumerating all {1}: {2} in a thousand".format(
         nd(NARR), nd(NFAM), nd(PPT)))

gate(NSW == 368 and SWKEEP == SWFORM and SWKEEP == 58 and 0 < SWKEEP < NSW,
     "F24",
     "rejector: of the {0} one-part replacements only {1} keep the label multiset, by count and by class sizes alike, so the label moves".format(
         nd(NSW), nd(SWKEEP)))

gate(DET[0] == 0 and DET[2] == 0 and 0 < DET[1] < GRP[1]
     and GRP == [15, 123, 15] and IGSZ == 13, "F25",
     "honest negative: the multiset fixes the sum rank in {0} of {1}, {2} of {3},"
     " {4} of {5} groups by weight; incidence group of {6} gives {7}".format(
         nd(DET[0]), nd(GRP[0]), nd(DET[1]), nd(GRP[1]), nd(DET[2]),
         nd(GRP[2]), nd(IGSZ), hstr(IHIST)))

gate(PRI == PRT and PCI == PCT and NPAIRS == 18336
     and sum(PCI.values()) == NPAIRS, "F26",
     "honest negative: of {0} pairs rows overlap {1} and columns {2};"
     " the twin the same".format(
         nd(NPAIRS), hstr(PRI), hstr(PCI)))

gate(GSTK == 24 and GSTK > 6 and GDIM == [6] and len(GIM) == 4, "F27",
     "honest negative: the {0} common weight-{1} images, each of dimension {2}, stack to rank {3}, so the rigidity is one pattern at a time".format(
         nd(len(GIM)), nd(3), nd(GDIM[0]), nd(GSTK)))

gate(NARR > NSW and set(TMS[0]) & set(IMS[0]) == set() and NARR == 30720
     and NARR < NFAM, "F28",
     "honest negative: the label puts the twin outside the {0} members sharing the incidence multiset, and {0} is far from {1}".format(
         nd(NARR), nd(1)))

gate(PFIX == [0] and PORB == 12 and PORBSZ == [16]
     and CORBSZ == [8] and CSTAB == [2] and len(CREP) == 24
     and sorted(CFIX) == [1] and CPURE, "F29",
     "the {0} flips fix {1} pieces bar the identity, giving {2} piece orbits of {3}; on"
     " covers, {4} orbits of {5}, every stabiliser of order {6}".format(
         nd(NFL), nd(PFIX[0]), nd(PORB), nd(PORBSZ[0]), nd(len(CREP)),
         nd(CORBSZ[0]), nd(CSTAB[0])))

gate(CMKEY == [1, 2, 4, 8] and CMSZ == [6] and sum(CMASK.values()) == 24
     and len(CMASK) == 4, "F30",
     "over the {0} cover orbits the stabiliser masks are the {1} single-axis masks {2}, each carried by {3} orbits".format(
         nd(len(CREP)), nd(4), nd(CMKEY), nd(CMSZ[0])))

gate(CDOK and CRKOK and CSPOK and CDCON and CDW == [24, 18, 12, 6, 0]
     and CSUM == 192 and PSUM == 192, "F31",
     "the cover-side block dimension by weight is {0}, six times four less the"
     " weight, its rank at both primes and the span of all {1}".format(
         sl(CDW), nd(NORB)))
emit("both sides sum to {0} over the {1} patterns: {2} of cover side, {3} times {4} of piece side".format(
    nd(CSUM), nd(16), nd(CSUM), nd(16), nd(PORB)))

gate(CONTBAD == 0 and CONTN == 1536 and CONTN == NORB * 16, "F32",
     "containment: {0} of the {1} table-and-pattern pairs put an image outside the cover-side block, so every table takes block into block".format(
         nd(CONTBAD), nd(CONTN)))

gate(CEIL == [12, 12, 12, 6, 0] and list(SP1) == [12, 12, 10, 6, 0]
     and SHORT == [0, 0, 2, 0, 0] and WCEIL == 156 and WMEAS == 144
     and WGAP == 12 and WGAP == CSIZE[2] * SHORT[2] and GAPW == [2], "F33",
     "ceiling {0} against measured {1} leaves {2}, weighting to {3} against {4},"
     " a deficit of {5} wholly at weight {6}".format(
         sl(CEIL), sl(list(SP1)), sl(SHORT), nd(WCEIL), nd(WMEAS), nd(WGAP),
         nd(2)))
emit("so a table must die at weight {0}, where the cover-side block is {1}, and must fill the block at weight {2}, where it is {3}".format(
    nd(4), nd(CDW[4]), nd(3), nd(CDW[3])))

gate(UNDER == [0, 1, 2] and SATW == [4, 3, 3, 1, 0] and SATCON
     and SATLB == [2, 2, 2, 1, 0] and max(SATW) < NORB, "F34",
     "honest negative and rejector: one table repeated spans {0} against"
     " ambient {1}, short at weights {2}".format(
         sl(list(SP1)), sl(CDW), sl(UNDER)))
emit("in orbit order {0} tables saturate it; the dimension bound alone allows {1},"
     " so filling is cheap and not a witness for the four parts".format(
         sl(SATW), sl(SATLB)))

emit("the top two weights are forced, so weights {0} to {1} carry the whole excess {2}; the image label separates the twin into {3} of {4}".format(
    nd(0), nd(2), nd(EXCESS), nd(NARR), nd(NFAM)))
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
MBS = RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RSS / 1024.0
emit("elapsed {0} s, peak resident {1} MB".format(nd(int(time.time() - T0)), nd(int(MBS))))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
sys.exit(0 if STAT[1] == 0 else 1)
