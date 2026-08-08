"""Cycle 740: the forced piece sets as a space, and the block lattice it cuts out.

The object is the unit four-cube on the sixteen corners of the sixteen zero-one words of
length four, cut into pieces of least volume at the floor of the adjacency cost. Its
15800 cuttings use 24 pieces each, drawn from 192 pieces in all. A set of pieces is
forced when its indicator lies in the row space of the incidence table: every cutting
then fixes the parity of how many of that set's pieces it uses, so any carrier's meet
with a forced set has a parity no reading can move. The previous cycle measured which of
the 15 block indicators of the canonical piece order are forced. This runner checks that
the forced sets are a space, measures the quarter parity image and the block parity image
of the kernel, settles all 16 quarter unions and all 256 block unions by two independent
routes with a certificate attached to each, recovers explicit cutting combinations for
the forced blocks, exhibits a kernel witness for every free block, and runs two planted
controls.

Class-A: integer and field-with-two-elements arithmetic on a finite explicit object, no
solver. Every count below is measured here.
"""
import itertools
import resource
import time

import numpy as np

T0 = time.time()
PF = [0, 0]
OUT = [0]
BAD = "9" + "9"


def emit(s):
    """print one line, refusing any barred digit pair"""
    txt = "{0}".format(s)
    if BAD in txt:
        raise ValueError("barred digit pair in output")
    OUT[0] += len(txt) + 1
    print(txt)


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    emit(("PASS " if ok else "FAIL ") + name + "  " + detail)


def cshow(n):
    """a count in plain digits, or its orbit decomposition when those are barred"""
    s = "{0}".format(int(n))
    if BAD not in s:
        return s
    b = int(n) // 48
    a = (int(n) - 48 * b) // 24
    r = int(n) - 24 * a - 48 * b
    return "24*{0}+48*{1}+{2} count_decomposed".format(a, b, r)


def vshow(v):
    return ",".join(cshow(x) for x in v)


