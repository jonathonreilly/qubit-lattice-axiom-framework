# b2_55_1 — criteria (written before the script; B2_55 §2.3, §2.4 Remark, §4.1, §5)

Reviewer/worker model: claude-opus-5-5. Plain python, exact rational arithmetic only (fractions.Fraction); exponentials and
ln 2 by rigorous rational enclosures (alternating Taylor partial sums with outward rounding; ln 2 = Σ 1/(n2^n) with tail bound).
No floats in any verdict. Floats may appear only in printed human-readable decimals after a verdict is fixed.

## Gate A — Lemma LS (1D lattice sum on a torus), the only computational lemma of Theorem B2
Cases: μ ∈ {1/10000, 1/100, 1/7, 1, 3}; h ∈ {1, 1/3, 1/9, 1/27}; T ∈ {3, 4, 5}; offsets a ∈ {0, h/3, h/2, 2h/3}; p = 0.
Grid G = {a + nh mod T : 0 ≤ n < T/h}; d_T(z, 0) := min(z mod T, T − (z mod T)).
For each case compute rigorous enclosures of S := Σ_{z∈G} e^{−μ d_T(z,0)}, of the plane closed form
P := (e^{−μt₀} + e^{−μ(h−t₀)})/(1 − e^{−μh}) (t₀ := a mod h), and of B₁ := 2/(1 − e^{−μh}); B₂ := 2(1 + 1/(μh)) (exact).
- **A PASS iff for every case: upper(S) ≤ lower(P), upper(P) ≤ lower(B₁), upper(B₁) ≤ B₂.**
- **A-ctl (designed FAIL; must fire):** the false bound S ≤ 1 + 1/(μh) (factor 2 dropped) must be violated, i.e. lower(S) > 1 + 1/(μh),
  in at least one case. Predicted to fire at μ = 1, h ∈ {1/9, 1/27}, T = 5. If it does not fire, the gate is reported as unable to
  discriminate.

## Gate D — the size statement of §2.4 Remark
m_Y := ln 2/(16L^c) with L^c ≥ 260 (BFT34_55 §0.2). With a certified upper bound u ≥ ln 2: m_Y ≤ u/4160 =: m̄.
- **D PASS iff (1 + 1/m̄)² ≥ 36 000 000** (then (1 + 1/μ)² ≥ 3.6·10⁷ for every 0 < μ ≤ m_Y). Also print m̄ to 6 digits.
- D-ctl: with the rounded value 1.67·10⁻⁴ in place of m̄, (1 + 1/(1.67·10⁻⁴))² ≥ 3.6·10⁷ must be FALSE (fires: shows the rounded
  intermediate printed in §2.4 is too loose to derive the statement; erratum).

## Gate E — the error-sum closed forms of §4.1 and the weight tolerances of §5 (arithmetic only)
Cases: (L, σ) ∈ {(3, 1), (5, 1), (7, 1), (9, 1/2)} (L^σ rational in every case); k = 1, …, 60.
- E1: Σ_{j=0}^{k−1} L^{−(2+σ)(k−1−j)}L^{2(k−j)} = L²Σ_{q=0}^{k−1}L^{−σq} exactly, and ≤ L²/(1 − L^{−σ}).
- E2: STEP55's printed form Σ_{j=0}^{k−1}L^{−(2+σ)(k−j)}L^{2(k−j)} equals E1's sum divided by L^{2+σ} exactly.
- E3: Σ_{j=0}^{k−1}L^{−2(k−j)}L^{k−j} ≤ 1/(L − 1), and Σ_{q≥1}L^{−3q}L^{2q}-type η² term Σ_{j<k}L^{−3(k−j)}L^{2(k−j)} ≤ 1/(L − 1).
- **E PASS iff E1, E2, E3 hold for every case and every k.**
- E-ctl1 (must fire): with the weight L^{(1+σ/2)(k−j)} in place of L^{k−j}, the mismatch sum equals k·L^{2+σ} exactly for every k
  (linear growth), so it exceeds L²/(1 − L^{−σ}) by a factor ≥ 30 at k = 60.
- E-ctl2 (must fire): with the level-0 weight L^{(1+a)k}, a = 1/2, L = 9 (σ irrelevant), the spin factor L^{−2k}L^{2(1+a)k} = L^{2ak} = 9^k
  exceeds 10⁶ at some k ≤ 60.

## Overall
PASS iff A, D, E all PASS and A-ctl, D-ctl, E-ctl1, E-ctl2 all fire. stderr must be empty.
What this check can and cannot decide: A can fail if Lemma LS's inequality chain is false for one of these cases (it is the
only computational input of Theorem B2's constant); D can fail if the size statement is wrong; E can fail only if a closed
form written in §4.1/§5 is wrong (arithmetic). None of A, D, E tests (H1), (H2)_μ, Lemma WD, or STEP55's ARGUED term bounds.
