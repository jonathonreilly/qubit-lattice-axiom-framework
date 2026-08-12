#!/usr/bin/env python3
"""Cycle 708 -- conditional signed-stabilizer classifier for a supplied K map.

Self-contained runner for the paired note
PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02.

It loads the landed Cycle-696 open-coframe K endpoint compiler by path and
re-measures every fact the finite battery uses: the exact group algebra of the 48
signed permutation matrices, the decorated stabilizer of each battery domain, the
exact state collapse on lawful cosets, rho bit-equality, the pointwise
constant-sign transport law on four declared edit domains, the measured multiset
classification of all 24 proper frames, four wrong-model rejectors, and the
inversion-pair corollaries. The general group classifier is conditional on that
transport premise; this runner does not promote its finite battery to an
arbitrary-edit-set theorem. Nothing is imported from sibling work; every number
below is produced by this run.

Physical scope guard: the axiom symmetry group is the 24 proper cubic rotations.
The 48 signed permutation matrices are used as COMPUTATIONAL BOOKKEEPING; the
improper (det -1) half are computational identities of the compiled chain, never
symmetries.  The floor VALUES printed here are measured, not derived.
"""

import importlib.util
import itertools
import json
import os
import sys
import time

import numpy as np

# ------------------------------------------------------------------ identity
NOTE_BASENAME = (
    "PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02.md")
RUNNER_BASENAME = (
    "physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02.py")
RECEIPT_BASENAME = (
    "physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02"
    "_receipt_2026-08-02.json")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE_BASENAME = "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02.md",
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

# ------------------------------------------------------------------ declared constants
AMP = 0.05              # insertion amplitude; must sit in the regime where no
                        # battery chain clips its coframe (multi-edit domains
                        # clip from ~0.10 up; the no-clip gates enforce this)
SIZES = (3, 7)          # open-box sizes; wrap is off everywhere
WRAP = False

CLASS_HIT = 1.0e-5      # multiset distance BELOW this counts as matching a sign
CLASS_MISS = 1.0e-3     # both distances AT OR ABOVE this counts as broken
#                         the open interval between the two is a forbidden gap
TOL_PLUS = 1.0e-10      # plus-branch bound (lawful defect, pointwise and multiset)
TOL_MINUS = 1.0e-7      # minus / both-branch bound
TOL_BROKEN = 1.0e-3     # smallest admissible broken-frame distance
SEP_BOUND = 1.0e7       # smallest admissible off-class-distance / worst-lawful-floor ratio
TIME_BUDGET = 900.0

T0 = time.time()

# ------------------------------------------------------------------ gate tally
PASS = 0
FAIL = 0


def gate(condition):
    """Count one discriminating gate.  Returns the boolean unchanged."""
    global PASS, FAIL
    if bool(condition):
        PASS += 1
    else:
        FAIL += 1
    return bool(condition)


def verdict(ok):
    return "PASS" if ok else "FAIL"


def fmt(value):
    return f"{float(value):.1e}"


def fmt_or_none(value):
    return "none" if value is None else fmt(value)


# ------------------------------------------------------------------ module load
_spec = importlib.util.spec_from_file_location(
    "c696m", os.path.join(ROOT, "scripts", MODULE_BASENAME))
c696 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c696)

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
FRAME_KEY = {m.tobytes(): i for i, m in enumerate(FRAMES)}


# ------------------------------------------------------------------ signed permutation algebra
def build_g48():
    """All 3x3 signed permutation matrices, in a fixed construction order."""
    out = []
    for order in itertools.permutations(range(3)):
        base = np.zeros((3, 3), dtype=np.int64)
        for row, col in enumerate(order):
            base[row, col] = 1
        for signs in itertools.product((1, -1), repeat=3):
            out.append(np.diag(np.asarray(signs, dtype=np.int64)) @ base)
    return out


G48 = build_g48()
G48_KEY = {m.tobytes(): i for i, m in enumerate(G48)}
IDENT = np.eye(3, dtype=np.int64)
MINUS_IDENT = -IDENT


def det_int(mat):
    return int(round(float(np.linalg.det(mat))))


def sp_data(mat):
    """Row permutation and row signs of a signed permutation matrix."""
    rows = [int(np.argmax(np.abs(mat[i]))) for i in range(3)]
    signs = [int(mat[i, rows[i]]) for i in range(3)]
    return tuple(rows), tuple(signs)


