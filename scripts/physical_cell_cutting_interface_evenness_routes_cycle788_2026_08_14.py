"""Physical cell cutting: interface evenness routes, the incidence transport obstruction, boundary frames, and the exchange distance law.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, the slot-preserving subgroup of order ninety-six for axis zero, and the sixteen-letter facet alphabet. Nothing outside
that finite object enters any gate.

The target of this cycle is the evenness of the 48 stubborn interface fibers, the entry-36 orbit that the sibling cycle left as a
measurement. Five named mechanism routes are tested here and every one of them is refuted, and the structure left behind is certified:
letter membership is not a GF(2)-affine function of the piece vector; the pair stabilizer of every stubborn fiber has order two and carries
an odd cycle, so no subgroup of it pairs the fiber; the tetra-pair count matrix factors exactly as A-transpose T A, while the letter-tetra
incidence A has GF(2) rank ten and hides a six-dimensional quotient of letter functionals from the tetra alphabet; boundary frames fix the
letter single-valuedly yet fall into odd classes, inside the stubborn fibers as well as outside; used-piece columns have odd support and
tetra functionals even support; and the within-fiber exchange distance takes 19 even values with 10 and 46 absent and least value 8, while
the odd-degree counting argument fails at every distance rule except the tautological complete-graph cutoff.

Gates G1 to G16, one line each, then a resource line and the total line. Any failure exits nonzero."""

import itertools
import sys
import time
import resource
from collections import Counter
from fractions import Fraction as FRA

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


def cshow(d):
    return " ".join("{0}:{1}".format(k, d[k]) for k in sorted(d))


def lshow(v):
    return "[" + ",".join("{0}".format(x) for x in v) + "]"


def pc(x):
    return bin(x).count("1")


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
    M = [[FRA(C[r][c]) for c in range(n)] + [FRA(1 if r == c else 0) for c in range(n)] for r in range(n)]
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
CSET = [frozenset(s) for s in SOLS]
PSIZE = len(set(len(s) for s in SOLS))
CSIZE = sorted(set(len(s) for s in SOLS))[0]
NCOR = len(set(len(KEPT[t]) for t in USED))
CORNS = sorted(set(len(KEPT[t]) for t in USED))[0]

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

STAB = [(p, m) for (p, m) in G384 if p[0] == 0]
NONSW = [g for g in STAB if not (g[1] & 1)]
SWAPS = [g for g in STAB if (g[1] & 1)]
GID = ((0, 1, 2, 3), 0)


def actcorner(g, v):
    p, m = g
    x = CORN[v]
    return CIDX[tuple(x[p[i]] ^ ((m >> p[i]) & 1) for i in range(4))]


def act3(g, pt):
    p, m = g
    return tuple(pt[p[i + 1] - 1] ^ ((m >> p[i + 1]) & 1) for i in range(3))


PSI = {}
PBAD = 0
for g in STAB:
    ps = tuple(KN[frozenset(frozenset(act3(g, v) for v in tet) for tet in ALLK[li])] for li in range(16))
    if sorted(ps) != list(range(16)):
        PBAD += 1
    PSI[g] = ps

PCACHE = {}


def permof(g):
    if g not in PCACHE:
        mp = {t: KIDX[frozenset(actcorner(g, v) for v in KEPT[t])] for t in USED}
        PCACHE[g] = [SIDX[frozenset(mp[t] for t in s)] for s in SOLS]
    return PCACHE[g]


gate(len(CAND) == 2672 and FLOOR == 6 and len(KEPT) == 400 and NS == 15800 and NU == 192
     and PSIZE == 1 and CSIZE == 24 and len(G384) == 384 and len(STAB) == 96 and PBAD == 0, "G1",
     "{0} five-corner unit-determinant pieces, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, cell group {6}, slot subgroup {7}"
     .format(len(CAND), FLOOR, len(KEPT), NS, CSIZE, NU, len(G384), len(STAB)))

# ---------------------------------------------------------------- G2 the alphabet

