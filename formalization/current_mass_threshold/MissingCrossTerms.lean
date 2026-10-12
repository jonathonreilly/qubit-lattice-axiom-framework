import Mathlib.Tactic.NormNum

-- Retain positive energies and both one-particle mass bounds, but replace
-- the squared total energy-momentum by the sum of individual mass squares.
example :
    (0 ≤ (1:ℝ) ∧ (1:ℝ)^2-0^2 ≥ 1^2) →
    (2*1)^2 ≤ ((1:ℝ)^2-0^2)+((1:ℝ)^2-0^2) := by
  norm_num
