#!/usr/bin/env python3
"""Exact/numeric audit-companion runner for
`KOIDE_DELTA_RADIAN_PERIOD_PHYSICAL_NOT_VACUOUS_NARROW_THEOREM_NOTE_2026-06-04.md`.

Question chased
---------------
The AC_phi_lambda admission's delta leg reduces (per the retained radian-bridge
no-go `koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24`) to a single
residual sharpened as:

    RESIDUAL = period-1-rad  vs  canonical period-2*pi-rad  convention choice

i.e. the framework derives the DIMENSIONLESS rational 2/9 (Type-B count), and the
open step is reading it as a RADIAN phase delta.  The chased question: is that
period choice a VACUOUS convention (reclassifiable, like g_bare/Y0, which cancel
in observables) or a GENUINE physical admission?

Decisive test
-------------
A convention is VACUOUS iff every physical observable is invariant under the
convention choice (it cancels).  This runner shows the radian-PERIOD choice
FAILS that test: it changes the charged-lepton mass ratios by ~100x.

  PART A  Type-A/Type-B disjointness (reproves the radian no-go's core fact):
          periodic phase sources give q*pi (q rational); combinatorial sources
          give the pure rational 2/9; {q*pi : q in Q} cap Q = {0} (pi
          irrational), so 2/9 is not supplied as a literal radian by any
          periodic source.  The lane's natural angles are (2/9)*pi and
          2*pi*(2/9) -- never 2/9 itself.

  PART B  The period choice is PHYSICAL (the decisive test).  In the Brannen
          parameterization sqrt(m_k) ~ 1 + sqrt(2) cos(delta + 2*pi*k/3):
          - period-1 (delta = 2/9 rad), period-2*pi
            (delta = 2*pi*2/9), and period-pi (delta = (2/9)*pi) give
            different mass-ratio observables.
          The Koide Q=2/3 holds for ALL delta (it is the parameterization), so
          the period choice is invisible to Q but sets the individual masses.
          PDG values are printed as COMPARATOR data, not proof inputs.

  PART C  Contrast with a VACUOUS rescaling convention (g_bare/Y0 class): an
          overall scale / rescaling leaves ratio observables invariant
          (d(observable)/d(convention) = 0).  The radian-period choice does NOT
          (Part B), so it is structurally a different kind of object.

  PART D  Classification consistency checks: the period-change and
          rescaling-invariance tests imply the radian-period residual fails the
          vacuous-convention criterion. Registry and audit-status changes remain
          outside this runner.

This SHARPENS (does not reduce) the review boundary: it forecloses the
"delta's radian bridge is just a unit convention" reclassification route.

Run: python3 scripts/audit_companion_koide_delta_radian_period_physical_not_vacuous_2026_06_04.py
Exit 0 on all-PASS, 1 if any FAIL.
"""

from __future__ import annotations

import math
import sys

import sympy as sp

PASS = 0
FAIL = 0
RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    RESULTS.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{status}] {name}{suffix}")


# ===========================================================================
# Part A -- Type-A/Type-B disjointness (reproves the radian no-go core fact)
# ===========================================================================
print("\n=== Part A: {q*pi : q in Q} cap Q = {0}; 2/9 is a Type-B rational, "
      "not a Type-A radian ===")

# A.1 pi is irrational => for rational q != 0, q*pi is irrational (not in Q).
q = sp.Rational(2, 9)
qpi = q * sp.pi
check("(2/9)*pi is irrational (Type-A periodic angle is not the rational 2/9)",
      not qpi.is_rational, f"(2/9)*pi = {sp.nsimplify(qpi)} ~= {float(qpi):.6f}")

# A.2 The pure rational 2/9 (Type-B count) IS rational and != any nonzero q*pi.
check("2/9 is a pure rational (Type-B count), and 2/9 != (2/9)*pi",
      sp.Rational(2, 9).is_rational and sp.simplify(sp.Rational(2, 9) - qpi) != 0,
      "disjoint away from 0: a nonzero rational is not a rational multiple of pi")

