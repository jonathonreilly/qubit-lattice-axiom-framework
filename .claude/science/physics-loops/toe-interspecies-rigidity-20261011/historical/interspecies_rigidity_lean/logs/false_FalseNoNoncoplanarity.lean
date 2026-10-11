import ControlData
open RigidityControls

-- The compiled square witness satisfies all four cross-edge equations,
-- but its multipliers alternate 2 and 3. Dropping noncoplanarity is false.
example : SquareEdges := square_edges_true
#check RigidityControls.square_edges_true
example (_h : SquareEdges) : (2 : ℚ) = 3 := by
  norm_num
