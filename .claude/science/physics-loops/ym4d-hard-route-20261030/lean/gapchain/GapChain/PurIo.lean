import GapChain.Purity

/-!
# Selecting calibrated cutoffs for the two-period purity test

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, supply the record estimate and the fixed-observable extraction
(YM4 release 3932084a). We keep the record condition visible when choosing the
cutoffs. The physical gap implication is the lane's row 1676.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open Filter Set YangMills YangMills.Construction
open YangMills.ContinuumLimit YangMills.BranchHot YangMills.Formulation
open TheStatementsProvedTogether ResponseInTheExpansion
open TransferOperators SeparatedTuples LimitTheorem
open scoped Topology

namespace GapChain.PurIo

/-- Original cutoffs passing the test on every cube of the prescribed side. -/
def passingCutoffs (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) : Set ℕ :=
  {k | ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ k →
    457 / 625 ≤ purity Γ (betaAt L M k g₀) (Γ.side / 512)}

/-- The one-loop partial sum, after subtracting half the mean slope, has a
running maximum at k. The comparison ranges over every earlier index. -/
def recordCutoffs (a : ℕ → ℝ) (s : ℝ) : Set ℕ :=
  {k | ∀ i < k, s / 2 * ((k : ℝ) - i) ≤ ∑ t ∈ Finset.Ico i k, a t}

/-- A positive average slope with bounded interval error gives a record in
each block of a fixed length. The length is independent of its starting point. -/
theorem record_in_every_block {a : ℕ → ℝ} {s c : ℝ} (hs : 0 < s)
    (ha : CouplingFlow.HasAverageSlope a s c) :
    ∃ d : ℕ, ∀ n : ℕ, ∃ k ∈ Icc n (n + d), k ∈ recordCutoffs a s := by
  obtain ⟨d, hd⟩ := exists_nat_gt (4 * c / s)
  let F (k : ℕ) := (∑ t ∈ Finset.range k, a t) - s / 2 * k
  have diff (i k : ℕ) (hik : i ≤ k) :
      F k - F i = (∑ t ∈ Finset.Ico i k, a t) - s / 2 * ((k : ℝ) - i) := by
    rw [Finset.sum_Ico_eq_sub _ hik]
    dsimp [F]
    ring
  refine ⟨d, fun n => ?_⟩
  obtain ⟨k, hk, hmax⟩ := (Finset.range (n + d + 1)).exists_max_image F ⟨0, by simp⟩
  have hkEnd : k ≤ n + d := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  have hstart : n ≤ k := by
    by_contra! hkn
    have hkn' : (k : ℝ) ≤ n := by exact_mod_cast hkn.le
    have hgain : 2 * c < s / 2 * (((n + d : ℕ) : ℝ) - k) := calc
      2 * c < s / 2 * (d : ℝ) := by nlinarith [(div_lt_iff₀ hs).mp hd]
      _ ≤ _ := mul_le_mul_of_nonneg_left (by push_cast; linarith) (by positivity)
    have hlow := (abs_le.mp (ha k (n + d) hkEnd)).1
    have hhigh := hmax (n + d) (Finset.mem_range.mpr (Nat.lt_succ_self _))
    nlinarith only [diff k (n + d) hkEnd, hlow, hhigh, hgain]
  refine ⟨k, ⟨hstart, hkEnd⟩, fun i hi => ?_⟩
  have h := hmax i (Finset.mem_range.mpr (hi.trans (Finset.mem_range.mp hk)))
  linarith only [diff i k hi.le, h]

/-- Even nonnegative coefficients of mean slope one can have zero last step
at every odd endpoint. This specializes the alternating error of rf10-incr §1
to disjointness from the release's record set. -/
theorem averageSlope_can_miss_infinite_set :
    ∃ (a : ℕ → ℝ) (A : Set ℕ), CouplingFlow.HasAverageSlope a 1 1 ∧
      A.Infinite ∧ (∀ t, 0 ≤ a t) ∧ Disjoint A (recordCutoffs a 1) := by
  let F (n : ℕ) : ℝ := n - (n % 2 : ℕ)
  let a (n : ℕ) := F (n + 1) - F n
  have total (i j : ℕ) (hij : i ≤ j) :
      ∑ t ∈ Finset.Ico i j, a t = F j - F i := by
    induction j, hij using Nat.le_induction with
    | base => simp
    | succ j hij ih =>
      rw [Finset.sum_Ico_succ_top hij, ih]
      dsimp only [a]
      ring
  have rem_le (n : ℕ) : ((n % 2 : ℕ) : ℝ) ≤ 1 := by
    exact_mod_cast (show n % 2 ≤ 1 by omega)
  have rem_nonneg (n : ℕ) : (0 : ℝ) ≤ (n % 2 : ℕ) := by positivity
  refine ⟨a, range (fun j : ℕ => 2 * j + 1), ?_,
    infinite_range_of_injective (fun _ _ h => by omega), ?_, ?_⟩
  · intro i j hij
    rw [total i j hij]
    dsimp only [F]
    rw [abs_le]
    constructor <;> linarith [rem_le i, rem_le j, rem_nonneg i, rem_nonneg j]
  · intro t
    dsimp only [a, F]
    push_cast
    linarith [rem_le (t + 1), rem_nonneg t]
  · apply Set.disjoint_left.mpr
    rintro _ ⟨j, rfl⟩ hr
    have h := hr (2 * j) (Nat.lt_succ_self _)
    rw [total (2 * j) (2 * j + 1) (Nat.le_succ _)] at h
    simp [F, Nat.add_mod] at h
    linarith

