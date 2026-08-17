"""Finite cell cutting: the row-transversal census is the normalizer index 48,
with two central relabellings realized by signed coordinate maps.

Standalone exact runner for a supplied finite model. The preamble rebuilds the
unit four-cube vertices; the determinant-one simplices at the declared
adjacency-cost minimum; 15800 exact 24-simplex cuttings; 192 pieces; 192
eight-piece transversals of the cutting family; 384 signed coordinate maps;
and 96 orbit tables on the 36864 piece-transversal pairs. The orbit tables are
pairwise disjoint and sum to the all-ones table, so the incidence is one of
3321960 four-table members. Requiring every row to equal a transversal leaves
48 members. Their row maps are the 48 right actions of N_G(H)/H, where the
point stabilizer H has order 2 and its normalizer has order 96. Exactly two row
maps are also signed-coordinate actions; they are the order-two centre.

Gates: G0F fields, G0 finite object, G0a exact tiling geometry, G1 family, G2
faithful group actions, G3 stabilizer and cosets, G4 normalizer and centre, G5
normalizer structure, G6-G14 row relabellings and census, G15-G22 partner,
profile, label and character identities, G23 the complete relabelling group
table/action, G24 the finite ladder, and G25 the final positive control counts.
All work is exact over the integers and the two declared prime fields; no
floating point enters a gate. Output is one line per gate, one resource line,
and the total line."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

AUDIT_TIMEOUT_SEC = 300

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


def is_prime(n):
    """Deterministic trial-division certificate for the declared moduli."""
    if n < 2 or n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


FIELDS_OK = (PRIME == 1000003 and PRIME2 == 1000033 and PRIME != PRIME2
             and is_prime(PRIME) and is_prime(PRIME2))
gate(FIELDS_OK, "G0F",
     "the declared moduli {0} and {1} are distinct primes".format(
         nd(PRIME), nd(PRIME2)))
if not FIELDS_OK:
    emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
    sys.exit(1)


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

# The generic sample makes the candidate-cutting enumeration exhaustive. This
# independent exact certificate proves that every selected 24-tuple is a
# geometric cutting. Every pair of simplices that co-occurs in a cutting has a
# weak separating normal in {-1,0,1}^4. Full dimensionality makes their
# interiors strictly disjoint, while 24 determinant-one volumes sum to one.
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

# cuttings through each piece, as a bit set over cuttings
PC = [0] * NPI
for k, s in enumerate(CUT):
    for i in s:
        PC[i] |= (1 << k)
PCN = [popc(x) for x in PC]
FULLC = (1 << NS) - 1
PCSET = sorted(set(PCN))

# ------------------------------------------------------------------
# 1d. the transversals: eight pieces, pairwise never in a common cutting
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

# every transversal meets every cutting exactly once
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

# induced action on the transversals
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

# the transversal incidence, its orbits, and the split by the two labels
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
    and each specified partner variant is built by this one path."""
    M = np.zeros((NCOV, NPI), dtype=np.int64)
    for k in ks:
        M = M + TAB[k]
    return M


def blk(X, s, p):
    """X cut down to the block of sign pattern s: transversals by twelve."""
    return np.mod(np.dot(np.mod(X, p), blockbasis(s, p).T), p)


def imkey(B, p):
    """A canonical form of the image of a block restriction inside the transversal
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
    """The basis of the transversal-side block of sign pattern s: one vector per
    flip orbit of transversals whose stabiliser carries the sign plus one at s, an orbit
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
# 11. the gates: the object and the family, replayed
# ------------------------------------------------------------------

gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and PCSET == [1975] and GENERIC
     and NSLOT == 379200 and NSLOT2 == NSLOT and NCOV == 192 and BRS == [8]
     and COVEXACT, "G0",
     "{0} unit-determinant subsets, {1} at cost floor {2}, {3} cuttings of {4}, {5} pieces in {6} each, {7} slots, {5} transversals of {8}".format(
         nd(NCAND), nd(NKEPT), nd(FLOOR), nd(NS), nd(SIZES[0]), nd(NPI),
         nd(PCSET[0]), nd(NSLOT), nd(BRS[0])))

gate(len(CO_PAIRS) == 15168 and len(SEP_NORMALS) == 80 and PAIR_SEPARATED,
     "G0a",
     "all {0} co-occurring simplex pairs have an exact separator among {1} signed ternary normals; the 24 volumes tile the cell".format(
         nd(len(CO_PAIRS)), nd(len(SEP_NORMALS))))

