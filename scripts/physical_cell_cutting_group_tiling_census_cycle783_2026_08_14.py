"""Physical cell cutting: the cuttings are exact tilings by two eight-element tiles, and the label-sum census is symmetry-forced.

Standalone exact runner, standard library only. The preamble rebuilds the unit four-cube cell object from scratch, as in the sibling
cycles: the five-corner unit-determinant pieces at the adjacency cost floor, the 15800 cuttings by 24 pieces, the 192 pieces that occur
in them, and the 192 chambers of the twelve-wall cut of the open cell, each piece holding 8 of them and each chamber sitting in 8 pieces.
A cutting meets every chamber in exactly one piece; that partition property is re-verified here and is the geometric input used below.

Put each piece in its minimal naming, start corner v0 below its opposite, and let L(P) = sgn(sg) times minus one to the weight of v0.
The label sum S(T) adds L over the 24 pieces of a cutting. The order-384 symmetry group of the cell, axis permutations composed with
per-axis reflections x -> 1 - x, permutes chambers and pieces; its sign character eps(g) = sgn(p) times minus one to the popcount of the
reflection mask satisfies L(gP) = eps(g) L(P), so S(gT) = eps(g) S(T) and the census is symmetric under a change of sign of S.

The even-mask subgroup, order 192, relabels the chambers freely and transitively, so pieces transport to eight-element subsets of the
subgroup. Two base pieces give two tiles X0 and X1, the 192 pieces are exactly the 192 distinct left translates of the two tiles, each
piece arising from exactly two translating elements, and L(w X) = sgn of the permutation part of w. A cutting is then a partition of the
subgroup into 24 translates. An independent search over the abstract model alone recovers 15800 tilings and the same census, and the two
collections agree cutting by cutting. Tile shadows give 12 positions; profiles give an abstract count of 125 with 25 realized, six orbits
under the symmetry group, per-orbit censuses, and the extreme cross-check at absolute value 8.

Gates: K1 object rebuild, K2 the group action and the sign character, K3 the free relabelling and the abstract product law, K4 the tiles
and the translate dictionary, K5 the label theorem, K6 the model-only recount, K7 the bijection, K8 the positions, K9 the profile system,
K10 the profile orbits, K11 the halving and the per-profile censuses, K12 the assembly identities, K13 the extreme orbits, K14 to K16
three wrong-value rejectors. All work is exact over the integers and the rationals; no floating point enters any gate."""

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

FULLC = (1 << NCH) - 1
BADP = 0
for s in CUT:
    u = 0
    tot = 0
    for i in s:
        u |= CHM[i]
        tot += popc(CHM[i])
    if not (len(s) == 24 and tot == NCH and u == FULLC):
        BADP += 1

# ------------------------------------------------------------------
# 4. the minimal naming, the piece label, the label sum
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
SVAL = [sum(LAB[i] for i in s) for s in CUT]
SCEN = {}
for v in SVAL:
    bump(SCEN, v)
SCENS = cens(SCEN)

# ------------------------------------------------------------------
# 5. the order-384 symmetry group of the cell and its sign character
# ------------------------------------------------------------------

MAGS = [FR(8, 20), FR(6, 20), FR(4, 20), FR(2, 20)]


def spt(ch):
    """an exact rational interior point of the chamber, on the diagonal scale"""
    b, s = ch
    u = [FR(0)] * 4
    for k in range(4):
        u[b[k]] = (s[k] if k < 3 else 1) * MAGS[k]
    return [FR(1, 2) + t for t in u]


PTS = [spt(c) for c in CHAM]


def ckey(x):
    """the chamber that holds the point x: the size order of the offsets and the first three signs"""
    u = [t - FR(1, 2) for t in x]
    b = tuple(sorted(range(4), key=lambda i: -abs(u[i])))
    return (b, tuple(1 if u[b[k]] > 0 else -1 for k in range(3)))


def cellmap(pi, m, x):
    """the cell map of the pair (p, m): permute the axes by p, then reflect x -> 1 - x on the axes of m"""
    return [1 - x[pi[i]] if (m >> i) & 1 else x[pi[i]] for i in range(4)]


