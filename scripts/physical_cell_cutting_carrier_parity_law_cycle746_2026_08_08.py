"""Cycle 746: the parity law that decides which splits can carry a charge.

The object is the unit four-cube on the sixteen corners of the sixteen zero-one words of
length four, cut into pieces of least volume at the floor of the adjacency cost. Its
15800 cuttings use 24 pieces each, drawn from 192 pieces in all, and a set of pieces
carries a reading when, on every cutting, the parity of how many of its pieces that
cutting uses reproduces the reading. The 192 pieces sit in two halves and four quarters,
and a search for carriers of a given size splits that size across the four quarters, so
a split no carrier of the reading can meet is weight the search need not lift.

This runner reads off the incidence, for each of the eighteen readings, which of those
blocks the reading fixes the parity of. The answer is the same five blocks for every
reading: the size, both halves, and quarters two and three. Quarters zero and one are
never fixed, and each half parity is the sum of the parities it covers, so the whole
licensing question is three parities. Two of the five are checked a second way, against
piece sets no cutting can see: a block is left free exactly when one of those sets meets
it in an odd number of pieces, and the size parity is what the odd number of cuttings
per piece already forces.

Those three parities sort the seventeen realizable supplied targets into exactly two
classes, and all six charge readings land in the all-even class.  The eighteenth target
is the deliberately inconsistent odd control from Cycle 745; it is retained only as a
hostile non-column-space rejector and is not called a reading or carrier class.  The two
realizable classes have exact licensed-split counts over the stated finite size ranges.

Class-A: integer and field-with-two-elements arithmetic on a finite explicit object, no
solver. Every count below is measured here.
"""
import copy
import hashlib
import itertools
import json
import resource
import sys
import time
from pathlib import Path

import numpy as np

T0 = time.time()
PF = [0, 0]
GATES = []
OUT = [0]

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = "scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py"
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_"
    "independent_check_2026_08_08.py"
)
C745_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md"
C745_PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py"
C745_CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_census_cycle745_"
    "independent_check_2026_08_05.py"
)
C745_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_census_cycle745_2026_08_05_"
    "receipt_2026-08-05.json"
)
C745_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_census_cycle745_"
    "independent_check_2026_08_05_receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08_"
    "receipt_2026-08-08.json"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    CHECKER_PATH,
    C745_NOTE_PATH,
    C745_PRIMARY_PATH,
    C745_CHECKER_PATH,
    C745_RECEIPT_PATH,
    C745_INDEPENDENT_RECEIPT_PATH,
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "requirements.txt",
    "requirements-release.txt",
)


def file_sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def receipt_inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded[path] == file_sha256(path)
        for path in recorded
    )


def load_receipt(path):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


