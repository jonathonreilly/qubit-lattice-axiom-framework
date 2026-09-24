# Referee report: J:derive:source-neutral-inclusion-attraction:a2

- **Author:** `w-macbookpro90c72-j091d` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j8c71` (`grok-4.6`). Different model family.
- **Material:** `probes/work/derive/source-neutral-inclusion-attraction/w-macbookpro90c72-j091d/ATTEMPT.md` and `check.py`, and the hit log under `logs/probes/J:derive:source-neutral-inclusion-attraction:a2/`.
- **Block 41 T4** (PR #8547, on its branch) gives the held-tilt cost `−κ a b G(r)/(G(0)² − G(r)²)`. The comparison below uses `κ = a = b = 1`.

The checks in `check.py` do not call the author's script. The torus Green function is a real-space solve of `(L + 11ᵀ/N)`, the interaction is the prime log-determinant of the modified Laplacian, and the `Z³` Green function is a Bessel quadrature checked against `G(0) − G(e₁) = 1/6` and Watson's gamma product.

## The statement

The task asks, in the quadratic model, for the exact interaction of two bond-stiffness inclusions, its second-order attraction and `r⁻⁶` constant, the ratio to two held tilts at `r = 5, 10, 20` for a vacancy, and whether any rotation-invariant inclusion can attract as `1/r`.

The attempt states that statement, with one correction: the `ε²` coefficient is `1/2`, not the task's `1/4`. That correction is right. Nothing else is weakened.

## Step by step

**S1 (torus Green function): holds.** On the `8³` torus, `G(0) = 118783817/528855040`. A Fourier sum at 40 decimals and a real-space solve agree with that fraction. `LG = δ − 1/512` and the column sums to zero. The attempt's route to the same value was exact arithmetic in `Q(√2)`; this is a different route.

**S2 (the determinant formula): holds.** For disjoint bonds,
`F = ½ log det(I − ε_x ε_y (I + ε_x A_x)⁻¹ M_xy (I + ε_y A_y)⁻¹ M_yx)`.
On `6³`, this matches the prime log-determinant of `L + ε_x D_x D_xᵀ + ε_y D_y D_yᵀ` to `1e-9` for like and unlike `ε`, including both signs. On `8³` at `ε = −1/2` the same log-determinant reproduces the printed values: `−0.0035209463`, `−0.00020640211`, `−4.9346887×10⁻⁵` at `r = 2, 3, 4`. At `r = 1` the shared bond is `+0.0030438` if its stiffness is multiplied by `(1+ε)²`, and `−0.098304` if the two shifts add. The attempt is right that the task does not choose the convention. The formula claimed for `r ≥ 2` does not use that convention.

**S3 (the sign): holds.** For `ε > −1` and disjoint bonds the quadratic form stays positive definite, because every bond coefficient `1+ε` is positive. `A` has eigenvalue `1` on `(1,…,1)` and eigenvalues strictly below `1` on the dipole directions (`μ = G(0) − G(2e₁) < 1`), so `I + εA` is positive definite for `ε > −1` and singular only at a vacancy. The cross factor is `det(I − TTᵀ)` or `det(I + TTᵀ)` according to the sign of `ε_x ε_y`, hence `F ≤ 0` for like inclusions and `F ≥ 0` for unlike ones. Checked on `6³` at `r = 2, 3` for six sign pairs.

**S4 (second order): holds, and the task's `1/4` does not.** For centered Gaussians, `Cov(X², Y²) = 2 Cov(X, Y)²`. With `δS = (ε/2) Σ_b (d_b·θ)²` and `κ = 1`, the cross cumulant is `F = −(ε_x ε_y / 2) Σ M² + O(ε³)`. Sympy confirms `Cov(X², Y²) = 2c²`. On `8³` at `r = 2`, `−(1/2) Σ M² = −0.011367274260`, and Richardson extrapolation of the `6×6` formula at `ε = 10⁻⁵, 2×10⁻⁵` agrees. `−(1/4) Σ M²` is half of that and does not. The same Wick count gives `Cov(X⁴, Y⁴) = 24c⁴ + 72 v_x v_y c²`, so the quartic inclusion in the attempt also starts at `O(c²)`.

**S5 (the constant on `Z³`): holds.** `G(0) − G(e₁) = 1/6` fixes the normalization `G = L⁺`. The quadrature matches Watson's product over `6` to `1e-10`. `μ = G(0) − G(2e₁) = 0.209841695316`, and `A v_i = μ v_i` for the dipole `v_i` with `+1` on `+e_i` and `−1` on `−e_i`. The continuum second derivative `∂_i∂_j G ∼ (3n_i n_j − δ_ij)/(4π r³)` gives `tr(MMᵀ) ∼ 3/(2π² r⁶)`. Numerically `tr(MMᵀ) r⁶` is `0.173` at `r = 10` and `0.157` at `r = 20`, against `0.15198`, and the error falls as `r⁻²`. Dressing each dipole by `1/(1+εμ)` produces
`F r⁶ → −(3/(16π²)) ε_x ε_y α_x α_y`, `α = 2/(1+εμ)`.
Two vacancies: `α = 2.5311384`, constant `−0.12171197`. The exact-in-`G` vacancy interaction, on the complement of `(1,…,1)`, has `F r⁶ = −0.2371, −0.1383, −0.1254` at `r = 5, 10, 20`, approaching the constant. Against T4's two unit tilts the ratios are `5.995×10⁻⁵`, `1.106×10⁻⁶`, `3.144×10⁻⁸`.

**S6 (no `1/r`): holds.** Invariance under `θ → θ + c` means the inclusion depends only on bond differences, so its cross-covariance is a power series in `M = O(r⁻³)`. The slowest term is `O(r⁻³)`. It is never `O(r⁻¹)`. The cubic group on the six bonds is the 48 signed axis permutations. Burnside gives one invariant direction, `(1,…,1)`. `M` annihilates it for `r ≥ 2`, because `Σ_b d_b = L e_y` and `G L e_y` is constant off `y`. A cubic-invariant inclusion therefore loses the `O(r⁻³)` term and interacts at `O(r⁻⁶)`. A vacancy is this case: `A` really does have eigenvalue `1` on `(1,…,1)`, which is why the attempt's complement projection is required, and that projection is what S5 evaluates.

## What was not a failure

- The `r = 1` sign depends on the shared-bond convention. The task leaves it open. The claims for `r ≥ 2` do not.
- The continuum expansion was marked ASSUMED in the attempt. The limit it is used for is a finite, checked statement: `tr(MMᵀ) r⁶ → 3/(2π²)` and the vacancy `F r⁶` approaches `−0.12171197`. The error is `O(r⁻²)`, as a lattice correction at `O(r⁻⁸)` in `F` requires.

## Verdict

The attempt proves the task's (a), (b) for `r ≥ 2`, (c), and (d). The only correction of the prompt, the factor `1/2` rather than `1/4`, is the one the Gaussian moment requires.
