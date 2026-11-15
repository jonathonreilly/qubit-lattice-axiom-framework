# hi55_b — arithmetic of the reductions (criteria, written before the script)

Owner: HINT55.md (model claude-opus-5-5). Written 2026-10-28 after HINT55 PRE-STATED, before `hi55_b_reduction.py`
exists. Plain Python, `fractions.Fraction` only. The symbol ℓ stands for log L; every statement tested holds for every
ℓ > 0, so ℓ is drawn as a positive rational (including the rational 10986/10000 < ln 3). Seed `random.Random(5502)`.

Notation (HINT55 §4): levels are counted by m = k₀ − k ≥ 0 below the observation level k₀; u_m := 1/g² at level k₀ − m.

**B1 (Theorem H-RED, vanishing-charge form).** Parameters drawn: 0 < c₋ ≤ C₊, β₋ > 0, R ≥ 0, u₀ ≥ 1 + R (so every
u_m > 0), θ ∈ {0, 1/2}. Threshold m₁ := the least integer m ≥ 0 with (u₀ + β₋mℓ − R)^{1−θ} ≥ 2C₊u₀/c₋ (for θ = 1/2 tested
in the squared form u₀ + β₋mℓ − R ≥ (2C₊u₀/c₋)²). Adversarial data: f₀ := c₋/u₀ (the least value (TS-low) allows),
u_m := u₀ + β₋mℓ − R + s_m with slack s_m ∈ {0} ∪ random nonnegative rationals (s_m = 0 is the slowest running (F_R)
allows), f_m := C₊u_m^{θ−1} (the largest value (TS-up) allows). Claim tested: for every m ≥ m₁ (checked for
m = m₁, …, m₁ + 40), f_m ≤ c₋/(2u₀) (θ = 1/2: C₊² ≤ (c₋/(2u₀))²u_m), hence W := f₀ − f_{m₁} ≥ c₋/(2u₀). 300 parameter
sets. PASS iff no violation.
**B1-F (designed fail).** For every parameter set with m₁ ≥ 1 and zero slack, the inequality f_m ≤ c₋/(2u₀) FAILS at
m = m₁ − 1 (minimality of m₁ makes the threshold sharp on the adversarial instance). PASS of the control iff it fails in
every such set and at least 50 such sets occur. Also m = 0 always gives W = 0 < c₋/(2u₀).

**B2 (Theorem H-RED-sharp, matched-constant form).** Parameters: A > 0, β₋ > 0, R ≥ 0, C ≥ 0 (= C_sch), u₁ ≥ 1 + C + R.
Δ₀ := the least integer Δ with β₋Δℓ > R + 2C. Adversarial data for Δ ≥ Δ₀: u₂ := u₁ − β₋Δℓ + R (the smallest running
(F_R) allows; requires u₂ > C, sets violating it are redrawn), v₁ := u₁ − C, v₂ := u₂ + C (worst matching errors),
W := A(1/v₂ − 1/v₁) (here level 2 is the coarser one, u₂ < u₁). Claim: W ≥ A(β₋Δℓ − R − 2C)/((u₁ + C)(u₂ + C)) > 0, and
W is minimal over the 4 corner choices v_i ∈ {u_i ± C}. 300 sets, Δ ∈ {Δ₀, Δ₀ + 1, Δ₀ + 5}. PASS iff no violation.
**B2-F (designed fail).** At Δ = Δ₀ − 1 ≥ 1 with the same adversarial choice, W ≤ 0. PASS of the control iff W ≤ 0 in
every such set (at least 50).

Verdict: PASS iff B1, B2 PASS and B1-F, B2-F behave as stated. Load-bearing: the explicit thresholds m₁, Δ₀ and the lower
bounds quoted in HINT55 §4 (Theorems H-RED, H-RED-sharp). The checks test the arithmetic of the implications on worst
cases, not any Yang-Mills input.
