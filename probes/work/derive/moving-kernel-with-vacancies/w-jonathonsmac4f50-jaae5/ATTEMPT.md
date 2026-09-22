# moving-kernel-with-vacancies, attempt 1 of 4: the twist moves the empty sites too, the scale sets the stiffness, and at the neutral scale the route closes

Worker `w-jonathonsmac4f50-jaae5` (`claude-opus-5-5`), unit `J-derive-moving-kernel-with-vacancies:a1`.

**Provenance.** Attempts `a2`, `a3` and `a4` were written by `claude-opus-5` workers on this machine: the same model family as
me (Claude), a different model version. The claim printout showed their one-line summaries. I formed my plan (below) before
reading their files. What I found contradicts `a3`'s central inequality, which `a4` and `a2` build on (§2, step 9). This is
therefore a disagreement within one model family. The referee from another family that `a2` already asks for is needed for all
four attempts. Outside inputs: block 39 (PR #8530; definitions, T5), block 19 (PR #8153; the Gaussian-domination template, which I
re-prove at this scope) and, only for an optional sharper constant, block 22's bracket on `3G(0)` (ASSUMED).

## 1. What is claimed

**Setting** (block 39 and the unit). A torus `T` with even sides, `N` sites and one bond `(x, x+e_i)` per site and direction.
On a side-2 direction the pair is joined twice. A site is empty (`∅`) or carries a content `s`. The **sphere menu** has
`s ∈ S²`, with a priori measure `δ_∅ + z·(uniform probability on S²)`. The **two-valued menu** has `s = ±1`, with
`δ_∅ + z·(counting)`. The bond kernel is `B(∅,·) = B(·,∅) = 1` and `B(s,s') = c e^{β s·s'}`. The law is
`∝ Π_b B(u_x,u_y)`. The records' field is `σ_x = n_x s_x`, with `n_x = 1[x occupied]`. Its transform is
`σ̂^e(k) = N^{-1/2} Σ_x e^{ik·x} σ_x·e`, and `E(k) = Σ_i 2(1 − cos k_i)`. The densities are `ρ = ⟨n_x⟩` and `ρ₂ = ⟨n_x n_y⟩`
on a bond.

Let `c₀(γ) = γ/sinh γ` (sphere) or `1/cosh γ` (two-valued), with `c₀(0) = 1`. It decreases strictly from `1` to `0` (F5). The
neutral scale of blocks 39–40 is `c₀(β)`. For `c₀(β) ≤ c < 1` let `γ(c)` be the root of `c₀(γ) = c`, and set `γ(c) = 0` for
`c ≥ 1`. Finally let `β_A(c) := β − γ(c)`.

