import RankOneScattering
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap RankOneScattering
noncomputable section
set_option autoImplicit false
example : ((scattering (1 : ℂ) 2)† ∘L scattering (1 : ℂ) 2) 1 = 4 := by
  rw [scattering_adjoint]
  norm_num [scattering, map_ofNat]
example : ((scattering (2 : ℂ) (-1))† ∘L scattering (2 : ℂ) (-1)) 1 = 49 := by
  rw [scattering_adjoint]
  norm_num [scattering, map_ofNat]
example : ‖(scattering (1 : ℂ) 1) 1‖ ^ 2 = 1 := by
  norm_num [scattering]
