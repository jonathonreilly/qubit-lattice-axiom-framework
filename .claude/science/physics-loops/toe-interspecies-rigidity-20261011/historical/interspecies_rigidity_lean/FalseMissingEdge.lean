import ControlData
open RigidityControls

-- These genuinely independent anchors satisfy three cross edges with
-- multipliers 1, 1, 2. Omitting the fourth edge does not force equality.
example : AffineIndependent ℚ ![z, e₁, e₂, e₃] := tetra_independent
example : TetraThreeEdges := tetra_three_edges_true
#check RigidityControls.tetra_three_edges_true
example (_h : TetraThreeEdges) : (1 : ℚ) = 2 := by
  norm_num