PSET = dict((frozenset(INC[i]), i) for i in range(NPI))
GPI = []
GMK = []
GCH = []
GPC = []
GEP = []
ACTOK = True
for pi in PERMS:
    for m in range(16):
        cp = [CIDX[ckey(cellmap(pi, m, p))] for p in PTS]
        if sorted(cp) != list(range(NCH)):
            ACTOK = False
        pp = []
        for i in range(NPI):
            j = PSET.get(frozenset(cp[c] for c in INC[i]), -1)
            if j < 0:
                ACTOK = False
            pp.append(j)
        GPI.append(pi)
        GMK.append(m)
        GCH.append(cp)
        GPC.append(tuple(pp))
        GEP.append(sgnp(pi) * (1 - 2 * (popc(m) & 1)))

NG = len(GPI)
FAITH = len(set(GPC))
NEG = sum(1 for g in range(NG) if GEP[g] == -1)
BADCOV = 0
for g in range(NG):
    ep = GEP[g]
    pc = GPC[g]
    for i in range(NPI):
        if LAB[pc[i]] != ep * LAB[i]:
            BADCOV += 1
NPAIRC = NG * NPI

# ------------------------------------------------------------------
# 6. the even-mask subgroup, its free transitive relabelling, the abstract model
# ------------------------------------------------------------------

EV = [m for m in range(16) if (popc(m) & 1) == 0]
EG = [g for g in range(NG) if (popc(GMK[g]) & 1) == 0]
C0 = CIDX[((0, 1, 2, 3), (1, 1, 1))]
ORB = [GCH[g][C0] for g in EG]
FREE = (len(EG) == 192 and sorted(ORB) == list(range(NCH)))

ELEMS = [(p, m) for p in PERMS for m in EV]
EIDX = dict((e, i) for i, e in enumerate(ELEMS))
NEL = len(ELEMS)


def pistar(pi, m):
    return sum(((m >> pi[i]) & 1) << i for i in range(4))


def prod(g, h):
    """the group product apply h then g, on pairs (permutation, mask)"""
    pg, mg = g
    ph, mh = h
    return (tuple(ph[pg[i]] for i in range(4)), mg ^ pistar(pg, mh))


def acttok(e, x):
    """the cell map of e on a token vector; a reflected axis carries the bit 4"""
    pi, m = e
    return tuple(x[pi[i]] ^ (4 if (m >> i) & 1 else 0) for i in range(4))


TOK = (0, 1, 2, 3)
IMGS = set(acttok(e, TOK) for e in ELEMS)
BADPR = 0
for g in ELEMS:
    for h in ELEMS:
        if acttok(prod(g, h), TOK) != acttok(g, acttok(h, TOK)):
            BADPR += 1

PHI = {}
for k, g in enumerate(EG):
    PHI[(GPI[g], GMK[g])] = ORB[k]
GOF = dict(((GPI[g], GMK[g]), g) for g in EG)
ECH = [PHI[e] for e in ELEMS]
INVCH = dict((c, i) for i, c in enumerate(ECH))
BADDICT = 0
for g in ELEMS:
    cg = GCH[GOF[g]]
    for h in ELEMS:
        if PHI[prod(g, h)] != cg[PHI[h]]:
            BADDICT += 1
NPAIRE = NEL * NEL

# ------------------------------------------------------------------
# 7. transport, the two base pieces, the two tiles, the translate dictionary
# ------------------------------------------------------------------

XOF = [tuple(sorted(INVCH[c] for c in INC[i])) for i in range(NPI)]
SHAD = [frozenset(ELEMS[b][0] for b in XOF[i]) for i in range(NPI)]


def unimodal(p):
    """the entries rise to the peak value and then fall"""
    k = 0
    while k + 1 < 4 and p[k] < p[k + 1]:
        k += 1
    while k + 1 < 4 and p[k] > p[k + 1]:
        k += 1
    return k == 3


