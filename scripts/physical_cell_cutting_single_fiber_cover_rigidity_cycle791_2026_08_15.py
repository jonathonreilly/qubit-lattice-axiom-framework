"""Physical cell cutting: the whole symmetry group of one wall fiber's cover instance, the refuted free involution, and the empty geometry.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, the slot-preserving subgroup of order ninety-six for axis zero, and the sixteen-letter facet alphabet. Nothing outside
that finite object enters any gate.

The previous cycle counted globally and found the parity carrier of the fold-held set one axis too coarse: the side flip pairs the eight
served fibers across, never within. This cycle drops to a single fiber. Its 14 fold-held cuttings become 12-subsets of two-orbit rows, and
the question is the whole symmetry of that cover instance: the kernel that moves rows inside membership classes, the group induced on the
14 solutions, whether any induced element is a free involution, and whether any of them is carried by a permutation of the sample points.

Gates G1 to G12, one line each with a few detail lines, then a resource line and the total line. Any failure exits nonzero."""

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


def pshow(v):
    return " ".join("({0},{1})".format(a, b) for (a, b) in v)


def gshow(v):
    return " ".join("({0},{1},{2},{3})/{4}".format(g[0][0], g[0][1], g[0][2], g[0][3], g[1]) for g in v)


def popc(x):
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
NK = len(KEPT)

P4 = list(itertools.permutations(range(4)))
G384 = [(p, m) for p in P4 for m in range(16)]

FACE = {}
for t in range(NK):
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
    ps = tuple(KN[frozenset(frozenset(act3(g, v) for v in tt) for tt in ALLK[li])] for li in range(16))
    if sorted(ps) != list(range(16)):
        PBAD += 1
    PSI[g] = ps


def compose(a, b):
    p, m = a
    q, n = b
    r = tuple(q[p[i]] for i in range(4))
    k = n
    for j in range(4):
        if (m >> j) & 1:
            k ^= (1 << q[j])
    return (r, k)


def piecemap(g, dom):
    return dict((t, KIDX[frozenset(actcorner(g, v) for v in KEPT[t])]) for t in dom)


def cycen(sig):
    seen = set()
    cc = Counter()
    for i in range(len(sig)):
        if i in seen:
            continue
        x, n = i, 0
        while True:
            seen.add(x)
            x = sig[x]
            n += 1
            if x == i:
                break
        cc[n] += 1
    return dict(sorted(cc.items()))


# ================================================================ G1 the declared object and the composition rule

IDXA = (0, 5, 17, 33, 64, 97, 128, 150, 191, 200, 233, 255, 260, 288, 300, 319, 340, 355, 370, 383)
IDXB = (383, 370, 355, 340, 319, 300, 288, 260, 255, 233, 200, 191, 150, 128, 97, 64, 33, 17, 5, 0)
CBAD = 0
for i in range(len(IDXA)):
    ca, cb = G384[IDXA[i]], G384[IDXB[i]]
    cc = compose(ca, cb)
    for v in range(len(CORN)):
        if actcorner(cc, v) != actcorner(ca, actcorner(cb, v)):
            CBAD += 1

gate(len(CAND) == 2672 and FLOOR == 6 and NK == 400 and NS == 15800 and PSIZE == 1 and CSIZE == 24 and NU == 192
     and len(G384) == 384 and len(STAB) == 96 and PBAD == 0 and CBAD == 0 and len(IDXA) == 20, "G1",
     "{0} pieces, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, cell group {6}, slot subgroup {7}, {8} composition pairs clean"
     .format(len(CAND), FLOOR, NK, NS, CSIZE, NU, len(G384), len(STAB), len(IDXA)))

# ================================================================ G2 the alphabet and the wall

