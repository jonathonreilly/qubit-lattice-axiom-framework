"""Physical cell cutting: the facet alphabet, the even-heavy parity law, and the forty period-one cuttings.

Standalone exact runner. Standard library only, no file input or output, no randomness, integer and exact rational arithmetic only.

The preamble rebuilds the declared finite object from the 16 corners of the unit four-cube: the five-corner unit-determinant pieces, the
adjacency cost floor, the kept pieces at that floor, the exact 24-piece cuttings, the used pieces, and the order-384 group of signed
coordinate maps of the cell. Nothing outside that finite object enters any gate.

The work of this cycle is the interface, that is the boundary reading of the object. A used piece meets the boundary in facet faces: four
of its five corners lying in a hyperplane of the cell and forming a unit tetrahedron of the projected three-cube. A five-corner piece
cannot place four corners in each of two parallel hyperplanes, so two such faces must sit on distinct axes; the measured count of faces is
exactly two for every used piece. Every cutting therefore dissects each of the eight boundary three-cubes into six tetrahedra. Only 16 such
dissections ever occur, the same 16 on every facet, and they are the letters of a finite alphabet. Four letters are single-diagonal, their
six tetrahedra all sharing one main diagonal of the three-cube, and those four turn out to be exactly the letters of slot multiplicity
1364; the other twelve split three and three over a pair of diagonals and carry multiplicity 862.

Two structural laws follow. The interface matrix of an axis is symmetric because the reflection of that coordinate lies in the group, maps
cuttings to cuttings, exchanges the two facets of the axis and leaves the projected dissections alone. And the number of heavy letters a
cutting shows is always even: there is a bookkeeping bit psi on the 24 boundary tetrahedra whose sum over the six tetrahedra of a letter
reads that letter's heavy bit, the multiset of the 48 piece faces of a cutting equals the multiset union of its eight letters, so the heavy
count is the number of pieces whose two faces disagree on psi, and that mismatch set of 88 pieces is orthogonal over GF(2) to an 88-row
basis of the cutting span. No strictly per-piece certificate exists: adjoining the 192 per-piece equality rows makes the letter system
inconsistent, so the law is global at piece level.

Finally the cuttings whose letters agree on both sides of all four axes, the forty, extend to a face-to-face tiling of four-space with one
cell per period; under the order-384 group they form two orbits, of sizes 8 and 32.

Gates K1 to K12, one or more lines each, then a resource line and the total line. Any failure exits nonzero."""

import itertools
import sys
import time
import resource
from collections import Counter
from fractions import Fraction as FR

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
    M = [[FR(C[r][c]) for c in range(n)] + [FR(1 if r == c else 0) for c in range(n)] for r in range(n)]
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
UIDX = {t: i for i, t in enumerate(USED)}
SIDX = {frozenset(s): i for i, s in enumerate(SOLS)}
PSIZE = len(set(len(s) for s in SOLS))
CSIZE = sorted(set(len(s) for s in SOLS))[0]

FACE = {}
for t in USED:
    S = KEPT[t]
    for a in range(4):
        for c in (0, 1):
            F = [v for v in S if CORN[v][a] == c]
            if len(F) == 4:
                FACE[(t, a, c)] = frozenset(tuple(CORN[v][r] for r in range(4) if r != a) for v in F)

KEYF = []
SIX = 0
for s in SOLS:
    d = {}
    for a in range(4):
        for c in (0, 1):
            fl = [FACE[(t, a, c)] for t in s if (t, a, c) in FACE]
            if len(fl) == 6 and len(set(fl)) == 6:
                SIX += 1
            d[(a, c)] = frozenset(fl)
    KEYF.append(d)

ALLK = sorted({d[k] for d in KEYF for k in d}, key=lambda f: sorted(sorted(t) for t in f))
KN = {k: i for i, k in enumerate(ALLK)}
KEY = [{k: KN[v] for k, v in d.items()} for d in KEYF]
NL = len(ALLK)

TETS = sorted({t for K in ALLK for t in K}, key=lambda f: sorted(f))
TN = {t: i for i, t in enumerate(TETS)}
NT = len(TETS)
TSET = set(TETS)