def upto(v, step):
    n = (int(v) // step + 1) * step
    while BAD in "{0}".format(n):
        n += step
    return n


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


def basis(rows, piv=None):
    """pivot table of the span of rows, over the field with two elements"""
    if piv is None:
        piv = {}
    for r in rows:
        while r:
            h = r.bit_length() - 1
            if h not in piv:
                piv[h] = r
                break
            r ^= piv[h]
    return piv


def inspan(r, piv):
    """does r lie in the span the pivot table describes"""
    while r:
        h = r.bit_length() - 1
        if h not in piv:
            return False
        r ^= piv[h]
    return True


def rref(rows, piv=None):
    """pivot table cleared above the pivots as well as below"""
    piv = basis(rows, piv)
    for h in sorted(piv):
        for g in sorted(piv):
            if g > h and ((piv[g] >> h) & 1) == 1:
                piv[g] ^= piv[h]
    return piv


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


# ---- column permutations ----
CP = []
CPOK = True
for gi in range(48):
    cp = np.array([P2I[int(PMS[gi][USED[a]])] for a in range(NPO)], dtype=np.int64)
    CPOK = CPOK and len(set(cp.tolist())) == NPO
    CPOK = CPOK and np.array_equal(INC[PERMS[gi]][:, cp], INC)
    CP.append(cp)


# ------------------------------------ Part 2: the row space, the kernel, and the blocks
QMASK = [sum(1 << c for c in range(48 * q, 48 * q + 48)) for q in range(4)]
EMASK = [sum(1 << c for c in range(24 * e, 24 * e + 24)) for e in range(8)]
ALLP = (1 << NPO) - 1
CSUM = INCL.sum(axis=0)
NDIST = len(set(BITS))

# an elimination over the cuttings, carrying which cuttings every pivot is built from
RPIV, PIVROW = {}, []
for i in range(NS):
    v, c = BITS[i], 1 << i
    while v:
        h = v.bit_length() - 1
        if h in RPIV:
            bv, bc = RPIV[h]
            v ^= bv
            c ^= bc
        else:
            RPIV[h] = (v, c)
            PIVROW.append(i)
            break
ERANK = len(RPIV)
for h in sorted(RPIV):
    for g in sorted(RPIV):
        if g > h and ((RPIV[g][0] >> h) & 1) == 1:
            RPIV[g] = (RPIV[g][0] ^ RPIV[h][0], RPIV[g][1] ^ RPIV[h][1])
PIVSET = set(PIVROW)


def redrow(u):
    """the cuttings whose symmetric difference is the piece set u, else None"""
    v, c = u, 0
    while v:
        h = v.bit_length() - 1
        if h not in RPIV:
            return None
        bv, bc = RPIV[h]
        v ^= bv
        c ^= bc
    return c


def rowsof(c):
    return [i for i in range(NS) if (c >> i) & 1]


def xorok(c, S):
    """fold the named cuttings and compare on all 192 piece coordinates"""
    idx = rowsof(c)
    got = INCL[idx].sum(axis=0) & 1
    tgt = np.array([(S >> j) & 1 for j in range(NPO)], dtype=np.int64)
    return bool((got == tgt).all()), len(idx)


# a second, independent elimination, this one over the pieces, giving the kernel
CPACK = np.packbits(INC, axis=0, bitorder="little")
COLI = [int.from_bytes(CPACK[:, j].tobytes(), "little") for j in range(NPO)]
CPIV, KER = {}, []
for j in range(NPO):
    v, w = COLI[j], 1 << j
    while v:
        h = v.bit_length() - 1
        if h in CPIV:
            bv, bw = CPIV[h]
            v ^= bv
            w ^= bw
        else:
            CPIV[h] = (v, w)
            break
    if v == 0:
        KER.append(w)
CRANK, NKER = len(CPIV), len(KER)
KMAT = np.zeros((NPO, NKER), dtype=np.float64)
for a, w in enumerate(KER):
    for j in range(NPO):
        if (w >> j) & 1:
            KMAT[j, a] = 1.0
KSYN = np.rint(INCL.astype(np.float64) @ KMAT).astype(np.int64) & 1
KZERO = KSYN.shape == (NS, NKER) and int(KSYN.max()) == 0
KIND = len(basis(list(KER))) == NKER
KPV = rref(KER)
KB = [KPV[h] for h in sorted(KPV)]
KWT = sorted(bin(w).count("1") for w in KB)


def bpar(w):
    p = 0
    for e in range(8):
        p |= (bin(w & EMASK[e]).count("1") & 1) << (7 - e)
    return p


def qpar(w):
    p = 0
    for q in range(4):
        p |= (bin(w & QMASK[q]).count("1") & 1) << (3 - q)
    return p


def spanof(vals):
    piv = basis(list(vals))
    out = set([0])
    for h in sorted(piv):
        out |= set(x ^ piv[h] for x in out)
    return piv, sorted(out)


def annih(sp, n):
    return [u for u in range(1 << n)
            if all((bin(u & x).count("1") & 1) == 0 for x in sp)]


def uset(u, n, masks):
    S = 0
    for k in range(n):
        if (u >> (n - 1 - k)) & 1:
            S |= masks[k]
    return S


def bshow(u, n):
    return "".join("1" if (u >> (n - 1 - k)) & 1 else "0" for k in range(n))


def cert(S):
    """a forced set gets a cutting combination, a free set a kernel word meeting it oddly"""
    c = redrow(S)
    if c is not None:
        return 1, c
    for a, w in enumerate(KB):
        if (bin(w & S).count("1") & 1) == 1:
            return 0, a
    return -1, -1


QPV, QSPAN = spanof(qpar(w) for w in KB)
BPV, BSPAN = spanof(bpar(w) for w in KB)
D4, D8 = len(QPV), len(BPV)
QANN, BANN = annih(QSPAN, 4), annih(BSPAN, 8)
BBASIS = [bshow(BPV[h], 8) for h in sorted(BPV)]

# ---- the table, its two spaces, and the symmetries that fix the canonical piece order
RS = INCL.sum(axis=1)
RMIN, RMAX = int(RS.min()), int(RS.max())
CMIN, CMAX = int(CSUM.min()), int(CSUM.max())
emit("cycle 740: INC {0}x{1} per-cutting {2} to {3} per-piece {4} to {5} rowrank {6} "
     "colrank {7} kernel {8} distinct {9}".format(NS, NPO, RMIN, RMAX, CMIN, CMAX,
                                                  ERANK, CRANK, NKER, NDIST))
emit("kernel words checked on every cutting, least weight {0} greatest {1}".format(
    KWT[0], KWT[-1]))
gate(INC.shape == (15800, 192) and NS == 15800 and NPO == 192 and FULL == set([24])
     and RMIN == 24 and RMAX == 24, "G01",
     "the cuttings of least cost form a {0} by {1} table over the two element field, "
     "{2} pieces to a cutting in the search and in the table alike".format(NS, NPO, RMIN))
gate(CMIN == CMAX and CMIN == 1975 and (CMIN & 1) == 1, "G02",
     "every one of the {0} pieces is used by exactly {1} cuttings, an odd count".format(
         NPO, CMIN))
gate(ERANK == 88 and CRANK == 88 and NKER == 104 and NKER == NPO - CRANK, "G03",
     "the elimination over the cuttings and the independent elimination over the pieces "
     "return the same rank {0}, leaving a kernel of dimension {1}".format(ERANK, NKER))
gate(NDIST == NS, "G04", "the {0} cuttings are pairwise distinct as piece sets".format(NS))
gate(KZERO and KIND and len(KB) == NKER, "G05",
     "all {0} kernel words meet every one of the {1} cuttings evenly and are "
     "independent".format(NKER, NS))
gate(CPOK and coll == 0 and len(CP) == 48, "G06",
     "the {0} symmetries permute cuttings and pieces leaving the table fixed, which is "
     "what fixes the canonical piece order the blocks are cut from".format(48))

# ---- the whole set as the symmetric difference of every cutting ----
PKX = np.bitwise_xor.reduce(np.packbits(INC, axis=1), axis=0)
NFULLB = int((PKX == 255).sum())
ALLONES = NFULLB == PKX.shape[0] and PKX.shape[0] == NPO // 8
NODD = int((CSUM & 1).sum())
PARONE = NODD == NPO
CW = redrow(ALLP)
WOK, WSZ = xorok(CW, ALLP)
emit("whole set: xor of all {0} cuttings fills {1} packed bytes and {2} odd columns, "
     "and a pivot combination of {3}".format(NS, NFULLB, NODD, WSZ))
gate(ALLONES and PARONE and NODD == NPO, "G07",
     "the symmetric difference of all {0} cuttings is the whole piece set: all {1} packed "
     "bytes come out full and all {2} column counts come out odd".format(
         NS, NFULLB, NODD))
gate(WOK and set(rowsof(CW)) <= PIVSET, "G08",
     "the whole set is carried a second way, by an explicit combination of {0} pivot "
     "cuttings checked on all {1} piece coordinates".format(WSZ, NPO))

# ---- the quarter parity image of the kernel ----
FIVE = [("whole", ALLP), ("L", QMASK[0] | QMASK[1]), ("R", QMASK[2] | QMASK[3]),
        ("Q2", QMASK[2]), ("Q3", QMASK[3])]
NOODD = all((bin(w & S).count("1") & 1) == 0 for _nm, S in FIVE for w in KB)
Q0ODD = [w for w in KB if (bin(w & QMASK[0]).count("1") & 1) == 1]
QPRED = [0, 12]
emit("quarter image dim {0} words {1} block image dim {2} words {3} basis {4}".format(
    D4, ",".join(bshow(x, 4) for x in QSPAN), D8, len(BSPAN), ",".join(BBASIS)))
gate(NOODD and len(FIVE) == 5, "G09",
     "no kernel word meets the whole set, either half or either quarter of the second "
     "half oddly, which is the previous cycle's forcing pattern seen from the kernel")
gate([x for x in QSPAN] == QPRED and D4 == 1 and len(Q0ODD) > 0, "G10",
     "the quarter parity image is exactly the two words {0}: contained in the "
     "annihilator of the forced quarters, and its generator is present because kernel "
     "words meet the first quarter oddly".format(
         ",".join(bshow(x, 4) for x in QSPAN)))

# ---- all 16 quarter unions, by direct membership and by the annihilator ----
QCERT = [cert(uset(u, 4, QMASK)) for u in range(16)]
QDIR = [k == 1 for k, _d in QCERT]
QAOK = all(QDIR[u] == (u in set(QANN)) for u in range(16))
QPOS, QNEG = True, True
for u in range(16):
    k, d = QCERT[u]
    S = uset(u, 4, QMASK)
    if k == 1:
        QPOS = QPOS and xorok(d, S)[0]
    elif k == 0:
        QNEG = QNEG and (bin(KB[d] & S).count("1") & 1) == 1
    else:
        QPOS = False
QNAME = {0: "empty", 3: "R", 12: "L", 15: "whole", 1: "Q3", 2: "Q2", 13: "compQ2",
         14: "compQ3"}
emit("quarter unions forced {0} of {1}: {2}".format(
    sum(1 for x in QDIR if x), 16,
    ",".join(QNAME.get(u, bshow(u, 4)) for u in range(16) if QDIR[u])))
gate(QAOK and sum(1 for x in QDIR if x) == len(QANN) and QDIR[13] and QDIR[14], "G11",
     "of the {0} quarter unions exactly the {1} annihilating the image are forced, the "
     "two quarter complements among them, and the direct membership test agrees with "
     "the annihilator one for one".format(16, 8))
gate(QPOS and QNEG and all(k in (0, 1) for k, _d in QCERT), "G12",
     "each of the {0} quarter unions carries its own certificate: a combination checked "
     "piece by piece when forced, a kernel word meeting it oddly when free".format(16))

# ---- the block parity image and all 256 block unions ----
CONS = all(((p >> 3) & 1) == ((p >> 2) & 1) and ((p >> 1) & 1) == (p & 1)
           and (((p >> 7) ^ (p >> 6) ^ (p >> 5) ^ (p >> 4)) & 1) == 0
           for p in [bpar(w) for w in KB])
FIDX = [sum(1 << (7 - e) for e in range(8) if (EMASK[e] & S) == EMASK[e])
        for _nm, S in FIVE]
FOK = all(uset(u, 8, EMASK) == S for u, (_nm, S) in zip(FIDX, FIVE))
FPV, FSPAN = spanof(FIDX)
BOUND = 8 - len(FPV)
INANN = all(all((bin(x & y).count("1") & 1) == 0 for y in FSPAN) for x in BSPAN)
BCERT = [cert(uset(u, 8, EMASK)) for u in range(256)]
BDIR = [k == 1 for k, _d in BCERT]
BAOK = all(BDIR[u] == (u in set(BANN)) for u in range(256))
NF256 = sum(1 for x in BDIR if x)
BPOS, BNEG = True, True
for u in range(256):
    k, d = BCERT[u]
    S = uset(u, 8, EMASK)
    if k == 1:
        BPOS = BPOS and xorok(d, S)[0]
    elif k == 0:
        BNEG = BNEG and (bin(KB[d] & S).count("1") & 1) == 1
    else:
        BPOS = False
FSET = [u for u in range(256) if BDIR[u]]
CLOSED = all(((a ^ b) in set(FSET)) for a in FSET for b in FSET) and 0 in FSET
PAIRED = all(all(((u >> (2 * k)) & 1) == ((u >> (2 * k + 1)) & 1) for k in range(4))
             and ((u >> 7) & 1) == ((u >> 5) & 1) for u in FSET)
FIF = [("whole", ALLP), ("L", QMASK[0] | QMASK[1]), ("R", QMASK[2] | QMASK[3])]
FIF += [("Q{0}".format(q), QMASK[q]) for q in range(4)]
FIF += [("E{0}".format(e), EMASK[e]) for e in range(8)]
FNAM = sorted(nm for nm, S in FIF if redrow(S) is not None)
UNAM = sorted(nm for nm, S in FIF if redrow(S) is None)
emit("block unions forced {0} of {1}, annihilator {2}, two to the {3} less {4}".format(
    NF256, 256, len(BANN), 8, D8))
emit("of the 15 blocks forced " + ",".join(FNAM) + "; free " + ",".join(UNAM))
gate(FOK and INANN and CONS and D8 == BOUND and len(BSPAN) == (1 << D8), "G13",
     "the block parity image annihilates the block words of the {0} sets the previous "
     "cycle found forced, which bounds its dimension by {1}; the measurement attains "
     "that bound at {2} with {3} words".format(len(FIVE), BOUND, D8, len(BSPAN)))
gate(BAOK and len(BCERT) == 256, "G14",
     "on all {0} block unions the direct membership test and the annihilator of the "
     "measured image return the same answer".format(256))
gate(NF256 == len(BANN) and NF256 == (1 << (8 - D8)), "G15",
     "exactly {0} of the {1} block unions are forced, two to the {2} less {3}".format(
         NF256, 256, 8, D8))
gate(BPOS and BNEG and all(k in (0, 1) for k, _d in BCERT), "G16",
     "each of the {0} block unions carries its own certificate, checked piece by piece "
     "when forced and by an odd kernel meet when free".format(256))
gate(FNAM == ["L", "Q2", "Q3", "R", "whole"] and len(FIF) == 15
     and UNAM == ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "Q0", "Q1"], "G17",
     "read back on the {0} block indicators the sweep returns the previous cycle's "
     "answer: the whole set, its halves and the two quarters of the second half".format(15))
