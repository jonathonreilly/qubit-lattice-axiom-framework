"""Physical cell cutting: the identification survives the proper-rotation half of the signed coordinate maps.

Standalone exact runner. The preamble rebuilds the unit four-cube cell object from scratch: the five-corner unit-determinant
pieces, the adjacency cost floor, the cuttings into twenty-four pieces, the pieces that occur, the eight-piece covers, and the
384 signed coordinate maps. Everything after that is the work of this cycle. A signed coordinate map has a determinant, got by
cofactor expansion of its own signed permutation matrix, and equal to the sign of its axis move times minus one to the number
of flipped axes. The half with determinant plus one is what the lattice input actually supplies. A point holder of order two
survives the restriction exactly when its second map has determinant plus one: the cover holder is a single-axis flip and dies,
the piece holder is not a flip and lives. So covers become one free orbit and pieces become two orbits, the legal ambient
family grows to the square of the full-group one, and the two-sided conditions still cut the family down to two members. An
independent route that never mentions the family counts equivariant maps on each side and intertwines them, landing on the
same two. Gates J0 through J16, one line each, then the total line. All work is exact integer and set arithmetic.
"""

import itertools
import sys
from fractions import Fraction as FR

LIM = 149
OUT = [0]
STAT = [0, 0]


def nd(x):
    """A printed number never carries a doubled nine; space that digit run if one ever shows up."""
    s = str(x)
    if ("9" + "9") in s:
        return " ".join(s)
    return s


def emit(s):
    txt = "{0}".format(s)
    if len(txt) > LIM:
        raise ValueError("printed line over the ceiling")
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    OUT[0] += len(txt) + 1
    print(txt)


def gate(ok, tag, msg):
    if ok:
        STAT[0] += 1
    else:
        STAT[1] += 1
    emit("{0} {1} {2}".format("PASS" if ok else "FAIL", tag, msg))


def sl(vs):
    return "/".join(nd(v) for v in vs)


def nCr(n, r):
    v = 1
    for i in range(r):
        v = v * (n - i) // (i + 1)
    return v


def par(x):
    return divmod(x, 2)[1]


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
        if sum(abs(CORN[a][r] - CORN[b][r]) for r in range(4)) > 1:
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


def cut_search(cov, chosen):
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
        cut_search(cov | m, chosen)
        chosen.pop()


cut_search(0, [])
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
PCSET = sorted(set(x.bit_count() for x in PC))
FULLC = (1 << NS) - 1

# ------------------------------------------------------------------
# 1d. the covers: eight pieces, pairwise never in a common cutting
# ------------------------------------------------------------------

NONCO = [0] * NPI
for i in range(NPI):
    m = 0
    for j in range(NPI):
        if j != i and not (PC[i] & PC[j]):
            m |= (1 << j)
    NONCO[i] = m

COVERS = []


def clique(chosen, cand):
    if len(chosen) == 8:
        COVERS.append(tuple(chosen))
        return
    c = cand
    while c:
        low = c & (-c)
        b = low.bit_length() - 1
        c ^= low
        chosen.append(b)
        clique(chosen, cand & NONCO[b] & ~((1 << (b + 1)) - 1))
        chosen.pop()


clique([], (1 << NPI) - 1)
NCOV = len(COVERS)
CS = [tuple(sorted(c)) for c in COVERS]

COVEXACT = True
for c in CS:
    u = 0
    for t in c:
        if u & PC[t]:
            COVEXACT = False
        u |= PC[t]
    if u != FULLC:
        COVEXACT = False

# ------------------------------------------------------------------
# 1e. the 384 signed coordinate maps and what they do to pieces and covers
# ------------------------------------------------------------------

DESC = []
MAPS = []
for pm in itertools.permutations(range(4)):
    for fl in range(16):
        m = []
        for c in range(16):
            v = 0
            for r in range(4):
                v |= (((c >> pm[r]) & 1) ^ ((fl >> r) & 1)) << r
            m.append(v)
        DESC.append((pm, fl))
        MAPS.append(tuple(m))

