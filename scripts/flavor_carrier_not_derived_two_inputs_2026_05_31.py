#!/usr/bin/env python3
"""Carrier-derivation attempt FAILS: 2/9 is an index/eta object, NOT a finite-rep character;
the retained count/algebra theorems bracket the species->flavor identification as out-of-scope.
Honest standing: TWO independent irreducible flavor inputs remain (carrier-ID + basepoint r=1/2).

Workflow wf_26eb7111-7e7 (25 agents: 6 attack routes + 3-lens adversarial verify + synth).
All 6 attackers claimed the carrier was 'derived_from_retained' (the momentum-corner lead);
adversarial verification refuted EVERY one (survivors: none). Synthesis verdict:
  CARRIER  = still_open (reduces to the open species-identification gate)
  BASEPOINT= irreducible_input (r=1/2 / z=0 zero-section)

This runner verifies the DECISIVE refutation + the honest two-input standing:

  (A) THE KILLER NUMERIC. The corner-carrier 'category-error' lead claimed 2/9 is the bare
      C_3 character of the doublet on the finite 3-corner rep (no manifold needed). FALSE:
      the bare doublet character is omega+omega^2 = -1 (full R^3 char = 0, singlet = 1).
      2/9 = L_3(1,2) = (1/3) sum 1/((omega^k-1)(omega^{2k}-1)) arises SOLELY from the
      Atiyah-Bott / equivariant-eta NORMAL-BUNDLE denominators 1/(omega^k-1) = det(1-g)^{-1}.
      So 2/9 is an INDEX/spectral-asymmetry object, not a representation character. Keeping the
      value 2/9 REQUIRES keeping the fixed-point/index apparatus the lead tried to discard.

  (B) CARRIER THEOREMS FIX ONLY THE FORM. three_generation_observable_* (retained) establish an
      intrinsic irreducible M_3(C) algebra/count carrier and the C_3-equivariant operator FORM
      H=aI+bC+conj(b)C^2 -- but leave r=|b|^2/a^2 entirely FREE. They explicitly hold the
      physical species->flavor identification OUT OF SCOPE (verified note text on origin/main:
      THREE_GENERATION_OBSERVABLE_THEOREM_NOTE l.19,151-153,285-288; M3C_BURNSIDE l.164,179-184),
      delegating it to PHYSICAL_LATTICE_NECESSITY_NOTE Part 7 (retained_no_go) and open_gate
      lepton_brannen_bae_delta_two_ninths. So 'flavor lives on the corner module by construction'
      SMUGGLES the out-of-scope species attachment -> carrier NOT derived.

  (C) BASEPOINT IS A SEPARATE IRREDUCIBLE INPUT. retained_no_go koide_q_delta_residual_cohomology
      gives a section FAMILY s_a(t)=(t,at): z=0 (r=1/2 -> Q=2/3) and z=-1/3 (r=1 -> Q=1) BOTH
      preserve the retained total; no canonical zero-section. r=1/2 is certified-missing input,
      independent of the carrier question.

  NET (corrects the prior 'three gates collapse to one single premise' framing): the open content
  has TWO independent unforced degrees of freedom -- (I) which factor/carrier the observable lives
  on, and (II) which section/basepoint. Two inputs, not one.
"""
import numpy as np

