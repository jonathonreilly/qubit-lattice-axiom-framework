"""Cycle 736: the charges the cell's least-cost cuttings carry, listed in full.

The single cell is the unit four-cube with three lattice directions and one tick. Cutting
it into pieces of least volume at the floor of the adjacency cost admits many answers; a
move between two of them replaces some pieces by the same number of others. This runner
asks which weights on the pieces answer a move size uniformly, lists every charge such a
weight can put on the population, and identifies the one charge that keeps the smallest
move with the indicator of a single symmetry orbit of groups.

Class-A: integer and field-with-two-elements arithmetic on a finite explicit object, no
solver. Every count below is measured here.  The unit-cell/tick graining, corner-simplex
domain, declared four-coordinate L1 charge, and 48-element symmetry action are supplied
finite-model inputs rather than consequences of the framework axioms.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md",
    "scripts/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.py",
    "scripts/physical_column_family_parity_law_forced_orbits_cycle733_independent_check_2026_08_04.py",
    "outputs/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04_receipt_2026-08-04.json",
)
ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_"
    "receipt_2026-08-05.json"
)


def file_sha256(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


C733_RECEIPT = json.loads((ROOT / AUDIT_INPUT_PATHS[-1]).read_text(encoding="utf-8"))

PF = [0, 0]
WORD = {4: "four", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail)


def sec(text):
    print("")
    print(text)


gate(
    C733_RECEIPT.get("claim_type") == "bounded_theorem"
    and C733_RECEIPT.get("totals", {}).get("fail") == 0
    and C733_RECEIPT.get("minimum", {}).get("dissections") == 15800
    and C733_RECEIPT.get("minimum", {}).get("used_pieces") == 192
    and C733_RECEIPT.get("minimum", {}).get("geometric_representatives") == 391
    and C733_RECEIPT.get("minimum", {}).get("geometric_pair_checks") == 107916,
    "dep.c733",
    "Cycle 733 binds the supplied finite model and independently certified geometric "
    "population used here",
)


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
INV_OK = bool(np.array_equal(MM @ IV, np.broadcast_to(np.eye(4, dtype=np.int64), MM.shape)))

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
PP = []
for (_, _, g) in G:
    PP.append(np.array([
        posp[tuple(sorted(int(g[c]) for c in UNI[i]))]
        for i in range(NPIECE)
    ], dtype=np.int32))
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

sec("the cuttings of the cell at the floor of the cost")
gate(len(SUB) == 4368 and NPIECE == 2672 and NQ == 2736 and coll == 0 and face == 0
     and CB == 3 and SB == 12810 and len(G) == 48 and NORB == 57 and INV_OK, "base.cell",
     "{0} five-subsets of the 16 corners give {1} pieces of least volume, carrying {2} "
     "sample points with no collision and {3} on a boundary; the declared action has {4} symmetries "
     "and the pieces {5} orbits".format(len(SUB), NPIECE, NQ, face, len(G), NORB))

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

# Finite sample coverage is only a search accelerator.  Exact separating-facet
# certificates establish that one representative of every supplied-symmetry orbit is a
# geometric dissection; symmetry then transports the certificate to the full population.
NEG = [np.array(t, dtype=np.int64)
       for t in itertools.product((-1, 0, 1), repeat=4) if any(t)]


def separated(indices):
    pts = [V[UNI[i]] for i in indices]
    facets = []
    for i in indices:
        inv = IV[i]
        facets.append([inv[k] for k in range(4)] + [-inv.sum(axis=0)])
    good, total = 0, 0
    for a in range(len(indices)):
        for b in range(a + 1, len(indices)):
            total += 1
            for normal in NEG + facets[a] + facets[b]:
                left, right = pts[a] @ normal, pts[b] @ normal
                if int(left.max()) <= int(right.min()) or int(right.max()) <= int(left.min()):
                    good += 1
                    break
    return good, total


SOLSET = set(SOL)
GEO_SEEN, GEO_REPS, GEO_PAIRS = set(), 0, 0
GEO_OK = True
for solution in SOL:
    if solution in GEO_SEEN:
        continue
    GEO_REPS += 1
    good, total = separated(solution)
    GEO_PAIRS += total
    GEO_OK = GEO_OK and good == total and len(solution) == 24
    for perm in PP:
        image = tuple(sorted(int(perm[i]) for i in solution))
        GEO_OK = GEO_OK and image in SOLSET
        GEO_SEEN.add(image)
gate(LO == 6 and len(MINP) == 400 and NODE[0] == 502838 and NS == 15800
     and FULL == set([24]) and NPO == 192 and GEO_OK and GEO_REPS == 391
     and GEO_PAIRS == 107916 and len(GEO_SEEN) == NS, "base.floor",
     "a complete search over the {0} pieces of least cost {1} visits {2} nodes and finds "
     "{3} exact geometric cuttings of {4} pieces each, between them using {5} pieces; "
     "{6} orbit representatives pass {7} exact pair-separation checks".format(
         len(MINP), LO, NODE[0], NS, 24, NPO, GEO_REPS, GEO_PAIRS))

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
NMOVE = dict((k, int(EA[k].size)) for k in SZC)
NDIST = dict((k, len(KEY[k])) for k in SZG)
DEG = np.zeros(NS, dtype=np.int64)
for k in [4, 6, 7, 8]:
    np.add.at(DEG, EA[k], 1)
    np.add.at(DEG, EB[k], 1)
CORE = np.flatnonzero(DEG == 0)

sec("moves between cuttings, counted by how many pieces they replace")
gate([NMOVE[k] for k in SZC] == [46128, 0, 31968, 60096, 151704, 119808, 281376]
     and [NDIST[k] for k in SZG] == [120, 528, 1152, 4212, 6144, 25248], "move.size",
     "moves replacing four, five, six, seven, eight, nine and ten pieces number {0}, {1}, "
     "{2}, {3}, {4}, {5} and {6}, drawn from {7}, {8}, {9}, {10}, {11} and {12} distinct "
     "exchanges in this independently reconstructed population".format(
         *([NMOVE[k] for k in SZC] + [NDIST[k] for k in SZG])))


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


DALL = basis(BITS[i] ^ BITS[0] for i in range(1, NS))
RKP = len(DALL) + (0 if inspan(BITS[0], DALL) else 1)
TK, SK = {}, {}
for k in SZG:
    TK[k] = rref(s ^ KEY[k][0] for s in KEY[k][1:])
    SK[k] = len(TK[k]) + (0 if inspan(KEY[k][0], TK[k]) else 1)
OUT7 = [v for v in DALL.values() if not inspan(v, TK[7])]
gate(RKP == 88 and len(DALL) == 87 and [len(TK[k]) for k in SZG] == [85, 86, 86, 87, 87, 87]
     and [SK[k] for k in SZG] == [86, 86, 86, 87, 87, 87] and len(OUT7) > 0, "span.pop",
     "the {0} cuttings span {1} dimensions and their differences {2}; the exchange "
     "differences span {3} at four rising to {4} at eight, nine and ten, and a population "
     "difference lying outside the seven-piece span is exhibited".format(
         NS, RKP, len(DALL), len(TK[4]), len(TK[8])))


def oddzero(keys):
    """an odd family of exchanges summing to zero, or None when a weight can reverse"""
    tag = 1 << NPO
    piv, src = {}, {}
    for n, s in enumerate(keys):
        r = s | tag
        while r:
            h = r.bit_length() - 1
            if h not in piv:
                piv[h] = r
                src[h] = n
                break
            r ^= piv[h]
    if not inspan(tag, piv):
        return None
    piv2 = {}
    for n in sorted(set(src.values())):
        r, pv = keys[n] | tag, 1 << n
        while r:
            h = r.bit_length() - 1
            if h not in piv2:
                piv2[h] = (r, pv)
                break
            r ^= piv2[h][0]
            pv ^= piv2[h][1]
    r, pv = tag, 0
    while r:
        h = r.bit_length() - 1
        assert h in piv2, "the pivot rows must span what the whole family spans"
        r ^= piv2[h][0]
        pv ^= piv2[h][1]
    return [n for n in range(len(keys)) if (pv >> n) & 1]


CERT, COK = {}, True
for k in SZG:
    CERT[k] = oddzero(KEY[k])
    if k == 4:
        COK = COK and CERT[k] is None
    else:
        J = CERT[k]
        x = 0
        for n in J:
            x ^= KEY[k][n]
        COK = COK and x == 0 and (len(J) & 1) == 1

NUL = perp(TK[4], NPO)
WIT = None
for w in NUL:
    if (bin(w & KEY[4][0]).count("1") & 1) == 1:
        WIT = w
        break
WV = np.zeros(NPO, dtype=np.int64)
for j in range(NPO):
    if ((WIT >> j) & 1) == 1:
        WV[j] = 1
RW = (INCL @ WV) & 1
FLIP4 = int((RW[EA[4]] != RW[EB[4]]).sum())

sec("which uniform answers a weight on the pieces can give")
gate(COK and WIT is not None and FLIP4 == NMOVE[4], "resp.rev",
     "a weight is exhibited whose reading changes across every one of the {0} smallest "
     "moves; at six, seven, eight, nine and ten a family of {1}, {2}, {3}, {4} and {5} "
     "exchanges summing to zero is exhibited, each family of odd size, so at those sizes "
     "no weight can change across every move".format(
         FLIP4, *[len(CERT[k]) for k in SZG[1:]]))

IN46 = all(inspan(v, TK[6]) for v in TK[4].values())
IN47 = all(inspan(v, TK[7]) for v in TK[4].values())
N67 = all(inspan(v, TK[7]) for v in TK[6].values())
N76 = all(inspan(v, TK[6]) for v in TK[7].values())
SUM67 = basis(TK[7].values(), dict(TK[6]))
EQ8 = (len(SUM67) == len(TK[8]) and all(inspan(v, TK[8]) for v in SUM67.values())
       and all(inspan(v, TK[9]) for v in TK[8].values())
       and all(inspan(v, TK[10]) for v in TK[9].values())
       and len(TK[8]) == len(TK[9]) and len(TK[9]) == len(TK[10]))
CAP = len(TK[6]) + len(TK[7]) - len(SUM67)
gate(IN46 and IN47 and (not N67) and (not N76) and EQ8 and CAP == len(TK[4]), "resp.lat",
     "the four-piece span sits inside both the six- and the seven-piece span, neither of "
     "which holds the other; their sum is the eight-piece span, itself the nine- and the "
     "ten-piece span, and their meet has dimension {0}, so the four-piece span is exactly "
     "the overlap of the six- and seven-piece spans".format(CAP))

MULTI = []
for mask in range(1, 1 << len(SZG)):
    ks = [k for i, k in enumerate(SZG) if (mask >> i) & 1]
    piv = {}
    for k in ks:
        basis(TK[k].values(), piv)
    lam = 0
    for sub in range(1, 1 << len(ks)):
        r = 0
        for i, k in enumerate(ks):
            if (sub >> i) & 1:
                r ^= KEY[k][0]
        if inspan(r, piv):
            lam += 1
    pat = 1 << (len(ks) - (lam + 1).bit_length() + 1)
    if pat > 1:
        MULTI.append((ks, pat))
MW = [" with ".join(WORD[k] for k in m[0]) for m in MULTI]
gate(len(MULTI) == 3 and [m[0] for m in MULTI] == [[4], [4, 6], [4, 7]]
     and [m[1] for m in MULTI] == [2, 2, 2], "resp.subs",
     "of the {0} non-empty sets of move sizes exactly {1} admit more than one answer "
     "pattern, namely {2}, {3} and {4}, each admitting {5}; every other set, the whole of "
     "them included, admits exactly one".format(
         (1 << len(SZG)) - 1, len(MULTI), MW[0], MW[1], MW[2], MULTI[0][1]))

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
UNIF = all((f[EA[4]] ^ f[EB[4]]).min() == (f[EA[4]] ^ f[EB[4]]).max() for f in FUN)
FLAT = sum(1 for f in FUN if int(f.sum()) in (0, NS))
ROW0 = sorted(TK[4].values())[0]
JBIT = (ROW0 & -ROW0).bit_length() - 1
WB = WV.copy()
WB[JBIT] = 1 - WB[JBIT]
RB = (INCL @ WB) & 1
DB = RB[EA[4]] ^ RB[EB[4]]

sec("the charges the cuttings carry")
gate(len(NUL) == 107 and len(BAS) == 3 and UNIF and FLAT == 2
     and DB.min() != DB.max(), "chg.space",
     "weights answering the smallest move uniformly form a space of dimension {0}; on the "
     "cuttings they induce {1} charges spanning dimension {2}, of which {3} are constant, "
     "and moving the exhibited weight on a single piece destroys uniformity at four".format(
         len(NUL), len(FUN), len(BAS), FLAT))

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
TAB, ONESIDE = {}, True
print("  {0:<8s}{1:>13s}{2:>12s}".format("keeps", "split", "rigid side")
      + "".join("{0:>9s}".format("at " + str(k)) for k in SZG))
for nm in ["four", "six", "seven"]:
    g = NAMED[nm]
    one = int(g.sum())
    row = [int((g[EA[k]] ^ g[EB[k]]).sum()) for k in SZG]
    sv = set(int(v) for v in g[CORE])
    ONESIDE = ONESIDE and len(sv) == 1
    rs = one if sv == set([1]) else NS - one
    TAB[nm] = (one, NS - one, rs, row)
    print("  {0:<8s}{1:>6d}/{2:<6d}{3:>12d}".format(nm, one, NS - one, rs)
          + "".join("{0:>9d}".format(v) for v in row))
gate(len(NAMED) == 3 and sorted(HITS.values()) == [2, 2, 2] and ONESIDE
     and TAB["four"] == (5664, 10136, 10136, [0, 9504, 26880, 32640, 48960, 124224])
     and TAB["six"] == (7704, 8096, 7704, [46128, 0, 26880, 28608, 87552, 190848])
     and TAB["seven"] == (7424, 8376, 8376, [46128, 9504, 0, 21312, 102336, 183744]),
     "chg.table",
     "there are {0} charges up to swapping the two sides, one keeping each of the four-, "
     "six- and seven-piece moves; the {1} of {2} that the six-keeping charge flips at "
     "seven, its {3} to {4} split, and the {3} side carrying all {5} rigid cuttings are "
     "measured directly here".format(
         len(NAMED), 26880, NMOVE[7], 7704, 8096, CORE.size))

J67 = rref(TK[7].values(), dict(TK[6]))
NUL67 = perp(J67, NPO)
W67 = np.zeros((NPO, len(NUL67)), dtype=np.int64)
for c, w in enumerate(NUL67):
    for j in range(NPO):
        if ((w >> j) & 1) == 1:
            W67[j, c] = 1
F67 = (INCL @ W67) & 1
CONST = all(int(F67[:, c].sum()) in (0, NS) for c in range(F67.shape[1]))
gate(CONST and len(NUL67) == 105, "chg.joint",
     "asking a weight to answer the six- and the seven-piece move uniformly at once "
     "leaves a space of dimension {0}, and every charge it puts on the cuttings is "
     "constant".format(len(NUL67)))

PAR = list(range(NS))


def find(x):
    """representative of x, compressing the path on the way up"""
    while PAR[x] != x:
        PAR[x] = PAR[PAR[x]]
        x = PAR[x]
    return x


for a, b in zip(EA[4].tolist(), EB[4].tolist()):
    ra, rb = find(a), find(b)
    if ra != rb:
        PAR[ra] = rb
COMP = {}
for i in range(NS):
    COMP.setdefault(find(i), []).append(i)
CLIST = [COMP[r] for r in sorted(COMP)]
PROF = {}
for c in CLIST:
    PROF[len(c)] = PROF.get(len(c), 0) + 1
SZL = sorted(PROF)
CNL = [PROF[s] for s in SZL]

sec("the groups the smallest move leaves behind")
gate(len(CLIST) == 349 and SZL == [1, 2, 4, 7, 236, 9320]
     and CNL == [144, 96, 36, 48, 24, 1], "comp.prof",
     "the smallest move leaves {0} groups, of sizes {1}, {2}, {3}, {4}, {5} and {6} with "
     "{7}, {8}, {9}, {10}, {11} and {12} groups at each size in the supplied population".format(
         len(CLIST), *(SZL + CNL)))

CID = np.zeros(NS, dtype=np.int64)
for n, c in enumerate(CLIST):
    CID[c] = n
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

CMAP, BROKE = [], 0
for p in PERMS:
    m = np.zeros(len(CLIST), dtype=np.int64)
    for n, c in enumerate(CLIST):
        t = CID[p[c]]
        if int(t.min()) != int(t.max()):
            BROKE += 1
        m[n] = int(t[0])
    CMAP.append(m)
SEEN, ORB = set(), []
for n in range(len(CLIST)):
    if n in SEEN:
        continue
    o = set(int(m[n]) for m in CMAP)
    SEEN |= o
    ORB.append(sorted(o))
O236 = [o for o in ORB if len(CLIST[o[0]]) == 236]
OBIG = [o for o in ORB if len(CLIST[o[0]]) == 9320]
gate(BROKE == 0 and len(ORB) == 14 and len(O236) == 1 and len(O236[0]) == 24
     and len(OBIG) == 1 and len(OBIG[0]) == 1, "comp.orb",
     "no supplied symmetry splits a group; the {0} groups fall into {1} orbits, and the "
     "{2} of size {3} form a single orbit whose stabiliser"
     " has order {4}, while the largest group is held fixed by all {5}".format(
         len(CLIST), len(ORB), 24, 236, len(G) // len(O236[0]), len(G)))

FIX = all(np.array_equal(f[p], f) for f in FUN for p in PERMS)
ONEC = np.zeros(NS, dtype=np.uint8)
ONEC[CLIST[O236[0][0]]] = 1
MOVED = len(set(ONEC[p].tobytes() for p in PERMS))
gate(FIX and MOVED == 24, "chg.fix",
     "every one of the {0} charges is left where it is by all {1} supplied symmetries, "
     "point by point, while the indicator of a single group of {2} cuttings is carried to "
     "{3} different functions".format(len(FUN), len(G), 236, MOVED))

SUP = set(np.flatnonzero(NAMED["four"]).tolist())
U236 = set()
for n in O236[0]:
    U236 |= set(CLIST[n])
gate(SUP == U236 and len(SUP) == 5664 and len(O236[0]) == 24 and CORE.size == 48
     and len(SUP & set(CORE.tolist())) == 0, "chg.supp",
     "the charge keeping the smallest move is exactly the indicator of that one orbit of "
     "{0} groups, holding {1} of the {2} cuttings, and the {3} cuttings carrying no move "
     "on at most eight pieces all sit off it".format(
         len(O236[0]), len(SUP), NS, CORE.size))

print("")
print("per_element: checked — all 192 used simplex indicators and every enumerated exchange vector are resolved exactly over GF(2)")
print("per_site: checked and not executed — the supplied one-cell cutting model contains no independently varying lattice-site field")
print("per_mode: checked and not executed — no spectral or normal-mode decomposition belongs to this finite incidence theorem")
print("per_block: checked — the complete supplied unit four-cube population of 15800 geometric cuttings is exhaustively resolved")
print("lattice_wide: checked and not executed — no multi-cell, arbitrary-tick, boundary, continuum, or framework-selection extension is asserted")
print("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))

receipt = {
    "schema": "physical-cell-cutting-charge-space-cycle736-v2",
    "claim_type": "bounded_theorem",
    "status": "pass" if PF[1] == 0 else "fail",
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "supplied_model": (
        "one unit four-cube with three labelled spatial columns and one labelled tick "
        "column, normalized-volume-one corner 4-simplices, four-coordinate L1 pair "
        "charge, and the declared 48-element spatial-rotation/tick-flip action"
    ),
    "population": {
        "unit_volume_pieces": NPIECE,
        "minimum_cost": LO,
        "minimum_pieces": len(MINP),
        "search_nodes": NODE[0],
        "geometric_cuttings": NS,
        "pieces_per_cutting": 24,
        "used_pieces": NPO,
        "geometric_orbit_representatives": GEO_REPS,
        "geometric_pair_checks": GEO_PAIRS,
    },
    "moves": {
        "sizes": SZC,
        "pair_counts": [NMOVE[k] for k in SZC],
        "distinct_exchange_counts": [NDIST[k] for k in SZG],
        "difference_span_ranks": [len(TK[k]) for k in SZG],
        "odd_zero_certificate_sizes": [None if CERT[k] is None else len(CERT[k]) for k in SZG],
    },
    "responses": {
        "population_span_rank": RKP,
        "population_difference_rank": len(DALL),
        "multiple_pattern_subsets": [[row[0], row[1]] for row in MULTI],
        "smallest_move_weight_dimension": len(NUL),
        "induced_charge_count": len(FUN),
        "induced_charge_rank": len(BAS),
        "constant_charge_count": FLAT,
        "charge_table": {
            name: {
                "split": [TAB[name][0], TAB[name][1]],
                "rigid_side": TAB[name][2],
                "flip_counts": TAB[name][3],
            }
            for name in ("four", "six", "seven")
        },
        "joint_six_seven_weight_dimension": len(NUL67),
    },
    "components": {
        "count": len(CLIST),
        "size_profile": {str(size): PROF[size] for size in SZL},
        "symmetry_orbits": len(ORB),
        "support_component_size": 236,
        "support_component_count": len(O236[0]),
        "support_cuttings": len(SUP),
        "rigid_cuttings": int(CORE.size),
    },
    "no_go_discipline": {
        "status": "PASS" if PF[1] == 0 else "FAIL",
        "negative_assertion_class": "derived_no_go_boundary",
        "checklist": "No-Go Discipline Gate section in the Cycle 736 note",
        "n5_certificate": "five resolution lines in primary stdout and canonical cache",
    },
    "gates": {"pass": PF[0], "fail": PF[1]},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + json.dumps(receipt, sort_keys=True, separators=(",", ":")))
sys.exit(1 if PF[1] else 0)
