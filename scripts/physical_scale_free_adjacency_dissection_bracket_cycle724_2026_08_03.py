"""Cycle 724 - the scale-free adjacency ceiling and the dissection cost bracket.

Everything here is a theorem of a SUPPLIED structural model, not of the framework
axioms alone: cells are 4-simplices - five vertices with all ten vertex pairs graded -
on the tick-extended domain Z^3 x {tick}, and a dissection is a family of such cells
with pairwise disjoint interiors whose volumes sum to the region's. The Lattice axiom
supplies only the spatial Z^3 6-NN adjacency that grades the vertex pairs; the
registered kinetic-isotropy primitive supplies only the equal tick/edge graining under
which the tick coordinate enters. Neither supplies a cell selection or a rule-to-tick
correspondence: whether physical assembly cells are pairwise-adjacency simplices at
all, and the physical tick-Admissibility realization bridge, are OPEN questions this
runner does not touch.

Every edge slot of a tick-extended cell is graded by its SPATIAL FOOTPRINT weight: the
L1 weight of the spatial part of the slot's direction. Weight 0 is a same-site slot,
weight 1 is a nearest-neighbour slot of the Lattice axiom's spatial 6-NN adjacency, and
weight 2 or more exceeds that adjacency. The adjacency cost of a cell is the number of
its ten vertex pairs of weight 2 or more; the cost of a dissection is the sum over its
cells.

On that supplied model this runner measures:

  (a) an adjacency clique lemma and an affine ceiling that hold at every lattice
      resolution, for every vertex choice, in every box - not just at the corners,
  (b) the exact per-cell cost floor and the complete structure of the cells attaining it,
  (c) a volume-weighted cost lower bound for arbitrary corner dissections - no claim
      that any dissection attains it - and the same bound recomputed on a twice-refined
      resolution of the same region,
  (d) the exact unimodular census, its interior-disjointness compatibility graph, and
      two clique numbers that bound the cost of a unimodular dissection from below,
      against the explicit monotone-path dissection from above.

All combinatorics - censuses, costs, volumes, affine ranks, clique numbers - is exact
integer arithmetic: determinants by integer cofactor expansion, ranks by fraction-free
integer elimination, the three ratios as exact rationals printed at one decimal place.
Interior-disjointness of two cells is decided by the exact separating-hyperplane scan
over the 210 four-subsets of their ten vertices; a separating hyperplane, when one
exists, is spanned by four affinely independent points of that union, so the scan
decides the predicate. It is cross-checked against an independent linear-programming
formulation of the same predicate - the one floating-point surface, held to TOL and
fail-closed: only a proven-infeasible programme certifies disjointness, and any other
unsuccessful solver termination aborts the run - and against a deliberately
overlapping pair.
"""

import itertools
import json
import sys
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog

PAIRS5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
SUBS = list(itertools.combinations(range(10), 4))
COLS = [[c for c in range(4) if c != k] for k in range(4)]
TOL = 1.0e-9

sys.setrecursionlimit(20000)

PASS = 0
FAIL = 0


