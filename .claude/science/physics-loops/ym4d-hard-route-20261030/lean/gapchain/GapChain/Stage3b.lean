import GapChain.Stage3

/-!
# Periodic covariance of two Wilson windows

The transfer and cutoff conventions are those of Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text. We use the EV-L argument of rows
731–732, the design of rows 1457–1458, and the marked words of rows 1657 and 1666.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open Filter MeasureTheory
open scoped BigOperators Topology InnerProductSpace
open YangMills YangMills.Construction TransferOperators SeparatedTuples
open ReflectionPositivity.TupleForm ReflectionPositivity.Reconstruction LimitTheorem
open InfiniteLattice
open GapChain.Stage3

namespace GapChain.Stage3b

/-- Time coordinates inside this word start at zero, independently of its
placement on the circle. The label set and its coefficients can be held fixed
while changing the cube. -/
structure WordFamily (n : spatialAxis → ℕ) (V : ℕ) (J : Type) (width : ℕ) where
  mark : J → ZMod V → LayerMark n
  blind : ∀ j x, CentreBlind (mark j x)
  support : ∀ j x, x ∉ Set.range (fun i : Fin width => (i.val : ZMod V)) → mark j x = 1

namespace WordFamily
variable {n : spatialAxis → ℕ} {V u w : ℕ} {J K : Type} [Fintype J] [Fintype K]

def word (F : WordFamily n V J u) (j : J) := residueWord (F.mark j) 0 u

def cost (F : WordFamily n V J u) (x : J → ℂ) : ℝ :=
  ∑ j, ‖x j‖ * ((F.word j).map fun f => ‖f‖).prod

def value (F : WordFamily n V J u) (x : J → ℂ) (s : ZMod V)
    (z : JointSlice n (Fin V)) : ℂ :=
  ∑ j, x j * jointMark (finRotate _).symm (fun i => F.mark j ((i.val : ZMod V) - s)) z

/-- The product family retains the two original words and their separation. -/
def separated (F : WordFamily n V J u) (G : WordFamily n V K w) (g : ℕ) :
    WordFamily n V (J × K) (u+g+w) where
  mark p t := F.mark p.1 t * G.mark p.2 (t - ((u+g : ℕ) : ZMod V))
  blind p t e v z h := by
    simp only [ContinuousMap.mul_apply, F.blind _ _ e v z h, G.blind _ _ e v z h]
  support p t ht := by
    have hf : F.mark p.1 t = 1 := F.support _ _ (by
      rintro ⟨i, rfl⟩
      exact ht ⟨⟨i.val, by omega⟩, rfl⟩)
    have hg : G.mark p.2 (t - ((u+g : ℕ) : ZMod V)) = 1 := G.support _ _ (by
      rintro ⟨i, hi⟩
      apply ht
      refine ⟨⟨i.val+(u+g), by omega⟩, ?_⟩
      simpa only [Nat.cast_add] using eq_sub_iff_add_eq.mp hi)
    rw [hf, hg, mul_one]

theorem separated_value (F : WordFamily n V J u) (G : WordFamily n V K w)
    (x : J → ℂ) (y : K → ℂ) (s : ZMod V) (g : ℕ) (z : JointSlice n (Fin V)) :
    (F.separated G g).value (fun p => x p.1 * y p.2) s z =
      F.value x s z * G.value y (s + ((u+g : ℕ) : ZMod V)) z := by
  simp only [value, separated, sub_add_eq_sub_sub, jointMark_mul, Fintype.sum_prod_type,
    Finset.sum_mul, Finset.mul_sum]
  conv_rhs => rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  ring

omit [Fintype J] [Fintype K] in
/-- In the combined vacuum insertion the empty layers lie between the words. -/
theorem separated_word (F : WordFamily n V J u) (G : WordFamily n V K w)
    (g : ℕ) (fits : u+g+w ≤ V) (p : J × K) :
    (F.separated G g).word p =
      F.word p.1 ++ List.replicate g 1 ++ G.word p.2 := by
  let a := V-(u+g+w)
  have h := cyclic_two_words (F.mark p.1) (G.mark p.2) (0 : ZMod V) 0
    (by simpa using F.support p.1) (by simpa using G.support p.2) 0 g a (by dsimp [a]; omega)
  simp only [zero_add, Nat.cast_zero, sub_zero, List.replicate_zero, List.nil_append] at h
  let H := fun i : Fin V => F.mark p.1 (i.val : ZMod V) *
    G.mark p.2 ((i.val : ZMod V) - ((u+g : ℕ) : ZMod V))
  have seg := ofFn_word_segment H
    (fun i : Fin (u+g+w) => (F.separated G g).mark p (i.val : ZMod V)) 0 (by omega) (by intro i; simp [H,separated])
  simp only [List.drop_zero] at seg
  unfold word residueWord
  simp only [zero_add]
  rw [← seg]
  dsimp only [H]
  rw [h]
  apply List.take_left'
  simp only [List.length_append,List.length_ofFn,List.length_replicate]

theorem separated_cost (F : WordFamily n V J u) (G : WordFamily n V K w)
    (x : J → ℂ) (y : K → ℂ) (g : ℕ) (fits : u+g+w ≤ V) :
    (F.separated G g).cost (fun p => x p.1 * y p.2) = F.cost x * G.cost y := by
  simp only [cost, separated_word F G g fits, List.map_append, List.prod_append,
    List.map_replicate, List.prod_replicate, norm_one, one_pow, mul_one,
    Fintype.sum_prod_type, norm_mul, Finset.sum_mul, Finset.mul_sum]
  conv_rhs => rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  ring

omit [Fintype J] in
theorem word_norm_product (F : WordFamily n V J u) (j : J) :
    ((F.word j).map fun f => ‖f‖).prod = ∏ i : Fin u, ‖F.mark j (i.val : ZMod V)‖ := by
  simp only [word, residueWord, zero_add, List.map_ofFn, List.prod_ofFn, Function.comp_apply]

theorem cost_nonneg (F : WordFamily n V J u) (x : J → ℂ) : 0 ≤ F.cost x := by
  unfold cost
  simp only [word_norm_product]
  positivity

