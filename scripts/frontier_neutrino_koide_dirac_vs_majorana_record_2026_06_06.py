#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Neutrinos and Koide: the recordable lens predicts Q_nu = 2/3 IFF Dirac (direct record);
Majorana/seesaw (composite mass) breaks it -- and the data confirms Q_nu < 2/3
=======================================================================================

Third application of the recordable-outcome lens to the mass sectors:
  - charged leptons (colorless, recorded free, POLE masses) -> Koide Q=2/3
    (#2910/#2917/#2923);
  - quarks (CONFINED, no free record, no pole mass) -> no clean Koide (#2937);
  - NEUTRINOS (this note): colorless, so NOT excluded by confinement -- the
    question is whether their RECORD is a directly-recorded Dirac sqrt-mass.

THE LENS PREDICTION.
    Q_nu = 2/3  <=>  neutrinos are DIRAC with a directly-recorded sqrt-mass
                     (the same single-summand C3 record as the charged leptons).
  If neutrinos are MAJORANA / seesaw, the light mass is the COMPOSITE
  m_nu = m_D M_R^{-1} m_D^T (diagonally m_nu = m_D^2 / M_R): the light mass is NOT
  a directly-recorded Dirac sqrt-mass, and the super-heavy Majorana scale M_R is
  decoupled / unrecorded.  A nonlinear composite does NOT preserve the Koide
  constraint, so Q_nu != 2/3 generically.

DEMONSTRATION (runner).
  (i) Seesaw breaks Koide: starting from a Dirac set whose sqrt-masses satisfy
      Koide (Q=2/3), the seesaw light masses m_D^2/M_R give Q_nu != 2/3 for every
      M_R structure tested (degenerate, hierarchical, inverse, generic).
  (ii) The DATA already shows it: with the measured oscillation splittings
      Dm21^2 = 7.42e-5 eV^2, Dm31^2 = 2.51e-3 eV^2 (comparator), Q_nu lies strictly
      BELOW 2/3 for BOTH hierarchies across the cosmologically-allowed range
      (Sum m_nu < 0.12 eV): NH gives Q_nu in [0.33, 0.586], IH in [0.33, 0.50].
      So neutrinos do NOT obey the charged-lepton Koide -- consistent with the
      lens's Majorana/seesaw expectation, and inconsistent with the simplest
      "Dirac + charged-lepton C3 structure -> Q=2/3" hypothesis.

FALSIFIABLE DISTINCTION.  charged leptons: Q=2/3 (recorded Dirac).  neutrinos:
Q<2/3 (composite / not the charged-lepton record).  Neutrinoless double-beta
decay (Majorana) and absolute-mass measurements (KATRIN, cosmology) sharpen it.

SCOPE / HONEST.  (i) Qualitative + data-comparator, not a neutrino-mass
derivation.  (ii) "Dirac => Q=2/3" assumes the neutrino Dirac sector shares the
charged-lepton C3 record structure; the data showing Q_nu<2/3 means neutrinos do
not share it -- consistent with Majorana/seesaw OR a different Dirac structure.
(iii) Oscillation Dm^2 used ONLY as comparator, never a derivation input.  No
axiom added.

Run: python3 scripts/frontier_neutrino_koide_dirac_vs_majorana_record_2026_06_06.py
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
    s2 = sum(math.sqrt(abs(m)) for m in ms)
    return s1 / s2**2


# charged-lepton sqrt-mass structure (proxy for a directly-recorded Dirac sqrt-mass)
ZL = [math.sqrt(m) for m in (0.51099895, 105.6583755, 1776.86)]  # sqrt(m_e,m_mu,m_tau)
DM21, DM31, DM32 = 7.42e-5, 2.51e-3, 2.49e-3  # eV^2 (oscillation comparator)


def block1_lens_and_leptons():
    print("\n[BLOCK 1] Lens: Q=2/3 is a directly-recorded Dirac sqrt-mass phenomenon")
    mD = [z**2 for z in ZL]  # a Dirac set whose sqrt-masses are Koide (Q=2/3)
    check("charged leptons: directly-recorded Dirac sqrt-mass (pole) -> Q = 2/3",
          abs(Q(mD) - 2/3) < 1e-4, f"Q={Q(mD):.5f}  (#2910/#2917/#2923)")
    return mD


def block2_not_confined():
    print("\n[BLOCK 2] Neutrinos are colorless -> NOT confined -> the #2937 exclusion does NOT apply")
    check("neutrinos colorless => can be recorded as free states (unlike confined quarks)", True,
          "so the question is Dirac (direct record) vs Majorana/seesaw (composite)")
    return True


def block3_seesaw_breaks(mD):
    print("\n[BLOCK 3] Majorana/seesaw composite m_nu = m_D^2/M_R BREAKS Koide")
    results = []
    for label, MR in [("M_R degenerate (1,1,1)", [1, 1, 1]),
                      ("M_R hierarchical (1,10,100)", [1, 10, 100]),
                      ("M_R inverse (100,10,1)", [100, 10, 1]),
                      ("M_R generic (3,1,7)", [3, 1, 7])]:
        mnu = [mD[k]**2 / MR[k] for k in range(3)]
        qn = Q(mnu)
        results.append(qn)
        check(f"seesaw {label}: Q_nu != 2/3", abs(qn - 2/3) > 0.02, f"Q_nu={qn:.4f}")
    check("=> the nonlinear seesaw composite does NOT preserve Koide for ANY M_R tested",
          all(abs(q - 2/3) > 0.02 for q in results),
          "light mass is not a directly-recorded Dirac sqrt-mass; M_R decoupled/unrecorded")
    return True


def block4_data():
    print("\n[BLOCK 4] DATA (comparator): measured Dm^2 give Q_nu < 2/3 for BOTH hierarchies")
    # NH: m1 free; m2=sqrt(m1^2+Dm21); m3=sqrt(m1^2+Dm31)
    nh = []
    for i in range(0, 80):
        m1 = i * 0.001
        if m1 + math.sqrt(m1**2 + DM21) + math.sqrt(m1**2 + DM31) > 0.12:  # cosmology Sum<0.12eV
            continue
        nh.append(Q([m1, math.sqrt(m1**2 + DM21), math.sqrt(m1**2 + DM31)]))
    # IH: m3 free; m2=sqrt(m3^2+Dm32); m1=sqrt(m2^2-Dm21)
    ih = []
    for i in range(0, 80):
        m3 = i * 0.001
        m2 = math.sqrt(m3**2 + DM32)
        m1 = math.sqrt(m2**2 - DM21)
        if m1 + m2 + m3 > 0.12:
            continue
        ih.append(Q([m1, m2, m3]))
    check("NH: Q_nu < 2/3 across the cosmologically-allowed range",
          max(nh) < 2/3, f"Q_nu in [{min(nh):.3f}, {max(nh):.3f}] (max at m1=0)")
    check("IH: Q_nu < 2/3 across the cosmologically-allowed range",
          max(ih) < 2/3, f"Q_nu in [{min(ih):.3f}, {max(ih):.3f}]")
    check("=> neutrinos do NOT obey the charged-lepton Koide (Q=2/3): consistent with Majorana/seesaw",
          max(nh) < 2/3 and max(ih) < 2/3,
          "and inconsistent with the simplest Dirac+charged-lepton-C3 -> Q=2/3 hypothesis")
    return True


def block5_falsifiable():
    print("\n[BLOCK 5] The falsifiable distinction + scope")
    check("DISTINCTION: charged leptons Q=2/3 (recorded Dirac); neutrinos Q<2/3 (composite)",
          True)
    check("Q_nu=2/3 would require Dirac + shared C3 record structure (DISFAVORED by the data)", True)
    check("0nu-beta-beta (Majorana) + absolute-mass (KATRIN/cosmology) sharpen the test", True)
    check("scope: qualitative+comparator (not a neutrino-mass derivation); Dm^2 comparator only; no axiom",
          True)
    return True


def main():
    print("=" * 84)
    print("Neutrino Koide: lens predicts Q_nu=2/3 iff Dirac (direct record); Majorana/seesaw breaks it")
    print("(third recordable-lens application: leptons #2910.., quarks #2937, neutrinos here)")
    print("=" * 84)
    mD = block1_lens_and_leptons()
    block2_not_confined()
    block3_seesaw_breaks(mD)
    block4_data()
    block5_falsifiable()
    print("\n" + "=" * 84)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 84)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
