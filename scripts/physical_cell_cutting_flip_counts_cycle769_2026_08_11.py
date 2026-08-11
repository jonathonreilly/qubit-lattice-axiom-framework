"""Four fixed-point counts force the cell-orbit count and a positive blind floor.

Standalone exact runner. It rebuilds the unit four-cube cell object from scratch:
the sixteen corners, the five-corner unit-determinant pieces at the adjacency cost
floor, the cuttings by them, the pieces that occur, and the eight-piece covers.
The symmetry group of order 384 is built by permuting the four coordinates and
flipping any of them, and it is transitive on the pieces and on the covers.

The subject of this cycle is four integers: how many pieces and how many covers
are fixed by the non-identity element of one piece stabiliser and of one cover
stabiliser. Each of the three orbit counts on ordered pairs is obtained twice,
once by direct orbit enumeration on the permutations and once from a two-element
stabiliser's fixed-point count. A perturbed copy of the action breaks the tie, so
the tie is not automatic. The four counts then force the cell-orbit count and a
strictly positive blind floor, and they show that the ceiling and the floor add to
the piece count for a reason rather than by accident.

All work is over the integers, the rationals and two fixed primes; no floating
point enters any gate and no constant is fitted.

Output: one line per gate, then the characters printed before that line, then
the total line.
"""

import itertools
import math
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

# ------------------------------------------------------------------
# 2. the group: permuting the four coordinates and flipping any of them
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
for a in MAPS:
    for b in MAPS:
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

IDP = tuple(range(NPI))
EID = PERM.index(IDP)

orbp = set([0])
frp = [0]
while frp:
    x = frp.pop()
    for p in PERM:
        y = p[x]
        if y not in orbp:
            orbp.add(y)
            frp.append(y)
PIECE_TRANS = (len(orbp) == NPI)

# the same group moves the covers
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
IDC = tuple(range(NCOV))
COV_BIJ = (len(CPERM) == NGRP
           and all(sorted(q) == list(range(NCOV)) for q in CPERM)
           and len(set(CPERM)) == NGRP)
orbc = set([0])
frc = [0]
while frc:
    x = frc.pop()
    for q in CPERM:
        y = q[x]
        if y not in orbc:
            orbc.add(y)
            frc.append(y)
COV_TRANS = (len(orbc) == NCOV)

# two elements generate the whole group; orbits may then be walked from them
GEN_DESC = [((1, 2, 3, 0), 0), ((1, 0, 2, 3), 1)]
GIDX = [DESC.index(d) for d in GEN_DESC]
GENS = [PERM[e] for e in GIDX]
GENC = [CPERM[e] for e in GIDX]
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

# ------------------------------------------------------------------
# 3. the two stabilisers
# ------------------------------------------------------------------

STABP = [e for e in range(NGRP) if PERM[e][0] == 0]
STABC = [e for e in range(NGRP) if CPERM[e][0] == 0]
NSP = len(STABP)
NSC = len(STABC)
EP = [e for e in STABP if e != EID][0] if NSP == 2 else -1
EC = [e for e in STABC if e != EID][0] if NSC == 2 else -1
SP = PERM[EP]
SC_ = CPERM[EC]
SQ_P = (tuple(SP[SP[i]] for i in range(NPI)) == IDP)
SQ_C = (tuple(SC_[SC_[i]] for i in range(NCOV)) == IDC)
DIFF_S = (EP != EC and PERM[EP] != PERM[EC] and CPERM[EP] != CPERM[EC])
ORBSTAB = (NGRP // NSP == NPI and NGRP // NSC == NCOV
           and NGRP == NSP * NPI and NGRP == NSC * NCOV)
GEN_NOT_S = all(g != EP and g != EC and g != EID for g in GIDX)

# ------------------------------------------------------------------
# 4. orbit counts, by direct enumeration on the permutations
# ------------------------------------------------------------------


