"""Physical cell cutting: parity constancy is a theorem of the sign characters, and the three small per-profile counts follow from coset blocks.

Standalone exact runner, standard library only. The preamble rebuilds the unit four-cube cell object from the corner coordinates, as in the
sibling cycles: the five-corner unit-determinant pieces at the adjacency cost floor, the 15800 cuttings by 24 pieces, the 192 pieces that
occur in them, the 192 chambers of the twelve-wall cut, the order-384 symmetry group of the cell, and the even-mask subgroup of order 192
that relabels the chambers freely and transitively. Transported to that subgroup every used piece is the graph of a function from an
eight-element set of axis orderings, its position, to the eight even masks. Twelve positions, sixteen pieces each, two types of eight: the
24 classes are the free orbits of mask translation, and the piece with class offset function f and translation mask m covers, at the axis
ordering rho of its position, the chamber (rho, m XOR f(rho)). All of that is derived here from the physical piece-chamber incidence.

Two derivations follow. First, the image of every class offset function lies inside exactly one of the three four-element mask subgroups
that contain the all-axes flip. Calling a cutting coset-pure when every class it meets carries a coset of a nontrivial subgroup of the mask
group, an independent exact cover by affine blocks, at most one block per class, reproduces the coset-pure cuttings exactly: 1224 of them,
carrying every class-B, class-C and class-D cutting and part of class A. Since the group maps cuttings to cuttings and is transitive on the
profiles of a class, the fibers over the profiles of one class have equal size, so the class totals 72, 120 and 96 split evenly into the
per-profile counts 24, 20 and 16. For one sub-family the count has a hand-sized closed form: 12 two-covering six-class choices, each signed
connected, times 2 colourings.

Second, at each axis ordering a cutting partitions the eight masks, and every nontrivial sign character sums to zero over the mask group, so
the class counts mod 2 lie in the kernel of an explicit 24 by 24 sign matrix for each of the seven characters. The kernels are exact, by
fraction-free integer row reduction on the transpose augmented with the identity, and their intersection has 128 vectors, every one of them
constant in the per-position parity. Parity constancy of the realized profiles is therefore a theorem, not a measurement.

Gates: K1 to K4 the object and the tile coordinates, K5 the census baseline, K6 the base fact, K7 to K10 the blocks and the purity content,
K11 and K12 the equal split and the arithmetic, K13 and K14 the families and the closed form, K15 the parity theorem, K16 two rejectors.
All work is exact over the integers and the rationals; no floating point enters any gate."""

import itertools
import sys
import time
import resource
from fractions import Fraction as FR

T0 = time.time()
OUT = [0]


def emit(s):
    txt = f"{s}"
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
    emit(f"{'PASS' if ok else 'FAIL'} {tag} {msg}")


def nd(x):
    """a printed number never carries a doubled nine; emit bars that digit run"""
    s = str(x)
    if ("9" + "9") in s:
        return " ".join(s)
    return s


def popc(x):
    return x.bit_count()


def bump(d, k):
    d[k] = d.get(k, 0) + 1


def cens(d):
    return " ".join(f"{nd(k)}:{nd(d[k])}" for k in sorted(d))


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
# 2. the paths and their namings
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
RIX = dict((p, i) for i, p in enumerate(PERMS))
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
# 4. the order-384 symmetry group of the cell
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

# ------------------------------------------------------------------
# 5. the even-mask subgroup and its free transitive relabelling
# ------------------------------------------------------------------

EV = [m for m in range(16) if (popc(m) & 1) == 0]
MIX = dict((m, i) for i, m in enumerate(EV))
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

# ------------------------------------------------------------------
# 6. the tile coordinates, derived from the piece-chamber incidence
# ------------------------------------------------------------------

XOF = [tuple(sorted(INVCH[c] for c in INC[i])) for i in range(NPI)]
ESET = dict((frozenset(XOF[i]), i) for i in range(NPI))
FUN = []
GRAPH = True
for i in range(NPI):
    d = {}
    for b in XOF[i]:
        p, m = ELEMS[b]
        if p in d:
            GRAPH = False
        d[p] = m
    if len(d) != 8:
        GRAPH = False
    FUN.append(d)

