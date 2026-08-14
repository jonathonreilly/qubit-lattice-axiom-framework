"""Rebuild the cutting system of the unit four-cube and test whether its
invariant cutting-kernel is a sum of complete isotypic components.

Every count below is measured here. The runner builds the cell complex, the least
volume pieces, the cuttings at the adjacency cost floor, the piece sharing table,
its exact rational rank and blind space, the group of symmetries carrying the
system to itself, the trace of each symmetry on the blind space, the maps
commuting with every symmetry, and the images of the least exchange, gating each
quantity in place.
"""
import copy
import hashlib
import itertools
import json
import math
import resource
import sys
import time
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_blind_space_symmetry_cycle755_2026_08_09.py"
)
CHECKER_PATH = (
    "scripts/physical_cell_cutting_blind_space_symmetry_cycle755_"
    "independent_check_2026_08_09.py"
)
NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_BLIND_SPACE_SYMMETRY_"
    "CYCLE755_NOTE_2026-08-09.md"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_blind_space_symmetry_cycle755_"
    "2026_08_09_receipt_2026-08-09.json"
)
C754_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_"
    "CYCLE754_NOTE_2026-08-09.md"
)
C754_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py"
)
C754_CHECKER_PATH = (
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "independent_check_2026_08_09.py"
)
C754_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "2026_08_09_receipt_2026-08-09.json"
)
C754_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_"
    "independent_check_2026_08_09_receipt_2026-08-09.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_BLIND_SPACE_SYMMETRY_CYCLE755_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_blind_space_symmetry_cycle755_independent_check_2026_08_09.py",
    "docs/PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09.md",
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py",
    "scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_independent_check_2026_08_09.py",
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09_receipt_2026-08-09.json",
    "outputs/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_independent_check_2026_08_09_receipt_2026-08-09.json",
    "requirements.txt",
    "requirements-release.txt",
)


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


def inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded.get(path) == sha256(path)
        for path in recorded
    )


def write_failure(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-isotypic-overlap-cycle755-v2",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cycle754_contract(primary, independent):
    rational = primary.get("rational_shadow", {})
    exchange = primary.get("exchange_boundary", {})
    independent_rational = independent.get("rational_shadow", {})
    independent_exchange = independent.get("exchange_boundary", {})
    return (
        primary.get("schema") == "physical-cell-cutting-shadow-rank-cycle754-v2"
        and primary.get("status") == "pass"
        and primary.get("claim_type") == "bounded_theorem"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C754_PRIMARY_PATH)
        and inputs_current(primary)
        and rational.get("rank") == 88
        and rational.get("kernel_dimension") == 104
        and exchange.get("four_for_four_witness")
        == {"positive": [4, 5, 10, 11], "negative": [1, 3, 7, 9]}
        and independent.get("schema")
        == "physical-cell-cutting-shadow-rank-cycle754-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("claim_type") == "bounded_theorem"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == sha256(C754_CHECKER_PATH)
        and inputs_current(independent)
        and independent_rational.get("rank") == 88
        and independent_rational.get("kernel_dimension") == 104
        and independent_exchange.get("witness_orbit_size") == 96
    )

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


write_failure("runner has not completed")
C754 = load(C754_RECEIPT_PATH)
C754I = load(C754_INDEPENDENT_RECEIPT_PATH)
C754_OK = cycle754_contract(C754, C754I)
gate(C754_OK, "dependency.cycle754",
     "current Cycle 754 primary and helper bind rank 88, kernel 104, and the least exchange")
bad_cycle754 = copy.deepcopy(C754I)
bad_cycle754.setdefault("rational_shadow", {})["rank"] = 87
gate(not cycle754_contract(C754, bad_cycle754), "hostile.cycle754_rank",
     "a one-unit reversion of the direct predecessor rank is rejected")



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
# ---- Part 4d: the object in plain counts ----
INT = INCL.astype(np.int32)
RW = sorted(set(int(v) for v in INT.sum(axis=1)))
CSUM = sorted(set(int(v) for v in INT.sum(axis=0)))
emit("")
emit("the object: {0} cuttings and {1} pieces, {2} pieces to a cutting, {3} cuttings "
     "through a piece".format(cshow(NS), NPO, cshow(RW[0]), cshow(CSUM[0])))