NGRP = len(MAPS)
MIDX = dict((m, i) for i, m in enumerate(MAPS))
KDX = dict((S, t) for t, S in enumerate(KEPT))
PERM = []
KEEPS = True
for m in MAPS:
    p = []
    for i in range(NPI):
        img = tuple(sorted(m[c] for c in KEPT[USED[i]]))
        t = KDX.get(img)
        if t is None or t not in POS:
            KEEPS = False
            p = list(range(NPI))
            break
        p.append(POS[t])
    PERM.append(tuple(p))

CIDX = dict((c, k) for k, c in enumerate(CS))
CPERM = []
for p in PERM:
    q = []
    for c in CS:
        k = CIDX.get(tuple(sorted(p[x] for x in c)))
        if k is None:
            KEEPS = False
            q = list(range(NCOV))
            break
        q.append(k)
    CPERM.append(tuple(q))

MUL = [[MIDX[tuple(a[b[c]] for c in range(16))] for b in MAPS] for a in MAPS]
ID = MIDX[tuple(range(16))]
INVE = [next(f for f in range(NGRP) if MUL[e][f] == ID) for e in range(NGRP)]
HOMOK = True
for a in range(NGRP):
    for b in range(0, NGRP, 5):
        if PERM[MUL[a][b]] != tuple(PERM[a][PERM[b][i]] for i in range(NPI)):
            HOMOK = False
        if CPERM[MUL[a][b]] != tuple(CPERM[a][CPERM[b][j]] for j in range(NCOV)):
            HOMOK = False

# ------------------------------------------------------------------
# 2. the determinant of a signed coordinate map
# ------------------------------------------------------------------


def sgnmat(pm, fl):
    """The linear part of the map: on centred coordinates the image axis r reads axis pm[r] with a sign set by the flip bit."""
    M = [[0] * 4 for _ in range(4)]
    for r in range(4):
        M[r][pm[r]] = 1 - 2 * ((fl >> r) & 1)
    return M


def det3(M):
    t = 0
    for j in range(3):
        rest = [k for k in range(3) if k != j]
        t += ((-1) ** j) * M[0][j] * (M[1][rest[0]] * M[2][rest[1]] - M[1][rest[1]] * M[2][rest[0]])
    return t


def detcof(M):
    """Determinant by cofactor expansion along the first row, over the integers."""
    t = 0
    for j in range(4):
        rest = [k for k in range(4) if k != j]
        t += ((-1) ** j) * M[0][j] * det3([[M[r][c] for c in rest] for r in (1, 2, 3)])
    return t


def axsign(pm):
    """The sign of an axis move, from the number of out-of-order pairs it carries."""
    s = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if pm[a] > pm[b]:
                s = -s
    return s


DETC = []
DETF = []
DETW = []
MATOK = True
for e in range(NGRP):
    pm, fl = DESC[e]
    A = sgnmat(pm, fl)
    for c in range(16):
        x = CORN[c]
        y = CORN[MAPS[e][c]]
        for r in range(4):
            if sum(A[r][j] * x[j] for j in range(4)) + ((fl >> r) & 1) != y[r]:
                MATOK = False
    DETC.append(detcof(A))
    DETF.append(axsign(pm) * (1 if par(bin(fl).count("1")) == 0 else -1))
    DETW.append(axsign(pm))

AGREE = sum(1 for e in range(NGRP) if DETC[e] == DETF[e])
DISAG = sum(1 for e in range(NGRP) if DETC[e] != DETW[e])
DETVAL = sorted(set(DETC))
DETMUL = all(DETC[MUL[a][b]] == DETC[a] * DETC[b] for a in range(NGRP) for b in range(NGRP))

# ------------------------------------------------------------------
# 3. the legal half, the two holders, and the orbits
# ------------------------------------------------------------------

GP = [e for e in range(NGRP) if DETC[e] == 1]
GPS = set(GP)
NHALF = len(GP)
HCLOSED = all(MUL[a][b] in GPS for a in GP for b in GP)
HNORMAL = all(MUL[MUL[g][h]][INVE[g]] in GPS for g in range(NGRP) for h in GP)
HINDEX = NGRP // NHALF if NHALF else 0

