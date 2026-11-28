import GapChain.Stage0
import GapChain.Trace

/-!
# The calibrated Pfaffian seed

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
supply the YM4 release and its transfer convention. The Pfaffian construction
follows rows 731 and 1004, with the interfaces of rows 1457 and 1458. Stage 0 fixes the six plaquette
stacks, the release time coordinate 3 and the periodic transfer normalization.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open Filter MeasureTheory
open scoped BigOperators ENNReal Topology
open YangMills YangMills.Construction
open TransferOperators SeparatedTuples ReflectionPositivity.TupleForm ReflectionPositivity.Reconstruction LimitTheorem
open GapChain.Wilson (Dir Sides Site Config Plane halfTrace transport)

namespace GapChain.Stage3

section Crossing

/-- The unique increasing orientation of two distinct axes. -/
def planeOf (i j : Dir) (hij : i ≠ j) : Plane :=
  if h : i < j then ⟨(i, j), h⟩ else ⟨(j, i), lt_of_le_of_ne (le_of_not_gt h) hij.symm⟩

theorem planeOf_swap (i j : Dir) (hij : i ≠ j) :
    planeOf j i hij.symm = planeOf i j hij := by
  rcases lt_or_gt_of_ne hij with h | h <;> simp [planeOf, h, h.not_gt]

def mapPlane (σ : Equiv.Perm Dir) (p : Plane) : Plane :=
  planeOf (σ p.val.1) (σ p.val.2) (σ.injective.ne p.property.ne)

theorem mapPlane_planeOf (σ : Equiv.Perm Dir) (i j : Dir) (hij : i ≠ j) :
    mapPlane σ (planeOf i j hij) = planeOf (σ i) (σ j) (σ.injective.ne hij) := by
  rcases lt_or_gt_of_ne hij with h | h
  · rw [planeOf, dif_pos h]
    rfl
  · rw [planeOf, dif_neg h.not_gt]
    exact planeOf_swap _ _ _

theorem mapPlane_mul (σ τ : Equiv.Perm Dir) (p : Plane) :
    mapPlane (σ * τ) p = mapPlane σ (mapPlane τ p) :=
  (mapPlane_planeOf σ _ _ _).symm

theorem mapPlane_one (p : Plane) : mapPlane 1 p = p := by
  rcases p with ⟨⟨i, j⟩, h⟩
  simp [mapPlane, planeOf, h]

def planePerm (σ : Equiv.Perm Dir) : Equiv.Perm Plane where
  toFun := mapPlane σ
  invFun := mapPlane σ⁻¹
  left_inv p := by rw [← mapPlane_mul, inv_mul_cancel, mapPlane_one]
  right_inv p := by rw [← mapPlane_mul, mul_inv_cancel, mapPlane_one]

/-- One face contribution. Reversing the orientation preserves both its stack test and its trace. -/
def faceAction {s : Sides} (U : Config s) (x : Site s) (b : Bool) (i j : Dir) : ℝ :=
  1 - (if b = true ∧ (x i).val = 0 ∧ (x j).val = 0 then -1 else 1) *
    halfTrace (transport U x i j)

theorem faceAction_swap {s : Sides} (U : Config s) (x : Site s) (b : Bool) (i j : Dir) :
    faceAction U x b j i = faceAction U x b i j := by
  have h : ((x j).val = 0 ∧ (x i).val = 0) ↔ ((x i).val = 0 ∧ (x j).val = 0) := and_comm
  simp only [faceAction, Wilson.halfTrace_reverse U x i j, h]

theorem faceAction_planeOf {s : Sides} (U : Config s) (x : Site s) (b : Bool)
    (i j : Dir) (hij : i ≠ j) :
    faceAction U x b (planeOf i j hij).val.1 (planeOf i j hij).val.2 = faceAction U x b i j := by
  by_cases h : i < j
  · simp [planeOf, h]
  · simpa only [planeOf, dif_neg h] using faceAction_swap U x b i j

theorem faceAction_relabel (s : Sides) (σ : Equiv.Perm Dir) (U : Config s)
    (x : Site (s ∘ σ)) (b : Bool) (p : Plane) :
    faceAction (Wilson.relabel s σ U) x b p.val.1 p.val.2 =
      faceAction U (Wilson.siteEquiv s σ x) b (mapPlane σ p).val.1 (mapPlane σ p).val.2 := by
  rw [mapPlane, faceAction_planeOf]
  have he := Wilson.faceTrace_relabel s σ U (x, ⟨p.val, p.property.ne⟩)
  change halfTrace (transport _ x p.val.1 p.val.2) =
    halfTrace (transport U (Wilson.siteEquiv s σ x) (σ p.val.1) (σ p.val.2)) at he
  simp only [faceAction, he, Wilson.siteEquiv, Equiv.piCongrLeft_apply_apply]

/-- W3 for the actual signed integrals on rectangular tori, for every side permutation. -/
theorem twistedPartition_permute (β : ℝ) (s : Sides) (σ : Equiv.Perm Dir) (k : Plane → Bool) :
    twistedPartition β (s ∘ σ) (k ∘ mapPlane σ) = twistedPartition β s k := by
  let density (n : Sides) (bits : Plane → Bool) (U : Config n) :=
    Real.exp (-β * ∑ x : Site n, ∑ p : Plane, faceAction U x (bits p) p.val.1 p.val.2)
  change (∫ U, density _ _ U ∂Wilson.haar _) = ∫ U, density s k U ∂Wilson.haar s
  rw [← (Wilson.measurePreserving_relabel s σ).integral_comp' (density _ _)]
  apply integral_congr_ae
  filter_upwards with U
  dsimp only [density, Function.comp_apply]
  congr 2
  rw [← (Wilson.siteEquiv s σ).sum_comp (fun x => ∑ p : Plane, faceAction U x (k p) p.val.1 p.val.2)]
  apply Finset.sum_congr rfl
  intro x _
  rw [← Equiv.sum_comp (planePerm σ) (fun p => faceAction U (Wilson.siteEquiv s σ x) (k p) p.val.1 p.val.2)]
  exact Finset.sum_congr rfl fun p _ => faceAction_relabel s σ U x _ p

set_option maxHeartbeats 2000000 in
/-- The three complementary pairs are permuted by each transposition. -/
theorem pfaffianSign_swap (i j : Dir) (k : Plane → Bool) :
    pfaffianSign (k ∘ mapPlane (Equiv.swap i j)) = pfaffianSign k := by
  let s (a b : Bool) : ℝ := if a && b then -1 else 1
  have hcomm (p q : Bool) : s p q = s q p := by dsimp [s]; rw [Bool.and_comm p q]
  let a := k ⟨(0, 1), by decide⟩
  let b := k ⟨(0, 2), by decide⟩
  let c := k ⟨(0, 3), by decide⟩
  let d := k ⟨(1, 2), by decide⟩
  let e := k ⟨(1, 3), by decide⟩
  let f := k ⟨(2, 3), by decide⟩
  have perm021 (x y z : ℝ) : x * z * y = x * y * z := by ac_rfl
  have perm210 (x y z : ℝ) : z * y * x = x * y * z := by ac_rfl
  have perm102 (x y z : ℝ) : y * x * z = x * y * z := by ac_rfl
  fin_cases i <;> fin_cases j
  · rfl
  · change s a f * s d c * s e b = s a f * s b e * s c d
    rw [hcomm d c, hcomm e b]
    exact perm021 _ _ _
  · change s d c * s b e * s f a = s a f * s b e * s c d
    rw [hcomm d c, hcomm f a]
    exact perm210 _ _ _
  · change s e b * s f a * s c d = s a f * s b e * s c d
    rw [hcomm e b, hcomm f a]
    exact perm102 _ _ _
  · change s a f * s d c * s e b = s a f * s b e * s c d
    rw [hcomm d c, hcomm e b]
    exact perm021 _ _ _
  · rfl
  · change s b e * s a f * s c d = s a f * s b e * s c d
    exact perm102 _ _ _
  · change s c d * s b e * s a f = s a f * s b e * s c d
    exact perm210 _ _ _
  · change s d c * s b e * s f a = s a f * s b e * s c d
    rw [hcomm d c, hcomm f a]
    exact perm210 _ _ _
  · change s b e * s a f * s c d = s a f * s b e * s c d
    exact perm102 _ _ _
  · rfl
  · change s a f * s c d * s b e = s a f * s b e * s c d
    exact perm021 _ _ _
  · change s e b * s f a * s c d = s a f * s b e * s c d
    rw [hcomm e b, hcomm f a]
    exact perm102 _ _ _
  · change s c d * s b e * s a f = s a f * s b e * s c d
    exact perm210 _ _ _
  · change s a f * s c d * s b e = s a f * s b e * s c d
    exact perm021 _ _ _
  · rfl


theorem pfaffianSign_permute (σ : Equiv.Perm Dir) (k : Plane → Bool) :
    pfaffianSign (k ∘ mapPlane σ) = pfaffianSign k := by
  induction σ using Equiv.Perm.swap_induction_on generalizing k with
  | one => simp [Function.comp_def, mapPlane_one]
  | swap_mul σ i j _ ih =>
    calc
      _ = pfaffianSign ((k ∘ mapPlane (Equiv.swap i j)) ∘ mapPlane σ) := by
        congr 1; funext p; exact congrArg k (mapPlane_mul _ _ p)
      _ = _ := (ih _).trans (pfaffianSign_swap i j k)

/-- Lemma W(a) for the Pfaffian weight, including permutations exchanging time and space. -/
theorem kappaWeight_permute (β : ℝ) (s : Sides) (σ : Equiv.Perm Dir) :
    kappaWeight β (s ∘ σ) = kappaWeight β s := by
  classical
  let pull : (Plane → Bool) ≃ (Plane → Bool) :=
    (planePerm σ).symm.arrowCongr (Equiv.refl Bool)
  have ep (k : Plane → Bool) : pull k = k ∘ mapPlane σ := rfl
  unfold kappaWeight
  rw [← pull.sum_comp (fun k => pfaffianSign k * twistedPartition β (s ∘ σ) k)]
  simp only [ep, pfaffianSign_permute, twistedPartition_permute]

end Crossing

section Sectors

/-- Spatial components in the order 0,1,2. Time has index 3. -/
abbrev Flux := Bool × Bool × Bool

/-- Electric components are 03, 13, 23. Their complementary magnetic planes are 12, 02, 01. -/
def joinTwist (e m : Flux) (p : Plane) : Bool :=
  match p.val.1.val, p.val.2.val with
  | 0, 3 => e.1
  | 1, 3 => e.2.1
  | 2, 3 => e.2.2
  | 1, 2 => m.1
  | 0, 2 => m.2.1
  | _, _ => m.2.2

def fluxEquiv : Flux × Flux ≃ (Plane → Bool) where
  toFun v := joinTwist v.1 v.2
  invFun k :=
    ((k ⟨(0, 3), by decide⟩, k ⟨(1, 3), by decide⟩, k ⟨(2, 3), by decide⟩),
     (k ⟨(1, 2), by decide⟩, k ⟨(0, 2), by decide⟩, k ⟨(0, 1), by decide⟩))
  left_inv _ := rfl
  right_inv k := by
    funext ⟨⟨i, j⟩, hij⟩
    fin_cases i <;> fin_cases j <;> first | rfl | exact absurd hij (by decide)

def character (e χ : Flux) : ℤ :=
  let sign (a b : Bool) : ℤ := if a && b then -1 else 1
  sign e.1 χ.1 * sign e.2.1 χ.2.1 * sign e.2.2 χ.2.2

theorem pfaffianSign_join (e m : Flux) :
    pfaffianSign (joinTwist e m) = (character e m : ℝ) := by
  let z (a b : Bool) : ℤ := if a && b then -1 else 1
  let v (a b : Bool) : ℝ := if a && b then -1 else 1
  have hc (a b : Bool) : (z a b : ℝ) = v a b := by
    cases a <;> cases b <;> norm_num [z, v]
  change v m.2.2 e.2.2 * v m.2.1 e.2.1 * v e.1 m.1 =
    ((z e.1 m.1 * z e.2.1 m.2.1 * z e.2.2 m.2.2 : ℤ) : ℝ)
  simp only [Int.cast_mul, hc, v, Bool.and_comm, mul_comm, mul_left_comm]

/-- Orthogonality of the eight characters with counting measure. -/
theorem character_orthogonal : ∀ χ m : Flux,
    (∑ e : Flux, character e χ * character e m) = if χ = m then 8 else 0 := by
  decide

/-- The electric Fourier coefficient of the *actual* six-stack partition function. -/
def sectorWeight (β : ℝ) (s : Sides) (χ m : Flux) : ℝ :=
  (∑ e : Flux, (character e χ : ℝ) * twistedPartition β s (joinTwist e m)) / 8

/-- The Pfaffian selects the eight diagonal electric/magnetic sectors. -/
theorem kappaWeight_eq_diagonal (β : ℝ) (s : Sides) :
    kappaWeight β s = ∑ m : Flux, sectorWeight β s m m := by
  unfold kappaWeight sectorWeight
  rw [← fluxEquiv.sum_comp (fun k => pfaffianSign k * twistedPartition β s k)]
  change (∑ em : Flux × Flux, pfaffianSign (joinTwist em.1 em.2) *
    twistedPartition β s (joinTwist em.1 em.2)) / 8 = _
  rw [Fintype.sum_prod_type_right]
  simp only [pfaffianSign_join, Finset.sum_div]

/-- Every twisted Wilson integrand is positive, including in a magnetic background. -/
theorem twistedPartition_pos (β : ℝ) (s : Sides) (k : Plane → Bool) : 0 < twistedPartition β s k := by
  unfold twistedPartition
  apply integral_exp_pos
  apply Continuous.integrable_of_hasCompactSupport _ (HasCompactSupport.of_compactSpace _)
  apply Real.continuous_exp.comp
  apply continuous_const.mul
  refine continuous_finsetSum Finset.univ (fun (x : Site s) _ => ?_)
  refine continuous_finsetSum Finset.univ (fun (p : Plane) _ => ?_)
  exact continuous_const.sub (continuous_const.mul (Wilson.continuous_faceTrace
    (n := s) (x, ⟨p.val, p.property.ne⟩)))

theorem character_symm : ∀ e χ : Flux, character e χ = character χ e := by decide

theorem character_le_one : ∀ e χ : Flux, character e χ ≤ 1 := by decide

/-- The three independent electric cuts, expressed in Stage 0's time-axis convention. -/
def fluxBit (e : Flux) (i : Dir) : Bool := ![e.1, e.2.1, e.2.2, false] i

def zeroFlux : Flux := (false, false, false)

theorem join_zero (p : Plane) : joinTwist zeroFlux zeroFlux p = false := by
  obtain ⟨⟨i, j⟩, hij⟩ := p
  fin_cases i <;> fin_cases j <;> rfl

theorem character_zero : ∀ e : Flux, character e zeroFlux = 1 := by decide

/-- S1 follows already from positivity of each original partition integral. -/
theorem sectorWeight_le_neutral (β : ℝ) (s : Sides) (χ m : Flux) :
    sectorWeight β s χ m ≤ sectorWeight β s zeroFlux m := by
  unfold sectorWeight
  apply div_le_div_of_nonneg_right _ (by norm_num)
  apply Finset.sum_le_sum
  intro e _
  rw [character_zero]
  exact mul_le_mul_of_nonneg_right (by exact_mod_cast character_le_one e χ)
    (twistedPartition_pos β s _).le

/-- Fourier inversion recovers each of the original 64 twisted partition integrals. -/
theorem twistedPartition_eq_sectorSum (β : ℝ) (s : Sides) (e m : Flux) :
    twistedPartition β s (joinTwist e m) =
      ∑ χ : Flux, (character e χ : ℝ) * sectorWeight β s χ m := by
  classical
  let Z (f : Flux) := twistedPartition β s (joinTwist f m)
  have orth (f : Flux) : (∑ χ : Flux, (character e χ : ℝ) * (character f χ : ℝ)) =
      if e = f then 8 else 0 := by
    have h := character_orthogonal e f
    simp_rw [character_symm e, character_symm f]
    split_ifs at h ⊢ <;> exact_mod_cast h
  unfold sectorWeight
  change Z e = ∑ χ : Flux, (character e χ : ℝ) * ((∑ f : Flux, (character f χ : ℝ) * Z f) / 8)
  simp only [mul_div_assoc', Finset.mul_sum, ← mul_assoc]
  rw [← Finset.sum_div, Finset.sum_comm]
  simp_rw [← Finset.sum_mul, orth]
  simp [ite_mul]

/-- The remaining sign needed for electric untwisting is positivity of the sector traces. -/
theorem electric_untwist (β : ℝ) (s : Sides) (e m : Flux)
    (hp : ∀ χ, 0 ≤ sectorWeight β s χ m) :
    twistedPartition β s (joinTwist e m) ≤ twistedPartition β s (joinTwist zeroFlux m) := by
  rw [twistedPartition_eq_sectorSum β s e m, twistedPartition_eq_sectorSum β s zeroFlux m]
  apply Finset.sum_le_sum
  intro χ _
  rw [character_symm zeroFlux χ, character_zero]
  exact mul_le_mul_of_nonneg_right (by exact_mod_cast character_le_one e χ) (hp χ)


/-- Erase the electric components for a chosen time direction while keeping every
magnetic component. -/
def eraseIncident (i : Dir) (k : Plane → Bool) (p : Plane) : Bool :=
  if p.val.1 = i ∨ p.val.2 = i then false else k p

theorem eraseIncident_map (σ : Equiv.Perm Dir) (i : Dir) (k : Plane → Bool) :
    eraseIncident i (k ∘ mapPlane σ) = eraseIncident (σ i) k ∘ mapPlane σ := by
  funext p
  have h (a b : Dir) (hne : a ≠ b) :
      ((planeOf a b hne).val.1 = σ i ∨ (planeOf a b hne).val.2 = σ i) ↔
        a = σ i ∨ b = σ i := by
    by_cases hab : a < b <;> simp only [planeOf, hab, dite_true, dite_false]
    exact or_comm
  simp only [eraseIncident, Function.comp_apply, mapPlane, h, Equiv.apply_eq_iff_eq]

theorem eraseIncident_time (e m : Flux) :
    eraseIncident TimeAxis.timeIdx (joinTwist e m) = joinTwist zeroFlux m := by
  funext ⟨⟨i, j⟩, hij⟩
  fin_cases i <;> fin_cases j <;> first | rfl | exact absurd hij (by decide)

/-- Given electric sector positivity in every permuted frame, untwist any incident
plane set on the *same* torus. -/
theorem untwist_axis {β : ℝ} {s : Sides}
    (hp : ∀ (σ : Equiv.Perm Dir) (χ m : Flux), 0 ≤ sectorWeight β (s ∘ σ) χ m)
    (k : Plane → Bool) (i : Dir) :
    twistedPartition β s k ≤ twistedPartition β s (eraseIncident i k) := by
  let σ := Equiv.swap TimeAxis.timeIdx i
  have he : σ TimeAxis.timeIdx = i := Equiv.swap_apply_left _ _
  rw [← twistedPartition_permute β s σ k, ← twistedPartition_permute β s σ (eraseIncident i k)]
  have hc := eraseIncident_map σ TimeAxis.timeIdx k
  rw [he] at hc
  rw [← hc]
  obtain ⟨⟨e, m⟩, hem⟩ := fluxEquiv.surjective (k ∘ mapPlane σ)
  change joinTwist e m = _ at hem
  rw [← hem, eraseIncident_time]
  exact electric_untwist _ _ _ _ (fun χ => hp σ χ m)

/-- S2 of TW-T. Three choices of time remove all six plane bits. -/
theorem all_twists_le_periodic {β : ℝ} {s : Sides}
    (hp : ∀ (σ : Equiv.Perm Dir) (χ m : Flux), 0 ≤ sectorWeight β (s ∘ σ) χ m)
    (k : Plane → Bool) : twistedPartition β s k ≤ Wilson.partition β s := by
  let k₁ := eraseIncident 0 k
  let k₂ := eraseIncident 1 k₁
  have he : eraseIncident 2 k₂ = fun _ => false := by
    funext ⟨⟨i, j⟩, hij⟩
    fin_cases i <;> fin_cases j <;> first | rfl | exact absurd hij (by decide)
  calc
    _ ≤ twistedPartition β s k₁ := untwist_axis hp k 0
    _ ≤ twistedPartition β s k₂ := untwist_axis hp k₁ 1
    _ ≤ twistedPartition β s (eraseIncident 2 k₂) := untwist_axis hp k₂ 2
    _ = _ := by rw [he, twistedPartition_untwisted]

/-- The neutral periodic coefficient contains the untwisted integral with weight 1/8. -/
theorem partition_div_eight_le_neutral (β : ℝ) (s : Sides) :
    Wilson.partition β s / 8 ≤ sectorWeight β s zeroFlux zeroFlux := by
  have hz : joinTwist zeroFlux zeroFlux = fun _ => false := funext join_zero
  unfold sectorWeight
  simp only [character_zero, Int.cast_one, one_mul]
  rw [← twistedPartition_untwisted β s, ← hz]
  exact div_le_div_of_nonneg_right
    (Finset.single_le_sum (fun (e : Flux) _ => (twistedPartition_pos β s (joinTwist e zeroFlux)).le)
      (Finset.mem_univ zeroFlux)) (by norm_num)

/-- After untwisting, every Fourier sector is at most eight times the neutral
periodic sector. This comparison holds before taking roots in the time length. -/
theorem sectorWeight_le_eight_neutral {β : ℝ} {s : Sides}
    (hp : ∀ (σ : Equiv.Perm Dir) (χ m : Flux), 0 ≤ sectorWeight β (s ∘ σ) χ m) (χ m : Flux) :
    sectorWeight β s χ m ≤ 8 * sectorWeight β s zeroFlux zeroFlux := by
  calc
    _ ≤ sectorWeight β s zeroFlux m := sectorWeight_le_neutral _ _ _ _
    _ ≤ Wilson.partition β s := by
      unfold sectorWeight
      simp only [character_zero, Int.cast_one, one_mul]
      apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 8)).mpr
      calc
        _ ≤ ∑ _ : Flux, Wilson.partition β s :=
          Finset.sum_le_sum fun _ _ => all_twists_le_periodic hp _
        _ = _ := by norm_num [Fintype.card_prod] <;> ring
    _ ≤ _ := by linarith only [partition_div_eight_le_neutral β s]


theorem partition_div_eight_le_kappa (β : ℝ) (s : Sides)
    (hp : ∀ m, 0 ≤ sectorWeight β s m m) : Wilson.partition β s / 8 ≤ kappaWeight β s := by
  rw [kappaWeight_eq_diagonal]
  exact (partition_div_eight_le_neutral β s).trans
    (Finset.single_le_sum (fun m _ => hp m) (Finset.mem_univ zeroFlux))

/-- The raw Wilson measure with its prescribed six stacks, normalized to mass one. -/
def twistedMeasure (β : ℝ) (s : Sides) (k : Plane → Bool) : Measure (Config s) :=
  (Wilson.haar s).tilted (fun U => -β * ∑ x : Site s, ∑ p : Plane,
    faceAction U x (k p) p.val.1 p.val.2)

theorem twistedMeasure_probability (β : ℝ) (s : Sides) (k : Plane → Bool) :
    IsProbabilityMeasure (twistedMeasure β s k) := by
  apply isProbabilityMeasure_tilted
  apply Continuous.integrable_of_hasCompactSupport _ (HasCompactSupport.of_compactSpace _)
  apply Real.continuous_exp.comp
  apply continuous_const.mul
  refine continuous_finsetSum Finset.univ (fun (x : Site s) _ => ?_)
  refine continuous_finsetSum Finset.univ (fun (p : Plane) _ => ?_)
  exact continuous_const.sub (continuous_const.mul (Wilson.continuous_faceTrace
    (n := s) (x, ⟨p.val, p.property.ne⟩)))

/-- Normalized mixture of the eight electric backgrounds. -/
def mixtureMean {Ω : Type*} [MeasurableSpace Ω] (w : Flux → ℝ) (μ : Flux → Measure Ω) (F : Ω → ℝ) : ℝ :=
  (∑ e : Flux, w e * ∫ U, F U ∂μ e) / ∑ e : Flux, w e

def neutralMean (β : ℝ) (s : Sides) (m : Flux) (F : Config s → ℝ) : ℝ :=
  mixtureMean (fun e => twistedPartition β s (joinTwist e m)) (fun e => twistedMeasure β s (joinTwist e m)) F

/-- The factor eight in Lemma MX(d) for the actual finite integrals. Positivity of
the Fourier sectors supplies the electric untwisting inequality. -/
theorem periodic_mean_sq_le {β : ℝ} {s : Sides} {m : Flux} (F : Config s → ℝ)
    (hp : ∀ χ, 0 ≤ sectorWeight β s χ m)
    (hF : MemLp F 2 (twistedMeasure β s (joinTwist zeroFlux m))) :
    (∫ U, F U ∂twistedMeasure β s (joinTwist zeroFlux m)) ^ 2 ≤
      8 * neutralMean β s m (fun U => F U ^ 2) := by
  let μ (e : Flux) := twistedMeasure β s (joinTwist e m)
  let w (e : Flux) := twistedPartition β s (joinTwist e m)
  let q (e : Flux) := ∫ U, F U ^ 2 ∂μ e
  letI : IsProbabilityMeasure (μ zeroFlux) := twistedMeasure_probability _ _ _
  have hw (e : Flux) : 0 < w e := twistedPartition_pos β s _
  have hq (e : Flux) : 0 ≤ q e := integral_nonneg fun U => sq_nonneg (F U)
  have hD : 0 < ∑ e : Flux, w e := Finset.sum_pos (fun e _ => hw e) Finset.univ_nonempty
  have hU : (∑ e : Flux, w e) ≤ 8 * w zeroFlux := calc
    _ ≤ ∑ _ : Flux, w zeroFlux := Finset.sum_le_sum fun e _ => electric_untwist β s e m hp
    _ = _ := by norm_num [Fintype.card_prod]
  have hS : w zeroFlux * q zeroFlux ≤ ∑ e : Flux, w e * q e :=
    Finset.single_le_sum (fun e _ => mul_nonneg (hw e).le (hq e)) (Finset.mem_univ zeroFlux)
  have hv := ProbabilityTheory.variance_nonneg F (μ zeroFlux)
  rw [ProbabilityTheory.variance_eq_sub hF] at hv
  refine (sub_nonneg.mp hv).trans ?_
  change q zeroFlux ≤ 8 * ((∑ e : Flux, w e * q e) / ∑ e : Flux, w e)
  rw [mul_div_assoc']
  apply (le_div_iff₀ hD).mpr
  calc
    _ ≤ q zeroFlux * (8 * w zeroFlux) := mul_le_mul_of_nonneg_left hU (hq _)
    _ = 8 * (w zeroFlux * q zeroFlux) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left hS (by norm_num)

theorem mixtureMean_sum {Ω I : Type*} [MeasurableSpace Ω] [Fintype I] (w : Flux → ℝ)
    (μ : Flux → Measure Ω) (f : I → Ω → ℝ) (hi : ∀ e i, Integrable (f i) (μ e)) :
    mixtureMean w μ (fun U => ∑ i, f i U) = ∑ i, mixtureMean w μ (f i) := by
  unfold mixtureMean
  simp_rw [integral_finsetSum _ (fun i _ => hi _ i),Finset.mul_sum]
  rw [Finset.sum_comm,Finset.sum_div]

/-- Quantitative EV-L time averaging on the actual periodic and neutral finite
measures. A common mean of translated real insertions and a summable covariance
envelope imply the finite-volume comparison. -/
theorem mixture_window_comparison {Ω : Type*} [MeasurableSpace Ω] (w : Flux → ℝ) (μ : Flux → Measure Ω)
    (hp : IsProbabilityMeasure (μ zeroFlux))
    (hmx : ∀ Y : Ω → ℝ, MemLp Y 2 (μ zeroFlux) → (∫ U, Y U ∂μ zeroFlux)^2 ≤ 8 * mixtureMean w μ (fun U => Y U ^ 2))
    {N : ℕ} (hN : 0 < N) (X : Fin N → Ω → ℝ) (hX : ∀ e i, MemLp (X i) 2 (μ e))
    {a A τ : ℝ} (hA : 0 ≤ A) (d : ℤ → ℝ) (hn : ∀ z, 0 ≤ d z) (hs : Summable d)
    (hmean : ∀ i, (∫ U, X i U ∂μ zeroFlux) = a)
    (hcov : ∀ i j : Fin N, mixtureMean w μ (fun U => X i U * X j U) ≤ A * (d ((j.val : ℤ)-i.val) + τ)) :
    |a| ≤ Real.sqrt (8 * A * ((∑' z, d z) / N + τ)) := by
  letI := hp
  let Y (U : Ω) := ∑ i, X i U
  have hi (e : Flux) (i j : Fin N) : Integrable (fun U => X i U * X j U) (μ e) :=
    (hX e i).integrable_mul (hX e j)
  have hY : MemLp Y 2 (μ zeroFlux) := memLp_finsetSum _ fun i _ => hX _ i
  have mean : (∫ U, Y U ∂μ zeroFlux) = (N : ℝ) * a := by
    unfold Y
    rw [integral_finsetSum _ (fun i _ => (hX zeroFlux i).integrable (by norm_num))]
    simp only [hmean,Finset.sum_const,Finset.card_univ,Fintype.card_fin,nsmul_eq_mul]
  have sqr : (fun U => Y U ^ 2) = fun U => ∑ i, ∑ j, X i U * X j U := by
    funext U
    simp only [Y,sq,Finset.sum_mul,Finset.mul_sum]
    exact Finset.sum_comm
  have expand : mixtureMean w μ (fun U => Y U ^ 2) =
      ∑ i, ∑ j, mixtureMean w μ (fun U => X i U * X j U) := by
    rw [sqr,mixtureMean_sum w μ _ (fun e i => integrable_finsetSum _ (fun j _ => hi e i j))]
    exact Finset.sum_congr rfl fun i _ => mixtureMean_sum w μ _ (fun e j => hi e i j)
  let D := ∑' z, d z
  have row (i : Fin N) : (∑ j : Fin N, d ((j.val : ℤ) - i.val)) ≤ D := by
    let f (j : Fin N) := (j.val : ℤ) - i.val
    have hinj : Function.Injective f := fun j k h => Fin.ext (by simpa [f] using h)
    simpa only [tsum_fintype,Function.comp_apply,f,D] using tsum_comp_le_tsum_of_inj hs hn hinj
  have mx := hmx Y hY
  rw [mean,expand] at mx
  have bound : (∑ i, ∑ j, mixtureMean w μ (fun U => X i U * X j U)) ≤ (N : ℝ) * (A * (D + (N : ℝ) * τ)) := by
    calc
      _ ≤ ∑ i : Fin N, ∑ j : Fin N, A * (d ((j.val : ℤ)-i.val) + τ) :=
        Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ => hcov i j
      _ ≤ ∑ _ : Fin N, A * (D + (N : ℝ) * τ) := by
        apply Finset.sum_le_sum
        intro i _
        rw [← Finset.mul_sum,Finset.sum_add_distrib,Finset.sum_const,Finset.card_univ,Fintype.card_fin,nsmul_eq_mul]
        exact mul_le_mul_of_nonneg_left (add_le_add_left (row i) _) hA
      _ = _ := by simp
  have hh := mx.trans (mul_le_mul_of_nonneg_left bound (by norm_num : 0 ≤ (8 : ℝ)))
  have ne : 0 < (N : ℝ) := by exact_mod_cast hN
  apply Real.le_sqrt_of_sq_le
  rw [sq_abs]
  apply (mul_le_mul_iff_right₀ (sq_pos_of_pos ne)).mp
  calc
    (N : ℝ)^2 * a^2 = ((N : ℝ) * a)^2 := (mul_pow _ _ _).symm
    _ ≤ _ := hh
    _ = _ := by change 8 * (N * (A * (D+N*τ))) = (N : ℝ)^2 * (8*A*(D/N+τ)); field_simp <;> ring

theorem periodic_window_comparison {β : ℝ} {s : Sides} {m : Flux} {N : ℕ} (hN : 0 < N)
    (X : Fin N → Config s → ℝ) (hp : ∀ χ, 0 ≤ sectorWeight β s χ m)
    (hX : ∀ e i, MemLp (X i) 2 (twistedMeasure β s (joinTwist e m)))
    {a A τ : ℝ} (hA : 0 ≤ A) (d : ℤ → ℝ) (hn : ∀ z, 0 ≤ d z) (hs : Summable d)
    (hmean : ∀ i, (∫ U, X i U ∂twistedMeasure β s (joinTwist zeroFlux m)) = a)
    (hcov : ∀ i j : Fin N, neutralMean β s m (fun U => X i U * X j U) ≤ A * (d ((j.val : ℤ)-i.val) + τ)) :
    |a| ≤ Real.sqrt (8 * A * ((∑' z, d z) / N + τ)) :=
  mixture_window_comparison _ _ (twistedMeasure_probability _ _ _) (fun Y hY => periodic_mean_sq_le Y hp hY)
    hN X hX hA d hn hs hmean hcov

/-- An exponential covariance envelope is summable in both time directions. -/
theorem summable_time_decay {q : ℝ} (h₀ : 0 ≤ q) (h₁ : q < 1) :
    Summable (fun j : ℤ => q ^ j.natAbs) := by
  apply Summable.of_nat_of_neg
  · simpa using summable_geometric_of_lt_one h₀ h₁
  · simpa using summable_geometric_of_lt_one h₀ h₁


end Sectors

section Stacks

/-- Multiplication by the nontrivial centre element implements a link sign. -/
def linkCentre (b : Bool) : Wilson.SU2 := if b then Wilson.centerMinus else 1

def bitSign (b : Bool) : ℝ := if b then -1 else 1

theorem linkCentre_comm (b : Bool) (u : Wilson.SU2) : Commute (linkCentre b) u := by
  cases b
  · exact Commute.one_left _
  · apply Subtype.ext
    change (-1 : Matrix (Fin 2) (Fin 2) ℂ) * u.val = u.val * (-1)
    simp

theorem linkCentre_xor (b c : Bool) : linkCentre (xor b c) = linkCentre b * linkCentre c := by
  cases b <;> cases c <;> simp [linkCentre]
  apply Subtype.ext
  change (1 : Matrix (Fin 2) (Fin 2) ℂ) = (-1) * (-1)
  simp

theorem linkCentre_inv (b : Bool) : (linkCentre b)⁻¹ = linkCentre b := by
  apply inv_eq_of_mul_eq_one_right
  rw [← linkCentre_xor]
  cases b <;> rfl

theorem bitSign_xor (b c : Bool) : bitSign (xor b c) = bitSign b * bitSign c := by
  cases b <;> cases c <;> norm_num [bitSign]

theorem halfTrace_linkCentre (b : Bool) (u : Wilson.SU2) :
    halfTrace (linkCentre b * u) = bitSign b * halfTrace u := by
  cases b <;> simp [linkCentre, bitSign, Wilson.halfTrace_centerMinus]

/-- The product of four link signs around a positive plaquette, grouped by parallel edges. -/
def faceCurl {s : Sides} (δ : Wilson.Link s → Bool) (x : Site s) (p : Plane) : Bool :=
  let i := p.val.1
  let j := p.val.2
  xor (xor (δ (x,i)) (δ (Wilson.step x j,i))) (xor (δ (x,j)) (δ (Wilson.step x i,j)))

def resign {s : Sides} (δ : Wilson.Link s → Bool) : Config s ≃ᵐ Config s :=
  MeasurableEquiv.piCongrRight fun b => MeasurableEquiv.mulLeft (linkCentre (δ b))

theorem resign_preserving {s : Sides} (δ : Wilson.Link s → Bool) :
    MeasurePreserving (resign δ) (Wilson.haar s) (Wilson.haar s) :=
  measurePreserving_pi _ _ (fun b => measurePreserving_mul_left Wilson.linkHaar (linkCentre (δ b)))

theorem linkCentre_mul_apply (b c : Bool) (u v : Wilson.SU2) :
    (linkCentre b * u) * (linkCentre c * v) = linkCentre (xor b c) * (u * v) := by
  rw [linkCentre_xor, show (linkCentre b * u) * (linkCentre c * v) =
    linkCentre b * (u * linkCentre c) * v by group, ← (linkCentre_comm c u).eq]
  group

theorem linkCentre_inv_apply (b : Bool) (u : Wilson.SU2) : (linkCentre b * u)⁻¹ = linkCentre b * u⁻¹ := by
  rw [mul_inv_rev, linkCentre_inv, (linkCentre_comm b u⁻¹).eq]

theorem transport_resign {s : Sides} (δ : Wilson.Link s → Bool) (U : Config s) (x : Site s) (p : Plane) :
    transport (resign δ U) x p.val.1 p.val.2 =
      linkCentre (faceCurl δ x p) * transport U x p.val.1 p.val.2 := by
  have reorder : ∀ a b c d : Bool, xor (xor (xor a b) c) d = xor (xor a c) (xor d b) := by decide
  unfold Wilson.transport
  change (linkCentre _ * _) * (linkCentre _ * _) * (linkCentre _ * _)⁻¹ * (linkCentre _ * _)⁻¹ = _
  rw [linkCentre_inv_apply, linkCentre_inv_apply, linkCentre_mul_apply, linkCentre_mul_apply, linkCentre_mul_apply, reorder]
  rfl

/-- An arbitrary real insertion in a signed Wilson integral on the rectangular torus. -/
def signedIntegral {s : Sides} (β : ℝ) (w : Site s → Plane → Bool) (F : Config s → ℝ) : ℝ :=
  ∫ U, F U * Real.exp (-β * ∑ x : Site s, ∑ p : Plane,
    (1 - bitSign (w x p) * halfTrace (transport U x p.val.1 p.val.2))) ∂Wilson.haar s

/-- A change of link signs adds its coboundary to the background and transports the insertion. -/
theorem signedIntegral_resign {s : Sides} (β : ℝ) (w : Site s → Plane → Bool)
    (δ : Wilson.Link s → Bool) (F : Config s → ℝ) :
    signedIntegral β w F =
      signedIntegral β (fun x p => xor (w x p) (faceCurl δ x p)) (fun U => F (resign δ U)) := by
  unfold signedIntegral
  rw [← (resign_preserving δ).integral_comp' (fun U => F U * Real.exp (-β * ∑ x : Site s, ∑ p : Plane,
    (1 - bitSign (w x p) * halfTrace (transport U x p.val.1 p.val.2))))]
  apply integral_congr_ae
  filter_upwards with U
  simp only [transport_resign, halfTrace_linkCentre, bitSign_xor, mul_assoc]

/-- The bit used by the canonical stacks of Stage 0. -/
def stackBits {s : Sides} (k : Plane → Bool) (x : Site s) (p : Plane) : Bool :=
  decide (k p = true ∧ (x p.val.1).val = 0 ∧ (x p.val.2).val = 0)

theorem signedIntegral_stackBits (β : ℝ) (s : Sides) (k : Plane → Bool) :
    signedIntegral (s := s) β (stackBits k) (fun _ => 1) = twistedPartition β s k := by
  unfold signedIntegral twistedPartition
  simp [bitSign, stackBits]

/-- A single stack in the unoriented plane {i,j}, placed at coordinates (b,c). -/
def oneStack {s : Sides} (i j : Dir) (b c : ℕ) (x : Site s) (p : Plane) : Bool :=
  if (p.val.1 = i ∧ p.val.2 = j) ∨ (p.val.1 = j ∧ p.val.2 = i)
  then decide ((x i).val = b ∧ (x j).val = c) else false

theorem oneStack_swap {s : Sides} (i j : Dir) (b c : ℕ) (x : Site s) (p : Plane) :
    oneStack j i c b x p = oneStack i j b c x p := by
  have ho : ((p.val.1 = j ∧ p.val.2 = i) ∨ (p.val.1 = i ∧ p.val.2 = j)) ↔
      ((p.val.1 = i ∧ p.val.2 = j) ∨ (p.val.1 = j ∧ p.val.2 = i)) := or_comm
  have ha : ((x j).val = c ∧ (x i).val = b) ↔ ((x i).val = b ∧ (x j).val = c) := and_comm
  simp only [oneStack, ho, ha]

/-- Boundary of the interval (0,b] in a cyclic coordinate, including the wraparound. -/
theorem interval_curl {n : ℕ} (q : Fin n) (b : ℕ) (hb : b < n) :
    xor (decide (0 < q.val ∧ q.val ≤ b))
      (decide (0 < (finRotate n q).val ∧ (finRotate n q).val ≤ b)) =
      xor (decide (q.val = 0)) (decide (q.val = b)) := by
  have parity : ∀ a b c d : Bool, xor a b = xor c d ↔
      ((a = true ↔ b = true) ↔ (c = true ↔ d = true)) := by decide
  rw [parity]
  simp only [decide_eq_true_eq]
  cases n with
  | zero => exact q.elim0
  | succ n =>
    rw [coe_finRotate]
    by_cases h : q = Fin.last n
    · subst q
      simp only [if_true, Fin.val_last]
      omega
    · rw [if_neg h]
      omega

def stripLinks {s : Sides} (i j : Dir) (b c : ℕ) (e : Wilson.Link s) : Bool :=
  decide (e.2 = j ∧ (e.1 j).val = c ∧ 0 < (e.1 i).val ∧ (e.1 i).val ≤ b)

/-- Resigning j-links along the strip (0,b] changes exactly its two boundary stacks. -/
theorem stripLinks_curl {s : Sides} (i j : Dir) (hij : i ≠ j) (b c : ℕ) (hb : b < s i)
    (x : Site s) (p : Plane) :
    faceCurl (stripLinks i j b c) x p = xor (oneStack i j 0 c x p) (oneStack i j b c x p) := by
  let δ := @stripLinks s i j b c
  let d := xor (decide ((x i).val = 0 ∧ (x j).val = c)) (decide ((x i).val = b ∧ (x j).val = c))
  have edge (u v : Dir) (huv : u ≠ v) :
      xor (δ (x,u)) (δ (Wilson.step x v,u)) = (if u = j ∧ v = i then d else false) := by
    by_cases hu : u = j
    · subst u
      by_cases hv : v = i
      · subst v
        by_cases hc : (x j).val = c
        · simpa only [δ, d, stripLinks, Wilson.step, if_neg hij.symm, if_pos rfl, hc, true_and,
            and_true, and_self, decide_true, ite_true] using interval_curl (x i) b hb
        · simp [δ, d, stripLinks, Wilson.step, hij.symm, hc]
      · simp [δ, stripLinks, Wilson.step, huv, Ne.symm hv, hv]
    · simp [δ, stripLinks, hu]
  change xor (xor (δ _) (δ _)) (xor (δ _) (δ _)) = _
  rw [edge _ _ p.property.ne, edge _ _ p.property.ne.symm]
  have hcomm : (p.val.2 = j ∧ p.val.1 = i) ↔ (p.val.1 = i ∧ p.val.2 = j) := and_comm
  simp only [hcomm]
  by_cases h : p.val.1 = i ∧ p.val.2 = j
  · have hn : ¬(p.val.1 = j ∧ p.val.2 = i) := fun h' => hij (h.1.symm.trans h'.1)
    simp [oneStack, h.1, h.2, hij, hij.symm, d]
  · by_cases h' : p.val.1 = j ∧ p.val.2 = i <;>
      simp [oneStack, h, h', hij, hij.symm, d]

/-- Any one of the six stacks can be moved to any position, in the presence of
all other stacks. The two coordinates can be moved independently. -/
theorem signedIntegral_moveStack {s : Sides} (β : ℝ) (w : Site s → Plane → Bool)
    (i j : Dir) (hij : i ≠ j) (b c : ℕ) (hb : b < s i) (hc : c < s j) :
    signedIntegral β (fun x p => xor (w x p) (oneStack i j 0 0 x p)) (fun _ => 1) =
    signedIntegral β (fun x p => xor (w x p) (oneStack i j b c x p)) (fun _ => 1) := by
  have cancel : ∀ a b c : Bool, xor (xor a b) (xor b c) = xor a c := by decide
  have first (i j : Dir) (hij : i ≠ j) (b c : ℕ) (hb : b < s i) :
      signedIntegral β (fun x p => xor (w x p) (oneStack i j 0 c x p)) (fun _ => 1) =
      signedIntegral β (fun x p => xor (w x p) (oneStack i j b c x p)) (fun _ => 1) := by
    rw [signedIntegral_resign β _ (stripLinks i j b c) (fun _ => 1)]
    simp only [stripLinks_curl i j hij b c hb, cancel]
  have h₁ := first j i hij.symm c 0 hc
  have swap (v w' : ℕ) :
      (fun x p => xor (w x p) (oneStack j i w' v x p)) =
      (fun x p => xor (w x p) (oneStack i j v w' x p)) := by
    funext x p
    rw [oneStack_swap i j]
  rw [swap 0 0, swap 0 c] at h₁
  exact h₁.trans (first i j hij b c hb)

theorem oneStack_plane {s : Sides} (p q : Plane) (b c : ℕ) (x : Site s) :
    oneStack p.val.1 p.val.2 b c x q =
      if q = p then decide ((x p.val.1).val = b ∧ (x p.val.2).val = c) else false := by
  have he : ((q.val.1 = p.val.1 ∧ q.val.2 = p.val.2) ∨
    (q.val.1 = p.val.2 ∧ q.val.2 = p.val.1)) ↔ q = p := by
    constructor
    · rintro (⟨h₁, h₂⟩ | ⟨h₁, h₂⟩)
      · exact Subtype.ext (Prod.ext h₁ h₂)
      · exact False.elim (p.property.asymm (h₁ ▸ h₂ ▸ q.property))
    · rintro rfl
      exact Or.inl ⟨rfl, rfl⟩
  simp only [oneStack, he]

/-- Each active plane may choose its two coordinates independently. -/
def locatedStacks {s : Sides} (k : Plane → Bool) (b c : Plane → ℕ) (x : Site s) (p : Plane) : Bool :=
  decide (k p = true ∧ (x p.val.1).val = b p ∧ (x p.val.2).val = c p)

theorem locatedStacks_partition {s : Sides} (β : ℝ) (k : Plane → Bool) (b c : Plane → ℕ)
    (hb : ∀ p : Plane, b p < s p.val.1) (hc : ∀ p : Plane, c p < s p.val.2) :
    signedIntegral (s := s) β (locatedStacks k b c) (fun _ => 1) = twistedPartition β s k := by
  classical
  let mixed (A : Finset Plane) (x : Site s) (p : Plane) :=
    if p ∈ A then locatedStacks k b c x p else stackBits k x p
  have h (A : Finset Plane) : signedIntegral β (mixed A) (fun _ => 1) = twistedPartition β s k := by
    induction A using Finset.induction_on with
    | empty => simpa only [mixed, Finset.notMem_empty, if_false] using signedIntegral_stackBits β s k
    | @insert p A hp ih =>
      by_cases hk : k p = true
      · let w (x : Site s) (q : Plane) := if q = p then false else mixed A x q
        have h0 : (fun x q => xor (w x q) (oneStack p.val.1 p.val.2 0 0 x q)) = mixed A := by
          funext x q
          by_cases hq : q = p <;> simp [w, oneStack_plane, hq, mixed, hp, hk, stackBits]
        have h1 : (fun x q => xor (w x q) (oneStack p.val.1 p.val.2 (b p) (c p) x q)) =
            mixed (insert p A) := by
          funext x q
          by_cases hq : q = p <;> simp [w, oneStack_plane, hq, mixed, hk, locatedStacks]
        have hm := signedIntegral_moveStack β w _ _ p.property.ne _ _ (hb p) (hc p)
        rw [h0, h1] at hm
        exact hm.symm.trans ih
      · have he : mixed (insert p A) = mixed A := by
          funext x q
          by_cases hq : q = p <;> simp [hq, mixed, hp, hk, locatedStacks, stackBits]
        rwa [he]
  simpa only [mixed, Finset.mem_univ, if_true] using h Finset.univ


end Stacks


section RectangularIntegrals

/-- Work directly with Stage 0's sites and its last (time) coordinate. -/
abbrev spatialBonds (s : Sides) := {b : Wilson.Link s // b.2 ≠ TimeAxis.timeIdx}

abbrev timeFiber (s : Sides) (t : Fin (s TimeAxis.timeIdx)) := {x : Site s // x TimeAxis.timeIdx = t}

abbrev spatialHaar (s : Sides) : Measure (spatialBonds s → Wilson.SU2) :=
  Measure.pi fun _ => Wilson.linkHaar

abbrev fiberHaar (s : Sides) (t : Fin (s TimeAxis.timeIdx)) : Measure (timeFiber s t → Wilson.SU2) :=
  Measure.pi fun _ => Wilson.linkHaar

def slabLinkIndex (s : Sides) :
    spatialBonds s ⊕ (Σ t, timeFiber s t) ≃ Wilson.Link s where
  toFun := Sum.elim Subtype.val (fun v => (v.2.val, TimeAxis.timeIdx))
  invFun := fun b => if h : b.2 = TimeAxis.timeIdx then .inr ⟨_, ⟨b.1, rfl⟩⟩ else .inl ⟨b, h⟩
  left_inv := by
    rintro (⟨b, hb⟩ | ⟨t, x, hx⟩)
    · simp [hb]
    · subst t; rfl
  right_inv := by
    rintro ⟨x, i⟩
    by_cases hi : i = TimeAxis.timeIdx <;> simp [hi]

/-- Separate all spatial bonds from the independent temporal bonds at each level. -/
def slabFields (s : Sides) : Config s ≃ᵐ
    (spatialBonds s → Wilson.SU2) × (∀ t, timeFiber s t → Wilson.SU2) :=
  (((MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) (slabLinkIndex s)).symm.trans
    (MeasurableEquiv.sumPiEquivProdPi (fun _ => Wilson.SU2))).trans
      ((MeasurableEquiv.refl _).prodCongr (MeasurableEquiv.piCurry (fun _ _ => Wilson.SU2))))

theorem slabFields_preserving (s : Sides) :
    MeasurePreserving (slabFields s) (Wilson.haar s)
      ((spatialHaar s).prod (Measure.pi (fiberHaar s))) := by
  have h : MeasurePreserving (MeasurableEquiv.piCurry
      (fun (t : Fin (s TimeAxis.timeIdx)) (_ : timeFiber s t) => Wilson.SU2))
      (Measure.pi fun _ => Wilson.linkHaar) (Measure.pi (fiberHaar s)) := by
    refine ⟨(MeasurableEquiv.piCurry _).measurable, ?_⟩
    simpa only [Measure.infinitePi_eq_pi] using
      Measure.infinitePi_map_piCurry (fun (t : Fin (s TimeAxis.timeIdx)) (_ : timeFiber s t) => Wilson.linkHaar)
  exact ((MeasurePreserving.id (spatialHaar s)).prod h).comp
    ((measurePreserving_sumPiEquivProdPi (fun _ : spatialBonds s ⊕ (Σ t, timeFiber s t) => Wilson.linkHaar)).comp
      ((measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) (slabLinkIndex s)).symm _))

/-- A slab keeps all spatial bonds and just the temporal bonds starting at t.
Values assigned to the other temporal bonds do not enter any face based at t. -/
def slabField {s : Sides} (u : spatialBonds s → Wilson.SU2) (t : Fin (s TimeAxis.timeIdx))
    (g : timeFiber s t → Wilson.SU2) (b : Wilson.Link s) : Wilson.SU2 :=
  if h : b.2 = TimeAxis.timeIdx then
    if ht : b.1 TimeAxis.timeIdx = t then g ⟨b.1, ht⟩ else 1
  else u ⟨b, h⟩

theorem transport_slabField {s : Sides} (U : Config s) (t : Fin (s TimeAxis.timeIdx))
    (x : timeFiber s t) (p : Plane) :
    transport (slabField (slabFields s U).1 t ((slabFields s U).2 t)) x.val p.val.1 p.val.2 =
      transport U x.val p.val.1 p.val.2 := by
  have link (y : Site s) (i : Dir) (hi : i = TimeAxis.timeIdx → y TimeAxis.timeIdx = t) :
      slabField (slabFields s U).1 t ((slabFields s U).2 t) (y,i) = U (y,i) := by
    by_cases h : i = TimeAxis.timeIdx
    · subst i
      rw [slabField, dif_pos rfl, dif_pos (hi rfl)]
      rfl
    · rw [slabField, dif_neg h]
      rfl
  have other (i j : Dir) (hij : i ≠ j) (h : j = TimeAxis.timeIdx) :
      Wilson.step x.val i TimeAxis.timeIdx = t := by
    subst j
    simpa only [Wilson.step, if_neg hij.symm] using x.property
  unfold Wilson.transport
  rw [link _ _ (fun _ => x.property), link _ _ (other _ _ p.property.ne),
    link _ _ (other _ _ p.property.ne.symm), link _ _ (fun _ => x.property)]

/-- A one-step weight before gauge averaging, valid for any signed background.
The four links in each factor are the physical boundary of the corresponding face. -/
def slabDensity {s : Sides} (β : ℝ) (w : Site s → Plane → Bool)
    (u : spatialBonds s → Wilson.SU2) (t : Fin (s TimeAxis.timeIdx)) (g : timeFiber s t → Wilson.SU2) : ℝ :=
  Real.exp (-β * ∑ x : timeFiber s t, ∑ p : Plane,
    (1 - bitSign (w x.val p) * halfTrace (transport (slabField u t g) x.val p.val.1 p.val.2)))

theorem signedDensity_eq_slabs {s : Sides} (β : ℝ) (w : Site s → Plane → Bool) (U : Config s) :
    Real.exp (-β * ∑ x : Site s, ∑ p : Plane,
      (1 - bitSign (w x p) * halfTrace (transport U x p.val.1 p.val.2))) =
      ∏ t, slabDensity β w (slabFields s U).1 t ((slabFields s U).2 t) := by
  let F (x : Site s) := ∑ p : Plane, (1 - bitSign (w x p) * halfTrace (transport U x p.val.1 p.val.2))
  have hh : (∑ t, ∑ x : timeFiber s t, F x.val) = ∑ x : Site s, F x := by
    rw [← Fintype.sum_sigma']
    exact (Equiv.sigmaFiberEquiv (fun x : Site s => x TimeAxis.timeIdx)).sum_comp F
  simp only [slabDensity, transport_slabField, ← Real.exp_sum, ← Finset.mul_sum]
  rw [← hh]

/-- W4's geometric integral on every rectangular box. The temporal Haar bonds
have been integrated independently; this equality precedes any spectral assumption. -/
theorem signedIntegral_eq_slabKernels {s : Sides} (β : ℝ) (w : Site s → Plane → Bool) :
    signedIntegral β w (fun _ => 1) =
      ∫ u, ∏ t, (∫ g, slabDensity β w u t g ∂fiberHaar s t) ∂spatialHaar s := by
  let e := slabFields s
  let μ := spatialHaar s
  let ν := Measure.pi (fiberHaar s)
  let D (U : Config s) := Real.exp (-β * ∑ x : Site s, ∑ p : Plane,
    (1 - bitSign (w x p) * halfTrace (transport U x p.val.1 p.val.2)))
  have hi : Integrable D (Wilson.haar s) := by
    apply Continuous.integrable_of_hasCompactSupport _ (HasCompactSupport.of_compactSpace _)
    apply Real.continuous_exp.comp
    apply continuous_const.mul
    refine continuous_finsetSum Finset.univ (fun (x : Site s) _ => ?_)
    refine continuous_finsetSum Finset.univ (fun (p : Plane) _ => ?_)
    exact continuous_const.sub (continuous_const.mul (Wilson.continuous_faceTrace (n := s) (x, ⟨p.val, p.property.ne⟩)))
  have he := (slabFields_preserving s).symm e
  let F := fun z : (spatialBonds s → Wilson.SU2) × (∀ t, timeFiber s t → Wilson.SU2) => D (e.symm z)
  have hi' : Integrable F (μ.prod ν) := he.integrable_comp_of_integrable hi
  unfold signedIntegral
  simp only [one_mul]
  change (∫ U, D U ∂Wilson.haar s) = _
  rw [← he.integral_comp' D]
  change (∫ z, F z ∂μ.prod ν) = _
  rw [integral_prod F hi']
  apply integral_congr_ae
  filter_upwards with u
  have point (g : ∀ t, timeFiber s t → Wilson.SU2) : F (u,g) = ∏ t, slabDensity β w u t (g t) := by
    simpa only [D, F, e, MeasurableEquiv.apply_symm_apply] using signedDensity_eq_slabs β w (e.symm (u,g))
  simp only [point]
  exact integral_fintype_prod_eq_prod (μ := fiberHaar s) (fun t g => slabDensity β w u t g)

theorem twistedPartition_eq_slabKernels (β : ℝ) (s : Sides) (k : Plane → Bool) :
    twistedPartition β s k =
      ∫ u, ∏ t, (∫ g, slabDensity β (stackBits k) u t g ∂fiberHaar s t) ∂spatialHaar s := by
  rw [← signedIntegral_stackBits]
  exact signedIntegral_eq_slabKernels _ _

/-- At every layer away from the temporal seam, the electric twist is absent. -/
theorem slabDensity_off_electric_cut {s : Sides} (β : ℝ) (e m : Flux)
    (u : spatialBonds s → Wilson.SU2) (t : Fin (s TimeAxis.timeIdx)) (ht : t.val ≠ 0)
    (g : timeFiber s t → Wilson.SU2) :
    slabDensity β (stackBits (joinTwist e m)) u t g =
      slabDensity β (stackBits (joinTwist zeroFlux m)) u t g := by
  have noTime (p : Plane) (h : p.val.2 ≠ TimeAxis.timeIdx) :
      joinTwist e m p = joinTwist zeroFlux m p := by
    obtain ⟨⟨i,j⟩, hij⟩ := p
    fin_cases i <;> fin_cases j <;> first | rfl | exact absurd hij (by decide) | exact (h rfl).elim
  have same (x : timeFiber s t) (p : Plane) :
      stackBits (joinTwist e m) x.val p = stackBits (joinTwist zeroFlux m) x.val p := by
    by_cases h : p.val.2 = TimeAxis.timeIdx
    · have hh : (x.val p.val.2).val ≠ 0 := by
        rw [h, x.property]
        exact ht
      simp only [stackBits, hh, and_false]
    · simp only [stackBits, noTime p h]
  simp only [slabDensity, same]

abbrev levelBonds (s : Sides) (t : Fin (s TimeAxis.timeIdx)) :=
  {b : spatialBonds s // b.val.1 TimeAxis.timeIdx = t}

abbrev levelHaar (s : Sides) (t : Fin (s TimeAxis.timeIdx)) : Measure (levelBonds s t → Wilson.SU2) :=
  Measure.pi fun _ => Wilson.linkHaar

/-- A time slab only reads the spatial bonds of its two boundary slices. -/
theorem slabDensity_adjacent {s : Sides} (β : ℝ) (w : Site s → Plane → Bool)
    (u v : spatialBonds s → Wilson.SU2) (t : Fin (s TimeAxis.timeIdx)) (g : timeFiber s t → Wilson.SU2)
    (h : ∀ b : spatialBonds s, b.val.1 TimeAxis.timeIdx = t ∨
      b.val.1 TimeAxis.timeIdx = finRotate _ t → u b = v b) : slabDensity β w u t g = slabDensity β w v t g := by
  have link (y : Site s) (i : Dir) (hy : y TimeAxis.timeIdx = t ∨ y TimeAxis.timeIdx = finRotate _ t) :
      slabField u t g (y,i) = slabField v t g (y,i) := by
    by_cases hi : i = TimeAxis.timeIdx
    · simp only [slabField, dif_pos hi]
    · exact (by simpa only [slabField, dif_neg hi] using h ⟨(y,i),hi⟩ hy)
  have hs (x : timeFiber s t) (i : Dir) : Wilson.step x.val i TimeAxis.timeIdx = t ∨
      Wilson.step x.val i TimeAxis.timeIdx = finRotate _ t := by
    by_cases hi : TimeAxis.timeIdx = i <;> simp [Wilson.step, hi, x.property]
  have word (x : timeFiber s t) (p : Plane) :
      transport (slabField u t g) x.val p.val.1 p.val.2 =
        transport (slabField v t g) x.val p.val.1 p.val.2 := by
    unfold Wilson.transport
    rw [link _ _ (Or.inl x.property), link _ _ (hs x p.val.1), link _ _ (hs x p.val.2),
      link _ _ (Or.inl x.property)]
  simp only [slabDensity, word]

def spatialLevels (s : Sides) :
    (spatialBonds s → Wilson.SU2) ≃ᵐ (∀ t, levelBonds s t → Wilson.SU2) :=
  ((MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2)
    (Equiv.sigmaFiberEquiv (fun b : spatialBonds s => b.val.1 TimeAxis.timeIdx))).symm.trans
      (MeasurableEquiv.piCurry (fun _ _ => Wilson.SU2)))

theorem spatialLevels_preserving (s : Sides) :
    MeasurePreserving (spatialLevels s) (spatialHaar s) (Measure.pi (levelHaar s)) := by
  have h : MeasurePreserving (MeasurableEquiv.piCurry
      (fun (t : Fin (s TimeAxis.timeIdx)) (_ : levelBonds s t) => Wilson.SU2))
      (Measure.pi fun _ => Wilson.linkHaar) (Measure.pi (levelHaar s)) := by
    refine ⟨(MeasurableEquiv.piCurry _).measurable, ?_⟩
    simpa only [Measure.infinitePi_eq_pi] using
      Measure.infinitePi_map_piCurry (fun (t : Fin (s TimeAxis.timeIdx)) (_ : levelBonds s t) => Wilson.linkHaar)
  exact h.comp ((measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar)
    (Equiv.sigmaFiberEquiv (fun b : spatialBonds s => b.val.1 TimeAxis.timeIdx))).symm _)

def boundaryField {s : Sides} (t : Fin (s TimeAxis.timeIdx))
    (u : levelBonds s t → Wilson.SU2) (v : levelBonds s (finRotate _ t) → Wilson.SU2)
    (b : spatialBonds s) : Wilson.SU2 :=
  if ht : b.val.1 TimeAxis.timeIdx = t then u ⟨b, ht⟩ else
    if hn : b.val.1 TimeAxis.timeIdx = finRotate _ t then v ⟨b, hn⟩ else 1

/-- Explicit single-step signed kernel on two spatial slices, with all temporal bonds averaged. -/
def layerKernel {s : Sides} (β : ℝ) (w : Site s → Plane → Bool) (t : Fin (s TimeAxis.timeIdx))
    (u : levelBonds s t → Wilson.SU2) (v : levelBonds s (finRotate _ t) → Wilson.SU2) : ℝ :=
  ∫ g, slabDensity β w (boundaryField t u v) t g ∂fiberHaar s t

/-- The rectangular twisted partition function is an actual cyclic Haar integral of
one-step kernels on consecutive spatial slices, with time coordinate 3 throughout. -/
theorem twistedPartition_eq_kernelCycle (β : ℝ) (s : Sides) (k : Plane → Bool) :
    twistedPartition β s k =
      ∫ u, ∏ t, layerKernel β (stackBits k) t (u t) (u (finRotate _ t)) ∂Measure.pi (levelHaar s) := by
  rw [twistedPartition_eq_slabKernels, ← (spatialLevels_preserving s).integral_comp'
    (fun u => ∏ t, layerKernel β (stackBits k) t (u t) (u (finRotate _ t)))]
  apply integral_congr_ae
  filter_upwards with u
  apply Finset.prod_congr rfl
  intro t _
  apply integral_congr_ae
  filter_upwards with g
  apply slabDensity_adjacent
  intro b hb
  unfold boundaryField
  by_cases ht : b.val.1 TimeAxis.timeIdx = t
  · rw [dif_pos ht]; rfl
  · rw [dif_neg ht, dif_pos (hb.resolve_left ht)]; rfl


/-- Flip the outgoing spatial slice along the three selected centre cuts. -/
def flipSlice {s : Sides} {t : Fin (s TimeAxis.timeIdx)} (e : Flux)
    (v : levelBonds s t → Wilson.SU2) (b : levelBonds s t) : Wilson.SU2 :=
  linkCentre (decide (fluxBit e b.val.val.2 = true ∧ (b.val.val.1 b.val.val.2).val = 0)) * v b

def seamLinks {s : Sides} (e : Flux) (t : Fin (s TimeAxis.timeIdx)) (b : Wilson.Link s) : Bool :=
  decide (b.2 ≠ TimeAxis.timeIdx ∧ b.1 TimeAxis.timeIdx = finRotate _ t ∧
    fluxBit e b.2 = true ∧ (b.1 b.2).val = 0)

theorem slabField_flipSlice {s : Sides} (e : Flux) (t : Fin (s TimeAxis.timeIdx))
    (hn : finRotate _ t ≠ t) (u : levelBonds s t → Wilson.SU2)
    (v : levelBonds s (finRotate _ t) → Wilson.SU2) (g : timeFiber s t → Wilson.SU2) :
    slabField (boundaryField t u (flipSlice e v)) t g =
      resign (seamLinks e t) (slabField (boundaryField t u v) t g) := by
  funext b
  change _ = linkCentre (seamLinks e t b) * slabField (boundaryField t u v) t g b
  by_cases hi : b.2 = TimeAxis.timeIdx
  · simp [slabField, seamLinks, hi, linkCentre, -finRotate_apply]
  · by_cases ht : b.1 TimeAxis.timeIdx = t
    · simp [slabField, boundaryField, hi, ht, hn.symm, seamLinks, linkCentre, -finRotate_apply]
    · by_cases hh : b.1 TimeAxis.timeIdx = finRotate _ t
      · simp [slabField, boundaryField, flipSlice, seamLinks, hi, ht, hh, hn, -finRotate_apply]
      · simp [slabField, boundaryField, hi, ht, hh, seamLinks, linkCentre, -finRotate_apply]

/-- On the electric seam the coboundary of the slice flip supplies exactly the
three temporal plane signs and preserves the existing magnetic signs. -/
theorem seamLinks_curl {s : Sides} (e m : Flux) (t : Fin (s TimeAxis.timeIdx))
    (ht : t.val = 0) (hn : finRotate _ t ≠ t) (x : timeFiber s t) (p : Plane) :
    xor (stackBits (joinTwist zeroFlux m) x.val p) (faceCurl (seamLinks e t) x.val p) =
      stackBits (joinTwist e m) x.val p := by
  have base (y : Site s) (hy : y TimeAxis.timeIdx = t) (i : Dir) : seamLinks e t (y,i) = false := by
    simp [seamLinks, hy, hn.symm, -finRotate_apply]
  have stay (i : Dir) (hi : i ≠ TimeAxis.timeIdx) : Wilson.step x.val i TimeAxis.timeIdx = t := by
    simpa only [Wilson.step, if_neg hi.symm] using x.property
  have low : p.val.1 ≠ TimeAxis.timeIdx := fun h => by
    have hh := p.property
    rw [h] at hh
    exact (not_lt_of_ge (Fin.le_last p.val.2)) hh
  by_cases high : p.val.2 = TimeAxis.timeIdx
  · have active (a : Flux) : joinTwist a m p = fluxBit a p.val.1 := by
      obtain ⟨⟨i,j⟩, hij⟩ := p
      change j = (3 : Dir) at high
      subst j
      fin_cases i <;> first | rfl | exact absurd hij (by decide)
    have z : fluxBit zeroFlux p.val.1 = false := by generalize p.val.1 = i; fin_cases i <;> rfl
    simp only [faceCurl, base _ x.property, base _ (stay _ low), high, Bool.false_xor, Bool.xor_false]
    have hxlast : (x.val p.val.2).val = 0 := by rw [high, x.property, ht]
    simp [stackBits, active, z, high, low, low.symm, seamLinks, Wilson.step, x.property, ht, hxlast, -finRotate_apply]
  · have mag : joinTwist e m p = joinTwist zeroFlux m p := by
      obtain ⟨⟨i,j⟩, hij⟩ := p
      fin_cases i <;> fin_cases j <;> first | rfl | exact absurd hij (by decide) | exact (high rfl).elim
    simp only [faceCurl, base _ x.property, base _ (stay _ low), base _ (stay _ high),
      Bool.false_xor, Bool.xor_false, stackBits, mag]

/-- On any rectangular spatial box the electric twist is precisely a centre
flip of the second argument of the untwisted-electric magnetic kernel at t=0. -/
theorem layerKernel_electric {s : Sides} (β : ℝ) (e m : Flux) (t : Fin (s TimeAxis.timeIdx))
    (hn : finRotate _ t ≠ t) (u : levelBonds s t → Wilson.SU2) (v : levelBonds s (finRotate _ t) → Wilson.SU2) :
    layerKernel β (stackBits (joinTwist e m)) t u v =
      layerKernel β (stackBits (joinTwist zeroFlux m)) t u (if t.val = 0 then flipSlice e v else v) := by
  unfold layerKernel
  apply integral_congr_ae
  filter_upwards with g
  by_cases ht : t.val = 0
  · rw [if_pos ht]
    unfold slabDensity
    rw [slabField_flipSlice e t hn]
    simp only [transport_resign, halfTrace_linkCentre, ← mul_assoc, ← bitSign_xor, seamLinks_curl e m t ht hn]
  · rw [if_neg ht]
    exact slabDensity_off_electric_cut β e m _ t ht g

theorem finRotate_ne_self_of_two {a : ℕ} (ha : 2 ≤ a) (t : Fin a) : finRotate a t ≠ t := by
  obtain ⟨a,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a ≠ 0)
  intro he
  have hv := congrArg Fin.val he
  rw [coe_finRotate] at hv
  by_cases hl : t = Fin.last a
  · subst t; simp only [ite_true, Fin.val_last] at hv; omega
  · rw [if_neg hl] at hv; omega

/-- The signed rectangular partition function as a magnetic kernel cycle with a
single electric insertion. No transfer representation or positivity is assumed. -/
theorem twistedPartition_eq_electricCycle {s : Sides} (β : ℝ) (e m : Flux) (ha : 2 ≤ s TimeAxis.timeIdx) :
    twistedPartition β s (joinTwist e m) =
      ∫ u, ∏ t, layerKernel β (stackBits (joinTwist zeroFlux m)) t (u t)
        (if t.val = 0 then flipSlice e (u (finRotate _ t)) else u (finRotate _ t)) ∂Measure.pi (levelHaar s) := by
  rw [twistedPartition_eq_kernelCycle]
  apply integral_congr_ae
  filter_upwards with u
  apply Finset.prod_congr rfl
  intro t _
  apply layerKernel_electric
  exact finRotate_ne_self_of_two ha t


end RectangularIntegrals


section ElectricProjections

open scoped InnerProductSpace
open Matrices

def cuts (e : Flux) : Finset Dir := Finset.univ.filter (fun i => fluxBit e i = true)

theorem mem_cuts (e : Flux) (i : Dir) : i ∈ cuts e ↔ fluxBit e i = true := by
  simp only [cuts, Finset.mem_filter, Finset.mem_univ, true_and]

def fluxAdd (e f : Flux) : Flux := (xor e.1 f.1, xor e.2.1 f.2.1, xor e.2.2 f.2.2)

theorem fluxBit_add (e f : Flux) (i : Dir) :
    fluxBit (fluxAdd e f) i = xor (fluxBit e i) (fluxBit f i) := by fin_cases i <;> rfl

theorem character_add : ∀ e f χ : Flux,
    character (fluxAdd e f) χ = character e χ * character f χ := by decide

theorem character_sq : ∀ e χ : Flux, character e χ * character e χ = 1 := by decide

def fluxTranslation (e : Flux) : Equiv.Perm Flux where
  toFun := fluxAdd e
  invFun := fluxAdd e
  left_inv := (by decide : ∀ a b : Flux, fluxAdd a (fluxAdd a b) = b) e
  right_inv := (by decide : ∀ a b : Flux, fluxAdd a (fluxAdd a b) = b) e

theorem centreElt_mul_self : centreElt * centreElt = 1 := by
  apply Subtype.ext
  change (-1 : Matrix (Fin 2) (Fin 2) ℂ) * (-1) = 1
  simp

section CharacterProjection

variable {H : Type*} [NormedAddCommGroup H] [NormedSpace ℂ H]
variable (C : Flux → H →L[ℂ] H)

def characterProj (χ : Flux) : H →L[ℂ] H := (1 / 8 : ℂ) • ∑ e : Flux, (character e χ : ℂ) • C e

theorem translation_characterProj (hC : ∀ e f, C e * C f = C (fluxAdd e f)) (g χ : Flux) :
    C g * characterProj C χ = (character g χ : ℂ) • characterProj C χ := by
  let c (e : Flux) : ℂ := character e χ
  have hc (e : Flux) : c e = c g * c (fluxAdd g e) := by
    dsimp [c]
    rw [character_add, Int.cast_mul, ← mul_assoc, ← Int.cast_mul, character_sq, Int.cast_one, one_mul]
  change C g * ((1 / 8 : ℂ) • ∑ e, c e • C e) = c g • ((1 / 8 : ℂ) • ∑ e, c e • C e)
  rw [mul_smul_comm, smul_comm (c g) (1 / 8 : ℂ)]
  apply congrArg ((1 / 8 : ℂ) • ·)
  rw [Finset.mul_sum, Finset.smul_sum, ← Equiv.sum_comp (fluxTranslation g) (fun e => c g • (c e • C e))]
  apply Finset.sum_congr rfl
  intro e _
  rw [mul_smul_comm, hC, smul_smul]
  exact congrArg (· • C (fluxAdd g e)) (hc e)

theorem characterProj_mul (hC : ∀ e f, C e * C f = C (fluxAdd e f)) (χ ψ : Flux) :
    characterProj C χ * characterProj C ψ = if χ = ψ then characterProj C ψ else 0 := by
  let P := characterProj C ψ
  have hc : (∑ e : Flux, (character e χ : ℂ) * (character e ψ : ℂ)) =
      if χ = ψ then 8 else 0 := by exact_mod_cast character_orthogonal χ ψ
  change ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • C e) * P = _
  rw [smul_mul_assoc, Finset.sum_mul]
  simp_rw [smul_mul_assoc, show ∀ e, C e * P = (character e ψ : ℂ) • P from
    fun e => translation_characterProj C hC e ψ, smul_smul]
  rw [← Finset.sum_smul, hc, smul_smul]
  split_ifs <;> norm_num [P]

end CharacterProjection


variable (Γ : CubicPeriodSublattice)
abbrev electricTranslation (e : Flux) := centreTranslation Γ TimeAxis.timeIdx (cuts e)

theorem centreShift_add (e f : Flux) :
    centreShift Γ TimeAxis.timeIdx (cuts (fluxAdd e f)) =
      centreShift Γ TimeAxis.timeIdx (cuts f) ∘ centreShift Γ TimeAxis.timeIdx (cuts e) := by
  funext u b
  let l := TransferOperators.CubicPeriodSublattice.linkRep b
  change centreSign Γ _ _ b * u b = centreSign Γ _ _ b * (centreSign Γ _ _ b * u b)
  rw [← mul_assoc]
  apply congrArg (· * u b)
  unfold centreSign
  let atCut := Γ.coordResidues (l.source : InfiniteLattice.LatticePoint 1) l.axis = 0
  change (if l.axis ∈ cuts (fluxAdd e f) ∧ atCut then centreElt else 1) =
    (if l.axis ∈ cuts f ∧ atCut then centreElt else 1) *
      (if l.axis ∈ cuts e ∧ atCut then centreElt else 1)
  by_cases h : atCut <;>
    cases he : fluxBit e l.axis <;> cases hf : fluxBit f l.axis <;>
    simp [cuts, Finset.mem_filter, h, he, hf, fluxBit_add, centreElt_mul_self]

theorem electricTranslation_mul (e f : Flux) :
    electricTranslation Γ e * electricTranslation Γ f = electricTranslation Γ (fluxAdd e f) := by
  apply ContinuousLinearMap.ext
  intro u
  change Lp.compMeasurePreserving _ _ (Lp.compMeasurePreserving _ _ u) = Lp.compMeasurePreserving _ _ u
  rw [← Lp.compMeasurePreserving_comp_apply]
  congr 2
  exact (centreShift_add Γ e f).symm

/-- Fourier projection on a release slice, in the Haar representation of the three centre flips. -/
def electricProj (χ : Flux) : Γ.SliceL2 TimeAxis.timeIdx →L[ℂ] Γ.SliceL2 TimeAxis.timeIdx :=
  (1 / 8 : ℂ) • ∑ e : Flux, (character e χ : ℂ) • electricTranslation Γ e

theorem translation_electricProj (g χ : Flux) :
    electricTranslation Γ g * electricProj Γ χ = (character g χ : ℂ) • electricProj Γ χ :=
  translation_characterProj _ (electricTranslation_mul Γ) g χ

theorem electricProj_mul (χ ψ : Flux) :
    electricProj Γ χ * electricProj Γ ψ = if χ = ψ then electricProj Γ ψ else 0 :=
  characterProj_mul _ (electricTranslation_mul Γ) χ ψ

theorem electricTranslation_zero : electricTranslation Γ zeroFlux = 1 := by
  apply ContinuousLinearMap.ext
  intro u
  let A := Lp.compMeasurePreservingₗᵢ ℂ _ (centreShift_measurePreserving Γ TimeAxis.timeIdx (cuts zeroFlux))
    (p := (2 : ℝ≥0∞)) (E := ℂ)
  apply A.injective
  exact DFunLike.congr_fun (electricTranslation_mul Γ zeroFlux zeroFlux) u

theorem electricTranslation_isSelfAdjoint (e : Flux) : IsSelfAdjoint (electricTranslation Γ e) := by
  let A := Lp.compMeasurePreservingₗᵢ ℂ _ (centreShift_measurePreserving Γ TimeAxis.timeIdx (cuts e))
    (p := (2 : ℝ≥0∞)) (E := ℂ)
  have he : fluxAdd e e = zeroFlux := (by decide : ∀ f : Flux, fluxAdd f f = zeroFlux) e
  have hi (w : Γ.SliceL2 TimeAxis.timeIdx) : A (A w) = w := by
    have h := electricTranslation_mul Γ e e
    rw [he, electricTranslation_zero] at h
    exact DFunLike.congr_fun h w
  apply ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mpr
  intro u v
  change ⟪A u, v⟫_ℂ = ⟪u, A v⟫_ℂ
  calc
    _ = ⟪A u, A (A v)⟫_ℂ := by rw [hi]
    _ = _ := A.inner_map_map u (A v)

theorem electricProj_isSelfAdjoint (χ : Flux) : IsSelfAdjoint (electricProj Γ χ) := by
  unfold IsSelfAdjoint electricProj
  simp [star_smul, (electricTranslation_isSelfAdjoint Γ _).star_eq]

theorem electricProj_sum : (∑ χ : Flux, electricProj Γ χ) = 1 := by
  have hc (e : Flux) : (∑ χ : Flux, (character e χ : ℂ)) = if e = zeroFlux then 8 else 0 := by
    have h := character_orthogonal e zeroFlux
    simp only [character_zero, mul_one] at h
    simp_rw [character_symm e]
    split_ifs at h ⊢ <;> exact_mod_cast h
  unfold electricProj
  rw [← Finset.smul_sum, Finset.sum_comm]
  simp_rw [← Finset.sum_smul, hc]
  simp [ite_smul, electricTranslation_zero, smul_smul]

/-- The eight bit vectors enumerate exactly the subsets in the release-slice neutral average. -/
def cutsEquiv : Flux ≃ ↥((Finset.univ.erase TimeAxis.timeIdx).powerset) where
  toFun e := ⟨cuts e, Finset.mem_powerset.mpr (by
    intro i hi
    exact Finset.mem_erase.mpr ⟨by
      rintro rfl
      exact Bool.false_ne_true ((mem_cuts _ _).mp hi), Finset.mem_univ _⟩)⟩
  invFun c := (decide (0 ∈ c.val), decide (1 ∈ c.val), decide (2 ∈ c.val))
  left_inv := by decide
  right_inv c := by
    apply Subtype.ext
    ext i
    have hn : (3 : Dir) ∉ c.val := fun h =>
      (Finset.mem_erase.mp (Finset.mem_powerset.mp c.property h)).1 rfl
    rw [mem_cuts]
    fin_cases i
    · exact decide_eq_true_iff
    · exact decide_eq_true_iff
    · exact decide_eq_true_iff
    · change (false = true) ↔ (3 : Dir) ∈ c.val
      simp [hn]

theorem electricProj_zero (Γ : CubicPeriodSublattice) :
    electricProj Γ zeroFlux = neutralProj Γ TimeAxis.timeIdx := by
  classical
  unfold electricProj neutralProj
  simp only [character_zero, Int.cast_one, one_smul]
  congr 1
  rw [← Finset.sum_attach]
  exact cutsEquiv.sum_comp (fun c => centreTranslation Γ TimeAxis.timeIdx c.val)

end ElectricProjections


section MagneticCubes

open Matrices TheStatementsProvedTogether SpinHarmonics
open scoped InnerProductSpace

variable (Γ : CubicPeriodSublattice)
local notation "μt" => TimeAxis.timeIdx
local instance : Fintype (Γ.FaceOrbits μt) := Fintype.ofFinite _

/-- Magnetic stacks on the release's quotient faces, using both zero residues at the base. -/
def magneticFace (m : Flux) (c : Γ.FaceOrbits μt) : Bool :=
  let p := (TransferOperators.CubicPeriodSublattice.faceRep c).val
  joinTwist zeroFlux m ⟨(p.lowAxis, p.highAxis), p.lowAxis_lt_highAxis⟩ &&
    decide (Γ.coordResidues p.corner p.lowAxis = 0 ∧ Γ.coordResidues p.corner p.highAxis = 0)

def magneticHolonomy (m : Flux) (c : Γ.FaceOrbits μt) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    Wilson.SU2 :=
  if magneticFace Γ m c then centreElt * Γ.orbitHolonomy c u else Γ.orbitHolonomy c u

theorem continuous_magneticHolonomy (m : Flux) (c : Γ.FaceOrbits μt) :
    Continuous (magneticHolonomy Γ m c) := by
  have hc : Continuous (Γ.orbitHolonomy c) := SliceEnergyProperties.continuous_holonomyOfFamily _
  unfold magneticHolonomy
  cases h : magneticFace Γ m c
  · exact hc
  · exact continuous_const.mul hc

/-- The real magnetic slice energy. Multiplying a plaquette holonomy by −I changes
the sign of its half trace and keeps its Wilson term nonnegative. -/
def magneticEnergy (β : ℝ) (m : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) : ℝ :=
  β * ∑ c : Γ.FaceOrbits μt, (1 - halfTrace (magneticHolonomy Γ m c u))

theorem magneticEnergy_nonneg {β : ℝ} (hβ : 0 ≤ β) (m : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    0 ≤ magneticEnergy Γ β m u :=
  mul_nonneg hβ (Finset.sum_nonneg fun c _ => sub_nonneg.mpr (Wilson.halfTrace_le_one _))

theorem continuous_magneticEnergy (β : ℝ) (m : Flux) : Continuous (magneticEnergy Γ β m) :=
  continuous_const.mul (continuous_finsetSum _ (fun c _ =>
    continuous_const.sub (Wilson.continuous_halfTrace.comp (continuous_magneticHolonomy Γ m c))))

theorem magneticEnergy_zero (β : ℝ) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    magneticEnergy Γ β zeroFlux u = (Γ.sliceEnergy β u).re := by
  rw [SliceEnergyProperties.sliceEnergy_eq_sum]
  simp only [magneticEnergy, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im, zero_mul,
    sub_zero, Complex.re_sum]
  apply congrArg (β * ·)
  apply Finset.sum_congr rfl
  intro c _
  simp only [magneticHolonomy, magneticFace, join_zero, Bool.false_and, Bool.false_eq_true, if_false]
  simp [Wilson.halfTrace, Complex.mul_re, div_eq_mul_inv]
  <;> ring

def magneticDensity (β : ℝ) (m : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) : ℂ :=
  (Real.exp (-magneticEnergy Γ β m u) : ℝ)

theorem magneticDensity_continuous (β : ℝ) (m : Flux) : Continuous (magneticDensity Γ β m) :=
  Complex.continuous_ofReal.comp (Real.continuous_exp.comp (continuous_magneticEnergy Γ β m).neg)

theorem magneticDensity_bound {β : ℝ} (hβ : 0 ≤ β) (m : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    ‖magneticDensity Γ β m u‖ ≤ 1 := by
  rw [magneticDensity, Complex.norm_real, Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
  exact Real.exp_le_one_iff.mpr (neg_nonpos.mpr (magneticEnergy_nonneg Γ hβ m u))

def magneticMultiplier {β : ℝ} (hβ : 0 < β) (m : Flux) :
    Γ.SliceL2 μt →L[ℂ] Γ.SliceL2 μt :=
  BoundedMultiplication.mulOp (magneticDensity_continuous Γ β m) (magneticDensity_bound Γ hβ.le m)

theorem magneticMultiplier_formula {β : ℝ} (hβ : 0 < β) (m : Flux) :
    IsMultiplicationOp (magneticDensity Γ β m) (magneticMultiplier Γ hβ m) :=
  BoundedMultiplication.isMultiplicationOp_mulOp _ _

theorem magneticMultiplier_positive {β : ℝ} (hβ : 0 < β) (m : Flux) :
    IsPositiveOp (magneticMultiplier Γ hβ m) :=
  BoundedMultiplication.isPositiveOp_of_nonneg_mul (f := magneticDensity Γ β m) (fun _ => rfl)
    (fun u => (Real.exp_pos (-magneticEnergy Γ β m u)).le)
    (magneticMultiplier_formula Γ hβ m)

/-- Magnetic transfer on the very slice of Stage 0, in the release's square-root convention. -/
def magneticTransfer {β : ℝ} (hβ : 0 < β) (m : Flux) : Γ.SliceL2 μt →L[ℂ] Γ.SliceL2 μt :=
  Γ.halfTransfer μt β * magneticMultiplier Γ hβ m * Γ.halfTransfer μt β

theorem magneticTransfer_zero {β : ℝ} (hβ : 0 < β) :
    magneticTransfer Γ hβ zeroFlux = Γ.transfer μt β := by
  have hM : magneticMultiplier Γ hβ zeroFlux = Γ.boltzmannMultiplier μt β := by
    apply ContinuousLinearMap.ext
    intro φ
    apply Lp.ext
    filter_upwards [magneticMultiplier_formula Γ hβ zeroFlux φ,
      ((cubic_torus_transfer_operators β hβ).1 Γ μt).2.1.formula φ] with u hu hv
    rw [hu, hv]
    apply congrArg (· * _)
    have him := ((transferOperator_sliceEnergy β hβ Γ μt).2.1 u).1
    have hreal := BoundedMultiplication.eq_ofReal_re_of_im_eq_zero him
    rw [magneticDensity, magneticEnergy_zero, Complex.ofReal_exp, Complex.ofReal_neg, ← hreal]
  unfold magneticTransfer
  rw [hM]
  rfl

theorem magneticTransfer_positive {β : ℝ} (hβ : 0 < β) (m : Flux) :
    IsPositiveOp (magneticTransfer Γ hβ m) := by
  let H := Γ.halfTransfer μt β
  let M := magneticMultiplier Γ hβ m
  have hH : IsSymmetricOp H := ((cubic_torus_transfer_operators β hβ).1 Γ μt).2.2.2.half_symm
  have hM : IsPositiveOp M := magneticMultiplier_positive Γ hβ m
  constructor
  · intro x y
    change ⟪x, H (M (H y))⟫_ℂ = ⟪H (M (H x)), y⟫_ℂ
    rw [hH, hM.1, ← hH (M (H x)) y]
  · intro x
    change 0 ≤ (⟪x, H (M (H x))⟫_ℂ : ℂ).re ∧ (⟪x, H (M (H x))⟫_ℂ : ℂ).im = 0
    rw [hH]
    exact hM.2 (H x)

theorem magneticTransfer_traceClass {β : ℝ} (hβ : 0 < β) (m : Flux) :
    IsTraceClassPW (magneticTransfer Γ hβ m) := by
  let H := Γ.halfTransfer μt β
  let M := magneticMultiplier Γ hβ m
  have hH : IsHilbertSchmidtPW H := ((cubic_torus_transfer_operators β hβ).1 Γ μt).2.2.2.half_hilbertSchmidt
  have hM : ‖M‖ ≤ 1 := BoundedMultiplication.opNorm_le_one_of_mul (magneticDensity_bound Γ hβ.le m)
    (magneticMultiplier_formula Γ hβ m)
  refine ⟨H, M * H, hH, Summable.of_nonneg_of_le (fun _ => sq_nonneg _) (fun i => ?_) hH, mul_assoc _ _ _⟩
  apply pow_le_pow_left₀ (norm_nonneg _)
  exact (M.le_opNorm _).trans ((mul_le_mul_of_nonneg_right hM (norm_nonneg _)).trans_eq (one_mul _))

theorem centreSign_comm (e : Flux) (b : Γ.LinkOrbits μt) (g : Wilson.SU2) :
    centreSign Γ μt (cuts e) b * g = g * centreSign Γ μt (cuts e) b := by
  unfold centreSign
  dsimp only
  split_ifs
  · apply Subtype.ext
    change (-1 : Matrix (Fin 2) (Fin 2) ℂ) * g.val = g.val * (-1)
    simp
  · simp

/-- Express the cut on an arbitrary link representative. -/
theorem centreSign_linkClass (e : Flux) (b : SliceLink μt) :
    centreSign Γ μt (cuts e) (Γ.linkClass b) =
      if b.axis ∈ cuts e ∧ Γ.coordResidues (b.source : InfiniteLattice.LatticePoint 1) b.axis = 0
      then centreElt else 1 := by
  let r := TransferOperators.CubicPeriodSublattice.linkRep (Γ.linkClass b)
  obtain ⟨γ, hγ, hb⟩ := Γ.mem_linkOrbit_linkRep b
  have ha : b.axis = r.axis := SliceProduct.axis_eq_of_translateLink hb
  have hsrc : (b.source : InfiniteLattice.LatticePoint 1) = r.source + γ :=
    congrArg InfiniteLattice.Link.initial hb
  have hr (i : Dir) : Γ.coordResidues b.source i = Γ.coordResidues r.source i := by
    simp only [TransferOperators.CubicPeriodSublattice.coordResidues, hsrc, SliceDecomposition.level_add,
      Int.cast_add, SliceDecomposition.level_period_eq_zero (AddSubgroup.mem_inf.mp hγ).1, add_zero]
  unfold centreSign
  rw [ha, hr]

theorem centreSign_ofAxis (e : Flux) (y : SliceSite μt) (i : Dir) (hi : i ≠ μt) :
    centreSign Γ μt (cuts e) (Γ.linkClass (SliceLink.ofAxis y i hi)) =
      if i ∈ cuts e ∧ Γ.coordResidues (y : InfiniteLattice.LatticePoint 1) i = 0
      then centreElt else 1 := by
  have ha : (SliceLink.ofAxis y i hi).axis = i := by
    apply BlockConditionalLaw.axisStep_injective
    rw [← SliceLink.terminal_sub_initial]
    exact add_sub_cancel_left _ _
  rw [centreSign_linkClass, ha]
  rfl

theorem centreSign_shift_transverse (e : Flux) (y : SliceSite μt) (i j : Dir)
    (hi : i ≠ μt) (hj : j ≠ μt) (hij : i ≠ j) :
    centreSign Γ μt (cuts e) (Γ.linkClass (SliceLink.ofAxis (y.shift j hj) i hi)) =
      centreSign Γ μt (cuts e) (Γ.linkClass (SliceLink.ofAxis y i hi)) := by
  rw [centreSign_ofAxis, centreSign_ofAxis]
  have hzero : level i (InfiniteLattice.axisStep 1 j) = 0 := by
    simpa only [one_zsmul, if_neg hij] using (SliceProduct.level_zsmul_axisStep (μ := j) i 1)
  change (if i ∈ cuts e ∧ ((level i (y + InfiniteLattice.axisStep 1 j) : ℤ) : ZMod Γ.side) = 0
      then centreElt else 1) = _
  rw [SliceDecomposition.level_add, hzero, add_zero]
  rfl

/-- A plaquette meets a spatial cut on both parallel edges or on neither edge. -/
theorem holonomy_centreShift (e : Flux) (p : SlicePlaquette μt) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    Γ.holonomyOfFamily p (centreShift Γ μt (cuts e) u) = Γ.holonomyOfFamily p u := by
  let sign (b : SliceLink μt) := centreSign Γ μt (cuts e) (Γ.linkClass b)
  let link (b : SliceLink μt) := u (Γ.linkClass b)
  have low : sign p.topLink = sign p.bottomLink :=
    centreSign_shift_transverse Γ e p.origin _ _ p.lowAxis_ne p.highAxis_ne p.val.lowAxis_lt_highAxis.ne
  have high : sign p.rightLink = sign p.leftLink :=
    centreSign_shift_transverse Γ e p.origin _ _ p.highAxis_ne p.lowAxis_ne p.val.lowAxis_lt_highAxis.ne.symm
  have pair (b d : SliceLink μt) (x y : Wilson.SU2) :
      (sign b * x) * (sign d * y) = (sign b * sign d) * (x * y) := by
    rw [show (sign b * x) * (sign d * y) = sign b * (x * sign d) * y by group,
      show x * sign d = sign d * x from (centreSign_comm Γ e _ x).symm]
    group
  let z := sign p.bottomLink * sign p.leftLink
  have hz (x : Wilson.SU2) : z * x = x * z := by
    exact ((show Commute (sign p.bottomLink) x from centreSign_comm Γ e _ x).mul_left
      (show Commute (sign p.leftLink) x from centreSign_comm Γ e _ x)).eq
  let a := link p.bottomLink
  change (sign p.bottomLink * link p.bottomLink) * (sign p.rightLink * link p.rightLink) *
      (sign p.topLink * link p.topLink)⁻¹ * (sign p.leftLink * link p.leftLink)⁻¹ =
    link p.bottomLink * link p.rightLink * (link p.topLink)⁻¹ * (link p.leftLink)⁻¹
  rw [low, high]
  let b := link p.rightLink
  let c := link p.topLink
  let d := link p.leftLink
  calc
    _ = ((sign p.bottomLink * a) * (sign p.leftLink * b)) *
        (((sign p.leftLink * d) * (sign p.bottomLink * c))⁻¹) := by dsimp only [a, b, c, d]; group
    _ = z * (a * b) * (z * (d * c))⁻¹ := by
      rw [pair, pair, show sign p.leftLink * sign p.bottomLink = sign p.bottomLink * sign p.leftLink from
        centreSign_comm Γ e _ _]
    _ = z * (a * b * (d * c)⁻¹) * z⁻¹ := by group
    _ = (a * b * (d * c)⁻¹) * z * z⁻¹ := by rw [hz]
    _ = _ := by dsimp only [a, b, c, d]; group

theorem magneticEnergy_centreShift (β : ℝ) (e m : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    magneticEnergy Γ β m (centreShift Γ μt (cuts e) u) = magneticEnergy Γ β m u := by
  simp only [magneticEnergy, magneticHolonomy, TransferOperators.CubicPeriodSublattice.orbitHolonomy,
    holonomy_centreShift]

theorem commutes_magneticMultiplier {β : ℝ} (hβ : 0 < β) (m e : Flux) :
    Commute (magneticMultiplier Γ hβ m) (electricTranslation Γ e) := by
  apply ContinuousLinearMap.ext
  intro φ
  apply Lp.ext
  let C := electricTranslation Γ e
  let M := magneticMultiplier Γ hβ m
  have hshift := (centreShift_measurePreserving Γ μt (cuts e)).quasiMeasurePreserving
  filter_upwards [magneticMultiplier_formula Γ hβ m (C φ), centreTranslation_spec Γ μt (cuts e) φ,
    centreTranslation_spec Γ μt (cuts e) (M φ),
    hshift.ae_eq_comp (magneticMultiplier_formula Γ hβ m φ)] with u h₁ h₂ h₃ h₄
  change (M (C φ)) u = (C (M φ)) u
  change (M φ) (centreShift Γ μt (cuts e) u) = _ at h₄
  rw [h₁, h₂, h₃]
  change _ = (M φ) (centreShift Γ μt (cuts e) u)
  rw [h₄]
  simp only [Function.comp_apply, magneticDensity, magneticEnergy_centreShift]

theorem centreShift_gauge (e : Flux) (g : Γ.VertexOrbits μt → Wilson.SU2)
    (u : Γ.LinkOrbits μt → Wilson.SU2) :
    centreShift Γ μt (cuts e) (Γ.orbitGaugeAct g u) = Γ.orbitGaugeAct g (centreShift Γ μt (cuts e) u) := by
  funext b
  change centreSign Γ μt (cuts e) b * (g _ * u b * (g _)⁻¹) =
    g _ * (centreSign Γ μt (cuts e) b * u b) * (g _)⁻¹
  simp only [mul_assoc]
  rw [← mul_assoc (centreSign _ _ _ _) (g _) _, centreSign_comm, mul_assoc]

theorem commutes_gaugeProjection {β : ℝ} (hβ : 0 < β) (e : Flux) :
    Commute (electricTranslation Γ e) (Γ.gaugeProjection μt) := by
  let props := ((cubic_torus_transfer_operators β hβ).1 Γ μt).1
  haveI := CubicTorusOperators.linkOrbits_nonempty Γ μt
  have hhaar := ReflectionPositivityChain.periodic_gibbs_haar_transfer_kernels.2.1 (Γ.LinkOrbits μt)
  apply props.commute_proj
  · intro x y
    exact ((electricTranslation_isSelfAdjoint Γ e).isSymmetric x y).symm
  · intro g
    let σ := centreShift Γ μt (cuts e)
    let f := Γ.orbitGaugeAct g⁻¹
    have hg : MeasurePreserving f (ComplexMatrix2.haarPi (Γ.LinkOrbits μt)) (ComplexMatrix2.haarPi _) :=
      TwistedActionOperators.measurePreserving_twistedConjAction hhaar g⁻¹
    apply ContinuousLinearMap.ext
    intro φ
    apply Lp.ext
    have hs := (centreShift_measurePreserving Γ μt (cuts e)).quasiMeasurePreserving
    filter_upwards [centreTranslation_spec Γ μt (cuts e) (Γ.gaugeRep g φ),
      hs.ae_eq_comp (props.rep_formula g φ), props.rep_formula g (electricTranslation Γ e φ),
      hg.quasiMeasurePreserving.ae_eq_comp (centreTranslation_spec Γ μt (cuts e) φ)] with u h₁ h₂ h₃ h₄
    change (electricTranslation Γ e (Γ.gaugeRep g φ)) u = (Γ.gaugeRep g (electricTranslation Γ e φ)) u
    change (Γ.gaugeRep g φ) (σ u) = φ (f (σ u)) at h₂
    change (electricTranslation Γ e φ) (f u) = φ (σ (f u)) at h₄
    exact (h₁.trans h₂).trans ((congrArg (φ : _ → ℂ) (centreShift_gauge Γ e g⁻¹ u).symm).trans
      (h₃.trans h₄).symm)

theorem commutes_sqrtLink {β : ℝ} (hβ : 0 < β) (e : Flux) :
    Commute (sqrtLinkOperator β (Γ.LinkOrbits μt)) (electricTranslation Γ e) := by
  let J := Γ.LinkOrbits μt
  letI := CubicTorusOperators.linkOrbits_nonempty Γ μt
  let g : Option J → Wilson.SU2 := fun o => o.elim 1 (fun b => (centreSign Γ μt (cuts e) b)⁻¹)
  have he : IsTwistedTranslation (some : J → Option J) (fun _ => none) g (electricTranslation Γ e) := by
    intro φ
    refine (centreTranslation_spec Γ μt (cuts e) φ).trans (Eventually.of_forall fun u => ?_)
    apply congrArg (φ : _ → ℂ)
    funext b
    simp [twistedConjAction, centreShift, g]
  have hG := ReflectionPositivityChain.periodic_gibbs_haar_transfer_kernels
  have hC := ((cubic_torus_transfer_operators β hβ).1 Γ μt).2.2.1.sqrt_continuous
  apply TwistedActionOperators.kernelOperator_commute (hG.2.1 J) hC
    (((hG.2.2.2 J).1 _ hC).2.1) _ he
  intro u v
  exact ((transferKernel_twisted_invariant β hβ J).1 _ some (fun _ => none) g⁻¹ u v).2.1

/-- All electric flips commute with the concrete magnetic transfer on a release cube. -/
theorem magneticTransfer_commutes {β : ℝ} (hβ : 0 < β) (e m : Flux) :
    Commute (magneticTransfer Γ hβ m) (electricTranslation Γ e) := by
  have hh : Commute (Γ.halfTransfer μt β) (electricTranslation Γ e) :=
    (commutes_sqrtLink Γ hβ e).mul_left (commutes_gaugeProjection Γ hβ e).symm
  exact (hh.mul_left (commutes_magneticMultiplier Γ hβ m e)).mul_left hh

theorem magneticTransfer_commutes_proj {β : ℝ} (hβ : 0 < β) (m χ : Flux) :
    Commute (magneticTransfer Γ hβ m) (electricProj Γ χ) := by
  let T := magneticTransfer Γ hβ m
  change T * ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • electricTranslation Γ e) =
    ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • electricTranslation Γ e) * T
  simp only [mul_smul_comm, smul_mul_assoc, Finset.mul_sum, Finset.sum_mul,
    show ∀ e, T * electricTranslation Γ e = electricTranslation Γ e * T from
      fun e => (magneticTransfer_commutes Γ hβ e m).eq]

/-- Half the spatial Wilson energy on each end of the layer. These two
multipliers compose to the full one, including on a magnetic stack. -/
theorem magneticMultiplier_half_sq {β : ℝ} (hβ : 0 < β) (m : Flux) :
    magneticMultiplier Γ (half_pos hβ) m * magneticMultiplier Γ (half_pos hβ) m = magneticMultiplier Γ hβ m := by
  let M := magneticMultiplier Γ (half_pos hβ) m
  apply ContinuousLinearMap.ext
  intro f
  apply Lp.ext
  filter_upwards [magneticMultiplier_formula Γ (half_pos hβ) m (M f),
    magneticMultiplier_formula Γ (half_pos hβ) m f, magneticMultiplier_formula Γ hβ m f] with u h₁ h₂ h₃
  change (M (M f)) u = _
  rw [h₁, h₂, h₃, ← mul_assoc]
  apply congrArg (· * _)
  unfold magneticDensity
  rw [← Complex.ofReal_mul, ← Real.exp_add]
  congr 2
  unfold magneticEnergy
  ring

/-- The symmetrically weighted transfer used by the rectangular kernel construction,
on the release slice. -/
def symmetricMagnetic (β : ℝ) (hβ : 0 < β) (m : Flux) : Γ.SliceL2 μt →L[ℂ] Γ.SliceL2 μt :=
  magneticMultiplier Γ (half_pos hβ) m * Γ.halfTransfer μt β ^ 2 * magneticMultiplier Γ (half_pos hβ) m

def layerFactor {β : ℝ} (hβ : 0 < β) (m : Flux) : Γ.SliceL2 μt →L[ℂ] Γ.SliceL2 μt :=
  magneticMultiplier Γ (half_pos hβ) m * Γ.halfTransfer μt β

theorem layerFactor_products {β : ℝ} (hβ : 0 < β) (m : Flux) :
    (layerFactor Γ hβ m).adjoint * layerFactor Γ hβ m = magneticTransfer Γ hβ m ∧
    layerFactor Γ hβ m * (layerFactor Γ hβ m).adjoint = symmetricMagnetic Γ β hβ m := by
  let M := magneticMultiplier Γ (half_pos hβ) m
  let H := Γ.halfTransfer μt β
  have hM : IsSelfAdjoint M := ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mpr
    (fun x y => ((magneticMultiplier_positive Γ (half_pos hβ) m).1 x y).symm)
  have hH : IsSelfAdjoint H := ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mpr
    (fun x y => (((cubic_torus_transfer_operators β hβ).1 Γ μt).2.2.2.half_symm x y).symm)
  have hs : (layerFactor Γ hβ m).adjoint = H * M := by
    change star (M * H) = H * M
    rw [star_mul, hH.star_eq, hM.star_eq]
  rw [hs]
  constructor
  · change H * M * (M * H) = H * magneticMultiplier Γ hβ m * H
    rw [← magneticMultiplier_half_sq Γ hβ m]
    simp only [M, mul_assoc]
  · change (M * H) * (H * M) = M * H ^ 2 * M
    simp only [pow_two, mul_assoc]

/-- The two symmetric splittings have the same operator norm. In the periodic
sector this is exactly the normalization in Stage 0's calibrated seed. -/
theorem symmetricMagnetic_norm {β : ℝ} (hβ : 0 < β) (m : Flux) :
    ‖symmetricMagnetic Γ β hβ m‖ = ‖magneticTransfer Γ hβ m‖ := by
  obtain ⟨h₁, h₂⟩ := layerFactor_products Γ hβ m
  rw [← h₁, ← h₂]
  exact CStarRing.norm_self_mul_star.trans CStarRing.norm_star_mul_self.symm

theorem symmetricMagnetic_zero_norm {β : ℝ} (hβ : 0 < β) :
    ‖symmetricMagnetic Γ β hβ zeroFlux‖ = ‖Γ.transfer μt β‖ := by
  rw [symmetricMagnetic_norm, magneticTransfer_zero]

/-- A spatial magnetic stack changes the sign of a trace. Gauge changes still
only conjugate its plaquette holonomy. -/
theorem magneticEnergy_gaugeAct {β : ℝ} (hβ : 0 < β) (m : Flux)
    (g : Γ.VertexOrbits μt → Wilson.SU2) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    magneticEnergy Γ β m (Γ.orbitGaugeAct g u) = magneticEnergy Γ β m u := by
  apply congrArg (β * ·)
  apply Finset.sum_congr rfl
  intro c _
  have h := SliceEnergyProperties.holonomyOfFamily_orbitGaugeAct
    ((bond_kernel_symmetric_gauge_invariant β hβ).2.2.1 μt) g u (CubicPeriodSublattice.faceRep c)
  have ht : halfTrace (Γ.orbitHolonomy c (Γ.orbitGaugeAct g u)) = halfTrace (Γ.orbitHolonomy c u) := by
    unfold CubicPeriodSublattice.orbitHolonomy
    rw [h]
    exact congrArg (fun z : ℂ => z.re / 2) (SliceEnergyProperties.fullTrace_conj _ _)
  unfold magneticHolonomy
  split
  · change 1 - halfTrace (Wilson.centerMinus * _) = 1 - halfTrace (Wilson.centerMinus * _)
    simp only [Wilson.halfTrace_centerMinus, ht]
  · rw [ht]

theorem magneticMultiplier_commutes_gaugeProjection {β : ℝ} (hβ : 0 < β) (m : Flux) :
    Commute (magneticMultiplier Γ hβ m) (Γ.gaugeProjection μt) := by
  let props := ((cubic_torus_transfer_operators β hβ).1 Γ μt).1
  let M := magneticMultiplier Γ hβ m
  haveI := CubicTorusOperators.linkOrbits_nonempty Γ μt
  have hhaar := ReflectionPositivityChain.periodic_gibbs_haar_transfer_kernels.2.1 (Γ.LinkOrbits μt)
  apply props.commute_proj M (magneticMultiplier_positive Γ hβ m).1
  intro g
  let σ := Γ.orbitGaugeAct (μ := μt) g⁻¹
  have hg : MeasurePreserving σ (ComplexMatrix2.haarPi (Γ.LinkOrbits μt)) (ComplexMatrix2.haarPi _) :=
    TwistedActionOperators.measurePreserving_twistedConjAction hhaar g⁻¹
  apply ContinuousLinearMap.ext
  intro φ
  apply Lp.ext
  filter_upwards [magneticMultiplier_formula Γ hβ m (Γ.gaugeRep g φ), props.rep_formula g φ,
    props.rep_formula g (M φ), hg.quasiMeasurePreserving.ae_eq_comp (magneticMultiplier_formula Γ hβ m φ)]
    with u h₁ h₂ h₃ h₄
  change (M (Γ.gaugeRep g φ)) u = (Γ.gaugeRep g (M φ)) u
  change (M φ) (σ u) = _ at h₄
  rw [h₁, h₂, h₃]
  change _ = (M φ) (σ u)
  rw [h₄]
  simp only [Function.comp_apply, σ, magneticDensity, magneticEnergy_gaugeAct Γ hβ]

/-- The two kinetic half-steps under the gauge projection are exactly the
release's full Wilson link-product operator followed by the same projection. -/
theorem halfTransfer_squared {β : ℝ} (hβ : 0 < β) :
    Γ.halfTransfer μt β ^ 2 = linkProductOperator β (Γ.LinkOrbits μt) * Γ.gaugeProjection μt := by
  letI := CubicTorusOperators.linkOrbits_nonempty Γ μt
  let A := sqrtLinkOperator β (Γ.LinkOrbits μt)
  let P := Γ.gaugeProjection μt
  let prop := (cubic_torus_transfer_operators β hβ).1 Γ μt
  have hp : P * P = P := prop.1.proj_idempotent
  have hc : A * P = P * A := prop.2.2.2.sqrt_commute_proj
  have ha : A * A = linkProductOperator β (Γ.LinkOrbits μt) :=
    ((sqrt_link_kernel_facts β hβ).1 (Γ.LinkOrbits μt)).2.2.2.2.2.2.2.1.1
  change (A * P) ^ 2 = _
  rw [pow_two, mul_assoc A P, ← mul_assoc P A P, ← hc, mul_assoc A P P, hp, ← mul_assoc, ha]

/-- The explicit symmetric one-step form has one gauge average and the ordinary
one-bond Wilson weight, with half of the magnetic energy on each boundary. -/
theorem symmetricMagnetic_kinetic {β : ℝ} (hβ : 0 < β) (m : Flux) :
    symmetricMagnetic Γ β hβ m =
      magneticMultiplier Γ (half_pos hβ) m * linkProductOperator β (Γ.LinkOrbits μt) *
        magneticMultiplier Γ (half_pos hβ) m * Γ.gaugeProjection μt := by
  let M := magneticMultiplier Γ (half_pos hβ) m
  let P := Γ.gaugeProjection μt
  let L := linkProductOperator β (Γ.LinkOrbits μt)
  rw [symmetricMagnetic, halfTransfer_squared Γ hβ]
  change M * (L * P) * M = M * L * M * P
  have h : P * M = M * P := (magneticMultiplier_commutes_gaugeProjection Γ (half_pos hβ) m).eq.symm
  simp only [mul_assoc, h]


open Module.End in
/-- AB and BA have linearly equivalent eigenspaces at every nonzero eigenvalue,
including multiplicities. The inverse on the eigenspace is z⁻¹ A. -/
theorem product_eigenspaces {H : Type*} [NormedAddCommGroup H] [NormedSpace ℂ H]
    (A B : H →L[ℂ] H) {z : ℂ} (hz : z ≠ 0) :
    Nonempty (Module.End.eigenspace (A * B).toLinearMap z ≃ₗ[ℂ] Module.End.eigenspace (B * A).toLinearMap z) := by
  have send (U V : H →L[ℂ] H) (x : eigenspace (U * V).toLinearMap z) :
      V x ∈ eigenspace (V * U).toLinearMap z := by
    apply mem_eigenspace_iff.mpr
    have hv := mem_eigenspace_iff.mp x.property
    change U (V x) = z • (x : H) at hv
    change V (U (V x)) = z • V x
    rw [hv, map_smul]
  exact ⟨{
    toFun := fun x => ⟨B x, send A B x⟩
    invFun := fun y => z⁻¹ • (⟨A y, send B A y⟩ : eigenspace (A * B).toLinearMap z)
    left_inv := fun x => by
      apply Subtype.ext
      have hx := mem_eigenspace_iff.mp x.property
      change z⁻¹ • (A (B x)) = (x : H)
      change A (B x) = z • (x : H) at hx
      rw [hx, inv_smul_smul₀ hz]
    right_inv := fun y => by
      apply Subtype.ext
      have hy := mem_eigenspace_iff.mp y.property
      change B (z⁻¹ • A y) = (y : H)
      change B (A y) = z • (y : H) at hy
      rw [map_smul, hy, inv_smul_smul₀ hz]
    map_add' := fun x y => Subtype.ext (map_add B _ _)
    map_smul' := fun c x => Subtype.ext (map_smul B _ _) }⟩

theorem symmetricMagnetic_sector_eigenspaces {β : ℝ} (hβ : 0 < β) (m χ : Flux) {z : ℂ} (hz : z ≠ 0) :
    Nonempty (Module.End.eigenspace (magneticTransfer Γ hβ m * electricProj Γ χ).toLinearMap z ≃ₗ[ℂ]
      Module.End.eigenspace (symmetricMagnetic Γ β hβ m * electricProj Γ χ).toLinearMap z) := by
  let J := layerFactor Γ hβ m
  let P := electricProj Γ χ
  have flip (e : Flux) : Commute J (electricTranslation Γ e) := by
    have hh : Commute (Γ.halfTransfer μt β) (electricTranslation Γ e) :=
      (commutes_sqrtLink Γ hβ e).mul_left (commutes_gaugeProjection Γ hβ e).symm
    exact (commutes_magneticMultiplier Γ (half_pos hβ) m e).mul_left hh
  have hp : Commute J P := by
    change J * ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • electricTranslation Γ e) =
      ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • electricTranslation Γ e) * J
    simp only [mul_smul_comm, smul_mul_assoc, Finset.mul_sum, Finset.sum_mul, fun e => (flip e).eq]
  obtain ⟨h₁, h₂⟩ := layerFactor_products Γ hβ m
  have a : (J.adjoint * P) * J = magneticTransfer Γ hβ m * P := by rw [mul_assoc, ← hp.eq, ← mul_assoc, h₁]
  have b : J * (J.adjoint * P) = symmetricMagnetic Γ β hβ m * P := by rw [← mul_assoc, h₂]
  change Nonempty (Module.End.eigenspace (magneticTransfer Γ hβ m * P).toLinearMap z ≃ₗ[ℂ]
      Module.End.eigenspace (symmetricMagnetic Γ β hβ m * P).toLinearMap z)
  rw [← a, ← b]
  exact product_eigenspaces _ _ hz


end MagneticCubes

section SliceCoordinates

open InfiniteLattice SpinHarmonics
local notation "μt" => TimeAxis.timeIdx
abbrev spatialAxis := {i : Dir // i ≠ μt}
abbrev sliceCode (S : ℕ) := spatialAxis → Fin S

/-- The seed rectangle in Stage 0's own convention. -/
def cubeGrid (S a : ℕ) (i : Dir) : ℕ := if i = μt then a else S

def spatialCode (Γ : CubicPeriodSublattice) (x : SliceSite μt) : sliceCode Γ.side :=
  fun i => ⟨(Γ.coordResidues x i.val).val, ZMod.val_lt _⟩

/-- Choose integer representatives of the three spatial residues at time zero. -/
def siteOfCode {S : ℕ} (c : sliceCode S) : SliceSite μt := by
  let z (i : Dir) : ℤ := if h : i = μt then 0 else (c ⟨i,h⟩).val
  exact ⟨⟨fun i => (z i : ℝ), z, fun _ => (mul_one _).symm⟩,
    show (((z μt : ℤ) : ℝ) = 0) by simp [z]⟩

theorem level_siteOfCode {S : ℕ} (c : sliceCode S) (i : spatialAxis) :
    level i.val (siteOfCode c) = (c i).val := by
  apply Int.cast_injective (α := ℝ)
  rw [level_cast]
  simp [siteOfCode, i.property]

theorem spatialCode_siteOfCode (Γ : CubicPeriodSublattice) (c : sliceCode Γ.side) :
    spatialCode Γ (siteOfCode c) = c := by
  funext i
  apply Fin.ext
  change (((level i.val (siteOfCode c) : ℤ) : ZMod Γ.side).val) = _
  rw [level_siteOfCode, Int.cast_natCast, ZMod.val_natCast_of_lt (c i).isLt]

theorem slicePeriods_of_spatialCode (Γ : CubicPeriodSublattice) {x y : SliceSite μt}
    (hc : spatialCode Γ x = spatialCode Γ y) : (y : LatticePoint 1) - x ∈ Γ.slicePeriods μt := by
  apply AddSubgroup.mem_inf.mpr
  refine ⟨Γ.sub_mem_periods (fun i => ?_), (sliceLattice μt).sub_mem y.property x.property⟩
  by_cases h : i = μt
  · subst i
    have hx : (x.val : AmbientSpace) μt = 0 := x.property
    have hy : (y.val : AmbientSpace) μt = 0 := y.property
    simp [level, hx, hy]
  · exact ZMod.val_injective _ (congrArg Fin.val (congrFun hc ⟨i,h⟩))

theorem spatialCode_of_translate (Γ : CubicPeriodSublattice) {x y : SliceSite μt} {γ : LatticePoint 1}
    (hγ : γ ∈ Γ.slicePeriods μt) (hy : (y : LatticePoint 1) = x + γ) : spatialCode Γ y = spatialCode Γ x := by
  funext i
  apply Fin.ext
  simp only [spatialCode, CubicPeriodSublattice.coordResidues, hy, SliceDecomposition.level_add,
    Int.cast_add, SliceDecomposition.level_period_eq_zero (AddSubgroup.mem_inf.mp hγ).1, add_zero]

def vertexFromCode (Γ : CubicPeriodSublattice) : sliceCode Γ.side ≃ Γ.VertexOrbits μt where
  toFun c := Γ.vertexClass (siteOfCode c)
  invFun v := spatialCode Γ (CubicPeriodSublattice.vertexRep v)
  left_inv c := by
    let y := siteOfCode c
    let x := CubicPeriodSublattice.vertexRep (Γ.vertexClass y)
    have he : Γ.vertexOrbit μt x = Γ.vertexOrbit μt y :=
      congrArg Subtype.val (SliceDecomposition.vertexClass_vertexRep (Γ.vertexClass y))
    have hy : y ∈ Γ.vertexOrbit μt x := by rw [he]; exact ⟨0, zero_mem _, (add_zero _).symm⟩
    obtain ⟨γ,hγ,hh⟩ := hy
    exact (spatialCode_of_translate Γ hγ hh).symm.trans (spatialCode_siteOfCode Γ c)
  right_inv v := by
    let y := CubicPeriodSublattice.vertexRep v
    have he : Γ.vertexClass (siteOfCode (spatialCode Γ y)) = Γ.vertexClass y :=
      Subtype.ext (Γ.vertexOrbit_eq_of_sub_mem (slicePeriods_of_spatialCode Γ (spatialCode_siteOfCode Γ _)))
    exact he.trans (SliceDecomposition.vertexClass_vertexRep v)

def releaseLinkLabel (Γ : CubicPeriodSublattice) (b : Γ.LinkOrbits μt) : sliceCode Γ.side × spatialAxis :=
  let l := CubicPeriodSublattice.linkRep b
  (spatialCode Γ l.source, ⟨l.axis, l.axis_ne⟩)

theorem releaseLinkLabel_class (Γ : CubicPeriodSublattice) (l : SliceLink μt) :
    releaseLinkLabel Γ (Γ.linkClass l) = (spatialCode Γ l.source, ⟨l.axis, l.axis_ne⟩) := by
  let b := CubicPeriodSublattice.linkRep (Γ.linkClass l)
  obtain ⟨γ,hγ,hl⟩ := Γ.mem_linkOrbit_linkRep l
  exact Prod.ext (spatialCode_of_translate Γ hγ (congrArg Link.initial hl)).symm
    (Subtype.ext (SliceProduct.axis_eq_of_translateLink hl).symm)

theorem sliceLink_ofAxis_axis (x : SliceSite μt) (i : spatialAxis) :
    (SliceLink.ofAxis x i.val i.property).axis = i.val := by
  apply BlockConditionalLaw.axisStep_injective
  rw [← SliceLink.terminal_sub_initial]
  exact add_sub_cancel_left _ _

theorem linkClass_eq_of_code (Γ : CubicPeriodSublattice) {l b : SliceLink μt}
    (hc : spatialCode Γ l.source = spatialCode Γ b.source) (hi : l.axis = b.axis) : Γ.linkClass l = Γ.linkClass b := by
  apply Subtype.ext
  apply Γ.linkOrbit_eq_of_mem
  refine ⟨(l.source : LatticePoint 1) - b.source, slicePeriods_of_spatialCode Γ hc.symm, Link.ext ?_ ?_⟩
  · change l.val.initial = b.val.initial + (l.val.initial - b.val.initial)
    abel
  · change l.val.terminal = b.val.terminal + (l.val.initial - b.val.initial)
    have h₁ := l.terminal_sub_initial
    have h₂ := b.terminal_sub_initial
    rw [hi] at h₁
    rw [← h₂] at h₁
    calc
      l.val.terminal = (l.val.terminal - l.val.initial) + l.val.initial := (sub_add_cancel _ _).symm
      _ = (b.val.terminal - b.val.initial) + l.val.initial := by rw [h₁]
      _ = _ := by abel

def linkFromCode (Γ : CubicPeriodSublattice) : (sliceCode Γ.side × spatialAxis) ≃ Γ.LinkOrbits μt where
  toFun v := Γ.linkClass (SliceLink.ofAxis (siteOfCode v.1) v.2.val v.2.property)
  invFun := releaseLinkLabel Γ
  left_inv v := by
    rw [releaseLinkLabel_class]
    exact Prod.ext (spatialCode_siteOfCode Γ v.1) (Subtype.ext (sliceLink_ofAxis_axis _ _))
  right_inv b := by
    let l := CubicPeriodSublattice.linkRep b
    let e := SliceLink.ofAxis (siteOfCode (spatialCode Γ l.source)) l.axis l.axis_ne
    change Γ.linkClass e = b
    refine (linkClass_eq_of_code Γ (l := e) (b := l) (spatialCode_siteOfCode Γ _) ?_).trans ?_
    · exact sliceLink_ofAxis_axis _ ⟨l.axis,l.axis_ne⟩
    exact CubicPeriodSublattice.linkClass_linkRep b

def gridSiteCode {S a : ℕ} {t : Fin (cubeGrid S a μt)} (x : timeFiber (cubeGrid S a) t) : sliceCode S :=
  fun i => Fin.cast (if_neg i.property) (x.val i.val)

def gridSiteFromCode (S a : ℕ) (t : Fin (cubeGrid S a μt)) : sliceCode S ≃ timeFiber (cubeGrid S a) t where
  toFun c := ⟨fun i => if h : i = μt then Fin.cast (by rw [h]) t
    else Fin.cast (if_neg h).symm (c ⟨i,h⟩), by simp⟩
  invFun := gridSiteCode
  left_inv c := by funext i; apply Fin.ext; simp [gridSiteCode, i.property] <;> rfl
  right_inv x := by
    apply Subtype.ext
    funext i
    apply Fin.ext
    by_cases h : i = μt
    · subst i
      simpa using (congrArg Fin.val x.property).symm
    · simp [gridSiteCode, h] <;> rfl

def gridLevelLabel (S a : ℕ) (t : Fin (cubeGrid S a μt)) :
    levelBonds (cubeGrid S a) t ≃ (sliceCode S × spatialAxis) where
  toFun b := (gridSiteCode ⟨b.val.val.1, b.property⟩, ⟨b.val.val.2,b.val.property⟩)
  invFun v := ⟨⟨((gridSiteFromCode S a t v.1).val,v.2.val),v.2.property⟩,(gridSiteFromCode S a t v.1).property⟩
  left_inv b := by
    rcases b with ⟨⟨⟨x,i⟩,hi⟩,ht⟩
    exact Subtype.ext (Subtype.ext (Prod.ext
      (congrArg Subtype.val ((gridSiteFromCode S a t).apply_symm_apply ⟨x,ht⟩)) rfl))
  right_inv v := Prod.ext ((gridSiteFromCode S a t).symm_apply_apply v.1) rfl

/-- Slice links in the signed finite integral are in bijection with the very
link orbits on which Stage 0 takes the transfer norm. Time may have a different period. -/
def releaseLayer (Γ : CubicPeriodSublattice) (a : ℕ) (t : Fin (cubeGrid Γ.side a μt)) :
    levelBonds (cubeGrid Γ.side a) t ≃ Γ.LinkOrbits μt :=
  (gridLevelLabel Γ.side a t).trans (linkFromCode Γ)

/-- The product Haar under the spatial bond identification is the release's normalized product Haar. -/
theorem releaseLayer_preserving (Γ : CubicPeriodSublattice) (a : ℕ) (t : Fin (cubeGrid Γ.side a μt)) :
    MeasurePreserving (MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) (releaseLayer Γ a t))
      (levelHaar (cubeGrid Γ.side a) t) (Matrices.ComplexMatrix2.haarPi (Γ.LinkOrbits μt)) := by
  classical
  letI := Fintype.ofFinite (Γ.LinkOrbits μt)
  rw [Matrices.ComplexMatrix2.haarPi, Measure.infinitePi_eq_pi]
  exact measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) (releaseLayer Γ a t)

/-- Under that bijection the finite electric seam is exactly the release centre translation. -/
theorem releaseLayer_flip (Γ : CubicPeriodSublattice) (a : ℕ) (t : Fin (cubeGrid Γ.side a μt))
    (e : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) (b : levelBonds (cubeGrid Γ.side a) t) :
    flipSlice e (fun b => u (releaseLayer Γ a t b)) b =
      centreShift Γ μt (cuts e) u (releaseLayer Γ a t b) := by
  let i : spatialAxis := ⟨b.val.val.2, b.val.property⟩
  let c := (gridLevelLabel Γ.side a t b).1
  change linkCentre _ * u _ = centreSign Γ μt (cuts e)
    (Γ.linkClass (SliceLink.ofAxis (siteOfCode c) i.val i.property)) * u _
  rw [centreSign_ofAxis]
  have hr : Γ.coordResidues (siteOfCode c) i.val = (c i).val := by
    change ((level i.val (siteOfCode c) : ℤ) : ZMod Γ.side) = _
    rw [level_siteOfCode, Int.cast_natCast]
  have hz : Γ.coordResidues (siteOfCode c) i.val = 0 ↔ (c i).val = 0 := by
    rw [hr]
    constructor
    · intro h
      have := congrArg ZMod.val h
      simpa [ZMod.val_natCast_of_lt (c i).isLt] using this
    · intro h; rw [h, Nat.cast_zero]
  have hb : (c i).val = (b.val.val.1 b.val.val.2).val := rfl
  have ok : (i.val ∈ cuts e ∧ Γ.coordResidues (siteOfCode c) i.val = 0) ↔
      (fluxBit e b.val.val.2 = true ∧ (b.val.val.1 b.val.val.2).val = 0) := by
    simp only [mem_cuts, hz, hb]; rfl
  by_cases h : fluxBit e b.val.val.2 = true ∧ (b.val.val.1 b.val.val.2).val = 0
  · rw [if_pos (ok.mpr h)]; simp only [h, decide_true, linkCentre, ite_true]; rfl
  · rw [if_neg (fun hv => h (ok.mp hv))]; simp only [h, decide_false, linkCentre, Bool.false_eq_true, ite_false]

/-- The gauge-averaged one-step kernel, pulled onto the actual release slice.
Magnetic spatial energy is assigned to the starting slice. -/
def releasedLayerKernel (Γ : CubicPeriodSublattice) (a : ℕ) (β : ℝ) (m : Flux)
    (t : Fin (cubeGrid Γ.side a μt)) (u v : Γ.LinkOrbits μt → Wilson.SU2) : ℝ :=
  layerKernel β (stackBits (joinTwist zeroFlux m)) t
    (fun b => u (releaseLayer Γ a t b)) (fun b => v (releaseLayer Γ a (finRotate _ t) b))

/-- The unprojected signed Haar integral, now on one common release configuration
space at all time levels and with the release's electric flip in the unique seam. -/
theorem twistedPartition_eq_releasedCycle (Γ : CubicPeriodSublattice) {a : ℕ} (ha : 2 ≤ a) (β : ℝ) (e m : Flux) :
    twistedPartition β (cubeGrid Γ.side a) (joinTwist e m) =
      ∫ u, ∏ t, releasedLayerKernel Γ a β m t (u t)
        (if t.val = 0 then centreShift Γ μt (cuts e) (u (finRotate _ t)) else u (finRotate _ t))
        ∂Measure.pi (fun _ => Matrices.ComplexMatrix2.haarPi (Γ.LinkOrbits μt)) := by
  let s := cubeGrid Γ.side a
  let E (t : Fin (s μt)) := MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) (releaseLayer Γ a t)
  let F := MeasurableEquiv.piCongrRight E
  have hw : MeasurePreserving F (Measure.pi (levelHaar s))
      (Measure.pi fun _ => Matrices.ComplexMatrix2.haarPi (Γ.LinkOrbits μt)) :=
    measurePreserving_pi _ _ (fun t => releaseLayer_preserving Γ a t)
  let K (u : Fin (s μt) → Γ.LinkOrbits μt → Wilson.SU2) :=
    ∏ t, releasedLayerKernel Γ a β m t (u t)
      (if t.val = 0 then centreShift Γ μt (cuts e) (u (finRotate _ t)) else u (finRotate _ t))
  change twistedPartition β s (joinTwist e m) = ∫ u, K u ∂_
  rw [twistedPartition_eq_electricCycle β e m (by simpa [s,cubeGrid] using ha), ← hw.integral_comp' K]
  apply integral_congr_ae
  filter_upwards with u
  have read (t : Fin (s μt)) : (fun b => F u t (releaseLayer Γ a t b)) = u t := by
    funext b
    exact MeasurableEquiv.piCongrLeft_apply_apply (releaseLayer Γ a t) (β := fun _ => Wilson.SU2) (u t) b
  change (∏ t, _) = ∏ t, releasedLayerKernel Γ a β m t (F u t)
    (if t.val = 0 then centreShift Γ μt (cuts e) (F u (finRotate _ t)) else F u (finRotate _ t))
  apply Finset.prod_congr rfl
  intro t _
  unfold releasedLayerKernel
  rw [read]
  by_cases ht : t.val = 0
  · rw [if_pos ht, if_pos ht]
    have hr := congrArg (flipSlice e) (read (finRotate _ t))
    rw [← hr]
    apply congrArg (layerKernel β (stackBits (joinTwist zeroFlux m)) t (u t))
    funext b
    exact releaseLayer_flip Γ a _ e _ b
  · rw [if_neg ht, if_neg ht, read]


end SliceCoordinates


section RectangularKernel

local notation "μt" => TimeAxis.timeIdx
attribute [local fun_prop] Wilson.continuous_halfTrace

/-- The three spatial periods, with no temporal coordinate in the vertex or bond type. -/
abbrev RectSite (n : spatialAxis → ℕ) := (i : spatialAxis) → Fin (n i)
abbrev RectSlice (n : spatialAxis → ℕ) := RectSite n × spatialAxis → Wilson.SU2
abbrev rectShape (s : Sides) := fun i : spatialAxis => s i.val
abbrev rectHaar (n : spatialAxis → ℕ) : Measure (RectSlice n) := Measure.pi fun _ => Wilson.linkHaar

def rectVertices (s : Sides) (t : Fin (s μt)) : RectSite (rectShape s) ≃ timeFiber s t where
  toFun x := ⟨fun i => if h : i = μt then Fin.cast (by rw [h]) t else x ⟨i,h⟩, by simp⟩
  invFun y := fun i => y.val i.val
  left_inv x := by funext i; simp [i.property]
  right_inv y := by
    apply Subtype.ext
    funext i
    by_cases h : i = μt
    · subst i; simpa using y.property.symm
    · simp [h]

def rectBonds (s : Sides) (t : Fin (s μt)) : levelBonds s t ≃ RectSite (rectShape s) × spatialAxis where
  toFun b := ((rectVertices s t).symm ⟨b.val.val.1,b.property⟩, ⟨b.val.val.2,b.val.property⟩)
  invFun v := ⟨⟨((rectVertices s t v.1).val,v.2.val),v.2.property⟩,(rectVertices s t v.1).property⟩
  left_inv b := by
    rcases b with ⟨⟨⟨x,i⟩,hi⟩,ht⟩
    exact Subtype.ext (Subtype.ext (Prod.ext
      (congrArg Subtype.val ((rectVertices s t).apply_symm_apply ⟨x,ht⟩)) rfl))
  right_inv v := Prod.ext ((rectVertices s t).symm_apply_apply v.1) rfl

def rectStep {n : spatialAxis → ℕ} (x : RectSite n) (i : spatialAxis) : RectSite n :=
  fun j => if j = i then finRotate _ (x j) else x j

theorem rectVertices_spaceStep (s : Sides) (t : Fin (s μt)) (x : RectSite (rectShape s)) (i : spatialAxis) :
    Wilson.step (rectVertices s t x).val i.val = (rectVertices s t (rectStep x i)).val := by
  funext j
  by_cases h : j = μt
  · subst j
    simp [Wilson.step, rectVertices, i.property.symm]
  · by_cases hj : j = i.val
    · subst j
      simp [Wilson.step, rectVertices, rectStep, i.property]
    · have hn : (⟨j,h⟩ : spatialAxis) ≠ i := fun he => hj (congrArg Subtype.val he)
      simp [Wilson.step, rectVertices, rectStep, hj, h, hn]

theorem rectVertices_timeStep (s : Sides) (t : Fin (s μt)) (x : RectSite (rectShape s)) :
    Wilson.step (rectVertices s t x).val μt = (rectVertices s (finRotate _ t) x).val := by
  funext j
  by_cases h : j = μt
  · subst j; simp [Wilson.step, rectVertices]
  · simp [Wilson.step, rectVertices, h]

def firstSpatial (p : Plane) : spatialAxis :=
  ⟨p.val.1, by
    intro h
    have hh := p.property
    rw [h] at hh
    exact (not_lt_of_ge (Fin.le_last p.val.2)) hh⟩

theorem magnetic_temporal_bit (m : Flux) (p : Plane) (ht : p.val.2 = μt) : joinTwist zeroFlux m p = false := by
  obtain ⟨⟨i,j⟩,h⟩ := p
  change j = μt at ht
  subst j
  fin_cases i <;> first | rfl | exact absurd h (by decide)

/-- The four factors of a temporal plaquette are a starting bond, a temporal
bond at its target, an outgoing inverse bond and a temporal inverse at its source. -/
def rectFaceTerm {n : spatialAxis → ℕ} (m : Flux) (u v : RectSlice n) (g : RectSite n → Wilson.SU2)
    (x : RectSite n) (p : Plane) : ℝ :=
  let i := firstSpatial p
  if h : p.val.2 = μt then
    1 - halfTrace (u (x,i) * g (rectStep x i) * (v (x,i))⁻¹ * (g x)⁻¹)
  else
    let j : spatialAxis := ⟨p.val.2,h⟩
    let b := decide (joinTwist zeroFlux m p = true ∧ (x i).val = 0 ∧ (x j).val = 0)
    1 - bitSign b * halfTrace (u (x,i) * u (rectStep x i,j) * (u (rectStep x j,i))⁻¹ * (u (x,j))⁻¹)

/-- This one-step magnetic kernel depends on the spatial periods and coupling alone.
Its vertex Haar variables have the same index set for every temporal period. -/
def rectKernel (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (u v : RectSlice n) : ℝ :=
  ∫ g, Real.exp (-β * ∑ x : RectSite n, ∑ p : Plane, rectFaceTerm m u v g x p)
    ∂Measure.pi (fun _ => Wilson.linkHaar)

/-- The indexed layer of the original signed Haar integral is this same
time-independent rectangle kernel at *each* level. -/
theorem layerKernel_eq_rectKernel (s : Sides) (ha : 2 ≤ s μt) (t : Fin (s μt)) (β : ℝ) (m : Flux)
    (u v : RectSlice (rectShape s)) :
    layerKernel β (stackBits (joinTwist zeroFlux m)) t (u ∘ rectBonds s t) (v ∘ rectBonds s (finRotate _ t)) =
      rectKernel (rectShape s) β m u v := by
  let Y := rectVertices s t
  let E := MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) Y
  have hE : MeasurePreserving E (Measure.pi fun _ => Wilson.linkHaar) (fiberHaar s t) :=
    measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) Y
  unfold layerKernel rectKernel
  rw [← hE.integral_comp']
  apply integral_congr_ae
  filter_upwards with g
  let F := slabField (boundaryField t (u ∘ rectBonds s t) (v ∘ rectBonds s (finRotate _ t))) t (E g)
  have here (x : RectSite (rectShape s)) (i : spatialAxis) : F ((Y x).val,i.val) = u (x,i) := by
    dsimp only [F,slabField,boundaryField]
    rw [dif_neg i.property, dif_pos (Y x).property]
    change u ((rectVertices s t).symm (Y x),i) = u (x,i)
    rw [Equiv.symm_apply_apply]
  have next (x : RectSite (rectShape s)) (i : spatialAxis) :
      F ((rectVertices s (finRotate _ t) x).val,i.val) = v (x,i) := by
    have ht := (rectVertices s (finRotate _ t) x).property
    have hn : (rectVertices s (finRotate _ t) x).val μt ≠ t := by rw [ht]; exact finRotate_ne_self_of_two ha t
    dsimp only [F,slabField,boundaryField]
    rw [dif_neg i.property, dif_neg hn, dif_pos ht]
    change v ((rectVertices s _).symm (rectVertices s _ x),i) = v (x,i)
    rw [Equiv.symm_apply_apply]
  have temporal (x : RectSite (rectShape s)) : F ((Y x).val,μt) = g x := by
    dsimp only [F,slabField]
    rw [dif_pos rfl, dif_pos (Y x).property]
    exact MeasurableEquiv.piCongrLeft_apply_apply Y (β := fun _ => Wilson.SU2) g x
  apply congrArg Real.exp
  apply congrArg (-β * ·)
  rw [← Y.sum_comp]
  apply Finset.sum_congr rfl
  intro x _
  apply Finset.sum_congr rfl
  intro p _
  let i := firstSpatial p
  change 1 - bitSign (stackBits _ (Y x).val p) * halfTrace
    (F ((Y x).val,i.val) * F (Wilson.step (Y x).val i.val,p.val.2) *
      (F (Wilson.step (Y x).val p.val.2,i.val))⁻¹ * (F ((Y x).val,p.val.2))⁻¹) = _
  rw [here, rectVertices_spaceStep s t x i]
  by_cases h : p.val.2 = μt
  · have hb : stackBits (joinTwist zeroFlux m) (Y x).val p = false := by
      simp [stackBits, magnetic_temporal_bit m p h]
    simp only [hb, bitSign, Bool.false_eq_true, if_false, one_mul, rectFaceTerm, dif_pos h]
    rw [h, temporal, rectVertices_timeStep, next, temporal]
  · let j : spatialAxis := ⟨p.val.2,h⟩
    have hi : p.val.1 ≠ μt := i.property
    have hb : stackBits (joinTwist zeroFlux m) (Y x).val p =
        decide (joinTwist zeroFlux m p = true ∧ (x i).val = 0 ∧ (x j).val = 0) := by
      simp only [stackBits, Y, rectVertices, Equiv.coe_fn_mk, dif_neg hi, dif_neg h]
      rfl
    simp only [rectFaceTerm, dif_neg h]
    rw [hb]
    change 1 - _ * halfTrace (u (x,i) * F ((Y (rectStep x i)).val,j.val) *
      (F (Wilson.step (Y x).val j.val,i.val))⁻¹ * (F ((Y x).val,j.val))⁻¹) = _
    rw [here, rectVertices_spaceStep s t x j, here, here]

/-- The three electric cuts now act on a time-independent rectangular slice. -/
def rectFlip {n : spatialAxis → ℕ} (e : Flux) (v : RectSlice n) (b : RectSite n × spatialAxis) : Wilson.SU2 :=
  linkCentre (decide (fluxBit e b.2.val = true ∧ (b.1 b.2).val = 0)) * v b

theorem twistedPartition_eq_rectCycle (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (e m : Flux) :
    twistedPartition β s (joinTwist e m) =
      ∫ u, ∏ t : Fin (s μt), rectKernel (rectShape s) β m (u t)
        (if t.val = 0 then rectFlip e (u (finRotate _ t)) else u (finRotate _ t))
        ∂Measure.pi (fun _ => rectHaar (rectShape s)) := by
  let E (t : Fin (s μt)) := MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) (rectBonds s t)
  let F := MeasurableEquiv.piCongrRight E
  have hw : MeasurePreserving F (Measure.pi (levelHaar s)) (Measure.pi fun _ => rectHaar (rectShape s)) :=
    measurePreserving_pi _ _ (fun t => measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) (rectBonds s t))
  let K (u : Fin (s μt) → RectSlice (rectShape s)) :=
    ∏ t, rectKernel (rectShape s) β m (u t)
      (if t.val = 0 then rectFlip e (u (finRotate _ t)) else u (finRotate _ t))
  change twistedPartition β s (joinTwist e m) = ∫ u, K u ∂_
  rw [twistedPartition_eq_electricCycle β e m ha, ← hw.integral_comp' K]
  apply integral_congr_ae
  filter_upwards with u
  have read (t : Fin (s μt)) : F u t ∘ rectBonds s t = u t :=
    funext fun b => MeasurableEquiv.piCongrLeft_apply_apply (rectBonds s t) (β := fun _ => Wilson.SU2) (u t) b
  change (∏ t, _) = ∏ t, rectKernel (rectShape s) β m (F u t)
    (if t.val = 0 then rectFlip e (F u (finRotate _ t)) else F u (finRotate _ t))
  apply Finset.prod_congr rfl
  intro t _
  rw [← layerKernel_eq_rectKernel s ha t, read]
  by_cases ht : t.val = 0
  · rw [if_pos ht, if_pos ht, ← read (finRotate _ t)]
    rfl
  · rw [if_neg ht, if_neg ht, read]

abbrev RectSpatialPlane := {p : Plane // p.val.2 ≠ μt}

def rectPlanes : spatialAxis ⊕ RectSpatialPlane ≃ Plane where
  toFun := Sum.elim (fun i => ⟨(i.val,μt), (Fin.le_last i.val).lt_of_ne i.property⟩) Subtype.val
  invFun p := if h : p.val.2 = μt then Sum.inl (firstSpatial p) else Sum.inr ⟨p,h⟩
  left_inv
    | .inl i => by simp [firstSpatial]
    | .inr p => by simp [p.property]
  right_inv p := by
    by_cases h : p.val.2 = μt
    · simp only [dif_pos h, Sum.elim_inl]; exact Subtype.ext (Prod.ext rfl h.symm)
    · simp only [dif_neg h, Sum.elim_inr]

def rectSpatialAction {n : spatialAxis → ℕ} (m : Flux) (u : RectSlice n) : ℝ :=
  ∑ x : RectSite n, ∑ p : RectSpatialPlane, rectFaceTerm m u u (fun _ => 1) x p.val

abbrev RectGauges (n : spatialAxis → ℕ) := RectSite n → Wilson.SU2
abbrev rectGaugeHaar (n : spatialAxis → ℕ) : Measure (RectGauges n) := Measure.pi fun _ => Wilson.linkHaar

def rectGauge (n : spatialAxis → ℕ) : C(RectSlice n × RectGauges n, RectSlice n) :=
  ⟨fun z b => z.2 b.1 * z.1 b * (z.2 (rectStep b.1 b.2))⁻¹, by fun_prop⟩

def rectTemporal (n : spatialAxis → ℕ) (β : ℝ) : C(RectSlice n × RectSlice n, ℝ) :=
  ⟨fun z => Real.exp (-β * ∑ b, (1 - halfTrace (z.2 b * (z.1 b)⁻¹))), by
    fun_prop (disch := exact Wilson.continuous_halfTrace)⟩

theorem rectKernel_factorization (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (u v : RectSlice n) :
    rectKernel n β m u v = Real.exp (-β * rectSpatialAction m u) *
      ∫ g, rectTemporal n β (u,rectGauge n (v,g)) ∂rectGaugeHaar n := by
  rw [← integral_const_mul]
  apply integral_congr_ae
  filter_upwards with g
  have timed (x : RectSite n) (i : spatialAxis) : rectFaceTerm m u v g x (rectPlanes (.inl i)) =
      1 - halfTrace (rectGauge n (v,g) (x,i) * (u (x,i))⁻¹) := by
    change 1 - halfTrace (u (x,i) * g (rectStep x i) * (v (x,i))⁻¹ * (g x)⁻¹) =
      1 - halfTrace (g x * v (x,i) * (g (rectStep x i))⁻¹ * (u (x,i))⁻¹)
    rw [← Wilson.halfTrace_inv (g x * v (x,i) * (g (rectStep x i))⁻¹ * (u (x,i))⁻¹)]
    simp only [mul_inv_rev, inv_inv, mul_assoc]
  have spaced (x : RectSite n) (p : RectSpatialPlane) : rectFaceTerm m u v g x (rectPlanes (.inr p)) =
      rectFaceTerm m u u (fun _ => 1) x p.val := by
    change rectFaceTerm m u v g x p.val = rectFaceTerm m u u (fun _ => 1) x p.val
    simp only [rectFaceTerm,dif_neg p.property]
  have split (x : RectSite n) : (∑ p : Plane, rectFaceTerm m u v g x p) =
      (∑ p : RectSpatialPlane, rectFaceTerm m u u (fun _ => 1) x p.val) +
      ∑ i : spatialAxis, (1 - halfTrace (rectGauge n (v,g) (x,i) * (u (x,i))⁻¹)) := by
    rw [← rectPlanes.sum_comp (rectFaceTerm m u v g x), Fintype.sum_sum_type]
    exact (congrArg₂ (· + ·) (Finset.sum_congr rfl (fun i _ => timed x i))
      (Finset.sum_congr rfl (fun p _ => spaced x p))).trans (add_comm _ _)
  change Real.exp _ = Real.exp _ * Real.exp _
  rw [← Real.exp_add]
  apply congrArg Real.exp
  simp only [split, Finset.sum_add_distrib, rectSpatialAction, Fintype.sum_prod_type, mul_add]

theorem continuous_rectSpatialAction (n : spatialAxis → ℕ) (m : Flux) :
    Continuous (rectSpatialAction (n := n) m) := by
  apply continuous_finsetSum
  intro x _
  apply continuous_finsetSum
  intro p _
  simp only [rectFaceTerm, dif_neg p.property]
  fun_prop (disch := exact Wilson.continuous_halfTrace)

attribute [local fun_prop] continuous_rectSpatialAction

def rectHalfWeight (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) : C(RectSlice n, ℝ) :=
  ⟨fun u => Real.exp (-β * rectSpatialAction m u / 2), by fun_prop (disch := exact continuous_rectSpatialAction n m)⟩

theorem rectGauge_mul {n : spatialAxis → ℕ} (u : RectSlice n) (g h : RectGauges n) :
    rectGauge n (rectGauge n (u,h),g) = rectGauge n (u,g*h) := by
  funext b
  simp [rectGauge, mul_assoc]

theorem rectTemporal_gauge (n : spatialAxis → ℕ) (β : ℝ) (u v : RectSlice n) (h : RectGauges n) :
    rectTemporal n β (rectGauge n (u,h),rectGauge n (v,h)) = rectTemporal n β (u,v) := by
  change Real.exp (-β * ∑ b, _) = Real.exp (-β * ∑ b, _)
  congr 2
  apply Finset.sum_congr rfl
  intro b _
  rw [show rectGauge n (v,h) b * (rectGauge n (u,h) b)⁻¹ =
    h b.1 * (v b * (u b)⁻¹) * (h b.1)⁻¹ by simp [rectGauge,mul_assoc], Wilson.halfTrace_conjugate]

def rectSymKernel (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) : C(RectSlice n × RectSlice n, ℝ) :=
  Kernel.sandwich (rectGaugeHaar n) (rectGauge n) (rectHalfWeight n β m) (rectTemporal n β)

theorem rectSymKernel_apply (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (u v : RectSlice n) :
    rectSymKernel n β m (u,v) = rectHalfWeight n β m u * rectHalfWeight n β m v *
      ∫ g, rectTemporal n β (u,rectGauge n (v,g)) ∂rectGaugeHaar n := by
  let a := rectGauge n
  let q := rectTemporal n β
  let ν := rectGaugeHaar n
  change _ * (∫ p : RectGauges n × RectGauges n, q (a (u,p.1),a (v,p.2)) ∂ν.prod ν) = _
  congr 1
  have hi : Integrable (fun p : RectGauges n × RectGauges n => q (a (u,p.1),a (v,p.2))) (ν.prod ν) :=
    Continuous.integrable_of_hasCompactSupport (by fun_prop) (HasCompactSupport.of_compactSpace _)
  rw [integral_prod _ hi]
  have avg (g : RectGauges n) : (∫ h, q (a (u,g), a (v,h)) ∂ν) = ∫ h, q (u,a (v,h)) ∂ν := by
    calc
      _ = ∫ h, q (a (u,g),a (v,g*h)) ∂ν :=
        (integral_mul_left_eq_self (μ := ν) (fun h => q (a (u,g),a (v,h))) g).symm
      _ = _ := by
        apply integral_congr_ae
        exact ae_of_all _ fun h => by
          change rectTemporal n β (rectGauge n (u,g),rectGauge n (v,g*h)) = _
          rw [← rectGauge_mul, rectTemporal_gauge]
  simp only [avg, integral_const, probReal_univ, one_smul]
  rfl

/-- Changing the placement of spatial weights is a similarity by a strictly
positive bounded multiplier on each finite rectangle. -/
theorem rectKernel_eq_sym (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (u v : RectSlice n) :
    rectKernel n β m u v = rectHalfWeight n β m u / rectHalfWeight n β m v * rectSymKernel n β m (u,v) := by
  rw [rectKernel_factorization, rectSymKernel_apply]
  let h := rectHalfWeight n β m
  have hp : h v ≠ 0 := (Real.exp_pos _).ne'
  have he : Real.exp (-β * rectSpatialAction m u) = h u * h u := by
    change _ = Real.exp _ * Real.exp _
    rw [← Real.exp_add]; congr 1; ring
  rw [he]
  change h u * h u * _ = h u / h v * (h u * h v * _)
  field_simp


/-- The finite Gram argument is row 1506's proof for the Wilson kinetic weight,
applied directly to the three separately indexed spatial periods. -/
theorem rectTemporal_gram (n : spatialAxis → ℕ) {β : ℝ} (hβ : 0 ≤ β) :
    rectTemporal n β ∈ closure {p | Kernel.FiniteGram p} := by
  let E := RectSite n × spatialAxis
  have hc (b : E) (i j : Fin 2) : Continuous (fun u : RectSlice n => (u b).val i j) :=
    (continuous_subtype_val.comp (continuous_apply b)).matrix_elem i j
  let re (b : E) (i j : Fin 2) : C(RectSlice n, ℝ) := ⟨_,Complex.continuous_re.comp (hc b i j)⟩
  let im (b : E) (i j : Fin 2) : C(RectSlice n, ℝ) := ⟨_,Complex.continuous_im.comp (hc b i j)⟩
  let Q := (β / 2) • ∑ b : E, ∑ i : Fin 2, ∑ j : Fin 2, (Kernel.gram (re b i j) + Kernel.gram (im b i j))
  have hQ : Kernel.FiniteGram Q :=
    (Kernel.FiniteGram.sum _ _ fun b _ => Kernel.FiniteGram.sum _ _ fun i _ => Kernel.FiniteGram.sum _ _ fun j _ =>
      (Kernel.FiniteGram.atom (re b i j)).add (Kernel.FiniteGram.atom (im b i j))).smul (by positivity)
  let c := Real.exp (-β * Fintype.card E)
  have hs : rectTemporal n β = c • NormedSpace.exp Q := by
    ext z
    have ev : (NormedSpace.exp Q) z = Real.exp (Q z) := by
      rw [Real.exp_eq_exp_ℝ]
      exact NormedSpace.map_exp (ContinuousMap.evalAlgHom ℝ ℝ z) (continuous_eval_const _) _
    change Real.exp (-β * ∑ b, (1 - halfTrace (z.2 b * (z.1 b)⁻¹))) = Real.exp _ * (NormedSpace.exp Q) z
    rw [ev, ← Real.exp_add]
    congr 1
    simp only [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul,
      mul_one, Wilson.halfTrace_mul_inv_entries, Q, ContinuousMap.smul_apply, smul_eq_mul,
      ContinuousMap.sum_apply, ContinuousMap.add_apply, Kernel.gram, re, im, ContinuousMap.coe_mk, ← Finset.sum_div,
      Function.comp_apply]
    ring
  rw [hs]
  have hm : closure {p : C(RectSlice n × RectSlice n, ℝ) | Kernel.FiniteGram p} ⊆
      (fun p => c • p) ⁻¹' closure {p | Kernel.FiniteGram p} := by
    apply (isClosed_closure.preimage (continuous_const_smul c)).closure_subset_iff.mpr
    intro p hp
    exact subset_closure (Kernel.FiniteGram.smul hp (Real.exp_pos _).le)
  exact hm hQ.exp_mem_closure

def rectSymOperator (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) :
    Kernel.Space (rectHaar n) →L[ℂ] Kernel.Space (rectHaar n) :=
  Kernel.realOperator (rectHaar n) (rectSymKernel n β m)

theorem rectSymOperator_positive (n : spatialAxis → ℕ) {β : ℝ} (hβ : 0 ≤ β) (m : Flux) :
    (rectSymOperator n β m).IsPositive :=
  Kernel.positive_sandwich _ _ _ _ (rectTemporal_gram n hβ)


theorem rectSpatialAction_flip (n : spatialAxis → ℕ) (e m : Flux) (u : RectSlice n) :
    rectSpatialAction m (rectFlip e u) = rectSpatialAction m u := by
  let cut (x : RectSite n) (i : spatialAxis) := decide (fluxBit e i.val = true ∧ (x i).val = 0)
  have transverse (x : RectSite n) (i j : spatialAxis) (hj : j ≠ i) : cut (rectStep x i) j = cut x j := by simp [cut,rectStep,hj]
  unfold rectSpatialAction
  apply Finset.sum_congr rfl
  intro x _
  apply Finset.sum_congr rfl
  intro p _
  let i := firstSpatial p.val
  let j : spatialAxis := ⟨p.val.val.2,p.property⟩
  have hij : i ≠ j := fun hh => p.val.property.ne (congrArg Subtype.val hh)
  have word : (rectFlip e u (x,i) * rectFlip e u (rectStep x i,j) *
      (rectFlip e u (rectStep x j,i))⁻¹ * (rectFlip e u (x,j))⁻¹) =
      u (x,i) * u (rectStep x i,j) * (u (rectStep x j,i))⁻¹ * (u (x,j))⁻¹ := by
    change (linkCentre (cut x i) * _) * (linkCentre (cut (rectStep x i) j) * _) *
      (linkCentre (cut (rectStep x j) i) * _)⁻¹ * (linkCentre (cut x j) * _)⁻¹ = _
    rw [transverse x i j hij.symm, transverse x j i hij, linkCentre_inv_apply, linkCentre_inv_apply,
      linkCentre_mul_apply, linkCentre_mul_apply, linkCentre_mul_apply,
      (by decide : ∀ a b : Bool, xor (xor (xor a b) a) b = false)]
    simp [linkCentre]
  simp only [rectFaceTerm,dif_neg p.property]
  exact congrArg (fun z => 1 - bitSign (decide (joinTwist zeroFlux m p.val = true ∧
    (x i).val = 0 ∧ (x j).val = 0)) * halfTrace z) word

theorem rectGauge_flip (n : spatialAxis → ℕ) (e : Flux) (v : RectSlice n) (g : RectGauges n) :
    rectGauge n (rectFlip e v,g) = rectFlip e (rectGauge n (v,g)) := by
  funext b
  change g b.1 * (linkCentre _ * v b) * _ = linkCentre _ * (g b.1 * v b * _)
  simp only [mul_assoc]
  rw [← mul_assoc (g b.1), ← (linkCentre_comm _ (g b.1)).eq, mul_assoc]

theorem rectTemporal_flip (n : spatialAxis → ℕ) (e : Flux) (β : ℝ) (u v : RectSlice n) :
    rectTemporal n β (rectFlip e u,rectFlip e v) = rectTemporal n β (u,v) := by
  change Real.exp (-β * ∑ b, _) = Real.exp (-β * ∑ b, _)
  congr 2
  apply Finset.sum_congr rfl
  intro b _
  let z := linkCentre (decide (fluxBit e b.2.val = true ∧ (b.1 b.2).val = 0))
  change 1 - halfTrace ((z * v b) * (z * u b)⁻¹) = _
  rw [show (z * v b) * (z * u b)⁻¹ = z * (v b * (u b)⁻¹) * z⁻¹ by group,
    Wilson.halfTrace_conjugate]

theorem rectHalfWeight_flip (n : spatialAxis → ℕ) (e m : Flux) (β : ℝ) (u : RectSlice n) :
    rectHalfWeight n β m (rectFlip e u) = rectHalfWeight n β m u := by
  simp only [rectHalfWeight,ContinuousMap.coe_mk,rectSpatialAction_flip]

theorem rectSymKernel_flip (n : spatialAxis → ℕ) (e m : Flux) (β : ℝ) (u v : RectSlice n) :
    rectSymKernel n β m (rectFlip e u,rectFlip e v) = rectSymKernel n β m (u,v) := by
  simp only [rectSymKernel_apply,rectHalfWeight_flip,rectGauge_flip,rectTemporal_flip]

set_option maxHeartbeats 1200000 in
/-- The similarity factors cancel around a signed cycle, including at the
electric seam because its flip preserves the magnetic spatial half-weight. -/
theorem twistedPartition_eq_symCycle (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (e m : Flux) :
    twistedPartition β s (joinTwist e m) =
      ∫ u, ∏ t : Fin (s μt), rectSymKernel (rectShape s) β m (u t,
        if t.val = 0 then rectFlip e (u (finRotate _ t)) else u (finRotate _ t))
        ∂Measure.pi (fun _ => rectHaar (rectShape s)) := by
  rw [twistedPartition_eq_rectCycle s ha β e m]
  apply integral_congr_ae
  filter_upwards with u
  let h := rectHalfWeight (rectShape s) β m
  have same (t : Fin (s μt)) : h (if t.val = 0 then rectFlip e (u (finRotate _ t)) else u (finRotate _ t)) =
      h (u (finRotate _ t)) := by
    by_cases ht : t.val = 0
    · rw [if_pos ht]
      exact rectHalfWeight_flip (rectShape s) e m β (u (finRotate _ t))
    · rw [if_neg ht]
  let v (t : Fin (s μt)) := if t.val = 0 then rectFlip e (u (finRotate _ t)) else u (finRotate _ t)
  let q (t : Fin (s μt)) := rectSymKernel (rectShape s) β m (u t,v t)
  have each (t : Fin (s μt)) : rectKernel (rectShape s) β m (u t) (v t) =
      (h (u t) / h (u (finRotate _ t))) * q t := by
    calc
      _ = (h (u t) / h (v t)) * q t := rectKernel_eq_sym _ β m _ _
      _ = _ := by rw [show h (v t) = h (u (finRotate _ t)) from same t]
  change (∏ t, rectKernel (rectShape s) β m (u t) (v t)) = ∏ t, q t
  rw [Finset.prod_congr rfl (fun t _ => each t), Finset.prod_mul_distrib, Finset.prod_div_distrib,
    Equiv.prod_comp (finRotate _) (fun t => h (u t))]
  have hp : (∏ t, h (u t)) ≠ 0 := Finset.prod_ne_zero_iff.mpr (fun _ _ => (Real.exp_pos _).ne')
  rw [div_self hp,one_mul]


open scoped InnerProductSpace

theorem continuous_rectKernel (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) :
    Continuous (fun q : RectSlice n × RectSlice n => rectKernel n β m q.1 q.2) := by
  rw [show (fun z : RectSlice n × RectSlice n => rectKernel n β m z.1 z.2) =
      (fun z => rectHalfWeight n β m z.1 / rectHalfWeight n β m z.2 * rectSymKernel n β m z) from
    funext fun z => rectKernel_eq_sym n β m z.1 z.2]
  exact (((rectHalfWeight n β m).continuous.comp continuous_fst).div
    ((rectHalfWeight n β m).continuous.comp continuous_snd) (fun _ => (Real.exp_pos _).ne')).mul
    (rectSymKernel n β m).continuous

def rectSeamKernel (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) (z : RectSlice n × RectSlice n) : ℂ :=
  rectKernel n β m z.1 (rectFlip e z.2)

theorem rectFlip_zero {n : spatialAxis → ℕ} (v : RectSlice n) : rectFlip zeroFlux v = v := by
  funext b
  have h : fluxBit zeroFlux b.2.val = false := by
    rcases b.2 with ⟨i,hi⟩
    fin_cases i <;> rfl
  simp [rectFlip,h,linkCentre]

theorem rectSeamKernel_memLp (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) :
    MemLp (rectSeamKernel n β m e) 2 ((rectHaar n).prod (rectHaar n)) := by
  have hf : Continuous (rectFlip (n := n) e) :=
    continuous_pi (fun b => continuous_const.mul (continuous_apply b))
  exact (Complex.continuous_ofReal.comp ((continuous_rectKernel n β m).comp
    (continuous_fst.prodMk (hf.comp continuous_snd)))).memLp_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)

def rectOperator (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) :
    Kernel.Space (rectHaar n) →L[ℂ] Kernel.Space (rectHaar n) :=
  Kernel.operator _ (rectSeamKernel_memLp n β m e)

def rectFlipEquiv (n : spatialAxis → ℕ) (e : Flux) : RectSlice n ≃ᵐ RectSlice n :=
  MeasurableEquiv.piCongrRight fun b => MeasurableEquiv.mulLeft
    (linkCentre (decide (fluxBit e b.2.val = true ∧ (b.1 b.2).val = 0)))

theorem rectFlip_preserving (n : spatialAxis → ℕ) (e : Flux) :
    MeasurePreserving (rectFlipEquiv n e) (rectHaar n) (rectHaar n) :=
  measurePreserving_pi _ _ (fun _ => measurePreserving_mul_left Wilson.linkHaar _)

theorem rectFlip_involution {n : spatialAxis → ℕ} (e : Flux) (v : RectSlice n) :
    rectFlip e (rectFlip e v) = v := by
  funext b
  change linkCentre _ * (linkCentre _ * v b) = v b
  let z := linkCentre (decide (fluxBit e b.2.val = true ∧ (b.1 b.2).val = 0))
  change z * (z * v b) = v b
  calc
    _ = z⁻¹ * (z * v b) := congrArg (· * (z * v b)) (linkCentre_inv _).symm
    _ = _ := inv_mul_cancel_left _ _

def rectTranslation (n : spatialAxis → ℕ) (e : Flux) : Kernel.Space (rectHaar n) →L[ℂ] Kernel.Space (rectHaar n) :=
  (Lp.compMeasurePreservingₗᵢ ℂ (rectFlipEquiv n e) (rectFlip_preserving n e)).toContinuousLinearMap

theorem rectFlip_add (n : spatialAxis → ℕ) (e f : Flux) :
    rectFlip (n := n) (fluxAdd e f) = rectFlip f ∘ rectFlip e := by
  funext u b
  dsimp only [rectFlip, Function.comp_apply]
  rw [← mul_assoc, ← linkCentre_xor]
  apply congrArg (fun d => linkCentre d * u b)
  by_cases hc : (b.1 b.2).val = 0 <;> cases he : fluxBit e b.2.val <;> cases hf : fluxBit f b.2.val <;>
    simp [fluxBit_add,hc,he,hf]

theorem rectTranslation_mul (n : spatialAxis → ℕ) (e f : Flux) :
    rectTranslation n e * rectTranslation n f = rectTranslation n (fluxAdd e f) := by
  apply ContinuousLinearMap.ext
  intro u
  change Lp.compMeasurePreserving _ _ (Lp.compMeasurePreserving _ _ u) = Lp.compMeasurePreserving _ _ u
  rw [← Lp.compMeasurePreserving_comp_apply]
  congr 2
  exact (rectFlip_add n e f).symm

theorem rectTranslation_zero (n : spatialAxis → ℕ) : rectTranslation n zeroFlux = 1 := by
  apply ContinuousLinearMap.ext
  intro f
  let C := Lp.compMeasurePreservingₗᵢ ℂ _ (rectFlip_preserving n zeroFlux) (p := (2 : ℝ≥0∞)) (E := ℂ)
  apply C.injective
  exact DFunLike.congr_fun (rectTranslation_mul n zeroFlux zeroFlux) f

theorem rectTranslation_selfAdjoint (n : spatialAxis → ℕ) (e : Flux) :
    IsSelfAdjoint (rectTranslation n e) := by
  let C := Lp.compMeasurePreservingₗᵢ ℂ _ (rectFlip_preserving n e) (p := (2 : ℝ≥0∞)) (E := ℂ)
  have hh (f : Kernel.Space (rectHaar n)) : C (C f) = f := by
    have he := rectTranslation_mul n e e
    rw [(by decide : ∀ e : Flux, fluxAdd e e = zeroFlux) e,rectTranslation_zero] at he
    exact DFunLike.congr_fun he f
  apply ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mpr
  intro f g
  change ⟪C f,g⟫_ℂ = ⟪f,C g⟫_ℂ
  calc
    _ = ⟪C f,C (C g)⟫_ℂ := by rw [hh]
    _ = _ := C.inner_map_map f (C g)

def rectProj (n : spatialAxis → ℕ) (χ : Flux) := characterProj (rectTranslation n) χ

theorem rectProj_idempotent (n : spatialAxis → ℕ) (χ : Flux) : rectProj n χ * rectProj n χ = rectProj n χ := by
  simpa only [rectProj,if_true] using characterProj_mul _ (rectTranslation_mul n) χ χ

theorem rectProj_selfAdjoint (n : spatialAxis → ℕ) (χ : Flux) : IsSelfAdjoint (rectProj n χ) := by
  unfold IsSelfAdjoint rectProj characterProj
  simp [star_smul,(rectTranslation_selfAdjoint n _).star_eq]

/-- Right multiplication by the centre translation inserts the seam in the
second variable of any square-integrable kernel. -/
theorem rectRight_insert (n : spatialAxis → ℕ) (e : Flux) (k : RectSlice n × RectSlice n → ℂ)
    (hk : MemLp k 2 ((rectHaar n).prod (rectHaar n)))
    (hl : MemLp (fun z => k (z.1,rectFlip e z.2)) 2 ((rectHaar n).prod (rectHaar n))) :
    Kernel.operator _ hl = Kernel.operator k hk * rectTranslation n e := by
  let C := rectTranslation n e
  apply ContinuousLinearMap.ext
  intro f
  apply Lp.ext
  have hC := Lp.coeFn_compMeasurePreserving f (rectFlip_preserving n e)
  filter_upwards [Kernel.operator_apply hl f, Kernel.operator_apply hk (C f)] with x hx hy
  change (Kernel.operator _ hl f) x = (Kernel.operator k hk (C f)) x
  rw [hx,hy]
  calc
    _ = ∫ y, k (x,y) * f (rectFlip e y) ∂rectHaar n := by
      rw [← (rectFlip_preserving n e).integral_comp' (fun y => k (x,y) * f (rectFlip e y))]
      exact integral_congr_ae (ae_of_all _ fun y => by
        change k (x,rectFlip e y) * f y = k (x,rectFlip e y) * f (rectFlip e (rectFlip e y))
        rw [rectFlip_involution])
    _ = _ := integral_congr_ae (hC.mono fun y hy' => congrArg (k (x,y) * ·) hy'.symm)

/-- Simultaneous centre equivariance also gives the same kernel by placing
the translation on the other end of the step. -/
theorem rectLeft_insert (n : spatialAxis → ℕ) (e : Flux) (k : RectSlice n × RectSlice n → ℂ)
    (hk : MemLp k 2 ((rectHaar n).prod (rectHaar n)))
    (hl : MemLp (fun z => k (z.1,rectFlip e z.2)) 2 ((rectHaar n).prod (rectHaar n)))
    (hflip : ∀ u v, k (rectFlip e u,rectFlip e v) = k (u,v)) :
    rectTranslation n e * Kernel.operator k hk = Kernel.operator _ hl := by
  let A := Kernel.operator k hk
  let C := rectTranslation n e
  apply ContinuousLinearMap.ext
  intro f
  apply Lp.ext
  have h₁ := Lp.coeFn_compMeasurePreserving (A f) (rectFlip_preserving n e)
  have h₂ := (rectFlip_preserving n e).quasiMeasurePreserving.ae_eq_comp (Kernel.operator_apply hk f)
  filter_upwards [h₁,h₂,Kernel.operator_apply hl f] with x hx hy hz
  change (C (A f)) x = (Kernel.operator _ hl f) x
  refine (hx.trans hy).trans (Eq.trans ?_ hz.symm)
  apply integral_congr_ae
  filter_upwards with y
  have h := hflip x (rectFlip e y)
  rw [rectFlip_involution] at h
  exact congrArg (· * f y) h

def rectSymEntry (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (z : RectSlice n × RectSlice n) : ℂ :=
  rectSymKernel n β m z

theorem rectSymEntry_memLp (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) :
    MemLp (rectSymEntry n β m) 2 ((rectHaar n).prod (rectHaar n)) :=
  (Complex.continuous_ofReal.comp (rectSymKernel n β m).continuous).memLp_of_hasCompactSupport
    (HasCompactSupport.of_compactSpace _)

theorem rectSymSeam_memLp (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) :
    MemLp (fun z : RectSlice n × RectSlice n => rectSymEntry n β m (z.1,rectFlip e z.2))
      2 ((rectHaar n).prod (rectHaar n)) := by
  have hf : Continuous (rectFlip (n := n) e) := continuous_pi (fun _ => continuous_const.mul (continuous_apply _))
  exact ((Complex.continuous_ofReal.comp (rectSymKernel n β m).continuous).comp
    (continuous_fst.prodMk (hf.comp continuous_snd))).memLp_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)

theorem rectSymOperator_eq (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) :
    rectSymOperator n β m = Kernel.operator _ (rectSymEntry_memLp n β m) := rfl

theorem rectSymOperator_commutes (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) :
    Commute (rectSymOperator n β m) (rectTranslation n e) := by
  rw [rectSymOperator_eq]
  exact (rectRight_insert n e _ (rectSymEntry_memLp n β m) (rectSymSeam_memLp n β m e)).symm.trans
    (rectLeft_insert n e _ _ _ (fun u v => congrArg Complex.ofReal (rectSymKernel_flip n e m β u v))).symm

theorem rectSymOperator_commutes_proj (n : spatialAxis → ℕ) (β : ℝ) (m χ : Flux) :
    Commute (rectSymOperator n β m) (rectProj n χ) := by
  let T := rectSymOperator n β m
  change T * ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • rectTranslation n e) =
    ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • rectTranslation n e) * T
  simp only [mul_smul_comm, smul_mul_assoc, Finset.mul_sum, Finset.sum_mul,
    show ∀ e, T * rectTranslation n e = rectTranslation n e * T from fun e => (rectSymOperator_commutes n β m e).eq]

def rectSector (n : spatialAxis → ℕ) (β : ℝ) (χ m : Flux) :=
  rectSymOperator n β m * rectProj n χ

theorem rectSector_positive (n : spatialAxis → ℕ) {β : ℝ} (hβ : 0 ≤ β) (χ m : Flux) :
    (rectSector n β χ m).IsPositive := by
  let T := rectSymOperator n β m
  let P := rectProj n χ
  have h := (rectSymOperator_positive n hβ m).adjoint_conj P
  have hP : P.adjoint = P := (rectProj_selfAdjoint n χ).star_eq
  change (P.adjoint * (T * P)).IsPositive at h
  rw [hP, ← mul_assoc, ← (rectSymOperator_commutes_proj n β m χ).eq, mul_assoc,rectProj_idempotent] at h
  exact h


/-- Domination of a complex kernel by a nonnegative real kernel controls its
operator norm. Apply the positive kernel to the pointwise modulus of the input. -/
theorem kernel_norm_domination {X : Type*} [MeasurableSpace X] {μ : Measure X} [IsProbabilityMeasure μ]
    {k : X × X → ℝ} {l : X × X → ℂ} (hk : MemLp k 2 (μ.prod μ))
    (hkc : MemLp (fun z => (k z : ℂ)) 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ))
    {C : ℝ} (hC : 0 ≤ C) (hn : ∀ z,0 ≤ k z) (hb : ∀ z, ‖l z‖ ≤ C * k z) :
    ‖Kernel.operator l hl‖ ≤ C * ‖Kernel.operator _ hkc‖ := by
  let T := Kernel.operator _ hkc
  apply (Kernel.operator l hl).opNorm_le_bound (mul_nonneg hC (norm_nonneg T))
  intro f
  let absf (x : X) : ℂ := ‖f x‖
  have ha : MemLp absf 2 μ := (Lp.memLp f).of_le
    (Complex.continuous_ofReal.comp_aestronglyMeasurable (Lp.aestronglyMeasurable f).norm) (ae_of_all _ fun x => by simp [absf])
  let g := ha.toLp absf
  have hnorm : ‖g‖ = ‖f‖ := by
    have eqn : ∀ᵐ x ∂μ, ‖g x‖ = ‖f x‖ := ha.coeFn_toLp.mono fun x hx => by simp [g,hx,absf]
    exact le_antisymm (Lp.norm_le_norm_of_ae_le (eqn.mono fun _ h => h.le))
      (Lp.norm_le_norm_of_ae_le (eqn.mono fun _ h => h.ge))
  have hc : ‖Kernel.operator l hl f‖ ≤ ‖(C : ℂ) • T g‖ := by
    apply Lp.norm_le_norm_of_ae_le
    filter_upwards [Kernel.operator_apply hl f,Kernel.operator_apply hkc g,Lp.coeFn_smul (C : ℂ) (T g),
      hk.norm.integrable_sq.prod_right_ae,hk.1.prodMk_left] with x h₁ h₂ h₃ h₄ h₅
    have hr : MemLp (fun y => k (x,y)) 2 μ := (memLp_two_iff_integrable_sq_norm h₅).2 h₄
    have hi : Integrable (fun y => k (x,y) * ‖f y‖) μ := hr.integrable_mul (Lp.memLp f).norm
    have hv : (T g) x = ((∫ y, k (x,y) * ‖f y‖ ∂μ : ℝ) : ℂ) := by
      rw [h₂,← integral_complex_ofReal]
      exact integral_congr_ae (ha.coeFn_toLp.mono fun y hy => by simp only [g,absf,hy,Complex.ofReal_mul])
    rw [h₁,h₃]
    change _ ≤ ‖(C : ℂ) * (T g x)‖
    rw [hv,norm_mul,Complex.norm_real,Complex.norm_real,Real.norm_eq_abs,Real.norm_eq_abs,
      abs_of_nonneg hC,abs_of_nonneg (integral_nonneg fun y => mul_nonneg (hn _) (norm_nonneg _)),← integral_const_mul]
    apply norm_integral_le_of_norm_le (hi.const_mul C)
    filter_upwards with y
    rw [norm_mul,← mul_assoc]
    exact mul_le_mul_of_nonneg_right (hb _) (norm_nonneg _)
  calc
    _ ≤ _ := hc
    _ = C * ‖T g‖ := by rw [norm_smul,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hC]
    _ ≤ C * (‖T‖ * ‖g‖) := mul_le_mul_of_nonneg_left (T.le_opNorm _) hC
    _ = _ := by rw [hnorm,mul_assoc]

/-- Insert any bounded continuous function of the two spatial boundaries and
the intervening temporal bonds into the symmetric one-step kernel. -/
def rectTestEntry (n : spatialAxis → ℕ) (β : ℝ) (m : Flux)
    (F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) (z : RectSlice n × RectSlice n) : ℂ :=
  ((rectHalfWeight n β m z.1 * rectHalfWeight n β m z.2 : ℝ) : ℂ) *
    ∫ g, F (z,g) * (rectTemporal n β (z.1,rectGauge n (z.2,g)) : ℝ) ∂rectGaugeHaar n

theorem rectTestEntry_continuous (n : spatialAxis → ℕ) (β : ℝ) (m : Flux)
    (F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) : Continuous (rectTestEntry n β m F) := by
  let a := rectGauge n
  let q := rectTemporal n β
  have h : Continuous (fun w : (RectSlice n × RectSlice n) × RectGauges n =>
      F w * (q (w.1.1,a (w.1.2,w.2)) : ℂ)) := by fun_prop
  have hi : Continuous (fun z : RectSlice n × RectSlice n => ∫ g, F (z,g) * (q (z.1,a (z.2,g)) : ℂ) ∂rectGaugeHaar n) := by
    simpa using continuous_parametric_integral_of_continuous (μ := rectGaugeHaar n)
      (f := fun z g => F (z,g) * (q (z.1,a (z.2,g)) : ℂ)) h (isCompact_univ : IsCompact (Set.univ : Set (RectGauges n)))
  exact (Complex.continuous_ofReal.comp (((rectHalfWeight n β m).continuous.comp continuous_fst).mul
    ((rectHalfWeight n β m).continuous.comp continuous_snd))).mul hi

theorem rectTestEntry_bound (n : spatialAxis → ℕ) (β : ℝ) (m : Flux)
    (F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) (z : RectSlice n × RectSlice n) :
    ‖rectTestEntry n β m F z‖ ≤ ‖F‖ * rectSymKernel n β m z := by
  let w := rectHalfWeight n β m z.1 * rectHalfWeight n β m z.2
  have hw : 0 ≤ w := mul_nonneg (Real.exp_pos _).le (Real.exp_pos _).le
  let q (g) := rectTemporal n β (z.1,rectGauge n (z.2,g))
  have hn (g) : 0 ≤ q g := (Real.exp_pos _).le
  have hc : Continuous q := by unfold q; fun_prop
  have hi := hc.integrable_of_hasCompactSupport (μ := rectGaugeHaar n) (HasCompactSupport.of_compactSpace _)
  change ‖(w : ℂ) * ∫ g, F (z,g) * (q g : ℂ) ∂rectGaugeHaar n‖ ≤ _
  rw [norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hw,rectSymKernel_apply]
  change w * _ ≤ ‖F‖ * (w * ∫ g, q g ∂rectGaugeHaar n)
  rw [mul_left_comm,← integral_const_mul]
  apply mul_le_mul_of_nonneg_left _ hw
  apply norm_integral_le_of_norm_le (hi.const_mul ‖F‖)
  filter_upwards with g
  simp only [norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg (hn g)]
  exact mul_le_mul_of_nonneg_right (F.norm_coe_le_norm _) (hn g)

theorem rectTestEntry_memLp (n : spatialAxis → ℕ) (β : ℝ) (m : Flux)
    (F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) :
    MemLp (rectTestEntry n β m F) 2 ((rectHaar n).prod (rectHaar n)) :=
  (rectTestEntry_continuous n β m F).memLp_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)

theorem rectTestOperator_bound (n : spatialAxis → ℕ) (β : ℝ) (m : Flux)
    (F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) :
    ‖Kernel.operator _ (rectTestEntry_memLp n β m F)‖ ≤ ‖F‖ * ‖rectSymOperator n β m‖ := by
  rw [rectSymOperator_eq]
  apply kernel_norm_domination ((rectSymKernel n β m).continuous.memLp_of_hasCompactSupport (HasCompactSupport.of_compactSpace _))
    (rectSymEntry_memLp n β m) (rectTestEntry_memLp n β m F) (norm_nonneg F) _ (rectTestEntry_bound n β m F)
  rintro ⟨u,v⟩
  rw [rectSymKernel_apply]
  exact mul_nonneg (mul_nonneg (Real.exp_pos _).le (Real.exp_pos _).le) (integral_nonneg fun _ => (Real.exp_pos _).le)


/-- The operator of the seam kernel equals the ordinary layer followed by the
electric translation on the same rectangular Hilbert space. -/
theorem rectOperator_insert (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) :
    rectOperator n β m e = rectOperator n β m zeroFlux * rectTranslation n e := by
  let μ := rectHaar n
  let C := rectTranslation n e
  let k := rectSeamKernel n β m zeroFlux
  apply ContinuousLinearMap.ext
  intro f
  apply Lp.ext
  have hC := Lp.coeFn_compMeasurePreserving f (rectFlip_preserving n e)
  filter_upwards [Kernel.operator_apply (rectSeamKernel_memLp n β m e) f,
    Kernel.operator_apply (rectSeamKernel_memLp n β m zeroFlux) (C f)] with x hx hy
  change (rectOperator n β m e f) x = (rectOperator n β m zeroFlux (C f)) x
  unfold rectOperator
  rw [hx, hy]
  calc
    _ = ∫ y, k (x,y) * f (rectFlip e y) ∂μ := by
      rw [← (rectFlip_preserving n e).integral_comp' (fun y => k (x,y) * f (rectFlip e y))]
      exact integral_congr_ae (ae_of_all _ fun y => by
        change rectSeamKernel n β m e (x,y) * f y = k (x,rectFlip e y) * f (rectFlip e (rectFlip e y))
        simp only [k, rectSeamKernel, rectFlip_zero, rectFlip_involution])
    _ = _ := integral_congr_ae (hC.mono fun y hy' => congrArg (k (x,y) * ·) hy'.symm)


/-- Move a distinguished edge from time zero to the closing edge in the
Hilbert–Schmidt cyclic trace formula. No invariance of the two kernels is required. -/
theorem integral_seamZero {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsProbabilityMeasure μ]
    (k l : X × X → ℂ) (n : ℕ) :
    (∫ u, ∏ t : Fin (n+2), if t.val = 0 then l (u t,u (finRotate _ t)) else k (u t,u (finRotate _ t))
      ∂Kernel.copies μ (n+2)) = ∫ u, Kernel.loopProduct k l n u ∂Kernel.copies μ (n+2) := by
  let R := finRotate (n+2)
  let E := MeasurableEquiv.piCongrLeft (fun _ => X) R.symm
  have hw : MeasurePreserving E (Kernel.copies μ (n+2)) (Kernel.copies μ (n+2)) :=
    measurePreserving_piCongrLeft (fun _ => μ) R.symm
  rw [← hw.integral_comp' (Kernel.loopProduct k l n)]
  apply integral_congr_ae
  filter_upwards with u
  have read (i : Fin (n+2)) : E u i = u (R i) := by
    have h := MeasurableEquiv.piCongrLeft_apply_apply R.symm (β := fun _ => X) u (R i)
    simpa only [Equiv.symm_apply_apply] using h
  let q (t : Fin (n+2)) := if t.val = 0 then l (u t,u (R t)) else k (u t,u (R t))
  have edges (i : Fin (n+1)) : k (E u i.castSucc,E u i.succ) = q i.succ := by
    rw [read,read,show R i.castSucc = i.succ from finRotate_of_lt i.isLt]
    simp [q]
  have closing : l (E u (Fin.last _),E u 0) = q 0 := by
    rw [read, read, show R (Fin.last _) = 0 from finRotate_last]
    simp only [q, Fin.val_zero, if_true]
  change (∏ t, q t) = (∏ i : Fin (n+1), k (E u i.castSucc, E u i.succ)) * l _
  rw [closing, Fin.prod_univ_succ q]
  simpa only [edges] using mul_comm (q 0) (∏ i : Fin (n+1), q i.succ)

/-- Actual rectangular trace with a single electric seam. The same operator
is used for every ordinary step and in every power at these spatial periods. -/
theorem rectInsertedTrace (s : Sides) {n : ℕ} (ha : s μt = n+2) (β : ℝ) (e m : Flux)
    {ι : Type*} (b : HilbertBasis ι ℂ (Kernel.Space (rectHaar (rectShape s)))) :
    HasSum (fun i => (⟪b i, (rectOperator (rectShape s) β m e *
      rectOperator (rectShape s) β m zeroFlux ^ (n+1)) (b i)⟫_ℂ).re)
      (twistedPartition β s (joinTwist e m)) := by
  let N := rectShape s
  let k := rectSeamKernel N β m zeroFlux
  let l := rectSeamKernel N β m e
  have ht := Kernel.hasSum_loopProduct b n (rectSeamKernel_memLp N β m zeroFlux) (rectSeamKernel_memLp N β m e)
  change HasSum _ (∫ u, Kernel.loopProduct k l n u ∂Kernel.copies (rectHaar N) (n+2)) at ht
  rw [← integral_seamZero (rectHaar N) k l n] at ht
  have hscalar : (∫ u, ∏ t : Fin (n+2), if t.val = 0 then l (u t,u (finRotate _ t))
      else k (u t,u (finRotate _ t)) ∂Kernel.copies (rectHaar N) (n+2)) =
      (twistedPartition β s (joinTwist e m) : ℂ) := by
    rw [twistedPartition_eq_rectCycle s (by omega) β e m,ha]
    rw [← integral_complex_ofReal]
    apply integral_congr_ae
    filter_upwards with u
    rw [Complex.ofReal_prod]
    apply Finset.prod_congr rfl
    intro t _
    by_cases h : t.val = 0 <;> simp only [h, if_true, if_false, k, l, rectSeamKernel, rectFlip_zero, N]
  rw [hscalar] at ht
  exact ht.mapL Complex.reCLM


def rectElectricEntry (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) (z : RectSlice n × RectSlice n) : ℂ :=
  rectSymEntry n β m (z.1,rectFlip e z.2)

theorem rectElectricEntry_operator (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) :
    Kernel.operator (rectElectricEntry n β m e) (rectSymSeam_memLp n β m e) =
      rectSymOperator n β m * rectTranslation n e :=
  (rectRight_insert n e (rectSymEntry n β m) (rectSymEntry_memLp n β m) (rectSymSeam_memLp n β m e)).trans
    (congrArg (· * rectTranslation n e) (rectSymOperator_eq n β m).symm)

theorem rectElectricEntry_product (n : spatialAxis → ℕ) (β : ℝ) (m e : Flux) (p : ℕ) :
    Kernel.operator (rectElectricEntry n β m e) (rectSymSeam_memLp n β m e) *
      Kernel.operator (rectSymEntry n β m) (rectSymEntry_memLp n β m) ^ (p+1) =
      rectSymOperator n β m ^ (p+2) * rectTranslation n e := by
  let T := rectSymOperator n β m
  let C := rectTranslation n e
  have hc : Commute T C := rectSymOperator_commutes n β m e
  have h : T * C * T ^ (p+1) = T ^ (p+2) * C := by
    calc
      _ = T * (C * T ^ (p+1)) := mul_assoc _ _ _
      _ = T * (T ^ (p+1) * C) := congrArg (T * ·) (hc.pow_left _).eq.symm
      _ = (T * T ^ (p+1)) * C := (mul_assoc _ _ _).symm
      _ = _ := congrArg (· * C) (pow_succ' T (p+1)).symm
  exact (congrArg₂ (· * ·) (rectElectricEntry_operator n β m e)
    (congrArg (· ^ (p+1)) (rectSymOperator_eq n β m).symm)).trans h

theorem rectSymLoop_partition (s : Sides) {p : ℕ} (ha : s μt = p+2) (β : ℝ) (e m : Flux) :
    (∫ u, Kernel.loopProduct (rectSymEntry (rectShape s) β m) (rectElectricEntry (rectShape s) β m e) p u
      ∂Kernel.copies (rectHaar (rectShape s)) (p+2)) = (twistedPartition β s (joinTwist e m) : ℂ) := by
  rw [← integral_seamZero,twistedPartition_eq_symCycle s (by omega) β e m,ha,← integral_complex_ofReal]
  apply integral_congr_ae
  filter_upwards with u
  rw [Complex.ofReal_prod]
  apply Finset.prod_congr rfl
  intro t _
  by_cases h : t.val = 0 <;> simp only [h,if_true,if_false,rectElectricEntry,rectSymEntry]

/-- Closing the actual symmetric rectangle with an electric translation gives
the signed Wilson partition function in every Hilbert basis. -/
theorem rectSymTrace {s : Sides} (ha : 2 ≤ s μt) (β : ℝ) (e m : Flux)
    {ι : Type*} (b : HilbertBasis ι ℂ (Kernel.Space (rectHaar (rectShape s)))) :
    HasSum (fun i => ⟪b i, (rectSymOperator (rectShape s) β m ^ (s μt) * rectTranslation (rectShape s) e) (b i)⟫_ℂ)
      (twistedPartition β s (joinTwist e m) : ℂ) := by
  obtain ⟨p,hp⟩ : ∃ p : ℕ, s μt = p+2 := ⟨s μt - 2, by omega⟩
  let n := rectShape s
  have h := Kernel.hasSum_loopProduct (k := rectSymEntry n β m) (l := rectElectricEntry n β m e)
    b p (rectSymEntry_memLp n β m) (rectSymSeam_memLp n β m e)
  rw [rectElectricEntry_product,rectSymLoop_partition s hp] at h
  rw [hp]
  exact h


/-- Fourier projection of the electric insertion produces the positive
operator whose powers represent this exact rectangular sector. -/
theorem rectSectorTrace {s : Sides} (ha : 2 ≤ s μt) (β : ℝ) (χ m : Flux)
    {ι : Type*} (b : HilbertBasis ι ℂ (Kernel.Space (rectHaar (rectShape s)))) :
    HasSum (fun i => (⟪b i, (rectSector (rectShape s) β χ m ^ (s μt)) (b i)⟫_ℂ).re)
      (sectorWeight β s χ m) := by
  let n := rectShape s
  let a := s μt
  let T := rectSymOperator n β m
  let P := rectProj n χ
  let C := rectTranslation n
  have hc : Commute T P := rectSymOperator_commutes_proj n β m χ
  have hi : IsIdempotentElem P := rectProj_idempotent n χ
  have pow : rectSector n β χ m ^ a = T ^ a * P := (hc.mul_pow a).trans (congrArg (T ^ a * ·) (hi.pow_eq (by omega : a ≠ 0)))
  have entry (i : ι) : (⟪b i, (T ^ a * P) (b i)⟫_ℂ).re =
      (∑ e : Flux, (character e χ : ℝ) * (⟪b i, (T ^ a * C e) (b i)⟫_ℂ).re) / 8 := by
    change (⟪b i, (T ^ a * ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • C e)) (b i)⟫_ℂ).re = _
    rw [mul_smul_comm, Finset.mul_sum]
    simp only [mul_smul_comm, ContinuousLinearMap.smul_apply, ContinuousLinearMap.sum_apply, inner_smul_right, inner_sum]
    norm_num [Complex.mul_re, Complex.re_sum, Complex.im_sum, div_eq_mul_inv]
    <;> ring
  change HasSum (fun i => (⟪b i, (rectSector n β χ m ^ a) (b i)⟫_ℂ).re) _
  rw [pow]
  simp_rw [entry]
  have ht (e : Flux) : HasSum (fun i => ⟪b i, (T ^ a * C e) (b i)⟫_ℂ)
      (twistedPartition β s (joinTwist e m) : ℂ) := rectSymTrace ha β e m b
  exact (hasSum_sum (s := Finset.univ) (fun (e : Flux) _ => ((ht e).mapL Complex.reCLM).mul_left
    (character e χ : ℝ))).div_const 8

theorem rectSector_compact (n : spatialAxis → ℕ) (β : ℝ) (χ m : Flux) :
    IsCompactOperator (rectSector n β χ m) := by
  have h := (Kernel.operator_compact (rectSymEntry_memLp n β m)).comp_clm (rectProj n χ)
  exact h

/-- Every positive eigenvalue is counted with its eigenspace multiplicity.
The temporal length may vary while the operator and its slots remain fixed. -/
theorem rectSector_moments {s : Sides} (ha : 2 ≤ s μt) {β : ℝ} (hβ : 0 ≤ β) (χ m : Flux) :
    HasSum (fun i : Wilson.PositiveSlot (rectSector (rectShape s) β χ m) => i.1.val ^ (s μt))
      (sectorWeight β s χ m) := by
  classical
  let T := rectSector (rectShape s) β χ m
  obtain ⟨w,b,j,hj,he,h₀⟩ := exists_positive_slot_basis T (rectSector_compact _ _ _ _) (rectSector_positive _ hβ _ _)
  obtain ⟨a,ha'⟩ : ∃ a : ℕ, s μt = a+1 := ⟨s μt - 1,by omega⟩
  have ht := rectSectorTrace ha β χ m b
  change HasSum (fun p => (⟪b p,(T ^ (s μt)) (b p)⟫_ℂ).re) _ at ht
  have out (p : w) (hp : p ∉ Set.range j) : (⟪b p,(T ^ (s μt)) (b p)⟫_ℂ).re = 0 := by
    rw [ha',pow_succ,ContinuousLinearMap.mul_apply,h₀ p hp,map_zero,inner_zero_right,Complex.zero_re]
  have hs := (hj.hasSum_iff out).2 ht
  apply hs.congr_fun
  intro i
  change i.1.val ^ (s μt) = (⟪b (j i), (T ^ (s μt)) (b (j i))⟫_ℂ).re
  rw [pow_apply_eigenvector T (he i),inner_smul_right,inner_self_eq_one_of_norm_eq_one (b.orthonormal.norm_eq_one _),
    mul_one, ← Complex.ofReal_pow, Complex.ofReal_re]

theorem sectorWeight_nonneg {s : Sides} (ha : 2 ≤ s μt) {β : ℝ} (hβ : 0 ≤ β) (χ m : Flux) :
    0 ≤ sectorWeight β s χ m :=
  hasSum_le (fun i => pow_nonneg i.1.property.le _) hasSum_zero (rectSector_moments ha hβ χ m)


end RectangularKernel



section CubicKernel

open InfiniteLattice Matrices SpinHarmonics
local notation "μt" => TimeAxis.timeIdx

variable (Γ : CubicPeriodSublattice)

/-- Reduction modulo the spatial period carries a lattice step into the cyclic
successor even when it wraps from the last site to zero. -/
theorem zmod_val_rotate {N : ℕ} [NeZero N] (z : ZMod N) :
    (z+1).val = (finRotate N ⟨z.val,ZMod.val_lt z⟩).val := by
  cases N with
  | zero => exact (NeZero.ne 0 rfl).elim
  | succ n => rw [finRotate_succ_apply]; rfl

theorem spatialCode_shift (y : SliceSite μt) (i : spatialAxis) :
    spatialCode Γ (y.shift i.val i.property) = rectStep (spatialCode Γ y) i := by
  funext j
  apply Fin.ext
  have step : level j.val (axisStep 1 i.val) = if j.val = i.val then 1 else 0 := by
    simpa using SliceProduct.level_zsmul_axisStep (μ := i.val) j.val 1
  by_cases h : j = i
  · subst j
    change (((level i.val (y.val + axisStep 1 i.val) : ℤ) : ZMod Γ.side).val) = _
    simp only [SliceDecomposition.level_add,step,if_true,Int.cast_add,Int.cast_one,rectStep]
    exact zmod_val_rotate _
  · have h' : j.val ≠ i.val := fun h' => h (Subtype.ext h')
    change (((level j.val (y.val + axisStep 1 i.val) : ℤ) : ZMod Γ.side).val) = _
    simp only [SliceDecomposition.level_add,step,if_neg h',add_zero,rectStep,if_neg h]; rfl

theorem vertexFromCode_class (y : SliceSite μt) : vertexFromCode Γ (spatialCode Γ y) = Γ.vertexClass y :=
  Subtype.ext (Γ.vertexOrbit_eq_of_sub_mem (slicePeriods_of_spatialCode Γ (spatialCode_siteOfCode Γ _)))

theorem linkFromCode_class (y : SliceSite μt) (i : spatialAxis) :
    linkFromCode Γ (spatialCode Γ y,i) = Γ.linkClass (SliceLink.ofAxis y i.val i.property) :=
  linkClass_eq_of_code Γ (spatialCode_siteOfCode Γ _) ((sliceLink_ofAxis_axis _ i).trans (sliceLink_ofAxis_axis _ i).symm)

def releaseFacePlane (p : SlicePlaquette μt) : RectSpatialPlane :=
  ⟨⟨(p.val.lowAxis,p.val.highAxis),p.val.lowAxis_lt_highAxis⟩,p.highAxis_ne⟩

def faceOfCode (c : sliceCode Γ.side) (p : RectSpatialPlane) : SlicePlaquette μt :=
  ⟨⟨(siteOfCode c).val,p.val.val.1,p.val.val.2,p.val.property⟩, by
    intro q hq
    simp only [ElementaryPlaquette.cornerSet,Set.mem_insert_iff,Set.mem_singleton_iff] at hq
    rcases hq with rfl|rfl|rfl|rfl
    · exact (siteOfCode c).property
    · exact add_axisStep_mem_sliceLattice (siteOfCode c).property (firstSpatial p.val).property
    · exact add_axisStep_mem_sliceLattice (add_axisStep_mem_sliceLattice (siteOfCode c).property
        (firstSpatial p.val).property) p.property
    · exact add_axisStep_mem_sliceLattice (siteOfCode c).property p.property⟩

def releaseFaceLabel (q : Γ.FaceOrbits μt) : sliceCode Γ.side × RectSpatialPlane :=
  let p := CubicPeriodSublattice.faceRep q
  (spatialCode Γ p.origin,releaseFacePlane p)

theorem releaseFaceLabel_class (p : SlicePlaquette μt) :
    releaseFaceLabel Γ (Γ.faceClass p) = (spatialCode Γ p.origin,releaseFacePlane p) := by
  let q := CubicPeriodSublattice.faceRep (Γ.faceClass p)
  have hm : p ∈ Γ.faceOrbit μt q := by
    rw [show Γ.faceOrbit μt q = Γ.faceOrbit μt p from (Γ.faceClass p).property.choose_spec]
    exact SliceProduct.self_mem_faceOrbit p
  obtain ⟨γ,hγ,hp⟩ := hm
  exact Prod.ext (spatialCode_of_translate Γ hγ (congrArg ElementaryPlaquette.corner hp)).symm
    (Subtype.ext (Subtype.ext (Prod.ext (congrArg ElementaryPlaquette.lowAxis hp).symm
      (congrArg ElementaryPlaquette.highAxis hp).symm)))

theorem faceClass_eq_of_code {p q : SlicePlaquette μt} (hs : spatialCode Γ p.origin = spatialCode Γ q.origin)
    (hd : releaseFacePlane p = releaseFacePlane q) : Γ.faceClass p = Γ.faceClass q := by
  apply Subtype.ext
  apply Γ.faceOrbit_eq_of_mem
  refine ⟨p.val.corner-q.val.corner,slicePeriods_of_spatialCode Γ hs.symm,ElementaryPlaquette.ext ?_
    (congrArg (fun d : RectSpatialPlane => d.val.val.1) hd) (congrArg (fun d : RectSpatialPlane => d.val.val.2) hd)⟩
  change p.val.corner = q.val.corner + (p.val.corner-q.val.corner)
  abel

def faceFromCode : (sliceCode Γ.side × RectSpatialPlane) ≃ Γ.FaceOrbits μt where
  toFun a := Γ.faceClass (faceOfCode Γ a.1 a.2)
  invFun := releaseFaceLabel Γ
  left_inv a := (releaseFaceLabel_class Γ _).trans (Prod.ext (spatialCode_siteOfCode Γ _) rfl)
  right_inv q := by
    let p := CubicPeriodSublattice.faceRep q
    change Γ.faceClass (faceOfCode Γ (spatialCode Γ p.origin) (releaseFacePlane p)) = q
    exact (faceClass_eq_of_code Γ (p := faceOfCode Γ (spatialCode Γ p.origin) (releaseFacePlane p)) (q := p) (spatialCode_siteOfCode Γ _) rfl).trans (Subtype.ext q.property.choose_spec)

def readLinks (u : Γ.LinkOrbits μt → Wilson.SU2) : RectSlice (fun _ => Γ.side) :=
  fun b => u (linkFromCode Γ b)

theorem readLinks_holonomy (p : SlicePlaquette μt) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    let x := spatialCode Γ p.origin
    let i : spatialAxis := ⟨p.val.lowAxis,p.lowAxis_ne⟩
    let j : spatialAxis := ⟨p.val.highAxis,p.highAxis_ne⟩
    Γ.holonomyOfFamily p u = readLinks Γ u (x,i) * readLinks Γ u (rectStep x i,j) *
      (readLinks Γ u (rectStep x j,i))⁻¹ * (readLinks Γ u (x,j))⁻¹ := by
  dsimp only
  let i : spatialAxis := ⟨p.val.lowAxis,p.lowAxis_ne⟩
  let j : spatialAxis := ⟨p.val.highAxis,p.highAxis_ne⟩
  unfold readLinks
  rw [← spatialCode_shift Γ p.origin i, ← spatialCode_shift Γ p.origin j]
  simp only [linkFromCode_class]
  rfl

theorem codeResidue_zero (p : SlicePlaquette μt) (i : spatialAxis) :
    Γ.coordResidues p.val.corner i.val = 0 ↔ (spatialCode Γ p.origin i).val = 0 :=
  (ZMod.val_eq_zero _).symm

theorem magneticFace_readCode (m : Flux) (q : Γ.FaceOrbits μt) :
    let p := CubicPeriodSublattice.faceRep q
    let i : spatialAxis := ⟨p.val.lowAxis,p.lowAxis_ne⟩
    let j : spatialAxis := ⟨p.val.highAxis,p.highAxis_ne⟩
    magneticFace Γ m q = decide (joinTwist zeroFlux m (releaseFacePlane p).val = true ∧
      (spatialCode Γ p.origin i).val = 0 ∧ (spatialCode Γ p.origin j).val = 0) := by
  let p := CubicPeriodSublattice.faceRep q
  let i : spatialAxis := ⟨p.val.lowAxis,p.lowAxis_ne⟩
  let j : spatialAxis := ⟨p.val.highAxis,p.highAxis_ne⟩
  let b := joinTwist zeroFlux m (releaseFacePlane p).val
  have hd := Bool.decide_congr ((codeResidue_zero Γ p i).and (codeResidue_zero Γ p j))
  change (b && decide (Γ.coordResidues p.val.corner i.val = 0 ∧ Γ.coordResidues p.val.corner j.val = 0)) =
    decide (b = true ∧ (spatialCode Γ p.origin i).val = 0 ∧ (spatialCode Γ p.origin j).val = 0)
  rw [hd]
  cases b <;> simp

theorem halfTrace_magneticHolonomy (m : Flux) (q : Γ.FaceOrbits μt) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    halfTrace (magneticHolonomy Γ m q u) = bitSign (magneticFace Γ m q) * halfTrace (Γ.orbitHolonomy q u) := by
  unfold magneticHolonomy
  cases h : magneticFace Γ m q <;> simp [bitSign,Wilson.halfTrace_centerMinus]

theorem rectFaceTerm_readCode (m : Flux) (q : Γ.FaceOrbits μt) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    1 - halfTrace (magneticHolonomy Γ m q u) =
      rectFaceTerm m (readLinks Γ u) (readLinks Γ u) (fun _ => 1) ((releaseFaceLabel Γ q).1)
        ((releaseFaceLabel Γ q).2).val := by
  let p := CubicPeriodSublattice.faceRep q
  let i : spatialAxis := ⟨p.val.lowAxis,p.lowAxis_ne⟩
  let j : spatialAxis := ⟨p.val.highAxis,p.highAxis_ne⟩
  let d := (releaseFacePlane p).val
  let x := spatialCode Γ p.origin
  let U := readLinks Γ u
  let w := U (x,i) * U (rectStep x i,j) * (U (rectStep x j,i))⁻¹ * (U (x,j))⁻¹
  have hw : Γ.orbitHolonomy q u = w := readLinks_holonomy Γ p u
  have hb : magneticFace Γ m q = decide (joinTwist zeroFlux m d = true ∧ (x i).val = 0 ∧ (x j).val = 0) :=
    magneticFace_readCode Γ m q
  rw [halfTrace_magneticHolonomy,hw,hb]
  change 1 - _ * halfTrace w = rectFaceTerm m U U (fun _ => 1) x d
  unfold rectFaceTerm
  rw [dif_neg (releaseFacePlane p).property]
  rfl

theorem magneticEnergy_readLinks (β : ℝ) (m : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    magneticEnergy Γ β m u = β * rectSpatialAction m (readLinks Γ u) := by
  classical
  letI : Fintype (Γ.FaceOrbits μt) := Fintype.ofFinite _
  let U := readLinks Γ u
  let f (b : sliceCode Γ.side × RectSpatialPlane) := rectFaceTerm m U U (fun _ => 1) b.1 b.2.val
  change β * ∑ q, (1 - halfTrace (magneticHolonomy Γ m q u)) = _
  apply congrArg (β * ·)
  change (∑ q, _) = ∑ x, ∑ p : RectSpatialPlane, f (x,p)
  rw [← Fintype.sum_prod_type, ← (faceFromCode Γ).symm.sum_comp f]
  exact Finset.sum_congr rfl fun q _ => rectFaceTerm_readCode Γ m q u


def readVertices (g : Γ.VertexOrbits μt → Wilson.SU2) : RectGauges (fun _ => Γ.side) :=
  fun x => g (vertexFromCode Γ x)

def linkCoordinates : (Γ.LinkOrbits μt → Wilson.SU2) ≃ᵐ RectSlice (fun _ => Γ.side) :=
  MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) (linkFromCode Γ).symm

def gaugeCoordinates : (Γ.VertexOrbits μt → Wilson.SU2) ≃ᵐ RectGauges (fun _ => Γ.side) :=
  MeasurableEquiv.piCongrLeft (fun _ => Wilson.SU2) (vertexFromCode Γ).symm

theorem linkCoordinates_apply (u : Γ.LinkOrbits μt → Wilson.SU2) : linkCoordinates Γ u = readLinks Γ u := by
  funext b
  have h := MeasurableEquiv.piCongrLeft_apply_apply (linkFromCode Γ).symm (β := fun _ => Wilson.SU2) u (linkFromCode Γ b)
  simpa only [linkCoordinates,readLinks,Equiv.symm_apply_apply] using h

theorem gaugeCoordinates_apply (g : Γ.VertexOrbits μt → Wilson.SU2) : gaugeCoordinates Γ g = readVertices Γ g := by
  funext x
  have h := MeasurableEquiv.piCongrLeft_apply_apply (vertexFromCode Γ).symm (β := fun _ => Wilson.SU2) g (vertexFromCode Γ x)
  simpa only [gaugeCoordinates,readVertices,Equiv.symm_apply_apply] using h

theorem linkCoordinates_preserving : MeasurePreserving (linkCoordinates Γ) (ComplexMatrix2.haarPi (Γ.LinkOrbits μt))
    (rectHaar (fun _ => Γ.side)) := by
  classical
  letI := Fintype.ofFinite (Γ.LinkOrbits μt)
  rw [ComplexMatrix2.haarPi,Measure.infinitePi_eq_pi]
  exact measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) (linkFromCode Γ).symm

theorem gaugeCoordinates_preserving : MeasurePreserving (gaugeCoordinates Γ) (ComplexMatrix2.haarPi (Γ.VertexOrbits μt))
    (rectGaugeHaar (fun _ => Γ.side)) := by
  classical
  letI := Fintype.ofFinite (Γ.VertexOrbits μt)
  rw [ComplexMatrix2.haarPi,Measure.infinitePi_eq_pi]
  exact measurePreserving_piCongrLeft (fun _ => Wilson.linkHaar) (vertexFromCode Γ).symm

theorem readLinks_gaugeAct (g : Γ.VertexOrbits μt → Wilson.SU2) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    readLinks Γ (Γ.orbitGaugeAct g u) = rectGauge (fun _ => Γ.side) (readLinks Γ u,readVertices Γ g) := by
  funext b
  obtain ⟨x,i⟩ := b
  let y := siteOfCode x
  let l := SliceLink.ofAxis y i.val i.property
  have ht : vertexFromCode Γ (rectStep x i) = Γ.vertexClass (y.shift i.val i.property) := by
    calc
      _ = vertexFromCode Γ (rectStep (spatialCode Γ y) i) := by rw [spatialCode_siteOfCode]
      _ = _ := by rw [← spatialCode_shift,vertexFromCode_class]
  change Γ.orbitGaugeAct g u (Γ.linkClass l) = g (Γ.vertexClass y) * u (Γ.linkClass l) * (g (vertexFromCode Γ (rectStep x i)))⁻¹
  rw [Γ.orbitGaugeAct_linkClass,ht]
  rfl

theorem readLinks_electric (e : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    readLinks Γ (centreShift Γ μt (cuts e) u) = rectFlip e (readLinks Γ u) := by
  funext b
  let s := cubeGrid Γ.side 2
  let t : Fin (s μt) := ⟨0,by simp [s,cubeGrid]⟩
  let l := (gridLevelLabel Γ.side 2 t).symm b
  have hw := releaseLayer_flip Γ 2 t e u l
  have hL : releaseLayer Γ 2 t l = linkFromCode Γ b := congrArg (linkFromCode Γ) ((gridLevelLabel Γ.side 2 t).apply_symm_apply b)
  have hx : (l.val.val.1 l.val.val.2).val = (b.1 b.2).val := by
    change ((gridLevelLabel Γ.side 2 t l).1 (gridLevelLabel Γ.side 2 t l).2).val = _
    rw [Equiv.apply_symm_apply]
  change centreShift Γ μt (cuts e) u (linkFromCode Γ b) = linkCentre _ * u (linkFromCode Γ b)
  rw [← hL, ← hw]
  change linkCentre (decide (fluxBit e l.val.val.2 = true ∧ (l.val.val.1 l.val.val.2).val = 0)) * u _ = _
  rw [hx]
  rfl

theorem singleBondWeight_real (β : ℝ) (u : Wilson.SU2) :
    singleBondWeight β u = (Real.exp (-β * (1 - halfTrace u)) : ℝ) := by
  let z := ComplexMatrix2.fullTrace (u : ComplexMatrix2)
  have him : z.im = 0 := YangMills.Construction.InfiniteLattice.SUTwoTrace.fullTrace_im u
  change Complex.exp (-(β : ℂ) * (1 - 1/2*z)) = _
  rw [Complex.ofReal_exp]
  apply congrArg Complex.exp
  change -(β : ℂ) * (1 - 1/2*z) = ((-β * (1-z.re/2) : ℝ) : ℂ)
  push_cast
  conv_lhs => rw [BoundedMultiplication.eq_ofReal_re_of_im_eq_zero him]
  ring

theorem rectTemporal_readLinks (β : ℝ) (u v : Γ.LinkOrbits μt → Wilson.SU2) :
    (rectTemporal (fun _ => Γ.side) β (readLinks Γ u,readLinks Γ v) : ℂ) = linkProductKernel β u v := by
  classical
  letI := Fintype.ofFinite (Γ.LinkOrbits μt)
  rw [linkProductKernel,finprod_eq_prod_of_fintype, ← (linkFromCode Γ).prod_comp]
  change (Real.exp (-β * ∑ b, (1 - halfTrace (v (linkFromCode Γ b) * (u (linkFromCode Γ b))⁻¹))) : ℂ) = _
  simp_rw [singleBondWeight_real]
  rw [Finset.mul_sum,Real.exp_sum,Complex.ofReal_prod]
  apply Finset.prod_congr rfl
  intro b _
  have hv := Wilson.halfTrace_inv (u (linkFromCode Γ b) * (v (linkFromCode Γ b))⁻¹)
  simpa only [mul_inv_rev,inv_inv] using congrArg (fun t : ℝ => (Real.exp (-β * (1-t)) : ℂ)) hv

theorem rectHalfWeight_readLinks (β : ℝ) (m : Flux) (u : Γ.LinkOrbits μt → Wilson.SU2) :
    (rectHalfWeight (fun _ => Γ.side) β m (readLinks Γ u) : ℂ) = magneticDensity Γ (β/2) m u := by
  unfold magneticDensity
  rw [magneticEnergy_readLinks]
  change (Real.exp _ : ℂ) = (Real.exp _ : ℂ)
  congr 2
  ring

/-- On the actual release slice, the rectangular kernel has exactly the
release magnetic half-weights, the full Wilson link kernel and the vertex gauge Haar. -/
theorem rectSymKernel_release (β : ℝ) (m : Flux) (u v : Γ.LinkOrbits μt → Wilson.SU2) :
    (rectSymKernel (fun _ => Γ.side) β m (readLinks Γ u,readLinks Γ v) : ℂ) =
      magneticDensity Γ (β/2) m u * magneticDensity Γ (β/2) m v *
        ∫ g, linkProductKernel β u (Γ.orbitGaugeAct g v) ∂ComplexMatrix2.haarPi (Γ.VertexOrbits μt) := by
  rw [rectSymKernel_apply,Complex.ofReal_mul,Complex.ofReal_mul,rectHalfWeight_readLinks,rectHalfWeight_readLinks]
  apply congrArg (magneticDensity Γ (β/2) m u * magneticDensity Γ (β/2) m v * ·)
  rw [← (gaugeCoordinates_preserving Γ).integral_comp' (fun g => rectTemporal (fun _ => Γ.side) β
    (readLinks Γ u,rectGauge (fun _ => Γ.side) (readLinks Γ v,g))), ← integral_complex_ofReal]
  apply integral_congr_ae
  filter_upwards with g
  rw [gaugeCoordinates_apply, ← readLinks_gaugeAct, rectTemporal_readLinks]


open TheStatementsProvedTogether
open scoped InnerProductSpace

/-- Move the gauge projection from an arbitrary L² input onto a continuous
kernel row. Haar invariance and the unitary gauge action justify the change of
variables before the order of integration is interchanged. -/
theorem integral_row_gaugeProjection {β : ℝ} (hβ : 0 < β)
    (F : C(Γ.LinkOrbits μt → Wilson.SU2, ℂ)) (φ : Γ.SliceL2 μt) :
    (∫ v, F v * (Γ.gaugeProjection μt φ) v ∂ComplexMatrix2.haarPi (Γ.LinkOrbits μt)) =
      ∫ v, (∫ g, F (Γ.orbitGaugeAct g v) ∂ComplexMatrix2.haarPi (Γ.VertexOrbits μt)) * φ v
        ∂ComplexMatrix2.haarPi (Γ.LinkOrbits μt) := by
  let X := Γ.LinkOrbits μt → Wilson.SU2
  let G := Γ.VertexOrbits μt → Wilson.SU2
  let μ := ComplexMatrix2.haarPi (Γ.LinkOrbits μt)
  let ν := ComplexMatrix2.haarPi (Γ.VertexOrbits μt)
  let ξ := SqrtLinkFacts.toHaarL2 (star F)
  have props := ((cubic_torus_transfer_operators β hβ).1 Γ μt).1
  haveI := CubicTorusOperators.linkOrbits_nonempty Γ μt
  have hh := ReflectionPositivityChain.periodic_gibbs_haar_transfer_kernels.2.1 (Γ.LinkOrbits μt)
  have row (ψ : Γ.SliceL2 μt) : ⟪ξ,ψ⟫_ℂ = ∫ v, F v * ψ v ∂μ :=
    TwoLevelArgument.inner_toHaarL2_star F ψ
  have key (g : G) : ⟪ξ,Γ.gaugeRep g φ⟫_ℂ = ∫ v, F (Γ.orbitGaugeAct g v) * φ v ∂μ := by
    let B := Γ.gaugeRep g φ
    have hT : MeasurePreserving (Γ.orbitGaugeAct g) μ μ :=
      TwistedActionOperators.measurePreserving_twistedConjAction hh g
    have hm := F.continuous.aestronglyMeasurable (μ := μ) |>.mul (Lp.aestronglyMeasurable B)
    rw [row]
    calc
      _ = ∫ v, F (Γ.orbitGaugeAct g v) * B (Γ.orbitGaugeAct g v) ∂μ := by
        calc
          _ = ∫ v, F v * B v ∂Measure.map (Γ.orbitGaugeAct g) μ := by rw [hT.map_eq]
          _ = _ := integral_map hT.aemeasurable (by rw [hT.map_eq]; exact hm)
      _ = _ := by
        apply integral_congr_ae
        filter_upwards [hT.quasiMeasurePreserving.ae_eq_comp (props.rep_formula g φ)] with v hv
        change B (Γ.orbitGaugeAct g v) = φ (Γ.orbitGaugeAct g⁻¹ (Γ.orbitGaugeAct g v)) at hv
        rw [hv,PairIntegralMatrixEntry.orbitGaugeAct_inv_orbitGaugeAct]
  have hA : Continuous (fun z : G × X => F (Γ.orbitGaugeAct z.1 z.2)) :=
    F.continuous.comp (by unfold CubicPeriodSublattice.orbitGaugeAct; fun_prop)
  have hi : Integrable (fun z : G × X => F (Γ.orbitGaugeAct z.1 z.2) * φ z.2) (ν.prod μ) :=
    (((Lp.memLp φ).integrable (by norm_num)).comp_snd ν).bdd_mul hA.aestronglyMeasurable
      (ae_of_all _ fun z => F.norm_coe_le_norm _)
  rw [← row, props.proj_inner]
  simp_rw [key]
  rw [integral_integral_swap (f := fun (g : G) (v : X) => F (Γ.orbitGaugeAct g v) * φ v) hi]
  exact integral_congr_ae (ae_of_all _ fun v => integral_mul_const (φ v) _)

/-- Integral kernel of the release's symmetric magnetic splitting. This acts
on every L² input and uses the very vertex Haar and link product of the release. -/
theorem symmetricMagnetic_hasKernel {β : ℝ} (hβ : 0 < β) (m : Flux) :
    Schatten.HasKernel (ComplexMatrix2.haarPi (Γ.LinkOrbits μt))
      (fun z => magneticDensity Γ (β/2) m z.1 * magneticDensity Γ (β/2) m z.2 *
        ∫ g, linkProductKernel β z.1 (Γ.orbitGaugeAct g z.2) ∂ComplexMatrix2.haarPi (Γ.VertexOrbits μt))
      (symmetricMagnetic Γ β hβ m) := by
  intro φ
  let X := Γ.LinkOrbits μt → Wilson.SU2
  let μ := ComplexMatrix2.haarPi (Γ.LinkOrbits μt)
  let ν := ComplexMatrix2.haarPi (Γ.VertexOrbits μt)
  let D := magneticDensity Γ (β/2) m
  let M := magneticMultiplier Γ (half_pos hβ) m
  let L := linkProductOperator β (Γ.LinkOrbits μt)
  let P := Γ.gaugeProjection μt
  haveI := CubicTorusOperators.linkOrbits_nonempty Γ μt
  have hc := ((cubic_torus_transfer_operators β hβ).1 Γ μt).2.2.1.link_continuous
  have hk := ((ReflectionPositivityChain.periodic_gibbs_haar_transfer_kernels.2.2.2 (Γ.LinkOrbits μt)).1 _ hc).2.1
  rw [symmetricMagnetic_kinetic Γ hβ m]
  change (fun u => (M (L (M (P φ)))) u) =ᵐ[μ] _
  filter_upwards [magneticMultiplier_formula Γ (half_pos hβ) m (L (M (P φ))),hk (M (P φ))] with u hu hl
  let F : C(X,ℂ) := ⟨fun v => linkProductKernel β u v * D v,
    (hc.comp (continuous_const.prodMk continuous_id)).mul (magneticDensity_continuous Γ (β/2) m)⟩
  change (M (L (M (P φ)))) u = ∫ v, _ * φ v ∂μ
  calc
    _ = D u * ∫ v, linkProductKernel β u v * (M (P φ)) v ∂μ := hu.trans (congrArg (D u * ·) hl)
    _ = D u * ∫ v, F v * (P φ) v ∂μ := by
      apply congrArg (D u * ·)
      apply integral_congr_ae
      filter_upwards [magneticMultiplier_formula Γ (half_pos hβ) m (P φ)] with v hv
      change _ * (M (P φ)) v = _ * D v * _
      rw [hv,mul_assoc]
    _ = D u * ∫ v, (∫ g, F (Γ.orbitGaugeAct g v) ∂ν) * φ v ∂μ :=
      congrArg (D u * ·) (integral_row_gaugeProjection Γ hβ F φ)
    _ = _ := by
      rw [← integral_const_mul]
      apply integral_congr_ae
      filter_upwards with v
      have eh (g : Γ.VertexOrbits μt → Wilson.SU2) : F (Γ.orbitGaugeAct g v) =
          linkProductKernel β u (Γ.orbitGaugeAct g v) * D v := by
        change _ * magneticDensity Γ (β/2) m (Γ.orbitGaugeAct g v) = _ * magneticDensity Γ (β/2) m v
        simp only [magneticDensity, magneticEnergy_gaugeAct Γ (half_pos hβ)]
      simp_rw [eh]
      rw [integral_mul_const]
      ring

def cubeIsometry : Kernel.Space (rectHaar (fun _ => Γ.side)) →ₗᵢ[ℂ] Γ.SliceL2 μt :=
  Lp.compMeasurePreservingₗᵢ ℂ (linkCoordinates Γ) (linkCoordinates_preserving Γ)

theorem cubeIsometry_surjective : Function.Surjective (cubeIsometry Γ) := by
  intro f
  let h := (linkCoordinates_preserving Γ).symm (linkCoordinates Γ)
  refine ⟨Lp.compMeasurePreserving (linkCoordinates Γ).symm h f,?_⟩
  apply Lp.ext
  have h₁ := Lp.coeFn_compMeasurePreserving (Lp.compMeasurePreserving (linkCoordinates Γ).symm h f)
    (linkCoordinates_preserving Γ)
  have h₂ := (linkCoordinates_preserving Γ).quasiMeasurePreserving.ae_eq_comp (Lp.coeFn_compMeasurePreserving f h)
  filter_upwards [h₁,h₂] with u hu hv
  exact hu.trans (hv.trans (congrArg (f : _ → ℂ) ((linkCoordinates Γ).symm_apply_apply u)))

theorem cubeIsometry_intertwines {β : ℝ} (hβ : 0 < β) (m : Flux)
    (f : Kernel.Space (rectHaar (fun _ => Γ.side))) :
    cubeIsometry Γ (rectSymOperator (fun _ => Γ.side) β m f) = symmetricMagnetic Γ β hβ m (cubeIsometry Γ f) := by
  let N : spatialAxis → ℕ := fun _ => Γ.side
  let T := rectSymOperator N β m
  let E := linkCoordinates Γ
  let U := cubeIsometry Γ
  have hE := linkCoordinates_preserving Γ
  have hf := Lp.coeFn_compMeasurePreserving f hE
  have ht := Kernel.operator_apply (rectSymEntry_memLp N β m) f
  have h0 := hE.quasiMeasurePreserving.ae_eq_comp ht
  apply Lp.ext
  filter_upwards [Lp.coeFn_compMeasurePreserving (T f) hE,h0,symmetricMagnetic_hasKernel Γ hβ m (U f)] with u h₁ h₂ h₃
  change (U (T f)) u = _
  refine (h₁.trans h₂).trans (Eq.trans ?_ h₃.symm)
  change (∫ v, rectSymEntry N β m (E u,v) * f v ∂rectHaar N) = ∫ v, _ * (U f) v ∂_
  rw [← hE.integral_comp' (fun v => rectSymEntry N β m (E u,v) * f v)]
  apply integral_congr_ae
  filter_upwards [hf] with v hv
  change (U f) v = f (E v) at hv
  rw [hv]
  apply congrArg (· * f (E v))
  change (rectSymKernel _ β m (linkCoordinates Γ u,linkCoordinates Γ v) : ℂ) = _
  rw [linkCoordinates_apply,linkCoordinates_apply,rectSymKernel_release]

theorem rectSymOperator_cube_norm {β : ℝ} (hβ : 0 < β) (m : Flux) :
    ‖rectSymOperator (fun _ => Γ.side) β m‖ = ‖magneticTransfer Γ hβ m‖ := by
  let U := cubeIsometry Γ
  let A := rectSymOperator (fun _ => Γ.side) β m
  let B := symmetricMagnetic Γ β hβ m
  have he (f) : U (A f) = B (U f) := cubeIsometry_intertwines Γ hβ m f
  rw [← symmetricMagnetic_norm Γ hβ m]
  apply le_antisymm
  · apply A.opNorm_le_bound (norm_nonneg B)
    intro f
    rw [← U.norm_map (A f),he,← U.norm_map f]
    exact B.le_opNorm _
  · apply B.opNorm_le_bound (norm_nonneg A)
    intro g
    obtain ⟨f,rfl⟩ := cubeIsometry_surjective Γ g
    rw [← he,U.norm_map,U.norm_map]
    exact A.le_opNorm _


theorem cubeIsometry_electric (e : Flux) (f : Kernel.Space (rectHaar (fun _ => Γ.side))) :
    cubeIsometry Γ (rectTranslation (fun _ => Γ.side) e f) =
      electricTranslation Γ e (cubeIsometry Γ f) := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let U := cubeIsometry Γ
  let E := linkCoordinates Γ
  let F := rectFlipEquiv n e
  let G := centreShift Γ μt (cuts e)
  have hE := linkCoordinates_preserving Γ
  have hF := rectFlip_preserving n e
  have hG := centreShift_measurePreserving Γ μt (cuts e)
  apply Lp.ext
  filter_upwards [Lp.coeFn_compMeasurePreserving (rectTranslation n e f) hE,
    hE.quasiMeasurePreserving.ae_eq_comp (Lp.coeFn_compMeasurePreserving f hF),
    Lp.coeFn_compMeasurePreserving (U f) hG,
    hG.quasiMeasurePreserving.ae_eq_comp (Lp.coeFn_compMeasurePreserving f hE)] with u ha hb hc hd
  change (U (rectTranslation n e f)) u = (electricTranslation Γ e (U f)) u
  refine (ha.trans hb).trans (Eq.trans ?_ (hc.trans hd).symm)
  apply congrArg (f : _ → ℂ)
  change rectFlip e (linkCoordinates Γ u) = linkCoordinates Γ (centreShift Γ μt (cuts e) u)
  rw [linkCoordinates_apply,linkCoordinates_apply,readLinks_electric]

theorem cubeIsometry_proj (χ : Flux) (f : Kernel.Space (rectHaar (fun _ => Γ.side))) :
    cubeIsometry Γ (rectProj (fun _ => Γ.side) χ f) = electricProj Γ χ (cubeIsometry Γ f) := by
  simp only [rectProj,electricProj,characterProj,ContinuousLinearMap.smul_apply,ContinuousLinearMap.sum_apply,
    map_smul,map_sum,cubeIsometry_electric]

/-- The actual spatial relabeling and the two transfer splittings identify
every nonzero projected eigenspace, including its multiplicity. -/
theorem cube_sector_eigenspaces {β : ℝ} (hβ : 0 < β) (χ m : Flux) {z : ℂ} (hz : z ≠ 0) :
    Nonempty (Module.End.eigenspace (rectSector (fun _ => Γ.side) β χ m).toLinearMap z ≃ₗ[ℂ]
      Module.End.eigenspace (magneticTransfer Γ hβ m * electricProj Γ χ).toLinearMap z) := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let A := rectSector n β χ m
  let B := symmetricMagnetic Γ β hβ m * electricProj Γ χ
  let U := cubeIsometry Γ
  have hu (f) : U (A f) = B (U f) := by
    change U (rectSymOperator n β m (rectProj n χ f)) = symmetricMagnetic Γ β hβ m (electricProj Γ χ (U f))
    rw [show U (rectSymOperator n β m (rectProj n χ f)) = _ from cubeIsometry_intertwines Γ hβ m _,cubeIsometry_proj]
  let V : Module.End.eigenspace A.toLinearMap z →ₗ[ℂ] Module.End.eigenspace B.toLinearMap z := {
    toFun f := ⟨U f,Module.End.mem_eigenspace_iff.mpr (by
      change B (U (f : Kernel.Space (rectHaar n))) = z • U (f : Kernel.Space (rectHaar n))
      have he : A (f : Kernel.Space (rectHaar n)) = z • (f : Kernel.Space (rectHaar n)) := Module.End.mem_eigenspace_iff.mp f.property
      rw [← hu,he,map_smul])⟩
    map_add' := fun f g => Subtype.ext (map_add U _ _)
    map_smul' := fun c f => Subtype.ext (map_smul U _ _) }
  have hj : Function.Injective V := fun f g h => Subtype.ext (U.injective (congrArg Subtype.val h))
  have hs : Function.Surjective V := by
    intro g
    obtain ⟨f,hf⟩ := cubeIsometry_surjective Γ (g : Γ.SliceL2 μt)
    have hgf := Module.End.mem_eigenspace_iff.mp g.property
    change B (g : Γ.SliceL2 μt) = z • (g : Γ.SliceL2 μt) at hgf
    refine ⟨⟨f,Module.End.mem_eigenspace_iff.mpr (U.injective ?_)⟩,Subtype.ext hf⟩
    change U (A f) = U (z • f)
    rw [hu,map_smul,hf,hgf]
  exact ⟨(LinearEquiv.ofBijective V ⟨hj,hs⟩).trans (symmetricMagnetic_sector_eigenspaces Γ hβ m χ hz).some.symm⟩


open TheStatementsProvedTogether
open scoped InnerProductSpace

/-- Compactness and positivity of the actual release electric sector. The
square-root link kernel is continuous on the compact slice Haar space. -/
theorem releaseSector_spectral (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (χ m : Flux) :
    IsCompactOperator (magneticTransfer Γ hβ m * electricProj Γ χ) ∧
      (magneticTransfer Γ hβ m * electricProj Γ χ).IsPositive := by
  let I := Γ.LinkOrbits μt
  letI := CubicTorusOperators.linkOrbits_nonempty Γ μt
  let μ := ComplexMatrix2.haarPi I
  let k (z : (I → Wilson.SU2) × (I → Wilson.SU2)) := sqrtLinkKernel β z.1 z.2
  have hc : Continuous k := ((sqrt_link_kernel_facts β hβ).1 I).1.2.2
  have hk : MemLp k 2 (μ.prod μ) := hc.memLp_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)
  have hop := ((ReflectionPositivityChain.periodic_gibbs_haar_transfer_kernels.2.2.2 I).1 k hc).2.1
  have he : sqrtLinkOperator β I = Kernel.operator k hk := by
    apply ContinuousLinearMap.ext
    intro f
    apply Lp.ext
    exact (hop f).trans (Kernel.operator_apply hk f).symm
  have ch : IsCompactOperator (Γ.halfTransfer μt β) := by
    change IsCompactOperator ⇑(sqrtLinkOperator β I * Γ.gaugeProjection μt)
    rw [he]
    exact (Kernel.operator_compact hk).comp_clm _
  let T := magneticTransfer Γ hβ m
  let P := electricProj Γ χ
  refine ⟨((ch.comp_clm (magneticMultiplier Γ hβ m)).comp_clm (Γ.halfTransfer μt β)).comp_clm P,?_⟩
  have ht := magneticTransfer_positive Γ hβ m
  have pos : T.IsPositive := (ContinuousLinearMap.isPositive_iff_complex T).2 (fun x => by
    change ((⟪T x,x⟫_ℂ : ℂ).re : ℂ) = ⟪T x,x⟫_ℂ ∧ 0 ≤ (⟪T x,x⟫_ℂ : ℂ).re
    rw [← ht.1 x x]
    exact ⟨(BoundedMultiplication.eq_ofReal_re_of_im_eq_zero (ht.2 x).2).symm,(ht.2 x).1⟩)
  have hp := pos.adjoint_conj P
  have idemp : P * P = P := by simpa [P] using electricProj_mul Γ χ χ
  change (P.adjoint * (T * P)).IsPositive at hp
  have hP : P.adjoint = P := (electricProj_isSelfAdjoint Γ χ).star_eq
  have hcP : Commute T P := magneticTransfer_commutes_proj Γ hβ m χ
  rw [hP,← mul_assoc,← hcP.eq,mul_assoc,idemp] at hp
  exact hp


end CubicKernel


section InsertedCycles

open scoped InnerProductSpace
variable {X : Type*} [TopologicalSpace X] [CompactSpace X] [FirstCountableTopology X]
  [MeasurableSpace X] [BorelSpace X] [SecondCountableTopology X]
variable [T2Space X]
variable (μ : Measure X) [IsProbabilityMeasure μ]

theorem edgeMemLp (k : C(X × X,ℂ)) : MemLp k 2 (μ.prod μ) :=
  k.continuous.memLp_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)

def edgeOperator (k : C(X × X,ℂ)) := Kernel.operator _ (edgeMemLp μ k)

def edgeCompose (k l : C(X × X,ℂ)) : C(X × X,ℂ) := ⟨Kernel.compose μ k l, by
  have hc : Continuous (fun w : (X × X) × X => k (w.1.1,w.2) * l (w.2,w.1.2)) := by fun_prop
  change Continuous (fun z : X × X => ∫ y, k (z.1,y) * l (y,z.2) ∂μ)
  simpa only [Measure.restrict_univ] using continuous_parametric_integral_of_continuous (μ := μ)
    (f := fun (z : X × X) (y : X) => k (z.1,y) * l (y,z.2)) hc (isCompact_univ : IsCompact (Set.univ : Set X))⟩

theorem edgeOperator_compose (k l : C(X × X,ℂ)) :
    edgeOperator μ (edgeCompose μ k l) = edgeOperator μ k * edgeOperator μ l :=
  Kernel.operator_compose (edgeMemLp μ k) (edgeMemLp μ l)

def edgePath {n : ℕ} (k : Fin (n+1) → C(X × X,ℂ)) (u : Fin (n+2) → X) : ℂ :=
  ∏ i : Fin (n+1), k i (u i.castSucc,u i.succ)

def edgeLoop {n : ℕ} (k : Fin (n+1) → C(X × X,ℂ)) (l : C(X × X,ℂ)) (u : Fin (n+2) → X) : ℂ :=
  edgePath k u * l (u (Fin.last (n+1)),u 0)

theorem edgeLoop_cons {n : ℕ} (k : Fin (n+2) → C(X × X,ℂ)) (l : C(X × X,ℂ))
    (u : Fin (n+2) → X) (x : X) :
    edgeLoop k l (Fin.cons x u) =
      edgePath (fun i => k i.succ) u * (l (u (Fin.last (n+1)),x) * k 0 (x,u 0)) := by
  unfold edgeLoop edgePath
  rw [Fin.prod_univ_succ]
  simp only [Fin.castSucc_zero,Fin.succ_castSucc,Fin.cons_zero,Fin.cons_succ,← Fin.succ_last,Fin.cons_succ]
  ac_rfl

theorem integral_edgeLoop {n : ℕ} (k : Fin (n+2) → C(X × X,ℂ)) (l : C(X × X,ℂ)) :
    (∫ u, edgeLoop k l u ∂Kernel.copies μ (n+3)) =
      ∫ u, edgeLoop (fun i => k i.succ) (edgeCompose μ l (k 0)) u ∂Kernel.copies μ (n+2) := by
  have hp := Kernel.prepend_preserving (μ := μ) (n+2)
  have hc : Continuous (edgeLoop k l) := by unfold edgeLoop edgePath; fun_prop
  have hi := hp.integrable_comp_of_integrable (hc.integrable_of_hasCompactSupport (HasCompactSupport.of_compactSpace _))
  rw [← hp.integral_comp']
  let F (p : X × (Fin (n+2) → X)) := edgeLoop k l (Kernel.prepend (n+2) p)
  change (∫ p, F p ∂μ.prod (Kernel.copies μ (n+2))) = _
  rw [integral_prod_symm F hi]
  apply integral_congr_ae
  filter_upwards with u
  simp only [F,Kernel.prepend_apply,edgeLoop_cons,integral_const_mul]
  rfl

/-- The product is in geometric order. Every edge may carry its own bounded
continuous insertion. In particular two disjoint windows can be marked at once. -/
theorem hasSum_edgeLoop {I : Type*} (b : HilbertBasis I ℂ (Kernel.Space μ)) (n : ℕ)
    (k : Fin (n+1) → C(X × X,ℂ)) (l : C(X × X,ℂ)) :
    HasSum (fun i => ⟪b i,(edgeOperator μ l * (List.ofFn (fun t => edgeOperator μ (k t))).prod) (b i)⟫_ℂ)
      (∫ u, edgeLoop k l u ∂Kernel.copies μ (n+2)) := by
  induction n generalizing l with
  | zero =>
    have h := Kernel.hasSum_loopProduct b 0 (edgeMemLp μ (k 0)) (edgeMemLp μ l)
    have eqn (u : Fin 2 → X) : edgeLoop k l u = Kernel.loopProduct (k 0) l 0 u := by
      rw [Kernel.loopProduct_zero,edgeLoop,edgePath,Fin.prod_univ_one]
      rfl
    simp_rw [eqn]
    simpa only [edgeOperator,List.ofFn_succ,List.ofFn_zero,List.prod_cons,List.prod_nil,mul_one,Nat.zero_add,pow_one,Fin.cast_zero] using h
  | succ n ih =>
    rw [integral_edgeLoop]
    have h := ih (fun i => k i.succ) (edgeCompose μ l (k 0))
    rw [edgeOperator_compose] at h
    simpa only [List.ofFn_succ,List.prod_cons,Function.comp_def,mul_assoc] using h

theorem hasSum_markedCycle {I : Type*} (b : HilbertBasis I ℂ (Kernel.Space μ)) (n : ℕ)
    (k : Fin (n+2) → C(X × X,ℂ)) :
    HasSum (fun i => ⟪b i,(edgeOperator μ (k (Fin.last (n+1))) *
      (List.ofFn (fun t : Fin (n+1) => edgeOperator μ (k t.castSucc))).prod) (b i)⟫_ℂ)
      (∫ u, ∏ t, k t (u t,u (finRotate (n+2) t)) ∂Kernel.copies μ (n+2)) := by
  have he (u : Fin (n+2) → X) : (∏ t, k t (u t,u (finRotate (n+2) t))) =
      edgeLoop (fun i => k i.castSucc) (k (Fin.last (n+1))) u := by
    rw [Fin.prod_univ_castSucc,finRotate_last]
    unfold edgeLoop edgePath
    congr 1
    exact Finset.prod_congr rfl (fun i _ => by rw [show finRotate (n+2) i.castSucc = i.succ from finRotate_of_lt i.isLt])
  simp_rw [he]
  exact hasSum_edgeLoop μ b n _ _

end InsertedCycles


section PhysicalInsertions

local notation "μt" => TimeAxis.timeIdx

open TheStatementsProvedTogether InfiniteLattice Matrices
variable (Γ : CubicPeriodSublattice)

abbrev ReleasePairs := ZMod Γ.side → (Γ.VertexOrbits μt → Wilson.SU2) × (Γ.LinkOrbits μt → Wilson.SU2)

def orbitLinkLabel := Equiv.ofBijective (Γ.labelQuotientLink μt) (cubic_torus_slice_decomposition Γ μt).1

def fieldOfPairs (p : ReleasePairs Γ) (b : Γ.lattice.QuotientLink) : Wilson.SU2 :=
  match (orbitLinkLabel Γ).symm b with
  | .inl (c,i) => (p (c-1)).2 i
  | .inr (c,i) => (p c).1 i

theorem fieldOfPairs_spatial (p : ReleasePairs Γ) (c : ZMod Γ.side) (i : Γ.LinkOrbits μt) :
    fieldOfPairs Γ p (Γ.spatialQuotientLink c i) = (p (c-1)).2 i := by
  change fieldOfPairs Γ p (orbitLinkLabel Γ (.inl (c,i))) = _
  simp only [fieldOfPairs,Equiv.symm_apply_apply]

theorem fieldOfPairs_temporal (p : ReleasePairs Γ) (c : ZMod Γ.side) (i : Γ.VertexOrbits μt) :
    fieldOfPairs Γ p (Γ.temporalQuotientLink c i) = (p c).1 i := by
  change fieldOfPairs Γ p (orbitLinkLabel Γ (.inr (c,i))) = _
  simp only [fieldOfPairs,Equiv.symm_apply_apply]

/-- Invert the release's layer coordinates on every quotient field, including
its one-step offset between the outgoing spatial and temporal arrays. -/
def releasePairCoordinates : Γ.lattice.QuotientField ≃ᵐ ReleasePairs Γ where
  toFun := Γ.slicePairs μt
  invFun := fieldOfPairs Γ
  left_inv U := by
    funext b
    obtain ⟨(⟨c,i⟩|⟨c,i⟩),rfl⟩ := (orbitLinkLabel Γ).surjective b
    · rw [show orbitLinkLabel Γ (.inl (c,i)) = Γ.spatialQuotientLink c i from rfl,fieldOfPairs_spatial]
      simp only [CubicPeriodSublattice.slicePairs,sub_add_cancel,CubicPeriodSublattice.sliceField]
    · rw [show orbitLinkLabel Γ (.inr (c,i)) = Γ.temporalQuotientLink c i from rfl,fieldOfPairs_temporal]
      rfl
  right_inv p := by
    funext c
    apply Prod.ext
    · funext i
      exact fieldOfPairs_temporal Γ p c i
    · funext i
      change fieldOfPairs Γ p (Γ.spatialQuotientLink (c+1) i) = _
      rw [fieldOfPairs_spatial,add_sub_cancel_right]
  measurable_toFun := (cubic_torus_slice_decomposition Γ μt).2.measurable
  measurable_invFun := by
    apply measurable_pi_lambda
    intro b
    change Measurable (fun p : ReleasePairs Γ => fieldOfPairs Γ p b)
    unfold fieldOfPairs
    rcases (orbitLinkLabel Γ).symm b with ⟨c,i⟩|⟨c,i⟩
    · change Measurable (fun p : ReleasePairs Γ => (p (c-1)).2 i)
      fun_prop
    · change Measurable (fun p : ReleasePairs Γ => (p c).1 i)
      fun_prop

abbrev releasePairHaar := Measure.pi (fun _ : ZMod Γ.side =>
  (ComplexMatrix2.haarPi (Γ.VertexOrbits μt)).prod (ComplexMatrix2.haarPi (Γ.LinkOrbits μt)))

def releasePairWeight (β : ℝ) (p : ReleasePairs Γ) : ℂ :=
  ∏ c, magneticDensity Γ β zeroFlux (p (c-1)).2 *
    linkProductKernel β (p (c-1)).2 (Γ.orbitGaugeAct (p c).1 (p c).2)

theorem releasePairWeight_boltzmann {β : ℝ} (hβ : 0 < β) (U : Γ.lattice.QuotientField) :
    releasePairWeight Γ β (releasePairCoordinates Γ U) = (Γ.lattice.boltzmannWeight β U : ℂ) := by
  rw [torusWeight_eq_prod_layers β hβ μt Γ U]
  apply Finset.prod_congr rfl
  intro c _
  change magneticDensity Γ β zeroFlux (Γ.sliceField U (c-1+1)) *
    linkProductKernel β (Γ.sliceField U (c-1+1)) _ = _
  rw [sub_add_cancel]
  apply congrArg (· * linkProductKernel β _ _)
  have him := ((transferOperator_sliceEnergy β hβ Γ μt).2.1 (Γ.sliceField U c)).1
  rw [magneticDensity,magneticEnergy_zero,Complex.ofReal_exp,Complex.ofReal_neg,
    ← BoundedMultiplication.eq_ofReal_re_of_im_eq_zero him]

/-- Arbitrary measurable physical insertions, including products of centered
plaquette observables, have this exact layer integral with the *same* observable. -/
theorem liftedGibbs_integral_pairs {β : ℝ} (hβ : 0 < β) (F : GaugeField 1 → ℂ) (hm : Measurable F) :
    (∫ U, F U ∂Γ.lattice.liftedGibbsMeasure β) =
      ((ENNReal.ofReal (Γ.lattice.partitionFunction β))⁻¹).toReal •
        ∫ p, releasePairWeight Γ β p * F (Γ.lattice.lift (fieldOfPairs Γ p)) ∂releasePairHaar Γ := by
  have hQ := LatticeSymmetries.periodicQuotient_finite.1 Γ.lattice
  have he : MeasurePreserving (releasePairCoordinates Γ) Γ.lattice.quotientHaar (releasePairHaar Γ) :=
    (cubic_torus_slice_decomposition Γ μt).2
  rw [PeriodSublattice.liftedGibbsMeasure,integral_map hQ.continuous_lift.measurable.aemeasurable hm.aestronglyMeasurable,
    PeriodSublattice.gibbsMeasure,integral_smul_measure,SplitTorusPullback.integral_withDensity_boltzmannWeight Γ.lattice hQ]
  congr 1
  rw [← he.integral_comp' (fun p => releasePairWeight Γ β p * F (Γ.lattice.lift (fieldOfPairs Γ p)))]
  apply integral_congr_ae
  filter_upwards with U
  rw [releasePairWeight_boltzmann Γ hβ U]
  change _ = _ * F (Γ.lattice.lift ((releasePairCoordinates Γ).symm (releasePairCoordinates Γ U)))
  rw [MeasurableEquiv.symm_apply_apply,Complex.real_smul]

/-- Integrate the independent temporal bonds in a cycle whose insertion may
change at every step. The half-weights telescope by permutation of levels. -/
theorem markedPair_integral {I X G : Type*} [Fintype I] [TopologicalSpace X] [TopologicalSpace G]
    [CompactSpace X] [CompactSpace G] [MeasurableSpace X] [MeasurableSpace G] [BorelSpace X] [BorelSpace G]
    [SecondCountableTopology X] [SecondCountableTopology G]
    (μ : Measure X) (ν : Measure G) [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] (σ : Equiv.Perm I)
    (h : C(X,ℂ)) (D : I → C((X × X) × G,ℂ)) :
    (∫ p : I → G × X, ∏ i, (h (p (σ i)).2)^2 * D i (((p (σ i)).2,(p i).2),(p i).1)
        ∂Measure.pi fun _ => ν.prod μ) =
      ∫ u : I → X, ∏ i, h (u (σ i)) * h (u i) * ∫ g, D i ((u (σ i),u i),g) ∂ν ∂Measure.pi (fun _ => μ) := by
  let e := MeasurableEquiv.arrowProdEquivProdArrow G X I
  have he := (measurePreserving_arrowProdEquivProdArrow G X I (fun _ => ν) (fun _ => μ)).symm
  let f (p : I → G × X) := ∏ i, (h (p (σ i)).2)^2 * D i (((p (σ i)).2,(p i).2),(p i).1)
  have hc : Continuous f := by unfold f; fun_prop
  have hi := he.integrable_comp_of_integrable (hc.integrable_of_hasCompactSupport (HasCompactSupport.of_compactSpace _))
  let H (p : (I → G) × (I → X)) := f (e.symm p)
  rw [← he.integral_comp' f]
  change (∫ p, H p ∂(Measure.pi fun _ => ν).prod (Measure.pi fun _ => μ)) = _
  rw [integral_prod_symm H hi]
  apply integral_congr_ae
  filter_upwards with u
  let f' (i) (g : G) := D i ((u (σ i),u i),g)
  change (∫ g : I → G, ∏ i, h (u (σ i)) ^ 2 * f' i (g i) ∂Measure.pi fun _ => ν) = _
  simp_rw [Finset.prod_mul_distrib]
  rw [integral_const_mul,integral_fintype_prod_eq_prod f']
  congr 1
  simp only [sq,Finset.prod_mul_distrib]
  rw [Equiv.prod_comp σ (fun i => h (u i))]

def physicalWindow (p : ReleasePairs Γ) (c : ZMod Γ.side) :
    (RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) × RectGauges (fun _ => Γ.side) :=
  ((readLinks Γ (p (c-1)).2,readLinks Γ (p c).2),readVertices Γ (p c).1)

theorem readLinks_continuous : Continuous (readLinks Γ) := continuous_pi fun _ => continuous_apply _
theorem readVertices_continuous : Continuous (readVertices Γ) := continuous_pi fun _ => continuous_apply _

theorem periodicHalfWeight_sq {β : ℝ} (u : Γ.LinkOrbits μt → Wilson.SU2) :
    (rectHalfWeight (fun _ => Γ.side) β zeroFlux (readLinks Γ u) : ℂ) ^ 2 = magneticDensity Γ β zeroFlux u := by
  rw [sq,← Complex.ofReal_mul]
  unfold magneticDensity
  rw [magneticEnergy_readLinks]
  change ((Real.exp _ * Real.exp _ : ℝ) : ℂ) = (Real.exp _ : ℂ)
  rw [← Real.exp_add]
  congr 2
  ring

/-- Exact marked cubic Haar cycle. The marks may involve the temporal bonds
in their layer as well as both spatial boundaries. -/
theorem integral_markedPairs (β : ℝ) (F : ZMod Γ.side → C((RectSlice (fun _ => Γ.side) ×
    RectSlice (fun _ => Γ.side)) × RectGauges (fun _ => Γ.side),ℂ)) :
    (∫ p, releasePairWeight Γ β p * ∏ c, F c (physicalWindow Γ p c) ∂releasePairHaar Γ) =
      ∫ u : ZMod Γ.side → RectSlice (fun _ => Γ.side),
        ∏ c, rectTestEntry (fun _ => Γ.side) β zeroFlux (F c) (u (c-1),u c)
          ∂Measure.pi (fun _ => rectHaar (fun _ => Γ.side)) := by
  let X := Γ.LinkOrbits μt → Wilson.SU2
  let G := Γ.VertexOrbits μt → Wilson.SU2
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let h : C(X,ℂ) := ⟨fun u => (rectHalfWeight n β zeroFlux (readLinks Γ u) : ℂ),
    Complex.continuous_ofReal.comp ((rectHalfWeight n β zeroFlux).continuous.comp (readLinks_continuous Γ))⟩
  let recode : C((X × X) × G,(RectSlice n × RectSlice n) × RectGauges n) :=
    ⟨fun z => ((readLinks Γ z.1.1,readLinks Γ z.1.2),readVertices Γ z.2),
      (((readLinks_continuous Γ).comp (continuous_fst.comp continuous_fst)).prodMk
        ((readLinks_continuous Γ).comp (continuous_snd.comp continuous_fst))).prodMk
        ((readVertices_continuous Γ).comp continuous_snd)⟩
  let D (c : ZMod Γ.side) : C((X × X) × G,ℂ) :=
    ⟨fun z => F c (recode z) * (rectTemporal n β ((recode z).1.1,rectGauge n ((recode z).1.2,(recode z).2)) : ℂ),by fun_prop⟩
  let σ : Equiv.Perm (ZMod Γ.side) := Equiv.subRight 1
  have link (u v : X) (g : G) : linkProductKernel β u (Γ.orbitGaugeAct g v) =
      (rectTemporal n β (readLinks Γ u,rectGauge n (readLinks Γ v,readVertices Γ g)) : ℂ) := by
    rw [← readLinks_gaugeAct,rectTemporal_readLinks]
  have point (p : ReleasePairs Γ) : releasePairWeight Γ β p * ∏ c, F c (physicalWindow Γ p c) =
      ∏ c, (h (p (σ c)).2)^2 * D c (((p (σ c)).2,(p c).2),(p c).1) := by
    unfold releasePairWeight
    rw [← Finset.prod_mul_distrib]
    apply Finset.prod_congr rfl
    intro c _
    change _ = (rectHalfWeight n β zeroFlux (readLinks Γ (p (c-1)).2) : ℂ)^2 * (_ * _)
    rw [periodicHalfWeight_sq,link]
    exact (mul_assoc _ _ _).trans (congrArg (magneticDensity Γ β zeroFlux (p (c-1)).2 * ·) (mul_comm _ _))
  simp_rw [point]
  rw [markedPair_integral _ _ σ h D]
  let E := MeasurableEquiv.piCongrRight fun _ : ZMod Γ.side => linkCoordinates Γ
  have mp : MeasurePreserving E (Measure.pi (fun _ => ComplexMatrix2.haarPi (Γ.LinkOrbits μt)))
      (Measure.pi (fun _ => rectHaar n)) := measurePreserving_pi _ _ fun _ => linkCoordinates_preserving Γ
  rw [← mp.integral_comp' (fun u => ∏ c, rectTestEntry n β zeroFlux (F c) (u (c-1),u c))]
  apply integral_congr_ae
  filter_upwards with u
  apply Finset.prod_congr rfl
  intro c _
  change (rectHalfWeight n β zeroFlux (readLinks Γ (u (c-1))) : ℂ) * (rectHalfWeight n β zeroFlux (readLinks Γ (u c)) : ℂ) *
      (∫ g, D c ((u (c-1),u c),g) ∂ComplexMatrix2.haarPi (Γ.VertexOrbits μt)) =
    rectTestEntry n β zeroFlux (F c) (linkCoordinates Γ (u (c-1)),linkCoordinates Γ (u c))
  rw [linkCoordinates_apply,linkCoordinates_apply,rectTestEntry,Complex.ofReal_mul]
  congr 1
  rw [← (gaugeCoordinates_preserving Γ).integral_comp' (fun g => F c (((readLinks Γ (u (c-1))),readLinks Γ (u c)),g) *
    (rectTemporal n β (readLinks Γ (u (c-1)),rectGauge n (readLinks Γ (u c),g)) : ℂ))]
  exact integral_congr_ae (ae_of_all _ fun g => by simp only [gaugeCoordinates_apply]; rfl)


def CentreBlind {n : spatialAxis → ℕ} (F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) : Prop :=
  ∀ (e : Flux) (u v : RectSlice n) (g : RectGauges n), F ((rectFlip e u,rectFlip e v),g) = F ((u,v),g)

theorem rectTestEntry_flip {n : spatialAxis → ℕ} (β : ℝ) (m : Flux)
    {F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)} (hb : CentreBlind F)
    (e : Flux) (u v : RectSlice n) : rectTestEntry n β m F (rectFlip e u,rectFlip e v) = rectTestEntry n β m F (u,v) := by
  simp only [rectTestEntry,rectHalfWeight_flip,rectGauge_flip,rectTemporal_flip,hb e]

set_option maxHeartbeats 900000 in
theorem rectTestOperator_commutes {n : spatialAxis → ℕ} (β : ℝ) (m : Flux)
    {F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)} (hb : CentreBlind F) (e : Flux) :
    Commute (Kernel.operator _ (rectTestEntry_memLp n β m F)) (rectTranslation n e) := by
  let k := rectTestEntry n β m F
  have hk := rectTestEntry_memLp n β m F
  have hf : Continuous (rectFlip (n := n) e) := continuous_pi fun _ => continuous_const.mul (continuous_apply _)
  have hl : MemLp (fun z : RectSlice n × RectSlice n => k (z.1,rectFlip e z.2)) 2 ((rectHaar n).prod (rectHaar n)) :=
    ((rectTestEntry_continuous n β m F).comp (continuous_fst.prodMk (hf.comp continuous_snd))).memLp_of_hasCompactSupport
      (HasCompactSupport.of_compactSpace _)
  exact (rectRight_insert n e k hk hl).symm.trans (rectLeft_insert n e k hk hl (rectTestEntry_flip β m hb e)).symm

def writeLinks (u : RectSlice (fun _ => Γ.side)) (b : Γ.LinkOrbits μt) := u ((linkFromCode Γ).symm b)

theorem writeLinks_readLinks (u : Γ.LinkOrbits μt → Wilson.SU2) : writeLinks Γ (readLinks Γ u) = u := by
  funext b
  simp only [writeLinks,readLinks,Equiv.apply_symm_apply]

theorem readLinks_writeLinks (u : RectSlice (fun _ => Γ.side)) : readLinks Γ (writeLinks Γ u) = u := by
  funext b
  simp only [writeLinks,readLinks,Equiv.symm_apply_apply]

theorem writeLinks_flip (e : Flux) (u : RectSlice (fun _ => Γ.side)) :
    writeLinks Γ (rectFlip e u) = centreShift Γ μt (cuts e) (writeLinks Γ u) := by
  have hc := readLinks_electric Γ e (writeLinks Γ u)
  rw [readLinks_writeLinks] at hc
  exact (congrArg (writeLinks Γ) hc.symm).trans (writeLinks_readLinks Γ _)

def spatialFaceMark (q : Γ.FaceOrbits μt) : C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) ×
    RectGauges (fun _ => Γ.side),ℂ) :=
  ⟨fun z => ((1 - halfTrace (Γ.orbitHolonomy q (writeLinks Γ z.1.1)) : ℝ) : ℂ),by
    have hw : Continuous (writeLinks Γ) := continuous_pi fun _ => continuous_apply _
    have hc : Continuous (Γ.orbitHolonomy q) := SliceEnergyProperties.continuous_holonomyOfFamily _
    exact Complex.continuous_ofReal.comp (continuous_const.sub (Wilson.continuous_halfTrace.comp
      (hc.comp (hw.comp (continuous_fst.comp continuous_fst)))))⟩

theorem spatialFaceMark_blind (q : Γ.FaceOrbits μt) : CentreBlind (spatialFaceMark Γ q) := by
  intro e u v g
  change ((1-halfTrace (Γ.orbitHolonomy q (writeLinks Γ (rectFlip e u))) : ℝ) : ℂ) = _
  rw [writeLinks_flip]
  exact congrArg (fun w => ((1-halfTrace w : ℝ) : ℂ)) (holonomy_centreShift Γ e (CubicPeriodSublattice.faceRep q) _)

def temporalFaceMark (b : Γ.LinkOrbits μt) : C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) ×
    RectGauges (fun _ => Γ.side),ℂ) :=
  let e := (linkFromCode Γ).symm b
  ⟨fun z => ((1 - halfTrace (z.1.1 e * (rectGauge (fun _ => Γ.side) (z.1.2,z.2) e)⁻¹) : ℝ) : ℂ),by
    apply Complex.continuous_ofReal.comp
    apply continuous_const.sub
    apply Wilson.continuous_halfTrace.comp
    fun_prop⟩

theorem temporalFaceMark_blind (b : Γ.LinkOrbits μt) : CentreBlind (temporalFaceMark Γ b) := by
  intro e u v g
  let a := (linkFromCode Γ).symm b
  change ((1 - halfTrace ((rectFlip e u a) * (rectGauge _ (rectFlip e v,g) a)⁻¹) : ℝ) : ℂ) = _
  rw [rectGauge_flip]
  let z := linkCentre (decide (fluxBit e a.2.val = true ∧ (a.1 a.2).val = 0))
  change ((1-halfTrace ((z * u a) * (z * rectGauge _ (v,g) a)⁻¹) : ℝ) : ℂ) = _
  rw [show (z * u a) * (z * rectGauge _ (v,g) a)⁻¹ = z * (u a * (rectGauge _ (v,g) a)⁻¹) * z⁻¹ by group,
    Wilson.halfTrace_conjugate]
  rfl

theorem faceEnergy_halfTrace (U : GaugeField 1) (p : ElementaryPlaquette 1) :
    faceEnergy U p = 1 - halfTrace (faceHolonomy U p) := by
  unfold faceEnergy halfTrace Matrices.ComplexMatrix2.fullTrace
  ring

theorem spatialFaceMark_read (c : ZMod Γ.side) (q : Γ.FaceOrbits μt) (p : ReleasePairs Γ) :
    (Γ.lattice.quotientFaceEnergy (fieldOfPairs Γ p) (SliceProduct.faceLabel Γ μt (.inl (c,q))) : ℂ) =
      spatialFaceMark Γ q (physicalWindow Γ p c) := by
  let U := fieldOfPairs Γ p
  let y := CubicPeriodSublattice.faceRep q
  have h := SliceProduct.holonomyOfFamily_sliceField (Γ := Γ) U (Γ.levelRep c) y
  rw [SliceProduct.levelClass_levelRep] at h
  change ((Γ.lattice.quotientFaceEnergy U (Γ.lattice.faceClass _) : ℝ) : ℂ) = _
  rw [SliceProduct.quotientFaceEnergy_faceClass,faceEnergy_halfTrace,← h]
  change ((1 - halfTrace (Γ.orbitHolonomy q (Γ.sliceField (μ := μt) U c)) : ℝ) : ℂ) =
    ((1 - halfTrace (Γ.orbitHolonomy q (writeLinks Γ (readLinks Γ (p (c-1)).2))) : ℝ) : ℂ)
  rw [writeLinks_readLinks]
  exact congrArg (fun u => ((1 - halfTrace (Γ.orbitHolonomy q u) : ℝ) : ℂ)) (funext (fieldOfPairs_spatial Γ p c))

theorem temporalFaceMark_read (c : ZMod Γ.side) (b : Γ.LinkOrbits μt) (p : ReleasePairs Γ) :
    (Γ.lattice.quotientFaceEnergy (fieldOfPairs Γ p) (SliceProduct.faceLabel Γ μt (.inr (c,b))) : ℂ) =
      temporalFaceMark Γ b (physicalWindow Γ p c) := by
  let U := fieldOfPairs Γ p
  have h := SliceProduct.sliceField_mul_inv_orbitGaugeAct (Γ := Γ) U (Γ.levelRep c) (CubicPeriodSublattice.linkRep b)
  rw [SliceProduct.levelClass_levelRep,Γ.linkClass_linkRep] at h
  change ((Γ.lattice.quotientFaceEnergy U (Γ.lattice.faceClass _) : ℝ) : ℂ) = _
  rw [SliceProduct.quotientFaceEnergy_faceClass,faceEnergy_halfTrace]
  have htr : halfTrace (faceHolonomy (Γ.lattice.lift U) (temporalPlaquette μt (Γ.levelRep c) (CubicPeriodSublattice.linkRep b))) =
      halfTrace (SliceProduct.temporalLoop (Γ.lattice.lift U) (Γ.levelRep c) (CubicPeriodSublattice.linkRep b)) := by
    rcases SliceProduct.faceHolonomy_temporalPlaquette (Γ.lattice.lift U) (Γ.levelRep c) (CubicPeriodSublattice.linkRep b) with h|h
    · rw [h]
    · rw [h,Wilson.halfTrace_inv]
  rw [htr,← h]
  have hu : Γ.sliceField (μ := μt) U c = (p (c-1)).2 := funext (fieldOfPairs_spatial Γ p c)
  have hv : Γ.sliceField (μ := μt) U (c+1) = (p c).2 := calc
    _ = (p (c+1-1)).2 := funext (fieldOfPairs_spatial Γ p (c+1))
    _ = _ := by rw [add_sub_cancel_right]
  have hg : Γ.temporalSliceField (μ := μt) U c = (p c).1 := funext (fieldOfPairs_temporal Γ p c)
  rw [hu,hv,hg]
  let a := (linkFromCode Γ).symm b
  change _ = ((1-halfTrace (readLinks Γ (p (c-1)).2 a * (rectGauge _ (readLinks Γ (p c).2,readVertices Γ (p c).1) a)⁻¹) : ℝ) : ℂ)
  rw [← readLinks_gaugeAct]
  simp only [a,readLinks,Equiv.apply_symm_apply]

theorem face_as_layer_plaquette (p : ElementaryPlaquette 1) :
    let j := level μt p.corner
    (∃ q : SlicePlaquette μt, shiftedPlaquette μt j q = p) ∨ ∃ b : SliceLink μt, temporalPlaquette μt j b = p := by
  let j := level μt p.corner
  let y := slicePart μt p.corner
  have hx : pointAtLevel μt j y = p.corner := SliceProduct.pointAtLevel_level_slicePart p.corner
  have hl : p.lowAxis ≠ μt := by
    intro h
    have hh := p.lowAxis_lt_highAxis
    rw [h] at hh
    exact (not_lt_of_ge (Fin.le_last p.highAxis)) hh
  by_cases hr : p.highAxis = μt
  · let b := SliceLink.ofAxis y p.lowAxis hl
    have hp : CutoffLattice.faceOfPair p.corner p.lowAxis μt hl = p := by
      unfold CutoffLattice.faceOfPair
      have hh := p.lowAxis_lt_highAxis
      rw [hr] at hh
      rw [dif_pos hh]
      exact ElementaryPlaquette.ext rfl rfl hr.symm
    have hd : b.axis = p.lowAxis := sliceLink_ofAxis_axis y ⟨p.lowAxis,hl⟩
    have he : temporalPlaquette μt j b = p := by
      unfold temporalPlaquette
      exact (SliceProduct.faceOfPair_congr hx hd _ _).trans hp
    exact Or.inr ⟨b,he⟩
  · let q : SlicePlaquette μt :=
      ⟨CutoffLattice.face (y : LatticePoint 1) p.lowAxis p.highAxis p.lowAxis_lt_highAxis, by
        intro c hc
        simp only [ElementaryPlaquette.cornerSet,Set.mem_insert_iff,Set.mem_singleton_iff] at hc
        rcases hc with rfl|rfl|rfl|rfl
        · exact y.property
        · exact add_axisStep_mem_sliceLattice y.property hl
        · exact add_axisStep_mem_sliceLattice (add_axisStep_mem_sliceLattice y.property hl) hr
        · exact add_axisStep_mem_sliceLattice y.property hr⟩
    have he : shiftedPlaquette μt j q = p := by
      refine ElementaryPlaquette.ext ?_ ?_ ?_
      · change (y : LatticePoint 1) + j • axisStep 1 μt = p.corner
        exact (add_comm _ _).trans hx
      · rfl
      · rfl
    exact Or.inl ⟨q,he⟩

/-- The base time of a lifted plaquette is fixed before taking the finite
quotient. This keeps the slab location when the volume varies. -/
theorem face_at_base_level (p : ElementaryPlaquette 1) :
    let c := Γ.levelClass (level μt p.corner)
    (∃ q : Γ.FaceOrbits μt, SliceProduct.faceLabel Γ μt (.inl (c,q)) = Γ.lattice.faceClass p) ∨
      ∃ b : Γ.LinkOrbits μt, SliceProduct.faceLabel Γ μt (.inr (c,b)) = Γ.lattice.faceClass p := by
  rcases face_as_layer_plaquette p with ⟨q,he⟩|⟨b,he⟩
  · left
    refine ⟨Γ.faceClass q,?_⟩
    change Γ.lattice.faceClass _ = _
    rw [SliceProduct.faceClass_shiftedPlaquette,he]
  · right
    refine ⟨Γ.linkClass b,?_⟩
    change Γ.lattice.faceClass _ = _
    rw [SliceProduct.faceClass_temporalPlaquette,he]

theorem wilsonFace_norm (g : Wilson.SU2) : ‖((1 - halfTrace g : ℝ) : ℂ)‖ ≤ 2 := by
  have lo := Wilson.halfTrace_le_one (centreElt * g)
  rw [Wilson.halfTrace_centerMinus] at lo
  rw [Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg (sub_nonneg.mpr (Wilson.halfTrace_le_one g))]
  linarith

theorem spatialFaceMark_norm (q : Γ.FaceOrbits μt) : ‖spatialFaceMark Γ q‖ ≤ 2 :=
  (ContinuousMap.norm_le _ (by norm_num : (0 : ℝ) ≤ 2)).2 (fun _ => wilsonFace_norm _)

theorem temporalFaceMark_norm (b : Γ.LinkOrbits μt) : ‖temporalFaceMark Γ b‖ ≤ 2 :=
  (ContinuousMap.norm_le _ (by norm_num : (0 : ℝ) ≤ 2)).2 (fun _ => wilsonFace_norm _)


theorem translate_temporalPlaquette (j k : ℤ) (b : SliceLink μt) :
    CutoffLattice.translateFace (temporalPlaquette μt j b) (k • axisStep 1 μt) = temporalPlaquette μt (j+k) b := by
  unfold temporalPlaquette
  rw [← SliceProduct.faceOfPair_add]
  apply SliceProduct.faceOfPair_congr _ rfl
  unfold pointAtLevel
  rw [add_smul]
  abel

theorem translate_spatialPlaquette (j k : ℤ) (q : SlicePlaquette μt) :
    CutoffLattice.translateFace (shiftedPlaquette μt j q) (k • axisStep 1 μt) = shiftedPlaquette μt (j+k) q := by
  unfold shiftedPlaquette
  rw [SliceProduct.translateFace_add,add_smul]

/-- One and the same marked kernel reads a given lifted plaquette and all its
integer time translates. Translation changes its level, including at the seam. -/
theorem faceEnergy_translated_layerMark (p : ElementaryPlaquette 1) :
    ∃ F : C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) × RectGauges (fun _ => Γ.side),ℂ),
      CentreBlind F ∧ ‖F‖ ≤ 2 ∧ ∀ (k : ℤ) (z : ReleasePairs Γ),
        (faceEnergy (Γ.lattice.lift (fieldOfPairs Γ z)) (CutoffLattice.translateFace p (k • axisStep 1 μt)) : ℂ) =
          F (physicalWindow Γ z (Γ.levelClass (level μt p.corner + k))) := by
  let j := level μt p.corner
  rcases face_as_layer_plaquette p with ⟨q,hq⟩|⟨b,hb⟩
  · refine ⟨spatialFaceMark Γ (Γ.faceClass q),spatialFaceMark_blind Γ _,spatialFaceMark_norm Γ _,fun k z => ?_⟩
    have he : CutoffLattice.translateFace p (k • axisStep 1 μt) = shiftedPlaquette μt (j+k) q := by
      exact (congrArg (fun f => CutoffLattice.translateFace f _) hq.symm).trans (translate_spatialPlaquette j k q)
    rw [he,← SliceProduct.quotientFaceEnergy_faceClass,← SliceProduct.faceClass_shiftedPlaquette]
    exact spatialFaceMark_read Γ _ _ z
  · refine ⟨temporalFaceMark Γ (Γ.linkClass b),temporalFaceMark_blind Γ _,temporalFaceMark_norm Γ _,fun k z => ?_⟩
    have he : CutoffLattice.translateFace p (k • axisStep 1 μt) = temporalPlaquette μt (j+k) b := by
      exact (congrArg (fun f => CutoffLattice.translateFace f _) hb.symm).trans (translate_temporalPlaquette j k b)
    rw [he,← SliceProduct.quotientFaceEnergy_faceClass,← SliceProduct.faceClass_temporalPlaquette]
    exact temporalFaceMark_read Γ _ _ z

def translateUnitFace (k : ℤ) : ElementaryPlaquette 1 ≃ ElementaryPlaquette 1 where
  toFun p := CutoffLattice.translateFace p (k • axisStep 1 μt)
  invFun p := CutoffLattice.translateFace p (-(k • axisStep 1 μt))
  left_inv p := by
    change CutoffLattice.translateFace (CutoffLattice.translateFace p _) _ = p
    rw [SliceProduct.translateFace_add,add_neg_cancel,SliceProduct.translateFace_zero]
  right_inv p := by
    change CutoffLattice.translateFace (CutoffLattice.translateFace p _) _ = p
    rw [SliceProduct.translateFace_add,neg_add_cancel,SliceProduct.translateFace_zero]

def translatedUnitTest (k : ℤ) (f : RealValued) : RealValued :=
  fun x => f (x - ((k • axisStep 1 μt : LatticePoint 1) : InfiniteLattice.AmbientSpace))

theorem translatedUnitTest_center (k : ℤ) (f : RealValued) (p : ElementaryPlaquette 1) :
    translatedUnitTest k f ((translateUnitFace k p).center) = f p.center := by
  have he : (translateUnitFace k p).center = p.center + ((k • axisStep 1 μt : LatticePoint 1) : InfiniteLattice.AmbientSpace) := by
    funext i
    simp only [translateUnitFace,Equiv.coe_fn_mk,CutoffLattice.translateFace,CutoffLattice.face,ElementaryPlaquette.center,AddSubgroup.coe_add,Pi.add_apply]
    ring
  simp only [translatedUnitTest,he,add_sub_cancel_right]

/-- The finite plaquette set, coefficients and marked kernels of a smearing
are fixed before choosing its time displacement. -/
theorem translated_smearedEnergy_layerMarks (f : RealValued) (hf : HasCompactSupport f) :
    ∃ P : Finset (ElementaryPlaquette 1), ∀ Γ : CubicPeriodSublattice,
      ∃ F : ElementaryPlaquette 1 → C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) ×
          RectGauges (fun _ => Γ.side),ℂ),
        (∀ q, CentreBlind (F q) ∧ ‖F q‖ ≤ 2) ∧ ∀ (k : ℤ) (z : ReleasePairs Γ),
        ((smearedEnergy (translatedUnitTest k f) (Γ.lattice.lift (fieldOfPairs Γ z)) : ℝ) : ℂ) =
          ∑ q ∈ P, (f q.center : ℂ) * F q (physicalWindow Γ z (Γ.levelClass (level μt q.corner+k))) := by
  classical
  let P := (FaceEnergyBounds.finite_setOf_center_mem (a := 1) (by norm_num) hf.isBounded).toFinset
  refine ⟨P,fun Γ => ?_⟩
  choose F hblind hnorm hread using faceEnergy_translated_layerMark Γ
  refine ⟨F,fun q => ⟨hblind q,hnorm q⟩,fun k z => ?_⟩
  let U := Γ.lattice.lift (fieldOfPairs Γ z)
  let G (p : ElementaryPlaquette 1) := faceEnergy U p * translatedUnitTest k f p.center
  have he (q : ElementaryPlaquette 1) : G (translateUnitFace k q) = faceEnergy U (translateUnitFace k q) * f q.center := by
    change faceEnergy U (translateUnitFace k q) * translatedUnitTest k f ((translateUnitFace k q).center) = _
    rw [translatedUnitTest_center]
  have hs : smearedEnergy (translatedUnitTest k f) U = ∑ q ∈ P,faceEnergy U (translateUnitFace k q) * f q.center := by
    change (∑ᶠ p, G p) = _
    rw [← finsum_comp_equiv (translateUnitFace k) (f := G)]
    simp_rw [he]
    apply finsum_eq_sum_of_support_subset
    intro q hq
    apply (Set.Finite.mem_toFinset _).2
    apply subset_tsupport
    intro hh
    exact hq (by simp [hh])
  rw [hs,Complex.ofReal_sum]
  apply Finset.sum_congr rfl
  intro q _
  rw [Complex.ofReal_mul]
  change (faceEnergy _ (CutoffLattice.translateFace q (k • axisStep 1 μt)) : ℂ) * _ = _
  rw [hread,mul_comm]


/-- Each actual plaquette of the infinite unit lattice, restricted to the
periodic release cube, is one bounded continuous, centre-blind layer insertion. -/
theorem faceEnergy_layerMark (p : ElementaryPlaquette 1) :
    ∃ F : C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) × RectGauges (fun _ => Γ.side),ℂ),
      CentreBlind F ∧ ‖F‖ ≤ 2 ∧ ∀ z : ReleasePairs Γ, (faceEnergy (Γ.lattice.lift (fieldOfPairs Γ z)) p : ℂ) =
        F (physicalWindow Γ z (Γ.levelClass (level μt p.corner))) := by
  let c := Γ.levelClass (level μt p.corner)
  rcases face_at_base_level Γ p with ⟨q,he⟩|⟨b,he⟩
  · refine ⟨spatialFaceMark Γ q,spatialFaceMark_blind Γ q,spatialFaceMark_norm Γ q,fun z => ?_⟩
    rw [← SliceProduct.quotientFaceEnergy_faceClass,← he]
    exact spatialFaceMark_read Γ c q z
  · refine ⟨temporalFaceMark Γ b,temporalFaceMark_blind Γ b,temporalFaceMark_norm Γ b,fun z => ?_⟩
    rw [← SliceProduct.quotientFaceEnergy_faceClass,← he]
    exact temporalFaceMark_read Γ c b z

/-- A physical smearing has a finite list of actual plaquettes chosen before
the volume. Each coefficient, time, and uniform layer norm is explicit. -/
theorem smearedEnergy_layerMarks (f : RealValued) (hf : HasCompactSupport f) :
    ∃ P : Finset (ElementaryPlaquette 1), ∀ Γ : CubicPeriodSublattice,
      ∃ F : ElementaryPlaquette 1 → C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) ×
          RectGauges (fun _ => Γ.side),ℂ),
        (∀ q, CentreBlind (F q) ∧ ‖F q‖ ≤ 2) ∧ ∀ p : ReleasePairs Γ,
        ((smearedEnergy f (Γ.lattice.lift (fieldOfPairs Γ p)) : ℝ) : ℂ) =
          ∑ q ∈ P, (f q.center : ℂ) * F q (physicalWindow Γ p (Γ.levelClass (level μt q.corner))) := by
  classical
  let P := (FaceEnergyBounds.finite_setOf_center_mem (a := 1) (by norm_num) hf.isBounded).toFinset
  refine ⟨P,fun Γ => ?_⟩
  choose F hblind hnorm hread using faceEnergy_layerMark Γ
  refine ⟨F,fun q => ⟨hblind q,hnorm q⟩,fun p => ?_⟩
  have finiteSum : smearedEnergy f (Γ.lattice.lift (fieldOfPairs Γ p)) =
      ∑ q ∈ P, faceEnergy (Γ.lattice.lift (fieldOfPairs Γ p)) q * f q.center := by
    apply finsum_eq_sum_of_support_subset
    intro q hq
    apply (Set.Finite.mem_toFinset _).2
    apply subset_tsupport
    intro h
    exact hq (by simp [h])
  rw [finiteSum,Complex.ofReal_sum]
  apply Finset.sum_congr rfl
  intro q _
  rw [Complex.ofReal_mul,hread,mul_comm]


theorem cubeTimeIndex {a : ℕ} (hs : Γ.side = a) :
    ∃ E : Fin a ≃ ZMod Γ.side, ∀ t, E (finRotate a t) = E t + 1 := by
  subst a
  exact ⟨Equiv.ofBijective Γ.indexLevel Γ.indexLevel_bijective,Γ.indexLevel_finRotate⟩

/-- Place every time label of a finite family in one integer interval. Its
origin and width are chosen before the spatial volume. Empty tests are included. -/
theorem finite_time_word {I J : Type*} [Fintype I] [Fintype J] (time : I → J → ℤ) :
    ∃ (b : ℤ) (w : ℕ), 0 < w ∧ ∀ i j,∃ k : Fin w,time i j = b + (k.val : ℤ) := by
  let R := ∑ p : I × J,(time p.1 p.2).natAbs
  refine ⟨-(R:ℤ),2*R+1,by omega,fun i j => ?_⟩
  have hs : (time i j).natAbs ≤ R := Finset.single_le_sum (f := fun p : I×J => (time p.1 p.2).natAbs)
    (fun p _ => Nat.zero_le _) (Finset.mem_univ (i,j))
  have hi : time i j ≤ ((time i j).natAbs : ℤ) := Int.le_natAbs
  have lo : -time i j ≤ ((time i j).natAbs : ℤ) := by simpa only [Int.natAbs_neg] using (Int.le_natAbs (a := -time i j))
  refine ⟨⟨(time i j + R).toNat,by omega⟩,?_⟩
  change time i j = -(R:ℤ)+((time i j + R).toNat:ℤ)
  omega

theorem word_residue_support {V w : ℕ} {I α : Type*} [One α] (F : ZMod V → α) (time : I → ℤ) (b : ℤ)
    (hl : ∀ i,∃ j : Fin w,time i = b+(j.val : ℤ))
    (hs : ∀ c,c ∉ Set.range (fun i => (time i : ZMod V)) → F c = 1) :
    ∀ c,c ∉ Set.range (fun j : Fin w => (b : ZMod V)+(j.val : ZMod V)) → F c = 1 := by
  intro c hc
  apply hs
  rintro ⟨i,rfl⟩
  obtain ⟨j,h⟩ := hl i
  apply hc
  refine ⟨j,?_⟩
  simp only [h,Int.cast_add,Int.cast_natCast]

/-- A mark identically one off a word has the same product on the circle
and over the word. This preserves the uniform norm bound when a word is cut out. -/
theorem residue_word_product {M : Type*} [CommMonoid M] {V w : ℕ} (hw : w ≤ V) (b : ZMod V)
    (F : ZMod V → M) [Fintype (ZMod V)]
    (hF : ∀ c,c ∉ Set.range (fun j : Fin w => b+(j.val : ZMod V)) → F c = 1) :
    (∏ j : Fin w,F (b+(j.val : ZMod V))) = ∏ c,F c := by
  classical
  let e : Fin w ↪ ZMod V := ⟨fun j => b+(j.val : ZMod V),fun i j h => by
    have he := congrArg ZMod.val (add_left_cancel h)
    rw [ZMod.val_natCast_of_lt (i.isLt.trans_le hw),ZMod.val_natCast_of_lt (j.isLt.trans_le hw)] at he
    exact Fin.ext he⟩
  calc
    _ = ∏ c ∈ Finset.univ.map e,F c := (Finset.prod_map Finset.univ e F).symm
    _ = _ := Finset.prod_subset (Finset.subset_univ _) fun c _ hc => hF c (fun ⟨i,hi⟩ =>
      hc (Finset.mem_map.mpr ⟨i,Finset.mem_univ _,hi⟩))


/-- The time origin of the physical joint chart is freely selectable, so the
seam can be placed outside a chosen family of translated windows. -/
theorem anchoredCubeTimeIndex (b : ZMod Γ.side) :
    ∃ E : Fin Γ.side ≃ ZMod Γ.side, (∀ t,E (finRotate _ t) = E t+1) ∧
      ∀ t,E t = b + (t.val : ZMod Γ.side) := by
  let E := (Equiv.ofBijective Γ.indexLevel Γ.indexLevel_bijective).trans (Equiv.addRight (b-1))
  refine ⟨E,fun t => ?_,fun t => ?_⟩
  · change Γ.indexLevel (finRotate _ t)+(b-1) = Γ.indexLevel t+(b-1)+1
    rw [Γ.indexLevel_finRotate]
    ring
  · change Γ.indexLevel t+(b-1) = b+(t.val : ZMod Γ.side)
    simp only [CubicPeriodSublattice.indexLevel,CubicPeriodSublattice.levelClass]
    push_cast
    ring


/-- Rewrite the cyclic Haar integral on residue classes with the same finite
time order used by the Hilbert--Schmidt trace. -/
theorem residue_cycle {I X : Type*} [AddCommGroup I] [Fintype I] [One I] [MeasurableSpace X]
    (μ : Measure X) [IsProbabilityMeasure μ] {a : ℕ} (E : Fin a ≃ I) (hE : ∀ t, E (finRotate a t) = E t + 1)
    (k : I → X × X → ℂ) :
    (∫ u : I → X, ∏ c, k c (u (c-1),u c) ∂Measure.pi (fun _ => μ)) =
      ∫ u : Fin a → X, ∏ t, k (E (finRotate a t)) (u t,u (finRotate a t)) ∂Kernel.copies μ a := by
  let R := MeasurableEquiv.piCongrLeft (fun _ : I => X) E
  have hp := measurePreserving_piCongrLeft (fun _ : I => μ) E
  rw [← hp.integral_comp' (fun u => ∏ c, k c (u (c-1),u c))]
  apply integral_congr_ae
  filter_upwards with u
  let e' := (finRotate a).trans E
  rw [← e'.prod_comp (fun c => k c (R u (c-1),R u c))]
  apply Finset.prod_congr rfl
  intro t _
  have prev : E (finRotate a t) - 1 = E t := by rw [hE,add_sub_cancel_right]
  change k (E (finRotate a t)) (R u (E (finRotate a t)-1),R u (E (finRotate a t))) = _
  rw [prev]
  apply congrArg (k (E (finRotate a t)))
  have eqn (i : Fin a) : R u (E i) = u i := MeasurableEquiv.piCongrLeft_apply_apply (β := fun _ : I => X) E u i
  rw [eqn,eqn]

def markedLayer (β : ℝ) (F : C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) × RectGauges (fun _ => Γ.side),ℂ)) :
    C(RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side),ℂ) :=
  ⟨rectTestEntry _ β zeroFlux F,rectTestEntry_continuous _ β zeroFlux F⟩

open scoped InnerProductSpace in
/-- Actual finite periodic Gibbs trace of a product of layer marks. The trace
may use any Hilbert basis and the multiplier may depend on each temporal bond. -/
theorem physical_marked_trace {β : ℝ} (hβ : 0 < β) (f : GaugeField 1 → ℂ) (hf : Measurable f)
    (F : ZMod Γ.side → C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) ×
      RectGauges (fun _ => Γ.side),ℂ))
    (he : ∀ p : ReleasePairs Γ, f (Γ.lattice.lift (fieldOfPairs Γ p)) = ∏ c, F c (physicalWindow Γ p c))
    {n : ℕ} (hs : Γ.side = n+2) (E : Fin (n+2) ≃ ZMod Γ.side) (hE : ∀ t, E (finRotate (n+2) t) = E t + 1)
    {I : Type*} (b : HilbertBasis I ℂ (Kernel.Space (rectHaar (fun _ => Γ.side)))) :
    let k (t : Fin (n+2)) := markedLayer Γ β (F (E (finRotate _ t)))
    let op := edgeOperator (rectHaar (fun _ => Γ.side))
    ∃ z : ℂ, HasSum (fun i => ⟪b i,(op (k (Fin.last _)) * (List.ofFn (fun t => op (k t.castSucc))).prod) (b i)⟫_ℂ) z ∧
      (∫ U, f U ∂Γ.lattice.liftedGibbsMeasure β) = ((ENNReal.ofReal (Γ.lattice.partitionFunction β))⁻¹).toReal • z := by
  let k (t : Fin (n+2)) := markedLayer Γ β (F (E (finRotate _ t)))
  refine ⟨_,hasSum_markedCycle (rectHaar (fun _ => Γ.side)) b n k,?_⟩
  rw [liftedGibbs_integral_pairs Γ hβ f hf]
  simp_rw [he]
  rw [integral_markedPairs]
  exact congrArg (fun z : ℂ => ((ENNReal.ofReal (Γ.lattice.partitionFunction β))⁻¹).toReal • z)
    (residue_cycle _ E hE (fun c => rectTestEntry _ β zeroFlux (F c)))


abbrev WindowTest (Γ : CubicPeriodSublattice) :=
  C((RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) × RectGauges (fun _ => Γ.side),ℂ)

def combineTests {J : Type*} [Fintype J] (time : J → ℤ) (F : J → WindowTest Γ)
    (c : ZMod Γ.side) : WindowTest Γ :=
  ∏ i, if Γ.levelClass (time i) = c then F i else 1

theorem combineTests_blind {J : Type*} [Fintype J] (time : J → ℤ) (F : J → WindowTest Γ)
    (hb : ∀ i,CentreBlind (F i)) (c : ZMod Γ.side) : CentreBlind (combineTests Γ time F c) := by
  intro e u v g
  simp only [combineTests,ContinuousMap.prod_apply]
  apply Finset.prod_congr rfl
  intro i _
  by_cases h : Γ.levelClass (time i) = c
  · simpa only [if_pos h] using hb i e u v g
  · simp only [if_neg h,ContinuousMap.one_apply]

theorem combineTests_off {J : Type*} [Fintype J] (time : J → ℤ) (F : J → WindowTest Γ)
    (c : ZMod Γ.side) (hc : c ∉ Set.range (Γ.levelClass ∘ time)) : combineTests Γ time F c = 1 := by
  apply Finset.prod_eq_one
  intro i _
  exact if_neg (fun h => hc ⟨i,h⟩)

theorem combineTests_values {J : Type*} [Fintype J] (time : J → ℤ) (F : J → WindowTest Γ)
    (win : ZMod Γ.side → (RectSlice (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) × RectGauges (fun _ => Γ.side)) :
    (∏ c, combineTests Γ time F c (win c)) =
      ∏ i, F i (win (Γ.levelClass (time i))) := by
  simp only [combineTests,ContinuousMap.prod_apply]
  rw [Finset.prod_comm]
  apply Finset.prod_congr rfl
  intro i _
  have h (c : ZMod Γ.side) : (if Γ.levelClass (time i) = c then F i else 1) (win c) =
      if Γ.levelClass (time i) = c then F i (win c) else 1 := by split_ifs <;> rfl
  simp_rw [h]
  exact Fintype.prod_ite_eq _ _

theorem combineTests_product {J : Type*} [Fintype J] (time : J → ℤ) (F : J → WindowTest Γ)
    (z : ReleasePairs Γ) :
    (∏ c, combineTests Γ time F c (physicalWindow Γ z c)) =
      ∏ i, F i (physicalWindow Γ z (Γ.levelClass (time i))) :=
  combineTests_values Γ time F (physicalWindow Γ z)

theorem combineTests_norm {J : Type*} [Fintype J] (time : J → ℤ) (F : J → WindowTest Γ) :
    (∏ c, ‖combineTests Γ time F c‖) ≤ ∏ i, ‖F i‖ := by
  calc
    _ ≤ ∏ c : ZMod Γ.side, ∏ i, ‖if Γ.levelClass (time i) = c then F i else 1‖ :=
      Finset.prod_le_prod (fun _ _ => norm_nonneg _) (fun c _ => Finset.norm_prod_le _ _)
    _ ≤ _ := by
      rw [Finset.prod_comm]
      apply Finset.prod_le_prod (fun _ _ => Finset.prod_nonneg fun _ _ => norm_nonneg _)
      intro i _
      have h (c : ZMod Γ.side) : ‖if Γ.levelClass (time i) = c then F i else 1‖ ≤
          if Γ.levelClass (time i) = c then ‖F i‖ else 1 := by
        split_ifs <;> simp
      exact (Finset.prod_le_prod (fun _ _ => norm_nonneg _) (fun c _ => h c)).trans_eq (Fintype.prod_ite_eq _ _)

/-- Expand each centered smeared energy into its constant and its finitely
many plaquettes. The choices of level, coefficients and norm bound are made
on the infinite lattice before taking the cube or its Haar average. -/
theorem translated_centeredProduct_layerExpansion {J : Type} [Fintype J] (f : J → RealValued)
    (hf : ∀ i, HasCompactSupport (f i)) (center : J → ℝ) :
    ∃ (I : Type) (_ : Fintype I) (weight : I → ℂ) (times : I → J → ℤ),
      ∀ Γ : CubicPeriodSublattice, ∃ K : I → ZMod Γ.side → WindowTest Γ,
        (∀ i c, CentreBlind (K i c)) ∧
        (∀ i c, c ∉ Set.range (Γ.levelClass ∘ times i) → K i c = 1) ∧
        (∀ i, (∏ c, ‖K i c‖) ≤ 2 ^ Fintype.card J) ∧ ∀ (k : ℤ) (z : ReleasePairs Γ),
          (∏ j, ((smearedEnergy (translatedUnitTest k (f j)) (Γ.lattice.lift (fieldOfPairs Γ z)) - center j : ℝ) : ℂ)) =
            ∑ i, weight i * ∏ c, K i c (physicalWindow Γ z (c+Γ.levelClass k)) := by
  classical
  choose P hP using fun j => translated_smearedEnergy_layerMarks (f j) (hf j)
  let I := (j : J) → Option ↥(P j)
  let w (j : J) : Option ↥(P j) → ℂ := fun q => q.elim (-(center j : ℂ)) (fun b => (f j b.val.center : ℂ))
  let t (j : J) : Option ↥(P j) → ℤ := fun q => q.elim 0 (fun b => level μt b.val.corner)
  let times (i : I) (j : J) := t j (i j)
  let weight (i : I) := ∏ j, w j (i j)
  refine ⟨I,inferInstance,weight,times,fun Γ => ?_⟩
  choose F hF he using fun j => hP j Γ
  let mark (j : J) : Option ↥(P j) → WindowTest Γ := fun q => q.elim 1 (fun b => F j b.val)
  let K (i : I) := combineTests Γ (times i) (fun j => mark j (i j))
  have blind (j : J) (a : Option ↥(P j)) : CentreBlind (mark j a) := by
    cases a with
    | none => exact fun _ _ _ _ => rfl
    | some q => exact (hF j q.val).1
  have bound (j : J) (a : Option ↥(P j)) : ‖mark j a‖ ≤ 2 := by
    cases a with
    | none => norm_num [mark]
    | some q => exact (hF j q.val).2
  refine ⟨K,fun i c => combineTests_blind Γ _ _ (fun j => blind j _) c,
    fun i c hc => combineTests_off Γ _ _ c hc,fun i => ?_,fun k z => ?_⟩
  · exact (combineTests_norm Γ _ _).trans ((Finset.prod_le_prod (fun _ _ => norm_nonneg _)
      (fun j _ => bound j (i j))).trans_eq (by simp))
  · let Z (j : J) (a : Option ↥(P j)) := mark j a (physicalWindow Γ z (Γ.levelClass (t j a) + Γ.levelClass k))
    have each (j : J) : ((smearedEnergy (translatedUnitTest k (f j)) (Γ.lattice.lift (fieldOfPairs Γ z)) - center j : ℝ) : ℂ) =
        ∑ a : Option ↥(P j), w j a * Z j a := by
      rw [Complex.ofReal_sub,he j k z,Fintype.sum_option]
      simp only [Z,mark,w,t,Option.elim_none,Option.elim_some,ContinuousMap.one_apply,mul_one,Finset.sum_coe_sort]
      rw [← Finset.sum_coe_sort (P j) (fun q => (f j q.center : ℂ) * F j q (physicalWindow Γ z (Γ.levelClass (level μt q.corner + k))))]
      simp only [CubicPeriodSublattice.levelClass,Int.cast_add]
      ring
    simp_rw [each]
    rw [Fintype.prod_sum]
    apply Finset.sum_congr rfl
    intro i _
    rw [Finset.prod_mul_distrib,combineTests_values]


theorem centeredProduct_layerExpansion {J : Type} [Fintype J] (f : J → RealValued)
    (hf : ∀ i, HasCompactSupport (f i)) (center : J → ℝ) :
    ∃ (I : Type) (_ : Fintype I) (weight : I → ℂ) (times : I → J → ℤ),
      ∀ Γ : CubicPeriodSublattice, ∃ K : I → ZMod Γ.side → WindowTest Γ,
        (∀ i c, CentreBlind (K i c)) ∧
        (∀ i c, c ∉ Set.range (Γ.levelClass ∘ times i) → K i c = 1) ∧
        (∀ i, (∏ c, ‖K i c‖) ≤ 2 ^ Fintype.card J) ∧ ∀ z : ReleasePairs Γ,
          (∏ j, ((smearedEnergy (f j) (Γ.lattice.lift (fieldOfPairs Γ z)) - center j : ℝ) : ℂ)) =
            ∑ i, weight i * ∏ c, K i c (physicalWindow Γ z c) := by
  obtain ⟨I,fi,weight,times,h⟩ := translated_centeredProduct_layerExpansion f hf center
  refine ⟨I,fi,weight,times,fun Γ => ?_⟩
  obtain ⟨K,hb,ho,hn,he⟩ := h Γ
  refine ⟨K,hb,ho,hn,fun z => ?_⟩
  have hz (g : RealValued) : translatedUnitTest 0 g = g := by
    funext x
    change g (x - ((0 • axisStep 1 μt : LatticePoint 1) : InfiniteLattice.AmbientSpace)) = g x
    simp
  simpa only [hz,CubicPeriodSublattice.levelClass,Int.cast_zero,add_zero] using he 0 z

end PhysicalInsertions


section MarkedTori

local notation "μt" => TimeAxis.timeIdx
variable {n : spatialAxis → ℕ} {I : Type} [Fintype I]

abbrev JointSlice (n : spatialAxis → ℕ) (I : Type) := I → RectGauges n × RectSlice n
abbrev jointHaar (n : spatialAxis → ℕ) (I : Type) [Fintype I] : Measure (JointSlice n I) :=
  Measure.pi fun _ => (rectGaugeHaar n).prod (rectHaar n)

def jointMark (σ : Equiv.Perm I) (F : I → C((RectSlice n × RectSlice n) × RectGauges n,ℂ))
    (z : JointSlice n I) : ℂ := ∏ c, F c (((z (σ c)).2,(z c).2),(z c).1)

/-- The electric seam acts on the outgoing boundary of a single layer.
The arbitrary mark is evaluated on the original link coordinates. -/
def jointDensity (σ : Equiv.Perm I) (β : ℝ) (m : Flux) (cut : I → Flux) (z : JointSlice n I) : ℝ :=
  ∏ c, (rectHalfWeight n β m (z (σ c)).2)^2 *
    rectTemporal n β ((z (σ c)).2,rectGauge n (rectFlip (cut c) (z c).2,(z c).1))

theorem jointDensity_pos (σ : Equiv.Perm I) (β : ℝ) (m : Flux) (cut : I → Flux) (z : JointSlice n I) :
    0 < jointDensity σ β m cut z :=
  Finset.prod_pos fun _ _ => mul_pos (sq_pos_of_pos (Real.exp_pos _)) (Real.exp_pos _)

theorem continuous_jointDensity (σ : Equiv.Perm I) (β : ℝ) (m : Flux) (cut : I → Flux) :
    Continuous (jointDensity (n := n) σ β m cut) := by
  have hf (e) : Continuous (rectFlip (n := n) e) := continuous_pi fun _ => continuous_const.mul (continuous_apply _)
  unfold jointDensity
  fun_prop

theorem joint_markedCycle (σ : Equiv.Perm I) (β : ℝ) (m : Flux) (cut : I → Flux)
    (F : I → C((RectSlice n × RectSlice n) × RectGauges n,ℂ))
    (hcut : ∀ c u v g, F c ((u,rectFlip (cut c) v),g) = F c ((u,v),g)) :
    (∫ z, (jointDensity σ β m cut z : ℂ) * jointMark σ F z ∂jointHaar n I) =
      ∫ u : I → RectSlice n, ∏ c, rectTestEntry n β m (F c) (u (σ c),rectFlip (cut c) (u c))
        ∂Measure.pi (fun _ => rectHaar n) := by
  let h : C(RectSlice n,ℂ) := ⟨fun u => (rectHalfWeight n β m u : ℂ),
    Complex.continuous_ofReal.comp (rectHalfWeight n β m).continuous⟩
  have hf (e) : Continuous (rectFlip (n := n) e) := continuous_pi fun _ => continuous_const.mul (continuous_apply _)
  let D (c : I) : C((RectSlice n × RectSlice n) × RectGauges n,ℂ) :=
    ⟨fun z => F c z * (rectTemporal n β (z.1.1,rectGauge n (rectFlip (cut c) z.1.2,z.2)) : ℂ),by fun_prop⟩
  have he (z : JointSlice n I) : (jointDensity σ β m cut z : ℂ) * jointMark σ F z =
      ∏ c, (h (z (σ c)).2)^2 * D c (((z (σ c)).2,(z c).2),(z c).1) := by
    unfold jointDensity jointMark
    rw [Complex.ofReal_prod,← Finset.prod_mul_distrib]
    apply Finset.prod_congr rfl
    intro c _
    simp only [Complex.ofReal_mul,Complex.ofReal_pow]
    exact (mul_assoc _ _ _).trans (congrArg ((h (z (σ c)).2)^2 * ·) (mul_comm _ _))
  simp_rw [he]
  rw [markedPair_integral _ _ σ h D]
  apply integral_congr_ae
  filter_upwards with u
  apply Finset.prod_congr rfl
  intro c _
  rw [rectTestEntry,rectHalfWeight_flip,Complex.ofReal_mul]
  congr 1
  exact integral_congr_ae (ae_of_all _ fun g => by
    change F c ((u (σ c),u c),g) * _ = F c ((u (σ c),rectFlip (cut c) (u c)),g) * _
    rw [hcut])

theorem rectTestEntry_one (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (u v : RectSlice n) :
    rectTestEntry n β m 1 (u,v) = rectSymEntry n β m (u,v) := by
  unfold rectTestEntry rectSymEntry
  simp only [rectSymKernel_apply,Complex.ofReal_mul,ContinuousMap.one_apply,one_mul,integral_complex_ofReal]

def predecessorSeam {a : ℕ} (e : Flux) (c : Fin a) : Flux :=
  if ((finRotate a).symm c).val = 0 then e else zeroFlux

theorem joint_partition (s : Sides) (β : ℝ) (e m : Flux) (ha : 2 ≤ s μt) :
    (∫ z : JointSlice (rectShape s) (Fin (s μt)), jointDensity (finRotate _).symm β m (predecessorSeam e) z
      ∂jointHaar _ _) = twistedPartition β s (joinTwist e m) := by
  let n := rectShape s
  let a := s μt
  let F (_ : Fin a) : C((RectSlice n × RectSlice n) × RectGauges n,ℂ) := 1
  have he := joint_markedCycle (finRotate a).symm β m (predecessorSeam e) F (fun _ _ _ _ => rfl)
  have hers (z : JointSlice n (Fin a)) : jointMark (finRotate a).symm F z = 1 := by simp [F,jointMark]
  simp only [hers,mul_one,integral_complex_ofReal,F,rectTestEntry_one] at he
  apply Complex.ofReal_injective
  rw [he,twistedPartition_eq_symCycle s ha β e m,← integral_complex_ofReal]
  apply integral_congr_ae
  filter_upwards with u
  rw [← Equiv.prod_comp (finRotate a) (fun c => rectSymEntry n β m (u ((finRotate a).symm c), rectFlip (predecessorSeam e c) (u c))),Complex.ofReal_prod]
  apply Finset.prod_congr rfl
  intro t _
  simp only [predecessorSeam,Equiv.symm_apply_apply]
  by_cases h : t.val = 0 <;> simp only [h,if_true,if_false,rectFlip_zero,rectSymEntry] <;> rfl

def closingCut {a : ℕ} (e : Flux) (t : Fin a) : Flux := if t.val = 0 then e else zeroFlux

def testLayerMap (n : spatialAxis → ℕ) (β : ℝ) (m : Flux)
    (F : C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) : C(RectSlice n × RectSlice n,ℂ) :=
  ⟨rectTestEntry n β m F,rectTestEntry_continuous n β m F⟩

def flipLayerMap (e : Flux) (k : C(RectSlice n × RectSlice n,ℂ)) : C(RectSlice n × RectSlice n,ℂ) :=
  ⟨fun z => k (z.1,rectFlip e z.2),k.continuous.comp (continuous_fst.prodMk
    ((continuous_pi fun b => continuous_const.mul (continuous_apply b)).comp continuous_snd))⟩

theorem flipLayerMap_zero (k : C(RectSlice n × RectSlice n,ℂ)) : flipLayerMap zeroFlux k = k := by
  ext z
  simp [flipLayerMap,rectFlip_zero]

theorem edgeOperator_flip (e : Flux) (k : C(RectSlice n × RectSlice n,ℂ)) :
    edgeOperator (rectHaar n) (flipLayerMap e k) = edgeOperator (rectHaar n) k * rectTranslation n e :=
  rectRight_insert n e k (edgeMemLp _ k) (edgeMemLp _ (flipLayerMap e k))

def startLayers {p : ℕ} (β : ℝ) (m : Flux) (F : Fin (p+2) → C((RectSlice n × RectSlice n) × RectGauges n,ℂ)) :=
  (List.ofFn fun t : Fin (p+1) => edgeOperator (rectHaar n) (testLayerMap n β m (F t.succ))).prod

open scoped InnerProductSpace in
/-- Insert a centre seam on the closing edge of an inhomogeneous window.
The test at that edge may be the identity. -/
theorem closing_mark_trace {p : ℕ} (β : ℝ) (m e : Flux)
    (F : Fin (p+2) → C((RectSlice n × RectSlice n) × RectGauges n,ℂ))
    (hF : ∀ u v g,F 0 ((u,rectFlip e v),g) = F 0 ((u,v),g))
    {J : Type*} (b : HilbertBasis J ℂ (Kernel.Space (rectHaar n))) :
    HasSum (fun i => ⟪b i,(edgeOperator (rectHaar n) (testLayerMap n β m (F 0)) *
      rectTranslation n e * startLayers β m F) (b i)⟫_ℂ)
      (∫ z, (jointDensity (finRotate _).symm β m (closingCut e) z : ℂ) * jointMark (finRotate _).symm F z
        ∂jointHaar n (Fin (p+2))) := by
  let r := finRotate (p+2)
  let L (c : Fin (p+2)) := testLayerMap n β m (F c)
  let k (t : Fin (p+2)) := flipLayerMap (closingCut e (r t)) (L (r t))
  have mark (c : Fin (p+2)) (u v : RectSlice n) (g : RectGauges n) :
      F c ((u,rectFlip (closingCut e c) v),g) = F c ((u,v),g) := by
    by_cases hc : c = 0
    · subst c
      simpa only [closingCut,Fin.val_zero,if_true] using hF u v g
    · simp only [closingCut,if_neg (show c.val ≠ 0 from fun h => hc (Fin.ext h)),rectFlip_zero]
  rw [joint_markedCycle r.symm β m (closingCut e) F mark]
  have prod' (u : Fin (p+2) → RectSlice n) : (∏ c, rectTestEntry n β m (F c) (u (r.symm c),rectFlip (closingCut e c) (u c))) =
      ∏ t, k t (u t,u (r t)) := by
    rw [← Equiv.prod_comp r (fun c => rectTestEntry n β m (F c) (u (r.symm c),rectFlip (closingCut e c) (u c)))]
    simp only [Equiv.symm_apply_apply]
    rfl
  simp_rw [prod']
  have h := hasSum_markedCycle (rectHaar n) b p k
  have hl : k (Fin.last (p+1)) = flipLayerMap e (L 0) := by simp [k,r,finRotate_last,closingCut]
  have hs (t : Fin (p+1)) : k t.castSucc = L t.succ := by
    have eqn : r t.castSucc = t.succ := finRotate_of_lt t.isLt
    simp only [k,eqn,closingCut,Fin.val_succ,Nat.succ_ne_zero,if_false,flipLayerMap_zero]
  simp_rw [hl,edgeOperator_flip,hs] at h
  exact h

open scoped InnerProductSpace in
/-- The normalized Fourier sum of actual positive marked-background integrals
is the Hilbert trace with the periodic electric-neutral projector. -/
theorem averaged_mark_trace {p : ℕ} (β : ℝ) (m : Flux) (F : Fin (p+2) → C((RectSlice n × RectSlice n) × RectGauges n,ℂ))
    (hF : ∀ e u v g,F 0 ((u,rectFlip e v),g) = F 0 ((u,v),g))
    {J : Type*} (b : HilbertBasis J ℂ (Kernel.Space (rectHaar n))) :
    HasSum (fun i => ⟪b i,(edgeOperator (rectHaar n) (testLayerMap n β m (F 0)) * rectProj n zeroFlux *
        startLayers β m F) (b i)⟫_ℂ)
      ((1/8 : ℂ) * ∑ e : Flux, ∫ z, (jointDensity (finRotate _).symm β m (closingCut e) z : ℂ) *
        jointMark (finRotate _).symm F z ∂jointHaar n (Fin (p+2))) := by
  let A := edgeOperator (rectHaar n) (testLayerMap n β m (F 0))
  let B := startLayers β m F
  have hj (e : Flux) := closing_mark_trace β m e F (hF e) b
  have he : rectProj n zeroFlux = (1/8 : ℂ) • ∑ e : Flux, rectTranslation n e := by
    change (1/8 : ℂ) • ∑ e : Flux, (character e zeroFlux : ℂ) • rectTranslation n e = _
    have hχ (e : Flux) : (character e zeroFlux : ℂ) = 1 := by
      rcases e with ⟨a,c,d⟩; cases a <;> cases c <;> cases d <;> norm_num [character,zeroFlux]
    simp only [hχ,one_smul]
  apply ((hasSum_sum (s := Finset.univ) fun e _ => hj e).mul_left (1/8 : ℂ)).congr_fun
  intro i
  change ⟪b i,(A * rectProj n zeroFlux * B) (b i)⟫_ℂ = _
  rw [he,mul_smul_comm,smul_mul_assoc,Finset.mul_sum,Finset.sum_mul]
  simp only [ContinuousLinearMap.smul_apply,ContinuousLinearMap.sum_apply,inner_smul_right,inner_sum]
  rfl


/-- Moving the unique temporal seam from the first to the closing edge
is a cyclic change of variables in the very same positive link measure. -/
theorem closing_partition (s : Sides) (β : ℝ) (e m : Flux) (ha : 2 ≤ s μt) :
    (∫ z : JointSlice (rectShape s) (Fin (s μt)), jointDensity (finRotate _).symm β m (closingCut e) z
      ∂jointHaar _ _) = twistedPartition β s (joinTwist e m) := by
  let n := rectShape s
  let a := s μt
  let r := finRotate a
  let μ := (rectGaugeHaar n).prod (rectHaar n)
  let R := MeasurableEquiv.piCongrLeft (fun _ : Fin a => RectGauges n × RectSlice n) r
  have hp : MeasurePreserving R (jointHaar n (Fin a)) (jointHaar n (Fin a)) := measurePreserving_piCongrLeft (fun _ => μ) r
  have eqn (z : JointSlice n (Fin a)) : jointDensity r.symm β m (predecessorSeam e) (R z) =
      jointDensity r.symm β m (closingCut e) z := by
    unfold jointDensity
    rw [← Equiv.prod_comp r (fun c => (rectHalfWeight n β m ((R z) (r.symm c)).2)^2 *
      rectTemporal n β (((R z) (r.symm c)).2,rectGauge n (rectFlip (predecessorSeam e c) ((R z) c).2,((R z) c).1)))]
    apply Finset.prod_congr rfl
    intro c _
    have hz (j) : R z (r j) = z j := MeasurableEquiv.piCongrLeft_apply_apply (β := fun _ : Fin a => RectGauges n × RectSlice n) r z j
    have hp' : R z c = z (r.symm c) := by simpa only [Equiv.apply_symm_apply] using hz (r.symm c)
    have hc : predecessorSeam e (r c) = closingCut e c := by
      unfold predecessorSeam closingCut
      change (if (r.symm (r c)).val = 0 then e else zeroFlux) = _
      rw [Equiv.symm_apply_apply]
    rw [Equiv.symm_apply_apply,hp',hz,hc]
  rw [← joint_partition s β e m ha,← hp.integral_comp' (jointDensity r.symm β m (predecessorSeam e))]
  exact integral_congr_ae (ae_of_all _ fun z => (eqn z).symm)

def jointState (s : Sides) (β : ℝ) (e m : Flux) : Measure (JointSlice (rectShape s) (Fin (s μt))) :=
  (jointHaar _ _).tilted fun z => Real.log (jointDensity (finRotate _).symm β m (closingCut e) z)

theorem jointState_probability (s : Sides) (β : ℝ) (e m : Flux) (ha : 2 ≤ s μt) : IsProbabilityMeasure (jointState s β e m) := by
  apply isProbabilityMeasure_tilted
  simp only [Real.exp_log (jointDensity_pos _ _ _ _ _)]
  by_contra hn
  have eqn := closing_partition s β e m ha
  rw [integral_undef hn] at eqn
  exact (twistedPartition_pos β s _).ne' eqn.symm

theorem jointState_integral (s : Sides) (β : ℝ) (e m : Flux) (ha : 2 ≤ s μt)
    (F : JointSlice (rectShape s) (Fin (s μt)) → ℂ) :
    (∫ z, F z ∂jointState s β e m) =
      (twistedPartition β s (joinTwist e m))⁻¹ •
        ∫ z, (jointDensity (finRotate _).symm β m (closingCut e) z : ℂ) * F z ∂jointHaar _ _ := by
  rw [jointState,integral_tilted]
  simp only [Real.exp_log (jointDensity_pos _ _ _ _ _),closing_partition s β e m ha]
  rw [← integral_smul]
  apply integral_congr_ae
  filter_upwards with z
  simp only [Complex.real_smul,Complex.ofReal_div,div_eq_mul_inv,Complex.ofReal_mul,Complex.ofReal_inv]
  ring

open InfiniteLattice TheStatementsProvedTogether Matrices

/-- Both spatial and temporal link coordinates are carried to the joint layer
space before applying an observable. The cyclic origin may be chosen freely. -/
def physicalJointCoordinates (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side) :
    ReleasePairs Γ ≃ᵐ JointSlice (fun _ => Γ.side) (Fin Γ.side) :=
  (MeasurableEquiv.piCongrRight fun _ : ZMod Γ.side => (gaugeCoordinates Γ).prodCongr (linkCoordinates Γ)).trans
    (MeasurableEquiv.piCongrLeft (fun _ : Fin Γ.side => RectGauges (fun _ => Γ.side) × RectSlice (fun _ => Γ.side)) E.symm)

theorem physicalJointCoordinates_apply (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side)
    (p : ReleasePairs Γ) (t : Fin Γ.side) :
    physicalJointCoordinates Γ E p t = (readVertices Γ (p (E t)).1,readLinks Γ (p (E t)).2) := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let z (c : ZMod Γ.side) := (gaugeCoordinates Γ (p c).1,linkCoordinates Γ (p c).2)
  have h := MeasurableEquiv.piCongrLeft_apply_apply (β := fun _ : Fin Γ.side => RectGauges n × RectSlice n) E.symm z (E t)
  rw [Equiv.symm_apply_apply] at h
  exact h.trans (Prod.ext (gaugeCoordinates_apply Γ _) (linkCoordinates_apply Γ _))

theorem physicalJointCoordinates_preserving (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side) :
    MeasurePreserving (physicalJointCoordinates Γ E) (releasePairHaar Γ) (jointHaar _ (Fin Γ.side)) := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  apply (measurePreserving_piCongrLeft (fun _ : Fin Γ.side => (rectGaugeHaar n).prod (rectHaar n)) E.symm).comp
  exact measurePreserving_pi _ _ (fun _ => (gaugeCoordinates_preserving Γ).prod (linkCoordinates_preserving Γ))

theorem physicalJointCoordinates_density (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side)
    (hE : ∀ t, E (finRotate _ t) = E t + 1) (β : ℝ) (p : ReleasePairs Γ) :
    releasePairWeight Γ β p = (jointDensity (finRotate _).symm β zeroFlux (closingCut zeroFlux)
      (physicalJointCoordinates Γ E p) : ℂ) := by
  let r := finRotate Γ.side
  have prev (t : Fin Γ.side) : E (r.symm t) = E t - 1 := by
    have hh := hE (r.symm t)
    change E (r (r.symm t)) = _ at hh
    rw [Equiv.apply_symm_apply] at hh
    exact eq_sub_of_add_eq hh.symm
  unfold releasePairWeight jointDensity
  rw [← Equiv.prod_comp E,Complex.ofReal_prod]
  apply Finset.prod_congr rfl
  intro t _
  simp only [physicalJointCoordinates_apply,closingCut,ite_self,rectFlip_zero,Complex.ofReal_mul,Complex.ofReal_pow]
  rw [show E ((finRotate Γ.side).symm t) = _ from prev t,periodicHalfWeight_sq,← readLinks_gaugeAct,rectTemporal_readLinks]

/-- Translate a physical mark by its integer time before reading the joint
coordinates. This equality holds pointwise on each configuration. -/
theorem physical_shifted_jointMark (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side)
    (hE : ∀ t,E (finRotate _ t) = E t + 1) (K : ZMod Γ.side → WindowTest Γ) (k : ℤ) (z : ReleasePairs Γ) :
    (∏ c,K c (physicalWindow Γ z (c+Γ.levelClass k))) =
      jointMark (finRotate _).symm (fun t => K (E t-Γ.levelClass k)) (physicalJointCoordinates Γ E z) := by
  let r := finRotate Γ.side
  let eqv := E.trans (Equiv.subRight (Γ.levelClass k))
  have prev (t : Fin Γ.side) : E (r.symm t) = E t-1 := by
    have he := hE (r.symm t)
    change E (r (r.symm t)) = _ at he
    rw [Equiv.apply_symm_apply] at he
    exact eq_sub_of_add_eq he.symm
  rw [← eqv.prod_comp (fun c => K c (physicalWindow Γ z (c+Γ.levelClass k)))]
  unfold jointMark
  apply Finset.prod_congr rfl
  intro t _
  change K (E t-Γ.levelClass k) (physicalWindow Γ z (E t-Γ.levelClass k+Γ.levelClass k)) = _
  rw [sub_add_cancel]
  simp only [physicalJointCoordinates_apply,show E ((finRotate Γ.side).symm t) = _ from prev t]
  rfl


theorem physicalJoint_partition (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (E : Fin Γ.side ≃ ZMod Γ.side) (hE : ∀ t, E (finRotate _ t) = E t + 1) :
    Γ.lattice.partitionFunction β = twistedPartition β (fun _ => Γ.side) (joinTwist zeroFlux zeroFlux) := by
  let s : Sides := fun _ => Γ.side
  have hs := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp ⟨Γ.lattice,Γ.periods_eq⟩
  have e' : MeasurePreserving (releasePairCoordinates Γ) Γ.lattice.quotientHaar (releasePairHaar Γ) :=
    (cubic_torus_slice_decomposition Γ μt).2
  apply Complex.ofReal_injective
  calc
    _ = ∫ p, releasePairWeight Γ β p ∂releasePairHaar Γ := by
      rw [← e'.integral_comp' (releasePairWeight Γ β)]
      simp_rw [releasePairWeight_boltzmann Γ hβ]
      rw [integral_complex_ofReal]
      rfl
    _ = (∫ z : JointSlice (rectShape s) (Fin (s μt)), jointDensity (finRotate _).symm β zeroFlux (closingCut zeroFlux) z ∂jointHaar _ _ : ℝ) := by
      rw [← integral_complex_ofReal,← (physicalJointCoordinates_preserving Γ E).integral_comp' (fun z =>
        (jointDensity (finRotate _).symm β zeroFlux (closingCut zeroFlux) z : ℂ))]
      exact integral_congr_ae (ae_of_all _ (physicalJointCoordinates_density Γ E hE β))
    _ = _ := congrArg Complex.ofReal (closing_partition s β zeroFlux zeroFlux (by exact le_trans (by decide : 2 ≤ 3) hs))

/-- The release Gibbs expectation and the periodic joint expectation use the
same field, positive density, and normalizing constant. This holds for arbitrary
measurable functions of the lifted field, before choosing a slab expansion. -/
theorem physicalJoint_expectation (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (E : Fin Γ.side ≃ ZMod Γ.side) (hE : ∀ t, E (finRotate _ t) = E t + 1)
    (f : GaugeField 1 → ℂ) (hf : Measurable f) :
    (∫ U, f U ∂Γ.lattice.liftedGibbsMeasure β) =
      ∫ z, f (Γ.lattice.lift (fieldOfPairs Γ ((physicalJointCoordinates Γ E).symm z)))
        ∂jointState (fun _ => Γ.side) β zeroFlux zeroFlux := by
  let s : Sides := fun _ => Γ.side
  have hs := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp ⟨Γ.lattice,Γ.periods_eq⟩
  have ha : 2 ≤ s μt := le_trans (by decide : 2 ≤ 3) hs
  rw [liftedGibbs_integral_pairs Γ hβ f hf,jointState_integral s β zeroFlux zeroFlux ha,
    physicalJoint_partition Γ hβ E hE,ENNReal.toReal_inv,ENNReal.toReal_ofReal (twistedPartition_pos _ _ _).le]
  congr 1
  rw [← (physicalJointCoordinates_preserving Γ E).integral_comp' (fun z =>
    (jointDensity (finRotate _).symm β zeroFlux (closingCut zeroFlux) z : ℂ) *
    f (Γ.lattice.lift (fieldOfPairs Γ ((physicalJointCoordinates Γ E).symm z))))]
  apply integral_congr_ae
  filter_upwards with p
  rw [MeasurableEquiv.symm_apply_apply,physicalJointCoordinates_density Γ E hE]


def jointNeutralMean (s : Sides) (β : ℝ) (m : Flux) (F : JointSlice (rectShape s) (Fin (s μt)) → ℝ) : ℝ :=
  mixtureMean (fun e => twistedPartition β s (joinTwist e m)) (fun e => jointState s β e m) F

/-- MX for the same layers that carry the physical tests and the projected
marked trace. The periodic law has mixture weight at least one eighth. -/
theorem jointPeriodic_mean_sq (s : Sides) (ha : 2 ≤ s μt) {β : ℝ} (hβ : 0 ≤ β) (m : Flux)
    (F : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (hF : MemLp F 2 (jointState s β zeroFlux m)) :
    (∫ z, F z ∂jointState s β zeroFlux m)^2 ≤ 8 * jointNeutralMean s β m (fun z => (F z)^2) := by
  let w (e : Flux) := twistedPartition β s (joinTwist e m)
  let q (e : Flux) := ∫ z, F z ^ 2 ∂jointState s β e m
  letI := jointState_probability s β zeroFlux m ha
  have hw (e) : 0 < w e := twistedPartition_pos _ _ _
  have hq (e) : 0 ≤ q e := integral_nonneg fun z => sq_nonneg _
  have hs : 0 < ∑ e : Flux, w e := Finset.sum_pos (fun e _ => hw e) Finset.univ_nonempty
  have hu : (∑ e : Flux, w e) ≤ 8 * w zeroFlux := calc
    _ ≤ ∑ _ : Flux, w zeroFlux := Finset.sum_le_sum fun e _ => electric_untwist β s e m (fun χ => sectorWeight_nonneg ha hβ χ m)
    _ = _ := by norm_num [Fintype.card_prod]
  have hv := ProbabilityTheory.variance_nonneg F (jointState s β zeroFlux m)
  rw [ProbabilityTheory.variance_eq_sub hF] at hv
  refine (sub_nonneg.mp hv).trans ?_
  change q zeroFlux ≤ 8 * ((∑ e : Flux, w e * q e) / ∑ e : Flux, w e)
  rw [mul_div_assoc']
  apply (le_div_iff₀ hs).2
  calc
    _ ≤ q zeroFlux * (8 * w zeroFlux) := mul_le_mul_of_nonneg_left hu (hq _)
    _ = 8 * (w zeroFlux * q zeroFlux) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left
      (Finset.single_le_sum (fun e _ => mul_nonneg (hw e).le (hq e)) (Finset.mem_univ zeroFlux)) (by norm_num)


/-- The positive mixture has exactly the projected-trace partition function
as its denominator. The same formula applies to every measurable real observable. -/
theorem jointNeutralMean_weight (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (f : JointSlice (rectShape s) (Fin (s μt)) → ℝ) :
    (jointNeutralMean s β m f : ℂ) * (sectorWeight β s zeroFlux m : ℂ) =
      (1/8 : ℂ) * ∑ e : Flux, ∫ z, (jointDensity (finRotate _).symm β m (closingCut e) z : ℂ) * (f z : ℂ) ∂jointHaar _ _ := by
  let w (e : Flux) := twistedPartition β s (joinTwist e m)
  have hw (e) : 0 < w e := twistedPartition_pos _ _ _
  have hp : 0 < ∑ e : Flux, w e := Finset.sum_pos (fun e _ => hw e) Finset.univ_nonempty
  have hs : sectorWeight β s zeroFlux m = (∑ e : Flux, w e) / 8 := by
    simp only [sectorWeight,character_zero,Int.cast_one,one_mul,w]
  have he : jointNeutralMean s β m f * sectorWeight β s zeroFlux m =
      (∑ e : Flux, w e * ∫ z, f z ∂jointState s β e m) / 8 := by
    rw [hs]
    change _ / (∑ e : Flux, w e) * _ = _
    field_simp
    rfl
  have term (e : Flux) : ((w e * ∫ z, f z ∂jointState s β e m : ℝ) : ℂ) =
      ∫ z, (jointDensity (finRotate _).symm β m (closingCut e) z : ℂ) * (f z : ℂ) ∂jointHaar _ _ := by
    rw [Complex.ofReal_mul,← integral_complex_ofReal,jointState_integral s β e m ha,Complex.real_smul,
      Complex.ofReal_inv,← mul_assoc]
    change ((w e : ℂ) * (w e : ℂ)⁻¹) * _ = _
    rw [mul_inv_cancel₀ (Complex.ofReal_ne_zero.mpr (hw e).ne'),one_mul]
  rw [← Complex.ofReal_mul,he,Complex.ofReal_div,Complex.ofReal_sum]
  simp_rw [term]
  push_cast
  ring


def relabelJoint {I : Type} [Fintype I] {n : spatialAxis → ℕ} (e : Equiv.Perm I) :
    JointSlice n I ≃ᵐ JointSlice n I := MeasurableEquiv.piCongrLeft (fun _ : I => RectGauges n × RectSlice n) e

theorem relabelJoint_apply (e : Equiv.Perm I) (z : JointSlice n I) (i : I) : relabelJoint e z (e i) = z i :=
  MeasurableEquiv.piCongrLeft_apply_apply (β := fun _ : I => RectGauges n × RectSlice n) e z i

theorem relabelJoint_preserving (n : spatialAxis → ℕ) (e : Equiv.Perm I) :
    MeasurePreserving (relabelJoint (n := n) e) (jointHaar n I) (jointHaar n I) :=
  measurePreserving_piCongrLeft (fun _ : I => (rectGaugeHaar n).prod (rectHaar n)) e

theorem periodicDensity_relabel (σ e : Equiv.Perm I) (hc : Commute σ e) (β : ℝ) (m : Flux) (z : JointSlice n I) :
    jointDensity σ β m (fun _ => zeroFlux) (relabelJoint e z) = jointDensity σ β m (fun _ => zeroFlux) z := by
  have comm (i : I) : σ (e i) = e (σ i) := congrArg (fun f : Equiv.Perm I => f i) hc.eq
  unfold jointDensity
  rw [← Equiv.prod_comp e (fun c => (rectHalfWeight n β m ((relabelJoint e z) (σ c)).2)^2 *
    rectTemporal n β (((relabelJoint e z) (σ c)).2,rectGauge n (rectFlip zeroFlux ((relabelJoint e z) c).2,((relabelJoint e z) c).1)))]
  simp only [comm,relabelJoint_apply]

/-- The common periodic mean in the time-average argument follows from a
rotation of the actual periodic joint Haar coordinates. -/
theorem jointPeriodic_shift_mean (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (e : Equiv.Perm (Fin (s μt))) (he : Commute (finRotate _).symm e)
    (F : JointSlice (rectShape s) (Fin (s μt)) → ℝ) :
    (∫ z, F (relabelJoint e z) ∂jointState s β zeroFlux m) = ∫ z, F z ∂jointState s β zeroFlux m := by
  apply Complex.ofReal_injective
  rw [← integral_complex_ofReal,← integral_complex_ofReal,jointState_integral s β zeroFlux m ha,
    jointState_integral s β zeroFlux m ha]
  congr 1
  rw [← (relabelJoint_preserving (rectShape s) e).integral_comp' (fun z =>
    (jointDensity (finRotate _).symm β m (closingCut zeroFlux) z : ℂ) * (F z : ℂ))]
  have hz : closingCut (a := s μt) zeroFlux = fun _ => zeroFlux := by funext i; simp [closingCut]
  apply integral_congr_ae
  filter_upwards with z
  rw [hz,periodicDensity_relabel _ _ he]


/-- Time average of actual marked joint layers. Only the pairwise envelope and
the common periodic mean enter; the finite mixture and its factor eight are fixed. -/
theorem joint_window_comparison (s : Sides) (ha : 2 ≤ s μt) {β : ℝ} (hβ : 0 ≤ β) (m : Flux)
    {N : ℕ} (hN : 0 < N) (X : Fin N → JointSlice (rectShape s) (Fin (s μt)) → ℝ)
    (hX : ∀ e i, MemLp (X i) 2 (jointState s β e m)) {a A τ : ℝ}
    (hA : 0 ≤ A) (d : ℤ → ℝ) (hn : ∀ z, 0 ≤ d z) (hs : Summable d)
    (hmean : ∀ i, (∫ z, X i z ∂jointState s β zeroFlux m) = a)
    (hcov : ∀ i j : Fin N, jointNeutralMean s β m (fun z => X i z * X j z) ≤ A * (d ((j.val : ℤ)-i.val) + τ)) :
    |a| ≤ Real.sqrt (8 * A * ((∑' z,d z)/N+τ)) :=
  mixture_window_comparison _ _ (jointState_probability s β zeroFlux m ha) (jointPeriodic_mean_sq s ha hβ m)
    hN X hX hA d hn hs hmean hcov

theorem jointNeutralMean_centered_product (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (X Y : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (c : ℝ)
    (hx : ∀ e, MemLp X 2 (jointState s β e m)) (hy : ∀ e, MemLp Y 2 (jointState s β e m)) :
    jointNeutralMean s β m (fun z => (X z-c)*(Y z-c)) =
      jointNeutralMean s β m (fun z => X z*Y z) - c * jointNeutralMean s β m X - c * jointNeutralMean s β m Y + c^2 := by
  let w (e : Flux) := twistedPartition β s (joinTwist e m)
  let μ (e : Flux) := jointState s β e m
  have W : 0 < ∑ e,w e := Finset.sum_pos (fun e _ => twistedPartition_pos β s _) Finset.univ_nonempty
  have term (e : Flux) : (∫ z,(X z-c)*(Y z-c) ∂μ e) =
      (∫ z,X z*Y z ∂μ e) - c*(∫ z,X z ∂μ e) - c*(∫ z,Y z ∂μ e) + c^2 := by
    letI : IsProbabilityMeasure (μ e) := jointState_probability s β e m ha
    have h : Integrable (fun z => X z*Y z) (μ e) := (hx e).integrable_mul (hy e)
    have x : Integrable (fun z => c*X z) (μ e) := ((hx e).integrable (by norm_num)).const_mul c
    have y : Integrable (fun z => c*Y z) (μ e) := ((hy e).integrable (by norm_num)).const_mul c
    have xy : Integrable (fun z => X z*Y z-c*X z) (μ e) := h.sub x
    have xyz : Integrable (fun z => X z*Y z-c*X z-c*Y z) (μ e) := xy.sub y
    rw [show (fun z => (X z-c)*(Y z-c)) = fun z => X z*Y z - c*X z - c*Y z + c^2 from funext fun z => by ring,
      integral_add xyz (g := fun _ => c^2) (integrable_const _),integral_sub xy y,integral_sub h x,
      integral_const_mul,integral_const_mul,integral_const,probReal_univ,one_smul]
  unfold jointNeutralMean mixtureMean
  change (∑ e,w e*(∫ z,(X z-c)*(Y z-c) ∂μ e))/(∑ e,w e) = _
  simp_rw [term,mul_add,mul_sub]
  simp only [Finset.sum_add_distrib,Finset.sum_sub_distrib]
  have xc (f : Flux → ℝ) : (∑ e,w e*(c*f e)) = c*∑ e,w e*f e := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro e _
    ring
  rw [xc,xc,← Finset.sum_mul]
  change ((∑ e,w e*∫ z,X z*Y z ∂μ e)-c*(∑ e,w e*∫ z,X z ∂μ e)-c*(∑ e,w e*∫ z,Y z ∂μ e)+(∑ e,w e)*c^2)/(∑ e,w e) =
    (∑ e,w e*∫ z,X z*Y z ∂μ e)/(∑ e,w e) - c*((∑ e,w e*∫ z,X z ∂μ e)/(∑ e,w e)) -
      c*((∑ e,w e*∫ z,Y z ∂μ e)/(∑ e,w e)) + c^2
  field_simp [W.ne']
  <;> ring

/-- Single-window and double-window trace estimates imply the centered envelope
used for time averaging. The vacuum one-point value c may have either sign. -/
theorem joint_covariance_envelope (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (X Y : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (c : ℝ)
    (hx : ∀ e, MemLp X 2 (jointState s β e m)) (hy : ∀ e, MemLp Y 2 (jointState s β e m))
    {M K q τ : ℝ} (hM : 0 ≤ M) (hq : 0 ≤ q)
    (hs : |jointNeutralMean s β m X-c| ≤ M*τ) (ht : |jointNeutralMean s β m Y-c| ≤ M*τ)
    (hp : |jointNeutralMean s β m (fun z => X z*Y z)-c^2| ≤ K*(q+τ)) :
    jointNeutralMean s β m (fun z => (X z-c)*(Y z-c)) ≤ (K+2 * |c| * M)*(q+τ) := by
  let EX := jointNeutralMean s β m X
  let EY := jointNeutralMean s β m Y
  let P := jointNeutralMean s β m (fun z => X z*Y z)
  have low (x : ℝ) (hh : |x-c| ≤ M*τ) : -(abs c*(M*τ)) ≤ c*(x-c) := by
    calc
      _ ≤ -(abs c * abs (x-c)) := neg_le_neg (mul_le_mul_of_nonneg_left hh (abs_nonneg _))
      _ = -abs (c*(x-c)) := by rw [abs_mul]
      _ ≤ _ := neg_abs_le _
  have hP : P-c^2 ≤ K*(q+τ) := (le_abs_self _).trans hp
  rw [jointNeutralMean_centered_product s ha β m X Y c hx hy]
  change P-c*EX-c*EY+c^2 ≤ _
  nlinarith only [hP,low EX hs,low EY ht,mul_nonneg (mul_nonneg (abs_nonneg c) hM) hq]


/-- Rotating a jointly marked field by an integral displacement amounts to
subtracting that displacement from every residue label. -/
theorem translated_residue_rotation {V : ℕ} (E : Fin V ≃ ZMod V) (hE : ∀ i,E (finRotate _ i) = E i+1)
    (t : ZMod V) : ∃ e : Equiv.Perm (Fin V), Commute (finRotate _).symm e ∧ ∀ i,E (e i) = E i-t := by
  let e := (E.trans (Equiv.subRight t)).trans E.symm
  have act (i : Fin V) : E (e i) = E i-t := E.apply_symm_apply _
  have prev (i : Fin V) : E ((finRotate _).symm i) = E i-1 := by
    have h := hE ((finRotate _).symm i)
    rw [Equiv.apply_symm_apply] at h
    exact eq_sub_of_add_eq h.symm
  refine ⟨e,Equiv.ext fun i => E.injective ?_,act⟩
  change E ((finRotate _).symm (e i)) = E (e ((finRotate _).symm i))
  rw [prev,act,act,prev]
  abel

/-- Every pair of distinct copies in the periodic time average fits with a
blank closing seam, an opposite half-circle and a near arc at least the
difference of the copy indices. The width is fixed before taking the volume. -/
theorem time_average_placement {V w : ℕ} (i j : Fin (V/(2*(w+1)))) (hij : i.val < j.val) :
    let start (t : ℕ) := 1+t*(w+1)
    ∃ d a : ℕ, V = start i.val+w+d+w+a ∧ start j.val = start i.val+w+d ∧
      j.val-i.val ≤ d ∧ V/2 ≤ a := by
  let start (t : ℕ) := 1+t*(w+1)
  obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le (Nat.succ_le_of_lt hij)
  let d := 1+k*(w+1)
  have sep : start j.val = start i.val+w+d := by rw [hk]; dsimp [start,d]; ring
  have fits : 2*(start j.val+w) ≤ V := calc
    _ = (j.val+1)*(2*(w+1)) := by dsimp [start]; ring
    _ ≤ V/(2*(w+1))*(2*(w+1)) := Nat.mul_le_mul_right _ j.isLt
    _ ≤ _ := Nat.div_mul_le_self _ _
  have lower : k ≤ k*(w+1) := Nat.le_mul_of_pos_right k (by omega)
  change ∃ d a : ℕ,V = start i.val+w+d+w+a ∧ start j.val = start i.val+w+d ∧ j.val-i.val ≤ d ∧ V/2 ≤ a
  refine ⟨d,V-(start j.val+w),by rw [← sep]; omega,sep,?_,by omega⟩
  dsimp [d]
  omega


theorem weighted_window_bound {J : Type*} [Fintype J] (w x c : J → ℂ) (C : J → ℝ) (E : ℝ)
    (h : ∀ j,‖x j-c j‖ ≤ C j*E) :
    ‖(∑ j,w j*x j)-(∑ j,w j*c j)‖ ≤ (∑ j,‖w j‖*C j)*E := by
  rw [← Finset.sum_sub_distrib,Finset.sum_mul]
  apply (norm_sum_le _ _).trans
  apply Finset.sum_le_sum
  intro j _
  rw [← mul_sub,norm_mul,mul_assoc]
  exact mul_le_mul_of_nonneg_left (h j) (norm_nonneg _)

/-- The product of the two norm budgets controls the whole finite polynomial.
Its dependence on the word labels factors before choosing the separation. -/
theorem weighted_window_pair_bound {J K : Type*} [Fintype J] [Fintype K]
    (u : J → ℂ) (v : K → ℂ) (x : J → K → ℂ) (f : J → ℂ) (g : K → ℂ) (C : J → ℝ) (D : K → ℝ) (E : ℝ)
    (h : ∀ j k,‖x j k-f j*g k‖ ≤ (C j*D k)*E) :
    ‖(∑ p : J×K,(u p.1*v p.2)*x p.1 p.2)-(∑ j,u j*f j)*(∑ k,v k*g k)‖ ≤
      (∑ j,‖u j‖*C j)*(∑ k,‖v k‖*D k)*E := by
  have hb := weighted_window_bound (fun p : J×K => u p.1*v p.2) (fun p => x p.1 p.2)
    (fun p => f p.1*g p.2) (fun p => C p.1*D p.2) E (fun p => h p.1 p.2)
  have prod {A : Type} [CommSemiring A] (u f : J → A) (v g : K → A) :
      (∑ p : J×K,(u p.1*v p.2)*(f p.1*g p.2)) = (∑ j,u j*f j)*(∑ k,v k*g k) := by
    rw [Fintype.sum_prod_type,Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro j _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k _
    ring
  simp only [norm_mul] at hb
  rw [prod u f v g,prod (fun j => ‖u j‖) C (fun k => ‖v k‖) D] at hb
  exact hb

/-- A complex vacuum value in the marked expansion supplies a real centering
constant for the probability estimate. The one-point error bounds its imaginary part. -/
theorem real_vacuum_errors (x p : ℝ) (c : ℂ) {A E T : ℝ} (hc : ‖c‖ ≤ A)
    (hx : ‖(x : ℂ)-c‖ ≤ T) (hp : ‖(p : ℂ)-c^2‖ ≤ E) :
    |x-c.re| ≤ T ∧ |p-c.re^2| ≤ E+A*T := by
  have re := (Complex.abs_re_le_norm ((x:ℂ)-c)).trans hx
  have im := (Complex.abs_im_le_norm ((x:ℂ)-c)).trans hx
  have im' : |c.im| ≤ T := by simpa only [Complex.sub_im,Complex.ofReal_im,zero_sub,abs_neg] using im
  have imA := (Complex.abs_im_le_norm c).trans hc
  have sq : c.im^2 ≤ A*T := by
    rw [← sq_abs,pow_two]
    exact mul_le_mul imA im' (abs_nonneg _) ((norm_nonneg c).trans hc)
  have pp := (Complex.abs_re_le_norm ((p:ℂ)-c^2)).trans hp
  simp only [Complex.sub_re,Complex.ofReal_re,pow_two,Complex.mul_re] at pp
  refine ⟨re,?_⟩
  calc
    _ = |(p-(c.re*c.re-c.im*c.im))-c.im^2| := by congr 1; ring
    _ ≤ |p-(c.re*c.re-c.im*c.im)| + |c.im^2| := abs_sub _ _
    _ ≤ _ := add_le_add pp (by rw [abs_of_nonneg (sq_nonneg _)]; exact sq)


/-- The periodic expectations of both separate physical slabs and their
product must be compared to the same vacuum expectations. The coefficient
on the connected vacuum term survives this conversion without a loss. -/
theorem periodic_covariance_of_three_means (P X Y p x y : ℂ) {E T A B D₁ D₂ D₃ : ℝ}
    (hX : ‖X‖ ≤ A) (hy : ‖y‖ ≤ B)
    (hp : ‖P-p‖ ≤ D₁*T) (hx : ‖X-x‖ ≤ D₂*T) (hy' : ‖Y-y‖ ≤ D₃*T)
    (hc : ‖p-x*y‖ ≤ E) :
    ‖P-X*Y‖ ≤ E + (D₁+B*D₂+A*D₃)*T := by
  have h0 : 0 ≤ A := (norm_nonneg _).trans hX
  have first : ‖(X-x)*y‖ ≤ (D₂*T)*B := by
    rw [norm_mul]
    exact mul_le_mul hx hy (norm_nonneg _) ((norm_nonneg _).trans hx)
  have second : ‖X*(Y-y)‖ ≤ A*(D₃*T) := by
    rw [norm_mul]
    exact mul_le_mul hX hy' (norm_nonneg _) h0
  have decomp : P-X*Y = ((P-p)+(p-x*y))-((X-x)*y+X*(Y-y)) := by ring
  rw [decomp]
  calc
    _ ≤ ‖(P-p)+(p-x*y)‖+‖(X-x)*y+X*(Y-y)‖ := norm_sub_le _ _
    _ ≤ (‖P-p‖+‖p-x*y‖)+(‖(X-x)*y‖+‖X*(Y-y)‖) := add_le_add (norm_add_le _ _) (norm_add_le _ _)
    _ ≤ (D₁*T+E)+((D₂*T)*B+A*(D₃*T)) := add_le_add (add_le_add hp hc) (add_le_add first second)
    _ = _ := by ring


/-- The finite volume error in EV-L(c) at the actual positive periodic state.
The common periodic mean of the rotated copies is automatic. In the envelope,
τ may be the opposite half-circle's signed thermal mass. -/
theorem periodic_rotates_error (s : Sides) {β : ℝ} (hβ : 0 ≤ β) (m : Flux) (ha : 2 ≤ s μt)
    (G : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (c : ℝ) {N V width : ℕ}
    (hwidth : 0 < width) (hV : 4*width ≤ V) (hN : N = V / (2*width))
    (rot : Fin N → Equiv.Perm (Fin (s μt))) (hc : ∀ i, Commute (finRotate _).symm (rot i))
    (hG : ∀ e i, MemLp (fun z => G (relabelJoint (rot i) z)) 2 (jointState s β e m))
    {A τ q : ℝ} (hA : 0 ≤ A) (ht : 0 ≤ τ) (hq : 0 ≤ q) (hq' : q < 1)
    (hcov : ∀ i j : Fin N, jointNeutralMean s β m (fun z => (G (relabelJoint (rot i) z)-c)*(G (relabelJoint (rot j) z)-c)) ≤
      A * (q ^ ((j.val : ℤ) - i.val).natAbs + τ)) :
    |(∫ z, G z ∂jointState s β zeroFlux m) - c| ≤
      Real.sqrt (8*A*(1+4*width*(∑' z : ℤ, q^z.natAbs))) * Real.sqrt (1/(V:ℝ)+τ) := by
  let w := 2*width
  have hw : 0 < w := by dsimp [w]; omega
  have hNV : N*w ≤ V := hN ▸ Nat.div_mul_le_self V w
  have rem := Nat.mod_lt V hw
  have div := Nat.mod_add_div V w
  have hn : 0 < N := by
    rw [hN]
    exact Nat.div_pos (by omega) (by omega)
  have hVN : V ≤ 4*width*N := by
    change N = V / w at hN
    rw [← hN] at div
    have h1 : w ≤ w*N := Nat.le_mul_of_pos_right _ hn
    have he : 4*width*N = w*N + w*N := by unfold w; ring
    omega
  let X (i : Fin N) (z : JointSlice (rectShape s) (Fin (s μt))) := G (relabelJoint (rot i) z)-c
  letI (e : Flux) := jointState_probability s β e m ha
  have hX (e i) : MemLp (X i) 2 (jointState s β e m) := (hG e i).sub (memLp_const _)
  have mean (i : Fin N) : (∫ z, X i z ∂jointState s β zeroFlux m) = (∫ z, G z ∂jointState s β zeroFlux m) - c := by
    rw [show (∫ z, X i z ∂jointState s β zeroFlux m) = _ from integral_sub ((hG _ i).integrable (by norm_num)) (integrable_const c),
      integral_const,probReal_univ,one_smul,jointPeriodic_shift_mean s ha β m _ (hc i)]
  let D := ∑' z : ℤ,q^z.natAbs
  have hd : 0 ≤ D := tsum_nonneg fun _ => pow_nonneg hq _
  have hh := joint_window_comparison s ha hβ m hn X hX hA _ (fun _ => pow_nonneg hq _) (summable_time_decay hq hq') mean hcov
  have vn : 0 < (V : ℝ) := by exact_mod_cast (show 0 < V by omega)
  have nn : 0 < (N : ℝ) := by exact_mod_cast hn
  have ww : 0 ≤ (width : ℝ) := by positivity
  have hh' : (V : ℝ) ≤ 4*(width : ℝ)*(N : ℝ) := by exact_mod_cast hVN
  have he : D/(N:ℝ) ≤ (4*(width:ℝ)*D)/(V:ℝ) := by
    apply (div_le_div_iff₀ nn vn).2
    nlinarith only [mul_le_mul_of_nonneg_left hh' hd]
  apply hh.trans
  rw [← Real.sqrt_mul (mul_nonneg (mul_nonneg (by norm_num) hA) (by positivity : 0 ≤ 1+4*(width:ℝ)*D))]
  apply Real.sqrt_le_sqrt
  change 8*A*(D/N+τ) ≤ (8*A*(1+4*(width:ℝ)*D))*(1/V+τ)
  rw [mul_assoc (8*A)]
  apply mul_le_mul_of_nonneg_left _ (mul_nonneg (by norm_num) hA)
  nlinarith only [he,one_div_nonneg.mpr vn.le,mul_nonneg (mul_nonneg ww hd) ht,
    show (4*(width:ℝ)*D)/(V:ℝ) = (4*(width:ℝ)*D)*(1/V) by ring]


theorem jointNeutralMean_le_bound (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (f : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (C : ℝ)
    (hi : ∀ e,Integrable f (jointState s β e m)) (h : ∀ z,f z ≤ C) : jointNeutralMean s β m f ≤ C := by
  let w (e : Flux) := twistedPartition β s (joinTwist e m)
  have hw (e) : 0 < w e := twistedPartition_pos β s _
  have sumpos : 0 < ∑ e,w e := Finset.sum_pos (fun e _ => hw e) Finset.univ_nonempty
  change (∑ e,w e*(∫ z,f z ∂jointState s β e m))/(∑ e,w e) ≤ C
  apply (div_le_iff₀ sumpos).2
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro e _
  letI := jointState_probability s β e m ha
  rw [mul_comm C]
  apply mul_le_mul_of_nonneg_left _ (hw e).le
  have bound := integral_mono (hi e) (integrable_const C) h
  simpa only [integral_const,probReal_univ,one_smul] using bound

/-- EV-L for a bounded physical polynomial once its one-word trace and the
distinct-copy traces have been identified. Coincident copies require only
the pointwise bound; the vacuum scalar may be complex. -/
theorem periodic_polynomial_comparison (s : Sides) {β : ℝ} (hβ : 0 ≤ β) (m : Flux) (ha : 2 ≤ s μt)
    (G : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (c : ℂ) {N V width : ℕ}
    (hwidth : 0 < width) (hV : 4*width ≤ V) (hN : N = V / (2*width))
    (rot : Fin N → Equiv.Perm (Fin (s μt))) (comm : ∀ i,Commute (finRotate _).symm (rot i))
    (hG : ∀ e i,MemLp (fun z => G (relabelJoint (rot i) z)) 2 (jointState s β e m))
    {B M D τ q : ℝ} (hB : 0 ≤ B) (hb : ∀ z,|G z| ≤ B) (hc : ‖c‖ ≤ B)
    (hM : 0 ≤ M) (hD : 0 ≤ D) (ht : 0 ≤ τ) (hq : 0 ≤ q) (hq' : q < 1)
    (single : ∀ i,‖(jointNeutralMean s β m (fun z => G (relabelJoint (rot i) z)) : ℂ)-c‖ ≤ M*τ)
    (pair : ∀ i j : Fin N,i ≠ j → ‖(jointNeutralMean s β m (fun z => G (relabelJoint (rot i) z)*G (relabelJoint (rot j) z)) : ℂ)-c^2‖ ≤
      D*(q^((j.val : ℤ)-i.val).natAbs+τ)) :
    let A := D+3*B*M+4*B^2
    |(∫ z,G z ∂jointState s β zeroFlux m)-c.re| ≤
      Real.sqrt (8*A*(1+4*width*(∑' z : ℤ,q^z.natAbs))) * Real.sqrt (1/(V:ℝ)+τ) := by
  let A := D+3*B*M+4*B^2
  let X (i : Fin N) z := G (relabelJoint (rot i) z)
  have nn : 0 ≤ A := by dsimp [A]; positivity
  apply periodic_rotates_error s hβ m ha G c.re hwidth hV hN rot comm hG nn ht hq hq'
  intro i j
  have rc : |c.re| ≤ B := (Complex.abs_re_le_norm _).trans hc
  by_cases eq : i = j
  · subst j
    have diag := jointNeutralMean_le_bound s ha β m (fun z => (X i z-c.re)*(X i z-c.re)) (4*B^2) (fun e => by
      letI := jointState_probability s β e m ha
      have hh := (hG e i).sub (memLp_const c.re)
      exact hh.integrable_mul hh) (fun z => by
        have hh := (abs_sub (X i z) c.re).trans (add_le_add (hb _) rc)
        have := mul_self_le_mul_self (abs_nonneg _) hh
        rw [abs_mul_abs_self] at this
        nlinarith only [this])
    simp only [sub_self,Int.natAbs_zero,pow_zero]
    apply diag.trans
    have extra : 0 ≤ D+3*B*M := by positivity
    nlinarith only [extra,mul_nonneg nn ht,show A = D+3*B*M+4*B^2 from rfl]
  · let d := q^((j.val : ℤ)-i.val).natAbs
    have hd : 0 ≤ d := pow_nonneg hq _
    have err := real_vacuum_errors _ _ c hc (single i) (pair i j eq)
    have one (k : Fin N) : |jointNeutralMean s β m (X k)-c.re| ≤ M*τ :=
      (Complex.abs_re_le_norm ((jointNeutralMean s β m (X k) : ℂ)-c)).trans (single k)
    have mixed : |jointNeutralMean s β m (fun z => X i z * X j z)-c.re^2| ≤ (D+B*M)*(d+τ) := by
      apply err.2.trans
      nlinarith only [mul_nonneg (mul_nonneg hB hM) hd]
    have h := joint_covariance_envelope s ha β m (X i) (X j) c.re (fun e => hG e i) (fun e => hG e j)
      hM hd (one i) (one j) mixed
    apply h.trans
    apply mul_le_mul_of_nonneg_right _ (add_nonneg hd ht)
    dsimp only [A]
    nlinarith only [mul_le_mul_of_nonneg_right rc hM,sq_nonneg B]


abbrev LayerMark (n : spatialAxis → ℕ) := C((RectSlice n × RectSlice n) × RectGauges n,ℂ)

def layerOperator (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) (F : LayerMark n) :=
  edgeOperator (rectHaar n) (testLayerMap n β m F)

theorem layerOperator_one (n : spatialAxis → ℕ) (β : ℝ) (m : Flux) :
    layerOperator n β m 1 = rectSymOperator n β m := by
  rw [rectSymOperator_eq]
  have he : (testLayerMap n β m 1 : RectSlice n × RectSlice n → ℂ) = rectSymEntry n β m := by
    funext z
    exact rectTestEntry_one n β m z.1 z.2
  unfold layerOperator edgeOperator
  congr 1

theorem layerOperator_commutes (β : ℝ) (m χ : Flux) {F : LayerMark n} (hF : CentreBlind F) :
    Commute (layerOperator n β m F) (rectProj n χ) := by
  let T := layerOperator n β m F
  change T * ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • rectTranslation n e) =
    ((1 / 8 : ℂ) • ∑ e, (character e χ : ℂ) • rectTranslation n e) * T
  have comm (e) : T * rectTranslation n e = rectTranslation n e * T := (rectTestOperator_commutes β m hF e).eq
  simp only [mul_smul_comm,smul_mul_assoc,Finset.mul_sum,Finset.sum_mul,comm]

def projectedLayer (n : spatialAxis → ℕ) (β top : ℝ) (m : Flux) (F : LayerMark n) :=
  ((top⁻¹ : ℝ) : ℂ) • (layerOperator n β m F * rectProj n zeroFlux)

def slabProduct (n : spatialAxis → ℕ) (β top : ℝ) (m : Flux) (F : List (LayerMark n)) :=
  (F.map (projectedLayer n β top m)).prod

theorem projectedLayer_one (n : spatialAxis → ℕ) (β top : ℝ) (m : Flux) :
    projectedLayer n β top m 1 = ((top⁻¹ : ℝ) : ℂ) • rectSector n β zeroFlux m := by
  simp only [projectedLayer,layerOperator_one,rectSector]

theorem rectProj_norm_le (n : spatialAxis → ℕ) (χ : Flux) : ‖rectProj n χ‖ ≤ 1 := by
  let P := rectProj n χ
  have h := CStarRing.norm_star_mul_self (x := P)
  rw [show star P = P from (rectProj_selfAdjoint n χ).star_eq,show P * P = P from rectProj_idempotent n χ] at h
  nlinarith only [h,norm_nonneg P]

theorem projectedLayer_bound (β : ℝ) (m : Flux) {top : ℝ} (ht : 0 < top)
    (h : ‖rectSymOperator n β m‖ = top) (F : LayerMark n) : ‖projectedLayer n β top m F‖ ≤ ‖F‖ := by
  have he : ‖layerOperator n β m F‖ ≤ ‖F‖ * top := h ▸ rectTestOperator_bound n β m F
  have hp := rectProj_norm_le n zeroFlux
  rw [projectedLayer,norm_smul,Complex.norm_real,Real.norm_eq_abs,abs_of_pos (inv_pos.mpr ht)]
  calc
    _ ≤ top⁻¹ * ((‖F‖ * top) * 1) := mul_le_mul_of_nonneg_left ((norm_mul_le _ _).trans
      (mul_le_mul he hp (norm_nonneg _) (mul_nonneg (norm_nonneg _) ht.le))) (inv_pos.mpr ht).le
    _ = _ := by field_simp

theorem slabProduct_bound (β : ℝ) (m : Flux) {top : ℝ} (ht : 0 < top)
    (h : ‖rectSymOperator n β m‖ = top) (F : List (LayerMark n)) :
    ‖slabProduct n β top m F‖ ≤ (F.map fun f => ‖f‖).prod := by
  induction F with
  | nil =>
    exact ContinuousLinearMap.norm_id_le
  | cons f fs ih =>
    change ‖projectedLayer n β top m f * slabProduct n β top m fs‖ ≤ ‖f‖ * _
    exact (norm_mul_le _ _).trans (mul_le_mul (projectedLayer_bound β m ht h f) ih (norm_nonneg _) (norm_nonneg f))

/-- The ordered projected product has exactly one copy of the electric
projector at every positive length. No invertibility assumption on the kernels is used. -/
theorem slabProduct_factor (β top : ℝ) (m : Flux) (F : List (LayerMark n)) (hb : ∀ f ∈ F,CentreBlind f) :
    slabProduct n β top m F = (((top⁻¹ : ℝ) : ℂ) ^ F.length) •
      ((F.map (layerOperator n β m)).prod * (rectProj n zeroFlux) ^ F.length) := by
  induction F with
  | nil => simp [slabProduct]
  | cons f fs ih =>
    let P := rectProj n zeroFlux
    let X := (fs.map (layerOperator n β m)).prod
    have hs (g) (hg : g ∈ fs) := hb g (List.mem_cons_of_mem _ hg)
    have hc : Commute P X := by
      apply Commute.list_prod_right
      intro M hM
      obtain ⟨g,hg,rfl⟩ := List.mem_map.mp hM
      exact (layerOperator_commutes β m zeroFlux (hs _ hg)).symm
    change projectedLayer n β top m f * slabProduct n β top m fs = _
    rw [ih hs]
    simp only [projectedLayer,smul_mul_assoc,mul_smul_comm,smul_smul,List.length_cons,List.map_cons,List.prod_cons,pow_succ']
    congr 1
    · ring
    · change layerOperator n β m f * P * (X * P ^ fs.length) = layerOperator n β m f * X * (P * P ^ fs.length)
      rw [mul_assoc,← mul_assoc P X,hc.eq]
      simp only [mul_assoc]

/-- Extract an interval of unmarked edges directly from the temporal array. -/
theorem ofFn_empty_arc {α : Type*} [One α] {N : ℕ} (F : Fin N → α) (start len : ℕ)
    (h : start+len ≤ N) (blank : ∀ i : Fin N, start ≤ i.val → i.val < start+len → F i = 1) :
    ((List.ofFn F).drop start).take len = List.replicate len 1 := by
  apply List.ext_getElem
  · simp only [List.length_take,List.length_drop,List.length_ofFn,List.length_replicate]
    omega
  · intro i hi hi'
    simp only [List.getElem_take,List.getElem_drop,List.getElem_ofFn,List.getElem_replicate]
    apply blank <;> simp_all only [List.length_replicate] <;> omega

/-- A pair of supports separated by empty arcs yields exactly the ordered word
taken by the neutral trace estimate, including short or empty marked blocks. -/
theorem ofFn_split_windows {α : Type*} [One α] {N : ℕ} (F : Fin N → α) (u d w a : ℕ)
    (hn : N = u+d+w+a)
    (middle : ∀ i : Fin N, u ≤ i.val → i.val < u+d → F i = 1)
    (far : ∀ i : Fin N,u+d+w ≤ i.val → F i = 1) :
    ∃ U W : List α, U.length = u ∧ W.length = w ∧
      List.ofFn F = U ++ List.replicate d 1 ++ W ++ List.replicate a 1 := by
  let l := List.ofFn F
  let U := l.take u
  let M := (l.drop u).take d
  let W := (l.drop (u+d)).take w
  let tail := l.drop (u+d+w)
  have hl : l.length = N := List.length_ofFn
  have hu : U.length = u := by simp [U,hl]; omega
  have hw : W.length = w := by simp [W,hl]; omega
  have hm : M = List.replicate d 1 := ofFn_empty_arc F u d (by omega) middle
  have ht : tail = List.replicate a 1 := by
    have hh := ofFn_empty_arc F (u+d+w) a (by omega) (fun i hi _ => far i hi)
    have len : tail.length = a := by simp [tail,hl]; omega
    exact (List.take_of_length_le (by omega : tail.length ≤ a)).symm.trans hh
  refine ⟨U,W,hu,hw,?_⟩
  rw [← hm,← ht]
  change l = l.take u ++ (l.drop u).take d ++ (l.drop (u+d)).take w ++ l.drop (u+d+w)
  rw [List.append_assoc,List.append_assoc,← List.drop_drop (i := w) (j := u+d) (l := l),List.take_append_drop,← List.drop_drop (i := d) (j := u) (l := l),
    List.take_append_drop,List.take_append_drop]


/-- A residue-supported family gives identical marks at every translate of
its word that fits in the chosen circle chart, including directly before the seam. -/
theorem shifted_word_entry {α : Type*} [One α] {V w : ℕ} (F : ZMod V → α) (b : ZMod V)
    (hs : ∀ x,x ∉ Set.range (fun j : Fin w => b+(j.val : ZMod V)) → F x = 1)
    (start : ℕ) (fits : start+w ≤ V) (i : Fin V) :
    F (b+(i.val : ZMod V)-(start : ZMod V)) =
      if _h : start ≤ i.val ∧ i.val < start+w then F (b+((i.val-start : ℕ) : ZMod V)) else 1 := by
  by_cases h : start ≤ i.val ∧ i.val < start+w
  · rw [dif_pos h,Nat.cast_sub h.1,add_sub_assoc]
  · rw [dif_neg h]
    apply hs
    rintro ⟨j,hj⟩
    have eqn : (i.val : ZMod V) = ((start+j.val : ℕ) : ZMod V) := by
      push_cast
      linear_combination -hj
    have hlt : start+j.val < V := by omega
    have hh := congrArg ZMod.val eqn
    rw [ZMod.val_natCast_of_lt i.isLt,ZMod.val_natCast_of_lt hlt] at hh
    exact h ⟨by omega,by omega⟩

/-- Read a fixed-length word at an arbitrary offset in the ordered trace. -/
theorem ofFn_word_segment {α : Type*} {V w : ℕ} (F : Fin V → α) (U : Fin w → α)
    (s : ℕ) (fits : s+w ≤ V)
    (entry : ∀ j : Fin w,F ⟨s+j.val,by omega⟩ = U j) :
    ((List.ofFn F).drop s).take w = List.ofFn U := by
  apply List.ext_getElem
  · simp only [List.length_take,List.length_drop,List.length_ofFn]
    omega
  · intro j hj hk
    simp only [List.getElem_take,List.getElem_drop,List.getElem_ofFn]
    exact entry ⟨j,by simpa only [List.length_ofFn] using hk⟩

/-- Two disjoint translates of fixed residue-supported families produce the
same two finite words at all such placements. Both the leading and trailing
unused arcs appear explicitly. -/
theorem cyclic_two_words {α : Type*} [MulOneClass α] {V u w : ℕ} (F G : ZMod V → α) (b c : ZMod V)
    (hf : ∀ x,x ∉ Set.range (fun j : Fin u => b+(j.val : ZMod V)) → F x = 1)
    (hg : ∀ x,x ∉ Set.range (fun j : Fin w => c+(j.val : ZMod V)) → G x = 1)
    (l d a : ℕ) (volume : V = l+u+d+w+a) :
    List.ofFn (fun i : Fin V => F (b+(i.val : ZMod V)-(l : ZMod V)) *
      G (c+(i.val : ZMod V)-((l+u+d : ℕ) : ZMod V))) =
      (List.replicate l 1 ++ List.ofFn (fun j : Fin u => F (b+(j.val : ZMod V)))) ++
      List.replicate d 1 ++ List.ofFn (fun j : Fin w => G (c+(j.val : ZMod V))) ++ List.replicate a 1 := by
  let s := l+u+d
  let H (i : Fin V) := F (b+(i.val : ZMod V)-(l : ZMod V)) * G (c+(i.val : ZMod V)-(s : ZMod V))
  let Hs := List.ofFn H
  have hlen : Hs.length = V := List.length_ofFn
  have hf' (i : Fin V) := shifted_word_entry F b hf l (by omega) i
  have hg' (i : Fin V) := shifted_word_entry G c hg s (by dsimp [s]; omega) i
  have hleft := ofFn_empty_arc H 0 l (by omega) (fun i _ hi => by
    dsimp only [H]
    rw [hf',hg',dif_neg (by omega),dif_neg (by dsimp [s]; omega),one_mul])
  have hu := ofFn_word_segment H (fun j : Fin u => F (b+(j.val : ZMod V))) l (by omega) (fun j => by
    simp only [H,hf',hg',Fin.val_mk]
    rw [dif_pos (by omega),dif_neg (by dsimp [s]; omega),mul_one,Nat.add_sub_cancel_left])
  have hm := ofFn_empty_arc H (l+u) d (by omega) (fun i hi hi' => by
    dsimp only [H]
    rw [hf',hg',dif_neg (by omega),dif_neg (by dsimp [s]; omega),one_mul])
  have hw := ofFn_word_segment H (fun j : Fin w => G (c+(j.val : ZMod V))) s (by dsimp [s]; omega) (fun j => by
    simp only [H,hf',hg',Fin.val_mk]
    rw [dif_neg (by dsimp [s]; omega),dif_pos (by omega),one_mul,Nat.add_sub_cancel_left])
  have tail := ofFn_empty_arc H (s+w) a (by dsimp [s]; omega) (fun i hi _ => by
    dsimp only [H]
    rw [hf',hg',dif_neg (by dsimp [s] at hi; omega),dif_neg (by omega),one_mul])
  have ht : Hs.drop (s+w) = List.replicate a 1 := by
    have len : (Hs.drop (s+w)).length ≤ a := by simp only [List.length_drop,hlen]; dsimp [s]; omega
    exact (List.take_of_length_le len).symm.trans tail
  simp only [List.drop_zero] at hleft
  change Hs = _
  rw [← hleft,← hu,← hm,← hw,← ht]
  change Hs = (Hs.take l ++ (Hs.drop l).take u) ++ (Hs.drop (l+u)).take d ++ (Hs.drop s).take w ++ Hs.drop (s+w)
  simp only [List.append_assoc]
  rw [← List.drop_drop (i := w) (j := s) (l := Hs),List.take_append_drop,show s = l+u+d from rfl,
    ← List.drop_drop (i := d) (j := l+u) (l := Hs),List.take_append_drop,← List.drop_drop (i := u) (j := l) (l := Hs),List.take_append_drop,List.take_append_drop]


def rawMarkedMean (β : ℝ) (m : Flux) {a : ℕ} (F : Fin a → LayerMark n) : ℂ :=
  (1/8 : ℂ) * ∑ e : Flux, ∫ z, (jointDensity (finRotate _).symm β m (closingCut e) z : ℂ) *
    jointMark (finRotate _).symm F z ∂jointHaar n (Fin a)

theorem jointNeutralMean_of_marks (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (f : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (F : Fin (s μt) → LayerMark (rectShape s))
    (he : ∀ z, (f z : ℂ) = jointMark (finRotate _).symm F z) :
    (jointNeutralMean s β m f : ℂ) = rawMarkedMean β m F / (sectorWeight β s zeroFlux m : ℂ) := by
  have hpos : 0 < sectorWeight β s zeroFlux m := by
    simp only [sectorWeight,character_zero,Int.cast_one,one_mul]
    exact div_pos (Finset.sum_pos (fun e _ => twistedPartition_pos β s _) Finset.univ_nonempty) (by norm_num)
  apply (eq_div_iff (Complex.ofReal_ne_zero.mpr hpos.ne')).2
  rw [jointNeutralMean_weight s ha β m]
  simp_rw [he]
  rfl

/-- Rotate marked layers in the same joint coordinates used by the periodic
mixture bound. Pointwise multiplication then represents the two rotated copies. -/
theorem jointMark_relabel (σ e : Equiv.Perm I) (hc : Commute σ e)
    (F : I → LayerMark n) (z : JointSlice n I) :
    jointMark σ F (relabelJoint e z) = jointMark σ (fun i => F (e i)) z := by
  have comm (i : I) : σ (e i) = e (σ i) := congrArg (fun f : Equiv.Perm I => f i) hc.eq
  unfold jointMark
  rw [← Equiv.prod_comp e (fun i => F i ((((relabelJoint e z) (σ i)).2,((relabelJoint e z) i).2),((relabelJoint e z) i).1))]
  simp only [comm,relabelJoint_apply]

theorem jointMark_mul (σ : Equiv.Perm I) (F G : I → LayerMark n) (z : JointSlice n I) :
    jointMark σ (fun i => F i * G i) z = jointMark σ F z * jointMark σ G z := by
  simp only [jointMark,ContinuousMap.mul_apply,Finset.prod_mul_distrib]

theorem jointNeutral_rotated_product (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (G H : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (F K : Fin (s μt) → LayerMark (rectShape s))
    (hf : ∀ z,(G z : ℂ) = jointMark (finRotate _).symm F z)
    (hk : ∀ z,(H z : ℂ) = jointMark (finRotate _).symm K z)
    (e e' : Equiv.Perm (Fin (s μt))) (he : Commute (finRotate _).symm e) (he' : Commute (finRotate _).symm e') :
    (jointNeutralMean s β m (fun z => G (relabelJoint e z) * H (relabelJoint e' z)) : ℂ) =
      rawMarkedMean β m (fun i => F (e i) * K (e' i)) / (sectorWeight β s zeroFlux m : ℂ) := by
  apply jointNeutralMean_of_marks s ha
  intro z
  rw [Complex.ofReal_mul,hf,hk,jointMark_relabel _ _ he,jointMark_relabel _ _ he',jointMark_mul]


theorem continuous_jointMark (σ : Equiv.Perm I) (F : I → LayerMark n) :
    Continuous (jointMark σ F) := by
  unfold jointMark
  apply continuous_finsetProd
  intro i _
  exact (F i).continuous.comp (by fun_prop)

/-- A real local polynomial may have a complex marked expansion. Its positive
neutral mean is the same finite linear combination of actual electric traces. -/
theorem jointNeutral_polynomial {J : Type*} [Fintype J] (s : Sides) (ha : 2 ≤ s μt) (β : ℝ) (m : Flux)
    (f : JointSlice (rectShape s) (Fin (s μt)) → ℝ) (w : J → ℂ)
    (F : J → Fin (s μt) → LayerMark (rectShape s))
    (repr : ∀ z,(f z : ℂ) = ∑ j,w j * jointMark (finRotate _).symm (F j) z) :
    (jointNeutralMean s β m f : ℂ) = (∑ j,w j * rawMarkedMean β m (F j)) / (sectorWeight β s zeroFlux m : ℂ) := by
  let σ := (finRotate (s μt)).symm
  let D (e : Flux) (z : JointSlice (rectShape s) (Fin (s μt))) := (jointDensity σ β m (closingCut e) z : ℂ)
  let M (j : J) := jointMark σ (F j)
  let μ := jointHaar (rectShape s) (Fin (s μt))
  letI : BorelSpace (RectGauges (rectShape s)) := Pi.borelSpace
  letI : BorelSpace (RectSlice (rectShape s)) := Pi.borelSpace
  letI : BorelSpace (RectGauges (rectShape s) × RectSlice (rectShape s)) := Prod.borelSpace
  letI : BorelSpace (JointSlice (rectShape s) (Fin (s μt))) := Pi.borelSpace
  have hi (e j) : Integrable (fun z => w j * (D e z * M j z)) μ :=
    (continuous_const.mul ((Complex.continuous_ofReal.comp (continuous_jointDensity σ β m (closingCut e))).mul
      (continuous_jointMark σ (F j)))).integrable_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)
  have term (e : Flux) : (∫ z,D e z*(f z : ℂ) ∂μ) = ∑ j,w j*(∫ z,D e z * M j z ∂μ) := by
    calc
      _ = ∫ z,∑ j,w j*(D e z * M j z) ∂μ := by
        apply integral_congr_ae
        filter_upwards with z
        rw [repr,Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        change D e z*(w j*M j z)=_
        ring
      _ = _ := by rw [integral_finsetSum _ (fun j _ => hi e j)]; simp_rw [integral_const_mul]
  have hp : 0 < sectorWeight β s zeroFlux m := by
    simp only [sectorWeight,character_zero,Int.cast_one,one_mul]
    exact div_pos (Finset.sum_pos (fun e _ => twistedPartition_pos β s _) Finset.univ_nonempty) (by norm_num)
  apply (eq_div_iff (Complex.ofReal_ne_zero.mpr hp.ne')).2
  rw [jointNeutralMean_weight s ha β m]
  change (1/8 : ℂ)*(∑ e : Flux,∫ z,D e z*(f z : ℂ) ∂μ) = ∑ j,w j*((1/8 : ℂ)*∑ e : Flux,∫ z,D e z*M j z ∂μ)
  simp_rw [term]
  rw [Finset.sum_comm,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [← Finset.mul_sum]
  ring

/-- The two rotated copies of a real smeared polynomial have pair labels in
the product of the original finite label sets, with multiplicative weights. -/
theorem rotated_polynomial_words {J K : Type*} [Fintype J] [Fintype K]
    (σ e e' : Equiv.Perm I) (he : Commute σ e) (he' : Commute σ e')
    (G H : JointSlice n I → ℝ) (u : J → ℂ) (v : K → ℂ) (F : J → I → LayerMark n) (A : K → I → LayerMark n)
    (hG : ∀ z,(G z : ℂ) = ∑ j,u j*jointMark σ (F j) z) (hH : ∀ z,(H z : ℂ) = ∑ k,v k*jointMark σ (A k) z)
    (z : JointSlice n I) :
    ((G (relabelJoint e z)*H (relabelJoint e' z) : ℝ) : ℂ) =
      ∑ p : J×K,(u p.1*v p.2)*jointMark σ (fun i => F p.1 (e i)*A p.2 (e' i)) z := by
  simp only [Complex.ofReal_mul,hG,hH,jointMark_relabel σ e he,jointMark_relabel σ e' he',Fintype.sum_prod_type,
    Finset.sum_mul,Finset.mul_sum,jointMark_mul]
  conv_lhs => rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro j _
  apply Finset.sum_congr rfl
  intro k _
  ring


open scoped InnerProductSpace in
theorem normalized_mark_trace {p : ℕ} (β top : ℝ) (m : Flux) (F : Fin (p+2) → LayerMark n)
    (hb : ∀ i,CentreBlind (F i)) (hcut : ∀ e u v g,F 0 ((u,rectFlip e v),g) = F 0 ((u,v),g))
    {I : Type*} (b : HilbertBasis I ℂ (Kernel.Space (rectHaar n))) :
    HasSum (fun i => ⟪b i,slabProduct n β top m (List.ofFn F) (b i)⟫_ℂ)
      ((((top⁻¹ : ℝ) : ℂ) ^ (p+2)) * rawMarkedMean β m F) := by
  let P := rectProj n zeroFlux
  let L := layerOperator n β m
  have facts (f) (hf : f ∈ List.ofFn F) : CentreBlind f := by
    obtain ⟨i,rfl⟩ := List.mem_ofFn.mp hf
    exact hb i
  have comm : Commute P (startLayers β m F) := by
    apply Commute.list_prod_right
    intro M hM
    obtain ⟨i,rfl⟩ := List.mem_ofFn.mp hM
    exact (layerOperator_commutes β m zeroFlux (hb i.succ)).symm
  have power : P ^ (p+2) = P := (show IsIdempotentElem P from rectProj_idempotent n zeroFlux).pow_eq (by omega)
  apply ((averaged_mark_trace β m F hcut b).mul_left (((top⁻¹ : ℝ) : ℂ) ^ (p+2))).congr_fun
  intro i
  rw [slabProduct_factor β top m _ facts,List.length_ofFn,power,ContinuousLinearMap.smul_apply,inner_smul_right]
  congr 2
  rw [← List.ofFn_comp',List.ofFn_succ,List.prod_cons]
  change (L (F 0) * startLayers β m F * P) (b i) = (L (F 0) * P * startLayers β m F) (b i)
  rw [mul_assoc,← comm.eq,← mul_assoc]


end MarkedTori


section Propagation

/-- Time is the fourth coordinate, including on rectangular spectator boxes. -/
def boxSides (R : Box) (a : ℕ) : Sides := ![R.x, R.y, R.z, a]

/-- The spatial sites and the operator are independent of the temporal period a. -/
def boxShape (R : Box) := rectShape (boxSides R 0)

theorem rectShape_boxSides (R : Box) (a : ℕ) : rectShape (boxSides R a) = boxShape R := by
  funext i
  rcases i with ⟨i,hi⟩
  fin_cases i <;> first | rfl | exact (hi rfl).elim

theorem boxSector_moments (R : Box) {a : ℕ} (ha : 2 ≤ a) {β : ℝ} (hβ : 0 ≤ β) (χ m : Flux) :
    HasSum (fun i : Wilson.PositiveSlot (rectSector (boxShape R) β χ m) => i.1.val ^ a)
      (sectorWeight β (boxSides R a) χ m) := by
  exact (congrArg (fun n : spatialAxis → ℕ => HasSum
    (fun i : Wilson.PositiveSlot (rectSector n β χ m) => i.1.val ^ a) (sectorWeight β (boxSides R a) χ m))
    (rectShape_boxSides R a)).mp (rectSector_moments (s := boxSides R a) ha hβ χ m)

/-- A natural-number list retains one slot per positive basis vector in each eigenspace. -/
def EncodesSlots {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] (T : H →L[ℂ] H)
    (v : ℕ → ℝ) : Prop :=
  ∃ enc : Wilson.PositiveSlot T → ℕ, Function.Injective enc ∧ (∀ i, v (enc i) = i.1.val) ∧
    ∀ j, j ∉ Set.range enc → v j = 0

open scoped InnerProductSpace in
/-- Encode the actual eigenspaces in natural slots, move a maximal slot to zero
and fill the unused entries with zeros. This also covers a zero sector. -/
theorem boxSector_labeledList (R : Box) {β : ℝ} (hβ : 0 ≤ β) (χ m : Flux) :
    ∃ v : ℕ → ℝ, EncodesSlots (rectSector (boxShape R) β χ m) v ∧ v 0 = ‖rectSector (boxShape R) β χ m‖ ∧ (∀ j, 0 ≤ v j) ∧
      (∀ j, v j ≤ v 0) ∧ ∀ a : ℕ, 2 ≤ a → HasSum (fun j => v j ^ a) (sectorWeight β (boxSides R a) χ m) := by
  classical
  let T := rectSector (boxShape R) β χ m
  let hc := rectSector_compact (boxShape R) β χ m
  let hp := rectSector_positive (boxShape R) hβ χ m
  obtain ⟨w,b,j,hj,he,h₀⟩ := exists_positive_slot_basis T hc hp
  have bound (i : Wilson.PositiveSlot T) : i.1.val ≤ ‖T‖ := by
    have hh := T.le_opNorm (b (j i))
    rw [he,norm_smul,b.orthonormal.norm_eq_one,mul_one,mul_one,Complex.norm_real,Real.norm_eq_abs,
      abs_of_pos i.1.property] at hh
    exact hh
  have mom (a : ℕ) (ha : 2 ≤ a) := boxSector_moments R ha hβ χ m
  by_cases hT : T = 0
  · have no (i : Wilson.PositiveSlot T) : False := i.1.property.not_ge (by simpa [hT] using bound i)
    refine ⟨0, ⟨fun i => (no i).elim,fun i => (no i).elim,fun i => (no i).elim,fun _ _ => rfl⟩,
      by change 0 = ‖T‖; rw [hT,norm_zero], fun _ => le_rfl, fun _ => le_rfl, fun a ha => ?_⟩
    have hz : HasSum (fun i : Wilson.PositiveSlot T => i.1.val ^ a) 0 :=
      hasSum_zero.congr_fun (fun i => (no i).elim)
    change HasSum (fun _ : ℕ => (0 : ℝ) ^ a) _
    rw [(mom a ha).unique hz,zero_pow (by omega : a ≠ 0)]
    exact hasSum_zero
  haveI : Nontrivial (Kernel.Space (rectHaar (boxShape R))) := by
    rcases subsingleton_or_nontrivial (Kernel.Space (rectHaar (boxShape R))) with h|h
    · exact (hT (Subsingleton.elim _ _)).elim
    · exact h
  have summ := (mom 2 (by decide)).summable
  haveI : Countable (Wilson.PositiveSlot T) := Set.countable_univ_iff.mp (by
    convert summ.countable_support using 1
    ext i
    simp [Function.mem_support, i.1.property.ne'])
  obtain ⟨ht,hte⟩ := Wilson.positive_top_eigenvalue T hc hp hT
  obtain ⟨t,hv⟩ := Wilson.nonzero_eigenvalue_has_slot T hc hp (by exact_mod_cast ht.ne') hte
  have hval : t.1.val = ‖T‖ := Complex.ofReal_injective hv
  obtain ⟨code,hcode⟩ := exists_injective_nat (Wilson.PositiveSlot T)
  let enc (i : Wilson.PositiveSlot T) : ℕ := Equiv.swap (code t) 0 (code i)
  have hinj : Function.Injective enc := (Equiv.swap _ _).injective.comp hcode
  let v : ℕ → ℝ := Function.extend enc (fun i => i.1.val) 0
  have on (i : Wilson.PositiveSlot T) : v (enc i) = i.1.val := hinj.extend_apply _ _ i
  have off (p : ℕ) (hh : p ∉ Set.range enc) : v p = 0 := Function.extend_apply' _ _ _ hh
  have hzero : v 0 = ‖T‖ := by
    have eh : enc t = 0 := Equiv.swap_apply_left _ _
    rw [← eh, on, hval]
  refine ⟨v,⟨enc,hinj,on,off⟩,hzero,fun p => ?_,fun p => ?_,fun a ha => ?_⟩
  · by_cases hh : p ∈ Set.range enc
    · obtain ⟨i,rfl⟩ := hh; rw [on]; exact i.1.property.le
    · rw [off p hh]
  · rw [hzero]
    by_cases hh : p ∈ Set.range enc
    · obtain ⟨i,rfl⟩ := hh; rw [on]; exact bound i
    · rw [off p hh]; exact norm_nonneg _
  · apply (hinj.hasSum_iff (fun p hh => by
        change v p ^ a = 0
        rw [off p hh,zero_pow (by omega : a ≠ 0)])).1
    change HasSum (fun i => v (enc i) ^ a) _
    exact (mom a ha).congr_fun (fun i => by rw [on])

theorem boxSector_list (R : Box) {β : ℝ} (hβ : 0 ≤ β) (χ m : Flux) :
    ∃ v : ℕ → ℝ, v 0 = ‖rectSector (boxShape R) β χ m‖ ∧ (∀ j, 0 ≤ v j) ∧
      (∀ j, v j ≤ v 0) ∧ ∀ a : ℕ, 2 ≤ a → HasSum (fun j => v j ^ a) (sectorWeight β (boxSides R a) χ m) := by
  obtain ⟨v,_,hv⟩ := boxSector_labeledList R hβ χ m
  exact ⟨v,hv⟩

theorem boxNeutral_norm_pos (R : Box) {β : ℝ} (hβ : 0 ≤ β) :
    0 < ‖rectSector (boxShape R) β zeroFlux zeroFlux‖ := by
  obtain ⟨v,ht,hn,hmax,hm⟩ := boxSector_list R hβ zeroFlux zeroFlux
  by_contra! h
  have hv (j) : v j = 0 := le_antisymm ((hmax j).trans (ht.trans_le h)) (hn j)
  have hz := (hm 2 le_rfl).tsum_eq
  simp only [hv,zero_pow (by decide : 2 ≠ 0), tsum_zero] at hz
  have hl := partition_div_eight_le_neutral β (boxSides R 2)
  rw [← hz] at hl
  exact (not_le_of_gt (div_pos (Wilson.partition_pos β _) (by norm_num))) hl


/-- The untwisted rectangular transfer and its electric-neutral restriction have
the same top. The factor eight comparing their partition functions disappears in
large integer moments. No choice of a Perron eigenfunction is needed. -/
theorem boxNeutral_norm (R : Box) {β : ℝ} (hβ : 0 ≤ β) :
    ‖rectSector (boxShape R) β zeroFlux zeroFlux‖ = ‖rectSymOperator (boxShape R) β zeroFlux‖ := by
  classical
  let n := boxShape R
  let T := rectSymOperator n β zeroFlux
  let P := rectProj n zeroFlux
  have hP : ‖P‖ ≤ 1 := by
    have hs := CStarRing.norm_star_mul_self (x := P)
    rw [(rectProj_selfAdjoint n zeroFlux).star_eq,rectProj_idempotent] at hs
    nlinarith only [hs,norm_nonneg P]
  have hn : ‖T * P‖ ≤ ‖T‖ := (norm_mul_le _ _).trans ((mul_le_mul_of_nonneg_left hP (norm_nonneg T)).trans_eq (mul_one _))
  apply le_antisymm hn
  obtain ⟨v,ht,hv,hmax,hm⟩ := boxSector_list R hβ zeroFlux zeroFlux
  let c := v 0
  have hc : 0 < c := (boxNeutral_norm_pos R hβ).trans_eq ht.symm
  have hs {a : ℕ} (ha : 2 ≤ a) : HasSum (fun i => (v i / c) ^ a) (sectorWeight β (boxSides R a) zeroFlux zeroFlux / c ^ a) := by
    simpa only [div_pow] using (hm a ha).div_const (c ^ a)
  let C := 8 * ∑' i, (v i / c) ^ 2
  by_contra! h
  have hbig : 1 < ‖T‖ / c := (one_lt_div hc).2 (ht.trans_lt h)
  obtain ⟨a,ha,hlarge⟩ := ((eventually_ge_atTop 3).and ((tendsto_pow_atTop_atTop_of_one_lt hbig) (eventually_gt_atTop C))).exists
  have hpow : 0 < c ^ a := pow_pos hc _
  have hT : T ≠ 0 := norm_pos_iff.mp (hc.trans (ht.trans_lt h))
  haveI : Nontrivial (Kernel.Space (rectHaar n)) := by
    rcases subsingleton_or_nontrivial (Kernel.Space (rectHaar n)) with h₁|h₁
    · exact (hT (Subsingleton.elim _ _)).elim
    · exact h₁
  have compact : IsCompactOperator T := Kernel.operator_compact (rectSymEntry_memLp n β zeroFlux)
  have pos := rectSymOperator_positive n hβ zeroFlux
  obtain ⟨hp,hEig⟩ := Wilson.positive_top_eigenvalue T compact pos hT
  obtain ⟨i,hi⟩ := Wilson.nonzero_eigenvalue_has_slot T compact pos (by exact_mod_cast hp.ne') hEig
  have htor : HasSum (fun i : Wilson.PositiveSlot T => i.1.val ^ a) (Wilson.partition β (boxSides R a)) := by
    apply Complex.hasSum_ofReal.mp
    have raw := Kernel.hasSum_cyclic (rectSymEntry_memLp n β zeroFlux) pos (by omega : 2 ≤ a)
    have hh := twistedPartition_eq_symCycle (boxSides R a) (by exact (show 2 ≤ a by omega)) β zeroFlux zeroFlux
    simp only [show joinTwist zeroFlux zeroFlux = fun _ => false from funext join_zero,twistedPartition_untwisted,rectFlip_zero,ite_self] at hh
    let F (n' : spatialAxis → ℕ) := ∫ u : Fin a → RectSlice n',
      ∏ t, rectSymKernel n' β zeroFlux (u t,u (finRotate a t)) ∂Measure.pi (fun _ => rectHaar n')
    change Wilson.partition β (boxSides R a) = F (rectShape (boxSides R a)) at hh
    have eqn : Wilson.partition β (boxSides R a) = F n := hh.trans (congrArg F (rectShape_boxSides R a))
    rw [eqn]
    let X := Kernel.Space (rectHaar n)
    let H (A : X →L[ℂ] X) := HasSum (fun i : Wilson.PositiveSlot A => ((i.1.val ^ a : ℝ) : ℂ)) ((F n : ℝ) : ℂ)
    apply (congrArg H (rectSymOperator_eq n β zeroFlux).symm).mp
    simpa only [H,F,rectSymEntry, Kernel.copies, ← Complex.ofReal_prod,integral_complex_ofReal] using raw
  have hbd : sectorWeight β (boxSides R a) zeroFlux zeroFlux / c ^ a ≤ ∑' i, (v i / c) ^ 2 :=
    hasSum_le (fun j => pow_le_pow_of_le_one (div_nonneg (hv _) hc.le) ((div_le_one hc).2 (hmax j)) (by omega))
      (hs (by omega : 2 ≤ a)) (hs (a := 2) le_rfl).summable.hasSum
  have hper := partition_div_eight_le_neutral β (boxSides R a)
  have hneut : Wilson.partition β (boxSides R a) ≤ 8 * sectorWeight β (boxSides R a) zeroFlux zeroFlux := by linarith
  change C < (‖T‖ / c) ^ a at hlarge
  refine (not_lt_of_ge ?_ hlarge)
  calc
    (‖T‖ / c) ^ a = i.1.val ^ a / c ^ a := by rw [Complex.ofReal_injective hi,div_pow]
    _ ≤ Wilson.partition β (boxSides R a) / c ^ a := div_le_div_of_nonneg_right
      ((htor.summable.le_tsum i (fun j _ => pow_nonneg j.1.property.le a)).trans_eq htor.tsum_eq) hpow.le
    _ ≤ (8 * sectorWeight β (boxSides R a) zeroFlux zeroFlux) / c ^ a := div_le_div_of_nonneg_right hneut hpow.le
    _ = 8 * (sectorWeight β (boxSides R a) zeroFlux zeroFlux / c ^ a) := by ring
    _ ≤ C := mul_le_mul_of_nonneg_left hbd (by norm_num)


section CubeTrace

open SpinHarmonics
open scoped InnerProductSpace

variable (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)

/-- The missing cubic gluing identity, with convergence and the actual electric
insertion. Here time has period a and each of the three spatial sides is Γ.side. -/
def CubicTraceIdentity (m : Flux) (a : ℕ) : Prop :=
  ∀ e : Flux, HasSum (fun i => (peterWeylEntry
    (magneticTransfer Γ hβ m ^ a * electricTranslation Γ e) i i).re)
    (twistedPartition β (boxSides (cube Γ.side) a) (joinTwist e m))

/-- This is the remaining cubic identification after the Haar and electric
witnesses have been identified. Both sides now use the release slice. -/
theorem cubicTraceIdentity_iff_kernelCycle (m : Flux) {a : ℕ} (ha : 2 ≤ a) :
    CubicTraceIdentity Γ hβ m a ↔ ∀ e : Flux, HasSum (fun i =>
      (peterWeylEntry (magneticTransfer Γ hβ m ^ a * electricTranslation Γ e) i i).re)
      (∫ u, ∏ t, releasedLayerKernel Γ a β m t (u t)
        (if t.val = 0 then centreShift Γ TimeAxis.timeIdx (cuts e) (u (finRotate _ t)) else u (finRotate _ t))
        ∂Measure.pi (fun _ => Matrices.ComplexMatrix2.haarPi (Γ.LinkOrbits TimeAxis.timeIdx))) := by
  have he : boxSides (cube Γ.side) a = cubeGrid Γ.side a := by funext i; fin_cases i <;> rfl
  simp only [CubicTraceIdentity, he, twistedPartition_eq_releasedCycle Γ ha]


/-- Fourier transformation of a convergent inserted trace gives exactly the
trace with the corresponding electric projection. -/
theorem projectedTrace_of_insertions (m χ : Flux) (a : ℕ) (ht : CubicTraceIdentity Γ hβ m a) :
    HasSum (fun i => (peterWeylEntry (magneticTransfer Γ hβ m ^ a * electricProj Γ χ) i i).re)
      (sectorWeight β (boxSides (cube Γ.side) a) χ m) := by
  let A := magneticTransfer Γ hβ m ^ a
  have entry (i : PeterWeylIndex (Γ.LinkOrbits TimeAxis.timeIdx)) :
      (peterWeylEntry (A * electricProj Γ χ) i i).re =
        (∑ e : Flux, (character e χ : ℝ) * (peterWeylEntry (A * electricTranslation Γ e) i i).re) / 8 := by
    unfold electricProj
    rw [mul_smul_comm, Finset.mul_sum]
    simp only [mul_smul_comm, peterWeylEntry, ContinuousLinearMap.smul_apply, ContinuousLinearMap.sum_apply,
      inner_smul_right, inner_sum]
    norm_num [Complex.mul_re, Complex.re_sum, Complex.im_sum, div_eq_mul_inv]
    <;> ring
  change HasSum (fun i => (peterWeylEntry (A * electricProj Γ χ) i i).re) _
  simp_rw [entry]
  exact (hasSum_sum (s := Finset.univ) (fun (e : Flux) _ => (ht e).mul_left (character e χ : ℝ))).div_const 8

/-- Positivity of the actual Fourier coefficient follows from gluing and commuting
with the indicated electric projection. -/
theorem sectorWeight_nonneg_of_insertions (m χ : Flux) (a : ℕ) (ht : CubicTraceIdentity Γ hβ m a)
    :
    0 ≤ sectorWeight β (boxSides (cube Γ.side) a) χ m := by
  let T := magneticTransfer Γ hβ m
  let P := electricProj Γ χ
  have hc := magneticTransfer_commutes_proj Γ hβ m χ
  have hT := magneticTransfer_positive Γ hβ m
  have htpos : T.IsPositive := (ContinuousLinearMap.isPositive_iff_complex T).2 (fun x => by
      change ((⟪T x, x⟫_ℂ : ℂ).re : ℂ) = ⟪T x, x⟫_ℂ ∧ 0 ≤ (⟪T x, x⟫_ℂ : ℂ).re
      rw [← hT.1 x x]
      exact ⟨(BoundedMultiplication.eq_ofReal_re_of_im_eq_zero (hT.2 x).2).symm, (hT.2 x).1⟩)
  have hs : T.adjoint = T := htpos.isSelfAdjoint.star_eq
  have hpow (n : ℕ) : (T ^ n).IsPositive := by
    refine Nat.twoStepInduction (by simpa only [pow_zero] using
      (ContinuousLinearMap.isPositive_one : (1 : Γ.SliceL2 TimeAxis.timeIdx →L[ℂ] Γ.SliceL2 TimeAxis.timeIdx).IsPositive))
      (by simpa only [pow_one] using htpos) (fun k hk _ => ?_) n
    have hk' := hk.adjoint_conj T
    change (T.adjoint * (T ^ k * T)).IsPositive at hk'
    rwa [hs, ← pow_succ, ← pow_succ'] at hk'
  have hpstar : P.adjoint = P := (electricProj_isSelfAdjoint Γ χ).star_eq
  have hi : P * P = P := by simpa [P] using electricProj_mul Γ χ χ
  have hpos := (hpow a).adjoint_conj P
  change (P.adjoint * (T ^ a * P)).IsPositive at hpos
  rw [hpstar, ← mul_assoc, ← (hc.pow_left a).eq, mul_assoc, hi] at hpos
  apply hasSum_le _ hasSum_zero (projectedTrace_of_insertions Γ hβ m χ a ht)
  intro i
  exact hpos.re_inner_nonneg_right (peterWeylVec i)

end CubeTrace

theorem kappaWeight_cross (β : ℝ) (R : Box) (i : Axis) (a b : ℕ) :
    kappaWeight β (boxSides (R.replace i b) a) =
      kappaWeight β (boxSides (R.replace i a) b) := by
  let j : Dir := match i with | .x => 0 | .y => 1 | .z => 2
  have h : boxSides (R.replace i b) a =
      boxSides (R.replace i a) b ∘ Equiv.swap (3 : Dir) j := by
    funext u
    cases i <;> fin_cases u <;> rfl
  rw [h, kappaWeight_permute]

/-- TW-T (S3) for every diagonal eigenvalue. Only the neutral periodic list
needs an a priori maximum. Untwisting and large integer moments bound every
other list by that same maximum. -/
theorem diagonal_values_le_periodic_top {β : ℝ} {R : Box} (v : Flux × ℕ → ℝ)
    (hn : ∀ i, 0 ≤ v i) (h0 : 0 < v (zeroFlux, 0))
    (hmax : ∀ i, v (zeroFlux, i) ≤ v (zeroFlux, 0))
    (hs : Summable (fun i : ℕ => v (zeroFlux, i) ^ 2))
    (ht : ∀ m a, 3 ≤ a → HasSum (fun i : ℕ => v (m, i) ^ a) (sectorWeight β (boxSides R a) m m))
    (hp : ∀ a, 3 ≤ a → ∀ (σ : Equiv.Perm Dir) (χ m : Flux), 0 ≤ sectorWeight β (boxSides R a ∘ σ) χ m)
    (p : Flux × ℕ) : v p ≤ v (zeroFlux, 0) := by
  let c := v (zeroFlux, 0)
  let q (m : Flux) (i : ℕ) := v (m, i) / c
  have hnq (m i) : 0 ≤ q m i := div_nonneg (hn _) h0.le
  have hs' : Summable (fun i => q zeroFlux i ^ 2) := by
    simpa only [q, div_pow] using hs.div_const (c ^ 2)
  have ht' (m a) (ha : 3 ≤ a) : HasSum (fun i => q m i ^ a) (sectorWeight β (boxSides R a) m m / c ^ a) := by
    simpa only [q, div_pow] using (ht m a ha).div_const (c ^ a)
  let C := 8 * ∑' i, q zeroFlux i ^ 2
  rcases p with ⟨m,i⟩
  by_contra! h
  have hq : 1 < q m i := (one_lt_div h0).2 h
  have hlarge := (tendsto_pow_atTop_atTop_of_one_lt hq) (eventually_gt_atTop C)
  obtain ⟨a, ha, hh⟩ := ((eventually_ge_atTop 3).and hlarge).exists
  have hc : 0 < c ^ a := pow_pos h0 a
  have hb : sectorWeight β (boxSides R a) zeroFlux zeroFlux / c ^ a ≤ ∑' i, q zeroFlux i ^ 2 :=
    hasSum_le (fun j => pow_le_pow_of_le_one (hnq _ j) ((div_le_one h0).2 (hmax j)) (by omega))
      (ht' zeroFlux a ha) hs'.hasSum
  change C < q m i ^ a at hh
  refine (not_lt_of_ge ?_ hh)
  calc
    q m i ^ a ≤ ∑' j, q m j ^ a := (ht' m a ha).summable.le_tsum i (fun j _ => pow_nonneg (hnq _ j) _)
    _ = _ := (ht' m a ha).tsum_eq
    _ ≤ (8 * sectorWeight β (boxSides R a) zeroFlux zeroFlux) / c ^ a :=
      div_le_div_of_nonneg_right (sectorWeight_le_eight_neutral (hp a ha) m m) hc.le
    _ = 8 * (sectorWeight β (boxSides R a) zeroFlux zeroFlux / c ^ a) := by ring
    _ ≤ C := mul_le_mul_of_nonneg_left hb (by norm_num)


/-- Count the positive eigenvalues of each diagonal electric/magnetic sector with
multiplicity, padding finite lists by zeros. Slot (0,0) is the periodic vacuum. -/
structure DiagonalTraces (β : ℝ) (R : Box) where
  value : Flux × ℕ → ℝ
  nonneg : ∀ i, 0 ≤ value i
  top_pos : 0 < value (zeroFlux, 0)
  le_top : ∀ i, value i ≤ value (zeroFlux, 0)
  squares : Summable (fun i => value i ^ 2)
  trace : ∀ m a, 3 ≤ a → HasSum (fun i : ℕ => value (m, i) ^ a)
    (sectorWeight β (boxSides R a) m m)

/-- Construct the W4 input from sector moments and a maximum only within the
periodic neutral sector. The comparison with every other sector follows from S2. -/
def DiagonalTraces.ofNeutralMaximum {β : ℝ} {R : Box} (v : Flux × ℕ → ℝ) (hn : ∀ i, 0 ≤ v i)
    (h0 : 0 < v (zeroFlux, 0)) (hmax : ∀ i, v (zeroFlux, i) ≤ v (zeroFlux, 0))
    (hs : Summable (fun i => v i ^ 2))
    (ht : ∀ m a, 3 ≤ a → HasSum (fun i : ℕ => v (m,i) ^ a) (sectorWeight β (boxSides R a) m m))
    (hp : ∀ a, 3 ≤ a → ∀ (σ : Equiv.Perm Dir) (χ m : Flux), 0 ≤ sectorWeight β (boxSides R a ∘ σ) χ m) :
    DiagonalTraces β R where
  value := v
  nonneg := hn
  top_pos := h0
  le_top := diagonal_values_le_periodic_top v hn h0 hmax
    (hs.comp_injective (show Function.Injective (fun i : ℕ => (zeroFlux, i)) from fun _ _ h => congrArg Prod.snd h)) ht hp
  squares := hs
  trace := ht


/-- The signed Wilson tori themselves give the rectangular moment data. The
distinguished value is the norm on the periodic electric-neutral sector. -/
theorem rectangularDiagonalTraces (R : Box) (hR : R.Valid) {β : ℝ} (hβ : 0 ≤ β) :
    ∃ A : DiagonalTraces β R, A.value (zeroFlux,0) = ‖rectSector (boxShape R) β zeroFlux zeroFlux‖ ∧
      ∀ m, EncodesSlots (rectSector (boxShape R) β m m) (fun i => A.value (m,i)) := by
  classical
  choose v henc htop hn hmax hm using (fun m : Flux => boxSector_labeledList R hβ m m)
  let w (p : Flux × ℕ) := v p.1 p.2
  have hzero : 0 < w (zeroFlux,0) := (boxNeutral_norm_pos R hβ).trans_eq (htop zeroFlux).symm
  have h₂ : Summable (fun p => w p ^ 2) := (summable_prod_of_nonneg (fun i => sq_nonneg (w i))).2
    ⟨fun m => (hm m 2 (by decide)).summable, (hasSum_fintype _).summable⟩
  have htrace (m : Flux) (a : ℕ) (ha : 3 ≤ a) := hm m a (by omega : 2 ≤ a)
  have hpos (a : ℕ) (ha : 3 ≤ a) (σ : Equiv.Perm Dir) (χ m : Flux) :
      0 ≤ sectorWeight β (boxSides R a ∘ σ) χ m := by
    have side (i : Dir) : 3 ≤ boxSides R a i := by
      obtain ⟨hx,hy,hz⟩ := hR
      fin_cases i <;> assumption
    exact sectorWeight_nonneg (le_trans (by decide : 2 ≤ 3) (side (σ TimeAxis.timeIdx))) hβ χ m
  exact ⟨DiagonalTraces.ofNeutralMaximum w (fun p => hn p.1 p.2) hzero (hmax zeroFlux) h₂ htrace hpos, htop zeroFlux,henc⟩


namespace DiagonalTraces

variable {β : ℝ} {R : Box} (A : DiagonalTraces β R)

/-- The actual signed weight is the moment of the combined diagonal list. -/
theorem hasSum_weight {a : ℕ} (ha : 3 ≤ a) :
    HasSum (fun i => A.value i ^ a) (kappaWeight β (boxSides R a)) := by
  have hs : Summable (fun i => A.value i ^ a) :=
    (summable_prod_of_nonneg (fun i => pow_nonneg (A.nonneg i) a)).2
      ⟨fun m => (A.trace m a ha).summable, (hasSum_fintype _).summable⟩
  have he := (hs.hasSum.prod_fiberwise (fun m => A.trace m a ha)).unique
    (hasSum_fintype (fun m => sectorWeight β (boxSides R a) m m))
  rw [kappaWeight_eq_diagonal, ← he]
  exact hs.hasSum

/-- The multiplicity-preserving enumeration is the one from the lane's Wilson module. -/
theorem boxSpectrum : ∃ B : BoxSpectrum, B.top = A.value (zeroFlux, 0) ∧
    Wilson.EnumeratesRatios B A.value (zeroFlux, 0) ∧
    ∀ a : ℕ, 3 ≤ a → B.weight a = kappaWeight β (boxSides R a) := by
  obtain ⟨B, ht, hc, hw⟩ := Wilson.boxSpectrum_of_slots A.value (zeroFlux, 0)
    A.top_pos A.nonneg A.le_top A.squares
  exact ⟨B, ht, hc, fun a ha => (hw a ha).trans (A.hasSum_weight ha).tsum_eq⟩

include A in
/-- Log convexity of the signed partition moments. The sum of
λ^a (x λ - y)^2 is nonnegative, with x=W(a), y=W(a+1). -/
theorem weight_logConvex {a : ℕ} (ha : 3 ≤ a) :
    kappaWeight β (boxSides R (a + 1)) ^ 2 ≤
      kappaWeight β (boxSides R a) * kappaWeight β (boxSides R (a + 2)) := by
  let x := kappaWeight β (boxSides R a)
  let y := kappaWeight β (boxSides R (a + 1))
  let z := kappaWeight β (boxSides R (a + 2))
  have hx : 0 < x := by
    obtain ⟨B, _, _, hw⟩ := A.boxSpectrum
    change 0 < kappaWeight β (boxSides R a)
    rw [← hw a ha]
    exact B.weight_pos a
  have h₀ : HasSum (fun i => A.value i ^ a) x := A.hasSum_weight ha
  have h₁ : HasSum (fun i => A.value i ^ (a + 1)) y := A.hasSum_weight (by omega)
  have h₂ : HasSum (fun i => A.value i ^ (a + 2)) z := A.hasSum_weight (by omega)
  have hs := ((h₂.mul_left (x ^ 2)).sub (h₁.mul_left (2 * x * y))).add (h₀.mul_left (y ^ 2))
  have hterms (i : Flux × ℕ) : 0 ≤ x ^ 2 * A.value i ^ (a + 2) -
      2 * x * y * A.value i ^ (a + 1) + y ^ 2 * A.value i ^ a := by
    rw [show a + 2 = a + 1 + 1 by omega, pow_succ _ (a + 1), pow_succ _ a]
    nlinarith only [mul_nonneg (pow_nonneg (A.nonneg i) a) (sq_nonneg (x * A.value i - y))]
  have h : 0 ≤ x ^ 2 * z - 2 * x * y * y + y ^ 2 * x :=
    hasSum_le hterms hasSum_zero hs
  change y ^ 2 ≤ x * z
  apply le_of_mul_le_mul_left (a := x) _ hx
  nlinarith only [h]

include A in
/-- Corollary EV for any enumerated realization. The explicit vacuum slot
is removed once from both traces. -/
theorem neutralTail_le {a : ℕ} (ha : 3 ≤ a) (B : BoxSpectrum)
    (hw : B.weight a = kappaWeight β (boxSides R a)) :
    sectorWeight β (boxSides R a) zeroFlux zeroFlux / B.top ^ a - 1 ≤ B.thermal a := by
  have hp (m : Flux) : 0 ≤ sectorWeight β (boxSides R a) m m :=
    hasSum_le (fun i => pow_nonneg (A.nonneg (m, i)) a) hasSum_zero (A.trace m a ha)
  have hd : sectorWeight β (boxSides R a) zeroFlux zeroFlux ≤ B.weight a := by
    rw [hw, kappaWeight_eq_diagonal]
    exact Finset.single_le_sum (fun m _ => hp m) (Finset.mem_univ zeroFlux)
  have ht := pow_pos B.top_pos a
  apply sub_le_iff_le_add.mpr
  apply (div_le_iff₀ ht).mpr
  simpa only [BoxSpectrum.weight, mul_comm (B.top ^ a), add_comm (1 : ℝ)] using hd

/-- The combined gap bounds the rate of each nonvacuum positive periodic neutral slot. -/
theorem gap_le_neutralSlot (B : BoxSpectrum)
    (hen : Wilson.EnumeratesRatios B A.value (zeroFlux, 0)) {i : ℕ} (hi : i ≠ 0)
    (hpos : 0 < A.value (zeroFlux, i)) :
    B.gap ≤ (Real.log (1 / (A.value (zeroFlux, i) / B.top)) : EReal) := by
  obtain ⟨e, _, he, _⟩ := hen
  have hn : (zeroFlux, i) ≠ (zeroFlux, 0) := fun h => hi (congrArg Prod.snd h)
  calc
    B.gap ≤ (if 0 < B.ratio (e (zeroFlux, i)) then
      (Real.log (1 / B.ratio (e (zeroFlux, i))) : EReal) else ⊤) := by
      unfold BoxSpectrum.gap
      exact iInf_le _ (e (zeroFlux, i))
    _ = _ := by rw [he _ hn, if_pos (div_pos hpos B.top_pos)]

end DiagonalTraces

section Cylinder

open scoped InnerProductSpace ComplexConjugate
variable {H I : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- The spectral estimate for a cylinder insertion orthogonal to its vacuum.
All nonvacuum modes, including kernel vectors, are counted in the basis. -/
theorem vacuumComplement_power_le (T : H →L[ℂ] H) (hT : T.IsSymmetric)
    (b : HilbertBasis I ℂ H) (o : I) (eigen : I → ℝ)
    (heig : ∀ i, T (b i) = (eigen i : ℂ) • b i) (hn : ∀ i, 0 ≤ eigen i)
    {q : ℝ} (hq : 0 ≤ q) (hb : ∀ i, i ≠ o → eigen i ≤ q)
    (f : H) (hf : ⟪b o, f⟫_ℂ = 0) (n : ℕ) : ‖(T ^ n) f‖ ≤ q ^ n * ‖f‖ := by
  have parseval (g : H) : HasSum (fun i => ‖⟪b i, g⟫_ℂ‖ ^ 2) (‖g‖ ^ 2) := by
    have h := (b.hasSum_inner_mul_inner g g).mapL Complex.reCLM
    convert h using 1
    · funext i
      change ‖⟪b i, g⟫_ℂ‖ ^ 2 = (⟪g, b i⟫_ℂ * ⟪b i, g⟫_ℂ).re
      rw [← inner_conj_symm g (b i), ← Complex.normSq_eq_conj_mul_self, Complex.ofReal_re,
        Complex.sq_norm]
    · exact (inner_self_eq_norm_sq (𝕜 := ℂ) g).symm
  have coeff (i : I) (d : ℕ) : ⟪b i, (T ^ d) f⟫_ℂ = (eigen i : ℂ) ^ d * ⟪b i, f⟫_ℂ := by
    induction d with
    | zero => simp
    | succ d ih =>
      rw [pow_succ', mul_apply_eq_comp, ← hT.apply_clm, heig, inner_smul_left, ih]
      simp only [map_pow, Complex.conj_ofReal, pow_succ']
      ring
  have hterm (i : I) : ‖⟪b i, (T ^ n) f⟫_ℂ‖ ^ 2 ≤ (q ^ n) ^ 2 * ‖⟪b i, f⟫_ℂ‖ ^ 2 := by
    rw [coeff, norm_mul, norm_pow, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (hn i), mul_pow]
    by_cases h : i = o
    · simp [h, hf]
    · exact mul_le_mul_of_nonneg_right
        (pow_le_pow_left₀ (pow_nonneg (hn i) n) (pow_le_pow_left₀ (hn i) (hb i h) n) 2) (sq_nonneg _)
  have hs := hasSum_le hterm (parseval ((T ^ n) f)) ((parseval f).mul_left ((q ^ n) ^ 2))
  exact le_of_pow_le_pow_left₀ (by decide : 2 ≠ 0) (mul_nonneg (pow_nonneg hq _) (norm_nonneg _)) (by simpa only [mul_pow] using hs)

/-- The transfer used by the neutral cylinder, in the release normalization. -/
def normalizedNeutral (Γ : CubicPeriodSublattice) (β : ℝ) (top : ℝ) :
    Γ.SliceL2 TimeAxis.timeIdx →L[ℂ] Γ.SliceL2 TimeAxis.timeIdx :=
  ((top⁻¹ : ℝ) : ℂ) • (Γ.transfer TimeAxis.timeIdx β * electricProj Γ zeroFlux)

theorem normalizedNeutral_symmetric (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (top : ℝ) :
    (normalizedNeutral Γ β top).IsSymmetric := by
  have hT := magneticTransfer_positive Γ hβ zeroFlux
  rw [magneticTransfer_zero] at hT
  have hsa : IsSelfAdjoint (Γ.transfer TimeAxis.timeIdx β) :=
    ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mpr (fun x y => (hT.1 x y).symm)
  have hc := magneticTransfer_commutes_proj Γ hβ zeroFlux zeroFlux
  rw [magneticTransfer_zero] at hc
  apply ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mp
  change star (((top⁻¹ : ℝ) : ℂ) • (Γ.transfer TimeAxis.timeIdx β * electricProj Γ zeroFlux)) = _
  rw [star_smul, show star ((top⁻¹ : ℝ) : ℂ) = ((top⁻¹ : ℝ) : ℂ) from Complex.conj_ofReal _,
    star_mul, hsa.star_eq, (electricProj_isSelfAdjoint Γ zeroFlux).star_eq, ← hc.eq]
  rfl

/-- With the W4 eigenvectors identified, the propagated rate bounds mixed matrix
elements of the actual normalized neutral transfer between separated insertions. -/
theorem neutralMatrixElement_le (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (A : DiagonalTraces β (cube Γ.side)) (B : BoxSpectrum)
    (hen : Wilson.EnumeratesRatios B A.value (zeroFlux, 0))
    {J : Type*} (b : HilbertBasis J ℂ (Γ.SliceL2 TimeAxis.timeIdx)) (o : J) (eigen : J → ℝ)
    (heig : ∀ i, normalizedNeutral Γ β B.top (b i) = (eigen i : ℂ) • b i)
    (hn : ∀ i, 0 ≤ eigen i) (hslots : ∀ i, i ≠ o → eigen i = 0 ∨
      ∃ j : ℕ, j ≠ 0 ∧ eigen i = A.value (zeroFlux, j) / B.top)
    {r : ℝ} (hr : (r : EReal) ≤ B.gap) (f g : Γ.SliceL2 TimeAxis.timeIdx)
    (hg : ⟪b o, g⟫_ℂ = 0) (d : ℕ) :
    ‖⟪f, (normalizedNeutral Γ β B.top ^ d) g⟫_ℂ‖ ≤ ‖f‖ * ‖g‖ * Real.exp (-r * d) := by
  have hq (i : J) (hi : i ≠ o) : eigen i ≤ Real.exp (-r) := by
    rcases hslots i hi with h | ⟨j, hj, h⟩
    · rw [h]; exact (Real.exp_pos _).le
    · by_cases hpos : 0 < A.value (zeroFlux, j)
      · have hepos : 0 < eigen i := h ▸ div_pos hpos B.top_pos
        have he := EReal.coe_le_coe_iff.mp (hr.trans (A.gap_le_neutralSlot B hen hj hpos))
        rw [← h, one_div, Real.log_inv] at he
        exact (Real.log_le_iff_le_exp hepos).mp (by linarith)
      · have hz := le_antisymm (not_lt.mp hpos) (A.nonneg _)
        rw [h, hz, zero_div]
        exact (Real.exp_pos _).le
  have hb := vacuumComplement_power_le _ (normalizedNeutral_symmetric Γ hβ B.top) b o eigen heig hn
    (Real.exp_pos _).le hq g hg d
  calc
    _ ≤ ‖f‖ * ‖(normalizedNeutral Γ β B.top ^ d) g‖ := norm_inner_le_norm _ _
    _ ≤ ‖f‖ * (Real.exp (-r) ^ d * ‖g‖) := mul_le_mul_of_nonneg_left hb (norm_nonneg _)
    _ = _ := by rw [← Real.exp_nat_mul, mul_comm (d : ℝ)]; ring

end Cylinder


/-- The two model identifications required of W4. A witness must give the
signed weight on every valid rectangle and the release norm on actual cubes. -/
structure RealizesKappa (β : ℝ) (T : TorusData) : Prop where
  weight : ∀ R : Box, R.Valid → ∀ a : ℕ, 3 ≤ a →
    (T.spectrum R).weight a = kappaWeight β (boxSides R a)
  top : ∀ Γ : CubicPeriodSublattice,
    (T.spectrum (cube Γ.side)).top = ‖Γ.transfer TimeAxis.timeIdx β‖

/-- Equality between the two time-coordinate conventions for the ordinary partition function. -/
theorem periodic_boxSides (β : ℝ) (R : Box) (a : ℕ) :
    Wilson.partition β (boxSides R a) = Wilson.Z β a R := by
  let σ := finRotate 4
  have he : boxSides R a = Wilson.sides a R ∘ σ := by
    funext i
    fin_cases i <;> rfl
  rw [he]
  exact Wilson.partition_permute β _ _

/-- Rectangular diagonal trace identities supply every field of W5, including the
uniform lower bound. The actual top on release cubes is a separate identification. -/
theorem torusData_of_diagonalTraces (β : ℝ) (tr : ∀ R : Box, R.Valid → DiagonalTraces β R)
    (hnorm : ∀ (Γ : CubicPeriodSublattice) (hR : (cube Γ.side).Valid),
      (tr _ hR).value (zeroFlux, 0) = ‖Γ.transfer TimeAxis.timeIdx β‖) :
    ∃ T : TorusData, RealizesKappa β T ∧ ∀ (R : Box) (hR : R.Valid),
      Wilson.EnumeratesRatios (T.spectrum R) (tr R hR).value (zeroFlux, 0) := by
  classical
  let B (R : Box) := if hR : R.Valid then (tr R hR).boxSpectrum.choose
    else (tr (cube 3) ⟨le_rfl, le_rfl, le_rfl⟩).boxSpectrum.choose
  have spec (R : Box) (hR : R.Valid) :
      (B R).top = (tr R hR).value (zeroFlux, 0) ∧
      Wilson.EnumeratesRatios (B R) (tr R hR).value (zeroFlux, 0) ∧
      ∀ a : ℕ, 3 ≤ a → (B R).weight a = kappaWeight β (boxSides R a) := by
    simpa only [B, dif_pos hR] using (tr R hR).boxSpectrum.choose_spec
  have valid (R : Box) (hR : R.Valid) (i : Axis) (b : ℕ) (hb : 3 ≤ b) :
      (R.replace i b).Valid := by cases i <;> simp_all [Box.Valid, Box.replace]
  let T : TorusData := {
    spectrum := B
    cross := by
      intro R hR i a b ha hb
      rw [(spec _ (valid R hR i b hb)).2.2 a ha, (spec _ (valid R hR i a ha)).2.2 b hb]
      exact kappaWeight_cross β R i a b
    logConvex := by
      intro R hR a ha
      rw [(spec R hR).2.2 _ (by omega), (spec R hR).2.2 _ ha, (spec R hR).2.2 _ (by omega)]
      exact (tr R hR).weight_logConvex ha
    lower := by
      intro R hR i
      let c := -6 * β * Wilson.spectatorArea R i
      refine ⟨c - Real.log 8, fun a b ha hb => ?_⟩
      have hv := valid R hR i b hb
      let R' := R.replace i b
      have hp (m : Flux) : 0 ≤ sectorWeight β (boxSides R' a) m m :=
        hasSum_le (fun j => pow_nonneg ((tr R' hv).nonneg (m, j)) a) hasSum_zero
          ((tr R' hv).trace m a ha)
      have h8 := partition_div_eight_le_kappa β (boxSides R' a) hp
      rw [periodic_boxSides] at h8
      have hZ : 0 < Wilson.Z β a R' := Wilson.partition_pos β _
      have hlog := Real.log_le_log (div_pos hZ (by norm_num)) h8
      rw [Real.log_div hZ.ne' (by norm_num)] at hlog
      rw [(spec R' hv).2.2 a ha]
      have hbase : c * a * b ≤ Real.log (Wilson.Z β a R') := Wilson.log_lower β R hR i a b ha hb
      have hab : (1 : ℝ) ≤ (a : ℝ) * b :=
        one_le_mul_of_one_le_of_one_le (by exact_mod_cast (show 1 ≤ a by omega))
          (by exact_mod_cast (show 1 ≤ b by omega))
      nlinarith only [hbase, hlog, mul_nonneg (Real.log_nonneg (by norm_num : (1 : ℝ) ≤ 8))
        (sub_nonneg.mpr hab)] }
  refine ⟨T, ⟨fun R hR => (spec R hR).2.2, fun Γ => ?_⟩, fun R hR => (spec R hR).2.1⟩
  have hs := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp
    ⟨Γ.lattice, Γ.periods_eq⟩
  have hv : (cube Γ.side).Valid := ⟨hs, hs, hs⟩
  exact (spec _ hv).1.trans (hnorm Γ hv)

/-- The rectangular W5 supplier has only the identification of the periodic
cubic norm left. All magnetic moments, axis exchanges and off-cube bounds are certified. -/
theorem torusData_of_cubicNorm {β : ℝ} (hβ : 0 < β)
    (hNorm : ∀ (Γ : CubicPeriodSublattice), (cube Γ.side).Valid →
      ‖rectSector (boxShape (cube Γ.side)) β zeroFlux zeroFlux‖ = ‖Γ.transfer TimeAxis.timeIdx β‖) :
    ∃ T : TorusData, RealizesKappa β T ∧ ∀ (R : Box) (hR : R.Valid),
      Wilson.EnumeratesRatios (T.spectrum R) (rectangularDiagonalTraces R hR hβ.le).choose.value (zeroFlux,0) :=
  torusData_of_diagonalTraces β (fun R hR => (rectangularDiagonalTraces R hR hβ.le).choose)
    (fun Γ hR => (rectangularDiagonalTraces _ hR hβ.le).choose_spec.1.trans (hNorm Γ hR))


theorem boxShape_cube (V : ℕ) : boxShape (cube V) = fun _ => V := by
  funext i
  rcases i with ⟨i,hi⟩
  fin_cases i <;> first | rfl | exact (hi rfl).elim

theorem calibrated_cubicNorm (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) :
    ‖rectSector (boxShape (cube Γ.side)) β zeroFlux zeroFlux‖ = ‖Γ.transfer TimeAxis.timeIdx β‖ := by
  rw [boxNeutral_norm _ hβ.le,boxShape_cube,rectSymOperator_cube_norm Γ hβ,magneticTransfer_zero]

/-- The Wilson signed integrals, their release normalization and every
rectangular witness required by the unchanged W5 theorem. -/
theorem rectangularTorusData {β : ℝ} (hβ : 0 < β) :
    ∃ T : TorusData, RealizesKappa β T ∧ ∀ (R : Box) (hR : R.Valid),
      Wilson.EnumeratesRatios (T.spectrum R) (rectangularDiagonalTraces R hR hβ.le).choose.value (zeroFlux,0) :=
  torusData_of_cubicNorm hβ (fun Γ _ => calibrated_cubicNorm Γ hβ)

theorem seed_eq_thermal (β : ℝ) (T : TorusData) (hT : RealizesKappa β T)
    (Γ : CubicPeriodSublattice) {N : ℕ} (hN : 3 ≤ N) (hside : 2 * N = Γ.side) :
    T.seed N = kappaWeight β (fun i => if i = TimeAxis.timeIdx then N else Γ.side) /
      ‖Γ.transfer TimeAxis.timeIdx β‖ ^ N - 1 := by
  let B := T.spectrum (cube Γ.side)
  have hv : (cube Γ.side).Valid := by
    have hs : 3 ≤ Γ.side := by omega
    exact ⟨hs, hs, hs⟩
  have he : (fun i => if i = TimeAxis.timeIdx then N else Γ.side) = boxSides (cube Γ.side) N := by
    funext i
    fin_cases i <;> rfl
  rw [he, ← hT.weight _ hv N hN, ← hT.top Γ, TorusData.seed, hside, BoxSpectrum.weight]
  change B.thermal N = B.top ^ N * (1 + B.thermal N) / B.top ^ N - 1
  field_simp [B.top_pos.ne']
  ring

/-- The endpoint uses the fixed positive rate even when the excited sum vanishes. -/
theorem seedRate_lower (T : TorusData) {N : ℕ} (hs : T.seed N < 1 / (2 : ℝ) ^ 18) :
    ((Real.log ((2 : ℝ) ^ 18 / 5041) / N : ℝ) : EReal) ≤ T.seedRate N := by
  unfold TorusData.seedRate
  split_ifs with hz
  · exact le_top
  · apply EReal.coe_le_coe_iff.mpr
    apply div_le_div_of_nonneg_right _ (Nat.cast_nonneg N)
    have hpos : 0 < 5041 * T.seed N := lt_of_le_of_ne
      (mul_nonneg (by norm_num) ((T.spectrum _).thermal_nonneg N)) (Ne.symm hz)
    apply Real.log_le_log (by norm_num)
    apply (le_div_iff₀ hpos).mpr
    linarith only [hs]

/-- W5 at all integer sides, including the intermediate (non-dyadic) volumes. -/
theorem halfSide_thermal_tendsto (T : TorusData) {N : ℕ} (hN : 3 ≤ N)
    (hs : T.seed N < 1 / (2 : ℝ) ^ 18) :
    Tendsto (fun V : ℕ => (T.spectrum (cube V)).thermal (V / 2)) atTop (𝓝 0) := by
  let q := 5041 * T.seed N
  let k (V : ℕ) := Nat.log 2 (V / (2 * N))
  have hden : 0 < 2 * N := by omega
  have hq0 : 0 ≤ q := mul_nonneg (by norm_num) ((T.spectrum _).thermal_nonneg N)
  have hq1 : q < 1 := by dsimp [q]; linarith only [hs]
  have hk : Tendsto k atTop atTop := by
    apply tendsto_atTop.2
    intro b
    filter_upwards [eventually_ge_atTop (2 ^ b * (2 * N))] with V hV
    exact Nat.le_log_of_pow_le (by decide : 1 < 2) ((Nat.le_div_iff_mul_le hden).2 hV)
  have he : Tendsto (fun V : ℕ => 2 ^ k V) atTop atTop :=
    (tendsto_pow_atTop_atTop_of_one_lt (by decide : 1 < (2 : ℕ))).comp hk
  have hb := ((tendsto_pow_atTop_nhds_zero_of_lt_one hq0 hq1).comp he).div_const 71
  apply squeeze_zero' (Eventually.of_forall fun V => (T.spectrum _).thermal_nonneg (V / 2)) _ (by
    simpa only [zero_div] using hb)
  filter_upwards [eventually_ge_atTop (2 * N)] with V hV
  have hx : V / (2 * N) ≠ 0 := (Nat.div_pos hV hden).ne'
  have hlo := (Nat.le_div_iff_mul_le hden).1 (Nat.pow_log_le_self 2 hx)
  have hhi := (Nat.div_lt_iff_lt_mul hden).1 (Nat.lt_pow_succ_log_self (by decide : 1 < 2) (V / (2 * N)))
  change 2 ^ k V * (2 * N) ≤ V at hlo
  change V < 2 ^ (k V + 1) * (2 * N) at hhi
  rw [pow_succ] at hhi
  have hl : 2 * (2 ^ k V * N) ≤ V := by simpa only [mul_left_comm, mul_assoc, mul_comm] using hlo
  have hu : V ≤ 4 * (2 ^ k V * N) := by nlinarith only [hhi]
  have ha : 3 ≤ 2 ^ k V * N := hN.trans (Nat.le_mul_of_pos_left N (by positivity))
  exact ((T.spectrum (cube V)).thermal_antitone ha (by omega)).trans
    (T.intermediate_thermal hN (hs.trans (by norm_num)) (k V) V hl hu)

theorem physicalRate_eq {L ℓ k N : ℕ} (hL : 0 < L) (hℓ : 0 < ℓ)
    (hN : 2 * N = ℓ * L ^ k) :
    gapRate ℓ * PeriodicLattice.meshSize L (k : ℤ) =
      Real.log ((2 : ℝ) ^ 18 / 5041) / N := by
  have h : 2 * (N : ℝ) = (ℓ : ℝ) * (L : ℝ) ^ k := by exact_mod_cast hN
  have hn : (N : ℝ) ≠ 0 := by
    have := mul_pos (show (0 : ℝ) < ℓ by exact_mod_cast hℓ)
      (pow_pos (show (0 : ℝ) < L by exact_mod_cast hL) k)
    linarith
  simp only [gapRate, PeriodicLattice.meshSize, zpow_neg, zpow_natCast]
  field_simp [hn, (Nat.cast_pos.mpr hℓ).ne', (Nat.cast_pos.mpr hL).ne']
  linear_combination h

end Propagation

section VolumeLimit

open InfiniteLattice CutoffLimits.CenteredMomentsAndVolumeFirst TheStatementsProvedTogether
open scoped ComplexConjugate

/-- Freeze the inner centering at the prescribed infinite-volume state while taking
the finite-volume expectation. The outer mean is computed in the sampling measure. -/
def volumeU {a : ℝ} (ν μ : Measure (GaugeField a)) (Z : PositiveSpan) (t : ℝ) : ℝ :=
  let moment (fs : List RealValued) := CutoffLimits.centredMoment μ ν fs.get
  let z := Z.val
  let mean := ∑ X ∈ z.support, z X * moment X.val
  let pair := ∑ X ∈ z.support, ∑ Y ∈ z.support, conj (z X) * z Y *
    moment (pushList TimeAxis.timeReflection X.val ++ pushList (translate (t • timeBasisVec)) Y.val)
  pair.re - ‖mean‖ ^ 2

theorem volumeU_self {a : ℝ} (ν : Measure (GaugeField a)) (Z : PositiveSpan) (t : ℝ) :
    volumeU ν ν Z t = latticeU ν Z t := rfl

theorem centredMoment_weak (D : FixedSpacing.Setup) {μ : ℕ → Measure D.Fields} {ν : Measure D.Fields}
    (hw : ∀ F : BoundedContinuousFunction D.Fields ℝ,
      Tendsto (fun v => ∫ x, F x ∂μ v) atTop (𝓝 (∫ x, F x ∂ν)))
    (fs : List RealValued) (hfs : ∀ f ∈ fs, SeparatedTuples.IsC1c f) :
    Tendsto (fun v => CutoffLimits.centredMoment (μ v) ν fs.get) atTop (𝓝 (listMoment ν fs)) := by
  let F : BoundedContinuousFunction D.Fields ℝ := BoundedContinuousFunction.mkOfCompact
    ⟨fun U => ∏ i, centeredFactor ν (fs.get i) U, continuous_finsetProd _ fun i _ => by
      have hc := FixedSpacing.CurvatureObservable.continuous_smearedEnergy
        fixed_spacing_lattice_basic_facts D
        (CutoffRepresentative.CentredCalculus.isBoundedBorelCompactlySupported_of_isC1c
          (hfs _ (List.get_mem fs i)))
      exact (Complex.continuous_re.comp hc).sub continuous_const⟩
  change Tendsto _ _ (𝓝 (CutoffLimits.centredMoment ν ν fs.get))
  simp only [centredMoment_eq_ofReal_integral]
  exact (Complex.continuous_ofReal.tendsto _).comp (hw F)

set_option maxHeartbeats 1000000 in
/-- The same volume subsequence works for every span and every fixed displacement. -/
theorem volumeU_tendsto {L k : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) :
    ∃ φ : ℕ → ℕ, StrictMono φ ∧ ∀ (Z : PositiveSpan) (t : ℝ),
      Tendsto (fun v => volumeU ν (liftedWilsonMeasure L (φ v) k β) Z t) atTop
        (𝓝 (latticeU ν Z t)) := by
  obtain ⟨_, φ, hφ, hw⟩ := hν
  refine ⟨φ, hφ, fun Z t => ?_⟩
  let D : FixedSpacing.Setup := ⟨L, hL, k, 1, β, hβ⟩
  have hc := centredMoment_weak D hw
  have hf (X Y : SepTuple) : ∀ f ∈ pushList TimeAxis.timeReflection X.val ++
      pushList (translate (t • timeBasisVec)) Y.val, SeparatedTuples.IsC1c f := by
    rw [← ConditionDefaults.push_val separatedTuples_basic.1
      (ConditionDefaults.isEuclidIsometry_timeReflection unit_normal_reflection_lattice_mirror),
      ← SeparatedTuples.push_translate_val]
    intro f hf
    rcases List.mem_append.mp hf with hp | hp
    · exact (push _ X).2.1 _ hp
    · exact (push _ Y).2.1 _ hp
  unfold volumeU latticeU
  exact ((Complex.continuous_re.tendsto _).comp (tendsto_finsetSum _ fun X _ =>
    tendsto_finsetSum _ fun Y _ => (hc _ (hf X Y)).const_mul _)).sub
      ((tendsto_finsetSum _ fun X _ => (hc _ X.2.1).const_mul _).norm.pow 2)

end VolumeLimit

section FiniteVolumes

local notation "μt" => TimeAxis.timeIdx

open InfiniteLattice

/-- The release's periodic side in lattice spacings, at fixed cutoff. -/
abbrev volumeSide (L k v : ℕ) := PeriodicLattice.gridSideLength L v (k : ℤ)

theorem volumeSide_tendsto {L : ℕ} (hL : 1 < L) (k : ℕ) :
    Tendsto (volumeSide L k) atTop atTop := by
  have h : StrictMono (fun v : ℕ => 2 * L ^ (v + k)) := fun i j hij =>
    Nat.mul_lt_mul_of_pos_left (Nat.pow_lt_pow_right hL (Nat.add_lt_add_right hij k)) (by decide)
  change Tendsto (fun v : ℕ => 2 * L ^ ((v : ℤ) + (k : ℤ)).toNat) atTop atTop
  simpa only [← Nat.cast_add, Int.toNat_natCast] using h.tendsto_atTop

/-- Dilation of a period subgroup with physical side t = V a. -/
theorem rescale_cubicPeriods {a t : ℝ} (ha : 0 < a) (V : ℕ) (ht : t = (V : ℝ) * a)
    (P : PeriodSublattice a) (hp : P.HasCubicPeriods t) :
    subgroupRescale ha P.periods = cubicSublattice 1 (V : ℝ) := by
  have scaled (z : Fin 4 → ℤ) (i : Dir) :
      a⁻¹ * TestFunctions.latticeTranslate t z i = (z i : ℝ) * V := by
    unfold TestFunctions.latticeTranslate
    rw [ht]
    field_simp [ne_of_gt ha] <;> ring
  ext y
  constructor
  · rintro ⟨x, hx, rfl⟩
    have hmem : (x : AmbientSpace) ∈ cubicPeriodSet t := by
      rw [← hp]
      exact ⟨x, hx, rfl⟩
    obtain ⟨z, hz⟩ := hmem
    refine ⟨z, fun i => ?_⟩
    change a⁻¹ * (x : AmbientSpace) i = (z i : ℝ) * V
    rw [← congrFun hz i]
    exact scaled z i
  · rintro ⟨z, hz⟩
    have hmem : TestFunctions.latticeTranslate t z ∈
        (fun x : LatticePoint a => (x : AmbientSpace)) '' (P.periods : Set (LatticePoint a)) := by
      rw [hp]
      exact Set.mem_range_self z
    obtain ⟨x, hx, he⟩ := hmem
    refine ⟨x, hx, Subtype.ext (funext fun i => ?_)⟩
    change a⁻¹ * (x : AmbientSpace) i = (y : AmbientSpace) i
    change (x : AmbientSpace) = TestFunctions.latticeTranslate t z at he
    rw [congrFun he i, show (y : AmbientSpace) i = (z i : ℝ) * V from hz i]
    exact scaled z i

/-- The released finite measure, at its own positive cutoff and volume, is exactly
the lift from a *unit-mesh* transfer cube with side 2 L^(v+k) after dilation. -/
theorem liftedWilson_unitCube {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L)
    (k v : ℕ+) {β : ℝ} (hβ : 0 < β) :
    ∃ Γ : CubicPeriodSublattice, Γ.side = volumeSide L k v ∧
      dilatedState (a := PeriodicLattice.meshSize L (k : ℤ))
        (by exact zpow_pos (by exact_mod_cast (show 0 < L by have := hL.2; omega)) _)
        (liftedWilsonMeasure L v k β) = Γ.lattice.liftedGibbsMeasure β := by
  let D : Conventions.StandingParameters := ⟨L, hL, k, v⟩
  let a := PeriodicLattice.meshSize L (k : ℤ)
  let V := volumeSide L k v
  have hL' : 0 < L := by have := hL.2; omega
  have ha : 0 < a := zpow_pos (by exact_mod_cast hL') _
  have hV : 1 ≤ V := by
    change 0 < 2 * L ^ _
    positivity
  have ht : PeriodicLattice.torusSide L v = (V : ℝ) * a :=
    PeriodicLattice.IsometryAction.torusSide_eq_mul_meshSize hL' (by omega)
  have hq := TheStatementsProvedTogether.cubic_torus_eq_quotient D β hβ
  obtain ⟨P, hp⟩ := hq.1
  have hd : UnitSpacing.PeriodSublatticesTransfer ha β :=
    (TheStatementsProvedTogether.dilation_to_spacing_one a β ha hβ).2.2.2.2.2.2.2
  obtain ⟨P', hp'⟩ := (hd.1 P.periods).mp ⟨P, rfl⟩
  let Γ : CubicPeriodSublattice := ⟨V, hV, P', hp'.trans (rescale_cubicPeriods ha V ht P hp)⟩
  refine ⟨Γ, rfl, ?_⟩
  have hm : P.liftedGibbsMeasure β = liftedWilsonMeasure L v k β := (hq.2.1 P hp).2.liftedGibbsMeasure_eq
  rw [← hm]
  exact (hd.2 P P' hp').2

/-- A physical test f at mesh a, expressed on the unit lattice. -/
def unitTest (a : ℝ) (f : RealValued) : RealValued := fun x => f (a • x)

theorem smearedEnergy_unitTest {a : ℝ} (ha : 0 < a) (f : RealValued)
    (hf : IsBoundedBorelCompactlySupported f) (U : GaugeField a) :
    smearedEnergy (unitTest a f) (fieldRescale ha U) = smearedEnergy f U := by
  have hb := ((Dilation.smearedEnergy_scales ℝ ha (show a = a * 1 by ring)) f hf).1
  have h := ((Dilation.smearedEnergy_scales ℝ (inv_pos.mpr ha) (one_eq_inv_mul_spacing ha)) (unitTest a f) hb).2 U
  simpa only [fieldRescale, unitTest, smul_smul, mul_inv_cancel₀ ha.ne', one_smul] using h

theorem measurable_smearedEnergy_unitTest {a : ℝ} (ha : 0 < a) (f : RealValued)
    (hf : IsBoundedBorelCompactlySupported f) (hm : Measurable (smearedEnergy f : GaugeField a → ℝ)) :
    Measurable (smearedEnergy (unitTest a f) : GaugeField 1 → ℝ) := by
  have h := ((Dilation.smearedEnergy_scales ℝ ha (show a = a * 1 by ring)) f hf).2
  have eqn : (smearedEnergy (unitTest a f) : GaugeField 1 → ℝ) =
      (smearedEnergy f : GaugeField a → ℝ) ∘ gaugeFieldScale ha (show a = a * 1 by ring) :=
    funext fun U => (h U).symm
  rw [eqn]
  exact hm.comp (measurable_gaugeFieldScale _ _)

open CutoffLimits.CenteredMomentsAndVolumeFirst in
/-- The same dilation acts on the sampling measure, the centering state and each
physical test. No new choice of an infinite-volume state enters. -/
theorem centredMoment_unitTest {a : ℝ} (ha : 0 < a) (μ ν : Measure (GaugeField a)) {n : ℕ}
    (f : Fin n → RealValued) (hf : ∀ i, IsBoundedBorelCompactlySupported (f i))
    (hm : ∀ i, Measurable (smearedEnergy (f i) : GaugeField a → ℝ)) :
    CutoffLimits.centredMoment (dilatedState ha μ) (dilatedState ha ν) (fun i => unitTest a (f i)) =
      CutoffLimits.centredMoment μ ν f := by
  have hms (i : Fin n) := measurable_smearedEnergy_unitTest ha (f i) (hf i) (hm i)
  have mean (i : Fin n) : (∫ U, smearedEnergy (unitTest a (f i)) U ∂dilatedState ha ν) =
      ∫ U, smearedEnergy (f i) U ∂ν := by
    rw [dilatedState_eq_map, integral_map (measurable_fieldRescale ha).aemeasurable (hms i).aestronglyMeasurable]
    exact integral_congr_ae (ae_of_all _ (smearedEnergy_unitTest ha (f i) (hf i)))
  simp only [centredMoment_eq_ofReal_integral]
  apply congrArg Complex.ofReal
  have hb : Measurable (fun U : GaugeField 1 => ∏ i, centeredFactor (dilatedState ha ν) (unitTest a (f i)) U) :=
    Finset.measurable_fun_prod _ fun i _ => (hms i).sub_const _
  rw [dilatedState_eq_map ha μ, integral_map (measurable_fieldRescale ha).aemeasurable hb.aestronglyMeasurable]
  apply integral_congr_ae
  filter_upwards with U
  apply Finset.prod_congr rfl
  intro i _
  unfold centeredFactor
  rw [mean, smearedEnergy_unitTest ha _ (hf i)]

/-- The equality with the unit transfer cube holds simultaneously for all test lists,
with every mean evaluated in the dilation of the very state supplied at the cutoff. -/
theorem liftedWilson_moments_unitCube {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L)
    (k v : ℕ+) {β : ℝ} (hβ : 0 < β) (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ)))) :
    let a := PeriodicLattice.meshSize L (k : ℤ)
    let ha : 0 < a := zpow_pos (by exact_mod_cast (show 0 < L by have := hL.2; omega)) _
    ∃ Γ : CubicPeriodSublattice, Γ.side = volumeSide L k v ∧ ∀ (n : ℕ) (f : Fin n → RealValued),
      (∀ i, IsC1c (f i)) →
      CutoffLimits.centredMoment (Γ.lattice.liftedGibbsMeasure β) (dilatedState ha ν)
        (fun i => unitTest a (f i)) = CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν f := by
  dsimp only
  obtain ⟨Γ, hs, hΓ⟩ := liftedWilson_unitCube hL k v hβ
  refine ⟨Γ, hs, fun n f hf => ?_⟩
  rw [← hΓ]
  let D : FixedSpacing.Setup := ⟨L, hL, k, v, β, hβ⟩
  have hfs (i : Fin n) := CutoffRepresentative.CentredCalculus.isBoundedBorelCompactlySupported_of_isC1c (hf i)
  apply centredMoment_unitTest _ _ _ f hfs
  intro i
  exact (Complex.continuous_re.comp (FixedSpacing.CurvatureObservable.continuous_smearedEnergy
    TheStatementsProvedTogether.fixed_spacing_lattice_basic_facts D (hfs i))).measurable


open scoped ComplexConjugate

/-- The physical torus law and its original centering constants appear in one
joint-coordinate formula for every test list. One cube and one time labeling
work for all those lists. -/
theorem cutoff_joint_moments {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k v : ℕ+)
    {β : ℝ} (hβ : 0 < β) (ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))) (origin : ℤ := 0) :
    let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    ∃ (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side), Γ.side = volumeSide L k v ∧
      (∀ t,E (finRotate _ t) = E t+1) ∧ (∀ t,E t = (origin : ZMod Γ.side)+(t.val : ZMod Γ.side)) ∧ ∀ (q : ℕ) (f : Fin q → RealValued), (∀ j,IsC1c (f j)) →
        CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν f =
          ∫ z, ∏ j, ((smearedEnergy (unitTest a (f j)) (Γ.lattice.lift (fieldOfPairs Γ ((physicalJointCoordinates Γ E).symm z))) -
            ∫ U, smearedEnergy (f j) U ∂ν : ℝ) : ℂ) ∂jointState (fun _ => Γ.side) β zeroFlux zeroFlux := by
  let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  have hL' := hL.2
  have ha : 0 < a := zpow_pos (by exact_mod_cast (show 0 < L by omega)) _
  obtain ⟨Γ,hs,hΓ⟩ := liftedWilson_moments_unitCube hL k v hβ ν
  obtain ⟨E,hE,hE0⟩ := anchoredCubeTimeIndex Γ (origin : ZMod Γ.side)
  refine ⟨Γ,E,hs,hE,hE0,fun q f hf => ?_⟩
  let D : FixedSpacing.Setup := ⟨L,hL,k,1,β,hβ⟩
  have good (j) := CutoffRepresentative.CentredCalculus.isBoundedBorelCompactlySupported_of_isC1c (hf j)
  have hf' (j) : Measurable (smearedEnergy (f j) : GaugeField a → ℝ) := (Complex.continuous_re.comp
    (FixedSpacing.CurvatureObservable.continuous_smearedEnergy TheStatementsProvedTogether.fixed_spacing_lattice_basic_facts D (good j))).measurable
  have hm (j) := measurable_smearedEnergy_unitTest ha (f j) (good j) (hf' j)
  let c (j) := ∫ U,smearedEnergy (f j) U ∂ν
  have mean (j) : (∫ U,smearedEnergy (unitTest a (f j)) U ∂dilatedState ha ν) = c j := by
    rw [dilatedState_eq_map,integral_map (measurable_fieldRescale ha).aemeasurable (hm j).aestronglyMeasurable]
    exact integral_congr_ae (ae_of_all _ (smearedEnergy_unitTest ha _ (good j)))
  let g (U : GaugeField 1) : ℂ := ∏ j, ((smearedEnergy (unitTest a (f j)) U - c j : ℝ) : ℂ)
  have hg : Measurable g := Finset.measurable_fun_prod _ fun j _ => Complex.continuous_ofReal.measurable.comp ((hm j).sub_const _)
  apply Eq.trans _ (physicalJoint_expectation Γ hβ E hE g hg)
  rw [← hΓ q f hf,CutoffLimits.CenteredMomentsAndVolumeFirst.centredMoment_eq_ofReal_integral,← integral_complex_ofReal]
  apply integral_congr_ae
  filter_upwards with U
  simp only [g,Complex.ofReal_prod,CutoffLimits.CenteredMomentsAndVolumeFirst.centeredFactor]
  apply Finset.prod_congr rfl
  intro j _
  change ((smearedEnergy (unitTest a (f j)) U - ∫ V, smearedEnergy (unitTest a (f j)) V ∂dilatedState ha ν : ℝ) : ℂ) = _
  rw [mean]


/-- Lattice isometries preserve a whole smeared moment with the inner mean
frozen at the prescribed volume limit and the outer mean on the physical torus. -/
theorem frozenMoment_motion {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k v : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (r : CutoffLatticeStates.refinedLatticeMotions L k)
    {q : ℕ} (f : Fin q → RealValued) (hf : ∀ i,IsC1c (f i)) :
    CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν (fun i => f i ∘ invMap r.val) =
      CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν f := by
  let s : Conventions.StandingParameters := ⟨L,hL,k,v⟩
  have H := TheStatementsProvedTogether.cutoffStates_isometry_invariant s β hβ
  obtain ⟨hfin,hfin'⟩ := H.1 v v.pos
  obtain ⟨hn,hperiod,_⟩ := Assembly.volumeLimit_symmetries L hL k β hβ ν hν
  letI : IsProbabilityMeasure ν := hn
  letI : IsProbabilityMeasure (liftedWilsonMeasure L v k β) := hfin
  have hnu := H.2.2.1 ν hperiod
  by_cases hq : 1 ≤ q
  · have hm := (H.2.2.2 r).2.2.2 ν (liftedWilsonMeasure L v k β) (hnu r) (hfin' r) q hq f
      (fun i => CutoffRepresentative.CentredCalculus.isBoundedBorelCompactlySupported_of_isC1c (hf i))
    exact hm.2.2
  · have hz : q = 0 := by omega
    subst q
    congr 1
    funext i
    exact Fin.elim0 i

/-- List transport preserves order, including the empty tuple, and matches the
release's Fin-indexed observable with its frozen centering. -/
theorem pushed_list_moment {a : ℝ} (μ ν : Measure (GaugeField a)) (r : InfiniteLattice.AmbientSpace → InfiniteLattice.AmbientSpace)
    (fs : List RealValued) :
    CutoffLimits.centredMoment μ ν (pushList r fs).get =
      CutoffLimits.centredMoment μ ν (fun i : Fin fs.length => fs.get i ∘ invMap r) := by
  simp only [CutoffLimits.CenteredMomentsAndVolumeFirst.centredMoment_eq_ofReal_integral]
  congr 1
  apply integral_congr_ae
  filter_upwards with U
  let G (f : RealValued) := CutoffLimits.CenteredMomentsAndVolumeFirst.centeredFactor ν f U
  have frame (l : List RealValued) (g : RealValued → ℝ) : (∏ i : Fin l.length,g (l.get i)) = (l.map g).prod := by
    rw [← Fin.prod_univ_fun_getElem]
    rfl
  change (∏ i : Fin (pushList r fs).length,G ((pushList r fs).get i)) =
    ∏ i : Fin fs.length, G (fs.get i ∘ invMap r)
  rw [frame,frame fs (fun f => G (f ∘ invMap r))]
  simp [pushList,List.map_map,Function.comp_def]

theorem siteReflection_motion (a : ℝ) : TimeAxis.timeReflection ∈ latticeMotions a := by
  refine ⟨coordinateSignFlip μt,coordinateSignFlip_mem_hypercubicGroup _,0,(latticeSubgroup a).zero_mem,fun x => ?_⟩
  rw [add_zero]
  funext i
  fin_cases i <;> rfl

theorem gridTranslation_motion (a : ℝ) (d : ℕ) :
    SeparatedTuples.translate (((d : ℝ) * a) • timeBasisVec) ∈ latticeMotions a := by
  let v : LatticePoint a := d • axisStep a μt
  have he : (v : InfiniteLattice.AmbientSpace) = ((d : ℝ) * a) • timeBasisVec := by
    funext i
    change (d • (Pi.single μt a : InfiniteLattice.AmbientSpace)) i = _
    by_cases hi : i = μt
    · subst i; simp [timeBasisVec,PeriodicLattice.coordVec,Pi.smul_apply,nsmul_eq_mul]
    · simp [timeBasisVec,PeriodicLattice.coordVec,Pi.smul_apply,Pi.single_eq_of_ne hi,nsmul_eq_mul]
  rw [← he]
  exact (InfiniteLattice.shiftMotion v).property

theorem frozen_smearedMean_motion {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (r : CutoffLatticeStates.refinedLatticeMotions L k)
    (f : RealValued) (hf : IsC1c f) :
    (∫ U, smearedEnergy (f ∘ invMap r.val) U ∂ν) = ∫ U, smearedEnergy f U ∂ν := by
  let s : Conventions.StandingParameters := ⟨L,hL,k,1⟩
  have H := TheStatementsProvedTogether.cutoffStates_isometry_invariant s β hβ
  obtain ⟨hn,hperiod,_⟩ := Assembly.volumeLimit_symmetries L hL k β hβ ν hν
  letI : IsProbabilityMeasure ν := hn
  have hi := H.2.2.1 ν hperiod r
  have hf' := CutoffRepresentative.CentredCalculus.isBoundedBorelCompactlySupported_of_isC1c hf
  have h := (H.2.2.2 r).2.1 f hf'
  let D : FixedSpacing.Setup := ⟨L,hL,k,1,β,hβ⟩
  let G (U : D.Fields) := ((smearedEnergy f U : ℝ) : ℂ)
  have hc : Continuous G := FixedSpacing.CurvatureObservable.continuous_smearedEnergy
    TheStatementsProvedTogether.fixed_spacing_lattice_basic_facts D hf'
  apply Complex.ofReal_injective
  rw [← integral_complex_ofReal,← integral_complex_ofReal]
  calc
    _ = ∫ U, latticeMotionAct r G U ∂ν := integral_congr_ae (ae_of_all _ fun U =>
      congrArg Complex.ofReal (congrFun h.1 U).symm)
    _ = _ := hi G (CutoffLatticeStates.MotionInvariance.isBoundedObservable_of_continuous hc)

theorem unitTest_gridTranslation (a : ℝ) (d : ℕ) (f : RealValued) :
    unitTest a (f ∘ invMap (SeparatedTuples.translate (((d : ℝ)*a) • timeBasisVec))) = translatedUnitTest d (unitTest a f) := by
  have shift : ((((d : ℤ) • axisStep 1 μt : LatticePoint 1)) : InfiniteLattice.AmbientSpace) = (d:ℝ) • timeBasisVec := by
    funext i
    change ((d : ℤ) • (Pi.single μt (1 : ℝ) : InfiniteLattice.AmbientSpace)) i = _
    by_cases hi : i = μt
    · subst i; simp [timeBasisVec,PeriodicLattice.coordVec,Pi.smul_apply,zsmul_eq_mul]
    · simp [timeBasisVec,PeriodicLattice.coordVec,Pi.smul_apply,Pi.single_eq_of_ne hi,zsmul_eq_mul]
  funext x
  change f (invMap (SeparatedTuples.translate _) (a • x)) = f (a • (x-_))
  rw [ReflectionPositivity.LimitContraction.invMap_translate,shift,smul_sub,smul_smul,mul_comm a (d : ℝ)]

/-- On the physical cutoff, all translates of a centered test monomial use
one finite family of marks with the original frozen means and a uniform norm budget. -/
theorem cutoff_translated_marks {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) {J : Type} [Fintype J] (f : J → RealValued) (hf : ∀ j,IsC1c (f j)) :
    let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    ∃ (I : Type) (_ : Fintype I) (weight : I → ℂ) (times : I → J → ℤ) (b : ℤ) (width : ℕ), 0 < width ∧
      ∀ Γ : CubicPeriodSublattice, ∃ K : I → ZMod Γ.side → WindowTest Γ,
        (∀ i c, CentreBlind (K i c)) ∧ (∀ i c, c ∉ Set.range (Γ.levelClass ∘ times i) → K i c = 1) ∧
        (∀ i c,c ∉ Set.range (fun j : Fin width => (b : ZMod Γ.side)+(j.val : ZMod Γ.side)) → K i c = 1) ∧
        (∀ i,(∏ c, ‖K i c‖) ≤ 2 ^ Fintype.card J) ∧
        (∀ i,width ≤ Γ.side → (∏ j : Fin width,‖K i ((b : ZMod Γ.side)+(j.val : ZMod Γ.side))‖) ≤ 2 ^ Fintype.card J) ∧ ∀ (d : ℕ) (z : ReleasePairs Γ),
        let g (j : J) := f j ∘ invMap (SeparatedTuples.translate (((d : ℝ)*a) • timeBasisVec))
        (∏ j, ((smearedEnergy (unitTest a (g j)) (Γ.lattice.lift (fieldOfPairs Γ z)) - ∫ U, smearedEnergy (g j) U ∂ν : ℝ) : ℂ)) =
          ∑ i, weight i * ∏ c, K i c (physicalWindow Γ z (c+Γ.levelClass (d:ℤ))) := by
  let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  have hL' := hL.2
  have ha : 0 < a := zpow_pos (by exact_mod_cast (show 0 < L by omega)) _
  let center (j : J) := ∫ U, smearedEnergy (f j) U ∂ν
  obtain ⟨I,fi,w,t,h⟩ := translated_centeredProduct_layerExpansion (fun j => unitTest a (f j))
    (fun j => (hf j).2.comp_smul ha.ne') center
  obtain ⟨b,width,hw,hb'⟩ := finite_time_word t
  refine ⟨I,fi,w,t,b,width,hw,fun Γ => ?_⟩
  obtain ⟨K,hb,ho,hn,he⟩ := h Γ
  have word (i : I) := word_residue_support (V := Γ.side) (K i) (t i) b (hb' i) (ho i)
  have normWord (i : I) (hw' : width ≤ Γ.side) :
      (∏ j : Fin width,‖K i ((b : ZMod Γ.side)+(j.val : ZMod Γ.side))‖) ≤ 2 ^ Fintype.card J := by
    rw [residue_word_product hw' (b : ZMod Γ.side) (fun c => ‖K i c‖) (fun c hc => by rw [word i c hc,norm_one])]
    exact hn i
  refine ⟨K,hb,ho,word,hn,normWord,fun d z => ?_⟩
  let r : CutoffLatticeStates.refinedLatticeMotions L k := ⟨_,gridTranslation_motion a d⟩
  have hc (j) := frozen_smearedMean_motion hL k hβ hν r (f j) (hf j)
  apply Eq.trans _ (he (d:ℤ) z)
  apply Finset.prod_congr rfl
  intro j _
  change ((smearedEnergy (unitTest a (f j ∘ invMap (SeparatedTuples.translate _))) _ - ∫ U,smearedEnergy (f j ∘ invMap r.val) U ∂ν : ℝ) : ℂ) = _
  rw [unitTest_gridTranslation,hc]


/-- Each physical cutoff moment and all its integral time translates are
periodic means of one polynomial in the marked layers. The coefficients and
width are uniform in the volume and the time origin is arbitrary. -/
theorem cutoff_polynomial_witness {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) {q : ℕ} (f : Fin q → RealValued) (hf : ∀ j,IsC1c (f j)) :
    let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    ∃ (J : Type) (_ : Fintype J) (w : J → ℂ) (b : ℤ) (width : ℕ), 0 < width ∧ ∀ (v : ℕ+) (origin : ℤ),
      ∃ (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side) (K : J → ZMod Γ.side → WindowTest Γ),
        Γ.side = volumeSide L k v ∧ (∀ t,E t = (origin : ZMod Γ.side)+(t.val : ZMod Γ.side)) ∧
        (∀ j c,CentreBlind (K j c)) ∧
        (∀ j c,c ∉ Set.range (fun t : Fin width => (b : ZMod Γ.side)+(t.val : ZMod Γ.side)) → K j c = 1) ∧
        (∀ j,width ≤ Γ.side → (∏ t : Fin width,‖K j ((b : ZMod Γ.side)+(t.val : ZMod Γ.side))‖) ≤ 2 ^ q) ∧
        ∀ d : ℕ,CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν
            (fun j => f j ∘ invMap (SeparatedTuples.translate (((d : ℝ)*a) • timeBasisVec))) =
          ∫ z,∑ j,w j*jointMark (finRotate _).symm (fun t => K j (E t-Γ.levelClass (d:ℤ))) z
            ∂jointState (fun _ => Γ.side) β zeroFlux zeroFlux := by
  let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  obtain ⟨J,fi,w,t,b,width,hw,expand⟩ := cutoff_translated_marks hL k hβ hν f hf
  refine ⟨J,fi,w,b,width,hw,fun v origin => ?_⟩
  obtain ⟨Γ,E,hside,hE,hE0,hm⟩ := cutoff_joint_moments hL k v hβ ν origin
  obtain ⟨K,hb,_,support,_,bound,he⟩ := expand Γ
  refine ⟨Γ,E,K,hside,hE0,hb,support,by simpa only [Fintype.card_fin] using bound,fun d => ?_⟩
  let u := ((d:ℝ)*a) • timeBasisVec
  let g (j : Fin q) := f j ∘ invMap (SeparatedTuples.translate u)
  have hg (j : Fin q) : IsC1c (g j) := by
    have hh : g j = (fun x => f j (x-u)) := by
      funext x
      change f j (invMap (SeparatedTuples.translate u) x) = _
      rw [ReflectionPositivity.LimitContraction.invMap_translate]
    rw [hh]
    exact BoundsOnEverySide.TranslatedTuples.isC1c_shift (hf j) _
  apply (hm q g hg).trans
  apply integral_congr_ae
  filter_upwards with z
  let p := (physicalJointCoordinates Γ E).symm z
  apply (he d p).trans
  apply Finset.sum_congr rfl
  intro j _
  rw [physical_shifted_jointMark Γ E hE,show physicalJointCoordinates Γ E p = z from
    (physicalJointCoordinates Γ E).apply_symm_apply z]


/-- Both one-point factors of the reflected, translated physical covariance
are exactly the original torus means even with the prescribed cutoff centering. -/
theorem oddGrid_marginals {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k v : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (X : SepTuple) (d : ℕ) :
    let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    let μ := liftedWilsonMeasure L v k β
    CutoffLimits.centredMoment μ ν (pushList TimeAxis.timeReflection X.val).get = CutoffLimits.centredMoment μ ν X.val.get ∧
      CutoffLimits.centredMoment μ ν (pushList (translate (((d : ℝ) * a) • timeBasisVec)) X.val).get =
        CutoffLimits.centredMoment μ ν X.val.get := by
  let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  have hf (i : Fin X.val.length) := X.property.1 _ (List.get_mem X.val i)
  constructor
  · rw [pushed_list_moment]
    exact frozenMoment_motion hL k v hβ hν ⟨_,siteReflection_motion a⟩ _ hf
  · rw [pushed_list_moment]
    exact frozenMoment_motion hL k v hβ hν ⟨_,gridTranslation_motion a d⟩ _ hf

/-- The scalar in Stage 0 is the finite sum of ordinary two-window connected
correlations. All one-point functions here are evaluated in the same torus. -/
theorem volumeU_connected_sum {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k v : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (Z : PositiveSpan) (d : ℕ) :
    let t := (d : ℝ) * PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    let M (fs : List RealValued) := CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν fs.get
    let Xs (X : SepTuple) := pushList TimeAxis.timeReflection X.val
    let Ys (Y : SepTuple) := pushList (translate (t • timeBasisVec)) Y.val
    volumeU ν (liftedWilsonMeasure L v k β) Z t =
      (∑ X ∈ Z.val.support, ∑ Y ∈ Z.val.support, conj (Z.val X) * Z.val Y *
        (M (Xs X ++ Ys Y) - M (Xs X) * M (Ys Y))).re := by
  let t := (d : ℝ) * PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  let M (fs : List RealValued) := CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν fs.get
  let z := Z.val
  let f (X : SepTuple) := pushList TimeAxis.timeReflection X.val
  let g (X : SepTuple) := pushList (translate (t • timeBasisVec)) X.val
  have hf (X : SepTuple) : M (f X) = M X.val := (oddGrid_marginals hL k v hβ hν X d).1
  have hg (X : SepTuple) : M (g X) = M X.val := (oddGrid_marginals hL k v hβ hν X d).2
  have realM (X : SepTuple) : conj (M X.val) = M X.val := by
    simp only [M,CutoffLimits.CenteredMomentsAndVolumeFirst.centredMoment_eq_ofReal_integral,Complex.conj_ofReal]
  let u := ∑ X ∈ z.support, z X * M X.val
  have hm : conj u * u = ∑ X ∈ z.support, ∑ Y ∈ z.support, conj (z X) * z Y * (M X.val * M Y.val) := by
    simp only [u,map_sum,map_mul,realM,Finset.sum_mul,Finset.mul_sum]
    conv_lhs => rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro X _
    apply Finset.sum_congr rfl
    intro Y _
    ring
  have hu : (conj u * u).re = ‖u‖^2 := by rw [← Complex.normSq_eq_conj_mul_self,Complex.ofReal_re,Complex.sq_norm]
  change (∑ X ∈ z.support,∑ Y ∈ z.support,conj (z X)*z Y*M (f X ++ g Y)).re - ‖u‖^2 =
    (∑ X ∈ z.support,∑ Y ∈ z.support,conj (z X)*z Y*(M (f X ++ g Y)-M (f X)*M (g Y))).re
  simp only [hf,hg,mul_sub,Finset.sum_sub_distrib,Complex.sub_re]
  rw [← hm,hu]


/-- A sufficient finite-volume slab estimate. The main prefactor is fixed before the
odd separation. The prefactor of the finite-volume error may depend on that separation.
The excited trace and the gap both refer to the same box spectrum. -/
def SlabEstimate (L k : ℕ) (β : ℝ) (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ))))
    (T : TorusData) (r : ℝ) : Prop :=
  ∀ Z : PositiveSpan, ∃ C : ℝ, ∀ n : ℕ, ∃ D : ℝ, ∀ᶠ v : ℕ in atTop,
    let V := volumeSide L k v
    let B := T.spectrum (cube V)
    let d := 2 * (n : ℝ) + 1
    (r : EReal) ≤ B.gap →
      volumeU ν (liftedWilsonMeasure L v k β) Z (d * PeriodicLattice.meshSize L (k : ℤ)) ≤
        C * Real.exp (-r * d) + D * Real.sqrt (1 / (V : ℝ) + B.thermal (V / 2))

def windowCovariance {a : ℝ} (ν μ : Measure (GaugeField a)) (X Y : SepTuple) (t : ℝ) : ℂ :=
  let M (fs : List RealValued) := CutoffLimits.centredMoment μ ν fs.get
  let f := pushList TimeAxis.timeReflection X.val
  let g := pushList (translate (t • timeBasisVec)) Y.val
  M (f ++ g) - M f * M g

/-- A test-by-test form of EV-L. Only individual real monomials in the actual
span have to be compared between the periodic and neutral positive measures. -/
def PairWindowEstimate (L k : ℕ) (β : ℝ) (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ))))
    (T : TorusData) (r : ℝ) : Prop :=
  ∀ Z : PositiveSpan, ∀ X Y : ↥Z.val.support, ∃ C : ℝ, ∀ n : ℕ, ∃ D : ℝ, ∀ᶠ v : ℕ in atTop,
    let V := volumeSide L k v
    let B := T.spectrum (cube V)
    let d := 2 * (n : ℝ) + 1
    (r : EReal) ≤ B.gap →
      ‖windowCovariance ν (liftedWilsonMeasure L v k β) X.val Y.val
          (d * PeriodicLattice.meshSize L (k : ℤ))‖ ≤
        C * Real.exp (-r * d) + D * Real.sqrt (1/(V : ℝ) + B.thermal (V/2))

theorem slabEstimate_of_pairWindows {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (T : TorusData) (r : ℝ) (h : PairWindowEstimate L k β ν T r) :
    SlabEstimate L k β ν T r := by
  intro Z
  let J := ↥Z.val.support
  let w (x y : J) := ‖Z.val x.val‖ * ‖Z.val y.val‖
  have pos (x y : J) : 0 ≤ w x y := mul_nonneg (norm_nonneg _) (norm_nonneg _)
  choose C hc using h Z
  refine ⟨∑ x : J,∑ y : J,w x y * C x y,fun n => ?_⟩
  choose D hd using fun x y : J => hc x y n
  refine ⟨∑ x : J,∑ y : J,w x y * D x y,?_⟩
  have hall := Filter.eventually_all.2 (fun x : J => Filter.eventually_all.2 (hd x))
  filter_upwards [hall,eventually_ge_atTop 1] with v hv hpos
  let V := volumeSide L k v
  let B := T.spectrum (cube V)
  let d := 2 * (n : ℝ) + 1
  let t := d * PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  let μ := liftedWilsonMeasure L v k β
  let E := Real.exp (-r*d)
  let δ := Real.sqrt (1/(V : ℝ)+B.thermal (V/2))
  change (r : EReal) ≤ B.gap → volumeU ν μ Z t ≤ (∑ x : J,∑ y : J,w x y * C x y)*E + (∑ x : J,∑ y : J,w x y * D x y)*δ
  intro hr
  have hsum : volumeU ν μ Z t = (∑ x : J,∑ y : J,conj (Z.val x.val) * Z.val y.val *
      windowCovariance ν μ x.val y.val t).re := by
    let H (x y : SepTuple) := conj (Z.val x) * Z.val y * windowCovariance ν μ x y t
    let summed (s : ℝ) := (∑ x ∈ Z.val.support,∑ y ∈ Z.val.support,
      conj (Z.val x)*Z.val y*windowCovariance ν μ x y s).re
    let step := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    have he : volumeU ν μ Z (((2*n+1 : ℕ) : ℝ)*step) = summed (((2*n+1 : ℕ) : ℝ)*step) :=
      volumeU_connected_sum hL k ⟨v,hpos⟩ hβ hν Z (2*n+1)
    rw [show ((2*n+1 : ℕ) : ℝ) = d by norm_num [d]] at he
    have hexp : volumeU ν μ Z t = (∑ x ∈ Z.val.support,∑ y ∈ Z.val.support,H x y).re := he
    rw [hexp]
    congr 1
    symm
    change (∑ x : J,∑ y : J,H x.val y.val) = ∑ x ∈ Z.val.support,∑ y ∈ Z.val.support,H x y
    calc
      _ = ∑ x : J,∑ y ∈ Z.val.support,H x.val y := Finset.sum_congr rfl fun x _ =>
        Finset.sum_coe_sort Z.val.support (H x.val)
      _ = _ := Finset.sum_coe_sort Z.val.support (fun x => ∑ y ∈ Z.val.support,H x y)
  rw [hsum]
  calc
    _ ≤ ∑ x : J,∑ y : J,w x y * ‖windowCovariance ν μ x.val y.val t‖ := by
      rw [Complex.re_sum]
      apply Finset.sum_le_sum
      intro x _
      rw [Complex.re_sum]
      apply Finset.sum_le_sum
      intro y _
      apply (Complex.re_le_norm _).trans_eq
      simp only [w,norm_mul,RingHomIsometric.norm_map]
    _ ≤ ∑ x : J,∑ y : J,w x y * (C x y * E + D x y * δ) := Finset.sum_le_sum fun x _ =>
      Finset.sum_le_sum fun y _ => mul_le_mul_of_nonneg_left (hv x y hr) (pos x y)
    _ = _ := by simp only [mul_add,←mul_assoc,Finset.sum_add_distrib,Finset.sum_mul,E,δ,V,B,d]


/-- Remove the distinguished vacuum term without choosing a basis of its complement. -/
def offVac {I : Type*} (o : I) (f : I → ℝ) (i : I) : ℝ := by
  classical
  exact if i = o then 0 else f i

/-- Spectral identification required of the actual neutral transfer on one cube.
The distinguished basis vector is the vacuum. Kernel eigenvectors may be padded with zeros. -/
structure NeutralResolution (β : ℝ) (V : ℕ) (B : BoxSpectrum) where
  Γ : CubicPeriodSublattice
  side : Γ.side = V
  top : B.top = ‖Γ.transfer TimeAxis.timeIdx β‖
  A : DiagonalTraces β (cube Γ.side)
  enumerates : Wilson.EnumeratesRatios B A.value (zeroFlux, 0)
  labels : Set (Γ.SliceL2 TimeAxis.timeIdx)
  basis : HilbertBasis labels ℂ (Γ.SliceL2 TimeAxis.timeIdx)
  vacuum : labels
  eigen : labels → ℝ
  vacuum_one : eigen vacuum = 1
  acts : ∀ i, normalizedNeutral Γ β B.top (basis i) = (eigen i : ℂ) • basis i
  nonneg : ∀ i, 0 ≤ eigen i
  slots : ∀ i, i ≠ vacuum → eigen i = 0 ∨ ∃ j : ℕ, j ≠ 0 ∧ eigen i = A.value (zeroFlux,j) / B.top
  thermal : ∀ a : ℕ, 3 ≤ a → ∃ t, HasSum (offVac vacuum (fun i => eigen i ^ a)) t ∧ t ≤ B.thermal a

/-- Transport the positive-slot index with its multiplicities, not just the
set of spectral values. The zero eigenspaces need not have the same dimension. -/
def releaseToRectangle (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (χ m : Flux) :
    Wilson.PositiveSlot (magneticTransfer Γ hβ m * electricProj Γ χ) ≃
      Wilson.PositiveSlot (rectSector (fun _ => Γ.side) β χ m) :=
  Equiv.sigmaCongrRight fun r => finCongr
    ((cube_sector_eigenspaces Γ hβ χ m (by exact_mod_cast r.property.ne')).some.finrank_eq.symm)

theorem release_sector_moments (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (χ m : Flux)
    (a : ℕ) (ha : 2 ≤ a) :
    HasSum (fun i : Wilson.PositiveSlot (magneticTransfer Γ hβ m * electricProj Γ χ) => i.1.val ^ a)
      (sectorWeight β (boxSides (cube Γ.side) a) χ m) := by
  have raw := boxSector_moments (cube Γ.side) ha hβ.le χ m
  rw [boxShape_cube] at raw
  exact (releaseToRectangle Γ hβ χ m).hasSum_iff.mpr raw

theorem release_neutralTail (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) (a : ℕ) (ha : 3 ≤ a) :
    let T := (rectangularTorusData hβ).choose
    let B := T.spectrum (cube Γ.side)
    (∑' i : Wilson.PositiveSlot (Γ.transfer μt β * electricProj Γ zeroFlux), (i.1.val / B.top) ^ a) - 1 ≤ B.thermal a := by
  have hs := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp
    ⟨Γ.lattice,Γ.periods_eq⟩
  have hv : (cube Γ.side).Valid := ⟨hs,hs,hs⟩
  let T := (rectangularTorusData hβ).choose
  let B := T.spectrum (cube Γ.side)
  have h := release_sector_moments Γ hβ zeroFlux zeroFlux a (by omega)
  rw [magneticTransfer_zero] at h
  have htail := h.div_const (B.top ^ a)
  simp_rw [← div_pow] at htail
  change _ - 1 ≤ B.thermal a
  rw [htail.tsum_eq]
  exact (rectangularDiagonalTraces (cube Γ.side) hv hβ.le).choose.neutralTail_le ha B
    ((rectangularTorusData hβ).choose_spec.1.weight _ hv a ha)


/-- The neutral normalizing constant on an arbitrary time circle lies between
one vacuum and one vacuum plus the signed thermal tail. -/
theorem neutralPartition_ratio {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) (a : ℕ) (ha : 3 ≤ a) :
    let R := cube Γ.side
    let B := (rectangularTorusData hβ).choose.spectrum R
    let z := sectorWeight β (boxSides R a) zeroFlux zeroFlux / B.top ^ a
    1 ≤ z ∧ z ≤ 1 + B.thermal a := by
  have hs := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp ⟨Γ.lattice,Γ.periods_eq⟩
  let R := cube Γ.side
  have hv : R.Valid := ⟨hs,hs,hs⟩
  let B := (rectangularTorusData hβ).choose.spectrum R
  let A := (rectangularDiagonalTraces R hv hβ.le).choose
  have he := (rectangularDiagonalTraces R hv hβ.le).choose_spec.1
  have hT := (rectangularTorusData hβ).choose_spec.1
  have top : B.top = A.value (zeroFlux,0) := (hT.top Γ).trans ((he.trans (calibrated_cubicNorm Γ hβ)).symm)
  have h := (A.trace zeroFlux a ha).div_const (B.top ^ a)
  have hz := h.summable.le_tsum 0 (fun i _ => div_nonneg (pow_nonneg (A.nonneg _) _) (pow_nonneg B.top_pos.le _))
  rw [h.tsum_eq] at hz
  change A.value (zeroFlux,0) ^ a / B.top ^ a ≤ _ at hz
  rw [← top,div_self (pow_pos B.top_pos a).ne'] at hz
  exact ⟨hz,by linarith only [A.neutralTail_le ha B (hT.weight R hv a ha)]⟩

/-- Restoring the finite partition function costs the vacuum product times its
excited mass. This bound allows zero error and zero reference expectation. -/
theorem divide_trace_error (x c : ℂ) {z E τ : ℝ} (hz : 1 ≤ z) (hu : z ≤ 1 + τ) (h : ‖x-c‖ ≤ E) :
    ‖x / (z : ℂ) - c‖ ≤ E + ‖c‖ * τ := by
  have hp : 0 < z := zero_lt_one.trans_le hz
  have hn : (z : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr hp.ne'
  have he : x / (z : ℂ) - c = ((x-c)-c * ((z : ℂ)-1)) / z := by field_simp; ring
  have hm : ‖(z : ℂ)-1‖ = z-1 := by
    rw [← Complex.ofReal_one,← Complex.ofReal_sub,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg (sub_nonneg.mpr hz)]
  rw [he,norm_div,Complex.norm_real,Real.norm_eq_abs,abs_of_pos hp]
  calc
    _ ≤ ‖(x-c)-c*((z:ℂ)-1)‖ := div_le_self (norm_nonneg _) hz
    _ ≤ ‖x-c‖ + ‖c*((z:ℂ)-1)‖ := norm_sub_le _ _
    _ ≤ _ := by rw [norm_mul,hm]; exact add_le_add h (mul_le_mul_of_nonneg_left (by linarith) (norm_nonneg _))


/-- A common spectral basis for the two kernel conventions. Positive eigenvalues
carry their geometric multiplicities. The remaining basis vectors lie in the kernel. -/
structure SectorResolution {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (S : H →L[ℂ] H) (B : BoxSpectrum) (v : ℕ → ℝ) where
  labels : Set H
  basis : HilbertBasis labels ℂ H
  vacuum : labels
  eigen : labels → ℝ
  vacuum_one : eigen vacuum = 1
  acts : ∀ i, (((B.top⁻¹ : ℝ) : ℂ) • S) (basis i) = (eigen i : ℂ) • basis i
  nonneg : ∀ i, 0 ≤ eigen i
  slots : ∀ i, i ≠ vacuum → eigen i = 0 ∨ ∃ j : ℕ, j ≠ 0 ∧ eigen i = v j / B.top
  thermal : ∀ a : ℕ, 3 ≤ a → ∃ t, HasSum (offVac vacuum (fun i => eigen i ^ a)) t ∧ t ≤ B.thermal a

theorem sectorResolution_of_slots {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (S : H →L[ℂ] H) (hc : IsCompactOperator S) (hp : S.IsPositive) (B : BoxSpectrum)
    (v : ℕ → ℝ) (ht : B.top = v 0) (labels : EncodesSlots S v)
    (thermal : ∀ d : ℕ, 3 ≤ d → ∃ t, HasSum (fun i : Wilson.PositiveSlot S => (i.1.val / B.top) ^ d) t ∧
      t - 1 ≤ B.thermal d) : Nonempty (SectorResolution S B v) := by
  classical
  obtain ⟨w,b,j,hj,he,h₀⟩ := exists_positive_slot_basis S hc hp
  obtain ⟨code,inj,hit,off⟩ := labels
  have hr : 0 ∈ Set.range code := by
    by_contra h
    exact B.top_pos.ne' (ht.trans (off 0 h))
  obtain ⟨o,ho⟩ := hr
  let a : w → ℝ := Function.extend j (fun i => i.1.val / B.top) 0
  have aeig (i : Wilson.PositiveSlot S) : a (j i) = i.1.val / B.top := hj.extend_apply _ _ i
  have atop : a (j o) = 1 := by rw [aeig,← hit o,ho,← ht,div_self B.top_pos.ne']
  refine ⟨⟨w,b,j o,a,atop,?_,?_,?_,?_⟩⟩
  · intro p
    by_cases h : p ∈ Set.range j
    · obtain ⟨i,rfl⟩ := h
      rw [ContinuousLinearMap.smul_apply,he,aeig,smul_smul]
      congr 1
      push_cast
      ring
    · rw [ContinuousLinearMap.smul_apply,h₀ p h,smul_zero,
        show a p = 0 from Function.extend_apply' _ _ _ h,Complex.ofReal_zero,zero_smul]
  · intro p
    by_cases h : p ∈ Set.range j
    · obtain ⟨i,rfl⟩ := h
      rw [aeig]
      exact div_nonneg i.1.property.le B.top_pos.le
    · rw [show a p = 0 from Function.extend_apply' _ _ _ h]
  · intro p hp'
    by_cases h : p ∈ Set.range j
    · obtain ⟨i,rfl⟩ := h
      refine Or.inr ⟨code i,fun hi => hp' (congrArg j (inj (hi.trans ho.symm))),?_⟩
      rw [aeig,hit]
    · exact Or.inl (Function.extend_apply' _ _ _ h)
  · intro d hd
    obtain ⟨t,hsum,hbd⟩ := thermal d hd
    have hall : HasSum (fun p => a p ^ d) t := by
      apply (hj.hasSum_iff (fun p hp' => by change a p ^ d = 0; rw [show a p = 0 from Function.extend_apply' _ _ _ hp',zero_pow (by omega : d ≠ 0)])).1
      exact hsum.congr_fun fun i => by change a (j i) ^ d = _; rw [aeig]
    refine ⟨_,(hall.sub (hasSum_ite_eq (j o) (1 : ℝ))).congr_fun ?_,hbd⟩
    intro p
    by_cases h : p = j o <;> simp [offVac,h,atop]

/-- The neutral basis on the exact Hilbert space in which the marked edge
operators act. Its gap and excited trace are the W5 quantities. -/
theorem markedSectorResolution {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) :
    let R := cube Γ.side
    let T := (rectangularTorusData hβ).choose
    ∃ A : DiagonalTraces β R, Wilson.EnumeratesRatios (T.spectrum R) A.value (zeroFlux,0) ∧
      Nonempty (SectorResolution (rectSector (fun _ => Γ.side) β zeroFlux zeroFlux)
        (T.spectrum R) (fun i => A.value (zeroFlux,i))) := by
  have hs := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp
    ⟨Γ.lattice,Γ.periods_eq⟩
  let R := cube Γ.side
  have hv : R.Valid := ⟨hs,hs,hs⟩
  let T := (rectangularTorusData hβ).choose
  let A := (rectangularDiagonalTraces R hv hβ.le).choose
  have hA := (rectangularDiagonalTraces R hv hβ.le).choose_spec
  have st := (rectangularTorusData hβ).choose_spec
  have labels : EncodesSlots (rectSector (boxShape R) β zeroFlux zeroFlux) (fun i => A.value (zeroFlux,i)) := hA.2 zeroFlux
  rw [show boxShape R = fun _ => Γ.side from boxShape_cube _] at labels
  refine ⟨A,st.2 R hv,sectorResolution_of_slots _ (rectSector_compact _ _ _ _) (rectSector_positive _ hβ.le _ _)
    (T.spectrum R) _ ((st.1.top Γ).trans ((hA.1.trans (calibrated_cubicNorm Γ hβ)).symm)) labels ?_⟩
  intro d hd
  have hh := boxSector_moments R (by omega : 2 ≤ d) hβ.le zeroFlux zeroFlux
  rw [show boxShape R = fun _ => Γ.side from boxShape_cube _] at hh
  have hsum := hh.div_const ((T.spectrum R).top ^ d)
  simp_rw [← div_pow] at hsum
  exact ⟨_,hsum,A.neutralTail_le hd _ (st.1.weight R hv d hd)⟩


section WindowCovariance

open scoped InnerProductSpace
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Subtract both vacuum one-point functions. This estimate applies to complex
slab operators with no adjoint or positivity requirement on either insertion. -/
theorem vacuum_covariance {B : BoxSpectrum} {β : ℝ} {R : Box} (A : DiagonalTraces β R)
    (hb : Wilson.EnumeratesRatios B A.value (zeroFlux,0)) (S : H →L[ℂ] H)
    (Q : SectorResolution S B (fun i => A.value (zeroFlux,i)))
    (T : H →L[ℂ] H) (hT : T = ((B.top⁻¹ : ℝ) : ℂ) • S) (hs : T.IsSymmetric)
    {r : ℝ} (hr : (r : EReal) ≤ B.gap) (F G : H →L[ℂ] H) (d : ℕ) :
    let u := Q.basis Q.vacuum
    ‖⟪u,F ((T ^ d) (G u))⟫_ℂ - ⟪u,F u⟫_ℂ * ⟪u,G u⟫_ℂ‖ ≤
      2 * ‖F‖ * ‖G‖ * Real.exp (-r * d) := by
  let u := Q.basis Q.vacuum
  let z := ⟪u,G u⟫_ℂ
  let g := G u - z • u
  have unit : ‖u‖ = 1 := Q.basis.orthonormal.norm_eq_one _
  have uu : ⟪u,u⟫_ℂ = 1 := inner_self_eq_one_of_norm_eq_one unit
  have gu : ⟪u,g⟫_ℂ = 0 := by simp only [g,z,inner_sub_right,inner_smul_right,uu,mul_one,sub_self]
  have hG : ‖G u‖ ≤ ‖G‖ := by simpa only [unit,mul_one] using G.le_opNorm u
  have hz : ‖z‖ ≤ ‖G‖ := (norm_inner_le_norm _ _).trans (by simpa only [unit,one_mul] using hG)
  have hg : ‖g‖ ≤ 2 * ‖G‖ := calc
    _ ≤ ‖G u‖ + ‖z • u‖ := norm_sub_le _ _
    _ = ‖G u‖ + ‖z‖ := by rw [norm_smul,unit,mul_one]
    _ ≤ _ := by linarith
  have eig (i) : T (Q.basis i) = (Q.eigen i : ℂ) • Q.basis i := hT ▸ Q.acts i
  have fix : T u = u := by simpa only [u,Q.vacuum_one,Complex.ofReal_one,one_smul] using eig Q.vacuum
  have pfix (n : ℕ) : (T ^ n) u = u := by
    induction n with
    | zero => rfl
    | succ n ih => rw [pow_succ',mul_apply_eq_comp,ih,fix]
  have bounds (i : Q.labels) (hi : i ≠ Q.vacuum) : Q.eigen i ≤ Real.exp (-r) := by
    rcases Q.slots i hi with h|⟨j,hj,h⟩
    · rw [h]; exact (Real.exp_pos _).le
    · by_cases hpos : 0 < A.value (zeroFlux,j)
      · have hpos' : 0 < Q.eigen i := h ▸ div_pos hpos B.top_pos
        have hh := EReal.coe_le_coe_iff.mp (hr.trans (A.gap_le_neutralSlot B hb hj hpos))
        rw [← h,one_div,Real.log_inv] at hh
        exact (Real.log_le_iff_le_exp hpos').mp (by linarith)
      · rw [h,le_antisymm (not_lt.mp hpos) (A.nonneg _),zero_div]
        exact (Real.exp_pos _).le
  have decay := vacuumComplement_power_le T hs Q.basis Q.vacuum Q.eigen eig Q.nonneg
    (Real.exp_pos _).le bounds g gu d
  have eqn : ⟪u,F ((T ^ d) (G u))⟫_ℂ - ⟪u,F u⟫_ℂ * z = ⟪u,F ((T ^ d) g)⟫_ℂ := by
    simp only [g,map_sub,map_smul,inner_sub_right,inner_smul_right,pfix]
    ring
  change ‖⟪u,F ((T ^ d) (G u))⟫_ℂ - ⟪u,F u⟫_ℂ * z‖ ≤ _
  rw [eqn]
  calc
    _ ≤ ‖u‖ * ‖F ((T ^ d) g)‖ := norm_inner_le_norm _ _
    _ ≤ ‖F‖ * (Real.exp (-r) ^ d * ‖g‖) := by
      rw [unit,one_mul]
      exact (F.le_opNorm _).trans (mul_le_mul_of_nonneg_left decay (norm_nonneg F))
    _ ≤ ‖F‖ * (Real.exp (-r) ^ d * (2 * ‖G‖)) :=
      mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hg (pow_nonneg (Real.exp_pos _).le _)) (norm_nonneg F)
    _ = _ := by rw [← Real.exp_nat_mul,mul_comm (d : ℝ)]; ring

end WindowCovariance


/-- The same positive slots occurring in W5 form a full spectral resolution
of the release's neutral transfer on the cube. -/
theorem release_neutralResolution (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    {B : BoxSpectrum} (A : DiagonalTraces β (cube Γ.side)) (ht : B.top = A.value (zeroFlux,0))
    (hnorm : B.top = ‖Γ.transfer μt β‖) (hb : Wilson.EnumeratesRatios B A.value (zeroFlux,0))
    (hweight : ∀ d : ℕ,3 ≤ d → B.weight d = kappaWeight β (boxSides (cube Γ.side) d))
    (labels : EncodesSlots (rectSector (boxShape (cube Γ.side)) β zeroFlux zeroFlux) (fun i => A.value (zeroFlux,i))) :
    Nonempty (NeutralResolution β Γ.side B) := by
  let S := magneticTransfer Γ hβ zeroFlux * electricProj Γ zeroFlux
  have hsp := releaseSector_spectral Γ hβ zeroFlux zeroFlux
  rw [boxShape_cube] at labels
  obtain ⟨c,hc,hon,hoff⟩ := labels
  let e := releaseToRectangle Γ hβ zeroFlux zeroFlux
  have enc : EncodesSlots S (fun i => A.value (zeroFlux,i)) := by
    refine ⟨fun i => c (e i),hc.comp e.injective,fun i => hon (e i),fun j hj => hoff j ?_⟩
    rintro ⟨i,rfl⟩
    exact hj ⟨e.symm i,congrArg c (e.apply_symm_apply i)⟩
  have hthermal (d : ℕ) (hd : 3 ≤ d) := (release_sector_moments Γ hβ zeroFlux zeroFlux d (by omega)).div_const (B.top ^ d)
  obtain ⟨Q⟩ := sectorResolution_of_slots S hsp.1 hsp.2 B _ ht enc (fun d hd => by
    have hh := hthermal d hd
    simp_rw [← div_pow] at hh
    exact ⟨_,hh,A.neutralTail_le hd B (hweight d hd)⟩)
  refine ⟨⟨Γ,rfl,hnorm,A,hb,Q.labels,Q.basis,Q.vacuum,Q.eigen,Q.vacuum_one,?_,Q.nonneg,Q.slots,Q.thermal⟩⟩
  intro i
  simpa only [normalizedNeutral,S,magneticTransfer_zero] using Q.acts i


theorem calibrated_neutralResolution (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β) :
    Nonempty (NeutralResolution β Γ.side ((rectangularTorusData hβ).choose.spectrum (cube Γ.side))) := by
  have hs := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds Γ.side Γ.one_le_side).mp
    ⟨Γ.lattice,Γ.periods_eq⟩
  have hv : (cube Γ.side).Valid := ⟨hs,hs,hs⟩
  let A := (rectangularDiagonalTraces (cube Γ.side) hv hβ.le).choose
  have hA := (rectangularDiagonalTraces (cube Γ.side) hv hβ.le).choose_spec
  have hT := (rectangularTorusData hβ).choose_spec
  have hnorm := hT.1.top Γ
  exact release_neutralResolution Γ hβ A (hnorm.trans ((hA.1.trans (calibrated_cubicNorm Γ hβ)).symm))
    hnorm (hT.2 _ hv) (hT.1.weight _ hv) (hA.2 zeroFlux)

open scoped InnerProductSpace in
theorem basis_insertedTrace_tail {H I : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (b : HilbertBasis I ℂ H) (o : I) (eigen : I → ℝ) (hon : eigen o = 1) (hn : ∀ i, 0 ≤ eigen i)
    (X : H →L[ℂ] H) (a : ℕ) (t tail : ℝ) (ht : HasSum (offVac o (fun i => eigen i ^ a)) t) (hle : t ≤ tail) :
    ∃ err : ℂ, HasSum (fun i => ((eigen i ^ a : ℝ) : ℂ) * ⟪b i,X (b i)⟫_ℂ)
      (⟪b o,X (b o)⟫_ℂ + err) ∧ ‖err‖ ≤ ‖X‖ * tail := by

  classical
  let c (i : I) := ⟪b i,X (b i)⟫_ℂ
  let f (i : I) := offVac o (fun j => eigen j ^ a) i
  let r (i : I) : ℂ := (f i : ℂ) * c i
  have non (i) : 0 ≤ f i := by
    by_cases h : i = o <;> simp [f,offVac,h,pow_nonneg (hn i)]
  have cb (i) : ‖c i‖ ≤ ‖X‖ := by
    calc
      _ ≤ ‖b i‖ * ‖X (b i)‖ := norm_inner_le_norm _ _
      _ ≤ ‖b i‖ * (‖X‖ * ‖b i‖) := mul_le_mul_of_nonneg_left (X.le_opNorm _) (norm_nonneg _)
      _ = _ := by rw [b.orthonormal.norm_eq_one,one_mul,mul_one]
  have hbd (i) : ‖r i‖ ≤ ‖X‖ * f i := by
    change ‖(f i : ℂ) * c i‖ ≤ _
    rw [norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg (non i),mul_comm (‖X‖)]
    exact mul_le_mul_of_nonneg_left (cb i) (non i)
  have hs : Summable r := Summable.of_norm_bounded (ht.summable.mul_left ‖X‖) hbd
  have hnormsum : Summable (fun i => ‖r i‖) := Summable.of_nonneg_of_le (fun i => norm_nonneg _) hbd (ht.summable.mul_left ‖X‖)
  refine ⟨∑' i, r i,?_,?_⟩
  · apply ((hasSum_ite_eq o (c o)).add hs.hasSum).congr_fun
    intro i
    by_cases h : i = o
    · subst i
      simp [c,r,f,offVac,hon]
    · simp [c,r,f,offVac,h]
  · exact (norm_tsum_le_tsum_norm hnormsum).trans
      ((hasSum_le hbd hnormsum.hasSum (ht.mul_left ‖X‖)).trans (mul_le_mul_of_nonneg_left hle (norm_nonneg _)))

open scoped InnerProductSpace in
/-- The actual marked-sector trace, with its vacuum product subtracted. The
near arc controls the connected term and the far arc controls the trace error. -/
theorem sector_trace_covariance {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    {B : BoxSpectrum} {β : ℝ} {R : Box} (A : DiagonalTraces β R)
    (hb : Wilson.EnumeratesRatios B A.value (zeroFlux,0)) (S : H →L[ℂ] H)
    (Q : SectorResolution S B (fun i => A.value (zeroFlux,i)))
    (T : H →L[ℂ] H) (ht : T = ((B.top⁻¹ : ℝ) : ℂ) • S) (hs : T.IsSymmetric) (hc : ‖T‖ ≤ 1)
    {r : ℝ} (hr : (r : EReal) ≤ B.gap) (F G : H →L[ℂ] H) (d a : ℕ) (ha : 3 ≤ a) :
    let u := Q.basis Q.vacuum
    let X := F * T ^ d * G
    ∃ tr : ℂ, HasSum (fun i => ((Q.eigen i ^ a : ℝ) : ℂ) * ⟪Q.basis i,X (Q.basis i)⟫_ℂ) tr ∧
      ‖tr - ⟪u,F u⟫_ℂ * ⟪u,G u⟫_ℂ‖ ≤ ‖F‖ * ‖G‖ * (2 * Real.exp (-r * d) + B.thermal a) := by
  let u := Q.basis Q.vacuum
  let X := F * T ^ d * G
  obtain ⟨t,h,hb'⟩ := Q.thermal a ha
  obtain ⟨err,he,herr⟩ := basis_insertedTrace_tail Q.basis Q.vacuum Q.eigen Q.vacuum_one Q.nonneg X a _ _ h hb'
  haveI : Nontrivial H := nontrivial_of_ne u 0 (by
    intro hz
    have hh : ‖u‖ = 1 := Q.basis.orthonormal.norm_eq_one _
    rw [hz,norm_zero] at hh
    exact zero_ne_one hh)
  have p := (norm_pow_le T d).trans (pow_le_one₀ (norm_nonneg T) hc)
  have xx : ‖X‖ ≤ ‖F‖ * ‖G‖ := by
    apply (norm_mul_le _ _).trans
    apply mul_le_mul_of_nonneg_right _ (norm_nonneg G)
    exact (norm_mul_le _ _).trans ((mul_le_mul_of_nonneg_left p (norm_nonneg F)).trans_eq (mul_one _))
  have cov := vacuum_covariance A hb S Q T ht hs hr F G d
  refine ⟨_,he,?_⟩
  change ‖⟪u,X u⟫_ℂ + err - ⟪u,F u⟫_ℂ * ⟪u,G u⟫_ℂ‖ ≤ _
  rw [add_sub_right_comm]
  calc
    _ ≤ ‖⟪u,X u⟫_ℂ - ⟪u,F u⟫_ℂ * ⟪u,G u⟫_ℂ‖ + ‖err‖ := norm_add_le _ _
    _ ≤ 2 * ‖F‖ * ‖G‖ * Real.exp (-r * d) + (‖F‖ * ‖G‖) * B.thermal a :=
      add_le_add cov (herr.trans (mul_le_mul_of_nonneg_right xx (B.thermal_nonneg a)))
    _ = _ := by ring

open scoped InnerProductSpace in
/-- A covariance estimate on the same cubic spatial space as the actual
inhomogeneous marked kernels. The basis is chosen once for all operators and separations. -/
theorem markedSector_covariance {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) :
    let R := cube Γ.side
    let B := (rectangularTorusData hβ).choose.spectrum R
    let S := rectSector (fun _ => Γ.side) β zeroFlux zeroFlux
    let T := ((B.top⁻¹ : ℝ) : ℂ) • S
    ∃ (A : DiagonalTraces β R) (Q : SectorResolution S B (fun i => A.value (zeroFlux,i))), Wilson.EnumeratesRatios B A.value (zeroFlux,0) ∧
      ∀ r : ℝ, (r : EReal) ≤ B.gap → ∀ F G : Kernel.Space (rectHaar (fun _ => Γ.side)) →L[ℂ] Kernel.Space (rectHaar (fun _ => Γ.side)),
        ∀ d a : ℕ, 3 ≤ a →
          ∃ tr : ℂ, HasSum (fun i => ((Q.eigen i ^ a : ℝ) : ℂ) *
              ⟪Q.basis i,(F * T ^ d * G) (Q.basis i)⟫_ℂ) tr ∧
            ‖tr - ⟪Q.basis Q.vacuum,F (Q.basis Q.vacuum)⟫_ℂ * ⟪Q.basis Q.vacuum,G (Q.basis Q.vacuum)⟫_ℂ‖ ≤
              ‖F‖ * ‖G‖ * (2 * Real.exp (-r * d) + B.thermal a) := by
  let B := (rectangularTorusData hβ).choose.spectrum (cube Γ.side)
  let S := rectSector (fun _ => Γ.side) β zeroFlux zeroFlux
  let T := ((B.top⁻¹ : ℝ) : ℂ) • S
  obtain ⟨A,hA,⟨Q⟩⟩ := markedSectorResolution hβ Γ
  have hn : B.top = ‖S‖ := by
    have h := calibrated_cubicNorm Γ hβ
    rw [boxShape_cube] at h
    exact (rectangularTorusData hβ).choose_spec.1.top Γ |>.trans h.symm
  have hc : ‖T‖ ≤ 1 := by
    rw [show ‖T‖ = _ from norm_smul _ _,Complex.norm_real,Real.norm_eq_abs,abs_of_pos (inv_pos.mpr B.top_pos),← hn,inv_mul_cancel₀ B.top_pos.ne']
  have hs : T.IsSymmetric := by
    apply ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mp
    change star (((B.top⁻¹ : ℝ) : ℂ) • S) = _
    rw [star_smul,show star ((B.top⁻¹ : ℝ) : ℂ) = ((B.top⁻¹ : ℝ) : ℂ) from Complex.conj_ofReal _,
      show star S = S from (rectSector_positive _ hβ.le zeroFlux zeroFlux).isSelfAdjoint.star_eq]
  exact ⟨A,Q,hA,fun r hr F G d a ha => sector_trace_covariance A hA S Q T rfl hs hc hr F G d a ha⟩


open scoped InnerProductSpace in
/-- EV-L's neutral two-slab estimate for actual homogeneous or inhomogeneous
electric-background integrals. The empty arcs are explicit lists of unmarked edges. -/
theorem split_marked_covariance {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) :
    let n : spatialAxis → ℕ := fun _ => Γ.side
    let R := cube Γ.side
    let B := (rectangularTorusData hβ).choose.spectrum R
    let S := rectSector n β zeroFlux zeroFlux
    ∃ (A : DiagonalTraces β R) (Q : SectorResolution S B (fun i => A.value (zeroFlux,i))), Wilson.EnumeratesRatios B A.value (zeroFlux,0) ∧
      ∀ {p : ℕ} (F : Fin (p+2) → LayerMark n), (∀ i,CentreBlind (F i)) →
        (∀ e u v g,F 0 ((u,rectFlip e v),g) = F 0 ((u,v),g)) →
        ∀ (U W : List (LayerMark n)) (d a : ℕ), 3 ≤ a →
          List.ofFn F = U ++ List.replicate d 1 ++ W ++ List.replicate a 1 →
          ∀ r : ℝ, (r : EReal) ≤ B.gap →
          let o := Q.basis Q.vacuum
          ‖(((B.top⁻¹ : ℝ) : ℂ) ^ (p+2)) * rawMarkedMean β zeroFlux F -
            ⟪o,slabProduct n β B.top zeroFlux U o⟫_ℂ * ⟪o,slabProduct n β B.top zeroFlux W o⟫_ℂ‖ ≤
              (U.map fun f => ‖f‖).prod * (W.map fun f => ‖f‖).prod * (2 * Real.exp (-r * d) + B.thermal a) := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let B := (rectangularTorusData hβ).choose.spectrum (cube Γ.side)
  let S := rectSector n β zeroFlux zeroFlux
  let T := ((B.top⁻¹ : ℝ) : ℂ) • S
  obtain ⟨A,Q,hA,hQ⟩ := markedSector_covariance hβ Γ
  refine ⟨A,Q,hA,?_⟩
  intro p F hb hcut U W d a ha shape r hr
  let M := slabProduct n β B.top zeroFlux
  have hn : ‖rectSymOperator n β zeroFlux‖ = B.top :=
    ((rectSymOperator_cube_norm Γ hβ zeroFlux).trans (congrArg norm (magneticTransfer_zero Γ hβ))).trans
      ((rectangularTorusData hβ).choose_spec.1.top Γ).symm
  obtain ⟨tr,htr,hle⟩ := hQ r hr (M U) (M W) d a ha
  have hraw := normalized_mark_trace β B.top zeroFlux F hb hcut Q.basis
  have prod' : M (List.ofFn F) = M U * T ^ d * M W * T ^ a := by
    rw [shape]
    simp only [M,slabProduct,List.map_append,List.prod_append,List.map_replicate,List.prod_replicate,projectedLayer_one,T,S]
  have he (i : Q.labels) (t : ℕ) : (T ^ t) (Q.basis i) = (Q.eigen i : ℂ)^t • Q.basis i := by
    induction t with
    | zero => simp
    | succ t ih =>
      rw [pow_succ',mul_apply_eq_comp,ih,map_smul,Q.acts,smul_smul,pow_succ]
  have eqn : (((B.top⁻¹ : ℝ) : ℂ) ^ (p+2)) * rawMarkedMean β zeroFlux F = tr := by
    apply HasSum.unique hraw
    apply htr.congr_fun
    intro i
    change ⟪Q.basis i,M (List.ofFn F) (Q.basis i)⟫_ℂ = _
    rw [prod',mul_apply_eq_comp,he,map_smul,inner_smul_right,Complex.ofReal_pow]
  rw [eqn]
  exact hle.trans (mul_le_mul_of_nonneg_right
    (mul_le_mul (slabProduct_bound β zeroFlux B.top_pos hn U) (slabProduct_bound β zeroFlux B.top_pos hn W)
      (norm_nonneg _) (List.prod_nonneg (fun x hx => by obtain ⟨f,_,rfl⟩ := List.mem_map.mp hx; exact norm_nonneg f)))
    (add_nonneg (mul_nonneg (by norm_num) (Real.exp_pos _).le) (B.thermal_nonneg a)))


open scoped InnerProductSpace in
/-- Divide the actual two-slab electric average by its neutral partition
function. Both vacuum one-point functions use a single volume-dependent vacuum. -/
theorem normalized_split_covariance {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) :
    let n : spatialAxis → ℕ := fun _ => Γ.side
    let R := cube Γ.side
    let B := (rectangularTorusData hβ).choose.spectrum R
    let S := rectSector n β zeroFlux zeroFlux
    ∃ (A : DiagonalTraces β R) (Q : SectorResolution S B (fun i => A.value (zeroFlux,i))), Wilson.EnumeratesRatios B A.value (zeroFlux,0) ∧
      ∀ {p : ℕ} (F : Fin (p+2) → LayerMark n), (∀ i,CentreBlind (F i)) →
        (∀ e u v g,F 0 ((u,rectFlip e v),g) = F 0 ((u,v),g)) →
        ∀ (U W : List (LayerMark n)) (d a : ℕ), 3 ≤ a →
          List.ofFn F = U ++ List.replicate d 1 ++ W ++ List.replicate a 1 →
          ∀ r : ℝ, (r : EReal) ≤ B.gap →
          let o := Q.basis Q.vacuum
          ‖rawMarkedMean β zeroFlux F / (sectorWeight β (boxSides R (p+2)) zeroFlux zeroFlux : ℂ) -
            ⟪o,slabProduct n β B.top zeroFlux U o⟫_ℂ * ⟪o,slabProduct n β B.top zeroFlux W o⟫_ℂ‖ ≤
              (U.map fun f => ‖f‖).prod * (W.map fun f => ‖f‖).prod * (2 * Real.exp (-r * d) + 2 * B.thermal a) := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let R := cube Γ.side
  let B := (rectangularTorusData hβ).choose.spectrum R
  obtain ⟨A,Q,hA,hQ⟩ := split_marked_covariance hβ Γ
  refine ⟨A,Q,hA,?_⟩
  intro p F hb hcut U W d a ha shape r hr
  let M := slabProduct n β B.top zeroFlux
  let C (l : List (LayerMark n)) := (l.map fun f => ‖f‖).prod
  let u := Q.basis Q.vacuum
  let vac (l : List (LayerMark n)) := ⟪u,M l u⟫_ℂ
  let w := sectorWeight β (boxSides R (p+2)) zeroFlux zeroFlux
  let z := w / B.top ^ (p+2)
  let x := (((B.top⁻¹ : ℝ) : ℂ) ^ (p+2)) * rawMarkedMean β zeroFlux F
  have leng := congrArg List.length shape
  simp only [List.length_ofFn,List.length_append,List.length_replicate] at leng
  have hp : 3 ≤ p+2 := by omega
  have rat := neutralPartition_ratio hβ Γ (p+2) hp
  have hlow : 1 ≤ z := rat.1
  have hτ := B.thermal_antitone ha (show a ≤ p+2 by omega)
  have hhigh : z ≤ 1 + B.thermal a := rat.2.trans (add_le_add_right hτ _)
  have ht : 0 < w := by
    have h : 0 < w / B.top ^ (p+2) := zero_lt_one.trans_le hlow
    exact (div_pos_iff_of_pos_right (pow_pos B.top_pos _)).mp h
  have hn : ‖rectSymOperator n β zeroFlux‖ = B.top :=
    ((rectSymOperator_cube_norm Γ hβ zeroFlux).trans (congrArg norm (magneticTransfer_zero Γ hβ))).trans
      ((rectangularTorusData hβ).choose_spec.1.top Γ).symm
  have unit : ‖u‖ = 1 := Q.basis.orthonormal.norm_eq_one _
  have bound (l) : ‖vac l‖ ≤ C l := calc
    _ ≤ ‖u‖ * ‖M l u‖ := norm_inner_le_norm _ _
    _ ≤ ‖M l‖ := by simpa only [unit,one_mul,mul_one] using (M l).le_opNorm u
    _ ≤ C l := slabProduct_bound β zeroFlux B.top_pos hn l
  have vv : ‖vac U * vac W‖ ≤ C U * C W := by
    rw [norm_mul]
    exact mul_le_mul (bound U) (bound W) (norm_nonneg _) ((norm_nonneg _).trans (bound U))
  have h := divide_trace_error x (vac U * vac W) hlow hhigh (hQ F hb hcut U W d a ha shape r hr)
  have eqn : x / (z : ℂ) = rawMarkedMean β zeroFlux F / (w : ℂ) := by
    change _ * rawMarkedMean β zeroFlux F / ((w / B.top ^ (p+2) : ℝ) : ℂ) = _
    rw [Complex.ofReal_div,Complex.ofReal_pow,Complex.ofReal_inv,inv_pow]
    field_simp [Complex.ofReal_ne_zero.mpr B.top_pos.ne',Complex.ofReal_ne_zero.mpr ht.ne']
  rw [← eqn]
  change ‖x / (z : ℂ) - vac U * vac W‖ ≤ C U*C W*(2*Real.exp (-r*d)+2*B.thermal a)
  calc
    _ ≤ C U*C W*(2*Real.exp (-r*d)+B.thermal a) + ‖vac U*vac W‖*B.thermal a := h
    _ ≤ C U*C W*(2*Real.exp (-r*d)+B.thermal a) + (C U*C W)*B.thermal a := add_le_add le_rfl (mul_le_mul_of_nonneg_right vv (B.thermal_nonneg _))
    _ = _ := by ring

open scoped InnerProductSpace in
/-- Empty leading or trailing layers leave the one-point value of a word
unchanged in the very vacuum used by the joint neutral trace. -/
theorem padded_vacuum_word {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice)
    {A : DiagonalTraces β (cube Γ.side)} (Q : SectorResolution (rectSector (fun _ => Γ.side) β zeroFlux zeroFlux)
      ((rectangularTorusData hβ).choose.spectrum (cube Γ.side)) (fun i => A.value (zeroFlux,i)))
    (U : List (LayerMark (fun _ => Γ.side))) (l r : ℕ) :
    let B := (rectangularTorusData hβ).choose.spectrum (cube Γ.side)
    let M := slabProduct (fun _ => Γ.side) β B.top zeroFlux
    let o := Q.basis Q.vacuum
    ⟪o,M (List.replicate l 1 ++ U ++ List.replicate r 1) o⟫_ℂ = ⟪o,M U o⟫_ℂ := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let B := (rectangularTorusData hβ).choose.spectrum (cube Γ.side)
  let S := rectSector n β zeroFlux zeroFlux
  let T := ((B.top⁻¹ : ℝ) : ℂ) • S
  let o := Q.basis Q.vacuum
  let M := slabProduct n β B.top zeroFlux
  have hs : T.IsSymmetric := by
    apply ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mp
    change star (((B.top⁻¹ : ℝ) : ℂ) • S) = _
    rw [star_smul,show star ((B.top⁻¹ : ℝ) : ℂ) = ((B.top⁻¹ : ℝ) : ℂ) from Complex.conj_ofReal _,
      show star S = S from (rectSector_positive _ hβ.le zeroFlux zeroFlux).isSelfAdjoint.star_eq]
  have fix : T o = o := by simpa only [o,Q.vacuum_one,Complex.ofReal_one,one_smul] using Q.acts Q.vacuum
  have right (t : ℕ) : (T^t) o = o := by
    induction t with
    | zero => rfl
    | succ t ih => rw [pow_succ',mul_apply_eq_comp,ih,fix]
  have left (z : Kernel.Space (rectHaar n)) (t : ℕ) : ⟪o,(T^t) z⟫_ℂ = ⟪o,z⟫_ℂ := by
    induction t with
    | zero => rfl
    | succ t ih => rw [pow_succ',mul_apply_eq_comp,← hs.apply_clm,fix,ih]
  have prod' : M (List.replicate l 1 ++ U ++ List.replicate r 1) = T^l * M U * T^r := by
    simp only [M,slabProduct,List.map_append,List.prod_append,List.map_replicate,List.prod_replicate,projectedLayer_one,T,S]
  change ⟪o,M _ o⟫_ℂ = ⟪o,M U o⟫_ℂ
  rw [prod',mul_apply_eq_comp,right,mul_apply_eq_comp,left]


open scoped InnerProductSpace in
/-- A single marked word in the normalized neutral measure differs from its
own vacuum expectation by the thermal mass of the unmarked arc. The supplied
resolution can be the very one used for two disjoint words. -/
theorem normalized_single_window {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice)
    {A : DiagonalTraces β (cube Γ.side)} (Q : SectorResolution (rectSector (fun _ => Γ.side) β zeroFlux zeroFlux)
      ((rectangularTorusData hβ).choose.spectrum (cube Γ.side)) (fun i => A.value (zeroFlux,i)))
    {p : ℕ} (F : Fin (p+2) → LayerMark (fun _ => Γ.side)) (hb : ∀ i,CentreBlind (F i))
    (hcut : ∀ e u v g,F 0 ((u,rectFlip e v),g) = F 0 ((u,v),g))
    (U : List (LayerMark (fun _ => Γ.side))) (a : ℕ) (ha : 3 ≤ a)
    (shape : List.ofFn F = U ++ List.replicate a 1) :
    let n : spatialAxis → ℕ := fun _ => Γ.side
    let B := (rectangularTorusData hβ).choose.spectrum (cube Γ.side)
    let o := Q.basis Q.vacuum
    ‖rawMarkedMean β zeroFlux F / (sectorWeight β (boxSides (cube Γ.side) (p+2)) zeroFlux zeroFlux : ℂ) -
      ⟪o,slabProduct n β B.top zeroFlux U o⟫_ℂ‖ ≤ 2 * (U.map fun f => ‖f‖).prod * B.thermal a := by
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let B := (rectangularTorusData hβ).choose.spectrum (cube Γ.side)
  let T := ((B.top⁻¹ : ℝ) : ℂ) • rectSector n β zeroFlux zeroFlux
  let M := slabProduct n β B.top zeroFlux
  let o := Q.basis Q.vacuum
  let c := ⟪o,M U o⟫_ℂ
  let C := (U.map fun f => ‖f‖).prod
  let w := sectorWeight β (boxSides (cube Γ.side) (p+2)) zeroFlux zeroFlux
  let z := w / B.top ^ (p+2)
  let x := (((B.top⁻¹ : ℝ) : ℂ) ^ (p+2)) * rawMarkedMean β zeroFlux F
  have hn : ‖rectSymOperator n β zeroFlux‖ = B.top :=
    ((rectSymOperator_cube_norm Γ hβ zeroFlux).trans (congrArg norm (magneticTransfer_zero Γ hβ))).trans
      ((rectangularTorusData hβ).choose_spec.1.top Γ).symm
  have hM : ‖M U‖ ≤ C := slabProduct_bound β zeroFlux B.top_pos hn U
  have unit : ‖o‖ = 1 := Q.basis.orthonormal.norm_eq_one _
  have hc : ‖c‖ ≤ C := (norm_inner_le_norm _ _).trans <| by
    rw [unit,one_mul]
    exact ((M U).le_opNorm o).trans ((mul_le_mul_of_nonneg_right hM (norm_nonneg o)).trans_eq (by rw [unit,mul_one]))
  have leng := congrArg List.length shape
  simp only [List.length_ofFn,List.length_append,List.length_replicate] at leng
  have hrat := neutralPartition_ratio hβ Γ (p+2) (by omega)
  have lo : 1 ≤ z := hrat.1
  have hi : z ≤ 1+B.thermal a := hrat.2.trans (add_le_add_right (B.thermal_antitone ha (by omega)) _)
  have pos : 0 < w := (div_pos_iff_of_pos_right (pow_pos B.top_pos _)).mp (zero_lt_one.trans_le lo)
  have prod' : M (List.ofFn F) = M U * T^a := by
    rw [shape]
    simp only [M,slabProduct,List.map_append,List.prod_append,List.map_replicate,List.prod_replicate,projectedLayer_one,T]
  have he (i : Q.labels) (t : ℕ) : (T^t) (Q.basis i) = (Q.eigen i : ℂ)^t • Q.basis i := by
    induction t with
    | zero => simp
    | succ t ih => rw [pow_succ',mul_apply_eq_comp,ih,map_smul,Q.acts,smul_smul,pow_succ]
  obtain ⟨mass,hm,ht⟩ := Q.thermal a ha
  obtain ⟨err,hs,hh⟩ := basis_insertedTrace_tail Q.basis Q.vacuum Q.eigen Q.vacuum_one Q.nonneg (M U) a mass _ hm ht
  have hx : x = c + err := by
    apply HasSum.unique (normalized_mark_trace β B.top zeroFlux F hb hcut Q.basis)
    apply hs.congr_fun
    intro i
    change ⟪Q.basis i,M (List.ofFn F) (Q.basis i)⟫_ℂ = _
    rw [prod',mul_apply_eq_comp,he,map_smul,inner_smul_right,Complex.ofReal_pow]
  have bound : ‖x-c‖ ≤ C*B.thermal a := by
    rw [hx,add_sub_cancel_left]
    exact hh.trans (mul_le_mul_of_nonneg_right hM (B.thermal_nonneg _))
  have eqn : x / (z : ℂ) = rawMarkedMean β zeroFlux F / (w : ℂ) := by
    change _ * rawMarkedMean β zeroFlux F / ((w / B.top ^ (p+2) : ℝ) : ℂ) = _
    rw [Complex.ofReal_div,Complex.ofReal_pow,Complex.ofReal_inv,inv_pow]
    field_simp [Complex.ofReal_ne_zero.mpr B.top_pos.ne',Complex.ofReal_ne_zero.mpr pos.ne']
  change ‖rawMarkedMean β zeroFlux F / (w : ℂ) - c‖ ≤ 2*C*B.thermal a
  rw [← eqn]
  calc
    _ ≤ C*B.thermal a + ‖c‖*B.thermal a := divide_trace_error x c lo hi bound
    _ ≤ C*B.thermal a + C*B.thermal a := add_le_add le_rfl (mul_le_mul_of_nonneg_right hc (B.thermal_nonneg _))
    _ = _ := by ring


set_option maxHeartbeats 800000 in
open scoped InnerProductSpace in
/-- The normalized neutral estimate for two residue-supported families placed
anywhere in the half-circle used for averaging. The vacuum values and norm
bounds depend only on the two words, independently of their placements. -/
theorem normalized_cyclic_words {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) :
    let n : spatialAxis → ℕ := fun _ => Γ.side
    let R := cube Γ.side
    let B := (rectangularTorusData hβ).choose.spectrum R
    let S := rectSector n β zeroFlux zeroFlux
    ∃ (A : DiagonalTraces β R) (Q : SectorResolution S B (fun i => A.value (zeroFlux,i))), Wilson.EnumeratesRatios B A.value (zeroFlux,0) ∧
      ∀ {p u w : ℕ} (F G : ZMod (p+2) → LayerMark n) (b c : ZMod (p+2)),
        (∀ x,CentreBlind (F x)) → (∀ x,CentreBlind (G x)) →
        (∀ x,x ∉ Set.range (fun j : Fin u => b+(j.val : ZMod (p+2))) → F x = 1) →
        (∀ x,x ∉ Set.range (fun j : Fin w => c+(j.val : ZMod (p+2))) → G x = 1) →
        ∀ l d a : ℕ, 0 < l → 3 ≤ a → p+2 = l+u+d+w+a → ∀ r : ℝ, (r : EReal) ≤ B.gap →
          let U := List.ofFn (fun j : Fin u => F (b+(j.val : ZMod (p+2))))
          let W := List.ofFn (fun j : Fin w => G (c+(j.val : ZMod (p+2))))
          let H (i : Fin (p+2)) := F (b+(i.val : ZMod (p+2))-(l : ZMod (p+2))) *
            G (c+(i.val : ZMod (p+2))-((l+u+d : ℕ) : ZMod (p+2)))
          let o := Q.basis Q.vacuum
          let M := slabProduct n β B.top zeroFlux
          ‖rawMarkedMean β zeroFlux H / (sectorWeight β (boxSides R (p+2)) zeroFlux zeroFlux : ℂ) -
            ⟪o,M U o⟫_ℂ * ⟪o,M W o⟫_ℂ‖ ≤
              (U.map fun f => ‖f‖).prod * (W.map fun f => ‖f‖).prod * (2*Real.exp (-r*d)+2*B.thermal a) := by
  obtain ⟨A,Q,hA,hQ⟩ := normalized_split_covariance hβ Γ
  refine ⟨A,Q,hA,?_⟩
  intro p u w F G b c hF hG hf hg l d a hl ha size r hr
  let U := List.ofFn (fun j : Fin u => F (b+(j.val : ZMod (p+2))))
  let W := List.ofFn (fun j : Fin w => G (c+(j.val : ZMod (p+2))))
  let H (i : Fin (p+2)) := F (b+(i.val : ZMod (p+2))-(l : ZMod (p+2))) *
    G (c+(i.val : ZMod (p+2))-((l+u+d : ℕ) : ZMod (p+2)))
  have blind (i) : CentreBlind (H i) := by
    intro e v z g
    simp only [H,ContinuousMap.mul_apply,hF _ e v z g,hG _ e v z g]
  have blank {width : ℕ} (A : ZMod (p+2) → LayerMark (fun _ => Γ.side)) (base : ZMod (p+2))
      (support : ∀ x,x ∉ Set.range (fun j : Fin width => base+(j.val : ZMod (p+2))) → A x = 1)
      (start : ℕ) (pos : 0 < start) (fits : start+width ≤ p+2) :
      A (base+((0 : Fin (p+2)).val : ZMod (p+2))-(start : ZMod (p+2))) = 1 := by
    rw [shifted_word_entry A base support start fits]
    split_ifs with bad
    · exact ((not_le_of_gt pos) bad.1).elim
    · rfl
  have one : H 0 = 1 := by
    change F _ * G _ = 1
    rw [blank F b hf l hl (by omega),blank G c hg (l+u+d) (by omega) (by omega),one_mul]
  have cut (e v z g) : H 0 ((v,rectFlip e z),g) = H 0 ((v,z),g) := by rw [one]; rfl
  have shape := cyclic_two_words F G b c hf hg l d a size
  have h := hQ H blind cut (List.replicate l 1 ++ U) W d a ha shape r hr
  have pad := padded_vacuum_word hβ Γ Q U l 0
  simp only [List.replicate_zero,List.append_nil] at pad
  dsimp only at h
  rw [pad] at h
  simpa only [List.map_append,List.prod_append,List.map_replicate,List.prod_replicate,norm_one,one_pow,one_mul] using h


open scoped InnerProductSpace in
/-- A translated single word has the same vacuum value at every placement.
The finite neutral error is bounded purely by the thermal mass of the far arc. -/
theorem normalized_cyclic_single {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice)
    {A : DiagonalTraces β (cube Γ.side)} (Q : SectorResolution (rectSector (fun _ => Γ.side) β zeroFlux zeroFlux)
      ((rectangularTorusData hβ).choose.spectrum (cube Γ.side)) (fun i => A.value (zeroFlux,i)))
    {p u : ℕ} (F : ZMod (p+2) → LayerMark (fun _ => Γ.side)) (b : ZMod (p+2)) (hF : ∀ x,CentreBlind (F x))
    (hf : ∀ x,x ∉ Set.range (fun j : Fin u => b+(j.val : ZMod (p+2))) → F x = 1)
    (l a : ℕ) (hl : 0 < l) (ha : 3 ≤ a) (size : p+2 = l+u+a) :
    let U := List.ofFn (fun j : Fin u => F (b+(j.val : ZMod (p+2))))
    let H (i : Fin (p+2)) := F (b+(i.val : ZMod (p+2))-(l : ZMod (p+2)))
    let B := (rectangularTorusData hβ).choose.spectrum (cube Γ.side)
    let o := Q.basis Q.vacuum
    ‖rawMarkedMean β zeroFlux H / (sectorWeight β (boxSides (cube Γ.side) (p+2)) zeroFlux zeroFlux : ℂ) -
      ⟪o,slabProduct (fun _ => Γ.side) β B.top zeroFlux U o⟫_ℂ‖ ≤ 2*(U.map fun f => ‖f‖).prod*B.thermal a := by
  let U := List.ofFn (fun j : Fin u => F (b+(j.val : ZMod (p+2))))
  let H (i : Fin (p+2)) := F (b+(i.val : ZMod (p+2))-(l : ZMod (p+2)))
  have one : H 0 = 1 := by
    change F (b+((0 : Fin (p+2)).val : ZMod (p+2))-(l : ZMod (p+2))) = 1
    rw [shifted_word_entry F b hf l (by omega)]
    split_ifs <;> first | rfl | simp_all
  have cut (e v z g) : H 0 ((v,rectFlip e z),g) = H 0 ((v,z),g) := by rw [one]; rfl
  have both := cyclic_two_words (w := 0) F (fun _ => 1) b 0 hf (fun _ _ => rfl) l 0 a (by omega)
  have shape : List.ofFn H = (List.replicate l 1 ++ U) ++ List.replicate a 1 := by
    simpa only [H,U,mul_one,List.replicate_zero,List.ofFn_zero,List.append_nil] using both
  have h := normalized_single_window hβ Γ Q H (fun i => hF _) cut (List.replicate l 1 ++ U) a ha shape
  have pad := padded_vacuum_word hβ Γ Q U l 0
  simp only [List.replicate_zero,List.append_nil] at pad
  dsimp only at h
  rw [pad] at h
  simpa only [List.map_append,List.prod_append,List.map_replicate,List.prod_replicate,norm_one,one_pow,one_mul] using h


/-- The fixed word read from a residue-supported mark. -/
def residueWord {n : spatialAxis → ℕ} {V : ℕ} (F : ZMod V → LayerMark n) (b : ZMod V) (width : ℕ) :=
  List.ofFn (fun j : Fin width => F (b+(j.val : ZMod V)))

open scoped InnerProductSpace in
/-- EV-L for two finite marked polynomials in the normalized neutral trace.
The centers use a single vacuum. The product of the two norm budgets is
independent of the separation and of the location of either word. -/
theorem normalized_word_polynomials {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) :
    let n : spatialAxis → ℕ := fun _ => Γ.side
    let R := cube Γ.side
    let B := (rectangularTorusData hβ).choose.spectrum R
    let S := rectSector n β zeroFlux zeroFlux
    ∃ (A : DiagonalTraces β R) (Q : SectorResolution S B (fun i => A.value (zeroFlux,i))), Wilson.EnumeratesRatios B A.value (zeroFlux,0) ∧
      ∀ {J K : Type} [Fintype J] [Fintype K] {p u w : ℕ} (F : J → ZMod (p+2) → LayerMark n)
        (G : K → ZMod (p+2) → LayerMark n) (b c : ZMod (p+2)) (x : J → ℂ) (y : K → ℂ),
        (∀ j z,CentreBlind (F j z)) → (∀ k z,CentreBlind (G k z)) →
        (∀ j z,z ∉ Set.range (fun i : Fin u => b+(i.val : ZMod (p+2))) → F j z = 1) →
        (∀ k z,z ∉ Set.range (fun i : Fin w => c+(i.val : ZMod (p+2))) → G k z = 1) →
        ∀ l d a : ℕ, 0 < l → 3 ≤ a → p+2 = l+u+d+w+a → ∀ r : ℝ, (r : EReal) ≤ B.gap →
          let M := slabProduct n β B.top zeroFlux
          let o := Q.basis Q.vacuum
          let U j := residueWord (F j) b u
          let W k := residueWord (G k) c w
          let Z := (sectorWeight β (boxSides R (p+2)) zeroFlux zeroFlux : ℂ)
          let H j k (i : Fin (p+2)) := F j (b+(i.val : ZMod (p+2))-(l : ZMod (p+2))) *
            G k (c+(i.val : ZMod (p+2))-((l+u+d : ℕ) : ZMod (p+2)))
          ‖(∑ q : J×K,(x q.1*y q.2)*rawMarkedMean β zeroFlux (H q.1 q.2))/Z -
              (∑ j,x j*⟪o,M (U j) o⟫_ℂ)*(∑ k,y k*⟪o,M (W k) o⟫_ℂ)‖ ≤
            (∑ j,‖x j‖*((U j).map fun f => ‖f‖).prod)*(∑ k,‖y k‖*((W k).map fun f => ‖f‖).prod)*
              (2*Real.exp (-r*d)+2*B.thermal a) := by
  obtain ⟨A,Q,hA,hQ⟩ := normalized_cyclic_words hβ Γ
  refine ⟨A,Q,hA,?_⟩
  intro J K fj fk p u w F G b c x y hF hG hf hg l d a hl ha size r hr
  let Z := (sectorWeight β (boxSides (cube Γ.side) (p+2)) zeroFlux zeroFlux : ℂ)
  let H (j : J) (k : K) (i : Fin (p+2)) := F j (b+(i.val : ZMod (p+2))-(l : ZMod (p+2))) *
    G k (c+(i.val : ZMod (p+2))-((l+u+d : ℕ) : ZMod (p+2)))
  have hh := weighted_window_pair_bound x y (fun j k => rawMarkedMean β zeroFlux (H j k)/Z) _ _ _ _ _
    (fun j k => hQ (F j) (G k) b c (hF j) (hG k) (hf j) (hg k) l d a hl ha size r hr)
  have eqn : (∑ q : J×K,(x q.1*y q.2)*rawMarkedMean β zeroFlux (H q.1 q.2))/Z =
      ∑ q : J×K,(x q.1*y q.2)*(rawMarkedMean β zeroFlux (H q.1 q.2)/Z) := by
    rw [Finset.sum_div]
    apply Finset.sum_congr rfl
    intro q _
    ring
  dsimp only
  rw [eqn]
  exact hh


namespace NeutralResolution

open scoped InnerProductSpace

/-- The finite neutral trace of an arbitrary bounded insertion differs from its
vacuum matrix entry by at most its norm times the excited thermal mass. -/
theorem insertedTrace_tail {β : ℝ} {V : ℕ} {B : BoxSpectrum} (Q : NeutralResolution β V B)
    (X : Q.Γ.SliceL2 μt →L[ℂ] Q.Γ.SliceL2 μt) (a : ℕ) (ha : 3 ≤ a) :
    ∃ err : ℂ, HasSum (fun i => ((Q.eigen i ^ a : ℝ) : ℂ) * ⟪Q.basis i,X (Q.basis i)⟫_ℂ)
      (⟪Q.basis Q.vacuum,X (Q.basis Q.vacuum)⟫_ℂ + err) ∧ ‖err‖ ≤ ‖X‖ * B.thermal a := by
  obtain ⟨t,ht,hle⟩ := Q.thermal a ha
  exact basis_insertedTrace_tail Q.basis Q.vacuum Q.eigen Q.vacuum_one Q.nonneg X a t _ ht hle

theorem normalized_contraction {β : ℝ} {V : ℕ} {B : BoxSpectrum} (Q : NeutralResolution β V B) :
    ‖normalizedNeutral Q.Γ β B.top‖ ≤ 1 := by
  let P := electricProj Q.Γ zeroFlux
  have hs := CStarRing.norm_star_mul_self (x := P)
  have idemp : P * P = P := by simpa [P] using electricProj_mul Q.Γ zeroFlux zeroFlux
  have hstar : star P = P := (electricProj_isSelfAdjoint Q.Γ zeroFlux).star_eq
  rw [hstar,idemp] at hs
  have hp : ‖P‖ ≤ 1 := by nlinarith only [hs,norm_nonneg P]
  rw [normalizedNeutral,norm_smul,Complex.norm_real,Real.norm_eq_abs,abs_of_pos (inv_pos.mpr B.top_pos)]
  calc
    _ ≤ B.top⁻¹ * (‖Q.Γ.transfer μt β‖ * ‖P‖) := mul_le_mul_of_nonneg_left (norm_mul_le _ _) (inv_pos.mpr B.top_pos).le
    _ = ‖P‖ := by rw [← Q.top,← mul_assoc,inv_mul_cancel₀ B.top_pos.ne',one_mul]
    _ ≤ 1 := hp

/-- Two bounded slab operators separated by d steps leave only the opposite
arc's excited mass in the difference between their finite trace and cylinder. -/
theorem twoInsertion_trace {β : ℝ} {V : ℕ} {B : BoxSpectrum} (Q : NeutralResolution β V B)
    (F H : Q.Γ.SliceL2 μt →L[ℂ] Q.Γ.SliceL2 μt) (d a : ℕ) (ha : 3 ≤ a) :
    let X := F * normalizedNeutral Q.Γ β B.top ^ d * H
    ∃ err : ℂ, HasSum (fun i => ((Q.eigen i ^ a : ℝ) : ℂ) * ⟪Q.basis i,X (Q.basis i)⟫_ℂ)
      (⟪Q.basis Q.vacuum,X (Q.basis Q.vacuum)⟫_ℂ + err) ∧ ‖err‖ ≤ ‖F‖ * ‖H‖ * B.thermal a := by
  let R := normalizedNeutral Q.Γ β B.top
  let X := F * R ^ d * H
  obtain ⟨err,he,hb⟩ := Q.insertedTrace_tail X a ha
  haveI : Nontrivial (Q.Γ.SliceL2 μt) := nontrivial_of_ne (Q.basis Q.vacuum) 0 (by
    intro hz
    have hh := Q.basis.orthonormal.norm_eq_one Q.vacuum
    rw [hz,norm_zero] at hh
    exact zero_ne_one hh)
  have hp : ‖R ^ d‖ ≤ 1 := (norm_pow_le R d).trans (pow_le_one₀ (norm_nonneg R) Q.normalized_contraction)
  have hx : ‖X‖ ≤ ‖F‖ * ‖H‖ := by
    apply (norm_mul_le _ _).trans
    apply mul_le_mul_of_nonneg_right _ (norm_nonneg H)
    exact (norm_mul_le _ _).trans ((mul_le_mul_of_nonneg_left hp (norm_nonneg F)).trans_eq (mul_one _))
  exact ⟨err,he,hb.trans (mul_le_mul_of_nonneg_right hx (B.thermal_nonneg a))⟩

end NeutralResolution


open scoped InnerProductSpace in
/-- EV-L input stated without an assumed exponential estimate. It compares the actual
periodic lifted moment to a vacuum-subtracted, neutral cylinder matrix element. The
norm bound and slab width are uniform in separation and volume at this cutoff. -/
def NeutralSlabComparison (L k : ℕ) (β : ℝ) (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ))))
    (T : TorusData) (r : ℝ) : Prop :=
  ∀ Z : PositiveSpan, ∃ A : ℝ, 0 ≤ A ∧ ∃ w : ℕ, ∀ n : ℕ, ∃ D : ℝ, ∀ᶠ v : ℕ in atTop,
    let V := volumeSide L k v
    let B := T.spectrum (cube V)
    let d := 2 * n + 1
    (r : EReal) ≤ B.gap →
    ∃ Q : NeutralResolution β V B, ∃ f g : Q.Γ.SliceL2 TimeAxis.timeIdx,
      ‖f‖ * ‖g‖ ≤ A ∧ ⟪Q.basis Q.vacuum, g⟫_ℂ = 0 ∧
      volumeU ν (liftedWilsonMeasure L v k β) Z ((d : ℝ) * PeriodicLattice.meshSize L (k : ℤ)) ≤
        ‖⟪f, (normalizedNeutral Q.Γ β B.top ^ (d - w)) g⟫_ℂ‖ +
          D * Real.sqrt (1 / (V : ℝ) + B.thermal (V / 2))

theorem slabEstimate_of_neutralComparison {L k : ℕ} {β : ℝ} (hβ : 0 < β)
    {ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ)))} {T : TorusData}
    {r : ℝ} (h : NeutralSlabComparison L k β ν T r) (hr : 0 < r) : SlabEstimate L k β ν T r := by
  intro Z
  obtain ⟨A, hA, w, hw⟩ := h Z
  refine ⟨A * Real.exp (r * w), fun n => ?_⟩
  obtain ⟨D, hD⟩ := hw n
  refine ⟨D, ?_⟩
  filter_upwards [hD] with v hv
  dsimp only
  intro hgap
  obtain ⟨Q, f, g, hnorm, hg, hvol⟩ := hv hgap
  let d := 2 * n + 1
  have hd : (d : ℝ) = 2 * (n : ℝ) + 1 := by norm_num [d]
  have he : (d : ℝ) - w ≤ ((d - w : ℕ) : ℝ) := by
    by_cases h' : w ≤ d
    · rw [Nat.cast_sub h']
    · rw [Nat.sub_eq_zero_of_le (by omega : d ≤ w), Nat.cast_zero]
      exact sub_nonpos.mpr (by exact_mod_cast (show d ≤ w by omega))
  have hdec := neutralMatrixElement_le Q.Γ hβ Q.A _ Q.enumerates Q.basis Q.vacuum Q.eigen
    Q.acts Q.nonneg Q.slots hgap f g hg (d - w)
  have hexp : Real.exp (-r * ((d - w : ℕ) : ℝ)) ≤ Real.exp (r * w) * Real.exp (-r * (2 * (n : ℝ) + 1)) := by
    rw [← Real.exp_add, ← hd]
    apply Real.exp_le_exp.mpr
    nlinarith only [mul_le_mul_of_nonneg_left he hr.le]
  rw [← hd]
  refine hvol.trans (add_le_add ?_ le_rfl)
  refine hdec.trans ?_
  rw [hd, mul_assoc A]
  exact mul_le_mul hnorm hexp (Real.exp_pos _).le hA


theorem cutoff_bound_of_finiteTori {L k ℓ N : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L)
    (hℓ : 0 < ℓ) (hN : 3 ≤ N) (hside : 2 * N = ℓ * L ^ k) {β : ℝ} (hβ : 0 < β)
    {ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (T : TorusData) (hs : T.seed N < 1 / (2 : ℝ) ^ 18)
    (hslab : SlabEstimate L k β ν T (gapRate ℓ * PeriodicLattice.meshSize L (k : ℤ)))
    (Z : PositiveSpan) :
    ∃ C : ℝ, ∀ n : ℕ, let t := (2 * (n : ℝ) + 1) * PeriodicLattice.meshSize L (k : ℤ)
      latticeU ν Z t ≤ C * Real.exp (-gapRate ℓ * t) := by
  have hL' : 1 < L := by have := hL.2; omega
  let a := PeriodicLattice.meshSize L (k : ℤ)
  let r := gapRate ℓ * a
  have hr : r = Real.log ((2 : ℝ) ^ 18 / 5041) / N :=
    physicalRate_eq (by omega) hℓ hside
  have hV := volumeSide_tendsto hL' k
  have hg : ∀ᶠ v in atTop, (r : EReal) ≤ (T.spectrum (cube (volumeSide L k v))).gap := by
    filter_upwards [hV (eventually_ge_atTop (2 * N))] with v hv
    rw [hr]
    exact (seedRate_lower T hs).trans (T.corollaryS3' hN (hs.trans (by norm_num)) hv)
  have hinv := (tendsto_const_div_atTop_nhds_zero_nat (1 : ℝ)).comp hV
  have hhalf := (halfSide_thermal_tendsto T hN hs).comp hV
  obtain ⟨φ, hφ, hlim⟩ := volumeU_tendsto hL hβ hν
  obtain ⟨C, hC⟩ := hslab Z
  refine ⟨C, fun n => ?_⟩
  let d := 2 * (n : ℝ) + 1
  obtain ⟨D, hD⟩ := hC n
  have herr := ((Real.continuous_sqrt.tendsto _).comp (hinv.add hhalf)).const_mul D
  have hbound := (hD.and hg).mono fun v h => h.1 h.2
  have he := le_of_tendsto_of_tendsto (hlim Z (d * a))
    ((herr.const_add (C * Real.exp (-r * d))).comp hφ.tendsto_atTop)
    (hφ.tendsto_atTop hbound)
  simpa only [zero_add, Real.sqrt_zero, mul_zero, add_zero, r, neg_mul, mul_right_comm,
    mul_assoc, mul_comm a d] using he

/-- Specialize the signed torus data to the exact side and half-time of one
good cutoff. The Stage 0 seed quantifies over every release presentation of that cube. -/
theorem seed_at_calibrated_cutoff {L ℓ : ℕ} (k : ℕ+) {β : ℝ} (hL : Conventions.IsAdmissibleBlockingFactor L)
    (hℓ : 0 < ℓ) (hfour : 4 ∣ ℓ) (T : TorusData) (hT : RealizesKappa β T)
    (hseed : ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ (k : ℕ) → KappaSeedOnCube Γ β) :
    ∃ N : ℕ, 3 ≤ N ∧ 2 * N = ℓ * L ^ (k : ℕ) ∧ T.seed N < 1 / (2 : ℝ) ^ 18 := by
  let n := ℓ * L ^ (k : ℕ)
  let N := n / 2
  have hL' := hL.2
  have hn : 13 ≤ n := calc
    13 ≤ L := hL'
    _ = L ^ 1 := (pow_one _).symm
    _ ≤ L ^ (k : ℕ) := Nat.pow_le_pow_right (by omega) k.pos
    _ ≤ n := Nat.le_mul_of_pos_left _ hℓ
  have hd : 2 ∣ n := dvd_trans (by decide : 2 ∣ 4) (dvd_mul_of_dvd_left hfour _)
  have hside : 2 * N = n := Nat.mul_div_cancel' hd
  have hN : 3 ≤ N := by omega
  obtain ⟨Λ,hΛ⟩ := (GibbsHaarKernels.cubicPeriodSublatticeIffThreeLe_holds n (by omega)).mpr (by omega)
  let Γ : CubicPeriodSublattice := ⟨n,by omega,Λ,hΛ⟩
  refine ⟨N,hN,hside,?_⟩
  rw [seed_eq_thermal β T hT Γ hN hside]
  exact (hseed Γ rfl).2

/-- Unconditional W2--W6 conclusion at the frequently seeded, calibrated
cutoffs. It controls every larger integer cube and the actual half-time tails. -/
theorem calibratedSpectralPropagation {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K}
    {S : CumulantFamily} (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K) :
    0 < gapRate ℓ ∧ ∃ᶠ j in atTop,
      let T := (rectangularTorusData (h.beta_pos j)).choose
      (∀ V ≥ ℓ * L ^ (K j : ℕ),
        ((gapRate ℓ * PeriodicLattice.meshSize L ((K j : ℕ) : ℤ) : ℝ) : EReal) ≤ (T.spectrum (cube V)).gap) ∧
        Tendsto (fun V : ℕ => (T.spectrum (cube V)).thermal (V/2)) atTop (𝓝 0) := by
  refine ⟨gapRate_pos hs.1,hs.2.2.mono fun j hj => ?_⟩
  let T := (rectangularTorusData (h.beta_pos j)).choose
  obtain ⟨N,hN,he,hseed⟩ := seed_at_calibrated_cutoff (K j) hL hs.1 hs.2.1 T
    (rectangularTorusData (h.beta_pos j)).choose_spec.1 hj
  refine ⟨fun V hV => ?_,halfSide_thermal_tendsto T hN hseed⟩
  have hL' := hL.2
  rw [physicalRate_eq (by omega) hs.1 he]
  exact (seedRate_lower T hseed).trans (T.corollaryS3' hN (hseed.trans (by norm_num)) (he ▸ hV))


theorem expClusters_of_finiteTori {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K}
    {S : CumulantFamily} (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K)
    (hfinite : ∀ j, ∃ T : TorusData, RealizesKappa (betaAt L M (K j) g₀) T ∧
      ∀ r : ℝ, 0 < r → SlabEstimate L (K j) (betaAt L M (K j) g₀) (ν j) T r) :
    ExpClusters L K ν (gapRate ℓ) := by
  intro Z
  refine hs.2.2.mono fun j hj => ?_
  let k : ℕ := K j
  have hL' := hL.2
  obtain ⟨T,hT,hslab⟩ := hfinite j
  obtain ⟨N,hN,hside,ht⟩ := seed_at_calibrated_cutoff (K j) hL hs.1 hs.2.1 T hT hj
  have ha : 0 < PeriodicLattice.meshSize L (k : ℤ) :=
    zpow_pos (by exact_mod_cast (show 0 < L by omega)) _
  exact cutoff_bound_of_finiteTori hL hs.1 hN hside (h.beta_pos j) (h.isLimit j)
    T ht (hslab _ (mul_pos (gapRate_pos hs.1) ha)) Z

/-- After supplying the two finite-volume inputs, the result has Stage 0’s exact type. -/
theorem expClusters_of_kappaSeed_of_finiteTori (supply : ∀ (L k : ℕ) (β : ℝ) (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ)))),
    Conventions.IsAdmissibleBlockingFactor L → 0 < β → IsInfiniteVolumeLimit L k β ν →
    ∃ T : TorusData, RealizesKappa β T ∧ ∀ r : ℝ, 0 < r → SlabEstimate L k β ν T r) :
    type_of% @GapChain.expClusters_of_kappaSeed :=
  fun {_ _ _ K ν _} hL h {_} hs => expClusters_of_finiteTori hL h hs
    (fun j => supply _ (K j) _ (ν j) hL (h.beta_pos j) (h.isLimit j))


/-- The finite supplier can instead give the EV-L comparison to actual neutral
cylinder insertions. The exponential and the passage to the exported state follow in Lean. -/
theorem expClusters_of_kappaSeed_of_neutralComparison (supply : ∀ (L k : ℕ) (β : ℝ)
    (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ)))),
    Conventions.IsAdmissibleBlockingFactor L → 0 < β → IsInfiniteVolumeLimit L k β ν →
    ∃ T : TorusData, RealizesKappa β T ∧ ∀ r : ℝ, 0 < r → NeutralSlabComparison L k β ν T r) :
    type_of% @GapChain.expClusters_of_kappaSeed := by
  apply expClusters_of_kappaSeed_of_finiteTori
  intro L k β ν hL hβ hν
  obtain ⟨T, hT, hC⟩ := supply L k β ν hL hβ hν
  exact ⟨T, hT, fun r hr => slabEstimate_of_neutralComparison hβ (hC r hr) hr⟩

/-- The good calibrated cutoffs suffice. EV-L may use the W5 gap at each
volume and choose its uniform prefactor after fixing the positive rate. -/
theorem expClusters_of_seeded_windows {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K}
    {S : CumulantFamily} (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K)
    (supply : ∀ j, (∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ (K j : ℕ) →
        KappaSeedOnCube Γ (betaAt L M (K j) g₀)) →
      NeutralSlabComparison L (K j) (betaAt L M (K j) g₀) (ν j) (rectangularTorusData (h.beta_pos j)).choose
        (gapRate ℓ * PeriodicLattice.meshSize L ((K j : ℕ) : ℤ))) :
    ExpClusters L K ν (gapRate ℓ) := by
  intro Z
  refine hs.2.2.mono fun j hj => ?_
  let T := (rectangularTorusData (h.beta_pos j)).choose
  obtain ⟨N,hN,hside,ht⟩ := seed_at_calibrated_cutoff (K j) hL hs.1 hs.2.1 T
    (rectangularTorusData (h.beta_pos j)).choose_spec.1 hj
  have hL' := hL.2
  have ha : 0 < PeriodicLattice.meshSize L ((K j : ℕ) : ℤ) :=
    zpow_pos (by exact_mod_cast (show 0 < L by omega)) _
  exact cutoff_bound_of_finiteTori hL hs.1 hN hside (h.beta_pos j) (h.isLimit j) T ht
    (slabEstimate_of_neutralComparison (h.beta_pos j) (supply j hj) (mul_pos (gapRate_pos hs.1) ha)) Z

/-- It suffices to establish EV-L for individual pairs of real physical
monomials on the seeded cutoffs. Their complex span and weak limit are automatic. -/
theorem expClusters_of_seeded_pairWindows {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K}
    {S : CumulantFamily} (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K)
    (supply : ∀ j, (∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ (K j : ℕ) →
        KappaSeedOnCube Γ (betaAt L M (K j) g₀)) →
      PairWindowEstimate L (K j) (betaAt L M (K j) g₀) (ν j) (rectangularTorusData (h.beta_pos j)).choose
        (gapRate ℓ * PeriodicLattice.meshSize L ((K j : ℕ) : ℤ))) :
    ExpClusters L K ν (gapRate ℓ) := by
  intro Z
  refine hs.2.2.mono fun j hj => ?_
  let T := (rectangularTorusData (h.beta_pos j)).choose
  obtain ⟨N,hN,hside,ht⟩ := seed_at_calibrated_cutoff (K j) hL hs.1 hs.2.1 T
    (rectangularTorusData (h.beta_pos j)).choose_spec.1 hj
  exact cutoff_bound_of_finiteTori hL hs.1 hN hside (h.beta_pos j) (h.isLimit j) T ht
    (slabEstimate_of_pairWindows hL (K j) (h.beta_pos j) (h.isLimit j) T _ (supply j hj)) Z

theorem expClusters_of_kappaSeed_of_pairWindows (supply : ∀ {L : ℕ} (k : ℕ+) {β : ℝ}
    (ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))),
    Conventions.IsAdmissibleBlockingFactor L → ∀ hβ : 0 < β, IsInfiniteVolumeLimit L k β ν →
    ∀ r : ℝ, 0 < r → PairWindowEstimate L k β ν (rectangularTorusData hβ).choose r) :
    type_of% @GapChain.expClusters_of_kappaSeed := by
  intro L M g₀ K ν S hL h ℓ hs
  apply expClusters_of_seeded_pairWindows hL h hs
  intro j _
  have hL' := hL.2
  have ha : 0 < PeriodicLattice.meshSize L ((K j : ℕ) : ℤ) := zpow_pos (by exact_mod_cast (show 0 < L by omega)) _
  exact supply (K j) (ν j) hL (h.beta_pos j) (h.isLimit j) _ (mul_pos (gapRate_pos hs.1) ha)

/-- Stage 0's exact statement after the centered finite-volume comparison.
The rate is in lattice units at this cutoff; W5 supplies its gap hypothesis. -/
theorem expClusters_of_kappaSeed_of_slabComparison (supply : ∀ (L k : ℕ) (β : ℝ)
    (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ)))),
    Conventions.IsAdmissibleBlockingFactor L → ∀ hβ : 0 < β, IsInfiniteVolumeLimit L k β ν →
    ∀ r : ℝ, 0 < r → NeutralSlabComparison L k β ν (rectangularTorusData hβ).choose r) :
    type_of% @GapChain.expClusters_of_kappaSeed := by
  apply expClusters_of_kappaSeed_of_neutralComparison
  intro L k β ν hL hβ hν
  exact ⟨(rectangularTorusData hβ).choose,(rectangularTorusData hβ).choose_spec.1,supply L k β ν hL hβ hν⟩

end FiniteVolumes

end GapChain.Stage3

#print axioms GapChain.Stage3.planeOf_swap
#print axioms GapChain.Stage3.mapPlane_planeOf
#print axioms GapChain.Stage3.mapPlane_mul
#print axioms GapChain.Stage3.mapPlane_one
#print axioms GapChain.Stage3.faceAction_swap
#print axioms GapChain.Stage3.faceAction_planeOf
#print axioms GapChain.Stage3.faceAction_relabel
#print axioms GapChain.Stage3.twistedPartition_permute
#print axioms GapChain.Stage3.pfaffianSign_swap
#print axioms GapChain.Stage3.pfaffianSign_permute
#print axioms GapChain.Stage3.kappaWeight_permute
#print axioms GapChain.Stage3.pfaffianSign_join
#print axioms GapChain.Stage3.character_orthogonal
#print axioms GapChain.Stage3.kappaWeight_eq_diagonal
#print axioms GapChain.Stage3.twistedPartition_pos
#print axioms GapChain.Stage3.character_symm
#print axioms GapChain.Stage3.character_le_one
#print axioms GapChain.Stage3.join_zero
#print axioms GapChain.Stage3.character_zero
#print axioms GapChain.Stage3.sectorWeight_le_neutral
#print axioms GapChain.Stage3.twistedPartition_eq_sectorSum
#print axioms GapChain.Stage3.electric_untwist
#print axioms GapChain.Stage3.eraseIncident_map
#print axioms GapChain.Stage3.eraseIncident_time
#print axioms GapChain.Stage3.untwist_axis
#print axioms GapChain.Stage3.all_twists_le_periodic
#print axioms GapChain.Stage3.partition_div_eight_le_neutral
#print axioms GapChain.Stage3.sectorWeight_le_eight_neutral
#print axioms GapChain.Stage3.partition_div_eight_le_kappa
#print axioms GapChain.Stage3.twistedMeasure_probability
#print axioms GapChain.Stage3.periodic_mean_sq_le
#print axioms GapChain.Stage3.mixtureMean_sum
#print axioms GapChain.Stage3.mixture_window_comparison
#print axioms GapChain.Stage3.periodic_window_comparison
#print axioms GapChain.Stage3.summable_time_decay
#print axioms GapChain.Stage3.linkCentre_comm
#print axioms GapChain.Stage3.linkCentre_xor
#print axioms GapChain.Stage3.linkCentre_inv
#print axioms GapChain.Stage3.bitSign_xor
#print axioms GapChain.Stage3.halfTrace_linkCentre
#print axioms GapChain.Stage3.resign_preserving
#print axioms GapChain.Stage3.linkCentre_mul_apply
#print axioms GapChain.Stage3.linkCentre_inv_apply
#print axioms GapChain.Stage3.transport_resign
#print axioms GapChain.Stage3.signedIntegral_resign
#print axioms GapChain.Stage3.signedIntegral_stackBits
#print axioms GapChain.Stage3.oneStack_swap
#print axioms GapChain.Stage3.interval_curl
#print axioms GapChain.Stage3.stripLinks_curl
#print axioms GapChain.Stage3.signedIntegral_moveStack
#print axioms GapChain.Stage3.oneStack_plane
#print axioms GapChain.Stage3.locatedStacks_partition
#print axioms GapChain.Stage3.slabFields_preserving
#print axioms GapChain.Stage3.transport_slabField
#print axioms GapChain.Stage3.signedDensity_eq_slabs
#print axioms GapChain.Stage3.signedIntegral_eq_slabKernels
#print axioms GapChain.Stage3.twistedPartition_eq_slabKernels
#print axioms GapChain.Stage3.slabDensity_off_electric_cut
#print axioms GapChain.Stage3.slabDensity_adjacent
#print axioms GapChain.Stage3.spatialLevels_preserving
#print axioms GapChain.Stage3.twistedPartition_eq_kernelCycle
#print axioms GapChain.Stage3.slabField_flipSlice
#print axioms GapChain.Stage3.seamLinks_curl
#print axioms GapChain.Stage3.layerKernel_electric
#print axioms GapChain.Stage3.finRotate_ne_self_of_two
#print axioms GapChain.Stage3.twistedPartition_eq_electricCycle
#print axioms GapChain.Stage3.mem_cuts
#print axioms GapChain.Stage3.fluxBit_add
#print axioms GapChain.Stage3.character_add
#print axioms GapChain.Stage3.character_sq
#print axioms GapChain.Stage3.centreElt_mul_self
#print axioms GapChain.Stage3.translation_characterProj
#print axioms GapChain.Stage3.characterProj_mul
#print axioms GapChain.Stage3.centreShift_add
#print axioms GapChain.Stage3.electricTranslation_mul
#print axioms GapChain.Stage3.translation_electricProj
#print axioms GapChain.Stage3.electricProj_mul
#print axioms GapChain.Stage3.electricTranslation_zero
#print axioms GapChain.Stage3.electricTranslation_isSelfAdjoint
#print axioms GapChain.Stage3.electricProj_isSelfAdjoint
#print axioms GapChain.Stage3.electricProj_sum
#print axioms GapChain.Stage3.electricProj_zero
#print axioms GapChain.Stage3.continuous_magneticHolonomy
#print axioms GapChain.Stage3.magneticEnergy_nonneg
#print axioms GapChain.Stage3.continuous_magneticEnergy
#print axioms GapChain.Stage3.magneticEnergy_zero
#print axioms GapChain.Stage3.magneticDensity_continuous
#print axioms GapChain.Stage3.magneticDensity_bound
#print axioms GapChain.Stage3.magneticMultiplier_formula
#print axioms GapChain.Stage3.magneticMultiplier_positive
#print axioms GapChain.Stage3.magneticTransfer_zero
#print axioms GapChain.Stage3.magneticTransfer_positive
#print axioms GapChain.Stage3.magneticTransfer_traceClass
#print axioms GapChain.Stage3.centreSign_comm
#print axioms GapChain.Stage3.centreSign_linkClass
#print axioms GapChain.Stage3.centreSign_ofAxis
#print axioms GapChain.Stage3.centreSign_shift_transverse
#print axioms GapChain.Stage3.holonomy_centreShift
#print axioms GapChain.Stage3.magneticEnergy_centreShift
#print axioms GapChain.Stage3.commutes_magneticMultiplier
#print axioms GapChain.Stage3.centreShift_gauge
#print axioms GapChain.Stage3.commutes_gaugeProjection
#print axioms GapChain.Stage3.commutes_sqrtLink
#print axioms GapChain.Stage3.magneticTransfer_commutes
#print axioms GapChain.Stage3.magneticTransfer_commutes_proj
#print axioms GapChain.Stage3.magneticMultiplier_half_sq
#print axioms GapChain.Stage3.layerFactor_products
#print axioms GapChain.Stage3.symmetricMagnetic_norm
#print axioms GapChain.Stage3.symmetricMagnetic_zero_norm
#print axioms GapChain.Stage3.magneticEnergy_gaugeAct
#print axioms GapChain.Stage3.magneticMultiplier_commutes_gaugeProjection
#print axioms GapChain.Stage3.halfTransfer_squared
#print axioms GapChain.Stage3.symmetricMagnetic_kinetic
#print axioms GapChain.Stage3.product_eigenspaces
#print axioms GapChain.Stage3.symmetricMagnetic_sector_eigenspaces
#print axioms GapChain.Stage3.level_siteOfCode
#print axioms GapChain.Stage3.spatialCode_siteOfCode
#print axioms GapChain.Stage3.slicePeriods_of_spatialCode
#print axioms GapChain.Stage3.spatialCode_of_translate
#print axioms GapChain.Stage3.releaseLinkLabel_class
#print axioms GapChain.Stage3.sliceLink_ofAxis_axis
#print axioms GapChain.Stage3.linkClass_eq_of_code
#print axioms GapChain.Stage3.releaseLayer_preserving
#print axioms GapChain.Stage3.releaseLayer_flip
#print axioms GapChain.Stage3.twistedPartition_eq_releasedCycle
#print axioms GapChain.Stage3.rectVertices_spaceStep
#print axioms GapChain.Stage3.rectVertices_timeStep
#print axioms GapChain.Stage3.magnetic_temporal_bit
#print axioms GapChain.Stage3.layerKernel_eq_rectKernel
#print axioms GapChain.Stage3.twistedPartition_eq_rectCycle
#print axioms GapChain.Stage3.rectKernel_factorization
#print axioms GapChain.Stage3.continuous_rectSpatialAction
#print axioms GapChain.Stage3.rectGauge_mul
#print axioms GapChain.Stage3.rectTemporal_gauge
#print axioms GapChain.Stage3.rectSymKernel_apply
#print axioms GapChain.Stage3.rectKernel_eq_sym
#print axioms GapChain.Stage3.rectTemporal_gram
#print axioms GapChain.Stage3.rectSymOperator_positive
#print axioms GapChain.Stage3.rectSpatialAction_flip
#print axioms GapChain.Stage3.rectGauge_flip
#print axioms GapChain.Stage3.rectTemporal_flip
#print axioms GapChain.Stage3.rectHalfWeight_flip
#print axioms GapChain.Stage3.rectSymKernel_flip
#print axioms GapChain.Stage3.twistedPartition_eq_symCycle
#print axioms GapChain.Stage3.continuous_rectKernel
#print axioms GapChain.Stage3.rectFlip_zero
#print axioms GapChain.Stage3.rectSeamKernel_memLp
#print axioms GapChain.Stage3.rectFlip_preserving
#print axioms GapChain.Stage3.rectFlip_involution
#print axioms GapChain.Stage3.rectFlip_add
#print axioms GapChain.Stage3.rectTranslation_mul
#print axioms GapChain.Stage3.rectTranslation_zero
#print axioms GapChain.Stage3.rectTranslation_selfAdjoint
#print axioms GapChain.Stage3.rectProj_idempotent
#print axioms GapChain.Stage3.rectProj_selfAdjoint
#print axioms GapChain.Stage3.rectRight_insert
#print axioms GapChain.Stage3.rectLeft_insert
#print axioms GapChain.Stage3.rectSymEntry_memLp
#print axioms GapChain.Stage3.rectSymSeam_memLp
#print axioms GapChain.Stage3.rectSymOperator_eq
#print axioms GapChain.Stage3.rectSymOperator_commutes
#print axioms GapChain.Stage3.rectSymOperator_commutes_proj
#print axioms GapChain.Stage3.rectSector_positive
#print axioms GapChain.Stage3.kernel_norm_domination
#print axioms GapChain.Stage3.rectTestEntry_continuous
#print axioms GapChain.Stage3.rectTestEntry_bound
#print axioms GapChain.Stage3.rectTestEntry_memLp
#print axioms GapChain.Stage3.rectTestOperator_bound
#print axioms GapChain.Stage3.rectOperator_insert
#print axioms GapChain.Stage3.integral_seamZero
#print axioms GapChain.Stage3.rectInsertedTrace
#print axioms GapChain.Stage3.rectElectricEntry_operator
#print axioms GapChain.Stage3.rectElectricEntry_product
#print axioms GapChain.Stage3.rectSymLoop_partition
#print axioms GapChain.Stage3.rectSymTrace
#print axioms GapChain.Stage3.rectSectorTrace
#print axioms GapChain.Stage3.rectSector_compact
#print axioms GapChain.Stage3.rectSector_moments
#print axioms GapChain.Stage3.sectorWeight_nonneg
#print axioms GapChain.Stage3.zmod_val_rotate
#print axioms GapChain.Stage3.spatialCode_shift
#print axioms GapChain.Stage3.vertexFromCode_class
#print axioms GapChain.Stage3.linkFromCode_class
#print axioms GapChain.Stage3.releaseFaceLabel_class
#print axioms GapChain.Stage3.faceClass_eq_of_code
#print axioms GapChain.Stage3.readLinks_holonomy
#print axioms GapChain.Stage3.codeResidue_zero
#print axioms GapChain.Stage3.magneticFace_readCode
#print axioms GapChain.Stage3.halfTrace_magneticHolonomy
#print axioms GapChain.Stage3.rectFaceTerm_readCode
#print axioms GapChain.Stage3.magneticEnergy_readLinks
#print axioms GapChain.Stage3.linkCoordinates_apply
#print axioms GapChain.Stage3.gaugeCoordinates_apply
#print axioms GapChain.Stage3.linkCoordinates_preserving
#print axioms GapChain.Stage3.gaugeCoordinates_preserving
#print axioms GapChain.Stage3.readLinks_gaugeAct
#print axioms GapChain.Stage3.readLinks_electric
#print axioms GapChain.Stage3.singleBondWeight_real
#print axioms GapChain.Stage3.rectTemporal_readLinks
#print axioms GapChain.Stage3.rectHalfWeight_readLinks
#print axioms GapChain.Stage3.rectSymKernel_release
#print axioms GapChain.Stage3.integral_row_gaugeProjection
#print axioms GapChain.Stage3.symmetricMagnetic_hasKernel
#print axioms GapChain.Stage3.cubeIsometry_surjective
#print axioms GapChain.Stage3.cubeIsometry_intertwines
#print axioms GapChain.Stage3.rectSymOperator_cube_norm
#print axioms GapChain.Stage3.cubeIsometry_electric
#print axioms GapChain.Stage3.cubeIsometry_proj
#print axioms GapChain.Stage3.cube_sector_eigenspaces
#print axioms GapChain.Stage3.releaseSector_spectral
#print axioms GapChain.Stage3.edgeMemLp
#print axioms GapChain.Stage3.edgeOperator_compose
#print axioms GapChain.Stage3.edgeLoop_cons
#print axioms GapChain.Stage3.integral_edgeLoop
#print axioms GapChain.Stage3.hasSum_edgeLoop
#print axioms GapChain.Stage3.hasSum_markedCycle
#print axioms GapChain.Stage3.fieldOfPairs_spatial
#print axioms GapChain.Stage3.fieldOfPairs_temporal
#print axioms GapChain.Stage3.releasePairWeight_boltzmann
#print axioms GapChain.Stage3.liftedGibbs_integral_pairs
#print axioms GapChain.Stage3.markedPair_integral
#print axioms GapChain.Stage3.readLinks_continuous
#print axioms GapChain.Stage3.readVertices_continuous
#print axioms GapChain.Stage3.periodicHalfWeight_sq
#print axioms GapChain.Stage3.integral_markedPairs
#print axioms GapChain.Stage3.rectTestEntry_flip
#print axioms GapChain.Stage3.rectTestOperator_commutes
#print axioms GapChain.Stage3.writeLinks_readLinks
#print axioms GapChain.Stage3.readLinks_writeLinks
#print axioms GapChain.Stage3.writeLinks_flip
#print axioms GapChain.Stage3.spatialFaceMark_blind
#print axioms GapChain.Stage3.temporalFaceMark_blind
#print axioms GapChain.Stage3.faceEnergy_halfTrace
#print axioms GapChain.Stage3.spatialFaceMark_read
#print axioms GapChain.Stage3.temporalFaceMark_read
#print axioms GapChain.Stage3.face_as_layer_plaquette
#print axioms GapChain.Stage3.face_at_base_level
#print axioms GapChain.Stage3.wilsonFace_norm
#print axioms GapChain.Stage3.spatialFaceMark_norm
#print axioms GapChain.Stage3.temporalFaceMark_norm
#print axioms GapChain.Stage3.translate_temporalPlaquette
#print axioms GapChain.Stage3.translate_spatialPlaquette
#print axioms GapChain.Stage3.faceEnergy_translated_layerMark
#print axioms GapChain.Stage3.translatedUnitTest_center
#print axioms GapChain.Stage3.translated_smearedEnergy_layerMarks
#print axioms GapChain.Stage3.faceEnergy_layerMark
#print axioms GapChain.Stage3.smearedEnergy_layerMarks
#print axioms GapChain.Stage3.cubeTimeIndex
#print axioms GapChain.Stage3.finite_time_word
#print axioms GapChain.Stage3.word_residue_support
#print axioms GapChain.Stage3.residue_word_product
#print axioms GapChain.Stage3.anchoredCubeTimeIndex
#print axioms GapChain.Stage3.residue_cycle
#print axioms GapChain.Stage3.physical_marked_trace
#print axioms GapChain.Stage3.combineTests_blind
#print axioms GapChain.Stage3.combineTests_off
#print axioms GapChain.Stage3.combineTests_values
#print axioms GapChain.Stage3.combineTests_product
#print axioms GapChain.Stage3.combineTests_norm
#print axioms GapChain.Stage3.translated_centeredProduct_layerExpansion
#print axioms GapChain.Stage3.centeredProduct_layerExpansion
#print axioms GapChain.Stage3.jointDensity_pos
#print axioms GapChain.Stage3.continuous_jointDensity
#print axioms GapChain.Stage3.joint_markedCycle
#print axioms GapChain.Stage3.rectTestEntry_one
#print axioms GapChain.Stage3.joint_partition
#print axioms GapChain.Stage3.flipLayerMap_zero
#print axioms GapChain.Stage3.edgeOperator_flip
#print axioms GapChain.Stage3.closing_mark_trace
#print axioms GapChain.Stage3.averaged_mark_trace
#print axioms GapChain.Stage3.closing_partition
#print axioms GapChain.Stage3.jointState_probability
#print axioms GapChain.Stage3.jointState_integral
#print axioms GapChain.Stage3.physicalJointCoordinates_apply
#print axioms GapChain.Stage3.physicalJointCoordinates_preserving
#print axioms GapChain.Stage3.physicalJointCoordinates_density
#print axioms GapChain.Stage3.physical_shifted_jointMark
#print axioms GapChain.Stage3.physicalJoint_partition
#print axioms GapChain.Stage3.physicalJoint_expectation
#print axioms GapChain.Stage3.jointPeriodic_mean_sq
#print axioms GapChain.Stage3.jointNeutralMean_weight
#print axioms GapChain.Stage3.relabelJoint_apply
#print axioms GapChain.Stage3.relabelJoint_preserving
#print axioms GapChain.Stage3.periodicDensity_relabel
#print axioms GapChain.Stage3.jointPeriodic_shift_mean
#print axioms GapChain.Stage3.joint_window_comparison
#print axioms GapChain.Stage3.jointNeutralMean_centered_product
#print axioms GapChain.Stage3.joint_covariance_envelope
#print axioms GapChain.Stage3.translated_residue_rotation
#print axioms GapChain.Stage3.time_average_placement
#print axioms GapChain.Stage3.weighted_window_bound
#print axioms GapChain.Stage3.weighted_window_pair_bound
#print axioms GapChain.Stage3.real_vacuum_errors
#print axioms GapChain.Stage3.periodic_covariance_of_three_means
#print axioms GapChain.Stage3.periodic_rotates_error
#print axioms GapChain.Stage3.jointNeutralMean_le_bound
#print axioms GapChain.Stage3.periodic_polynomial_comparison
#print axioms GapChain.Stage3.layerOperator_one
#print axioms GapChain.Stage3.layerOperator_commutes
#print axioms GapChain.Stage3.projectedLayer_one
#print axioms GapChain.Stage3.rectProj_norm_le
#print axioms GapChain.Stage3.projectedLayer_bound
#print axioms GapChain.Stage3.slabProduct_bound
#print axioms GapChain.Stage3.slabProduct_factor
#print axioms GapChain.Stage3.ofFn_empty_arc
#print axioms GapChain.Stage3.ofFn_split_windows
#print axioms GapChain.Stage3.shifted_word_entry
#print axioms GapChain.Stage3.ofFn_word_segment
#print axioms GapChain.Stage3.cyclic_two_words
#print axioms GapChain.Stage3.jointNeutralMean_of_marks
#print axioms GapChain.Stage3.jointMark_relabel
#print axioms GapChain.Stage3.jointMark_mul
#print axioms GapChain.Stage3.jointNeutral_rotated_product
#print axioms GapChain.Stage3.continuous_jointMark
#print axioms GapChain.Stage3.jointNeutral_polynomial
#print axioms GapChain.Stage3.rotated_polynomial_words
#print axioms GapChain.Stage3.normalized_mark_trace
#print axioms GapChain.Stage3.rectShape_boxSides
#print axioms GapChain.Stage3.boxSector_moments
#print axioms GapChain.Stage3.boxSector_labeledList
#print axioms GapChain.Stage3.boxSector_list
#print axioms GapChain.Stage3.boxNeutral_norm_pos
#print axioms GapChain.Stage3.boxNeutral_norm
#print axioms GapChain.Stage3.cubicTraceIdentity_iff_kernelCycle
#print axioms GapChain.Stage3.projectedTrace_of_insertions
#print axioms GapChain.Stage3.sectorWeight_nonneg_of_insertions
#print axioms GapChain.Stage3.kappaWeight_cross
#print axioms GapChain.Stage3.diagonal_values_le_periodic_top
#print axioms GapChain.Stage3.rectangularDiagonalTraces
#print axioms GapChain.Stage3.DiagonalTraces.hasSum_weight
#print axioms GapChain.Stage3.DiagonalTraces.boxSpectrum
#print axioms GapChain.Stage3.DiagonalTraces.weight_logConvex
#print axioms GapChain.Stage3.DiagonalTraces.neutralTail_le
#print axioms GapChain.Stage3.DiagonalTraces.gap_le_neutralSlot
#print axioms GapChain.Stage3.vacuumComplement_power_le
#print axioms GapChain.Stage3.normalizedNeutral_symmetric
#print axioms GapChain.Stage3.neutralMatrixElement_le
#print axioms GapChain.Stage3.periodic_boxSides
#print axioms GapChain.Stage3.torusData_of_diagonalTraces
#print axioms GapChain.Stage3.torusData_of_cubicNorm
#print axioms GapChain.Stage3.boxShape_cube
#print axioms GapChain.Stage3.calibrated_cubicNorm
#print axioms GapChain.Stage3.rectangularTorusData
#print axioms GapChain.Stage3.seed_eq_thermal
#print axioms GapChain.Stage3.seedRate_lower
#print axioms GapChain.Stage3.halfSide_thermal_tendsto
#print axioms GapChain.Stage3.physicalRate_eq
#print axioms GapChain.Stage3.volumeU_self
#print axioms GapChain.Stage3.centredMoment_weak
#print axioms GapChain.Stage3.volumeU_tendsto
#print axioms GapChain.Stage3.volumeSide_tendsto
#print axioms GapChain.Stage3.rescale_cubicPeriods
#print axioms GapChain.Stage3.liftedWilson_unitCube
#print axioms GapChain.Stage3.smearedEnergy_unitTest
#print axioms GapChain.Stage3.measurable_smearedEnergy_unitTest
#print axioms GapChain.Stage3.centredMoment_unitTest
#print axioms GapChain.Stage3.liftedWilson_moments_unitCube
#print axioms GapChain.Stage3.cutoff_joint_moments
#print axioms GapChain.Stage3.frozenMoment_motion
#print axioms GapChain.Stage3.pushed_list_moment
#print axioms GapChain.Stage3.siteReflection_motion
#print axioms GapChain.Stage3.gridTranslation_motion
#print axioms GapChain.Stage3.frozen_smearedMean_motion
#print axioms GapChain.Stage3.unitTest_gridTranslation
#print axioms GapChain.Stage3.cutoff_translated_marks
#print axioms GapChain.Stage3.cutoff_polynomial_witness
#print axioms GapChain.Stage3.oddGrid_marginals
#print axioms GapChain.Stage3.volumeU_connected_sum
#print axioms GapChain.Stage3.slabEstimate_of_pairWindows
#print axioms GapChain.Stage3.release_sector_moments
#print axioms GapChain.Stage3.release_neutralTail
#print axioms GapChain.Stage3.neutralPartition_ratio
#print axioms GapChain.Stage3.divide_trace_error
#print axioms GapChain.Stage3.sectorResolution_of_slots
#print axioms GapChain.Stage3.markedSectorResolution
#print axioms GapChain.Stage3.vacuum_covariance
#print axioms GapChain.Stage3.release_neutralResolution
#print axioms GapChain.Stage3.calibrated_neutralResolution
#print axioms GapChain.Stage3.basis_insertedTrace_tail
#print axioms GapChain.Stage3.sector_trace_covariance
#print axioms GapChain.Stage3.markedSector_covariance
#print axioms GapChain.Stage3.split_marked_covariance
#print axioms GapChain.Stage3.normalized_split_covariance
#print axioms GapChain.Stage3.padded_vacuum_word
#print axioms GapChain.Stage3.normalized_single_window
#print axioms GapChain.Stage3.normalized_cyclic_words
#print axioms GapChain.Stage3.normalized_cyclic_single
#print axioms GapChain.Stage3.normalized_word_polynomials
#print axioms GapChain.Stage3.NeutralResolution.insertedTrace_tail
#print axioms GapChain.Stage3.NeutralResolution.normalized_contraction
#print axioms GapChain.Stage3.NeutralResolution.twoInsertion_trace
#print axioms GapChain.Stage3.slabEstimate_of_neutralComparison
#print axioms GapChain.Stage3.cutoff_bound_of_finiteTori
#print axioms GapChain.Stage3.seed_at_calibrated_cutoff
#print axioms GapChain.Stage3.calibratedSpectralPropagation
#print axioms GapChain.Stage3.expClusters_of_finiteTori
#print axioms GapChain.Stage3.expClusters_of_kappaSeed_of_finiteTori
#print axioms GapChain.Stage3.expClusters_of_kappaSeed_of_neutralComparison
#print axioms GapChain.Stage3.expClusters_of_seeded_windows
#print axioms GapChain.Stage3.expClusters_of_seeded_pairWindows
#print axioms GapChain.Stage3.expClusters_of_kappaSeed_of_pairWindows
#print axioms GapChain.Stage3.expClusters_of_kappaSeed_of_slabComparison
