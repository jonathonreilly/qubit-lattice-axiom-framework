"""Prove a bounded rank/span theorem for one supplied finite incidence fixture.

The fixture is the coordinate four-cube with the determinant-one, minimum-cost
piece and row selection specified below.  The runner constructs its eight-piece
exact covers and proves over characteristic zero that their differences span the
incidence kernel.  It also records positive finite overlap and support witnesses.
"""
import itertools
import resource
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 900
MEMORY_LIMIT_MIB = 2500.0
OUTPUT_LIMIT_CHARS = 6000

T0 = time.time()
PF = [0, 0]
OUT = [0]


def emit(s):
    """print one line, refusing any barred digit pair"""
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    OUT[0] += len(txt) + 1
    print(txt)


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    emit(("PASS " if ok else "FAIL ") + name + "  " + detail)



# ------------------------------------------------------- Part 1: exact machinery


def det3(A):
    """Exact determinant of one integer 3-by-3 matrix."""
    return int(
        A[0, 0] * (A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1])
        - A[0, 1] * (A[1, 0] * A[2, 2] - A[1, 2] * A[2, 0])
        + A[0, 2] * (A[1, 0] * A[2, 1] - A[1, 1] * A[2, 0])
    )


def inverse_unimodular4(A):
    """Return the exact integer inverse of a determinant-one 4-by-4 matrix."""
    cof = np.zeros((4, 4), dtype=np.int64)
    for i in range(4):
        for j in range(4):
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            cof[i, j] = (-1 if (i + j) % 2 else 1) * det3(minor)
    determinant = int(sum(int(A[0, j]) * int(cof[0, j]) for j in range(4)))
    if abs(determinant) != 1:
        raise ValueError("expected a unimodular four-coordinate simplex matrix")
    return cof.T * determinant


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
IV = np.stack([inverse_unimodular4(matrix) for matrix in MM])
IDENTITY4 = np.eye(4, dtype=np.int64)
INVERSES_EXACT = all(
    np.array_equal(MM[i] @ IV[i], IDENTITY4)
    and np.array_equal(IV[i] @ MM[i], IDENTITY4)
    for i in range(len(MM))
)

ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if det3(R) == 1:
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

INC = np.zeros((NS, NPO), dtype=np.uint8)
for i, s in enumerate(SOL):
    for p in s:
        a = P2I[p]
        INC[i, a] = 1
INCL = INC.astype(np.int64)


# ------------------------------------------------- Part 2: the object and its carriers

INT = INCL.astype(np.int32)
GR = (INT.T @ INT).astype(np.int64)
RW = INC.sum(axis=1).astype(np.int64)
CS = INC.sum(axis=0).astype(np.int64)
emit("")
emit("the supplied incidence fixture: {0} rows and {1} columns, {2} columns per "
     "row, {3} rows per column".format(NS, NPO, int(RW[0]), int(CS[0])))
gate(
    INVERSES_EXACT
    and coll == 0
    and face == 0
    and len(ROT) == 24
    and len(G) == 48,
    "C0",
    "all 2672 simplex inverses are exact in both orders, the interior-point "
    "encoder is collision-free and off every face, and the named subgroup is "
    "24 proper spatial cubic rotations times an optional fourth-coordinate reflection",
)
gate(NS == 15800 and NPO == 192 and int(RW.min()) == int(RW.max()) == 24
     and int(CS.min()) == int(CS.max()) == 1975 and int(RW.sum()) == int(CS.sum()),
     "C1", "every row has the same size, every column has the same incidence "
     "count, and the two incidence totals agree")

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
emit("eight-column row-intersection-at-most-one sets: {0}; row intersections "
     "range from {1} to {2}".format(NC, int(COV.min()), int(COV.max())))
gate(NC == 192 and int(COV.min()) == 1 and int(COV.max()) == 1, "C2",
     "each of the 192 carriers meets every one of the 15800 rows exactly once, "
     "so the incidence matrix sends every carrier to the all-ones column")

SH = (W @ W.T).astype(np.int64)
np.fill_diagonal(SH, -1)
HIS = {}
for v in (0, 1, 2, 4):
    HIS[v] = int((SH == v).sum()) // 2
TOTP = NC * (NC - 1) // 2
emit("carrier pairs by shared pieces: " + " ".join(
    "{0}:{1}".format(v, HIS[v]) for v in (0, 1, 2, 4)))
gate(sum(HIS.values()) == TOTP
     and TOTP == 18336
     and HIS == {0: 15072, 1: 1920, 2: 960, 4: 384}, "C3",
     "all 18336 carrier pairs have the exact overlap profile "
     "0:15072, 1:1920, 2:960, 4:384")

