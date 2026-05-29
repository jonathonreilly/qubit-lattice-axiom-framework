#!/usr/bin/env python3
"""
Radial-wall probe: does the modular/Tomita weight of the trace state on the
HERMITIAN circulant algebra force the {omega, omega-bar} doublet to count as
ONE complex unit (-> F1, r=|b|^2/a^2=1/2, Q=2/3), via the reality constraint
b-bar = conj(b)?  This is the one untested place "pair=1" might be FORCED by
reality rather than imported (per the 6-mechanism wall-attack synthesis).

Tests:
  (1) the circulant algebra is COMMUTATIVE  => for the trace state, the
      Tomita modular operator Delta = 1, modular flow sigma_t = id. So
      Tomita-Takesaki is STATE-INDEPENDENT and BLIND to any F1/F3 weight.
  (2) the natural (Jordan) trace form Tr(H^2) = 3a^2 + 6|b|^2 supplies the
      block ENERGIES {E_+=3a^2, E_perp=6|b|^2} = diag(3,6,6); it is
      J-invariant but NEUTRAL on the F1-vs-F3 comparison rule: equating the
      two block TOTALS gives F1 (r=1/2), inserting a per-real-dimension /2
      gives F3 (r=1). [Corrected from an earlier mislabel of it as "F3-side";
      caught by the verification workflow's adversarial angle.]
  (3) candidate reality/complex-structure-respecting weights and the r each
      selects: Bargmann/Fock (r=1=F3), per-real-dof flat (r=2), block-count
      MaxEnt (r=1/2=F1).  "Count complex blocks" (F1) vs "count real dims"
      (F3) is the unforced choice; reality supplies J, not the count.
"""

import numpy as np
np.set_printoptions(precision=6, suppress=True)


def C_shift():
    return np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)