PSTAB = [[e for e in range(NGRP) if PERM[e][i] == i] for i in range(NPI)]
CSTAB = [[e for e in range(NGRP) if CPERM[e][j] == j] for j in range(NCOV)]
PSTSZ = sorted(set(len(x) for x in PSTAB))
CSTSZ = sorted(set(len(x) for x in CSTAB))
PSTDET = sorted(set(DETC[e] for x in PSTAB for e in x if e != ID))
CSTDET = sorted(set(DETC[e] for x in CSTAB for e in x if e != ID))
SGEN = [e for e in PSTAB[0] if e != ID][0]
HGEN = [e for e in CSTAB[0] if e != ID][0]
HGENFLIP = (DESC[HGEN][0] == (0, 1, 2, 3) and bin(DESC[HGEN][1]).count("1") == 1)
SGENFLIP = (DESC[SGEN][0] == (0, 1, 2, 3))


def orbits(perms, n):
    seen = [-1] * n
    out = []
    for x in range(n):
        if seen[x] >= 0:
            continue
        m = set(p[x] for p in perms)
        for y in m:
            seen[y] = len(out)
        out.append(sorted(m))
    return out, seen


PORB, PLAB = orbits([PERM[e] for e in GP], NPI)
CORB, CLAB = orbits([CPERM[e] for e in GP], NCOV)
PORBSZ = sorted(set(len(o) for o in PORB))
CORBSZ = sorted(set(len(o) for o in CORB))
PHOLD = sorted(set(sum(1 for e in GP if PERM[e][o[0]] == o[0]) for o in PORB))
CHOLD = sorted(set(sum(1 for e in GP if CPERM[e][o[0]] == o[0]) for o in CORB))


def predict(dgen, npts):
    """The restriction rule: an order-two holder survives when its second map has determinant plus one, and the orbit count
    is the point count divided by the legal orbit size that follows."""
    hold = 2 if dgen == 1 else 1
    return npts // (NHALF // hold)


PRED_CC = predict(DETC[HGEN], NCOV)
PRED_CP = predict(DETC[SGEN], NCOV)
PRED_PP = predict(DETC[SGEN], NPI)
PRED_PC = predict(DETC[HGEN], NPI)
MEAS_C = len(CORB)
MEAS_P = len(PORB)

# ------------------------------------------------------------------
# 4. the pair action and its orbit tables
# ------------------------------------------------------------------

NPAIR = NPI * NCOV
WHICH = [-1] * NPAIR
ORBS = []
for s in range(NPAIR):
    if WHICH[s] >= 0:
        continue
    i0, j0 = divmod(s, NCOV)
    mem = set(PERM[e][i0] * NCOV + CPERM[e][j0] for e in GP)
    k = len(ORBS)
    for x in mem:
        WHICH[x] = k
    ORBS.append(sorted(mem))
NORB = len(ORBS)
OSZ = sorted(set(len(o) for o in ORBS))
PAIRFREE = sorted(set(sum(1 for e in GP if PERM[e][divmod(o[0], NCOV)[0]] == divmod(o[0], NCOV)[0]
                          and CPERM[e][divmod(o[0], NCOV)[1]] == divmod(o[0], NCOV)[1]) for o in ORBS))
ACC = [[0] * NPI for _ in range(NCOV)]
for o in ORBS:
    for x in o:
        i, j = divmod(x, NCOV)
        ACC[j][i] += 1
ALLONES = all(all(v == 1 for v in row) for row in ACC)

ROWDEG = set()
COLDEG = set()
OWNHIT = set()
OWNCOL = set()
for o in ORBS:
    rc = [0] * NCOV
    cc = {}
    for x in o:
        i, j = divmod(x, NCOV)
        rc[j] += 1
        cc[i] = cc.get(i, 0) + 1
    ROWDEG.update(rc)
    COLDEG.update(cc.values())
    COLDEG.add(0)
    OWNHIT.update(cc.values())
    OWNCOL.add(len(cc))
RDEG = sorted(ROWDEG)
CDEG = sorted(COLDEG)
TGROUP = [PLAB[divmod(ORBS[k][0], NCOV)[0]] for k in range(NORB)]
TSPLIT = [TGROUP.count(0), TGROUP.count(1)]
ONEORB = all(len(set(PLAB[divmod(x, NCOV)[0]] for x in o)) == 1 for o in ORBS)

ROWPC = [[-1] * NCOV for _ in range(NORB)]
for k in range(NORB):
    for x in ORBS[k]:
        i, j = divmod(x, NCOV)
        ROWPC[k][j] = i

