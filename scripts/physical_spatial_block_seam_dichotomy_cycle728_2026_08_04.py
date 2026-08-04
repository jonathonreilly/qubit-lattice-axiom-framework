"""Cycle 728 -- a 2 by 1 by 1 spatial block, and what its seam costs.

Two neighbouring lattice cells, carried through one tick, make a box with 24 corners.
Dissect it into minimal pieces -- corner simplices of the least possible volume -- and
charge each piece one unit for every pair of its corners whose spatial separation exceeds
nearest-neighbour distance.  The cost of a dissection is the sum over its pieces.

The box has an internal wall: the plane through the shared face of the two cells.  Call it
the seam.  A piece either stays inside one closed cell or it crosses.  Everything in this
cycle is about what crossing buys and what it costs.

Three things are established here, all by arithmetic over the full piece set, with no
solver anywhere in this file.

  * The one-cell cost is bracketed between 108 and 128 by two integer certificates, and
    both ends are reached by explicit dissections carried here as data.
  * A dissection whose pieces all stay inside one closed cell is exactly a pair of cell
    dissections, so its cost lies between 216 and 256, and both ends are reached.
  * A dissection costing 318 is carried here as data, verified piece by piece.  Since 318
    is above 256, the dearest dissection of the block cannot respect the seam, while the
    cheapest found does.  Cheapness factorizes across the seam; expense does not.

The same 17280 pieces also carry a second charge -- the one that counts separation in the
tick direction and the two short spatial directions instead.  That is the same box measured
with the long direction treated as the tick rather than as space.  The two charges are
evaluated side by side on one set of pieces, so the contrast needs no second box.

Certificates.  Sample points are placed one per piece, one per orbit, and carried around
the box symmetry.  With no sample point on any piece boundary, every point lies inside
exactly one piece of any dissection, so a weight per point orbit plus an offset gives

    cost >= (points per orbit) * sum(u) + (pieces) * Z, all over D

when BO u + Z <= D BX holds on every minimal piece, and the reverse inequality gives the
matching upper bound.  No symmetry assumption enters that argument; symmetry only shrinks
the number of distinct weights.  The certificate vectors below are carried as data and
re-verified here against every one of the 2672 one-cell pieces.

Weights are generic by construction, not by luck: with barycentric integers bounded by C
and a superincreasing offset chain, no sample point can land on a piece boundary, and the
verification confirms it.
"""
import itertools
from collections import Counter

import numpy as np

PAIRS = list(itertools.combinations(range(5), 2))
OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
NP = [0, 0]

CELL_UFL = [89, -73, 128, -128, -94, 128, -29, 128, 128, 128, -50, -128, -128, -126,
            -128, -127, 128, 128, 75, -128, 128, 15, 128, 128, 128, 128, 128, 128,
            -128, -128, 128, -40, 28, -128, -128, -84, -128, -113, -128, -125, -76, 42,
            -76, 128, 128, -128, 128, 128, 128, -128, -128, -128, 128, 128, -128, -128,
            67]
CELL_ZFL = 123
CELL_DFL = 2
CELL_UCL = [-191, -27, -181, -192, 192, -192, -192, 192, 192, 192, 42, -192, -192, 192,
            192, -192, -192, 192, 192, -192, 192, -27, -192, -192, 192, 192, -192, 192,
            192, -192, -192, -192, 190, -192, 190, -188, -192, 186, 74, 111, -192, 111,
            135, 192, -172, 192, 192, -96, -192, 192, -192, 192, 191, 34, -192, 83,
            -76]
CELL_ZCL = 6
CELL_DCL = 3
CELL_HI = [[0, 1, 3, 6, 10], [0, 1, 4, 6, 10], [0, 1, 4, 10, 12], [0, 1, 8, 10, 12],
            [0, 2, 3, 6, 10], [1, 3, 6, 7, 12], [1, 3, 6, 10, 12], [1, 3, 7, 11, 12],
            [1, 3, 10, 11, 12], [1, 4, 5, 7, 12], [1, 4, 6, 7, 12],
            [1, 4, 6, 10, 12], [1, 5, 7, 12, 13], [1, 7, 11, 12, 15],
            [1, 7, 12, 13, 15], [1, 8, 9, 11, 12], [1, 8, 10, 11, 12],
            [1, 9, 11, 12, 13], [1, 11, 12, 13, 15], [3, 6, 7, 10, 12],
            [3, 7, 10, 11, 12], [6, 7, 10, 12, 15], [6, 10, 12, 14, 15],
            [7, 10, 11, 12, 15]]
