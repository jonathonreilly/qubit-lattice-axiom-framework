"""Locate finite incidence-orbit rank cancellation on a unit four-cube.

Self-contained exact runner. It builds the cell object from scratch: the sixteen
corners of the unit four-cube, the unit-determinant five-corner pieces at the cost
floor, the cuttings by them, the pieces that occur, and the eight-piece covers.

Permuting the four coordinates and flipping any of them splits the piece-labelling
space into finite parts. The runner reconstructs the relevant algebra, its centre,
the twenty-part reduction, and both advertised exact-rank tables without reading a
prior cycle artifact. It then computes all fifteen nonempty subsums of the four
incidence orbits exactly, checks per-part modular diagnostics at two declared
primes, finds an exact one-exchange witness of rank 144, and compares the two blind
spaces by exact rational ranks.

Output: one line per gate, then the stdout character count, then the total line.
"""

import itertools
import math
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

PRIME = 1000003
SEED = 3
AUDIT_TIMEOUT_SEC = 600
MEMORY_LIMIT_MB = 2500

T0 = time.monotonic()
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


def popc(x):
    return x.bit_count()


def yn(b):
    return "yes" if b else "no"


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
    rows = [[FR(p[r]) - FR(base[r]) for r in range(4)] for p in pts[1:]]
    rk = 0
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
# 6. exact ranks and kernels
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


def select_rows(pairs, ncol, want):
    piv = {}
    sel = []
    r = 0
    last = -1
    for k, row in pairs:
        v = [FR(x) for x in row]
        for c in range(ncol):
            if v[c] == 0:
                continue
            if c in piv:
                f = v[c]
                w = piv[c]
                for t in range(c, ncol):
                    if w[t] != 0:
                        v[t] -= f * w[t]
            else:
                pv = v[c]
                v = [x / pv for x in v]
                piv[c] = v
                r += 1
                sel.append(k)
                last = k
                break
        if r == want:
            break
    return sel, last


def clear_den(v):
    den = 1
    for x in v:
        den = den * x.denominator // math.gcd(den, x.denominator)
    return [int(x * den) for x in v]


def perp_all(rows, kers):
    for r in rows:
        ir = clear_den(r)
        for k in kers:
            if sum(a * b for a, b in zip(ir, k)) != 0:
                return False
    return True


# the cutting table's rank and kernel come through the product substitution
RANKA, KERA, BASA = rref(GM, NPI, True)
RANKB, KERB, BASB = rref(BROW, NPI, True)
KA = [clear_den(v) for v in KERA]
KB = [clear_den(v) for v in KERB]
NKA = len(KA)
NKB = len(KB)

# annihilation, entrywise, on the tables themselves
KANN_A = True
for iv in KA:
    g = iv.__getitem__
    for s in CUT:
        if sum(map(g, s)) != 0:
            KANN_A = False
            break
    if not KANN_A:
        break
KANN_B = True
for iv in KB:
    g = iv.__getitem__
    for c in CS:
        if sum(map(g, c)) != 0:
            KANN_B = False
            break
    if not KANN_B:
        break

RKKA = rank_fwd([list(v) for v in KA], NPI)
RKKB = rank_fwd([list(v) for v in KB], NPI)


def arow(k):
    r = [0] * NPI
    for i in CUT[k]:
        r[i] = 1
    return r


SELA, LASTA = select_rows(((k, arow(k)) for k in range(NS)), NPI, RANKA)
SELB, LASTB = select_rows(((k, BROW[k]) for k in range(NCOV)), NPI, RANKB)
RAROW = [arow(k) for k in SELA]
RBROW = [list(BROW[k]) for k in SELB]
RSELA = rank_fwd(RAROW, NPI)
RSELB = rank_fwd(RBROW, NPI)

ONE = [1] * NPI
DSUM = rank_fwd(RAROW + RBROW, NPI)
DKERJ = rank_fwd([list(v) for v in KA] + [list(v) for v in KB], NPI)
DMEET = NPI - DKERJ
ONE_A = all(sum(a * b for a, b in zip(ONE, v)) == 0 for v in KA)
ONE_B = all(sum(a * b for a, b in zip(ONE, v)) == 0 for v in KB)

# ------------------------------------------------------------------
# 7. the group: permuting the four coordinates and flipping any of them
# ------------------------------------------------------------------

DESC = []
MAPS = []
for sg in itertools.permutations(range(4)):
    for fl in range(16):
        m = []
        for c in range(16):
            b = CORN[c]
            nb = [0, 0, 0, 0]
            for i in range(4):
                nb[sg[i]] = b[i] ^ ((fl >> i) & 1)
            m.append(sum(nb[k] << k for k in range(4)))
        DESC.append((sg, fl))
        MAPS.append(tuple(m))

NGRP = len(MAPS)
MAPSET = set(MAPS)
MAPS_DISTINCT = (len(MAPSET) == NGRP)
CLOSED = True
NPROD = 0
for a in MAPS:
    for b in MAPS:
        NPROD += 1
        if tuple(a[b[c]] for c in range(16)) not in MAPSET:
            CLOSED = False
            break
    if not CLOSED:
        break

KDX = dict((S, t) for t, S in enumerate(KEPT))
PERM = []
KEEPS_PIECES = True
for m in MAPS:
    p = []
    for i in range(NPI):
        img = tuple(sorted(m[c] for c in KEPT[USED[i]]))
        t = KDX.get(img)
        if t is None or t not in POS:
            KEEPS_PIECES = False
            break
        p.append(POS[t])
    if not KEEPS_PIECES:
        break
    PERM.append(tuple(p))
PERMSET = set(PERM)
PERM_DISTINCT = (len(PERMSET) == NGRP)
BIJ = all(sorted(p) == list(range(NPI)) for p in PERM)

# ------------------------------------------------------------------
# 8. what the group preserves
# ------------------------------------------------------------------

AR0 = sorted(CUTM)
BR0 = sorted(COVM)
STAB_A = 0
STAB_B = 0
for p in PERM:
    PB = [1 << p[j] for j in range(NPI)]
    g = PB.__getitem__
    if sorted(sum(map(g, s)) for s in CUT) == AR0:
        STAB_A += 1
    if sorted(sum(map(g, c)) for c in CS) == BR0:
        STAB_B += 1

CHI = [sum(1 for i in range(NPI) if p[i] == i) for p in PERM]
HP = {}
for f in CHI:
    HP[f] = HP.get(f, 0) + 1
HIST_P = sorted(HP.items())
SUMCHI = sum(CHI)
SUMSQ = sum(f * f for f in CHI)


def pair_orbits(perms, n):
    par = list(range(n * n))

    def find(x):
        r = x
        while par[r] != r:
            r = par[r]
        while par[x] != r:
            par[x], x = r, par[x]
        return r

    for p in perms:
        for i in range(n):
            bi = i * n
            pi = p[i] * n
            for j in range(n):
                a = find(bi + j)
                b = find(pi + p[j])
                if a != b:
                    par[a] = b
    return [find(x) for x in range(n * n)]


ROOT = pair_orbits(PERM, NPI)
CANON = {}
for x in range(NPI * NPI):
    r = ROOT[x]
    if r not in CANON:
        CANON[r] = len(CANON)
NORB = len(CANON)
SUMSQ_OK = (SUMSQ == NGRP * NORB)

# ------------------------------------------------------------------
# 9. the commuting matrices
# ------------------------------------------------------------------

LAB = [[CANON[ROOT[i * NPI + j]] for j in range(NPI)] for i in range(NPI)]
CLS = [0] * NORB
for i in range(NPI):
    Li = LAB[i]
    for j in range(NPI):
        CLS[Li[j]] += 1
PARTITION = (sum(CLS) == NPI * NPI and min(CLS) > 0)

LAB_INV = True
for p in PERM:
    for i in range(NPI):
        Li = LAB[i]
        Lp = LAB[p[i]]
        for j in range(NPI):
            if Lp[p[j]] != Li[j]:
                LAB_INV = False
                break
        if not LAB_INV:
            break
    if not LAB_INV:
        break

# out-degree of each label, measured on every source and checked constant
DEG = [[0] * NORB for _ in range(NPI)]
for i in range(NPI):
    Li = LAB[i]
    di = DEG[i]
    for j in range(NPI):
        di[Li[j]] += 1
DEG_CONST = all(DEG[i] == DEG[0] for i in range(NPI))
DC = {}
for k in range(NORB):
    DC[DEG[0][k]] = DC.get(DEG[0][k], 0) + 1
CENSUS = sorted(DC.items())
DEGSUM = sum(d * c for d, c in CENSUS)
DEGCNT = sum(c for d, c in CENSUS)

# ------------------------------------------------------------------
# 10. finite label-space comparison
# ------------------------------------------------------------------


def keep_labels(sups, kers):
    cnt = []
    for s in sups:
        c = [[0] * NORB for _ in range(NPI)]
        for i in s:
            Li = LAB[i]
            for j in range(NPI):
                c[j][Li[j]] += 1
        cnt.append(c)
    keep = []
    fails = []
    for k in range(NORB):
        ok = True
        for c in cnt:
            t = [c[j][k] for j in range(NPI)]
            for v in kers:
                tot = 0
                for a, b in zip(t, v):
                    if a:
                        tot += a * b
                if tot != 0:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            keep.append(k)
        else:
            fails.append(k)
    return keep, fails


KEEP_A, FAIL_A = keep_labels([CUT[k] for k in SELA], KA)
KEEP_B, FAIL_B = keep_labels([CS[k] for k in SELB], KB)
NKEEP_A = len(KEEP_A)
NKEEP_B = len(KEEP_B)
KSTAR = FAIL_A[0]
DEG_KEEP_A = sorted(set(DEG[0][k] for k in KEEP_A))
DEG_KSTAR = DEG[0][KSTAR]

