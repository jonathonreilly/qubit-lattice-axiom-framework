"""A bounded four-part family and its sign-character kernel measurements.

Standalone exact runner. It rebuilds the unit four-cube cell object from scratch:
the sixteen corners, the five-corner unit-determinant pieces at the adjacency cost
floor, the cuttings by them, the 192 pieces that occur, and the 192 eight-piece
covers. The group of 384 signed coordinate maps is built by permuting the four
coordinates and flipping any of them; it acts freely on the 36864 pairs made of one
piece and one cover, giving 96 orbits of size 384, each read as a zero and one table
over covers by pieces.

The sixteen pure flips act freely on the pieces, producing sixteen integral character
blocks of dimension twelve. Over the two named odd prime fields the incidence member
and the lexicographically selected comparison member have nullity 87, meet dimension
33, and per-weight meet profile 3, 0, 3, 0, 12. The all-signs block is annihilated by
every orbit table as an exact integer identity. A declared deterministic 460-member
sample supplies selected-weight-3 kernel multiplicities and transversality counts.

All scientific gates use integer, rational, or named finite-field arithmetic. The
shifted grid is used only to enumerate candidates; exact simplex volumes and exact
integer separating hyperplanes certify the resulting continuous cuttings.

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


def is_prime(n):
    """Deterministic trial-division certificate for the two small field moduli."""
    if n < 2 or n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


FIELDS_OK = PRIME != PRIME2 and is_prime(PRIME) and is_prime(PRIME2)
if not FIELDS_OK:
    raise ValueError("field moduli must be distinct primes")


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
MASK_VISIBLE = len(MASK) == NKEPT and all(bits != 0 for bits in MASK)

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
SOLS_UNIQUE = len(set(SOLS)) == NS


def mask_search_certificate(masks, sols):
    """Every emitted candidate is a unique, disjoint full shifted-mask cover."""
    if len(masks) != NKEPT or any(bits == 0 for bits in masks):
        return False
    if len(sols) != 15800 or len(set(sols)) != len(sols):
        return False
    for sol in sols:
        if len(sol) != 24 or len(set(sol)) != 24:
            return False
        cov = 0
        for t in sol:
            if t < 0 or t >= len(masks) or cov & masks[t]:
                return False
            cov |= masks[t]
        if cov != UNIV:
            return False
    return True


MASK_SEARCH_OK = mask_search_certificate(MASK, SOLS)

USED = sorted(set(t for s in SOLS for t in s))
NPI = len(USED)
POS = dict((t, i) for i, t in enumerate(USED))
CUT = [tuple(sorted(POS[t] for t in s)) for s in SOLS]


def piece_det_num(S):
    v0 = CORN[S[0]]
    return abs(det4([[CORN[S[j + 1]][r] - v0[r] for j in range(4)]
                     for r in range(4)]))


KEPT_DET = [piece_det_num(S) for S in KEPT]
VOLUME_OK = (all(x == 1 for x in KEPT_DET)
             and all(sum(KEPT_DET[t] for t in sol) == 24 for sol in SOLS))

# Exact continuous certificate.  Each pair of full-dimensional simplices that
# co-occurs in a selected cutting is weakly separated by a nonzero normal from
# {-1,0,1}^4.  Their interiors are therefore disjoint.  The 24 normalized unit
# volumes equal the normalized volume 24 of [0,1]^4, so their union is the cube.
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
PAIR_SEPARATED = all(
    bool(np.any((SEP_HI[i] <= SEP_LO[j]) | (SEP_HI[j] <= SEP_LO[i])))
    for i, j in CO_PAIRS
)


def continuous_cut_certificate(detnums, separated):
    return (len(detnums) == NKEPT and all(x == 1 for x in detnums)
            and all(sum(detnums[t] for t in sol) == 24 for sol in SOLS)
            and len(CO_PAIRS) == 15168 and len(SEP_NORMALS) == 80 and separated)


CONTINUOUS_CUT_OK = continuous_cut_certificate(KEPT_DET, PAIR_SEPARATED)

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


def blockbasis_int(s):
    """The same character basis over the integers, with literal signs."""
    B = np.zeros((len(REPF), NPI), dtype=np.int64)
    for t, i0 in enumerate(REPF):
        for u in range(NFL):
            B[t, PERM[FLIPS[u]][i0]] = 1 if (popc(s & FW[u]) & 1) == 0 else -1
    return B


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
# 6. the four-part family, the all-signs deflation, and the graded meet
# ------------------------------------------------------------------

OUTI = [k for k in range(NORB) if k not in IORB]
TWINI = OUTI[:4]


def partsum(ks):
    """The entrywise sum of the orbit tables listed. Every member of the family,
    and both rejectors below, is built by this one path."""
    M = np.zeros((NCOV, NPI), dtype=np.int64)
    for k in ks:
        M = M + TAB[k]
    return M


def entset(X):
    return sorted(set(int(v) for v in X.reshape(-1)))


def rowset(X):
    return sorted(set(int(v) for v in X.sum(axis=1)))


def colset(X):
    return sorted(set(int(v) for v in X.sum(axis=0)))


def blockker(X, s, p):
    """A basis, in the twelve coefficients of the block of sign pattern s, of the
    part of the null space of X that lies inside that block."""
    return nullbasis(np.mod(np.dot(np.mod(X, p), blockbasis(s, p).T), p), p)


def meetdim(K1, K2, p):
    """dim K1 plus dim K2 minus the rank of the two stacked: the meet dimension."""
    if K1.shape[0] == 0 or K2.shape[0] == 0:
        return 0
    return K1.shape[0] + K2.shape[0] - rrank(np.vstack([K1, K2]), p)


def byweight(v):
    """The first value of each weight class, and whether the class is constant."""
    cls = [[v[s] for s in range(16) if WT[s] == w] for w in range(5)]
    return [c[0] for c in cls], all(len(set(c)) == 1 for c in cls)


def igcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a - b * (a // b)
    return a


def intker(H):
    """An integer basis of the null space of H by exact rational reduction, with
    denominators cleared and the content divided out. No floating point."""
    n = H.shape[1]
    A = [[FR(int(H[r][c])) for c in range(n)] for r in range(H.shape[0])]
    piv = []
    r = 0
    for c in range(n):
        q = -1
        for rr in range(r, len(A)):
            if A[rr][c] != 0:
                q = rr
                break
        if q < 0:
            continue
        A[r], A[q] = A[q], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for rr in range(len(A)):
            if rr != r and A[rr][c] != 0:
                f = A[rr][c]
                A[rr] = [A[rr][k] - f * A[r][k] for k in range(n)]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        v = [FR(0)] * n
        v[fc] = FR(1)
        for rr, pc in enumerate(piv):
            v[pc] = -A[rr][fc]
        den = 1
        for x in v:
            den = den * x.denominator // igcd(den, x.denominator)
        w = [int(x * den) for x in v]
        g = 0
        for x in w:
            g = igcd(g, x)
        if g:
            w = [x // g for x in w]
        out.append(w)
    return out


TWIN = partsum(TWINI)
ISUM4 = partsum(IORB)

# the partition of the all-ones table by the 96 orbit tables
TNZ = sorted(set(int(np.count_nonzero(TAB[k])) for k in range(NORB)))
OVLP = 0
for a in range(NORB):
    for b in range(a + 1, NORB):
        ov = int(np.count_nonzero(np.logical_and(TAB[a], TAB[b])))
        if ov > OVLP:
            OVLP = ov
TSUM = partsum(range(NORB))
ONES = np.ones((NCOV, NPI), dtype=np.int64)
FILL = NORB * TNZ[0]
NFAM = sum(1 for _ in itertools.combinations(range(NORB), 4))

IENT = entset(ISUM4)
IRS = rowset(ISUM4)
ICS = colset(ISUM4)
TWEN = entset(TWIN)
TWRS = rowset(TWIN)
TWCS = colset(TWIN)

RPT = partsum([IORB[0], IORB[0], IORB[1], IORB[2]])
RPE = entset(RPT)
RPR = rowset(RPT)
FIVEI = IORB + [OUTI[0]]
FIVE = partsum(FIVEI)
F5E = entset(FIVE)
F5R = rowset(FIVE)

COVKEY = set(frozenset(c) for c in CS)
ICV = sum(1 for j in range(NCOV)
          if frozenset(int(x) for x in np.nonzero(INC[j])[0]) in COVKEY)
TCV = sum(1 for j in range(NCOV)
          if frozenset(int(x) for x in np.nonzero(TWIN[j])[0]) in COVKEY)

# the all-signs block, and the kernel each single table has inside it
ALLS = [s for s in range(16) if WT[s] == 4][0]
ASD = rrank(blockbasis(ALLS, PRIME), PRIME)
TABK = sorted(set(blockker(TAB[k], ALLS, PRIME).shape[0] for k in range(NORB)))
ALLSB_INT = blockbasis_int(ALLS)
ALLS_INTEGER_OK = all(not TAB[k].dot(ALLSB_INT.T).any() for k in range(NORB))

HOLDI = all(np.array_equal(INC[list(CPERM[e])][:, list(PERM[e])], INC)
            for e in FLIPS)
HOLDT = all(np.array_equal(TWIN[list(CPERM[e])][:, list(PERM[e])], TWIN)
            for e in FLIPS)
HOLDFULLI = all(np.array_equal(INC[list(CPERM[e])][:, list(PERM[e])], INC)
                for e in range(NGRP))
HOLDFULLT = all(np.array_equal(TWIN[list(CPERM[e])][:, list(PERM[e])], TWIN)
                for e in range(NGRP))

BKI = {}
BKT = {}
KD1 = {}
KD2 = {}
KDM = {}
KP1 = {}
KC1 = {}
KP2 = {}
KC2 = {}
MP = {}
MC = {}
MT = {}
FULLM = {}
for q in (PRIME, PRIME2):
    BKI[q] = [blockker(INC, s, q) for s in range(16)]
    BKT[q] = [blockker(TWIN, s, q) for s in range(16)]
    KD1[q] = [B.shape[0] for B in BKI[q]]
    KD2[q] = [B.shape[0] for B in BKT[q]]
    KDM[q] = [meetdim(BKI[q][s], BKT[q][s], q) for s in range(16)]
    KP1[q], KC1[q] = byweight(KD1[q])
    KP2[q], KC2[q] = byweight(KD2[q])
    MP[q], MC[q] = byweight(KDM[q])
    MT[q] = wsum(MP[q])
    FULLM[q] = meetdim(nullbasis(INC, q), nullbasis(TWIN, q), q)

KIF = nullbasis(INC, PRIME)
KTF = nullbasis(TWIN, PRIME)
MEETF = FULLM[PRIME]
MEET4 = KDM[PRIME][ALLS]
EARN = MEETF - MEET4

ONLY = [KD1[PRIME][s] - KDM[PRIME][s] for s in range(16)]
OP, OC = byweight(ONLY)
OT = wsum(OP)


def wclass(w):
    """For every block of pattern weight w, in order: the two kernel dimensions,
    their meet, the rank of the two bases stacked, and the block dimension."""
    out = []
    for s in range(16):
        if WT[s] != w:
            continue
        st = rrank(np.vstack([BKI[PRIME][s], BKT[PRIME][s]]), PRIME)
        out.append((KD1[PRIME][s], KD2[PRIME][s], KDM[PRIME][s], st,
                    rrank(blockbasis(s, PRIME), PRIME)))
    return out


W3P = [s for s in range(16) if WT[s] == 3]
S1A = wclass(1)
S2A = wclass(2)
S3A = wclass(3)
S1T = sorted(set(S1A))
S2T = sorted(set(S2A))
S3T = sorted(set(S3A))

# the piece swap that destroys the hold of the flips
MSW = INC.copy()
MSW[:, [REPF[0], REPF[1]]] = MSW[:, [REPF[1], REPF[0]]]
HOLDN = sum(1 for e in FLIPS
            if np.array_equal(MSW[list(CPERM[e])][:, list(PERM[e])], MSW))
SWB = sum(blockker(MSW, s, PRIME).shape[0] for s in range(16))
SWK = NPI - rrank(MSW, PRIME)
INCB = sum(KD1[PRIME])
INCK = NPI - rrank(INC, PRIME)

# the weight zero reduction: flip orbits of covers, the quotient, and its halving
CSTB = sorted(set(sum(1 for e in FLIPS if CPERM[e][j] == j) for j in range(NCOV)))
CORB2 = []
CSEEN = [-1] * NCOV
for j in range(NCOV):
    if CSEEN[j] < 0:
        mem = sorted(set(CPERM[e][j] for e in FLIPS))
        for y in mem:
            CSEEN[y] = len(CORB2)
        CORB2.append(mem)
COSZ = sorted(set(len(o) for o in CORB2))
POSZ = sorted(set(len(o) for o in ORBF))
PIDX = [-1] * NPI
for t, o in enumerate(ORBF):
    for i in o:
        PIDX[i] = t


def quotient(X):
    """One row per cover orbit, taken at its first member, one column per piece
    orbit, entry the count of pieces of that orbit inside that cover."""
    Q = np.zeros((len(CORB2), len(ORBF)), dtype=np.int64)
    for a, co in enumerate(CORB2):
        j = co[0]
        for i in range(NPI):
            if X[j, i]:
                Q[a, PIDX[i]] += int(X[j, i])
    return Q


QI = quotient(INC)
QT = quotient(TWIN)
QUOTIENT_INPUT_OK = (QI.shape == (24, 12) and QT.shape == (24, 12)
                     and entset(QI) == [0, 2] and entset(QT) == [0, 2]
                     and not np.any(QI % 2) and not np.any(QT % 2))
if not QUOTIENT_INPUT_OK:
    raise ValueError("quotient entries must be exactly even before halving")
ROWI = [tuple(int(v) for v in QI[a]) for a in range(QI.shape[0])]
ROWT = [tuple(int(v) for v in QT[a]) for a in range(QT.shape[0])]
MULI = sorted(set(ROWI.count(r) for r in ROWI))
MULT = sorted(set(ROWT.count(r) for r in ROWT))
UNI = sorted(set(ROWI))
UNT = sorted(set(ROWT))
HI = np.array([[v // 2 for v in r] for r in UNI], dtype=np.int64)
HT = np.array([[v // 2 for v in r] for r in UNT], dtype=np.int64)
RKI = [rrank(HI, q) for q in (PRIME, PRIME2)]
RKT = [rrank(HT, q) for q in (PRIME, PRIME2)]

KBI = intker(HI)
KENT = sorted(set(x for v in KBI for x in v))
KSUP = [sorted(i for i, x in enumerate(v) if x) for v in KBI]
KFLAT = [i for s in KSUP for i in s]
KZERO = all(all(sum(int(HI[rr][c]) * v[c] for c in range(HI.shape[1])) == 0
                for rr in range(HI.shape[0])) for v in KBI)
KZERO_T = all(all(sum(int(HT[rr][c]) * v[c] for c in range(HT.shape[1])) == 0
                  for rr in range(HT.shape[0])) for v in KBI)
PM2 = sorted(set((v.count(1), v.count(-1)) for v in KBI))

NKI = nullbasis(HI, PRIME)
NKT = nullbasis(HT, PRIME)
NMEET = meetdim(NKI, NKT, PRIME)
HI24 = QI // 2
HT24 = QT // 2
AGR = sum(1 for a in range(len(CORB2)) if np.array_equal(HI24[a], HT24[a]))
MSI = sorted(tuple(int(v) for v in r) for r in HI24)
MST = sorted(tuple(int(v) for v in r) for r in HT24)

# how far apart the two are as tables
SHR = sorted(set(int(np.dot(INC[j], TWIN[j])) for j in range(NCOV)))
DIF = INC - TWIN
DE = entset(DIF)
DNZ = int(np.count_nonzero(DIF))
DPR = DNZ // NCOV
DPF, DCON, DTOT = profile(DIF, PRIME)

# the one swap sweep, at one prime
SWEEP = {}
NMEM = 0
KTOT = set()
MTOT = set()
MCONS = set()
KCONS = set()
MAS = set()
for drop in IORB:
    for add in range(NORB):
        if add in IORB:
            continue
        X = partsum([k for k in IORB if k != drop] + [add])
        bk = [blockker(X, s, PRIME) for s in range(16)]
        kd = [B.shape[0] for B in bk]
        md = [meetdim(BKI[PRIME][s], bk[s], PRIME) for s in range(16)]
        pk, ck = byweight(kd)
        pm, cm = byweight(md)
        tk = wsum(pk)
        tm = wsum(pm)
        key = (tuple(pk), tk, tuple(pm), tm)
        SWEEP[key] = SWEEP.get(key, 0) + 1
        NMEM += 1
        KTOT.add(tk)
        MTOT.add(tm)
        KCONS.add(ck)
        MCONS.add(cm)
        MAS.add(pm[4])

# a wider deterministic sample of the family, and its kernel at the first
# sign pattern of weight three
SAMP = []
for drop in IORB:
    for add in range(NORB):
        if add not in IORB:
            SAMP.append([k for k in IORB if k != drop] + [add])
NSWAP = len(SAMP)
NDISJ = len(OUTI) // 4
for t in range(NDISJ):
    SAMP.append(OUTI[4 * t:4 * t + 4])
BASE4 = IORB[:2] + OUTI[:6]
NSUB = 0
for c in itertools.combinations(BASE4, 4):
    SAMP.append(list(c))
    NSUB += 1
UNIQ = sorted(set(tuple(sorted(m)) for m in SAMP))
NSAMP = len(UNIQ)

S3F = W3P[0]
KI3 = BKI[PRIME][S3F]
KT3 = BKT[PRIME][S3F]
CI3 = rref_modp(KI3, PRIME)[0].tobytes()
CT3 = rref_modp(KT3, PRIME)[0].tobytes()
HST = {}
CAN = {}
CDM = {}
SIX = 0
TRANS = 0
for m in UNIQ:
    K = blockker(partsum(m), S3F, PRIME)
    d = K.shape[0]
    HST[d] = HST.get(d, 0) + 1
    cb = rref_modp(K, PRIME)[0].tobytes()
    CAN[cb] = CAN.get(cb, 0) + 1
    CDM[cb] = d
    if d == 6:
        SIX += 1
        if meetdim(KI3, K, PRIME) == 0:
            TRANS += 1
HDIM = sorted(HST)
HCNT = [HST[d] for d in HDIM]
NDIS = len(CAN)
NDS6 = sum(1 for c in CAN if CDM[c] == 6)
MAXM = max(CAN.values())
INCR = CAN.get(CI3, 0)
TWNR = CAN.get(CT3, 0)


# ------------------------------------------------------------------
# 6b. production predicates and targeted one-fault mutations
# ------------------------------------------------------------------


def orbit_table_certificate(tables):
    if len(tables) != 96:
        return False
    if any(entset(M) != [0, 1] or rowset(M) != [2] or colset(M) != [2]
           for M in tables):
        return False
    return np.array_equal(sum(tables), ONES)


def allsign_certificate(tables, basis):
    return all(not M.dot(basis.T).any() for M in tables)


def rank_meet_certificate(X, Y):
    for q in (PRIME, PRIME2):
        kx = nullbasis(X, q)
        ky = nullbasis(Y, q)
        if kx.shape[0] != 87 or ky.shape[0] != 87 or meetdim(kx, ky, q) != 33:
            return False
    return True


def quotient_certificate(Q):
    if Q.shape != (24, 12) or entset(Q) != [0, 2] or np.any(Q % 2):
        return False
    rows = [tuple(int(v) for v in Q[a]) for a in range(Q.shape[0])]
    uniq = sorted(set(rows))
    if len(uniq) != 12 or sorted(set(rows.count(r) for r in rows)) != [2]:
        return False
    half = np.array([[v // 2 for v in r] for r in uniq], dtype=np.int64)
    return entset(half) == [0, 1] and rowset(half) == [4] and colset(half) == [4]


def selector_certificate(sel):
    return (sel == [k for k in range(NORB) if k not in IORB][:4]
            and len(sel) == len(set(sel)) == 4 and not set(sel) & set(IORB))


def sample_certificate(raw, unique, canon):
    dup = sorted((m, n) for m, n in
                 ((m, raw.count(m)) for m in sorted(set(raw))) if n > 1)
    return (len(raw) == 461 and len(unique) == 460
            and dup == [(tuple(TWINI), 2)]
            and len(canon) == 130 and max(canon.values()) == 27
            and canon.get(CI3, 0) == 13 and canon.get(CT3, 0) == 2)


OBJECT_CERT_OK = (MASK_VISIBLE and SOLS_UNIQUE and MASK_SEARCH_OK and VOLUME_OK
                  and CONTINUOUS_CUT_OK)
ORBIT_TABLE_OK = orbit_table_certificate(TAB)
RANK_MEET_OK = rank_meet_certificate(INC, TWIN)
QUOTIENT_OK = quotient_certificate(QI) and quotient_certificate(QT)
SELECTOR_OK = selector_certificate(TWINI)
SAMPLE_OK = sample_certificate([tuple(sorted(m)) for m in SAMP], UNIQ, CAN)

BAD_MASKS = list(MASK)
BAD_MASKS[0] = 0
MUT_MASK = not mask_search_certificate(BAD_MASKS, SOLS)
BAD_DETS = list(KEPT_DET)
BAD_DETS[0] = 2
MUT_GEOMETRY = not continuous_cut_certificate(BAD_DETS, PAIR_SEPARATED)
BAD_TABLES = list(TAB)
BAD_TABLES[0] = TAB[0].copy()
BAD_TABLES[0][0, 0] ^= 1
MUT_ORBIT = not orbit_table_certificate(BAD_TABLES)
BAD_ALLS = ALLSB_INT.copy()
BAD_ALLS[0, 0] *= -1
MUT_ALLSIGN = not allsign_certificate(TAB, BAD_ALLS)
BAD_INC = INC.copy()
BAD_INC[0, 0] ^= 1
MUT_RANK_MEET = not rank_meet_certificate(BAD_INC, TWIN)
BAD_QT = QT.copy()
BAD_QT[0, 0] = 1
MUT_QUOTIENT = not quotient_certificate(BAD_QT)
MUT_SELECTOR = not selector_certificate(OUTI[1:5])
BAD_SAMPLE = [tuple(sorted(m)) for m in SAMP] + [tuple(TWINI)]
MUT_SAMPLE_DUP = not sample_certificate(BAD_SAMPLE, UNIQ, CAN)
BAD_CAN = dict(CAN)
BAD_CAN[CI3] = BAD_CAN[CI3] + 1
MUT_SAMPLE_CANON = not sample_certificate([tuple(sorted(m)) for m in SAMP], UNIQ, BAD_CAN)
MUT_PRIME = not is_prime(PRIME + 2)
MUT_REPEAT = not (entset(RPT) == [0, 1] and rowset(RPT) == [8] and colset(RPT) == [8])
MUT_FIFTH = not (entset(FIVE) == [0, 1] and rowset(FIVE) == [8] and colset(FIVE) == [8])
MUT_BLOCK = HOLDN != NFL or SWB != SWK
MUTATIONS = [MUT_MASK, MUT_GEOMETRY, MUT_ORBIT, MUT_ALLSIGN, MUT_RANK_MEET,
             MUT_QUOTIENT, MUT_SELECTOR, MUT_SAMPLE_DUP, MUT_SAMPLE_CANON,
             MUT_PRIME, MUT_REPEAT, MUT_FIFTH, MUT_BLOCK]

# ------------------------------------------------------------------
# 7. the gates
# ------------------------------------------------------------------

NSLOT = NS * SIZES[0]
NSLOT2 = NPI * PCSET[0]
gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and PCSET == [1975] and GENERIC
     and NSLOT == 379200 and NSLOT2 == 379200 and MASK_SEARCH_OK, "E0",
     "the cell has {0} unit-determinant subsets, {1} at cost floor {2}, {3} cuttings of {4}, {5} pieces in {6} each, {7} slots both ways".format(
         nd(NCAND), nd(NKEPT), nd(FLOOR), nd(NS), nd(SIZES[0]), nd(NPI),
         nd(PCSET[0]), nd(NSLOT)))

gate(OBJECT_CERT_OK and len(CO_PAIRS) == 15168 and len(SEP_NORMALS) == 80,
     "E0G", "exact masks, 24 unit volumes, and {0} co-occurring pairs with {1} integer normals certify continuous cuttings".format(
         nd(len(CO_PAIRS)), nd(len(SEP_NORMALS))))

gate(NCOV == 192 and BRS == [8] and COVEXACT
     and BRS[0] * PCSET[0] == NS, "E1",
     "the {0} covers hold {1} pieces each and meet every cutting exactly once, and {1} times {2} is the cutting count {3}".format(
         nd(NCOV), nd(BRS[0]), nd(PCSET[0]), nd(NS)))

gate(NGRP == 384 and GDISTINCT and CLOSED and KEEPS and COVKEEP and PBIJ and PDIST
     and PIDOK and CBIJ and CDIST and len(ORBP) == NPI and len(ORBC) == NCOV
     and NPAIR == 36864 and FSTAB == set([1]) and NORB == 96 and OSZ == [384], "E2",
     "the {0} maps close under composition, act transitively on pieces and covers, and freely on the {1} pairs: {2} orbits of {0}".format(
         nd(NGRP), nd(NPAIR), nd(NORB)))

FSUB = all(COMP[a][b] in FLIPS for a in FLIPS for b in FLIPS)
BDIM = sorted(set(rrank(blockbasis(s, q), q)
                  for s in range(16) for q in (PRIME, PRIME2)))
BSTK = [rrank(np.vstack([blockbasis(s, q) for s in range(16)]), q)
        for q in (PRIME, PRIME2)]
gate(FIELDS_OK and NFL == 16 and FSUB and FLPFREE and AXOK and len(REPF) == 12
     and sorted(set(len(o) for o in ORBF)) == [16] and BDIM == [12]
     and BSTK == [192, 192], "E3",
     ("the {0} flips form a subgroup free on the {1} pieces with {2} orbits; "
      "each block has dimension {2}, and all {0} stack to {1}, both primes").format(
         nd(NFL), nd(NPI), nd(len(REPF))))

gate(TNZ == [384] and OVLP == 0 and np.array_equal(TSUM, ONES)
     and FILL == NCOV * NPI and FILL == 36864 and TRS == {2} and TCS == {2}
     and ORBIT_TABLE_OK, "E4",
     "the {0} disjoint orbit tables partition all pairs and each has row/column fibres {1}; every table has {2} entries".format(
         nd(NORB), nd(sorted(TRS)), nd(TNZ[0])))

gate(IENT == [0, 1] and TWEN == [0, 1] and IRS == [8] and TWRS == [8]
     and ICS == [8] and TWCS == [8] and NFAM == 3321960 and len(IORB) == 4
     and len(TWINI) == 4 and np.array_equal(INC, ISUM4)
     and np.array_equal(ISUM, ISUM4) and SELECTOR_OK, "E5",
     "incidence and twin, each a sum of {0} tables, have entry set {1}, row sums {2} and column sums {3}; the family has {4} members".format(
         nd(len(IORB)), nd(IENT), nd(IRS[0]), nd(ICS[0]), nd(NFAM)))

gate(2 in RPE and RPE != [0, 1] and RPR == [8] and len(RPE) == 3, "E6",
     "mutation witness: repeating one of {2} selected tables changes the entry set to {0} while row sums remain {1}".format(
         nd(RPE), nd(RPR[0]), nd(len(IORB))))

gate(F5E == [0, 1] and F5R == [10] and F5R != IRS and len(FIVEI) == 5
     and len(set(FIVEI)) == 5, "E7",
     ("mutation witness: a sum of {0} distinct tables stays binary and changes "
      "the row sum from {2} to {1}; four-table selection fixes regularity").format(
         nd(len(FIVEI)), nd(F5R[0]), nd(IRS[0]), nd(len(IORB))))

gate(ICV == NCOV and TCV == 0 and TWEN == [0, 1] and TWRS == [8], "E8",
     "cover-row census in the two binary {2}-regular members: incidence {0} of {0}, comparison {1} of {0}".format(
         nd(NCOV), nd(TCV), nd(TWRS[0])))

gate(TABK == [12] and ASD == 12 and TABK[0] == ASD and len(TABK) == 1
     and ALLS_INTEGER_OK and allsign_certificate(TAB, ALLSB_INT), "E9",
     ("every one of the {0} tables annihilates the whole all-signs block: the "
      "per-table kernel dimensions there are {1}, the block dimension {2}").format(
         nd(NORB), nd(TABK), nd(ASD)))

gate(MEET4 == 12 and MEETF == 33 and EARN == 21 and MEET4 + EARN == MEETF
     and KIF.shape[0] == 87 and KTF.shape[0] == 87, "E10",
     "over F_{3}, the {0}-dimensional integer all-signs block lies in the {1}-dimensional meet; the complementary contribution is {2}".format(
         nd(MEET4), nd(MEETF), nd(EARN), nd(PRIME)))

gate(HOLDI and HOLDT and HOLDFULLI and HOLDFULLT
     and KP1[PRIME] == [3, 3, 6, 6, 12]
     and KP1[PRIME2] == [3, 3, 6, 6, 12] and KP2[PRIME] == [3, 3, 6, 6, 12]
     and KP2[PRIME2] == [3, 3, 6, 6, 12] and KC1[PRIME] and KC1[PRIME2]
     and KC2[PRIME] and KC2[PRIME2]
     and [wsum(KP1[q]) for q in (PRIME, PRIME2)] == [87, 87]
     and [wsum(KP2[q]) for q in (PRIME, PRIME2)] == [87, 87], "E11",
     "both members are held by all signed coordinate maps; odd-field character dimensions {1} recompose to {2} at both primes".format(
         nd(NFL), nd(KP1[PRIME]), nd(wsum(KP1[PRIME]))))

gate(MP[PRIME] == [3, 0, 3, 0, 12] and MP[PRIME2] == [3, 0, 3, 0, 12]
     and MC[PRIME] and MC[PRIME2] and MT[PRIME] == 33 and MT[PRIME2] == 33
     and FULLM[PRIME] == MT[PRIME] and FULLM[PRIME2] == MT[PRIME2]
     and RANK_MEET_OK, "E12",
     "the meet profile is {0} by character weight and recomposes to full-space meet {1} over both named prime fields".format(
         nd(MP[PRIME]), nd(MT[PRIME]), nd(NPI)))

gate(OP == [0, 3, 3, 6, 0] and OC and OT == 54
     and OT + MT[PRIME] == KIF.shape[0], "E13",
     "over F_{4}, incidence-only block dimensions are {0}, totaling {1}; with meet {2}, {1}+{2}={3}".format(
         nd(OP), nd(OT), nd(MT[PRIME]), nd(OT + MT[PRIME]), nd(PRIME)))

gate(len(S3A) == 4 and len(W3P) == 4 and S3T == [(6, 6, 0, 12, 12)]
     and len(S3T) == 1 and HOLDFULLI and HOLDFULLT, "E14",
     ("over F_{6}, all {0} weight-{1} blocks have kernel pair {2}/{2}, meet {3}, stack rank "
      "{4}/{5}; coordinate permutations carry the class").format(
         nd(len(S3A)), nd(3), nd(S3T[0][0]), nd(S3T[0][2]), nd(S3T[0][3]),
         nd(S3T[0][4]), nd(PRIME)))

gate(S1T == [(3, 3, 0, 6, 12)] and S2T == [(6, 6, 3, 9, 12)]
     and len(S1T) == 1 and len(S2T) == 1, "E15",
     ("over F_{7}: weight-{0} stack rank {1}/{2}, meet {3}; weight-{4} meet "
      "{5}/{6}; separation is at odd weight").format(
         nd(1), nd(S1T[0][3]), nd(S1T[0][4]), nd(S1T[0][2]), nd(2),
         nd(S2T[0][2]), nd(S2T[0][0]), nd(PRIME)))

gate(HOLDN == 1 and SWB != SWK and INCB == INCK and INCK == 87
     and SWK == 87, "E16",
     ("over F_{6}, swap mutation holds {0}/{1} flips, block sum {2} differs from kernel "
      "{3}; incidence block/full {4}/{5}").format(
         nd(HOLDN), nd(NFL), nd(SWB), nd(SWK), nd(INCB), nd(INCK), nd(PRIME)))

gate(CSTB == [2] and len(CORB2) == 24 and COSZ == [8] and len(ORBF) == 12
     and POSZ == [16] and len(CORB2) * COSZ[0] == NCOV
     and len(ORBF) * POSZ[0] == NPI, "E17",
     "every cover has flip stabiliser of order {0}, giving {1} orbits of {2}; the {3} piece orbits have size {4}, and {1} times {2} is {5}".format(
         nd(CSTB[0]), nd(len(CORB2)), nd(COSZ[0]), nd(len(ORBF)), nd(POSZ[0]),
         nd(NCOV)))

gate(QUOTIENT_INPUT_OK and QI.shape == (24, 12) and entset(QI) == [0, 2] and rowset(QI) == [8]
     and colset(QI) == [16] and len(UNI) == 12 and MULI == [2], "E18",
     "the orbit quotient is {0} by {1} with entry set {2}, row sums {3}, column sums {4}, and {1} distinct rows each occurring {5} times".format(
         nd(QI.shape[0]), nd(QI.shape[1]), nd(entset(QI)), nd(rowset(QI)[0]),
         nd(colset(QI)[0]), nd(MULI[0])))

gate(HI.shape == (12, 12) and entset(HI) == [0, 1] and rowset(HI) == [4]
     and colset(HI) == [4] and RKI == [9, 9] and HI.shape[1] - RKI[0] == 3, "E19",
     "halving those rows gives a {0} by {0} zero-one table, {1} regular in rows and columns, of rank {2} at both primes and corank {3}".format(
         nd(HI.shape[0]), nd(rowset(HI)[0]), nd(RKI[0]), nd(HI.shape[1] - RKI[0])))

gate(len(KBI) == 3 and KENT == [-1, 0, 1] and [len(s) for s in KSUP] == [4, 4, 4]
     and len(KFLAT) == len(set(KFLAT)) and sorted(KFLAT) == list(range(12))
     and PM2 == [(2, 2)] and KZERO and KZERO_T, "E20",
     ("{0} integer vectors, entries {1}, disjoint size-{2} supports, partition "
      "{3} piece orbits and annihilate both halved quotients").format(
         nd(len(KBI)), nd(KENT), nd(len(KSUP[0])), nd(len(KFLAT)),
         nd(PM2[0][0])))

gate(len(UNT) == 12 and MULT == [2] and entset(HT) == [0, 1]
     and rowset(HT) == [4] and RKT == [9, 9] and HT.shape[1] - RKT[0] == 3
     and NKI.shape[0] == 3 and NKT.shape[0] == 3 and NMEET == 3
     and QUOTIENT_OK, "E21",
     "over F_{2}, twin halved rank/corank {0}/{1}; its and incidence's {1}-nullspaces meet in dimension {1} and coincide".format(
         nd(RKT[0]), nd(HT.shape[1] - RKT[0]), nd(PRIME)))

gate(not np.array_equal(HI24, HT24) and AGR == 0 and MSI != MST
     and not np.array_equal(HI, HT) and NMEET == 3, "E22",
     ("the halved quotients are distinct with {0} of {1} rows equal in place and "
      "different row multisets; their named-field null spaces coincide").format(
         nd(AGR), nd(len(CORB2))))

gate(SHR == [0] and len(SHR) == 1, "E23",
     "the incidence row and the twin row share {0} pieces in every one of the {1} rows".format(
         nd(SHR[0]), nd(NCOV)))

gate(DE == [-1, 0, 1] and DNZ == 3072 and DNZ == NCOV * 16 and DPR == 16, "E24",
     "the difference of the two has entry set {0} and {1} nonzero entries, which is {2} times {3}".format(
         nd(DE), nd(DNZ), nd(NCOV), nd(DPR)))

gate(DPF == [6, 9, 6, 6, 0] and DCON and wsum(DPF) == 102 and DTOT == 102
     and DPF[4] == 0, "E25",
     "over F_{2}, difference ranks by weight are {0}, class-constant, total {1}, zero on the all-signs block".format(
         nd(DPF), nd(wsum(DPF)), nd(PRIME)))

gate(NMEM == 368 and len(SWEEP) == 185 and min(KTOT) == 48 and max(KTOT) == 120
     and MCONS == set([True]) and MAS == set([12]), "E26",
     "over F_{5}, the {0}-member one-swap sweep has {1} signatures, kernel totals {2}..{3}, all-signs meet entry {4}".format(
         nd(NMEM), nd(len(SWEEP)), nd(min(KTOT)), nd(max(KTOT)),
         nd(sorted(MAS)[0]), nd(PRIME)))

gate(min(MTOT) == 12 and max(MTOT) == 59 and NMEM == 368 and NFAM == 3321960, "E27",
     "over F_{5}, the declared {3}-member one-swap sweep has meet totals {0}..{1}; full family size {4}".format(
         nd(min(MTOT)), nd(max(MTOT)), nd(KIF.shape[0]), nd(NMEM), nd(NFAM), nd(PRIME)))

gate(NSAMP == 460 and NSWAP == 368 and NDISJ == 23 and NSUB == 70
     and HDIM == [6, 7, 9, 12] and HCNT == [366, 55, 37, 2] and SIX == 366
     and TRANS == 169 and SAMPLE_OK, "E28",
     ("over F_{4}, the sample has {0}/{1} dimension-{3} selected weight-{2} kernels "
      "transverse to incidence").format(
         nd(TRANS), nd(SIX), nd(3), nd(HDIM[0]), nd(PRIME)))

gate(NDIS == 130 and NDS6 == 103 and MAXM == 27 and NDIS < NSAMP
     and NDS6 < SIX and MAXM > 1, "E29",
     ("over F_{9}, the {0}-member sample realises {4} selected weight-{5} kernels; "
      "{6} have dimension {7}, maximum multiplicity {8}").format(
         nd(NSAMP), nd(NSWAP), nd(NDISJ), nd(NSUB), nd(NDIS), nd(3), nd(NDS6),
         nd(HDIM[0]), nd(MAXM), nd(PRIME)))

gate(INCR == 13 and TWNR == 2 and CI3 != CT3 and INCR > 1 and TWNR > 1
     and INCR < NSAMP, "E30",
     ("over F_{4}, selected weight-{0} kernel multiplicities in the {2}-member sample: "
      "incidence {1}, comparison {3}; kernels distinct").format(
         nd(3), nd(INCR), nd(NSAMP), nd(TWNR), nd(PRIME)))

gate(len(MUTATIONS) == 13 and all(MUTATIONS), "E31",
     "all {0} targeted mutations are rejected: masks, geometry, orbit fibres, signs, ranks, quotient, selectors, sample, fields, and family".format(
         nd(len(MUTATIONS))))

emit("the {0} tables give {1} four-part sums; the named-field meet {3} contains the {2}-dimensional integer all-signs block, profile {4}".format(
    nd(NORB), nd(NFAM), nd(MEET4), nd(MEETF), nd(MP[PRIME])))
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
MBS = RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RSS / 1024.0
emit("elapsed {0} s, peak resident {1} MB".format(nd(int(time.time() - T0)), nd(int(MBS))))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
sys.exit(0 if STAT[1] == 0 else 1)