gate(NORB == 96 and TNZ == [384] and OVLP == 0 and np.array_equal(TSUM, ONES)
     and FILL == NCOV * NPI and FILL == 36864 and NFAM == 3321960
     and IRC == [[0, 1], [8], [8]] and TRC == [[0, 1], [8], [8]]
     and np.array_equal(INC, INCS) and len(IPARTS) == 4
     and TRS == set([2]) and TCS == set([2]), "G1",
     "{0} tables of {1} entries, pairwise disjoint, summing to the all-ones table ({2}); {3} members, the incidence one of them".format(
         nd(NORB), nd(TNZ[0]), nd(FILL), nd(NFAM)))

# ------------------------------------------------------------------
# 12. the group table, the stabilizer of a transversal, and its normalizer
# ------------------------------------------------------------------

PA = [np.asarray(p, dtype=np.int64) for p in PERM]
CA = [np.asarray(q, dtype=np.int64) for q in CPERM]
PMAT = np.array(PERM, dtype=np.int64)
CMAT = np.array(CPERM, dtype=np.int64)
PIDX = dict((PA[e].tobytes(), e) for e in range(NGRP))
MUL = []
CLOSN = 0
for e in range(NGRP):
    row = [PIDX.get(r.tobytes(), -1) for r in PA[e][PMAT]]
    CLOSN += row.count(-1)
    MUL.append(row)
ID = PIDX[np.arange(NPI, dtype=np.int64).tobytes()]
INVE = [0] * NGRP
for e in range(NGRP):
    for f in range(NGRP):
        if MUL[e][f] == ID:
            INVE[e] = f
            break
IDOK = all(MUL[e][ID] == e and MUL[ID][e] == e for e in range(NGRP))
INVOK = all(MUL[e][INVE[e]] == ID and MUL[INVE[e]][e] == ID
            for e in range(NGRP))

# the transversal action against the piece action, on every 384 x 384 pair
HPAIR = 0
HMISS = 0
for e in range(NGRP):
    LH = CMAT[np.asarray(MUL[e], dtype=np.int64)]
    RH = CA[e][CMAT]
    HPAIR += NGRP
    HMISS += int(np.count_nonzero((LH != RH).any(axis=1)))
TRANS = len(set(int(CA[e][0]) for e in range(NGRP)))

gate(CLOSN == 0 and IDOK and INVOK and HMISS == 0 and TRANS == NCOV
     and HPAIR == NGRP * NGRP and HPAIR == 147456
     and GDISTINCT and CLOSED and KEEPS and PBIJ and PDIST and PIDOK
     and COVKEEP and CBIJ and CDIST and AXOK, "G2",
     "the {0} maps give faithful piece/transversal actions; {1} action pairs have {2} misses; the transversal orbit has {3} members".format(
         nd(NGRP), nd(HPAIR), nd(HMISS), nd(TRANS)))

H = [e for e in range(NGRP) if int(CA[e][0]) == 0]
HNID = [e for e in H if e != ID]
h0 = HNID[0] if HNID else ID
HIX = FLIPS.index(h0) if h0 in FLIPS else -1
HMASK = FW[HIX] if HIX >= 0 else 0
AX0 = HMASK.bit_length() - 1
STO = sorted(set(sum(1 for e in range(NGRP) if int(CA[e][c]) == c)
                 for c in range(NCOV)))
GC = [-1] * NCOV
GC2 = [-1] * NCOV
for e in range(NGRP):
    c = int(CA[e][0])
    if GC[c] < 0:
        GC[c] = e
    GC2[c] = e
GCOK = (min(GC) >= 0 and min(GC2) >= 0)
GCH = sum(1 for c in range(NCOV)
          if GC[c] != GC2[c] and MUL[GC[c]][h0] == GC2[c])

gate(len(H) == 2 and HIX >= 0 and popc(HMASK) == 1 and STO == [2] and GCOK
     and GCH == NCOV and AX0 >= 0, "G3",
     "each transversal has stabilizer {0}, generated at the base by axis-{1} flip; all {2} coset fibres have size two".format(
         nd(len(H)), nd(AX0), nd(GCH)))

NHS = set(e for e in range(NGRP)
          if set(MUL[MUL[e][h]][INVE[e]] for h in H) == set(H))