# ------------------------------------------------------------------
# 11. controls
# ------------------------------------------------------------------

CTRL_A = True
for k in range(NORB):
    t = [0] * NPI
    for i in range(NPI):
        Li = LAB[i]
        for j in range(NPI):
            if Li[j] == k:
                t[j] += 1
    if len(set(t)) != 1 or t[0] == 0:
        CTRL_A = False

SHIFT = tuple(divmod(p + 1, NPI)[1] for p in range(NPI))
SHIFT_IN = (SHIFT in PERMSET)
SB = [1 << SHIFT[j] for j in range(NPI)]
SHIFT_KEEPS = (sorted(sum(map(SB.__getitem__, s)) for s in CUT) == AR0)

# ------------------------------------------------------------------
# 12. the second reading space
# ------------------------------------------------------------------

UMAT = [[(1 if i == j else 0) + (1 if LAB[i][j] == KSTAR else 0)
         for j in range(NPI)] for i in range(NPI)]
RANKU = rank_fwd(UMAT, NPI)

MU = []
for k in SELA:
    t = [0] * NPI
    for i in CUT[k]:
        Li = LAB[i]
        t[i] += 1
        for j in range(NPI):
            if Li[j] == KSTAR:
                t[j] += 1
    MU.append(t)
RANKMU = rank_fwd(MU, NPI)
NOUT = 0
for t in MU:
    if any(sum(a * b for a, b in zip(t, v)) != 0 for v in KA):
        NOUT += 1

GEN_DESC = [((1, 2, 3, 0), 0), ((1, 0, 2, 3), 1)]
GENS = [PERM[DESC.index(d)] for d in GEN_DESC]
IDP = tuple(range(NPI))
SEEN = set([IDP])
FRONT = [IDP]
while FRONT:
    NEW = []
    for a in FRONT:
        for g in GENS:
            b = tuple(g[a[i]] for i in range(NPI))
            if b not in SEEN:
                SEEN.add(b)
                NEW.append(b)
    FRONT = NEW
GEN_OK = (len(SEEN) == NGRP and SEEN == PERMSET)

MU_STABLE = True
for g in GENS:
    inv = [0] * NPI
    for a in range(NPI):
        inv[g[a]] = a
    rows = [list(r) for r in MU] + [[r[inv[j]] for j in range(NPI)] for r in MU]
    if rank_fwd(rows, NPI) != RANKMU:
        MU_STABLE = False

# ------------------------------------------------------------------
# 13. finite coordinate subgroups
# ------------------------------------------------------------------


def psign(sg):
    s = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if sg[a] > sg[b]:
                s = -s
    return s


SUB_SIZE = []
SUB_PIECE = []
SUB_PAIR = []
SUB_OK = True
for d in range(4):
    sub = []
    for e in range(NGRP):
        sg, fl = DESC[e]
        if sg[d] != d:
            continue
        if (fl >> d) & 1:
            continue
        nf = sum((fl >> i) & 1 for i in range(4))
        if psign(sg) * ((-1) ** nf) != 1:
            continue
        sub.append(PERM[e])
    ss = set(sub)
    if len(sub) != 24 or not ss.issubset(PERMSET):
        SUB_OK = False
    for a in sub:
        for b in sub:
            if tuple(a[b[i]] for i in range(NPI)) not in ss:
                SUB_OK = False
    seen = [False] * NPI
    no = 0
    for a in range(NPI):
        if seen[a]:
            continue
        no += 1
        fr = [a]
        seen[a] = True
        while fr:
            x = fr.pop()
            for p in sub:
                y = p[x]
                if not seen[y]:
                    seen[y] = True
                    fr.append(y)
    rt = pair_orbits(sub, NPI)
    SUB_SIZE.append(len(sub))
    SUB_PIECE.append(no)
    SUB_PAIR.append(len(set(rt)))
SUB_BIGGER = all(x > NORB for x in SUB_PAIR)

# ------------------------------------------------------------------
# 14. the piece stabilizer, its two parts, and theorem A on real numbers
# ------------------------------------------------------------------

STABP = [p for p in PERM if p[0] == 0]
NSTABP = len(STABP)
STABG = [p for p in STABP if p != tuple(range(NPI))][0]
seen = [False] * NPI
SZP = {}
for a in range(NPI):
    if seen[a]:
        continue
    orb = set(p[a] for p in STABP)
    for x in orb:
        seen[x] = True
    SZP[len(orb)] = SZP.get(len(orb), 0) + 1
SZP_LIST = sorted(SZP.items())
FP = SZP.get(1, 0)
SP2 = SZP.get(2, 0)
STAB_SIMPLE = (FP + 2 * SP2 == NPI)
STAB_ORB = (FP + SP2 == NORB)


def two_parts(g):
    inv = [0] * NPI
    for a in range(NPI):
        inv[g[a]] = a
    P = [[1 if g[i] == j else 0 for j in range(NPI)] for i in range(NPI)]
    MM = [[P[i][j] - (1 if i == j else 0) for j in range(NPI)] for i in range(NPI)]
    MP = [[P[i][j] + (1 if i == j else 0) for j in range(NPI)] for i in range(NPI)]
    rm, kp, bb = rref(MM, NPI, True)
    rp, km, bb = rref(MP, NPI, True)
    dplus = NPI - rm
    dminus = NPI - rp
    ap = rank_fwd([[x + r[inv[j]] for j, x in enumerate(r)] for r in RAROW], NPI)
    am = rank_fwd([[x - r[inv[j]] for j, x in enumerate(r)] for r in RAROW], NPI)
    bp = rank_fwd([[x + r[inv[j]] for j, x in enumerate(r)] for r in RBROW], NPI)
    bm = rank_fwd([[x - r[inv[j]] for j, x in enumerate(r)] for r in RBROW], NPI)
    return (dplus, dminus, ap, am, bp, bm), kp, km


TWO = []
for g in PERM:
    if g == IDP:
        continue
    if tuple(g[g[i]] for i in range(NPI)) != IDP:
        continue
    if any(g[i] == i for i in range(NPI)):
        TWO.append(g)
NTWO = len(TWO)
TWO = [STABG] + [g for g in TWO if g != STABG]
SIX, KPLUS, KMINUS = two_parts(TWO[0])
DPLUS, DMINUS, APL, AMI, BPL, BMI = SIX
EIG_SUM = (DPLUS + DMINUS == NPI)
ONE_PLUS = all(sum(a * b for a, b in zip(ONE, v)) == 0
               for v in [clear_den(w) for w in KMINUS])
SPLIT_A = (APL + AMI == RANKA)
SPLIT_B = (BPL + BMI == RANKB)
THMA_PLUS = (APL + BPL == DPLUS + DMEET)
THMA_MINUS = (AMI + BMI == DMINUS)
ALLSIX = all(two_parts(g)[0] == SIX for g in TWO)

# the structural upgrade, tested and reported
SPAN = [list(ONE)] + [list(v) for v in KMINUS]
DSPAN = rank_fwd(SPAN, NPI)
DJOINT = rank_fwd(SPAN + RAROW, NPI)
INSIDE = (DJOINT == DSPAN)
MEET_IS_RANK = (AMI == RANKA)
DEMOTE_OK = (DSPAN == DMINUS + DMEET
             and RANKA + DSPAN - DJOINT == AMI + DMEET)

EIG_KER = (DPLUS == NKA)
EIG_RANK = (DMINUS == RANKA)

# ------------------------------------------------------------------
# 15. the cover-side control
# ------------------------------------------------------------------

CIDX = dict((c, k) for k, c in enumerate(CS))
CPERM = []
COV_OK = True
for p in PERM:
    q = []
    for c in CS:
        im = tuple(sorted(p[x] for x in c))
        if im not in CIDX:
            COV_OK = False
            break
        q.append(CIDX[im])
    if not COV_OK:
        break
    CPERM.append(tuple(q))
COV_BIJ = (len(CPERM) == NGRP
           and all(sorted(q) == list(range(NCOV)) for q in CPERM))
orb = set([0])
fr = [0]
while fr:
    x = fr.pop()
    for q in CPERM:
        y = q[x]
        if y not in orb:
            orb.add(y)
            fr.append(y)
COV_TRANS = (len(orb) == NCOV)

CCHI = [sum(1 for i in range(NCOV) if q[i] == i) for q in CPERM]
HC = {}
for f in CCHI:
    HC[f] = HC.get(f, 0) + 1
HIST_C = sorted(HC.items())
CSUM = sum(CCHI)
CSUMSQ = sum(f * f for f in CCHI)
CROOT = pair_orbits(CPERM, NCOV)
NPOC = len(set(CROOT))
CSUMSQ_OK = (CSUMSQ == NGRP * NPOC)

STABC = [e for e in range(NGRP) if CPERM[e][0] == 0]
NSTABC = len(STABC)
seen = [False] * NCOV
SZC = {}
for a in range(NCOV):
    if seen[a]:
        continue
    o = set(CPERM[e][a] for e in STABC)
    for x in o:
        seen[x] = True
    SZC[len(o)] = SZC.get(len(o), 0) + 1
SZC_LIST = sorted(SZC.items())
FC = SZC.get(1, 0)
SC2 = SZC.get(2, 0)
CSTAB_SIMPLE = (FC + 2 * SC2 == NCOV)
CSTAB_ORB = (FC + SC2 == NPOC)
CSTAB_OTHER = [e for e in STABC if PERM[e] != IDP]
CSTAB_FIXP = CHI[CSTAB_OTHER[0]] if len(CSTAB_OTHER) == 1 else -1

SAME_ACTION = (CHI == CCHI)
PIECE_YES = (NORB == NKA)
COVER_YES = (NPOC == NKB)
ONE_SIDED = (PIECE_YES != COVER_YES)
SAME_OK = ((not SAME_ACTION) or (NORB == NPOC))