PFACE = {}
for (t, a, c), f in FACE.items():
    PFACE.setdefault(t, []).append(f)

gate(len(CAND) == 2672 and FLOOR == 6 and len(KEPT) == 400 and NS == 15800 and NU == 192
     and PSIZE == 1 and CSIZE == 24, "K1",
     "the cell has 2672 unit-determinant five-corner pieces, adjacency cost floor 6, 400 kept, 15800 cuttings of 24, 192 used pieces")

# ---------------------------------------------------------------- K2 the facet-face lemma

SLOTS = {}
NFOK = 0
AXOK = 0
FIN = 0
for t in USED:
    sl = [(a, c) for a in range(4) for c in (0, 1) if (t, a, c) in FACE]
    if len(sl) == 2:
        NFOK += 1
        if sl[0][0] != sl[1][0]:
            AXOK += 1
    for k in sl:
        if FACE[(t, k[0], k[1])] in TSET:
            FIN += 1
    SLOTS[t] = frozenset(sl)
SPC = Counter(SLOTS.values())
SPCEN = Counter(SPC.values())

gate(NFOK == 192 and AXOK == 192 and FIN == 384 and NT == 24, "K2",
     "all 192 used pieces cut exactly 2 facet faces, on distinct axes, and all 384 faces are among the 24 boundary tetrahedra")
gate(len(SPC) == 24 and set(SPCEN) == {8} and SPCEN[8] == 24, "K2",
     "the 192 pieces spread over exactly 24 slot-pairs with 8 pieces each, and 24 times 8 = 192")

# ---------------------------------------------------------------- K3, K4 the alphabet

SLOTSETS = [set(KEY[i][(a, c)] for i in range(NS)) for a in range(4) for c in (0, 1)]
SAME = all(x == SLOTSETS[0] for x in SLOTSETS)

gate(SIX == NS * 8 and SIX == 126400, "K3",
     "every one of the 15800 cuttings cuts 6 pieces and 6 distinct tetrahedra on each of the 8 facets, 126400 slots, 0 misses")
gate(NL == 16 and SAME and len(SLOTSETS[0]) == 16, "K4",
     "the facet alphabet has exactly 16 dissections and the same 16 letters occur on every one of the 8 slots")

# ---------------------------------------------------------------- K5 tetra structure and the intrinsic split

DIAGS = [((0, 0, 0), (1, 1, 1)), ((1, 0, 0), (0, 1, 1)), ((0, 1, 0), (1, 0, 1)), ((0, 0, 1), (1, 1, 0))]
TDIAG = {}
ONEP = 0
for t in TETS:
    ds = [i for i, (p, q) in enumerate(DIAGS) if p in t and q in t]
    if len(ds) == 1:
        ONEP += 1
        TDIAG[t] = ds[0]
DCEN = Counter(TDIAG.values())

SING = {}
PAIRC = Counter()
for i, K in enumerate(ALLK):
    c = Counter(TDIAG[t] for t in K)
    if len(c) == 1:
        SING[i] = next(iter(c))
    elif sorted(c.values()) == [3, 3]:
        PAIRC[tuple(sorted(c))] += 1
SINGOK = (SING == {1: 2, 6: 3, 8: 1, 15: 0}) and sorted(SING.values()) == [0, 1, 2, 3]

gate(NT == 24 and ONEP == 24 and dict(DCEN) == {0: 6, 1: 6, 2: 6, 3: 6}, "K5",
     "the letters use 24 tetrahedra, each holding exactly 1 antipodal corner pair, with 6 tetrahedra on each of the 4 main diagonals")
gate(len(SING) == 4 and SINGOK and sum(PAIRC.values()) == 12 and len(PAIRC) == 6
     and set(PAIRC.values()) == {2}, "K5",
     "4 single-diagonal letters, bijection {0} to the diagonals; other 12 split (3, 3), 2 per diagonal pair".format(dshow(SING)))

# ---------------------------------------------------------------- K6 the boundary group

P3 = list(itertools.permutations(range(3)))
G48 = [(p, m) for p in P3 for m in range(8)]
FC3 = [tuple((i >> b) & 1 for b in range(3)) for i in range(8)]