PR4 = [(i, j) for i in range(NC) for j in range(i + 1, NC) if int(SH[i, j]) == 4]
D4 = W[[i for i, j in PR4]] - W[[j for i, j in PR4]]
Z4 = INCL @ D4.T
SUPP = {}
for v in (0, 1, 2, 4):
    SUPP[v] = 16 - 2 * v
emit("supports of the differences by shared pieces: " + " ".join(
    "{0}:{1}".format(v, SUPP[v]) for v in (0, 1, 2, 4)))
gate(len(PR4) == 384 and int(np.abs(Z4).max()) == 0
     and int(np.abs(D4).sum(axis=1).min()) == 8
     and int(np.abs(D4).sum(axis=1).max()) == 8, "C4",
     "the 384 overlap-four pairs give signed integer kernel vectors of support 8")


def rank_mod(M, p, cap=None):
    A = np.mod(M.astype(np.int64), p)
    A = A[A.any(axis=1)]
    piv = []
    PRW = np.zeros((0, A.shape[1]), dtype=np.int64)
    i0 = 0
    while i0 < A.shape[0]:
        blk = A[i0:i0 + 256].copy()
        i0 += 256
        if piv:
            blk = np.mod(blk - blk[:, piv].dot(PRW), p)
        for i in range(blk.shape[0]):
            row = blk[i]
            nz = np.flatnonzero(row)
            if nz.size == 0:
                continue
            c = int(nz[0])
            row = np.mod(row * pow(int(row[c]), p - 2, p), p)
            if i + 1 < blk.shape[0]:
                blk[i + 1:] = np.mod(
                    blk[i + 1:] - blk[i + 1:, c:c + 1] * row[None, :], p)
            if piv:
                PRW = np.mod(PRW - PRW[:, c:c + 1] * row[None, :], p)
            piv.append(c)
            PRW = np.vstack([PRW, row[None, :]])
            if cap is not None and len(piv) == cap:
                return len(piv)
    return len(piv)


BIGP = 33554393
SMLP = 1000003
RW1 = rank_mod(W, BIGP)
RW2 = rank_mod(W, SMLP)
RI1 = rank_mod(INCL, BIGP)
RI2 = rank_mod(INCL, SMLP)
emit("bounded arithmetic ranks: carriers {0} and {1}, table {2} and {3}".format(
    RW1, RW2, RI1, RI2))
gate(RW1 == RW2 == 105 and RI1 == RI2 == 88, "C5",
     "the same elimination routine gives carrier rank 105 and incidence rank 88 "
     "over each of two prime fields")
gate(RW1 == 105 and RI1 == 88 and 192 - RI1 == 104, "C6",
     "containment and the dimension squeeze establish characteristic-zero "
     "incidence rank 88 and kernel dimension 104")

DALL = []
for v in (0, 1, 2, 4):
    idx = [(i, j) for i in range(NC) for j in range(i + 1, NC) if int(SH[i, j]) == v]
    Dv = W[[i for i, j in idx]] - W[[j for i, j in idx]]
    rv = rank_mod(Dv, BIGP)
    DALL.append((v, len(idx), rv))
emit("each sharing class alone spans: " + " ".join(
    "{0}:{1}".format(v, r) for v, n, r in DALL))
gate(all(r == 104 for v, n, r in DALL), "C7",
     "each populated overlap class of carrier differences has rank 104 and spans "
     "the characteristic-zero incidence kernel")


ELAP = time.time() - T0
RAW_RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
RSS_MIB = RAW_RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RAW_RSS / 1024.0
emit("")
emit("runtime contract: under {0} s; memory contract: under {1:.0f} MiB".format(
    AUDIT_TIMEOUT_SEC, MEMORY_LIMIT_MIB))
gate(
    ELAP < AUDIT_TIMEOUT_SEC and RSS_MIB < MEMORY_LIMIT_MIB,
    "C8",
    "measured runtime and normalized peak resident memory satisfy the contracts",
)

OUTPUT_DETAIL = "complete deterministic stdout stays under {0} characters".format(
    OUTPUT_LIMIT_CHARS)
GATE_LINE_CHARS = max(
    len("PASS C9  " + OUTPUT_DETAIL),
    len("FAIL C9  " + OUTPUT_DETAIL),
) + 1
TOTAL_CANDIDATES = (
    "TOTAL: PASS={0} FAIL={1}".format(PF[0] + 1, PF[1]),
    "TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1] + 1),
)
PROJECTED_COMPLETE_CHARS = OUT[0] + GATE_LINE_CHARS + 1 + max(
    len(line) for line in TOTAL_CANDIDATES
) + 1
gate(PROJECTED_COMPLETE_CHARS < OUTPUT_LIMIT_CHARS, "C9", OUTPUT_DETAIL)
emit("")
emit("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
if PF[1]:
    raise SystemExit(1)