theorem norm_value_le (F : WordFamily n V J u) (x : J → ℂ) (s : ZMod V) (hw : u ≤ V)
    [NeZero V] (E : Fin V ≃ ZMod V) (hE : ∀ i, E i = (i.val : ZMod V))
    (z : JointSlice n (Fin V)) : ‖F.value x s z‖ ≤ F.cost x := by
  apply (norm_sum_le _ _).trans
  apply Finset.sum_le_sum
  intro j _
  rw [norm_mul, word_norm_product]
  apply mul_le_mul_of_nonneg_left _ (norm_nonneg _)
  unfold jointMark
  rw [norm_prod]
  calc
    _ ≤ ∏ i : Fin V, ‖F.mark j ((i.val : ZMod V)-s)‖ :=
      Finset.prod_le_prod (fun _ _ => norm_nonneg _) (fun _ _ => ContinuousMap.norm_coe_le_norm _ _)
    _ = ∏ t : ZMod V, ‖F.mark j t‖ := by
      simpa only [Equiv.trans_apply, Equiv.subRight_apply, hE] using
        (E.trans (Equiv.subRight s)).prod_comp (fun t => ‖F.mark j t‖)
    _ = _ := by
      simpa only [zero_add] using (residue_word_product hw (0 : ZMod V) (fun t => ‖F.mark j t‖)
        (by intro t ht; rw [F.support j t (by simpa using ht), norm_one])).symm

theorem continuous_value (F : WordFamily n V J u) (x : J → ℂ) (s : ZMod V) :
    Continuous (F.value x s) :=
  continuous_finsetSum _ fun _ _ => continuous_const.mul (continuous_jointMark _ _)

end WordFamily

abbrev spectrum {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice) :=
  (rectangularTorusData hβ).choose.spectrum (cube Γ.side)

abbrev CubeResolution {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice)
    (A : DiagonalTraces β (cube Γ.side)) :=
  SectorResolution (rectSector (fun _ => Γ.side) β zeroFlux zeroFlux) (spectrum hβ Γ)
    (fun i => A.value (zeroFlux,i))

section Spectral
variable {β : ℝ} {hβ : 0 < β} {Γ : CubicPeriodSublattice} {A : DiagonalTraces β (cube Γ.side)}

def vacuumValue (Q : CubeResolution hβ Γ A) {J : Type} [Fintype J] {V w : ℕ}
    (F : WordFamily (fun _ => Γ.side) V J w) (x : J → ℂ) : ℂ :=
  let o := Q.basis Q.vacuum
  ∑ j, x j * ⟪o,slabProduct _ β (spectrum hβ Γ).top zeroFlux (F.word j) o⟫_ℂ

theorem norm_vacuumValue_le (Q : CubeResolution hβ Γ A) {J : Type} [Fintype J] {V w : ℕ}
    (F : WordFamily (fun _ => Γ.side) V J w) (x : J → ℂ) : ‖vacuumValue Q F x‖ ≤ F.cost x := by
  let o := Q.basis Q.vacuum
  have unit : ‖o‖ = 1 := Q.basis.orthonormal.norm_eq_one _
  have hn := ((rectSymOperator_cube_norm Γ hβ zeroFlux).trans (congrArg norm (magneticTransfer_zero Γ hβ))).trans
    ((rectangularTorusData hβ).choose_spec.1.top Γ).symm
  apply (norm_sum_le _ _).trans
  apply Finset.sum_le_sum
  intro j _
  rw [norm_mul]
  apply mul_le_mul_of_nonneg_left _ (norm_nonneg _)
  let M := slabProduct _ β (spectrum hβ Γ).top zeroFlux (F.word j)
  calc
    ‖⟪o,M o⟫_ℂ‖ ≤ ‖o‖ * ‖M o‖ := norm_inner_le_norm _ _
    _ ≤ ‖M‖ := by simpa only [unit,one_mul,mul_one] using M.le_opNorm o
    _ ≤ _ := slabProduct_bound β zeroFlux (spectrum hβ Γ).top_pos hn _

set_option maxHeartbeats 900000 in
theorem separated_vacuum (Q : CubeResolution hβ Γ A)
    (enum : Wilson.EnumeratesRatios (spectrum hβ Γ) A.value (zeroFlux,0))
    {J K : Type} [Fintype J] [Fintype K] {V u w : ℕ}
    (F : WordFamily (fun _ => Γ.side) V J u) (G : WordFamily (fun _ => Γ.side) V K w)
    (x : J → ℂ) (y : K → ℂ) (g : ℕ) (fits : u+g+w ≤ V)
    {r : ℝ} (hr : (r : EReal) ≤ (spectrum hβ Γ).gap) :
    ‖vacuumValue Q (F.separated G g) (fun p => x p.1*y p.2) -
      vacuumValue Q F x * vacuumValue Q G y‖ ≤
      F.cost x * G.cost y * (2 * Real.exp (-r*g)) := by
  let B := spectrum hβ Γ
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let S := rectSector n β zeroFlux zeroFlux
  let T := ((B.top⁻¹ : ℝ) : ℂ) • S
  let M := slabProduct n β B.top zeroFlux
  have hn : ‖rectSymOperator n β zeroFlux‖ = B.top :=
    ((rectSymOperator_cube_norm Γ hβ zeroFlux).trans (congrArg norm (magneticTransfer_zero Γ hβ))).trans
      ((rectangularTorusData hβ).choose_spec.1.top Γ).symm
  have hs : T.IsSymmetric := by
    apply ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric.mp
    change star (((B.top⁻¹ : ℝ) : ℂ) • S) = _
    rw [star_smul,show star ((B.top⁻¹ : ℝ) : ℂ) = ((B.top⁻¹ : ℝ) : ℂ) from Complex.conj_ofReal _,
      show star S = S from (rectSector_positive _ hβ.le zeroFlux zeroFlux).isSelfAdjoint.star_eq]
  let o := Q.basis Q.vacuum
  let vac (l : List (LayerMark n)) := ⟪o,M l o⟫_ℂ
  let normWord (l : List (LayerMark n)) := (l.map fun f => ‖f‖).prod
  apply weighted_window_pair_bound x y (fun j k => vac ((F.separated G g).word (j,k)))
    (fun j => vac (F.word j)) (fun k => vac (G.word k)) (fun j => normWord (F.word j))
    (fun k => normWord (G.word k)) (2*Real.exp (-r*g))
  intro j k
  rw [WordFamily.separated_word _ _ _ fits]
  have hm : M (F.word j ++ List.replicate g 1 ++ G.word k) = (M (F.word j) * T^g) * M (G.word k) := by
    simp only [M,slabProduct,List.map_append,List.prod_append,List.map_replicate,List.prod_replicate,projectedLayer_one]
    rfl
  change ‖⟪_, M _ _⟫_ℂ - _‖ ≤ _
  rw [hm]
  have cov := vacuum_covariance A enum S Q T rfl hs hr (M (F.word j)) (M (G.word k)) g
  apply cov.trans
  have h := mul_le_mul (slabProduct_bound β zeroFlux B.top_pos hn (F.word j))
    (slabProduct_bound β zeroFlux B.top_pos hn (G.word k)) (norm_nonneg _) (by
      rw [WordFamily.word_norm_product]; positivity)
  nlinarith only [mul_le_mul_of_nonneg_right h (Real.exp_pos (-r*g)).le]