SHAD = [frozenset(FUN[i]) for i in range(NPI)]
POSL = sorted(set(SHAD), key=lambda P: sorted(P))
PIDX = dict((P, k) for k, P in enumerate(POSL))
NPOS = len(POSL)
PPOS = [PIDX[SHAD[i]] for i in range(NPI)]
PERPOS = sorted(set(PPOS.count(k) for k in range(NPOS)))

TRANS = {}
BADTR = 0
for i in range(NPI):
    for m in EV:
        j = ESET.get(frozenset(EIDX[(p, m ^ FUN[i][p])] for p in SHAD[i]), -1)
        if j < 0:
            BADTR += 1
        TRANS[(m, i)] = j

ORBIT = [-1] * NPI
ORBL = []
for i in range(NPI):
    if ORBIT[i] >= 0:
        continue
    o = sorted(set(TRANS[(m, i)] for m in EV))
    for j in o:
        ORBIT[j] = len(ORBL)
    ORBL.append(o)
ORBSZ = sorted(set(len(o) for o in ORBL))

TYP = [-1] * NPI
TPERP = []
for k in range(NPOS):
    os = []
    for i in range(NPI):
        if PPOS[i] == k and ORBIT[i] not in os:
            os.append(ORBIT[i])
    TPERP.append(len(os))
    for i in range(NPI):
        if PPOS[i] == k:
            TYP[i] = os.index(ORBIT[i])

KOF = [2 * PPOS[i] + TYP[i] for i in range(NPI)]
NCL = len(set(KOF))
BASE = {}
for i in range(NPI):
    if KOF[i] not in BASE:
        BASE[KOF[i]] = i
FB = dict((k, FUN[BASE[k]]) for k in sorted(BASE))
MC = [-1] * NPI
BADMC = 0
for i in range(NPI):
    ms = set(FUN[i][p] ^ FB[KOF[i]][p] for p in SHAD[i])
    if len(ms) != 1:
        BADMC += 1
    MC[i] = min(ms)

LAWBAD = 0
for i in range(NPI):
    ch = set(ECH[EIDX[(p, MC[i] ^ FB[KOF[i]][p])]] for p in FB[KOF[i]])
    if ch != set(INC[i]):
        LAWBAD += 1

CLM = {}
for i in range(NPI):
    CLM[(KOF[i], MC[i])] = i
CLSZ = sorted(set(KOF.count(k) for k in range(NCL)))
SHM = {}
for k in range(NCL):
    v = 0
    for p in FB[k]:
        v |= 1 << RIX[p]
    SHM[k] = v
CLAT = [[k for k in range(NCL) if (SHM[k] >> r) & 1] for r in range(24)]
ATR = sorted(set(len(x) for x in CLAT))

# ------------------------------------------------------------------
# 7. the profiles, the six orbits, the census baseline
# ------------------------------------------------------------------

PRV = []
for s in CUT:
    nu = [0] * NPOS
    for i in s:
        nu[PPOS[i]] += 1
    PRV.append(tuple(nu))
BYP = {}
for k, pr in enumerate(PRV):
    BYP.setdefault(pr, []).append(k)
P25 = sorted(BYP)

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
OKORB = all(len(set(CNTOF[pr] for pr in o)) == 1 for o in ORBS)
OCNT = [CNTOF[o[0]] for o in ORBS]
RANK = sorted(range(len(ORBS)), key=lambda oi: -OCNT[oi])
TAGS = "UOABCD"
TAGOF = {}
for r, oi in enumerate(RANK):
    for pr in ORBS[oi]:
        TAGOF[pr] = TAGS[r]
OSZ = [len(ORBS[oi]) for oi in RANK]
OCB = [OCNT[oi] for oi in RANK]
CTAG = [TAGOF[PRV[si]] for si in range(NS)]
TOTC = {}
for si in range(NS):
    bump(TOTC, CTAG[si])
