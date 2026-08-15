"""Physical cell cutting: the interface transfer operator, its exact spectrum, and strip growth.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, and the order-384 group of signed
coordinate maps of the cell. Nothing outside that finite object enters any gate.

The work of this cycle is the interface transfer operator of one axis. Every cutting dissects each of the eight boundary three-cubes into
six tetrahedra, and only 16 such dissections ever occur; they are the letters of the facet alphabet. For an axis a the 16 by 16 integer
matrix T_a counts, in entry (k, j), the cuttings whose letter on side 0 of a is k and whose letter on side 1 is j. The four axes give the
same matrix entry for entry, so one matrix T carries the whole interface.

The gates certify: the matrix and its censuses; the mechanism by which the maps holding a facet act by one letter map on both boundary
cubes, hence the twelve-dimensional commuting algebra and the twelve orbits on ordered letter pairs; the exact factored characteristic
polynomial with its kernel dimensions and a fully discriminating minimal-polynomial test; the class block and the growth eigenvalue with
exact certificates in the ring adjoining the square root of 243057; the closed strip counts of one to six cells and their recurrence
cross-check; the invariant factors and the determinant; and the evenness theorem for the entries, derived on 208 of the 256 fibers by an
explicit free pairing and left as a measurement on the remaining orbit of 48, where the group mechanism provably cannot certify it.

Gates G1 to G22, one line each, then a resource line and the total line. Any failure exits nonzero."""

import itertools
import sys
import time
import resource
from collections import Counter
from fractions import Fraction as FR

AUDIT_TIMEOUT_SEC = 900

T0 = time.time()
OUT = [0]


def emit(s):
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    if len(txt) > 148:
        raise ValueError("output line over the length limit")
    OUT[0] += len(txt) + 1
    print(txt)


STAT = [0, 0]


def gate(ok, tag, msg):
    if ok:
        STAT[0] += 1
    else:
        STAT[1] += 1
    emit("{0} {1} {2}".format("PASS" if ok else "FAIL", tag, msg))


def dshow(d):
    return "{" + ", ".join("{0}: {1}".format(k, d[k]) for k in sorted(d)) + "}"


def lshow(v):
    return "[" + ",".join("{0}".format(x) for x in v) + "]"


# ---------------------------------------------------------------- the object

CORN = [tuple((i >> b) & 1 for b in range(4)) for i in range(16)]
CIDX = {c: i for i, c in enumerate(CORN)}


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
    M = [[FR(C[r][c]) for c in range(n)] + [FR(1 if r == c else 0) for c in range(n)] for r in range(n)]
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


CAND = [S for S in itertools.combinations(range(16), 5)
        if abs(det4([[CORN[S[j + 1]][r] - CORN[S[0]][r] for j in range(4)] for r in range(4)])) == 1]
COSTS = [adjcost(S) for S in CAND]
FLOOR = min(COSTS)
KEPT = [CAND[i] for i in range(len(CAND)) if COSTS[i] == FLOOR]

