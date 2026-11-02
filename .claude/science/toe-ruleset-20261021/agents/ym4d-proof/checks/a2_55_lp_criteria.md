# a2_55_lp — pre-registered criteria (written before the script exists)

Purpose: exact checks of the algebra and of the detail mechanism of the hierarchical local-path alignment Λ_LP (ALIGN2_55 §2), and of
the nesting identity of periodic cubic-spline subdivision (ALIGN2_55 §2, SUB for every L). Fractions/ints only; stdout only.

## Model
d = 2, L = 3, coarse torus side T = 4, depths k = 2 (level-0 side 36) and k = 3 (side 108). Level-l sites = level-0 sites whose
coordinates are multiples of L^l (nested roots; level-(l+1) sites are the level-l sites with both level-l indices ≡ 0 mod 3).
S_0 = tensor product of the ternary 4-point Deslauriers–Dubuc scheme s3 (cubic Lagrange through coarse nodes J−1, J, J+1, J+2 at
τ = 1/3, 2/3; weights (−5, 60, 30, −4)/81 and (−4, 30, 60, −5)/81). Paths γ(Y→y): axial, axis 1 then axis 2, shortest (no wrap; T = 4
makes every used displacement ≤ 5 < 6 level-(k−1) steps). M_l x(y) := Σ_Y a(y, Y)·∫_{γ(Y→y)} x_l; μ_l := −M_l x_l; λ_k := 0;
λ_l := S_0 λ_{l+1} + μ_l; Λ_LP x := λ_0. Values in ℚ (scalar gauge functions suffice: the maps are linear and componentwise).

## Part A — algebra (k = 2 and k = 3, two seeds each)
- **A1 PASS iff** Λ_LP Ξ_1 ν == −ν exactly for random ν vanishing at the level-k roots (Ξ_1ν := (d ev^{(l)}ν)_{l<k}).
- **A2 PASS iff** ev^{(l)} λ_0 == λ_l for every l (nested restriction), for random chains x.
- **A3 PASS iff** perturbing x_m alone leaves λ_l unchanged for every l > m (hierarchical dependence (H)).
- **A4 PASS iff** for q supported on level-l sites, ⟨q, Λ_LP x⟩ is unchanged when x_m with m < l is perturbed (transpose locality).
- **A5 PASS iff** for x = a unit value on one level-m link b (m = k − 1), the coarse ℓ^∞ radius of supp(λ_0) around b is ≤ the a-priori bound
  R_pred := ρ_m·(3L + 1)·L/(L − 1) coarse units AND the measured radius is the same at k = 2 and k = 3 (finite range, uniform in k).
- **A1r PASS iff** A1 also holds when the axial paths are replaced by seeded random lattice paths with the same endpoints (the left-inverse
  identity M_l∘d = 1 − S_0R is path-independent).

## Part B — the detail mechanism (k = 2 and k = 3, level l = 0, window sites whose stencils and paths do not meet the coordinate seam)
- **B1 PASS iff** μ_0(x_0) == 0 at every window site, for x^c with constant coarse gradient (x^c_μ = c_μ + Σ_ν A_{μν}·pos^c_ν, generic rational
  c, A, A not symmetric), at both depths.
- **B2 PASS iff** for a generic quadratic coarse field x^c_μ = Σ quadratic monomials of pos^c, max_window|μ_0| at k = 3 divided by
  max_window|μ_0| at k = 2 equals exactly L^{−3} = 1/27 (detail ∝ ρ_1³ for a C^{2} field: no ρ_1² term), and the k = 2 maximum is nonzero.
- **Controls (each must FIRE):** CB1 s3 replaced by linear interpolation (weights (2/3, 1/3)): B1 fails; CB2 axial paths replaced by seeded
  random paths: B1 fails (antisymmetric part); CB3 with linear interpolation the B2 ratio is NOT 1/27.

## Part C — periodic cubic-spline subdivision (1D, exact)
S^{(L)}_{M}: values on a periodic grid of M points (spacing 1) ↦ values at the LM points of spacing 1/L of the periodic cubic-spline
interpolant (uniform cubic B-spline basis; coefficients by inverting the circulant (1/6, 4/6, 1/6)).
- **C1 PASS iff** S^{(L)}_{LM} ∘ S^{(L)}_{M} == S^{(L²)}_{M} exactly, for (L, M) ∈ {(3, 4), (5, 3), (3, 3)} (nesting: iterates = samples of one spline).
- **C2 PASS iff** S^{(L)}_M is interpolatory (its rows at the coarse points are unit vectors) and reproduces constants, for the same (L, M).
- **C3 PASS iff** the periodic collocation circulant is invertible (exact nonzero determinant) for M = 1..8.
- **Control CC1 (must FIRE):** the square of the ternary 4-point DD scheme is NOT the 9-adic 4-point DD scheme (cubic Lagrange at τ = i/9).

## What this check cannot decide (stated in advance)
No norm bound, no k-uniformity beyond A5's two depths, nothing in d = 4, no Hölder constants, no completion-norm bound, no background
estimate, no statement about su(N) beyond linearity. OVERALL PASS iff A1-A5, A1r, B1, B2, C1-C3 PASS and CB1-CB3, CC1 all FIRE.

## Amendment A1 (written 2026-10-29T05:0xZ, BEFORE the script a2_55_lp.py exists; reason stated)
On working out the support bound for the script, the pre-registered A5 is wrong in two ways: (i) "the measured radius is the same at k = 2
and k = 3" contradicts the geometric tail of the down-propagation (each extra level below adds up to 6 own steps of that finer level, so the
radius grows with k toward a k-uniform limit; it is not constant); (ii) the printed R_pred = ρ_m(3L + 1)L/(L − 1) is a miscount, and with
T = 4 the support would wrap the torus (R_pred > T/2). **A5 is replaced by:** on the torus T = 8 (so the bound is below T/2), for x = a unit
value on one level-m link b, m = k − 1, **A5 PASS iff the coarse ℓ^∞ radius of supp(λ_0) around tail(b) is ≤ R_pred := 6ρ_m·L/(L − 1)**
(= 3 coarse units at L = 3) at both k = 2 and k = 3. (Derivation: b lies on a path between Y and y, |y − Y|_∞ ≤ 6 level-m steps; one S_0 step
moves support by ≤ 6 steps of the finer level; Σ_{j<m}6ρ_j ≤ 6ρ_m/(L − 1).) All other criteria unchanged.
