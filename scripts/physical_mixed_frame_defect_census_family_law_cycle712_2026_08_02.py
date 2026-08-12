"""Cycle 712 -- finite mixed-frame assembly-defect family census.

Cycle `physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02`
derived the exact magnitude-4 comparator stencil behind the mixed-frame
assembly defect and recorded its signed census (entries of magnitude above 2)
as measured, not derived.  This runner certifies finite counting identities for
that census.  For each of the 18 mixed proper rotations (the complement of the
constant-sign sextet) and box sizes L in {3,4,5,6,7}, the large entries of the
defect E = Q[m,m] - Q decompose into exactly 12 signed numerical families (6
per sign), keyed by the nearest reference center in
{2, 2*sqrt(2), 2*sqrt(3), 4} (finite-difference tolerance 2e-7) and the pair
pattern of the entry pair (a, b) = (Q[m i, m j], Q[i, j]):

  swap families  -- one side of the pair vanishes (a or b below 0.5);
  wall family    -- centered near 2*sqrt(2), both sides finite, one wall pin;
  edge family    -- centered near 2, diagonal entries on wall-edge lines.

At L in {4,5,6}, every family's base-position set decomposes into unique
six-neighbor connected components, each a full product box.  Their per-axis
descriptors (growing interval [lo, L-1-hi] with fixed margins, or a pin at a
wall) are L-independent and frame-covariant.  The resulting finite counting
identities per sign are

  8(L-1)^3   in the center-4 swap family,
  8(L-1)^3   in the center-2*sqrt(3) swap family,
  12(L-1)^3 + 16(L-1)^2                in the center-2*sqrt(2) families,
  12(L-1)^3 + 8(L-1)^2(L-2) + 4(L-1)  in the center-2 families.

They are checked against the complete measured census at L in {3,4,5,6,7};
L=3 and L=7 are held out from descriptor extraction.  The rounded buckets
reproduce the Cycle-711 anchors.  The center-2 families enter the strict census
cut A > 2.0 through a positive finite-difference offset, so that cut is
deterministic on the scanned data.  Only the center-4 swap magnitude has the
upstream exact stencil derivation.  The other surd-center identifications, and
the wall and edge entry-pair magnitudes, remain finite-difference observations;
exact stencil evaluation is the named next target.  All finite identities below
are recomputed from the Cycle-696 compiler chain; a second-center gap and a
perturbed-operator rejector discriminate.
"""
from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c712", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
SPC = tuple(c696.SPATIAL_CLASSES)
DIRV = {c: np.asarray(c696.regge.DIRS15[c][:3], dtype=np.int64) for c in SPC}

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_MIXED_FRAME_DEFECT_CENSUS_FAMILY_LAW_CYCLE712_NOTE_2026-08-02.md",
    "docs/PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md",
    "docs/PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02.md",
    "scripts/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02.py",
    "scripts/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02.py",
    "outputs/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02_receipt_2026-08-02.json",
    "outputs/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02_receipt_2026-08-02.json",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

L_FIT = (4, 5, 6)          # descriptor-extraction sizes
L_ALL = (3, 4, 5, 6, 7)    # measured-census sizes (3 and 7 are extrapolation checks)
BIG = 1.5                  # family-entry threshold on |E|
CUT = 2.0                  # census cut of the landed cycle-711 note
ARG_CUT = 3.9              # argmax-family cut (center 4, next center ~3.46)
TOL_CENTER = 2e-7          # finite-difference tolerance around reference centers
PAIR_LO = 0.5              # swap-pattern threshold: vanished side of (a, b)
PAIR_HI = 10.0             # wall pair magnitudes ~5.86/8.69, edge pair ~22.2/24.2
WINDOW = 1e-7              # magnitude-2 census-entry offset window above 2.0
CENTER_GAP_FLOOR = 0.1     # distance-to-second-center rejector floor
SEXTET_BOUND = 1e-9
PERT = 1.7                 # perturbed-operator rejector step (lands between centers)