# the full-group tables, got by gluing each legal table to its partner under a determinant minus one map
GLUE = {}
BIGOK = True
for k in range(NORB):
    i0, j0 = divmod(ORBS[k][0], NCOV)
    kk = WHICH[PERM[HGEN][i0] * NCOV + CPERM[HGEN][j0]]
    if kk == k:
        BIGOK = False
    GLUE[tuple(sorted((k, kk)))] = 1
NBIG = len(GLUE)
BIGROW = sorted(set(sum(1 for x in ORBS[a] + ORBS[b] if divmod(x, NCOV)[1] == 0) for (a, b) in GLUE))

# ------------------------------------------------------------------
# 5. the incidence, the derived census convention, and the family
# ------------------------------------------------------------------

INC = [[0] * NPI for _ in range(NCOV)]
for j in range(NCOV):
    for i in CS[j]:
        INC[j][i] = 1
RSUM = sorted(set(sum(r) for r in INC))
CSUM = sorted(set(sum(INC[j][i] for j in range(NCOV)) for i in range(NPI)))
RWANT = RSUM[0] // RDEG[0] if RDEG[0] else 0
RTIMES = RDEG[0]
CWANT = CSUM[0] // CDEG[-1] if CDEG[-1] else 0
CTIMES = CDEG[-1]
DERIVOK = (len(RSUM) == 1 and len(CSUM) == 1 and RWANT * RTIMES == RSUM[0] and CWANT * CTIMES == CSUM[0])

ITAB = sorted(set(WHICH[i * NCOV + j] for j in range(NCOV) for i in CS[j]))
ISPLIT = [sum(1 for k in ITAB if TGROUP[k] == 0), sum(1 for k in ITAB if TGROUP[k] == 1)]
INSIDE = all(INC[divmod(x, NCOV)[1]][divmod(x, NCOV)[0]] == 1 for k in ITAB for x in ORBS[k])
REB = [[0] * NPI for _ in range(NCOV)]
for k in ITAB:
    for x in ORBS[k]:
        i, j = divmod(x, NCOV)
        REB[j][i] += 1
REBOK = (REB == INC)

NPER = TSPLIT[0]
FWANT = RSUM[0] // BIGROW[0] if BIGROW and BIGROW[0] else 0
NFAMFULL = nCr(NBIG, FWANT)
NFAM = nCr(NPER, CWANT) * nCr(TSPLIT[1], CWANT)
REGOK = True
for m in [tuple(ITAB), tuple(sorted([k for k in range(NORB) if TGROUP[k] == 0][:CWANT]
                                    + [k for k in range(NORB) if TGROUP[k] == 1][:CWANT]))]:
    rr = [0] * NCOV
    cc = [0] * NPI
    for k in m:
        for x in ORBS[k]:
            i, j = divmod(x, NCOV)
            rr[j] += 1
            cc[i] += 1
    if sorted(set(rr)) != [RSUM[0]] or sorted(set(cc)) != [CSUM[0]]:
        REGOK = False

# ------------------------------------------------------------------
# 6. the row census
# ------------------------------------------------------------------

CSET = set(frozenset(c) for c in CS)
C0 = 0
TOFP = dict((ROWPC[k][C0], k) for k in range(NORB))
ROWBIJ = (len(TOFP) == NORB)


def rowok(ks):
    for c in range(NCOV):
        if frozenset(ROWPC[k][c] for k in ks) not in CSET:
            return False
    return True


ROWMEM = []
ROWSPL = set()
for d in range(NCOV):
    ks = frozenset(TOFP[p] for p in CS[d])
    if len(ks) == RWANT and rowok(ks):
        ROWMEM.append(ks)
        ROWSPL.add((sum(1 for k in ks if TGROUP[k] == 0), sum(1 for k in ks if TGROUP[k] == 1)))
ROWSET = set(ROWMEM)
NROW = len(ROWSET)

# ------------------------------------------------------------------
# 7. the column census
# ------------------------------------------------------------------

