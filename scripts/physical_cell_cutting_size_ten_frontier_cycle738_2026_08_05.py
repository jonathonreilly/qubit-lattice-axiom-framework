"""Cycle 738: the size-ten frontier for readings in a supplied finite cutting model.

The single cell is the unit four-cube with three lattice directions and one tick. Its
least-volume cuttings at the floor of the supplied four-coordinate L1-pair cost carry eight readings of the
population: the constant zero, the constant one, and the two sides of each of three
nonconstant algebraic readings. A set of pieces carries a reading when, on every cutting, the parity of how many
of its pieces that cutting uses reproduces the reading. The previous cycle searched every
set of at most eight pieces; this runner completes the next even size. It rebuilds the
cuttings and the block parities any search of them is forced to respect, reproduces the
answer at every even size up to eight as a known-answer check, and then searches every
set of exactly ten
pieces against eighteen readings: the eight above, four planted controls of four and
eight pieces, five planted ten-piece controls, and one synthetic reading whose forced
total parity is odd, which no set of an even size can carry.

The named readings are algebraic functions induced by Cycle 737; this runner makes no
physical identification.  Class-A: integer and field-with-two-elements arithmetic on a
finite explicit object, no solver. Every count below is measured here.
"""
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

PF = [0, 0]
GATES = []
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md"
INDEPENDENT_PATH = (
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_independent_check_2026_08_05.py"
)
C737_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md"
C737_PRIMARY_PATH = "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py"
C737_CHECKER_PATH = (
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05.py"
)
C737_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05_"
    "receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    NOTE_PATH,
    INDEPENDENT_PATH,
)
AUDIT_TIMEOUT_SEC = 900


