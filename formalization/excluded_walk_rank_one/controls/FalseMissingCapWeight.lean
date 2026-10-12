import RankOneScattering
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap RankOneScattering
noncomputable section
set_option autoImplicit false
universe u
variable {E : Type u} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
local notation "⟪" x ", " y "⟫" => inner ℂ x y
example (A Q : E →L[ℂ] E) (hA : A† = A) (hAA : A ∘L A = A)
    (v : E) (hne : A v ≠ 0) (s : ℂ) (hdisjoint : Q (A v) = 0) :
    ‖Q (scattering v s (capVector A v))‖ ^ 2 =
      ‖s - 1‖ ^ 2 * ‖Q v‖ ^ 2 := by
  rw [cap_transfer A Q hA hAA v hne s hdisjoint]
  ring