COLOF = [frozenset(j for j in range(NCOV) if INC[j][i] == 1) for i in range(NPI)]
COLDIST = len(set(COLOF))
FIXS = [i for i in range(NPI) if PERM[SGEN][i] == i]
FIXSPL = [sum(1 for i in FIXS if PLAB[i] == w) for w in (0, 1)]
FIXCOV = sum(1 for j in range(NCOV) if CPERM[SGEN][j] == j)
PREPS = [PORB[0][0], -1]
for i in FIXS:
    if PLAB[i] == 1:
        PREPS[1] = i
        break
SAMEHOLD = (PREPS[1] >= 0 and set(e for e in GP if PERM[e][PREPS[0]] == PREPS[0])
            == set(e for e in GP if PERM[e][PREPS[1]] == PREPS[1]))

COLCEN = [[], []]
COLCAND = [0, 0]
COLPART = True
for w in (0, 1):
    p0 = PREPS[w]
    tof = {}
    cnt = {}
    for j in range(NCOV):
        k = WHICH[p0 * NCOV + j]
        tof[j] = k
        cnt[k] = cnt.get(k, 0) + 1
        if TGROUP[k] != w:
            COLPART = False
    if sorted(set(cnt.values())) != [CTIMES] or len(cnt) != TSPLIT[w]:
        COLPART = False
    cands = [q for q in range(NPI) if all(CPERM[SGEN][j] in COLOF[q] for j in COLOF[q])]
    COLCAND[w] = len(cands)
    for q in cands:
        ks = frozenset(tof[j] for j in COLOF[q])
        if len(ks) != CWANT:
            continue
        good = True
        for i in range(NPI):
            if PLAB[i] != w:
                continue
            cc = frozenset(divmod(x, NCOV)[1] for k in ks for x in ORBS[k] if divmod(x, NCOV)[0] == i)
            if cc not in set(COLOF):
                good = False
                break
        if good:
            COLCEN[w].append(ks)
COLN = [len(set(COLCEN[0])), len(set(COLCEN[1]))]
COLSET = set()
for a in set(COLCEN[0]):
    for b in set(COLCEN[1]):
        COLSET.add(a | b)
NCOL = len(COLSET)
CROSS = ROWSET & COLSET
NCROSS = len(CROSS)
INCIN = (frozenset(ITAB) in ROWSET, frozenset(ITAB) in CROSS)

# ------------------------------------------------------------------
# 8. the equivariant maps on each side, and the intertwining
# ------------------------------------------------------------------

COVMAPS = []
for tgt in range(NCOV):
    phi = [-1] * NCOV
    for e in GP:
        phi[CPERM[e][0]] = CPERM[e][tgt]
    if min(phi) < 0:
        continue
    if not all(tuple(phi[CPERM[e][c]] for c in range(NCOV)) == tuple(CPERM[e][phi[c]] for c in range(NCOV)) for e in GP):
        continue
    if len(set(phi)) != NCOV:
        continue
    COVMAPS.append(tuple(phi))
NCM = len(COVMAPS)

HOLD = [[e for e in GP if PERM[e][PREPS[w]] == PREPS[w]] for w in (0, 1)]
ADM = [[t for t in range(NPI) if all(PERM[e][t] == t for e in HOLD[w])] for w in (0, 1)]
WELLDEF = len(ADM[0]) * len(ADM[1])
GALL = {}
for e in GP:
    for w in (0, 1):
        GALL.setdefault((w, PERM[e][PREPS[w]]), []).append(e)
GSIZE = sorted(set(len(v) for v in GALL.values()))
PIECEMAPS = []
CONSIST = True
for tA in ADM[0]:
    for tB in ADM[1]:
        psi = [-1] * NPI
        for w in (0, 1):
            tgt = tA if w == 0 else tB
            for i in PORB[w]:
                vs = set(PERM[e][tgt] for e in GALL[(w, i)])
                if len(vs) != 1:
                    CONSIST = False
                psi[i] = sorted(vs)[0]
        if min(psi) < 0:
            continue
        if not all(tuple(psi[PERM[e][i]] for i in range(NPI)) == tuple(PERM[e][psi[i]] for i in range(NPI)) for e in GP):
            continue
        if len(set(psi)) != NPI:
            continue
        PIECEMAPS.append(tuple(psi))