# A.3 The lane's natural angles are (2/9)*pi and 2*pi*(2/9); neither equals 2/9.
ang_plancherel = sp.Rational(2, 9) * sp.pi          # (2/9)pi
ang_eta = 2 * sp.pi * sp.Rational(2, 9)             # 2pi(2/9)
check("natural lane angles (2/9)pi and 2pi(2/9) both differ from 2/9",
      sp.simplify(ang_plancherel - sp.Rational(2, 9)) != 0
      and sp.simplify(ang_eta - sp.Rational(2, 9)) != 0,
      f"(2/9)pi~={float(ang_plancherel):.4f}, 2pi(2/9)~={float(ang_eta):.4f}, 2/9~=0.2222")


# ===========================================================================
# Part B -- the period choice is PHYSICAL (decisive vacuous-vs-physical test)
# ===========================================================================
print("\n=== Part B: the radian-period choice changes the charged-lepton mass "
      "ratios by ~100x (PDG = comparator only) ===")

SQRT2 = math.sqrt(2.0)


def sqrt_masses(delta: float) -> list[float]:
    # Brannen / Koide Z3 parameterization (parameterization, not a proof input).
    return [1.0 + SQRT2 * math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3)]


def koide_Q(delta: float) -> float:
    s = sqrt_masses(delta)
    m = [x * x for x in s]
    return sum(m) / (sum(s) ** 2)


def mass_ratios(delta: float) -> tuple[float, float]:
    s = sqrt_masses(delta)
    m = sorted(x * x for x in s)            # ascending
    return m[2] / m[0], m[1] / m[0]         # (heaviest/lightest, middle/lightest)


# B.1 Koide Q = 2/3 for ALL delta (the period choice is invisible to Q).
qs = [koide_Q(d) for d in (0.05, 2 / 9, 1.0, 2 * math.pi * 2 / 9)]
q_invisible_to_period = all(abs(Q - 2 / 3) < 1e-12 for Q in qs)
check("Koide Q = 2/3 for every delta (period choice invisible to Q)",
      q_invisible_to_period, f"Q values: {[round(Q, 6) for Q in qs]}")

# B.2 PDG comparator sanity check. This is not used below to prove
# non-vacuity; non-vacuity is established by period-choice non-invariance.
# PDG charged-lepton masses (MeV) -- COMPARATOR data, not a proof input.
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
pdg_tau_e, pdg_mu_e = mtau / me, mmu / me
r1_te, r1_me = mass_ratios(2 / 9)
rel_err = abs(r1_te - pdg_tau_e) / pdg_tau_e + abs(r1_me - pdg_mu_e) / pdg_mu_e
pdg_comparator_close = rel_err < 1e-3
check("PDG comparator sanity: period-1 ratios are within <1e-3 of observed ratios",
      pdg_comparator_close,
      f"model (tau/e,mu/e)=({r1_te:.2f},{r1_me:.3f}) vs PDG ({pdg_tau_e:.2f},{pdg_mu_e:.3f}); relerr={rel_err:.2e}")

# B.3 Alternative period readings give different mass ratios from period-1.
# This, not the PDG comparison, is the load-bearing non-vacuity test.
r2_te, r2_me = mass_ratios(2 * math.pi * 2 / 9)
rpi_te, rpi_me = mass_ratios((2 / 9) * math.pi)
period_2pi_changes_ratios = (
    abs(r1_te - r2_te) / r1_te > 0.5
    and abs(r1_me - r2_me) / r1_me > 0.5
)
period_pi_changes_ratios = (
    abs(r1_te - rpi_te) / r1_te > 0.5
    and abs(r1_me - rpi_me) / r1_me > 0.5
)
check("period-2pi reading changes both mass ratios relative to period-1",
      period_2pi_changes_ratios,
      f"period-1=({r1_te:.2f},{r1_me:.3f}); period-2pi=({r2_te:.2f},{r2_me:.3f})")
check("period-pi reading changes both mass ratios relative to period-1",
      period_pi_changes_ratios,
      f"period-1=({r1_te:.2f},{r1_me:.3f}); period-pi=({rpi_te:.2f},{rpi_me:.3f})")

