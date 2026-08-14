"""Physical cell cutting: the odd-diagonal count of a cutting is divisible by four.

Standalone exact runner, standard library only. The preamble rebuilds the unit four-cube cell object from scratch, as in the sibling
cycles: the five-corner unit-determinant pieces at the adjacency cost floor, the 15800 cuttings of 24 pieces, the 192 pieces that occur
in them, and the 192 chambers of the twelve-wall cut of the open cell, each piece holding 8 of them and each chamber sitting in 8 pieces.
A cutting meets every chamber in exactly one piece; that partition property is re-verified here and is the only global input used below.

Put each piece in its minimal naming, start corner v0 below its opposite, and call v0 the diagonal label of the piece. The quantity
studied is A2(T), the number of pieces of a cutting whose diagonal label has odd weight. The chain has three local ingredients and one
telescoping step. A sign class Y_w, one for each of the eight labels, holds 24 chambers; the count of Y_w inside a single piece is
1, 4, 4, 6 or 0 according to the mismatch pattern between the piece label and w, which gives, after telescoping over a cutting, the
identity n_w = 24 - 4 a_w - 4 c_w - 6 q_w and hence n_w congruent to 2 q_w modulo 4. The pieces carrying the six-valued entry at w are
exactly the half-set pieces whose transported label phi equals w, and phi preserves the weight parity of the label, so the sum of n_w
over the four odd labels is twice the number of odd-diagonal half-set pieces of the cutting, modulo 4. Finally a function of a chamber
alone, supported on 20 chambers, has per-piece count congruent to the odd-diagonal half-set indicator modulo 2; telescoping it gives an
even count of such pieces on every cutting, and the divisibility by four follows.

Gates: K1 object rebuild and the partition property, K2 the sign classes, K3 the local law, K4 the telescoping identity, K5 the q class
in closed form, K6 the parity transport, K7 the certificate shape, K8 the certificate law, K9 the evenness, K10 the theorem, K11 and K12
two discriminating perturbations, K13 naming invariance, K14 the coupling. All work is exact over the integers and the rationals; no
floating point enters any gate. Output: one line per gate, two census lines, the total line, then a resource line."""

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

# ------------------------------------------------------------------
# 2. the paths and their two namings
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

NMOF = [None] * NPI
for p in PATHS:
    i = PMAP.get(p, -1)
    if i >= 0:
        NMOF[i] = PBY[p]

NPER = sorted(set(len(v) for v in PBY.values()))

# ------------------------------------------------------------------
# 3. the chambers of the twelve-wall cut, and the incidence
# ------------------------------------------------------------------

PERMS = list(itertools.permutations(range(4)))
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
# 5. the minimal naming, the diagonal label, the half set, the odd part
# ------------------------------------------------------------------

DIAG = [0] * NPI
SIG = [None] * NPI
for i in range(NPI):
    v0a, sga = NMOF[i][0]
    if v0a < (v0a ^ 15):
        v0, sg = v0a, sga
    else:
        v0, sg = v0a ^ 15, tuple(reversed(sga))
    DIAG[i] = v0
    SIG[i] = sg

DIAGSET = sorted(set(DIAG))
HIND = [1 if 3 in (SIG[i][0], SIG[i][1]) else 0 for i in range(NPI)]
HALF = [i for i in range(NPI) if HIND[i]]
HODD = [1 if (HIND[i] and (popc(DIAG[i]) & 1)) else 0 for i in range(NPI)]
NHODD = sum(HODD)

# ------------------------------------------------------------------
# 6. the sign classes and the local law
# ------------------------------------------------------------------

ETA = [tuple(1 - 2 * ((w >> j) & 1) for j in range(4)) for w in range(8)]

YM = [0] * 8
YSZ = [0] * 8
for w in range(8):
    m = 0
    for c in range(NCH):
        b, s = CHAM[c]
        if all(s[k] == ETA[w][b[k]] for k in range(3)):
            m |= (1 << c)
    YM[w] = m
    YSZ[w] = popc(m)

BADYS = sum(1 for w in range(8) if YSZ[w] != 24)