def act3(g, v):
    p, m = g
    return tuple(v[p[i]] ^ ((m >> p[i]) & 1) for i in range(3))


def actk(g, key):
    return frozenset(frozenset(act3(g, v) for v in tet) for tet in key)


KFAIL = 0
KORB = []
SEENK = set()
for k in ALLK:
    if KN[k] in SEENK:
        continue
    o = set()
    for g in G48:
        kk = actk(g, k)
        if kk not in KN:
            KFAIL += 1
            continue
        o.add(KN[kk])
    SEENK |= o
    KORB.append(sorted(o))
KORBS = [len(o) for o in KORB]

P4 = list(itertools.permutations(range(4)))
G384 = [(p, m) for p in P4 for m in range(16)]


def actcorner(g, v):
    p, m = g
    x = CORN[v]
    return CIDX[tuple(x[p[i]] ^ ((m >> p[i]) & 1) for i in range(4))]


FACECORN = [v for v in range(16) if CORN[v][0] == 0]
HOLD = []
for g in G384:
    if all(CORN[actcorner(g, v)][0] == 0 for v in FACECORN):
        HOLD.append(g)
INDH = set()
for g in HOLD:
    INDH.add(tuple(tuple(CORN[actcorner(g, v)][1:]) for v in FACECORN))
INDG = set()
for g in G48:
    INDG.add(tuple(act3(g, CORN[v][1:]) for v in FACECORN))

KIDX = {frozenset(S): t for t, S in enumerate(KEPT)}
PMAP = {}
PBAD = 0
for g in G384:
    mp = {}
    ok = True
    for t in USED:
        tt = KIDX.get(frozenset(actcorner(g, v) for v in KEPT[t]))
        if tt is None:
            ok = False
            break
        mp[t] = tt
    if ok:
        PMAP[g] = mp
    else:
        PBAD += 1

gate(KFAIL == 0 and sorted(KORBS, reverse=True) == [12, 4] and len(KORB) == 2, "K6",
     "the 16 letters are closed under the order-48 signed maps of the boundary three-cube, 0 failures, and split into orbits [12, 4]")
gate(len(HOLD) == 48 and len(INDH) == 48 and INDH == INDG and len(INDG) == 48 and PBAD == 0, "K6",
     "the slot holder inside the order-384 cell group has 48 maps inducing all 48 signed maps of the boundary three-cube, 0 strays")

# ---------------------------------------------------------------- K7 the multiplicity law

MULT = []
for a in range(4):
    for c in (0, 1):
        MULT.append(Counter(KEY[i][(a, c)] for i in range(NS)))
MCEN = [dict(sorted(Counter(m.values()).items())) for m in MULT]
MSAME = all(x == MCEN[0] for x in MCEN)
MVAL = sorted(MCEN[0])
HEAVY = set(k for k in MULT[0] if MULT[0][k] == MVAL[-1])
HSAME = all(set(k for k in m if m[k] == MVAL[-1]) == HEAVY for m in MULT)
IDOK = (MCEN[0][MVAL[0]] * MVAL[0] + MCEN[0][MVAL[-1]] * MVAL[-1] == NS)

gate(MSAME and MCEN[0] == {862: 12, 1364: 4} and IDOK, "K7",
     "the slot multiplicity census is {0} on every one of the 8 slots, and 12 times 862 plus 4 times 1364 is 15800".format(
         dshow(MCEN[0])))
gate(HSAME and sorted(HEAVY) == [1, 6, 8, 15] and HEAVY == set(SING) and MVAL[-1] == 1364, "K7",
     "the heavy keys, defined as the keys of slot multiplicity 1364, are {0} and are exactly the single-diagonal letters".format(
         sorted(HEAVY)))

# ---------------------------------------------------------------- K8 the interface matrix

SWBAD = 0
for a in range(4):
    mp = PMAP[(tuple(range(4)), 1 << a)]
    for i in range(NS):
        j = SIDX.get(frozenset(mp[t] for t in SOLS[i]))
        if j is None or KEY[j][(a, 0)] != KEY[i][(a, 1)] or KEY[j][(a, 1)] != KEY[i][(a, 0)]:
            SWBAD += 1

