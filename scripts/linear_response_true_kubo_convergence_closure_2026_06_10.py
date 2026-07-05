#!/usr/bin/env python3
"""First-order Kubo closure for the linear-response lane: convergence hardening.

Companion runner for

    docs/LINEAR_RESPONSE_TRUE_KUBO_FIRST_ORDER_CLOSURE_NARROW_THEOREM_NOTE_2026-06-10.md

This runner completes and hardens the closure path named by the open-gate
note docs/LINEAR_RESPONSE_DERIVATION_NOTE.md ("scripts/linear_response_true_kubo.py
remains the closure path for the literal Kubo theorem").

WHAT IS VERIFIED (all live, no fitted parameters anywhere):

  (1) FROZEN-ARTIFACT REPRODUCTION. The SHA-pinned caches of the two landed
      lanes (logs/runner-cache/linear_response_true_kubo.txt and the heuristic
      lane's frozen 44-family log logs/2026-04-07-linear-response-derivation.txt)
      are parsed and their headline statistics recomputed from their own
      columns (r = 0.9716 overall / 0.9875 / 0.9793 / 0.9995 by group,
      42/44 sign agreement, ratio stats; heuristic r = 0.5605, 36/44).
      The landed runner scripts/linear_response_true_kubo.py is IMPORTED
      (not transcribed) and its kubo_true and response values are reproduced
      live for all 44 families against the cache columns.

  (2) THE EXACT MATCHED DERIVATIVE (the literal first-order Kubo object).
      The response lane (ind.prop_beam, used by both landed lanes) puts the
      imposed field on an edge as the ENDPOINT AVERAGE
          f_edge(s) = 0.5*(field[i]+field[j]),  field[i] = s/(r_i+0.1),
      so the exact derivative of the per-edge factor exp(i k L (1-f_edge))
      at s=0 carries g_edge = 0.5*(1/(r_i+0.1)+1/(r_j+0.1)).  The parallel
      perturbation recurrence of the landed bounded theorem
      (LINEAR_RESPONSE_TRUE_KUBO_NOTE.md),
          B_j = sum_{i->j} [B_i + A_i * (-i k L g_edge)] * exp(i k L) * w h^2/L^2,
      with THIS g_edge (and the response lane's own prune rule |A|<1e-30)
      is therefore the exact derivative d(cz)/ds at s=0 of the response map.
      The landed runner instead used the edge-MIDPOINT factor
      g_mid = 1/(r_mid+0.1): that is the exact derivative of a *variant*
      discretization (the source bounded-theorem scope), not of the
      response map.  Both variants are computed here side by side.

  (3) CONVERGENCE (the key new check).  For 16 live families spanning all
      three groups and INCLUDING the three residual cases of the open-gate
      note (G2_asym_z, H1_ring, L1_longrange) plus the landed lane's
      remaining sign-miss (R1_kreg_k15), the finite-difference response is
      recomputed on the ladder s = 4e-3, 2e-3, 1e-3, 5e-4,
      2.5e-4 (forward) and +-1e-3, +-5e-4, +-2.5e-4 (centered):
        - forward error vs kubo_end shrinks O(s)  (last-pair ratio ~ 1/2),
        - centered error shrinks O(s^2)           (last-pair ratio ~ 1/4),
        - Richardson extrapolation of the centered differences (an
          INDEPENDENT high-order method: 4 propagator runs, no B recurrence)
          agrees with kubo_end to <= 1e-5 relative,
        - a 5-point O(s^4) stencil cross-checks kubo_end independently,
        - the limit is kubo_end and NOT kubo_mid wherever the two differ.

  (4) FULL-44 PANEL AT A SMALLER STEP.  response(s=5e-4) is computed live
      for every family.  Panel classification is made explicit:
      4 detector-dead families (free detector probability is exactly 0),
      1 prune-zone family (R2_kreg_k8: p_det ~ 1e-63, below the response
      lane's own prune resolution; its landed kubo_true = +4.36 is shown to
      be a prune-semantics artifact - the matched derivative is ~0, matching
      response ~ 0), and 39 live families.  On the live panel the
      correlation and through-origin slope versus kubo_end move toward 1
      as s decreases, and sign agreement is counted with no exclusions.

  (5) HEURISTIC CHARACTERIZATION.  The open-gate note's detector-only
      heuristic (kubo_heuristic = cz_weighted - cz_free, recomputed live and
      matched against its frozen log) is correlated against the exact
      derivative: it is a coarse approximation, and on the three residual
      cases its sign is wrong while the exact derivative's sign is right.

SCOPE / HONESTY: this is the graph-family toy linear-response lane (grown
DAGs + held-out generators + off-scaffold layered generators), NOT the
cubic-Coxeter geometric rows.  First order in s only.  No audit grade is
authored here; the independent audit lane adjudicates all statuses.

Run: python3 scripts/linear_response_true_kubo_convergence_closure_2026_06_10.py
"""

