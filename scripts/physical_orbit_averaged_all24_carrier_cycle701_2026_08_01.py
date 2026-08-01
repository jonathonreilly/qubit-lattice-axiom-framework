#!/usr/bin/env python3
"""Cycle 701: the orbit-averaged all-24 coframe carrier.

Verifies that the uniform average of the Cycle-696 single-complex coframe
pipeline over the 24 proper cubic rotations is exactly O-equivariant, that
every partial (single-coset) average only conjugates the landed D3 scope
instead of enlarging it, and that the averaged carrier keeps the landed
positive-definiteness domain. Paired note:
docs/PHYSICAL_ORBIT_AVERAGED_ALL24_CARRIER_CYCLE701_NOTE_2026-08-01.md
"""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from itertools import product as iproduct
import json
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


_STARTED = perf_counter()
ROOT = Path(__file__).resolve().parents[1]

D3 = [1, 4, 9, 15, 18, 23]
COSET_REPS = [0, 23, 2, 3]
WITNESS_FRAMES = [0, 2, 3]
EDIT3 = {((1, 1, 1), (2, 1, 1)): 5}
EDIT7 = {((3, 3, 3), (4, 3, 3)): 5}
EQUIV_AMP = 0.20
TENSION_AMP = 0.40
SPREAD_AMPS = [0.40, 0.20, 0.10, 0.05]
PD_SCAN_N = 26
PD_SCAN_HI = 1.05
PD_BISECTIONS = 50
MACHINE_TOL = 1e-12
COVAR_TOL = 1e-9
VIOLATION_FLOOR = 0.3
WALL_BUDGET_S = 900.0

CUBIC_SPREADS_PIN = [0.33489977962932677, 0.20202937219367642,
                     0.12752360963188508, 0.07130325023123454]
S_PD_PIN = 0.4228364271
S_AVG_PIN = 0.42303983651076393
LAMBDA_MIN_PIN = 0.03227752380131965
L7_SINGLE_SPREAD_PIN = 0.4146141008085868
SYNTH_H = np.array([[0.02, 0.005, 0.007],
                    [0.005, -0.01, -0.003],
                    [0.007, -0.003, 0.015]])
SYNTH_SV_PIN = 0.874032
AXES_DEV_PIN = 7.0e-3

_OUT: list[str] = []
_PASS = 0
_FAIL = 0


def emit(line: str) -> None:
    _OUT.append(line)


def check(label: str, ok: bool, measured: object = "", pinned: object = "") -> bool:
    global _PASS, _FAIL
    if len(label) > 34 or not all(c.islower() or c.isdigit() or c == "_" for c in label):
        raise ValueError("invalid check label: " + label)
    if ok:
        _PASS += 1
        emit("PASS " + label)
    else:
        _FAIL += 1
        emit("FAIL " + label + " measured=" + str(measured) + " pinned=" + str(pinned))
    return ok