/-- Both estimates in the time average must refer to the same resolution.
The temporal period is independent of the spatial cube. -/
def PairTrace (Q : CubeResolution hβ Γ A) : Prop :=
  ∀ {J K : Type} [Fintype J] [Fintype K] {V u w : ℕ}
    (F : WordFamily (fun _ => Γ.side) V J u) (G : WordFamily (fun _ => Γ.side) V K w)
    (x : J → ℂ) (y : K → ℂ) (l d a : ℕ), 0 < l → 3 ≤ a → V = l+u+d+w+a →
    ∀ r : ℝ, (r : EReal) ≤ (spectrum hβ Γ).gap →
    ‖(∑ p : J×K,(x p.1*y p.2)*rawMarkedMean β zeroFlux (fun i : Fin V =>
        F.mark p.1 ((i.val : ZMod V) - l) * G.mark p.2 ((i.val : ZMod V) - ((l+u+d : ℕ) : ZMod V)))) /
        (sectorWeight β (boxSides (cube Γ.side) V) zeroFlux zeroFlux : ℂ) -
      vacuumValue Q F x * vacuumValue Q G y‖ ≤
      F.cost x * G.cost y * (2*Real.exp (-r*d) + 2*(spectrum hβ Γ).thermal a)

theorem common_resolution (hβ : 0 < β) (Γ : CubicPeriodSublattice) :
    ∃ (A : DiagonalTraces β (cube Γ.side)) (Q : CubeResolution hβ Γ A),
      Wilson.EnumeratesRatios (spectrum hβ Γ) A.value (zeroFlux,0) ∧ PairTrace Q := by
  obtain ⟨A,Q,enum,h⟩ := normalized_word_polynomials hβ Γ
  refine ⟨A,Q,enum,?_⟩
  intro J K _ _ V u w F G x y l d a hl ha size r hr
  obtain ⟨p,rfl⟩ : ∃ p, V = p+2 := ⟨V-2, by omega⟩
  simpa only [vacuumValue,WordFamily.cost,WordFamily.word,spectrum,zero_add] using h F.mark G.mark 0 0 x y F.blind G.blind
    (by simpa only [zero_add] using F.support) (by simpa only [zero_add] using G.support) l d a hl ha size r hr

theorem single_trace (Q : CubeResolution hβ Γ A) {J : Type} [Fintype J] {V w : ℕ}
    (F : WordFamily (fun _ => Γ.side) V J w) (x : J → ℂ) (l a : ℕ)
    (hl : 0 < l) (ha : 3 ≤ a) (size : V = l+w+a) :
    ‖(∑ j, x j * rawMarkedMean β zeroFlux (fun i : Fin V => F.mark j ((i.val : ZMod V) - l))) /
        (sectorWeight β (boxSides (cube Γ.side) V) zeroFlux zeroFlux : ℂ) - vacuumValue Q F x‖ ≤
      F.cost x * (2*(spectrum hβ Γ).thermal a) := by
  obtain ⟨p,rfl⟩ : ∃ p, V = p+2 := ⟨V-2, by omega⟩
  rw [Finset.sum_div]
  simp only [mul_div_assoc]
  apply weighted_window_bound
  intro j
  have h := normalized_cyclic_single hβ Γ Q (F.mark j) 0 (F.blind j)
    (by simpa using F.support j) l a hl ha size
  dsimp only at h
  simpa only [WordFamily.word,residueWord,spectrum,zero_add,mul_assoc,mul_left_comm] using h

end Spectral

