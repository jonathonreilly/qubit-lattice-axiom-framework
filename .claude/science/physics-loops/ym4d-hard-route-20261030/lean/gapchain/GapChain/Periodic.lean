import GapChain.Transfer
import Mathlib.MeasureTheory.Integral.Pi
import Mathlib.Probability.ProductMeasure

/-!
# Periodic Wilson weights from the rectangular transfer kernel

The link and plaquette conventions follow Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text (outline GL8, complete account I §1.1).
The time-slice calculation follows Claude Opus 5.5, row 667 §1 and row 698
Lemma 1.1. The spectral identity is the separate input from row 1508.
-/

noncomputable section

open MeasureTheory Filter Topology
open scoped BigOperators

namespace GapChain.Wilson.Periodic

def cyclic (β : ℝ) (R : Box) (a : ℕ) : ℝ :=
  ∫ u : Fin a → Slice R, ∏ t : Fin a, transferKernel β R (u t, u (finRotate a t))
    ∂(Measure.pi fun _ => sliceHaar R)

/-- Insert time in coordinate zero of a four-dimensional site. -/
def site (a : ℕ) (R : Box) : Fin a × Vertex R ≃ Site (sides a R) :=
  Fin.consEquiv (fun i => Fin (sides a R i))

/-- Index each spatial link by its time and spatial edge, and each temporal
link by its time and spatial vertex. All three spatial periods are independent. -/
def linkIndex (a : ℕ) (R : Box) :
    ((Fin a × Edge R) ⊕ (Fin a × Vertex R)) ≃ Link (sides a R) where
  toFun := Sum.elim (fun p => (site a R (p.1, p.2.1), p.2.2.succ))
    (fun p => (site a R p, 0))
  invFun l := Fin.cases (Sum.inr ((site a R).symm l.1))
    (fun i => Sum.inl (((site a R).symm l.1).1, ((site a R).symm l.1).2, i)) l.2
  left_inv := by
    rintro (⟨t, x, i⟩ | ⟨t, x⟩) <;> simp
  right_inv := by
    rintro ⟨y, d⟩
    cases d using Fin.cases <;> simp

/-- Four-dimensional links as a family of spatial fields and a family of
vertex gauges, both indexed by time. -/
def layers (a : ℕ) (R : Box) : Config (sides a R) ≃ᵐ
    (Fin a → Slice R) × (Fin a → Gauges R) :=
  ((MeasurableEquiv.piCongrLeft (fun _ => SU2) (linkIndex a R)).symm.trans
    (MeasurableEquiv.sumPiEquivProdPi (fun _ => SU2))).trans
      ((MeasurableEquiv.curry (Fin a) (Edge R) SU2).prodCongr
        (MeasurableEquiv.curry (Fin a) (Vertex R) SU2))

theorem measurePreserving_layers (a : ℕ) (R : Box) :
    MeasurePreserving (layers a R) (haar (sides a R))
      ((Measure.pi fun _ : Fin a => sliceHaar R).prod
        (Measure.pi fun _ : Fin a => gaugeHaar R)) := by
  have curryHaar (I : Type) [Fintype I] :
      MeasurePreserving (MeasurableEquiv.curry (Fin a) I SU2)
        (Measure.pi fun _ => linkHaar) (Measure.pi fun _ => Measure.pi fun _ => linkHaar) := by
    refine ⟨(MeasurableEquiv.curry ..).measurable, ?_⟩
    simpa only [Measure.infinitePi_eq_pi] using
      (Measure.infinitePi_map_curry (fun (_ : Fin a) (_ : I) => linkHaar))
  exact ((curryHaar (Edge R)).prod (curryHaar (Vertex R))).comp
    ((measurePreserving_sumPiEquivProdPi
      (fun _ : (Fin a × Edge R) ⊕ (Fin a × Vertex R) => linkHaar)).comp
      ((measurePreserving_piCongrLeft (fun _ => linkHaar) (linkIndex a R)).symm _))

/-- The three temporal planes and the three purely spatial planes. -/
def planes : Fin 3 ⊕ SpatialPlane ≃ Plane where
  toFun := Sum.elim (fun i => ⟨(0, i.succ), Fin.succ_pos i⟩)
    (fun p => ⟨(p.1.1.succ, p.1.2.succ), Fin.succ_lt_succ_iff.mpr p.2⟩)
  invFun
    | ⟨(i, j), hij⟩ =>
      Fin.cases (motive := fun j => i < j → Fin 3 ⊕ SpatialPlane)
        (fun h => (Fin.not_lt_zero i h).elim)
        (fun j => Fin.cases (motive := fun i => i < j.succ → Fin 3 ⊕ SpatialPlane)
          (fun _ => Sum.inl j) (fun i h => Sum.inr ⟨(i, j), Fin.succ_lt_succ_iff.mp h⟩) i) j hij
  left_inv := by rintro (i | ⟨⟨i, j⟩, h⟩) <;> rfl
  right_inv := by
    rintro ⟨⟨i, j⟩, h⟩
    cases j using Fin.cases with
    | zero => exact (Fin.not_lt_zero _ h).elim
    | succ j => cases i using Fin.cases <;> rfl