CBASE = " ".join(f"{nd(OCB[k])}:{nd(OSZ[k])}" for k in range(len(RANK)))
WTOT = sum(OSZ[k] * OCB[k] for k in range(len(RANK)))

# ------------------------------------------------------------------
# 8. the base fact: each class offset image sits in one mask subgroup
# ------------------------------------------------------------------

FLIP = 15
VS = [frozenset((0, 3, 12, 15)), frozenset((0, 5, 10, 15)), frozenset((0, 6, 9, 15))]
VSTR = [",".join(nd(x) for x in sorted(V)) for V in VS]
VSUB = []
for V in VS:
    if not (len(V) == 4 and FLIP in V and all((a ^ b) in V for a in V for b in V)):
        VSUB.append(-1)
VOF = {}
BASEF = True
for k in range(NCL):
    vals = frozenset(FB[k].values())
    ins = [vi for vi in range(3) if vals <= VS[vi]]
    if len(ins) != 1:
        BASEF = False
    else:
        VOF[k] = ins[0]
VCT = {}
for k in sorted(VOF):
    bump(VCT, VOF[k])
VSPL = " ".join(nd(VCT.get(vi, 0)) for vi in range(3))

# ------------------------------------------------------------------
# 9. the affine blocks and the independent exact cover
# ------------------------------------------------------------------

AFF = []
for r in range(1, 256):
    A = tuple(EV[j] for j in range(8) if (r >> j) & 1)
    if len(A) < 2:
        continue
    H = set(a ^ A[0] for a in A)
    if all((x ^ y) in H for x in H for y in H):
        AFF.append(A)
AFFN = {}
for A in AFF:
    bump(AFFN, len(A))

BLK = []
for k in range(NCL):
    for A in AFF:
        cells = 0
        for p in FB[k]:
            for a in A:
                cells |= 1 << (8 * RIX[p] + MIX[a ^ FB[k][p]])
        BLK.append((k, A, cells))
NBLK = len(BLK)

FULLB = (1 << 192) - 1
BYCELL = [[] for _ in range(192)]
for b in range(NBLK):
    mm = BLK[b][2]
    while mm:
        lo = mm & (-mm)
        BYCELL[lo.bit_length() - 1].append(b)
        mm ^= lo

SOLB = []


def block_search(cov, used, ch):
    if cov == FULLB:
        SOLB.append(tuple(ch))
        return
    free = FULLB & (~cov)
    p = (free & (-free)).bit_length() - 1
    for b in BYCELL[p]:
        k, A, c = BLK[b]
        if (c & cov) or ((used >> k) & 1):
            continue
        ch.append(b)
        block_search(cov | c, used | (1 << k), ch)
        ch.pop()


block_search(0, 0, [])
NBP = len(SOLB)

CIX = dict((frozenset(s), i) for i, s in enumerate(CUT))
BPIX = []
BADBP = 0
for so in SOLB:
    j = CIX.get(frozenset(CLM[(BLK[b][0], a)] for b in so for a in BLK[b][1]), -1)
    if j < 0:
        BADBP += 1
    BPIX.append(j)
BPDIST = len(set(BPIX))

# ------------------------------------------------------------------
# 10. coset purity, the class content, and the three subgroup families
# ------------------------------------------------------------------

PUR = []
FAM = [[], [], []]
for si in range(NS):
    d = {}
    for i in CUT[si]:
        d.setdefault(KOF[i], []).append(MC[i])
    ok = True
    for ms in d.values():
        if len(ms) < 2:
            ok = False
            break
        H = set(x ^ ms[0] for x in ms)
        if any((x ^ y) not in H for x in H for y in H):
            ok = False
            break
    if ok:
        PUR.append(si)
    for vi in range(3):
        if all(len(ms) == 4 and frozenset(x ^ ms[0] for x in ms) == VS[vi]
               for ms in d.values()):
            FAM[vi].append(si)

PURC = {}
for si in PUR:
    bump(PURC, CTAG[si])