NPM = len(PIECEMAPS)
KEEPO = sum(1 for p in PIECEMAPS if PLAB[p[PREPS[0]]] == 0)
SWAPO = sum(1 for p in PIECEMAPS if PLAB[p[PREPS[0]]] == 1)
ISOAB = sum(1 for p in PIECEMAPS if PLAB[p[PREPS[0]]] == 1 and PLAB[p[PREPS[1]]] == 0)

COVKEY = dict((frozenset(c), j) for j, c in enumerate(CS))
IND = []
for psi in PIECEMAPS:
    back = [0] * NPI
    for i in range(NPI):
        back[psi[i]] = i
    im = []
    ok = True
    for c in range(NCOV):
        k = COVKEY.get(frozenset(back[p] for p in CS[c]))
        if k is None:
            ok = False
            break
        im.append(k)
    IND.append(tuple(im) if ok else None)

NCANDP = 0
WIN = []
for u in range(NCM):
    for v in range(NPM):
        NCANDP += 1
        if IND[v] is not None and IND[v] == COVMAPS[u]:
            WIN.append((u, v))


def entrywise(u, v):
    phi = COVMAPS[u]
    psi = PIECEMAPS[v]
    return all(INC[phi[c]][p] == INC[c][psi[p]] for c in range(NCOV) for p in range(NPI))


CENT = [e for e in range(NGRP) if all(MUL[e][f] == MUL[f][e] for f in range(NGRP))]
WINOK = all(entrywise(u, v) for (u, v) in WIN)
WINCEN = all(any(tuple(CPERM[z]) == COVMAPS[u] and tuple(PERM[z]) == PIECEMAPS[v] for z in CENT) for (u, v) in WIN)
SAMPLE = [(u, v) for u in range(0, NCM, 47) for v in range(0, NPM, 41)][:8]
SAMPOK = all(entrywise(u, v) == (IND[v] is not None and IND[v] == COVMAPS[u]) for (u, v) in SAMPLE)
SAMPNEG = sum(1 for (u, v) in SAMPLE if not entrywise(u, v))

# ------------------------------------------------------------------
# 9. normalizer arithmetic on both holders
# ------------------------------------------------------------------

CLSF = set(MUL[MUL[g][SGEN]][INVE[g]] for g in range(NGRP))
CLSH = set(MUL[MUL[g][SGEN]][INVE[g]] for g in GP)
CENS = [e for e in range(NGRP) if MUL[e][SGEN] == MUL[SGEN][e]]
CENSIN = set(CENS) <= GPS
NORMS = [e for e in GP if MUL[MUL[e][SGEN]][INVE[e]] in (ID, SGEN)]
NORMIDX = len(NORMS) // 2
NORBSZ = sorted(set(len(set(PERM[e][PREPS[w]] for e in NORMS)) for w in (0, 1)))
CENH = [e for e in range(NGRP) if MUL[e][HGEN] == MUL[HGEN][e]]
HFIXP = sum(1 for i in range(NPI) if PERM[HGEN][i] == i)
HFIXC = sum(1 for j in range(NCOV) if CPERM[HGEN][j] == j)

# ------------------------------------------------------------------
# 10. the four local candidate labels
# ------------------------------------------------------------------

F1 = []
F2 = []
F3 = []
F4 = []
for i in range(NPI):
    S = KEPT[USED[i]]
    v0 = CORN[S[0]]
    M = [[CORN[S[j + 1]][r] - v0[r] for j in range(4)] for r in range(4)]
    F1.append(1 if det4(M) > 0 else -1)
    F2.append(sum(1 for c in S if par(bin(c).count("1")) == 0))
    F3.append(par(sum(S)))
    F4.append(par(sum(bin(c).count("1") for c in S)))
CANDN = ("det sign", "even corners", "index parity", "coordinate parity")
CANDF = (F1, F2, F3, F4)
CANDSET = [[sorted(set(F[i] for i in PORB[w])) for w in (0, 1)] for F in CANDF]
CANDCON = [any(len(CANDSET[t][w]) == 1 for w in (0, 1)) for t in range(4)]
CANDINV = [all(F[PERM[e][i]] == F[i] for e in GP for i in range(NPI)) for F in CANDF]

# ------------------------------------------------------------------
# 11. the perturbation rejector
# ------------------------------------------------------------------

