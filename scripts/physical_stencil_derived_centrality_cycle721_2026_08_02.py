"""Cycle 721 -- stencil-derived centrality of the box-centre point reflection.

Class-A finite check script (stdlib + numpy only).  Cycles 717-720 MEASURED that the
static open-box assembly of the landed Cycle-696 compiler is invariant under a
twelve-element set of signed axis permutations whose proper half is a sextet, and that
the box-centre point reflection sigma commutes with all twenty-four proper frames.
This script DERIVES that group from the assembly stencil alone and then confirms the
derivation against the assembled form, in this order:

  A  the frame site map of the landed compiler is the centre conjugate
     s -> R(s - c) + c, and its translation part is exactly (I - R)c, an integer
     box-corner offset -- so the map is a signed permutation followed by a corner shift;
  B  the induced slot relabelling is therefore a group homomorphism on all forty-eight
     signed axis permutations, with the composition order fixed by an explicit rejector;
  C  sigma is the scalar -I, hence central in the matrix group; the homomorphism
     transports centrality to the slot maps, so centrality is a COROLLARY reached with
     no evaluation of the assembled form at all, and the Cycle-719 closed form for
     sigma is recovered rather than measured;
  D  the assembly stencil is the twenty-four path simplices of the base cell, every one
     of which carries the body diagonal of the four-cube; on the folded tick the set of
     signed axis permutations preserving that stencil has order twelve, and the improper
     half of it is supplied by the periodic tick identification;
  E  the derived group predicts the invariance of the assembled form at three box sizes,
     and -- the discriminating gate -- tracks deliberately mutilated stencils, where the
     derived and measured groups move together.

The six improper members are registered as computational identities of the assembled
form, not as lattice symmetries: the lattice axiom sanctions proper rotations only.

No value is read from a pinned table: every number printed here is recomputed in this
run from the landed compiler and from the stencil combinatorics.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c721", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)
regge = c696.regge

L_LIST = (3, 4, 5)
L_PAIRS = (3, 5)
SEXTET = (1, 4, 9, 15, 18, 23)
DIAG = (1, 1, 1)
BOUND_EXACT = 0.0
TOL_REL = 1.0e-8
GAP_RATIO = 1.0e3

RECEIPT_NAME = (
    "physical_stencil_derived_centrality_cycle721_2026_08_02_receipt_2026-08-02.json"
)

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
DIRV = {c: np.asarray(regge.DIRS15[c][:3], dtype=np.int64) for c in c696.SPATIAL_CLASSES}
BYDIR = {tuple(int(t) for t in v): c for c, v in DIRV.items()}
SIMPLICES = [tuple(tuple(int(t) for t in v) for v in vs)
             for vs in regge.cell_simplices((0, 0, 0, 0))]
LT = c696.LT
SIGMA = -np.eye(3, dtype=np.int64)
MIXED = np.diag([1, 1, -1]).astype(np.int64)
SHEARS = [np.asarray(m, dtype=np.int64) for m in
          ([[1, 1, 0], [0, 1, 0], [0, 0, 1]],
           [[1, 0, 0], [1, 1, 0], [0, 0, 1]],
           [[1, 0, 1], [0, 1, 0], [0, 0, 1]],
           [[1, 0, 0], [0, 1, 0], [1, 0, 1]])]


def fmt(x) -> str:
    return "{:.6e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  Every gate below is discriminating: each carries an
    explicit wrong-convention, wrong-offset, wrong-order or mutilated-stencil rejector."""
    global N_PASS, N_FAIL
    ok = bool(ok)
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES[name] = {"pass": ok, "detail": detail}
    print("{} {} {}".format("PASS" if ok else "FAIL", name, detail))
    return ok


def signed_axis_permutations() -> list:
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            A = np.zeros((3, 3), dtype=np.int64)
            for a in range(3):
                A[a, p[a]] = s[a]
            out.append(A)
    return out


B48 = signed_axis_permutations()
KEY48 = {A.tobytes(): i for i, A in enumerate(B48)}
FRAME_AT = [KEY48[np.asarray(F, dtype=np.int64).tobytes()] for F in FRAMES]


