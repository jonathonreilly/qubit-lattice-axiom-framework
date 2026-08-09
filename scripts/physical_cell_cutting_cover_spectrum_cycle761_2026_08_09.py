"""Exact finite certificates for the eight-piece Gram and its row-space characters.

Every count below is measured here. The runner rebuilds the cell complex, the least
volume pieces, the cuttings at the adjacency cost floor, the cutting by piece table
and the sets of eight pieces no two of which share a cutting. Each such set is shown
here to meet every cutting exactly once. It forms the eight set by piece table M and
the Gram
S = M M transpose, then reads the spectrum of S exactly: ten whole values with their
multiplicities, three quadratic families and one cubic family, each factor shown to
be unbreakable over the whole numbers, with the fourteen nullities adding to the full
size and the product of the fourteen factors killing the matrix. A sum-of-roots
checksum reproduces the trace. It then builds the maps obtained by permuting the four
coordinates of the four-cube and flipping any of them, certifies whole-number
multiples of the orthogonal projectors onto the row spaces of the two tables, proves
that those projectors are invariant under every map, and averages their characters.
Fixed corruptions exercise the rebuild, spectrum, sharing-relation, group-action, and
projector-invariance check families.
"""
import itertools
import math
import resource
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 300

T0 = time.monotonic()
PF = [0, 0]
OUT = [0]


def emit(s):
    """print one line, refusing any barred digit pair or over-long line"""
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    if len(txt) > 149:
        raise ValueError("line over the length limit")
    OUT[0] += len(txt) + 1
    print(txt)


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    emit(("PASS " if ok else "FAIL ") + name + "  " + detail)


def joins(xs):
    """one space separated string of a sequence of integers"""
    return " ".join(str(int(x)) for x in xs)


def pairs(ks, d):
    """a value to count mapping as a compact key:value string"""
    return " ".join("{0}:{1}".format(k, d[k]) for k in ks)


# ---------------------------------------------------------------- Part 1: the rebuild


def det4(A):
    def minors(r0, r1):
        out = {}
        for i in range(4):
            for j in range(i + 1, 4):
                out[(i, j)] = (A[:, r0, i] * A[:, r1, j] - A[:, r0, j] * A[:, r1, i])
        return out
    m, c = minors(0, 1), minors(2, 3)
    return (m[(0, 1)] * c[(2, 3)] - m[(0, 2)] * c[(1, 3)] + m[(0, 3)] * c[(1, 2)]
            + m[(1, 2)] * c[(0, 3)] - m[(1, 3)] * c[(0, 2)] + m[(2, 3)] * c[(0, 1)])


CORN = [(x, y, z, t) for x in (0, 1) for y in (0, 1) for z in (0, 1) for t in (0, 1)]
V = np.array(CORN, dtype=np.int64)
POS = dict((c, i) for i, c in enumerate(CORN))
PAIRS = list(itertools.combinations(range(5), 2))
SUB = np.array(list(itertools.combinations(range(16), 5)), dtype=np.int64)
VOL = np.abs(det4(V[SUB[:, 1:]] - V[SUB[:, 0]][:, None, :]))
UNI = SUB[VOL == 1]
NPIECE = len(UNI)


def cost(P, cols):
    """the count of corner pairs of each piece more than one lattice step apart"""
    tot = np.zeros(len(P), dtype=np.int64)
    for a, b in PAIRS:
        d = np.abs(V[P[:, a]][:, cols] - V[P[:, b]][:, cols]).sum(axis=1)
        tot = tot + (d > 1).astype(np.int64)
    return tot


C4 = cost(UNI, [0, 1, 2, 3])
LO = int(C4.min())
MINP = [i for i in range(NPIECE) if int(C4[i]) == LO]
MM = np.stack([(V[p[1:]] - V[p[0]]).T for p in UNI])
IV = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)

ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if int(round(np.linalg.det(R.astype(float)))) == 1:
            ROT.append(R)