def circulant(a, b):
    C = C_shift()
    return a * np.eye(3) + b * C + np.conj(b) * (C @ C)


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("(1) circulant algebra is COMMUTATIVE -> Tomita modular flow trivial")
    # sample several Hermitian circulants; check mutual commutativity
    rng = np.random.default_rng(1)
    mats = [circulant(rng.normal(), rng.normal() + 1j * rng.normal())
            for _ in range(5)]
    maxcomm = 0.0
    for i in range(len(mats)):
        for j in range(len(mats)):
            maxcomm = max(maxcomm, np.max(np.abs(mats[i] @ mats[j] - mats[j] @ mats[i])))
    print(f"  max ||[H_i, H_j]|| over samples = {maxcomm:.2e}  (=> commutative)")
    print("  THEOREM (standard): for a faithful trace tau on an ABELIAN von")
    print("  Neumann algebra, the GNS modular operator Delta = 1 and the")
    print("  modular automorphism group sigma_t = id (KMS is trivial).")
    print("  => Tomita-Takesaki is STATE-INDEPENDENT here; it cannot prefer")
    print("     equal-block (F1) over dimension-weighted (F3). Modular route")
    print("     to 'pair=1' is BLIND. (Sharper than the prior 'modular is")
    print("     blind' finding: here it is provably trivial, not just silent.)")

    sep("(2) Jordan trace form Tr(H^2) = diag(3,6,6): NEUTRAL on F1-vs-F3")
    a, b = 1.3, 0.7 * np.exp(1j * 0.9)
    H = circulant(a, b)
    tr_h2 = np.real(np.trace(H @ H))
    E_plus, E_perp = 3 * a**2, 6 * abs(b)**2
    print(f"  Tr(H^2)            = {tr_h2:.6f}")
    print(f"  E_+ + E_perp       = {E_plus + E_perp:.6f}  (3a^2 + 6|b|^2)")
    print(f"  E_+ = {E_plus:.4f}  E_perp = {E_perp:.4f}   (quad form diag(3,6,6))")
    # J = grade-2 bivector dual to body diagonal, acting on the doublet plane.
    # The trace form is J-invariant: rotating b by any phase leaves Tr(H^2).
    for ph in [0.0, 0.5, 1.3]:
        Hp = circulant(a, np.exp(1j * ph) * b)
        print(f"    Tr(H^2) at arg-shift {ph:.2f} = {np.real(np.trace(Hp@Hp)):.6f}"
              f"  (J-invariant: block energies unchanged)")
    print("  CORRECTION (verification workflow, adversarial angle): the trace")
    print("  form supplies the block ENERGIES {3a^2, 6|b|^2} but NOT the rule")
    print("  for comparing unequal-dimension blocks. Equate TOTALS 3a^2=6|b|^2")
    print("  -> r=1/2 = F1.  Insert per-real-dim /2 (3a^2 = 3|b|^2) -> r=1 = F3.")
    print("  => the trace form is NEUTRAL on F1-vs-F3 (F1-leaning under naive")
    print("     total-equality); it is NOT 'F3-side'. The fork is the unforced")
    print("     'one complex unit vs two real dims' choice, which it cannot make.")

    sep("(3) which reality-respecting weight gives which r = |b|^2/a^2 ?")
    print("  F1 (Q=2/3): r=1/2  <=> E_+ = E_perp  (equal block TOTAL power)")
    print("  F3 (Q=1):   r=1    <=> equal PER-REAL-DIM power")
    print()
    # Bargmann/Fock on complex b: <|b|^2>=1 ; real Gaussian on a: <a^2>=1
    print(f"  Bargmann/Fock (holomorphic, <|b|^2>=1, <a^2>=1): r = {1/1:.3f} = F3")
    # flat per-real-dof: <a^2>=s, <|b|^2>=<Reb^2>+<Imb^2>=2s
    print(f"  flat per-real-dof (<|b|^2>=2<a^2>):              r = {2.0:.3f}  (past F3)")
    # block-count MaxEnt: maximize log E_+ + log E_perp at fixed E_++E_perp -> E_+=E_perp
    print(f"  block-count MaxEnt (count complex block ONCE):   r = {0.5:.3f} = F1")
    print()
    print("  reality (b-bar=conj b) makes the {omega,omega-bar} pair ONE")
    print("  complex number b (one complex DOF). But one complex DOF = TWO")
    print("  real DOF; whether the weight counts it as 1 (complex block, F1)")
    print("  or 2 (real dims, F3) is NOT fixed by reality -- reality supplies")
    print("  the complex structure J, not the counting CONVENTION.")

    sep("VERDICT (confirmed by 4-angle verification workflow, 0/4 forcing)")
    print("  Reality + modular do NOT force pair=1, KINEMATICALLY. Confirmed:")
    print("   - generation circulant abelian => modular flow trivial (Delta=1)")
    print("     for EVERY state, not just the trace; KMS blind to F1/F3.")
    print("   - Z^3 type-III hole CLOSED: a modular weight on the abelian")
    print("     circulant is a diagonal Fourier multiplier; reality forces")
    print("     p_omega = p_omega-bar (two equal modes; collapse needs p=0 =")
    print("     reality violation). And a generic type-III modular flow does")
    print("     NOT preserve the circulant subalgebra, so no induced block")
    print("     weight exists to invoke.")
    print("   - canonical Euclidean-Jordan structure is rank-3 SPLIT (R+R+R):")
    print("     doublet = 2 frame slots, not 1; forcing rank-2 needs a spin-")
    print("     factor product = an unflagged import.")
    print("   - trace form is NEUTRAL (above), not evidence either way.")
    print("  => KINEMATIC/normalization forcing of r=1/2 is a retained_no_go")
    print("     on the phase+reality+modular/KMS+Jordan family. Routes OPEN.")
    print("  HIGHEST-VALUE OPEN ROUTE: a DERIVED DYNAMICAL Z^3 potential whose")
    print("  stationary point sits at 3a^2=6|b|^2 (r=1/2). The no-go is purely")
    print("  KINEMATIC (how to COUNT the irrep); a DYNAMICAL selection lives in")
    print("  the spatial/translation sector the abelian-generation argument")
    print("  explicitly does not constrain. That sector is untouched.")


if __name__ == "__main__":
    main()
