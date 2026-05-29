#!/usr/bin/env python3
"""
Panel findings runner: the F1 (equal-block, Q=2/3) selection crux.

14-lens panel (10 physics + 4 meta) verdict: NO import-free, non-circular
derivation of F1 exists. Every canonical measure A1+A2+retained supplies
counts the C_3 doublet isotype by its REAL DIMENSION (2), forcing
F3 = (1,2) -> Q = 1. F1 = (1,1) -> Q = 2/3 requires counting the
2-real-dim doublet as ONE unit.

This runner verifies the panel's NEW load-bearing claims:
  (A) every canonical volume/dimension measure gives the (1,2) weighting
      -> Q=1 (equipartition theorem, Plancherel dim^2/|G|, Gaussian det),
  (B) the convention-illegitimacy criterion: F1<->F3 MOVES the
      dimensionless observable Q (2/3 vs 1), so it CANNOT be a unit/
      measure convention of the radian/meter class (which by definition
      leave dimensionless ratios invariant),
  (C) the single named wall: a U(1)_b angular quotient on the doublet
      (Re b, Im b) plane -- collapsing 2 real dofs to 1 radial dof BEFORE
      the measure -- is exactly what turns (1,2)->(1,1), i.e. F3->F1,
  (D) the d=3 transversal rigidity (bankable three-generation predictor).
"""

import math


def Q_of_weighting(p_plus, p_perp):
    """Q from isotype power split: |s_par|^2 = p_plus, |s_perp|^2 = p_perp."""
    cos2 = p_plus / (p_plus + p_perp)
    return 1.0 / (3 * cos2)


def sep(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def main():
    sep("(A) EVERY CANONICAL VOLUME/DIMENSION MEASURE -> (1,2) -> Q=1 = F3")
    print("  trivial isotype E_+ = 3 a^2 (1 real dim); doublet E_perp = 6|b|^2")
    print("  (2 real dim). The doublet is counted by its REAL DIMENSION = 2:")
    print()
    # equipartition theorem: kT/2 per quadratic real dof
    kT = 1.0
    e_singlet = 1 * (kT / 2)        # 1 real dof
    e_doublet = 2 * (kT / 2)        # 2 real dofs
    print(f"  equipartition:  singlet energy = {e_singlet} (1 dof),"
          f"  doublet = {e_doublet} (2 dofs)  ratio 1:2")
    # Plancherel: dim^2/|G| over the 3 complex chars {1, w, wbar}
    planch = [1**2 / 3, 1**2 / 3, 1**2 / 3]   # each complex char
    print(f"  Plancherel dim^2/|G|: trivial={planch[0]:.3f},"
          f"  doublet(w+wbar)={planch[1]+planch[2]:.3f}  ratio 1:2")
    # Gaussian path-integral det on R^3 = R(+)R^2: doublet is 2D
    print(f"  Gaussian det / Haar on R^3: doublet block is 2-dimensional -> 1:2")
    print(f"  => all give (p_+,p_perp)=(1/3,2/3): Q = {Q_of_weighting(1/3,2/3):.5f} = F3")
    print(f"     equal-block (1/2,1/2): Q = {Q_of_weighting(0.5,0.5):.5f} = F1 (physical)")
    print(f"     all-trivial (1,0):     Q = {Q_of_weighting(1.0,0.0):.5f} (Q_min)")

    sep("(B) CONVENTION-ILLEGITIMACY: F1<->F3 MOVES the dimensionless Q")
    qF1, qF3 = Q_of_weighting(0.5, 0.5), Q_of_weighting(1/3, 2/3)
    print(f"  Q(F1) = {qF1:.5f},  Q(F3) = {qF3:.5f}")
    print(f"  |Delta Q| / Q = {abs(qF1-qF3)/qF1*100:.1f}%  (50% shift)")
    print("  A legitimate unit/measure convention (meter/GeV/radian class)")
    print("  must leave every DIMENSIONLESS predicted-vs-measured ratio")
    print("  INVARIANT -- that is the admissibility criterion that licensed")
    print("  the radian/meter reclassifications. Q is dimensionless and")
    print("  directly measured (=0.6667). A choice moving it by 50% against")
    print("  PDG data CANNOT be a unit convention.")
    print("  => CORRECTION: F1-vs-F3 is NOT audit-decidable as a convention;")
    print("     it is a genuine, still-open physics measure-SELECTION gap.")
    print(f"     (PDG Q=0.6667 sits at F1, decisively excluding F3=Q=1.)")

    sep("(C) THE SINGLE NAMED WALL: U(1)_b angular quotient on the doublet")
    print("  Doublet coordinate b = |b| e^{i theta} in the (Re b, Im b) plane.")
    print("  Retained K/CPT supplies the DISCRETE Z_2 (w <-> wbar); it does")
    print("  NOT supply the CONTINUOUS U(1)_b phase quotient.")
    print("  If theta is gauged/quotiented out BEFORE the measure, the")
    print("  doublet collapses 2 real dofs -> 1 radial dof |b|:")
    for quotient in [False, True]:
        doublet_dofs = 1 if quotient else 2
        # power split with doublet counted as `doublet_dofs` real dims
        p_perp = doublet_dofs / 3.0       # normalized dimension share
        p_plus = 1.0 / 3.0
        Q = Q_of_weighting(p_plus, p_perp)
        tag = "F1 (Q=2/3)" if quotient else "F3 (Q=1)"
        print(f"    U(1)_b quotient={quotient!s:5}: doublet counts as"
              f" {doublet_dofs} real dof -> weighting (1,{doublet_dofs})"
              f" -> Q={Q:.4f} = {tag}")
    print("  => F3->F1 IFF the continuous doublet phase is quotiented out.")
    print("     This single missing ingredient is the entire residual gap.")

    sep("(D) BANKABLE: d=3 transversal rigidity (three-generation predictor)")
    print("  Delta(d) = Q_mid - Q_equi = (1+d)/(2d) - 2/d = (d-3)/(2d).")
    for d in [2, 3, 4]:
        delta = (d - 3) / (2 * d)
        qe, qm = 2.0 / d, (1.0 + d) / (2.0 * d)
        print(f"    d={d}: Q_equi={qe:.4f} Q_mid={qm:.4f} Delta={delta:+.4f}"
              f"  {'<= unique zero' if d == 3 else ''}")
    print("  Simple transversal zero only at d=3 (slope 1/6) -> exactly 3")
    print("  Koide-coherent generations; a Q=2/3 4th charged lepton is")
    print("  falsified (d=4 needs Q_equi=1/2 but Q_mid=5/8). This is a")
    print("  CONSISTENCY FILTER over d, NOT the selection law over the")
    print("  ratio r at fixed d -- file as rigidity/predictor, not closure.")

    sep("VERDICT")
    print("  No escape. F1 is NOT derived. F1-vs-F3 is NOT a legitimate unit")
    print("  convention (it moves dimensionless Q). The crux collapses to ONE")
    print("  unforced step: a U(1)_b angular quotient on the C_3 doublet that")
    print("  would let counting-on-blocks (F1) override the dimension/")
    print("  Plancherel measure (F3) that every retained structure selects.")
    print("  Most promising route: Jaynes MaxEnt derives the 2-valued FS")
    print("  block label as the macrostate variable (defeats Q=1/3), but")
    print("  cannot adjudicate cell-counting (F1) vs Haar-volume (F3).")


if __name__ == "__main__":
    main()