def meanError (K : ℝ) (w : ℕ) (r : ℝ) : ℝ :=
  Real.sqrt (8*(2*K^2 + 3*K*(2*K) + 4*K^2) *
    (1+4*((w+1 : ℕ) : ℝ)*(∑' z : ℤ, (Real.exp (-r))^z.natAbs))) + 2*K

/-- Time averaging a real polynomial on a cube. Its physical position may
wrap the origin. Each copy used in the neutral estimates has a blank seam. -/
theorem polynomial_periodic {β : ℝ} {hβ : 0 < β} {Γ : CubicPeriodSublattice}
    {A : DiagonalTraces β (cube Γ.side)} (Q : CubeResolution hβ Γ A) (pairTrace : PairTrace Q)
    {J : Type} [Fintype J] {w : ℕ} (F : WordFamily (fun _ => Γ.side) Γ.side J w)
    (x : J → ℂ) (s : ZMod Γ.side) (G : JointSlice (fun _ => Γ.side) (Fin Γ.side) → ℝ)
    (repr : ∀ z,(G z : ℂ) = F.value x s z) {K r : ℝ} (hK : F.cost x ≤ K)
    (hr : 0 < r) (gap : (r : EReal) ≤ (spectrum hβ Γ).gap)
    (size : 4*(w+1)+6 ≤ Γ.side) (small : (spectrum hβ Γ).thermal (Γ.side/2) ≤ 1) :
    ‖((∫ z,G z ∂jointState (fun _ => Γ.side) β zeroFlux zeroFlux : ℝ) : ℂ) - vacuumValue Q F x‖ ≤
      meanError K w r * Real.sqrt (1/(Γ.side : ℝ) + (spectrum hβ Γ).thermal (Γ.side/2)) := by
  let V := Γ.side
  let B := spectrum hβ Γ
  let τ := B.thermal (V/2)
  let q := Real.exp (-r)
  let c := vacuumValue Q F x
  let sides : Wilson.Sides := fun _ => Γ.side
  let N := V/(2*(w+1))
  let start (i : Fin N) := 1+i.val*(w+1)
  have tall : 4*(w+1)+6 ≤ V := size
  have sidesEq : boxSides (cube Γ.side) Γ.side = sides := by funext i; fin_cases i <;> rfl
  have fits (i : Fin N) : 2*(start i+w) ≤ V := calc
    _ = (i.val+1)*(2*(w+1)) := by dsimp [start]; ring
    _ ≤ V/(2*(w+1))*(2*(w+1)) := Nat.mul_le_mul_right _ i.isLt
    _ ≤ V := Nat.div_mul_le_self _ _
  obtain ⟨E,next,hE⟩ := anchoredCubeTimeIndex Γ 0
  simp only [zero_add] at hE
  let delta (i : Fin N) := (start i : ZMod V)-s
  let rot (i : Fin N) := (translated_residue_rotation E next (delta i)).choose
  have comm (i : Fin N) : Commute (finRotate _).symm (rot i) := (translated_residue_rotation E next (delta i)).choose_spec.1
  have action (i : Fin N) (t : Fin V) : ((rot i t).val : ZMod V) - s = (t.val : ZMod V) - start i := by
    have hh := (translated_residue_rotation E next (delta i)).choose_spec.2 t
    change E (rot i t) = E t - delta i at hh
    rw [hE,hE] at hh
    rw [hh]; dsimp only [delta]; abel
  let label (j : J) (t : Fin V) := F.mark j ((t.val : ZMod V)-s)
  have rotated (i : Fin N) (z) : (G (relabelJoint (rot i) z) : ℂ) = F.value x (start i) z := by
    rw [repr]
    simp only [WordFamily.value, jointMark_relabel _ _ (comm i), action]
  have zeroK := (F.cost_nonneg x).trans hK
  have absG (z) : |G z| ≤ K := by
    rw [← Real.norm_eq_abs, ← Complex.norm_real, repr]
    exact (F.norm_value_le x s (by omega) E hE z).trans hK
  have hc : ‖c‖ ≤ K := (norm_vacuumValue_le Q F x).trans hK
  have half : 3 ≤ V/2 := by omega
  have τpos : 0 ≤ τ := B.thermal_nonneg _
  have single (i : Fin N) :
      ‖(jointNeutralMean sides β zeroFlux (fun z => G (relabelJoint (rot i) z)) : ℂ)-c‖ ≤ (2*K)*τ := by
    have f := fits i
    let a := V-(start i+w)
    have hfar : V/2 ≤ a := by dsimp [a]; omega
    have hh := single_trace Q F x (start i) a (by dsimp [start]; omega) (by omega) (by dsimp [a]; omega)
    rw [sidesEq] at hh
    rw [jointNeutral_polynomial sides (by change 2 ≤ V; omega) β zeroFlux _ x _ (rotated i)]
    apply hh.trans
    have ha := B.thermal_antitone half hfar
    calc
      _ ≤ K * (2 * τ) := mul_le_mul hK (by linarith only [ha]) (by positivity [B.thermal_nonneg a]) zeroK
      _ = _ := by ring
  have ordered (i j : Fin N) (lt : i.val < j.val) :
      ‖(jointNeutralMean sides β zeroFlux (fun z => G (relabelJoint (rot i) z)*G (relabelJoint (rot j) z)) : ℂ)-c^2‖ ≤
        (2*K^2)*(q^((j.val : ℤ)-i.val).natAbs+τ) := by
    obtain ⟨d,a,size',pos,near,far⟩ := time_average_placement i j lt
    change V = start i+w+d+w+a at size'
    change start j = start i+w+d at pos
    have repr₂ := rotated_polynomial_words (finRotate V).symm (rot i) (rot j) (comm i) (comm j)
      G G x x label label repr repr
    simp only [label, action] at repr₂
    rw [jointNeutral_polynomial sides (by change 2 ≤ V; omega) β zeroFlux _ _ _ repr₂]
    have hh := pairTrace F F x x (start i) d a (by dsimp [start]; omega) (by omega) size' r gap
    rw [sidesEq, ← pos, ← pow_two] at hh
    apply hh.trans
    have ha := B.thermal_antitone half far
    have nexp : Real.exp (-r * d) ≤ q^((j.val : ℤ)-i.val).natAbs := by
      rw [show ((j.val : ℤ)-i.val).natAbs = j.val-i.val by omega]
      dsimp [q]
      rw [← Real.exp_nat_mul]
      exact Real.exp_le_exp.mpr (by have : ((j.val-i.val : ℕ) : ℝ) ≤ d := by exact_mod_cast near
                                    nlinarith only [mul_le_mul_of_nonneg_left this hr.le])
    calc
      _ ≤ (K*K) * (2*q^((j.val : ℤ)-i.val).natAbs+2*τ) :=
        mul_le_mul (mul_le_mul hK hK (F.cost_nonneg x) zeroK) (by linarith only [nexp,ha])
          (add_nonneg (by positivity) (mul_nonneg (by norm_num) (B.thermal_nonneg _))) (mul_nonneg zeroK zeroK)
      _ = _ := by ring
  have pair (i j : Fin N) (ne : i ≠ j) :
      ‖(jointNeutralMean sides β zeroFlux (fun z => G (relabelJoint (rot i) z)*G (relabelJoint (rot j) z)) : ℂ)-c^2‖ ≤
        (2*K^2)*(q^((j.val : ℤ)-i.val).natAbs+τ) := by
    rcases lt_or_gt_of_ne ne with lt|lt
    · exact ordered i j lt
    · rw [show ((j.val : ℤ)-i.val).natAbs = ((i.val : ℤ)-j.val).natAbs by omega]
      simpa only [mul_comm (G (relabelJoint (rot j) _))] using ordered j i lt
  have two : 2 ≤ sides TimeAxis.timeIdx := by change 2 ≤ V; omega
  let n : spatialAxis → ℕ := fun _ => Γ.side
  let _ : BorelSpace (RectGauges n) := Pi.borelSpace
  let _ : BorelSpace (RectSlice n) := Pi.borelSpace
  let _ : BorelSpace (RectGauges n × RectSlice n) := Prod.borelSpace
  let _ : BorelSpace (JointSlice n (Fin V)) := Pi.borelSpace
  have lp (e i) : MemLp (fun z => G (relabelJoint (rot i) z)) 2 (jointState sides β e zeroFlux) := by
    let _ := jointState_probability sides β e zeroFlux two
    have eq : (fun z => G (relabelJoint (rot i) z)) = fun z => (F.value x (start i) z).re :=
      funext fun z => congrArg Complex.re (rotated i z)
    rw [eq]
    exact (Complex.continuous_re.comp (F.continuous_value x _)).memLp_of_hasCompactSupport (HasCompactSupport.of_compactSpace _)
  have per := periodic_polynomial_comparison sides hβ.le zeroFlux two G c (Nat.zero_lt_succ w)
    (show 4*(w+1) ≤ V by omega) rfl rot comm lp zeroK absG hc
    (show 0 ≤ 2*K by positivity) (show 0 ≤ 2*K^2 by positivity) τpos
    (Real.exp_pos (-r)).le (Real.exp_lt_one_iff.mpr (neg_lt_zero.mpr hr)) single pair
  let i₀ : Fin N := ⟨0, Nat.div_pos (by omega) (by omega)⟩
  have im := (Complex.abs_im_le_norm _).trans (single i₀)
  simp only [Complex.sub_im,Complex.ofReal_im,zero_sub,abs_neg] at im
  have τle : τ ≤ Real.sqrt (1/(V : ℝ)+τ) := Real.le_sqrt_of_sq_le (by
    have h : τ ≤ 1 := small
    nlinarith only [one_div_nonneg.mpr (Nat.cast_nonneg V : (0 : ℝ) ≤ V),mul_nonneg τpos (sub_nonneg.mpr h)])
  apply (Complex.norm_le_abs_re_add_abs_im _).trans
  simp only [Complex.sub_re,Complex.sub_im,Complex.ofReal_re,Complex.ofReal_im,zero_sub,abs_neg]
  unfold meanError
  rw [add_mul]
  exact add_le_add per (im.trans (mul_le_mul_of_nonneg_left τle (by positivity)))

section Cutoff

/-- The physical list observable in one fixed joint-coordinate chart. -/
def monomial {a : ℝ} (ν : Measure (GaugeField a)) (Γ : CubicPeriodSublattice)
    (E : Fin Γ.side ≃ ZMod Γ.side) (fs : List RealValued)
    (z : JointSlice (fun _ => Γ.side) (Fin Γ.side)) : ℝ :=
  (fs.map (fun f => smearedEnergy (unitTest a f)
    (Γ.lattice.lift (fieldOfPairs Γ ((physicalJointCoordinates Γ E).symm z))) -
    ∫ U, smearedEnergy f U ∂ν)).prod

theorem monomial_append {a : ℝ} (ν : Measure (GaugeField a)) (Γ : CubicPeriodSublattice)
    (E : Fin Γ.side ≃ ZMod Γ.side) (fs gs : List RealValued) (z) :
    monomial ν Γ E (fs++gs) z = monomial ν Γ E fs z * monomial ν Γ E gs z := by
  simp only [monomial,List.map_append,List.prod_append]

theorem list_product {α M : Type*} [CommMonoid M] (fs : List α) (f : α → M) :
    (fs.map f).prod = ∏ i : Fin fs.length, f (fs.get i) := by
  rw [← Fin.prod_univ_fun_getElem]
  rfl

theorem cutoff_list_chart {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k v : ℕ+)
    {β : ℝ} (hβ : 0 < β) (ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))) :
    ∃ (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side), Γ.side = volumeSide L k v ∧
      (∀ t,E (finRotate _ t) = E t+1) ∧ (∀ t,E t = (t.val : ZMod Γ.side)) ∧
      ∀ (fs : List RealValued), (∀ f ∈ fs, IsC1c f) →
        CutoffLimits.centredMoment (liftedWilsonMeasure L v k β) ν fs.get =
          ((∫ z,monomial ν Γ E fs z ∂jointState (fun _ => Γ.side) β zeroFlux zeroFlux : ℝ) : ℂ) := by
  obtain ⟨Γ,E,side,next,base,hm⟩ := cutoff_joint_moments hL k v hβ ν 0
  refine ⟨Γ,E,side,next,by simpa using base,fun fs hf => ?_⟩
  rw [← integral_complex_ofReal]
  apply (hm _ fs.get (fun i => hf _ (fs.get_mem i))).trans
  apply integral_congr_ae
  filter_upwards with z
  simp only [monomial,list_product,Complex.ofReal_prod]

def gridShift (a : ℝ) (d : ℕ) (fs : List RealValued) :=
  pushList (translate (((d : ℝ)*a) • timeBasisVec)) fs

theorem gridShift_zero (a : ℝ) (fs : List RealValued) : gridShift a 0 fs = fs := by
  simp only [gridShift,Nat.cast_zero,zero_mul,zero_smul,pushList]
  convert List.map_id fs using 2
  funext f t
  change f (invMap (SeparatedTuples.translate 0) t) = f t
  rw [ReflectionPositivity.LimitContraction.invMap_translate, sub_zero]

/-- The coefficients, temporal anchor, width and budget precede the cube.
All families can subsequently be read in the very same chart. This is a
pointwise identity and therefore also identifies products at different offsets. -/
theorem cutoff_word_family {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (fs : List RealValued) (hf : ∀ f ∈ fs, IsC1c f) :
    let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    ∃ (J : Type) (_ : Fintype J) (x : J → ℂ) (b : ℤ) (w : ℕ) (K : ℝ), 0 ≤ K ∧
      ∀ Γ : CubicPeriodSublattice, ∃ F : WordFamily (fun _ => Γ.side) Γ.side J w,
        (w ≤ Γ.side → F.cost x ≤ K) ∧ ∀ (E : Fin Γ.side ≃ ZMod Γ.side),
        (∀ t,E (finRotate _ t) = E t+1) → (∀ t,E t = (t.val : ZMod Γ.side)) →
        ∀ (d : ℕ) z, (monomial ν Γ E (gridShift a d fs) z : ℂ) =
          F.value x ((b : ZMod Γ.side)+(d : ZMod Γ.side)) z := by
  let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  obtain ⟨J,fi,x,t,b,w,_,families⟩ := cutoff_translated_marks hL k hβ hν fs.get
    (fun i => hf _ (fs.get_mem i))
  let K := ∑ j, ‖x j‖ * (2:ℝ)^fs.length
  refine ⟨J,fi,x,b,w,K,by dsimp [K]; positivity,fun Γ => ?_⟩
  obtain ⟨P,hb,_,supp,_,bound,expand⟩ := families Γ
  let F : WordFamily (fun _ => Γ.side) Γ.side J w := {
    mark := fun j t => P j ((b : ZMod Γ.side)+t)
    blind := fun j t => hb _ _
    support := fun j c hc => supp _ _ (by rintro ⟨i,hi⟩; exact hc ⟨i,add_left_cancel hi⟩) }
  refine ⟨F,fun fit => Finset.sum_le_sum (fun j _ => mul_le_mul_of_nonneg_left ?_ (norm_nonneg _)),
    fun E next origin d z => ?_⟩
  · rw [WordFamily.word_norm_product]
    simpa only [F,Fintype.card_fin] using bound j fit
  · let p := (physicalJointCoordinates Γ E).symm z
    have eqn := expand d p
    dsimp only at eqn
    unfold monomial gridShift pushList
    rw [List.map_map, list_product, Complex.ofReal_prod]
    refine eqn.trans ?_
    apply Finset.sum_congr rfl
    intro j _
    rw [physical_shifted_jointMark Γ E next,show physicalJointCoordinates Γ E p = z from
      (physicalJointCoordinates Γ E).apply_symm_apply z]
    simp only [origin,CubicPeriodSublattice.levelClass,Int.cast_natCast]
    congr 2
    funext i
    change P j _ = P j _
    congr 1
    abel

end Cutoff

def periodicMean (Γ : CubicPeriodSublattice) (β : ℝ)
    (G : JointSlice (fun _ => Γ.side) (Fin Γ.side) → ℝ) : ℂ :=
  ((∫ z,G z ∂jointState (fun _ => Γ.side) β zeroFlux zeroFlux : ℝ) : ℂ)

theorem norm_periodicMean_le (Γ : CubicPeriodSublattice) (β : ℝ) (hv : 2 ≤ Γ.side)
    (G : JointSlice (fun _ => Γ.side) (Fin Γ.side) → ℝ) {K : ℝ} (h : ∀ z, ‖G z‖ ≤ K) :
    ‖periodicMean Γ β G‖ ≤ K := by
  let μ := jointState (fun _ => Γ.side) β zeroFlux zeroFlux
  let _ : IsProbabilityMeasure μ := jointState_probability _ β _ _ hv
  simpa only [periodicMean, Complex.norm_real, probReal_univ, mul_one] using
    norm_integral_le_of_norm_le_const (μ := μ) (ae_of_all _ h)

theorem trivial_covariance (Γ : CubicPeriodSublattice) (β : ℝ) (hv : 2 ≤ Γ.side)
    (G H : JointSlice (fun _ => Γ.side) (Fin Γ.side) → ℝ) {K M : ℝ}
    (hb : ∀ z, ‖G z‖ ≤ K) (hc : ∀ z, ‖H z‖ ≤ M) (hK : 0 ≤ K) :
    ‖periodicMean Γ β (fun z => G z*H z) - periodicMean Γ β G * periodicMean Γ β H‖ ≤ 2*K*M := by
  have prod (z) : ‖G z * H z‖ ≤ K*M := by rw [norm_mul]; exact mul_le_mul (hb z) (hc z) (norm_nonneg _) hK
  apply (norm_sub_le _ _).trans
  rw [norm_mul]
  linarith only [norm_periodicMean_le Γ β hv _ prod,
    mul_le_mul (norm_periodicMean_le Γ β hv _ hb) (norm_periodicMean_le Γ β hv _ hc) (norm_nonneg _) hK]

/-- The physical moments and their *pointwise* product share one periodic
cube and one time chart. Each factor has a fixed budget before the displacement. -/
theorem cutoff_product_witness {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L) (k : ℕ+)
    {β : ℝ} (hβ : 0 < β) {ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))}
    (hν : IsInfiniteVolumeLimit L k β ν) (X Y : SepTuple) :
    let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
    ∃ (I : Type) (_ : Fintype I) (x : I → ℂ) (b : ℤ) (u : ℕ) (K : ℝ)
      (J : Type) (_ : Fintype J) (y : J → ℂ) (c : ℤ) (w : ℕ) (M : ℝ), 0 ≤ K ∧ 0 ≤ M ∧
      ∀ v : ℕ+, ∃ (Γ : CubicPeriodSublattice) (E : Fin Γ.side ≃ ZMod Γ.side)
        (F : WordFamily (fun _ => Γ.side) Γ.side I u) (H : WordFamily (fun _ => Γ.side) Γ.side J w),
        Γ.side = volumeSide L k v ∧ (∀ i, E i = (i.val : ZMod Γ.side)) ∧
        (u ≤ Γ.side → F.cost x ≤ K) ∧ (w ≤ Γ.side → H.cost y ≤ M) ∧
        ∀ d : ℕ, let G := monomial ν Γ E (pushList TimeAxis.timeReflection X.val)
                 let P := monomial ν Γ E (gridShift a d Y.val)
                 (∀ z, (G z : ℂ) = F.value x b z) ∧
                 (∀ z, (P z : ℂ) = H.value y ((c : ZMod Γ.side)+d) z) ∧
                 (∀ z, (monomial ν Γ E (pushList TimeAxis.timeReflection X.val ++ gridShift a d Y.val) z : ℂ) =
                   F.value x b z * H.value y ((c : ZMod Γ.side)+d) z) ∧
                 windowCovariance ν (liftedWilsonMeasure L v k β) X Y ((d : ℝ)*a) =
                   periodicMean Γ β (fun z => G z * P z) - periodicMean Γ β G * periodicMean Γ β P := by
  let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  let fs := pushList TimeAxis.timeReflection X.val
  have hf : ∀ f ∈ fs, IsC1c f := by
    dsimp only [fs]
    rw [← ConditionDefaults.push_val TheStatementsProvedTogether.separatedTuples_basic.1
      (ConditionDefaults.isEuclidIsometry_timeReflection TheStatementsProvedTogether.unit_normal_reflection_lattice_mirror)]
    exact (push _ X).2.1
  obtain ⟨I,fi,x,b,u,K,hK,xf⟩ := cutoff_word_family hL k hβ hν fs hf
  obtain ⟨J,fj,y,c,w,M,hM,yf⟩ := cutoff_word_family hL k hβ hν Y.val Y.2.1
  refine ⟨I,fi,x,b,u,K,J,fj,y,c,w,M,hK,hM,fun v => ?_⟩
  obtain ⟨Γ,E,side,next,origin,mom⟩ := cutoff_list_chart hL k v hβ ν
  obtain ⟨F,fc,hF⟩ := xf Γ
  obtain ⟨H,hc,hH⟩ := yf Γ
  refine ⟨Γ,E,F,H,side,origin,fc,hc,fun d => ?_⟩
  let gs := gridShift a d Y.val
  have hg : ∀ f ∈ gs, IsC1c f := by
    dsimp only [gs,gridShift]
    rw [← SeparatedTuples.push_translate_val]
    exact (push _ Y).2.1
  have first (z) : (monomial ν Γ E fs z : ℂ) = F.value x b z := by
    simpa only [gridShift_zero,Nat.cast_zero,add_zero] using hF E next origin 0 z
  have second := hH E next origin d
  refine ⟨first,second,?_,?_⟩
  · intro z
    change (monomial ν Γ E (fs ++ gs) z : ℂ) = _
    rw [monomial_append,Complex.ofReal_mul,first,second]
  · have hfg : ∀ f ∈ fs++gs, IsC1c f := by
      intro f h
      exact (List.mem_append.mp h).elim (hf f) (hg f)
    change CutoffLimits.centredMoment _ ν (fs++gs).get -
      CutoffLimits.centredMoment _ ν fs.get * CutoffLimits.centredMoment _ ν gs.get = _
    rw [mom _ hfg,mom _ hf,mom _ hg]
    simp only [periodicMean,monomial_append,fs,gs,a]