/-- Pointwise part of the release's `uniform_record_gap` (RecordCutoffs.lean).
Taking the record as an argument allows restriction to a prescribed set. -/
theorem drop_at_record {T : RenormalizationStepParameters.ParameterAssignment} {y : ℝ}
    {Kr : WeightedResponses.ResponseParameters} {lam cr s : ℝ} (hs : 0 < s)
    (hr : RunTable T y Kr lam cr) (hF : RefinedTable T y) :
    ∃ H : ℝ, ∀ k ∈ recordCutoffs (FamilyNorms.ParameterAssignment.oneLoop T) s,
      ∀ (b P : ℝ), H ≤ P → IsTunedAt T y P k b →
        ∀ i < k, P + s/4 ≤ TotalDensityFlow.coupling (T.stepParameters y) b i := by
  obtain ⟨C₁,M,hF⟩ := hF
  let A := C₁ * (2*C₁+1)
  let X := max (1:ℝ) (max (8*M/s) ((8*A/s)^(4/5:ℝ)))
  refine ⟨X + |cr|, ?_⟩
  intro k hk b P hP ht
  let x := flowCouplings (T.stepParameters y) b
  let a := FamilyNorms.ParameterAssignment.oneLoop T
  have had := (above_iff_total expansion_gives_total_flow total_density_flow_unique hr).mp ht.1
  have he := (total_flow_of_above_total expansion_gives_total_flow total_density_flow_unique hr ht.1).2
  have hterm : x k = P := (he k le_rfl).symm.trans ht.2
  have hl (t : ℕ) (htk : t ≤ k) : X ≤ x t := by
    have h := hr.descent b had.1 k had.2 t htk
    change lam * ((k:ℝ)-t) - cr ≤ x t - x k at h
    have hd : 0 ≤ lam * ((k:ℝ)-t) := mul_nonneg hr.lam_pos.le (sub_nonneg.mpr (by exact_mod_cast htk))
    linarith [le_abs_self cr]
  have hs₁ (t : ℕ) (htk : t < k) : a t - s/4 ≤ x t - x (t+1) := by
    have hstay : CouplingFlow.StaysAbove y (CouplingFlow.couplingAt (T.stepParameters y) b) t :=
      fun j hj => had.2 j (lt_of_le_of_lt hj htk)
    have hrm := CouplingFlow.followsFlowAbove_couplingAt hF le_rfl b t hstay
    change |x (t+1) - (x t - a t - FamilyNorms.ParameterAssignment.secondStep T t / x t)| ≤
      A * x t ^ (-(5/4):ℝ) at hrm
    have hX := hl t htk.le
    have hA : 0 < A := by dsimp [A]; have := hF.C₁_pos; positivity
    have h₁ := Levels.OneStepDropsAlongARun.remainder_term_le hA hs ((le_max_right _ _).trans ((le_max_right _ _).trans hX))
    have h₂ := Levels.OneStepDropsAlongARun.second_term_le hs (hF.secondStep_le t)
      ((le_max_left _ _).trans hX) ((le_max_left _ _).trans ((le_max_right _ _).trans hX))
    linarith [(abs_le.mp hrm).2, (abs_le.mp h₂).1]
  intro i hi
  have hprefix : ∀ n, i ≤ n → n ≤ k →
      (∑ t ∈ Finset.Ico i n, a t) - s/4*((n:ℝ)-i) ≤ x i - x n := by
    intro n hn
    induction n,hn using Nat.le_induction with
    | base => simp
    | succ n hin ih =>
        intro hn
        rw [Finset.sum_Ico_succ_top hin, Nat.cast_succ]
        have hp := ih (Nat.le_of_succ_le hn)
        have hstep := hs₁ n hn
        linarith
  have h₁ := hprefix k hi.le le_rfl
  have h₂ := hk i hi
  change s/2*((k:ℝ)-i) ≤ ∑ t ∈ Finset.Ico i k, a t at h₂
  have hinc : (1:ℝ) ≤ (k:ℝ)-i := by
    have hh : (i:ℝ)+1 ≤ (k:ℝ) := by exact_mod_cast (show i+1 ≤ k from hi)
    linarith
  rw [he i hi.le]
  change P + s/4 ≤ x i
  nlinarith [mul_nonneg hs.le (sub_nonneg.mpr hinc)]