REFERENCE_CENTERS = (("two", 2.0), ("two_rt2", 2.0 * math.sqrt(2.0)),
                     ("two_rt3", 2.0 * math.sqrt(3.0)), ("four", 4.0))
UNSIGNED = (("four", "swap"), ("two_rt3", "swap"), ("two_rt2", "swap"),
            ("two_rt2", "wall"), ("two", "swap"), ("two", "edge"))
POLY = {
    ("four", "swap"): (lambda L: 8 * (L - 1) ** 3, "8(L-1)^3"),
    ("two_rt3", "swap"): (lambda L: 8 * (L - 1) ** 3, "8(L-1)^3"),
    ("two_rt2", "swap"): (lambda L: 12 * (L - 1) ** 3, "12(L-1)^3"),
    ("two_rt2", "wall"): (lambda L: 16 * (L - 1) ** 2, "16(L-1)^2"),
    ("two", "swap"): (lambda L: 12 * (L - 1) ** 3 + 8 * (L - 1) ** 2 * (L - 2),
                      "12(L-1)^3+8(L-1)^2(L-2)"),
    ("two", "edge"): (lambda L: 4 * (L - 1), "4(L-1)"),
}
BOX_SHAPE = {("four", "swap"): (8, 0), ("two_rt3", "swap"): (8, 0),
             ("two_rt2", "swap"): (12, 0), ("two_rt2", "wall"): (16, 1),
             ("two", "swap"): (20, 0), ("two", "edge"): (4, 2)}
ANCHOR = {3: (64, 224, 136), 7: (1728, 4896, 4056)}   # cycle-711 census per sign
ARGMAX_ANCHOR = {3: 128, 7: 3456}                     # cycle-711 argmax per frame