def cs_sign(mat):
    """+1 / -1 for a constant-sign element of G48; None otherwise."""
    _, signs = sp_data(mat)
    if all(s == 1 for s in signs):
        return 1
    if all(s == -1 for s in signs):
        return -1
    return None


SO_IDX = [i for i, m in enumerate(G48) if det_int(m) == 1]
CS_IDX = [i for i, m in enumerate(G48) if cs_sign(m) is not None]
CS_PROPER_IDX = [i for i in CS_IDX if det_int(G48[i]) == 1]
CS_PROPER_FRAMES = sorted(FRAME_KEY[G48[i].tobytes()] for i in CS_PROPER_IDX)


def msd(field_a, field_b):
    """Multiset distance: max gap between the two sorted value lists."""
    return float(np.max(np.abs(np.sort(np.ravel(field_a)) - np.sort(np.ravel(field_b)))))


# ------------------------------------------------------------------ battery
def battery(size):
    """Centre-anchored integer edit sets; keys are directed away from the anchor."""
    half = (size - 1) // 2
    ctr = (half, half, half)

    def out(step):
        return tuple(ctr[i] + step[i] for i in range(3))

    plus_x, plus_y, plus_z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    minus_x = (-1, 0, 0)
    return ctr, [
        ("one_edit", "(c,c+ex):5",
         {(ctr, out(plus_x)): 5}),
        ("two_distinct_axis_edits", "(c,c+ex):5 (c,c+ey):7",
         {(ctr, out(plus_x)): 5, (ctr, out(plus_y)): 7}),
        ("three_distinct_axis_edits", "(c,c+ex):5 (c,c+ey):7 (c,c+ez):11",
         {(ctr, out(plus_x)): 5, (ctr, out(plus_y)): 7, (ctr, out(plus_z)): 11}),
        ("inversion_pair", "(c,c+ex):5 (c,c-ex):5",
         {(ctr, out(plus_x)): 5, (ctr, out(minus_x)): 5}),
    ]


NAMES = (
    "one_edit",
    "two_distinct_axis_edits",
    "three_distinct_axis_edits",
    "inversion_pair",
)


# =====================================================================
# G-A  group algebra (exact integer, size-independent)
# =====================================================================
print("Cycle 708 conditional signed-stabilizer classifier for a supplied K map")
print(f"note {NOTE_BASENAME}")
print("battery one-edit, two-distinct-axis-edits, three-distinct-axis-edits, "
      "and inversion-pair; sizes 3 and 7")

_a1 = gate(len(G48) == 48 and len(G48_KEY) == 48 and len(SO_IDX) == 24
           and {G48[i].tobytes() for i in SO_IDX} == set(FRAME_KEY))
print(f"group_order G48 order {len(G48)} distinct {len(G48_KEY)} proper {len(SO_IDX)} "
      f"equals module FRAMES set {verdict(_a1)}")

_cs_closed = True
_n_products = 0
for _i in CS_IDX:
    for _j in CS_IDX:
        _n_products += 1
        _cs_closed &= cs_sign(G48[_i] @ G48[_j]) is not None
_a2 = gate(len(CS_IDX) == 12 and _cs_closed and _n_products == 144)
print(f"constant_sign_closure CS order {len(CS_IDX)} closed under all {_n_products} "
      f"products {verdict(_a2)}")

_a3 = gate(len(CS_PROPER_IDX) == 6 and CS_PROPER_FRAMES == [1, 4, 9, 15, 18, 23])
print(f"constant_sign_proper CS_proper order {len(CS_PROPER_IDX)} FRAMES indices "
      f"{CS_PROPER_FRAMES} {verdict(_a3)}")

_sx_mult = True
for _i in CS_IDX:
    for _j in CS_IDX:
        _sx_mult &= cs_sign(G48[_i] @ G48[_j]) == cs_sign(G48[_i]) * cs_sign(G48[_j])
_a4 = gate(_sx_mult)
print(f"sign_character sx multiplicative on all {_n_products} CS pairs {verdict(_a4)}")


# =====================================================================
# per-size measurement
# =====================================================================
def stabilizer_indices(dom):
    """Stab48(D) recomputed by decorated-fingerprint equality, never hardcoded."""
    key = c696.domain_key(dom)
    return [i for i, mat in enumerate(G48)
            if c696.domain_key(c696.apply_frame_to_domain(dom, mat)) == key]


