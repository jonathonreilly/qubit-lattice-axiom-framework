import Init

/-!
Row 1428 (c): acceptance fixtures for the 2D Haar gluing component, each corruption
implemented as a corrupted OPERATION and named exactly (check 1420, defect 3).

`MomentPoly`, `sew`, `equivalent`, `plaquette`, `known` are the fixture of row 1418
(`library/gap-rg-step-sizing-astra62.md`, gpt-6.2-astra), kernel-checked in row 1427
(`lean/glue/GlueNamed.lean`).  `(a + b x + c x^2) / d` with `x` the quaternion scalar part;
character coefficients: vacuum `(a + c/4)/d`, fundamental `b/(2d)`, adjoint `c/(4d)`.
Only `import Init`; no mathlib, no `native_decide`.
-/

namespace Step1Glue

structure MomentPoly where
  a : Nat
  b : Nat
  c : Nat
  d : Nat

/-- Correct gluing: `E[(a + b x + c x^2)(a' + b' y + c' y^2)]` over a Haar unit quaternion,
with `E x^2 = E y^2 = 1/4`, `E xy = u/4`, `E x^2 y^2 = (1 + 2u^2)/24`, cleared by 24. -/
def sew (p q : MomentPoly) : MomentPoly :=
  ⟨24*p.a*q.a + 6*(p.a*q.c + p.c*q.a) + p.c*q.c,
   6*p.b*q.b, 2*p.c*q.c, 24*p.d*q.d⟩

def equivalent (p q : MomentPoly) : Bool :=
  (p.d != 0) && (q.d != 0) && (p.a*q.d == q.a*p.d) &&
  (p.b*q.d == q.b*p.d) && (p.c*q.d == q.c*p.d)

/-- The same comparison without the guard on the denominators (a wrong checker). -/
def crossOnly (p q : MomentPoly) : Bool :=
  (p.a*q.d == q.a*p.d) && (p.b*q.d == q.b*p.d) && (p.c*q.d == q.c*p.d)

def plaquette : MomentPoly := ⟨15, 8, 4, 16⟩
def pairOfPlaquettes := sew plaquette plaquette
def square := sew pairOfPlaquettes pairOfPlaquettes
def known : MomentPoly := ⟨1769471, 1728, 4, 1769472⟩

theorem square_ok : equivalent square known = true := by decide

/-! ## C1: a missing `1/d` in the fundamental channel (`d = 2`)

Schur: `chi_j * chi_j = chi_j / d_j`.  In the fundamental channel the correct coefficient of
`sew` is `6 = 24 * (1/4)`; without the `1/d` it is `12`. -/

def sewMissingInvD (p q : MomentPoly) : MomentPoly :=
  ⟨24*p.a*q.a + 6*(p.a*q.c + p.c*q.a) + p.c*q.c,
   12*p.b*q.b, 2*p.c*q.c, 24*p.d*q.d⟩

/-- Exactly one of the three gluings lacks the `1/d` (the last one): the fundamental
coefficient is `1/1024` instead of `1/2048`, i.e. `b = 3456`; rejected. -/
theorem C1_one_missing_last_is_3456 :
    equivalent (sewMissingInvD pairOfPlaquettes pairOfPlaquettes) { known with b := 3456 } = true := by
  decide
theorem C1_one_missing_last_rejected :
    equivalent (sewMissingInvD pairOfPlaquettes pairOfPlaquettes) known = false := by decide
/-- Exactly one missing, in the first gluing instead: same wrong value, rejected. -/
theorem C1_one_missing_first_is_3456 :
    equivalent (sew (sewMissingInvD plaquette plaquette) pairOfPlaquettes) { known with b := 3456 } = true := by
  decide
theorem C1_one_missing_first_rejected :
    equivalent (sew (sewMissingInvD plaquette plaquette) pairOfPlaquettes) known = false := by decide
/-- Two missing: `1/512`, `b = 6912` (the corrupted target of the row 1418 Lean fixture). -/
theorem C1_two_missing_is_6912 :
    equivalent (sewMissingInvD (sewMissingInvD plaquette plaquette) pairOfPlaquettes)
      { known with b := 6912 } = true := by decide
/-- All three missing: `1/256`, `b = 13824` (the wrong output of the row 1418 Python fixture). -/
theorem C1_three_missing_is_13824 :
    equivalent (sewMissingInvD (sewMissingInvD plaquette plaquette) (sewMissingInvD plaquette plaquette))
      { known with b := 13824 } = true := by decide
theorem C1_targets_rejected :
    [3456, 6912, 13824].map (fun b => equivalent square { known with b := b }) = [false, false, false] := by
  decide

/-! ## C2: the spin-one channel dropped in one gluing

The vacuum coefficient of the product is kept, `(a + c/4)(a' + c'/4)`, the adjoint output is
set to zero.  Cleared by 48. -/

