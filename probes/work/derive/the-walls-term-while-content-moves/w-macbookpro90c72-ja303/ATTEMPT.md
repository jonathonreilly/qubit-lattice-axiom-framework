# J:derive:the-walls-term-while-content-moves:a1

Worker `w-macbookpro90c72-ja303` (claude-opus-5-5). This is attempt 1 of 2, and there were no prior attempts. The plan is my own. All definitions come from the notes of block 60 (open PR #8590), block 55 (#8571) and block 54 (#8570) on their PR branches.

**Overlap.** This worker's model earlier produced #8753, on a ledger that transports the rates, in the same direction. Nothing from it is used here.

## (1) Exact statement

### Setting (block 60)

- **The box.** A finite box of Z³ with interior `I = {1..n}³`. The walls `W` are the sites outside `I` that have a neighbour in `I`. The bonds are the nearest-neighbour pairs with at least one end in `I`.
- **Fields.** Rates `w = e^u`, lengths `ℓ = e^λ = χ²`, and `N = wχ`. The walls are held at `w = ℓ = 1`, so neither `u` nor `λ` is varied there.
- **Content.** The content `⟨H⟩` has weight one in the rates and lives in `I`. It is one of two kinds:
  - supplied content at rest, `⟨H⟩ = Σ_x w_x ρ_x(t)` (block 60 T4's bodies, with the positions given as functions of the label);
  - a walker on block 54's walk `H = Σ_j σ_j S_j`, with `S_j = (T_j − T_j†)/(2i)` restricted to `I`. Its bonds are crossed at `√(w_x w_y)/(χ_x χ_y)` (block 60): `⟨H⟩ = ⟨ψ|H_eff|ψ⟩` with `H_eff = A H A` and `A = √w/χ`.
- **Ledger.** `𝓔 = ⟨H⟩ + F`, of weight one. The curvature member is `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`.
- **Kinetic term.** `K_λ` is any function quadratic in `λ̇`, of weight −1 in the rates, holding no rate of change of a rate and not involving the walls' rates. Block 60 T5's instance is `Σ_I c_k ℓ^s λ̇²/w`; the task takes `s = 3`, `c_k = −6K`.
- **Lagrangian.** `L = K_λ − 𝓔`, plus the walker's own first-order term `L_ψ = (i/2)(⟨ψ|ψ̇⟩ − ⟨ψ̇|ψ⟩)` when the content is a walker.
- **Solutions.** Euler–Lagrange in `λ_x` and stationarity in `u_x` (the rates are multipliers), for `x ∈ I`. The walker obeys `iψ̇ = H_eff ψ`.
- **Walls' term.** `Wt := Σ_{x∈W} ∂𝓔/∂u_x`. For the curvature member, `Wt = 8K Σ_{x∈W} (Δχ)_x = 8K Σ_{wall bonds} (χ_interior − 1)`, which is `8K ×` (the flux of `χ` into the walls).

### Claims

**T1.** For every configuration, `h := K_λ + ⟨H⟩ + F` satisfies `h − Wt = −Σ_{x∈I} ∂L/∂u_x`. Hence on solutions `h = Wt` at every label time. With `K_λ = 0` this is block 60 T1(c).

**T2.** Along solutions, `dh/dt = −∂L/∂t = ∂𝓔/∂t` at fixed `u`, `λ`, `ψ`. Only an explicit label dependence of the content moves the walls' term.

**(a) Supplied content at rest.**
- **Exact rate.** `dWt/dt = Σ_x w_x ρ̇_x` exactly, at every strength and speed. This is the power the supply delivers against block 54's pull (`−m∇w` on a body of bare energy `m`), that is, the work done on the supplied motion. It is not zero in general.
- **(a1) First order in the speed, any strength.** The fields differ from the static ones by terms with two label derivatives, so `dWt/dt = d/dt Wt_static(ρ(t)) + O(ρ̇ρ̈, ρ̇³)`. The walls track the instantaneous static ledger: for bodies, block 60 T4's `Σ m_i/χ_i`.
- **(a2) Weak field, curvature member, walls at 1,** with `g = (−Δ)⁻¹` on `I` (zero walls) and `λ⁽¹⁾ = gρ/(4K)`:

  `Wt = Σρ − (1/8K) ρ·gρ + c_k Σ_I (λ̇⁽¹⁾)² + O(ρ³)`.

  For `c_k = −6K` this is `Wt = Σρ − (1/8K)(ρ·gρ + 3 ρ̇·g²ρ̇) + O(ρ³)`.
  - The first non-vanishing order of `dWt/dt` is `−(1/4K) ρ̇·gρ`: second order in the bare energies, first order in the speed. It vanishes exactly when `ρ·gρ` is stationary along the motion.
  - On the `3³` interior with `K = 1/2`: a body carried from the centre to a face-adjacent site raises `Wt` by `(g_cc − g_oo)/(8K) = 3/952` (times the bare energy squared). A body carried towards a fixed one lowers it by `61/2856`.
  - Over a closed cycle of supplied motion the `O(ρ²)` change is zero, because the rate is a total derivative. Nothing is left behind, consistent with block 60 T5's absence of delay.

**(b) A walker with the fields slaved.**
- **(b1) Static law** (no kinetic term; the fields are stationary in `I` at each label time). `⟨H⟩ + F` is exactly constant, so by T1(c) the flux of `χ` into the walls is exactly constant.
- **(b2) With the lengths' kinetic term.** `K_λ + ⟨H⟩ + F = Wt` is exactly constant. `⟨H⟩ + F = Wt − K_λ` moves by `−dK_λ/dt`.
- **(b3) A different generator.** If the walker is evolved by some `G ≠ H_eff`, then under the static law `dWt/dt = d(⟨H⟩ + F)/dt = i⟨ψ|[G, H_eff]|ψ⟩`. An example is `G = √w H √w` while the ledger crosses bonds with the lengths. The rate is not zero in general.

**(c) Block 55's kept ledger.**
- Block 55 T2 holds the unit of rate by fixing `Σu` and removes the mean of the source (`μ`). Here the held walls hold the unit of rate instead: the interior rate equations carry no `μ`, and the kept ledger is `Wt`. What block 55 T4(b) called the ledger per site, `μ`, is carried by the flux into the walls.
- With lengths, block 55 T1 becomes `d⟨H⟩/dt = Σ e_x u̇_x − Σ τ_x λ̇_x`, with `τ = e` for block 54's walk.
- With a kinetic term for the lengths, the kept quantity is `K_λ + ⟨H⟩ + F`, not `⟨H⟩ + F`. Note that `K_λ < 0` when `c_k < 0`.

## (2) Steps

1. **PROVED (Euler).** Scale every rate, walls included: `w → s w` at fixed `λ`, `λ̇`, `ψ`. Then `𝓔 → s𝓔` and `K_λ → K_λ/s`. Differentiating at `s = 1` gives `Σ_all ∂𝓔/∂u_x = 𝓔` and `Σ_all ∂K_λ/∂u_x = −K_λ`. Since `L_ψ` holds no rate, `Σ_all ∂L/∂u_x = −K_λ − 𝓔 = −h`.

2. **PROVED (T1).** `K_λ` does not involve the walls' rates, so `Σ_W ∂L/∂u_x = −Σ_W ∂𝓔/∂u_x = −Wt`. Step 1 then gives `h = Wt − Σ_I ∂L/∂u_x`. `L` holds no `u̇`, so the Euler–Lagrange equation of `u_x` is `∂L/∂u_x = 0` for `x ∈ I`, and on solutions `h = Wt`.

   The curvature member has `F = 8K Σ_all N_x (Δχ)_x`, where `Δ` runs over the bonds with an interior end. Hence `∂F/∂u_x = 8K N_x (Δχ)_x`, and at the walls `N = 1`. The content does not depend on the walls' rates: the rest content lives in `I`, and the walker is confined to `I`. So `Wt = 8K Σ_W (Δχ)_x`. Because `Σ_all (Δχ)_x = 0` (each bond enters twice with opposite signs), also `Wt = −8K Σ_I (Δχ)_x`.

3. **CHECKED (E1).** On the `2³` box at a rational point with the walls at 1, exactly, check.py verifies:
   - `∂F/∂u_x = 8K N_x (Δχ)_x` at all 32 sites;
   - `∂F/∂χ_z = 8K[w_z (Δχ)_z + (ΔN)_z]`;
   - for a walker with Gaussian-rational amplitudes, `∂⟨H⟩/∂u_z = e_z = Re ψ_z†(H_eff ψ)_z = −∂⟨H⟩/∂λ_z` and `Σ e = ⟨H⟩`;
   - `Σ_all Δχ = 0`;
   - `Σ_W ∂(⟨H⟩ + F)/∂u = 8K ×` flux, for both contents;
   - the T1 identity for both contents, with `c_k = −6K`, `s = 3` and rational `λ̇`.

   The derivatives are symbolic (sympy), not hand-written.

4. **PROVED (T2).** Let `p_x = ∂L/∂λ̇_x`.
   - Because `K_λ` is homogeneous of degree two in `λ̇`, `Σ λ̇ p − L = 2K_λ − K_λ + 𝓔 = h`. The walker's `L_ψ` is linear in `ψ̇` and contributes nothing.
   - Then `dh/dt = Σ_I λ̇_x (ṗ_x − ∂L/∂λ_x) − Σ_I u̇_x ∂L/∂u_x − ∂L/∂t`, plus walker terms `ψ̇·(d/dt ∂L/∂ψ̇ − ∂L/∂ψ) + c.c.`. The walls do not move.
   - On solutions every bracket vanishes, leaving `dh/dt = −∂L/∂t = ∂𝓔/∂t` at fixed fields. `K_λ` carries no explicit label dependence.

5. **CHECKED (E2).** The off-shell identity of step 4 holds exactly on the `2³` box at `t = 1/3` and `t = 3/4`. The paths of `χ` and `φ = √w` are polynomial in the label, and a supplied `ρ(t)` gives `−∂L/∂t = Σ w ρ̇`.

6. **PROVED ((a), exact).** For `⟨H⟩ = Σ w ρ(t)`, `∂𝓔/∂t = Σ_x w_x ρ̇_x`, so by T1 and T2, `dWt/dt = Σ w ρ̇`. By block 54 the pull on a body of energy `m w` is `−m w ∇u = −m ∇w`. The supply that holds the body on its path therefore delivers power `m ∇w · ẋ`. On the lattice, carrying bare energy between sites delivers `Σ w ρ̇`.

7. **PROVED ((a1)).**
   - With `K_λ` present, the `u`-equation is `∂𝓔/∂u_x = −∂K_λ/∂u_x`, which is quadratic in `λ̇`.
   - The `λ`-equation is `∂𝓔/∂λ_x = ∂K_λ/∂λ_x − d/dt ∂K_λ/∂λ̇_x`. It is built from `λ̈` and from products of first derivatives.
   - Both right-hand sides are therefore `O(ρ̈, ρ̇²)`. Where the static Hessian of `𝓔` in the interior fields is invertible, the fields are the static ones plus `O(ρ̈, ρ̇²)`.
   - So `Σ w ρ̇ = Σ w_static ρ̇ + O(ρ̇ ρ̈, ρ̇³)`. By the envelope identity `d/dt 𝓔(ρ, fields*(ρ)) = Σ w_static ρ̇` (the fields are stationary in `I`), this equals `d/dt Wt_static` via T1(c).

8. **PROVED ((a2)).** Write `ρ = ερ̂`, `χ = 1 + εχ₁ + ε²χ₂` and `w = 1 + εw₁ + …`.
   - The `u`-equation `c_k ℓ^s λ̇²/w + wρ + 8K N Δχ = 0` at order `ε` gives `ρ̂ + 8K Δχ₁ = 0`, so `χ₁ = gρ̂/(8K)` and `λ₁ = 2χ₁`.
   - The `χ`-equation at order `ε` gives `8c_k χ̈₁ + 8K(Δw₁ + 2Δχ₁) = 0`, so `w₁ = −2χ₁ + (c_k/K) g χ̈₁`.
   - The `u`-equation at order `ε²` gives `8K Δχ₂ = −[4c_k χ̇₁² + w₁ρ̂ + 8K(w₁ + χ₁)Δχ₁] = −[4c_k χ̇₁² − χ₁ρ̂]`. Here `w₁` drops out.
   - By step 2, `Wt = −8K Σ_I Δχ`. So `Wt⁽¹⁾ = Σρ̂` and `Wt⁽²⁾ = c_k Σ λ̇₁² − ρ̂·gρ̂/(8K)`.
   - Independently, `Σ w₁ ρ̂̇ = −(1/4K) ρ̂̇·gρ̂ + (c_k/8K²) ρ̂̇·g²ρ̂̈`, which is `d/dt [−ρ̂·gρ̂/(8K) + (c_k/16K²) ρ̂̇·g²ρ̂̇]`. This equals `dWt⁽²⁾/dt`, as T2 requires. For `c_k = −6K`, `c_k/16K² = −3/(8K)`.

9. **CHECKED (E3, exact).** On the `3³` interior with `K = 1/2` and `c_k = −6K`, the equations are expanded as truncated series in `ε`, with coefficients that are polynomials in the label. The expansion uses its own series arithmetic applied to the exact expressions, not the hand-simplified ones.
   - Two supplied motions are used: a body carried centre → `(2,2,1)` by the smooth step `3t² − 2t³`, and a body carried towards a fixed one.
   - For both: the order-`ε` equation holds; the order-`ε` flux equals `Σρ̂` (lattice Gauss); `Wt⁽²⁾` equals the closed form; and `dWt⁽²⁾/dt = Σ w₁ ρ̂̇` as polynomials in `t`.
   - The values are `g_cc = 11/51` and `g_oo = 145/714`. The changes are `+3/952` and `−61/2856`.

10. **CHECKED (S1; high precision, 80 digits; error bounds printed).** This is the strong field under the static law, with T4's exact two-body solution: bare energy shared between the centre and a face-adjacent site at `s = 3/10`, `m/(8K) = 20`, `χ_centre ≈ 2.41`.
    - The residuals of both field equations are below 10⁻⁵⁰.
    - The flux of `χ`, `⟨H⟩ + F`, and `8K(Q₁ + Q₂)` agree to 10⁻⁵⁰.
    - `dWt/ds` agrees with `m(w_off − w_cen)` to 10⁻⁴⁹.

    This is (a1) and the exact rate of step 6 at strong field.

11. **PROVED ((b)).**
    - **(b1)** With `K_λ = 0`, `h = 𝓔` and T2 give `d𝓔/dt = 0`. Directly: `d𝓔/dt = Σ_I (∂𝓔/∂u_x u̇_x + ∂𝓔/∂λ_x λ̇_x) + i⟨ψ|[G, H_eff]|ψ⟩`. The first sum vanishes because the fields are stationary in `I` and held at `W`. The second vanishes for `G = H_eff`.
    - **(b2)** This is T2 with `K_λ ≠ 0`.
    - **(b3)** This is the same formula with `G ≠ H_eff`. Here T1(c) still gives `𝓔 = Wt`, because the fields stay stationary.

12. **CHECKED (B1, B2; floating point, evidence).** Block 54's walk on the `3³` interior with `K = 1/8`, starting from a superposition of the two highest energy levels. The fields are re-solved at every RK4 stage.
    - **B1:** the flux of `χ` equals `⟨H⟩ + F` to `9×10⁻¹⁵`, and is constant to `5×10⁻¹²` over `t ∈ [0, 3]`, while the density moves by 0.31 in l1.
    - **B2:** with `G = √w H √w`, the flux moves at the predicted `i⟨[G, H_eff]⟩` at `t = 0, 1, 2` (gap `10⁻¹¹`), drifting by `4×10⁻⁴`, which is `8×10⁷` times B1's drift.

13. **PROVED ((c)).**
    - Block 55 T2(a) holds `Σu` fixed, so its stationarity carries the multiplier `μ`. In the box the held walls fix the unit of rate, and stationarity in `u_x`, `x ∈ I`, carries none. Step 11 keeps the ledger, and step 1 gives `𝓔 = Σ_W ∂𝓔/∂u = Wt`. Block 55 T4(b)'s "the ledger per site" is replaced by the flux into the walls.
    - Block 55 T1 with lengths follows from step 3's derivatives.
    - The statement about the kinetic term is T2.

### ASSUMED

- **A1.** Solutions that are differentiable in the label exist. Block 60 T4 proves this for bodies at rest under the static law. For walker content, where `e_x` can be negative at some sites, and with `K_λ`, which makes a differential-algebraic system, it is assumed here. B1 exhibits one branch numerically. Step 7 also assumes the static Hessian is invertible.
- **A2.** The walker is confined to the interior; its amplitude is zero on the walls. This is part of the declared box.
- **A3.** Supplied content is at rest in block 60 T4's sense, `⟨H⟩ = Σ w ρ`, with no hop energy.

## (3) Route failures

No step fails.

Boundaries:
- The flux form of `Wt` belongs to the curvature member. For other weight-one ledgers, T1 and T2 hold with `Wt = Σ_W ∂𝓔/∂u`.
- The `O(ρ²)` coefficient of the speed term depends on the kinetic instance.
- Nothing here selects `K`, `c_k`, `s` or the member, and no physical identification is made.

## (4) What would finish it

- Existence and uniqueness of slaved branches for walker content and for `c_k < 0` (A1).
- Block 61's direction-dependent lengths, which carry travelling disturbances. T1 and T2 hold for any such Lagrangian with held walls. However, the tracking of step 7 would fail at the order where the supply excites disturbances: part of the supply's work would sit in the disturbances, which held walls reflect.
- Bound bodies with internal motion, where content with hop energy `τ` would add `−Σ τ λ̇` terms to the supply's work.
