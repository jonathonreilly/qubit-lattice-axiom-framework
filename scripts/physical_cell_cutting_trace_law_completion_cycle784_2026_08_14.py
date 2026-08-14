"""Physical cell cutting: the label sum is an affine function of a single family trace.

Standalone exact runner, standard library only. The preamble rebuilds the unit four-cube cell object from scratch, as in the sibling
cycles: the five-corner unit-determinant pieces at the adjacency cost floor, the 15800 cuttings by 24 pieces, the 192 pieces that occur in
them, and the 192 chambers of the twelve cut walls, each piece holding 8 of them and each chamber sitting in 8 pieces. A cutting meets
every chamber in exactly one piece; that partition property is re-verified here and is the only global input used below.

Put each piece in its minimal naming, start corner below its opposite, and give it the label L(P), the sign of the naming order times the
sign of the corner weight. The label sum S(T) over the 24 pieces of a cutting takes the five values 0, plus or minus 4, plus or minus 8.
The position of a piece is read straight off the chamber incidence, as the set of axis orders of its 8 chambers. The family H holds the
pieces whose minimal naming uses the last axis within the first two steps of the walk. This runner measures that H meets every cutting in
exactly 12 pieces and that S(T) = 4 (p - 6), with p the size of the trace inside the positive half H+, so the label sum is an affine
function of one family trace. The mirror g0, the reflection of the first axis alone, is a sign-minus element of the order-384 symmetry
group of the cell; it preserves H, exchanges the two halves and negates every label, which forces the p layer and the 12 - p layer of the
trace layer to agree. The completion counts N(A) are then measured over the distinct traces, the extreme cuttings are shown to be
determined by their traces, and the per-class constancy that a product factorization over the trace layer would need is refuted by an
explicit witness pair.

Gates: K1 the object, K2 the labels and the census, K3 the positions, K4 the family, K5 the constant trace, K6 the affine law, K7 the
corollaries, K8 the p census, K9 the mirror, K10 the trace layer, K11 the per-p layers, K12 the extremes, K13 the refutation, K14 a
single-swap rejector on the family. All work is exact over the integers and the rationals; no floating point enters any gate. Output: one
line per gate, a few data lines, the total line, then a resource line."""

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
    if len(txt) > 148:
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
# 2. the walks and their two namings
# ------------------------------------------------------------------


def walk(v0, sg):
    """the corner sequence of the walk that starts at v0 and steps along the axes of sg"""
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
NMISS = sum(1 for x in NMOF if x is None)

# ------------------------------------------------------------------
# 3. the chambers of the twelve cut walls, and the incidence
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
# 5. the minimal naming and the label
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

LAB = [sgnp(SIG[i]) * (1 - 2 * (popc(DIAG[i]) & 1)) for i in range(NPI)]
LABOK = sorted(set(LAB)) == [-1, 1]

SOF = []
SCEN = {}
for s in CUT:
    v = 0
    for i in s:
        v += LAB[i]
    SOF.append(v)
    bump(SCEN, v)

SCENS = cens(SCEN)
STGT = "-8:120 -4:2832 0:9896 4:2832 8:120"

# ------------------------------------------------------------------
# 6. the positions, straight off the chamber incidence
# ------------------------------------------------------------------

PSET = [frozenset(CHAM[c][0] for c in INC[i]) for i in range(NPI)]
PLIST = sorted(set(PSET), key=lambda z: sorted(z))
PIDX = dict((z, k) for k, z in enumerate(PLIST))
PID = [PIDX[PSET[i]] for i in range(NPI)]

PCT = {}
for i in range(NPI):
    bump(PCT, PID[i])
ORDCT = {}
for z in PLIST:
    for b in z:
        bump(ORDCT, b)

PSZ = sorted(set(len(z) for z in PLIST))
POSOK = (len(PLIST) == 12 and PSZ == [8] and sorted(set(PCT.values())) == [16]
         and len(PCT) == 12 and len(ORDCT) == 24 and sorted(set(ORDCT.values())) == [4])

# ------------------------------------------------------------------
# 7. the family H, its halves, and its spread over the positions
# ------------------------------------------------------------------

HIND = [1 if 3 in (SIG[i][0], SIG[i][1]) else 0 for i in range(NPI)]
HFAM = [i for i in range(NPI) if HIND[i]]
HPL = [i for i in HFAM if LAB[i] == 1]
HMI = [i for i in HFAM if LAB[i] == -1]
HSET = set(HFAM)
HPSET = set(HPL)

