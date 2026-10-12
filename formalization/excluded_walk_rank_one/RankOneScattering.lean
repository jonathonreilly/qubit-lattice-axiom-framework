import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Module
import Mathlib.Tactic.NormNum

/-!
Universal rank-one algebra on arbitrary complex Hilbert spaces. The inner
product is conjugate-linear in its first argument. `scattering v s` is
`1 + (s - 1) |v><v|`; the observable difference uses its adjoint on the left.
No threshold regularity, wave-operator, coarea, flux or physical-law theorem
is asserted by this file. All normalization and disjointness assumptions
are explicit. No finite-dimensional hypothesis is used.
-/

noncomputable section
set_option autoImplicit false
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap

namespace RankOneScattering

universe u
variable {E : Type u} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
local notation "⟪" x ", " y "⟫" => inner ℂ x y

def scattering (v : E) (s : ℂ) : E →L[ℂ] E :=
  1 + (s - 1) • rankOne ℂ v v

def centered (g : E →L[ℂ] E) (v : E) : E :=
  g v - ⟪v, g v⟫ • v

omit [CompleteSpace E] in
theorem inner_unit {v : E} (hv : ‖v‖ = 1) : ⟪v, v⟫ = 1 := by
  simp [inner_self_eq_norm_sq_to_K, hv]

theorem phase_conj_mul {s : ℂ} (hs : ‖s‖ = 1) : conj s * s = 1 := by
  simpa [hs] using Complex.conj_mul' s

theorem scattering_adjoint (v : E) (s : ℂ) :
    (scattering v s)† = scattering v (conj s) := by
  simp [scattering, map_add, map_smulₛₗ, adjoint_one]

omit [CompleteSpace E] in
theorem scattering_comp {v : E} (hv : ‖v‖ = 1) (s t : ℂ) :
    scattering v s ∘L scattering v t = scattering v (s * t) := by
  ext x
  simp [scattering, hv]
  module

omit [CompleteSpace E] in
theorem scattering_one (v : E) : scattering v 1 = 1 := by
  simp [scattering]

theorem scattering_unitary {v : E} {s : ℂ} (hv : ‖v‖ = 1) (hs : ‖s‖ = 1) :
    scattering v s ∈ unitary (E →L[ℂ] E) := by
  change (scattering v s)† ∘L scattering v s = 1 ∧
    scattering v s ∘L (scattering v s)† = 1
  rw [scattering_adjoint, scattering_comp hv, scattering_comp hv,
    phase_conj_mul hs, mul_comm s (conj s), phase_conj_mul hs, scattering_one]
  exact ⟨rfl, rfl⟩

theorem observable_expansion (g : E →L[ℂ] E) (hg : g† = g) (v : E) (s : ℂ) :
    (scattering v s)† ∘L g ∘L scattering v s - g =
      (s - 1) • rankOne ℂ (centered g v) v +
      (conj s - 1) • rankOne ℂ v (centered g v) +
      ((conj s * s - 1) * ⟪v, g v⟫) • rankOne ℂ v v := by
  have hpair (x : E) : ⟪v, g x⟫ = ⟪g v, x⟫ := by
    simpa only [hg] using (adjoint_inner_left g x v).symm
  rw [scattering_adjoint]
  ext x
  simp [scattering, centered, hpair]
  module

theorem observable_difference (g : E →L[ℂ] E) (hg : g† = g)
    (v : E) {s : ℂ} (hs : ‖s‖ = 1) :
    (scattering v s)† ∘L g ∘L scattering v s - g =
      (s - 1) • rankOne ℂ (centered g v) v +
      (conj s - 1) • rankOne ℂ v (centered g v) := by
  rw [observable_expansion g hg, phase_conj_mul hs]
  simp

omit [CompleteSpace E] in
theorem centered_orthogonal (g : E →L[ℂ] E) {v : E} (hv : ‖v‖ = 1) :
    ⟪v, centered g v⟫ = 0 := by
  simp [centered, inner_sub_right, inner_smul_right, hv]

omit [CompleteSpace E] in
theorem scattering_contact {v : E} (hv : ‖v‖ = 1) (s : ℂ) :
    scattering v s v = s • v := by
  simp [scattering, hv]
  module

