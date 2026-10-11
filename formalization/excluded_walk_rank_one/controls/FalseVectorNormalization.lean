import RankOneScattering
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap RankOneScattering
noncomputable section
set_option autoImplicit false
example : ((scattering (2 : ℂ) (-1))† ∘L scattering (2 : ℂ) (-1)) 1 = 1 := by
  rw [scattering_adjoint]
  norm_num [scattering, map_ofNat]
