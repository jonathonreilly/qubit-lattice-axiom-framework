import ControlData
open RigidityControls

-- The second edge is added instead of subtracted; the claimed cycle is
-- the nonzero vector (2,-2,0) at the verified tetrahedron.
#check RigidityControls.wrong_cycle_nonzero
example : WrongCycle = 0 := by
  ext i
  fin_cases i <;> norm_num [WrongCycle, z, e₁, e₂, e₃]
