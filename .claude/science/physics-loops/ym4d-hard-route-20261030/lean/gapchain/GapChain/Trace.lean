import GapChain.Transfer
import Mathlib.MeasureTheory.VectorMeasure.WithDensity
import Mathlib.MeasureTheory.Integral.Pi

/-!
# The cyclic integral of a square-integrable kernel

The product-space Hilbert basis gives the Hilbert–Schmidt pairing for arbitrary
probability spaces. Integrating out one vertex composes adjacent kernels.
The rectangular application follows the hand construction of rows 667 and 698
by Claude Opus 5.5. Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text, give the cubic transfer design in GL8.
-/

noncomputable section

open MeasureTheory Filter Set InnerProductSpace
open scoped ENNReal BigOperators InnerProductSpace ComplexConjugate

namespace GapChain.Kernel

variable {X : Type*} [MeasurableSpace X] {μ : Measure X} [IsProbabilityMeasure μ]
variable {k l : X × X → ℂ}

/-- A kernel is determined up to product-null sets by its operator, even on
a nonseparable space. Pairs of indicator functions test all rectangles. -/
theorem ae_eq_of_operator_eq (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ))
    (h : operator k hk = operator l hl) : k =ᵐ[μ.prod μ] l := by
  classical
  have hk' := hk.integrable (by norm_num : (1 : ℝ≥0∞) ≤ 2)
  have hl' := hl.integrable (by norm_num : (1 : ℝ≥0∞) ≤ 2)
  have rect (s t : Set X) (hs : MeasurableSet s) (ht : MeasurableSet t) :
      (μ.prod μ).withDensityᵥ k (s ×ˢ t) = (μ.prod μ).withDensityᵥ l (s ×ˢ t) := by
    let f := indicatorConstLp 2 hs (measure_ne_top μ s) (1 : ℂ)
    let g := indicatorConstLp 2 ht (measure_ne_top μ t) (1 : ℂ)
    have hf : ⇑f =ᵐ[μ] s.indicator (fun _ => (1 : ℂ)) := indicatorConstLp_coeFn
    have hg : ⇑g =ᵐ[μ] t.indicator (fun _ => (1 : ℂ)) := indicatorConstLp_coeFn
    have test (q : X × X → ℂ) (hq : MemLp q 2 (μ.prod μ)) :
        ⟪f, operator q hq g⟫_ℂ = ∫ z in s ×ˢ t, q z ∂μ.prod μ := by
      rw [pairing, ← integral_indicator (hs.prod ht)]
      apply integral_congr_ae
      filter_upwards [(measurePreserving_fst (μ := μ) (ν := μ)).quasiMeasurePreserving.ae hf,
        (measurePreserving_snd (μ := μ) (ν := μ)).quasiMeasurePreserving.ae hg] with z hx hy
      change f z.1 = _ at hx
      change g z.2 = _ at hy
      by_cases h₁ : z.1 ∈ s <;> by_cases h₂ : z.2 ∈ t <;>
        simp [hx, hy, Set.indicator, Set.mem_prod, h₁, h₂]
    rw [withDensityᵥ_apply hk' (hs.prod ht), withDensityᵥ_apply hl' (hs.prod ht),
      ← test k hk, ← test l hl, h]
  apply hk'.ae_eq_of_withDensityᵥ_eq hl'
  apply VectorMeasure.ext_of_generateFrom _ _ generateFrom_prod.symm isPiSystem_prod
  · simpa using rect univ univ .univ .univ
  · rintro _ ⟨s, hs, t, ht, rfl⟩
    exact rect s t hs ht

/-- The kernel of the rank-one map with output vector `f` and input test `g`. -/
def rankKernel (f g : Space μ) : Space (μ.prod μ) :=
  ((outer_memLp g f).comp_measurePreserving Measure.measurePreserving_swap).toLp _

theorem rankKernel_apply (f g : Space μ) :
    ⇑(rankKernel f g) =ᵐ[μ.prod μ] fun z => conj (g z.2) * f z.1 :=
  MemLp.coeFn_toLp _

theorem inner_rankKernel (f g : Space μ) (hk : MemLp k 2 (μ.prod μ)) :
    ⟪rankKernel f g, hk.toLp k⟫_ℂ = ⟪f, operator k hk g⟫_ℂ := by
  rw [L2.inner_def, pairing]
  apply integral_congr_ae
  filter_upwards [rankKernel_apply f g, hk.coeFn_toLp] with z h₁ h₂
  simp [h₁, h₂, mul_comm]