NH = sorted(NHS)
CHC = sorted(e for e in range(NGRP) if MUL[e][h0] == MUL[h0][e])
CENT = [e for e in range(NGRP)
        if all(MUL[e][f] == MUL[f][e] for f in range(NGRP))]
# DESC carries, for each map index, the axis move and the sign mask the preamble
# built it from; AXM re-reads the axis move off the corner map, so the two agree.
AXP = [DESC[e][0] for e in range(NGRP)]
SGN = [DESC[e][1] for e in range(NGRP)]
AXCON = all(AXM[e][AXP[e][r]] == r for e in range(NGRP) for r in range(4))
AFIX = sorted(e for e in range(NGRP) if AXP[e][AX0] == AX0)
NAXP = len(set(AXP[e] for e in NH))
NSGN = len(set(SGN[e] for e in NH))
FCL = [e for e in CENT if e != ID]
FC = FCL[0] if FCL else ID

gate(len(NH) == 96 and NH == CHC and NH == AFIX and NAXP == 6 and NSGN == 16
     and NAXP * NSGN == len(NH) and len(CENT) == 2 and set(CENT) <= NHS
     and AXCON and SGN[FC] == 15 and AXP[FC] == (0, 1, 2, 3), "G4",
     "the normalizer of the holder is the centralizer of its flip: {0} maps"
     " = {1} axis moves fixing axis {2} times {3} masks; centre {4}, its flip all axes".format(
         nd(len(NH)), nd(NAXP), nd(AX0), nd(NSGN), nd(len(CENT))))

ORD = {}
for e in NH:
    x = e
    o = 1
    while x != ID:
        x = MUL[x][e]
        o += 1
    ORD[e] = o
NHORD = sorted(set(ORD.values()))
NHAB = all(MUL[a][b] == MUL[b][a] for a in NH for b in NH)

gate((not NHAB) and NHORD == [1, 2, 3, 4, 6] and set(CENT) <= NHS
     and len(ORD) == len(NH), "G5",
     "the normalizer is noncommutative with element orders {0}; the centre lies inside it".format(
         sl(NHORD)))

# ------------------------------------------------------------------
# 13. the equivariant relabellings of the transversals and their images
# ------------------------------------------------------------------


def sigma(n, base):
    """The transversal relabelling by right multiplication by n, read through a
    choice of one map per transversal."""
    return tuple(int(CA[MUL[base[c]][n]][0]) for c in range(NCOV))


SIG = {}
for n in NH:
    SIG.setdefault(sigma(n, GC), []).append(n)
SKEY = sorted(SIG)
SBIJ = all(len(set(k)) == NCOV for k in SKEY)
SFIB = sorted(set(len(SIG[k]) for k in SKEY))
WDEF = sum(1 for n in NH if sigma(n, GC) == sigma(n, GC2))

gate(len(SIG) == 48 and SBIJ and SFIB == [2] and WDEF == len(NH)
     and len(NH) == 96 and WDEF == 96, "G6",
     "right multiplication by the normalizer gives {0} relabellings of the"
     " transversals, each a bijection from {1} maps; {2} of {3} choice independent".format(
         nd(len(SIG)), nd(SFIB[0]), nd(WDEF), nd(len(NH))))

OUTG = [e for e in range(NGRP) if e not in NHS]
RJ = sum(1 for e in OUTG if sigma(e, GC) == sigma(e, GC2))

gate(len(OUTG) == 288 and RJ == 0 and len(OUTG) + len(NH) == NGRP, "G7",
     "the normalizer supplies every choice-independent right action; among the"
     " other {1} maps the representative-independent count is {0}".format(
         nd(RJ), nd(len(OUTG))))


def decomp(B):
    """The tables are pairwise disjoint and sum to the all-ones table, so each
    table is either wholly inside B or meets it in a part it cannot fill; this
    single pass is therefore exact and free of any order choice."""
    left = B.copy()
    got = []
    for k in range(NORB):
        if bool(np.all(left >= TAB[k])):
            got.append(k)
            left = left - TAB[k]
    return tuple(got) if (len(got) == 4 and not left.any()) else None


MEM = {}
for k in SKEY:
    MEM[k] = decomp(INC[list(k), :])
EQSET = set(v for v in MEM.values() if v is not None)
DECN = sum(1 for k in SKEY if MEM[k] is not None)