from __future__ import annotations

# Heavy compute / sweep runner - `AUDIT_TIMEOUT_SEC = 1800` per
# docs/audit/RUNNER_CACHE_POLICY.md (same ceiling as the landed
# linear_response_true_kubo.py, whose cached run took ~947 s).
AUDIT_TIMEOUT_SEC = 1800

import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import universality_classifier as uc                    # noqa: E402
import independent_generators_heldout as ind            # noqa: E402
import global_coherence_off_scaffold as offs            # noqa: E402
import linear_response_true_kubo as ltk                 # noqa: E402  (landed closure-path runner, imported not transcribed)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FROZEN_TRUE_KUBO_CACHE = os.path.join(REPO, "logs", "runner-cache", "linear_response_true_kubo.txt")
FROZEN_HEURISTIC_LOG = os.path.join(REPO, "logs", "2026-04-07-linear-response-derivation.txt")

MASS_Z = uc.MASS_Z          # z_src = 3.0 (lane convention)
H = uc.H                    # 0.5
K = uc.K                    # 5.0
BETA = 0.8                  # matches uc/ind prop_beam weight exp(-BETA*theta^2)
PRUNE = 1e-30               # the response lane's own prune threshold (ind.prop_beam)

S_FWD = [0.004, 0.002, 0.001, 0.0005, 0.00025]   # forward ladder (0.001 = both landed lanes' epsilon)
S_CTR = [0.001, 0.0005, 0.00025]                 # centered ladder (extra -s runs)

# Convergence subset: the three residual cases of the open-gate note, the
# landed lane's remaining sign-miss, and 12 more spanning all groups/stencils.
SUBSET = [
    "A1_orig_Fam1_swept", "B1_pure_grid_swept", "C1_random_lo_swept",
    "E1_PW3_narrow_swept", "G2_asym_z_swept", "H1_ring_swept",
    "H2_cross_swept", "K2_huge_drift_md1_swept", "K3_NL5_swept",
    "R1_kreg_k15_scaf", "R3_kreg_k20_scaf", "E1_er_p005_scaf",
    "L1_longrange_k12_scaf",
    "OF1_uniform_k15_off", "OF6_rotated_grid_off", "OF9_stretched_off",
]
RESIDUAL3 = ["G2_asym_z_swept", "H1_ring_swept", "L1_longrange_k12_scaf"]

PASS = 0
FAIL = 0


def repo_rel(path: str) -> str:
    return os.path.relpath(path, REPO)


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))
    return bool(cond)


def pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx <= 0 or syy <= 0:
        return 0.0
    return sxy / math.sqrt(sxx * syy)


def slope_through_origin(xs, ys):
    """Least-squares slope of y on x with zero intercept."""
    num = sum(x * y for x, y in zip(xs, ys))
    den = sum(x * x for x in xs)
    return num / den if den > 0 else float("nan")


# ---------------------------------------------------------------------------
# The matched perturbation propagator.
#
# Derivation (one line, from the response lane's own edge factor): in
# ind.prop_beam each edge multiplies by exp(i k L (1 - f)) * w * h^2/L^2 with
# f = 0.5*(field[i]+field[j]) and field[i] = s/(r_i+0.1) (uc.imposed_field,
# distance in the x-z plane).  d/ds of that factor at s=0 is
# (-i k L g_edge) * exp(i k L) * w * h^2/L^2 with
#     g_edge = 0.5*(1/(r_i+0.1) + 1/(r_j+0.1)).
# Termwise differentiation of the finite accumulation (same sweep order,
# same prune rule on |A|) gives the parallel recurrence below - the same
# recurrence form as the landed bounded theorem (LINEAR_RESPONSE_TRUE_KUBO_
# NOTE.md), with g_edge matched to the response discretization.  B_mid uses
# the landed runner's midpoint factor g_mid = 1/(r_mid+0.1) for side-by-side
# comparison (that variant is the exact derivative of a DIFFERENT, midpoint-
# sampled discretization).
# ---------------------------------------------------------------------------
def pert_prop_matched(pos, adj, x_src, z_src):
    n = len(pos)
    A = [0j] * n
    Be = [0j] * n     # matched endpoint-average factor (exact for the response map)
    Bm = [0j] * n     # landed midpoint factor (variant discretization)
    A[0] = 1.0 + 0j
    order = sorted(range(n), key=lambda i: pos[i][0])   # identical to prop_beam
    h2 = H * H
    n_pruned = 0
    for i in order:
        ai = A[i]
        if abs(ai) < PRUNE:                              # response lane's prune rule
            if ai != 0 or Be[i] != 0 or Bm[i] != 0:
                n_pruned += 1
            continue
        bei = Be[i]
        bmi = Bm[i]
        xi, yi, zi = pos[i]
        ri = math.sqrt((xi - x_src) ** 2 + (zi - z_src) ** 2) + 0.1
        for j in adj.get(i, []):
            xj, yj, zj = pos[j]
            dx = xj - xi
            dy = yj - yi
            dz = zj - zi
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            rj = math.sqrt((xj - x_src) ** 2 + (zj - z_src) ** 2) + 0.1
            mx = 0.5 * (xi + xj)
            mz = 0.5 * (zi + zj)
            rm = math.sqrt((mx - x_src) ** 2 + (mz - z_src) ** 2) + 0.1
            g_end = 0.5 * (1.0 / ri + 1.0 / rj)
            g_mid = 1.0 / rm
            phase = K * L
            phi = complex(math.cos(phase), math.sin(phase))
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            cw = w * h2 / (L * L)
            A[j] += ai * phi * cw
            Be[j] += (bei + ai * complex(0.0, -K * L * g_end)) * phi * cw
            Bm[j] += (bmi + ai * complex(0.0, -K * L * g_mid)) * phi * cw
    return A, Be, Bm, n_pruned


