#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Lorentz naturalness: supplied-parameter comparator estimate.

Given a Collins-type regenerated marginal LV coefficient and a supplied
asymptotically-free anomalous-dimension range, the gauge-flow suppression is far
too small to bridge representative LV comparator bounds.
=================================================================================

This quantifies the supplied-parameter comparator form of the open residual in
EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06, which
left open a physical-coefficient question: does the attractive IR flow plus the
a^-1=M_Pl hierarchy suppress a power-divergent marginal Lorentz-violation
coefficient below representative SME/GRB/Fermi-LAT comparator bounds?

Supplied-parameter answer (orders-of-magnitude scaling; standard one-loop
estimates): NO. If delta v_UV is O(alpha_s/4pi) and gamma = c_gamma alpha_s
with c_gamma in {1,2,3}, the IR suppression (mu/M_Pl)^gamma is too weak to
bridge the comparator bounds. This is the Collins-Perez-Sudarsky-Urrutia-
Vucetich (PRL 93 (2004) 191301) naturalness problem, used here as comparator
context rather than a framework-native derivation of the coefficient.

Structure (all robust at the ORDER-OF-MAGNITUDE level; O(1) coefficients estimated):

  A  UV REGENERATION (not Planck-suppressed).  The lattice dim-6 anisotropy feeds the
     marginal coefficient via a spatial power-divergent loop: delta v|_UV ~
     alpha_s(M_Pl)/(4pi).  At the framework's bare coupling beta=6 (g^2 = 2N/beta = 1
     for SU(3)), alpha_s(M_Pl) = g^2/4pi ~ 0.08, so delta v|_UV ~ 6e-3.

  B  SUPPLIED gamma range is SMALL.  gamma = c_gamma alpha_s(M_Pl), c_gamma ~ O(1-3) ->
     gamma ~ 0.08-0.24.  (Asymptotic freedom: the coupling is weak exactly where the
     regeneration happens.)

  C  REQUIRED gamma_crit.  To bring delta v|_UV below a bound over the hierarchy:
     gamma_crit = log10(delta v_UV / bound) / log10(M_Pl/mu).  For the tight bounds
     (photon, electron, nucleon) gamma_crit ~ 0.9-1.3; even the weakest (quark/gluon)
     needs gamma_crit ~ 0.5.

  D  THE GAP.  supplied gamma range (~0.1-0.24) << gamma_crit (~0.5-1.3): the net
     delta v|_IR ~ 1e-5..1e-8, leaving a 4-16 order gap to the bounds.

  E  WHAT THE COMPARATOR WOULD NEED.  The supplied estimate would need
     gamma >= gamma_crit ~ 1, e.g. an O(1) anomalous dimension over the hierarchy
     or a separate custodial mechanism. This runner does not derive the absence
     of every such mechanism from the framework.

No new axiom/primitive/import.  Literature (Collins et al 2004; Chadha-Nielsen 1983;
Bednik-Pujolas-Sibiryakov 2013; Nibbelink-Pospelov 2005) is comparator/scope only.
The robust output is the ORDER-OF-MAGNITUDE gap and the gamma_crit threshold; the
exact O(1) regeneration coefficient and the precise fixed-point gamma are named
open inputs. This runner is a supplied-parameter comparator, not a first-
principles no-go.

