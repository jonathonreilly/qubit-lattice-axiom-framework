# lc55_4 — criteria (written before the script). A uniform family down to every threshold on a region with a collar.

Author: claude-opus-5-5 (LCONV55 worker). Exact arithmetic only (polynomials in τ over Q; python `fractions`).

## Object
Cylinder region of lc55_2 G2b with fixed width n = 9 in x_1 (collar sites x_1 ∈ {0, 9}), x_2 periodic, x_3, x_4 boxed by the
envelope f(x) = x(n_⊥+1−x); stripe P = 3, pattern (β, 0, −β), β = 2arctan τ. Riemannian chart; horizontal vectors exactly
parametrised by the recursion w_1(x) = w_1(x−1) − (Ad_{G(x)} − 1)w_2(x) (x = 1..8), free data w_1(0) ∈ R³, w_2(1..8) ∈ R³.

## Gate G4 (all τ ∈ (0, 1/10])
Form Q̂(τ) := (1+τ²)²·Hess on the (1+τ²)²-scaled recursion basis (27 vectors) as an exact polynomial matrix; exact degenerate
perturbation theory on K := ker Q̂(0) (expected: the three wall-to-wall holonomy directions, constant w_1, w_2 = 0).
- If KᵀQ̂_1K has a negative direction: certify at first order (N_1 < 0) with the tail bound below.
- Else require KᵀQ̂_1K = 0 and certify at second order: p(τ) = p⁽⁰⁾ + τp⁽¹⁾, N(τ) = pᵀQ̂p with N_0 = N_1 = 0, n_2 < 0.
PASS iff the certified order's coefficient is negative and Σ_{j>j*}|n_j|(1/10)^{j−j*} < |n_{j*}| (j* = certified order).
Then compute, exactly: κ := |n_{j*}| − Σ_{j>j*}|n_j|(1/10)^{j−j*}; D_max := Σ_j |d_j|(1/10)^j for D(τ) = |w(τ)|² (an upper
bound on [0, 1/10]); c_* := κ/((1 + 1/100)²·D_max), so RQ_cyl(τ) ≤ −c_*τ^{j*} on (0, 1/10]. With the exact identity
2S_1/S_0 = 20/((n_⊥+1)² + 1) (verified exactly for n_⊥ = 1..200 in the script), the region with
n_⊥(τ) := ⌈(40/(c_*τ^{j*}))^{1/2}⌉ has RQ_4D ≤ −c_*τ^{j*}/2 < 0. Record c_* and n_⊥(τ) at τ = 10⁻⁴⁴ (below the lane's ε_1 scale).

## Agreement and controls
- G4-agree: at τ ∈ {1/10, 1/50, 1/1000}, the polynomial N(τ)/(1+τ²)² equals the direct exact Hess (lc55_2-style t-expansion
  with the actual G) and the 2×2-complex assembled Hess of w(τ), exactly.
- C4a: at τ = 0 the certified p(0) has Hess ≥ 0. C4b: the σ_3-components alone have Hess ≥ 0 at τ = 1/10.
- C4c: horizontality residual of w(τ) exactly 0 at τ ∈ {1/10, 1/50, 1/1000}; a perturbed vector has nonzero residual.