def coset_signs(frame, stab):
    """Sorted (G48 index, sx) list for (g . Stab48) intersect CS."""
    hits = []
    for si in stab:
        hi = G48_KEY[(frame @ G48[si]).tobytes()]
        sgn = cs_sign(G48[hi])
        if sgn is not None:
            hits.append((hi, sgn))
    return sorted(set(hits))


def predicted_class(frame, stab):
    signs = sorted({s for _, s in coset_signs(frame, stab)})
    if signs == [-1, 1]:
        return "both"
    if signs == [1]:
        return "plus"
    if signs == [-1]:
        return "minus"
    return "broken"


def run_size(size):
    """One open-box size: assemble, solve, and measure the whole battery."""
    ctr, sets = battery(size)
    model = c696.assemble_static_hessian(size, wrap=WRAP)
    sol = c696.sector_solve(model)
    sites = list(itertools.product(range(size), repeat=3))
    cache = {}
    # Every gated K value must come from an unclipped principal coframe: the clip
    # branch in metric_and_coframe is a guard, never a smoothing a gate may rest on.
    clip = {"chains": 0, "clipped": 0, "pd_min": None}

    def chain(dom):
        """rho -> b -> eps -> coframe -> K, cached on the exact decorated fingerprint."""
        key = c696.domain_key(dom)
        if key not in cache:
            rho = c696.rho_vector(dom, model["site_index"])
            eps = c696.response(model, sol, rho @ model["G"])["eps"]
            mc = c696.metric_and_coframe(size, AMP * eps, model["index"])
            clip["chains"] += 1
            clip["clipped"] += int(bool(mc["clip_used"]))
            low = float(np.min(mc["pd_min"]))
            if clip["pd_min"] is None or low < clip["pd_min"]:
                clip["pd_min"] = low
            cache[key] = (np.asarray(c696.k_field(mc["e_clipped"])["K"]), rho)
        return cache[key]

    out = {}
    for name, label, edits in sets:
        dom = c696.build_domain(size, edits=edits)
        base_k, base_rho = chain(dom)
        stab = stabilizer_indices(dom)
        cs_stab = [i for i in stab if cs_sign(G48[i]) is not None]
        has_minus = any(cs_sign(G48[i]) == -1 for i in cs_stab)
        has_neg_ident = any(np.array_equal(G48[i], MINUS_IDENT) for i in stab)
        product_set = {(G48[ci] @ G48[si]).tobytes() for ci in CS_IDX for si in stab}
        formula = len(CS_IDX) * len(stab) // len(cs_stab)

        profile = {"plus": 0, "minus": 0, "both": 0, "broken": 0}
        floors = {"plus": None, "minus": None, "both": None}
        broken_min = None
        gap_hits = 0
        agreement = 0
        collapse_ok = True
        rho_ok = True
        n_lawful_pairs = 0
        reps = {}
        wrong_sign = {"plus": None, "minus": None}
        measured = []

        for fi in range(24):
            frame = FRAMES[fi]
            image = c696.apply_frame_to_domain(dom, frame)
            image_k, image_rho = chain(image)
            dist_plus = msd(image_k, base_k)
            dist_minus = msd(image_k, -base_k)
            for dist in (dist_plus, dist_minus):
                if not (dist < CLASS_HIT or dist >= CLASS_MISS):
                    gap_hits += 1
            if dist_plus < CLASS_HIT and dist_minus < CLASS_HIT:
                seen = "both"
                floors["both"] = max(floors["both"] or 0.0, dist_plus, dist_minus)
            elif dist_plus < CLASS_HIT:
                seen = "plus"
                floors["plus"] = max(floors["plus"] or 0.0, dist_plus)
                wrong_sign["plus"] = (dist_minus if wrong_sign["plus"] is None
                                      else min(wrong_sign["plus"], dist_minus))
            elif dist_minus < CLASS_HIT:
                seen = "minus"
                floors["minus"] = max(floors["minus"] or 0.0, dist_minus)
                wrong_sign["minus"] = (dist_plus if wrong_sign["minus"] is None
                                       else min(wrong_sign["minus"], dist_plus))
            else:
                seen = "broken"
                low = min(dist_plus, dist_minus)
                broken_min = low if broken_min is None else min(broken_min, low)
            profile[seen] += 1
            measured.append(seen)
            if seen == predicted_class(frame, stab):
                agreement += 1

            hits = coset_signs(frame, stab)
            for hi, want in hits:
                n_lawful_pairs += 1
                rep = G48[hi]
                rep_dom = c696.apply_frame_to_domain(dom, rep)
                # rho recomputed fresh from the collapsed link state, never via the
                # chain cache: the cache is keyed on domain_key, so a cached read
                # would compare the image rho against itself.
                rep_rho = c696.rho_vector(rep_dom, model["site_index"])
                collapse_ok &= c696.domain_key(rep_dom) == c696.domain_key(image)
                rho_ok &= bool(np.array_equal(rep_rho, image_rho))
                reps[hi] = want

        point = {"plus": None, "minus": None}
        for hi in sorted(reps):
            want = reps[hi]
            smap = c696.frame_site_map(size, G48[hi])
            rep_k, _ = chain(c696.apply_frame_to_domain(dom, G48[hi]))
            worst = 0.0
            for site in sites:
                worst = max(worst, abs(float(rep_k[smap[site]]) - want * float(base_k[site])))
            branch = "plus" if want == 1 else "minus"
            point[branch] = max(point[branch] or 0.0, worst)

        corollary = None
        if name == "inversion_pair":
            smap = c696.frame_site_map(size, MINUS_IDENT)
            anti = 0.0
            for site in sites:
                anti = max(anti, abs(float(base_k[smap[site]]) + float(base_k[site])))
            corollary = {"neg_ident_in_stab": has_neg_ident,
                         "palindrome": msd(base_k, -base_k),
                         "centre_value": abs(float(base_k[ctr])),
                         "antisymmetry": anti}

        out[name] = {
            "label": label, "stab": stab, "cs_stab": cs_stab, "has_minus": has_minus,
            "product_order": len(product_set), "formula": formula,
            "predicted": [predicted_class(FRAMES[fi], stab) for fi in range(24)],
            "measured": measured, "profile": profile, "agreement": agreement,
            "floors": floors, "broken_min": broken_min, "gap_hits": gap_hits,
            "collapse_ok": collapse_ok, "rho_ok": rho_ok,
            "n_lawful_pairs": n_lawful_pairs, "n_reps": len(reps),
            "point": point, "wrong_sign": wrong_sign, "corollary": corollary,
        }
    out["coframe_clip"] = clip
    return out