def chk(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print("[{0}] {1}{2}".format(tag, name, (" " + detail) if detail else ""))


def f1(x):
    return "{0:.1f}".format(float(x))


def domain(vals, ticks):
    return np.array([list(s) + [t] for s in itertools.product(vals, repeat=3)
                     for t in ticks], dtype=np.int64)


def det3b(a, b, c):
    """Batched three-by-three determinant of integer row triples."""
    return (a[:, 0] * (b[:, 1] * c[:, 2] - b[:, 2] * c[:, 1])
            - a[:, 1] * (b[:, 0] * c[:, 2] - b[:, 2] * c[:, 0])
            + a[:, 2] * (b[:, 0] * c[:, 1] - b[:, 1] * c[:, 0]))


def det4(M):
    """Exact four-by-four integer determinant by cofactor expansion, in Python ints."""
    a = [[int(x) for x in row] for row in M]

    def det3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    return sum(((-1) ** k) * a[0][k]
               * det3([[a[r][c] for c in COLS[k]] for r in (1, 2, 3)])
               for k in range(4))


def det4b(D):
    """Batched exact four-by-four integer determinant by cofactor expansion along the
    first row; all arithmetic stays in int64, which these entry sizes cannot overflow."""
    out = np.zeros(len(D), dtype=np.int64)
    for k in range(4):
        out += ((-1) ** k) * D[:, 0, k] * det3b(D[:, 1, COLS[k]], D[:, 2, COLS[k]],
                                                D[:, 3, COLS[k]])
    return out


def rank_int(A):
    """Exact rank of an integer matrix by fraction-free Gaussian elimination."""
    rows = [[int(x) for x in r] for r in A]
    ncols = len(rows[0]) if rows else 0
    rank = 0
    col = 0
    r = 0
    while r < len(rows) and col < ncols:
        piv = next((i for i in range(r, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(r + 1, len(rows)):
            if rows[i][col] != 0:
                f, p = rows[i][col], rows[r][col]
                rows[i] = [p * rows[i][c] - f * rows[r][c] for c in range(ncols)]
        r += 1
        rank += 1
        col += 1
    return rank


def cost(M):
    """Adjacency cost: vertex pairs whose spatial footprint weight is 2 or more."""
    return sum(1 for i, j in PAIRS5 if int(abs(M[i][:3] - M[j][:3]).sum()) >= 2)


def l1(a, b):
    return sum(abs(a[k] - b[k]) for k in range(3))


# ----------------------------------------------------------------------------------
# (a) the adjacency clique lemma and the affine ceiling, at every resolution
# ----------------------------------------------------------------------------------
print("--- adjacency ceiling, resolution-free ---")
BOX = list(itertools.product(range(-2, 3), repeat=3))
near = [(a, b) for a, b in itertools.combinations(range(len(BOX)), 2)
        if l1(BOX[a], BOX[b]) <= 1]
triples = sum(1 for a, b in near for c in range(len(BOX))
              if c != a and c != b
              and l1(BOX[a], BOX[c]) <= 1 and l1(BOX[b], BOX[c]) <= 1) // 3
chk("adjacency clique lemma: no three distinct sites are pairwise adjacent",
    triples == 0, "offending triples {0} over {1} sites, {2} adjacent pairs".format(
        triples, len(BOX), len(near)))

# By the lemma an adjacency-only vertex set occupies at most two sites, so every such
# set lies in a two-site slab. Enumerate the slabs directly (translation invariance
# fixes one site at the origin) and measure both the affine rank of a slab and the
# volume of every five-subset drawn from one.
ranks = set()
dets = set()
slabs = 0
sub5 = 0
for p in itertools.product(range(-1, 2), repeat=3):
    if sum(abs(c) for c in p) > 1:
        continue
    slabs += 1
    A = np.array([list(s) + [t] for s in ((0, 0, 0), p) for t in range(-2, 3)],
                 dtype=np.int64)
    ranks.add(rank_int(A[1:] - A[0]))
    for comb in itertools.combinations(range(len(A)), 5):
        M = A[list(comb)]
        dets.add(abs(det4(M[1:] - M[0])))
        sub5 += 1
chk("affine rank of an adjacency-only vertex set is at most two, and two is reached",
    max(ranks) == 2 and ranks == {1, 2},
    "{0} two-site slabs, observed ranks {1}".format(slabs, sorted(ranks)))
chk("no nondegenerate cell is adjacency-only, at any resolution or box",
    dets == {0},
    "{0} five-subsets of the slabs, distinct volumes {1}".format(sub5, sorted(dets)))

tight = np.array([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                 dtype=np.int64)
chk("rejector: a cell just above adjacency-only does reach affine rank four",
    rank_int(tight[1:] - tight[0]) == 4 and cost(tight) == 3,
    "rank {0} at adjacency cost {1}".format(
        rank_int(tight[1:] - tight[0]), cost(tight)))

# ----------------------------------------------------------------------------------
# (b) the exact per-cell floor at the native resolution, and what attains it
# ----------------------------------------------------------------------------------
print("--- per-cell floor and its minimizers ---")
A1 = domain((0, 1), (0, 1))
tot1 = 0
joint1 = {}
mins = []
UV = []
UW = []
for comb in itertools.combinations(range(16), 5):
    M = A1[list(comb)]
    v = abs(det4(M[1:] - M[0]))
    if v == 0:
        continue
    tot1 += 1
    e = cost(M)
    joint1[(e, v)] = joint1.get((e, v), 0) + 1
    if e == 3:
        mins.append(M)
    if v == 1:
        UV.append(M)
        UW.append(e)
floor1 = min(e for e, _ in joint1)
chk("corner cell census at the native resolution",
    tot1 == 3008 and len(list(itertools.combinations(range(16), 5))) == 4368,
    "{0} nondegenerate of {1} five-subsets".format(tot1, 4368))
chk("per-cell adjacency floor is three, attained by exactly sixty-four cells",
    floor1 == 3 and len(mins) == 64,
    "floor {0}, attaining cells {1}".format(floor1, len(mins)))

pat = set()
for M in mins:
    sites = [tuple(int(c) for c in row[:3]) for row in M]
    mult = tuple(sorted((sites.count(s) for s in set(sites)), reverse=True))
    dbl = [s for s in set(sites) if sites.count(s) == 2]
    both = all(sorted(int(M[k][3]) for k in range(5)
                      if tuple(int(c) for c in M[k][:3]) == s) == [0, 1] for s in dbl)
    axes = len(dbl) == 1 and all(l1(s, dbl[0]) == 1
                                 for s in set(sites) if s != dbl[0])
    pat.add((mult, both, axes, abs(det4(M[1:] - M[0]))))
chk("every floor-cost cell is a doubled star on three axes, of minimal volume",
    pat == {((2, 1, 1, 1), True, True, 1)},
    "structure {0}".format(sorted(str(p) for p in pat)))

# ----------------------------------------------------------------------------------
# (c) volume-weighted floor for arbitrary corner dissections, and one refinement
# ----------------------------------------------------------------------------------
print("--- volume-weighted dissection floor ---")
ratio1 = min(Fraction(24 * e, v) for (e, v) in joint1)
arg1 = sorted((e, v) for (e, v) in joint1 if Fraction(24 * e, v) == ratio1)
chk("volume-weighted cost lower bound for an arbitrary corner dissection of the cell",
    ratio1 == 56 and arg1 == [(7, 3)],
    "lower bound {0} set by the ratio-minimising cost and volume class {1}; no claim"
    " that any dissection attains it".format(f1(ratio1), arg1))
ratmin = min(Fraction(24 * e, v) for (e, v) in joint1 if e == floor1)
chk("the floor-cost cells are not the volume-efficient ones, so they do not set it",
    ratmin > ratio1,
    "floor-cost cells run at {0} against the dissection lower bound {1}".format(
        f1(ratmin), f1(ratio1)))


def sweep(A, chunk=200000):
    src = itertools.combinations(range(len(A)), 5)
    joint = {}
    while True:
        block = list(itertools.islice(src, chunk))
        if not block:
            break
        M = A[np.array(block, dtype=np.int64)]
        det = det4b(M[:, 1:, :] - M[:, :1, :])
        keep = det != 0
        if not keep.any():
            continue
        M = M[keep]
        v24 = np.abs(det[keep])
        exc = np.zeros(len(M), dtype=np.int64)
        for i, j in PAIRS5:
            exc += (np.abs(M[:, i, :3] - M[:, j, :3]).sum(axis=1) >= 2)
        for e, v in zip(exc.tolist(), v24.tolist()):
            joint[(e, v)] = joint.get((e, v), 0) + 1
    return joint


J2 = sweep(domain((0, 1, 2), (0, 1)))
tot2 = sum(J2.values())
ratio2 = min(Fraction(24 * e, v) for (e, v) in J2)
region2 = ratio2 * 8
chk("the per-cell floor survives a twice-refined resolution of the same region",
    min(e for e, _ in J2) == 3 and tot2 == 2449800,
    "{0} nondegenerate refined cells, floor {1}".format(tot2, min(e for e, _ in J2)))
chk("the refined region floor rises above the native-resolution region floor",
    ratio2 == 10 and region2 > ratio1,
    "refined {0} against native {1}".format(f1(region2), f1(ratio1)))

# ----------------------------------------------------------------------------------
# (d) the unimodular census, its compatibility graph, and the cost bracket
# ----------------------------------------------------------------------------------
print("--- unimodular census and compatibility ---")
V = np.array(UV, dtype=np.int64)
Wa = np.array(UW, dtype=np.int64)
prof = {}
for w in UW:
    prof[w] = prof.get(w, 0) + 1
chk("unimodular corner cells and their adjacency-cost profile",
    len(UV) == 2672 and prof == {3: 64, 4: 384, 5: 1152, 6: 768, 7: 304},
    "{0} cells, profile {1}".format(len(UV), dict(sorted(prof.items()))))


def disjoint_batch(P, Q):
    """Exact interior-disjointness of two cells, batched over pairs."""
    out = np.zeros(len(P), dtype=bool)
    live = np.arange(len(P))
    U = np.concatenate([P, Q], axis=1)
    for s in SUBS:
        if live.size == 0:
            break
        Ul = U[live]
        base = Ul[:, s[0]]
        v1 = Ul[:, s[1]] - base
        v2 = Ul[:, s[2]] - base
        v3 = Ul[:, s[3]] - base
        nv = np.stack([((-1) ** k) * det3b(v1[:, COLS[k]], v2[:, COLS[k]],
                                           v3[:, COLS[k]]) for k in range(4)], axis=1)
        ok = nv.any(axis=1)
        c = (nv * base).sum(axis=1)
        a = np.einsum("bvd,bd->bv", P[live], nv) - c[:, None]
        b = np.einsum("bvd,bd->bv", Q[live], nv) - c[:, None]
        sep = ok & (((a.max(1) <= 0) & (b.min(1) >= 0))
                    | ((b.max(1) <= 0) & (a.min(1) >= 0)))
        out[live[sep]] = True
        live = live[~sep]
    return out


def disjoint_lp(P, Q):
    """Independent reference for the same predicate, by linear programming rather than
    by hyperplane search: maximise the smallest barycentric coordinate over the points
    common to both cells. The interiors meet exactly when that optimum is positive.

    Fail-closed: a proven-infeasible programme is the one unsuccessful termination that
    certifies disjointness (the closed cells share no point at all). Any other
    unsuccessful termination - iteration limit, numerical failure, unboundedness -
    certifies nothing and raises, aborting the run with a nonzero exit instead of
    silently agreeing with the hyperplane scan."""
    obj = [0.0] * 10 + [-1.0]
    aeq, beq = [], []
    for d in range(4):
        aeq.append([float(P[i][d]) for i in range(5)]
                   + [-float(Q[j][d]) for j in range(5)] + [0.0])
        beq.append(0.0)
    aeq.append([1.0] * 5 + [0.0] * 5 + [0.0])
    beq.append(1.0)
    aeq.append([0.0] * 5 + [1.0] * 5 + [0.0])
    beq.append(1.0)
    aub = []
    for k in range(10):
        row = [0.0] * 11
        row[k] = -1.0
        row[10] = 1.0
        aub.append(row)
    res = linprog(obj, A_ub=aub, b_ub=[0.0] * 10, A_eq=aeq, b_eq=beq,
                  bounds=[(0.0, 1.0)] * 10 + [(None, None)])
    if res.status == 2:
        return True
    if not res.success:
        raise RuntimeError(
            "linprog terminated abnormally (status {0}: {1}); no disjointness"
            " certificate either way".format(res.status, res.message))
    return float(-res.fun) <= TOL


t3 = np.flatnonzero(Wa == 3)
lp_pairs = list(itertools.combinations(range(len(t3)), 2))
bad = 0
for x, y in lp_pairs:
    p, q = V[t3[x]], V[t3[y]]
    if bool(disjoint_batch(p[None], q[None])[0]) != disjoint_lp(p, q):
        bad += 1
chk("the hyperplane predicate agrees with the independent programme formulation",
    bad == 0, "{0} disagreements over {1} floor-cost pairs".format(bad, len(lp_pairs)))
same = V[t3[0]]
chk("rejector: a cell is not interior-disjoint from itself, under either method",
    not bool(disjoint_batch(same[None], same[None])[0]) and not disjoint_lp(same, same),
    "the deliberately overlapping pair is refused by both")

n = len(V)
adj = np.zeros((n, n), dtype=bool)
I, J = np.triu_indices(n, 1)
for lo in range(0, len(I), 300000):
    ii, jj = I[lo:lo + 300000], J[lo:lo + 300000]
    adj[ii, jj] = disjoint_batch(V[ii], V[jj])
adj |= adj.T
deg = adj.sum(1)
edges = int(adj.sum()) // 2
chk("interior-disjointness compatibility graph over the unimodular census",
    edges == 1984616,
    "edges {0}, degree {1} to {2}".format(edges, int(deg.min()), int(deg.max())))


def max_clique(verts):
    """Exact maximum clique. The colour bound is sound only when candidates are taken
    in decreasing colour order; taking them in increasing order silently under-reports,
    which is how an earlier reading of this graph came out two cells short."""
    idx = list(verts)
    sub = adj[np.ix_(idx, idx)]
    nbr = [set(np.flatnonzero(sub[i]).tolist()) for i in range(len(idx))]
    best = [0, None]

    def colour_sort(cand):
        classes = []
        colour = {}
        for v in sorted(cand, key=lambda x: -len(nbr[x] & cand)):
            placed = False
            for ci, cl in enumerate(classes):
                if not (nbr[v] & cl):
                    cl.add(v)
                    colour[v] = ci + 1
                    placed = True
                    break
            if not placed:
                classes.append({v})
                colour[v] = len(classes)
        return [v for cl in classes for v in cl], colour

    def expand(clique, cand):
        if not cand:
            if len(clique) > best[0]:
                best[0], best[1] = len(clique), list(clique)
            return
        order, colour = colour_sort(cand)
        for i in range(len(order) - 1, -1, -1):
            v = order[i]
            if len(clique) + colour[v] <= best[0]:
                return
            expand(clique + [v], cand & nbr[v])
            cand = cand - {v}

    expand([], set(range(len(idx))))
    return best[0], [idx[i] for i in best[1]]


def plain_clique(verts):
    """Maximum clique again with the colour bound removed entirely: only the
    can-this-branch-still-beat-the-incumbent size test survives. Slower, but it shares
    no pruning rule with the coloured search, so agreement is a real cross-check."""
    idx = list(verts)
    sub = adj[np.ix_(idx, idx)]
    nbr = [set(np.flatnonzero(sub[i]).tolist()) for i in range(len(idx))]
    best = [0]

    def dfs(size, cand):
        if size + len(cand) <= best[0]:
            return
        if not cand:
            best[0] = max(best[0], size)
            return
        for v in sorted(cand):
            dfs(size + 1, cand & nbr[v])
            cand = cand - {v}
            if size + len(cand) <= best[0]:
                return

    dfs(0, set(range(len(idx))))
    return best[0]


def verify_family(fam):
    """Re-derive pairwise interior-disjointness of a witness family straight from the
    vertex coordinates, bypassing the cached graph entirely."""
    prs = list(itertools.combinations(sorted(fam), 2))
    if not prs:
        return True
    P = np.array([V[a] for a, _ in prs], dtype=np.int64)
    Q = np.array([V[b] for _, b in prs], dtype=np.int64)
    return bool(disjoint_batch(P, Q).all())


print("--- cost bracket for a unimodular dissection ---")
tier3 = np.flatnonzero(Wa == 3).tolist()
k3, w3 = max_clique(tier3)
chk("largest pairwise interior-disjoint family of floor-cost cells",
    k3 == 8, "size {0} of the {1} floor-cost cells".format(k3, len(tier3)))
k3p = plain_clique(tier3)
chk("that maximum survives dropping the colour bound, and its witness re-derived"
    " from the vertex coordinates",
    k3p == k3 and len(set(w3)) == k3 and verify_family(w3),
    "colour-free search agrees at {0}".format(k3p))
tier34 = np.flatnonzero(Wa <= 4).tolist()
k34, w34 = max_clique(tier34)
p34 = {}
for v in w34:
    p34[int(Wa[v])] = p34.get(int(Wa[v]), 0) + 1
chk("largest pairwise interior-disjoint family of below-average-cost cells",
    k34 == 16 and 3 not in p34,
    "size {0}, profile {1}".format(k34, dict(sorted(p34.items()))))
k34r, w34r = max_clique(tier34[::-1])
chk("that maximum is invariant under reversing the vertex order, and both witnesses"
    " re-derived from the vertex coordinates",
    k34r == k34 and len(set(w34)) == k34 and verify_family(w34) and verify_family(w34r),
    "reversed order agrees at {0}".format(k34r))
lower = 120 - k3 - k34
chk("cost floor for any unimodular corner dissection",
    lower == 96,
    "twenty-four cells benchmarked at cost five give {0}; costs above five only add,"
    " a cost-3 cell saves 2, a cost-4 cell saves 1, and the saving 2*n3 + n4 ="
    " n3 + (n3 + n4) is at most {1} + {2}, leaving at least {3}".format(
        120, k3, k34, lower))

kuhn = []
for perm in itertools.permutations(range(4)):
    cur = np.zeros(4, dtype=np.int64)
    verts = [cur.copy()]
    for ax in perm:
        cur = cur.copy()
        cur[ax] = 1
        verts.append(cur)
    kuhn.append(np.array(verts, dtype=np.int64))
K = np.array(kuhn, dtype=np.int64)
kpairs = list(itertools.combinations(range(24), 2))
kover = int((~disjoint_batch(K[[x for x, _ in kpairs]],
                             K[[y for _, y in kpairs]])).sum())
kvol = sum(abs(det4(M[1:] - M[0])) for M in kuhn)
kw = [cost(M) for M in kuhn]
kprof = {}
for w in kw:
    kprof[w] = kprof.get(w, 0) + 1
chk("the monotone-path stencil is a genuine unimodular dissection of the whole cell",
    len(kuhn) == 24 and kover == 0 and kvol == 24
    and all(abs(det4(M[1:] - M[0])) == 1 for M in kuhn),
    "{0} cells, overlapping pairs {1}, volumes summing to the whole cell {2}".format(
        len(kuhn), kover, kvol))
upper = sum(kw)
chk("its adjacency cost, and that no cell of it attains the per-cell floor",
    upper == 108 and min(kw) == 4,
    "cost {0}, profile {1}, cheapest cell {2} against the floor {3}".format(
        upper, dict(sorted(kprof.items())), min(kw), floor1))
chk("the bracket is nonempty, and restricting to unimodular cells raises the floor",
    lower < upper and lower > ratio1,
    "unimodular bracket {0} to {1}, arbitrary-dissection floor {2}".format(
        lower, upper, f1(ratio1)))
print("the refined region floor {0} lies below the achieved cost {1}: refining the"
      " resolution raises the guaranteed minimum, it does not raise the achieved"
      " count".format(f1(region2), upper))

RECEIPT = {
    "adjacency_clique_offending_triples": triples,
    "adjacency_clique_box_sites": len(BOX),
    "adjacency_only_affine_ranks": sorted(ranks),
    "adjacency_only_cell_volumes": sorted(dets),
    "adjacency_only_five_subsets": sub5,
    "rejector_affine_rank": rank_int(tight[1:] - tight[0]),
    "rejector_adjacency_cost": cost(tight),
    "corner_five_subsets": 4368,
    "corner_cells_nondegenerate": tot1,
    "per_cell_cost_floor": floor1,
    "floor_attaining_cells": len(mins),
    "floor_cell_structure": sorted(str(p) for p in pat),
    "arbitrary_dissection_floor": f1(ratio1),
    "arbitrary_floor_argmin": [list(x) for x in arg1],
    "floor_cost_cell_ratio": f1(ratmin),
    "refined_cells_nondegenerate": tot2,
    "refined_cell_cost_floor": min(e for e, _ in J2),
    "refined_region_floor": f1(region2),
    "unimodular_cells": len(UV),
    "unimodular_cost_profile": dict((str(k), v) for k, v in sorted(prof.items())),
    "compatibility_edges": edges,
    "compatibility_degree_range": [int(deg.min()), int(deg.max())],
    "programme_disagreements": bad,
    "programme_pairs_checked": len(lp_pairs),
    "floor_cost_clique": k3,
    "floor_cost_clique_colour_free": k3p,
    "below_average_cost_clique": k34,
    "below_average_clique_reversed_order": k34r,
    "below_average_clique_profile": dict((str(k), v) for k, v in sorted(p34.items())),
    "unimodular_cost_lower_bound": lower,
    "monotone_path_cells": len(kuhn),
    "monotone_path_overlaps": kover,
    "monotone_path_dissection_cost": upper,
    "monotone_path_cost_profile": dict((str(k), v) for k, v in sorted(kprof.items())),
    "review_loop": {
        "iteration": 1,
        "disposition": "FIX_THEN_PROCEED",
        "reviewer": "Sol",
        "date": "2026-08-08",
        "fix": "narrowed the physical framing to the supplied tick-extended simplex"
               " model, removed the 56-attainability claim, made the programme"
               " cross-check fail-closed, made determinants/ranks/ratios exact, and"
               " rewired the dependency edges to the actual premises",
    },
}
print("RECEIPT " + json.dumps(RECEIPT, sort_keys=True))
print("TOTAL: PASS={0} FAIL={1}".format(PASS, FAIL))
sys.exit(1 if FAIL else 0)