def corner_offset(L: int, A: np.ndarray) -> np.ndarray:
    """The integer translation carried by the centre conjugate: 0 or L-1 per axis."""
    return np.array([L - 1 if A[a].min() < 0 else 0 for a in range(3)], dtype=np.int64)


def slot_map(L: int, A: np.ndarray) -> np.ndarray:
    """Slot relabelling induced by the site map s -> A s + corner_offset.  An edge slot
    is (class, low corner); the image class is the non-negative representative of the
    image direction and the image low corner is the smaller endpoint."""
    index = c696.static_variable_index(L, False)
    m = np.full(len(index), -1, dtype=np.int64)
    off = corner_offset(L, A)
    for (c, x), i in index.items():
        Rw = A @ DIRV[c]
        lo = A @ np.asarray(x, dtype=np.int64) + off + np.minimum(Rw, 0)
        m[i] = index[(BYDIR[tuple(int(abs(t)) for t in Rw)],
                      (int(lo[0]), int(lo[1]), int(lo[2])))]
    return m


def fold_canon(vs) -> frozenset:
    """Canonical form of a cell simplex on the folded lattice: free spatial translation
    and, because the tick is periodic of length LT, a free tick shift."""
    mn = [min(v[m] for v in vs) for m in range(3)]
    best = None
    for k in range(LT):
        fs = frozenset((v[0] - mn[0], v[1] - mn[1], v[2] - mn[2],
                        divmod(v[3] + k, LT)[1]) for v in vs)
        key = tuple(sorted(fs))
        if best is None or key < best[0]:
            best = (key, fs)
    return best[1]


def rigid_canon(vs) -> frozenset:
    """Same, with the tick held fixed -- the unfolded comparison."""
    mn = [min(v[m] for v in vs) for m in range(3)]
    return frozenset((v[0] - mn[0], v[1] - mn[1], v[2] - mn[2], v[3]) for v in vs)


def stencil_image(vs, A):
    return [tuple(int(t) for t in (A @ np.asarray(v[:3], dtype=np.int64))) + (v[3],)
            for v in vs]


FOLD_IDX = {fold_canon(vs): p for p, vs in enumerate(SIMPLICES)}
RIGID_IDX = {rigid_canon(vs): p for p, vs in enumerate(SIMPLICES)}
RHO = [[FOLD_IDX.get(fold_canon(stencil_image(vs, A))) for vs in SIMPLICES] for A in B48]
RHO_RIGID = [[RIGID_IDX.get(rigid_canon(stencil_image(vs, A))) for vs in SIMPLICES]
             for A in B48]


def derived_stabilizer(subset, table=None) -> set:
    """Signed axis permutations that permute a template subset inside the stencil."""
    tab = RHO if table is None else table
    S = set(subset)
    return {k for k in range(48)
            if all(tab[k][p] is not None and tab[k][p] in S for p in S)}


def assemble_subset(L: int, subset) -> np.ndarray:
    """Simplex-local part of the Cycle-696 open assembly, restricted to a subset of the
    stencil templates.  With the full subset this is the simplex block of the landed
    assembly; proper subsets are deliberate mutilations used as rejectors."""
    index = c696.static_variable_index(L, False)
    vidx = c696._vidx_lookup(L, index)
    bases = c696.cell_bases(L, False)
    Q = np.zeros((len(index), len(index)))
    for p in subset:
        tmpl = c696.CELL[p]
        H = c696.simplex_local_hessian(p)
        sv = []
        for i in range(10):
            c, off = tmpl["cls"][i], tmpl["anc"][i]
            if regge.DIRS15[c][3] != 0:
                sv.append(None)
                continue
            xs = bases + np.asarray(off[:3], dtype=np.int64)
            sv.append(vidx[c696.SPATIAL_SLOT[c], xs[:, 0], xs[:, 1], xs[:, 2]])
        for i in range(10):
            if sv[i] is None:
                continue
            for j in range(10):
                if sv[j] is None:
                    continue
                m = (sv[i] >= 0) & (sv[j] >= 0)
                np.add.at(Q, (sv[i][m], sv[j][m]), H[i, j] * LT)
    return Q


def deviations(Q: np.ndarray, maps) -> list:
    return [float(np.max(np.abs(Q[np.ix_(m, m)] - Q))) for m in maps]


