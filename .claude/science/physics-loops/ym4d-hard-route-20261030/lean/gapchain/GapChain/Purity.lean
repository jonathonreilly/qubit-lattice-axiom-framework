import GapChain.Final

/-!
# A conditional gap from the neutral two-period purity

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, supply the Wilson transfer, Peter–Weyl trace and continuum witnesses.
The purity test is Fact PUR (Codex rows 1373 and 1461, Claude Opus check
1465, Claude Fable row 1468 §3.1). We follow the direct physical-seed
argument of Codex check 1675 on the cutoff sequence of the chosen witnesses.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open Filter YangMills YangMills.Construction
open TransferOperators SpinHarmonics SeparatedTuples LimitTheorem

namespace GapChain

local notation "μt" => TimeAxis.timeIdx

/-- The two neutral Peter–Weyl traces on the same spatial cube, at times 2u and u. -/
def purity (Γ : CubicPeriodSublattice) (β : ℝ) (u : ℕ) : ℝ :=
  let T := Γ.transfer μt β
  let P₀ := neutralProj Γ μt
  (tracePW (P₀ * T ^ (2 * u)) / tracePW (P₀ * T ^ u) ^ 2).re

/-- For infinitely many indices of K, every cube of the specified side passes the purity test. -/
def PurityAlong (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) (K : ℕ → ℕ+) : Prop :=
  0 < ℓ ∧ 1024 ∣ ℓ ∧ ∃ᶠ j in atTop,
    ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ (K j : ℕ) →
      457 / 625 ≤ purity Γ (betaAt L M (K j) g₀) (Γ.side / 512)

namespace Purity

open Stage3 (zeroFlux)
open Stage4 (sectorMoment)

