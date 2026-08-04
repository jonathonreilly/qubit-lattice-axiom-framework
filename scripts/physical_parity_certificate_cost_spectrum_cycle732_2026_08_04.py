"""Cycle 732: a parity certificate for the single cell, and the exact cost spectrum.

THE OBJECT.  The cell is the unit four-box over the lattice: three spatial coordinates
and one tick, sixteen corners.  A piece is a five-corner set of least volume; its
adjacency charge counts the corner pairs whose spatial separation exceeds one step.  A
dissection of the cell is a family of twenty four pieces with disjoint interiors whose
union is the cell, and its cost is the sum of the piece charges.

WHAT IS ALREADY MEASURED IN THIS LANE.  The cost of a dissection lies between 108 and
128, both ends attained, each end certified by an exhibited integer combination of the
piece inequalities.  A further certificate turns the lower end into an equality: the
floor slack takes only two values, so the cost is 108 plus the number of pieces outside
the tight set.

WHAT THIS ADDS: a congruence, and with it the whole spectrum.

  1.  PARITY.  There is a set S of sample points, each interior to the cell and none on
      any piece boundary, with

          the number of points of S inside p  ==  charge(p)   modulo 2

      on every one of the 2672 pieces of least volume.  Every sample point lies inside
      exactly one piece of any dissection, so summing the congruence over a dissection
      gives cost == the size of S modulo 2.  The set exhibited here has 228 points, an
      even number, so EVERY dissection of the cell has EVEN cost.  The argument uses no
      solver and no piece count: only the exhibited set and the 2672 verified rows.

  2.  HOW MUCH SYMMETRY A CERTIFICATE CAN KEEP.  The cell has 48 symmetries, the 24
      proper rotations with and without the tick flip.  No parity certificate is
      invariant under all of them.  Sweeping every subgroup: of the twelve subgroups of
      order twelve or more, exactly one admits an invariant certificate, and it is a
      twelve element subgroup of pure rotations, no tick flip, with rotation traces 3
      once, 0 eight times and -1 three times.  So a certificate must drop the symmetry
      by index four, and need drop no more.  The set S above is a union of nineteen
      orbits of that subgroup.

  3.  PARITY IS THE SHARP CONGRUENCE, by two independent routes.  Eleven dissections are
      exhibited, one of each even cost from 108 to 128, each validated in full: twenty
      four distinct pieces of least volume, pairwise disjoint by an exhibited integer
      separating direction, covering every sample point.  Their costs differ by 2, so no
      modulus above 2 divides every cost difference.  Independently, the point level
      system has no solution modulo 3.

  4.  THE SPECTRUM.  The two bounding certificates give 108 <= cost <= 128, the parity
      certificate makes every cost even, and the eleven dissections attain every even
      value between.  The cost spectrum of the cell is exactly the eleven even integers
      108, 110, ..., 128.

METHOD.  No solver appears in this artifact.  The certificate is produced by exact
Gaussian elimination over a prime field and then verified row by row in integer
arithmetic; the negative result modulo three is the same elimination reporting an
inconsistent row.  Subgroups are found by closing generator sets to a fixpoint, which
reaches every subgroup because any subgroup is the last link of a chain of single
generator extensions, and the family is checked closed under one more extension.
Dissections are exhibited, never searched for inside the artifact: each pinned piece
list is checked for least volume, for pairwise disjointness against an exhibited integer
direction, and for covering all 2736 sample points.

Every number quoted in the companion note is printed below.
"""
import itertools
import math

import numpy as np

PF = [0, 0]


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail)


def sec(text):
    print("")
    print(text)


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

sec("the group table and the exact elimination used below")

ELS = [tuple(int(c) for c in g[2]) for g in G]
IDX = dict((e, i) for i, e in enumerate(ELS))
qpos = dict((tuple(int(c) for c in row), i) for i, row in enumerate(Q))
PERM = []
for (R, tf, _) in G:
    pr = np.empty(NQ, dtype=np.int64)
    for i, row in enumerate(Q):
        u = R @ (row[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]),
               (SB - int(row[3])) if tf else int(row[3]))
        pr[i] = qpos[key]
    PERM.append(pr)