def section_a() -> None:
    print("-- A  the landed site map is the centre conjugate, offset (I-R)c --")
    worst_t, worst_landed, escapes, nonint, shear_bad = 0.0, 0, 0, 0, 0
    for L in L_LIST:
        cen = np.asarray(c696.box_centre(L), dtype=float)
        sites = list(itertools.product(range(L), repeat=3))
        for S in SHEARS:
            if any(abs(float(v) - round(float(v))) > 1e-12
                   for v in ((np.eye(3) - S) @ cen)):
                shear_bad += 1
        for A in B48:
            off = corner_offset(L, A)
            worst_t = max(worst_t, float(np.max(np.abs(
                off.astype(float) - (np.eye(3) - A) @ cen))))
            landed = c696.frame_site_map(L, A.astype(float))
            for s in sites:
                y = A @ np.asarray(s, dtype=np.int64) + off
                worst_landed += int(tuple(int(t) for t in y) != landed[s])
                z = A @ np.asarray(s, dtype=np.int64)
                if int(z.min()) < 0 or int(z.max()) > L - 1:
                    escapes += 1
            if any(abs(float(v) - round(float(v))) > 1e-12
                   for v in ((np.eye(3) - A) @ cen)):
                nonint += 1
    check("A1.offset_is_centre_conjugate", worst_t == BOUND_EXACT,
          "max deviation from (I-R)c over 48 frames and three box sizes {}".format(
              fmt(worst_t)))
    check("A2.reproduces_landed_site_map", worst_landed == 0,
          "site mismatch against the landed map, 48 frames x 3 sizes {}".format(
              worst_landed))
    check("A3.integer_offset_is_special", nonint == 0 and shear_bad > 0,
          "non-integer offsets among 144 frame-size pairs {} against {} for "
          "unimodular non-permutation rejectors".format(nonint, shear_bad))
    check("A4.zero_offset_rejector", escapes > 0,
          "images leaving the box when the offset is dropped {}".format(escapes))
    NOTES["offset_escapes"] = escapes


def section_b() -> None:
    print("-- B  the slot relabelling is a homomorphism --")
    for L in L_PAIRS:
        maps = [slot_map(L, A) for A in B48]
        n = len(maps[0])
        bij = sum(1 for m in maps if len(set(m.tolist())) == n and int(m.min()) >= 0)
        fwd = rev = 0
        for a in range(48):
            for b in range(48):
                c = KEY48[(B48[a] @ B48[b]).tobytes()]
                fwd += int(np.count_nonzero(maps[c] - maps[a][maps[b]]))
                rev += int(np.count_nonzero(maps[c] - maps[b][maps[a]]))
        check("B1.L{}.bijective".format(L), bij == 48,
              "bijective slot maps out of 48, slot count {}".format(n))
        check("B2.L{}.homomorphism".format(L), fwd == 0,
              "composition mismatch over 2304 ordered pairs {}".format(fwd))
        check("B3.L{}.reversed_order_rejector".format(L), rev > 0,
              "mismatch under the reversed composition order {}".format(rev))
        check("B4.L{}.maps_distinct".format(L),
              len({m.tobytes() for m in maps}) == 48,
              "distinct slot maps {}".format(len({m.tobytes() for m in maps})))