def file_sha256(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


C737_RECEIPT = json.loads((ROOT / C737_RECEIPT_PATH).read_text(encoding="utf-8"))


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    GATES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


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

gate(len(SUB) == 4368 and NPIECE == 2672 and NQ == 2736 and coll == 0 and face == 0
     and np.array_equal(MM @ IV, np.broadcast_to(np.eye(4, dtype=np.int64), MM.shape))
     and CB == 3 and SB == 12810 and len(G) == 48 and NORB == 57, "base.cell",
     "{0} five-subsets of the 16 corners give {1} pieces of least volume, carrying {2} "
     "sample points with no collision and {3} on a boundary; the cell has {4} "
     "symmetries".format(len(SUB), NPIECE, NQ, face, len(G)))

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
gate(LO == 6 and len(MINP) == 400 and NODE[0] == 502838 and NS == 15800
     and FULL == set([24]) and NPO == 192, "base.floor",
     "a complete search over the {0} pieces of least cost {1} visits {2} nodes and finds "
     "{3} cuttings of {4} pieces each, between them using {5} pieces".format(
         len(MINP), LO, NODE[0], NS, 24, NPO))

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
SZC = [4, 5, 6, 7, 8, 9, 10]
SZG = [4, 6, 7, 8, 9, 10]
EA = dict((k, []) for k in SZC)
EB = dict((k, []) for k in SZC)
DIS = dict((k, set()) for k in SZG)
for lo in range(0, NS, 100):
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
gate(CPOK and len(CP) == 48 and NORB == 4 and OSZ == [48, 48, 48, 48], "base.cols",
     "each of the {0} symmetries permutes the {1} used pieces in step with its action on "
     "the {2} cuttings; the pieces fall into {3} orbits of {4}".format(
         len(CP), NPO, NS, NORB, OSZ[0]))

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

# ---- row basis, packed syndromes ----
piv = {}
I88 = []
for i in range(NS):
    r = BITS[i]
    while r:
        h = r.bit_length() - 1
        if h not in piv:
            piv[h] = r
            I88.append(i)
            break
        r ^= piv[h]
I88 = np.array(I88, dtype=np.int64)
SUBI = INC[I88].astype(np.uint64)
slo = np.zeros(NPO, dtype=np.uint64)
shi = np.zeros(NPO, dtype=np.uint64)
for j in range(len(I88)):
    if j < 64:
        slo ^= SUBI[j] << np.uint64(j)
    else:
        shi ^= SUBI[j] << np.uint64(j - 64)


def packf(f):
    v = f[I88].astype(np.uint64)
    lo, hi = np.uint64(0), np.uint64(0)
    for j in range(len(I88)):
        if j < 64:
            lo ^= v[j] << np.uint64(j)
        else:
            hi ^= v[j] << np.uint64(j - 64)
    return lo, hi


TS = [packf(f) for _, f in TGT]

# ------------------------------------------- Part 2: parity and license certificates

csum = INC.sum(axis=0)
gate(int(csum.min()) == 1975 and int(csum.max()) == 1975 and (1975 & 1) == 1,
     "par.colsum",
     "every one of the {0} pieces is used by {1} of the {2} cuttings, an odd count".format(
         NPO, int(csum.min()), NS))

ONES = [int(TGT[t][1].sum()) for t in range(8)]
gate(ONES == [0, 15800, 5664, 10136, 7704, 8096, 7424, 8376]
     and all((v & 1) == 0 for v in ONES), "par.ones",
     "zero, one, four, four-flip, six, six-flip, seven and seven-flip hold on {0}, {1}, "
     "{2}, {3}, {4}, {5}, {6} and {7} cuttings, every count even".format(*ONES))

CTUP = [[int(corner) for corner in UNI[piece]] for piece in USED]
READING_IDENTITY = C737_RECEIPT.get("reading_identity", {})
FUNCTION_IDENTITY = READING_IDENTITY.get("functions", {})
EXPECTED_NAMES = ["zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip"]
IDENTITY_OK = (
    C737_RECEIPT.get("schema") == "physical-cell-cutting-least-computing-sets-cycle737-v2"
    and C737_RECEIPT.get("status") == "pass"
    and C737_RECEIPT.get("gates", {}).get("fail") == 0
    and C737_RECEIPT.get("complete_support_sweep", {}).get("maximum_cardinality") == 8
    and C737_RECEIPT.get("complete_support_sweep", {}).get(
        "nonconstant_reading_minimum_lower_bound"
    ) == 10
    and READING_IDENTITY.get("incidence_packbits_sha256")
    == hashlib.sha256(np.packbits(INC, axis=1).tobytes()).hexdigest()
    and READING_IDENTITY.get("support_column_order_sha256")
    == hashlib.sha256(json.dumps(CTUP, separators=(",", ":")).encode("utf-8")).hexdigest()
)
EXPECTED_WITNESS_SIZES = {
    "four": 16,
    "four-flip": 20,
    "six": 24,
    "six-flip": 24,
    "seven": 30,
    "seven-flip": 30,
}
for name, expected_size in EXPECTED_WITNESS_SIZES.items():
    witness = C737_RECEIPT.get("verified_upper_witnesses", {}).get(name, {})
    support = witness.get("support_indices_0_to_191", [])
    corner_support = witness.get("support_corner_tuples", [])
    IDENTITY_OK = IDENTITY_OK and witness.get("size") == expected_size
    IDENTITY_OK = IDENTITY_OK and len(support) == expected_size == len(corner_support)
    IDENTITY_OK = IDENTITY_OK and all(
        CTUP[index] == corners for index, corners in zip(support, corner_support)
    )
for name, (_target_name, function) in zip(EXPECTED_NAMES, TGT[:8]):
    metadata = FUNCTION_IDENTITY.get(name, {})
    IDENTITY_OK = IDENTITY_OK and metadata.get("ones") == int(function.sum())
    IDENTITY_OK = IDENTITY_OK and metadata.get("packbits_sha256") == hashlib.sha256(
        np.packbits(function).tobytes()
    ).hexdigest()
gate(IDENTITY_OK, "dep.c737",
     "Cycle 737 v2 is pass and binds the exact 15,800-row incidence, piece order, eight "
     "reading functions, and lower-bound-10 predecessor result")

FB = []
for i in range(NS):
    fb = 0
    for t in range(NT):
        fb |= int(TGT[t][1][i]) << t
    FB.append(fb)
piv2 = {}
for i in range(NS):
    r, fb = BITS[i], FB[i]
    while r:
        h = r.bit_length() - 1
        if h in piv2:
            pr, pf = piv2[h]
            r ^= pr
            fb ^= pf
        else:
            piv2[h] = (r, fb)
            break


def member(tint):
    """None if the functional is outside the rowspace; else forced-parity bits."""
    r, fb = tint, 0
    while r:
        h = r.bit_length() - 1
        if h not in piv2:
            return None
        pr, pf = piv2[h]
        r ^= pr
        fb ^= pf
    return fb


gate(len(I88) == 88 and len(piv2) == 88, "base.rank",
     "the {0} cuttings span {1} dimensions over the field with two elements".format(
         NS, len(I88)))

LH = (1 << 96) - 1
FULL = (1 << NPO) - 1
QUART = [((1 << 48) - 1) << (48 * k) for k in range(4)]
mA = member(FULL)
mL = member(LH)
mQ2 = member(QUART[2])
mQ3 = member(QUART[3])
gate(mA is not None and (mA & 255) == 0, "lic.full",
     "the forced parity of the all-pieces indicator against the eight readings is "
     "{0}".format(tuple((mA >> t) & 1 for t in range(8))))
gate(mL is not None and mQ2 is not None and mQ3 is not None
     and (mL & 255) == 0 and (mQ2 & 255) == 0 and (mQ3 & 255) == 0, "lic.half",
     "the left half {0}, pieces 96 to 143 {1} and pieces 144 to 191 {2}: each lies in the "
     "row space with all eight forced parities 0".format(
         mL & 255, mQ2 & 255, mQ3 & 255))
gate(member(QUART[0]) is None and member(QUART[1]) is None, "lic.quart",
     "the indicators of pieces 0 to 47 and of pieces 48 to 95 lie outside the row space, "
     "so an odd split inside a half is not licensed")
orb_out = []
for j in range(NORB):
    tint = 0
    for c in np.flatnonzero(lab == j).tolist():
        tint |= 1 << c
    orb_out.append(member(tint) is None)
gate(orb_out == [True] * NORB, "lic.orb",
     "the indicator of each of the {0} orbits of {1} pieces lies outside the row space: "
     "{2}".format(NORB, OSZ[0], orb_out))
gate(((mL >> 8) & 15) == 0, "lic.plant",
     "each of the 4 planted targets also has forced left-half parity 0, so the even-split "
     "sweep covers them too")

wodd = [5, 17, 60, 130]
fodd = (INCL[:, wodd].sum(axis=1) & 1).astype(np.uint8)
FBo = []
for i in range(NS):
    FBo.append(int(fodd[i]))
piv3 = {}
for i in range(NS):
    r, fb = BITS[i], FBo[i]
    while r:
        h = r.bit_length() - 1
        if h in piv3:
            pr, pf = piv3[h]
            r ^= pr
            fb ^= pf
        else:
            piv3[h] = (r, fb)
            break
r, fb = LH, 0
while r:
    h = r.bit_length() - 1
    pr, pf = piv3[h]
    r ^= pr
    fb ^= pf
gate(fb == 1, "lic.ctrl",
     "a synthetic reading built from pieces {0}, {1}, {2} and {3} has forced left-half "
     "parity {4}, so the license test can fail".format(
         wodd[0], wodd[1], wodd[2], wodd[3], fb))

# ---------------------------------- smoke stop: the construction and its certificates

if len(sys.argv) > 1 and sys.argv[1] == "smoke":
    print("")
    print("SMOKE OK: PASS={0} FAIL={1}".format(PF[0], PF[1]))
    raise SystemExit(1 if PF[1] else 0)

# ------------------------------------ Part 3: the engine for the size-ten search
# A set of pieces is split by quarter into a cell (q0, q1, q2, q3). Each quarter's
# subsets are enumerated by a lex extension chain; the cell is searched by meeting the
# stored quarters against the streamed ones on the 88 independent cutting parities.

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

prng1 = np.random.default_rng(738)
PKOK = ERANK == 88
for _ in range(20):
    Ssmp = prng1.choice(NPO, 10, replace=False)
    direct = pack88((INC[:, Ssmp].sum(axis=1) & 1)[EPIV])
    xk = np.zeros(2, dtype=np.uint64)
    for j in Ssmp:
        xk ^= COLS[j]
    PKOK = PKOK and bool(np.array_equal(xk, direct))

# ---- the eighteen readings: the twelve of Part 1, five planted ten-sets, one control ----
P10SPEC = [("p10-2233", (2, 2, 3, 3)),
           ("p10-1144", (1, 1, 4, 4)),
           ("p10-4411", (4, 4, 1, 1)),
           ("p10-5500", (5, 5, 0, 0)),
           ("p10-0019", (0, 0, 1, 9))]
prng2 = np.random.default_rng(73800)
P10 = {}
TNAME = [nm for nm, _f in TGT]
FVEC = [f for _nm, f in TGT]
for pi, (pnm, prof) in enumerate(P10SPEC):
    Sp = []
    for q in range(4):
        Sp += [48 * q + int(c) for c in prng2.choice(48, prof[q], replace=False)]
    Sp = sorted(Sp)
    P10[NT + pi] = frozenset(Sp)
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


# ---- the stored side of a meeting, with a bitmap in front of every probe ----
class Store:
    def __init__(self, k0, k1, pay):
        idx = np.argsort(k0, kind="stable")
        self.k0 = np.ascontiguousarray(k0[idx])
        self.k1 = np.ascontiguousarray(k1[idx])
        self.pay = np.ascontiguousarray(pay[idx])
        self.bmp = np.zeros(2**BQ, dtype=np.uint8)
        self.bmp[(self.k0 & MQ).astype(np.int64)] = 1

    def probe(self, x0, x1, out):
        """Collect (stream_pos, store_pay) exact matches into out."""
        g = self.bmp[(x0 & MQ).astype(np.int64)]
        pos = np.nonzero(g)[0]
        if not len(pos):
            return
        s0 = x0[pos]
        lo = np.searchsorted(self.k0, s0, side="left")
        hi = np.searchsorted(self.k0, s0, side="right")
        sel = np.nonzero(hi > lo)[0]
        for si in sel:
            p = int(pos[si])
            for qq in range(int(lo[si]), int(hi[si])):
                if self.k1[qq] == x1[p] and self.k0[qq] == x0[p]:
                    out.append((p, int(self.pay[qq])))


def product_keys(tabs):
    """XOR-product of block tables (row-major over tabs order). Returns (n, keys)."""
    n = 1
    for t in tabs:
        n *= len(t)
    acc = np.zeros((n, 2), dtype=np.uint64)
    tile = n
    for tab in tabs:
        s = len(tab)
        tile //= s
        base = np.arange(n) // tile
        rows = base - (base // s) * s
        acc ^= tab[rows]
    return n, acc


def product_store(tabs, tids, folded):
    """Store over the XOR-product of tabs; folded -> keys ^= TG[t] per target."""
    n, acc = product_keys(tabs)
    if folded:
        nt = len(tids)
        k0 = np.empty(n * nt, dtype=np.uint64)
        k1 = np.empty(n * nt, dtype=np.uint64)
        pay = np.empty(n * nt, dtype=np.int64)
        for a, t in enumerate(tids):
            k0[a * n:(a + 1) * n] = acc[:, 0] ^ TG[t, 0]
            k1[a * n:(a + 1) * n] = acc[:, 1] ^ TG[t, 1]
            pay[a * n:(a + 1) * n] = np.arange(n) + a * n
        return Store(k0, k1, pay), n
    return Store(acc[:, 0].copy(), acc[:, 1].copy(),
                 np.arange(n, dtype=np.int64)), n


def decode_flat(flat, sizes):
    out = []
    for s in reversed(sizes):
        nxt = flat // s
        out.append(int(flat - nxt * s))
        flat = nxt
    return list(reversed(out))


# ---- what the sweep keeps ----
CNT = {}
RES = {}
CAP = 200000


def record(tid, cols_iter):
    c = CNT.get(tid, 0) + 1
    CNT[tid] = c
    if c <= CAP:
        s = frozenset(int(x) for x in cols_iter)
        RES.setdefault(tid, []).append(s)


# ---- which cells a reading licenses, and how each is searched ----
def licensed_cell(cell, m, tid):
    q0, q1, q2, q3 = cell
    for nm, val in (("total", m), ("L", q0 + q1), ("Q2", q2), ("Q3", q3)):
        f = FORCED[nm]
        if f is not None and (val & 1) != ((f >> tid) & 1):
            return False
    return True


def cells_of(m):
    out = []
    for q0 in range(min(10, m) + 1):
        for q1 in range(min(10, m - q0) + 1):
            for q2 in range(min(10, m - q0 - q1) + 1):
                q3 = m - q0 - q1 - q2
                if 0 <= q3 <= 10:
                    out.append((q0, q1, q2, q3))
    return out


def plan_cell(cell, nt):
    ks = sorted(((cell[q], q) for q in range(4)), reverse=True)
    if ks[0][0] >= 9:
        return {"kind": "w48", "bigq": ks[0][1], "bigk": ks[0][0]}
    if ks[0][0] >= 7:
        return {"kind": "lop", "bigq": ks[0][1], "bigk": ks[0][0]}
    live = [q for q in range(4) if cell[q] > 0]
    best = None
    for r in range(0, len(live)):
        for st_set in itertools.combinations(live, r):
            str_set = [q for q in live if q not in st_set]
            store_n = 1
            for q in st_set:
                store_n *= math.comb(48, cell[q])
            ssz = sorted((math.comb(48, cell[q]), q) for q in str_set)
            stream_n = 1
            for s, _q in ssz:
                stream_n *= s
            if len(str_set) == 1:
                rate, outer_iters = 19e6, 0
            else:
                outer_n = 1
                for s, _q in ssz[:-1]:
                    outer_n *= s
                if outer_n > 30000:
                    continue
                rate, outer_iters = 120e6, outer_n
            for folded in (True, False):
                stot = store_n * (nt if folded else 1)
                if stot > 50_000_000:
                    continue
                passes = 1 if folded else nt
                probes = stream_n * passes
                cost = (stot * 4e-7 + probes / rate +
                        outer_iters * passes * 3e-5)
                if best is None or cost < best["cost"]:
                    best = {"kind": "pair", "st": list(st_set),
                            "str": [q for _s, q in ssz],
                            "folded": folded, "cost": cost}
    assert best is not None, cell
    return best


def run_pair(cell, plan, tids):
    st_meta = []
    st_tabs = []
    for q in plan["st"]:
        tab, unr = qtab(q, cell[q])
        st_tabs.append(tab)
        st_meta.append((q, unr, len(tab)))
    stq, n_store = product_store(st_tabs, tids, plan["folded"])
    sizes = [m[2] for m in st_meta]
    str_qs = plan["str"]                      # ascending by size
    inner_q = str_qs[-1]
    inner_tab, inner_unr = qtab(inner_q, cell[inner_q])
    outer_qs = str_qs[:-1]
    outer_unrs = [qtab(q, cell[q])[1] for q in outer_qs]
    if outer_qs:
        on, oacc = product_keys([qtab(q, cell[q])[0] for q in outer_qs])
        osizes = [len(qtab(q, cell[q])[0]) for q in outer_qs]
    else:
        on, oacc, osizes = 1, np.zeros((1, 2), dtype=np.uint64), []

    def emit(hits, shift_t=None):
        ni = len(inner_tab)
        for spos, pay in hits:
            oi, ii = divmod(spos, ni)
            if plan["folded"]:
                a, flat = divmod(pay, n_store)
                tid = tids[a]
            else:
                tid, flat = shift_t, pay
            if CNT.get(tid, 0) >= CAP:
                CNT[tid] = CNT.get(tid, 0) + 1
                continue
            cols = []
            for (q, unr, _s), bi in zip(st_meta, decode_flat(flat, sizes)):
                cols += unr(bi)
            cols += inner_unr(ii)
            for unr, bi in zip(outer_unrs, decode_flat(oi, osizes)):
                cols += unr(bi)
            record(tid, cols)

    CHV = 4_000_000
    ni = len(inner_tab)
    if plan["folded"]:
        hits = []
        for io in range(on):
            b0, b1 = oacc[io, 0], oacc[io, 1]
            for cb in range(0, ni, CHV):
                blk = inner_tab[cb:cb + CHV]
                sub = []
                stq.probe(blk[:, 0] ^ b0, blk[:, 1] ^ b1, sub)
                hits += [((io * ni + cb + p), pay) for p, pay in sub]
        emit(hits)
    else:
        for t in tids:
            hits = []
            for io in range(on):
                b0 = oacc[io, 0] ^ TG[t, 0]
                b1 = oacc[io, 1] ^ TG[t, 1]
                for cb in range(0, ni, CHV):
                    blk = inner_tab[cb:cb + CHV]
                    sub = []
                    stq.probe(blk[:, 0] ^ b0, blk[:, 1] ^ b1, sub)
                    hits += [((io * ni + cb + p), pay) for p, pay in sub]
            emit(hits, shift_t=t)


def run_lop_group(bigq, bigk, jobs):
    stores = []
    for cell, tids in jobs:
        rest = [q for q in range(4) if q != bigq and cell[q] > 0]
        tabs, meta = [], []
        for q in rest:
            tab, unr = qtab(q, cell[q])
            tabs.append(tab)
            meta.append((q, unr, len(tab)))
        stq, n_store = product_store(tabs, tids, True)
        stores.append((stq, [m[2] for m in meta], n_store, meta, tids, []))
    T6, noff6 = get_T6(bigq)
    cols = Q_COLS[bigq]
    if bigk == 7:
        outers = [((c,), int(noff6[c + 1])) for c in range(48)]
    else:
        outers = [((c0, c1), int(noff6[c1 + 1]))
                  for c0 in range(48) for c1 in range(c0 + 1, 48)]
    for pre, lo in outers:
        if lo >= len(T6):
            continue
        x = T6[lo:].copy()
        for c in pre:
            x ^= COLS[cols[c]]
        x0 = np.ascontiguousarray(x[:, 0])
        x1 = np.ascontiguousarray(x[:, 1])
        for ent in stores:
            sub = []
            ent[0].probe(x0, x1, sub)
            for p, pay in sub:
                ent[5].append((pre, lo + p, pay))
    unr6 = qtab(bigq, 6)[1]
    for stq, sizes, n_store, meta, tids, hits in stores:
        for pre, i6, pay in hits:
            a, flat = divmod(pay, n_store)
            tid = tids[a]
            if CNT.get(tid, 0) >= CAP:
                CNT[tid] = CNT.get(tid, 0) + 1
                continue
            cc = [int(cols[c]) for c in pre] + unr6(i6)
            for (q, unr, _s), bi in zip(meta, decode_flat(flat, sizes)):
                cc += unr(bi)
            record(tid, cc)


def run_w48_group(bigq, bigk, jobs):
    eA, eB = 2 * bigq, 2 * bigq + 1
    colsA, colsB = E_COLS[eA], E_COLS[eB]
    kk = min(10, bigk)
    TA, NA = build_chain(colsA, kk)
    TB, NB = build_chain(colsB, kk)
    sh = []
    for cell, tids in jobs:
        rest = [q for q in range(4) if q != bigq and cell[q] > 0]
        combos = [([], np.zeros(2, dtype=np.uint64))]
        for q in rest:
            tab, unr = qtab(q, cell[q])
            combos = [(cc + unr(i), key ^ tab[i])
                      for cc, key in combos for i in range(len(tab))]
        for t in tids:
            for cc, key in combos:
                sh.append((t, TG[t] ^ key, cc))
    if not sh:
        return
    for ka in range(max(0, bigk - 24), min(24, bigk) + 1):
        kb = bigk - ka
        if ka > kk or kb > kk:
            continue
        tA, tB = TA.get(ka), TB.get(kb)
        if tA is None or tB is None or len(tA) == 0 or len(tB) == 0:
            continue
        if len(tA) <= len(tB):
            smlT, smlN, smlK, smlCols = tA, NA, ka, colsA
            bigT, bigN, bigK, bigCols = tB, NB, kb, colsB
        else:
            smlT, smlN, smlK, smlCols = tB, NB, kb, colsB
            bigT, bigN, bigK, bigCols = tA, NA, ka, colsA
        ns = len(smlT)
        nsh = len(sh)
        hits = []  # (big_idx, sml_idx, sh_idx)
        if ns * nsh <= max(3_000_000, len(bigT)):
            k0 = np.empty(ns * nsh, dtype=np.uint64)
            k1 = np.empty(ns * nsh, dtype=np.uint64)
            pay = np.empty(ns * nsh, dtype=np.int64)
            for a, (t, key, cc) in enumerate(sh):
                k0[a * ns:(a + 1) * ns] = smlT[:, 0] ^ key[0]
                k1[a * ns:(a + 1) * ns] = smlT[:, 1] ^ key[1]
                pay[a * ns:(a + 1) * ns] = np.arange(ns) + a * ns
            stq = Store(k0, k1, pay)
            CHV = 4_000_000
            for cb in range(0, len(bigT), CHV):
                blk = bigT[cb:cb + CHV]
                sub = []
                stq.probe(np.ascontiguousarray(blk[:, 0]),
                          np.ascontiguousarray(blk[:, 1]), sub)
                for p, pv in sub:
                    a, i_s = divmod(pv, ns)
                    hits.append((cb + p, i_s, a))
        else:
            # store the big side raw; probe the small side once per shift
            stq = Store(bigT[:, 0].copy(), bigT[:, 1].copy(),
                        np.arange(len(bigT), dtype=np.int64))
            for a, (t, key, cc) in enumerate(sh):
                sub = []
                stq.probe(smlT[:, 0] ^ key[0], smlT[:, 1] ^ key[1], sub)
                for p, pv in sub:
                    hits.append((pv, p, a))
        for ib, i_s, a in hits:
            t, key, cc = sh[a]
            if CNT.get(t, 0) >= CAP:
                CNT[t] = CNT.get(t, 0) + 1
                continue
            cols = (unrank(smlN, smlK, i_s, smlCols) +
                    unrank(bigN, bigK, ib, bigCols) + [int(x) for x in cc])
            record(t, cols)


def run_sweep(m, tgt_ids):
    """search every set of exactly m pieces; returns the licensed-cell count"""
    todo = []
    for cell in cells_of(m):
        tids = [t for t in tgt_ids if licensed_cell(cell, m, t)]
        if tids:
            todo.append((cell, tids))
    lop_groups, w48_groups = {}, {}
    for cell, tids in todo:
        plan = plan_cell(cell, len(tids))
        if plan["kind"] == "w48":
            w48_groups.setdefault((plan["bigq"], plan["bigk"]), []).append(
                (cell, tids))
        elif plan["kind"] == "lop":
            lop_groups.setdefault((plan["bigq"], plan["bigk"]), []).append(
                (cell, tids))
        else:
            run_pair(cell, plan, tids)
    for (q, k), jobs in sorted(lop_groups.items()):
        run_lop_group(q, k, jobs)
    for (q, k), jobs in sorted(w48_groups.items()):
        run_w48_group(q, k, jobs)
    return len(todo)


def gf2_rank(ints):
    bs = {}
    r = 0
    for v in ints:
        while v:
            lb = v.bit_length() - 1
            if lb in bs:
                v ^= bs[lb]
            else:
                bs[lb] = v
                r += 1
                break
    return r


gate(PKOK and UNROK and NTG == 18 and len(FORCED) == 15, "eng.pack",
     "the {0} cuttings pin {1} independent parities; a piece's packed parities add as "
     "they should on 20 sampled ten-sets, the lex chains unrank correctly, and {2} "
     "readings are in play".format(NS, ERANK, NTG))

# --------------------------- Part 4: every even size below ten, recomputed as a check

CS = {}
LCS = {}
for msml in (2, 4, 6):
    CNT.clear()
    RES.clear()
    LCS[msml] = run_sweep(msml, list(range(8)))
    CS[msml] = [CNT.get(t, 0) for t in range(8)]

gate([LCS[msml] for msml in (2, 4, 6)] == [5, 14, 30]
     and all(c == 0 for msml in (2, 4, 6) for c in CS[msml]), "m8.below",
     "no set of two, four or six pieces carries any of the eight readings: those sizes "
     "license {0}, {1} and {2} cells and every count over them is 0".format(
         LCS[2], LCS[4], LCS[6]))

CNT.clear()
RES.clear()
LC8 = run_sweep(8, list(range(8)))
C8 = [CNT.get(t, 0) for t in range(8)]
RES8 = dict((t, list(RES.get(t, []))) for t in range(8))

gate(C8[0] == 648 and LC8 == 55, "m8.zero",
     "at eight pieces the constant zero reading is carried by {0} sets, found over the "
     "{1} cells the eight readings license".format(C8[0], LC8))
gate(C8[1] == 192, "m8.one",
     "the constant one reading is carried by {0} sets of eight pieces".format(C8[1]))
gate(all(c == 0 for c in C8[2:]), "m8.reading",
     "no set of eight pieces carries any of the six nonconstant readings: the six "
     "counts are {0}".format(C8[2:]))
NV8 = 0
BAD8 = 0
for t in range(8):
    for s in RES8[t]:
        Sv = sorted(s)
        fv = (INCL[:, Sv].sum(axis=1) & 1).astype(np.uint8)
        if len(Sv) != 8 or not np.array_equal(fv, FV[t]):
            BAD8 += 1
        NV8 += 1
gate(NV8 == C8[0] + C8[1] and BAD8 == 0, "m8.ver",
     "each of the {0} returned octets has eight pieces and reproduces its own reading on "
     "all {1} cuttings; {2} mismatched".format(NV8, NS, BAD8))
EV8 = [uint_of(sorted(s)) for s in RES8[0]]
OD8 = [uint_of(sorted(s)) for s in RES8[1]]
R_EV = gf2_rank(EV8)
R_OD = gf2_rank([OD8[0] ^ v for v in OD8[1:]]) if len(OD8) > 1 else -1
R_JT = gf2_rank(EV8 + [OD8[0] ^ v for v in OD8[1:]])
gate(R_EV == 104 and R_OD == 104 and R_JT == 104, "m8.span",
     "the {0} zero-carrying octets span {1} dimensions, the dimension of the space of "
     "sets that carry it; differences of the {2} one-carrying octets span {3}, and the "
     "two together still span {4}".format(C8[0], R_EV, C8[1], R_OD, R_JT))

# -------------------------------- Part 5: what the block parities license, and Part 6:
# the search at ten pieces. The sweep runs here because the last licensing gate reports
# the control reading's swept count alongside the cells it licenses.

FNAMES = sorted(nm for nm in BLK if FORCED[nm] is not None)
UNAMES = sorted(nm for nm in BLK if FORCED[nm] is None)
NR = NTG - 1


def fbit(nm, t):
    """the forced parity of a block for one reading, or -1 when the block is free"""
    a = FORCED[nm]
    return -1 if a is None else ((a >> t) & 1)


def parvec(nm):
    return [fbit(nm, t) for t in range(NR)]


ZR = [0] * NR
QPAT = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]
LCOK = []
for pi, (pnm, prof) in enumerate(P10SPEC):
    t = NT + pi
    expp = (sum(prof) & 1, (prof[0] + prof[1]) & 1, prof[2] & 1, prof[3] & 1)
    gotp = tuple(fbit(nm, t) for nm in ("total", "L", "Q2", "Q3"))
    LCOK.append(gotp == expp)
PODD = fbit("total", TCTL)
LC_ODD = sum(1 for cell in cells_of(10) if licensed_cell(cell, 10, TCTL))

CNT.clear()
RES.clear()
LC10 = run_sweep(10, list(range(NTG)))
GOT = [CNT.get(t, 0) for t in range(NTG)]

gate(FNAMES == ["L", "Q2", "Q3", "R", "total"] and parvec("total") == ZR
     and parvec("L") == ZR and parvec("R") == ZR and parvec("Q2") == QPAT
     and parvec("Q3") == QPAT, "lic.forced",
     "a forced parity exists for exactly the whole set, its two halves and the two "
     "quarters of the second half; whole and halves force even on all {0} readings, and "
     "each of those quarters forces {1}".format(NR, QPAT))
gate(UNAMES == ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "Q0", "Q1"],
     "lic.free",
     "neither quarter of the first half, and none of the eight blocks of {0} pieces, "
     "carries a forced parity, so a search may split those freely: {1} free "
     "blocks".format(24, len(UNAMES)))