UNI = frozenset(p for p in PERMS if unimodal(p))

TYPE = [-1] * NPI
NTYP = 0
for i in range(NPI):
    if TYPE[i] >= 0:
        continue
    st = [i]
    TYPE[i] = NTYP
    while st:
        q = st.pop()
        for g in EG:
            r = GPC[g][q]
            if TYPE[r] < 0:
                TYPE[r] = NTYP
                st.append(r)
    NTYP += 1
TYPSZ = sorted(TYPE.count(k) for k in range(NTYP))

INC0 = sorted(HOLD[C0])
CAND0 = [i for i in INC0 if SHAD[i] == UNI]
B0 = min(CAND0)
CAND1 = [i for i in INC0 if TYPE[i] != TYPE[B0]]
B1 = min(CAND1)
XT = [[ELEMS[b] for b in XOF[B0]], [ELEMS[b] for b in XOF[B1]]]
GRAPH = all(len(set(x[0] for x in XT[t])) == 8 and len(XT[t]) == 8 for t in (0, 1))
SH0 = (frozenset(x[0] for x in XT[0]) == UNI)

TILE = {}
REPC = {}
BADLB = 0
for w in ELEMS:
    sw = sgnp(w[0])
    for t in (0, 1):
        mk = 0
        for x in XT[t]:
            mk |= 1 << EIDX[prod(w, x)]
        REPC[mk] = REPC.get(mk, 0) + 1
        if mk in TILE:
            if TILE[mk] != (sw, t):
                BADLB += 1
        else:
            TILE[mk] = (sw, t)

TM = sorted(TILE)
TL = [TILE[m][0] for m in TM]
TT = [TILE[m][1] for m in TM]
NTM = len(TM)
TCEN = {}
for m in TM:
    bump(TCEN, TILE[m][1])
ETIL = [[] for _ in range(NEL)]
for ti, m in enumerate(TM):
    mm = m
    while mm:
        b = mm & (-mm)
        ETIL[b.bit_length() - 1].append(ti)
        mm ^= b
REPS = sorted(set(REPC.values()))
DEG = sorted(set(len(x) for x in ETIL))

STB = []
for t in (0, 1):
    base = 0
    for x in XT[t]:
        base |= 1 << EIDX[x]
    hs = []
    for h in ELEMS:
        mk = 0
        for x in XT[t]:
            mk |= 1 << EIDX[prod(h, x)]
        if mk == base:
            hs.append(h)
    STB.append(hs)
