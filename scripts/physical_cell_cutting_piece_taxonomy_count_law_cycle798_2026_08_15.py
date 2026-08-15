"""Cycle 798: tree taxonomy of the kept pieces, the derived point-count law, and the two-component wall split (finite checks).

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, the order-384 group of signed coordinate
maps of the cell, the sixteen-letter facet alphabet on the two slots of axis zero, and the interface matrix with its wall entries. Nothing
outside that finite object enters any gate.

The previous cycle counted three things: every kept piece has a point count of five times a unit drawn from the spectrum 1, 3, 7, 14; every
cutting carries the one unit profile 1, 11, 11, 1; and the smallest off-diagonal interface value is carried by two different action orbits of
six unordered letter pairs each. This cycle asks why. Every kept piece is shown to be a tree on its five corners of one of exactly three
degree types, each family is rebuilt by an independent construction and matched, the families are identified with the three orbits of the
cell group, an inequality description read off the tree alone is checked against the barycentric membership at every grid point, and the
point count of a chain or of a hub is shown to be a binomial coefficient of its ascent count or of its hub weight. The chain words are then
paired by the fourth-axis flip, every cutting is shown to carry 24 distinct word classes, and the wall graph is split into its two
components, which separates the two orbits sharing the smallest off-diagonal value.
Gates G1 to G10, one line each with a few detail lines, then the total line. Any failure exits nonzero.
"""

import itertools
import sys
from collections import Counter
from fractions import Fraction as FRA
from math import comb

AUDIT_TIMEOUT_SEC = 900

OUT = [0]


def emit(s):
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    if len(txt) > 148:
        raise ValueError("output line over the length limit")
    OUT[0] += len(txt) + 1
    if OUT[0] >= 5800:
        raise ValueError("output over the character budget")
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
                fq = M[r][c]
                M[r] = [M[r][k] - fq * M[c][k] for k in range(2 * n)]
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
NPTS = RSTEP ** 4


def buildmask(offs):
    """Membership bitmasks of every kept piece on the sample points of one per-axis offset table, by exact integer barycentric tests."""
    axval = [[NSHIFT * k + offs[i] for k in range(RSTEP)] for i in range(4)]
    out = []
    for (v0, Ci) in BARY:
        off = [sum(Ci[i][c] * DIV * v0[c] for c in range(4)) for i in range(4)]
        col = [[[Ci[i][ax] * u for i in range(4)] for u in axval[ax]] for ax in range(4)]
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
        out.append(bits)
    return out


MASK = buildmask(OFFS)
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
FLIPD = ((0, 1, 2, 3), 8)

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

ALLK = sorted({d[k] for d in KEYF for k in d}, key=lambda fz: sorted(sorted(t) for t in fz))
KN = {k: i for i, k in enumerate(ALLK)}
KEY = [{k: KN[v] for k, v in d.items()} for d in KEYF]
NL = len(ALLK)


def actcorner(g, v):
    p, m = g
    x = CORN[v]
    return CIDX[tuple(x[p[i]] ^ ((m >> p[i]) & 1) for i in range(4))]


def piecemap(g, dom):
    return dict((t, KIDX[frozenset(actcorner(g, v) for v in KEPT[t])]) for t in dom)


# ---------------------------------------------- the alphabet, the interface matrix and the wall

PAIROF = [(KEY[i][(0, 0)], KEY[i][(0, 1)]) for i in range(NS)]
JC = Counter(PAIROF)
TRM = [[JC[(x, y)] for y in range(NL)] for x in range(NL)]
TRC = sum(TRM[x][x] for x in range(NL))
N36 = sum(1 for x in range(NL) for y in range(NL) if TRM[x][y] == 36)
FIB = {}
for i in range(NS):
    FIB.setdefault(PAIROF[i], []).append(i)
E36 = sorted(kj for kj in FIB if TRM[kj[0]][kj[1]] == 36)
NF = len(E36)

PSZ = [popc(MASK[t]) for t in range(NK)]
UNIT = [0] * NK
DIVOK = 0
for t in range(NK):
    q, r = divmod(PSZ[t], RSTEP)
    UNIT[t] = q
    if r == 0:
        DIVOK += 1

# ============================================== G1 the declared cell preamble