def covarianceError (K M : ℝ) (u w g : ℕ) (r : ℝ) :=
  meanError (K*M) (u+g+w) r + M * meanError K u r + K * meanError M w r

theorem meanError_nonneg {K : ℝ} (hK : 0 ≤ K) (w : ℕ) (r : ℝ) : 0 ≤ meanError K w r := by
  unfold meanError
  positivity

theorem covarianceError_nonneg {K M : ℝ} (hK : 0 ≤ K) (hM : 0 ≤ M) (u w g : ℕ) (r : ℝ) :
    0 ≤ covarianceError K M u w g r :=
  add_nonneg (add_nonneg (meanError_nonneg (mul_nonneg hK hM) _ _)
    (mul_nonneg hM (meanError_nonneg hK _ _))) (mul_nonneg hK (meanError_nonneg hM _ _))

/-- Three periodic comparisons use a single neutral vacuum; the two-word
vacuum covariance pays only the two separate budgets. -/
theorem separated_periodic_covariance {β : ℝ} (hβ : 0 < β) (Γ : CubicPeriodSublattice)
    {I J : Type} [Fintype I] [Fintype J] {u w : ℕ}
    (F : WordFamily (fun _ => Γ.side) Γ.side I u) (H : WordFamily (fun _ => Γ.side) Γ.side J w)
    (x : I → ℂ) (y : J → ℂ) (s : ZMod Γ.side) (g : ℕ)
    (G P : JointSlice (fun _ => Γ.side) (Fin Γ.side) → ℝ)
    (hf : ∀ z, (G z : ℂ) = F.value x s z)
    (hh : ∀ z, (P z : ℂ) = H.value y (s+((u+g : ℕ) : ZMod Γ.side)) z)
    {r K M : ℝ} (fc : F.cost x ≤ K) (hc : H.cost y ≤ M)
    (hr : 0 < r) (gap : (r : EReal) ≤ (spectrum hβ Γ).gap)
    (size : 4*(u+g+w+1)+6 ≤ Γ.side) (small : (spectrum hβ Γ).thermal (Γ.side/2) ≤ 1) :
    ‖periodicMean Γ β (fun z => G z * P z) - periodicMean Γ β G * periodicMean Γ β P‖ ≤
      K*M*(2*Real.exp (-r*g)) + covarianceError K M u w g r *
        Real.sqrt (1/(Γ.side : ℝ)+(spectrum hβ Γ).thermal (Γ.side/2)) := by
  obtain ⟨A,Q,enum,trace⟩ := common_resolution hβ Γ
  let S := F.separated H g
  let v := fun p : I × J => x p.1*y p.2
  have hfg (z) : ((G z * P z : ℝ) : ℂ) = S.value v s z := by
    rw [Complex.ofReal_mul,hf,hh,WordFamily.separated_value]
  have fg : F.cost x * H.cost y ≤ K*M :=
    mul_le_mul fc hc (H.cost_nonneg y) ((F.cost_nonneg x).trans fc)
  have sc : S.cost v ≤ K*M := (F.separated_cost H x y g (by omega)).trans_le fg
  have eFG := polynomial_periodic Q trace S v s _ hfg sc hr gap size small
  have eF := polynomial_periodic Q trace F x s G hf fc hr gap (by omega) small
  have eH := polynomial_periodic Q trace H y _ P hh hc hr gap (by omega) small
  have vac := separated_vacuum Q enum F H x y g (by omega) gap
  obtain ⟨E,_,hE⟩ := anchoredCubeTimeIndex Γ 0
  simp only [zero_add] at hE
  have Gbound (z) : ‖G z‖ ≤ K := by
    rw [← Complex.norm_real,hf]; exact (F.norm_value_le x s (by omega) E hE z).trans fc
  apply periodic_covariance_of_three_means _ _ _ _ _ _ (norm_periodicMean_le Γ β (by omega) G Gbound)
    ((norm_vacuumValue_le Q H y).trans hc) eFG eF eH
  exact vac.trans (mul_le_mul_of_nonneg_right fg (by positivity))