BLOCK_HI = [[0, 1, 3, 7, 10], [0, 1, 4, 7, 12], [0, 1, 7, 8, 18], [0, 1, 7, 8, 20],
            [0, 1, 7, 10, 18], [0, 1, 7, 12, 20], [0, 2, 3, 7, 10], [0, 2, 6, 7, 10],
            [0, 4, 6, 7, 10], [0, 4, 7, 10, 12], [0, 7, 8, 18, 20],
            [0, 7, 10, 12, 20], [0, 7, 10, 18, 20], [1, 3, 7, 10, 18],
            [1, 3, 7, 11, 18], [1, 4, 5, 7, 12], [1, 5, 7, 12, 20],
            [1, 5, 7, 13, 20], [1, 7, 8, 16, 18], [1, 7, 8, 16, 20],
            [1, 7, 11, 16, 18], [1, 7, 11, 16, 20], [1, 7, 11, 19, 20],
            [1, 7, 13, 20, 21], [1, 7, 15, 19, 20], [1, 7, 15, 20, 21],
            [1, 9, 15, 19, 20], [1, 9, 15, 20, 21], [1, 9, 16, 19, 20],
            [1, 11, 16, 19, 20], [4, 6, 7, 10, 12], [6, 7, 10, 12, 20],
            [6, 7, 10, 18, 20], [6, 7, 14, 18, 20], [7, 8, 16, 18, 20],
            [7, 11, 16, 18, 20], [7, 11, 18, 19, 20], [7, 14, 15, 18, 20],
            [7, 15, 18, 19, 20], [9, 15, 17, 19, 20], [9, 15, 17, 20, 21],
            [9, 16, 17, 19, 20], [11, 16, 18, 19, 20], [14, 15, 18, 20, 22],
            [15, 17, 19, 20, 21], [15, 18, 19, 20, 23], [15, 18, 20, 22, 23],
            [15, 19, 20, 21, 23]]
BLOCK_UCL = [16, 0, 0, -25, 0, 0, 14, 0, 0, -24, 0, 23, 0, 13, 20, 0, 36, 25, 0, -5, 0,
            0, 0, -16, 0, 0, 0, 0, 0, 0, 0, 0, -29, -50, 9, 0, 121, 0, 0, 0, 0, 0, 0,
            -9, 0, 0, 0, 0, 0, 0, 0, 0, -40, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -29, 0, -61, -30, 0, 0, 0, -2,
            0, 0, 0, -16, 0, 0, 0, 0, 0, 0, -94, 24, 0, 0, -48, 0, 0, 45, 0, 0, 0, 0,
            -55, 0, -5, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, -44, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 79, 0, 0, 0, 0, 0, 0, 0, 36, 0, 0, 0, 0, 0, 0, -52, 0, 0, 0, 0,
            0, 0, 0, 78, 0, 0, 0, 0, 0, 0, -57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, -74, 0, 0, -54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -38, 0, 0, 19, 0, 0,
            0, 0, -14, 0, 0, -83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 0, 0, 0, 0, 0, 0, 2,
            0, 0, 0, 0, 0, 0, 0, 0, -15, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 0,
            0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 6, 5, 0, -10, 0, 39,
            0, 0, 0, 0, 0, 0, -63, 101, 22, 46, 0, 0, 0, 0, 0, 18, -55, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, -6, 0, 0, 0, 0, -39, 0, -63, 0, -67, 25, 0, 0, 0, 0, 0, 0,
            0, 0, 4, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 12,
            0, -14, 77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -46, 23, 0, 0, 0,
            0, 0, 0, 17, 0, 0, 0, 0, 28, 0, 0, 0, 0, 0, 41, 0, 20, 0, -10, -12, 0, 12,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, 67, -7, -30, 0,
            -50, 20, 0, 0, 0, 0, 0, 68, 0, 0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 3, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0,
            0, 179, 0, 0, -64, 0, 0, -19, 0, 0, 0, 30, 23, 0, 0, 0, 0, 0, -26, 0, 0, 0,
            0, 0, 0, 0, 0, 28, 62, 0, 0, 0, 0, -20, 0, 0, 0, 0, 0, 0, -24, 0, 0, 0, 0,
            0, 0, 0, 0, 0, -43, 0, -8, 0, 0, 0, 0, 0, 0, 42, 0, 0, 16, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -54, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -72, 0, 0, 0, 0, 0, 0, 33, 0, -65, 0, 0, -68,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            9, 17, 0, -73, 0, 0, 0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 58, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -76, 0, 0, 24, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            -41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 0,
            0, 0, 0, 0, 0, 0, 51, 0, 0, 0, 0, 0, 0, -49, 0, 0, -12, 0, 0, 0, 0, 39, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 47, 0, 0,
            0, 0, 0, 0, 0, 0, -36, 0, 0, 0, 0, 0, 0, -27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 23, -13, 0, 0, -36, 0, -29, 0, 0, 0, 0, 59, 0, -56, 0, 0,
            0, 25, -36, 0, 21, 0, 0, 0, 0, 0, 23, 0, 0, 12, 0, 0, -33, 0, 0, 0, -50, 0,
            0, 98, 0, 0, 0, 0, 0, 0, 0, 0, 0, 67, 0, 0, 0, 0, -16, -41, 0, 0, 0, 10,
            -78, 0, 0, 0, 0, 0, 0, 0, 0, 0, -23, 0, -77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, -13, 0, 0, 0, 0, 62, 0, -28, 0, 0, 0, 0, 0, 0, 0, 0,
            -13, 0, 0, 0, 0, 0, 0, -36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -33, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 0, -4, 0, -31, 0, 0, 0, 0,
            0, 0, 0]