Run: python3 scripts/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.py
"""

from __future__ import annotations

import sys

import numpy as np

PASS, FAIL = 0, 0
M_PL = 1.22e19  # GeV


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 94 + f"\n{t}\n" + "-" * 94)


# experimental marginal-LV bounds (representative; SME / Kostelecky-Russell tables)
BOUNDS = [
    ("photon (GRB/Fermi-LAT)", 1e-20, 1e3),
    ("electron (clock/Penning)", 1e-22, 1e-3),
    ("nucleon (Hughes-Drever)", 1e-27, 1.0),
    ("quark/gluon (mesons,UHECR)", 1e-12, 1.0),  # weakest (colored sector)
]


def main():
    print("=" * 94)
    print("Lorentz naturalness: supplied-parameter comparator estimate")
    print("=" * 94)

    # =====================================================================
    section("Part A: UV regeneration delta v ~ alpha_s(M_Pl)/4pi (NOT Planck-suppressed)")
    # =====================================================================
    N = 3
    beta6 = 6.0
    g2 = 2 * N / beta6          # SU(3) Wilson: beta = 2N/g^2  =>  g^2 = 2N/beta = 1
    alpha_s = g2 / (4 * np.pi)
    dv_UV = alpha_s / (4 * np.pi)
    check("(A1) beta=6 -> g^2 = 2N/beta = 1 (SU(3)); alpha_s(M_Pl) = g^2/4pi ~ 0.08",
          abs(g2 - 1.0) < 1e-9 and abs(alpha_s - 0.0796) < 1e-3,
          detail=f"g^2={g2:.3f}, alpha_s(M_Pl)={alpha_s:.4f}")
    check("(A2) UV-regenerated marginal LV delta v|_UV ~ alpha_s/4pi ~ 6e-3 (loop- but NOT Planck-suppressed)",
          1e-3 < dv_UV < 1e-2, detail=f"delta v|_UV = {dv_UV:.3e}  (Collins et al: the lattice dim-6 feeds the marginal coeff)")

    # =====================================================================
    section("Part B: the supplied anomalous-dimension estimate is SMALL (asymptotic freedom)")
    # =====================================================================
    gammas = {cg: cg * alpha_s for cg in (1, 2, 3)}
    for cg, gm in gammas.items():
        print(f"     c_gamma={cg}: gamma = c_gamma*alpha_s(M_Pl) ~ {gm:.3f}")
    check("(B1) supplied gamma range ~ 0.08-0.24 (weak, because alpha_s is small at the UV regeneration scale)",
          all(0.05 < gm < 0.3 for gm in gammas.values()),
          detail="asymptotic freedom: the coupling is weak exactly where the regeneration occurs")

    # =====================================================================
    section("Part C: required gamma_crit to bridge the gap to each bound")
    # =====================================================================
    print(f"     {'observable':<28}{'bound':>9}{'mu(GeV)':>10}{'gamma_crit':>12}")
    gcrits = {}
    for name, bound, mu in BOUNDS:
        gcrit = np.log10(dv_UV / bound) / np.log10(M_PL / mu)
        gcrits[name] = gcrit
        print(f"     {name:<28}{bound:>9.0e}{mu:>10.0e}{gcrit:>12.2f}")
    check("(C1) tight bounds (photon/electron/nucleon) require gamma_crit ~ 0.9-1.3",
          all(gcrits[n] > 0.85 for n in ["photon (GRB/Fermi-LAT)", "electron (clock/Penning)", "nucleon (Hughes-Drever)"]),
          detail="even the WEAKEST (quark/gluon) needs gamma_crit ~ 0.5")
    check("(C2) the supplied gamma range (<=0.24) is BELOW even the weakest gamma_crit (~0.51)",
          max(gammas.values()) < gcrits["quark/gluon (mesons,UHECR)"],
          detail=f"max supplied gamma {max(gammas.values()):.3f} < quark/gluon gamma_crit {gcrits['quark/gluon (mesons,UHECR)']:.2f}")

    # =====================================================================
    section("Part D: the residual gap (net delta v|_IR vs the bounds)")
    # =====================================================================
    smallest_colored_gap = float("inf")
    for gamma in (0.1, 0.2, 0.3):
        mu = 1.0  # GeV
        dv_IR = dv_UV * (mu / M_PL) ** gamma
        gap_q = np.log10(dv_IR / 1e-12)   # vs quark/gluon (weakest)
        gap_g = np.log10(dv_IR / 1e-20)   # vs photon
        smallest_colored_gap = min(smallest_colored_gap, gap_q)
        print(f"     gamma={gamma}: delta v|_IR(1 GeV) ~ {dv_IR:.2e}  | gap vs quark/gluon(1e-12) = {gap_q:.1f} orders; vs photon(1e-20) = {gap_g:.1f}")
    check("(D1) even for the WEAKEST bound and the most-optimistic gamma, a multi-order gap REMAINS",
          smallest_colored_gap > 3.0,
          detail=(
              "smallest gap (quark/gluon, gamma=0.3) "
              f"~ {smallest_colored_gap:.1f} orders; tight bounds 12-16 orders"
          ))

    # =====================================================================
    section("Part E: what the supplied comparator would need")
    # =====================================================================
    check("(E1) closing the supplied-parameter gap needs gamma >= gamma_crit ~ 1",
          gcrits["photon (GRB/Fermi-LAT)"] > 1.0,
          detail="this is an arithmetic threshold, not a framework-native exclusion of all mechanisms")
    # the IR strong-QCD regime (alpha_s ~ 1) acts over too few e-folds to help:
    # extra suppression from the last ~1 e-fold near Lambda_QCD with gamma~1: factor ~ e^-1
    extra = np.exp(-1.0)
    check("(E2) IR strong-QCD (alpha_s~1, gamma~1) acts over too FEW e-folds (~1 near Lambda_QCD) -> negligible",
          extra > 0.1, detail=f"extra suppression ~ e^-1 = {extra:.2f}, vs the ~10^-14 needed")
    print("     Scope: a custodial symmetry or hidden framework mechanism is not ruled out here;")
    print("     the runner only quantifies what the supplied gamma range fails to do.")

    # =====================================================================
    section("Summary")
    # =====================================================================
    print("  A  UV regeneration delta v|_UV ~ alpha_s(M_Pl)/4pi ~ 6e-3 (beta=6; NOT Planck-suppressed).")
    print("  B  supplied gamma range ~ 0.08-0.24 (asymptotic freedom -> weak coupling at the regeneration scale).")
    print("  C  required gamma_crit ~ 0.9-1.3 (tight bounds), ~0.5 (weakest); supplied gamma range is BELOW all.")
    print("  D  net delta v|_IR ~ 1e-5..1e-8 -> 4-16 order GAP to the experimental LV bounds.")
    print("  E  the supplied estimate would need gamma~1 or a separate custodial/protection mechanism.")
    print("  => SUPPLIED-PARAMETER COMPARATOR: under the listed Collins/gamma/bound inputs,")
    print("     gauge-flow suppression is too small. This runner does not derive the")
    print("     regeneration coefficient, the physical gamma range, or absence of all")
    print("     hidden protection mechanisms from framework primitives.")
    print("\n" + "=" * 94)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 94)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
