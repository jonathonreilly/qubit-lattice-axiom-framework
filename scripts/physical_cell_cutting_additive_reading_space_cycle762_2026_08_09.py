"""Cutting-side and cover-side additive reading spaces on one unit four-cube cell.

Self-contained exact runner. It builds the cell object from scratch: the sixteen
corners of the unit four-cube, the unit-determinant five-corner pieces at the
adjacency-cost floor, the exact cuttings of the cell by those pieces, the pieces
that actually occur, and the eight-piece covers that meet every cutting once.
It then verifies, over the rationals with no floating point in any gate, that the
assignments whose cutting-side total is the same on every cutting are exactly the
cover table's row space, that the assignments whose cover-side total is the same
on every cover are exactly the cutting table's row space, that the two row spaces
span the whole assignment space and meet in the constants alone, and that the two
common totals are the plain sum divided by eight and by twenty four.

Three controls are built to come out negative. No gate compares a quantity with
itself and no constant is fitted.

Output: one line per gate, then the stdout character count, then the total line.
"""

import itertools
import math
import sys
import time
import resource
from fractions import Fraction as FR

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


def gate(ok, tag, msg):
    if ok:
        STAT[0] += 1
    else:
        STAT[1] += 1
    emit("{0} {1}  {2}".format("PASS" if ok else "FAIL", tag, msg))


def popc(x):
    return x.bit_count()


# ------------------------------------------------------------------
# 1. the cell and its unit-determinant pieces
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
# 2. a sample lattice that avoids every facet plane of every piece
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
# 3. the cuttings
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
CUTM = [sum(1 << i for i in s) for s in CUT]

# cuttings through each piece, as a bit set over cuttings
PC = [0] * NPI
for k, s in enumerate(CUT):
    for i in s:
        PC[i] |= (1 << k)
PCN = [popc(x) for x in PC]
FULLC = (1 << NS) - 1

# ------------------------------------------------------------------
# 4. exact interior disjointness for every co-occurring pair
# ------------------------------------------------------------------


def solve4(rows):
    n = 4
    M = [[FR(x) for x in r] for r in rows]
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
                M[r] = [M[r][k] - f * M[c][k] for k in range(n + 1)]
    return [M[r][n] for r in range(n)]


def afrank(pts):
    if not pts:
        return -1
    base = pts[0]
    rows = [[p[r] - base[r] for r in range(4)] for p in pts[1:]]
    rk = 0
    piv = []
    for c in range(4):
        p = -1
        for i in range(rk, len(rows)):
            if rows[i][c] != 0:
                p = i
                break
        if p < 0:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        pv = rows[rk][c]
        for i in range(rk + 1, len(rows)):
            if rows[i][c] != 0:
                f = rows[i][c] / pv
                rows[i] = [rows[i][k] - f * rows[rk][k] for k in range(4)]
        piv.append(c)
        rk += 1
    return rk


def side(a, b, x):
    return a[0] * x[0] + a[1] * x[1] + a[2] * x[2] + a[3] * x[3] + b


def sep_facet(r1, P1, r2, P2):
    for (a, b) in r1:
        if max(side(a, b, x) for x in P2) <= 0:
            return True
    for (a, b) in r2:
        if max(side(a, b, x) for x in P1) <= 0:
            return True
    return False


def inter_dim(r1, r2):
    con = list(r1) + list(r2)
    pts = []
    for idx in itertools.combinations(range(10), 4):
        rows = [list(con[i][0]) + [-con[i][1]] for i in idx]
        x = solve4(rows)
        if x is None:
            continue
        ok = True
        for (a, b) in con:
            if a[0] * x[0] + a[1] * x[1] + a[2] * x[2] + a[3] * x[3] + b < 0:
                ok = False
                break
        if ok:
            tx = tuple(x)
            if tx not in pts:
                pts.append(tx)
    return afrank(pts)


PAIRS = []
for i in range(NPI):
    for j in range(i + 1, NPI):
        if PC[i] & PC[j]:
            PAIRS.append((i, j))
NPAIR = len(PAIRS)
NFAC = 0
NDIM = 0
DISJ_OK = True
PTS = [tuple(CORN[c] for c in S) for S in KEPT]
for (i, j) in PAIRS:
    r1 = BARY[USED[i]][2]
    r2 = BARY[USED[j]][2]
    if sep_facet(r1, PTS[USED[i]], r2, PTS[USED[j]]):
        NFAC += 1
        continue
    if inter_dim(r1, r2) <= 3:
        NDIM += 1
    else:
        DISJ_OK = False