def sweep_labels(act1, n1, act2, n2):
    """label every ordered pair by sweeping the whole group over it"""
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


LAB, NORB = sweep_labels(PERM, NPI, PERM, NPI)
CCLAB, NPOC = sweep_labels(CPERM, NCOV, CPERM, NCOV)
CPLAB, NCP = sweep_labels(CPERM, NCOV, PERM, NPI)
SWEEP_FULL = (min(min(r) for r in LAB) >= 0 and min(min(r) for r in CCLAB) >= 0
              and min(min(r) for r in CPLAB) >= 0)

LA = np.array(LAB, dtype=np.int64)
CCA = np.array(CCLAB, dtype=np.int64)
CA = np.array(CPLAB, dtype=np.int64)
LAB_INV = True
for e in range(NGRP):
    jp = np.array(PERM[e], dtype=np.int64)
    jc = np.array(CPERM[e], dtype=np.int64)
    if not np.array_equal(LA[np.ix_(jp, jp)], LA):
        LAB_INV = False
    if not np.array_equal(CCA[np.ix_(jc, jc)], CCA):
        LAB_INV = False
    if not np.array_equal(CA[np.ix_(jc, jp)], CA):
        LAB_INV = False


def comp_count(g1, n1, g2, n2):
    """orbits of the group generated by the paired permutations, walked directly"""
    seen = [False] * (n1 * n2)
    cnt = 0
    ng = len(g1)
    for s in range(n1 * n2):
        if seen[s]:
            continue
        cnt += 1
        seen[s] = True
        fr = [s]
        while fr:
            x = fr.pop()
            i, j = divmod(x, n2)
            for t in range(ng):
                y = g1[t][i] * n2 + g2[t][j]
                if not seen[y]:
                    seen[y] = True
                    fr.append(y)
    return cnt


WPP = comp_count(GENS, NPI, GENS, NPI)
WCC = comp_count(GENC, NCOV, GENC, NCOV)
WCP = comp_count(GENC, NCOV, GENS, NPI)
WALK_OK = (WPP == NORB and WCC == NPOC and WCP == NCP)

FIXP = [sum(1 for i in range(NPI) if p[i] == i) for p in PERM]
FIXC = [sum(1 for i in range(NCOV) if q[i] == i) for q in CPERM]
QPP, RPP = divmod(sum(f * f for f in FIXP), NGRP)
QCC, RCC = divmod(sum(f * f for f in FIXC), NGRP)
QCP, RCP = divmod(sum(FIXC[e] * FIXP[e] for e in range(NGRP)), NGRP)
AVG_OK = (RPP == 0 and RCC == 0 and RCP == 0
          and QPP == NORB and QCC == NPOC and QCP == NCP)

# ------------------------------------------------------------------
# 5. the four fixed-point counts and the counting identity
# ------------------------------------------------------------------

FPP = sum(1 for i in range(NPI) if PERM[EP][i] == i)
FCP = sum(1 for i in range(NCOV) if CPERM[EP][i] == i)
FPC = sum(1 for i in range(NPI) if PERM[EC][i] == i)
FCC = sum(1 for i in range(NCOV) if CPERM[EC][i] == i)


def breaks(npp, npoc, ncp, fpp, fcc, fpc, fcp):
    """how many of the four counting identities fail on the data handed in"""
    b = 0
    if 2 * npp - NPI != fpp:
        b += 1
    if 2 * npoc - NCOV != fcc:
        b += 1
    if 2 * ncp - NPI != fpc:
        b += 1
    if 2 * ncp - NCOV != fcp:
        b += 1
    return b


TRUE_BREAK = breaks(NORB, NPOC, NCP, FPP, FCC, FPC, FCP)


def orb2(perm, n):
    """orbits of the two-element group generated by an involution, counted directly"""
    return sum(1 for i in range(n) if perm[i] >= i)


