# h2_55_d — reduction arithmetic: inter-scale lemma, (B-BR) constants, k₁ conversion (criteria, written
# 2026-10-29T03:18Z (file mtime), before any h2_55_d script; header time corrected at 03:19Z — it first said 03:22Z)

Owner: HINT2_55.md (claude-opus-5-5). `fractions.Fraction` and `sympy` exact only; log L is carried as a positive rational
symbol-value ℓ (every inequality below is polynomial in ℓ, so exactness is not lost). nice 10.

## Gates
- **D1 (Lemma INT arithmetic).** Grid t_m := c_t L^{−2m} (c_t ∈ {1, 3/2}, L ∈ {2, 3, 4}, m = 0..6). For 40 fixed
  non-increasing step/rational functions e(t) on (0, c_t] (deterministic list: e(t) = Σ_i w_i·1[t ≤ s_i]·(1 + 1/(1+n_i t)),
  w_i ≥ 0 rational) and 30 rational sample points t in each [t_{m+1}, t_m]: t²e(t) ≤ L⁴·t_{m+1}²e(t_{m+1}). Zero
  violations.
- **D2 (continuous-time threshold).** With U_±(m) := u₀ + b_± m ± R (b_± := β_±ℓ > 0, rationals; u₀ = g^{−2}),
  ϑ ∈ {0, 1/3, 1/2, 2/3}, define m₁^c := least m ≥ m₀ with U₋(m+1)^{1−ϑ} ≥ 2L⁴C₊U₊(m₀)/c₋ (compared as integer powers:
  ϑ = p/q ⇒ U^{q−p} ≥ X^q). For 200 parameter sets: (i) the inequality holds at every m ∈ [m₁^c, m₁^c + 40];
  (ii) m₁^c ≥ m₁′ − 1 where m₁′ := least m ≥ m₀ with U₋(m)^{1−ϑ} ≥ 2C₊U₊(m₀)/c₋ (H-RED′'s threshold), i.e. the inter-scale
  factor never lowers the threshold by more than the one-step index shift.
- **D3 ((B-BR) ⇒ F-flow constants).** For 200 rational sets (β′ > 0, β″ ≥ β′, C_ργ², ℓ) with C_ργ² ≤ ½β′ℓ:
  β₋ := β′ − C_ργ²/ℓ ≥ β′/2 > 0 and β₊ := β″ + C_ργ²/ℓ ≤ β″ + β′/2.
- **D4 (k₁ conversion, Codex §3).** With α = g²/(4π): A g²(1 + k_g g²) ≡ A·4πα(1 + k_α α) iff k_α = 4πk_g (symbolic);
  and (4/b₀)·(N/(16π²))·(11γ/3 + 52/9 − 3Λ) with b₀ = 11N/(48π²) equals 4γ + 208/33 − (36/11)Λ (γ, Λ symbols).

## Designed-FAIL controls
- **D1-F** an increasing e(t) = 1 + t (on the same grid) must violate D1 for some (m, t).
- **D2-F** at m₁^c − 1 (when m₁^c > m₀) the threshold inequality must fail (sharpness of the least index; registered as a
  sanity control of the implementation, not as mathematical content).
- **D3-F** C_ργ² = β′ℓ gives β₋ = 0 (must be reported as a violation of β₋ > 0).
- **D4-F** using k_α in place of k_g (no 4π) gives a different coefficient (must be reported unequal).

PASS = all gates hold and all four controls fire.
