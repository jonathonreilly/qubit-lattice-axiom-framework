"""Physical cell cutting: the label sum of a cutting is four times the positive half-set count less six, so its size is at most eight.

Standalone exact runner, standard library only. The preamble rebuilds the unit four-cube cell object from scratch, as in the sibling
cycles: the five-corner unit-determinant pieces at the adjacency cost floor, the 15800 cuttings of 24, the 192 pieces that occur in them,
the handedness label of a piece, and the 192 chambers of the twelve-wall cut of the open cell, each piece holding 8 of them and each
chamber sitting in 8 pieces. The predecessor cycle showed that a cutting meets every chamber in exactly one piece; that partition property
is re-verified here and is the only global input used below. Everything else is a local statement about one piece and its 8 chambers.

Put each piece in its minimal naming, start corner v0 below its opposite, so that L = sign(sigma) times chi(v0) with chi the corner weight
parity sign. Let H be the pieces whose minimal naming steps axis 3 within its first two steps: 96 pieces, 48 of label plus one and 48 of
label minus one. Two functions of a chamber alone do the work. The halving certificate g1, supported on the chambers whose order ends in
axis 3 and equal there to the order sign times the product of the three chamber signs, has per-piece sum L on a piece outside H and minus L
on a piece inside H, and total 0 over the 192 chambers; summing over a cutting gives S = 2 S_H. The W certificate, the 12 chambers whose
order carries axis 3 in the second slot with the last two slots ascending and whose second sign is plus one, has per-piece count 1 inside H
and 0 outside; summing over a cutting gives h = 12.

The size bound is then a finite obstruction. A complete enumeration, run twice with different search orders, finds exactly 24 families of
9 pairwise-disjoint pieces inside the positive half of H and exactly 24 inside the negative half. Each of the 48 leaves a chamber that no
member holds but whose 8 holders all meet the family, so the partition property forbids any cutting from containing it. Hence p and m, the
positive and negative half-set counts of a cutting, are each at most 8, and p + m = 12, giving S = 2 (p - m) = 4 (p - 6) with p between 4
and 8. The label sum lies in -8, -4, 0, 4, 8 pointwise, its size is at most 8, and divisibility by four follows as a corollary.

Gates: K1 object rebuild, K2 the partition property, K3 the minimal-naming label form, K4 the half set, K5 the halving certificate,
K6 the halving identity, K7 the W certificate, K8 the constant twelve, K9 the family enumeration, K10 the sealing obstruction, K11 the
theorem, K12 the two censuses, K13 and K14 two discriminating perturbations. All work is exact over the integers and the rationals; no
floating point enters any gate. Output: one line per gate, a resource line, then the total line."""

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
     and NPI == 192 and PCSET == [1975] and len(NAMES) == 384 and NPER == [2] and GENERIC, "K1",
     "cell: {0} unit pieces, cost floor {1}, {2} at floor, {3} cuttings of {4}, {5} used pieces each in {6}, {7} namings {8} per piece"
     .format(nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NS), nd(SIZES[0]), nd(NPI), nd(PCSET[0]), nd(len(NAMES)), nd(NPER[0])))

gate(BADP == 0 and HOLDN == [8] and INCN == [8] and DEALOK == NPI and NCH == 192, "K2",
     "partition: each of the {0} pieces of a cutting holds {1} of the {2} chambers, each chamber sits in {1} pieces, failures {3} of {4}"
     .format(nd(SIZES[0]), nd(INCN[0]), nd(NCH), nd(BADP), nd(NS)))

gate(BADL == 0 and DIAGSET == list(range(8)), "K3",
     "minimal naming: L = sign of the axis order times the corner weight parity sign, over {0} start corners, mismatches {1} of {2}"
     .format(nd(len(DIAGSET)), nd(BADL), nd(NPI)))

gate(len(HALF) == 96 and len(HP) == 48 and len(HM) == 48, "K4",
     "half set: the pieces whose minimal naming steps axis {0} within its first {1} steps number {2}, label split {3} and {3}"
     .format(nd(3), nd(2), nd(len(HALF)), nd(len(HP))))

gate(BADG1 == 0 and G1TOT == 0 and cens(G1CEN) == "-1:24 0:144 1:24", "K5",
     "halving certificate on chambers: value census {0}, per-piece identity failures {1} of {2}, chamber total {3}"
     .format(cens(G1CEN), nd(BADG1), nd(NPI), nd(G1TOT)))

gate(BADHALV == 0, "K6",
     "halving identity: the label sum S equals {0} times the half-set label sum S_H, failures {1} of {2}"
     .format(nd(2), nd(BADHALV), nd(NS)))

gate(BADW == 0 and len(WSET) == 12 and WIN == len(HALF) and WOUT == NPI - len(HALF), "K7",
     "W certificate: {0} chambers, exactly {1} inside each of the {2} half-set pieces and {3} inside each of the other {2},"
     " failures {4} of {5}"
     .format(nd(len(WSET)), nd(1), nd(len(HALF)), nd(0), nd(BADW), nd(NPI)))

gate(BADH == 0, "K8",
     "the constant twelve: every cutting holds exactly {0} half-set pieces, failures {1} of {2}"
     .format(nd(12), nd(BADH), nd(NS)))

gate(AGREE and len(FAMPA) == 24 and len(FAMMA) == 24, "K9",
     "families of {0} pairwise-disjoint pieces: {1} inside the positive half, {2} inside the negative half, two search orders agree: {3}"
     .format(nd(9), nd(len(FAMPA)), nd(len(FAMMA)), "yes" if AGREE else "no"))

gate(UNSEALED == 0 and NFAM == 48, "K10",
     "sealing: each of the {0} families leaves a chamber it does not hold whose {1} holders all meet it, failures {2} of {0}"
     .format(nd(NFAM), nd(8), nd(UNSEALED)))

gate(BADTH == 0, "K11",
     "theorem: S = {0} (p - {1}) at the positive half-set count p, with p + m = {2} and p between {3} and {4}, failures {5} of {6}"
     .format(nd(4), nd(6), nd(12), nd(4), nd(8), nd(BADTH), nd(NS)))

gate(cens(PCEN) == "4:120 5:2832 6:9896 7:2832 8:120" and cens(SCEN) == "-8:120 -4:2832 0:9896 4:2832 8:120"
     and sum(PCEN.values()) == NS, "K12",
     "p census {0} sum {1}; label sum census {2}"
     .format(cens(PCEN), nd(NS), cens(SCEN)))

gate(PERTP == 8 and PERTP == NHOLD, "K13",
     "control one: negating the halving certificate at one chamber breaks the per-piece identity at exactly {0} pieces, its holders"
     .format(nd(PERTP)))

gate(PERTC == 1975 and PERTC == NTHRU, "K14",
     "control two: dropping one piece from the half set breaks the constant {0} at exactly {1} cuttings, the cuttings through it"
     .format(nd(12), nd(PERTC)))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit("resource: under {0} s of the {1} s budget, under {2} MB of the {3} MB budget, {4} gate characters"
     .format(nd(((SECS // 60) + 1) * 60), nd(900), nd(((PEAK // 250) + 1) * 250), nd(2500), nd(OUT[0])))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
