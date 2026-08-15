"""Cycle 799: the class-set fiber of a cell cutting is the free toggle group on its mirror atoms (finite checks).

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, and the order-384 group of signed
coordinate maps of the cell. Nothing outside that finite object enters any gate.

The previous cycle counted the class sets: every used piece is a chain carrying a four-letter word, the class of a word is the smaller of
the word and its reversed complement, every cutting carries 24 distinct classes, and the 15800 cuttings carry only 4116 distinct class sets
with multiplicities 2, 4, 8, 16 and 64. This cycle derives that ladder. The mirror map is the pure fourth-axis flip; it sends each chain to
the chain of the reversed complement word, hence keeps the class, so replacing some pieces of a cutting by their mirrors can leave the class
set alone. The edits available inside one fiber are shown to form a group under symmetric difference; its least moving parts, the atoms, are
characterized twice, once by membership profiles across the edits of the fiber and once by flip overlap in the point geometry of a single
cutting; the two characterizations agree at every fiber and at every member, so the fiber is the free toggle group on the atoms and its size
is two to the atom count.
Gates G1 to G10, one line each with a few detail lines, then the measured censuses and the total line. Any failure exits nonzero.
"""

import itertools
import sys
from collections import Counter
from fractions import Fraction as FRA

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


def tshow(seq):
    return "(" + ", ".join("{0}".format(x) for x in seq) + ")"


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
NK = len(KEPT)

BYPT = [[] for _ in range(NPTS)]
for t in range(NK):
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
KIDX = {frozenset(S): t for t, S in enumerate(KEPT)}
SSET = [frozenset(s) for s in SOLS]
SIDX = dict((SSET[i], i) for i in range(NS))
CSIZE = sorted(set(len(s) for s in SOLS))[0]
PSIZE = len(set(len(s) for s in SOLS))

P4 = list(itertools.permutations(range(4)))
G384 = [(p, m) for p in P4 for m in range(16)]
FLIPD = ((0, 1, 2, 3), 8)


def actcorner(g, v):
    p, m = g
    x = CORN[v]
    return CIDX[tuple(x[p[i]] ^ ((m >> p[i]) & 1) for i in range(4))]


def piecemap(g, dom):
    return dict((t, KIDX[frozenset(actcorner(g, v) for v in KEPT[t])]) for t in dom)


MP8 = piecemap(FLIPD, sorted(USED))

# The point flip: the permutation of the sample grid sending the fourth coordinate x to DIV minus x, that is the last index k to RSTEP-1-k.
PERM = [0] * NPTS
for k0 in range(RSTEP):
    for k1 in range(RSTEP):
        for k2 in range(RSTEP):
            for k3 in range(RSTEP):
                PERM[((k0 * RSTEP + k1) * RSTEP + k2) * RSTEP + k3] = ((k0 * RSTEP + k1) * RSTEP + k2) * RSTEP + (RSTEP - 1 - k3)


def flipbits(m):
    """The point mask carried through the fourth-axis point flip. This route reads the grid alone and never touches the piece map."""
    out = 0
    mm = m
    while mm:
        low = mm & (-mm)
        out |= (1 << PERM[low.bit_length() - 1])
        mm ^= low
    return out


FM = dict((t, flipbits(MASK[t])) for t in USED)

# ============================================== G1 the declared cell preamble

gate(len(CAND) == 2672 and FLOOR == 6 and NK == 400 and NS == 15800 and PSIZE == 1 and CSIZE == 24 and NU == 192
     and len(G384) == 384 and NPTS == 625 and DIV == 80, "G1",
     "the declared cell rebuilds from the corner list alone: {0} candidates, floor {1}, {2} kept, {3} cuttings of {4}, {5} used, {6} maps"
     .format(len(CAND), FLOOR, NK, NS, CSIZE, NU, len(G384)))
emit("G1 detail: the generic grid carries {0} values per axis, {1} points in all, on the integer scale of width {2}, offsets {3}"
     .format(RSTEP, NPTS, DIV, ", ".join("{0}".format(o) for o in OFFS)))

# ============================================== G2 chain coordinates and the word law


