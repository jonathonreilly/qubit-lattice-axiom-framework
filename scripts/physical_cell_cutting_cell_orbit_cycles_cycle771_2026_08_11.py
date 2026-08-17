"""Order-four stabilizer products and universal orbit-table rank 144.

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
determinant, with no 192 by 192 elimination in the proof, and the integral kernel
is exhibited rather than inferred. Exact geometry certificates identify the
finite object with continuous simplex cuttings. In-memory mutations exercise
every load-bearing check family.

All work is exact over the integers and two fixed primes; no floating point enters
any gate and no constant is fitted.

Output: one line per gate, two summary lines, then the total line."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

AUDIT_TIMEOUT_SEC = 180

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
MASK_VISIBLE = (len(MASK) == NKEPT and all(bits != 0 for bits in MASK))

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
SOLS_UNIQUE = (len(set(SOLS)) == NS)
SEARCH_OUTPUT_OK = SOLS_UNIQUE
for s in SOLS:
    cov = 0
    for t in s:
        if cov & MASK[t]:
            SEARCH_OUTPUT_OK = False
        cov |= MASK[t]
    if cov != UNIV:
        SEARCH_OUTPUT_OK = False


def piece_det_num(S):
    v0 = CORN[S[0]]
    return abs(det4([[CORN[S[j + 1]][r] - v0[r] for j in range(4)]
                     for r in range(4)]))


KEPT_DET = [piece_det_num(S) for S in KEPT]
CUT_VOLUME_OK = (all(x == 1 for x in KEPT_DET)
                 and all(sum(KEPT_DET[t] for t in s) == 24 for s in SOLS))


def mask_search_certificate(masks, sols):
    """Recheck that every emitted cutting is a disjoint full mask cover."""
    if len(masks) != NKEPT or any(bits == 0 for bits in masks):
        return False
    if len(sols) != 15800 or len(set(sols)) != len(sols):
        return False
    for sol in sols:
        if len(sol) != 24 or len(set(sol)) != 24:
            return False
        cov = 0
        for t in sol:
            if cov & masks[t]:
                return False
            cov |= masks[t]
        if cov != UNIV:
            return False
    return True


OBJECT_RECHECK_OK = mask_search_certificate(MASK, SOLS)

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

# Exact pairwise interior-disjointness for every pair that co-occurs in a
# cutting. Together with unit simplex volumes summing to the cube's normalized
# volume 24, this upgrades the mask search to a continuous cutting certificate.


def solve4(rows):
    n = 4
    M = [[FR(x) for x in r] for r in rows]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), -1)
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
    rows = [[FR(p[r]) - FR(base[r]) for r in range(4)] for p in pts[1:]]
    rk = 0
    for c in range(4):
        p = next((i for i in range(rk, len(rows)) if rows[i][c] != 0), -1)
        if p < 0:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        pv = rows[rk][c]
        for i in range(rk + 1, len(rows)):
            if rows[i][c] != 0:
                f = rows[i][c] / pv
                rows[i] = [rows[i][k] - f * rows[rk][k] for k in range(4)]
        rk += 1
    return rk


def side(a, b, x):
    return sum(a[r] * x[r] for r in range(4)) + b


def sep_facet(r1, p1, r2, p2):
    return (any(max(side(a, b, x) for x in p2) <= 0 for (a, b) in r1)
            or any(max(side(a, b, x) for x in p1) <= 0 for (a, b) in r2))


def inter_dim(r1, r2):
    con = list(r1) + list(r2)
    pts = []
    for idx in itertools.combinations(range(10), 4):
        x = solve4([list(con[i][0]) + [-con[i][1]] for i in idx])
        if x is None or any(side(a, b, x) < 0 for (a, b) in con):
            continue
        tx = tuple(x)
        if tx not in pts:
            pts.append(tx)
    return afrank(pts)


CO_PAIRS = [(i, j) for i in range(NPI) for j in range(i + 1, NPI)
            if PC[i] & PC[j]]
NFAC = 0
NDIM = 0
DISJ_OK = True
PTS = [tuple(CORN[c] for c in S) for S in KEPT]
for (i, j) in CO_PAIRS:
    r1 = BARY[USED[i]][2]
    r2 = BARY[USED[j]][2]
    if sep_facet(r1, PTS[USED[i]], r2, PTS[USED[j]]):
        NFAC += 1
    elif inter_dim(r1, r2) <= 3:
        NDIM += 1
    else:
        DISJ_OK = False


def continuous_cut_certificate(detnums, nfac, ndim, disjoint):
    return (len(detnums) == NKEPT and all(x == 1 for x in detnums)
            and all(sum(detnums[t] for t in s) == 24 for s in SOLS)
            and disjoint and nfac + ndim == len(CO_PAIRS))


CONTINUOUS_CUT_OK = continuous_cut_certificate(KEPT_DET, NFAC, NDIM, DISJ_OK)
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
BCS = sorted(set(sum(BROW[k][i] for k in range(NCOV)) for i in range(NPI)))
CS = [tuple(sorted(c)) for c in COVERS]
COVM = [sum(1 << i for i in c) for c in CS]
COVERS_UNIQUE = (len(set(COVM)) == NCOV)


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


def is_prime(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


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


def map_family_certificate(maps):
    if len(maps) != 384 or len(set(maps)) != 384:
        return False
    if any(sorted(m) != list(range(16)) for m in maps):
        return False
    idx = dict((m, i) for i, m in enumerate(maps))
    return all(tuple(a[b[c]] for c in range(16)) in idx
               for a in maps for b in maps)


MAP_FAMILY_OK = map_family_certificate(MAPS)

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
CIDOK = (CPERM[IDG] == IDC)


def action_certificate(pp, qq):
    if len(pp) != NGRP or len(qq) != NGRP:
        return False
    if (any(sorted(p) != list(range(NPI)) for p in pp)
            or any(sorted(q) != list(range(NCOV)) for q in qq)):
        return False
    for a in range(NGRP):
        for b in range(NGRP):
            e = COMP[a][b]
            if tuple(pp[a][pp[b][i]] for i in range(NPI)) != pp[e]:
                return False
            if tuple(qq[a][qq[b][j]] for j in range(NCOV)) != qq[e]:
                return False
    return True


ACTION_OK = action_certificate(PERM, CPERM)

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

OBJECT_CERT_OK = (GENERIC and MASK_VISIBLE and SEARCH_OUTPUT_OK
                  and CUT_VOLUME_OK and CONTINUOUS_CUT_OK and OBJECT_RECHECK_OK)

gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and PCNSET == [1975]
     and len(USED) == NPI and len(POS) == NPI and LHS == RHS == 379200
     and OBJECT_CERT_OK,
     "C0",
     "exact cell {0} unit-det, {1} at floor {2}, {3} cuttings of {4}, {5} pieces, {6} each, {7}={8}".format(
         nd(NCAND), nd(NKEPT), nd(FLOOR), nd(NS), nd(CUTSZ), nd(NPI), nd(PCN0), nd(LHS), nd(RHS)))

gate(NCOV == 192 and BRS == [8] and BCS == [8] and COVERS_UNIQUE
     and COVEXACT and COVSZ * PCN0 == NS,
     "C1",
     "covers {0}, each of {1} pieces, each meets every cutting once, {1} x {2} = {3}".format(
         nd(NCOV), nd(COVSZ), nd(PCN0), nd(NS)))

gate(NGRP == 384 and NPROD == 147456 and GDISTINCT and CLOSED and MAP_FAMILY_OK
     and KEEPS and COVKEEP and PBIJ and PDIST and PIDOK and CBIJ and CDIST
     and CIDOK and ACTION_OK and len(ORBP) == NPI == 192 and len(ORBC) == NCOV == 192,
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


def orbit_partition_certificate(orbs):
    if len(orbs) != 96 or any(len(o) != 384 or len(set(o)) != 384 for o in orbs):
        return False
    flat = [x for o in orbs for x in o]
    return len(flat) == NPAIR and len(set(flat)) == NPAIR and set(flat) == set(range(NPAIR))


ORBIT_PARTITION_OK = orbit_partition_certificate(ORBS)

gate(NORB == 96 and OSZ == [384] and NPAIR == 36864
     and NORB * NGRP == NPAIR and min(WHICH) >= 0 and ORBIT_PARTITION_OK,
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
OHIST = dict((v, PRODO2.count(v)) for v in OD2)

gate(len(INVS) == 75 and len(PRODO2) == 900 and OD2 == [1, 2, 4, 8]
     and OHIST == {1: 12, 2: 216, 4: 480, 8: 192},
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


def cycle_partition_certificate(orbs, cycles):
    if len(orbs) != 96 or len(cycles) != 96:
        return False
    for orbit, table_cycles in zip(orbs, cycles):
        if len(table_cycles) != 48:
            return False
        edges = []
        for pcs, cvs in table_cycles:
            if len(pcs) != 4 or len(cvs) != 4 or len(set(pcs)) != 4 or len(set(cvs)) != 4:
                return False
            edges.extend(pcs[t] * NCOV + cvs[t] for t in range(4))
            edges.extend(pcs[(t + 1) & 3] * NCOV + cvs[t] for t in range(4))
        if len(edges) != 384 or set(edges) != set(orbit):
            return False
    return True


CYCLE_PARTITION_OK = cycle_partition_certificate(ORBS, CYCA)

CPT = sorted(CPTS)[0]
CL = sorted(CLENS)[0]

gate(CYCOK and CYCLE_PARTITION_OK and CLENS == set([8]) and CPTS == set([48])
     and CPT * CL == NGRP
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
     "the integral alternating vector on each of the {0} cycles is annihilated; the {1} per table form a kernel basis".format(
         nd(TOTC), nd(CPT)))

gate(is_prime(PRIME) and is_prime(PRIME2) and PRIME != PRIME2
     and all(v == RANKDER for v in RK1) and all(v == RANKDER for v in RK2)
     and len(RK1) + len(RK2) == 2 * NORB,
     "C18",
     "direct modular elimination gives rank {0} for all {1} tables at both primes, {2} measurements".format(
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

gate(R0 == RANKDER and BAD and RP == 145,
     "C19",
     "F_1000003 rejector: moving one row entry breaks two-regularity and moves rank from {0} to {1}".format(
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

gate(is_prime(PRIME) and is_prime(PRIME2) and IR1 == 105 and IR2 == 105
     and NPI - IR1 == 87 and RANKDER - IR1 == 39,
     "C22",
     "incidence rank {0} at F_1000003 and F_1000033, kernel {1}, excess {3} from singleton rank {4}".format(
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

gate(all(v == RANKDER for v in FR1) and len(FR1) == len(IORB)
     and PS == [72, 93, 117, 129, 144, 144],
     "C23",
     "at F_1000003 each of {0} summands has rank {1}; the {2} pair sums measure {3}".format(
         nd(len(IORB)), nd(RANKDER), nd(len(PS)), " ".join(nd(v) for v in PS)))

# ------------------------------------------------------------------
# 9. discriminating in-memory mutations for every load-bearing family
# ------------------------------------------------------------------


def freeness_certificate(fixp, fixc):
    return (len(fixp) == NGRP and len(fixc) == NGRP
            and all(e == IDG or not (fixp[e] > 0 and fixc[e] > 0)
                    for e in range(NGRP)))


def order_summary_ok(vals):
    hist = dict((v, vals.count(v)) for v in sorted(set(vals)))
    return len(vals) == 900 and hist == {1: 12, 2: 216, 4: 480, 8: 192}


def block_packet_certificate(table, cycles):
    if table.shape != (NCOV, NPI) or len(cycles) != 48:
        return False
    for pcs, cvs in cycles:
        if len(pcs) != 4 or len(cvs) != 4:
            return False
        ia = np.array(pcs, dtype=np.int64)
        ja = np.array(cvs, dtype=np.int64)
        if not np.array_equal(table[ja][:, ia], A4A):
            return False
        if int(table[ja].sum()) != 8 or int(table[:, ia].sum()) != 8:
            return False
    return True


def integral_kernel_packet(cycles):
    V = np.zeros((NPI, len(cycles)), dtype=np.int64)
    for t, (pcs, unused_covers) in enumerate(cycles):
        for u, piece in enumerate(pcs):
            V[piece, t] = 1 if (u & 1) == 0 else -1
    return V


def kernel_packet_certificate(table, vectors):
    return (vectors.shape == (NPI, 48)
            and bool(np.all(np.count_nonzero(vectors, axis=0) == 4))
            and bool(np.all(np.count_nonzero(vectors, axis=1) == 1))
            and set(np.unique(vectors)).issubset({-1, 0, 1})
            and bool(np.all(table.dot(vectors) == 0)))


def incidence_certificate(labels, summed, target):
    return (len(labels) == 4 and len(set(labels)) == 4
            and summed.shape == target.shape and np.array_equal(summed, target))


def pair_summary_ok(vals):
    return list(vals) == [72, 93, 117, 129, 144, 144]


BAD_MASKS = list(MASK)
BAD_MASKS[0] = 0
MUT_OBJECT = not mask_search_certificate(BAD_MASKS, SOLS)

BAD_DETS = list(KEPT_DET)
BAD_DETS[0] = 2
MUT_GEOMETRY = not continuous_cut_certificate(BAD_DETS, NFAC, NDIM, DISJ_OK)

BAD_MAPS = list(MAPS)
BAD_MAPS[-1] = BAD_MAPS[0]
MUT_GROUP = not map_family_certificate(BAD_MAPS)

BAD_PERM = list(PERM)
bad_identity = list(BAD_PERM[IDG])
bad_identity[0], bad_identity[1] = bad_identity[1], bad_identity[0]
BAD_PERM[IDG] = tuple(bad_identity)
MUT_ACTION = not action_certificate(BAD_PERM, CPERM)

BAD_FIXP = list(FIXP)
BAD_FIXP[SETC[0]] = 1
MUT_FREE = not freeness_certificate(BAD_FIXP, FIXC)

BAD_ORBITS = [list(o) for o in ORBS]
BAD_ORBITS[0] = BAD_ORBITS[0][:-1]
MUT_ORBITS = not orbit_partition_certificate(BAD_ORBITS)

BAD_CYCLES = list(CYCA)
bad_first_cycles = list(BAD_CYCLES[0])
bad_pieces, bad_covers = bad_first_cycles[0]
bad_first_cycles[0] = (bad_pieces[:-1], bad_covers)
BAD_CYCLES[0] = bad_first_cycles
MUT_CYCLES = not cycle_partition_certificate(ORBS, BAD_CYCLES)

BAD_ORDERS = list(PRODO2)
BAD_ORDERS[0] = 4 if BAD_ORDERS[0] != 4 else 1
MUT_ORDERS = not order_summary_ok(BAD_ORDERS)

FIRST_TABLE = np.zeros((NCOV, NPI), dtype=np.int64)
for x in ORBS[0]:
    i, j = divmod(x, NCOV)
    FIRST_TABLE[j, i] = 1
FIRST_KERNEL = integral_kernel_packet(CYCA[0])

BAD_BLOCK = FIRST_TABLE.copy()
bad_piece, bad_cover = divmod(ORBS[0][0], NCOV)
BAD_BLOCK[bad_cover, bad_piece] = 0
MUT_BLOCK = not block_packet_certificate(BAD_BLOCK, CYCA[0])

BAD_KERNEL = FIRST_KERNEL.copy()
BAD_KERNEL[int(np.nonzero(BAD_KERNEL[:, 0])[0][0]), 0] = 0
MUT_KERNEL = not kernel_packet_certificate(FIRST_TABLE, BAD_KERNEL)

MUT_RANK = (rank_modp([[1, 0], [1, 0]], PRIME) != 2)

BAD_SUM4 = SUM4.copy()
BAD_SUM4[0, 0] += 1
MUT_INCIDENCE = not incidence_certificate(IORB, BAD_SUM4, INC)

BAD_PAIR = list(PS)
BAD_PAIR[0] += 1
MUT_PAIR = not pair_summary_ok(BAD_PAIR)

MUTATIONS = [MUT_OBJECT, MUT_GEOMETRY, MUT_GROUP, MUT_ACTION, MUT_FREE, MUT_ORBITS,
             MUT_CYCLES, MUT_ORDERS, MUT_BLOCK, MUT_KERNEL, MUT_RANK,
             MUT_INCIDENCE, MUT_PAIR]

gate(all(MUTATIONS) and len(MUTATIONS) == 13,
     "C24",
     "mutations 13/13 reject: object/geometry/group/action/free/orbit/cycle/order/block/kernel/rank/incidence/pair")

emit("group {0}, orbits {1}, cycles {2}, every orbit table rank {3}, incidence rank {4}".format(
    nd(NGRP), nd(NORB), nd(TOTC), nd(RANKDER), nd(IR1)))
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
MBS = RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RSS / 1024.0
emit("elapsed {0} s, peak resident {1} MB".format(
    nd("{0:.1f}".format(time.time() - T0)), nd("{0:.1f}".format(MBS))))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
sys.exit(0 if STAT[1] == 0 else 1)
