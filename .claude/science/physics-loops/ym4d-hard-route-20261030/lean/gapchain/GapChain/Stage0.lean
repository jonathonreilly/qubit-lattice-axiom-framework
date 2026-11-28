import GapChain.SequenceLemma
import GapChain.LemmaM1
import GapChain.TheoremS
import GapChain.Wilson
import YangMills.Construction.TransferOperators.FactsOfTheOperatorsOfACubicTorus
import Formulation.FixedObservableContinuum

/-!
# Conditional gap of the calibrated action-density hierarchy

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
supply the Wilson transfer, lattice moments, continuum witnesses and reconstruction
in the YM4 Lean release at `3932084a9b82`. The conditional chain follows FINISH
row 1457, §§4.1–4.5, with the corrections of row 1458. The physical seed is a
hypothesis. Stage 1 supplies U4, W1 and W5 in the first three imports.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open Filter MeasureTheory
open scoped BigOperators ComplexConjugate InnerProductSpace NNReal Topology ContDiff
open YangMills YangMills.Construction
open Matrices TransferOperators SeparatedTuples ReflectionPositivity.TupleForm
open ReflectionPositivity.Reconstruction HilbertSpaceBasics LimitTheorem

namespace GapChain

/-- The release and row 1504 use the same matrix SU(2). -/
abbrev centreElt : ComplexMatrix2.specialUnitary := Wilson.centerMinus

section Slice
variable (Γ : CubicPeriodSublattice) (μ : Fin 4)

/-- A cut in direction ν changes the outgoing ν-links at residue zero.
The subsets of the three spatial axes index the eight electric translations. -/
def centreSign (cuts : Finset (Fin 4)) (e : Γ.LinkOrbits μ) : ComplexMatrix2.specialUnitary :=
  let l := TransferOperators.CubicPeriodSublattice.linkRep e
  if l.axis ∈ cuts ∧ Γ.coordResidues (l.source : InfiniteLattice.LatticePoint 1) l.axis = 0
  then centreElt else 1

def centreShift (cuts : Finset (Fin 4)) (u : Γ.LinkOrbits μ → ComplexMatrix2.specialUnitary) :
    Γ.LinkOrbits μ → ComplexMatrix2.specialUnitary := fun e => centreSign Γ μ cuts e * u e

theorem centreShift_measurePreserving (cuts : Finset (Fin 4)) :
    MeasurePreserving (centreShift Γ μ cuts)
      (ComplexMatrix2.haarPi (Γ.LinkOrbits μ)) (ComplexMatrix2.haarPi (Γ.LinkOrbits μ)) := by
  classical
  let := Fintype.ofFinite (Γ.LinkOrbits μ)
  let : ComplexMatrix2.haarProb.IsMulLeftInvariant := by
    unfold ComplexMatrix2.haarProb
    infer_instance
  rw [ComplexMatrix2.haarPi, Measure.infinitePi_eq_pi]
  exact measurePreserving_pi _ _ fun e =>
    measurePreserving_mul_left ComplexMatrix2.haarProb (centreSign Γ μ cuts e)

/-- Pullback by the actual Haar-preserving change of variables on a slice. -/
def centreTranslation (cuts : Finset (Fin 4)) : Γ.SliceL2 μ →L[ℂ] Γ.SliceL2 μ :=
  (Lp.compMeasurePreservingₗᵢ ℂ _ (centreShift_measurePreserving Γ μ cuts)).toContinuousLinearMap

def IsCentreTranslation (cuts : Finset (Fin 4)) (C : Γ.SliceL2 μ →L[ℂ] Γ.SliceL2 μ) : Prop :=
  ∀ φ : Γ.SliceL2 μ, (C φ : (Γ.LinkOrbits μ → ComplexMatrix2.specialUnitary) → ℂ)
    =ᵐ[ComplexMatrix2.haarPi (Γ.LinkOrbits μ)] φ ∘ centreShift Γ μ cuts

