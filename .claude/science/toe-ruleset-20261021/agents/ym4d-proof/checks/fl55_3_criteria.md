# fl55_3 criteria — the gauge-covariance step of the h-tadpole lemma, exact (written before any fl55_3 script)

Owner: FLOW55.md (worker claude-opus-5-5). Script: checks/fl55_3.py, written AFTER this file. Plain python 3,
`fractions.Fraction` only (exact rational Gauss-Jordan); no numpy, no floats in any verdict. nice 10. Output:
checks/fl55_3_out.txt, checks/fl55_3_err.txt.

## Objects (a finite instance of the level-n h-Gaussian of FLOW55 §K)
Graph: the 2-dimensional periodic lattice (Z/3)² (9 sites, 18 oriented links c = (x, x + e_μ), μ = 1, 2). Gauge group SU(2)
in the adjoint representation: Lie algebra R³ with [a, b] := a × b (cross product); Ad of a group element is a rotation
R ∈ SO(3). Rational rotations are produced by the Cayley map R = (I + K)(I − K)^{-1}, K a rational antisymmetric 3×3 matrix
(exact; R ∈ SO(3) is verified exactly in-script: RᵀR = I, det R = 1).
- Background on links: R_c := Ad(V_c) ∈ SO(3).
- Covariant gradient on adjoint 0-forms ν (sites → R³): (D_Vν)_c := R_cᵀν(x) − ν(x + e_μ) for c = (x, x + e_μ) (the
  infinitesimal gauge action in the exponential chart, FLOW §79 (a)).
- h-Hessian: 𝔊_V := D_VᵀWD_V + m²·1, W = diagonal link weights w_c (colour-scalar), w_c = 1 + (c-index mod 5)/7, m² = 1/3.
  Cov_V := 𝔊_V^{-1} (27×27, exact).
- Second-order orbit term: w_2(ν, ν)_c := −½[R_cᵀν(x), ν(x + e_μ)].
- Tadpole vector on link c: T_c(V) := E_{Cov_V}[w_2(ν, ν)_c] = −½Σ_{a,b}Cov_V((x, a), (x + e_μ, b))·(R_cᵀe_a) × e_b ∈ R³.

## Part 1 — exact pure-gauge identity
Pure-gauge background: site rotations g_x := Cayley(K_x) with K_x pseudo-random rational antisymmetric (entries
numerators in [−3, 3], denominators in [1, 4], seed 5503), and R_c := g_x g_{x+e_μ}ᵀ.
- **P1.** T_c(V) = 0 (exactly, all three components) for all 18 links. PASS iff exact.
- **P1-c (designed FAIL control).** The "naive" tadpole with the untransported trivial-background covariance,
  T_c^naive := −½Σ_{a,b}Cov_1((x, a), (x + e_μ, b))·(R_cᵀe_a) × e_b, is NONZERO on at least one link. Must fire.

## Part 2 — exact first-order identity
V(ε) := exp(εv) on links, v a link field (links → R³). Exact first-order coefficient T^{(1)}_c[v] := d/dε T_c(V(ε))|_{ε=0},
computed from d/dε R_cᵀ|_0 = −[v_c]_× (the cross-product matrix of v_c), δ𝔊 := δDᵀWD_1 + D_1ᵀWδD with (δDν)_c := −v_c × ν(x),
δCov := −Cov_1·δ𝔊·Cov_1, so
  T^{(1)}_c[v] = −½Σ_{a,b}δCov((x,a),(y,b))·e_a × e_b − ½Σ_{a,b}Cov_1((x,a),(y,b))·(−v_c × e_a) × e_b   (y = x + e_μ).
- **P2 (gradients).** For v_c := λ(x) − λ(x + e_μ) (first-order pure gauge), λ pseudo-random rational (seed 5504, numerators
  [−4, 4], denominators [1, 3]): T^{(1)}_c[v] = 0 for all links. Tested for three independent λ. PASS iff exact.
- **P2-n (non-vacuity).** For a pseudo-random rational v (seed 5505) that is not a gradient, T^{(1)}[v] ≠ 0 on at least one
  link. PASS iff nonzero (otherwise the functional is identically zero and P2 is vacuous: report INVALID).
- **P2-c (designed FAIL control).** Dropping the δCov term (keeping only the second term) gives a NONZERO result on a
  gradient v for at least one λ. Must fire.
- **P3 (linearity sanity).** T^{(1)}[v_1 + v_2] = T^{(1)}[v_1] + T^{(1)}[v_2] exactly for the seed-5505 field and one
  gradient. PASS iff exact.

## Overall
PASS iff P1, P2, P2-n, P3 PASS and P1-c, P2-c fire. A control that does not fire, or P2-n failing, makes the check INVALID
(reported, not hidden). Run once; output kept unaltered.
