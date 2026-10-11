import ControlData
open RigidityControls

-- The coplanar residual witness has alpha=beta=-1/2 and gamma=1.
-- Thus the claimed gamma=0 after removing skewness is mathematically false.
example : CoplanarResidual := coplanar_residual_true
#check RigidityControls.coplanar_residual_true
example (_h : CoplanarResidual) : (1 : ℚ) = 0 := by
  norm_num