gate(CLOSED and len(set(FSET)) == NF256, "G18",
     "the forced block unions contain the empty set and are closed under symmetric "
     "difference, so they are a space of {0} sets".format(NF256))
gate(PAIRED, "G19",
     "every forced block union is a union of quarters: no block of {0} pieces is forced "
     "alone, and the two quarters of the first half are forced only together".format(24))

# ---- explicit combinations for the half, the third quarter and the two complements ----
COMB = []
for nm, S in (("L", QMASK[0] | QMASK[1]), ("Q2", QMASK[2]), ("compQ2", ALLP ^ QMASK[2]),
              ("compQ3", ALLP ^ QMASK[3])):
    c = redrow(S)
    ok, sz = xorok(c, S)
    COMB.append((nm, ok, sz, set(rowsof(c)) <= PIVSET))
emit("combinations " + " ".join("{0} {1}".format(nm, cshow(sz))
                                for nm, _o, sz, _p in COMB))
gate(all(o for _n, o, _s, _p in COMB) and all(p for _n, _o, _s, p in COMB), "G20",
     "the first half and the third quarter are the symmetric differences of {0} and {1} "
     "pivot cuttings, each checked on all {2} piece coordinates".format(
         COMB[0][2], COMB[1][2], NPO))
gate(COMB[2][1] and COMB[3][1] and COMB[2][3] and COMB[3][3], "G21",
     "the two quarter complements, forced here for the first time, are the symmetric "
     "differences of {0} and {1} pivot cuttings, checked the same way".format(
         COMB[2][2], COMB[3][2]))