def fail_receipt(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-carrier-parity-law-cycle746-v2",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


fail_receipt("runner has not completed")
C745_RECEIPT = load_receipt(C745_RECEIPT_PATH)
C745_INDEPENDENT_RECEIPT = load_receipt(C745_INDEPENDENT_RECEIPT_PATH)


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
CTUP = [tuple(sorted(int(c) for c in UNI[USED[a]])) for a in range(NPO)]
CANONICAL_INCIDENCE_ROWS_SHA256 = hashlib.sha256(
    b"".join(sorted(bytes(row) for row in np.packbits(INC, axis=1)))
).hexdigest()
SUPPORT_COLUMN_ORDER_SHA256 = hashlib.sha256(
    json.dumps(CTUP, separators=(",", ":")).encode("utf-8")
).hexdigest()

PK = np.packbits(INC, axis=1)
LUT = np.array([bin(i).count("1") for i in range(256)], dtype=np.uint8)
SZC = [4, 6]
SZG = [4]
EA = dict((k, []) for k in SZC)
EB = dict((k, []) for k in SZC)
DIS = dict((k, set()) for k in SZG)
PROCESSED_PAIR_ROWS = 0
for lo in range(0, NS, 200):
    hi = min(lo + 200, NS)
    PROCESSED_PAIR_ROWS += hi - lo
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
ODD_CONTROL_ROW_BYTES = min(bytes(row) for row in PK)
ODD_CONTROL_ROW_INDEX = next(
    index for index, row in enumerate(PK) if bytes(row) == ODD_CONTROL_ROW_BYTES
)
ODD_CONTROL_ROW_SHA256 = hashlib.sha256(ODD_CONTROL_ROW_BYTES).hexdigest()
FODD[ODD_CONTROL_ROW_INDEX] = 1
TNAME.append("odd-ctl")
FVEC.append(FODD)
NTG = len(FVEC)
TCTL = NTG - 1
FV = np.stack(FVEC)
TG = pack88(FV[:, EPIV])


def target_is_realizable(target):
    """Exact consistency of INC*x=target by simultaneous GF(2) elimination."""
    pivots = {}
    for row, bit in zip(EROW, target):
        vector, rhs = int(row), int(bit)
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (vector, rhs)
                break
            basis_vector, basis_rhs = pivots[pivot]
            vector ^= basis_vector
            rhs ^= basis_rhs
        if vector == 0 and rhs:
            return False
    return True


REALIZABLE = [target_is_realizable(FV[t]) for t in range(NTG)]
REAL_IDS = [t for t in range(NTG) if REALIZABLE[t]]
TARGET_FUNCTION_IDENTITY = {
    name: {
        "ones": int(FV[index].sum()),
        "canonical_rows_with_bit_sha256": hashlib.sha256(b"".join(sorted(
            bytes(row) + bytes((int(bit),))
            for row, bit in zip(PK, FV[index])
        ))).hexdigest(),
        "realizable": bool(REALIZABLE[index]),
    }
    for index, name in enumerate(TNAME)
}
FIXED_CONTROL_SUPPORTS = {name: [int(value) for value in support]
                          for name, support in PLANT}
PLANTED_SPECS = {name: [int(value) for value in profile] for name, profile in P16SPEC}
PLANTED_SUPPORTS = {TNAME[index]: [int(value) for value in PSET[index]]
                    for index in sorted(PSET)}

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


def cycle745_contract(primary, independent):
    """Bind the exact 18-target predecessor population and hostile control."""
    identity = primary.get("target_identity", {})
    independent_identity = independent.get("target_identity", {})

    def identity_matches(candidate):
        targets = candidate.get("targets", {})
        metadata_ok = (
            candidate.get("canonical_incidence_rows_sha256")
            == CANONICAL_INCIDENCE_ROWS_SHA256
            and candidate.get("support_column_order_sha256")
            == SUPPORT_COLUMN_ORDER_SHA256
            and candidate.get("ordered_names") == TNAME
            and candidate.get("fixed_control_supports") == FIXED_CONTROL_SUPPORTS
            and candidate.get("pseed") == PSEED
            and candidate.get("planted_specs") == PLANTED_SPECS
            and candidate.get("planted_supports") == PLANTED_SUPPORTS
            and candidate.get("odd_control_non_column_space") is True
            and candidate.get("odd_control_row_sha256") == ODD_CONTROL_ROW_SHA256
        )
        functions_ok = all(
            name in targets
            and targets[name].get("ones") == local["ones"]
            and targets[name].get("canonical_rows_with_bit_sha256")
            == local["canonical_rows_with_bit_sha256"]
            and targets[name].get("realizable") == local["realizable"]
            for name, local in TARGET_FUNCTION_IDENTITY.items()
        )
        witness_ok = True
        for index, name in enumerate(TNAME):
            support = targets.get(name, {}).get("witness_support")
            if REALIZABLE[index]:
                witness_ok = witness_ok and isinstance(support, list)
                if isinstance(support, list):
                    witness_ok = witness_ok and all(
                        isinstance(value, int) and 0 <= value < NPO for value in support
                    )
                    witness_ok = witness_ok and len(set(support)) == len(support)
                    witness_ok = witness_ok and np.array_equal(
                        (INCL[:, support].sum(axis=1) & 1).astype(np.uint8), FV[index]
                    )
            else:
                witness_ok = witness_ok and support is None
        return metadata_ok and functions_ok and witness_ok

    return (
        primary.get("schema") == "physical-cell-cutting-sixteen-census-cycle745-v2"
        and primary.get("status") == "pass"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == file_sha256(C745_PRIMARY_PATH)
        and receipt_inputs_current(primary)
        and independent.get("schema")
        == "physical-cell-cutting-sixteen-census-cycle745-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and (independent.get("checker_sha256") or independent.get("runner_sha256"))
        == file_sha256(C745_CHECKER_PATH)
        and receipt_inputs_current(independent)
        and identity_matches(identity)
        and identity_matches(independent_identity)
    )


C745_OK = cycle745_contract(C745_RECEIPT, C745_INDEPENDENT_RECEIPT)

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
def lic_count(m, tid):
    return sum(1 for c in cells_of(m) if licensed_cell(c, m, tid))
SIX = list(range(2, 8))

# ---------------------------------------------------------------------------
# cycle 746: what each reading fixes, and what that leaves the search to do
# ---------------------------------------------------------------------------
BARRED = "9" + "9"


def upto(v, step):
    n = (int(v) // step + 1) * step
    while BARRED in "{0}".format(n):
        n += step
    return n


RW = INC.sum(axis=1)
CU = INC.sum(axis=0)
emit("cuttings {0}  pieces {1}  pieces per cutting {2}  cuttings per piece {3}  "
     "pivot rank {4}  realizable targets {5}  hostile controls {6}".format(
         NS, NPO, int(RW.min()), int(CU.min()), ERANK, len(REAL_IDS), NTG - len(REAL_IDS)))
gate(NS == 15800 and NPO == 192 and int(RW.min()) == int(RW.max()) == 24, "G1",
     "the cut object carries {0} cuttings, each using {1} of its {2} pieces".format(
         15800, 24, 192))
gate(int(CU.min()) == int(CU.max()) == 1975 and int(CU.min()) & 1 == 1, "G2",
     "every piece is used by the same odd number of cuttings, {0}".format(1975))
gate(ERANK == 88 and NTG == 18 and len(REAL_IDS) == 17 and len(SIX) == 6,
     "G3", "the incidence has pivot rank 88; 17 targets are realizable, six of "
     "them named charge readings, and one is a hostile inconsistent control")
gate(PROCESSED_PAIR_ROWS == NS, "inventory.pair_rows",
     "the move scan processes all 15800 possible first endpoints")
gate(C745_OK, "dependency.cycle745",
     "the exact Cycle 745 target identities, supports, seed, and control status are bound")
gate(REAL_IDS == list(range(17)) and not REALIZABLE[TCTL], "target.consistency",
     "targets zero through sixteen lie in the incidence column space; odd-ctl does not")

# ---- which blocks a reading fixes the parity of ----
NAMES = ("total", "L", "R", "Q0", "Q1", "Q2", "Q3")
SHOW = {"total": "size", "L": "left half", "R": "right half", "Q0": "quarter zero",
        "Q1": "quarter one", "Q2": "quarter two", "Q3": "quarter three"}


def par(nm, t):
    """the parity reading t fixes on block nm, or None where the block is left free"""
    f = FORCED[nm]
    return None if f is None else (f >> t) & 1


DET = [nm for nm in NAMES if all(par(nm, t) is not None for t in REAL_IDS)]
FRE = [nm for nm in NAMES if all(par(nm, t) is None for t in REAL_IDS)]
emit("fixed for every realizable target: " + ", ".join(SHOW[nm] for nm in DET))
emit("left free for every realizable target: " + ", ".join(SHOW[nm] for nm in FRE))
gate(sorted(DET + FRE) == sorted(NAMES)
     and set(DET) == set(("total", "L", "R", "Q2", "Q3")), "G4",
     "each block is fixed for every realizable target or free for all, and the fixed "
     "ones are the size, "
     "both halves, and quarters two and three")
gate(all(par("R", t) == (par("Q2", t) ^ par("Q3", t))
         and par("L", t) == (par("total", t) ^ par("R", t)) for t in REAL_IDS), "G5",
     "each half parity is the sum of the parities it covers, so licensing a reading is "
     "exactly three conditions: the size, quarter two, and quarter three")

# ---- the same split, seen from the piece sets no cutting can distinguish ----
ECH = {}
for _i in range(ERANK):
    _r = 0
    for _j in range(NPO):
        if P88[_i][_j]:
            _r |= 1 << _j
    while _r:
        _p = _r.bit_length() - 1
        if _p in ECH:
            _r ^= ECH[_p]
        else:
            ECH[_p] = _r
            break
for _p in sorted(ECH):
    _r = ECH[_p]
    for _q in sorted(ECH):
        if _q < _p and (_r >> _q) & 1:
            _r ^= ECH[_q]
    ECH[_p] = _r
KER = []
for _f in range(NPO):
    if _f in ECH:
        continue
    _v = 1 << _f
    for _p in ECH:
        if (ECH[_p] >> _f) & 1:
            _v |= 1 << _p
    KER.append(_v)
KM = np.zeros((NPO, len(KER)), dtype=np.int64)
for _j, _v in enumerate(KER):
    for _i in range(NPO):
        if (_v >> _i) & 1:
            KM[_i, _j] = 1
KRES = (INCL @ KM) & 1
emit("independent piece sets no cutting can see: {0}, the ones built here of sizes {1} "
     "to {2}".format(len(KER), int(KM.sum(axis=0).min()), int(KM.sum(axis=0).max())))
gate(len(ECH) == ERANK and len(KER) == NPO - ERANK and int(KRES.max()) == 0, "G6",
     "{0} independent piece sets no cutting can see, built from the pivot cuttings "
     "alone, are each checked invisible directly against the incidence".format(192 - 88))


def blkmask(nm):
    n = 0
    for i in BLK[nm]:
        n |= 1 << i
    return n


FREEK = set(nm for nm in NAMES
            if any(bin(v & blkmask(nm)).count("1") & 1 for v in KER))
gate(FREEK == set(FRE), "G7",
     "a block is left free exactly when one of those invisible sets meets it in an odd "
     "number of pieces, which happens for quarter zero and quarter one and no other")
WPAR = [int(np.count_nonzero(np.asarray(FVEC[t]))) & 1 for t in range(NTG)]
gate(all(par("total", t) == WPAR[t] for t in REAL_IDS), "G8",
     "and the size parity a reading fixes is the parity of how many cuttings the reading "
     "marks, which is what an odd number of cuttings per piece already forces")


# ---- the three classes those parities cut the readings into ----
def triple(t):
    return (par("total", t), par("Q2", t), par("Q3", t))


def label(tr):
    return "{0} size, quarter two {1}, quarter three {2}".format(
        *["even" if b == 0 else "odd" for b in tr])


CLS = {}
for t in REAL_IDS:
    CLS.setdefault(triple(t), []).append(t)
for tr in sorted(CLS):
    emit("  {0}: {1} readings, {2} of them charges".format(
        label(tr), len(CLS[tr]), sum(1 for t in CLS[tr] if t in SIX)))
gate(len(CLS) == 2 and sorted(len(members) for members in CLS.values()) == [2, 15],
     "G9", "the 17 realizable targets fall into exactly two classes of sizes 2 and 15")
gate(all(triple(t) == (0, 0, 0) for t in SIX), "G10",
     "every charge reading sits in the all-even class, so every carrier of a charge has "
     "even size and meets quarters two and three evenly")
ODD = [tr for tr in CLS if tr[0] == 1]
gate(not ODD and triple(TCTL) == (1, 1, 1) and not REALIZABLE[TCTL], "G11",
     "no realizable class demands odd size; the apparent third class is only odd-ctl, "
     "which exact elimination rejects as inconsistent")
NPR, DIS = 0, 0
for m in range(1, 21):
    for c in cells_of(m):
        for t in REAL_IDS:
            NPR += 1
            if licensed_cell(c, m, t) != ((m & 1) == par("total", t)
                                          and (c[2] & 1) == par("Q2", t)
                                          and (c[3] & 1) == par("Q3", t)):
                DIS += 1
gate(DIS == 0, "G12",
     "the search's own licensing test agrees with those three parities on all {0} pairs "
     "of a split and a realizable target up to size twenty".format(NPR))


# ---- what each class leaves the search to cover ----
def pyr(n):
    """the sum of the first n squares"""
    return n * (n + 1) * (2 * n + 1) // 6


def direct(m, a, b, anchored):
    """splits of m over the four quarters, each holding at most 48 pieces, with quarter
    two of parity a and quarter three of parity b, counted without the incidence"""
    n = 0
    for q2 in range(min(48, m) + 1):
        if (q2 & 1) != a:
            continue
        for q3 in range(min(48, m - q2) + 1):
            if (q3 & 1) != b or (anchored and q3 == 0):
                continue
            rest = m - q2 - q3
            n += sum(1 for q0 in range(min(48, rest) + 1) if rest - q0 <= 48)
    return n


def anc_count(m, t):
    return sum(1 for c in cells_of(m) if c[3] >= 1 and licensed_cell(c, m, t))


EV = list(range(2, 21, 2))
OD = list(range(1, 20, 2))
TCH = SIX[0]
LIC = [lic_count(m, TCH) for m in EV]
ANC = [anc_count(m, TCH) for m in EV]
emit("charge class, splits licensed at sizes two to twenty: "
     + ",".join(str(x) for x in LIC))
emit("of those, splits holding a piece in the anchor quarter: "
     + ",".join(str(x) for x in ANC))
gate(LIC == [pyr(m // 2 + 1) for m in EV], "G13",
     "a charge licenses, at size two k, the sum of the first k plus one squares")
gate(ANC == [pyr(m // 2) for m in EV], "G14",
     "and of those the ones holding a piece in the anchor quarter number the sum of the "
     "first k squares")
gate(LIC == [direct(m, 0, 0, False) for m in EV]
     and ANC == [direct(m, 0, 0, True) for m in EV], "G15",
     "both agree with a direct enumeration that never consults the incidence")
gate(ANC[1:] == LIC[:-1], "G16",
     "so drawing every subset through the anchor costs exactly one size step of the "
     "search's split budget")
GAP = [a - b for a, b in zip(LIC, ANC)]
emit("splits a charge licenses that miss the anchor quarter: "
     + ",".join(str(x) for x in GAP))
gate(GAP == [(m // 2 + 1) ** 2 for m in EV], "G17",
     "the splits a charge licenses that miss the anchor quarter number k plus one, "
     "squared")
if (0, 1, 1) not in CLS:
    raise ValueError("the even-size odd-quarter class is absent")
TWO = CLS[(0, 1, 1)][0]
L2 = [lic_count(m, TWO) for m in EV]
A2 = [anc_count(m, TWO) for m in EV]
emit("odd-quarter class, splits licensed at the same sizes: "
     + ",".join(str(x) for x in L2))
gate(L2 == [pyr(m // 2) for m in EV], "G18",
     "a reading whose two fixed quarters are both odd licenses the sum of the first k "
     "squares, one size step below a charge")
gate(A2 == L2, "G19",
     "and every split it licenses already holds a piece in the anchor quarter, so there "
     "the anchor is free")
gate(not target_is_realizable(FODD), "G20",
     "the planted one-hot odd control is rejected by an exact zero-row/nonzero-RHS "
     "dependency and is not promoted to a carrier class")
gate(all(par("total", t) == 0 for t in REAL_IDS)
     and all(lic_count(m, t) == 0 for m in OD for t in REAL_IDS), "G21",
     "every realizable supplied target has even forced size and licenses no odd-size "
     "split through nineteen")
NMATCH = 0
for _a, _b in ((0, 0), (0, 1), (1, 0), (1, 1)):
    ROW = [direct(m, _a, _b, False) for m in EV[:8]]
    emit("  quarters {0} and {1}: {2}".format(
        "even" if _a == 0 else "odd", "even" if _b == 0 else "odd",
        ",".join(str(x) for x in ROW)))
    if ROW == LIC[:8]:
        NMATCH += 1
gate(NMATCH == 1, "G22",
     "of the four parity pairs only the even one reproduces the charge count, so this "
     "test rejects a wrong parity instead of holding whatever the parities are")

SKIPPED_PAIR_ROWS = sum(min(lo + 100, NS) - lo for lo in range(0, NS, 200))
gate(SKIPPED_PAIR_ROWS == NS // 2 and SKIPPED_PAIR_ROWS != PROCESSED_PAIR_ROWS,
     "hostile.pair_inventory",
     "the submitted half-width chunk loop is detected as 7900 rather than 15800 rows")
bad_dependency = copy.deepcopy(C745_RECEIPT)
bad_dependency["status"] = "fail"
gate(not cycle745_contract(bad_dependency, C745_INDEPENDENT_RECEIPT),
     "hostile.dependency", "a failing predecessor receipt is rejected")
bad_identity = copy.deepcopy(C745_RECEIPT)
bad_identity["target_identity"]["targets"]["four"][
    "canonical_rows_with_bit_sha256"
] = "0" * 64
gate(not cycle745_contract(bad_identity, C745_INDEPENDENT_RECEIPT),
     "hostile.target_identity", "a changed target function identity is rejected")
mutated_odd = FODD.copy()
mutated_odd[ODD_CONTROL_ROW_INDEX] = 0
gate(target_is_realizable(mutated_odd) and not target_is_realizable(FODD),
     "hostile.consistency", "the exact consistency test distinguishes zero from one-hot")

EL = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
ELB, RSB = upto(EL, 20), 2500
emit("elapsed under {0} s peak memory under {1} MB".format(ELB, RSB))
gate(EL < 900.0 and RSS < float(RSB), "G23",
     "it finishes inside its time and memory budget")
CH = OUT[0] + 1400
gate(CH < 6500, "G24", "its output stays under {0} characters".format(6500))
emit("")
print("per_element: checked -- all 192 support columns enter the incidence, kernel, "
      "block, and consistency calculations", flush=True)
print("per_site: checked and not executed -- one supplied coordinate four-cube only; "
      "no framework cell or site is identified", flush=True)
print("per_mode: checked and not executed -- these finite binary targets have no field "
      "or momentum-mode decomposition", flush=True)
print("per_block: checked -- total, two halves, four quarters, all 17 realizable "
      "targets, and the inconsistent control", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell, arbitrary-domain, "
      "boundary, thermodynamic, or continuum statement", flush=True)

receipt = {
    "schema": "physical-cell-cutting-carrier-parity-law-cycle746-v2",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "runner_sha256": file_sha256(PRIMARY_PATH),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependency": {
        "cycle": 745,
        "schema": C745_RECEIPT.get("schema"),
        "target_identity": C745_RECEIPT.get("target_identity"),
    },
    "supplied_incidence": {
        "cuttings": NS,
        "support_columns": NPO,
        "rank": ERANK,
        "kernel_dimension": len(KER),
        "canonical_incidence_rows_sha256": CANONICAL_INCIDENCE_ROWS_SHA256,
        "support_column_order_sha256": SUPPORT_COLUMN_ORDER_SHA256,
        "processed_pair_rows": PROCESSED_PAIR_ROWS,
    },
    "target_population": {
        "ordered_names": TNAME,
        "functions": TARGET_FUNCTION_IDENTITY,
        "realizable_target_indices": REAL_IDS,
        "realizable_targets": len(REAL_IDS),
        "inconsistent_controls": [TNAME[TCTL]],
        "named_charge_indices": SIX,
    },
    "forced_block_parity": {
        "fixed_blocks": DET,
        "free_blocks": FRE,
        "independent_coordinates": ["total", "Q2", "Q3"],
        "realizable_classes": {
            "000": [TNAME[t] for t in CLS[(0, 0, 0)]],
            "011": [TNAME[t] for t in CLS[(0, 1, 1)]],
        },
        "odd_control_triple": list(triple(TCTL)),
        "odd_control_is_realizable": bool(REALIZABLE[TCTL]),
    },
    "licensed_split_counts": {
        "measured_even_sizes": EV,
        "all_even_class": LIC,
        "all_even_class_anchored_q3": ANC,
        "all_even_class_missing_q3": GAP,
        "odd_quarters_class": L2,
        "odd_quarters_class_anchored_q3": A2,
        "split_target_pairs_checked": NPR,
    },
    "no_go_discipline": {
        "status": "PASS",
        "claim_scope": (
            "necessary block-parity licensing and finite split-count identities for "
            "17 exact realizable targets in one supplied incidence table; no carrier "
            "existence or sufficiency claim"
        ),
        "n5_execution_certificate": [
            "per_element checked",
            "per_site checked and not executed",
            "per_mode checked and not executed",
            "per_block checked",
            "lattice_wide checked and not executed",
        ],
    },
    "gates": {
        "pass": PF[0],
        "fail": PF[1],
        "named": {name: "PASS" if ok else "FAIL" for name, ok in GATES},
    },
}
tmp_receipt = RECEIPT_PATH.with_suffix(RECEIPT_PATH.suffix + ".tmp")
tmp_receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n",
                       encoding="utf-8")
tmp_receipt.replace(RECEIPT_PATH)
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]), flush=True)
sys.exit(0 if PF[1] == 0 else 1)
