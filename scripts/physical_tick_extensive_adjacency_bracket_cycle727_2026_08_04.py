"""Tick-extensive adjacency bracket for the two-tick lattice box -- cycle 727.

One lattice cell carried through two ticks is the box {0,1}^3 x {0,1,2}: 24 corners and
volume 2, so a corner dissection into minimal-volume pieces uses 48 of them.  The
adjacency charge of a piece counts the vertex pairs whose spatial separation exceeds one
nearest-neighbour step; the LATTICE axiom supplies spatial adjacency only, and the tick
direction is emergent and carries no weight of its own.

The bracket over all minimal-volume corner dissections of this box is exactly [216, 256]
-- twice the one-tick bracket [108, 128] at both ends.  Both bounds are carried by
integer certificates that verify by arithmetic over every one of the 17280 minimal
pieces, and both ends are attained by dissections certified piece by piece with exhibited
separating hyperplanes.  No solver reads anything here.

Why a certificate suffices.  A dissection covers each sample point exactly once and uses
exactly 48 pieces, and every point orbit carries exactly 48 points, so for integers u
(one per point orbit) and Z obeying

    BO . u + Z  <=  D * BX     on every minimal piece,

every dissection costs at least 48 (sum u + Z)/D; with the inequality reversed the same
sum bounds the cost from above.  Symmetry enters only to say the multipliers are constant
on orbits, which shrinks the certificate from 17472 numbers to one per orbit.  The
inequality itself is checked on all 17280 pieces.

Both certificates are exact -- 216 on the nose and 256 on the nose -- but they sit at very
different denominators.  Every point orbit carries 48 points, so the value is always
48 (sum u + Z)/D: reaching 216 wants D even, and reaching 256 wants D a multiple of three.
The floor is carried at denominator 2 and the ceiling at denominator 48, and the runner
checks both divisibility conditions on the numbers it actually embeds.

A second charge appears at two ticks: the tick-span charge, counting vertex pairs whose
tick separation exceeds one.  It vanishes identically on any one-tick box, and here it
vanishes on exactly the slab-confined pieces.

Everything below is measured, not derived from the numbers it reports.
"""
import numpy as np
from itertools import combinations, permutations, product

PASS = 0
FAIL = 0