theorem exponential_offset {K M r : ℝ} (hK : 0 ≤ K) (hM : 0 ≤ M) (hr : 0 ≤ r)
    (d c g : ℕ) (hd : d ≤ g+(c+1)) :
    K*M*(2*Real.exp (-r*g)) ≤ (2*K*M*Real.exp (r*(c+1))) * Real.exp (-r*d) := by
  rw [mul_assoc (2*K*M), ← Real.exp_add]
  have bound : (d : ℝ) ≤ g+((c : ℝ)+1) := by exact_mod_cast hd
  have e := Real.exp_le_exp.mpr (show -r*(g : ℝ) ≤ r*((c : ℝ)+1) + -r*(d : ℝ) by
    nlinarith only [mul_le_mul_of_nonneg_left bound hr])
  calc
    _ = 2*K*M*Real.exp (-r*(g : ℝ)) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left e (by positivity)

/-- EV-L at the exact cutoff state and every positive lattice rate. The leading
constant is fixed before the separation. The opposite-arc error may depend on it. -/
theorem pairWindowEstimate {L : ℕ} (k : ℕ+) {β : ℝ}
    (ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ))))
    (hL : Conventions.IsAdmissibleBlockingFactor L) (hβ : 0 < β)
    (hν : IsInfiniteVolumeLimit L k β ν) (r : ℝ) (hr : 0 < r) :
    PairWindowEstimate L k β ν (rectangularTorusData hβ).choose r := by
  intro Z X Y
  obtain ⟨I,fi,x,b,u,K,J,fj,y,c,w,M,hK,hM,all⟩ := cutoff_product_witness hL k hβ hν X.val Y.val
  let c₀ := (b-c).natAbs + u
  let C := 2*K*M * Real.exp (r*((c₀ : ℝ)+1))
  have Cpos : 0 ≤ C := by dsimp [C]; positivity
  refine ⟨C,fun n => ?_⟩
  let d := 2*n+1
  let g := (c+(d : ℤ)-b-u).toNat
  let D := covarianceError K M u w g r + 2*K*M
  have errpos := covarianceError_nonneg hK hM u w g r
  have Dpos : 0 ≤ D := add_nonneg errpos (by positivity)
  refine ⟨D,?_⟩
  have grow := volumeSide_tendsto (L := L) (by have := hL.2; omega) (k : ℕ)
  filter_upwards [eventually_ge_atTop 1,grow (eventually_ge_atTop (4*(u+g+w+1)+6))] with v hv size
  let v' : ℕ+ := ⟨v,by omega⟩
  obtain ⟨Γ,E,F,H,side,origin,fc,hc,windows⟩ := all v'
  change Γ.side = volumeSide L k v at side
  have large : 4*(u+g+w+1)+6 ≤ Γ.side := side ▸ size
  let B := spectrum hβ Γ
  let a := PeriodicLattice.meshSize L ((k : ℕ) : ℤ)
  let G := monomial ν Γ E (pushList TimeAxis.timeReflection X.val.val)
  let P := monomial ν Γ E (gridShift a d Y.val.val)
  let τ := B.thermal (Γ.side/2)
  let δ := Real.sqrt (1/(Γ.side : ℝ)+τ)
  have castd : (d : ℝ) = 2*(n : ℝ)+1 := by dsimp [d]; push_cast; ring
  dsimp only
  rw [← castd, ← side]
  intro gap
  obtain ⟨hF,hH,_,cov⟩ := windows d
  change windowCovariance ν (liftedWilsonMeasure L v k β) X.val Y.val ((d : ℝ)*a) =
    periodicMean Γ β (fun z => G z * P z) - periodicMean Γ β G * periodicMean Γ β P at cov
  change ‖windowCovariance ν (liftedWilsonMeasure L v k β) X.val Y.val ((d : ℝ)*a)‖ ≤ _
  rw [cov]
  change ‖periodicMean Γ β (fun z => G z * P z) - periodicMean Γ β G * periodicMean Γ β P‖ ≤
    C*Real.exp (-r*d) + D*δ
  have boundF (z) : ‖G z‖ ≤ K := by
    rw [← Complex.norm_real,hF]
    exact (F.norm_value_le x _ (by omega) E origin z).trans (fc (by omega))
  have boundH (z) : ‖P z‖ ≤ M := by
    rw [← Complex.norm_real,hH]
    exact (H.norm_value_le y _ (by omega) E origin z).trans (hc (by omega))
  have trivial := trivial_covariance Γ β (by omega) G P boundF boundH hK
  have δpos : 0 ≤ δ := Real.sqrt_nonneg _
  by_cases close : d ≤ c₀
  · have bound := exponential_offset hK hM hr.le d c₀ 0 (by omega)
    simp only [Nat.cast_zero,mul_zero,Real.exp_zero,mul_one] at bound
    apply trivial.trans
    linarith only [bound,mul_nonneg Dpos δpos,show K*M*2 = 2*K*M by ring]
  by_cases small : τ ≤ 1
  · have place : (c : ZMod Γ.side)+(d : ZMod Γ.side) = (b : ZMod Γ.side)+((u+g : ℕ) : ZMod Γ.side) := by
      have eq : c+(d : ℤ) = b+((u+g : ℕ) : ℤ) := by
        dsimp only [c₀] at close
        dsimp only [g]
        omega
      simpa only [Int.cast_add,Int.cast_natCast] using congrArg (fun z : ℤ => (z : ZMod Γ.side)) eq
    have sep := separated_periodic_covariance hβ Γ F H x y (b : ZMod Γ.side) g G P hF
      (fun z => (hH z).trans (congrArg (fun t => H.value y t z) place))
      (fc (by omega)) (hc (by omega)) hr gap large small
    apply sep.trans
    apply add_le_add (exponential_offset hK hM hr.le d c₀ g (by dsimp [c₀,g]; omega))
    exact mul_le_mul_of_nonneg_right (le_add_of_nonneg_right (by positivity)) δpos
  · have one : 1 ≤ δ := by
      apply Real.le_sqrt_of_sq_le
      have := one_div_nonneg.mpr (Nat.cast_nonneg Γ.side : (0 : ℝ) ≤ Γ.side)
      linarith
    apply trivial.trans
    have hD : 2*K*M ≤ D := le_add_of_nonneg_left errpos
    linarith only [mul_le_mul hD one zero_le_one Dpos, mul_nonneg Cpos (Real.exp_pos (-r*d)).le]

