"""Cycle 733: finite column-cost parity and minimum-support theorem.

The cell is the unit four-cube, three lattice directions and one tick, cut into pieces
of least volume. For a set S of columns, the cost of a piece counts the pairs of its
corners that are more than one step apart when only the columns of S are read, and the
cost of a dissection is the sum over its pieces. This runner measures the whole family
of fifteen such costs at once: which of them are blind to how the cell is cut, which
obey a parity law with an exhibited certificate, where that law breaks and why, and
which pieces the minimum principle forces a least cost dissection to use.

The cell, tick graining, corner-simplex domain, and charge are supplied inputs rather
than consequences of the framework axioms.  No solver is called.  Every finite result
is an exhibited certificate checked in integers, a complete exact-cover enumeration,
or exact elimination over a finite field.  Every enumerated positive exact cover is
also checked geometrically before it is called a dissection.
"""

import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md",
    "scripts/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03.py",
    "outputs/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03_receipt_2026-08-03.json",
    "docs/PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md",
    "scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py",
    "outputs/physical_cost_identity_indicator_certificate_cycle731_2026_08_04_receipt_2026-08-04.json",
)
ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = ROOT / (
    "outputs/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04_"
    "receipt_2026-08-04.json"
)


def file_sha256(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


C725_RECEIPT = json.loads((ROOT / AUDIT_INPUT_PATHS[5]).read_text(encoding="utf-8"))
C731_RECEIPT = json.loads((ROOT / AUDIT_INPUT_PATHS[8]).read_text(encoding="utf-8"))

PF = [0, 0]


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


def sec(text):
    print("")
    print(text)


gate(
    C725_RECEIPT.get("bracket_minimal_pieces") == [108, 128]
    and C725_RECEIPT.get("fail") == 0
    and "corner 4-simplex" in C725_RECEIPT.get("supplied_model", ""),
    "dep.c725",
    "Cycle 725 binds the supplied corner-simplex model and exact adjacency bracket",
)
gate(
    C731_RECEIPT.get("claim_type") == "bounded_theorem"
    and C731_RECEIPT.get("totals", {}).get("fail") == 0
    and C731_RECEIPT.get("floor", {}).get("bound") == 108
    and C731_RECEIPT.get("floor", {}).get("support_pieces") == 1792,
    "dep.c731",
    "Cycle 731 binds the spatial floor 108 and its 1792-piece certificate support",
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


sec("the cell and its pieces of least volume")

CORN = [(x, y, z, t) for x in (0, 1) for y in (0, 1) for z in (0, 1) for t in (0, 1)]
V = np.array(CORN, dtype=np.int64)
POS = dict((c, i) for i, c in enumerate(CORN))
PAIRS = list(itertools.combinations(range(5), 2))
SUB = np.array(list(itertools.combinations(range(16), 5)), dtype=np.int64)
VOL = np.abs(det4(V[SUB[:, 1:]] - V[SUB[:, 0]][:, None, :]))
UNI = SUB[VOL == 1]
NPIECE = len(UNI)


def charge(P, cols):
    tot = np.zeros(len(P), dtype=np.int64)
    for a, b in PAIRS:
        d = np.abs(V[P[:, a]][:, cols] - V[P[:, b]][:, cols]).sum(axis=1)
        tot = tot + (d > 1).astype(np.int64)
    return tot


CX = charge(UNI, [0, 1, 2])
CSP = sorted((int(a), int(b)) for a, b in zip(*np.unique(CX, return_counts=True)))
gate(len(SUB) == 4368 and NPIECE == 2672,
     "cell.pieces",
     "{0} five-subsets of the 16 corners, {1} of least volume".format(len(SUB), NPIECE))
gate(CSP == [(3, 64), (4, 384), (5, 1152), (6, 768), (7, 304)],
     "cell.charge", "adjacency charge spectrum {0}".format(CSP))

MM = np.stack([(V[p[1:]] - V[p[0]]).T for p in UNI])
IV = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)
gate(bool((np.einsum("nij,njk->nik", IV, MM) == np.eye(4, dtype=np.int64)).all()),
     "cell.inverse", "every piece matrix inverts exactly over the integers")

sec("the symmetry of the cell")

ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if int(round(np.linalg.det(R.astype(float)))) == 1:
            ROT.append(R)

CEN = np.array([1, 1, 1], dtype=np.int64)
KEEP, G = [], []
for R in ROT:
    good = False
    for tf in (0, 1):
        img = []
        for (x, y, z, t) in CORN:
            w = R @ (2 * np.array([x, y, z], dtype=np.int64) - CEN) + CEN
            if bool((w & 1).any()):
                img = None
                break
            key = (int(w[0]) // 2, int(w[1]) // 2, int(w[2]) // 2, (1 - t) if tf else t)
            if key not in POS:
                img = None
                break
            img.append(POS[key])
        if img is not None:
            G.append((R, tf, np.array(img, dtype=np.int64)))
            good = True
    if good:
        KEEP.append(R)
gate(len(KEEP) == 24 and len(G) == 48,
     "sym.group", "{0} proper rotations kept, {1} elements once the tick flip is "
                  "included".format(len(KEEP), len(G)))

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
SZ = np.bincount(LAB, minlength=NORB)
gate(NORB == 57 and sorted(set(int(t) for t in SZ)) == [16, 48] and int(SZ.sum()) == NPIECE,
     "sym.orbits", "{0} piece orbits, sizes {1}, summing to {2}".format(
         NORB, sorted(set(int(t) for t in SZ)), int(SZ.sum())))
gate(all(int(CX[LAB == o].max()) == int(CX[LAB == o].min()) for o in range(NORB)),
     "sym.constant", "adjacency charge is constant on every piece orbit")

sec("sample points, none of them on a piece boundary")

OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
gate(CB == 3 and SB == 12810,
     "pts.weights", "barycentric bound {0}, superincreasing weight total {1}".format(CB, SB))

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
PORB = np.array([lab[k] for k in KEYS], dtype=np.int64)

INC = np.zeros((NPIECE, NQ), dtype=np.int16)
QT = Q.T
face = 0
MASK = []
for i in range(NPIECE):
    lam = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lam.sum(axis=0)
    face += int(((lam == 0).any(axis=0) | (tot == SB)).sum())
    ins = (lam > 0).all(axis=0) & (tot < SB)
    INC[i] = ins.astype(np.int16)
    b = 0
    for j in np.flatnonzero(ins):
        b |= 1 << int(j)
    MASK.append(b)
MI = INC.astype(np.int64)
gate(NQ == 2736 and coll == 0 and face == 0,
     "pts.generic", "{0} sample points, no collision, {1} lying on any piece "
                    "boundary".format(NQ, face))
PSZ = sorted(set(int(t) for t in np.bincount(PORB)))
gate(len(set(int(o) for o in PORB)) == NORB and PSZ == [48],
     "pts.orbits", "they fall into {0} orbits of the full symmetry, sizes {1}, one orbit "
                   "for each piece orbit".format(NORB, PSZ))
RS = (int(MI.sum(axis=1).min()), int(MI.sum(axis=1).max()))
CS = (int(MI.sum(axis=0).min()), int(MI.sum(axis=0).max()))
gate(RS == (6, 409) and CS == (90, 224),
     "pts.incidence", "points inside a piece range over {0}, pieces containing a point "
                      "over {1}, so no row and no column of the incidence is "
                      "empty".format(RS, CS))

def solvep(A, b, P):
    """Gauss-Jordan over the field with P elements: a solution, or None, plus the rank"""
    n, w = A.shape
    Aw = np.zeros((n, w + 1), dtype=np.int16)
    Aw[:, :w] = np.remainder(A, P)
    Aw[:, w] = np.remainder(b, P)
    piv, r = [], 0
    for c in range(w):
        nz = np.flatnonzero(Aw[r:, c])
        if not len(nz):
            continue
        pr = r + int(nz[0])
        if pr != r:
            Aw[[r, pr]] = Aw[[pr, r]]
        inv = pow(int(Aw[r, c]), P - 2, P)
        if inv != 1:
            Aw[r] = np.remainder(Aw[r] * inv, P)
        col = Aw[:, c].copy()
        col[r] = 0
        nzr = np.flatnonzero(col)
        if len(nzr):
            if P == 2:
                Aw[nzr] = Aw[nzr] ^ Aw[r]
            else:
                Aw[nzr] = np.remainder(Aw[nzr] - np.outer(col[nzr], Aw[r]), P)
        piv.append(c)
        r += 1
        if r == n:
            break
    for i in range(r, n):
        if not Aw[i, :w].any() and Aw[i, w]:
            return None, r
    x = np.zeros(w, dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = int(Aw[i, w])
    return x, r

AP = np.zeros((NPIECE, NQ + 1), dtype=np.int16)
AP[:, :NQ] = MI
AP[:, NQ] = 1

WIT = [
    ((1,15), (1,31), (2,15), (2,31), (3,19), (3,23), (3,63), (4,15), (5,15), (5,31), (6,7),
     (6,11), (8,29), (8,45), (8,53), (9,5), (9,51), (9,52), (12,18), (12,22), (12,26),
     (12,30), (12,36), (12,37)),
    ((0,6), (0,32), (1,60), (13,6), (15,18), (15,25), (15,30), (15,52), (18,12), (19,20),
     (22,44), (23,0), (28,40), (28,48), (28,51), (29,17), (29,19), (29,30), (31,4),
     (34,29), (35,62), (37,38), (38,38), (41,47)),
    ((0,6), (0,32), (1,60), (13,6), (15,18), (15,25), (15,30), (15,52), (18,12), (19,20),
     (22,44), (23,0), (28,40), (28,48), (28,51), (29,17), (29,19), (29,30), (31,4),
     (34,29), (35,62), (37,37), (39,62), (41,47)),
    ((0,9), (4,31), (4,35), (4,62), (5,63), (8,27), (9,8), (10,42), (12,12), (13,18),
     (13,46), (14,32), (17,32), (23,21), (25,13), (25,17), (27,41), (33,55), (35,41),
     (36,10), (36,57), (39,10), (40,17), (40,50)),
    ((0,9), (4,35), (4,62), (5,13), (5,63), (8,27), (8,51), (9,32), (10,42), (12,12),
     (13,18), (13,46), (14,32), (17,32), (23,21), (25,17), (27,34), (27,41), (33,55),
     (35,41), (36,57), (39,10), (40,17), (40,50)),
    ((0,9), (4,35), (4,62), (5,13), (5,63), (8,27), (8,51), (9,32), (10,42), (12,12),
     (13,18), (13,42), (14,32), (23,21), (24,21), (25,17), (27,34), (27,41), (33,55),
     (35,41), (36,57), (39,10), (40,17), (40,50)),
    ((0,9), (4,35), (4,62), (5,13), (5,55), (8,27), (8,51), (9,32), (10,32), (12,18),
     (13,18), (13,42), (14,32), (23,21), (24,25), (25,17), (27,34), (27,41), (28,50),
     (35,41), (36,57), (38,51), (40,17), (40,50)),
    ((0,9), (4,35), (4,62), (5,13), (5,51), (8,27), (8,51), (9,32), (10,32), (13,18),
     (13,42), (14,32), (23,21), (24,9), (25,17), (27,34), (27,41), (33,27), (33,55),
     (35,41), (36,57), (38,51), (40,17), (40,50)),
    ((0,9), (4,35), (4,62), (5,13), (5,51), (8,27), (8,51), (9,32), (10,32), (13,18),
     (13,42), (14,32), (23,21), (24,8), (25,17), (27,34), (27,46), (33,26), (33,55),
     (33,59), (35,41), (36,57), (38,51), (40,26)),
    ((0,9), (4,35), (4,62), (5,13), (5,51), (8,27), (8,51), (9,32), (10,32), (13,18),
     (13,42), (14,32), (23,21), (24,8), (25,17), (27,34), (27,46), (33,26), (33,55),
     (33,59), (35,43), (36,57), (36,58), (38,51)),
    ((0,9), (4,23), (4,35), (4,62), (5,51), (8,33), (10,32), (13,18), (13,42), (14,32),
     (22,45), (24,8), (25,17), (27,46), (29,34), (31,8), (33,26), (33,55), (33,59),
     (34,56), (35,43), (38,48), (39,17), (39,18)),
    ((0,6), (0,32), (1,60), (13,6), (15,18), (15,25), (15,30), (15,52), (18,12), (19,20),
     (22,41), (25,25), (28,40), (28,48), (28,51), (29,17), (29,19), (29,30), (31,4), (34,29),
     (35,62), (37,38), (38,38), (41,47)),
]
DIS = [sorted((a << 6) + b for a, b in row) for row in WIT]

ALLQ = (1 << NQ) - 1
NEG = [np.array(t, dtype=np.int64)
       for t in itertools.product((-1, 0, 1), repeat=4) if any(t)]


def separated(idx):
    pts = [V[UNI[i]] for i in idx]
    fac = []
    for i in idx:
        Iv = IV[i]
        fac.append([Iv[k] for k in range(4)] + [-Iv.sum(axis=0)])
    good, total = 0, 0
    for a in range(len(idx)):
        for b in range(a + 1, len(idx)):
            total += 1
            for nv in NEG + fac[a] + fac[b]:
                p, q = pts[a] @ nv, pts[b] @ nv
                if int(p.max()) <= int(q.min()) or int(q.max()) <= int(p.min()):
                    good += 1
                    break
    return good, total


def is_dissection(idx):
    g, t = separated(idx)
    cov = 0
    for i in idx:
        cov |= MASK[i]
    return len(idx) == 24 and len(set(idx)) == 24 and g == t and cov == ALLQ

FLOOR_U = [(0, -36), (4, 144), (19, 64), (20, -36), (34, 216), (35, 135),
           (44, -216), (45, 36), (51, -72), (52, 163), (53, -172), (54, -118)]
FLOOR_D, FLOOR_Z = 216, 756

ROWM = np.zeros((NPIECE, NORB), dtype=np.int64)
for o in range(NORB):
    ROWM[:, o] = MI[:, PORB == o].sum(axis=1)


def build(dat):
    u = np.zeros(NORB, dtype=np.int64)
    for j, w in dat:
        u[j] = w
    return u


def slacks(u, Z, D, upper):
    s = (ROWM @ u + Z) - D * CX
    return s if upper else -s


sec("the exhibited dissections, including the monotone stencil")

KU = []
for pm in itertools.permutations(range(4)):
    cur, path = [0, 0, 0, 0], [POS[(0, 0, 0, 0)]]
    for c in pm:
        cur[c] = 1
        path.append(POS[tuple(cur)])
    KU.append(posp[tuple(sorted(path))])
KU = sorted(KU)
DSS = [list(d) for d in DIS] + [KU]
gate(len(set(KU)) == 24 and all(is_dissection(list(d)) for d in DSS), "wit.valid",
     "{0} exhibited lists and the monotone stencil, one piece per ordering of the four "
     "columns, each cut the cell into {1} pieces of least volume".format(len(DIS), 24))


sec("the family of nearest neighbour costs")

SETS = [list(S) for k in range(1, 5) for S in itertools.combinations(range(4), k)]
CH = dict((tuple(S), charge(UNI, S)) for S in SETS)
NZ = [tuple(S) for S in SETS if int(CH[tuple(S)].max()) > 0]
ZS = [tuple(S) for S in SETS if int(CH[tuple(S)].max()) == 0]
gate(len(ZS) == 4 and len(NZ) == 11 and all(len(S) == 1 for S in ZS), "fam.trivial",
     "of {0} column sets the {1} single columns give the zero cost, leaving {2}".format(
         len(SETS), len(ZS), len(NZ)))

gate(all(bool((CH[tuple(P)] <= CH[tuple(Q2)]).all())
         for P in SETS for Q2 in SETS if set(P) <= set(Q2)), "fam.monotone",
     "cost never drops when a column is added, on all {0} sets".format(len(SETS)))

CLS = {}
for S in NZ:
    CLS.setdefault((len([c for c in S if c < 3]), 3 in S), []).append(S)
SIZ = sorted(len(v) for v in CLS.values())
gate(len(CLS) == 5 and SIZ == [1, 1, 3, 3, 3], "fam.classes",
     "the {0} split by spatial count and tick into {1} classes of sizes {2}".format(
         len(NZ), len(CLS), SIZ))

PP = np.zeros((len(G), NPIECE), dtype=np.int64)
for a in range(len(G)):
    gp = G[a][2]
    for i in range(NPIECE):
        PP[a, i] = posp[tuple(sorted(int(gp[c]) for c in UNI[i]))]
gate(all(len(set(int(v) for v in PP[a])) == NPIECE for a in range(len(G))), "fam.permute",
     "each of the {0} symmetries permutes the {1} pieces".format(len(G), NPIECE))

PRS, JOI = 0, 0
for k in CLS:
    for P in CLS[k]:
        for Q2 in CLS[k]:
            PRS += 1
            if any(bool((CH[Q2] == CH[P][PP[a]]).all()) for a in range(len(G))):
                JOI += 1
gate(PRS == 29 and JOI == PRS, "fam.symmetry",
     "all {0} ordered pairs inside a class are joined by an exhibited symmetry".format(PRS))

KON = [S for S in NZ if all(len(set(int(v) for v in CH[S][LAB == o])) == 1
                            for o in range(NORB))]
gate(KON == [(0, 1, 2), (0, 1, 2, 3)], "fam.invariant",
     "exactly {0} of the {1} are constant on the {2} piece orbits, {3}".format(
         len(KON), len(NZ), NORB, KON))


sec("no cost in the family is blind to the cut")

gate(all(len(set(int(CH[S][np.array(d)].sum()) for d in DSS)) >= 2 for S in NZ),
     "cut.varies",
     "every one of the {0} takes at least two values on the {1} dissections".format(
         len(NZ), len(DSS)))


sec("parity is a law for the ten proper column sets")

CERT = {}
for S in NZ:
    x, rk = solvep(AP, (CH[S] & 1).astype(np.int16), 2)
    CERT[S] = None if x is None else (np.array([int(v) for v in x[:NQ]], dtype=np.int64),
                                      int(x[NQ]))
PROP = [S for S in NZ if len(S) < 4]
gate(len(PROP) == 10 and all(CERT[S] is not None for S in PROP)
     and CERT[(0, 1, 2, 3)] is None, "par.certs",
     "each of the {0} proper sets carries a weighting over the field with two elements "
     "and the full set carries none".format(len(PROP)))

BADR = max(int((((MI @ CERT[S][0] + CERT[S][1] - CH[S]) & 1) != 0).sum()) for S in PROP)
gate(BADR == 0, "par.rows",
     "the weightings reproduce the cost of every one of the {0} pieces, wrong rows "
     "{1}".format(NPIECE, BADR))

SUP = [int(CERT[S][0].sum()) for S in PROP]
gate(all((s & 1) == 0 for s in SUP), "par.even",
     "every support is even, and the piece count {0} is even too, so the constant drops "
     "out of the total: supports {1}".format(24, SUP))

gate(all((int(CH[S][np.array(d)].sum()) & 1) == (int(CERT[S][0].sum()) & 1)
         for S in PROP for d in DSS), "par.law",
     "cost agrees with support modulo two on all {0} dissections".format(len(DSS)))

APR = AP[:, ::-1]
SEC, DIFF = {}, 0
for S in PROP:
    y, _ = solvep(APR, (CH[S] & 1).astype(np.int16), 2)
    v = np.array([int(t) for t in y[::-1]], dtype=np.int64)
    SEC[S] = v
    if not bool((v[:NQ] == CERT[S][0]).all()):
        DIFF += 1
gate(DIFF > 0 and all((int(SEC[S][:NQ].sum()) & 1) == (int(CERT[S][0].sum()) & 1)
                      for S in PROP)
     and max(int((((MI @ SEC[S][:NQ] + SEC[S][NQ] - CH[S]) & 1) != 0).sum())
             for S in PROP) == 0, "par.unique",
     "a second weighting found by eliminating in the opposite order differs on {0} of "
     "the {1} sets, yet always has the same support parity, so the law does not depend "
     "on which weighting is picked".format(DIFF, len(PROP)))


sec("the parity law breaks exactly at the full column set")

C4 = CH[(0, 1, 2, 3)]
COST = sorted(set(int(C4[np.array(d)].sum()) for d in DSS))
gate(any((c & 1) == 1 for c in COST) and any((c & 1) == 0 for c in COST), "brk.odd",
     "the full cost takes both parities on exhibited dissections: {0}".format(COST))

DU = [4, 52, 228, 839]
CV = MI[np.array(DU)].sum(axis=0)
DSUM = int(C4[np.array(DU)].sum())
gate(sorted(set(int(v) for v in CV)) == [0, 2] and (DSUM & 1) == 1, "brk.dual",
     "{0} pieces cover {1} points exactly twice and the rest not at all, with odd cost "
     "sum {2}".format(len(DU), int((CV == 2).sum()), DSUM))

DROP = []
for k in range(len(DU)):
    sub = np.array([DU[j] for j in range(len(DU)) if j != k])
    cv = MI[sub].sum(axis=0)
    DROP.append(int((cv & 1).sum()) == 0 and (int(C4[sub].sum()) & 1) == 1)
gate(not any(DROP), "brk.minimal",
     "dropping any one of the {0} destroys the even cover".format(len(DU)))


sec("where the odd part of the full cost lives")

MIX = np.zeros(NPIECE, dtype=np.int64)
for i in range(NPIECE):
    W = V[UNI[i]]
    m = 0
    for a, b in itertools.combinations(range(5), 2):
        dd = np.abs(W[a] - W[b])
        if int(dd[3]) == 1 and int(dd[:3].sum()) == 1:
            m += 1
    MIX[i] = m
gate(bool((CX == CH[(0, 1, 2)]).all()) and bool((C4 == CX + MIX).all()), "spl.exact",
     "the full cost is the spatial cost plus the count of pairs that step in the tick "
     "and in one lattice direction, on all {0} pieces".format(NPIECE))

gate(int((C4 == CX).sum()) == 64, "spl.needed",
     "without that second term the identity survives on only {0} pieces".format(
         int((C4 == CX).sum())))

gate(all((int(CX[np.array(d)].sum()) & 1) == 0 for d in DSS), "spl.carries",
     "the spatial cost is even on every exhibited dissection, so the parity of the full "
     "cost is carried entirely by the second term")


sec("the floor of the full cost is exact, with no certificate needed")

VU, CU = np.unique(C4, return_counts=True)
SPEC = [(int(a), int(b)) for a, b in zip(VU, CU)]
LO = int(C4.min())
gate(LO == 6 and SPEC[0] == (6, 400), "flo.least",
     "the cost of a single piece runs over {0}".format(SPEC))

gate(min(COST) == 24 * LO, "flo.bound",
     "no piece costs under {0}, so no dissection costs under {1}; what is measured here "
     "is that {1} is reached, by the monotone stencil".format(LO, 24 * LO))


sec("the minimum principle forces four orbits of pieces")

MINP = [i for i in range(NPIECE) if int(C4[i]) == LO]
BY, MK = {}, dict((i, MASK[i]) for i in MINP)
for i in MINP:
    for j in np.flatnonzero(MI[i]):
        BY.setdefault(int(j), []).append(i)
SOL, NODE = [], [0]


def rec(cov, chosen):
    NODE[0] += 1
    if cov == ALLQ:
        if len(chosen) == 24:
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
gate(len(MINP) == 400 and NODE[0] == 502838 and len(SOL) == 15800, "for.count",
     "a complete search over the {0} pieces of least cost visits {1} nodes and finds {2} "
     "dissections".format(len(MINP), NODE[0], len(SOL)))

SEEN, OSZ = set(), []
for s in SOL:
    if s in SEEN:
        continue
    fam = set()
    for a in range(len(G)):
        fam.add(tuple(sorted(int(PP[a][i]) for i in s)))
    OSZ.append(len(fam))
    SEEN |= fam
gate(len(OSZ) == 391 and sorted(set(OSZ)) == [8, 12, 24, 48] and len(SEEN) == len(SOL),
     "for.orbits", "they fall into {0} orbits of sizes {1}, covering all {2}".format(
         len(OSZ), sorted(set(OSZ)), len(SEEN)))

# Sample exact coverage is necessary for a dissection, but is not by itself a
# geometric proof.  Check one representative of every symmetry orbit with the
# independent separating-direction predicate; symmetry carries that exact
# convex-geometric certificate to every member of the orbit.
GEO_REPS, GEO_PAIRS, GEO_OK = [], 0, True
geo_seen = set()
for s in SOL:
    if s in geo_seen:
        continue
    GEO_REPS.append(s)
    good, total = separated(list(s))
    GEO_PAIRS += total
    GEO_OK = GEO_OK and good == total and is_dissection(list(s))
    for a in range(len(G)):
        geo_seen.add(tuple(sorted(int(PP[a][i]) for i in s)))
gate(GEO_OK and len(GEO_REPS) == len(OSZ) and len(geo_seen) == len(SOL)
     and GEO_PAIRS == 391 * 276,
     "for.geometry",
     "all {0} sample-cover orbits have geometric dissection representatives; {1} pair "
     "certificates checked and symmetry covers all {2} solutions".format(
         len(GEO_REPS), GEO_PAIRS, len(geo_seen)))

USED = sorted(set(i for s in SOL for i in s))
FOUR = sorted(set(int(LAB[i]) for i in USED))
POOL = [i for i in MINP if int(LAB[i]) in set(FOUR)]
gate(len(FOUR) == 4 and len(USED) == 192 and len(POOL) == len(USED)
     and sorted(int(SZ[o]) for o in FOUR) == [48, 48, 48, 48], "for.pool",
     "the pieces they use are {0} whole orbits, {1} pieces; the other {2} pieces of least "
     "cost are never used".format(len(FOUR), len(USED), len(MINP) - len(USED)))

NEED = []
for o in FOUR:
    KEEP = [i for i in MINP if int(LAB[i]) != o]
    MK2 = dict((i, MASK[i]) for i in KEEP)
    BY2 = {}
    for i in KEEP:
        for j in np.flatnonzero(MI[i]):
            BY2.setdefault(int(j), []).append(i)
    HIT = []

    def rec2(cov, chosen):
        if cov == ALLQ:
            if len(chosen) == 24:
                HIT.append(1)
            return
        rem = ALLQ & ~cov
        j = (rem & -rem).bit_length() - 1
        for i in BY2.get(j, []):
            if MK2[i] & cov:
                continue
            chosen.append(i)
            rec2(cov | MK2[i], chosen)
            chosen.pop()

    rec2(0, [])
    NEED.append((len(KEEP), len(HIT)))
gate(len(NEED) == 4 and all(a == len(MINP) - 48 and b == 0 for a, b in NEED), "for.needed",
     "and every one of the four is needed: drop any one and the remaining {0} pieces of "
     "least cost admit no dissection at all".format(NEED[0][0]))

KC = sorted((o, sum(1 for i in KU if int(LAB[i]) == o))
            for o in set(int(LAB[i]) for i in KU))
gate([o for o, _ in KC] == FOUR and all(c == 6 for _, c in KC), "for.stencil",
     "the monotone stencil takes six pieces from each of those {0}".format(len(FOUR)))

FS = slacks(build(FLOOR_U), FLOOR_Z, FLOOR_D, False)
ON = set(i for i in range(NPIECE) if int(FS[i]) == 0)
gate(all(int(CX[np.array(s)].sum()) == 108 for s in SOL)
     and all(int(MIX[np.array(s)].sum()) == 36 for s in SOL)
     and set(USED) <= ON, "for.split",
     "every one of them splits as spatial {0} and second term {1}, and every piece it "
     "uses sits on the exhibited spatial floor support of {2}".format(108, 36, len(ON)))

BYM = {}
for i in range(NPIECE):
    BYM.setdefault(MASK[i], []).append(i)
HOL, ALT, SELF = 0, 0, 0
for s in SOL:
    tot = 0
    for j in range(24):
        tot |= MASK[s[j]]
    for k in range(24):
        HOL += 1
        fit = BYM.get(ALLQ & ~(tot & ~MASK[s[k]]), [])
        SELF += 1 if s[k] in fit else 0
        ALT += sum(1 for i in fit if i != s[k])
gate(len(BYM) == NPIECE and SELF == HOL and ALT == 0, "for.rigid",
     "the {0} footprints are distinct, and of the {1} holes made by removing one piece "
     "each is filled by the piece just removed and by no other".format(len(BYM), HOL))


sec("what can see which pieces the minimum principle keeps out")

REST = [i for i in MINP if int(LAB[i]) not in set(FOUR)]
SPL = dict((nm, {}) for nm in ("pool", "rest"))
for nm, grp in (("pool", POOL), ("rest", REST)):
    for i in grp:
        key = (int(CX[i]), int(MIX[i]))
        SPL[nm][key] = SPL[nm].get(key, 0) + 1
gate(set(SPL["pool"]) < set(SPL["rest"]), "sep.blind",
     "the pair of costs that the symmetries keep fixed is blind to the exclusion; kept "
     "{0}, left out {1}".format(sorted(SPL["pool"].items()), sorted(SPL["rest"].items())))

VP = set(tuple(int(CH[S][i]) for S in NZ) for i in POOL)
VR = set(tuple(int(CH[S][i]) for S in NZ) for i in REST)
gate(len(VP) == 12 and len(VR) == 13 and len(VP & VR) == 0, "sep.sharp",
     "the whole family is not blind: {0} cost vectors on the kept pieces, {1} on those "
     "left out, {2} in common".format(len(VP), len(VR), len(VP & VR)))

ALLV = set(tuple(int(CH[S][i]) for S in NZ) for i in MINP)
CTRL = []
for ky in (lambda i: i, lambda i: (int(CX[i]), i), lambda i: (int(LAB[i]), i)):
    ORD = sorted(MINP, key=ky)
    VA = set(tuple(int(CH[S][i]) for S in NZ) for i in ORD[:len(POOL)])
    VB = set(tuple(int(CH[S][i]) for S in NZ) for i in ORD[len(POOL):])
    CTRL.append(len(VA & VB))
gate(len(ALLV) == len(VP) + len(VR) and min(CTRL) > 0, "sep.level",
     "so the kept pieces are exactly a union of level sets of the family, {0} of the {1} "
     "carried by any piece of least cost; three other splits into the same two sizes share "
     "{2} vectors, so a clean separation is not automatic".format(len(VP), len(ALLV), CTRL))


print("")
print("per_element: checked all 2672 minimal pieces for the eleven costs, ten parity "
      "certificates, the full-set dual obstruction, and the least-cost support partition")
print("per_site: checked and not executed — the supplied theorem has no lattice-site field; "
      "its smallest resolved objects are one-cell corner simplices and sample points")
print("per_mode: checked and not executed — no spectral or mode decomposition occurs in "
      "this finite incidence and exact-cover theorem")
print("per_block: checked the complete supplied one-cell by one-tick four-box, all 2672 "
      "minimal pieces, all 15800 least-cost dissections, and all 391 symmetry orbits")
print("lattice_wide: checked and not executed — no multi-cell, arbitrary-tick, boundary, "
      "continuum, or framework-selection extension is asserted")
print("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))

receipt = {
    "claim_type": "bounded_theorem",
    "supplied_model": C725_RECEIPT.get("supplied_model"),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "family": {
        "column_sets": len(SETS),
        "trivial_sets": len(ZS),
        "nontrivial_sets": len(NZ),
        "proper_sets_certified": len(PROP),
        "full_set_dual_pieces": list(DU),
        "full_set_dual_cost": DSUM,
        "certificate_supports": SUP,
    },
    "minimum": {
        "piece_cost": LO,
        "dissection_cost": 24 * LO,
        "least_pieces": len(MINP),
        "exact_cover_nodes": NODE[0],
        "dissections": len(SOL),
        "dissection_orbits": len(OSZ),
        "geometric_representatives": len(GEO_REPS),
        "geometric_pair_checks": GEO_PAIRS,
        "used_piece_orbits": FOUR,
        "used_pieces": len(USED),
        "excluded_pieces": len(REST),
        "holes": HOL,
    },
    "separation": {
        "kept_vectors": len(VP),
        "excluded_vectors": len(VR),
        "intersection": len(VP & VR),
    },
    "cycle731_floor": {"bound": 108, "support_pieces": len(ON)},
    "no_go_discipline": {
        "status": "PASS",
        "negative_assertion_class": "derived_no_go_boundary",
        "checklist": "No-Go Discipline Gate section in the Cycle 733 note",
        "n5_certificate": "five resolution lines in primary stdout and canonical cache",
    },
    "totals": {"pass": PF[0], "fail": PF[1]},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + json.dumps(receipt, sort_keys=True, separators=(",", ":")))
sys.exit(1 if PF[1] else 0)