/-- Realize the recurrent interval's upper endpoint as a passage threshold
at an allowed coupling, using the release's inverse-square parametrization. -/
theorem exists_coupling_at_threshold {Bs γ W : ℝ} (hγ : 0 < γ)
    (hW : Bs + (γ⁻¹)^2 + 1 ≤ W) :
    ∃ G ∈ Ioc (0 : ℝ) γ, SequencePassage.passageThreshold Bs G = W := by
  have hdiff : 0 < W - Bs := by linarith [sq_nonneg γ⁻¹]
  let G := (Real.sqrt (W - Bs))⁻¹
  have hz : γ⁻¹ ≤ Real.sqrt (W - Bs) :=
    (Real.le_sqrt (inv_pos.mpr hγ).le hdiff.le).2 (by linarith)
  refine ⟨G, ⟨inv_pos.mpr (Real.sqrt_pos.mpr hdiff), ?_⟩, ?_⟩
  · simpa [G] using inv_anti₀ (inv_pos.mpr hγ) hz
  · dsimp [SequencePassage.passageThreshold, G]
    rw [inv_zpow', neg_neg, zpow_two, Real.mul_self_sqrt hdiff.le]
    ring

/-- Invert the inverse-coupling slope in the units of the release export. -/
theorem coupling_limit_of_beta_limit {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+}
    (hβ : Tendsto (fun j => betaAt L M (K j) g₀ / ((K j : ℝ) * Real.log L))
      atTop (𝓝 (11 / (3 * Real.pi ^ 2)))) :
    Tendsto (fun j => renormalizedBareCoupling L M (K j) g₀ ^ 2 * (K j : ℝ) * Real.log L)
      atTop (𝓝 (3 * Real.pi ^ 2 / 11)) := by
  have h := hβ.inv₀ (by positivity)
  rw [show (11 / (3 * Real.pi ^ 2) : ℝ)⁻¹ = 3 * Real.pi ^ 2 / 11 by rw [inv_div]] at h
  apply h.congr
  intro j
  change (((renormalizedBareCoupling L M (K j) g₀ ^ 2)⁻¹ / ((K j : ℝ) * Real.log L))⁻¹) = _
  rw [inv_div, div_eq_mul_inv, inv_inv]
  ring

/-- The table is chosen together with M and δ, before the physical coupling,
passing set, or side. Every infinite intersection with its records supports a
fresh full fixed-observable extraction, with all cutoffs in that intersection. -/
theorem su2_fixed_observable_selection_on_records :
    ∃ L₀ : ℕ, ∀ L : ℕ, Odd L → L₀ ≤ L →
      ∃ (M : ℕ+) (δ : ℝ) (a : ℕ → ℝ) (c : ℝ),
        8 ≤ PeriodicLattice.torusSide L M ∧ 0 < δ ∧
        (∀ᶠ k : ℕ in atTop, ∀ g₀ ∈ Ioo (0 : ℝ) δ,
          IsLeast {t : ℝ | 0 < t ∧ referenceResponse L M k (t^2)⁻¹ = fixedPhysicalLevel g₀}
            (renormalizedBareCoupling L M k g₀)) ∧
        CouplingFlow.HasAverageSlope a (CouplingFlow.slopeConst L) c ∧
        ∀ g₀ ∈ Ioo (0 : ℝ) δ, ∀ A : Set ℕ,
          (A ∩ recordCutoffs a (CouplingFlow.slopeConst L)).Infinite →
          ∃ K v ν S X₂ X₄, FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧
            (∀ j, (K j : ℕ) ∈ A ∩ recordCutoffs a (CouplingFlow.slopeConst L)) ∧
            ∀ ℓ, 0 < ℓ → 1024 ∣ ℓ → A ⊆ passingCutoffs L M g₀ ℓ →
              HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S) := by
  obtain ⟨L₀, head⟩ := bare_root_with_window_data
    ((noEscapingTables_of_stageDecay stopped_covariance_vanishes).and refined_tables)
  refine ⟨L₀, fun L ho hL₀ => ?_⟩
  obtain ⟨T,y,Kr,lam,cr,Bs,γ,c₅,speed,CT,c,Nw,hL,havg,hRun,⟨hno,href⟩,hγ,_,conditions,root⟩ :=
    head L ho hL₀
  subst L
  let L := (T.stepParameters y).side
  let p := T.stepParameters y
  have hadm : Conventions.IsAdmissibleBlockingFactor p.side :=
    ⟨hRun.adm.L_odd, (by have := hRun.adm.L_ge; change 13 ≤ T.side; omega)⟩
  let s := CouplingFlow.slopeConst L
  have hs : 0 < s := by
    have hh : 1 < L := by change 1 < p.side; have := hadm.2; omega
    have hl := Real.log_pos (show 1 < (L:ℝ) by exact_mod_cast hh)
    dsimp only [s,CouplingFlow.slopeConst]; positivity
  obtain ⟨X, hdrop⟩ := drop_at_record hs hRun href
  let H := max X (Bs + (γ⁻¹)^2 + 1)
  obtain ⟨M,δ,hM,hδ,hroots⟩ := root H
  refine ⟨M, δ, _, c, hM, hδ, hroots.mono (fun _ hj g₀ hg₀ => (hj g₀ hg₀).1),
    havg, fun g₀ hg₀ A hA => ?_⟩
  have hcold := hno Kr lam cr hRun M
  have hfreq : ∃ᶠ k : ℕ in atTop, k ∈ A ∩ recordCutoffs (FamilyNorms.ParameterAssignment.oneLoop T) s :=
    Nat.frequently_atTop_iff_infinite.mpr hA
  obtain ⟨w,hw,hboth⟩ := extraction_of_frequently_atTop
    ((hfreq.and_eventually hroots).and_eventually (eventually_ge_atTop 1))
  let K (j : ℕ) : ℕ+ := ⟨w j, (hboth j).2⟩
  let g (j : ℕ) := renormalizedBareCoupling L M (K j) g₀
  let b (j : ℕ) := (g j ^ 2)⁻¹
  let P (j : ℕ) := TotalDensityFlow.coupling p (b j) (K j)
  have hdata j : IsLeast {t : ℝ | 0<t ∧ referenceResponse L M (K j) (t^2)⁻¹ = fixedPhysicalLevel g₀} (g j) ∧
      b j ∈ runDomain T y (K j) ∧ IsTunedAt T y (P j) (K j) (b j) ∧ H ≤ P j :=
    (hboth j).1.2 g₀ hg₀
  have hβ j : 0 < b j := inv_pos.mpr (sq_pos_of_pos (hdata j).1.1.1)
  let f (j : ℕ) := referenceResponse L M (K j) (b j)
  have heq j : f j = fixedPhysicalLevel g₀ := (hdata j).1.1.2
  have hpos := fixedPhysicalLevel_pos hg₀.1
  have hc (e : ℕ → ℕ) (he : StrictMono e) (hesc : Tendsto (P ∘ e) atTop atTop) :
      Tendsto (f ∘ e) atTop (𝓝 0) :=
    (hcold _ hpos (w ∘ e) (b ∘ e) (hw.comp he) (fun i => hβ (e i))
      (fun i => (hdata (e i)).2.1) (fun i => (hdata (e i)).2.2.1) (fun i => heq (e i)) hesc).elim
  obtain ⟨W,hW,hwin⟩ := ReferenceCalibration.fixed_window_of_positive_reference P f hpos
    (show 0 < s/4 by positivity) (fun j => (hdata j).2.2.2) heq hc
  have hWX : Bs + (γ⁻¹)^2 + 1 ≤ W := (le_max_right ..).trans hW
  obtain ⟨G, hG, hth⟩ := exists_coupling_at_threshold hγ hWX
  have hp : ∃ᶠ j in atTop, TotalDensitySystem.IsFirstPassagePair p Bs G (K j) (b j) := by
    refine hwin.mono fun j hj => ?_
    have hd := (hdata j).2.2.1
    have hdef := (total_flow_of_above_total expansion_gives_total_flow total_density_flow_unique hRun hd.1).1
    have hgap := hdrop (w j) (hboth j).1.1.2 (b j) (P j) ((le_max_left ..).trans (hdata j).2.2.2) hd
    have hprior (i : ℕ) (hi : i < K j) : W < TotalDensityFlow.coupling p (b j) i := hj.2.trans_le (hgap i hi)
    change TotalDensityFlow.IsDefinedUpTo p (b j) (K j) ∧
      SequencePassage.passageThreshold Bs G ≤ b j ∧ P j ≤ SequencePassage.passageThreshold Bs G ∧
        ∀ i < (K j:ℕ), SequencePassage.passageThreshold Bs G < TotalDensityFlow.coupling p (b j) i
    rw [hth]
    exact ⟨hdef,(hprior 0 (K j).pos).le,hj.1,hprior⟩
  obtain ⟨φ,m,ν,S,X₂,X₄,hφ,_,hν,hm,hslope,htail⟩ :=
    su2_continuum_limit_of_frequent_passage os_axioms_for_components hadm (conditions G hG) K b hw.tendsto_atTop hβ hp
  have hKs : StrictMono K := fun i j hij => show w i < w j from hw hij
  have hlimit : FixedObservableWitnesses L M g₀ (K ∘ φ) m ν S X₂ X₄ := by
    refine ⟨hKs.comp hφ, fun j => (hdata (φ j)).1, ?_, hν, hm, hslope, htail⟩
    exact coupling_limit_of_beta_limit (K := K ∘ φ) hslope
  refine ⟨K ∘ φ, m, ν, S, X₂, X₄, hlimit, fun j => (hboth (φ j)).1.1, ?_⟩
  intro ℓ hℓ hd hpass
  apply Purity.massGap_of_purity hadm hlimit.inputs
  exact ⟨hℓ, hd, Frequently.of_forall (fun j => hpass (hboth (φ j)).1.1.1)⟩