STOK = all(len(h) == 2 and h[0] == (TOK, 0) and sgnp(h[1][0]) == 1 for h in STB)
TORB = [NTM // 2, NTM // 2]

TPC = []
BADTP = 0
for m in TM:
    chs = frozenset(ECH[b] for b in range(NEL) if (m >> b) & 1)
    j = PSET.get(chs, -1)
    if j < 0:
        BADTP += 1
    TPC.append(j)
DICTOK = (sorted(TPC) == list(range(NPI)) and BADTP == 0)
BADTHM = sum(1 for t in range(NTM) if TL[t] != LAB[TPC[t]])
BASEOK = (LAB[B0] == 1 and LAB[B1] == 1)


def pstr(p):
    return "".join(str(x) for x in p)


def tstr(X):
    return " ".join("{0}:{1}".format(pstr(x[0]), nd(x[1])) for x in X)


# ------------------------------------------------------------------
# 8. the recount over the abstract model alone
# ------------------------------------------------------------------


def recount(nel, tiles):
    """a search over the abstract data only: nel elements, tiles given as (mask, label) pairs"""
    full = (1 << nel) - 1
    byel = [[] for _ in range(nel)]
    for ti in range(len(tiles)):
        mm = tiles[ti][0]
        while mm:
            b = mm & (-mm)
            byel[b.bit_length() - 1].append(ti)
            mm ^= b
    sols = []
    cen = {}

    def rec(cov, sig, ch):
        if cov == full:
            sols.append(tuple(ch))
            cen[sig] = cen.get(sig, 0) + 1
            return
        rem = full & (~cov)
        low = (rem & (-rem)).bit_length() - 1
        for ti in byel[low]:
            mk = tiles[ti][0]
            if mk & cov:
                continue
            ch.append(ti)
            rec(cov | mk, sig + tiles[ti][1], ch)
            ch.pop()

    rec(0, 0, [])
    return sols, cen


ABSD = [(TM[t], TL[t]) for t in range(NTM)]
SOL2, RCEN = recount(NEL, ABSD)
NR = len(SOL2)
RCENS = cens(RCEN)

CIX = dict((frozenset(s), i) for i, s in enumerate(CUT))
S2C = []
BADBIJ = 0
for so in SOL2:
    j = CIX.get(frozenset(TPC[t] for t in so), -1)
    if j < 0:
        BADBIJ += 1
    S2C.append(j)
BIJ = (len(CIX) == NS and sorted(S2C) == list(range(NS)) and BADBIJ == 0)
BADSIG = sum(1 for k, so in enumerate(SOL2)
             if sum(TL[t] for t in so) != SVAL[S2C[k]])

# ------------------------------------------------------------------
# 9. the positions
# ------------------------------------------------------------------

SHT = [frozenset(ELEMS[b][0] for b in range(NEL) if (TM[t] >> b) & 1) for t in range(NTM)]
POSL = sorted(set(SHT), key=lambda P: sorted(P))
PIDX = dict((P, k) for k, P in enumerate(POSL))
NPOS = len(POSL)
TPOS = [PIDX[s] for s in SHT]
PPOS = [None] * NPI
for t in range(NTM):
    PPOS[TPC[t]] = TPOS[t]
RDEG = {}
for P in POSL:
    for r in P:
        bump(RDEG, r)
PERPOS = {}
PERPT = {}
for t in range(NTM):
    bump(PERPOS, TPOS[t])
    bump(PERPT, (TPOS[t], TT[t]))
LABPT = {}
BADPT = 0
for t in range(NTM):
    k = (TPOS[t], TT[t])
    if k in LABPT:
        if LABPT[k] != TL[t]:
            BADPT += 1
    else:
        LABPT[k] = TL[t]
OPP = all(LABPT[(k, 0)] == -LABPT[(k, 1)] for k in range(NPOS))
SHOK = sorted(set(len(s) for s in SHT))

# ------------------------------------------------------------------
# 10. the profile system, the realized profiles, the parity question
# ------------------------------------------------------------------

INCP = [[r for r in range(24) if PERMS[r] in POSL[k]] for k in range(NPOS)]
POSOF = [[k for k in range(NPOS) if r in INCP[k]] for r in range(24)]


def profsolve(tgt):
    """all nonnegative integer position vectors whose four positions at each permutation sum to tgt"""
    out = []
    rem = [tgt] * 24
    mu = [0] * NPOS

    def rec(k):
        if k == NPOS:
            if all(v == 0 for v in rem):
                out.append(tuple(mu))
            return
        mx = min(rem[r] for r in INCP[k])
        for v in range(mx, -1, -1):
            for r in INCP[k]:
                rem[r] -= v
            ok = True
            for r in range(24):
                if rem[r] > 0 and all(q <= k for q in POSOF[r]):
                    ok = False
                    break
            if ok:
                mu[k] = v
                rec(k + 1)
            for r in INCP[k]:
                rem[r] += v
        mu[k] = 0

    rec(0)
    return out


def paritycl(mu):
    ps = set(v & 1 for v in mu)
    return "odd" if ps == set([1]) else ("even" if ps == set([0]) else "mix")


ABSP = profsolve(8)
APAR = {}
for mu in ABSP:
    bump(APAR, paritycl(mu))

PROF = []
for so in SOL2:
    nu = [0] * NPOS
    for t in so:
        nu[TPOS[t]] += 1
    PROF.append(tuple(nu))
BYP = {}
for k, pr in enumerate(PROF):
    BYP.setdefault(pr, []).append(k)
P25 = sorted(BYP)
RPAR = {}
for pr in P25:
    bump(RPAR, paritycl(pr))
SUBSET = set(P25) <= set(ABSP)
MIXNR = sum(1 for mu in ABSP if paritycl(mu) == "mix" and mu not in BYP)

ROWS = []
for r in range(24):
    v = 0
    for k in POSOF[r]:
        v |= 1 << k
    ROWS.append(v)
PIV = []
for v in ROWS:
    x = v
    for p in PIV:
        lo = p & (-p)
        if x & lo:
            x ^= p
    if x:
        PIV.append(x)
RK2 = len(PIV)
KDIM = NPOS - RK2

# ------------------------------------------------------------------
# 11. the profile orbits, the per-profile counts and censuses, the halving
# ------------------------------------------------------------------

PPERM = []
BADPA = 0
for g in range(NG):
    pp = [None] * NPOS
    for i in range(NPI):
        a, b = PPOS[i], PPOS[GPC[g][i]]
        if pp[a] is None:
            pp[a] = b
        elif pp[a] != b:
            BADPA += 1
    PPERM.append(tuple(pp))


def actprof(pp, pr):
    out = [0] * NPOS
    for j in range(NPOS):
        out[pp[j]] = pr[j]
    return tuple(out)


ORBOF = {}
ORBS = []
for pr in P25:
    if pr in ORBOF:
        continue
    o = set([pr])
    st = [pr]
    while st:
        q = st.pop()
        for pp in PPERM:
            im = actprof(pp, q)
            if im not in o:
                o.add(im)
                st.append(im)
    for q in o:
        ORBOF[q] = len(ORBS)
    ORBS.append(sorted(o))

CNTOF = dict((pr, len(BYP[pr])) for pr in P25)
CENOF = {}
for pr in P25:
    d = {}
    for k in BYP[pr]:
        bump(d, SVAL[S2C[k]])
    CENOF[pr] = d
OKORB = True
OCNT = {}
OCEN = {}
for oi, o in enumerate(ORBS):
    cs = set(CNTOF[pr] for pr in o)
    ces = set(tuple(sorted(CENOF[pr].items())) for pr in o)
    if len(cs) != 1 or len(ces) != 1:
        OKORB = False
    OCNT[oi] = sorted(cs)[0]
    OCEN[oi] = dict(sorted(ces)[0])
RANK = sorted(range(len(ORBS)), key=lambda oi: -OCNT[oi])
TAGS = "UOABCD"
OSZ = [len(ORBS[oi]) for oi in RANK]
OCT = [OCNT[oi] for oi in RANK]
OCS = [OCEN[oi] for oi in RANK]
WTOT = sum(OSZ[k] * OCT[k] for k in range(len(RANK)))
OEXT = [OCS[k].get(8, 0) + OCS[k].get(-8, 0) for k in range(len(RANK))]

STABEPS = 0
for pr in P25:
    if any(GEP[g] == -1 and actprof(PPERM[g], pr) == pr for g in range(NG)):
        STABEPS += 1
HALV = all(OCS[k].get(8, 0) == OCS[k].get(-8, 0) for k in range(len(RANK)))
PUREO = all(abs(SVAL[S2C[k]]) == 4 for pr in ORBS[RANK[1]] for k in BYP[pr])
PUREB = all(abs(SVAL[S2C[k]]) == 8 for pr in ORBS[RANK[3]] for k in BYP[pr])

WANT = [(1, 9368, {-8: 24, 0: 9320, 8: 24}), (6, 944, {-4: 472, 4: 472}),
        (3, 160, {-8: 8, 0: 144, 8: 8}), (3, 24, {-8: 12, 8: 12}),
        (6, 20, {-8: 6, 0: 8, 8: 6}), (6, 16, {0: 16})]
GOT = [(OSZ[k], OCT[k], OCS[k]) for k in range(len(RANK))]

# ------------------------------------------------------------------
# 12. the assembly identities
# ------------------------------------------------------------------

NEXT8 = SCEN.get(8, 0)
NEXTA = SCEN.get(8, 0) + SCEN.get(-8, 0)
TOTEXT = sum(OSZ[k] * OEXT[k] for k in range(len(RANK)))
FOUR = SCEN.get(4, 0)
ASM1 = (FOUR == OSZ[1] * OCS[1].get(4, 0))
ASM2 = (NEXT8 == TOTEXT // 2)
ASM3 = (SCEN.get(0, 0) == NS - OSZ[1] * OCT[1] - TOTEXT)
ASM4 = (OEXT == [48, 0, 16, 24, 12, 0] and TOTEXT == 240)

# ------------------------------------------------------------------
# 13. the extreme orbits
# ------------------------------------------------------------------

EXT = [i for i in range(NS) if abs(SVAL[i]) == 8]
CSET = [frozenset(s) for s in CUT]
EOF = {}
EORB = []
ESTB = []
EOK = True
for i in EXT:
    if i in EOF:
        continue
    T = CSET[i]
    orb = set()
    stb = []
    for g in range(NG):
        j = CIX[frozenset(GPC[g][p] for p in T)]
        orb.add(j)
        if j == i:
            stb.append(GEP[g])
    for j in orb:
        EOF[j] = len(EORB)
    sc = {}
    for j in orb:
        bump(sc, SVAL[j])
    if set(stb) != set([1]) or sc.get(8, 0) != sc.get(-8, 0) or len(orb) * len(stb) != NG:
        EOK = False
    EORB.append(len(orb))
    ESTB.append(len(stb))
ESZ = {}
for x in EORB:
    bump(ESZ, x)
EPAIR = sorted(set(zip(EORB, ESTB)))

# ------------------------------------------------------------------
# 14. three wrong-value rejectors
# ------------------------------------------------------------------

XP = list(XT[0])
M2 = [q for q in EV if q != XP[0][1]][0]
XP[0] = (XP[0][0], M2)
PMASK = set()
for w in ELEMS:
    for XX in (XP, XT[1]):
        mk = 0
        for x in XX:
            mk |= 1 << EIDX[prod(w, x)]
        PMASK.add(mk)
PHIT = 0
for mk in PMASK:
    if frozenset(ECH[b] for b in range(NEL) if (mk >> b) & 1) in PSET:
        PHIT += 1

WCEN = {}
for so in SOL2:
    bump(WCEN, sum(TL[t] * (1 - 2 * TT[t]) for t in so))
DIFFK = [k for k in sorted(set(list(WCEN) + list(RCEN))) if WCEN.get(k, 0) != RCEN.get(k, 0)]
WM8 = WCEN.get(-8, 0)
RM8 = RCEN.get(-8, 0)

MIXW = None
for mu in ABSP:
    if paritycl(mu) == "mix":
        MIXW = mu
        break
MIXN = len(BYP.get(MIXW, []))

# ------------------------------------------------------------------
# 15. gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800 and SIZES == [24] and NPI == 192
     and NCH == 192 and INCN == [8] and HOLDN == [8] and DEALOK == NPI and BADP == 0 and GENERIC
     and NPER == [2] and len(NAMES) == 384 and NPTS == 625, "K1",
     "object: {0} candidates, floor {1}, {2} kept, {3} points, {4} cuttings of {5}, {6} pieces, {7} chambers, incidence {8} and {8},"
     " bad {9}"
     .format(nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NPTS), nd(NS), nd(SIZES[0]), nd(NPI), nd(NCH), nd(INCN[0]), nd(BADP)))

