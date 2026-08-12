"""Cycle 722 -- finite oriented-diagonal stencil and projection census.

Cycles 717-721 measured an order-12 frame group and a 4-valued frame label on the
landed STATIC second-variation form.  This runner rebuilds the same assembly on the
TICK-RESOLVED complex at tick lengths 2, 3, 4 and 5 and separates three things the
static form had merged:

  (1) the declared static contractions at L={3,4}, LT={2,3} differ only by LT/2;
  (2) the frame label is 8-valued on the tick-resolved complex at the declared
      L=3, LT={2,3,5} rows and names an oriented body diagonal of the cell;
  (3) in twelve declared projection rows, the exact line stabilizer is admitted when
      the complementary stencils are numerically identified, while the exact oriented
      stabilizer is admitted when they are separated.

The eight stencils are the eight Kuhn path triangulations of the unit 4-cube, one per
oriented main diagonal, indexed by the spatial corner a in {0,1}^3 at tick 0.  The
Lattice axiom's proper cubic rotations act transitively on the declared family.  No
member is fixed by the full proper-frame action, so selecting one member is additional
input on this finite surface.  Spatial determinant, diagonal-orientation reversal,
and tick sense are kept as three separate gradings.

Everything is anchored to the landed cycle-696 compiler: the local pieces are imported
from it, and the tick-resolved assembly is required to contract onto its static form.
"""

import importlib.util
import itertools
import json
import os
import sys

import numpy as np

AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 300

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
DIDX = {d: i for i, d in enumerate(DIRS)}
PAIRS5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
CORNERS = list(itertools.product((0, 1), repeat=3))

TOL = 1.0e-9
TOL_SCALAR = 1.0e-6
CONTROL_FACTOR_SHIFT = 1.0e-3
PASS = 0
FAIL = 0
GATES = []
RECEIPT = {"controls": {"factor_shift": CONTROL_FACTOR_SHIFT},
           "tolerances": {"matrix": TOL, "reported_scalar": TOL_SCALAR}}