/-- One calibrated finite block length suffices. If arbitrarily late whole
blocks pass, all witnesses can be chosen inside any such prescribed set A. -/
theorem su2_fixed_observable_gap_of_passing_blocks :
    FixedObservableLimit (fun L M g₀ => ∃ d : ℕ,
      ∀ (ℓ : ℕ) (A : Set ℕ), 0 < ℓ → 1024 ∣ ℓ → A ⊆ passingCutoffs L M g₀ ℓ →
        (∃ᶠ n : ℕ in atTop, Icc n (n + d) ⊆ A) →
        ∃ K v ν S X₂ X₄, (∀ j, (K j : ℕ) ∈ A) ∧
          FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧
          HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S)) := by
  obtain ⟨L₀, h⟩ := su2_fixed_observable_selection_on_records
  refine ⟨max L₀ 13, fun L hodd hL => ?_⟩
  obtain ⟨M, δ, a, c, hM, hδ, hroots, havg, hsel⟩ :=
    h L hodd ((le_max_left ..).trans hL)
  have hlarge : 13 ≤ L := (le_max_right ..).trans hL
  have hlog := Real.log_pos (show 1 < (L : ℝ) by exact_mod_cast (show 1 < L by omega))
  have hs : 0 < CouplingFlow.slopeConst L := by unfold CouplingFlow.slopeConst; positivity
  obtain ⟨d, hblock⟩ := record_in_every_block hs havg
  refine ⟨M, δ, hM, hδ, hroots, fun g₀ hg₀ => ⟨d, fun ℓ A hℓ hd hpass hblocks => ?_⟩⟩
  have hmeet : ∃ᶠ k : ℕ in atTop, k ∈ A ∩ recordCutoffs a (CouplingFlow.slopeConst L) := by
    apply frequently_atTop.2
    intro N
    obtain ⟨n, hn, hsub⟩ := frequently_atTop.1 hblocks N
    obtain ⟨k, hk, hr⟩ := hblock n
    exact ⟨k, hn.trans hk.1, hsub hk, hr⟩
  obtain ⟨K, v, ν, S, X₂, X₄, hw, hmem, hgap⟩ :=
    hsel g₀ hg₀ A (Nat.frequently_atTop_iff_infinite.mp hmeet)
  exact ⟨K, v, ν, S, X₂, X₄, fun j => (hmem j).1, hw, hgap ℓ hℓ hd hpass⟩

