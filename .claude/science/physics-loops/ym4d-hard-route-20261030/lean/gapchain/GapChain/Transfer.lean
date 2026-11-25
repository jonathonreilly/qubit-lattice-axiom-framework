import GapChain.Wilson
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.MeasureTheory.Integral.Prod

/-!
# Integral operators and the rectangular Wilson transfer kernel

The finite-family bound follows row 667, Lemma A0, by applying Bessel's
inequality to the conjugate of each kernel section. The Wilson conventions
are those of row 698, Lemma 1.1, and of Ethan Sussman and Levent Alpoge,
with Claude and Codex, in their cubic transfer construction (GL8).
-/

noncomputable section

open MeasureTheory Filter Set InnerProductSpace
open scoped BigOperators InnerProductSpace ComplexConjugate

namespace GapChain.Kernel

variable {X : Type*} [MeasurableSpace X] {μ : Measure X}

abbrev Space (μ : Measure X) := Lp ℂ 2 μ

/-- The norm of an L² class expressed using its canonical representative. -/
theorem norm_sq (f : Space μ) : ‖f‖ ^ 2 = ∫ x, ‖f x‖ ^ 2 ∂μ := by
  calc
    ‖f‖ ^ 2 = RCLike.re ⟪f, f⟫_ℂ := (inner_self_eq_norm_sq (𝕜 := ℂ) f).symm
    _ = ∫ x, RCLike.re ⟪f x, f x⟫_ℂ ∂μ := (integral_re (L2.integrable_inner (𝕜 := ℂ) f f)).symm
    _ = _ := integral_congr_ae (ae_of_all _ fun x => inner_self_eq_norm_sq (𝕜 := ℂ) (f x))

theorem norm_sq_toLp {f : X → ℂ} (hf : MemLp f 2 μ) :
    ‖hf.toLp f‖ ^ 2 = ∫ x, ‖f x‖ ^ 2 ∂μ := by
  rw [norm_sq]
  exact integral_congr_ae (hf.coeFn_toLp.fun_comp fun z => ‖z‖ ^ 2)

/-- Row vector representing evaluation of the integral against an L² input.
The zero value outside the good sections fixes an irrelevant null set. -/
def row (k : X × X → ℂ) (x : X) : Space μ := by
  classical
  exact if h : MemLp (fun y => k (x,y)) 2 μ then h.star.toLp _ else 0

variable [IsProbabilityMeasure μ] {k : X × X → ℂ}

theorem sections (hk : MemLp k 2 (μ.prod μ)) :
    ∀ᵐ x ∂μ, MemLp (fun y => k (x,y)) 2 μ := by
  filter_upwards [hk.1.prodMk_left, hk.norm.integrable_sq.prod_right_ae] with x hm hi
  exact (memLp_two_iff_integrable_sq_norm hm).2 hi

theorem row_inner (hk : MemLp k 2 (μ.prod μ)) :
    ∀ᵐ x ∂μ, ∀ f : Space μ,
      ⟪row k x, f⟫_ℂ = ∫ y, k (x,y) * f y ∂μ := by
  classical
  filter_upwards [sections hk] with x hx
  intro f
  rw [row, dif_pos hx, L2.inner_def]
  apply integral_congr_ae
  filter_upwards [hx.star.coeFn_toLp] with y hy
  simp [hy, mul_comm]

theorem row_norm_sq (hk : MemLp k 2 (μ.prod μ)) :
    ∀ᵐ x ∂μ, ‖row (μ := μ) k x‖ ^ 2 = ∫ y, ‖k (x,y)‖ ^ 2 ∂μ := by
  classical
  filter_upwards [sections hk] with x hx
  rw [row, dif_pos hx, norm_sq_toLp]
  simp

theorem integrable_row_norm_sq (hk : MemLp k 2 (μ.prod μ)) :
    Integrable (fun x => ‖row (μ := μ) k x‖ ^ 2) μ :=
  hk.norm.integrable_sq.integral_prod_left.congr ((row_norm_sq hk).mono fun _ hx => hx.symm)

theorem integral_row_norm_sq (hk : MemLp k 2 (μ.prod μ)) :
    (∫ x, ‖row (μ := μ) k x‖ ^ 2 ∂μ) = ‖hk.toLp k‖ ^ 2 := by
  rw [norm_sq_toLp, integral_prod _ hk.norm.integrable_sq]
  exact integral_congr_ae (row_norm_sq hk)