gate(len(CAND) == 2672 and FLOOR == 6 and NK == 400 and NS == 15800 and PSIZE == 1 and CSIZE == 24 and NU == 192
     and len(G384) == 384 and NL == 16 and TRC == 2000 and N36 == 48 and NF == 48 and DIVOK == NK
     and NPTS == 625 and DIV == 80, "G1",
     "the declared cell rebuilds from the corner list alone: {0} candidate pieces, {1} kept at the floor, {2} cuttings of {3} pieces"
     .format(len(CAND), NK, NS, CSIZE))
emit("G1 detail: declared cell: {0} candidates, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, {6} letters, trace {7}"
     .format(len(CAND), FLOOR, NK, NS, CSIZE, NU, NL, TRC))

# ============================================== G2 the taxonomy, by degree and by independent construction


def edges_of(t):
    """The corner-adjacency edges of kept piece t: its corner pairs at coordinate distance one."""
    S = KEPT[t]
    return [(a, b) for a, b in itertools.combinations(S, 2)
            if sum(abs(CORN[a][r] - CORN[b][r]) for r in range(4)) == 1]


DEGT = {(1, 1, 2, 2, 2): 0, (1, 1, 1, 2, 3): 1, (1, 1, 1, 1, 4): 2}
ADJ = []
CLS = []
NE4 = 0
CONN = 0
for t in range(NK):
    E = edges_of(t)
    if len(E) == 4:
        NE4 += 1
    ad = dict((v, []) for v in KEPT[t])
    for a, b in E:
        ad[a].append(b)
        ad[b].append(a)
    seen = set([KEPT[t][0]])
    stack = [KEPT[t][0]]
    while stack:
        v = stack.pop()
        for u in ad[v]:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    if len(seen) == 5:
        CONN += 1
    ADJ.append(ad)
    CLS.append(DEGT.get(tuple(sorted(len(ad[v]) for v in KEPT[t])), -1))

FAMA = [set(frozenset(KEPT[t]) for t in range(NK) if CLS[t] == f) for f in range(3)]
CENA = Counter(CLS)

BCH = set()
NWALK = 0
for c in range(16):
    for order in P4:
        v = c
        S = [v]
        for ax in order:
            v = v ^ (1 << ax)
            S.append(v)
        NWALK += 1
        BCH.add(frozenset(S))
BHB = set(frozenset([c] + [c ^ (1 << a) for a in range(4)]) for c in range(16))
BAR = set()
NARM = 0
for c in range(16):
    for d in range(4):
        for e in range(4):
            if e == d:
                continue
            ab = [x for x in range(4) if x != d and x != e]
            NARM += 1
            BAR.add(frozenset([c, c ^ (1 << ab[0]), c ^ (1 << ab[1]), c ^ (1 << e), c ^ (1 << e) ^ (1 << d)]))
FAMB = [BCH, BAR, BHB]
NBALL = sum(len(FAMB[f]) for f in range(3))
BKEPT = sum(1 for f in range(3) for S in FAMB[f] if S in KIDX)

gate(NE4 == NK and CONN == NK and CENA[-1] == 0 and dict(CENA) == {0: 192, 1: 192, 2: 16}
     and NWALK == 384 and NARM == 192 and [len(FAMB[f]) for f in range(3)] == [192, 192, 16]
     and all(FAMA[f] == FAMB[f] for f in range(3)) and NBALL == NK and BKEPT == NBALL, "G2",
     "each of the {0} kept pieces has exactly {1} corner-adjacency edges on its {2} corners and is connected, so each is a tree"
     .format(NK, 4, 5))
emit("G2 detail: the degree multisets are exactly three: chain {0}, three-arm {1}, hub {2}"
     .format(CENA[0], CENA[1], CENA[2]))
emit("G2 detail: the independent constructions give {0} bit-flip walks with {1} distinct chains, {2} hubs, and {3} three-arm sets"
     .format(NWALK, len(BCH), len(BHB), NARM))
emit("G2 detail: the constructed families equal the degree families as sets, and all {0} constructed sets are kept pieces".format(BKEPT))

# ============================================== G3 the used pieces are exactly the chain family

USEDS = set(frozenset(KEPT[t]) for t in USED)