/-- The endpoint may lie just below a fixed threshold. The first crossing then
occurs at most a bounded number of steps earlier. This is the varying-endpoint
form of the release's `tuned_first_passage_index` (trajectory check, BND-2). -/
theorem passage_before_endpoint {T : RenormalizationStepParameters.ParameterAssignment}
    {y P b Bs G W lam cr : ℝ} {Kr : WeightedResponses.ResponseParameters} {k : ℕ}
    (hr : RunTable T y Kr lam cr) (ht : IsTunedAt T y P k b)
    (hW : SequencePassage.passageThreshold Bs G = W) (hwin : P ≤ W ∧ W < P + 1)
    (hk : runDepth lam (cr + 1) ≤ k) :
    ∃ J : ℕ+, (J : ℕ) ≤ k ∧ k - (J : ℕ) < runDepth lam (cr + 1) ∧
      TotalDensitySystem.IsFirstPassagePair (T.stepParameters y) Bs G J b := by
  classical
  let x := TotalDensityFlow.coupling (T.stepParameters y) b
  have hx : x k = P := ht.2
  have ha := (above_iff_total expansion_gives_total_flow total_density_flow_unique hr).mp ht.1
  have agree := (total_flow_of_above_total expansion_gives_total_flow total_density_flow_unique hr ht.1).2
  have descent (i : ℕ) (hi : i ≤ k) : lam * ((k : ℝ) - i) - cr ≤ x i - P := by
    have h := hr.descent b ha.1 k ha.2 i hi
    change lam * ((k : ℝ) - i) - cr ≤
      flowCouplings (T.stepParameters y) b i - flowCouplings (T.stepParameters y) b k at h
    rwa [← agree i hi, ← agree k le_rfl, ht.2] at h
  have start : W < x 0 := by
    have d := descent 0 (Nat.zero_le _)
    simp only [Nat.cast_zero, sub_zero] at d
    have bound := FirstPassageOfATunedPair.lt_mul_runDepth (c₅ := cr + 1) hr.lam_pos
    have mul := mul_le_mul_of_nonneg_left (show (runDepth lam (cr + 1) : ℝ) ≤ k by exact_mod_cast hk)
      hr.lam_pos.le
    linarith [hwin.2]
  have hex : ∃ i, x i ≤ W := ⟨k, hx ▸ hwin.1⟩
  let j := Nat.find hex
  have crossed : x j ≤ W := Nat.find_spec hex
  have prior (i : ℕ) (hi : i < j) : W < x i := lt_of_not_ge (Nat.find_min hex hi)
  have hpos : 0 < j := by
    by_contra! hz
    have hzero : j = 0 := by omega
    exact (not_lt_of_ge (hzero ▸ crossed)) start
  have hj : j ≤ k := Nat.find_min' hex (hx ▸ hwin.1)
  have hdist : k - j < runDepth lam (cr + 1) := by
    apply FirstPassageOfATunedPair.sub_lt_runDepth hr.lam_pos hj
    linarith [descent j hj, hwin.2]
  have subrun := (total_flow_of_above_total expansion_gives_total_flow total_density_flow_unique hr
    (show y ≤ b ∧ ∀ i < j, y ≤ x i from ⟨ht.1.1, fun i hi => ht.1.2 i (hi.trans_le hj)⟩)).1
  have hx0 : x 0 = b := agree 0 (Nat.zero_le _)
  refine ⟨⟨j, hpos⟩, hj, hdist, ?_⟩
  change TotalDensityFlow.IsDefinedUpTo (T.stepParameters y) b j ∧
    SequencePassage.passageThreshold Bs G ≤ b ∧ x j ≤ SequencePassage.passageThreshold Bs G ∧
    ∀ i < j, SequencePassage.passageThreshold Bs G < x i
  rw [hW]
  exact ⟨subrun, hx0 ▸ start.le, crossed, prior⟩

