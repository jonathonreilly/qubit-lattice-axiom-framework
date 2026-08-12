"""Cycle 713 -- assembly-defect weight law and complete census (open-boundary box).

Cycle `physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02`
recorded the mixed-frame assembly-defect census as measured, not derived, and
cycle `physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02`
derived the counts of the six entry families above the census cut while taking
the four defect magnitudes {2, 2*sqrt(2), 2*sqrt(3), 4} as a measured menu.
This runner derives the menu and completes the census.

Let v_i be the spatial direction vector of the coframe variable i in the
cycle-696 open compiler chain and s_i = |v_i|^2 its support (1 for the three
axis directions, 2 for the six face diagonals, 3 for the body diagonal), and
let LT = 2 be the tick length of the landed 3+1 module.  For every proper
rotation R outside the constant-sign sextet, and every scanned box size L,
EVERY resolved entry of the assembly defect E = Q[m, m] - Q, meaning
|E_ij| > 1e-9, obeys the weight law

    |E_ij| = w * LT * |v_i| * |v_j| = w * LT * sqrt(s_i s_j),   w in {1, 1/2},

with half weight w = 1/2 occurring exactly on axis-axis (support (1,1)) pairs.
The four magnitudes above the cut are the four realized values of LT|v_i||v_j|;
the support signatures (2,3), (3,2) and (3,3) are never realized.  The census
then holds at three polynomials, per mixed frame and frame-uniform:

    full weight, per sign : 48(L-1)^3 + 8(L-1)^2 + 4(L-1)
    half weight, per sign : 16(L-1)^2
    resolved entries      : 96(L-1)^3 + 48(L-1)^2 + 8(L-1)

so the finite census agrees with a cubic leading coefficient of 96, a
quadratic term, and a linear term at the scanned sizes.  No alternative
boundary re-anchoring is constructed or tested.  The cycle-711 cut at 2.0 is
exactly the full/half separator (largest half magnitude 1, smallest full
magnitude 2).
The laws are fitted on L in {3, 4, 5, 6} and tested against L = 7, 8 and 9,
which no earlier cycle measured, and against the landed cycle-711 per-sign
census totals at L = 3 and L = 7.  All computational identities below are
recomputed from the cycle-696 compiler chain in this run.  An additive
alternative LT*sqrt(s_i + s_j), a shuffled support assignment, and a
perturbed operator all fail the weight law by wide margins.
"""
from __future__ import annotations

import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c713", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

# The complete repository-source closure used by the imported Cycle-696
# compiler.  The cache binds these bytes so a transitive compiler change makes
# this result stale instead of silently reusing old output.
AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 600

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
SPC = tuple(c696.SPATIAL_CLASSES)
DIRV = {c: np.asarray(c696.regge.DIRS15[c][:3], dtype=np.int64) for c in SPC}
SUP = {c: int(np.abs(DIRV[c]).sum()) for c in SPC}
LT = int(c696.LT)

L_FIT = (3, 4, 5, 6)          # law-fitting sizes
L_HELD = (7, 8, 9)            # held-out sizes measured by no earlier cycle
L_ALL = L_FIT + L_HELD
ZERO = 1e-9                   # resolved-entry floor on |E|
TOL_W = 2e-7                  # weight-law tolerance (finite-difference scale)
CUT = 2.0                     # census cut of the landed cycle-711 note
SEXTET_BOUND = 1e-9
ADD_FLOOR = 0.5               # additive-alternative rejector floor
PERT = 1.7                    # perturbed-operator rejector step
CARRIER = 30                  # ordered class pairs carrying full-weight entries
ANCHOR_FULL = {3: 424, 7: 10680}   # cycle-711 per-sign census totals
SIG_FULL = ((1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1))
SIG_ABSENT = ((2, 3), (3, 2), (3, 3))
CARRIER_SIG = {(1, 1): 8, (1, 2): 7, (2, 1): 7, (1, 3): 2, (3, 1): 2, (2, 2): 4}
MAG_LAW = (
    ("four", 4.0, lambda L: 8 * (L - 1) ** 3, "8(L-1)^3"),
    ("two_rt3", 2.0 * math.sqrt(3.0), lambda L: 8 * (L - 1) ** 3, "8(L-1)^3"),
    ("two_rt2", 2.0 * math.sqrt(2.0),
     lambda L: 12 * (L - 1) ** 3 + 16 * (L - 1) ** 2, "12(L-1)^3+16(L-1)^2"),
    ("two", 2.0,
     lambda L: 20 * (L - 1) ** 3 - 8 * (L - 1) ** 2 + 4 * (L - 1),
     "20(L-1)^3-8(L-1)^2+4(L-1)"),
)