gate(USEDS == FAMA[0] and len(USEDS) == NU and NU == 192 and len(FAMA[0]) == 192, "G3",
     "the {0} used pieces are exactly the chain family, {0} of {0}: a kept piece occurs in a cutting if and only if its tree is a path"
     .format(NU))

# ============================================== G4 the three families are the three orbits of the cell group

OPAR = list(range(NK))


def findo(a):
    while OPAR[a] != a:
        OPAR[a] = OPAR[OPAR[a]]
        a = OPAR[a]
    return a


for g in G384:
    pmk = piecemap(g, range(NK))
    for t in range(NK):
        ra, rb = findo(t), findo(pmk[t])
        if ra != rb:
            OPAR[ra] = rb
ORB = {}
for t in range(NK):
    ORB.setdefault(findo(t), []).append(t)
OSZ = sorted(len(v) for v in ORB.values())
OMATCH = 0
OCEN = [None] * 3
for mem in ORB.values():
    ms = set(frozenset(KEPT[t]) for t in mem)
    for f in range(3):
        if ms == FAMA[f]:
            OMATCH += 1
            OCEN[f] = Counter(UNIT[t] for t in mem)
ALLU = all(OCEN[f] is not None and sorted(OCEN[f]) == [1, 3, 7, 14] for f in range(3))

gate(len(ORB) == 3 and OSZ == [16, 192, 192] and OMATCH == 3 and ALLU
     and dict(OCEN[0]) == {1: 8, 3: 88, 7: 88, 14: 8} and dict(OCEN[1]) == {1: 14, 3: 82, 7: 82, 14: 14}
     and dict(OCEN[2]) == {1: 2, 3: 6, 7: 6, 14: 2}, "G4",
     "the {0} cell maps carry the {1} kept pieces in exactly {2} orbits, of sizes {3}, and those orbits are the three degree families"
     .format(len(G384), NK, len(ORB), OSZ))
emit("G4 detail: unit census on the chain orbit {0}, on the hub orbit {1}".format(dshow(OCEN[0]), dshow(OCEN[2])))
emit("G4 detail: unit census on the three-arm orbit {0}".format(dshow(OCEN[1])))
emit("G4 detail: every orbit carries all four units, so the unit is constant on no orbit and is not an invariant of the cell group")

# ============================================== G5 the tree-derived inequality description, pointwise

PTS = []
for k0 in range(RSTEP):
    for k1 in range(RSTEP):
        for k2 in range(RSTEP):
            for k3 in range(RSTEP):
                PTS.append(tuple(NSHIFT * k + OFFS[ax] for ax, k in enumerate((k0, k1, k2, k3))))


def xio(pt, ax, bit):
    """The oriented coordinate on axis ax: the point value when the bit is zero and its complement in the scale when the bit is one."""
    return pt[ax] if bit == 0 else DIV - pt[ax]


def walk_of(t):
    """The corner sequence and the step list of a chain, walked from its smaller-indexed degree-one end."""
    ad = ADJ[t]
    ends = sorted(v for v in ad if len(ad[v]) == 1)
    v = ends[0]
    seq = [v]
    prev = -1
    while len(seq) < 5:
        nxt = [u for u in ad[v] if u != prev][0]
        seq.append(nxt)
        prev, v = v, nxt
    steps = []
    for i in range(4):
        ax = (seq[i] ^ seq[i + 1]).bit_length() - 1
        steps.append((ax, (seq[i] >> ax) & 1))
    return seq, steps


def armparts(t):
    """The hub corner, the mid corner, the tip axis and the mid axis of a three-arm piece."""
    ad = ADJ[t]
    c = [v for v in ad if len(ad[v]) == 3][0]
    m = [v for v in ad if len(ad[v]) == 2][0]
    tip = [u for u in ad[m] if u != c][0]
    return c, m, (m ^ tip).bit_length() - 1, (c ^ m).bit_length() - 1


