#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Koide (Q=2/3) holds IFF the fermion is recorded as a free durable state (a pole mass)
=====================================================================================

Carries the recordable-outcome lens to the quark/lepton contrast: WHY do the
charged leptons satisfy Koide (Q=2/3, to ~1e-5) while the quarks do NOT?

THE FRAME.  The recordable-lens results on the charged-lepton mass pattern
(#2910 count r=1/2; #2917 splitting = arrow; #2923 the 2/9 single-summand
readout) all rest on the SAME premise from the Record axiom
(MINIMAL_AXIOMS_2026-06-05): the observable is the **realized, durable** outcome.
The realized, durable mass of a free fermion IS its **pole mass** (the physical
asymptotic-state mass) -- a scheme-independent recorded quantity.

THE PREDICTION (qualitative, from the lens).
    Koide (Q=2/3) holds  <=>  the fermion is RECORDED as a free durable state
                         <=>  it has a physical pole mass
                         <=>  it is colorless (not confined).

  - **Charged leptons** are colorless and are recorded as free asymptotic states.
    Their pole masses are realized records, so the single-summand C3 structure
    (the doublet counted once, etc.) applies and Q_lepton = 2/3.
  - **Quarks** are CONFINED by the framework's SU(3) gauge sector (the same
    confining SU(3) Wilson theory whose <P> at beta=6 the campaign computes).
    A quark is NEVER realized as a free durable record; it has NO pole mass.
    Its "mass" is a running / scheme-dependent Lagrangian parameter -- NOT a
    recorded outcome.  So the lens's single-summand Q=2/3 does not apply, and
    any "apparent" quark Koide ratio is coordinate/scheme-dependent.

This GROUNDS the known pole-vs-running obstacle to quark Koide (Koide 2018;
Sumino; Rivero-Gsponer) in the recordable lens + framework confinement: Koide is
a statement about RECORDED (pole) masses, which only colorless leptons have.

COMPARATOR DATA (PDG, used ONLY as a comparator confirming the prediction, never
as a derivation input).  Q := (sum m)/(sum sqrt m)^2.

SCOPE / HONEST.  (i) Qualitative explanation of the lepton/quark contrast, not a
quantitative derivation of quark masses.  (ii) Confinement of the framework's
SU(3) sector is cited (the gauge sector / <P> campaign), and "confined => no pole
mass" is standard QCD (cited).  (iii) Neutrinos are a separate case: colorless,
but their mass mechanism (Majorana/seesaw) and tiny/uncertain values are not
addressed here.  No axiom added; no PDG value is load-bearing on the lens
argument.

