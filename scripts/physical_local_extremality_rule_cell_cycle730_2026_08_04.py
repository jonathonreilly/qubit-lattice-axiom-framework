"""Cycle 730: zero-slack endpoint criteria in a supplied one-tick corner model.

The object is the supplied Cycle-725 one-tick corner-simplex model: a four-box
with sixteen corners, twenty-four unimodular pieces per dissection, and a
declared charge counting vertex pairs separated by more than one spatial
nearest-neighbour step.  The Lattice axiom supplies that spatial grading and
the kinetic-isotropy primitive supplies equal tick/edge graining.  Neither
selects the simplex model, cost, physical cell, or tick--Admissibility bridge.

The two integer endpoint certificates decompose the cost of an already-valid
dissection into nonnegative per-piece slacks.  Endpoint equality holds exactly
when all twenty-four slacks vanish.  This is an additive membership criterion;
compatibility, disjointness, and coverage remain global obligations.

The finite support census stores a geometrically checked dissection witness for
every orbit classified as realized.  Excluded floor orbits carry one-step
sample-cover orphan certificates; excluded ceiling orbits carry exhaustive
forced-cover search counts.  No optimiser or external solver is called.  The
runner writes its receipt and exits nonzero on any failed gate.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_LOCAL_EXTREMALITY_RULE_CELL_CYCLE730_NOTE_2026-08-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md",
    "scripts/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03.py",
    "outputs/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03_"
    "receipt_2026-08-03.json",
)
ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = ROOT / (
    "outputs/physical_local_extremality_rule_cell_cycle730_2026_08_04_"
    "receipt_2026-08-04.json"
)

NP = [0, 0]
PAIRS = list(itertools.combinations(range(5), 2))
OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)

FLOOR_U = [(0, 12), (1, 12), (2, 72), (3, 121), (4, -36), (5, -229), (6, -36), (7, 17),
           (8, -97), (10, 217), (13, -23), (14, 12), (15, 12)]
FLOOR_D, FLOOR_Z = 24, 0
CEIL_U = [(0, 3), (1, 3), (2, 23), (3, 34), (4, -10), (5, -70), (6, -12), (7, 8),
          (8, -29), (10, 69), (13, -9), (14, 3), (15, 3)]
CEIL_D, CEIL_Z = 6, 0

NEAR = [[0, 1, 2, 5, 8], [0, 2, 5, 6, 14], [0, 2, 5, 10, 14], [0, 4, 5, 6, 12],
        [0, 5, 6, 12, 14], [0, 5, 8, 10, 14], [0, 5, 8, 12, 14], [1, 2, 3, 7, 11],
        [1, 2, 5, 7, 8], [1, 2, 7, 8, 10], [1, 2, 7, 11, 15], [1, 2, 10, 11, 15],
        [1, 5, 7, 12, 13], [1, 7, 8, 9, 10], [1, 7, 9, 13, 14], [1, 7, 12, 13, 14],
        [1, 8, 9, 13, 14], [1, 8, 12, 13, 14], [1, 9, 10, 11, 15], [2, 5, 6, 7, 10],
        [5, 6, 7, 10, 14], [7, 8, 9, 10, 15], [7, 8, 10, 14, 15], [7, 9, 13, 14, 15]]

FLOOR_ABSENT = [16, 17, 22, 23, 26, 27, 30, 31, 34, 35, 36, 37, 47]
FLOOR_SEARCHED = [16, 17, 22, 23, 34, 35, 36, 37, 47]
CEIL_ABSENT = [9, 10]


def gate(ok, name, detail):
    NP[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail)


def sec(text):
    print(text)


def file_sha256(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


C725_RECEIPT = json.loads(
    (ROOT / AUDIT_INPUT_PATHS[-1]).read_text(encoding="utf-8")
)
gate(
    C725_RECEIPT.get("bracket_minimal_pieces") == [108, 128]
    and C725_RECEIPT.get("fail") == 0
    and "corner 4-simplex" in C725_RECEIPT.get("supplied_model", ""),
    "the Cycle 725 supplied-model dependency is exact",
    "contained minimal-piece bracket {0}".format(
        C725_RECEIPT.get("bracket_minimal_pieces")
    ),
)


def det4(A):
    """exact integer determinants of a batch of 4 by 4 integer matrices"""
    def minors(r0, r1):
        out = {}
        for i in range(4):
            for j in range(i + 1, 4):
                out[(i, j)] = (A[:, r0, i] * A[:, r1, j] - A[:, r0, j] * A[:, r1, i])
        return out
    m, c = minors(0, 1), minors(2, 3)
    return (m[(0, 1)] * c[(2, 3)] - m[(0, 2)] * c[(1, 3)] + m[(0, 3)] * c[(1, 2)]
            + m[(1, 2)] * c[(0, 3)] - m[(1, 3)] * c[(0, 2)] + m[(2, 3)] * c[(0, 1)])


sec("the cell and its minimal pieces")
CORN = [(x, y, z, t) for x in (0, 1) for y in (0, 1) for z in (0, 1) for t in (0, 1)]
V = np.array(CORN, dtype=np.int64)
POS = dict((c, i) for i, c in enumerate(CORN))
SUB = np.array(list(itertools.combinations(range(16), 5)), dtype=np.int64)
VOL = np.abs(det4(V[SUB[:, 1:]] - V[SUB[:, 0]][:, None, :]))
UNI = SUB[VOL == 1]
NPIECE = len(UNI)
gate(len(SUB) == 4368 and NPIECE == 2672, "the minimal pieces are counted",
     "{0} five-subsets of the 16 corners, {1} of volume 1/24".format(len(SUB), NPIECE))
NZV = sorted(set(int(t) for t in VOL if t > 0))
gate(NZV[0] == 1, "no five-subset beats the minimal volume",
     "nonzero scaled volumes take the values {0}, so volume 1/24 is the floor".format(NZV))


def charge(P, cols):
    tot = np.zeros(len(P), dtype=np.int64)
    for a, b in PAIRS:
        d = np.abs(V[P[:, a]][:, cols] - V[P[:, b]][:, cols]).sum(axis=1)
        tot = tot + (d > 1).astype(np.int64)
    return tot


CX = charge(UNI, [0, 1, 2])
SPEC = sorted((int(a), int(b)) for a, b in zip(*np.unique(CX, return_counts=True)))
gate(SPEC == [(3, 64), (4, 384), (5, 1152), (6, 768), (7, 304)],
     "the adjacency spectrum of the minimal pieces", "charge to count {0}".format(SPEC))
gate(sum(b for _, b in SPEC) == NPIECE and 24 * int(CX.min()) == 72
     and 24 * int(CX.max()) == 168, "charging every piece its cheapest or dearest is weak",
     "counting alone gives only the interval 72 to 168 against the measured 108 to 128")

MM = np.stack([(V[p[1:]] - V[p[0]]).T for p in UNI])
IV = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)
gate(bool((np.einsum("nij,njk->nik", IV, MM) == np.eye(4, dtype=np.int64)).all()),
     "each piece carries an exact integer inverse",
     "all {0} rounded inverses multiply back to the identity".format(NPIECE))

sec("")
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
gate(len(ROT) == 24 and len(KEEP) == 24 and len(G) == 48,
     "the cell keeps every proper rotation",
     "{0} rotations kept, {1} group elements with the tick flip".format(len(KEEP), len(G)))

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
     "the pieces fall into orbits", "{0} orbits of sizes {1} summing to {2}".format(
         NORB, sorted(set(int(t) for t in SZ)), int(SZ.sum())))
gate(all(int(CX[LAB == o].max()) == int(CX[LAB == o].min()) for o in range(NORB)),
     "adjacency charge is constant on orbits",
     "every orbit has a single charge, so the program may be written per orbit")

sec("")
sec("generic sample points, none on a piece boundary")
L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
gate(CB == 3 and SB == 12810, "the weights are chosen past the barycentric bound",
     "corner coordinates bounded by {0}, weight total {1}".format(CB, SB))

SC = np.array([SB // 2, SB // 2, SB // 2], dtype=np.int64)
lab = {}
COLL = 0
for o, i in enumerate(REPS):
    q = (WT[:, None] * V[UNI[i]]).sum(axis=0)
    for (R, tf, _) in G:
        u = R @ (q[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]), (SB - int(q[3])) if tf else int(q[3]))
        if lab.setdefault(key, o) != o:
            COLL += 1
keys = sorted(lab)
Q = np.array(keys, dtype=np.int64)
PORB = np.array([lab[k] for k in keys], dtype=np.int64)
NQ = len(Q)

M = np.zeros((NPIECE, NORB), dtype=np.int16)
QT = Q.T
face = 0
MASK = []
INC = np.zeros((NPIECE, NQ), dtype=bool)
for i in range(NPIECE):
    lam = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lam.sum(axis=0)
    face += int(((lam == 0).any(axis=0) | (tot == SB)).sum())
    ins = (lam > 0).all(axis=0) & (tot < SB)
    INC[i] = ins
    M[i] = np.bincount(PORB[ins], minlength=NORB)
    b = 0
    for j in np.flatnonzero(ins):
        b |= 1 << int(j)
    MASK.append(b)
MO = np.bincount(PORB, minlength=NORB).astype(np.int64)
gate(NQ == 2736 and COLL == 0 and face == 0, "the sample is group-closed and interior",
     "{0} points, no orbit collision, {1} on a piece boundary".format(NQ, face))
gate(not bool((MO == SZ).all()) and int(MO.sum()) == NQ,
     "point counts are the program coefficients, not orbit sizes",
     "point stabilizers can be smaller than piece stabilizers, so the two vectors differ")


def build(dat):
    u = np.zeros(NORB, dtype=np.int64)
    for j, w in dat:
        u[j] = w
    return u


def slacks(u, Z, D, upper):
    s = (M.astype(np.int64) @ u + Z) - D * CX
    return s if upper else -s


sec("")
sec("two zero-gap certificates, verified over every piece in integers")
UFL, UCL = build(FLOOR_U), build(CEIL_U)
FS = slacks(UFL, FLOOR_Z, FLOOR_D, False)
CS = slacks(UCL, CEIL_Z, CEIL_D, True)
VFL = int((MO * UFL).sum()) + 24 * FLOOR_Z
VCL = int((MO * UCL).sum()) + 24 * CEIL_Z
gate(bool((FS >= 0).all()) and VFL == 108 * FLOOR_D,
     "the floor certificate holds and has zero gap",
     "denominator {0}, value {1} = 108 * {0}, so cost is at least 108".format(FLOOR_D, VFL))
gate(bool((CS >= 0).all()) and VCL == 128 * CEIL_D,
     "the ceiling certificate holds and has zero gap",
     "denominator {0}, value {1} = 128 * {0}, so cost is at most 128".format(CEIL_D, VCL))
gate(int((FS == 0).sum()) == 2416 and int((CS == 0).sum()) == 1040,
     "the tight rows are the local rule",
     "{0} pieces sit on a tight floor row, {1} on a tight ceiling row".format(
         int((FS == 0).sum()), int((CS == 0).sum())))
gate(-((-VFL) // FLOOR_D) == 108 and VCL // CEIL_D == 128,
     "the two certificates round to the measured interval",
     "the value divided by its denominator gives 108 below and 128 above")
for k in (2, 3, 5):
    sk = slacks(k * UFL, k * FLOOR_Z, k * FLOOR_D, False)
    vk = int((MO * (k * UFL)).sum()) + 24 * k * FLOOR_Z
    gate(bool((sk >= 0).all()) and vk == 108 * k * FLOOR_D,
         "the floor certificate scales by " + str(k),
         "denominator {0} gives the same bound".format(k * FLOOR_D))
RW = int(np.argmin(FS))
EXACT = FLOOR_D * int(CX[RW]) - (sum(int(M[RW, o]) * int(UFL[o]) for o in range(NORB))
                                 + FLOOR_Z)
gate(EXACT == int(FS[RW]), "the arithmetic does not overflow",
     "recomputing the tightest row in unbounded integers gives {0}".format(EXACT))
TR = int(np.flatnonzero(FS == 0)[0])
CO = int(np.argmax(M[TR]))
UB = UFL.copy()
UB[CO] += 1
gate(not bool((slacks(UB, FLOOR_Z, FLOOR_D, False) >= 0).all()),
     "a single bumped weight breaks the floor certificate",
     "raising one live weight on a tight row makes the inequality fail somewhere")
MB = M.copy()
MB[TR, CO] += 1
SB2 = (MB.astype(np.int64) @ UFL + FLOOR_Z) - FLOOR_D * CX
gate(not bool(((-SB2) >= 0).all()),
     "a single corrupted membership count breaks the floor certificate",
     "adding one point to a live column of a tight row makes that row violate the bound")

sec("")
sec("the local rule and what it excludes")
fr, cr = FS == 0, CS == 0
FORB = sorted(set(int(t) for t in LAB[fr]))
CORB = sorted(set(int(t) for t in LAB[cr]))
gate(len(FORB) == 51 and len(CORB) == 23 and int((fr & cr).sum()) == 784
     and int((~fr & ~cr).sum()) == 0, "the two rules cover every piece",
     "floor rule {0} in {1} orbits, ceiling rule {2} in {3} orbits, {4} in both, none in "
     "neither".format(int(fr.sum()), len(FORB), int(cr.sum()), len(CORB),
                      int((fr & cr).sum())))
gate(all(len(set(int(t) for t in fr[LAB == o])) == 1 for o in range(NORB)),
     "rule membership is constant on orbits",
     "the local test never splits an orbit, as the certificate is orbit-indexed")
exc = sorted(set(int(t) for t in LAB[~fr]))
zg, bd = 0, 0
for o in exc:
    P5 = V[UNI[REPS[o]]]
    sp = sorted(int(np.abs(P5[a][:3] - P5[b][:3]).sum()) for a, b in PAIRS)
    zg += 1 if sp[0] == 0 else 0
    bd += 1 if sp[-1] == 3 else 0
gate(len(exc) == 6 and int((~fr).sum()) == 256 and zg == 4 and bd == 2,
     "the floor rule excludes two recognisable shapes",
     "{0} orbits, {1} pieces: {2} carry a pure-tick edge, {3} carry a body diagonal".format(
         len(exc), int((~fr).sum()), zg, bd))

sec("")
sec("dissections found without any cost objective")
ALLQ = (1 << NQ) - 1
NEG = [np.array(t, dtype=np.int64)
       for t in itertools.product((-1, 0, 1), repeat=4) if any(t)]


def separated(P):
    pts = [V[p] for p in P]
    fac = []
    for p in P:
        A = (V[p[1:]] - V[p[0]]).T
        Iv = np.rint(np.linalg.inv(A.astype(float))).astype(np.int64)
        fac.append([Iv[k] for k in range(4)] + [-Iv.sum(axis=0)])
    good, total = 0, 0
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            total += 1
            for nv in NEG + fac[i] + fac[j]:
                a, b = pts[i] @ nv, pts[j] @ nv
                if int(a.max()) <= int(b.min()) or int(b.max()) <= int(a.min()):
                    good += 1
                    break
    return good, total


def is_dissection(idx):
    P = [UNI[i] for i in idx]
    g, t = separated(P)
    covered = 0
    for i in idx:
        covered |= MASK[i]
    return len(idx) == 24 and g == t and covered == ALLQ


def by_point(pool):
    out = [[] for _ in range(NQ)]
    for i in pool:
        out[(MASK[i] & -MASK[i]).bit_length() - 1].append(int(i))
    return out


def first_cover(pool):
    bp = by_point(pool)
    res = []

    def rec(cov, cur):
        if cov == ALLQ:
            res.append(list(cur))
            return True
        j = ~cov & ALLQ
        j = (j & -j).bit_length() - 1
        for i in bp[j]:
            if MASK[i] & cov:
                continue
            cur.append(i)
            if rec(cov | MASK[i], cur):
                return True
            cur.pop()
        return False

    rec(0, [])
    return np.array(sorted(res[0]), dtype=np.int64) if res else None


COVER = {}
for nm, pool, want in (("floor rule", np.flatnonzero(fr), 108),
                       ("ceiling rule", np.flatnonzero(cr), 128),
                       ("any piece", np.arange(NPIECE), 114)):
    d = COVER[nm] = first_cover(list(pool))
    cost = int(CX[d].sum())
    gate(cost == want and is_dissection(d),
         "cover search over the " + nm + " pool",
         "the first dissection it returns has {0} pieces and cost {1}".format(
             len(d), cost))
    gate(int(FS[d].sum()) == FLOOR_D * (cost - 108)
         and int(CS[d].sum()) == CEIL_D * (128 - cost),
         "the slack identity holds on that dissection",
         "floor slack {0} = {1} * (cost - 108), ceiling slack {2} = {3} * (128 - cost)"
         .format(int(FS[d].sum()), FLOOR_D, int(CS[d].sum()), CEIL_D))
    if want == 108:
        gate(int((FS[d] > 0).sum()) == 0, "the cheapest dissection is entirely on the rule",
             "no cost objective was used anywhere in the search")

STEN = []
for perm in itertools.permutations(range(4)):
    v = [0, 0, 0, 0]
    path = [tuple(v)]
    for c in perm:
        v[c] += 1
        path.append(tuple(v))
    STEN.append(tuple(sorted(POS[p] for p in path)))
sidx = np.array(sorted(posp[t] for t in sorted(STEN)), dtype=np.int64)
gate(len(sidx) == 24 and is_dissection(sidx) and int(CX[sidx].sum()) == 108
     and int((FS[sidx] > 0).sum()) == 0,
     "the monotone stencil attains the floor",
     "the 24 monotone corner paths dissect the cell at cost 108, all on the rule")

nidx = np.array(sorted(posp[tuple(sorted(r))] for r in NEAR), dtype=np.int64)
ncost = int(CX[nidx].sum())
noff = np.flatnonzero(FS[nidx] > 0)
gate(is_dissection(nidx) and ncost == 110 and len(noff) == 1
     and int(FS[nidx][noff[0]]) == 48 and int(FS[nidx].sum()) == 48,
     "one off-rule piece costs exactly its own excess",
     "cost {0}, a single off-rule piece, its slack {1} = {2} * (110 - 108)".format(
         ncost, int(FS[nidx].sum()), FLOOR_D))

sec("")
sec("the rule is necessary and not sufficient")


def enumerate_support(pool, cap):
    bp = by_point(pool)
    sup, witnesses, n, valid = set(), {}, [0], [0]

    def rec(cov, cur):
        if cov == ALLQ:
            n[0] += 1
            present = set(int(t) for t in LAB[np.array(cur)])
            if present - sup and is_dissection(np.array(cur, dtype=np.int64)):
                valid[0] += 1
                witness = tuple(sorted(int(t) for t in cur))
                for orbit in present:
                    witnesses.setdefault(orbit, witness)
                sup.update(present)
            return n[0] >= cap
        j = ~cov & ALLQ
        j = (j & -j).bit_length() - 1
        for i in bp[j]:
            if MASK[i] & cov:
                continue
            cur.append(i)
            if rec(cov | MASK[i], cur):
                return True
            cur.pop()
        return False

    rec(0, [])
    return n[0], valid[0], sup, witnesses


def occurs(pool, forced, cap):
    """complete backtrack over the pool with one piece forced in"""
    bp = by_point(pool)
    st, res = [0], []

    def rec(cov, cur):
        st[0] += 1
        if st[0] > cap:
            return True
        if cov == ALLQ:
            res.append(list(cur))
            return True
        j = ~cov & ALLQ
        j = (j & -j).bit_length() - 1
        for i in bp[j]:
            if MASK[i] & cov:
                continue
            cur.append(i)
            if rec(cov | MASK[i], cur):
                return True
            cur.pop()
        return False

    rec(MASK[forced], [forced])
    if res:
        return "occurs", np.array(sorted(res[0]), dtype=np.int64), st[0]
    return ("unsettled" if st[0] > cap else "absent"), None, st[0]


def propagate(pool, forced):
    """force one piece in, then deduce; no branching and no point order"""
    live = np.zeros(NPIECE, dtype=bool)
    live[pool] = True
    cov = INC[forced].copy()
    live &= ~(INC & cov).any(axis=1)
    live[forced] = False
    rounds = 0
    while True:
        rounds += 1
        cnt = INC[live].sum(axis=0)
        op = ~cov
        orph = np.flatnonzero(op & (cnt == 0))
        if len(orph):
            return "absent", rounds, int(orph[0])
        unit = np.flatnonzero(op & (cnt == 1))
        if len(unit) == 0:
            return "open", rounds, -1
        idx = np.flatnonzero(live)
        add = sorted(set(int(idx[INC[idx, j]][0]) for j in unit))
        for a in add:
            if (INC[a] & cov).any():
                return "absent", rounds, -1
            cov |= INC[a]
        live &= ~(INC & cov).any(axis=1)


CAP = 20000000
CTRL_CAP = 200000
POOLS, SUP, REALIZATION_WITNESSES, SEARCH_CERTIFICATES = {}, {}, {}, {}
for nm, sl, orbs, ab, want, tgt, ctrl, nc in (
        ("floor", FS, FORB, FLOOR_SEARCHED, 38, 108, sidx, 22),
        ("ceiling", CS, CORB, CEIL_ABSENT, 21, 128, COVER["ceiling rule"], 24)):
    pool = list(np.flatnonzero(sl == 0))
    POOLS[nm] = pool
    n, nvalid, sup, witnesses = enumerate_support(pool, 200000)
    SUP[nm] = sup
    REALIZATION_WITNESSES[nm] = witnesses
    gate(len(sup) == want and sup.issubset(set(orbs)),
         "the " + nm + " support is exhibited by enumeration",
         "{0} sample exact covers inspected; {1} geometrically validated witness covers use "
         "{2} of its {3} orbits".format(n, nvalid, len(sup), len(orbs)))
    bad, search_certificates = [], {}
    for o in ab:
        rep = int(np.flatnonzero((LAB == o) & (sl == 0))[0])
        st, _, nodes = occurs(pool, rep, CAP)
        search_certificates[o] = {"forced_piece": rep, "nodes": nodes, "status": st}
        if st != "absent":
            bad.append(o)
    SEARCH_CERTIFICATES[nm] = search_certificates
    gate(not bad, "the whole search comes back empty on those " + nm + " pieces",
         "{0} orbits, {1} pieces: forcing one representative per orbit leaves the search "
         "empty after at most {2} nodes".format(
             len(ab), sum(int((LAB == o).sum()) for o in ab),
             max(t["nodes"] for t in search_certificates.values())))
    nab, nocc, wrong = 0, 0, 0
    for p in ctrl:
        st, d, _ = occurs(pool, int(p), CTRL_CAP)
        if st == "absent":
            nab += 1
        elif st == "occurs":
            nocc += 1
            if len(d) != 24 or int(CX[d].sum()) != tgt or not is_dissection(d):
                wrong += 1
    gate(nab == 0 and wrong == 0 and nocc == nc,
         "the same search never empties on a piece of an exhibited " + nm + " dissection",
         "each of its 24 pieces forced in turn: {0} return a dissection at cost {1}, "
         "{2} return the empty answer".format(nocc, tgt, nab))

sec("")
sec("one deduction step, and the point that can then no longer be covered")
PROP, WIT, ONE, PRUNING_CERTIFICATES = {}, {}, {}, {}
for nm in ("floor", "ceiling"):
    pool = POOLS[nm]
    orbs, npc, one, pruning_certificates = set(), 0, 0, {}
    for p in pool:
        st, r, o = propagate(pool, int(p))
        if st != "absent":
            continue
        orbs.add(int(LAB[p]))
        npc += 1
        if r == 1:
            one += 1
            if nm not in WIT and o >= 0:
                WIT[nm] = (int(p), o)
            if o >= 0:
                pruning_certificates.setdefault(
                    int(LAB[p]), {"forced_piece": int(p), "orphan_point": int(o)}
                )
    PROP[nm] = orbs
    ONE[nm] = (npc, one)
    PRUNING_CERTIFICATES[nm] = pruning_certificates

gate(ONE["floor"][0] == ONE["floor"][1] == 624
     and ONE["ceiling"][0] == ONE["ceiling"][1],
     "every floor piece the step rules out goes at the first round",
     "{0} of its {1} pieces go, in {2} orbits, with no branching anywhere".format(
         ONE["floor"][0], len(POOLS["floor"]), len(PROP["floor"])))

left = set(FORB) - PROP["floor"] - SUP["floor"]
gate(PROP["floor"] == set(FLOOR_ABSENT) and not (PROP["floor"] & SUP["floor"])
     and not left,
     "the two routes cut the floor rule in the same place",
     "the step rules out {0} orbits, enumeration exhibits {1}, and {2} is the whole "
     "rule".format(len(PROP["floor"]), len(SUP["floor"]), len(FORB)))
gate(not PROP["ceiling"],
     "at the ceiling the same step returns no verdict",
     "{0} of its {1} pieces go, so that end rests on the whole search instead".format(
         len(PROP["ceiling"]), len(POOLS["ceiling"])))

wp, wq = WIT["floor"]
hold = [i for i in POOLS["floor"] if INC[i][wq]]
meet = [i for i in hold if bool((INC[i] & INC[wp]).any())]
gate(len(hold) == len(meet) and len(hold) > 0 and not INC[wp][wq]
     and int(INC[sidx, wq].sum()) == 1,
     "the stranded point is nameable and is covered in a dissection already exhibited",
     "{0} rule pieces hold it and all {0} overlap the forced piece, which does not hold "
     "it; exactly one piece of the exhibited dissection does".format(len(hold)))

gate(len(FLOOR_ABSENT) + len(SUP["floor"]) == len(FORB),
     "the floor support is settled completely",
     "{0} of the {1} floor-rule orbits occur and the other {2} cannot".format(
         len(SUP["floor"]), len(FORB), len(FLOOR_ABSENT)))
gate(len(CEIL_ABSENT) + len(SUP["ceiling"]) == len(CORB),
     "the ceiling support is settled completely",
     "{0} of the {1} ceiling-rule orbits occur and the other {2} cannot".format(
         len(SUP["ceiling"]), len(CORB), len(CEIL_ABSENT)))

gate(
    set(REALIZATION_WITNESSES["floor"]) == SUP["floor"]
    and set(REALIZATION_WITNESSES["ceiling"]) == SUP["ceiling"]
    and set(PRUNING_CERTIFICATES["floor"]) == set(FLOOR_ABSENT)
    and set(SEARCH_CERTIFICATES["ceiling"]) == set(CEIL_ABSENT),
    "every support classification has a landed certificate",
    "realized orbits carry geometric witnesses; floor exclusions carry orphan points; "
    "ceiling exclusions carry exhaustive search counts",
)

print("")
print("per_element: checked all 2672 minimal pieces for exact certificate slack and every "
      "classified orbit representative for a positive or negative support certificate")
print("per_site: checked and not executed — the supplied theorem has no site field; its "
      "smallest resolved objects are corner-simplex pieces and interior sample points")
print("per_mode: checked and not executed — no spectral or mode decomposition occurs in "
      "this finite exact-cover and convex-dissection theorem")
print("per_block: checked the complete supplied one-cell by one-tick four-box, including all "
      "2672 minimal pieces and both endpoint support partitions")
print("lattice_wide: checked and not executed — no multi-cell, arbitrary-tick, boundary, or "
      "continuum extension is asserted by this bounded supplied-model result")
print("")
print("TOTAL: PASS={0} FAIL={1}".format(NP[0], NP[1]))

receipt = {
    "claim_type": "bounded_theorem",
    "supplied_model": C725_RECEIPT.get("supplied_model"),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "piece_census": {
        "five_subsets": len(SUB),
        "minimal_pieces": NPIECE,
        "piece_orbits": NORB,
        "sample_points": NQ,
        "pieces_per_dissection": 24,
    },
    "certificates": {
        "floor": {"denominator": FLOOR_D, "bound": 108, "tight_pieces": int(fr.sum())},
        "ceiling": {"denominator": CEIL_D, "bound": 128, "tight_pieces": int(cr.sum())},
    },
    "support": {
        "floor": {
            "realized_orbits": sorted(SUP["floor"]),
            "excluded_orbits": sorted(set(FLOOR_ABSENT)),
            "realization_witnesses": {
                str(o): list(REALIZATION_WITNESSES["floor"][o]) for o in sorted(SUP["floor"])
            },
            "pruning_certificates": {
                str(o): PRUNING_CERTIFICATES["floor"][o] for o in sorted(FLOOR_ABSENT)
            },
        },
        "ceiling": {
            "realized_orbits": sorted(SUP["ceiling"]),
            "excluded_orbits": sorted(set(CEIL_ABSENT)),
            "realization_witnesses": {
                str(o): list(REALIZATION_WITNESSES["ceiling"][o]) for o in sorted(SUP["ceiling"])
            },
            "search_certificates": {
                str(o): SEARCH_CERTIFICATES["ceiling"][o] for o in sorted(CEIL_ABSENT)
            },
        },
    },
    "no_go_discipline": {
        "status": "PASS",
        "negative_assertion_class": "derived_no_go_boundary",
        "checklist": "No-Go Discipline Gate section in the Cycle 730 note",
        "n5_certificate": "five resolution lines in primary stdout and canonical cache",
    },
    "totals": {"pass": NP[0], "fail": NP[1]},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + json.dumps(receipt, sort_keys=True, separators=(",", ":")))
sys.exit(1 if NP[1] else 0)
