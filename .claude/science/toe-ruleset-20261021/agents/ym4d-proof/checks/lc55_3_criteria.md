# lc55_3 — criteria (written before the script). Exponential/axial chart (the chart (LC-2′) names) at the stripe.

Author: claude-opus-5-5 (LCONV55 worker). Rigorous rational interval arithmetic for cos/sin-type functions; exact otherwise.

## Objects
- Background in exponential coordinates: A_ℓ = a(x_1 mod 3)·σ_3 on direction-2 links (pattern (β, 0, −β)), A_ℓ = 0 elsewhere,
  with β RATIONAL: β ∈ {1/5, 1/20}. U_ℓ = exp(i(A_ℓ + t v_ℓ)·σ).
- Second-order expansion of exp(iX·σ) = F(|X|²) + i·Gf(|X|²)·X·σ, F(s) = Σ(−s)^k/(2k)!, Gf(s) = Σ(−s)^k/(2k+1)!; the needed
  Taylor coefficients F_j(β²), Gf_j(β²) (j = 0, 1, 2) are enclosed by exact partial sums plus a rigorous tail bound.
- Slice: axial gauge along x_4 with its tree on the boundary of Ω. In the bulk it constrains only v_4 (= 0 for every mode here),
  so every (v_1, v_2) on the 2D box's free links, lifted by f⊗f with v_3 = v_4 = 0, lies in the slice. No horizontality.
- 2D box: sites {0..n}², n = 6, collar as in lc55_2 G2c. Lift bound (Lemma SEP-exp, LCONV55 §C): Hess_4D ≤ S_0²Hess_2D(w)
  + 2S_0S_1|w|² (uses |∫_0^1 Ad_{e^{−isA}}w ds| ≤ |w|), so RQ_4D ≤ RQ_2D(w) + 2S_1/S_0.

## Gate G3
Pre-registered instances (β, n, n_⊥) ∈ {(1/5, 6, 12), (1/20, 6, 24)}. PASS iff the rigorous upper end of
RQ_2D(w) + 2S_1/S_0 is < 0 for the certified rational w (proposal from floats, then rounded).
Second code path (must agree within the interval widths): the exp-chart Hessian of the same w computed from the truncated
matrix power series of exp(M_0 + tM_1) (Duhamel ordering, rigorous tail bound) instead of the closed-form scalar functions.

## Designed-FAIL control
- C3a (β = 0): the same pipeline must report RQ_2D(w) ≥ 0 for every proposal (sum of squares at the trivial background).
- C3b: the same proposal evaluated in the Riemannian chart (exact, lc55_2's code) is recorded; G3 is about the exponential
  chart and is decided only by its own interval.
