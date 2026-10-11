import RankOneScattering
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap RankOneScattering
noncomputable section
set_option autoImplicit false
universe u
variable {E : Type u} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
local notation "⟪" x ", " y "⟫" => inner ℂ x y
example (g : E →L[ℂ] E) (hg : g† = g) {v u : E}
    (hv : ‖v‖ = 1) (hu : ‖u‖ = 1) (hvu : ⟪v, u⟫ = 0)
    {s : ℂ} (hs : ‖s‖ = 1) (sigma : ℝ)
    (hw : centered g v = (sigma : ℂ) • u) {r : ℝ} (hr : 2 * r ^ 2 = 1) :
    ⟪coherent v u r,
      ((scattering v s)† ∘L g ∘L scattering v s - g) (coherent v u r)⟫ =
      (-sigma * s.im : ℝ) := by
  rw [coherent_current g hg hv hu hvu hs sigma hw hr]
  norm_cast
  ring