EXPECT_STAB = {
    "one_edit": 8,
    "two_distinct_axis_edits": 2,
    "three_distinct_axis_edits": 1,
    "inversion_pair": 16,
}
EXPECT_CS_STAB = {
    "one_edit": 2,
    "two_distinct_axis_edits": 1,
    "three_distinct_axis_edits": 1,
    "inversion_pair": 4,
}
EXPECT_MINUS = {
    "one_edit": False,
    "two_distinct_axis_edits": False,
    "three_distinct_axis_edits": False,
    "inversion_pair": True,
}

RESULTS = {}
SEPMIN = {}
for _size in SIZES:
    RESULTS[_size] = run_size(_size)
    res = RESULTS[_size]

    ok = all(gate(len(res[n]["stab"]) == EXPECT_STAB[n]) for n in NAMES)
    orders = " ".join(f"{n} {len(res[n]['stab'])}" for n in NAMES)
    print(f"stabilizer_orders L={_size} Stab48 orders {orders} {verdict(ok)}")

    ok = all(gate(len(res[n]["cs_stab"]) == EXPECT_CS_STAB[n]
                  and res[n]["has_minus"] == EXPECT_MINUS[n]) for n in NAMES)
    orders = " ".join(f"{len(res[n]['cs_stab'])}" for n in NAMES)
    minus = " ".join(("yes" if res[n]["has_minus"] else "no") for n in NAMES)
    print(f"stabilizer_intersections L={_size} CS^Stab orders {orders} "
          f"minus-sign member {minus} {verdict(ok)}")

    ok = all(gate(res[n]["product_order"] == res[n]["formula"]) for n in NAMES)
    orders = " ".join(f"{res[n]['product_order']}" for n in NAMES)
    forms = " ".join(f"{res[n]['formula']}" for n in NAMES)
    print(f"product_counting L={_size} CS.Stab set orders {orders} "
          f"equal formula {forms} {verdict(ok)}")

    cl = res["coframe_clip"]
    ok = gate(cl["clipped"] == 0 and cl["pd_min"] is not None and cl["pd_min"] > 0.0)
    print(f"coframe_unclipped L={_size} principal coframe unclipped on all "
          f"{cl['chains']} chains "
          f"pd_min {fmt_or_none(cl['pd_min'])} {verdict(ok)}")

    ok = all(gate(res[n]["collapse_ok"]) for n in NAMES)
    pairs = " ".join(f"{res[n]['n_lawful_pairs']}" for n in NAMES)
    print(f"state_collapse L={_size} state collapse over every lawful representative "
          f"{pairs} {verdict(ok)}")

    ok = all(gate(res[n]["rho_ok"]) for n in NAMES)
    print(f"rho_equality L={_size} rho bit-equality over the same representatives "
          f"{verdict(ok)}")

    ok = True
    for n in NAMES:
        pt = res[n]["point"]
        ok &= gate((pt["plus"] is None or pt["plus"] <= TOL_PLUS)
                   and (pt["minus"] is None or pt["minus"] <= TOL_MINUS))
    reps_n = " ".join(f"{res[n]['n_reps']}" for n in NAMES)
    wp = max((res[n]["point"]["plus"] or 0.0) for n in NAMES)
    wm = max((res[n]["point"]["minus"] or 0.0) for n in NAMES)
    print(f"pointwise_transport L={_size} distinct representatives {reps_n} "
          f"worst plus {fmt(wp)} "
          f"minus {fmt(wm)} {verdict(ok)}")

    for n in NAMES:
        r = res[n]
        prof = "/".join(str(r["profile"][k]) for k in ("plus", "minus", "both", "broken"))
        pred = {"plus": 0, "minus": 0, "both": 0, "broken": 0}
        for cls in r["predicted"]:
            pred[cls] += 1
        pstr = "/".join(str(pred[k]) for k in ("plus", "minus", "both", "broken"))
        ok = gate(r["agreement"] == 24 and r["gap_hits"] == 0 and prof == pstr)
        print(f"class_agreement L={_size} {n} measured {prof} predicted {pstr} "
              f"agreement {r['agreement']}/24 {verdict(ok)}")

    for n in NAMES:
        r = res[n]
        fl = r["floors"]
        held = [v for v in (fl["plus"], fl["minus"], fl["both"]) if v is not None]
        r["worst_floor"] = max(held) if held else 0.0
        ok = gate((fl["plus"] is None or fl["plus"] <= TOL_PLUS)
                  and (fl["minus"] is None or fl["minus"] <= TOL_MINUS)
                  and (fl["both"] is None or fl["both"] <= TOL_MINUS)
                  and (r["broken_min"] is None or r["broken_min"] >= TOL_BROKEN))
        r["separation"] = None
        if r["broken_min"] is not None and r["worst_floor"] > 0.0:
            r["separation"] = r["broken_min"] / r["worst_floor"]
        print(f"branch_separation L={_size} {n} floors plus {fmt_or_none(fl['plus'])} "
              f"minus {fmt_or_none(fl['minus'])} both {fmt_or_none(fl['both'])} "
              f"broken {fmt_or_none(r['broken_min'])} "
              f"sep {fmt_or_none(r['separation'])} {verdict(ok)}")

    # ---- G-D rejectors -------------------------------------------------
    two_edit = "two_distinct_axis_edits"
    stab24 = [i for i in RESULTS[_size][two_edit]["stab"] if det_int(G48[i]) == 1]
    proper_only = sum(1 for fi in range(24)
                      if predicted_class(FRAMES[fi], stab24) != "broken")
    full_lawful = 24 - res[two_edit]["profile"]["broken"]
    res[two_edit]["proper_only"] = proper_only
    ok = gate(proper_only == 6 and full_lawful == 12 and full_lawful - proper_only == 6)
    print(f"proper_only_rejector L={_size} lawful {proper_only} vs measured "
          f"{full_lawful} on two_distinct_axis_edits mismatch "
          f"{full_lawful - proper_only} {verdict(ok)}")

    det_wrong = sum(1 for cls in res["one_edit"]["measured"] if cls != "plus")
    ok = gate(det_wrong == 12 and all(det_int(FRAMES[fi]) == 1 for fi in range(24)))
    print(f"determinant_sign_rejector L={_size} misclassifies {det_wrong} of 24 "
          f"on one_edit "
          f"{verdict(ok)}")

    for n in ("one_edit", "three_distinct_axis_edits"):
        ws = res[n]["wrong_sign"]
        vals = [v for v in (ws["plus"], ws["minus"]) if v is not None]
        ok = gate(bool(vals) and min(vals) >= TOL_BROKEN)
        wsep = None
        if vals and res[n]["worst_floor"] > 0.0:
            wsep = min(vals) / res[n]["worst_floor"]
        res[n]["wrong_sign_sep"] = wsep
        print(f"wrong_sign_rejector L={_size} {n} minimum wrong-sign distance "
              f"on plus frames {fmt_or_none(ws['plus'])} "
              f"minus-frame {fmt_or_none(ws['minus'])} sep {fmt_or_none(wsep)} {verdict(ok)}")

    # ---- G-E symmetric-pair corollaries --------------------------------
    cor = res["inversion_pair"]["corollary"]
    ok = gate(cor["neg_ident_in_stab"])
    print(f"inversion_stabilizer L={_size} -I in Stab48(inversion_pair) "
          f"{cor['neg_ident_in_stab']} {verdict(ok)}")
    e2 = gate(cor["palindrome"] <= TOL_MINUS)
    e3 = gate(cor["centre_value"] <= TOL_MINUS)
    e4 = gate(cor["antisymmetry"] <= TOL_MINUS)
    print(f"inversion_corollaries L={_size} inversion_pair palindrome "
          f"{fmt(cor['palindrome'])} centre "
          f"{fmt(cor['centre_value'])} antisymmetry {fmt(cor['antisymmetry'])} "
          f"{verdict(e2 and e3 and e4)}")

    # ---- G-F battery-wide class-separation margin ----------------------
    seps = [res[n]["separation"] for n in NAMES if res[n]["separation"] is not None]
    seps += [res[n].get("wrong_sign_sep")
             for n in ("one_edit", "three_distinct_axis_edits")
             if res[n].get("wrong_sign_sep") is not None]
    SEPMIN[_size] = min(seps)
    ok = gate(SEPMIN[_size] >= SEP_BOUND)
    print(f"separation_floor L={_size} smallest off-class distance over worst lawful floor "
          f"{fmt(SEPMIN[_size])} across {len(seps)} rows {verdict(ok)}")