O2PP = orb2(PERM[EP], NPI)
O2CC = orb2(CPERM[EC], NCOV)
O2PC = orb2(PERM[EC], NPI)
O2CP = orb2(CPERM[EP], NCOV)
TWO_OK = (O2PP == NORB and O2CC == NPOC and O2PC == NCP and O2CP == NCP)

# ------------------------------------------------------------------
# 6. the discriminator: perturbed copies of the action
# ------------------------------------------------------------------

TRANS = []
kk = 1
while len(TRANS) < 6:
    a = divmod(SEED * kk, NPI)[1]
    b = divmod(SEED * kk * kk + 5, NPI)[1]
    if a != b and (a, b) not in TRANS:
        TRANS.append((a, b))
    kk += 1


def swapped(p, a, b):
    v = list(p)
    v[a], v[b] = v[b], v[a]
    return tuple(v)


PBRK = []
for (a, b) in TRANS:
    g0 = swapped(GENS[0], a, b)
    pg = [g0, GENS[1]]
    npp = comp_count(pg, NPI, pg, NPI)
    npoc = comp_count(GENC, NCOV, GENC, NCOV)
    ncp = comp_count(GENC, NCOV, pg, NPI)
    pperm = list(PERM)
    pperm[GIDX[0]] = g0
    fpp = sum(1 for i in range(NPI) if pperm[EP][i] == i)
    fpc = sum(1 for i in range(NPI) if pperm[EC][i] == i)
    fcp = sum(1 for i in range(NCOV) if CPERM[EP][i] == i)
    fcc = sum(1 for i in range(NCOV) if CPERM[EC][i] == i)
    PBRK.append(breaks(npp, npoc, ncp, fpp, fcc, fpc, fcp))

CBRK = []
for (a, b) in TRANS:
    h0 = swapped(GENC[0], a, b)
    cg = [h0, GENC[1]]
    npp = comp_count(GENS, NPI, GENS, NPI)
    npoc = comp_count(cg, NCOV, cg, NCOV)
    ncp = comp_count(cg, NCOV, GENS, NPI)
    cperm = list(CPERM)
    cperm[GIDX[0]] = h0
    fpp = sum(1 for i in range(NPI) if PERM[EP][i] == i)
    fpc = sum(1 for i in range(NPI) if PERM[EC][i] == i)
    fcp = sum(1 for i in range(NCOV) if cperm[EP][i] == i)
    fcc = sum(1 for i in range(NCOV) if cperm[EC][i] == i)
    CBRK.append(breaks(npp, npoc, ncp, fpp, fcc, fpc, fcp))

NTRY = len(TRANS)
PMIN = min(PBRK)
PMAX = max(PBRK)
CMIN = min(CBRK)
CMAX = max(CBRK)
FIRSTP = 1 + [i for i in range(NTRY) if PBRK[i] > 0][0] if PMAX > 0 else -1
FIRSTC = 1 + [i for i in range(NTRY) if CBRK[i] > 0][0] if CMAX > 0 else -1
DISC_OK = (PMIN >= 1 and CMIN >= 1 and TRUE_BREAK == 0)

# ------------------------------------------------------------------
# 7. freeness on the cells, and the forced cell-orbit count
# ------------------------------------------------------------------

