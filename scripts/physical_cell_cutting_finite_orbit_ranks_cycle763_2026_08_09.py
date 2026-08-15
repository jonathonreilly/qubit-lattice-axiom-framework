"""Rebuild and gate finite orbit-table rank identities on a unit four-cube.

The runner constructs the sixteen corners, the unit-determinant five-corner
pieces at the adjacency-cost floor, every certified cutting by those pieces,
the supported pieces, and the eight-piece covers that meet every cutting once.
It then constructs the 384 coordinate relabelings and their actions on pieces,
covers, ordered pairs, and cover-piece cells.

The certified target is finite and positive: the cover table is a union of four
cover-piece orbit indicators with exact integer rank 105, while an explicit
four-orbit union of the same binary row-and-column shape has exact integer rank
144. Stabilizer splits, orbital-basis preservation counts, and modular ranks are
reported as separately labelled finite diagnostics.

Output is one line per gate, followed by the stdout character count and total.
"""

import itertools
import math
import sys
import time
import resource
from fractions import Fraction as FR
import numpy as np
PRIME = 1000003
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


def gate(ok, tag, msg):
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
# 10. canonical orbital-basis preservation counts
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
# 13. determinant-one coordinate subgroups
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
SAME_OK = ((not SAME_ACTION) and NORB != NPOC)

# ------------------------------------------------------------------
# 16. cover-piece orbit tables
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
# 17. the cover table and a same-shape orbit-union witness
# ------------------------------------------------------------------

SZH = {}
for j in range(NCP):
    sz = len(CELLS[j])
    SZH[sz] = SZH.get(sz, 0) + 1
SZLIST = sorted(SZH.items())
SZ_SUM = sum(a * b for a, b in SZLIST)
SZ_CNT = sum(b for a, b in SZLIST)
SZ_OK = (SZ_SUM == NCOV * NPI and SZ_CNT == NCP and min(SZH) > 0
         and len(SZH) == 1)

# how many ones one orbit puts in a cover row, and how many orbits a row needs
CONTRIB, RCON = divmod(SZLIST[0][0], NCOV)
BROWS = sorted(set(sum(r) for r in BROW))
NEEDED, RNEED = divmod(BROWS[0], CONTRIB) if CONTRIB > 0 else (0, 1)
MSET = sorted(set(CPLAB[i][k] for i in range(NCOV)
                  for k in range(NPI) if BROW[i][k]))
NMET = len(MSET)
COUNT_OK = (len(SZH) == 1 and RCON == 0 and RNEED == 0 and len(BROWS) == 1
            and NMET == NEEDED)

MS = set(MSET)
REB_OK = True
for i in range(NCOV):
    Li = CPLAB[i]
    row = BROW[i]
    for k in range(NPI):
        if (1 if Li[k] in MS else 0) != row[k]:
            REB_OK = False

BORD_RK = sorted(set(CPRK[j] for j in MSET))
BORD_OK = (len(BORD_RK) == 1 and BORD_RK[0] == WIT)

ACC = np.zeros((NCOV, NPI), dtype=np.int64)
RUN = []
for j in MSET:
    ACC = ACC + (CPL == j).astype(np.int64)
    RUN.append(rank_modp(ACC, PRIME))
RUN_OK = (len(RUN) == NEEDED and RUN[-1] == RANKB)

WITSEL = (6, 11, 28, 39)
WITMAT = np.isin(CPL, WITSEL).astype(np.int64)
WIT_ROWS = sorted(set(int(x) for x in WITMAT.sum(axis=1)))
WIT_COLS = sorted(set(int(x) for x in WITMAT.sum(axis=0)))
WIT_LABELS_OK = (len(set(WITSEL)) == NEEDED
                 and all(0 <= j < NCP for j in WITSEL))
WIT_SHAPE = (WIT_ROWS == BROWS and WIT_COLS == BCS)


def rank_exact(rows):
    M = [list(map(int, r)) for r in rows]
    m, n = len(M), len(M[0])
    prev, r = 1, 0
    for c in range(n):
        if r >= m:
            break
        piv = -1
        for i in range(r, m):
            if M[i][c]:
                piv = i
                break
        if piv < 0:
            continue
        if piv != r:
            M[r], M[piv] = M[piv], M[r]
        prc = M[r][c]
        for i in range(r + 1, m):
            mic = M[i][c]
            Mi, Mr = M[i], M[r]
            if mic:
                for j in range(c + 1, n):
                    Mi[j] = (prc * Mi[j] - mic * Mr[j]) // prev
                Mi[c] = 0
            else:
                for j in range(c + 1, n):
                    Mi[j] = (prc * Mi[j]) // prev
        prev = prc
        r += 1
    return r


