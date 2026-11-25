import GapChain.Trace
import GapChain.Periodic

/-!
# Stage 1f: the Wilson torus data with no remaining hypothesis

Row 1508 (`Trace.lean`) proves the cyclic trace identity for the Wilson
transfer operator. Row 1509 (`Periodic.lean`) proves `Z = cyclic` and builds
the torus data from that identity. The two modules define `cyclic` with the
same body, so they agree by `rfl`. This file joins them and states Theorem S
for the SU(2) Wilson model. The seed hypothesis of Theorem S stays open.
-/

noncomputable section

namespace GapChain.Wilson.Assembly

theorem cyclic_agree (β : ℝ) (R : Box) (a : ℕ) :
    Trace.cyclic β R a = Periodic.cyclic β R a := rfl

/-- The SU(2) Wilson torus data at positive coupling, with no hypothesis. -/
def torusData (β : ℝ) (hβ : 0 < β) : TorusData :=
  Periodic.torusData_of_trace β hβ fun R hR a ha =>
    (cyclic_agree β R a).symm.trans (Trace.cyclic_eq_tsum hβ R hR ha)

/-- On valid boxes the spectrum is the transfer-operator spectrum of row 1506. -/
theorem torusData_spectrum (β : ℝ) (hβ : 0 < β) (R : Box) (hR : R.Valid) :
    (torusData β hβ).spectrum R = (transfer_boxSpectrum β hβ R hR).choose :=
  Periodic.torusData_of_trace_spectrum β hβ _ R hR

/-- On valid boxes, for every time period a ≥ 3, the weight of the torus data
is the SU(2) Wilson partition function `Z β a R`. -/
theorem torusData_weight (β : ℝ) (hβ : 0 < β) (R : Box) (hR : R.Valid) {a : ℕ}
    (ha : 3 ≤ a) : ((torusData β hβ).spectrum R).weight a = Z β a R := by
  rw [torusData_spectrum β hβ R hR]
  exact ((transfer_boxSpectrum β hβ R hR).choose_spec.2.2 a ha).trans
    ((Trace.cyclic_eq_tsum hβ R hR ha).symm.trans
      ((cyclic_agree β R a).trans (Periodic.Z_eq_cyclic β a R).symm))

/-- Theorem S for the SU(2) Wilson model: a seed below 1/5041 on one cube
gives thermal decay and a gap on every dyadic cube. -/
theorem wilson_theoremS (β : ℝ) (hβ : 0 < β) {N : ℕ} (hN : 3 ≤ N)
    (hseed : (torusData β hβ).seed N < 1 / 5041) (k : ℕ) :
    (torusData β hβ).seed (2 ^ k * N) ≤ (5041 * (torusData β hβ).seed N) ^ (2 ^ k) / 5041 ∧
      (torusData β hβ).seedRate N ≤ ((torusData β hβ).spectrum (cube (2 * (2 ^ k * N)))).gap :=
  (torusData β hβ).theoremS hN hseed k

end GapChain.Wilson.Assembly

#print axioms GapChain.Wilson.Assembly.cyclic_agree
#print axioms GapChain.Wilson.Assembly.torusData
#print axioms GapChain.Wilson.Assembly.torusData_spectrum
#print axioms GapChain.Wilson.Assembly.torusData_weight
#print axioms GapChain.Wilson.Assembly.wilson_theoremS
