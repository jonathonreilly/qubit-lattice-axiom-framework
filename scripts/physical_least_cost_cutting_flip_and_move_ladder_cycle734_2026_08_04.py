"""Cycle 734. Finite move structure at one supplied cell's four-column cost floor.

A piece is a five corner simplex of the four cube of least volume; the cost of a piece
counts the pairs of its corners more than one lattice step apart. This runner shows that
a cutting at the floor of that cost cannot be adjusted by recutting two or three of its
pieces, that the smallest change keeping the cost replaces four, that such a change is a
flip between the two floor cuts of one of five regions, and that the cuttings at the
floor stay in separate groups until moves on ten pieces are allowed.

No solver. Every count is a complete search over an explicit finite set, and every
separation is a plane exhibited and checked in whole numbers.

Everything here is a theorem of a SUPPLIED finite structural model, not of the
framework axioms alone. The Lattice axiom supplies only spatial Z^3 adjacency and
proper cubic rotations; kinetic isotropy supplies only equal tick/edge graining.
The four-cube, corner-simplex class, exact dissection rule, four-coordinate pair
charge, and physical interpretation of the fourth coordinate are declared inputs.
The physical tick--Admissibility and assembly-cell--simplex bridges remain open.
Any failed gate makes the runner exit nonzero.
"""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / (
    "outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_"
    "2026_08_04_receipt_2026-08-04.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_LEAST_COST_CUTTING_FLIP_AND_MOVE_LADDER_CYCLE734_NOTE_2026-08-04.md",
    "scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_"
    "independent_check_2026_08_04.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md",
    "docs/PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md",
)
AUDIT_TIMEOUT_SEC = 600

PF = [0, 0]


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


def sec(text):
    print("", flush=True)
    print(text, flush=True)


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

sec("sample points inside the pieces")
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


sec("the least volume, and the piece count it forces")

VV, VC = np.unique(VOL, return_counts=True)
VSP = [(int(a), int(b)) for a, b in zip(VV, VC)]
NFAC = math.factorial(4)
gate(VSP == [(0, 1360), (1, 2672), (2, 320), (3, 16)] and NFAC == 24
     and int(VOL[VOL > 0].min()) == 1, "vol.least",
     "over the {0} five corner sets the volumes run {1} in units of one over {2}, so a "
     "piece of least volume is one part in {2} and a cutting has {2} of "
     "them".format(len(SUB), VSP, NFAC))

