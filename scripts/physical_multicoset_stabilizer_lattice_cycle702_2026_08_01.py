#!/usr/bin/env python3
"""Cycle 702: the multi-coset partial-average stabilizer lattice.

Verifies that the equivariance group of a partial average of the Cycle-696
single-complex coframe pipeline over a union of right cosets of the landed D3
scope is the setwise stabilizer of that union under the four-point action on
the body diagonals: the containment direction is exact change-of-variables
algebra, the stabilizer profile by union size is 6, 4, 6, 24, and an
exhaustive subgroup census shows that no proper nonempty union can exceed
order six. Paired note:
docs/PHYSICAL_MULTICOSET_STABILIZER_LATTICE_CYCLE702_NOTE_2026-08-01.md
"""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from itertools import combinations, product as iproduct
import json
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


_STARTED = perf_counter()
ROOT = Path(__file__).resolve().parents[1]

D3_PIN = [1, 4, 9, 15, 18, 23]
ORDERS_PIN = {1: 2, 4: 2, 9: 2, 15: 3, 18: 3, 23: 1}
EDIT3 = {((1, 1, 1), (2, 1, 1)): 5}
EDIT7 = {((3, 3, 3), (4, 3, 3)): 5}
EQUIV_AMP = 0.20
BODY_DIAGONALS = {(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)}
SUBGROUP_COUNT_PIN = 30
ORDER_HIST_PIN = {1: 1, 2: 9, 3: 4, 4: 7, 6: 4, 8: 3, 12: 1, 24: 1}
KPROFILE_PIN = [6, 4, 6, 24]
L7_UNION = (0, 1)
MACHINE_TOL = 1e-12
COVAR_TOL = 1e-9
SEPARATION_FLOOR = 1e-2
WALL_BUDGET_S = 900.0

_OUT: list[str] = []
_PASS = 0
_FAIL = 0


def emit(line: str) -> None:
    _OUT.append(line)


def check(label: str, ok: bool, measured: object = "", pinned: object = "",
          shown: str = "") -> bool:
    global _PASS, _FAIL
    if len(label) > 34 or not all(c.islower() or c.isdigit() or c == "_" for c in label):
        raise ValueError("invalid check label: " + label)
    if ok:
        _PASS += 1
        emit("PASS " + label + ((" " + shown) if shown else ""))
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
    ROOT, "cycle702_c696",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
)

FRAMES = tuple(np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES)


def fidx(m):
    for k, f in enumerate(FRAMES):
        if np.array_equal(f, m):
            return k
    raise KeyError("frame not found")


MULT = [[fidx(FRAMES[a] @ FRAMES[b]) for b in range(24)] for a in range(24)]
IDENT = fidx(np.eye(3, dtype=np.int64))
INV = [next(b for b in range(24) if MULT[a][b] == IDENT) for a in range(24)]


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


def axis_of(i):
    """+1 eigenline of a half-turn, read off the column space of R + I."""
    R = FRAMES[i]
    M = R + np.eye(3, dtype=np.int64)
    col = max(range(3), key=lambda j: int(np.abs(M[:, j]).sum()))
    v = M[:, col]
    v = v // int(np.gcd.reduce(np.abs(v)))
    return canon_dir(v), bool(np.array_equal(R @ v, v))


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


def generated(seed):
    H = {IDENT} | set(seed)
    while True:
        grown = {MULT[a][b] for a in H for b in H}
        if grown <= H:
            return frozenset(H)
        H |= grown