# ---- a kernel witness for each free block ----
FREEB = [("E{0}".format(e), EMASK[e]) for e in range(8)]
FREEB += [("Q0", QMASK[0]), ("Q1", QMASK[1])]
WIT = []
for nm, M in FREEB:
    odd = [w for w in KB if (bin(w & M).count("1") & 1) == 1]
    ev = [w for w in KB if (bin(w & M).count("1") & 1) == 0]
    best = min(odd, key=lambda w: (bin(w).count("1"), w))
    step = True
    while step:
        step = False
        for w in ev:
            if bin(best ^ w).count("1") < bin(best).count("1"):
                best ^= w
                step = True
    WIT.append((nm, M, best))

SEED, REDRAW = 74000, 0
while True:
    GP = sorted(int(x) for x in np.random.default_rng(SEED).choice(NPO, 20, replace=False))
    GM = 0
    for j in GP:
        GM |= 1 << j
    GODD = [w for w in KB if (bin(w & GM).count("1") & 1) == 1]
    if GODD:
        break
    REDRAW += 1
    SEED += 1
GW = min(GODD, key=lambda w: (bin(w).count("1"), w))

WALL = [w for _nm, _M, w in WIT] + [GW]
WMAT = np.zeros((NPO, len(WALL)), dtype=np.float64)
for a, w in enumerate(WALL):
    for j in range(NPO):
        if (w >> j) & 1:
            WMAT[j, a] = 1.0
