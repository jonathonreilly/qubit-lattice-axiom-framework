"""Independent reconstruction of Cycle 737's finite support theorem.

The single cell is the unit four-cube with three lattice directions and one tick. Its
least-volume cuttings at the floor of the adjacency cost carry eight readings of the
population: the constant zero, the constant one, and the two sides of each of the three
charges. A set of pieces carries a reading when, on every cutting, the parity of how many
of its pieces that cutting uses reproduces the reading. This runner searches every set of
at most eight pieces, lists the two families of eight-piece sets and their symmetry
orbits, verifies a set of pieces carrying each of the six charge readings, and reads off
the corner geometry of the eight-piece families.

This checker imports and executes no primary implementation.  It uses a Leibniz
determinant rather than the primary minor formula and the largest uncovered exact-cover
pivot rather than the primary smallest pivot.  The support search is rerun from the
independently reconstructed incidence matrix and every returned support is checked on all
15,800 rows.  Failed gates exit nonzero.
"""
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md"
PRIMARY_PATH = (
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json"
)
C736_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05_"
    "receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json",
)
AUDIT_TIMEOUT_SEC = 900


def file_sha256(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


C736_RECEIPT = json.loads((ROOT / C736_RECEIPT_PATH).read_text(encoding="utf-8"))
PRIMARY_RECEIPT = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))

PF = [0, 0]
GATES = []


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    GATES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


# ---------------------------------------------------------------- Part 1: machinery


def det4(A):
    result = np.zeros(len(A), dtype=np.int64)
    rows = np.arange(4)
    for permutation in itertools.permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4) for j in range(i + 1, 4)
        )
        sign = -1 if inversions % 2 else 1
        result += sign * np.prod(A[:, rows, permutation], axis=1, dtype=np.int64)
    return result


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
gate(bool(np.array_equal(
         MM @ IV,
         np.broadcast_to(np.eye(4, dtype=np.int64), MM.shape))),
     "independent.inverse",
     "every float-proposed inverse is accepted only after exact integer multiplication")

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
NEG = [np.array(t, dtype=np.int64)
       for t in itertools.product((-1, 0, 1), repeat=4) if any(t)]


def separated(piece_indices):
    """Count pairs separated by an exact integer plane from a finite candidate set."""
    points = [V[UNI[i]] for i in piece_indices]
    facets = []
    for i in piece_indices:
        inverse = IV[i]
        facets.append([inverse[k] for k in range(4)] + [-inverse.sum(axis=0)])
    good = 0
    total = 0
    for a in range(len(piece_indices)):
        for b in range(a + 1, len(piece_indices)):
            total += 1
            for normal in NEG + facets[a] + facets[b]:
                left = points[a] @ normal
                right = points[b] @ normal
                if int(left.max()) <= int(right.min()) or int(right.max()) <= int(left.min()):
                    good += 1
                    break
    return good, total