emit("namings: {0} walk namings, {1} per piece, and the minimal one starts at the corner below its opposite"
     .format(nd(len(NAMES)), nd(NPER[0])))

gate(ACTOK and NG == 384 and FAITH == 384 and BADCOV == 0 and NEG == 192 and SCENS ==
     "-8:120 -4:2832 0:9896 4:2832 8:120", "K2",
     "symmetry group: {0} elements permute {1} chambers and {1} pieces, distinct maps {2}, sign minus on {3},"
     " covariance failures {4} of {5}"
     .format(nd(NG), nd(NPI), nd(FAITH), nd(NEG), nd(BADCOV), nd(NPAIRC)))

gate(FREE and len(IMGS) == 192 and BADPR == 0 and BADDICT == 0 and NEL == 192 and len(EV) == 8, "K3",
     "relabelling: the even-mask subgroup of {0} elements, from {1} masks, hits each of {2} chambers once;"
     " product failures {3}, dictionary {4} of {5}"
     .format(nd(len(EG)), nd(len(EV)), nd(NCH), nd(BADPR), nd(BADDICT), nd(NPAIRE)))

emit("tile zero: {0}".format(tstr(XT[0])))
emit("tile one: {0}".format(tstr(XT[1])))
emit("stabilizers: tile zero fixed by {0}:{1}, tile one by {2}:{3}, both permutation signs plus, orbit {4} times stabilizer {5} is {6}"
     .format(pstr(STB[0][1][0]), nd(STB[0][1][1]), pstr(STB[1][1][0]), nd(STB[1][1][1]), nd(TORB[0]), nd(len(STB[0])), nd(NEL)))

