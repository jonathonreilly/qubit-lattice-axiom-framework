import Mathlib.Analysis.InnerProductSpace.l2Space
import Mathlib.Analysis.InnerProductSpace.Positive
import Mathlib.Tactic

/-!
# The forward implication of Lemma M1 (W1)

Row 1356, §2.1, Claude Fable 5.2. This is the free-scale, rank-one
case of the estimate of Eckart and Young. We sum the column-norm
identity in an arbitrary Hilbert basis and use the given unit vector throughout.
-/

open Filter InnerProductSpace
open scoped BigOperators InnerProductSpace ComplexConjugate

namespace GapChain

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

/-- The finite-orthonormal-family test used in the gap-chain statement file. -/
def HSNormLE (A : H →L[ℂ] H) (δ : ℝ) : Prop :=
  ∀ (n : ℕ) (v : Fin n → H), Orthonormal ℂ v → ∑ i, ‖A (v i)‖ ^ 2 ≤ δ ^ 2

/-- The operator x ↦ ⟪φ, x⟫ • φ. -/
noncomputable def ketBra (φ : H) : H →L[ℂ] H := rankOne ℂ φ φ

/-- Restrict the finite-family test to any finite subset of a Hilbert basis. -/
theorem HSNormLE.sum_le {ι : Type*} {A : H →L[ℂ] H} {δ : ℝ}
    (h : HSNormLE A δ) (b : HilbertBasis ι ℂ H) (s : Finset ι) :
    ∑ i ∈ s, ‖A (b i)‖ ^ 2 ≤ δ ^ 2 := by
  classical
  let e : Fin s.card ≃ s := s.equivFin.symm
  let f : Fin s.card → ι := fun i => (e i).val
  have hf : Function.Injective f := Subtype.val_injective.comp e.injective
  have hb := h _ (b ∘ f) (b.orthonormal.comp f hf)
  calc
    ∑ i ∈ s, ‖A (b i)‖ ^ 2 = ∑ i : s, ‖A (b i)‖ ^ 2 := by
      rw [← Finset.sum_attach, Finset.attach_eq_univ]
    _ = ∑ j : Fin s.card, ‖A (b (f j))‖ ^ 2 :=
      (e.sum_comp (fun i : s => ‖A (b i)‖ ^ 2)).symm
    _ ≤ δ ^ 2 := hb

/-- Squared Hilbert–Schmidt mass in an arbitrary Hilbert basis. -/
noncomputable def hsSq {ι : Type*} (b : HilbertBasis ι ℂ H) (B : H →L[ℂ] H) : ℝ :=
  ∑' i, ‖B (b i)‖ ^ 2

/-- The square-completion estimate, valid even without positivity of the operator. -/
theorem lemmaM1_hsSq {ι : Type*} (b : HilbertBasis ι ℂ H) (B : H →L[ℂ] H)
    (hB : Summable (fun i => ‖B (b i)‖ ^ 2)) {φ : H} (hφ : ‖φ‖ = 1)
    {c δ : ℝ} (hc : 0 < c)
    (h : HSNormLE (((c⁻¹ : ℝ) : ℂ) • B - ketBra φ) δ) :
    (1 - δ ^ 2) * hsSq b B ≤ ‖B‖ ^ 2 := by
  classical
  let t := c⁻¹
  let A := ((t : ℝ) : ℂ) • B - ketBra φ
  have ht : 0 ≤ t := (inv_pos.mpr hc).le
  have hproj : HasSum (fun i => ‖inner ℂ φ (b i)‖ ^ 2) 1 := by
    convert Complex.hasSum_re (b.hasSum_inner_mul_inner φ φ) using 1
    · ext i
      rw [← inner_conj_symm (b i) φ, Complex.mul_conj, Complex.ofReal_re,
        Complex.normSq_eq_norm_sq]
    · simp [inner_self_eq_norm_sq_to_K, hφ]
  have hcross : HasSum
      (fun i => (inner ℂ (b i) φ * inner ℂ φ (B (b i))).re)
      (inner ℂ φ (B φ)).re := by
    simpa [b.repr_apply_apply, inner_smul_right] using
      Complex.hasSum_re (((b.hasSum_repr φ).mapL B).mapL (innerSL ℂ φ))
  have hexpand (i : ι) : ‖A (b i)‖ ^ 2 =
      t ^ 2 * ‖B (b i)‖ ^ 2 -
      (2 * t) * (inner ℂ (b i) φ * inner ℂ φ (B (b i))).re +
      ‖inner ℂ φ (b i)‖ ^ 2 := by
    simp only [A, ketBra, sub_apply, smul_apply,
      rankOne_apply]
    rw [norm_sub_rev, norm_sub_sq (𝕜 := ℂ)]
    simp only [norm_smul, hφ, mul_one, Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg ht, inner_smul_left, inner_smul_right, inner_conj_symm]
    simp [Complex.mul_re]
    ring
  have herror : HasSum (fun i => ‖A (b i)‖ ^ 2)
      (t ^ 2 * hsSq b B - (2 * t) * (inner ℂ φ (B φ)).re + 1) := by
    simpa only [hexpand, hsSq] using
      (((hB.hasSum.mul_left (t ^ 2)).sub (hcross.mul_left (2 * t))).add hproj)
  have herr := le_of_tendsto herror (Eventually.of_forall fun s => h.sum_le b s)
  have hinner : (inner ℂ φ (B φ)).re ≤ ‖B‖ := by
    calc
      _ ≤ ‖φ‖ * ‖B φ‖ := re_inner_le_norm (𝕜 := ℂ) _ _
      _ ≤ ‖φ‖ * (‖B‖ * ‖φ‖) := mul_le_mul_of_nonneg_left (B.le_opNorm φ) (norm_nonneg _)
      _ = ‖B‖ := by simp [hφ]
  have hquad : t ^ 2 * hsSq b B - 2 * t * ‖B‖ + 1 ≤ δ ^ 2 := by
    nlinarith [mul_nonneg ht (sub_nonneg.mpr hinner)]
  have hmass : 0 ≤ hsSq b B := tsum_nonneg fun _ => sq_nonneg _
  nlinarith [mul_nonneg (sub_nonneg.mpr hquad) hmass, sq_nonneg (t * hsSq b B - ‖B‖)]

/-- Forward M1 for a positive Hilbert–Schmidt operator. The sum is the real diagonal
trace of B². Its coefficient is positive throughout 0 ≤ δ < 1. -/
theorem lemmaM1 {ι : Type*} (b : HilbertBasis ι ℂ H) (B : H →L[ℂ] H)
    (hpos : B.IsPositive) (hB : Summable (fun i => ‖B (b i)‖ ^ 2))
    {φ : H} (hφ : ‖φ‖ = 1) {c δ : ℝ} (hc : 0 < c)
    (h : HSNormLE (((c⁻¹ : ℝ) : ℂ) • B - ketBra φ) δ) :
    (1 - δ ^ 2) * (∑' i, (inner ℂ (b i) (B (B (b i)))).re) ≤ ‖B‖ ^ 2 := by
  have hdiag (i : ι) : (inner ℂ (b i) (B (B (b i)))).re = ‖B (b i)‖ ^ 2 := by
    exact (congrArg Complex.re (hpos.isSymmetric (b i) (B (b i))).symm).trans
      (inner_self_eq_norm_sq (𝕜 := ℂ) _)
  simpa only [hdiag, hsSq] using lemmaM1_hsSq b B hB hφ hc h

#print axioms HSNormLE.sum_le
#print axioms lemmaM1_hsSq
#print axioms lemmaM1

end GapChain