theorem inner_rankKernel_rankKernel (f g u v : Space μ) :
    ⟪rankKernel f g, rankKernel u v⟫_ℂ = ⟪f, u⟫_ℂ * ⟪v, g⟫_ℂ := by
  rw [L2.inner_def, L2.inner_def f u, L2.inner_def v g, ← integral_prod_mul]
  apply integral_congr_ae
  filter_upwards [rankKernel_apply f g, rankKernel_apply u v] with z h₁ h₂
  simp [h₁, h₂, mul_comm, mul_left_comm]

/-- Products of two basis vectors give a basis of product-space L².
The first index labels the input, the second the output. -/
theorem exists_kernel_basis {ι : Type*} (b : HilbertBasis ι ℂ (Space μ)) :
    ∃ c : HilbertBasis (ι × ι) ℂ (Space (μ.prod μ)),
      ∀ i, c i = rankKernel (b i.2) (b i.1) := by
  classical
  let v (i : ι × ι) := rankKernel (b i.2) (b i.1)
  have on : Orthonormal ℂ v := by
    rw [orthonormal_iff_ite]
    rintro ⟨i,j⟩ ⟨i',j'⟩
    simp only [v, inner_rankKernel_rankKernel, orthonormal_iff_ite.mp b.orthonormal]
    by_cases hi : i = i'
    · subst i'
      simp
    · simp [hi, Ne.symm hi]
  have total : (Submodule.span ℂ (range v))ᗮ = ⊥ := by
    apply le_antisymm _ bot_le
    intro q hq
    have coeff (i j : ι) :
        ⟪b j, operator (⇑q) (Lp.memLp q) (b i)⟫_ℂ = 0 := by
      rw [← inner_rankKernel, Lp.toLp_coeFn]
      exact hq _ (Submodule.subset_span ⟨(i,j), rfl⟩)
    have zero_on (i : ι) : operator (⇑q) (Lp.memLp q) (b i) = 0 := by
      apply b.repr.injective
      apply lp.ext
      funext j
      simpa [b.repr_apply_apply] using coeff i j
    have zero_op : operator (⇑q) (Lp.memLp q) = 0 := by
      ext x : 1
      have lim := (b.hasSum_repr x).mapL (operator (⇑q) (Lp.memLp q))
      simpa [map_smul, zero_on] using lim.tsum_eq.symm
    have zmem : MemLp (fun _ : X × X => (0 : ℂ)) 2 (μ.prod μ) := memLp_const (0 : ℂ)
    have zOp : operator (fun _ : X × X => (0 : ℂ)) zmem = 0 := by
      ext f : 1
      apply Lp.ext
      filter_upwards [operator_apply zmem f, Lp.coeFn_zero ℂ 2 μ] with x hx h₀
      change (operator _ zmem f) x = (0 : Space μ) x
      change (0 : Space μ) x = 0 at h₀
      simpa [h₀] using hx
    apply Lp.ext
    exact (ae_eq_of_operator_eq (Lp.memLp q) zmem (zero_op.trans zOp.symm)).trans
      (Lp.coeFn_zero ℂ 2 (μ.prod μ)).symm
  refine ⟨HilbertBasis.mkOfOrthogonalEqBot on total, ?_⟩
  intro i
  exact congrFun (HilbertBasis.coe_mkOfOrthogonalEqBot on total) i