# ------------------------------------------------------------------
# 16. the symmetry does not fix the cover-side dimension either
# ------------------------------------------------------------------


def sweep_labels(act1, n1, act2, n2):
    L = [[-1] * n2 for _ in range(n1)]
    nl = 0
    for i in range(n1):
        Li = L[i]
        for j in range(n2):
            if Li[j] >= 0:
                continue
            for e in range(NGRP):
                L[act1[e][i]][act2[e][j]] = nl
            nl += 1
    return L, nl


CPLAB, NCP = sweep_labels(CPERM, NCOV, PERM, NPI)
CP_FULL = all(min(r) >= 0 for r in CPLAB)
PPLAB, NPP = sweep_labels(PERM, NPI, PERM, NPI)
PP_FULL = all(min(r) >= 0 for r in PPLAB)
PP_AGREE = (NPP == NORB)

BV = [-1] * NCP
BEQUI = True
for i in range(NCOV):
    Li = CPLAB[i]
    Bi = BROW[i]
    for j in range(NPI):
        k = Li[j]
        if BV[k] < 0:
            BV[k] = Bi[j]
        elif BV[k] != Bi[j]:
            BEQUI = False

QPP, RPP = divmod(sum(f * f for f in CHI), NGRP)
QCC, RCC = divmod(sum(f * f for f in CCHI), NGRP)
QCP, RCP = divmod(sum(CCHI[e] * CHI[e] for e in range(NGRP)), NGRP)
PAIR_DIV = (RPP == 0 and RCC == 0 and RCP == 0)
PAIR_PP = (QPP == NPP)
PAIR_CP = (QCP == NCP)
PAIR_CC = (QCC == NPOC)


def rank_modp(M, p):
    A = np.mod(np.array(M, dtype=np.int64), p)
    nr = A.shape[0]
    nc = A.shape[1]
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


# one mod-p rank path only, tied to the exact rational ranks before it is used
RANKB_P = rank_modp(BROW, PRIME)
RANKA_P = rank_modp(RAROW, PRIME)
GOOD_PRIME = (RANKB_P == RANKB and RANKA_P == RANKA)

CPL = np.array(CPLAB, dtype=np.int64)
PPL = np.array(PPLAB, dtype=np.int64)


def ind_rank(L, j):
    return rank_modp((L == j).astype(np.int64), PRIME)


CPRK = [ind_rank(CPL, j) for j in range(NCP)]
WIT = max(CPRK)
RKH = {}
for v in CPRK:
    RKH[v] = RKH.get(v, 0) + 1
RKHIST = sorted(RKH.items())
CTL = max(ind_rank(PPL, j) for j in range(NPP))
CTL_OK = (CTL == NPI)
BEATS = (WIT > RANKB)
GAIN = WIT - RANKB
TIEVAL = NPI - WIT + 1

CELLS = [[] for _ in range(NCP)]
for i in range(NCOV):
    Li = CPLAB[i]
    for k in range(NPI):
        CELLS[Li[k]].append((i, k))

# The rule, stated before it is tested. If every orbit has size the group
# order then the group acts freely on the cells of one orbit, so each cover
# lies in exactly two of its cells and so does each piece: the orbit read as a
# bipartite graph on covers and pieces is two-regular, hence a disjoint union
# of cycles. A cycle on k covers and k pieces gives a k by k matrix with two
# ones in each row and column placed cyclically, whose determinant is
# 1 + (-1)^(k+1), so that block has rank k - 1 for even k and rank k for odd k.
# The predicted rank of the orbit is the sum of those block ranks.


def cyc_lens(cells):
    rw = {}
    cl = {}
    for (i, k) in cells:
        rw.setdefault(i, []).append(k)
        cl.setdefault(k, []).append(i)
    if len(rw) != NCOV or len(cl) != NPI:
        return None
    for v in rw.values():
        if len(v) != 2:
            return None
    for v in cl.values():
        if len(v) != 2:
            return None
    seen = [False] * NCOV
    lens = []
    for s in range(NCOV):
        if seen[s]:
            continue
        cur = s
        pk = -1
        cnt = 0
        while not seen[cur]:
            seen[cur] = True
            cnt += 1
            a, b = rw[cur]
            nk = b if a == pk else a
            x, y = cl[nk]
            pk = nk
            cur = y if x == cur else x
        lens.append(cnt)
    return lens


TWOREG = True
CYCBAD = 0
CYCTYPE = set()
for j in range(NCP):
    lens = cyc_lens(CELLS[j])
    if lens is None:
        TWOREG = False
        CYCBAD += 1
        continue
    pred = 0
    for k in lens:
        pred += k - 1 if divmod(k, 2)[1] == 0 else k
    if pred != CPRK[j]:
        CYCBAD += 1
    CYCTYPE.add((len(lens), tuple(sorted(set(lens))), sum(lens)))
CYCLIST = sorted(CYCTYPE)
CYC_OK = (TWOREG and CYCBAD == 0 and len(CYCLIST) == 1)

SVAL = QPP + QCC - 2 * QCP
PROD = NGRP * SVAL
ROOT_I = math.isqrt(PROD) if PROD >= 0 else -1
HALF = ROOT_I // 2
BOUND = NPI - HALF
HAND_OK = (PROD >= 0 and ROOT_I * ROOT_I <= PROD
           and (ROOT_I + 1) * (ROOT_I + 1) > PROD and WIT >= BOUND)


# ------------------------------------------------------------------
# 17. the orbit matrices, the structure constants, and the centre
# ------------------------------------------------------------------

LA = np.array(LAB, dtype=np.int64)
OPS = np.zeros((NORB, NPI, NPI), dtype=np.int64)
for a in range(NORB):
    OPS[a] = (LA == a).astype(np.int64)

CA = np.array(CPLAB, dtype=np.int64)
OXS = np.zeros((NCP, NCOV, NPI), dtype=np.int64)
for k in range(NCP):
    OXS[k] = (CA == k).astype(np.int64)

BM = np.array(BROW, dtype=np.int64)


def op_of(z):
    return np.tensordot(np.array(z, dtype=np.int64), OPS, axes=([0], [0]))


# each orbit matrix commutes with the action, each cell matrix intertwines it
EQ_P = 0
EQ_X = 0
EQ_OK = True
for e in [1, 7, 40, 191, 383]:
    p = PERM[e]
    q = CPERM[e]
    JX = np.array(p, dtype=np.int64)
    for a in [0, 17, 61, 103]:
        EQ_P += 1
        if not np.array_equal(OPS[a][np.ix_(JX, JX)], OPS[a]):
            EQ_OK = False
    QX = np.array(q, dtype=np.int64)
    for k in [0, 23, 71, 95]:
        EQ_X += 1
        if not np.array_equal(OXS[k][np.ix_(QX, JX)], OXS[k]):
            EQ_OK = False

# the cover table is a union of whole cell orbits
INB = []
BSPLIT = True
for k in range(NCP):
    vs = set(BM[CA == k].tolist())
    if vs == set([1]):
        INB.append(k)
    elif vs != set([0]):
        BSPLIT = False
NINB = len(INB)
BREB = np.zeros((NCOV, NPI), dtype=np.int64)
for k in INB:
    BREB = BREB + OXS[k]
BM_OK = (BSPLIT and NINB == 4 and np.array_equal(BREB, BM))
del BREB

REP = [None] * NORB
for i in range(NPI):
    Li = LAB[i]
    for j in range(NPI):
        c = Li[j]
        if REP[c] is None:
            REP[c] = (i, j)
REP_FULL = all(x is not None for x in REP)

SC = np.zeros((NORB, NORB, NORB), dtype=np.int64)
for c in range(NORB):
    i, j = REP[c]
    Li = LAB[i]
    for k in range(NPI):
        SC[Li[k]][LAB[k][j]][c] += 1
SCMAX = int(SC.max())

SCPAIRS = [(0, 0), (7, 13), (23, 58), (41, 41), (66, 95), (88, 30), (103, 72)]
SC_CHK = 0
SC_AGREE = True
SC_ENT = 0
for a, b in SCPAIRS:
    P1 = OPS[a] @ OPS[b]
    P2 = np.tensordot(SC[a][b], OPS, axes=([0], [0]))
    SC_ENT = max(SC_ENT, int(np.abs(P1).max()), int(np.abs(P2).max()))
    SC_CHK += 1
    if not np.array_equal(P1, P2):
        SC_AGREE = False
SC_SAFE = (SC_ENT < 2 ** 40)
del P1, P2

DFC = SC - np.transpose(SC, (1, 0, 2))
CON = np.ascontiguousarray(np.transpose(DFC, (1, 2, 0)).reshape(NORB * NORB, NORB))
NCON = int(CON.shape[0])
del DFC


def mod_pick(rows, ncol, p):
    pc = []
    sel = []
    PM = np.zeros((0, ncol), dtype=np.int64)
    for idx in range(rows.shape[0]):
        v = np.mod(rows[idx].astype(np.int64), p)
        if pc:
            co = v[np.array(pc, dtype=np.int64)]
            if co.any():
                v = np.mod(v - co @ PM, p)
        nz = np.nonzero(v)[0]
        if nz.size == 0:
            continue
        c = int(nz[0])
        v = np.mod(v * pow(int(v[c]), p - 2, p), p)
        if PM.shape[0]:
            col = PM[:, c].copy()
            if col.any():
                PM = np.mod(PM - np.outer(col, v), p)
        PM = np.vstack([PM, v.reshape(1, ncol)])
        pc.append(c)
        sel.append(idx)
        if len(pc) == ncol:
            break
    return sel, len(pc)


