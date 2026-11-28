import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic

/-!
# The sequence lemma (U4)

Scalar form of Lemma A2, row 668 (Claude Opus 5.5), used on the odd
reflection-moment grid in rows 1457–1458. The geometric upper bound may
hold on any unbounded set of indices. The three-term inequality itself
propagates zeros on an infinite sequence. For the reflected-moment inputs,
see UI2–UI3 of the outline by Ethan Sussman and Levent Alpoge, authored
with Claude and Codex (lines 28272–28288).
-/

open Filter
open scoped Topology

namespace GapChain

/-- A geometric envelope at arbitrarily large indices gives the one-step inequality
even at a zero of the sequence or at rate zero. -/
theorem sequenceLemma {m : ℕ → ℝ} {q C : ℝ} (hq : 0 ≤ q)
    (hm : ∀ n, 0 ≤ m n)
    (hconv : ∀ n, m (n + 1) ^ 2 ≤ m n * m (n + 2))
    (henv : ∃ᶠ j in atTop, m j ≤ C * q ^ j) (n : ℕ) :
    m (n + 1) ≤ q * m n := by
  by_contra! hbad
  have hn : 0 < m n := by
    rcases (hm n).eq_or_lt with hz | hp
    · have hc := hconv n
      rw [← hz, zero_mul] at hc
      rw [← hz, mul_zero] at hbad
      nlinarith
    · exact hp
  let r := m (n + 1) / m n
  have hqr : q < r := (lt_div_iff₀ hn).2 hbad
  have hr := lt_of_le_of_lt hq hqr
  have hstep (k : ℕ) : 0 < m (n + k) ∧ r * m (n + k) ≤ m (n + k + 1) := by
    induction k with
    | zero => exact ⟨by simpa using hn, by simp [r, hn.ne']⟩
    | succ k ih =>
      obtain ⟨hx, hxy⟩ := ih
      have hy := lt_of_lt_of_le (mul_pos hr hx) hxy
      refine ⟨hy, (le_of_mul_le_mul_right ?_ hx)⟩
      calc
        r * m (n + k + 1) * m (n + k) =
            (r * m (n + k)) * m (n + k + 1) := by ring
        _ ≤ m (n + k + 1) ^ 2 := by
          simpa [sq] using mul_le_mul_of_nonneg_right hxy hy.le
        _ ≤ m (n + k + 2) * m (n + k) := by simpa [mul_comm] using hconv (n + k)
  have hgrow (k : ℕ) : m n * r ^ k ≤ m (n + k) := by
    induction k with
    | zero => simp
    | succ k ih =>
      calc
        m n * r ^ (k + 1) = r * (m n * r ^ k) := by rw [pow_succ]; ring
        _ ≤ r * m (n + k) := mul_le_mul_of_nonneg_left ih hr.le
        _ ≤ _ := (hstep k).2
  have hlim : Tendsto (fun k : ℕ => C * q ^ n * (q / r) ^ k) atTop (𝓝 0) := by
    simpa using (tendsto_pow_atTop_nhds_zero_of_lt_one (div_nonneg hq hr.le)
      ((div_lt_one hr).2 hqr)).const_mul (C * q ^ n)
  obtain ⟨K, hK⟩ := eventually_atTop.1 (hlim.eventually_lt_const hn)
  obtain ⟨j, hj, hbound⟩ := frequently_atTop.1 henv (n + K)
  let k := j - n
  have hjk : n + k = j := by dsimp [k]; omega
  have hsmall := hK k (by dsimp [k]; omega)
  rw [div_pow, ← mul_div_assoc, div_lt_iff₀ (pow_pos hr k)] at hsmall
  rw [← hjk, pow_add] at hbound
  linarith [hgrow k, show C * (q ^ n * q ^ k) = C * q ^ n * q ^ k by ring]

/-- The all-index envelope used in Stage 1. -/
theorem sequenceLemma_of_bound {m : ℕ → ℝ} {q C : ℝ} (hq : 0 ≤ q)
    (hm : ∀ n, 0 ≤ m n) (hconv : ∀ n, m (n + 1) ^ 2 ≤ m n * m (n + 2))
    (henv : ∀ j, m j ≤ C * q ^ j) (n : ℕ) : m (n + 1) ≤ q * m n :=
  sequenceLemma hq hm hconv (Eventually.of_forall henv).frequently n

#print axioms sequenceLemma
#print axioms sequenceLemma_of_bound

end GapChain
