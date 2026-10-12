import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

noncomputable section
set_option autoImplicit false
set_option maxHeartbeats 800000
open scoped BigOperators

namespace CurrentMassThreshold

theorem reverse_minkowski_identity (e₁ e₂ u₁ u₂ : ℝ) :
    (e₁ * e₂ - u₁ * u₂)^2 =
      (e₁^2-u₁^2)*(e₂^2-u₂^2)+(e₁*u₂-e₂*u₁)^2 := by
  ring

theorem pair_lower_bound (m e₁ e₂ u₁ u₂ : ℝ)
    (he₁ : 0 ≤ e₁) (he₂ : 0 ≤ e₂)
    (h₁ : m^2 ≤ e₁^2-u₁^2) (h₂ : m^2 ≤ e₂^2-u₂^2) :
    m^2 ≤ e₁*e₂-u₁*u₂ := by
  have hc₁ : |u₁| ≤ e₁ := by
    apply (sq_le_sq₀ (abs_nonneg u₁) he₁).mp
    rw [sq_abs]
    nlinarith [sq_nonneg m]
  have hc₂ : |u₂| ≤ e₂ := by
    apply (sq_le_sq₀ (abs_nonneg u₂) he₂).mp
    rw [sq_abs]
    nlinarith [sq_nonneg m]
  have hp : |u₁| * |u₂| ≤ e₁*e₂ :=
    mul_le_mul hc₁ hc₂ (abs_nonneg u₂) he₁
  have hn : 0 ≤ e₁*e₂-u₁*u₂ := by
    have ha : u₁*u₂ ≤ e₁*e₂ :=
      (le_abs_self (u₁*u₂)).trans (by simpa [abs_mul] using hp)
    exact sub_nonneg.mpr ha
  have hd : m^2*m^2 ≤ (e₁^2-u₁^2)*(e₂^2-u₂^2) :=
    mul_le_mul h₁ h₂ (sq_nonneg m) ((sq_nonneg m).trans h₁)
  have hs : (m^2)^2 ≤ (e₁*e₂-u₁*u₂)^2 := by
    rw [reverse_minkowski_identity]
    nlinarith [sq_nonneg (e₁*u₂-e₂*u₁)]
  exact (sq_le_sq₀ (sq_nonneg m) hn).mp hs

theorem finite_total_mass_bound {ι : Type*} (s : Finset ι)
    (m : ℝ) (e u : ι → ℝ)
    (he : ∀ i ∈ s, 0 ≤ e i)
    (hm : ∀ i ∈ s, m^2 ≤ (e i)^2-(u i)^2) :
    ((s.card : ℝ)*m)^2 ≤ (∑ i ∈ s, e i)^2-(∑ i ∈ s, u i)^2 := by
  have hp : (∑ i ∈ s, ∑ j ∈ s, m^2) ≤
      ∑ i ∈ s, ∑ j ∈ s, (e i*e j-u i*u j) := by
    apply Finset.sum_le_sum
    intro i hi
    apply Finset.sum_le_sum
    intro j hj
    exact pair_lower_bound m (e i) (e j) (u i) (u j)
      (he i hi) (he j hj) (hm i hi) (hm j hj)
  calc
    ((s.card : ℝ)*m)^2 = ∑ i ∈ s, ∑ j ∈ s, m^2 := by
      simp
      ring
    _ ≤ ∑ i ∈ s, ∑ j ∈ s, (e i*e j-u i*u j) := hp
    _ = (∑ i ∈ s, e i)^2-(∑ i ∈ s, u i)^2 := by
      simp_rw [Finset.sum_sub_distrib, ← Finset.mul_sum]
      simp_rw [← Finset.sum_mul]
      ring

theorem missing_energy_sign_counterexample :
    (1:ℝ)^2-0^2 ≥ 1^2 ∧ (-1:ℝ)^2-0^2 ≥ 1^2 ∧
    ((1:ℝ)+(-1))^2-(0+0)^2 < (2*1)^2 := by
  norm_num

theorem missing_cross_terms_counterexample :
    ((1:ℝ)^2-0^2)+((1:ℝ)^2-0^2) < (2*1)^2 ∧
    ((1:ℝ)+1)^2-(0+0)^2 = (2*1)^2 := by
  norm_num

end CurrentMassThreshold

#print axioms CurrentMassThreshold.reverse_minkowski_identity
#print axioms CurrentMassThreshold.pair_lower_bound
#print axioms CurrentMassThreshold.finite_total_mass_bound
#print axioms CurrentMassThreshold.missing_energy_sign_counterexample
#print axioms CurrentMassThreshold.missing_cross_terms_counterexample
