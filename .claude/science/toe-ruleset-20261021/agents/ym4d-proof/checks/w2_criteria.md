# w2 criteria (lane H, session 2). Written 2026-10-28 04:00 UTC, BEFORE the script w2_relseq_toy.py exists.
Informational check; never a proof. One run planned (deterministic, fixed seeds), under the mandatory numeric lock,
nice 10, BLAS/OMP threads = 1, no `timeout`. Output must be < 6000 chars.

## A. Capped inequalities (Lemma CAP of §14)
- A1: for 10^6 random (a, b, π) with a, b ≥ 0, π > 0 (log-uniform scales 1e-6 .. 1e6): min(π, a + b) ≤ a + min(π, b). PASS iff
  zero violations (tolerance 1e-12 relative).
- A2: capped Chernoff: for random X ≥ 0, π > 0, θ > 0: 1{X ≥ π} ≤ exp(θ(min(X, π) - π)). PASS iff zero violations.
- A3 (negative control): the false split min(π, a + b) ≤ min(π/2, a) + min(π/2, b) must FAIL on some sample.

## B. Lemma REL-seq on an exactly enumerable toy
Lattice: 4×4 torus-free square grid (16 sites), *-adjacency (8 neighbours). A configuration is a defect set D ⊂ sites (2^16).
Laws: (L1) independent Bernoulli(p), p ∈ {0.02, 0.05, 0.1, 0.2}; (L2) correlated (attractive) W ∝ exp(J·#{*-adjacent defect
pairs} + h|D|), (J, h) ∈ {(0.5, -3), (1.0, -4), (0.3, -2.5)}. Threshold n_♯ ∈ {1, 2}.
"History": a relaxed region U (fixed: the 2×2 block at the corner, and its *-neighbourhood N_1(U)), S_0 := sites ∖ N_1(U);
R_S := {every *-component of D ∩ S has ≤ n_♯ sites}. Relax the sites of N_1(U) one at a time in a fixed order (and in a
second, reversed order) to S_final = all sites.
- B1 (identity): Z(R_all)/Z(R_{S_0}) = Π_i μ_{R_{S_i}}(R_{S_{i+1}}) to 1e-12 relative. PASS iff all cases.
- B2 (step containment, S2-F1): on R_{S_i} ∖ R_{S_{i+1}} the added site x is a defect and lies in a *-connected all-defect
  subset of S_{i+1} with exactly n_♯ + 1 sites containing x. PASS iff zero exceptions over all configs and steps.
- B3 (the REL-seq bound with the exact step prices): with p_i := Σ_{𝒟 ∋ x_i, |𝒟| = n_♯+1, *-conn, 𝒟 ⊂ S_{i+1}} μ_{R_{S_i}}(𝒟 ⊂ D)
  (the union bound, computed exactly), whenever max p_i ≤ 1/2: log(Z(R_all)/Z(R_{S_0})) ≥ -2Σ_i p_i. PASS iff all cases.
  Also the declared-set inequality (Lemma DECL): μ_{R_{S_i}}(𝒟 ⊂ D) ≤ μ_{R_{S_i, 𝒟}}(𝒟 ⊂ D) for every 𝒟 in the union. PASS iff
  zero violations.
- B4 (negative control): the bound with the animal count removed, log ratio ≥ -2·Σ_i max_𝒟 μ_{R_{S_i}}(𝒟 ⊂ D), must FAIL in at
  least one case (otherwise the check does not see the union over animals). Report tightness log-ratio / (-2Σp_i).
- B5: the order of relaxation does not matter for B1-B3 (both orders PASS).

## C. Arithmetic of §13-§15 at the recorded constants (prints only; PASS = formulas evaluate as stated)
- C1: REL-seq depth term: for c ∈ {0.1, 1}, a ∈ {1e-17, 1e-23}, β_- ∈ {0.19, 0.37}, L = 3: n_H := floor((4 + 38416c/log L)/(aβ_-)) and
  check (n_H + 1)aβ_- log L ≥ 38416c (the condition that absorbs e^{38416c(K-1-j)}).
- C2: LOOP-const: per-level growth factor G := 81·L^{-θ a β_+}e^{-θ a R} for θ ∈ {1/6, 1/100}, a ∈ {2.3e-16, 5e-23}, β_+ ∈
  {0.56, 1, 10}, R ∈ {0, 1}: report G and G^K for K = 100. PASS iff G > 1 in every case (the claimed divergence).
- C3: LOOP-div: minimal depth m_* at which ρ_0^m θ_K u_K/(u_K + β_+ m log L + R) > 1/ρ_0 for ρ_0 ∈ {4, 24, 96}, θ_K = 1/(2ρ_0),
  g_K² ∈ {0.1, 0.01}, β_+ = 1, R = 1. PASS iff m_* finite and ≤ 20 in every case.
- C4: GAS-div bookkeeping: Σ_{m<K} L^{(4 - aβ_+)m} for a·β_+ ∈ {1e-16, 1, 4.5} and K ∈ {10, 50}: diverging for aβ_+ < 4,
  bounded at 4.5.

## D. (g3) count (informational)
Number of *-connected sets of n cubes in Z^4 containing the origin, n = 1, 2, 3, vs 6400^{n-1}. PASS iff count ≤ 6400^{n-1}.

OVERALL PASS iff A1, A2, B1, B2, B3, B5, C1-C4, D pass and the controls A3, B4 fail as required.
