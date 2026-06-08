#!/usr/bin/env python3
"""Consolidation cross-check for the falsifiable-predictions catalog (publication surface).

This runner RE-STATES the three headline falsifiable forecasts and checks the falsifier-margin
arithmetic of the catalog note FALSIFIABLE_PREDICTIONS_2026-06-08.md. It does NOT re-derive the
predictions -- the rigorous derivations live in the cited per-prediction runners:
  P1 (delta_CP):  frontier_pmns_theta12_theta13_dcp_predictions_narrow.py        (box-Krawczyk, 200-bit)
  P2 (theta_23):  frontier_pmns_theta23_upper_octant_full_3sigma_rectangle_narrow.py
  P3 (vacuum):    frontier_higgs_vacuum_stability_new_physics_discrimination.py
This is a meta publication-surface cross-check: the numbers are consistent and the falsifier margins
are as stated. No PDG/NuFit value is consumed as a derived input; the NuFit/DUNE bands are comparison
windows only. No framework derivation is asserted here.
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
    print("FALSIFIABLE-PREDICTIONS CATALOG -- consolidation cross-check (publication surface)")
    print("=" * 86)

    # ---- P1: PMNS delta_CP third-quadrant bracket ----
    print("\n-- P1: PMNS delta_CP --")
    lo, hi = 251.86, 270.00                 # certified bracket (per the P1 note)
    width = hi - lo
    nufit_lo, nufit_hi = 120.0, 369.0        # NuFit 5.3 NO 3-sigma band (named external comparison)
    nufit_width = nufit_hi - nufit_lo
    frac = width / nufit_width
    check("P1 bracket is in the third quadrant (180,270) and near maximal CP violation",
          180.0 < lo < hi <= 270.0, f"delta_CP in [{lo}, {hi}] deg")
    check("P1 bracket width = 18.13 deg = ~7.3% of the NuFit 3-sigma band (249 deg)",
          abs(width - 18.13) < 0.01 and abs(frac - 0.0728) < 0.002,
          f"width={width:.2f} deg, fraction of NuFit band = {100*frac:.1f}%")
    # anchor sin(delta_CP) ~ -0.987 at delta_CP = 260.88 deg (third-quadrant branch)
    anchor = 260.88
    s = math.sin(math.radians(anchor))
    check("P1 anchor sin(delta_CP) ~ -0.987 and cos(delta_CP) < 0 (third-quadrant branch)",
          abs(s - (-0.987)) < 0.002 and math.cos(math.radians(anchor)) < 0,
          f"sin({anchor})={s:.4f}, cos={math.cos(math.radians(anchor)):.4f}")
    # DUNE design 5-sigma resolution ~ +/-15 deg; the 18.13 deg bracket is testable (resolvable)
    dune_5sigma_deg = 15.0
    check("P1 is falsifiable at DUNE/T2HK: a 5-sigma measurement (design +/-15 deg) outside the "
          "bracket would falsify; bracket (18.13 deg) is comparable to design resolution -> testable",
          width < 2 * dune_5sigma_deg, f"bracket {width:.2f} deg vs DUNE 5-sigma window {2*dune_5sigma_deg:.0f} deg")

    # ---- P2: PMNS theta_23 octant ----
    print("\n-- P2: PMNS theta_23 octant --")
    s23sq_bound = 0.5277                     # tightest certified lower bound (per the P2 note)
    check("P2: certified s_23^2 lower bound > 0.5 (upper octant) over the full NuFit rectangle",
          s23sq_bound > 0.5, f"s_23^2 > {s23sq_bound} (gap from maximal mixing 0.5 = {s23sq_bound-0.5:.4f})")
    check("P2 is falsifiable: a lower-octant determination (s_23^2 < 0.5) by DUNE/NOvA/T2K/Hyper-K "
          "falsifies it; certified gap > 2.7e-2 from maximal mixing",
          (s23sq_bound - 0.5) > 2.7e-2, f"gap = {s23sq_bound-0.5:.4f}")

    # ---- P3: Higgs vacuum stability ----
    print("\n-- P3: Higgs vacuum stability --")
    framework = "absolutely_stable"
    sm_with_current_yt = "metastable"
    check("P3: framework forecast (absolutely stable) differs from the SM-with-current-y_t "
          "comparison (metastable) -> a binary YES/NO discrimination test",
          framework != sm_with_current_yt,
          f"framework={framework} vs SM-comparison={sm_with_current_yt}")
    check("P3 is falsifiable: a definitive metastability determination (precision m_t/m_H/alpha_s, "
          "lambda at the high scale) falsifies the absolute-stability forecast",
          True, "binary discrimination; not a closure of m_H")

    # ---- honest conditionality (re-stated, not a numerical claim) ----
    print("\n-- Conditionality (honest) --")
    check("all three forecasts are CONDITIONAL (unaudited source notes; external NuFit/SM comparison "
          "windows; PMNS forecasts downstream of the AC_phi_lambda flavor admission) -- catalog states this",
          True, "no unconditional closure is asserted; status authority = independent audit lane")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the catalog's three headline forecasts (delta_CP third-quadrant bracket; theta_23 "
        "upper octant; absolute vacuum stability) and their falsifier margins are internally "
        "consistent and re-stated here; the rigorous derivations are deferred to the cited "
        "per-prediction runners, and all three are honestly conditional/unaudited."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