CLS = [[4] * 8 for _ in range(NPI)]
CNT = [[0] * 8 for _ in range(NPI)]
BADLAW = 0
BADFOUR = 0
PCEN = {}
for i in range(NPI):
    v = DIAG[i]
    sg = SIG[i]
    for w in range(8):
        cnt = popc(YM[w] & CHM[i])
        CNT[i][w] = cnt
        if w == v:
            kc = 0
            exp = 1
        else:
            neg = tuple(k for k in range(4) if ETA[v][sg[k]] * ETA[w][sg[k]] == -1)
            if neg == (3,):
                kc = 1
                exp = 4
            elif neg == (1, 2, 3):
                kc = 2
                exp = 4
            elif neg == (2, 3):
                kc = 3
                exp = 6
            else:
                kc = 4
                exp = 0
        CLS[i][w] = kc
        bump(PCEN, kc)
        if cnt != exp:
            BADLAW += 1
        if cnt != (4 if exp == 6 else exp):
            BADFOUR += 1

NPAIR = 8 * NPI
PCOK = (PCEN.get(0, 0) == 192 and PCEN.get(1, 0) == 144 and PCEN.get(2, 0) == 48
        and PCEN.get(3, 0) == 96 and PCEN.get(4, 0) == 1056)
PSUM = (PCEN.get(0, 0) * 1 + (PCEN.get(1, 0) + PCEN.get(2, 0)) * 4 + PCEN.get(3, 0) * 6)

# ------------------------------------------------------------------
# 7. the q class in closed form, and the parity transport
# ------------------------------------------------------------------

E4 = [1, 2, 4, 8]
PHI = [0] * NPI
for i in range(NPI):
    x = DIAG[i] ^ E4[SIG[i][2]] ^ E4[SIG[i][3]]
    PHI[i] = min(x, x ^ 15)

BADQ = 0
for i in range(NPI):
    for w in range(8):
        if (CLS[i][w] == 3) != (HIND[i] == 1 and PHI[i] == w):
            BADQ += 1

FIB = {}
for i in HALF:
    bump(FIB, PHI[i])
FIBOK = (sorted(FIB) == list(range(8)) and sorted(set(FIB.values())) == [12])

BADTR = sum(1 for i in HALF if (popc(PHI[i]) & 1) != (popc(DIAG[i]) & 1))

# ------------------------------------------------------------------
# 8. the parity certificate on chambers, in closed form
# ------------------------------------------------------------------


def cl1(b, s):
    return b[1] == 3 and s[1] == 1 and b[2] < b[3] and s[0] * s[2] == -1


def cl2(b, s):
    return b[1] == 3 and s[1] == 1 and b[2] > b[3] and s[2] == 1


def cl3(b, s):
    return b[0] == 3 and s[0] == 1 and b[1] < b[2] < b[3] and s[1] * s[2] == 1


def cl4(b, s):
    return b[0] == 3 and s[0] == 1 and b[1] < b[2] and b[3] < b[2] and s[1] == -1


def cl5(b, s):
    return b[0] == 3 and s[0] == 1 and b[1] > b[2] > b[3] and s[2] == 1


CLAUSE = [cl1, cl2, cl3, cl4, cl5]
CELL = []
for f in CLAUSE:
    CELL.append(sorted(c for c in range(NCH) if f(CHAM[c][0], CHAM[c][1])))
CSZ = [len(x) for x in CELL]
DISJ = True
for a in range(len(CELL)):
    for b in range(a + 1, len(CELL)):
        if set(CELL[a]) & set(CELL[b]):
            DISJ = False

G3 = sorted(set(c for cell in CELL for c in cell))
G3M = 0
for c in G3:
    G3M |= (1 << c)
NG3 = len(G3)

BADCERT = sum(1 for i in range(NPI) if (popc(G3M & CHM[i]) & 1) != HODD[i])

# ------------------------------------------------------------------
# 9. the per-cutting arithmetic, by a packed count over the eight labels
# ------------------------------------------------------------------

