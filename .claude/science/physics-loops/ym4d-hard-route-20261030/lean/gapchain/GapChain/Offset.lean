import GapChain.PurIo

/-!
# The volume-first limit at a fixed cutoff offset

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, supply the YM4 release (3932084a), its finite dilation identity and
volume compactness. Row 1678 selects the cutoffs. In first-passage units
each original test is composed with multiplication by the smaller mesh ratio.
-/

set_option autoImplicit false
set_option Elab.async false
noncomputable section

open Filter MeasureTheory Set YangMills YangMills.Construction
open YangMills.Formulation YangMills.ContinuumLimit
open TheStatementsProvedTogether PeriodicLattice LimitTheorem
open scoped Topology

namespace GapChain.Offset

/-- Pull a separated Euclidean test tuple back by scalar multiplication. -/
def scaleTuple {n : ℕ} {a : ℝ} (ha : 0 < a) (X : TestSpaces.SepTupleOfCard n) :
    TestSpaces.SepTupleOfCard n :=
  let e : InfiniteLattice.AmbientSpace ≃ₜ InfiniteLattice.AmbientSpace :=
    Homeomorph.smulOfNeZero a ha.ne'
  ⟨fun i x => X.1 i (a • x),
    fun i => ⟨(X.2.1 i).1.comp (contDiff_const_smul a),
      (X.2.1 i).2.1.comp_homeomorph e, subset_univ _⟩,
    fun _ _ hij => ((X.2.2 hij).preimage e).mono
      (tsupport_comp_subset_preimage _ e.continuous)
      (tsupport_comp_subset_preimage _ e.continuous)⟩

def scaleFamily {a : ℝ} (ha : 0 < a) (S : CumulantFamily) : CumulantFamily :=
  fun n hn X => S n hn (scaleTuple ha X)