gate(DECN == 48 and len(EQSET) == 48 and len(SKEY) == 48
     and tuple(IPARTS) in EQSET, "G8",
     "each of the {0} relabellings sends the incidence to a sum of four tables, all {0} of them distinct, the incidence itself among them".format(
         nd(DECN)))

# ------------------------------------------------------------------
# 14. the brute-force census of members whose rows are transversals
# ------------------------------------------------------------------

# Row c of the member built from a 4-set of tables equals transversal d exactly
# when the tables owning its eight pieces, read off row c, are four tables each hit
# twice; intersecting that over the 192 rows leaves the members all of whose rows
# are transversals. This computation is independent of the normalizer census.
OWN = np.zeros((NCOV, NPI), dtype=np.int64)
for k in range(NORB):
    OWN[TAB[k] == 1] = k
COV = [np.nonzero(INC[c])[0].tolist() for c in range(NCOV)]
ANS = None
for c in range(NCOV):
    g = set()
    for d in range(NCOV):
        cnt = {}
        for k in OWN[c][COV[d]].tolist():
            cnt[k] = cnt.get(k, 0) + 1
        if len(cnt) == 4 and set(cnt.values()) == set([2]):
            g.add(tuple(sorted(cnt)))
    ANS = g if ANS is None else (ANS & g)
ANSL = sorted(ANS)

gate(len(ANS) == 48 and len(ANSL) == len(ANS) and tuple(IPARTS) in ANS, "G9",
     "the census over all {0} rows of the {1} members leaves {2} whose every row is one of the {3} transversals, the incidence among them".format(
         nd(NCOV), nd(NFAM), nd(len(ANS)), nd(NCOV)))

gate(EQSET == ANS and len(EQSET ^ ANS) == 0 and len(EQSET) == len(ANS)
     and len(ANS) == 48, "G10",
     "the {0} relabellings and the {0} census members are the same {0}, element by element: the symmetry count is the combinatorial count".format(
         nd(len(ANS))))

CIDX = dict((tuple(COV[d]), d) for d in range(NCOV))


def rowmap(v):
    """The transversal each row of member v names, or minus one otherwise."""
    M = np.zeros((NCOV, NPI), dtype=np.int64)
    for k in v:
        M = M + TAB[k]
    return tuple(CIDX.get(tuple(np.nonzero(M[c])[0].tolist()), -1)
                 for c in range(NCOV))


RMAP = dict((v, rowmap(v)) for v in ANSL)
RMDEF = sum(1 for v in ANSL if min(RMAP[v]) >= 0)
RMBIJ = sum(1 for v in ANSL if len(set(RMAP[v])) == NCOV)

gate(RMDEF == 48 and RMBIJ == 48 and len(RMAP) == len(ANS), "G11",
     "all {0} census members send their {1} rows onto the {1} transversals, and all {0} of those row maps are bijections".format(
         nd(RMDEF), nd(NCOV)))

EQCHK = 0
EQMISS = 0
for v in ANSL:
    S = np.asarray(RMAP[v], dtype=np.int64)
    for e in range(NGRP):
        EQCHK += NCOV
        EQMISS += int(np.count_nonzero(S[CA[e]] != CA[e][S]))

gate(EQMISS == 0 and EQCHK == len(ANSL) * NGRP * NCOV and EQCHK == 3538944,
     "G12",
     "direct check: on {0} comparisons of member, map and transversal the row map commutes with the signed-coordinate action, {1} miss".format(
         nd(EQCHK), nd(EQMISS)))

GRP = dict((CA[e].tobytes(), e) for e in range(NGRP))
SYM = []
for v in ANSL:
    e = GRP.get(np.asarray(RMAP[v], dtype=np.int64).tobytes(), -1)
    if e >= 0:
        SYM.append((v, e))
SYMV = [v for v, e in SYM]
SYME = sorted(e for v, e in SYM)

gate(len(SYM) == 2 and SYME == sorted(CENT) and tuple(IPARTS) in SYMV
     and len(set(SYMV)) == 2, "G13",
     "exactly {0} row maps are themselves maps of the cell, the centre {1} and {2}: the members {3} and {4}".format(
         nd(len(SYM)), nd(SYME[0]), nd(SYME[1]), sl(SYMV[0]), sl(SYMV[1])))

RAE = []
RAN = 0
for e in range(NGRP):
    if decomp(INC[CA[e], :]) is None:
        RAN += 1
    else:
        RAE.append(e)

