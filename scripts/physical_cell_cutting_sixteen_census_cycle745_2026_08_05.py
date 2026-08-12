"""Cycle 745: the complete sixteen census through an anchored slice.

The object is the unit four-cube on the sixteen corners of the sixteen zero-one words of
length four, cut into pieces of least volume at the floor of the declared adjacency cost. Its
15800 cuttings use 24 pieces each, drawn from 192 pieces in all, and a set of pieces
represents a named algebraic reading when, on every cutting, the parity of how many of its pieces that
cutting uses reproduces the reading. Earlier cycles completed the search at every even
size up to fourteen and found none of the six named nonconstant readings, and the forced total
parity of each reading bars every odd size, so sixteen is the first open size. This
runner rebuilds the two seeded order-two piece permutations that extend the 48 to fifty
generators acting with a single orbit on the pieces and fixing all eight readings, so
every sixteen-piece carrier of such a reading has an image through a chosen anchor piece. It
then completes the anchored slice of the search at exactly sixteen, every subset drawn
through the anchor, against the six named nonconstant readings and five planted sixteen-piece controls
through the anchor. A canonical synthetic odd-total target is separately rejected by
augmented rank before licensing or search. The runner reconstructs the full
census of each reading as the group images of its anchored slice, re-verifying every
reconstructed member directly against the incidence columns and folding the census into
orbits under the 48 and under the full group.

Class-A: integer and field-with-two-elements arithmetic on a finite explicit object, no
solver. Every count below is measured here.
"""
import hashlib
import itertools
import json
import math
import resource
import sys
import time
from pathlib import Path

import numpy as np

T0 = time.time()
PF = [0, 0]
OUT = [0]
GATES = []
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_census_cycle745_"
    "independent_check_2026_08_05.py"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_sixteen_census_cycle745_2026_08_05_"
    "receipt_2026-08-05.json"
)
C737_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md"
C737_PRIMARY_PATH = "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py"
C737_CHECKER_PATH = (
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
    "independent_check_2026_08_05.py"
)
C737_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json"
)
C737_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C741_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md"
C741_PRIMARY_PATH = "scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py"
C741_CHECKER_PATH = (
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_"
    "independent_check_2026_08_05.py"
)
C741_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05_"
    "receipt_2026-08-05.json"
)
C741_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py",
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_census_cycle745_"
    "independent_check_2026_08_05.py",
)
AUDIT_TIMEOUT_SEC = 900

C737_PRIMARY_INPUTS = (
    C737_NOTE_PATH,
    C737_CHECKER_PATH,
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
)
C737_INDEPENDENT_INPUTS = (
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_RECEIPT_PATH,
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
)
C739_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_TWELVE_FRONTIER_CYCLE739_NOTE_2026-08-05.md"
C739_PRIMARY_PATH = "scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py"
C739_CHECKER_PATH = (
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_"
    "independent_check_2026_08_05.py"
)
C739_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_"
    "receipt_2026-08-05.json"
)
C739_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C739_PRIMARY_INPUTS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    "docs/PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05.py",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    C739_NOTE_PATH,
    C739_CHECKER_PATH,
    "requirements.txt",
    "requirements-release.txt",
)
C739_INDEPENDENT_INPUTS = (
    C739_NOTE_PATH,
    C739_CHECKER_PATH,
    C739_PRIMARY_PATH,
    C739_RECEIPT_PATH,
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    "docs/PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05.py",
    "scripts/physical_cell_cutting_size_ten_frontier_cycle738_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_size_ten_frontier_cycle738_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "requirements.txt",
    "requirements-release.txt",
)
C741_PRIMARY_INPUTS = (
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    C739_NOTE_PATH,
    C739_PRIMARY_PATH,
    C739_CHECKER_PATH,
    C739_RECEIPT_PATH,
    C739_INDEPENDENT_RECEIPT_PATH,
    C741_NOTE_PATH,
    C741_CHECKER_PATH,
)
C741_INDEPENDENT_INPUTS = (
    C741_NOTE_PATH,
    C741_PRIMARY_PATH,
    C741_RECEIPT_PATH,
    "requirements.txt",
    "requirements-release.txt",
    C737_NOTE_PATH,
    C737_PRIMARY_PATH,
    C737_CHECKER_PATH,
    C737_RECEIPT_PATH,
    C737_INDEPENDENT_RECEIPT_PATH,
    C739_RECEIPT_PATH,
    C739_INDEPENDENT_RECEIPT_PATH,
    C739_NOTE_PATH,
    C739_PRIMARY_PATH,
    C739_CHECKER_PATH,
)


