"""Cycle 741: the complete search at fourteen pieces.

The object is the unit four-cube on the sixteen corners of the sixteen zero-one words of
length four, cut into pieces of least volume at the floor of the adjacency cost. Its
15800 cuttings use 24 pieces each, drawn from 192 pieces in all, and a set of pieces
carries a reading when, on every cutting, the parity of how many of its pieces that
cutting uses reproduces the reading. Earlier cycles completed the search at every set of
at most eight pieces, at exactly ten and at exactly twelve and found none of the six
charge readings there, and the forced total parity of each charge bars every odd size.
This runner reproduces those sweeps and then completes the search at exactly fourteen
against eighteen readings: the constant zero, the constant one, the two sides of each of
the three charges, four planted controls, five planted fourteen-piece controls, and one
synthetic reading whose forced total parity is odd.

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
PSEED = 74100
P14SPEC = [("p14-7700", (7, 7, 0, 0)),
           ("p14-4442", (4, 4, 4, 2)),
           ("p14-2246", (2, 2, 4, 6)),
           ("p14-0248", (0, 2, 4, 8)),
           ("p14-0-0-2-12", (0, 0, 2, 12))]
prng2 = np.random.default_rng(PSEED)
PSET = {}
TNAME = [nm for nm, _f in TGT]
FVEC = [f for _nm, f in TGT]
for pi, (pnm, prof) in enumerate(P14SPEC):
    Sp = []
    for q in range(4):
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


# ------------------------------------------- Part 4: the certificate tree and the sweeps
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


def pshow(cols):
    """a piece index as quarter:offset, the block coordinates used throughout"""
    return ",".join("{0}:{1}".format(*divmod(int(c), 48)) for c in sorted(cols))


# ---- the incidence matrix, its rank, and the rows ----
CSUM = INCL.sum(axis=0)
SHAPE_OK = INC.shape == (15800, 192) and NS == 15800 and NPO == 192
CS_OK = bool((CSUM == 1975).all()) and (1975 & 1) == 1
NKER = NPO - ERANK
NDIST = len(set(EROW))
emit("INC {0}x{1} colsum {2} rank {3} kernel {4} rows-distinct {5}".format(
    NS, NPO, 1975, ERANK, NKER, NDIST))
gate(SHAPE_OK, "G01", "the cuttings of least cost form a {0} by {1} table over the two "
     "element field".format(NS, NPO))
gate(CS_OK, "G02", "every one of the {0} pieces is used by exactly {1} cuttings, an odd "
     "count".format(NPO, 1975))
gate(ERANK == 88 and NKER == 104, "G03",
     "that table has rank {0} and kernel dimension {1}".format(ERANK, NKER))
gate(NDIST == NS, "G04", "the {0} cuttings are pairwise distinct as piece sets".format(NS))

# ---- which blocks carry a forced parity ----
FNAMES = sorted(nm for nm in BLK if FORCED[nm] is not None)
UNAMES = sorted(nm for nm in BLK if FORCED[nm] is None)
NR = NTG - 1


def fbit(nm, t):
    a = FORCED[nm]
    return -1 if a is None else ((a >> t) & 1)


def parvec(nm):
    return [fbit(nm, t) for t in range(NR)]


ZR = [0] * NR
QPAT12 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
Q2V, Q3V = parvec("Q2"), parvec("Q3")
emit("forced " + ",".join(FNAMES) + " free " + ",".join(UNAMES))
emit("Q2 parity t0-11 " + vshow(Q2V[:12]) + " planted " + vshow(Q2V[12:])
     + " odd-ctl total " + "{0}".format(fbit("total", TCTL)))
gate(FNAMES == ["L", "Q2", "Q3", "R", "total"]
     and UNAMES == ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "Q0", "Q1"]
     and len(BLK) == 15, "G05",
     "of the 15 block indicators exactly the whole set, its halves and the two "
     "quarters of the second half lie in the row space")
gate(Q2V[:12] == QPAT12 and Q3V[:12] == QPAT12 and Q2V == Q3V
     and parvec("total") == ZR and parvec("L") == ZR and parvec("R") == ZR
     and fbit("total", TCTL) == 1, "G06",
     "those quarters force the printed parity vector on the first twelve readings; "
     "the whole and its halves force even; the synthetic reading forces an odd whole")

PROFOK = []
for pi, (pnm, prof) in enumerate(P14SPEC):
    t = NT + pi
    expp = (sum(prof) & 1, (prof[0] + prof[1]) & 1, prof[2] & 1, prof[3] & 1)
    gotp = tuple(fbit(nm, t) for nm in ("total", "L", "Q2", "Q3"))
    PROFOK.append(gotp == expp)
gate(all(PROFOK) and len(PROFOK) == 5, "G07",
     "each planted fourteen piece reading forces exactly the whole, half and quarter "
     "parities its own profile has")


# ---- the kernel subcode inside the first quarter, enumerated apart from any search ----
def subwords(ker):
    n = len(ker)
    syn = np.zeros((1 << n, 2), dtype=np.uint64)
    msk = [0] * (1 << n)
    wts = np.zeros(1 << n, dtype=np.int64)
    bsy = []
    for b in ker:
        s = np.zeros(2, dtype=np.uint64)
        for a in range(64):
            if (b >> a) & 1:
                s = s ^ COLS[a]
        bsy.append(s)
    for mm in range(1, 1 << n):
        lo = mm & (-mm)
        i = lo.bit_length() - 1
        p = mm ^ lo
        msk[mm] = msk[p] ^ ker[i]
        syn[mm] = syn[p] ^ bsy[i]
        wts[mm] = bin(msk[mm]).count("1")
    return msk, syn, wts


def wdist(wts):
    d = {}
    for w in wts.tolist():
        d[w] = d.get(w, 0) + 1
    return d


def cols_of(m):
    return tuple(a for a in range(48) if (m >> a) & 1)


K0 = sub_kernel(QCOLS[0])
M0, S0, W0 = subwords(K0)
D0 = wdist(W0)
MINW0 = min(w for w in D0 if w > 0)
NW8, NW12, NW14 = D0.get(8, 0), D0.get(12, 0), D0.get(14, 0)
emit("Q0 subcode dim {0} words {1} minwt {2} at8 {3} at12 {4} at14 {5}".format(
    len(K0), 1 << len(K0), MINW0, cshow(NW8), cshow(NW12), cshow(NW14)))
gate(len(K0) == 14 and (1 << len(K0)) == 16384 and not bool(S0.any()), "G08",
     "the sets inside the first quarter met evenly by every cutting form a space of "
     "dimension {0}, all {1} words verified".format(len(K0), 1 << len(K0)))
gate(MINW0 == 8 and NW8 == 30 and NW12 == 63, "G09",
     "its least nonzero weight is {0}, with {1} words there and {2} at weight "
     "12".format(MINW0, NW8, NW12))

PIECES = [PSET[NT + pi] for pi in range(5)]
PROF = []
PRNM = []
for pi, (pnm, prof) in enumerate(P14SPEC):
    S = PIECES[pi]
    got = tuple(sum(1 for c in S if 48 * q <= c < 48 * q + 48) for q in range(4))
    PROF.append(got == prof and len(set(S)) == 14)
    PRNM.append("-".join("{0}".format(x) for x in prof))
emit("planted seed {0} profiles ".format(PSEED) + " ".join(PRNM))
gate(all(PROF) and len(PROF) == 5, "G10",
     "the five planted readings are fourteen distinct pieces each, drawn to the five "
     "quarter profiles their names carry")

# ---- which readings the table can carry at all, measured apart from the search ----
CBAS = {}
for a in range(NPO):
    x = int.from_bytes(np.packbits(INC[:, a], bitorder="little").tobytes(), "little")
    while x:
        h = x.bit_length() - 1
        if h not in CBAS:
            CBAS[h] = x
            break
        x ^= CBAS[h]
ACH = []
for t in range(NTG):
    x = int.from_bytes(np.packbits(FV[t], bitorder="little").tobytes(), "little")
    while x:
        h = x.bit_length() - 1
        if h not in CBAS:
            break
        x ^= CBAS[h]
    ACH.append(x == 0)
emit("in-column-space " + vshow([1 if a else 0 for a in ACH]))
gate(len(CBAS) == ERANK and all(ACH[:TCTL]) and not ACH[TCTL], "G11",
     "all but the synthetic reading lie in the column space, so each of the six "
     "charges is carried by some set")

# ---- licensed cells, by direct enumeration and by the square continuation ----
SIZES = (2, 4, 6, 8, 10, 12, 14)
ALLEV = [lic_count(m, 0) for m in SIZES]
ALLOD = [lic_count(m, 8) for m in SIZES]
DIFE = [ALLEV[i + 1] - ALLEV[i] for i in range(6)]
DIFO = [ALLOD[i + 1] - ALLOD[i] for i in range(6)]
SQ = [(k + 3) * (k + 3) for k in range(6)]
CONTE = ALLEV[5] + SQ[5]
CONTO = ALLOD[5] + SQ[4]
emit("licensed even " + vshow(ALLEV) + " diffs " + vshow(DIFE))
emit("licensed odd-quarter " + vshow(ALLOD) + " diffs " + vshow(DIFO))
gate(ALLEV[:6] == [5, 14, 30, 55, 91, 140] and DIFE[:5] == SQ[:5]
     and ALLOD[:6] == [1, 5, 14, 30, 55, 91], "G12",
     "the cells an even reading licenses at sizes 2 to 12 are {0} with square "
     "differences {1}, reproducing an earlier cycle".format(ALLEV[:6], SQ[:5]))
gate(ALLEV[6] == CONTE and ALLOD[6] == CONTO and CONTE > 0, "G13",
     "at fourteen the count {0} for an even reading equals the continuation "
     "{1} plus the next square {2}, and {3} for an odd quarter "
     "reading equals {4} plus {5}".format(ALLEV[6], ALLEV[5], SQ[5],
                                          ALLOD[6], ALLOD[5], SQ[4]))
gate(lic_count(14, TCTL) == 0 and lic_count(12, TCTL) == 0, "G14",
     "the synthetic reading, whose forced whole is odd, licenses no cell at fourteen")

TIDS = list(range(NTG))
SIX = list(range(2, 8))
PLT = list(range(NT, NT + 5))

# ---- sweep one: every set of at most eight pieces ----
fresh()
for msz in range(1, 9):
    run_sweep(msz, TIDS)
C8 = [CNT.get(t, 0) for t in TIDS]
V8 = verify(TIDS)
O8Z, N8Z, CL8Z = orbsum(0)
O8O, N8O, CL8O = orbsum(1)
W8OK = sum(1 for m in M0 if bin(m).count("1") == 8 and has_set(0, cols_of(m)))
emit("m<=8 counts " + vshow(C8) + " verify " + vshow(V8))
emit("m<=8 orbits zero " + cshow(N8Z) + " " + dshow(O8Z) + " one " + cshow(N8O)
     + " " + dshow(O8O))
gate(C8[0] == 648 and C8[1] == 192 and V8[1] == 0 and V8[2] == 0
     and V8[0] == sum(C8), "G15",
     "a complete search of every set of at most eight pieces finds {0} carrying the "
     "constant zero reading and {1} the constant one reading, all {2} "
     "recorded sets verified".format(C8[0], C8[1], V8[0]))
gate(all(C8[t] == 0 for t in SIX) and C8[TCTL] == 0, "G16",
     "no set of eight or fewer carries either side of any charge, or the synthetic odd "
     "reading")
gate(N8Z == 22 and O8Z == {24: 17, 48: 5} and CL8Z and N8O == 5
     and O8O == {24: 2, 48: 3} and CL8O, "G17",
     "the {0} zero-reading sets fall into {1} orbits of the symmetries, 17 of "
     "size 24 and 5 of size 48, and the {2} one-reading sets into {3} orbits, 2 of "
     "size 24 and 3 of size 48".format(C8[0], N8Z, C8[1], N8O))
gate(W8OK == NW8 and NW8 <= C8[0], "G18",
     "all {0} weight 8 words of the quarter subcode, enumerated apart from it, "
     "are among those {1}".format(W8OK, C8[0]))

# ---- sweep two: every set of exactly ten pieces ----
fresh()
run_sweep(10, TIDS)
C10 = [CNT.get(t, 0) for t in TIDS]
V10 = verify(TIDS)
emit("m=10 counts " + vshow(C10) + " verify " + vshow(V10))
gate(C10[:12] == [0, 0, 0, 0, 0, 0, 0, 0, 108, 1, 2, 0] and C10[TCTL] == 0
     and V10[1] == 0 and V10[2] == 0 and V10[0] == sum(C10)
     and lic_count(10, TCTL) == 0, "G19",
     "a complete search at ten reproduces an earlier cycle on the twelve readings it "
     "shares: {0}, the synthetic reading licensing no cell".format(C10[:12]))

# ---- sweep three: every set of exactly twelve pieces ----
fresh()
OK12 = run_sweep(12, TIDS)
C12 = [CNT.get(t, 0) for t in TIDS]
V12 = verify(TIDS)
COV12, NSPL12, NDS12 = coverage(12, TIDS)
LIC12 = [lic_count(12, t) for t in TIDS]
W12OK = sum(1 for m in M0 if bin(m).count("1") == 12 and has_set(0, cols_of(m)))
emit("m=12 counts " + vshow(C12) + " verify " + vshow(V12) + " splits " + cshow(NSPL12))
gate(C12[:12] == [7808, 3072, 0, 0, 0, 0, 0, 0, 661, 25, 38, 38] and C12[TCTL] == 0,
     "G20", "a complete search at twelve reproduces an earlier cycle on the twelve "
     "readings it shares: {0}, and finds no synthetic set".format(C12[:12]))
gate(COV12 == LIC12 and NSPL12 == NDS12 and NSPL12 > 0 and LIC12[0] == 140
     and LIC12[8] == 91, "G21",
     "every licensed cell at twelve is met once per reading, {0} per even and {1} per "
     "odd quarter reading, its {2} splits distinct".format(
         LIC12[0], LIC12[8], NSPL12))
gate(V12[1] == 0 and V12[2] == 0 and V12[0] == sum(min(c, CAP) for c in C12), "G22",
     "all {0} recorded sets at twelve recompute to their own reading, have weight 12, "
     "and are distinct".format(V12[0]))
gate(W12OK == NW12 and NW12 <= C12[0], "G23",
     "all {0} weight 12 words of the quarter subcode are among the {1} sets carrying "
     "the zero reading at twelve".format(W12OK, C12[0]))

# ---- the first quarter on its own at fourteen, against the enumerated subcode ----
fresh()
OKQ = run_cell((14, 0, 0, 0), 14, [0])
CQ = CNT.get(0, 0)
VQ = verify([0])
WQOK = sum(1 for m in M0 if bin(m).count("1") == 14 and has_set(0, cols_of(m)))
emit("first-quarter-14 found " + cshow(CQ) + " subcode " + cshow(NW14)
     + " verify " + vshow(VQ))
gate(OKQ and CQ == NW14 and WQOK == NW14 and VQ[1] == 0 and VQ[2] == 0
     and VQ[0] == CQ, "G24",
     "the complete search of the first quarter alone at fourteen returns the "
     "{0} weight 14 words of its subcode, enumerated apart from the search".format(
         NW14))

# ---- sweep four: every set of exactly fourteen pieces ----
fresh()
OK14 = run_sweep(14, TIDS)
C14 = [CNT.get(t, 0) for t in TIDS]
V14 = verify(TIDS)
COV14, NSPL14, NDS14 = coverage(14, TIDS)
LIC14 = [lic_count(14, t) for t in TIDS]
PREC = [has_set(NT + pi, PIECES[pi]) for pi in range(5)]
ORB14 = {}
CL14 = True
for t in TIDS:
    if C14[t] and C14[t] <= CAP and len(STAB[t]) > 1:
        d, nb, cl = orbsum(t)
        ORB14[t] = (d, nb)
        CL14 = CL14 and cl
DIV14 = all((48 // s) * s == 48 for t in ORB14 for s in ORB14[t][0])
SNG = [t for t in TIDS if C14[t] and len(STAB[t]) == 1]
emit("m=14 counts " + vshow(C14))
emit("m=14 licensed " + vshow(LIC14))
emit("m=14 verify " + vshow(V14) + " splits " + cshow(NSPL14) + " cells "
     + cshow(sum(1 for c in cells_of(14) if any(licensed_cell(c, 14, t) for t in TIDS))))
for t in sorted(ORB14):
    emit("m=14 orbits {0} {1} {2}".format(TNAME[t], cshow(ORB14[t][1]),
                                          dshow(ORB14[t][0])))
emit("m=14 orbits all of size 1 for readings " + vshow(SNG))
gate(COV14 == LIC14 and NSPL14 == NDS14 and NSPL14 > 0, "G25",
     "every licensed cell at fourteen is met once per reading, {0} per even and {1} "
     "per odd quarter reading, its {2} splits distinct".format(
         LIC14[0], LIC14[8], NSPL14))
gate(OK14 and OKQ and OK12 and not BLOWN, "G26",
     "no intermediate or final table in any of the searches reached the cap of {0} "
     "entries".format(TABCAP))
gate(V14[1] == 0 and V14[2] == 0 and V14[0] == sum(min(c, CAP) for c in C14), "G27",
     "all {0} recorded sets at fourteen recompute to their own reading, have weight "
     "14, and are distinct".format(V14[0]))
gate(all(PREC) and len(PREC) == 5, "G28",
     "each of the five planted fourteen piece sets is found by a search blind to it, "
     "including the two whose profile cuts one quarter and the one that cuts two")
gate(CL14 and DIV14 and len(ORB14) + len(SNG) == sum(1 for c in C14 if c), "G29",
     "the sets found at fourteen fall into orbits of the symmetries that fix their "
     "reading, of sizes dividing 48")
gate(C14[TCTL] == 0 and C10[TCTL] == 0 and C12[TCTL] == 0 and C8[TCTL] == 0, "G30",
     "the synthetic reading outside the column space is carried by no set at any size "
     "searched")

gate(all(C14[t] == 0 for t in SIX), "G31",
     "neither side of any of the three charges is carried by any set of exactly "
     "fourteen pieces")
gate(all(C8[t] == 0 for t in SIX) and all(C10[t] == 0 for t in SIX)
     and all(C12[t] == 0 for t in SIX) and all(C14[t] == 0 for t in SIX)
     and all(fbit("total", t) == 0 for t in SIX), "G32",
     "the searches at every even size to fourteen are complete and empty for the six, "
     "and each forces an even total, barring every odd size: the six charges need at "
     "least sixteen pieces")

EL = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
ELB, RSB = upto(EL, 500), 2500
emit("elapsed under {0} s peak memory under {1} MB".format(ELB, RSB))
gate(EL < 900.0 and RSS < float(RSB), "G33",
     "the whole runner finishes under {0} seconds inside the printed {1} MB".format(
         900, 2500))
CH = OUT[0] + 120
gate(CH < 5500, "G34", "its output stays under {0} characters".format(5500))

emit("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
