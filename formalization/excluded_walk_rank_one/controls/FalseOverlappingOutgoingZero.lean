import RankOneScattering
open scoped ComplexConjugate InnerProduct
open InnerProductSpace ContinuousLinearMap RankOneScattering
noncomputable section
set_option autoImplicit false
example : ‖(scattering (1 : ℂ) 1) 1‖ ^ 2 = 0 := by
  norm_num [scattering]