gate(len(RW) == 1 and len(CSUM) == 1 and RW == [24] and CSUM == [1975]
     and RW[0] * NS == CSUM[0] * NPO, "G11",
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
     and MK[2] + MK[3] == NS and [FLR[1], FLR[2], FLR[3]] == [8, 3, 6], "G12",
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
     and CSUM[0] * FLR[1] == NS, "G13",
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
     and sum(PAIR.values()) == 192 * 191 // 2, "G14",
     "those carriers meet each piece the same number of times and meet each other in "
     "0, 1, 2 or 4 pieces, never 3")

CLOSED = all(any(np.array_equal(FV[i] ^ FV[j], FV[k]) for k in range(8))
             for i in range(8) for j in range(8))
FLIPOK = all(np.array_equal(FV[i] ^ FV[1], FV[i ^ 1]) for i in range(8))
emit("those eight readings close into an addition group of order {0}".format(8))
gate(CLOSED and FLIPOK and len(set(tuple(int(x) for x in v) for v in FV)) == 8, "G15",
     "each flip partner is its reading plus the all-marked reading, so a reading and "
     "its flip partner have least sizes differing by at most eight")

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

EG = closure(GENS, NP)
SSET = set(frozenset(s) for s in STARS)
PERMS = all(frozenset(int(g[j]) for j in s) in SSET for g in EG for s in STARS)
emit("")
gate(len(EG) == 384 and PERMS and EORB == [NP], "G16",
     "they close into a group of {0} transitive on the pieces, permuting the {1} eight-piece carriers".format(384, len(SSET)))

FA = INCL.astype(np.float64)
SHC = np.rint(FA.T @ FA).astype(np.int64)
np.fill_diagonal(SHC, 0)
IB = INCL.astype(np.int64)
NCUT = int(INCL.shape[0])
# ---- Part 5a: the shadow the pieces cast, and the exchanges no cutting sees ----
from fractions import Fraction as YFR
import hashlib as YHL

YPCOL = IB.sum(axis=0)
YPPC = int(YPCOL[0])
YPCOK = bool((YPCOL == YPPC).all())
YPROW = IB.sum(axis=1)
YPPR = int(YPROW[0])
YPROK = bool((YPROW == YPPR).all())
YPKB = np.packbits(IB.astype(np.uint8), axis=0)
YNDC = len(set(YPKB[:, w].tobytes() for w in range(NPO)))
YSMAX = int(SHC.max())

YGRM = IB.T @ IB
YDIA = np.diag(YGRM).copy()
YGOK = bool(((YGRM - np.diag(YDIA)) == SHC).all())
YGOK = YGOK and bool((YDIA == YPCOL).all())
YGOK = YGOK and bool((YGRM.sum(axis=1) == YPPC * YPPR).all())



def yrref(YMAT):
    """rational elimination on the sharing table, the exact certificate for its rank"""
    ya = [[YFR(int(v)) for v in row] for row in YMAT]
    yn = len(ya)
    ym = len(ya[0])
    ypiv = []
    yr = 0
    for yc in range(ym):
        yp = None
        for ys in range(yr, yn):
            if ya[ys][yc] != 0:
                yp = ys
                break
        if yp is None:
            continue
        ya[yr], ya[yp] = ya[yp], ya[yr]
        yiv = ya[yr][yc]
        ya[yr] = [v / yiv for v in ya[yr]]
        for ys in range(yn):
            if ys != yr and ya[ys][yc] != 0:
                yf = ya[ys][yc]
                ya[ys] = [ya[ys][j] - yf * ya[yr][j] for j in range(ym)]
        ypiv.append(yc)
        yr += 1
        if yr == yn:
            break
    return ya, ypiv


YRR, YPIV = yrref(YGRM.tolist())
YRANK = len(YPIV)
YPSET = set(YPIV)
YFREE = [w for w in range(NPO) if w not in YPSET]
YKB = []
for YF in YFREE:
    YVEC = [YFR(0)] * NPO
    YVEC[YF] = YFR(1)
    for YI in range(YRANK):
        YVEC[YPIV[YI]] = -YRR[YI][YF]
    YDEN = 1
    for YW in YVEC:
        YDEN = YDEN * YW.denominator // math.gcd(YDEN, YW.denominator)
    YKB.append([int(YW * YDEN) for YW in YVEC])