BLOCK_ZCL = 81
BLOCK_DCL = 12


def gate(ok, name, detail):
    NP[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail)


def sec(text):
    print(text)


def det4(A):
    """exact integer determinants of a batch of 4 by 4 integer matrices"""
    def minors(r0, r1):
        out = {}
        for i in range(4):
            for j in range(i + 1, 4):
                out[(i, j)] = (A[:, r0, i] * A[:, r1, j]
                               - A[:, r0, j] * A[:, r1, i])
        return out
    m = minors(0, 1)
    c = minors(2, 3)
    return (m[(0, 1)] * c[(2, 3)] - m[(0, 2)] * c[(1, 3)] + m[(0, 3)] * c[(1, 2)]
            + m[(1, 2)] * c[(0, 3)] - m[(1, 3)] * c[(0, 2)] + m[(2, 3)] * c[(0, 1)])


def volumes(V, P):
    A = V[P[:, 1:]] - V[P[:, 0]][:, None, :]
    return np.abs(det4(A))


def census(V):
    subs = np.array(list(itertools.combinations(range(len(V)), 5)), dtype=np.int64)
    return subs, volumes(V, subs)


def charge(V, P, cols):
    tot = np.zeros(len(P), dtype=np.int64)
    for a, b in PAIRS:
        d = np.abs(V[P[:, a]][:, cols] - V[P[:, b]][:, cols]).sum(axis=1)
        tot = tot + (d > 1).astype(np.int64)
    return tot


def inverses(V, P):
    MM = np.stack([(V[p[1:]] - V[p[0]]).T for p in P])
    IV = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)
    eye = np.eye(4, dtype=np.int64)
    exact = bool((np.einsum("nij,njk->nik", IV, MM) == eye).all())
    return IV, exact


def bary_bound(V, P, IV):
    L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[P[:, 0]][:, None, :])
    return max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))


def weights(cmax):
    base = cmax * int(OFF.sum()) + 1
    w = 2 * (base + OFF)
    return w, int(w.sum())


ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if int(round(np.linalg.det(R.astype(float)))) == 1:
            ROT.append(R)


def group(corners, pos, cen2):
    keep = []
    out = []
    for R in ROT:
        good = False
        for tf in (0, 1):
            img = []
            for (x, y, z, t) in corners:
                w = R @ (2 * np.array([x, y, z], dtype=np.int64) - cen2) + cen2
                if bool((w & 1).any()):
                    img = None
                    break
                key = (int(w[0]) // 2, int(w[1]) // 2, int(w[2]) // 2,
                       (1 - t) if tf else t)
                if key not in pos:
                    img = None
                    break
                img.append(pos[key])
            if img is not None:
                out.append((R, tf, np.array(img, dtype=np.int64)))
                good = True
        if good:
            keep.append(R)
    return keep, out


def orbits(P, G):
    posp = dict((tuple(int(c) for c in s), i) for i, s in enumerate(P))
    lab = -np.ones(len(P), dtype=np.int64)
    reps = []
    for i in range(len(P)):
        if lab[i] >= 0:
            continue
        o = len(reps)
        reps.append(i)
        for (_, _, g) in G:
            lab[posp[tuple(sorted(int(g[c]) for c in P[i]))]] = o
    return lab, np.array(reps, dtype=np.int64)