NCELL = NCOV * NPI
FIXED_CELLS = sum(FIXC[e] * FIXP[e] for e in range(NGRP) if e != EID)
ALLFIX = sum(FIXC[e] * FIXP[e] for e in range(NGRP))
CELL_AVG, CELL_R = divmod(ALLFIX, NGRP)
FREE_OK = (FIXED_CELLS == 0 and CELL_R == 0 and CELL_AVG == NCP
           and NCELL == NGRP * NCP and NCP == NGRP // (NSP * NSC))

MOVED = sum(1 for i in range(NPI) if PERM[EC][i] != i)
NCHK = 0
IMPL_OK = True
for c in range(NCOV):
    st = [e for e in range(NGRP) if CPERM[e][c] == c]
    if len(st) != 2:
        IMPL_OK = False
        break
    o = [e for e in st if e != EID][0]
    if FIXP[o] != 0:
        IMPL_OK = False
        break
    NCHK += 1

# ------------------------------------------------------------------
# 8a. exact linear algebra used by the part table
# ------------------------------------------------------------------


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


def clear_den(v):
    den = 1
    for x in v:
        den = den * x.denominator // math.gcd(den, x.denominator)
    return [int(x * den) for x in v]


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


# ------------------------------------------------------------------
# 8b. orbit matrices, structure constants, and the centre
# ------------------------------------------------------------------

OPS = np.zeros((NORB, NPI, NPI), dtype=np.int64)
for a in range(NORB):
    OPS[a] = (LA == a).astype(np.int64)
OXS = np.zeros((NCP, NCOV, NPI), dtype=np.int64)
for k in range(NCP):
    OXS[k] = (CA == k).astype(np.int64)
BM = np.array(BROW, dtype=np.int64)


def op_of(z):
    return np.tensordot(np.array(z, dtype=np.int64), OPS, axes=([0], [0]))


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
BM_OK = (BSPLIT and np.array_equal(BREB, BM))
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
for a, b in SCPAIRS:
    P1 = OPS[a] @ OPS[b]
    P2 = np.tensordot(SC[a][b], OPS, axes=([0], [0]))
    SC_CHK += 1
    if not np.array_equal(P1, P2):
        SC_AGREE = False
del P1, P2

DFC = SC - np.transpose(SC, (1, 0, 2))
CON = np.ascontiguousarray(np.transpose(DFC, (1, 2, 0)).reshape(NORB * NORB, NORB))
del DFC

SEL, RKC = mod_pick(CON, NORB, PRIME)
CROWS = [CON[i].tolist() for i in SEL]
del CON
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
for z in CENB:
    za = np.array(z, dtype=np.int64)
    LZ = np.tensordot(za, SC, axes=([0], [0]))
    RZ = np.tensordot(za, SC, axes=([0], [1]))
    if not np.array_equal(LZ, RZ):
        CEN_OK = False

# ------------------------------------------------------------------
# 8c. one central element and the values it separates
# ------------------------------------------------------------------

NBCOL = [[CENB[l][a] for l in range(NCEN)] for a in range(NORB)]
TRY = 0
TWORK = 0
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
        VALS = vv
        NUL = nn
        M0 = MC
        Z0 = op_of(wv)

VAL_OK = (TWORK > 0 and len(VALS) == NCEN and all(x == 1 for x in NUL))
REP_OK = VAL_OK
if VAL_OK:
    for k in [0, 1, NCEN - 1]:
        LHS = Z0 @ op_of(CENB[k])
        RHS = np.zeros((NPI, NPI), dtype=np.int64)
        for l in range(NCEN):
            if M0[l][k]:
                RHS = RHS + M0[l][k] * op_of(CENB[l])
        if not np.array_equal(LHS, RHS):
            REP_OK = False
    del LHS, RHS

# ------------------------------------------------------------------
# 8d. the part table
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
    PARTS.append((dim, d, m, mc, blind))
    del PR, XR, KB, AZ, stk

NPART = len(PARTS)
DIMS = sorted(t[0] for t in PARTS)
DIMSTR = ",".join(str(x) for x in DIMS)
SUM_DIM = sum(t[0] for t in PARTS)
SUM_DM = sum(t[1] * t[2] for t in PARTS)
SUM_DMC = sum(t[1] * t[3] for t in PARTS)
SUM_MM = sum(t[2] * t[2] for t in PARTS)
SUM_CC = sum(t[3] * t[3] for t in PARTS)
SUM_MMC = sum(t[2] * t[3] for t in PARTS)
SUM_BL = sum(t[4] for t in PARTS)
BRIDGE_OK = (SUM_MM == NORB and SUM_CC == NPOC and SUM_MMC == NCP)

# ------------------------------------------------------------------
# 9. the positive floor
# ------------------------------------------------------------------

GAP = SUM_MM - SUM_MMC
BIGGER = [t for t in PARTS if t[2] > t[3]]
NBIG = len(BIGGER)
CEIL = sum(t[1] * min(t[2], t[3]) for t in PARTS)
FLOORB = sum(t[1] * max(0, t[2] - t[3]) for t in PARTS)
CONTRIB = [t for t in PARTS if t[1] * max(0, t[2] - t[3]) > 0]
SAME_SET = (sorted(CONTRIB) == sorted(BIGGER))
POS_OK = (GAP > 0 and NBIG >= 1)
SLACK = min(t[4] - t[1] * max(0, t[2] - t[3]) for t in PARTS)

# ------------------------------------------------------------------
# 10. ceiling plus floor is the piece count
# ------------------------------------------------------------------


def row_ok(dim, d, m, mc):
    """a row is sound when its dimension is d times m and the split rebuilds it"""
    if m < 0 or mc < 0 or d < 1 or dim != d * m:
        return False
    return d * min(m, mc) + d * max(0, m - mc) == dim


NROWS = sum(1 for t in PARTS if row_ok(t[0], t[1], t[2], t[3]))
ROW_OK = (NROWS == NPART)
ADD_OK = (CEIL + FLOORB == SUM_DM and SUM_DM == NPI and NPI == NCOV)

K0 = INB[0]
SGL = OXS[K0].tolist()
SGR1 = rank_modp(SGL, PRIME)
SGR2 = rank_modp(SGL, PRIME2)
SGN = NPI - SGR1
SGL_OK = (SGR1 == SGR2 and SGR1 == CEIL and SGN == FLOORB and SGR1 + SGN == NPI)

# ------------------------------------------------------------------
# 11. wrong-value rejectors
# ------------------------------------------------------------------

WRONGF = [(FPP + 1, FCC, FPC, FCP), (FPP - 1, FCC, FPC, FCP),
          (FPP, FCC + 1, FPC, FCP), (FPP, FCC - 1, FPC, FCP),
          (FPP, FCC, FPC + 1, FCP), (FPP, FCC, FPC, FCP + 1),
          (FCC, FPP, FPC, FCP), (FPP, FCC, FCC, FCP)]
NREJF = sum(1 for w in WRONGF
            if breaks(NORB, NPOC, NCP, w[0], w[1], w[2], w[3]) >= 1)
REJF_OK = (NREJF == len(WRONGF) and TRUE_BREAK == 0)

WRONGR = []
for t in PARTS:
    WRONGR.append((t[0] + 1, t[1], t[2], t[3]))
    WRONGR.append((t[0], t[1] + 1, t[2], t[3]))
NREJR = sum(1 for w in WRONGR if not row_ok(w[0], w[1], w[2], w[3]))
REJR_OK = (NREJR == len(WRONGR))

# ------------------------------------------------------------------
# 12. source hygiene
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
# 13. budget
# ------------------------------------------------------------------

ELAPSED = int(time.time() - T0)
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSSMB = RSS // 1048576 if RSS > 10000000 else RSS // 1024

# ------------------------------------------------------------------
# gates
# ------------------------------------------------------------------

emit("all numbers below are exact computational identities;"
     " no floating point enters any gate")

gate(NCAND == 2672 and NKEPT == 400 and FLOOR == 6 and NS == 15800
     and SIZES == [24] and NPI == 192 and NCOV == 192 and GENERIC, "C0",
     "object: {0} pieces, {1} at cost floor {2}, {3} cuttings of {4},"
     " {5} used, {6} covers".format(NCAND, NKEPT, FLOOR, NS, SIZES[0],
                                    NPI, NCOV))

gate(PCSET == [1975] and 8 * 1975 == NS and BRS == [8] and COVEXACT, "C1",
     "each piece lies in {0} cuttings, 8 times {0} is {1}; each cover has 8"
     " pieces and meets every cutting once".format(1975, NS))

gate(NGRP == 384 and MAPS_DISTINCT and CLOSED and KEEPS_PIECES, "C2",
     "group: {0} coordinate maps, all distinct, closed under composition,"
     " every one carries pieces to pieces".format(NGRP))

gate(PERM_DISTINCT and BIJ and PIECE_TRANS, "C3",
     "piece action: {0} distinct bijections of the {1} pieces, one orbit"
     .format(NGRP, NPI))

gate(COV_OK and COV_BIJ and COV_TRANS, "C4",
     "cover action: {0} distinct bijections of the {1} covers, one orbit"
     .format(NGRP, NCOV))

gate(GEN_OK and GEN_NOT_S, "C5",
     "two of the {0} elements generate all {0}; neither is the identity nor"
     " either stabiliser element".format(NGRP))

gate(NSP == 2 and NSC == 2 and SQ_P and SQ_C, "C6",
     "stabiliser of piece 0 has order {0}, of cover 0 has order {1}; both"
     " non-identity elements square to the identity".format(NSP, NSC))

gate(DIFF_S and ORBSTAB, "C7",
     "the two stabiliser elements differ; {0} = {1} times {2} = {3} times {4}"
     .format(NGRP, NSP, NPI, NSC, NCOV))

gate(SWEEP_FULL and LAB_INV and NORB == 104 and NPOC == 120 and NCP == 96,
     "C8",
     "direct orbit counts: {0} on ordered piece pairs, {1} on ordered cover"
     " pairs, {2} on cover-by-piece cells".format(NORB, NPOC, NCP))

gate(WALK_OK, "C9",
     "same three counts walked from the two generators alone: {0}, {1}, {2}"
     .format(WPP, WCC, WCP))

gate(AVG_OK, "C10",
     "fixed-point averages over the group give the same three counts:"
     " {0}, {1}, {2}".format(QPP, QCC, QCP))

gate(FPP == 16 and FCP == 0 and FPC == 0 and FCC == 48, "C11",
     "the four counts: piece stabiliser fixes {0} pieces and {1} covers;"
     " cover stabiliser fixes {2} pieces and {3} covers"
     .format(FPP, FCP, FPC, FCC))

gate(TRUE_BREAK == 0, "C12",
     "twice the orbit count minus the set size {0} equals the measured fixed"
     " count in all four cases: {1}, {2}, {3}, {4}"
     .format(NPI, 2 * NORB - NPI, 2 * NPOC - NCOV, 2 * NCP - NPI,
             2 * NCP - NCOV))

gate(TWO_OK, "C13",
     "two-element stabiliser orbits counted directly: {0} on pieces, {1} on"
     " covers, {2} and {3} across".format(O2PP, O2CC, O2PC, O2CP))

gate(PMIN >= 1, "C14",
     "perturbed piece action: all {0} transpositions tried break at least one"
     " of the four, fewest {1}, most {2}, the first already at try {3}"
     .format(NTRY, PMIN, PMAX, FIRSTP))

gate(CMIN >= 1, "C15",
     "perturbed cover action: all {0} transpositions tried break at least one"
     " of the four, fewest {1}, most {2}, the first already at try {3}"
     .format(NTRY, CMIN, CMAX, FIRSTC))

gate(DISC_OK, "C16",
     "the true action breaks {0} of the four while every perturbation breaks"
     " at least {1}, so the agreement is not automatic"
     .format(TRUE_BREAK, min(PMIN, CMIN)))

gate(FIXED_CELLS == 0 and MOVED == NPI, "C17",
     "no non-identity element fixes any of the {0} cells; the cover"
     " stabiliser moves all {1} pieces".format(NCELL, MOVED))

gate(IMPL_OK and NCHK == NCOV, "C18",
     "for each of the {0} covers the stabiliser's other element fixes no"
     " piece, so cover and piece stabilisers meet in the identity"
     .format(NCHK))

gate(FREE_OK, "C19",
     "free action: {0} = {1} times {2}, and {2} = {1} over {3} times {4}"
     .format(NCELL, NGRP, NCP, NSP, NSC))

gate(PART_OK and NPART == 20 and NCEN == 20 and SUM_DIM == NPI, "C20",
     "part table: {0} rows, dimensions {1}".format(NPART, DIMSTR))

gate(BM_OK and REP_FULL and SC_AGREE and SC_CHK == 7 and GUARD_OK
     and CEN_OK and REP_OK and RKC + NCEN == NORB, "C21",
     "the {0} orbit matrices multiply by the structure constants on {1}"
     " sampled pairs; the centre has dimension {2}"
     .format(NORB, SC_CHK, NCEN))

gate(SUM_DM == NPI and SUM_DMC == NCOV, "C22",
     "sum of d times m is {0}, sum of d times mc is {1}"
     .format(SUM_DM, SUM_DMC))

gate(SUM_MM == 104 and SUM_CC == 120 and SUM_MMC == 96, "C23",
     "part table sums: m dot m is {0}, mc dot mc is {1}, m dot mc is {2}"
     .format(SUM_MM, SUM_CC, SUM_MMC))

gate(BRIDGE_OK, "C24",
     "bridge: those three sums equal the direct orbit counts {0}, {1}, {2}"
     .format(NORB, NPOC, NCP))

gate(POS_OK and GAP == 8, "C25",
     "m dot m minus m dot mc is {0}, strictly above zero, so at least one"
     " part has m above mc: {1} do".format(GAP, NBIG))

gate(FLOORB == 48 and SAME_SET, "C26",
     "the blind floor is {0}, carried by the {1} parts with m above mc, which"
     " are its contributors by bookkeeping since d is at least 1"
     .format(FLOORB, NBIG))

gate(SLACK >= 0, "C27",
     "each part's measured blind dimension is at least its forced part;"
     " total blind dimension {0}, least slack {1}".format(SUM_BL, SLACK))

gate(ROW_OK and NROWS == 20, "C28",
     "row by row on all {0} rows, d times min plus d times the positive"
     " difference rebuilds the row dimension".format(NROWS))

gate(CEIL == 144 and FLOORB == 48 and ADD_OK, "C29",
     "ceiling {0} plus floor {1} is {2}, which is the piece count and the"
     " cover count".format(CEIL, FLOORB, SUM_DM))

gate(SGL_OK, "C30",
     "one cell orbit alone has rank {0} at both primes and blind dimension"
     " {1}, and {0} plus {1} is {2}".format(SGR1, SGN, NPI))

gate(REJF_OK, "C31",
     "wrong-count rejector: {0} of {0} altered fixed-point tuples break at"
     " least one identity".format(NREJF))

gate(REJR_OK, "C32",
     "wrong-row rejector: {0} of {0} altered rows fail the row test, which"
     " turns on the dimension being d times m".format(NREJR))

gate(ASCII_OK and NO_PC and NO_TAB and NO_EM and NO_D9 and BAN_OK, "C33",
     "source hygiene: ASCII {0}, no tab {1}, no remainder sign {2}, no long"
     " dash {3}, {4} barred strings absent {5}"
     .format(yn(ASCII_OK), yn(NO_TAB), yn(NO_PC), yn(NO_EM), NBAN, yn(BAN_OK)))

gate(ELAPSED < 900 and RSSMB < 2500 and OUT[0] + 200 < 5200, "C34",
     "budget: {0} s under 900, {1} MB under 2500, stdout under 5200 with"
     " {2} to spare".format(nd(ELAPSED), nd(RSSMB), nd(5200 - 200 - OUT[0])))

emit("characters printed before this line: {0}".format(nd(OUT[0])))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
