# lc55_2 — criteria (written before the script). Riemannian (gauge-quotient) Hessian of the Wilson action at the stripe.

Author: claude-opus-5-5 (LCONV55 worker). Exact arithmetic only (python `fractions`; polynomials in τ with rational
coefficients where stated). Floats are used ONLY to propose a direction, which is then rounded to rationals; every verdict
is computed exactly.

## Conventions
- S := Σ_p (1 − ½ tr U_p) (the lane's s(U) = 1 − N⁻¹Re tr U at N = 2, summed; u_0 is factored out).
- Riemannian chart at the point (bi-invariant metric, |v|² = Σ_i v_i²): U_ℓ ↦ U_ℓ·exp(i t v_ℓ·σ); Hess(v) := d²/dt² S|_{t=0}.
  (Geodesics through U_ℓ are t ↦ U_ℓ e^{itv·σ}, so this is the Riemannian Hessian.)
- Vertical vectors ξ(λ)_ℓ = Ad_{U_ℓ⁻¹}λ(x) − λ(y) for ℓ = (x → y), λ supported on non-collar sites. Horizontal := Euclidean-
  orthogonal to every ξ(λ). The quotient (Riemannian) Hessian is Hess restricted to horizontal vectors.
- Stripe pattern for period P ∈ {3, 5, 7}: a(c) = 0 at c = (P−1)/2, a(c−1) = +β, a(c+1) = −β, a = 0 elsewhere
  (P = 3: (β, 0, −β)); background U_2(x) = exp(i a(x_1 mod P) σ_3), all other links 1; exp(iβσ_3) exact in τ = tan(β/2).
- Transverse lift (x_3, x_4 envelope): f(x) = x(n_⊥ + 1 − x), S_0 := Σ_{x=1}^{n_⊥} f(x)², S_1 := Σ_{x=0}^{n_⊥}(f(x+1) − f(x))².
  For a 2D-plane mode w with v_3 = v_4 = 0: claimed identity (Lemma SEP, proven in LCONV55 §C, checked in G2-sep)
  Hess_4D(w⊗f⊗f) = S_0²·Hess_2D(w) + 2·S_0·S_1·|w|², and w⊗f⊗f is horizontal iff w is. So RQ_4D = RQ_2D(w) + 2S_1/S_0.

## Gates
- **G2-agree (two code paths).** For every vector certified below, Hess(v) computed (i) by direct t-expansion of S along
  U e^{itv} (quaternion arithmetic truncated at t²) and (ii) by an assembled per-plaquette bilinear form (second-derivative
  insertion formulas) must agree EXACTLY. PASS iff equal for all certified vectors.
- **G2-sep (lift identity).** On a small 4D instance (cylinder below with n = 4, x_2-period 2, n_⊥ = 3, τ = 1/10), compute the
  full 4D Hess(w⊗f⊗f) by summing over all six plaquette orientations and compare with S_0²·Hess_2D(w)·(x_2-period) +
  2S_0S_1|w|²·(x_2-period) for an exactly horizontal w. PASS iff exactly equal; and horizontality residual of w⊗f⊗f is
  exactly 0 in 4D.
- **G2a (reduced torus, every small τ; P ∈ {3, 5, 7}).** On the x_2-independent, x_1-periodic (period P) reduced problem,
  parametrise the horizontal space exactly (charged parts of w_2 at the two ±β sites tied by the solvability condition,
  w_1 by the recursion w_1(x) = w_1(x−1) − (Ad_{G(x)} − 1)w_2(x)), form the quadratic form Q̂(τ) := (1+τ²)^m·Hess on that
  basis as an exact polynomial matrix in τ, and do exact degenerate perturbation theory: K := ker Q̂(0); require
  KᵀQ̂_1K = 0; p⁽¹⁾ := an exact solution of Q̂_0 p⁽¹⁾ = −Q̂_1 p⁽⁰⁾; choose a rational p⁽⁰⁾ ∈ K. Let
  N(τ) := p(τ)ᵀQ̂(τ)p(τ), p(τ) = p⁽⁰⁾ + τp⁽¹⁾ (an exact polynomial).
  PASS iff N has zero τ⁰ and τ¹ coefficients, n_2 := [τ²]N < 0, and Σ_{j≥3}|n_j|·(1/10)^{j−2} < |n_2|
  (hence N(τ) < 0 for every 0 < τ ≤ 1/10, i.e. a horizontal direction of negative quotient Hessian exists at EVERY such τ,
  in particular below every threshold the lane can choose). Record n_2/D_0 (D_0 = |p⁽⁰⁾|²-norm at τ = 0 in the lifted
  coordinates) as the leading coefficient of RQ in τ².
- **G2b (cylinder region).** Region: x_1 ∈ {0..n}, sites x_1 ∈ {0, n} in the fixed collar; x_2 periodic; x_3, x_4 bounded by
  the transverse lift. 1D reduced variables w_1(x) (x = 0..n−1), w_2(x) (x = 1..n−1); horizontality at x = 1..n−1 by the
  recursion (exact, by construction). Pre-registered instances (P = 3):
  (τ, n, n_⊥) ∈ {(1/10, 9, 16), (1/10, 60, 12), (1/50, 9, 80), (1/50, 240, 80)}.
  PASS iff, for each instance, the exact RQ_4D := Hess_cyl(w)/|w|² + 2S_1/S_0 < 0 for the certified rational horizontal w.
- **G2c (box region, all four directions bounded).** 2D box sites {0..n}², all sites with x_1 or x_2 ∈ {0, n} in the collar
  (links between two collar sites fixed; all other links free), lifted by the transverse envelope. Exact horizontal
  projection by solving the vertical normal equations over Q. Pre-registered instance: P = 3, (τ, n, n_⊥) = (1/10, 12, 16).
  PASS iff the exact RQ_4D < 0. (If the exact solve does not finish in the session, G2c is reported NOT RUN — not PASS.)

## Designed-FAIL controls (must NOT certify negativity; reported as fired/not fired)
- C2a (free background, τ = 0): same constructions; Hess ≥ 0 must be found for each proposal (sum of squares at U_P = 1).
- C2b (neutral sector): the σ_3-components of each certified vector alone give Hess ≥ 0 (expected Σ_P cos θ_P (dc)_P² ≥ 0).
- C2c (horizontality detector): the horizontality residual of the unprojected/un-recursed float proposal is nonzero
  (the detector can fire), and of every certified vector is exactly zero.