HCT = {}
HPCT = {}
for i in HFAM:
    bump(HCT, PID[i])
for i in HPL:
    bump(HPCT, PID[i])

FAMOK = (len(HFAM) == 96 and len(HPL) == 48 and len(HMI) == 48
         and len(HCT) == 12 and sorted(set(HCT.values())) == [8]
         and len(HPCT) == 12 and sorted(set(HPCT.values())) == [4])

HFX = dict((p, k) for k, p in enumerate(HFAM))
NH = len(HFAM)

# ------------------------------------------------------------------
# 8. the trace of a cutting, the constant size, the affine law
# ------------------------------------------------------------------

BADSZ = 0
BADLAW = 0
BADCOR = 0
TRM = []
TRP = []
PCEN = {}
for si in range(NS):
    s = CUT[si]
    m = 0
    n = 0
    p = 0
    npos = 0
    for i in s:
        if LAB[i] == 1:
            npos += 1
        k = HFX.get(i, -1)
        if k >= 0:
            m |= (1 << k)
            n += 1
            if i in HPSET:
                p += 1
    if n != 12:
        BADSZ += 1
    if SOF[si] != 4 * (p - 6):
        BADLAW += 1
    if npos != 2 * p or p < 4 or p > 8 or ((abs(SOF[si]) == 8) != (p == 4 or p == 8)):
        BADCOR += 1
    TRM.append(m)
    TRP.append(p)
    bump(PCEN, p)

PCENS = cens(PCEN)
PTGT = "4:120 5:2832 6:9896 7:2832 8:120"
PRANGE = sorted(PCEN) == [4, 5, 6, 7, 8]

# ------------------------------------------------------------------
# 9. the symmetry group of the cell, acting through the namings
# ------------------------------------------------------------------

NM2PI = {}
for i in range(NPI):
    for nm in NMOF[i]:
        NM2PI[nm] = i


def permbits(v, pi):
    o = 0
    for j in range(4):
        if (v >> j) & 1:
            o |= (1 << pi[j])
    return o


def act(pi, f):
    """the piece map of the cell symmetry with axis order pi and axis flips f, by naming transport"""
    out = [0] * NPI
    for i in range(NPI):
        v0, sg = NMOF[i][0]
        key = (permbits(v0, pi) ^ f, tuple(pi[a] for a in sg))
        if key not in NM2PI:
            return None
        out[i] = NM2PI[key]
    return out


G0 = act((0, 1, 2, 3), 1)
G0OK = G0 is not None and len(set(G0)) == NPI
G0H = G0OK and set(G0[i] for i in HFAM) == HSET
G0S = G0OK and set(G0[i] for i in HPL) == set(HMI) and set(G0[i] for i in HMI) == HPSET
BADNEG = sum(1 for i in range(NPI) if LAB[G0[i]] != -LAB[i]) if G0OK else NPI

NMINUS = 0
NSWAP = 0
for pi in PERMS:
    for f in range(16):
        sgn = sgnp(pi) * (1 - 2 * (popc(f) & 1))
        if sgn != -1:
            continue
        NMINUS += 1
        mp = act(pi, f)
        if mp is None:
            continue
        if set(mp[i] for i in HFAM) == HSET and set(mp[i] for i in HPL) == set(HMI):
            NSWAP += 1

# ------------------------------------------------------------------
# 10. the trace layer and its completion counts
# ------------------------------------------------------------------

NAC = {}
PAC = {}
for si in range(NS):
    bump(NAC, TRM[si])
    PAC[TRM[si]] = TRP[si]

NTR = len(NAC)
NHIST = {}
for m in NAC:
    bump(NHIST, NAC[m])
NHS = cens(NHIST)
NHTGT = "1:2688 2:1536 3:816 4:384 5:96 7:168 8:96 9:48 10:320"
NWSUM = sum(k * NHIST[k] for k in NHIST)
NCSUM = sum(NHIST[k] for k in NHIST)

GH = [HFX[G0[HFAM[k]]] for k in range(NH)] if G0OK else list(range(NH))
BADMIR = 0
BADMP = 0
for m in NAC:
    mm = 0
    mv = m
    while mv:
        low = mv & (-mv)
        mm |= (1 << GH[low.bit_length() - 1])
        mv ^= low
    if mm not in NAC or NAC[mm] != NAC[m]:
        BADMIR += 1
    elif PAC[mm] != 12 - PAC[m]:
        BADMP += 1

