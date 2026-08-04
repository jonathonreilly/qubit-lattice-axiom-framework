"""Cycle 731 of the emergent-geometry lane: the cost of a cell dissection counts its pieces.

The object is one lattice cell carried through a tick -- a 4-cube with 16 corners and
four-volume 1, cut into minimal simplices of volume 1/24, so every minimal-volume dissection
of it uses exactly 24 pieces.  The adjacency charge of a piece counts the corner pairs whose
spatial separation is more than one lattice step, and the cost of a dissection is the total
over its 24 pieces.  Cycle 725 measured that cost interval as 108 to 128, and cycle 730 made
minimal cost a LOCAL condition: given a certificate of zero gap, a dissection is cheapest
exactly when each of its pieces sits on a tight row.

This cycle turns that bound into an identity.  An integer weight u_o per orbit of sample
points, an integer Z, and a positive integer denominator D give a floor certificate when

    sum_o M[p][o] u_o + Z  <=  D * adjacency(p)

holds for every minimal piece p, and the certificate has zero gap when its value MO.u + 24 Z
is exactly 108 D.  Per-piece slack is then exact accounting: over any dissection of cost C
the slacks sum to D (C - 108).

The floor certificate carried here has slack in {0, D} on ALL 2672 pieces.  It is the
INDICATOR of a fixed set of 1792 pieces in 38 orbits, so the accounting collapses to

    cost(dissection)  =  108  +  #(its pieces outside that set)

for every 24-piece dissection of the cell.  Cost is a counting function of local membership,
with no reference to how the pieces fit together.  Since cost never passes 128, no dissection
has more than 20 pieces outside the set, so every dissection of the cell carries at least
4 pieces inside it, and a dissection of cost 128 carries exactly 4.

The set is pinned from both sides with no search over dissections.  Any piece of a cost-108
dissection is tight, because the slacks are nonnegative and sum to zero; and each of the 38
orbits is exhibited inside a cost-108 dissection, six of which already realize all 38.

The other end behaves differently, and an exact integer identity says why.  Five orbits carry
a dependency among the rows of the incidence matrix,

    3 M[3] + M[17] - M[1] - M[15] - 2 M[27] = 0,

their five coefficients sum to zero, and the same combination of their adjacency charges is
-2.  So for EVERY (u, Z, D) whatsoever the ceiling slacks obey

    3 s(3) + s(17) - s(1) - s(15) - 2 s(27)  =  2 D.

Orbits 1, 15, 17 and 27 each occur in a cost-128 dissection exhibited here, so a zero-gap
ceiling certificate is tight on all four, leaving 3 s(3) = 2 D.  That forces 3 to divide D,
so 3 is the least denominator carrying a zero-gap ceiling certificate and one at D = 3 is
exhibited; and it leaves s(3) equal to neither 0 nor D, so the ceiling carries no indicator
certificate at all.  The floor pattern (0,1,0,1,1) on those same five orbits solves the same
relation in 0/1, which is why the floor does carry one.

Locally the set is partly readable off the charge alone: charge at most 4 puts a piece inside
it and charge 7 puts a piece outside, deciding 752 of the 2672 pieces, while the 1920 pieces
at charge 5 or 6 split both ways.  None of the local invariants swept here separates the 38
orbits from the other 19 on its own.

No solver appears in this artifact.  The certificates are literal integers checked in integer
arithmetic over every piece; the dissections are found by deterministic backtracking cover
search and proved to be dissections by volume, by pairwise disjointness through exhibited
integer normals, and by containment of every sample point.
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


def irank(rows):
    """rank over the rationals, by fraction-free elimination over the integers"""
    A = [list(r) for r in rows]
    n, m, piv = len(A), len(A[0]), 0
    for c in range(m):
        p = next((r for r in range(piv, n) if A[r][c]), None)
        if p is None:
            continue
        A[piv], A[p] = A[p], A[piv]
        pv = A[piv][c]
        for r in range(piv + 1, n):
            if A[r][c]:
                f = A[r][c]
                A[r] = [pv * x - f * y for x, y in zip(A[r], A[piv])]
                g = 0
                for x in A[r]:
                    g = math.gcd(g, abs(x))
                if g > 1:
                    A[r] = [x // g for x in A[r]]
        piv += 1
        if piv == n:
            break
    return piv


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


sec("the cell and its minimal pieces")

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
spec = sorted((int(a), int(b)) for a, b in zip(*np.unique(CX, return_counts=True)))
gate(len(SUB) == 4368 and NPIECE == 2672,
     "cell.pieces",
     "{0} five-subsets of the 16 corners, {1} of volume 1/24".format(len(SUB), NPIECE))
vspec = sorted(set(int(t) for t in VOL))
gate(vspec == [0, 1, 2, 3] and int(np.min(VOL[VOL > 0])) == 1,
     "cell.volumes",
     "scaled volumes of the five-subsets are {0}, least nonzero 1".format(vspec))
gate(spec == [(3, 64), (4, 384), (5, 1152), (6, 768), (7, 304)],
     "cell.charge", "adjacency charge spectrum {0}".format(spec))

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
     "sym.group", "{0} proper rotations kept, {1} elements with the tick flip".format(
         len(KEEP), len(G)))

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
     "sym.constant", "adjacency charge is constant on every orbit")

sec("generic sample points, none on a piece boundary")

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
keys = sorted(lab)
Q = np.array(keys, dtype=np.int64)
PORB = np.array([lab[k] for k in keys], dtype=np.int64)
NQ = len(Q)

M = np.zeros((NPIECE, NORB), dtype=np.int16)
QT = Q.T
face = 0
MASK = []
for i in range(NPIECE):
    lam = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lam.sum(axis=0)
    face += int(((lam == 0).any(axis=0) | (tot == SB)).sum())
    ins = (lam > 0).all(axis=0) & (tot < SB)
    M[i] = np.bincount(PORB[ins], minlength=NORB)
    b = 0
    for j in np.flatnonzero(ins):
        b |= 1 << int(j)
    MASK.append(b)
MI = M.astype(np.int64)
MO = np.bincount(PORB, minlength=NORB).astype(np.int64)
gate(NQ == 2736 and coll == 0 and face == 0,
     "pts.generic", "{0} sample points, no collision, {1} on any piece boundary".format(
         NQ, face))
gate(not bool((MO == SZ).all()),
     "pts.weighted", "points per orbit is not the orbit size, so it carries the objective")

sec("an indicator certificate at the floor")

FLOOR_U = [(0, -36), (4, 144), (19, 64), (20, -36), (34, 216), (35, 135),
           (44, -216), (45, 36), (51, -72), (52, 163), (53, -172), (54, -118)]
FLOOR_D, FLOOR_Z = 216, 756
CEIL_U = [(0, 3), (4, 3), (20, 3), (22, -5), (34, 4), (35, -31), (36, 31),
          (37, 6), (43, 2), (44, -4), (45, -1), (51, -1), (52, -2)]
CEIL_D, CEIL_Z = 3, 0


def build(dat):
    u = np.zeros(NORB, dtype=np.int64)
    for j, w in dat:
        u[j] = w
    return u


def slacks(u, Z, D, upper):
    s = (MI @ u + Z) - D * CX
    return s if upper else -s


def value(u, Z):
    return int((MO * u).sum()) + 24 * Z


FU, CU = build(FLOOR_U), build(CEIL_U)
FS = slacks(FU, FLOOR_Z, FLOOR_D, False)
FV = value(FU, FLOOR_Z)
gate(bool((FS >= 0).all()),
     "floor.valid", "floor rows hold on all {0} pieces at D {1}, Z {2}".format(
         NPIECE, FLOOR_D, FLOOR_Z))
gate(FV == 108 * FLOOR_D,
     "floor.zerogap", "value {0} is exactly 108 times {1}, so the gap is zero".format(
         FV, FLOOR_D))
fspec = sorted(set(int(t) for t in FS))
gate(fspec == [0, FLOOR_D],
     "floor.indicator", "floor slack spectrum over all pieces is {0}, that is 0 and D".format(
         fspec))
SUP = np.flatnonzero(FS == 0)
SUPO = sorted(set(int(LAB[i]) for i in SUP))
OFFS = np.ones(NPIECE, dtype=np.int64)
OFFS[SUP] = 0
gate(len(SUP) == 1792 and len(SUPO) == 38,
     "floor.support", "the indicator picks out {0} pieces in {1} orbits".format(
         len(SUP), len(SUPO)))

surv = 0
for j in range(NORB):
    for d in (1, -1):
        u2 = FU.copy()
        u2[j] += d
        if bool((slacks(u2, FLOOR_Z, FLOOR_D, False) >= 0).all()) and \
                value(u2, FLOOR_Z) == 108 * FLOOR_D:
            surv += 1
for d in (1, -1):
    if bool((slacks(FU, FLOOR_Z + d, FLOOR_D, False) >= 0).all()) and \
            value(FU, FLOOR_Z + d) == 108 * FLOOR_D:
        surv += 1
gate(surv == 0,
     "floor.corner", "{0} of {1} single-step moves in u or Z stay valid at zero gap".format(
         surv, 2 * NORB + 2))

sec("the cost of a dissection counts its pieces outside the support")

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
    return len(idx) == 24 and g == t and cov == ALLQ


def search(pool, forced=()):
    by_pt = [[] for _ in range(NQ)]
    for i in pool:
        by_pt[(MASK[i] & -MASK[i]).bit_length() - 1].append(int(i))
    out = []
    cov0, cur0 = 0, [int(i) for i in forced]
    for i in forced:
        cov0 |= MASK[i]

    def rec(cov, cur):
        if cov == ALLQ:
            out.append(list(cur))
            return True
        j = ~cov & ALLQ
        j = (j & -j).bit_length() - 1
        for i in by_pt[j]:
            if MASK[i] & cov:
                continue
            cur.append(i)
            if rec(cov | MASK[i], cur):
                return True
            cur.pop()
        return False

    rec(cov0, cur0)
    return sorted(out[0]) if out else None


CS = slacks(CU, CEIL_Z, CEIL_D, True)
CTI = [int(i) for i in np.flatnonzero(CS == 0)]
STEN = set()
for perm in itertools.permutations(range(4)):
    v, path = [0, 0, 0, 0], [(0, 0, 0, 0)]
    for c in perm:
        v[c] += 1
        path.append(tuple(v))
    STEN.add(tuple(sorted(POS[p] for p in path)))
DIS = {"monotone stencil": sorted(posp[t] for t in sorted(STEN)),
       "any piece": search(list(range(NPIECE))),
       "inside the support": search([int(i) for i in SUP]),
       "on the ceiling rows": search(CTI)}
NAMES = ["monotone stencil", "any piece", "inside the support", "on the ceiling rows"]
COST = dict((k, int(CX[np.array(v)].sum())) for k, v in DIS.items())
OFFC = dict((k, int(OFFS[np.array(v)].sum())) for k, v in DIS.items())
gate(all(is_dissection(DIS[k]) for k in NAMES),
     "cost.dissect", "all four exhibited covers are dissections: 24 pieces, disjoint, "
                     "every sample point covered")
gate([COST[k] for k in NAMES] == [108, 114, 108, 128],
     "cost.spread", "their costs are {0}".format([COST[k] for k in NAMES]))
gate(all(COST[k] == 108 + OFFC[k] for k in NAMES),
     "cost.identity", "cost equals 108 plus the pieces outside the support: {0}".format(
         [(COST[k], OFFC[k]) for k in NAMES]))
gate(all(int(FS[np.array(DIS[k])].sum()) == FLOOR_D * (COST[k] - 108) for k in NAMES),
     "cost.slack", "floor slack over a dissection is D times the excess over 108")
gate(all(bool((MI[np.array(DIS[k])].sum(axis=0) == MO).all()) for k in NAMES),
     "cost.census", "the rows of a dissection sum to the point census, which is what makes "
                    "the slacks add to D times the cost less the value")
gate(all(int((MI[np.array(DIS[k])] @ FU).sum()) + 24 * FLOOR_Z == FV for k in NAMES),
     "cost.value", "summing the certificate over any dissection returns the value {0}, "
                   "a second route to it".format(FV))
few = min(24 - OFFC[k] for k in NAMES)
gate(few == 4 and 24 - (128 - 108) == few,
     "cost.floorpieces", "the ceiling caps cost at 128, so at most 20 pieces lie outside "
                         "and every dissection holds at least 4 inside; fewest here {0}".format(few))

occ = sorted(set(int(LAB[i]) for k in NAMES for i in DIS[k]))
kept = 0
for o in occ:
    flip = OFFS.copy()
    flip[LAB == o] = 1 - flip[LAB == o]
    if all(COST[k] == 108 + int(flip[np.array(DIS[k])].sum()) for k in NAMES):
        kept += 1
gate(kept == 0,
     "cost.discriminate", "{0} of {1} orbits occurring in these dissections can be moved "
                          "across the support and keep the identity".format(kept, len(occ)))

sec("the support is exactly the tight set, pinned from both sides")

gate(all(bool((FS[np.array(DIS[k])] == 0).all()) for k in NAMES if COST[k] == 108),
     "tight.forced", "in a cost-108 dissection the slacks are nonnegative and sum to zero, "
                     "so every piece is tight")
comp = []
for o in SUPO:
    d = search([int(i) for i in SUP], forced=[int(REPS[o])])
    comp.append((o, d))
gate(all(d is not None and int(CX[np.array(d)].sum()) == 108 and
         bool((FS[np.array(d)] == 0).all()) for o, d in comp),
     "tight.reached", "each of the {0} support orbits sits in a cost-108 dissection whose "
                      "pieces all lie in the support".format(len(SUPO)))

bits = []
for o, d in comp:
    b = 0
    for i in d:
        b |= 1 << SUPO.index(int(LAB[i]))
    bits.append(b)
FULL = (1 << len(SUPO)) - 1
SEEDS = [12, 13, 45, 50, 53, 56]
b6 = 0
for s in SEEDS:
    b6 |= bits[SUPO.index(s)]
gate(b6 == FULL and all(s in SUPO for s in SEEDS),
     "tight.family", "six of them, seeded at orbits {0}, already realize all {1}".format(
         SEEDS, len(SUPO)))
five = any(bits[a] | bits[b] | bits[c] | bits[d] | bits[e] == FULL
           for a, b, c, d, e in itertools.combinations(range(len(bits)), 5))
gate(not five,
     "tight.minimal", "a complete sweep of all {0} five-subsets of these {1} shows none "
                      "covers all {1}".format(
                          len(SUPO) * (len(SUPO) - 1) * (len(SUPO) - 2) *
                          (len(SUPO) - 3) * (len(SUPO) - 4) // 120, len(SUPO)))

sec("the ceiling admits no indicator, by an exact integer identity")

CV = value(CU, CEIL_Z)
gate(bool((CS >= 0).all()) and CV == 128 * CEIL_D,
     "ceil.valid", "ceiling rows hold on all pieces at D {0}, value {1} is 128 times "
                   "{0}".format(CEIL_D, CV))
cspec = sorted(set(int(t) for t in CS))
gate(cspec != [0, CEIL_D] and len(np.flatnonzero(CS == 0)) == 944,
     "ceil.notind", "its slack spectrum is {0}, not 0 and D; tight on {1} pieces in {2} "
                    "orbits".format(cspec, int((CS == 0).sum()),
                                    len(set(int(LAB[i]) for i in CTI))))

COEF = [(3, 3), (17, 1), (1, -1), (15, -1), (27, -2)]
MR, CXR = MI[REPS], CX[REPS]
dep = np.zeros(NORB, dtype=np.int64)
for o, c in COEF:
    dep = dep + c * MR[o]
csum = sum(c for _, c in COEF)
xsum = sum(c * int(CXR[o]) for o, c in COEF)
gate(bool((dep == 0).all()),
     "id.rows", "the five orbit rows are integer dependent with coefficients {0}, "
                "largest residual {1}".format([c for _, c in COEF], int(np.abs(dep).max())))
gate(csum == 0 and xsum == -2,
     "id.charges", "those coefficients sum to {0} and combine the charges {1} to {2}".format(
         csum, [int(CXR[o]) for o, _ in COEF], xsum))

RW = [[int(x) for x in MR[k]] for k in range(NORB)]
rk = irank(RW)
aug = irank([RW[k] + [1] for k in range(NORB)])
gate(rk == 13 and aug == rk,
     "id.rank", "the {0} orbit rows span {1} dimensions, so their dependencies form a {2}-"
                "dimensional space and this is one of many; adjoining the constant column "
                "does not raise the span, so a weighting giving every piece orbit the same "
                "total exists and every dependency has coefficient sum zero".format(
                    NORB, rk, NORB - rk))
sub = irank([RW[o] for o, _ in COEF])
four = max(4 - irank([RW[o] for j, (o, _) in enumerate(COEF) if j != k])
           for k in range(len(COEF)))
gate(sub == len(COEF) - 1 and four == 0,
     "id.support", "its support is minimal: on these five orbits the dependency is unique "
                   "up to scale, and no four of them carry one")


def prim(r):
    """the primitive representative of a row, up to sign and positive scale"""
    g = 0
    for x in r:
        g = math.gcd(g, abs(x))
    if g == 0:
        return tuple(r)
    v = [x // g for x in r]
    j = next(i for i in range(len(v)) if v[i])
    return tuple(v) if v[j] > 0 else tuple(-x for x in v)


CLS = {}
for k in range(NORB):
    CLS.setdefault(prim(RW[k]), []).append(k)
CREP = [CLS[k][0] for k in sorted(CLS)]
NCL = len(CREP)
gate(NCL == 49 and irank([RW[k] for k in CREP]) == rk,
     "id.classes", "up to sign and positive scale the rows fall into {0} classes of the "
                   "same span {1}; two orbits sharing a class are already a two-term "
                   "dependency, so the classes are where five-term ones live".format(NCL, rk))


def nullvec(S):
    """the one-dimensional integer left nullspace of the rows S, cleared to primitive"""
    n, m = len(S), len(RW[0])
    A = [[RW[k][c] for k in S] for c in range(m)]
    piv, where = 0, {}
    for c in range(n):
        p = next((r for r in range(piv, m) if A[r][c]), None)
        if p is None:
            continue
        A[piv], A[p] = A[p], A[piv]
        pv = A[piv][c]
        for r in range(m):
            if r != piv and A[r][c]:
                f = A[r][c]
                A[r] = [pv * x - f * y for x, y in zip(A[r], A[piv])]
                g = 0
                for x in A[r]:
                    g = math.gcd(g, abs(x))
                if g > 1:
                    A[r] = [x // g for x in A[r]]
        where[c] = piv
        piv += 1
    free = [c for c in range(n) if c not in where]
    if len(free) != 1:
        return None
    fc, den = free[0], 1
    for c, r in where.items():
        den = den * A[r][c] // math.gcd(den, abs(A[r][c]))
    v = [0] * n
    v[fc] = den
    for c, r in where.items():
        v[c] = -A[r][fc] * (den // A[r][c])
    g = 0
    for x in v:
        g = math.gcd(g, abs(x))
    return [x // g for x in v]


CNT, CMB, ncirc, worst = {}, {}, 0, 0
for S in itertools.combinations(range(NCL), 5):
    rows = [RW[CREP[k]] for k in S]
    if irank(rows) != 4:
        continue
    if max(4 - irank([rows[j] for j in range(5) if j != d]) for d in range(5)) != 0:
        continue
    v = nullvec([CREP[k] for k in S])
    if v is None:
        continue
    ncirc += 1
    CNT[sum(v)] = CNT.get(sum(v), 0) + 1
    xs = sum(a * int(CXR[CREP[k]]) for a, k in zip(v, S))
    CMB[xs] = CMB.get(xs, 0) + 1
    res = [0] * len(RW[0])
    for a, k in zip(v, S):
        for c in range(len(RW[0])):
            res[c] += a * RW[CREP[k]][c]
    worst = max(worst, max(abs(x) for x in res))
NTOT = NCL * (NCL - 1) * (NCL - 2) * (NCL - 3) * (NCL - 4) // 120
gate(ncirc == 185 and worst == 0 and sorted(CNT) == [0],
     "id.census", "a complete sweep of all {0} five-element supports finds {1} minimal-"
                  "support dependencies, each verified to residual {2}, and every one has "
                  "coefficient sum {3} as the span argument requires".format(
                      NTOT, ncirc, worst, sorted(CNT)[0]))
nzc = sum(CMB[x] for x in CMB if x != 0)
gate(nzc == 49 and len([x for x in CMB if x != 0]) == 3,
     "id.spread", "their charge combinations are {0}, so {1} carry an exact slack identity "
                  "and those take more than one value; this cycle's relation is one "
                  "instance of a mechanism".format(
                      dict(sorted(CMB.items())), nzc))

probe = []
for j in range(NORB):
    e = np.zeros(NORB, dtype=np.int64)
    e[j] = 1
    probe.append((e, 0, 1))
probe.append((FU, FLOOR_Z, FLOOR_D))
probe.append((CU, CEIL_Z, CEIL_D))
holds = 0
for u, Z, D in probe:
    s = slacks(u, Z, D, True)
    if sum(c * int(s[int(REPS[o])]) for o, c in COEF) == 2 * D:
        holds += 1
gate(holds == len(probe),
     "id.universal", "the combination equals 2D for all {0} weight vectors tried, as the "
                     "row dependency requires".format(len(probe)))

forced = []
for o, _ in COEF:
    if o == 3:
        continue
    d = search(CTI, forced=[int(REPS[o])])
    forced.append((o, d))
gate(all(d is not None and is_dissection(d) and int(CX[np.array(d)].sum()) == 128 and
         int(CS[np.array(d)].sum()) == 0 for o, d in forced),
     "ceil.forced", "orbits {0} each sit in an exhibited cost-128 dissection, so a zero-gap "
                    "ceiling certificate is tight on all four".format([o for o, _ in forced]))
s3 = int(CS[int(REPS[3])])
gate(3 * s3 == 2 * CEIL_D and 2 * CEIL_D - (2 * CEIL_D // 3) * 3 == 0,
     "ceil.pinned", "that leaves 3 s(3) = 2D, here 3 times {0} = {1}; so 3 divides D, "
                    "3 is the least denominator and it is attained".format(s3, 3 * s3))
chi = [int(FS[int(REPS[o])] != 0) for o, _ in COEF]
cmb = sum(c * t for (o, c), t in zip(COEF, chi))
gate(cmb == -2 and not any(3 * x == 2 for x in (0, 1)),
     "ceil.noind", "an indicator needs the combination to be 2, and 3 x = 2 has no 0/1 "
                   "answer; the floor pattern {0} gives {1} and does".format(chi, cmb))

broke = 0
for k in range(len(COEF)):
    for d in (0, 2):
        alt = list(COEF)
        alt[k] = (alt[k][0], alt[k][1] * d if d == 0 else alt[k][1] + 1)
        w = np.zeros(NORB, dtype=np.int64)
        for o, c in alt:
            w = w + c * MR[o]
        if bool((w != 0).any()):
            broke += 1
gate(broke == 2 * len(COEF),
     "id.discriminate", "{0} of {1} single-coefficient changes destroy the dependency".format(
         broke, 2 * len(COEF)))

sec("what the support looks like locally")

tab = []
for c in range(3, 8):
    ii = np.flatnonzero(CX == c)
    tab.append((c, int(len(ii)), int((FS[ii] == 0).sum())))
gate(tab == [(3, 64, 64), (4, 384, 384), (5, 1152, 960), (6, 768, 384), (7, 304, 0)],
     "loc.table", "pieces and support pieces by charge {0}".format(tab))
dec = int(((CX <= 4) | (CX == 7)).sum())
gate(int(((CX <= 4) & (FS != 0)).sum()) == 0 and int(((CX == 7) & (FS == 0)).sum()) == 0,
     "loc.ends", "charge at most 4 forces support, charge 7 forces outside; that decides "
                 "{0} of {1} pieces".format(dec, NPIECE))
gate(NPIECE - dec == 1920 and all(0 < t[2] < t[1] for t in tab if t[0] in (5, 6)),
     "loc.middle", "the remaining {0} pieces at charge 5 or 6 split both ways".format(
         NPIECE - dec))

inn = set(SUPO)
INV = {"least spatial gap": [], "largest spatial gap": [], "zero-gap pairs": [],
       "body-diagonal pairs": [], "tick differences": [], "orbit size": []}
for o in range(NORB):
    P5 = V[UNI[int(REPS[o])]]
    sp = sorted(int(np.abs(P5[a][:3] - P5[b][:3]).sum()) for a, b in PAIRS)
    INV["least spatial gap"].append(sp[0])
    INV["largest spatial gap"].append(sp[-1])
    INV["zero-gap pairs"].append(sum(1 for x in sp if x == 0))
    INV["body-diagonal pairs"].append(sum(1 for x in sp if x == 3))
    INV["tick differences"].append(sum(int(abs(P5[a][3] - P5[b][3])) for a, b in PAIRS))
    INV["orbit size"].append(int(SZ[o]))
sepd = [k for k, vals in INV.items()
        if not (set(vals[o] for o in range(NORB) if o in inn) &
                set(vals[o] for o in range(NORB) if o not in inn))]
gate(sepd == [],
     "loc.noinv", "none of the {0} local invariants swept separates the {1} support orbits "
                  "from the other {2}".format(len(INV), len(SUPO), NORB - len(SUPO)))

print("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
