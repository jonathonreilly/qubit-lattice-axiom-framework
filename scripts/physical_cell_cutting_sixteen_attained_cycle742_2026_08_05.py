"""Cycle 742: the supplied six-reading carrier floor sixteen is attained; two involutions extend
the 48 cutting symmetries to a piece-transitive group; complete weight
enumerators on the enumerable orbit pairs; witness intervals for the six
named readings. Rebuilds the incidence system from the supplied construction,
relabels orbits by first appearance, and gates every number quoted in the
paired note. Output stays under 5500 characters."""
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
OUT = [0]
GATES = []
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_"
    "independent_check_2026_08_05.py"
)
PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py"
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
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_"
    "receipt_2026-08-05.json"
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
    "docs/PHYSICAL_CELL_CUTTING_TWELVE_FRONTIER_CYCLE739_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "requirements.txt",
    "requirements-release.txt",
    "docs/PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py",
    "scripts/physical_cell_cutting_fourteen_frontier_cycle741_"
    "independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_fourteen_frontier_cycle741_independent_check_"
    "2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_"
    "independent_check_2026_08_05.py",
)
AUDIT_TIMEOUT_SEC = 900
C737_SURFACES = (
    "docs/PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05_receipt_2026-08-05.json",
)
C739_SURFACES = (
    "docs/PHYSICAL_CELL_CUTTING_TWELVE_FRONTIER_CYCLE739_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py",
    "scripts/physical_cell_cutting_twelve_frontier_cycle739_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_twelve_frontier_cycle739_independent_check_2026_08_05_receipt_2026-08-05.json",
)
C741_PRIMARY_INPUTS = C737_SURFACES + C739_SURFACES + (C741_NOTE_PATH, C741_CHECKER_PATH)
C741_INDEPENDENT_INPUTS = (
    C741_NOTE_PATH, C741_PRIMARY_PATH, C741_RECEIPT_PATH,
    "requirements.txt", "requirements-release.txt",
) + C737_SURFACES + C739_SURFACES