LAY = {}
for m in NAC:
    LAY.setdefault(PAC[m], {})
    bump(LAY[PAC[m]], NAC[m])

LCT = dict((p, sum(LAY[p].values())) for p in LAY)
LCTS = cens(LCT)
LCTGT = "4:120 5:1488 6:2936 7:1488 8:120"
PURE = sorted(LAY.get(4, {})) == [1] and sorted(LAY.get(8, {})) == [1]
MIRLAY = LAY.get(5, {}) == LAY.get(7, {})
SIXSET = sorted(LAY.get(6, {}))
L57 = cens(LAY.get(5, {}))
L6 = cens(LAY.get(6, {}))
L57TGT = "1:816 2:480 3:72 5:48 8:48 9:24"
L6TGT = "1:816 2:576 3:672 4:384 7:168 10:320"

# ------------------------------------------------------------------
# 11. the extremes, and the refutation of a product factorization
# ------------------------------------------------------------------

EXI = [si for si in range(NS) if abs(SOF[si]) == 8]
EXU = sum(1 for si in EXI if NAC[TRM[si]] == 1)
EXTR = set(TRM[si] for si in EXI)
EXP48 = set(m for m in NAC if PAC[m] == 4 or PAC[m] == 8)
EXOK = len(EXI) == 240 and EXU == len(EXI) and EXTR == EXP48 and len(EXTR) == 240

NVAL = dict((p, len(LAY[p])) for p in LAY)
NOTCONST = [p for p in (5, 6, 7) if NVAL.get(p, 0) > 1]
W1 = sorted(m for m in NAC if PAC[m] == 6 and NAC[m] == 1)
W10 = sorted(m for m in NAC if PAC[m] == 6 and NAC[m] == 10)


def famlist(m):
    return " ".join(nd(k) for k in range(NH) if (m >> k) & 1)


# ------------------------------------------------------------------
# 12. the rejector: one swap in the family
# ------------------------------------------------------------------

MIN_IN = min(HFAM)
MIN_OUT = min(i for i in range(NPI) if not HIND[i])
RSET = (HSET - set([MIN_IN])) | set([MIN_OUT])
RPSET = set(i for i in RSET if LAB[i] == 1)
RBADSZ = 0
RBADLAW = 0
for si in range(NS):
    n = 0
    p = 0
    for i in CUT[si]:
        if i in RSET:
            n += 1
            if i in RPSET:
                p += 1
    if n != 12:
        RBADSZ += 1
    if SOF[si] != 4 * (p - 6):
        RBADLAW += 1

# ------------------------------------------------------------------
# 13. gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800 and SIZES == [24] and NPI == 192
     and NCH == 192 and INCN == [8] and HOLDN == [8] and DEALOK == NPI and BADP == 0 and GENERIC
     and NPER == [2] and NMISS == 0 and len(NAMES) == 384, "K1",
     "object: {0} candidates, floor {1}, {2} kept, {3} points, {4} cuttings by {5}, {6} pieces, {7} chambers, incidence {8} and {8}, bad {9}"
     .format(nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NPTS), nd(NS), nd(SIZES[0]), nd(NPI), nd(NCH), nd(INCN[0]), nd(BADP)))

emit("namings: {0} walks from the {1} corners, {2} per piece, and the minimal naming starts at the corner below its opposite"
     .format(nd(len(NAMES)), nd(len(CORN)), nd(NPER[0])))

gate(LABOK and SCENS == STGT and sum(SCEN.values()) == NS, "K2",
     "labels: naming sign times corner weight sign; label sum census {0}, total {1}"
     .format(SCENS, nd(NS)))

gate(POSOK, "K3",
     "positions from the incidence: {0} distinct, {1} axis orders each, {2} pieces each, every one of the {3} axis orders in exactly {4}"
     .format(nd(len(PLIST)), nd(PSZ[0]), nd(sorted(PCT.values())[0]), nd(len(ORDCT)), nd(sorted(ORDCT.values())[0])))

gate(FAMOK, "K4",
     "family: {0} pieces use the last axis within the first {1} steps, halves {2} and {2}, every position meets H in {3} and H+ in {4}"
     .format(nd(len(HFAM)), nd(2), nd(len(HPL)), nd(sorted(HCT.values())[0]), nd(sorted(HPCT.values())[0])))