omit [CompleteSpace E] in
theorem pure_contact_zero (g : E →L[ℂ] E) {v : E} {s : ℂ}
    (hv : ‖v‖ = 1) (hs : ‖s‖ = 1) :
    ⟪scattering v s v, g (scattering v s v)⟫ - ⟪v, g v⟫ = 0 := by
  rw [scattering_contact hv]
  simp [inner_smul_left, inner_smul_right, ← mul_assoc, Complex.mul_conj', hs]

omit [CompleteSpace E] in
theorem outgoing_amplitude (Q : E →L[ℂ] E) (v phi : E) (s : ℂ)
    (hdisjoint : Q phi = 0) :
    Q (scattering v s phi) = ((s - 1) * ⟪v, phi⟫) • Q v := by
  simp [scattering, hdisjoint, smul_smul]

omit [CompleteSpace E] in
theorem disjoint_transfer (Q : E →L[ℂ] E) (v phi : E) (s : ℂ)
    (hdisjoint : Q phi = 0) :
    ‖Q (scattering v s phi)‖ ^ 2 =
      ‖s - 1‖ ^ 2 * ‖⟪v, phi⟫‖ ^ 2 * ‖Q v‖ ^ 2 := by
  rw [outgoing_amplitude Q v phi s hdisjoint]
  simp [norm_smul, mul_pow, mul_assoc]

def capVector (A : E →L[ℂ] E) (v : E) : E := (‖A v‖ : ℂ)⁻¹ • A v

omit [CompleteSpace E] in
theorem cap_normalized (A : E →L[ℂ] E) (v : E) (hne : A v ≠ 0) :
    ‖capVector A v‖ = 1 := by
  simp [capVector, norm_smul, norm_ne_zero_iff.mpr hne]

theorem cap_overlap (A : E →L[ℂ] E) (hA : A† = A) (hAA : A ∘L A = A)
    (v : E) (hne : A v ≠ 0) : ⟪v, capVector A v⟫ = (‖A v‖ : ℂ) := by
  have haa : A (A v) = A v := congrArg (fun f : E →L[ℂ] E => f v) hAA
  have hip : ⟪v, A v⟫ = (‖A v‖ : ℂ) ^ 2 := by
    calc
      ⟪v, A v⟫ = ⟪v, A (A v)⟫ := by rw [haa]
      _ = ⟪A v, A v⟫ := by simpa only [hA] using adjoint_inner_right A v (A v)
      _ = (‖A v‖ : ℂ) ^ 2 := inner_self_eq_norm_sq_to_K (A v)
  have hn : (‖A v‖ : ℂ) ≠ 0 := by exact_mod_cast norm_ne_zero_iff.mpr hne
  simp only [capVector, inner_smul_right, hip, pow_two]
  rw [← mul_assoc, inv_mul_cancel₀ hn, one_mul]

theorem cap_transfer (A Q : E →L[ℂ] E) (hA : A† = A) (hAA : A ∘L A = A)
    (v : E) (hne : A v ≠ 0) (s : ℂ) (hdisjoint : Q (A v) = 0) :
    ‖Q (scattering v s (capVector A v))‖ ^ 2 =
      ‖s - 1‖ ^ 2 * ‖A v‖ ^ 2 * ‖Q v‖ ^ 2 := by
  have hQ : Q (capVector A v) = 0 := by simp [capVector, hdisjoint]
  rw [disjoint_transfer Q v (capVector A v) s hQ, cap_overlap A hA hAA v hne]
  simp

def coherent (v u : E) (r : ℝ) : E := (r : ℂ) • (v + Complex.I • u)

omit [CompleteSpace E] in
theorem coherent_normalized {v u : E} (hv : ‖v‖ = 1) (hu : ‖u‖ = 1)
    (hvu : ⟪v, u⟫ = 0) {r : ℝ} (hr : 2 * r ^ 2 = 1) :
    ‖coherent v u r‖ = 1 := by
  have huv : ⟪u, v⟫ = 0 := by
    simpa only [hvu, map_zero] using (inner_conj_symm (𝕜 := ℂ) u v).symm
  have hrC : (2 : ℂ) * (r : ℂ) ^ 2 = 1 := by exact_mod_cast hr
  have hi : ⟪coherent v u r, coherent v u r⟫ = (2 : ℂ) * (r : ℂ) ^ 2 := by
    simp only [coherent, inner_add_left, inner_add_right, inner_smul_left,
      inner_smul_right, inner_unit hv, inner_unit hu, hvu, huv]
    norm_num
    ring_nf
    simp [Complex.I_sq]
    ring
  rw [norm_eq_sqrt_re_inner (𝕜 := ℂ), hi, hrC]
  norm_num

theorem coherent_current (g : E →L[ℂ] E) (hg : g† = g) {v u : E}
    (hv : ‖v‖ = 1) (hu : ‖u‖ = 1) (hvu : ⟪v, u⟫ = 0)
    {s : ℂ} (hs : ‖s‖ = 1) (sigma : ℝ)
    (hw : centered g v = (sigma : ℂ) • u) {r : ℝ} (hr : 2 * r ^ 2 = 1) :
    ⟪coherent v u r,
      ((scattering v s)† ∘L g ∘L scattering v s - g) (coherent v u r)⟫ =
      (sigma * s.im : ℝ) := by
  have huv : ⟪u, v⟫ = 0 := by
    simpa only [hvu, map_zero] using (inner_conj_symm (𝕜 := ℂ) u v).symm
  rw [observable_difference g hg v hs, hw]
  have hi :
      ⟪coherent v u r,
        ((s - 1) • rankOne ℂ ((sigma : ℂ) • u) v +
          (conj s - 1) • rankOne ℂ v ((sigma : ℂ) • u)) (coherent v u r)⟫ =
        (2 * r ^ 2 * sigma * s.im : ℝ) := by
    simp only [coherent, _root_.add_apply, _root_.smul_apply,
      rankOne_apply, inner_add_left, inner_add_right, inner_smul_left,
      inner_smul_right, inner_unit hv, inner_unit hu, hvu, huv]
    apply Complex.ext <;> simp [pow_two] <;> ring
  rw [hi, hr]
  simp

end RankOneScattering

#print axioms RankOneScattering.scattering_unitary
#print axioms RankOneScattering.observable_difference
#print axioms RankOneScattering.centered_orthogonal
#print axioms RankOneScattering.pure_contact_zero
#print axioms RankOneScattering.disjoint_transfer
#print axioms RankOneScattering.coherent_normalized
#print axioms RankOneScattering.coherent_current
#print axioms RankOneScattering.cap_normalized
#print axioms RankOneScattering.cap_overlap
#print axioms RankOneScattering.cap_transfer

#check @RankOneScattering.scattering_unitary
#check @RankOneScattering.observable_difference
#check @RankOneScattering.coherent_normalized
#check @RankOneScattering.coherent_current
#check @RankOneScattering.pure_contact_zero
#check @RankOneScattering.cap_normalized
#check @RankOneScattering.cap_overlap
#check @RankOneScattering.cap_transfer