SLOTSETS = [set(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
SAME = all(x == SLOTSETS[0] for x in SLOTSETS)
MULT = [Counter(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
MCEN = dict(sorted(Counter(MULT[0].values()).items()))
MSAME = all(m == MULT[0] for m in MULT)

MEXPR = " + ".join("{0} x {1}".format(MCEN[k], k) for k in sorted(MCEN))
MSUM = sum(k * MCEN[k] for k in MCEN)

gate(NL == 16 and SAME and len(SLOTSETS) == 8 and len(SLOTSETS[0]) == 16 and MSAME
     and MCEN == {862: 12, 1364: 4} and MSUM == NS and NS == 15800, "G2",
     "{0} letters, the same set on all {1} slots, multiplicity census {2}, and {3} = {4}"
     .format(NL, len(SLOTSETS), dshow(MCEN), MEXPR, MSUM))

# ---------------------------------------------------------------- G3 the interface matrix

TMS = []
for a in range(4):
    J = Counter((KEY[i][(a, 0)], KEY[i][(a, 1)]) for i in range(NS))
    TMS.append([[J[(x, y)] for y in range(16)] for x in range(16)])
TR = TMS[0]
AXEQ = sum(1 for a in range(4) for x in range(16) for y in range(16) if TMS[a][x][y] != TR[x][y])
SYMM = sum(1 for x in range(16) for y in range(16) if TR[x][y] != TR[y][x])
ECEN = dict(sorted(Counter(TR[x][y] for x in range(16) for y in range(16)).items()))
TRC = sum(TR[x][x] for x in range(16))
NEVEN = sum(1 for x in range(16) for y in range(16) if (TR[x][y] & 1) == 0)
N36 = sum(1 for x in range(16) for y in range(16) if TR[x][y] == 36)
NOT36 = 16 * 16 - N36

gate(AXEQ == 0 and SYMM == 0 and TRC == 2000 and NEVEN == 256 and N36 == 48 and NOT36 == 208
     and min(ECEN) == 18
     and ECEN == {18: 24, 36: 48, 50: 48, 52: 48, 90: 12, 92: 48, 100: 12, 104: 12, 200: 4}, "G3",
     "T equal on {0} axes, symmetric, trace {1}, all {2} even, {3} at 36 and {4} not; {5}"
     .format(len(TMS), TRC, NEVEN, N36, NOT36, cshow(ECEN)))

# ---------------------------------------------------------------- G4 the tetra alphabet and its producers

TALL = sorted({tet for L in ALLK for tet in L}, key=lambda f: sorted(f))
TIX = {tet: a for a, tet in enumerate(TALL)}
NT_LEN = len(TALL)
SIDE0 = set(FACE[(t, 0, 0)] for t in USED if (t, 0, 0) in FACE)
SIDE1 = set(FACE[(t, 0, 1)] for t in USED if (t, 0, 1) in FACE)

BITS = [0] * len(KEPT)
for i, s in enumerate(SOLS):
    b = 1 << i
    for t in s:
        BITS[t] |= b
COL = [BITS[t] for t in USED]
ALLONE = (1 << NS) - 1

PRODS = [[[] for _ in range(NT_LEN)], [[] for _ in range(NT_LEN)]]
for t in USED:
    for s in (0, 1):
        f = FACE.get((t, 0, s))
        if f is not None:
            PRODS[s][TIX[f]].append(t)

NT = [[0] * NT_LEN, [0] * NT_LEN]
DJ = 0
for s in (0, 1):
    for a in range(NT_LEN):
        v = 0
        tot = 0
        for t in PRODS[s][a]:
            v ^= BITS[t]
            tot += pc(BITS[t])
        NT[s][a] = v
        if pc(v) != tot:
            DJ += 1

FRM0 = []
FRM1 = []
PCEN = Counter()
OVER = 0
for s in SOLS:
    p0 = frozenset(t for t in s if (t, 0, 0) in FACE)
    p1 = frozenset(t for t in s if (t, 0, 1) in FACE)
    FRM0.append(p0)
    FRM1.append(p1)
    PCEN[(len(p0), len(p1))] += 1
    if p0 & p1:
        OVER += 1
PCEN = dict(PCEN)

gate(NT_LEN == 24 and SIDE0 == set(TALL) and SIDE1 == set(TALL) and DJ == 0 and OVER == 0
     and NCOR == 1 and CORNS == 5 and PCEN == {(6, 6): 15800}, "G4",
     "{0} tetra, same set both sides, producer supports disjoint, {1}-corner pieces give disjoint sides, census {2}"
     .format(NT_LEN, CORNS, dshow(PCEN)))

# ---------------------------------------------------------------- G5 the letter-tetra incidence

AM = [[1 if TALL[a] in ALLK[k] else 0 for a in range(NT_LEN)] for k in range(16)]
ARS = set(sum(AM[k]) for k in range(16))
ACS = set(sum(AM[k][a] for k in range(16)) for a in range(NT_LEN))

RS = sorted(ARS)[0]
CS = sorted(ACS)[0]

gate(len(AM) == 16 and NT_LEN == 24 and ARS == {6} and ACS == {4} and len(AM) * RS == NT_LEN * CS
     and len(AM) * RS == 96, "G5",
     "incidence A is {0} by {1}, every row sum {2}, every column sum {3}, and {0} x {2} = {4} = {1} x {3}"
     .format(len(AM), NT_LEN, RS, CS, len(AM) * RS))

# ---------------------------------------------------------------- G6 the transport identity

NM = [[pc(NT[0][a] & NT[1][b]) for b in range(NT_LEN)] for a in range(NT_LEN)]
MIS = 0
for a in range(NT_LEN):
    for b in range(NT_LEN):
        tot = 0
        for k in range(16):
            if AM[k][a]:
                row = TR[k]
                for j in range(16):
                    if AM[j][b]:
                        tot += row[j]
        if tot != NM[a][b]:
            MIS += 1
NCEN = dict(sorted(Counter(NM[a][b] for a in range(NT_LEN) for b in range(NT_LEN)).items()))
NEV = sum(1 for a in range(NT_LEN) for b in range(NT_LEN) if (NM[a][b] & 1) == 0)

gate(MIS == 0 and NEV == 576 and NT_LEN * NT_LEN == 576
     and NCEN == {862: 168, 872: 48, 894: 48, 904: 168, 1270: 24, 1280: 48, 1322: 48, 1332: 24}, "G6",
     "N = A-transpose T A on all {0} entries, {1} misses, all {2} even; {3}"
     .format(NT_LEN * NT_LEN, MIS, NEV, cshow(NCEN)))

# ---------------------------------------------------------------- G7 the GF(2) ranks


def badd(basis, v):
    while v:
        b = v.bit_length() - 1
        if b in basis:
            v ^= basis[b]
        else:
            basis[b] = v
            return True
    return False


def inspan(basis, v):
    while v:
        b = v.bit_length() - 1
        if b not in basis:
            return False
        v ^= basis[b]
    return True


BA = {}
for k in range(16):
    r = 0
    for a in range(NT_LEN):
        if AM[k][a]:
            r |= (1 << a)
    badd(BA, r)
RKA = len(BA)
KERA = 16 - RKA

BT = [{}, {}]
for s in (0, 1):
    for a in range(NT_LEN):
        badd(BT[s], NT[s][a])
    badd(BT[s], ALLONE)
RKT = [len(BT[0]), len(BT[1])]

BC = {}
for v in COL:
    badd(BC, v)
badd(BC, ALLONE)
RKC = len(BC)

gate(RKA == 10 and KERA == 6 and RKT == [10, 10] and RKC == 88, "G7",
     "GF(2) ranks: A has rank {0} with kernel dimension {1}; tetra span with all-ones {2} on both sides; used columns with all-ones {3}"
     .format(RKA, KERA, RKT[0], RKC))

# ---------------------------------------------------------------- G8 letter non-affinity

LET = [[0] * 16, [0] * 16]
for i in range(NS):
    b = 1 << i
    LET[0][KEY[i][(0, 0)]] |= b
    LET[1][KEY[i][(0, 1)]] |= b
AFF = []
for s in (0, 1):
    AFF.append(sum(1 for k in range(16) if inspan(BT[s], LET[s][k])))
    AFF.append(sum(1 for k in range(16) if inspan(BC, LET[s][k])))
LSUM = sum(1 for s in (0, 1) for k in range(16) if pc(LET[s][k]) == sum(TR[k]))

gate(AFF == [0, 0, 0, 0] and LSUM == 32 and NL == 16, "G8",
     "{0} of {4} letters in the tetra span and {1} of {4} in the used-column span on side 0; {2} and {3} of {4} on side 1"
     .format(AFF[0], AFF[1], AFF[2], AFF[3], NL))

# ---------------------------------------------------------------- G9, G10 the pair stabilizer

FIB = {}
for i in range(NS):
    FIB.setdefault((KEY[i][(0, 0)], KEY[i][(0, 1)]), []).append(i)
E36 = sorted(kj for kj in FIB if TR[kj[0]][kj[1]] == 36)

SCEN = Counter()
IDOK = 0
HELD = 0
ODDCYC = 0
for kj in E36:
    k, j = kj
    st = []
    for g in STAB:
        ps = PSI[g]
        if g[1] & 1:
            keep = (ps[k] == j and ps[j] == k)
        else:
            keep = (ps[k] == k and ps[j] == j)
        if keep:
            st.append(g)
    SCEN[len(st)] += 1
    if GID in st:
        IDOK += 1
    rest = [g for g in st if g != GID]
    if len(rest) != 1:
        continue
    pm = permof(rest[0])
    F = FIB[kj]
    S = set(F)
    if not all(pm[c] in S for c in F):
        continue
    HELD += 1
    seen = set()
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
            ODDCYC += 1
            break
SCEN = dict(SCEN)

gate(len(E36) == 48 and SCEN == {2: 48} and IDOK == len(E36), "G9",
     "all {0} entry-36 pairs have pair stabilizer of order two inside the {1} slot-preserving maps, census {2}"
     .format(len(E36), len(STAB), dshow(SCEN)))
gate(HELD == 48 and ODDCYC == 48 and len(E36) == 48, "G10",
     "{0} of {2} stubborn fibers held by the second stabilizer element, {1} of {2} with an odd cycle, so no subgroup pairs any"
     .format(HELD, ODDCYC, len(E36)))

# ---------------------------------------------------------------- G11 column parities

ODDCOL = sum(1 for v in COL if (pc(v) & 1))
EVT = sum(1 for s in (0, 1) for a in range(NT_LEN) if (pc(NT[s][a]) & 1) == 0)

gate(ODDCOL == 192 and EVT == 48 and NT_LEN * 2 == 48, "G11",
     "all {0} used-piece columns have odd support; {1} of {2} tetra functionals have even support, {3} tetra on each of both sides"
     .format(ODDCOL, EVT, NT_LEN * 2, NT_LEN))

# ---------------------------------------------------------------- G12, G13 boundary frames

JOINT = [(FRM0[i], FRM1[i]) for i in range(NS)]
L0 = {}
L1 = {}
LJ = {}
for i in range(NS):
    L0.setdefault(FRM0[i], set()).add(KEY[i][(0, 0)])
    L1.setdefault(FRM1[i], set()).add(KEY[i][(0, 1)])
    LJ.setdefault(JOINT[i], set()).add((KEY[i][(0, 0)], KEY[i][(0, 1)]))
BAD0 = sum(1 for v in L0.values() if len(v) > 1)
BAD1 = sum(1 for v in L1.values() if len(v) > 1)
BADJ = sum(1 for v in LJ.values() if len(v) > 1)
C0 = Counter(FRM0)
CJ = Counter(JOINT)
ODD0 = sum(1 for v in C0.values() if v & 1)
ODDJ = sum(1 for v in CJ.values() if v & 1)

WF = 0
WP = 0
for kj in E36:
    cf = Counter(JOINT[i] for i in FIB[kj])
    cp = Counter(tuple(KEY[i][(a, c)] for a in range(4) for c in (0, 1)) for i in FIB[kj])
    if any(v & 1 for v in cf.values()):
        WF += 1
    if any(v & 1 for v in cp.values()):
        WP += 1

gate(len(L0) == 1024 and len(L1) == 1024 and len(LJ) == 6184 and BAD0 == 0 and BAD1 == 0 and BADJ == 0, "G12",
     "{0} side-zero frames, {1} side-one frames, {2} joint frames; {3} frames carry two letters, {4} joint frames carry two pairs"
     .format(len(L0), len(L1), len(LJ), BAD0 + BAD1, BADJ))
gate(ODDJ == 3368 and ODD0 == 856 and len(CJ) == 6184 and len(C0) == 1024 and WF == 48 and WP == 48, "G13",
     "{0} of {1} joint classes odd, {2} of {3} side-zero odd; inside {4} and {5} of the {6} fibers frames and profiles leave an odd class"
     .format(ODDJ, len(CJ), ODD0, len(C0), WF, WP, len(E36)))

# ---------------------------------------------------------------- G14, G15, G16 the exchange distance law

DCEN = Counter()
NV = 49
ODDV = [0] * NV
ODDC = [0] * NV
REPKJ = E36[0]
REP = None
for kj in sorted(FIB):
    F = FIB[kj]
    n = len(F)
    sets = [CSET[i] for i in F]
    cnts = [Counter() for _ in range(n)]
    for x in range(n):
        sx = sets[x]
        cx = cnts[x]
        for y in range(x + 1, n):
            d = 48 - 2 * len(sx & sets[y])
            cx[d] += 1
            cnts[y][d] += 1
            DCEN[d] += 1
    pref = []
    for c in cnts:
        acc = 0
        row = []
        for v in range(NV):
            acc += c.get(v, 0)
            row.append(acc)
        pref.append(row)
    for v in range(NV):
        av = True
        ac = True
        for x in range(n):
            if not (cnts[x].get(v, 0) & 1):
                av = False
            if not (pref[x][v] & 1):
                ac = False
            if not av and not ac:
                break
        if av:
            ODDV[v] += 1
        if ac:
            ODDC[v] += 1
    if kj == REPKJ:
        REP = (F, sets, [dict(c) for c in cnts])

VALS = sorted(DCEN)
DTGT = [8, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 48]
DEV = all((v & 1) == 0 for v in VALS)
DMAX = 2 * CSIZE
MISSV = [v for v in range(min(VALS), max(VALS) + 1, 2) if v not in DCEN]
SHARE = sorted((DMAX - v) // 2 for v in MISSV)

gate(VALS == DTGT and len(VALS) == 19 and MISSV == [10, 46] and SHARE == [1, 19] and min(VALS) == 8
     and DEV and DMAX == 48, "G14",
     "{0} even values {1}; least {2}, {3} absent, d = {4} - 2t, shared {5} absent"
     .format(len(VALS), lshow(VALS), min(VALS), lshow(MISSV), DMAX, lshow(SHARE)))
gate(max(ODDV) == 0 and max(ODDC[c] for c in range(DMAX)) == 0 and ODDC[DMAX] == 256 and len(FIB) == 256, "G15",
     "all-odd degrees: {0} of {1} fibers at every value and every cutoff below {2}; at cutoff {2}, {3} of {1}, tautological complete graph"
     .format(max(ODDV), len(FIB), DMAX, ODDC[DMAX]))

RF, RSETS, RCNT = REP
RN = len(RF)
DMAT = [[0] * RN for _ in range(RN)]
for x in range(RN):
    for y in range(x + 1, RN):
        d = 48 - 2 * len(RSETS[x] & RSETS[y])
        DMAT[x][y] = d
        DMAT[y][x] = d
MINS = []
PART = []
MULTI = 0
AGREE = 0
for x in range(RN):
    best = min(DMAT[x][y] for y in range(RN) if y != x)
    MINS.append(best)
    if best == min(RCNT[x]):
        AGREE += 1
    # ties are broken by the lowest within-fiber member index, which is cover order
    ms = [y for y in range(RN) if y != x and DMAT[x][y] == best]
    PART.append(ms[0])
    if len(ms) > 1:
        MULTI += 1
NONINV = [x for x in range(RN) if PART[PART[x]] != x]
MCEN2 = dict(sorted(Counter(MINS).items()))

gate(RN == 36 and MCEN2 == {8: 36} and AGREE == RN and MULTI > 0 and len(NONINV) > 0, "G16",
     "first entry-36 fiber: least-distance census {0}, {1} members with a tied minimizer, {2} not paired back, so no involution"
     .format(dshow(MCEN2), MULTI, len(NONINV)))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
emit("resource: under {0} s, under {1} MB".format(((int(time.time() - T0) // 60) + 1) * 60, ((PEAK // 250) + 1) * 250))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