YKA = np.array(YKB, dtype=np.int64)
YKDIM = int(YKA.shape[0])
YKZERO = bool(((IB @ YKA.T) == 0).all())
YKUNIT = bool((YKA[np.arange(YKDIM), YFREE] == 1).all())
YBAL = bool((YKA.sum(axis=1) == 0).all())
YVALS = sorted(int(w) for w in np.unique(YKA))
YKMX = int(np.abs(YKA).max())
YSUP = np.count_nonzero(YKA, axis=1)
YSV, YSC = np.unique(YSUP, return_counts=True)
YSUPS = " ".join("{0}".format(int(w)) for w in YSV)
YCNTS = " ".join("{0}".format(int(w)) for w in YSC)
YHIS = [(int(YSV[w]), int(YSC[w])) for w in range(len(YSV))]

# ---- Part 5b: the sharing table is fixed by every symmetry, so the shadow is too ----
YFIXG = all(bool((YGRM[np.ix_(g, g)] == YGRM).all()) for g in EG)
YSTK = np.concatenate([YKA[:, g].T for g in EG], axis=1)
YSTKN = int(YSTK.shape[1])
YBND = NPO * int(YGRM.max()) * YKMX < (1 << 24)
YSYMOK = bool((YGRM.astype(np.float32) @ YSTK.astype(np.float32) == 0.0).all())
del YSTK



# ---- Part 6a: the object and its shadow, gated in exact integers ----

emit("")
gate(YPCOK and YPROK and YGOK and YPPC == 1975 and YPPR == 24
     and YNDC == NPO and YSMAX == 1266 and YSMAX < YPPC, "G17",
     "every piece sits on {0} cuttings and every cutting on {1} pieces, all {2} "
     "columns differ, and the largest share of two pieces is {3}"
     .format(YPPC, YPPR, YNDC, YSMAX))
gate(YKZERO and YKUNIT and YBAL and YKDIM == 104 and YRANK == 88
     and YRANK + YKDIM == NPO, "G18",
     "the table has exact rational rank {0}, so the blind space has dimension {1} "
     "and the two add to {2}".format(YRANK, YKDIM, NPO))

ZNG = len(EG)
ZB = YKA
ZF = list(YFREE)
ZKD = YKDIM
ZSTK = np.concatenate([ZB[:, g].T for g in EG], axis=1)
ZSYM = bool((YGRM @ ZSTK == 0).all())
del ZSTK
ZOVB = NPO * int(YGRM.max()) * YKMX
gate(YFIXG and ZSYM and YSYMOK and YBND and ZOVB < (1 << 62), "G19",
     "each of the {0} symmetries fixes the sharing table and carries the blind space "
     "into itself, by exact integers and by a bounded second arithmetic alike"
     .format(ZNG))


# ---- Part 6b: the trace of a symmetry on the blind space, without a projector ----

ZIDA = np.arange(NPO, dtype=np.int64)
ZID = [i for i in range(ZNG) if bool((EG[i] == ZIDA).all())][0]
ZFIX = [int(sum(1 for i in range(NPO) if int(g[i]) == i)) for g in EG]
ZCHK = [int(sum(int(ZB[k][g[ZF[k]]]) for k in range(ZKD))) for g in EG]
ZCHR = [ZFIX[i] - ZCHK[i] for i in range(ZNG)]


def ztrace(g):
    """the trace of one symmetry on the blind space, formed as a matrix"""
    return int(np.trace(ZB[:, g][:, ZF]))


ZMIS = sum(1 for i in range(ZNG) if ztrace(EG[i]) != ZCHK[i])
gate(ZMIS == 0 and ZCHK[ZID] == ZKD and ZFIX[ZID] == NPO
     and ZCHR[ZID] == YRANK, "G20",
     "the trace on the blind space is the sum of {0} basis entries read at the moved "
     "free places, agreeing with the formed trace on all {1} symmetries"
     .format(ZKD, ZNG))