def gate(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tail = "  " + detail if detail else ""
    print("{0} {1}{2}".format("PASS" if ok else "FAIL", name, tail))


def fmt(x):
    return "{0:.6f}".format(float(x))


PR = np.array(list(combinations(range(5), 2)), dtype=np.int64)
NEG = np.array([v for v in product((-1, 0, 1), repeat=4) if any(v)], dtype=np.int64)


def dets(V):
    return np.rint(np.linalg.det(
        (V[:, 1:, :] - V[:, :1, :]).astype(np.float64))).astype(np.int64)


def adjug(V):
    """(det, adjugate) of each piece's edge matrix, as exact integers."""
    Mx = (V[:, 1:, :] - V[:, :1, :]).transpose(0, 2, 1).astype(np.float64)
    d = np.rint(np.linalg.det(Mx)).astype(np.int64)
    A = np.rint(np.linalg.inv(Mx) * d[:, None, None]).astype(np.int64)
    return d, A


def bxcost(V):
    return ((np.abs(V[:, PR[:, 0], :3] - V[:, PR[:, 1], :3]).sum(axis=2)) > 1).sum(axis=1)


def tscost(V):
    return (np.abs(V[:, PR[:, 0], 3] - V[:, PR[:, 1], 3]) > 1).sum(axis=1)


def spectrum(a):
    v, c = np.unique(a, return_counts=True)
    return dict(zip(v.tolist(), c.tolist()))


def facet_normals(V):
    """the five integer facet normals of each piece: adjugate rows and their negated sum."""
    d, A = adjug(V)
    A = A * np.sign(d)[:, None, None]
    return np.concatenate([A, -A.sum(axis=1, keepdims=True)], axis=1)


def separated(V):
    """count piece pairs for which a separating integer normal is exhibited."""
    n = len(V)
    FN = facet_normals(V)
    good = 0
    for i in range(n):
        for j in range(i + 1, n):
            N = np.concatenate([NEG, FN[i], FN[j]], axis=0)
            a, b = V[i] @ N.T, V[j] @ N.T
            if bool(((a.max(axis=0) <= b.min(axis=0)) |
                     (b.max(axis=0) <= a.min(axis=0))).any()):
                good += 1
    return good, n * (n - 1) // 2


def dissection(V, boxvol):
    """(all pieces minimal, pairs separated, pairs total, volume matches the box)."""
    vv = np.abs(dets(V))
    g, t = separated(V)
    return (int(vv.min()) == 1 and int(vv.max()) == 1, g, t,
            int(vv.sum()) == 24 * boxvol)


def box(nt):
    """corners of one lattice cell carried through nt ticks."""
    return np.array([[a, b, c, t] for t in range(nt + 1)
                     for a in range(2) for b in range(2) for c in range(2)],
                    dtype=np.int64)


def pieces(COR):
    SUB = np.array(list(combinations(range(len(COR)), 5)), dtype=np.int64)
    V = COR[SUB]
    d = np.abs(dets(V))
    keep = d == 1
    return SUB, d, SUB[keep], V[keep]


COR1, COR2 = box(1), box(2)
SUB2, VOL2, CELL2, V2 = pieces(COR2)
CELL1, V1 = pieces(COR1)[2:]
K2, K1 = len(CELL2), len(CELL1)
BX2, BX1 = bxcost(V2), bxcost(V1)
TS2, TS1 = tscost(V2), tscost(V1)
NP = 24 * 2

print("two-tick box: one lattice cell carried through two ticks")
gate("corner count", len(COR2) == 24 and len(COR1) == 16,
     "two-tick 24 one-tick 16")
gate("five-subset census", len(SUB2) == 42504, "subsets 42504")
gate("volume spectrum", spectrum(VOL2) == {0: 13152, 1: 17280, 2: 9840, 3: 1472,
                                           4: 680, 5: 64, 6: 16},
     "{0}".format(sorted(spectrum(VOL2).items())))
gate("minimal pieces", K2 == 17280 and K1 == 2672,
     "two-tick 17280 one-tick 2672")
gate("pieces per dissection", NP == 48, "24 * boxvol = 48")

print("charges")
gate("adjacency charge range", (int(BX2.min()), int(BX2.max())) == (3, 7), "(3, 7)")
gate("adjacency spectrum", spectrum(BX2) == {3: 432, 4: 2592, 5: 7488, 6: 4896,
                                             7: 1872},
     "{0}".format(sorted(spectrum(BX2).items())))
gate("trivial counting bounds", (NP * int(BX2.min()), NP * int(BX2.max())) == (144, 336),
     "floor 144 ceiling 336")
gate("tick-span charge range", (int(TS2.min()), int(TS2.max())) == (0, 4), "(0, 4)")
gate("tick-span spectrum", spectrum(TS2) == {0: 5344, 1: 1744, 2: 4944, 3: 3040,
                                             4: 2208},
     "{0}".format(sorted(spectrum(TS2).items())))
gate("tick-span is new at two ticks", int(TS1.max()) == 0,
     "identically zero on the one-tick box")

SPAN = V2[:, :, 3].max(axis=1) - V2[:, :, 3].min(axis=1)
SEAM = SPAN == 2
gate("slab-confined count", int((~SEAM).sum()) == 5344 and 5344 == 2 * K1,
     "5344 = 2 * 2672")
gate("seam-crossing count", int(SEAM.sum()) == 11936, "11936")
gate("slab-confined charge doubles the one-tick spectrum",
     spectrum(BX2[~SEAM]) == dict((k, 2 * v) for k, v in spectrum(BX1).items()),
     "{0}".format(sorted(spectrum(BX2[~SEAM]).items())))
gate("seam pieces reach the same least charge", int(BX2[SEAM].min()) == 3,
     "least charge 3 on both sides of the split")
gate("tick-span splits along the seam",
     int(TS2[~SEAM].max()) == 0 and int(TS2[SEAM].min()) > 0,
     "zero exactly on the slab-confined pieces")

print("box symmetry, used only to compress the certificate")
ROT = []
for perm in permutations(range(3)):
    for sg in product((-1, 1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if int(round(np.linalg.det(R.astype(np.float64)))) == 1:
            ROT.append(R)
IDX = {tuple(c): i for i, c in enumerate(COR2.tolist())}
GP = []
for R in ROT:
    for tf in (0, 1):
        img = []
        for c in COR2:
            w = R @ (2 * c[:3] - 1)
            s = (2 - c[3]) if tf else c[3]
            img.append(IDX[tuple(((w + 1) // 2).tolist() + [int(s)])])
        GP.append(img)
GP = np.array(GP, dtype=np.int64)
gate("proper cubic rotations", len(ROT) == 24, "24")
gate("group order", len(GP) == 48 and len(set(map(tuple, GP.tolist()))) == 48,
     "24 rotations times the tick relabelling, 48 distinct corner permutations")

CODE = {tuple(c): i for i, c in enumerate(CELL2.tolist())}
orb = np.full(K2, -1, dtype=np.int64)
reps = []
for p in range(K2):
    if orb[p] >= 0:
        continue
    o = len(reps)
    reps.append(p)
    for g in range(48):
        orb[CODE[tuple(sorted(GP[g][CELL2[p]].tolist()))]] = o
NO = len(reps)
OSZ = np.bincount(orb, minlength=NO)
gate("piece orbits", NO == 364 and sorted(spectrum(OSZ).items()) == [(16, 6), (48, 358)],
     "364 orbits, 6 of size 16 and 358 of size 48")
gate("adjacency charge is constant on every orbit",
     bool((BX2 == BX2[np.array(reps)][orb]).all()),
     "one charge per orbit")

print("sample points, generic by construction and verified generic")
DT2, AJ2 = adjug(V2)
CMAX = 0
for i0 in range(0, K2, 512):
    sl = slice(i0, i0 + 512)
    lam = np.einsum("cij,cpj->cpi", AJ2[sl] * DT2[sl, None, None],
                    COR2[None, :, :] - V2[sl, :1, :])
    CMAX = max(CMAX, int(np.abs(lam).max()), int(np.abs(lam.sum(axis=2) - 1).max()))
OFF = [0]
while len(OFF) < 5:
    OFF.append(CMAX * sum(OFF) + 1)
BASE = CMAX * sum(OFF) + 1
W = 2 * np.array([BASE + o for o in OFF], dtype=np.int64)
S = int(W.sum())
gate("barycentric integers are bounded", CMAX == 6,
     "no corner sees a barycentric integer above 6 on any minimal piece")
gate("weights are generic by construction and near-uniform",
     W.tolist() == [4802, 4804, 4816, 4900, 5488] and S == 24810,
     "spread {0} below 1.15".format(fmt(W.max() / float(W.min()))))

pts, pid = [], []
for o, p in enumerate(reps):
    q = (W[:, None] * V2[p]).sum(axis=0)
    for g in range(48):
        w = ROT[g // 2] @ (2 * q[:3] - S)
        s = (2 * S - q[3]) if (g & 1) else q[3]
        pts.append(((w + S) // 2).tolist() + [int(s)])
        pid.append(o)
Q = np.array(pts, dtype=np.int64)
PID = np.array(pid, dtype=np.int64)
gate("point family", len(Q) == 17472 and len(np.unique(Q, axis=0)) == 17472,
     "one point per orbit carried around the group, 17472 distinct")
gate("points per orbit", spectrum(np.bincount(PID)) == {48: 364},
     "every orbit carries 48 points")

BO = np.zeros((K2, NO), dtype=np.int64)
BND = 0
for i0 in range(0, K2, 96):
    sl = slice(i0, i0 + 96)
    nb = min(96, K2 - i0)
    lam = np.einsum("cij,cpj->cpi", AJ2[sl] * DT2[sl, None, None],
                    Q[None, :, :] - S * V2[sl, :1, :])
    tot = lam.sum(axis=2)
    ins = ((lam > 0).all(axis=2) & (tot < S)).astype(np.int64)
    BND += int(((lam == 0).any(axis=2) | (tot == S)).sum())
    BO[sl] = ins.reshape(nb, NO, 48).sum(axis=2)
gate("no sample point lands on a piece boundary", BND == 0,
     "boundary incidences 0 over all {0} pieces".format(K2))
gate("membership is constant on every orbit",
     bool((BO == BO[np.array(reps)][orb]).all()),
     "{0} rows carry {1} distinct".format(K2, len(np.unique(BO, axis=0))))

print("witnesses, certified piece by piece with exhibited separating normals")
STEP = (4, 2, 1, 8)


def stencil(t0):
    """the 24 monotone corner paths across the slab from tick t0 to tick t0 + 1."""
    out = []
    for p in permutations(STEP):
        v, path = 8 * t0, [8 * t0]
        for s in p:
            v += s
            path.append(v)
        out.append(path)
    return out


ONE = [[0, 1, 2, 4, 12], [0, 1, 2, 8, 12], [1, 2, 3, 7, 10], [1, 2, 4, 6, 12],
       [1, 2, 6, 7, 12], [1, 2, 7, 8, 10], [1, 2, 7, 8, 12], [1, 3, 7, 10, 11],
       [1, 4, 5, 7, 12], [1, 4, 6, 7, 12], [1, 5, 7, 12, 13], [1, 7, 8, 9, 10],
       [1, 7, 8, 9, 12], [1, 7, 9, 10, 11], [1, 7, 9, 12, 13], [2, 6, 7, 10, 12],
       [2, 7, 8, 10, 12], [6, 7, 10, 12, 14], [7, 8, 9, 10, 15], [7, 8, 9, 12, 15],
       [7, 8, 10, 12, 15], [7, 9, 10, 11, 15], [7, 9, 12, 13, 15], [7, 10, 12, 14, 15]]
LOW = [c for c in ONE]
UPP = [[i + 8 for i in c] for c in ONE]
FAM = (("least-charge witness", stencil(0) + stencil(1), 216),
       ("greatest-charge witness", LOW + UPP, 256))
COST = {}

for tag, cells, cost in FAM:
    CE = np.array(cells, dtype=np.int64)
    VV = COR2[CE]
    mn, sep, tot, vol = dissection(VV, 2)
    gate("{0} is a dissection".format(tag), len(CE) == NP and mn and vol,
         "48 pieces, every one of volume one, volumes summing to the box")
    gate("{0} pieces are pairwise interior-disjoint".format(tag), sep == tot,
         "{0} of {1} pairs carry an exhibited separating normal".format(sep, tot))
    COST[tag] = int(bxcost(VV).sum())
    gate("{0} charge".format(tag), COST[tag] == cost,
         "adjacency charge {0}".format(cost))
    gate("{0} respects the seam".format(tag), int(tscost(VV).max()) == 0,
         "tick-span charge zero on every piece")

print("the one-tick box, measured here so the doubling is not a supplied number")
ONEFAM = (("one-tick least-charge witness", stencil(0), 108),
          ("one-tick greatest-charge witness", ONE, 128))

for tag, cells, cost in ONEFAM:
    VV = COR1[np.array(cells, dtype=np.int64)]
    mn, sep, tot, vol = dissection(VV, 1)
    gate("{0} is a dissection".format(tag), len(cells) == 24 and mn and vol,
         "24 pieces, every one of volume one, volumes summing to the box")
    gate("{0} pieces are pairwise interior-disjoint".format(tag), sep == tot,
         "{0} of {1} pairs carry an exhibited separating normal".format(sep, tot))
    COST[tag] = int(bxcost(VV).sum())
    gate("{0} charge".format(tag), COST[tag] == cost,
         "adjacency charge {0}".format(cost))

gate("the tick-span charge vanishes identically on the one-tick box",
     int(tscost(COR1[CELL1]).max()) == 0,
     "zero on all {0} minimal one-tick pieces".format(len(CELL1)))
gate("both ends of the bracket double",
     COST["least-charge witness"] == 2 * COST["one-tick least-charge witness"]
     and COST["greatest-charge witness"] == 2 * COST["one-tick greatest-charge witness"],
     "{0} and {1} against {2} and {3}"
     .format(COST["least-charge witness"], COST["greatest-charge witness"],
             COST["one-tick least-charge witness"],
             COST["one-tick greatest-charge witness"]))

print("integer certificates, arithmetic over every one of the 17280 minimal pieces")
FLOOR_U = [22, 60, 60, 14, -60, -58, 15, 55, 10, 60, -60, -60, -3, 20, 56, -60, 60, -60, 60,
    -60, -5, -30, -13, -60, -47, -20, -60, -60, -60, -60, -60, -60, 60, 37, -60, -60, 19, 60,
    33, -60, -60, 60, 60, -58, 60, 14, -60, 60, 55, -44, -32, 60, 60, -39, 60, -60, -55, -3,
    -60, 60, -60, -60, -60, 60, 60, -26, 57, -60, 11, 60, 60, -60, 20, 59, -17, -60, 21, 60,
    60, -60, -60, 14, 52, -48, -60, -60, -60, -60, 60, 60, 60, 60, 44, -16, 39, -60, -60, 60,
    55, 60, -60, 16, 60, -60, -60, 60, 60, -60, 47, -24, 51, -60, -60, -60, 60, -60, 40, -21,
    60, 60, 60, -60, 49, -60, 51, 60, 60, -60, -57, -60, 60, 60, 60, 60, 60, 60, 60, 60, -60,
    -57, 60, 60, -60, 53, 60, 44, -33, 60, 60, 40, -59, 60, 60, 37, 60, 58, 60, 60, 60, 6, 60,
    -17, -60, 60, 60, -60, -60, 47, -2, -57, -18, 17, -60, 60, -60, -60, 60, -20, 60, 60, 60,
    -50, 6, 60, 60, 60, -60, 60, -60, -52, -59, -60, 58, -60, 60, -60, 60, 60, 60, -44, -60,
    -60, -60, 60, 60, 8, -35, -8, 22, -60, -8, -60, -60, 60, -26, 31, -5, 59, 60, -60, -60,
    -60, 60, 15, -43, 29, 60, 60, 60, 60, -58, -60, -60, -43, -60, -59, -51, 60, 6, -56, 5,
    -4, 60, -60, -60, -57, 58, 47, 60, 60, 37, -60, 60, -60, 29, -60, -60, 60, -60, -13, 17,
    -60, -60, 53, 60, -60, 60, -43, 60, -36, -56, -60, -18, 60, -60, -39, 60, -60, -60, -60,
    60, -60, -60, 60, -60, 60, 25, -60, 48, 60, -60, -60, -60, 60, -60, -54, -60, 60, 60, -60,
    17, -7, -36, -60, -25, 60, 60, -57, -60, -5, -60, -54, -60, 60, 23, -60, 60, 60, -58, 60,
    46, -60, -60, -44, 36, 60, 53, -60, -37, 19, 28, -59, -60, 58, -60, -60, 60, -60, 60, 10,
    59, 25, -60, -60, -51, 60, 60, 60, -10, 52, -60, -54, 60, -32, 60, 0, 60, 57, 60, -60,
    -60, -60, 60, 20]
FLOOR_Z = -60
FLOOR_D = 2
CEIL_U = [-2592, 5694, -8622, 8640, -8634, 8640, -2034, 5004, -8634, -8640, -8004, -8622,
    5172, 1194, -708, 8640, -8640, -8622, 4824, 8562, 8220, 8640, -8640, -8640, 3354, -8640,
    8640, -8640, -8640, 4470, 1392, 8640, 8640, 8640, 8640, -8640, 8640, 8640, -8640, -8640,
    -8640, -8640, -8640, -8640, 8640, 8184, -792, -8640, -8640, 8640, 504, 8640, 8640, -8640,
    -8640, -8526, 8640, -8640, -1626, 8592, 8640, -8640, 1668, -8592, -4440, 8640, 8634,
    -8640, -5430, 8640, 7350, 8640, -6558, -8640, -8640, -7686, -8640, -8640, 6396, 72, 8640,
    -8640, -8640, -8640, 8640, 8640, -894, -8640, 8634, -8640, 8640, 8640, -8640, -8640,
    -8640, -8640, 8610, -8640, 8640, -8640, 8640, -8610, 8640, -8628, -6624, 8622, 8640, 8640,
    4602, 8640, 8640, 4194, 8640, 8640, 8640, 2778, -8640, 8640, 8640, 8640, -8640, 8640,
    8640, 8640, 8640, -8640, -8640, -8640, -8640, 8640, 8640, 8640, -8640, -7530, 8640, -8640,
    -8640, 8640, -8640, 8640, -8640, -8640, 8640, 8640, -8640, -8640, 8640, -8640, -8640,
    8640, 8640, -8640, 8640, 8640, 8640, -8640, 8640, 8640, -8640, -8640, 8640, 8640, 8610,
    -8640, 8640, 8640, 8640, 8640, 8640, 8640, -8640, -8082, -5796, 8640, -8640, -8640, -8640,
    8640, 132, -8640, 8178, 8640, -8628, -8640, -8640, 8640, 8640, 8640, 5466, -8640, -8640,
    -7488, 8640, 1788, -8640, 8640, 8640, -8640, -8640, 8640, 8640, -8634, -8628, -8634,
    -8640, 8640, 8616, 6510, 1446, 8640, -8640, 2406, 8640, 8640, -8640, -8640, -8640, -4158,
    -8544, -8640, 8640, -2184, -8640, 8640, -8640, -8640, 8640, -8640, 8640, -834, -8640,
    -8640, -8640, -8640, -8640, -8640, 8640, -564, 8640, 8640, -8640, -7260, -8640, 8640,
    -8640, -8640, 8640, -8634, -8640, -8640, -8640, -8640, 8640, -8640, -8640, -8640, -8640,
    2358, 8640, -8640, 8640, -8640, 8640, 1194, -8640, 8640, 8640, -5088, 8640, -6102, -8640,
    8640, 8640, 2892, 8640, 8640, 7878, 8640, 8640, -8640, -2754, 8640, -8640, 8640, -8640,
    540, 8634, 8640, -558, -1164, -8640, 8640, -8640, 318, -8640, -4422, -8640, 8640, -8640,
    -8640, 6708, -6060, 8640, 8640, 8640, 8640, 8640, 8640, 8640, -6444, 8640, 8622, 8640,
    8640, -8640, 8640, 8640, -8640, -8640, -8640, 8640, 8640, -8640, -8640, 2568, 8640, -8640,
    -8640, -3138, 8640, -8478, 8640, 8640, 8640, 8640, -8640, 8640, -8640, 8640, -8640, -8562,
    -5988, 8640, 8640, -8610, 2568, -8640, -8640, -8640, -8640, 8640, 8640, -8640, 8640, 8640,
    1818, -8568, -8640, 8622, -8640, -5280, -2862, 8478, -4746]
CEIL_Z = 8640
CEIL_D = 288


def carries(u, Z, D, low):
    """least slack of the certificate inequality over every minimal piece."""
    s = BO @ u + Z - D * BX2
    s = -s if low else s
    return int(s.min()), int((s == 0).sum())


UF = np.array(FLOOR_U, dtype=np.int64)
UC = np.array(CEIL_U, dtype=np.int64)
TF = int(UF.sum()) + FLOOR_Z
TC = int(UC.sum()) + CEIL_Z
lf, tf = carries(UF, FLOOR_Z, FLOOR_D, True)
lc, tc = carries(UC, CEIL_Z, CEIL_D, False)
gate("floor certificate holds on every minimal piece", lf >= 0 and len(UF) == NO,
     "least slack {0}, equality on {1} of {2}".format(lf, tf, K2))
gate("floor certificate value", 48 * TF == 216 * FLOOR_D,
     "48 times {0} over {1} is exactly {2}".format(TF, FLOOR_D, fmt(216)))
gate("ceiling certificate holds on every minimal piece", lc >= 0 and len(UC) == NO,
     "least slack {0}, equality on {1} of {2}".format(lc, tc, K2))
gate("ceiling certificate value", 48 * TC == 256 * CEIL_D,
     "48 times {0} over {1} is exactly {2}".format(TC, CEIL_D, fmt(256)))
gate("the denominator law the two ends obey",
     2 * TF == 9 * FLOOR_D and 3 * TC == 16 * CEIL_D
     and divmod(FLOOR_D, 2)[1] == 0 and divmod(CEIL_D, 3)[1] == 0,
     "48 points per orbit, so 216 wants an even denominator and 256 a multiple of three")
gate("both certificates are met by a witness",
     COST["least-charge witness"] == 216 and COST["greatest-charge witness"] == 256,
     "the bracket over all minimal-volume corner dissections is exactly [216, 256]")
gate("the bracket sits strictly inside the counting bounds",
     48 * int(BX2.min()) < 216 and 256 < 48 * int(BX2.max()),
     "{0} below and {1} above".format(48 * int(BX2.min()), 48 * int(BX2.max())))

print("TOTAL: PASS={0} FAIL={1}".format(PASS, FAIL))
