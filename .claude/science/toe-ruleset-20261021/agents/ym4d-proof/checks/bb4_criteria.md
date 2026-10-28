# bb4 criteria (pre-registered; written after BFT_B.md §12 (07:30:46 UTC) and before checks/bb4_models.py exists)

Purpose: the algebra of Theorem RW^∇_k-Π (hard slice), the frame-covariance mechanism of Theorem GI-cov (with the
background given, i.e. no (CovLift) is tested), and the m = 0 regime of RW^∇_k's walk factor (reviewer's request,
REVIEW_BFT_B_S3 Part F). Model operators only; no k-uniformity, no lane-A norm, no (CovLift).

Common: numpy/scipy, float64/complex128, single thread, fixed seeds (base 20261028). Cutoff profile σ(t) = 1 (t ≤ 0),
1 - 2t² (0 ≤ t ≤ ½), 2(1 - t)² (½ ≤ t ≤ 1), 0 (t ≥ 1) (Lemma W-cut). Sup norms are max-abs; operator sup norms are
maximal absolute row sums.

## (A) m = 0 regime (single box, sup norms; d = 2 scalar site fields)
- Operators on a periodic torus of side T: A1 (coarse mass, massless inside blocks): 𝓛 = -Δ + (1/9)·P_blk, P_blk the
  average over aligned 3×3 blocks (mimics the top residual); A0 (control, no coarse mass): 𝓛 = -Δ + Π_0, Π_0 the global
  mean projector of that torus.