gate(all(LCOK) and len(LCOK) == 5, "lic.prof",
     "each of the five planted ten-piece readings forces exactly the whole, half and "
     "quarter parities its own construction has: {0}".format(LCOK))
gate(PODD == 1 and LC_ODD == 0 and GOT[TCTL] == 0, "lic.odd",
     "the synthetic reading of odd total parity forces an odd whole, which no set of ten "
     "pieces can meet: it licenses {0} cells and the sweep returns {1} sets".format(
         LC_ODD, GOT[TCTL]))

# ------------------------------------------ Part 6: the frontier at ten pieces

EXP10 = [0, 0, 0, 0, 0, 0, 0, 0, 108, 1, 2, 0, 2, 1, 1, 1, 1, 0]
gate(GOT == EXP10 and LC10 == 146, "ten.counts",
     "over the {0} cells the eighteen readings license, the complete search at ten "
     "pieces returns {1}".format(LC10, GOT))
PREC = [P10[NT + pi] in set(RES.get(NT + pi, [])) for pi in range(5)]
gate(all(PREC), "ten.plant",
     "each of the five planted ten-piece sets is among the sets the sweep returns for "
     "its own reading: {0}".format(PREC))
NV10 = 0
BAD10 = 0
DUP10 = 0
for t in range(NTG):
    lst = RES.get(t, [])
    if len(set(lst)) != len(lst):
        DUP10 += 1
    for s in lst[:100]:
        Sv = sorted(s)
        fv = (INCL[:, Sv].sum(axis=1) & 1).astype(np.uint8)
        if len(Sv) != 10 or not np.array_equal(fv, FV[t]):
            BAD10 += 1
        NV10 += 1