IDT = [[1 if i == k else 0 for k in range(NCOV)] for i in range(NCOV)]
RX_ID = rank_exact(IDT)
ID_OK = (RX_ID == NCOV)
RX_B = rank_exact(BROW)
RX_DUP = rank_exact(BROW + BROW)
DUP_OK = (RX_DUP == RX_B)
EXACT_OK = (RX_B == RANKB_P)
RX_WIT = rank_exact(WITMAT)
WITNESS_OK = (WIT_LABELS_OK and WIT_SHAPE and RX_WIT == 144
              and RX_B == 105 and RX_WIT != RX_B)

# ------------------------------------------------------------------
# 18. source hygiene and budget
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

emit("finite-object claims use integer or rational arithmetic; the final resource gate uses measured bounds")

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and GENERIC and NPTS == 625
     and DIV == 80 and NS == 15800 and SIZES == [24] and NPI == 192
     and sorted(set(PCN)) == [1975] and NCOV == 192 and BRS == [8] and BCS == [8],
     "G0",
     "{0} pieces of determinant one, {1} at floor {2}, {3} cuttings of {4} over {5} points, {6} used, {7} covers".format(
         NCAND, NKEPT, FLOOR, NS, SIZES[0], NPTS, NPI, NCOV))

gate(DISJ_OK and NPAIR == NFAC + NDIM and COVEXACT and ACS == [1975],
     "G1",
     "each cutting tiles: {0} pieces of volume 1 over 24, its {1} co-occurring pairs interior-disjoint, {2} by facet".format(
         SIZES[0], NPAIR, NFAC))

gate(OMAX > 1 and OMIN > 0 and OMIN < OMAX and SLOTS == 120 and NCORN == 16 and SLOTS > NCORN,
     "G2",
     "corner sharing: {0} corner slots on {1} corners, one corner taking from {2} to {3}".format(
         SLOTS, NCORN, OMIN, OMAX))

gate(GRAM_OK and KANN_A and KANN_B and PCN[0] == 1975,
     "G3",
     "two builds of the {0} square agree, both kernels give total zero on every cutting and cover".format(
         NPI))

gate(MAPS_DISTINCT and CLOSED and NPROD == NGRP * NGRP and KEEPS_PIECES
     and PERM_DISTINCT and BIJ and NGRP == 384,
     "G4",
     "permuting the four coordinates and flipping any of them gives {0} distinct maps, closed over {1} products".format(
         NGRP, NPROD))

gate(STAB_A == NGRP and STAB_B == NGRP,
     "G5",
     "stability: all {0} elements carry the sorted cutting and cover tables to themselves, both row spaces stand".format(
         NGRP))

gate(SUMCHI == NGRP and SUMSQ_OK and HIST_P[0][0] == 0,
     "G6",
     "fixed-piece counts {0} sum to {1}, one orbit on pieces, squares sum to {1} times {2}".format(
         HIST_P, NGRP, NORB))

gate(NORB == 104 and SUMSQ_OK,
     "G7",
     "union-find over the {0} ordered piece pairs under all {1} elements gives {2} orbits, matching the squares".format(
         NPI * NPI, NGRP, NORB))

gate(RANKA == 88 and NKA == 104 and RANKB == 105 and NKB == 87
     and RANKA + NKA == NPI and RANKB + NKB == NPI and RKKA == NKA and RKKB == NKB,
     "G8",
     "cutting rank {0} kernel {1}, cover rank {2} kernel {3}, each kernel certified by total zero and its own rank".format(
         RANKA, NKA, RANKB, NKB))

gate(RSELA == RANKA and RSELB == RANKB and len(SELA) == RANKA
     and len(SELB) == RANKB and perp_all(RAROW, KA) and perp_all(RBROW, KB),
     "G9",
     "independent selections of {0} cutting and {1} cover rows reach those ranks and are zeroed by each kernel".format(
         RANKA, RANKB))

gate(DSUM == NPI and DMEET == 1 and ONE_A and ONE_B,
     "G10",
     "the two row spaces span all {0} dimensions and meet in dimension {1}, the constants, killed by both kernels".format(
         DSUM, DMEET))

