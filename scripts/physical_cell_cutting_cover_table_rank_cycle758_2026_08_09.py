"""Measure the exact rank of the cover by piece table of the cut unit four-cube and
the whole number part of the spectrum of its two sharing tables.

Every count below is measured here. The runner rebuilds the cell complex, the least
volume pieces, the cuttings at the adjacency cost floor, the incidence table, the
eight-piece sets that meet every cutting exactly once, and the cover by piece table.
It then shows the all ones piece vector lying in the row space of that table and
carried by the cutting table to a nonzero constant, hence outside the space the
cuttings cannot see; the table having rank one above its cover differences; and both
sharing tables carrying the one exact whole number spectrum. Two controls, one fixed
in advance and one perturbed, show the spectrum scan reads what is there.
"""
import itertools
import math
import resource
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ()

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

ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if int(round(np.linalg.det(R.astype(float)))) == 1:
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
     and int(CS.min()) == int(CS.max()) == 1975 and int(RW.sum()) == int(CS.sum()),
     "C0", "the pieces per cutting and the cuttings through a piece are each the "
     "same number for every one of them")

emit("the {0} eight piece sets no cutting uses twice meet each of the {1} cuttings "
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


# --------------------------------------- Part 3: rank, kernel and the whole spectrum

PMOD = 1000003


def rank_mod(rows, p):
    """rank of an integer matrix over the field with p elements

    Ordinary elimination with every value reduced by p through divmod, and the
    pivot turned around by raising it to the power p minus two.
    """
    wk = [[divmod(int(x), p)[1] for x in r] for r in rows]
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
        inv = pow(wk[rk][col], p - 2, p)
        pr = [divmod(x * inv, p)[1] for x in wk[rk]]
        wk[rk] = pr
        for r in range(rk + 1, nr):
            f = wk[r][col]
            if f:
                rw = wk[r]
                wk[r] = rw[:col] + [divmod(rw[c] - f * pr[c], p)[1]
                                    for c in range(col, m)]
        rk += 1
    return rk


def whole_spectrum(A, lo, hi):
    """the whole numbers in lo..hi that are eigenvalues of A, exact multiplicities

    The rank over the prime field is never above the rank over the rationals, so a
    zero nullity over the prime field rules the number out with no further work.
    Every survivor of that cheap pass is then confirmed by the exact routine, and
    only the exact nullity is reported.
    """
    n = A.shape[0]
    idm = np.eye(n, dtype=np.int64)
    out = []
    for lam in range(lo, hi + 1):
        rows = [[int(x) for x in r] for r in (A - lam * idm)]
        if n - rank_mod(rows, PMOD) > 0:
            e = n - rank_exact(rows)
            if e > 0:
                out.append((lam, e))
    return out


def pshow(ps):
    """value:multiplicity string of a list of value and multiplicity pairs"""
    return " ".join("{0}:{1}".format(a, b) for a, b in ps)


ONES = np.ones(NPO, dtype=np.int64)
emit("adding up all {0} rows of the cover by piece table gives {1} at every one of "
     "the {2} pieces".format(NC, int(CSUM.min()), M.shape[1]))
gate(int(CSUM.min()) == int(CSUM.max()) == 8 and M.shape[1] == 192
     and len(CSUM) == 192, "C3",
     "the all ones piece vector is the sum of all the cover rows, so it sits in the "
     "row space of the cover by piece table")

IMG = INCL @ ONES
IVAL = sorted(set(int(x) for x in np.unique(IMG)))
emit("the cutting table sends the all ones piece vector to the single value {0} at "
     "every one of the {1} cuttings".format(joins(IVAL), len(IMG)))
gate(IVAL == [24] and len(IMG) == NS and NS == 15800, "C4",
     "the image is one value and that value is not zero, so the all ones piece "
     "vector is not blind to the cuttings")

RKM = rank_exact([[int(x) for x in r] for r in M])
RKD = rank_exact([[int(x) for x in (M[i] - M[0])] for i in range(1, NC)])
emit("exact rank of the cover by piece table {0}, exact rank of its {1} cover "
     "differences {2}, difference {3}".format(RKM, NC - 1, RKD, RKM - RKD))
gate(RKM == 105 and RKD == 104 and RKM - RKD == 1, "C5",
     "the cover differences drop exactly one dimension against the covers "
     "themselves, and that dimension is the all ones direction")

MT = M.T
STK = np.vstack([MT, np.ones((1, NC), dtype=np.int64)])
RKS = rank_exact([[int(x) for x in r] for r in STK])
RKT = rank_exact([[int(x) for x in r] for r in MT])
emit("stacking the {0} rows of the transposed table with one all ones cover row "
     "gives rank {1}, against rank {2} without it".format(NPO, RKS, RKT))
gate(RKS == RKT and RKS == 105 and RKT == 105 and STK.shape == (NPO + 1, NC), "C6",
     "the all ones cover row raises nothing, so it sits in the row space and every "
     "kernel vector of that table sums to zero over the covers")

NUL = NC - RKT
emit("exact nullity of the transposed table {0}, and {1} minus that nullity is "
     "{2}".format(NUL, NC - 1, NC - 1 - NUL))
gate(NUL == 87 and NC - 1 - NUL == 104, "C7",
     "the kernel takes {0} of the {1} cover directions away and the {2} cover "
     "differences fill the {3} that is left".format(NUL, NC, NC - 1, NC - 1 - NUL))

RKSS = rank_exact([[int(x) for x in r] for r in S])
RKNN = rank_exact([[int(x) for x in r] for r in N])
emit("exact rank of the cover side sharing table {0} and of the piece side sharing "
     "table {1}".format(RKSS, RKNN))
gate(RKSS == 105 and RKNN == 105 and RKSS == RKM and RKNN == RKM, "C8",
     "a table and the two products of it with its transpose all carry the one rank")

SHI = int(S.sum(axis=1).max())
SPEC = whole_spectrum(S, 0, SHI)
SWT = sum(m for _, m in SPEC)
emit("the cover side table is an integer table times its transpose so no eigenvalue "
     "is below 0, and its largest row sum {0} puts none above {0}".format(SHI))
emit("a rational eigenvalue of an integer symmetric table is an algebraic integer, "
     "hence a whole number, so only the whole numbers 0 to {0} can occur".format(SHI))
emit("rank over the prime field {0} is never above rank over the rationals, so zero "
     "nullity there proves zero nullity over the rationals".format(PMOD))
emit("cover side whole number spectrum " + pshow(SPEC))
emit("counted with multiplicity {0} of the {1} eigenvalues are whole numbers and {2} "
     "are not rational".format(SWT, NC, NC - SWT))
gate(SPEC == [(0, 87), (2, 8), (4, 8), (8, 3), (10, 8), (12, 6), (16, 2), (20, 10),
              (24, 3), (64, 1)] and SWT == 136 and NC - SWT == 56 and SHI == 64,
     "C9", "the rational part of the cover side sharing spectrum is exactly these "
     "ten whole numbers with these exact multiplicities")

NHI = int(N.sum(axis=1).max())
NSPEC = whole_spectrum(N, 0, NHI)
NWT = sum(m for _, m in NSPEC)
emit("piece side whole number spectrum " + pshow(NSPEC))
gate(NSPEC == SPEC and NWT == SWT and NHI == SHI, "C10",
     "the two products of one table with its transpose carry the one nonzero "
     "spectrum, and the table is square so the count at 0 agrees")

TRS = sum(int(S[i, i]) for i in range(NC))
TRS2 = sum(int(x) * int(x) for r in S for x in r)
WH1 = sum(v * m for v, m in SPEC)
WH2 = sum(v * v * m for v, m in SPEC)
emit("trace {0} splits as {1} from the whole numbers plus {2}, trace of the square "
     "{3} splits as {4} plus {5}".format(TRS, WH1, TRS - WH1, TRS2, WH2, TRS2 - WH2))
gate(TRS == 1536 and WH1 == 592 and TRS - WH1 == 944 and TRS2 == 36096
     and WH2 == 12352 and TRS2 - WH2 == 23744 and TRS - WH1 > 0 and TRS2 - WH2 > 0,
     "C11", "the whole numbers make neither total on their own, and both leftovers "
     "are positive, as eigenvalues that are not rational require")

HV = np.array([[(k >> b) & 1 for b in range(4)] for k in range(16)], dtype=np.int64)
HD = np.abs(HV[:, None, :] - HV[None, :, :]).sum(axis=2)
CTRL = (HD == 1).astype(np.int64)
CHI = int(CTRL.sum(axis=1).max())
CSPEC = whole_spectrum(CTRL, -CHI, CHI)
CTOT = sum(m for _, m in CSPEC)
CTOP = list(reversed(CSPEC))
emit("control on the {0} corners of the four cube, adjacent when they differ in one "
     "coordinate: {1}".format(len(HV), pshow(CTOP)))
gate(CTOP == [(4, 1), (2, 4), (0, 6), (-2, 4), (-4, 1)] and CTOT == 16 and CHI == 4,
     "C12", "the scan recovers the {0} eigenvalues that were fixed for this control "
     "before any measurement, so it reads the right answer".format(CTOT))

PERT = CTRL.copy()
PERT[0, 3] = PERT[0, 3] + 1
PERT[3, 0] = PERT[3, 0] + 1
PHI = int(PERT.sum(axis=1).max())
PSPEC = whole_spectrum(PERT, -PHI, PHI)
PTOT = sum(m for _, m in PSPEC)
emit("the same control with 1 added at the symmetric pair (0,3): {0}, whole number "
     "eigenvalues with multiplicity {1}".format(pshow(list(reversed(PSPEC))), PTOT))
gate(PSPEC != CSPEC and PTOT < CTOT and PTOT < 16
     and set(int(x) for x in np.unique(PERT)) == set([0, 1])
     and np.array_equal(PERT, PERT.T), "C13",
     "one added symmetric pair changes the whole number spectrum and drops the "
     "count, so the scan is not returning a canned answer")

ELAP = time.monotonic() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
EBD = 300 * (int(ELAP // 300) + 1)
RBD = 500 * (int(RSS // 500) + 1)
emit("elapsed under {0} s and peak memory under {1} MB, both measured in this "
     "run".format(EBD, RBD))
gate(ELAP < 900.0 and RSS < 2500.0 and EBD <= 900 and RBD <= 2500, "C14",
     "inside its time and memory allowance")

emit("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
if PF[1]:
    raise SystemExit(1)