RECEIPT_NAME = ("physical_mixed_frame_defect_census_family_law_cycle712"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.1e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  The census gates compare recomputed counts
    exactly; the magnitude gates carry a second-center distance floor and a
    perturbed-operator rejector so that a wrong object cannot pass."""
    global N_PASS, N_FAIL
    ok = bool(ok)
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES[name] = {"pass": ok, "detail": detail}
    print("{} {} {}".format("PASS" if ok else "FAIL", name, detail))
    return ok


def constant_sign(R: np.ndarray) -> bool:
    nz = R[R != 0]
    return bool(np.all(nz == 1) or np.all(nz == -1))


def support(c: int) -> int:
    return int(np.abs(DIRV[c]).sum())


def dof_perm(L: int, index: dict, R: np.ndarray) -> np.ndarray:
    smap = c696.frame_site_map(L, R)
    dir2class = {tuple(int(t) for t in DIRV[c]): c for c in SPC}
    m = np.empty(len(index), dtype=np.int64)
    for (c, x), i in index.items():
        w = R @ DIRV[c]
        vp = tuple(int(t) for t in np.abs(w))
        xp = tuple(int(t) for t in (np.asarray(smap[x], dtype=np.int64) + np.minimum(w, 0)))
        m[i] = index[(dir2class[vp], xp)]
    return m


def component_product_boxes(xs):
    """Return the unique six-neighbor components if each is a full box.

    Connected components are intrinsic to the finite site set; unlike a greedy
    recursive split, this decomposition does not depend on an axis choice.
    """
    points = {tuple(int(t) for t in x) for x in xs}
    if len(points) != len(xs):
        return None
    unseen = set(points)
    boxes = []
    while unseen:
        seed = unseen.pop()
        component = {seed}
        frontier = [seed]
        while frontier:
            x = frontier.pop()
            for axis in range(3):
                for step in (-1, 1):
                    y = list(x)
                    y[axis] += step
                    yt = tuple(y)
                    if yt in unseen:
                        unseen.remove(yt)
                        component.add(yt)
                        frontier.append(yt)
        arr = np.asarray(sorted(component), dtype=np.int64)
        lo = arr.min(axis=0)
        hi = arr.max(axis=0)
        if int(np.prod(hi - lo + 1)) != len(component):
            return None
        boxes.append(tuple((int(lo[a]), int(hi[a])) for a in range(3)))
    return sorted(boxes)


def axdesc(lo: int, hi: int, L: int):
    """Per-axis descriptor: wall pin, or growing interval with fixed margins."""
    if lo == hi:
        return "P" if lo in (0, L - 1) else None
    return ("G", int(lo + (L - 1 - hi)))


def canon_boxes(boxes, L):
    """Frame-covariant canonical form: per box the sorted axis descriptors."""
    out = []
    for box in boxes:
        descs = []
        for (lo, hi) in box:
            d = axdesc(lo, hi, L)
            if d is None:
                return None
            descs.append(d)
        out.append(tuple(sorted(descs, key=repr)))
    return tuple(sorted(out, key=repr))


def predict(canon, L: int) -> int:
    tot = 0
    for box in canon:
        p = 1
        for d in box:
            p *= 1 if d == "P" else (L - d[1])
        tot += p
    return tot


def classify(av: float):
    """Return (center name, deviation, distance to second-nearest center)."""
    devs = sorted((abs(av - s), name) for name, s in REFERENCE_CENTERS)
    return devs[0][1], devs[0][0], devs[1][0]


def main() -> int:
    mixed = [g for g in range(24) if not constant_sign(FRAMES[g])]
    sextet = [g for g in range(24) if constant_sign(FRAMES[g])]
    print("== cycle 712: finite mixed-frame assembly-defect family census ==")
    print("config: fit L={} census L={} mixed_frames={} of 24 fd_step={} "
          "tol_center={} cut={} pair_cuts=({}, {})".format(
              L_FIT, L_ALL, len(mixed), fmt(c696.FD_H), fmt(TOL_CENTER),
              fmt(CUT), PAIR_LO, PAIR_HI))

    counts: dict = {}       # (L, famkey) -> set of per-frame counts
    canons: dict = {}       # (L, famkey) -> set of normalized component boxes
    keysets: dict = {}      # L -> set of per-frame famkey tuples
    censuses: dict = {}     # L -> set of per-frame rounded census tuples
    argmaxes: dict = {}     # L -> set of per-frame argmax-family sizes
    dev_max = {name: 0.0 for name, _ in REFERENCE_CENTERS}
    gap_min = float("inf")
    outliers = 0
    n_entries = 0
    two_off_lo, two_off_hi = float("inf"), -float("inf")
    two_all_above = True
    wall_vals: dict = {"lo": [], "hi": []}
    edge_vals: dict = {"lo": [], "hi": []}
    edge_diag_ok = True
    edge_cls_ok = True
    pin_ok = True
    swap_partner_max = 0.0
    wall_partner_min = float("inf")
    wall_partner_max = 0.0
    edge_partner_min = float("inf")

    sext_max = 0.0
    model3 = c696.assemble_static_hessian(3, wrap=False)
    Q3, index3 = model3["Q"], model3["index"]
    for g in sextet:
        mm = dof_perm(3, index3, FRAMES[g])
        sext_max = max(sext_max, float(np.abs(Q3[np.ix_(mm, mm)] - Q3).max()))
    check("g01_sextet_defect_zero", sext_max <= SEXTET_BOUND,
          "max defect below {} on all {} constant-sign frames".format(
              fmt(SEXTET_BOUND), len(sextet)))

    pert_outliers = None
    pert_gap = None

    for L in L_ALL:
        model = c696.assemble_static_hessian(L, wrap=False)
        Q, index = model["Q"], model["index"]
        N = len(index)
        cls_of = np.empty(N, dtype=np.int64)
        site_of = np.empty((N, 3), dtype=np.int64)
        for (c, x), i in index.items():
            cls_of[i] = c
            site_of[i] = x
        store = L in L_FIT
        for g in mixed:
            mm = dof_perm(L, index, FRAMES[g])
            E = Q[np.ix_(mm, mm)] - Q
            A = np.abs(E)
            ii, jj = np.where(A > BIG)
            fams: dict = {}
            for i, j in zip(ii, jj):
                v = float(E[i, j])
                av = float(A[i, j])
                a = float(Q[mm[i], mm[j]])
                b = float(Q[i, j])
                name, dev, second = classify(av)
                n_entries += 1
                if dev > TOL_CENTER:
                    outliers += 1
                    continue
                dev_max[name] = max(dev_max[name], dev)
                gap_min = min(gap_min, second)
                mab = min(abs(a), abs(b))
                pc = "swap" if mab < PAIR_LO else ("wall" if mab < PAIR_HI else "edge")
                if pc == "swap":
                    swap_partner_max = max(swap_partner_max, mab)
                elif pc == "wall":
                    wall_partner_min = min(wall_partner_min, mab)
                    wall_partner_max = max(wall_partner_max, mab)
                else:
                    edge_partner_min = min(edge_partner_min, mab)
                if name == "two":
                    off = av - CUT
                    two_off_lo = min(two_off_lo, off)
                    two_off_hi = max(two_off_hi, off)
                    two_all_above = two_all_above and (av > CUT)
                if pc == "wall":
                    for val in (abs(a), abs(b)):
                        wall_vals["lo" if val < 7.0 else "hi"].append(val)
                if pc == "edge":
                    edge_diag_ok = edge_diag_ok and (i == j)
                    edge_cls_ok = edge_cls_ok and (support(int(cls_of[i])) == 1
                                                   and support(int(cls_of[j])) == 1)
                    for val in (abs(a), abs(b)):
                        edge_vals["lo" if val < 23.0 else "hi"].append(val)
                famkey = (1 if v > 0 else -1, name, pc)
                d = fams.setdefault(famkey, {"n": 0, "tpl": {}})
                d["n"] += 1
                if store:
                    tpl = (int(cls_of[i]), int(cls_of[j])) + tuple(
                        int(t) for t in (site_of[j] - site_of[i]))
                    d["tpl"].setdefault(tpl, []).append(tuple(int(t) for t in site_of[i]))
            keysets.setdefault(L, set()).add(tuple(sorted(fams.keys())))
            for famkey, d in fams.items():
                counts.setdefault((L, famkey), set()).add(d["n"])
                if store:
                    allboxes = []
                    for tpl, sites in d["tpl"].items():
                        boxes = component_product_boxes(sites)
                        if boxes is None:
                            pin_ok = False
                            continue
                        cb = canon_boxes(boxes, L)
                        if cb is None:
                            pin_ok = False
                            continue
                        allboxes.extend(cb)
                    canons.setdefault((L, famkey), set()).add(
                        tuple(sorted(allboxes, key=repr)))
            vals = np.round(E[A > CUT]).astype(np.int64)
            u, c = np.unique(vals, return_counts=True)
            censuses.setdefault(L, set()).add(
                tuple(sorted(zip(u.tolist(), c.tolist()))))
            argmaxes.setdefault(L, set()).add(int((A > ARG_CUT).sum()))
            if pert_outliers is None:
                d0 = next(i for (c0, x0), i in index.items()
                          if support(c0) == 2 and x0 == (1, 1, 1))
                Q2 = Q.copy()
                Q2[d0, d0] += PERT
                E2 = Q2[np.ix_(mm, mm)] - Q2
                A2 = np.abs(E2)
                po, pg = 0, float("inf")
                for av2 in A2[A2 > BIG].tolist():
                    _, dev2, _ = classify(float(av2))
                    if dev2 > TOL_CENTER:
                        po += 1
                        pg = min(pg, dev2)
                pert_outliers, pert_gap = po, pg

    expect_keys = tuple(sorted((s, name, pc) for s in (1, -1)
                               for (name, pc) in UNSIGNED))
    check("g02_family_key_set",
          all(ks == {expect_keys} for ks in keysets.values()),
          "12 signed families = 6 unsigned x 2 signs at every L and frame")
    check("g03_no_outliers", outliers == 0,
          "all {} large entries within {} of a numerical reference center".format(
              n_entries, fmt(TOL_CENTER)))
    check("g04_frame_uniform_counts",
          all(len(v) == 1 for v in counts.values()),
          "per-family counts identical across the 18 mixed frames at every L")
    bij = all(next(iter(counts[(L, (1, name, pc))])) ==
              next(iter(counts[(L, (-1, name, pc))]))
              for L in L_ALL for (name, pc) in UNSIGNED)
    check("g05_sign_balance", bij,
          "plus and minus family counts equal at every L")
    check("g06_canon_frame_invariant",
          all(len(v) == 1 for v in canons.values()),
          "connected-component box descriptors frame-invariant at L={}".format(L_FIT))
    canon_of_signed = {}
    lstable = True
    for sign in (-1, 1):
        for (name, pc) in UNSIGNED:
            cs = [next(iter(canons[(L, (sign, name, pc))])) for L in L_FIT]
            lstable = lstable and (len(set(cs)) == 1)
            canon_of_signed[(sign, name, pc)] = cs[0]
    check("g07_canon_L_invariant", lstable,
          "both signs carry fixed margins and wall pins, independent of L")
    shape_ok = pin_ok
    for sign in (-1, 1):
        for (name, pc), (nbox, npin) in BOX_SHAPE.items():
            cb = canon_of_signed[(sign, name, pc)]
            shape_ok = shape_ok and (len(cb) == nbox)
            shape_ok = shape_ok and all(
                sum(1 for d in box if d == "P") == npin for box in cb)
    check("g08_box_shape", shape_ok,
          "both signs: boxes 8/8/12/16/20/4 with pins 0/0/0/1/0/2 per box")
    check("g09_edge_family_diagonal", edge_diag_ok and edge_cls_ok,
          "edge family is diagonal (i == j) on axis (NN) classes")
    for name, _ in REFERENCE_CENTERS:
        check("g10_center_dev_{}".format(name), dev_max[name] <= TOL_CENTER,
              "max reference-center deviation {}".format(fmt(dev_max[name])))
    check("g14_second_center_gap", gap_min >= CENTER_GAP_FLOOR,
          "distance to second-nearest center at least {}".format(fmt(gap_min)))
    check("g15_two_window", two_all_above and two_off_hi <= WINDOW,
          "magnitude-2 offsets in ({}, {}] strictly above the census cut".format(
              fmt(two_off_lo), fmt(two_off_hi)))
    wl = (min(wall_vals["lo"]), max(wall_vals["lo"]))
    wh = (min(wall_vals["hi"]), max(wall_vals["hi"]))
    check("g16_wall_pair_values",
          wl[1] - wl[0] <= WINDOW and wh[1] - wh[0] <= WINDOW,
          "wall pair magnitudes {:.12f} and {:.12f} (spreads {} / {})".format(
              wl[0], wh[0], fmt(wl[1] - wl[0]), fmt(wh[1] - wh[0])))
    el = (min(edge_vals["lo"]), max(edge_vals["lo"]))
    eh = (min(edge_vals["hi"]), max(edge_vals["hi"]))
    check("g17_edge_pair_values",
          el[1] - el[0] <= WINDOW and eh[1] - eh[0] <= WINDOW,
          "edge pair magnitudes {:.12f} and {:.12f} (spreads {} / {})".format(
              el[0], eh[0], fmt(el[1] - el[0]), fmt(eh[1] - eh[0])))
    check("g18_pair_cut_margins",
          swap_partner_max < PAIR_LO and wall_partner_min > PAIR_LO
          and wall_partner_max < PAIR_HI
          and edge_partner_min > PAIR_HI,
          "swap max {}; wall range [{}, {}]; edge min {} stay between cuts "
          "{} / {}".format(fmt(swap_partner_max), fmt(wall_partner_min),
                                           fmt(wall_partner_max),
                                           fmt(edge_partner_min),
                                           PAIR_LO, PAIR_HI))
    for (name, pc) in UNSIGNED:
        canon = canon_of_signed[(1, name, pc)]
        meas = [next(iter(counts[(L, (1, name, pc))])) for L in L_ALL]
        pred = [predict(canon, L) for L in L_ALL]
        poly = [POLY[(name, pc)][0](L) for L in L_ALL]
        check("g18_law_{}_{}".format(name, pc),
              meas == pred == poly,
              "counts(L=3..7)={} = {}".format(meas, POLY[(name, pc)][1]))
    poly_ok = all(
        predict(canon_of_signed[(sign,) + k], L) == POLY[k][0](L)
        for sign in (-1, 1) for k in POLY for L in range(3, 11)
    )
    check("g19_poly_identity", poly_ok,
          "descriptor prediction equals the stated polynomial for L=3..10")
    for L in (3, 7):
        n4, n3, n2 = ANCHOR[L]
        want = tuple(sorted([(-4, n4), (-3, n3), (-2, n2),
                             (2, n2), (3, n3), (4, n4)]))
        check("g20_census_anchor_L{}".format(L),
              censuses[L] == {want},
              "rounded census above cut = {} (cycle-711 anchor)".format(want))
    comp_ok = True
    for L in (3, 7):
        n4, n3, n2 = ANCHOR[L]
        c_of = lambda k: next(iter(counts[(L, (1,) + k)]))
        comp_ok = comp_ok and n4 == c_of(("four", "swap"))
        comp_ok = comp_ok and n3 == (c_of(("two_rt3", "swap"))
                                     + c_of(("two_rt2", "swap"))
                                     + c_of(("two_rt2", "wall")))
        comp_ok = comp_ok and n2 == (c_of(("two", "swap")) + c_of(("two", "edge")))
    check("g22_bucket_composition", comp_ok,
          "census buckets = family sums (rounded 3 mixes two numerical centers)")
    argm_ok = all(argmaxes[L] == {ARGMAX_ANCHOR[L]}
                  and ARGMAX_ANCHOR[L] == 16 * (L - 1) ** 3
                  and ARGMAX_ANCHOR[L] == 2 * next(iter(counts[(L, (1, "four", "swap"))]))
                  for L in (3, 7))
    check("g23_argmax_law", argm_ok,
          "argmax family per frame = 16(L-1)^3 = {} / {} (cycle-711 anchor)".format(
              ARGMAX_ANCHOR[3], ARGMAX_ANCHOR[7]))
    check("g24_perturbed_rejector", pert_outliers >= 1,
          "{} entries leave the reference-center set (distance {}) under a {} "
          "diagonal perturbation".format(pert_outliers, fmt(pert_gap), PERT))

    NOTES["laws_per_sign"] = {"|".join(k): POLY[k][1] for k in POLY}
    NOTES["counts_per_sign"] = {
        "|".join(k): [int(next(iter(counts[(L, (1,) + k)]))) for L in L_ALL]
        for k in POLY}
    NOTES["census_anchor"] = {str(L): list(ANCHOR[L]) for L in ANCHOR}
    NOTES["argmax_anchor"] = {str(L): ARGMAX_ANCHOR[L] for L in ARGMAX_ANCHOR}
    NOTES["center_deviation_max"] = {k: fmt(v) for k, v in dev_max.items()}
    NOTES["second_center_gap"] = fmt(gap_min)
    NOTES["pair_cut_margins"] = {
        "swap_partner_max": fmt(swap_partner_max),
        "wall_smaller_side_min": fmt(wall_partner_min),
        "wall_smaller_side_max": fmt(wall_partner_max),
        "edge_smaller_side_min": fmt(edge_partner_min),
    }
    NOTES["two_window"] = [fmt(two_off_lo), fmt(two_off_hi)]
    NOTES["wall_pair"] = ["{:.12f}".format(wl[0]), "{:.12f}".format(wh[0])]
    NOTES["edge_pair"] = ["{:.12f}".format(el[0]), "{:.12f}".format(eh[0])]
    receipt = {"cycle": 712, "gates": GATES, "notes": NOTES}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("receipt: outputs/{}".format(RECEIPT_NAME))
    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 0 if N_FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