/-- The calibrated Pfaffian seed implies exponential clustering at Stage 0's original type. -/
theorem expClusters_of_kappaSeed : type_of% @GapChain.expClusters_of_kappaSeed :=
  expClusters_of_kappaSeed_of_pairWindows @pairWindowEstimate

end GapChain.Stage3b

#print axioms GapChain.Stage3b.WordFamily.separated_value
#print axioms GapChain.Stage3b.WordFamily.separated_word
#print axioms GapChain.Stage3b.WordFamily.separated_cost
#print axioms GapChain.Stage3b.WordFamily.word_norm_product
#print axioms GapChain.Stage3b.WordFamily.cost_nonneg
#print axioms GapChain.Stage3b.WordFamily.norm_value_le
#print axioms GapChain.Stage3b.WordFamily.continuous_value
#print axioms GapChain.Stage3b.norm_vacuumValue_le
#print axioms GapChain.Stage3b.separated_vacuum
#print axioms GapChain.Stage3b.common_resolution
#print axioms GapChain.Stage3b.single_trace
#print axioms GapChain.Stage3b.polynomial_periodic
#print axioms GapChain.Stage3b.monomial_append
#print axioms GapChain.Stage3b.list_product
#print axioms GapChain.Stage3b.cutoff_list_chart
#print axioms GapChain.Stage3b.gridShift_zero
#print axioms GapChain.Stage3b.cutoff_word_family
#print axioms GapChain.Stage3b.norm_periodicMean_le
#print axioms GapChain.Stage3b.trivial_covariance
#print axioms GapChain.Stage3b.cutoff_product_witness
#print axioms GapChain.Stage3b.meanError_nonneg
#print axioms GapChain.Stage3b.covarianceError_nonneg
#print axioms GapChain.Stage3b.separated_periodic_covariance
#print axioms GapChain.Stage3b.exponential_offset
#print axioms GapChain.Stage3b.pairWindowEstimate
#print axioms GapChain.Stage3b.expClusters_of_kappaSeed
