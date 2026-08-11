"""Three sign labellings split every cover of the physical cell cutting four and four.

Standalone exact runner. It rebuilds the unit four-cube cell object from scratch:
the sixteen corners, the five-corner unit-determinant pieces at the adjacency cost
floor, the cuttings by them, the pieces that occur, and the eight-piece covers.
The group of 384 signed coordinate maps is built by permuting the four coordinates
and flipping any of them, and it is transitive on the 192 pieces and on the 192
covers with point stabilisers of order two.

The subject of this cycle is the four sign characters of that group. Each is plus
one on the non-identity element of a piece stabiliser, so each transports from one
piece to a labelling of all 192 pieces by plus and minus one, unique up to a global
sign. The three nonconstant labellings are then measured against the eight-piece
covers: every cover is split four and four. Two of the three vanish because the
cover side carries no copy of their character at all; the third is a lone block
number that could have been any even value up to eight and is measured to be zero.
The flip parity labelling is identified in closed form as the parity of the total
number of ones over a piece's five corners, and a complete walk over all 65536
corner subsets shows that labelling and its negative are the only ones of that kind.
Three wrong-value rejectors and one perturbed action show the gates discriminate.

All work is over the integers, the rationals and two fixed primes; no floating
point enters any gate and no constant is fitted.

Output: one line per gate, then the characters printed before that line, then
the total line.
"""

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
# 3. the four sign characters
# ------------------------------------------------------------------


def sgn_perm(pm):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if pm[i] > pm[j]:
                s = -s
    return s


CHAR = [[1] * NGRP,
        [sgn_perm(DESC[e][0]) for e in range(NGRP)],
        [1 - 2 * (popc(DESC[e][1]) & 1) for e in range(NGRP)]]
CHAR.append([CHAR[1][e] * CHAR[2][e] for e in range(NGRP)])
NCH = len(CHAR)

HOM = True
for a in range(NGRP):
    ra = COMP[a]
    for b in range(NGRP):
        j = ra[b]
        for k in range(NCH):
            if CHAR[k][j] != CHAR[k][a] * CHAR[k][b]:
                HOM = False
CHDIST = (len(set(tuple(c) for c in CHAR)) == NCH)

# two elements generate everything, so a sign character is fixed by two signs
GDX = [DESC.index(((1, 2, 3, 0), 0)), DESC.index(((1, 0, 2, 3), 1))]
GENSET = set([IDG])
fr = [IDG]
while fr:
    x = fr.pop()
    for g in GDX:
        y = COMP[g][x]
        if y not in GENSET:
            GENSET.add(y)
            fr.append(y)
GEN_OK = (len(GENSET) == NGRP)
NSIGN = 1 << len(GDX)

CHEP = [CHAR[k][EPP] for k in range(NCH)]
CHEC = [CHAR[k][ECC] for k in range(NCH)]

# ------------------------------------------------------------------
# 4. transport labellings on the pieces
# ------------------------------------------------------------------

LABS = []
WELL = []
EQV = []
for k in range(NCH):
    u = [0] * NPI
    ok = True
    for e in range(NGRP):
        j = PERM[e][0]
        v = CHAR[k][e]
        if u[j] == 0:
            u[j] = v
        elif u[j] != v:
            ok = False
    WELL.append(ok and all(x != 0 for x in u))
    EQV.append(all(u[PERM[e][i]] == CHAR[k][e] * u[i]
                   for e in range(NGRP) for i in range(NPI)))
    LABS.append(u)
NEQ = NGRP * NPI
PLUS = [sum(1 for x in u if x == 1) for u in LABS]


def covcount(u):
    d = {}
    for c in CS:
        s = sum(u[p] for p in c)
        d[s] = d.get(s, 0) + 1
    return d


def spread(d):
    return ",".join("{0}:{1}".format(a, b) for a, b in sorted(d.items()))


CSUM = [covcount(u) for u in LABS]
CS0 = (CSUM[0] == {8: NCOV})
CSZ = all(CSUM[k] == {0: NCOV} for k in [1, 2, 3])
HALFC = set()
for k in [1, 2, 3]:
    for c in CS:
        HALFC.add(sum(1 for p in c if LABS[k][p] == 1))