INCROW = rowok(ITAB)
NTEST = 0
NREJ = 0
for pos in range(len(ITAB)):
    k0 = ITAB[pos]
    for alt in range(NORB):
        if alt == k0 or TGROUP[alt] != TGROUP[k0]:
            continue
        NTEST += 1
        if not rowok([k for k in ITAB if k != k0] + [alt]):
            NREJ += 1

# ------------------------------------------------------------------
# 12. the gates
# ------------------------------------------------------------------

gate(NCAND == 2672 and FLOOR == 6 and NKEPT == 400 and NS == 15800 and SIZES == [24] and NPI == 192
     and PCSET == [1975] and NCOV == 192 and NGRP == 384 and GENERIC and COVEXACT and KEEPS and HOMOK, "J0",
     "rebuilt: {0} unimodular pieces, floor {1} with {2} there, {3} cuttings of {4}, {5} pieces in {6} each, {7} covers, group {8}".format(
         nd(NCAND), nd(FLOOR), nd(NKEPT), nd(NS), nd(SIZES[0]), nd(NPI), nd(PCSET[0]), nd(NCOV), nd(NGRP)))

gate(MATOK and AGREE == NGRP and DISAG > 0 and DISAG == 192 and DETVAL == [-1, 1] and DETMUL, "J1",
     "cofactor determinant equals axis-move sign times minus one to the flip count on {0} of {1} maps; parity-dropped form misses {2}".format(
         nd(AGREE), nd(NGRP), nd(DISAG)))

gate(NHALF == 192 and HCLOSED and HNORMAL and HINDEX == 2 and CSTDET == [-1] and PSTDET == [1]
     and HGENFLIP and not SGENFLIP, "J2",
     "the plus-one half is closed of order {0} and index {1}, normal under all {2} conjugations; cover holder {3}, piece holder {4}".format(
         nd(NHALF), nd(HINDEX), nd(NGRP), sl(CSTDET), sl(PSTDET)))

gate(MEAS_C == 1 and CORBSZ == [192] and CHOLD == [1] and MEAS_P == 2 and PORBSZ == [96] and PHOLD == [2]
     and PSTSZ == [2] and CSTSZ == [2], "J3",
     "under the half: covers {0} orbit of {1} with holder order {2}; pieces {3} orbits of {4} with holder order {5}".format(
         nd(MEAS_C), sl(CORBSZ), sl(CHOLD), nd(MEAS_P), sl(PORBSZ), sl(PHOLD)))

gate(PRED_CC == MEAS_C and PRED_PP == MEAS_P and PRED_CP != MEAS_C and PRED_PC != MEAS_P, "J4",
     ("cross rules both wrong: piece rule on covers says {0} against {1} seen, "
      "cover rule on pieces says {2} against {3} seen; own rules right").format(
         nd(PRED_CP), nd(MEAS_C), nd(PRED_PC), nd(MEAS_P)))

gate(NORB == 192 and OSZ == [192] and PAIRFREE == [1] and ALLONES and NPAIR == 36864, "J5",
     "the pair action is free: {0} orbit tables, every orbit of size {1}, {2} entries summing to the all-ones table".format(
         nd(NORB), sl(OSZ), nd(NPAIR)))

gate(RDEG == [1] and CDEG == [0, 2] and DERIVOK and RWANT == 8 and RTIMES == 1 and CWANT == 4 and CTIMES == 2, "J6",
     ("row degree {0} and nonzero column degree {1} measured; row sum {2} over {0} wants {3} labels once, "
      "column sum {4} over {1} wants {5} labels twice").format(
         nd(RDEG[0]), nd(CDEG[-1]), nd(RSUM[0]), nd(RWANT), nd(CSUM[0]), nd(CWANT)))

gate(TSPLIT == [96, 96] and ONEORB and OWNHIT == set([2]) and OWNCOL == set([96]) and REGOK and BIGOK
     and NBIG == 96 and BIGROW == [2] and FWANT == CWANT and NFAMFULL == 3321960 and NFAM == 11035418241600
     and NFAM == NFAMFULL * NFAMFULL, "J7",
     "tables split {0} and {1} by target orbit with {2} hits per own-orbit piece; {3} plus {3} unions are {4}-regular; {5} squared = {6}".format(
         nd(TSPLIT[0]), nd(TSPLIT[1]), nd(sorted(OWNHIT)[0]), nd(CWANT), nd(RSUM[0]), nd(NFAMFULL), nd(NFAM)))

