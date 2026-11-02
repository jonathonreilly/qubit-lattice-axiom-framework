# s3 criteria (lane F session 3; written 2026-10-28 before any s3 script exists; not edited after the script exists)

Each criterion is tagged EVIDENTIAL (a wrong lemma or a wrong constant could make it fail) or ARITHMETIC (it re-computes a
number of the text; it can fail only through an algebra slip in the text). No criterion is a construction identity.

## A. Lemma LOC-s′ at the edge of its domain (EVIDENTIAL; REVIEW_SF_S2 Part E recommendation)
Model: sites y = 0..11 on a ring; "X^+" = sites {0, 1}; far sites F = {2..11}, |F| = 10; scalar Z_y ∈ [-1, 1] random (seed 3);
b_y := 0.6·e^{-0.5·dist(y, 0)}·Z_y; g(s) := 1/(1 - w(s)), w(s) := c_0 + Σ_{y∈F}b_ys_y, c_0 := b_0 + b_1 (s = 1 on X^+).
F_S := Σ_{T⊂S}(-1)^{|S∖T|}g(1_T) for every S ⊂ F (1024 sets), computed exactly (float64).
For each S choose radii r_y := e^{0.5·dist(y,0)}·ρ_S with ρ_S the largest common factor such that
m_S := |c_0| + Σ_{y∈S}|b_y|(1 + r_y) = 1 - 10⁻³ (the refined domain of LOC-s′ comes within 10⁻³ of the pole). If ρ_S ≤ 0 skip S
(count reported). Refined bound B_S := (1/(1 - m_S))·Π_{y∈S}r_y^{-1}.
- **A1** |F_S| ≤ B_S for every non-skipped S.
- **A2 (non-vacuous)** max_S |F_S|/B_S ≥ 10⁻⁴ over S with |S| ≥ 1, and at least 500 sets are not skipped.
- **A3 (the refinement is load-bearing)** for at least one non-skipped S with |S| ≥ 1, the UNREFINED domain (|s_y| ≤ 1 + r_y for
  ALL y ∈ F, radii r_y := e^{0.5·dist}ρ_S for y ∈ F∖S too) contains the pole, i.e. |c_0| + Σ_{y∈F}|b_y|(1 + r_y) ≥ 1.

## B. Lemma QC, the large-site cost by Hölder (EVIDENTIAL)
Model B-scalar: ring of 300 sites, one link per site, symmetric kernel K(b, b') = u_{bb'}e^{-0.3|b-b'|} (u iid N(0,1), symmetrised),
N_0 := max_bΣ_{b'}|K(b, b')|. Model B-block: ring of 150 sites with 4 links per site, symmetric link kernel as above in link
distance |b - b'|/4 rounded, |K(b, y)| := Σ_{b' at y}|K(b, b')|, N_0 := max_bΣ_{b'}|K(b, b')| (link row sums).
200 trials each: Q random of density 0.05-0.5, t_y := 2^{j_y+1} with j_y uniform in {0..6}; σ_b := Σ_{y∈Q}|K(b, y)|t_y.
- **B1** scalar: Σσ³ ≤ N_0³Σt³, Σσ² ≤ N_0²Σt², Σσ ≤ N_0Σt in every trial.
- **B2** block: Σσ³ ≤ 4N_0³Σt³, Σσ² ≤ 4N_0²Σt², Σσ ≤ 4N_0Σt in every trial.
- **B3 (non-vacuous)** the max over trials of Σσ/(N_0Σt) (scalar) is ≥ 0.3 and of Σσ³/(N_0³Σt³) is ≥ 10⁻³.

## C. Lemma SF-N♮'s spread bound (EVIDENTIAL)
SU(2) and SU(3); L = 3, p_L = 11; loops of ℓ = 22 factors U_{b_i}^{±1} (random signs); real links U_b = e^{X_b}, X_b ∈ su(N) random
with |X_b|_HS = α ∈ {1e-4, 3e-4} (then y_bg := |log(loop)|_HS); complex A_b ∈ sl(N, ℂ) random with |A_b|_HS = a, a ∈ {1e-4, 5e-4};
for each (N, α, a) 300 random samples and 1 ALIGNED sample (A_b chosen so that every conjugated factor Ã_i equals the same aŴ,
with Ŵ ∈ su(N) of unit HS norm), y := |log(loop at e^AU)|_HS (principal log). ℓa ≤ 0.011 and y_bg ≤ 22α·1.04 ≤ 1/120 in all cases.
- **C1** y ≤ y_bg + 2.2p_L·a (c_y = 2.2p_L, ℓ ≤ 2p_L) in every sample, both N.
- **C2** y_bg ≤ 2.2p_L·α in every sample (the real-background bound of the lemma's proof).
- **C3 (non-vacuous)** for the aligned samples, (y - y_bg)/(ℓa) ≥ 0.5 for at least one (N, α, a), and (y - y_bg)/(ℓa) ≤ 1.04 for all.

## D. CE-col constants, rate closure, CE-Q band weights (ARITHMETIC)
- **D1** κ_0 = 16 log 12800 ∈ [151.31, 151.32]; κ̃_0 = 16 log(2·624²) ∈ [217.0, 217.1]; κ_0 + 2κ̃_0 + 3 ∈ [588, 589].
- **D2** with w := w_8 = Σ_{n≥1}(2n + 1)⁴e^{-8n}, the smallest κ_c with 3(κ_c - κ_0 - 2κ̃_0 - 3 - 16 log 2 - κ_0) - 1 ≥
  κ_c + 16 log 2 + 1296w lies in [1100, 1200].
- **D3** the 273 route: 3(κ_c - 3κ_0 - 3 - κ_0) - 1 < 273(κ_c + 16 log 2) + 1296w for every κ_c on a grid of 10⁴ points in
  [3κ_0 + 3, 10⁸] (log-spaced).
- **D4** the CE-Q per-site sum: for n = 4(N² - 1), N = 2, 3, and p ∈ {10, 30, 100}: Σ_{j≥0}2^{n/2}e^{-4^jp²/4}e^{(3/16)4^jp²}
  ≤ 2·2^{n/2}e^{-p²/16} (sum to j = 30).

OVERALL PASS iff every criterion passes. Runtime target < 2 min; numeric lock; nice 10; BLAS threads 1.