PSET2 = set(PUR)
BPSET = set(BPIX)
SETEQ = (PSET2 == BPSET and PSET2 <= BPSET and BPSET <= PSET2)
CONT = " ".join(f"{t} {nd(PURC.get(t, 0))} of {nd(TOTC[t])}" for t in "BCDAUO")
FAMN = [len(FAM[vi]) for vi in range(3)]
FAMTAG = sorted(set(CTAG[si] for vi in range(3) for si in FAM[vi]))
FAMTOT = sum(FAMN)

# ------------------------------------------------------------------
# 11. the group action on cuttings, and the equal split
# ------------------------------------------------------------------

CSET = set()
for s in CUT:
    v = 0
    for i in s:
        v |= 1 << i
    CSET.add(v)
BADACT = 0
for g in range(NG):
    pc = GPC[g]
    PB = [1 << pc[i] for i in range(NPI)]
    look = PB.__getitem__
    if sorted(pc) != list(range(NPI)):
        BADACT += 1
        continue
    for s in CUT:
        if sum(map(look, s)) not in CSET:
            BADACT += 1

SPL = []
SPLOK = True
for t in "BCD":
    oi = RANK[TAGS.index(t)]
    q, rm = divmod(PURC[t], OSZ[TAGS.index(t)])
    SPL.append((PURC[t], OSZ[TAGS.index(t)], q))
    if rm != 0 or q != OCB[TAGS.index(t)] or PURC[t] != TOTC[t]:
        SPLOK = False
SPLS = " ".join(f"{nd(a)}/{nd(b)} = {nd(c)}" for (a, b, c) in SPL)
SPLM = " ".join(nd(OCB[TAGS.index(t)]) for t in "BCD")

# ------------------------------------------------------------------
# 12. the closed form for the subgroup families
# ------------------------------------------------------------------

ALLR = (1 << 24) - 1
CHOICE = []
CONS = []
COMPS = []
CTOT = []
for vi in range(3):
    V = VS[vi]
    phi = dict((k, dict((p, 0 if FB[k][p] in V else 1) for p in FB[k])) for k in range(NCL))
    subs = []

    def choose(start, ch, c1, c2):
        if len(ch) == 6:
            if c2 == ALLR and c1 == 0:
                subs.append(tuple(ch))
            return
        if NCL - start < 6 - len(ch):
            return
        for k in range(start, NCL):
            m = SHM[k]
            if m & c2:
                continue
            ch.append(k)
            choose(k + 1, ch, c1 ^ m, c2 | (m & c1))
            ch.pop()

    choose(0, [], 0, 0)
    tot = 0
    good = 0
    comps = set()
    for sub in subs:
        adj = dict((k, []) for k in sub)
        for r in range(24):
            a, b = [k for k in sub if (SHM[k] >> r) & 1]
            e = (phi[a][PERMS[r]] + phi[b][PERMS[r]] + 1) & 1
            adj[a].append((b, e))
            adj[b].append((a, e))
        col = {}
        nc = 0
        okc = True
        for k in sub:
            if k in col:
                continue
            nc += 1
            st = [(k, 0)]
            while st:
                v, c = st.pop()
                if v in col:
                    if col[v] != c:
                        okc = False
                    continue
                col[v] = c
                for w, e in adj[v]:
                    st.append((w, c ^ e))
        if okc:
            good += 1
            comps.add(nc)
            tot += 1 << nc
    CHOICE.append(len(subs))
    CONS.append(good)
    COMPS.append(sorted(comps))
    CTOT.append(tot)
CFOK = (CTOT == FAMN and CONS == [12, 12, 12] and COMPS == [[1], [1], [1]])

# ------------------------------------------------------------------
# 13. the sign characters and their exact kernels
# ------------------------------------------------------------------


def sgc(w, m):
    """the sign character w evaluated on a mask, over the first three bits"""
    return ((w & 1) & (m & 1)) ^ (((w >> 1) & 1) & ((m >> 1) & 1)) ^ (((w >> 2) & 1) & ((m >> 2) & 1))