FOURFOUR = (HALFC == set([4]))

# ------------------------------------------------------------------
# 5. the closed form of the flip parity labelling
# ------------------------------------------------------------------

CP1 = [1 - 2 * (sum(popc(c) for c in KEPT[USED[i]]) & 1) for i in range(NPI)]
CPSGN = 1 if CP1[0] == LABS[2][0] else -1
CPMATCH = all(CP1[i] == CPSGN * LABS[2][i] for i in range(NPI))

AX = []
for r in range(4):
    AX.append([1 - 2 * (sum(CORN[c][r] for c in KEPT[USED[i]]) & 1)
               for i in range(NPI)])
PRODAX = all(AX[0][i] * AX[1][i] * AX[2][i] * AX[3][i] == CP1[i] for i in range(NPI))

AXPLUS = [sum(1 for x in a if x == 1) for a in AX]
AXCNT = [covcount(a) for a in AX]
AXSAME = all(sorted(AXCNT[r].items()) == sorted(AXCNT[0].items()) for r in range(4))
ONESIDE = [set(k for k in range(NCOV) if sum(AX[r][p] for p in CS[k]) != 0)
           for r in range(4)]
OSSZ = sorted(set(len(s) for s in ONESIDE))
OSINT = len(set.intersection(*ONESIDE))
OSUNI = len(set.union(*ONESIDE))
OSPAIR = max(len(ONESIDE[r] & ONESIDE[s])
             for r in range(4) for s in range(4) if r < s)
OSONE = sorted(set(sum(1 for r in range(4) if k in ONESIDE[r])
                   for k in range(NCOV)))

# ------------------------------------------------------------------
# 6. the orientation sign is a different function
# ------------------------------------------------------------------