def section_c() -> None:
    print("-- C  centrality of the box-centre point reflection, with no assembled form --")
    mat = max(int(np.max(np.abs(A @ SIGMA - SIGMA @ A))) for A in B48)
    mixed_bad = sum(1 for A in B48 if int(np.max(np.abs(A @ MIXED - MIXED @ A))) != 0)
    check("C1.sigma_is_scalar_central", mat == 0,
          "max matrix commutator of -I against all 48 {}".format(mat))
    check("C2.noncentral_matrix_rejector", mixed_bad > 0,
          "frames failing to commute with a single-axis sign flip {}".format(mixed_bad))
    check("C3.sigma_involution_not_a_frame",
          int(np.max(np.abs(SIGMA @ SIGMA - np.eye(3, dtype=np.int64)))) == 0
          and SIGMA.tobytes() not in {F.tobytes() for F in FRAMES},
          "sigma squares to the identity and is not one of the 24 proper frames")
    for L in L_PAIRS:
        maps = [slot_map(L, A) for A in B48]
        s = KEY48[SIGMA.tobytes()]
        x = KEY48[MIXED.tobytes()]
        com = max(int(np.count_nonzero(maps[s][maps[a]] - maps[a][maps[s]]))
                  for a in range(48))
        comx = sum(1 for a in range(48)
                   if int(np.count_nonzero(maps[x][maps[a]] - maps[a][maps[x]])) != 0)
        index = c696.static_variable_index(L, False)
        closed = 0
        for (c, x0), i in index.items():
            w = DIRV[c]
            tgt = tuple(int(L - 1 - x0[a] - w[a]) for a in range(3))
            closed += int(maps[s][i] != index[(c, tgt)])
        check("C4.L{}.sigma_slot_central".format(L), com == 0,
              "worst slot commutator of sigma against all 48 {}".format(com))
        check("C5.L{}.noncentral_slot_rejector".format(L), comx > 0,
              "frames whose slot map fails to commute with the flip {}".format(comx))
        check("C6.L{}.closed_form_recovered".format(L), closed == 0,
              "mismatch against the landed closed form for sigma {}".format(closed))