/-- The asymptotic-freedom coefficient also holds at the original cutoff when
the first-passage index differs from it by one fixed integer. Both ratios use
the least-root bare coupling of the original cutoff. -/
theorem coupling_limits_at_offset {p : TorusLumps.StepParameters} {M r Nw : ℕ}
    {g₀ Bs c₅ lam CT G : ℝ} {K J : ℕ → ℕ+} (hL : Conventions.IsAdmissibleBlockingFactor p.side)
    (hc : TotalDensitySystem.CouplingConditions p Bs c₅ lam Nw CT G) (hJ : StrictMono J)
    (hadd : ∀ j, (J j : ℕ) + r = K j)
    (hpass : ∀ j, TotalDensitySystem.IsFirstPassagePair p Bs G (J j) (betaAt p.side M (K j) g₀)) :
    Tendsto (fun j => renormalizedBareCoupling p.side M (K j) g₀ ^ 2 * (K j : ℝ) * Real.log p.side)
        atTop (𝓝 (3 * Real.pi ^ 2 / 11)) ∧
    Tendsto (fun j => betaAt p.side M (K j) g₀ / ((K j : ℝ) * Real.log p.side))
        atTop (𝓝 (11 / (3 * Real.pi ^ 2))) := by
  obtain ⟨ε, hε, herr⟩ := hc.passage.asymptotically_free
  have hnat : StrictMono fun j => (J j : ℕ) := fun _ _ hij => hJ hij
  have hlog := Real.log_pos (show 1 < (p.side : ℝ) by
    exact_mod_cast (show 1 < p.side by have := hL.2; omega))
  have hr : Tendsto (fun j => betaAt p.side M (K j) g₀ /
      Real.log (1 / PeriodicLattice.meshSize p.side ((J j : ℕ) : ℤ)))
      atTop (𝓝 SystemsWithFiveBounds.asymptoticFreedomSlope) := by
    rw [tendsto_iff_norm_sub_tendsto_zero]
    exact squeeze_zero (fun _ => norm_nonneg _)
      (fun j => herr _ _ (J j).pos (hpass j)) (hε.comp hnat.tendsto_atTop)
  have hfrac := (tendsto_natCast_div_add_atTop (r : ℝ)).comp hnat.tendsto_atTop
  have hraw : Tendsto (fun j => betaAt p.side M (K j) g₀ / ((K j : ℝ) * Real.log p.side))
      atTop (𝓝 (11 / (3 * Real.pi ^ 2))) := by
    have hslope : SystemsWithFiveBounds.asymptoticFreedomSlope = 11 / (3 * Real.pi ^ 2) := by
      unfold SystemsWithFiveBounds.asymptoticFreedomSlope
      field_simp
      ring
    rw [hslope] at hr
    have h := hr.mul hfrac
    simp only [mul_one] at h
    apply h.congr
    intro j
    change betaAt p.side M (K j) g₀ / Real.log (1 / PeriodicLattice.meshSize p.side ((J j : ℕ) : ℤ)) *
      ((J j : ℝ) / ((J j : ℝ) + r)) = _
    rw [NonGaussianLimits.log_inv_meshSize (by have := hL.2; omega : 0 < p.side)]
    have he : (K j : ℝ) = (J j : ℝ) + r := by exact_mod_cast (hadd j).symm
    have hj : (0 : ℝ) < (J j : ℕ) := by exact_mod_cast (J j).pos
    have hpos : (0 : ℝ) < (J j : ℕ) + (r : ℝ) := by positivity
    rw [he]
    field_simp
  exact ⟨coupling_limit_of_beta_limit hraw, hraw⟩

