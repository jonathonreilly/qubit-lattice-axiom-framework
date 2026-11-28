import GapChain.Stage0
import GapChain.Stage2
import GapChain.Stage3b
import GapChain.Stage4

/-!
# Conditional gap at the fixed-observable continuum witnesses

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, supply the fixed-observable release. This assembles the lane's proved
stages at the interfaces of row 1652, following design and check rows 1457–1458.
-/

set_option autoImplicit false
set_option Elab.async false

open Filter YangMills YangMills.Construction
open SeparatedTuples LimitTheorem

namespace GapChain.Final

variable {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K} {S : CumulantFamily}

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
  apply Stage4.kappaSeed_of_neutralPhysicalSeed Γ (hβ j) hfour hlarge
  -- Construct the physical seed with Stage 4's tail at max 3 (2 * w).
  obtain ⟨w, hw, hwSide, hrank⟩ := htest Γ hΓ
  obtain ⟨htop, hsum, htail⟩ := (Stage4.neutralTail_of_rankOneAtTime Γ (hβ j) hw hrank).2
  refine ⟨max 3 (2 * w), le_max_left .., ?_, htop, hsum, htail.trans (by norm_num)⟩
  rcases le_total 3 (2 * w) with hle | hle
  · rw [max_eq_right hle]
    omega
  · rw [max_eq_left hle]
    exact (by decide : 512 * 3 ≤ 2 ^ 70).trans hlarge

example : type_of% @GapChain.kappaSeedAlong_of_mNeutral := @Final.kappaSeedAlong_of_mNeutral

theorem expClusters_of_mNeutral (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : MNeutralAlong L M g₀ ℓ K) :
    ExpClusters L K ν (gapRate ℓ) :=
  Stage3b.expClusters_of_kappaSeed hL h
    (Final.kappaSeedAlong_of_mNeutral hL h.strictMono h.beta_pos hs)

example : type_of% @GapChain.expClusters_of_mNeutral := @Final.expClusters_of_mNeutral

theorem massGap_of_mNeutral (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : MNeutralAlong L M g₀ ℓ K) :
    HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S) := by
  have hm := gapRate_pos hs.1
  have hgap := Stage2.massGap_of_expClusters hL h hm (Final.expClusters_of_mNeutral hL h hs)
  exact ⟨hgap, hgap.uniqueVacuum hm⟩

example : type_of% @GapChain.massGap_of_mNeutral := @Final.massGap_of_mNeutral

/-- Choose the release witnesses once, before quantifying over the physical seed side. -/
theorem su2_fixed_observable_gap_of_mNeutral :
    FixedObservableLimit FixedObservableContinuumWithGap := by
  obtain ⟨L₀, h⟩ := YangMills.su2_fixed_observable_continuum_limit
  refine ⟨max L₀ 13, fun L hodd hL => ?_⟩
  obtain ⟨M, δ, hside, hδ, hall, hlim⟩ := h L hodd ((le_max_left ..).trans hL)
  have hadm : Conventions.IsAdmissibleBlockingFactor L := ⟨hodd, (le_max_right ..).trans hL⟩
  refine ⟨M, δ, hside, hδ, hall, fun g₀ hg₀ => ?_⟩
  obtain ⟨K, v, ν, S, X₂, X₄, hw⟩ :=
    (fixedObservableContinuum_iff L M g₀).mp (hlim g₀ hg₀)
  exact ⟨K, v, ν, S, X₂, X₄, hw, fun _ hs =>
    Final.massGap_of_mNeutral hadm hw.inputs (hs.along hw.inputs.strictMono)⟩

example : type_of% @GapChain.su2_fixed_observable_gap_of_mNeutral := @Final.su2_fixed_observable_gap_of_mNeutral

end GapChain.Final

#print axioms GapChain.Final.kappaSeedAlong_of_mNeutral
#print axioms GapChain.Final.expClusters_of_mNeutral
#print axioms GapChain.Final.massGap_of_mNeutral
#print axioms GapChain.Final.su2_fixed_observable_gap_of_mNeutral
#print axioms YangMills.su2_fixed_observable_continuum_limit