theorem centreTranslation_spec (cuts : Finset (Fin 4)) :
    IsCentreTranslation Γ μ cuts (centreTranslation Γ μ cuts) := fun φ =>
  Lp.coeFn_compMeasurePreserving φ (centreShift_measurePreserving Γ μ cuts)

/-- P₀ averages the centre action over all subsets of the three axes other than μ. -/
def neutralProj : Γ.SliceL2 μ →L[ℂ] Γ.SliceL2 μ :=
  (1 / 8 : ℂ) • ∑ cuts ∈ (Finset.univ.erase μ).powerset, centreTranslation Γ μ cuts

/-- The neutral rank-one test at lattice time w. -/
def RankOneAtTime (β : ℝ) (w : ℕ) : Prop :=
  ∃ (φ : Γ.SliceL2 μ) (c : ℝ), ‖φ‖ = 1 ∧ 0 < c ∧
    HSNormLE (((c⁻¹ : ℝ) : ℂ) • (neutralProj Γ μ * Γ.transfer μ β ^ w) - ketBra φ) (2 / 5)

def NeutralRankOneTest (β : ℝ) : Prop :=
  ∃ w : ℕ, 1 ≤ w ∧ 1024 * w ≤ Γ.side ∧ RankOneAtTime Γ μ β w

end Slice

/-- Periodic neutral excited trace in periodic-vacuum units. Summability and
a positive denominator are part of the bound, including when u = 2. -/
def NeutralTailLE (Γ : CubicPeriodSublattice) (β : ℝ) (u : ℕ) (b : ℝ) : Prop :=
  let T := Γ.transfer TimeAxis.timeIdx β
  let A := neutralProj Γ TimeAxis.timeIdx * T ^ u
  0 < ‖T‖ ∧ SpinHarmonics.TraceSummablePW A ∧
    (SpinHarmonics.tracePW A).re / ‖T‖ ^ u - 1 ≤ b

def NeutralPhysicalSeed (Γ : CubicPeriodSublattice) (β : ℝ) : Prop :=
  ∃ u : ℕ, 3 ≤ u ∧ 512 * u ≤ Γ.side ∧ NeutralTailLE Γ β u (1 / 2)

/-- One geometric plaquette per site and plane, with a sign on the stacks
xᵢ = xⱼ = 0 selected by the six twist bits (row 1004, §1.4). -/
def twistedPartition (β : ℝ) (sides : Wilson.Sides) (k : Wilson.Plane → Bool) : ℝ :=
  ∫ U : Wilson.Config sides, Real.exp (-β * (∑ x : Wilson.Site sides, ∑ p : Wilson.Plane,
    let i := p.val.1
    let j := p.val.2
    let sign : ℝ := if k p = true ∧ (x i).val = 0 ∧ (x j).val = 0 then -1 else 1
    1 - sign * Wilson.halfTrace (Wilson.transport U x i j))) ∂Wilson.haar sides

theorem twistedPartition_untwisted (β : ℝ) (sides : Wilson.Sides) :
    twistedPartition β sides (fun _ => false) = Wilson.partition β sides := by
  simp [twistedPartition, Wilson.partition, Wilson.density, Wilson.action_eq_geometric]

/-- The three complementary plane pairs give the sign (−1)^Pf(k). -/
def pfaffianSign (k : Wilson.Plane → Bool) : ℝ :=
  let pairSign (p q : Wilson.Plane) : ℝ := if k p && k q then -1 else 1
  pairSign ⟨(0, 1), by decide⟩ ⟨(2, 3), by decide⟩ *
    pairSign ⟨(0, 2), by decide⟩ ⟨(1, 3), by decide⟩ *
    pairSign ⟨(0, 3), by decide⟩ ⟨(1, 2), by decide⟩

/-- Wκ is the signed sum of 64 twisted partition functions divided by eight (row 731, §8.4). -/
def kappaWeight (β : ℝ) (sides : Wilson.Sides) : ℝ :=
  (∑ k : Wilson.Plane → Bool, pfaffianSign k * twistedPartition β sides k) / 8