/-- For every infinite set, keep the original least roots, both coupling
limits and infinite-volume states on that set. A single offset r relates its
cutoffs to first passages at precisely the same bare inverse couplings. -/
theorem su2_fixed_observable_cutoffs_at_fixed_offset :
    FixedObservableLimit (fun L M g₀ => ∀ A : Set ℕ, A.Infinite →
      ∃ (K J : ℕ → ℕ+) (ν : CutoffStates L K) (r : ℕ) (p : TorusLumps.StepParameters)
        (Bs c₅ lam CT G : ℝ) (Nw : ℕ),
        p.side = L ∧ TotalDensitySystem.CouplingConditions p Bs c₅ lam Nw CT G ∧
        StrictMono K ∧ StrictMono J ∧ (∀ j, (K j : ℕ) ∈ A) ∧ (∀ j, (J j : ℕ) + r = K j) ∧
        (∀ j, IsLeast {t : ℝ | 0 < t ∧ referenceResponse L M (K j) (t ^ 2)⁻¹ = fixedPhysicalLevel g₀}
          (renormalizedBareCoupling L M (K j) g₀)) ∧
        (∀ j, TotalDensitySystem.IsFirstPassagePair p Bs G (J j) (betaAt L M (K j) g₀)) ∧
        (∀ j, InfiniteLattice.IsInfiniteVolumeLimit L (K j) (betaAt L M (K j) g₀) (ν j)) ∧
        Tendsto (fun j => renormalizedBareCoupling L M (K j) g₀ ^ 2 * (K j : ℝ) * Real.log L)
          atTop (𝓝 (3 * Real.pi ^ 2 / 11)) ∧
        Tendsto (fun j => betaAt L M (K j) g₀ / ((K j : ℝ) * Real.log L))
          atTop (𝓝 (11 / (3 * Real.pi ^ 2)))) := by
  obtain ⟨L₀, head⟩ := bare_root_with_window_data
    (noEscapingTables_of_stageDecay stopped_covariance_vanishes)
  refine ⟨L₀, fun L ho hlarge => ?_⟩
  obtain ⟨T, y, Kr, lam, cr, Bs, γ, c₅, speed, CT, c, Nw, hL, _, hRun, hno, hγ, _,
    conditions, root⟩ := head L ho hlarge
  subst L
  let p := T.stepParameters y
  let L := p.side
  have hadm : Conventions.IsAdmissibleBlockingFactor p.side :=
    ⟨hRun.adm.L_odd, by have := hRun.adm.L_ge; change 13 ≤ T.side; omega⟩
  let H := Bs + (γ⁻¹)^2 + 1
  obtain ⟨M, δ, hM, hδ, hroots⟩ := root H
  refine ⟨M, δ, hM, hδ, hroots.mono (fun _ hj g₀ hg₀ => (hj g₀ hg₀).1), fun g₀ hg₀ A hA => ?_⟩
  have hfreq : ∃ᶠ k : ℕ in atTop, k ∈ A := Nat.frequently_atTop_iff_infinite.mpr hA
  obtain ⟨w, hw, hboth⟩ := extraction_of_frequently_atTop
    ((hfreq.and_eventually hroots).and_eventually (eventually_ge_atTop (runDepth lam (cr + 1))))
  let b (j : ℕ) := betaAt L M (w j) g₀
  let P (j : ℕ) := TotalDensityFlow.coupling p (b j) (w j)
  have data j : IsLeast {t : ℝ | 0 < t ∧ referenceResponse L M (w j) (t ^ 2)⁻¹ = fixedPhysicalLevel g₀}
      (renormalizedBareCoupling L M (w j) g₀) ∧ b j ∈ runDomain T y (w j) ∧
      IsTunedAt T y (P j) (w j) (b j) ∧ H ≤ P j := (hboth j).1.2 g₀ hg₀
  have hβ j : 0 < b j := inv_pos.mpr (sq_pos_of_pos (data j).1.1.1)
  let f (j : ℕ) := referenceResponse L M (w j) (b j)
  have heq j : f j = fixedPhysicalLevel g₀ := (data j).1.1.2
  have hpos := fixedPhysicalLevel_pos hg₀.1
  have cold (e : ℕ → ℕ) (he : StrictMono e) (hesc : Tendsto (P ∘ e) atTop atTop) :
      Tendsto (f ∘ e) atTop (𝓝 0) :=
    (hno Kr lam cr hRun M _ hpos (w ∘ e) (b ∘ e) (hw.comp he) (fun i => hβ (e i))
      (fun i => (data (e i)).2.1) (fun i => (data (e i)).2.2.1) (fun i => heq (e i)) hesc).elim
  obtain ⟨W, hW, hwin⟩ := ReferenceCalibration.fixed_window_of_positive_reference P f hpos
    zero_lt_one (fun j => (data j).2.2.2) heq cold
  obtain ⟨G, hG, threshold⟩ := exists_coupling_at_threshold hγ hW
  obtain ⟨e, he, hwindow⟩ := extraction_of_frequently_atTop hwin
  choose jStop hle hdist hpass using fun n => passage_before_endpoint hRun
    (data (e n)).2.2.1 threshold (hwindow n) (hboth (e n)).2
  obtain ⟨r, _, hfr⟩ := LimitsOfATunedSequence.exists_frequently_eq_of_forall_lt hdist
  obtain ⟨φ, hφ, hroff⟩ := extraction_of_frequently_atTop hfr
  let J (n : ℕ) := jStop (φ n)
  have hadd (n : ℕ) : (J n : ℕ) + r = w (e (φ n)) := by
    have h₁ := hle (φ n)
    have h₂ := hroff n
    dsimp only [J]
    omega
  let K (n : ℕ) : ℕ+ := ⟨w (e (φ n)), by have := hadd n; have := (J n).pos; omega⟩
  have hK : StrictMono K := fun i j hij => hw (he (hφ hij))
  have hJ : StrictMono J := by
    intro i j hij
    have h := hw (he (hφ hij))
    change (J i : ℕ) < (J j : ℕ)
    have hi := hadd i
    have hj := hadd j
    omega
  have hp j : TotalDensitySystem.IsFirstPassagePair p Bs G (J j) (betaAt L M (K j) g₀) := hpass (φ j)
  have hstate (j : ℕ) := torus_limit_sets_nonempty L (K j) hadm (K j).pos _ (hβ (e (φ j)))
  simp only [torus_limits_eq_infinite_volume_limits _ _ _ (show 2 ≤ L by have := hadm.2; change 13 ≤ L at this; omega)] at hstate
  choose ν hν using hstate
  exact ⟨K, J, ν, r, p, Bs, c₅, speed, CT, G, Nw, rfl, conditions G hG, hK, hJ,
    fun n => (hboth (e (φ n))).1.1, hadd, fun j => (data (e (φ j))).1, hp, hν,
    coupling_limits_at_offset hadm (conditions G hG) hJ hadd hp⟩

end GapChain.PurIo

#print axioms GapChain.PurIo.record_in_every_block
#print axioms GapChain.PurIo.averageSlope_can_miss_infinite_set
#print axioms GapChain.PurIo.drop_at_record
#print axioms GapChain.PurIo.exists_coupling_at_threshold
#print axioms GapChain.PurIo.coupling_limit_of_beta_limit
#print axioms GapChain.PurIo.su2_fixed_observable_selection_on_records
#print axioms GapChain.PurIo.su2_fixed_observable_gap_of_passing_blocks
#print axioms GapChain.PurIo.passage_before_endpoint
#print axioms GapChain.PurIo.coupling_limits_at_offset
#print axioms GapChain.PurIo.su2_fixed_observable_cutoffs_at_fixed_offset