gate(PARTITION and min(CLS) > 0 and len(CLS) == NORB,
     "G11",
     "the {0} labels cut all {1} entries into classes of sizes {2} to {3}, so their matrices span the commuters".format(
         NORB, NPI * NPI, min(CLS), max(CLS)))

gate(NKEEP_A == 2,
     "G12",
     "exactly {0} of {1} canonical orbital basis matrices individually preserve the cutting row space".format(
         NKEEP_A, NORB))

gate(NKEEP_B == 2,
     "G13",
     "exactly {0} of {1} canonical orbital basis matrices individually preserve the cover row space".format(
         NKEEP_B, NORB))

gate(CTRL_A,
     "G14",
     "control: the constants times each of the {0} orbital basis matrices stays a multiple of the constants".format(
         NORB))

gate((not SHIFT_IN) and (not SHIFT_KEEPS),
     "G15",
     "control: the cyclic shift on {0} pieces lies outside the {1}-element action and changes the cutting table".format(
         NPI, NGRP))

gate(RANKU == NPI and RANKMU == RANKA and NOUT == len(MU),
     "G16",
     "the first basis matrix outside the preserving set has degree {0}; with identity rank {1}, moved-row rank {2}".format(
         DEG_KSTAR, RANKU, RANKMU))

gate(GEN_OK and MU_STABLE and len(GENS) == 2,
     "G17",
     "two named elements generate all {0}, and the moved span keeps rank {1} stacked with its image under each".format(
         NGRP, RANKMU))

gate(LAB_INV,
     "G18",
     "labels survive every element on all {0} entries; true by construction of the orbits, so non-discriminating".format(
         NPI * NPI))

gate(DEG_CONST and DEGSUM == NPI and DEGCNT == NORB,
     "G19",
     "out-degree census {0} from every source piece; degrees by count sum to {1}, counts to {2}".format(
         CENSUS, DEGSUM, DEGCNT))

gate(NSTABP == 2 and STAB_SIMPLE and STAB_ORB,
     "G20",
     "the stabilizer of a piece has order {0}, orbit sizes {1}: {2} plus twice {3} is {4}, {2} plus {3} is {5}".format(
         NSTABP, SZP_LIST, FP, SP2, NPI, NORB))

gate(EIG_SUM and NTWO == 12 and ONE_PLUS,
     "G21",
     "its non-identity element has plus and minus dimensions {0} and {1} by two independent exact ranks, sum {2}".format(
         DPLUS, DMINUS, NPI))

emit("separately computed agreements: plus dimension {0} equals cutting kernel {1}; minus dimension {2} equals rank {3}".format(
    DPLUS, NKA, DMINUS, RANKA))

gate(SPLIT_A and SPLIT_B,
     "G22",
     "that element splits the cutting row space {0} plus {1} and the cover row space {2} plus {3}, ranks {4} and {5}".format(
         APL, AMI, BPL, BMI, RANKA, RANKB))

gate(THMA_PLUS and THMA_MINUS,
     "G23",
     "theorem A: {0} plus {1} is {2}, the plus dimension {3} plus the constants; {4} plus {5} is {6}, the minus".format(
         APL, BPL, APL + BPL, DPLUS, AMI, BMI, AMI + BMI))

gate(ALLSIX and NTWO == 12,
     "G24",
     "all {0} order-two elements fixing a piece give the same six dimensions {1}, each by its own rank".format(
         NTWO, list(SIX)))

gate(DEMOTE_OK,
     "G25",
     "space comparison: cutting-minus intersection dimension {0}, cutting rank {1}, augmented-minus span dimension {2}".format(
         AMI, RANKA, DSPAN))

gate(COV_OK and COV_BIJ and COV_TRANS,
     "G26",
     "all {0} elements carry covers to covers, and the action on the {1} covers is transitive".format(
         NGRP, NCOV))

gate(CSUM == NGRP and CSUMSQ_OK,
     "G27",
     "fixed-cover counts {0} sum to {1}, squares to {1} times {2}; pair orbits cover {2}, piece {3}".format(
         HIST_C, NGRP, NPOC, NORB))

gate(NSTABC == 2 and CSTAB_SIMPLE and CSTAB_ORB,
     "G28",
     "cover stabilizer order {0}, sizes {1}: {2} plus twice {3} is {4}, {2} plus {3} is {5}; it fixes {6} pieces".format(
         NSTABC, SZC_LIST, FC, SC2, NCOV, NPOC, CSTAB_FIXP))

