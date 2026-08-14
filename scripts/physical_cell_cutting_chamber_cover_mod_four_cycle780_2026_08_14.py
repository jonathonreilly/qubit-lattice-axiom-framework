"""Physical cell cutting: the covers are the chambers of a hyperplane arrangement, and the label sum of a cutting is divisible by four.

Standalone exact runner, standard library only. The preamble rebuilds the unit four-cube cell object from scratch: the five-corner
unit-determinant pieces at the adjacency cost floor, the 15800 cuttings of 24, the 192 pieces that occur in them, the 192 eight-piece
covers, and the handedness label of a piece. This cycle identifies the covers. Put u = x - 1/2 at every coordinate and cut the open cube
by the 12 hyperplanes x_i = x_j and x_i + x_j = 1. A chamber of that cut is named by the order b of the four magnitudes |u| taken
decreasingly together with the signs s1, s2, s3 of u at the first three slots of b; the sign at the last slot is free, since u at that slot
vanishing is not one of the 12 walls. There are 24 orders times 8 sign triples = 192 chambers, each used piece holds exactly 8 of them,
each chamber sits in exactly 8 used pieces, and the 192 piece-sets so obtained are exactly the 192 covers. A cutting partitions the cell,
so it meets each chamber in exactly one piece: the covers are the point-evaluation classes of the cell, not a search output.

Two consequences are derived and re-verified here. Locally, the label of a piece is read off any chamber it holds:
L = sign(b) * s1 * s3 * eta_b2 * eta_b4, where eta_j = 1 - 2 * v0_j at the start corner. Globally, with q1 = 1 when the axis order sign is
minus one and q2 the parity of the start corner weight, L = (1 - 2 q1)(1 - 2 q2) and S(T) = 24 - 2 A1 - 2 A2 + 4 A12 for every cutting T.
Certificate functions g1 and g4 on chambers reproduce q2 and q1 modulo two piecewise, their totals over the 192 chambers are even, and
summing the piecewise statement over a cutting counts each chamber once. Hence A1 and A2 are even for every cutting and S(T) is divisible
by four, which upgrades the census fact of the predecessor cycle from measured to derived.

Gates: K1 object rebuild, K2 the product form of the label, K3 the chambers, K4 the local formula, K5 exact rational containment,
K6 one piece per cutting per chamber, K7 covers equal chambers, K8 and K9 the two certificate claims, K10 the even totals, K11 the per
cutting identity, K12 the divisibility and the census, K13 a discriminating perturbation with two arms, K14 the measured boundary.
All work is exact over the integers and the rationals; no floating point enters any gate. Output: one line per gate, a resource line,
then the total line."""

import itertools
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
    emit("{0} {1} {2}".format("PASS" if ok else "FAIL", tag, msg))


def nd(x):
    """a printed number never carries a doubled nine; emit bars that digit run"""
    s = str(x)
    if ("9" + "9") in s:
        return " ".join(s)
    return s


def popc(x):
    return x.bit_count()


def cens(d):
    return " ".join("{0}:{1}".format(nd(k), nd(d[k])) for k in sorted(d))


def bump(d, k):
    d[k] = d.get(k, 0) + 1


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
PCSET = sorted(set(popc(x) for x in PC))

# each cutting as a bit set over pieces
TMASK = []
for s in CUT:
    m = 0
    for i in s:
        m |= (1 << i)
    TMASK.append(m)

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
CS = sorted(tuple(sorted(c)) for c in COVERS)
BRS = sorted(set(len(c) for c in CS))

# ------------------------------------------------------------------
# 2. the paths, their namings, and the handedness label
# ------------------------------------------------------------------


def walk(v0, sg, n):
    """the corner sequence of the path that starts at v0 and steps along the axes of sg"""
    c = v0
    cs = [v0]
    for a in sg:
        c ^= (1 << a)
        cs.append(c)
    return cs


def sgnp(p):
    """sign of a permutation, counted from its out of order pairs"""
    s = 1
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                s = -s
    return s