gate(BAD10 == 0 and DUP10 == 0 and NV10 == sum(min(c, 100) for c in GOT), "ten.ver",
     "{0} of the returned ten-piece sets, up to 100 per reading, reproduce their reading "
     "on all {1} cuttings; {2} mismatched and no reading returned a set "
     "twice".format(NV10, NS, BAD10))

RPK = dict((PK[i].tobytes(), i) for i in range(NS))
RP = []
FD0 = True
for cp in CP:
    inv = np.argsort(cp)
    pkp = np.packbits(INC[:, inv], axis=1)
    rp = np.empty(NS, dtype=np.int64)
    for i in range(NS):
        rp[i] = RPK.get(pkp[i].tobytes(), -1)
    FD0 = FD0 and int(rp.min()) >= 0 and len(set(rp.tolist())) == NS
    RP.append(rp)
CPFIX = [all(bool(np.array_equal(FV[t][rp], FV[t])) for rp in RP)
         for t in range(NTG)]
FD2 = True
ORBT = {}
JOBS = [(t, RES.get(t, []), 10) for t in range(NTG)]
JOBS += [(0, RES8[0], 8), (1, RES8[1], 8)]
for t, src, msz in JOBS:
    if not CPFIX[t] or not src:
        continue
    tups = set(tuple(sorted(int(c) for c in s)) for s in src)
    for s in tups:
        for cp in CP:
            FD2 = FD2 and tuple(sorted(int(cp[c]) for c in s)) in tups
    rest = set(tups)
    osz = []
    while rest:
        s0 = min(rest)
        orb = set(tuple(sorted(int(cp[c]) for c in s0)) for cp in CP)
        osz.append(len(orb))
        rest -= orb
    ORBT["{0} at {1}".format(TNAME[t], msz)] = sorted(osz)