gate(len(SUB) == 4368 and NPIECE == 2672 and NQ == 2736 and coll == 0 and face == 0
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
    j = rem.bit_length() - 1
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
gate(LO == 6 and len(MINP) == 400 and NODE[0] == 496849 and NS == 15800
     and FULL == set([24]) and NPO == 192, "base.floor",
    "the independent largest-uncovered-pivot search over the {0} pieces of least cost "
    "{1} visits {2} nodes and finds "
     "{3} cuttings of {4} pieces each, between them using {5} pieces".format(
         len(MINP), LO, NODE[0], NS, 24, NPO))

cooccurring = set()
for solution in SOL:
    cooccurring.update(itertools.combinations(solution, 2))
separated_pairs = sum(separated(pair)[0] for pair in sorted(cooccurring))
gate(
    len(cooccurring) == 15168 and separated_pairs == len(cooccurring),
    "base.geometry",
    "all {0} co-occurring piece pairs have an exact integer separating plane; together "
    "with 24 normalized-unit pieces this certifies every returned cover as a geometric "
    "dissection".format(len(cooccurring)),
)

dep_population = C736_RECEIPT.get("population", {})
dep_responses = C736_RECEIPT.get("responses", {})
gate(
    C736_RECEIPT.get("schema") == "physical-cell-cutting-charge-space-cycle736-v2"
    and C736_RECEIPT.get("status") == "pass"
    and C736_RECEIPT.get("claim_type") == "bounded_theorem"
    and C736_RECEIPT.get("gates", {}).get("fail") == 0
    and dep_population.get("geometric_cuttings") == len(SOL)
    and dep_population.get("used_pieces") == len(USED)
    and dep_responses.get("induced_charge_count") == 8
    and dep_responses.get("induced_charge_rank") == 3
    and dep_responses.get("constant_charge_count") == 2,
    "dep.cycle736",
    "Cycle 736 binds the same supplied geometric population and the complete "
    "eight-reading rank-three induced GF(2) function space",
)

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

dep_table = dep_responses.get("charge_table", {})
gate(
    len(NUL) == 107 and len(BAS) == 3 and len(FUN) == 8
    and HITS == {"four": 2, "six": 2, "seven": 2}
    and sorted(int(NAMED[name].sum()) for name in NAMED) == [5664, 7424, 7704]
    and sorted(dep_table.get("four", {}).get("split", [])) == [5664, 10136]
    and sorted(dep_table.get("six", {}).get("split", [])) == [7704, 8096]
    and sorted(dep_table.get("seven", {}).get("split", [])) == [7424, 8376],
    "dep.responses",
    "the locally reconstructed dimension-three function space has eight readings, two "
    "constants, and exactly the three Cycle 736 nonconstant complement pairs",
)

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

# ------------------------------------------------- Part 4: the complete even-split sweep


def combo_array(n, k):
    if k == 0:
        return np.zeros((1, 0), dtype=np.int16)
    cnt = math.comb(n, k)
    it = itertools.chain.from_iterable(itertools.combinations(range(n), k))
    return np.fromiter(it, dtype=np.int16, count=cnt * k).reshape(-1, k)


def syn_of(cols, cmb):
    lo = np.zeros(len(cmb), dtype=np.uint64)
    hi = np.zeros(len(cmb), dtype=np.uint64)
    for j in range(cmb.shape[1]):
        cc = cols[cmb[:, j].astype(np.int64)]
        lo ^= slo[cc]
        hi ^= shi[cc]
    return lo, hi


def side_tables(cols, kmax):
    tabs = {}
    for k in range(kmax + 1):
        cmb = combo_array(len(cols), k)
        lo, hi = syn_of(cols, cmb)
        order = np.argsort(lo, kind="stable")
        tabs[k] = (lo[order], hi[order], cmb[order])
    return tabs


def lexk(cols, k):
    n = len(cols)
    cmb = combo_array(n, k)
    lo, hi = syn_of(cols, cmb)
    start = [math.comb(n, k) - math.comb(n - s, k) for s in range(n - k + 1)]
    return lo, hi, cmb, start


def combined_light(tab, tlist):
    lo, hi, cmb = tab
    parts = []
    for t in tlist:
        tlo, thi = TS[t]
        parts.append((lo ^ tlo, hi ^ thi,
                      np.full(len(lo), t, dtype=np.int64),
                      np.arange(len(lo), dtype=np.int64)))
    clo = np.concatenate([p[0] for p in parts])
    chi = np.concatenate([p[1] for p in parts])
    ct = np.concatenate([p[2] for p in parts])
    ci = np.concatenate([p[3] for p in parts])
    o = np.argsort(clo, kind="stable")
    return clo[o], chi[o], ct[o], ci[o], cmb


def stream_multi(cols, lx, ctab, light_cols, h, tk, sink):
    """weight-h heavy support in cols vs combined light table; exact, all targets."""
    xlo, xhi, xcmb, xstart = lx
    clo, chi, ct, ci, lcmb = ctab
    n = len(cols)
    for pre in itertools.combinations(range(n), h - tk):
        s = pre[-1] + 1 if pre else 0
        if s > n - tk:
            continue
        st = xstart[s]
        plo, phi = np.uint64(0), np.uint64(0)
        for p in pre:
            plo = plo ^ slo[cols[p]]
            phi = phi ^ shi[cols[p]]
        q = xlo[st:] ^ plo
        left = np.searchsorted(clo, q, side="left")
        right = np.searchsorted(clo, q, side="right")
        cnt = right - left
        hq = np.flatnonzero(cnt > 0)
        if hq.size == 0:
            continue
        ch = cnt[hq]
        tot = int(ch.sum())
        li = np.repeat(left[hq], ch) + (np.arange(tot, dtype=np.int64)
                                        - np.repeat(np.cumsum(ch) - ch, ch))
        qi = np.repeat(hq, ch)
        good = chi[li] == (xhi[st:][qi] ^ phi)
        for u, v in zip(li[good].tolist(), qi[good].tolist()):
            t = int(ct[u])
            supp = ([int(cols[p]) for p in pre]
                    + cols[xcmb[st + v].astype(np.int64)].tolist()
                    + light_cols[lcmb[int(ci[u])].astype(np.int64)].tolist())
            sink[t].append(tuple(sorted(supp)))


def pair_multi(tabA, colsA, tabB, colsB, tlist, sink):
    la, ha, ca = tabA
    lb, hb, cb = tabB
    for t in tlist:
        tlo, thi = TS[t]
        q = lb ^ tlo
        left = np.searchsorted(la, q, side="left")
        right = np.searchsorted(la, q, side="right")
        cnt = right - left
        hq = np.flatnonzero(cnt > 0)
        if hq.size == 0:
            continue
        ch = cnt[hq]
        tot = int(ch.sum())
        li = np.repeat(left[hq], ch) + (np.arange(tot, dtype=np.int64)
                                        - np.repeat(np.cumsum(ch) - ch, ch))
        qi = np.repeat(hq, ch)
        good = ha[li] == (hb[qi] ^ thi)
        for u, v in zip(li[good].tolist(), qi[good].tolist()):
            supp = (colsA[ca[u].astype(np.int64)].tolist()
                    + colsB[cb[v].astype(np.int64)].tolist())
            sink[t].append(tuple(sorted(supp)))


def in_half_multi(cols96, m, tlist, sink):
    """all weight-m solutions supported inside one 96-column half; all quarter splits."""
    qa, qb = cols96[:48], cols96[48:]
    ta = side_tables(qa, min(4, m))
    tb = side_tables(qb, min(4, m))
    la4 = lexk(qa, 4)
    lb4 = lexk(qb, 4)
    la5 = lexk(qa, 5) if m >= 7 else None
    lb5 = lexk(qb, 5) if m >= 7 else None
    for k1 in range(0, m + 1):
        k2 = m - k1
        if k1 > 8 or k2 > 8:
            continue
        if k1 <= 4 and k2 <= 4:
            pair_multi(ta[k1], qa, tb[k2], qb, tlist, sink)
        elif k1 >= 5:
            lx, tk = (la4, 4) if k1 <= 6 else (la5, 5)
            stream_multi(qa, lx, combined_light(tb[k2], tlist), qb, k1, tk, sink)
        else:
            lx, tk = (lb4, 4) if k2 <= 6 else (lb5, 5)
            stream_multi(qb, lx, combined_light(ta[k1], tlist), qa, k2, tk, sink)


HL = np.arange(95, -1, -1, dtype=np.int64)
HR = np.arange(191, 95, -1, dtype=np.int64)
TL = side_tables(HL, 4)
TR = side_tables(HR, 4)
XL4 = lexk(HL, 4)
XR4 = lexk(HR, 4)

ALL = list(range(NT))
FOUND = {t: {} for t in ALL}
DUP = True
for m in (2, 4, 6, 8):
    sink = {t: [] for t in ALL}
    for a in (0, 2, 4):
        b = m - a
        if 0 <= b <= 4:
            pair_multi(TL[a], HL, TR[b], HR, ALL, sink)
    if m >= 6:
        b = m - 6
        stream_multi(HL, XL4, combined_light(TR[b], ALL), HR, 6, 4, sink)
        stream_multi(HR, XR4, combined_light(TL[b], ALL), HL, 6, 4, sink)
    if m == 8:
        in_half_multi(HL, 8, ALL, sink)
        in_half_multi(HR, 8, ALL, sink)
    for t in ALL:
        got = sink[t]
        DUP = DUP and len(set(got)) == len(got)
        if got:
            FOUND[t][m] = sorted(set(got))


def verall(sols, f):
    """does every listed set of pieces reproduce f on all NS cuttings"""
    ok = True
    fl = f.astype(np.int64)[:, None]
    for i in range(0, len(sols), 256):
        blk = sols[i:i + 256]
        W = np.zeros((NPO, len(blk)), dtype=np.int64)
        for r, s in enumerate(blk):
            W[list(s), r] = 1
        ok = ok and bool((((INCL @ W) & 1) == fl).all())
    return ok


def splits(sols):
    """how the sets divide between the two halves"""
    h = {}
    for s in sols:
        a = sum(1 for x in s if x < 96)
        h[(a, len(s) - a)] = h.get((a, len(s) - a), 0) + 1
    return sorted(h.items())


VOK = True
for t in ALL:
    for m in sorted(FOUND[t]):
        VOK = VOK and verall(FOUND[t][m], TGT[t][1])

S0 = FOUND[0].get(8, [])
S1 = FOUND[1].get(8, [])
gate(sorted(FOUND[0]) == [8] and len(S0) == 648 and DUP
     and splits(S0) == [((0, 8), 42), ((2, 6), 240), ((4, 4), 204), ((8, 0), 162)],
     "sweep.zero",
     "no set of {0}, {1} or {2} pieces sums to zero; at {3} there are exactly {4}, "
     "splitting {5}".format(2, 4, 6, 8, len(S0), splits(S0)))
gate(sorted(FOUND[1]) == [8] and len(S1) == 192
     and splits(S1) == [((2, 6), 96), ((4, 4), 48), ((8, 0), 48)], "sweep.one",
     "the all-ones reading needs {0} pieces too, none at {1}, {2} or {3}; there are "
     "exactly {4}, splitting {5}".format(8, 2, 4, 6, len(S1), splits(S1)))
gate(all(not FOUND[t] for t in range(2, 8)), "sweep.nonconstant",
     "four, four-flip, six, six-flip, seven and seven-flip are carried by no support of {0}, "
     "{1}, {2} or {3} pieces; parity bars odd sizes, so each needs at least {4}".format(
         2, 4, 6, 8, 10))
gate(VOK and DUP, "sweep.ver",
     "every set of pieces the sweep found reproduces its own reading on all {0} cuttings, "
     "and no set was found twice".format(NS))
POK = [tuple(sorted(psupp)) in set(FOUND[8 + k].get(len(psupp), []))
       for k, (pname, psupp) in enumerate(PLANT)]
gate(POK == [True] * 4, "sweep.plant",
     "planted sets of {0}, {1}, {2} and {3} pieces, one in each search class, are all "
     "recovered: {4}".format(4, 8, 8, 8, POK))

# --------------------------------------------- Part 5: orbits of the two octet families

ORB = {}
for t in (0, 1):
    sols = FOUND[t][8]
    sset = set(sols)
    left_ = set(sols)
    sizes = []
    closed = True
    while left_:
        s = min(left_)
        o = set()
        for cp in CP:
            o.add(tuple(sorted(int(cp[x]) for x in s)))
        closed = closed and o <= sset
        sizes.append(len(o))
        left_ -= o
    cover = len(set(x for s in sols for x in s))
    ORB[t] = (sorted(sizes), closed, cover)

sz0, cl0, cv0 = ORB[0]
gate(len(sz0) == 22 and sz0.count(24) == 17 and sz0.count(48) == 5 and cl0 and cv0 == NPO,
     "orb.zero",
     "the {0} octets summing to zero form {1} orbits under the {2} symmetries, {3} of size "
     "{4} and {5} of size {6}, closed under the action and together using all {7} "
     "pieces".format(len(S0), len(sz0), len(G), 17, 24, 5, 48, cv0))
sz1, cl1, cv1 = ORB[1]
gate(sz1 == [24, 24, 48, 48, 48] and cl1 and cv1 == NPO, "orb.one",
     "the {0} octets reading all-ones form {1} orbits of sizes {2}, closed under the "
     "action and together using all {3} pieces".format(len(S1), len(sz1), sz1, cv1))

SPR = {}
for t in (0, 1):
    h = {}
    for s in FOUND[t][8]:
        key = tuple(sorted(int(x) for x in np.bincount(lab[list(s)], minlength=NORB)))
        h[key] = h.get(key, 0) + 1
    SPR[t] = sorted(h.items())
gate(SPR[0] == [((0, 0, 4, 4), 120), ((0, 2, 2, 4), 48), ((1, 1, 3, 3), 192),
                ((2, 2, 2, 2), 288)], "orb.spread.zero",
     "across the four orbits of pieces the octets summing to zero spread as {0}, each "
     "spread the ordered counts smallest first".format(SPR[0]))
gate(SPR[1] == [((0, 0, 4, 4), 48), ((0, 2, 2, 4), 48), ((1, 1, 3, 3), 48),
                ((2, 2, 2, 2), 48)], "orb.spread.one",
     "the all-ones octets spread as {0}, the same four patterns, 48 sets at "
     "each".format(SPR[1]))

# ------------------------------------ Part 6: sets of pieces carrying the six readings

CTUP = [tuple(sorted(int(c) for c in UNI[USED[a]])) for a in range(192)]
assert len(set(CTUP)) == 192
POS = {t: a for a, t in enumerate(CTUP)}

WITS = [
    ("four", 2, 16, (8, 8),
     (3, 7, 27, 42, 58, 61, 82, 95, 108, 124, 128, 143, 158, 172, 180, 188),
     ((0, 1, 2, 6, 14), (0, 1, 3, 4, 12), (0, 2, 3, 7, 15), (0, 4, 5, 7, 8),
      (0, 8, 12, 13, 15), (1, 2, 3, 5, 13), (1, 5, 6, 7, 9), (1, 9, 13, 14, 15),
      (2, 4, 5, 6, 10), (2, 10, 12, 13, 14), (3, 4, 6, 7, 11), (3, 11, 12, 14, 15),
      (4, 8, 9, 11, 12), (5, 9, 10, 11, 13), (6, 8, 9, 10, 14), (7, 8, 10, 11, 15))),
    ("four-flip", 3, 20, (10, 10),
     (0, 6, 26, 43, 53, 56, 62, 85, 89, 92, 113, 118, 120, 131, 136, 138, 145, 152,
      167, 169),
     ((0, 1, 2, 5, 10), (0, 1, 3, 4, 11), (0, 2, 3, 7, 8), (0, 4, 5, 7, 15),
      (0, 4, 12, 14, 15), (0, 8, 10, 11, 15), (1, 2, 3, 6, 9), (1, 5, 7, 14, 15),
      (1, 5, 13, 14, 15), (1, 9, 10, 11, 14), (2, 5, 6, 7, 13), (2, 6, 12, 13, 14),
      (2, 8, 9, 10, 13), (3, 5, 7, 12, 13), (3, 7, 12, 13, 15), (3, 8, 9, 11, 12),
      (4, 5, 6, 10, 14), (4, 6, 7, 8, 12), (5, 7, 8, 12, 13), (5, 7, 10, 14, 15))),
    ("six", 4, 24, (12, 12),
     (2, 21, 22, 25, 27, 30, 38, 41, 43, 50, 84, 88, 98, 118, 127, 132, 140, 141, 163,
      164, 169, 172, 177, 182),
     ((0, 1, 2, 6, 9), (0, 1, 8, 12, 14), (0, 1, 9, 11, 15), (0, 2, 3, 4, 12),
      (0, 2, 3, 7, 15), (0, 2, 4, 5, 10), (0, 2, 8, 9, 13), (0, 2, 10, 14, 15),
      (0, 4, 5, 7, 15), (0, 4, 8, 9, 11), (1, 5, 7, 8, 9), (1, 5, 12, 13, 14),
      (2, 3, 5, 7, 10), (2, 6, 12, 13, 14), (3, 4, 5, 7, 12), (3, 6, 7, 9, 11),
      (3, 9, 11, 12, 13), (3, 10, 11, 12, 14), (4, 11, 12, 14, 15), (5, 6, 7, 9, 13),
      (5, 7, 10, 14, 15), (5, 9, 10, 11, 13), (6, 7, 8, 12, 14), (6, 9, 10, 11, 14))),
    ("six-flip", 5, 24, (12, 12),
     (0, 10, 11, 31, 34, 56, 58, 63, 80, 81, 84, 85, 96, 98 + 1, 116, 119, 139, 142,
      154, 157, 172, 174, 177, 178),
     ((0, 1, 2, 5, 10), (0, 1, 3, 8, 12), (0, 1, 3, 11, 15), (0, 2, 4, 5, 13),
      (0, 2, 6, 7, 8), (0, 8, 10, 11, 15), (0, 8, 12, 13, 15), (1, 2, 3, 6, 14),
      (1, 4, 5, 9, 11), (1, 4, 5, 12, 14), (1, 5, 7, 8, 9), (1, 5, 7, 14, 15),
      (2, 3, 4, 6, 11), (2, 3, 5, 7, 13), (2, 6, 8, 9, 10), (2, 6, 13, 14, 15),
      (3, 8, 10, 11, 12), (3, 11, 12, 13, 15), (4, 6, 8, 9, 12), (4, 6, 11, 14, 15),
      (5, 9, 10, 11, 13), (5, 10, 12, 13, 14), (6, 7, 8, 12, 14), (6, 7, 9, 11, 15))),
    ("seven", 6, 30, (16, 14),
     (3, 6, 9, 16, 28, 29, 34, 45, 48, 49, 56, 63, 69, 82, 87, 94, 97, 125, 126, 132,
      133, 138, 144, 150, 158, 168, 170, 171, 184, 188),
     ((0, 1, 2, 6, 14), (0, 1, 3, 4, 11), (0, 1, 3, 7, 15), (0, 1, 5, 7, 8),
      (0, 2, 3, 8, 12), (0, 2, 3, 11, 15), (0, 2, 6, 7, 8), (0, 4, 5, 13, 15),
      (0, 4, 6, 8, 9), (0, 4, 6, 14, 15), (0, 8, 10, 11, 15), (1, 2, 3, 6, 14),
      (1, 3, 5, 12, 13), (1, 5, 6, 7, 9), (1, 5, 9, 10, 11), (1, 9, 12, 13, 14),
      (2, 3, 4, 6, 12), (2, 10, 13, 14, 15), (3, 4, 5, 7, 11), (3, 6, 7, 9, 11),
      (3, 6, 7, 12, 14), (3, 8, 9, 11, 12), (4, 5, 6, 9, 13), (4, 5, 10, 12, 14),
      (4, 8, 9, 11, 12), (5, 7, 10, 11, 15), (5, 8, 9, 10, 13), (5, 8, 10, 12, 13),
      (6, 9, 12, 13, 14), (7, 8, 10, 11, 15))),
    ("seven-flip", 7, 30, (14, 16),
     (4, 5, 15, 19, 32, 36, 46, 47, 52, 56, 69, 73, 87, 94, 98, 100, 110, 125, 126,
      127, 136, 138, 148, 150, 157, 164, 177, 180, 186, 189),
     ((0, 1, 2, 9, 13), (0, 1, 2, 10, 14), (0, 1, 4, 12, 14), (0, 1, 5, 13, 15),
      (0, 2, 4, 10, 11), (0, 2, 6, 8, 9), (0, 4, 6, 7, 8), (0, 4, 6, 7, 15),
      (0, 4, 12, 13, 15), (0, 8, 10, 11, 15), (1, 3, 5, 12, 13), (1, 3, 7, 14, 15),
      (1, 5, 9, 10, 11), (1, 9, 12, 13, 14), (2, 3, 5, 7, 10), (2, 3, 6, 9, 11),
      (2, 4, 6, 10, 11), (2, 10, 13, 14, 15), (3, 4, 5, 7, 11), (3, 4, 5, 7, 12),
      (3, 7, 12, 13, 15), (3, 8, 9, 11, 12), (4, 5, 8, 10, 12), (4, 5, 10, 12, 14),
      (4, 6, 11, 14, 15), (5, 6, 7, 9, 13), (6, 7, 8, 12, 14), (6, 8, 9, 10, 14),
      (7, 8, 9, 11, 15), (7, 8, 10, 14, 15))),
]

for wname, wt, wsz, wsp, WSUPP, WCORN in WITS:
    assert tuple(POS[t] for t in WCORN) == WSUPP, "the corner encoding must pin the order"
    wv = (INCL[:, list(WSUPP)].sum(axis=1) & 1).astype(np.uint8)
    ver = bool(np.array_equal(wv, TGT[wt][1]))
    a = sum(1 for x in WSUPP if x < 96)
    sp = (a, len(WSUPP) - a)
    gate(len(WSUPP) == wsz and (wsz & 1) == 0 and wsz >= 10 and ver and sp == wsp,
         "wit." + wname,
         "{0}: size {1}, verified {2}, split {3}".format(wname, len(WSUPP), ver, sp))

# ---------------------------------------------------------------- Part 7: separations

d4 = sorted(KEY[4])
KSUP = [tuple(c for c in range(NPO) if (msk >> c) & 1) for msk in d4]
KPC = sorted(set(len(s) for s in KSUP))
KW = np.zeros((NPO, len(KSUP)), dtype=np.int64)
for r, s in enumerate(KSUP):
    KW[list(s), r] = 1
KNUL = int((((INCL @ KW) & 1).sum(axis=0) == 0).sum())
KOVR = len(set(KSUP) & set(S0))
gate(len(d4) == 120 and KPC == [8] and KNUL == 0 and KOVR == 0, "sep.move",
     "the {0} smallest exchanges each replace {1} pieces, {2} of them sum to zero, and "
     "{3} of them are among the {4} octets".format(
         len(d4), KPC[0], KNUL, KOVR, len(S0)))

f4, f6, f7 = NAMED["four"], NAMED["six"], NAMED["seven"]
ID1 = bool(np.array_equal(f4 ^ f6 ^ f7, ONE))
ID2 = not bool(np.array_equal(f4, f6 ^ f7))
gate(ID1 and ID2, "sep.fun",
     "four is six added to seven and then flipped, on all {0} cuttings, and differs from "
     "six added to seven somewhere".format(NS))

# ------------------------------------------------------------- Part 8: octet geometry

CORN2 = [frozenset(int(c) for c in UNI[USED[a]]) for a in range(NPO)]
thrc = [sum(1 for s in CORN2 if c in s) for c in range(16)]
tedge = [sum(1 for s in CORN2 if frozenset([v, v ^ 1]) <= s) for v in range(0, 16, 2)]
sedge = {}
for b in (2, 4, 8):
    for v in range(16):
        if (v & b) == 0:
            n = sum(1 for s in CORN2 if frozenset([v, v | b]) <= s)
            sedge[n] = sedge.get(n, 0) + 1
gate(sorted(set(thrc)) == [60] and 16 * 60 == 5 * NPO and sorted(set(tedge)) == [24]
     and len(tedge) == 8 and sorted(sedge.items()) == [(24, 24)], "geo.corner",
     "each of the 16 corners lies in {0} of the {1} pieces, 16 times {0} being 5 times "
     "{1}; each of the {2} tick edges lies in {3}, and the spatial edges give {4}".format(
         thrc[0], NPO, len(tedge), tedge[0], sorted(sedge.items())))


def octgeo(sols):
    """corner intersections, unions and shared-pair statistics of a family of octets"""
    ih, uh, dh, vh, pm, xh = {}, {}, {}, {}, {}, {}
    for s in sols:
        inter = CORN2[s[0]]
        union = CORN2[s[0]]
        for c in s[1:]:
            inter = inter & CORN2[c]
            union = union | CORN2[c]
        ih[len(inter)] = ih.get(len(inter), 0) + 1
        uh[len(union)] = uh.get(len(union), 0) + 1
        if len(inter) != 2:
            continue
        u, v = sorted(inter)
        d = bin(u ^ v).count("1")
        dh[d] = dh.get(d, 0) + 1
        vh[u ^ v] = vh.get(u ^ v, 0) + 1
        pm[(u, v)] = pm.get((u, v), 0) + 1
        xh[(d, len(union))] = xh.get((d, len(union)), 0) + 1
    return ih, uh, dh, vh, pm, xh


IH0, UH0, DH0, VH0, PM0, XH0 = octgeo(S0)
IH1, UH1, DH1, VH1, PM1, XH1 = octgeo(S1)
gate(sorted(IH0.items()) == [(2, 648)] and sorted(IH1.items()) == [(2, 192)],
     "geo.inter",
     "the eight pieces of an octet share exactly two corners: sizes {0} for the octets "
     "summing to zero and {1} for the all-ones octets".format(
         sorted(IH0.items()), sorted(IH1.items())))
gate(sorted(UH0.items()) == [(10, 240), (12, 120), (16, 288)]
     and sorted(UH1.items()) == [(16, 192)], "geo.union",
     "corners the eight pieces cover between them: zero octets {0}, all-ones octets "
     "{1}".format(sorted(UH0.items()), sorted(UH1.items())))
MH1 = {}
for key in PM1:
    MH1[PM1[key]] = MH1.get(PM1[key], 0) + 1
gate(sorted(DH1.items()) == [(1, 192)]
     and sorted(VH1.items()) == [(1, 48), (2, 48), (4, 48), (8, 48)]
     and len(PM1) == 32 and sorted(MH1.items()) == [(6, 32)], "geo.odd",
     "the two corners an all-ones octet shares are always a cell edge: distances {0}, "
     "directions {1}, and the {2} edges each carried {3} times, {4}".format(
         sorted(DH1.items()), sorted(VH1.items()), len(PM1), 6, sorted(MH1.items())))
MD0 = {}
for (u, v) in PM0:
    MD0.setdefault(bin(u ^ v).count("1"), set()).add(PM0[(u, v)])
MSET = [sorted(MD0[d])[0] for d in (1, 2, 3, 4)]
NPD = [sum(1 for (u, v) in PM0 if bin(u ^ v).count("1") == d) for d in (1, 2, 3, 4)]
gate(sorted(DH0.items()) == [(1, 288), (2, 144), (3, 96), (4, 120)] and len(PM0) == 120
     and all(len(MD0[d]) == 1 for d in (1, 2, 3, 4)) and MSET == [9, 3, 3, 15]
     and NPD == [32, 48, 32, 8]
     and sum(NPD[i] * MSET[i] for i in range(4)) == len(S0), "geo.even.d",
     "the pairs zero octets share run over all {0} corner pairs, distances {1}, and at "
     "each distance a single multiplicity: {2}, {3}, {4} and {5}".format(
         len(PM0), sorted(DH0.items()), MSET[0], MSET[1], MSET[2], MSET[3]))
gate(sorted(XH0.items()) == [((1, 12), 96), ((1, 16), 192), ((2, 10), 144),
                             ((3, 10), 96), ((4, 12), 24), ((4, 16), 96)], "geo.even.x",
     "distance against corners covered, for the zero octets: {0}".format(
         sorted(XH0.items())))

bad_support = S0[0][1:]
gate(not verall([bad_support], ZERO), "hostile.support",
     "deleting one piece from a certified zero octet destroys the full-table identity")
bad_dependency = json.loads(json.dumps(C736_RECEIPT))
bad_dependency["status"] = "fail"
gate(not (bad_dependency.get("status") == "pass"
              and bad_dependency.get("gates", {}).get("fail") == 0),
     "hostile.dependency",
     "a failed direct-dependency receipt cannot satisfy the acceptance predicate")

overlap_control = next(
    ((left, right) for left in MINP for right in MINP
     if left < right and not (MASK[left] & MASK[right])
     and separated((left, right))[0] == 0),
    None,
)
gate(overlap_control is not None, "hostile.sample_geometry",
     "sample-disjoint declared pieces can overlap, so the exact separator gate is "
     "load-bearing")

print("")
print("per_element: checked -- all 192 used pieces enter the exact incidence, response, "
      "support-search, orbit, and corner-geometry censuses", flush=True)
print("per_site: checked -- one supplied 16-corner coordinate cell only; no physical "
      "assembly-cell or framework site identification is executed", flush=True)
print("per_mode: checked and not executed -- the finite cutting incidence system has no "
      "field, spectral, or momentum-mode decomposition", flush=True)
print("per_block: checked -- all 15,800 geometric cuttings and every used-piece support "
      "of cardinality at most eight under the certified split search", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell, arbitrary-domain, "
      "thermodynamic, boundary, or continuum negative is asserted", flush=True)

packed_incidence_rows = [bytes(row) for row in np.packbits(INC, axis=1)]
canonical_incidence_rows = sorted(packed_incidence_rows)


def canonical_reading_hash(function):
    pairs = sorted(zip(packed_incidence_rows, (int(bit) for bit in function)))
    return hashlib.sha256(
        b"".join(row + bytes((bit,)) for row, bit in pairs)
    ).hexdigest()


reading_identity = {
    "incidence_packbits_sha256": hashlib.sha256(
        np.packbits(INC, axis=1).tobytes()
    ).hexdigest(),
    "canonical_incidence_rows_sha256": hashlib.sha256(
        b"".join(canonical_incidence_rows)
    ).hexdigest(),
    "support_column_order_sha256": hashlib.sha256(
        json.dumps(CTUP, separators=(",", ":")).encode("utf-8")
    ).hexdigest(),
    "functions": {
        name: {
            "ones": int(function.sum()),
            "packbits_sha256": hashlib.sha256(
                np.packbits(function).tobytes()
            ).hexdigest(),
            "canonical_rows_with_bit_sha256": canonical_reading_hash(function),
        }
        for name, function in TGT[:8]
    },
}
primary_identity = PRIMARY_RECEIPT.get("reading_identity", {})
canonical_identity_matches = (
    primary_identity.get("canonical_incidence_rows_sha256")
    == reading_identity["canonical_incidence_rows_sha256"]
    and primary_identity.get("support_column_order_sha256")
    == reading_identity["support_column_order_sha256"]
    and set(primary_identity.get("functions", {}))
    == set(reading_identity["functions"])
    and all(
        primary_identity["functions"][name].get("ones")
        == reading_identity["functions"][name]["ones"]
        and primary_identity["functions"][name].get(
            "canonical_rows_with_bit_sha256"
        )
        == reading_identity["functions"][name]["canonical_rows_with_bit_sha256"]
        for name in reading_identity["functions"]
    )
)
gate(
    PRIMARY_RECEIPT.get("schema")
    == "physical-cell-cutting-least-computing-sets-cycle737-v2"
    and PRIMARY_RECEIPT.get("status") == "pass"
    and PRIMARY_RECEIPT.get("gates", {}).get("fail") == 0
    and PRIMARY_RECEIPT.get("runner_sha256") == file_sha256(PRIMARY_PATH)
    and canonical_identity_matches,
    "dep.primary_receipt",
    "the primary pass receipt binds the current primary bytes and exactly matches the "
    "independently reconstructed row-order-invariant incidence/readings identity; "
    "ordered hashes are retained as traversal-specific provenance",
)

receipt = {
    "schema": "physical-cell-cutting-least-computing-sets-cycle737-independent-v1",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "runner_sha256": file_sha256(
        "scripts/physical_cell_cutting_least_computing_sets_cycle737_"
        "independent_check_2026_08_05.py"
    ),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "supplied_model": {
        "shape": [1, 1, 1, 1],
        "support_universe": "the 192 pieces used by the 15,800 supplied cuttings only",
        "piece_class": "five-corner normalized-volume-one simplices only",
        "cost": "corner pairs with four-coordinate L1 separation greater than one",
        "physical_cell_tick_simplex_reading_bridge": "open",
    },
    "direct_dependency": {
        "cycle": 736,
        "status": C736_RECEIPT.get("status"),
        "geometric_cuttings": NS,
        "used_pieces": NPO,
        "induced_charge_count": len(FUN),
        "induced_charge_rank": len(BAS),
    },
    "population": {
        "geometric_cuttings": NS,
        "cooccurring_pairs_exactly_separated": len(cooccurring),
        "used_pieces": NPO,
        "pieces_per_cutting": 24,
        "uses_per_piece": int(csum.min()),
        "incidence_rank": len(I88),
    },
    "complete_support_sweep": {
        "maximum_cardinality": 8,
        "cardinalities_checked": [2, 4, 6, 8],
        "odd_cardinalities_excluded_by_parity": True,
        "zero_octets": len(S0),
        "one_octets": len(S1),
        "nonconstant_reading_minimum_lower_bound": 10,
        "nonconstant_readings": 6,
        "duplicate_free": DUP,
    },
    "reading_identity": reading_identity,
    "verified_upper_witnesses": {
        name: {
            "size": size,
            "support_indices_0_to_191": list(support),
            "support_corner_tuples": [list(corners) for corners in corner_tuples],
        }
        for name, _target, size, _split, support, corner_tuples in WITS
    },
    "octet_families": {
        "zero_orbit_sizes": sz0,
        "one_orbit_sizes": sz1,
        "shared_corners_per_octet": 2,
        "one_octets_per_edge": 6,
        "one_octet_edges": len(PM1),
        "exchange_overlap_with_zero_octets": KOVR,
    },
    "no_go_discipline": {
        "status": "PASS",
        "claim_scope": "complete support search through cardinality eight in the fixed "
        "192-column finite incidence system only",
        "n5_certificate": "five resolution lines in primary stdout and canonical cache",
    },
    "gates": {
        "pass": PF[0],
        "fail": PF[1],
        "named": {name: "PASS" if ok else "FAIL" for name, ok in GATES},
    },
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]), flush=True)
sys.exit(0 if PF[1] == 0 else 1)