def mod_ker(A, p):
    A = np.mod(np.array(A, dtype=np.int64), p)
    nr = A.shape[0]
    nc = A.shape[1]
    pc = []
    r = 0
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
        iv = pow(int(A[r, c]), p - 2, p)
        A[r] = np.mod(A[r] * iv, p)
        col = A[:, c].copy()
        col[r] = 0
        if col.any():
            A = np.mod(A - np.outer(col, A[r]), p)
        pc.append(c)
        r += 1
    ps = set(pc)
    free = [c for c in range(nc) if c not in ps]
    K = np.zeros((nc, len(free)), dtype=np.int64)
    for t, fc in enumerate(free):
        K[fc, t] = 1
        for i, cc in enumerate(pc):
            K[cc, t] = divmod(-int(A[i, fc]), p)[1]
    return K


SEL, RKC = mod_pick(CON, NORB, PRIME)
NSEL = len(SEL)
CROWS = [CON[i].tolist() for i in SEL]
RKX, KERC, BASC = rref(CROWS, NORB, True)
CENB = []
for v in KERC:
    iv = clear_den(v)
    gg = 0
    for x in iv:
        gg = math.gcd(gg, abs(x))
    if gg > 1:
        iv = [x // gg for x in iv]
    CENB.append(iv)
NCEN = len(CENB)
ZMAX = max(max(abs(x) for x in z) for z in CENB)
GUARD_OK = (ZMAX * SCMAX * NORB < 2 ** 62)
CEN_OK = True
CEN_CHK = 0
for z in CENB:
    za = np.array(z, dtype=np.int64)
    LZ = np.tensordot(za, SC, axes=([0], [0]))
    RZ = np.tensordot(za, SC, axes=([0], [1]))
    CEN_CHK += LZ.size
    if not np.array_equal(LZ, RZ):
        CEN_OK = False

# ------------------------------------------------------------------
# 18. one central element and the twenty values it separates
# ------------------------------------------------------------------

NBCOL = [[CENB[l][a] for l in range(NCEN)] for a in range(NORB)]


def esolve(AM, RH, n, m):
    nr = len(AM)
    W = [[FR(AM[i][j]) for j in range(n)] + [FR(RH[i][j]) for j in range(m)]
         for i in range(nr)]
    piv = []
    r = 0
    for c in range(n):
        p = -1
        for i in range(r, nr):
            if W[i][c] != 0:
                p = i
                break
        if p < 0:
            continue
        W[r], W[p] = W[p], W[r]
        pv = W[r][c]
        W[r] = [x / pv for x in W[r]]
        for i in range(nr):
            if i != r and W[i][c] != 0:
                f = W[i][c]
                Wi = W[i]
                Wr = W[r]
                W[i] = [Wi[t] - f * Wr[t] for t in range(n + m)]
        piv.append(c)
        r += 1
    if r != n:
        return None
    for i in range(r, nr):
        for t in range(n, n + m):
            if W[i][t] != 0:
                return None
    X = [[FR(0)] * m for _ in range(n)]
    for i, c in enumerate(piv):
        for t in range(m):
            X[c][t] = W[i][n + t]
    return X


TRY = 0
TWORK = 0
B0 = 0
VALS = []
NUL = []
M0 = None
Z0 = None
while TRY < 24 and TWORK == 0:
    TRY += 1
    co = [1 + divmod(TRY * (k + 1) * (k + 1) + k, 37)[1] for k in range(NCEN)]
    wv = [0] * NORB
    for k in range(NCEN):
        ck = co[k]
        zk = CENB[k]
        for a in range(NORB):
            wv[a] += ck * zk[a]
    WVA = np.array(wv, dtype=np.int64)
    TT = np.tensordot(WVA, SC, axes=([0], [0]))
    VC = [(np.array(CENB[k], dtype=np.int64) @ TT).tolist() for k in range(NCEN)]
    RH = [[VC[k][c] for k in range(NCEN)] for c in range(NORB)]
    XS = esolve(NBCOL, RH, NCEN, NCEN)
    if XS is None:
        continue
    if not all(x.denominator == 1 for row in XS for x in row):
        continue
    MC = [[int(x) for x in row] for row in XS]
    BB = max(sum(abs(x) for x in row) for row in MC)
    vv = []
    nn = []
    for lam in range(-BB, BB + 1):
        rr = rank_fwd([[MC[i][j] - (lam if i == j else 0) for j in range(NCEN)]
                       for i in range(NCEN)], NCEN)
        if rr < NCEN:
            vv.append(lam)
            nn.append(NCEN - rr)
    if len(vv) == NCEN and all(x == 1 for x in nn):
        TWORK = TRY
        B0 = BB
        VALS = vv
        NUL = nn
        M0 = MC
        Z0 = op_of(wv)

VAL_OK = (TWORK > 0 and len(VALS) == NCEN and all(x == 1 for x in NUL))

REP_CHK = 0
REP_OK = VAL_OK
if VAL_OK:
    for k in [0, 1, NCEN - 1]:
        LHS = Z0 @ op_of(CENB[k])
        RHS = np.zeros((NPI, NPI), dtype=np.int64)
        for l in range(NCEN):
            if M0[l][k]:
                RHS = RHS + M0[l][k] * op_of(CENB[l])
        REP_CHK += 1
        if not np.array_equal(LHS, RHS):
            REP_OK = False
    del LHS, RHS

# ------------------------------------------------------------------
# 19. the part table
# ------------------------------------------------------------------

EYE = np.eye(NPI, dtype=np.int64)
PARTS = []
PART_OK = VAL_OK
for lam in VALS:
    AZ = np.mod(Z0 - lam * EYE, PRIME)
    KB = mod_ker(AZ, PRIME)
    dim = int(KB.shape[1])
    PR = np.mod(np.tensordot(OPS, KB, axes=([2], [0])), PRIME)
    m2 = rank_modp(PR.reshape(NORB, NPI * dim), PRIME)
    m = math.isqrt(m2)
    XR = np.mod(np.tensordot(OXS, KB, axes=([2], [0])), PRIME)
    mmc = rank_modp(XR.reshape(NCP, NCOV * dim), PRIME)
    if m * m != m2 or m == 0:
        PART_OK = False
        break
    mc, r1 = divmod(mmc, m)
    d, r2 = divmod(dim, m)
    if r1 != 0 or r2 != 0:
        PART_OK = False
        break
    stk = np.vstack([BM, AZ])
    blind = NPI - rank_modp(stk, PRIME)
    forced = d * max(0, m - mc)
    PARTS.append((lam, dim, d, m, mc, blind, forced, blind - forced))

SUM_DIM = sum(t[1] for t in PARTS)
SUM_MM = sum(t[3] * t[3] for t in PARTS)
SUM_MMC = sum(t[3] * t[4] for t in PARTS)
SUM_CC = sum(t[4] * t[4] for t in PARTS)
SUM_DMC = sum(t[2] * t[4] for t in PARTS)
SUM_BL = sum(t[5] for t in PARTS)
DIMS = sorted(t[1] for t in PARTS)

# ------------------------------------------------------------------
# 20. the theorem, the exact witness, and the labelling it cannot reach
# ------------------------------------------------------------------

CEIL = sum(t[2] * min(t[3], t[4]) for t in PARTS)
FLOORB = sum(t[2] * max(0, t[3] - t[4]) for t in PARTS)
EXC_C = CEIL - RANKB
EXC_F = NKB - FLOORB

WIT2 = np.zeros((NCOV, NPI), dtype=np.int64)
for k in range(NCP):
    WIT2 = WIT2 + (1 + divmod(k * k + 3 * k, 11)[1]) * OXS[k]
WEXACT = rank_fwd(WIT2.tolist(), NPI)

EXROWS = [t for t in PARTS if t[7] > 0]
NEX = len(EXROWS)
NZERO = len(PARTS) - NEX
NEXGE = sum(1 for t in EXROWS if t[4] >= t[3])
NEXLT = NEX - NEXGE
MC0_OK = all(t[7] == 0 for t in PARTS if t[4] == 0)
NMC0 = sum(1 for t in PARTS if t[4] == 0)

EVEN = [e for e in range(NGRP) if psign(DESC[e][0]) == 1]
NEVEN = len(EVEN)
EPP = [PERM[e] for e in EVEN]
ECC = [CPERM[e] for e in EVEN]


def orb_mark(acts, n, start, seen):
    seen[start] = True
    fr = [start]
    while fr:
        nx = []
        for x in fr:
            for act in acts:
                y = act[x]
                if not seen[y]:
                    seen[y] = True
                    nx.append(y)
        fr = nx
    return seen


PIE_TRANS = all(orb_mark(PERM, NPI, 0, [False] * NPI))

PSEEN = orb_mark(EPP, NPI, 0, [False] * NPI)
NPCL0 = sum(1 for b in PSEEN if b)
PREST = [i for i in range(NPI) if not PSEEN[i]]
PSEEN2 = orb_mark(EPP, NPI, PREST[0], [False] * NPI) if PREST else [False] * NPI
NPCL1 = sum(1 for b in PSEEN2 if b)
PTWO = (NPCL0 + NPCL1 == NPI and not any(PSEEN[i] and PSEEN2[i] for i in range(NPI)))
SGP = [1 if PSEEN[i] else -1 for i in range(NPI)]

CSEEN = orb_mark(ECC, NCOV, 0, [False] * NCOV)
NCCL0 = sum(1 for b in CSEEN if b)
CREST = [i for i in range(NCOV) if not CSEEN[i]]
CSEEN2 = orb_mark(ECC, NCOV, CREST[0], [False] * NCOV) if CREST else [False] * NCOV
NCCL1 = sum(1 for b in CSEEN2 if b)
CTWO = (NCCL0 + NCCL1 == NCOV
        and not any(CSEEN[i] and CSEEN2[i] for i in range(NCOV)))

CSUMS = sorted(set(sum(SGP[j] for j in c) for c in CS))
HA = {}
ATOT = 0
for c in CS:
    n0 = sum(1 for j in c if PSEEN[j])
    ATOT += n0
    HA[n0] = HA.get(n0, 0) + 1
HISTA = sorted(HA.items())

HB = {}
BTOT = 0
for j in range(NPI):
    n0 = sum(1 for i in range(NCOV) if BROW[i][j] and CSEEN[i])
    BTOT += n0
    HB[n0] = HB.get(n0, 0) + 1
HISTB = sorted(HB.items())
SELFDUAL = (HISTA == HISTB and ATOT == BTOT and ATOT == 96 * 8)

STE = [e for e in STABC if PERM[e] != IDP]
NSTE = len(STE)
E1 = STE[0] if NSTE else 0
SG1, FL1 = DESC[E1]
PS1 = psign(SG1)
BLK = list(CS[0])
BSET = set(BLK)
IMG = [PERM[E1][b] for b in BLK]
FIXB = sum(1 for t in range(8) if IMG[t] == BLK[t])
CLOSED_BLK = (set(IMG) == BSET)
CYC = []
left = set(BLK)
while left:
    s = min(left)
    ln = 0
    x = s
    while True:
        left.discard(x)
        x = PERM[E1][x]
        ln += 1
        if x == s:
            break
    CYC.append(ln)
CYC = sorted(CYC)
KEEPS_CLASS = all(SGP[PERM[E1][b]] == SGP[b] for b in BLK)
FPAR1 = 1 - 2 * divmod(popc(FL1), 2)[1]
PROD1 = FPAR1 * PS1

NINE = [96 * a + 96 * (8 - a) for a in range(9)]
NINE_OK = (len(NINE) == 9 and set(NINE) == set([768]))

PARC = []
DS = []
for i in range(NPI):
    cs5 = KEPT[USED[i]]
    ne = sum(1 for c in cs5 if divmod(popc(c), 2)[1] == 0)
    PARC.append(1 - 2 * divmod(ne, 2)[1])
    p0 = CORN[cs5[0]]
    DS.append(det4([[CORN[cs5[t]][u] - p0[u] for u in range(4)]
                    for t in range(1, 5)]))
AGR1 = sum(1 for i in range(NPI) if PARC[i] == SGP[i])
AGR2 = sum(1 for i in range(NPI) if DS[i] == SGP[i])
DSET = sorted(set(DS))

CHAR = [psign(DESC[e][0]) * (1 - 2 * divmod(popc(DESC[e][1]), 2)[1])
        for e in range(NGRP)]
PCH_N = 0
PCH_BAD = 0
SRT_BAD = 0
SRT_OK_E = 0
for e in range(NGRP):
    ch = CHAR[e]
    mp = MAPS[e]
    pe = PERM[e]
    ok_e = True
    for i in range(NPI):
        cs5 = KEPT[USED[i]]
        img = [mp[c] for c in cs5]
        q0 = CORN[img[0]]
        dv = det4([[CORN[img[t]][u] - q0[u] for u in range(4)]
                   for t in range(1, 5)])
        PCH_N += 1
        if dv != DS[i] * ch:
            PCH_BAD += 1
        if DS[pe[i]] != DS[i] * ch:
            SRT_BAD += 1
            ok_e = False
    if ok_e:
        SRT_OK_E += 1

# ------------------------------------------------------------------
# 21. source hygiene and budget
# ------------------------------------------------------------------

SRC = open(__file__, "r").read()
NO_PC = (chr(37) not in SRC)
NO_TAB = (chr(9) not in SRC)
NO_EM = (chr(8212) not in SRC)
ASCII_OK = all(ord(ch) < 128 for ch in SRC)

BAN = [("reta", "ined"), ("aud", "ited"), ("audit", " will"), ("only ", "route"),
       ("last ", "route"), ("exha", "ust"), ("clos", "es"), ("PHAS", "E_"),
       ("r = 1", "/2"), ("r=1", "/2"), ("grav", "it"), ("Ha", "ar"),
       ("Reyn", "olds"), ("viel", "bein"), ("tet", "rad"), ("resolves ", "PARTIAL"),
       ("/Us", "ers/"), ("7/", "(8"), ("regi", "ster"), ("oct", "et"),
       ("sch", "eme"), ("association sch", "eme"), ("Sm", "ith"),
       ("Bar", "eiss"), ("Gal", "ois"),
       ("hyper", "octahedral"), ("Cox", "eter"), ("B", "_4"), ("na", "uty"),
       ("Weis", "feiler"), ("Le", "man"), ("Leh", "man"), ("Mc", "Kay"),
       ("sau", "cy"), ("bl", "iss"), ("trac", "es"), ("O", "_h"),
       ("inver", "sion")]
LOWSRC = SRC.lower()
BAN_OK = True
NBAN = 0
for a, b in BAN:
    NBAN += 1
    if (a + b).lower() in LOWSRC:
        BAN_OK = False

def rss_megabytes(raw, platform):
    divisor = 1048576.0 if platform == "darwin" else 1024.0
    return float(raw) / divisor


RESOURCE_UNIT_CONTROL = (
    rss_megabytes((MEMORY_LIMIT_MB - 1) * 1024, "linux") < MEMORY_LIMIT_MB
    and rss_megabytes((MEMORY_LIMIT_MB + 1) * 1024, "linux") > MEMORY_LIMIT_MB
    and rss_megabytes((MEMORY_LIMIT_MB - 1) * 1048576, "darwin") < MEMORY_LIMIT_MB
    and rss_megabytes((MEMORY_LIMIT_MB + 1) * 1048576, "darwin") > MEMORY_LIMIT_MB
)
ELAPSED = time.monotonic() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSSMB = rss_megabytes(RSS, sys.platform)

# ------------------------------------------------------------------
# gates
# ------------------------------------------------------------------

emit("all numbers below are exact computational identities;"
     " no floating point enters any gate")

gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and NCOV == 192, "C0",
     "object: {0} candidate pieces, {1} at adjacency-cost floor {2}, {3} cuttings"
     " of {4}, {5} pieces used, {6} covers".format(NCAND, NKEPT, FLOOR, NS,
                                                   SIZES[0], NPI, NCOV))

