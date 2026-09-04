"""Physical cell cutting: the label sum of a cutting is four times the positive half-set count less six, so its size is at most eight.

Standalone exact runner, standard library only. The preamble rebuilds the unit four-cube cell object from scratch, as in the sibling
cycles: the five-corner unit-determinant pieces at the adjacency cost floor, the 15800 cuttings of 24, the 192 pieces that occur in them,
the handedness label of a piece, and the 192 chambers of the twelve-wall cut of the open cell, each piece holding 8 of them and each
chamber sitting in 8 pieces. Exact integer separating planes certify that every sample-selected cover is a geometric cutting, while an
independent chamber-cover search reproduces the same 15800 cuttings. Everything else is a local statement about one piece and its 8
chambers or an exhaustive statement about this declared finite cutting family.

Put each piece in its minimal naming, start corner v0 below its opposite, so that L = sign(sigma) times chi(v0) with chi the corner weight
parity sign. Let H be the pieces whose minimal naming steps axis 3 within its first two steps: 96 pieces, 48 of label plus one and 48 of
label minus one. Two functions of a chamber alone do the work. The halving certificate g1, supported on the chambers whose order ends in
axis 3 and equal there to the order sign times the product of the three chamber signs, has per-piece sum L on a piece outside H and minus L
on a piece inside H, and total 0 over the 192 chambers; summing over a cutting gives S = 2 S_H. The W certificate, the 12 chambers whose
order carries axis 3 in the second slot with the last two slots ascending and whose second sign is plus one, has per-piece count 1 inside H
and 0 outside; summing over a cutting gives h = 12.

The size bound is then a finite obstruction. A complete enumeration, cross-checked with a second search order, finds exactly 24 families of
9 pairwise-disjoint pieces inside the positive half of H and exactly 24 inside the negative half. Each of the 48 leaves a chamber that no
member holds but whose 8 holders all meet the family, so the partition property forbids any cutting from containing it. Hence p and m, the
positive and negative half-set counts of a cutting, are each at most 8, and p + m = 12, giving S = 2 (p - m) = 4 (p - 6) with p between 4
and 8. The label sum lies in -8, -4, 0, 4, 8 pointwise, its size is at most 8, and divisibility by four follows as a corollary.

The descriptive gates cover object reconstruction, geometric tiling, chamber reconstruction, both local certificates, the five distinct
finite attacks on a nine-piece counterexample, the theorem and censuses, and two built-in discriminating perturbations. All work is exact
over the integers and rationals; no floating point enters any gate. Output ends with a resource line and the total line."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR

AUDIT_TIMEOUT_SEC = 120

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

BARY = []
for S in KEPT:
    v0 = CORN[S[0]]
    C = [[CORN[S[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]
    BARY.append((v0, inv4(C)))

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

# The generic sample makes every genuine cutting in the declared candidate
# class appear in SOLS.  The converse needs a separate certificate: every pair
# of simplices co-occurring in a sample cover is weakly separated by an exact
# nonzero normal in {-1,0,1}^4.  Full dimensionality makes the interiors
# strictly disjoint.  Twenty-four determinant-one 4-simplex volumes then sum
# to the unit four-cube volume, so every sample cover is a geometric cutting.
CO_PAIRS = sorted(set(pair for cutting in CUT
                      for pair in itertools.combinations(cutting, 2)))
SEP_NORMALS = [normal for normal in itertools.product((-1, 0, 1), repeat=4)
               if any(normal)]
VERTEX_DOTS = [[sum(CORN[v][axis] * normal[axis] for axis in range(4))
                for normal in SEP_NORMALS] for v in range(16)]
PIECE_LO = []
PIECE_HI = []
for i in range(NPI):
    vertices = KEPT[USED[i]]
    PIECE_LO.append([min(VERTEX_DOTS[v][k] for v in vertices)
                     for k in range(len(SEP_NORMALS))])
    PIECE_HI.append([max(VERTEX_DOTS[v][k] for v in vertices)
                     for k in range(len(SEP_NORMALS))])


def separated(i, j):
    return any(PIECE_HI[i][k] <= PIECE_LO[j][k]
               or PIECE_HI[j][k] <= PIECE_LO[i][k]
               for k in range(len(SEP_NORMALS)))


PAIR_SEPARATED = all(separated(i, j) for i, j in CO_PAIRS)

PC = [0] * NPI
for k, s in enumerate(CUT):
    for i in s:
        PC[i] |= (1 << k)
PCSET = sorted(set(popc(x) for x in PC))

# ------------------------------------------------------------------
# 2. the paths, their namings, and the handedness label
# ------------------------------------------------------------------


def walk(v0, sg):
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
    PBY.setdefault(tuple(sorted(walk(nm[0], nm[1]))), []).append(nm)
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

# ------------------------------------------------------------------
# 3. the chambers of the twelve-wall cut, and the incidence
# ------------------------------------------------------------------

PERMS = list(itertools.permutations(range(4)))
SGNB = dict((p, sgnp(p)) for p in PERMS)
TRIP = list(itertools.product((1, -1), repeat=3))
CHAM = [(b, s) for b in PERMS for s in TRIP]
CIDX = dict((c, k) for k, c in enumerate(CHAM))
NCH = len(CHAM)


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
        out.append((b, tuple(rho[k] * eta[b[k]] for k in range(3))))
    return out


INC = [[] for _ in range(NPI)]
HOLD = [[] for _ in range(NCH)]
DEALOK = 0
for i in range(NPI):
    v0, sg = NMOF[i][0]
    seen = sorted(set(CIDX[(b, s)] for (b, s) in deal(v0, sg)))
    if len(seen) == 8:
        DEALOK += 1
    INC[i] = seen
    for cid in seen:
        HOLD[cid].append(i)

HOLDN = sorted(set(len(x) for x in HOLD))
INCN = sorted(set(len(x) for x in INC))

CHM = [0] * NPI
for i in range(NPI):
    m = 0
    for c in INC[i]:
        m |= (1 << c)
    CHM[i] = m

# Reconstruct the cutting family from chamber incidence alone, independently
# of the shifted sample masks used above.  Minimum-remaining-value branching
# is only a speed choice; every compatible holder of the selected uncovered
# chamber is explored.
CHCUT = []


def chamber_cover_search(cov, chosen):
    if cov == (1 << NCH) - 1:
        CHCUT.append(tuple(sorted(chosen)))
        return
    free = ((1 << NCH) - 1) & (~cov)
    options = None
    while free:
        low = free & (-free)
        cid = low.bit_length() - 1
        free ^= low
        compatible = [i for i in HOLD[cid] if CHM[i] & cov == 0]
        if not compatible:
            return
        if options is None or len(compatible) < len(options):
            options = compatible
            if len(options) == 1:
                break
    for i in options:
        chosen.append(i)
        chamber_cover_search(cov | CHM[i], chosen)
        chosen.pop()


chamber_cover_search(0, [])
CHCUT_SET = set(CHCUT)
CUT_SET = set(CUT)
CHAMBER_RECONSTRUCTION_OK = (
    len(CHCUT) == len(CHCUT_SET) == NS and CHCUT_SET == CUT_SET
)

# ------------------------------------------------------------------
# 4. the partition property, re-verified on every cutting
# ------------------------------------------------------------------

FULL = (1 << NCH) - 1
BADP = 0
for s in CUT:
    u = 0
    tot = 0
    for i in s:
        u |= CHM[i]
        tot += popc(CHM[i])
    if not (len(s) == 24 and tot == NCH and u == FULL):
        BADP += 1

# ------------------------------------------------------------------
# 5. the minimal naming, the label form, and the half set
# ------------------------------------------------------------------

DIAG = [0] * NPI
SIG = [None] * NPI
E1 = [0] * NPI
for i in range(NPI):
    v0a, sga = NMOF[i][1]
    if v0a < (v0a ^ 15):
        v0, sg = v0a, sga
    else:
        v0, sg = v0a ^ 15, tuple(reversed(sga))
    DIAG[i] = v0
    SIG[i] = sg
    E1[i] = sgnp(sg)

CHI = [1 - 2 * (popc(w) & 1) for w in range(16)]
BADL = sum(1 for i in range(NPI) if LABP[i] != E1[i] * CHI[DIAG[i]])
DIAGSET = sorted(set(DIAG))

HIND = [1 if 3 in (SIG[i][0], SIG[i][1]) else 0 for i in range(NPI)]
HALF = [i for i in range(NPI) if HIND[i]]
HP = [i for i in HALF if LABP[i] == 1]
HM = [i for i in HALF if LABP[i] == -1]
HPS = set(HP)
HMS = set(HM)

# ------------------------------------------------------------------
# 6. the two chamber certificates, in closed form
# ------------------------------------------------------------------


def g1_of(cid):
    b, s = CHAM[cid]
    if b[3] != 3:
        return 0
    return SGNB[b] * s[0] * s[1] * s[2]


G1 = [g1_of(c) for c in range(NCH)]
G1CEN = {}
for v in G1:
    bump(G1CEN, v)
G1TOT = sum(G1)

TARG = [LABP[i] - 2 * LABP[i] * HIND[i] for i in range(NPI)]
BADG1 = sum(1 for i in range(NPI) if sum(G1[c] for c in INC[i]) != TARG[i])

WSET = set(c for c in range(NCH)
           if CHAM[c][0][1] == 3 and CHAM[c][0][2] < CHAM[c][0][3] and CHAM[c][1][1] == 1)
BADW = sum(1 for i in range(NPI) if sum(1 for c in INC[i] if c in WSET) != HIND[i])
WIN = sum(1 for i in HALF if sum(1 for c in INC[i] if c in WSET) == 1)
WOUT = sum(1 for i in range(NPI) if not HIND[i] and not [c for c in INC[i] if c in WSET])

# ------------------------------------------------------------------
# 7. the per-cutting arithmetic
# ------------------------------------------------------------------

BADHALV = 0
BADH = 0
BADTH = 0
PCEN = {}
SCEN = {}
for s in CUT:
    sv = 0
    sh = 0
    h = 0
    p = 0
    m = 0
    for i in s:
        sv += LABP[i]
        if HIND[i]:
            h += 1
            sh += LABP[i]
            if i in HPS:
                p += 1
            else:
                m += 1
    if sv != 2 * sh:
        BADHALV += 1
    if h != 12:
        BADH += 1
    if not (p + m == 12 and sv == 4 * (p - 6) and 4 <= p <= 8):
        BADTH += 1
    bump(PCEN, p)
    bump(SCEN, sv)

CHAMBER_BOUND_FAILURES = 0
for s in CHCUT:
    p = sum(1 for i in s if i in HPS)
    m = sum(1 for i in s if i in HMS)
    if p > 8 or m > 8:
        CHAMBER_BOUND_FAILURES += 1

# ------------------------------------------------------------------
# 8. the nine-piece families inside each half, twice over
# ------------------------------------------------------------------


def enum_a(verts):
    """extension in index order over the disjointness graph"""
    n = len(verts)
    adj = [0] * n
    for a in range(n):
        for b in range(a + 1, n):
            if CHM[verts[a]] & CHM[verts[b]] == 0:
                adj[a] |= (1 << b)
                adj[b] |= (1 << a)
    out = []

    def go(cand, cur):
        if len(cur) == 9:
            out.append(tuple(verts[v] for v in cur))
            return
        if len(cur) + popc(cand) < 9:
            return
        c = cand
        while c:
            v = (c & (-c)).bit_length() - 1
            c &= c - 1
            go(cand & adj[v] & ~((1 << (v + 1)) - 1), cur + [v])
            cand &= ~(1 << v)
            if len(cur) + popc(cand) < 9:
                return

    go((1 << n) - 1, [])
    return set(out)


def enum_b(verts):
    """take it or leave it walk down the list, carrying the union of chambers used"""
    n = len(verts)
    out = []

    def go(idx, cur, used):
        if len(cur) == 9:
            out.append(tuple(cur))
            return
        if len(cur) + (n - idx) < 9 or idx == n:
            return
        v = verts[idx]
        if CHM[v] & used == 0:
            go(idx + 1, cur + [v], used | CHM[v])
        go(idx + 1, cur, used)

    go(0, [], 0)
    return set(out)


FAMPA = enum_a(HP)
FAMPB = enum_b(HP)
FAMMA = enum_a(HM)
FAMMB = enum_b(HM)
AGREE = (FAMPA == FAMPB) and (FAMMA == FAMMB)
FAMS = sorted(FAMPA) + sorted(FAMMA)
NFAM = len(FAMS)

CUT_BITS = [sum(1 << i for i in cutting) for cutting in CUT]
FAMILY_BITS = [sum(1 << i for i in family) for family in FAMS]
FAMILIES_CONTAINED = sum(
    1 for family in FAMILY_BITS if any(cutting & family == family for cutting in CUT_BITS)
)


def seeded_completion_exists(family):
    cov = 0
    for i in family:
        if cov & CHM[i]:
            return False
        cov |= CHM[i]

    def go(used):
        if used == FULL:
            return True
        free = FULL & (~used)
        options = None
        while free:
            low = free & (-free)
            cid = low.bit_length() - 1
            free ^= low
            compatible = [i for i in HOLD[cid] if CHM[i] & used == 0]
            if not compatible:
                return False
            if options is None or len(compatible) < len(options):
                options = compatible
                if len(options) == 1:
                    break
        return any(go(used | CHM[i]) for i in options)

    return go(cov)


COMPLETABLE_FAMILIES = sum(1 for family in FAMS if seeded_completion_exists(family))


def seal_witness(F):
    cov = 0
    for i in F:
        cov |= CHM[i]
    for c in range(NCH):
        if (cov >> c) & 1:
            continue
        if all(CHM[q] & cov for q in HOLD[c]):
            return c
    return -1


UNSEALED = sum(1 for F in FAMS if seal_witness(F) < 0)

# ------------------------------------------------------------------
# 9. the two discriminating perturbations
# ------------------------------------------------------------------

CFLIP = min(c for c in range(NCH) if G1[c] != 0)
G1X = list(G1)
G1X[CFLIP] = -G1X[CFLIP]
PERTP = sum(1 for i in range(NPI) if sum(G1X[c] for c in INC[i]) != TARG[i])
NHOLD = len(HOLD[CFLIP])

PDROP = HALF[0]
HINDX = list(HIND)
HINDX[PDROP] = 0
PERTC = 0
for s in CUT:
    if sum(HINDX[i] for i in s) != 12:
        PERTC += 1
NTHRU = popc(PC[PDROP])

# ------------------------------------------------------------------
# 10. gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800 and SIZES == [24]
     and NPI == 192 and PCSET == [1975] and len(NAMES) == 384 and NPER == [2] and GENERIC, "object_rebuild",
     "{0} unit pieces, floor {1}, {2} kept, {3} cuttings of {4}, {5} used pieces in {6} each, {7} namings, {8} per piece"
     .format(nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NS), nd(SIZES[0]), nd(NPI), nd(PCSET[0]), nd(len(NAMES)), nd(NPER[0])))

gate(len(CO_PAIRS) == 15168 and len(SEP_NORMALS) == 80 and PAIR_SEPARATED, "geometric_tiling",
     "all {0} co-occurring simplex pairs have an exact separator among {1} ternary normals; {2} unit volumes fill the cell"
     .format(nd(len(CO_PAIRS)), nd(len(SEP_NORMALS)), nd(24)))

gate(BADP == 0 and HOLDN == [8] and INCN == [8] and DEALOK == NPI and NCH == 192, "chamber_partition",
     "each of {0} cutting pieces holds {1} of {2} chambers, each chamber has {1} holders, failures {3} of {4}"
     .format(nd(SIZES[0]), nd(INCN[0]), nd(NCH), nd(BADP), nd(NS)))

gate(BADL == 0 and DIAGSET == list(range(8)), "minimal_naming",
     "minimal naming: L = sign of the axis order times the corner weight parity sign, over {0} start corners, mismatches {1} of {2}"
     .format(nd(len(DIAGSET)), nd(BADL), nd(NPI)))

gate(len(HALF) == 96 and len(HP) == 48 and len(HM) == 48, "half_set",
     "half set: the pieces whose minimal naming steps axis {0} within its first {1} steps number {2}, label split {3} and {3}"
     .format(nd(3), nd(2), nd(len(HALF)), nd(len(HP))))

gate(BADG1 == 0 and G1TOT == 0 and cens(G1CEN) == "-1:24 0:144 1:24", "halving_certificate",
     "halving certificate on chambers: value census {0}, per-piece identity failures {1} of {2}, chamber total {3}"
     .format(cens(G1CEN), nd(BADG1), nd(NPI), nd(G1TOT)))

gate(BADHALV == 0, "halving_identity",
     "halving identity: the label sum S equals {0} times the half-set label sum S_H, failures {1} of {2}"
     .format(nd(2), nd(BADHALV), nd(NS)))

gate(BADW == 0 and len(WSET) == 12 and WIN == len(HALF) and WOUT == NPI - len(HALF), "witness_set",
     "W: {0} chambers, exactly {1} in each of {2} half-set pieces and {3} in each other piece,"
     " failures {4} of {5}"
     .format(nd(len(WSET)), nd(1), nd(len(HALF)), nd(0), nd(BADW), nd(NPI)))

gate(BADH == 0, "constant_twelve",
     "the constant twelve: every cutting holds exactly {0} half-set pieces, failures {1} of {2}"
     .format(nd(12), nd(BADH), nd(NS)))

gate(CHAMBER_RECONSTRUCTION_OK and CHAMBER_BOUND_FAILURES == 0, "chamber_reconstruction",
     "chamber-only search returns the same {0} cuttings; same-sign half-set bound failures {1}"
     .format(nd(len(CHCUT_SET)), nd(CHAMBER_BOUND_FAILURES)))

gate(AGREE and len(FAMPA) == 24 and len(FAMMA) == 24, "nine_family_census",
     "families of {0} disjoint pieces: {1} positive, {2} negative; graph and union searches agree: {3}"
     .format(nd(9), nd(len(FAMPA)), nd(len(FAMMA)), "yes" if AGREE else "no"))

gate(FAMILIES_CONTAINED == 0 and NFAM == 48, "direct_noncontainment",
     "direct set containment finds {0} of the {1} nine-piece families inside any enumerated cutting"
     .format(nd(FAMILIES_CONTAINED), nd(NFAM)))

gate(COMPLETABLE_FAMILIES == 0 and NFAM == 48, "seeded_completion",
     "chamber exact-cover searches seeded by all {0} nine-piece families find {1} completions"
     .format(nd(NFAM), nd(COMPLETABLE_FAMILIES)))

gate(UNSEALED == 0 and NFAM == 48, "sealing_witnesses",
     "sealing: each of the {0} families leaves a chamber it does not hold whose {1} holders all meet it, failures {2} of {0}"
     .format(nd(NFAM), nd(8), nd(UNSEALED)))

gate(BADTH == 0, "size_bound_identity",
     "theorem: S = {0} (p - {1}) at the positive half-set count p, with p + m = {2} and p between {3} and {4}, failures {5} of {6}"
     .format(nd(4), nd(6), nd(12), nd(4), nd(8), nd(BADTH), nd(NS)))

gate(cens(PCEN) == "4:120 5:2832 6:9896 7:2832 8:120" and cens(SCEN) == "-8:120 -4:2832 0:9896 4:2832 8:120"
     and sum(PCEN.values()) == NS, "endpoint_censuses",
     "p census {0} sum {1}; label sum census {2}"
     .format(cens(PCEN), nd(NS), cens(SCEN)))

gate(PERTP == 8 and PERTP == NHOLD, "halving_mutation",
     "control one: negating the halving certificate at one chamber breaks the per-piece identity at exactly {0} pieces, its holders"
     .format(nd(PERTP)))

gate(PERTC == 1975 and PERTC == NTHRU, "half_set_mutation",
     "control two: dropping one piece from the half set breaks the constant {0} at exactly {1} cuttings, the cuttings through it"
     .format(nd(12), nd(PERTC)))

emit("per_element: checked - all 192 piece incidences, labels, g1 sums, and W counts are executed exactly")
emit("per_site: checked and not executed - the one-cell theorem has no framework site variable or sitewise extension")
emit("per_mode: checked and not executed - the finite incidence theorem defines no mode decomposition or modal extension")
emit("per_block: checked - all 15800 declared cell cuttings are scanned and each same-sign half-set count is at most 8")
emit("lattice_wide: checked and not executed - no multi-cell or lattice-wide statement is made or tested by this runner")

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit("resource: under {0} s of the {1} s budget, under {2} MB of the {3} MB budget, {4} gate characters"
     .format(nd(((SECS // 60) + 1) * 60), nd(AUDIT_TIMEOUT_SEC),
             nd(((PEAK // 250) + 1) * 250), nd(2500), nd(OUT[0])))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
raise SystemExit(1 if STAT[1] else 0)