theorem row_inner_memLp (hk : MemLp k 2 (μ.prod μ)) (f : Space μ) :
    MemLp (fun x => ⟪row k x, f⟫_ℂ) 2 μ := by
  have hm : AEStronglyMeasurable (fun x => ⟪row k x, f⟫_ℂ) μ :=
    ((hk.1.mul (Lp.aestronglyMeasurable f).comp_snd).integral_prod_right').congr
      ((row_inner hk).mono fun x hx => (hx f).symm)
  apply (memLp_two_iff_integrable_sq_norm hm).2
  apply ((integrable_row_norm_sq hk).mul_const (‖f‖ ^ 2)).mono' (hm.norm.pow 2)
  filter_upwards [] with x
  change ‖‖⟪row k x, f⟫_ℂ‖ ^ 2‖ ≤ ‖row k x‖ ^ 2 * ‖f‖ ^ 2
  rw [Real.norm_of_nonneg (sq_nonneg _), ← mul_pow]
  exact pow_le_pow_left₀ (norm_nonneg _) (norm_inner_le_norm _ _) 2

theorem row_bound (hk : MemLp k 2 (μ.prod μ)) (f : Space μ) :
    ‖(row_inner_memLp hk f).toLp _‖ ≤ ‖hk.toLp k‖ * ‖f‖ := by
  apply le_of_sq_le_sq _ (by positivity)
  rw [norm_sq_toLp, mul_pow, ← integral_row_norm_sq hk, ← integral_mul_const]
  apply integral_mono ((row_inner_memLp hk f).norm.integrable_sq)
    ((integrable_row_norm_sq hk).mul_const _)
  intro x
  change ‖⟪row k x, f⟫_ℂ‖ ^ 2 ≤ ‖row k x‖ ^ 2 * ‖f‖ ^ 2
  rw [← mul_pow]
  exact pow_le_pow_left₀ (norm_nonneg _) (norm_inner_le_norm _ _) 2

/-- The bounded operator of a scalar square-integrable kernel on a probability space. -/
def operator (k : X × X → ℂ) (hk : MemLp k 2 (μ.prod μ)) : Space μ →L[ℂ] Space μ := by
  let A : Space μ →ₗ[ℂ] Space μ :=
    { toFun := fun f => (row_inner_memLp hk f).toLp _
      map_add' := fun f g => by
        apply Lp.ext
        filter_upwards [(row_inner_memLp hk (f + g)).coeFn_toLp,
          Lp.coeFn_add ((row_inner_memLp hk f).toLp _) ((row_inner_memLp hk g).toLp _),
          (row_inner_memLp hk f).coeFn_toLp, (row_inner_memLp hk g).coeFn_toLp] with x h₁ h₂ h₃ h₄
        rw [h₁, h₂, Pi.add_apply, h₃, h₄, inner_add_right]
      map_smul' := fun c f => by
        apply Lp.ext
        filter_upwards [(row_inner_memLp hk (c • f)).coeFn_toLp,
          Lp.coeFn_smul c ((row_inner_memLp hk f).toLp _),
          (row_inner_memLp hk f).coeFn_toLp] with x h₁ h₂ h₃
        rw [RingHom.id_apply, h₁, h₂, Pi.smul_apply, h₃, smul_eq_mul, inner_smul_right] }
  exact A.mkContinuous ‖hk.toLp k‖ (row_bound hk)

theorem operator_norm_le (hk : MemLp k 2 (μ.prod μ)) : ‖operator k hk‖ ≤ ‖hk.toLp k‖ :=
  (operator k hk).opNorm_le_bound (norm_nonneg _) (row_bound hk)

/-- For each L² input, the output class is represented by the ordinary row integral. -/
theorem operator_apply (hk : MemLp k 2 (μ.prod μ)) (f : Space μ) :
    ⇑(operator k hk f) =ᵐ[μ] fun x => ∫ y, k (x,y) * f y ∂μ :=
  (row_inner_memLp hk f).coeFn_toLp.trans ((row_inner hk).mono fun _ hx => hx f)

theorem operator_congr {l : X × X → ℂ} (hk : MemLp k 2 (μ.prod μ))
    (hl : MemLp l 2 (μ.prod μ)) (h : k =ᵐ[μ.prod μ] l) : operator k hk = operator l hl := by
  ext f : 1
  apply Lp.ext
  filter_upwards [operator_apply hk f, operator_apply hl f, Measure.ae_ae_of_ae_prod h] with x hx hy he
  rw [hx, hy]
  apply integral_congr_ae
  filter_upwards [he] with y hy
  rw [hy]

/-- The Hilbert–Schmidt bound uses the full product L² norm, on arbitrary
finite orthonormal families, including on nonseparable spaces. -/
theorem operator_hs (hk : MemLp k 2 (μ.prod μ)) :
    HSNormLE (operator k hk) ‖hk.toLp k‖ := by
  intro n v hv
  calc
    ∑ i, ‖operator k hk (v i)‖ ^ 2 =
        ∑ i, ∫ x, ‖⟪row k x, v i⟫_ℂ‖ ^ 2 ∂μ :=
      Finset.sum_congr rfl fun i _ => norm_sq_toLp (row_inner_memLp hk (v i))
    _ = ∫ x, ∑ i, ‖⟪row k x, v i⟫_ℂ‖ ^ 2 ∂μ :=
      (integral_finsetSum _ fun i _ => (row_inner_memLp hk (v i)).norm.integrable_sq).symm
    _ ≤ ∫ x, ‖row (μ := μ) k x‖ ^ 2 ∂μ := by
      apply integral_mono (integrable_finsetSum _ fun i _ =>
        (row_inner_memLp hk (v i)).norm.integrable_sq) (integrable_row_norm_sq hk)
      intro x
      simpa only [norm_inner_symm (row k x)] using
        (hv.sum_inner_products_le (s := Finset.univ) (row k x))
    _ = ‖hk.toLp k‖ ^ 2 := integral_row_norm_sq hk

end GapChain.Kernel

namespace GapChain.Kernel

variable {X : Type*} [MeasurableSpace X] {μ : Measure X} [IsProbabilityMeasure μ]
variable {k : X × X → ℂ}

omit [IsProbabilityMeasure μ] in
theorem outer_memLp (g f : Space μ) :
    MemLp (fun z : X × X => conj (g z.1) * f z.2) 2 (μ.prod μ) := by
  apply (memLp_two_iff_integrable_sq_norm
    ((Lp.aestronglyMeasurable g).star.comp_fst.mul (Lp.aestronglyMeasurable f).comp_snd)).2
  change Integrable (fun z : X × X => ‖conj (g z.1) * f z.2‖ ^ 2) (μ.prod μ)
  simpa only [norm_mul, mul_pow, Complex.norm_conj] using
    (Lp.memLp g).norm.integrable_sq.mul_prod (Lp.memLp f).norm.integrable_sq

/-- The product-space pairing, with the conjugation on the test function. -/
theorem pairing (hk : MemLp k 2 (μ.prod μ)) (g f : Space μ) :
    ⟪g, operator k hk f⟫_ℂ = ∫ z, k z * (conj (g z.1) * f z.2) ∂μ.prod μ := by
  rw [L2.inner_def, integral_prod (fun z : X × X => k z * (conj (g z.1) * f z.2))
    (hk.integrable_mul (outer_memLp g f))]
  apply integral_congr_ae
  filter_upwards [operator_apply hk f] with x hx
  rw [RCLike.inner_apply', hx, ← integral_const_mul]
  exact integral_congr_ae (ae_of_all _ fun y => by ring)

def adjKernel (k : X × X → ℂ) (z : X × X) : ℂ := conj (k z.swap)

theorem adjKernel_memLp (hk : MemLp k 2 (μ.prod μ)) :
    MemLp (adjKernel k) 2 (μ.prod μ) :=
  (hk.comp_measurePreserving Measure.measurePreserving_swap).star

/-- The adjoint kernel is the conjugate transpose, modulo product null sets. -/
theorem operator_adjoint (hk : MemLp k 2 (μ.prod μ)) :
    (operator k hk).adjoint = operator (adjKernel k) (adjKernel_memLp hk) := by
  symm
  apply (ContinuousLinearMap.eq_adjoint_iff _ _).2
  intro f g
  rw [← inner_conj_symm, pairing (adjKernel_memLp hk), pairing hk, ← integral_conj]
  rw [← integral_prod_swap (fun z => k z * (conj (f z.1) * g z.2))]
  apply integral_congr_ae
  exact ae_of_all _ fun z => by simp [adjKernel, mul_comm, mul_left_comm, mul_assoc]

theorem operator_selfAdjoint (hk : MemLp k 2 (μ.prod μ))
    (hs : adjKernel k =ᵐ[μ.prod μ] k) : IsSelfAdjoint (operator k hk) :=
  (operator_adjoint hk).trans (operator_congr (adjKernel_memLp hk) hk hs)

end GapChain.Kernel

namespace GapChain

/-- A finite-family Hilbert–Schmidt bound implies compactness. Truncating the
input Fourier expansion controls the operator-norm error by the square root
of the remaining Hilbert–Schmidt mass. -/
theorem HSNormLE.isCompact {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    [CompleteSpace H] {T : H →L[ℂ] H} {δ : ℝ} (hs : HSNormLE T δ) : IsCompactOperator T := by
  classical
  obtain ⟨ι, b, _⟩ := exists_hilbertBasis ℂ H
  let mass (i : ι) := ‖T (b i)‖ ^ 2
  have summ : Summable mass :=
    summable_of_sum_le (fun i => sq_nonneg _) (fun s => hs.sum_le b s)
  let F (s : Finset ι) := ∑ i ∈ s, rankOne ℂ (T (b i)) (b i)
  have eval (s : Finset ι) (x : H) : F s x = ∑ i ∈ s, b.repr x i • T (b i) := by
    simp [F, b.repr_apply_apply]
  let tail (s : Finset ι) := (∑' i, mass i) - ∑ i ∈ s, mass i
  have err (s : Finset ι) : ‖F s - T‖ ≤ √(tail s) := by
    apply ContinuousLinearMap.opNorm_le_bound _ (Real.sqrt_nonneg _)
    intro x
    have lim : HasSum (fun i => b.repr x i • T (b i)) (T x) := by
      simpa only [map_smul] using (b.hasSum_repr x).mapL T
    change ‖F s x - T x‖ ≤ _
    rw [norm_sub_rev, eval]
    apply le_of_tendsto ((lim.sub_const (∑ i ∈ s, b.repr x i • T (b i))).norm)
    filter_upwards [eventually_ge_atTop s] with t ht
    rw [← Finset.sum_sdiff ht, add_sub_cancel_right]
    calc
      ‖∑ i ∈ t \ s, b.repr x i • T (b i)‖ ≤
          ∑ i ∈ t \ s, ‖T (b i)‖ * ‖b.repr x i‖ := by
        simpa only [norm_smul, mul_comm] using
          (norm_sum_le (t \ s) (fun i => b.repr x i • T (b i)))
      _ ≤ √(∑ i ∈ t \ s, mass i) * √(∑ i ∈ t \ s, ‖b.repr x i‖ ^ 2) :=
        Real.sum_mul_le_sqrt_mul_sqrt _ _ _
      _ ≤ √(tail s) * ‖x‖ := by
        apply mul_le_mul _ _ (Real.sqrt_nonneg _) (Real.sqrt_nonneg _)
        · apply Real.sqrt_le_sqrt
          change _ ≤ _ - _
          rw [le_sub_iff_add_le, Finset.sum_sdiff ht]
          exact summ.sum_le_tsum t (fun i _ => sq_nonneg _)
        · rw [← Real.sqrt_sq (norm_nonneg x)]
          apply Real.sqrt_le_sqrt
          simpa only [b.repr_apply_apply] using
            (b.orthonormal.sum_inner_products_le (s := t \ s) x)
  have ht : Tendsto (fun s => √(tail s)) atTop (nhds 0) := by
    have htail : Tendsto tail atTop (nhds ((∑' i, mass i) - ∑' i, mass i)) :=
      tendsto_const_nhds.sub summ.hasSum
    simpa only [sub_self, Real.sqrt_zero] using htail.sqrt
  apply isCompactOperator_of_tendsto (tendsto_iff_norm_sub_tendsto_zero.mpr
    (squeeze_zero (fun _ => norm_nonneg _) err ht))
  apply Eventually.of_forall
  intro s
  induction s using Finset.induction_on with
  | empty => simpa [F] using (isCompactOperator_zero : IsCompactOperator (0 : H →L[ℂ] H))
  | insert i s hi ih =>
    have hr : IsCompactOperator (rankOne ℂ (T (b i)) (b i)) := by
      rw [rankOne_def']
      exact (isCompactOperator_of_locallyCompactSpace_dom (innerSL ℂ (b i))).clm_comp
        (ContinuousLinearMap.toSpanSingleton ℂ (T (b i)))
    rw [show F (insert i s) = rankOne ℂ (T (b i)) (b i) + F s by simp [F, hi]]
    exact hr.add ih

namespace Kernel

theorem operator_compact {X : Type*} [MeasurableSpace X] {μ : Measure X} [IsProbabilityMeasure μ]
    {k : X × X → ℂ} (hk : MemLp k 2 (μ.prod μ)) : IsCompactOperator (operator k hk) :=
  (operator_hs hk).isCompact

end Kernel
end GapChain

namespace GapChain.Kernel

variable {X : Type*} [TopologicalSpace X] [CompactSpace X]
  [MeasurableSpace X] [BorelSpace X] [SecondCountableTopology X]
variable (μ : Measure X) [IsProbabilityMeasure μ]

/-- Real continuous kernels act on complex L². Uniform convergence of such
kernels entails operator-norm convergence. -/
def realOperator : C(X × X, ℝ) →L[ℝ] (Space μ →L[ℂ] Space μ) := by
  let hm (q : C(X × X, ℝ)) : MemLp (fun z => (q z : ℂ)) 2 (μ.prod μ) :=
    (Complex.continuous_ofReal.comp q.continuous).memLp_of_hasCompactSupport
      (HasCompactSupport.of_compactSpace _)
  let A : C(X × X, ℝ) →ₗ[ℝ] (Space μ →L[ℂ] Space μ) :=
    { toFun := fun q => operator _ (hm q)
      map_add' := fun q r => by
        ext f : 1
        apply Lp.ext
        filter_upwards [operator_apply (hm (q+r)) f, operator_apply (hm q) f,
          operator_apply (hm r) f, Lp.coeFn_add (operator _ (hm q) f) (operator _ (hm r) f),
          sections (hm q), sections (hm r)] with x ha hq hr he iq ir
        rw [_root_.add_apply, ha, he, Pi.add_apply, hq, hr]
        rw [← integral_add (f := fun y => (q (x,y) : ℂ) * f y)
          (g := fun y => (r (x,y) : ℂ) * f y) (iq.integrable_mul (Lp.memLp f))
          (ir.integrable_mul (Lp.memLp f))]
        exact integral_congr_ae (ae_of_all _ fun y => by simp [add_mul])
      map_smul' := fun c q => by
        ext f : 1
        apply Lp.ext
        filter_upwards [operator_apply (hm (c • q)) f, operator_apply (hm q) f,
          Lp.coeFn_smul c (operator _ (hm q) f)] with x ha hq he
        rw [RingHom.id_apply, _root_.smul_apply, ha, he, Pi.smul_apply, hq]
        change _ = (c : ℂ) * _
        rw [← integral_const_mul]
        exact integral_congr_ae (ae_of_all _ fun y => by simp [mul_assoc, Algebra.smul_def]) }
  apply A.mkContinuous 1
  intro q
  rw [one_mul]
  apply (operator_norm_le (hm q)).trans
  apply le_of_sq_le_sq _ (norm_nonneg _)
  rw [norm_sq_toLp]
  calc
    _ ≤ ∫ _ : X × X, ‖q‖ ^ 2 ∂μ.prod μ := by
      apply integral_mono ((hm q).norm.integrable_sq) (integrable_const _)
      intro z
      simpa only [Complex.norm_real, Real.norm_eq_abs] using
        pow_le_pow_left₀ (norm_nonneg _) (q.norm_coe_le_norm z) 2
    _ = _ := by simp

theorem realOperator_eq (q : C(X × X, ℝ)) (hq : MemLp (fun z => (q z : ℂ)) 2 (μ.prod μ)) :
    realOperator μ q = operator _ hq := rfl

/-- Real rank-one kernels, used for exponential and gauge averaging. -/
def gram (f : C(X, ℝ)) : C(X × X, ℝ) :=
  ⟨fun z => f z.1 * f z.2, (f.continuous.comp continuous_fst).mul
    (f.continuous.comp continuous_snd)⟩

theorem realOperator_gram (f : C(X, ℝ)) :
    (realOperator μ (gram f)).IsPositive := by
  let a : X → ℂ := fun x => f x
  have ha : MemLp a 2 μ := (Complex.continuous_ofReal.comp f.continuous).memLp_of_hasCompactSupport
    (HasCompactSupport.of_compactSpace _)
  have hk : MemLp (fun z => (gram f z : ℂ)) 2 (μ.prod μ) :=
    (Complex.continuous_ofReal.comp (gram f).continuous).memLp_of_hasCompactSupport
      (HasCompactSupport.of_compactSpace _)
  have h : realOperator μ (gram f) = rankOne ℂ (ha.toLp a) (ha.toLp a) := by
    rw [realOperator_eq μ _ hk]
    ext v : 1
    apply Lp.ext
    rw [rankOne_apply]
    filter_upwards [operator_apply hk v, Lp.coeFn_smul (⟪ha.toLp a, v⟫_ℂ) (ha.toLp a),
      ha.coeFn_toLp] with x hx hy he
    rw [hx, hy, Pi.smul_apply, smul_eq_mul, he, mul_comm, L2.inner_def, ← integral_const_mul]
    apply integral_congr_ae
    filter_upwards [ha.coeFn_toLp] with y h
    simp [gram, h, a, mul_left_comm, mul_comm]
  rw [h]
  exact isPositive_rankOne_self _

end GapChain.Kernel

namespace GapChain.Kernel

variable {X : Type*} [TopologicalSpace X]

/-- Finite sums of real rank-one kernels. The factors are allowed to have
either sign. This class is stable under pointwise multiplication. -/
inductive FiniteGram : C(X × X, ℝ) → Prop
  | zero : FiniteGram 0
  | atom (f : C(X, ℝ)) : FiniteGram (gram f)
  | add {q r} : FiniteGram q → FiniteGram r → FiniteGram (q+r)

theorem FiniteGram.mul_atom {q : C(X × X, ℝ)} (hq : FiniteGram q) (f : C(X, ℝ)) :
    FiniteGram (q * gram f) := by
  induction hq with
  | zero => simpa using (FiniteGram.zero (X := X))
  | atom g =>
    convert FiniteGram.atom (g*f) using 1
    ext z
    simp [gram]
    ring
  | add _ _ ih₁ ih₂ => simpa [add_mul] using ih₁.add ih₂

theorem FiniteGram.mul {q r : C(X × X, ℝ)} (hq : FiniteGram q) (hr : FiniteGram r) :
    FiniteGram (q*r) := by
  induction hr with
  | zero => simpa using (FiniteGram.zero (X := X))
  | atom f => exact hq.mul_atom f
  | add _ _ ih₁ ih₂ => simpa [mul_add] using ih₁.add ih₂

theorem FiniteGram.const {c : ℝ} (hc : 0 ≤ c) :
    FiniteGram (ContinuousMap.const (X × X) c) := by
  convert FiniteGram.atom (ContinuousMap.const X (√c)) using 1
  ext z
  exact (Real.mul_self_sqrt hc).symm

theorem FiniteGram.pow {q : C(X × X, ℝ)} (hq : FiniteGram q) (n : ℕ) : FiniteGram (q ^ n) := by
  induction n with
  | zero => simpa only [pow_zero, ContinuousMap.const_one] using (FiniteGram.const (X := X) zero_le_one)
  | succ n ih => simpa only [pow_succ] using ih.mul hq

theorem FiniteGram.smul {q : C(X × X, ℝ)} (hq : FiniteGram q) {c : ℝ} (hc : 0 ≤ c) :
    FiniteGram (c • q) := (FiniteGram.const hc).mul hq

theorem FiniteGram.sum {ι : Type*} (s : Finset ι) (q : ι → C(X × X, ℝ))
    (hq : ∀ i ∈ s, FiniteGram (q i)) : FiniteGram (∑ i ∈ s, q i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using (FiniteGram.zero (X := X))
  | insert i s hi ih =>
    rw [Finset.sum_insert hi]
    exact (hq i (by simp)).add (ih fun j hj => hq j (by simp [hj]))

/-- Exponentiating a finite Gram kernel is a uniform limit of finite Gram
kernels. This is the exact exponential series in the Banach algebra C(X²,ℝ). -/
theorem FiniteGram.exp_mem_closure [CompactSpace X] {q : C(X × X, ℝ)} (hq : FiniteGram q) :
    NormedSpace.exp q ∈ closure {p | FiniteGram p} := by
  apply mem_closure_of_tendsto (NormedSpace.exp_series_hasSum_exp' (𝕂 := ℝ) q)
  exact Eventually.of_forall fun s => FiniteGram.sum s _ fun n _ =>
    (hq.pow n).smul (by positivity)

end GapChain.Kernel

namespace GapChain.Kernel

variable {X Y G : Type*} [TopologicalSpace X] [CompactSpace X]
  [TopologicalSpace Y] [CompactSpace Y] [FirstCountableTopology Y]
  [TopologicalSpace G] [CompactSpace G] [MeasurableSpace G] [OpensMeasurableSpace G]

/-- Average the pullbacks of a continuous scalar function over a probability space. -/
def average (ν : Measure G) [IsProbabilityMeasure ν] (a : C(Y × G, X)) :
    C(X, ℝ) →L[ℝ] C(Y, ℝ) := by
  let A : C(X, ℝ) →ₗ[ℝ] C(Y, ℝ) :=
    { toFun := fun q => ⟨fun y => ∫ g, q (a (y,g)) ∂ν, by
        apply continuous_of_dominated (bound := fun _ => ‖q‖)
        · intro y
          exact ((q.continuous.comp a.continuous).comp (continuous_const.prodMk continuous_id)).aestronglyMeasurable
        · exact fun y => ae_of_all _ fun g => q.norm_coe_le_norm _
        · exact integrable_const _
        · exact ae_of_all _ fun g => (q.continuous.comp a.continuous).comp
            (continuous_id.prodMk continuous_const)⟩
      map_add' := fun q r => by
        ext y
        apply integral_add <;>
          exact Continuous.integrable_of_hasCompactSupport
            (by fun_prop) (HasCompactSupport.of_compactSpace _)
      map_smul' := fun c q => by
        ext y
        exact integral_const_mul _ _ }
  apply A.mkContinuous 1
  intro q
  rw [one_mul]
  apply (ContinuousMap.norm_le _ (norm_nonneg _)).2
  intro y
  change ‖∫ g, q (a (y,g)) ∂ν‖ ≤ ‖q‖
  simpa using (norm_integral_le_of_norm_le_const (μ := ν)
    (ae_of_all _ fun g => q.norm_coe_le_norm (a (y,g))))

variable [MeasurableSpace X] [BorelSpace X] [SecondCountableTopology X]
variable (μ : Measure X) [IsProbabilityMeasure μ]
variable [SecondCountableTopology G]
variable (ν : Measure G) [IsProbabilityMeasure ν]

/-- Average the two endpoints independently, then multiply by one spatial
half-weight at each endpoint. This operation preserves the closed Gram cone. -/
def sandwich (a : C(X × G, X)) (m : C(X, ℝ)) :
    C(X × X, ℝ) →L[ℝ] C(X × X, ℝ) :=
  (ContinuousLinearMap.mul ℝ _ (gram m)).comp <|
    average (ν.prod ν) ⟨fun z => (a (z.1.1,z.2.1), a (z.1.2,z.2.2)), by fun_prop⟩

omit [MeasurableSpace X] [BorelSpace X] in
theorem sandwich_gram (a : C(X × G, X)) (m f : C(X, ℝ)) :
    sandwich ν a m (gram f) = gram (m * average ν a f) := by
  ext z
  change (m z.1 * m z.2) * (∫ g : G × G, f (a (z.1,g.1)) * f (a (z.2,g.2)) ∂ν.prod ν) =
    (m z.1 * ∫ g, f (a (z.1,g)) ∂ν) * (m z.2 * ∫ g, f (a (z.2,g)) ∂ν)
  rw [integral_prod_mul (μ := ν) (ν := ν) (fun g => f (a (z.1,g))) (fun g => f (a (z.2,g)))]
  ring

theorem positive_sandwich (a : C(X × G, X)) (m : C(X, ℝ)) {q : C(X × X, ℝ)}
    (hq : q ∈ closure {p | FiniteGram p}) : (realOperator μ (sandwich ν a m q)).IsPositive := by
  let L := (realOperator μ).comp (sandwich ν a m)
  change (L q).IsPositive
  apply (ContinuousLinearMap.nonneg_iff_isPositive _).mp
  apply (isClosed_le continuous_const L.continuous).closure_subset_iff.mpr _ hq
  intro p hp
  change FiniteGram p at hp
  induction hp with
  | zero => simp
  | atom f =>
    apply (ContinuousLinearMap.nonneg_iff_isPositive _).mpr
    change (realOperator μ (sandwich ν a m (gram f))).IsPositive
    rw [sandwich_gram]
    exact realOperator_gram μ _
  | add _ _ ih₁ ih₂ => simpa using add_nonneg ih₁ ih₂

end GapChain.Kernel

namespace GapChain.Wilson

open Kernel
open scoped Matrix

attribute [local fun_prop] continuous_halfTrace

abbrev spatialSides (R : Box) : Fin 3 → ℕ := ![R.x, R.y, R.z]
abbrev Vertex (R : Box) := (i : Fin 3) → Fin (spatialSides R i)
abbrev Edge (R : Box) := Vertex R × Fin 3
abbrev Slice (R : Box) := Edge R → SU2
abbrev Gauges (R : Box) := Vertex R → SU2
abbrev sliceHaar (R : Box) : Measure (Slice R) := Measure.pi (fun _ => linkHaar)
abbrev gaugeHaar (R : Box) : Measure (Gauges R) := Measure.pi (fun _ => linkHaar)

def spatialStep {R : Box} (x : Vertex R) (i : Fin 3) : Vertex R :=
  fun j => if j = i then finRotate (spatialSides R j) (x j) else x j

abbrev SpatialPlane := {p : Fin 3 × Fin 3 // p.1 < p.2}

def spatialAction {R : Box} (u : Slice R) : ℝ :=
  ∑ x : Vertex R, ∑ p : SpatialPlane,
    (1 - halfTrace (u (x,p.1.1) * u (spatialStep x p.1.1,p.1.2) *
      (u (spatialStep x p.1.2,p.1.1))⁻¹ * (u (x,p.1.2))⁻¹))

theorem continuous_spatialAction (R : Box) : Continuous (@spatialAction R) := by
  unfold spatialAction
  fun_prop (disch := exact continuous_halfTrace)

attribute [local fun_prop] continuous_spatialAction

theorem spatialAction_nonneg {R : Box} (u : Slice R) : 0 ≤ spatialAction u :=
  Finset.sum_nonneg fun _ _ => Finset.sum_nonneg fun _ _ => sub_nonneg.mpr (halfTrace_le_one _)

def halfWeight (β : ℝ) (R : Box) : C(Slice R, ℝ) :=
  ⟨fun u => Real.exp (-β * spatialAction u / 2), by
    fun_prop (disch := exact continuous_spatialAction R)⟩

/-- The temporal links act as independent gauge variables at the vertices. -/
def gaugeAction (R : Box) : C(Slice R × Gauges R, Slice R) :=
  ⟨fun z e => z.2 e.1 * z.1 e * (z.2 (spatialStep e.1 e.2))⁻¹, by fun_prop⟩

theorem gauge_mul {R : Box} (u : Slice R) (g h : Gauges R) :
    gaugeAction R (gaugeAction R (u,h),g) = gaugeAction R (u,g*h) := by
  ext e : 1
  simp [gaugeAction, mul_assoc]

def temporalAction {R : Box} (z : Slice R × Slice R) : ℝ :=
  ∑ e : Edge R, (1 - halfTrace (z.2 e * (z.1 e)⁻¹))

def temporal (β : ℝ) (R : Box) : C(Slice R × Slice R, ℝ) :=
  ⟨fun z => Real.exp (-β * temporalAction z), by
    unfold temporalAction
    fun_prop (disch := exact continuous_halfTrace)⟩

/-- One vertex gauge average and half the spatial action on each endpoint. -/
def transferKernel (β : ℝ) (R : Box) : C(Slice R × Slice R, ℝ) :=
  gram (halfWeight β R) *
    average (gaugeHaar R) ⟨fun z => (z.1.1, gaugeAction R (z.1.2,z.2)), by fun_prop⟩ (temporal β R)

theorem transferKernel_apply (β : ℝ) (R : Box) (u v : Slice R) :
    transferKernel β R (u,v) = Real.exp (-β * (spatialAction u + spatialAction v) / 2) *
      ∫ g : Gauges R, ∏ e : Edge R, Real.exp (-β *
        (1 - halfTrace (g e.1 * v e * (g (spatialStep e.1 e.2))⁻¹ * (u e)⁻¹))) ∂gaugeHaar R := by
  change (Real.exp _ * Real.exp _) * (∫ _, Real.exp _ ∂_) = _
  congr 1
  · rw [← Real.exp_add]
    congr 1
    ring
  · apply integral_congr_ae
    apply ae_of_all
    intro g
    dsimp only
    rw [← Real.exp_sum]
    congr 1
    exact Finset.mul_sum _ _ _

theorem halfTrace_conjugate (a b : SU2) : halfTrace (a * b * a⁻¹) = halfTrace b := by
  have comm (s t : SU2) : halfTrace (s*t) = halfTrace (t*s) :=
    congrArg (fun z : ℂ => z.re / 2) (Matrix.trace_mul_comm s.val t.val)
  rw [comm, inv_mul_cancel_left]

theorem temporal_gauge (β : ℝ) (R : Box) (u v : Slice R) (h : Gauges R) :
    temporal β R (gaugeAction R (u,h), gaugeAction R (v,h)) = temporal β R (u,v) := by
  change Real.exp (-β * ∑ e, _) = Real.exp (-β * ∑ e, _)
  congr 2
  apply Finset.sum_congr rfl
  intro e _
  rw [show gaugeAction R (v,h) e * (gaugeAction R (u,h) e)⁻¹ =
    h e.1 * (v e * (u e)⁻¹) * (h e.1)⁻¹ by simp [gaugeAction, mul_assoc]]
  rw [halfTrace_conjugate]

/-- Independent endpoint averages reduce to the single temporal-link integral
by left invariance of normalized vertex Haar and simultaneous gauge invariance. -/
theorem transferKernel_eq_sandwich (β : ℝ) (R : Box) :
    transferKernel β R = sandwich (gaugeHaar R) (gaugeAction R) (halfWeight β R) (temporal β R) := by
  ext z
  let q := temporal β R
  let a := gaugeAction R
  let ν := gaugeHaar R
  change _ * (∫ h, q (z.1, a (z.2,h)) ∂ν) =
    _ * (∫ p : Gauges R × Gauges R, q (a (z.1,p.1), a (z.2,p.2)) ∂ν.prod ν)
  congr 1
  have hi : Integrable (fun p : Gauges R × Gauges R => q (a (z.1,p.1), a (z.2,p.2))) (ν.prod ν) :=
    Continuous.integrable_of_hasCompactSupport (by fun_prop) (HasCompactSupport.of_compactSpace _)
  rw [integral_prod _ hi]
  have innerEq (g : Gauges R) :
      (∫ h, q (a (z.1,g), a (z.2,h)) ∂ν) = ∫ h, q (z.1, a (z.2,h)) ∂ν := by
    calc
      _ = ∫ h, q (a (z.1,g), a (z.2,g*h)) ∂ν :=
        (integral_mul_left_eq_self (μ := ν) (fun h => q (a (z.1,g), a (z.2,h))) g).symm
      _ = _ := by
        apply integral_congr_ae
        exact ae_of_all _ fun h => by
          change temporal β R (gaugeAction R (z.1,g), gaugeAction R (z.2,g*h)) = _
          rw [← gauge_mul, temporal_gauge]
  simp only [innerEq, integral_const, probReal_univ, one_smul]

/-- The real part of the matrix trace is the Euclidean dot product of the
real and imaginary matrix entries. This avoids a choice of SU(2) coordinates. -/
theorem halfTrace_mul_inv_entries (v u : SU2) : halfTrace (v*u⁻¹) =
    (∑ i : Fin 2, ∑ j : Fin 2, ((u.val i j).re * (v.val i j).re +
      (u.val i j).im * (v.val i j).im)) / 2 := by
  change ((v.val * u.valᴴ).trace.re / 2) = _
  simp [Matrix.trace, Matrix.mul_apply, Complex.mul_re,
    mul_comm]

theorem continuous_entry {R : Box} (e : Edge R) (i j : Fin 2) :
    Continuous (fun u : Slice R => (u e).val i j) := by
  have hv : Continuous (fun g : SU2 => g.val) := continuous_subtype_val
  have he : Continuous (fun u : Slice R => u e) := continuous_apply e
  exact (hv.comp he).matrix_elem i j

def entryRe {R : Box} (e : Edge R) (i j : Fin 2) : C(Slice R, ℝ) :=
  ⟨fun u => ((u e).val i j).re, Complex.continuous_re.comp (continuous_entry e i j)⟩

def entryIm {R : Box} (e : Edge R) (i j : Fin 2) : C(Slice R, ℝ) :=
  ⟨fun u => ((u e).val i j).im, Complex.continuous_im.comp (continuous_entry e i j)⟩

def score (β : ℝ) (R : Box) : C(Slice R × Slice R, ℝ) :=
  (β / 2) • ∑ e : Edge R, ∑ i : Fin 2, ∑ j : Fin 2,
    (gram (entryRe e i j) + gram (entryIm e i j))

theorem score_gram {β : ℝ} (hβ : 0 ≤ β) (R : Box) : FiniteGram (score β R) :=
  (FiniteGram.sum _ _ fun e _ => FiniteGram.sum _ _ fun i _ => FiniteGram.sum _ _ fun j _ =>
    (FiniteGram.atom (entryRe e i j)).add (FiniteGram.atom (entryIm e i j))).smul (by positivity)

theorem temporal_eq_exp (β : ℝ) (R : Box) :
    temporal β R = Real.exp (-β * Fintype.card (Edge R)) • NormedSpace.exp (score β R) := by
  ext z
  have ev : (NormedSpace.exp (score β R)) z = Real.exp (score β R z) := by
    rw [Real.exp_eq_exp_ℝ]
    exact NormedSpace.map_exp (ContinuousMap.evalAlgHom ℝ ℝ z) (continuous_eval_const _) _
  change Real.exp (-β * temporalAction z) = Real.exp _ * (NormedSpace.exp (score β R)) z
  rw [ev, ← Real.exp_add]
  congr 1
  simp only [temporalAction, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ,
    nsmul_eq_mul, mul_one, halfTrace_mul_inv_entries, score, ContinuousMap.smul_apply,
    smul_eq_mul, ContinuousMap.sum_apply, ContinuousMap.add_apply, gram, entryRe, entryIm,
    ContinuousMap.coe_mk, ← Finset.sum_div]
  ring

theorem temporal_gram_closure {β : ℝ} (hβ : 0 ≤ β) (R : Box) :
    temporal β R ∈ closure {p | FiniteGram p} := by
  rw [temporal_eq_exp]
  let c := Real.exp (-β * Fintype.card (Edge R))
  have hmap : closure {p : C(Slice R × Slice R, ℝ) | FiniteGram p} ⊆
      (fun p => c • p) ⁻¹' closure {p | FiniteGram p} := by
    apply (isClosed_closure.preimage (continuous_const_smul c)).closure_subset_iff.mpr
    intro p hp
    exact subset_closure (FiniteGram.smul hp (Real.exp_pos _).le)
  exact hmap (score_gram hβ R).exp_mem_closure

/-- The one-step Wilson operator on the full spatial-link L² space. -/
def transfer (β : ℝ) (R : Box) : Space (sliceHaar R) →L[ℂ] Space (sliceHaar R) :=
  realOperator (sliceHaar R) (transferKernel β R)

theorem transferKernel_memLp (β : ℝ) (R : Box) :
    MemLp (fun z => (transferKernel β R z : ℂ)) 2 ((sliceHaar R).prod (sliceHaar R)) :=
  (Complex.continuous_ofReal.comp (transferKernel β R).continuous).memLp_of_hasCompactSupport
    (HasCompactSupport.of_compactSpace _)

theorem transfer_apply (β : ℝ) (R : Box) (f : Space (sliceHaar R)) :
    ⇑(transfer β R f) =ᵐ[sliceHaar R] fun u =>
      ∫ v, (transferKernel β R (u,v) : ℂ) * f v ∂sliceHaar R :=
  operator_apply (transferKernel_memLp β R) f

theorem transfer_positive {β : ℝ} (hβ : 0 ≤ β) (R : Box) : (transfer β R).IsPositive := by
  unfold transfer
  rw [transferKernel_eq_sandwich]
  exact positive_sandwich _ _ _ _ (temporal_gram_closure hβ R)

theorem transfer_compact (β : ℝ) (R : Box) : IsCompactOperator (transfer β R) :=
  operator_compact (transferKernel_memLp β R)

end GapChain.Wilson

namespace GapChain.Wilson

open Kernel

theorem transferKernel_pos (β : ℝ) (R : Box) (z : Slice R × Slice R) :
    0 < transferKernel β R z := by
  change 0 < (Real.exp _ * Real.exp _) * ∫ g : Gauges R,
    Real.exp (-β * temporalAction (z.1,gaugeAction R (z.2,g))) ∂gaugeHaar R
  apply mul_pos (mul_pos (Real.exp_pos _) (Real.exp_pos _))
  apply integral_exp_pos
  change Integrable (fun g => temporal β R (z.1, gaugeAction R (z.2,g))) _
  exact Continuous.integrable_of_hasCompactSupport (by fun_prop) (HasCompactSupport.of_compactSpace _)

theorem transferKernel_le_one {β : ℝ} (hβ : 0 ≤ β) (R : Box) (z : Slice R × Slice R) :
    transferKernel β R z ≤ 1 := by
  have half (u : Slice R) : halfWeight β R u ≤ 1 :=
    Real.exp_le_one_iff.mpr (div_nonpos_of_nonpos_of_nonneg
      (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr hβ) (spatialAction_nonneg u)) (by norm_num))
  have tim (p : Slice R × Slice R) : temporal β R p ≤ 1 :=
    Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr hβ)
      (Finset.sum_nonneg fun _ _ => sub_nonneg.mpr (halfTrace_le_one _)))
  have avg : (∫ g, temporal β R (z.1, gaugeAction R (z.2,g)) ∂gaugeHaar R) ≤ 1 := by
    calc
      _ ≤ ∫ _ : Gauges R, (1 : ℝ) ∂gaugeHaar R := integral_mono
        (Continuous.integrable_of_hasCompactSupport (by fun_prop) (HasCompactSupport.of_compactSpace _))
        (integrable_const _) (fun _ => tim _)
      _ = _ := by simp
  exact mul_le_one₀ (mul_le_one₀ (half _) (Real.exp_pos _).le (half _))
    (integral_nonneg fun _ => (Real.exp_pos _).le) avg

theorem transfer_hs {β : ℝ} (hβ : 0 ≤ β) (R : Box) : HSNormLE (transfer β R) 1 := by
  have hk := transferKernel_memLp β R
  intro n v hv
  apply ((operator_hs hk) n v hv).trans
  rw [norm_sq_toLp]
  calc
    _ ≤ ∫ _ : Slice R × Slice R, (1 : ℝ) ^ 2 ∂(sliceHaar R).prod (sliceHaar R) := by
      apply integral_mono hk.norm.integrable_sq (integrable_const _)
      intro z
      change ‖(transferKernel β R z : ℂ)‖ ^ 2 ≤ 1 ^ 2
      rw [Complex.norm_real, Real.norm_eq_abs, abs_of_pos (transferKernel_pos β R z)]
      exact pow_le_pow_left₀ (transferKernel_pos β R z).le (transferKernel_le_one hβ R z) 2
    _ = _ := by simp

theorem transfer_ne_zero (β : ℝ) (R : Box) : transfer β R ≠ 0 := by
  let μ := sliceHaar R
  let one : Space μ := (memLp_const (1 : ℂ)).toLp _
  have hOne : ⇑one =ᵐ[μ] fun _ => (1 : ℂ) := (memLp_const _).coeFn_toLp
  intro hz
  have hz' : ⇑(transfer β R one) =ᵐ[μ] fun _ => 0 := by
    rw [hz]
    change ⇑(0 : Space μ) =ᵐ[μ] _
    exact Lp.coeFn_zero ℂ 2 μ
  obtain ⟨u, hu⟩ := ((transfer_apply β R one).symm.trans hz').exists
  have hi : (∫ v, (transferKernel β R (u,v) : ℂ) * one v ∂μ) =
      ((∫ v, transferKernel β R (u,v) ∂μ : ℝ) : ℂ) := by
    rw [← integral_complex_ofReal]
    exact integral_congr_ae (hOne.mono fun v hv => by simp [hv])
  have hpos : 0 < ∫ v, transferKernel β R (u,v) ∂μ := by
    apply (integral_pos_iff_support_of_nonneg (fun v => (transferKernel_pos β R (u,v)).le)
      (Continuous.integrable_of_hasCompactSupport (by fun_prop) (HasCompactSupport.of_compactSpace _))).2
    have hs : Function.support (fun v => transferKernel β R (u,v)) = univ :=
      Set.eq_univ_iff_forall.mpr fun v => (transferKernel_pos β R (u,v)).ne'
    simp [hs]
  exact hpos.ne' (Complex.ofReal_eq_zero.mp (hi.symm.trans hu))

/-- The physical operator provides the top and the multiplicity list for
every valid rectangle. The periodic Haar cycle identity is a separate step. -/
theorem transfer_boxSpectrum (β : ℝ) (hβ : 0 < β) (R : Box) (_hR : R.Valid) :
    ∃ B : BoxSpectrum, B.top = ‖transfer β R‖ ∧
      (∃ t : PositiveSlot (transfer β R), t.1.val = ‖transfer β R‖ ∧
        EnumeratesRatios B (fun i => i.1.val) t) ∧
      ∀ a : ℕ, 3 ≤ a → B.weight a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a := by
  cases subsingleton_or_nontrivial (Space (sliceHaar R)) with
  | inl h => exact False.elim (transfer_ne_zero β R (Subsingleton.elim _ _))
  | inr h =>
    exact boxSpectrum_of_operator _ (transfer_compact β R) (transfer_positive hβ.le R)
      (transfer_ne_zero β R) (transfer_hs hβ.le R)

end GapChain.Wilson

#print axioms GapChain.Kernel.norm_sq
#print axioms GapChain.Kernel.norm_sq_toLp
#print axioms GapChain.Kernel.sections
#print axioms GapChain.Kernel.row_inner
#print axioms GapChain.Kernel.row_norm_sq
#print axioms GapChain.Kernel.integrable_row_norm_sq
#print axioms GapChain.Kernel.integral_row_norm_sq
#print axioms GapChain.Kernel.row_inner_memLp
#print axioms GapChain.Kernel.row_bound
#print axioms GapChain.Kernel.operator_norm_le
#print axioms GapChain.Kernel.operator_apply
#print axioms GapChain.Kernel.operator_congr
#print axioms GapChain.Kernel.operator_hs
#print axioms GapChain.Kernel.outer_memLp
#print axioms GapChain.Kernel.pairing
#print axioms GapChain.Kernel.adjKernel_memLp
#print axioms GapChain.Kernel.operator_adjoint
#print axioms GapChain.Kernel.operator_selfAdjoint
#print axioms GapChain.HSNormLE.isCompact
#print axioms GapChain.Kernel.operator_compact
#print axioms GapChain.Kernel.realOperator_eq
#print axioms GapChain.Kernel.realOperator_gram
#print axioms GapChain.Kernel.FiniteGram.mul_atom
#print axioms GapChain.Kernel.FiniteGram.mul
#print axioms GapChain.Kernel.FiniteGram.const
#print axioms GapChain.Kernel.FiniteGram.pow
#print axioms GapChain.Kernel.FiniteGram.smul
#print axioms GapChain.Kernel.FiniteGram.sum
#print axioms GapChain.Kernel.FiniteGram.exp_mem_closure
#print axioms GapChain.Kernel.sandwich_gram
#print axioms GapChain.Kernel.positive_sandwich
#print axioms GapChain.Wilson.continuous_spatialAction
#print axioms GapChain.Wilson.spatialAction_nonneg
#print axioms GapChain.Wilson.gauge_mul
#print axioms GapChain.Wilson.transferKernel_apply
#print axioms GapChain.Wilson.halfTrace_conjugate
#print axioms GapChain.Wilson.temporal_gauge
#print axioms GapChain.Wilson.transferKernel_eq_sandwich
#print axioms GapChain.Wilson.halfTrace_mul_inv_entries
#print axioms GapChain.Wilson.continuous_entry
#print axioms GapChain.Wilson.score_gram
#print axioms GapChain.Wilson.temporal_eq_exp
#print axioms GapChain.Wilson.temporal_gram_closure
#print axioms GapChain.Wilson.transferKernel_memLp
#print axioms GapChain.Wilson.transfer_apply
#print axioms GapChain.Wilson.transfer_positive
#print axioms GapChain.Wilson.transfer_compact
#print axioms GapChain.Wilson.transferKernel_pos
#print axioms GapChain.Wilson.transferKernel_le_one
#print axioms GapChain.Wilson.transfer_hs
#print axioms GapChain.Wilson.transfer_ne_zero
#print axioms GapChain.Wilson.transfer_boxSpectrum