BARY = []
for S in KEPT:
    v0 = CORN[S[0]]
    C = [[CORN[S[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]
    BARY.append((v0, inv4(C)))

NSHIFT, OFFS, RSTEP = 16, (1, 2, 4, 8), 5
DIV = NSHIFT * RSTEP
AXVAL = [[NSHIFT * k + OFFS[i] for k in range(RSTEP)] for i in range(4)]
NPTS = RSTEP ** 4
MASK = []
for (v0, Ci) in BARY:
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
                    w = [s3[i] + d[i] for i in range(4)]
                    sw = sum(w)
                    if all(x > 0 for x in w) and sw < DIV:
                        bits |= (1 << idx)
                    idx += 1
    MASK.append(bits)
UNIV = (1 << NPTS) - 1

BYPT = [[] for _ in range(NPTS)]
for t in range(len(KEPT)):
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
USED = sorted(set(t for s in SOLS for t in s))
NU = len(USED)
SIDX = {frozenset(s): i for i, s in enumerate(SOLS)}
KIDX = {frozenset(S): t for t, S in enumerate(KEPT)}
PSIZE = len(set(len(s) for s in SOLS))
CSIZE = sorted(set(len(s) for s in SOLS))[0]

P4 = list(itertools.permutations(range(4)))
G384 = [(p, m) for p in P4 for m in range(16)]

FACE = {}
for t in USED:
    S = KEPT[t]
    for a in range(4):
        for c in (0, 1):
            F = [v for v in S if CORN[v][a] == c]
            if len(F) == 4:
                FACE[(t, a, c)] = frozenset(tuple(CORN[v][r] for r in range(4) if r != a) for v in F)

KEYF = []
for s in SOLS:
    d = {}
    for a in range(4):
        for c in (0, 1):
            d[(a, c)] = frozenset(FACE[(t, a, c)] for t in s if (t, a, c) in FACE)
    KEYF.append(d)

ALLK = sorted({d[k] for d in KEYF for k in d}, key=lambda f: sorted(sorted(t) for t in f))
KN = {k: i for i, k in enumerate(ALLK)}
KEY = [{k: KN[v] for k, v in d.items()} for d in KEYF]
NL = len(ALLK)

gate(len(CAND) == 2672 and FLOOR == 6 and len(KEPT) == 400 and NS == 15800 and NU == 192
     and PSIZE == 1 and CSIZE == 24 and len(G384) == 384, "G1",
     "the cell has 2672 unit-determinant five-corner pieces, cost floor 6, 400 kept, 15800 cuttings of 24, 192 used, group order 384")

# ---------------------------------------------------------------- G2 the alphabet

SLOTSETS = [set(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
SAME = all(x == SLOTSETS[0] for x in SLOTSETS)
MULT = [Counter(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
MCEN = dict(sorted(Counter(MULT[0].values()).items()))
MSAME = all(m == MULT[0] for m in MULT)

gate(NL == 16 and SAME and len(SLOTSETS) == 8 and len(SLOTSETS[0]) == 16 and MSAME
     and MCEN == {862: 12, 1364: 4}, "G2",
     "the facet alphabet has 16 letters, the same 16 on all 8 slots, with slot multiplicity census {0}".format(dshow(MCEN)))

# ---------------------------------------------------------------- G3 to G7 the transfer operator

TMS = []
for a in range(4):
    J = Counter((KEY[i][(a, 0)], KEY[i][(a, 1)]) for i in range(NS))
    TMS.append([[J[(x, y)] for y in range(16)] for x in range(16)])
TR = TMS[0]
AXEQ = sum(1 for a in range(4) for x in range(16) for y in range(16) if TMS[a][x][y] != TR[x][y])
SYMM = sum(1 for x in range(16) for y in range(16) if TR[x][y] != TR[y][x])
RSUM = [sum(TR[k]) for k in range(16)]
RCEN = dict(sorted(Counter(RSUM).items()))
RMULT = all(RSUM[k] == MULT[0][k] for k in range(16))
ECEN = dict(sorted(Counter(TR[x][y] for x in range(16) for y in range(16)).items()))
TRC = sum(TR[x][x] for x in range(16))
DEVEN = sum(1 for x in range(16) if (TR[x][x] & 1) == 0)

gate(AXEQ == 0 and len(TMS) == 4 and 16 * 16 == 256, "G3",
     "axis equality T_0 = T_1 = T_2 = T_3 entry for entry, 4 axes over all 256 entries, 0 misses")
gate(SYMM == 0, "G4", "the transfer operator is symmetric, T[k][j] = T[j][k] on all 256 entries, 0 misses")
gate(RMULT and RCEN == {862: 12, 1364: 4} and 12 * 862 + 4 * 1364 == NS, "G5",
     "every row sum is that letter's multiplicity, census {0}, and 12 x 862 + 4 x 1364 = 15800".format(dshow(RCEN)))
gate(ECEN == {18: 24, 36: 48, 50: 48, 52: 48, 90: 12, 92: 48, 100: 12, 104: 12, 200: 4}
     and min(ECEN) == 18, "G6",
     "entry census {0}, least entry 18, strictly positive".format(dshow(ECEN)))
gate(TRC == 2000 and DEVEN == 16 and 2 * 1000 == TRC, "G7",
     "trace 2000 with all 16 diagonal entries even, so the trace is 2 x 1000")

# ---------------------------------------------------------------- G8, G9 the holding maps

STAB = [(p, m) for (p, m) in G384 if p[0] == 0]
NONSW = [g for g in STAB if not (g[1] & 1)]
SWAPS = [g for g in STAB if (g[1] & 1)]


def actcorner(g, v):
    p, m = g
    x = CORN[v]
    return CIDX[tuple(x[p[i]] ^ ((m >> p[i]) & 1) for i in range(4))]


def act3(g, pt):
    p, m = g
    return tuple(pt[p[i + 1] - 1] ^ ((m >> p[i + 1]) & 1) for i in range(3))


PSI = {}
PERM = {}
PBAD = 0
for g in STAB:
    ps = tuple(KN[frozenset(frozenset(act3(g, v) for v in tet) for tet in ALLK[li])] for li in range(16))
    if sorted(ps) != list(range(16)):
        PBAD += 1
    PSI[g] = ps
    mp = {t: KIDX[frozenset(actcorner(g, v) for v in KEPT[t])] for t in USED}
    PERM[g] = [SIDX[frozenset(mp[t] for t in s)] for s in SOLS]

MECH = 0
for g in NONSW:
    ps = PSI[g]
    pm = PERM[g]
    for i in range(NS):
        if KEY[pm[i]][(0, 0)] != ps[KEY[i][(0, 0)]] or KEY[pm[i]][(0, 1)] != ps[KEY[i][(0, 1)]]:
            MECH += 1
PSET = set(PSI[g] for g in NONSW)
CLOS = all(tuple(a[b[i]] for i in range(16)) in PSET for a in PSET for b in PSET)
IDIN = tuple(range(16)) in PSET

gate(len(STAB) == 96 and len(NONSW) == 48 and len(SWAPS) == 48 and PBAD == 0 and len(PSET) == 48
     and CLOS and IDIN and MECH == 0, "G8",
     "the 48 letter maps of the facet holder form a group; letters follow the cuttings on 15800 cuttings x 48 maps x 2 sides, 0 misses")

COMM = 0
for g in NONSW:
    ps = PSI[g]
    for k in range(16):
        for j in range(16):
            if TR[ps[k]][ps[j]] != TR[k][j]:
                COMM += 1
SEENP = set()
ORB = []
for k in range(16):
    for j in range(16):
        if (k, j) in SEENP:
            continue
        o = set()
        for g in NONSW:
            ps = PSI[g]
            o.add((ps[k], ps[j]))
        SEENP |= o
        vals = set(TR[a][b] for a, b in o)
        ORB.append((len(o), sorted(vals)))
FLAT = sorted((n, v[0]) for n, v in ORB)
CONST = all(len(v) == 1 for n, v in ORB)
TGT = [(4, 200), (12, 18), (12, 18), (12, 90), (12, 100), (12, 104), (24, 50), (24, 50),
       (24, 92), (24, 92), (48, 36), (48, 52)]

gate(COMM == 0 and len(ORB) == 12 and CONST and FLAT == TGT and len(set(e for n, e in FLAT)) == 9
     and sum(n for n, e in FLAT) == 256, "G9",
     "commutation 0 misses; 12 pair orbits, sizes {0}, entries {1}".format(
         lshow([n for n, e in FLAT]), lshow([e for n, e in FLAT])))

# ---------------------------------------------------------------- G10 the class block

LIGHT = [k for k in range(16) if RSUM[k] == 862]
HEAVY = [k for k in range(16) if RSUM[k] == 1364]
LL = set(sum(TR[k][j] for j in LIGHT) for k in LIGHT)
LH = set(sum(TR[k][j] for j in HEAVY) for k in LIGHT)
HL = set(sum(TR[k][j] for j in LIGHT) for k in HEAVY)
HH = set(sum(TR[k][j] for j in HEAVY) for k in HEAVY)
BLK = [[578, 284], [852, 512]]
BOK = (LL == {578} and LH == {284} and HL == {852} and HH == {512})
BTR = BLK[0][0] + BLK[1][1]
BDT = BLK[0][0] * BLK[1][1] - BLK[0][1] * BLK[1][0]

gate(BOK and len(LIGHT) == 12 and len(HEAVY) == 4 and BTR == 1090 and BDT == 53968
     and 578 + 284 == 862 and 852 + 512 == 1364, "G10",
     "class block: light rows (578, 284), heavy rows (852, 512); block trace 1090, block determinant 53968")

# ---------------------------------------------------------------- G11 to G14 the exact spectrum

N = 16
ID = [[1 if i == j else 0 for j in range(N)] for i in range(N)]


def fdet(M):
    A = [[FR(x) for x in row] for row in M]
    d = FR(1)
    for c in range(N):
        p = -1
        for r in range(c, N):
            if A[r][c] != 0:
                p = r
                break
        if p < 0:
            return FR(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        pv = A[c][c]
        d *= pv
        for r in range(c + 1, N):
            if A[r][c] != 0:
                f = A[r][c] / pv
                A[r] = [A[r][k] - f * A[c][k] for k in range(N)]
    return d


def frank(M):
    A = [[FR(x) for x in row] for row in M]
    rk = 0
    for c in range(N):
        p = -1
        for r in range(rk, N):
            if A[r][c] != 0:
                p = r
                break
        if p < 0:
            continue
        A[rk], A[p] = A[p], A[rk]
        pv = A[rk][c]
        for r in range(N):
            if r != rk and A[r][c] != 0:
                f = A[r][c] / pv
                A[r] = [A[r][k] - f * A[rk][k] for k in range(N)]
        rk += 1
    return rk


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def shift(lam):
    return [[TR[i][j] - (lam if i == j else 0) for j in range(N)] for i in range(N)]


TR2 = mmul(TR, TR)


def quadm(b, c):
    return [[TR2[i][j] - b * TR[i][j] + (c if i == j else 0) for j in range(N)] for i in range(N)]


def facval(t):
    return ((t - 50) ** 2 * (t - 42) ** 2 * (t - 10) ** 3 * (t + 54)
            * (t * t - 1090 * t + 53968) * (t * t - 250 * t + 7728) ** 3)


PTS = 0
for t in range(17):
    if fdet([[(t if i == j else 0) - TR[i][j] for j in range(N)] for i in range(N)]) == facval(t):
        PTS += 1

KD = [N - frank(shift(lam)) for lam in (50, 42, 10, -54)]
KQ = [N - frank(quadm(1090, 53968)), N - frank(quadm(250, 7728))]

FACT = [shift(50), shift(42), shift(10), shift(-54), quadm(1090, 53968), quadm(250, 7728)]


def fprod(idxs):
    A = ID
    for i in idxs:
        A = mmul(A, FACT[i])
    return A


ANN = all(x == 0 for r in fprod(range(6)) for x in r)
DROPS = sum(1 for d in range(6) if any(x != 0 for r in fprod([i for i in range(6) if i != d]) for x in r))

D1 = 1090 * 1090 - 4 * 53968
D2 = 250 * 250 - 4 * 7728


def isprime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n - (n // d) * d == 0:
            return False
        d += 1
    return True


SF1 = (D1 == 972228 and D1 == 4 * 243057 and 243057 == 3 * 81019 and isprime(81019)
       and 81019 - (81019 // 3) * 3 != 0)
SF2 = (D2 == 31588 and D2 == 4 * 7897 and 7897 == 53 * 149 and isprime(53) and isprime(149))

gate(PTS == 17, "G11",
     "the factored characteristic polynomial matches det(t I - T) at all 17 points t = 0 to 16, an identity in degree 16")
gate(KD == [2, 2, 3, 1] and KQ == [2, 6] and sum(KD) + sum(KQ) == 16, "G12",
     "kernel dimensions 2, 2, 3, 1 at 50, 42, 10, -54 and 2, 6 at the two quadratics, summing to 16")
gate(ANN and DROPS == 6, "G13",
     "the minimal polynomial has degree 8 and annihilates T, and each of the 6 single-factor drops leaves a nonzero matrix")
gate(SF1 and SF2, "G14",
     "1090^2 - 4 x 53968 = 972228 = 4 x 243057 = 4 x 3 x 81019, 81019 prime; 250^2 - 4 x 7728 = 31588 = 4 x 7897 = 4 x 53 x 149")

# ---------------------------------------------------------------- G15 to G17 the growth eigenvalue

WSQ = 243057


def wmul(x, y):
    return (x[0] * y[0] + x[1] * y[1] * WSQ, x[0] * y[1] + x[1] * y[0])


VEC = [(284, 0), (-33, 1)]
LAM = (545, 1)
LHS = [(BLK[r][0] * VEC[0][0] + BLK[r][1] * VEC[1][0], BLK[r][0] * VEC[0][1] + BLK[r][1] * VEC[1][1])
       for r in range(2)]
RHS = [wmul(LAM, VEC[0]), wmul(LAM, VEC[1])]
POSV = (33 * 33 == 1089 and 1089 < WSQ)
BR1 = (493 * 493 == 243049 and 243049 < WSQ and WSQ < 244036 and 244036 == 494 * 494)
BR2 = (88 * 88 == 7744 and 7744 < 7897 and 7897 < 7921 and 7921 == 89 * 89)
BND = max(50, 42, 10, 54, 545 - 493, 125 + 89)
DOM = (BND == 214 and BND < 1038 and 545 + 493 == 1038 and 545 + 494 == 1039)
KCERT = 284 * 1364 + 33 * 862
OVW = (862 * 862 * WSQ == 180602045508 and KCERT * KCERT == 172907935684
       and 180602045508 > 172907935684 and KCERT == 415822)

gate(LHS == RHS and POSV and VEC[0][0] == 284 and LAM == (545, 1), "G15",
     "the vector (284, w - 33) with w x w = 243057 is exact for the class block at eigenvalue 545 + w; positive since 1089 < 243057")
gate(BR1 and BR2 and DOM, "G16",
     "493^2 = 243049 < 243057 < 244036 = 494^2 and 88^2 = 7744 < 7897 < 7921 = 89^2, so 125 + sqrt 7897 < 214 < 1038 < 545 + w < 1039")
gate(OVW, "G17",
     "heavy over-weighting 862^2 x 243057 = 180602045508 > 172907935684 = 415822^2 with 415822 = 284 x 1364 + 33 x 862")

# ---------------------------------------------------------------- G18, G19 closed strips

STRIP = []
PW = [r[:] for r in TR]
for n in range(1, 7):
    if n > 1:
        PW = mmul(PW, TR)
    STRIP.append(sum(PW[i][i] for i in range(N)))
SELF = sum(1 for i in range(NS) if KEY[i][(0, 0)] == KEY[i][(0, 1)])
STGT = [2000, 1233040, 1148284352, 1167237515200, 1206389522378240, 1251135002657559808]


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


CO = [1]
for f, e in (([1, -50], 2), ([1, -42], 2), ([1, -10], 3), ([1, 54], 1),
             ([1, -1090, 53968], 1), ([1, -250, 7728], 3)):
    for _ in range(e):
        CO = pmul(CO, f)
PSUM = []
for n in range(1, 7):
    s = -n * CO[n]
    for k in range(1, n):
        s -= CO[k] * PSUM[n - k - 1]
    PSUM.append(s)

gate(STRIP == STGT and STRIP[0] == SELF and len(CO) == 17, "G18",
     "closed strip counts for n = 1 to 6: {0}".format(", ".join("{0}".format(x) for x in STRIP)))
gate(PSUM == STRIP, "G19",
     "the power-sum recurrence from the expanded characteristic polynomial reproduces all 6 strip counts, 0 misses")

# ---------------------------------------------------------------- G20 invariant factors


def invfac(M):
    A = [row[:] for row in M]
    res = []
    for s in range(N):
        while True:
            piv = None
            best = None
            for i in range(s, N):
                for j in range(s, N):
                    v = A[i][j]
                    if v != 0 and (best is None or abs(v) < best):
                        best = abs(v)
                        piv = (i, j)
            if piv is None:
                break
            i0, j0 = piv
            A[s], A[i0] = A[i0], A[s]
            for r in range(N):
                A[r][s], A[r][j0] = A[r][j0], A[r][s]
            p = A[s][s]
            done = True
            for i in range(s + 1, N):
                if A[i][s] != 0:
                    q = A[i][s] // p
                    for j in range(s, N):
                        A[i][j] -= q * A[s][j]
                    if A[i][s] != 0:
                        done = False
            for j in range(s + 1, N):
                if A[s][j] != 0:
                    q = A[s][j] // p
                    for i in range(s, N):
                        A[i][j] -= q * A[i][s]
                    if A[s][j] != 0:
                        done = False
            if done:
                bad = None
                for i in range(s + 1, N):
                    for j in range(s + 1, N):
                        if A[i][j] - (A[i][j] // p) * p != 0:
                            bad = i
                            break
                    if bad is not None:
                        break
                if bad is None:
                    break
                for j in range(s, N):
                    A[s][j] += A[bad][j]
        res.append(abs(A[s][s]))
    return res


INF = invfac(TR)
CHAIN = all(INF[i] != 0 and INF[i + 1] - (INF[i + 1] // INF[i]) * INF[i] == 0 for i in range(N - 1))
PROD = 1
for x in INF:
    PROD *= x
DET = int(fdet(TR))
EVF = 50 ** 2 * 42 ** 2 * 10 ** 3 * 54 * 53968 * 7728 ** 3
TAIL = [210, 420, 19320, 96600, 17594917200]
INFOK = (INF == [2] * 11 + TAIL and 17594917200 == 2 ** 4 * 3 ** 4 * 5 ** 2 * 7 * 23 * 3373
         and all((x & 1) == 0 for x in INF))

gate(INFOK and CHAIN and DET < 0 and PROD == -DET and PROD == EVF and PROD == 5931574826283246551040000000,
     "G20",
     "invariant factors: eleven 2s, {0} = 2^4 x 3^4 x 5^2 x 7 x 23 x 3373; det {1}".format(
         ", ".join("{0}".format(x) for x in TAIL), DET))

# ---------------------------------------------------------------- G21, G22 evenness

ALLEVEN = all((TR[x][y] & 1) == 0 for x in range(16) for y in range(16))
R0 = ((0, 1, 2, 3), 1)
RFIX = sum(1 for i in range(NS) if PERM[R0][i] == i)
RID = (PSI[R0] == tuple(range(16)))
RSW = sum(1 for i in range(NS) if KEY[PERM[R0][i]][(0, 0)] != KEY[i][(0, 1)]
          or KEY[PERM[R0][i]][(0, 1)] != KEY[i][(0, 0)])

FIB = {}
for i in range(NS):
    FIB.setdefault((KEY[i][(0, 0)], KEY[i][(0, 1)]), []).append(i)
FSET = {k: set(v) for k, v in FIB.items()}
SIZEOK = all(len(FIB.get((x, y), [])) == TR[x][y] for x in range(16) for y in range(16))
WIT = {}
AEV = {}
CRIT = 0
for kj in FIB:
    k, j = kj
    F = FIB[kj]
    S = FSET[kj]
    w = 0
    ae = 0
    for g in STAB:
        pm = PERM[g]
        held = all(pm[c] in S for c in F)
        ps = PSI[g]
        if g[1] & 1:
            pred = (ps[k] == j and ps[j] == k)
        else:
            pred = (ps[k] == k and ps[j] == j)
        if held != pred:
            CRIT += 1
        if not held:
            continue
        if all(pm[c] != c and pm[pm[c]] == c for c in F):
            w += 1
        seen = set()
        ok = True
        for c in F:
            if c in seen:
                continue
            x = c
            cyc = 0
            while True:
                seen.add(x)
                x = pm[x]
                cyc += 1
                if x == c:
                    break
            if cyc & 1:
                ok = False
                break
        if ok:
            ae += 1
    WIT[kj] = w
    AEV[kj] = ae
WCEN = dict(sorted(Counter(WIT.values()).items()))
PAIRED = sum(1 for v in WIT.values() if v > 0)
ZERO = set(kj for kj in WIT if WIT[kj] == 0)
ZENT = set(TR[k][j] for k, j in ZERO)
ORB36 = []
SEENQ = set()
for k in range(16):
    for j in range(16):
        if (k, j) in SEENQ:
            continue
        o = set()
        for g in NONSW:
            ps = PSI[g]
            o.add((ps[k], ps[j]))
        SEENQ |= o
        if len(o) == 48 and all(TR[a][b] == 36 for a, b in o):
            ORB36.append(o)
ZAEV = sum(AEV[kj] for kj in ZERO)

gate(ALLEVEN and RFIX == 0 and RID and RSW == 0 and len(FIB) == 256 and SIZEOK and CRIT == 0
     and WCEN == {0: 48, 1: 156, 2: 48, 4: 4} and PAIRED == 208, "G21",
     "all 256 entries even; the axis-zero flip fixes 0 cuttings, swaps sides; free pairings {0} on 208 fibers".format(dshow(WCEN)))
gate(len(ZERO) == 48 and ZENT == {36} and len(ORB36) == 1 and ZERO == ORB36[0] and ZAEV == 0, "G22",
     "the 48 fibers with no free pairing are exactly the entry-36 orbit, and 0 of them admit any of the 96 holding maps with even orbits")

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
emit("resource: under {0} s, under {1} MB".format(((int(time.time() - T0) // 60) + 1) * 60, ((PEAK // 250) + 1) * 250))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
