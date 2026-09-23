# J:derive:source-neutral-inclusion-attraction:a2: like inclusions attract as r⁻⁶ with a dressed constant; no rotation-invariant inclusion, quadratic or not, gives 1/r

**Provenance.**
- Worker `w-macbookpro90c72-j091d`, model `claude-opus-5-5`, one session. Unit a2 (attempt 2 of 4).
- **Plan, formed before reading the prior attempt:**
  - the matrix determinant lemma for rank-six stiffness changes;
  - the second order;
  - the continuum constant;
  - for (d), Gaussian integration by parts (Price's theorem) together with the cubic group acting on a site's six bonds.
- **The prior attempt a3** (worker `j0b3c`) is the same model family and has not been refereed. It already covers (a)–(d). Its exact torus `G` comes from an orbit reduction, and it lists the Gaussian interpolation identity as ASSUMED for non-quadratic inclusions.
- **What this attempt adds:**
  - an **independent confirmation by different machinery**: `G` on the `8³` torus by exact Fourier sums in `Q(√2)`, the `ε²` coefficient by exact determinants with Richardson extrapolation, and the `Z³` constants from the lattice Green function at 30 digits;
  - a **proof, not an assumption**, of (d) for arbitrary local rotation-invariant inclusions.
  Every number a3 reports that is recomputed here agrees.
- **Related earlier unit by the same model:** #8742 (source-direction rules; the Goldstone coupling in an ordered medium). It is not a premise here.
- **Setting.** Block 41's T4 (PR #8547, read on its branch) gives the held-tilt cost `−κab G(r)/(G(0)² − G(r)²)`.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Notation.**
- The field has weight `exp(−(κ/2)Σ_bonds(θ_u − θ_v)²)`, with the zero mode removed. `G = L⁺`, so the covariance is `G/κ`.
- The bonds at `x` are oriented outward, `d_b = e_x − e_{x+d}`, and `D_x` is the `N × 6` matrix of them. Then `A_x = D_xᵀGD_x` and `M_xy = D_xᵀGD_y`.
- An inclusion multiplies the stiffness of its six bonds by `1 + ε`.

**(a) (PROVED; CHECKED B1, B2).**
- For `r ≥ 2`,

  `F(x,y) = ½ log det(I − ε_xε_y (I + ε_xA_x)⁻¹ M_xy (I + ε_yA_y)⁻¹ M_yx)`,

  a `6 × 6` determinant, derived from Sylvester's identity on the zero-mode complement plus a Schur complement.
- At `r = 1` the shared bond enters with `(1+ε)² − 1` under the multiplicative convention, or `2ε` under the additive one.
- **Exact on the `8³` torus at `ε = −½`:**

  | r | F (exact) | second order |
  |---|---|---|
  | 2 | `−0.0035209463` | `−0.00284182` |
  | 3 | `−0.00020640211` | `−0.00016664` |
  | 4 | `−4.9346887·10⁻⁵` | `−3.968·10⁻⁵` |

  At `r = 1`: `+0.0030438` (multiplicative) and `−0.098304` (additive). These agree with a3 to all printed digits.

**(b) (PROVED; CHECKED B1, B2, C1, C2).**
- **Second order.** `F = −(ε_xε_y/2) Σ_{b at x, b' at y} (d_bᵀGd_{b'})² + O(ε³)`.
  - The coefficient is **½**, not the task's `¼`, because `Cov((d·θ)², (d'·θ)²) = 2(dᵀCd')²`.
  - Checked at `r = 2` by exact determinants at `ε = 10⁻⁶` and `2·10⁻⁶` with Richardson extrapolation: `−0.0113672742596` both ways.
- **The sign at every order** (`r ≥ 2`, `ε > −1`): like signs attract (`F < 0`), unlike signs repel.
- **Decay on `Z³`.**
  - `F·r⁶ → −(3/(16π²)) ε_xε_y α_xα_y`, with `α = 2/(1 + εμ)` and `μ = G(0) − G(2e₁) = 0.209841695316`.
  - At second order this is `−3ε²/(4π²)`.
  - Two vacancies give `α = 2.5311384` and the constant `−0.12171197`.
  - The exact vacancy `F·r⁶` is `−0.2371, −0.1383, −0.1254` at `r = 5, 10, 20`, approaching it.

**(c) (CHECKED C2).** Against two held unit tilts, `F_vac/F_tilt = 5.995·10⁻⁵, 1.106·10⁻⁶, 3.144·10⁻⁸` at `r = 5, 10, 20`, falling as `r⁻⁵`.

**(d) (PROVED; CHECKED D1).**
- **Setting.** Take any local inclusion `V_x` that is invariant under the medium's rotation `θ → θ + c`. It then depends only on the bond differences `X = D_xᵀθ` near `x`. Its interaction with another such inclusion is:
  - `O(r⁻³)` in general;
  - `O(r⁻⁶)` if it is also invariant under the cubic group about its site, as a record of unread content is;
  - never `1/r`.
- **Why.** In Price's expansion
  1. `Cov(f(X), g(Y)) = Σ_{n≥1} (1/n!) Σ C_{i₁j₁}⋯C_{iₙjₙ} ⟨∂ⁿf⟩⟨∂ⁿg⟩`, with `C = M_xy/κ = O(r⁻³)`.
  2. The first-order term is `u_xᵀCu_y`, with `u_x = ⟨∇e^{−V_x}⟩` in the six-bond space.
  3. For a cubic-invariant inclusion `u_x` is invariant under the 48-element group permuting the bonds. That representation has exactly one invariant direction, `(1,…,1)`.
  4. `M_xy(1,…,1) = D_xᵀG L e_y = 0` for `r ≥ 2`, so the first-order term vanishes and the interaction is `O(C²)`.
- **What `1/r` needs.** A coupling to `θ` itself, a held tilt (block 41 T4), which the rotation forbids.
- **Checked.** For the quartic inclusion `λΣ_b(d_b·θ)⁴`, the exact `O(λ²)` interaction `−λ²Σ(72s⁴c² + 24c⁴)` has no term linear in `c`.

## 2. Steps

**S1: exact `G` on the `8³` torus (CHECKED A1).**
- `G(r) = (1/N)Σ_{k≠0} Π_a cos(k_a r_a)/λ(k)`, with `λ(k) = Σ(2 − 2cos k_a)` and `cos(2πn/8) ∈ {0, ±1, ±√2/2}`.
- The sums are evaluated in `Q(√2)`. All 35 orbit values come out rational (`G(0) = 118783817/528855040`), `LG = δ − 1/512` holds exactly, and `ΣG = 0`.

**S2: the determinant formula (PROVED; CHECKED B1).**
- The stiffness matrix is `κ(L + D H Dᵀ)`. The columns of `D` annihilate constants, so on the complement of the zero mode `det(L + DHDᵀ)/det L = det(I + H DᵀL⁺D)` (Sylvester), and `κ` cancels in the four-term combination.
- For disjoint bonds, the block determinant factorises through a Schur complement into `det(I + ε_xA_x)·det(I + ε_yA_y)·det(I − …)`.

**S3: the sign (PROVED).**
- `L − D_xD_xᵀ` is the Laplacian of the graph without `x`'s bonds, hence positive semidefinite. So `A_x ≤ I`, and `I + εA_x > 0` for `ε > −1`.
- Put `T = √(ε_xε_y) (I + ε_xA_x)^{−1/2} M_xy (I + ε_yA_y)^{−1/2}` when `ε_xε_y > 0`. Then `exp 2F = det(I − TTᵀ)`.
- This lies in `(0, 1]`, because the full stiffness matrix is positive definite. So `F ≤ 0`.
- For `ε_xε_y < 0` the same steps give `det(I + TTᵀ) ≥ 1`, so `F ≥ 0`.

**S4: second order (PROVED; CHECKED B2).** Expand `log det(I − X) = −tr X + O(X²)`, which gives `−(ε_xε_y/2) tr(M Mᵀ)`.

**S5: the constant on `Z³` (PROVED given the Green function's asymptotics, ASSUMED: `∂_i∂_jG = (3n_in_j − δ_ij)/(4πr³) + O(r⁻⁴)`; CHECKED C1, C2).**
- **The dipole vectors.** Let `v_i` be the bond vector with `+1` on `+e_i` and `−1` on `−e_i`. Then `A v_i = μ v_i` exactly, with `μ = G(0) − G(2e₁)` (the other components cancel by symmetry). Also `G(0) − G(e₁) = 1/6` exactly.
- **The far field.** `M_xy ≈ −Σ_{ij} T_ij v_i v_jᵀ` with `T = ∂∂G`, and `tr(MMᵀ) ≈ 4ΣT_ij² = 3/(2π²r⁶)`.
- **Result.** `F·r⁶ → −(3/(4π²)) ε_xε_y/((1 + ε_xμ)(1 + ε_yμ))`.
- The `Z³` values are Bessel integrals `G(x) = (1/6)∫₀^∞ e^{−t}Π I_{x_i}(t/3)dt` with a two-term tail. `G(0)` matches Watson's closed form to `10⁻¹⁸`.
- The vacancy limit is taken on the complement of `(1,…,1)`, which `M` annihilates.

**S6: (d) (PROVED; CHECKED D1).**
1. **Price's identity.** For a Gaussian vector with covariance `Σ`, `∂E[h]/∂Σ_kl = ½E[∂_k∂_l h]` (for `k ≠ l` the two symmetric entries together give `E[∂_k∂_l h]`), because the Gaussian density satisfies the heat equation in `Σ`. It holds for `h` of polynomial growth.
2. **The expansion.** Taylor-expand in the cross-covariance `C`, keeping the blocks at `x` and `y` fixed. This gives the series above: each derivative in `C_ij` produces `∂_i ⊗ ∂_j`, and at `C = 0` the two expectations factorise.
3. **Bound.** `F(x,y) = −log(1 + Cov(e^{−V_x}, e^{−V_y})/(E e^{−V_x} E e^{−V_y}))`, which has the order of the covariance.
4. **The invariant direction.** The bond-permutation representation of the cubic group decomposes as `A₁g ⊕ E_g ⊕ T₁u`. Its invariant subspace is one-dimensional: by Burnside, the mean number of fixed bonds is 1, and this is CHECKED.

## 3. The first failing step

- **Nothing fails** for the questions asked.
- **The `r = 1` sign depends on a convention** the task leaves open. The multiplicative convention gives mild repulsion (`+0.0030` at `ε = −½`), the additive one attraction.
- **The `r⁻⁶` constant** rests on the standard asymptotics of the lattice Green function (ASSUMED). The exact `Z³` values at `r = 5, 10, 20` approach it as `r⁻²`.

## 4. What would finish it

1. The next term of the large-`r` expansion, `O(r⁻⁸)`, which is anisotropic on the lattice, with its cubic-harmonic coefficient.
2. Beyond the quadratic model: the ordered medium of blocks 39–41, where the tilt field is the actual content field of the record gas. Is its stiffness change at a record of unread content an `ε` of the kind treated here, and with what sign?
3. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/source-neutral-inclusion-attraction/w-macbookpro90c72-j091d/check.py
```

The run takes about 15 s. `G` on the torus and all determinants are exact (Fractions, `Q(√2)`); logs and the `Z³` Green function are at 30 digits. It prints A1, B1, B2, C1, C2 and D1, then the SUMMARY and HIT lines.

Standard mathematics used, none as authority:
- Sylvester's determinant identity and Schur complements;
- Price's theorem (Gaussian integration by parts);
- the lattice Green function's integral representation and its asymptotics;
- Burnside's lemma.
