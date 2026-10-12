import RankOneScattering
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap RankOneScattering
noncomputable section
set_option autoImplicit false
example : ((scattering (1 : ℂ) 2)† ∘L scattering (1 : ℂ) 2) 1 = 1 := by
  rw [scattering_adjoint]
  norm_num [scattering, map_ofNat]