def zavg(a, b):
    """the average of a product of two trace lists over the symmetries"""
    s = 0
    for i in range(ZNG):
        s += a[i] * b[i]
    q, r = divmod(s, ZNG)
    return q, r


ZONE = [1] * ZNG
ZK1, ZK1R = zavg(ZCHK, ZONE)
ZR1, ZR1R = zavg(ZCHR, ZONE)
ZFF, ZFFR = zavg(ZFIX, ZFIX)
ZRK, ZRKR = zavg(ZCHR, ZCHK)
ZKK, ZKKR = zavg(ZCHK, ZCHK)
ZRR, ZRRR = zavg(ZCHR, ZCHR)
ZREM = [ZK1R, ZR1R, ZFFR, ZRKR, ZKKR, ZRRR]
gate(ZR1 == 1 and ZK1 == 0 and EORB == [NP] and max(ZREM) == 0, "G21",
     "the symmetries have one orbit on the pieces, so a constant weighting is the "
     "one symmetric weighting, it is not blind, and the blind space holds none")


# ---- Part 6c: how many orbits the symmetries have on ordered pairs of pieces ----

ZGA = np.array(EG, dtype=np.int64)
ZLAB = np.full(NPO * NPO, -1, dtype=np.int64)
ZNOR = 0
for ZP in range(NPO * NPO):
    if ZLAB[ZP] >= 0:
        continue
    ZI, ZJ = divmod(ZP, NPO)
    ZLAB[ZGA[:, ZI] * NPO + ZGA[:, ZJ]] = ZNOR
    ZNOR += 1
ZLB = ZLAB.reshape(NPO, NPO)
ZSTB = [i for i in range(ZNG) if int(EG[i][0]) == 0]
ZSF = sorted(ZFIX[i] for i in ZSTB)
gate(ZNOR == ZFF and len(ZSTB) * NPO == ZNG and ZSF == [16, NPO]
     and 2 * ZNOR == NPO + 16, "G22",
     "the symmetries have {0} orbits on ordered pairs, by the averaged square of the "
     "fixed counts, by direct orbits, and from a piece stabiliser of order {1} whose "
     "other element fixes 16 pieces".format(ZNOR, len(ZSTB)))

emit("")
emit("averaged squares: seen with seen {0}, seen with blind {1}, blind with blind {2}"
     .format(ZRR, ZRK, ZKK))
gate(ZRR + 2 * ZRK + ZKK == ZFF and ZRR == 29 and ZKK == 33, "G23",
     "the three rebuild the pair-orbit count {0}, so the split of the {1} weightings "
     "into seen and blind is accounted for".format(ZFF, NPO))
gate(ZRK == 21 and ZRK > 0, "G24",
     "the seen/blind irreducible multiplicities have inner product {0}, so the "
     "invariant blind space is not a sum of complete isotypic components"
     .format(ZRK))


# ---- Part 6d: the maps commuting with every symmetry, and what they see ----

ZBT = ZB.T
ZRES = []
ZVEC = []
for ZR in range(ZNOR):
    ZA = (ZLB == ZR).astype(np.int64)
    ZM = YGRM @ (ZA @ ZBT)
    ZRES.append(int(np.abs(ZM).max()))
    ZVEC.append(ZM.reshape(-1))
ZKEEP = [ZR for ZR in range(ZNOR) if ZRES[ZR] == 0]
ZEGS = set(tuple(int(v) for v in g) for g in EG)
ZPOK = True
for ZR in ZKEEP:
    ZA = (ZLB == ZR)
    if not (bool((ZA.sum(axis=1) == 1).all()) and bool((ZA.sum(axis=0) == 1).all())):
        ZPOK = False
        continue
    if tuple(int(np.nonzero(ZA[i])[0][0]) for i in range(NPO)) not in ZEGS:
        ZPOK = False
ZMAXR = max(ZRES)
ZBIG = NPO * int(YGRM.max()) * NPO * YKMX