gate(SAME_OK,
     "G29",
     "piece and cover fixed-point lists differ: {0}; their ordered-pair orbit counts are {1} and {2}".format(
         yn(not SAME_ACTION), NORB, NPOC))

emit("pair-orbit and kernel counts: piece {0} and {1}; cover {2} and {3}; equality occurs on one side".format(
    NORB, NKA, NPOC, NKB))

gate(SUB_OK and SUB_BIGGER and SUB_SIZE == [24, 24, 24, 24],
     "G30",
     "four determinant-one coordinate subgroups of order {0}: piece orbits {2}, pair orbits {3}, full-action count {4}".format(
         SUB_SIZE[0], NGRP, sorted(set(SUB_PIECE)), sorted(set(SUB_PAIR)), NORB))

gate(NORB == NKA,
     "G31",
     "pair-orbit count and cutting kernel are both {0}, computed by separate routes".format(
         NORB))

gate(CP_FULL and PP_FULL and PP_AGREE and BEQUI,
     "G32",
     "cover-piece orbits {0} label all {1} cells, the cover table constant on them: {2}; the piece sweep gives {3}".format(
         NCP, NCOV * NPI, yn(BEQUI), NPP))

gate(PAIR_DIV and PAIR_PP and PAIR_CP and PAIR_CC,
     "G33",
     "pairings of the two fixed-point counts, each dividing exactly: piece {0}, cover {1}, cross {2}".format(
         QPP, QCC, QCP))

gate(CTL_OK and GOOD_PRIME and WIT > 0 and len(RKHIST) == 1,
     "G34",
     "single-orbit mod-{0} ranks, value to count: {1}; ordered-pair control reaches {2}".format(
         PRIME, RKHIST, CTL))

gate(BEATS,
     "G35",
     "single-orbit modular rank exceeds exact cover rank {0} by {1}; the associated count is {2}".format(
         RANKB, GAIN, TIEVAL))

gate(CYC_OK,
     "G36",
     "cycle rule: {0} of {1} orbit checks differ from the predicted rank; cycle types {2}".format(
         CYCBAD, NCP, CYCLIST))

gate(HAND_OK,
     "G37",
     "hand bound: S {0}, order times S {1}, half its integer square root {2}, bound {3}; the largest {4} clears it".format(
         SVAL, PROD, HALF, BOUND, WIT))

gate(SZ_OK,
     "G38",
     "the {0} cover-piece orbits all have size {1}, summing to {2} cells".format(
         NCP, SZLIST[0][0], SZ_SUM))

gate(COUNT_OK and REB_OK,
     "G39",
     "each orbit puts {0} ones in every cover row, so {1} orbits make {2}; those {1} rebuild the cover table exactly".format(
         CONTRIB, NEEDED, BROWS[0]))

gate(BORD_OK and RUN_OK,
     "G40",
     "the {0} selected cover orbits each have mod-p rank {1}; modular prefix ranks {2}, exact cover rank {3}".format(
         NEEDED, BORD_RK[0], RUN, RANKB))

gate(WITNESS_OK,
     "G41",
     "orbit union {0} has row and column sum {1}, exact rank {2}; cover exact rank {3}".format(
         WITSEL, WIT_ROWS[0], RX_WIT, RX_B))

gate(ID_OK,
     "D8",
     "control: the identity table of size {0} returns dimension {1} over the integers".format(
         NCOV, RX_ID))

gate(DUP_OK,
     "D9",
     "control: the cover table stacked on itself gives dimension {0}, the cover table alone gives {1}".format(
         RX_DUP, RX_B))

gate(EXACT_OK,
     "D10",
     "exact dimension of the cover table over the integers: {0}; agrees with the modular count: {1}".format(
         RX_B, yn(EXACT_OK)))

gate(NO_PC and NO_TAB and NO_EM and ASCII_OK and BAN_OK and NBAN == len(BAN),
     "G42",
     "source hygiene: plain ASCII, no per-cent character, no tab, no long dash, all {0} barred strings absent".format(
         NBAN))

gate(RESOURCE_UNIT_CONTROL and ELAPSED < AUDIT_TIMEOUT_SEC and RSSMB < MEMORY_LIMIT_MB,
     "G43",
     "budget: elapsed under {0} seconds, peak memory under {1} MB, Darwin/Linux unit controls pass".format(
         AUDIT_TIMEOUT_SEC, MEMORY_LIMIT_MB))

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