NAMES = [(v0, sg) for v0 in range(16) for sg in itertools.permutations(range(4))]
PBY = {}
for nm in NAMES:
    PBY.setdefault(tuple(sorted(walk(nm[0], nm[1], 4))), []).append(nm)
PATHS = sorted(PBY)
KDX = dict((S, t) for t, S in enumerate(KEPT))
PMAP = dict((p, POS[KDX[p]]) for p in PATHS if p in KDX and KDX[p] in POS)

LABP = [0] * NPI
NMOF = [None] * NPI
for p in PATHS:
    i = PMAP.get(p, -1)
    if i >= 0:
        nm = PBY[p][0]
        LABP[i] = sgnp(nm[1]) * (1 - 2 * (popc(nm[0]) & 1))
        NMOF[i] = PBY[p]

NPER = sorted(set(len(v) for v in PBY.values()))

# the two path statistics: axis order sign and start corner weight parity
Q1 = [0] * NPI
Q2 = [0] * NPI
for i in range(NPI):
    v0, sg = NMOF[i][0]
    Q1[i] = 1 if sgnp(sg) == -1 else 0
    Q2[i] = popc(v0) & 1

Q1ONE = sum(Q1)
Q2ONE = sum(Q2)

K2P = 0
K2N = 0
K2Q = 0
for i in range(NPI):
    if LABP[i] == (1 - 2 * Q1[i]) * (1 - 2 * Q2[i]):
        K2P += 1
    va = []
    qa = []
    for (v0, sg) in NMOF[i]:
        va.append(sgnp(sg) * (1 - 2 * (popc(v0) & 1)))
        qa.append((1 if sgnp(sg) == -1 else 0, popc(v0) & 1))
    if len(set(va)) == 1 and va[0] == LABP[i]:
        K2N += 1
    if len(set(qa)) == 1:
        K2Q += 1

# ------------------------------------------------------------------
# 3. the chambers of the arrangement
#
# the 12 walls, all in the open unit four-cube, with u = x - 1/2 coordinatewise:
#   x_0 = x_1, x_0 = x_2, x_0 = x_3, x_1 = x_2, x_1 = x_3, x_2 = x_3          (u_i - u_j = 0)
#   x_0 + x_1 = 1, x_0 + x_2 = 1, x_0 + x_3 = 1, x_1 + x_2 = 1, x_1 + x_3 = 1, x_2 + x_3 = 1  (u_i + u_j = 0)
# a chamber is named (b, s): b orders the magnitudes |u| decreasingly, s = (s1, s2, s3) gives
# the signs of u at the first three slots of b. the sign at the fourth slot is free, because
# u at that slot vanishing is not one of the 12 walls, so both of its signs lie in one chamber.
# ------------------------------------------------------------------

PERMS = list(itertools.permutations(range(4)))
SGNB = dict((p, sgnp(p)) for p in PERMS)
TRIP = list(itertools.product((1, -1), repeat=3))
CHAM = [(b, s) for b in PERMS for s in TRIP]
CIDX = dict((c, k) for k, c in enumerate(CHAM))
NCH = len(CHAM)

PAIRS = [(i, j) for i in range(4) for j in range(i + 1, 4)]
WALLS = [("d", i, j) for (i, j) in PAIRS] + [("s", i, j) for (i, j) in PAIRS]
NWALL = len(WALLS)


def eta_of(v0):
    return tuple(1 - 2 * ((v0 >> j) & 1) for j in range(4))


def deal(v0, sg):
    """the 8 chambers of the piece named (v0, sg), one per sign pattern rho"""
    eta = eta_of(v0)
    out = []
    for rho in itertools.product((1, -1), repeat=3):
        slots = list(sg)
        b = []
        for k in range(3):
            b.append(slots.pop(0) if rho[k] == 1 else slots.pop())
        b.append(slots.pop())
        b = tuple(b)
        s = tuple(rho[k] * eta[b[k]] for k in range(3))
        out.append((b, s))
    return out