WSYN = np.rint(INCL.astype(np.float64) @ WMAT).astype(np.int64) & 1
WZERO = WSYN.shape == (NS, len(WALL)) and int(WSYN.max()) == 0
WODD = all((bin(w & M).count("1") & 1) == 1 for _nm, M, w in WIT)
WWT = [bin(w).count("1") for _nm, _M, w in WIT]
WIMG = all(bpar(w) in set(BSPAN) for _nm, _M, w in WIT)
WBIT = all(((bpar(w) >> (7 - e)) & 1) == 1 for e, (_nm, _M, w) in enumerate(WIT[:8]))
WBIT = WBIT and all(((bpar(w) >> (7 - 2 * q)) ^ (bpar(w) >> (6 - 2 * q))) & 1 == 1
                    for q, (_nm, _M, w) in enumerate(WIT[8:]))
PAIRW = min(bin(KB[a] ^ KB[b]).count("1")
            for a in range(NKER) for b in range(a + 1, NKER))
emit("witness weights " + vshow(WWT) + " parities "
     + ",".join(bshow(bpar(w), 8) for _nm, _M, w in WIT[:2])
     + " least basis pair weight {0}".format(PAIRW))
gate(WZERO and WODD and len(WIT) == len(UNAM), "G22",
     "each of the {0} free blocks has a kernel witness: zero syndrome on all {1} "
     "cuttings and an odd meet with its own block".format(len(WIT), NS))