/-- The Hilbert–Schmidt pairing is the ordinary product-space L² pairing.
Parseval on the product basis justifies summation even for uncountable bases. -/
theorem hasSum_hs_pairing {ι : Type*} (b : HilbertBasis ι ℂ (Space μ))
    (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    HasSum (fun i => ⟪operator k hk (b i), operator l hl (b i)⟫_ℂ)
      ⟪hk.toLp k, hl.toLp l⟫_ℂ := by
  obtain ⟨c, hc⟩ := exists_kernel_basis b
  have h := c.hasSum_inner_mul_inner (hk.toLp k) (hl.toLp l)
  have val (i) : ⟪hk.toLp k, c i⟫_ℂ = ⟪operator k hk (b i.1), b i.2⟫_ℂ := by
    rw [← inner_conj_symm, hc, inner_rankKernel, inner_conj_symm]
  simp_rw [val, hc, inner_rankKernel] at h
  exact h.prod_fiberwise fun i =>
    b.hasSum_inner_mul_inner (operator k hk (b i)) (operator l hl (b i))

end GapChain.Kernel

namespace GapChain.Kernel

variable {X : Type*} [MeasurableSpace X] {μ : Measure X} [IsProbabilityMeasure μ]
variable {k l : X × X → ℂ}

theorem row_apply_ae (hk : MemLp k 2 (μ.prod μ)) :
    ∀ᵐ x ∂μ, ⇑(row (μ := μ) k x) =ᵐ[μ] fun y => conj (k (x,y)) := by
  classical
  filter_upwards [sections hk] with x hx
  rw [row, dif_pos hx]
  exact hx.star.coeFn_toLp

/-- Integrate over the common endpoint of two edges. -/
def compose (μ : Measure X) (k l : X × X → ℂ) (z : X × X) : ℂ :=
  ∫ y, k (z.1,y) * l (y,z.2) ∂μ

theorem compose_measurable_ae (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    AEStronglyMeasurable (compose μ k l) (μ.prod μ) := by
  have p₁ : MeasurePreserving (fun p : (X × X) × X => (p.1.1,p.2)) ((μ.prod μ).prod μ)
      (μ.prod μ) := measurePreserving_fst.prod (MeasurePreserving.id μ)
  have p₂ : MeasurePreserving (fun p : (X × X) × X => (p.2,p.1.2)) ((μ.prod μ).prod μ)
      (μ.prod μ) := Measure.measurePreserving_swap.comp
        (measurePreserving_snd.prod (MeasurePreserving.id μ))
  exact ((hk.1.comp_quasiMeasurePreserving p₁.quasiMeasurePreserving).mul
    (hl.1.comp_quasiMeasurePreserving p₂.quasiMeasurePreserving)).integral_prod_right'

theorem compose_eq_inner (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    ∀ᵐ z ∂μ.prod μ, compose μ k l z = ⟪row (μ := μ) k z.1, row (adjKernel l) z.2⟫_ℂ := by
  filter_upwards [measurePreserving_fst.quasiMeasurePreserving.ae (row_inner hk),
    measurePreserving_snd.quasiMeasurePreserving.ae (row_apply_ae (adjKernel_memLp hl))]
    with z hkx hly
  rw [hkx]
  apply integral_congr_ae
  filter_upwards [hly] with a ha
  simp [ha, adjKernel]

theorem compose_memLp (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    MemLp (compose μ k l) 2 (μ.prod μ) := by
  have hm := compose_measurable_ae hk hl
  apply (memLp_two_iff_integrable_sq_norm hm).2
  apply ((integrable_row_norm_sq hk).mul_prod
    (integrable_row_norm_sq (adjKernel_memLp hl))).mono' (hm.norm.pow 2)
  filter_upwards [compose_eq_inner hk hl] with z hz
  change ‖‖compose μ k l z‖ ^ 2‖ ≤ ‖row (μ := μ) k z.1‖ ^ 2 * ‖row (μ := μ) (adjKernel l) z.2‖ ^ 2
  rw [Real.norm_of_nonneg (sq_nonneg _), hz, ← mul_pow]
  exact pow_le_pow_left₀ (norm_nonneg _) (norm_inner_le_norm _ _) _

theorem row_compose (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    ∀ᵐ x ∂μ, row (compose μ k l) x = (operator l hl).adjoint (row k x) := by
  filter_upwards [row_apply_ae (compose_memLp hk hl), row_apply_ae hk] with x hc hx
  apply Lp.ext
  rw [operator_adjoint]
  filter_upwards [hc, operator_apply (adjKernel_memLp hl) (row k x)] with z h₁ h₂
  rw [h₁, h₂, compose, ← integral_conj]
  apply integral_congr_ae
  filter_upwards [hx] with y hy
  simp [hy, adjKernel, mul_comm]

/-- Composition of two L² kernels represents the product of their operators. -/
theorem operator_compose (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    operator (compose μ k l) (compose_memLp hk hl) = operator k hk * operator l hl := by
  ext f : 1
  apply Lp.ext
  change ⇑(operator _ _ f) =ᵐ[μ] ⇑(operator k hk (operator l hl f))
  filter_upwards [(row_inner_memLp (compose_memLp hk hl) f).coeFn_toLp,
    (row_inner_memLp hk (operator l hl f)).coeFn_toLp, row_compose hk hl] with x h₁ h₂ he
  change (operator (compose μ k l) (compose_memLp hk hl) f) x = _ at h₁
  change (operator k hk (operator l hl f)) x = _ at h₂
  rw [h₁, h₂, he, ContinuousLinearMap.adjoint_inner_left]

end GapChain.Kernel

namespace GapChain.Kernel

variable {X : Type*} [MeasurableSpace X] {μ : Measure X} [IsProbabilityMeasure μ]
variable {k l : X × X → ℂ}

abbrev copies (μ : Measure X) (n : ℕ) := Measure.pi fun _ : Fin n => μ

/-- Two different vertices have product law, including on a two-vertex loop. -/
theorem evalPair_preserving {n : ℕ} (i j : Fin (n+1)) (hij : i ≠ j) :
    MeasurePreserving (fun u : Fin (n+1) → X => (u i,u j)) (copies μ (n+1)) (μ.prod μ) := by
  obtain ⟨a, rfl⟩ := Fin.exists_succAbove_eq hij.symm
  exact ((MeasurePreserving.id μ).prod (measurePreserving_eval (fun _ : Fin n => μ) a)).comp
    (measurePreserving_piFinSuccAbove (fun _ => μ) i)

def pathProduct (k : X × X → ℂ) {n : ℕ} (u : Fin (n+1) → X) : ℂ :=
  ∏ j : Fin n, k (u j.castSucc,u j.succ)

/-- A cycle with a distinguished closing edge. There are `n + 2` vertices. -/
def loopProduct (k l : X × X → ℂ) (n : ℕ) (u : Fin (n+2) → X) : ℂ :=
  pathProduct k u * l (u (Fin.last _), u 0)

omit [MeasurableSpace X] in
theorem loopProduct_zero (k l : X × X → ℂ) (u : Fin 2 → X) :
    loopProduct k l 0 u = k (u 0,u 1) * l (u 1,u 0) := by
  simp [loopProduct, pathProduct]

omit [MeasurableSpace X] in
theorem loopProduct_cons (k l : X × X → ℂ) (n : ℕ) (x : X) (u : Fin (n+2) → X) :
    loopProduct k l (n+1) (Fin.cons x u) =
      pathProduct k u * (l (u (Fin.last _),x) * k (x,u 0)) := by
  unfold loopProduct pathProduct
  rw [Fin.prod_univ_succ]
  change (k (x,u 0) * ∏ j : Fin (n+1), k (u j.castSucc,u j.succ)) *
    l (u (Fin.last _),x) = _
  ring

omit [MeasurableSpace X] in
theorem loopProduct_rotate (k : X × X → ℂ) (n : ℕ) (u : Fin (n+2) → X) :
    (∏ i, k (u i, u (finRotate (n+2) i))) = loopProduct k k n u := by
  rw [Fin.prod_univ_castSucc, finRotate_last]
  unfold loopProduct pathProduct
  congr 1
  apply Finset.prod_congr rfl
  intro i _
  rw [show finRotate (n+2) i.castSucc = i.succ from finRotate_of_lt i.isLt]

theorem loopProduct_aestronglyMeasurable (hk : MemLp k 2 (μ.prod μ))
    (hl : MemLp l 2 (μ.prod μ)) (n : ℕ) :
    AEStronglyMeasurable (loopProduct k l n) (copies μ (n+2)) := by
  apply AEStronglyMeasurable.mul
  · apply Finset.aestronglyMeasurable_fun_prod
    intro i _
    exact hk.1.comp_quasiMeasurePreserving
      (evalPair_preserving i.castSucc i.succ (by intro h; have := congrArg Fin.val h; simp at this)).quasiMeasurePreserving
  · exact hl.1.comp_quasiMeasurePreserving
      (evalPair_preserving (Fin.last (n+1)) 0 (by simp)).quasiMeasurePreserving

omit [IsProbabilityMeasure μ] in
/-- Each integrated vertex replaces its two incident edges by their composition. -/
theorem integral_vertex (k l : X × X → ℂ) (n : ℕ) (u : Fin (n+2) → X) :
    (∫ x, loopProduct k l (n+1) (Fin.cons x u) ∂μ) =
      loopProduct k (compose μ l k) n u := by
  simp only [loopProduct_cons, integral_const_mul]
  rfl

def absKernel (k : X × X → ℂ) (z : X × X) : ℂ := ‖k z‖

omit [MeasurableSpace X] in
theorem loopProduct_abs (k l : X × X → ℂ) (n : ℕ) (u : Fin (n+2) → X) :
    loopProduct (absKernel k) (absKernel l) n u = (‖loopProduct k l n u‖ : ℂ) := by
  simp [loopProduct, pathProduct, absKernel, norm_prod]

/-- This splitting map inserts the isolated vertex in position zero. -/
def prepend (n : ℕ) : X × (Fin n → X) ≃ᵐ (Fin (n+1) → X) :=
  (MeasurableEquiv.piFinSuccAbove (fun _ => X) 0).symm

theorem prepend_apply (n : ℕ) (p : X × (Fin n → X)) : prepend n p = Fin.cons p.1 p.2 := by
  simp [prepend, MeasurableEquiv.piFinSuccAbove_symm_apply, Fin.consEquiv]

theorem prepend_preserving (n : ℕ) :
    MeasurePreserving (prepend (X := X) n) (μ.prod (copies μ n)) (copies μ (n+1)) :=
  (measurePreserving_piFinSuccAbove (fun _ : Fin (n+1) => μ) 0).symm

/-- Absolute integrability for an arbitrary L² cycle. The induction uses
the same shorter cycle with both incident kernels replaced by their norms. -/
theorem integrable_loopProduct (n : ℕ) (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    Integrable (loopProduct k l n) (copies μ (n+2)) := by
  induction n generalizing k l with
  | zero =>
    simp_rw [show loopProduct k l 0 = fun u => k (u 0,u 1) * l (u 1,u 0) from funext (loopProduct_zero k l)]
    exact (measurePreserving_finTwoArrow μ).integrable_comp_of_integrable
      (hk.integrable_mul (hl.comp_measurePreserving Measure.measurePreserving_swap))
  | succ n ih =>
    let e := prepend (X := X) (n+2)
    have mp := prepend_preserving (μ := μ) (n+2)
    rw [← mp.integrable_comp_emb e.measurableEmbedding]
    apply (integrable_prod_iff' ((loopProduct_aestronglyMeasurable hk hl (n+1)).comp_quasiMeasurePreserving
      mp.quasiMeasurePreserving)).2
    constructor
    · have tr := hk.comp_measurePreserving Measure.measurePreserving_swap
      filter_upwards [(measurePreserving_eval (fun _ : Fin (n+2) => μ) (Fin.last _)).quasiMeasurePreserving.ae (sections hl),
        (measurePreserving_eval (fun _ : Fin (n+2) => μ) 0).quasiMeasurePreserving.ae (sections tr)] with u hu hv
      change MemLp (fun x => l (u (Fin.last _),x)) 2 μ at hu
      change MemLp (fun x => k (x,u 0)) 2 μ at hv
      have hi : Integrable (fun x => l (u (Fin.last _),x) * k (x,u 0)) μ := hu.integrable_mul hv
      simpa only [Function.comp_apply, prepend_apply, loopProduct_cons] using
        hi.const_mul (pathProduct k u)
    · have short := ih (k := absKernel k) (l := compose μ (absKernel l) (absKernel k))
        hk.norm.ofReal (compose_memLp hl.norm.ofReal hk.norm.ofReal)
      apply short.norm.congr
      apply ae_of_all
      intro u
      simp only [Function.comp_apply, prepend_apply]
      have hx := integral_vertex (μ := μ) (absKernel k) (absKernel l) n u
      simp only [loopProduct_abs, integral_complex_ofReal] at hx
      rw [← hx, Complex.norm_real, Real.norm_of_nonneg (integral_nonneg fun _ => norm_nonneg _)]

theorem integrable_cyclic (hk : MemLp k 2 (μ.prod μ)) {a : ℕ} (ha : 2 ≤ a) :
    Integrable (fun u : Fin a → X => ∏ t, k (u t,u (finRotate a t))) (copies μ a) := by
  obtain ⟨n,rfl⟩ : ∃ n, a = n+2 := ⟨a-2, by omega⟩
  simpa only [loopProduct_rotate] using integrable_loopProduct n hk hk

theorem integral_loopProduct_succ (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) (n : ℕ) :
    (∫ u, loopProduct k l (n+1) u ∂copies μ (n+3)) =
      ∫ u, loopProduct k (compose μ l k) n u ∂copies μ (n+2) := by
  have mp := prepend_preserving (μ := μ) (n+2)
  let F (p : X × (Fin (n+2) → X)) := loopProduct k l (n+1) (prepend (n+2) p)
  have hi : Integrable F (μ.prod (copies μ (n+2))) :=
    mp.integrable_comp_of_integrable (integrable_loopProduct (n+1) hk hl)
  rw [← mp.integral_comp']
  change (∫ p, F p ∂μ.prod (copies μ (n+2))) = _
  rw [integral_prod_symm F hi]
  apply integral_congr_ae
  exact ae_of_all _ fun u => by simp only [F, prepend_apply, integral_vertex]

/-- A trace formula for a cycle whose closing edge may be a different kernel.
It holds for any Hilbert basis and does not require positivity. -/
theorem hasSum_loopProduct {ι : Type*} (b : HilbertBasis ι ℂ (Space μ)) (n : ℕ)
    (hk : MemLp k 2 (μ.prod μ)) (hl : MemLp l 2 (μ.prod μ)) :
    HasSum (fun i => ⟪b i, (operator l hl * operator k hk ^ (n+1)) (b i)⟫_ℂ)
      (∫ u, loopProduct k l n u ∂copies μ (n+2)) := by
  induction n generalizing l with
  | zero =>
    have eqn : ⟪(adjKernel_memLp hl).toLp _, hk.toLp k⟫_ℂ =
        ∫ u, loopProduct k l 0 u ∂copies μ 2 := by
      rw [L2.inner_def]
      calc
        _ = ∫ z, k z * l z.swap ∂μ.prod μ := by
          apply integral_congr_ae
          filter_upwards [(adjKernel_memLp hl).coeFn_toLp, hk.coeFn_toLp] with z h₁ h₂
          simp [h₁, h₂, adjKernel]
        _ = _ := by
          rw [← (measurePreserving_finTwoArrow μ).integral_comp']
          apply integral_congr_ae
          exact ae_of_all _ fun u => (loopProduct_zero k l u).symm
    rw [← eqn]
    refine (hasSum_hs_pairing (k := adjKernel l) (l := k) b (adjKernel_memLp hl) hk).congr_fun fun i => ?_
    simpa only [zero_add, pow_one, mul_apply_eq_comp, operator_adjoint hl] using
      ((operator l hl).adjoint_inner_left (operator k hk (b i)) (b i)).symm
  | succ n ih =>
    rw [integral_loopProduct_succ hk hl]
    have h := ih (compose_memLp hl hk)
    rw [operator_compose hl hk] at h
    simpa only [mul_assoc, ← pow_succ'] using h

end GapChain.Kernel

namespace GapChain

open Module.End Wilson

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Extend one orthonormal basis per positive eigenvalue to a Hilbert basis.
The operator vanishes on every added vector, including in nonseparable spaces. -/
theorem exists_positive_slot_basis (T : H →L[ℂ] H) (hc : IsCompactOperator T)
    (hp : T.IsPositive) :
    ∃ (w : Set H) (b : HilbertBasis w ℂ H) (j : PositiveSlot T → w),
      Function.Injective j ∧
      (∀ i, T (b (j i)) = (i.1.val : ℂ) • b (j i)) ∧
      ∀ p, p ∉ range j → T (b p) = 0 := by
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
  obtain ⟨w,b,inc,hb⟩ := on.toSubtypeRange.exists_hilbertBasis_extension
  let j (i : PositiveSlot T) : w := ⟨v i, inc ⟨i,rfl⟩⟩
  have bj (i) : b (j i) = v i := congrFun hb _
  refine ⟨w,b,j, fun _ _ h => on.linearIndependent.injective (congrArg Subtype.val h), ?_, ?_⟩
  · intro i
    rw [bj]
    exact mem_eigenspace_iff.mp (basis i.1 i.2).property
  · intro p hnot
    have hperp (i : PositiveSlot T) : ⟪b p, v i⟫_ℂ = 0 := by
      rw [← bj]
      exact b.orthonormal.inner_eq_zero (fun h => hnot ⟨i,h.symm⟩)
    have hmem : T (b p) ∈ (⨆ c : ℂ, eigenspace T.toLinearMap c)ᗮ := by
      rw [← Submodule.iInf_orthogonal, Submodule.mem_iInf]
      intro c
      rw [Submodule.mem_orthogonal']
      intro y hy
      rw [hp.isSymmetric.apply_clm, show T y = c • y from mem_eigenspace_iff.mp hy, inner_smul_right]
      by_cases hc₀ : c = 0
      · simp [hc₀]
      by_cases hy₀ : y = 0
      · simp [hy₀]
      obtain ⟨i,hi⟩ := nonzero_eigenvalue_has_slot T hc hp hc₀
        (hasEigenvalue_of_hasEigenvector ⟨hy,hy₀⟩)
      subst c
      let F := (innerSL ℂ (b p)).comp (eigenspace T.toLinearMap (z i.1)).subtypeL
      have hF (q) : F (basis i.1 q) = 0 := hperp ⟨i.1,q⟩
      have hf : F ⟨y,hy⟩ = 0 := by
        rw [← (basis i.1).sum_repr ⟨y,hy⟩, map_sum]
        simp only [map_smul, hF, smul_zero, Finset.sum_const_zero]
      exact mul_eq_zero_of_right _ hf
    rwa [ContinuousLinearMap.orthogonalComplement_iSup_eigenspaces_eq_bot hc hp.isSymmetric,
      Submodule.mem_bot] at hmem

omit [CompleteSpace H] in
theorem pow_apply_eigenvector (T : H →L[ℂ] H) {v : H} {c : ℂ} (hv : T v = c • v) (a : ℕ) :
    (T ^ a) v = c ^ a • v := by
  induction a with
  | zero => simp
  | succ a ih =>
    rw [pow_succ', mul_apply_eq_comp, ih, map_smul, hv, smul_smul, pow_succ]

namespace Kernel

variable {X : Type*} [MeasurableSpace X] {μ : Measure X} [IsProbabilityMeasure μ]
variable {k : X × X → ℂ}

/-- The oriented cyclic integral of a positive L² kernel is the spectral
power sum counted with multiplicity, for every length at least two. -/
theorem hasSum_cyclic (hk : MemLp k 2 (μ.prod μ)) (hp : (operator k hk).IsPositive)
    {a : ℕ} (ha : 2 ≤ a) :
    HasSum (fun i : PositiveSlot (operator k hk) => ((i.1.val ^ a : ℝ) : ℂ))
      (∫ u : Fin a → X, ∏ t, k (u t, u (finRotate a t)) ∂copies μ a) := by
  obtain ⟨n,rfl⟩ : ∃ n, a = n+2 := ⟨a-2, by omega⟩
  let T := operator k hk
  obtain ⟨w,b,j,hj,he,h₀⟩ := exists_positive_slot_basis T (operator_compact hk) hp
  have tr : HasSum (fun p => ⟪b p, (T ^ (n+2)) (b p)⟫_ℂ)
      (∫ u, loopProduct k k n u ∂copies μ (n+2)) := by
    simpa only [T, ← pow_succ'] using hasSum_loopProduct b n hk hk
  have outside (p : w) (h : p ∉ range j) : ⟪b p, (T ^ (n+2)) (b p)⟫_ℂ = 0 := by
    rw [pow_succ, mul_apply_eq_comp, h₀ p h, map_zero, inner_zero_right]
  have hjtr := (hj.hasSum_iff outside).2 tr
  have term (i : PositiveSlot T) : ⟪b (j i), (T ^ (n+2)) (b (j i))⟫_ℂ =
      ((i.1.val ^ (n+2) : ℝ) : ℂ) := by
    rw [pow_apply_eigenvector T (he i), inner_smul_right, inner_self_eq_one_of_norm_eq_one (b.orthonormal.norm_eq_one _),
      mul_one, Complex.ofReal_pow]
  have slots : HasSum (fun i : PositiveSlot T => ((i.1.val ^ (n+2) : ℝ) : ℂ))
      (∫ u, loopProduct k k n u ∂copies μ (n+2)) :=
    hjtr.congr_fun fun i => (term i).symm
  simpa only [loopProduct_rotate] using slots

theorem cyclic_eq_tsum (hk : MemLp k 2 (μ.prod μ)) (hp : (operator k hk).IsPositive)
    {a : ℕ} (ha : 2 ≤ a) :
    (∫ u : Fin a → X, ∏ t, k (u t, u (finRotate a t)) ∂copies μ a) =
      ((∑' i : PositiveSlot (operator k hk), i.1.val ^ a : ℝ) : ℂ) ∧
      Summable (fun i : PositiveSlot (operator k hk) => i.1.val ^ a) := by
  have h := hasSum_cyclic hk hp ha
  refine ⟨(h.tsum_eq.symm.trans (Complex.ofReal_tsum _).symm), ?_⟩
  simpa only [Complex.reCLM_apply, Complex.ofReal_re] using (h.mapL Complex.reCLM).summable

end Kernel
end GapChain

namespace GapChain.Wilson.Trace

def cyclic (β : ℝ) (R : Box) (a : ℕ) : ℝ :=
  ∫ u : Fin a → Slice R, ∏ t : Fin a, transferKernel β R (u t, u (finRotate a t))
    ∂(Measure.pi fun _ => sliceHaar R)

end GapChain.Wilson.Trace

namespace GapChain.Wilson.Trace

/-- The series of positive spectral slots sums to the actual real Haar integral. -/
theorem cyclic_hasSum {β : ℝ} (hβ : 0 ≤ β) (R : Box) {a : ℕ} (ha : 2 ≤ a) :
    HasSum (fun i : PositiveSlot (transfer β R) => i.1.val ^ a) (cyclic β R a) := by
  have hp : (Kernel.operator _ (transferKernel_memLp β R)).IsPositive := transfer_positive hβ R
  have h := Kernel.hasSum_cyclic (transferKernel_memLp β R) hp ha
  rw [show transfer β R = Kernel.operator _ (transferKernel_memLp β R) from rfl]
  apply Complex.hasSum_ofReal.mp
  simpa only [cyclic, Kernel.copies, ← Complex.ofReal_prod, integral_complex_ofReal] using h

/-- The weight consumed by Stage 1 on each valid rectangular box. -/
theorem cyclic_eq_tsum {β : ℝ} (hβ : 0 < β) (R : Box) (_hR : R.Valid) {a : ℕ} (ha : 3 ≤ a) :
    cyclic β R a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a :=
  (cyclic_hasSum hβ.le R (by omega : 2 ≤ a)).tsum_eq.symm

theorem summable_pow {β : ℝ} (hβ : 0 ≤ β) (R : Box) {a : ℕ} (ha : 2 ≤ a) :
    Summable (fun i : PositiveSlot (transfer β R) => i.1.val ^ a) :=
  (cyclic_hasSum hβ R ha).summable

end GapChain.Wilson.Trace

#print axioms GapChain.Kernel.ae_eq_of_operator_eq
#print axioms GapChain.Kernel.rankKernel_apply
#print axioms GapChain.Kernel.inner_rankKernel
#print axioms GapChain.Kernel.inner_rankKernel_rankKernel
#print axioms GapChain.Kernel.exists_kernel_basis
#print axioms GapChain.Kernel.hasSum_hs_pairing
#print axioms GapChain.Kernel.row_apply_ae
#print axioms GapChain.Kernel.compose_measurable_ae
#print axioms GapChain.Kernel.compose_eq_inner
#print axioms GapChain.Kernel.compose_memLp
#print axioms GapChain.Kernel.row_compose
#print axioms GapChain.Kernel.operator_compose
#print axioms GapChain.Kernel.evalPair_preserving
#print axioms GapChain.Kernel.loopProduct_zero
#print axioms GapChain.Kernel.loopProduct_cons
#print axioms GapChain.Kernel.loopProduct_rotate
#print axioms GapChain.Kernel.loopProduct_aestronglyMeasurable
#print axioms GapChain.Kernel.integral_vertex
#print axioms GapChain.Kernel.loopProduct_abs
#print axioms GapChain.Kernel.prepend_apply
#print axioms GapChain.Kernel.prepend_preserving
#print axioms GapChain.Kernel.integrable_loopProduct
#print axioms GapChain.Kernel.integrable_cyclic
#print axioms GapChain.Kernel.integral_loopProduct_succ
#print axioms GapChain.Kernel.hasSum_loopProduct
#print axioms GapChain.exists_positive_slot_basis
#print axioms GapChain.pow_apply_eigenvector
#print axioms GapChain.Kernel.hasSum_cyclic
#print axioms GapChain.Kernel.cyclic_eq_tsum
#print axioms GapChain.Wilson.Trace.cyclic_hasSum
#print axioms GapChain.Wilson.Trace.cyclic_eq_tsum
#print axioms GapChain.Wilson.Trace.summable_pow