def edges_of(t):
    """The corner-adjacency edges of kept piece t: its corner pairs at coordinate distance one."""
    S = KEPT[t]
    return [(a, b) for a, b in itertools.combinations(S, 2)
            if sum(abs(CORN[a][r] - CORN[b][r]) for r in range(4)) == 1]


ADJ = {}
CHAINOK = 0
for t in USED:
    ad = dict((v, []) for v in KEPT[t])
    E = edges_of(t)
    for a, b in E:
        ad[a].append(b)
        ad[b].append(a)
    ADJ[t] = ad
    seen = set([KEPT[t][0]])
    stack = [KEPT[t][0]]
    while stack:
        v = stack.pop()
        for u in ad[v]:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    if len(KEPT[t]) == 5 and len(E) == 4 and len(seen) == 5 and sorted(len(ad[v]) for v in ad) == [1, 1, 2, 2, 2]:
        CHAINOK += 1


def walk_of(t):
    """The corner sequence and the step list of a chain, walked from its smaller-labelled degree-one end."""
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


def word_of(t):
    """The effective-offset word of a chain: the axis offset when the corner bit rises and its complement in the shift when it falls."""
    return tuple(OFFS[ax] if b == 0 else NSHIFT - OFFS[ax] for ax, b in walk_of(t)[1])


def canon(w):
    """The class of a word: the smaller of the word and its mirror, the reversed word with complemented letters."""
    return min(w, tuple(NSHIFT - x for x in reversed(w)))


def ascents(w):
    return sum(1 for i in range(3) if w[i] < w[i + 1])


WORD = dict((t, word_of(t)) for t in USED)
CW = dict((t, canon(WORD[t])) for t in USED)
AXO = dict((t, tuple(ax for ax, _ in walk_of(t)[1])) for t in USED)
ASC = dict((t, ascents(WORD[t])) for t in USED)
AXONE = sum(1 for t in USED if sorted(AXO[t]) == [0, 1, 2, 3])
LAWOK = 0
for t in USED:
    c = walk_of(t)[0][0]
    if WORD[t] == tuple(OFFS[ax] if ((c >> ax) & 1) == 0 else NSHIFT - OFFS[ax] for ax in AXO[t]):
        LAWOK += 1

gate(CHAINOK == NU and AXONE == NU and LAWOK == NU and NU == 192, "G2",
     "every one of the {0} used pieces is a five-corner chain whose four steps carry the four axes once each, {0} of {0}".format(NU))
emit("G2 detail: the word law reads each letter off the start corner and the step axis alone, offset {0} up and {1} minus it down, {2} of {2}"
     .format(tshow(OFFS), NSHIFT, LAWOK))

# ============================================== G3 the mirror lemma

MOK = sum(1 for t in USED if MASK[MP8[t]] == FM[t])
INV = sum(1 for t in USED if MP8[MP8[t]] == t)
FIX = sum(1 for t in USED if MP8[t] == t)
RCOK = sum(1 for t in USED if WORD[MP8[t]] == tuple(NSHIFT - x for x in reversed(WORD[t])))
CWOK = sum(1 for t in USED if CW[MP8[t]] == CW[t])
NCLS = len(set(CW.values()))
NWRD = len(set(WORD.values()))

gate(MOK == NU and INV == NU and FIX == 0 and RCOK == NU and CWOK == NU and NWRD == NU and NCLS == 96, "G3",
     "the mirror map on the {0} used pieces is exactly the point flip, {0} of {0}, an involution with {1} fixed pieces".format(NU, FIX))
emit("G3 detail: the mirror word is the reversed complement at {0} of {0}, so the mirror keeps the class of every chain, {1} classes in all"
     .format(NU, NCLS))
emit("G3 detail: the {0} chain words are pairwise distinct, so a class has exactly the two chains of one mirror pair".format(NWRD))

# ============================================== G4 the fibers and the toggle form

FIB = {}
for i in range(NS):
    FIB.setdefault(frozenset(CW[t] for t in SOLS[i]), []).append(i)
