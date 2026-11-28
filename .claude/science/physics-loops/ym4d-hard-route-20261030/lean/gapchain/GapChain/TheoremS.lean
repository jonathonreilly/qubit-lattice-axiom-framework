import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Order.MonotoneConvergence
import Mathlib.Tactic

/-!
# A finite seed for all cubic periods (W5)

Claude Fable 5.2, row 697, §3.4 (K, X, E and Theorem S).
Codex GPT-6 Astra, row 699, point 8 (E′ and the corrected S3′).
The symmetric two-period argument uses the submultiplicativity and
log-convexity of the trace (Lemma A). The final time step uses the
ordinary counting sum over excited eigenvalues with multiplicities.
All periods entering a trace are at least three.
-/

open Filter Set
open scoped Topology BigOperators
noncomputable section

namespace GapChain

/-- Two varying periods with the other two held fixed. The lower bound is the
finite-bulk-density hypothesis in §3.4. Symmetry supplies Lemma A in the second period. -/
structure PairWeight where
  W : ℕ → ℕ → ℝ
  pos : ∀ {a b}, 3 ≤ a → 3 ≤ b → 0 < W a b
  swap : ∀ {a b}, 3 ≤ a → 3 ≤ b → W a b = W b a
  submul : ∀ {a c b}, 3 ≤ a → 3 ≤ c → 3 ≤ b → W (a + c) b ≤ W a b * W c b
  logConvex : ∀ {a b}, 3 ≤ a → 3 ≤ b → W (a + 1) b ^ 2 ≤ W a b * W (a + 2) b
  lower : ∃ d : ℝ, ∀ {a b}, 3 ≤ a → 3 ≤ b → d * a * b ≤ Real.log (W a b)

namespace PairWeight

variable (P : PairWeight)

/-- Restrict the infimum of normalized logarithms to the admissible periods. -/
def slopeInf (f : ℕ → ℝ) : ℝ := ⨅ j : ℕ, f (j + 3) / (↑(j + 3 : ℕ) : ℝ)

/-- Logarithm of the two-period partition function. -/
def F (a b : ℕ) : ℝ := Real.log (P.W a b)

/-- Long-time log weight per time step. For a trace weight this is the logarithm
of the top eigenvalue. -/
def ground (b : ℕ) : ℝ := slopeInf (fun a => P.F a b)

/-- Bulk log density for these fixed spectator periods. -/
def bulk : ℝ := slopeInf P.ground

/-- The ground logarithm above its bulk contribution. -/
def deficit (b : ℕ) : ℝ := P.ground b - P.bulk * b

/-- The logarithm of one plus the excited-state thermal sum. -/
def g (a b : ℕ) : ℝ := P.F a b - a * P.ground b

/-- Excited-state thermal sum expressed through the two-period weight. -/
def thermal (a b : ℕ) : ℝ := Real.exp (P.g a b) - 1

/-- A discrete convex function lies above the line of any earlier forward difference. -/
private theorem secant_lower {f : ℕ → ℝ}
    (hc : ∀ n ≥ 3, 2 * f (n + 1) ≤ f n + f (n + 2)) {a : ℕ} (ha : 3 ≤ a) (k : ℕ) :
    (k : ℝ) * (f (a + 1) - f a) ≤ f (a + k) - f a := by
  have hi : MonotoneOn (fun n => f (n + 1) - f n) {n | 3 ≤ n} :=
    monotoneOn_nat_Ici_of_le_succ fun n hn => by linarith [hc n hn]
  induction k with
  | zero => simp
  | succ k ih =>
    have h := hi ha (show 3 ≤ a + k by omega) (show a ≤ a + k by omega)
    dsimp at h
    calc
      _ = (k : ℝ) * (f (a + 1) - f a) + (f (a + 1) - f a) := by push_cast; ring
      _ ≤ _ := by rw [← Nat.add_assoc]; linarith only [ih, h]

private theorem convex_first {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) :
    2 * P.F (a + 1) b ≤ P.F a b + P.F (a + 2) b := by
  have h := Real.log_le_log (pow_pos (P.pos (by omega : 3 ≤ a + 1) hb) 2)
    (P.logConvex ha hb)
  rw [Real.log_pow, Real.log_mul (P.pos ha hb).ne' (P.pos (by omega) hb).ne'] at h
  simpa [F] using h