NMAT = []
ECEN = []
SYM = 0
TRC = []
for a in range(4):
    J = Counter((KEY[i][(a, 0)], KEY[i][(a, 1)]) for i in range(NS))
    M = [[J[(x, y)] for y in range(16)] for x in range(16)]
    NMAT.append(M)
    ECEN.append(dict(sorted(Counter(M[x][y] for x in range(16) for y in range(16)).items())))
    if all(M[x][y] == M[y][x] for x in range(16) for y in range(16)):
        SYM += 1
    TRC.append(sum(M[x][x] for x in range(16)))

ESAME = all(e == ECEN[0] for e in ECEN)
DLIGHT = set(NMAT[a][x][x] for a in range(4) for x in range(16) if x not in HEAVY)
DHEAVY = set(NMAT[a][x][x] for a in range(4) for x in range(16) if x in HEAVY)
HROW = [dict(sorted(Counter(NMAT[a][x]).items())) for a in range(4) for x in sorted(HEAVY)]
HRSAME = all(h == HROW[0] for h in HROW)
HRSUM = sum(k * HROW[0][k] for k in HROW[0])

GLUE = [sum(MULT[2 * a][k] * MULT[2 * a + 1][k] for k in range(16)) for a in range(4)]
RSUM = [dict(sorted(Counter(MULT[2 * a][KEY[i][(a, 1)]] for i in range(NS)).items())) for a in range(4)]
RSAME = all(r == RSUM[0] for r in RSUM)

gate(SWBAD == 0, "K8",
     "the reflection of a coordinate sends all 15800 cuttings to cuttings and swaps the two letters of its own axis, 4 axes, 0 misses")
gate(SYM == 4 and ESAME and ECEN[0] == {18: 24, 36: 48, 50: 48, 52: 48, 90: 12, 92: 48, 100: 12, 104: 12, 200: 4}, "K8",
     "interface matrix symmetric on all 4 axes; entry census {0}".format(dshow(ECEN[0])))
gate(set(TRC) == {2000} and DLIGHT == {100} and DHEAVY == {200} and 12 * 100 + 4 * 200 == 2000
     and HRSAME and HROW[0] == {50: 6, 92: 6, 104: 3, 200: 1} and HRSUM == 1364, "K8",
     "trace 2000 is 12 times 100 plus 4 times 200; every heavy row is 200 plus 3 times 104 plus 6 times 92 plus 6 times 50, giving 1364")
gate(set(GLUE) == {16358512} and 12 * 862 * 862 + 4 * 1364 * 1364 == 16358512 and RSAME
     and RSUM[0] == {862: 10344, 1364: 5456}, "K8",
     "the gluing relation has 16358512 pairs on every axis, with the row-sum census {0} over cuttings".format(dshow(RSUM[0])))

# ---------------------------------------------------------------- K9 the self-match laws

MATCH = [tuple(a for a in range(4) if KEY[i][(a, 0)] == KEY[i][(a, 1)]) for i in range(NS)]
WCEN = dict(sorted(Counter(len(m) for m in MATCH).items()))
SGL = dict(sorted(Counter(m[0] for m in MATCH if len(m) == 1).items()))
PRC = dict(sorted(Counter(m for m in MATCH if len(m) == 2).items()))
PERAX = [sum(1 for m in MATCH if a in m) for a in range(4)]
W2 = Counter()
for i in range(NS):
    if len(MATCH[i]) == 2:
        W2["".join(sorted("H" if KEY[i][(a, 0)] in HEAVY else "L" for a in MATCH[i]))] += 1
W1 = Counter()
for i in range(NS):
    if len(MATCH[i]) == 1:
        W1["H" if KEY[i][(MATCH[i][0], 0)] in HEAVY else "L"] += 1

gate(set(PERAX) == {2000} and WCEN == {0: 9504, 1: 4672, 2: 1584, 4: 40} and 3 not in WCEN, "K9",
     "self-matching holds for 2000 cuttings on each axis, with weight census {0}, and weight 3 never occurs".format(dshow(WCEN)))