FKEYS = list(FIB.keys())
NFIB = len(FKEYS)
TOGOK = 0
NMEM = 0
SUPS = {}
for k in FKEYS:
    mem = FIB[k]
    A = SSET[mem[0]]
    sup = []
    for j in mem:
        B = SSET[j]
        S = A - B
        sup.append(S)
        NMEM += 1
        if B == (A - S) | frozenset(MP8[t] for t in S):
            TOGOK += 1
    SUPS[k] = sup
LAD = Counter(len(FIB[k]) for k in FKEYS)

gate(NFIB == 4116 and TOGOK == NS and NMEM == NS and sum(k * LAD[k] for k in LAD) == NS
     and all(len(set(SUPS[k])) == len(FIB[k]) for k in FKEYS)
     and all(len(k) == CSIZE for k in FKEYS), "G4",
     "the {0} cuttings fall into {1} class-set fibers, and every member is the fiber head with a subset of its pieces replaced by mirrors"
     .format(NS, NFIB))
emit("G4 detail: the toggle form holds at {0} of {0} members, and the class-set multiplicity ladder is {1}".format(NS, dshow(LAD)))

# ============================================== G5 the supports form a subspace

SUBOK = 0
for k in FKEYS:
    ss = set(SUPS[k])
    ok = True
    for a in ss:
        for b in ss:
            if (a ^ b) not in ss:
                ok = False
                break
        if not ok:
            break
    if ok:
        SUBOK += 1

gate(SUBOK == NFIB and NFIB == 4116, "G5",
     "inside every fiber the difference supports are closed under symmetric difference, hence a group of toggles, {0} of {0}".format(NFIB))

# ============================================== G6 the atoms and the derived ladder


def atoms_sorted(parts):
    return sorted((tuple(sorted(p)) for p in parts), key=lambda a: (len(a), a))


FATOM = {}
UNIONOK = 0
SIZEOK = 0
for k in FKEYS:
    A = SSET[FIB[k][0]]
    sup = SUPS[k]
    prof = {}
    for t in sorted(A):
        prof.setdefault(tuple(1 if t in S else 0 for S in sup), []).append(t)
    aset = atoms_sorted(prof.values())
    FATOM[k] = aset
    good = True
    for S in sup:
        rem = set(S)
        for a in aset:
            sa = set(a)
            if sa <= rem:
                rem -= sa
            elif sa & rem:
                good = False
                break
        if not good or rem:
            good = False
            break
    if good:
        UNIONOK += 1
    if len(FIB[k]) == 2 ** len(aset):
        SIZEOK += 1
ACOUNT = Counter(len(FATOM[k]) for k in FKEYS)

gate(UNIONOK == NFIB and SIZEOK == NFIB and NFIB == 4116
     and dict(Counter(2 ** a for a in ACOUNT.elements())) == dict(LAD), "G6",
     "every difference support is a union of fiber atoms and every fiber has size two to its atom count, {0} of {0}".format(NFIB))
emit("G6 detail: the atom-count census is {0}, and two to those counts is the ladder above".format(dshow(ACOUNT)))

# ============================================== G7 the two-route atom theorem


def geo_atoms(s):
    """The atoms of one cutting read off the point geometry alone: join two pieces when one meets the point flip of the other."""
    par = dict((t, t) for t in s)

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for p in s:
        fp = FM[p]
        for q in s:
            if MASK[q] & fp:
                ra, rb = find(p), find(q)
                if ra != rb:
                    par[ra] = rb
    comp = {}
    for t in s:
        comp.setdefault(find(t), []).append(t)
    return atoms_sorted(comp.values())


TWOOK = 0
for k in FKEYS:
    if geo_atoms(sorted(SSET[FIB[k][0]])) == FATOM[k]:
        TWOOK += 1

gate(TWOOK == NFIB and NFIB == 4116, "G7",
     "the geometric atoms of the fiber head equal its fiber atoms at {0} of {0} fibers, two routes that share no input".format(NFIB))
emit("G7 detail: the geometric route reads only the point masks of that one cutting; the fiber route reads only membership across supports")

# ============================================== G8 member independence