CEN = np.array([1, 1, 1], dtype=np.int64)
GG = []
for R in ROT:
    for tf in (0, 1):
        img = []
        for (x, y, z, t) in CORN:
            w = R @ (2 * np.array([x, y, z], dtype=np.int64) - CEN) + CEN
            key = (int(w[0]) // 2, int(w[1]) // 2, int(w[2]) // 2, (1 - t) if tf else t)
            if key not in POS:
                img = None
                break
            img.append(POS[key])
        if img is not None:
            GG.append((R, tf, np.array(img, dtype=np.int64)))

posp = dict((tuple(int(c) for c in s), i) for i, s in enumerate(UNI))
LAB = -np.ones(NPIECE, dtype=np.int64)
REPS = []
for i in range(NPIECE):
    if LAB[i] >= 0:
        continue
    o = len(REPS)
    REPS.append(i)
    for (_, _, g) in GG:
        LAB[posp[tuple(sorted(int(g[c]) for c in UNI[i]))]] = o
REPS = np.array(REPS, dtype=np.int64)

OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
SC = np.array([SB // 2, SB // 2, SB // 2], dtype=np.int64)
lab = {}
for o, i in enumerate(REPS):
    q = (WT[:, None] * V[UNI[i]]).sum(axis=0)
    for (R, tf, _) in GG:
        u = R @ (q[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]), (SB - int(q[3])) if tf else int(q[3]))
        lab.setdefault(key, o)
KEYS = sorted(lab)
Q = np.array(KEYS, dtype=np.int64)
NQ = len(Q)
QT = Q.T
MASK = []
MI = np.zeros((NPIECE, NQ), dtype=np.int8)
for i in range(NPIECE):
    lam = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lam.sum(axis=0)
    ins = (lam > 0).all(axis=0) & (tot < SB)
    MI[i] = ins.astype(np.int8)
    b = 0
    for j in np.flatnonzero(ins):
        b |= 1 << int(j)
    MASK.append(b)
ALLQ = (1 << NQ) - 1

BY, MK = {}, dict((i, MASK[i]) for i in MINP)
for i in MINP:
    for j in np.flatnonzero(MI[i]):
        BY.setdefault(int(j), []).append(i)
SOL = []


def rec(cov, chosen):
    """collect every cutting: complete search over the pieces at the cost floor"""
    if cov == ALLQ:
        SOL.append(tuple(sorted(chosen)))
        return
    rem = ALLQ & ~cov
    j = (rem & -rem).bit_length() - 1
    for i in BY[j]:
        if MK[i] & cov:
            continue
        chosen.append(i)
        rec(cov | MK[i], chosen)
        chosen.pop()


rec(0, [])
NS = len(SOL)
USED = sorted(set(i for s in SOL for i in s))
NPO = len(USED)
P2I = dict((p, a) for a, p in enumerate(USED))

# Two zero-one 4-simplices have disjoint interiors exactly when a supporting
# direction separates them.  An extreme separating direction is orthogonal to
# three ternary vertex-difference vectors, so its 3-by-3 minors have magnitude
# at most four.  The finite direction sweep therefore decides disjointness.
DIR = np.array([d for d in itertools.product(range(-4, 5), repeat=4) if any(d)],
               dtype=np.int64)
PV = V[UNI[USED]]
DPROJ = np.tensordot(DIR, PV, axes=([1], [2]))
DHI = DPROJ.max(axis=2).T
DLO = DPROJ.min(axis=2).T
SEP = np.eye(NPO, dtype=bool)
for a in range(NPO):
    for b in range(a + 1, NPO):
        ok = bool((DHI[a] <= DLO[b]).any()) or bool((DHI[b] <= DLO[a]).any())
        SEP[a, b] = SEP[b, a] = ok
del DPROJ, DHI, DLO

CUT_LOCAL = [[P2I[p] for p in s] for s in SOL]
DISJOINT = all(SEP[np.ix_(s, s)].sum() == len(s) * len(s) for s in CUT_LOCAL)

INC = np.zeros((NS, NPO), dtype=np.uint8)
for i, s in enumerate(SOL):
    for p in s:
        INC[i, P2I[p]] = 1
INCL = INC.astype(np.int64)
RW = INC.sum(axis=1).astype(np.int64)
CS = INC.sum(axis=0).astype(np.int64)

CM = np.zeros(NPIECE, dtype=np.int64)
for i in range(NPIECE):
    b = 0
    for t in UNI[i]:
        b |= 1 << int(t)
    CM[i] = b
M2I = dict((int(CM[i]), i) for i in range(NPIECE))

INT = INCL.astype(np.int32)
GR = (INT.T @ INT).astype(np.int64)
NSH = (GR == 0)
np.fill_diagonal(NSH, False)
ADJ = [0] * NPO
for a in range(NPO):
    m = 0
    for b in np.flatnonzero(NSH[a]):
        m |= 1 << int(b)
    ADJ[a] = m
CLQ = []


def extend(cur, cand):
    """collect every set of eight pieces no two of which lie on a common cutting"""
    if len(cur) == 8:
        CLQ.append(tuple(cur))
        return
    c = cand
    while c:
        low = c & -c
        v = low.bit_length() - 1
        c ^= low
        extend(cur + [v], c & ADJ[v])


extend([], (1 << NPO) - 1)
NC = len(CLQ)
M = np.zeros((NC, NPO), dtype=np.int64)
for i, s in enumerate(CLQ):
    for p in s:
        M[i, int(p)] = 1
S = M @ M.T
IDN = np.eye(NC, dtype=np.int64)


# ------------------------------------------------- Part 2: exact integer machinery

PMOD = 1000003


def rank_exact(rows):
    """exact rank over the rationals of an integer matrix, integer arithmetic only

    One step fraction free elimination: each combined row is divided through by
    the greatest common divisor of its entries, so no denominator is ever needed
    and no floating point is used.
    """
    wk = [[int(x) for x in r] for r in rows]
    nr = len(wk)
    if nr == 0:
        return 0
    m = len(wk[0])
    rk = 0
    for col in range(m):
        piv = -1
        for r in range(rk, nr):
            if wk[r][col]:
                piv = r
                break
        if piv < 0:
            continue
        wk[rk], wk[piv] = wk[piv], wk[rk]
        pr = wk[rk]
        pv = pr[col]
        for r in range(rk + 1, nr):
            f = wk[r][col]
            if f:
                rw = wk[r]
                nw = [0] * col + [pv * rw[c] - f * pr[c] for c in range(col, m)]
                g = 0
                for x in nw:
                    if x:
                        g = math.gcd(g, x if x > 0 else -x)
                        if g == 1:
                            break
                if g > 1:
                    nw = [x // g for x in nw]
                wk[r] = nw
        rk += 1
    return rk


def nullity(A):
    """the exact nullity of a square integer matrix"""
    return A.shape[0] - rank_exact(A.tolist())


def basis_rows(A, p):
    """indices of rows forming a basis of the row space over the field with p"""
    W2 = np.mod(A, p).astype(np.int64)
    n, m = W2.shape
    rowsel = []
    used = [False] * n
    for c in range(m):
        colv = W2[:, c].tolist()
        i = -1
        for r in range(n):
            if not used[r] and colv[r]:
                i = r
                break
        if i < 0:
            continue
        used[i] = True
        rowsel.append(i)
        inv = pow(int(W2[i, c]), p - 2, p)
        W2[i] = np.mod(W2[i] * inv, p)
        hit = np.nonzero(W2[:, c])[0]
        hit = hit[hit != i]
        if hit.size:
            W2[hit] = np.mod(W2[hit] - np.outer(W2[hit, c], W2[i]), p)
    return rowsel


def liftN(A, D):
    """the exact integer matrix D times the projector onto the row space of A

    The projector is formed over the field with PMOD elements from a basis of the
    row space, multiplied by D, and each entry lifted into the range symmetric about
    zero. That step only proposes the lift. The whole number identities N N = D N
    and N A transpose = D A transpose, checked by the caller, are what certify it.
    """
    rows = basis_rows(A, PMOD)
    B = np.mod(A[rows], PMOD).astype(np.int64)
    k = len(rows)
    aug = np.concatenate([np.mod(B @ B.T, PMOD), B], axis=1)
    for c in range(k):
        nz = [i for i in range(c, k) if aug[i, c]]
        aug[[c, nz[0]]] = aug[[nz[0], c]]
        aug[c] = np.mod(aug[c] * pow(int(aug[c, c]), PMOD - 2, PMOD), PMOD)
        hit = np.nonzero(aug[:, c])[0]
        hit = hit[hit != c]
        if hit.size:
            aug[hit] = np.mod(aug[hit] - np.outer(aug[hit, c], aug[c]), PMOD)
    Pm = np.mod(B.T @ aug[:, k:], PMOD)
    N = np.mod(Pm * D, PMOD)
    N = np.where(N > PMOD // 2, N - PMOD, N).astype(np.int64)
    return N, k


def polymat(co):
    """a whole number polynomial evaluated at S by Horner, coefficients high first"""
    R = np.zeros((NC, NC), dtype=np.int64)
    for c in co:
        R = R @ S + int(c) * IDN
    return R


def sqfree(n):
    """whether a nonnegative whole number fails to be a perfect square"""
    r = math.isqrt(int(n))
    return r * r != int(n)


# ---------------------------------------------------- Part 3: the piece relabellings


def colperm(img):
    """a map of the 16 corners turned into a permutation of the pieces"""
    out = [0] * NPO
    for a, p in enumerate(USED):
        w = 0
        for c in range(16):
            if (int(CM[p]) >> c) & 1:
                w |= 1 << img[c]
        out[a] = P2I[M2I[w]]
    return tuple(out)


FULL = []
for perm in itertools.permutations(range(4)):
    for sg in itertools.product((0, 1), repeat=4):
        img = tuple(POS[tuple(c[perm[i]] ^ sg[i] for i in range(4))] for c in CORN)
        FULL.append(colperm(img))
PA = np.array(FULL, dtype=np.int64)
NG = len(FULL)
IDX = np.arange(NPO)
CPERM = np.array([int((PA[i] == IDX).sum()) for i in range(NG)], dtype=np.int64)
PERMOK = bool((np.sort(PA, axis=1) == IDX[None, :]).all())
FULLSET = set(FULL)
GROUP_CLOSED = all(tuple(a[b[j]] for j in range(NPO)) in FULLSET
                   for a in FULL for b in FULL)
BAD_PA = PA.copy()
BAD_PA[0, 0] = BAD_PA[0, 1]
GROUP_MUTATION_CAUGHT = not bool((np.sort(BAD_PA, axis=1) == IDX[None, :]).all())

ORB = set([0])
FRONT = [0]
while FRONT:
    x = FRONT.pop()
    for pm in FULL:
        y = pm[x]
        if y not in ORB:
            ORB.add(y)
            FRONT.append(y)

REMS = [0]


def counting(A, D, want):
    """the character of an invariant row space, with its integer certificate"""
    N, k = liftN(A, D)
    NO = N.astype(object)
    AO = A.astype(np.int64)
    sym = bool((N == N.T).all())
    idm = bool((NO @ NO == D * NO).all())
    fix = bool((N @ AO.T == D * AO.T).all())
    inv = all(bool((N[np.ix_(pm, pm)] == N).all()) for pm in PA)
    rk = rank_exact((AO.T @ AO).tolist())
    tr = int(np.trace(N))
    vals = []
    for i in range(NG):
        q, r = divmod(int(N[PA[i], IDX].sum()), D)
        REMS[0] += r
        vals.append(q)
    ok = sym and idm and fix and inv and tr == D * rk and rk == want and k == want
    return np.array(vals, dtype=np.int64), rk, ok, N


def avg(u, v):
    """the average of a product of two counting functions over the relabellings"""
    q, r = divmod(int((u * v).sum()), NG)
    REMS[0] += r
    return q


# ------------------------------------------------------ Part 4: the object and gates

emit("Every count below is measured here.")
emit("the object: {0} cuttings and {1} pieces, {2} pieces to a cutting, {3} cuttings "
     "through a piece".format(NS, NPO, int(RW.min()), int(CS.min())))
gate(NS == 15800 and NPO == 192 and int(RW.min()) == int(RW.max()) == 24
     and int(CS.min()) == int(CS.max()) == 1975 and DISJOINT, "object census",
     "all sample covers are pairwise interior-disjoint; the two incidence degrees "
     "are constant")

MV = sorted(set(M.ravel().tolist()))
MR = sorted(set(M.sum(axis=1).tolist()))
MK2 = sorted(set(M.sum(axis=0).tolist()))
gate(MV == [0, 1] and MR == [8] and MK2 == [8] and NC == 192, "eight-set table",
     "M is {0} eight piece sets by {1} pieces, entries {2}, every row sum {3}, every "
     "column sum {4}".format(NC, NPO, joins(MV), MR[0], MK2[0]))


def det3(R):
    """the exact whole number determinant of a three by three integer matrix"""
    return int(R[0, 0] * (R[1, 1] * R[2, 2] - R[1, 2] * R[2, 1])
               - R[0, 1] * (R[1, 0] * R[2, 2] - R[1, 2] * R[2, 0])
               + R[0, 2] * (R[1, 0] * R[2, 1] - R[1, 1] * R[2, 0]))


IDF = np.eye(4, dtype=np.int64)
FRM = bool((MM @ IV == IDF[None, :, :]).all())
RD = sorted(set(det3(R) for R in ROT))
gate(FRM and len(ROT) == 24 and RD == [1] and len(GG) == 48, "piece frames",
     "all {0} piece frames invert exactly over the whole numbers, and the {1} "
     "rotations behind the sample points have determinant {2}".format(
         NPIECE, len(ROT), RD[0]))

HIT = INCL @ M.T
HV = sorted(set(HIT.ravel().tolist()))
DBL = int(HIT.sum())
gate(HV == [1] and DBL == NS * NC and DBL == NPO * int(CS.min()) * MR[0]
     and NPO == int(RW.min()) * MK2[0] and NS == MR[0] * int(CS.min()),
     "exact-cover double count",
     "every eight piece set meets every cutting exactly once, so {0} = {1} times {2} "
     "and {3} = {4} times {5}".format(
         NPO, int(RW.min()), MK2[0], NS, MR[0], int(CS.min())))

MBAD = M.copy()
MBAD[0, 0] = 1 - MBAD[0, 0]
BAD_TABLE_OK = (sorted(set(MBAD.sum(axis=1).tolist())) == [8]
                and sorted(set(MBAD.sum(axis=0).tolist())) == [8]
                and bool((INCL @ MBAD.T == 1).all()))
BAD_CUT = list(CUT_LOCAL[0])
BAD_CUT[-1] = 0
BAD_COVER = sum(MI[USED[p]].astype(np.int64) for p in BAD_CUT)
BAD_DISJOINT = bool(SEP[np.ix_(BAD_CUT, BAD_CUT)].all())
gate(not BAD_TABLE_OK and not bool((BAD_COVER == 1).all()) and not BAD_DISJOINT,
     "rebuild mutation control",
     "a fixed table-bit flip and a fixed piece replacement are both detected")

SD = sorted(set(np.diag(S).tolist()))
SR = sorted(set(S.sum(axis=1).tolist()))
TR = int(np.trace(S))
gate(bool((S == S.T).all()) and SD == [8] and SR == [64] and TR == 1536
     and TR == NC * SD[0], "Gram invariants",
     "S symmetric, diagonal {0}, row sum {1}, trace {2} = {3} times {4}".format(
         SD[0], SR[0], TR, NC, SD[0]))

WHOLE = [(0, 87), (2, 8), (4, 8), (8, 3), (10, 8), (12, 6), (16, 2), (20, 10),
         (24, 3), (64, 1)]
QUAD = [((1, -20, 80), 6), ((1, -44, 400), 6), ((1, -52, 320), 4)]
CUBE = ((1, -44, 516, -1280), 8)

FACTS = [((1, -v), mu, 1) for v, mu in WHOLE]
FACTS += [(co, mu, 2) for co, mu in QUAD]
FACTS += [(CUBE[0], CUBE[1], 3)]
NUL = [nullity(polymat(co)) for co, mu, dg in FACTS]

WM = [NUL[i] for i in range(10)]
emit("whole part of the spectrum, value:multiplicity  "
     + pairs([v for v, mu in WHOLE], dict((WHOLE[i][0], WM[i]) for i in range(10)))
     + ", adding to {0}".format(sum(WM)))
gate(WM == [mu for v, mu in WHOLE] and sum(WM) == 136, "integer spectrum",
     "each whole candidate has the nullity claimed for it and the ten of them carry "
     "{0} of the {1}".format(sum(WM), NC))

emit("non whole factors, high coefficient first, by multiplicity: " + "; ".join(
    "{0} by {1}".format(joins(co), NUL[10 + i] // dg)
    for i, (co, mu, dg) in enumerate(FACTS[10:])))

QN = NUL[10:13]
gate(QN == [2 * mu for co, mu in QUAD] and sum(QN) == 32, "quadratic spectrum",
     "the three quadratic factors have nullity {0}, twice the multiplicities {1}, "
     "adding to {2}".format(joins(QN), joins([mu for co, mu in QUAD]), sum(QN)))

gate(NUL[13] == 3 * CUBE[1] and NUL[13] == 24, "cubic spectrum",
     "the cubic factor has nullity {0}, three times the multiplicity {1}".format(
         NUL[13], CUBE[1]))

gate(sum(NUL) == 192 and sum(NUL) == NC, "spectrum completeness",
     "the fourteen nullities add to {0}, the full size of S; {1} whole and {2} "
     "not".format(sum(NUL), sum(WM), sum(NUL[10:])))

RUN = np.zeros((NC, NC), dtype=object)
for i in range(NC):
    RUN[i, i] = 1
for co, mu, dg in FACTS:
    RUN = polymat(co).astype(object) @ RUN
NZP = int((RUN != 0).sum())
gate(NZP == 0, "annihilating polynomial",
     "the fourteen factors multiplied one at a time leave {0} nonzero entries, so "
     "their product kills S over the whole numbers".format(NZP))

DIFF = len(set(co for co, mu, dg in FACTS)) == 14
DISC = [co[1] * co[1] - 4 * co[0] * co[2] for co, mu in QUAD]
a, b, c, d = CUBE[0]
DC = (18 * a * b * c * d - 4 * b ** 3 * d + b * b * c * c - 4 * a * c ** 3
      - 27 * a * a * d * d)
CAND = []
for k in range(1, abs(d) + 1):
    if divmod(abs(d), k)[1] == 0:
        CAND.extend([k, -k])
HITS = [x for x in CAND if a * x ** 3 + b * x * x + c * x + d == 0]
emit("irreducibility: quadratic discriminants {0}, cubic {1}, none a perfect "
     "square; {2} cubic root candidates tried, {3} worked".format(
         joins(DISC), DC, len(CAND), len(HITS)))
gate(DIFF and all(sqfree(x) for x in DISC) and DISC == [80, 336, 1424]
     and len(CAND) == 36 and HITS == [] and DC == 8640512 and sqfree(DC),
     "irreducible factors",
     "the fourteen factors are pairwise different and none of the four non whole "
     "ones breaks up over the whole numbers")

TW = sum(v * WM[i] for i, (v, mu) in enumerate(WHOLE))
TQ = sum(-co[1] * (QN[i] // 2) for i, (co, mu) in enumerate(QUAD))
TC = -b * (NUL[13] // 3)
gate(TW == 592 and TQ == 592 and TC == 352 and TW + TQ + TC == TR,
     "trace checksum",
     "trace checksum from the sums of roots: {0} + {1} + {2} = {3}, the measured trace "
     "of S".format(TW, TQ, TC, TW + TQ + TC))

BAD = np.zeros((NC, NC), dtype=object)
for i in range(NC):
    BAD[i, i] = 1
for co, mu, dg in FACTS[:13]:
    BAD = polymat(co).astype(object) @ BAD
BAD = polymat((a, b, c, d - 1)).astype(object) @ BAD
NZB = int((BAD != 0).sum())
ALT = sum(NUL) - WM[7] + 9
gate(NZB > 0 and NZB == 33024 and WM[7] == 10 and ALT == 191 and ALT != NC,
     "spectrum mutation control",
     "changed cubic leaves {0} nonzeros; multiplicity {1} at {2} gives total {3}".format(
         NZB, 9, WHOLE[7][0], ALT))

CBIT = []
for s in CLQ:
    w = 0
    for p in s:
        w |= 1 << int(p)
    CBIT.append(w)
SHOK = all(bin(CBIT[i] & CBIT[j]).count("1") == int(S[i, j])
           for i in range(NC) for j in range(NC) if i != j)
OFFV = sorted(set(int(S[i, j]) for i in range(NC) for j in range(NC) if i != j))
ROWC = set()
for i in range(NC):
    row = [int(S[i, j]) for j in range(NC) if j != i]
    ROWC.add(tuple(row.count(v) for v in OFFV))
RC = sorted(ROWC)[0]
NDIST = sum(dg for (co, mu, dg), nl in zip(FACTS, NUL) if nl > 0)
NDW = sum(dg for (co, mu, dg), nl in zip(FACTS[:10], NUL[:10]) if nl > 0)
NDN = NDIST - NDW
DIAG = np.eye(NC, dtype=bool)
REL = [IDN] + [((S == v) & ~DIAG).astype(np.int64) for v in OFFV]
RELATION_FORM = bool((S == 8 * REL[0] + REL[2] + 2 * REL[3] + 4 * REL[4]).all())
VAR_PRODUCTS = []
for ia, A in enumerate(REL):
    for ib, B in enumerate(REL):
        C = A @ B
        for ir, R in enumerate(REL):
            z = np.unique(C[R.astype(bool)])
            if len(z) > 1:
                VAR_PRODUCTS.append((ia, ib, ir, int(z.min()), int(z.max())))
                break
emit("sharing: {0} distinct off diagonal values; each of the {1} rows carries "
     "value:count ".format(len(OFFV), NC) + pairs(OFFV, dict(zip(OFFV, RC)))
     + ", adding to {0}".format(sum(RC)))
emit("product variation: {0} ordered pairs of sharing-relation matrices vary within "
     "at least one relation class".format(len(VAR_PRODUCTS)))
gate(SHOK and len(OFFV) == 4 and OFFV == [0, 1, 2, 4] and len(ROWC) == 1
     and sorted(RC, reverse=True) == [157, 20, 10, 4] and sum(RC) == 191
     and NDIST == 19 and NDW == 10 and NDN == 9 and RELATION_FORM
     and len(VAR_PRODUCTS) == 16 and VAR_PRODUCTS[0][:2] == (1, 1),
     "sharing product witnesses",
     "S has {0} distinct eigenvalues and {1} ordered relation products vary within a "
     "sharing class".format(NDIST, len(VAR_PRODUCTS)))

BAD_SHARING = S.copy()
BAD_SHARING[0, 1] += 1
BAD_SHARING[1, 0] += 1
BAD_SHARING_OK = all(bin(CBIT[i] & CBIT[j]).count("1") == int(BAD_SHARING[i, j])
                     for i in range(NC) for j in range(NC) if i != j)
gate(not BAD_SHARING_OK, "sharing mutation control",
     "a fixed corrupted shared-piece count is detected")

PP = avg(CPERM, CPERM)
gate(NG == 384 and len(set(FULL)) == 384 and len(ORB) == NPO and PP == 104
     and PERMOK and GROUP_CLOSED, "four-cube relabelling action",
     "{0} distinct permutations form a group on {1} pieces in one orbit; character "
     "norm {2}".format(NG, NPO, PP))
gate(GROUP_MUTATION_CAUGHT, "group-action mutation control",
     "a fixed duplicated image in one proposed map is detected")


def side(A, D, want, nm, tag, wv, wb, wx):
    """measure and gate one table's counting functions"""
    CV, rk, ok, N = counting(A, D, want)
    CB2 = CPERM - CV
    ONES = np.ones(NG, dtype=np.int64)
    vv, vb, bb = avg(CV, CV), avg(CV, CB2), avg(CB2, CB2)
    vt, bt = avg(CV, ONES), avg(CB2, ONES)
    tot = vv + bb + 2 * vb
    gate(ok and rk == want and vv == wv and bb == wb and vb == wx and vt == 1
         and bt == 0 and tot == PP, "{0}".format(tag),
         "{0} rank {1}, invariant: row-space {2}, complement {3}, cross {4}, constants "
         "{5} and {6}".format(nm, rk, vv, bb, vb, vt, bt))
    return CV, N


CVC, NCERT = side(INCL, 960, 88, "cutting", "cutting characters", 29, 33, 21)
CVE, ECERT = side(M, 320, 105, "eight-set", "eight-set characters", 34, 28, 21)

ONE = np.ones((1, NPO), dtype=np.int64)
CO, RKO, OKO, _ = counting(ONE, NPO, 1)
CR = CPERM - CO
XO, OO, RR = avg(CO, CR), avg(CO, CO), avg(CR, CR)
gate(OKO and RKO == 1 and sorted(set(CO.tolist())) == [1] and XO == 0
     and OO == 1 and RR == 103 and OO + RR + 2 * XO == PP,
     "character decomposition control",
     "the invariant all-ones line and its complement have cross inner product {0}; "
     "self inner products {1} and {2}".format(XO, OO, RR))

COORD = np.zeros((1, NPO), dtype=np.int64)
COORD[0, 0] = 1
_, _, COORD_OK, _ = counting(COORD, 1, 1)
gate(not COORD_OK, "character mutation control",
     "a fixed non-invariant coordinate line is rejected by the conjugation check")

gate(REMS[0] == 0, "exact character division",
     "every counting value and every average divides through with remainder {0} on "
     "both tables and on the control".format(REMS[0]))

ELAP = time.monotonic() - T0
RSS_DIVISOR = 1048576.0 if sys.platform == "darwin" else 1024.0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / RSS_DIVISOR
EBD = 300 * (int(ELAP // 300) + 1)
RBD = 500 * (int(RSS // 500) + 1)
gate(ELAP < AUDIT_TIMEOUT_SEC and RSS < 2500.0 and EBD <= AUDIT_TIMEOUT_SEC
     and RBD <= 2500, "resource bounds",
     "elapsed under {0} s and peak memory under {1} MB, measured in this run against "
     "limits of {2} s and {3} MB".format(EBD, RBD, AUDIT_TIMEOUT_SEC, 2500))

TOT = "TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1])
CNT = "stdout characters: {0}"
n = OUT[0] + len(TOT) + 1
for _ in range(6):
    n = OUT[0] + len(CNT.format(n)) + 1 + len(TOT) + 1
emit(CNT.format(n))
emit(TOT)
if PF[1]:
    raise SystemExit(1)