def descmask(t):
    """The membership bitmask of kept piece t read off its tree alone, with no use of the barycentric inverse matrices."""
    bits = 0
    if CLS[t] == 0:
        steps = walk_of(t)[1]
        for p in range(NPTS):
            pt = PTS[p]
            vals = [xio(pt, ax, b) for ax, b in steps]
            if vals[0] < DIV and vals[3] > 0 and vals[0] > vals[1] > vals[2] > vals[3]:
                bits |= (1 << p)
    elif CLS[t] == 2:
        c = [v for v in ADJ[t] if len(ADJ[t][v]) == 4][0]
        for p in range(NPTS):
            pt = PTS[p]
            if sum(xio(pt, ax, (c >> ax) & 1) for ax in range(4)) < DIV:
                bits |= (1 << p)
    else:
        c, m, d, e = armparts(t)
        oth = [ax for ax in range(4) if ax != d]
        mb = (m >> d) & 1
        for p in range(NPTS):
            pt = PTS[p]
            if sum(xio(pt, ax, (c >> ax) & 1) for ax in oth) < DIV:
                xe = xio(pt, e, (c >> e) & 1)
                xd = xio(pt, d, mb)
                if xe > xd and xd > 0:
                    bits |= (1 << p)
    return bits


DESC = [descmask(t) for t in range(NK)]
SAME = sum(1 for t in range(NK) if DESC[t] == MASK[t])

gate(SAME == NK and NK == 400 and NPTS == 625 and DIV == 80, "G5",
     "the inequality description read off the tree agrees with the barycentric membership at all {0} grid points, {1} of {1} pieces"
     .format(NPTS, NK))
emit("G5 detail: the oriented coordinate is the point value or {0} minus it; a chain is a strict decrease along its walk between {1} and {0}"
     .format(DIV, 0))
emit("G5 detail: a hub is a sum of four oriented coordinates below {0}; a three-arm is a sum of three below {0} with one ordered pair"
     .format(DIV))
emit("G5 detail: the description route never reads the barycentric inverse matrices, so the two routes share no code")

# ============================================== G6 the chain count law

CH = [t for t in range(NK) if CLS[t] == 0]


def chain_word(t):
    """The effective-offset word of a chain: the axis offset when the corner bit rises and its complement in the shift when it falls."""
    return tuple(OFFS[ax] if bit == 0 else NSHIFT - OFFS[ax] for ax, bit in walk_of(t)[1])


def canon(w):
    """The canonical class of a word: the smaller of the word and its mirror, the reversed word with complemented offsets."""
    rc = tuple(NSHIFT - x for x in reversed(w))
    return min(w, rc)


def ascents(w):
    return sum(1 for i in range(3) if w[i] < w[i + 1])


WORD = dict((t, chain_word(t)) for t in CH)
ASC = dict((t, ascents(WORD[t])) for t in CH)
ACEN = Counter(ASC[t] for t in CH)
G6OK = sum(1 for t in CH if PSZ[t] == comb(8 - ASC[t], 4) and PSZ[t] == RSTEP * UNIT[t])

gate(G6OK == len(CH) and len(CH) == 192 and dict(ACEN) == {0: 8, 1: 88, 2: 88, 3: 8}
     and [comb(8 - s, 4) for s in range(4)] == [70, 35, 15, 5], "G6",
     "every one of the {0} chains has point count comb({1} - s, {2}) for its ascent count s, and that count is {3} times its unit"
     .format(len(CH), 8, 4, RSTEP))
emit("G6 detail: the ascent census over the chains is {0}".format(dshow(ACEN)))
emit("G6 detail: comb({0}, {1}) = {2}, comb({3}, {1}) = {4}, comb({5}, {1}) = {6}, comb({7}, {1}) = {8}, that is {9} times {10}"
     .format(5, 4, comb(5, 4), 6, comb(6, 4), 7, comb(7, 4), 8, comb(8, 4), RSTEP, [1, 3, 7, 14]))

# ============================================== G7 the hub count law

HB = [t for t in range(NK) if CLS[t] == 2]
HW = {}
for t in HB:
    c = [v for v in ADJ[t] if len(ADJ[t][v]) == 4][0]
    HW[t] = popc(c & 7)
WCEN = Counter(HW[t] for t in HB)
G7OK = sum(1 for t in HB if PSZ[t] == comb(8 - HW[t], 4) and PSZ[t] == RSTEP * UNIT[t])

gate(G7OK == len(HB) and len(HB) == 16 and dict(WCEN) == {0: 2, 1: 6, 2: 6, 3: 2}, "G7",
     "every one of the {0} hubs has point count comb({1} - w, {2}) for the three-axis weight w of its hub corner, {0} of {0}"
     .format(len(HB), 8, 4))