PHIOK = (len(set((m & 1, (m >> 1) & 1, (m >> 2) & 1) for m in EV)) == 8)


def zkernel(A):
    """the saturated integer kernel of A, by fraction-free row reduction of the transpose beside the identity"""
    n = len(A)
    m = len(A[0])
    B = [[A[i][j] for i in range(n)] + [1 if jj == j else 0 for jj in range(m)]
         for j in range(m)]
    rr = 0
    for col in range(n):
        while True:
            p = -1
            for i in range(rr, m):
                if B[i][col] != 0 and (p < 0 or abs(B[i][col]) < abs(B[p][col])):
                    p = i
            if p < 0:
                break
            B[rr], B[p] = B[p], B[rr]
            pv = B[rr][col]
            done = True
            for i in range(rr + 1, m):
                if B[i][col] != 0:
                    q = B[i][col] // pv
                    if q:
                        B[i] = [a - q * b for a, b in zip(B[i], B[rr])]
                    if B[i][col] != 0:
                        done = False
            if done:
                rr += 1
                break
    return [row[n:] for row in B if not any(row[:n])]


def tobits(v):
    x = 0
    for i, a in enumerate(v):
        if a & 1:
            x |= 1 << i
    return x


def ech(vs):
    """the fully reduced echelon basis of a mod-two space, canonical for the space it spans"""
    b = []
    for x in vs:
        for c in b:
            h = c.bit_length() - 1
            if (x >> h) & 1:
                x ^= c
        if x:
            b.append(x)
            b.sort(reverse=True)
    for i in range(len(b) - 1, -1, -1):
        h = b[i].bit_length() - 1
        for j in range(i):
            if (b[j] >> h) & 1:
                b[j] ^= b[i]
    return sorted(b, reverse=True)


def red(b, x):
    for c in b:
        h = c.bit_length() - 1
        if (x >> h) & 1:
            x ^= c
    return x


def inter2(U, V):
    """the intersection of two mod-two spaces, by tracking the combinations whose residue dies"""
    e = []
    out = []
    for u in U:
        r = red(V, u)
        v = u
        for (r2, v2) in e:
            h = r2.bit_length() - 1
            if r and ((r >> h) & 1):
                r ^= r2
                v ^= v2
        if r == 0:
            if v:
                out.append(v)
        else:
            e.append((r, v))
            e.sort(key=lambda z: -z[0])
    return ech(out)


SP = {}
KDIM = []
SATOK = True
for w in range(1, 8):
    A = []
    for r in range(24):
        row = [0] * NCL
        for k in CLAT[r]:
            row[k] = -1 if sgc(w, FB[k][PERMS[r]]) else 1
        A.append(row)
    K = zkernel(A)
    sp = ech([tobits(v) for v in K])
    if len(sp) != len(K):
        SATOK = False
    SP[w] = sp
    KDIM.append(len(sp))
KDS = " ".join(nd(x) for x in sorted(KDIM, reverse=True))

A0 = []
for r in range(24):
    row = [0] * NCL
    for k in CLAT[r]:
        row[k] = 1
    A0.append(row)
B0 = [[A0[i][j] for i in range(24)] + [1 if jj == j else 0 for jj in range(NCL)]
      for j in range(NCL)]
rr = 0
for col in range(24):
    p = -1
    for i in range(rr, NCL):
        if B0[i][col] & 1:
            p = i
            break
    if p < 0:
        continue
    B0[rr], B0[p] = B0[p], B0[rr]
    for i in range(NCL):
        if i != rr and (B0[i][col] & 1):
            B0[i] = [(a ^ b) & 1 for a, b in zip(B0[i], B0[rr])]
    rr += 1
SP0 = ech([tobits(row[24:]) for row in B0 if not any(x & 1 for x in row[:24])])

FULLI = list(SP0)
for w in range(1, 8):
    FULLI = inter2(FULLI, SP[w])
CONLY = list(SP[1])
for w in range(2, 8):
    CONLY = inter2(CONLY, SP[w])