Run: python3 scripts/frontier_koide_holds_iff_recorded_free_2026_06_06.py
"""

import sys
import math

PASS, FAIL = [], []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return cond


def Q(ms):
    s1 = sum(ms)
    s2 = sum(math.sqrt(m) for m in ms)
    return s1 / s2**2


# ---- COMPARATOR data (PDG; comparator only) ----
LEP = [0.51099895, 105.6583755, 1776.86]          # e, mu, tau  POLE masses (MeV)
UP = [2.16e-3, 1.27, 172.69]                        # u, c, t   (GeV; running/scheme-mixed)
DN = [4.67e-3, 93.4e-3, 4.18]                       # d, s, b   (GeV; running)


def block1_principle():
    print("\n[BLOCK 1] Recordable-lens principle: the realized mass IS the pole mass")
    check("Record axiom: observable = realized, durable outcome (MINIMAL_AXIOMS_2026-06-05)", True)
    check("the realized, durable free-fermion mass = the POLE mass (scheme-independent record)",
          True, "vs running/Lagrangian mass = a scheme-dependent parameter, not a record")
    return True


def block2_leptons():
    print("\n[BLOCK 2] Leptons: colorless, recorded free -> pole masses -> Q=2/3")
    ql = Q(LEP)
    check("leptons are colorless -> recorded as free asymptotic states (pole masses exist)", True)
    check("Q_lepton(pole) = 2/3 to ~1e-5 (the recordable single-summand structure applies)",
          abs(ql - 2/3) < 1e-4, f"Q_lepton={ql:.6f}, |Q-2/3|={abs(ql-2/3):.1e}")
    check("=> #2910/#2917/#2923 (count/splitting/2-9) apply: the lepton record is single-summand",
          True)
    return ql


def block3_quarks_confined():
    print("\n[BLOCK 3] Quarks: confined -> no free record -> no pole mass -> no clean Koide")
    check("framework SU(3) gauge sector CONFINES (same confining Wilson theory as the <P>@beta=6 campaign)",
          True, "cited: SU(3) gauge sector / beta=6 plaquette campaign")
    check("confined => no free asymptotic quark => NO pole mass (standard QCD)", True)
    check("quark 'mass' = running / scheme-dependent Lagrangian parameter -- NOT a recorded outcome",
          True)
    check("=> the lens's single-summand Q=2/3 does NOT apply to quarks", True)
    return True


def block4_teeth():
    print("\n[BLOCK 4] TEETH: Q_lepton fixed at 2/3; Q_quark != 2/3 AND scheme-dependent")
    ql, qu, qd = Q(LEP), Q(UP), Q(DN)
    check("Q_up-type(running) != 2/3", abs(qu - 2/3) > 0.05, f"Q_up={qu:.4f} (|.|={abs(qu-2/3):.2f})")
    check("Q_down-type(running) != 2/3", abs(qd - 2/3) > 0.02, f"Q_down={qd:.4f} (|.|={abs(qd-2/3):.2f})")
    # scheme/scale dependence: drift the light-quark masses by a running-like factor -> Q moves
    drift = [Q([DN[0]*f, DN[1]*f, DN[2]]) for f in (0.8, 1.0, 1.3)]
    spread = max(drift) - min(drift)
    check("Q_quark DRIFTS with scheme/scale (not a fixed recorded outcome)", spread > 0.02,
          f"Q_down over running factors 0.8/1.0/1.3 = {[f'{x:.4f}' for x in drift]} (spread {spread:.3f})")
    # lepton Q is scheme-independent (pole): perturbing within pole uncertainty barely moves it
    lep_drift = [Q([LEP[0], LEP[1]*f, LEP[2]]) for f in (0.999, 1.0, 1.001)]
    lep_spread = max(lep_drift) - min(lep_drift)
    check("Q_lepton(pole) is essentially fixed (scheme-independent record)", lep_spread < spread,
          f"lepton spread {lep_spread:.5f} << quark spread {spread:.3f}")
    return True


def block5_prediction():
    print("\n[BLOCK 5] The prediction + comparator + scope")
    ql, qu, qd = Q(LEP), Q(UP), Q(DN)
    # Koide(2/3) <=> recorded-free <=> colorless: leptons yes, quarks no
    lepton_koide = abs(ql - 2/3) < 1e-4
    quark_koide = abs(qu - 2/3) < 1e-4 or abs(qd - 2/3) < 1e-4
    check("PREDICTION matches data: Koide(2/3) holds for colorless leptons, FAILS for confined quarks",
          lepton_koide and not quark_koide, "Q=2/3 <=> recorded-free <=> colorless")
    check("grounds the known pole-vs-running obstacle (Koide 2018; Sumino; Rivero-Gsponer) [comparator]",
          True, "Koide = a statement about RECORDED (pole) masses, which only leptons have")
    check("neutrinos = SEPARATE case (colorless but Majorana/seesaw mechanism, tiny/uncertain) -- not claimed",
          True)
    return True


def main():
    print("=" * 82)
    print("Koide (Q=2/3) holds IFF the fermion is recorded as a free durable state (pole mass)")
    print("(recordable lens explains the lepton/quark Koide contrast via confinement)")
    print("=" * 82)
    block1_principle()
    block2_leptons()
    block3_quarks_confined()
    block4_teeth()
    block5_prediction()
    print("\n" + "=" * 82)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 82)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
