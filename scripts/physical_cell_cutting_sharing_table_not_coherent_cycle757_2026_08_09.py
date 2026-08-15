"""Rebuild and gate finite identities of the unit-four-cube cutting system.

The runner constructs the cell complex, least-volume pieces, minimum-cost
cuttings, eight-piece exact covers, cover and piece sharing tables, selected
products of the sharing relations, one declared pair-colour refinement, the
declared spatial-rotation/time-flip action, and exact cover-difference ranks.
Two small four-cube controls exercise both uniform and heterogeneous product
value profiles.
"""
import itertools
import math
import resource
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 600

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


def mset(a):
    """value to count dictionary of an integer array"""
    v, c = np.unique(np.asarray(a), return_counts=True)
    return dict((int(x), int(y)) for x, y in zip(v, c))


def msets(d):
    """value:count string of a value to count dictionary"""
    return " ".join("{0}:{1}".format(k, d[k]) for k in sorted(d))

# ---------------------------------------------------------------- Part 1: machinery


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
I4 = np.eye(4, dtype=np.int64)
INV_OK = (
    np.array_equal(
        np.einsum("nij,njk->nik", MM, IV),
        np.broadcast_to(I4, MM.shape),
    )
    and np.array_equal(
        np.einsum("nij,njk->nik", IV, MM),
        np.broadcast_to(I4, MM.shape),
    )
)