NFIX = sum(1 for v in CPFIX if v)
gate(FD0 and FD2 and CPFIX[0] and CPFIX[1], "ten.sym",
     "each of the 48 symmetries of the cell permutes the {0} cuttings among themselves; "
     "{1} of the {2} readings are unmoved by all of them, and the sets carrying those "
     "map onto one another under the action, in orbits of sizes {3}".format(
         NS, NFIX, NTG, ORBT))

SIX = list(range(2, 8))
gate(all(CS[msml][t] == 0 for msml in (2, 4, 6) for t in SIX)
     and all(C8[t] == 0 for t in SIX) and all(GOT[t] == 0 for t in SIX)
     and all(fbit("total", t) == 0 for t in SIX), "ten.floor",
     "neither side of any of the three nonconstant readings is carried at two, four, six, eight or "
     "ten pieces, and each forces an even total, which bars every odd size: every one "
     "of the six nonconstant readings needs at least twelve pieces")
gate(all(CS[msml][0] == 0 and CS[msml][1] == 0 for msml in (2, 4, 6))
     and C8[0] == 648 and GOT[0] == 0 and C8[1] == 192 and GOT[1] == 0, "ten.gap",
     "the sets carrying the constant zero reading number 0 below eight pieces, {0} at "
     "eight and {1} at ten; those carrying the constant one likewise number 0, {2} and "
     "{3}".format(C8[0], GOT[0], C8[1], GOT[1]))