def load_module(root: Path, alias: str, relative: str):
    spec = importlib.util.spec_from_file_location(alias, root / relative)
    if spec is None or spec.loader is None:
        raise ImportError(relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


c696 = load_module(
    ROOT, "cycle701_c696",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
)

FRAMES = tuple(np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES)


def fidx(m):
    for k, f in enumerate(FRAMES):
        if np.array_equal(f, m):
            return k
    raise KeyError("frame not found")


def rotate_site(x, m, LL):
    c = np.full(3, (LL - 1) // 2, dtype=np.int64)
    return tuple(int(v) for v in (np.asarray(m, dtype=np.int64)
                                  @ (np.asarray(x) - c) + c))


def pull(hfield, i, LL):
    R = FRAMES[i].astype(float)
    out = np.zeros_like(hfield)
    for x in iproduct(range(LL), repeat=3):
        out[x] = R.T @ hfield[rotate_site(x, FRAMES[i], LL)] @ R
    return out


def push(hfield, i, LL):
    R = FRAMES[i].astype(float)
    out = np.zeros_like(hfield)
    for x in iproduct(range(LL), repeat=3):
        out[rotate_site(x, FRAMES[i], LL)] = R @ hfield[x] @ R.T
    return out


def make_level(LL):
    model = c696.assemble_static_hessian(LL, wrap=False)
    sol = c696.sector_solve(model)
    return model, sol


def eps_of(model, sol, dom):
    rho = c696.rho_vector(dom, model["site_index"])
    b = rho @ model["G"]
    return c696.response(model, sol, b)["eps"]


def hfield_of(model, sol, dom, LL, amp):
    return c696.metric_and_coframe(LL, amp * eps_of(model, sol, dom),
                                   model["index"])["h"]


_T24: dict = {}


def terms24(model, sol, dom, LL, amp):
    key = (LL, float(amp), c696.domain_key(dom))
    hit = _T24.get(key)
    if hit is not None:
        return hit
    out = []
    for i in range(24):
        dg = c696.apply_frame_to_domain(dom, FRAMES[i])
        out.append(pull(hfield_of(model, sol, dg, LL, amp), i, LL))
    _T24[key] = out
    return out


def x_of(model, sol, dom, LL, amp, subset=None):
    t = terms24(model, sol, dom, LL, amp)
    if subset is None:
        return np.mean(t, axis=0)
    return np.mean([t[i] for i in subset], axis=0)


def equiv_defect(model, sol, dom, LL, amp, r, subset=None):
    xa = x_of(model, sol, dom, LL, amp, subset)
    dr = c696.apply_frame_to_domain(dom, FRAMES[r])
    xb = x_of(model, sol, dr, LL, amp, subset)
    return float(np.max(np.abs(xb - push(xa, r, LL))))


_ORB: dict = {}


def site_orbits(LL):
    hit = _ORB.get(LL)
    if hit is not None:
        return hit
    seen = set()
    orbits = []
    for x in iproduct(range(LL), repeat=3):
        if x in seen:
            continue
        orb = {rotate_site(x, f, LL) for f in FRAMES}
        seen |= orb
        orbits.append(sorted(orb))
    _ORB[LL] = orbits
    return orbits


def orbit_spread(field, LL):
    worst = 0.0
    for orb in site_orbits(LL):
        vals = [field[x] for x in orb]
        worst = max(worst, max(vals) - min(vals))
    return worst


def logvol(hf, LL):
    out = np.zeros((LL, LL, LL))
    for x in iproduct(range(LL), repeat=3):
        out[x] = np.linalg.slogdet(np.eye(3) + hf[x])[1]
    return out


def mat_order(m):
    p = np.eye(3, dtype=np.int64)
    for k in range(1, 25):
        p = p @ np.asarray(m, dtype=np.int64)
        if np.array_equal(p, np.eye(3, dtype=np.int64)):
            return k
    return -1


def canon_dir(v):
    t = tuple(int(round(float(a))) for a in v)
    for a in t:
        if a > 0:
            return t
        if a < 0:
            return tuple(-b for b in t)
    return t


def quad_rows(dirs):
    return np.array([[v[0] * v[0], v[1] * v[1], v[2] * v[2],
                      2.0 * v[0] * v[1], 2.0 * v[0] * v[2], 2.0 * v[1] * v[2]]
                     for v in dirs], dtype=float)


def quad_recover(dirs, H):
    A = quad_rows(dirs)
    b = np.array([float(np.asarray(v, dtype=float) @ H @ np.asarray(v, dtype=float))
                  for v in dirs])
    p = np.linalg.lstsq(A, b, rcond=None)[0]
    Hrec = np.array([[p[0], p[3], p[4]],
                     [p[3], p[1], p[5]],
                     [p[4], p[5], p[2]]])
    rank = int(np.linalg.matrix_rank(A))
    sv = float(np.linalg.svd(A, compute_uv=False).min())
    return rank, sv, float(np.max(np.abs(Hrec - H)))


def pd_scan_and_bisect(predicate):
    scan = [bool(predicate(float(s))) for s in np.linspace(0.0, PD_SCAN_HI, PD_SCAN_N)]
    onsets = sum(scan[i - 1] and not scan[i] for i in range(1, PD_SCAN_N))
    lo, hi = 0.0, PD_SCAN_HI
    for _ in range(PD_BISECTIONS):
        mid = 0.5 * (lo + hi)
        if predicate(mid):
            lo = mid
        else:
            hi = mid
    return onsets, 0.5 * (lo + hi), scan


def main() -> int:
    global _PASS, _FAIL
    _OUT.clear()
    _PASS = 0
    _FAIL = 0
    started = _STARTED

    # ---------------- A block: anchors on the landed machinery -------------
    mats = [tuple(tuple(int(v) for v in row) for row in f) for f in FRAMES]
    dets = [int(round(float(np.linalg.det(f.astype(float))))) for f in FRAMES]
    check("a1_frames_distinct_det", len(set(mats)) == 24 and set(dets) == {1},
          (len(set(mats)), sorted(set(dets))), (24, [1]))
    closed = True
    for a in range(24):
        for b in range(24):
            try:
                fidx(FRAMES[a] @ FRAMES[b])
            except KeyError:
                closed = False
    check("a1_frames_closed", closed, closed, True)

    model3, sol3 = make_level(3)
    dom3 = c696.build_domain(3)
    scope = [i for i in range(24)
             if c696.variable_permutation(3, model3["index"], FRAMES[i]) is not None]
    check("a2_scope_frames", scope == D3, scope, D3)
    orders = {i: mat_order(FRAMES[i]) for i in scope}
    check("a2_scope_orders", orders == {1: 2, 4: 2, 9: 2, 15: 3, 18: 3, 23: 1},
          orders, {1: 2, 4: 2, 9: 2, 15: 3, 18: 3, 23: 1})

    eps3 = eps_of(model3, sol3, dom3)

    def single_pd(s):
        return c696.metric_and_coframe(3, s * eps3, model3["index"])["pd_mask"].all()

    onsets1, s_pd, _scan1 = pd_scan_and_bisect(single_pd)
    check("a3_single_scan_one_onset", onsets1 == 1, onsets1, 1)
    check("a4_s_pd_pin", abs(s_pd - S_PD_PIN) < 1e-8, repr(s_pd), S_PD_PIN)
    just = c696.metric_and_coframe(3, (s_pd + 1e-3) * eps3, model3["index"])
    fail_sites = sorted([int(v) for v in x] for x in np.argwhere(~just["pd_mask"]))
    check("a5_first_fail_sites",
          fail_sites == [[0, 1, 1], [1, 0, 1], [1, 1, 0],
                         [1, 1, 2], [1, 2, 1], [2, 1, 1]],
          fail_sites, [[0, 1, 1], [1, 0, 1], [1, 1, 0],
                       [1, 1, 2], [1, 2, 1], [2, 1, 1]])
    cubic_spreads = [orbit_spread(logvol(hfield_of(model3, sol3, dom3, 3, a), 3), 3)
                     for a in SPREAD_AMPS]
    check("a6_cubic_spreads_reproduce",
          all(abs(cubic_spreads[i] - CUBIC_SPREADS_PIN[i]) < MACHINE_TOL
              for i in range(4)),
          cubic_spreads, CUBIC_SPREADS_PIN)

    # ---------------- S block: coset and direction structure ---------------
    cells = {}
    for g in range(24):
        cells[g] = frozenset(fidx(FRAMES[d] @ FRAMES[g]) for d in D3)
    distinct_cells = set(cells.values())
    cell0 = sorted(cells[0])
    rep_cells = {cells[r] for r in COSET_REPS}
    covers = set().union(*distinct_cells) == set(range(24))
    check("s1_cosets_partition",
          len(distinct_cells) == 4 and all(len(c) == 6 for c in distinct_cells)
          and covers and cell0 == [0, 6, 10, 12, 19, 21] and len(rep_cells) == 4,
          (len(distinct_cells), cell0, len(rep_cells)), (4, [0, 6, 10, 12, 19, 21], 4))
    labels = {}
    for g in range(24):
        labels[g] = canon_dir(FRAMES[g].T @ np.array([1, 1, 1]))
    per_cell = {c: {labels[g] for g in c} for c in distinct_cells}
    check("s1_diagonal_labels",
          all(len(v) == 1 for v in per_cell.values())
          and len({next(iter(v)) for v in per_cell.values()}) == 4,
          sorted(sorted(v)[0] for v in per_cell.values()), "4 distinct body diagonals")

    copies = [{canon_dir(FRAMES[r] @ np.asarray(d, dtype=np.int64))
               for d in c696.SPATIAL_DIRS} for r in COSET_REPS]
    union = set().union(*copies)
    o_invariant = all({canon_dir(f @ np.asarray(cl, dtype=np.int64)) for cl in union}
                      == union for f in FRAMES)
    census: dict = {}
    for cl in union:
        mult = sum(cl in cp for cp in copies)
        key = (sum(abs(a) for a in cl), mult)
        census[key] = census.get(key, 0) + 1
    census_pin = {(1, 4): 3, (2, 2): 6, (3, 1): 4}
    total_incidence = sum(k[1] * n for k, n in census.items())
    check("s2_union_13_o_invariant",
          len(union) == 13 and o_invariant and census == census_pin
          and total_incidence == 28 == 4 * len(c696.SPATIAL_DIRS),
          (len(union), o_invariant, sorted(census.items()), total_incidence),
          (13, True, sorted(census_pin.items()), 28))

    rank7, sv7, dev7 = quad_recover(c696.SPATIAL_DIRS, SYNTH_H)
    check("s3_seven_dir_recovery",
          rank7 == 6 and abs(sv7 - SYNTH_SV_PIN) < 1e-4 and dev7 < MACHINE_TOL,
          (rank7, sv7, dev7), (6, SYNTH_SV_PIN, "<1e-12"))
    rot_ok = True
    for r in COSET_REPS:
        rd = [FRAMES[r] @ np.asarray(d, dtype=np.int64) for d in c696.SPATIAL_DIRS]
        rr, _rs, rdev = quad_recover(rd, SYNTH_H)
        rot_ok &= (rr == 6 and rdev < MACHINE_TOL)
    check("s3_rep_rotated_recovery", rot_ok, rot_ok, True)
    rank_ax, _sv_ax, dev_ax = quad_recover([(1, 0, 0), (0, 1, 0), (0, 0, 1)], SYNTH_H)
    check("s4_axes_only_rejector",
          rank_ax == 3 and abs(dev_ax - AXES_DEV_PIN) < 1e-9 and dev_ax >= 5e-3,
          (rank_ax, dev_ax), (3, AXES_DEV_PIN))

    # ---------------- H block: headline equivariance -----------------------
    rho3 = c696.rho_vector(dom3, model3["site_index"])
    src_dev3 = max(float(np.max(np.abs(
        c696.rho_vector(c696.apply_frame_to_domain(dom3, FRAMES[i]),
                        model3["site_index"]) - rho3))) for i in range(24))
    check("h1_source_o_invariant_l3", src_dev3 == 0.0, src_dev3, 0.0)

    dom3e = c696.build_domain(3, edits=EDIT3)
    h_base = hfield_of(model3, sol3, dom3e, 3, EQUIV_AMP)
    unavg = {}
    for g in WITNESS_FRAMES:
        hg = hfield_of(model3, sol3, c696.apply_frame_to_domain(dom3e, FRAMES[g]),
                       3, EQUIV_AMP)
        unavg[g] = float(np.max(np.abs(hg - push(h_base, g, 3))))
    check("h2_unaveraged_violation",
          all(v >= VIOLATION_FLOOR for v in unavg.values()),
          [round(unavg[g], 4) for g in WITNESS_FRAMES], ">=0.3")

    x24_defects = {r: equiv_defect(model3, sol3, dom3e, 3, EQUIV_AMP, r)
                   for r in WITNESS_FRAMES}
    x24_defect_max = max(x24_defects.values())
    check("h3_x24_equivariant", x24_defect_max <= MACHINE_TOL,
          x24_defect_max, MACHINE_TOL)

    t_all = terms24(model3, sol3, dom3e, 3, EQUIV_AMP)
    within = 0.0
    for i in cell0:
        for j in cell0:
            within = max(within, float(np.max(np.abs(t_all[i] - t_all[j]))))
    check("h4_within_coset_equal", within <= COVAR_TOL, within, COVAR_TOL)

    x24 = x_of(model3, sol3, dom3e, 3, EQUIV_AMP)
    x4 = x_of(model3, sol3, dom3e, 3, EQUIV_AMP, COSET_REPS)
    transversal_diff = float(np.max(np.abs(x24 - x4)))
    check("h5_transversal_reduction", transversal_diff <= COVAR_TOL,
          transversal_diff, COVAR_TOL)

    inv0 = np.linalg.inv(FRAMES[0].astype(float)).round().astype(np.int64)
    conj = sorted(fidx(inv0 @ FRAMES[d] @ FRAMES[0]) for d in D3)
    check("h6_conj_predicted", conj == [2, 4, 11, 13, 17, 23], conj,
          [2, 4, 11, 13, 17, 23])
    coset_defect = {r: equiv_defect(model3, sol3, dom3e, 3, EQUIV_AMP, r, cell0)
                    for r in range(24)}
    small = sorted(r for r in range(24) if coset_defect[r] < COVAR_TOL)
    check("h6_conj_measured_set",
          set(small) <= set(conj) and set(conj) <= set(small), small, conj)
    worst_r = max(coset_defect, key=lambda r: coset_defect[r])
    check("h6_coset_max_defect",
          coset_defect[worst_r] >= VIOLATION_FLOOR,
          (worst_r, round(coset_defect[worst_r], 7)), ">=0.3")

    h40 = hfield_of(model3, sol3, dom3, 3, TENSION_AMP)
    pulled = {r: pull(h40, r, 3) for r in COSET_REPS}
    tension = 0.0
    for a in COSET_REPS:
        for b in COSET_REPS:
            tension = max(tension, float(np.max(np.abs(pulled[a] - pulled[b]))))
    check("h7_inter_coset_tension", tension >= VIOLATION_FLOOR,
          round(tension, 7), ">=0.3")

    # ---------------- P block: spread collapse -----------------------------
    averaged_spreads = [orbit_spread(logvol(x_of(model3, sol3, dom3, 3, a), 3), 3)
                        for a in SPREAD_AMPS]
    check("p1_averaged_spread_collapse",
          all(v <= MACHINE_TOL for v in averaged_spreads),
          averaged_spreads, MACHINE_TOL)
    edit_spread = orbit_spread(
        logvol(x_of(model3, sol3, dom3e, 3, EQUIV_AMP), 3), 3)
    check("p2_edited_spread_rejector", edit_spread >= 0.1,
          round(edit_spread, 7), ">=0.1")

    # ---------------- D block: PD domain of the averaged carrier -----------
    def avg_h(s):
        hs = c696.metric_and_coframe(3, s * eps3, model3["index"])["h"]
        return np.mean([pull(hs, i, 3) for i in range(24)], axis=0)

    def avg_lambda_min(s):
        hv = avg_h(s)
        return min(float(np.linalg.eigvalsh(np.eye(3) + hv[x]).min())
                   for x in iproduct(range(3), repeat=3))

    lam040 = avg_lambda_min(TENSION_AMP)
    check("d1_avg_lambda_min_amp040", abs(lam040 - LAMBDA_MIN_PIN) < 1e-8,
          repr(lam040), LAMBDA_MIN_PIN)

    def avg_pd(s):
        return avg_lambda_min(s) > c696.COFRAME_PD_MARGIN

    onsets_avg, s_avg, _scan_avg = pd_scan_and_bisect(avg_pd)
    check("d2_avg_scan_one_onset", onsets_avg == 1, onsets_avg, 1)
    check("d2_s_avg_pin", abs(s_avg - S_AVG_PIN) < 1e-8, repr(s_avg), S_AVG_PIN)
    margin_gain = s_avg - s_pd
    check("d2_avg_domain_not_smaller", margin_gain > 1e-4,
          "%.6e" % margin_gain, ">1e-4")

    # ---------------- L7 block: size robustness ----------------------------
    model7, sol7 = make_level(7)
    dom7 = c696.build_domain(7)
    rho7 = c696.rho_vector(dom7, model7["site_index"])
    src_dev7 = max(float(np.max(np.abs(
        c696.rho_vector(c696.apply_frame_to_domain(dom7, FRAMES[i]),
                        model7["site_index"]) - rho7))) for i in range(24))
    check("l1_source_o_invariant_l7", src_dev7 == 0.0, src_dev7, 0.0)
    l7_single = orbit_spread(logvol(hfield_of(model7, sol7, dom7, 7, EQUIV_AMP), 7), 7)
    check("l2_l7_single_spread_pin", abs(l7_single - L7_SINGLE_SPREAD_PIN) < 1e-9,
          repr(l7_single), L7_SINGLE_SPREAD_PIN)
    l7_avg = orbit_spread(logvol(x_of(model7, sol7, dom7, 7, EQUIV_AMP), 7), 7)
    check("l3_l7_averaged_spread", l7_avg <= MACHINE_TOL, l7_avg, MACHINE_TOL)
    dom7e = c696.build_domain(7, edits=EDIT7)
    l4_defect = equiv_defect(model7, sol7, dom7e, 7, EQUIV_AMP, 0)
    check("l4_edit7_x24_equivariant", l4_defect <= MACHINE_TOL, l4_defect, MACHINE_TOL)
    h7b = hfield_of(model7, sol7, dom7e, 7, EQUIV_AMP)
    h7g = hfield_of(model7, sol7, c696.apply_frame_to_domain(dom7e, FRAMES[0]),
                    7, EQUIV_AMP)
    l4_unavg = float(np.max(np.abs(h7g - push(h7b, 0, 7))))
    check("l4_edit7_unaveraged_violation", l4_unavg >= 0.5, round(l4_unavg, 4), ">=0.5")

    elapsed = perf_counter() - started
    check("wall_under_budget", elapsed < WALL_BUDGET_S, round(elapsed, 2),
          WALL_BUDGET_S)

    summary = {
        "cycle": 701,
        "elapsed_sec": round(elapsed, 2),
        "s_pd": s_pd,
        "s_avg": s_avg,
        "pd_margin_gain": margin_gain,
        "lambda_min_avg_amp040": lam040,
        "scope_frames": scope,
        "scope_orders": orders,
        "conj_frames": conj,
        "coset_reps": COSET_REPS,
        "cell0": cell0,
        "union_classes": len(union),
        "census": {"%d,%d" % k: v for k, v in sorted(census.items())},
        "cubic_spreads": cubic_spreads,
        "averaged_spreads": ["%.3e" % v for v in averaged_spreads],
        "l7_single_spread": l7_single,
        "l7_averaged_spread": "%.3e" % l7_avg,
        "l7_edit_x24_defect": "%.3e" % l4_defect,
        "l7_edit_unaveraged_violation": round(l4_unavg, 4),
        "synth_min_singular": round(sv7, 6),
        "x24_defect_max": "%.3e" % x24_defect_max,
        "within_coset_spread": "%.3e" % within,
        "transversal_diff": "%.3e" % transversal_diff,
        "inter_coset_tension": round(tension, 7),
        "coset_defect_max": [worst_r, round(coset_defect[worst_r], 7)],
        "unaveraged_violation": [round(unavg[g], 4) for g in WITNESS_FRAMES],
        "edited_averaged_spread": round(edit_spread, 7),
        "axes_only_dev": dev_ax,
        "first_fail_sites": fail_sites,
    }
    prospective_pass = _PASS + 1
    summary["pass"] = prospective_pass
    summary["fail"] = _FAIL
    summary_line = "SUMMARY_JSON " + json.dumps(summary, sort_keys=True,
                                                separators=(",", ":"))
    total_line = f"TOTAL: PASS={prospective_pass} FAIL={_FAIL}"
    reserved = len("PASS stdout_under_6000") + 1 + len(summary_line) + 1 + len(total_line) + 1
    n_stdout = sum(len(s) + 1 for s in _OUT) + reserved
    check("stdout_under_6000", n_stdout < 6000, n_stdout, 6000)
    summary["pass"] = _PASS
    summary["fail"] = _FAIL
    summary_line = "SUMMARY_JSON " + json.dumps(summary, sort_keys=True,
                                                separators=(",", ":"))
    total_line = f"TOTAL: PASS={_PASS} FAIL={_FAIL}"
    _OUT.append(summary_line)
    _OUT.append(total_line)
    sys.stdout.write("\n".join(_OUT) + "\n")
    receipt_body = dict(summary)
    receipt_body["resources"] = {"elapsed_seconds": perf_counter() - started}
    receipt_body["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    receipt_body["pass_count"] = _PASS
    receipt_body["fail_count"] = _FAIL
    receipt_body["pass"] = _FAIL == 0
    if "--no-receipt" not in sys.argv:
        receipt = ROOT / "outputs" / (
            "physical_orbit_averaged_all24_carrier_cycle701"
            "_receipt_2026_08_01.json"
        )
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(
            json.dumps(receipt_body, indent=1, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
    return 0 if _FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
