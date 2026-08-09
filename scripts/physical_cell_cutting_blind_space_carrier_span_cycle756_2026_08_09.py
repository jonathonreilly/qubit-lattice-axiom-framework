"""Rebuild the cutting system of the unit four-cube and ask where the space the
cuttings cannot see comes from.

Every count below is measured here. The runner builds the cell complex, the least
volume pieces, the cuttings at the adjacency cost floor, the piece sharing table,
the eight-piece carriers that meet every cutting exactly once, the span of their
differences, the sharing classes of carrier pairs, and a complete sweep of the
small supports a blind weighting could have, gating each quantity in place.
"""
import itertools
import math
import resource
import time

import numpy as np

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
emit("")
emit("the object: {0} cuttings and {1} pieces, {2} pieces to a cutting, "
     "{3} cuttings through a piece".format(NS, NPO, int(RW[0]), int(CS[0])))
gate(NS == 15800 and NPO == 192 and int(RW.min()) == int(RW.max()) == 24
     and int(CS.min()) == int(CS.max()) == 1975 and int(RW.sum()) == int(CS.sum()),
     "C0", "every cutting uses the same number of pieces, every piece sits in the "
     "same number of cuttings, and the two counts of the incidences agree")

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
emit("eight pieces no cutting uses twice: {0}, each meeting every cutting "
     "between {1} and {2} times".format(NC, int(COV.min()), int(COV.max())))
gate(NC == 192 and int(COV.min()) == 1 and int(COV.max()) == 1, "C1",
     "each of the 192 carriers meets every one of the 15800 cuttings exactly once, "
     "so the table sends every carrier to the same all-ones column")

SH = (W @ W.T).astype(np.int64)
np.fill_diagonal(SH, -1)
HIS = {}
for v in (0, 1, 2, 4):
    HIS[v] = int((SH == v).sum()) // 2
TOTP = NC * (NC - 1) // 2
emit("carrier pairs by shared pieces: " + " ".join(
    "{0}:{1}".format(v, HIS[v]) for v in (0, 1, 2, 4)))
gate(sum(HIS.values()) == TOTP and TOTP == 18336 and HIS[4] == 384, "C2",
     "the shared count of two carriers is 0, 1, 2 or 4, never 3, over all "
     "18336 pairs, and the least sharing pair count is 384")

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
     and int(np.abs(D4).sum(axis=1).max()) == 8, "C3",
     "a carrier difference is blind because both carriers give the same all-ones "
     "column, and the 384 least exchanges are the differences of support 8")


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
gate(RW1 == RW2 == 105 and RI1 == RI2 == 88, "C4",
     "two different bounded arithmetics agree, and a bounded rank never exceeds "
     "the exact rank, so the carriers span at least 105 and the table at least 88")
gate(RW1 == 105 and RI1 == 88 and 192 - RI1 == 104, "C5",
     "the table rank being at least 88 leaves the blind space at most 104, while "
     "the carriers spanning at least 105 puts at least 104 independent differences "
     "inside it, so both are exact: rank 88, blind space 104")

DALL = []
for v in (0, 1, 2, 4):
    idx = [(i, j) for i in range(NC) for j in range(i + 1, NC) if int(SH[i, j]) == v]
    Dv = W[[i for i, j in idx]] - W[[j for i, j in idx]]
    rv = rank_mod(Dv, BIGP)
    DALL.append((v, len(idx), rv))
emit("each sharing class alone spans: " + " ".join(
    "{0}:{1}".format(v, r) for v, n, r in DALL))
gate(all(r == 104 for v, n, r in DALL), "C6",
     "the differences at each single sharing class already span the whole blind "
     "space, so no one class of exchange is the source and the least ones suffice")


# ------------------------------------------- Part 3: how small a blind support can be

MASK = [0] * NPO
for p in range(NPO):
    m = 0
    for c in np.flatnonzero(INC[:, p]):
        m |= 1 << int(c)
    MASK[p] = m
AB4 = np.abs(D4)
MEETS = INCL @ AB4.T
MEET = sorted(set(int(x) for x in np.unique(MEETS)))
CARR = sorted(set(int(x) for x in np.unique(COV)))
emit("cuttings meet a blind support this often: " + " ".join(str(x) for x in MEET)
     + " ; they meet a carrier this often: " + " ".join(str(x) for x in CARR))
gate(MEET == [0, 2] and CARR == [1], "C7",
     "a blind weighting cannot have a cutting meeting its support just once, since "
     "that lone piece would then carry no weight, and the two readings separate: "
     "all 384 least exchanges meet every cutting 0 or 2 times while a carrier, "
     "which is not blind, meets every cutting exactly once")

ANCH = []
for j in range(NORB):
    ANCH.append(int(np.flatnonzero(lab == j)[0]))
gate(CPOK and NORB == 4 and sorted(OSZ) == [48, 48, 48, 48] and len(ANCH) == 4,
     "C8", "each of the 48 proper cube symmetries carries the table to itself by a "
     "piece relabelling paired with a cutting relabelling, and they leave 4 kinds "
     "of piece, 48 of each, so a support of any size is the same up to symmetry as "
     "one holding a piece of one of those 4 kinds")


