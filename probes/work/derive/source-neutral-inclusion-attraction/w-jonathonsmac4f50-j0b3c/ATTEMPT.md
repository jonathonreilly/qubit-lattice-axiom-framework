# source-neutral-inclusion-attraction, attempt 3 of 4: two neutral inclusions attract at every order, as r⁻⁶ with a dressed constant, and never as 1/r

Worker `w-jonathonsmac4f50-j0b3c` (`claude-opus-5-5`), unit `J-derive-source-neutral-inclusion-attraction:a3`.

**Provenance.**
- No attempt of this problem had been delivered: a1 and a2 left nothing on `ai/probes`.
- Definitions come from the task statement and from block 41 (PR #8547, read on its branch): the quadratic model, and T4's cost of two held tilts. Block 41 is from the same model family as me and is unrefereed.
- My plan was fixed before any reading beyond block 41's T4: the matrix determinant lemma, a Schur complement for the sign, and a multipole argument for (d).
- Imports marked ASSUMED:
  - the asymptotics of the `Z³` lattice Green function, used only for the constant of the `r⁻⁶` law;
  - the Gaussian interpolation identity, used only for the non-quadratic remark in (d).

## 1. What is claimed

**Setting.**
- The field is `θ` on the `L³` torus, or on `Z³`, with weight `exp(−(κ/2) Σ_bonds (θ_u − θ_v)²)` and the zero mode removed.
- `L` is the graph Laplacian and `G = L⁺`, so the covariance is `G/κ`.
- An inclusion at `x` multiplies the stiffness of its six bonds by `1 + ε`. At `r = 1` the shared bond gets `(1+ε_x)(1+ε_y)`; that is the multiplicative convention, and the additive one is `1 + ε_x + ε_y`.
- For a bond `b = (u, v)`, `d_b = e_u − e_v`, and `M_xy = D_xᵀ G D_y` is the `6 × 6` matrix of second differences of `G` between the bonds of `x` and of `y`.
- `F = ½ log det` on the zero-mode complement, and `F(x,y) = F_both − F_x − F_y + F_none`.

> **(a) Exact formula.** `exp(2F(x,y)) = det(I + H Dᵀ G D) / [det(I + ε_x M_xx) det(I + ε_y M_yy)]`, taken over the bonds of both
> inclusions (`H` = their stiffness changes). For `r ≥ 2` (disjoint bonds) it is one `6 × 6` determinant:
> `F(x,y) = ½ log det(I − ε_x ε_y A_x M_xy A_y M_yx)`, with `A = (I + εM₀₀)⁻¹`.
> For vacancies (`ε = −1`), `A` is taken on the complement of `(1,…,1)`, which `M_xy` annihilates.
>
> **(b) Sign at every order, second order, decay.**
> - For `r ≥ 2` and `ε_x, ε_y > −1`, `0 < exp(2F) ≤ 1` when `ε_xε_y > 0` (attraction) and `exp(2F) ≥ 1` when `ε_xε_y < 0`
>   (repulsion). The inequalities are strict unless `M_xy = 0`. The vacancy limit is included.
> - The second-order term is `F = −(ε_xε_y/2) Σ_{b∈x, b'∈y} (d_bᵀ G d_{b'})² + O(ε³)`.
>   The task's coefficient `¼` is `½` under the stated normalisation, because `Cov((d·θ)², (d'·θ)²) = 2(dᵀCd')²`.
> - At `r = 1` the shared bond adds `+ε² d_sᵀ G d_s` (multiplicative convention). There the sign is **not** fixed: at `ε = −½`,
>   `F = +0.0030` (multiplicative) against `−0.098` (additive).
> - On `Z³`, `F(r)·r⁶ → −(3/(16π²)) ε_xε_y α(ε_x)α(ε_y)`, with `α(ε) = 2/(1 + ε(G(0) − G(2e₁)))`. That is
>   `−3ε²/(4π²)` at second order, and `−0.121712` for two vacancies, where `α(−1) = 2.53114`.
>
> **(c) Against two held tilts** (block 41 T4, `−κab G(r)/(G(0)² − G(r)²)`, `κab = 1`). Two vacancies give ratios
> `F_vac/F_tilt = 6.00·10⁻⁵, 1.11·10⁻⁶, 3.14·10⁻⁸` at `r = 5, 10, 20`, falling as `r⁻⁵`.
>
> **(d) No rotation-invariant inclusion gives `1/r`.**
> - In the quadratic model, an inclusion unchanged by the medium's rotation `θ → θ + c` couples only to differences of `θ`.
> - Its quadratic part is `−Σ_{u<v} Q_uv (e_u − e_v)(e_u − e_v)ᵀ`, and its linear part has zero sum.
> - So it interacts at order `r⁻³` at most (dipole–dipole). If it is also even in `θ`, the order is `r⁻⁶`.
> - A `1/r` term needs a charge (`Σh ≠ 0`), which is a held tilt, and that is not rotation invariant.

## 2. The steps

1. **CHECKED (E0).** `G = L⁺` is computed exactly on the 4³ and 8³ tori. `G` is invariant under the cubic group and
   reflections, so the equation `LG = δ − 1/N` reduces to its orbits (35 unknowns on 8³), with `Σ G = 0` replacing one equation.
   Verified at every site.
2. **PROVED + CHECKED (A1, A2): the formula.**
   - `K = κ(L + D H Dᵀ)`. The columns of `D` annihilate constants, so on the zero-mode complement Sylvester's identity gives
     `det(L + DHDᵀ)/det L = det(I + H Dᵀ L⁺ D)`. `κ` cancels in the four-term combination.
   - For `r ≥ 2`, `H = diag(ε_x I, ε_y I)`, and the block determinant is
     `det(I + ε_xM_xx) det(I + ε_yM_yy) det(I − ε_xε_y A_yM_yxA_xM_xy)`. Then use `det(I − XY) = det(I − YX)`.
   - For `ε = −1`:
     - `M_xx 1 = D_xᵀ G L e_x = D_xᵀ(e_x − 1/N) = 1`, so `1` is the singular direction of `I − M_xx`.
     - `M_xy 1 = D_xᵀ(e_y − 1/N) = 0`, and likewise `1ᵀM_xy = 0`, for `r ≥ 2`.
     - So `A_ε M_xy` extends continuously to `ε = −1` through the inverse on `1⊥`.
   - Checked exactly against the four `64 × 64` determinants on the 4³ torus (five cases, including `r = 1` under both
     conventions), and the `6 × 6` against the `12 × 12` form on the 8³ torus at `r = 2, 3, 4`.
3. **PROVED + CHECKED (B1): second order.**
   - `log det(I + E) = tr E − ½ tr E² + O(E³)`. For `r ≥ 2` the order-`ε` terms cancel between the four determinants, and at
     order `ε²` what remains is `−ε_xε_y tr(M_xy M_yx) = −ε_xε_y Σ M_xy²`.
   - At `r = 1` the shared bond's `ε²` in `(1+ε)² − 1` adds `ε² M_ss`.
   - Checked as an exact series in `ε` (sympy, exact matrices) on the 8³ torus at `r = 1…4`.
   - The table of exact `F` against `F₂` at `ε = −½` (for instance `r = 2`: `−0.0035209` against `−0.0028418`) shows the finite-`ε`
     dressing of step 5: the ratio is `1.24` ≈ `1/(1 − μ/2)²`.
4. **PROVED + CHECKED (B2): the sign at every order, `r ≥ 2`.**
   - *(i)* `L − D_UD_Uᵀ` is the Laplacian of the rest of the graph, so it is positive semidefinite. Hence `D_UD_Uᵀ ≤ L`,
     `‖L^{+/2}D_U‖ ≤ 1`, and `0 ≤ M_U = D_UᵀL⁺D_U ≤ I`. For `ε > −1`, `I + εM₀₀ ≥ (1+ε)I > 0`, so `A_x`, `A_y` are positive
     definite.
   - *(ii)* Put `X = A_x^{1/2} M_xy A_y^{1/2}`. Then `A_xM_xyA_yM_yx` is similar to `XXᵀ`, so
     `exp(2F) = Π_i (1 − ε_xε_y σ_i²)`, with `σ_i` the singular values of `X`.
   - *(iii)* Like signs.
     - Put `E = diag(|ε_x|I, |ε_y|I)`. The matrix `S = I ± E^{1/2}M_UE^{1/2}` is positive definite: this uses
       `E^{1/2}M_UE^{1/2} ≥ 0` for `+`, and `≤ max|ε| I < I` for `−` when `−1 < ε < 0`.
     - The Schur complement of `S` is then positive definite. By congruence with `A_y^{1/2}`, every `ε_xε_yσ_i² < 1`, so
       `0 < exp(2F) ≤ 1`.
   - *(iv)* Unlike signs: every factor is `≥ 1`.
   - *(v)* `ε = −1` follows by continuity.
   - Checked with exact rational comparisons at `r = 2, 3, 4` on the 8³ torus, for five like-sign pairs (vacancies included) and
     three unlike-sign pairs.
5. **PROVED (algebra) + ASSUMED (lattice asymptotics) + CHECKED (B3): decay and constant.**
   - The asymptotic step is ASSUMED: `G(n) = 1/(4π|n|) + O(|n|⁻³)` on `Z³`, with second differences equal to `∂∂G + O(r⁻⁴)`. Under it,
     `M_xy = −PᵀT(r)P + O(r⁻⁴)`, with `T = ∂∂(1/(4πr))` and `P` the `3 × 6` bond-to-axis map (`PPᵀ = 2I`).
   - `A` commutes with the cubic group, and the odd bond vectors form one irreducible representation (T₁ᵤ). So `PAPᵀ = αI` with
     `α = 2/(1 + εμ)`, where `μ` is the odd eigenvalue of `M₀₀`:
     `μ = m₀ − m₁ = 2(G(0) − G(e₁)) − (G(0) − 2G(e₁) + G(2e₁)) = G(0) − G(2e₁)`.
   - Then `2F = −ε_xε_y tr(A_xM_xyA_yM_yx) + O(r⁻¹²) = −ε_xε_y α_xα_y Σ_ij T_ij² + …`. Here
     `Σ T_ij² = 3/(8π²r⁶)`, checked symbolically.
   - NUMERIC on `Z³`: `G` by the Bessel integral `∫₀^∞ e^{−6t} Π I_{n_i}(2t) dt` at 25 digits, with the lattice-Laplace residual
     below `10⁻²⁰`. Results:
     - `μ = 0.209841695316`;
     - `F₂r⁶ = −0.1492, −0.0865, −0.0783, −0.0766` at `r = 5, 10, 20, 40`, against `−3/(4π²) = −0.07599`;
     - `F_vac r⁶ = −0.2371, −0.1383, −0.1254, −0.1226` against the predicted `−0.121712`, within 1% at `r = 40` with `O(r⁻²)`
       corrections.
6. **NUMERIC (C1): (c).**
   - `F_tilt = −G(r)/(G(0)² − G(r)²)` (block 41 T4, `κab = 1`) falls as `1/r`, and `F_vac` as `r⁻⁶`.
   - Ratios `5.9951·10⁻⁵, 1.1063·10⁻⁶, 3.1437·10⁻⁸` at `r = 5, 10, 20` along an axis.
   - The ratio scales as `1/(κab)`.
7. **PROVED + CHECKED (D1): (d).**
   - Take `U_x(θ) = ½θᵀQ_xθ + h_xᵀθ`, supported near `x`. `U(θ + c1) = U(θ)` for all `θ`, `c` forces `Q_x1 = 0` and `h_xᵀ1 = 0`.
   - A symmetric `Q` with zero row sums is `−Σ_{u<v} Q_uv(e_u − e_v)(e_u − e_v)ᵀ` (checked for random rational `Q` on a
     2 × 2 × 2 neighbourhood). So the determinant part of the interaction has step 2's structure, with difference vectors in place
     of bonds: second differences of `G`, which are `O(r⁻³)`, giving `F = O(r⁻⁶)`.
   - The linear part contributes the cross term `−h_xᵀ G h_y/κ + …`. With `Σh_x = Σh_y = 0`, the Taylor expansion of
     `G(u − v)` about `x − y` loses its monopole term, and the first surviving term is `(Σ_u h_x(u)(u−x))·∂∂G·(Σ_v h_y(v)(v−y))`,
     which is `O(r⁻³)`.
   - A `1/r` term requires `Σh ≠ 0`: a charge, which is block 41's held tilt and not rotation invariant.
   - *General local shift-invariant `U`* (not quadratic), at second order in the coupling: `F = −Cov(U_x, U_y)`. `U_x` is a
     function of the Gaussian vector `D_xᵀθ`. The Gaussian interpolation identity (**ASSUMED**) gives
     `|Cov| ≤ ‖D_xᵀGD_y‖ · (E‖∇U_x‖²)^{1/2} (E‖∇U_y‖²)^{1/2} / κ` (Cauchy–Schwarz, since the interpolated pair has the same marginals), which is `O(r⁻³)`; for even `U`, the first-order Hermite terms vanish and it is
     `O(r⁻⁶)`.

## 3. Where this stops

- **Nothing on the route fails.** (a), (b), (c) and (d) are answered. The limits:
  - The constant of the `r⁻⁶` law uses the ASSUMED lattice Green asymptotics. It is supported numerically to 1% at `r = 40`,
    and not proved here.
  - The contact case `r = 1` depends on a convention the task does not fix. The multiplicative one, which is natural for
    vacancies, makes adjacent half-vacancies repel at `ε = −½`.
  - (d) is exact for quadratic-plus-linear inclusions, and at second order for general local ones. A non-perturbative statement
    for general non-Gaussian inclusions would need a cluster expansion.
- The quadratic model is block 41's stand-in for the ordered medium, with a single scalar tilt. For the six-axis medium,
  block 41 found no long-range kernel at all, and nothing here changes that.

## 4. What would finish it

1. A proof of the lattice Green asymptotics used in step 5. It is classical, but is to be re-proved at this scope or cited
   exactly.
2. The two-component tilt: the quadratic model for the transverse tilt `(θ₁, θ₂)` of an ordered sphere medium, where
   "rotation invariant" includes rotations about the order axis. The same argument should give `r⁻⁶` with a tensor-valued
   dressing.
3. The link to the record layer: the actual `ε` of a record of unread content in an ordered medium, from block 41's law with
   vacancies.
4. A referee from another model family, particularly for step 4 (the every-order sign) and step 5 (the dressing `α`).

## 5. Running it

```
python3 probes/work/derive/source-neutral-inclusion-attraction/w-jonathonsmac4f50-j0b3c/check.py
```

- It has 8 lines.
- E0, A1, A2, B1, B2 and D1 are exact (`fractions`, `sympy`). B3 is exact symbolic algebra together with labelled `Z³`
  numerics, and C1 is numeric.
- It runs in about 80 seconds, most of it the `Z³` Bessel quadratures.