def zrankp(ZMT, ZQ):
    """the rank of an integer matrix over a prime field, a floor on its rank over
    the rationals, so a ceiling on the dimension of what it sends to zero"""
    ZX = np.mod(ZMT, ZQ)
    ZN, ZW = ZX.shape
    ZK = 0
    for ZC in range(ZW):
        ZNZ = np.nonzero(ZX[ZK:, ZC])[0]
        if ZNZ.size == 0:
            continue
        ZPV = ZK + int(ZNZ[0])
        if ZPV != ZK:
            ZX[[ZK, ZPV]] = ZX[[ZPV, ZK]]
        ZX[ZK] = np.mod(ZX[ZK] * pow(int(ZX[ZK, ZC]), ZQ - 2, ZQ), ZQ)
        ZCL = ZX[ZK + 1:, ZC].copy()
        ZNN = np.nonzero(ZCL)[0]
        if ZNN.size:
            ZX[ZK + 1 + ZNN] = np.mod(
                ZX[ZK + 1 + ZNN] - np.outer(ZCL[ZNN], ZX[ZK]), ZQ)
        ZK += 1
        if ZK == ZN:
            break
    return ZK


ZPRM = 2147483647
ZRNK = zrankp(np.array(ZVEC, dtype=np.int64), ZPRM)
ZDIM = ZNOR - ZRNK
gate(ZRNK == ZRK and ZRNK == 21 and ZDIM == 83 and ZDIM == ZNOR - ZRK
     and ZBIG < (1 << 62), "G25",
     "the maps commuting with every symmetry span {0} dimensions and exactly {1} of "
     "them carry the blind space into itself, a prime-field rank of that condition "
     "returning the same {2} the trace count gave, using a distinct calculation on "
     "the same finite object".format(ZNOR, ZDIM, ZRK))
gate(len(ZKEEP) == 2 and ZPOK and ZNOR - len(ZKEEP) == 102 and ZMAXR == 12738, "G26",
     "yet of the {0} pair-orbit maps spanning them, {1} do so on their own and both "
     "are symmetries in the group already, the other {2} missing by as much as {3}"
     .format(ZNOR, len(ZKEEP), ZNOR - len(ZKEEP), ZMAXR))


# ---- Part 6e: the least exchange, and how much of the blindness it reaches ----

ZV0 = np.zeros(NPO, dtype=np.int64)
for ZW in [4, 5, 10, 11]:
    ZV0[ZW] = 1
for ZW in [1, 3, 7, 9]:
    ZV0[ZW] = -1
ZORB = sorted(set(tuple(int(x) for x in ZV0[g]) for g in EG))
ZOA = np.array(ZORB, dtype=np.int64)
ZOBL = bool(((IB @ ZOA.T) == 0).all())
ZOSUP = sorted(set(int(w) for w in np.count_nonzero(ZOA, axis=1)))
ZMR, ZMP = yrref([list(t) for t in ZORB])
ZSPN = len(ZMP)
ZGAP = ZKD - ZSPN
gate(ZOBL and len(ZORB) == 192 and ZOSUP == [8] and ZSPN == 60
     and ZGAP == 44, "G27",
     "a four-for-four exchange has {0} signed images, every one blind against all "
     "{1} cuttings, and they span {2} of the {3} blind dimensions, leaving {4}"
     .format(len(ZORB), NCUT, ZSPN, ZKD, ZGAP))

ZMU = all(ZMR[k][ZMP[j]] == (1 if k == j else 0)
          for k in range(ZSPN) for j in range(ZSPN))
ZCHM = []
ZDOK = True
for g in EG:
    ZT = 0
    for k in range(ZSPN):
        ZT = ZT + ZMR[k][int(g[ZMP[k]])]
    if ZT.denominator != 1:
        ZDOK = False
    ZCHM.append(int(ZT))
ZM1, ZM1R = zavg(ZCHM, ZONE)
ZMM, ZMMR = zavg(ZCHM, ZCHM)
ZMQ = [ZCHK[i] - ZCHM[i] for i in range(ZNG)]
ZQQ, ZQQR = zavg(ZMQ, ZMQ)
ZMX, ZMXR = zavg(ZCHM, ZMQ)
ZMS, ZMSR = zavg(ZCHM, ZCHR)
ZRM = [ZM1R, ZMMR, ZQQR, ZMXR, ZMSR]
gate(ZMU and ZDOK and ZCHM[ZID] == ZSPN and ZM1 == 0 and max(ZRM) == 0, "G28",
     "those images span a part of the blind space that every symmetry carries into "
     "itself, of dimension {0}, holding no constant weighting".format(ZSPN))
