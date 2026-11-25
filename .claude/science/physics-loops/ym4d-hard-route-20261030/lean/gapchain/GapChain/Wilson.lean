import GapChain.TheoremS
import GapChain.LemmaM1
import Mathlib.Analysis.CStarAlgebra.Matrix
import Mathlib.Analysis.CStarAlgebra.ContinuousFunctionalCalculus.Order
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Analysis.Convex.Integral
import Mathlib.Analysis.InnerProductSpace.Spectrum
import Mathlib.Analysis.InnerProductSpace.StarOrder
import Mathlib.Analysis.InnerProductSpace.l2Space
import Mathlib.Logic.Equiv.Fin.Rotate
import Mathlib.MeasureTheory.Constructions.Pi
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.MeasureTheory.Measure.Haar.Basic
import Mathlib.Topology.Algebra.Star.Unitary

/-!
# Wilson partition functions on rectangular periodic lattices

The group is the matrix SU(2), with Haar mass one. A site has four independent
cyclic coordinates. A link points in the positive direction of its coordinate.
The two traversals of each geometric square have inverse transports. We use
both ordered directions with weight one half to make relabelling transparent.

The normalization and the finite-volume symmetry follow the outline of Ethan
Sussman and Levent Alpoge, with Claude and Codex (240–278), and CA-I §1.1.
The rectangular conventions are those of the lane's rows 697 and 698, Lemma 1.1.
-/

noncomputable section
open MeasureTheory Set
open scoped BigOperators Matrix

namespace GapChain.Wilson

abbrev SU2 := Matrix.specialUnitaryGroup (Fin 2) ℂ

instance : IsTopologicalGroup SU2 where
  continuous_inv := continuous_induced_rng.mpr
    (continuous_subtype_val.star : Continuous (fun U : SU2 => star U.val))

instance : CompactSpace SU2 := by
  apply isCompact_iff_compactSpace.mp
  refine (isCompact_closedBall (0 : ℂ) 1).matrix.of_isClosed_subset ?_ ?_
  · have hc : IsClosed {A : Matrix (Fin 2) (Fin 2) ℂ | A.det = 1} :=
      isClosed_eq continuous_id.matrix_det continuous_const
    exact isClosed_unitary.inter hc
  · intro U hU i j
    simpa [Metric.mem_closedBall, dist_zero_right] using
      entry_norm_bound_of_unitary (Matrix.specialUnitaryGroup_le_unitaryGroup hU) i j

instance : SecondCountableTopology SU2 :=
  TopologicalSpace.secondCountableTopology_induced SU2 (Fin 2 → Fin 2 → ℂ) (fun U => U.val)

instance : MeasurableSpace SU2 := borel SU2
instance : BorelSpace SU2 := ⟨rfl⟩

/-- The compact normalizing set is the entire group. -/
def haarDomain : TopologicalSpace.PositiveCompacts SU2 :=
  ⟨⟨univ, isCompact_univ⟩, by simp⟩

abbrev linkHaar : Measure SU2 := Measure.haarMeasure haarDomain

instance : IsProbabilityMeasure linkHaar :=
  ⟨Measure.haarMeasure_self (K₀ := haarDomain)⟩

/-- The real part of the trace in the defining representation, divided by two. -/
def halfTrace (g : SU2) : ℝ := g.val.trace.re / 2

theorem continuous_halfTrace : Continuous halfTrace := by
  unfold halfTrace
  fun_prop

theorem halfTrace_inv (g : SU2) : halfTrace g⁻¹ = halfTrace g := by
  change (g.valᴴ).trace.re / 2 = g.val.trace.re / 2
  rw [Matrix.trace_conjTranspose]
  rfl

theorem halfTrace_le_one (g : SU2) : halfTrace g ≤ 1 := by
  have bound (i : Fin 2) : (g.val i i).re ≤ 1 :=
    (Complex.re_le_norm _).trans (entry_norm_bound_of_unitary g.property.1 i i)
  simp only [halfTrace, Matrix.trace, Fin.sum_univ_two, Matrix.diag_apply, Complex.add_re]
  linarith [bound 0, bound 1]

/-- Multiplying the first edge of a loop by the nontrivial central element
negates its trace. Its determinant is one in dimension two. -/
def centerMinus : SU2 := ⟨-1, by
  rw [Matrix.mem_specialUnitaryGroup_iff]
  constructor
  · simp [Unitary.mem_iff]
  · simp [Matrix.det_neg]⟩