PACK = [0] * NPI
for i in range(NPI):
    v = 0
    for w in range(8):
        kc = CLS[i][w]
        if kc == 0:
            v += 1 << (8 * w)
        elif kc == 1:
            v += 1 << (8 * (8 + w))
        elif kc == 2:
            v += 1 << (8 * (16 + w))
        elif kc == 3:
            v += 1 << (8 * (24 + w))
    if popc(DIAG[i]) & 1:
        v += 1 << (8 * 32)
    if HODD[i]:
        v += 1 << (8 * 33)
    PACK[i] = v

ODDW = (1, 2, 4, 7)
BADTEL = 0
BADEVEN = 0
BADA2 = 0
BADCOUP = 0
HCEN = {}
ACEN = {}
for s in CUT:
    tot = 0
    for i in s:
        tot += PACK[i]
    n = [(tot >> (8 * w)) & 255 for w in range(8)]
    a = [(tot >> (8 * (8 + w))) & 255 for w in range(8)]
    cc = [(tot >> (8 * (16 + w))) & 255 for w in range(8)]
    q = [(tot >> (8 * (24 + w))) & 255 for w in range(8)]
    a2d = (tot >> (8 * 32)) & 255
    h = (tot >> (8 * 33)) & 255
    for w in range(8):
        if n[w] != 24 - 4 * a[w] - 4 * cc[w] - 6 * q[w]:
            BADTEL += 1
    a2s = sum(n[w] for w in ODDW)
    if h & 1:
        BADEVEN += 1
    if not (a2s == a2d and (a2d - 2 * h) & 3 == 0 and a2d & 3 == 0):
        BADA2 += 1
    if sum(q[w] for w in ODDW) != h:
        BADCOUP += 1
    bump(HCEN, h)
    bump(ACEN, a2d)

HCENS = cens(HCEN)
ACENS = cens(ACEN)
HTGT = "0:472 2:1848 4:3384 6:4392 8:3384 10:1848 12:472"
ATGT = "0:112 4:1176 8:3936 12:5352 16:3936 20:1176 24:112"

# ------------------------------------------------------------------
# 10. the two discriminating perturbations
# ------------------------------------------------------------------

CDROP = CELL[0][0]
G3X = G3M & ~(1 << CDROP)
PBAD = [i for i in range(NPI) if (popc(G3X & CHM[i]) & 1) != HODD[i]]
PMATCH = (sorted(PBAD) == sorted(HOLD[CDROP]))

# ------------------------------------------------------------------
# 11. naming invariance from the second naming
# ------------------------------------------------------------------

BADNM = 0
for i in range(NPI):
    v0b = DIAG[i] ^ 15
    sgb = tuple(reversed(SIG[i]))
    if (v0b, sgb) not in NMOF[i]:
        BADNM += 1
        continue
    if v0b < (v0b ^ 15):
        u0, ug = v0b, sgb
    else:
        u0, ug = v0b ^ 15, tuple(reversed(sgb))
    hi = 1 if 3 in (ug[0], ug[1]) else 0
    ho = 1 if (hi and (popc(u0) & 1)) else 0
    if u0 != DIAG[i] or hi != HIND[i] or ho != HODD[i]:
        BADNM += 1

# ------------------------------------------------------------------
# 12. gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800 and SIZES == [24] and NPI == 192
     and NCH == 192 and INCN == [8] and HOLDN == [8] and DEALOK == NPI and BADP == 0 and GENERIC
     and NPER == [2] and DIAGSET == list(range(8)), "K1",
     "object: {0} pieces, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, {6} chambers, {7} per piece, {7} holders, {8} bad"
     .format(nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NS), nd(SIZES[0]), nd(NPI), nd(NCH), nd(INCN[0]), nd(BADP)))

gate(BADYS == 0 and sorted(set(YSZ)) == [24], "K2",
     "sign classes: each of the {0} label classes Y_w holds {1} of the {2} chambers, size failures {3} of {0}"
     .format(nd(8), nd(YSZ[0]), nd(NCH), nd(BADYS)))

gate(BADLAW == 0 and PCOK and PSUM == NPAIR and NPAIR == 1536, "K3",
     "local law {0} / {1} / {1} / {2} / {3} by mismatch pattern, failures {4} of {5}; classes {6} self, {7} and {8} at {1}, {9} at {2},"
     " {10} at {3}, total {5}"
     .format(nd(1), nd(4), nd(6), nd(0), nd(BADLAW), nd(NPAIR), nd(PCEN[0]), nd(PCEN[1]), nd(PCEN[2]), nd(PCEN[3]), nd(PCEN[4])))