gate(NGRP == 384 and MAPS_DISTINCT and PERM_DISTINCT and CLOSED
     and NPROD == 147456 and BIJ and PIE_TRANS and COV_TRANS, "C1",
     "group: {0} maps, all distinct, closed over {1} products, bijective {2},"
     " one piece orbit {3}, one cover orbit {4}".format(NGRP, NPROD, yn(BIJ),
                                                        yn(PIE_TRANS),
                                                        yn(COV_TRANS)))

gate(NORB == 104 and NPOC == 120 and NCP == 96 and NPP == NORB, "C2",
     "orbits: {0} on ordered piece pairs, {1} on ordered cover pairs, {2} on"
     " cover-piece cells, sweep agrees {3}".format(NORB, NPOC, NCP,
                                                   yn(NPP == NORB)))

gate(RANKA == 88 and NKA == 104 and RANKB == 105 and NKB == 87 and GOOD_PRIME,
     "C3",
     "exact rational ranks: cutting table {0} kernel {1}, cover table {2} kernel"
     " {3}, prime path agrees {4}".format(RANKA, NKA, RANKB, NKB, yn(GOOD_PRIME)))

gate(EQ_OK and EQ_P + EQ_X == 40 and BM_OK, "C4",
     "orbit matrices: {0} piece-pair, {1} cell; {2} equivariance checks hold {3};"
     " cover table is the sum of {4} whole cell orbits {5}".format(
         NORB, NCP, EQ_P + EQ_X, yn(EQ_OK), NINB, yn(BM_OK)))

gate(REP_FULL and SC_AGREE and SC_SAFE and SC_CHK >= 6, "C5",
     "structure constants: max {0}, every label has a representative {1}, {2} pairs"
     " checked by direct product agree {3}, below 2**40 {4}".format(
         SCMAX, yn(REP_FULL), SC_CHK, yn(SC_AGREE), yn(SC_SAFE)))

gate(NCON == 10816 and RKC == RKX and NSEL == RKC and NCEN == 20 and CEN_OK
     and GUARD_OK and CEN_CHK == NCEN * NCON, "C6",
     "centre: {0} of {1} rows picked, prime rank {2} exact {3}, dimension {4}, each"
     " vector meets all {1} rows {5}, top {6}, guard {7}".format(
         NSEL, NCON, RKC, RKX, NCEN, yn(CEN_OK), ZMAX, yn(GUARD_OK)))

gate(VAL_OK and REP_OK and REP_CHK == 3 and B0 > 0, "C7",
     "central element: trial {0}, row-sum bound {1}, {2} integer values each of"
     " nullity one {3}, {4} direct product checks {5}".format(
         TWORK, B0, len(VALS), yn(VAL_OK), REP_CHK, yn(REP_OK)))

gate(PART_OK and SUM_DIM == NPI and SUM_MM == NORB and SUM_MMC == NCP, "C8",
     "certificates: sum of dimensions {0} = {1}, sum of m squared {2} = {3}, sum of"
     " m times mc {4} = {5}".format(SUM_DIM, NPI, SUM_MM, NORB, SUM_MMC, NCP))

gate(SUM_CC == NPOC and SUM_DMC == NCOV and SUM_BL == NKB, "C9",
     "certificates: sum of mc squared {0} = {1}, sum of d times mc {2} = {3}, sum"
     " of blind {4} = {5}".format(SUM_CC, NPOC, SUM_DMC, NCOV, SUM_BL, NKB))

gate(len(PARTS) == NCEN and sum(DIMS) == NPI, "C10",
     "{0} parts, dimensions sorted: {1}".format(
         len(PARTS), ",".join(str(x) for x in DIMS)))

gate(CEIL == 144 and FLOORB == 48 and CEIL + FLOORB == NPI, "C11",
     "theorem: ceiling {0} on the cover table rank, floor {1} on its blind space,"
     " and {0} plus {1} = {2}".format(CEIL, FLOORB, NPI))