> **(a) What the twist twists.** For every `β'`,
> `B(u,u') = e^{(β'/2)(n+n')} e^{−(β'/2)|σ−σ'|²} · R_{β−β'}(u,u')`, where `R_γ` is the vacancy kernel with the same `c` and
> coupling `γ` (F1). The Gaussian factor is a function of the **embedded field** `σ = n s`, with the empty state at the origin
> of `R^D`. The twist replaces `σ_x` by `σ_x − φ_x e` at **every** site, empty ones included:
>
> `Z_{β'}(φ) = ∫ Π_b e^{(β'/2)(n_x+n_y)} e^{−(β'/2)|σ_x − σ_y − (φ_x − φ_y)e|²} R_{β−β'}(u_x,u_y) Π_x dμ(u_x)`.
>
> A bond with an empty end **is** twisted: for `x` occupied and `y` empty its Gaussian factor is
> `e^{β'/2} e^{−(β'/2)|s_x − (φ_x−φ_y)e|²}`, which is not `1`. This is forced. The linear term is the Laplacian term
> `E(k)Σσψ` only when every bond is twisted (A1, all `3⁸` configurations of the `2×2×2` torus). Twisting only record–record
> bonds gives something else (X3).
>
> **(b) Theorem A (split domination; infrared bound).** Suppose `0 ≤ β' ≤ β` and `c ≥ c₀(β − β')`. Then `Z_{β'}(φ) ≤ Z` for
> every twist, and for every `z`, every component `e` and every `k ≠ 0`,
>
> `⟨|σ̂^e(k)|²⟩ ≤ 1/(β' E(k))`,  best at `β' = β_A(c) = β − γ(c)`.
>
> For `c ≥ 1` this is block 19's bound `1/(βE(k))` itself, whatever `z` and `ρ`. The sum rule is
> `Σ_e Σ_k ⟨|σ̂^e(k)|²⟩ = Nρ`.
>
> **Theorem B (small twists, full `β`; two-valued menu).** For
> `c ≥ c₁(β) = ((1+β²) sinh β − β cosh β)/(sinh β cosh β − β)`, the bound holds with the full `β`:
> `⟨|σ̂(k)|²⟩ ≤ 1/(βE(k))`. Here `c₀ < c₁ < 1`: `c₁ = 0.99249, 0.91112, 0.71508, 0.28323` at `β = 1, 2, 3, 5`, against
> `c₀ = 0.64805, 0.26580, 0.09933, 0.01348`. For the sphere menu the corresponding threshold is computed numerically
> (`0.99666, 0.83758, 0.45606, 0.09512` at `β = 1, 3, 5, 8`). It is not proved there.
>
> **(c) Long-range order and the obstruction.** On `Z³` (sphere), `M² ≥ ρ − 3G(0)/β_A(c)`. So long-range order holds once
> `β_A(c)·ρ > 3G(0)`, and `G(0) ≤ √3π/8` suffices for an explicit constant: `(β − γ(c))ρ > 3√3π/8 ≈ 2.04`. The criterion uses
> **no bond density and no correlation inequality**. **At the neutral scale `c = c₀(β)` the route closes.** There `β_A = 0`, and
> no partial twist strength survives even small twists (N2). Moreover the infrared bound with `β` is **false** there:
>
> **X1 (exact).** Take the `2×2×2` torus, two-valued menu, `e^β = 3`, `c = c₀ = 3/5`, `z = 1/8` and `k = (π,π,π)`. Then
> `⟨|σ̂(k)|²⟩ = 4295671717826064002261/38505646859840596246081 = 0.111560…`, with `E = 12`, so `⟨|σ̂(k)|²⟩ β E(k) > 1.4707`.
>
> **(d) The stiffness.** In the proved bound the coefficient of `1/E(k)` is `1/β_A(c)`. It depends on the scale `c` through
> `γ(c)`, and not on the density or the fugacity. For the two-valued menu it is `1/β` from `c₁(β)` up. `a3`'s coefficient
> `1/(βρ₂)` is not what the argument yields, and it is false at the neutral scale:
>
> **X2 (exact).** Take the `2×2×2` torus, `e^β = 20`, `c = c₀ = 40/401`, `z = 1/5` and `k = (π,π,π)`. Then `ρ = 0.8002`,
> `ρ₂ = 0.6882`, and `⟨|σ̂(k)|²⟩ β ρ₂ E(k) > 1.8164`.
>
> The sphere menu fails the same way numerically (N3). On rings at the neutral scale, the per-component full-`β` bound is
> exceeded by `1.0212, 1.4290, 2.0870` at `β = 3, 5, 8`. The `ρ₂` form is exceeded, `1.0335`, at `β = 8` on the 4-ring.

## 2. The steps

1. **PROVED + CHECKED (F1).** The factorization. `|σ − σ'|² = n + n' − 2nn' s·s'` because `n² = n` and `|s| = 1`. If `nn' = 0`
   both sides are `1`. If `nn' = 1`, then `e^{β'} e^{−β'(1 − s·s')} c e^{(β−β')s·s'} = c e^{βs·s'}`. Checked symbolically for
   the four occupation pairs.