ORI = []
for i in range(NPI):
    S = KEPT[USED[i]]
    v0 = CORN[S[0]]
    ORI.append(det4([[CORN[S[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]))
ORIPM = (sorted(set(ORI)) == [-1, 1])
ORIPLUS = sum(1 for x in ORI if x == 1)
ORICNT = covcount(ORI)
ORIBAL = ORICNT.get(0, 0)
ORISGN = 1 if ORI[0] == CP1[0] else -1
ORIDIFF = sum(1 for i in range(NPI) if ORISGN * ORI[i] != CP1[i])

# ------------------------------------------------------------------
# 7. independence, blindness and the rank of the incidence table
# ------------------------------------------------------------------

UU = [LABS[1], LABS[2], LABS[3]]
GRAM = [[sum(UU[a][i] * UU[b][i] for i in range(NPI)) for b in range(3)]
        for a in range(3)]
GDET = (GRAM[0][0] * (GRAM[1][1] * GRAM[2][2] - GRAM[1][2] * GRAM[2][1])
        - GRAM[0][1] * (GRAM[1][0] * GRAM[2][2] - GRAM[1][2] * GRAM[2][0])
        + GRAM[0][2] * (GRAM[1][0] * GRAM[2][1] - GRAM[1][1] * GRAM[2][0]))
MUZERO = all(sum(BROW[r][i] * u[i] for i in range(NPI)) == 0
             for u in UU for r in range(NCOV))
RANK = rank_modp(BROW, PRIME)
RANK2 = rank_modp(BROW, PRIME2)
BLIND = NPI - RANK


def pivot_sets(Mx, p):
    """mod p elimination returning the pivot row and pivot column index lists"""
    A = np.mod(np.array(Mx, dtype=np.int64), p)
    nr, nc = A.shape
    idx = list(range(nr))
    pr, pc = [], []
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
            idx[r], idx[piv] = idx[piv], idx[r]
        iv = pow(int(A[r, c]), p - 2, p)
        A[r] = np.mod(A[r] * iv, p)
        if r + 1 < nr:
            A[r + 1:] = np.mod(A[r + 1:] - np.outer(A[r + 1:, c], A[r]), p)
        pr.append(idx[r])
        pc.append(c)
        r += 1
        if r == nr:
            break
    return pr, pc


def ff_inverse(Sx, n):
    """fraction free elimination on [S | I]: integer B and d with B S = d I.

    Every intermediate value is an integer minor of S, so no fraction and no
    floating point enters, and the returned d is the determinant of S.
    """
    A = [Sx[i][:] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    prev = 1
    sgn = 1
    for k in range(n):
        if A[k][k] == 0:
            sw = None
            for i in range(k + 1, n):
                if A[i][k]:
                    sw = i
                    break
            if sw is None:
                return 0, None
            A[k], A[sw] = A[sw], A[k]
            sgn = -sgn
        pk = A[k][k]
        Ak = A[k]
        for i in range(n):
            if i == k:
                continue
            Ai = A[i]
            f = Ai[k]
            for j in range(2 * n):
                Ai[j] = (Ai[j] * pk - f * Ak[j]) // prev
            Ai[k] = 0
        prev = pk
    return sgn * prev, [[sgn * A[i][n + j] for j in range(n)] for i in range(n)]


# the two sided integer certificate for the rank.  A minor of determinant one
# forces the rank up in EVERY characteristic; showing that every row of the
# table is an integer combination of the chosen rows forces it back down.
PIVR, PIVC = pivot_sets(BROW, PRIME)
NPIV = len(PIVR)
MINOR = [[BROW[r][c] for c in PIVC] for r in PIVR]
MDET, MINV = ff_inverse(MINOR, NPIV)
INVOK = MINV is not None and all(
    sum(MINV[i][k] * MINOR[k][j] for k in range(NPIV)) == (MDET if i == j else 0)
    for i in range(NPIV) for j in range(NPIV))
UNIMOD = bool(INVOK and MDET * MDET == 1)
LATT = UNIMOD
if UNIMOD:
    AINV = [[MDET * MINV[i][j] for j in range(NPIV)] for i in range(NPIV)]
    for r in range(NCOV):
        mr = [BROW[r][c] for c in PIVC]
        co = [sum(mr[k] * AINV[k][j] for k in range(NPIV)) for j in range(NPIV)]
        rec = [0] * NPI
        for j in range(NPIV):
            cj = co[j]
            if cj:
                brj = BROW[PIVR[j]]
                for col in range(NPI):
                    rec[col] += cj * brj[col]
        if rec != BROW[r]:
            LATT = False
            break
EXACTRK = UNIMOD and LATT and NPIV == RANK

# ------------------------------------------------------------------
# 8. the separation: which side carries a copy of which character
# ------------------------------------------------------------------

CONF = []
for k in range(NCH):
    w = [0] * NCOV
    bad = [False] * NCOV
    for e in range(NGRP):
        j = CPERM[e][0]
        v = CHAR[k][e]
        if w[j] == 0:
            w[j] = v
        elif w[j] != v:
            bad[j] = True
    CONF.append(sum(1 for x in bad if x))

MPD = [divmod(sum(CHAR[k][e] * FIXP[e] for e in range(NGRP)), NGRP) for k in range(NCH)]
MCD = [divmod(sum(CHAR[k][e] * FIXC[e] for e in range(NGRP)), NGRP) for k in range(NCH)]
MP = [x[0] for x in MPD]
MC = [x[0] for x in MCD]
MREM = all(x[1] == 0 for x in MPD) and all(x[1] == 0 for x in MCD)
CEILK = [min(MP[k], MC[k]) for k in range(NCH)]
BLK = [sum(LABS[k][p] for p in CS[0]) if CEILK[k] == 1 else None for k in range(NCH)]
RK = [0 if BLK[k] is None else (1 if BLK[k] != 0 else 0) for k in range(NCH)]
EXCK = [CEILK[k] - RK[k] for k in range(NCH)]
CEILS = sum(CEILK)
EXCS = sum(EXCK)
NBLKV = len(range(-8, 10, 2))

# carried in from an earlier cycle of this lane, which is in flight and not on
# the main line.  It is context for the two numbers this cycle measures, and it
# is not asserted here as an established input.
CEIL_LANE = 144
EXC_LANE = CEIL_LANE - RANK

# ------------------------------------------------------------------
# 9. wrong-value rejectors
# ------------------------------------------------------------------

R1 = []
for k in [1, 2, 3]:
    u = LABS[k]
    for i in range(NPI):
        v = list(u)
        v[i] = -v[i]
        R1.append(sum(1 for c in CS if sum(v[p] for p in c) != 0))
R1N = len(R1)

R2 = []
for k in [1, 2, 3]:
    u = LABS[k]
    pairs = []
    t = 1
    while len(pairs) < 24 and t < 4000:
        a = divmod(5 * t, NPI)[1]
        b = divmod(7 * t * t + 11, NPI)[1]
        if a != b and u[a] == -u[b] and (a, b) not in pairs:
            pairs.append((a, b))
        t += 1
    for (a, b) in pairs:
        v = list(u)
        v[a], v[b] = v[b], v[a]
        R2.append(sum(1 for c in CS if sum(v[p] for p in c) != 0))
R2N = len(R2)
R2PER = R2N // 3


def transport_ok(P2, k):
    u = [0] * NPI
    for e in range(NGRP):
        j = P2[e][0]
        v = CHAR[k][e]
        if u[j] == 0:
            u[j] = v
        elif u[j] != v:
            return False
    if any(x == 0 for x in u):
        return False
    for e in range(NGRP):
        pe = P2[e]
        ck = CHAR[k][e]
        for i in range(NPI):
            if u[pe[i]] != ck * u[i]:
                return False
    return True


TR = []
kk = 1
while len(TR) < 12:
    a = divmod(SEED * kk, NPI)[1]
    b = divmod(SEED * kk * kk + 5, NPI)[1]
    if a != b and (a, b) not in TR:
        TR.append((a, b))
    kk += 1

R3 = []
for j, (a, b) in enumerate(TR):
    e0 = divmod(11 * (j + 1), NGRP)[1]
    P2 = list(PERM)
    row = list(PERM[e0])
    ia = row.index(a)
    ib = row.index(b)
    row[ia] = b
    row[ib] = a
    P2[e0] = tuple(row)
    for k in [1, 2, 3]:
        R3.append((not transport_ok(P2, k), LABS[k][a] != LABS[k][b]))
R3EQ = all(x == y for x, y in R3)
R3N = sum(1 for x, y in R3 if x)
R3T = sum(1 for j in range(len(TR)) if any(R3[3 * j + t][0] for t in range(3)))

# ------------------------------------------------------------------
# 10. every corner subset, by a walk that changes one corner at a time
# ------------------------------------------------------------------

PMSK = [0] * 16
for i in range(NPI):
    for c in KEPT[USED[i]]:
        PMSK[c] |= (1 << i)
COVW = [sum(1 << p for p in c) for c in CS]
PFULL = (1 << NPI) - 1
NSUB = 1 << 16
NCORN = len(KEPT[USED[0]])
WORD = [0] * NSUB
SBLIND = []
W = 0
g = 0
if all(popc(0 & COVW[t]) == 4 for t in range(NCOV)):
    SBLIND.append(0)
for k in range(1, NSUB):
    r = (k & (-k)).bit_length() - 1
    g ^= (1 << r)
    W ^= PMSK[r]
    WORD[g] = W
    ok = True
    for t in range(NCOV):
        if popc(W & COVW[t]) != 4:
            ok = False
            break
    if ok:
        SBLIND.append(g)
SBN = len(SBLIND)
SBSZ = sorted(popc(x) for x in SBLIND)
SODD = sum(1 << c for c in range(16) if (popc(c) & 1) == 1)
SCOMP = (NSUB - 1) ^ SODD
SBSET = (sorted(SBLIND) == sorted([SODD, SCOMP]))
NEGOK = all(WORD[(NSUB - 1) ^ s] == (WORD[s] ^ PFULL) for s in range(NSUB))
LABODD = [1 - 2 * ((WORD[SODD] >> i) & 1) for i in range(NPI)]
ODDMATCH = (LABODD == LABS[2])
AXSUB = [sum(1 << c for c in range(16) if (c >> r) & 1) for r in range(4)]
AXSCNT = []
for am in AXSUB:
    d = {}
    for t in range(NCOV):
        s = 8 - 2 * popc(WORD[am] & COVW[t])
        d[s] = d.get(s, 0) + 1
    AXSCNT.append(d)
AXSBLIND = any(am in SBLIND for am in AXSUB)
AXSSAME = all(sorted(d.items()) == sorted(AXCNT[0].items()) for d in AXSCNT)
WSET = set(WORD)
ORIW = sum(1 << i for i in range(NPI) if ORI[i] == -1)
ORISUB = (ORIW in WSET) or ((ORIW ^ PFULL) in WSET)

# ------------------------------------------------------------------
# 11. source hygiene
# ------------------------------------------------------------------

SRC = open(__file__, "r").read()
NO_PC = (chr(37) not in SRC)
NO_TAB = (chr(9) not in SRC)
NO_EM = (chr(8212) not in SRC)
ASCII_OK = all(ord(ch) < 128 for ch in SRC)
NO_D9 = (("9" + "9") not in SRC)

BAN = [("reta", "ined"), ("aud", "ited"), ("audit", " will"), ("only ", "route"),
       ("last ", "route"), ("exha", "ust"), ("clos", "es"), ("PHAS", "E_"),
       ("r = 1", "/2"), ("r=1", "/2"), ("grav", "it"), ("Ha", "ar"),
       ("Reyn", "olds"), ("viel", "bein"), ("tet", "rad"), ("resolves ", "PARTIAL"),
       ("/Us", "ers/"), ("7/", "(8"), ("regi", "ster"), ("oct", "et"),
       ("sch", "eme"), ("assoc", "iation"), ("Sm", "ith"), ("Bar", "eiss"),
       ("Gal", "ois"), ("Hor", "ner"), ("Sch", "ur"), ("B", "_4"),
       ("hyper", "octahedral"), ("Cox", "eter"), ("na", "uty"), ("sau", "cy"),
       ("bl", "iss"), ("trac", "es"), ("Mc", "Kay"), ("Weis", "feiler"),
       ("Le", "man"), ("Leh", "man"), ("O", "_h"), ("inver", "sion"),
       ("what a construction would ", "have to give up")]
LOWSRC = SRC.lower()
BAN_OK = True
NBAN = 0
for a, b in BAN:
    NBAN += 1
    if (a + b).lower() in LOWSRC:
        BAN_OK = False

# ------------------------------------------------------------------
# 12. budget
# ------------------------------------------------------------------

ELAPSED = int(time.time() - T0)
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSSMB = RSS // 1048576 if RSS > 10000000 else RSS // 1024

# ------------------------------------------------------------------
# gates
# ------------------------------------------------------------------

emit("all numbers below are exact computational identities;"
     " no floating point enters any gate")

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800
     and SIZES == [24] and NPI == 192 and NCOV == 192 and GENERIC, "C0",
     "object: {0} candidates, {1} at adjacency cost floor {2}, {3} cuttings of {4},"
     " {5} pieces used, {6} covers"
     .format(NCAND, NKEPT, FLOOR, NS, SIZES[0], NPI, NCOV))

gate(PCSET == [1975] and BRS == [8] and COVEXACT, "C1",
     "each piece lies in {0} cuttings and {1} times {0} is {2}; each cover has {1}"
     " pieces and meets every cutting once"
     .format(PCN[0], BRS[0], NS))

gate(GDISTINCT and CLOSED and KEEPS, "C2",
     "group: {0} coordinate maps, all distinct, shut under composition, every one"
     " carrying pieces to pieces".format(NGRP))

gate(PBIJ and PDIST and PIDOK and len(ORBP) == NPI, "C3",
     "piece action: {0} distinct bijections of the {1} pieces, a single orbit"
     .format(NGRP, NPI))

gate(CBIJ and CDIST and COVKEEP and len(ORBC) == NCOV, "C4",
     "cover action: {0} distinct bijections of the {1} covers, a single orbit"
     .format(NGRP, NCOV))

gate(len(STABP) == 2 and len(STABC) == 2 and SQP and SQC, "C5",
     "stabilisers: piece {0} has order {1}, cover {0} has order {1}, both non-identity"
     " elements square to the identity".format(0, len(STABP)))

gate(HOM and CHDIST and GEN_OK, "C6",
     "chars: {0} elements generate all {1}, so at most {2} sign characters exist; the {2}"
     " built are homomorphisms on {3} products, all distinct"
     .format(len(GDX), NGRP, NSIGN, NPROD))

gate(CHEP == [1, 1, 1, 1] and CHEC == [1, 1, -1, -1], "C7",
     "on the piece stabiliser element all {0} characters are 1; on the cover stabiliser"
     " element they are {1}".format(NCH, ", ".join(str(x) for x in CHEC)))

gate(FIXP[EPP] == 16 and FIXC[EPP] == 0 and FIXP[ECC] == 0 and FIXC[ECC] == 48, "C8",
     "fixed points: the piece stabiliser element fixes {0} pieces and {1} covers; the"
     " cover stabiliser element fixes {2} pieces and {3} covers"
     .format(FIXP[EPP], FIXC[EPP], FIXP[ECC], FIXC[ECC]))

gate(all(WELL) and all(EQV) and PLUS == [192, 96, 96, 96], "C9",
     "transport: all {0} labellings well defined and equivariant on {1} element-piece"
     " pairs; plus counts {2}"
     .format(NCH, NEQ, ", ".join(str(x) for x in PLUS)))

gate(CS0 and CSZ and FOURFOUR, "C10",
     "cover sums: trivial {0} on all {1} covers; the other {2} are 0 on all {1}, that is"
     " {3} plus and {3} minus in every cover"
     .format(8, NCOV, NCH - 1, sorted(HALFC)[0]))

gate(CPMATCH and CPSGN == 1, "C11",
     "the flip parity labelling equals the corner-ones parity on all {0} pieces, with"
     " global sign {1}".format(NPI, CPSGN))

gate(PRODAX, "C12",
     "the corner-ones parity is the product of the {0} single-axis parities on all {1}"
     " pieces".format(4, NPI))

gate(AXPLUS == [96, 96, 96, 96] and AXSAME
     and sorted(AXCNT[0].items()) == [(-8, 24), (0, 144), (8, 24)], "C13",
     "each single-axis parity is {0} and {0} with cover sums {1}, the same for all {2}"
     " axes, so {3} covers are one-sided"
     .format(AXPLUS[0], spread(AXCNT[0]), 4, len(ONESIDE[0])))

gate(OSSZ == [48] and OSINT == 0 and OSUNI == NCOV and OSPAIR == 0
     and OSONE == [1], "C14",
     "the {0} one-sided cover sets have {1} each, pairwise meet in {2} and cover all {3}:"
     " every cover is one-sided for exactly {4} axis"
     .format(4, OSSZ[0], OSPAIR, OSUNI, OSONE[0]))

gate(ORIPM and ORIPLUS == 96 and ORIBAL == 84 and ORIDIFF == 96, "C15",
     "orientation sign {0} and {0}; cover sums {1}; only {2} balance; differs from"
     " corner-ones on {3} pieces"
     .format(ORIPLUS, spread(ORICNT), ORIBAL, ORIDIFF))

gate(GDET != 0, "C16",
     "the {0} nonconstant labellings are independent over the rationals: their {0} by {0}"
     " Gram determinant is {1}, which is not zero".format(3, nd(GDET)))

gate(MUZERO, "C17",
     "each of the {0} satisfies M u = 0 exactly over the integers on all {1} covers, so"
     " all {0} lie in the blind space".format(3, NCOV))

gate(EXACTRK and RANK == 105 and RANK2 == RANK and BLIND == 87, "C18",
     "rank exactly {0}: a {0} by {0} minor of determinant {1}, and all {2} rows lie in its"
     " row lattice; blind {3} in every characteristic"
     .format(RANK, MDET, NCOV, BLIND))

gate(CONF == [0, 0, NCOV, NCOV] and MC == [1, 1, 0, 0] and MREM, "C19",
     "the {0} characters that are -1 on the cover stabiliser element have no cover-side"
     " copy: their cover transport conflicts on all {1} covers".format(2, CONF[2]))

gate(MP[1] == 1 and MC[1] == 1 and BLK[1] == 0, "C20",
     "permutation sign: multiplicity {0} on both sides, so its block is one even number,"
     " a priori {1} values from -8 to 8, measured {2}"
     .format(MP[1], NBLKV, BLK[1]))

gate(MP == [1, 1, 1, 1] and CEILS == 2 and EXCS == 1 and MREM, "C21",
     "the {0} one-dimensional rows have piece multiplicities {1} and cover multiplicities"
     " {2}: ceiling {3} = {4}, excess {5} = {6}"
     .format(NCH, "".join(str(x) for x in MP), "".join(str(x) for x in MC),
             "+".join(str(x) for x in CEILK), CEILS,
             "+".join(str(x) for x in EXCK), EXCS))

gate(EXC_LANE == 39 and CEILS == 2 and EXCS == 1, "C22",
     "carried-in ceiling {0} less the measured rank {1} is an excess of {2}; these {3}"
     " rows supply {4} of the ceiling and {5} of the excess"
     .format(CEIL_LANE, RANK, EXC_LANE, NCH, CEILS, EXCS))

gate(min(R1) >= 1 and R1N == 3 * NPI and min(R1) == 8 and max(R1) == 8, "C23",
     "rejector one: flipping any single one of the {0} labels breaks a cover for each of"
     " the {1} labellings; fewest {2}, most {3}"
     .format(NPI, 3, min(R1), max(R1)))

gate(min(R2) >= 1 and R2PER >= 24, "C24",
     "rejector two: {0} opposite-label swaps, {1} per labelling, each breaks a cover;"
     " fewest {2}, most {3}".format(R2N, R2PER, min(R2), max(R2)))

gate(R3EQ and R3N >= 1, "C25",
     "rejector three: a transposed action breaks the transport exactly when the {0}"
     " swapped pieces differ; {1} of {2} break, {3} of {4} transpositions"
     .format(2, R3N, len(R3), R3T, len(TR)))

gate(SBN == 2 and SBSZ == [8, 8] and SBSET, "C26",
     "all {0} corner subsets: exactly {1} have cover sum 0 on every cover, both of size"
     " {2}, the masks {3} and {4}"
     .format(NSUB, SBN, SBSZ[0], min(SBLIND), max(SBLIND)))

gate(NEGOK and ODDMATCH and NCORN == 5, "C27",
     "complementing negates the labelling on all {0} subsets since a piece has {1}"
     " corners; subset {2} gives the flip parity labelling"
     .format(NSUB, NCORN, SODD))

gate(not AXSBLIND and AXSSAME and not ORISUB, "C28",
     "the {0} single-axis subsets are not blind: each has cover sums {1}; the orientation"
     " sign is no subset labelling of the {2}".format(4, spread(AXSCNT[0]), NSUB))

gate(ELAPSED < 900 and RSSMB < 2500 and OUT[0] + 320 < 5200, "C29",
     "budget: {0} s under 900, {1} MB under 2500, characters printed under 5200 with"
     " {2} to spare".format(nd(ELAPSED), nd(RSSMB), nd(5200 - 320 - OUT[0])))

gate(ASCII_OK and NO_PC and NO_TAB and NO_EM and NO_D9 and BAN_OK, "C30",
     "source hygiene: ASCII {0}, no tab {1}, no remainder sign {2}, no long dash {3},"
     " {4} barred strings absent {5}"
     .format(yn(ASCII_OK), yn(NO_TAB), yn(NO_PC), yn(NO_EM), NBAN, yn(BAN_OK)))

emit("characters printed before this line: {0}".format(nd(OUT[0])))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