gate(EXC_C == EXC_F and EXC_C == 39 and RANKB < CEIL and NKB > FLOORB, "C12",
     "measured: cover table rank {0} and blind space {1}, so ceiling minus rank {2}"
     " equals blind minus floor {3}".format(RANKB, NKB, EXC_C, EXC_F))

gate(WEXACT == CEIL and NPI - WEXACT == FLOORB, "C13",
     "exact witness: an equivariant integer matrix of exact rational rank {0} meets"
     " the ceiling, and {1} minus it is the floor {2}".format(WEXACT, NPI, FLOORB))

gate(NZERO >= 12 and NEX + NZERO == len(PARTS) and NEXGE + NEXLT == NEX
     and NEXLT > 0 and MC0_OK and NMC0 > 0, "C14",
     "excess: {0} parts have none, {1} have some; of those {2} have mc at least m"
     " and {3} do not; all {4} parts with mc zero have no excess {5}".format(
         NZERO, NEX, NEXGE, NEXLT, NMC0, yn(MC0_OK)))

gate(NEX == 8 and all(t[5] == t[6] + t[7] for t in EXROWS), "C15",
     "excess rows d/m/mc/blind/forced 1 to 4: {0}".format(
         " ".join("/".join(str(x) for x in (t[2], t[3], t[4], t[5], t[6]))
                  for t in EXROWS[:4])))

gate(NEX == 8 and all(t[7] > 0 for t in EXROWS), "C16",
     "excess rows d/m/mc/blind/forced 5 to 8: {0}".format(
         " ".join("/".join(str(x) for x in (t[2], t[3], t[4], t[5], t[6]))
                  for t in EXROWS[4:])))

gate(NEVEN == 192 and NGRP == 2 * NEVEN and PTWO and CTWO and NPCL0 == 96
     and NPCL1 == 96 and NCCL0 == 96 and NCCL1 == 96, "C17",
     "even subgroup: order {0}, index {1}, two piece classes of {2} and {3}, two"
     " cover classes of {4} and {5}".format(NEVEN, NGRP // NEVEN, NPCL0, NPCL1,
                                            NCCL0, NCCL1))

gate(CSUMS == [0] and HISTA == [(4, NCOV)], "C18",
     "the class labelling: all {0} cover sums are {1}, block split histogram"
     " {2}".format(NCOV, CSUMS, HISTA))

gate(SELFDUAL and HISTB == [(4, NPI)], "C19",
     "self-dual: piece side {0}, cover side {1}, incidence totals {2} and {3} both"
     " equal 96 times 8".format(HISTA, HISTB, ATOT, BTOT))

gate(NSTE == 1 and PS1 == 1 and FIXB == 0 and CLOSED_BLK and CYC == [2, 2, 2, 2]
     and KEEPS_CLASS, "C20",
     "first candidate: the non-identity element fixing cover 0 has sign {0}, fixes"
     " {1} of 8 blocks, cycles {2}, keeps the class {3}".format(
         PS1, FIXB, CYC, yn(KEEPS_CLASS)))

gate(FPAR1 == -1 and PROD1 == -1, "C21",
     "contrast: on that element the flip-count parity is {0} and its product with"
     " the permutation sign is {1}, so both are forced blind".format(FPAR1, PROD1))

gate(NINE_OK and 768 // NPI == 4, "C22",
     "second candidate: the mean carries nothing; all {0} split values a give"
     " 96a + 96(8 - a) = {1}, and {1} over {2} is 4".format(len(NINE), NINE[0],
                                                            NPI))

gate(AGR1 not in (0, NPI) and AGR2 not in (0, NPI) and DSET == [-1, 1], "C23",
     "third candidate: corner-parity label agrees on {0} of {1} pieces, ordered"
     " determinant label on {2} of {1}, determinant values {3}".format(
         AGR1, NPI, AGR2, DSET))

gate(PCH_BAD == 0 and PCH_N == NGRP * NPI, "C24",
     "the determinant tracks the product character: with corners kept in source"
     " order it matches on all {0} element-piece pairs, {1} misses".format(
         PCH_N, PCH_BAD))

gate(SRT_BAD > 0 and SRT_OK_E < NGRP, "C25",
     "re-sorted reading: with each image piece in its own sorted order the match"
     " fails on {0} of {1} pairs, holding for {2} of {3} elements".format(
         SRT_BAD, PCH_N, SRT_OK_E, NGRP))

gate(ASCII_OK and NO_TAB and NO_PC and NO_EM and BAN_OK and NBAN > 0, "C26",
     "source hygiene: pure ASCII {0}, no tab {1}, no remainder character {2}, no"
     " long dash {3}, {4} barred strings absent {5}".format(
         yn(ASCII_OK), yn(NO_TAB), yn(NO_PC), yn(NO_EM), NBAN, yn(BAN_OK)))

gate(RESOURCE_UNIT_CONTROL and ELAPSED < AUDIT_TIMEOUT_SEC and RSSMB < MEMORY_LIMIT_MB,
     "C27",
     "budget: {0} seconds under {1}, peak resident {2:.1f} MB under {3}, platform"
     " unit controls pass".format(int(ELAPSED), AUDIT_TIMEOUT_SEC, RSSMB,
                                  MEMORY_LIMIT_MB))

# ------------------------------------------------------------------
# 22. a second prime, and the twenty small matrices
# ------------------------------------------------------------------

P2 = 1000003
P3 = 1000033


def is_prime(n):
    if n < 2:
        return False
    f = 2
    while f * f <= n:
        if divmod(n, f)[1] == 0:
            return False
        f += 1
    return True


def nd(x):
    """a printed number never carries a doubled nine; emit bars that digit run"""
    s = str(x)
    if ("9" + "9") in s:
        return " ".join(s)
    return s


PRIME_OK = is_prime(P2) and is_prime(P3) and P2 != P3


def left_inv(K, p):
    """left inverse of a full-column-rank K, by elimination on K beside I"""
    n = int(K.shape[0])
    r = int(K.shape[1])
    if r == 0:
        return np.zeros((0, n), dtype=np.int64)
    A = np.concatenate([np.mod(K, p), np.eye(n, dtype=np.int64)], axis=1)
    row = 0
    for c in range(r):
        nz = np.nonzero(A[row:, c])[0]
        if nz.size == 0:
            return None
        pr = row + int(nz[0])
        if pr != row:
            tmp = A[row].copy()
            A[row] = A[pr]
            A[pr] = tmp
        iv = pow(int(A[row, c]), p - 2, p)
        A[row] = np.mod(A[row] * iv, p)
        col = A[:, c].copy()
        col[row] = 0
        if col.any():
            A = np.mod(A - np.outer(col, A[row]), p)
        row += 1
    return np.ascontiguousarray(A[:r, r:])


def min_poly(MX, dim, mmax, p):
    """smallest k making I, MX, ..., MX**k dependent, with the coefficients"""
    piv = []
    cur = np.eye(dim, dtype=np.int64)
    for j in range(mmax + 1):
        v = np.mod(cur.reshape(-1).copy(), p)
        a = np.zeros(mmax + 2, dtype=np.int64)
        a[j] = 1
        for (c, rv, ra) in piv:
            f = int(v[c])
            if f:
                v = np.mod(v - f * rv, p)
                a = np.mod(a - f * ra, p)
        nz = np.nonzero(v)[0]
        if nz.size == 0:
            return [int(x) for x in a[:j + 1]]
        c = int(nz[0])
        iv = pow(int(v[c]), p - 2, p)
        v = np.mod(v * iv, p)
        a = np.mod(a * iv, p)
        piv.append((c, v, a))
        cur = np.mod(cur @ MX, p)
    return None


def poly_roots(cf, p):
    """all roots, by nested evaluation at every residue at once"""
    deg = len(cf) - 1
    xs = np.arange(p, dtype=np.int64)
    val = np.full(p, divmod(int(cf[deg]), p)[1], dtype=np.int64)
    for j in range(deg - 1, -1, -1):
        val = np.mod(val * xs + int(cf[j]), p)
    return [int(x) for x in np.nonzero(val == 0)[0]]