TAB = [[IDX[tuple(ELS[a][c] for c in ELS[b])] for b in range(48)] for a in range(48)]
E = ELS.index(tuple(range(16)))
gate(len(IDX) == 48 and all(TAB[a][E] == a and TAB[E][a] == a for a in range(48)),
     "grp.table", "the 48 elements act faithfully on the corners, compose, and share an "
                  "identity")


def gen(H, g):
    """the subgroup generated by H together with g, closed to a fixpoint"""
    S, fr = set(H), [g]
    S.add(g)
    while fr:
        a = fr.pop()
        for b in list(S):
            for c in (TAB[a][b], TAB[b][a]):
                if c not in S:
                    S.add(c)
                    fr.append(c)
    return frozenset(S)


def orbits(H):
    lb, nxt = -np.ones(NQ, dtype=np.int64), 0
    for i in range(NQ):
        if lb[i] >= 0:
            continue
        for g in H:
            lb[PERM[g][i]] = nxt
        nxt += 1
    return lb, nxt


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


sec("how much of the symmetry a parity certificate can keep")

subs, todo = set([frozenset([E])]), [frozenset([E])]
while todo:
    H = todo.pop()
    for a in range(48):
        if a in H:
            continue
        K = gen(H, a)
        if K not in subs:
            subs.add(K)
            todo.append(K)
SHUT = all(all(TAB[a][b] in H for a in H for b in H) and E in H for H in subs)
LAG = all(divmod(len(G), len(H))[1] == 0 for H in subs)
gate(len(subs) == 98 and SHUT and LAG,
     "lad.closed", "closing every one-element extension to a fixpoint reaches {0} sets, "
                   "each of them shut under composition, holding the identity, and of "
                   "order dividing {1}".format(len(subs), len(G)))

BIG = sorted([H for H in subs if len(H) >= 12], key=lambda h: (-len(h), sorted(h)))
CEN2 = [(d, sum(1 for H in BIG if len(H) == d))
        for d in sorted(set(len(H) for H in BIG), reverse=True)]
gate(CEN2 == [(48, 1), (24, 3), (16, 3), (12, 5)],
     "lad.orders", "subgroups of order at least 12, counted by order: {0}".format(CEN2))

CXB = (CX & 1).astype(np.int16)
wins = []
for H in BIG:
    lb, nb = orbits(H)
    A = np.zeros((NPIECE, nb + 1), dtype=np.int16)
    for o in range(nb):
        A[:, o] = MI[:, lb == o].sum(axis=1)
    A[:, nb] = 1
    x, _ = solvep(A, CXB, 2)
    if x is not None:
        wins.append((H, lb, nb, x))
gate(len(wins) == 1,
     "lad.unique", "{0} of the {1} subgroups of order at least 12 admits an invariant "
                   "certificate".format(len(wins), len(BIG)))