/-- Normalized trace logarithms decrease at *all* successive periods.
Convexity bridges the interval from a to 2a, so submultiplicativity at
the double is sufficient even for the non-dyadic interpolation. -/
theorem normalized_antitone {b : ℕ} (hb : 3 ≤ b) :
    AntitoneOn (fun a : ℕ => P.F a b / a) {a | 3 ≤ a} := by
  apply antitoneOn_nat_Ici_of_succ_le
  intro a ha
  have ha' : (0 : ℝ) < a := by exact_mod_cast (show 0 < a by omega)
  have hd := Real.log_le_log (P.pos (by omega : 3 ≤ a + a) hb) (P.submul ha ha hb)
  rw [Real.log_mul (P.pos ha hb).ne' (P.pos ha hb).ne'] at hd
  change P.F (a + a) b ≤ P.F a b + P.F a b at hd
  have hs := secant_lower (f := fun a => P.F a b) (fun n hn => P.convex_first hn hb) ha a
  apply (div_le_div_iff₀ (by positivity) ha').2
  push_cast
  linarith

private theorem bounded_slopes {b : ℕ} (hb : 3 ≤ b) :
    BddBelow (range fun j : ℕ => P.F (j + 3) b / (↑(j + 3 : ℕ) : ℝ)) := by
  obtain ⟨d, hd⟩ := P.lower
  refine ⟨d * b, ?_⟩
  rintro _ ⟨j, rfl⟩
  apply (le_div_iff₀ (by positivity)).2
  simpa [F, mul_right_comm] using hd (show 3 ≤ j + 3 by omega) hb

/-- K(a). The ground logarithm is both the infimum and the limit of log W(a,b)/a. -/
theorem ground_limit {b : ℕ} (hb : 3 ≤ b) :
    Tendsto (fun a : ℕ => P.F a b / a) atTop (𝓝 (P.ground b)) := by
  apply (tendsto_add_atTop_iff_nat 3).1
  exact tendsto_atTop_ciInf (antitone_add_nat_iff_antitoneOn_nat_Ici.mpr
    (P.normalized_antitone hb)) (P.bounded_slopes hb)

theorem ground_le {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) :
    P.ground b ≤ P.F a b / a := by
  simpa only [ground, slopeInf, Nat.sub_add_cancel ha] using ciInf_le (P.bounded_slopes hb) (a - 3)

private theorem ground_lower {d : ℝ}
    (hd : ∀ {a b : ℕ}, 3 ≤ a → 3 ≤ b → d * a * b ≤ P.F a b) {b : ℕ} (hb : 3 ≤ b) :
    d * b ≤ P.ground b := by
  apply le_ciInf
  intro j
  apply (le_div_iff₀ (by positivity)).2
  simpa [mul_right_comm] using hd (show 3 ≤ j + 3 by omega) hb

private theorem bulk_bounded :
    BddBelow (range fun j : ℕ => P.ground (j + 3) / (↑(j + 3 : ℕ) : ℝ)) := by
  obtain ⟨d, hd⟩ := P.lower
  refine ⟨d, ?_⟩
  rintro _ ⟨j, rfl⟩
  exact (le_div_iff₀ (by positivity)).2 (P.ground_lower hd (by omega))

/-- K(b), the bulk value is the infimum over both admissible periods. -/
theorem bulk_eq :
    P.bulk = ⨅ j : ℕ, ⨅ i : ℕ, P.F (i + 3) (j + 3) /
      ((↑(i + 3 : ℕ) : ℝ) * (↑(j + 3 : ℕ) : ℝ)) := by
  have hi (j : ℕ) : P.ground (j + 3) / (↑(j + 3 : ℕ) : ℝ) =
      ⨅ i : ℕ, P.F (i + 3) (j + 3) / ((↑(i + 3 : ℕ) : ℝ) * (↑(j + 3 : ℕ) : ℝ)) := by
    have hj : (0 : ℝ) < (↑(j + 3 : ℕ) : ℝ) := by positivity
    have hden (i : ℕ) : (0 : ℝ) < (↑(i + 3 : ℕ) : ℝ) * (↑(j + 3 : ℕ) : ℝ) := by positivity
    obtain ⟨d, hd⟩ := P.lower
    have hbdd : BddBelow (range fun i : ℕ => P.F (i + 3) (j + 3) /
        ((↑(i + 3 : ℕ) : ℝ) * (↑(j + 3 : ℕ) : ℝ))) := by
      refine ⟨d, ?_⟩
      rintro _ ⟨i, rfl⟩
      exact (le_div_iff₀ (hden i)).2 (by simpa [F, mul_assoc] using (hd (show 3 ≤ i + 3 by omega) (show 3 ≤ j + 3 by omega)))
    apply le_antisymm
    · apply le_ciInf
      intro i
      rw [← div_div]
      exact div_le_div_of_nonneg_right (P.ground_le (by omega) (by omega)) hj.le
    · apply (le_div_iff₀ hj).2
      apply le_ciInf
      intro i
      apply (le_div_iff₀ hj).1
      rw [div_div]
      exact ciInf_le hbdd i
  exact iInf_congr hi

theorem deficit_nonneg {b : ℕ} (hb : 3 ≤ b) : 0 ≤ P.deficit b := by
  have h : P.bulk ≤ P.ground b / b := by
    simpa only [bulk, slopeInf, Nat.sub_add_cancel hb] using ciInf_le P.bulk_bounded (b - 3)
  exact sub_nonneg.mpr ((le_div_iff₀ (by exact_mod_cast (show 0 < b by omega))).1 h)

private theorem F_swap {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) : P.F a b = P.F b a :=
  congrArg Real.log (P.swap ha hb)

/-- The normalized ground logarithms also decrease. This includes K(b) at multiples. -/
theorem ground_normalized_antitone : AntitoneOn (fun b : ℕ => P.ground b / b) {b | 3 ≤ b} := by
  intro b hb h hh hbh
  apply le_of_tendsto_of_tendsto ((P.ground_limit hh).div_const (h : ℝ))
    ((P.ground_limit hb).div_const (b : ℝ))
  filter_upwards [eventually_ge_atTop 3] with a ha
  have hnorm := P.normalized_antitone ha hb hh hbh
  dsimp at hnorm ⊢
  rw [P.F_swap ha hh, P.F_swap ha hb]
  simpa only [div_div, mul_comm (a : ℝ)] using
    div_le_div_of_nonneg_right hnorm (Nat.cast_nonneg (α := ℝ) a)

theorem ground_multiple {b j : ℕ} (hb : 3 ≤ b) (hj : 1 ≤ j) :
    P.ground (j * b) ≤ j * P.ground b := by
  have hbj : b ≤ j * b := Nat.le_mul_of_pos_left _ (by omega)
  have h := P.ground_normalized_antitone hb (le_trans hb hbj) hbj
  have hb' : (0 : ℝ) < b := by exact_mod_cast (show 0 < b by omega)
  have hj' : (0 : ℝ) < j := by exact_mod_cast (show 0 < j by omega)
  have h' := (div_le_div_iff₀ (by positivity : (0 : ℝ) < (↑(j * b : ℕ) : ℝ)) hb').1 h
  push_cast at h'
  exact (le_of_mul_le_mul_right (by linarith) hb')

/-- K(c). Discrete convexity passes to the ground logarithm in the long-time limit. -/
theorem ground_convex {b : ℕ} (hb : 3 ≤ b) :
    2 * P.ground (b + 1) ≤ P.ground b + P.ground (b + 2) := by
  apply le_of_tendsto_of_tendsto ((P.ground_limit (by omega : 3 ≤ b + 1)).const_mul 2)
    ((P.ground_limit hb).add (P.ground_limit (by omega : 3 ≤ b + 2)))
  filter_upwards [eventually_ge_atTop 3] with a ha
  rw [P.F_swap ha (by omega : 3 ≤ b + 1), P.F_swap ha hb,
    P.F_swap ha (by omega : 3 ≤ b + 2), ← mul_div_assoc, ← add_div]
  exact div_le_div_of_nonneg_right (P.convex_first hb ha) (Nat.cast_nonneg a)

theorem deficit_convex {b : ℕ} (hb : 3 ≤ b) :
    2 * P.deficit (b + 1) ≤ P.deficit b + P.deficit (b + 2) := by
  unfold deficit
  push_cast
  linarith [P.ground_convex hb]

/-- K(d). At any later period the forward difference dominates the earlier
difference and is bounded above by the later normalized ground logarithm.
Taking its infimum proves that the deficit is non-increasing. -/
theorem lemmaK : AntitoneOn P.deficit {b | 3 ≤ b} := by
  have inc : MonotoneOn (fun b => P.ground (b + 1) - P.ground b) {b | 3 ≤ b} :=
    monotoneOn_nat_Ici_of_le_succ fun b hb => by linarith [P.ground_convex hb]
  apply antitoneOn_nat_Ici_of_succ_le
  intro b hb
  have hdiff : P.ground (b + 1) - P.ground b ≤ P.bulk := by
    apply le_ciInf
    intro j
    let h := max b (j + 3)
    have hbh : b ≤ h := le_max_left _ _
    have hjh : j + 3 ≤ h := le_max_right _ _
    have hh := le_trans hb hbh
    have hh' : (0 : ℝ) < h := by exact_mod_cast (show 0 < h by omega)
    have hnorm := P.ground_normalized_antitone hh (show 3 ≤ h + 1 by omega) (Nat.le_succ h)
    have hn := (div_le_div_iff₀ (by positivity : (0 : ℝ) < (↑(h + 1 : ℕ) : ℝ)) hh').1 hnorm
    push_cast at hn
    calc
      _ ≤ P.ground (h + 1) - P.ground h := inc hb hh hbh
      _ ≤ P.ground h / h := (le_div_iff₀ hh').2 (by linarith)
      _ ≤ _ := P.ground_normalized_antitone (by omega : 3 ≤ j + 3) hh hjh
  unfold deficit
  push_cast
  linarith

theorem g_nonneg {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) : 0 ≤ P.g a b := by
  have ha' : (0 : ℝ) < a := by exact_mod_cast (show 0 < a by omega)
  have h := (le_div_iff₀ ha').1 (P.ground_le ha hb)
  unfold g
  linarith

/-- X, including the exact crossing identity before discarding the two
nonnegative terms. -/
theorem crossing {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) :
    a * P.deficit b + P.g a b = b * P.deficit a + P.g b a := by
  unfold deficit g
  rw [P.F_swap ha hb]
  ring

theorem lemmaX {a b : ℕ} (ha : 3 ≤ a) (hab : a < b) :
    ((b : ℝ) - a) * P.deficit b ≤ P.g a b := by
  have hb := ha.trans hab.le
  have hκ := P.lemmaK ha hb hab.le
  have hcross := P.crossing ha hb
  nlinarith [P.g_nonneg hb ha, mul_le_mul_of_nonneg_left hκ (Nat.cast_nonneg (α := ℝ) b)]

/-- E′ in logarithms, for any integer new period, including the original one. -/
theorem interpolate_log {a b h : ℕ} (ha : 3 ≤ a) (hab : a < b) (hbh : b ≤ h) :
    P.g a h ≤ (h / ((b : ℝ) - a)) * P.g a b := by
  have hb := ha.trans hab.le
  have hh := hb.trans hbh
  have ha' : (0 : ℝ) ≤ a := Nat.cast_nonneg _
  have hb' : (0 : ℝ) < b := by exact_mod_cast (show 0 < b by omega)
  have hh' : (0 : ℝ) < h := by exact_mod_cast (show 0 < h by omega)
  have hba : (0 : ℝ) < (b : ℝ) - a := sub_pos.mpr (by exact_mod_cast hab)
  have hz := (div_le_div_iff₀ hh' hb').1 (P.normalized_antitone ha hb hh hbh)
  rw [← P.F_swap ha hh, ← P.F_swap ha hb] at hz
  have h1 : (b : ℝ) * P.g a h ≤ h * (P.g a b + a * P.deficit b) := by
    have hp := mul_nonneg (mul_nonneg hb'.le ha') (P.deficit_nonneg hh)
    unfold g deficit at *
    linarith only [hz, hp]
  have h2 : ((b : ℝ) - a) * (P.g a b + a * P.deficit b) ≤ b * P.g a b := by
    linarith only [mul_le_mul_of_nonneg_left (P.lemmaX ha hab) ha']
  rw [div_mul_eq_mul_div, le_div_iff₀ hba]
  apply le_of_mul_le_mul_left _ hb'
  calc
    (b : ℝ) * (P.g a h * (b - a)) = (b - a) * (b * P.g a h) := by ring
    _ ≤ (b - a) * (h * (P.g a b + a * P.deficit b)) :=
      mul_le_mul_of_nonneg_left h1 hba.le
    _ = h * ((b - a) * (P.g a b + a * P.deficit b)) := by ring
    _ ≤ h * (b * P.g a b) := mul_le_mul_of_nonneg_left h2 hh'.le
    _ = _ := by ring

theorem lemmaE' {a b h : ℕ} (ha : 3 ≤ a) (hab : a < b) (hbh : b ≤ h) :
    1 + P.thermal a h ≤ (1 + P.thermal a b) ^ ((h : ℝ) / (b - a)) := by
  have identity (t : ℕ) : 1 + P.thermal a t = Real.exp (P.g a t) := by unfold thermal; ring
  rw [identity, identity, Real.rpow_def_of_pos (Real.exp_pos _), Real.log_exp, Real.exp_le_exp]
  simpa only [mul_comm] using P.interpolate_log ha hab hbh

theorem lemmaE {a b : ℕ} (ha : 3 ≤ a) (hab : a < b) :
    1 + P.thermal a (2 * b) ≤ (1 + P.thermal a b) ^ ((2 * b : ℝ) / (b - a)) := by
  simpa only [Nat.cast_mul, Nat.cast_ofNat] using
    P.lemmaE' ha hab (show b ≤ 2 * b by omega)

#print axioms secant_lower
#print axioms convex_first
#print axioms normalized_antitone
#print axioms bounded_slopes
#print axioms ground_limit
#print axioms ground_le
#print axioms ground_lower
#print axioms bulk_bounded
#print axioms bulk_eq
#print axioms deficit_nonneg
#print axioms F_swap
#print axioms ground_normalized_antitone
#print axioms ground_multiple
#print axioms ground_convex
#print axioms deficit_convex
#print axioms lemmaK
#print axioms g_nonneg
#print axioms crossing
#print axioms lemmaX
#print axioms interpolate_log
#print axioms lemmaE'
#print axioms lemmaE

end PairWeight

/-- Spectral data for trace powers at periods ≥ 3. Each excited eigenvalue
is listed once per multiplicity, relative to the top eigenvalue. Finiteness
of the third-power trace suffices. Zeros can pad a finite list. -/
structure BoxSpectrum where
  top : ℝ
  top_pos : 0 < top
  ratio : ℕ → ℝ
  nonneg : ∀ i, 0 ≤ ratio i
  le_one : ∀ i, ratio i ≤ 1
  atThree : Summable (fun i => ratio i ^ 3)

namespace BoxSpectrum

variable (B : BoxSpectrum)

def thermal (a : ℕ) : ℝ := ∑' i, B.ratio i ^ a
def weight (a : ℕ) : ℝ := B.top ^ a * (1 + B.thermal a)

theorem summable {a : ℕ} (ha : 3 ≤ a) : Summable (fun i => B.ratio i ^ a) :=
  Summable.of_nonneg_of_le (fun i => pow_nonneg (B.nonneg i) _)
    (fun i => pow_le_pow_of_le_one (B.nonneg i) (B.le_one i) ha) B.atThree

theorem thermal_nonneg (a : ℕ) : 0 ≤ B.thermal a :=
  tsum_nonneg fun i => pow_nonneg (B.nonneg i) _

theorem member_le {a : ℕ} (ha : 3 ≤ a) (i : ℕ) : B.ratio i ^ a ≤ B.thermal a :=
  (B.summable ha).le_tsum i (fun j _ => pow_nonneg (B.nonneg j) _)

theorem thermal_antitone {a b : ℕ} (ha : 3 ≤ a) (hab : a ≤ b) : B.thermal b ≤ B.thermal a :=
  (B.summable (ha.trans hab)).tsum_le_tsum
    (fun i => pow_le_pow_of_le_one (B.nonneg i) (B.le_one i) hab) (B.summable ha)

/-- Counting multiplicity gives the product estimate for the excited trace itself. -/
theorem thermal_add {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) :
    B.thermal (a + b) ≤ B.thermal a * B.thermal b := by
  have hm := (B.summable ha).mul_right (B.thermal b)
  calc
    B.thermal (a + b) ≤ ∑' i, B.ratio i ^ a * B.thermal b := by
      apply (B.summable (by omega : 3 ≤ a + b)).tsum_le_tsum _ hm
      intro i
      rw [pow_add]
      exact mul_le_mul_of_nonneg_left (B.member_le hb i) (pow_nonneg (B.nonneg i) _)
    _ = _ := ((B.summable ha).hasSum.mul_right (B.thermal b)).tsum_eq

theorem weight_pos (a : ℕ) : 0 < B.weight a :=
  mul_pos (pow_pos B.top_pos _) (by linarith [B.thermal_nonneg a])

theorem weight_add {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) :
    B.weight (a + b) ≤ B.weight a * B.weight b := by
  have h : 1 + B.thermal (a + b) ≤ (1 + B.thermal a) * (1 + B.thermal b) := by
    nlinarith [B.thermal_add ha hb, B.thermal_nonneg a, B.thermal_nonneg b]
  unfold weight
  rw [pow_add]
  calc
    _ ≤ _ := mul_le_mul_of_nonneg_left h (mul_nonneg (pow_nonneg B.top_pos.le a) (pow_nonneg B.top_pos.le b))
    _ = _ := by ring

theorem log_weight (a : ℕ) :
    Real.log (B.weight a) = a * Real.log B.top + Real.log (1 + B.thermal a) := by
  rw [weight, Real.log_mul (pow_pos B.top_pos _).ne' (by linarith [B.thermal_nonneg a]),
    Real.log_pow]

/-- Thus the abstract K(a) ground logarithm agrees with the spectral one. -/
theorem log_weight_limit :
    Tendsto (fun a : ℕ => Real.log (B.weight a) / a) atTop (𝓝 (Real.log B.top)) := by
  have hlim : Tendsto (fun a : ℕ => Real.log (1 + B.thermal a) / a) atTop (𝓝 0) := by
    apply squeeze_zero' _ _ (tendsto_const_div_atTop_nhds_zero_nat (Real.log (1 + B.thermal 3)))
    · exact Eventually.of_forall fun a => div_nonneg
        (Real.log_nonneg (by linarith [B.thermal_nonneg a])) (Nat.cast_nonneg a)
    · filter_upwards [eventually_ge_atTop 3] with a ha
      apply div_le_div_of_nonneg_right _ (Nat.cast_nonneg a)
      exact Real.log_le_log (by linarith [B.thermal_nonneg a])
        (add_le_add_right (B.thermal_antitone (by decide : 3 ≤ 3) ha) 1)
  have ht := hlim.const_add (Real.log B.top)
  rw [add_zero] at ht
  apply ht.congr'
  filter_upwards [eventually_ge_atTop 3] with a ha
  rw [B.log_weight, add_div, mul_div_cancel_left₀ _ (by exact_mod_cast (show a ≠ 0 by omega))]

/-- Infimum of the energies of the excited states with positive eigenvalue.
A box whose excited eigenvalues are all zero has gap +∞. -/
def gap : EReal := ⨅ i, if 0 < B.ratio i then (Real.log (1 / B.ratio i) : EReal) else ⊤

/-- A bound on every relative eigenvalue at time N gives the gap itself.
At a zero seed the extended-real conclusion is +∞. -/
theorem gap_of_pow_bound {N : ℕ} (hN : 0 < N) {q : ℝ}
    (h : ∀ i, B.ratio i ^ N ≤ q) :
    (if q = 0 then ⊤ else ((Real.log (1 / q) / N : ℝ) : EReal)) ≤ B.gap := by
  apply le_iInf
  intro i
  by_cases hi : 0 < B.ratio i
  · rw [if_pos hi]
    have hq' := lt_of_lt_of_le (pow_pos hi N) (h i)
    rw [if_neg hq'.ne', EReal.coe_le_coe_iff]
    have hlog := Real.log_le_log (pow_pos hi N) (h i)
    rw [Real.log_pow] at hlog
    simp only [one_div, Real.log_inv]
    apply (div_le_iff₀ (by exact_mod_cast hN)).2
    linarith
  · simp [hi]

#print axioms summable
#print axioms thermal_nonneg
#print axioms member_le
#print axioms thermal_antitone
#print axioms thermal_add
#print axioms weight_pos
#print axioms weight_add
#print axioms log_weight
#print axioms log_weight_limit
#print axioms gap_of_pow_bound

end BoxSpectrum

/-- A spatial box with three independently variable periods. -/
structure Box where
  x : ℕ
  y : ℕ
  z : ℕ

inductive Axis | x | y | z

def Box.Valid (R : Box) : Prop := 3 ≤ R.x ∧ 3 ≤ R.y ∧ 3 ≤ R.z

def Box.replace (R : Box) (i : Axis) (b : ℕ) : Box :=
  match i with
  | .x => { R with x := b }
  | .y => { R with y := b }
  | .z => { R with z := b }

def cube (b : ℕ) : Box := ⟨b, b, b⟩

/-- Rectangular trace data. Exchanging time with any spatial direction is the
only symmetry used. The bulk lower bound may depend on the spectators.
The spectra determine the trace weights. Axis exchange and the lower bound
are hypotheses on the family of boxes, and log-convexity is taken from Lemma A. -/
structure TorusData where
  spectrum : Box → BoxSpectrum
  cross : ∀ R : Box, R.Valid → ∀ i a b, 3 ≤ a → 3 ≤ b →
    (spectrum (R.replace i b)).weight a = (spectrum (R.replace i a)).weight b
  logConvex : ∀ R : Box, R.Valid → ∀ a, 3 ≤ a →
    (spectrum R).weight (a + 1) ^ 2 ≤ (spectrum R).weight a * (spectrum R).weight (a + 2)
  lower : ∀ R : Box, R.Valid → ∀ i, ∃ d : ℝ, ∀ a b : ℕ, 3 ≤ a → 3 ≤ b →
    d * a * b ≤ Real.log ((spectrum (R.replace i b)).weight a)

namespace TorusData

variable (T : TorusData)

/-- The pair weight for one crossing. The unchanged sides are held fixed
throughout the associated infima and limits. -/
def pair (R : Box) (hR : R.Valid) (i : Axis) : PairWeight where
  W a b := (T.spectrum (R.replace i b)).weight a
  pos := fun _ _ => BoxSpectrum.weight_pos _ _
  swap := fun ha hb => T.cross R hR i _ _ ha hb
  submul := fun ha hc _ => BoxSpectrum.weight_add _ ha hc
  logConvex := fun {a b} ha hb => T.logConvex _ (by cases i <;> simp_all [Box.Valid, Box.replace]) a ha
  lower := by
    obtain ⟨d, hd⟩ := T.lower R hR i
    exact ⟨d, fun ha hb => hd _ _ ha hb⟩

theorem pair_thermal (R : Box) (hR : R.Valid) (i : Axis) {a b : ℕ} (hb : 3 ≤ b) :
    (T.pair R hR i).thermal a b = (T.spectrum (R.replace i b)).thermal a := by
  let B := T.spectrum (R.replace i b)
  have he : (T.pair R hR i).ground b = Real.log B.top :=
    tendsto_nhds_unique ((T.pair R hR i).ground_limit hb) B.log_weight_limit
  unfold PairWeight.thermal PairWeight.g
  rw [he]
  change Real.exp (Real.log (B.weight a) - a * Real.log B.top) - 1 = B.thermal a
  rw [B.log_weight, add_sub_cancel_left, Real.exp_log (by linarith [B.thermal_nonneg a])]
  ring

/-- At time a, increasing a single side from 2a to any period up to 4a
costs at most the fourth power. -/
theorem enlarge_side (R : Box) (hR : R.Valid) (i : Axis) {a L : ℕ} (ha : 3 ≤ a)
    (hlo : 2 * a ≤ L) (hhi : L ≤ 4 * a) :
    1 + (T.spectrum (R.replace i L)).thermal a ≤
      (1 + (T.spectrum (R.replace i (2 * a))).thermal a) ^ 4 := by
  have hb : 3 ≤ 2 * a := by omega
  have h := (T.pair R hR i).lemmaE' ha (show a < 2 * a by omega) hlo
  rw [T.pair_thermal R hR i (hb.trans hlo), T.pair_thermal R hR i hb] at h
  have hratio : (L : ℝ) / ((↑(2 * a : ℕ) : ℝ) - a) ≤ 4 := by
    push_cast
    have ha' : (0 : ℝ) < a := by exact_mod_cast (show 0 < a by omega)
    apply (div_le_iff₀ (by linarith)).2
    have h4 : (L : ℝ) ≤ 4 * a := by exact_mod_cast hhi
    linarith
  calc
    _ ≤ _ := h
    _ ≤ (1 + (T.spectrum (R.replace i (2 * a))).thermal a) ^ (4 : ℝ) :=
      Real.rpow_le_rpow_of_exponent_le
        (by linarith [(T.spectrum (R.replace i (2 * a))).thermal_nonneg a]) hratio
    _ = _ := by norm_num

/-- Three successive crossings, retaining the new spectator periods at each step. -/
theorem cube_enlarge {a L : ℕ} (ha : 3 ≤ a) (hlo : 2 * a ≤ L) (hhi : L ≤ 4 * a) :
    1 + (T.spectrum (cube L)).thermal a ≤ (1 + (T.spectrum (cube (2 * a))).thermal a) ^ 64 := by
  let b := 2 * a
  have hb : 3 ≤ b := by dsimp [b]; omega
  have hL : 3 ≤ L := hb.trans hlo
  let R₀ := cube b
  let R₁ : Box := ⟨L, b, b⟩
  let R₂ : Box := ⟨L, L, b⟩
  have hx : 1 + (T.spectrum R₁).thermal a ≤ (1 + (T.spectrum R₀).thermal a) ^ 4 :=
    T.enlarge_side R₀ ⟨hb, hb, hb⟩ .x ha hlo hhi
  have hy : 1 + (T.spectrum R₂).thermal a ≤ (1 + (T.spectrum R₁).thermal a) ^ 4 :=
    T.enlarge_side R₁ ⟨hL, hb, hb⟩ .y ha hlo hhi
  have hz : 1 + (T.spectrum (cube L)).thermal a ≤ (1 + (T.spectrum R₂).thermal a) ^ 4 :=
    T.enlarge_side R₂ ⟨hL, hL, hb⟩ .z ha hlo hhi
  have pos (R : Box) : 0 ≤ 1 + (T.spectrum R).thermal a := by
    linarith [(T.spectrum R).thermal_nonneg a]
  calc
    _ ≤ _ := hz
    _ ≤ ((1 + (T.spectrum R₁).thermal a) ^ 4) ^ 4 := pow_le_pow_left₀ (pos R₂) hy 4
    _ ≤ (((1 + (T.spectrum R₀).thermal a) ^ 4) ^ 4) ^ 4 :=
      pow_le_pow_left₀ (pow_nonneg (pos R₁) _) (pow_le_pow_left₀ (pos R₁) hx 4) 4
    _ = _ := by rw [← pow_mul, ← pow_mul]

/-- The thermal sum in the aspect ratio used by the seed. -/
def seed (n : ℕ) : ℝ := (T.spectrum (cube (2 * n))).thermal n

/-- Theorem S, one doubling. E′ changes the three spatial sides, then the
counting sum on the final box supplies the square when time doubles. -/
theorem theoremS_step {n : ℕ} (hn : 3 ≤ n) :
    T.seed (2 * n) ≤ ((1 + T.seed n) ^ 64 - 1) ^ 2 := by
  let B := T.spectrum (cube (4 * n))
  have h := T.cube_enlarge hn (show 2 * n ≤ 4 * n by omega) (le_refl (4 * n))
  have hb : B.thermal n ≤ (1 + T.seed n) ^ 64 - 1 := by
    change 1 + B.thermal n ≤ (1 + T.seed n) ^ 64 at h
    linarith
  have hs := B.thermal_add hn hn
  unfold seed
  rw [show 2 * (2 * n) = 4 * n by omega]
  calc
    _ = B.thermal (n + n) := by rw [two_mul]
    _ ≤ B.thermal n ^ 2 := by simpa only [sq] using hs
    _ ≤ _ := pow_le_pow_left₀ (B.thermal_nonneg n) hb 2

/-- Exact arithmetic for the constant 71. Telescoping the powers bounds
each increment by x(641/640)^63 on the entire interval [0,1/640]. -/
theorem seed_polynomial {x : ℝ} (hx : 0 ≤ x) (hsmall : x ≤ 1 / 640) :
    (1 + x) ^ 64 - 1 ≤ 71 * x := by
  have hbase : 1 + x ≤ 641 / 640 := by linarith
  have h (k : ℕ) (hk : k ≤ 64) :
      (1 + x) ^ k ≤ 1 + (k : ℝ) * (641 / 640 : ℝ) ^ 63 * x := by
    induction k with
    | zero => simp
    | succ k ih =>
      have hl := ih (by omega)
      have hy : (1 + x) ^ k ≤ (641 / 640 : ℝ) ^ 63 :=
        (pow_le_pow_left₀ (by linarith) hbase k).trans
          (pow_le_pow_right₀ (by norm_num) (by omega))
      rw [pow_succ]
      push_cast
      nlinarith only [hl, mul_le_mul_of_nonneg_right hy hx]
  have hnum : 64 * (641 / 640 : ℝ) ^ 63 ≤ 71 := by norm_num
  have h64 := h 64 (by decide)
  norm_num only [Nat.cast_ofNat] at h64
  linarith only [h64, mul_le_mul_of_nonneg_right hnum hx]

/-- Iterating the exact quadratic bound while the seed stays below 1/5041. -/
theorem dyadic_thermal {N : ℕ} (hN : 3 ≤ N) (hseed : T.seed N < 1 / 5041) (k : ℕ) :
    5041 * T.seed (2 ^ k * N) ≤ (5041 * T.seed N) ^ (2 ^ k) := by
  let q := 5041 * T.seed N
  have hq : 0 ≤ q := mul_nonneg (by norm_num) ((T.spectrum (cube (2 * N))).thermal_nonneg N)
  have hq1 : q ≤ 1 := by dsimp [q]; linarith
  induction k with
  | zero => simp
  | succ k ih =>
    let a := 2 ^ k * N
    have ha : 3 ≤ a := hN.trans (Nat.le_mul_of_pos_left _ (by positivity))
    have hs := (T.spectrum (cube (2 * a))).thermal_nonneg a
    change 0 ≤ T.seed a at hs
    change 5041 * T.seed a ≤ q ^ (2 ^ k) at ih
    have hb := seed_polynomial hs (by linarith [pow_le_one₀ (n := 2 ^ k) hq hq1])
    have hpos : 0 ≤ (1 + T.seed a) ^ 64 - 1 :=
      sub_nonneg.mpr (one_le_pow₀ (by linarith) : (1 : ℝ) ≤ (1 + T.seed a) ^ 64)
    rw [show 2 ^ (k + 1) * N = 2 * a by dsimp [a]; ring]
    calc
      _ ≤ 5041 * (((1 + T.seed a) ^ 64 - 1) ^ 2) :=
        mul_le_mul_of_nonneg_left (T.theoremS_step ha) (by norm_num)
      _ ≤ 5041 * (71 * T.seed a) ^ 2 :=
        mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hpos hb 2) (by norm_num)
      _ = (5041 * T.seed a) ^ 2 := by ring
      _ ≤ (q ^ (2 ^ k)) ^ 2 := pow_le_pow_left₀ (by positivity) ih 2
      _ = _ := by rw [← pow_mul, pow_succ 2 k]

/-- S3′, the thermal estimate in each interval 2a ≤ L < 4a, a = 2^k N.
The same proof allows the upper endpoint. -/
theorem intermediate_thermal {N : ℕ} (hN : 3 ≤ N) (hseed : T.seed N < 1 / 5041)
    (k L : ℕ) (hlo : 2 * (2 ^ k * N) ≤ L) (hhi : L ≤ 4 * (2 ^ k * N)) :
    (T.spectrum (cube L)).thermal (2 ^ k * N) ≤ (5041 * T.seed N) ^ (2 ^ k) / 71 := by
  let a := 2 ^ k * N
  have ha : 3 ≤ a := hN.trans (Nat.le_mul_of_pos_left _ (by positivity))
  have hs : 0 ≤ T.seed a := (T.spectrum (cube (2 * a))).thermal_nonneg _
  have hq : 0 ≤ 5041 * T.seed N := mul_nonneg (by norm_num) ((T.spectrum _).thermal_nonneg _)
  have hdy := T.dyadic_thermal hN hseed k
  change 5041 * T.seed a ≤ _ at hdy
  have hq1 : 5041 * T.seed N ≤ 1 := by linarith
  have hpol := seed_polynomial hs (by linarith [pow_le_one₀ (n := 2 ^ k) hq hq1])
  have hen := T.cube_enlarge ha hlo hhi
  change 1 + (T.spectrum (cube L)).thermal a ≤ (1 + T.seed a) ^ 64 at hen
  change (T.spectrum (cube L)).thermal a ≤ _
  linarith

/-- The inverse-time lower bound in lattice units with the zero-seed case interpreted
in extended reals. For a positive seed it is log(1/(5041 s))/N. -/
def seedRate (N : ℕ) : EReal :=
  if 5041 * T.seed N = 0 then ⊤ else ((Real.log (1 / (5041 * T.seed N)) / N : ℝ) : EReal)

/-- Corollary S3′. Every integer side L ≥ 2N has the same lower bound from
one seed. The dyadic interval brackets L without requiring divisibility. -/
theorem corollaryS3' {N : ℕ} (hN : 3 ≤ N) (hseed : T.seed N < 1 / 5041)
    {L : ℕ} (hL : 2 * N ≤ L) : T.seedRate N ≤ (T.spectrum (cube L)).gap := by
  have hN' : (0 : ℝ) < N := by exact_mod_cast (show 0 < N by omega)
  have hbase : (0 : ℝ) < 2 * N := by positivity
  have hL' : (2 : ℝ) * N ≤ L := by exact_mod_cast hL
  obtain ⟨k, hk₁, hk₂⟩ := exists_nat_pow_near ((one_le_div hbase).2 hL') (by norm_num : (1 : ℝ) < 2)
  have hlo : 2 * (2 ^ k * N) ≤ L := by
    exact_mod_cast (show (2 : ℝ) * (2 ^ k * N) ≤ L by linarith only [(le_div_iff₀ hbase).1 hk₁])
  have hhi : L ≤ 4 * (2 ^ k * N) := by
    have hx := (div_lt_iff₀ hbase).1 hk₂
    rw [pow_succ] at hx
    exact_mod_cast (show (L : ℝ) ≤ 4 * (2 ^ k * N) by linarith only [hx])
  let B := T.spectrum (cube L)
  let q := 5041 * T.seed N
  have hq : 0 ≤ q := mul_nonneg (by norm_num) ((T.spectrum _).thermal_nonneg _)
  apply B.gap_of_pow_bound (q := q) (by omega : 0 < N)
  intro i
  have ha : 3 ≤ 2 ^ k * N := hN.trans (Nat.le_mul_of_pos_left _ (by positivity))
  have hi := (B.member_le ha i).trans (T.intermediate_thermal hN hseed k L hlo hhi)
  have hp : (B.ratio i ^ N) ^ (2 ^ k) ≤ q ^ (2 ^ k) := by
    rw [← pow_mul, Nat.mul_comm N]
    change B.ratio i ^ (2 ^ k * N) ≤ q ^ (2 ^ k) / 71 at hi
    linarith [pow_nonneg hq (2 ^ k)]
  exact (pow_le_pow_iff_left₀ (pow_nonneg (B.nonneg i) N) hq (by positivity : 2 ^ k ≠ 0)).1 hp

/-- Theorem S, thermal decay and gap on every dyadic cube from the given seed. -/
theorem theoremS {N : ℕ} (hN : 3 ≤ N) (hseed : T.seed N < 1 / 5041) (k : ℕ) :
    T.seed (2 ^ k * N) ≤ (5041 * T.seed N) ^ (2 ^ k) / 5041 ∧
      T.seedRate N ≤ (T.spectrum (cube (2 * (2 ^ k * N)))).gap := by
  constructor
  · linarith [T.dyadic_thermal hN hseed k]
  · apply T.corollaryS3' hN hseed
    exact Nat.mul_le_mul_left _ (Nat.le_mul_of_pos_left _ (by positivity))

/-- Doubling one spatial period costs at most a factor two in log W. -/
private theorem log_space_double (R : Box) (hR : R.Valid) (i : Axis)
    {a b : ℕ} (ha : 3 ≤ a) (hb : 3 ≤ b) :
    Real.log ((T.spectrum (R.replace i (2 * b))).weight a) ≤
      2 * Real.log ((T.spectrum (R.replace i b)).weight a) := by
  rw [T.cross R hR i a (2 * b) ha (by omega), T.cross R hR i a b ha hb]
  let B := T.spectrum (R.replace i a)
  have h := Real.log_le_log (B.weight_pos _) (B.weight_add hb hb)
  rw [Real.log_mul (B.weight_pos b).ne' (B.weight_pos b).ne'] at h
  simpa [B, two_mul] using h

/-- The two partition functions in the alternative pressure seed. -/
def phi (n : ℕ) : ℝ :=
  16 * Real.log ((T.spectrum (cube n)).weight n) -
    Real.log ((T.spectrum (cube (2 * n))).weight (2 * n))

/-- Theorem D(b), used in the last clause of Theorem S. -/
theorem log_seed_le_phi {n : ℕ} (hn : 3 ≤ n) : Real.log (1 + T.seed n) ≤ T.phi n := by
  let b := 2 * n
  let R₀ := cube n
  let R₁ : Box := ⟨b, n, n⟩
  let R₂ : Box := ⟨b, b, n⟩
  let B := T.spectrum (cube b)
  have hb : 3 ≤ b := by dsimp [b]; omega
  have hx : Real.log ((T.spectrum R₁).weight n) ≤ 2 * Real.log ((T.spectrum R₀).weight n) :=
    T.log_space_double R₀ ⟨hn, hn, hn⟩ .x hn hn
  have hy : Real.log ((T.spectrum R₂).weight n) ≤ 2 * Real.log ((T.spectrum R₁).weight n) :=
    T.log_space_double R₁ ⟨hb, hn, hn⟩ .y hn hn
  have hz : Real.log (B.weight n) ≤ 2 * Real.log ((T.spectrum R₂).weight n) :=
    T.log_space_double R₂ ⟨hb, hb, hn⟩ .z hn hn
  have hlog := Real.log_le_log (by linarith [B.thermal_nonneg (2 * n)] : 0 < 1 + B.thermal (2 * n))
    (add_le_add_right (B.thermal_antitone hn (show n ≤ 2 * n by omega)) 1)
  have ht : Real.log (1 + B.thermal n) ≤ 2 * Real.log (B.weight n) - Real.log (B.weight (2 * n)) := by
    simp only [B.log_weight, Nat.cast_mul, Nat.cast_ofNat]
    linarith only [hlog]
  change Real.log (1 + B.thermal n) ≤ 16 * Real.log ((T.spectrum R₀).weight n) -
    Real.log (B.weight (2 * n))
  linarith only [hx, hy, hz, ht]

/-- The exact decimal pressure threshold 0.00019 implies the strict thermal seed. -/
theorem seed_of_phi {n : ℕ} (hn : 3 ≤ n) (h : T.phi n ≤ 19 / 100000) :
    T.seed n < 1 / 5041 := by
  let x : ℝ := 19 / 100000
  have hx : 1 + T.seed n ≤ Real.exp x := by
    have := Real.exp_le_exp.mpr ((T.log_seed_le_phi hn).trans h)
    have hs : 0 ≤ T.seed n := (T.spectrum _).thermal_nonneg _
    rwa [Real.exp_log (by linarith : 0 < 1 + T.seed n)] at this
  have ht := Real.add_one_le_exp (-x)
  rw [Real.exp_neg] at ht
  have hu := mul_le_mul_of_nonneg_left ht (Real.exp_pos x).le
  rw [mul_inv_cancel₀ (Real.exp_pos x).ne'] at hu
  change Real.exp x * (-(19 / 100000 : ℝ) + 1) ≤ 1 at hu
  linarith only [hx, hu]

#print axioms pair_thermal
#print axioms enlarge_side
#print axioms cube_enlarge
#print axioms theoremS_step
#print axioms seed_polynomial
#print axioms dyadic_thermal
#print axioms intermediate_thermal
#print axioms corollaryS3'
#print axioms theoremS
#print axioms log_space_double
#print axioms log_seed_le_phi
#print axioms seed_of_phi

end TorusData
end GapChain