gate(len(ITAB) == 8 and len(ITAB) == RWANT and INSIDE and REBOK and ISPLIT == [4, 4], "J8",
     "the cover incidence meets exactly {0} of the {1} tables, each met table lies wholly inside it, and the {0} sum back to it".format(
         nd(len(ITAB)), nd(NORB)))

gate(NROW == 192 and NROW == NCOV and len(ROWMEM) == NCOV and ROWBIJ and sorted(ROWSPL) == [(4, 4)], "J9",
     "row census {0}, one member for each of the {1} covers, and every member draws {2} tables from each of the two groups".format(
         nd(NROW), nd(NCOV), nd(sorted(ROWSPL)[0][0])))

gate(COLN == [16, 16] and NCOL == 256 and COLCAND == [16, 16] and COLPART and COLDIST == 192
     and SAMEHOLD and FIXSPL == [8, 8], "J10",
     "column census {0} on each piece orbit and {1} in product; each comes from one of the {2} piece columns the piece holder leaves alone".format(
         nd(COLN[0]), nd(NCOL), nd(COLCAND[0])))

gate(NCROSS == 2 and INCIN == (True, True), "J11",
     "the row census and the column census cross in exactly {0} members; the cover incidence is in the row census and in the crossing".format(
         nd(NCROSS)))

gate(NCM == 192 and NPM == 128 and KEEPO == 64 and SWAPO == 64 and WELLDEF == 256 and ISOAB == 64
     and CONSIST and GSIZE == [2] and [len(ADM[0]), len(ADM[1])] == [16, 16], "J12",
     "equivariant cover maps {0}; piece maps {1} = {2} orbit-preserving plus {3} orbit-swapping, gated on {4} maps; orbits alike".format(
         nd(NCM), nd(NPM), nd(KEEPO), nd(SWAPO), nd(NHALF)))

gate(NCANDP == 24576 and len(WIN) == 2 and WINOK and WINCEN and len(CENT) == 2 and SAMPOK and SAMPNEG > 0, "J13",
     "{0} candidate pairs, exactly {1} intertwining, each winner the pair of actions of one of the {2} central maps of the group".format(
         nd(NCANDP), nd(len(WIN)), nd(len(CENT))))

gate(len(CLSF) == 12 and len(CLSH) == 12 and len(CENS) == 32 and not CENSIN and len(NORMS) == 16
     and NORMIDX == 8 and NORBSZ == [8] and len(FIXS) == 16 and FIXSPL == [8, 8] and FIXCOV == 0
     and len(CENH) == 96 and HFIXP == 0 and HFIXC == 48, "J14",
     ("class {0} unsplit, centraliser {1} outside the half, normalizer {2}, index {3}, "
      "fixes {4} pieces as {5}+{5} and {6} covers; flip {7}/{6}/{8}").format(
         nd(len(CLSF)), nd(len(CENS)), nd(len(NORMS)), nd(NORMIDX), nd(len(FIXS)), nd(FIXSPL[0]), nd(FIXCOV),
         nd(len(CENH)), nd(HFIXC)))

gate((not any(CANDCON)) and (not any(CANDINV)), "J15",
     "none constant on an orbit: {0} {1} and {2}, {3} {4} and {5}, {6} {7} and {8}, {9} {10} and {11}".format(
         CANDN[0], sl(CANDSET[0][0]), sl(CANDSET[0][1]), CANDN[1], sl(CANDSET[1][0]), sl(CANDSET[1][1]),
         CANDN[2], sl(CANDSET[2][0]), sl(CANDSET[2][1]), CANDN[3], sl(CANDSET[3][0]), sl(CANDSET[3][1])))

gate(INCROW and NTEST >= 20 and NREJ == NTEST and NTEST == 760, "J16",
     "{0} single-table swaps inside the same group tested and {1} rejected by the row census test".format(
         nd(NTEST), nd(NREJ)))

emit("TOTAL: PASS={0} FAIL={1}".format(nd(STAT[0]), nd(STAT[1])))
if STAT[1]:
    sys.exit(1)