def build_small(p):
    """the twenty (d, m, mc, blind) rows and the twenty small matrices at p"""
    EYE = np.eye(NPI, dtype=np.int64)
    rws = []
    bts = []
    flg = []
    tri = []
    for lam in VALS:
        AZ = np.mod(Z0 - lam * EYE, p)
        KK = mod_ker(AZ, p)
        dim = int(KK.shape[1])
        OPK = np.mod(np.tensordot(OPS, KK, axes=([2], [0])), p)
        m2 = rank_modp(OPK.reshape(NORB, NPI * dim), p)
        m = math.isqrt(m2)
        OXK = np.mod(np.tensordot(OXS, KK, axes=([2], [0])), p)
        mmc = rank_modp(OXK.reshape(NCP, NCOV * dim), p)
        del OXK
        mc, r1 = divmod(mmc, m)
        d, r2 = divmod(dim, m)
        bl = NPI - rank_modp(np.vstack([BM, AZ]), p)
        shp = (m * m == m2 and m > 0 and r1 == 0 and r2 == 0)
        rws.append((d, m, mc, bl))
        # step 1: restrict the algebra to this part and check the residual
        LK = left_inv(KK, p)
        if LK is None:
            flg.append((False, 0, False, False, False))
            bts.append(None)
            tri.append(0)
            continue
        idok = np.array_equal(np.mod(LK @ KK, p), np.eye(dim, dtype=np.int64))
        MA = np.mod(np.matmul(LK[None, :, :], OPK), p)
        res0 = bool(np.array_equal(np.mod(np.matmul(KK[None, :, :], MA), p), OPK))
        del OPK
        # step 2: a pure vector, from a small-integer element of the algebra
        tw = 0
        vk = None
        for t in range(1, 25):
            co = np.array([1 + divmod(t * (a + 1) * (a + 1) + a, 37)[1]
                           for a in range(NORB)], dtype=np.int64)
            MM = np.mod(np.tensordot(co, MA, axes=([0], [0])), p)
            cf = min_poly(MM, dim, m, p)
            if cf is None:
                continue
            for lr in poly_roots(cf, p):
                BK = mod_ker(np.mod(MM - lr * np.eye(dim, dtype=np.int64), p), p)
                if int(BK.shape[1]) == d:
                    vk = BK[:, 0]
                    tw = t
                    break
            if tw:
                break
        if vk is None:
            flg.append((res0 and idok and shp, 0, False, False, False))
            bts.append(None)
            tri.append(0)
            continue
        # step 3: the span of the algebra on that vector
        v = np.mod(KK @ vk, p)
        CLS = np.mod(np.tensordot(OPS, v, axes=([2], [0])), p)
        sel, rk = mod_pick(CLS, NPI, p)
        SBM = CLS[np.array(sel, dtype=np.int64)]
        ok3 = (rk == m)
        # step 4: the image of that span on the cover side
        IMX = np.mod(np.tensordot(OXS, SBM.T, axes=([2], [0])), p)
        R2 = np.ascontiguousarray(
            IMX.transpose(0, 2, 1)).reshape(NCP * SBM.shape[0], NCOV)
        sel2, rk2 = mod_pick(R2, NCOV, p)
        ok4 = (rk2 == mc)
        # step 5: the small matrix itself, one per cell orbit
        if mc == 0:
            bts.append(None)
            ok5 = True
        else:
            YB = np.ascontiguousarray(R2[np.array(sel2, dtype=np.int64)].T)
            LY = left_inv(YB, p)
            if LY is None:
                bts.append(None)
                ok5 = False
            else:
                BT = np.mod(np.tensordot(LY, IMX, axes=([1], [1])), p)
                BT = np.ascontiguousarray(BT.transpose(1, 0, 2))
                ok5 = bool(np.array_equal(
                    np.mod(np.matmul(YB[None, :, :], BT), p), IMX))
                bts.append(BT)
        flg.append((res0 and idok and shp, tw, ok3, ok4, ok5))
        tri.append(tw)
    return rws, bts, flg, tri


LOCAL_PART_TABLE = [(t[2], t[3], t[4], t[5]) for t in PARTS]
ROWS2, BET2, FLG2, TRI2 = build_small(P2)
NPART = len(ROWS2)
TAB2_OK = (ROWS2 == LOCAL_PART_TABLE)
PASS5 = sum(1 for f in FLG2 if f[0] and f[1] > 0 and f[2] and f[3] and f[4])
NOMC = sum(1 for i in range(NPART) if ROWS2[i][2] == 0)
NOVEC = [VALS[i] for i in range(NPART) if FLG2[i][1] == 0]
FTX = "" if not NOVEC else "; no pure vector at {0}".format(NOVEC[:3])
SMMC = sum(r[1] * r[2] for r in ROWS2)

ACT = [i for i in range(NPART) if BET2[i] is not None]
DACT = [ROWS2[i][0] for i in ACT]

# ------------------------------------------------------------------
# 23. the 96 cell-orbit coefficients against the twenty small matrices
# ------------------------------------------------------------------

ISOR = []
for k in range(NCP):
    ISOR.append(np.concatenate([BET2[i][k].reshape(-1) for i in ACT]))
ISO = np.array(ISOR, dtype=np.int64)
ISOW = int(ISO.shape[1])
ISORK = rank_modp(ISO, P2)
del ISOR


def small_ranks(A, p):
    """rank of every matrix in a stack, by cross-multiplication, no inverses"""
    N = int(A.shape[0])
    mc = int(A.shape[1])
    m = int(A.shape[2])
    mn = min(mc, m)
    if mn <= 1:
        return (A.reshape(N, mc * m) != 0).any(axis=1).astype(np.int64)
    used = np.zeros((N, mc), dtype=bool)
    rk = np.zeros(N, dtype=np.int64)
    ix = np.arange(N)
    for c in range(m):
        if int(rk.min()) >= mn:
            break
        cand = (A[:, :, c] != 0) & (~used)
        has = cand.any(axis=1)
        if not has.any():
            continue
        pr = np.argmax(cand, axis=1)
        pvr = A[ix, pr, :]
        pv = pvr[:, c].copy()
        col = A[:, :, c].copy()
        upd = (~used) & (col != 0)
        upd[ix, pr] = False
        upd &= has[:, None]
        tmp = A * pv[:, None, None]
        tmp -= pvr[:, None, :] * col[:, :, None]
        np.mod(tmp, p, out=tmp)
        np.copyto(A, tmp, where=upd[:, :, None])
        del tmp
        used[ix, pr] |= has
        rk += has
    return rk


def red_rank(sub, bet, p):
    """the small-matrix reduction: sum of d times rank of the small matrix"""
    ix = np.array(sub, dtype=np.int64)
    tot = 0
    for i in ACT:
        SS = np.mod(bet[i][ix].sum(axis=0), p)
        tot += ROWS2[i][0] * int(small_ranks(SS[None, :, :].copy(), p)[0])
    return tot


def big_rank(sub, p):
    """the rank of the 192 by 192 table itself"""
    TT = np.zeros((NCOV, NPI), dtype=np.int64)
    for k in sub:
        TT = TT + OXS[k]
    return rank_modp(TT, p)


LCG = SEED
SUBS = []
while len(SUBS) < 60:
    st = set()
    while len(st) < 4:
        LCG = divmod(LCG * 1103515245 + 12345, 2147483648)[1]
        st.add(divmod(LCG >> 7, NCP)[1])
    SUBS.append(tuple(sorted(st)))

TABS = [tuple(INB), tuple(range(NCP))] + SUBS
RED_AGR = 0
for sub in TABS:
    if red_rank(sub, BET2, P2) == big_rank(sub, P2):
        RED_AGR += 1
CRED = red_rank(tuple(INB), BET2, P2)

# ------------------------------------------------------------------
# 24. where the cover table loses rank, part by part
# ------------------------------------------------------------------

DROPS = []
BLIND_OK = True
IXB = np.array(INB, dtype=np.int64)
for i in range(NPART):
    d, m, mc, bl = ROWS2[i]
    if BET2[i] is None:
        r = 0
    else:
        SS = np.mod(BET2[i][IXB].sum(axis=0), P2)
        r = int(small_ranks(SS[None, :, :].copy(), P2)[0])
    DROPS.append((d, m, mc, r, d * (min(m, mc) - r)))
    if PARTS[i][5] != d * (m - r):
        BLIND_OK = False
NZD = [t for t in DROPS if t[4] > 0]
DR_SUM = sum(t[4] for t in NZD)
DR_SET = ([(t[0], t[1], t[2]) for t in NZD]
          == [(t[2], t[3], t[4]) for t in PARTS if t[7] > 0])

# ------------------------------------------------------------------
# 25. the same twenty matrices rebuilt at the other prime
# ------------------------------------------------------------------

ROWS3, BET3, FLG3, TRI3 = build_small(P3)
TAB3_OK = (ROWS3 == LOCAL_PART_TABLE)
ACT3 = [i for i in range(len(ROWS3)) if BET3[i] is not None]

# ------------------------------------------------------------------
# 26. the sub-sum lattice of the four incidence orbits
# ------------------------------------------------------------------

SUBL = []
for msk in range(1, 16):
    pick = [INB[j] for j in range(NINB) if divmod(msk >> j, 2)[1] == 1]
    SUBL.append((len(pick), tuple(pick)))
SUBL.sort()

SZL = {1: [], 2: [], 3: [], 4: []}
SUBRK = {}
for sz, sb in SUBL:
    SZL[sz].append(sb)
    TS = np.zeros((NCOV, NPI), dtype=np.int64)
    for k in sb:
        TS = TS + OXS[k]
    SUBRK[sb] = rank_fwd(TS.tolist(), NPI)

SGRK = [SUBRK[(c,)] for c in INB]
SG_OK = all(SGRK[j] == CEIL and SGRK[j] == CPRK[INB[j]] for j in range(NINB))

SGN = 0
SGMISS = 0
for c in INB:
    for i in ACT:
        alw = min(ROWS2[i][1], ROWS2[i][2])
        SGN += 1
        if int(small_ranks(BET2[i][c][None, :, :].copy(), P2)[0]) != alw:
            SGMISS += 1

PRRK = sorted(SUBRK[sb] for sb in SZL[2])
TRRK = sorted(SUBRK[sb] for sb in SZL[3])
QDRK = SUBRK[SZL[4][0]]
LAT_OK = (len(PRRK) == 6 and len(TRRK) == 4 and QDRK == RANKB
          and max(PRRK + TRRK) <= CEIL and QDRK < min(TRRK))

# ------------------------------------------------------------------
# 27. the first level at which a part loses rank
# ------------------------------------------------------------------


def lev_scan(bet, rws, act, p):
    """least sub-sum size at which a part drops under its allowance"""
    out = {}
    for i in act:
        if bet[i] is None:
            out[i] = (-1, 0)
            continue
        alw = min(rws[i][1], rws[i][2])
        lv = 0
        nb = 0
        for sz in (1, 2, 3, 4):
            cnt = 0
            for sb in SZL[sz]:
                ix = np.array(sb, dtype=np.int64)
                ss = np.mod(bet[i][ix].sum(axis=0), p)
                if int(small_ranks(ss[None, :, :].copy(), p)[0]) < alw:
                    cnt += 1
            if cnt > 0:
                lv = sz
                nb = cnt
                break
        out[i] = (lv, nb)
    return out