2. **PROVED + CHECKED (F2–F4).** `R_γ` is a sum of products with non-negative coefficients exactly when `c ≥ c₀(γ)`.
   - *Two-valued:* `e^{γss'} = cosh γ + ss' sinh γ`, so `R_γ = 1 + (c cosh γ − 1)nn' + (c sinh γ)(ns)(n's')`. This is checked on
     all nine state pairs. The complement of the empty state has eigenvalues `2c cosh γ − 2` and `2c sinh γ`.
   - *Sphere:* `e^{γt} = Σ_ℓ a_ℓ P_ℓ(t)` with `a_ℓ = ((2ℓ+1)/2)(γ^ℓ/(2^ℓ ℓ!)) ∫(1−t²)^ℓ e^{γt}dt > 0` (Rodrigues;
     checked for `ℓ ≤ 4`), and `a₀ = sinh γ/γ`. With the addition theorem for `P_ℓ(s·s')` (named import):
     `R_γ = 1 + (c a₀ − 1)nn' + c Σ_{ℓ≥1} a_ℓ (4π/(2ℓ+1)) Σ_m (nY_ℓm(s))(n'Ȳ_ℓm(s'))`.
   - The converse also holds. If `c a₀ < 1`, uniform point sets on the sphere give a negative form, which is block 39's T5 at this
     coupling.
3. **PROVED.** The crossing kernel is a sum of squares. On pairs (state, shift) let `τ = σ − ae`. Then
   `𝒦 = [e^{(β'/2)n − (β'/2)|τ|²}][same at the other end] · e^{β'τ·τ'} · R_{β−β'}`, and
   `e^{β'τ·τ'} = Σ_α (β'^{|α|}/α!) τ^α τ'^α`. Multiplying this by step 2's expansion gives `𝒦 = Σ_j λ_j h_j ⊗ h̄_j` with every
   `λ_j ≥ 0`, for **every** pair of shifts, provided `c ≥ c₀(β−β')`.
4. **PROVED.** Cauchy–Schwarz through a bond plane. Split `T` into halves `H^±` by a plane bisecting bonds, and its antipode;
   the crossing bonds join `x` to `θx`. Expanding every crossing factor,
   `Z_{β'}(φ) = Σ_J Λ_J I_J(φ|_{H+}) · conj(I_J(φ|_{H−}∘θ))`, with `Λ_J ≥ 0`. Hence
   `Z_{β'}(φ)² ≤ Z_{β'}(φ^{(+)}) Z_{β'}(φ^{(−)})`, where `φ^{(±)}` copies one half's field onto the other by reflection.
5. **PROVED.** Domination. `Z_{β'}` depends on `∇φ` only, it is continuous, and
   `Z_{β'}(φ) ≤ Z e^{−(β'/2)Σ_b(∇_bφ)² + 2β'Σ_b|∇_bφ|}` because `|∇_bσ·e| ≤ 2`. So it attains its maximum. Take a maximizer
   with the most zero-gradient bonds. If some bond has a nonzero gradient, reflect through a plane that crosses it. By step 4
   both `φ^{(±)}` are maximizers. Together they have `2(#nz(φ) − #nz_crossing(φ)) < 2#nz(φ)` nonzero-gradient bonds, so one of
   them has fewer than `φ`, which contradicts the choice. Hence the maximum is at a constant field, and `Z_{β'}(φ) ≤ Z`.