def det_slice(pos, PW):
    hw = int(PW / H)
    npl = (2 * hw + 1) ** 2
    return len(pos) - npl, len(pos)


def cz_det(amps, pos, PW):
    """Detector centroid + detector probability (ind.cz convention)."""
    ds, n = det_slice(pos, PW)
    t = sum(abs(amps[i]) ** 2 for i in range(ds, n))
    if t <= 0:
        return 0.0, 0.0
    return sum(abs(amps[i]) ** 2 * pos[i][2] for i in range(ds, n)) / t, t


def dcz_from_AB(A, B, pos, PW):
    """d(cz)/ds from the quotient rule (same readout as the landed runner)."""
    ds, n = det_slice(pos, PW)
    weights = [abs(A[i]) ** 2 for i in range(ds, n)]
    total = sum(weights)
    if total <= 0:
        return float("nan")
    zs = [pos[i][2] for i in range(ds, n)]
    cz_free = sum(w * z for w, z in zip(weights, zs)) / total
    dT = sum(2.0 * (A[i].conjugate() * B[i]).real for i in range(ds, n))
    dN = sum(2.0 * (A[i].conjugate() * B[i]).real * pos[i][2] for i in range(ds, n))
    Nn = total * cz_free
    return dN / total - Nn * dT / (total * total)


def heuristic_kubo(free, pos, PW, z_src):
    """The open-gate note's detector-only heuristic (linear_response_derivation.py,
    kubo_predictor): centroid reweighted by |amp|^2/(|z-z_src|+0.1) minus free."""
    ds, n = det_slice(pos, PW)
    w_std = [abs(free[i]) ** 2 for i in range(ds, n)]
    w_fld = [abs(free[i]) ** 2 / (abs(pos[i][2] - z_src) + 0.1) for i in range(ds, n)]
    zs = [pos[i][2] for i in range(ds, n)]
    T1 = sum(w_std)
    T2 = sum(w_fld)
    if T1 <= 0 or T2 <= 0:
        return float("nan")
    return (sum(w * z for w, z in zip(w_fld, zs)) / T2
            - sum(w * z for w, z in zip(w_std, zs)) / T1)


def all_families():
    """(cache_name, group, builder, NL, PW) in the landed runner's order."""
    fams = []
    for fam in uc.make_families():
        def build(f=fam):
            return uc.grow(f["seed"], f["drift"], f["restore"], f["NL"], f["PW"],
                           f["md"], mode=f.get("mode", "dense"),
                           anisotropy=f.get("anisotropy", 1.0))
        fams.append((fam["name"] + "_swept", "swept", build, fam["NL"], fam["PW"]))
    for name, builder in ind.make_independent_families():
        fams.append((name + "_scaf", "scaffolded", builder, ind.NL, ind.PW))
    for name, builder in offs.make_off_scaffold_families():
        fams.append((name + "_off", "off_scaffold", builder, offs.NL, offs.PW))
    return fams


ROW_RE = re.compile(
    r"^(?P<family>\S+)\s+(?P<group>swept|scaffolded|off_scaffold)\s+"
    r"(?P<status>PASS|FAIL)\s+(?P<response>[+-]\d+\.\d+)\s+"
    r"(?P<kubo>[+-]\d+\.\d+)", re.MULTILINE)


def parse_table(text):
    return {m.group("family"): {
        "group": m.group("group"),
        "response": float(m.group("response")),
        "kubo": float(m.group("kubo")),
    } for m in ROW_RE.finditer(text)}


