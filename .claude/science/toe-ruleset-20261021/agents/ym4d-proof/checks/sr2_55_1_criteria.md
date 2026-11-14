# sr2_55_1 — pre-registered criteria (written 2026-10-29 ≈06:20Z, BEFORE the script exists)

Owner: SRC2_55.md (Opus 5.5 worker). Plain python3, `python3 -I -B`, integers and fractions.Fraction only (no floats, no
numpy). Every exponential is enclosed by rigorous rational bounds: for rational x ≥ 0 and N ≥ 2x,
  EU(x) := 1/P_N(x) ≥ e^{−x},  EL(x) := 1/(P_N(x) + x^{N+1}/((N+1)!·(1 − x/(N+2)))) ≤ e^{−x},  P_N(x) := Σ_{k≤N} x^k/k!.
Output: stdout only (redirected by the runner to sr2_55_1_out.txt; stderr to sr2_55_1_err.txt). Final line "VERDICT: PASS" iff
every gate passes AND every control fires; otherwise "VERDICT: FAIL". No file is written by the script.

## Gates (what is claimed in SRC2_55.md and how it is tested)
- **G1 (Theorem I (d): Bell numbers B_n ≤ n!).** Compute B_n exactly (B_0 = 1, B_{n+1} = Σ_k C(n,k)B_k) for n = 1..80; PASS iff
  B_n ≤ n! for every n. **Control C1:** the false bound B_n ≤ (n−1)! must fail for some n (expected: n = 3, 5 > 2).
- **G2 (Proposition NF).** (a) Π_{i=1}^K(1 + 1/i) = K + 1 exactly for K = 1..400; (b) Π_{i=1}^K(1 + 1/i²) < 4 for K = 1..400.
  PASS iff both hold for all K. **Control C2:** the false claim "Π_{i=1}^K(1 + 1/i) ≤ 4 for all K ≤ 400" must fail; **C2b:** the
  false claim "Π_{i=1}^K(1 + 1/i²) < 3 for all K ≤ 400" must fail.
- **G3 (Lemma SSUM).** For (𝔡, L) ∈ {(1/10, 3), (1/2, 3), (1, 3), (2, 3), (1, 5), (4, 7)} and τ ∈ {1, 5/4, 3/2, 2, 5/2, 29/10} with τ < L
  (and also τ = 4, 6 when L = 5, 7): a rigorous rational UPPER bound S⁺(τ) of S(τ) := Σ_{j∈ℤ}(τL^j)⁴e^{−𝔡τL^j/2} (finite range |j| ≤ J
  with EU, plus rigorous tails: j < −J by Σ(τL^j)⁴; j > J by M·Σ_k e^{−𝔡x_{J+1}(1+k(L−1))/4} with M := x_{J+1}⁴EU(𝔡x_{J+1}/4) valid when
  x_{J+1} ≥ 16/𝔡) must be ≤ a rigorous rational LOWER bound Ŝ⁻ of Ŝ(𝔡, L) := L⁴/(L⁴ − 1) + (16/𝔡)⁴e^{−4}e^{−𝔡/4}/(1 − e^{−𝔡(L−1)/4}).
  Also the single-level bound: t⁴·EU(𝔡t/2) ≤ (8/𝔡)⁴·EL(4) at t = 8/𝔡 ± small rational offsets is NOT required (it is calculus);
  only the sum bound is gated. PASS iff S⁺(τ) ≤ Ŝ⁻ for every sample. **Control C3:** the wrong bound L⁴/(L⁴ − 1) (second term
  dropped) must be exceeded by a rigorous LOWER bound S⁻(τ) (finite sum with EL, no tails) for at least one sample.
- **G4 (Proposition HOM).** (a) For 100 pseudo-random Gaussian-rational u ≠ 0 and ε ∉ {±1, 0}: (Σ_p 1/c_p)^{−1} = (u/4)(1 − ε²) exactly,
  c = (u(1+ε), u(1+ε), u(1−ε), u(1−ε)). (b) For 50 pseudo-random real positive rational quadruples c and rational Φ: the Lagrange
  point F_p = Φ/(c_pΣ_q1/c_q) satisfies Σ_pF_p = Φ and its energy ½Σc_pF_p² equals ½Φ²/Σ_p(1/c_p), and is ≤ the energy of each of
  20 random feasible perturbations F + d (Σd = 0, d ≠ 0) — strictly less. (c) Size: at u = 1000, ε = 1/4, C_b = 1000:
  (u/4)ε² > C_b/u. PASS iff (a)-(c) hold. **Control C4:** the claim "c_eff = u/4 (arithmetic) for ε = 1/4, u = 1" must fail.
- **G5 (Theorem I (f) / Corollary II arithmetic).** With (b, p, r) = (1, 2 + α, 1), q_X = 4 and α ∈ {1/10, 1/2, 9/10}: BRIDGE gives
  p_X = 6 + α, r_X = 7, b_X = 23/2; EXT with integer majorants gives s′ = max(⌈r_X + p_X + 7⌉, q_X + 6) = 21 and β′ = b_X + 7r_X + 1 = 123/2;
  the composed formulas s = max(⌈p + r + 17⌉, q_X + 6) = 21, β = b + 19r/2 + 51 = 123/2 must agree. PASS iff all equal.
  **Control C5:** the claims s = 20 and β = 61 must both fail.
- **G6 (Lemma SC (ii)).** In 2D (the lemma's proof is dimension-free), tents f_i(x) = max(0, 1 − |x − c_i|_∞/w_i) with w_i ≥ λ (so
  ‖f_i‖_∞ = 1, Euclidean |∇f_i| = 1/w_i ≤ 1/λ), centres placed so that the supports are ≥ λ apart in Euclidean distance; z_i Gaussian
  rationals with |z_i|² ≤ ζ²; 2000 pseudo-random rational point pairs (half of them inside supports): PASS iff
  |η(x) − η(y)|² ≤ 4ζ²·min(1, |x − y|²/λ²) for every pair (exact squares). **Control C6:** the bound without the factor 2,
  |η(x) − η(y)|² ≤ ζ²·min(1, |x − y|²/λ²), must fail on at least one pair (the sample includes z_1 = ζ, z_2 = −ζ and centre-to-centre pairs).

## What this check can and cannot decide
It certifies the combinatorial constant (Bell ≤ n!), the exact NF products, the SSUM constant at sample parameters (the proof is
in the text), the HOM identity and minimiser in its model, the parameter arithmetic of the OS chain, and Lemma SC on samples. It
cannot decide anything about Yang–Mills, about the inputs (Rep_m^𝒞), (Flow-pos), (LF-src), (Rep^O), or about Theorem I/II's
logic (those are proofs in the text). Each gate has a control that a wrong formula would trip.