6. **PROVED + CHECKED (A1).** The bound. Put `φ = λψ` with `ψ = cos(k·x)` or `sin(k·x)`. Then
   `Z_{β'}(λψ)/Z = ⟨exp(β'λX − (β'λ²/2)Σ_b(∇_bψ)²)⟩`, with `X = Σ_b(∇_bψ)(∇_bσ)·e = E(k)Σ_x σ^e_x ψ_x`. The last equality holds
   because the plane wave is a Laplacian eigenfunction on bonds counted with multiplicity; A1 checks it for every configuration
   and wavevector of the `2×2×2` torus. `⟨X⟩ = 0` by `s ↦ −s`. The second-order coefficient must be `≤ 0`, which gives
   `⟨(Σσ^eψ)²⟩ ≤ Σψ²/(β'E(k))`. Adding the cosine and sine terms, `⟨|σ̂^e(k)|²⟩ ≤ 1/(β'E(k))`. The fugacity enters only the site
   measures.
7. **PROVED (Theorem A's best strength; (c)).** `c ≥ c₀(β−β')` holds exactly when `β' ≤ β − γ(c)` (F5). Unitarity gives
   `Σ_eΣ_k⟨|σ̂^e(k)|²⟩ = Σ_x⟨n_x⟩ = Nρ`, so `M_N² = N^{-1}Σ_e⟨|σ̂^e(0)|²⟩ ≥ ρ_N − (3/β_A)N^{-1}Σ_{k≠0}1/E(k)`. As in block 19's
   G3, the Riemann sum tends to `G(0)`, and `1 − cos u ≥ 2u²/π²` gives `G(0) ≤ √3π/8`. Using block 22's `3G(0) < 0.76`
   instead is **ASSUMED**.
8. **PROVED modulo one CHECKED identification (Theorem B, two-valued).** Take the full-`β` kernel `𝒦` on the six points
   {3 states} × {two shifts `a, a'`}. The empty–empty and empty–occupied entries do not involve `c`, so the kernel is positive
   definite exactly when `c ≥ c_crit(Δ) = λ_max(G_oo⁻¹ G_eoᵀ G_ee⁻¹ G_eo)`, with `Δ = a − a'`, by the Schur complement.
   - *Limit.* For `0 < |Δ| < 1` the six `τ`-values are distinct and both blocks are nonsingular. Rewriting each pair as
     (value, difference quotient), the Gram converges as `Δ → 0` to the Gram of values and shift-derivatives. There
     `G_ee = diag(1, β)` (B1), and `c₁(β)` is symbolically an eigenvalue of the limit pencil (B1). It is the largest one, and
     `c₀ < c₁ < 1`: this is **CHECKED** at `β = 1/2, 1, 2, 3, 5, 8` to 40 digits (B2), and a small finite `Δ` reproduces it
     numerically (N1).
   - *Domination.* For `c > c₁`, choose `δ` so that `c_crit(Δ) < c` for `|Δ| ≤ 2δ`. On `D_δ = {max|φ_x| ≤ δ}`, each crossing
     pair's six-point eigendecomposition gives step 4's inequality. The decomposition restricted to one shift reproduces
     `Z(φ^{(±)})`. Steps 5–6 run inside the compact, reflection-invariant set `D_δ`.
   - *Endpoint.* At `c = c₁` the bound follows by continuity of finite-torus expectations in `c`.
9. **CHECKED, exact (X1, X2, X3), with controls (A2–A4).**
   - X1 and X2 are as in §1. The logarithms are bracketed by rational partial sums of `2 atanh`, with tail bounds (L0).
   - X3: on the 4-ring with `σ = (+1, +1, ∅, +1)` and `k = π/2`, the record-bonds-only linear term is `0`, while
     `E(k)Σσψ = 2`. So `a3`'s twist, in which a bond with an empty end weighs 1 whatever the twist, does not produce the
     structure factor of `σ`. Even if it did, its quadratic term `βΣ_b n_xn_y(∇ψ)²` has mean `βρ₂ E(k)N/2`, which would put `ρ₂`
     **in the numerator** of the bound, not the denominator.
   - Controls on the same torus hold as proved. With `c ∈ {1, 2}` and the full `β`, the largest value is `< 0.4313`. With
     `c = 4/5 = 1/cosh(ln 2)` and `β − γ = ln(3/2)` it is `< 0.3494`. At that last point the full-`β` value is recorded, not
     claimed: `> 0.9466`.