theorem halfTrace_centerMinus (g : SU2) : halfTrace (centerMinus * g) = -halfTrace g := by
  change ((-1 : Matrix (Fin 2) (Fin 2) ℂ) * g.val).trace.re / 2 = -(g.val.trace.re / 2)
  simp
  ring

abbrev Dir := Fin 4
abbrev Sides := Dir → ℕ
abbrev Site (n : Sides) := (i : Dir) → Fin (n i)
abbrev Link (n : Sides) := Site n × Dir
abbrev Config (n : Sides) := Link n → SU2
abbrev haar (n : Sides) : Measure (Config n) := Measure.pi (fun _ => linkHaar)

/-- A positive unit step with periodic boundary conditions. -/
def step {n : Sides} (x : Site n) (i : Dir) : Site n :=
  fun k => if k = i then finRotate (n k) (x k) else x k

/-- Boundary word for the positive i,j traversal from x. -/
def transport {n : Sides} (U : Config n) (x : Site n) (i j : Dir) : SU2 :=
  U (x, i) * U (step x i, j) * (U (step x j, i))⁻¹ * (U (x, j))⁻¹

theorem halfTrace_reverse {n : Sides} (U : Config n) (x : Site n) (i j : Dir) :
    halfTrace (transport U x j i) = halfTrace (transport U x i j) := by
  rw [← halfTrace_inv (transport U x i j)]
  simp [transport, mul_assoc]

/-- Both orientations of the six coordinate planes. -/
abbrev OrderedPlane := {p : Dir × Dir // p.1 ≠ p.2}
abbrev Face (n : Sides) := Site n × OrderedPlane

def faceTrace {n : Sides} (U : Config n) (p : Face n) : ℝ :=
  halfTrace (transport U p.1 p.2.val.1 p.2.val.2)

/-- Each unoriented plaquette contributes exactly one copy of 1 − Re tr(Uₚ)/2. -/
def action {n : Sides} (U : Config n) : ℝ :=
  (∑ p : Face n, (1 - faceTrace U p)) / 2

/-- Canonically oriented geometric planes. -/
abbrev Plane := {p : Dir × Dir // p.1 < p.2}

/-- Choose a geometric plane and one of its two orientations. -/
def orientations : Plane ⊕ Plane ≃ OrderedPlane where
  toFun
    | .inl p => ⟨p.val, p.property.ne⟩
    | .inr p => ⟨p.val.swap, p.property.ne'⟩
  invFun p := if h : p.val.1 < p.val.2 then Sum.inl ⟨p.val, h⟩ else
    Sum.inr ⟨p.val.swap, lt_of_le_of_ne (le_of_not_gt h) p.property.symm⟩
  left_inv p := by
    rcases p with p | p <;> rcases p with ⟨⟨i, j⟩, hij⟩ <;> simp [hij, hij.not_gt]
  right_inv p := by
    rcases p with ⟨⟨i, j⟩, hij⟩
    by_cases h : i < j <;> simp [h]

/-- The directed formula agrees with one plaquette per vertex and pair i < j. -/
theorem action_eq_geometric {n : Sides} (U : Config n) :
    action U = ∑ x : Site n, ∑ p : Plane, (1 - halfTrace (transport U x p.val.1 p.val.2)) := by
  have count (x : Site n) :
      (∑ q : OrderedPlane, (1 - faceTrace U (x, q))) =
      (∑ p : Plane, (1 - halfTrace (transport U x p.val.1 p.val.2))) +
      (∑ p : Plane, (1 - halfTrace (transport U x p.val.1 p.val.2))) := by
    rw [← orientations.sum_comp (fun q => 1 - faceTrace U (x, q)), Fintype.sum_sum_type]
    refine congrArg₂ (· + ·) rfl (Finset.sum_congr rfl ?_)
    intro p _
    exact congrArg (1 - ·) (halfTrace_reverse U x p.val.1 p.val.2)
  simp only [action, Fintype.sum_prod_type, count, Finset.sum_add_distrib]
  ring


def density (β : ℝ) {n : Sides} (U : Config n) : ℝ := Real.exp (-β * action U)

def partition (β : ℝ) (n : Sides) : ℝ := ∫ U, density β U ∂haar n

theorem continuous_faceTrace {n : Sides} (p : Face n) :
    Continuous (fun U : Config n => faceTrace U p) := by
  unfold faceTrace transport
  apply continuous_halfTrace.comp
  fun_prop

theorem continuous_action (n : Sides) : Continuous (action (n := n)) := by
  exact (continuous_finsetSum _ (fun p _ => continuous_const.sub (continuous_faceTrace p))).div_const 2

theorem integrable_density (β : ℝ) (n : Sides) : Integrable (density β) (haar n) := by
  apply Continuous.integrable_of_hasCompactSupport _ (HasCompactSupport.of_compactSpace _)
  exact Real.continuous_exp.comp (continuous_const.mul (continuous_action n))

theorem partition_le_one {β : ℝ} (hβ : 0 ≤ β) (n : Sides) : partition β n ≤ 1 := by
  have h (U : Config n) : density β U ≤ 1 := by
    have hA : 0 ≤ action U := div_nonneg
      (Finset.sum_nonneg (fun p _ => sub_nonneg.mpr (halfTrace_le_one _))) (by norm_num)
    exact Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr hβ) hA)
  simpa [partition] using integral_mono (integrable_density β n)
    (integrable_const (1 : ℝ)) h

