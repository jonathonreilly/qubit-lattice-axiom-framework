import RigidityGeometry
import Mathlib.Tactic.FinCases

set_option autoImplicit false
open scoped BigOperators
open InterspeciesRigidity

namespace RigidityControls

abbrev Q3 := Fin 3 → ℚ
def z : Q3 := ![0, 0, 0]
def e₁ : Q3 := ![1, 0, 0]
def e₂ : Q3 := ![0, 1, 0]
def e₃ : Q3 := ![0, 0, 1]

theorem tetra_independent : AffineIndependent ℚ ![z, e₁, e₂, e₃] := by
  rw [affineIndependent_iff_of_fintype]
  intro w hw hv i
  rw [Finset.weightedVSub_eq_linear_combination hw] at hv
  have h1 : w 1 = 0 := by
    simpa [Fin.sum_univ_succ, z, e₁, e₂, e₃] using congrFun hv 0
  have h2 : w 2 = 0 := by
    simpa [Fin.sum_univ_succ, z, e₁, e₂, e₃] using congrFun hv 1
  have h3 : w 3 = 0 := by
    simpa [Fin.sum_univ_succ, z, e₁, e₂, e₃] using congrFun hv 2
  have h0 : w 0 = 0 := by simpa [Fin.sum_univ_succ, h1, h2, h3] using hw
  fin_cases i <;> assumption

theorem positive_four_cycle_application :
    (3:ℚ) = 3 ∧ (3:ℚ) = 3 ∧ (3:ℚ) = 3 := by
  apply four_cycle_multipliers (P₁ := ![2,-1,5]) (P₂ := ![5,-1,5])
    (Q₁ := ![2,2,5]) (Q₂ := ![2,-1,8]) tetra_independent 3 3 3 3 <;>
    ext i <;> fin_cases i <;> norm_num [z, e₁, e₂, e₃]

theorem positive_exceptional_application (α β γ : ℚ)
    (he : α • (e₃-e₂) - β • (e₁-z) = γ • (![0,2,-1]-![2,0,0])) :
    α = 0 ∧ β = 0 ∧ γ = 0 := by
  have hx : (![0,2,-1] : Q3) = e₂ + (-1:ℚ) • (e₃-e₂) := by
    ext i; fin_cases i <;> norm_num [e₂, e₃]
  have hy : (![2,0,0] : Q3) = z + (2:ℚ) • (e₁-z) := by
    ext i; fin_cases i <;> norm_num [z, e₁]
  obtain ⟨ha, hb, hc, _, _⟩ := opposite_skew_line_residuals tetra_independent
    (-1) 2 α β γ hx hy rfl rfl he
  exact ⟨ha, hb, hc⟩

def SquareEdges : Prop :=
  (z-![2,0,0] = (2:ℚ) • (z-e₁)) ∧
  ((![2,3,0]:Q3)-![2,0,0] = (3:ℚ) • (![1,1,0]-e₁)) ∧
  ((![2,3,0]:Q3)-![0,3,0] = (2:ℚ) • (![1,1,0]-e₂)) ∧
  (z-![0,3,0] = (3:ℚ) • (z-e₂))

theorem square_edges_true : SquareEdges := by
  unfold SquareEdges
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    ext i <;> fin_cases i <;> norm_num [z, e₁, e₂]

theorem square_multipliers_unequal : (2:ℚ) ≠ 3 := by norm_num

def TetraThreeEdges : Prop :=
  (z-e₂ = (1:ℚ) • (z-e₂)) ∧
  (e₁-e₂ = (1:ℚ) • (e₁-e₂)) ∧
  (e₁-![-1,0,2] = (2:ℚ) • (e₁-e₃))

theorem tetra_three_edges_true : TetraThreeEdges := by
  unfold TetraThreeEdges
  refine ⟨?_, ?_, ?_⟩ <;>
    ext i <;> fin_cases i <;> norm_num [z, e₁, e₂, e₃]

def CoplanarResidual : Prop :=
  ((-1/2:ℚ) • (e₂-e₁) - (-1/2:ℚ) • (![1,1,0]-z)) = (1:ℚ) • (e₁-z)

theorem coplanar_residual_true : CoplanarResidual := by
  unfold CoplanarResidual
  ext i; fin_cases i <;> norm_num [z, e₁, e₂]

def WrongCycle : Q3 := (z-e₂) + (e₁-e₂) + (e₁-e₃) - (z-e₃)

theorem wrong_cycle_nonzero : WrongCycle ≠ 0 := by
  intro h
  have h0 := congrFun h 0
  norm_num [WrongCycle, z, e₁, e₂, e₃] at h0

end RigidityControls

#print axioms RigidityControls.tetra_independent
#print axioms RigidityControls.positive_four_cycle_application
#print axioms RigidityControls.positive_exceptional_application
#print axioms RigidityControls.square_edges_true
#print axioms RigidityControls.tetra_three_edges_true
#print axioms RigidityControls.coplanar_residual_true
#print axioms RigidityControls.wrong_cycle_nonzero