# ---- Size-independence of the decorated stabilizer ----------------------
_ok = all(gate(RESULTS[SIZES[0]][n]["stab"] == RESULTS[SIZES[1]][n]["stab"])
          for n in NAMES)
print("size_independence Stab48 member index lists equal at L=3 and L=7 "
      f"for all four domains {verdict(_ok)}")

# ---- D4 sgn-set single-valuedness (exact integer, size-independent) -----
_single = {}
_ok = True
for _n in ("one_edit", "two_distinct_axis_edits", "three_distinct_axis_edits"):
    _stab = RESULTS[SIZES[0]][_n]["stab"]
    _cnt = 0
    _good = True
    for _fi in range(24):
        _hits = coset_signs(FRAMES[_fi], _stab)
        if not _hits:
            continue
        _cnt += 1
        _good &= len({s for _, s in _hits}) == 1
    _single[_n] = _cnt
    _ok &= gate(_good)
_counts = " ".join(
    f"{_n} {_single[_n]}"
    for _n in ("one_edit", "two_distinct_axis_edits", "three_distinct_axis_edits")
)
print(f"sign_single_valuedness on every lawful frame {_counts} {verdict(_ok)}")

# ------------------------------------------------------------------ receipt
def domain_receipt(rec):
    fl, pt = rec["floors"], rec["point"]
    pred = {"plus": 0, "minus": 0, "both": 0, "broken": 0}
    for cls in rec["predicted"]:
        pred[cls] += 1
    order = ("plus", "minus", "both", "broken")
    return {
        "edits": rec["label"],
        "stab48_order": len(rec["stab"]),
        "cs_stab_order": len(rec["cs_stab"]),
        "cs_stab_has_minus_sign": bool(rec["has_minus"]),
        "cs_stab_product_order": rec["product_order"],
        "product_formula": rec["formula"],
        "predicted_profile": [pred[k] for k in order],
        "measured_profile": [rec["profile"][k] for k in order],
        "agreement": rec["agreement"],
        "forbidden_gap_hits": rec["gap_hits"],
        "lawful_pairs": rec["n_lawful_pairs"],
        "distinct_representatives": rec["n_reps"],
        "floor_plus": fmt_or_none(fl["plus"]),
        "floor_minus": fmt_or_none(fl["minus"]),
        "floor_both": fmt_or_none(fl["both"]),
        "broken_minimum": fmt_or_none(rec["broken_min"]),
        "worst_lawful_floor": fmt_or_none(rec["worst_floor"]),
        "broken_over_floor": fmt_or_none(rec["separation"]),
        "pointwise_plus": fmt_or_none(pt["plus"]),
        "pointwise_minus": fmt_or_none(pt["minus"]),
    }