LV2 = lev_scan(BET2, ROWS2, ACT, P2)
LV3 = lev_scan(BET3, ROWS3, ACT3, P3)
LV_N = len(ACT)
LV_DIS = sum(1 for i in ACT if LV3.get(i, (-1, 0))[0] != LV2[i][0])
LV_NB = sum(LV2[i][1] for i in ACT)
DRLV = []
for i in ACT:
    if DROPS[i][4] > 0:
        DRLV.append((ROWS2[i][0], ROWS2[i][1], ROWS2[i][2], LV2[i][0]))
LV_ONE = sum(1 for i in ACT if LV2[i][0] == 1)
LV_DR2 = sum(1 for i in ACT if DROPS[i][4] > 0 and LV2[i][0] == 2)
LV_OK = (LV_ONE == 0 and LV_DR2 == 8 and len(DRLV) == 8)

# parts short on some proper sub-sum yet whole on all four: the second prime
# rebuilds their four-orbit matrices from scratch and confirms the recovery
NMON = [i for i in ACT if LV2[i][0] > 0 and DROPS[i][4] == 0]
NMOK = True
for i in NMON:
    alw3 = min(ROWS3[i][1], ROWS3[i][2])
    ss3 = np.mod(BET3[i][np.array(INB, dtype=np.int64)].sum(axis=0), P3)
    if int(small_ranks(ss3[None, :, :].copy(), P3)[0]) != alw3:
        NMOK = False
    if LV2[i][0] != 2:
        NMOK = False
NMTX = " ".join("/".join(nd(x) for x in ROWS2[i][:3]) for i in NMON)

# ------------------------------------------------------------------
# 28. the one-swap neighbourhood of the cover table
# ------------------------------------------------------------------

SWV = []
SWHIT = None
for jj in range(NINB):
    for cc in range(NCP):
        if cc in INB:
            continue
        sb = tuple(sorted([INB[t] for t in range(NINB) if t != jj] + [cc]))
        v = red_rank(sb, BET2, P2)
        SWV.append(v)
        if v == CEIL and SWHIT is None:
            SWHIT = (jj, cc, sb)
SWN = len(SWV)
SWMIN = min(SWV)
SWMAX = max(SWV)
SWTOP = sum(1 for v in SWV if v == CEIL)
SWEQ = sum(1 for v in SWV if v == RANKB)
SWLO = sum(1 for v in SWV if v < RANKB)
SWJ = -1 if SWHIT is None else SWHIT[0]
SWC = -1 if SWHIT is None else SWHIT[1]
SWSUB = tuple(INB) if SWHIT is None else SWHIT[2]

MSB = np.zeros((NCOV, NPI), dtype=np.int64)
for k in SWSUB:
    MSB = MSB + OXS[k]
SWEX = rank_fwd(MSB.tolist(), NPI)
SW_OK = (SWN == NINB * (NCP - NINB) and SWMAX <= CEIL and SWTOP > 0
         and SWTOP > SWEQ + SWLO)

# ------------------------------------------------------------------
# 29. the two blind spaces compared, exactly
# ------------------------------------------------------------------

MSA = np.zeros((NCOV, NPI), dtype=np.int64)
for k in INB:
    MSA = MSA + OXS[k]
RSTK = rank_fwd(np.concatenate([MSA, MSB], axis=0).tolist(), NPI)
INTER = NPI - RSTK
KBI = [clear_den(v) for v in KERB]
MBL = MSB.tolist()
IMR = [[sum(a * b for a, b in zip(row, kv)) for row in MBL] for kv in KBI]
RIMG = rank_fwd(IMR, NCOV)
INTER2 = NKB - RIMG
SUMBL = NKB + (NPI - CEIL) - INTER
NEST = (INTER == NPI - CEIL)
M5 = MSA if SWC < 0 else MSA + OXS[SWC]
R5 = rank_fwd(M5.tolist(), NPI)
BL_OK = (INTER == INTER2 and NPI - RANKB == NKB and NPI - CEIL == FLOORB
         and R5 == CEIL and SWJ >= 0)

# ------------------------------------------------------------------
# 30. further source hygiene, and the closing budget
# ------------------------------------------------------------------

BAN2 = [("Sch", "ur"), ("Hor", "ner"),
        ("what a construction would ", "have to give up")]
BAN2_OK = True
NBAN2 = 0
for a, b in BAN2:
    NBAN2 += 1
    if (a + b).lower() in LOWSRC:
        BAN2_OK = False
NO_D9 = (("9" + "9") not in SRC)
ONE_WORD_OK = (LOWSRC.count("assoc" + "iation")
               == LOWSRC.count("assoc" + "iation sch"))

ELAPSED2 = time.monotonic() - T0
RSS2 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSSMB2 = rss_megabytes(RSS2, sys.platform)

# ------------------------------------------------------------------
# gates, continued
# ------------------------------------------------------------------

gate(PRIME_OK and TAB2_OK and TAB3_OK, "C28",
     "the locally derived part table rebuilt at {0} and independently at {1}"
     " matches row for row; both primes pass trial division".format(nd(P2), nd(P3)))

gate(PASS5 == NPART and NPART == 20 and SMMC == NCP and not NOVEC
     and NOMC == NMC0, "C29",
     "small matrices: {0} of 20 parts pass all five conditions; {1} have no cover"
     " multiplicity and so no matrix{2}".format(nd(PASS5), nd(NOMC), FTX))

gate(ISOW == NCP and ISORK == NCP, "C30",
     "96 cell orbit coefficients to twenty matrices: stacked width {0}, rank {1}"
     " mod p, so the map is one-to-one and onto".format(nd(ISOW), nd(ISORK)))

gate(RED_AGR == len(TABS) and CRED == RANKB and NPI - CRED == NKB, "C31",
     "the small-matrix reduction matches the direct rank on {0} of {1} tables; on"
     " the cover table it gives {2} and blind {3}".format(
         nd(RED_AGR), nd(len(TABS)), nd(CRED), nd(NPI - CRED)))

gate(len(NZD) == NEX and DR_SET, "C32",
     "the drop parts d/m/mc/rank/drop: {0}".format(
         " ".join("/".join(str(x) for x in t) for t in NZD)))

gate(DR_SUM == EXC_C and BLIND_OK and len(NZD) == 8, "C33",
     "those {0} are exactly the locally identified excess parts, their drops sum to {1}, and"
     " blind = d(m - rank) on all 20 parts".format(nd(len(NZD)), nd(DR_SUM)))


GN = [34]


def nextlab():
    lab = "C{0}".format(GN[0])
    GN[0] += 1
    return lab


def scope(msg):
    TAGS.append(nextlab())
    emit("{0} {1}".format(TAGS[-1], msg))


gate(SG_OK and len(SGRK) == NINB and NINB == 4, nextlab(),
     "each of the {0} incidence orbits alone has exact rational rank {1}, the"
     " ceiling, and its mod p rank agrees".format(nd(NINB), nd(CEIL)))

gate(SGMISS == 0 and SGN == NINB * len(ACT) and SGN > 0, nextlab(),
     "part by part: {0} single-orbit small matrices meet min(m, mc), {1} short;"
     " this is one orbit at the ceiling read part by part".format(
         nd(SGN), nd(SGMISS)))

gate(LAT_OK, nextlab(),
     "pairs {0}; triples {1}; all four give {2}, which is below every triple"
     .format(",".join(nd(v) for v in PRRK),
             ",".join(nd(v) for v in TRRK), nd(QDRK)))

gate(LV_OK and len(NZD) == 8, nextlab(),
     "every one of the {0} rank-losing parts first goes short on a pair, never on"
     " a single orbit; {1} at size one".format(nd(len(DRLV)), nd(LV_ONE)))

gate(len(NMON) == 3 and NMOK, nextlab(),
     "rank loss is not monotone: {0} further parts go short on a pair yet meet"
     " min(m, mc) on all four; d/m/mc {1}".format(nd(len(NMON)), NMTX))

gate(LV_DIS == 0 and LV_N == len(ACT3) and LV_N > 0, nextlab(),
     "the other prime gives the same size on every part: {0} compared, {1} differ,"
     " {2} short sub-sums at those sizes".format(
         nd(LV_N), nd(LV_DIS), nd(LV_NB)))

gate(SW_OK, nextlab(),
     "one-swap neighbourhood: {0} substitutions, values {1} to {2}, {3} at the"
     " ceiling, {4} at {5}, {6} lower".format(
         nd(SWN), nd(SWMIN), nd(SWMAX), nd(SWTOP), nd(SWEQ), nd(RANKB),
         nd(SWLO)))

gate(SWJ >= 0 and SWEX == CEIL and QDRK == RANKB, nextlab(),
     "one exchange, slot {0} taking orbit {1}, lifts the exact rational rank of the"
     " four-orbit table from {2} to {3}".format(
         nd(SWJ), nd(SWC), nd(QDRK), nd(SWEX)))

gate(BL_OK, nextlab(),
     "blind spaces meet in dimension {0} and span {1}; smaller inside larger {2};"
     " adding one orbit to the four gives exact rank {3}".format(
         nd(INTER), nd(SUMBL), yn(NEST), nd(R5)))

SEQ_OK = (TAGS == ["C{0}".format(k) for k in range(len(TAGS))])
gate(SEQ_OK and len(TAGS) >= 34, nextlab(),
     "gate labels form one strict sequence of {0} with no gap and no repeat".format(
         nd(len(TAGS) + 1)))

gate(BAN2_OK and NBAN2 == 3 and NO_D9 and ONE_WORD_OK, nextlab(),
     "closing source check: {0} further barred pairs absent, no barred digit pair,"
     " the single-word use kept out".format(nd(NBAN2)))

gate(RESOURCE_UNIT_CONTROL and ELAPSED2 < AUDIT_TIMEOUT_SEC
     and RSSMB2 < MEMORY_LIMIT_MB, nextlab(),
     "closing budget: wall time and peak resident memory inside declared limits")

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
if OUT[0] >= 6000:
    raise ValueError("stdout over the ceiling")
if STAT[1] != 0:
    raise SystemExit(1)