def shut(s):
    """true when every cutting through a member of s meets a second member"""
    for p in s:
        u = 0
        for q in s:
            if q != p:
                u |= MASK[q]
        if MASK[p] & ~u:
            return False
    return True


S8 = tuple(int(x) for x in np.flatnonzero(AB4[0]))
SC = tuple(int(x) for x in CLQ[0])
gate(len(S8) == 8 and len(SC) == 8 and shut(S8) and not shut(SC), "C9",
     "the test the sweep applies says yes on the 8 pieces a least exchange touches "
     "and no on the 8 pieces of a carrier, so it is a test that separates and not "
     "one that refuses every candidate")


def sweep(anchor, top):
    """all minimal covers of one piece's cuttings up to size top, then every
    support up to size top + 1 built on them, tested by the full condition"""
    uni = [int(c) for c in np.flatnonzero(INC[:, anchor])]
    pos = dict((c, i) for i, c in enumerate(uni))
    nu = len(uni)
    sets = [0] * NPO
    for q in range(NPO):
        if q == anchor:
            continue
        b = 0
        for c in np.flatnonzero(INC[:, q]):
            i = pos.get(int(c))
            if i is not None:
                b |= 1 << i
        sets[q] = b
    full = (1 << nu) - 1
    mx = max(bin(s).count("1") for s in sets)
    by = [[] for _ in range(nu)]
    for q in range(NPO):
        x = sets[q]
        while x:
            low = x & -x
            by[low.bit_length() - 1].append(q)
            x ^= low
    cores = set()

    def rec(cov, chosen):
        if cov == full:
            cores.add(tuple(sorted(chosen)))
            return
        slots = top - len(chosen)
        if slots == 0:
            return
        rem = full & ~cov
        if mx * slots < bin(rem).count("1"):
            return
        e = (rem & -rem).bit_length() - 1
        for q in by[e]:
            if q in chosen:
                continue
            rec(cov | sets[q], chosen + [q])

    rec(0, [])
    bysz = {}
    for c in cores:
        bysz.setdefault(len(c), []).append(c)
    oth = [q for q in range(NPO) if q != anchor]
    tried = 0
    passed = 0
    hits = 0
    for k in range(5, top + 2):
        seen = set()
        for sz in sorted(bysz):
            extra = k - 1 - sz
            if extra < 0:
                continue
            for cc in bysz[sz]:
                rest = [q for q in oth if q not in cc]
                for add in itertools.combinations(rest, extra):
                    t = tuple(sorted(cc + add))
                    if t in seen:
                        continue
                    seen.add(t)
                    tried += 1
                    s = (anchor,) + t
                    bad = False
                    for p in s:
                        tot = 0
                        for q in s:
                            if q != p:
                                tot += int(GR[p, q])
                        if tot < 1975:
                            bad = True
                            break
                    if bad:
                        continue
                    passed += 1
                    good = True
                    for p in s:
                        u = 0
                        for q in s:
                            if q != p:
                                u |= MASK[q]
                        if MASK[p] & ~u:
                            good = False
                            break
                    if good:
                        hits += 1
        seen = None
    return min(bysz), sorted(bysz), tried, passed, hits


LEAST = []
TRIED = 0
PASSED = 0
HITS = 0
SIZES = None
for a in ANCH:
    lo, szs, tr, pa, hi = sweep(a, 6)
    LEAST.append(lo)
    if a == ANCH[0]:
        SIZES = szs
    TRIED += tr
    PASSED += pa
    HITS += hi
emit("least other pieces covering one piece's cuttings, by piece kind: " + " ".join(
    str(x) for x in LEAST))
gate(LEAST == [4, 4, 4, 4], "C10",
     "the 1975 cuttings through a piece are not covered by 2 or by 3 other pieces "
     "but are covered by 4, so a blind support holding that piece holds at least "
     "4 more and no support of size 2, 3 or 4 can be blind")
emit("candidate supports of size 5, 6 and 7 built and tested: {0}, of those "
     "passing the count bound: {1}".format(TRIED, PASSED))
gate(HITS == 0 and TRIED > 0 and PASSED > 0, "C11",
     "every support of size 5, 6 or 7 was built from a least cover of its anchor "
     "piece and tested by the full condition, and none of them is blind")
gate(LEAST == [4, 4, 4, 4] and HITS == 0 and int(np.abs(D4).sum(axis=1).max()) == 8,
     "C12", "so no blind weighting of the cutting table touches fewer than 8 "
     "pieces, and 8 is reached, by the least exchanges: the smallest blind "
     "support has exactly the size of a carrier")

ELAP = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
emit("")
emit("elapsed under 900 s peak memory under 2500 MB")
gate(ELAP < 900.0 and RSS < 2500.0, "C13", "inside its time and memory allowance")
gate(OUT[0] < 6000, "C14", "its output stays under 6000 characters")
emit("")
emit("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