gate(set(WWT) == set([KWT[0]]) and PAIRW == KWT[0], "G23",
     "a reduction over the kernel basis gets every free block down to a witness of "
     "weight {0}, which is also the least weight in that basis and the least weight any "
     "pair of basis words reaches".format(KWT[0]))
gate(WIMG and WBIT, "G24",
     "every witness parity word lies in the measured block image and is odd on the "
     "block it was found for, the two free quarters included")

# ---- the two planted controls ----
PLANT = sorted(int(x) for x in np.random.default_rng(74000).choice(NS, 30, replace=False))
PF2 = 0
for i in PLANT:
    PF2 ^= BITS[i]
CPL = redrow(PF2)
POKE, PSZ = xorok(CPL, PF2) if CPL is not None else (False, -1)
PIDX = set(rowsof(CPL)) if CPL is not None else set()
XS = PF2 ^ (QMASK[0] | QMASK[1])
CXS = redrow(XS)
XOKE, XSZ = xorok(CXS, XS) if CXS is not None else (False, -1)
GFREE = redrow(GM) is None
emit("planted forced weight {0} from {1} cuttings, recovered {2}; with the half {3}; "
     "planted free {4} pieces seed {5} redraws {6} witness weight {7}".format(
         bin(PF2).count("1"), len(PLANT), cshow(PSZ), cshow(XSZ), len(GP), SEED, REDRAW,
         bin(GW).count("1")))
gate(POKE and PIDX != set(PLANT) and PIDX <= PIVSET, "G25",
     "the planted forced set is recovered blind as forced, by a combination of {0} pivot "
     "cuttings that is not the {1} cuttings planted, checked piece by piece".format(
         PSZ, len(PLANT)))
gate(XOKE and CXS is not None, "G26",
     "its symmetric difference with the first half, a set that is no block union, is "
     "forced too, by {0} pivot cuttings checked the same way".format(XSZ))
gate(GFREE and (bin(GW & GM).count("1") & 1) == 1 and len(GP) == 20, "G27",
     "the planted {0} piece set is not forced: a kernel word of weight {1} with zero "
     "syndrome meets it oddly, after {2} redraws".format(20, bin(GW).count("1"), REDRAW))

EL = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
emit("elapsed under {0} s peak memory under {1} MB".format(upto(EL, 10), upto(RSS, 100)))
gate(EL < 900.0, "G28", "the whole runner finishes under {0} seconds".format(900))
gate(OUT[0] + 120 < 5500, "G29", "its output stays under {0} characters".format(5500))

emit("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