RECEIPT = {
    "note": NOTE_BASENAME,
    "runner": RUNNER_BASENAME,
    "sizes": list(SIZES),
    "response_amplitude": fmt(AMP),
    "group_algebra": {
        "g48_order": len(G48),
        "proper_order": len(SO_IDX),
        "cs_order": len(CS_IDX),
        "cs_proper_order": len(CS_PROPER_IDX),
        "cs_proper_frame_indices": CS_PROPER_FRAMES,
    },
    "domains": {f"L{s}": {n: domain_receipt(RESULTS[s][n]) for n in NAMES}
                for s in SIZES},
    "rejectors": {
        "proper_only_lawful_two_distinct_axis_edits":
            RESULTS[SIZES[0]]["two_distinct_axis_edits"]["proper_only"],
        "full_classifier_lawful_two_distinct_axis_edits":
            24 - RESULTS[SIZES[0]]["two_distinct_axis_edits"]["profile"]["broken"],
        "proper_only_mismatch_two_distinct_axis_edits":
            (24 - RESULTS[SIZES[0]]["two_distinct_axis_edits"]["profile"]["broken"])
            - RESULTS[SIZES[0]]["two_distinct_axis_edits"]["proper_only"],
        "det_model_misclassified_one_edit": sum(
            1 for cls in RESULTS[SIZES[0]]["one_edit"]["measured"] if cls != "plus"),
        "wrong_sign_distance": {
            f"L{s}": {n: {"plus_frame": fmt_or_none(RESULTS[s][n]["wrong_sign"]["plus"]),
                          "minus_frame": fmt_or_none(RESULTS[s][n]["wrong_sign"]["minus"]),
                          "over_floor": fmt_or_none(RESULTS[s][n]["wrong_sign_sep"])}
                      for n in ("one_edit", "three_distinct_axis_edits")}
            for s in SIZES},
        "sgn_set_single_valued_lawful_frames": _single,
    },
    "corollaries_symmetric_pair": {
        f"L{s}": {
            "neg_identity_in_stab48": bool(
                RESULTS[s]["inversion_pair"]["corollary"]["neg_ident_in_stab"]),
            "palindrome_defect": fmt(
                RESULTS[s]["inversion_pair"]["corollary"]["palindrome"]),
            "centre_value": fmt(
                RESULTS[s]["inversion_pair"]["corollary"]["centre_value"]),
            "antisymmetry_defect": fmt(
                RESULTS[s]["inversion_pair"]["corollary"]["antisymmetry"]),
        } for s in SIZES},
    "class_separation": {f"L{s}": fmt(SEPMIN[s]) for s in SIZES},
    "coframe_clip": {
        f"L{s}": {"chains": RESULTS[s]["coframe_clip"]["chains"],
                  "clipped": RESULTS[s]["coframe_clip"]["clipped"],
                  "pd_min": fmt_or_none(RESULTS[s]["coframe_clip"]["pd_min"])}
        for s in SIZES},
    "tolerances": {"class_hit": fmt(CLASS_HIT), "class_miss": fmt(CLASS_MISS),
                   "plus_bound": fmt(TOL_PLUS), "minus_bound": fmt(TOL_MINUS),
                   "broken_bound": fmt(TOL_BROKEN),
                   "separation_bound": fmt(SEP_BOUND)},
    "gates": {"pass": PASS, "fail": FAIL},
}

with open(os.path.join(ROOT, "outputs", RECEIPT_BASENAME), "w") as fh:
    fh.write(json.dumps(RECEIPT, sort_keys=True, indent=2))
    fh.write("\n")

if time.time() - T0 > TIME_BUDGET:
    print("TIME_BUDGET_EXCEEDED")
    sys.exit(1)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