/-- Sκ(n/2; n³) < 2⁻¹⁸ in the same periodic-vacuum normalization. -/
def KappaSeedOnCube (Γ : CubicPeriodSublattice) (β : ℝ) : Prop :=
  let N := Γ.side / 2
  let sides : Wilson.Sides := fun i => if i = TimeAxis.timeIdx then N else Γ.side
  let top := ‖Γ.transfer TimeAxis.timeIdx β‖
  0 < top ∧ kappaWeight β sides / top ^ N - 1 < 1 / (2 : ℝ) ^ 18

/-- Corollary M2, forward direction and monotonicity at max(3,2w). -/
theorem neutralTail_of_rankOneAtTime (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    {w : ℕ} (hw : 1 ≤ w) (h : RankOneAtTime Γ TimeAxis.timeIdx β w) :
    NeutralTailLE Γ β (2 * w) (4 / 21) ∧ NeutralTailLE Γ β (max 3 (2 * w)) (4 / 21) := by
  sorry -- Stage 4, W8: identify the neutral trace with the Stage 1 M1 estimate.

theorem neutralPhysicalSeed_of_mNeutral (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (hside : 1536 ≤ Γ.side) (h : NeutralRankOneTest Γ TimeAxis.timeIdx β) :
    NeutralPhysicalSeed Γ β := by
  obtain ⟨w, hw, hwSide, htest⟩ := h
  obtain ⟨htop, hsum, htail⟩ := (neutralTail_of_rankOneAtTime Γ hβ hw htest).2
  refine ⟨max 3 (2 * w), le_max_left .., ?_, htop, hsum, htail.trans (by norm_num)⟩
  rcases le_total 3 (2 * w) with hle | hle
  · rw [max_eq_right hle]
    omega
  · rw [max_eq_left hle]
    omega

/-- Row 1161's finite-aspect theorem at the constants consumed by the chain. -/
theorem kappaSeed_of_neutralPhysicalSeed (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (hfour : 4 ∣ Γ.side) (hlarge : 2 ^ 70 ≤ Γ.side) (hs : NeutralPhysicalSeed Γ β) :
    KappaSeedOnCube Γ β := by
  sorry -- Stage 4, W7: both flux alternatives give the Pfaffian seed on this cube.

/-- Inverse squared bare coupling selected by the release's reference observable. -/
def betaAt (L M K : ℕ) (g₀ : ℝ) : ℝ := (renormalizedBareCoupling L M K g₀ ^ 2)⁻¹

def NeutralAtCutoff (L M : ℕ) (g₀ : ℝ) (ℓ K : ℕ) : Prop :=
  ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ K →
    NeutralRankOneTest Γ TimeAxis.timeIdx (betaAt L M K g₀)

/-- At a specified physical side. The seed of row 1453 is `∃ ℓ, MNeutralAll L M g₀ ℓ`. -/
def MNeutralAll (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) : Prop :=
  0 < ℓ ∧ 4 ∣ ℓ ∧ ∃ K₀ : ℕ, ∀ K ≥ K₀, NeutralAtCutoff L M g₀ ℓ K

def MNeutralAlong (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) (K : ℕ → ℕ+) : Prop :=
  0 < ℓ ∧ 4 ∣ ℓ ∧ ∃ᶠ j in atTop, NeutralAtCutoff L M g₀ ℓ (K j)

def KappaSeedAlong (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) (K : ℕ → ℕ+) : Prop :=
  0 < ℓ ∧ 4 ∣ ℓ ∧ ∃ᶠ j in atTop, ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ (K j : ℕ) →
    KappaSeedOnCube Γ (betaAt L M (K j) g₀)

theorem MNeutralAll.along {L M : ℕ} {g₀ : ℝ} {ℓ : ℕ} (h : MNeutralAll L M g₀ ℓ)
    {K : ℕ → ℕ+} (hK : StrictMono K) : MNeutralAlong L M g₀ ℓ K := by
  obtain ⟨hpos, hfour, K₀, htail⟩ := h
  have hmono : StrictMono fun j => (K j : ℕ) := fun _ _ hij => hK hij
  have hlate : ∀ᶠ j : ℕ in atTop, K₀ ≤ (K j : ℕ) :=
    hmono.tendsto_atTop (eventually_ge_atTop K₀)
  exact ⟨hpos, hfour, (hlate.mono fun j hj => htail (K j) hj).frequently⟩

/-- Semigroup form of the gap on the OS completion of positive-time separated tensors. -/
def HasMassGap (σ : TupleFunctional) (m : ℝ) : Prop :=
  ∃ hσ : IsPosSemidef (reflectionForm σ), HasReconstruction σ hσ ∧
    ∀ ψ : PhysicalSpace σ hσ, ⟪vacuum σ hσ, ψ⟫_ℂ = 0 →
      ∀ t : ℝ≥0, ‖timeShift σ hσ t ψ‖ ≤ Real.exp (-m * (t : ℝ)) * ‖ψ‖

def HasUniqueVacuum (σ : TupleFunctional) : Prop :=
  ∃ hσ : IsPosSemidef (reflectionForm σ), HasReconstruction σ hσ ∧
    ∀ ψ : PhysicalSpace σ hσ, (∀ t : ℝ≥0, timeShift σ hσ t ψ = ψ) →
      ∃ c : ℂ, ψ = c • vacuum σ hσ

/-- A fixed vector's orthogonal component contracts strictly at time one. -/
theorem HasMassGap.uniqueVacuum {σ : TupleFunctional} {m : ℝ} (hm : 0 < m)
    (h : HasMassGap σ m) : HasUniqueVacuum σ := by
  obtain ⟨hσ, hrec, hbound⟩ := h
  refine ⟨hσ, hrec, fun ψ hfix => ?_⟩
  let Ω := vacuum σ hσ
  let c := ⟪Ω, ψ⟫_ℂ
  have hunit : ‖Ω‖ = 1 := hrec.1.2.1
  have horth : ⟪Ω, ψ - c • Ω⟫_ℂ = 0 := by
    simp [inner_sub_right, inner_smul_right, inner_self_eq_norm_sq_to_K, hunit, c]
  have hΩ : timeShift σ hσ 1 Ω = Ω :=
    ReflectionPositivity.ShiftSpectralMeasure.timeShift_vacuum σ hσ hrec.2.1.2.1 1
  have hle := hbound (ψ - c • Ω) horth 1
  rw [map_sub, map_smul, hfix, hΩ] at hle
  have hstrict : Real.exp (-m * ((1 : ℝ≥0) : ℝ)) < 1 := by
    simpa only [NNReal.coe_one, mul_one, Real.exp_lt_one_iff] using neg_lt_zero.mpr hm
  refine ⟨c, sub_eq_zero.mp ?_⟩
  by_contra hn
  exact (not_lt_of_ge hle) (by
    simpa only [one_mul] using mul_lt_mul_of_pos_right hstrict (norm_pos_iff.mpr hn))

/-- The centred lattice moment accepts lists of any length, including overlapping tests. -/
def listMoment {a : ℝ} (ν : Measure (InfiniteLattice.GaugeField a)) (fs : List RealValued) : ℂ :=
  InfiniteLattice.centeredMoment ν fs.get

/-- Reflected truncated autocorrelation. Ordinary lists keep both arguments even at
negative times. Both the individual energies and the final mean use the same ν. -/
def latticeU {a : ℝ} (ν : Measure (InfiniteLattice.GaugeField a)) (Z : PositiveSpan)
    (t : ℝ) : ℝ :=
  let z := Z.val
  let mean := ∑ X ∈ z.support, z X * listMoment ν X.val
  let pair := ∑ X ∈ z.support, ∑ Y ∈ z.support,
    conj (z X) * z Y * listMoment ν
      (pushList TimeAxis.timeReflection X.val ++ pushList (translate (t • timeBasisVec)) Y.val)
  pair.re - ‖mean‖ ^ 2

abbrev CutoffStates (L : ℕ) (K : ℕ → ℕ+) :=
  ∀ j : ℕ, Measure (InfiniteLattice.GaugeField (PeriodicLattice.meshSize L (K j : ℤ)))

/-- (EC-ν) on all positive-time finite complex combinations of separated C¹_c tuples.
The link mirror is at −a/2. The good cutoffs and prefactors may depend on Z. -/
def ExpClusters (L : ℕ) (K : ℕ → ℕ+) (ν : CutoffStates L K) (m : ℝ) : Prop :=
  ∀ Z : PositiveSpan, ∃ᶠ j in atTop, ∃ C : ℝ, ∀ n : ℕ,
    let t := (2 * (n : ℝ) + 1) * PeriodicLattice.meshSize L (K j : ℤ)
    latticeU (ν j) Z t ≤ C * Real.exp (-m * t)

/-- The public lattice clauses needed for reconstruction at the named witnesses (check 1458, R1). -/
structure Inputs (L M : ℕ) (g₀ : ℝ) (K : ℕ → ℕ+) (ν : CutoffStates L K)
    (S : CumulantFamily) : Prop where
  strictMono : StrictMono K
  beta_pos : ∀ j, 0 < betaAt L M (K j) g₀
  isLimit : ∀ j, InfiniteLattice.IsInfiniteVolumeLimit L (K j) (betaAt L M (K j) g₀) (ν j)
  moments : ∀ n (X : TestSpaces.SepTupleOfCard n),
    Tendsto (fun j => InfiniteLattice.centeredMoment (ν j) X.val) atTop
      (𝓝 (TestSpaces.centredOfCumulants S ⟨n, X⟩ : ℂ))

def gapRate (ℓ : ℕ) : ℝ := (2 / (ℓ : ℝ)) * Real.log ((2 : ℝ) ^ 18 / 5041)

theorem gapRate_pos {ℓ : ℕ} (hℓ : 0 < ℓ) : 0 < gapRate ℓ := by
  exact mul_pos (div_pos (by norm_num) (by exact_mod_cast hℓ)) (Real.log_pos (by norm_num))

section Chain
variable {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K} {S : CumulantFamily}

/-- Upper half U. Pass the odd-grid estimate through the moment limit and complete the OS space. -/
theorem massGap_of_expClusters (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hm : 0 < m) (hc : ExpClusters L K ν m) :
    HasMassGap (centredOf S) m := by
  sorry -- Stage 2: public reconstruction, odd-grid moments, dense times and completion.

theorem kappaSeedAlong_of_mNeutral (hL : Conventions.IsAdmissibleBlockingFactor L)
    (hK : StrictMono K) (hβ : ∀ j, 0 < betaAt L M (K j) g₀)
    {ℓ : ℕ} (hs : MNeutralAlong L M g₀ ℓ K) : KappaSeedAlong L M g₀ ℓ K := by
  have hmono : StrictMono fun j => (K j : ℕ) := fun _ _ hij => hK hij
  have hlate := hmono.tendsto_atTop (eventually_ge_atTop 70)
  refine ⟨hs.1, hs.2.1, (hs.2.2.and_eventually hlate).mono ?_⟩
  rintro j ⟨htest, hj⟩ Γ hΓ
  have hlarge : 2 ^ 70 ≤ Γ.side := calc
    (2 : ℕ) ^ 70 ≤ 2 ^ (K j : ℕ) := Nat.pow_le_pow_right (by decide) hj
    _ ≤ L ^ (K j : ℕ) := Nat.pow_le_pow_left (by have := hL.2; omega) _
    _ ≤ ℓ * L ^ (K j : ℕ) := Nat.le_mul_of_pos_left _ hs.1
    _ = Γ.side := hΓ.symm
  have hfour : 4 ∣ Γ.side := hΓ ▸ dvd_mul_of_dvd_left hs.2.1 _
  exact kappaSeed_of_neutralPhysicalSeed Γ (hβ j) hfour hlarge
    (neutralPhysicalSeed_of_mNeutral Γ (hβ j) (le_trans (by decide : 1536 ≤ 2 ^ 70) hlarge)
      (htest Γ hΓ))

/-- The Stage 3 interface uses the Pfaffian seed on the good cutoffs of these very states. -/
theorem expClusters_of_kappaSeed (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K) :
    ExpClusters L K ν (gapRate ℓ) := by
  sorry -- Stage 3, W2–W6 and W9–W11: twisted propagation, slab estimates and the volume limit.

theorem expClusters_of_mNeutral (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : MNeutralAlong L M g₀ ℓ K) :
    ExpClusters L K ν (gapRate ℓ) :=
  expClusters_of_kappaSeed hL h (kappaSeedAlong_of_mNeutral hL h.strictMono h.beta_pos hs)

theorem massGap_of_mNeutral (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : MNeutralAlong L M g₀ ℓ K) :
    HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S) := by
  have hm := gapRate_pos hs.1
  have hgap := massGap_of_expClusters hL h hm (expClusters_of_mNeutral hL h hs)
  exact ⟨hgap, hgap.uniqueVacuum hm⟩

end Chain

open PeriodicLattice

/-- The body of Sussman and Alpoge's fixed-observable export at its six witnesses.
The definitional equivalence below checks all conjuncts and their scopes. -/
def FixedObservableWitnesses (L M : ℕ) (g₀ : ℝ) (K v : ℕ → ℕ+) (ν : CutoffStates L K)
    (S : CumulantFamily) (X₂ : TestSpaces.SepTupleOfCard 2) (X₄ : TestSpaces.SepTupleOfCard 4) :
    Prop :=
  let g := fun j => renormalizedBareCoupling L M (K j) g₀
  let β := fun j => betaAt L M (K j) g₀
  StrictMono K ∧
  (∀ j, IsLeast {u : ℝ | 0 < u ∧ referenceResponse L M (K j) (u ^ 2)⁻¹ = fixedPhysicalLevel g₀}
    (g j)) ∧
  Tendsto (fun j => (g j) ^ 2 * (K j : ℝ) * Real.log L) atTop (𝓝 (3 * Real.pi ^ 2 / 11)) ∧
  (∀ j, InfiniteLattice.IsInfiniteVolumeLimit L (K j) (β j) (ν j)) ∧
  Tendsto (fun j => torusSide L (v j)) atTop atTop ∧
  Tendsto (fun j => β j / ((K j : ℝ) * Real.log L)) atTop (𝓝 (11 / (3 * Real.pi ^ 2))) ∧
  (∀ n hn (X : TestSpaces.SepTupleOfCard n),
    (∀ᶠ j in atTop, SchwingerFunctions.IsR4TestFamily (torusSide L (v j)) X.val) ∧
    Tendsto (fun j => InfiniteLattice.smearedEnergyCumulant (ν j) X.val) atTop (𝓝 (S n hn X : ℂ)) ∧
    Tendsto (fun j => SchwingerFunctions.connectedSchwingerR4 L (v j) (K j) (β j) X.val)
      atTop (𝓝 (S n hn X : ℂ))) ∧
  (∀ n (X : TestSpaces.SepTupleOfCard n), let z : ℂ := TestSpaces.centredOfCumulants S ⟨n, X⟩
    Tendsto (fun j => InfiniteLattice.centeredMoment (ν j) X.val) atTop (𝓝 z) ∧
    Tendsto (fun j => su2_centeredMoment L (v j) (K j) (β j) X) atTop (𝓝 z)) ∧
  (∀ i, ContDiff ℝ ∞ (X₂.val i)) ∧ 0 < S 2 le_rfl X₂ ∧
  (∀ i, ContDiff ℝ ∞ (X₄.val i)) ∧ 0 < S 4 (by decide) X₄ ∧
  (∃ (D : SystemsWithFiveBounds.LimitConstants) (T : ConfigSpace.FlatSequence),
    D.Valid ∧ SystemsWithFiveBounds.HasSchwingerSequence (centredOf S) T ∧
    SystemsWithFiveBounds.SatisfiesGrowth T D.schwartzOrder D.schwartzPrefactor D.schwartzBase D.schwartzExp ∧
    ConfigSpace.IsEuclidInvariant T ∧ ConfigSpace.IsOSPositive T ∧
    ConfigSpace.IsPermSymmetric T ∧ ConfigSpace.IsReflectionReal T ∧ HasCumulants (centredOf S) S) ∧
  ∃ (A : SeparatedTuples.DecompositionData) (D : SystemsWithFiveBounds.LimitConstants),
    D.Valid ∧ A.IsCanonical (centredOf S) ∧
    (∀ ξ, ∃ T : ConfigSpace.FlatSequence, SystemsWithFiveBounds.HasSchwingerSequence (A.comp ξ) T ∧
      SystemsWithFiveBounds.OSAxioms D T) ∧
    ∀ᵐ ξ ∂A.law, ModelSeams.IsNonGaussianOnSmoothQuadruple (A.comp ξ)

theorem fixedObservableContinuum_iff (L M : ℕ) (g₀ : ℝ) :
    FixedObservableContinuum L M g₀ ↔
      ∃ K v ν S X₂ X₄, FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ := Iff.rfl

theorem FixedObservableWitnesses.inputs {L M : ℕ} {g₀ : ℝ} {K v : ℕ → ℕ+}
    {ν : CutoffStates L K} {S : CumulantFamily} {X₂ : TestSpaces.SepTupleOfCard 2}
    {X₄ : TestSpaces.SepTupleOfCard 4} (h : FixedObservableWitnesses L M g₀ K v ν S X₂ X₄) :
    Inputs L M g₀ K ν S := by
  obtain ⟨hK, hroot, _, hν, _, _, _, hmom, _⟩ := h
  exact ⟨hK, fun j => inv_pos.mpr (sq_pos_of_pos (hroot j).1.1), hν, fun n X => (hmom n X).1⟩

/-- The full OS export, with the conditional gap attached inside the original witness scope. -/
def FixedObservableContinuumWithGap (L M : ℕ) (g₀ : ℝ) : Prop :=
  ∃ K v ν S X₂ X₄, FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧
    ∀ ℓ, MNeutralAll L M g₀ ℓ →
      HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S)

theorem su2_fixed_observable_gap_of_mNeutral : FixedObservableLimit FixedObservableContinuumWithGap := by
  obtain ⟨L₀, h⟩ := su2_fixed_observable_continuum_limit
  refine ⟨max L₀ 13, fun L hodd hL => ?_⟩
  obtain ⟨M, δ, hside, hδ, hall, hlim⟩ := h L hodd ((le_max_left ..).trans hL)
  have hadm : Conventions.IsAdmissibleBlockingFactor L := ⟨hodd, (le_max_right ..).trans hL⟩
  refine ⟨M, δ, hside, hδ, hall, fun g₀ hg₀ => ?_⟩
  obtain ⟨K, v, ν, S, X₂, X₄, hw⟩ := (fixedObservableContinuum_iff L M g₀).mp (hlim g₀ hg₀)
  exact ⟨K, v, ν, S, X₂, X₄, hw, fun _ hs =>
    massGap_of_mNeutral hadm hw.inputs (hs.along hw.inputs.strictMono)⟩

end GapChain

#print axioms GapChain.centreShift_measurePreserving
#print axioms GapChain.centreTranslation_spec
#print axioms GapChain.twistedPartition_untwisted
#print axioms GapChain.neutralTail_of_rankOneAtTime
#print axioms GapChain.neutralPhysicalSeed_of_mNeutral
#print axioms GapChain.kappaSeed_of_neutralPhysicalSeed
#print axioms GapChain.MNeutralAll.along
#print axioms GapChain.HasMassGap.uniqueVacuum
#print axioms GapChain.gapRate_pos
#print axioms GapChain.massGap_of_expClusters
#print axioms GapChain.kappaSeedAlong_of_mNeutral
#print axioms GapChain.expClusters_of_kappaSeed
#print axioms GapChain.expClusters_of_mNeutral
#print axioms GapChain.massGap_of_mNeutral
#print axioms GapChain.fixedObservableContinuum_iff
#print axioms GapChain.FixedObservableWitnesses.inputs
#print axioms GapChain.su2_fixed_observable_gap_of_mNeutral
