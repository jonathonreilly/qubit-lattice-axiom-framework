import RankOneScattering
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap RankOneScattering
noncomputable section
set_option autoImplicit false
universe u
variable {E : Type u} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
local notation "⟪" x ", " y "⟫" => inner ℂ x y
example (g : E →L[ℂ] E) (hg : g† = g) (v : E)
    {s : ℂ} (hs : ‖s‖ = 1) :
    (scattering v s)† ∘L g ∘L scattering v s - g =
      (s - 1) • rankOne ℂ (centered g v) v +
      (s - 1) • rankOne ℂ v (centered g v) := by
  rw [observable_difference g hg v hs]
  ext x
  simp only [_root_.add_apply, _root_.smul_apply, rankOne_apply]
  module
