import Mathlib.Tactic.NormNum

-- Removing the nonnegative-energy hypotheses permits energies 1 and -1.
-- Both one-particle mass squares are 1, but the total mass square is 0.
example :
    ((1:ℝ)^2-0^2 ≥ 1^2 ∧ (-1:ℝ)^2-0^2 ≥ 1^2) →
    (2*1)^2 ≤ ((1:ℝ)+(-1))^2-(0+0)^2 := by
  norm_num