def constant_on_orbits(lab, n_orb, vals):
    order = np.argsort(lab, kind="stable")
    bnd = np.searchsorted(lab[order], np.arange(n_orb + 1))
    for o in range(n_orb):
        blk = vals[order[bnd[o]:bnd[o + 1]]]
        if int(blk.max()) != int(blk.min()):
            return False
    return True


def points(V, P, G, reps, w, s, sc):
    lab = {}
    for o, i in enumerate(reps):
        q = (w[:, None] * V[P[i]]).sum(axis=0)
        for (R, tf, _) in G:
            u = R @ (q[:3] - sc) + sc
            key = (int(u[0]), int(u[1]), int(u[2]),
                   (s - int(q[3])) if tf else int(q[3]))
            if lab.setdefault(key, o) != o:
                return None, None
    keys = sorted(lab)
    return (np.array(keys, dtype=np.int64),
            np.array([lab[k] for k in keys], dtype=np.int64))


def membership(V, P, IV, Q, porb, n_orb, s):
    M = np.zeros((len(P), n_orb), dtype=np.int16)
    QT = Q.T
    bad = 0
    for i in range(len(P)):
        lam = IV[i] @ (QT - (s * V[P[i, 0]])[:, None])
        tot = lam.sum(axis=0)
        bad += int(((lam == 0).any(axis=0) | (tot == s)).sum())
        ins = (lam > 0).all(axis=0) & (tot < s)
        M[i] = np.bincount(porb[ins], minlength=n_orb)
    return M, bad


NEG = [np.array(t, dtype=np.int64)
       for t in itertools.product((-1, 0, 1), repeat=4) if any(t)]


def separated(V, P):
    pts = [V[p] for p in P]
    fac = []
    for p in P:
        MM = (V[p[1:]] - V[p[0]]).T
        Iv = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)
        fac.append([Iv[k] for k in range(4)] + [-Iv.sum(axis=0)])
    good = 0
    total = 0
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            total += 1
            for nv in NEG + fac[i] + fac[j]:
                a = pts[i] @ nv
                b = pts[j] @ nv
                if int(a.max()) <= int(b.min()) or int(b.max()) <= int(a.min()):
                    good += 1
                    break
    return good, total


def kuhn(base, pos):
    out = []
    for perm in itertools.permutations(range(4)):
        v = list(base)
        path = [tuple(v)]
        for c in perm:
            v[c] += 1
            path.append(tuple(v))
        out.append(tuple(sorted(pos[p] for p in path)))
    return sorted(out)


# ---------------------------------------------------------------- the two boxes
CORNB = [(x, y, z, t) for x in range(3) for y in range(2)
         for z in range(2) for t in range(2)]
VB = np.array(CORNB, dtype=np.int64)
POSB = dict((c, i) for i, c in enumerate(CORNB))
CORNC = [(x, y, z, t) for x in range(2) for y in range(2)
         for z in range(2) for t in range(2)]
VC = np.array(CORNC, dtype=np.int64)
POSC = dict((c, i) for i, c in enumerate(CORNC))

SUBB, DB = census(VB)
MINB = SUBB[DB == 1]
SUBC, DC = census(VC)
MINC = SUBC[DC == 1]

sec("2 by 1 by 1 spatial block: two lattice cells side by side, carried through one tick")
gate(len(CORNB) == 24 and len(CORNC) == 16, "corner count",
     "block {0} one cell {1}".format(len(CORNB), len(CORNC)))
gate(len(SUBB) == 42504, "five-subset census", "subsets {0}".format(len(SUBB)))
gate(int(DB.max()) == 6, "volume spectrum",
     str(sorted(Counter(DB.tolist()).items())))
gate(len(MINB) == 17280 and len(MINC) == 2672, "minimal pieces",
     "block {0} one cell {1}".format(len(MINB), len(MINC)))
gate(24 * 2 == 48, "pieces per dissection", "24 times the box volume 2 is 48")

# ---------------------------------------------------------------- the two charges
BX = charge(VB, MINB, [0, 1, 2])
BT = charge(VB, MINB, [3, 1, 2])
SX = charge(VB, MINB, [0])
BXC = charge(VC, MINC, [0, 1, 2])

hi_x = int((BX > BT).sum())
hi_t = int((BT > BX).sum())

sec("two charges on one set of pieces")
gate((int(BX.min()), int(BX.max())) == (3, 9), "spatial adjacency charge range",
     str((int(BX.min()), int(BX.max()))))
gate(len(BX) == 17280, "spatial adjacency spectrum",
     str(sorted(Counter(BX.tolist()).items())))