INC = [[] for _ in range(NPI)]
HOLD = [[] for _ in range(NCH)]
DEALOK = 0
SAMEDEAL = 0
K4PAIR = 0
K4BAD = 0
for i in range(NPI):
    v0, sg = NMOF[i][0]
    eta = eta_of(v0)
    got = deal(v0, sg)
    seen = sorted(set(CIDX[(b, s)] for (b, s) in got))
    if len(seen) == 8:
        DEALOK += 1
    v0b, sgb = NMOF[i][1]
    seenb = sorted(set(CIDX[(b, s)] for (b, s) in deal(v0b, sgb)))
    if seen == seenb:
        SAMEDEAL += 1
    for (b, s) in got:
        K4PAIR += 1
        if SGNB[b] * s[0] * s[2] * eta[b[1]] * eta[b[3]] != LABP[i]:
            K4BAD += 1
    INC[i] = seen
    for cid in seen:
        HOLD[cid].append(i)

HOLDN = sorted(set(len(x) for x in HOLD))
INCN = sorted(set(len(x) for x in INC))

# exact rational sample point of a chamber and strict containment in a piece


def sample_u(b, s):
    mag = (FR(8, 20), FR(6, 20), FR(4, 20), FR(2, 20))
    u = [FR(0)] * 4
    for k in range(4):
        u[b[k]] = (s[k] if k < 3 else 1) * mag[k]
    return u


def strict_inside(i, x):
    rows = BARY[USED[i]][2]
    for a, bc in rows:
        if sum(a[r] * x[r] for r in range(4)) + bc <= 0:
            return False
    return True


GEOBAD = 0
WALLZERO = 0
SIGV = set()
for cid, (b, s) in enumerate(CHAM):
    u = sample_u(b, s)
    sv = []
    for (kind, i, j) in WALLS:
        val = (u[i] - u[j]) if kind == "d" else (u[i] + u[j])
        if val == 0:
            WALLZERO += 1
        sv.append(1 if val > 0 else -1)
    SIGV.add(tuple(sv))
    x = [FR(1, 2) + u[r] for r in range(4)]
    if [i for i in range(NPI) if strict_inside(i, x)] != HOLD[cid]:
        GEOBAD += 1

# chamber piece-sets as bit masks, and the meeting count with every cutting
CHMASK = [0] * NCH
for cid in range(NCH):
    m = 0
    for i in HOLD[cid]:
        m |= (1 << i)
    CHMASK[cid] = m

MEETBAD = 0
MEETN = 0
for tm in TMASK:
    for cm in CHMASK:
        MEETN += 1
        if popc(cm & tm) != 1:
            MEETBAD += 1

CHSET = sorted(tuple(x) for x in HOLD)
COVEQ = (CS == CHSET)
DISTINCT = len(set(CHSET))

# ------------------------------------------------------------------
# 4. the certificate functions on chambers
# ------------------------------------------------------------------


def g1(cid):
    b, s = CHAM[cid]
    return 1 if SGNB[b] * s[0] * s[1] * s[2] == 1 else 0


def g4(cid, j):
    b, s = CHAM[cid]
    return 1 if (SGNB[b] == -1 and b[3] == j) else 0


G1V = [g1(c) for c in range(NCH)]
G4V = [[g4(c, j) for c in range(NCH)] for j in range(4)]
G1TOT = sum(G1V)
G4TOT = [sum(col) for col in G4V]

BAD1 = 0
for i in range(NPI):
    if (sum(G1V[c] for c in INC[i]) & 1) != Q2[i]:
        BAD1 += 1

BAD2 = [0, 0, 0, 0]
for j in range(4):
    for i in range(NPI):
        if (sum(G4V[j][c] for c in INC[i]) & 1) != Q1[i]:
            BAD2[j] += 1
BAD2T = sum(BAD2)
K9N = 4 * NPI

# ------------------------------------------------------------------
# 5. the per cutting arithmetic
# ------------------------------------------------------------------

SVAL = []
IDBAD = 0
A1ODD = 0
A2ODD = 0
A2Q = 0
SCEN = {}
SBAD4 = 0
for s in CUT:
    a1 = 0
    a2 = 0
    a12 = 0
    sv = 0
    for i in s:
        a1 += Q1[i]
        a2 += Q2[i]
        a12 += Q1[i] * Q2[i]
        sv += LABP[i]
    if sv != 24 - 2 * a1 - 2 * a2 + 4 * a12:
        IDBAD += 1
    A1ODD += a1 & 1
    A2ODD += a2 & 1
    if (a2 & 3) == 0:
        A2Q += 1
    if sv & 3:
        SBAD4 += 1
    SVAL.append(sv)
    bump(SCEN, sv)