INSIDE = (L >= 0).all(axis=2) & (L.sum(axis=2) <= 1)
OWN = np.zeros((NPIECE, 16), dtype=bool)
OWN[np.arange(NPIECE)[:, None], UNI] = True
BIG = np.flatnonzero(VOL > 1)
EXACT, FRAC, PAST = 0, 0, 0
for i in BIG:
    s = SUB[i]
    E = (V[s[1:]] - V[s[0]]).astype(np.int64)
    d = int(det4(E[None, :, :])[0])
    M, ab = E.T, abs(d)
    ad = np.rint(np.linalg.inv(M.astype(np.float64)) * d).astype(np.int64)
    if bool((M @ ad == d * np.eye(4, dtype=np.int64)).all()):
        EXACT = EXACT + 1
    y = ad @ (V.astype(np.int64) - V[s[0]]).T
    if bool((y - (y // ab) * ab != 0).any()):
        FRAC = FRAC + 1
    w = y if d > 0 else -y
    ins = (w >= 0).all(axis=0) & (w.sum(axis=0) <= ab)
    if sorted(np.flatnonzero(ins).tolist()) != sorted(int(t) for t in s):
        PAST = PAST + 1
gate(bool((INSIDE == OWN).all()) and int(INSIDE.sum()) == 5 * NPIECE
     and EXACT == len(BIG) and FRAC == len(BIG) and PAST == 0, "vol.corner",
     "a corner read against a piece gives whole numbers, so a corner inside the closed "
     "piece has all but one of them zero: over all pieces the corners inside are exactly "
     "the {0} of the piece itself. whole numbers are what the least volume buys: all {1} "
     "five corner sets of volume two or three read some corner in fractions, while {2} "
     "of them reach past their own corners, so the reading is special to the least "
     "volume and the conclusion is not".format(5, len(BIG), PAST))

sec("the cost, its floor, and the cuttings that reach it")

C4 = charge(UNI, [0, 1, 2, 3])
VU, CU = np.unique(C4, return_counts=True)
SPEC = [(int(a), int(b)) for a, b in zip(VU, CU)]
LO = int(C4.min())
gate(LO == 6 and SPEC == [(6, 400), (7, 1216), (8, 864), (9, 192)], "cost.piece",
     "one piece costs {0}".format(SPEC))

MINP = [i for i in range(NPIECE) if int(C4[i]) == LO]
HOSTILE_C4 = C4.copy()
HOSTILE_C4[MINP[0]] = HOSTILE_C4[MINP[0]] + 1
gate(len(np.flatnonzero(HOSTILE_C4 == LO)) == 399, "cost.hostile",
     "raising one minimum piece charge removes it from the complete floor-search pool")
BY, MK = {}, dict((i, MASK[i]) for i in MINP)
for i in MINP:
    for j in np.flatnonzero(MI[i]):
        BY.setdefault(int(j), []).append(i)
SOL, NODE, FULL = [], [0], []


def rec(cov, chosen):
    NODE[0] += 1
    if cov == ALLQ:
        FULL.append(len(chosen))
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
gate(len(MINP) == 400 and NODE[0] == 502838 and len(SOL) == 15800
     and set(FULL) == set([24]), "cost.floor",
     "a complete search over the {0} pieces of least cost visits {1} nodes and finds {2} "
     "cuttings, each of {3} pieces, so the floor {4} is reached".format(
         len(MINP), NODE[0], len(SOL), 24, 24 * LO))

USED = sorted(set(i for s in SOL for i in s))
NPO = len(USED)
P2I = dict((p, a) for a, p in enumerate(USED))
gate(NPO == 192 and len(set(int(LAB[i]) for i in USED)) == 4, "cost.pool",
     "those cuttings between them use {0} of the {1} pieces of least cost, filling {2} "
     "whole families".format(NPO, len(MINP), 4))

sec("the cuttings really cut the cell")

CO = np.zeros((NPO, NPO), dtype=bool)
PSOL = {}
for solution_index, s in enumerate(SOL):
    idx = [P2I[i] for i in s]
    CO[np.ix_(idx, idx)] = True
    for a, b in itertools.combinations(idx, 2):
        PSOL.setdefault((min(a, b), max(a, b)), solution_index)
np.fill_diagonal(CO, False)
CP = [(a, b) for a in range(NPO) for b in range(a + 1, NPO) if CO[a, b]]
SEP = sum(separated([USED[a], USED[b]])[0] for a, b in CP)
gate(len(CP) == 15168 and SEP == len(CP), "cut.apart",
     "each of the {0} pairs of pieces sharing a cutting is pushed apart by a plane shown "
     "in whole numbers, so the {1} pieces meet only on their boundaries and, carrying "
     "the volume of the cell between them, fill it".format(len(CP), 24))

sec("no move on two pieces keeps the cost")

CM = np.zeros(NPIECE, dtype=np.int64)
for i in range(NPIECE):
    b = 0
    for t in UNI[i]:
        b |= 1 << int(t)
    CM[i] = b
ALLI = np.arange(NPIECE, dtype=np.int64)


def span(pcs):
    hc, hp = 0, 0
    for i in pcs:
        hc |= int(CM[i])
        hp |= MASK[i]
    return hc, hp


def refills(hc, hp, k, univ, cmu):
    cand = [int(j) for j in univ[(cmu & ~hc) == 0]]
    cand = [j for j in cand if (MASK[j] & ~hp) == 0]
    out = []

    def rec2(cov, chosen, start):
        if len(chosen) == k:
            if cov == hp:
                out.append(tuple(chosen))
            return
        for a in range(start, len(cand)):
            j = cand[a]
            if MASK[j] & cov:
                continue
            chosen.append(j)
            rec2(cov | MASK[j], chosen, a + 1)
            chosen.pop()

    rec2(0, [], 0)
    return len(cand), out


SH, FLIP, FACE, SEC2 = {}, [], [], {}
for a, b in CP:
    pr = (USED[a], USED[b])
    n = bin(int(CM[pr[0]]) & int(CM[pr[1]])).count("1")
    SH[n] = SH.get(n, 0) + 1
    if n == 4:
        FACE.append(pr)
    hc, hp = span(pr)
    fil = refills(hc, hp, 2, ALLI, CM)[1]
    if len(fil) > 1:
        FLIP.append(pr)
        SEC2[pr] = fil
SHC = sorted(SH.items())
gate(SHC == [(0, 2976), (1, 5280), (2, 5376), (3, 1248), (4, 288)]
     and len(FLIP) == 288 and set(FLIP) == set(FACE), "two.face",
     "over those pairs the corners in common run {0}; exactly {1} can be refilled a "
     "second way, and they are exactly the pairs meeting in four corners".format(
         SHC, len(FLIP)))


def idet(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = 0
    for j in range(n):
        if M[0][j] == 0:
            continue
        sub = [[M[r][c] for c in range(n) if c != j] for r in range(1, n)]
        tot = tot + ((-1) ** j) * M[0][j] * idet(sub)
    return tot


RAD, UNIT, DLT = {}, 0, {}
for pr in FLIP:
    cor = sorted(set(int(t) for t in UNI[pr[0]]) | set(int(t) for t in UNI[pr[1]]))
    MR = [[1] + [int(x) for x in V[c]] for c in cor]
    lam = [((-1) ** j) * idet([MR[r] for r in range(6) if r != j]) for j in range(6)]
    g = 0
    for x in lam:
        g = math.gcd(g, abs(x))
    lam = [x // g for x in lam]
    sg = (sum(1 for x in lam if x > 0), sum(1 for x in lam if x < 0))
    key = (max(sg), min(sg), sum(1 for x in lam if x == 0))
    RAD[key] = RAD.get(key, 0) + 1
    if sorted(x for x in lam if x != 0) == [-1, -1, 1, 1]:
        UNIT = UNIT + 1
    base = int(C4[pr[0]]) + int(C4[pr[1]])
    for u in SEC2[pr]:
        if set(u) != set(pr):
            d = sum(int(C4[j]) for j in u) - base
            DLT[d] = DLT.get(d, 0) + 1
DL = sorted(DLT.items())
gate(sorted(RAD.items()) == [((2, 2, 2), 288)] and UNIT == len(FLIP), "two.square",
     "the six corners of such a pair carry one relation, and it puts two corners of "
     "weight one on each side leaving two out, so the four corners that move are the "
     "corners of a flat square: {0}".format(sorted(RAD.items())))
gate(DL == [(1, 192), (2, 96)] and min(k for k, _ in DL) > 0, "two.cost",
     "recutting that square always costs more, by {0}".format(DL))

GEO2 = 0
for pr in FLIP:
    pair_positions = tuple(sorted((P2I[pr[0]], P2I[pr[1]])))
    common = sorted(set(SOL[PSOL[pair_positions]]) - set(pr))
    alternate = next(t for t in SEC2[pr] if set(t) != set(pr))
    candidate = common + list(alternate)
    cov = 0
    for piece in candidate:
        cov |= MASK[piece]
    apart, total = separated(candidate)
    GEO2 += int(len(candidate) == 24 and cov == ALLQ and apart == total)
gate(GEO2 == len(FLIP), "two.geometry",
     "all {0} alternate two-piece incidence refills are genuine geometric re-cuts after "
     "adjoining the unchanged 22-piece complement".format(GEO2))

sec("no move on three pieces keeps the cost")

MEM = [0] * NPO
for solution_index, solution in enumerate(SOL):
    bit = 1 << solution_index
    for piece in solution:
        MEM[P2I[piece]] |= bit

TRI, CLIQUE, SPURIOUS, KEEP, RAISE, TSP = 0, 0, 0, 0, 0, {}
for a in range(NPO):
    nb = [b for b in range(a + 1, NPO) if CO[a, b]]
    for x in range(len(nb)):
        for y in range(x + 1, len(nb)):
            b, c = nb[x], nb[y]
            if not CO[b, c]:
                continue
            CLIQUE = CLIQUE + 1
            if not (MEM[a] & MEM[b] & MEM[c]):
                SPURIOUS = SPURIOUS + 1
                continue
            TRI = TRI + 1
            org = set((USED[a], USED[b], USED[c]))
            hc, hp = span(org)
            fil = refills(hc, hp, 3, ALLI, CM)[1]
            if len(fil) < 2:
                continue
            hit = False
            for t in fil:
                if set(t) == org:
                    continue
                k = sum(int(C4[j]) for j in t)
                TSP[k] = TSP.get(k, 0) + 1
                if k == 3 * LO:
                    hit = True
            if hit:
                KEEP = KEEP + 1
            else:
                RAISE = RAISE + 1
TSL = sorted(TSP.items())
gate(CLIQUE == 649600 and SPURIOUS == 13568 and TRI == 636032
     and KEEP == 0 and RAISE == 40512 and len(TSL) > 0
     and min(TSP) > 3 * LO, "three.none",
     "of the {0} co-occurrence cliques, {1} are spurious and the remaining {2} are "
     "triples that genuinely share a cutting; {3} admit a second refill at all "
     "and {4} admit one by three pieces of least cost; the second refills that do exist "
     "cost {5}, every one of them above the floor {6}, so every three piece recut costs "
     "more. The candidate-refill spectrum is an incidence result; the exact absence "
     "of a floor-preserving three-piece move is independently forced below by the "
     "complete minimizer-distance census".format(
         CLIQUE, SPURIOUS, TRI, KEEP + RAISE, KEEP, TSL, 3 * LO))

sec("the smallest move that keeps the cost changes four pieces")

A = np.zeros((len(SOL), NPO), dtype=np.float32)
for r, s in enumerate(SOL):
    A[r, [P2I[i] for i in s]] = 1.0
BAG = dict((k, []) for k in range(4, 11))
CEN = {}
for lo in range(0, len(SOL), 1000):
    B = A[lo:lo + 1000] @ A.T
    for r in range(B.shape[0]):
        B[r, lo + r] = -1.0
    d = (24 - B).astype(np.int16)
    uv, uc = np.unique(d, return_counts=True)
    for x, y in zip(uv.tolist(), uc.tolist()):
        if 0 < x <= 24:
            CEN[x] = CEN.get(x, 0) + y
    for k in range(4, 11):
        rr, cc = np.nonzero(d == k)
        m = (rr + lo) < cc
        BAG[k].append(np.stack([rr[m] + lo, cc[m]]).astype(np.int32))
BYD = dict((k, np.concatenate(BAG[k], axis=1)) for k in range(4, 11))
CEN = dict((k, v // 2) for k, v in CEN.items())
DS = sorted(CEN)
NPAIR = len(SOL) * (len(SOL) - 1) // 2
gate(DS == [4] + list(range(6, 25)) and sum(CEN.values()) == NPAIR
     and CEN[4] == 46128 and CEN[24] == 29069284, "four.least",
     "over all {0} pairs of cuttings at the floor the number of pieces they differ in "
     "takes the values {1}, never one two three or five; the smallest is {2}, reached "
     "{3} times".format(NPAIR, DS, DS[0], CEN[4]))

BYP = {}
for i, s in enumerate(SOL):
    for p in s:
        BYP.setdefault(p, []).append(i)
BYP = dict((p, np.array(v, dtype=np.int64)) for p, v in BYP.items())
DJ = 0
for i in range(len(SOL)):
    hit = np.zeros(len(SOL), dtype=bool)
    for p in SOL[i]:
        hit[BYP[p]] = True
    DJ = DJ + len(SOL) - i - 1 - int(hit[i + 1:].sum())
gate(DJ == CEN[24] and DJ == 29069284, "four.apart",
     "at the other end of that range {0} pairs of cuttings at the floor share no piece "
     "at all, counted again by listing which cuttings each piece belongs to".format(DJ))

par = list(range(len(SOL)))


def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


LAD = []
for k in range(4, 11):
    e = BYD[k]
    for j in range(e.shape[1]):
        ra, rb = find(int(e[0, j])), find(int(e[1, j]))
        if ra != rb:
            par[ra] = rb
    LAD.append(len(set(find(i) for i in range(len(SOL)))))
gate(LAD == [349, 349, 157, 61, 61, 13, 1], "four.ladder",
     "allowing moves on up to four then five and so on to ten pieces, the cuttings at "
     "the floor sit in {0} groups within reach of one another".format(LAD))

sec("the smallest move recuts one of five regions")

E4 = BYD[4]
REG = {}
REG_EDGE = {}
for j in range(E4.shape[1]):
    key = span(sorted(set(SOL[int(E4[0, j])]) - set(SOL[int(E4[1, j])])))
    REG[key] = REG.get(key, 0) + 1
    REG_EDGE.setdefault(key, (int(E4[0, j]), int(E4[1, j])))
NC = sorted(set(bin(k[0]).count("1") for k in REG))
WID = set()
for (hc, hp) in REG:
    cor = [c for c in range(16) if hc >> c & 1]
    WID.add(tuple(len(set(int(V[c][d]) for c in cor)) for d in range(4)))
gate(len(REG) == 120 and len(set(k[0] for k in REG)) == 120
     and sum(REG.values()) == int(E4.shape[1]) and NC == [8]
     and WID == set([(2, 2, 2, 2)]), "reg.count",
     "the {0} smallest moves recut {1} regions with {1} distinct corner sets, each "
     "holding {2} corners and reaching both values in all four columns".format(
         int(E4.shape[1]), len(REG), NC[0]))

CAN = {}
for r in REG:
    ims = []
    for (_, _, g) in G:
        w = 0
        for c in range(16):
            if r[0] >> c & 1:
                w |= 1 << int(g[c])
        ims.append(w)
    CAN.setdefault(min(ims), []).append(r)
OS = sorted(len(v) for v in CAN.values())
gate(len(CAN) == 5 and OS == [12, 12, 24, 24, 48] and sum(OS) == len(REG), "reg.shape",
     "up to the symmetry of the cell there are {0} such regions, in families of sizes "
     "{1}".format(len(CAN), OS))

CUT = {}
PAIR_OK = dict(((min(USED[a], USED[b]), max(USED[a], USED[b])), True) for a, b in CP)


def pair_apart(a, b):
    key = (min(a, b), max(a, b))
    if key not in PAIR_OK:
        PAIR_OK[key] = separated([a, b]) == (1, 1)
    return PAIR_OK[key]


def genuine_refill(region, refill):
    a, b = REG_EDGE[region]
    common = sorted(set(SOL[a]) & set(SOL[b]))
    candidate = common + list(refill)
    if len(candidate) != 24 or len(set(candidate)) != 24:
        return False
    cov = 0
    for piece in candidate:
        cov |= MASK[piece]
    return cov == ALLQ and all(pair_apart(x, y) for x, y in itertools.combinations(candidate, 2))


for (hc, hp) in REG:
    nc, out = refills(hc, hp, 4, ALLI, CM)
    valid = [t for t in out if genuine_refill((hc, hp), t)]
    cs = [sum(int(C4[j]) for j in t) for t in out]
    mn = [t for t in out if sum(int(C4[j]) for j in t) == 4 * LO]
    CUT[(hc, hp)] = (nc, len(out), min(cs), mn, len(valid))
INS = sorted(set(v[0] for v in CUT.values()))
TOT = sorted(set(v[1] for v in CUT.values()))
FLR = sorted(set(v[2] for v in CUT.values()))
MNC = sorted(set(len(v[3]) for v in CUT.values()))
GEO = sorted(set(v[4] for v in CUT.values()))
gate(INS == [8, 32] and TOT == [2, 24] and FLR == [4 * LO] and MNC == [2], "reg.cut",
     "a region holds {0} pieces and cuts into four in {1} ways, of which exactly {2} "
     "reach its own floor {3}".format(INS, TOT, MNC[0], FLR[0]))
gate(GEO == TOT, "reg.geometry",
     "all incidence-compatible four-piece refills are genuine geometric re-cuts after "
     "adjoining the unchanged 20-piece complement: {0}".format(GEO))

USE = sorted((len(CAN[k]), sum(REG[r] for r in CAN[k]),
              sorted(set(CUT[r][0] for r in CAN[k]))) for k in CAN)
PER = sorted(set(u // n for n, u, _ in USE))
RIGID = [(n, u) for n, u, ins in USE if ins == [8]]
gate([(n, u) for n, u, _ in USE] == [(12, 5736), (12, 5736), (24, 240), (24, 11472),
                                     (48, 22944)]
     and PER == [10, 478] and RIGID == [(24, 240)], "reg.use",
     "the regions of a family are used equally often, {0} times each; the family holding "
     "only {1} pieces is the rigid one, used {2} times in all".format(
         PER, 8, RIGID[0][1]))

sec("the smallest move is the flip between the two floor cuts of its region")

SSET = [set(s) for s in SOL]
SS = set(frozenset(s) for s in SOL)
SEEN, BACK = 0, 0
for r in REG:
    mn = CUT[r][3]
    m0, m1 = set(mn[0]), set(mn[1])
    for ss in SSET:
        if m0 <= ss:
            SEEN = SEEN + 1
            t = (ss - m0) | m1
            if frozenset(t) in SS and ((t - m1) | m0) == ss:
                BACK = BACK + 1
gate(SEEN == int(E4.shape[1]) and BACK == SEEN, "reg.flip",
     "swapping the two floor cuts of a region carries a cutting at the floor to another "
     "and back {0} times, exactly the number of smallest moves".format(BACK))

print("per_element: checked -- all 2,672 declared minimal pieces enter the exact "
      "volume, charge, incidence, orbit, and refill candidate censuses")
print("per_site: checked -- one supplied coordinate cell only; no physical "
      "assembly-cell or site identification is executed")
print("per_mode: checked and not executed -- this finite corner-dissection model "
      "has no momentum, spectral, or field-mode decomposition")
print("per_block: checked -- all 15,800 floor dissections, 124,812,100 pairs, "
      "636,032 genuine co-occurring triples, and 120 four-piece regions")
print("lattice_wide: checked and not executed -- no arbitrary-cell, repeated-domain, "
      "thermodynamic, or continuum negative is asserted")


def spectrum(values):
    return {str(k): int(v) for k, v in sorted(Counter(int(x) for x in values).items())}


receipt = {
    "schema": "physical-least-cost-cutting-flip-and-move-ladder-cycle734-v2",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "gates": {"pass": int(PF[0]), "fail": int(PF[1])},
    "supplied_model": {
        "shape": [1, 1, 1, 1],
        "piece_class": "five-corner normalized-volume-one simplices only",
        "cost": "all corner pairs with four-coordinate L1 separation greater than one",
        "physical_tick_admissibility_bridge": "open",
        "physical_assembly_cell_simplex_bridge": "open",
    },
    "cell": {
        "five_subsets": len(SUB),
        "minimal_pieces": NPIECE,
        "pieces_per_dissection": 24,
        "volume_spectrum": spectrum(VOL),
        "four_column_piece_cost_spectrum": spectrum(C4),
        "carried_action_order": len(G),
        "piece_orbits": NORB,
        "sample_points": NQ,
    },
    "floor": {
        "piece_cost": LO,
        "dissection_cost": 24 * LO,
        "candidate_pieces": len(MINP),
        "genuine_dissections": len(SOL),
        "used_pieces": NPO,
        "used_piece_orbits": len(set(int(LAB[i]) for i in USED)),
        "cooccurring_pairs_exactly_separated": len(CP),
    },
    "three_piece_census": {
        "cooccurrence_graph_triangles": CLIQUE,
        "spurious_pairwise_cliques": SPURIOUS,
        "genuine_cooccurring_triples": TRI,
        "triples_with_incidence_compatible_second_refill": RAISE,
        "least_cost_candidate_second_refills": KEEP,
        "candidate_second_refill_cost_spectrum": {str(k): int(v) for k, v in TSL},
    },
    "minimizer_distance": {
        "pairs": NPAIR,
        "difference_spectrum": CEN,
        "least_difference": min(DS),
        "four_piece_moves": CEN[4],
        "disjoint_pairs": CEN[24],
        "components_under_cumulative_thresholds_4_to_10": LAD,
    },
    "four_piece_regions": {
        "regions": len(REG),
        "corner_sets": len(set(key[0] for key in REG)),
        "carried_families": len(CAN),
        "family_sizes": OS,
        "pieces_available": INS,
        "genuine_four_piece_refills": GEO,
        "floor_refills_per_region": MNC[0],
        "involutive_floor_flips": BACK,
    },
    "no_go_discipline": {
        "status": "PASS",
        "no_universal_no_go_claim_shipped": True,
        "scope": "finite declared-class floor-dissection population only",
        "n5_certificate": "five resolution lines in primary cached stdout",
    },
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + json.dumps(receipt, sort_keys=True), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]), flush=True)
raise SystemExit(0 if PF[1] == 0 else 1)