def sewDropAdjoint (p q : MomentPoly) : MomentPoly :=
  ⟨48*p.a*q.a + 12*(p.a*q.c + p.c*q.a) + 3*p.c*q.c,
   12*p.b*q.b, 0, 48*p.d*q.d⟩

/-- The target with the adjoint coefficient removed: `(1, 1/2048, 0)`. -/
def knownNoAdjoint : MomentPoly := ⟨1769472, 1728, 0, 1769472⟩

theorem C2_drop_in_last_is_no_adjoint :
    equivalent (sewDropAdjoint pairOfPlaquettes pairOfPlaquettes) knownNoAdjoint = true := by decide
theorem C2_drop_in_last_rejected :
    equivalent (sewDropAdjoint pairOfPlaquettes pairOfPlaquettes) known = false := by decide
theorem C2_drop_in_first_is_no_adjoint :
    equivalent (sew (sewDropAdjoint plaquette plaquette) pairOfPlaquettes) knownNoAdjoint = true := by
  decide
theorem C2_drop_in_first_rejected :
    equivalent (sew (sewDropAdjoint plaquette plaquette) pairOfPlaquettes) known = false := by decide

/-! ## C3: zero denominator -/

/-- A zero denominator in the target (row 1418's fourth example). -/
theorem C3_zero_target_denominator_rejected :
    equivalent square { known with d := 0 } = false := by decide
/-- `0/0` on both sides: cross-multiplication alone accepts it, the guarded test rejects it. -/
theorem C3_zero_over_zero_passes_unguarded :
    crossOnly ⟨0, 0, 0, 0⟩ known = true := by decide
theorem C3_zero_over_zero_rejected :
    equivalent ⟨0, 0, 0, 0⟩ known = false := by decide
/-- A plaquette with zero denominator makes the glued denominator zero: rejected. -/
theorem C3_zero_input_denominator_rejected :
    equivalent (sew (sew { plaquette with d := 0 } plaquette) pairOfPlaquettes) known = false := by
  decide

/-! ## The sphere-moment arithmetic behind `sew` (not the Haar integral itself)

With `m2 = E x_i^2`, `m4 = E x_i^4`, `m22 = E x_i^2 x_j^2` (`i ≠ j`) on the unit sphere of
R^4, in units of `1/24`: `m2 = 6`, `m4 = 3`, `m22 = 1`.  The three relations that force them
(lane report, Lemma SM): `4 m2 = 1`, `4 m4 + 12 m22 = 1`, and invariance of `E x_1^4` under
the rational rotation `x_1 -> (3 x_1 + 4 x_2)/5`: `625 m4 = (81 + 256) m4 + 6 * 144 m22`. -/

theorem SM_relations :
    (4 * 6 = 24) ∧ (4 * 3 + 12 * 1 = 24) ∧ (625 * 3 = (81 + 256) * 3 + 6 * 144 * 1) := by decide
/-- `E x^2 y^2 = u^2 m4 + (1 - u^2) m22 = (1 + 2 u^2)/24`: constant `m22`, slope `m4 - m22`. -/
theorem SM_x2y2 : (1 = 1) ∧ (3 - 1 = 2) := by decide
/-- The coefficients of `sew`: `24 E x^2 = 6`, `24 E x^2 y^2 = 1 + 2 u^2`, `24 E xy = 6 u`. -/
theorem SM_sew_coefficients : (24 / 4 = 6) ∧ (24 * 1 / 24 = 1) ∧ (24 * 2 / 24 = 2) := by decide

end Step1Glue

#print axioms Step1Glue.square_ok
#print axioms Step1Glue.C1_one_missing_last_is_3456
#print axioms Step1Glue.C1_one_missing_last_rejected
#print axioms Step1Glue.C1_one_missing_first_is_3456
#print axioms Step1Glue.C1_one_missing_first_rejected
#print axioms Step1Glue.C1_two_missing_is_6912
#print axioms Step1Glue.C1_three_missing_is_13824
#print axioms Step1Glue.C1_targets_rejected
#print axioms Step1Glue.C2_drop_in_last_is_no_adjoint
#print axioms Step1Glue.C2_drop_in_last_rejected
#print axioms Step1Glue.C2_drop_in_first_is_no_adjoint
#print axioms Step1Glue.C2_drop_in_first_rejected
#print axioms Step1Glue.C3_zero_target_denominator_rejected
#print axioms Step1Glue.C3_zero_over_zero_passes_unguarded
#print axioms Step1Glue.C3_zero_over_zero_rejected
#print axioms Step1Glue.C3_zero_input_denominator_rejected
#print axioms Step1Glue.SM_relations
#print axioms Step1Glue.SM_x2y2
#print axioms Step1Glue.SM_sew_coefficients
