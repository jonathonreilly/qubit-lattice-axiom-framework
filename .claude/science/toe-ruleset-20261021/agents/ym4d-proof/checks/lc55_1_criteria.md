# lc55_1 — criteria (written before the script). Stripe configurations: membership in the multiscale small-field region.

Author: claude-opus-5-5 (LCONV55 worker). Exact arithmetic only: SU(2) as quaternions over Q (python `fractions`).

## Objects
- d = 4, SU(2). Fine torus of side 2L in every direction (coarse torus side 2). L odd.
- Stripe S(L, pattern, τ): every link is the identity except direction-2 links, U_2(x) = exp(i a(x_1 mod L) σ_3), with
  exp(i β σ_3) = ((1−τ²) + 2τ·iσ_3)/(1+τ²) (β = 2 arctan τ, exact).
- Centred antisymmetric pattern (period P = L): a(c) = 0 at c = (L−1)/2, a(c−1) = +β, a(c+1) = −β, a = 0 elsewhere.
  L = 3: (β, 0, −β). L = 5: (0, β, 0, −β, 0).
- S4′ transporters (PROOF §1 "S4′"): for the coarse link c = (X, X+e_μ), block centre c_X = L·X + ((L−1)/2)(1,1,1,1),
  c_Y = c_X + L e_μ; for each of the 24 axis orders σ and each y in the block B(X):
  T^σ_y = P^σ(c_X → y) · S_y · P^σ(c_Y → y + L e_μ)^†, P^σ the complete-axial path moving through the coordinates in the
  order σ, S_y the L straight steps from y in direction μ. Kernel centre M̄_c := mean over (σ, y) (PLD §17.3).
  Straight centre transporter S_{c_X} := the L straight steps from c_X in direction μ.

## Gate G1 (PASS/FAIL), run for L ∈ {3, 5}, τ ∈ {1/10, 1/1000}, and for one representative coarse link per direction
## (μ = 1, 2, 3, 4) plus a translation spot check on a second link per direction:
PASS iff ALL of
 (a) every T^σ_y has zero σ_1 and σ_2 components (lies in the σ_3-torus);
 (b) every M̄_c is a real scalar (zero σ_1, σ_2, σ_3 components) with positive scalar part r_c (so W_0(M̄_c) = 1, mismatch to a
     following coarse link V_c = W_0(M̄_c) is 0);
 (c) every S_{c_X} equals the identity exactly (so ‖V_c − S_c(U)‖ = 0 for the following field);
 (d) the spot-check link has the same M̄_c as the representative of its direction (translation invariance).
Records (no gate): the exact set of values ‖1 − U_p‖²_op = 2 − tr U_p over all level-0 plaquettes; each r_c.

## Designed-FAIL controls (each must make the G1 predicate FALSE; a control that does not fire is reported as such)
 C1a (pattern not antisymmetric): L = 3, pattern a = (β, 0, 0), τ = 1/10. Expected: M̄_c for μ = 2 has a nonzero σ_3 part.
 C1b (period not dividing L): L = 3, period-2 pattern a(x_1) = β·[x_1 odd] on the fine torus of side 6, τ = 1/10; compute the
     following level-1 field V = W_0(M̄) on all 64 coarse links (W_0(M) = M/|M| for SU(2); compare plaquettes via
     2 − tr(V_P) = 2 − Re tr(M̄_1 M̄_2 M̄_3^† M̄_4^†)/(|M̄_1||M̄_2||M̄_3||M̄_4|), decided exactly by comparing squares) and the
     G1 predicate on all links. Expected: (b) fails for some link and some coarse (1,2)-plaquette has 2 − tr V_P > 0.

## Analytic complement (not a gate; written in LCONV55 §C)
If G1 passes, the level-1 following field is the identity everywhere (translation invariance + (b)), hence every level ≥ 1
following field is the identity (the transporters of an all-identity field are the identity), all coarse plaquettes are 1,
and all mismatches vanish.