emit("a least exchange reaches {0} of the {1} blind dimensions; averaged squares "
     "for that part {2}, for the rest {3}, across {4}, with the seen space {5}"
     .format(ZSPN, ZKD, ZMM, ZQQ, ZMX, ZMS))
gate(ZMM + 2 * ZMX + ZQQ == ZKK, "G29",
     "the part and the rest rebuild the blind count {0}, which follows from its "
     "premise, the measured content being that every average came out a whole "
     "number, as a wrong trace would not".format(ZKK))

emit("per_element: checked -- all 192 piece coordinates enter the exact invariant-kernel and character checks")
emit("per_site: checked and not executed -- the theorem concerns one supplied coordinate four-cube only")
emit("per_mode: checked -- exact characters resolve multiplicity overlap between the seen and blind modules")
emit("per_block: checked -- blind, seen, exchange-orbit, and complementary blocks are tested explicitly")
emit("lattice_wide: checked and not executed -- no multicell, infinite-lattice, causal, or continuum claim")


# ---- Part 6f: allowances ----

emit("")
EL = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
ELB, RSB = upto(EL, 100), 2500
emit("elapsed under {0} s peak memory under {1} MB".format(ELB, RSB))
gate(EL < 900.0 and RSS < float(RSB), "G30", "inside its time and memory allowance")
CH = OUT[0] + 120
gate(CH < 6000, "G31", "its output stays under {0} characters".format(6000))
emit("")
receipt = {
    "schema": "physical-cell-cutting-isotypic-overlap-cycle755-v2",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "runner_sha256": sha256(PRIMARY_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependencies": {
        "cycle754": {
            "receipt_sha256": sha256(C754_RECEIPT_PATH),
            "independent_receipt_sha256": sha256(C754_INDEPENDENT_RECEIPT_PATH),
            "contract_current": C754_OK,
        },
    },
    "finite_object": {
        "cuttings": NCUT,
        "piece_coordinates": NPO,
        "group_order": ZNG,
        "sharing_rank": YRANK,
        "blind_dimension": ZKD,
        "blind_invariant_under_group": ZSYM,
    },
    "character_overlap": {
        "seen_seen": ZRR,
        "seen_blind": ZRK,
        "blind_blind": ZKK,
        "endomorphism_dimension": ZFF,
        "blind_is_sum_of_complete_isotypic_components": ZRK == 0,
        "rank_88_derived_from_group_fixed_point_characters": False,
    },
    "commutant": {
        "ordered_pair_orbits": ZNOR,
        "residual_rank_mod_prime": ZRNK,
        "blind_preserving_dimension": ZDIM,
        "individual_orbital_matrices_preserving_blind": len(ZKEEP),
        "largest_nonzero_residual_entry": ZMAXR,
    },
    "least_exchange_orbit": {
        "signed_images": len(ZORB),
        "span_dimension": ZSPN,
        "blind_complement_dimension": ZGAP,
    },
    "boundary": {
        "finite_supplied_coordinate_four_cube_only": True,
        "blind_space_is_group_invariant": True,
        "group_fixed_point_characters_alone_determine_rank_claimed": False,
        "all_symmetry_or_incidence_routes_to_rank_excluded": False,
        "all_support_eight_blind_vectors_classified": False,
        "remaining_44_dimensions_generated": False,
        "physical_or_multicell_interpretation_claimed": False,
    },
    "no_go_discipline": {
        "status": "PASS",
        "n5_execution_certificate": [
            "per_element checked",
            "per_site checked and not executed",
            "per_mode checked",
            "per_block checked",
            "lattice_wide checked and not executed",
        ],
    },
    "gates": {"pass": PF[0], "fail": PF[1]},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
emit("RECEIPT {0}".format(RECEIPT_PATH.relative_to(ROOT)))
emit("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
sys.exit(0 if PF[1] == 0 else 1)