# ------------------------------------------------------------------
# 5. the covers
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
COVM = [sum(1 << i for i in c) for c in COVERS]

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
BCS = sorted(set(sum(BROW[k][i] for k in range(NCOV)) for i in range(NPI)))

# ------------------------------------------------------------------
# 6. the two tables and the Gram substitution
# ------------------------------------------------------------------

GM = [[popc(PC[i] & PC[j]) for j in range(NPI)] for i in range(NPI)]
GM2 = [[0] * NPI for _ in range(NPI)]
for s in CUT:
    for i in s:
        gi = GM2[i]
        for j in s:
            gi[j] += 1
GRAM_OK = (GM == GM2)

ACS = sorted(set(GM[i][i] for i in range(NPI)))


def rref(rows, ncol, want_kernel):
    M = [[FR(x) for x in r] for r in rows]
    nr = len(M)
    piv = []
    r = 0
    for c in range(ncol):
        p = -1
        for i in range(r, nr):
            if M[i][c] != 0:
                p = i
                break
        if p < 0:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                Mi = M[i]
                Mr = M[r]
                M[i] = [Mi[k] - f * Mr[k] for k in range(ncol)]
        piv.append(c)
        r += 1
        if r == nr:
            break
    ker = []
    if want_kernel:
        ps = set(piv)
        for fc in range(ncol):
            if fc in ps:
                continue
            v = [FR(0)] * ncol
            v[fc] = FR(1)
            for i, pcl in enumerate(piv):
                v[pcl] = -M[i][fc]
            ker.append(v)
    return r, ker, [M[i] for i in range(r)]


def rank_fwd(rows, ncol, cap=None):
    piv = {}
    r = 0
    for row in rows:
        v = [FR(x) for x in row]
        for c in range(ncol):
            if v[c] == 0:
                continue
            if c in piv:
                f = v[c]
                w = piv[c]
                for k in range(c, ncol):
                    if w[k] != 0:
                        v[k] -= f * w[k]
            else:
                pv = v[c]
                v = [x / pv for x in v]
                piv[c] = v
                r += 1
                break
        if cap is not None and r >= cap:
            break
    return r


RA, KERA, BASA = rref(GM, NPI, True)
RB, KERB, BASB = rref(BROW, NPI, True)

ONE = [FR(1)] * NPI

def clear_den(v):
    den = 1
    for x in v:
        den = den * x.denominator // math.gcd(den, x.denominator)
    return [int(x * den) for x in v]


# ker(G) annihilates every row of A
KANN = True
KERAI = [clear_den(v) for v in KERA]
KERBI = [clear_den(v) for v in KERB]
for iv in KERAI:
    g = iv.__getitem__
    for s in CUT:
        if sum(map(g, s)) != 0:
            KANN = False
            break
    if not KANN:
        break

# rank of A from A's own rows, on two evenly spread selections
def spread_rank(n):
    st = NS // n
    idxs = [i * st for i in range(n)]
    rows = []
    for k in idxs:
        row = [0] * NPI
        for i in CUT[k]:
            row[i] = 1
        rows.append(row)
    return rank_fwd(rows, NPI)


RA400 = spread_rank(400)
RA800 = spread_rank(800)

# the two reading spaces
S105 = [list(v) for v in KERA] + [list(ONE)]
S88 = [list(v) for v in KERB] + [list(ONE)]
D105 = rank_fwd(S105, NPI)
D88 = rank_fwd(S88, NPI)

A1 = sorted(set(len(s) for s in CUT))
B1 = sorted(set(sum(r) for r in BROW))
ONE_NOT_KERA = (A1 == [24])
ONE_NOT_KERB = (B1 == [8])

# basis validation. a row space is exactly the perpendicular of the kernel once
# the two dimensions add to the number of columns, so a set of the right rank
# that is perpendicular to the kernel spans the row space.
def perp_all(rows, kers):
    for r in rows:
        ir = clear_den(r)
        for k in kers:
            if sum(a * b for a, b in zip(ir, k)) != 0:
                return False
    return True


BASA_OK = (rank_fwd(BASA, NPI) == RA and perp_all(BASA, KERAI)
           and RA + len(KERA) == NPI)
BASB_OK = (rank_fwd(BASB, NPI) == RB and perp_all(BASB, KERBI)
           and RB + len(KERB) == NPI)