gate(len(RAE) == 2 and sorted(RAE) == sorted(CENT) and RAN == 382
     and RAN + len(RAE) == NGRP, "G14",
     "among all {0} signed-coordinate row relabellings, exactly {1} remain"
     " four-table members and they are the centre".format(
         nd(NGRP), nd(len(RAE))))

# ------------------------------------------------------------------
# 15. the partner map, the sixteen variants, and the two instruments
# ------------------------------------------------------------------

U8 = [np.ascontiguousarray(T.astype(np.uint8)) for T in TAB]
SGNK = dict((U8[k].tobytes(), k) for k in range(NORB))
PARTNER = [SGNK.get(np.ascontiguousarray(U8[k][:, PA[FC]]).tobytes(), -1)
           for k in range(NORB)]
PVAL = (min(PARTNER) >= 0)
PINV = PVAL and all(PARTNER[PARTNER[k]] == k for k in range(NORB))
PFIXN = sum(1 for k in range(NORB) if PARTNER[k] == k)
VAR = []
for m in range(16):
    VAR.append(tuple(sorted(PARTNER[k] if divmod(m >> i, 2)[1] == 1 else k
                            for i, k in enumerate(sorted(IPARTS)))))

gate(PVAL and PINV and PFIXN == 0 and len(set(VAR)) == 16
     and VAR[0] == tuple(sorted(IPARTS)) and len(PARTNER) == NORB, "G15",
     "the central flip moves the pieces and permutes the {0} tables, an"
     " involution with {1} fixed; the {2} variants of the four parts are distinct".format(
         nd(NORB), nd(PFIXN), nd(len(VAR))))

BAS = dict(((s, p), blockbasis(s, p))
           for s in range(16) for p in (PRIME, PRIME2))
BIG = np.concatenate([TAB[k] for k in range(NORB)], axis=0)
BLKT = {}
for p in (PRIME, PRIME2):
    for s in range(16):
        BLKT[(s, p)] = np.mod(np.dot(BIG, BAS[(s, p)].T),
                              p).reshape(NORB, NCOV, PORB)


def prof(v):
    """The block rank of the member v at each of the sixteen sign patterns and
    both primes, the block restrictions taken one table at a time."""
    out = []
    for p in (PRIME, PRIME2):
        for s in range(16):
            A = np.zeros((NCOV, PORB), dtype=np.int64)
            for k in v:
                A = np.mod(A + BLKT[(s, p)][k], p)
            out.append(rrank(A, p))
    return tuple(out)


def labl(s, p):
    """The image label of each of the 96 tables at sign pattern s, numbered by
    first appearance in table order."""
    d = {}
    out = []
    for k in range(NORB):
        out.append(d.setdefault(imkey(BLKT[(s, p)][k], p), len(d)))
    return out


PRF = dict((v, prof(v)) for v in ANSL)
PRF0 = prof(tuple(IPARTS))
PSAME = sum(1 for v in ANSL if PRF[v] == PRF0)
PHALF = all(PRF[v][:16] == PRF[v][16:] for v in ANSL)
LAB = [labl(s, PRIME) for s in range(16)]
ONEW1 = (len(set(tuple(LAB[s]) for s in W1P)) == 1)
IML = tuple(tuple(sorted(LAB[s][k] for k in IPARTS)) for s in W1P)
FOUR = sorted(v for v in ANSL
              if tuple(tuple(sorted(LAB[s][k] for k in v))
                       for s in W1P) == IML)
FSET = set(FOUR)


def pmem(v):
    return tuple(sorted(PARTNER[k] for k in v))


# The four variant indices are a fixed declared comparison set, not search output.
VJ = [0, 6, 9, 15]
VPAT = []
for j in VJ:
    VPAT.append((prof(VAR[j]) == PRF0, VAR[j] in ANS))
VFOUR = set(VAR[j] for j in VJ)

gate(VPAT == [(True, True), (True, False), (True, False), (True, True)]
     and VFOUR != FSET and len(VFOUR) == 4, "G16",
     "the {0} specified partner variants share the profile; {1} lie in the row census; this four-set differs from the image-label set".format(
         nd(len(VJ)), nd(sum(1 for a, b in VPAT if b))))

gate(PSAME == 48 and len(set(PRF[v] for v in ANSL)) == 1 and PHALF
     and len(PRF0) == 32, "G17",
     "all {0} census members carry the declared 32-entry two-field profile {1}; the field profiles agree entrywise: {2}".format(
         nd(PSAME), sl(PRF0[:16]), yn(PHALF)))