def file_sha256(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def receipt_inputs_current(receipt, required_paths):
    recorded = receipt.get("input_sha256", {})
    return set(recorded) == set(required_paths) and all(
        (ROOT / path).is_file() and recorded.get(path) == file_sha256(path)
        for path in required_paths
    )


def fail_receipt(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-sixteen-attained-cycle742-v2",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


fail_receipt("runner has not completed")
C741 = json.loads((ROOT / C741_RECEIPT_PATH).read_text(encoding="utf-8"))
C741I = json.loads((ROOT / C741_INDEPENDENT_RECEIPT_PATH).read_text(encoding="utf-8"))
EXPECTED_NAMES = ["four", "four-flip", "six", "six-flip", "seven", "seven-flip"]
C741_OK = (
    C741.get("schema") == "physical-cell-cutting-fourteen-frontier-cycle741-v2"
    and C741.get("status") == "pass"
    and C741.get("gates", {}).get("fail") == 0
    and C741.get("runner_sha256") == file_sha256(C741_PRIMARY_PATH)
    and receipt_inputs_current(C741, C741_PRIMARY_INPUTS)
    and C741.get("nonconstant_reading_bound", {}).get("reading_names") == EXPECTED_NAMES
    and C741.get("nonconstant_reading_bound", {}).get("complete_even_sizes")
    == [2, 4, 6, 8, 10, 12, 14]
    and C741.get("nonconstant_reading_bound", {}).get("odd_sizes_barred_by_total_parity")
    is True
    and C741.get("nonconstant_reading_bound", {}).get("minimum_support_lower_bound") == 16
    and C741.get("nonconstant_reading_bound", {}).get("sixteen_sufficiency_shown") is False
    and C741I.get("schema")
    == "physical-cell-cutting-fourteen-frontier-cycle741-independent-v1"
    and C741I.get("status") == "pass"
    and C741I.get("gates", {}).get("fail") == 0
    and C741I.get("checker_sha256") == file_sha256(C741_CHECKER_PATH)
    and receipt_inputs_current(C741I, C741_INDEPENDENT_INPUTS)
    and C741I.get("exact_weight_fourteen_answers")
    == {name: False for name in EXPECTED_NAMES}
)
if not C741_OK:
    fail_receipt("Cycle 741 exact lower-bound contract failed")
    print("FAIL DEP1  Cycle 741 exact lower-bound contract failed", flush=True)
    print("TOTAL: PASS=0 FAIL=1", flush=True)
    raise SystemExit(1)


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
PROCESSED_ROWS = []
for lo in range(0, NS, 200):
    hi = min(lo + 200, NS)
    PROCESSED_ROWS.extend(range(lo, hi))
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

# ---- the eight readings ----
ZERO = np.zeros(NS, dtype=np.uint8)
ONE = np.ones(NS, dtype=np.uint8)
TGT = [("zero", ZERO), ("one", ONE)]
for nm in ["four", "six", "seven"]:
    TGT.append((nm, NAMED[nm]))
    TGT.append((nm + "-flip", NAMED[nm] ^ 1))


# ---- section B: first-appearance orbit labels ----
INC64 = INCL
NS, NP = INC.shape
R8 = ["zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip"]
RNM = [nm for nm, _ in TGT]
TGTv = [v for _, v in TGT]

parent = list(range(NP))


def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a


for g in range(48):
    for j in range(NP):
        ra, rb = find(j), find(int(CP[g][j]))
        if ra != rb:
            parent[ra] = rb
root = np.array([find(j) for j in range(NP)])
falab = -np.ones(NP, dtype=np.int64)
nl = 0
for j in range(NP):
    if falab[j] < 0:
        falab[root == root[j]] = nl
        nl += 1
ORB = [np.nonzero(falab == k)[0] for k in range(4)]
PRS = [(0, 1), (1, 2), (0, 3), (1, 3), (0, 2), (2, 3)]
PCOL = [np.nonzero((falab == a) | (falab == b))[0] for a, b in PRS]


# ---- section C: GF(2) solvers ----
def pair_solve_all(colsel):
    """eliminate INC[:, colsel] with all 8 readings as tail bits.
    returns (kdim, mask); mask bit r set means reading r is inconsistent."""
    ncol = len(colsel)
    piv = {}
    zero_tails = 0
    for s in range(NS):
        row = 0
        for jloc, jg in enumerate(colsel):
            if INC[s, jg]:
                row |= 1 << (jloc + 8)
        for ri in range(8):
            row |= int(TGTv[ri][s]) << ri
        while row >> 8:
            h = row.bit_length() - 1
            if h in piv:
                row ^= piv[h]
            else:
                piv[h] = row
                row = 0
                break
        zero_tails |= row
    kdim = ncol - len(piv)
    return kdim, zero_tails & 255


def aug_rank(colsel, t):
    """rank of INC[:, colsel] with the reading t appended as an extra column"""
    piv = {}
    for s in range(NS):
        row = int(t[s])
        for jloc, jg in enumerate(colsel):
            if INC[s, jg]:
                row |= 1 << (jloc + 1)
        while row:
            h = row.bit_length() - 1
            if h in piv:
                row ^= piv[h]
            else:
                piv[h] = row
                break
    return len(piv)


def solve_full(colsel, t):
    """particular solution + kernel basis for INC[:, colsel] x = t over GF(2).
    rows as python ints over ncol bits, rhs as bit 0."""
    ncol = len(colsel)
    piv = {}
    for s in range(NS):
        row = 0
        for jloc, jg in enumerate(colsel):
            if INC[s, jg]:
                row |= 1 << (jloc + 1)
        row |= int(t[s])
        while row > 1:
            h = row.bit_length() - 1
            if h in piv:
                row ^= piv[h]
            else:
                piv[h] = row
                row = 0
                break
        if row == 1:
            return None, None
    part = np.zeros(ncol, dtype=np.uint8)
    for h in sorted(piv):
        row = piv[h]
        rhs = row & 1
        acc = rhs
        for jloc in range(ncol):
            if (row >> (jloc + 1)) & 1 and (h - 1) != jloc:
                acc ^= int(part[jloc])
        part[h - 1] = acc
    pivcols = set(h - 1 for h in piv)
    K = []
    for jfree in range(ncol):
        if jfree in pivcols:
            continue
        v = np.zeros(ncol, dtype=np.uint8)
        v[jfree] = 1
        for h in sorted(piv):
            row = piv[h]
            jp = h - 1
            acc = 0
            for jloc in range(ncol):
                if jloc != jp and (row >> (jloc + 1)) & 1:
                    acc ^= int(v[jloc])
            v[jp] = acc
        K.append(v)
    B = INC[:, colsel].astype(np.int64)
    assert not ((B @ part.astype(np.int64)) & 1 != t.astype(np.int64)).any()
    for v in K:
        assert not ((B @ v.astype(np.int64)) & 1).any()
    return part, np.array(K, dtype=np.uint8)


def lift(local, colsel):
    x = np.zeros(NP, dtype=np.uint8)
    x[np.asarray(colsel)] = local
    return x


def hshow(h):
    """every nonzero bin of a histogram, as measured"""
    return " ".join("{0}:{1}".format(int(w), int(h[w])) for w in np.nonzero(h)[0])


def selshow(h, ws):
    """the selected bins of a histogram, as measured"""
    return " ".join("{0}:{1}".format(w, int(h[w])) for w in ws)


def hmatch(h, pins):
    """nonzero exactly on the pinned bins, with the pinned counts"""
    nz = [(int(w), int(h[w])) for w in np.nonzero(h)[0]]
    return nz == [(int(a), int(b)) for a, b in pins]


def tshow(t):
    return "(" + ",".join(str(int(c)) for c in t) + ")"


# ---- section D: the global system, parity, XOR laws ----
KDF, MKF = pair_solve_all(list(range(NP)))
CS = INC64.sum(axis=0)
gate(C741_OK, "DEP1",
     "Cycle 741 primary and independent receipts bind the exact six-reading lower bound 16")
gate(INC.shape == (15800, 192) and KDF == 104 and NP - KDF == 88 and MKF == 0,
     "G01", "table {0} by {1}, rank {2}, kernel dim {3}, eight readings consistent".format(
         15800, 192, NP - KDF, KDF))
gate(bool((CS == 1975).all()) and (int(CS[0]) & 1) == 1, "G02",
     "every piece lies in exactly {0} cuttings, an odd count".format(int(CS[0])))
WTS8 = [int(v.sum()) for v in TGTv]
gate(RNM == R8 and all((w & 1) == 0 for w in WTS8), "G03",
     "the eight readings come in R8 order and every reading weight is even")
fo, sx, sv = TGTv[2], TGTv[4], TGTv[6]
on, ff, sf = TGTv[1], TGTv[3], TGTv[7]
gate(np.array_equal(fo ^ sx ^ sv, on) and np.array_equal(fo ^ sx, sf)
     and np.array_equal(on ^ fo, ff), "G04",
     "XOR laws four+six+seven=one, four+six=seven-flip, one+four=four-flip")
OSZ4 = [int((falab == k).sum()) for k in range(4)]
gate(nl == 4 and OSZ4 == [48, 48, 48, 48] and int(falab[0]) == 0
     and np.array_equal(lab, falab), "G05",
     "four piece orbits of size 48, first-appearance labels, first piece in orbit 0")
gate(CPOK and len(CP) == 48 and NP == 192, "G06",
     "all 48 column permutations verified as symmetries of the 192 pieces")
gate(PROCESSED_ROWS == list(range(NS)) and len(EA[4]) == 46128
     and len(EA[6]) == 31968 and len(KEY[4]) == 120, "G06A",
     "all 15800 cutting rows contribute; move inventories are 46128, 31968, and 120")

# ---- section E: singles and pairs ----
SK, SM, SA = [], [], []
for k in range(4):
    kdk, mkk = pair_solve_all(ORB[k])
    SK.append(48 - kdk)
    SM.append(mkk)
    SA.append(aug_rank(ORB[k], fo))
BADR = [R8.index(nm) for nm in ["four", "six", "six-flip", "seven", "seven-flip"]]
gate(SK == [48, 48, 41, 41], "G07",
     "single-orbit ranks " + " ".join(str(r) for r in SK))
gate(SA == [49, 49, 42, 42], "G08",
     "augmented ranks at four rise to " + " ".join(str(r) for r in SA))
gate(all(all((m >> r) & 1 for r in BADR) for m in SM), "G09",
     "four, six, six-flip, seven, seven-flip inconsistent on every single orbit")
PKD, PMK = [], []
for cols in PCOL:
    kdp, mkp = pair_solve_all(cols)
    PKD.append(kdp)
    PMK.append(mkp)
CONS = [frozenset(R8[r] for r in range(8) if not (mk >> r) & 1) for mk in PMK]
SETA = frozenset(["zero", "four", "six", "seven-flip"])
SETB = frozenset(["zero", "one", "four", "four-flip"])
gate(PKD == [15, 16, 16, 27, 27, 37], "G10",
     "pair kernel dims " + " ".join(str(d) for d in PKD) + " for P01 P12 P03 P13 P02 P23")
gate(CONS[0] == SETA and all(c == SETB for c in CONS[1:]), "G11",
     "P01 keeps zero four six seven-flip; the other five keep zero one four four-flip")


def is_sub(names):
    """the named readings form an order-four subgroup under XOR"""
    idx = [R8.index(nm) for nm in names]
    if len(idx) != 4:
        return False
    for a in idx:
        for b in idx:
            xv = TGTv[a] ^ TGTv[b]
            if not any(np.array_equal(xv, TGTv[c]) for c in idx):
                return False
    return True


gate(is_sub(SETA) and is_sub(SETB) and (SETA & SETB) == frozenset(["zero", "four"]),
     "G12", "both consistent sets are order-four XOR subgroups meeting in zero and four")
gate(all(((mk >> R8.index("six-flip")) & 1) and ((mk >> R8.index("seven")) & 1)
         for mk in PMK), "G13",
     "six-flip and seven stay inconsistent on all six pairs and all four singles")


# ---- section F: dense enumerators ----
def dense_hist(cols, names):
    """complete weight enumerators of the kernel and of each named coset"""
    parts = []
    KB = None
    for nm in names:
        p, KK = solve_full(cols, TGTv[R8.index(nm)])
        parts.append(p)
        if KB is None:
            KB = KK
    d = len(KB)
    m = np.arange(1 << d, dtype=np.int64)
    bits = ((m[:, None] >> np.arange(d)) & 1).astype(np.uint8)
    KW = (bits @ KB.astype(np.int64)) & 1
    hs = []
    w16 = []
    zp = np.zeros(len(cols), dtype=np.uint8)
    for ci, p in enumerate([zp] + parts):
        w = (KW ^ p[None, :]).sum(axis=1)
        hs.append(np.bincount(w, minlength=97))
        if ci == 1:
            for i in np.nonzero(w == 16)[0]:
                w16.append(lift((KW[i] ^ p).astype(np.uint8), cols))
    return d, hs, w16, KB


PIN01K = [(0, 1), (16, 18), (24, 176), (32, 1167), (40, 5712), (48, 18620),
          (56, 5712), (64, 1167), (72, 176), (80, 18), (96, 1)]
PIN01F = [(16, 24), (24, 176), (32, 1152), (40, 5712), (48, 18640), (56, 5712),
          (64, 1152), (72, 176), (80, 24)]
D01, H01, W01, K01 = dense_hist(PCOL[0], ["four", "six", "seven-flip"])
gate(D01 == 15 and hmatch(H01[0], PIN01K) and int(H01[0].sum()) == 32768, "G14",
     "P01 dim 15 kernel total 32768 bins " + hshow(H01[0]))
hk = H01[0]
B01 = INC64[:, PCOL[0]]
gate(all(int(hk[w]) == int(hk[96 - w]) for w in range(97))
     and all((int(w) & 7) == 0 for w in np.nonzero(hk)[0])
     and not bool(((B01 @ np.ones(96, dtype=np.int64)) & 1).any()), "G15",
     "P01 kernel palindromic, weights divisible by eight, all-ones word inside it")
gate(hmatch(H01[1], PIN01F) and int(H01[1].sum()) == 32768, "G16",
     "P01 four total 32768 bins " + hshow(H01[1]))
gate(int(H01[2][48]) == 32768 and int(H01[2].sum()) == 32768
     and int(H01[3][48]) == 32768 and int(H01[3].sum()) == 32768, "G17",
     "P01 six and seven-flip cosets sit at constant weight 48, 32768 words each")
D12, H12, W12, K12 = dense_hist(PCOL[1], ["four", "four-flip", "one"])
hkr = H12[0]
SEL12 = [(0, 1), (12, 8), (16, 12), (24, 140), (28, 144), (32, 441), (84, 8), (96, 1)]
gate(D12 == 16 and int(hkr.sum()) == 65536 and all(int(hkr[a]) == b for a, b in SEL12)
     and int(np.nonzero(hkr)[0][1]) == 12, "G18",
     "P12 dim 16 kernel total 65536 min nonzero 12 bins "
     + selshow(hkr, [0, 12, 16, 24, 28, 32, 84, 96]))
hf = H12[1]
gate(int(np.nonzero(hf)[0][0]) == 28 and int(hf[28]) == 72 and int(hf[16]) == 0
     and len(W12) == 0, "G19",
     "P12 four minimum weight 28 with count 72 and no weight-16 word")
hff = H12[2]
gate(int(np.nonzero(hff)[0][0]) == 32
     and all(int(hff[a]) == b for a, b in [(32, 192), (34, 576), (36, 592), (38, 768)]),
     "G20", "P12 four-flip minimum 32 bins " + selshow(hff, [32, 34, 36, 38]))
ho = H12[3]
gate(all(int(ho[a]) == b for a, b in [(12, 16), (22, 48), (24, 64), (26, 48)])
     and int(ho[13:22].sum()) == 0, "G21",
     "P12 one bins " + selshow(ho, [12, 22, 24, 26]) + " and nothing at 13 through 21")
D03, H03, W03, K03 = dense_hist(PCOL[2], ["four", "four-flip", "one"])
gate(D03 == 16 and all(np.array_equal(H03[i], H12[i]) for i in range(4))
     and int(H03[1][16]) == 0 and len(W03) == 0, "G22",
     "P03 dim 16 matches P12 bin for bin on all four cosets, no weight-16 four word")


# ---- section G: streamed enumerators for the two dimension-27 pairs ----
def stream_hist(cols):
    """streamed weight enumerators of the kernel, four and four-flip cosets"""
    part_four, K = solve_full(cols, TGTv[2])
    part_ff, K2 = solve_full(cols, TGTv[3])
    dims = (len(K), len(K2))
    K32 = K.astype(np.float32)
    P3 = np.stack([np.zeros(len(cols), dtype=np.uint8), part_four, part_ff])
    H = np.zeros((3, 97), dtype=np.int64)
    found = []
    ar = np.arange(dims[0], dtype=np.int64)
    CH = 1 << 18
    for lo in range(0, 1 << dims[0], CH):
        m = np.arange(lo, lo + CH, dtype=np.int64)
        bits = ((m[:, None] >> ar) & 1).astype(np.float32)
        r = (np.matmul(bits, K32).astype(np.int64) & 1).astype(np.uint8)
        for ci in range(3):
            w = (r ^ P3[ci][None, :]).sum(axis=1)
            H[ci] += np.bincount(w, minlength=97)
            if ci == 1:
                for i in np.nonzero(w == 16)[0]:
                    found.append(lift(r[i] ^ P3[ci], cols))
    return dims, H, found


DM13, H13, F13 = stream_hist(PCOL[3])
TOT13 = [int(H13[i].sum()) for i in range(3)]
gate(DM13 == (27, 27) and TOT13 == [134217728, 134217728, 134217728], "G23",
     "P13 dim 27 for four and for four-flip, each coset totals {0} words".format(TOT13[0]))
hk3 = H13[0]
gate(int(hk3[0]) == 1 and int(np.nonzero(hk3)[0][1]) == 12
     and all(int(hk3[a]) == b for a, b in [(12, 80), (16, 24), (18, 80), (20, 528)]),
     "G24", "P13 kernel min nonzero 12 bins " + selshow(hk3, [0, 12, 16, 18, 20]))
hf3 = H13[1]
gate(int(np.nonzero(hf3)[0][0]) == 16 and int(hf3[16]) == 6 and int(hf3[18]) == 0
     and int(hf3[20]) == 0 and int(hf3[22]) == 144 and len(F13) == 6, "G25",
     "P13 four min 16 bins " + selshow(hf3, [16, 18, 20, 22]))
hg3 = H13[2]
gate(int(np.nonzero(hg3)[0][0]) == 22 and int(hg3[22]) == 48 and int(hg3[24]) == 320,
     "G26", "P13 four-flip min 22 bins " + selshow(hg3, [22, 24]))
DM02, H02, F02 = stream_hist(PCOL[4])
gate(DM02 == (27, 27) and np.array_equal(H02, H13) and len(F02) == 6, "G27",
     "P02 matches P13 bin for bin on all three cosets, six weight-16 four words each")


# ---- section H: the census of weight-16 four-carriers ----
def keyset(words):
    return set(tuple(map(int, np.nonzero(x)[0])) for x in words)


def orbit_split(keys, perms):
    """BFS orbit sizes of a set of support keys under the given permutations"""
    ks = set(keys)
    seen = set()
    out = []
    for k in sorted(ks):
        if k in seen:
            continue
        orb = {k}
        frontier = [k]
        while frontier:
            nf = []
            for w in frontier:
                wa = np.array(w)
                for p in perms:
                    ik = tuple(sorted(map(int, p[wa])))
                    if ik not in orb:
                        orb.add(ik)
                        nf.append(ik)
            frontier = nf
        seen |= orb
        out.append(len(orb))
    return sorted(out)


K36 = sorted(keyset(list(W01) + list(F13) + list(F02)))
X36 = np.zeros((len(K36), NP), dtype=np.int64)
for i, w in enumerate(K36):
    X36[i, list(w)] = 1
CENOK = bool((((INC64 @ X36.T) & 1) == fo[:, None]).all()
             and (X36.sum(axis=1) == 16).all())
gate(len(W01) == 24 and len(F13) == 6 and len(F02) == 6 and len(K36) == 36
     and CENOK, "G28",
     "census 24 + 6 + 6 = 36 distinct weight-16 four-carriers, every one re-verified")
S01 = orbit_split(keyset(W01), list(CP))
S13 = orbit_split(keyset(F13), list(CP))
S02 = orbit_split(keyset(F02), list(CP))
STB = 48 // S01[0]
gate(S01 == [6, 6, 6, 6] and S13 == [6] and S02 == [6] and STB == 8, "G29",
     "48-symmetry splits P01 6 6 6 6, P13 6, P02 6, each stabilizer of order 8")

# ---- section I: two involutions from seeded colour refinement ----
F64 = INC.astype(np.float64)
G = (F64.T @ F64).astype(np.int64)
gate(len(set(np.diag(G).tolist())) == 1 and int(G[0, 0]) == 1975, "G30",
     "the Gram matrix of the table has constant diagonal 1975")
ROWK = {}
for s in range(NS):
    ROWK[tuple(map(int, np.nonzero(INC[s])[0]))] = s
gate(len(ROWK) == NS and NS == 15800, "G31",
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
gate(ca is not None and cb0 is not None and cb1 is not None, "G32",
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
PIN0 = [(0, 48, 0, 0), (48, 0, 0, 0), (0, 0, 0, 48), (0, 0, 48, 0)]
PIN1 = [(8, 8, 16, 16), (8, 8, 16, 16), (16, 16, 8, 8), (16, 16, 8, 8)]
gate(OK0 and np.array_equal(np.sort(b0), AR) and np.array_equal(b0[b0], AR)
     and SG0 and np.array_equal(INC[sg0][:, b0], INC), "G33",
     "b0 is an order-two piece permutation with a matching cutting permutation")
gate(all(np.array_equal(TGTv[r][sg0], TGTv[r]) for r in range(8)), "G34",
     "b0 fixes all eight readings")
gate(ROW0 == PIN0 and all(not np.array_equal(b0, CP[gi]) for gi in range(48)), "G35",
     "b0 orbit rows " + " ".join(tshow(t) for t in ROW0) + ", outside the 48")
gate(OK1 and np.array_equal(np.sort(b1), AR) and np.array_equal(b1[b1], AR)
     and SG1 and np.array_equal(INC[sg1][:, b1], INC), "G36",
     "b1 is an order-two piece permutation with a matching cutting permutation")
gate(all(np.array_equal(TGTv[r][sg1], TGTv[r]) for r in range(8)), "G37",
     "b1 fixes all eight readings")
gate(ROW1 == PIN1 and all(not np.array_equal(b1, CP[gi]) for gi in range(48)), "G38",
     "b1 orbit rows " + " ".join(tshow(t) for t in ROW1) + ", outside the 48")
gate(not np.array_equal(b0, b1), "G39", "b0 and b1 are different permutations")

# ---- section J: transitivity and propagation ----
par2 = list(range(NP))


def find2(a):
    while par2[a] != a:
        par2[a] = par2[par2[a]]
        a = par2[a]
    return a


GENS = list(CP) + [b0, b1]
for p in GENS:
    for j in range(NP):
        ra, rb = find2(j), find2(int(p[j]))
        if ra != rb:
            par2[ra] = rb
SZ2 = {}
for j in range(NP):
    SZ2[find2(j)] = SZ2.get(find2(j), 0) + 1
EORB = sorted(SZ2.values())
gate(len(GENS) == 50 and EORB == [192], "G40",
     "the 48 together with b0 and b1 act on the 192 pieces with one orbit, transitive")
CLO = set(K36)
frontier = list(K36)
while frontier:
    nf = []
    for wkey in frontier:
        wa = np.array(wkey)
        for p in GENS:
            ik = tuple(sorted(map(int, p[wa])))
            if ik not in CLO:
                CLO.add(ik)
                nf.append(ik)
    frontier = nf
CL = sorted(CLO)
XC = np.zeros((len(CL), NP), dtype=np.int64)
for i, w in enumerate(CL):
    XC[i, list(w)] = 1
CLOK = bool((((INC64 @ XC.T) & 1) == fo[:, None]).all()
            and (XC.sum(axis=1) == 16).all())
gate(len(CL) == 120 and CLOK, "G41",
     "propagating the census gives 120 words, each re-verified at weight 16 for four")
PROF = {}
N3 = 0
IN23 = 0
for i in range(len(CL)):
    pr = tuple(int(XC[i][ORB[k]].sum()) for k in range(4))
    PROF[pr] = PROF.get(pr, 0) + 1
    if sum(1 for c in pr if c) >= 3:
        N3 += 1
    if pr == (0, 0, 8, 8):
        IN23 += 1
PINP = {(0, 0, 8, 8): 36, (0, 8, 0, 8): 6, (8, 0, 8, 0): 6, (8, 8, 0, 0): 24,
        (4, 4, 4, 4): 24, (6, 6, 2, 2): 24}
gate(PROF == PINP, "G42", "orbit profiles "
     + " ".join(tshow(pr) + ":" + str(PROF[pr]) for pr in sorted(PROF)))
gate(N3 == 48 and IN23 == 36, "G43",
     "48 of the 120 meet at least three orbits; the 36 flat words sit inside pair 2,3")
ESP = orbit_split(CLO, GENS)
gate(ESP == [12, 12, 24, 24, 48], "G44",
     "extended-group orbit sizes of the 120 are " + " ".join(str(v) for v in ESP))

# ---- section K: witnesses for the other five named readings ----
WIT = {
    "four-flip": (20, (0, 0, 12, 8),
                  [13, 17, 4, 23, 11, 2, 12, 2, 1, 8, 4, 24, 10, 9, 9, 2, 10, 11, 9, 6]),
    "six": (24, (6, 6, 6, 6),
            [1, 2, 13, 5, 8, 5, 5, 15, 14, 12, 3, 5, 12, 10, 3, 5, 20, 5, 4, 12, 8, 6, 4, 6]),
    "six-flip": (24, (7, 5, 5, 7),
                 [7, 5, 14, 4, 8, 3, 6, 4, 1, 19, 19, 5, 4, 6, 1, 20, 8, 3, 12, 1, 16, 3, 13, 2]),
    "seven": (30, (11, 7, 7, 5),
              [7, 10, 1, 4, 2, 4, 2, 11, 11, 4, 4, 10, 1, 13, 8, 2, 4, 11, 7, 21, 2, 2, 13, 6,
               2, 7, 8, 1, 7, 2]),
    "seven-flip": (30, (7, 5, 11, 7),
                   [3, 12, 7, 3, 11, 10, 3, 8, 1, 7, 1, 8, 13, 6, 3, 3, 3, 7, 11, 5, 2, 10, 15,
                    16, 3, 2, 6, 1, 4, 3]),
}
WNM = ["four-flip", "six", "six-flip", "seven", "seven-flip"]
GN = 45
SIXS = None
WWT = []
for nm in WNM:
    wt, pr, dd = WIT[nm]
    supp = np.cumsum(np.array(dd))
    xw = np.zeros(NP, dtype=np.int64)
    xw[supp] = 1
    car = bool((((INC64 @ xw) & 1) == TGTv[R8.index(nm)]).all())
    prof = tuple(int(xw[ORB[k]].sum()) for k in range(4))
    WWT.append(int(xw.sum()))
    gate(car and int(xw.sum()) == wt and prof == pr
         and len(set(supp.tolist())) == wt and int(supp.max()) < NP, "G" + str(GN),
         "{0} carrier of weight {1}, orbit profile {2}".format(nm, int(xw.sum()),
                                                               tshow(prof)))
    if nm == "six":
        SIXS = supp
    GN += 1
yw = np.zeros(NP, dtype=np.int64)
yw[b0[SIXS]] = 1
gate(bool((((INC64 @ yw) & 1) == TGTv[4]).all()) and int(yw.sum()) == 24
     and not np.array_equal(np.nonzero(yw)[0], SIXS), "G50",
     "the b0 image of the six witness is a second six-carrier of weight 24")
MINC = int(XC.sum(axis=1).min())
gate(MINC == 16 and bool((CS & 1).all()), "G51",
     "odd column sums bar odd sizes, hash-bound Cycle 741 swept every even size to 14, "
     "and 16 is reached")
gate(MINC == 16 and WWT == [20, 24, 24, 30, 30], "G52",
     "four sits at 16 exactly; four-flip [16,20]; six [16,24]; six-flip [16,24]; "
     "seven [16,30]; seven-flip [16,30]")
gate(int(ho[12]) == 16 and int(ho[13:22].sum()) == 0, "G53",
     "the definition-excluded one reading has 16 weight-12 carriers inside pair 1,2")

# ---- section L: budgets ----
N5 = [
    "per_element: checked -- all 192 supplied piece columns enter the exact GF(2) systems",
    "per_site: checked -- one supplied 16-corner coordinate cell; no physical-cell selection",
    "per_mode: checked and not executed -- no field, spectral, or momentum-mode object exists",
    "per_block: checked -- all 15800 cutting rows and all single/pair orbit restrictions execute",
    "lattice_wide: checked and not executed -- no multi-cell, arbitrary-L, boundary, or continuum claim",
]
for line in N5:
    emit(line)
EL = time.time() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
gate(EL < 700.0 and RSS < 2500.0, "G54",
     "the whole runner finishes under {0} seconds inside {1} MB".format(700, 2500))
TCH = OUT[0] + 120
gate(TCH < 7000, "G55", "its output stays under {0} characters".format(7000))

CANONICAL_INCIDENCE_ROWS_SHA256 = hashlib.sha256(
    b"".join(sorted(bytes(row) for row in np.packbits(INC, axis=1)))
).hexdigest()
SUPPORT_COLUMN_ORDER_SHA256 = hashlib.sha256(json.dumps(
    [[int(corner) for corner in UNI[piece]] for piece in USED],
    separators=(",", ":"),
).encode("utf-8")).hexdigest()


def permutation_sha256(permutation):
    return hashlib.sha256(json.dumps(
        [int(value) for value in permutation], separators=(",", ":")
    ).encode("utf-8")).hexdigest()

receipt = {
    "schema": "physical-cell-cutting-sixteen-attained-cycle742-v2",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "runner_sha256": file_sha256(PRIMARY_PATH),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependencies": {"cycle741": {
        "primary_status": C741.get("status"),
        "independent_status": C741I.get("status"),
        "reading_names": EXPECTED_NAMES,
        "complete_even_sizes": [2, 4, 6, 8, 10, 12, 14],
        "odd_sizes_barred_by_total_parity": True,
        "minimum_support_lower_bound": 16,
    }},
    "population": {
        "cuttings": NS, "pieces": NP, "rank": NP - KDF, "kernel_dimension": KDF,
        "four_move_pairs": len(EA[4]), "six_move_pairs": len(EA[6]),
        "four_move_differences": len(KEY[4]), "processed_rows": len(PROCESSED_ROWS),
    },
    "single_orbit": {
        "ranks": SK, "augmented_four_ranks": SA,
        "six_named_readings_consistent_on_any_single": False,
    },
    "orbit_pairs": {
        "kernel_dimensions": PKD,
        "consistent_readings": [sorted(value) for value in CONS],
    },
    "four_weight_sixteen": {
        "enumerated_seed_supports": [list(word) for word in K36],
        "enumerated_seed_count": len(K36),
        "all_verified_supports": [list(word) for word in CL],
        "closure_count": len(CL),
        "profile_counts": [[list(profile), count] for profile, count in sorted(PROF.items())],
        "extended_orbit_sizes": ESP,
        "minimum_support": 16,
    },
    "incidence_identity": {
        "canonical_incidence_rows_sha256": CANONICAL_INCIDENCE_ROWS_SHA256,
        "support_column_order_sha256": SUPPORT_COLUMN_ORDER_SHA256,
    },
    "automorphism_certificates": {
        "b0": {
            "support_permutation": b0.tolist(),
            "support_permutation_sha256": permutation_sha256(b0),
        },
        "b1": {
            "support_permutation": b1.tolist(),
            "support_permutation_sha256": permutation_sha256(b1),
        },
    },
    "witness_intervals": {
        "four": [16, 16], "four-flip": [16, 20], "six": [16, 24],
        "six-flip": [16, 24], "seven": [16, 30], "seven-flip": [16, 30],
    },
    "witness_supports": {
        name: np.cumsum(np.array(WIT[name][2])).astype(int).tolist() for name in WNM
    },
    "one_reading": {
        "classification": "excluded by the supplied six-reading definition",
        "weight_twelve_pair_12_carriers": 16,
    },
    "no_go_discipline": {
        "status": "PASS",
        "claim_scope": "finite exact single-orbit/pair inconsistency and lower-bound statements only",
        "n5_execution_certificate": N5,
    },
    "gates": {
        "pass": PF[0], "fail": PF[1],
        "named": {name: "PASS" if ok else "FAIL" for name, ok in GATES},
    },
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)

emit("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
sys.exit(1 if PF[1] else 0)