def main():
    print("=" * 100)
    print("TRUE FIRST-ORDER KUBO - CONVERGENCE CLOSURE (matched-discretization derivative, s->0 ladder)")
    print("=" * 100)

    # ------------------------------------------------------------------
    print("\nSECTION 1 - frozen-artifact reproduction (parse + recompute)")
    print("-" * 100)
    cache_rows = {}
    if check("frozen true-kubo runner cache exists", os.path.exists(FROZEN_TRUE_KUBO_CACHE), repo_rel(FROZEN_TRUE_KUBO_CACHE)):
        text = open(FROZEN_TRUE_KUBO_CACHE, encoding="utf-8").read()
        cache_rows = parse_table(text)
        check("cache parses to 44 family rows (26/9/9 by group)",
              len(cache_rows) == 44
              and sum(1 for r in cache_rows.values() if r["group"] == "swept") == 26
              and sum(1 for r in cache_rows.values() if r["group"] == "scaffolded") == 9
              and sum(1 for r in cache_rows.values() if r["group"] == "off_scaffold") == 9,
              f"rows={len(cache_rows)}")
        xs = [r["kubo"] for r in cache_rows.values()]
        ys = [r["response"] for r in cache_rows.values()]
        r_all = pearson(xs, ys)
        check("cached overall r recomputes to 0.9716 from the cache's own columns",
              abs(r_all - 0.9716) < 5e-4, f"r={r_all:.4f}")
        grp_expect = {"swept": 0.9875, "scaffolded": 0.9793, "off_scaffold": 0.9995}
        ok = True
        det = []
        for g, exp in grp_expect.items():
            rows = [r for r in cache_rows.values() if r["group"] == g]
            rg = pearson([r["kubo"] for r in rows], [r["response"] for r in rows])
            det.append(f"{g}={rg:.4f}")
            ok = ok and abs(rg - exp) < 5e-4
        check("cached by-group r recompute (0.9875 / 0.9793 / 0.9995)", ok, " ".join(det))
        sign_ok = sum(1 for r in cache_rows.values() if (r["kubo"] > 0) == (r["response"] > 0))
        check("cached sign agreement recounts to 42/44", sign_ok == 42, f"{sign_ok}/44")
        ratios = [r["kubo"] / r["response"] for r in cache_rows.values() if abs(r["response"]) > 1e-6]
        mr = sum(ratios) / len(ratios)
        sr = math.sqrt(sum((x - mr) ** 2 for x in ratios) / len(ratios))
        check("cached ratio stats recompute (N=39, mean 1.0465, std 0.8269, min -0.3596, max 5.7671)",
              len(ratios) == 39 and abs(mr - 1.0465) < 5e-3 and abs(sr - 0.8269) < 5e-3
              and abs(min(ratios) + 0.3596) < 5e-3 and abs(max(ratios) - 5.7671) < 5e-3,
              f"N={len(ratios)} mean={mr:.4f} std={sr:.4f} min={min(ratios):.4f} max={max(ratios):.4f}")

    heur_frozen = {}
    if check("heuristic lane frozen 44-family log exists", os.path.exists(FROZEN_HEURISTIC_LOG), repo_rel(FROZEN_HEURISTIC_LOG)):
        htext = open(FROZEN_HEURISTIC_LOG, encoding="utf-8").read()
        heur_frozen = parse_table(htext)   # same row shape: response then kubo(heuristic)
        r_h = pearson([r["kubo"] for r in heur_frozen.values()],
                      [r["response"] for r in heur_frozen.values()])
        s_h = sum(1 for r in heur_frozen.values() if (r["kubo"] > 0) == (r["response"] > 0))
        check("heuristic frozen log recomputes (44 rows, r=0.5605, sign 36/44)",
              len(heur_frozen) == 44 and abs(r_h - 0.5605) < 5e-4 and s_h == 36,
              f"rows={len(heur_frozen)} r={r_h:.4f} sign={s_h}/44")

    # ------------------------------------------------------------------
    print("\nSECTION 2 - full 44-family live lap (free beam, matched + midpoint derivatives,")
    print("            landed-runner import, response at s=1e-3 and s=5e-4, panel classification)")
    print("-" * 100)
    rows = []
    for name, group, build, NL, PW in all_families():
        pos, adj, nmap = build()
        x_src = (NL // 3) * H
        free = ind.prop_beam(pos, adj, nmap, None, K)
        cz0, p_det = cz_det(free, pos, PW)
        A, Be, Bm, n_pruned = pert_prop_matched(pos, adj, x_src, MASS_Z)
        k_end = dcz_from_AB(A, Be, pos, PW)
        k_mid = dcz_from_AB(A, Bm, pos, PW)
        k_ltk, _ = ltk.true_kubo_dcz_ds(pos, adj, nmap, NL, PW)   # landed code, imported
        heur = heuristic_kubo(free, pos, PW, MASS_Z)
        meas = {}
        for s in (0.001, 0.0005):
            fld = uc.imposed_field(pos, x_src, MASS_Z, s)
            czs, _ = cz_det(ind.prop_beam(pos, adj, nmap, fld, K), pos, PW)
            meas[s] = (czs - cz0) / s
        if p_det == 0.0:
            cls = "detector_dead"
        elif p_det < 1e-58:
            cls = "prune_zone"
        else:
            cls = "live"
        rows.append({"name": name, "group": group, "cls": cls, "p_det": p_det,
                     "n_pruned": n_pruned, "cz0": cz0, "k_end": k_end, "k_mid": k_mid,
                     "k_ltk": k_ltk, "heur": heur, "meas": meas,
                     "pos": pos if name in SUBSET else None,
                     "adj": adj if name in SUBSET else None,
                     "nmap": nmap if name in SUBSET else None,
                     "NL": NL, "PW": PW})
        print(f"  {name:30s} {group:>12s} {cls:>13s} p_det={p_det:9.3e} pruned={n_pruned:5d} "
              f"k_end={k_end:+11.6f} k_mid={k_mid:+11.6f} m(1e-3)={meas[0.001]:+11.6f}")

    by = {r["name"]: r for r in rows}
    live = [r for r in rows if r["cls"] == "live"]
    dead = sorted(r["name"] for r in rows if r["cls"] == "detector_dead")
    prune_zone = [r for r in rows if r["cls"] == "prune_zone"]

    check("panel classification: 39 live / 4 detector-dead / 1 prune-zone",
          len(live) == 39 and len(dead) == 4 and len(prune_zone) == 1,
          f"live={len(live)} dead={dead} prune={[r['name'] for r in prune_zone]}")
    check("detector-dead set is exactly {H1_hub, I1_drift_y, T1_tree_fan4, X1_expander_k12} (free p_det = 0)",
          dead == ["H1_hub_scaf", "I1_drift_y_swept", "T1_tree_fan4_scaf", "X1_expander_k12_scaf"],
          ",".join(dead))

    if cache_rows:
        dev_ltk = max(abs(r["k_ltk"] - cache_rows[r["name"]]["kubo"]) for r in rows)
        check("imported landed runner reproduces ALL 44 cached kubo_true values (<= 1.5e-6, print precision)",
              dev_ltk <= 1.5e-6, f"max|dev|={dev_ltk:.2e}")
        dev_meas = max(abs(r["meas"][0.001] - cache_rows[r["name"]]["response"]) for r in rows)
        check("live response(s=1e-3) reproduces ALL 44 cached response values (<= 1.5e-6)",
              dev_meas <= 1.5e-6, f"max|dev|={dev_meas:.2e}")
    dev_mid = max(abs(r["k_mid"] - r["k_ltk"]) / max(abs(r["k_ltk"]), 1e-12) for r in live)
    check("this runner's midpoint variant equals the imported landed kubo_true on all 39 live rows (rel <= 1e-9)",
          dev_mid <= 1e-9, f"max rel dev={dev_mid:.2e}")

    rz = prune_zone[0] if prune_zone else None
    if rz is not None:
        check("prune-zone row is R2_kreg_k8 (p_det ~ 1e-63, below the lane's |amp|<1e-30 prune resolution squared)",
              rz["name"] == "R2_kreg_k8_scaf" and rz["p_det"] < 1e-58 and rz["n_pruned"] > 0,
              f"{rz['name']} p_det={rz['p_det']:.2e} pruned={rz['n_pruned']}")
        check("R2: matched derivative ~ 0 AND response ~ 0 at both steps; the cached kubo_true=+4.36 is a "
              "prune-semantics artifact (landed B-pass keeps propagating where the response lane prunes)",
              abs(rz["k_end"]) < 1e-10 and abs(rz["meas"][0.001]) < 1e-6 and abs(rz["meas"][0.0005]) < 1e-6
              and abs(rz["k_ltk"] - 4.358926) < 1.5e-6,
              f"k_end={rz['k_end']:.2e} m(1e-3)={rz['meas'][0.001]:.2e} k_ltk={rz['k_ltk']:+.4f}")

    # ------------------------------------------------------------------
    print("\nSECTION 3 - convergence ladders on the 16-family subset (incl. the 3 residual cases)")
    print("-" * 100)
    conv = {}
    for name in SUBSET:
        r = by[name]
        pos, adj, nmap, NL, PW = r["pos"], r["adj"], r["nmap"], r["NL"], r["PW"]
        x_src = (NL // 3) * H
        cz0 = r["cz0"]
        czs = {}
        for s in S_FWD:
            if s in r["meas"]:
                czs[s] = r["meas"][s] * s + cz0
            else:
                fld = uc.imposed_field(pos, x_src, MASS_Z, s)
                czs[s], _ = cz_det(ind.prop_beam(pos, adj, nmap, fld, K), pos, PW)
        for s in S_CTR:
            fld = uc.imposed_field(pos, x_src, MASS_Z, -s)
            czs[-s], _ = cz_det(ind.prop_beam(pos, adj, nmap, fld, K), pos, PW)
        Df = {s: (czs[s] - cz0) / s for s in S_FWD}
        Dc = {s: (czs[s] - czs[-s]) / (2 * s) for s in S_CTR}
        k_end, k_mid = r["k_end"], r["k_mid"]
        # Richardson on the two smallest centered steps: O(s^4) estimate,
        # independent of the B recurrence (pure propagator runs).
        rich = (4 * Dc[0.00025] - Dc[0.0005]) / 3
        # 5-point O(s^4) stencil at h=2.5e-4 (uses +-2.5e-4 and +-5e-4): second
        # independent high-order cross-check of the derivative value.
        h = 0.00025
        d5 = (-czs[2 * h] + 8 * czs[h] - 8 * czs[-h] + czs[-2 * h]) / (12 * h)
        ef = {s: Df[s] - k_end for s in S_FWD}
        ec = {s: Dc[s] - k_end for s in S_CTR}
        ratio_f = abs(ef[0.00025]) / abs(ef[0.0005]) if ef[0.0005] != 0 else float("nan")
        ratio_c = abs(ec[0.00025]) / abs(ec[0.0005]) if ec[0.0005] != 0 else float("nan")
        rel_rich_end = abs(rich - k_end) / max(abs(k_end), 1e-12)
        rel_d5_end = abs(d5 - k_end) / max(abs(k_end), 1e-12)
        gap_mid = abs(k_mid - k_end)
        conv[name] = dict(Df=Df, Dc=Dc, rich=rich, d5=d5, ratio_f=ratio_f, ratio_c=ratio_c,
                          rel_rich_end=rel_rich_end, rel_d5_end=rel_d5_end, gap_mid=gap_mid,
                          k_end=k_end, k_mid=k_mid)
        print(f"\n  {name}  (p_det={r['p_det']:.2e})")
        print(f"    k_end={k_end:+.6f}  k_mid={k_mid:+.6f}  (mid-end gap {k_mid-k_end:+.3e})")
        for s in S_FWD:
            line = f"    s={s:8.6f}  Df={Df[s]:+12.6f}  err_end={ef[s]:+10.3e}  err_mid={Df[s]-k_mid:+10.3e}"
            if s in S_CTR:
                line += f"  Dc={Dc[s]:+12.6f}  errC_end={ec[s]:+10.3e}"
            print(line)
        print(f"    fwd err ratio (2.5e-4 / 5e-4) = {ratio_f:.3f}   ctr err ratio = {ratio_c:.3f}")
        print(f"    Richardson(centered) = {rich:+.8f}  rel-to-k_end = {rel_rich_end:.2e}")
        print(f"    5-point O(s^4)       = {d5:+.8f}  rel-to-k_end = {rel_d5_end:.2e}")

    ok_f = all(0.42 <= conv[n]["ratio_f"] <= 0.60 for n in SUBSET)
    check("forward finite-difference error is O(s) on all 16 subset families (last-pair ratio in [0.42, 0.60])",
          ok_f, " ".join(f"{conv[n]['ratio_f']:.2f}" for n in SUBSET))
    ok_c = all(0.22 <= conv[n]["ratio_c"] <= 0.28 for n in SUBSET)
    check("centered finite-difference error is O(s^2) on all 16 (last-pair ratio in [0.22, 0.28])",
          ok_c, " ".join(f"{conv[n]['ratio_c']:.2f}" for n in SUBSET))
    worst_rich = max(conv[n]["rel_rich_end"] for n in SUBSET)
    check("Richardson limit of response(s) equals the matched derivative kubo_end on all 16 (rel <= 1e-5)",
          worst_rich <= 1e-5, f"worst rel={worst_rich:.2e}")
    worst_d5 = max(conv[n]["rel_d5_end"] for n in SUBSET)
    check("independent 5-point O(s^4) stencil confirms kubo_end on all 16 (rel <= 1e-5)",
          worst_d5 <= 1e-5, f"worst rel={worst_d5:.2e}")
    ok_disc = all(abs(conv[n]["rich"] - conv[n]["k_end"]) <= 0.02 * conv[n]["gap_mid"]
                  for n in SUBSET if conv[n]["gap_mid"] > 1e-8)
    check("limit discrimination: wherever mid- and endpoint variants differ, the s->0 limit is the MATCHED "
          "endpoint variant (Richardson at least 50x closer to k_end than the mid-end gap)",
          ok_disc, f"families with gap>1e-8: {sum(1 for n in SUBSET if conv[n]['gap_mid'] > 1e-8)}/16")

    print("\n  Residual-case adjudication (the open-gate note's three sign-miss families):")
    g2 = conv["G2_asym_z_swept"]
    check("G2_asym_z: response(s) converges to k_end=+0.0902 (sign +, like response); cached "
          "magnitude gap was midpoint-variant offset (+0.216) plus O(s) error, both now quantified",
          abs(g2["k_end"] - 0.0902) < 5e-4 and g2["rel_rich_end"] <= 1e-5
          and g2["k_end"] > 0 and by["G2_asym_z_swept"]["meas"][0.001] > 0,
          f"k_end={g2['k_end']:+.4f} k_mid={g2['k_mid']:+.4f} rich rel={g2['rel_rich_end']:.1e}")
    check("G2_asym_z nonlinearity exhibit: at the battery scale s=4e-3 the lane response has the "
          "OPPOSITE sign of the derivative (strongly nonlinear family), turning correct for s <= 2e-3",
          g2["Df"][0.004] < 0 and g2["Df"][0.002] > 0 and g2["k_end"] > 0,
          f"Df(4e-3)={g2['Df'][0.004]:+.4f} Df(2e-3)={g2['Df'][0.002]:+.4f}")
    h1 = conv["H1_ring_swept"]
    check("H1_ring: response(s) converges to k_end=-1.0934 (sign -, like response); landed midpoint "
          "value -2.116 overstated the magnitude ~2x",
          abs(h1["k_end"] + 1.0934) < 5e-4 and h1["rel_rich_end"] <= 1e-5 and h1["k_end"] < 0,
          f"k_end={h1['k_end']:+.4f} k_mid={h1['k_mid']:+.4f} rich rel={h1['rel_rich_end']:.1e}")
    l1 = conv["L1_longrange_k12_scaf"]
    check("L1_longrange: response(s) converges to k_end=-0.8133 (sign -, like response)",
          abs(l1["k_end"] + 0.8133) < 5e-4 and l1["rel_rich_end"] <= 1e-5 and l1["k_end"] < 0,
          f"k_end={l1['k_end']:+.4f} k_mid={l1['k_mid']:+.4f} rich rel={l1['rel_rich_end']:.1e}")
    r1 = conv["R1_kreg_k15_scaf"]
    check("R1_kreg_k15 (the landed lane's unexplained sign miss) RESOLVED: the matched derivative is "
          "k_end=-0.8844, agreeing in sign with response (-0.853 at 1e-3); the landed +0.307 was the "
          "midpoint-variant artifact, not measurement noise",
          abs(r1["k_end"] + 0.8844) < 5e-4 and r1["rel_rich_end"] <= 1e-5
          and r1["k_end"] < 0 and r1["k_mid"] > 0,
          f"k_end={r1['k_end']:+.4f} k_mid={r1['k_mid']:+.4f} rich rel={r1['rel_rich_end']:.1e}")

    # ------------------------------------------------------------------
    print("\nSECTION 4 - full live panel: correlation and slope versus the matched derivative as s decreases")
    print("-" * 100)
    if cache_rows:
        r_cacheconv = pearson([r["k_ltk"] for r in rows], [r["meas"][0.001] for r in rows])
        check("end-to-end live reproduction of the cached comparison: r(kubo_true, response(1e-3)) over all "
              "44 rows = 0.9716", abs(r_cacheconv - 0.9716) < 1e-3, f"r={r_cacheconv:.4f}")
    stats = {}
    for s in (0.001, 0.0005):
        xs = [r["k_end"] for r in live]
        ys = [r["meas"][s] for r in live]
        r_end = pearson(xs, ys)
        sl = slope_through_origin(xs, ys)
        sign_ok = sum(1 for r in live if (r["k_end"] > 0) == (r["meas"][s] > 0))
        rels = [abs(r["meas"][s] - r["k_end"]) / abs(r["k_end"]) for r in live if abs(r["k_end"]) >= 1e-3]
        rms = math.sqrt(sum(e * e for e in rels) / len(rels))
        r_mid = pearson([r["k_mid"] for r in live], ys)
        stats[s] = dict(r_end=r_end, slope=sl, sign_ok=sign_ok, rms=rms, r_mid=r_mid, n_rel=len(rels))
        print(f"  s={s:7.4f}: live-39 r(k_end, response)={r_end:.6f}  slope={sl:.6f}  "
              f"sign={sign_ok}/39  rms-rel={rms:.4f} (N={len(rels)})  [r(k_mid, response)={r_mid:.6f}]")
    check("sign agreement on the FULL live panel is 39/39 at BOTH steps versus the matched derivative "
          "(no exclusions; the cached comparison's two sign misses are resolved/classified)",
          stats[0.001]["sign_ok"] == 39 and stats[0.0005]["sign_ok"] == 39,
          f"{stats[0.001]['sign_ok']}/39 at 1e-3, {stats[0.0005]['sign_ok']}/39 at 5e-4")
    check("correlation rises toward 1 as s decreases: r(5e-4) > r(1e-3) > cached r=0.9716",
          stats[0.0005]["r_end"] > stats[0.001]["r_end"] > 0.9716,
          f"r(1e-3)={stats[0.001]['r_end']:.6f} r(5e-4)={stats[0.0005]['r_end']:.6f}")
    check("through-origin slope walks to 1 at O(s): |slope(5e-4)-1| <= 0.62*|slope(1e-3)-1|",
          abs(stats[0.0005]["slope"] - 1) <= 0.62 * abs(stats[0.001]["slope"] - 1),
          f"|slope-1|: {abs(stats[0.001]['slope']-1):.4f} -> {abs(stats[0.0005]['slope']-1):.4f}")
    check("rms relative deviation halves with s (O(s) panel-wide): ratio in [0.42, 0.60]",
          0.42 <= stats[0.0005]["rms"] / stats[0.001]["rms"] <= 0.60,
          f"rms: {stats[0.001]['rms']:.4f} -> {stats[0.0005]['rms']:.4f} "
          f"(ratio {stats[0.0005]['rms']/stats[0.001]['rms']:.3f})")
    check("the midpoint variant does NOT converge: r(k_mid, response) stays below r(k_end, response) at "
          "both steps (its deviation is s-independent discretization offset)",
          stats[0.001]["r_mid"] < stats[0.001]["r_end"] and stats[0.0005]["r_mid"] < stats[0.0005]["r_end"],
          f"mid {stats[0.001]['r_mid']:.4f}/{stats[0.0005]['r_mid']:.4f} vs "
          f"end {stats[0.001]['r_end']:.6f}/{stats[0.0005]['r_end']:.6f}")

    # ------------------------------------------------------------------
    print("\nSECTION 5 - the open-gate heuristic characterized against the exact derivative")
    print("-" * 100)
    if heur_frozen:
        devs = [abs(by[n]["heur"] - heur_frozen[n]["kubo"]) for n in SUBSET]
        check("live heuristic recompute matches the heuristic lane's frozen log on the 16 subset families "
              "(<= 1.5e-6)", max(devs) <= 1.5e-6, f"max|dev|={max(devs):.2e}")
    r_heur = pearson([r["heur"] for r in live], [r["k_end"] for r in live])
    print(f"  r(heuristic, k_end) over live-39 = {r_heur:.4f}")
    check("heuristic is a coarse approximation of the exact derivative, not the derivative itself "
          "(0 < r(heuristic, k_end) < 0.9 on the live panel)", 0.0 < r_heur < 0.9, f"r={r_heur:.4f}")
    ok3 = True
    for n in RESIDUAL3:
        hsign = by[n]["heur"] > 0
        msign = by[n]["meas"][0.001] > 0
        esign = by[n]["k_end"] > 0
        print(f"  {n}: heuristic={by[n]['heur']:+.4f} response(1e-3)={by[n]['meas'][0.001]:+.4f} "
              f"k_end={by[n]['k_end']:+.4f}")
        ok3 = ok3 and (hsign != msign) and (esign == msign)
    check("on the three residual cases the heuristic sign is WRONG and the exact derivative sign is RIGHT "
          "(the derivative captures the path-phase structure the detector-only reweighting misses)", ok3)

    # ------------------------------------------------------------------
    print("\n" + "=" * 100)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 100)
    print("VERDICT: the literal first-order response of the detector centroid to the lane's imposed")
    print("  1/r source field is DERIVED in closed recurrence form and VERIFIED as the s->0 limit of the")
    print("  finite-difference response: the parallel perturbation propagator with the lane's own")
    print("  endpoint-averaged edge field factor g_edge = (1/(r_i+0.1)+1/(r_j+0.1))/2 is the")
    print("  exact derivative d(cz)/ds at s=0 (O(s) forward / O(s^2) centered convergence on all 16 ladder")
    print("  families incl. the three residual cases; Richardson and 5-point O(s^4) cross-checks agree to")
    print("  <= 1e-5 relative; live-panel sign agreement 39/39 at both tested steps; r and slope walk to 1")
    print("  as s decreases). The landed runner's midpoint r_edge variant is the exact derivative of a")
    print("  DIFFERENT (midpoint-sampled) discretization: its per-family offset is s-independent and is the")
    print("  dominant part of the cached magnitude gaps; on R1_kreg_k15 it produced the one real sign miss,")
    print("  now resolved by the matched derivative. The open-gate note's detector-only heuristic is")
    print("  characterized as a coarse approximation (its three residual sign misses are exactly where it")
    print("  drops the path-phase cross terms the derivative keeps). BOUNDARIES: graph-family toy")
    print("  linear-response lane only (NOT the cubic-Coxeter geometric rows); first order in s at s=0;")
    print("  4 detector-dead families and 1 prune-zone family (R2_kreg_k8) are classified out with their")
    print("  free detector probabilities printed; convergence is exhibited on the 16-family ladder subset")
    print("  and the panel statistics on all 39 live families at s in {1e-3, 5e-4}. No audit grade is")
    print("  authored here; the independent audit lane adjudicates all ledger statuses.")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
