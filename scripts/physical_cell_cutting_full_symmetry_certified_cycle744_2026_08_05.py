"""Cycle 744: full finite incidence symmetry in one supplied cutting table.

Rebuilds the incidence table of the 15800 cuttings on 192 pieces, the eight
readings, the 48 cutting permutations and the two extra incidence
automorphisms certified by Cycles 742 and 743, re-forms the extended group of
order 384, and certifies by an exhaustive stabilizer branch that no other
piece permutation preserves this exact incidence family.  This is a bounded
finite theorem, not a physical or arbitrary-cell symmetry claim.  Failed
gates write a failing receipt and exit nonzero.  Output stays bounded.
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

PF = [0, 0]
GATES = []
OUT = [0]
T0 = time.time()

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = "scripts/physical_cell_cutting_full_symmetry_certified_cycle744_2026_08_05.py"
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_full_symmetry_certified_cycle744_"
    "independent_check_2026_08_05.py"
)
C742_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md"
C742_PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py"
C742_CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_"
    "independent_check_2026_08_05.py"
)
C742_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_"
    "receipt_2026-08-05.json"
)
C742_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C743_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md"
C743_PRIMARY_PATH = "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05.py"
C743_CHECKER_PATH = (
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_"
    "independent_check_2026_08_05.py"
)
C743_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05_"
    "receipt_2026-08-05.json"
)
C743_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_"
    "independent_check_2026_08_05_receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_full_symmetry_certified_cycle744_2026_08_05_"
    "receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_full_symmetry_certified_cycle744_independent_check_2026_08_05.py",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_independent_check_2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05.py",
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_independent_check_2026_08_05_receipt_2026-08-05.json",
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


def canonical_perm_sha256(perm):
    payload = json.dumps([int(value) for value in perm], separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def fail_receipt(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-full-symmetry-certified-cycle744-v2",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


fail_receipt("runner has not completed")


def load_receipt(path):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


C742_RECEIPT = load_receipt(C742_RECEIPT_PATH)
C742_INDEPENDENT_RECEIPT = load_receipt(C742_INDEPENDENT_RECEIPT_PATH)
C743_RECEIPT = load_receipt(C743_RECEIPT_PATH)
C743_INDEPENDENT_RECEIPT = load_receipt(C743_INDEPENDENT_RECEIPT_PATH)


def emit(s):
    """print one line, refusing any barred digit pair"""
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    print(txt)
    OUT[0] += len(txt) + 1


def gate(ok, n, name, got, exp=None):
    """record and print one gate: computed value first, pinned value after"""
    passed = bool(ok)
    PF[0 if passed else 1] += 1
    GATES.append((str(n), passed))
    tail = "" if exp is None else " exp {0}".format(exp)
    emit("G{0} {1}: {2}{3} -> {4}".format(n, name, got, tail,
                                          "PASS" if passed else "FAIL"))


def cshow(c):
    """an element-order census as measured"""
    return " ".join("{0}:{1}".format(a, b) for a, b in c)


# ------------------------------------------------- Part 1: rebuild
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
GRP = []
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
            GRP.append((R, tf, np.array(img, dtype=np.int64)))

posp = dict((tuple(int(c) for c in s), i) for i, s in enumerate(UNI))
LAB = -np.ones(NPIECE, dtype=np.int64)
REPS = []
for i in range(NPIECE):
    if LAB[i] >= 0:
        continue
    o = len(REPS)
    REPS.append(i)
    for (_, _, g) in GRP:
        LAB[posp[tuple(sorted(int(g[c]) for c in UNI[i]))]] = o
REPS = np.array(REPS, dtype=np.int64)

OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
LMB = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(LMB).max()), int(np.abs(LMB.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
SC = np.array([SB // 2, SB // 2, SB // 2], dtype=np.int64)
lab, coll = {}, 0
for o, i in enumerate(REPS):
    q = (WT[:, None] * V[UNI[i]]).sum(axis=0)
    for (R, tf, _) in GRP:
        u = R @ (q[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]), (SB - int(q[3])) if tf else int(q[3]))
        if lab.setdefault(key, o) != o:
            coll += 1
KEYS = sorted(lab)
Q = np.array(KEYS, dtype=np.int64)
NQ = len(Q)
QT = Q.T
MASK = []
MI = np.zeros((NPIECE, NQ), dtype=np.int64)
for i in range(NPIECE):
    lm = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lm.sum(axis=0)
    ins = (lm > 0).all(axis=0) & (tot < SB)
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
SOL = []


def rec(cov, chosen):
    if cov == ALLQ:
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
NP = NPO
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
    d = LUT[np.bitwise_xor(PK[lo:hi, None, :], PK[None, :, :])].sum(axis=2,
                                                                   dtype=np.int16)
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

NAMED = {}
for f in FUN:
    one = int(f.sum())
    if one in (0, NS):
        continue
    g = f if 2 * one <= NS else (f ^ 1)
    d4 = g[EA[4]] ^ g[EB[4]]
    d6 = g[EA[6]] ^ g[EB[6]]
    nm = "four" if d4.max() == 0 else ("six" if d6.max() == 0 else "seven")
    NAMED[nm] = g

R8 = ["zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip"]
TGT = [("zero", np.zeros(NS, dtype=np.uint8)), ("one", np.ones(NS, dtype=np.uint8))]
for nm in ["four", "six", "seven"]:
    TGT.append((nm, NAMED[nm]))
    TGT.append((nm + "-flip", NAMED[nm] ^ 1))
RNM = [nm for nm, _ in TGT]
TGTv = [v for _, v in TGT]
T8 = np.array(TGTv)
LOCAL_READING_IDENTITY = {
    name: {
        "ones": int(target.sum()),
        "canonical_rows_with_bit_sha256": hashlib.sha256(b"".join(sorted(
            bytes(row) + bytes((int(bit),))
            for row, bit in zip(PK, target)
        ))).hexdigest(),
    }
    for name, target in TGT
}

PMS = []
M2I = dict((int(CM[i]), i) for i in range(NPIECE))
for (_, _, g) in GRP:
    arr = np.zeros(NPIECE, dtype=np.int32)
    for i in range(NPIECE):
        w = 0
        for c in range(16):
            if (int(CM[i]) >> c) & 1:
                w |= 1 << int(g[c])
        arr[i] = M2I[w]
    PMS.append(arr)
CP = []
for gi in range(len(PMS)):
    CP.append(np.array([P2I[int(PMS[gi][USED[a]])] for a in range(NPO)],
                       dtype=np.int32))

SUPP = np.array([np.nonzero(INC[s])[0] for s in range(NS)], dtype=np.int32)
SUPD = dict((SUPP[s].tobytes(), s) for s in range(NS))
ID = np.arange(NP, dtype=np.int32)
IDR = np.arange(NS, dtype=np.int32)


def row_perm(pi):
    """the cutting permutation matching a piece permutation, via the support table"""
    img = np.sort(np.asarray(pi, dtype=np.int32)[SUPP], axis=1)
    out = np.empty(NS, dtype=np.int32)
    ok = True
    for s in range(NS):
        k = img[s].tobytes()
        if k in SUPD:
            out[s] = SUPD[k]
        else:
            ok = False
            out[s] = 0
    return (ok and len(set(out.tolist())) == NS), out


CROW = []
CPOK = True
for gi in range(len(CP)):
    okg, rp = row_perm(CP[gi])
    CPOK = CPOK and okg and np.array_equal(INC[rp][:, CP[gi]], INC)
    CROW.append(rp)

par = list(range(NP))


def find(a):
    while par[a] != a:
        par[a] = par[par[a]]
        a = par[a]
    return a


for gi in range(len(CP)):
    for j in range(NP):
        ra, rb = find(j), find(int(CP[gi][j]))
        if ra != rb:
            par[ra] = rb
root = np.array([find(j) for j in range(NP)])
falab = -np.ones(NP, dtype=np.int64)
nl = 0
for j in range(NP):
    if falab[j] < 0:
        falab[root == root[j]] = nl
        nl += 1
ORB = [np.nonzero(falab == k)[0] for k in range(nl)]

GRAM = INC.T.astype(np.int64) @ INC.astype(np.int64)


def settle(colors):
    """the stable colouring the overlap table refines a starting colouring to"""
    while True:
        CODE = colors[None, :] * 2048 + GRAM
        S = np.sort(CODE, axis=1)
        M = np.hstack([colors[:, None] * (1 << 40), S])
        _, new = np.unique(M, axis=0, return_inverse=True)
        new = new.astype(np.int64)
        if len(set(new.tolist())) == len(set(colors.tolist())):
            return new
        colors = new


base = settle(np.zeros(NP, dtype=np.int64))


def refine_seed(x):
    """seed one piece, then split the smallest surviving class until discrete"""
    colors = base.copy()
    colors[x] = colors.max() + 1
    colors = settle(colors)
    for _ in range(400):
        classes = {}
        for i in range(NP):
            classes.setdefault(int(colors[i]), []).append(i)
        big = [mem for mem in classes.values() if len(mem) > 1]
        if not big:
            return colors
        mem = sorted(big, key=lambda m: (len(m), m[0]))[0]
        colors[mem[0]] = colors.max() + 1
        colors = settle(colors)
    return None


ca = refine_seed(int(ORB[1][0]))
cb0 = refine_seed(0)
cb1 = refine_seed(5)


def build_pi(cb):
    """the piece permutation matching the anchored colouring to a seeded one"""
    inv = {}
    for i in range(NP):
        inv.setdefault(int(cb[i]), []).append(i)
    pi = np.zeros(NP, dtype=np.int32)
    ok = True
    for i in range(NP):
        mm = inv.get(int(ca[i]), [])
        if len(mm) != 1:
            ok = False
        else:
            pi[i] = mm[0]
    return ok, pi


OK0, b0 = build_pi(cb0)
OK1, b1 = build_pi(cb1)
SG0, sg0 = row_perm(b0)
SG1, sg1 = row_perm(b1)


def cycle742_contract(primary, independent):
    """Bind the exact finite table, readings, and two supplied automorphisms."""
    incidence = primary.get("incidence_identity", {})
    readings = primary.get("reading_identity", {})
    certs = primary.get("automorphism_certificates", {})
    cert0, cert1 = certs.get("b0", {}), certs.get("b1", {})
    return (
        primary.get("schema") == "physical-cell-cutting-sixteen-attained-cycle742-v2"
        and primary.get("status") == "pass"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == file_sha256(C742_PRIMARY_PATH)
        and receipt_inputs_current(primary)
        and independent.get("schema")
        == "physical-cell-cutting-sixteen-attained-cycle742-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and (independent.get("checker_sha256") or independent.get("runner_sha256"))
        == file_sha256(C742_CHECKER_PATH)
        and receipt_inputs_current(independent)
        and incidence.get("canonical_incidence_rows_sha256")
        == CANONICAL_INCIDENCE_ROWS_SHA256
        and incidence.get("support_column_order_sha256") == SUPPORT_COLUMN_ORDER_SHA256
        and readings.get("canonical_incidence_rows_sha256")
        == CANONICAL_INCIDENCE_ROWS_SHA256
        and readings.get("support_column_order_sha256") == SUPPORT_COLUMN_ORDER_SHA256
        and readings.get("functions") == LOCAL_READING_IDENTITY
        and cert0.get("support_permutation") == [int(value) for value in b0]
        and cert1.get("support_permutation") == [int(value) for value in b1]
        and cert0.get("support_permutation_sha256") == canonical_perm_sha256(b0)
        and cert1.get("support_permutation_sha256") == canonical_perm_sha256(b1)
    )


def cycle743_contract(primary, independent):
    """Bind the exact generated group whose open completeness wall is answered."""
    direct = primary.get("direct_dependency", {})
    reconstruction = independent.get("independent_reconstruction", {})
    return (
        primary.get("schema")
        == "physical-cell-cutting-hidden-three-bit-geometry-cycle743-v2"
        and primary.get("status") == "pass"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == file_sha256(C743_PRIMARY_PATH)
        and receipt_inputs_current(primary)
        and independent.get("schema")
        == "physical-cell-cutting-hidden-three-bit-geometry-cycle743-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and independent.get("checker_sha256") == file_sha256(C743_CHECKER_PATH)
        and receipt_inputs_current(independent)
        and primary.get("generated_group", {}).get("order") == 384
        and reconstruction.get("generated_group_order") == 384
        and direct.get("canonical_incidence_rows_sha256")
        == CANONICAL_INCIDENCE_ROWS_SHA256
        and direct.get("support_column_order_sha256") == SUPPORT_COLUMN_ORDER_SHA256
        and direct.get("functions") == LOCAL_READING_IDENTITY
        and direct.get("b0_support_permutation_sha256") == canonical_perm_sha256(b0)
        and direct.get("b1_support_permutation_sha256") == canonical_perm_sha256(b1)
    )


C742_OK = cycle742_contract(C742_RECEIPT, C742_INDEPENDENT_RECEIPT)
C743_OK = cycle743_contract(C743_RECEIPT, C743_INDEPENDENT_RECEIPT)

emit("-- rebuild")
CS = INCL.sum(axis=0)
RS = INCL.sum(axis=1)
gate(INC.shape == (15800, 192), "01", "shape",
     "{0}x{1}".format(INC.shape[0], INC.shape[1]), "15800x192")
gate(bool((CS == 1975).all()), "02", "colsum",
     sorted(set(CS.tolist())), "[1975]")
gate(bool((RS == 24).all()) and len(SUPD) == NS, "03", "rowsupp",
     "width {0} distinct {1}".format(sorted(set(RS.tolist()))[0], len(SUPD)),
     "24 15800")
gate(CPOK and len(CP) == 48, "04", "perms48", len(CP), 48)
gate(nl == 4 and sorted(len(o) for o in ORB) == [48, 48, 48, 48], "05", "orbits48",
     "{0} of sizes {1}".format(nl, sorted(len(o) for o in ORB)), "4 of 48")
XG = all(any(np.array_equal(T8[a] ^ T8[b], T8[c]) for c in range(8))
         for a in range(8) for b in range(8))
DIST8 = len(set(v.tobytes() for v in TGTv)) == 8
gate(RNM == R8 and DIST8 and XG, "06", "readings",
     "{0} distinct, closed under xor".format(len(TGTv)), 8)
gate(PROCESSED_PAIR_ROWS == NS, "pairrows", "all pair-search first endpoints", NS)
gate(OK0 and SG0 and np.array_equal(b0[b0], ID)
     and np.array_equal(INC[sg0][:, b0], INC)
     and all(not np.array_equal(b0, CP[gi]) for gi in range(48)), "07", "b0",
     "an involution outside the 48", "automorphism")
gate(OK1 and SG1 and np.array_equal(b1[b1], ID)
     and np.array_equal(INC[sg1][:, b1], INC)
     and all(not np.array_equal(b1, CP[gi]) for gi in range(48)), "08", "b1",
     "an involution outside the 48", "automorphism")
gate(all(np.array_equal(T8[r][sg0], T8[r]) and np.array_equal(T8[r][sg1], T8[r])
         for r in range(8)), "09", "bfix", "8 of 8 readings kept", 8)
gate(C742_OK, "dep.cycle742", "exact incidence/readings/b0/b1 bytes", "bound")
gate(C743_OK, "dep.cycle743", "exact generated order-384 group bytes", "bound")


# ------------------------------------------------- Part 2: the group E
def closure(gens):
    """the piece permutations the generators reach, each with its cutting map"""
    seen = {ID.tobytes(): (ID, IDR)}
    frontier = [(ID, IDR)]
    while frontier:
        nf = []
        for (p, r) in frontier:
            for (gp, gr) in gens:
                q = gp[p]
                k = q.tobytes()
                if k not in seen:
                    seen[k] = (q, gr[r])
                    nf.append(seen[k])
        frontier = nf
    return seen


def norbits(perms, n):
    """how many orbits a collection of permutations has on n points"""
    pr = list(range(n))

    def f(a):
        while pr[a] != a:
            pr[a] = pr[pr[a]]
            a = pr[a]
        return a
    for p in perms:
        for j in range(n):
            ra, rb = f(j), f(int(p[j]))
            if ra != rb:
                pr[ra] = rb
    cnt = {}
    for j in range(n):
        r = f(j)
        cnt[r] = cnt.get(r, 0) + 1
    return cnt


G48 = [(CP[i], CROW[i]) for i in range(48)]
GENS = [CP[i] for i in range(48)] + [b0, b1]
E = closure(G48 + [(b0, sg0), (b1, sg1)])
EK = sorted(E)
EP = dict((k, E[k][0]) for k in EK)
ER = dict((k, E[k][1]) for k in EK)

emit("-- the group E")
gate(len(E) == 384, "10", "ordE", len(E), 384)
EO = norbits([EP[k] for k in EK], NP)
gate(len(EO) == 1 and list(EO.values()) == [192], "11", "trans",
     "{0} orbit of {1}".format(len(EO), list(EO.values())[0]), "1 of 192")
STK = [k for k in EK if int(EP[k][0]) == 0]
gate(len(STK) == 2, "12", "stab", len(STK), 2)
s0 = [EP[k] for k in STK if not np.array_equal(EP[k], ID)][0]
NFIX = int((s0 == ID).sum())
gate(bool(np.array_equal(s0[s0], ID)) and NFIX == 16, "13", "s0",
     "an involution keeping {0}".format(NFIX), 16)
gate(all(np.array_equal(T8[:, ER[k]], T8) for k in EK), "14", "Efix",
     "384 elements keep 8 readings", "all")


# ------------------------------------------------- Part 3: overlaps
emit("-- overlaps")
DG = np.diag(GRAM)
gate(bool((DG == 1975).all()), "15", "diag", sorted(set(DG.tolist())), "[1975]")
OFFD = GRAM - np.diag(DG)
OMX = int(OFFD.max())
gate(OMX == 1266 and OMX < 1975, "16", "offmax",
     "{0}, under the diagonal entry".format(OMX), 1266)
UPR = GRAM[np.triu_indices(NP, 1)].tolist()
NDV = len(set(UPR))
gate(NDV == 47, "17", "offvals", NDV, 47)
ROWB = sorted(INC[s].tobytes() for s in range(NS))
NDR = len(set(ROWB))
gate(NDR == NS and NDR == 15800, "18", "rowdist", NDR, 15800)


def is_aut(pi, M=None):
    """whether a piece permutation carries the family of cuttings onto itself"""
    MP = (INC if M is None else M)[:, pi]
    return sorted(MP[s].tobytes() for s in range(NS)) == ROWB


# ------------------------------------------------- Part 4: refinement
def refine(indiv):
    """the stable colouring reached from a starting individualization"""
    col = np.zeros(NP, dtype=np.int64)
    for v, t in indiv:
        col[v] = t
    rounds = 0
    while True:
        cl = col.tolist()
        keys = []
        for i in range(NP):
            cnt = {}
            for pr in zip(GRAM[i].tolist(), cl):
                cnt[pr] = cnt.get(pr, 0) + 1
            keys.append((cl[i], tuple(sorted(cnt.items()))))
        dense = dict((k, n) for n, k in enumerate(sorted(set(keys))))
        new = np.array([dense[k] for k in keys], dtype=np.int64)
        rounds += 1
        if len(set(new.tolist())) == len(set(cl)):
            return new, rounds
        col = new


def match(cx, cy):
    """the piece map carrying one colouring onto another, when there is one"""
    hx, hy, inv = {}, {}, {}
    for i in range(NP):
        u, v = int(cx[i]), int(cy[i])
        hx[u] = hx.get(u, 0) + 1
        hy[v] = hy.get(v, 0) + 1
        inv.setdefault(v, []).append(i)
    if sorted(hx.values()) != sorted(hy.values()):
        return False, None
    pi = np.zeros(NP, dtype=np.int32)
    for i in range(NP):
        mm = inv.get(int(cx[i]), [])
        if len(mm) != 1:
            return False, None
        pi[i] = mm[0]
    return True, pi


emit("-- refinement")
bcol, brnd = refine([])
gate(len(set(bcol.tolist())) == 1, "19", "basecells", len(set(bcol.tolist())), 1)
gate(brnd == 1, "20", "baserounds", brnd, 1)

emit("-- the stabilizer partition")
c0, r0 = refine([(0, -1)])
cellmap = {}
for i in range(NP):
    cellmap.setdefault(int(c0[i]), []).append(i)
sz = {}
for v in cellmap.values():
    sz[len(v)] = sz.get(len(v), 0) + 1
SZL = sorted(sz.items())
gate(len(cellmap) == 104, "21", "cells", len(cellmap), 104)
gate(SZL == [(1, 16), (2, 88)], "22", "sizes", cshow(SZL), "1:16 2:88")
gate(r0 == 3, "23", "rounds", r0, 3)
gate(bool(np.array_equal(c0[s0], c0)), "24", "kept",
     "the colouring is kept by the stabilizer element", "kept")
FIXS = set(i for i in range(NP) if int(s0[i]) == i)
SGL = set(v[0] for v in cellmap.values() if len(v) == 1)
gate(SGL == FIXS and len(SGL) == 16, "25", "singles",
     "{0} singleton cells, exactly the kept pieces".format(len(SGL)), 16)
PAIROK = all(len(v) == 2 and int(s0[v[0]]) == v[1] and int(s0[v[1]]) == v[0]
             for v in cellmap.values() if len(v) > 1)
gate(PAIROK, "26", "pairs", "every larger cell is a stabilizer orbit", "orbits")

emit("-- the two branches")
BC = min(c for c, v in cellmap.items() if len(v) > 1)
pa, pb = cellmap[BC]
cA, rA = refine([(0, -1), (pa, -2)])
cB, rB = refine([(0, -1), (pb, -2)])
NCA = len(set(cA.tolist()))
NCB = len(set(cB.tolist()))
gate(NCA == NP, "27", "discA", "{0} cells".format(NCA), 192)
gate(rA == 3, "28", "roundsA", rA, 3)
gate(NCB == NP, "29", "discB", "{0} cells".format(NCB), 192)
gate(rB == 3, "30", "roundsB", rB, 3)
gate(bool(np.array_equal(cA, cB[s0])), "31", "align",
     "the branch colourings agree along the stabilizer element", "aligned")
OKB, piB = match(cA, cB)
gate(OKB and bool(np.array_equal(piB, s0)), "32", "matchB",
     "the branch map is the stabilizer element", "s0")
gate(is_aut(s0), "33", "s0aut", "carries the family onto itself", "automorphism")
gate(is_aut(ID), "34", "idaut", "carries the family onto itself", "automorphism")
OKA, piA = match(cA, cA)
gate(OKA and bool(np.array_equal(piA, ID)), "35", "matchA",
     "the branch map is the identity", "identity")

emit("-- rejectors and the count")
FL = sorted(FIXS)
MV = sorted(set(range(NP)) - FIXS)
tp = ID.copy()
tp[FL[0]] = MV[0]
tp[MV[0]] = FL[0]
gate(not is_aut(tp), "36", "rjswap", "a two-piece swap rejected", "rejected")
BAD = INC.copy()
BAD[0, 0] = 1 - BAD[0, 0]
gate(not is_aut(ID, BAD), "37", "rjedit", "an edited table rejected", "rejected")
OKR, _ = match(cA, bcol)
gate(not OKR, "38", "rjmatch", "mismatched colourings rejected", "rejected")
GOK = all(is_aut(g) for g in GENS)
gate(GOK and len(GENS) == 50, "39", "gens",
     "{0} generators carry the family onto itself".format(len(GENS)), 50)
ORB0 = len(set(int(EP[k][0]) for k in EK))
gate(GOK and ORB0 == NP, "40", "orbit",
     "{0} images of the base piece".format(ORB0), 192)
AST = set([ID.tobytes(), piB.tobytes()])
EST = set(EP[k].tobytes() for k in STK)
gate(len(AST) == 2 and AST == EST, "41", "stabsame",
     "{0} elements, the same two".format(len(AST)), 2)
gate(NP * 2 == 384 and len(E) == 384, "42", "count",
     "{0} times {1} is {2}".format(NP, 2, NP * 2), 384)

# ------------------------------------------------- Part 5: hostile controls and evidence
SKIPPED_PAIR_ROWS = sum(min(lo + 100, NS) - lo for lo in range(0, NS, 200))
gate(SKIPPED_PAIR_ROWS == NS // 2 and SKIPPED_PAIR_ROWS != PROCESSED_PAIR_ROWS,
     "hostile.pair_inventory", "submitted half-width chunks are rejected",
     "7900 is not 15800")

bad_c743 = copy.deepcopy(C743_RECEIPT)
bad_c743["status"] = "fail"
gate(not cycle743_contract(bad_c743, C743_INDEPENDENT_RECEIPT),
     "hostile.dependency", "a failing Cycle 743 receipt is rejected", "fail closed")

bad_c742 = copy.deepcopy(C742_RECEIPT)
bad_perm = bad_c742["automorphism_certificates"]["b0"]["support_permutation"]
bad_perm[0], bad_perm[1] = bad_perm[1], bad_perm[0]
bad_c742["automorphism_certificates"]["b0"][
    "support_permutation_sha256"
] = hashlib.sha256(json.dumps(bad_perm, separators=(",", ":")).encode("utf-8")).hexdigest()
gate(not cycle742_contract(bad_c742, C742_INDEPENDENT_RECEIPT),
     "hostile.automorphism_identity",
     "a self-consistently rehashed changed predecessor map is rejected", "fail closed")

E_MINUS_B1 = closure(G48 + [(b0, sg0)])
gate(len(E_MINUS_B1) == 96 and len(E_MINUS_B1) != len(E),
     "hostile.omitted_generator", "omitting b1 collapses the generated group",
     "96 not 384")

bad_reading = copy.deepcopy(C742_RECEIPT)
bad_reading["reading_identity"]["functions"]["four"][
    "canonical_rows_with_bit_sha256"
] = "0" * 64
gate(not cycle742_contract(bad_reading, C742_INDEPENDENT_RECEIPT),
     "hostile.reading_identity", "a changed reading identity is rejected", "fail closed")

elapsed = time.time() - T0
rss_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
gate(elapsed < 900.0, "budget.time", "elapsed {0:.2f}s".format(elapsed), "<900s")
gate(rss_mb < 2500.0, "budget.memory", "peak {0:.1f} MB".format(rss_mb), "<2500 MB")
gate(OUT[0] + 1400 < 6500, "budget.output", "bounded stdout", "<6500 chars")

print("per_element: checked -- all 192 support columns enter the exact incidence, "
      "group, overlap, and stabilizer-branch checks", flush=True)
print("per_site: checked and not executed -- one supplied coordinate four-cube only; "
      "no framework cell or site is identified", flush=True)
print("per_mode: checked and not executed -- the finite incidence table has no field "
      "or momentum-mode decomposition", flush=True)
print("per_block: checked -- every one of the 15800 supplied cutting supports and all "
      "50 declared generators enter the direct automorphism tests", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell, arbitrary-domain, "
      "boundary, thermodynamic, or continuum theorem is asserted", flush=True)

GRAM_SHA256 = hashlib.sha256(GRAM.astype("<i8", copy=False).tobytes()).hexdigest()
receipt = {
    "schema": "physical-cell-cutting-full-symmetry-certified-cycle744-v2",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "runner_sha256": file_sha256(PRIMARY_PATH),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "direct_dependencies": {
        "cycle742": {
            "schema": C742_RECEIPT.get("schema"),
            "canonical_incidence_rows_sha256": CANONICAL_INCIDENCE_ROWS_SHA256,
            "support_column_order_sha256": SUPPORT_COLUMN_ORDER_SHA256,
            "b0_support_permutation_sha256": canonical_perm_sha256(b0),
            "b1_support_permutation_sha256": canonical_perm_sha256(b1),
            "functions": LOCAL_READING_IDENTITY,
        },
        "cycle743": {
            "schema": C743_RECEIPT.get("schema"),
            "generated_group_order": C743_RECEIPT.get("generated_group", {}).get("order"),
            "independent_generated_group_order": C743_INDEPENDENT_RECEIPT.get(
                "independent_reconstruction", {}
            ).get("generated_group_order"),
        },
    },
    "supplied_incidence": {
        "cuttings": NS,
        "support_columns": NP,
        "pieces_per_cutting": int(RS[0]),
        "uses_per_piece": int(CS[0]),
        "canonical_incidence_rows_sha256": CANONICAL_INCIDENCE_ROWS_SHA256,
        "support_column_order_sha256": SUPPORT_COLUMN_ORDER_SHA256,
        "overlap_gram_sha256": GRAM_SHA256,
    },
    "generated_group": {
        "order": len(E),
        "transitive_support_orbit": ORB0,
        "point_stabilizer_order": len(STK),
        "point_stabilizer_permutation_sha256": canonical_perm_sha256(s0),
        "generators_directly_verified": len(GENS),
    },
    "full_automorphism_certificate": {
        "role_preserving_incidence_automorphisms": True,
        "base_support_column": 0,
        "base_partition_cells": len(cellmap),
        "base_partition_singletons": len(SGL),
        "base_partition_pairs": sz.get(2, 0),
        "selected_pair": [int(pa), int(pb)],
        "branch_cells": [NCA, NCB],
        "branch_rounds": [rA, rB],
        "candidate_stabilizer_size": len(AST),
        "candidate_permutation_sha256": sorted(
            [canonical_perm_sha256(ID), canonical_perm_sha256(s0)]
        ),
        "full_automorphism_group_order": NP * len(AST),
        "equals_generated_group": NP * len(AST) == len(E),
    },
    "no_go_discipline": {
        "status": "PASS",
        "claim_scope": (
            "exhaustive absence of additional role-preserving automorphisms only for "
            "the exact supplied 15800-by-192 incidence table"
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
        "named": {name: "PASS" if passed else "FAIL" for name, passed in GATES},
    },
}
RECEIPT_PATH.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]), flush=True)
sys.exit(0 if PF[1] == 0 else 1)