/-- Permuting coordinates of a site also permutes its cyclic factors. -/
def siteEquiv (n : Sides) (e : Equiv.Perm Dir) : Site (n ∘ e) ≃ Site n :=
  Equiv.piCongrLeft (fun i => Fin (n i)) e

def linkEquiv (n : Sides) (e : Equiv.Perm Dir) : Link (n ∘ e) ≃ Link n :=
  (siteEquiv n e).prodCongr e

def planeEquiv (e : Equiv.Perm Dir) : OrderedPlane ≃ OrderedPlane where
  toFun p := ⟨(e p.val.1, e p.val.2), e.injective.ne p.property⟩
  invFun p := ⟨(e.symm p.val.1, e.symm p.val.2), e.symm.injective.ne p.property⟩
  left_inv p := by simp
  right_inv p := by simp

def faceEquiv (n : Sides) (e : Equiv.Perm Dir) : Face (n ∘ e) ≃ Face n :=
  (siteEquiv n e).prodCongr (planeEquiv e)

/-- Pull a configuration back by the link bijection. -/
def relabel (n : Sides) (e : Equiv.Perm Dir) : Config n ≃ᵐ Config (n ∘ e) :=
  (MeasurableEquiv.piCongrLeft (fun _ => SU2) (linkEquiv n e)).symm

theorem measurePreserving_relabel (n : Sides) (e : Equiv.Perm Dir) :
    MeasurePreserving (relabel n e) (haar n) (haar (n ∘ e)) :=
  (measurePreserving_piCongrLeft (fun _ => linkHaar) (linkEquiv n e)).symm _

theorem siteEquiv_step (n : Sides) (e : Equiv.Perm Dir) (x : Site (n ∘ e)) (i : Dir) :
    siteEquiv n e (step x i) = step (siteEquiv n e x) (e i) := by
  funext k
  obtain ⟨j, rfl⟩ := e.surjective k
  simp only [siteEquiv, Equiv.piCongrLeft_apply_apply, step, Function.comp_apply,
    Equiv.apply_eq_iff_eq]

theorem faceTrace_relabel (n : Sides) (e : Equiv.Perm Dir) (U : Config n) (p : Face (n ∘ e)) :
    faceTrace (relabel n e U) p = faceTrace U (faceEquiv n e p) := by
  have pull (l : Link (n ∘ e)) : relabel n e U l = U (linkEquiv n e l) := rfl
  rcases p with ⟨x, ⟨⟨i, j⟩, hij⟩⟩
  simp [faceTrace, transport, faceEquiv, planeEquiv, pull, linkEquiv, siteEquiv_step]

theorem action_relabel (n : Sides) (e : Equiv.Perm Dir) (U : Config n) :
    action (relabel n e U) = action U := by
  simp only [action, faceTrace_relabel]
  rw [(faceEquiv n e).sum_comp (fun p => 1 - faceTrace U p)]

