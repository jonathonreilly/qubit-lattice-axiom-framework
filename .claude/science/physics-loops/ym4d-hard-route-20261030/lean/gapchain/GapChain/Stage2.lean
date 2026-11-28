import GapChain.Stage0

/-!
# Exponential clustering on the calibrated witnesses

We use the YM4 release of Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text. Rows 1457 and 1458 give the conditional argument and
its corrected odd-time grid. The scalar ratio lemma is from row 1459.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open Filter MeasureTheory
open scoped BigOperators ComplexConjugate InnerProductSpace NNReal Topology ContDiff
open YangMills YangMills.Construction
open SeparatedTuples ReflectionPositivity.TupleForm ReflectionPositivity.Reconstruction
open HilbertSpaceBasics LimitTheorem TheStatementsProvedTogether

namespace GapChain.Stage2

variable {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K} {S : CumulantFamily}

theorem gibbsAt (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    (j : ℕ) : ν j ∈ InfiniteLattice.periodicGibbsSet L (K j) (betaAt L M (K j) g₀) :=
  (torus_weak_limit_periodic_gibbs L (K j) hL (K j).pos _ (h.beta_pos j)).2 (h.isLimit j)

theorem faceMeanData (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) (j : ℕ) :
    (∀ r : InfiniteLattice.LatticeSymmetry _, InfiniteLattice.IsSymmetricUnder (ν j) r) ∧
    ∃ c : ℝ, (∀ p, ∫ U, InfiniteLattice.faceEnergy U p ∂ν j = c) ∧
      ∀ f ∈ ReflectionPositivity.continuousCompact, ∀ U : InfiniteLattice.GaugeField
        (PeriodicLattice.meshSize L (K j : ℤ)),
        InfiniteLattice.smearedEnergy f U - ∫ V, InfiniteLattice.smearedEnergy f V ∂ν j =
          ∑ᶠ p : InfiniteLattice.ElementaryPlaquette (PeriodicLattice.meshSize L (K j : ℤ)),
            f p.center * (InfiniteLattice.faceEnergy U p - c) :=
  (periodic_gibbs_lattice_approximation L hL).2.1 (K j) _ (h.beta_pos j)
    ⟨ν j, (gibbsAt hL h j).1.1⟩ (gibbsAt hL h j)

/-- Positive index `i` represents the original index `i.natPred`, including index zero. -/
def approximation (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) : LimitConventions.ApproxTriple L where
  cutoff i := K i.natPred
  tendsto_cutoff := QuaternionicWilsonModel.TopLimitsRealNonzero.tendsto_of_strictMono_pnat
    (h.strictMono.comp PNat.natPred_strictMono)
  state i := ν i.natPred
  isProbabilityMeasure_state i := (gibbsAt hL h i.natPred).1.1
  offset i := (faceMeanData hL h i.natPred).2.choose

abbrev mesh (L : ℕ) (K : ℕ → ℕ+) (j : ℕ) := PeriodicLattice.meshSize L (K j : ℤ)

theorem mesh_pos (hL : Conventions.IsAdmissibleBlockingFactor L) (j : ℕ) :
    0 < mesh L K j := by
  have hp : 0 < L := (by have := hL.2; omega)
  exact zpow_pos (by exact_mod_cast hp) _

theorem approximation_rp (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S) :
    (approximation hL h).IsReflPos := by
  intro i
  have hν := gibbsAt hL h i.natPred
  let : IsProbabilityMeasure (ν i.natPred) := hν.1.1
  have ha := mesh_pos (K := K) hL i.natPred
  obtain ⟨hs, hr⟩ := ReflectionPositivity.PeriodicGibbs.shiftInvariant_and_reflectionPositive
    periodic_gibbs_reflection_symmetries ha (h.beta_pos _) hν
  exact ⟨hs, fun _ hQ => ReflectionPositivity.PeriodicGibbs.reflectionPositive_of_allMirrors
    reflectionPositivity_formulations_equiv ha hr hQ⟩

/-- At every cutoff the face offset in the reconstructed triple centers in the named state. -/
theorem integral_tupleRep (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) (i : ℕ+) (X : SepTuple) :
    ((∫ U, (approximation hL h).tupleRep i X U ∂ν i.natPred : ℝ) : ℂ) =
      listMoment (ν i.natPred) X.val := by
  let A := approximation hL h
  have heq : (∫ U, A.tupleRep i X U ∂ν i.natPred) =
      ∫ U, InfiniteLattice.CutoffRepresentative.centredProduct L (K i.natPred)
        (ν i.natPred) (TupleLists.ofList X) U ∂ν i.natPred := by
    apply integral_congr_ae
    filter_upwards with U
    change (X.val.map fun f => A.smearedField i f U).prod = ∏ k : Fin X.val.length, _
    rw [← Fin.prod_univ_fun_getElem]
    apply Finset.prod_congr rfl
    intro k _
    have hf := X.2.1 _ (List.get_mem X.val k)
    exact ((faceMeanData hL h i.natPred).2.choose_spec.2 (X.val.get k)
      ⟨hf.1.continuous, hf.2⟩ U).symm
  change ((∫ U, A.tupleRep i X U ∂ν i.natPred : ℝ) : ℂ) = _
  rw [heq]
  exact (((limit_representative_identifications L hL _ _
    (fun k : ℕ+ => (gibbsAt hL h k.natPred).1.1) S).1 i).1 _ (TupleLists.ofList X).2).1

theorem approximation_converges (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) : (approximation hL h).ConvergesTo (centredOf S) := by
  intro X
  have hnat := h.moments _ (TupleLists.ofList X).2
  have hlim := (Complex.continuous_re.tendsto _).comp
    (hnat.comp InfiniteLattice.PeriodicExtensions.tendsto_pnatNatPred_atTop)
  apply hlim.congr
  intro i
  exact (congrArg Complex.re (integral_tupleRep hL h i X)).symm

/-- Tuple-form reconstruction with the original cutoff states and continuum cumulants. -/
theorem reconstruction (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S) :
    ∃ hσ : IsPosSemidef (reflectionForm (centredOf S)), HasReconstruction (centredOf S) hσ := by
  let D := WindowLimits.unitAxisMirrorData hL
  have hc := approximation_converges hL h
  have hb := (bounded_of_tendsto_on_tuples.1 D (approximation hL h)
    fun X => ⟨_, hc X⟩).2
  exact (limit_reconstruction D _ (centredOf S) hb (approximation_rp hL h) hc).2.2

section Correlations

open ReflectionPositivity.LatticeScalarProduct

/-- Linear extension of the centered moments at one cutoff. -/
def average {a : ℝ} (μ : Measure (InfiniteLattice.GaugeField a)) : FormalSpan →ₗ[ℂ] ℂ :=
  linearExtend fun X => listMoment μ X.val

def connectedValue (E : FormalSpan →ₗ[ℂ] ℂ) (Z : PositiveSpan) (t : ℝ) : ℝ :=
  (E (reflMulShift Z Z.val (t • timeBasisVec))).re - ‖E Z.val‖ ^ 2

theorem latticeU_eq {a : ℝ} (μ : Measure (InfiniteLattice.GaugeField a)) (Z : PositiveSpan)
    {t : ℝ} (ht : 0 ≤ t) : latticeU μ Z t = connectedValue (average μ) Z t := by
  classical
  obtain ⟨δ, hd, hz, _⟩ := exists_common_margin Z Z
  have hcomp := reflMulShiftComposable_of_nonneg hd hz hz
    (v := t • timeBasisVec) (by simpa only [timeComponent_smul_timeBasisVec] using ht)
  have hzsum : ∑ X ∈ Z.val.support, Z.val X • basisVec X = Z.val := by
    conv_rhs => rw [← Finsupp.sum_single Z.val]
    exact Finset.sum_congr rfl fun X _ => by simp [basisVec]
  have hexp : reflMulShift Z Z.val (t • timeBasisVec) =
      ∑ X ∈ Z.val.support, ∑ Y ∈ Z.val.support,
        (conj (Z.val X) * Z.val Y) • basisVec (SepTuple.juxt (push TimeAxis.timeReflection X)
          (push (translate (t • timeBasisVec)) Y)) := by
    unfold reflMulShift reflectConj
    have hp (r : InfiniteLattice.AmbientSpace → InfiniteLattice.AmbientSpace) (c : SepTuple → ℂ) :
        pushSpan r (∑ X ∈ Z.val.support, c X • basisVec X) =
          ∑ X ∈ Z.val.support, c X • basisVec (push r X) := by
      simp only [map_sum, map_smul, pushSpan_basisVec]
    conv_lhs => rw [← hzsum, conjugation_sum, hp, hp, formalMul_sum]
  have href := ConditionDefaults.push_val separatedTuples_basic.1
    (ConditionDefaults.isEuclidIsometry_timeReflection unit_normal_reflection_lattice_mirror)
  unfold connectedValue latticeU
  rw [hexp]
  simp only [map_sum, map_smul, average, linearExtend_basisVec, smul_eq_mul]
  congr 2
  exact Finset.sum_congr rfl fun X hX => Finset.sum_congr rfl fun Y hY => by
    rw [SepTuple.juxt_val (hcomp X hX Y hY), href, push_translate_val]

theorem average_tendsto (h : Inputs L M g₀ K ν S) (W : FormalSpan) :
    Tendsto (fun j => average (ν j) W) atTop (𝓝 ((centredOf S).spanExtension W)) := by
  simpa only [average, TupleFunctional.spanExtension, linearExtend, Finsupp.linearCombination_apply,
    Finsupp.sum, smul_eq_mul, listMoment, centredOf, TupleLists.ofList] using
      (tendsto_finsetSum W.support fun X _ =>
        (h.moments _ (TupleLists.ofList X).2).const_mul (W X))

theorem latticeU_tendsto (h : Inputs L M g₀ K ν S) (Z : PositiveSpan) {t : ℝ} (ht : 0 ≤ t) :
    Tendsto (fun j => latticeU (ν j) Z t) atTop
      (𝓝 (connectedValue (centredOf S).spanExtension Z t)) := by
  simp_rw [latticeU_eq _ Z ht]
  exact ((Complex.continuous_re.tendsto _).comp (average_tendsto h _)).sub
    ((average_tendsto h Z.val).norm.pow 2)

end Correlations

section OddMoments

open InfiniteLattice ReflectionPositivity.LatticeScalarProduct
open LatticeConventions.MirrorReconstructionProof (actOn_shift_zero shift_comp_shift)

def negativeMirror (a : ℝ) : halfSpacingTimes a := ⟨-a / 2, -1, by push_cast; ring⟩

def unitStep (a : ℝ) : positiveMultiples a := ⟨a, 1, by decide, by simp⟩

def oddTime (a : ℝ) (n : ℕ) : ℝ := (2 * (n : ℝ) + 1) * a

theorem translate_negativeMirror (a : LatticeConventions.Spacing) :
    (shift (timeStep (unitStep a))).comp (timeReflect (negativeMirror a)) =
      LatticeConventions.SiteFrame.timeReflection a := by
  apply LatticeConventions.MirrorReconstructionProof.latticeSymmetry_eq_of_toFun
  rw [siteTimeReflection_toFun_eq]
  funext x i
  change (((timeReflect (negativeMirror a)).toFun x + (timeStep (unitStep a) : AmbientSpace)) i) = _
  rw [timeReflect_apply]
  fin_cases i <;> simp [negativeMirror, timeStep, unitStep, TimeAxis.timeReflection,
    timeAxis]
  ring

theorem oddDisplacement (a : ℝ) (n : ℕ) :
    ((timeStep (unitStep a) + (2 * (n : ℤ)) • timeStep (unitStep a) : LatticePoint a) :
      AmbientSpace) = oddTime a n • timeBasisVec := by
  ext i
  change (Pi.single timeAxis a : AmbientSpace) i + (2 * (n : ℤ)) •
    (Pi.single timeAxis a : AmbientSpace) i = oddTime a n * timeBasisVec i
  by_cases hi : i = timeAxis
  · subst i
    simp [timeBasisVec, PeriodicLattice.coordVec, TimeAxis.timeIdx, timeAxis, oddTime, zsmul_eq_mul]
    ring
  · simp [timeBasisVec, PeriodicLattice.coordVec,
      TimeAxis.timeIdx, show i ≠ 3 from hi]

theorem integral_spanRep (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    (i : ℕ+) (W : FormalSpan) :
    ∫ U, (approximation hL h).spanRep i W U ∂ν i.natPred = average (ν i.natPred) W := by
  let A := approximation hL h
  let : IsProbabilityMeasure (A.state i) := A.isProbabilityMeasure_state i
  have hint (X : SepTuple) : Integrable (fun U => (A.tupleRep i X U : ℂ)) (A.state i) := by
    obtain ⟨hm, C, hC⟩ := (((representatives_covariant_local L hL A i).2.2.1 X).2.1).1
    exact Integrable.of_bound hm.aestronglyMeasurable C (ae_of_all _ hC)
  change (∫ U, A.spanRep i W U ∂A.state i) = average (ν i.natPred) W
  rw [spanRep_eq_sum]
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, average, linearExtend,
    Finsupp.linearCombination_apply, Finsupp.sum]
  rw [integral_finsetSum _ fun X _ => (hint X).const_mul _]
  refine Finset.sum_congr rfl fun X _ => ?_
  rw [integral_const_mul, integral_complex_ofReal]
  exact congrArg (fun z : ℂ => W X * z) (integral_tupleRep hL h i X)

theorem centered_pair_integral {α : Type*} [MeasurableSpace α] {μ : Measure α}
    [IsProbabilityMeasure μ] {F G : α → ℂ} {c : ℂ} (hF : Integrable F μ)
    (hG : Integrable G μ) (hFG : Integrable (fun x => conj (F x) * G x) μ)
    (hmeanF : ∫ x, F x ∂μ = c) (hmeanG : ∫ x, G x ∂μ = c) :
    ∫ x, conj (F x - c) * (G x - c) ∂μ =
      (∫ x, conj (F x) * G x ∂μ) - conj c * c := by
  have e (x : α) : conj (F x - c) * (G x - c) =
      (conj (F x) * G x - conj (F x) * c) - conj c * G x + conj c * c := by
    rw [map_sub]; ring
  have hconj : Integrable (fun x => conj (F x)) μ :=
    (@RCLike.conjLIE ℂ _).integrable_comp_iff.mpr hF
  have h₁ : Integrable (fun x => conj (F x) * G x - conj (F x) * c) μ :=
    hFG.sub (hconj.mul_const c)
  have h₂ : Integrable (fun x => conj (F x) * G x - conj (F x) * c - conj c * G x) μ :=
    h₁.sub (hG.const_mul (conj c))
  simp_rw [e]
  rw [integral_add h₂ (integrable_const (conj c * c)),
    integral_sub h₁ (hG.const_mul (conj c)),
    integral_sub hFG (hconj.mul_const c), integral_mul_const, integral_const_mul,
    integral_conj, hmeanF, hmeanG, integral_const]
  simp

theorem oneInsertion_iterate {a : ℝ} {μ : Measure (GaugeField a)} (A : GaugeField a → ℂ)
    (hc : ReflectionMomentsLogConvex μ (negativeMirror a) (unitStep a) (fun _ => 1) A)
    (n : ℕ) :
    (insertedTransfer (negativeMirror a) (unitStep a) (fun _ => 1))^[n] A =
      (shift ((2 * (n : ℤ)) • timeStep (unitStep a))).actOn A := by
  rcases n with _ | n
  · simp [actOn_shift_zero]
  · rw [(hc.2.2.2 _ (Nat.succ_pos n)).2.2]
    have h1 (i : ℕ) : insertSeq (negativeMirror a) (unitStep a) (fun _ => 1) i = 1 := by
      funext U
      by_cases hi : Odd i <;> simp [insertSeq, hi, reflectedInsert, LatticeSymmetry.actOn]
    simp [h1]

/-- The centered representative at the link mirror one half-spacing below the origin. -/
def linkTest (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    (j : ℕ) (Z : PositiveSpan) : GaugeField (mesh L K j) → ℂ := fun U =>
  (approximation hL h).spanRep j.succPNat Z.val U - average (ν j) Z.val

theorem linkTest_mem (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    (j : ℕ) (Z : PositiveSpan) {δ : ℝ} (hδ : mesh L K j ≤ δ) (hz : SupportedAbove δ Z.val) :
    linkTest hL h j Z ∈ upperAlgebra (negativeMirror (mesh L K j)) ∧
      IsBoundedObservable ((approximation hL h).spanRep j.succPNat Z.val) := by
  let a := mesh L K j
  let A := approximation hL h
  let B := A.spanRep j.succPNat Z.val
  have hB := spanRep_mem_upperSpace (WindowLimits.unitAxisMirrorData hL) A
    ((representatives_covariant_local L hL A j.succPNat).2.2.1) hδ hz
  rw [← SetLike.mem_coe, LatticeConventions.SiteFrame.coe_upperSpace] at hB
  rcases Set.mem_iUnion₂.mp hB with ⟨Q, hQ, hobs, hmeas⟩
  have ha := mesh_pos (K := K) hL j
  change Bornology.IsBounded Q at hQ
  refine ⟨⟨⟨hobs.1.sub measurable_const, ?_⟩, {x : AmbientSpace | 0 ≤ x timeAxis} ∩ Q, ?_,
    hQ.subset Set.inter_subset_right,
    hmeas.sub measurable_const⟩, hobs⟩
  · obtain ⟨C, hC⟩ := hobs.2
    exact ⟨C + ‖average (ν j) Z.val‖, fun U => (norm_sub_le _ _).trans (add_le_add (hC U) le_rfl)⟩
  · intro x hx
    change -(mesh L K j) / 2 < x timeAxis
    have hx0 : 0 ≤ x timeAxis := hx.1
    linarith

theorem linkMoments (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) (j : ℕ) (Z : PositiveSpan)
    (hA : linkTest hL h j Z ∈ upperAlgebra (negativeMirror (mesh L K j))) :
    ReflectionMomentsLogConvex (ν j) (negativeMirror (mesh L K j)) (unitStep (mesh L K j))
      (fun _ => 1) (linkTest hL h j Z) := by
  let D : ReflectionPositivity.AxisMirror.MirrorData :=
    { L := L, isAdmissible := hL, K := K j, m := 1, β := _, β_pos := h.beta_pos j }
  have h1 : IsSlabLocalized (negativeMirror D.mesh) (unitStep D.mesh)
      (fun _ : GaugeField D.mesh => (1 : ℂ)) :=
    ⟨⟨measurable_const, 1, by simp⟩, ∅, Set.empty_subset _, Bornology.isBounded_empty, measurable_const⟩
  have hp := (periodic_gibbs_reflection_transfer D (ν j) (gibbsAt hL h j) (negativeMirror D.mesh)).2.2.2
  exact (hp (unitStep D.mesh) _ h1).2 _ hA

/-- Centering both factors in a symmetric state subtracts the squared mean. -/
theorem centered_reflectionMoment {a : ℝ} {μ : Measure (GaugeField a)} [IsProbabilityMeasure μ]
    {B : GaugeField a → ℂ} (hb : IsBoundedObservable B) {c : ℂ} (hmean : ∫ U, B U ∂μ = c)
    (hinv : ∀ r, IsSymmetricUnder μ r)
    (hc : ReflectionMomentsLogConvex μ (negativeMirror a) (unitStep a) (fun _ => 1)
      (fun U => B U - c)) (n : ℕ) :
    reflectionMoment μ (negativeMirror a) (unitStep a) (fun _ => 1) (fun U => B U - c) n =
      (∫ U, conj ((timeReflect (negativeMirror a)).actOn B U) *
        (shift ((2 * (n : ℤ)) • timeStep (unitStep a))).actOn B U ∂μ) - conj c * c := by
  let θ := timeReflect (negativeMirror a)
  let s := shift ((2 * (n : ℤ)) • timeStep (unitStep a))
  have hF := ReflectionPairingProof.isBoundedObservable_actOn θ hb
  have hG := ReflectionPairingProof.isBoundedObservable_actOn s hb
  have hpair := ReflectionPairingProof.isBoundedObservable_mul
    (ReflectionPairingProof.isBoundedObservable_conj hF) hG
  have hint {F : GaugeField a → ℂ} (hf : IsBoundedObservable F) : Integrable F μ :=
    Integrable.of_bound hf.1.aestronglyMeasurable hf.2.choose (ae_of_all _ hf.2.choose_spec)
  rw [reflectionMoment, oneInsertion_iterate _ hc]
  exact centered_pair_integral (F := θ.actOn B) (G := s.actOn B)
    (hint hF) (hint hG) (hint hpair) ((hinv θ B hb).trans hmean) ((hinv s B hb).trans hmean)

/-- A common symmetry in a symmetric state preserves the reflected two-point integral. -/
theorem translated_pair {a : ℝ} {μ : Measure (GaugeField a)} (r θ s : LatticeSymmetry a)
    {B : GaugeField a → ℂ} (hb : IsBoundedObservable B) (hinv : IsSymmetricUnder μ r) :
    (∫ U, conj ((r.comp θ).actOn B U) * (r.comp s).actOn B U ∂μ) =
      ∫ U, conj (θ.actOn B U) * s.actOn B U ∂μ := by
  have hF := ReflectionPairingProof.isBoundedObservable_actOn θ hb
  have hG := ReflectionPairingProof.isBoundedObservable_actOn s hb
  have hpair := ReflectionPairingProof.isBoundedObservable_mul
    (ReflectionPairingProof.isBoundedObservable_conj hF) hG
  rw [SmearedEnergyAndSymmetryAction.actOn_comp_holds r θ B hb,
    SmearedEnergyAndSymmetryAction.actOn_comp_holds r s B hb]
  exact hinv _ hpair

/-- Translating both factors by one step produces the odd separation `(2n+1)a`. -/
theorem oddMoment_eq (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    (j : ℕ) (Z : PositiveSpan) {δ : ℝ} (hd : 0 < δ) (hz : SupportedAbove δ Z.val)
    (haδ : mesh L K j ≤ δ) (n : ℕ) :
    (reflectionMoment (ν j) (negativeMirror (mesh L K j)) (unitStep (mesh L K j))
      (fun _ => 1) (linkTest hL h j Z) n).re = latticeU (ν j) Z (oddTime (mesh L K j) n) := by
  let a := mesh L K j
  let A := approximation hL h
  let D := WindowLimits.unitAxisMirrorData hL
  let i := j.succPNat
  let B : GaugeField a → ℂ := A.spanRep i Z.val
  let c := average (ν j) Z.val
  let e := timeStep (unitStep a)
  let r := shift e
  let θ := timeReflect (negativeMirror a)
  let s := shift ((2 * (n : ℤ)) • e)
  let v := e + (2 * (n : ℤ)) • e
  let t := oddTime a n
  let : IsProbabilityMeasure (ν j) := (gibbsAt hL h j).1.1
  have ha := mesh_pos (K := K) hL j
  have ht : 0 ≤ t := mul_nonneg (by positivity) ha.le
  have hv : (v : AmbientSpace) = t • timeBasisVec := oddDisplacement a n
  obtain ⟨hupper, hb⟩ := linkTest_mem hL h j Z haδ hz
  have hinv := (faceMeanData hL h j).1
  have hctr := centered_reflectionMoment (μ := ν j) (B := B) (c := c) hb
    (integral_spanRep hL h i Z.val) hinv (linkMoments hL h j Z hupper) n
  have htrans := translated_pair (μ := ν j) r θ s (B := B) hb (hinv r)
  have hgeo : r.comp θ = LatticeConventions.SiteFrame.timeReflection (meshAt D A i) :=
    translate_negativeMirror (meshAt D A i)
  have hshift : r.comp s = shift v := shift_comp_shift e ((2 * (n : ℤ)) • e)
  rw [hgeo, hshift] at htrans
  have hcomp : ReflMulShiftComposable Z.val Z.val (v : AmbientSpace) := by
    rw [hv]
    exact reflMulShiftComposable_of_nonneg hd hz hz (by simpa only [timeComponent_smul_timeBasisVec] using ht)
  have hrep := conjReflMulShift_eq_spanRep D A
    ((representatives_covariant_local L hL A i).2.1) (Z := Z) (W := Z) (v := (v : AmbientSpace)) v.2 hcomp
  have hmem : (v : AmbientSpace) ∈ latticeSubgroup (meshAt D A i : ℝ) := v.2
  rw [conjReflMulShift, dif_pos hmem] at hrep
  have hraw : (∫ U, conj (θ.actOn B U) * s.actOn B U ∂ν j) =
      average (ν j) (reflMulShift Z Z.val (t • timeBasisVec)) := by
    refine htrans.symm.trans ?_
    calc
      _ = ∫ U, A.spanRep i (reflMulShift Z Z.val (v : AmbientSpace)) U ∂ν j :=
        integral_congr_ae (ae_of_all _ (congrFun hrep))
      _ = average (ν j) (reflMulShift Z Z.val (v : AmbientSpace)) := integral_spanRep hL h i _
      _ = _ := by rw [hv]
  change reflectionMoment (ν j) (negativeMirror a) (unitStep a) (fun _ => 1)
    (fun U => B U - c) n = _ at hctr
  change (reflectionMoment (ν j) (negativeMirror a) (unitStep a) (fun _ => 1)
    (fun U => B U - c) n).re = latticeU (ν j) Z t
  rw [hctr, latticeU_eq _ Z ht]
  change ((∫ U, conj (θ.actOn B U) * s.actOn B U ∂ν j) - conj c * c).re =
    (average (ν j) (reflMulShift Z Z.val (t • timeBasisVec))).re - ‖c‖ ^ 2
  rw [hraw, Complex.sub_re, ← Complex.normSq_eq_conj_mul_self, Complex.ofReal_re,
    Complex.normSq_eq_norm_sq]

end OddMoments


section Bounds

open ReflectionPositivity.LatticeScalarProduct

/-- Iterating the scalar ratio removes the prefactor even when it varies with the cutoff. -/
theorem oddGrid_ratio {f : ℕ → ℝ} {a m C : ℝ}
    (hp : ∀ n, 0 ≤ f n) (hlc : ∀ n, f (n + 1) ^ 2 ≤ f n * f (n + 2))
    (he : ∀ n, f n ≤ C * Real.exp (-m * oddTime a n)) (s d : ℕ) :
    f (s + d) ≤ Real.exp (-m * (oddTime a (s + d) - oddTime a s)) * f s := by
  let q := Real.exp (-m * (2 * a))
  have hq : 0 ≤ q := (Real.exp_pos _).le
  have henv (n : ℕ) : f n ≤ (C * Real.exp (-m * a)) * q ^ n := by
    refine (he n).trans_eq ?_
    rw [mul_assoc, ← Real.exp_nat_mul, ← Real.exp_add]
    congr 2
    unfold oddTime
    ring
  have hiter : f (s + d) ≤ q ^ d * f s := by
    induction d with
    | zero => simp
    | succ d ih =>
      calc
        f (s + d + 1) ≤ q * f (s + d) := sequenceLemma_of_bound hq hp hlc henv _
        _ ≤ q * (q ^ d * f s) := mul_le_mul_of_nonneg_left ih hq
        _ = q ^ (d + 1) * f s := by ring
  refine hiter.trans_eq ?_
  dsimp [q]
  rw [← Real.exp_nat_mul]
  congr 2
  simp only [oddTime, Nat.cast_add]
  ring

theorem cutoff_ratio (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    (j : ℕ) (Z : PositiveSpan) {δ m C : ℝ} (hd : 0 < δ) (hz : SupportedAbove δ Z.val)
    (haδ : mesh L K j ≤ δ) (he : ∀ n, latticeU (ν j) Z (oddTime (mesh L K j) n) ≤
      C * Real.exp (-m * oddTime (mesh L K j) n)) (s d : ℕ) :
    latticeU (ν j) Z (oddTime (mesh L K j) (s + d)) ≤
      Real.exp (-m * (oddTime (mesh L K j) (s + d) - oddTime (mesh L K j) s)) *
        latticeU (ν j) Z (oddTime (mesh L K j) s) := by
  have hid := oddMoment_eq hL h j Z hd hz haδ
  have hm := linkMoments hL h j Z (linkTest_mem hL h j Z haδ hz).1
  apply oddGrid_ratio (f := fun n => latticeU (ν j) Z (oddTime (mesh L K j) n)) _ _ he
  · exact fun n => (hm.1 n).2.trans_eq (hid n)
  · intro n
    simp only [← hid]
    simpa using (hm.2.2.2 (n + 1) (Nat.succ_pos n)).1

abbrev scale (L k : ℕ) : ℝ := PeriodicLattice.meshSize L (k : ℤ)

theorem scale_tendsto_zero (hL : Conventions.IsAdmissibleBlockingFactor L) :
    Tendsto (scale L) atTop (𝓝 0) := by
  have hl : 1 < (L : ℝ) := by exact_mod_cast (show 1 < L by have := hL.2; omega)
  change Tendsto (fun k : ℕ => (L : ℝ) ^ (-(k : ℤ))) atTop (𝓝 0)
  simpa only [zpow_neg, zpow_natCast, inv_pow] using
    (tendsto_pow_atTop_nhds_zero_of_lt_one (inv_nonneg.mpr (lt_trans zero_lt_one hl).le)
      (inv_lt_one_of_one_lt₀ hl))

/-- The first coarse odd time and any later coarse odd time are odd at each finer level. -/
theorem refine_odd_times (hL : Conventions.IsAdmissibleBlockingFactor L) {k p : ℕ}
    (hkp : k ≤ p) (n : ℕ) : ∃ r d : ℕ, scale L k = oddTime (scale L p) r ∧
      oddTime (scale L k) n = oddTime (scale L p) (r + d) := by
  obtain ⟨b, rfl⟩ := Nat.exists_eq_add_of_le hkp
  obtain ⟨r, hr⟩ := hL.1.pow (n := b)
  have hr' : (L : ℝ) ^ b = 2 * (r : ℝ) + 1 := by exact_mod_cast hr
  have hl : (L : ℝ) ≠ 0 := by exact_mod_cast (show L ≠ 0 by have := hL.2; omega)
  have he : (L : ℝ) ^ b * scale L (k + b) = scale L k := by
    simp only [scale, PeriodicLattice.meshSize, zpow_neg, zpow_natCast, pow_add]
    field_simp
  refine ⟨r, n * L ^ b, ?_, ?_⟩
  · simpa only [oddTime, ← hr'] using he.symm
  · unfold oddTime
    push_cast
    calc
      _ = (2 * (n : ℝ) + 1) * ((L : ℝ) ^ b * scale L (k + b)) := by rw [he]
      _ = _ := by rw [hr']; ring

theorem continuum_grid_bound (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hc : ExpClusters L K ν m) (Z : PositiveSpan)
    (k n : ℕ) :
    connectedValue (centredOf S).spanExtension Z (oddTime (scale L k) n) ≤
      Real.exp (-m * (oddTime (scale L k) n - scale L k)) *
        connectedValue (centredOf S).spanExtension Z (scale L k) := by
  obtain ⟨δ, hd, hz, _⟩ := exists_common_margin Z Z
  have hmono : StrictMono fun j => (K j : ℕ) := fun _ _ hij => h.strictMono hij
  have hsmall : ∀ᶠ j in atTop, mesh L K j ≤ δ :=
    ((scale_tendsto_zero hL).comp hmono.tendsto_atTop).eventually_le_const hd
  have hlate := hmono.tendsto_atTop (eventually_ge_atTop k)
  have hpos : 0 < scale L k := zpow_pos
    (by exact_mod_cast (show 0 < L by have := hL.2; omega)) _
  apply le_of_tendsto_of_tendsto_of_frequently (latticeU_tendsto h Z
    (mul_nonneg (by positivity) hpos.le)) ((latticeU_tendsto h Z hpos.le).const_mul _)
  refine (((hc Z).and_eventually (hsmall.and hlate))).mono ?_
  rintro j ⟨⟨C, he⟩, ha, hk⟩
  obtain ⟨r, d, hr, ht⟩ := refine_odd_times hL hk n
  change latticeU (ν j) Z (oddTime (scale L k) n) ≤
    Real.exp (-m * (oddTime (scale L k) n - scale L k)) * latticeU (ν j) Z (scale L k)
  rw [ht, hr]
  exact cutoff_ratio hL h j Z hd hz ha he r d

/-- Odd mesh midpoints approximate every nonnegative time with error at most one spacing. -/
theorem oddTime_floor_dist {a t : ℝ} (ha : 0 < a) (ht : 0 ≤ t) :
    dist (oddTime a ⌊t / (2 * a)⌋₊) t ≤ a := by
  have hp : 0 < 2 * a := by positivity
  have h₁ := (le_div_iff₀ hp).mp (Nat.floor_le (div_nonneg ht hp.le))
  have h₂ := (div_lt_iff₀ hp).mp (Nat.lt_floor_add_one (t / (2 * a)))
  rw [Real.dist_eq, abs_le]
  unfold oddTime
  constructor <;> nlinarith

/-- Continuity extends the coarse-grid ratios while their left endpoints tend to zero. -/
theorem bound_all_times (hL : Conventions.IsAdmissibleBlockingFactor L) {u : ℝ → ℝ}
    (hu : Continuous u) (m : ℝ) (hgrid : ∀ k n, u (oddTime (scale L k) n) ≤
      Real.exp (-m * (oddTime (scale L k) n - scale L k)) * u (scale L k))
    {t : ℝ} (ht : 0 ≤ t) : u t ≤ Real.exp (-m * t) * u 0 := by
  let n (k : ℕ) := ⌊t / (2 * scale L k)⌋₊
  let τ (k : ℕ) := oddTime (scale L k) (n k)
  have hd := scale_tendsto_zero hL
  have hτ : Tendsto τ atTop (𝓝 t) := by
    apply tendsto_iff_dist_tendsto_zero.2
    exact squeeze_zero (fun _ => dist_nonneg) (fun k => oddTime_floor_dist
      (zpow_pos (by exact_mod_cast (show 0 < L by have := hL.2; omega)) _) ht) hd
  have hrate := (Real.continuous_exp.tendsto _).comp
    ((hτ.sub hd).const_mul (-m))
  have hle := le_of_tendsto_of_tendsto' ((hu.tendsto _).comp hτ)
    (hrate.mul ((hu.tendsto _).comp hd)) (fun k => hgrid k (n k))
  simpa only [sub_zero] using hle

end Bounds


section Completion

variable {σ : TupleFunctional} {hσ : IsPosSemidef (reflectionForm σ)}

theorem vacuum_mean (hr : HasReconstruction σ hσ) (Z : PositiveSpan) :
    ⟪vacuum σ hσ, posClass σ hσ Z⟫_ℂ = σ.spanExtension Z.val := by
  rcases Z with ⟨W, hW⟩
  induction hW using Submodule.span_induction with
  | mem W hW =>
    obtain ⟨X, rfl⟩ := hW
    change ⟪vacuum σ hσ, posClass σ hσ (posTupleVec X)⟫_ℂ = σ.spanExtension (basisVec X.val)
    rw [(hr.1.2.2 X).2]
    simp [TupleFunctional.spanExtension, linearExtend_basisVec]
  | zero =>
    change ⟪vacuum σ hσ, posClass σ hσ 0⟫_ℂ = σ.spanExtension 0
    simp
  | add X Y hx hy ihx ihy =>
    change ⟪vacuum σ hσ, posClass σ hσ (⟨X, hx⟩ + ⟨Y, hy⟩)⟫_ℂ = σ.spanExtension (X + Y)
    rw [map_add, inner_add_right, ihx, ihy, map_add]
  | smul c X hx ih =>
    change ⟪vacuum σ hσ, posClass σ hσ (c • ⟨X, hx⟩)⟫_ℂ = σ.spanExtension (c • X)
    rw [map_smul, inner_smul_right, ih, map_smul, smul_eq_mul]

/-- A continuous extension in real time, used on the nonnegative half-line. -/
def osCovariance (σ : TupleFunctional) (hσ : IsPosSemidef (reflectionForm σ))
    (v : PhysicalSpace σ hσ) (t : ℝ) : ℝ :=
  (⟪v, timeShift σ hσ t.toNNReal v⟫_ℂ).re - ‖⟪vacuum σ hσ, v⟫_ℂ‖ ^ 2

theorem osCovariance_continuous (hr : HasReconstruction σ hσ) (v : PhysicalSpace σ hσ) :
    Continuous (osCovariance σ hσ v) := by
  have ht := (hr.2.1.2.2.1 v).comp (show Continuous Real.toNNReal by fun_prop)
  exact (Complex.continuous_re.comp (continuous_const.inner ht)).sub continuous_const

theorem osCovariance_posClass (hr : HasReconstruction σ hσ) (Z : PositiveSpan)
    {t : ℝ} (ht : 0 ≤ t) :
    osCovariance σ hσ (posClass σ hσ Z) t = connectedValue σ.spanExtension Z t := by
  have hm := hr.2.2.2 Z Z t.toNNReal 0
  have hz : embedSpatial 0 = 0 := by ext i; fin_cases i <;> rfl
  rw [hr.2.2.1.2.2.2.1.map_zero, one_apply_eq_self, hz, add_zero,
    Real.coe_toNNReal _ ht] at hm
  unfold osCovariance connectedValue
  rw [vacuum_mean hr Z, hm]
  rfl

/-- The centered estimate survives completion by continuity in the vector at both times. -/
theorem completed_covariance_bound (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hc : ExpClusters L K ν m)
    {hp : IsPosSemidef (reflectionForm (centredOf S))} (hr : HasReconstruction (centredOf S) hp)
    (v : PhysicalSpace (centredOf S) hp) (t : ℝ≥0) :
    osCovariance (centredOf S) hp v t ≤ Real.exp (-m * (t : ℝ)) *
      osCovariance (centredOf S) hp v 0 := by
  have hd : DenseRange (posClass (centredOf S) hp) :=
    ReflectionPositivity.ReconstructionComplements.dense_range_posClass
      hilbertSpace_basic_facts.2.2.2.2.2.1
  apply hd.induction_on (p := fun w => osCovariance (centredOf S) hp w t ≤
    Real.exp (-m * (t : ℝ)) * osCovariance (centredOf S) hp w 0) v
  · unfold osCovariance
    exact isClosed_le (by fun_prop) (by fun_prop)
  · intro Z
    apply bound_all_times hL (osCovariance_continuous hr _) m _ t.2
    intro k n
    have ha : 0 < scale L k := zpow_pos
      (by exact_mod_cast (show 0 < L by have := hL.2; omega)) _
    rw [osCovariance_posClass hr Z (t := oddTime (scale L k) n) (mul_nonneg (by positivity) ha.le),
      osCovariance_posClass hr Z ha.le]
    exact continuum_grid_bound hL h hc Z k n

-- The public signature keeps the positive-rate hypothesis used by the corollary.
set_option linter.unusedVariables false in
/-- On the completed OS space, exponential clustering gives the same physical decay rate. -/
theorem massGap_of_expClusters (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hm : 0 < m) (hc : ExpClusters L K ν m) :
    HasMassGap (centredOf S) m := by
  obtain ⟨hp, hr⟩ := reconstruction hL h
  refine ⟨hp, hr, fun v hv t => ?_⟩
  let T := timeShift (centredOf S) hp
  have sg := hr.2.1.2.2.2.1
  have hs := ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mp
    (hr.2.1.2.2.2.2.1 t).1
  have hdouble : (⟪v, T (t + t) v⟫_ℂ).re = ‖T t v‖ ^ 2 := by
    rw [show T (t + t) = T t * T t from sg.map_add t t]
    change (⟪v, T t (T t v)⟫_ℂ).re = _
    exact (congrArg Complex.re (hs v (T t v)).symm).trans
      (inner_self_eq_norm_sq (𝕜 := ℂ) (T t v))
  have hb := completed_covariance_bound hL h hc hr v (t + t)
  simp only [osCovariance, Real.toNNReal_coe, Real.toNNReal_zero, hv, norm_zero, ne_eq,
    OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, sub_zero, sg.map_zero,
    one_apply_eq_self] at hb
  rw [hdouble, show (⟪v, v⟫_ℂ).re = ‖v‖ ^ 2 from inner_self_eq_norm_sq (𝕜 := ℂ) v] at hb
  apply (sq_le_sq₀ (norm_nonneg _) (mul_nonneg (Real.exp_pos _).le (norm_nonneg _))).mp
  simp only [NNReal.coe_add, mul_add, Real.exp_add] at hb
  refine hb.trans_eq ?_
  ring

-- The expected type is inferred from the imported declaration, including all implicit binders.
example : type_of% @GapChain.massGap_of_expClusters := @massGap_of_expClusters

theorem uniqueVacuum_of_expClusters (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hm : 0 < m) (hc : ExpClusters L K ν m) :
    HasUniqueVacuum (centredOf S) :=
  (massGap_of_expClusters hL h hm hc).uniqueVacuum hm

end Completion


end GapChain.Stage2

#print axioms GapChain.Stage2.gibbsAt
#print axioms GapChain.Stage2.faceMeanData
#print axioms GapChain.Stage2.mesh_pos
#print axioms GapChain.Stage2.approximation_rp
#print axioms GapChain.Stage2.integral_tupleRep
#print axioms GapChain.Stage2.approximation_converges
#print axioms GapChain.Stage2.reconstruction
#print axioms GapChain.Stage2.latticeU_eq
#print axioms GapChain.Stage2.average_tendsto
#print axioms GapChain.Stage2.latticeU_tendsto
#print axioms GapChain.Stage2.translate_negativeMirror
#print axioms GapChain.Stage2.oddDisplacement
#print axioms GapChain.Stage2.integral_spanRep
#print axioms GapChain.Stage2.centered_pair_integral
#print axioms GapChain.Stage2.oneInsertion_iterate
#print axioms GapChain.Stage2.linkTest_mem
#print axioms GapChain.Stage2.linkMoments
#print axioms GapChain.Stage2.centered_reflectionMoment
#print axioms GapChain.Stage2.translated_pair
#print axioms GapChain.Stage2.oddMoment_eq
#print axioms GapChain.Stage2.oddGrid_ratio
#print axioms GapChain.Stage2.cutoff_ratio
#print axioms GapChain.Stage2.scale_tendsto_zero
#print axioms GapChain.Stage2.refine_odd_times
#print axioms GapChain.Stage2.continuum_grid_bound
#print axioms GapChain.Stage2.oddTime_floor_dist
#print axioms GapChain.Stage2.bound_all_times
#print axioms GapChain.Stage2.vacuum_mean
#print axioms GapChain.Stage2.osCovariance_continuous
#print axioms GapChain.Stage2.osCovariance_posClass
#print axioms GapChain.Stage2.completed_covariance_bound
#print axioms GapChain.Stage2.massGap_of_expClusters
#print axioms GapChain.Stage2.uniqueVacuum_of_expClusters
