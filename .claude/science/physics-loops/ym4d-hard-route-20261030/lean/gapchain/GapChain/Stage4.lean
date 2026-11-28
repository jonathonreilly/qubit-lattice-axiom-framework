import GapChain.Stage0
import GapChain.Stage3

/-!
# Neutral and Pfaffian seeds on a single Wilson cube

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
supply the transfer and the Peter–Weyl normalization. Stage 3 identifies the
positive spectral slots with the twisted Wilson integrals. We use the rank-one
estimate of row 1356 and the two-flux argument of row 1161, with the conventions
of design rows 1457–1458 and the exact interfaces of row 1652.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open MeasureTheory Filter
open scoped BigOperators InnerProductSpace ComplexConjugate
open YangMills YangMills.Construction TransferOperators SpinHarmonics TheStatementsProvedTogether
open GapChain.Stage3
open GapChain.Wilson (Dir Sides)

namespace GapChain.Stage4

local notation "μt" => TimeAxis.timeIdx

/-- Include the zero eigenspace when representing the positive slots on the release slice. -/
structure SectorBasis {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (T : H →L[ℂ] H) (weight : ℕ → ℝ) where
  indices : Set H
  basis : HilbertBasis indices ℂ H
  value : indices → ℝ
  nonneg : ∀ i, 0 ≤ value i
  acts : ∀ i, T (basis i) = (value i : ℂ) • basis i
  moments : ∀ a : ℕ, 2 ≤ a → HasSum (fun i => value i ^ a) (weight a)

theorem releaseSectorBasis (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (χ m : Flux) :
    Nonempty (SectorBasis (magneticTransfer Γ hβ m * electricProj Γ χ)
      (fun a => sectorWeight β (boxSides (cube Γ.side) a) χ m)) := by
  classical
  let T := magneticTransfer Γ hβ m * electricProj Γ χ
  obtain ⟨hc,hp⟩ := releaseSector_spectral Γ hβ χ m
  obtain ⟨w,b,j,hj,he,hz⟩ := exists_positive_slot_basis T hc hp
  let v := Function.extend j (fun i : Wilson.PositiveSlot T => i.1.val) 0
  have atSlot (i : Wilson.PositiveSlot T) : v (j i) = i.1.val := hj.extend_apply _ _ _
  have off (i : w) (hi : i ∉ Set.range j) : v i = 0 := Function.extend_apply' _ _ _ hi
  refine ⟨⟨w, b, v, ?_, ?_, ?_⟩⟩
  · intro i
    by_cases hi : i ∈ Set.range j
    · obtain ⟨k,rfl⟩ := hi
      exact (atSlot k).symm ▸ k.1.property.le
    · exact (off i hi).symm ▸ le_rfl
  · intro i
    by_cases hi : i ∈ Set.range j
    · obtain ⟨k,rfl⟩ := hi
      rw [atSlot, he]
    · rw [off i hi, hz i hi, Complex.ofReal_zero, zero_smul]
  · intro a ha
    apply (hj.hasSum_iff (fun i hi => show v i ^ a = 0 by rw [off i hi, zero_pow (by omega : a ≠ 0)])).1
    exact (release_sector_moments Γ hβ χ m a ha).congr_fun fun i => by simp only [Function.comp_apply,atSlot]

/-- Change from a positive diagonal spectral sum to the release's Peter–Weyl trace.
Absolute convergence follows by summing the nonnegative squared change-of-basis
coefficients in both orders. -/
theorem pwTrace_of_eigenbasis {J : Type} [Finite J] [Nonempty J]
    {I : Type*} (b : HilbertBasis I ℂ (HaarL2 J)) (A : HaarL2 J →L[ℂ] HaarL2 J)
    {v : I → ℝ} {s : ℝ} (hn : ∀ i, 0 ≤ v i)
    (he : ∀ i, A (b i) = (v i : ℂ) • b i) (hs : HasSum v s) :
    TraceSummablePW A ∧ tracePW A = (s : ℂ) := by
  let f (p : I × PeterWeylIndex J) : ℝ := v p.1 * ‖⟪peterWeylVec p.2, b p.1⟫_ℂ‖ ^ 2
  have hnon (p) : 0 ≤ f p := mul_nonneg (hn _) (sq_nonneg _)
  have rows (i : I) : HasSum (fun k => f (i,k)) (v i) := by
    have h := (ReflectionPositivityChain.peter_weyl_expansion J (b i)).2.2
    simpa only [f, b.orthonormal.norm_eq_one, one_pow, mul_one] using h.mul_left (v i)
  have allS : Summable f := (summable_prod_of_nonneg hnon).2
    ⟨fun i => (rows i).summable, by simpa only [(rows _).tsum_eq] using hs.summable⟩
  have total : HasSum f s := allS.hasSum_iff.mpr (by
    rw [allS.tsum_prod]; simpa only [fun i => (rows i).tsum_eq] using hs.tsum_eq)
  let d (k : PeterWeylIndex J) := ∑' i, f (i,k)
  have hd : HasSum d s := ((Equiv.prodComm _ _).hasSum_iff.mpr total).prod_fiberwise
    (fun k => (allS.prod_symm.prod_factor k).hasSum)
  have diag (k : PeterWeylIndex J) : (d k : ℂ) = peterWeylEntry A k k := by
    have hab := (((b.hasSum_repr (peterWeylVec k)).mapL A).mapL (innerSL ℂ (peterWeylVec k)))
    apply (Complex.hasSum_ofReal.mpr (allS.prod_symm.prod_factor k).hasSum).unique
    apply hab.congr_fun
    intro i
    change (↑(f (i,k)) : ℂ) = _
    simp only [map_smul, he, innerSL_apply_apply,
      b.repr_apply_apply, f, Complex.ofReal_mul, Complex.ofReal_pow]
    rw [← Complex.ofReal_pow, ← Complex.normSq_eq_norm_sq, ← Complex.mul_conj]
    rw [← inner_conj_symm (b i) (peterWeylVec k)]
    ring
  constructor
  · unfold TraceSummablePW
    have eqn (k) : ‖peterWeylEntry A k k‖ = d k := by
      rw [← diag, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (tsum_nonneg fun i => hnon (i,k))]
    simpa only [eqn] using hd.summable
  · exact ((Complex.hasSum_ofReal.mpr hd).congr_fun (fun k => (diag k).symm)).tsum_eq

theorem projected_power (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (χ m : Flux)
    {a : ℕ} (ha : 0 < a) :
    electricProj Γ χ * magneticTransfer Γ hβ m ^ a =
      (magneticTransfer Γ hβ m * electricProj Γ χ) ^ a := by
  have hc := magneticTransfer_commutes_proj Γ hβ m χ
  have hi : IsIdempotentElem (electricProj Γ χ) := by simpa [IsIdempotentElem] using electricProj_mul Γ χ χ
  obtain ⟨d,rfl⟩ := Nat.exists_eq_succ_of_ne_zero ha.ne'
  rw [hc.mul_pow, hi.pow_succ_eq, (hc.pow_left _).eq]

/-- Includes time two. The zero eigenspace contributes zero at every positive time. -/
theorem projectedTrace_eq_sectorWeight (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (χ m : Flux)
    (a : ℕ) (ha : 2 ≤ a) :
    let A := electricProj Γ χ * magneticTransfer Γ hβ m ^ a
    TraceSummablePW A ∧ tracePW A = (sectorWeight β (boxSides (cube Γ.side) a) χ m : ℂ) := by
  let := CubicTorusOperators.linkOrbits_nonempty Γ μt
  obtain ⟨B⟩ := releaseSectorBasis Γ hβ χ m
  dsimp only
  rw [projected_power Γ hβ χ m (by omega : 0 < a)]
  apply pwTrace_of_eigenbasis B.basis _ (v := fun i => B.value i ^ a)
    (fun i => pow_nonneg (B.nonneg i) _) _ (B.moments a ha)
  intro i
  rw [pow_apply_eigenvector _ (B.acts i), Complex.ofReal_pow]

/-- Positivity follows from the two-step Wilson integral, without identifying
the neutral and full top eigenvalues. -/
theorem periodicTransfer_norm_pos (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) :
    0 < ‖Γ.transfer μt β‖ := by
  let s := boxSides (cube Γ.side) 2
  have pos : 0 < sectorWeight β s zeroFlux zeroFlux :=
    (div_pos (Wilson.partition_pos β s) (by norm_num)).trans_le (partition_div_eight_le_neutral β s)
  by_contra! hn
  have hz : Γ.transfer μt β = 0 := norm_le_zero_iff.mp hn
  obtain ⟨_,he⟩ := projectedTrace_eq_sectorWeight Γ hβ zeroFlux zeroFlux 2 le_rfl
  rw [magneticTransfer_zero,hz,zero_pow (by decide : 2 ≠ 0),mul_zero] at he
  have eq : (0 : ℂ) = (sectorWeight β s zeroFlux zeroFlux : ℂ) := by
    simpa only [tracePW,peterWeylEntry,zero_apply,inner_zero_right,tsum_zero] using he
  exact pos.ne' (by exact_mod_cast eq.symm)

theorem neutralTail_iff_sectorWeight (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (a : ℕ) (ha : 2 ≤ a) (bound : ℝ) :
    NeutralTailLE Γ β a bound ↔
      sectorWeight β (boxSides (cube Γ.side) a) zeroFlux zeroFlux /
        ‖Γ.transfer μt β‖ ^ a - 1 ≤ bound := by
  have top := periodicTransfer_norm_pos Γ hβ
  obtain ⟨hs,ht⟩ := projectedTrace_eq_sectorWeight Γ hβ zeroFlux zeroFlux a ha
  rw [electricProj_zero, magneticTransfer_zero] at hs ht
  simp only [NeutralTailLE, top, hs, ht, Complex.ofReal_re, true_and]

theorem neutral_projection_norm_le (Γ : CubicPeriodSublattice) : ‖electricProj Γ zeroFlux‖ ≤ 1 := by
  let P := electricProj Γ zeroFlux
  have ht := CStarRing.norm_star_mul_self (x := P)
  have he : P * P = P := by simpa [P] using electricProj_mul Γ zeroFlux zeroFlux
  rw [(electricProj_isSelfAdjoint Γ zeroFlux).star_eq,he] at ht
  nlinarith only [ht,norm_nonneg P]

/-- The same normalized trace is bounded at every later integer time. The norm
estimate uses only contractivity of the centre projection. -/
theorem neutralTail_after_rankOne (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    {w : ℕ} (hw : 1 ≤ w) (h : RankOneAtTime Γ μt β w) (a : ℕ) (ha : 2 * w ≤ a) :
    NeutralTailLE Γ β a (4 / 21) := by
  let T := Γ.transfer μt β
  let P := electricProj Γ zeroFlux
  let S := T * P
  have top : 0 < ‖T‖ := periodicTransfer_norm_pos Γ hβ
  have normS : ‖S‖ ≤ ‖T‖ := (norm_mul_le T P).trans
    ((mul_le_mul_of_nonneg_left (neutral_projection_norm_le Γ) (norm_nonneg T)).trans_eq (mul_one _))
  obtain ⟨φ,c,hφ,hc,htest⟩ := h
  have hwP := projected_power Γ hβ zeroFlux zeroFlux (by omega : 0 < w)
  rw [magneticTransfer_zero] at hwP
  rw [← electricProj_zero, hwP] at htest
  obtain ⟨B⟩ := releaseSectorBasis Γ hβ zeroFlux zeroFlux
  rw [magneticTransfer_zero] at B
  let v := B.value
  have norm_col (i) : ‖(S ^ w) (B.basis i)‖ ^ 2 = v i ^ (2*w) := by
    rw [pow_apply_eigenvector S (B.acts i), norm_smul, B.basis.orthonormal.norm_eq_one,
      mul_one, norm_pow, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (B.nonneg i)]
    rw [mul_comm 2 w, pow_mul]
  have hs := B.moments (2*w) (by omega)
  have hsum : Summable (fun i => ‖(S ^ w) (B.basis i)‖ ^ 2) := by simpa only [norm_col] using hs.summable
  have m1 := lemmaM1_hsSq B.basis (S ^ w) hsum hφ hc htest
  simp only [hsSq, norm_col, v, hs.tsum_eq] at m1
  have normSq : ‖S ^ w‖ ^ 2 ≤ ‖T‖ ^ (2*w) := by
    rw [mul_comm 2 w,pow_mul]
    exact pow_le_pow_left₀ (norm_nonneg _) ((norm_pow_le' S hw).trans (pow_le_pow_left₀ (norm_nonneg S) normS _)) 2
  have base : sectorWeight β (boxSides (cube Γ.side) (2*w)) zeroFlux zeroFlux / ‖T‖ ^ (2*w) ≤ 25/21 := by
    apply (div_le_iff₀ (pow_pos top _)).2
    linarith only [m1,normSq]
  have atMost (i) : v i ≤ ‖T‖ := by
    have hle := S.le_opNorm (B.basis i)
    rw [B.acts, norm_smul, B.basis.orthonormal.norm_eq_one, mul_one, mul_one,
      Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (B.nonneg i)] at hle
    exact hle.trans normS
  have atTime (t : ℕ) (ht : 2 ≤ t) : HasSum (fun i => (v i / ‖T‖)^t)
      (sectorWeight β (boxSides (cube Γ.side) t) zeroFlux zeroFlux / ‖T‖ ^ t) := by
    simpa only [div_pow] using (B.moments t ht).div_const (‖T‖ ^ t)
  have mono := hasSum_le (fun i => pow_le_pow_of_le_one (div_nonneg (B.nonneg i) top.le)
    ((div_le_one top).2 (atMost i)) ha) (atTime a (by omega)) (atTime (2*w) (by omega))
  apply (neutralTail_iff_sectorWeight Γ hβ a (by omega) _).2
  change sectorWeight β _ _ _ / ‖T‖ ^ a - 1 ≤ 4/21
  linarith only [mono,base]

theorem neutralTail_of_rankOneAtTime (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    {w : ℕ} (hw : 1 ≤ w) (h : RankOneAtTime Γ μt β w) :
    NeutralTailLE Γ β (2 * w) (4 / 21) ∧ NeutralTailLE Γ β (max 3 (2 * w)) (4 / 21) :=
  ⟨neutralTail_after_rankOne Γ hβ hw h _ le_rfl,
    neutralTail_after_rankOne Γ hβ hw h _ (le_max_right ..)⟩

example : type_of% @GapChain.neutralTail_of_rankOneAtTime := @neutralTail_of_rankOneAtTime

/-- Change the time coordinate from 3 to a chosen coordinate of the four-torus. -/
def inFrame (i : Dir) (e m : Flux) : Flux × Flux :=
  match i.val with
  | 0 => ((e.1,m.2.2,m.2.1), (m.1,e.2.2,e.2.1))
  | 1 => ((m.2.2,e.2.1,m.1), (e.2.2,m.2.1,e.1))
  | 2 => ((m.2.1,m.1,e.2.2), (e.2.1,e.1,m.2.2))
  | _ => (e,m)

theorem inFrame_time (e m : Flux) : inFrame μt e m = (e,m) := rfl

theorem inFrame_planes : ∀ (i : Dir) (e m : Flux) (p : Wilson.Plane),
    joinTwist (inFrame i e m).1 (inFrame i e m).2 p =
      joinTwist e m (mapPlane (Equiv.swap μt i) p) := by decide

theorem raw_in_frame (β : ℝ) (s : Sides) (i : Dir) (e m : Flux) :
    twistedPartition β s (joinTwist e m) =
      ∑ χ : Flux, (character (inFrame i e m).1 χ : ℝ) *
        sectorWeight β (s ∘ Equiv.swap μt i) χ (inFrame i e m).2 := by
  rw [← twistedPartition_eq_sectorSum, funext (inFrame_planes i e m)]
  exact (twistedPartition_permute β s (Equiv.swap μt i) (joinTwist e m)).symm

/-- Coefficient after averaging over the *original* electric star and expanding
in the new time frame. The retained two-point projection has a positive trace. -/
def crossedCoeff (i : Dir) (m q r : Flux) : ℤ :=
  ∑ e : Flux, if (inFrame i e m).2 = r then character (inFrame i e m).1 q else 0

theorem crossed_neutral_sum (β : ℝ) (s : Sides) (i : Dir) (m : Flux) :
    8 * sectorWeight β s zeroFlux m =
      ∑ q : Flux, ∑ r : Flux, (crossedCoeff i m q r : ℝ) *
        sectorWeight β (s ∘ Equiv.swap μt i) q r := by
  let X := sectorWeight β (s ∘ Equiv.swap μt i)
  have row (q e : Flux) : (∑ r : Flux,
      ((if (inFrame i e m).2 = r then character (inFrame i e m).1 q else 0 : ℤ) : ℝ) * X q r)
      = (character (inFrame i e m).1 q : ℝ) * X q (inFrame i e m).2 := by
    simp only [Int.cast_ite,Int.cast_zero,ite_mul,zero_mul,Finset.sum_ite_eq,Finset.mem_univ,if_true]
  change 8 * sectorWeight β s zeroFlux m = ∑ q : Flux, ∑ r : Flux, (crossedCoeff i m q r : ℝ) * X q r
  simp only [sectorWeight, character_zero, Int.cast_one, one_mul, raw_in_frame β s i _ m,
    crossedCoeff, Int.cast_sum, Finset.sum_mul]
  rw [mul_div_cancel₀ _ (by norm_num : (8 : ℝ) ≠ 0)]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro q _
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro e _
  rw [row]
  dsimp [X,sectorWeight]

/-- Erasing the two static bits incident to the new time axis can only increase
each coefficient. Two frame changes erase all three magnetic bits. -/
theorem crossed_erasure : ∀ m q r : Flux,
    crossedCoeff 0 m q r ≤ crossedCoeff 0 (m.1,false,false) q r ∧
    crossedCoeff 1 (m.1,false,false) q r ≤ crossedCoeff 1 zeroFlux q r := by
  decide

theorem sectorWeight_le_periodicNeutral {β : ℝ} (hβ : 0 ≤ β) {s : Sides} (hs : ∀ i, 2 ≤ s i)
    (χ m : Flux) : sectorWeight β s χ m ≤ sectorWeight β s zeroFlux zeroFlux := by
  have step (i : Dir) (a b : Flux) (h : ∀ q r, crossedCoeff i a q r ≤ crossedCoeff i b q r) :
      sectorWeight β s zeroFlux a ≤ sectorWeight β s zeroFlux b := by
    have ineq : 8 * sectorWeight β s zeroFlux a ≤ 8 * sectorWeight β s zeroFlux b := by
      rw [crossed_neutral_sum β s i a, crossed_neutral_sum β s i b]
      exact Finset.sum_le_sum fun q _ => Finset.sum_le_sum fun r _ =>
        mul_le_mul_of_nonneg_right (by exact_mod_cast h q r)
          (sectorWeight_nonneg (hs ((Equiv.swap μt i) μt)) hβ q r)
    linarith only [ineq]
  exact (sectorWeight_le_neutral _ _ χ m).trans
    ((step 0 m _ fun q r => (crossed_erasure m q r).1).trans
      (step 1 _ zeroFlux fun q r => (crossed_erasure m q r).2))

/-- Physical normalized character moment. All magnetic backgrounds use the same
periodic release vacuum, even when their own top eigenvalues differ. -/
def sectorMoment (Γ : CubicPeriodSublattice) (β : ℝ) (χ m : Flux) (t : ℕ) : ℝ :=
  sectorWeight β (boxSides (cube Γ.side) t) χ m / ‖Γ.transfer μt β‖ ^ t

theorem cubeSides_ge_two (Γ : CubicPeriodSublattice) {t : ℕ} (ht : 2 ≤ t) :
    ∀ i, 2 ≤ boxSides (cube Γ.side) t i := by
  have hside := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp
    ⟨Γ.lattice,Γ.periods_eq⟩
  intro i
  fin_cases i <;> first | exact ht | exact le_trans (by decide : 2 ≤ 3) hside

theorem sectorMoment_bound (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    {u : ℕ} (hu : 2 ≤ u) (hs : NeutralTailLE Γ β u (1/2)) (χ m : Flux) :
    sectorMoment Γ β χ m u ≤ 3/2 := by
  have hn := div_le_div_of_nonneg_right (sectorWeight_le_periodicNeutral hβ.le (cubeSides_ge_two Γ hu) χ m)
    (pow_nonneg (norm_nonneg (Γ.transfer μt β)) u)
  have hh := (neutralTail_iff_sectorWeight Γ hβ u hu _).mp hs
  exact hn.trans (by linarith only [hh])

/-- Remove the single largest slot, counting multiplicity. Every remaining
slot is bounded at the short period because it and slot zero both occur in the trace. -/
theorem excited_slot_le {v : ℕ → ℝ} (hv : ∀ i, 0 ≤ v i) (hm : ∀ i, v i ≤ v 0)
    {u : ℕ} {c : ℝ} (hs : HasSum (fun i => v i ^ u) c) (hc : c ≤ 3/2) (i : ℕ) (hi : i ≠ 0) :
    v i ^ u ≤ 3/4 := by
  have two := hs.summable.sum_le_tsum ({0,i} : Finset ℕ) (fun j _ => pow_nonneg (hv j) u)
  rw [Finset.sum_pair hi.symm, hs.tsum_eq] at two
  linarith only [two,hc,pow_le_pow_left₀ (hv i) (hm i) u]

/-- Spend `k` full short periods on the spectral ratio. The unused steps cost
at most one in periodic-vacuum units. -/
theorem tail_at_multiple {v : ℕ → ℝ} {u t k : ℕ} (ht : (k+1)*u ≤ t)
    (hn : ∀ i, 0 ≤ v i) (hm : ∀ i, v i ≤ v 0) (h1 : ∀ i, v i ≤ 1)
    {a b : ℝ} (hs : HasSum (fun i => v i ^ u) a) (ha : a ≤ 3/2)
    (hl : HasSum (fun i => v i ^ t) b) :
    b - v 0 ^ t ≤ (3/2 : ℝ) * (3/4)^k := by
  have terms (i : ℕ) : v i ^ t - (if i = 0 then v 0 ^ t else 0) ≤ (3/4 : ℝ)^k * v i ^ u := by
    split_ifs with h
    · subst i
      exact (sub_self _).le.trans (mul_nonneg (by positivity) (pow_nonneg (hn _) _))
    · rw [sub_zero]
      calc
        v i ^ t ≤ v i ^ ((k+1)*u) := pow_le_pow_of_le_one (hn i) (h1 i) ht
        _ = (v i ^ u)^k * v i ^ u := by rw [Nat.mul_comm, pow_mul, pow_succ]
        _ ≤ _ := mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (pow_nonneg (hn _) _)
          (excited_slot_le hn hm hs ha i h) k) (pow_nonneg (hn _) _)
  have summed := hasSum_le terms (hl.sub (hasSum_ite_eq 0 (v 0^t))) (hs.mul_left ((3/4 : ℝ)^k))
  exact summed.trans (by rw [mul_comm]; exact mul_le_mul_of_nonneg_right ha (by positivity))

/-- The spatial magnetic matrix, by rows in the order of Stage 3's three cuts. -/
def magneticRow (m : Flux) (i : spatialAxis) : Flux :=
  match i.val.val with
  | 0 => (false,m.2.2,m.2.1)
  | 1 => (m.2.2,false,m.1)
  | _ => (m.2.1,m.1,false)

abbrev magneticBit (m : Flux) (i j : spatialAxis) := fluxBit (magneticRow m i) j.val

theorem magneticBit_diag : ∀ m i, magneticBit m i i = false := by decide

theorem magneticBit_symm : ∀ m i j, magneticBit m i j = magneticBit m j i := by decide

theorem magneticBit_plane : ∀ (m : Flux) (p : RectSpatialPlane),
    magneticBit m (firstSpatial p.val) ⟨p.val.val.2,p.property⟩ = joinTwist zeroFlux m p.val := by decide

def misaligned (m q : Flux) : Prop := m ≠ zeroFlux ∧ q ≠ zeroFlux ∧ q ≠ m
instance (m q : Flux) : Decidable (misaligned m q) := inferInstanceAs (Decidable (_ ∧ _ ∧ _))

theorem misaligned_row : ∀ m q, misaligned m q → ∃ i : spatialAxis, character (magneticRow m i) q = -1 := by
  decide

abbrev evenShape (h : ℕ) : spatialAxis → ℕ := fun _ => h+h

def halfTurn {h : ℕ} (t : Fin (h+h)) : Fin (h+h) :=
  if ht : t.val < h then ⟨t.val+h,by omega⟩ else ⟨t.val-h,by omega⟩

def inStrip {h : ℕ} (t : Fin (h+h)) : Bool := decide (0 < t.val ∧ t.val ≤ h)
def atCut {n : ℕ} (t : Fin n) : Bool := decide (t.val = 0)

theorem halfTurn_val {h : ℕ} (t : Fin (h+h)) :
    (halfTurn t).val = if t.val < h then t.val+h else t.val-h := by
  unfold halfTurn
  split <;> simp_all

theorem halfTurn_twice {h : ℕ} (t : Fin (h+h)) : halfTurn (halfTurn t) = t := by
  apply Fin.ext
  simp only [halfTurn_val]
  have bound := t.isLt
  split_ifs <;> omega

theorem finRotate_val_if {n : ℕ} (t : Fin n) :
    (finRotate n t).val = if t.val+1 < n then t.val+1 else 0 := by
  cases n with
  | zero => exact Fin.elim0 t
  | succ n =>
    by_cases h : t.val < n
    · rw [if_pos (by omega),show t = ⟨t.val,by omega⟩ from rfl,finRotate_of_lt h]
    · have he : t = Fin.last n := Fin.ext (by simp; omega)
      subst t
      simp

theorem halfTurn_rotate {h : ℕ} (t : Fin (h+h)) :
    halfTurn (finRotate _ t) = finRotate _ (halfTurn t) := by
  apply Fin.ext
  simp only [halfTurn_val,finRotate_val_if]
  have bound := t.isLt
  split_ifs <;> omega

theorem inStrip_halfTurn {h : ℕ} (t : Fin (h+h)) : inStrip (halfTurn t) = !(inStrip t) := by
  have bound := t.isLt
  rw [Bool.eq_iff_iff]
  simp only [inStrip,halfTurn_val,Bool.not_eq_true',decide_eq_true_eq,decide_eq_false_iff_not]
  split_ifs <;> omega

theorem inStrip_boundary {h : ℕ} (t : Fin (h+h)) :
    xor (inStrip (finRotate _ t)) (inStrip t) = xor (atCut t) (atCut (halfTurn t)) := by
  have bound := t.isLt
  have xor_true : ∀ a b : Bool, xor a b = true ↔ ¬(a = true ↔ b = true) := by decide
  rw [Bool.eq_iff_iff]
  simp only [xor_true,inStrip,atCut,finRotate_val_if,halfTurn_val,decide_eq_true_eq]
  split_ifs <;> omega

def shiftedSite {h : ℕ} (i : spatialAxis) (x : RectSite (evenShape h)) : RectSite (evenShape h) :=
  fun j => if j = i then halfTurn (x j) else x j

theorem shiftedSite_twice {h : ℕ} (i : spatialAxis) (x : RectSite (evenShape h)) :
    shiftedSite i (shiftedSite i x) = x := by
  funext j
  by_cases hj : j=i <;> simp [shiftedSite,hj,halfTurn_twice]

def siteHalfShift {h : ℕ} (i : spatialAxis) : Equiv.Perm (RectSite (evenShape h)) where
  toFun := shiftedSite i
  invFun := shiftedSite i
  left_inv := shiftedSite_twice i
  right_inv := shiftedSite_twice i

theorem shift_rectStep {h : ℕ} (axis i : spatialAxis) (x : RectSite (evenShape h)) :
    shiftedSite axis (rectStep x i) = rectStep (shiftedSite axis x) i := by
  funext j
  dsimp only [rectStep,shiftedSite]
  split_ifs <;> first | rfl | exact halfTurn_rotate _

/-- Flip the outgoing j-bonds on the j-cut in the half-strip of the translation direction. -/
def stripSign {h : ℕ} (m : Flux) (axis : spatialAxis) (x : RectSite (evenShape h)) (j : spatialAxis) :=
  magneticBit m axis j && inStrip (x axis) && atCut (x j)

def squareCurl (a b c d : Bool) := xor (xor (xor a b) c) d
def squareStack {h : ℕ} (m : Flux) (x : RectSite (evenShape h)) (i j : spatialAxis) :=
  magneticBit m i j && atCut (x i) && atCut (x j)

theorem strip_curl {h : ℕ} (m : Flux) (axis i j : spatialAxis) (hij : i ≠ j)
    (x : RectSite (evenShape h)) :
    xor (squareStack m x i j) (squareCurl (stripSign m axis x i) (stripSign m axis (rectStep x i) j)
      (stripSign m axis (rectStep x j) i) (stripSign m axis x j)) =
      squareStack m (shiftedSite axis x) i j := by
  have hi := inStrip_boundary (x axis)
  by_cases ha : axis = i
  · subst axis
    simp only [squareStack,stripSign,squareCurl,rectStep,shiftedSite,
      if_neg hij,if_neg hij.symm,magneticBit_diag,Bool.false_and,Bool.false_xor,Bool.xor_false]
    exact (by decide : ∀ b z z' c d d' : Bool, xor d' d = xor z z' →
      xor (b && z && c) (xor (b && d' && c) (b && d && c)) = (b && z' && c)) _ _ _ _ _ _ hi
  · by_cases hb : axis = j
    · subst axis
      simp only [squareStack,stripSign,squareCurl,rectStep,shiftedSite,
        if_neg hij,if_neg hij.symm,magneticBit_diag,Bool.false_and,Bool.xor_false,
        magneticBit_symm m j i]
      exact (by decide : ∀ b z z' c d d' : Bool, xor d' d = xor z z' →
        xor (b && c && z) (xor (b && d && c) (b && d' && c)) = (b && c && z')) _ _ _ _ _ _ hi
    · simp only [squareStack,stripSign,squareCurl,rectStep,shiftedSite,
        if_neg ha,if_neg (Ne.symm ha),if_neg hb,if_neg (Ne.symm hb),if_neg hij,if_neg hij.symm]
      exact (by decide : ∀ f a b : Bool, xor f (xor (xor (xor a b) a) b) = f) _ _ _

theorem strip_squared {h : ℕ} (m : Flux) (axis j : spatialAxis) (x : RectSite (evenShape h)) :
    xor (stripSign m axis x j) (stripSign m axis (shiftedSite axis x) j) =
      (magneticBit m axis j && atCut (x j)) := by
  by_cases hj : j = axis
  · subst j; simp [stripSign,magneticBit_diag]
  · simp only [stripSign,shiftedSite,if_neg hj,if_true,inStrip_halfTurn]
    exact (by decide : ∀ a b c : Bool, xor (a && b && c) (a && (!b) && c) = (a && c)) _ _ _

def compensated {h : ℕ} (m : Flux) (i : spatialAxis) (u : RectSlice (evenShape h))
    (b : RectSite (evenShape h) × spatialAxis) : Wilson.SU2 :=
  linkCentre (stripSign m i b.1 b.2) * u (shiftedSite i b.1,b.2)

theorem compensated_sq {h : ℕ} (m : Flux) (i : spatialAxis) (u : RectSlice (evenShape h)) :
    compensated m i (compensated m i u) = rectFlip (magneticRow m i) u := by
  funext b
  rcases b with ⟨x,j⟩
  change linkCentre _ * (linkCentre _ * u (shiftedSite i (shiftedSite i x),j)) = linkCentre _ * u (x,j)
  rw [← mul_assoc,← linkCentre_xor,strip_squared,shiftedSite_twice]
  congr 2
  simp [atCut,magneticBit]

/-- The half-period permutation pulls back the product Haar measure. The
position-dependent signs multiply the individual bonds by fixed group elements. -/
def compensatedEquiv (h : ℕ) (m : Flux) (i : spatialAxis) :
    RectSlice (evenShape h) ≃ᵐ RectSlice (evenShape h) :=
  (MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2)
    ((siteHalfShift i).prodCongr (Equiv.refl spatialAxis))).trans
      (MeasurableEquiv.piCongrRight fun b => MeasurableEquiv.mulLeft (linkCentre (stripSign m i b.1 b.2)))

theorem pi_pull_involution {I A : Type*} [MeasurableSpace A] (e : Equiv.Perm I) (he : Function.Involutive e)
    (u : I → A) : MeasurableEquiv.piCongrLeft (fun _ => A) e u = u ∘ e := by
  funext i
  obtain ⟨j,rfl⟩ := e.surjective i
  exact (MeasurableEquiv.piCongrLeft_apply_apply (β := fun _ => A) e u j).trans (congrArg u (he j)).symm

theorem compensated_apply (h : ℕ) (m : Flux) (i : spatialAxis) (u : RectSlice (evenShape h)) :
    compensatedEquiv h m i u = compensated m i u := by
  let E := (siteHalfShift (h := h) i).prodCongr (Equiv.refl spatialAxis)
  have he : Function.Involutive E := fun b => Prod.ext (shiftedSite_twice i b.1) rfl
  funext b
  change linkCentre _ * ((MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) E u) b) = _
  rw [pi_pull_involution E he]
  rfl

theorem compensated_preserving (h : ℕ) (m : Flux) (i : spatialAxis) :
    MeasurePreserving (compensatedEquiv h m i) (rectHaar (evenShape h)) (rectHaar (evenShape h)) :=
  (measurePreserving_pi _ _ (fun _ => measurePreserving_mul_left Wilson.linkHaar _)).comp
    (measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) _)

theorem rectStep_comm {n : spatialAxis → ℕ} (x : RectSite n) (i j : spatialAxis) :
    rectStep (rectStep x i) j = rectStep (rectStep x j) i := by
  funext k
  dsimp only [rectStep]
  split_ifs <;> rfl

def spatialWord {n : spatialAxis → ℕ} (u : RectSlice n) (x : RectSite n) (i j : spatialAxis) :=
  u (x,i) * u (rectStep x i,j) * (u (rectStep x j,i))⁻¹ * (u (x,j))⁻¹

theorem rectFace_spatial {h : ℕ} (m : Flux) (u : RectSlice (evenShape h)) (x : RectSite (evenShape h))
    (p : RectSpatialPlane) :
    let i := firstSpatial p.val
    let j : spatialAxis := ⟨p.val.val.2,p.property⟩
    rectFaceTerm m u u (fun _ => 1) x p.val =
      1 - bitSign (squareStack m x i j) * Wilson.halfTrace (spatialWord u x i j) := by
  dsimp only
  simp [rectFaceTerm,p.property,spatialWord,squareStack,atCut,magneticBit_plane,Bool.and_assoc]

theorem compensated_word {h : ℕ} (m : Flux) (axis i j : spatialAxis) (u : RectSlice (evenShape h))
    (x : RectSite (evenShape h)) :
    spatialWord (compensated m axis u) x i j =
      linkCentre (squareCurl (stripSign m axis x i) (stripSign m axis (rectStep x i) j)
        (stripSign m axis (rectStep x j) i) (stripSign m axis x j)) *
      spatialWord u (shiftedSite axis x) i j := by
  simp only [spatialWord,compensated,shift_rectStep,linkCentre_inv_apply,linkCentre_mul_apply,squareCurl]

theorem compensated_action {h : ℕ} (m : Flux) (axis : spatialAxis) (u : RectSlice (evenShape h)) :
    rectSpatialAction m (compensated m axis u) = rectSpatialAction m u := by
  unfold rectSpatialAction
  rw [← Equiv.sum_comp (siteHalfShift (h := h) axis) (fun x => ∑ p : RectSpatialPlane, rectFaceTerm m u u (fun _ => 1) x p.val)]
  apply Finset.sum_congr rfl
  intro x _
  apply Finset.sum_congr rfl
  intro p _
  let i := firstSpatial p.val
  let j : spatialAxis := ⟨p.val.val.2,p.property⟩
  have hij : i ≠ j := fun hh => p.val.property.ne (congrArg Subtype.val hh)
  simp only [rectFace_spatial,compensated_word,halfTrace_linkCentre]
  rw [← mul_assoc,← bitSign_xor,strip_curl m axis i j hij]
  rfl

abbrev bondHalfShift {h : ℕ} (axis : spatialAxis) :=
  (siteHalfShift (h := h) axis).prodCongr (Equiv.refl spatialAxis)

theorem compensated_temporal {h : ℕ} (m : Flux) (axis : spatialAxis) (β : ℝ)
    (u v : RectSlice (evenShape h)) :
    rectTemporal _ β (compensated m axis u, compensated m axis v) = rectTemporal _ β (u,v) := by
  change Real.exp (-β * ∑ b, _) = Real.exp (-β * ∑ b, (1 - Wilson.halfTrace (v b * (u b)⁻¹)))
  rw [← (bondHalfShift axis).sum_comp (fun b => 1 - Wilson.halfTrace (v b * (u b)⁻¹))]
  congr 2
  apply Finset.sum_congr rfl
  rintro ⟨x,j⟩ _
  let z := linkCentre (stripSign m axis x j)
  change 1 - Wilson.halfTrace ((z * v _) * (z * u _)⁻¹) = 1 - Wilson.halfTrace (v (shiftedSite axis x,j) * (u (shiftedSite axis x,j))⁻¹)
  rw [show (z * v (shiftedSite axis x,j)) * (z * u (shiftedSite axis x,j))⁻¹ =
    z * (v (shiftedSite axis x,j) * (u (shiftedSite axis x,j))⁻¹) * z⁻¹ by group,
    Wilson.halfTrace_conjugate]

theorem compensated_gauge {h : ℕ} (m : Flux) (axis : spatialAxis) (u : RectSlice (evenShape h))
    (g : RectGauges (evenShape h)) :
    rectGauge _ (compensated m axis u, g ∘ shiftedSite axis) = compensated m axis (rectGauge _ (u,g)) := by
  funext b
  rcases b with ⟨x,j⟩
  simp only [rectGauge,compensated,ContinuousMap.coe_mk,Function.comp_apply,shift_rectStep]
  rw [← mul_assoc (g _),← (linkCentre_comm _ _).eq]
  simp only [mul_assoc]

theorem compensated_kernel {h : ℕ} (m : Flux) (axis : spatialAxis) (β : ℝ)
    (u v : RectSlice (evenShape h)) :
    rectSymKernel _ β m (compensated m axis u,compensated m axis v) = rectSymKernel _ β m (u,v) := by
  simp only [rectSymKernel_apply,rectHalfWeight,ContinuousMap.coe_mk,compensated_action]
  apply congrArg (fun z : ℝ => rectHalfWeight _ β m u * rectHalfWeight _ β m v * z)
  let E : RectGauges (evenShape h) ≃ᵐ RectGauges (evenShape h) := MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) (siteHalfShift (h := h) axis)
  have he : MeasurePreserving E (rectGaugeHaar (evenShape h)) (rectGaugeHaar (evenShape h)) :=
    measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) _
  rw [← he.integral_comp' (fun g => rectTemporal _ β (compensated m axis u, rectGauge _ (compensated m axis v,g)))]
  apply integral_congr_ae
  exact ae_of_all _ fun g => by
    change rectTemporal _ β (compensated m axis u, rectGauge _ (compensated m axis v,E g)) = _
    rw [show E g = g ∘ shiftedSite axis from pi_pull_involution (siteHalfShift axis) (shiftedSite_twice axis) g]
    rw [compensated_gauge,compensated_temporal]

theorem rectHalfWeight_gauge (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (u : RectSlice n) (g : RectGauges n) :
    rectHalfWeight n β m (rectGauge n (u,g)) = rectHalfWeight n β m u := by
  have gaugeWord (x : RectSite n) (i j : spatialAxis) : spatialWord (rectGauge n (u,g)) x i j =
      g x * spatialWord u x i j * (g x)⁻¹ := by
    unfold spatialWord
    simp only [rectGauge,ContinuousMap.coe_mk,mul_inv_rev,inv_inv,rectStep_comm x j i]
    group
  have action : rectSpatialAction m (rectGauge n (u,g)) = rectSpatialAction m u := by
    apply Finset.sum_congr rfl
    intro x _
    apply Finset.sum_congr rfl
    intro p _
    simp only [rectFaceTerm,dif_neg p.property]
    rw [show (rectGauge n (u,g) (x,_) * _ * _ * _) = _ from gaugeWord x (firstSpatial p.val) ⟨p.val.val.2,p.property⟩,
      Wilson.halfTrace_conjugate]
    rfl
  simp only [rectHalfWeight,ContinuousMap.coe_mk,action]

theorem rectSymKernel_gauge_right (n : spatialAxis → ℕ) (β : ℝ) (m : Flux)
    (u v : RectSlice n) (g : RectGauges n) (hg : ∀ x a, Commute (g x) a) :
    rectSymKernel n β m (u,rectGauge n (v,g)) = rectSymKernel n β m (u,v) := by
  rw [rectSymKernel_apply,rectSymKernel_apply,rectHalfWeight_gauge]
  have swap (y : RectGauges n) : y*g = g*y := funext fun x => (hg x (y x)).eq.symm
  simp only [rectGauge_mul,swap]
  exact congrArg (_ * ·) (integral_mul_left_eq_self (μ := rectGaugeHaar n)
    (fun y => rectTemporal n β (u,rectGauge n (v,y))) g)

def displacedCutGauge {h : ℕ} (e : Flux) (axis : spatialAxis) (x : RectSite (evenShape h)) : Wilson.SU2 :=
  linkCentre (fluxBit e axis.val && inStrip (x axis))

/-- Moving the cut in the translation direction changes its representative by
the central vertex gauge on the intervening strip. -/
theorem compensated_flip {h : ℕ} (m e : Flux) (axis : spatialAxis) (u : RectSlice (evenShape h)) :
    rectFlip e (compensated m axis u) =
      rectGauge _ (compensated m axis (rectFlip e u),displacedCutGauge e axis) := by
  funext b
  rcases b with ⟨x,j⟩
  let f (y : RectSite (evenShape h)) := fluxBit e j.val && atCut (y j)
  let g (y : RectSite (evenShape h)) := fluxBit e axis.val && inStrip (y axis)
  let d := stripSign m axis x j
  have cut (y : RectSite (evenShape h)) : decide (fluxBit e j.val = true ∧ (y j).val = 0) = f y := by
    simp [f,atCut]
  simp only [rectFlip,compensated,rectGauge,ContinuousMap.coe_mk,cut,displacedCutGauge,linkCentre_inv]
  change linkCentre (f x) * (linkCentre d * _) =
    linkCentre (g x) * (linkCentre d * (linkCentre (f (shiftedSite axis x)) * _)) * linkCentre (g (rectStep x j))
  rw [(linkCentre_comm (g (rectStep x j)) _).eq.symm]
  simp only [← mul_assoc,← linkCentre_xor]
  congr 2
  by_cases hh : j=axis
  · subst j
    simp only [f,g,shiftedSite,rectStep,if_true]
    exact (by decide : ∀ a d s t v w : Bool, xor t s = xor v w →
      xor (a && v) d = xor (a && t) (xor (a && s) (xor d (a && w)))) _ _ _ _ _ _ (inStrip_boundary (x axis))
  · simp only [f,g,shiftedSite,rectStep,if_neg hh,if_neg (Ne.symm hh)]
    exact (by decide : ∀ a b c : Bool, xor a b = xor c (xor c (xor b a))) _ _ _

theorem compensated_electricEntry {h : ℕ} (m e : Flux) (axis : spatialAxis) (β : ℝ)
    (u v : RectSlice (evenShape h)) :
    rectElectricEntry _ β m e (compensated m axis u,compensated m axis v) = rectElectricEntry _ β m e (u,v) := by
  unfold rectElectricEntry rectSymEntry
  rw [compensated_flip,rectSymKernel_gauge_right _ _ _ _ _ (displacedCutGauge e axis) (fun x a => linkCentre_comm _ a),
    compensated_kernel]

section Conjugation

variable {X : Type*} [MeasurableSpace X] {ν : Measure X} [IsProbabilityMeasure ν]

def pullSlice (E : X ≃ᵐ X) (he : MeasurePreserving E ν ν) :
    Kernel.Space ν →L[ℂ] Kernel.Space ν :=
  (Lp.compMeasurePreservingₗᵢ ℂ E he).toContinuousLinearMap

theorem pull_operator_commutes (E : X ≃ᵐ X) (he : MeasurePreserving E ν ν)
    (k : X × X → ℂ) (hk : MemLp k 2 (ν.prod ν)) (h : ∀ x y, k (E x,E y) = k (x,y)) :
    Commute (pullSlice E he) (Kernel.operator k hk) := by
  apply ContinuousLinearMap.ext
  intro f
  apply Lp.ext
  have left := Lp.coeFn_compMeasurePreserving (Kernel.operator k hk f) he
  have row := he.quasiMeasurePreserving.ae_eq_comp (Kernel.operator_apply hk f)
  have right := Lp.coeFn_compMeasurePreserving f he
  filter_upwards [left,row,Kernel.operator_apply hk (pullSlice E he f)] with x hx hy hz
  refine (hx.trans hy).trans (Eq.trans ?_ hz.symm)
  change (∫ y, k (E x,y) * f y ∂ν) = _
  rw [← he.integral_comp' (fun y => k (E x,y) * f y)]
  apply integral_congr_ae
  filter_upwards [right] with y hfy
  rw [h]
  exact congrArg (k (x,y) * ·) hfy.symm

def sliceConj (ν : Measure X) : Kernel.Space ν →+ Kernel.Space ν where
  toFun := star
  map_zero' := by
    apply Lp.ext
    filter_upwards [Lp.coeFn_star (0 : Kernel.Space ν), Lp.coeFn_zero ℂ 2 ν] with x hx hz
    change (0 : Kernel.Space ν) x = 0 at hz
    change (star (0 : Kernel.Space ν) : Kernel.Space ν) x = star ((0 : Kernel.Space ν) x) at hx
    rw [hx,hz,star_zero]
  map_add' f g := by
    apply Lp.ext
    filter_upwards [Lp.coeFn_star (f+g),Lp.coeFn_star f,Lp.coeFn_star g,
      Lp.coeFn_add f g,Lp.coeFn_add (star f) (star g)] with x ha hf hg hb hc
    rw [ha,hc]
    change star ((f+g : Kernel.Space ν) x) = (star f : Kernel.Space ν) x + (star g : Kernel.Space ν) x
    rw [hf,hg,hb]
    exact star_add _ _

omit [IsProbabilityMeasure ν] in
theorem sliceConj_smul (a : ℂ) (f : Kernel.Space ν) :
    sliceConj ν (a • f) = conj a • sliceConj ν f := by
  apply Lp.ext
  filter_upwards [Lp.coeFn_star (a • f),Lp.coeFn_star f,Lp.coeFn_smul a f,
    Lp.coeFn_smul (conj a) (star f)] with x h1 h2 h3 h4
  change (star (a • f) : Kernel.Space ν) x = (conj a • star f : Kernel.Space ν) x
  rw [h1,h4]
  change conj ((a • f : Kernel.Space ν) x) = conj a * (star f : Kernel.Space ν) x
  rw [h2,h3]
  exact map_mul _ _ _

omit [IsProbabilityMeasure ν] in
theorem pull_conjugate (E : X ≃ᵐ X) (he : MeasurePreserving E ν ν) (f : Kernel.Space ν) :
    pullSlice E he (sliceConj ν f) = sliceConj ν (pullSlice E he f) := by
  apply Lp.ext
  have h₁ := Lp.coeFn_compMeasurePreserving (sliceConj ν f) he
  have h₂ := he.quasiMeasurePreserving.ae_eq_comp (Lp.coeFn_star f)
  filter_upwards [h₁,h₂,Lp.coeFn_star (pullSlice E he f),Lp.coeFn_compMeasurePreserving f he] with x h1 h2 h3 h4
  exact (h1.trans h2).trans ((congrArg star h4.symm).trans h3.symm)

theorem real_kernel_conjugate (k : X × X → ℝ) (hk : MemLp (fun p => (k p : ℂ)) 2 (ν.prod ν))
    (f : Kernel.Space ν) :
    Kernel.operator _ hk (sliceConj ν f) = sliceConj ν (Kernel.operator _ hk f) := by
  apply Lp.ext
  filter_upwards [Kernel.operator_apply hk (sliceConj ν f),Kernel.operator_apply hk f,
    Lp.coeFn_star (Kernel.operator _ hk f)] with x h1 h2 h3
  refine h1.trans (Eq.trans ?_ h3.symm)
  change _ = conj ((Kernel.operator _ hk f) x)
  rw [h2,← integral_conj]
  apply integral_congr_ae
  filter_upwards [Lp.coeFn_star f] with y hy
  change _ * (star f : Kernel.Space ν) y = _
  rw [hy]
  simp

end Conjugation

theorem rectSector_conjugate (n : spatialAxis → ℕ) (β : ℝ) (q m : Flux) (f : Kernel.Space (rectHaar n)) :
    rectSector n β q m (sliceConj _ f) = sliceConj _ (rectSector n β q m f) := by
  let C := sliceConj (rectHaar n)
  have hP : rectProj n q (C f) = C (rectProj n q f) := by
    unfold rectProj characterProj
    dsimp only [C]
    simp only [smul_apply,sum_apply, sliceConj_smul,
      map_sum, map_intCast, map_div₀, map_one, map_ofNat]
    exact congrArg ((1/8 : ℂ) • ·) (Finset.sum_congr rfl (fun e _ => congrArg ((character e q : ℂ) • ·)
      (pull_conjugate (rectFlipEquiv n e) (rectFlip_preserving n e) f)))
  change rectSymOperator n β m (rectProj n q (C f)) = C (rectSymOperator n β m (rectProj n q f))
  rw [hP]
  exact real_kernel_conjugate _ (rectSymEntry_memLp n β m) _

def magneticShift (h : ℕ) (m : Flux) (axis : spatialAxis) :=
  pullSlice (compensatedEquiv h m axis) (compensated_preserving h m axis)

theorem magneticShift_square (h : ℕ) (m : Flux) (i : spatialAxis) :
    magneticShift h m i * magneticShift h m i = rectTranslation (evenShape h) (magneticRow m i) := by
  let E := compensatedEquiv h m i
  have he := compensated_preserving h m i
  apply ContinuousLinearMap.ext
  intro f
  apply Lp.ext
  have twice := he.quasiMeasurePreserving.ae_eq_comp (Lp.coeFn_compMeasurePreserving f he)
  filter_upwards [Lp.coeFn_compMeasurePreserving (magneticShift h m i f) he,twice,
    Lp.coeFn_compMeasurePreserving f (rectFlip_preserving (evenShape h) (magneticRow m i))] with x h1 h2 h3
  refine (h1.trans h2).trans (Eq.trans ?_ h3.symm)
  apply congrArg (fun u => f u)
  change compensatedEquiv h m i (compensatedEquiv h m i x) = rectFlip (magneticRow m i) x
  simp only [compensated_apply,compensated_sq]

theorem magneticShift_commutes (h : ℕ) (β : ℝ) (q m : Flux) (axis : spatialAxis) :
    Commute (magneticShift h m axis) (rectSector (evenShape h) β q m) := by
  let n := evenShape h
  let S := rectSymOperator n β m
  let D := magneticShift h m axis
  have hc (e : Flux) : Commute D (S * rectTranslation n e) := by
    rw [show S * rectTranslation n e = _ from (rectElectricEntry_operator n β m e).symm]
    exact pull_operator_commutes _ (compensated_preserving h m axis) (rectElectricEntry n β m e) (rectSymSeam_memLp n β m e)
      (fun u v => by simpa only [compensated_apply] using compensated_electricEntry m e axis β u v)
  change D * (S * ((1 / 8 : ℂ) • ∑ e : Flux, (character e q : ℂ) • rectTranslation n e)) =
    (S * ((1 / 8 : ℂ) • ∑ e : Flux, (character e q : ℂ) • rectTranslation n e)) * D
  simp only [mul_smul_comm,smul_mul_assoc,Finset.mul_sum,Finset.sum_mul,fun e => (hc e).eq]

theorem translation_on_sector (n : spatialAxis → ℕ) (β : ℝ) (q m e : Flux) :
    rectTranslation n e * rectSector n β q m = (character e q : ℂ) • rectSector n β q m := by
  unfold rectSector
  rw [← mul_assoc,(rectSymOperator_commutes n β m e).eq.symm,mul_assoc]
  rw [show rectTranslation n e * rectProj n q = _ from translation_characterProj _ (rectTranslation_mul n) e q,
    mul_smul_comm]
  rfl

/-- A complex line admits no antilinear endomorphism with square minus the identity. -/
theorem finrank_ne_one_of_antilinear {H : Type*} [AddCommGroup H] [Module ℂ H]
    (V : Submodule ℂ H) (J : H → H) (hJ : ∀ f ∈ V, J f ∈ V)
    (anti : ∀ (c : ℂ) (f : H), J (c • f) = conj c • J f) (minus : ∀ f ∈ V, J (J f) = -f) :
    Module.finrank ℂ V ≠ 1 := by
  intro dim
  obtain ⟨z,hz,hspan⟩ := (finrank_eq_one_iff' (K := ℂ) (V := V)).mp dim
  obtain ⟨c,hc⟩ := hspan ⟨J z.val,hJ _ z.property⟩
  have eqc : c • z.val = J z.val := congrArg Subtype.val hc
  have rel : (conj c * c) • z.val = (-1 : ℂ) • z.val := by
    calc
      _ = conj c • (c • z.val) := mul_smul _ _ _
      _ = conj c • J z.val := congrArg (conj c • ·) eqc
      _ = J (c • z.val) := (anti c z.val).symm
      _ = J (J z.val) := congrArg J eqc
      _ = -z.val := minus _ z.property
      _ = _ := (neg_one_smul ℂ _).symm
  have nz : z.val ≠ 0 := fun hh => hz (Subtype.ext hh)
  have hn := congrArg Complex.re (smul_left_injective ℂ nz rel)
  rw [mul_comm, Complex.mul_conj,Complex.ofReal_re] at hn
  norm_num at hn
  linarith [Complex.normSq_nonneg c]


/-- An antilinear map whose square is minus the identity excludes a complex
one-dimensional eigenspace. The construction uses the reality of Wilson weights. -/
theorem misaligned_not_simple (h : ℕ) (β : ℝ) (q m : Flux) (hm : misaligned m q) (r : ℝ) (hr : 0 < r) :
    Module.finrank ℂ (Module.End.eigenspace (rectSector (evenShape h) β q m).toLinearMap (r : ℂ)) ≠ 1 := by
  obtain ⟨i,hi⟩ := misaligned_row m q hm
  let n := evenShape h
  let S := rectSector n β q m
  let D := magneticShift h m i
  let C := sliceConj (rectHaar n)
  let J (f : Kernel.Space (rectHaar n)) := D (C f)
  let V := Module.End.eigenspace S.toLinearMap (r : ℂ)
  have hJ (f : Kernel.Space (rectHaar n)) (hf : f ∈ V) : J f ∈ V := by
    have hSf : S f = (r:ℂ) • f := Module.End.mem_eigenspace_iff.mp hf
    apply Module.End.mem_eigenspace_iff.mpr
    change S (D (C f)) = _
    calc
      S (D (C f)) = D (S (C f)) := (DFunLike.congr_fun (magneticShift_commutes h β q m i).eq (C f)).symm
      _ = D (C (S f)) := congrArg D (rectSector_conjugate n β q m f)
      _ = _ := by rw [hSf]; simp only [C,sliceConj_smul,map_smul,Complex.conj_ofReal]; rfl
  have minus (f : Kernel.Space (rectHaar n)) (hf : f ∈ V) : J (J f) = -f := by
    have hSf : S f = (r:ℂ) • f := Module.End.mem_eigenspace_iff.mp hf
    have neg := DFunLike.congr_fun (translation_on_sector n β q m (magneticRow m i)) f
    rw [hi] at neg
    change rectTranslation n (magneticRow m i) (S f) = ((-1 : ℤ) : ℂ) • S f at neg
    rw [hSf,map_smul] at neg
    have hD : D (D f) = rectTranslation n (magneticRow m i) f := DFunLike.congr_fun (magneticShift_square h m i) f
    have flip : rectTranslation n (magneticRow m i) f = -f := by
      apply smul_right_injective _ (by exact_mod_cast hr.ne' : (r:ℂ) ≠ 0)
      simpa using neg
    change D (C (D (C f))) = -f
    rw [← show D (C (C f)) = C (D (C f)) from pull_conjugate _ (compensated_preserving h m i) (C f),
      show C (C f) = f from star_star f,hD,flip]
  exact finrank_ne_one_of_antilinear V J hJ (fun c f => by simp only [J,C,sliceConj_smul,map_smul]) minus

/-- A comparison of all integer moments compares every slot to the second
sector's maximal slot. A strictly intermediate scale covers a zero maximum. -/
theorem slot_le_of_moments {v w : ℕ → ℝ} {V W : ℕ → ℝ} (hv : ∀ i, 0 ≤ v i)
    (hw : ∀ j, 0 ≤ w j) (hmax : ∀ j, w j ≤ w 0)
    (vs : ∀ t, 2 ≤ t → HasSum (fun i => v i ^ t) (V t))
    (ws : ∀ t, 2 ≤ t → HasSum (fun i => w i ^ t) (W t))
    (cmp : ∀ t, 2 ≤ t → V t ≤ W t) (i : ℕ) : v i ≤ w 0 := by
  by_contra! h
  let c := (w 0 + v i)/2
  have hc : 0 < c := by dsimp [c]; linarith [hw 0]
  have hlo : w 0 < c := by dsimp [c]; linarith
  have hhi : 1 < v i / c := (one_lt_div hc).2 (by dsimp [c]; linarith)
  have ss (t) (ht : 2 ≤ t) : HasSum (fun j => (w j/c)^t) (W t / c^t) := by
    simpa only [div_pow] using (ws t ht).div_const (c^t)
  have tend := tendsto_pow_atTop_atTop_of_one_lt hhi (eventually_gt_atTop (W 2 / c^2))
  obtain ⟨t,ht,large⟩ := ((eventually_ge_atTop 2).and tend).exists
  have first := (vs t ht).summable.le_tsum i (fun j _ => pow_nonneg (hv j) _)
  rw [(vs t ht).tsum_eq] at first
  have le := hasSum_le (fun j => pow_le_pow_of_le_one (div_nonneg (hw j) hc.le)
    ((div_le_one hc).2 ((hmax j).trans hlo.le)) ht) (ss t ht) (ss 2 le_rfl)
  change W 2/c^2 < (v i/c)^t at large
  exact large.not_ge (by rw [div_pow]; exact (div_le_div_of_nonneg_right (first.trans (cmp t ht)) (pow_pos hc t).le).trans le)

structure FluxSpectrum (Γ : CubicPeriodSublattice) (β : ℝ) where
  level : Flux → Flux → ℕ → ℝ
  nonneg : ∀ q m i, 0 ≤ level q m i
  le_first : ∀ q m i, level q m i ≤ level q m 0
  le_one : ∀ q m i, level q m i ≤ 1
  vacuum : level zeroFlux zeroFlux 0 = 1
  moment : ∀ q m t, 2 ≤ t → HasSum (fun j => level q m j ^ t) (sectorMoment Γ β q m t)
  partner : ∀ q m, misaligned m q → ∃ j ≠ 0, level q m j = level q m 0

theorem misaligned_partner {n : ℕ} (hd : 4 ∣ n) (β : ℝ) (q m : Flux) (hm : misaligned m q)
    (v : ℕ → ℝ) (encodes : EncodesSlots (rectSector (boxShape (cube n)) β q m) v)
    (hn : ∀ j, 0 ≤ v j) (maximum : ∀ j, v j ≤ v 0) :
    ∃ j ≠ 0, v j = v 0 := by
  classical
  by_cases no : v 0 = 0
  · exact ⟨1,by decide,le_antisymm (maximum 1) (no ▸ hn 1)⟩
  let S := rectSector (boxShape (cube n)) β q m
  obtain ⟨enc,inj,hit,off⟩ := encodes
  obtain ⟨z,hz⟩ : 0 ∈ Set.range enc := by by_contra h; exact no (off 0 h)
  rcases z with ⟨r,j⟩
  let dim := Module.finrank ℂ (Module.End.eigenspace S.toLinearMap (r.val : ℂ))
  have big : 1 < dim := by
    have hdim : dim ≠ 1 := by
      obtain ⟨k,hk⟩ := hd
      have he : n = (2*k)+(2*k) := by omega
      change Module.finrank ℂ (Module.End.eigenspace (rectSector (boxShape (cube n)) β q m).toLinearMap _) ≠ 1
      rw [boxShape_cube,he]
      exact misaligned_not_simple (2*k) β q m hm r.val r.property
    have nz : j.val < dim := j.isLt
    omega
  let a : Fin dim := if j.val = 0 then ⟨1,big⟩ else ⟨0,by omega⟩
  have ne : a ≠ j := by
    intro eq
    have := congrArg Fin.val eq
    dsimp only [a] at this
    split_ifs at this <;> simp only at this <;> omega
  let z' : Wilson.PositiveSlot S := ⟨r,a⟩
  refine ⟨enc z',fun hh => ?_,(hit z').trans (by rw [← hz,hit])⟩
  have eq : z' = ⟨r,j⟩ := inj (hh.trans hz.symm)
  exact ne (by simpa only [z',Sigma.mk.inj_iff,heq_eq_eq,true_and] using eq)

theorem cubeFluxSpectrum (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (hd : 4 ∣ Γ.side) :
    Nonempty (FluxSpectrum Γ β) := by
  classical
  let R := cube Γ.side
  let c := ‖Γ.transfer μt β‖
  have hc : 0 < c := (boxNeutral_norm_pos R hβ.le).trans_eq (calibrated_cubicNorm Γ hβ)
  choose v enc top nn hm hs using boxSector_labeledList R hβ.le
  have vac : v zeroFlux zeroFlux 0 = c := (top _ _).trans (calibrated_cubicNorm Γ hβ)
  refine ⟨⟨fun q m j => v q m j / c,fun q m j => div_nonneg (nn q m j) hc.le,
    fun q m j => div_le_div_of_nonneg_right (hm q m j) hc.le,?_,(by rw [vac,div_self hc.ne']),?_,?_⟩⟩
  · intro q m j
    apply (div_le_one hc).2
    rw [← vac]
    exact slot_le_of_moments (nn q m) (nn _ _) (hm _ _) (hs q m) (hs _ _)
      (fun t ht => sectorWeight_le_periodicNeutral hβ.le (cubeSides_ge_two Γ ht) q m) j
  · intro q m t ht
    simpa only [sectorMoment,div_pow] using (hs q m t ht).div_const (c^t)
  · intro q m h
    obtain ⟨j,hj,hval⟩ := misaligned_partner hd β q m h _ (enc q m) (nn q m) (hm q m)
    exact ⟨j,hj,congrArg (· / c) hval⟩

section FiniteAspect

variable {Γ : CubicPeriodSublattice} {β : ℝ} (F : FluxSpectrum Γ β)

/-- All higher levels are negligible at the cube and half-cube periods. For
misaligned flux there is a second top slot, so the entire sector is negligible. -/
theorem flux_moment_bounds (q m : Flux) {u t k : ℕ} (hu : 2 ≤ u) (ht : (k+1)*u ≤ t)
    (short : sectorMoment Γ β q m u ≤ 3/2) :
    0 ≤ sectorMoment Γ β q m t - F.level q m 0 ^ t ∧
    sectorMoment Γ β q m t - F.level q m 0 ^ t ≤ (3/2 : ℝ) * (3/4)^k ∧
    (misaligned m q → sectorMoment Γ β q m t ≤ (3/2 : ℝ) * (3/4)^k) := by
  have hut : u ≤ t := (Nat.le_mul_of_pos_left u (Nat.succ_pos k)).trans ht
  have ts := F.moment q m t (hu.trans hut)
  have us := F.moment q m u hu
  have first := ts.summable.le_tsum 0 (fun j _ => pow_nonneg (F.nonneg q m j) t)
  rw [ts.tsum_eq] at first
  refine ⟨sub_nonneg.mpr first, tail_at_multiple ht (F.nonneg q m) (F.le_first q m)
    (F.le_one q m) us short ts,fun hm => ?_⟩
  obtain ⟨j,hj,hjv⟩ := F.partner q m hm
  have hv := excited_slot_le (F.nonneg q m) (F.le_first q m) us short j hj
  rw [hjv] at hv
  have each (i) : F.level q m i ^ t ≤ (3/4 : ℝ)^k * F.level q m i ^ u := by
    calc
      _ ≤ F.level q m i ^ ((k+1)*u) := pow_le_pow_of_le_one (F.nonneg _ _ _) (F.le_one _ _ _) ht
      _ = (F.level q m i ^ u)^k * F.level q m i ^ u := by rw [Nat.mul_comm,pow_mul,pow_succ]
      _ ≤ _ := mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (pow_nonneg (F.nonneg _ _ _) _)
        ((pow_le_pow_left₀ (F.nonneg _ _ _) (F.le_first _ _ _) _).trans hv) k) (pow_nonneg (F.nonneg _ _ _) _)
  exact (hasSum_le each ts (us.mul_left _)).trans (by
    rw [mul_comm]; exact mul_le_mul_of_nonneg_right short (by positivity))

end FiniteAspect

/-- Integer geometric-sum bounds used for both differences of a spectral moment. -/
theorem geometric_loss {z : ℝ} (hz : 0 ≤ z) (h1 : z ≤ 1) (p : ℕ) :
    (p : ℝ) * z^p * (1-z) ≤ 1-z^p ∧ 1-z^p ≤ p * (1-z) := by
  induction p with
  | zero => norm_num
  | succ p ih =>
    have prev := mul_le_mul_of_nonneg_right ih.1 hz
    have small := mul_le_mul_of_nonneg_right (pow_le_one₀ (n := (p+1)) hz h1) (sub_nonneg.mpr h1)
    have small' := mul_le_mul_of_nonneg_right (pow_le_one₀ (n := p) hz h1) (sub_nonneg.mpr h1)
    rw [pow_succ] at small ⊢
    push_cast
    constructor <;> nlinarith only [prev,ih.2,small,small']

/-- The integer displacement keeps both neighboring periods physical. On the
large cubes it also satisfies n ≤ 2⁷⁰ k, needed to recover the full-period loss. -/
def differenceStep (n : ℕ) : ℕ := n / 2^69

theorem differenceStep_budget {n u : ℕ} (hn : 2^70 ≤ n) (hu : 512*u ≤ n) :
    let k := differenceStep n
    0 < k ∧ n ≤ 2^70*k ∧ u + k + (k * 2^67)*2 ≤ n ∧ 2 ≤ n-k := by
  dsimp only
  set k := differenceStep n
  obtain ⟨r,hr,eq⟩ : ∃ r < 2^69, r + 2^69*k = n :=
    ⟨n % 2^69,Nat.mod_lt _ (by decide),Nat.mod_add_div ..⟩
  have hk : 1 ≤ k := Nat.div_pos (le_trans (by decide : 2^69 ≤ 2^70) hn) (by decide)
  have lower : k * 2^69 ≤ n := Nat.div_mul_le_self ..
  clear_value k
  refine ⟨hk,?_,?_,Nat.le_sub_of_add_le ?_⟩
  · linarith only [eq,hr,hk]
  · linarith only [hu,lower]
  · linarith only [hn,lower]

/-- Two geometric sums turn the remaining long time into a square of the
step loss. Only integer powers of the transfer enter the bound. -/
theorem second_difference_term {z : ℝ} (hz : 0 ≤ z) (h1 : z ≤ 1) {n k u : ℕ}
    (budget : u+k+(k*2^67)*2 ≤ n) :
    z^(n-k) * (1-z^k)^2 ≤ z^u / (2:ℝ)^134 := by
  have hp : z^(n-k) ≤ z^u * ((z^k)^(2^67))^2 := by
    rw [← pow_mul,← pow_mul,← pow_add]
    exact pow_le_pow_of_le_one hz h1 (by omega)
  have geom := (geometric_loss (pow_nonneg hz k) (pow_le_one₀ (n := k) hz h1) (2^67)).1
  have bound : (z^k)^(2^67) * (1-z^k) ≤ 1 / (2:ℝ)^67 := by
    apply (le_div_iff₀ (by positivity)).mpr
    simp only [Nat.cast_pow,Nat.cast_ofNat] at geom
    rw [mul_comm,← mul_assoc]
    exact geom.trans (sub_le_self _ (pow_nonneg (pow_nonneg hz k) _))
  have sq := pow_le_pow_left₀ (mul_nonneg (pow_nonneg (pow_nonneg hz k) _) (sub_nonneg.mpr (pow_le_one₀ (n := _) hz h1))) bound 2
  calc
    _ ≤ (z^u * ((z^k)^(2^67))^2) * (1-z^k)^2 := mul_le_mul_of_nonneg_right hp (sq_nonneg _)
    _ = z^u * ((z^k)^(2^67) * (1-z^k))^2 := by rw [mul_pow,mul_assoc]
    _ ≤ z^u * (1 / (2:ℝ)^67)^2 := mul_le_mul_of_nonneg_left sq (pow_nonneg hz _)
    _ = _ := by norm_num [div_eq_mul_inv]

theorem second_difference_identity (z : ℝ) {n k : ℕ} (h : k ≤ n) :
    z^(n+k) + z^(n-k) - 2*z^n = z^(n-k)*(1-z^k)^2 := by
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le h
  simp only [Nat.add_sub_cancel_left,pow_add]
  ring

theorem sector_second_difference {Γ : CubicPeriodSublattice} {β : ℝ} (F : FluxSpectrum Γ β)
    {n k u : ℕ} (hu : 2 ≤ u) (budget : u+k+(k*2^67)*2 ≤ n) (q m : Flux)
    (hs : sectorMoment Γ β q m u ≤ 3/2) :
    let X := sectorMoment Γ β q m
    |X (n+k) + X (n-k) - 2*X n| ≤ 1/(2:ℝ)^133 := by
  let v := F.level q m
  let X := sectorMoment Γ β q m
  have allS := ((F.moment q m (n+k) (by omega)).add (F.moment q m (n-k) (by omega))).sub
    ((F.moment q m n (by omega)).mul_left 2)
  have hs' : HasSum (fun i => v i^(n-k)*(1-v i^k)^2) (X (n+k) + X (n-k) - 2*X n) :=
    allS.congr_fun (fun i => (second_difference_identity _ (by omega : k ≤ n)).symm)
  have hn := hasSum_le (fun i => mul_nonneg (pow_nonneg (F.nonneg q m i) _) (sq_nonneg _)) hasSum_zero hs'
  have upper := hasSum_le (fun i => second_difference_term (F.nonneg q m i) (F.le_one q m i) budget)
    hs' ((F.moment q m u hu).div_const ((2:ℝ)^134))
  dsimp only
  rw [abs_of_nonneg hn]
  change X (n+k) + X (n-k) - 2*X n ≤ _
  exact upper.trans (by norm_num at hs ⊢; linarith only [hs])

/-- Real linear functionals on the 64 raw twist weights. -/
abbrev TwistIndex := Flux × Flux

def rawMoment (Γ : CubicPeriodSublattice) (β : ℝ) (t : ℕ) (B : TwistIndex) :=
  twistedPartition β (boxSides (cube Γ.side) t) (joinTwist B.1 B.2) / ‖Γ.transfer μt β‖^t

def fourier (Z : TwistIndex → ℝ) (i : Dir) (q m : Flux) : ℝ :=
  (∑ e : Flux, (character e q : ℝ) * Z (inFrame i e m)) / 8

theorem inFrame_involution : ∀ (i : Dir) (k : TwistIndex), inFrame i (inFrame i k.1 k.2).1 (inFrame i k.1 k.2).2 = k := by decide

theorem invert_fourier (Z : TwistIndex → ℝ) (i : Dir) (e m : Flux) :
    Z (inFrame i e m) = ∑ q : Flux, (character e q : ℝ) * fourier Z i q m := by
  have orth (u : Flux) : (∑ q : Flux, (character e q : ℝ) * (character u q : ℝ)) =
      if e=u then 8 else 0 := by
    have h := character_orthogonal e u
    simp_rw [character_symm e,character_symm u]
    split_ifs at h ⊢ <;> exact_mod_cast h
  unfold fourier
  simp only [← mul_div_assoc,Finset.mul_sum,← mul_assoc,← Finset.sum_div]
  rw [Finset.sum_comm]
  simp only [← Finset.sum_mul,orth,ite_mul,zero_mul,Finset.sum_ite_eq,Finset.mem_univ,if_true]
  ring

theorem fourier_raw (Γ : CubicPeriodSublattice) (β : ℝ) (t : ℕ) (i : Dir) (q m : Flux) :
    fourier (rawMoment Γ β t) i q m =
      sectorWeight β (boxSides (cube Γ.side) t ∘ Equiv.swap μt i) q m / ‖Γ.transfer μt β‖^t := by
  let s := boxSides (cube Γ.side) t
  have eq (e : Flux) : twistedPartition β s (joinTwist (inFrame i e m).1 (inFrame i e m).2) =
      twistedPartition β (s ∘ Equiv.swap μt i) (joinTwist e m) := by
    rw [← twistedPartition_permute β s (Equiv.swap μt i)]
    congr 1
    funext p
    change joinTwist (inFrame i e m).1 (inFrame i e m).2 (mapPlane (Equiv.swap μt i) p) = _
    rw [← inFrame_planes]
    exact congrArg (fun y : TwistIndex => joinTwist y.1 y.2 p) (inFrame_involution i (e,m))
  change (∑ e : Flux, (character e q : ℝ) * (twistedPartition β s _ / _)) / 8 = _
  simp only [eq,sectorWeight,← mul_div_assoc,← Finset.sum_div]
  ring

theorem fourier_time (Γ : CubicPeriodSublattice) (β : ℝ) (t : ℕ) (q m : Flux) :
    fourier (rawMoment Γ β t) μt q m = sectorMoment Γ β q m t := by
  simp [fourier_raw,sectorMoment]

theorem boxSides_cube_diag (n : ℕ) : boxSides (cube n) n = fun _ => n := by funext i; fin_cases i <;> rfl

theorem fourier_cube (Γ : CubicPeriodSublattice) (β : ℝ) (i : Dir) (q m : Flux) :
    fourier (rawMoment Γ β Γ.side) i q m = sectorMoment Γ β q m Γ.side := by
  rw [fourier_raw,sectorMoment,boxSides_cube_diag]
  rfl

theorem fourier_raw_nonneg (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) {t : ℕ} (ht : 2 ≤ t)
    (i : Dir) (q m : Flux) : 0 ≤ fourier (rawMoment Γ β t) i q m := by
  rw [fourier_raw]
  exact div_nonneg (sectorWeight_nonneg (s := boxSides (cube Γ.side) t ∘ Equiv.swap μt i) (cubeSides_ge_two Γ ht _) hβ.le _ _)
    (pow_nonneg (norm_nonneg _) t)

theorem fourier_sub (X Y : TwistIndex → ℝ) (i : Dir) (q m : Flux) :
    fourier (fun B => X B-Y B) i q m = fourier X i q m - fourier Y i q m := by
  simp only [fourier,mul_sub,Finset.sum_sub_distrib,sub_div]

theorem fourier_second (X Y Z : TwistIndex → ℝ) (i : Dir) (q m : Flux) :
    fourier (fun B => X B+Y B-2*Z B) i q m = fourier X i q m + fourier Y i q m - 2*fourier Z i q m := by
  have linear (c x y z : ℝ) : c*(x+y-2*z) = c*x+c*y-2*(c*z) := by ring
  simp only [fourier,linear,Finset.sum_sub_distrib,Finset.sum_add_distrib,← Finset.mul_sum]
  ring

theorem character_abs : ∀ e q : Flux, |character e q| = 1 := by decide

theorem signed_flux_sum (a : Flux → ℝ) (s : Flux → ℝ) (C : ℝ) (hs : ∀ q, |s q| ≤ 1)
    (h : ∀ q, |a q| ≤ C) : |∑ q : Flux, s q * a q| ≤ 8*C := by
  calc
    _ ≤ ∑ q : Flux, |s q * a q| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _ : Flux, C := Finset.sum_le_sum fun q _ => by
      rw [abs_mul]; simpa only [one_mul] using mul_le_mul (hs q) (h q) (abs_nonneg _) (by norm_num)
    _ = _ := by norm_num [Fintype.card_prod]

theorem fourier_bound (Z : TwistIndex → ℝ) (C : ℝ) (h : ∀ B, |Z B| ≤ C) (i : Dir) (q m : Flux) :
    |fourier Z i q m| ≤ C := by
  rw [fourier,abs_div,abs_of_pos (by norm_num : (0:ℝ)<8)]
  apply (div_le_iff₀ (by norm_num : (0:ℝ)<8)).2
  rw [mul_comm]
  exact signed_flux_sum _ _ _ (fun e => by exact_mod_cast (character_abs e q).le) (fun e => h _)

abbrev Shear := Dir × Fin 3
def shearAxis (j : Fin 3) : spatialAxis := ⟨j.castSucc,j.castSucc_ne_last⟩

/-- Adding a spatial basis direction to time adds one magnetic row to its electric star. -/
def shear (B : TwistIndex) (a : Shear) : TwistIndex :=
  let p := inFrame a.1 B.1 B.2
  inFrame a.1 (fluxAdd p.1 (magneticRow p.2 (shearAxis a.2))) p.2

theorem changed_character : ∀ (e m q : Flux) (j : Fin 3),
    character (fluxAdd e (magneticRow m (shearAxis j))) q ≠ character e q → misaligned m q := by decide

theorem shear_bound (Z : TwistIndex → ℝ) {C : ℝ} (hc : 0 ≤ C)
    (small : ∀ i q m, misaligned m q → |fourier Z i q m| ≤ C) (B : TwistIndex) (a : Shear) :
    |Z (shear B a) - Z B| ≤ 16*C := by
  let i := a.1
  let p := inFrame i B.1 B.2
  let e' := fluxAdd p.1 (magneticRow p.2 (shearAxis a.2))
  have one : Z B = ∑ q : Flux, (character p.1 q : ℝ) * fourier Z i q p.2 := by
    rw [← invert_fourier,show inFrame i p.1 p.2 = B from inFrame_involution i B]
  have two : Z (shear B a) = ∑ q : Flux, (character e' q : ℝ) * fourier Z i q p.2 := invert_fourier Z i e' p.2
  rw [two,one,← Finset.sum_sub_distrib]
  calc
    _ ≤ ∑ q : Flux, |(character e' q : ℝ) * fourier Z i q p.2 -
        (character p.1 q : ℝ) * fourier Z i q p.2| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _ : Flux, 2*C := by
      apply Finset.sum_le_sum
      intro q _
      by_cases eq : character e' q = character p.1 q
      · simp [eq,hc]
      · have hb := small i q p.2 (changed_character p.1 p.2 q a.2 eq)
        rw [← sub_mul,abs_mul]
        have diff := abs_sub (character e' q : ℝ) (character p.1 q : ℝ)
        have abs1 (f g : Flux) : |(character f g : ℝ)| = 1 := by exact_mod_cast character_abs f g
        rw [abs1,abs1] at diff
        exact mul_le_mul (by linarith only [diff]) hb (abs_nonneg _) (by norm_num)
    _ = _ := by norm_num [Fintype.card_prod]; ring

def pureTwist (mag : Bool) (f : Flux) : TwistIndex := if mag then (zeroFlux,f) else (f,zeroFlux)
def referenceTwist : TwistIndex := ((true,false,false),zeroFlux)

/-- Paths between the pure rank-two forms used in the time comparison. Each
pair is (new time axis, spatial row in that frame). Their endpoints are checked below. -/
def comparisonPath (mag : Bool) : Flux → List Shear
  | (false,false,false) => []
  | (true,false,false)  => if mag then [(3,2),(2,2),(0,1),(1,0)] else []
  | (false,true,false)  => if mag then [(3,2),(2,2)] else [(0,1),(1,0)]
  | (true,true,false)   => if mag then [(3,2),(2,2),(1,0)] else [(1,0)]
  | (false,false,true)  => if mag then [(3,1),(1,1)] else [(0,2),(2,0)]
  | (true,false,true)   => if mag then [(3,1),(2,0),(1,1)] else [(2,0)]
  | (false,true,true)   => if mag then [(3,1),(2,1),(1,1)] else [(2,1),(0,1),(1,0)]
  | (true,true,true)    => if mag then [(3,2),(2,2),(0,0),(1,0)] else [(2,0),(1,0)]

theorem comparisonPath_spec : ∀ mag f, f ≠ zeroFlux →
    (comparisonPath mag f).foldl shear (pureTwist mag f) = referenceTwist ∧
    (comparisonPath mag f).length ≤ 4 := by decide

theorem path_bound (Z : TwistIndex → ℝ) {C : ℝ} (hc : 0 ≤ C)
    (small : ∀ i q m, misaligned m q → |fourier Z i q m| ≤ C) (B : TwistIndex) (p : List Shear) :
    |Z (p.foldl shear B) - Z B| ≤ p.length * (16*C) := by
  induction p generalizing B with
  | nil => simp
  | cons a p ih =>
    simp only [List.foldl_cons,List.length_cons,Nat.cast_add,Nat.cast_one]
    exact (abs_sub_le _ (Z (shear B a)) _).trans (by linarith only [ih (shear B a),shear_bound Z hc small B a])

theorem pure_comparison (Z : TwistIndex → ℝ) {C : ℝ} (hc : 0 ≤ C)
    (small : ∀ i q m, misaligned m q → |fourier Z i q m| ≤ C)
    (m e : Flux) (hm : m ≠ zeroFlux) (he : e ≠ zeroFlux) :
    |Z (zeroFlux,m) - Z (e,zeroFlux)| ≤ 128*C := by
  have one (mag : Bool) (f : Flux) (hf : f ≠ zeroFlux) :
      |Z referenceTwist - Z (pureTwist mag f)| ≤ 4*(16*C) := by
    obtain ⟨endpoint,dist⟩ := comparisonPath_spec mag f hf
    have h := path_bound Z hc small (pureTwist mag f) (comparisonPath mag f)
    rw [endpoint] at h
    exact h.trans (mul_le_mul_of_nonneg_right (by exact_mod_cast dist) (by positivity))
  have a := one true m hm
  have b := one false e he
  rw [abs_sub_comm] at a
  exact (abs_sub_le _ (Z referenceTwist) _).trans (by change |Z (zeroFlux,m) - Z referenceTwist| ≤ _ at a; change |Z referenceTwist - Z (e,zeroFlux)| ≤ _ at b; linarith only [a,b])

theorem short_ratio_at {t k : ℕ} (h : 3*(k+1) ≤ t) :
    (3/2 : ℝ)*(3/4)^t ≤ 1/(2:ℝ)^k := by
  calc
    _ ≤ 2*((3/4 : ℝ)^3)^(k+1) := mul_le_mul (by norm_num) (by
      rw [← pow_mul]
      exact pow_le_pow_of_le_one (by norm_num) (by norm_num) h) (by positivity) (by norm_num)
    _ ≤ 2*(1/2 : ℝ)^(k+1) := mul_le_mul_of_nonneg_left
      (pow_le_pow_left₀ (by norm_num : 0 ≤ (3/4:ℝ)^3) (by norm_num) (k+1)) (by norm_num)
    _ = _ := by rw [pow_succ,div_pow,one_pow]; ring

/-- Positivity in every crossed time frame at n-k and n+k controls its
forward difference by the second difference in the original frame. -/
theorem cube_comparisons {Γ : CubicPeriodSublattice} {β : ℝ} (hβ : 0 < β) (F : FluxSpectrum Γ β)
    {u : ℕ} (hu : 3 ≤ u) (hs : NeutralTailLE Γ β u (1/2)) (hn : 2^70 ≤ Γ.side) (hu' : 512*u ≤ Γ.side)
    (m e : Flux) (hm : m ≠ zeroFlux) (he : e ≠ zeroFlux) :
    let n := Γ.side
    let k := differenceStep n
    let Z := rawMoment Γ β
    |Z n (zeroFlux,m) - Z n (e,zeroFlux)| ≤ 1/(2:ℝ)^160 ∧
    |(Z n (zeroFlux,m)-Z (n+k) (zeroFlux,m)) - (Z n (e,zeroFlux)-Z (n+k) (e,zeroFlux))| ≤ 1/(2:ℝ)^122 := by
  let n := Γ.side
  let k := differenceStep n
  let Z := rawMoment Γ β
  let d (B : TwistIndex) := Z n B - Z (n+k) B
  let d₂ (B : TwistIndex) := Z (n+k) B + Z (n-k) B - 2*Z n B
  obtain ⟨_,_,budget,hmink⟩ := differenceStep_budget hn hu'
  have short := sectorMoment_bound Γ hβ (by omega : 2 ≤ u) hs
  have small (i : Dir) (q m : Flux) (hmis : misaligned m q) : |fourier (Z n) i q m| ≤ 1 / (2:ℝ)^169 := by
    rw [abs_of_nonneg (fourier_raw_nonneg Γ hβ (by dsimp [n]; omega) _ _ _),fourier_cube]
    have hh := (flux_moment_bounds F q m (k := 511) (by omega) (by omega : (511+1)*u ≤ n) (short q m)).2.2 hmis
    exact hh.trans (short_ratio_at (by decide))
  have second (B : TwistIndex) : |d₂ B| ≤ 8 * (1 / (2:ℝ)^133) := by
    rcases B with ⟨e,m⟩
    rw [show d₂ (e,m) = _ from invert_fourier d₂ μt e m]
    apply signed_flux_sum _ _ _ (fun q => by exact_mod_cast (character_abs e q).le)
    intro q
    change |fourier (fun B => Z (n+k) B+Z (n-k) B-2*Z n B) μt q m| ≤ _
    rw [fourier_second]
    simp only [Z,fourier_time]
    exact sector_second_difference F (by omega) budget q m (short q m)
  have tiny (i : Dir) (q m : Flux) (hmis : misaligned m q) : |fourier d i q m| ≤ 1 / (2:ℝ)^129 := by
    have hb := fourier_bound d₂ _ second i q m
    dsimp only [d₂] at hb
    rw [fourier_second] at hb
    obtain ⟨_,hb⟩ := abs_le.mp hb
    have h0 := (abs_le.mp (small i q m hmis)).2
    have posP : 0 ≤ fourier (Z (n+k)) i q m := fourier_raw_nonneg Γ hβ (by dsimp [n]; omega) i q m
    have posM : 0 ≤ fourier (Z (n-k)) i q m := fourier_raw_nonneg Γ hβ hmink i q m
    dsimp only [d]
    rw [fourier_sub,abs_le]
    constructor <;> linarith only [hb,h0,posP,posM]
  exact ⟨(pure_comparison (Z n) (by positivity) small m e hm he).trans (by norm_num),
    (pure_comparison d (by positivity) tiny m e hm he).trans (by norm_num)⟩

/-- The average over the seven nonzero temporal twists is at most the neutral
coefficient when the physical Fourier coefficients at zero magnetic flux are positive. -/
theorem pureMag_upper (Z : TwistIndex → ℝ) (m : Flux) (ε : ℝ)
    (pos : ∀ q, 0 ≤ fourier Z μt q zeroFlux)
    (cmp : ∀ e ≠ zeroFlux, Z (zeroFlux,m) - Z (e,zeroFlux) ≤ ε) :
    Z (zeroFlux,m) ≤ fourier Z μt zeroFlux zeroFlux + ε := by
  let U := (Finset.univ : Finset Flux).erase zeroFlux
  have card : U.card = 7 := by decide
  have raw : Z (zeroFlux,zeroFlux) = ∑ q : Flux, fourier Z μt q zeroFlux := by
    simpa only [inFrame_time,character_symm zeroFlux _,character_zero,Int.cast_one,one_mul] using invert_fourier Z μt zeroFlux zeroFlux
  have first : fourier Z μt zeroFlux zeroFlux ≤ Z (zeroFlux,zeroFlux) := by
    rw [raw]
    exact Finset.single_le_sum (fun q _ => pos q) (Finset.mem_univ _)
  have total : ∑ e : Flux, Z (e,zeroFlux) = 8 * fourier Z μt zeroFlux zeroFlux := by
    simp only [fourier,character_zero,Int.cast_one,one_mul]
    change _ = 8 * ((∑ e : Flux, Z (e,zeroFlux))/8)
    ring
  have splitSum := Finset.sum_erase_add (s := (Finset.univ : Finset Flux)) (fun e => Z (e,zeroFlux)) (Finset.mem_univ zeroFlux)
  have lower : ∑ _ ∈ U, (Z (zeroFlux,m) - ε) ≤ ∑ e ∈ U, Z (e,zeroFlux) :=
    Finset.sum_le_sum fun i hi => by linarith only [cmp i (Finset.mem_erase.mp hi).1]
  rw [Finset.sum_const,card,nsmul_eq_mul] at lower
  let W := ∑ e ∈ U, Z (e,zeroFlux)
  change (7:ℝ)*(Z (zeroFlux,m)-ε) ≤ W at lower
  have eq : W + Z (zeroFlux,zeroFlux) = 8*fourier Z μt zeroFlux zeroFlux := splitSum.trans total
  linarith only [first,eq,lower]

theorem untwistedElectric_sum (Γ : CubicPeriodSublattice) (β : ℝ) (t : ℕ) (m : Flux) :
    rawMoment Γ β t (zeroFlux,m) = ∑ q : Flux, sectorMoment Γ β q m t := by
  simpa only [inFrame_time,character_symm zeroFlux _,character_zero,Int.cast_one,one_mul,fourier_time] using invert_fourier (rawMoment Γ β t) μt zeroFlux m

theorem level_drop_bounds {Γ : CubicPeriodSublattice} {β : ℝ} (F : FluxSpectrum Γ β)
    (q m : Flux) {t : ℕ} (ht : 2 ≤ t) (k : ℕ) :
    let ρ := F.level q m 0
    0 ≤ sectorMoment Γ β q m t - sectorMoment Γ β q m (t+k) ∧
    ρ ^ t * (1 - ρ^k) ≤ sectorMoment Γ β q m t - sectorMoment Γ β q m (t+k) := by
  let v := F.level q m
  have allS := (F.moment q m t ht).sub (F.moment q m (t+k) (by omega))
  have each (i : ℕ) : 0 ≤ v i ^ t - v i^(t+k) := sub_nonneg.mpr
    (pow_le_pow_of_le_one (F.nonneg _ _ _) (F.le_one _ _ _) (by omega))
  have one := allS.summable.le_tsum 0 (fun j _ => each j)
  rw [allS.tsum_eq] at one
  refine ⟨(each 0).trans one,?_⟩
  change v 0^t * (1-v 0^k) ≤ _
  calc
    _ = v 0^t-v 0^(t+k) := by rw [pow_add]; ring
    _ ≤ _ := one

/-- The original time frame has nonnegative moment drops. Lower bounding the
magnetic mass by both the neutral and the aligned sector bounds the aligned
top level away from one. Its forward drop then bounds that same level near zero.
This uses the same inequalities in both flux alternatives. -/
theorem aligned_half_small {Γ : CubicPeriodSublattice} {β : ℝ} (hβ : 0 < β) (F : FluxSpectrum Γ β)
    {u : ℕ} (hu : 3 ≤ u) (hs : NeutralTailLE Γ β u (1/2)) (hn : 2^70 ≤ Γ.side) (hu' : 512*u ≤ Γ.side)
    (hd : 4 ∣ Γ.side) (m : Flux) (hm : m ≠ zeroFlux) : F.level m m 0 ^ (Γ.side/2) ≤ 1/(2:ℝ)^22 := by
  let n := Γ.side
  let k := differenceStep n
  let Z := rawMoment Γ β
  let X := sectorMoment Γ β
  let ρ := F.level m m 0
  have hn2 : 2 ≤ n := by dsimp [n]; omega
  have hnk : 2 ≤ n+k := by omega
  have non (q m : Flux) (t : ℕ) (ht : 2 ≤ t) : 0 ≤ X q m t := by
    change 0 ≤ sectorMoment Γ β q m t
    rw [← fourier_time]; exact fourier_raw_nonneg Γ hβ ht μt q m
  have oneLE (t : ℕ) (ht : 2 ≤ t) : 1 ≤ X zeroFlux zeroFlux t := by
    have s := F.moment zeroFlux zeroFlux t ht
    have b := s.summable.le_tsum 0 (fun j _ => pow_nonneg (F.nonneg _ _ _) _)
    simpa only [s.tsum_eq,F.vacuum,one_pow] using b
  have neutral : X zeroFlux zeroFlux n ≤ 1+1/(2:ℝ)^169 := by
    have t := (flux_moment_bounds F zeroFlux zeroFlux (k := 511) (by omega : 2 ≤ u) hu'
      (sectorMoment_bound Γ hβ (by omega) hs _ _)).2.1
    rw [F.vacuum,one_pow] at t
    have small : (3/2:ℝ)*(3/4)^511 ≤ 1/(2:ℝ)^169 := short_ratio_at (by decide)
    change X zeroFlux zeroFlux n - 1 ≤ _ at t
    exact (sub_le_iff_le_add.mp (t.trans small)).trans_eq (add_comm _ _)
  have cmp := fun (e : Flux) (he : e ≠ zeroFlux) => cube_comparisons hβ F hu hs hn hu' m e hm he
  have mass : Z n (zeroFlux,m) ≤ 3/2 := by
    have h := pureMag_upper (Z n) m _ (fun q => fourier_raw_nonneg Γ hβ hn2 μt q zeroFlux)
      (fun e he => (abs_le.mp (cmp e he).1).2)
    rw [fourier_time] at h
    linarith only [h,neutral]
  have drop : Z n (zeroFlux,m)-Z (n+k) (zeroFlux,m) ≤ 1/(2:ℝ)^121 := by
    have h := pureMag_upper (fun B => Z n B - Z (n+k) B) m (1/(2:ℝ)^122) (fun q => by
      rw [fourier_sub,fourier_time,fourier_time]; exact (level_drop_bounds F q zeroFlux hn2 k).1)
      (fun e he => (abs_le.mp (cmp e he).2).2)
    rw [fourier_sub,fourier_time,fourier_time] at h
    linarith only [h,neutral,oneLE (n+k) hnk]
  have ss := F.moment m m n hn2
  have a := ss.summable.le_tsum 0 (fun j _ => pow_nonneg (F.nonneg _ _ _) _)
  rw [ss.tsum_eq] at a
  have b : X m m n ≤ X zeroFlux m n := div_le_div_of_nonneg_right (sectorWeight_le_neutral _ _ _ _)
    (pow_nonneg (norm_nonneg _) _)
  have two : X zeroFlux m n + X m m n ≤ Z n (zeroFlux,m) := by
    dsimp only [Z]
    rw [untwistedElectric_sum,← Finset.sum_pair hm.symm (f := fun q => X q m n)]
    exact Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ _) (fun q _ _ => non q m n hn2)
  have gap : ρ^n ≤ 3/4 := by linarith only [a,b,two,mass]
  have dx : ρ^n * (1-ρ^k) ≤ 1/(2:ℝ)^121 := by
    dsimp only [Z] at drop
    rw [untwistedElectric_sum,untwistedElectric_sum,← Finset.sum_sub_distrib] at drop
    exact (level_drop_bounds F m m hn2 k).2.trans ((Finset.single_le_sum
      (fun q _ => (level_drop_bounds F q m hn2 k).1) (Finset.mem_univ m)).trans drop)
  have between := (differenceStep_budget hn hu').2.1
  have power : (ρ^k)^(2^70) ≤ ρ^n := by
    rw [← pow_mul,Nat.mul_comm k]
    exact pow_le_pow_of_le_one (F.nonneg m m 0) (F.le_one m m 0) between
  have geom : 1-(ρ^k)^(2^70) ≤ (2:ℝ)^70*(1-ρ^k) := by
    rw [← show ((2^70 : ℕ) : ℝ) = (2:ℝ)^70 by norm_num]
    exact (geometric_loss (pow_nonneg (F.nonneg m m 0) k) (pow_le_one₀ (F.nonneg m m 0) (F.le_one m m 0)) (2^70)).2
  have loss : 1-ρ^n ≤ (2:ℝ)^70*(1-ρ^k) := (sub_le_sub_left power 1).trans geom
  have product := mul_le_mul_of_nonneg_left loss (pow_nonneg (F.nonneg m m 0) n)
  have away := mul_le_mul_of_nonneg_left gap (pow_nonneg (F.nonneg m m 0) n)
  have tiny : ρ^n ≤ 1/(2:ℝ)^49 := by nlinarith only [dx,product,away]
  have even : n/2*2=n := by dsimp [n]; obtain ⟨z,hz⟩ := hd; omega
  have sq : (ρ^(n/2))^2 = ρ^n := by rw [← pow_mul,even]
  change ρ^(n/2) ≤ _
  by_contra! big
  have := (sq_lt_sq₀ (by norm_num : 0 ≤ 1/(2:ℝ)^22) (pow_nonneg (F.nonneg m m 0) (n/2))).2 big
  rw [sq] at this
  linarith only [this,tiny]

theorem kappaSeed_of_neutralPhysicalSeed (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (hfour : 4 ∣ Γ.side) (hlarge : 2 ^ 70 ≤ Γ.side) (hs : NeutralPhysicalSeed Γ β) :
    KappaSeedOnCube Γ β := by
  obtain ⟨u,hu,hside,hs⟩ := hs
  obtain ⟨F⟩ := cubeFluxSpectrum Γ hβ hfour
  let t := Γ.side/2
  have sides : (fun i : Dir => if i=μt then t else Γ.side) = boxSides (cube Γ.side) t := by
    funext i; fin_cases i <;> rfl
  have tail (m : Flux) : sectorMoment Γ β m m t - F.level m m 0 ^ t ≤ 1/(2:ℝ)^84 :=
    (flux_moment_bounds F m m (k := 255) (by omega : 2 ≤ u) (by dsimp [t]; omega)
      (sectorMoment_bound Γ hβ (by omega) hs _ _)).2.1.trans (short_ratio_at (by decide))
  have nonzero (m : Flux) (hm : m ≠ zeroFlux) : sectorMoment Γ β m m t ≤ 1/(2:ℝ)^22 + 1/(2:ℝ)^84 := by
    linarith only [tail m,aligned_half_small hβ F hu hs hlarge hside hfour m hm]
  have atZero := tail zeroFlux
  rw [F.vacuum,one_pow] at atZero
  let U := (Finset.univ : Finset Flux).erase zeroFlux
  have card : U.card = 7 := by decide
  have sum := Finset.sum_le_sum (s := U) (fun m hm => nonzero m (Finset.mem_erase.mp hm).1)
  simp only [Finset.sum_const,card,nsmul_eq_mul] at sum
  have splitSum := Finset.sum_erase_add (s := (Finset.univ : Finset Flux)) (fun m => sectorMoment Γ β m m t) (Finset.mem_univ zeroFlux)
  refine ⟨(boxNeutral_norm_pos (cube Γ.side) hβ.le).trans_eq (calibrated_cubicNorm Γ hβ),?_⟩
  rw [sides,kappaWeight_eq_diagonal,Finset.sum_div]
  change (∑ m : Flux, sectorMoment Γ β m m t)-1 < _
  linarith only [sum,splitSum,atZero]

example : type_of% @GapChain.kappaSeed_of_neutralPhysicalSeed := @kappaSeed_of_neutralPhysicalSeed

end GapChain.Stage4

#print axioms GapChain.Stage4.releaseSectorBasis
#print axioms GapChain.Stage4.pwTrace_of_eigenbasis
#print axioms GapChain.Stage4.projected_power
#print axioms GapChain.Stage4.projectedTrace_eq_sectorWeight
#print axioms GapChain.Stage4.periodicTransfer_norm_pos
#print axioms GapChain.Stage4.neutralTail_iff_sectorWeight
#print axioms GapChain.Stage4.neutral_projection_norm_le
#print axioms GapChain.Stage4.neutralTail_after_rankOne
#print axioms GapChain.Stage4.neutralTail_of_rankOneAtTime
#print axioms GapChain.Stage4.inFrame_time
#print axioms GapChain.Stage4.inFrame_planes
#print axioms GapChain.Stage4.raw_in_frame
#print axioms GapChain.Stage4.crossed_neutral_sum
#print axioms GapChain.Stage4.crossed_erasure
#print axioms GapChain.Stage4.sectorWeight_le_periodicNeutral
#print axioms GapChain.Stage4.cubeSides_ge_two
#print axioms GapChain.Stage4.sectorMoment_bound
#print axioms GapChain.Stage4.excited_slot_le
#print axioms GapChain.Stage4.tail_at_multiple
#print axioms GapChain.Stage4.magneticBit_diag
#print axioms GapChain.Stage4.magneticBit_symm
#print axioms GapChain.Stage4.magneticBit_plane
#print axioms GapChain.Stage4.misaligned_row
#print axioms GapChain.Stage4.halfTurn_val
#print axioms GapChain.Stage4.halfTurn_twice
#print axioms GapChain.Stage4.finRotate_val_if
#print axioms GapChain.Stage4.halfTurn_rotate
#print axioms GapChain.Stage4.inStrip_halfTurn
#print axioms GapChain.Stage4.inStrip_boundary
#print axioms GapChain.Stage4.shiftedSite_twice
#print axioms GapChain.Stage4.shift_rectStep
#print axioms GapChain.Stage4.strip_curl
#print axioms GapChain.Stage4.strip_squared
#print axioms GapChain.Stage4.compensated_sq
#print axioms GapChain.Stage4.pi_pull_involution
#print axioms GapChain.Stage4.compensated_apply
#print axioms GapChain.Stage4.compensated_preserving
#print axioms GapChain.Stage4.rectStep_comm
#print axioms GapChain.Stage4.rectFace_spatial
#print axioms GapChain.Stage4.compensated_word
#print axioms GapChain.Stage4.compensated_action
#print axioms GapChain.Stage4.compensated_temporal
#print axioms GapChain.Stage4.compensated_gauge
#print axioms GapChain.Stage4.compensated_kernel
#print axioms GapChain.Stage4.rectHalfWeight_gauge
#print axioms GapChain.Stage4.rectSymKernel_gauge_right
#print axioms GapChain.Stage4.compensated_flip
#print axioms GapChain.Stage4.compensated_electricEntry
#print axioms GapChain.Stage4.pull_operator_commutes
#print axioms GapChain.Stage4.sliceConj_smul
#print axioms GapChain.Stage4.pull_conjugate
#print axioms GapChain.Stage4.real_kernel_conjugate
#print axioms GapChain.Stage4.rectSector_conjugate
#print axioms GapChain.Stage4.magneticShift_square
#print axioms GapChain.Stage4.magneticShift_commutes
#print axioms GapChain.Stage4.translation_on_sector
#print axioms GapChain.Stage4.finrank_ne_one_of_antilinear
#print axioms GapChain.Stage4.misaligned_not_simple
#print axioms GapChain.Stage4.slot_le_of_moments
#print axioms GapChain.Stage4.misaligned_partner
#print axioms GapChain.Stage4.cubeFluxSpectrum
#print axioms GapChain.Stage4.flux_moment_bounds
#print axioms GapChain.Stage4.geometric_loss
#print axioms GapChain.Stage4.differenceStep_budget
#print axioms GapChain.Stage4.second_difference_term
#print axioms GapChain.Stage4.second_difference_identity
#print axioms GapChain.Stage4.sector_second_difference
#print axioms GapChain.Stage4.inFrame_involution
#print axioms GapChain.Stage4.invert_fourier
#print axioms GapChain.Stage4.fourier_raw
#print axioms GapChain.Stage4.fourier_time
#print axioms GapChain.Stage4.boxSides_cube_diag
#print axioms GapChain.Stage4.fourier_cube
#print axioms GapChain.Stage4.fourier_raw_nonneg
#print axioms GapChain.Stage4.fourier_sub
#print axioms GapChain.Stage4.fourier_second
#print axioms GapChain.Stage4.character_abs
#print axioms GapChain.Stage4.signed_flux_sum
#print axioms GapChain.Stage4.fourier_bound
#print axioms GapChain.Stage4.changed_character
#print axioms GapChain.Stage4.shear_bound
#print axioms GapChain.Stage4.comparisonPath_spec
#print axioms GapChain.Stage4.path_bound
#print axioms GapChain.Stage4.pure_comparison
#print axioms GapChain.Stage4.short_ratio_at
#print axioms GapChain.Stage4.cube_comparisons
#print axioms GapChain.Stage4.pureMag_upper
#print axioms GapChain.Stage4.untwistedElectric_sum
#print axioms GapChain.Stage4.level_drop_bounds
#print axioms GapChain.Stage4.aligned_half_small
#print axioms GapChain.Stage4.kappaSeed_of_neutralPhysicalSeed