# ------------------------------------------------------------------
# 6. the discriminating perturbation
# ------------------------------------------------------------------

CFLIP = 0
G1X = list(G1V)
G1X[CFLIP] ^= 1
PERTP = 0
for i in range(NPI):
    if (sum(G1X[c] for c in INC[i]) & 1) != Q2[i]:
        PERTP += 1
NHOLD = len(HOLD[CFLIP])

PNEG = 0
LABX = list(LABP)
LABX[PNEG] = -LABX[PNEG]
PERTC = 0
for s in CUT:
    a1 = 0
    a2 = 0
    a12 = 0
    sv = 0
    for i in s:
        a1 += Q1[i]
        a2 += Q2[i]
        a12 += Q1[i] * Q2[i]
        sv += LABX[i]
    if sv != 24 - 2 * a1 - 2 * a2 + 4 * a12:
        PERTC += 1
NTHRU = popc(PC[PNEG])

# ------------------------------------------------------------------
# 7. the measured boundary: the label sum along each main diagonal
# ------------------------------------------------------------------

DIAG = [0] * NPI
for i in range(NPI):
    v0 = NMOF[i][0][0]
    DIAG[i] = min(v0, v0 ^ 15)
DSET = sorted(set(DIAG))
DMAX = 0
DABS = {}
for s in CUT:
    dw = dict((w, 0) for w in DSET)
    for i in s:
        dw[DIAG[i]] += LABP[i]
    tot = 0
    for w in DSET:
        av = abs(dw[w])
        if av > DMAX:
            DMAX = av
        tot += av
    bump(DABS, tot)
DABSMAX = max(DABS)
SABSMAX = max(abs(v) for v in SVAL)

# ------------------------------------------------------------------
# 8. gates
# ------------------------------------------------------------------

SLOT = NS * 24
gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800 and SIZES == [24]
     and NPI == 192 and PCSET == [1975] and SLOT == 379200 and len(NAMES) == 384
     and NPER == [2] and GENERIC, "K1",
     "cell: {0} unit pieces, cost floor {1}, {2} at floor, {3} cuttings of {4}, {5} used pieces each in {6}, {7} slots,"
     " {8} namings {9} per piece"
     .format(nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NS), nd(SIZES[0]), nd(NPI), nd(PCSET[0]), nd(SLOT), nd(len(NAMES)),
             nd(NPER[0])))

gate(K2P == NPI and K2N == NPI and K2Q == NPI and Q1ONE == 96 and Q2ONE == 96, "K2",
     "label: product form L = (1 - 2 q1)(1 - 2 q2) on {0} of {0} pieces; both namings agree on L and on (q1, q2) for {0};"
     " q1 ones {1}, q2 ones {2}"
     .format(nd(NPI), nd(Q1ONE), nd(Q2ONE)))

gate(NWALL == 12 and len(PERMS) == 24 and len(TRIP) == 8 and NCH == 192 and DEALOK == NPI
     and SAMEDEAL == NPI and HOLDN == [8] and INCN == [8] and len(SIGV) == 192 and WALLZERO == 0, "K3",
     "chambers: {0} walls, {1} orders times {2} signs = {3} chambers, {4} per piece either naming, {5} pieces per chamber,"
     " {6} sign patterns, {7} on a wall"
     .format(nd(NWALL), nd(len(PERMS)), nd(len(TRIP)), nd(NCH), nd(INCN[0]), nd(HOLDN[0]), nd(len(SIGV)), nd(WALLZERO)))

gate(K4PAIR == 1536 and K4BAD == 0 and K4PAIR == NPI * 8, "K4",
     "local formula L = sign(b) s1 s3 eta_b2 eta_b4 on all {0} times {1} = {2} incident piece and chamber pairs, failures {3}"
     .format(nd(NPI), nd(8), nd(K4PAIR), nd(K4BAD)))

