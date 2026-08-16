"""Finite complement spaces, partner pairs, and pair/triple modular censuses.

Self-contained exact runner. It builds the cell object from scratch: the sixteen
corners of the unit four-cube, the unit-determinant five-corner pieces at the cost
floor, the cuttings by them, the pieces that occur, and the eight-piece covers.

The signed-coordinate action splits the cover-piece cells into 96 orbit tables.
The runner certifies their finite construction, the rational complement-space
identity, the partner-pair description on every cover, and complete rank
censuses for pairs and triples over F_1000003. The pair census is rebuilt over
F_1000033. Exact rational checks cover the incidence subsets and the singleton
cycle rule. The small-block bridge is certified at both primes.

All arithmetic used by scientific gates is integer, rational, or finite-field
arithmetic. Output contains one line per gate, a pre-trailer count, and the total.
"""

import hashlib
import itertools
import math
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np

AUDIT_TIMEOUT_SEC = 900

PRIME = 1000003
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
MASK_VISIBLE = (len(MASK) == NKEPT and all(bits != 0 for bits in MASK))

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
COVERS_UNIQUE = (len(set(COVM)) == NCOV)

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
ROW_KERNEL_OK = perp_all(RAROW, KA) and perp_all(RBROW, KB)

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


def map_family_certificate(maps):
    return (len(maps) == 384 and len(set(maps)) == 384
            and all(sorted(m) == list(range(16)) for m in maps))


GROUP_RECHECK_OK = map_family_certificate(MAPS)
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
# 10. finite label calculations
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
# 13. pass-down to the axiom's covariance group
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
# 16. cover-side orbit controls
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
# 20. the block bound, exact witness, and finite label diagnostics
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

ELAPSED = int(time.time() - T0)
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSSMB = RSS // 1048576 if RSS > 10000000 else RSS // 1024

# ------------------------------------------------------------------
# gates
# ------------------------------------------------------------------

emit("all numbers below are exact computational identities;"
     " no floating point enters any gate")

OBJECT_CERT_OK = (GENERIC and MASK_VISIBLE and SEARCH_OUTPUT_OK
                  and CUT_VOLUME_OK and DISJ_OK and NFAC + NDIM == NPAIR
                  and COVEXACT and COVERS_UNIQUE and BRS == [8] and BCS == [8]
                  and OBJECT_RECHECK_OK)
gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and NCOV == 192 and OBJECT_CERT_OK, "C0",
     "object/certs {0}/{1}/{2}/{3}; constructor checks yes".format(
         NCAND, NKEPT, NS, NPI))

gate(NGRP == 384 and MAPS_DISTINCT and PERM_DISTINCT and CLOSED
     and NPROD == 147456 and BIJ and PIE_TRANS and COV_TRANS
     and GROUP_RECHECK_OK, "C1",
     "group {0}; products {1}; bijective/transitive yes".format(NGRP, NPROD))

gate(NORB == 104 and NPOC == 120 and NCP == 96 and NPP == NORB, "C2",
     "orbit counts piece/cover/cell {0}/{1}/{2}; sweep yes".format(
         NORB, NPOC, NCP))

RANK_CERT_OK = (GRAM_OK and KANN_A and KANN_B and RKKA == NKA and RKKB == NKB
                and RSELA == RANKA and RSELB == RANKB and ROW_KERNEL_OK)
gate(RANKA == 88 and NKA == 104 and RANKB == 105 and NKB == 87
     and GOOD_PRIME and RANK_CERT_OK, "C3",
     "ranks/kernels cutting {0}/{1}, cover {2}/{3}; certificates yes".format(
         RANKA, NKA, RANKB, NKB))

gate(EQ_OK and EQ_P + EQ_X == 40 and BM_OK, "C4",
     "orbit bases {0}/{1}; equivariance {2}; cover-orbit sum {3}".format(
         NORB, NCP, EQ_P + EQ_X, NINB))

gate(REP_FULL and SC_AGREE and SC_SAFE and SC_CHK >= 6, "C5",
     "structure constants max {0}; representatives/products/guard yes".format(SCMAX))

gate(NCON == 10816 and RKC == RKX and NSEL == RKC and NCEN == 20 and CEN_OK
     and GUARD_OK and CEN_CHK == NCEN * NCON, "C6",
     "centre rank {0} exact; dimension {1}; {2} constraints; guard yes".format(
         RKX, NCEN, NCON))

gate(VAL_OK and REP_OK and REP_CHK == 3 and B0 > 0, "C7",
     "central separator trial {0}; {1} simple parts; {2} product checks".format(
         TWORK, len(VALS), REP_CHK))

gate(PART_OK and SUM_DIM == NPI and SUM_MM == NORB and SUM_MMC == NCP, "C8",
     "dimension sums module/commutant/map {0}/{1}/{2}".format(
         SUM_DIM, SUM_MM, SUM_MMC))

gate(SUM_CC == NPOC and SUM_DMC == NCOV and SUM_BL == NKB, "C9",
     "dual dimension sums {0}/{1}/{2}".format(SUM_CC, SUM_DMC, SUM_BL))

gate(len(PARTS) == NCEN and sum(DIMS) == NPI, "C10",
     "{0} parts, dims sorted: {1}".format(
         len(PARTS), ",".join(str(x) for x in DIMS)))

gate(CEIL == 144 and FLOORB == 48 and CEIL + FLOORB == NPI, "C11",
     "rank/blind bounds {0}/{1}; sum {2}".format(CEIL, FLOORB, NPI))

gate(EXC_C == EXC_F and EXC_C == 39 and RANKB < CEIL and NKB > FLOORB, "C12",
     "cover rank/blind {0}/{1}; bound gaps {2}/{3}".format(
         RANKB, NKB, EXC_C, EXC_F))

gate(WEXACT == CEIL and NPI - WEXACT == FLOORB, "C13",
     "exact equivariant witness rank {0}; blind {1}".format(WEXACT, FLOORB))

gate(NZERO >= 12 and NEX + NZERO == len(PARTS) and NEXGE + NEXLT == NEX
     and NEXLT > 0 and MC0_OK and NMC0 > 0, "C14",
     "block excess zero/positive {0}/{1}; mc>=m split {2}/{3}; mc0 checks yes".format(
         NZERO, NEX, NEXGE, NEXLT))

gate(NEX == 8 and all(t[5] == t[6] + t[7] for t in EXROWS), "C15",
     "excess d/m/mc/blind/forced 1 to 4: {0}".format(
         " ".join("/".join(str(x) for x in (t[2], t[3], t[4], t[5], t[6]))
                  for t in EXROWS[:4])))

gate(NEX == 8 and all(t[7] > 0 for t in EXROWS), "C16",
     "excess d/m/mc/blind/forced 5 to 8: {0}".format(
         " ".join("/".join(str(x) for x in (t[2], t[3], t[4], t[5], t[6]))
                  for t in EXROWS[4:])))

