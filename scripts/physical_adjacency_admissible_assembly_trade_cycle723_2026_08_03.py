"""Cycle 723 - adjacency-admissible assembly and the excess-slot trade.

Every edge slot of the tick-extended assembly is partitioned by its SPATIAL FOOTPRINT
weight: the L1 weight of the spatial part of the slot's direction. Weight 0 is a
same-site slot, weight 1 is a nearest-neighbour slot of the LATTICE axiom's own 6-NN
adjacency, and weight 2 or more exceeds that adjacency. The runner measures

  (a) how much of the assembly stencil sits above adjacency, and whether any corner
      stencil at all could avoid it, and
  (b) what the assembled second-variation form does when the exceeding slots are
      deleted, and when they are eliminated instead.

The combinatorial half is exact integer arithmetic over a complete enumeration of
corner subsets. The assembly half reuses the open-coframe endpoint compiler.
"""

import importlib.util
import itertools
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
C696 = os.path.join(HERE, "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py")
_spec = importlib.util.spec_from_file_location("c696", C696)
m = importlib.util.module_from_spec(_spec)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
_spec.loader.exec_module(m)

regge = m.regge
DIRS = list(regge.DIRS15)
DIDX = dict((d, i) for i, d in enumerate(DIRS))
PAIRS5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
C4 = [tuple(v) for v in itertools.product((0, 1), repeat=4)]
C3 = [tuple(v) for v in itertools.product((0, 1), repeat=3)]
FLAT_TOL = 1.0e-5
SYM_TOL = 1.0e-6

PASS = 0
FAIL = 0


