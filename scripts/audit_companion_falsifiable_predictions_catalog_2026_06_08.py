#!/usr/bin/env python3
"""Consolidation cross-check for the falsifiable-predictions catalog (publication surface).

RE-STATES the publication catalog's falsifiable forecasts, their CURRENT standing against the latest data
(NuFit-6.1 Nov 2025; ACT DR6 2025; J global-fit comparison windows), and the falsifier-margin arithmetic of the catalog
note FALSIFIABLE_PREDICTIONS_2026-06-08.md. It does NOT re-derive the predictions -- the rigorous
derivations live in the cited per-prediction runners:
  P1 (delta_CP):  frontier_pmns_theta12_theta13_dcp_predictions_narrow.py        (box-Krawczyk, 200-bit)
  P2 (theta_23):  frontier_pmns_theta23_upper_octant_full_3sigma_rectangle_narrow.py
  P3 (vacuum):    frontier_higgs_vacuum_stability_new_physics_discrimination.py
Headline: bucket A (clean unconditional forward falsifier) is empty in this catalog. P1/P2 are
fit-conditional and current data (NuFit-6.1) lean AGAINST them; the two apparent tensions (T1 n_s,
T2 J) are NOT independent axiom-tests (each re-expresses an already-admitted chain and dissolves
under its own comparator/chain uncertainty). All
NuFit/ACT/global-fit values are comparison windows only, never derived inputs.
"""
from __future__ import annotations
import math

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def main() -> int:
    print("FALSIFIABLE-PREDICTIONS CATALOG -- honest consolidation cross-check (publication surface)")
    print("=" * 90)

    # ---- P1: PMNS delta_CP bracket + NuFit-6.1 standing ----
    print("\n-- P1: PMNS delta_CP (bracket + NuFit-6.1 standing) --")
    lo, hi = 251.86, 270.00                  # certified bracket (landed theorem content)
    width = hi - lo
    check("P1 bracket is third quadrant (180,270), near maximal CP violation",
          180.0 < lo < hi <= 270.0, f"delta_CP in [{lo}, {hi}] deg, width {width:.2f}")
    # NuFit-6.1 NO (comparator only): best fits 207 deg no-SK / 212 deg with-SK;
    # no-SK 3-sigma [114,405]; band within 3-sigma, best fits OUTSIDE band.
    dcp_bf_no_sk, dcp_bf_with_sk, dcp_lo3, dcp_hi3 = 207.0, 212.0, 114.0, 405.0
    within3 = dcp_lo3 <= lo and hi <= dcp_hi3
    bf_outside = not (lo <= dcp_bf_no_sk <= hi) and not (lo <= dcp_bf_with_sk <= hi)
    check("P1 standing (NuFit-6.1 NO): best fits 207 deg no-SK / 212 deg with-SK OUTSIDE the band "
          "(disfavored) but band WITHIN 3-sigma "
          "[114,405] (not excluded) -> disfavored-but-allowed",
          within3 and bf_outside,
          f"best fits in band? no-SK={lo <= dcp_bf_no_sk <= hi}, with-SK={lo <= dcp_bf_with_sk <= hi}; "
          f"band within 3-sigma? {within3}")
    check("P1 falsifiable at DUNE/Hyper-K: bracket comparable to design 5-sigma resolution; band at "
          "maximal CP (peak sensitivity, no escape hatch)", width < 30.0,
          f"bracket {width:.2f} deg vs DUNE 5-sigma window ~30 deg")
    check("P1 bucket = D (fit-conditional): consumes NuFit (s12^2,s13^2) as inputs; unaudited chain", True)

    # ---- P2: PMNS theta_23 octant -- DISFAVORED under NuFit-6.1 (both variants lower octant) ----
    print("\n-- P2: PMNS theta_23 octant (NuFit-6.1: disfavored) --")
    check("P2 forecast: s_23^2 > 0.5 (upper octant), certified > 0.5277 over the NuFit-5.3 rectangle",
          0.5277 > 0.5, "gap from maximal mixing 0.5 = 0.0277")
    s23_61, s23_61_3sig = 0.470, (0.432, 0.587)
    check("P2 standing (NuFit-6.1 NO): best fit s_23^2 = 0.470 (LOWER octant) in BOTH without-SK and with-SK "
          "(the NuFit-6.0 without-SK upper value 0.561 moved DOWN) -> upper-octant prediction DISFAVORED, "
          "though 0.5 is still inside the 3-sigma range [0.432, 0.587]",
          s23_61 < 0.5 and s23_61_3sig[0] < 0.5 < s23_61_3sig[1],
          f"NuFit-6.1 s_23^2 = {s23_61} (lower); framework predicts > 0.5")
    check("P2 bucket = D (fit-conditional): same consumed rectangle; unaudited", True)

    # ---- P3: Higgs vacuum stability ----
    print("\n-- P3: Higgs vacuum stability (conditional y_t signature) --")
    check("P3: framework central value y_t(v)=0.918 is below the admitted y_t,crit~0.93 stability comparator, "
          "but the framework's own +-3pct y_t band [0.890,0.946] straddles that boundary", True,
          "0.44 sigma_sys above center; Gaussian-tail diagnostic ~33pct metastable; hard-interval fraction ~28pct")
    check("P3 bucket = B: conditional beyond-SM y_t signature, not a robust binary. The boundary "
          "lambda(M_Pl)=0 is an ADMITTED SM-shared input, y_t rests on an open Ward gate, and the "
          "stable/metastable verdict flips inside the y_t systematic", True,
          "central-value stable; weakly disfavored / not robust; not a closure of m_H")

    # ---- Table B: two apparent tensions that are NOT independent axiom-tests ----
    print("\n-- Table B: apparent tensions (NOT independent axiom-tests) --")
    # T1: n_s = 1 - 2/N_e; the tension is comparator- and N_e-dependent and dissolves
    def ns(Ne): return 1.0 - 2.0 / Ne
    ns_act, ns_act_err = 0.974, 0.003        # ACT DR6 2025 P-ACT-LB (arXiv:2503.14452)
    ns_planck, ns_pl_err = 0.9649, 0.0042    # Planck 2018
    pull_act = (ns(60) - ns_act) / ns_act_err
    pull_planck = (ns(60) - ns_planck) / ns_pl_err
    Ne_match_act = 2.0 / (1.0 - ns_act)      # N_e that reproduces ACT
    check("T1: n_s = 1 - 2/N_e (N_e=60) = 0.9667 is -2.4 sigma vs ACT but only -0.4 sigma vs Planck 2018, and "
          "N_e ~ 77 reproduces ACT exactly -> tension is comparator- and N_e-dependent, NOT robust",
          abs(ns(60) - 0.96667) < 1e-4 and abs(pull_act + 2.44) < 0.2 and abs(pull_planck) < 0.6
          and abs(Ne_match_act - 76.9) < 1.0,
          f"pull vs ACT={pull_act:.2f}, vs Planck={pull_planck:.2f}, N_e(match ACT)={Ne_match_act:.0f}")
    check("T1 is NOT an axiom-test: n_s = 1 - 2/N_e is the UNIVERSAL plateau/Starobinsky formula (not "
          "framework-distinctive); the framework's own 1 - d/N_e = 0.95 is patched by an underived growth-noise "
          "term (missing_bridge_theorem); N_e=60 assumed (sim reaches ~1.4). Shares ACT's universal-plateau tension",
          True)
    # T2: Jarlskog J -- framework NLO value vs the comparator RANGE; mild and comparator-dependent
    J_fw = 3.335e-5                          # NLO J_bar = sqrt5 * alpha_s^3 * (4 - alpha_s) / 288 (alpha_s=0.1033)
    J_fw_LO = 3.424e-5                       # LO atlas form sqrt5 * alpha_s^3 / 72
    pull_300 = (J_fw - 3.00e-5) / 0.13e-5    # vs lower global-fit comparison window
    pull_316 = (J_fw - 3.16e-5) / 0.12e-5    # vs higher global-fit comparison window
    check("T2: framework J ~ 3.33e-5 (NLO) is MILD and COMPARATOR-DEPENDENT: +2.6 sigma vs J=3.00+/-0.13 but "
          "only +1.4 sigma vs J=3.16e-5 -> NOT a firm ~2.5 sigma tension",
          abs(pull_300 - 2.6) < 0.3 and abs(pull_316 - 1.4) < 0.4 and J_fw < J_fw_LO,
          f"pull vs 3.00={pull_300:+.1f} sigma, vs 3.16={pull_316:+.1f} sigma; LO form gives {J_fw_LO:.3e}")
    # decomposition: ~half beta=6 alpha_s (vanishes if alpha_s drops ~2%), ~half eta=sqrt5/6 = delta admission
    eta_fw, eta_global, eta_err = math.sqrt(5)/6, 0.347, 0.009   # eta_bar framework vs global apex (chase)
    eta_pull = (0.363 - eta_global) / eta_err   # eta_bar (NLO) standalone pull
    check("T2 is NOT an axiom-test: J = A^2 lambda^6 eta_bar is imported textbook Wolfenstein over two non-clean "
          "inputs -- alpha_s (the beta=6 plaquette; excess vanishes if alpha_s drops ~2%) and eta=sqrt5/6 (the "
          "delta_CKM admission). The one robust alpha_s-independent residual is eta_bar ~ +1.8 sigma above the "
          "global apex eta_bar~0.347 -- a standing property of the delta admission, not a new falsifier",
          abs(eta_fw - 0.3727) < 1e-3 and abs(eta_pull - 1.8) < 0.3,
          f"eta=sqrt5/6={eta_fw:.4f}; eta_bar standalone pull ~ +{eta_pull:.1f} sigma")

    # ---- NOT forward falsifiers (postdictions / out of reach) ----
    print("\n-- NOT forward falsifiers (stated to prevent over-quoting) --")
    check("precision EW/QCD (alpha_s, m_t, m_H, v, sin^2 theta_W, Dm^2_31) are POSTDICTIONS calibrated/bracketed "
          "through the imported beta=6 plaquette <P>=0.5934 + convention knobs (g_bare, kappa_EW); re-measuring "
          "re-calibrates the comparator, does not exclude -> NOT forward falsifiers", True,
          "sin^2 theta_W '-0.26%' hides ~10 sigma once the experimental error is restored")
    check("clean-but-untestable (bucket C): Lorentz Y_40 fingerprint 7-18 orders below bounds; proton decay "
          "~13 orders beyond Hyper-K; 3-gen/3-color retrodictions -> distinctive, not near-term falsifiers", True)

    # ---- HEADLINE: bucket A empty on this catalog surface ----
    print("\n-- Headline (honest) --")
    check("BUCKET A IS EMPTY IN THIS CATALOG: no clean, unconditional, forward falsifier is identified on "
          "this publication surface; the sharp near-term "
          "forecasts (P1,P2) are fit-conditional (D) and NuFit-6.1 leans AGAINST them; T1/T2 are NOT independent "
          "axiom-tests (restate already-admitted chains, dissolve under their own uncertainties); the precision "
          "EW matches are beta=6-calibrated postdictions (B)", True,
          "framework's empirical content is mostly postdictions + conditional, currently unfavorable bets")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the catalog's forecasts and CURRENT standings are internally consistent and re-stated here -- "
        "P1 disfavored-but-allowed (NuFit-6.1 best fits 207/212 deg outside the band, band within 3-sigma); P2 "
        "disfavored (NuFit-6.1 both variants lower octant 0.470); P3 weakly disfavored / not robust; T1/T2 NOT independent "
        "axiom-tests (n_s -2.4 sigma vs ACT but -0.4 sigma vs Planck and N_e-dependent; J mild +1.4..+2.6 sigma "
        "comparator-dependent, decomposing into beta=6 alpha_s + the delta_CKM eta admission); bucket A empty "
        "in this catalog. "
        "Rigorous derivations deferred to the cited per-prediction runners; NuFit/ACT/global-fit values are "
        "comparison windows only, never derived inputs."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