print("")
print("N5 execution certificate", flush=True)
N5 = [
    "per_element: checked -- all 192 used piece columns and every exact-weight-ten support",
    "per_site: checked -- one supplied 16-corner coordinate cell; no physical cell selection",
    "per_mode: checked and not executed -- no field, spectral, or momentum-mode decomposition",
    "per_block: checked -- all 15,800 cutting rows and every licensed quarter-split cell",
    "lattice_wide: checked and not executed -- no multi-cell, arbitrary-L, or continuum claim",
]
for line in N5:
    print("N5 " + line, flush=True)

receipt = {
    "schema": "physical-cell-cutting-size-ten-frontier-cycle738-v2",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "runner_sha256": file_sha256("scripts/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05.py"),
    "supplied_model": {
        "shape": [1, 1, 1, 1],
        "support_universe": "the 192 pieces used by the 15,800 supplied cuttings only",
        "piece_class": "five-corner normalized-volume-one simplices only",
        "cost": "corner pairs with four-coordinate L1 separation greater than one",
        "physical_cell_tick_simplex_reading_bridge": "open",
    },
    "direct_dependency": {
        "cycle": 737,
        "status": C737_RECEIPT.get("status"),
        "geometric_cuttings": NS,
        "used_pieces": NPO,
        "reading_identity_bound": IDENTITY_OK,
        "previous_maximum_cardinality": C737_RECEIPT.get("complete_support_sweep", {}).get("maximum_cardinality"),
    },
    "forced_parity_certificate": {
        "forced_blocks": FNAMES,
        "free_blocks": UNAMES,
        "quarter_pattern": QPAT,
        "licensed_cells_at_ten": LC10,
    },
    "complete_search_at_ten": {
        "readings": TNAME,
        "counts": GOT,
        "nonconstant_readings": 6,
        "nonconstant_minimum_lower_bound": 12,
        "zero_and_one_next_support_lower_bound": 12,
        "duplicate_returns": DUP10,
        "mismatched_verified_returns": BAD10,
    },
    "no_go_discipline": {
        "status": "PASS",
        "claim_scope": "exact-weight-ten UNSAT for eight named functions in one fixed 192-column finite incidence system only",
        "n5_execution_certificate": N5,
    },
    "gates": {"pass": PF[0], "fail": PF[1], "named": {name: "PASS" if ok else "FAIL" for name, ok in GATES}},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]), flush=True)
sys.exit(1 if PF[1] else 0)