- Box □ = [0, R)² (R ∈ {6, 12, 18, 24, 30}), local torus side T_W = the least multiple of 3 that is ≥ 3R + 14, box placed
  at offset aligned to the blocks. ψ(z) = Π_μσ((d_μ(z) - R/2)/(R/2)) (d_μ = distance of z_μ to the box's interval).
  Inputs: unit sources at the sites of □^{(1)}. G_□ := max over sites of Σ_inputs |𝓛^{-1}(site, input)|;
  r_□ := max over sites of Σ_inputs |(C 𝓛^{-1})(site, input)| with C := [-Δ, ψ] + [(1/9)P_blk, ψ] for A1 and
  C := [-Δ, ψ] (local part) for A0.
- **A-1 (PASS criterion; the O(1/R) law with uniform G):** for A1, max_{R≥12} R·r_□(R) ≤ 6·r_□(6) AND
  max_R G_□(R) ≤ 2·G_□(6).
- **A-2 (prediction RW∇-F5; "PASS" = prediction confirmed):** for A0, G_□(30) ≥ 4·G_□(6) AND 30·r_□(30) ≥ 2·6·r_□(6).
- Informational: the tables of G_□, r_□, R·r_□ for both operators.

## (B) frame covariance (d = 2, SU(2) fundamental, background given)
- Torus 32², links U = exp(i·0.1·Σ_k a_kσ_k), a_k i.i.d. N(0, 1); 𝓛(U) = covariant Laplacian + μ², μ² = 1;
  E(φ) = ½⟨φ, 𝓛φ⟩ + (λ/4)Σ|φ_x|⁴ - Re⟨j, φ⟩, λ = 0.05, j entries i.i.d. complex N(0, 0.3²). Gauge h: Haar SU(2) per site;
  U ↦ h(x)^†U_μ(x)h(x + e_μ), φ, j ↦ h^†φ, h^†j.
- R = 4, M_c = 8 (16 cubes, 64 boxes), T_W = 26, frame region Ω = □^{(10)} (24² sites), root = lowest corner of □,
  complete axial frame (axis 0 then axis 1). χ_□ = σ-spline partition (scale 1), ψ_□ = Π_μσ((d - 2)/2), η_Q =
  σ(d/2)-weights normalised. Local tori: frame data U^{g} on the links internal to the embedded Ω, 1 elsewhere. Control
  ("frame-free"): U itself (given gauge) on the embedded Ω, 1 elsewhere, no frame. Bond family as Construction BB-bond_k
  with g = -j, 𝔑(u) = λ|u|²u, 𝔈_Q = Σ_{x∈Q}[-½Re⟨j_x, (S_Q𝐀)_x⟩ - (λ/4)|(S_Q𝐀)_x|⁴]; s real.
- **B-1:** parametrix identity max|𝓛P y - (1 - R)y| / max|y| ≤ 1e-10 on 4 random y, frame and control, at U and at U^h.
- **B-2:** covariance (frame): max over boxes and 4 random y of |P_□(U^h)h^†y - h^†P_□(U)y| / max|P_□(U)y| ≤ 1e-10, and the
  same for R_□.
- **B-3:** walk inverse P(1 - R)^{-1}y = 𝓛^{-1}y (relative ≤ 1e-10, frame).
- **B-4:** energy invariance (frame): for 3 random s ∈ [0, 1.2]^bonds and s ≡ 1, |ΔE(s; U^h, h^†j) - ΔE(s; U, j)| ≤
  1e-10·(1 + |ΔE|); and ΔE(1) = E(φ*) - E(0) (relative ≤ 1e-10) for frame and control.
- **B-5:** two-cube polymer R(X), X = two *-adjacent cubes (bond family with only the internal bond free, all bonds
  leaving X set to 0: R(X) = ΔE_X(s_b = 1) - ΔE_X(s_b = 0)): invariant under h for the frame version (≤ 1e-10·(1 + |R|)).
- **B-6 (witness of RW∇-F2 for the frame-free transplant; "PASS" = non-invariance observed):** control: max over the 3
  random s of |ΔE(s; U^h) - ΔE(s; U)| ≥ 1e-6, and |R(X)(U^h) - R(X)(U)| ≥ 1e-8; while its B-1 and its s ≡ 1 energy hold.

## (C) hard slice (d = 2 abelian 1-form, Theorem RW^∇_k-Π's algebra)
- Fine torus side T = 60; roots at even sites (b = 2). x real on links. 𝓑(u, x) = Σ_p(du)_p(dx)_p + Σ_{X,μ}Λu·Λx,
  Λx(X, μ) := x_μ(c_X) + x_μ(c_X + e_μ). Tents χ_X(z) = Π_νmax(0, 1 - |z_ν - c_{X,ν}|/2); λ_X(z) := -½Σ_{two axial orders}
  (line integral of x from c_X to z); Pλ := Σ_Xχ_Xλ_X; Πx := x + d(Pλ(x)); S := Ran Π.
- Boxes R = 12 (25 boxes), link positions = midpoints; χ_□ = σ-spline partition of the link positions (intervals
  [a - ½, a + R - ½)); ψ_□ = Π_μσ((d - 6)/6); local tori side T^Π_W = 56 (= 3R + 14 + 2·3), box placed at [22, 34)²
  (even shift). Slice inverses: u = Πw, (Π^T𝓑Π + (1 - Π)^T(1 - Π))w = Π^Ty. P^Π_□, R^Π_□ as in §12.1 with
  C^♯ := 𝓑(ψu) - ψ(𝓑u).
- **C-1:** max|Π∘Π - Π| ≤ 1e-12 (entries), and max|Π dλ| ≤ 1e-12·max|dλ| for 3 random λ vanishing at the roots.
- **C-2 (Lemma W-gauge0 in the model):** max|𝓑 dλ| ≤ 1e-12·max|dλ| for the same λ.
- **C-3:** slice parametrix identity: max|Π^T(𝓑P^Πy - (1 - R^Π)y)| / max|y| ≤ 1e-10 for 4 random y, and P^Πy ∈ S
  (max|(1 - Π)P^Πy| ≤ 1e-12·max|P^Πy|).
- **C-4:** walk inverse: z := (1 - R^Π)^{-1}y by GMRES (tol 1e-13): max|P^Πz - u_glob| / max|u_glob| ≤ 1e-8, u_glob the
  global slice solution.
- **C-5 (control, predicted failure):** ψ' = Π_μσ((d - 2)/10) (plateau radius 2 < 1 + r_Π): the identity residual of
  C-3 is ≥ 1e-6 (relative).
- **C-6 (control):** P'y := ψι^*u without Π: the S-tested identity still holds (≤ 1e-10; first-slot gauge annihilation),
  but P'z ∉ S: max|(1 - Π)P'z| ≥ 1e-6·max|P'z|.

## Verdict
ALL PASS iff A-1, A-2, B-1..B-6, C-1..C-6 all hold. A FAIL of a prediction row (A-2, B-6, C-5) is reported as a failed
prediction, not repaired after the fact.

## Run rules
Numeric lock `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, load1 < 8 checked, nice 10,
OPENBLAS/OMP/MKL/VECLIB threads = 1, PYTHONDONTWRITEBYTECODE=1, /usr/bin/time -l, python3 without -I, no `timeout`, no
trap, `rmdir` exactly once; < 20 min, < 1 GB.