/-- Restoring the periodic-vacuum units gives the actual complex Peter–Weyl trace. -/
theorem neutralTrace_eq_scaledMoment (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (t : ℕ) (ht : 2 ≤ t) :
    tracePW (neutralProj Γ μt * Γ.transfer μt β ^ t) =
      ((sectorMoment Γ β zeroFlux zeroFlux t * ‖Γ.transfer μt β‖ ^ t : ℝ) : ℂ) := by
  rw [sectorMoment, div_mul_cancel₀ _ (pow_ne_zero _ (Stage4.periodicTransfer_norm_pos Γ hβ).ne')]
  simpa only [Stage3.electricProj_zero, Stage3.magneticTransfer_zero] using
    (Stage4.projectedTrace_eq_sectorWeight Γ hβ zeroFlux zeroFlux t ht).2

/-- On the summable powers the complex trace ratio itself equals the real purity. -/
theorem purity_eq_traceRatio (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (u : ℕ) (hu : 2 ≤ u) :
    (purity Γ β u : ℂ) = tracePW (neutralProj Γ μt * Γ.transfer μt β ^ (2 * u)) /
      tracePW (neutralProj Γ μt * Γ.transfer μt β ^ u) ^ 2 := by
  simp only [purity, neutralTrace_eq_scaledMoment Γ hβ (2 * u) (by omega),
    neutralTrace_eq_scaledMoment Γ hβ u hu, ← Complex.ofReal_pow, ← Complex.ofReal_div,
    Complex.ofReal_re]

/-- The common top eigenvalue cancels between the two physical periods. -/
theorem purity_eq_sectorMoments (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (u : ℕ) (hu : 2 ≤ u) :
    purity Γ β u =
      sectorMoment Γ β zeroFlux zeroFlux (2 * u) / sectorMoment Γ β zeroFlux zeroFlux u ^ 2 := by
  have hpow : ‖Γ.transfer μt β‖ ^ (2 * u) = (‖Γ.transfer μt β‖ ^ u) ^ 2 := by
    rw [Nat.mul_comm 2 u, pow_mul]
  simp only [purity, neutralTrace_eq_scaledMoment Γ hβ (2 * u) (by omega),
    neutralTrace_eq_scaledMoment Γ hβ u hu, ← Complex.ofReal_pow, ← Complex.ofReal_div,
    Complex.ofReal_re]
  rw [hpow, mul_pow, mul_div_mul_right _ _
    (pow_ne_zero 2 (pow_ne_zero u (Stage4.periodicTransfer_norm_pos Γ hβ).ne'))]

/-- A neutral slot in [0,1] contributes at most as much at 2u as at u.
Slot zero contributes one at u, so division by the short moment is legitimate. -/
theorem neutralTailLE_of_purity (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (hfour : 4 ∣ Γ.side) {u : ℕ} (hu : 2 ≤ u) (hp : 2 / 3 ≤ purity Γ β u) :
    NeutralTailLE Γ β u (1 / 2) := by
  obtain ⟨F⟩ := Stage4.cubeFluxSpectrum Γ hβ hfour
  let D := sectorMoment Γ β zeroFlux zeroFlux u
  have short := F.moment zeroFlux zeroFlux u hu
  have hDpos : 0 < D := by
    have h := short.summable.le_tsum 0 (fun i _ => pow_nonneg (F.nonneg zeroFlux zeroFlux i) u)
    rw [F.vacuum, one_pow, short.tsum_eq] at h
    exact zero_lt_one.trans_le h
  have hdouble : sectorMoment Γ β zeroFlux zeroFlux (2 * u) ≤ D :=
    hasSum_le (fun i => pow_le_pow_of_le_one (F.nonneg zeroFlux zeroFlux i)
      (F.le_one zeroFlux zeroFlux i) (by omega : u ≤ 2 * u))
      (F.moment zeroFlux zeroFlux (2 * u) (by omega)) short
  have hbound : (2 / 3 : ℝ) ≤ 1 / D := calc
    2 / 3 ≤ purity Γ β u := hp
    _ = sectorMoment Γ β zeroFlux zeroFlux (2 * u) / D ^ 2 := purity_eq_sectorMoments Γ hβ u hu
    _ ≤ D / D ^ 2 := div_le_div_of_nonneg_right hdouble (sq_nonneg D)
    _ = 1 / D := by simpa only [one_mul, sq] using (mul_div_mul_right 1 D hDpos.ne')
  apply (Stage4.neutralTail_iff_sectorWeight Γ hβ u hu (1 / 2)).2
  change D - 1 ≤ 1 / 2
  linarith only [(le_div_iff₀ hDpos).mp hbound]

/-- The requested finite cube uses the single time ⌊side/512⌋. The 2^70
size condition is needed by the subsequent Stage 4 Pfaffian implication. -/
theorem neutralPhysicalSeed_of_purity (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (hfour : 4 ∣ Γ.side) (_hlarge : 2 ^ 70 ≤ Γ.side) (hside : 1536 ≤ Γ.side)
    (hp : 2 / 3 ≤ purity Γ β (Γ.side / 512)) : NeutralPhysicalSeed Γ β := by
  have hu : 3 ≤ Γ.side / 512 := (Nat.le_div_iff_mul_le (by decide : 0 < 512)).2 hside
  exact ⟨Γ.side / 512, hu, by omega,
    neutralTailLE_of_purity Γ hβ hfour ((by decide : 2 ≤ 3).trans hu) hp⟩

variable {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K} {S : CumulantFamily}

theorem kappaSeedAlong_of_purity (hL : Conventions.IsAdmissibleBlockingFactor L)
    (hK : StrictMono K) (hβ : ∀ j, 0 < betaAt L M (K j) g₀)
    {ℓ : ℕ} (hs : PurityAlong L M g₀ ℓ K) : KappaSeedAlong L M g₀ ℓ K := by
  have hfour : 4 ∣ ℓ := dvd_trans (by decide : 4 ∣ 1024) hs.2.1
  have hmono : StrictMono fun j => (K j : ℕ) := fun _ _ hij => hK hij
  have hlate := hmono.tendsto_atTop (eventually_ge_atTop 70)
  refine ⟨hs.1, hfour, (hs.2.2.and_eventually hlate).mono ?_⟩
  rintro j ⟨htest, hj⟩ Γ hΓ
  have hlarge : 2 ^ 70 ≤ Γ.side := calc
    (2 : ℕ) ^ 70 ≤ 2 ^ (K j : ℕ) := Nat.pow_le_pow_right (by decide) hj
    _ ≤ L ^ (K j : ℕ) := Nat.pow_le_pow_left (by have := hL.2; omega) _
    _ ≤ ℓ * L ^ (K j : ℕ) := Nat.le_mul_of_pos_left _ hs.1
    _ = Γ.side := hΓ.symm
  have hd : 4 ∣ Γ.side := hΓ ▸ dvd_mul_of_dvd_left hfour _
  apply Stage4.kappaSeed_of_neutralPhysicalSeed Γ (hβ j) hd hlarge
  exact neutralPhysicalSeed_of_purity Γ (hβ j) hd hlarge ((by decide : 1536 ≤ 2 ^ 70).trans hlarge)
    ((by norm_num : (2 / 3 : ℝ) ≤ 457 / 625).trans (htest Γ hΓ))

theorem massGap_of_purity (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : PurityAlong L M g₀ ℓ K) :
    HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S) := by
  have hm := gapRate_pos hs.1
  have hκ := kappaSeedAlong_of_purity hL h.strictMono h.beta_pos hs
  have hgap := Stage2.massGap_of_expClusters hL h hm (Stage3b.expClusters_of_kappaSeed hL h hκ)
  exact ⟨hgap, hgap.uniqueVacuum hm⟩

/-- Choose all six release witnesses before testing any physical side on their cutoffs K. -/
theorem su2_fixed_observable_gap_of_purity :
    FixedObservableLimit (fun L M g₀ =>
      ∃ K v ν S X₂ X₄, FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧
        ∀ ℓ, PurityAlong L M g₀ ℓ K →
          HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S)) := by
  obtain ⟨L₀, h⟩ := YangMills.su2_fixed_observable_continuum_limit
  refine ⟨max L₀ 13, fun L hodd hL => ?_⟩
  obtain ⟨M, δ, hside, hδ, hall, hlim⟩ := h L hodd ((le_max_left ..).trans hL)
  have hadm : Conventions.IsAdmissibleBlockingFactor L := ⟨hodd, (le_max_right ..).trans hL⟩
  refine ⟨M, δ, hside, hδ, hall, fun g₀ hg₀ => ?_⟩
  obtain ⟨K, v, ν, S, X₂, X₄, hw⟩ :=
    (fixedObservableContinuum_iff L M g₀).mp (hlim g₀ hg₀)
  exact ⟨K, v, ν, S, X₂, X₄, hw, fun _ hs => massGap_of_purity hadm hw.inputs hs⟩

end Purity
end GapChain

#print axioms GapChain.Purity.neutralTrace_eq_scaledMoment
#print axioms GapChain.Purity.purity_eq_traceRatio
#print axioms GapChain.Purity.purity_eq_sectorMoments
#print axioms GapChain.Purity.neutralTailLE_of_purity
#print axioms GapChain.Purity.neutralPhysicalSeed_of_purity
#print axioms GapChain.Purity.kappaSeedAlong_of_purity
#print axioms GapChain.Purity.massGap_of_purity
#print axioms GapChain.Purity.su2_fixed_observable_gap_of_purity