def section_d() -> None:
    print("-- D  the stencil fixes the group, before any assembly --")
    shares = sum(1 for vs in SIMPLICES
                 if (0, 0, 0, 0) in vs and (1, 1, 1, 1) in vs)
    check("D1.templates_carry_the_body_diagonal", shares == len(SIMPLICES),
          "templates carrying the four-cube body diagonal {} of {}".format(
              shares, len(SIMPLICES)))
    full = tuple(range(len(SIMPLICES)))
    stab = derived_stabilizer(full)
    rigid = derived_stabilizer(full, RHO_RIGID)
    one = np.asarray(DIAG, dtype=np.int64)
    crit = {k for k in range(48) if len({int(t) for t in (B48[k] @ one)}) == 1}
    dets = [int(round(float(np.linalg.det(B48[k])))) for k in stab]
    proper = sorted(FRAME_AT.index(k) for k in stab if k in FRAME_AT)
    check("D2.folded_stabilizer_order", len(stab) == 12,
          "signed axis permutations preserving the stencil {}".format(len(stab)))
    check("D3.body_diagonal_criterion", stab == crit,
          "stencil stabilizer equals the set fixing the body-diagonal line, 48 of 48")
    check("D4.tick_fold_supplies_improper_half", len(rigid) == 6 and rigid < stab,
          "order without the periodic tick identification {} against {}".format(
              len(rigid), len(stab)))
    check("D5.determinant_split", dets.count(1) == 6 and dets.count(-1) == 6,
          "proper {} improper {} within the stabilizer".format(
              dets.count(1), dets.count(-1)))
    check("D6.proper_half_is_the_sextet", tuple(proper) == SEXTET,
          "proper members among the 24 landed frames {}".format(tuple(proper)))
    check("D7.coset_count", len(FRAMES) // len(proper) == 4,
          "proper frames per stabilizer member {}".format(len(FRAMES) // len(proper)))
    orbits = set()
    for p in range(len(SIMPLICES)):
        orbits.add(frozenset(RHO[k][p] for k in stab))
    check("D8.orbit_structure", len(orbits) == 2 and {len(o) for o in orbits} == {12},
          "stencil orbits under the derived group {} of size {}".format(
              len(orbits), sorted({len(o) for o in orbits})))
    hs = [c696.simplex_local_hessian(p) for p in range(len(SIMPLICES))]
    spread = max(float(np.max(np.abs(hs[p] - hs[q])))
                 for p in range(len(hs)) for q in range(len(hs)))
    classes = len({tuple(c696.CELL[p]["cls"]) for p in range(len(SIMPLICES))})
    check("D9.local_pieces_coincide", spread == BOUND_EXACT and classes == 24,
          "worst spread over the 24 local pieces {} with {} distinct class tuples".format(
              fmt(spread), classes))
    NOTES["stencil_order"] = len(stab)
    NOTES["rigid_order"] = len(rigid)


def section_e() -> None:
    print("-- E  the derived group predicts, and tracks mutilated stencils --")
    full = tuple(range(len(SIMPLICES)))
    stab = derived_stabilizer(full)
    proper_stab = {k for k in stab if k in FRAME_AT}
    for L in L_LIST:
        Q = c696.assemble_static_hessian(L, False)["Q"]
        maps = [slot_map(L, A) for A in B48]
        dev = deviations(Q, maps)
        inside = max(dev[k] for k in stab)
        outside = min(dev[k] for k in range(48) if k not in stab)
        scale = float(np.max(np.abs(Q)))
        tol = TOL_REL * max(scale, 1.0)
        measured = {k for k in range(48) if dev[k] <= tol}
        check("E1.L{}.derived_predicts_measured".format(L), measured == stab,
              "slots {} agreement 48 of 48 invariant {}".format(Q.shape[0], len(measured)))
        check("E2.L{}.separation".format(L),
              inside < tol < outside and outside >= GAP_RATIO * max(inside, 1e-300),
              "within {} floor outside {} entry max {}".format(
                  fmt(inside), fmt(outside), fmt(scale)))
        # the four-valued frame label as a coset count; a signed permutation is
        # orthogonal, so its inverse is its transpose -- no float linear algebra enters
        blocks = set()
        for gi in range(len(FRAMES)):
            k = FRAME_AT[gi]
            blocks.add(frozenset(
                gj for gj in range(len(FRAMES))
                if KEY48[(B48[k] @ B48[FRAME_AT[gj]].T).tobytes()] in proper_stab))
        qmats = [Q[np.ix_(maps[FRAME_AT[gi]], maps[FRAME_AT[gi]])]
                 for gi in range(len(FRAMES))]
        seen = []
        label = [-1] * len(FRAMES)
        for gi in range(len(FRAMES)):
            for ci, rep in enumerate(seen):
                if float(np.max(np.abs(qmats[gi] - qmats[rep]))) <= tol:
                    label[gi] = ci
                    break
            if label[gi] < 0:
                label[gi] = len(seen)
                seen.append(gi)
        cosets = {frozenset(gj for gj in range(len(FRAMES)) if label[gj] == ci)
                  for ci in range(len(seen))}
        check("E3.L{}.label_is_the_coset_count".format(L),
              len(seen) == 4 and cosets == blocks,
              "measured classes {} matching the derived cosets, block size {}".format(
                  len(seen), sorted({len(b) for b in cosets})))
    print("-- E4  mutilated stencils: derived and measured groups move together --")
    stab_full = derived_stabilizer(full)
    cases = [("full", full),
             ("single_a", (0,)),
             ("single_b", (7,)),
             ("orbit", tuple(sorted({RHO[k][0] for k in stab_full}))),
             ("half", tuple(range(12))),
             ("pair", (0, 1))]
    L = 3
    maps = [slot_map(L, A) for A in B48]
    tracked = 0
    for name, sub in cases:
        Q = assemble_subset(L, sub)
        dev = deviations(Q, maps)
        scale = float(np.max(np.abs(Q)))
        tol = TOL_REL * max(scale, 1.0)
        measured = {k for k in range(48) if dev[k] <= tol}
        der = derived_stabilizer(sub)
        ok = measured == der
        tracked += int(ok)
        check("E4.{}".format(name), ok,
              "templates {} derived {} measured {} floor {}".format(
                  len(sub), len(der), len(measured),
                  fmt(min([dev[k] for k in range(48) if k not in der],
                          default=float("nan")))))
    check("E5.stencil_tracking", tracked == len(cases),
          "mutilated stencils whose measured group equals the derived one {} of {}".format(
              tracked, len(cases)))
    NOTES["tracked_stencils"] = tracked


def main() -> int:
    print("c721 stencil-derived centrality of the box-centre point reflection")
    print("48 signed axis permutations, {} stencil templates, tick length {}".format(
        len(SIMPLICES), LT))
    section_a()
    section_b()
    section_c()
    section_d()
    section_e()

    receipt = {"box_sizes": list(L_LIST),
               "fail": N_FAIL,
               "gates": GATES,
               "notes": NOTES,
               "pass": N_PASS,
               "runner": Path(__file__).name,
               "sextet": list(SEXTET),
               "tick_length": LT}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")

    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