gate(set(SGL.values()) == {1168} and len(SGL) == 4 and set(PRC.values()) == {264} and len(PRC) == 6
     and dict(W2) == {"HH": 384, "HL": 768, "LL": 432} and dict(W1) == {"H": 1600, "L": 3072}, "K9",
     "singleton 1168 on each axis and 264 on each of the 6 axis pairs; weight 2 gives HH 384 HL 768 LL 432, weight 1 H 1600 L 3072")

# ---------------------------------------------------------------- K10 the parity law

HCEN = dict(sorted(Counter(sum(1 for a in range(4) for c in (0, 1) if KEY[i][(a, c)] in HEAVY)
                           for i in range(NS)).items()))
ODD = sum(HCEN[k] for k in HCEN if k & 1)

LETR = []
for i, K in enumerate(ALLK):
    m = 0
    for t in K:
        m ^= (1 << TN[t])
    LETR.append((m, 1 if i in HEAVY else 0))

R = list(LETR)
PIVC = []
rr = 0
for col in range(NT):
    p = None
    for j in range(rr, len(R)):
        if (R[j][0] >> col) & 1:
            p = j
            break
    if p is None:
        continue
    R[rr], R[p] = R[p], R[rr]
    for j in range(len(R)):
        if j != rr and ((R[j][0] >> col) & 1):
            R[j] = (R[j][0] ^ R[rr][0], R[j][1] ^ R[rr][1])
    PIVC.append(col)
    rr += 1
LCONS = not any(m == 0 and b == 1 for m, b in R)
PSI = 0
for j in range(rr):
    if R[j][1]:
        PSI |= (1 << PIVC[j])
SUPP = [i for i in range(NT) if (PSI >> i) & 1]
LOK = sum(1 for i, K in enumerate(ALLK)
          if (sum((PSI >> TN[t]) & 1 for t in K) & 1) == (1 if i in HEAVY else 0))

OM = 0
for t, fs in PFACE.items():
    if ((PSI >> TN[fs[0]]) & 1) != ((PSI >> TN[fs[1]]) & 1):
        OM |= (1 << UIDX[t])
OSZ = bin(OM).count("1")

FMBAD = 0
for i, s in enumerate(SOLS):
    faces = Counter()
    for t in s:
        f1, f2 = PFACE[t]
        faces[f1] += 1
        faces[f2] += 1
    lets = Counter()
    for a in range(4):
        for c in (0, 1):
            for tet in ALLK[KEY[i][(a, c)]]:
                lets[tet] += 1
    if faces != lets:
        FMBAD += 1

CUTM = []
for s in SOLS:
    m = 0
    for t in s:
        m |= (1 << UIDX[t])
    CUTM.append(m)
ODIR = sum(1 for cm in CUTM if bin(cm & OM).count("1") & 1)
PIVU = {}
BROWS = []
for idx, cm in enumerate(CUTM):
    m = cm
    while m:
        h = m.bit_length() - 1
        if h in PIVU:
            m ^= PIVU[h]
        else:
            PIVU[h] = m
            BROWS.append(idx)
            break
BOK = all(bin(CUTM[i] & OM).count("1") & 1 == 0 for i in BROWS)


def elim(rows):
    piv = {}
    incons = False
    for m, b in rows:
        while m:
            h = m.bit_length() - 1
            if h in piv:
                pm, pb = piv[h]
                m ^= pm
                b ^= pb
            else:
                piv[h] = (m, b)
                break
        if m == 0 and b == 1:
            incons = True
    return len(piv), incons


CUTR = []
for s in SOLS:
    m = 0
    for t in s:
        f1, f2 = PFACE[t]
        m ^= (1 << TN[f1]) ^ (1 << TN[f2])
    CUTR.append((m, 0))
PROWS = [((1 << TN[fs[0]]) ^ (1 << TN[fs[1]]), 0) for fs in PFACE.values()]
PTRIV = sum(1 for m, b in PROWS if m == 0)
RA, IA = elim(LETR)
RB, IB = elim(LETR + CUTR)
RC, IC = elim(LETR + CUTR + PROWS)