gate(BADTEL == 0, "K4",
     "telescoping: n_w = {0} - {1} a_w - {1} c_w - {2} q_w on every cutting at every label, failures {3} of {4}"
     .format(nd(24), nd(4), nd(6), nd(BADTEL), nd(NS * 8)))

gate(BADQ == 0 and FIBOK, "K5",
     "q class: the {0}-valued pattern holds exactly at the half-set pieces with phi = w, failures {1} of {2}; {3} fibres of phi of size {4}"
     .format(nd(6), nd(BADQ), nd(NPAIR), nd(8), nd(12)))

gate(BADTR == 0 and len(HALF) == 96, "K6",
     "parity transport: on the half set, axis {0} within the first {1} steps, the weight parity of phi equals that of the label,"
     " failures {2} of {3}"
     .format(nd(3), nd(2), nd(BADTR), nd(len(HALF))))

gate(DISJ and CSZ == [6, 6, 2, 4, 2] and NG3 == 20 and (NG3 & 1) == 0, "K7",
     "certificate shape: the five clause cells are pairwise disjoint of sizes {0}, total {1} chambers, even parity {2}"
     .format(", ".join(nd(x) for x in CSZ), nd(NG3), "yes" if (NG3 & 1) == 0 else "no"))

gate(BADCERT == 0 and NHODD == 48, "K8",
     "certificate law: the parity of the certificate count on a piece equals its odd-diagonal half-set value, failures {0} of {1},"
     " support {2}"
     .format(nd(BADCERT), nd(NPI), nd(NHODD)))

gate(BADEVEN == 0 and HCENS == HTGT and sum(HCEN.values()) == NS, "K9",
     "evenness: every cutting holds an even number of odd-diagonal half-set pieces, failures {0} of {1}"
     .format(nd(BADEVEN), nd(NS)))

gate(BADA2 == 0 and ACENS == ATGT and sum(ACEN.values()) == NS, "K10",
     "theorem: A2 sums n_w over the odd labels {0}, {1}, {2}, {3}, and modulo {4} it is {5} times the odd count and is {6}, failures"
     " {7} of {8}"
     .format(nd(1), nd(2), nd(4), nd(7), nd(4), nd(2), nd(0), nd(BADA2), nd(NS)))

gate(len(PBAD) == 8 and PMATCH, "K11",
     "control one: dropping {0} chamber from the certificate breaks the piece parity at exactly {1} pieces, its holders, match {2}"
     .format(nd(1), nd(len(PBAD)), "yes" if PMATCH else "no"))

gate(BADFOUR == 96 and BADFOUR == PCEN[3], "K12",
     "control two: replacing the {0} of the local law by {1} breaks the rule at exactly {2} pairs, the q class, of the {3}"
     .format(nd(6), nd(4), nd(BADFOUR), nd(NPAIR)))

gate(BADNM == 0 and NPER == [2] and len(NAMES) == 384, "K13",
     "naming invariance: the second of the {0} namings, {1} per piece, by complement and reversal, gives the same {2} odd values,"
     " failures {3}"
     .format(nd(len(NAMES)), nd(NPER[0]), nd(NPI), nd(BADNM)))

gate(BADCOUP == 0, "K14",
     "coupling: the sum of q_w over the four odd labels equals the odd-diagonal half-set count of the cutting, failures {0} of {1}"
     .format(nd(BADCOUP), nd(NS)))

emit("census: odd-diagonal half-set count over the {0} cuttings {1}, sum {0}".format(nd(NS), HCENS))
emit("census: A2 over the {0} cuttings {1}, sum {0}".format(nd(NS), ACENS))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit("resource: under {0} s of the {1} s budget, under {2} MB of the {3} MB budget, {4} characters"
     .format(nd(((SECS // 60) + 1) * 60), nd(900), nd(((PEAK // 250) + 1) * 250), nd(2500), nd(OUT[0])))