def md(x, n):
    """Non-negative residue without the residue operator."""
    return int(x - n * (x // n))


def chk(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print("[{0}] {1}{2}".format(tag, name, (" " + detail) if detail else ""))


def bound(dev, tol):
    """Report a near-zero deviation as a bound at the pass tolerance, not as noise digits."""
    return "below {0:.1e}".format(tol) if dev < tol else "at {0:.6e}".format(dev)


def f3(x):
    return "{0:.3f}".format(float(x))


def foot(p, q):
    """Spatial footprint weight of the slot joining two corners."""
    return sum(abs(p[c] - q[c]) for c in range(3))


def stp(p, q):
    return tuple(abs(p[i] - q[i]) for i in range(4))


def vol24(P):
    """Twenty-four times the volume of a corner 4-simplex, as an exact integer."""
    M = np.array([[P[t][c] - P[0][c] for c in range(4)] for t in range(1, 5)], dtype=np.int64)
    return abs(int(round(float(np.linalg.det(M)))))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def sub3(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def dot3(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vol6(T):
    """Six times the volume of a corner tetrahedron of a cell facet."""
    return abs(dot3(sub3(T[1], T[0]), cross(sub3(T[2], T[0]), sub3(T[3], T[0]))))


def eclass(p, r):
    """Undirected edge class: the sign of the step is absorbed into the anchor."""
    return (DIDX[stp(p, r)], tuple(min(p[i], r[i]) for i in range(4)))


def paths(a):
    """The 24 path simplices whose main diagonal runs (a,0) -> (1-a,1)."""
    v0 = (a[0], a[1], a[2], 0)
    v1 = (1 - a[0], 1 - a[1], 1 - a[2], 1)
    out = []
    for perm in itertools.permutations(range(4)):
        vs = [list(v0)]
        for q in perm:
            w = list(vs[-1])
            w[q] = v1[q]
            vs.append(w)
        out.append([tuple(v) for v in vs])
    return out


# ---------------------------------------------------- section 1: slot census

SK = paths((0, 0, 0))
uses = dict((w, 0) for w in range(4))
spat = dict((w, 0) for w in range(4))
nspat = 0
distinct = {}
for s in SK:
    for i, j in PAIRS5:
        p, q = s[i], s[j]
        d = stp(p, q)
        uses[foot(p, q)] += 1
        if d[3] == 0:
            nspat += 1
            spat[foot(p, q)] += 1
        distinct[(d, tuple(min(p[c], q[c]) for c in range(4)))] = foot(p, q)
dcen = dict((w, 0) for w in range(4))
for f in distinct.values():
    dcen[f] += 1

chk("slot_uses_total", sum(uses.values()) == 240 and nspat == 120,
    "240 slot-uses of which {0} are purely spatial".format(nspat))
chk("spatial_slot_split", (spat[1], spat[2], spat[3]) == (72, 36, 12),
    "spatial 120 = 72 axis + 36 face-diagonal + 12 body-diagonal")
chk("footprint_census", [uses[w] for w in range(4)] == [24, 108, 72, 36],
    "slot-uses by spatial footprint weight 0/1/2/3 = 24/108/72/36")
chk("distinct_slots_per_cell",
    len(distinct) == 65 and [dcen[w] for w in range(4)] == [8, 36, 18, 3],
    "65 distinct slots per cell = 8/36/18/3 by footprint weight")
chk("slot_uses_exceeding_adjacency", uses[2] + uses[3] == 108 and dcen[2] + dcen[3] == 21,
    "108 of 240 slot-uses and 21 of 65 distinct slots exceed 6-NN adjacency")

# ------------------------------------------ section 2: the axiom obstruction

best_ind = {}
best_dep = {}
for msz in (3, 4):
    bi, bd = 0, 0
    for comb in itertools.combinations(range(8), msz):
        P = [C3[i] for i in comb]
        M = np.array([[P[t][c] - P[0][c] for c in range(3)] for t in range(1, msz)], dtype=float)
        e = sum(1 for i, j in itertools.combinations(range(msz), 2) if foot(P[i], P[j]) == 1)
        if int(np.linalg.matrix_rank(M)) == msz - 1:
            bi = max(bi, e)
        else:
            bd = max(bd, e)
    best_ind[msz], best_dep[msz] = bi, bd

chk("six_nn_pairs_three_corners", best_ind[3] == 2,
    "at most 2 of the 3 slots of a nondegenerate corner triangle are 6-NN")
chk("six_nn_pairs_four_corners", best_ind[4] == 3 and best_dep[4] == 4,
    "an affinely independent corner quadruple reaches 3; the rejector, a dependent one, reaches 4")

SIMS = []
for comb in itertools.combinations(range(16), 5):
    P = [C4[i] for i in comb]
    v = vol24(P)
    if v == 0:
        continue
    SIMS.append({
        "P": P,
        "v": v,
        "k": sum(1 for x in P if x[3] == 0),
        "nex": sum(1 for i, j in PAIRS5 if foot(P[i], P[j]) > 1),
        "nsp": sum(1 for i, j in PAIRS5 if stp(P[i], P[j])[3] == 0 and foot(P[i], P[j]) > 1),
        "nf": sum(1 for f in itertools.combinations(range(5), 4) if all(P[i][3] == 0 for i in f)),
    })

nfloor, sfloor, kfaces, kvol = {}, {}, {}, {}
for S in SIMS:
    k = S["k"]
    nfloor[k] = min(nfloor[k], S["nex"]) if k in nfloor else S["nex"]
    sfloor[k] = min(sfloor[k], S["nsp"]) if k in sfloor else S["nsp"]
    kfaces.setdefault(k, set()).add(S["nf"])
    kvol.setdefault(k, set()).add(S["v"])

kex, ksp = {}, {}
for s in SK:
    k = sum(1 for v in s if v[3] == 0)
    kex.setdefault(k, set()).add(sum(1 for i, j in PAIRS5 if foot(s[i], s[j]) > 1))
    ksp.setdefault(k, set()).add(
        sum(1 for i, j in PAIRS5 if stp(s[i], s[j])[3] == 0 and foot(s[i], s[j]) > 1))

chk("corner_simplex_census_complete", len(SIMS) == 3008,
    "{0} nondegenerate corner 4-simplices among all 4368 corner 5-subsets".format(len(SIMS)))
chk("exceeding_floor_every_tick_split", [nfloor[k] for k in (1, 2, 3, 4)] == [3, 3, 3, 3],
    "every nondegenerate corner 4-simplex carries at least 3 exceeding slots, at all four splits")
chk("no_adjacency_only_corner_stencil", min(nfloor.values()) > 0,
    "that floor is positive, so no corner assembly stencil is adjacency-only")
chk("path_stencil_attains_spatial_floor",
    [sfloor[k] for k in (1, 2, 3, 4)] == [3, 1, 1, 3]
    and [sorted(ksp[k]) for k in (1, 2, 3, 4)] == [[3], [1], [1], [3]],
    "spatial-only floor 3/1/1/3 by tick split, and the path stencil realizes exactly 3/1/1/3")
chk("path_stencil_exceeds_footprint_floor",
    [sorted(kex[k]) for k in (1, 2, 3, 4)] == [[5], [4], [4], [5]],
    "the path stencil carries 5/4/4/5 exceeding slots against the floor 3/3/3/3")

# ------------------------------ section 3: facet forcing and the global floor

chk("facet_forcing_law",
    all(kfaces[k] == set([0]) for k in (1, 2, 3)) and kfaces[4] == set([1]),
    "a corner 4-simplex meets the tick-0 hyperplane in a 3-face exactly when 4 corners lie there")

cone = True
for S in SIMS:
    if S["k"] == 4:
        cone = cone and S["v"] == vol6(tuple(x[:3] for x in S["P"] if x[3] == 0))
    if S["k"] == 1:
        cone = cone and S["v"] == vol6(tuple(x[:3] for x in S["P"] if x[3] == 1))
chk("cone_volume_relation", cone and sorted(kvol[4]) == [1, 2] and sorted(kvol[1]) == [1, 2],
    "an extreme-split simplex is a cone whose 24-fold volume equals its base facet's 6-fold volume")

TET = [T for T in itertools.combinations(C3, 4) if vol6(T) > 0]
AXES = {}
for T in TET:
    AXES[T] = ([sub3(T[j], T[i]) for i, j in itertools.combinations(range(4), 2)],
               [cross(sub3(T[b], T[a]), sub3(T[c], T[a]))
                for a, b, c in itertools.combinations(range(4), 3)])


def disjoint(A, B):
    """Exact integer separating-axis test: the interiors meet when no axis separates."""
    EA, NA = AXES[A]
    EB, NB = AXES[B]
    for n in list(NA) + list(NB) + [cross(u, v) for u in EA for v in EB]:
        if n == (0, 0, 0):
            continue
        pa = [dot3(n, p) for p in A]
        pb = [dot3(n, p) for p in B]
        if max(pa) <= min(pb) or max(pb) <= min(pa):
            return True
    return False


DIS = {}
for i, j in itertools.combinations(range(len(TET)), 2):
    DIS[(i, j)] = disjoint(TET[i], TET[j])
VOL = [vol6(T) for T in TET]
NEX = [sum(1 for i, j in itertools.combinations(range(4), 2) if foot(T[i], T[j]) > 1) for T in TET]
SOLS = []


def dfs(start, chosen, vol):
    if vol == 6:
        SOLS.append(tuple(chosen))
        return
    for k in range(start, len(TET)):
        if vol + VOL[k] > 6:
            continue
        if all(DIS[(c, k)] for c in chosen):
            chosen.append(k)
            dfs(k + 1, chosen, vol + VOL[k])
            chosen.pop()


dfs(0, [], 0)
dsz = sorted(set(len(s) for s in SOLS))
dna = min(sum(NEX[k] for k in s) for s in SOLS)
vmax23 = max(max(kvol[2]), max(kvol[3]))
vinner = 24 - 6 - 6
ninner = -(-vinner // vmax23)
gfloor = 2 * dna + min(nfloor[2], nfloor[3]) * ninner

chk("facet_corner_tetrahedra", len(TET) == 58 and sorted(set(VOL)) == [1, 2],
    "58 nondegenerate corner tetrahedra of a cell facet, of 6-fold volume 1 and 2")
chk("facet_corner_dissections", len(SOLS) == 182 and dsz == [5, 6],
    "182 corner dissections of a cell facet, of sizes 5 and 6")
chk("facet_dissection_exceeding_floor", dna == 18,
    "every corner dissection of a facet carries at least 18 exceeding slots")
chk("interior_volume_bookkeeping", vmax23 == 3 and vinner == 12 and ninner == 4,
    "the two cone families take 6 volume units each, leaving 12 for simplices of size at most 3")
chk("global_corner_stencil_floor", gfloor == 48 and uses[2] + uses[3] == 108,
    "any corner stencil carries at least {0} exceeding slot-uses; the path stencil carries {1}".format(
        gfloor, uses[2] + uses[3]))
chk("floor_and_spatial_count_are_distinct_quantities",
    gfloor == spat[2] + spat[3] and gfloor != uses[2] + uses[3],
    "the floor and the stencil's spatial-only count are different counts that happen to agree")

# ----------------------------------------------------- section 4: assembly


def stencil(a):
    out = []
    for vs in paths(a):
        cls, anc = [], []
        for (i, j) in PAIRS5:
            c, an = eclass(vs[i], vs[j])
            cls.append(int(c))
            anc.append(tuple(int(z) for z in an))
        out.append({"cls": cls, "anc": anc, "vs": vs})
    return out


def triangles(sten):
    """Distinct triangle types, translated so the componentwise minimum is the origin."""
    seen = {}
    for T in sten:
        for tri in itertools.combinations(range(5), 3):
            V = [T["vs"][i] for i in tri]
            mm = tuple(min(v[q] for v in V) for q in range(4))
            V0 = tuple(sorted(tuple(v[q] - mm[q] for q in range(4)) for v in V))
            if V0 in seen:
                continue
            cls, anc = [], []
            for (i, j) in ((0, 1), (1, 2), (0, 2)):
                c, an = eclass(V0[i], V0[j])
                cls.append(int(c))
                anc.append(tuple(int(z) for z in an))
            seen[V0] = {"cls": cls, "anc": anc,
                        "span": tuple(max(v[q] for v in V0) for q in range(3))}
    return list(seen.values())


_sh, _th = {}, {}


def sim_H(cls10):
    key = tuple(cls10)
    if key not in _sh:
        _sh[key] = m._fd_hessian(m._simplex_grad, [m.CLASS_ELL[c] for c in cls10], m.FD_H)
    return _sh[key]


def tri_H(cls3):
    key = tuple(cls3)
    if key not in _th:
        _th[key] = m._fd_hessian(m._area_grad, [m.CLASS_ELL[c] for c in cls3], m.FD_H)
    return _th[key]


def assemble(L, LT, sten):
    """Tick-resolved second-variation form on a spatially open box, tick periodic."""
    idx = {}
    for c, d in enumerate(DIRS):
        for x in itertools.product(range(L), repeat=3):
            if all(x[q] + d[q] <= L - 1 for q in range(3)):
                for t in range(LT):
                    idx[(c, x, t)] = len(idx)
    Q = np.zeros((len(idx), len(idx)))

    def put(H, cls, anc, bx, bt, k):
        sl = [idx[(cls[i], tuple(bx[q] + anc[i][q] for q in range(3)),
                   md(bt + anc[i][3], LT))] for i in range(k)]
        for i in range(k):
            for j in range(k):
                Q[sl[i], sl[j]] += H[i, j]

    for T in sten:
        H = sim_H(T["cls"])
        for bx in itertools.product(range(L - 1), repeat=3):
            for bt in range(LT):
                put(H, T["cls"], T["anc"], bx, bt, 10)
    for T in triangles(sten):
        HA = tri_H(T["cls"])
        sp = T["span"]
        for bx in itertools.product(*[range(L - sp[q]) for q in range(3)]):
            for bt in range(LT):
                put(HA, T["cls"], T["anc"], bx, bt, 3)
    keys = [None] * len(idx)
    for ky, i in idx.items():
        keys[i] = ky
    return keys, Q


SIGNED = []
for _perm in itertools.permutations(range(3)):
    for _sg in itertools.product((1, -1), repeat=3):
        _A = np.zeros((3, 3), dtype=np.int64)
        for _i in range(3):
            _A[_i, _perm[_i]] = _sg[_i]
        SIGNED.append(_A)
PROPER = [A for A in SIGNED if round(float(np.linalg.det(A))) == 1]


def extents(keys, sel):
    """Spatial diameter of the smallest box holding both slots' site supports."""
    sup = []
    for i in sel:
        x = keys[i][1]
        d = DIRS[keys[i][0]]
        sup.append([x, tuple(x[q] + d[q] for q in range(3))])
    E = np.zeros((len(sel), len(sel)), dtype=np.int64)
    for a in range(len(sel)):
        for b in range(len(sel)):
            P = sup[a] + sup[b]
            E[a, b] = max(max(p[q] for p in P) - min(p[q] for p in P) for q in range(3))
    return E


def keymap(keys, L, LT, A, k):
    """Relabelling of the slot variables by a signed axis permutation and a tick shift."""
    off = np.array([(L - 1) if A[q].min() < 0 else 0 for q in range(3)], dtype=np.int64)
    pos = dict((ky, i) for i, ky in enumerate(keys))
    mp = np.empty(len(keys), dtype=np.int64)
    for ky, j in pos.items():
        d = DIRS[ky[0]]
        Rw = A @ np.array(d[:3])
        nds = np.abs(Rw)
        cp = DIDX[(int(nds[0]), int(nds[1]), int(nds[2]), d[3])]
        xp = tuple(int(z) for z in (A @ np.array(ky[1]) + off + np.minimum(Rw, 0)))
        ky2 = (cp, xp, md(ky[2] + k, LT))
        if ky2 not in pos:
            return None
        mp[pos[ky2]] = j
    return mp


def nsym(keys, L, LT, M):
    n = 0
    for A in SIGNED:
        for k in range(LT):
            mp = keymap(keys, L, LT, A, k)
            if mp is not None and np.abs(M[np.ix_(mp, mp)] - M).max() < SYM_TOL:
                n += 1
                break
    return n


def nlabels(keys, L, LT, M):
    reps = []
    for A in PROPER:
        mp = keymap(keys, L, LT, A, 0)
        Mg = M[np.ix_(mp, mp)]
        if not any(np.abs(Mg - R).max() < SYM_TOL for R in reps):
            reps.append(Mg)
    return len(reps)


def split(keys):
    fw = np.array([sum(DIRS[ky[0]][:3]) for ky in keys])
    return np.where(fw <= 1)[0], np.where(fw >= 2)[0]


def schur(Q, A, D):
    """Eliminate the exceeding slots, discarding the flat directions of their block."""
    w, V = np.linalg.eigh(Q[np.ix_(D, D)])
    ker = np.abs(w) < FLAT_TOL
    inv = np.where(ker, 0.0, 1.0 / np.where(ker, 1.0, w))
    QAD = Q[np.ix_(A, D)]
    return w, V, ker, inv, Q[np.ix_(A, A)] - (QAD @ V) @ (inv[:, None] * (V.T @ QAD.T))


def fro(M):
    return float(np.sqrt(float((M * M).sum())))


keys3, Q3 = assemble(3, 2, stencil((0, 0, 0)))
A3, D3 = split(keys3)
EQ3 = extents(keys3, list(range(len(keys3))))
qbey = float(np.abs(Q3[EQ3 >= 2]).max())

chk("assembled_form_is_cell_local", int(EQ3.max()) >= 2 and qbey == 0.0,
    "no coupling of the assembled form reaches past one cell; largest entry there {0:.6e}".format(
        qbey))
chk("partition_sizes", (len(keys3), len(A3), len(D3)) == (446, 270, 176),
    "446 slot variables split into 270 adjacency-admissible and 176 exceeding")

flat = {}
for (L, LT) in ((3, 2), (3, 3), (4, 2)):
    kk, QQ = assemble(L, LT, stencil((0, 0, 0)))
    AA, DD = split(kk)
    w, V, ker, inv, S = schur(QQ, AA, DD)
    live = np.abs(w[~ker])
    dec = float(max(np.linalg.norm(QQ[np.ix_(AA, DD)] @ V[:, j]) for j in np.where(ker)[0]))
    flat[(L, LT)] = (int(ker.sum()), LT * (L - 1) ** 3, float(np.abs(w[ker]).max()), dec,
                     float(live.min()), float(live.max() / live.min()))

chk("exceeding_block_flat_count_law", all(flat[k][0] == flat[k][1] for k in flat),
    "flat directions of the exceeding block number one per cell per tick: {0}".format(
        ", ".join("L={0} LT={1} gives {2}".format(k[0], k[1], flat[k][0]) for k in sorted(flat))))
chk("flat_directions_are_decoupled",
    all(flat[k][2] < FLAT_TOL and flat[k][3] < 1.0e-4 for k in flat),
    "flat eigenvalues {0}; their coupling to the admissible slots {1}".format(
        bound(max(flat[k][2] for k in flat), FLAT_TOL),
        bound(max(flat[k][3] for k in flat), 1.0e-4)))
chk("live_block_is_well_conditioned",
    all(flat[k][4] > 1.0e-2 and flat[k][5] < 1.0e4 for k in flat),
    "softest live eigenvalue {0:.4e} and {1:.4e}; condition number {2:.2e} and {3:.2e}".format(
        flat[(3, 2)][4], flat[(4, 2)][4], flat[(3, 2)][5], flat[(4, 2)][5]))

w3, V3, ker3, inv3, S3 = schur(Q3, A3, D3)
gen = np.random.default_rng(20260803)
xv = gen.standard_normal(len(A3))
zv = np.zeros(len(keys3))
zv[A3] = xv
zv[D3] = -(V3 @ (inv3 * (V3.T @ (Q3[np.ix_(A3, D3)].T @ xv))))
rhs = float(zv @ Q3 @ zv)
rel = abs(float(xv @ S3 @ xv) - rhs) / abs(rhs)
relp = abs(float(xv @ (S3 + 1.0e-2 * np.eye(len(A3))) @ xv) - rhs) / abs(rhs)

chk("schur_stationarity_identity", rel < 1.0e-12,
    "the eliminated form reproduces the stationary value of the full form, deviation {0}".format(
        bound(rel, 1.0e-12)))
chk("schur_stationarity_rejector", relp > 1.0e-4,
    "a uniformly shifted eliminated form breaks that identity at {0:.3e}".format(relp))

rows = {}
for (L, LT) in ((3, 2), (4, 2)):
    kk, QQ = assemble(L, LT, stencil((0, 0, 0)))
    AA, DD = split(kk)
    w, V, ker, inv, S = schur(QQ, AA, DD)
    QAA = QQ[np.ix_(AA, AA)]
    E = extents(kk, AA)
    tS = fro(S)
    sh = dict((int(e), fro(S[E == e]) / tS) for e in sorted(set(E.flatten())))
    kA = [kk[i] for i in AA]
    rows[L] = (1.0 - (fro(QAA) / fro(QQ)) ** 2, sh, float(np.abs(S[E >= 2]).max()),
               nsym(kk, L, LT, QQ), nlabels(kk, L, LT, QQ),
               nsym(kA, L, LT, QAA), nlabels(kA, L, LT, QAA),
               nsym(kA, L, LT, S), nlabels(kA, L, LT, S))

chk("deletion_horn_discarded_share",
    0.5 < rows[3][0] < 0.6 and 0.5 < rows[4][0] < 0.6,
    "deleting the exceeding slots discards {0} of the form at L=3 and {1} at L=4".format(
        f3(rows[3][0]), f3(rows[4][0])))
chk("elimination_horn_generates_range",
    rows[3][1][2] > 0.2 and rows[4][1][2] + rows[4][1][3] > 0.3,
    "eliminated form past one cell: {0} at L=3; {1} at range 2 and {2} at range 3 at L=4".format(
        f3(rows[3][1][2]), f3(rows[4][1][2]), f3(rows[4][1][3])))
chk("range_is_generated_not_inherited", qbey == 0.0 and rows[3][2] > 1.0,
    "largest past-cell entry: assembled form {0:.6e}, eliminated form {1:.3f}".format(
        qbey, rows[3][2]))
chk("cell_local_share_of_eliminated_form",
    abs(rows[3][1][0] - 0.400) < 0.002 and abs(rows[3][1][1] - 0.886) < 0.002,
    "eliminated form at L=3 carries {0} on-site and {1} at range 1".format(
        f3(rows[3][1][0]), f3(rows[3][1][1])))
chk("frame_label_of_the_full_form",
    (rows[3][3], rows[3][4], rows[4][3], rows[4][4]) == (6, 8, 6, 8),
    "full form: symmetry count 6 and 8 frame labels at both box sizes")
chk("frame_label_survives_deletion",
    (rows[3][5], rows[3][6], rows[4][5], rows[4][6]) == (6, 8, 6, 8),
    "deleted form: symmetry count 6 and 8 frame labels at both box sizes")
chk("frame_label_survives_elimination",
    (rows[3][7], rows[3][8], rows[4][7], rows[4][8]) == (6, 8, 6, 8),
    "eliminated form: symmetry count 6 and 8 frame labels at both box sizes")

RECEIPT = {
    "slot_uses_by_footprint_weight": [uses[w] for w in range(4)],
    "distinct_slots_by_footprint_weight": [dcen[w] for w in range(4)],
    "spatial_axis_face_body": [spat[1], spat[2], spat[3]],
    "nondegenerate_corner_4_simplices": len(SIMS),
    "exceeding_floor_by_tick_split": [nfloor[k] for k in (1, 2, 3, 4)],
    "spatial_floor_by_tick_split": [sfloor[k] for k in (1, 2, 3, 4)],
    "stencil_exceeding_by_tick_split": [sorted(kex[k])[0] for k in (1, 2, 3, 4)],
    "facet_corner_tetrahedra": len(TET),
    "facet_corner_dissections": len(SOLS),
    "facet_dissection_exceeding_floor": dna,
    "global_corner_stencil_floor": gfloor,
    "flat_directions": dict(("L{0}_LT{1}".format(k[0], k[1]), flat[k][0]) for k in sorted(flat)),
    "softest_live_eigenvalue": dict(
        ("L{0}_LT{1}".format(k[0], k[1]), "{0:.4e}".format(flat[k][4])) for k in sorted(flat)),
    "live_condition_number": dict(
        ("L{0}_LT{1}".format(k[0], k[1]), "{0:.2e}".format(flat[k][5])) for k in sorted(flat)),
    "deletion_discarded_share": {"L3": f3(rows[3][0]), "L4": f3(rows[4][0])},
    "eliminated_share_by_range": {
        "L3": dict((str(e), f3(v)) for e, v in rows[3][1].items()),
        "L4": dict((str(e), f3(v)) for e, v in rows[4][1].items())},
    "assembled_form_past_cell_entry": "{0:.6e}".format(qbey),
    "eliminated_form_past_cell_entry": "{0:.3f}".format(rows[3][2]),
    "stationarity_relative_deviation": "{0:.3e}".format(rel),
    "stationarity_rejector_deviation": "{0:.3e}".format(relp),
    "symmetry_and_labels": {"full": [rows[3][3], rows[3][4]],
                            "deleted": [rows[3][5], rows[3][6]],
                            "eliminated": [rows[3][7], rows[3][8]]},
}
print("RECEIPT " + json.dumps(RECEIPT, sort_keys=True))
print("TOTAL: PASS={0} FAIL={1}".format(PASS, FAIL))
sys.exit(1 if FAIL else 0)