J1 = rank_fwd(list(BASB) + S105, NPI)
J2 = rank_fwd(list(BASA) + S88, NPI)
J3 = rank_fwd(list(BASB) + list(BASA), NPI)

# column sums give the constants inside each row space
ATC = sorted(set(PCN))
COLA = ATC[0]
COLB = BCS[0]

# ------------------------------------------------------------------
# 7. the two totals, on fixed deterministic elements
# ------------------------------------------------------------------


def read_cut(v):
    g = v.__getitem__
    return sorted(set(sum(map(g, s)) for s in CUT))


def read_cov(v):
    return sorted(set(sum(v[i] for i in c) for c in COVERS))


TOT_OK = True
NZ105 = 0
NZ88 = 0
for pat in range(3):
    v = [FR(0)] * NPI
    for i, kv in enumerate(KERA):
        c = FR(1 + divmod(i * (pat + 2) + pat, 7)[1])
        for j in range(NPI):
            v[j] += c * kv[j]
    for j in range(NPI):
        v[j] += FR(pat + 1)
    vals = read_cut(v)
    sv = sum(v)
    if len(vals) != 1 or vals[0] != sv / 8:
        TOT_OK = False
    if sv != 0:
        NZ105 += 1
    w = [FR(0)] * NPI
    for i, kv in enumerate(KERB):
        c = FR(1 + divmod(i * (pat + 3) + pat, 5)[1])
        for j in range(NPI):
            w[j] += c * kv[j]
    for j in range(NPI):
        w[j] += FR(pat + 1)
    valw = read_cov(w)
    sw = sum(w)
    if len(valw) != 1 or valw[0] != sw / 24:
        TOT_OK = False
    if sw != 0:
        NZ88 += 1

# ------------------------------------------------------------------
# 8. controls
# ------------------------------------------------------------------

C11 = sorted(set(len(COVSET[0] & cs) for cs in COVSET))
C11ALL = set()
for a in range(NCOV):
    for b in range(NCOV):
        C11ALL.add(len(COVSET[a] & COVSET[b]))
C11ALL = sorted(C11ALL)
C11_OK = (len(C11) > 1 and C11 == C11ALL)

C12A = rank_fwd([list(v) for v in KERA], NPI)
C12B = rank_fwd([list(v) for v in KERB], NPI)
C12_OK = (C12A == NPI - RA and C12B == NPI - RB and C12A != D105 and C12B != D88)

B2ROW = [[BROW[k][divmod(i - 1, NPI)[1]] for i in range(NPI)] for k in range(NCOV)]
B2RS = sorted(set(sum(r) for r in B2ROW))
B2CS = sorted(set(sum(B2ROW[k][i] for k in range(NCOV)) for i in range(NPI)))
RB2 = rank_fwd([list(map(FR, r)) for r in B2ROW], NPI)
J13 = rank_fwd([list(map(FR, r)) for r in B2ROW] + S105, NPI)
C13_OK = (RB2 == RB and B2RS == BRS and B2CS == BCS and J13 > D105)

# corner sharing: how many pieces of one cutting hold a given corner
NCORN = len(CORN)
SLOTS = SIZES[0] * 5
OMIN = 10 ** 6
OMAX = 0
for s in SOLS:
    occ = [0] * 16
    for t in s:
        for c in KEPT[t]:
            occ[c] += 1
    a = min(occ)
    b = max(occ)
    if a < OMIN:
        OMIN = a
    if b > OMAX:
        OMAX = b

# ------------------------------------------------------------------
# 9. source hygiene and budget
# ------------------------------------------------------------------

SRC = open(__file__, "r").read()
NO_PC = (chr(37) not in SRC)
NO_EM = (chr(8212) not in SRC)
ASCII_OK = all(ord(ch) < 128 for ch in SRC)

ELAPSED = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSSMB = RSS / 1048576.0 if RSS > 10000000 else RSS / 1024.0

# ------------------------------------------------------------------
# gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and GENERIC and NPTS == 625
     and DIV == 80 and NS == 15800 and SIZES == [24] and NPI == 192
     and sorted(set(PCN)) == [1975] and NCOV == 192 and BRS == [8] and BCS == [8],
     "G0",
     "{0} pieces of determinant one, {1} at cost floor {2}, {3} cuttings of {4} over {5} points of divisor {9}, {6} used, {7} each, {8} covers".format(
         NCAND, NKEPT, FLOOR, NS, SIZES[0], NPTS, NPI, PCN[0], NCOV, DIV))