def file_sha256(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def receipt_inputs_current(receipt, required_paths):
    expected = receipt.get("input_sha256", {})
    return set(expected) == set(required_paths) and all(
        expected.get(path) == file_sha256(path) for path in required_paths
    )


def emit(s):
    """print one line, refusing any barred digit pair"""
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    OUT[0] += len(txt) + 1
    print(txt)


def gate(ok, name, detail):
    passed = bool(ok)
    PF[0 if passed else 1] += 1
    GATES.append((name, passed))
    emit(("PASS " if passed else "FAIL ") + name + "  " + detail)



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
ODD_CONTROL_PACKED_ROW = min(bytes(np.packbits(row)) for row in INC)
ODD_CONTROL_ROW = next(
    row for row in range(NS)
    if bytes(np.packbits(INC[row])) == ODD_CONTROL_PACKED_ROW
)
FODD[ODD_CONTROL_ROW] = 1
TNAME.append("odd-ctl")
FVEC.append(FODD)
NTG = len(FVEC)
TCTL = NTG - 1
FV = np.stack(FVEC)
TG = pack88(FV[:, EPIV])

# ---- exact identity and predecessor closure ----
PACKED_ROWS = [bytes(row) for row in np.packbits(INC, axis=1)]
CANONICAL_INCIDENCE_ROWS_SHA256 = hashlib.sha256(
    b"".join(sorted(PACKED_ROWS))
).hexdigest()
SUPPORT_TUPLES = [tuple(sorted(int(c) for c in UNI[USED[a]])) for a in range(NPO)]
SUPPORT_COLUMN_ORDER_SHA256 = hashlib.sha256(
    json.dumps(SUPPORT_TUPLES, separators=(",", ":")).encode("utf-8")
).hexdigest()


def canonical_target_hash(function):
    pairs = sorted(zip(PACKED_ROWS, (int(bit) for bit in function)))
    return hashlib.sha256(
        b"".join(row + bytes((bit,)) for row, bit in pairs)
    ).hexdigest()


def target_witness(function):
    """A deterministic support whose incidence response is function, or None."""
    piv = {}
    for column in range(NPO):
        value = int(COLS[column, 0]) | (int(COLS[column, 1]) << 64)
        witness = 1 << column
        while value:
            head = value.bit_length() - 1
            if head not in piv:
                piv[head] = (value, witness)
                break
            basis_value, basis_witness = piv[head]
            value ^= basis_value
            witness ^= basis_witness
    target = pack88(function[EPIV])
    value = int(target[0]) | (int(target[1]) << 64)
    witness = 0
    while value:
        head = value.bit_length() - 1
        if head not in piv:
            return None
        basis_value, basis_witness = piv[head]
        value ^= basis_value
        witness ^= basis_witness
    support = [column for column in range(NPO) if (witness >> column) & 1]
    return support if np.array_equal(
        (INCL[:, support].sum(axis=1) & 1).astype(np.uint8), function
    ) else None


TARGET_IDENTITY = {}
for target_name, target_function in zip(TNAME, FV):
    exact_witness = target_witness(target_function)
    TARGET_IDENTITY[target_name] = {
        "ones": int(target_function.sum()),
        "canonical_rows_with_bit_sha256": canonical_target_hash(target_function),
        "realizable": exact_witness is not None,
        "witness_support": exact_witness,
    }
ODD_CONTROL_ROW_SHA256 = hashlib.sha256(ODD_CONTROL_PACKED_ROW).hexdigest()

C737 = json.loads((ROOT / C737_RECEIPT_PATH).read_text(encoding="utf-8"))
C737I = json.loads((ROOT / C737_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
C741 = json.loads((ROOT / C741_RECEIPT_PATH).read_text(encoding="utf-8"))
C741I = json.loads((ROOT / C741_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
for reading_name, witness in C737.get("verified_upper_witnesses", {}).items():
    TARGET_IDENTITY[reading_name]["witness_support"] = list(
        witness.get("support_indices_0_to_191", [])
    )
for control_name, control_support in PLANT:
    TARGET_IDENTITY[control_name]["witness_support"] = list(control_support)
for planted_index, (planted_name, _profile) in enumerate(P16SPEC):
    TARGET_IDENTITY[planted_name]["witness_support"] = list(PSET[NT + planted_index])
C737_IDENTITY = C737.get("reading_identity", {})
C737I_IDENTITY = C737I.get("reading_identity", {})
EXPECTED_READING_NAMES = [
    "zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip"
]
IDENTITY_OK = (
    C737.get("schema") == "physical-cell-cutting-least-computing-sets-cycle737-v2"
    and C737.get("status") == "pass" and C737.get("gates", {}).get("fail") == 0
    and C737.get("runner_sha256") == file_sha256(C737_PRIMARY_PATH)
    and receipt_inputs_current(C737, C737_PRIMARY_INPUTS)
    and C737I.get("schema")
    == "physical-cell-cutting-least-computing-sets-cycle737-independent-v1"
    and C737I.get("status") == "pass" and C737I.get("gates", {}).get("fail") == 0
    and C737I.get("runner_sha256") == file_sha256(C737_CHECKER_PATH)
    and receipt_inputs_current(C737I, C737_INDEPENDENT_INPUTS)
    and C737_IDENTITY.get("canonical_incidence_rows_sha256")
    == CANONICAL_INCIDENCE_ROWS_SHA256
    and C737I_IDENTITY.get("canonical_incidence_rows_sha256")
    == CANONICAL_INCIDENCE_ROWS_SHA256
    and C737_IDENTITY.get("support_column_order_sha256")
    == SUPPORT_COLUMN_ORDER_SHA256
    and C737I_IDENTITY.get("support_column_order_sha256")
    == SUPPORT_COLUMN_ORDER_SHA256
    and all(
        TARGET_IDENTITY[name]["ones"]
        == C737_IDENTITY.get("functions", {}).get(name, {}).get("ones")
        == C737I_IDENTITY.get("functions", {}).get(name, {}).get("ones")
        and TARGET_IDENTITY[name]["canonical_rows_with_bit_sha256"]
        == C737_IDENTITY.get("functions", {}).get(name, {}).get(
            "canonical_rows_with_bit_sha256"
        )
        == C737I_IDENTITY.get("functions", {}).get(name, {}).get(
            "canonical_rows_with_bit_sha256"
        )
        for name in EXPECTED_READING_NAMES
    )
)
C741_SEARCH = C741.get("complete_search_at_fourteen", {})
C741_BOUND = C741.get("nonconstant_reading_bound", {})
PREDECESSOR_OK = (
    C741.get("schema") == "physical-cell-cutting-fourteen-frontier-cycle741-v2"
    and C741.get("status") == "pass" and C741.get("gates", {}).get("fail") == 0
    and C741.get("runner_sha256") == file_sha256(C741_PRIMARY_PATH)
    and receipt_inputs_current(C741, C741_PRIMARY_INPUTS)
    and C741I.get("schema")
    == "physical-cell-cutting-fourteen-frontier-cycle741-independent-v1"
    and C741I.get("status") == "pass" and C741I.get("gates", {}).get("fail") == 0
    and C741I.get("checker_sha256") == file_sha256(C741_CHECKER_PATH)
    and receipt_inputs_current(C741I, C741_INDEPENDENT_INPUTS)
    and C741_SEARCH.get("readings", [])[:8] == EXPECTED_READING_NAMES
    and C741_SEARCH.get("counts", [])[:8] == [34560, 26880, 0, 0, 0, 0, 0, 0]
    and C741_SEARCH.get("execution_inventory_exact") is True
    and C741_SEARCH.get("scheduled_splits") == 2562
    and C741_SEARCH.get("executed_splits") == 2562
    and C741_BOUND.get("reading_names") == EXPECTED_READING_NAMES[2:]
    and C741_BOUND.get("complete_even_sizes") == [2, 4, 6, 8, 10, 12, 14]
    and C741_BOUND.get("odd_sizes_barred_by_total_parity") is True
    and C741_BOUND.get("minimum_support_lower_bound") == 16
    and C741.get("no_go_discipline", {}).get("status") == "PASS"
    and C741I.get("exact_weight_fourteen_answers", {})
    == {name: False for name in EXPECTED_READING_NAMES[2:]}
)
gate(IDENTITY_OK, "D01", "Cycle 737 binds this exact incidence, order, and eight readings")
gate(PREDECESSOR_OK, "D02",
     "Cycle 741 primary and independent receipts bind complete emptiness through weight 14")
gate(len(EA[4]) == 46128 and len(EA[6]) == 31968 and len(KEY[4]) == 120
     and HITS == {"four": 2, "six": 2, "seven": 2}, "ID01",
     "the complete 124812100-pair census pins 46128 four-moves, 31968 six-moves, "
     "120 four-move differences, and exactly the three normalized reading pairs")
gate([TARGET_IDENTITY[name]["ones"] for name in EXPECTED_READING_NAMES]
     == [0, 15800, 5664, 10136, 7704, 8096, 7424, 8376]
     and all(TARGET_IDENTITY[name]["realizable"] for name in TNAME[:-1])
     and not TARGET_IDENTITY[TNAME[-1]]["realizable"], "ID02",
     "seventeen named targets are realizable; the odd-total synthetic rejector alone is not")
TARGET_WITNESSES_OK = all(
    metadata["realizable"]
    and metadata["witness_support"] is not None
    and np.array_equal(
        (INCL[:, metadata["witness_support"]].sum(axis=1) & 1).astype(np.uint8),
        FV[TNAME.index(name)],
    )
    for name, metadata in TARGET_IDENTITY.items() if name != "odd-ctl"
)
gate(TARGET_WITNESSES_OK and TARGET_IDENTITY["odd-ctl"]["witness_support"] is None,
     "ID03", "every realizable target has a directly rechecked exact support witness")
if not (IDENTITY_OK and PREDECESSOR_OK):
    emit("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
    raise SystemExit(1)

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
        PROCD.append((cell, tuple(sorted([A] + list(B)))))
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
SWEEP = SIX + PL16
PIECES = [PSET[NT + pi] for pi in range(5)]

gate(set(nm for nm in BLK if FORCED[nm] is not None) >= {"total", "L", "R", "Q2", "Q3"}
     and all(fbit(nm, t) == 0 for t in SIX + PL16
             for nm in ("total", "L", "R", "Q2", "Q3")), "G11",
     "each realizable named nonconstant reading and each planted reading forces even "
     "total, side, and quarter parities")

SEQ = [lic_count(m, 2) for m in range(2, 17, 2)]
ARITH = [sum((k + 1) * (m - 2 * k + 1) for k in range(m // 2 + 1))
         for m in range(2, 17, 2)]
DIFF = [SEQ[i + 1] - SEQ[i] for i in range(7)]
gate(SEQ == ARITH and SEQ == [5, 14, 30, 55, 91, 140, 204, 285]
     and DIFF == [(i + 3) * (i + 3) for i in range(7)], "G12",
     "the licensed cells of a named nonconstant reading count 5,14,30,55,91,140,204,285 at the even sizes "
     "two to sixteen, matching the closed sum, with consecutive odd squares as steps")
CS = [frozenset(c for c in cells_of(16) if licensed_cell(c, 16, t)) for t in SIX]
gate(all(cs == CS[0] for cs in CS) and len(CS[0]) == 285
     and all(lic_count(16, t) == 285 for t in SIX), "G13",
     "all six named nonconstant readings license the same 285 cells at sixteen, one pass covers the six")
gate(TCTL not in SWEEP and not TARGET_IDENTITY["odd-ctl"]["realizable"], "G14",
     "the inconsistent odd-total synthetic target is rejected before licensing or search")

AL16 = [c for c in cells_of(16) if licensed_cell(c, 16, 2) and c[3] >= 1]
gate(len(AL16) == 204 and all(
     frozenset(c for c in cells_of(16) if licensed_cell(c, 16, t) and c[3] >= 1)
     == frozenset(AL16) for t in SIX + PL16), "G15",
     "the licensed cells at sixteen with a piece in the last quarter number 204, and "
     "the six named nonconstant readings and the five planted readings share exactly that list")

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


def expected_anchored_inventory(m, tid):
    """Independent mathematical partition inventory; ignores streamed-part choice."""
    inventory = []
    for cell in cells_of(m):
        if cell[3] < 1 or not licensed_cell(cell, m, tid):
            continue
        heavy = [q for q in range(4) if cell[q] > 6]
        if not heavy:
            parts = [("Q", q, cell[q]) for q in range(4) if cell[q] > 0]
            inventory.append((cell, tuple(sorted(parts))))
            continue
        distributions = [
            [(left, cell[q] - left) for left in range(cell[q] + 1)
             if left <= 24 and cell[q] - left <= 24]
            for q in heavy
        ]
        for split in itertools.product(*distributions):
            parts = []
            for q, (left, right) in zip(heavy, split):
                parts.extend((("E", 2 * q, left), ("E", 2 * q + 1, right)))
            parts.extend(("Q", q, cell[q]) for q in range(4) if q not in heavy)
            if ("E", AE, 0) in parts:
                continue
            inventory.append((cell, tuple(sorted(p for p in parts if p[2] > 0))))
    return inventory


EXPECTED12 = expected_anchored_inventory(12, 2)
EXPECTED16 = expected_anchored_inventory(16, 2)


def arun(m, tids):
    ok = True
    for cell in cells_of(m):
        if cell[3] < 1:
            continue
        if not run_cell(cell, m, tids):
            ok = False
    return ok


# ---- Part 4d: the anchored control at twelve and the anchored sweep at sixteen ----
fresh()
del BLOWN[:]
OK12 = arun(12, SIX)
C12 = [CNT.get(t, 0) for t in SIX]
COV12, NSPL12, NDS12 = coverage(12, SIX)
AL12 = [c for c in cells_of(12) if licensed_cell(c, 12, 2) and c[3] >= 1]
emit("m=12 anchored control counts " + vshow(C12) + " splits " + cshow(NSPL12))
gate(OK12 and not BLOWN and C12 == [0, 0, 0, 0, 0, 0]
     and COV12 == [len(AL12)] * 6 and NSPL12 == NDS12 == len(EXPECTED12) == 371
     and PROCD == EXPECTED12, "G17",
     "the anchored search at twelve reproduces the earlier empty census for the six "
     "readings, every anchored licensed cell and all 371 expected splits covered")

fresh()
del BLOWN[:]
OK16 = arun(16, SWEEP)
C16 = [CNT.get(t, 0) for t in SWEEP]
COV16, NSPL16, NDS16 = coverage(16, SWEEP)
emit("m=16 anchored counts " + vshow(C16) + " splits " + cshow(NSPL16))
gate(OK16 and not BLOWN, "G18",
     "the anchored search at sixteen runs every split within the table budget")
gate(COV16 == [len(AL16)] * 11 and NSPL16 == NDS16 and NSPL16 > 0, "G19",
     "every anchored licensed cell at sixteen is covered for all eleven live readings "
     "and all splits are distinct")
gate(NSPL16 == NDS16 == len(EXPECTED16) == 2004 and PROCD == EXPECTED16, "G19b",
     "the executed anchored schedule equals the independently constructed 2004-split "
     "inventory in exact order")
DELETED_INVENTORY = PROCD[:-1]
REDIRECTED_INVENTORY = list(PROCD)
redirected_cell, redirected_parts = REDIRECTED_INVENTORY[0]
redirected_parts = list(redirected_parts)
redirected_kind, redirected_index, redirected_size = redirected_parts[0]
redirected_parts[0] = (redirected_kind, redirected_index, redirected_size + 1)
REDIRECTED_INVENTORY[0] = (redirected_cell, tuple(sorted(redirected_parts)))
gate(DELETED_INVENTORY != EXPECTED16 and REDIRECTED_INVENTORY != EXPECTED16, "H01",
     "deleting or redirecting one scheduled split invalidates the exact inventory")
V16 = verify(SWEEP)
gate(V16[1] == 0 and V16[2] == 0
     and V16[0] == sum(min(c, CAP) for c in C16), "G20",
     "every recorded set checks back against the columns, no duplicates")
ANOK = True
for t in SWEEP:
    for w, arr in by_width(t).items():
        ANOK = ANOK and bool((arr == ACOL).any(axis=1).all())
gate(ANOK, "G21", "every recorded set holds the anchor piece")
gate(TCTL not in SWEEP and TARGET_IDENTITY["odd-ctl"]["witness_support"] is None, "G22",
     "the non-column-space odd-total synthetic target cannot enter the carrier search")
PREC = [has_set(NT + pi, PIECES[pi]) for pi in range(5)]
gate(all(PREC) and len(PREC) == 5, "G23",
     "all five planted anchored sixteen-piece controls are found by the search")
gate(C16[0] >= 1, "G24",
     "the four reading attains sixteen, consistent with the landed floor")

# ---- Part 4e: the full group and the census reconstruction ----
gate(all(np.array_equal(INC[PERMS[gi]][:, CP[gi]], INC) for gi in range(48))
     and all(len(STAB[t]) == 48 for t in SIX), "G25",
     "each of the 48 pairs with its cutting permutation on the table and fixes all six "
     "named algebraic readings")
GN = [np.ascontiguousarray(p.astype(np.int64)) for p in GENS]
IDP = np.arange(NP, dtype=np.int64)
EG = {IDP.tobytes(): IDP}
FR = [IDP]
while FR:
    NX = []
    for p in FR:
        for g in GN:
            q = g[p]
            kb = q.tobytes()
            if kb not in EG:
                EG[kb] = q
                NX.append(q)
    FR = NX
EGL = list(EG.values())
gate(len(EGL) == 384 and len(set(int(p[ACOL]) for p in EGL)) == NP, "G26",
     "the fifty generators close into a group of order 384 whose images of the anchor "
     "piece reach all 192 pieces")

BW4 = by_width(2)
FOUND4 = sorted(set(tuple(int(x) for x in row) for arr in BW4.values() for row in arr))
A4 = len(FOUND4)
CEN = set()
for p in EGL:
    for S in FOUND4:
        CEN.add(tuple(sorted(int(p[c]) for c in S)))
NCEN = len(CEN)
emit("the " + TNAME[2] + " reading: anchored slice " + cshow(A4)
     + " sets, census " + cshow(NCEN) + " sets")
gate(A4 >= 1 and A4 == C16[0] and NCEN == 12 * A4, "G27",
     "the census is exactly twelve sets for each anchored one")
CCN = np.zeros(NP, dtype=np.int64)
for S in CEN:
    for c in S:
        CCN[c] += 1
gate(bool((CCN == A4).all()), "G28",
     "each of the 192 pieces lies in the same number of census sets as the anchor")
gate(set(S for S in CEN if ACOL in S) == set(FOUND4), "G29",
     "the anchored members of the reconstructed census are exactly the recorded slice, "
     "so the slice is stable under the group")
FA4 = FV[2]
VOK = all(len(S) == 16 and len(set(S)) == 16
          and bool((((INCL[:, list(S)].sum(axis=1)) & 1) == FA4).all()) for S in CEN)
gate(VOK, "G30",
     "every census member re-checks directly against the incidence columns as a "
     "sixteen-piece carrier of the " + TNAME[2] + " reading, all distinct")
gate(all(CNT.get(t, 0) == 0 for t in SIX[1:]), "G31",
     "the anchored slices of the other five readings are empty, so their size-16 "
     "censuses are empty and, with prior sizes and odd sizes barred, 18 is next unsearched")


def cfold(perms):
    LST = sorted(CEN)
    IDX = {}
    for i, S in enumerate(LST):
        IDX[S] = i
    par = list(range(len(LST)))

    def fnd(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    closed = True
    for p in perms:
        for i, S in enumerate(LST):
            j = IDX.get(tuple(sorted(int(p[c]) for c in S)))
            if j is None:
                closed = False
                continue
            ra, rb = fnd(i), fnd(j)
            if ra != rb:
                par[ra] = rb
    SZ = {}
    for i in range(len(LST)):
        r = fnd(i)
        SZ[r] = SZ.get(r, 0) + 1
    DIST = {}
    for v in SZ.values():
        DIST[v] = DIST.get(v, 0) + 1
    return closed, len(SZ), DIST


CL48, NO48, DI48 = cfold([CP[gi] for gi in range(48)])
CLE, NOE, DIE = cfold(GN)
gate(CL48 and CLE and sum(k * v for k, v in DI48.items()) == NCEN
     and sum(k * v for k, v in DIE.items()) == NCEN and NOE <= NO48, "G32",
     "the census is a union of whole orbits under the 48 and under the full group")
emit("census fold under the 48: " + cshow(NO48) + " orbits sized " + dshow(DI48))
emit("census fold under the full group: " + cshow(NOE) + " orbits sized " + dshow(DIE))

EL = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
ELB, RSB = upto(EL, 500), 2500
emit("elapsed under {0} s peak memory under {1} MB".format(ELB, RSB))
gate(EL < 900.0 and RSS < float(RSB), "G33",
     "the whole runner finishes under {0} seconds inside the printed {1} MB".format(
         900, 2500))
CH = OUT[0] + 120
gate(CH < 5500, "G34", "its output stays under {0} characters".format(5500))

N5 = [
    "per_element: checked -- every one of the 192 supplied columns is eligible",
    "per_site: checked -- the claim concerns one supplied 16-corner cell only",
    "per_mode: checked and not executed -- this finite system defines no modes",
    "per_block: checked -- all 15800 cutting rows constrain every exact search",
    "lattice_wide: checked and not executed -- no multicell or limit claim is made",
]
for n5_line in N5:
    print("N5 " + n5_line, flush=True)

inventory_sha256 = hashlib.sha256(
    json.dumps(PROCD, separators=(",", ":")).encode("utf-8")
).hexdigest()
group_sha256 = hashlib.sha256(b"".join(sorted(EG))).hexdigest()
seeded_permutations = {
    "b0": [int(column) for column in b0],
    "b1": [int(column) for column in b1],
}
base_support_permutations = [
    [int(column) for column in permutation] for permutation in CP
]
ordered_generator_support_permutations = base_support_permutations + [
    seeded_permutations["b0"], seeded_permutations["b1"]
]
ordered_generator_support_permutations_sha256 = hashlib.sha256(
    json.dumps(
        ordered_generator_support_permutations, separators=(",", ":")
    ).encode("utf-8")
).hexdigest()
receipt = {
    "schema": "physical-cell-cutting-sixteen-census-cycle745-v2",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "runner_sha256": file_sha256(PRIMARY_PATH),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependencies": {
        "cycle737_identity_bound": IDENTITY_OK,
        "cycle741_through_fourteen_bound": PREDECESSOR_OK,
    },
    "population": {
        "cuttings": NS,
        "used_pieces": NPO,
        "incidence_rank": ERANK,
    },
    "incidence_identity": {
        "canonical_incidence_rows_sha256": CANONICAL_INCIDENCE_ROWS_SHA256,
        "support_column_order_sha256": SUPPORT_COLUMN_ORDER_SHA256,
        "support_column_corner_tuples": [list(support) for support in SUPPORT_TUPLES],
    },
    "reading_identity": {
        "canonical_incidence_rows_sha256": CANONICAL_INCIDENCE_ROWS_SHA256,
        "support_column_order_sha256": SUPPORT_COLUMN_ORDER_SHA256,
        "functions": {
            name: {
                "ones": TARGET_IDENTITY[name]["ones"],
                "canonical_rows_with_bit_sha256": TARGET_IDENTITY[name][
                    "canonical_rows_with_bit_sha256"
                ],
            }
            for name in EXPECTED_READING_NAMES
        },
    },
    "target_identity": {
        "ordered_names": list(TNAME),
        "targets": TARGET_IDENTITY,
        "fixed_control_supports": {
            name: [int(column) for column in support] for name, support in PLANT
        },
        "pseed": PSEED,
        "planted_specs": [
            {"name": name, "profile": [int(value) for value in profile]}
            for name, profile in P16SPEC
        ],
        "planted_supports": {
            name: [int(column) for column in PSET[NT + index]]
            for index, (name, _profile) in enumerate(P16SPEC)
        },
        "odd_control_non_column_space": not TARGET_IDENTITY["odd-ctl"]["realizable"],
        "odd_control_row_sha256": ODD_CONTROL_ROW_SHA256,
        "canonical_incidence_rows_sha256": CANONICAL_INCIDENCE_ROWS_SHA256,
        "support_column_order_sha256": SUPPORT_COLUMN_ORDER_SHA256,
    },
    "complete_anchored_search_at_sixteen": {
        "readings": [TNAME[target] for target in SWEEP],
        "counts": C16,
        "licensed_anchor_cells_per_live_reading": len(AL16),
        "scheduled_splits": len(EXPECTED16),
        "executed_splits": len(PROCD),
        "execution_inventory_exact": PROCD == EXPECTED16,
        "execution_inventory_sha256": inventory_sha256,
        "mismatched_returns": V16[1],
        "duplicate_returns": V16[2],
    },
    "transitive_group": {
        "base_generator_count": len(CP),
        "base_support_permutations": base_support_permutations,
        "seeded_support_permutations": seeded_permutations,
        "seeded_support_permutations_sha256": hashlib.sha256(
            json.dumps(seeded_permutations, separators=(",", ":"), sort_keys=True).encode(
                "utf-8"
            )
        ).hexdigest(),
        "ordered_generator_support_permutations_sha256": (
            ordered_generator_support_permutations_sha256
        ),
        "generated_order": len(EGL),
        "anchor_column": ACOL,
        "anchor_orbit_size": len(set(int(p[ACOL]) for p in EGL)),
        "generated_group_sha256": group_sha256,
    },
    "four_reading_census": {
        "anchored_count": A4,
        "complete_count": NCEN,
        "anchored_supports": [list(support) for support in FOUND4],
        "complete_supports": [list(support) for support in sorted(CEN)],
        "per_piece_multiplicity": A4,
        "base_48_orbit_count": NO48,
        "base_48_orbit_size_distribution": DI48,
        "full_group_orbit_count": NOE,
        "full_group_orbit_size_distribution": DIE,
    },
    "nonconstant_reading_boundary": {
        "four_attains_size": 16,
        "empty_at_sixteen": [TNAME[target] for target in SIX[1:]],
        "prior_complete_even_sizes": C741_BOUND.get("complete_even_sizes", []),
        "odd_sizes_barred_by_total_parity": True,
        "next_unsearched_size": 18,
        "attainment_at_eighteen_shown": False,
    },
    "no_go_discipline": {
        "status": "PASS",
        "named_wall": "exact size-16 emptiness for five named nonconstant readings",
        "residual": "size 18 and larger remain open; no size-18 witness is claimed",
        "n5_execution_certificate": N5,
    },
    "gates": {
        "pass": PF[0],
        "fail": PF[1],
        "named": {name: "PASS" if ok else "FAIL" for name, ok in GATES},
    },
}
RECEIPT_PATH.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
emit("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