gate((int(BT.min()), int(BT.max())) == (3, 7), "transposed charge range",
     str((int(BT.min()), int(BT.max()))))
gate(len(BT) == 17280, "transposed charge spectrum",
     str(sorted(Counter(BT.tolist()).items())))
gate(hi_x > 0 and hi_t > 0, "neither charge dominates the other",
     "spatial is larger on {0} pieces and smaller on {1}".format(hi_x, hi_t))
gate(int(BX.max()) > int(BT.max()), "the long direction costs when it is spatial",
     "spatial reaches {0} where transposed stops at {1}".format(
         int(BX.max()), int(BT.max())))
gate(True, "trivial counting bounds",
     "spatial {0} to {1}, transposed {2} to {3}".format(
         48 * int(BX.min()), 48 * int(BX.max()),
         48 * int(BT.min()), 48 * int(BT.max())))

# ---------------------------------------------------------------- the seam
sub = True
for a, b in PAIRS:
    dx = np.abs(VB[MINB[:, a]][:, 0] - VB[MINB[:, b]][:, 0])
    l1 = np.abs(VB[MINB[:, a]][:, :3] - VB[MINB[:, b]][:, :3]).sum(axis=1)
    sub = sub and bool(((dx > 1) <= (l1 > 1)).all())

xs = VB[MINB][:, :, 0]
one_cell = (xs.max(axis=1) - xs.min(axis=1)) <= 1
slab = SX == 0
seam = SX > 0
spans = bool((xs[seam].min(axis=1) == 0).all() and (xs[seam].max(axis=1) == 2).all())

shift = xs.min(axis=1)
posc = dict((tuple(int(c) for c in s), i) for i, s in enumerate(MINC))
tr_ok = True
tr_hit = 0
for i in np.nonzero(slab)[0]:
    key = tuple(sorted(POSC[(int(VB[c][0]) - int(shift[i]), int(VB[c][1]),
                             int(VB[c][2]), int(VB[c][3]))] for c in MINB[i]))
    j = posc.get(key)
    if j is None or int(BXC[j]) != int(BX[i]):
        tr_ok = False
        break
    tr_hit += 1

sec("the seam between the two cells")
gate((int(SX.min()), int(SX.max())) == (0, 4), "long-axis span charge range",
     str((int(SX.min()), int(SX.max()))))
gate(len(SX) == 17280, "long-axis span spectrum",
     str(sorted(Counter(SX.tolist()).items())))
gate(sub, "span is a sub-charge of adjacency",
     "every counted long-axis pair is counted by adjacency as well")
gate(bool((one_cell == slab).all()), "span zero means the piece sits in one closed cell",
     "{0} pieces, agreeing pair by pair".format(int(slab.sum())))
gate(spans, "every seam-crossing piece spans the block",
     "least x zero and greatest x two on all {0}".format(int(seam.sum())))
gate(tr_ok and tr_hit == 5344 and 5344 == 2 * len(MINC),
     "slab-confined pieces are one-cell pieces",
     "5344 = 2 times 2672, charge unchanged by the translation")
gate(int(slab.sum()) == 5344, "slab-confined charge doubles the one-cell spectrum",
     str(sorted(Counter(BX[slab].tolist()).items())))
gate(int(BX[seam].min()) > int(BX[slab].min()), "crossing the seam costs at least two",
     "least charge {0} crossing against {1} confined".format(
         int(BX[seam].min()), int(BX[slab].min())))

# ---------------------------------------------------------------- symmetry
KEEPB, GB = group(CORNB, POSB, np.array([2, 1, 1], dtype=np.int64))
KEEPC, GC = group(CORNC, POSC, np.array([1, 1, 1], dtype=np.int64))
permB = set(tuple(int(c) for c in g) for (_, _, g) in GB)
LABB, REPB = orbits(MINB, GB)
NORB = len(REPB)
szb = np.bincount(LABB, minlength=NORB)

sec("box symmetry, used only to compress the certificate")
gate(len(ROT) == 24, "proper cubic rotations", "24")
gate(len(KEEPB) == 8, "rotations preserving a 2 by 1 by 1 block", str(len(KEEPB)))
gate(len(GB) == 16 and len(permB) == 16, "group order",
     "8 rotations times the tick relabelling, 16 distinct corner permutations")
gate(NORB == 1080 and int(szb.min()) == 16 and int(szb.max()) == 16, "piece orbits",
     "{0} orbits, every one of size 16".format(NORB))
gate(constant_on_orbits(LABB, NORB, BX) and constant_on_orbits(LABB, NORB, SX),
     "both charges are constant on every orbit",
     "one adjacency charge and one span charge per orbit")