FPAIR = sorted(set(tuple(sorted([v, pmem(v)])) for v in FOUR))
FCLOSE = all(pmem(v) in FSET for v in FOUR)
FNOFIX = all(pmem(v) != v for v in FOUR)
FSYM = len(FSET & set(SYMV))

gate(len(FOUR) == 4 and FCLOSE and FNOFIX and len(FPAIR) == 2 and FSYM == 2
     and ONEW1, "G18",
     "the weight-one image label selects {1} of {0}: {2} partner pairs without fixed members, including both {3} central-map members".format(
         nd(len(ANSL)), nd(len(FOUR)), nd(len(FPAIR)), nd(FSYM)))

LOWI = [s for s in range(16) if WT[s] <= 2]
LOWP = sum(1 for v in ANSL
           if tuple(PRF[v][s] for s in LOWI) == tuple(PRF0[s] for s in LOWI))
BOTH = sorted(v for v in ANSL
              if tuple(PRF[v][s] for s in LOWI) == tuple(PRF0[s] for s in LOWI)
              and v in FSET)

gate(len(LOWI) == 11 and LOWP == 48 and BOTH == FOUR and len(BOTH) == 4,
     "G19",
     "the {0} low-weight ranks select {1} of {2}; their conjunction with the"
     " weight-one image label selects the same {3}".format(
         nd(len(LOWI)), nd(LOWP), nd(len(ANSL)), nd(len(BOTH))))

# ------------------------------------------------------------------
# 16. the character law, the closed form of the partner, and relabelling
# ------------------------------------------------------------------

CEQ = {}
CNG = {}
CLCHK = 0
CLMISS = 0
for s in range(16):
    for p in (PRIME, PRIME2):
        eq = 0
        ng = 0
        for k in range(NORB):
            a = BLKT[(s, p)][k]
            b = BLKT[(s, p)][PARTNER[k]]
            e1 = bool(np.array_equal(a, b))
            e2 = (not np.mod(a + b, p).any())
            eq += 1 if e1 else 0
            ng += 1 if e2 else 0
            CLCHK += 1
            if not (e1 or e2):
                CLMISS += 1
        CEQ[(s, p)] = eq
        CNG[(s, p)] = ng
CLAW = []
CLCON = True
for w in range(5):
    ks = [(s, p) for s in range(16) if WT[s] == w for p in (PRIME, PRIME2)]
    ev = set(CEQ[x] for x in ks)
    nv = set(CNG[x] for x in ks)
    if len(ev) != 1 or len(nv) != 1:
        CLCON = False
    CLAW.append((w, sorted(ev)[0], sorted(nv)[0]))

gate(CLAW == [(0, 96, 0), (1, 0, 96), (2, 96, 0), (3, 0, 96), (4, 96, 96)]
     and CLCON and CLMISS == 0 and CLCHK == NORB * 16 * 2, "G20",
     "over {0} table, pattern, prime checks a partner block is its block times the weight parity, {1} outside: {2}".format(
         nd(CLCHK), nd(CLMISS),
         " ".join("{0}:{1}/{2}".format(nd(a), nd(b), nd(c))
                  for a, b, c in CLAW)))

CFN = []
for e in range(NGRP):
    Pe = PA[e]
    c = 0
    for k in range(NORB):
        if SGNK.get(np.ascontiguousarray(U8[k][:, Pe]).tobytes(), -1) >= 0:
            c += 1
    CFN.append(c)
CFALL = sorted(e for e in range(NGRP) if CFN[e] == NORB)
CFZERO = sum(1 for e in range(NGRP) if CFN[e] == 0)
PUREO = [e for e in FLIPS if e != ID and e not in CENT]
PZ = sum(1 for e in PUREO if CFN[e] == 0)

gate(CFALL == sorted(CENT) and len(CFALL) == 2 and len(PUREO) == 14
     and PZ == 14 and CFZERO == NGRP - 2, "G21",
     "moving the pieces by a map permutes the {0} tables only for the {1} central maps; {2} of the other {3} return none, {4} of them flips".format(
         nd(NORB), nd(len(CFALL)), nd(CFZERO), nd(NGRP - 2), nd(len(PUREO))))