# B.4 Therefore the observable depends on the period choice.
period_choice_changes_observable = period_2pi_changes_ratios and period_pi_changes_ratios
check("the mass-ratio observable changes under the period choice (non-vacuous)",
      period_choice_changes_observable,
      f"|period-1 - period-2pi| / period-1 = {abs(r1_te - r2_te) / r1_te:.2f} (tau/e)")
check("Q stays invariant while mass ratios change",
      q_invisible_to_period and period_choice_changes_observable,
      "period choice is invisible to Q but visible to individual ratio observables")

print(
    "[INFO] PDG comparator only: "
    f"period-1 vs PDG relerr={rel_err:.2e}; "
    f"period-2pi tau/e={r2_te:.2f}; period-pi tau/e={rpi_te:.2f}"
)


# ===========================================================================
# Part C -- contrast with a VACUOUS rescaling convention (g_bare / Y0 class)
# ===========================================================================
print("\n=== Part C: a vacuous rescaling convention leaves ratio observables "
      "INVARIANT (unlike the radian period) ===")

# A vacuous convention (g_bare = beta-gauge rescaling; Y0 = overall hypercharge
# scale) acts as an overall rescaling.  Ratio observables are invariant under it:
# under m_k -> lambda * m_k, the ratio m_i/m_j is unchanged (d/d lambda = 0).
lam = sp.symbols("lambda", positive=True)
m_i, m_j = sp.symbols("m_i m_j", positive=True)
ratio_rescaled = (lam * m_i) / (lam * m_j)
rescaling_invariant = (
    sp.simplify(ratio_rescaled - m_i / m_j) == 0
    and sp.simplify(sp.diff(ratio_rescaled, lam)) == 0
)
check("vacuous rescaling m_k -> lambda m_k leaves ratio m_i/m_j invariant "
      "(d/dlambda = 0)",
      rescaling_invariant, "g_bare/Y0 are rescalings: they cancel in ratio observables")

# Contrast: the radian period enters as cos(delta) (a NON-scale, NON-cancelling
# argument), so it cannot be absorbed into an overall rescaling.  Numerically,
# Part B already shows the ratio is NOT invariant under the period choice.
d_sym = sp.symbols("delta", real=True)
obs = sp.cos(d_sym)
cos_delta_is_not_scale = sp.simplify(sp.diff(obs, d_sym)) != 0
check("radian period enters as cos(delta): NOT an overall scale, d/ddelta != 0",
      cos_delta_is_not_scale, "cos(delta) has nonzero derivative; the period choice does not cancel")


# ===========================================================================
# Part D -- classification consistency checks
# ===========================================================================
print("\n=== Part D: classification -- radian-period residual is a PHYSICAL "
      "admission, not a vacuous convention ===")

radian_period_is_physical = (
    q_invisible_to_period
    and period_choice_changes_observable
    and cos_delta_is_not_scale
)
vacuous_reclassification_fails = radian_period_is_physical and rescaling_invariant

check("RADIAN_PERIOD_CLASSIFICATION = physical under Brannen mass-ratio test",
      radian_period_is_physical,
      "Q is invariant, but mass ratios change through cos(delta)")
check("VACUOUS_RECLASSIFICATION_ROUTE = closed by failed invariance criterion",
      vacuous_reclassification_fails,
      "vacuous rescalings cancel; the radian-period choice does not")
print("[INFO] This runner does not derive delta, change the Tier-A registry, "
      "or set any audit status.")


# ===========================================================================
# Summary
# ===========================================================================
print("\n" + "=" * 70)
print(f"TOTAL: {PASS} PASS / {FAIL} FAIL  (out of {PASS + FAIL} checks)")
print("=" * 70)

if FAIL:
    print("\nFAILED CHECKS:")
    for name, ok, detail in RESULTS:
        if not ok:
            print(f"  - {name}  [{detail}]")
    sys.exit(1)

print("\nAll checks passed: under the Brannen parameterization, the radian-period "
      "choice changes charged-lepton mass ratios through cos(delta) and therefore "
      "fails the vacuous-convention invariance test. This does not derive delta, "
      "change the admitted-input registry, or set any audit status.")
sys.exit(0)
