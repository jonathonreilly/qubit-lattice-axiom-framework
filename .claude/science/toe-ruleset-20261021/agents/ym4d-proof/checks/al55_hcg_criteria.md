# al55_hcg — criteria (written before the script; ALIGN55.md §5.4, Lemma HC-1)

Purpose: exact verification of the algebra of the hierarchical Coulomb-detail gauge Λ_HC (Lemma HC-1 (i)-(vi)) and of the commuting pair,
with controls. Python fractions/ints only; exact sparse elimination for Δ_l^{−1} (torus Laplacian, one site pinned, mean-zero output);
`python3 -I -B`; stdout only. su(N) is componentwise, so one real component is used (every map is componentwise linear).

## Models
- MA: d = 2, L = 3, k = 2, T = 2: level-0 torus 18×18, level-1 6×6, level-2 2×2.
- MB: d = 2, L = 3, k = 3, T = 1: level-0 27×27, level-1 9×9, level-2 3×3, level-3 1×1 (three detail levels; top torus degenerate but the
  algebra is defined).
s = the ternary 4-point Deslauriers–Dubuc scheme (al55_sub's s3), periodised on each coarse torus; S_0 = s⊗s; S_1 on μ-links = s^{[1]} in
direction μ ⊗ s in the other direction, s^{[1]} the derived scheme (mask a/σ_3); R = restriction to the coarse sublattice (coarse site J at
fine index 1 + 3J along each axis).

## PASS criteria (exact equalities)
- H1 (iii): Λ_HCΞ_1ν = −ν for 3 random ν ∈ Λ_0 (MA and MB).
- H2 (i): for 2 random chains x, ev^{(l)}Λ_HCx = λ_l (the level-l function of the recursion) for every l (MA, MB).
- H3 (ii): for MB and every pair m < l, changing x_m at random leaves λ_l unchanged; changing x_l changes λ_l.
- H4 (iv): Λ_HCx^φ vanishes on level-1 sites (φ = δ_{y_0} at a level-1 non-root site y_0, x^φ = (dφ, 0, …)).
- H5 (v): for random q supported on level-l sites (l = 0, 1, 2 in MB) and random x: ⟨q, Λ_HCx⟩ = Σ_m⟨c_m, x_m⟩ with
  c_m = −d_mΔ_m^{−1}(1 − R^TS_0^T)S^{(m→0)T}q; and c_m = 0 for m < l.
- H6 (vi): for x with x_l = 0, λ_l = S_0λ_{l+1} (MB, each l).
- H7: RS_0 = 1 on random coarse data; S_0 reproduces constants and the sampled affine functions of one coordinate on a torus section away
  from the wrap (exact on the infinite-line proxy: 1D s applied to samples of j, j², j³ on a long segment, compared in the interior).
- H8: d∘S_0 = S_1∘d on random coarse functions (periodic, MA's level 1 → 0 and 2 → 1).

## Controls (must FIRE)
- K1: without the detail projection (μ_l := −Δ_l^{−1}d_l^*x_l), nested restriction fails: ev^{(l+1)}λ_l ≠ λ_{l+1} for some l.
- K2: a non-interpolatory S_0 (s replaced by the ternary cubic B-spline mask (1, 3, 6, 7, 6, 3, 1)/9 at −3..3) breaks H1 or H2.
- K3: dropping S_0λ_{l+1} from the recursion breaks H1.
- K4: omitting S^{(m→0)T} in the transpose formula breaks H5 for q supported on level-0 sites in MB.
- K5: the derived mask without dividing by σ_3 (s^{[1]} := s) breaks H8.

## What this check cannot decide
(P1′) and (P2-tw) — the k-, T-uniform estimates — are not sampled; MB's top torus is degenerate (1×1); the d = 4 structure is not tested
(the algebra is dimension-free).
