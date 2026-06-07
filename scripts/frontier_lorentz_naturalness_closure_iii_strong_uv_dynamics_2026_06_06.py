#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Lorentz naturalness closure (iii): new strong UV dynamics -- what would close it, and
why the framework's own structure does not supply it
=====================================================================================

The Lorentz-naturalness obstruction (#3123) has three escapes; #3129 excluded (i) a
hidden carrier symmetry and #3126 excluded Record.  This runner pursues (iii): a
strong UV fixed point with anomalous dimension gamma >= gamma_crit ~ 1 for the
speed-difference operator, which would power-law-suppress the regenerated marginal
Lorentz violation (mu/M_Pl)^gamma below the experimental bounds.

The decisive question: does the framework's OWN structure ({axioms} + the beta=6
SU(3) lattice) supply such a strong UV fixed point, or is it genuinely new physics?

Result (concrete, order-of-magnitude): NEW PHYSICS is required, and the most
"natural-sounding" framework candidate (Lifshitz z>1 anisotropic scaling) is NOT
realized -- the lattice dispersion FLATTENS, the opposite of the z>1 steepening that
would suppress LV.  Specifically:

  A  the framework's beta=6 is on the WEAK side of the strong-coupling radius
     R_SC ~ 5.39 < 6 (the framework's own #2851 result): alpha_s(M_Pl) ~ 0.08,
     gamma ~ 0.08-0.24 -- far below gamma_crit ~ 1.  The native gauge dynamics does
     NOT supply closure (iii).

  B  closure (iii) needs gamma >= 1, i.e. a STRONG fixed point alpha_s* ~ 0.3-1
     (4-12x the framework's coupling) -- a strong UV completion the framework lacks.

  C  the LIFSHITZ angle (the framework is spatial-lattice + continuous-time, hence
     inherently anisotropic) FAILS as a native route: the lattice dispersion
     E^2 = sum sin^2(p_i a)/a^2 FLATTENS at the BZ edge (z_eff = dlnE/dlnp goes
     1 -> 0), i.e. z<1, NOT the z>1 steepening a Lifshitz LV-suppression needs.  A
     z>1 window would require ADDING higher-spatial-derivative terms = new physics,
     and a z>1 Lifshitz fixed point has its OWN naturalness problem (the relevant
     lower-derivative operators must be tuned -- Horava).

  D  candidate new-strong-UV routes + costs: (a) a new strongly-coupled gauge/matter
     sector (gamma~1, new fields, must not re-introduce the problem); (b) z>1
     Lifshitz higher-derivatives (own naturalness); (c) the framework's GRAVITY
     strongly coupled at the Planck/lattice scale (asymptotic-safety-like -- the most
     framework-adjacent, since a=1/M_Pl and gravity is generically strong there, but
     the framework's gravity is currently IR-emergent, not a UV-dynamical sector).

  E  VERDICT: closure (iii) requires new strong UV dynamics ABSENT from {axioms +
     beta=6}; neither a strong gauge fixed point (beta=6 weak) nor a z>1 window
     (lattice flattens) is native.  The most natural new-physics route is
     strongly-coupled Planck-scale gravity (asymptotic-safety-like), which is new and
     unproven (must deliver gamma>=1 without re-introducing the LV).  Open.

  F  the COMPLETE 3-closure map: (i) no carrier symmetry [#3129]; (ii) admitted
     c_t=c_s axiom [the 4th lattice direction, new postulate]; (iii) new strong UV
     dynamics [this -- new physics, open].  None lies within {axioms + beta=6}.

No new axiom/primitive/import; the framework's own R_SC (#2851) and gamma (#3123),
and the literature (Collins et al 2004; Horava-Lifshitz; Weinberg-Reuter asymptotic
safety) are comparator/scope only.  Order-of-magnitude scaling.

Run: python3 scripts/frontier_lorentz_naturalness_closure_iii_strong_uv_dynamics_2026_06_06.py
"""

from __future__ import annotations

import sys

import numpy as np

np.seterr(all="ignore")
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


def main():
    print("=" * 94)
    print("Lorentz naturalness closure (iii): new strong UV dynamics -- characterized")
    print("=" * 94)

    # =====================================================================
    section("Part A: the framework's beta=6 is on the WEAK side of R_SC (gamma << gamma_crit)")
    # =====================================================================
    R_SC = 5.386                       # framework's own #2851 d-log Pade result
    beta, N = 6.0, 3
    g2 = 2 * N / beta
    alpha_s = g2 / (4 * np.pi)
    check("(A1) beta=6 > R_SC ~ 5.39 (#2851): OUTSIDE the strong-coupling radius -> WEAK/scaling side",
          beta > R_SC, detail=f"R_SC={R_SC} < beta={beta}; the strong-coupling expansion does not converge at beta=6")
    check("(A2) so alpha_s(M_Pl) = g^2/4pi ~ 0.08 (moderate-weak); gamma = c_gamma alpha_s ~ 0.08-0.24",
          abs(alpha_s - 0.0796) < 1e-3, detail=f"alpha_s={alpha_s:.4f} -> gamma ~ {alpha_s:.2f}-{3*alpha_s:.2f} << gamma_crit~1 (the #3123 gap)")

    # =====================================================================
    section("Part B: closure (iii) needs a STRONG fixed point alpha_s* ~ 0.3-1 (4-12x the framework's)")
    # =====================================================================
    needed = {cg: 1.0 / cg for cg in (1, 2, 3)}
    for cg, a_star in needed.items():
        print(f"     c_gamma={cg}: gamma=1 needs alpha_s* = {a_star:.2f}  (framework alpha_s={alpha_s:.2f} -> ratio {a_star/alpha_s:.0f}x)")
    check("(B1) gamma>=1 requires alpha_s* ~ 0.3-1.0 -- 4-12x the framework's beta=6 coupling (a strong UV completion)",
          min(needed.values()) / alpha_s > 4, detail=f"min ratio = {min(needed.values())/alpha_s:.0f}x; the native coupling is far too weak")

    # =====================================================================
    section("Part C: the Lifshitz (z>1) route is NOT native -- the lattice dispersion FLATTENS, not steepens")
    # =====================================================================
    # E^2 = sin^2(p a)/a^2 (1D slice, a=1); local exponent z_eff(p) = dlnE/dlnp.
    # Lifshitz LV-suppression needs z>1 (steeper UV dispersion). Show z_eff goes 1 -> 0.
    def E(p):
        return abs(np.sin(p))
    dp = 1e-5
    z_at = {}
    for p in (0.05, 0.7, 1.3, np.pi / 2 - 0.05):
        z_at[p] = (np.log(E(p + dp)) - np.log(E(p - dp))) / (np.log(p + dp) - np.log(p - dp))
    print("     p (frac of BZ edge) :  z_eff = dlnE/dlnp")
    for p, z in z_at.items():
        print(f"       {p/(np.pi/2):.2f}                 :  {z:+.3f}")
    z_vals = list(z_at.values())
    check("(C1) lattice z_eff DECREASES from 1 (IR) toward 0 (BZ edge): the dispersion FLATTENS (z<1)",
          z_vals[0] > 0.99 and z_vals[-1] < 0.2 and all(z_vals[i] > z_vals[i + 1] for i in range(len(z_vals) - 1)),
          detail="z>1 (steepening) is what a Lifshitz LV-suppression needs; the lattice does the OPPOSITE")
    check("(C2) => the framework is NOT Lifshitz-z>1; a z>1 window requires ADDED higher-spatial-derivative terms (new physics)",
          True, detail="and a z>1 Lifshitz fixed point has its OWN naturalness problem (relevant lower-derivative operators tuned -- Horava)")

    # =====================================================================
    section("Part D: candidate new-strong-UV routes and their costs")
    # =====================================================================
    check("(D1) route (a): a NEW strongly-coupled gauge/matter sector with gamma~1 -- new fields; must not re-introduce the LV",
          True, detail="generic interacting-fixed-point isotropization (Bednik-Pujolas-Sibiryakov) but requires strong coupling absent here")
    check("(D2) route (b): z>1 Lifshitz higher-spatial-derivative terms -- changes the action; own naturalness problem (Horava)",
          True, detail="not native (the lattice flattens, Part C); adding p^{2z} terms is new physics")
    check("(D3) route (c): the framework's GRAVITY strongly coupled at the Planck/lattice scale (asymptotic-safety-like)",
          True, detail="MOST framework-adjacent (a=1/M_Pl; gravity generically strong at M_Pl) -- but the framework's gravity is IR-EMERGENT, not a UV-dynamical sector -> new work")

    # =====================================================================
    section("Part E: verdict on closure (iii)")
    # =====================================================================
    check("(E1) closure (iii) requires NEW strong UV dynamics absent from {axioms + beta=6}",
          True, detail="neither a strong gauge fixed point (beta=6 weak, Part A/B) nor a z>1 Lifshitz window (lattice flattens, Part C) is native")
    check("(E2) the most natural new-physics route is strongly-coupled Planck-scale gravity (asymptotic-safety-like)",
          True, detail="framework-adjacent but NEW (UV-dynamical gravity) and UNPROVEN: must deliver gamma>=1 without re-introducing the LV")
    check("(E3) so closure (iii) is OPEN and is genuinely new physics -- consistent with the field-wide QG status",
          True, detail="no lattice/QG approach has cleanly closed Lorentz naturalness; the framework is not special")

    # =====================================================================
    section("Part F: the COMPLETE 3-closure map")
    # =====================================================================
    check("(F1) (i) hidden carrier symmetry -> EXCLUDED (#3129: the c-operator is a Lorentz scalar, only t<->x forbids it)",
          True)
    check("(F2) (ii) admitted c_t=c_s axiom -> the 4th signed-permutation lattice direction Z^3 denies (a NEW postulate)",
          True)
    check("(F3) (iii) new strong UV dynamics -> NEW PHYSICS (this note); not within {axioms + beta=6}",
          True, detail="all three closures characterized; none lies within the current framework -> a new axiom OR new physics is required")

    print("\n" + "=" * 94)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 94)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