emit("G7 detail: the hub-corner weight census is {0}, and the axis of offset {1} is invisible: its two directions share one offset"
     .format(dshow(WCEN), 8))

# ============================================== G8 the three-arm family stays measured

AR = [t for t in range(NK) if CLS[t] == 1]
ACEN8 = Counter(UNIT[t] for t in AR)
INSPEC = sum(1 for t in AR if UNIT[t] in (1, 3, 7, 14) and PSZ[t] == RSTEP * UNIT[t])
BYW = {}
for t in AR:
    BYW.setdefault(popc(armparts(t)[0] & 7), []).append(t)
WIT = None
for w in sorted(BYW):
    us = sorted(set(UNIT[t] for t in BYW[w]))
    if len(us) > 1 and WIT is None:
        WIT = (w, min(t for t in BYW[w] if UNIT[t] == us[0]), min(t for t in BYW[w] if UNIT[t] == us[-1]))

gate(INSPEC == len(AR) and len(AR) == 192 and dict(ACEN8) == {1: 14, 3: 82, 7: 82, 14: 14}
     and WIT is not None and UNIT[WIT[1]] != UNIT[WIT[2]] and popc(armparts(WIT[1])[0] & 7) == popc(armparts(WIT[2])[0] & 7), "G8",
     "all {0} three-arm pieces have point count {1} times a unit of the spectrum {2}, but the hub-corner weight does not fix the unit"
     .format(len(AR), RSTEP, [1, 3, 7, 14]))
emit("G8 detail: the three-arm unit census is {0}, and no closed form for this family is given here".format(dshow(ACEN8)))
emit("G8 detail: witness at hub weight {0}: the piece {1} has unit {2} while the piece {3} has unit {4}"
     .format(WIT[0], KEPT[WIT[1]], UNIT[WIT[1]], KEPT[WIT[2]], UNIT[WIT[2]]))

# ============================================== G9 the word classes and the cuttings

CLASSES = {}
for t in CH:
    CLASSES.setdefault(canon(WORD[t]), []).append(t)
CSZ = sorted(set(len(v) for v in CLASSES.values()))
PMD = piecemap(FLIPD, range(NK))
PAIRED = sum(1 for k in CLASSES if len(CLASSES[k]) == 2 and PMD[CLASSES[k][0]] == CLASSES[k][1])
FIXCH = sum(1 for t in CH if PMD[t] == t)
CUTOK = 0
SELFP = 0
DISTC = 0
PROF = Counter()
for i in range(NS):
    s = SOLS[i]
    j = SIDX.get(frozenset(PMD[t] for t in s))
    if j is not None:
        CUTOK += 1
        if j == i:
            SELFP += 1
    if len(set(canon(WORD[t]) for t in s)) == CSIZE:
        DISTC += 1
    PROF[tuple(sorted(Counter(ASC[t] for t in s).items()))] += 1
CSETW = Counter(frozenset(canon(WORD[t]) for t in s) for s in SOLS)
MCEN = Counter(CSETW.values())
WSETW = Counter(frozenset(WORD[t] for t in s) for s in SOLS)
WMCEN = Counter(WSETW.values())
ONEPR = sorted(PROF)[0]

gate(len(set(WORD.values())) == 192 and len(CLASSES) == 96 and CSZ == [2] and PAIRED == 96 and FIXCH == 0
     and CUTOK == NS and SELFP == 0 and DISTC == NS and len(PROF) == 1
     and ONEPR == ((0, 1), (1, 11), (2, 11), (3, 1)) and dict(MCEN) == {2: 2636, 4: 936, 8: 336, 16: 192, 64: 16}
     and sum(k * MCEN[k] for k in MCEN) == NS and len(CSETW) == 4116 and dict(WMCEN) == {1: NS} and len(WSETW) == NS, "G9",
     "the {0} chain words are pairwise distinct and fall into exactly {1} mirror classes of {2}, and every cutting carries {3} distinct ones"
     .format(len(CH), len(CLASSES), CSZ[0], CSIZE))
emit("G9 detail: the fourth-axis flip pairs the two chains of every class, fixes {0} of the {1} chains, and permutes the {2} cuttings with {0} "
     "fixed".format(FIXCH, len(CH), CUTOK))