DROPOK = True
for w0 in range(1, 8):
    c = list(SP0)
    for w in range(1, 8):
        if w != w0:
            c = inter2(c, SP[w])
    if c != FULLI:
        DROPOK = False
IMPL = (CONLY == FULLI)


def spanof(b):
    a = [0]
    for x in b:
        a = a + [y ^ x for y in a]
    return a


EMSK = 0
for P in range(NPOS):
    EMSK |= 1 << (2 * P)


def nonconst(vecs):
    bad = 0
    for p in vecs:
        e = (p ^ (p >> 1)) & EMSK
        if e != 0 and e != EMSK:
            bad += 1
    return bad


PSTAR = spanof(FULLI)
NPS = len(PSTAR)
NCONST = nonconst(PSTAR)
PS = set(PSTAR)
SEEN = set()
ALLIN = True
for s in CUT:
    n = [0] * NCL
    for i in s:
        n[KOF[i]] += 1
    p = tobits(n)
    SEEN.add(p)
    if p not in PS:
        ALLIN = False
NSEEN = len(SEEN)

# ------------------------------------------------------------------
# 14. the rejectors
# ------------------------------------------------------------------

L1 = spanof(SP0)
NL1 = len(L1)
NL1BAD = nonconst(L1)
REJ1 = (len(SP0) == 18 and NL1BAD > 0 and NL1BAD < NL1)
REJ2 = (len(PUR) < NS and PURC.get("A", 0) < TOTC["A"])

# ------------------------------------------------------------------
# 15. gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NPTS == 625 and GENERIC, "K1",
     f"cell: {nd(NCAND)} candidate five-corner unit-determinant pieces, {nd(NKEPT)} kept at adjacency cost floor {nd(FLOOR)},"
     f" {nd(NPTS)} generic sample points")

gate(NS == 15800 and SIZES == [24] and NPI == 192 and BADP == 0 and NPER == [2]
     and len(NAMES) == 384 and DEALOK == NPI, "K2",
     f"cuttings: {nd(NS)} exact covers by {nd(SIZES[0])} pieces, used pieces {nd(NPI)}, each cutting meets every chamber once,"
     f" failures {nd(BADP)}")

gate(NCH == 192 and INCN == [8] and HOLDN == [8] and NG == 384 and ACTOK and FREE
     and NEL == 192 and BADDICT == 0, "K3",
     f"chambers {nd(NCH)}, {nd(INCN[0])} per piece and {nd(HOLDN[0])} per chamber: the order-{nd(NG)} cell group acts freely and"
     f" transitively, even-mask subgroup {nd(24)} x {nd(8)} = {nd(NEL)}")

gate(GRAPH and NPOS == 12 and PERPOS == [16] and NCL == 24 and CLSZ == [8]
     and TPERP == [2] * NPOS and ORBSZ == [8] and BADTR == 0 and BADMC == 0
     and LAWBAD == 0 and len(CLM) == NPI and ATR == [8], "K4",
     f"tiles: every used piece is the graph of a function, positions {nd(NPOS)}, {nd(PERPOS[0])} pieces each in {nd(TPERP[0])} types,"
     f" classes {nd(NCL)} of {nd(CLSZ[0])}, value law failures {nd(LAWBAD)}")

gate(len(P25) == 25 and OSZ == [1, 6, 3, 3, 6, 6] and OCB == [9368, 944, 160, 24, 20, 16]
     and OKORB and BADPA == 0 and WTOT == NS, "K5",
     f"census: {nd(len(P25))} realized profiles in {nd(len(ORBS))} orbits, per-profile count by orbit size {CBASE},"
     f" weighted total {nd(WTOT)}")

emit(f"the three mask subgroups that hold the all-axes flip {nd(FLIP)}: {VSTR[0]} and {VSTR[1]} and {VSTR[2]}")

gate(BASEF and VSUB == [] and VCT == {0: 8, 1: 8, 2: 8} and len(VOF) == NCL, "K6",
     f"base fact: every class offset image lies inside exactly one of those three subgroups, class split {VSPL},"
     f" classes {nd(len(VOF))}")