gate(GRAPH and SH0 and TYPSZ == [96, 96] and NTM == 192 and TCEN == {0: 96, 1: 96} and REPS == [2]
     and DEG == [8] and DICTOK and BADLB == 0 and STOK and len(INC0) == 8 and B0 == 9 and B1 == 73
     and len(CAND0) == 2 and len(set(SHAD)) == 12 and sorted(set(len(s) for s in SHAD)) == [8], "K4",
     "tiles: bases {0} and {1} among the {2} at the base chamber, types {3} and {3}, {4} translates {5} and {5},"
     " {6} carriers each, degree {7}, bad {8}"
     .format(nd(B0), nd(B1), nd(len(INC0)), nd(TYPSZ[0]), nd(NTM), nd(TCEN[0]), nd(REPS[0]), nd(DEG[0]), nd(BADTP + BADLB)))

gate(BADTHM == 0 and BASEOK, "K5",
     "label theorem: L of a translate w X equals the sign of the permutation part of w, failures {0} of {1}, both base labels plus"
     .format(nd(BADTHM), nd(NPI)))

gate(NR == 15800 and RCENS == "-8:120 -4:2832 0:9896 4:2832 8:120", "K6",
     "model-only recount: the abstract search over {0} elements and {1} tiles finds {2} tilings, census {3}"
     .format(nd(NEL), nd(NTM), nd(NR), RCENS))