RECEIPT_NAME = ("physical_defect_weight_law_and_complete_census_cycle713"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.1e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  The census gates compare recomputed integer
    counts exactly; the weight-law gates carry an additive-alternative floor, a
    shuffled-support rejector and a perturbed-operator rejector, so a wrong
    magnitude rule cannot pass them."""
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


def dof_perm(L: int, index: dict, R: np.ndarray) -> np.ndarray:
    """Frame relabelling of the coframe variables induced by the rotation R."""
    smap = c696.frame_site_map(L, R)
    dir2class = {tuple(int(t) for t in DIRV[c]): c for c in SPC}
    m = np.empty(len(index), dtype=np.int64)
    for (c, x), i in index.items():
        w = R @ DIRV[c]
        vp = tuple(int(t) for t in np.abs(w))
        xp = tuple(int(t) for t in (np.asarray(smap[x], dtype=np.int64)
                                    + np.minimum(w, 0)))
        m[i] = index[(dir2class[vp], xp)]
    return m


def class_vector(index: dict) -> np.ndarray:
    cls = np.empty(len(index), dtype=np.int64)
    for (c, x), i in index.items():
        cls[i] = c
    return cls


def entries(Q, cls, m, sup):
    """Resolved defect entries with their support signature and weight split."""
    E = Q[np.ix_(m, m)] - Q
    ii, jj = np.nonzero(np.abs(E) > ZERO)
    val = E[ii, jj]
    av = np.abs(val)
    si = sup[cls[ii]]
    sj = sup[cls[jj]]
    full = LT * np.sqrt(si * sj)
    isf = np.abs(av - full) < TOL_W
    ish = np.abs(av - full / 2.0) < TOL_W
    return {"i": ii, "j": jj, "val": val, "av": av, "si": si, "sj": sj,
            "full": full, "isf": isf, "ish": ish,
            "dev": np.minimum(np.abs(av - full), np.abs(av - full / 2.0))}


def cubic_from(vals):
    """Exact integer Lagrange fit of a cubic in L through L_FIT, evaluated at L."""
    xs = list(L_FIT)

    def at(L):
        tot = 0.0
        for a in range(4):
            t = float(vals[a])
            for b in range(4):
                if b != a:
                    t *= (L - xs[b]) / (xs[a] - xs[b])
            tot += t
        return int(round(tot))
    return at


def main() -> int:
    supmax = max(SPC) + 1
    sup = np.zeros(supmax, dtype=np.int64)
    for c in SPC:
        sup[c] = SUP[c]
    mixed = [k for k, R in enumerate(FRAMES) if not constant_sign(R)]
    sextet = [k for k, R in enumerate(FRAMES) if constant_sign(R)]

    print("== cycle 713: assembly-defect weight law and complete census ==")
    print("config: LT={} supports={} fit L={} held-out L={} mixed_frames={} of {} "
          "fd_step={} tol={} cut={}".format(
              LT, tuple(sorted(set(SUP.values()))), L_FIT, L_HELD, len(mixed),
              len(FRAMES), fmt(c696.FD_H), fmt(TOL_W), fmt(CUT)))

    dev_all = 0.0
    unclassified = 0
    add_gap = []
    half_sig = Counter()
    full_sig = Counter()
    per_L = {}
    uniform = {}
    carrier_ok = True
    carrier_sig_ok = True
    carrier_sets = set()
    mag_counts = {}
    sextet_max = 0.0
    scanned = 0
    perm_ok = True
    half_max = 0.0
    full_min = float("inf")

    for L in L_ALL:
        model = c696.assemble_static_hessian(L, wrap=False)
        Q, index = model["Q"], model["index"]
        cls = class_vector(index)
        if L == L_FIT[0]:
            for k in sextet:
                m = dof_perm(L, index, FRAMES[k])
                sextet_max = max(sextet_max, float(np.abs(Q[np.ix_(m, m)] - Q).max()))
        rec = []
        mag = Counter()
        for k in mixed:
            m = dof_perm(L, index, FRAMES[k])
            perm_ok = perm_ok and len(np.unique(m)) == len(m)
            e = entries(Q, cls, m, sup)
            scanned += int(e["av"].size)
            good = e["isf"] | e["ish"]
            unclassified += int((~good).sum())
            dev_all = max(dev_all, float(e["dev"].max()) if e["av"].size else 0.0)
            if e["ish"].any():
                half_max = max(half_max, float(e["av"][e["ish"]].max()))
            if e["isf"].any():
                full_min = min(full_min, float(e["av"][e["isf"]].min()))
            add = LT * np.sqrt(e["si"] + e["sj"])
            sel = (np.abs(e["full"] - add) > ZERO) & e["isf"]
            if sel.any():
                add_gap.append(float(np.abs(e["av"][sel] - add[sel]).min()))
            for a, b in zip(e["si"][e["ish"]], e["sj"][e["ish"]]):
                half_sig[(int(a), int(b))] += 1
            for a, b in zip(e["si"][e["isf"]], e["sj"][e["isf"]]):
                full_sig[(int(a), int(b))] += 1
            v = e["val"]
            rec.append((int((e["ish"] & (v > 0)).sum()),
                        int((e["ish"] & (v < 0)).sum()),
                        int((e["isf"] & (v > 0)).sum()),
                        int((e["isf"] & (v < 0)).sum()),
                        int((e["av"] > CUT).sum())))
            pairs = Counter()
            for a, b in zip(cls[e["i"][e["isf"]]], cls[e["j"][e["isf"]]]):
                pairs[(int(a), int(b))] += 1
            carrier_ok = carrier_ok and len(pairs) == CARRIER
            carrier_sets.add(tuple(sorted(pairs)))
            sigc = Counter()
            for (ca, cb) in pairs:
                sigc[(SUP[ca], SUP[cb])] += 1
            carrier_sig_ok = carrier_sig_ok and dict(sigc) == CARRIER_SIG
            for name, target, _, _ in MAG_LAW:
                mag[name] += int((np.abs(e["av"] - target) < TOL_W).sum())
        uniform[L] = len(set(rec)) == 1
        per_L[L] = rec[0]
        mag_counts[L] = {n: mag[n] // (2 * len(mixed)) for n, _, _, _ in MAG_LAW}
        del Q, model

    check("g01_sextet_defect_ceiling", sextet_max < SEXTET_BOUND,
          "measured max defect below {} on all {} constant-sign frames at L=3".format(
              fmt(SEXTET_BOUND), len(sextet)))
    check("g02_frame_relabel_bijective", perm_ok,
          "frame relabelling is a permutation of the coframe variables")
    check("g03_complete_classification", unclassified == 0,
          "all {} resolved entries above {} obey |E| = w*LT*sqrt(s_i s_j), "
          "w in (1, 1/2); unclassified {}".format(
              scanned, fmt(ZERO), unclassified))
    check("g04_weight_law_dev", dev_all < TOL_W,
          "max weight-law deviation {}".format(fmt(dev_all)))
    check("g05_half_signature_axis_only", set(half_sig) == {(1, 1)},
          "half weight occurs only on axis-axis pairs, signature set "
          "{}".format(sorted(half_sig)))
    check("g06_full_signatures", tuple(sorted(full_sig)) == SIG_FULL,
          "realized full signatures {}".format(sorted(full_sig)))
    check("g07_absent_signatures",
          all(s not in full_sig and s not in half_sig for s in SIG_ABSENT),
          "signatures {} are never realized".format(list(SIG_ABSENT)))
    check("g08_additive_rejector", min(add_gap) >= ADD_FLOOR,
          "additive alternative LT*sqrt(s_i+s_j) misses by at least "
          "{:.2f} where it differs".format(min(add_gap)))
    check("g09_full_half_gap", half_max < CUT <= full_min,
          "largest half-weight magnitude {} below the cycle-711 cut {}, "
          "smallest full-weight magnitude {}".format(
              fmt(half_max), fmt(CUT), fmt(full_min)))
    check("g10_cut_is_weight_separator",
          all(r[4] == r[2] + r[3] for r in per_L.values()),
          "entries above the cycle-711 cut equal the full-weight entries "
          "at every size and frame")
    check("g11_sign_balance",
          all(r[0] == r[1] and r[2] == r[3] for r in per_L.values()),
          "plus and minus counts equal for both weights at every size")
    check("g12_frame_uniform", all(uniform.values()),
          "per-frame weight counts identical across the {} mixed "
          "frames at every size".format(len(mixed)))

    full_meas = [per_L[L][2] for L in L_ALL]
    half_meas = [per_L[L][0] for L in L_ALL]
    tot_meas = [2 * (per_L[L][0] + per_L[L][2]) for L in L_ALL]
    full_law = [48 * (L - 1) ** 3 + 8 * (L - 1) ** 2 + 4 * (L - 1) for L in L_ALL]
    half_law = [16 * (L - 1) ** 2 for L in L_ALL]
    tot_law = [96 * (L - 1) ** 3 + 48 * (L - 1) ** 2 + 8 * (L - 1) for L in L_ALL]
    check("g13_full_law", full_meas == full_law,
          "full per sign L={}: {} = 48(L-1)^3+8(L-1)^2+4(L-1)".format(
              L_ALL, full_meas))
    check("g14_half_law", half_meas == half_law,
          "half per sign L={}: {} = 16(L-1)^2".format(L_ALL, half_meas))
    check("g15_total_law", tot_meas == tot_law,
          "resolved entries per frame L={}: {} = "
          "96(L-1)^3+48(L-1)^2+8(L-1)".format(
              L_ALL, tot_meas))

    fit_full = cubic_from([per_L[L][2] for L in L_FIT])
    fit_tot = cubic_from([2 * (per_L[L][0] + per_L[L][2]) for L in L_FIT])
    check("g16_heldout_full",
          all(fit_full(L) == per_L[L][2] for L in L_HELD),
          "cubic fitted on L={} predicts full per sign at L={}: {}".format(
              L_FIT, L_HELD, [fit_full(L) for L in L_HELD]))
    check("g17_heldout_total",
          all(fit_tot(L) == 2 * (per_L[L][0] + per_L[L][2]) for L in L_HELD),
          "cubic fitted on L={} predicts resolved entries per frame at L={}: {}".format(
              L_FIT, L_HELD, [fit_tot(L) for L in L_HELD]))
    check("g18_census_anchor",
          all(per_L[L][2] == ANCHOR_FULL[L] for L in ANCHOR_FULL),
          "full per sign {} at L={} (cycle-711 census totals)".format(
              [ANCHOR_FULL[L] for L in sorted(ANCHOR_FULL)],
              sorted(ANCHOR_FULL)))

    for name, _, poly, text in MAG_LAW:
        got = [mag_counts[L][name] for L in L_ALL]
        want = [poly(L) for L in L_ALL]
        check("g19_mag_{}".format(name), got == want,
              "per sign L={}: {} = {}".format(L_ALL, got, text))
    check("g20_magnitudes_sum",
          all(sum(mag_counts[L].values()) == per_L[L][2] for L in L_ALL),
          "the four full magnitudes partition the full-weight population")
    check("g21_carrier_size", carrier_ok,
          "{} ordered class pairs carry the full-weight entries, at every "
          "size and frame".format(CARRIER))
    check("g22_carrier_signature", carrier_sig_ok and len(carrier_sets) == 3,
          "carrier support signatures {}, with {} frame-dependent identity "
          "sets".format({str(k): v for k, v in sorted(CARRIER_SIG.items())},
                         len(carrier_sets)))

    L = L_FIT[1]
    model = c696.assemble_static_hessian(L, wrap=False)
    Q, index = model["Q"], model["index"]
    cls = class_vector(index)
    m = dof_perm(L, index, FRAMES[mixed[0]])
    shuf = sup.copy()
    shuf[1], shuf[13] = sup[13], sup[1]
    e_sh = entries(Q, cls, m, shuf)
    check("g23_support_shuffle_rejector", int((~(e_sh["isf"] | e_sh["ish"])).sum()) > 0,
          "swapping the axis and body-diagonal supports leaves {} entries "
          "outside the weight law".format(
              int((~(e_sh["isf"] | e_sh["ish"])).sum())))
    n = Q.shape[0]
    d = np.arange(n)
    Qu = Q.copy()
    Qu[d, d] += PERT
    e_u = entries(Qu, cls, m, sup)
    check("g24_uniform_shift_invariance",
          float(np.abs(np.abs(Qu[np.ix_(m, m)] - Qu) - np.abs(Q[np.ix_(m, m)] - Q)).max()) < ZERO
          and int(e_u["av"].size) == int(entries(Q, cls, m, sup)["av"].size),
          "a uniform {:.1f} diagonal shift leaves the defect unchanged, "
          "because the frame relabelling is a permutation".format(PERT))
    Qr = Q.copy()
    Qr[d, d] += PERT * d / float(n)
    e_r = entries(Qr, cls, m, sup)
    bad = ~(e_r["isf"] | e_r["ish"])
    check("g25_ramp_rejector", int(bad.sum()) > 0,
          "a site-graded diagonal ramp of height {:.1f}, which the relabelling "
          "does not commute with, leaves {} entries outside the weight "
          "law".format(PERT, int(bad.sum())))

    NOTES["weight_law"] = "|E_ij| = w * LT * sqrt(s_i s_j), w in (1, 1/2)"
    NOTES["full_per_sign_poly"] = "48(L-1)^3 + 8(L-1)^2 + 4(L-1)"
    NOTES["half_per_sign_poly"] = "16(L-1)^2"
    NOTES["resolved_entries_per_frame_poly"] = "96(L-1)^3 + 48(L-1)^2 + 8(L-1)"
    NOTES["magnitude_polys"] = {n: t for n, _, _, t in MAG_LAW}
    NOTES["half_max"] = fmt(half_max)
    NOTES["full_min"] = fmt(full_min)
    NOTES["carrier_pairs"] = CARRIER
    NOTES["carrier_identity_sets"] = len(carrier_sets)

    receipt = {
        "cycle": 713,
        "object": "assembly-defect weight law and complete census",
        "LT": LT,
        "supports": {str(c): SUP[c] for c in SPC},
        "mixed_frames": len(mixed),
        "sizes": list(L_ALL),
        "full_per_sign": full_meas,
        "half_per_sign": half_meas,
        "resolved_entries_per_frame": tot_meas,
        "weight_law_dev": fmt(dev_all),
        "additive_gap": "{:.2f}".format(min(add_gap)),
        "entries_scanned": scanned,
        "gates": GATES,
        "notes": NOTES,
        "pass": N_PASS,
        "fail": N_FAIL,
    }
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("receipt: outputs/{}".format(RECEIPT_NAME))
    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 0 if N_FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