OVER = [H for H in BIG if len(H) > 12]
WO = sorted(len(H) for H, _, _, _ in wins)
gate(len(OVER) == 7 and max(WO) == 12 and len(G) // max(WO) == 4,
     "lad.index", "all {0} subgroups of order above 12 fail and one of order {1} "
                  "succeeds, so the symmetry drops by index {2} and no more".format(
                      len(OVER), max(WO), len(G) // max(WO)))

HW, LBW, NBW, XW = wins[0]
tick = sum(1 for g in HW if G[g][1])
tr = sorted(int(np.trace(G[g][0])) for g in HW)
gate(tick == 0 and tr == [-1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 3],
     "lad.rotations", "the surviving subgroup carries the tick flip on {0} of its "
                      "elements and has rotation traces {1}".format(tick, tr))
OSZ = sorted(set(int((LBW == o).sum()) for o in range(NBW)))
gate(NBW == 228 and OSZ == [12],
     "lad.pointorbits", "it splits the {0} sample points into {1} orbits, sizes "
                        "{2}".format(NQ, NBW, OSZ))

sec("the parity certificate")

W = np.zeros(NQ, dtype=np.int64)
for o in range(NBW):
    if XW[o]:
        W[LBW == o] = 1
ZC = int(XW[NBW])
SSZ = int(W.sum())
gate(bool((np.remainder(MI @ W + ZC, 2) == CXB).all()),
     "par.rows", "the exhibited point set meets every one of the {0} pieces in a number "
                 "of points congruent to that piece's charge modulo 2".format(NPIECE))
gate(ZC == 0,
     "par.shift", "the certificate carries no constant term, so the argument never uses "
                  "how many pieces a dissection has")
gate(SSZ == 228 and (SSZ & 1) == 0,
     "par.even", "the point set has {0} points, an even number, which is what forces "
                 "every cost to be even".format(SSZ))
NSUP = sorted(set(int((LBW == o).sum()) for o in range(NBW) if XW[o]))
gate(int(XW[:NBW].sum()) == 19 and NSUP == [12],
     "par.orbits", "it is a union of {0} orbits of the surviving subgroup, sizes "
                   "{1}".format(int(XW[:NBW].sum()), NSUP))
STAB = sum(1 for g in range(48) if bool((W[PERM[g]] == W).all()))
gate(STAB == 12 and all(bool((W[PERM[g]] == W).all()) for g in HW),
     "par.stab", "exactly {0} of the {1} symmetries of the cell fix the point set, and "
                 "they are the surviving subgroup".format(STAB, len(G)))
BRK = MI.sum(axis=0)
gate(int(BRK.min()) == 90,
     "par.point", "moving any single one of the {0} sample points into or out of the set "
                  "breaks at least {1} of the {2} rows".format(NQ, int(BRK.min()), NPIECE))
gate(int((np.remainder(MI @ W + ZC + 1, 2) != CXB).sum()) == NPIECE,
     "par.const", "changing the constant term by one breaks every row")
gate(not bool((np.remainder(MI @ (1 - W) + ZC, 2) == CXB).all()) and
     not bool((np.remainder(MI @ np.ones(NQ, dtype=np.int64) + ZC, 2) == CXB).all()),
     "par.wrong", "neither the complementary point set nor the set of all sample points "
                  "certifies the same congruence")

sec("no rule modulo three, exhibited on four pieces and confirmed twice over")

AP = np.zeros((NPIECE, NQ + 1), dtype=np.int16)
AP[:, :NQ] = MI
AP[:, NQ] = 1
TG3 = np.remainder(CX, 3).astype(np.int16)
X3, R3 = solvep(AP, TG3, 3)
X2, R2 = solvep(AP, CXB, 2)

# The obstruction, exhibited rather than reported as the outcome of a search.  These four
# pieces of least volume all sit inside a single six corner subset of the cell, and taken
# with the multiplicities below they cover part of the cell exactly three times over and
# the rest of it not at all.  Any rule assigning a residue modulo three to each piece
# would have to hand that triple cover a total divisible by three.  The charges decline.
DUAL = [(72, 1), (74, 2), (176, 2), (479, 1)]
DJ = [j for j, _ in DUAL]
DC = np.array([c for _, c in DUAL], dtype=np.int64)
DSIX = sorted(set(int(t) for j in DJ for t in UNI[j]))
DCOL = DC @ MI[DJ]
DCH = int(DC @ CX[DJ])
gate(len(DSIX) == 6 and sorted(set(int(t) for t in DCOL)) == [0, 3] and
     int(np.remainder(DC.sum(), 3)) == 0 and int(np.remainder(DCH, 3)) != 0,
     "cong.witness",
     "four pieces inside the six corner set {0}, counted {1} times over, cover {2} sample "
     "points three times each and the remaining {3} not at all, and their multiplicities "
     "add to {4}; their charges {5} add to {6}, which is {7} modulo 3".format(
         DSIX, [c for _, c in DUAL], int((DCOL == 3).sum()), int((DCOL == 0).sum()),
         int(DC.sum()), [int(CX[j]) for j in DJ], DCH, int(np.remainder(DCH, 3))))

# and the same obstruction is a common local feature, not one freak configuration
LOOK = {}
for j in range(NPIECE):
    LOOK[tuple(int(t) for t in UNI[j])] = j
NSIX, loc, held = 0, 0, {}
for S in itertools.combinations(range(16), 6):
    NSIX += 1
    js = [LOOK.get(tuple(t for t in S if t != om)) for om in S]
    js = [j for j in js if j is not None]
    if len(js) < 2:
        continue
    if solvep(AP[js], TG3[js], 3)[0] is None:
        loc += 1
        held[len(js)] = held.get(len(js), 0) + 1
gate(NSIX == 8008 and loc == 1104 and sorted(held.items()) == [(4, 864), (6, 240)],
     "cong.local", "of the {0} six corner subsets of the cell, {1} carry such an "
                   "obstruction using their own pieces alone: {2} of them hold four pieces "
                   "of least volume and {3} hold six".format(
                       NSIX, loc, held.get(4, 0), held.get(6, 0)))
gate(X3 is None,
     "cong.mod3", "eliminating the whole point level system agrees: rank {0} modulo 3 "
                  "with an inconsistent row, so no certificate modulo 3 exists".format(R3))
gate(X2 is not None and R2 == 465,
     "cong.mod2", "the same system has rank {0} modulo 2 and is consistent".format(R2))

sec("eleven dissections, one of each even cost")

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


COST = [int(CX[np.array(d)].sum()) for d in DIS]
gate(all(is_dissection(d) for d in DIS),
     "wit.dissect", "all {0} pinned covers are dissections: 24 distinct pieces of least "
                    "volume, pairwise disjoint by an exhibited direction, every sample "
                    "point covered".format(len(DIS)))
gate(COST == list(range(108, 129, 2)),
     "wit.cost", "their costs are {0}".format(COST))
gate(all(int(MI[np.array(d)].sum(axis=0).max()) == 1 for d in DIS),
     "wit.once", "every sample point lies inside exactly one piece of each of them, which "
                 "is the step that turns the row congruence into a claim about cost")
gate(all(int((MI[np.array(d)] @ W).sum()) == SSZ for d in DIS),
     "wit.count", "summing the point set over the pieces of each dissection returns {0} "
                  "every time".format(SSZ))
gate(all((c & 1) == 0 for c in COST),
     "wit.even", "every exhibited cost is even, as the certificate requires")
GG = 0
for c in COST:
    GG = math.gcd(GG, c - COST[0])
gate(GG == 2,
     "wit.sharp", "the greatest common divisor of the cost differences is {0}, so no "
                  "modulus above 2 divides all of them".format(GG))

sec("the bounding certificates and the spectrum")

FLOOR_U = [(0, -36), (4, 144), (19, 64), (20, -36), (34, 216), (35, 135),
           (44, -216), (45, 36), (51, -72), (52, 163), (53, -172), (54, -118)]
FLOOR_D, FLOOR_Z = 216, 756
CEIL_U = [(0, 3), (4, 3), (20, 3), (22, -5), (34, 4), (35, -31), (36, 31),
          (37, 6), (43, 2), (44, -4), (45, -1), (51, -1), (52, -2)]
CEIL_D, CEIL_Z = 3, 0
ROWM = np.zeros((NPIECE, NORB), dtype=np.int64)
for o in range(NORB):
    ROWM[:, o] = MI[:, PORB == o].sum(axis=1)
MOF = np.bincount(PORB, minlength=NORB).astype(np.int64)


def build(dat):
    u = np.zeros(NORB, dtype=np.int64)
    for j, w in dat:
        u[j] = w
    return u


def slacks(u, Z, D, upper):
    s = (ROWM @ u + Z) - D * CX
    return s if upper else -s


def value(u, Z):
    return int((MOF * u).sum()) + 24 * Z


FU, CU = build(FLOOR_U), build(CEIL_U)
FS, CSL = slacks(FU, FLOOR_Z, FLOOR_D, False), slacks(CU, CEIL_Z, CEIL_D, True)
FV, CV = value(FU, FLOOR_Z), value(CU, CEIL_Z)
gate(bool((FS >= 0).all()) and FV == 108 * FLOOR_D,
     "cert.floor", "the floor rows hold on all {0} pieces and sum to {1}, which is 108 "
                   "times {2}".format(NPIECE, FV, FLOOR_D))
gate(bool((CSL >= 0).all()) and CV == 128 * CEIL_D,
     "cert.ceil", "the ceiling rows hold on all {0} pieces and sum to {1}, which is 128 "
                  "times {2}".format(NPIECE, CV, CEIL_D))
gate(min(COST) == 108 and max(COST) == 128,
     "cert.attain", "the exhibited costs run from {0} to {1}, so both bounds are "
                    "attained".format(min(COST), max(COST)))
gate(sorted(set(COST)) == list(range(108, 129, 2)) and len(set(COST)) == 11,
     "cert.spectrum", "bounded below by 108, above by 128, even by the certificate, and "
                      "every even value between attained: the cost spectrum of the cell "
                      "is exactly {0}".format(sorted(set(COST))))

print("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