gate(HCEN == {0: 1200, 2: 7872, 4: 6240, 6: 480, 8: 8} and ODD == 0, "K10",
     "the heavy-slot census over all cuttings is {0}, so no cutting shows an odd number of heavy letters".format(dshow(HCEN)))
gate(rr == 10 and LCONS and NT - rr == 14 and PIVC == [0, 1, 2, 3, 4, 6, 8, 12, 14, 18]
     and SUPP == [0, 2, 3, 4, 8, 12, 14, 18], "K10",
     "letter system rank 10, consistent, solution dim 14, pivots {0}, psi support {1}".format(PIVC, SUPP))
gate(LOK == 16 and FMBAD == 0, "K10",
     "psi verifies all 16 letter equations and the face-multiset identity holds on all 15800 cuttings with 0 violations")
gate(OSZ == 88 and ODIR == 0 and len(PIVU) == 88 and NU - len(PIVU) == 104 and BOK and len(BROWS) == 88, "K10",
     "the mismatch set has 88 pieces and meets every cutting evenly, 0 odd; the cutting matrix has rank 88 over GF(2), left 104")
gate(RA == 10 and not IA and RB == 10 and not IB and RC == 23 and IC and len(PROWS) == NU
     and PTRIV == 2 and len(PROWS) - PTRIV == 190, "K10",
     "letters plus 15800 cutting rows keep rank 10, consistent; the 192 per-piece rows, 2 of them trivial, 190 not, give rank 23 inconsistent")

# ---------------------------------------------------------------- K11, K12 the forty

ALL40 = [i for i in range(NS) if len(MATCH[i]) == 4]
ORB = []
SEEN40 = set()
for i in ALL40:
    if i in SEEN40:
        continue
    o = set()
    st = 0
    for g in G384:
        j = SIDX[frozenset(PMAP[g][t] for t in SOLS[i])]
        o.add(j)
        if j == i:
            st += 1
    SEEN40 |= o
    ORB.append((sorted(o), st))
OSIZE = sorted(len(o) for o, st in ORB)
OSTAB = sorted(st for o, st in ORB)
IN40 = all(set(o) <= set(ALL40) for o, st in ORB)
PROF = {}
for o, st in ORB:
    pr = set()
    for i in o:
        pr.add("".join(sorted("H" if KEY[i][(a, 0)] in HEAVY else "L" for a in range(4))))
    PROF[len(o)] = sorted(pr)
H8 = set(i for i in range(NS) if sum(1 for a in range(4) for c in (0, 1) if KEY[i][(a, c)] in HEAVY) == 8)
EQ8 = any(set(o) == H8 and len(o) == 8 for o, st in ORB)

gate(len(ALL40) == 40 and IN40 and OSIZE == [8, 32] and OSTAB == [12, 48]
     and 8 * 48 == 384 and 32 * 12 == 384, "K11",
     "exactly 40 cuttings match on all 4 axes; two orbits of sizes [8, 32] with holder orders [48, 12], and 8 times 48 is 384")
gate(PROF.get(8) == ["HHHH"] and PROF.get(32) == ["HLLL"] and EQ8 and len(H8) == 8, "K11",
     "the size 8 orbit is all-heavy HHHH and equals the 8 cuttings of heavy count 8; the size 32 orbit is HLLL throughout")

WIT = []
WOK = 0
for o, st in sorted(ORB, key=lambda z: len(z[0])):
    i = o[0]
    ls = [KEY[i][(a, 0)] for a in range(4)]
    if all(KEY[i][(a, 0)] == KEY[i][(a, 1)] for a in range(4)):
        WOK += 1
    WIT.append(ls)

gate(WOK == 2 and len(WIT) == 2, "K12",
     "one witness per orbit, letters {0} and {1}, matching on both sides of all 4 axes; each has period one".format(WIT[0], WIT[1]))

RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PEAK = RSS // (1024 * 1024) if sys.platform == "darwin" else RSS // 1024
emit("resource: under {0} s, under {1} MB".format(((int(time.time() - T0) // 60) + 1) * 60, ((PEAK // 250) + 1) * 250))
emit("TOTAL: PASS={0} FAIL={1}".format(STAT[0], STAT[1]))
if STAT[1]:
    sys.exit(1)