gate(BIJ and BADSIG == 0, "K7",
     "bijection: the {0} tilings and the {0} cuttings match as sets, and the tile sum equals the label sum on each, failures {1}"
     .format(nd(NS), nd(BADSIG + BADBIJ)))

gate(NPOS == 12 and sorted(set(RDEG.values())) == [4] and sorted(set(PERPOS.values())) == [16]
     and sorted(set(PERPT.values())) == [8] and BADPT == 0 and OPP and SHOK == [8], "K8",
     "positions: {0} shadows of size {1}, every permutation in {2} of them, {3} pieces each and {1} per type, label failures {4},"
     " types opposite {5}"
     .format(nd(NPOS), nd(SHOK[0]), nd(sorted(set(RDEG.values()))[0]), nd(sorted(set(PERPOS.values()))[0]), nd(BADPT),
             "yes" if OPP else "no"))

gate(len(ABSP) == 125 and APAR == {"odd": 8, "even": 27, "mix": 90} and len(P25) == 25
     and RPAR == {"odd": 6, "even": 19} and SUBSET and MIXNR == 90 and KDIM == 6, "K9",
     "profiles: {0} abstract solutions, {1} odd {2} even {3} parity-mixed; {4} realized, {5} odd {6} even, mixed realized {7};"
     " kernel dimension {8} of {9}"
     .format(nd(len(ABSP)), nd(APAR["odd"]), nd(APAR["even"]), nd(APAR["mix"]), nd(len(P25)), nd(RPAR["odd"]), nd(RPAR["even"]),
             nd(len(ABSP) - MIXNR - APAR["odd"] - APAR["even"]), nd(KDIM), nd(NPOS)))