MULT = [Counter(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
NSLOT = len(MULT)
MSAME = all(m == MULT[0] for m in MULT)
MCEN = dict(sorted(Counter(MULT[0].values()).items()))
PAIROF = [(KEY[i][(0, 0)], KEY[i][(0, 1)]) for i in range(NS)]
JC = Counter(PAIROF)
TR = [[JC[(x, y)] for y in range(NL)] for x in range(NL)]
TRC = sum(TR[x][x] for x in range(NL))
N36 = sum(1 for x in range(NL) for y in range(NL) if TR[x][y] == 36)
FIB = {}
for i in range(NS):
    FIB.setdefault(PAIROF[i], []).append(i)
E36 = sorted(kj for kj in FIB if TR[kj[0]][kj[1]] == 36)
FSZ = sorted(set(len(FIB[kj]) for kj in E36))
NF = len(E36)
WSZ = FSZ[0]

gate(NL == 16 and MSAME and NSLOT == 8 and MCEN == {862: 12, 1364: 4} and TRC == 2000
     and N36 == 48 and NF == 48 and FSZ == [36], "G2",
     "{0} letters on each of {1} slots, multiplicity census {2}, trace {3}, {4} entries at {5}, {6} fibers of {5} cuttings"
     .format(NL, NSLOT, dshow(MCEN), TRC, N36, WSZ, NF))

# ================================================================ G3 the folds and the sample fiber

FL = [FIB[kj] for kj in E36]
FS = [set(F) for F in FL]
WALL = sorted(set(c for F in FL for c in F))
POSW = {c: i for i, c in enumerate(WALL)}
FOLD = [None] * NF
STCNT = [0] * NF
DEFECT = 0
for g in G384:
    mp = piecemap(g, USED)
    if len(set(mp.values())) != NU:
        DEFECT += 1
    img = [SIDX[frozenset(mp[t] for t in SOLS[c])] for c in WALL]
    for f in range(NF):
        S = FS[f]
        ok = True
        for c in FL[f]:
            if img[POSW[c]] not in S:
                ok = False
                break
        if ok:
            STCNT[f] += 1
            if g != GID:
                FOLD[f] = g

DIST = sorted(set(FOLD))
SERVE = dict(sorted(Counter(Counter(FOLD).values()).items()))
GREP = ((0, 3, 2, 1), 15)
MPK = piecemap(GREP, range(NK))
GPM = [SIDX[frozenset(MPK[t] for t in s)] for s in SOLS]
NFIX = sum(1 for c in range(NS) if GPM[c] == c)
GFIBS = [f for f in range(NF) if FOLD[f] == GREP]
REPF = GFIBS[0]
RPAIR = E36[REPF]
R14 = [c for c in FL[REPF] if GPM[c] == c]
NH = len(R14)

gate(DEFECT == 0 and set(STCNT) == set([2]) and len(DIST) == 6 and SERVE == {8: 6} and GREP in DIST
     and NFIX == 336 and NH == 14 and len(FL[REPF]) == 36, "G3",
     "the {0} fiber folds are {1} distinct maps, census {2}; the sample fold holds {3} of the {4} cuttings"
     .format(NF, len(DIST), dshow(SERVE), NFIX, NS))
emit("G3 detail: the six folds are {0}".format(gshow(DIST)))
emit("G3 detail: the sample fiber has letter pair {0} and the fold holds {1} of its {2} cuttings"
     .format(pshow([RPAIR]), NH, len(FL[REPF])))

# ================================================================ G4 the fiber instance as two-orbit rows

ORBS = []
SING = 0
OVL = 0
SEEN = set()
for t in range(NK):
    if t in SEEN:
        continue
    u = MPK[t]
    SEEN.add(t)
    SEEN.add(u)
    if u == t:
        SING += 1
    if MASK[t] & MASK[u]:
        OVL += 1
    ORBS.append((t, u))
OIDX = {}
for i in range(len(ORBS)):
    OIDX[ORBS[i][0]] = i
    OIDX[ORBS[i][1]] = i

RAW = []
UNOK = 0
for c in R14:
    s = set(SOLS[c])
    rr = frozenset(OIDX[t] for t in s)
    if all(ORBS[i][0] in s and ORBS[i][1] in s for i in rr):
        UNOK += 1
    RAW.append(rr)
RSIZE = sorted(set(len(r) for r in RAW))
ROWG = sorted(set().union(*RAW))
NR = len(ROWG)
RPOS = {r: i for i, r in enumerate(ROWG)}
SR = [frozenset(RPOS[r] for r in RAW[i]) for i in range(NH)]
FREQ = dict(sorted(Counter(sum(1 for i in range(NH) if r in SR[i]) for r in range(NR)).items()))
WSUM = sum(k * v for k, v in FREQ.items())

gate(len(ORBS) == 200 and SING == 0 and OVL == 0 and UNOK == NH and RSIZE == [12] and NR == 40
     and FREQ == {1: 6, 2: 10, 3: 2, 4: 7, 6: 9, 8: 3, 10: 3} and WSUM == 168, "G4",
     "the {0} kept pieces give {1} two-orbits, no singleton and no overlap; each held cutting is {2} of them, {3} rows occur"
     .format(NK, len(ORBS), RSIZE[0], NR))
emit("G4 detail: occurrence census over the {0} rows {1}, weighted sum {2} equal to {3} times {4}"
     .format(NR, dshow(FREQ), WSUM, NH, RSIZE[0]))

# ================================================================ G5 the pairwise structure of the fourteen

MEET = Counter()
SDIF = Counter()
IDOK = 0
NPAIR = 0
for i, j in itertools.combinations(range(NH), 2):
    m = len(SR[i] & SR[j])
    d = len(SR[i] ^ SR[j])
    MEET[m] += 1
    SDIF[d] += 1
    NPAIR += 1
    if d == 24 - 2 * m:
        IDOK += 1
MCEN5 = dict(sorted(MEET.items()))
SCEN5 = dict(sorted(SDIF.items()))

gate(NPAIR == 91 and IDOK == 91 and MCEN5 == {0: 12, 1: 6, 2: 10, 3: 14, 4: 4, 5: 14, 6: 4, 7: 5, 8: 10, 9: 1, 10: 11}
     and SCEN5 == {4: 11, 6: 1, 8: 10, 10: 5, 12: 4, 14: 14, 16: 4, 18: 14, 20: 10, 22: 6, 24: 12}, "G5",
     "the {0} solution pairs meet in row counts with census {1}".format(NPAIR, dshow(MCEN5)))
emit("G5 detail: symmetric difference census {0}".format(dshow(SCEN5)))
emit("G5 detail: the identity 24 minus twice the meet holds on every one of the {0} pairs".format(IDOK))

# ================================================================ G6 the membership classes

MEM = {}
for r in range(NR):
    key = frozenset(i for i in range(NH) if r in SR[i])
    MEM.setdefault(key, []).append(r)
CLS = sorted(MEM.items(), key=lambda kv: (len(kv[1]), sorted(kv[0]), kv[1][0]))
NC = len(CLS)
CMASK = []
CROW = []
for key, rowl in CLS:
    mm = 0
    for i in key:
        mm |= (1 << i)
    CMASK.append(mm)
    CROW.append(sorted(rowl))
CSZ = [len(v) for v in CROW]
CCEN = dict(sorted(Counter(CSZ).items()))

gate(NC == 20 and CCEN == {1: 6, 2: 10, 3: 2, 4: 2} and sum(CSZ) == NR and len(set(CMASK)) == NC, "G6",
     "the {0} rows fall into {1} classes of equal membership, size census {2}, sizes summing to {0}, all memberships distinct"
     .format(NR, NC, dshow(CCEN)))

# ================================================================ G7 the kernel that moves rows inside classes

TWOC = [c for c in range(NC) if CSZ[c] == 2][0]
SWAP = list(range(NR))
u, v = CROW[TWOC][0], CROW[TWOC][1]
SWAP[u], SWAP[v] = v, u
KFIX = sum(1 for i in range(NH) if frozenset(SWAP[r] for r in SR[i]) == SR[i])
FAC = {}
for s in sorted(set(CSZ)):
    f = 1
    for k in range(2, s + 1):
        f *= k
    FAC[s] = f ** CCEN[s]
KORD = 1
for s in FAC:
    KORD *= FAC[s]

gate(KFIX == NH and FAC[2] == 1024 and FAC[3] == 36 and FAC[4] == 576 and KORD == 21233664, "G7",
     "a swap inside one size-{0} class holds all {1} solutions as row sets; the kernel order is {2} times {3} times {4} equal to {5}"
     .format(2, NH, FAC[2], FAC[3], FAC[4], KORD))

# ================================================================ G8 the group induced on the fourteen solutions

CPOP = [popc(m) for m in CMASK]
BYSIG = {}
for c in range(NC):
    BYSIG.setdefault((CSZ[c], CPOP[c]), []).append(CMASK[c])
NODE = [0]
IND = []


def okpart(A, B):
    for c in range(NC):
        a, b = A[c], B[c]
        good = False
        for mm in BYSIG[(CSZ[c], CPOP[c])]:
            if (a & ~mm) == 0 and (b & mm) == 0:
                good = True
                break
        if not good:
            return False
    return True


def bt(k, sig, used, A, B):
    NODE[0] += 1
    if k == NH:
        IND.append(tuple(sig))
        return
    for w in range(NH):
        if used & (1 << w):
            continue
        bit = 1 << w
        A2 = [A[c] | bit if (CMASK[c] >> k) & 1 else A[c] for c in range(NC)]
        B2 = [B[c] if (CMASK[c] >> k) & 1 else B[c] | bit for c in range(NC)]
        if not okpart(A2, B2):
            continue
        sig.append(w)
        bt(k + 1, sig, used | bit, A2, B2)
        sig.pop()


bt(0, [], 0, [0] * NC, [0] * NC)
IDS = tuple(range(NH))
NONT = [s for s in IND if s != IDS]
NTC = cycen(NONT[0]) if NONT else {}
TWOCYC = sorted((i, NONT[0][i]) for i in range(NH) if NONT and NONT[0][i] != i and i < NONT[0][i])
FREEI = sum(1 for s in IND if cycen(s) == {2: 7})


def classimg(sig, c):
    im = 0
    mm = CMASK[c]
    for i in range(NH):
        if (mm >> i) & 1:
            im |= (1 << sig[i])
    return im


def rowmap(sig):
    tgt = []
    for c in range(NC):
        im = classimg(sig, c)
        cand = [d for d in range(NC) if CMASK[d] == im and CSZ[d] == CSZ[c]]
        if len(cand) != 1:
            return None
        tgt.append(cand[0])
    if sorted(tgt) != list(range(NC)):
        return None
    phi = [-1] * NR
    for c in range(NC):
        for a, b in zip(CROW[c], CROW[tgt[c]]):
            phi[a] = b
    return phi


def leafok(sig):
    A = [0] * NC
    B = [0] * NC
    for k in range(NH):
        bit = 1 << sig[k]
        for c in range(NC):
            if (CMASK[c] >> k) & 1:
                A[c] |= bit
            else:
                B[c] |= bit
    return okpart(A, B)


BUILT = 0
PHI = {}
for s in IND:
    ph = rowmap(s)
    if ph is None or sorted(ph) != list(range(NR)):
        continue
    if all(frozenset(ph[r] for r in SR[i]) == SR[s[i]] for i in range(NH)):
        BUILT += 1
    PHI[s] = ph
NEAR = 0
if len(TWOCYC) == 2:
    for (x, y) in TWOCYC:
        tp = list(range(NH))
        tp[x], tp[y] = y, x
        if not leafok(tuple(tp)):
            NEAR += 1

gate(len(IND) == 2 and len(NONT) == 1 and NTC == {1: 10, 2: 2} and FREEI == 0 and BUILT == 2 and NEAR == 2, "G8",
     "the complete backtracking over all permutations of the {0} solutions leaves {1} induced maps, the nontrivial one of cycle census {2}"
     .format(NH, len(IND), dshow(NTC)))
emit("G8 detail: its two-cycles are {0}; free involutions of census {1} number {2}; both survivors realized by an explicit row bijection"
     .format(pshow(TWOCYC), dshow({2: 7}), FREEI))
emit("G8 detail: the search visited {0} partial maps; each lone two-cycle of the survivor fails the class condition, {1} of {1} rejected"
     .format(NODE[0], NEAR))

# ================================================================ G9 the whole symmetry group of the instance

WORD = len(IND) * KORD
SQ = tuple(NONT[0][NONT[0][i]] for i in range(NH))
PH2 = [PHI[NONT[0]][PHI[NONT[0]][r]] for r in range(NR)]
SQOK = all(frozenset(PH2[r] for r in SR[i]) == SR[i] for i in range(NH))

gate(WORD == 42467328 and len(IND) * KORD == WORD and SQ == IDS and SQOK, "G9",
     "the whole group of row maps preserving the system has order {0} times {1} equal to {2}, and the survivor squares into the kernel"
     .format(len(IND), KORD, WORD))

# ================================================================ G10 the geometric support of the symmetry

SUP = [MASK[ORBS[ROWG[i]][0]] | MASK[ORBS[ROWG[i]][1]] for i in range(NR)]
SSZ = [popc(x) for x in SUP]
INT = [[popc(SUP[i] & SUP[j]) for j in range(NR)] for i in range(NR)]
PAT = []
for p in range(NPTS):
    q = 0
    for i in range(NR):
        if (SUP[i] >> p) & 1:
            q |= (1 << i)
    PAT.append(q)
PATC = Counter(PAT)
NPAT = len(PATC)
BARE = PATC.get(0, 0)
ORDC = sorted(range(NC), key=lambda c: (CSZ[c], c))


def relab(q, ph):
    o = 0
    for i in range(NR):
        if (q >> i) & 1:
            o |= (1 << ph[i])
    return o


def realizations(sig):
    tgt = []
    for c in range(NC):
        im = classimg(sig, c)
        tgt.append([d for d in range(NC) if CMASK[d] == im][0])
    slots = []
    for c in ORDC:
        for r in CROW[c]:
            slots.append((r, CROW[tgt[c]]))
    n = len(slots)
    surv = []
    cnt = [0, 0]

    def rec(k, asg, taken):
        cnt[0] += 1
        if k == n:
            cnt[1] += 1
            ph = [-1] * NR
            for (a, b) in asg:
                ph[a] = b
            for q in PATC:
                if PATC.get(relab(q, ph), -1) != PATC[q]:
                    return
            surv.append(list(ph))
            return
        src, cands = slots[k]
        for t in cands:
            if taken & (1 << t):
                continue
            if SSZ[t] != SSZ[src]:
                continue
            good = True
            for (a, b) in asg:
                if INT[src][a] != INT[t][b]:
                    good = False
                    break
            if not good:
                continue
            asg.append((src, t))
            rec(k + 1, asg, taken | (1 << t))
            asg.pop()

    rec(0, [], 0)
    return surv, cnt


RID, CID = realizations(IDS)
RNT, CNT = realizations(NONT[0])
IDENT = len(RID) == 1 and RID[0] == list(range(NR))

gate(NPAT == 68 and BARE == 0 and len(RID) == 1 and IDENT and len(RNT) == 0, "G10",
     "the {0} rows cut the {1} sample points into {2} incidence patterns; the identity has {3} point realization and it is the identity"
     .format(NR, NPTS, NPAT, len(RID)))
emit("G10 detail: the survivor of G8 has {0} realizations, so exactly {1} of the {2} row maps is carried by a point permutation"
     .format(len(RNT), len(RID), WORD))
emit("G10 detail: the two searches over class-respecting row bijections visited {0} and {1} partial maps, reaching {2} and {3} leaves"
     .format(CID[0], CNT[0], CID[1], CNT[1]))

# ================================================================ G11 the native re-derivation of the fourteen

OTH = [c for c in FL[REPF] if GPM[c] != c]
UNI = 0
for c in OTH:
    s = set(SOLS[c])
    if all(ORBS[OIDX[t]][0] in s and ORBS[OIDX[t]][1] in s for t in s):
        UNI += 1
OM = [MASK[a] | MASK[b] for (a, b) in ORBS]
OBY = [[] for _ in range(NPTS)]
for i in range(len(ORBS)):
    mm = OM[i]
    while mm:
        low = mm & (-mm)
        OBY[low.bit_length() - 1].append(i)
        mm ^= low
QS = []


def qsearch(cov, ch):
    if cov == UNIV:
        QS.append(tuple(ch))
        return
    fr = UNIV & (~cov)
    p = (fr & (-fr)).bit_length() - 1
    for i in OBY[p]:
        m = OM[i]
        if m & cov:
            continue
        ch.append(i)
        qsearch(cov | m, ch)
        ch.pop()


qsearch(0, [])
QSZ = sorted(set(len(s) for s in QS))
QP = [frozenset(x for i in s for x in ORBS[i]) for s in QS]


def pairof(ps):
    return tuple(KN.get(frozenset(FACE[(t, 0, c)] for t in ps if (t, 0, c) in FACE), -1) for c in (0, 1))


FILT = [q for q in QP if pairof(q) == RPAIR]
SAME = set(FILT) == set(CSET[c] for c in R14)

gate(UNI == 0 and len(OTH) == 22 and len(QS) == 336 and QSZ == [12] and len(FILT) == NH and SAME
     and len(set(QP)) == len(QP), "G11",
     "none of the fiber's other {0} cuttings is a union of two-orbits; the native cover of the {1} points has {2} solutions of {3}"
     .format(len(OTH), NPTS, len(QS), QSZ[0]))
emit("G11 detail: filtering those by the letter pair {0} leaves {1}, equal as piece sets to the fold-held cuttings of the sample fiber"
     .format(pshow([RPAIR]), len(FILT)))

# ================================================================ G12 the cell group cannot see the survivor

POS14 = {c: i for i, c in enumerate(R14)}
S14 = set(R14)
HOLD = []
HID = 0
HNT = 0
for g in G384:
    mp = piecemap(g, USED)
    im = [SIDX[frozenset(mp[t] for t in SOLS[c])] for c in R14]
    if set(im) == S14:
        HOLD.append(g)
        sig = tuple(POS14[im[i]] for i in range(NH))
        if sig == IDS:
            HID += 1
        if sig == NONT[0]:
            HNT += 1

gate(len(HOLD) == 2 and HOLD == [GID, GREP] and HID == 2 and HNT == 0, "G12",
     "of the {0} cell maps exactly {1} hold the fiber's {2} cuttings, both inducing the identity on them, {3} inducing the survivor"
     .format(len(G384), len(HOLD), NH, HNT))

# ================================================================ totals

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
emit("resource: under {0} s, under {1} MB".format(((int(time.time() - T0) // 60) + 1) * 60, ((PEAK // 250) + 1) * 250))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