def permutation_sign(perm):
    """Exact sign of a finite permutation."""
    inversions = sum(
        1
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
        if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1

ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if permutation_sign(perm) * math.prod(sg) == 1:
            ROT.append(R)
CEN = np.array([1, 1, 1], dtype=np.int64)
G = []
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
            G.append((R, tf, np.array(img, dtype=np.int64)))

posp = dict((tuple(int(c) for c in s), i) for i, s in enumerate(UNI))
LAB = -np.ones(NPIECE, dtype=np.int64)
REPS = []
for i in range(NPIECE):
    if LAB[i] >= 0:
        continue
    o = len(REPS)
    REPS.append(i)
    for (_, _, g) in G:
        LAB[posp[tuple(sorted(int(g[c]) for c in UNI[i]))]] = o
REPS = np.array(REPS, dtype=np.int64)
NORB = len(REPS)

OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
SC = np.array([SB // 2, SB // 2, SB // 2], dtype=np.int64)
lab, coll = {}, 0
for o, i in enumerate(REPS):
    q = (WT[:, None] * V[UNI[i]]).sum(axis=0)
    for (R, tf, _) in G:
        u = R @ (q[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]), (SB - int(q[3])) if tf else int(q[3]))
        if lab.setdefault(key, o) != o:
            coll += 1
KEYS = sorted(lab)
Q = np.array(KEYS, dtype=np.int64)
NQ = len(Q)
QT = Q.T
face, MASK = 0, []
MI = np.zeros((NPIECE, NQ), dtype=np.int64)
for i in range(NPIECE):
    lam = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lam.sum(axis=0)
    face += int(((lam == 0).any(axis=0) | (tot == SB)).sum())
    ins = (lam > 0).all(axis=0) & (tot < SB)
    MI[i] = ins.astype(np.int64)
    b = 0
    for j in np.flatnonzero(ins):
        b |= 1 << int(j)
    MASK.append(b)
ALLQ = (1 << NQ) - 1


BY, MK = {}, dict((i, MASK[i]) for i in MINP)
for i in MINP:
    for j in np.flatnonzero(MI[i]):
        BY.setdefault(int(j), []).append(i)
SOL, NODE, FULL = [], [0], set()


def rec(cov, chosen):
    NODE[0] += 1
    if cov == ALLQ:
        FULL.add(len(chosen))
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

CM = np.zeros(NPIECE, dtype=np.int64)
for i in range(NPIECE):
    b = 0
    for t in UNI[i]:
        b |= 1 << int(t)
    CM[i] = b

INC = np.zeros((NS, NPO), dtype=np.uint8)
BITS = [0] * NS
for i, s in enumerate(SOL):
    v = 0
    for p in s:
        a = P2I[p]
        INC[i, a] = 1
        v |= 1 << a
    BITS[i] = v
INCL = INC.astype(np.int64)
PMS = []
M2I = dict((int(CM[i]), i) for i in range(NPIECE))
for (_, _, g) in G:
    arr = np.zeros(NPIECE, dtype=np.int32)
    for i in range(NPIECE):
        w = 0
        for c in range(16):
            if (int(CM[i]) >> c) & 1:
                w |= 1 << int(g[c])
        arr[i] = M2I[w]
    PMS.append(arr)
SOLARR = np.array(SOL, dtype=np.int32)
KEYMAP = dict((np.sort(SOLARR[i]).tobytes(), i) for i in range(NS))
PERMS = []
for arr in PMS:
    img = np.sort(arr[SOLARR], axis=1)
    PERMS.append(np.array([KEYMAP[img[i].tobytes()] for i in range(NS)], dtype=np.int64))


# ---- column permutations and column orbits ----
CP = []
CPOK = True
for gi in range(48):
    cp = np.array([P2I[int(PMS[gi][USED[a]])] for a in range(NPO)], dtype=np.int64)
    CPOK = CPOK and len(set(cp.tolist())) == NPO
    CPOK = CPOK and np.array_equal(INC[PERMS[gi]][:, cp], INC)
    CP.append(cp)
lab = -np.ones(NPO, dtype=np.int64)
NORB = 0
for a in range(NPO):
    if lab[a] < 0:
        for cp in CP:
            lab[int(cp[a])] = NORB
        NORB += 1
OSZ = sorted(int((lab == j).sum()) for j in range(NORB))


# ------------------------------------------------- Part 2: the object and its carriers

INT = INCL.astype(np.int32)
GR = (INT.T @ INT).astype(np.int64)
RW = INC.sum(axis=1).astype(np.int64)
CS = INC.sum(axis=0).astype(np.int64)

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
W = np.zeros((NC, NPO), dtype=np.int64)
for i, s in enumerate(CLQ):
    for p in s:
        W[i, int(p)] = 1
COV = INCL @ W.T


# ------------------------------------------ Part 2: the sharing tables of the covers

emit("Every count below is measured here.")
emit("the object: {0} cuttings and {1} pieces, {2} pieces to a cutting, "
     "{3} cuttings through a piece".format(NS, NPO, int(RW.min()), int(CS.min())))
gate(NS == 15800 and NPO == 192 and int(RW.min()) == int(RW.max()) == 24
     and int(CS.min()) == int(CS.max()) == 1975 and int(RW.sum()) == int(CS.sum())
     and len(SUB) == 4368 and NPIECE == 2672 and LO == 6 and NQ == 2736
     and coll == 0 and face == 0 and CB == 3 and SB == 12810
     and FULL == {24} and len(KEYMAP) == NS
     and INV_OK and len(ROT) == 24 and len(G) == 48,
     "C0", "the cell sample is collision- and boundary-free; incidence degrees, "
     "exact inverses, and the declared action match")

emit("the {0} free eight-piece sets meet each of the {1} cuttings "
     "between {2} and {3} times".format(NC, NS, int(COV.min()), int(COV.max())))
gate(NC == 192 and int(COV.min()) == int(COV.max()) == 1, "C1",
     "each of the {0} sets is an exact cover: the table sends it to the all ones "
     "column over all {1} cuttings".format(NC, NS))

M = W
RSUM = M.sum(axis=1)
CSUM = M.sum(axis=0)
emit("the cover by piece table has row sums {0} to {1} and column sums {2} to "
     "{3}".format(int(RSUM.min()), int(RSUM.max()), int(CSUM.min()), int(CSUM.max())))
gate(M.shape == (NC, NPO) and set(int(x) for x in np.unique(M)) == set([0, 1])
     and int(RSUM.min()) == int(RSUM.max()) == 8
     and int(CSUM.min()) == int(CSUM.max()) == 8, "C2",
     "the zero one table is {0} regular on both sides".format(int(RSUM.min())))

S = M @ M.T
N = M.T @ M
OFFD = ~np.eye(NC, dtype=bool)
SVAL = sorted(set(int(x) for x in np.unique(S[OFFD])))
NVAL = sorted(set(int(x) for x in np.unique(N[OFFD])))
SCNT = dict((v, ((S == v) & OFFD).sum(axis=1)) for v in SVAL)
NCNT = dict((v, ((N == v) & OFFD).sum(axis=1)) for v in NVAL)
SPRO = [int(SCNT[v].min()) for v in SVAL]
NPRO = [int(NCNT[v].min()) for v in NVAL]
MISS = [v for v in NVAL if v not in SVAL]
SFIX = all(int(SCNT[v].min()) == int(SCNT[v].max()) for v in SVAL)
NFIX = all(int(NCNT[v].min()) == int(NCNT[v].max()) for v in NVAL)
emit("cover side sharing values {0} with per cover counts {1}, the same for every "
     "one of the {2} covers".format(joins(SVAL), joins(SPRO), NC))
gate(SVAL == [0, 1, 2, 4] and 3 not in SVAL and SFIX and SPRO == [157, 20, 10, 4]
     and sum(SPRO) == NC - 1 and MISS == [3], "C3",
     "the complete distinct-cover profile is {0}, with the same counts in every "
     "row".format(joins(SVAL)))
emit("piece side sharing values {0} with per piece counts {1}, the same for every "
     "one of the {2} pieces".format(joins(NVAL), joins(NPRO), NPO))
gate(NVAL == [0, 1, 2, 3, 4] and NFIX and NPRO == [158, 18, 10, 2, 3]
     and sum(NPRO) == NPO - 1, "C4",
     "the complete distinct-piece profile is {0}, with the same counts in every "
     "row".format(joins(NVAL)))

SMUL = mset(S[OFFD])
NMUL = mset(N[OFFD])
emit("cover side off diagonal multiset " + msets(SMUL))
emit("piece side off diagonal multiset " + msets(NMUL))
gate(SMUL != NMUL, "C5",
     "the cover-side and piece-side off-diagonal multisets are distinct")

SDG = sorted(set(int(x) for x in np.unique(np.diag(S))))
AI = np.eye(NC, dtype=np.int64)
REL = [AI] + [(S == v).astype(np.int64) for v in SVAL]
RNM = ["AI"] + ["A{0}".format(v) for v in SVAL]
RSU = sum(REL)
VAL = [int(X[0].sum()) for X in REL]
emit("the classes " + " ".join(RNM) + " have valencies " + joins(VAL))
gate(all(set(int(x) for x in np.unique(X)) <= set([0, 1]) for X in REL)
     and int(RSU.min()) == int(RSU.max()) == 1
     and all(np.array_equal(X, X.T) for X in REL)
     and len(SDG) == 1 and SDG[0] == 8
     and np.array_equal(REL[0], (S == SDG[0]).astype(np.int64))
     and sum(VAL) == NC, "C6",
     "the {0} zero one classes are symmetric, disjoint, add up to the all ones "
     "matrix, and the share {1} class is the identity".format(len(REL), SDG[0]))


def closure_report(mats):
    """Distinct integer values of every relation product on every relation."""
    n = len(mats)
    msk = [X > 0 for X in mats]
    prods = {}
    vals = {}
    for i in range(n):
        for j in range(n):
            P = mats[i].astype(np.int64) @ mats[j].astype(np.int64)
            prods[(i, j)] = P
            for k in range(n):
                vals[(i, j, k)] = sorted(int(x) for x in np.unique(P[msk[k]]))
    return prods, vals


def spread(vals):
    """the triple of class indices carrying the most values, and how many"""
    worst = None
    for key in sorted(vals):
        if worst is None or len(vals[key]) > len(vals[worst]):
            worst = key
    return worst, len(vals[worst])


PRD, VLS = closure_report(REL)
P00 = PRD[(1, 1)]
V00 = VLS[(1, 1, 1)]
IDX = np.argwhere(REL[1] > 0)
XA, YA = int(IDX[0][0]), int(IDX[0][1])
VA = int(P00[XA, YA])
PICK = None
for r in range(IDX.shape[0]):
    xb, yb = int(IDX[r][0]), int(IDX[r][1])
    if int(P00[xb, yb]) != VA:
        PICK = (xb, yb, int(P00[xb, yb]))
        break
emit("{0} . {0} takes {1} values on the class {0}: {2}".format(
    RNM[1], len(V00), joins(V00)))
emit("pair ({0},{1}) and pair ({2},{3}) both share {4} pieces yet carry {5} and "
     "{6}".format(XA, YA, PICK[0], PICK[1], int(S[XA, YA]), VA, PICK[2]))
gate(len(V00) > 1 and PICK is not None and int(S[XA, YA]) == 0
     and int(S[PICK[0], PICK[1]]) == 0 and VA != PICK[2], "C7",
     "two entries of the zero-sharing relation carry distinct squared-product values")

XY = PRD[(1, 2)]
YX = PRD[(2, 1)]
DIF = np.argwhere(XY != YX)
XC, YC = int(DIF[0][0]), int(DIF[0][1])
emit("{0} . {1} and {1} . {0} differ at entry ({2},{3}): {4} against {5}".format(
    RNM[1], RNM[2], XC, YC, int(XY[XC, YC]), int(YX[XC, YC])))
gate(DIF.shape[0] > 0 and not np.array_equal(XY, YX)
     and int(XY[XC, YC]) != int(YX[XC, YC]), "C8",
     "the two ordered relation products have distinct entries")

HV = np.array([[(k >> b) & 1 for b in range(4)] for k in range(16)], dtype=np.int64)
HD = np.abs(HV[:, None, :] - HV[None, :, :]).sum(axis=2)
HR = [(HD == d).astype(np.int64) for d in range(5)]
HP, HVL = closure_report(HR)
HOK = all(len(v) == 1 for v in HVL.values())
emit("control on the {0} corners of the four cube by differing coordinates: {1} "
     "products, one number D1 . D1 on D0 = {2}".format(
         len(HV), len(HP), HVL[(1, 1, 0)][0]))
gate(HOK and np.array_equal(sum(HR), np.ones((16, 16), dtype=np.int64))
     and len(HVL) == 125, "C9",
     "the same test finds all {0} products of the control constant on all {1} of "
     "its classes".format(len(HP), len(HR)))

QR = [X.copy() for X in HR]
CAN = np.argwhere(HD == 2)
QX, QY = int(CAN[0][0]), int(CAN[0][1])
QR[2][QX, QY] = QR[2][QY, QX] = 0
QR[1][QX, QY] = QR[1][QY, QX] = 1
QP, QVL = closure_report(QR)
QOK = all(len(v) == 1 for v in QVL.values())
QW, QN = spread(QVL)
emit("control with the symmetric pair ({0},{1}) moved from the d 2 class to the d 1 "
     "class: product ({2},{3}) takes {4} values on class {5}".format(
         QX, QY, QW[0], QW[1], QN, QW[2]))
gate((not QOK) and np.array_equal(sum(QR), np.ones((16, 16), dtype=np.int64))
     and all(np.array_equal(X, X.T) for X in QR) and QN > 1, "C10",
     "the moved-pair control remains a symmetric partition and reports multiple "
     "product values")


def refine_once(C):
    """recolour each ordered pair by its old colour together with the multiset of
    the colour pairs it makes with every third index"""
    n = C.shape[0]
    k = int(C.max()) + 1
    code = C[:, :, None].astype(np.int32) * np.int32(k) + C[None, :, :].astype(np.int32)
    code.sort(axis=1)
    sig = np.ascontiguousarray(code.transpose(0, 2, 1)).reshape(n * n, n)
    key = np.concatenate(
        [C.reshape(n * n, 1).astype(np.int32), sig], axis=1)
    raw = np.ascontiguousarray(key).tobytes()
    wid = key.shape[1] * 4
    seen = {}
    out = np.zeros(n * n, dtype=np.int64)
    for t in range(n * n):
        h = raw[t * wid:(t + 1) * wid]
        u = seen.get(h)
        if u is None:
            u = len(seen)
            seen[h] = u
        out[t] = u
    return out.reshape(n, n), len(seen)


COL = np.zeros((NC, NC), dtype=np.int64)
for t, v in enumerate([SDG[0]] + SVAL):
    COL[S == v] = t
ROUND = [int(COL.max()) + 1]
while True:
    NEW, KN = refine_once(COL)
    ROUND.append(KN)
    if KN == ROUND[-2]:
        break
    COL = NEW
KF = ROUND[-1]
CSZ = mset([int((COL == c).sum()) for c in range(KF)])
SPL = [len(set(int(x) for x in np.unique(COL[REL[t] > 0]))) for t in range(len(REL))]
emit("declared pair-colour refinement, classes by round: " + joins(ROUND))
emit("final classes {0} with sizes {1}; the five relations split as {2}".format(
    KF, msets(CSZ), joins(SPL)))
gate(KF == 120 and CSZ == {192: 48, 384: 72} and SPL == [1, 100, 10, 6, 3]
     and sum(k * v for k, v in CSZ.items()) == NC * NC, "C11",
     "the declared refinement stabilizes at 120 classes with the gated split profile")

CKEY = dict((frozenset(int(p) for p in CLQ[i]), i) for i in range(NC))
CARP = []
for cp in CP:
    img = []
    for i in range(NC):
        j = CKEY.get(frozenset(int(cp[p]) for p in CLQ[i]))
        if j is None:
            break
        img.append(j)
    if len(img) == NC and len(set(img)) == NC:
        CARP.append(img)
SEEN = [-1] * NC
OSIZ = []
for i in range(NC):
    if SEEN[i] < 0:
        SEEN[i] = len(OSIZ)
        front, cnt = [i], 0
        while front:
            x = front.pop()
            cnt += 1
            for pp in CARP:
                y = pp[x]
                if SEEN[y] < 0:
                    SEEN[y] = SEEN[i]
                    front.append(y)
        OSIZ.append(cnt)
emit("all {0} declared spatial-rotation/time-flip maps send covers to covers; orbits: "
     "{1} of sizes {2}".format(len(CARP), len(OSIZ), joins(sorted(OSIZ))))
gate(CPOK and len(CP) == 48 and len(CARP) == 48 and len(OSIZ) == 5
     and sorted(OSIZ) == [24, 24, 48, 48, 48] and sum(OSIZ) == NC, "C12",
     "every one of the {0} action elements permutes the {1} covers, producing {2} "
     "orbits of covers".format(len(CARP), NC, len(OSIZ)))


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


ORK = []
for j in range(len(OSIZ)):
    mem = [i for i in range(NC) if SEEN[i] == j]
    ORK.append(rank_exact([[int(x) for x in (W[i] - W[mem[0]])] for i in mem[1:]]))
ARK = rank_exact([[int(x) for x in (W[i] - W[0])] for i in range(1, NC)])
OPR = " ".join("{0}:{1}".format(OSIZ[j], ORK[j]) for j in range(len(OSIZ)))
emit("cover differences inside each orbit, orbit size then exact rank: {0}; all {1} "
     "covers together: {2}".format(OPR, NC, ARK))
gate(ARK == 104 and all(r < ARK for r in ORK)
     and all(ORK[j] <= OSIZ[j] - 1 for j in range(len(OSIZ)))
     and any(ORK[j] < OSIZ[j] - 1 for j in range(len(OSIZ)))
     and len(ORK) == len(OSIZ), "C13",
     "the {0}-cover difference rank is {1}; each action-orbit rank is smaller"
     .format(NC, ARK))

ELAP = time.monotonic() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
EBD = 30 * (int(ELAP // 30) + 1)
RBD = 500 * (int(RSS // 500) + 1)
emit("elapsed under {0} s and peak memory under {1} MB, both measured in this "
     "run".format(EBD, RBD))
gate(ELAP < AUDIT_TIMEOUT_SEC and RSS < 2500.0
     and EBD <= AUDIT_TIMEOUT_SEC and RBD <= 2500, "C14",
     "inside its time and memory allowance")

emit("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
raise SystemExit(1 if PF[1] else 0)