theorem scaleTuple_inverse {n : ℕ} {a : ℝ} (ha : 0 < a) (X : TestSpaces.SepTupleOfCard n) :
    scaleTuple ha (scaleTuple (inv_pos.mpr ha) X) = X := by
  apply Subtype.ext
  funext i x
  change X.1 i (a⁻¹ • a • x) = X.1 i x
  rw [inv_smul_smul₀ ha.ne']

/-- The periodized tests at the two different physical sides are paired
exactly, including before any support lies in a fundamental cell. -/
theorem torus_cumulant_at_offset {L : ℕ} (hL : 3 ≤ L) (m J r : ℕ) (β : ℝ)
    {n : ℕ} (f : Fin n → InfiniteLattice.AmbientSpace → ℝ) :
    SchwingerFunctions.connectedSchwingerR4 L m (J + r) β f =
      SchwingerFunctions.connectedSchwingerR4 L (m + r) J β
        (fun i => TestFunctions.dilateR4 L r (f i)) := by
  have hpos : 0 < L := by omega
  have hratio : torusSide L m / torusSide L (m + r) = meshSize L (r : ℤ) := by
    simp only [torusSide, meshSize, zpow_neg, zpow_natCast, pow_add]
    field_simp
  unfold SchwingerFunctions.connectedSchwingerR4
  rw [connectedSchwinger_dilate_up four_point_cutoff_rescaling_invariant hL m (J + r) r
    (by omega) β, Nat.add_sub_cancel]
  congr 1
  funext i
  dsimp only [SchwingerFunctions.periodizeAll]
  rw [← TestFunctions.PairTransport.dilateTorus_eq_periodize (m := m) hpos r (f := f i) rfl]
  unfold FourPointBounds.dilateToSide TestFunctions.dilateTorus TestFunctions.contractTorus
  rw [hratio]
  rfl

/-- Shrinking growing passage tori by one fixed factor leaves growing tori
with positive integer exponents. The discarded prefix is common to all tests. -/
theorem shift_volumes {L : ℕ} (hL : 1 ≤ L) (r : ℕ) (s : ℕ → ℕ)
    (hs : Tendsto (fun i => torusSide L (s i)) atTop atTop) :
    ∃ (e : ℕ → ℕ) (v : ℕ → ℕ+), StrictMono e ∧
      (∀ i, (v i : ℕ) + r = s (e i)) ∧
      Tendsto (fun i => torusSide L (v i)) atTop atTop := by
  have hevent := hs.eventually_gt_atTop (torusSide L r)
  obtain ⟨e, he, he'⟩ := extraction_of_frequently_atTop hevent.frequently
  have hr i : r < s (e i) := by
    by_contra! h
    exact (he' i).not_ge (QuaternionicWilsonModel.TopLimitsRealNonzero.torusSide_mono hL h)
  let v (i : ℕ) : ℕ+ := ⟨s (e i) - r, Nat.sub_pos_of_lt (hr i)⟩
  have heq i : (v i : ℕ) + r = s (e i) := Nat.sub_add_cancel (hr i).le
  refine ⟨e, v, he, heq, ?_⟩
  have hpos : (0 : ℝ) < L := by exact_mod_cast hL
  apply ((hs.comp he.tendsto_atTop).atTop_mul_const (inv_pos.mpr (pow_pos hpos r))).congr
  intro i
  change torusSide L (s (e i)) * ((L : ℝ) ^ r)⁻¹ = _
  rw [← heq]
  simp only [torusSide, pow_add]
  field_simp

theorem mesh_at_offset {L J K r : ℕ} (h : J + r = K) :
    meshSize L (K : ℤ) = meshSize L (r : ℤ) * meshSize L (J : ℤ) := by
  subst K
  simp only [meshSize, zpow_neg, zpow_natCast, pow_add, mul_inv_rev]

/-- The release's pushforward of the passage state to the original mesh. -/
def stateAtOffset {L J K r : ℕ} (hL : 0 < L) (h : J + r = K)
    (μ : Measure (InfiniteLattice.RefinedGaugeField L J)) : Measure (InfiniteLattice.RefinedGaugeField L K) :=
  InfiniteLattice.scaledState (TestFunctions.PairTransport.meshSize_natCast_pos hL r) (mesh_at_offset h) μ

theorem stateAtOffset_cumulant {L J K r : ℕ} (hL : 0 < L) (h : J + r = K)
    (μ : Measure (InfiniteLattice.RefinedGaugeField L J)) (hp : IsProbabilityMeasure μ)
    {n : ℕ} (hn : 2 ≤ n) (X : TestSpaces.SepTupleOfCard n) :
    InfiniteLattice.smearedEnergyCumulant (stateAtOffset hL h μ) X.1 =
      InfiniteLattice.smearedEnergyCumulant μ (fun i => TestFunctions.dilateR4 L r (X.1 i)) := by
  have pos := TestFunctions.PairTransport.meshSize_natCast_pos hL
  have props := dilatedState_properties _ _ _ (pos J) (pos r) (mesh_at_offset (L := L) h)
  exact (props.2.2.2.2.1 μ hp).2.2 n (by omega) X.1 fun i =>
    InfiniteLattice.isBoundedBorelCompactlySupported_of_continuous (X.2.1 i).1.continuous (X.2.1 i).2.1

/-- Match one infinite-volume state on the passage lattice by a genuine
volume limit at the finer cutoff. Compactness is used on the very tori
defining the passage state. One subsequence works for all separated tuples. -/
theorem match_volume_state {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L)
    (J K : ℕ+) (r : ℕ) (hK : (J : ℕ) + r = K) {β : ℝ} (hβ : 0 < β)
    (μ : Measure (InfiniteLattice.RefinedGaugeField L J))
    (hμ : InfiniteLattice.IsInfiniteVolumeLimit L J β μ) :
    ∃ ν : Measure (InfiniteLattice.RefinedGaugeField L K),
      InfiniteLattice.IsInfiniteVolumeLimit L K β ν ∧
      ∀ n, 2 ≤ n → ∀ X : TestSpaces.SepTupleOfCard n,
        InfiniteLattice.smearedEnergyCumulant ν X.1 =
          InfiniteLattice.smearedEnergyCumulant (stateAtOffset (by have := hL.2; omega : 0 < L) hK μ) X.1 := by
  have h3 : 3 ≤ L := by have := hL.2; omega
  have ha := TestFunctions.PairTransport.meshSize_natCast_pos (by omega : 0 < L) r
  have bridge (k : ℕ+) := InfiniteLattice.VolumeLimitSymmetries.isInfiniteVolumeLimit_iff
    cutoff_covering_identifies_torus_measures periodicLift_clusterPt_seq_limit hL k hβ
  obtain ⟨q, ⟨s, ρ, hspos, hstop, hρ, hsq⟩, rfl⟩ := (bridge J μ).mp hμ
  have old := (torus_state_infinite_volume_limit_points L hL J J.pos β hβ).2.2.1
    s q ⟨hspos, hstop⟩ ⟨ρ, hρ, hsq⟩
  obtain ⟨e, v, he, hvol, hvtop⟩ := shift_volumes (by omega : 1 ≤ L) r s hstop
  let w (i : ℕ) : ℕ := v i
  have props := torus_state_infinite_volume_limit_points L hL K K.pos β hβ
  obtain ⟨t, ν, ht, hweak⟩ := props.1.2.2 w ⟨fun i => (v i).pos, hvtop⟩
  have hwt : InfiniteLattice.SideExponentsTendToInfinity L (w ∘ t) :=
    ⟨fun i => (v (t i)).pos, hvtop.comp ht.tendsto_atTop⟩
  have young := props.2.2.1 _ ν hwt hweak
  obtain ⟨η, hη, hην⟩ := hweak
  refine ⟨ν.1, (bridge K ν.1).mpr
    ⟨ν, ⟨w ∘ t, η, hwt.1, hwt.2, hη, hην⟩, rfl⟩, ?_⟩
  intro n hn X
  rw [stateAtOffset_cumulant _ _ q.1 q.2 hn X]
  have lip (Y : TestSpaces.SepTupleOfCard n) : InfiniteLattice.IsDisjointCompactLipschitzTuple Y.1 :=
    ⟨hn, fun i => FamiliesOfLimits.GrowingToriProof.isLipschitzFor_of_isC1c
      ⟨(Y.2.1 i).1, (Y.2.1 i).2.1⟩, fun i => (Y.2.1 i).2.1, fun _ _ h => Y.2.2 h⟩
  have a := (young.2.2 n X.1 (lip X)).2
  have b := ((old.2.2 n (scaleTuple ha X).1 (lip _)).2).comp (he.comp ht).tendsto_atTop
  apply tendsto_nhds_unique a
  apply b.congr
  intro i
  change SchwingerFunctions.connectedSchwingerR4 L (s (e (t i))) J β _ =
    SchwingerFunctions.connectedSchwingerR4 L (v (t i)) K β X.1
  rw [← hvol, ← hK]
  exact (torus_cumulant_at_offset h3 (v (t i)) J r β X.1).symm


/-! ## Dilation of separated lists and their canonical decomposition -/

open SeparatedTuples
open InfiniteLattice (AmbientSpace)

def scaleTest (a : ℝ) (f : RealValued) : RealValued := fun x => f (a • x)

theorem disjoint_scaled {a : ℝ} (ha : 0 < a) (f g : RealValued) :
    Disjoint (tsupport (scaleTest a f)) (tsupport (scaleTest a g)) ↔
      Disjoint (tsupport f) (tsupport g) := by
  have pushDisj {t : ℝ} {u v : RealValued} (h : Disjoint (tsupport u) (tsupport v)) :
      Disjoint (tsupport (scaleTest t u)) (tsupport (scaleTest t v)) :=
    (h.preimage (fun x : AmbientSpace => t • x)).mono
      (tsupport_comp_subset_preimage u (continuous_const_smul t))
      (tsupport_comp_subset_preimage v (continuous_const_smul t))
  refine ⟨fun h => ?_, pushDisj⟩
  have cancel (u : RealValued) : scaleTest a⁻¹ (scaleTest a u) = u := by
    funext x
    exact congrArg u (smul_inv_smul₀ ha.ne' x)
  simpa only [cancel] using pushDisj (t := a⁻¹) h

theorem disjointlySupported_scaled {a : ℝ} (ha : 0 < a) {xs : List RealValued}
    (h : IsDisjointlySupported xs) : IsDisjointlySupported (xs.map (scaleTest a)) := by
  refine ⟨?_, List.pairwise_map.mpr (h.2.imp fun hd => (disjoint_scaled ha _ _).mpr hd)⟩
  rintro _ hf
  obtain ⟨f, hmem, rfl⟩ := List.mem_map.mp hf
  exact ⟨(h.1 f hmem).1.comp (contDiff_const_smul a),
    (h.1 f hmem).2.comp_homeomorph (Homeomorph.smulOfNeZero a ha.ne')⟩

def scaleList {a : ℝ} (ha : 0 < a) (X : SepTuple) : SepTuple :=
  ⟨X.1.map (scaleTest a), disjointlySupported_scaled ha X.2⟩

def scaleFunctional {a : ℝ} (ha : 0 < a) (σ : TupleFunctional) : TupleFunctional :=
  ⟨fun X => σ (scaleList ha X), σ.map_nil⟩

theorem functional_ext {σ τ : TupleFunctional} (h : ∀ X, σ X = τ X) : σ = τ := by
  cases σ; cases τ
  congr
  exact funext h

theorem scaleList_toList {a : ℝ} (ha : 0 < a) {n : ℕ} (X : TestSpaces.SepTupleOfCard n) :
    scaleList ha (TupleLists.toList ⟨n, X⟩) = TupleLists.toList ⟨n, scaleTuple ha X⟩ := by
  apply Subtype.ext
  exact List.map_ofFn

theorem centred_scale {a : ℝ} (ha : 0 < a) (S : CumulantFamily) :
    centredOf (scaleFamily ha S) = scaleFunctional ha (centredOf S) := by
  apply functional_ext
  intro Z
  obtain ⟨⟨n, X⟩, rfl⟩ := TupleLists.sepTupleEquivList.surjective Z
  change TestSpaces.centredOfCumulants _ (TupleLists.ofList (TupleLists.toList ⟨n, X⟩)) =
    TestSpaces.centredOfCumulants S (TupleLists.ofList (scaleList ha (TupleLists.toList ⟨n, X⟩)))
  rw [scaleList_toList, TupleLists.ofList_toList, TupleLists.ofList_toList]
  rfl

theorem connected_scale {a : ℝ} (ha : 0 < a) (σ : TupleFunctional) {n : ℕ}
    (X : TestSpaces.SepTupleOfCard n) :
    connectedFn (scaleFunctional ha σ) X = connectedFn σ (scaleTuple ha X) := by
  unfold connectedFn TestSpaces.cumulant evalOnMap
  simp only [scaleFunctional, scaleList_toList]
  rfl

theorem nonGaussian_scale {a : ℝ} (ha : 0 < a) {σ : TupleFunctional}
    (h : ModelSeams.IsNonGaussianOnSmoothQuadruple σ) :
    ModelSeams.IsNonGaussianOnSmoothQuadruple (scaleFunctional ha σ) := by
  obtain ⟨X, hs, hX⟩ := h
  refine ⟨scaleTuple (inv_pos.mpr ha) X, fun i => (hs i).comp (contDiff_const_smul _), ?_⟩
  rwa [connected_scale, scaleTuple_inverse]

theorem scaleList_translate {a : ℝ} (ha : 0 < a) (v : AmbientSpace) (X : SepTuple) :
    scaleList ha (push (translate v) X) = push (translate (a⁻¹ • v)) (scaleList ha X) := by
  apply Subtype.ext
  simp only [scaleList, push_translate_val, pushList_translate, List.map_map]
  apply List.map_congr_left
  intro f _
  funext x
  change f (a • x - v) = f (a • (x - a⁻¹ • v))
  rw [smul_sub, smul_inv_smul₀ ha.ne']

theorem scaleList_juxt {a : ℝ} (ha : 0 < a) (X Y : SepTuple) :
    scaleList ha (X.juxt Y) = (scaleList ha X).juxt (scaleList ha Y) := by
  have iffcomp : (scaleList ha X).Composable (scaleList ha Y) ↔ X.Composable Y := by
    constructor
    · intro h f hf g hg
      exact (disjoint_scaled ha f g).mp (h _ (List.mem_map_of_mem hf) _ (List.mem_map_of_mem hg))
    · intro h f hf g hg
      obtain ⟨u, hu, rfl⟩ := List.mem_map.mp hf
      obtain ⟨v, hv, rfl⟩ := List.mem_map.mp hg
      exact (disjoint_scaled ha u v).mpr (h u hu v hv)
  by_cases h : X.Composable Y
  · apply Subtype.ext
    rw [SepTuple.juxt_val (iffcomp.mpr h)]
    exact (congrArg (List.map (scaleTest a)) (SepTuple.juxt_val h)).trans List.map_append
  · simp only [SepTuple.juxt, dif_neg h, dif_neg (iffcomp.not.mpr h)]
    rfl

def scalePlaced {a : ℝ} (ha : 0 < a) (p : SepTuple × AmbientSpace) : SepTuple × AmbientSpace :=
  (scaleList ha p.1, a⁻¹ • p.2)

theorem scale_shiftedJuxt {a : ℝ} (ha : 0 < a) (X : SepTuple) (P : List (SepTuple × AmbientSpace)) :
    scaleList ha (shiftedJuxt X P) = shiftedJuxt (scaleList ha X) (P.map (scalePlaced ha)) := by
  induction P generalizing X with
  | nil => rfl
  | cons p P ih =>
    change scaleList ha (shiftedJuxt _ P) = shiftedJuxt _ (P.map _)
    rw [ih, scaleList_juxt, scaleList_translate]
    rfl

theorem scale_shiftedComponents {a : ℝ} (ha : 0 < a) (X : SepTuple) (P : List (SepTuple × AmbientSpace)) :
    (shiftedComponents X P).map (scaleTest a) =
      shiftedComponents (scaleList ha X) (P.map (scalePlaced ha)) := by
  have tailEq : (P.flatMap fun p : SepTuple × AmbientSpace => (push (SeparatedTuples.translate p.2) p.1).1).map (scaleTest a) =
      (P.map (scalePlaced ha)).flatMap fun p : SepTuple × AmbientSpace => (push (SeparatedTuples.translate p.2) p.1).1 := by
    induction P with
    | nil => rfl
    | cons p P ih =>
      simp only [List.flatMap_cons, List.map_cons, List.map_append, ih]
      exact congrArg (· ++ _) (congrArg Subtype.val (scaleList_translate ha p.2 p.1))
  exact List.map_append.trans (congrArg (_ ++ ·) tailEq)

theorem scale_zip {a : ℝ} (ha : 0 < a) (Y : List SepTuple) (vs : List AmbientSpace) :
    (Y.zip vs).map (scalePlaced ha) = (Y.map (scaleList ha)).zip (vs.map (a⁻¹ • ·)) := by
  induction Y generalizing vs with
  | nil => simp
  | cons y ys ih => cases vs <;> simp [scalePlaced, ih]

theorem scale_atInfinity {a : ℝ} (ha : 0 < a) :
    map (fun v : AmbientSpace => a • v) (atInfinityWithin univ) = atInfinityWithin univ := by
  rw [atInfinityWithin_univ]
  have go {t : ℝ} (ht : 0 < t) : Tendsto (fun v : AmbientSpace => t • v) atInfinity atInfinity := by
    apply tendsto_comap_iff.mpr
    have h : Tendsto TorusMetric.euclidNormVec atInfinity atTop := tendsto_comap
    simpa [Function.comp_def, TestFunctions.PairTransport.euclidNormVec_smul, abs_of_pos ht]
      using h.const_mul_atTop ht
  refine le_antisymm (go ha) ?_
  have h := Filter.map_mono (m := fun v : AmbientSpace => a • v) (go (inv_pos.mpr ha))
  change map (fun v : AmbientSpace => a • v) (map (fun v : AmbientSpace => a⁻¹ • v) atInfinity) ≤ _ at h
  rw [Filter.map_map, show ((fun v : AmbientSpace => a • v) ∘ fun v => a⁻¹ • v) = id from
    funext (smul_inv_smul₀ ha.ne'), Filter.map_id] at h
  exact h

theorem iterLimit_scale {a : ℝ} (ha : 0 < a) (σ : TupleFunctional) (X : SepTuple)
    (Y : List SepTuple) (k : ℕ) (vs : List AmbientSpace) :
    iterLimitValue (scaleFunctional ha σ) X Y univ k vs =
      iterLimitValue σ (scaleList ha X) (Y.map (scaleList ha)) univ k (vs.map (a⁻¹ • ·)) := by
  induction k generalizing vs with
  | zero =>
    change σ (scaleList ha (shiftedJuxt X (Y.zip vs))) = _
    rw [scale_shiftedJuxt, scale_zip]
    rfl
  | succ k ih =>
    simp only [iterLimitValue, ih, List.map_cons]
    unfold limUnder
    rw [show (fun v : AmbientSpace => iterLimitValue σ (scaleList ha X) (Y.map (scaleList ha)) univ k
        (a⁻¹ • v :: vs.map (a⁻¹ • ·))) =
      (fun u => iterLimitValue σ (scaleList ha X) (Y.map (scaleList ha)) univ k
        (u :: vs.map (a⁻¹ • ·))) ∘ (fun v : AmbientSpace => a⁻¹ • v) from rfl,
      ← Filter.map_map, scale_atInfinity (inv_pos.mpr ha)]

def scaleDecomposition {a : ℝ} (ha : 0 < a) (A : DecompositionData) : DecompositionData :=
  { A with comp := fun ξ => scaleFunctional ha (A.comp ξ) }

theorem canonical_scale {a : ℝ} (ha : 0 < a) {σ : TupleFunctional} {A : DecompositionData}
    (hA : A.IsCanonical σ) : (scaleDecomposition ha A).IsCanonical (scaleFunctional ha σ) := by
  refine ⟨hA.compact, hA.metrizable, hA.isProb, hA.measureSupport_eq, ?_, ?_,
    fun X => hA.continuous_comp (scaleList ha X), ?_, ?_, ?_⟩
  · intro ξ X π
    let e := finCongr (List.length_map (f := scaleTest a) (as := X.1))
    let τ := (e.trans π).trans e.symm
    apply Eq.trans _ (hA.comp_permInvariant ξ (scaleList ha X) τ)
    apply congrArg (A.comp ξ)
    apply Subtype.ext
    simp only [scaleList, SepTuple.reorder, List.map_ofFn]
    apply List.ext_getElem
    · simp
    · intro i hi hj
      simp [e, τ, Function.comp_def, List.get_eq_getElem]
      rfl
  · intro ξ B C f g u v X Y Z hx hy hz
    apply hA.comp_entrywiseLinear ξ (B.map (scaleTest a)) (C.map (scaleTest a))
      (scaleTest a f) (scaleTest a g) u v (scaleList ha X) (scaleList ha Y) (scaleList ha Z)
    all_goals simp only [scaleList, hx, hy, hz, List.map_append, List.map_cons]
    rfl
  · intro x y hxy
    apply hA.comp_injective
    apply functional_ext
    intro X
    have h := congrArg (fun F : TupleFunctional => F (scaleList (inv_pos.mpr ha) X)) hxy
    have eqn : scaleList ha (scaleList (inv_pos.mpr ha) X) = X := by
      apply Subtype.ext
      have eqf : scaleTest a ∘ scaleTest a⁻¹ = id := by
        funext f x
        exact congrArg f (inv_smul_smul₀ ha.ne' x)
      simp only [scaleList, List.map_map, eqf, List.map_id]
    change A.comp x (scaleList ha _) = A.comp y (scaleList ha _) at h
    rwa [eqn] at h
  · intro X Y k hk vs hvs
    let Y' := Y.map (scaleList ha)
    let vs' := vs.map (a⁻¹ • ·)
    have hd : vs' ∈ iterLimitDomain (scaleList ha X) Y' univ (k + 1) := by
      refine ⟨by simpa [vs', Y'] using hvs.1, fun _ _ => mem_univ _, ?_⟩
      have h := disjointlySupported_scaled ha hvs.2.2
      rw [scale_shiftedComponents ha, scale_zip ha, List.map_drop] at h
      exact h
    obtain ⟨c, hc⟩ := hA.iterLimits_exist (scaleList ha X) Y' k (by simpa [Y'] using hk) vs' hd
    refine ⟨c, ?_⟩
    simp only [iterLimit_scale ha, List.map_cons]
    exact
      hc.comp (show Tendsto (fun x : AmbientSpace => a⁻¹ • x) (atInfinityWithin univ)
        (atInfinityWithin univ) from (scale_atInfinity (inv_pos.mpr ha)).le)
  · intro X Y
    change _ = iterLimitValue _ X Y univ Y.length []
    rw [iterLimit_scale ha]
    have h := hA.integral_comp_prod (scaleList ha X) (Y.map (scaleList ha))
    simp only [iteratedLimitAtInfinity, List.length_map, List.map_map, Function.comp_def] at h
    exact h


/-! ## Schwinger representatives and a uniform growth bound -/

open ConfigSpace SchwartzOps
open scoped ENNReal ComplexConjugate

/-- A dimension-independent column bound for dilation controls all orders of
the Schwinger sequence after raising one fixed factor to the Schwartz order. -/
def scaleCost (a : ℝ) : ℝ := max 1 a⁻¹ * max 1 a

theorem scaleCost_pos (a : ℝ) : 0 < scaleCost a :=
  mul_pos (zero_lt_one.trans_le (le_max_left ..)) (zero_lt_one.trans_le (le_max_left ..))

def scaleLinear (a : ℝ) (n : ℕ) : Config n →L[ℝ] Config n := a • ContinuousLinearMap.id ℝ _

theorem scale_affine (a : ℝ) {n : ℕ} (x : Config n) : affineOf (scaleLinear a n) 0 x = a • x := by
  simp [affineOf, scaleLinear]

theorem scale_weight {a : ℝ} (ha : 0 < a) {n : ℕ} (x : Config n) :
    1 + euclidNorm x ^ 2 ≤ (max 1 a⁻¹) ^ 2 * (1 + euclidNorm (a • x) ^ 2) := by
  have he : euclidNorm (a • x) ^ 2 = a ^ 2 * euclidNorm x ^ 2 := by
    rw [euclidNorm_sq_eq_sum_sq, euclidNorm_sq_eq_sum_sq, Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by
      rw [Pi.smul_apply, TestFunctions.PairTransport.euclidNormVec_smul, abs_of_pos ha, mul_pow]
  have hb : 1 ≤ max 1 a⁻¹ := le_max_left ..
  have hab : 1 ≤ max 1 a⁻¹ * a := by
    simpa [ha.ne'] using mul_le_mul_of_nonneg_right (le_max_right 1 a⁻¹) ha.le
  rw [he]
  calc
    1 + euclidNorm x ^ 2 ≤ (max 1 a⁻¹) ^ 2 + (max 1 a⁻¹ * a) ^ 2 * euclidNorm x ^ 2 :=
      add_le_add (one_le_pow₀ hb) (le_mul_of_one_le_left (sq_nonneg _) (one_le_pow₀ hab))
    _ = _ := by ring

theorem scale_schwartz_bound {a : ℝ} (ha : 0 < a) {n : ℕ} {f : Config n → ℂ}
    (hf : IsSchwartz f) (k : ℕ) :
    schwartzSeminorm k (fun x => f (a • x)) ≤ ENNReal.ofReal (scaleCost a ^ k) * schwartzSeminorm k f := by
  classical
  have hcol (p : Fin n × Fin 4) :
      ∑ b : Fin n × Fin 4, |(scaleLinear a n (unitVec p)) b.1 b.2| ≤ max 1 a := by
    rw [Finset.sum_eq_single p]
    · simp [scaleLinear, unitVec, abs_of_pos ha]
    · rintro ⟨i, μ⟩ _ h
      rcases p with ⟨j, ν⟩
      by_cases hij : i = j
      · subst j
        have hne : μ ≠ ν := fun e => h (by rw [e])
        simp [scaleLinear, unitVec, Pi.single_eq_of_ne hne]
      · simp [scaleLinear, unitVec, Pi.single_eq_of_ne hij]
    · simp
  have hb : 0 < max 1 a⁻¹ := zero_lt_one.trans_le (le_max_left ..)
  have h := schwartzSeminorm_comp_le (scaleLinear a n) 0 (le_max_left 1 a) hcol (sq_pos_of_pos hb)
    (fun x => by rw [scale_affine]; exact scale_weight ha x) hf.1 k
    ((isSchwartz_iff_mem_schwartzSpace.mp hf).2 k)
  have e : ((max 1 a⁻¹) ^ 2) ^ ((k : ℝ) / 2) = (max 1 a⁻¹) ^ k := by
    rw [← Real.rpow_natCast_mul hb.le]
    norm_num only [Nat.cast_ofNat]
    rw [show 2 * ((k : ℝ) / 2) = k by ring, Real.rpow_natCast]
  simpa only [Function.comp_def, scale_affine, e, scaleCost, mul_pow] using h

theorem scale_flat_on_domain {a : ℝ} (ha : 0 < a) {n : ℕ} {f : Config n → ℂ}
    {V : Set (Config n)} (hV : IsOpen V) (hstable : ∀ x, a • x ∈ V → x ∈ V)
    (hf : IsSchwartz f ∧ FlatOff f V) :
    IsSchwartz (fun x => f (a • x)) ∧ FlatOff (fun x => f (a • x)) V := by
  have hb : 0 < max 1 a⁻¹ := zero_lt_one.trans_le (le_max_left ..)
  simpa only [Function.comp_def, scale_affine] using
    flatOff_comp_affineOf (scaleLinear a n) 0 (sq_pos_of_pos hb)
      (fun x => by rw [scale_affine]; exact scale_weight ha x)
      hV (fun x hx => by rw [scale_affine]; exact fun h => hx (hstable x h)) hf

theorem scale_diagonal {a : ℝ} (ha : 0 < a) {n : ℕ} {f : Config n → ℂ}
    (hf : f ∈ schwartzFlatOffDiagonal n) : (fun x => f (a • x)) ∈ schwartzFlatOffDiagonal n :=
  scale_flat_on_domain ha isOpen_distinctArgs
    (fun _ h _ _ e => h (congrArg (a • ·) e)) hf

theorem scale_posTime {a : ℝ} (ha : 0 < a) {n : ℕ} {f : Config n → ℂ}
    (hf : f ∈ schwartzFlatOffPosTime n) : (fun x => f (a • x)) ∈ schwartzFlatOffPosTime n := by
  apply scale_flat_on_domain ha isOpen_posTimeSet _ hf
  intro x hx
  refine ⟨fun _ _ e => hx.1 (congrArg (a • ·) e), fun i => ?_⟩
  exact pos_of_mul_pos_right (show 0 < a * x i 3 from hx.2 i) ha.le

def scaleRaw (a : ℝ) : {n : ℕ} → FnOrScalar n → FnOrScalar n
  | 0, c => c
  | _ + 1, f => fun x => f (a • x)

theorem scale_flat_mem {a : ℝ} (ha : 0 < a) {n : ℕ} {f : FnOrScalar n} :
    scaleRaw a f ∈ flatOffDiagonalAt n ↔ f ∈ flatOffDiagonalAt n := by
  cases n with
  | zero => rfl
  | succ n =>
    refine ⟨fun h => ?_, fun h => scale_diagonal ha h⟩
    have ht := scale_diagonal (inv_pos.mpr ha) h
    change (fun x => f (a • a⁻¹ • x)) ∈ schwartzFlatOffDiagonal (n+1) at ht
    have hc : (fun x : Config (n+1) => f (a • a⁻¹ • x)) = f := by
      funext x
      rw [smul_inv_smul₀ ha.ne']
    rw [hc] at ht
    exact ht

def scaleFlat {a : ℝ} (ha : 0 < a) (T : FlatSequence) : FlatSequence :=
  fun _ f => T _ ⟨scaleRaw a f.1, (scale_flat_mem ha).mpr f.2⟩

theorem scale_bracket {a : ℝ} (ha : 0 < a) {n : ℕ} (f : schwartzFlatOffDiagonal n) (k : ℕ) :
    bracketNorm k (toSchwartzFn ⟨_, scale_diagonal ha f.2⟩) ≤
      scaleCost a ^ k * bracketNorm k (toSchwartzFn f) := by
  have hf := (isSchwartz_iff_mem_schwartzSpace.mp f.2.1).2 k
  have bound := scale_schwartz_bound ha f.2.1 k
  have hz := ENNReal.toReal_mono (ENNReal.mul_lt_top ENNReal.ofReal_lt_top hf).ne bound
  simpa only [bracketNorm, toSchwartzFn, ENNReal.toReal_mul,
    ENNReal.toReal_ofReal (pow_nonneg (scaleCost_pos a).le k)] using hz

def scaleConstants (a : ℝ) (D : SystemsWithFiveBounds.LimitConstants) :
    SystemsWithFiveBounds.LimitConstants :=
  { D with schwartzBase := D.schwartzBase * scaleCost a ^ D.schwartzOrder }

theorem scaleConstants_valid {a : ℝ} {D : SystemsWithFiveBounds.LimitConstants} (hD : D.Valid) :
    (scaleConstants a D).Valid :=
  { hD with schwartzBase_pos := mul_pos hD.schwartzBase_pos (pow_pos (scaleCost_pos a) _) }

theorem scale_growth {a : ℝ} (ha : 0 < a) {D : SystemsWithFiveBounds.LimitConstants} (hD : D.Valid)
    {T : FlatSequence} (hT : SystemsWithFiveBounds.SatisfiesGrowth T D.schwartzOrder
      D.schwartzPrefactor D.schwartzBase D.schwartzExp) :
    SystemsWithFiveBounds.SatisfiesGrowth (scaleFlat ha T) D.schwartzOrder D.schwartzPrefactor
      (scaleConstants a D).schwartzBase D.schwartzExp := by
  intro m f
  have ht := hT m ⟨_, scale_diagonal ha f.2⟩
  apply ht.trans
  refine (mul_le_mul_of_nonneg_left (scale_bracket ha f (D.schwartzOrder * (m + 1)))
    (mul_nonneg (mul_nonneg hD.schwartzPrefactor_pos.le (pow_nonneg hD.schwartzBase_pos.le _))
      (Real.rpow_nonneg (Nat.cast_nonneg _) _))).trans_eq ?_
  simp only [scaleConstants, mul_pow, pow_mul]
  ring

def scaleSepFamily {a : ℝ} (ha : 0 < a) {n : ℕ} (X : SepFamilyOfLength n) : SepFamilyOfLength n :=
  ⟨fun i => scaleTest a (X.1 i), fun i => by
    obtain ⟨_, hc, hk, _⟩ := mem_realC1CompactIn_iff.mp (X.2.1 i)
    exact mem_realC1CompactIn_iff.mpr ⟨isOpen_univ, hc.comp (contDiff_const_smul a),
      (show HasCompactSupport (X.1 i) from hk).comp_homeomorph (Homeomorph.smulOfNeZero a ha.ne'), subset_univ _⟩,
    fun _ _ h => (disjoint_scaled ha _ _).mpr (X.2.2 h)⟩

theorem eval_sep_scale {a : ℝ} (ha : 0 < a) (σ : TupleFunctional) {n : ℕ} (X : SepFamilyOfLength n) :
    SystemsWithFiveBounds.evalOnSepFamily (scaleFunctional ha σ) ⟨n, X⟩ =
      SystemsWithFiveBounds.evalOnSepFamily σ ⟨n, scaleSepFamily ha X⟩ :=
  congrArg σ (scaleList_toList ha _)

theorem scale_representative {a : ℝ} (ha : 0 < a) {σ : TupleFunctional} {T : FlatSequence}
    (h : SystemsWithFiveBounds.HasSchwingerSequence σ T) :
    SystemsWithFiveBounds.HasSchwingerSequence (scaleFunctional ha σ) (scaleFlat ha T) := by
  refine ⟨⟨?_, ?_⟩, fun c => h.2.1 c, fun m => ⟨⟨?_, ?_⟩, ?_⟩⟩
  · exact h.1.1
  · intro n hn i b c X Y Z hXY hz hZX
    simp only [eval_sep_scale]
    exact h.1.2 n hn i b c (scaleSepFamily ha X) (scaleSepFamily ha Y) (scaleSepFamily ha Z)
      (fun j hj => congrArg (scaleTest a) (hXY j hj)) (congrArg (scaleTest a) hz)
      (fun j hj => congrArg (scaleTest a) (hZX j hj))
  · intro b c f g u he
    exact (h.2.2 m).1.1 b c ⟨_, scale_diagonal ha f.2⟩ ⟨_, scale_diagonal ha g.2⟩
      ⟨_, scale_diagonal ha u.2⟩ (congrArg (fun v : Config (m+1) → ℂ => fun x => v (a • x)) he)
  · obtain ⟨k, C, hk, hC, hb⟩ := (h.2.2 m).1.2
    refine ⟨k, C * scaleCost a ^ k, hk, mul_nonneg hC (pow_nonneg (scaleCost_pos a).le _), fun f => ?_⟩
    exact (hb ⟨_, scale_diagonal ha f.2⟩).trans
      ((mul_le_mul_of_nonneg_left (scale_bracket ha f k) hC).trans_eq (mul_assoc ..).symm)
  · intro X hs hf
    rw [eval_sep_scale]
    apply (h.2.2 m).2 (scaleSepFamily ha X) _ (scale_diagonal ha hf)
    intro i
    obtain ⟨_, hc, hk, _⟩ := mem_realSmoothCompactIn_iff.mp (hs i)
    exact mem_realSmoothCompactIn_iff.mpr ⟨isOpen_univ, hc.comp (contDiff_const_smul a),
      (show HasCompactSupport (X.1 i) from hk).comp_homeomorph (Homeomorph.smulOfNeZero a ha.ne'), subset_univ _⟩


/-! ## Euclidean symmetries, reflection positivity and component clustering -/

theorem scale_motion {a : ℝ} (ha : 0 < a) (R : EuclidMotion) :
    ∃ Q : EuclidMotion, ∀ x : AmbientSpace, R.invMap (a • x) = a • Q.invMap x := by
  obtain ⟨M, hM, v, hRv⟩ := R.2
  let Q : EuclidMotion := ⟨fun x => M.mulVec x + a⁻¹ • v, M, hM, a⁻¹ • v, fun _ => rfl⟩
  refine ⟨Q, fun x => ?_⟩
  rw [R.invMap_eq hM hRv, Q.invMap_eq hM (v := a⁻¹ • v) (fun _ => rfl),
    ← Matrix.mulVec_smul, smul_sub, smul_inv_smul₀ ha.ne']

theorem scale_euclidInvariant {a : ℝ} (ha : 0 < a) {T : FlatSequence} (h : IsEuclidInvariant T) :
    IsEuclidInvariant (scaleFlat ha T) := by
  intro m f R hf
  obtain ⟨Q, hQ⟩ := scale_motion ha R
  have eqn : (fun x => motionAct R f.1 (a • x)) = motionAct Q (fun x => f.1 (a • x)) := by
    funext x
    change f.1 (fun i => R.invMap (a • x i)) = _
    simp only [hQ]
    rfl
  have hm := scale_diagonal ha hf
  rw [eqn] at hm
  exact (congrArg (T.atSucc m) (Subtype.ext eqn)).trans (h m ⟨_, scale_diagonal ha f.2⟩ Q hm)

theorem scale_permSymmetric {a : ℝ} (ha : 0 < a) {T : FlatSequence} (h : IsPermSymmetric T) :
    IsPermSymmetric (scaleFlat ha T) := fun m f π hp =>
  h m ⟨_, scale_diagonal ha f.2⟩ π (scale_diagonal ha hp)

theorem scale_flip (a : ℝ) {n : ℕ} (f : FnOrScalar n) :
    scaleRaw a (flipConjAt f) = flipConjAt (scaleRaw a f) := by
  cases n with
  | zero => rfl
  | succ n =>
    funext x
    have h (v : AmbientSpace) : timeFlip (a • v) = a • timeFlip v := by
      funext i
      fin_cases i <;> simp [timeFlip]
    change starRingEnd ℂ (f (fun i => timeFlip (a • x i))) = _
    simp only [h]
    rfl

theorem scale_reflectionReal {a : ℝ} (ha : 0 < a) {T : FlatSequence} (h : IsReflectionReal T) :
    IsReflectionReal (scaleFlat ha T) := by
  intro n f hf
  have he := scale_flip a (n := n+1) f.1
  change (fun x => flipConj f.1 (a • x)) = flipConj (fun x => f.1 (a • x)) at he
  have hm := scale_diagonal ha hf
  rw [he] at hm
  exact (congrArg (T.atSucc n) (Subtype.ext he)).trans (h n ⟨_, scale_diagonal ha f.2⟩ hm)

theorem scaleRaw_cast (a : ℝ) {p q : ℕ} (h : p = q) (f : FnOrScalar p) :
    scaleRaw a (h ▸ f : FnOrScalar q) = h ▸ scaleRaw a f := by subst q; rfl

theorem scale_tensor (a : ℝ) {p q : ℕ} (f : FnOrScalar p) (g : FnOrScalar q) :
    scaleRaw a (tensorAt f g) = tensorAt (scaleRaw a f) (scaleRaw a g) := by
  cases p with
  | zero =>
    change scaleRaw a ((Nat.zero_add q).symm ▸ smulAt (show ℂ from f) g) =
      (Nat.zero_add q).symm ▸ smulAt (show ℂ from f) (scaleRaw a g)
    rw [scaleRaw_cast]
    congr 1
    cases q <;> rfl
  | succ p => cases q <;> rfl

theorem scale_shift {a : ℝ} (ha : 0 < a) (w : AmbientSpace) {n : ℕ} (f : FnOrScalar n) :
    scaleRaw a (shiftActAt w f) = shiftActAt (a⁻¹ • w) (scaleRaw a f) := by
  cases n with
  | zero => rfl
  | succ n =>
    funext x
    change f (fun i => EuclidMotion.invMap (ConfigSpace.shiftMotion w) ((a • x) i)) =
      f (a • (fun i => EuclidMotion.invMap (ConfigSpace.shiftMotion (a⁻¹ • w)) (x i)))
    apply congrArg f
    funext i
    simp only [shiftMotion_invMap, Pi.smul_apply, smul_sub, smul_inv_smul₀ ha.ne']

theorem scale_eval {a : ℝ} (ha : 0 < a) (T : FlatSequence) {n : ℕ} (f : FnOrScalar n) :
    (scaleFlat ha T).evalAt f = T.evalAt (scaleRaw a f) := by
  by_cases h : f ∈ flatOffDiagonalAt n
  · rw [FlatSequence.evalAt_of_mem _ h, FlatSequence.evalAt_of_mem _ ((scale_flat_mem ha).mpr h)]
    rfl
  · simp only [FlatSequence.evalAt, dif_neg h, dif_neg ((scale_flat_mem ha).not.mpr h)]

def scalePosSeq {a : ℝ} (ha : 0 < a) (Φ : PosTimeSeq) : PosTimeSeq
  | 0 => Φ 0
  | n+1 => ⟨_, scale_posTime ha (Φ (n+1)).2⟩

theorem scalePosSeq_apply {a : ℝ} (ha : 0 < a) (Φ : PosTimeSeq) (n : ℕ) :
    (scalePosSeq ha Φ n).1 = scaleRaw a (Φ n).1 := by cases n <;> rfl

theorem scalePosSeq_finite {a : ℝ} (ha : 0 < a) {Φ : PosTimeSeq} (h : Φ.IsFinitelySupported) :
    (scalePosSeq ha Φ).IsFinitelySupported := by
  apply h.subset
  intro n hn hz
  apply hn
  rw [scalePosSeq_apply, hz]
  cases n <;> rfl

theorem scale_pairing {a : ℝ} (ha : 0 < a) (T : FlatSequence)
    (F G : (q : ℕ) → FnOrScalar q) :
    (scaleFlat ha T).reflectionPairing F G =
      T.reflectionPairing (fun q => scaleRaw a (F q)) (fun q => scaleRaw a (G q)) := by
  simp only [FlatSequence.reflectionPairing, scale_eval, scale_tensor, scale_flip]

theorem scale_osPositive {a : ℝ} (ha : 0 < a) {T : FlatSequence} (h : IsOSPositive T) :
    IsOSPositive (scaleFlat ha T) := by
  intro Φ hΦ
  simpa only [scale_pairing, scalePosSeq_apply] using h (scalePosSeq ha Φ) (scalePosSeq_finite ha hΦ)

theorem scale_cluster {a : ℝ} (ha : 0 < a) {T : FlatSequence} (h : HasClusterProperty T) :
    HasClusterProperty (scaleFlat ha T) := by
  intro Φ Ψ hΦ hΨ v hv hn
  have hv' : a⁻¹ • v ∈ zeroTimeHyperplane := by
    change a⁻¹ * v 3 = 0
    rw [show v 3 = 0 from hv, mul_zero]
  have hn' : a⁻¹ • v ≠ 0 := smul_ne_zero (inv_ne_zero ha.ne') hn
  have hc := h (scalePosSeq ha Φ) (scalePosSeq ha Ψ)
    (scalePosSeq_finite ha hΦ) (scalePosSeq_finite ha hΨ) _ hv' hn'
  simpa only [scale_pairing, scale_eval, scale_flip, scale_shift ha, scalePosSeq_apply,
    smul_comm a⁻¹] using hc

theorem scale_OS {a : ℝ} (ha : 0 < a) {D : SystemsWithFiveBounds.LimitConstants} (hd : D.Valid)
    {T : FlatSequence} (h : SystemsWithFiveBounds.OSAxioms D T) :
    SystemsWithFiveBounds.OSAxioms (scaleConstants a D) (scaleFlat ha T) :=
  ⟨scale_growth ha hd h.growth, scale_euclidInvariant ha h.euclidInv,
    scale_osPositive ha h.osPositive, scale_permSymmetric ha h.permSymm,
    scale_cluster ha h.cluster, scale_reflectionReal ha h.reality⟩


/-! ## The volume-first witness on the prescribed passing set -/

/-- The centred moments on an arbitrary sequence of original-mesh states.
This is the singleton-free partition argument of the release's volume-first export. -/
theorem volume_moments_tendsto {L : ℕ} (hL : Conventions.IsAdmissibleBlockingFactor L)
    (K : ℕ → ℕ+) (ν : CutoffStates L K) (hp : ∀ j, IsProbabilityMeasure (ν j))
    (S : CumulantFamily) (hc : ∀ n hn (X : TestSpaces.SepTupleOfCard n),
      Tendsto (fun j => InfiniteLattice.smearedEnergyCumulant (ν j) X.1) atTop (𝓝 (S n hn X : ℂ)))
    (n : ℕ) (X : TestSpaces.SepTupleOfCard n) :
    Tendsto (fun j => InfiniteLattice.centeredMoment (ν j) X.1) atTop
      (𝓝 (TestSpaces.centredOfCumulants S ⟨n, X⟩ : ℂ)) := by
  let s : Conventions.StandingParameters := ⟨L, hL, 1, 1⟩
  let f : AmbientPoints.separatedTuples s .euclidean n :=
    ⟨X.1, (AmbientPoints.mem_separatedTuples_r4_iff X.1).2 X.2⟩
  let T : AmbientPoints.TupleMapFamily s .euclidean :=
    fun k hk u => S k hk (AmbientPoints.toR4Tuple u)
  have he := AmbientPoints.centredOfMaps_r4 T S (fun _ _ _ => rfl) f
  change Tendsto _ atTop (𝓝 ((TestSpaces.centredOfCumulants S ⟨n, AmbientPoints.toR4Tuple f⟩ : ℝ) : ℂ))
  rw [← he]
  apply (CumulantLimits.CentredMoments.tendsto_sum_singletonFree T
    (fun j _ u => InfiniteLattice.smearedEnergyCumulant (ν j) u)
    (fun k hk u => hc k hk (AmbientPoints.toR4Tuple u)) f).congr
  intro j
  let st : Conventions.StandingParameters := ⟨L, hL, K j, 1⟩
  have hid := (gibbsState_centered_identity st _ (hp j)).2.2 n f.1
    (CumulantLimits.CentredMoments.apply_mem_compactTestFunctions f.2)
  exact (hid.trans (CumulantLimits.CentredMoments.ursellPartitionSum_eq_sum _ _)).symm

/-- The reference reading and the purity seed both stay at the prescribed
cutoffs. Only the continuum tests and the exponents of the large tori change. -/
theorem su2_fixed_observable_gap_of_infinite_passing :
    FixedObservableLimit (fun L M g₀ =>
      ∀ (ℓ : ℕ) (A : Set ℕ), 0 < ℓ → 1024 ∣ ℓ → A.Infinite → A ⊆ PurIo.passingCutoffs L M g₀ ℓ →
        ∃ K v ν S X₂ X₄, (∀ j, (K j : ℕ) ∈ A) ∧
          FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧
          HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S)) := by
  obtain ⟨L₀, head⟩ := PurIo.su2_fixed_observable_cutoffs_at_fixed_offset
  refine ⟨max L₀ 13, fun L hodd hlarge => ?_⟩
  have hL : Conventions.IsAdmissibleBlockingFactor L := ⟨hodd, (le_max_right ..).trans hlarge⟩
  obtain ⟨M, δ, hM, hδ, hroots, hsel⟩ := head L hodd ((le_max_left ..).trans hlarge)
  refine ⟨M, δ, hM, hδ, hroots, fun g₀ hg ℓ A hℓ hd hA hpass => ?_⟩
  obtain ⟨K, J, _, r, p, Bs, c₅, lam, CT, G, Nw, rfl, hc, hK, hJ, hmem, hadd, hroot, hfp, _,
    hgs, hbs⟩ := hsel g₀ hg A hA
  let L := p.side
  let β j := betaAt L M (K j) g₀
  have hβ j : 0 < β j := inv_pos.mpr (sq_pos_of_pos (hroot j).1.1)
  have h3 : 3 ≤ L := by have := hL.2; change 13 ≤ L at this; omega
  have hmono : StrictMono fun j => (J j : ℕ) := fun _ _ hij => hJ hij
  -- Export at the passage cutoffs using the bare couplings of the original cutoffs.
  obtain ⟨φ, m, μ, S, X₂, X₄, hφ, _, hμ, hm, _, hconv, _, hx₂, h₂, hx₄, h₄,
    ⟨D, T, hD, hT, hgr, heu, hos, hps, hr, hcum⟩, B, C, hC, hB, hcomp, hng⟩ :=
    su2_continuum_limit_of_frequent_passage os_axioms_for_components hL hc J β
      hmono.tendsto_atTop hβ (Frequently.of_forall hfp)
  obtain ⟨e, v, he, hv, hvtop⟩ := shift_volumes (by omega : 1 ≤ L) r (fun i => (m i : ℕ)) hm
  let t := φ ∘ e
  let K' := K ∘ t
  have ht : StrictMono t := hφ.comp he
  have ha := TestFunctions.PairTransport.meshSize_natCast_pos (by omega : 0 < L) r
  let S' := scaleFamily ha S
  -- Each inner volume limit uses all separated tests on its defining subsequence.
  choose ν hν hmatch using fun i => match_volume_state hL (J (t i)) (K' i) r
    (hadd (t i)) (hβ (t i)) (μ (e i)) (hμ (e i))
  have hi n hn (X : TestSpaces.SepTupleOfCard n) :
      Tendsto (fun i => InfiniteLattice.smearedEnergyCumulant (ν i) X.1) atTop (𝓝 (S' n hn X : ℂ)) :=
    ((hconv n hn (scaleTuple ha X)).2.1.comp he.tendsto_atTop).congr fun i =>
      ((hmatch i n hn X).trans (stateAtOffset_cumulant (by omega : 0 < L) (hadd (t i))
        (μ (e i)) (hμ (e i)).1 hn X)).symm
  have hf n hn (X : TestSpaces.SepTupleOfCard n) :
      Tendsto (fun i => SchwingerFunctions.connectedSchwingerR4 L (v i) (K' i) (β (t i)) X.1)
        atTop (𝓝 (S' n hn X : ℂ)) := by
    apply ((hconv n hn (scaleTuple ha X)).2.2.comp he.tendsto_atTop).congr
    intro i
    change SchwingerFunctions.connectedSchwingerR4 L (m (e i)) (J (t i)) (β (t i)) _ = _
    change _ = SchwingerFunctions.connectedSchwingerR4 L (v i) (K (t i)) (β (t i)) _
    rw [← hadd, ← hv]
    exact (torus_cumulant_at_offset h3 (v i) (J (t i)) r (β (t i)) X.1).symm
  -- Reassemble the release at the fine mesh before applying the purity estimate.
  have hw : FixedObservableWitnesses L M g₀ K' v ν S'
      (scaleTuple (inv_pos.mpr ha) X₂) (scaleTuple (inv_pos.mpr ha) X₄) := by
    refine ⟨hK.comp ht, fun i => hroot (t i), hgs.comp ht.tendsto_atTop, hν, hvtop,
      hbs.comp ht.tendsto_atTop, fun n hn X => ⟨?_, hi n hn X, hf n hn X⟩,
      fun n X => ⟨volume_moments_tendsto hL K' ν (fun i => (hν i).1) S' hi n X,
        su2_moments_tendsto hL (.of_forall fun i => (v i).pos) (.of_forall fun i => hβ (t i)) hf n X⟩,
      fun i => (hx₂ i).comp (contDiff_const_smul _), ?_,
      fun i => (hx₄ i).comp (contDiff_const_smul _), ?_, ?_, ?_⟩
    · obtain ⟨i, hs, hsep, Z, hZ⟩ := (hconv n hn X).1.exists
      filter_upwards [hvtop.eventually_ge_atTop (torusSide L (m i))] with j hj
      exact ⟨hs, hsep, Z, fun k => ⟨fun x hx y hy => ((hZ k).1 x hx y hy).trans
        (div_le_div_of_nonneg_right hj (by norm_num)), (hZ k).2⟩⟩
    · simpa only [S', scaleFamily, scaleTuple_inverse] using h₂
    · simpa only [S', scaleFamily, scaleTuple_inverse] using h₄
    · rw [show centredOf S' = scaleFunctional ha (centredOf S) from centred_scale ha S]
      exact ⟨scaleConstants (meshSize L (r : ℤ)) D, scaleFlat ha T, scaleConstants_valid hD,
        scale_representative ha hT, scale_growth ha hD hgr, scale_euclidInvariant ha heu,
        scale_osPositive ha hos, scale_permSymmetric ha hps, scale_reflectionReal ha hr,
        fun n hn X => (connected_scale ha _ X).trans (hcum n hn (scaleTuple ha X))⟩
    · rw [show centredOf S' = scaleFunctional ha (centredOf S) from centred_scale ha S]
      refine ⟨scaleDecomposition ha B, scaleConstants (meshSize L (r : ℤ)) C, scaleConstants_valid hC, canonical_scale ha hB,
        fun ξ => ?_, hng.mono fun _ h => nonGaussian_scale ha h⟩
      obtain ⟨U, hu, hos⟩ := hcomp ξ
      exact ⟨scaleFlat ha U, scale_representative ha hu, scale_OS ha hC hos⟩
  exact ⟨K', v, ν, S', _, _, fun i => hmem (t i), hw, Purity.massGap_of_purity hL hw.inputs
    ⟨hℓ, hd, Frequently.of_forall fun i => hpass (hmem (t i))⟩⟩


end GapChain.Offset

#print axioms GapChain.Offset.scaleTuple_inverse
#print axioms GapChain.Offset.torus_cumulant_at_offset
#print axioms GapChain.Offset.shift_volumes
#print axioms GapChain.Offset.mesh_at_offset
#print axioms GapChain.Offset.stateAtOffset_cumulant
#print axioms GapChain.Offset.match_volume_state
#print axioms GapChain.Offset.disjoint_scaled
#print axioms GapChain.Offset.disjointlySupported_scaled
#print axioms GapChain.Offset.functional_ext
#print axioms GapChain.Offset.scaleList_toList
#print axioms GapChain.Offset.centred_scale
#print axioms GapChain.Offset.connected_scale
#print axioms GapChain.Offset.nonGaussian_scale
#print axioms GapChain.Offset.scaleList_translate
#print axioms GapChain.Offset.scaleList_juxt
#print axioms GapChain.Offset.scale_shiftedJuxt
#print axioms GapChain.Offset.scale_shiftedComponents
#print axioms GapChain.Offset.scale_zip
#print axioms GapChain.Offset.scale_atInfinity
#print axioms GapChain.Offset.iterLimit_scale
#print axioms GapChain.Offset.canonical_scale
#print axioms GapChain.Offset.scaleCost_pos
#print axioms GapChain.Offset.scale_affine
#print axioms GapChain.Offset.scale_weight
#print axioms GapChain.Offset.scale_schwartz_bound
#print axioms GapChain.Offset.scale_flat_on_domain
#print axioms GapChain.Offset.scale_diagonal
#print axioms GapChain.Offset.scale_posTime
#print axioms GapChain.Offset.scale_flat_mem
#print axioms GapChain.Offset.scale_bracket
#print axioms GapChain.Offset.scaleConstants_valid
#print axioms GapChain.Offset.scale_growth
#print axioms GapChain.Offset.eval_sep_scale
#print axioms GapChain.Offset.scale_representative
#print axioms GapChain.Offset.scale_motion
#print axioms GapChain.Offset.scale_euclidInvariant
#print axioms GapChain.Offset.scale_permSymmetric
#print axioms GapChain.Offset.scale_flip
#print axioms GapChain.Offset.scale_reflectionReal
#print axioms GapChain.Offset.scaleRaw_cast
#print axioms GapChain.Offset.scale_tensor
#print axioms GapChain.Offset.scale_shift
#print axioms GapChain.Offset.scale_eval
#print axioms GapChain.Offset.scalePosSeq_apply
#print axioms GapChain.Offset.scalePosSeq_finite
#print axioms GapChain.Offset.scale_pairing
#print axioms GapChain.Offset.scale_osPositive
#print axioms GapChain.Offset.scale_cluster
#print axioms GapChain.Offset.scale_OS
#print axioms GapChain.Offset.volume_moments_tendsto
#print axioms GapChain.Offset.su2_fixed_observable_gap_of_infinite_passing
