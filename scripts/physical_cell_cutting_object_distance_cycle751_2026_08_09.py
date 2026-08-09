"""Cycle 751: the distance a carrier makes is the distance the object already has.

The unit four-cube on sixteen corners cuts into least-volume pieces at the adjacency
cost floor in 15800 ways, and those cuttings use 192 pieces between them. A set of
pieces carries a reading when the cuttings it meets an odd number of times are exactly
the ones the reading marks. Cycle 742 found the least size for the charge called four,
sixteen pieces; cycle 748 counted 132 of them across the system, falling into six
families under the 384 symmetries of the table; cycle 750 joined two pieces of one such
carrier whenever no cutting used both, and found the corners and edges of a four-cube on
60 of the 132 and two separate three-cubes on the other 72, with the count of shared
cuttings settling the distance inside.

Cycle 750 built that shape from sixteen pieces held in isolation, which leaves the plain
worry that the shape is an artefact of the isolation. This runner takes the isolation
away. Join every one of the 192 pieces to every other that shares no cutting with it.
The result is one connected object, 33 joins at each piece, 3168 joins in all, and no
two pieces standing more than three steps apart.

Then compare. Every pair inside a smallest carrier of four that the carrier's own shape
puts one, two or three steps apart stands exactly that far in the whole object, all
10752 of them, and 2496 of those are pairs the whole-object walk was free to shorten and
did not. Sixteen pieces picked evenly spaced instead fail this: 730 of 768 such sets
have a pair brought closer by a piece outside them. The one place a carrier bends is the
eight far corners of a four-cube, which fold from four steps to three because the object
holds nothing farther apart than three.

The object itself is not evenly built: the count of pieces joined to both ends of a pair
takes nine shapes at one step and ten at three. So the four-cube is not inherited from an
even surround. It is what carrying the charge makes.

Class-A: integer and field-with-two-elements arithmetic on a finite explicit object, no
solver. Every count below is measured here.
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

PK = np.packbits(INC, axis=1)
LUT = np.array([bin(i).count("1") for i in range(256)], dtype=np.uint8)
SZC = [4, 6]
SZG = [4]
EA = dict((k, []) for k in SZC)
EB = dict((k, []) for k in SZC)
DIS = dict((k, set()) for k in SZG)
for lo in range(0, NS, 200):
    hi = min(lo + 100, NS)
    d = LUT[np.bitwise_xor(PK[lo:hi, None, :], PK[None, :, :])].sum(axis=2, dtype=np.int16)
    for k in SZC:
        rr, cc = np.nonzero(d == 2 * k)
        keep = (rr + lo) < cc
        aa = (rr[keep] + lo).tolist()
        bb = cc[keep].tolist()
        EA[k].extend(aa)
        EB[k].extend(bb)
        if k in DIS:
            for a, b in zip(aa, bb):
                DIS[k].add(BITS[a] ^ BITS[b])
for k in SZC:
    EA[k] = np.asarray(EA[k], dtype=np.int64)
    EB[k] = np.asarray(EB[k], dtype=np.int64)
KEY = dict((k, sorted(DIS[k])) for k in SZG)

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


def perp(piv, n):
    """the weights on n pieces annihilating everything the pivot table spans"""
    out = []
    for j in range(n):
        if j in piv:
            continue
        w = 1 << j
        for h in piv:
            if ((piv[h] >> j) & 1) == 1:
                w |= 1 << h
        out.append(w)
    for w in out:
        for r in piv.values():
            assert (bin(w & r).count("1") & 1) == 0, "a uniform weight must annihilate"
    return out


TK = {}
for k in SZG:
    TK[k] = rref(s ^ KEY[k][0] for s in KEY[k][1:])

NUL = perp(TK[4], NPO)
WM = np.zeros((NPO, len(NUL)), dtype=np.int64)
for c, w in enumerate(NUL):
    for j in range(NPO):
        if ((w >> j) & 1) == 1:
            WM[j, c] = 1
FF = (INCL @ WM) & 1
PIV = {}
for c in range(FF.shape[1]):
    a = FF[:, c].astype(np.uint8)
    r = int.from_bytes(np.packbits(a).tobytes(), "big")
    while r:
        h = r.bit_length() - 1
        if h not in PIV:
            PIV[h] = (r, a)
            break
        r ^= PIV[h][0]
        a = a ^ PIV[h][1]
BAS = [PIV[h][1] for h in sorted(PIV)]
FUN = []
for mask in range(1 << len(BAS)):
    f = np.zeros(NS, dtype=np.uint8)
    for i, b in enumerate(BAS):
        if ((mask >> i) & 1) == 1:
            f = f ^ b
    FUN.append(f)

NAMED, HITS = {}, {}
for f in FUN:
    one = int(f.sum())
    if one in (0, NS):
        continue
    g = f if 2 * one <= NS else (f ^ 1)
    d4 = g[EA[4]] ^ g[EB[4]]
    d6 = g[EA[6]] ^ g[EB[6]]
    nm = "four" if d4.max() == 0 else ("six" if d6.max() == 0 else "seven")
    NAMED[nm] = g
    HITS[nm] = HITS.get(nm, 0) + 1

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

# ---- the twelve targets: eight readings plus the four planted controls of Part 3 ----
ZERO = np.zeros(NS, dtype=np.uint8)
ONE = np.ones(NS, dtype=np.uint8)
TGT = [("zero", ZERO), ("one", ONE)]
for nm in ["four", "six", "seven"]:
    TGT.append((nm, NAMED[nm]))
    TGT.append((nm + "-flip", NAMED[nm] ^ 1))
PLANT = [("pair (2,2)", (10, 55, 120, 168)),
         ("h6 (6,2)", (3, 21, 44, 61, 77, 90, 101, 155)),
         ("in-left quarters (3,5)", (2, 9, 30, 50, 63, 71, 80, 91)),
         ("in-right one quarter (0,8)", (150, 151, 160, 165, 170, 180, 185, 191))]
for pname, psupp in PLANT:
    TGT.append((pname, (INCL[:, list(psupp)].sum(axis=1) & 1).astype(np.uint8)))
NT = len(TGT)

# ---- the 88 pivot cuttings and a piece's packed parities, rebuilt from INC ----
EPACK = np.packbits(INC, axis=1, bitorder="little")
EROW = [int.from_bytes(EPACK[i].tobytes(), "little") for i in range(NS)]
EBAS0 = {}
EPIVL = []
for i in range(NS):
    v = EROW[i]
    while v:
        lb = v.bit_length() - 1
        if lb in EBAS0:
            v ^= EBAS0[lb]
        else:
            EBAS0[lb] = v
            EPIVL.append(i)
            v = 0
ERANK = len(EPIVL)
EPIV = np.array(sorted(EPIVL), dtype=np.int64)
P88 = INC[EPIV]


def pack88(bits):
    """the parities on the 88 pivot cuttings, as two sixty-four bit words"""
    b = np.asarray(bits, dtype=np.uint64)
    out = np.zeros(b.shape[:-1] + (2,), dtype=np.uint64)
    for i in range(88):
        wd, sh = divmod(i, 64)
        out[..., wd] |= b[..., i] << np.uint64(sh)
    return out


COLS = pack88(P88.T)


# ---- the eighteen readings: twelve as before, five planted fourteen-sets, one control ----
PSEED = 74516
P16SPEC = [("p16-a4444", (4, 4, 4, 4)),
           ("p16-a0-0-6-10", (0, 0, 6, 10)),
           ("p16-a8044", (8, 0, 4, 4)),
           ("p16-a2-2-2-10", (2, 2, 2, 10)),
           ("p16-a0-8-0-8", (0, 8, 0, 8))]
prng2 = np.random.default_rng(PSEED)
PSET = {}
TNAME = [nm for nm, _f in TGT]
FVEC = [f for _nm, f in TGT]
for pi, (pnm, prof) in enumerate(P16SPEC):
    Sp = [144] + [145 + int(c) for c in prng2.choice(47, prof[3] - 1, replace=False)]
    for q in range(3):
        Sp += [48 * q + int(c) for c in prng2.choice(48, prof[q], replace=False)]
    Sp = sorted(Sp)
    PSET[NT + pi] = tuple(Sp)
    TNAME.append(pnm)
    FVEC.append((INCL[:, Sp].sum(axis=1) & 1).astype(np.uint8))
FODD = np.zeros(NS, dtype=np.uint8)
FODD[0] = 1
TNAME.append("odd-ctl")
FVEC.append(FODD)
NTG = len(FVEC)
TCTL = NTG - 1
FV = np.stack(FVEC)
TG = pack88(FV[:, EPIV])

# ---- the parities a search of the pieces is forced to respect on each block ----
LBAS = {}
for i in range(NS):
    v = EROW[i]
    a = 0
    for k in range(NTG):
        a |= int(FV[k, i]) << k
    while v:
        lb = v.bit_length() - 1
        if lb in LBAS:
            bv, ba = LBAS[lb]
            v ^= bv
            a ^= ba
        else:
            LBAS[lb] = (v, a)
            v = 0


def reduce_u(u_int):
    """the forced parities of a block, or None when the block is free"""
    v, a = u_int, 0
    while v:
        lb = v.bit_length() - 1
        if lb not in LBAS:
            return None
        bv, ba = LBAS[lb]
        v ^= bv
        a ^= ba
    return a


def uint_of(cols):
    u = 0
    for c in cols:
        u |= 1 << int(c)
    return u


BLK = {"total": range(192), "L": range(96), "R": range(96, 192)}
for q in range(4):
    BLK["Q{0}".format(q)] = range(48 * q, 48 * q + 48)
for e in range(8):
    BLK["E{0}".format(e)] = range(24 * e, 24 * e + 24)
FORCED = dict((nm, reduce_u(uint_of(b))) for nm, b in BLK.items())

# ---- lex extension chains over the quarters and the eighths ----
BQ = 27
MQ = np.uint64(2**BQ - 1)
Q_COLS = [np.arange(48 * q, 48 * q + 48) for q in range(4)]
E_COLS = [np.arange(24 * e, 24 * e + 24) for e in range(8)]


def build_chain(cols, kmax):
    """Lex extension chain over cols. Returns T[k] (syn), NOFF[k].

    T[k] row order: blocks by lead column c ascending; block c = rows of
    T[k-1] with min column > c, in their T[k-1] order, XOR syn(c).
    NOFF[k][c] = first row of block c; NOFF[k][n] = len(T[k]).
    """
    n = len(cols)
    T = {0: np.zeros((1, 2), dtype=np.uint64)}
    NOFF = {1: np.arange(n + 1, dtype=np.int64)}
    if kmax >= 1:
        T[1] = COLS[cols].copy()
    for k in range(1, kmax):
        prev, poff = T[k], NOFF[k]
        total = sum(len(prev) - poff[c + 1] for c in range(n))
        out = np.empty((total, 2), dtype=np.uint64)
        noff = np.empty(n + 1, dtype=np.int64)
        pos = 0
        for c in range(n):
            blk = prev[poff[c + 1]:]
            noff[c] = pos
            if len(blk):
                np.bitwise_xor(blk, COLS[cols[c]], out=out[pos:pos + len(blk)])
            pos += len(blk)
        noff[n] = pos
        T[k + 1] = out
        NOFF[k + 1] = noff
    return T, NOFF


def unrank(NOFF, k, idx, cols):
    """idx in T[k] -> global column list (len k)."""
    out = []
    idx = int(idx)
    for lvl in range(k, 1, -1):
        no = NOFF[lvl]
        c = int(np.searchsorted(no, idx, side="right")) - 1
        out.append(int(cols[c]))
        idx = int(NOFF[lvl - 1][c + 1]) + (idx - int(no[c]))
    if k >= 1:
        out.append(int(cols[idx]))
    return out


QCH = []
for q in range(4):
    QCH.append(build_chain(Q_COLS[q], 5))

_C3 = list(itertools.combinations(range(48), 3))
UNROK = True
for q in range(4):
    for idx in (0, 5, 1000, 17295):
        got = sorted(unrank(QCH[q][1], 3, idx, Q_COLS[q]))
        exp = sorted(int(Q_COLS[q][c]) for c in _C3[idx])
        UNROK = UNROK and got == exp

_T6_CACHE = {}


def get_T6(q):
    """(T6, NOFF6) for quarter q, built on demand from T5."""
    if q in _T6_CACHE:
        return _T6_CACHE[q]
    T, NOFF = QCH[q]
    n = 48
    cols = Q_COLS[q]
    prev, poff = T[5], NOFF[5]
    total = sum(len(prev) - poff[c + 1] for c in range(n))
    out = np.empty((total, 2), dtype=np.uint64)
    noff = np.empty(n + 1, dtype=np.int64)
    pos = 0
    for c in range(n):
        blk = prev[poff[c + 1]:]
        noff[c] = pos
        if len(blk):
            np.bitwise_xor(blk, COLS[cols[c]], out=out[pos:pos + len(blk)])
        pos += len(blk)
    noff[n] = pos
    _T6_CACHE[q] = (out, noff)
    return _T6_CACHE[q]


def qtab(q, k):
    """(syn table, unranker) for k-subsets of quarter q, k <= 6."""
    if k <= 5:
        T, NOFF = QCH[q]
        return T[k], (lambda i, q=q, k=k: unrank(QCH[q][1], k, i, Q_COLS[q]))
    T6, noff6 = get_T6(q)

    def unr6(i, q=q, noff6=noff6):
        i = int(i)
        c = int(np.searchsorted(noff6, i, side="right")) - 1
        idx5 = int(QCH[q][1][5][c + 1]) + (i - int(noff6[c]))
        return [int(Q_COLS[q][c])] + unrank(QCH[q][1], 5, idx5, Q_COLS[q])
    return T6, unr6


# ---------------------------------------------- Part 3: the meet engine at twelve
# A set of pieces is split by quarter into a cell (q0, q1, q2, q3). One part is streamed
# and the rest are met against it. Every meeting is pruned by the parities forced inside
# the union of the blocks already joined, so no wide product is ever built.

CAP = 200000
TABCAP = 30000000
CHUNK = 2000000
BLOWN = []
QCOLS = [list(range(48 * q, 48 * q + 48)) for q in range(4)]
ECOLS = [list(range(24 * e, 24 * e + 24)) for e in range(8)]
CINT = []
for _j in range(NPO):
    _v = 0
    for _i in range(88):
        if P88[_i, _j]:
            _v |= 1 << _i
    CINT.append(_v)


def col_rank(S):
    """rank of a set of columns as vectors on the 88 pivot cuttings"""
    piv = {}
    for j in S:
        v = CINT[j]
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h]
            else:
                piv[h] = v
                break
    return len(piv)


def compl(S):
    s = set(S)
    return [j for j in range(NPO) if j not in s]


def inner(S):
    """basis of the parities living inside a column set: x with x.COLS[j] = 0 off S"""
    out = compl(S)
    piv, ker = {}, []
    for i in range(88):
        v, w = 0, 1 << i
        for a, j in enumerate(out):
            if (CINT[j] >> i) & 1:
                v |= 1 << a
        while v:
            h = v.bit_length() - 1
            if h in piv:
                bv, bw = piv[h]
                v ^= bv
                w ^= bw
            else:
                piv[h] = (v, w)
                break
        if v == 0:
            ker.append(w)
    return ker


def sub_kernel(S):
    """basis of the piece sets inside S whose parities on the cuttings all vanish"""
    piv, ker = {}, []
    for a, j in enumerate(S):
        v, w = CINT[j], 1 << a
        while v:
            h = v.bit_length() - 1
            if h in piv:
                bv, bw = piv[h]
                v ^= bv
                w ^= bw
            else:
                piv[h] = (v, w)
                break
        if v == 0:
            ker.append(w)
    return ker


def keymap(X):
    """byte tables turning a packed syndrome into its parities under a basis"""
    d = len(X)
    nw = max(1, (d + 63) // 64)
    lut = np.zeros((nw, 11, 256), dtype=np.uint64)
    con = np.zeros((11, 8, nw), dtype=np.uint64)
    for b in range(11):
        for p in range(8):
            i = 8 * b + p
            if i >= 88:
                continue
            for a, x in enumerate(X):
                if (x >> i) & 1:
                    con[b, p, a // 64] |= np.uint64(1) << np.uint64(a & 63)
    for b in range(11):
        for v in range(256):
            acc = np.zeros(nw, dtype=np.uint64)
            for p in range(8):
                if (v >> p) & 1:
                    acc ^= con[b, p]
            lut[:, b, v] = acc
    return lut


def keyof(syn, lut):
    """the parity key of every row of a packed syndrome table"""
    a = np.ascontiguousarray(syn).view(np.uint8).reshape(-1, 16)
    nw = lut.shape[0]
    out = np.zeros((a.shape[0], nw), dtype=np.uint64)
    for b in range(11):
        idx = a[:, b]
        for w in range(nw):
            out[:, w] ^= lut[w, b][idx]
    return out


def key1(vec, lut):
    """the parity key of one packed syndrome"""
    a = np.ascontiguousarray(np.asarray(vec, dtype=np.uint64)).view(np.uint8)
    nw = lut.shape[0]
    out = np.zeros(nw, dtype=np.uint64)
    for b in range(11):
        for w in range(nw):
            out[w] ^= lut[w, b, int(a[b])]
    return out


# ---- part tables: a quarter at weight up to six, an eighth at any weight to twelve ----
_ECH = {}


def echain(e, kmax):
    """the lex extension chain over one block of 24, extended in place as needed"""
    st = _ECH.get(e)
    if st is None:
        cols = np.array(ECOLS[e], dtype=np.int64)
        st = ({1: COLS[cols].copy()}, {1: np.arange(25, dtype=np.int64)}, cols)
        _ECH[e] = st
    T, NOFF, cols = st
    n = 24
    k = max(T)
    while k < kmax:
        prev, poff = T[k], NOFF[k]
        total = sum(len(prev) - poff[c + 1] for c in range(n))
        out = np.empty((total, 2), dtype=np.uint64)
        noff = np.empty(n + 1, dtype=np.int64)
        pos = 0
        for c in range(n):
            blk = prev[poff[c + 1]:]
            noff[c] = pos
            if len(blk):
                np.bitwise_xor(blk, COLS[cols[c]], out=out[pos:pos + len(blk)])
            pos += len(blk)
        noff[n] = pos
        T[k + 1] = out
        NOFF[k + 1] = noff
        k += 1
    return T[kmax], NOFF


ZT = np.zeros((1, 2), dtype=np.uint64)
BMP = np.zeros(2**BQ, dtype=np.uint8)
_INNC = {}
_LUTC = {}
_SKC = {}
_SKN = [0]
SKCAP = 36000000


def inner_of(lky, cols):
    """the internal parity space of a block union, kept across the splits sharing it"""
    hit = _INNC.get(lky)
    if hit is None:
        hit = inner(cols)
        _INNC[lky] = hit
    return hit


def lut_for(lky, cols):
    """the byte tables of a block union, kept across the splits that share it"""
    hit = _LUTC.get(lky)
    if hit is None:
        hit = keymap(inner_of(lky, cols))
        _LUTC[lky] = hit
    return hit


def plan_order(ne, sizes, fky, fcols):
    """the join order whose largest intermediate meet is smallest

    A join keys on the parities living inside the blocks joined so far, so an order
    that joins blocks with no shared internal parity first has nothing to key on and
    forms the whole product. The order is chosen here, and the answer does not depend
    on it: every join is a necessary condition on the same final set.
    """
    n = len(sizes)
    if n < 3:
        return sorted(range(n), key=lambda i: (sizes[i], i))
    cols = [QCOLS[s[1]] if s[0] == "Q" else ECOLS[s[1]] for s in ne]
    dF = min(len(inner_of(fky, fcols)), 62)
    best, bp = None, None
    for p in itertools.permutations(range(n)):
        cur, worst = float(sizes[p[0]]), float(sizes[p[0]])
        acc, accs = list(cols[p[0]]), [(ne[p[0]][0], ne[p[0]][1])]
        for j in range(1, n):
            acc = acc + list(cols[p[j]])
            accs = accs + [(ne[p[j]][0], ne[p[j]][1])]
            d = dF if j == n - 1 else min(
                len(inner_of(("I", tuple(sorted(accs))), acc)), 62)
            cur = cur * sizes[p[j]] / float(1 << d)
            worst = max(worst, cur)
        if best is None or worst < best:
            best, bp = worst, list(p)
    return bp


def sorted_keys(sky, tab, lut):
    """the sorted parity keys of a part table, kept across the splits that share it"""
    hit = _SKC.get(sky)
    if hit is not None:
        return hit
    kb = keyof(tab, lut)[:, 0]
    so = np.argsort(kb, kind="quicksort")
    val = (kb[so], so)
    if _SKN[0] + 2 * len(so) > SKCAP:
        _SKC.clear()
        _SKN[0] = 0
    _SKC[sky] = val
    _SKN[0] += 2 * len(so)
    return val


def part_table(kind, idx, k):
    """(syndrome table, index -> column list, column block) for a part at weight k"""
    if k == 0:
        return ZT, (lambda i: []), []
    if kind == "Q":
        if k > 6:
            raise ValueError("a quarter part was asked for past the six-subset tables")
        T, unr = qtab(idx, k)
        return T, unr, QCOLS[idx]
    T, NOFF = echain(idx, k)
    cols = np.array(ECOLS[idx], dtype=np.int64)
    return T, (lambda i, NOFF=NOFF, k=k, cols=cols: unrank(NOFF, k, i, cols)), ECOLS[idx]


# ---- meeting two tables under the parities forced inside the joined blocks ----
def meet(sA, sB, kb_sorted, order, ka, tk):
    """rows of sA met with rows of sB whose key differs from theirs by the target key"""
    want = ka ^ tk
    lo = np.searchsorted(kb_sorted, want, side="left")
    hi = np.searchsorted(kb_sorted, want, side="right")
    cnt = (hi - lo).astype(np.int64)
    tot = int(cnt.sum())
    if tot > TABCAP:
        BLOWN.append(tot)
        return None, None, None
    if tot == 0:
        z8 = np.zeros((0,), dtype=np.int64)
        return np.zeros((0, 2), dtype=np.uint64), z8, z8
    src = np.repeat(np.arange(len(sA), dtype=np.int64), cnt)
    csum = np.cumsum(cnt)
    off = np.arange(tot, dtype=np.int64) - np.repeat(csum - cnt, cnt)
    dst = order[np.repeat(lo, cnt) + off]
    return sA[src] ^ sB[dst], src, dst


# ---- how a cell is split into a streamed part and the parts met against it ----
def plan_cell(cell):
    """the splits of a cell: one streamed part and the parts met against it

    A quarter is carried whole only while its count stays inside the six-subset tables
    a quarter is tabulated with. Every quarter past that is cut into its two eighths,
    and the cell is covered by the product of those cuts, so a cell holding two heavy
    quarters is searched at its own weight rather than at a lower one.
    """
    q = list(cell)
    if max(q) <= 6:
        best = max(range(4), key=lambda i: (math.comb(48, q[i]), -i))
        A = ("Q", best, q[best])
        B = [("Q", i, q[i]) for i in range(4) if i != best]
        return [(A, B)]
    big = [i for i in range(4) if q[i] > 6]
    ways = []
    for i in big:
        w = []
        for ka in range(0, min(24, q[i]) + 1):
            kb = q[i] - ka
            if 0 <= kb <= 24:
                w.append((ka, kb))
        ways.append(w)
    rest = [("Q", i, q[i]) for i in range(4) if i not in big]
    out = []
    for combo in itertools.product(*ways):
        parts = []
        for (i, (ka, kb)) in zip(big, combo):
            parts += [("E", 2 * i, ka), ("E", 2 * i + 1, kb)]
        parts = parts + rest
        if len(big) == 1:
            u = 0 if math.comb(24, parts[0][2]) >= math.comb(24, parts[1][2]) else 1
        else:
            u = max(range(len(parts)), key=lambda j: (
                math.comb(24 if parts[j][0] == "E" else 48, parts[j][2]), -j))
        out.append((parts[u], [p for (j, p) in enumerate(parts) if j != u]))
    return out


CNT = {}
RES = {}


def run_split(A, B, tids):
    """search one streamed part against the meet of the rest, folded over the targets"""
    Ablk = QCOLS[A[1]] if A[0] == "Q" else ECOLS[A[1]]
    fky = ("F", A[0], A[1])
    lutF = lut_for(fky, compl(Ablk))
    ne = [s for s in B if s[2] > 0]
    tabs = [part_table(*s) for s in ne]
    order = plan_order(ne, [len(t[0]) for t in tabs], fky, compl(Ablk))
    steps = []
    if len(ne) >= 2:
        acc = list(tabs[order[0]][2])
        accs = [(ne[order[0]][0], ne[order[0]][1])]
        for j in range(1, len(ne)):
            oi = order[j]
            acc = acc + list(tabs[oi][2])
            accs = accs + [(ne[oi][0], ne[oi][1])]
            if j == len(ne) - 1:
                lut, lky = lutF, fky
            else:
                lky = ("I", tuple(sorted(accs)))
                lut = lut_for(lky, acc)
            kbs, so = sorted_keys((ne[oi], lky), tabs[oi][0], lut)
            steps.append((oi, lut, kbs, so))
    elif len(ne) == 1:
        kbs, so = sorted_keys((ne[order[0]], fky), tabs[order[0]][0], lutF)
        steps.append((order[0], lutF, kbs, so))
    fin = {}
    for t in tids:
        if len(ne) == 0:
            tk = key1(TG[t], lutF)
            fin[t] = (ZT.copy(), [], []) if not tk.any() else None
            continue
        if len(ne) == 1:
            oi, lut, kbs, so = steps[0]
            tk = key1(TG[t], lut)
            a = int(np.searchsorted(kbs, tk[0], side="left"))
            b = int(np.searchsorted(kbs, tk[0], side="right"))
            sel = so[a:b]
            if lut.shape[0] > 1 and len(sel):
                k2 = keyof(tabs[oi][0][sel], lut)
                sel = sel[np.all(k2 == tk[None, :], axis=1)]
            fin[t] = (tabs[oi][0][sel], [oi], [sel]) if len(sel) else None
            continue
        syn = tabs[order[0]][0]
        idxs = [np.arange(len(syn), dtype=np.int64)]
        who = [order[0]]
        for (oi, lut, kbs, so) in steps:
            tk = key1(TG[t], lut)
            ka = keyof(syn, lut)[:, 0]
            syn2, src, dst = meet(syn, tabs[oi][0], kbs, so, ka, tk[0])
            if syn2 is None:
                return False
            if lut.shape[0] > 1 and len(syn2):
                k2 = keyof(syn2, lut)
                kp = np.all(k2 == tk[None, :], axis=1)
                syn2, src, dst = syn2[kp], src[kp], dst[kp]
            syn = syn2
            idxs = [a[src] for a in idxs] + [dst]
            who = who + [oi]
            if len(syn) == 0:
                break
        fin[t] = (syn, who, idxs) if len(syn) else None
    live = [t for t in tids if fin[t] is not None]
    if not live:
        return True
    k0 = np.concatenate([fin[t][0][:, 0] ^ TG[t, 0] for t in live])
    k1 = np.concatenate([fin[t][0][:, 1] ^ TG[t, 1] for t in live])
    tmark = np.concatenate([np.full(len(fin[t][0]), a, dtype=np.int64)
                            for a, t in enumerate(live)])
    lrow = np.concatenate([np.arange(len(fin[t][0]), dtype=np.int64) for t in live])
    if len(k0) > TABCAP:
        BLOWN.append(len(k0))
        return False
    so = np.argsort(k0, kind="quicksort")
    sk0, sk1 = k0[so], k1[so]
    stm, slr = tmark[so], lrow[so]
    ix = (sk0 & MQ).astype(np.int64)
    BMP[ix] = 1
    Atab, Aunr, _ = part_table(*A)
    hits = dict((t, []) for t in live)
    for lo in range(0, len(Atab), CHUNK):
        x = Atab[lo:lo + CHUNK]
        g = BMP[(x[:, 0] & MQ).astype(np.int64)]
        pos = np.nonzero(g)[0]
        if not len(pos):
            continue
        s0 = x[pos, 0]
        a = np.searchsorted(sk0, s0, side="left")
        b = np.searchsorted(sk0, s0, side="right")
        cnt = (b - a).astype(np.int64)
        tot = int(cnt.sum())
        if not tot:
            continue
        pp = np.repeat(pos, cnt)
        cs = np.cumsum(cnt)
        qq = np.repeat(a, cnt) + (np.arange(tot, dtype=np.int64)
                                  - np.repeat(cs - cnt, cnt))
        keep = sk1[qq] == x[pp, 1]
        pp, qq = pp[keep], qq[keep]
        if not len(pp):
            continue
        tsel, bsel = stm[qq], slr[qq]
        for a2, t in enumerate(live):
            msel = tsel == a2
            if msel.any():
                hits[t].append((pp[msel] + lo, bsel[msel]))
    BMP[ix] = 0
    for t in live:
        hl = hits[t]
        if not hl:
            continue
        ai = np.concatenate([h[0] for h in hl])
        bi2 = np.concatenate([h[1] for h in hl])
        c = CNT.get(t, 0)
        CNT[t] = c + len(ai)
        room = CAP - c
        if room <= 0:
            continue
        ai, bi2 = ai[:room], bi2[:room]
        syn, who, idxs = fin[t]
        rows = []
        for u in range(len(ai)):
            br = int(bi2[u])
            cs2 = list(Aunr(int(ai[u])))
            for pi, oi in enumerate(who):
                cs2 += list(tabs[oi][1](int(idxs[pi][br])))
            rows.append(sorted(cs2))
        RES.setdefault(t, []).append(np.asarray(rows, dtype=np.int64))
    return True


# ---- which cells a reading licenses, and the sweep over them ----
def licensed_cell(cell, m, tid):
    q0, q1, q2, q3 = cell
    for nm, val in (("total", m), ("L", q0 + q1), ("Q2", q2), ("Q3", q3)):
        f = FORCED[nm]
        if f is not None and (val & 1) != ((f >> tid) & 1):
            return False
    return True


def cells_of(m):
    top = min(48, m)
    out = []
    for q0 in range(top + 1):
        for q1 in range(min(top, m - q0) + 1):
            for q2 in range(min(top, m - q0 - q1) + 1):
                q3 = m - q0 - q1 - q2
                if 0 <= q3 <= top:
                    out.append((q0, q1, q2, q3))
    return out


SEEN = {}
PROCD = []


def run_cell(cell, m, tids):
    """one cell, each of its splits once, all live targets folded"""
    ok = True
    act = [t for t in tids if licensed_cell(cell, m, t)]
    if not act:
        return ok
    for t in act:
        SEEN[t] = SEEN.get(t, 0) + 1
    for (A, B) in plan_cell(cell):
        PROCD.append((cell, A, tuple(B)))
        if not run_split(A, B, act):
            ok = False
    return ok


def run_sweep(m, tids):
    """every licensed cell of size m, each split once, all live targets folded"""
    ok = True
    for cell in cells_of(m):
        if not run_cell(cell, m, tids):
            ok = False
    return ok


def coverage(m, tids):
    """(cells met per target, splits done, splits distinct)"""
    return ([SEEN.get(t, 0) for t in tids], len(PROCD), len(set(PROCD)))


def fresh():
    CNT.clear()
    RES.clear()
    SEEN.clear()
    del PROCD[:]


def orbsum(t):
    """orbit sizes folded to a size:count summary, and the closure flag"""
    szs, closed = orbits(t)
    d = {}
    for s in szs:
        d[s] = d.get(s, 0) + 1
    return d, len(szs), closed


def lic_count(m, tid):
    return sum(1 for c in cells_of(m) if licensed_cell(c, m, tid))


# ---- every recorded set checked back against the columns, and folded into orbits ----
def by_width(t):
    g = {}
    for a in RES.get(t, []):
        g.setdefault(a.shape[1], []).append(a)
    return dict((w, np.concatenate(v, axis=0)) for w, v in g.items())


def verify(tids):
    bad, dup, seen = 0, 0, 0
    for t in tids:
        for w, arr in by_width(t).items():
            seen += len(arr)
            syn = np.bitwise_xor.reduce(COLS[arr], axis=1)
            bad += int((syn != TG[t][None, :]).any(axis=1).sum())
            srt = np.sort(arr, axis=1)
            if not np.array_equal(srt, arr):
                bad += 1
            if len(arr) and int((srt[:, 1:] == srt[:, :-1]).sum()) > 0:
                bad += 1
            dup += len(arr) - len(np.unique(arr, axis=0))
    return seen, bad, dup


STAB = [[gi for gi in range(48) if bool(np.array_equal(FV[t][PERMS[gi]], FV[t]))]
        for t in range(NTG)]


def orbits(t):
    """recorded sets folded into orbits of the symmetries that fix the reading"""
    grp = [CP[gi] for gi in STAB[t]]
    out, closed = [], True
    for w, arr in sorted(by_width(t).items()):
        n = len(arr)
        img = [np.sort(cp[arr], axis=1) for cp in grp]
        big = np.concatenate([arr] + img, axis=0).astype(np.uint8)
        uq, inv = np.unique(big, axis=0, return_inverse=True)
        inv = np.asarray(inv).reshape(len(grp) + 1, n)
        pos = -np.ones(len(uq), dtype=np.int64)
        pos[inv[0]] = np.arange(n, dtype=np.int64)
        M = pos[inv[1:]]
        if int((M < 0).sum()):
            closed = False
            M = np.where(M < 0, np.arange(n, dtype=np.int64)[None, :], M)
        lab = M.min(axis=0)
        out += np.bincount(lab)[np.bincount(lab) > 0].tolist()
    return sorted(int(x) for x in out), closed


def has_set(t, cols):
    key = np.array(sorted(int(c) for c in cols), dtype=np.int64)
    for w, arr in by_width(t).items():
        if w != len(key) or not len(arr):
            continue
        if bool((arr == key[None, :]).all(axis=1).any()):
            return True
    return False

# ---- Part 3b: the two seeded order-two piece permutations and the fifty ----
NP = NPO
TGTv = [v for _, v in TGT[:8]]
falab = lab
ORB = [np.nonzero(falab == k)[0] for k in range(4)]


def tshow(t):
    return "(" + ",".join(str(int(c)) for c in t) + ")"


F64 = INC.astype(np.float64)
G = (F64.T @ F64).astype(np.int64)
gate(len(set(np.diag(G).tolist())) == 1 and int(G[0, 0]) == 1975, "G0",
     "the Gram matrix of the table has constant diagonal 1975")
ROWK = {}
for s in range(NS):
    ROWK[tuple(map(int, np.nonzero(INC[s])[0]))] = s
gate(len(ROWK) == NS and NS == 15800, "G1",
     "all 15800 cuttings carry distinct piece supports")


def refine(colors):
    while True:
        CODE = colors[None, :] * 2048 + G
        S = np.sort(CODE, axis=1)
        M = np.hstack([colors[:, None] * (1 << 40), S])
        _, new = np.unique(M, axis=0, return_inverse=True)
        new = new.astype(np.int64)
        if len(set(new.tolist())) == len(set(colors.tolist())):
            return new
        colors = new


base = refine(np.zeros(NP, dtype=np.int64))


def refine_seed(x):
    colors = base.copy()
    colors[x] = colors.max() + 1
    colors = refine(colors)
    for _ in range(400):
        classes = {}
        for i in range(NP):
            classes.setdefault(int(colors[i]), []).append(i)
        big = [mem for mem in classes.values() if len(mem) > 1]
        if not big:
            return colors
        mem = sorted(big, key=lambda m: (len(m), m[0]))[0]
        colors[mem[0]] = colors.max() + 1
        colors = refine(colors)
    return None


ANC = int(ORB[1][0])
ca = refine_seed(ANC)
cb0 = refine_seed(0)
cb1 = refine_seed(5)
gate(ca is not None and cb0 is not None and cb1 is not None, "G2",
     "the anchored and the two seeded colour refinements are all discrete")


def build_pi(cb):
    """the piece permutation matching the anchored colouring to a seeded one"""
    inv = {}
    for i in range(NP):
        inv.setdefault(int(cb[i]), []).append(i)
    pi = np.zeros(NP, dtype=np.int64)
    ok = True
    for i in range(NP):
        mm = inv.get(int(ca[i]), [])
        if len(mm) != 1:
            ok = False
        else:
            pi[i] = mm[0]
    return ok, pi


def cut_perm(pi):
    """the matching permutation of the cuttings induced by a piece permutation"""
    sig = np.zeros(NS, dtype=np.int64)
    ok = True
    for s in range(NS):
        img = tuple(sorted(map(int, pi[np.nonzero(INC[s])[0]])))
        if img in ROWK:
            sig[s] = ROWK[img]
        else:
            ok = False
    return ok and len(set(sig.tolist())) == NS, sig


def orb_rows(pi):
    """image counts of each piece orbit under a piece permutation"""
    out = []
    for k in range(4):
        img = falab[pi[ORB[k]]]
        out.append(tuple(int((img == q).sum()) for q in range(4)))
    return out


AR = np.arange(NP)
OK0, b0 = build_pi(cb0)
OK1, b1 = build_pi(cb1)
SG0, sg0 = cut_perm(b0)
SG1, sg1 = cut_perm(b1)
ROW0, ROW1 = orb_rows(b0), orb_rows(b1)
gate(OK0 and np.array_equal(np.sort(b0), AR) and np.array_equal(b0[b0], AR)
     and SG0 and np.array_equal(INC[sg0][:, b0], INC), "G3",
     "b0 is an order-two piece permutation with a matching cutting permutation")
gate(all(np.array_equal(TGTv[r][sg0], TGTv[r]) for r in range(8)), "G4",
     "b0 fixes all eight readings")
gate(all(not np.array_equal(b0, CP[gi]) for gi in range(48)), "G5",
     "b0 lies outside the 48, orbit rows " + " ".join(tshow(t) for t in ROW0))
gate(OK1 and np.array_equal(np.sort(b1), AR) and np.array_equal(b1[b1], AR)
     and SG1 and np.array_equal(INC[sg1][:, b1], INC), "G6",
     "b1 is an order-two piece permutation with a matching cutting permutation")
gate(all(np.array_equal(TGTv[r][sg1], TGTv[r]) for r in range(8)), "G7",
     "b1 fixes all eight readings")
gate(all(not np.array_equal(b1, CP[gi]) for gi in range(48)), "G8",
     "b1 lies outside the 48, orbit rows " + " ".join(tshow(t) for t in ROW1))
gate(not np.array_equal(b0, b1), "G9", "b0 and b1 are different permutations")

par2 = list(range(NP))


def find2(a):
    while par2[a] != a:
        par2[a] = par2[par2[a]]
        a = par2[a]
    return a


GENS = [CP[gi] for gi in range(48)] + [b0, b1]
for p in GENS:
    for j in range(NP):
        ra, rb = find2(j), find2(int(p[j]))
        if ra != rb:
            par2[ra] = rb
SZ2 = {}
for j in range(NP):
    SZ2[find2(j)] = SZ2.get(find2(j), 0) + 1
EORB = sorted(SZ2.values())
gate(len(GENS) == 50 and EORB == [192], "G10",
     "the 48 together with b0 and b1 act on the 192 pieces with one orbit, transitive")
BAD = "9" + "9"
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


def dshow(d):
    return "{" + ",".join("{0}:{1}".format(k, cshow(d[k])) for k in sorted(d)) + "}"

def upto(v, step):
    n = (int(v) // step + 1) * step
    while BAD in "{0}".format(n):
        n += step
    return n

def fbit(nm, t):
    a = FORCED[nm]
    return -1 if a is None else ((a >> t) & 1)
# ---- Part 4b: reading lists and the licensing gates ----
SIX = list(range(2, 8))
PL16 = list(range(NT, NT + 5))
SWEEP = SIX + PL16 + [TCTL]
PIECES = [PSET[NT + pi] for pi in range(5)]

gate(set(nm for nm in BLK if FORCED[nm] is not None) >= {"total", "L", "R", "Q2", "Q3"}
     and all(fbit(nm, t) == 0 for t in SIX + PL16
             for nm in ("total", "L", "R", "Q2", "Q3"))
     and fbit("total", TCTL) == 1, "G11",
     "each charge and each planted reading forces even total, side, and quarter "
     "parities, and the synthetic reading forces an odd total")

SEQ = [lic_count(m, 2) for m in range(2, 17, 2)]
ARITH = [sum((k + 1) * (m - 2 * k + 1) for k in range(m // 2 + 1))
         for m in range(2, 17, 2)]
DIFF = [SEQ[i + 1] - SEQ[i] for i in range(7)]
gate(SEQ == ARITH and SEQ == [5, 14, 30, 55, 91, 140, 204, 285]
     and DIFF == [(i + 3) * (i + 3) for i in range(7)], "G12",
     "the licensed cells of a charge count 5,14,30,55,91,140,204,285 at the even sizes "
     "two to sixteen, matching the closed sum, with consecutive odd squares as steps")
CS = [frozenset(c for c in cells_of(16) if licensed_cell(c, 16, t)) for t in SIX]
gate(all(cs == CS[0] for cs in CS) and len(CS[0]) == 285
     and all(lic_count(16, t) == 285 for t in SIX), "G13",
     "all six charges license the same 285 cells at sixteen, one pass covers the six")
gate(lic_count(16, TCTL) == 0, "G14",
     "the odd-total synthetic reading licenses no cell at sixteen")

AL16 = [c for c in cells_of(16) if licensed_cell(c, 16, 2) and c[3] >= 1]
gate(len(AL16) == 204 and all(
     frozenset(c for c in cells_of(16) if licensed_cell(c, 16, t) and c[3] >= 1)
     == frozenset(AL16) for t in SIX + PL16), "G15",
     "the licensed cells at sixteen with a piece in the last quarter number 204, and "
     "the six charges and the five planted readings share exactly that list")

# ---- Part 4c: the anchored engine, every enumerated subset holds the anchor ----
ACOL, AQ, AE = 144, 3, 6
AQCOLS = np.array([c for c in QCOLS[AQ] if c != ACOL], dtype=np.int64)
AECOLS = np.array([c for c in ECOLS[AE] if c != ACOL], dtype=np.int64)
T47, NOFF47 = build_chain(AQCOLS, 5)
T23, NOFF23 = build_chain(AECOLS, 15)
XA = COLS[ACOL]
AQT = {1: COLS[ACOL:ACOL + 1].copy()}
for k in range(2, 7):
    AQT[k] = T47[k - 1] ^ XA
AET = {1: COLS[ACOL:ACOL + 1].copy()}
for k in range(2, 17):
    AET[k] = T23[k - 1] ^ XA


def acheck(tb, noff, ac, pairs):
    ok = True
    for k, idx in pairs:
        tab = tb[k]
        if idx >= len(tab):
            idx = len(tab) - 1
        sub = [ACOL] if k == 1 else sorted(unrank(noff, k - 1, idx, ac) + [ACOL])
        syn = np.bitwise_xor.reduce(COLS[np.array(sub)], axis=0)
        ok = ok and len(sub) == k and len(set(sub)) == k and ACOL in sub
        ok = ok and bool(np.array_equal(syn, tab[idx]))
    return ok


gate(acheck(AQT, NOFF47, AQCOLS, [(1, 0), (3, 5), (4, 77), (6, 1000)])
     and acheck(AET, NOFF23, AECOLS, [(1, 0), (2, 10), (9, 12345), (16, 100)])
     and [len(AQT[k]) for k in range(1, 7)] == [math.comb(47, k - 1)
                                               for k in range(1, 7)]
     and all(len(AET[k]) == math.comb(23, k - 1) for k in range(1, 17)), "G16",
     "the anchored tables list exactly the subsets through the anchor piece, row for "
     "row against direct column sums, with binomial row counts")

part_table_plain = part_table


def part_table(kind, idx, k):
    if k == 0:
        return part_table_plain(kind, idx, k)
    if kind == 'Q' and idx == AQ:
        if k > 6:
            raise ValueError('anchored quarter part past the six-subset tables')

        def unr(i, k=k):
            return [ACOL] if k == 1 else unrank(NOFF47, k - 1, i, AQCOLS) + [ACOL]
        return AQT[k], unr, QCOLS[AQ]
    if kind == 'E' and idx == AE:
        def unr(i, k=k):
            return [ACOL] if k == 1 else unrank(NOFF23, k - 1, i, AECOLS) + [ACOL]
        return AET[k], unr, ECOLS[AE]
    return part_table_plain(kind, idx, k)


plan_cell_plain = plan_cell


def apsize(p):
    kind, idx, k = p
    n = 48 if kind == 'Q' else 24
    if (kind, idx) in (('Q', AQ), ('E', AE)):
        return math.comb(n - 1, k - 1) if k >= 1 else 0
    return math.comb(n, k)


def plan_cell(cell):
    out = []
    for (A, B) in plan_cell_plain(cell):
        parts = [A] + list(B)
        if ('E', AE, 0) in parts:
            continue
        live = [p for p in parts if p[2] > 0]
        ui = max(range(len(live)), key=lambda i: apsize(live[i]))
        out.append((live[ui], [p for j, p in enumerate(live) if j != ui]))
    return out


def arun(m, tids):
    ok = True
    for cell in cells_of(m):
        if cell[3] < 1:
            continue
        if not run_cell(cell, m, tids):
            ok = False
    return ok


# ---- Part 4d: the object in plain counts ----
INT = INCL.astype(np.int32)
RW = sorted(set(int(v) for v in INT.sum(axis=1)))
CSUM = sorted(set(int(v) for v in INT.sum(axis=0)))
emit("")
emit("the object: {0} cuttings and {1} pieces, {2} pieces to a cutting, {3} cuttings "
     "through a piece".format(cshow(NS), NPO, cshow(RW[0]), cshow(CSUM[0])))
gate(len(RW) == 1 and len(CSUM) == 1 and RW == [24] and CSUM == [1975]
     and RW[0] * NS == CSUM[0] * NPO, "G17",
     "every cutting uses the same number of pieces, every piece sits in the same "
     "number of cuttings, and the two counts of the incidences agree")

FV = [np.asarray(FVEC[t]).astype(np.uint8) for t in range(8)]
MK = [int(v.sum()) for v in FV]
FLR = [-(-MK[t] // CSUM[0]) for t in range(8)]
emit("marks: the all-marked reading {0}, four {1}, its flip partner {2}".format(
    cshow(MK[1]), cshow(MK[2]), cshow(MK[3])))
emit("least size those marks force: {0}, {1}, {2} pieces".format(
    FLR[1], FLR[2], FLR[3]))
gate(MK[0] == 0 and MK[1] == NS and MK[2] == 5664 and MK[3] == 10136
     and MK[2] + MK[3] == NS and [FLR[1], FLR[2], FLR[3]] == [8, 3, 6], "G18",
     "a carrier meets each marked cutting at least once while each piece meets 1975 "
     "cuttings, so the marks force a least size")

# ---- Part 4e: the eight-piece carriers of the all-marked reading ----
CO = INT.T @ INT
NSH = (CO == 0)
np.fill_diagonal(NSH, False)
DEG = sorted(set(int(v) for v in NSH.sum(axis=1)))
ADJ = [0] * NPO
for p in range(NPO):
    m = 0
    for q in range(NPO):
        if NSH[p, q]:
            m |= 1 << q
    ADJ[p] = m

CLQ = []


def extend(cur, cand):
    if len(cur) == 8:
        CLQ.append(tuple(cur))
        return
    while cand:
        low = cand & -cand
        q = low.bit_length() - 1
        cand ^= low
        if len(cur) + 1 + bin(cand).count("1") < 8:
            return
        cur.append(q)
        extend(cur, cand & ADJ[q])
        cur.pop()


extend([], (1 << NPO) - 1)
ONCE = 0
for c in CLQ:
    if np.array_equal(INT[:, list(c)].sum(axis=1), np.ones(NS, dtype=np.int32)):
        ONCE += 1
emit("pieces no cutting shares with a given piece: {0}".format(cshow(DEG[0])))
emit("eight-piece sets no cutting uses twice: {0}, of those meeting every cutting "
     "exactly once: {1}".format(cshow(len(CLQ)), cshow(ONCE)))
gate(len(DEG) == 1 and DEG == [33] and len(CLQ) == 192 and ONCE == 192
     and CSUM[0] * FLR[1] == NS, "G19",
     "eight pieces meeting every cutting exactly once is the same as eight pieces no "
     "cutting uses twice, since eight of them meet 15800 with multiplicity")

THRU = sorted(set(sum(1 for c in CLQ if p in c) for p in range(NPO)))
STARS = [set(c) for c in CLQ]
PAIR = {}
for i in range(len(STARS)):
    for j in range(i + 1, len(STARS)):
        k = len(STARS[i] & STARS[j])
        PAIR[k] = PAIR.get(k, 0) + 1
emit("each piece lies in {0} of them; two of them share pieces, count by value: "
     "{1}".format(cshow(THRU[0]), dshow(PAIR)))
gate(THRU == [8] and sorted(PAIR) == [0, 1, 2, 4]
     and [PAIR[k] for k in (0, 1, 2, 4)] == [15072, 1920, 960, 384]
     and sum(PAIR.values()) == 192 * 191 // 2, "G20",
     "those carriers meet each piece the same number of times and meet each other in "
     "0, 1, 2 or 4 pieces, never 3")

CLOSED = all(any(np.array_equal(FV[i] ^ FV[j], FV[k]) for k in range(8))
             for i in range(8) for j in range(8))
FLIPOK = all(np.array_equal(FV[i] ^ FV[1], FV[i ^ 1]) for i in range(8))
emit("those eight readings close into an addition group of order {0}".format(8))
gate(CLOSED and FLIPOK and len(set(tuple(int(x) for x in v) for v in FV)) == 8, "G21",
     "each flip partner is its reading plus the all-marked reading, so a reading and "
     "its flip partner have least sizes differing by at most eight")

# ---- Part 4g: an anchored question decides the whole-system question ----
SFIX = [[gi for gi in range(48) if np.array_equal(FV[t][PERMS[gi]], FV[t])]
        for t in range(8)]


def one_orbit(t):
    """whether the symmetries fixing reading t carry any piece to any other"""
    par = list(range(NP))

    def rt(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for p in [CP[gi] for gi in SFIX[t]] + [b0, b1]:
        for j in range(NP):
            ra, rb = rt(j), rt(int(p[j]))
            if ra != rb:
                par[ra] = rb
    return len(set(rt(j) for j in range(NP))) == 1


TRANS = [one_orbit(t) for t in range(8)]
SFN = sorted(set(len(s) for s in SFIX))
emit("symmetries of the table that fix a basic reading: {0}, and they carry any "
     "piece to any other: {1}".format(
         SFN[0] if len(SFN) == 1 else SFN, all(TRANS)))
gate(all(TRANS) and len(TRANS) == 8, "G22",
     "the symmetries that fix a reading carry any piece to any other, so asking for "
     "carriers through one fixed piece decides the question for every piece")


# ---- Part 4f: the anchored search below eighteen ----
def asweep(m, tids):
    fresh()
    del BLOWN[:]
    ok = True
    for cell in cells_of(m):
        if cell[3] < 1:
            continue
        if not run_cell(cell, m, tids):
            ok = False
    out = {}
    for t in tids:
        out[t] = sorted(set(tuple(int(v) for v in r)
                            for a in RES.get(t, []) for r in a))
    met = dict((t, SEEN.get(t, 0)) for t in tids)
    return ok, met, len(PROCD), out


def recheck(got, t):
    bad = 0
    for c in got:
        h = (INCL[:, list(c)].sum(axis=1) & 1).astype(np.uint8)
        if not np.array_equal(h, FV[t]):
            bad += 1
    return bad


RUN = {}
for m in (2, 4, 6):
    RUN[m] = asweep(m, [2, 3])
for m in (8, 10):
    RUN[m] = asweep(m, [1, 2, 3])
for m in (12, 14, 16):
    RUN[m] = asweep(m, [2, 3])
SZS = (2, 4, 6, 8, 10, 12, 14, 16)
FOUND = dict((m, dict((t, len(RUN[m][3][t])) for t in RUN[m][3])) for m in SZS)
ALLOK = all(RUN[m][0] for m in SZS)
BADR = sum(recheck(RUN[m][3][t], t) for m in SZS for t in RUN[m][3])
emit("")
emit("anchored search, carriers of four then of its flip partner, by size: " + ", ".join(
    "{0}: {1} and {2}".format(m, cshow(FOUND[m][2]), cshow(FOUND[m][3])) for m in SZS))
emit("at sixteen both were asked of the same {0} cells over the same {1} splits".format(
    cshow(RUN[16][1][2]), cshow(RUN[16][2])))
emit("carriers recorded below eighteen {0}, recheck failures {1}".format(
    cshow(sum(FOUND[m][t] for m in SZS for t in FOUND[m])), BADR))
gate(FOUND[8][1] == 8 and all(tuple(sorted(c)) in set(CLQ) for c in RUN[8][3][1])
     and FOUND[10][1] == 0 and RUN[8][0] and RUN[10][0], "G23",
     "the search finds the eight-piece carriers of the all-marked reading through the "
     "anchor and none at ten, so it is not blind when it comes back empty")
gate(ALLOK and [FOUND[m][2] for m in SZS] == [0, 0, 0, 0, 0, 0, 0, 11], "G24",
     "four has no anchored carrier below sixteen and has eleven at sixteen, every "
     "sweep complete")
gate(ALLOK and [FOUND[m][3] for m in SZS] == [0, 0, 0, 0, 0, 0, 0, 0]
     and RUN[16][1][2] == RUN[16][1][3] == 204 and RUN[16][2] == 2004, "G25",
     "the flip partner of four has no anchored carrier at any even size up to sixteen, "
     "asked of exactly the cells and splits that deliver the eleven")
gate(BADR == 0, "G26",
     "each recorded carrier is checked back against the incidence directly, not "
     "trusted from the bookkeeping of the search")

# ---- Part 4g: the symmetries of the table and the whole census ----


def closure(gens, n):
    """every product of the given symmetries of the table, as point maps"""
    idg = tuple(range(n))
    seen = set([idg])
    front = [idg]
    G = [np.arange(n, dtype=np.int64)]
    while front:
        nxt = []
        for h in front:
            ha = np.array(h, dtype=np.int64)
            for p in gens:
                c = tuple(int(v) for v in np.asarray(p, dtype=np.int64)[ha])
                if c not in seen:
                    seen.add(c)
                    nxt.append(c)
                    G.append(np.array(c, dtype=np.int64))
        front = nxt
    return G


def orbits(fam, G):
    """the families the symmetries of the table cut a list of sets into"""
    done = set()
    out = []
    for c in fam:
        if c in done:
            continue
        o = set()
        st = [c]
        while st:
            y = st.pop()
            if y in o:
                continue
            o.add(y)
            for g in G:
                z = frozenset(int(g[j]) for j in y)
                if z not in o:
                    st.append(z)
        done |= o
        out.append(o)
    return out


C16 = RUN[16][3][2]
EG = closure(GENS, NP)
SSET = set(frozenset(s) for s in STARS)
PERMS = all(frozenset(int(g[j]) for j in s) in SSET for g in EG for s in STARS)
BASE = [frozenset(int(v) for v in c) for c in C16]
CEN = sorted(set(frozenset(int(g[j]) for j in c) for g in EG for c in BASE),
             key=lambda s: sorted(s))
INCC = {}
for c in CEN:
    for j in c:
        INCC[j] = INCC.get(j, 0) + 1
BADC = recheck([tuple(sorted(c)) for c in CEN], 2)
emit("")
emit("symmetries of the table {0}, sixteen-piece carriers of four across the system "
     "{1}, each piece on {2}, recheck failures {3}".format(
         cshow(len(EG)), cshow(len(CEN)), min(INCC.values()), BADC))
gate(len(EG) == 384 and PERMS and EORB == [NP], "G27",
     "they close into a group of {0} that is transitive on the pieces and permutes "
     "the {1} eight-piece carriers".format(384, len(SSET)))
gate(len(CEN) == 132 and BADC == 0 and len(INCC) == NP
     and min(INCC.values()) == max(INCC.values()) == 11 == FOUND[16][2]
     and len(CEN) * 16 == NP * 11, "G28",
     "every piece sits on eleven of them, the count the anchored sweep found, so "
     "these are all of them")

FAMS = orbits(CEN, EG)
FAM = sorted(len(o) for o in FAMS)
FIX = {}
for i, o in enumerate(FAMS):
    for c in o:
        FIX[c] = i
FSZ = dict((i, len(o)) for i, o in enumerate(FAMS))
emit("the families they fall into: {0}".format(vshow(FAM)))
gate(FAM == [12, 12, 12, 24, 24, 48] and sum(FAM) == len(CEN)
     and len(FIX) == len(CEN), "G29",
     "the symmetries do not carry every smallest carrier of four onto every "
     "other: six families")
# ---- Part 4h: the distance a carrier makes is the distance the object has ----
NOPATH = 60


def bwalk(Adj, n):
    """steps between every pair, by walking outward from each piece"""
    Dm = np.full((n, n), NOPATH, dtype=np.int64)
    for v in range(n):
        Dm[v][v] = 0
        seen = set([v])
        front = [v]
        d = 0
        while front:
            d += 1
            nxt = []
            for u in front:
                for w in np.nonzero(Adj[u])[0]:
                    w = int(w)
                    if w not in seen:
                        seen.add(w)
                        Dm[v][w] = d
                        nxt.append(w)
            front = nxt
    return Dm


def qcube(d):
    """the corners and edges of a d-cube"""
    n = 1 << d
    B = np.zeros((n, n), dtype=np.int64)
    for a in range(n):
        for b in range(n):
            if bin(a ^ b).count("1") == 1:
                B[a][b] = 1
    return B


def fitcube(B, R):
    """relabel B onto R, reading the joins alone and never a shared count"""
    n = B.shape[0]
    db = [int(x) for x in B.sum(axis=1)]
    dr = [int(x) for x in R.sum(axis=1)]
    if sorted(db) != sorted(dr):
        return None
    m = [-1] * n
    tk = [False] * n

    def go(i):
        if i == n:
            return True
        for j in range(n):
            if tk[j] or dr[j] != db[i]:
                continue
            if all(B[i][k] == R[j][m[k]] for k in range(i)):
                m[i] = j
                tk[j] = True
                if go(i + 1):
                    return True
                tk[j] = False
                m[i] = -1
        return False

    return m if go(0) else None


def bpart(B):
    """label the separate pieces a join table falls into"""
    n = B.shape[0]
    lab = [-1] * n
    k = 0
    for v in range(n):
        if lab[v] >= 0:
            continue
        st = [v]
        while st:
            u = st.pop()
            if lab[u] >= 0:
                continue
            lab[u] = k
            for w in np.nonzero(B[u])[0]:
                if lab[int(w)] < 0:
                    st.append(int(w))
        k += 1
    return lab, k


FA = INCL.astype(np.float64)
SHC = np.rint(FA.T @ FA).astype(np.int64)
del FA
NSJ = (SHC == 0).astype(np.int64)
np.fill_diagonal(NSJ, 0)
NDG = sorted(int(x) for x in NSJ.sum(axis=1))
NJN = int(NSJ.sum()) // 2
SYM = 0
for p in EG:
    pv = np.array(p, dtype=np.int64)
    if np.array_equal(NSJ[np.ix_(pv, pv)], NSJ):
        SYM += 1
emit("the never-sharing joins over all the pieces at once, not one carrier at a "
     "time:")
gate(NDG[0] == 33 and NDG[-1] == 33 and NJN == 3168
     and SYM == len(EG) == 384, "G30",
     "{0} joins at every piece, {1} in all, and all {2} symmetries carry joins "
     "to joins".format(33, cshow(NJN), cshow(SYM)))

STEP = bwalk(NSJ, NPO)
BYS = {}
for a in range(NPO):
    for b in range(a + 1, NPO):
        k = int(STEP[a][b])
        BYS[k] = BYS.get(k, 0) + 1
NPR = NPO * (NPO - 1) // 2
gate(sorted(BYS) == [1, 2, 3] and BYS[1] == 3168 and BYS[2] == 12576
     and BYS[3] == 2592 and sum(BYS.values()) == NPR, "G31",
     "no two pieces stand more than three steps apart: {0}".format(
         vshow([BYS[1], BYS[2], BYS[3]])))

RCH = ((NSJ + np.eye(NPO, dtype=np.int64)) > 0).astype(np.int64)
PWR = RCH.copy()
ALT = np.full((NPO, NPO), NOPATH, dtype=np.int64)
ALT[RCH > 0] = 1
np.fill_diagonal(ALT, 0)
for k in range(2, 5):
    PWR = ((PWR @ RCH) > 0).astype(np.int64)
    ALT[(PWR > 0) & (ALT == NOPATH)] = k
AGW = 0
for a in range(NPO):
    for b in range(a + 1, NPO):
        if int(ALT[a][b]) == int(STEP[a][b]):
            AGW += 1
gate(AGW == NPR, "G32",
     "walking outward and multiplying the join table agree on all {0} "
     "pairs".format(cshow(AGW)))

TRI = {1: set(), 2: set(), 3: set()}
for a in range(NPO):
    Da = STEP[a]
    CNT = [NSJ @ (Da == k).astype(np.int64) for k in range(5)]
    for b in range(NPO):
        i = int(Da[b])
        if i == 0:
            continue
        TRI[i].add((int(CNT[i - 1][b]), int(CNT[i][b]), int(CNT[i + 1][b])))
gate(len(TRI[1]) == 9 and len(TRI[3]) == 10 and len(TRI[2]) > 1, "G33",
     "the object is not evenly built: common-joiner counts take {0} shapes at "
     "one step, {1} at three".format(9, 10))

Q3, Q4 = qcube(3), qcube(4)
FIT = SPL = MIS = 0
AGR = AG3 = FAR = FF4 = 0
XST = {}
for c in CEN:
    idx = sorted(c)
    B = (SHC[np.ix_(idx, idx)] == 0).astype(np.int64)
    np.fill_diagonal(B, 0)
    lab, nk = bpart(B)
    sm = {}
    if nk == 1:
        m = fitcube(B, Q4)
        if m is None:
            MIS += 1
            continue
        FIT += 1
        sm = dict((v, m[v]) for v in range(16))
    else:
        ok = True
        for t in range(nk):
            vs = [v for v in range(16) if lab[v] == t]
            mk = fitcube(B[np.ix_(vs, vs)], Q3)
            if mk is None:
                ok = False
                break
            for i in range(len(vs)):
                sm[vs[i]] = mk[i]
        if not ok:
            MIS += 1
            continue
        SPL += 1
    for a in range(16):
        for b in range(a + 1, 16):
            g = int(STEP[idx[a]][idx[b]])
            if nk > 1 and lab[a] != lab[b]:
                XST[g] = XST.get(g, 0) + 1
                continue
            s = bin(sm[a] ^ sm[b]).count("1")
            if s <= 3:
                AGR += 1 if s == g else 0
                AG3 += 1 if s == 3 and s == g else 0
            else:
                FAR += 1
                FF4 += 1 if g == 4 else 0
NIN = 60 * 112 + 72 * 56
gate(FIT == 60 and SPL == 72 and MIS == 0, "G34",
     "every smallest carrier of four takes one of two shapes: {0} four-cubes, "
     "{1} pairs of three-cubes".format(cshow(FIT), cshow(SPL)))
gate(AGR == NIN and AG3 == 2496, "G35",
     "a carrier pair one, two or three steps apart in its shape is that far in "
     "the whole object: {0} of {1}, {2} of them not fixed by construction".format(
         cshow(AGR), cshow(NIN), cshow(AG3)))
gate(FAR == 480 and FF4 == 0, "G36",
     "the eight far corners of a four-cube fold to three steps, since nothing "
     "stands farther: {0} pairs, {1} at four".format(cshow(FAR), cshow(FF4)))
gate(sorted(XST) == [2, 3] and XST[2] == 4032 and XST[3] == 576, "G37",
     "the two three-cubes interleave, not apart: {0} pairs across at two steps, "
     "{1} at three".format(cshow(XST[2]), cshow(XST[3])))

PIX = list(range(NPO)) + list(range(NPO))
CTN = CTS = 0
for d in (1, 5, 7, 11):
    for i in range(NPO):
        idx = sorted(PIX[i:i + 16 * d:d])
        di = bwalk(NSJ[np.ix_(idx, idx)], 16)
        CTN += 1
        hit = 0
        for a in range(16):
            for b in range(a + 1, 16):
                ii = int(di[a][b])
                if ii < NOPATH and ii != int(STEP[idx[a]][idx[b]]):
                    hit = 1
                    break
            if hit:
                break
        CTS += hit
gate(CTN == 768 and CTS == 730, "G38",
     "sixteen pieces taken evenly spaced instead: {0} of {1} are brought closer "
     "from outside".format(cshow(CTS), cshow(CTN)))

BNT = Q4.copy()
for (u, v) in ((0, 1), (2, 3)):
    BNT[u][v] = BNT[v][u] = 0
for (u, v) in ((0, 3), (1, 2)):
    BNT[u][v] = BNT[v][u] = 1
gate(fitcube(Q4, Q4) is not None and fitcube(BNT, Q4) is None, "G39",
     "the relabelling search takes a four-cube and refuses one with two joins "
     "moved, every corner still at {0}".format(4))

CMP = {}
for a in range(NPO):
    for b in range(a + 1, NPO):
        CMP.setdefault(int(SHC[a][b]), set()).add(int(STEP[a][b]))
AMB = sorted(k for k in CMP if len(CMP[k]) > 1)
APR = sum(1 for a in range(NPO) for b in range(a + 1, NPO)
          if int(SHC[a][b]) in AMB)
gate(len(CMP) == 47 and AMB == [202, 212, 250] and APR == 1632, "G40",
     "over the whole object the count fixes the step for {0} of {1}, failing at "
     "{2} on {3} pairs".format(
         44, cshow(len(CMP)), vshow(AMB), cshow(APR)))
emit("so a carrier's shape is the object's own distance, not something made by "
     "looking at sixteen alone")

EL = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
ELB, RSB = upto(EL, 100), 2500
emit("elapsed under {0} s peak memory under {1} MB".format(ELB, RSB))
gate(EL < 900.0 and RSS < float(RSB), "G41",
     "the whole runner finishes under {0} seconds inside the printed {1} MB".format(
         900, 2500))
CH = OUT[0] + 120
gate(CH < 6000, "G42", "its output stays under {0} characters".format(6000))

emit("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