set_option maxHeartbeats 800000 in
/-- The oriented temporal plaquette starts along the temporal link at x,
then follows the spatial link on the next slice. -/
theorem action_eq_layers (a : ℕ) (R : Box) (U : Config (sides a R)) :
    action U = ∑ t : Fin a,
      (spatialAction ((layers a R U).1 t) +
        temporalAction ((layers a R U).1 t,
          gaugeAction R ((layers a R U).1 (finRotate a t), (layers a R U).2 t))) := by
  classical
  let u := (layers a R U).1
  let g := (layers a R U).2
  have spaceLink (t : Fin a) (x : Vertex R) (i : Fin 3) :
      U (site a R (t, x), i.succ) = u t (x, i) := rfl
  have timeLink (t : Fin a) (x : Vertex R) : U (site a R (t, x), 0) = g t x := rfl
  have timeStep (t : Fin a) (x : Vertex R) :
      step (site a R (t, x)) 0 = site a R (finRotate a t, x) := by
    funext k
    cases k using Fin.cases with
    | zero =>
      change (if (0 : Dir) = 0 then finRotate a t else t) = finRotate a t
      exact if_pos rfl
    | succ j =>
      change (if j.succ = 0 then finRotate (spatialSides R j) (x j) else x j) = x j
      exact if_neg (Fin.succ_ne_zero j)
  have spaceStep (t : Fin a) (x : Vertex R) (i : Fin 3) :
      step (site a R (t, x)) i.succ = site a R (t, spatialStep x i) := by
    funext k
    cases k using Fin.cases with
    | zero =>
      change (if (0 : Dir) = i.succ then finRotate a t else t) = t
      exact if_neg (Fin.succ_ne_zero i).symm
    | succ j =>
      change (if j.succ = i.succ then finRotate (spatialSides R j) (x j) else x j) =
        (if j = i then finRotate (spatialSides R j) (x j) else x j)
      simp only [Fin.succ_inj]
  -- The geometric action has already paired both orientations using halfTrace_reverse.
  let onSite (x : Site (sides a R)) := ∑ p : Plane, (1 - halfTrace (transport U x p.1.1 p.1.2))
  rw [action_eq_geometric U]
  change (∑ x, onSite x) = _
  rw [← (site a R).sum_comp onSite, Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro t _
  let face (x : Vertex R) (p : Plane) :=
    1 - halfTrace (transport U (site a R (t, x)) p.1.1 p.1.2)
  change (∑ x : Vertex R, ∑ p : Plane, face x p) = spatialAction (u t) +
    temporalAction (u t, gaugeAction R (u (finRotate a t), g t))
  have split (x : Vertex R) :
      (∑ p : Plane, face x p) =
        (∑ p : SpatialPlane, face x (planes (.inr p))) +
        (∑ i : Fin 3, face x (planes (.inl i))) := by
    rw [← planes.sum_comp (face x), Fintype.sum_sum_type, add_comm]
  simp only [split, Finset.sum_add_distrib]
  refine congrArg₂ (· + ·) ?_ ?_
  · unfold spatialAction
    apply Finset.sum_congr rfl
    intro x _
    apply Finset.sum_congr rfl
    intro p _
    change 1 - halfTrace (transport U (site a R (t, x)) p.1.1.succ p.1.2.succ) = _
    simp only [transport, spaceStep, spaceLink]
  · unfold temporalAction
    rw [Fintype.sum_prod_type]
    apply Finset.sum_congr rfl
    intro x _
    apply Finset.sum_congr rfl
    intro i _
    change 1 - halfTrace (transport U (site a R (t, x)) 0 i.succ) =
      1 - halfTrace (g t x * u (finRotate a t) (x, i) *
        (g t (spatialStep x i))⁻¹ * (u t (x, i))⁻¹)
    simp only [transport, timeStep, spaceStep, timeLink, spaceLink]

/-- One time step before integrating its temporal bonds. -/
def layerWeight (β : ℝ) {R : Box} (u v : Slice R) (g : Gauges R) : ℝ :=
  Real.exp (-β * (spatialAction u + spatialAction v) / 2) *
    temporal β R (u, gaugeAction R (v, g))

theorem integral_layerWeight (β : ℝ) {R : Box} (u v : Slice R) :
    ∫ g, layerWeight β u v g ∂gaugeHaar R = transferKernel β R (u, v) := by
  simp only [transferKernel_apply, layerWeight, integral_const_mul]
  congr 1
  apply integral_congr_ae
  apply ae_of_all
  intro g
  change Real.exp (-β * ∑ e : Edge R, _) = _
  rw [Finset.mul_sum, Real.exp_sum]
  rfl

/-- Cyclic rotation gives both halves of each spatial action exactly once. -/
theorem density_eq_layerProduct (β : ℝ) (a : ℕ) (R : Box) (U : Config (sides a R)) :
    density β U = ∏ t : Fin a, layerWeight β ((layers a R U).1 t)
      ((layers a R U).1 (finRotate a t)) ((layers a R U).2 t) := by
  let S := fun t => spatialAction ((layers a R U).1 t)
  let V := fun t => temporalAction ((layers a R U).1 t,
    gaugeAction R ((layers a R U).1 (finRotate a t), (layers a R U).2 t))
  have rotate : (∑ t, S (finRotate a t)) = ∑ t, S t := Equiv.sum_comp (finRotate a) S
  unfold density
  rw [action_eq_layers a R U]
  change Real.exp (-β * ∑ t, (S t + V t)) =
    ∏ t, (Real.exp (-β * (S t + S (finRotate a t)) / 2) * Real.exp (-β * V t))
  simp_rw [← Real.exp_add]
  rw [← Real.exp_sum]
  congr 1
  simp only [Finset.sum_add_distrib, ← Finset.sum_div, ← Finset.mul_sum, rotate]
  ring

/-- The periodic Haar factorization holds for the indexed lattice at every
natural period, including empty index types, and for every real coupling. -/
theorem Z_eq_cyclic (β : ℝ) (a : ℕ) (R : Box) : Z β a R = cyclic β R a := by
  let e := layers a R
  let μ := Measure.pi fun _ : Fin a => sliceHaar R
  let ν := Measure.pi fun _ : Fin a => gaugeHaar R
  have h := (measurePreserving_layers a R).symm e
  let F := fun z : (Fin a → Slice R) × (Fin a → Gauges R) => density β (e.symm z)
  have hi : Integrable F (μ.prod ν) := h.integrable_comp_of_integrable (integrable_density β _)
  change (∫ U, density β U ∂haar (sides a R)) = _
  rw [← h.integral_comp' (density β)]
  change (∫ z, F z ∂μ.prod ν) = _
  rw [integral_prod F hi]
  apply integral_congr_ae
  apply ae_of_all
  intro u
  have point (g : Fin a → Gauges R) :
      F (u, g) = ∏ t, layerWeight β (u t) (u (finRotate a t)) (g t) := by
    simpa only [F, e, MeasurableEquiv.apply_symm_apply] using
      density_eq_layerProduct β a R (e.symm (u, g))
  simp only [point]
  calc
    _ = ∏ t, ∫ g, layerWeight β (u t) (u (finRotate a t)) g ∂gaugeHaar R :=
      integral_fintype_prod_eq_prod (μ := fun _ : Fin a => gaugeHaar R)
        (fun t g => layerWeight β (u t) (u (finRotate a t)) g)
    _ = _ := Finset.prod_congr rfl fun t _ => integral_layerWeight β (u t) (u (finRotate a t))

/-- Claude Opus 5.5, row 1503, appendix A. -/
theorem weight_logConvex (B : BoxSpectrum) {a : ℕ} (ha : 3 ≤ a) :
    B.weight (a + 1) ^ 2 ≤ B.weight a * B.weight (a + 2) := by
  have hA : HasSum (fun i => B.ratio i ^ a) (B.thermal a) := (B.summable ha).hasSum
  have hX : HasSum (fun i => B.ratio i ^ (a + 1)) (B.thermal (a + 1)) :=
    (B.summable (by omega : 3 ≤ a + 1)).hasSum
  have hC : HasSum (fun i => B.ratio i ^ (a + 2)) (B.thermal (a + 2)) :=
    (B.summable (by omega : 3 ≤ a + 2)).hasSum
  have hcs : B.thermal (a + 1) ^ 2 ≤ B.thermal a * B.thermal (a + 2) := by
    refine le_of_tendsto_of_tendsto' (hX.tendsto_sum_nat.pow 2)
      (hA.tendsto_sum_nat.mul hC.tendsto_sum_nat) (fun n => ?_)
    have h := Finset.sum_mul_sq_le_sq_mul_sq (Finset.range n) (fun i => Real.sqrt (B.ratio i) ^ a)
      (fun i => Real.sqrt (B.ratio i) ^ (a + 2))
    have e1 : ∀ i, Real.sqrt (B.ratio i) ^ a * Real.sqrt (B.ratio i) ^ (a + 2) =
        B.ratio i ^ (a + 1) := by
      intro i
      rw [← pow_add, show a + (a + 2) = 2 * (a + 1) by ring, pow_mul, Real.sq_sqrt (B.nonneg i)]
    have e2 : ∀ k i, (Real.sqrt (B.ratio i) ^ k) ^ 2 = B.ratio i ^ k := by
      intro k i
      rw [← pow_mul, mul_comm, pow_mul, Real.sq_sqrt (B.nonneg i)]
    simpa only [e1, e2] using h
  have ham : 2 * B.thermal (a + 1) ≤ B.thermal a + B.thermal (a + 2) := by
    refine hasSum_le (fun i => ?_) (hX.mul_left 2) (hA.add hC)
    have hr := B.nonneg i
    have h0 : 0 ≤ B.ratio i ^ a * (1 - B.ratio i) ^ 2 := mul_nonneg (pow_nonneg hr a) (sq_nonneg _)
    have e1 : B.ratio i ^ (a + 1) = B.ratio i ^ a * B.ratio i := pow_succ _ _
    have e2 : B.ratio i ^ (a + 2) = B.ratio i ^ a * B.ratio i * B.ratio i := by
      rw [pow_succ, pow_succ]
    simp only [e1, e2]
    nlinarith [h0]
  have hA0 := B.thermal_nonneg a
  have hC0 := B.thermal_nonneg (a + 2)
  have hsq : (1 + B.thermal (a + 1)) ^ 2 ≤ (1 + B.thermal a) * (1 + B.thermal (a + 2)) := by
    nlinarith [hcs, ham]
  unfold BoxSpectrum.weight
  have ht : 0 ≤ B.top ^ a * B.top ^ (a + 2) := by have := B.top_pos; positivity
  calc (B.top ^ (a + 1) * (1 + B.thermal (a + 1))) ^ 2
      = (B.top ^ a * B.top ^ (a + 2)) * (1 + B.thermal (a + 1)) ^ 2 := by ring
    _ ≤ (B.top ^ a * B.top ^ (a + 2)) * ((1 + B.thermal a) * (1 + B.thermal (a + 2))) :=
        mul_le_mul_of_nonneg_left hsq ht
    _ = B.top ^ a * (1 + B.thermal a) * (B.top ^ (a + 2) * (1 + B.thermal (a + 2))) := by ring

/-- Select the actual transfer spectrum on valid boxes. The structure also
requires a value on invalid boxes, where the reference cube supplies one. -/
def spectrum (β : ℝ) (hβ : 0 < β) (R : Box) : BoxSpectrum := by
  classical
  exact if hR : R.Valid then (transfer_boxSpectrum β hβ R hR).choose
    else (transfer_boxSpectrum β hβ (cube 3) ⟨le_rfl, le_rfl, le_rfl⟩).choose

/-- The cyclic spectral identity is the sole remaining input to the
rectangular Wilson torus data at positive coupling. -/
def torusData_of_trace (β : ℝ) (hβ : 0 < β)
    (trace : ∀ R : Box, R.Valid → ∀ a : ℕ, 3 ≤ a →
      cyclic β R a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a) : TorusData := by
  have bridge (R : Box) (hR : R.Valid) (a : ℕ) (ha : 3 ≤ a) :
      (spectrum β hβ R).weight a = Z β a R := by
    calc
      _ = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a := by
        simpa only [spectrum, dif_pos hR] using (transfer_boxSpectrum β hβ R hR).choose_spec.2.2 a ha
      _ = cyclic β R a := (trace R hR a ha).symm
      _ = Z β a R := (Z_eq_cyclic β a R).symm
  let fields := fields_of_bridge β (spectrum β hβ) bridge
  exact { spectrum := spectrum β hβ
          cross := fields.1
          lower := fields.2
          logConvex := fun R _ a ha => weight_logConvex (spectrum β hβ R) ha }

/-- On the domain of the trace identity the constructed data uses the
witness chosen from row 1506, including its multiplicity enumeration. -/
theorem torusData_of_trace_spectrum (β : ℝ) (hβ : 0 < β) (trace)
    (R : Box) (hR : R.Valid) :
    (torusData_of_trace β hβ trace).spectrum R = (transfer_boxSpectrum β hβ R hR).choose := by
  simp only [torusData_of_trace, spectrum, dif_pos hR]

#print axioms measurePreserving_layers
#print axioms action_eq_layers
#print axioms integral_layerWeight
#print axioms density_eq_layerProduct
#print axioms Z_eq_cyclic
#print axioms weight_logConvex
#print axioms torusData_of_trace
#print axioms torusData_of_trace_spectrum

end GapChain.Wilson.Periodic