emit("G9 detail: the ascent census inside a cutting is {0} at all {1} cuttings, so the count law re-derives the one unit profile"
     .format(dshow(dict(ONEPR)), NS))
emit("G9 detail: the {0} cuttings carry only {1} distinct class sets, so the class set of a cutting is not the cutting"
     .format(NS, len(CSETW)))
emit("G9 detail: the class-set multiplicity census is {0}".format(dshow(MCEN)))
emit("G9 detail: the {0} word sets are instead pairwise distinct, so the word set does determine the cutting and only the class set loses it"
     .format(NS))

# ============================================== G10 the wall separator

UNW = sorted(set(tuple(sorted(e)) for e in E36))
WLET = sorted(set(x for e in UNW for x in e))
NB = dict((v, set()) for v in WLET)
WPAR = dict((v, v) for v in WLET)


def findw(x):
    while WPAR[x] != x:
        WPAR[x] = WPAR[WPAR[x]]
        x = WPAR[x]
    return x


for a, b in UNW:
    NB[a].add(b)
    NB[b].add(a)
    ra, rb = findw(a), findw(b)
    if ra != rb:
        WPAR[ra] = rb
CMP = {}
for v in WLET:
    CMP.setdefault(findw(v), []).append(v)
CO = sorted(sorted(v) for v in CMP.values())
COF = dict((v, i) for i, C in enumerate(CO) for v in C)
NONADJ = sorted((a, b) for C in CO for a, b in itertools.combinations(C, 2) if b not in NB[a])
NNCEN = sorted(set(len(C) - 1 - len(NB[a] & set(C)) for C in CO for a in C))
A18 = sorted(set(tuple(sorted((a, b))) for a in range(NL) for b in range(NL) if TRM[a][b] == 18))
WITHIN = sorted(p for p in A18 if COF.get(p[0]) == COF.get(p[1]))
CROSS = sorted(p for p in A18 if p not in WITHIN)
COMN = sorted(set(len(NB[a] & NB[b]) for a, b in WITHIN))
CRCEN = Counter(TRM[a][b] for a in CO[0] for b in CO[1])
# The two landed letter-pair lists of the previous cycle at the smallest off-diagonal value, pinned here only as comparison targets.
# The split below is computed from the wall graph alone; these lists are never read by the code that forms it.
LAND1 = [(0, 7), (2, 13), (3, 5), (4, 11), (9, 12), (10, 14)]
LAND2 = [(0, 12), (2, 11), (3, 10), (4, 13), (5, 14), (7, 9)]

gate(len(UNW) == 24 and len(WLET) == 12 and len(CO) == 2 and [len(C) for C in CO] == [6, 6]
     and CO[0] == [0, 4, 7, 10, 11, 14] and CO[1] == [2, 3, 5, 9, 12, 13] and NNCEN == [1]
     and len(NONADJ) == 6 and NONADJ == LAND1 and len(A18) == 12 and WITHIN == LAND1 and CROSS == LAND2
     and COMN == [4] and sorted(x for p in CROSS for x in p) == WLET
     and dict(CRCEN) == {18: 6, 52: 24, 90: 6} and sum(CRCEN.values()) == 36, "G10",
     "the {0} unordered wall edges on the {1} wall letters fall into exactly {2} components of {3}, and that splits the {1} pairs at {4}"
     .format(len(UNW), len(WLET), len(CO), len(CO[0]), 18))
emit("G10 detail: the components are {0} and {1}".format(CO[0], CO[1]))
emit("G10 detail: inside a component every letter has exactly {0} non-neighbour, giving {1} non-adjacent pairs per component"
     .format(NNCEN[0], len(NONADJ) // 2))
emit("G10 detail: the {0} within-component pairs at that value are {1}, each with {2} common neighbours"
     .format(len(WITHIN), WITHIN, COMN[0]))
emit("G10 detail: the {0} cross-component pairs are {1}, a perfect matching of all {2} wall letters"
     .format(len(CROSS), CROSS, len(WLET)))
emit("G10 detail: the value census over all {0} cross-component letter pairs is {1}".format(sum(CRCEN.values()), dshow(CRCEN)))

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