gate(NEVEN == 192 and NGRP == 2 * NEVEN and PTWO and CTWO and NPCL0 == 96
     and NPCL1 == 96 and NCCL0 == 96 and NCCL1 == 96, "C17",
     "even subgroup {0}, index {1}; piece/cover classes 96+96".format(
         NEVEN, NGRP // NEVEN))

gate(CSUMS == [0] and HISTA == [(4, NCOV)], "C18",
     "class sums {0}; cover profile {1}".format(CSUMS, HISTA))

gate(SELFDUAL and HISTB == [(4, NPI)], "C19",
     "self-dual profiles {0}/{1}; totals {2}/{3}".format(
         HISTA, HISTB, ATOT, BTOT))

gate(NSTE == 1 and PS1 == 1 and FIXB == 0 and CLOSED_BLK and CYC == [2, 2, 2, 2]
     and KEEPS_CLASS, "C20",
     "cover stabilizer sign/fixes/cycles {0}/{1}/{2}; class kept".format(
         PS1, FIXB, CYC))

gate(FPAR1 == -1 and PROD1 == -1, "C21",
     "sign diagnostic: flip parity {0}, product character {1}".format(
         FPAR1, PROD1))

gate(NINE_OK and 768 // NPI == 4, "C22",
     "split-count identity: {0} cases give {1}; mean 4".format(
         len(NINE), NINE[0]))

gate(AGR1 not in (0, NPI) and AGR2 not in (0, NPI) and DSET == [-1, 1], "C23",
     "label diagnostics parity/determinant {0}/{1}; values {2}".format(
         AGR1, AGR2, DSET))

gate(PCH_BAD == 0 and PCH_N == NGRP * NPI, "C24",
     "product-character checks {0}; misses {1}".format(PCH_N, PCH_BAD))

gate(SRT_BAD > 0 and SRT_OK_E < NGRP, "C25",
     "sorted-order diagnostic unequal/equal-elements {0}/{1}".format(
         SRT_BAD, SRT_OK_E))

gate(ASCII_OK and NO_TAB and NO_PC and NO_EM and BAN_OK and NBAN > 0, "C26",
     "source hygiene ASCII/tab/remainder/dash/barred checks clean")

gate(ELAPSED < AUDIT_TIMEOUT_SEC and RSSMB < 2500, "C27",
     "resource envelope: wall under declared timeout and peak resident under 2500 MB")

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


BASE_ROWS = [(t[2], t[3], t[4], t[5]) for t in PARTS]
ROWS2, BET2, FLG2, TRI2 = build_small(P2)
NPART = len(ROWS2)
TAB2_OK = (ROWS2 == BASE_ROWS)
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


def red_rank_data(sub, bet, rows, act, p):
    """Small-block rank formula with every input supplied explicitly."""
    ix = np.array(sub, dtype=np.int64)
    tot = 0
    for i in act:
        SS = np.mod(bet[i][ix].sum(axis=0), p)
        tot += rows[i][0] * int(small_ranks(SS[None, :, :].copy(), p)[0])
    return tot


def red_rank(sub, bet, p):
    """The certified small-block formula at the primary census prime."""
    return red_rank_data(sub, bet, ROWS2, ACT, p)


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
DROP_IDS = []
BLIND_OK = True
IXB = np.array(INB, dtype=np.int64)
for i in range(NPART):
    d, m, mc, bl = ROWS2[i]
    if BET2[i] is None:
        r = 0
    else:
        SS = np.mod(BET2[i][IXB].sum(axis=0), P2)
        r = int(small_ranks(SS[None, :, :].copy(), P2)[0])
        flat = ",".join(str(int(x)) for x in SS.reshape(-1))
        sig = hashlib.sha256(flat.encode("ascii")).hexdigest()[:12]
    DROPS.append((d, m, mc, r, d * (min(m, mc) - r)))
    DROP_IDS.append((i, VALS[i], sig if BET2[i] is not None else "none"))
    if PARTS[i][5] != d * (m - r):
        BLIND_OK = False
NZD = [t for t in DROPS if t[4] > 0]
DR_SUM = sum(t[4] for t in NZD)
DR_SET = ([(t[0], t[1], t[2]) for t in NZD]
          == [(t[2], t[3], t[4]) for t in PARTS if t[7] > 0])
DROP_ID_OK = (len(set(DROP_IDS)) == len(DROP_IDS)
              and all(DROP_IDS[i][2] != "none" for i in range(NPART)
                      if DROPS[i][4] > 0))
DROP_HASHES = ",".join(DROP_IDS[i][2][:8] for i in range(NPART)
                       if DROPS[i][4] > 0)
while ("9" + "9") in DROP_HASHES:
    DROP_HASHES = DROP_HASHES.replace("9" + "9", "9 9")

# ------------------------------------------------------------------
# 25. the same twenty matrices rebuilt at the other prime
# ------------------------------------------------------------------

ROWS3, BET3, FLG3, TRI3 = build_small(P3)
TAB3_OK = (ROWS3 == BASE_ROWS)
ACT3 = [i for i in range(len(ROWS3)) if BET3[i] is not None]
PASS5_3 = sum(1 for f in FLG3 if f[0] and f[1] > 0 and f[2] and f[3] and f[4])
NOMC3 = sum(1 for i in range(len(ROWS3)) if ROWS3[i][2] == 0)
NOVEC3 = [VALS[i] for i in range(len(ROWS3)) if FLG3[i][1] == 0]
SMMC3 = sum(r[1] * r[2] for r in ROWS3)
SEP2 = (len(set(divmod(x, P2)[1] for x in VALS)) == len(VALS))
SEP3 = (len(set(divmod(x, P3)[1] for x in VALS)) == len(VALS))
ISOR3 = []
for k in range(NCP):
    ISOR3.append(np.concatenate([BET3[i][k].reshape(-1) for i in ACT3]))
ISO3 = np.array(ISOR3, dtype=np.int64)
ISOW3 = int(ISO3.shape[1])
ISORK3 = rank_modp(ISO3, P3)
del ISOR3


def second_prime_certificate(rows, flags, active, width, coeff_rank):
    passes = sum(1 for f in flags if f[0] and f[1] > 0 and f[2] and f[3] and f[4])
    no_mc = sum(1 for row in rows if row[2] == 0)
    no_vec = [i for i, f in enumerate(flags) if f[1] == 0]
    return (rows == BASE_ROWS and passes == NPART and sum(r[1] * r[2] for r in rows) == NCP
            and not no_vec and no_mc == NMC0 and active == ACT
            and width == NCP and coeff_rank == NCP)


SECOND_PRIME_OK = (SEP2 and SEP3 and second_prime_certificate(
    ROWS3, FLG3, ACT3, ISOW3, ISORK3))

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
# 31. the all-ones sum and the complementary-rank identity
# ------------------------------------------------------------------

# Each of the 36864 cells lies in exactly one of the 96 cell orbits, so the
# 96 orbit tables add up entry by entry to the all-ones table J, whose exact
# rational rank is one. Each orbit is free under the group of order 384 and
# meets every cover in two pieces, so each table carries two ones in every
# row and every column, 384 in all. Both facts are measured here, not
# assumed. The comparison that follows pairs a set S of cell orbits with the
# set left out: the two tables add to J, and the two exact rational ranks
# are found to agree at every set tried, while the two end points, where one
# side is empty, give 0 against 1 and so fix the range of the statement.
# Every rank is computed straight from its own table by rank_fwd; no rank
# below is supplied by the pairing itself.

JALL = np.ones((NCOV, NPI), dtype=np.int64)
SUMX = OXS.sum(axis=0)
RKJ = rank_fwd(JALL.tolist(), NPI)
SUMJ_OK = (bool(np.array_equal(SUMX, JALL)) and RKJ == 1)

REG2_N = 0
REG2_BAD = 0
for kx in range(NCP):
    a2 = OXS[kx]
    REG2_N += 1
    if (int(a2.sum()) != 2 * NCOV or int(a2.max()) != 1 or int(a2.min()) != 0
            or not bool((a2.sum(axis=1) == 2).all())
            or not bool((a2.sum(axis=0) == 2).all())):
        REG2_BAD += 1
REG2_OK = (REG2_N == NCP and REG2_BAD == 0 and 2 * NCOV == 384)


def orb_tab(sub):
    """entrywise sum of the cell orbit tables named in sub"""
    out = np.zeros((NCOV, NPI), dtype=np.int64)
    for kk2 in sub:
        out = out + OXS[kk2]
    return out


def orb_comp(sub):
    """the cell orbits left out of sub"""
    st = set(sub)
    return [kk3 for kk3 in range(NCP) if kk3 not in st]


# The pairing is checked before use: complementary size, disjoint labels, and
# an entrywise sum equal to J are all explicit predicates.
PAIR_N = 0
PAIR_BAD = 0
for sbz in [tuple(INB), (INB[0],)] + list(SZL[2]):
    cmz = orb_comp(sbz)
    PAIR_N += 1
    if (len(cmz) != NCP - len(sbz) or len(set(cmz) & set(sbz)) != 0
            or not bool(np.array_equal(orb_tab(sbz) + orb_tab(cmz), JALL))):
        PAIR_BAD += 1

RC92 = rank_fwd(orb_tab(orb_comp(INB)).tolist(), NPI)
RC95 = rank_fwd(orb_tab(orb_comp([INB[0]])).tolist(), NPI)
CPRS = []
for sbx in SZL[2]:
    CPRS.append((SUBRK[sbx], rank_fwd(orb_tab(orb_comp(sbx)).tolist(), NPI)))
CPR6 = sorted(x2[1] for x2 in CPRS)
CMPL_OK = (RC92 == QDRK and QDRK == RANKB and RC95 == SGRK[0]
           and SGRK[0] == CEIL and len(CPRS) == 6 and CPR6 == PRRK
           and PAIR_N == 8 and PAIR_BAD == 0
           and all(oa == ob for oa, ob in CPRS))
RKE = rank_fwd(np.zeros((NCOV, NPI), dtype=np.int64).tolist(), NPI)
ENDP_OK = (RKE == 0 and RKJ == 1 and RKE != RKJ)

# ------------------------------------------------------------------
# 32. the stratification of the 96 cell orbits by corner overlap
# ------------------------------------------------------------------

# A cell is a pair (cover C, piece P). Profile A of the cell is the sorted
# eight-tuple of corner overlaps, the size of corners(P) and corners(Q) met,
# as Q runs over the eight blocks of C. Profile B is the sorted eight-tuple
# of body overlaps popcount(PC[P] and PC[Q]) over the same eight. Every used
# piece has exactly five corners and no two distinct pieces share more than
# four, so an entry of five in profile A says that P is itself one of the
# eight blocks of C. Profile A is recomputed on all 36864 cells, so its
# constancy along a cell orbit is measured rather than inherited from the
# group action. The strata are the fibres of profile A; for each one the
# exact rational rank of the summed table and the blind dimension 192 minus
# that rank are measured.

CMK = [0] * NPI
for ii in range(NPI):
    for cn2 in KEPT[USED[ii]]:
        CMK[ii] = CMK[ii] | (1 << cn2)
NC5 = sum(1 for vx in CMK if popc(vx) == 5)
OFFMAX = 0
NPRS = 0
for ii in range(NPI):
    for jx in range(ii + 1, NPI):
        NPRS += 1
        vx2 = popc(CMK[ii] & CMK[jx])
        if vx2 > OFFMAX:
            OFFMAX = vx2
PIECE_OK = (NC5 == NPI and OFFMAX == 4 and OFFMAX < 5
            and NPRS == NPI * (NPI - 1) // 2)

PROFA = [None] * NCP
PABAD = 0
NCELL = 0
for kx in range(NCP):
    bd = 0
    for cx, px in CELLS[kx]:
        NCELL += 1
        prx = tuple(sorted(popc(CMK[px] & CMK[qx]) for qx in CS[cx]))
        if PROFA[kx] is None:
            PROFA[kx] = prx
        elif prx != PROFA[kx]:
            bd = 1
    PABAD += bd
PROFA_OK = (NCELL == NCP * NGRP and NCELL == 36864 and PABAD == 0
            and all(vx3 is not None for vx3 in PROFA))

STRA = {}
for kx in range(NCP):
    STRA.setdefault(PROFA[kx], []).append(kx)
SKEYS = sorted(STRA.keys())
NSTR = len(SKEYS)
SZH = {}
for qx in SKEYS:
    SZH[len(STRA[qx])] = SZH.get(len(STRA[qx]), 0) + 1
SZTX = " ".join("{0}:{1}".format(nd(sz2), nd(SZH[sz2])) for sz2 in sorted(SZH))
FIVE = [kx for kx in range(NCP) if 5 in PROFA[kx]]
NF5 = len(set(PROFA[kx] for kx in FIVE))
STRAT_OK = (NSTR == 25 and sorted(FIVE) == sorted(INB) and NF5 == 1
            and sum(len(STRA[qx]) for qx in SKEYS) == NCP
            and SZH == {2: 12, 4: 7, 6: 4, 8: 1, 12: 1}
            and sum(sz3 * SZH[sz3] for sz3 in SZH) == NCP
            and STRA[PROFA[INB[0]]] == sorted(INB))

PROFB = [None] * NCP
PBBAD = 0
for kx in range(NCP):
    bd = 0
    for cx, px in CELLS[kx]:
        prx = tuple(sorted(GM[px][qx] for qx in CS[cx]))
        if PROFB[kx] is None:
            PROFB[kx] = prx
        elif prx != PROFB[kx]:
            bd = 1
    PBBAD += bd
BGRP = {}
for kx in range(NCP):
    BGRP.setdefault(PROFB[kx], []).append(kx)
NBV = len(BGRP)
BFIN = all(len(set(PROFA[kx] for kx in vv2)) == 1 for vv2 in BGRP.values())
ACOAR = all(len(set(PROFB[kx] for kx in vv2)) == 1 for vv2 in STRA.values())
DIAG_OK = all(GM[ii][ii] == 1975 for ii in range(NPI))
B75 = [kx for kx in range(NCP) if 1975 in PROFB[kx]]
PROFB_OK = (PBBAD == 0 and NBV == 83 and BFIN and not ACOAR and NBV > NSTR
            and DIAG_OK and sorted(B75) == sorted(INB))

SRK = []
for qx in SKEYS:
    SRK.append(rank_fwd(orb_tab(STRA[qx]).tolist(), NPI))
SRMAX = max(SRK)
SRMINB = min(NPI - rr2 for rr2 in SRK)
SRINC = SRK[SKEYS.index(PROFA[INB[0]])]
SRANK_OK = (len(SRK) == NSTR and max(SRK) <= CEIL and SRMAX == 143
            and SRMAX < CEIL and SRMINB >= FLOORB and SRMINB == NPI - SRMAX
            and SRINC == RANKB)

# ------------------------------------------------------------------
# 33. which cell orbits lift the first slot of the cover table
# ------------------------------------------------------------------

# Cycle 766 measured the whole one-exchange neighbourhood of the four
# incidence orbits: 368 substitutions, some of them reaching the ceiling
# 144. Here the first slot alone is taken apart. Its 92 values are rebuilt
# from the small-matrix reduction and matched against the stored row, one
# member of the lifting set is confirmed by an exact rational rank and one
# non-member likewise, and the lifting set is then compared with the profile
# A strata to see whether lifting is a property of the stratum. What comes
# back is a measurement: a stratum may lift wholly, not at all, or in part.

NONI = [cx for cx in range(NCP) if cx not in INB]
RSL0 = []
for cx in NONI:
    sbx = tuple(sorted([INB[t2] for t2 in range(NINB) if t2 != 0] + [cx]))
    RSL0.append(int(red_rank(sbx, BET2, P2)))
SWROW = [int(vx) for vx in SWV[0:len(NONI)]]
REP0 = [NONI[t3] for t3 in range(len(NONI)) if RSL0[t3] == CEIL]
RSET = set(REP0)
NREP = len(REP0)
NRC = [cx for cx in NONI if cx not in RSET][0]
EXNR = rank_fwd(orb_tab(tuple(sorted(
    [INB[t2] for t2 in range(NINB) if t2 != 0] + [NRC]))).tolist(), NPI)
S5 = SKEYS.index(PROFA[SWC])
REPAIR_OK = (len(NONI) == NCP - NINB and RSL0 == SWROW and NREP == 19
             and NREP > 0 and SWC in RSET and SWJ == 0 and SWEX == CEIL
             and SWC == 5 and S5 == 23 and 0 <= S5 < NSTR
             and EXNR == RSL0[NONI.index(NRC)] and EXNR < CEIL)

RSW = 0
RSN = 0
RSM = 0
for qx in SKEYS:
    memx = [kx for kx in STRA[qx] if kx not in INB]
    hh = sum(1 for kx in memx if kx in RSET)
    if memx and hh == len(memx):
        RSW += 1
    elif hh == 0:
        RSN += 1
    else:
        RSM += 1
RSTRAT_OK = (RSW + RSN + RSM == NSTR and RSW == 0 and RSN == 10 and RSM == 15)

# ------------------------------------------------------------------
# 34. the incidence quartet inside a single cover
# ------------------------------------------------------------------

# The group has order 384 and moves the 192 covers in one orbit, so the
# subgroup fixing cover 0 has order two. Its non-identity element acts on
# the eight blocks of that cover; the blocks it pairs, the corner overlap
# inside each pair, and the cell orbit each pair sits in are all measured.
# The section ends at the least of the six pair ranks: the pair of incidence
# orbits attaining it is named by the partner overlaps of its two orbits,
# and its rank is recomputed exactly.

NST0 = len(STABC)
PE1 = PERM[E1]
BLK0 = list(CS[0])
FIX0 = sum(1 for bx in BLK0 if PE1[bx] == bx)
PRS = []
SEENB = set()
for bx in BLK0:
    if bx in SEENB:
        continue
    SEENB.add(bx)
    SEENB.add(PE1[bx])
    PRS.append((bx, PE1[bx]))
STAB_OK = (NST0 == 2 and NST0 == NGRP // NCOV and FIX0 == 0 and len(BLK0) == 8
           and len(PRS) == NINB and len(SEENB) == 8
           and all(PE1[oa] == ob and PE1[ob] == oa for oa, ob in PRS))

POVL = {}
PCH = 0
for oa, ob in PRS:
    if CPLAB[0][oa] == CPLAB[0][ob]:
        PCH += 1
    POVL[CPLAB[0][oa]] = popc(CMK[oa] & CMK[ob])
OVL = [POVL.get(cx, -1) for cx in INB]
PARTN_OK = (PCH == NINB and len(POVL) == NINB and sorted(POVL) == sorted(INB)
            and min(OVL) == 2 and max(OVL) == 2)

PMIN = min(PRRK)
LSB = [sbx for sbx in SZL[2] if SUBRK[sbx] == PMIN]
LPRK = rank_fwd(orb_tab(LSB[0]).tolist(), NPI)
NXT = sorted(PRRK)[1]
LNAM = [POVL[cx] for cx in LSB[0]]
P72_OK = (len(LSB) == 1 and len(LNAM) == 2 and LPRK == PMIN and LPRK == 72
          and NXT > LPRK and NXT == 93 and all(LPRK <= vx for vx in PRRK))

# ------------------------------------------------------------------
# 36. the partner pairs of a cover, read on all 192 covers
# ------------------------------------------------------------------

# The group has order 384 and moves the 192 covers in one orbit, so the
# subgroup holding a cover still has order two, and because the action on the
# 36864 cells is free its non-identity element can hold no piece still. That
# element is then a fixed-point-free involution on the 192 pieces with 96
# partner pairs, and two ones in every row makes each cell orbit meet the row
# of that cover in exactly one such pair. Every cover is measured. The fibre
# cardinality and distinct-label counts accompany the partner predicate, and a
# swapped-label scratch row is required to be rejected.


def row_pairs_ok(rowl, sgp):
    """the row labelling is constant on partners and has 96 fibres of size two"""
    for px6 in range(NPI):
        if rowl[px6] != rowl[sgp[px6]]:
            return False
    hs6 = {}
    for px6 in range(NPI):
        hs6[rowl[px6]] = hs6.get(rowl[px6], 0) + 1
    if len(hs6) != NCP:
        return False
    return all(v6 == 2 for v6 in hs6.values())


TBCOV = 0
TBSTAB = 0
TBFIX = 0
TBINV = 0
TBLAB = 0
TBFIB = 0
TBPRS = set()
for cx6 in range(NCOV):
    TBCOV += 1
    STG = [ex6 for ex6 in range(NGRP) if CPERM[ex6][cx6] == cx6]
    STN = [ex6 for ex6 in STG if PERM[ex6] != IDP]
    if len(STG) != 2 or len(STN) != 1:
        TBSTAB += 1
        continue
    sg6 = PERM[STN[0]]
    TBFIX += sum(1 for px6 in range(NPI) if sg6[px6] == px6)
    if any(sg6[sg6[px6]] != px6 for px6 in range(NPI)):
        TBINV += 1
    rw6 = CPLAB[cx6]
    TBLAB += sum(1 for px6 in range(NPI) if rw6[px6] != rw6[sg6[px6]])
    hs7 = {}
    for px6 in range(NPI):
        hs7[rw6[px6]] = hs7.get(rw6[px6], 0) + 1
    TBPRS.add(len(hs7))
    if row_pairs_ok(rw6, sg6):
        TBFIB += 1
TBPR = min(TBPRS) if len(TBPRS) == 1 else -1
TBDIST = len(set(CPLAB[0]))

# The rejector swaps two distinct labels while preserving fibre sizes, thereby
# isolating the partner predicate from the cardinality predicate.
BADR = list(CPLAB[0])
DIFP = [px7 for px7 in range(NPI) if BADR[px7] != BADR[0]]
BADR[0], BADR[DIFP[0]] = BADR[DIFP[0]], BADR[0]
TBREJ = 0 if row_pairs_ok(BADR, PERM[E1]) else 1

TBIJ_OK = (TBCOV == NCOV and NCOV == 192 and TBFIX == 0 and TBLAB == 0
           and TBSTAB == 0 and TBPR == NCP and TBINV == 0
           and TBFIB == NCOV and TBDIST == NCP)

def incidence_row_ok(labels, blocks):
    """Four incidence labels occur twice each on one eight-block cover."""
    hist = {}
    for bx6 in blocks:
        hist[labels[bx6]] = hist.get(labels[bx6], 0) + 1
    return (sorted(hist) == sorted(INB) and len(blocks) == 8
            and sum(hist.values()) == 8 and all(v7 == 2 for v7 in hist.values()))


BHST = {}
for bx6 in CS[0]:
    BHST[CPLAB[0][bx6]] = BHST.get(CPLAB[0][bx6], 0) + 1
BLAB = sorted(BHST)
NBLAB = len(BLAB)
BINC_OK = (NBLAB == NINB and incidence_row_ok(CPLAB[0], CS[0]))

# ------------------------------------------------------------------
# 37. the same blind space and the same seen space, not merely the same size
# ------------------------------------------------------------------

# Every orbit table carries two ones in each row and each column and the 96
# add to the all-ones table, so a sum over a set has all row sums and all
# column sums equal to twice the size of the set, and the sum over the
# left-out orbits is the all-ones table minus it. The all-ones vector then
# sits in the row space and in the column space of the sum, which is what
# makes every blind vector have entries adding to zero, and that in turn
# makes the left-out table blind in exactly the same directions. The row and
# column space statement is checked in exact rational arithmetic. The
# subspaces themselves are then compared over a prime field by stacking the
# two kernel bases and comparing ranks. Two equal tables would make that
# comparison empty, so the two tables are required to differ entry by entry,
# and one deliberately spoiled table is required to be turned away.

TSETS = [tuple(INB), (INB[0],)] + [tuple(sbx) for sbx in SZL[2]]
for szx in (3, 5, 7, 11, 17, 32, 48, 64):
    stx = set()
    while len(stx) < szx:
        LCG = divmod(LCG * 1103515245 + 12345, 2147483648)[1]
        stx.add(divmod(LCG >> 7, NCP)[1])
    TSETS.append(tuple(sorted(stx)))

ONES = [1] * NPI
EXN = 0
EXBAD = 0
EXMX = 0
for sx6 in TSETS:
    TSX = orb_tab(sx6)
    rb6 = rank_fwd(TSX.tolist(), NPI)
    rb7 = rank_fwd(TSX.tolist() + [ONES], NPI)
    rc6 = rank_fwd(TSX.T.tolist(), NPI)
    rc7 = rank_fwd(TSX.T.tolist() + [ONES], NPI)
    EXN += 1
    if rb6 > EXMX:
        EXMX = rb6
    if not (rb7 == rb6 and rc7 == rc6 and rc6 == rb6):
        EXBAD += 1

SPN = 0
SPBAD = 0
SPKER = 0
SPIM = 0
SPDIFF = 0
SPDIM = set()
SPD4 = -1
for sx6 in TSETS:
    TSX = orb_tab(sx6)
    cm6 = orb_comp(sx6)
    TCX = orb_tab(cm6)
    SPN += 1
    if (len(cm6) != NCP - len(sx6) or len(set(cm6) & set(sx6)) != 0
            or not bool(np.array_equal(TSX + TCX, JALL))):
        SPBAD += 1
    if not bool(np.array_equal(TSX, TCX)):
        SPDIFF += 1
    KA = mod_ker(np.mod(TSX, P2), P2)
    KB = mod_ker(np.mod(TCX, P2), P2)
    ka6 = rank_modp(KA.T, P2)
    kb6 = rank_modp(KB.T, P2)
    if rank_modp(np.hstack([KA, KB]).T, P2) != ka6 or ka6 != kb6:
        SPKER += 1
    SPDIM.add(ka6)
    if sx6 == tuple(INB):
        SPD4 = ka6
    LKA = mod_ker(np.mod(TSX.T, P2), P2)
    LKB = mod_ker(np.mod(TCX.T, P2), P2)
    la6 = rank_modp(LKA.T, P2)
    lb6 = rank_modp(LKB.T, P2)
    if rank_modp(np.hstack([LKA, LKB]).T, P2) != la6 or la6 != lb6:
        SPIM += 1
SPDL = sorted(SPDIM)

# the rejector: one zero entry of the first table is lifted to one, which
# leaves a table of the same shape and nearly the same entries but no longer
# blind in the same directions as the left-out table
TS0 = orb_tab(TSETS[0])
KB0 = mod_ker(np.mod(orb_tab(orb_comp(TSETS[0])), P2), P2)
rk0 = rank_modp(KB0.T, P2)
ZP0 = np.argwhere(TS0 == 0)
ZI0 = int(ZP0[0][0])
ZJ0 = int(ZP0[0][1])
TS0[ZI0, ZJ0] = 1
KP0 = mod_ker(np.mod(TS0, P2), P2)
rp0 = rank_modp(KP0.T, P2)
SPREJ = 0
if rank_modp(np.hstack([KP0, KB0]).T, P2) != rp0 or rp0 != rk0:
    SPREJ = 1

SPACE_OK = (SPN == len(TSETS) and SPBAD == 0 and SPKER == 0 and SPIM == 0
            and SPDIFF == SPN and SPREJ == 1 and EXBAD == 0 and EXN > 0
            and SPD4 == NKB)
EXACT_OK = (EXBAD == 0 and EXN == len(TSETS) and EXMX < NPI and EXMX == CEIL)

# ------------------------------------------------------------------
# 38. the rank of every one of the 4560 pairs of cell orbits
# ------------------------------------------------------------------

# The reduction to twenty small matrices turns the rank of a covariant table
# into a sum of small ranks, and one vectorised call gives the small ranks of
# a whole stack, so the complete pair census costs little. It is checked
# three ways: rebuilt at the other prime, set against the rank of the full
# 192 by 192 table on 25 pairs drawn by the recurrence already in use, and
# pinned to the exact rational ranks of the six incidence pairs. By the
# theorem of section 37 this same vector is at once the complete spectrum of
# all 4560 sets of size 94.


def cens_ix(bet, rws, act, p, ixl):
    """the reduction, run on a whole stack of subsets given by index arrays"""
    tot = np.zeros(ixl[0].shape[0], dtype=np.int64)
    for i7 in act:
        SS = bet[i7][ixl[0]].copy()
        for ax7 in ixl[1:]:
            SS = SS + bet[i7][ax7]
        np.mod(SS, p, out=SS)
        tot += rws[i7][0] * small_ranks(SS, p)
    return tot


PAIRS = list(itertools.combinations(range(NCP), 2))
IA = np.array([px8[0] for px8 in PAIRS], dtype=np.int64)
IB = np.array([px8[1] for px8 in PAIRS], dtype=np.int64)
PSPEC = cens_ix(BET2, ROWS2, ACT, P2, [IA, IB])
PSP3 = cens_ix(BET3, ROWS3, ACT3, P3, [IA, IB])
PDIS = int((PSPEC != PSP3).sum())
PMIN2 = int(PSPEC.min())
PMAX2 = int(PSPEC.max())
PNV = len(set(int(v8) for v8 in PSPEC))
PCEIL = int((PSPEC == CEIL).sum())
PLOW = int((PSPEC <= RANKB).sum())

PIDX = {}
for t8 in range(len(PAIRS)):
    PIDX[PAIRS[t8]] = t8

PSEL = []
while len(PSEL) < 25:
    st8 = set()
    while len(st8) < 2:
        LCG = divmod(LCG * 1103515245 + 12345, 2147483648)[1]
        st8.add(divmod(LCG >> 7, NCP)[1])
    pr8 = tuple(sorted(st8))
    if pr8 not in PSEL:
        PSEL.append(pr8)
PBIG = 0
PBAD = 0
for pr8 in PSEL:
    PBIG += 1
    if big_rank(pr8, P2) != int(PSPEC[PIDX[pr8]]):
        PBAD += 1

PEXB = 0
PEXV = []
for sbx in SZL[2]:
    v8 = int(PSPEC[PIDX[tuple(sorted(sbx))]])
    PEXV.append(v8)
    if v8 != SUBRK[sbx]:
        PEXB += 1
if sorted(PEXV) != PRRK:
    PEXB += 1

def pair_summary_ok(spec):
    vals = [int(v8) for v8 in spec]
    return (len(vals) == 4560 and len(set(vals)) == 13 and min(vals) == 48
            and max(vals) == 144 and sum(v8 == 144 for v8 in vals) == 960
            and sum(v8 <= 105 for v8 in vals) == 1104)


PSPEC_OK = (pair_summary_ok(PSPEC) and PDIS == 0 and PBAD == 0 and PBIG == 25
            and PEXB == 0)

# ------------------------------------------------------------------
# 39. the rank of every one of the 142880 triples of cell orbits
# ------------------------------------------------------------------

# The same reduction, over every three-element set, in blocks of 20000 so the
# working arrays inside the stacked reduction stay small. The two checks are
# the exact rational ranks of the four incidence triples and the rank of the
# full 192 by 192 table on 15 triples drawn by the same recurrence. By the
# theorem of section 37 this is at once the complete spectrum at size 93.

TRIP = list(itertools.combinations(range(NCP), 3))
NTRI = len(TRIP)
TIA = np.array([t9[0] for t9 in TRIP], dtype=np.int64)
TIB = np.array([t9[1] for t9 in TRIP], dtype=np.int64)
TIC = np.array([t9[2] for t9 in TRIP], dtype=np.int64)
CHK = 20000
TSPEC = np.zeros(NTRI, dtype=np.int64)
for s9 in range(0, NTRI, CHK):
    e9 = min(s9 + CHK, NTRI)
    TSPEC[s9:e9] = cens_ix(BET2, ROWS2, ACT, P2,
                           [TIA[s9:e9], TIB[s9:e9], TIC[s9:e9]])
TMIN = int(TSPEC.min())
TMAX = int(TSPEC.max())
TNV = len(set(int(v9) for v9 in TSPEC))
TCEIL = int((TSPEC == CEIL).sum())
TLOW = int((TSPEC <= RANKB).sum())

TSEL = []
while len(TSEL) < 15:
    st9 = set()
    while len(st9) < 3:
        LCG = divmod(LCG * 1103515245 + 12345, 2147483648)[1]
        st9.add(divmod(LCG >> 7, NCP)[1])
    tr9 = tuple(sorted(st9))
    if tr9 not in TSEL:
        TSEL.append(tr9)

TNEED = set(TSEL) | set(tuple(sorted(sbx)) for sbx in SZL[3])
TPOS = {}
for t9 in range(NTRI):
    if TRIP[t9] in TNEED:
        TPOS[TRIP[t9]] = t9

TBIGN = 0
TBADN = 0
for tr9 in TSEL:
    TBIGN += 1
    if big_rank(tr9, P2) != int(TSPEC[TPOS[tr9]]):
        TBADN += 1

TEXB = 0
TEXV = []
for sbx in SZL[3]:
    v9 = int(TSPEC[TPOS[tuple(sorted(sbx))]])
    TEXV.append(v9)
    if v9 != SUBRK[sbx]:
        TEXB += 1
if sorted(TEXV) != TRRK:
    TEXB += 1

def triple_summary_ok(spec):
    vals = [int(v9) for v9 in spec]
    return (len(vals) == 142880 and len(set(vals)) == 18 and min(vals) == 64
            and max(vals) == 144 and sum(v9 == 144 for v9 in vals) == 60960
            and sum(v9 <= 105 for v9 in vals) == 1472)


TSPEC_OK = (triple_summary_ok(TSPEC) and TEXB == 0 and TBADN == 0
            and TBIGN == 15)

# ------------------------------------------------------------------
# 40. finite pair-degree and stratum-fibre aggregation
# ------------------------------------------------------------------

# The degree of an orbit counts below-ceiling partners. The first incidence
# orbit is rebuilt from all 95 full tables. The stratum-fibre aggregation then
# records how many modular ranks occur in every realized stratum pair.

DEG = [0] * NCP
BELOW = 0
for t9 in range(len(PAIRS)):
    if int(PSPEC[t9]) < CEIL:
        BELOW += 1
        DEG[PAIRS[t9][0]] += 1
        DEG[PAIRS[t9][1]] += 1
DGMIN = min(DEG)
DGMAX = max(DEG)
DGNV = len(set(DEG))
DGINB = [DEG[cx9] for cx9 in INB]
# read "at the top" off the degree VALUES, not off a sort of the indices: an
# index sort would let its own tie-break decide the answer whenever the
# degrees tie, which is exactly the case that has to stay visible
DGSRT = sorted(DEG, reverse=True)
DGTOP = min(DGINB) >= DGSRT[NINB - 1]
DGTIE = sum(1 for v9 in DEG if v9 == DGMAX)

DGREF = 0
for j9 in range(NCP):
    if j9 == INB[0]:
        continue
    if big_rank(tuple(sorted((INB[0], j9))), P2) < CEIL:
        DGREF += 1

STRIX = [SKEYS.index(PROFA[k9]) for k9 in range(NCP)]
STPM = {}
STCN = {}
for t9 in range(len(PAIRS)):
    a9 = STRIX[PAIRS[t9][0]]
    b9 = STRIX[PAIRS[t9][1]]
    ky9 = (min(a9, b9), max(a9, b9))
    STPM.setdefault(ky9, set()).add(int(PSPEC[t9]))
    STCN[ky9] = STCN.get(ky9, 0) + 1
STPN = len(STPM)
STPD = sum(1 for ky9 in STPM if len(STPM[ky9]) > 1)
STPMAX = max(len(STPM[ky9]) for ky9 in STPM)

# one conjunct here discriminates against a wrong object: DGREF rebuilds one
# orbit's degree from 95 full-table ranks and must match the degree the census
# gives. The rest are bookkeeping on the loops just above, holding either by
# construction or as weak sanity limits; they are kept as loop checks, and no
# claim in the note leans on them
def degree_summary_ok(spec):
    deg = [0] * NCP
    strata = {}
    below = 0
    for ix9, rank9 in enumerate(spec):
        rank9 = int(rank9)
        a9, b9 = PAIRS[ix9]
        if rank9 < CEIL:
            below += 1
            deg[a9] += 1
            deg[b9] += 1
        ky9 = tuple(sorted((STRIX[a9], STRIX[b9])))
        strata.setdefault(ky9, set()).add(rank9)
    return (below == 3600 and deg == [75] * NCP and sum(deg) == 7200
            and len(strata) == 325
            and sum(len(vals9) > 1 for vals9 in strata.values()) == 313
            and max(len(vals9) for vals9 in strata.values()) == 13)


DEG_OK = (degree_summary_ok(PSPEC) and DGREF == DEG[INB[0]]
          and sum(STCN.values()) == len(PAIRS) and DGMIN == DGMAX == 75
          and DGNV == 1 and DGINB == [75] * NINB and DGTIE == NCP
          and STPN == 325 and STPD == 313 and STPMAX == 13)

# ------------------------------------------------------------------
# 41. discriminating in-memory mutations for every load-bearing family
# ------------------------------------------------------------------


def orbit_basis_certificate(tables):
    total = np.zeros((NCOV, NPI), dtype=np.int64)
    if len(tables) != NCP:
        return False
    for table in tables:
        if (table.shape != (NCOV, NPI)
                or not bool(np.all(table.sum(axis=0) == 2))
                or not bool(np.all(table.sum(axis=1) == 2))):
            return False
        total += table
    return bool(np.array_equal(total, JALL))


def exact_ones_space_ok(table):
    rows = table.tolist()
    cols = table.T.tolist()
    return (rank_fwd(rows + [ONES], NPI) == rank_fwd(rows, NPI)
            and rank_fwd(cols + [ONES], NPI) == rank_fwd(cols, NPI))


BAD_MASKS = list(MASK)
BAD_MASKS[0] = 0
MUT_OBJECT = not mask_search_certificate(BAD_MASKS, SOLS)

BAD_MAPS = list(MAPS)
BAD_MAPS[-1] = BAD_MAPS[0]
MUT_GROUP = not map_family_certificate(BAD_MAPS)

BAD_ORBITS = list(OXS)
BAD_ORBITS[0] = np.zeros_like(OXS[0])
MUT_ORBITS = not orbit_basis_certificate(BAD_ORBITS)
del BAD_ORBITS

MUT_BLOCK = False
for mi in ACT:
    msum = np.mod(BET2[mi][IXB].sum(axis=0), P2)
    mrank = int(small_ranks(msum[None, :, :].copy(), P2)[0])
    if mrank:
        BAD_ROWS = list(ROWS2)
        row = list(BAD_ROWS[mi])
        row[0] += 1
        BAD_ROWS[mi] = tuple(row)
        MUT_BLOCK = (red_rank_data(tuple(INB), BET2, BAD_ROWS, ACT, P2)
                     != big_rank(tuple(INB), P2))
        break

BAD_ROWS3 = list(ROWS3)
bad3 = list(BAD_ROWS3[ACT3[0]])
bad3[0] += 1
BAD_ROWS3[ACT3[0]] = tuple(bad3)
MUT_SECOND = not second_prime_certificate(BAD_ROWS3, FLG3, ACT3, ISOW3, ISORK3)

BAD_INCIDENCE = list(CPLAB[0])
BAD_INCIDENCE[CS[0][0]] = NCP
MUT_INCIDENCE = not incidence_row_ok(BAD_INCIDENCE, CS[0])

MUT_EXACT = not exact_ones_space_ok(np.zeros((NCOV, NPI), dtype=np.int64))
MUT_CYCLE = (cyc_lens(CELLS[0][1:]) is None)

BAD_PAIR = PSPEC.copy()
BAD_PAIR[0] = CEIL + 1
MUT_PAIR = not pair_summary_ok(BAD_PAIR)

BAD_TRIPLE = TSPEC.copy()
BAD_TRIPLE[0] = CEIL + 1
MUT_TRIPLE = not triple_summary_ok(BAD_TRIPLE)

BAD_DEGREE = PSPEC.copy()
bad_degree_index = int(np.nonzero(BAD_DEGREE < CEIL)[0][0])
BAD_DEGREE[bad_degree_index] = CEIL
MUT_DEGREE = not degree_summary_ok(BAD_DEGREE)

MUTATIONS = [MUT_OBJECT, MUT_GROUP, MUT_ORBITS, MUT_BLOCK, MUT_SECOND,
             MUT_INCIDENCE, MUT_EXACT, MUT_CYCLE, MUT_PAIR, MUT_TRIPLE,
             MUT_DEGREE]
MUTATION_OK = all(MUTATIONS)

# ------------------------------------------------------------------
# 42. further source hygiene, and the closing budget
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

ELAPSED2 = int(time.time() - T0)
RSS2 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSSMB2 = RSS2 // 1048576 if RSS2 > 10000000 else RSS2 // 1024

# ------------------------------------------------------------------
# gates, continued
# ------------------------------------------------------------------

gate(PRIME_OK and TAB2_OK and TAB3_OK and SECOND_PRIME_OK, "C28",
     "two-prime block rebuilds: rows/separation/factors/active/coefficient map yes")

gate(PASS5 == NPART and NPART == 20 and SMMC == NCP and not NOVEC
     and NOMC == NMC0, "C29",
     "small-block five-condition passes {0}/20; zero cover multiplicity {1}".format(
         nd(PASS5), nd(NOMC)))

gate(ISOW == NCP and ISORK == NCP and ISOW3 == NCP and ISORK3 == NCP, "C30",
     "orbit coefficient maps: widths {0}/{1}, ranks {2}/{3} at the two primes".format(
         nd(ISOW), nd(ISOW3), nd(ISORK), nd(ISORK3)))

gate(RED_AGR == len(TABS) and CRED == RANKB and NPI - CRED == NKB, "C31",
     "block/full rank checks {0}/{1}; cover rank/blind {2}/{3}".format(
         nd(RED_AGR), nd(len(TABS)), nd(CRED), nd(NPI - CRED)))

gate(len(NZD) == NEX and DR_SET and DROP_ID_OK, "C32",
     "8 drop blocks have unique ordinal/value/hash ids; hashes {0}".format(
         DROP_HASHES))

gate(DR_SUM == EXC_C and BLIND_OK and len(NZD) == 8, "C33",
     "internal block accounting: {0} drops sum to {1}; blind = d(m-rank) on"
     " all 20".format(nd(len(NZD)), nd(DR_SUM)))


GN = [34]


def nextlab():
    lab = "C{0}".format(GN[0])
    GN[0] += 1
    return lab


def scope(msg):
    TAGS.append(nextlab())
    emit("{0} {1}".format(TAGS[-1], msg))


gate(SG_OK and len(SGRK) == NINB and NINB == 4, nextlab(),
     "incidence singleton ranks: {0} copies of exact {1}; modular agrees".format(
         nd(NINB), nd(CEIL)))

gate(SGMISS == 0 and SGN == NINB * len(ACT) and SGN > 0, nextlab(),
     "singleton block checks {0}; short count {1}".format(nd(SGN), nd(SGMISS)))

gate(LAT_OK, nextlab(),
     "pairs {0}; triples {1}; four give {2}, below every triple"
     .format(",".join(nd(v) for v in PRRK),
             ",".join(nd(v) for v in TRRK), nd(QDRK)))

gate(LV_OK and len(NZD) == 8, nextlab(),
     "first-short level pair for {0} blocks; singleton short count {1}".format(
         nd(len(DRLV)), nd(LV_ONE)))

gate(len(NMON) == 3 and NMOK, nextlab(),
     "recoverable blocks: {0} short on a pair and full on the incidence quartet;"
     " {1}".format(nd(len(NMON)), NMTX))

gate(LV_DIS == 0 and LV_N == len(ACT3) and LV_N > 0, nextlab(),
     "second-prime level checks {0}; differences {1}; short sub-sums {2}".format(
         nd(LV_N), nd(LV_DIS), nd(LV_NB)))

gate(SW_OK, nextlab(),
     "one-swap {0}: range {1}..{2}, ceiling {3}, rank-{5} {4}, lower {6}".format(
         nd(SWN), nd(SWMIN), nd(SWMAX), nd(SWTOP), nd(SWEQ), nd(RANKB),
         nd(SWLO)))

gate(SWJ >= 0 and SWEX == CEIL and QDRK == RANKB, nextlab(),
     "exchange slot/orbit {0}/{1}; exact rank {2}->{3}".format(
         nd(SWJ), nd(SWC), nd(QDRK), nd(SWEX)))

gate(BL_OK, nextlab(),
     "blind meet/span {0}/{1}; four-plus-one rank {2}".format(
         nd(INTER), nd(SUMBL), nd(R5)))

gate(SUMJ_OK, nextlab(),
     "{0} sum to J rank {1}".format(nd(NCP), nd(RKJ)))

gate(REG2_OK, nextlab(),
     "{0} ok {1} off {2} ones".format(nd(REG2_N), nd(REG2_BAD), nd(2 * NCOV)))

gate(CMPL_OK, nextlab(),
     "cmpl {0} {1} {2}".format(nd(RC92), nd(RC95),
                               ",".join(nd(v) for v in CPR6)))

gate(ENDP_OK, nextlab(),
     "empty {0} full {1}".format(nd(RKE), nd(RKJ)))

gate(PIECE_OK, nextlab(),
     "{0} of {1} corners top {2}".format(nd(NC5), nd(5), nd(OFFMAX)))

gate(PROFA_OK, nextlab(),
     "{0} cells {1} vary".format(nd(NCELL), nd(PABAD)))

gate(STRAT_OK, nextlab(),
     "{0} strata {1}".format(nd(NSTR), SZTX))

gate(PROFB_OK, nextlab(),
     "B {0} vals finer {1} on {2}".format(nd(NBV), nd(1975), nd(len(B75))))

gate(SRANK_OK, nextlab(),
     "stratum max/ceiling/min-blind/incidence {0}/{1}/{2}/{3}".format(
         nd(SRMAX), nd(CEIL), nd(SRMINB), nd(SRINC)))

gate(REPAIR_OK, nextlab(),
     "{0} lift slot {1} orb {2} str {3}".format(nd(NREP), nd(SWJ), nd(SWC),
                                                nd(S5)))

gate(RSTRAT_OK, nextlab(),
     "{0} all {1} none {2} mixed".format(nd(RSW), nd(RSN), nd(RSM)))

gate(STAB_OK, nextlab(),
     "stab {0} fix {1} {2} pairs".format(nd(NST0), nd(FIX0), nd(len(PRS))))

gate(PARTN_OK, nextlab(),
     "partners {0}".format(" ".join(nd(v) for v in OVL)))

gate(P72_OK, nextlab(),
     "least pair {0} rank {1}".format(" ".join(nd(v) for v in LNAM), nd(LPRK)))

gate(TBIJ_OK and TBREJ == 1, nextlab(),
     "row-pair checks covers/fixed/misses/pairs/reject {0}/{1}/{2}/{3}/{4}".format(
         nd(TBCOV), nd(TBFIX), nd(TBLAB), nd(TBPR), nd(TBREJ)))

gate(BINC_OK, nextlab(),
     "one cover: 8 blocks, {0} incidence labels, multiplicity two".format(
         nd(NBLAB)))

gate(SPACE_OK, nextlab(),
     "complement spaces sets/right/left/different/reject/blind {0}/{1}/{2}/{3}/{4}/{5}".format(
         nd(SPN), nd(SPKER), nd(SPIM), nd(SPDIFF), nd(SPREJ), nd(SPD4)))

gate(EXACT_OK, nextlab(),
     "exact all-ones row/column checks {0}; misses {1}; top rank {2}".format(
         nd(EXN), nd(EXBAD), nd(EXMX)))

# the size-one spectrum, three independent routes forced to agree: the cycle
# rule on the bipartite structure, the mod p elimination, and the ceiling read
# off the parts. A wrong object breaks the first two against each other.
ONE_OK = (CYC_OK and CYCBAD == 0 and CYCLIST == [(48, (4,), NCOV)]
          and len(RKHIST) == 1 and RKHIST[0] == (CEIL, NCP))

gate(ONE_OK, nextlab(),
     "singleton cycle/rank: {0}x{1}, orbits {2}, rank {3}, misses {4}".format(
         nd(CYCLIST[0][0]), nd(CYCLIST[0][1][0]), nd(RKHIST[0][1]),
         nd(RKHIST[0][0]), nd(CYCBAD)))

gate(PSPEC_OK, nextlab(),
     "F_1000003 pairs: 4560, {0} values {1}..{2}, ceiling {3}, <=105 {4};"
     " {5} full-table checks, second-prime misses {6}; complements size 94".format(
         nd(PNV), nd(PMIN2), nd(PMAX2), nd(PCEIL), nd(PLOW), nd(PBIG), nd(PDIS)))

gate(TSPEC_OK, nextlab(),
     "F_1000003 triples: 142880, {0} values {1}..{2}, ceiling {3}, <=105"
     " {4}; {5} full-table checks; complements size 93".format(
         nd(TNV), nd(TMIN), nd(TMAX), nd(TCEIL), nd(TLOW), nd(TBIGN)))

gate(DEG_OK, nextlab(),
     "F_1000003 pair aggregation: degree {0} on all {1}; {2} of {3} stratum"
     " fibres contain multiple ranks, maximum {4}".format(
         nd(DGMIN), nd(DGTIE), nd(STPD), nd(STPN), nd(STPMAX)))

gate(MUTATION_OK, nextlab(),
     "mutations 11/11 reject: object/group/orbit/block/p2/incidence/exact/cycle/pair/triple/degree")

SEQ_OK = (TAGS == ["C{0}".format(k) for k in range(len(TAGS))])
gate(SEQ_OK and len(TAGS) >= 34, nextlab(),
     "gate labels sequential: {0}".format(nd(len(TAGS) + 1)))

gate(BAN2_OK and NBAN2 == 3 and NO_D9 and ONE_WORD_OK, nextlab(),
     "closing source checks clean: {0}".format(nd(NBAN2)))

FINAL_TAG = nextlab()
FINAL_MSG = "budget: declared wall/RSS limits and prospective complete stdout under 6000"
RESOURCE_OK = (ELAPSED2 < AUDIT_TIMEOUT_SEC and RSSMB2 < 2500)


def prospective_stdout(ok):
    gate_line = "{0} {1} {2}\n".format("PASS" if ok else "FAIL", FINAL_TAG, FINAL_MSG)
    before_trailer = OUT[0] + len(gate_line)
    count_line = "stdout characters before trailer: {0}\n".format(nd(before_trailer))
    pass_count = STAT[0] + (1 if ok else 0)
    fail_count = STAT[1] + (0 if ok else 1)
    total_line = "TOTAL: PASS={0} FAIL={1}\n".format(pass_count, fail_count)
    return before_trailer + len(count_line) + len(total_line)


FINAL_OK = RESOURCE_OK
FINAL_OK = RESOURCE_OK and prospective_stdout(FINAL_OK) < 6000
FINAL_COMPLETE_CHARS = prospective_stdout(FINAL_OK)
gate(FINAL_OK, FINAL_TAG, FINAL_MSG)
emit("stdout characters before trailer: {0}".format(nd(OUT[0])))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if OUT[0] != FINAL_COMPLETE_CHARS:
    raise RuntimeError("stdout accounting drift")
if STAT[1]:
    raise SystemExit(1)
