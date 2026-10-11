import Mathlib.LinearAlgebra.AffineSpace.Independent
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.Module
import Mathlib.Tactic.NormNum
import Mathlib.Basic.Real.Basic

/-!
Finite affine geometry from I9-I14 of the frozen interspecies rigidity note.
All statements below are universal over vector spaces over a field. Their
specialization to real three-space is the intended application. No shell,
measure, differential or physical hypothesis is formalized here.
-/

noncomputable section
set_option autoImplicit false
set_option maxHeartbeats 800000
open scoped BigOperators

namespace InterspeciesRigidity

universe u v
variable {K : Type u} [Field K] {V : Type v} [AddCommGroup V] [Module K V]

theorem four_affine_coefficients_zero {x₁ x₂ y₁ y₂ : V}
    (h : AffineIndependent K ![x₁, x₂, y₁, y₂])
    (a b c d : K) (hsum : a + b + c + d = 0)
    (hvec : a • x₁ + b • x₂ + c • y₁ + d • y₂ = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 := by
  have hs : ∑ i ∈ (Finset.univ : Finset (Fin 4)), (![a, b, c, d] : Fin 4 → K) i = 0 := by
    simpa [Fin.sum_univ_succ, add_assoc] using hsum
  have hv : ∑ i ∈ (Finset.univ : Finset (Fin 4)),
      (![a, b, c, d] : Fin 4 → K) i • (![x₁, x₂, y₁, y₂] : Fin 4 → V) i = 0 := by
    simpa [Fin.sum_univ_succ, add_assoc] using hvec
  have hz := h.eq_zero_of_sum_eq_zero hs hv
  exact ⟨by simpa using hz 0 (Finset.mem_univ 0),
    by simpa using hz 1 (Finset.mem_univ 1),
    by simpa using hz 2 (Finset.mem_univ 2),
    by simpa using hz 3 (Finset.mem_univ 3)⟩

theorem four_cycle_multipliers {x₁ x₂ y₁ y₂ P₁ P₂ Q₁ Q₂ : V}
    (h : AffineIndependent K ![x₁, x₂, y₁, y₂])
    (l₁₁ l₂₁ l₂₂ l₁₂ : K)
    (h₁₁ : P₁ - Q₁ = l₁₁ • (x₁ - y₁))
    (h₂₁ : P₂ - Q₁ = l₂₁ • (x₂ - y₁))
    (h₂₂ : P₂ - Q₂ = l₂₂ • (x₂ - y₂))
    (h₁₂ : P₁ - Q₂ = l₁₂ • (x₁ - y₂)) :
    l₁₁ = l₂₁ ∧ l₂₁ = l₂₂ ∧ l₂₂ = l₁₂ := by
  have hc : (P₁ - Q₁) - (P₂ - Q₁) + (P₂ - Q₂) - (P₁ - Q₂) = 0 := by module
  rw [h₁₁, h₂₁, h₂₂, h₁₂] at hc
  have hv : (l₁₁ - l₁₂) • x₁ + (-l₂₁ + l₂₂) • x₂ +
      (-l₁₁ + l₂₁) • y₁ + (-l₂₂ + l₁₂) • y₂ = 0 := by
    calc
      _ = l₁₁ • (x₁ - y₁) - l₂₁ • (x₂ - y₁) +
          l₂₂ • (x₂ - y₂) - l₁₂ • (x₁ - y₂) := by module
      _ = 0 := hc
  obtain ⟨_, hb, hc', hd⟩ := four_affine_coefficients_zero h
    (l₁₁-l₁₂) (-l₂₁+l₂₂) (-l₁₁+l₂₁) (-l₂₂+l₁₂) (by ring) hv
  exact ⟨(eq_of_sub_eq_zero (by simpa [sub_eq_add_neg, add_comm] using hc')).symm,
    (eq_of_sub_eq_zero (by simpa [sub_eq_add_neg, add_comm] using hb)).symm,
    (eq_of_sub_eq_zero (by simpa [sub_eq_add_neg, add_comm] using hd)).symm⟩

theorem opposite_skew_line_residuals {x₁ x₂ y₁ y₂ x y r s : V}
    (h : AffineIndependent K ![x₁, x₂, y₁, y₂])
    (tx ty α β γ : K)
    (hx : x = y₁ + tx • (y₂ - y₁))
    (hy : y = x₁ + ty • (x₂ - x₁))
    (hr : r = α • (y₂ - y₁))
    (hs : s = β • (x₂ - x₁))
    (hedge : r - s = γ • (x - y)) :
    α = 0 ∧ β = 0 ∧ γ = 0 ∧ r = 0 ∧ s = 0 := by
  have hz : r - s - γ • (x - y) = 0 := sub_eq_zero.mpr hedge
  rw [hx, hy, hr, hs] at hz
  have hv : (β + γ * (1-ty)) • x₁ + (-β + γ*ty) • x₂ +
      (-α - γ*(1-tx)) • y₁ + (α-γ*tx) • y₂ = 0 := by
    calc
      _ = α • (y₂-y₁) - β • (x₂-x₁) -
          γ • ((y₁+tx • (y₂-y₁)) - (x₁+ty • (x₂-x₁))) := by module
      _ = 0 := hz
  obtain ⟨h1, h2, h3, h4⟩ := four_affine_coefficients_zero h
    (β+γ*(1-ty)) (-β+γ*ty) (-α-γ*(1-tx)) (α-γ*tx) (by ring) hv
  have hγ : γ = 0 := by
    calc
      γ = (β+γ*(1-ty)) + (-β+γ*ty) := by ring
      _ = 0 := by rw [h1, h2]; simp
  have hα : α = 0 := by simpa [hγ] using h4
  have hβ : β = 0 := by simpa [hγ] using h1
  exact ⟨hα, hβ, hγ, by simp [hr, hα], by simp [hs, hβ]⟩

end InterspeciesRigidity

#print axioms InterspeciesRigidity.four_affine_coefficients_zero
#print axioms InterspeciesRigidity.four_cycle_multipliers
#print axioms InterspeciesRigidity.opposite_skew_line_residuals