gate(BADPA == 0 and OKORB and len(ORBS) == 6 and OSZ == [1, 6, 3, 3, 6, 6]
     and OCT == [9368, 944, 160, 24, 20, 16] and WTOT == 15800, "K10",
     "orbits: {0} orbits of the {1} realized profiles, sizes {2}, counts {3}, weighted total {4}, action failures {5}"
     .format(nd(len(ORBS)), nd(len(P25)), " ".join(nd(x) for x in OSZ), " ".join(nd(x) for x in OCT), nd(WTOT), nd(BADPA)))

for k in range(0, 6, 2):
    emit("profile census: {0} size {1} count {2} {3}; {4} size {5} count {6} {7}"
         .format(TAGS[k], nd(OSZ[k]), nd(OCT[k]), cens(OCS[k]), TAGS[k + 1], nd(OSZ[k + 1]), nd(OCT[k + 1]), cens(OCS[k + 1])))

gate(STABEPS == 25 and HALV and GOT == WANT and PUREO and PUREB, "K11",
     "halving: each of the {0} profiles has a sign-minus stabilizer, per-profile censuses all sign symmetric, class {1} pure at {2}"
     " and class {3} at {4}"
     .format(nd(len(P25)), TAGS[1], nd(4), TAGS[3], nd(8)))

gate(ASM1 and ASM2 and ASM3 and ASM4 and NEXTA == 240, "K12",
     "assembly: {0} = {1} times {2}; {3} = ({4} + {5} times {6} + {5} times {7} + {8} times {9}) halved; {10} = {11} - {12} - {13}"
     .format(nd(FOUR), nd(OSZ[1]), nd(OCS[1][4]), nd(NEXT8), nd(OEXT[0]), nd(OSZ[2]), nd(OEXT[2]), nd(OEXT[3]), nd(OSZ[4]),
             nd(OEXT[4]), nd(SCEN[0]), nd(NS), nd(OSZ[1] * OCT[1]), nd(TOTEXT)))

gate(EOK and len(EXT) == 240 and len(EORB) == 7 and ESZ == {24: 4, 48: 3} and EPAIR == [(24, 16), (48, 8)]
     and NEXT8 == sum(EORB) // 2, "K13",
     "extremes: the {0} cuttings at size {1} fall into {2} orbits, {3} of size {4} by stabilizer {5} and {6} of size {7} by {8},"
     " each product {9}"
     .format(nd(len(EXT)), nd(8), nd(len(EORB)), nd(ESZ[24]), nd(24), nd(16), nd(ESZ[48]), nd(48), nd(8), nd(NG)))

gate(PHIT < 192 and PHIT == 96 and len(PMASK) == 288, "K14",
     "rejector one: moving one tile element to another even mask gives {0} distinct translates of which {1} are pieces, short of {2}"
     .format(nd(len(PMASK)), nd(PHIT), nd(NPI)))

gate(len(DIFFK) == 3 and WM8 == 108 and RM8 == 120, "K15",
     "rejector two: negating the labels of one tile type changes the census at {0} values, the count at minus {1} moving from {2} to {3}"
     .format(nd(len(DIFFK)), nd(8), nd(RM8), nd(WM8)))

gate(MIXW is not None and MIXN == 0, "K16",
     "rejector three: the parity-mixed abstract solution {0} is realized by {1} of the {2} tilings"
     .format(" ".join(nd(v) for v in MIXW), nd(MIXN), nd(NS)))

emit("census: label sum over the {0} cuttings {1}".format(nd(NS), SCENS))
emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit("resource: under {0} s of the {1} s budget, under {2} MB of the {3} MB budget, {4} characters"
     .format(nd(((SECS // 60) + 1) * 60), nd(900), nd(((PEAK // 250) + 1) * 250), nd(2500), nd(OUT[0])))