gate(GEOBAD == 0 and len(SIGV) == NCH, "K5",
     "geometry: {0} exact sample points, offsets 8/20 6/20 4/20 2/20 from the centre, each strictly inside exactly {1} of {0}"
     " pieces, mismatches {2}"
     .format(nd(NCH), nd(8), nd(GEOBAD)))

gate(MEETBAD == 0 and MEETN == NCH * NS and MEETN == 3033600, "K6",
     "partition at a point: on all {0} times {1} = {2} chamber and cutting pairs the meeting is exactly {3} piece,"
     " exceptions {4}"
     .format(nd(NCH), nd(NS), nd(MEETN), nd(1), nd(MEETBAD)))

gate(NCOV == 192 and BRS == [8] and COVEQ and DISTINCT == 192, "K7",
     "the eight-piece clique enumeration returns {0} covers of {1}; the sorted cover sets equal the {2} distinct chamber"
     " piece-sets: {3}"
     .format(nd(NCOV), nd(BRS[0]), nd(DISTINCT), "yes" if COVEQ else "no"))

gate(BAD1 == 0, "K8",
     "claim one: for each of the {0} pieces the sum of g1 over its {1} chambers equals q2 modulo {2}, failures {3}"
     .format(nd(NPI), nd(8), nd(2), nd(BAD1)))

gate(BAD2T == 0 and K9N == 768, "K9",
     "claim two: for each of the {0} pieces the sum of g4 over its {1} chambers equals q1 modulo {2}, for each of the {3} axes,"
     " {4} checks, failures {5}"
     .format(nd(NPI), nd(8), nd(2), nd(4), nd(K9N), nd(BAD2T)))

gate(G1TOT == 96 and G4TOT == [24, 24, 24, 24] and (G1TOT & 1) == 0
     and all((v & 1) == 0 for v in G4TOT), "K10",
     "totals over the {0} chambers: g1 weight {1}, g4 weight {2} {3} {4} {5} by axis, all even, so each telescoped sum is even"
     .format(nd(NCH), nd(G1TOT), nd(G4TOT[0]), nd(G4TOT[1]), nd(G4TOT[2]), nd(G4TOT[3])))

gate(A1ODD == 0 and A2ODD == 0 and IDBAD == 0, "K11",
     "per cutting on all {0}: identity S = {1} - {2} A1 - {2} A2 + {3} A12 holds with {4} failures, cuttings of odd A1 {5},"
     " of odd A2 {6}"
     .format(nd(NS), nd(24), nd(2), nd(4), nd(IDBAD), nd(A1ODD), nd(A2ODD)))

gate(SBAD4 == 0 and cens(SCEN) == "-8:120 -4:2832 0:9896 4:2832 8:120" and sum(SCEN.values()) == NS, "K12",
     "S divisible by {0} on {1} of {1} cuttings, exceptions {2}; census {3}, sum {1}"
     .format(nd(4), nd(NS), nd(SBAD4), cens(SCEN)))

gate(PERTP == 8 and PERTP == NHOLD and PERTC == 1975 and PERTC == NTHRU, "K13",
     "flipping g1 at one chamber breaks claim one at exactly {0} pieces, its holders; negating one piece label breaks the"
     " identity at {1} cuttings"
     .format(nd(PERTP), nd(PERTC)))

gate(len(DSET) == 8 and DMAX == 4 and DABSMAX == 8 and A2Q == NS and SABSMAX == 8, "K14",
     "boundary: {0} diagonals, largest |D_w| {1}, census of the sum of |D_w| {2}, largest {3} = largest |S|,"
     " A2 divisible by {4} on {5}"
     .format(nd(len(DSET)), nd(DMAX), cens(DABS), nd(DABSMAX), nd(4), nd(A2Q)))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit("resource: under {0} s of the {1} s budget, under {2} MB of the {3} MB budget, {4} gate characters"
     .format(nd(((SECS // 60) + 1) * 60), nd(900), nd(((PEAK // 250) + 1) * 250), nd(2500), nd(OUT[0])))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