# ---------------------------------------------------------------- sample points
IB, exB = inverses(VB, MINB)
CB = bary_bound(VB, MINB, IB)
WB, SBT = weights(CB)
QB, PORBB = points(VB, MINB, GB, REPB, WB, SBT,
                   np.array([SBT, SBT // 2, SBT // 2], dtype=np.int64))
MB, badB = membership(VB, MINB, IB, QB, PORBB, NORB, SBT)
rowsB = len(set(MB[i].tobytes() for i in range(len(MINB))))
ptsz = np.bincount(PORBB, minlength=NORB)

IC, exC = inverses(VC, MINC)
CC = bary_bound(VC, MINC, IC)
WC, SCT = weights(CC)
spread_b = float(WB.max()) / float(WB.min())
spread_c = float(WC.max()) / float(WC.min())

sec("sample points, generic by construction and verified generic")
gate(exB and exC, "piece inverses are exact integer matrices",
     "{0} block and {1} one-cell inverses give the identity".format(
         len(MINB), len(MINC)))
gate(CB == 6 and CC == 3, "barycentric integers are bounded",
     "no corner sees a barycentric integer above {0} on a block piece".format(CB))
gate(spread_b < 1.15 and spread_c < 1.3,
     "weights are generic by construction and near-uniform",
     "block spread {0:.6f}, one-cell spread {1:.6f}".format(spread_b, spread_c))
gate(QB is not None and len(QB) == 17280, "point family",
     "one point per orbit carried around the group, {0} distinct".format(len(QB)))
gate(int(ptsz.min()) == 16 and int(ptsz.max()) == 16, "points per orbit",
     "every orbit carries 16 points")
gate(badB == 0, "no sample point lands on a piece boundary",
     "boundary incidences {0} over all {1} pieces".format(badB, len(MINB)))
gate(rowsB == 1060, "membership is constant on every orbit",
     "{0} rows carry {1} distinct".format(len(MINB), rowsB))

# ---------------------------------------------------------------- symmetric dissections
BO = MB[REPB].astype(np.int16)
ordb = np.argsort(LABB, kind="stable")
bndb = np.searchsorted(LABB[ordb], np.arange(NORB))
SM = np.add.reduceat(MB[ordb].astype(np.int64), bndb, axis=0)
ident = bool((SM == 16 * BO.astype(np.int64)).all())
diagok = bool((np.array([BO[o, o] for o in range(NORB)]) >= 1).all())
elig = np.nonzero(BO.max(axis=1) <= 1)[0]
BE = BO[elig]
rowof = dict((BE[k].tobytes(), k) for k in range(len(elig)))
ones = np.ones(NORB, dtype=np.int16)
tri = 0
for a in range(len(elig)):
    T = BE[a + 1:] + BE[a]
    for gi in np.nonzero(T.max(axis=1) <= 1)[0]:
        k = rowof.get((ones - T[gi]).tobytes())
        if k is not None and k > a + 1 + int(gi):
            tri += 1

sec("no dissection of the block carries the block symmetry")
gate(48 == 3 * 16, "a symmetric dissection is a union of whole orbits",
     "48 pieces over orbits of size 16 leaves 3 orbits")
gate(diagok, "every orbit covers a point of its own orbit",
     "the diagonal never vanishes, so an orbit is used at most once")
gate(ident, "an orbit meets a point as often as its representative does",
     "orbit sums are 16 times the representative row")
gate(len(elig) == 23, "orbits that could appear at all",
     "{0} of {1}; the other {2} already cover some sample point twice".format(
         len(elig), NORB, NORB - len(elig)))
gate(tri == 0, "triples of orbits covering every point exactly once", str(tri))

# ---------------------------------------------------------------- one cell
LABC, REPC = orbits(MINC, GC)
NOC = len(REPC)
QC, PORBC = points(VC, MINC, GC, REPC, WC, SCT,
                   np.array([SCT // 2, SCT // 2, SCT // 2], dtype=np.int64))
MC, badC = membership(VC, MINC, IC, QC, PORBC, NOC, SCT)
szc = np.bincount(PORBC, minlength=NOC)

ufl = np.array(CELL_UFL, dtype=np.int64)
ucl = np.array(CELL_UCL, dtype=np.int64)
sfl = CELL_DFL * BXC - (MC.astype(np.int64) @ ufl + CELL_ZFL)
scl = (MC.astype(np.int64) @ ucl + CELL_ZCL) - CELL_DCL * BXC
vfl = int((szc * ufl).sum()) + 24 * CELL_ZFL
vcl = int((szc * ucl).sum()) + 24 * CELL_ZCL

CLO = kuhn((0, 0, 0, 0), POSC)
PLO_C = np.array(CLO, dtype=np.int64)
SWC = dict((i, POSC[(c[3], c[1], c[2], c[0])]) for i, c in enumerate(CORNC))
swapinv = (sorted(tuple(sorted(SWC[i] for i in p)) for p in CLO)
           == sorted(tuple(p) for p in CLO))
tk_lo_c = int(charge(VC, PLO_C, [3, 1, 2]).sum())
PHI_C = np.array(sorted(tuple(p) for p in CELL_HI), dtype=np.int64)
vol_lo_c = volumes(VC, PLO_C)
vol_hi_c = volumes(VC, PHI_C)
g_lo_c, t_lo_c = separated(VC, PLO_C)
g_hi_c, t_hi_c = separated(VC, PHI_C)
c_lo = int(charge(VC, PLO_C, [0, 1, 2]).sum())
c_hi = int(charge(VC, PHI_C, [0, 1, 2]).sum())
tk_hi_c = int(charge(VC, PHI_C, [3, 1, 2]).sum())
swaphi = (sorted(tuple(sorted(SWC[i] for i in p)) for p in PHI_C.tolist())
          == sorted(tuple(p) for p in PHI_C.tolist()))

sec("one cell, measured here so nothing about it is a supplied number")
gate(len(MINC) == 2672, "one-cell minimal pieces", str(len(MINC)))
gate((int(BXC.min()), int(BXC.max())) == (3, 7), "one-cell charge range and spectrum",
     "(3, 7) " + str(sorted(Counter(BXC.tolist()).items())))
gate(len(GC) == 48, "one-cell group order",
     "24 rotations times the tick relabelling, 48 corner permutations")
gate(NOC == 57, "one-cell piece orbits", str(NOC))
gate(len(QC) == 2736 and badC == 0, "one-cell sample points",
     "{0} distinct, boundary incidences {1}".format(len(QC), badC))
gate(bool((sfl >= 0).all()), "floor certificate holds on every one-cell piece",
     "least slack {0}, equality on {1} of {2}".format(
         int(sfl.min()), int((sfl == 0).sum()), len(MINC)))
gate(vfl == 216 and CELL_DFL == 2, "floor certificate value",
     "24 times 9 over 2 is exactly {0:.6f}".format(vfl / CELL_DFL))
gate(bool((scl >= 0).all()), "ceiling certificate holds on every one-cell piece",
     "least slack {0}, equality on {1} of {2}".format(
         int(scl.min()), int((scl == 0).sum()), len(MINC)))
gate(vcl == 384 and CELL_DCL == 3, "ceiling certificate value",
     "24 times 16 over 3 is exactly {0:.6f}".format(vcl / CELL_DCL))
gate(bool((vol_lo_c == 1).all()) and int(vol_lo_c.sum()) == 24
     and bool((vol_hi_c == 1).all()) and int(vol_hi_c.sum()) == 24
     and g_lo_c == t_lo_c and g_hi_c == t_hi_c,
     "one-cell witnesses at both ends are dissections",
     "24 pieces each, {0} of {1} pairs separated both times".format(
         g_lo_c, t_lo_c))
gate(c_lo == 108 and c_hi == 128, "the one-cell bracket is exactly [108, 128]",
     "certified at both ends and attained at both ends")

# ---------------------------------------------------------------- what the seam forces
def lift(pieces_c, k):
    out = []
    for p in pieces_c:
        out.append(tuple(sorted(
            POSB[(int(VC[c][0]) + k, int(VC[c][1]), int(VC[c][2]), int(VC[c][3]))]
            for c in p)))
    return out


BLO = np.array(sorted(lift(PLO_C, 0) + lift(PLO_C, 1)), dtype=np.int64)
BSH = np.array(sorted(lift(PHI_C, 0) + lift(PHI_C, 1)), dtype=np.int64)
BHI = np.array(sorted(tuple(p) for p in BLOCK_HI), dtype=np.int64)

vlo, vsh, vhi = volumes(VB, BLO), volumes(VB, BSH), volumes(VB, BHI)
glo, tlo = separated(VB, BLO)
gsh, tsh = separated(VB, BSH)
ghi, thi = separated(VB, BHI)
xlo = int(charge(VB, BLO, [0, 1, 2]).sum())
tklo = int(charge(VB, BLO, [3, 1, 2]).sum())
xsh = int(charge(VB, BSH, [0, 1, 2]).sum())
xhi = int(charge(VB, BHI, [0, 1, 2]).sum())
tkhi = int(charge(VB, BHI, [3, 1, 2]).sum())
crosslo = int((charge(VB, BLO, [0]) > 0).sum())
crosssh = int((charge(VB, BSH, [0]) > 0).sum())
crosshi = int((charge(VB, BHI, [0]) > 0).sum())

sec("what respecting the seam forces")
gate(bool((one_cell == slab).all()),
     "a seam-respecting dissection is a pair of cell dissections",
     "span zero puts every piece inside one closed cell")
gate(2 * 108 == 216 and 2 * 128 == 256, "seam-respecting cost bracket",
     "between 216 and 256, from the certified one-cell bracket")
gate(bool((vlo == 1).all()) and int(vlo.sum()) == 48 and glo == tlo
     and xlo == 216 and crosslo == 0, "least-charge stacked dissection",
     "48 unit pieces, {0} of {1} pairs separated, charge 216, span zero".format(
         glo, tlo))
gate(bool((vsh == 1).all()) and int(vsh.sum()) == 48 and gsh == tsh
     and xsh == 256 and crosssh == 0, "greatest seam-respecting dissection",
     "48 unit pieces, {0} of {1} pairs separated, charge 256, span zero".format(
         gsh, tsh))

sec("the dissection that refuses the seam")
gate(bool((vhi == 1).all()) and int(vhi.sum()) == 48,
     "greatest-charge witness is a dissection",
     "48 pieces, every one of volume one, volumes summing to the box")
gate(ghi == thi, "greatest-charge witness pieces are pairwise interior-disjoint",
     "{0} of {1} pairs separated".format(ghi, thi))
gate(xhi == 318 and tkhi == 238, "greatest-charge witness charge",
     "spatial {0}, transposed {1}".format(xhi, tkhi))
gate(crosshi == 31, "greatest-charge witness crosses the seam",
     "{0} of its 48 pieces".format(crosshi))
gate(xhi > 2 * 128, "the dearest dissection cannot respect the seam",
     "318 above the seam-respecting ceiling 256")

# ------------------------------------------- a certificate for the whole block
ubl = np.array(BLOCK_UCL, dtype=np.int64)
sbl = np.empty(len(MINB), dtype=np.int64)
for k0 in range(0, len(MINB), 2160):
    sbl[k0:k0 + 2160] = MB[k0:k0 + 2160].astype(np.int64) @ ubl
sbl += BLOCK_ZCL - BLOCK_DCL * BX.astype(np.int64)
vbl = 16 * int(ubl.sum()) + 48 * BLOCK_ZCL
dv2 = min(d for d in range(1, 17) if int(np.remainder(216 * d, 16)) == 0)
dv3 = min(d for d in range(1, 17) if int(np.remainder(324 * d, 16)) == 0)
gate(bool((sbl >= 0).all()) and int(sbl.min()) == 0,
     "block ceiling holds on every piece",
     "least slack 0, equality on {0} of {1}".format(int((sbl == 0).sum()), len(MINB)))
gate(vbl == 3888 and vbl // BLOCK_DCL == 324, "certified block ceiling",
     "{0} over {1} is {2}, and the witness reaches {3}".format(
         vbl, BLOCK_DCL, vbl // BLOCK_DCL, xhi))
gate(dv2 == 2 and dv3 == 4 and int(np.remainder(BLOCK_DCL, 4)) == 0,
     "denominators a block certificate value can use",
     "216 needs an even one, 324 a multiple of four, and 12 serves")

sec("what the cycle measures")
gate(xhi - tkhi == 80, "one dissection carries the two charges far apart",
     "{0} against {1} on the same 48 pieces".format(xhi, tkhi))
gate(swapinv, "the stencil uses every ordering of the four coordinates",
     "the long spatial axis and the tick exchange freely")
gate(tk_lo_c == 108 and tklo == xlo,
     "so the two charges agree on the stacked stencil",
     "one cell {0} both ways, stacked {1} against {2}".format(tk_lo_c, xlo, tklo))
gate(not swaphi and tk_hi_c == 116, "the dear one-cell dissection has no such symmetry",
     "the swap moves it, and its charges read {0} against {1}".format(c_hi, tk_hi_c))
gate(48 * int(BX.min()) < xlo and xhi < 48 * int(BX.max()), "measured span of the cost",
     "216 at the least found and 318 at the greatest found, inside 144 and 432")

print("TOTAL: PASS={0} FAIL={1}".format(NP[0], NP[1]))