gate(len(AFF) == 43 and AFFN == {2: 28, 4: 14, 8: 1} and NBLK == 1032, "K7",
     f"blocks: affine mask subsets per class {nd(len(AFF))} = {nd(AFFN[2])} pairs + {nd(AFFN[4])} four-element cosets"
     f" + {nd(AFFN[8])} whole group, total {nd(NBLK)}")

gate(NBP == 1224 and BADBP == 0 and BPDIST == NBP, "K8",
     f"block partitions: {nd(NBP)} found by exact cover with at most one block per class, every one of them a cutting,"
     f" distinct {nd(BPDIST)}")

gate(len(PUR) == 1224 and SETEQ and NBP == len(PUR), "K9",
     f"purity: coset-pure cuttings among the {nd(NS)} number {nd(len(PUR))}, and that set equals the block partitions"
     f" in both directions")

gate(PURC == {"B": 72, "C": 120, "D": 96, "A": 144, "U": 792}
     and TOTC == {"B": 72, "C": 120, "D": 96, "A": 480, "U": 9368, "O": 5664}, "K10",
     f"class content of the {nd(len(PUR))} coset-pure cuttings: {CONT}")

gate(BADACT == 0 and OKORB and sum(OSZ) == len(P25) and len(ORBS) == 6, "K11",
     f"action: all {nd(NG)} elements carry all {nd(NS)} cuttings to cuttings, the {nd(len(ORBS))} profile orbits cover"
     f" the {nd(len(P25))} profiles with a constant count on each")

gate(SPLOK and [c for (a, b, c) in SPL] == [24, 20, 16], "K12",
     f"equal split: {SPLS}, matching the measured per-profile counts {SPLM} of the three small classes")

gate(FAMN == [24, 24, 24] and FAMTAG == ["C"] and FAMTOT == 72 and TOTC["C"] == 120, "K13",
     f"families: per subgroup {' '.join(nd(x) for x in FAMN)} cuttings whose class mask sets are all cosets of it, every one in class"
     f" {FAMTAG[0]}, {nd(3)} x {nd(FAMN[0])} = {nd(FAMTOT)} of {nd(TOTC['C'])}")

gate(CFOK and CHOICE == [512, 512, 512], "K14",
     f"closed form: two-covering six-class choices {nd(CHOICE[0])}, of which {nd(CONS[0])} admit a consistent colouring,"
     f" each in {nd(COMPS[0][0])} part, {nd(CONS[0])} x {nd(2)} = {nd(CTOT[0])} = the family")

emit(f"characters: dropping any one of the seven leaves the intersection unchanged, and the character-only intersection is already that space")

gate(sorted(KDIM) == [9, 9, 9, 9, 12, 12, 12] and len(FULLI) == 7 and NPS == 128
     and NCONST == 0 and ALLIN and NSEEN == 124 and DROPOK and IMPL and SATOK
     and PHIOK, "K15",
     f"parity: kernel dimensions {KDS}, intersection dimension {nd(len(FULLI))}, {nd(NPS)} vectors, none parity-mixed,"
     f" {nd(NS)} realized inside, distinct {nd(NSEEN)}")

gate(REJ1 and NL1 == 262144 and NL1BAD == 253952 and REJ2, "K16",
     f"rejectors: level-one alone has dimension {nd(len(SP0))}, {nd(NL1)} vectors, {nd(NL1BAD)} parity-mixed;"
     f" purity is not universal, {nd(len(PUR))} under {nd(NS)}, {nd(PURC['A'])} under {nd(TOTC['A'])}")

emit(f"TOTAL: PASS={nd(STAT[0])} FAIL={nd(STAT[1])}")

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
SECS = int(time.time() - T0)
emit(f"resource: under {nd(((SECS // 60) + 1) * 60)} s of the {nd(900)} s budget, under {nd(((PEAK // 250) + 1) * 250)} MB"
     f" of the {nd(2500)} MB budget, {nd(OUT[0])} characters")

sys.exit(0 if STAT[1] == 0 else 1)