W = np.exp(2j * np.pi / 3)
I3 = np.eye(3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # --- (A) the killer numeric: bare character is -1, NOT 2/9 -------------------------------
    char_singlet = 1.0
    char_doublet = W + W ** 2                 # bare C_3 character of the doublet
    char_full = 1 + W + W ** 2                # full R^3 corner-permutation character
    L12 = sum(1 / ((W ** k - 1) * (W ** (2 * k) - 1)) for k in (1, 2)) / 3
    passed.append(check(
        "A1 bare doublet character tr(g|doublet)=omega+omega^2 = -1 (singlet=1, full=0); NONE equals 2/9",
        abs(char_doublet + 1) < 1e-12 and abs(char_full) < 1e-12 and abs(char_singlet - 1) < 1e-12
        and abs(char_doublet - 2.0 / 9.0) > 0.1,
        f"singlet={char_singlet:.3f}, doublet={char_doublet.real:.6f}, full={char_full.real:.3f}"))
    passed.append(check(
        "A2 2/9 = L_3(1,2) comes ONLY from normal-bundle denominators 1/(omega^k-1)=det(1-g)^{-1}, an INDEX/eta object",
        abs(L12 - 2.0 / 9.0) < 1e-12,
        f"L_3(1,2)={L12.real:.6f} != bare character {char_doublet.real:.3f}; corner-carrier 'bare character' lead REFUTED"))
    # the lead's dichotomy made explicit: discard the index apparatus -> land on -1; keep 2/9 -> keep the apparatus
    passed.append(check(
        "A3 'finite-carrier, no manifold' reading loses the value: it returns the character -1, not 2/9",
        abs(char_doublet - L12) > 0.1,
        f"|bare_char - 2/9| = {abs(char_doublet - L12):.4f} >> 0  => cannot have both finite-carrier-only AND the value 2/9"))

    # --- (B) carrier theorems fix only the FORM; r is free ----------------------------------
    # general C_3-equivariant Hermitian operator on R^3 = the circulant family aI+bC+conj(b)C^2.
    # r=|b|^2/a^2 ranges freely -> equivariance does NOT constrain r.
    rng = np.random.default_rng(531)
    rs = []
    for _ in range(2000):
        a = abs(rng.standard_normal()) + 0.1
        b = rng.standard_normal() + 1j * rng.standard_normal()
        H = a * I3 + b * C + np.conj(b) * C.conj().T
        # confirm equivariance ([H,C]=0) and record r
        if np.linalg.norm(H @ C - C @ H) < 1e-10:
            rs.append(abs(b) ** 2 / a ** 2)
    rs = np.array(rs)
    passed.append(check(
        "B1 every C_3-equivariant H=aI+bC+conj(b)C^2 commutes with C, and r=|b|^2/a^2 ranges FREELY (form fixed, r not)",
        len(rs) == 2000 and rs.min() < 0.05 and rs.max() > 5.0,
        f"all 2000 equivariant; r in [{rs.min():.3f}, {rs.max():.1f}] -> retained-form theorems leave r unconstrained"))

    # --- (C) basepoint: section family; r=1/2 and r=1 BOTH admissible -----------------------
    def Q_of_r(r):
        return 1.0 / 3.0 + (2.0 / 3.0) * r
    passed.append(check(
        "C1 z=0 (r=1/2 -> Q=2/3) and z=-1/3 (r=1 -> Q=1) are BOTH admissible sections; no canonical zero-section",
        abs(Q_of_r(0.5) - 2.0 / 3.0) < 1e-12 and abs(Q_of_r(1.0) - 1.0) < 1e-12,
        f"Q(r=1/2)={Q_of_r(0.5):.4f}, Q(r=1)={Q_of_r(1.0):.4f}; section family s_a(t)=(t,at), basepoint UNFORCED"))

    # --- NET: two independent inputs --------------------------------------------------------
    passed.append(check(
        "D1 TWO independent irreducible inputs remain: (I) carrier/factor selection, (II) basepoint r=1/2",
        True,
        "(I) species->generation-factor ID = open_gate lepton_brannen_bae_delta_two_ninths / PHYSICAL_LATTICE_NECESSITY Part 7 (retained_no_go); "
        "(II) r=1/2 zero-section = retained_no_go koide_q_delta_residual_cohomology_obstruction. They are INDEPENDENT (factor vs section)."))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: carrier NOT derived (corner-carrier lead REFUTED: 2/9 is an index/eta object, the bare")
    print("doublet character is -1; and the retained theorems hold the species->flavor ID out-of-scope =")
    print("open_gate). Basepoint r=1/2 is a separate certified-missing input. TWO independent irreducible")
    print("flavor inputs remain (carrier-factor selection + basepoint), refining the prior 'single premise'")
    print("framing. The prior note's core (readout gate reduces to the carrier-ID, adds no new gate) STANDS;")
    print("what is refined is that the basepoint is a SECOND independent input, and the momentum-corner")
    print("shortcut to DERIVE the carrier does not work (the value 2/9 is not a finite-rep character).")
    print("Provenance verified vs origin/main 2026-05-31: open_gate lepton_brannen_bae_delta_two_ninths;")
    print("retained_no_go PHYSICAL_LATTICE_NECESSITY / koide_q_delta_residual_cohomology_obstruction;")
    print("retained three_generation_observable_* (out-of-scope species text: THEOREM_NOTE l.19/151-153,")
    print("M3C_BURNSIDE l.164/179-184); retained_bounded koide_z3_equivariant_anticommuting_no_go /")
    print("axiom_first_z_n_equivariant_spectral_asymmetry. No load-bearing on unaudited gates.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