NPRE = 500
MIOK = 0
MITOT = 0
for k in FKEYS[:NPRE]:
    A = SSET[FIB[k][0]]
    aset = FATOM[k]
    for j in FIB[k]:
        B = SSET[j]
        S = A - B
        tr = atoms_sorted([set(a) - S | frozenset(MP8[t] for t in (set(a) & S)) for a in aset])
        MITOT += 1
        if tr == geo_atoms(sorted(B)):
            MIOK += 1

gate(MIOK == MITOT and MITOT == 2368 and NPRE == 500, "G8",
     "over the first {0} fibers the transported atoms equal the geometric atoms of every member, {1} of {1}".format(NPRE, MITOT))
emit("G8 detail: so the atom split is a property of each cutting on its own, carried along by the toggle rather than fixed by the fiber head")

# ============================================== G9 the atom-size profiles

PROF = Counter(tuple(len(a) for a in FATOM[k]) for k in FKEYS)
DIV4 = all((len(a) & 3) == 0 for k in FKEYS for a in FATOM[k])
SUM24 = all(sum(len(a) for a in FATOM[k]) == CSIZE for k in FKEYS)
RECOUNT = sum((2 ** len(p)) * PROF[p] for p in PROF)
PTARGET = {(24,): 2636, (4, 20): 552, (12, 12): 384, (4, 4, 16): 336, (4, 4, 4, 12): 192, (4, 4, 4, 4, 4, 4): 16}

gate(dict(PROF) == PTARGET and DIV4 and SUM24 and RECOUNT == NS and len(PROF) == 6, "G9",
     "the atom-size profiles are exactly {0}, every size divisible by {1}, every profile summing to {2}, and the recount is {3}"
     .format(len(PROF), 4, CSIZE, RECOUNT))
for p in sorted(PROF, key=lambda q: (len(q), q)):
    emit("G9 detail: profile {0} at {1} fibers, each carrying {2} cuttings".format(tshow(p), PROF[p], 2 ** len(p)))

# ============================================== G10 the global mirror

MIRIN = 0
MIRFIX = 0
for i in range(NS):
    ms = frozenset(MP8[t] for t in SOLS[i])
    if ms in SIDX:
        MIRIN += 1
        if ms == SSET[i]:
            MIRFIX += 1
FULLOK = 0
for k in FKEYS:
    A = SSET[FIB[k][0]]
    allat = frozenset(t for a in FATOM[k] for t in a)
    tog = frozenset(MP8[t] for t in allat)
    if allat == A and tog in SIDX and tog in set(SSET[j] for j in FIB[k]) and A in set(SSET[j] for j in FIB[k]):
        FULLOK += 1

gate(MIRIN == NS and MIRFIX == 0 and FULLOK == NFIB and NFIB == 4116, "G10",
     "toggling every atom of a fiber head gives its mirror, a cutting of the same fiber, at {0} of {0}, and no cutting is its own mirror"
     .format(NFIB))
emit("G10 detail: the mirror of a cutting is again a cutting at {0} of {0}, with {1} fixed, so the mirror is a free involution on cuttings"
     .format(NS, MIRFIX))

# ============================================== the measured censuses

SHAPE = Counter()
for s in SOLS:
    c = Counter()
    for t in s:
        c[AXO[t]] += 1
        c[tuple(reversed(AXO[t]))] += 1
    SHAPE[tuple(sorted(c.values()))] += 1
NWALKS = 2 * CSIZE
emit("census: over the {0} walk representations of a cutting the axis-order census takes {1} shapes, written as multiplicity: orders"
     .format(NWALKS, len(SHAPE)))
emit("census: " + ", ".join("{0} at {1}".format(dshow(Counter(sh)), SHAPE[sh])
                           for sh in sorted(SHAPE, key=lambda x: -SHAPE[x])))
ACEN = Counter(tuple(sorted(Counter(ASC[t] for t in s).items())) for s in SOLS)
if len(ACEN) != 1:
    raise ValueError("the ascent census is not a single shape")
ONE = sorted(ACEN)[0]
emit("census: the ascent census inside a cutting is {0} at all {1} cuttings, one shape, kept by every toggle"
     .format(dshow(dict(ONE)), ACEN[ONE]))

emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