RL1 = np.array_equal(sum(TAB[PARTNER[k]] for k in IPARTS), INC[:, PA[FC]])
RL2 = np.array_equal(INC[:, PA[FC]], INC[CA[FC], :])
RL3 = (pmem(tuple(IPARTS)) in ANS)

gate(RL1 and RL2 and RL3 and FC != ID, "G22",
     "the partner image of the incidence is its piece image under the central flip and equally its transversal relabelling")

# ------------------------------------------------------------------
# 17. the relabelling group action, the ladder, and positive controls
# ------------------------------------------------------------------

SIDX = dict((s, i) for i, s in enumerate(SKEY))
SIDREL = SIDX.get(tuple(range(NCOV)), -1)
SPROD = []
SQUOT = True
SACT = True
MMEM = dict((s, partsum(MEM[s])) for s in SKEY)
for a in SKEY:
    row = []
    for b in SKEY:
        comp = tuple(a[b[c]] for c in range(NCOV))
        ix = SIDX.get(comp, -1)
        row.append(ix)
        if ix < 0:
            SQUOT = False
            SACT = False
            continue
        # sigma(n) after sigma(m) represents the quotient product m*n for the
        # left-coset/right-action convention used by sigma(). Check every
        # representative in both order-two fibres.
        SQUOT = SQUOT and all(
            sigma(MUL[nb][na], GC) == comp
            for na in SIG[a] for nb in SIG[b]
        )
        SACT = SACT and bool(np.array_equal(MMEM[a][list(b), :], MMEM[comp]))
    SPROD.append(row)
SRANGE = list(range(len(SKEY)))
SLATIN = (all(sorted(row) == SRANGE for row in SPROD)
          and all(sorted(SPROD[i][j] for i in SRANGE) == SRANGE
                  for j in SRANGE))
SIDOK = (SIDREL >= 0 and all(SPROD[SIDREL][i] == i
                            and SPROD[i][SIDREL] == i for i in SRANGE))
SINVOK = (SIDREL >= 0 and all(any(SPROD[i][j] == SIDREL
                                  and SPROD[j][i] == SIDREL for j in SRANGE)
                              for i in SRANGE))
TOR = sum(1 for row in SPROD for ix in row if ix >= 0)
TORM = len(set(MEM[k] for k in SKEY))

gate(TOR == len(SKEY) * len(SKEY) and TOR == 2304 and TORM == 48
     and len(SKEY) == 48 and SLATIN and SIDOK and SINVOK and SQUOT and SACT,
     "G23",
     "the {0}x{0} relabelling table is Latin with identity/inverses, matches N_G(H)/H, and acts on all {2} images ({1} products)".format(
         nd(len(SKEY)), nd(TOR), nd(TORM)))

LFAM = nCr(NORB, 4)
LCNT = hist(LAB[W1P[0]])
LMUL = hist(list(IML[0]))
LSURV = 1
for v in sorted(LMUL):
    LSURV = LSURV * nCr(LCNT[v], LMUL[v])

gate(LFAM == 3321960 and LSURV == 30720 and len(ANS) == 48 and len(FOUR) == 4
     and len(SYM) == 2 and LFAM == NFAM, "G24",
     "the ladder: {0} members; label {1}; row-transversal {2}; both {3}; signed-coordinate row map {4}".format(
         nd(LFAM), nd(LSURV), nd(len(ANS)), nd(len(FOUR)), nd(len(SYM))))

CTRL1 = (len(ANS) == 48 and len(SYM) == 2)
CTRL2 = (len(set(PRF[v] for v in ANSL)) == 1)
CTRL3 = (len(ANSL) - len(SYM))
LABA = dict((v, tuple(tuple(sorted(LAB[s][k] for k in v))
                      for s in range(16))) for v in SYMV)
CTRL4 = (PRF[SYMV[0]] == PRF[SYMV[1]] and LABA[SYMV[0]] == LABA[SYMV[1]]
         and SYMV[0] != SYMV[1])

gate(CTRL1 and CTRL2 and CTRL3 == 46 and CTRL4, "G25",
     "row census {0}: central-map members {1}, other equivariant relabellings {2}; the central pair has equal profiles and labels".format(
         nd(len(ANS)), nd(len(SYM)), nd(CTRL3)))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
MBS = RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RSS / 1024.0
emit("elapsed {0} s, peak resident {1} MB".format(nd(int(time.time() - T0)), nd(int(MBS))))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
sys.exit(0 if STAT[1] == 0 else 1)
