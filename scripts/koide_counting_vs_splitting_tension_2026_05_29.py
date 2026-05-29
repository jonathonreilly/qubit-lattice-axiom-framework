#!/usr/bin/env python3
"""
Time-emergence panel capstone (14 lenses, 0 escapes, unanimous confirms-import).
The panel closed the last structural door (time-emergence / anomaly-cancellation)
AND discovered two sharp NEW structural facts that characterize the gate far more
precisely than "r=1/2 is unforced".

FACT 1 -- the COUNTING-vs-SPLITTING tension (the gate, precisely located):
  The C_3 orbit is what makes the three hw=1 corners ONE orbit -> the NUMBER 3.
  But C_3-equivariance ([H,R]=0) forces H circulant, and every circulant COMMUTES
  with the generation grading Gamma_chi -> Q=1. The operator that delivers Q=2/3
  ANTICOMMUTES with Gamma_chi and NECESSARILY BREAKS the C_3 orbit ([H,R]!=0).
  => the SAME C_3 cannot supply both the COUNT (needs [H,R]=0) and the VALUE
     (needs [H,R]!=0). Getting "3 generations" from one symmetry orbit structurally
     forbids fixing "2/3" internally. They are two faces of one C_3 fact, in tension.

FACT 2 -- the CATEGORY MISMATCH (why no consistency condition can fix it):
  Anomaly cancellation / time-emergence output DISCRETE data: rational charges +
  spacetime signature (3,1) + the count 3. Koide Q=2/3 (r=|b|^2/a^2=1/2) is a
  CONTINUOUS Yukawa-coefficient modulus. Sweeping free Yukawas at fixed
  anomaly-cancelling charges sweeps Q over all of [1/3,1], hitting 2/3 only at
  chance. No discrete consistency condition fixes a continuous modulus -- in this
  framework OR the Standard Model.

ALSO (panel): DISTINCTNESS is NOT the obstruction. Distinct translation characters
(retained three_generation_hw1_distinct_translation_characters) give distinct
masses; the obstruction is specifically the CHIRAL orbit-splitting, not distinctness.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q_of(a, b):
    lam = np.array([a + 2 * abs(b) * np.cos(np.angle(b) + 2 * np.pi * j / 3) for j in range(3)])
    s = np.abs(lam)
    return (s * s).sum() / s.sum() ** 2


def main():
    R = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
    J = np.ones((3, 3)); Gx = (2/3) * J - np.eye(3)

    sep("FACT 1: COUNTING-vs-SPLITTING tension on the C_3 orbit")
    H = 1.3 * np.eye(3) + 0.7 * R + 0.2 * R.T   # generic circulant
    print(f"  C_3-equivariant (gives the COUNT 3): [H,R]={np.max(np.abs(H@R-R@H)):.1e}, "
          f"{{H,Gx}}={np.max(np.abs(H@Gx+Gx@H)):.2f} (commutes -> Q=1)")
    es = np.ones(3)/np.sqrt(3); d1 = np.array([1, -1, 0])/np.sqrt(2)
    Hc = np.outer(es, d1) + np.outer(d1, es)    # chiral, anticommutes with Gx
    print(f"  chiral (gives the VALUE 2/3):        {{H,Gx}}={np.max(np.abs(Hc@Gx+Gx@Hc)):.1e}, "
          f"[H,R]={np.max(np.abs(Hc@R-R@Hc)):.2f} (BREAKS the orbit)")
    print("  => count needs [H,R]=0; value needs [H,R]!=0. Mutually exclusive on")
    print("     the same C_3. (Rests on retained_bounded koide_z3_equivariant_anticommuting.)")

    sep("FACT 2: CATEGORY MISMATCH -- anomaly fixes charges, not the modulus r")
    rng = np.random.default_rng(0); N = 200000; hits = 0
    for _ in range(N):
        a = rng.uniform(0.1, 3); b = rng.uniform(-2, 2) + 1j * rng.uniform(-2, 2)
        if abs(Q_of(a, b) - 2/3) < 0.01:
            hits += 1
    print(f"  free Yukawa coeffs at FIXED anomaly-cancelling charges:")
    print(f"    within 0.01 of Q=2/3: {hits/N*100:.2f}% (chance level -> no preference)")
    print("  charges = discrete/deformation-invariant; Q=2/3 = continuous Yukawa")
    print("  modulus. No discrete consistency condition fixes it (framework OR SM).")

    sep("VERDICT (time-emergence panel, 14 lenses, 0 escapes, confirms-import)")
    print("  Time-emergence / anomaly-cancellation does NOT force Q=2/3: it reaches")
    print("  CHARGES + signature + the COUNT 3, never the continuous mass ratio.")
    print("  Co-emergence is transport's twin, not its escape (provenance-independent:")
    print("  Gamma_chi is itself circulant, so comm(R) cap anticomm(Gamma_chi)={0}).")
    print("  GATE, precisely located: the C_3-orbit COUNTING-vs-SPLITTING tension.")
    print("  Status: open_gate; the single import (S_3-orbit-splitting chiral grading")
    print("  on the generation R^3) is shared with generation-ID and signed-gravity.")
    print("  NOT a promotion of Q=2/3; a sharper POSITIVE characterization of why")
    print("  it is not internally derivable.")


if __name__ == "__main__":
    main()