gate(DISJ_OK and NPAIR == NFAC + NDIM and COVEXACT and ACS == [1975],
     "G1",
     "each cutting is a tiling: {0} pieces of volume 1 over 24, all {1} co-occurring pairs interior-disjoint, {2} by facet".format(
         SIZES[0], NPAIR, NFAC))

gate(OMAX > 1 and SLOTS == 120 and NCORN == 16 and SLOTS > NCORN,
     "G2",
     "corner sharing: a cutting spends {0} corner slots on {1} corners, one corner taking from {2} to {3}, so a corner reading is not partitioned".format(
         SLOTS, NCORN, OMIN, OMAX))

gate(GRAM_OK and KANN and RA400 == 88 and RA800 == 88 and RA == 88,
     "G3",
     "product substitution sound: two builds of the {0} square agree, its kernel kills every cutting row, and 400 and 800 rows give rank {1}".format(
         NPI, RA400))

gate(RA == 88 and len(KERA) == 104 and RB == 105 and len(KERB) == 87
     and RA + len(KERA) == NPI and RB + len(KERB) == NPI,
     "G4",
     "cutting table rank {0} kernel {1}, cover table rank {2} kernel {3}, and {0} plus {1} and {2} plus {3} are both {4}".format(
         RA, len(KERA), RB, len(KERB), NPI))

gate(ONE_NOT_KERA and ONE_NOT_KERB and COLA == 1975 and COLB == 8,
     "G5",
     "one over {0} times the constants reads 1 on every cutting and one over {1} times the constants reads 1 on every cover".format(
         A1[0], B1[0]))

gate(D105 == 105 and D88 == 88 and BASA_OK and BASB_OK,
     "G6",
     "the equal-cutting-reading set has dimension {0} and the equal-cover-reading set has dimension {1}, the constants lying in neither kernel".format(
         D105, D88))

gate(J1 == 105 and D105 == 105 and RB == 105,
     "G7",
     "claim one: equal-cutting-reading set and cover table row space have joint rank {0}, matching both dimensions, so they are equal".format(
         J1))

gate(J2 == 88 and D88 == 88 and RA == 88,
     "G8",
     "claim two: equal-cover-reading set and cutting table row space have joint rank {0}, matching both dimensions, so they are equal".format(
         J2))

gate(J3 == 192 and RA + RB - J3 == 1,
     "G9",
     "claim three: the two row spaces have joint rank {0} and so meet in dimension {1}, the constants being the column sums over {2} and {3}".format(
         J3, RA + RB - J3, COLA, COLB))

gate(TOT_OK and NZ105 == 3 and NZ88 == 3 and NS == 8 * 1975 and NPI == 24 * 8,
     "G10",
     "claim four: on {0} nonzero-sum elements of each space the readings are the sum over 8 and the sum over 24, with {1} being 8 times {2}".format(
         NZ105, NS, 1975))

gate(C11_OK,
     "G11",
     "control negative: a cover lies in the {0}-space yet its cover-side reading takes the values {1}, so it is not constant".format(
         D105, ", ".join(str(x) for x in C11)))

gate(C12_OK,
     "G12",
     "control negative: with the constants replaced by the zero space the two dimensions drop to {0} and {1}, a real extra direction".format(
         C12A, C12B))

gate(C13_OK,
     "G13",
     "control negative: a cyclic column shift keeps rank {0} and both sums 8, but its joint rank with the {1}-space is {2}, so the match fails".format(
         RB2, D105, J13))

gate(D105 == NPI - D88 + 1 and D88 == NPI - D105 + 1 and D88 + D105 == NPI + 1,
     "G14",
     "bookkeeping: {0} is {1} minus {2} plus 1, {2} is {1} minus {0} plus 1, and {2} plus {0} is {1} plus 1".format(
         D105, NPI, D88))

gate(NO_PC and NO_EM and ASCII_OK,
     "G15",
     "source hygiene: no per-cent character, no long dash, every character of this file is plain ASCII")

gate(ELAPSED < 300.0 and RSSMB < 1500.0,
     "G16",
     "budget: elapsed under 300 seconds and peak resident memory under 1500 MB")

TAIL = "TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1])
BASE = OUT[0]
n = BASE
for _ in range(30):
    line = "stdout characters: {0}".format(n)
    cand = BASE + len(line) + 1 + len(TAIL) + 1
    if cand == n:
        break
    n = cand
emit("stdout characters: {0}".format(n))
emit(TAIL)
if OUT[0] != n:
    raise ValueError("character accounting did not close")
