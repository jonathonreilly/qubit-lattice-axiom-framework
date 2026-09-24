# the-two-source-interaction-under-light-cone-formation, attempt a1: aligned sources couple positively at every separation

Worker `w-macbookpro9927a-je0d3` (`claude-opus-5-5`), unit `J-derive-the-two-source-interaction-under-light-cone-formation-a1`.

**Sources.**
- **Blocks 90–93**, read as landed and narrowed on origin/main `0e6ad8285096`: 90 (#8692), 91 (#8696), 92 (#8703) and 93.
- **The clause.** Block 90's light-cone clause is block 92's "excluded re-recording clause". Every statement below is conditional on it, and nothing is adopted.

**Provenance and independence.**
- **The prior attempt.** `a2` (`w-jonathonsmac4f50-j7576`, claude-opus-5-5, another machine, same model family) has a HIT, not yet refereed. At claim time I saw only its one-line summary.
- **My plan, formed before opening a2's file.** Four points:
  1. two-source reversibility;
  2. a tilt identity that makes every cross term of log Z a cumulant of the source-free records;
  3. an exact factorisation of the stationary weight;
  4. the sign, from reflection positivity and `R̂ ≥ 0`.
- **What a2 already has.**
  - Point 1.
  - Point 2 at second order, as a "mutual alignment".
  - Point 4 for mirror pairs only. Its open item 3 is "A sign for every separation, for example through a correlation inequality for the sphere menu".
- **What I did instead.** I took a different route for the sign, Griffiths' first inequality, re-proved below at the scope used. It settles that item.
- **What is new here:**
  - the sign at every separation (step 5);
  - the all-orders cumulant form and the factorisation (steps 2–4). Their second-order content coincides with a2's and is credited.
- **Related earlier units of this worker.** #8837 (the small-`k` limit of the held-source response) and #9075 (the zero-field floor). Neither is used, except that the floor enters (b) through a2 and block 92.

## 1. What is attempted

**Setting** (blocks 90 and 91).
- **The records.** They are contents on the unit sphere with the uniform base measure; any menu invariant under each coordinate sign flip serves.
- **The update.** Each site draws a new record with weight `exp(β s′_x·(h_x(s) + εe_z + h(x)))`, where `h_x(s) = Σ_{d∈N₇} s_{x+d}` and `N₇ = {0, ±e_j}`.
- **The sources.** `h(x₁) = h₁` and `h(x₂) = h₂`, with `x₁ ≠ x₂`, `β > 0` and `ε ≥ 0`.
- **The site sum.** `σ(x) = s_{x,0} + s_{x,1}` is the sum of the two records at `x`, one per level.
- **The response.** `R(r) = 2β Cov(S_+(0), S_+(r)) = (β/2)⟨σ^α(0)σ^α(r)⟩`, per component, at zero field (block 91 T2).

**(a) What couples the sources.**
- **(a1) Reversible.** With both sources on both levels, the two-level law is

  `μ_h ∝ exp(βΣ_{x,d} s′_x·s_{x+d} + βεΣ(s_z + s′_z) + βh₁·σ(x₁) + βh₂·σ(x₂))`.

- **(a2) A tilt.** `μ_h` is the source-free two-level law tilted by `exp(βh₁·σ(x₁) + βh₂·σ(x₂))`. So

  `log Z(h₁,h₂) − log Z(0,0) = log E₀ exp(βh₁·σ(x₁) + βh₂·σ(x₂))`.

  Every cross term, at every order, is a mixed cumulant of `σ(x₁)` and `σ(x₂)` in the source-free law.
- **(a3) Second order.** At zero field the cross term is

  `β² h₁^α h₂^γ Cov₀(σ^α(x₁), σ^γ(x₂)) = 2β(h₁·h₂)R(x₁ − x₂)`.

  The third-order cross terms vanish, by the global flip.
- **(a4) No pair term in the formation law.** The update kernel is a product over sites, and each source enters only its own site. The unnormalised stationary weight factorises exactly:

  `w(h₁,h₂)·w(0,0) = w(h₁,0)·w(0,h₂)`.

  So the interaction is entirely the statistical dependence of the records the sources tilt. The formation law measures it through the joint law of the records at `x₁` and `x₂` over two consecutive ticks. At second order that is a2's mutual alignment, `∂⟨σ(x₁)⟩/∂h₂ = 2R`.

**(b) Separation** (a2 and blocks 91–92, credited).
- `R(0) − R(r) = N⁻¹Σ_{k≠0}(1 − cos k·r)R̂(k)` lies between block 92's floor applied to that sum and `Γ_L(r)`.
- New here: `0 < R(r) ≤ R(0)` at every `r`.

**(c) Sign.** This is the new exact result. For `β > 0`, all sites `x ≠ y`, all levels `l, l′` and every component `α`:
- `⟨s^α_{x,l} s^α_{y,l′}⟩₀ > 0` at zero field;
- with the uniform field `εe_z`, `ε ≥ 0`, the same for the transverse components `α = 1, 2`.
- Hence `R(r) > 0` (and `R_⊥(r) > 0` with the field) at **every** separation. Aligned sources have a strictly positive cross term at every distance, not only for mirror pairs.

## 2. Steps

0. **ASSUMED (supplied).**
   - Block 90's light-cone clause, which block 92's corrigendum marks as excluded by the axioms memo as written.
   - Block 91's held sources. Nothing is adopted.

1. **PROVED; CHECKED Q1 (reversible with two sources; block 91 T1's argument).**
   - `π̃_h(s) = exp(βεΣs_z + βΣ_i h_i·s_{x_i}) Π_x Z(h_x(s) + εe_z + h(x))`, where `Z` is the single-record normaliser.
   - `K(s′|s) = Π_x exp(βs′_x·(h_x(s) + εe_z + h(x)))/Z(·)`.
   - Their product is the exponent of `μ_h` in (a1). It is symmetric in the two levels because `N₇ = −N₇`.
   - Check Q1: every pair of levels on the doubled ring of four, with the two-valued menu and exact rational weights.

2. **PROVED; CHECKED Q3 (the tilt).**
   - The product in step 1 is the source-free one times `exp(βΣ_i h_i·(s_{x_i} + s′_{x_i}))`.
   - Normalising gives (a2). Check Q3: every pair of levels.

3. **PROVED; CHECKED Q4 (cumulants).**
   - `log E₀ e^{a·σ₁ + b·σ₂}` is the joint cumulant generating function, and its `a^α b^γ` coefficient is `Cov₀(σ₁^α, σ₂^γ)`.
   - At zero field the mean vanishes by the global flip `(s, s′) → (−s, −s′)`. The same flip kills the odd cumulants.
   - Rotation invariance gives `δ_αγ` for the sphere.
   - With block 91 T2, `β²Cov₀ = β²·(2/β)R = 2βR`.
   - With the field, the flips of `s¹` and `s²` make the covariance block diagonal: `2β(h₁^⊥·h₂^⊥R_⊥ + h₁^z h₂^z R_∥)`.
   - Check Q4: on the ring of six, with sources two sites apart:
     - the `ab` coefficient of the exact series equals `Cov₀(σ₁, σ₂) = 2804904263700/2797699210501`;
     - the `a²b` coefficient is `0`.

4. **PROVED; CHECKED Q2 (factorisation).**
   - In `π̃_h` the `Z`-factor at `x₁` carries only `h₁` and the one at `x₂` only `h₂`; every other factor is source-free. The identity in (a4) follows.
   - The kernel is a product over sites, each with its own source.
   - Check Q2: every state of the doubled ring of four.

5. **PROVED; CHECKED G1–G3 (Griffiths' first inequality on the doubled graph, sphere menu).**
   - **(i) Expansion.** Expand
     `exp(βΣ_{edges}Σ_α s_u^α s_v^α + βεΣ_v s_v^3) = Σ_n (β^n/n!)(Σ_{e,α} s_u^α s_v^α + εΣ_v s_v^3)^n`.
     - Every term is a monomial in the components, with a non-negative coefficient (`β, ε ≥ 0`).
     - Multiplying by `s^α_a s^α_b` keeps that.
     - The series converges absolutely (bounded records, finite graph), so it can be rearranged.
   - **(ii) Each monomial has a non-negative mean.** Under the product measure, the mean is `Π_v E[Π_α (s_v^α)^{m_{v,α}}]`.
     - If some exponent is odd, the factor is `0`, because the menu is invariant under `s^α → −s^α`.
     - Otherwise it integrates a non-negative function.
     - For the sphere, `E[x^{2a}y^{2b}z^{2c}] = (2a−1)!!(2b−1)!!(2c−1)!!/(2K+1)!!`, with `K = a+b+c`. Proof: write a standard Gaussian vector as `x = rω` with `ω` uniform and `r` independent. Then `E[x_i^{2k}] = (2k−1)!!` and `E[r^{2K}] = 2^KΓ(K + 3/2)/Γ(3/2) = (2K+1)!!`.
     - So `Z₀⟨s^α_a s^α_b⟩ ≥ 0`.
   - **(iii) Strictness.**
     - The doubled graph is connected: `(x,0)` is joined to `(x+d,1)` for `d ∈ N₇`.
     - Take a path `a = v₀, …, v_n = b`. Choosing each of its edges once, with component `α`, gives a term `β^n` times a monomial in which every vertex has `(s^α)²`. Its mean is `3^{−(n+1)} > 0`.
     - Every other term is `≥ 0`, so `⟨s^α_a s^α_b⟩₀ > 0`.
   - **(iv) Covariance.** At zero field every mean vanishes. With the field, `⟨s^α⟩ = 0` for `α = 1, 2`, by the flip of that component, which keeps the field term. So the covariances equal these correlations, and `R(r) = (β/2)Σ_{l,l′}⟨s^α_{0,l}s^α_{r,l′}⟩ > 0`.
   - **(v) Other menus.** The same holds for every menu invariant under each coordinate sign flip, such as `±1` or the cube and octahedron vertices.
   - **Checks.**
     - G1: with the two-valued menu on the doubled ring of six, each correlation is `P_r(w)/Q(w)` with `w = tanh β` and non-negative integer coefficients, for `r = 1, 2, 3`; `r = 2` is not a mirror pair. The lowest orders are `w, w², w³`.
     - G2: the sphere moments against direct integration, for `a + b + c ≤ 4`.
     - G3: the sphere menu on the doubled ring of four. The `β`-series of the unnormalised `⟨s¹(0)s¹(2)⟩` at the non-mirror separation 2 is `0, 0, 2/27, 0, 22/135` through `β⁴`. With a field `½e_z`, transverse, across levels, it is `0, 0, 0, 2/27, 0`.

6. **PROVED ((b); a2 and blocks 91–92 credited).**
   - `R̂ ≥ 0`, because it is a variance, gives `R(r) ≤ R(0)`.
   - Step 5 gives `R(r) > 0`.
   - The bracket of `R(0) − R(r)` is a2's step 3.

7. **The meaning under the formation reading.**
   - Held sources do not interact through the update rule or through the stationary weight (step 4).
   - Their cross term is the dependence of the source-free records at the two sites: their covariance at second order, and their joint cumulants at higher orders (steps 2–3).
   - For aligned sources it is positive at every separation (step 5): each source turns the other's records toward itself at every distance.
   - Read as a free energy, `−β⁻¹ log Z` falls by `2(h₁·h₂)R` for aligned sources. That reading is not needed.

**Mutation census.** Each mutation is caught, in its own family:
- a one-sided past fails Q1 (and G3);
- a wrong tilt exponent fails Q3;
- an antiferromagnetic edge fails G1;
- a wrong sphere moment fails G2.

## 3. Where the route stops (not claimed)

- **The longitudinal sign with a field.** It needs Griffiths' second inequality for the sphere menu on this graph. That is not proved here; for the `±1` menu it is classical and not used.
- **Monotonicity** of `R` in separation or in `β`.
- **The real-space shape** of `R` (as in a2).
- **The signs of higher cross terms.** Their fourth-cumulant signs are not known for the sphere.
- **Movable sources.**

## 4. What would finish it

- **Griffiths' second inequality** for the sphere menu on the doubled graph. It would give the longitudinal sign and monotonicity in `β`.
- **The small-`k` limit** of `R̂(k)E(k)` (blocks 91 and 92; this worker's #8837 made the Bogoliubov step exact).
- **Sources that are themselves formed records** (a2's item 1).

## Checks (`check.py`, about 30 s)

| Family | What it checks |
|---|---|
| Q1–Q4 | Reversibility, factorisation, tilt and cumulants, with the two-valued menu on doubled rings of 4 and 6; exact rationals |
| G1 | Griffiths I for the two-valued menu at separations 1, 2 and 3 |
| G2 | Sphere moments |
| G3 | Sphere-menu series at a non-mirror separation, with and without a field |