10. **PROVED + CHECKED (the obstruction at the neutral scale).**
    - (i) Theorem A allows only `β' = 0` at `c = c₀(β)`, because `c₀` decreases strictly.
    - (ii) **NUMERIC (N2).** Within the same family (twist strength `β'` times the untwisted remainder), the small-twist threshold
      exceeds `c₀(β)` for every tested `β' > 0`, and it increases with `β'`. At `β = 1`, the values for `β' = 0.01, 0.1, 1/2` are
      `0.65296, 0.69483, 0.84150`, against `c₀ = 0.64805`.
    - (iii) X1 shows that no argument can give the full-`β` bound there.
    - *Mechanism (a remark, not claimed).* At the neutral scale an empty neighbour weighs what a record of random content weighs
      on average. At low density records are therefore nearly free, with nearly independent contents. The structure factor then
      stays near `ρ` even at the largest wavevectors, and `ρβE_max > 1` as soon as `β > 1/(ρE_max)`.

## 3. Where this stops

- **Theorem B for the sphere menu is numerical.** Truncating the occupied span can only lower the supremum. The truncations at
  `ℓ ≤ 12` and `ℓ ≤ 20` agree to `10⁻²⁰` (N4), but a proof needs an upper bound.
- **The neutral scale has no infrared bound here.** Whether the neutral law has long-range order at large `β` and some density
  is open. The reflection-positivity route cannot settle it: the kernel is positive semidefinite (T5), yet it admits no Gaussian
  domination.
- **The best strength inside the family is known only at its ends.** Between `c₀` and `c₁` the best `β_eff(c)` (small twists,
  partial strength) is computed at sample points only. It is at least `β − γ(c)` (A) and equals `β` from `c₁` up
  (two-valued, B).
- **The counterexamples are small.** They use the `2×2×2` torus (doubled bonds) and rings. That is enough to refute an inequality
  that the argument would deliver on every even torus. It says nothing about the infinite-volume stiffness.
- **`a4` and `a2`.** Their inputs (`ρ₂ ≥ ρ²`, the FKG and GKS-II steps) serve `a3`'s criterion `βρ₂ρ > 3G(0)`. Wherever
  Theorem A applies (`c > c₀`), the criterion is `β_A(c)ρ > 3G(0)` and `ρ₂` plays no role. At the neutral scale `a3`'s premise is
  false (X2), so no long-range-order conclusion there rests on it. Their lattice-condition results stand on their own; I did not
  re-check them.

## 4. What would finish it

1. For the sphere menu, an upper bound for the infinitesimal-twist supremum (a closed form of the Legendre pencil). That would
   make Theorem B a theorem for the unit's own menu.
2. At the neutral scale, one of two things:
   - an infrared bound with some `β' > 0` by a route outside this family (another embedding of the empty state; domination only
     in the transverse directions of a clustered phase); or
   - a proof that none exists with `β'ρ > 3G(0)`, by making the nearly-free-records mechanism rigorous (a lower bound on `S(k)` at
     large `k`).
3. The best `β_eff(c)` on `(c₀, c₁)`, and whether `c₁` is sharp for the full-`β` bound. On rings the failures stop at
   `c ≈ 0.72` (`β = 2`), `0.64` (`3`) and `0.26` (`5`), against `c₁ = 0.91, 0.72, 0.28`. That was an exploratory scan, not
   recorded in `check.py`.
4. A referee from another model family, on this attempt and on `a2`–`a4`.

## 5. Running it

```
python3 probes/work/derive/moving-kernel-with-vacancies/w-jonathonsmac4f50-jaae5/check.py
```

It uses sympy, mpmath and numpy, and runs 19 checks in about a minute. The torus and log checks are exact rational arithmetic.
Items labelled `NUMERIC` use floating point or 40–60-digit mpmath and are not used by any exact claim.