def main() -> int:
    global _PASS, _FAIL
    _OUT.clear()
    _PASS = 0
    _FAIL = 0
    started = _STARTED

    # ---------- a block: coset and term structure, measured at L = 3 --------
    model3, sol3 = make_level(3)
    scope = [i for i in range(24)
             if c696.variable_permutation(3, model3["index"], FRAMES[i]) is not None]
    orders = {i: mat_order(FRAMES[i]) for i in scope}
    cells = {g: frozenset(MULT[d][g] for d in scope) for g in range(24)}
    cosets = sorted(set(cells.values()), key=min)
    reps = [min(c) for c in cosets]
    cindex = [next(k for k, c in enumerate(cosets) if g in c) for g in range(24)]
    sizes = [len(c) for c in cosets]
    disjoint = all(not (cosets[a] & cosets[b]) for a, b in combinations(range(4), 2))
    check("a1_cosets_partition",
          len(cosets) == 4 and sizes == [6, 6, 6, 6] and disjoint
          and sorted(set().union(*cosets)) == list(range(24)),
          (len(cosets), sizes, disjoint), (4, [6, 6, 6, 6], True),
          str(reps))
    check("a2_scope_frames_orders",
          scope == D3_PIN and orders == ORDERS_PIN, (scope, orders),
          (D3_PIN, ORDERS_PIN), str(scope))

    dom3e = c696.build_domain(3, edits=EDIT3)
    t3 = terms24(model3, sol3, dom3e, 3, EQUIV_AMP)
    within = max(float(np.max(np.abs(t3[i] - t3[j])))
                 for c in cosets for i in c for j in c)
    check("a3_within_coset_spread", within <= COVAR_TOL, within, COVAR_TOL,
          "%.6e" % within)

    tc = [np.mean([t3[g] for g in sorted(cosets[c])], axis=0) for c in range(4)]
    pair_dist = min(float(np.max(np.abs(tc[a] - tc[b])))
                    for a, b in combinations(range(4), 2))
    check("a4_inter_coset_min_distance", pair_dist >= SEPARATION_FLOOR,
          pair_dist, SEPARATION_FLOOR, "%.6e" % pair_dist)
    splits = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    split_dist = min(float(np.max(np.abs(tc[a] + tc[b] - tc[c] - tc[d])))
                     for (a, b), (c, d) in splits)
    check("a5_two_two_split_min_distance", split_dist >= SEPARATION_FLOOR,
          split_dist, SEPARATION_FLOOR, "%.6e" % split_dist)

    unions = [frozenset(s) for k in range(1, 5) for s in combinations(range(4), k)]
    proper = [C for C in unions if len(C) < 4]
    elements = {C: sorted(g for c in C for g in cosets[c]) for C in unions}
    transversal_gap = max(
        float(np.max(np.abs(x_of(model3, sol3, dom3e, 3, EQUIV_AMP, elements[C])
                            - x_of(model3, sol3, dom3e, 3, EQUIV_AMP,
                                   [reps[c] for c in sorted(C)]))))
        for C in proper)
    check("a6_transversal_agreement", transversal_gap <= COVAR_TOL,
          transversal_gap, COVAR_TOL, "%.6e" % transversal_gap)

    # ---------- b block: the four-point action dictionary -------------------
    pi = [tuple(cindex[MULT[reps[c]][u]] for c in range(4)) for u in range(24)]
    check("b1_right_mult_well_defined",
          all(cindex[MULT[g][u]] == pi[u][cindex[g]]
              for g in range(24) for u in range(24)),
          "24x24 checked", True, "576")
    check("b2_composition_law",
          all(pi[MULT[u][v]] == tuple(pi[v][pi[u][c]] for c in range(4))
              for u in range(24) for v in range(24)),
          "24x24 checked", True, "576")
    check("b3_faithful_24_permutations",
          len(set(pi)) == 24 and all(sorted(p) == [0, 1, 2, 3] for p in pi),
          len(set(pi)), 24, str(len(set(pi))))

    d0 = np.array([1, 1, 1], dtype=np.int64)
    labels = {g: canon_dir(FRAMES[g].T @ d0) for g in range(24)}
    axes = [labels[reps[c]] for c in range(4)]
    check("b4_diagonal_dictionary",
          all(len({labels[g] for g in c}) == 1 for c in cosets)
          and set(axes) == BODY_DIAGONALS and len(set(axes)) == 4
          and all(axes[pi[u][c]]
                  == canon_dir(FRAMES[u].T @ np.asarray(axes[c], dtype=np.int64))
                  for u in range(24) for c in range(4)),
          axes, sorted(BODY_DIAGONALS), "4 axes")

    # ---------- c block: exhaustive subgroup census -------------------------
    family = {generated([g]) for g in range(24)}
    rounds = 0
    while True:
        rounds += 1
        grown = {generated(set(H) | {g}) for H in family for g in range(24)}
        if grown <= family:
            break
        family |= grown
    hist: dict = {}
    for H in family:
        hist[len(H)] = hist.get(len(H), 0) + 1
    check("c1_subgroup_family_fixpoint",
          len(family) == SUBGROUP_COUNT_PIN and rounds >= 2,
          (len(family), rounds), (SUBGROUP_COUNT_PIN, ">=2"), str(len(family)))
    check("c2_order_histogram", hist == ORDER_HIST_PIN, dict(sorted(hist.items())),
          ORDER_HIST_PIN, str(sorted(hist.items())))
    check("c3_completeness_certificate",
          all(generated(set(H) | {g}) in family for H in family for g in range(24)),
          "30x24 checked", True, "720")
    check("c4_conjugation_closed",
          all(frozenset(MULT[MULT[g][h]][INV[g]] for h in H) in family
              for H in family for g in range(24)),
          "30x24 checked", True, "720")

    # ---------- d block: the stabilizer lattice -----------------------------
    def stab(C):
        return frozenset(u for u in range(24)
                         if frozenset(pi[u][c] for c in C) == frozenset(C))

    stabs = {C: stab(C) for C in unions}
    profile = [sorted({len(stabs[C]) for C in unions if len(C) == k})
               for k in (1, 2, 3, 4)]
    check("d1_stabilizer_orders", profile == [[6], [4], [6], [24]], profile,
          [[6], [4], [6], [24]], str([p[0] for p in profile]))

    def conjugator(H):
        for g in range(24):
            if frozenset(MULT[MULT[g][h]][INV[g]] for h in H) == frozenset(scope):
                return g
        return -1

    conj1 = [conjugator(stabs[frozenset([c])]) for c in range(4)]
    conj3 = [conjugator(stabs[frozenset(range(4)) - frozenset([c])]) for c in range(4)]
    check("d2_conjugate_to_d3", all(g >= 0 for g in conj1 + conj3),
          (conj1, conj3), "all conjugate to D3", str(conj1))

    pair_ok = True
    pair_axes: list = []
    for C in unions:
        if len(C) != 2:
            continue
        nontrivial = sorted(stabs[C] - {IDENT})
        traces = [int(round(float(np.trace(FRAMES[u].astype(float)))))
                  for u in nontrivial]
        info = [axis_of(u) for u in nontrivial]
        kinds = sorted(sum(1 for a in v[0] if a != 0) for v in info)
        pair_ok &= (len(nontrivial) == 3 and traces == [-1, -1, -1]
                    and all(v[1] for v in info) and kinds == [1, 2, 2])
        pair_axes.append([v[0] for v in info])
    check("d3_pair_stabilizer_geometry", pair_ok, pair_axes,
          "traces -1; axes 1 coordinate + 2 face diagonals", "1,2,2")
    check("d4_complement_duality",
          all(stabs[C] == stabs[frozenset(range(4)) - C] for C in proper),
          "14 unions checked", True, "14")
    proper_max = max(len(stabs[C]) for C in proper)
    check("d5_proper_max_order_six", proper_max == 6, proper_max, 6,
          str(proper_max))

    def orbit(H, start):
        orb = {start}
        while True:
            grown = {pi[u][c] for u in H for c in orb}
            if grown <= orb:
                return orb
            orb |= grown

    big = [H for H in family if len(H) > 6]
    check("d6_five_transitive_subgroups",
          len(big) == 5 and all(len(orbit(H, c)) == 4 for H in big for c in range(4)),
          (len(big), sorted(len(H) for H in big)), (5, [8, 8, 8, 12, 24]),
          str(sorted(len(H) for H in big)))
    singleton_orbits = sorted({tuple(sorted({len(orbit(stabs[frozenset([c])], s))
                                             for s in range(4)}))
                               for c in range(4)})
    check("d7_singleton_not_transitive", singleton_orbits == [(1, 3)],
          singleton_orbits, [(1, 3)], "1,3")

    # ---------- e block: measured equivariance equals the stabilizer --------
    defects = {C: [equiv_defect(model3, sol3, dom3e, 3, EQUIV_AMP, u, elements[C])
                   for u in range(24)] for C in unions}
    verified = 0
    e2 = 0.0
    e3 = float("inf")
    measured_profile: dict = {}
    for C in unions:
        small = frozenset(u for u in range(24) if defects[C][u] <= COVAR_TOL)
        if small <= stabs[C] and stabs[C] <= small:
            verified += 1
        measured_profile.setdefault(len(C), set()).add(len(small))
        e2 = max(e2, max(defects[C][u] for u in stabs[C]))
        outside = [defects[C][u] for u in range(24) if u not in stabs[C]]
        if outside:
            e3 = min(e3, min(outside))
    check("e1_measured_equals_stabilizer", verified == 15, verified, 15,
          "%d/15" % verified)
    check("e2_stabilizer_side_max_defect", e2 <= COVAR_TOL, e2, COVAR_TOL,
          "%.6e" % e2)
    check("e3_outside_min_defect", e3 >= SEPARATION_FLOOR, e3, SEPARATION_FLOOR,
          "%.6e" % e3)
    kprofile = [sorted(measured_profile[k]) for k in (1, 2, 3, 4)]
    check("e4_measured_k_profile",
          kprofile == [[6], [4], [6], [24]], kprofile, [[6], [4], [6], [24]],
          str(KPROFILE_PIN))
    e5 = max(equiv_defect(model3, sol3, dom3e, 3, EQUIV_AMP, u) for u in range(24))
    check("e5_full_average_defect", e5 <= MACHINE_TOL, e5, MACHINE_TOL,
          "%.6e" % e5)

    # ---------- f block: L = 7 spot on a two-coset union ---------------------
    model7, sol7 = make_level(7)
    dom7e = c696.build_domain(7, edits=EDIT7)
    c7 = frozenset(L7_UNION)
    sub7 = sorted(g for c in c7 for g in cosets[c])
    d7v = [equiv_defect(model7, sol7, dom7e, 7, EQUIV_AMP, u, sub7)
           for u in range(24)]
    small7 = frozenset(u for u in range(24) if d7v[u] <= COVAR_TOL)
    check("f1_l7_measured_equals_stab",
          small7 <= stabs[c7] and stabs[c7] <= small7, sorted(small7),
          sorted(stabs[c7]), str(sorted(small7)))
    f_in = max(d7v[u] for u in stabs[c7])
    f_out = min(d7v[u] for u in range(24) if u not in stabs[c7])
    check("f2_l7_two_sided_margin",
          f_in <= COVAR_TOL and f_out >= SEPARATION_FLOOR, (f_in, f_out),
          (COVAR_TOL, SEPARATION_FLOOR), "%.6e %.6e" % (f_in, f_out))

    # ---------- g block: discipline -----------------------------------------
    elapsed = perf_counter() - started
    check("g1_wall_under_budget", elapsed < WALL_BUDGET_S, round(elapsed, 2),
          WALL_BUDGET_S, "%.2fs" % elapsed)

    summary = {
        "cycle": 702,
        "elapsed_sec": round(elapsed, 2),
        "scope_frames": scope,
        "scope_orders": orders,
        "coset_cells": [sorted(c) for c in cosets],
        "coset_reps": reps,
        "coset_axes": [",".join(str(a) for a in v) for v in axes],
        "within_coset_spread": "%.6e" % within,
        "inter_coset_min_distance": "%.6e" % pair_dist,
        "two_two_split_min_distance": "%.6e" % split_dist,
        "transversal_agreement": "%.6e" % transversal_gap,
        "subgroups": len(family),
        "order_histogram": dict(sorted(hist.items())),
        "orders_above_six": sorted(len(H) for H in big),
        "stab_profile_by_k": [p[0] for p in profile],
        "conjugators_k1": conj1,
        "conjugators_k3": conj3,
        "unions_verified": "%d/15" % verified,
        "measured_profile_by_k": [p[0] for p in kprofile],
        "stab_side_max_defect": "%.6e" % e2,
        "outside_min_defect": "%.6e" % e3,
        "full_average_max_defect": "%.6e" % e5,
        "l7_union": sorted(c7),
        "l7_stab": sorted(stabs[c7]),
        "l7_stab_side_max": "%.6e" % f_in,
        "l7_outside_min": "%.6e" % f_out,
        "equiv_amp": EQUIV_AMP,
    }
    prospective_pass = _PASS + 1
    summary["pass"] = prospective_pass
    summary["fail"] = _FAIL
    summary_line = "SUMMARY_JSON " + json.dumps(summary, sort_keys=True,
                                                separators=(",", ":"))
    total_line = f"TOTAL: PASS={prospective_pass} FAIL={_FAIL}"
    # Reserve the not-yet-emitted g2 line (its own shown value is at most five
    # digits, over-reserved on purpose), the summary line and the total line.
    reserved = (len("PASS g2_stdout_under_6000") + 1 + 5 + 1 + len(summary_line)
                + 1 + len(total_line) + 1)
    n_stdout = sum(len(s) + 1 for s in _OUT) + reserved
    check("g2_stdout_under_6000", n_stdout < 6000, n_stdout, 6000, str(n_stdout))
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
            "physical_multicoset_stabilizer_lattice_cycle702"
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
