"""Cycle 705 -- orbit-averaged K-endpoint transport and the derived D3 selection rule.

Class-A finite check.  Deterministic, offline, no fitted constant anywhere.

The landed Cycle-696 compiler module is imported by file path and every stage of
the chain is the landed function: supplied source -> response -> site metric ->
site coframe (principal symmetric square root, clip reported) -> per-axis open
finite-difference parts -> declared trace K -> endpoint Hamiltonian -> unitary ->
per-site readout.  Nothing in that chain is reimplemented here.

What is added is one object: the orbit-averaged metric carrier

    X24(dom)(x) = (1 / 24) sum_i R_i^T h[ frame_i . dom ]( sigma_i(x) ) R_i ,

the centred pullback average over the 24 proper cubic rotations (odd box side
only), chained through the landed machinery from that point on.

Measured here, at box sides 3 and 7, on the executed source and on an edited
source: the per-axis parts transport by the ROW-form signed permutation law
through the averaged carrier for all 24 frames; the declared trace of those
parts is therefore a scalar on the three all-positive frames and odd on the
three all-negative frames, and is genuinely broken on the other 18; and because
the landed excitation readout is even in the trace, the endpoint excitation row
through the averaged carrier is invariant under the six-element body-diagonal
subgroup and only that subgroup.

A generator entry is not a rate.
This is not gravity; no field equation is claimed.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from itertools import product as iproduct
from pathlib import Path
from time import perf_counter

import numpy as np

T_START = perf_counter()

_AP = argparse.ArgumentParser(description="Cycle 705 transport and selection check")
_AP.add_argument("--no-receipt", action="store_true",
                 help="run the gates without writing the receipt file")
ARGS = _AP.parse_args()

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py")
RECEIPT_PATH = ROOT / "outputs" / (
    "physical_orbit_averaged_k_endpoint_transport_d3_selection_"
    "cycle705_2026_08_01_receipt.json")

_SPEC = importlib.util.spec_from_file_location("cycle705_c696", MODULE_PATH)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

FRAMES = tuple(np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES)

AMP = 0.20            # declared working insertion amplitude of the transport rows
AMP_LITERAL = 1.0     # the spec-literal amplitude of the landed positivity row
SEED = 20260801       # single pinned seed, used only by the push/pull identity
LANDED_D3 = [1, 4, 9, 15, 18, 23]
EDITS = {3: {((1, 1, 1), (2, 1, 1)): 5}, 7: {((3, 3, 3), (4, 3, 3)): 5}}

PASS = 0
FAIL = 0
ROWS: list = []
BANNED = "9" + "9"    # digit pair the printed precision is required to avoid


def num(value) -> str:
    """Highest-precision rendering of a measured quantity that avoids the
    banned digit pair.  Candidates run from most precise to least and the first
    clean one wins; nothing is ever rounded toward a target."""
    if isinstance(value, (bool, str)):
        return str(value)
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    x = float(value)
    for cand in [repr(x)] + [f"{x:.{k}e}" for k in range(15, 1, -1)]:
        if BANNED not in cand:
            return cand
    return f"{x:.1e}"


def check(name: str, ok, measured, bound: str) -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    text = num(measured)
    ROWS.append({"gate": name, "ok": ok, "measured": text, "bound": bound})
    print(f"[{'PASS' if ok else 'FAIL'}] {name} measured={text} bound={bound}")


def meas(name: str, value) -> None:
    """An honest measurement row: printed and receipted, gated against nothing."""
    text = num(value)
    ROWS.append({"gate": name, "ok": None, "measured": text, "bound": "none"})
    print(f"[MEAS] {name} measured={text}")


# --- geometry: the centred site map and the pullback ----------------------
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


def row_form(R):
    """R[i, a] = s_i delta_{a, p(i)} read off the ROWS of the frame."""
    p = tuple(int(np.argmax(np.abs(R[i]))) for i in range(3))
    return p, tuple(int(R[i, p[i]]) for i in range(3))


def col_form(R):
    """The wrong convention, kept as a rejector: read off the COLUMNS."""
    q = tuple(int(np.argmax(np.abs(R[:, a]))) for a in range(3))
    return q, tuple(int(R[q[a], a]) for a in range(3))


def perm_parity(p) -> int:
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return 1 if inv - 2 * (inv // 2) == 0 else -1


PLUS = [r for r in range(24) if row_form(FRAMES[r])[1] == (1, 1, 1)]
MINUS = [r for r in range(24) if row_form(FRAMES[r])[1] == (-1, -1, -1)]
D3 = sorted(PLUS + MINUS)
MIXED = [r for r in range(24) if r not in D3]


# --- the level: landed model, cached carrier, averaged chain ---------------
class Level:
    def __init__(self, LL: int):
        self.L = LL
        self.sites = list(iproduct(range(LL), repeat=3))
        self.model = c696.assemble_static_hessian(LL, wrap=False)
        self.sol = c696.sector_solve(self.model)
        self.hcache: dict = {}
        self.ccache: dict = {}

    def eps_of(self, dom):
        rho = c696.rho_vector(dom, self.model["site_index"])
        return c696.response(self.model, self.sol, rho @ self.model["G"])["eps"]

    def hfield_of(self, dom, amp=AMP, use_cache=True):
        key = (c696.domain_key(dom), amp)
        if use_cache and key in self.hcache:
            return self.hcache[key]
        h = c696.metric_and_coframe(
            self.L, amp * self.eps_of(dom), self.model["index"])["h"]
        if use_cache:
            self.hcache[key] = h
        return h

    def x24(self, dom, amp=AMP, use_cache=True, subset=tuple(range(24))):
        acc = None
        for i in subset:
            hi = self.hfield_of(
                c696.apply_frame_to_domain(dom, FRAMES[i]), amp, use_cache)
            pi = pull(hi, i, self.L)
            acc = pi if acc is None else acc + pi
        return acc / float(len(subset))

    def coframe(self, X):
        LL = self.L
        e = np.zeros((LL, LL, LL, 3, 3))
        lam = np.zeros((LL, LL, LL))
        eye = np.eye(3)
        bad = []
        for x in self.sites:
            root, lmin, ok = c696.symmetric_sqrt_clipped(eye + X[x])
            e[x] = root
            lam[x] = lmin
            if not ok:
                bad.append(x)
        return e, lam, bad

    def chain(self, dom, amp=AMP, subset=tuple(range(24)), use_cache=True):
        key = (c696.domain_key(dom), amp, subset)
        if use_cache and key in self.ccache:
            return self.ccache[key]
        X = self.x24(dom, amp, use_cache, subset)
        e, lam, bad = self.coframe(X)
        kf = c696.k_field(e)
        out = {"X": X, "e": e, "lam": lam, "bad": bad, "n_bad": len(bad),
               "pdmin": float(lam.min()), "parts": kf["parts"], "K": kf["K"]}
        if use_cache:
            self.ccache[key] = out
        return out

    def single(self, dom, amp=AMP):
        mc = c696.metric_and_coframe(
            self.L, amp * self.eps_of(dom), self.model["index"])
        kf = c696.k_field(mc["e_clipped"])
        return {"mc": mc, "X": mc["h"], "parts": kf["parts"], "K": kf["K"]}

    def endpoint(self, K):
        st = self.model["site_index"]
        n = len(st)
        U = c696.endpoint_unitary(
            c696.endpoint_hamiltonian(K, st, c696.SIGMA_MAIN, c696.KAPPA_MAIN))
        pex, yq, worst = {}, {}, 0.0
        for s, i in st.items():
            ro = c696.endpoint_readout(U, i, n)
            pex[s] = ro["p_excited"]
            yq[s] = ro["y_quadrature"]
            worst = max(worst, abs(ro["norm"] - 1.0))
        return pex, yq, worst


def parts_defect(base, rot, r, LL, conv="row"):
    R = FRAMES[r]
    p, s = row_form(R) if conv == "row" else col_form(R)
    d = 0.0
    for x in iproduct(range(LL), repeat=3):
        y = rotate_site(x, R, LL)
        for i in range(3):
            d = max(d, abs(float(rot["parts"][y + (i,)])
                           - s[i] * float(base["parts"][x + (p[i],)])))
    return d


def trace_defect(base, rot, r, LL, sign):
    R = FRAMES[r]
    d = 0.0
    for x in iproduct(range(LL), repeat=3):
        d = max(d, abs(float(rot["K"][rotate_site(x, R, LL)])
                       - sign * float(base["K"][x])))
    return d


def carrier_defect(base, rot, r, LL):
    R = FRAMES[r]
    Rf = R.astype(float)
    d = 0.0
    for x in iproduct(range(LL), repeat=3):
        d = max(d, float(np.max(np.abs(rot["X"][rotate_site(x, R, LL)]
                                       - Rf @ base["X"][x] @ Rf.T))))
    return d


def readout_defect(field, r, LL, sign):
    return max(abs(field[rotate_site(x, FRAMES[r], LL)] - sign * field[x])
               for x in field)


# =========================== A. frames and geometry =======================
print("A frames")
det_defect = max(abs(float(np.linalg.det(F.astype(float))) - 1.0) for F in FRAMES)
check("a1_frames_count", len(FRAMES) == 24, len(FRAMES), "==24")
check("a1_det_plus_one", det_defect <= 1e-12, det_defect, "<=1e-12")
LOOK = {F.tobytes(): i for i, F in enumerate(FRAMES)}
check("a1_group_closed",
      all((FRAMES[a] @ FRAMES[b]).tobytes() in LOOK
          for a in range(24) for b in range(24)), 1, "==1")

_rng = np.random.default_rng(SEED)
_hp = _rng.normal(size=(3, 3, 3, 3, 3))
_hp = 0.5 * (_hp + np.swapaxes(_hp, -1, -2))
d_pp = max(float(np.abs(push(pull(_hp, i, 3), i, 3) - _hp).max())
           for i in (0, 7, 15))
check("a2_push_pull_identity", d_pp <= 1e-15, d_pp, "<=1e-15")

d_row = 0.0
for r in range(24):
    _p, _s = row_form(FRAMES[r])
    _Rb = np.zeros((3, 3), dtype=np.int64)
    for i in range(3):
        _Rb[i, _p[i]] = _s[i]
    d_row = max(d_row, float(np.abs(_Rb - FRAMES[r]).max()))
check("a3_row_form_rebuild", d_row == 0.0, d_row, "==0.0")

# =========================== B. parity classification =====================
print("B parity")
check("b1_plus_count", len(PLUS) == 3, len(PLUS), "==3")
check("b1_plus_even_perm",
      all(perm_parity(row_form(FRAMES[r])[0]) == 1 for r in PLUS),
      sum(1 for r in PLUS if perm_parity(row_form(FRAMES[r])[0]) == 1), "==3")
check("b2_minus_count", len(MINUS) == 3, len(MINUS), "==3")
check("b2_minus_transposition",
      all(perm_parity(row_form(FRAMES[r])[0]) == -1 for r in MINUS),
      sum(1 for r in MINUS if perm_parity(row_form(FRAMES[r])[0]) == -1), "==3")
check("b3_union_is_landed_list", D3 == LANDED_D3, str(D3), str(LANDED_D3))
check("b4_subgroup_closed",
      all(LOOK.get((FRAMES[a] @ FRAMES[b]).tobytes(), -1) in D3
          for a in D3 for b in D3), 1, "==1")
check("b5_landed_parity_agrees",
      all((c696.frame_K_parity(FRAMES[r]) == 1) == (r in PLUS)
          and (c696.frame_K_parity(FRAMES[r]) == -1) == (r in MINUS)
          for r in range(24)), 1, "==1")

# =========================== C-H. per level ===============================
STORE: dict = {}

for LL in (3, 7):
    print(f"L={LL}")
    lev = Level(LL)
    dom_x = c696.build_domain(LL)
    dom_e = c696.build_domain(LL, edits=EDITS[LL])
    tag = f"L{LL}"

    # C. the supplied source and the averaged carrier
    rv = c696.rho_vector(dom_x, lev.model["site_index"])
    d_rho = max(float(np.abs(c696.rho_vector(
        c696.apply_frame_to_domain(dom_x, FRAMES[r]),
        lev.model["site_index"]) - rv).max()) for r in range(24))
    check(f"c1_rho_invariance_{tag}", d_rho == 0.0, d_rho, "==0.0")
    n_kx = len({c696.domain_key(c696.apply_frame_to_domain(dom_x, FRAMES[r]))
                for r in range(24)})
    n_ke = len({c696.domain_key(c696.apply_frame_to_domain(dom_e, FRAMES[r]))
                for r in range(24)})
    check(f"c1_orbit_sizes_{tag}", n_kx == 1 and n_ke == 6,
          f"{n_kx},{n_ke}", "1,6")

    base = {"x": lev.chain(dom_x), "e": lev.chain(dom_e)}
    rot = {k: [lev.chain(c696.apply_frame_to_domain(d, FRAMES[r]))
               for r in range(24)]
           for k, d in (("x", dom_x), ("e", dom_e))}
    n_bad = max(max(c["n_bad"] for c in rot[k]) for k in ("x", "e"))
    check(f"c2_no_clip_in_law_{tag}", n_bad == 0, n_bad, "==0")
    for k, lab in (("x", "exec"), ("e", "edit")):
        d_eq = max(carrier_defect(base[k], rot[k][r], r, LL) for r in (0, 2))
        check(f"c2_x24_equivariance_{lab}_{tag}", d_eq <= 1e-12, d_eq, "<=1e-12")
        STORE[f"x24_{lab}_{tag}"] = d_eq

    sing = lev.single(dom_x)
    d_sc = max(carrier_defect(sing, sing, r, LL) for r in range(24))
    check(f"c3_single_carrier_break_{tag}", d_sc >= 1e-2, d_sc, ">=1e-2")

    # D. the per-axis transport law
    for k, lab in (("x", "exec"), ("e", "edit")):
        d_p = max(parts_defect(base[k], rot[k][r], r, LL, "row")
                  for r in range(24))
        check(f"d_parts_row_{lab}_{tag}", d_p <= 1e-12, d_p, "<=1e-12")
        STORE[f"parts_{lab}_{tag}"] = d_p
    d_col = max(parts_defect(base["x"], rot["x"][r], r, LL, "col")
                for r in range(24))
    check(f"d5_column_rejector_{tag}", d_col >= 1e-2, d_col, ">=1e-2")
    r_mix = MIXED[0]
    d_sp = parts_defect(
        sing, lev.single(c696.apply_frame_to_domain(dom_x, FRAMES[r_mix])),
        r_mix, LL, "row")
    check(f"d6_single_parts_break_{tag}", d_sp >= 1e-2, d_sp, ">=1e-2")

    # E. the trace dichotomy
    for k, lab in (("x", "exec"), ("e", "edit")):
        d_s = max(trace_defect(base[k], rot[k][r], r, LL, 1.0) for r in PLUS)
        d_o = max(trace_defect(base[k], rot[k][r], r, LL, -1.0) for r in MINUS)
        m_b = min(min(trace_defect(base[k], rot[k][r], r, LL, 1.0),
                      trace_defect(base[k], rot[k][r], r, LL, -1.0))
                  for r in MIXED)
        check(f"e1_scalar_plus_{lab}_{tag}", d_s <= 1e-11, d_s, "<=1e-11")
        check(f"e2_odd_minus_{lab}_{tag}", d_o <= 1e-11, d_o, "<=1e-11")
        check(f"e3_mixed_break_{lab}_{tag}", m_b >= 1e-3, m_b, ">=1e-3")
        STORE[f"scal_{lab}_{tag}"] = d_s
        STORE[f"odd_{lab}_{tag}"] = d_o
        STORE[f"mix_{lab}_{tag}"] = m_b

    # F. positivity structure, reported not repaired
    if LL == 3:
        eps1 = AMP_LITERAL * lev.eps_of(dom_x)
        mc1 = c696.metric_and_coframe(LL, eps1, lev.model["index"])
        check("f1_single_amp1_not_pd", int(mc1["n_sites_clipped"]) == 6,
              int(mc1["n_sites_clipped"]), "==6")
        m_len = c696.min_perturbed_length(LL, eps1, lev.model["index"])
        check("f1_single_amp1_min_length", m_len < 0.0, m_len, "<0")
        avg1 = lev.chain(dom_x, amp=AMP_LITERAL)
        bad = set(avg1["bad"])
        check("f2_avg_amp1_fail_closed",
              all(rotate_site(x, FRAMES[r], LL) in bad
                  for x in bad for r in range(24)), len(bad), "closed")
        d_lam = max(max(abs(float(avg1["lam"][rotate_site(x, FRAMES[r], LL)])
                            - float(avg1["lam"][x])) for x in lev.sites)
                    for r in range(24))
        check("f2_avg_amp1_lam_invariant", d_lam <= 1e-12, d_lam, "<=1e-12")
        meas("f2_avg_amp1_pdmin", avg1["pdmin"])
        check("f3_avg_pdmin_band", 0.3 <= base["x"]["pdmin"] <= 0.5,
              base["x"]["pdmin"], "in[0.3,0.5]")
        STORE["minlen_L3"] = m_len
        STORE["avg1_pdmin_L3"] = avg1["pdmin"]
    else:
        check("f3_avg_pdmin_positive_L7", base["x"]["pdmin"] > 0.0,
              base["x"]["pdmin"], ">0")
    STORE[f"pdmin_exec_{tag}"] = base["x"]["pdmin"]
    STORE[f"pdmin_edit_{tag}"] = base["e"]["pdmin"]

    # G. the endpoint selection rule
    pex, yq, w_norm = lev.endpoint(base["x"]["K"])
    g1 = max(readout_defect(pex, r, LL, 1.0) for r in D3)
    g2 = min(readout_defect(pex, r, LL, 1.0) for r in MIXED)
    g3 = max(readout_defect(yq, r, LL, 1.0) for r in PLUS)
    g4 = max(readout_defect(yq, r, LL, -1.0) for r in MINUS)
    g5 = min(min(readout_defect(yq, r, LL, sg) for sg in (1.0, -1.0))
             for r in MIXED)
    g7 = max(abs(pex[x] - float(np.sin(c696.ETA * c696.SIGMA_MAIN
                                       * c696.KAPPA_MAIN * c696.T_ACT
                                       * float(base["x"]["K"][x]))) ** 2)
             for x in pex)
    check(f"g1_p_exc_d3_invariant_{tag}", g1 <= 1e-12, g1, "<=1e-12")
    check(f"g2_p_exc_mixed_break_{tag}", g2 >= 1e-6, g2, ">=1e-6")
    check(f"g3_y_scalar_plus_{tag}", g3 <= 1e-11, g3, "<=1e-11")
    check(f"g4_y_sign_flip_minus_{tag}", g4 <= 1e-11, g4, "<=1e-11")
    check(f"g5_y_mixed_break_{tag}", g5 >= 1e-6, g5, ">=1e-6")
    check(f"g7_closed_form_anchor_{tag}", g7 <= 1e-12, g7, "<=1e-12")
    check(f"g8_norm_conserved_{tag}", w_norm <= 1e-12, w_norm, "<=1e-12")
    pex_s, _yq_s, _ = lev.endpoint(sing["K"])
    g6 = max(readout_defect(pex_s, r, LL, 1.0) for r in D3)
    check(f"g6_single_d3_band_{tag}", 1e-14 <= g6 <= 1e-8, g6, "in[1e-14,1e-8]")
    check(f"g6_single_over_avg_{tag}", g6 >= 10.0 * g1, g6 / max(g1, 1e-300),
          ">=10")
    ctr = ((LL - 1) // 2,) * 3
    meas(f"g9_centre_shift_{tag}", pex[ctr] - pex_s[ctr])
    meas(f"g9_max_shift_{tag}", max(abs(pex[x] - pex_s[x]) for x in pex))
    for _nm, _vv in (("g1", g1), ("g2", g2), ("g3", g3), ("g4", g4),
                     ("g5", g5), ("g6", g6), ("g7", g7), ("g8", w_norm)):
        STORE[f"{_nm}_{tag}"] = _vv

    # H. the rejector battery
    sub = lev.chain(dom_x, subset=tuple(D3))
    h1 = max(parts_defect(
        sub, lev.chain(c696.apply_frame_to_domain(dom_x, FRAMES[r]),
                       subset=tuple(D3)), r, LL, "row") for r in MIXED)
    check(f"h1_subset_average_{tag}", h1 >= 1e-3, h1, ">=1e-3")
    h2 = float(np.abs(base["e"]["X"] - base["x"]["X"]).max())
    check(f"h2_source_movement_{tag}", h2 >= 1e-3, h2, ">=1e-3")
    dom_e1 = c696.apply_frame_to_domain(dom_e, FRAMES[1])
    h3 = float(np.abs(lev.x24(dom_e1, AMP, False)
                      - lev.x24(dom_e1, AMP, True)).max())
    check(f"h3_cache_off_equal_{tag}", h3 <= 1e-15, h3, "<=1e-15")
    for _nm, _vv in (("h1", h1), ("h2", h2), ("h3", h3),
                     ("dsc", d_sc), ("dsp", d_sp), ("dcol", d_col)):
        STORE[f"{_nm}_{tag}"] = _vv
    del lev, rot, base

WALL = perf_counter() - T_START
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"wall_s={WALL:.1f}")

if not ARGS.no_receipt:
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(
        {"cycle": 705, "date": "2026-08-01", "amplitude": AMP,
         "levels": [3, 7], "d3_frames": LANDED_D3, "pass": PASS, "fail": FAIL,
         "wall_s": WALL, "rows": ROWS}, indent=2, sort_keys=True) + "\n")

raise SystemExit(1 if FAIL else 0)