gate(BADSZ == 0, "K5",
     "constant trace: the family meets each of the {0} cuttings in exactly {1} pieces, failures {2}"
     .format(nd(NS), nd(12), nd(BADSZ)))

gate(BADLAW == 0, "K6",
     "affine law: the label sum equals {0} times (p - {1}) with p the size of the trace in H+, failures {2} of {3}"
     .format(nd(4), nd(6), nd(BADLAW), nd(NS)))

gate(BADCOR == 0 and PRANGE, "K7",
     "corollaries: label-positive count {0} p, p from {1} to {2}, size {3} exactly when p is {1} or {2}, failures {4} of {5}"
     .format(nd(2), nd(4), nd(8), nd(8), nd(BADCOR), nd(NS)))

gate(PCENS == PTGT and sum(PCEN.values()) == NS, "K8",
     "p census over the cuttings: {0}, total {1}, and the affine law carries it to the label sum census"
     .format(PCENS, nd(NS)))

gate(G0OK and G0H and G0S and BADNEG == 0 and NSWAP == 24 and NMINUS == 192, "K9",
     "mirror: the first-axis reflection is a bijection of the {0} pieces, keeps H, sends the {1} of H+ onto the {1} of H-, negations {2}"
     .format(nd(NPI), nd(len(HPL)), nd(BADNEG)))

emit("mirror layer: {0} of the {1} sign-minus elements keep H and swap its halves; trace failures {2} and {3} of {4}, p goes to {5} - p"
     .format(nd(NSWAP), nd(NMINUS), nd(BADMIR), nd(BADMP), nd(NTR), nd(12)))

gate(NTR == 6152 and NHS == NHTGT and NWSUM == NS and NCSUM == NTR and 6 not in NHIST, "K10",
     "trace layer: {0} distinct traces, completion counts {1}, none at {2}, weighted {3}"
     .format(nd(NTR), NHS, nd(6), nd(NWSUM)))

gate(BADMIR == 0 and BADMP == 0 and LCTS == LCTGT and PURE and MIRLAY and SIXSET == [1, 2, 3, 4, 7, 10], "K11",
     "per-p trace counts {0}; p {1} and p {2} pure at {3}; p {4} and p {5} equal entry by entry; p {6} takes {7}"
     .format(LCTS, nd(4), nd(8), nd(1), nd(5), nd(7), nd(6), " ".join(nd(x) for x in SIXSET)))

W5 = sum(k * LAY[5][k] for k in LAY[5])
W6 = sum(k * LAY[6][k] for k in LAY[6])
emit("layers p {0} and p {1}: {2}, each of {3} traces over {4} cuttings"
     .format(nd(5), nd(7), L57, nd(LCT[5]), nd(W5)))
emit("layer p {0}: {1}, {2} traces over {3} cuttings".format(nd(6), L6, nd(LCT[6]), nd(W6)))

gate(EXOK and L57 == L57TGT and L6 == L6TGT, "K12",
     "extremes: all {0} cuttings of label sum size {1} are the unique completion of their trace, and those traces are the p {2} and p {3} layers"
     .format(nd(len(EXI)), nd(8), nd(4), nd(8)))

gate(NOTCONST == [5, 6, 7] and len(W1) > 0 and len(W10) > 0, "K13",
     "refutation: the completion count is not constant on the p {0}, p {1}, p {2} classes, taking {3}, {4} and {5} values there"
     .format(nd(5), nd(6), nd(7), nd(NVAL[5]), nd(NVAL[6]), nd(NVAL[7])))

emit("witness one: a p {0} trace of completion count {1}, family members {2}".format(nd(6), nd(NAC[W1[0]]), famlist(W1[0])))
emit("witness two: a p {0} trace of completion count {1}, family members {2}".format(nd(6), nd(NAC[W10[0]]), famlist(W10[0])))

gate(RBADSZ == 3390 and RBADLAW == 1975 and RBADSZ > 0 and RBADLAW > 0 and len(RSET) == NH, "K14",
     "rejector: swapping the least family piece for the least outsider breaks the constant trace on {0} cuttings and the affine law on {1}"
     .format(nd(RBADSZ), nd(RBADLAW)))

emit("census: label sum over the {0} cuttings {1}".format(nd(NS), SCENS))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit("resource: under {0} s of the {1} s budget, under {2} MB of the {3} MB budget, {4} characters"
     .format(nd(((SECS // 60) + 1) * 60), nd(900), nd(((PEAK // 250) + 1) * 250), nd(2500), nd(OUT[0])))