theorem partition_permute (β : ℝ) (n : Sides) (e : Equiv.Perm Dir) :
    partition β (n ∘ e) = partition β n := by
  rw [partition, ← (measurePreserving_relabel n e).integral_comp' (density β)]
  simp only [density, action_relabel, partition]


/-- A single Haar link changes the sign of a plaquette trace. The edge
opposite the chosen one starts at a different vertex whenever its side is ≥ 2. -/
theorem integral_faceTrace {n : Sides} (hn : ∀ i, 2 ≤ n i) (p : Face n) :
    ∫ U, faceTrace U p ∂haar n = 0 := by
  classical
  rcases p with ⟨x, ⟨⟨i, j⟩, hij⟩⟩
  have moved : step x j ≠ x := by
    intro h
    have hr : finRotate (n j) (x j) = x j := by simpa [step] using congrFun h j
    let : NeZero (n j) := ⟨by have := hn j; omega⟩
    rw [finRotate_apply] at hr
    have ho : (1 : Fin (n j)) = 0 := add_eq_left.mp hr
    have hv := congrArg Fin.val ho
    change 1 % n j = 0 at hv
    rw [Nat.mod_eq_of_lt (hn j)] at hv
    contradiction
  let flip : Config n := fun l => if l = (x, i) then centerMinus else 1
  apply integral_eq_zero_of_mul_left_eq_neg (g := flip)
  intro U
  simp [faceTrace, transport, flip, Pi.mul_apply, Prod.ext_iff, hij.symm, moved,
    mul_assoc, halfTrace_centerMinus]

/-- There are twelve ordered planes per site, each with expected trace zero. -/
theorem mean_action {n : Sides} (hn : ∀ i, 2 ≤ n i) :
    (∫ U : Config n, action U ∂haar n) = 6 * (Fintype.card (Site n) : ℝ) := by
  have hi (p : Face n) : Integrable (fun U : Config n => faceTrace U p) (haar n) :=
    (continuous_faceTrace p).integrable_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)
  have count : Fintype.card OrderedPlane = 12 := by decide +kernel
  have mean (p : Face n) : (∫ U, 1 - faceTrace U p ∂haar n) = 1 := by
    rw [integral_sub (integrable_const _) (hi p), integral_faceTrace hn p]
    simp
  unfold action
  rw [integral_div, integral_finsetSum Finset.univ
    (f := fun (p : Face n) (U : Config n) => 1 - faceTrace U p)
    (fun p _ => (integrable_const _).sub (hi p))]
  simp only [mean, Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
  change (Fintype.card (Site n × OrderedPlane) : ℝ) / 2 = _
  rw [Fintype.card_prod, count]
  push_cast
  ring

/-- Jensen for the actual product Haar probability. -/
theorem jensen (β : ℝ) (n : Sides) :
    Real.exp (-β * ∫ U : Config n, action U ∂haar n) ≤ partition β n := by
  have hc : Continuous (fun U : Config n => -β * action U) :=
    continuous_const.mul (continuous_action n)
  have h := convexOn_exp.map_integral_le (μ := haar n) (f := fun U => -β * action U)
    Real.continuous_exp.continuousOn isClosed_univ (Filter.Eventually.of_forall (fun _ => trivial))
    (hc.integrable_of_hasCompactSupport (HasCompactSupport.of_compactSpace _))
    (integrable_density β n)
  simpa only [integral_const_mul, partition, density] using h

theorem partition_pos (β : ℝ) (n : Sides) : 0 < partition β n :=
  (Real.exp_pos _).trans_le (jensen β n)

def sides (a : ℕ) (R : Box) : Sides := ![a, R.x, R.y, R.z]

/-- Time has length a. The first, second, and third spatial periods are R.x, R.y, R.z. -/
def Z (β : ℝ) (a : ℕ) (R : Box) : ℝ := partition β (sides a R)

theorem Z_bounds (β : ℝ) (hβ : 0 < β) (a : ℕ) (R : Box) :
    0 < Z β a R ∧ Z β a R ≤ 1 :=
  ⟨partition_pos _ _, partition_le_one hβ.le _⟩

/-- The pullback interchanges the specified spatial axis with time. -/
def exchange : Axis → Equiv.Perm Dir
  | .x => Equiv.swap 0 1
  | .y => Equiv.swap 0 2
  | .z => Equiv.swap 0 3

theorem cross (β : ℝ) (R : Box) (i : Axis) (a b : ℕ) :
    Z β a (R.replace i b) = Z β b (R.replace i a) := by
  have hs : sides b (R.replace i a) = sides a (R.replace i b) ∘ exchange i := by
    cases i <;> funext k <;> fin_cases k <;> rfl
  unfold Z
  rw [hs]
  exact (partition_permute _ _ _).symm

/-- Product of the two periods left fixed when axis i is exchanged with time. -/
def spectatorArea (R : Box) : Axis → ℝ
  | .x => (R.y : ℝ) * R.z
  | .y => (R.x : ℝ) * R.z
  | .z => (R.x : ℝ) * R.y

theorem log_lower (β : ℝ) (R : Box) (hR : R.Valid) (i : Axis) (a b : ℕ)
    (ha : 3 ≤ a) (hb : 3 ≤ b) :
    (-6 * β * spectatorArea R i) * a * b ≤ Real.log (Z β a (R.replace i b)) := by
  have hn : ∀ k, 2 ≤ sides a (R.replace i b) k := by
    obtain ⟨hx, hy, hz⟩ := hR
    intro k
    cases i <;> fin_cases k <;> simp [sides, Box.replace] <;> omega
  have h := Real.log_le_log (Real.exp_pos _) (jensen β (sides a (R.replace i b)))
  rw [Real.log_exp, mean_action hn] at h
  change _ ≤ Real.log (partition β (sides a (R.replace i b)))
  refine le_trans (le_of_eq ?_) h
  have card_site (n : Sides) : Fintype.card (Site n) = ∏ k, n k := by
    calc
      _ = ∏ k, Fintype.card (Fin (n k)) := Fintype.card_pi (α := fun k => Fin (n k))
      _ = _ := by simp
  rw [card_site]
  cases i <;> simp [sides, Box.replace, spectatorArea, Fin.prod_univ_succ] <;> ring

/-- The only model-dependent hypothesis here is the rectangular spectral trace identity
on valid periods. The conclusions have the types of TorusData.cross and TorusData.lower. -/
theorem fields_of_bridge (β : ℝ) (spectrum : Box → BoxSpectrum)
    (bridge : ∀ R : Box, R.Valid → ∀ a : ℕ, 3 ≤ a → (spectrum R).weight a = Z β a R) :
    (∀ R : Box, R.Valid → ∀ i a b, 3 ≤ a → 3 ≤ b →
      (spectrum (R.replace i b)).weight a = (spectrum (R.replace i a)).weight b) ∧
    (∀ R : Box, R.Valid → ∀ i, ∃ d : ℝ, ∀ a b : ℕ, 3 ≤ a → 3 ≤ b →
      d * a * b ≤ Real.log ((spectrum (R.replace i b)).weight a)) := by
  have valid (R : Box) (hR : R.Valid) (i : Axis) (b : ℕ) (hb : 3 ≤ b) :
      (R.replace i b).Valid := by cases i <;> simp_all [Box.Valid, Box.replace]
  constructor
  · intro R hR i a b ha hb
    rw [bridge _ (valid R hR i b hb) a ha, bridge _ (valid R hR i a ha) b hb]
    exact cross β R i a b
  · intro R hR i
    refine ⟨-6 * β * spectatorArea R i, ?_⟩
    intro a b ha hb
    rw [bridge _ (valid R hR i b hb) a ha]
    exact log_lower β R hR i a b ha hb


section Spectral

open Module.End
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- First part of the spectral bridge. In arbitrary dimension a compact symmetric
operator splits as the Hilbert direct sum of its full eigenspaces, including its kernel. -/
theorem compact_eigenblocks (T : H →L[ℂ] H) (hc : IsCompactOperator T) (hs : T.IsSymmetric) :
    IsHilbertSum ℂ (fun z : ℂ => eigenspace T.toLinearMap z)
      (fun z => (eigenspace T.toLinearMap z).subtypeₗᵢ) := by
  let (z : ℂ) : CompleteSpace (eigenspace T.toLinearMap z) := by
    have hset : (eigenspace T.toLinearMap z : Set H) = {v | T v = z • v} :=
      Set.ext fun _ => mem_eigenspace_iff
    have hclosed : IsClosed (eigenspace T.toLinearMap z : Set H) := by
      rw [hset]
      exact isClosed_eq T.continuous (continuous_const.smul continuous_id)
    exact hclosed.completeSpace_coe
  apply IsHilbertSum.mkInternal (fun z => eigenspace T.toLinearMap z) hs.orthogonalFamily_eigenspaces
  rw [← Submodule.orthogonal_orthogonal_eq_closure,
    ContinuousLinearMap.orthogonalComplement_iSup_eigenspaces_eq_bot hc hs]
  simp

/-- Each nonzero eigenvalue gets one slot per orthonormal basis vector of its block.
An absent nonzero scalar has zero slots. -/
theorem nonzero_eigenblock_basis (T : H →L[ℂ] H) (hc : IsCompactOperator T)
    (z : ℂ) (hz : z ≠ 0) :
    ∃ b : OrthonormalBasis (Fin (Module.finrank ℂ (eigenspace T.toLinearMap z))) ℂ
      (eigenspace T.toLinearMap z), ∀ k, T (b k : H) = z • (b k : H) := by
  let := ContinuousLinearMap.finite_dimensional_eigenspace hc z hz
  exact ⟨stdOrthonormalBasis ℂ _, fun k => mem_eigenspace_iff.mp (Subtype.property _)⟩

/-- A nonzero positive compact operator actually attains its positive spectral top. -/
theorem positive_top_eigenvalue [Nontrivial H] (T : H →L[ℂ] H) (hc : IsCompactOperator T)
    (hp : T.IsPositive) (hT : T ≠ 0) :
    0 < ‖T‖ ∧ HasEigenvalue T.toLinearMap (‖T‖ : ℂ) := by
  have hn := norm_pos_iff.mpr hT
  refine ⟨hn, (hc.hasEigenvalue_iff_mem_spectrum (by exact_mod_cast hn.ne')).mpr ?_⟩
  exact spectrum.algebraMap_mem ℂ (CStarAlgebra.norm_mem_spectrum_of_nonneg
    ((ContinuousLinearMap.nonneg_iff_isPositive _).mpr hp))

end Spectral

/-- The injection records multiplicity. Its distinguished index is counted by the
explicit 1 in the weight. Unused natural indices have zero ratio. -/
def EnumeratesRatios {I : Type*} (B : BoxSpectrum) (value : I → ℝ) (top : I) : Prop :=
  ∃ e : I ↪ ℕ, B.ratio (e top) = 0 ∧
    (∀ i, i ≠ top → B.ratio (e i) = value i / B.top) ∧
    ∀ j, j ∉ Set.range e → B.ratio j = 0

/-- Package a square-summable positive list with multiplicities. One specified maximal
slot is removed. Extending the remaining ratios by zero handles finite spectra too. -/
theorem boxSpectrum_of_slots {I : Type*} [Countable I] (value : I → ℝ) (top : I)
    (ht : 0 < value top) (hn : ∀ i, 0 ≤ value i) (hm : ∀ i, value i ≤ value top)
    (h₂ : Summable (fun i => value i ^ 2)) :
    ∃ B : BoxSpectrum, B.top = value top ∧ EnumeratesRatios B value top ∧
      ∀ a : ℕ, 3 ≤ a → B.weight a = ∑' i, value i ^ a := by
  classical
  obtain ⟨code, hcode⟩ := exists_injective_nat I
  let r (i : I) := value i / value top
  have hr0 (i) : 0 ≤ r i := div_nonneg (hn i) ht.le
  have hr1 (i) : r i ≤ 1 := (div_le_one ht).mpr (hm i)
  have hr₂ : Summable (fun i => r i ^ 2) := by
    simpa only [r, div_pow] using h₂.div_const (value top ^ 2)
  have hrs {a : ℕ} (ha : 2 ≤ a) : Summable (fun i => r i ^ a) :=
    Summable.of_nonneg_of_le (fun i => pow_nonneg (hr0 i) a)
      (fun i => pow_le_pow_of_le_one (hr0 i) (hr1 i) ha) hr₂
  let g (i : I) := if i = top then 0 else r i
  have hg (i) : 0 ≤ g i ∧ g i ≤ r i := by
    by_cases hi : i = top <;> simp [g, hi, hr0]
  let ratio : ℕ → ℝ := Function.extend code g 0
  have bounds (j : ℕ) : 0 ≤ ratio j ∧ ratio j ≤ 1 := by
    by_cases hj : ∃ i, code i = j
    · obtain ⟨i, rfl⟩ := hj
      rw [show ratio (code i) = g i from hcode.extend_apply _ _ i]
      exact ⟨(hg i).1, (hg i).2.trans (hr1 i)⟩
    · simp [ratio, Function.extend_apply' _ _ _ hj]
  have powers (a : ℕ) (ha : a ≠ 0) :
      (fun j => ratio j ^ a) = Function.extend code (fun i => g i ^ a) 0 := by
    funext j
    by_cases hj : ∃ i, code i = j
    · obtain ⟨i, rfl⟩ := hj
      simp [ratio, hcode.extend_apply]
    · simp [ratio, Function.extend_apply' _ _ _ hj, ha]
  have hg₃ : Summable (fun i => g i ^ 3) := Summable.of_nonneg_of_le
    (fun i => pow_nonneg (hg i).1 _) (fun i => pow_le_pow_left₀ (hg i).1 (hg i).2 _) (hrs (by decide))
  let B : BoxSpectrum := {
    top := value top, top_pos := ht, ratio := ratio,
    nonneg := fun j => (bounds j).1, le_one := fun j => (bounds j).2,
    atThree := by rw [powers 3 (by decide)]; exact (summable_extend_zero hcode).2 hg₃ }
  have enumerates : EnumeratesRatios B value top := by
    refine ⟨⟨code, hcode⟩, ?_, ?_, ?_⟩
    · change Function.extend code g 0 (code top) = 0
      simp [hcode.extend_apply, g]
    · intro i hi
      change Function.extend code g 0 (code i) = r i
      simp [hcode.extend_apply, g, hi]
    · intro j hj
      change Function.extend code g (0 : ℕ → ℝ) j = 0
      exact Function.extend_apply' g (0 : ℕ → ℝ) j hj
  refine ⟨B, rfl, enumerates, ?_⟩
  intro a ha
  have ha0 : a ≠ 0 := by omega
  have drop (i : I) : g i ^ a = if i = top then 0 else r i ^ a := by
    by_cases hi : i = top <;> simp [g, hi, ha0]
  have split := (hrs (a := a) (by omega)).tsum_eq_add_tsum_ite top
  have rt : r top = 1 := div_self ht.ne'
  change value top ^ a * (1 + ∑' j, ratio j ^ a) = _
  rw [show (∑' j, ratio j ^ a) = ∑' i, g i ^ a by rw [powers a ha0, tsum_extend_zero hcode]]
  simp_rw [drop]
  rw [rt, one_pow] at split
  rw [← split, ← tsum_mul_left]
  apply tsum_congr
  intro i
  dsimp only [r]
  rw [div_pow, mul_comm, div_mul_cancel₀ _ (pow_ne_zero _ ht.ne')]

section OperatorSlots

open Module.End
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- One slot for each basis direction in the eigenspace of each positive real number. -/
abbrev PositiveSlot (T : H →L[ℂ] H) :=
  (r : {r : ℝ // 0 < r}) × Fin (Module.finrank ℂ (eigenspace T.toLinearMap (r.val : ℂ)))

/-- Positive slots exhaust the nonzero point spectrum of a compact positive operator. -/
theorem nonzero_eigenvalue_has_slot (T : H →L[ℂ] H) (hc : IsCompactOperator T)
    (hp : T.IsPositive) {z : ℂ} (hz : z ≠ 0) (he : HasEigenvalue T.toLinearMap z) :
    ∃ i : PositiveSlot T, (i.1.val : ℂ) = z := by
  have hr : (z.re : ℂ) = z := Complex.conj_eq_iff_re.mp (hp.isSymmetric.conj_eigenvalue_eq_self he)
  have he' : HasEigenvalue T.toLinearMap (z.re : ℂ) := hr.symm ▸ he
  have hn : 0 ≤ z.re := eigenvalue_nonneg_of_nonneg he' hp.re_inner_nonneg_right
  have hpos : 0 < z.re := lt_of_le_of_ne hn (fun h => hz (by rw [← hr, ← h]; simp))
  let r : {r : ℝ // 0 < r} := ⟨z.re, hpos⟩
  let := ContinuousLinearMap.finite_dimensional_eigenspace hc (r.val : ℂ) (hr.symm ▸ hz)
  have : Nontrivial (eigenspace T.toLinearMap (r.val : ℂ)) :=
    Submodule.nontrivial_iff_ne_bot.mpr he'
  exact ⟨⟨r, ⟨0, Module.finrank_pos_iff.mpr inferInstance⟩⟩, hr⟩

/-- The spectral sum carries all positive multiplicities and exactly one distinguished top.
The separate Wilson input that remains is equality of this sum with the Haar cycle. -/
theorem boxSpectrum_of_operator [Nontrivial H] (T : H →L[ℂ] H) (hc : IsCompactOperator T)
    (hp : T.IsPositive) (hT : T ≠ 0) {δ : ℝ} (hhs : HSNormLE T δ) :
    ∃ B : BoxSpectrum, B.top = ‖T‖ ∧
      (∃ t : PositiveSlot T, t.1.val = ‖T‖ ∧ EnumeratesRatios B (fun i => i.1.val) t) ∧
      ∀ a : ℕ, 3 ≤ a → B.weight a = ∑' i : PositiveSlot T, i.1.val ^ a := by
  classical
  let z (r : {r : ℝ // 0 < r}) : ℂ := r.val
  have hz (r) : z r ≠ 0 := by
    change (r.val : ℂ) ≠ 0
    exact_mod_cast r.property.ne'
  let basis (r) := (nonzero_eigenblock_basis T hc (z r) (hz r)).choose
  let v (i : PositiveSlot T) : H := basis i.1 i.2
  have inj : Function.Injective z := fun _ _ h => Subtype.ext (Complex.ofReal_injective h)
  have on : Orthonormal ℂ v :=
    (hp.isSymmetric.orthogonalFamily_eigenspaces.comp inj).orthonormal_sigma_orthonormal
      (fun r => (basis r).orthonormal)
  have mass (i : PositiveSlot T) : ‖T (v i)‖ = i.1.val := by
    have he : T (v i) = z i.1 • v i := mem_eigenspace_iff.mp (basis i.1 i.2).property
    rw [he, norm_smul, on.1 i, mul_one]
    simp [z, Real.norm_eq_abs, i.1.property.le]
  have h₂ : Summable (fun i : PositiveSlot T => i.1.val ^ 2) := by
    apply summable_of_sum_le (c := δ ^ 2) (fun i => sq_nonneg _)
    intro s
    let e : Fin s.card ≃ s := s.equivFin.symm
    let f : Fin s.card → PositiveSlot T := fun i => (e i).val
    have hh := hhs _ (v ∘ f) (on.comp f (Subtype.val_injective.comp e.injective))
    calc
      ∑ i ∈ s, i.1.val ^ 2 = ∑ i : s, i.val.1.val ^ 2 := by
        rw [← Finset.sum_attach, Finset.attach_eq_univ]
      _ = ∑ k : Fin s.card, (f k).1.val ^ 2 := (e.sum_comp _).symm
      _ ≤ δ ^ 2 := by simpa only [Function.comp_apply, mass] using hh
  let : Countable (PositiveSlot T) := Set.countable_univ_iff.mp (by
    convert h₂.countable_support using 1
    ext i
    simp [Function.mem_support, i.1.property.ne'])
  obtain ⟨ht, htEig⟩ := positive_top_eigenvalue T hc hp hT
  let rt : {r : ℝ // 0 < r} := ⟨‖T‖, ht⟩
  let := ContinuousLinearMap.finite_dimensional_eigenspace hc (z rt) (hz rt)
  have : Nontrivial (eigenspace T.toLinearMap (z rt)) := Submodule.nontrivial_iff_ne_bot.mpr htEig
  let t : PositiveSlot T := ⟨rt, ⟨0, Module.finrank_pos_iff.mpr inferInstance⟩⟩
  have hmax (i : PositiveSlot T) : i.1.val ≤ ‖T‖ := by
    simpa only [mass, on.1 i, mul_one] using T.le_opNorm (v i)
  obtain ⟨B, htop, enumeration, weights⟩ := boxSpectrum_of_slots
    (fun i : PositiveSlot T => i.1.val) t ht (fun i => i.1.property.le) hmax h₂
  exact ⟨B, htop, ⟨t, rfl, enumeration⟩, weights⟩

end OperatorSlots


#print axioms continuous_halfTrace
#print axioms halfTrace_inv
#print axioms halfTrace_le_one
#print axioms halfTrace_centerMinus
#print axioms halfTrace_reverse
#print axioms action_eq_geometric
#print axioms continuous_faceTrace
#print axioms continuous_action
#print axioms integrable_density
#print axioms partition_le_one
#print axioms measurePreserving_relabel
#print axioms siteEquiv_step
#print axioms faceTrace_relabel
#print axioms action_relabel
#print axioms partition_permute
#print axioms integral_faceTrace
#print axioms mean_action
#print axioms jensen
#print axioms partition_pos
#print axioms Z_bounds
#print axioms cross
#print axioms log_lower
#print axioms fields_of_bridge
#print axioms compact_eigenblocks
#print axioms nonzero_eigenblock_basis
#print axioms positive_top_eigenvalue
#print axioms boxSpectrum_of_slots
#print axioms nonzero_eigenvalue_has_slot
#print axioms boxSpectrum_of_operator

end GapChain.Wilson