def md(x, n):
    """Non-negative residue; the module operator is avoided in this source."""
    return int(x - n * (x // n))


def chk(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    GATES.append({"detail": detail, "gate": name, "ok": bool(ok)})
    print("[{0}] {1}{2}".format(tag, name, (" " + detail) if detail else ""))


def bound(dev, tol=TOL):
    """Report a near-zero deviation as a bound at the pass tolerance, not as noise digits."""
    return "dev < {0:.1e}".format(tol) if dev < tol else "dev = {0:.6e}".format(dev)


# ---------------------------------------------------------------- stencil geometry

def eclass(p, r):
    """Undirected edge class: the sign of the step is absorbed into the anchor."""
    return (DIDX[tuple(abs(r[i] - p[i]) for i in range(4))],
            tuple(min(p[i], r[i]) for i in range(4)))


def eclass_wrong(p, r):
    """Rejector: keeps the first vertex as the anchor regardless of step sign."""
    return (DIDX[tuple(abs(r[i] - p[i]) for i in range(4))], tuple(p))


def stencil(a, cls_fn=eclass):
    """The 24 Kuhn path simplices whose main diagonal runs (a,0) -> (1-a,1)."""
    v0 = (a[0], a[1], a[2], 0)
    v1 = (1 - a[0], 1 - a[1], 1 - a[2], 1)
    out = []
    for perm in itertools.permutations(range(4)):
        vs = [list(v0)]
        for q in perm:
            w = list(vs[-1])
            w[q] = v1[q]
            vs.append(w)
        vs = [tuple(v) for v in vs]
        cls, anc = [], []
        for (i, j) in PAIRS5:
            c, an = cls_fn(vs[i], vs[j])
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
    k = tuple(cls10)
    if k not in _sh:
        _sh[k] = m._fd_hessian(m._simplex_grad, [m.CLASS_ELL[c] for c in cls10], m.FD_H)
    return _sh[k]


def tri_H(cls3):
    k = tuple(cls3)
    if k not in _th:
        _th[k] = m._fd_hessian(m._area_grad, [m.CLASS_ELL[c] for c in cls3], m.FD_H)
    return _th[k]


# ---------------------------------------------------------------- assembly

def vindex(L, LT):
    idx = {}
    for c, d in enumerate(DIRS):
        for x in itertools.product(range(L), repeat=3):
            if all(x[q] + d[q] <= L - 1 for q in range(3)):
                for t in range(LT):
                    idx[(c, x, t)] = len(idx)
    return idx


def assemble(L, LT, sten):
    """Tick-resolved second-variation form: spatially open box, tick periodic."""
    idx = vindex(L, LT)
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
    return idx, Q


SIGNED = []
for _perm in itertools.permutations(range(3)):
    for _sg in itertools.product((1, -1), repeat=3):
        _A = np.zeros((3, 3), dtype=np.int64)
        for _i in range(3):
            _A[_i, _perm[_i]] = _sg[_i]
        SIGNED.append(_A)
PROPER = [A for A in SIGNED if round(float(np.linalg.det(A))) == 1]
SIGNED_KEY = {tuple(int(x) for x in A.ravel()): i for i, A in enumerate(SIGNED)}


def corner_of(A, a):
    """Where a signed axis permutation sends a corner of the cell."""
    s = np.array([1 if A[q].min() < 0 else 0 for q in range(3)], dtype=np.int64)
    return tuple(int(z) for z in (A @ np.array(a) + s))


def matrix_subset_closed(indices):
    """Exact closure of a subset of the signed spatial permutation group."""
    ss = set(indices)
    return all(SIGNED_KEY[tuple(int(x) for x in (SIGNED[i] @ SIGNED[j]).ravel())] in ss
               for i in ss for j in ss)


def determinant_split(indices):
    dets = [int(round(float(np.linalg.det(SIGNED[i])))) for i in indices]
    return (dets.count(1), dets.count(-1))


SOURCE_CORNER = (0, 0, 0)
SOURCE_LINE = frozenset((SOURCE_CORNER, (1, 1, 1)))
ORIENTED_FRAME_IDS = tuple(i for i, A in enumerate(SIGNED)
                           if corner_of(A, SOURCE_CORNER) == SOURCE_CORNER)
LINE_FRAME_IDS = tuple(i for i, A in enumerate(SIGNED)
                       if frozenset((corner_of(A, SOURCE_CORNER),
                                     tuple(1 - z for z in corner_of(A, SOURCE_CORNER))))
                       == SOURCE_LINE)
REVERSING_COSET_IDS = tuple(i for i in LINE_FRAME_IDS if i not in ORIENTED_FRAME_IDS)
PROPER_FRAME_IDS = frozenset(i for i, A in enumerate(SIGNED)
                             if int(round(float(np.linalg.det(A)))) == 1)


def keymap(L, LT, keys, A, k, eps, fold, drop):
    """Relabelling of projected variables by (spatial frame, tick shift, tick sense)."""
    off = np.array([(L - 1) if A[q].min() < 0 else 0 for q in range(3)], dtype=np.int64)
    pos = {ky: i for i, ky in enumerate(keys)}
    mp = np.empty(len(keys), dtype=np.int64)
    for ky, j in pos.items():
        c, x = ky[0], ky[1]
        d = DIRS[c]
        Rw = A @ np.array(d[:3])
        nds = np.abs(Rw)
        cp = DIDX[(int(nds[0]), int(nds[1]), int(nds[2]), d[3])]
        xp = tuple(int(z) for z in (A @ np.array(x) + off + np.minimum(Rw, 0)))
        if fold:
            ky2 = (cp, xp)
        else:
            tp = md(ky[2] + k, LT) if eps > 0 else md(k - ky[2] - d[3], LT)
            ky2 = (cp, xp, tp)
        mp[pos[ky2]] = j
    return mp


def project(idx, Q, LT, fold, drop):
    ks = [ky for ky in idx if (not drop) or DIRS[ky[0]][3] == 0]
    if fold:
        out = sorted({(c, x) for (c, x, t) in ks})
        o = {ky: i for i, ky in enumerate(out)}
        P = np.zeros((len(out), Q.shape[0]))
        for (c, x, t) in ks:
            P[o[(c, x)], idx[(c, x, t)]] = 1.0
    else:
        out = sorted(ks)
        o = {ky: i for i, ky in enumerate(out)}
        P = np.zeros((len(out), Q.shape[0]))
        for ky in ks:
            P[o[ky], idx[ky]] = 1.0
    return out, P @ Q @ P.T


def symmetry_frames(L, LT, keys, QP, fold, drop, senses=(1,), frames=SIGNED):
    """Spatial frame indices admitting some declared tick relabelling."""
    out = []
    for A in frames:
        for k in range(LT):
            for e in senses:
                mp = keymap(L, LT, keys, A, k, e, fold, drop)
                if np.abs(QP[np.ix_(mp, mp)] - QP).max() < TOL:
                    out.append(SIGNED_KEY[tuple(int(x) for x in A.ravel())])
                    break
            else:
                continue
            break
    return tuple(sorted(out))


def nsym(L, LT, keys, QP, fold, drop, senses=(1,), frames=SIGNED):
    return len(symmetry_frames(L, LT, keys, QP, fold, drop, senses, frames))


def nlabels(L, LT, keys, QP, fold, drop):
    reps = []
    for A in PROPER:
        mp = keymap(L, LT, keys, A, 0, 1, fold, drop)
        Qg = QP[np.ix_(mp, mp)]
        if not any(np.abs(Qg - R).max() < TOL for R in reps):
            reps.append(Qg)
    return len(reps)


# ================================================================ gates
print("Cycle 722 -- oriented body diagonal of the assembly stencil")
print("Local pieces imported from the cycle-696 compiler; its tick length is "
      + str(m.LT) + ".")
print("")

print("-- Tick-resolved contraction onto the supplied static form --")
S0 = stencil((0, 0, 0))
chk("triangle types match the landed count",
    len(triangles(S0)) == len(m.TRI_UW),
    "mine = {0}, landed = {1}".format(len(triangles(S0)), len(m.TRI_UW)))
scale_seen = None
for L in (3, 4):
    for LT in (2, 3):
        idx, Q4 = assemble(L, LT, S0)
        st = m.static_variable_index(L, False)
        Qs = m.assemble_static_hessian(L, False)["Q"]
        C = np.zeros((len(st), Q4.shape[0]))
        for (c, x), j in st.items():
            for t in range(LT):
                C[j, idx[(c, tuple(int(z) for z in x), t)]] = 1.0
        dev = float(np.abs(C @ Q4 @ C.T - (LT / 2.0) * Qs).max())
        scale_seen = float(np.abs(Qs).max())
        chk("L={0} LT={1} contraction equals (LT/2) times the landed form".format(L, LT),
            dev < TOL, "dim = {0}, {1}".format(Q4.shape[0], bound(dev)))
        if L == 3 and LT == 2:
            bad = float(np.abs(C @ Q4 @ C.T
                               - (LT / 2.0 + CONTROL_FACTOR_SHIFT) * Qs).max())
            chk("rejector: a shifted tick-length factor is refused", bad > TOL,
                "dev = {0:.6e}".format(bad))
            RECEIPT["static_form_scale"] = scale_seen
print("Supplied static form scale {0:.6e}; all declared contractions differ".format(scale_seen))
print("only by the overall factor LT/2.")
print("")

print("-- Sign-absorbing edge classifier --")
mism = sum(1 for p, T in enumerate(S0) for i in range(10)
           if T["cls"][i] != m.CELL[p]["cls"][i]
           or tuple(T["anc"][i]) != tuple(int(z) for z in m.CELL[p]["anc"][i]))
chk("classifier reproduces the landed cell template on the source corner 000", mism == 0,
    "{0} slot mismatches over 240".format(mism))


def anchor_violations(cls_fn):
    """anchor + class direction must land on the far endpoint of every edge slot."""
    bad = 0
    for a in CORNERS:
        for T in stencil(a, cls_fn=cls_fn):
            for (i, j), c, an in zip(PAIRS5, T["cls"], T["anc"]):
                far = tuple(max(T["vs"][i][q], T["vs"][j][q]) for q in range(4))
                if tuple(an[q] + DIRS[c][q] for q in range(4)) != far:
                    bad += 1
    return bad


vg = anchor_violations(eclass)
vb = anchor_violations(eclass_wrong)
chk("every edge slot of all eight stencils satisfies the anchor law", vg == 0,
    "{0} violations over 1920 slots".format(vg))
chk("rejector: the sign-blind anchor rule breaks the anchor law", vb > 0,
    "{0} violations over 1920 slots".format(vb))
print("")

print("-- Finite stencil orbit and three distinct group gradings --")
orb8 = len({corner_of(A, (0, 0, 0)) for A in PROPER})
st8 = sum(1 for A in PROPER if corner_of(A, (0, 0, 0)) == (0, 0, 0))
line = lambda a: frozenset({a, tuple(1 - z for z in a)})
orb4 = len({line(corner_of(A, (0, 0, 0))) for A in PROPER})
st4 = sum(1 for A in PROPER if line(corner_of(A, (0, 0, 0))) == line((0, 0, 0)))
s48o = len(ORIENTED_FRAME_IDS)
s48l = len(LINE_FRAME_IDS)
chk("proper rotations act transitively on the 8 oriented diagonals", orb8 == 8,
    "orbit = {0}, stabilizer = {1}, 24/{1} = {2}".format(orb8, st8, 24 // st8))
chk("proper rotations act transitively on the 4 diagonal lines", orb4 == 4,
    "orbit = {0}, stabilizer = {1}, 24/{1} = {2}".format(orb4, st4, 24 // st4))
chk("oriented stabilizer inside the proper rotations has order 3", st8 == 3)
chk("line stabilizer inside the proper rotations has order 6 (the sextet)", st4 == 6)
chk("oriented stabilizer inside the 48 signed permutations has order 6", s48o == 6,
    "48/6 = 8 oriented labels")
chk("line stabilizer inside the 48 signed permutations has order 12", s48l == 12,
    "48/12 = 4 line labels")
chk("oriented and line stabilizers are closed exact matrix subgroups",
    matrix_subset_closed(ORIENTED_FRAME_IDS) and matrix_subset_closed(LINE_FRAME_IDS))
chk("diagonal-orientation-reversing coset has six elements",
    len(REVERSING_COSET_IDS) == 6 and
    set(LINE_FRAME_IDS) == set(ORIENTED_FRAME_IDS) | set(REVERSING_COSET_IDS))
chk("spatial determinant splits 3+3 on both diagonal-orientation classes",
    determinant_split(ORIENTED_FRAME_IDS) == (3, 3)
    and determinant_split(REVERSING_COSET_IDS) == (3, 3),
    "orientation-preserving = {0}, orientation-reversing = {1}"
    .format(determinant_split(ORIENTED_FRAME_IDS),
            determinant_split(REVERSING_COSET_IDS)))
proper_line = set(LINE_FRAME_IDS) & PROPER_FRAME_IDS
chk("proper line sextet draws three elements from each orientation class",
    len(proper_line & set(ORIENTED_FRAME_IDS)) == 3
    and len(proper_line & set(REVERSING_COSET_IDS)) == 3,
    "proper split = 3 orientation-preserving + 3 orientation-reversing")
print("Order 12 stabilizes the UNORIENTED line, order 6 the ORIENTED diagonal; the")
print("orientation-reversing coset is determinant-mixed (3 proper + 3 improper).")
print("")

print("-- Finite assembly covariance across the stencil orbit --")
reflection_rows = []
for (L, LT) in ((3, 3), (4, 2)):
    idx, _ = assemble(L, LT, S0)
    QA = {a: assemble(L, LT, stencil(a))[1] for a in CORNERS}
    keys = sorted(idx, key=lambda k: idx[k])
    worst = 0.0
    npair = 0
    for A in PROPER:
        mp = keymap(L, LT, keys, A, 0, 1, 0, 0)
        for a in CORNERS:
            worst = max(worst, float(np.abs(QA[a][np.ix_(mp, mp)] - QA[corner_of(A, a)]).max()))
            npair += 1
    chk("L={0} LT={1}: relabelling by g carries stencil a onto stencil g.a".format(L, LT),
        worst < TOL, "{0} pairs, {1}".format(npair, bound(worst)))
    sepL = min(float(np.abs(QA[(0, 0, 0)] - QA[a]).max()) for a in CORNERS[1:])
    mI = -np.eye(3, dtype=np.int64)
    sdevL = min(float(np.abs(QA[(0, 0, 0)][np.ix_(mp, mp)] - QA[(0, 0, 0)]).max())
                for mp in (keymap(L, LT, keys, mI, k, 1, 0, 0) for k in range(LT)))
    sxL = min(float(np.abs(QA[(0, 0, 0)][np.ix_(mp, mp)] - QA[(1, 1, 1)]).max())
              for mp in (keymap(L, LT, keys, mI, k, 1, 0, 0) for k in range(LT)))
    reflection_rows.append((L, LT, sxL, sdevL, sepL))
    if L == 3:
        wrong = 0.0
        for A in PROPER:
            mp = keymap(L, LT, keys, A, 0, 1, 0, 0)
            wrong = max(wrong, float(np.abs(QA[(0, 0, 0)][np.ix_(mp, mp)] - QA[(0, 0, 0)]).max()))
        chk("rejector: holding the stencil fixed under the same relabelling is refused",
            wrong > TOL, "dev = {0:.6e}".format(wrong))
        sep = sepL
        RECEIPT["stencil_separation"] = sep
        Qb = sum(QA[a] for a in CORNERS) / 8.0
        cost = float(np.abs(Qb - QA[(0, 0, 0)]).max())
        signed_average_frames = symmetry_frames(L, LT, keys, Qb, 0, 0)
        proper_average_frames = symmetry_frames(L, LT, keys, Qb, 0, 0,
                                                frames=PROPER)
        lb = nlabels(L, LT, keys, Qb, 0, 0)
        RECEIPT["orbit_average_cost"] = cost
print("")

print("-- Spatial box-centre reflection intertwiner --")
chk("the point reflection sends source corner 000 to 111",
    corner_of(-np.eye(3, dtype=np.int64), (0, 0, 0)) == (1, 1, 1))
for L, LT, sxL, sdevL, sepL in reflection_rows:
    chk("L={0} LT={1}: reflection carries stencil 000 form to stencil 111 form"
        .format(L, LT), sxL < TOL, bound(sxL))
    chk("L={0} LT={1}: fixed-stencil reflection cost equals stencil separation"
        .format(L, LT), abs(sdevL - sepL) < TOL,
        "floor = {0:.6e}, min separation = {1:.6e}".format(sdevL, sepL))
print("")

print("-- Orbit-average proper-frame invariance and signed-frame extension --")
chk("L=3 LT=3: the orbit average admits all 24 axiom proper frames",
    len(proper_average_frames) == 24, "{0} of 24".format(len(proper_average_frames)))
chk("L=3 LT=3: the finite fixture also admits all 48 signed spatial frames",
    len(signed_average_frames) == 48,
    "{0} of 48".format(len(signed_average_frames)))
chk("the orbit-averaged form carries a single frame label", lb == 1)
chk("the averaging cost is exactly half the stencil separation",
    abs(2.0 * cost - sep) < TOL_SCALAR,
    "cost = {0:.6e}, separation = {1:.6e}".format(cost, sep))
print("")

print("-- Tick-resolved finite frame-label census --")
for LT in (2, 3, 5):
    idx, _ = assemble(3, LT, S0)
    QA = {a: assemble(3, LT, stencil(a))[1] for a in CORNERS}
    dis = []
    for a in CORNERS:
        if not any(np.abs(QA[a] - R).max() < TOL for R in dis):
            dis.append(QA[a])
    keys = sorted(idx, key=lambda k: idx[k])
    nl = nlabels(3, LT, keys, QA[(0, 0, 0)], 0, 0)
    chk("LT={0}: 8 distinct stencil forms and 8 frame classes".format(LT),
        len(dis) == 8 and nl == 8,
        "dim = {0}, distinct = {1}, classes = {2}".format(len(idx), len(dis), nl))
    del QA, dis
print("")

print("-- Finite projection identification and admitted-frame census --")
VARIANTS = (("tick-resolved, all classes", 0, 0),
            ("tick-resolved, temporal dropped", 0, 1),
            ("tick-folded, all classes", 1, 0),
            ("tick-folded, temporal dropped = STATIC", 1, 1))
for LT in (2, 3, 5):
    idx, Q0 = assemble(3, LT, stencil((0, 0, 0)))
    _, Q1 = assemble(3, LT, stencil((1, 1, 1)))
    for nm, fold, drop in VARIANTS:
        keys, P0 = project(idx, Q0, LT, fold, drop)
        _, P1 = project(idx, Q1, LT, fold, drop)
        sepv = float(np.abs(P0 - P1).max())
        admitted = symmetry_frames(3, LT, keys, P0, fold, drop)
        ns = len(admitted)
        ident = sepv < TOL
        expected = LINE_FRAME_IDS if ident else ORIENTED_FRAME_IDS
        chk("LT={0} {1}".format(LT, nm), admitted == expected
            and matrix_subset_closed(admitted),
            "admitted signed spatial frames = {0} ({1}); stencils {2}".format(
                ns, "line stabilizer" if ident else "oriented stabilizer",
                "identified" if ident else "separated at {0:.6e}".format(sepv)))
        if fold == 1 and drop == 1 and LT in (2, 3):
            nlab = nlabels(3, LT, keys, P0, fold, drop)
            RECEIPT["static_labels_LT{0}".format(LT)] = nlab
    del idx, Q0, Q1
print("Identification selects the exact line stabilizer; separation selects the exact")
print("oriented stabilizer in every declared row.")
print("")

print("-- Tick fold versus temporal-class removal --")
for LT in (3, 4, 5):
    idx, Q0 = assemble(3, LT, stencil((0, 0, 0)))
    _, Q1 = assemble(3, LT, stencil((1, 1, 1)))
    keys, P0 = project(idx, Q0, LT, 0, 1)
    _, P1 = project(idx, Q1, LT, 0, 1)
    d = float(np.abs(P0 - P1).max())
    chk("LT={0}: dropping temporal classes leaves the stencils separated".format(LT),
        abs(d - 1.0) < TOL_SCALAR, "floor = {0:.6f}".format(d))
    if LT == 4:
        _, F0 = project(idx, Q0, LT, 1, 1)
        _, F1 = project(idx, Q1, LT, 1, 1)
        df = float(np.abs(F0 - F1).max())
        chk("LT=4: the tick fold identifies them where dropping does not",
            df < TOL, bound(df))
    del idx, Q0, Q1, P0, P1
print("Temporal-class dropping identifies only at tick length 2; the fold identifies")
print("at each declared tick length.  The supplied static form applies both projections.")
print("")

print("-- Diagonal-orientation reversal and tick sense --")
for LT in (2, 3, 4, 5):
    idx, Q = assemble(3, LT, S0)
    keys = sorted(idx, key=lambda k: idx[k])
    trans = symmetry_frames(3, LT, keys, Q, 0, 0, senses=(1,))
    with_reversal = symmetry_frames(3, LT, keys, Q, 0, 0, senses=(1, -1))
    chk("LT={0}: translations select the oriented stabilizer; adding tick reversal "
        "selects the line stabilizer".format(LT),
        trans == ORIENTED_FRAME_IDS and with_reversal == LINE_FRAME_IDS,
        "translations = {0}, with reversal = {1}".format(
            len(trans), len(with_reversal)))
    del idx, Q
print("")

print("-- Stencil edge-slot inventory versus nearest-neighbour adjacency --")
AXIS = {c for c, d in enumerate(DIRS) if d[3] == 0 and sum(d[:3]) == 1}
tot = sum(1 for T in S0 for c in T["cls"])
spa = sum(1 for T in S0 for c in T["cls"] if DIRS[c][3] == 0)
axc = sum(1 for T in S0 for c in T["cls"] if c in AXIS)
chk("the stencil carries 240 edge slots, 120 of them spatial",
    tot == 240 and spa == 120, "total = {0}, spatial = {1}".format(tot, spa))
chk("a large share of the spatial slots are not nearest-neighbour steps",
    axc == 72 and spa - axc == 48,
    "{0} on the six axis directions, {1} not".format(axc, spa - axc))
print("")

print("-- Static projection reproduction of the four-label census --")
chk("static form at LT=2 carries 4 frame labels", RECEIPT.get("static_labels_LT2") == 4,
    "labels = " + str(RECEIPT.get("static_labels_LT2")))
chk("static form at LT=3 carries 4 frame labels", RECEIPT.get("static_labels_LT3") == 4,
    "labels = " + str(RECEIPT.get("static_labels_LT3")))
print("")

RECEIPT["pass"] = PASS
RECEIPT["fail"] = FAIL
RECEIPT["gates"] = GATES
RECEIPT["oriented_stabilizer_48"] = s48o
RECEIPT["line_stabilizer_48"] = s48l
RECEIPT["orientation_class_determinant_splits"] = {
    "preserving": list(determinant_split(ORIENTED_FRAME_IDS)),
    "reversing": list(determinant_split(REVERSING_COSET_IDS)),
}
RECEIPT["oriented_labels"] = 8
RECEIPT["line_labels"] = 4
RECEIPT["temporal_drop_floor"] = 1.0
with open(os.path.join(ROOT, "outputs",
                       "physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02_receipt_2026-08-02.json"),
          "w") as fh:
    json.dump(RECEIPT, fh, indent=2, sort_keys=True)
    fh.write("\n")

print("TOTAL: PASS={0} FAIL={1}".format(PASS, FAIL))
sys.exit(1 if FAIL else 0)
