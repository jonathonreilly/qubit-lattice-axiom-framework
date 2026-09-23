# J:derive:inertial-gas-viscosity-and-damping:a2

Worker `w-macbookpro90c72-jd030` (claude-opus-5-5). This is attempt 2 of 4. No earlier attempt's files or claim exist on `ai/probes`, so the plan is my own. All definitions come from block 44 (open PR #8550: its note, its control output `specs/supervisor_control_block44_inertial.out.txt`, and `probes/lib/inertial.py`).

## (1) Exact statement

### The clause

Six-axis menu (block 44 (S), (C)):

- **(S)** Each record, at rate 1, swaps the states of its site `x` and of `x + e_d`, where `d` is its content. The swap enters the target if it is empty and exchanges contents if it is occupied.
- **(C)** Each bond, at rate `γ`, re-draws two records uniformly on their momentum class.

The sphere menu is the same, with stepping rates `p_k(s) = max(0, s·e_k)/√3` and the re-draw `P/2 ± r w`.

### Claims

**(a) The Boltzmann-type closure.** Replace every two-site expectation in the exact one-point equations by a product. Linearise at the uniform product state, which block 44 T2 proves stationary.

- **Six axes, `k` along an axis.**
  - The sound roots are `±i√((1−ρ)/3) k − (Γ/2)k² + O(k³)`, with

    `Γ = D + ν_L`, `D = (1−ρ)/6 + ρ/6 = 1/6`, `ν_L = 1/2 + ρ/6 + γρ/2 + 1/(3γρ)`.

  - The shear eigenvalue is exactly `−(1 − cos k) ρ (1/3 + γ)` in the closure, so `ν_T = ρ/6 + γρ/2`.
  - The momentum flux has two parts:
    - its diagonal part (the axis quadrupole, two modes) relaxes by (C) alone at rate `2γρ`;
    - streaming with exchange does not relax it; instead it spreads contents at rate `ρ/6` per bond.
  - The collision-limited viscosity `1/(3γρ)` is purely longitudinal and traceless: no bulk part, and none for transverse waves along an axis.
  - `D` is the non-Galilean correction: the mass current is `(1−ρ)` times the content flux, so the hop noise carries `(1−ρ)/6`. The exchange diffusion `ρ/6` makes the total independent of `ρ`.
- **Sphere.**
  - The quadrupole relaxes at `3γρ`; the re-draw retains `a_l = 1, 1/2, 1/4, 3/16, 9/64` for `l = 0..4`.
  - `Γ_s = (5/8 + ρ/4)/√3 + γρ/2 + 4/(135γρ)`.
  - `ν_T = √3/16 + ρ/(4√3) + γρ/2 + 1/(45γρ)`.
  - The kinetic parts are a pure shear, `1/(45γρ)`, with no bulk part.
- **Rate dependence.** Both menus have a collision-limited term `∝ 1/(γρ)` and a collision momentum-diffusion term `γρ/2`. `Γ` is therefore not monotone in `γ`: in the continuous clause the six-axis minimum is at `γρ = √(2/3)`.

**(b) Predictions** at `ρ = 0.3`, `γ = 1`, wavelengths 64 and 32 (damping = −Re of the sound root):

| | closure | block 44 measured |
|---|---|---|
| sphere | 0.0031, 0.0125 | 0.0030, 0.0130 |
| six axes | 0.0096, 0.0396 | 0.0130–0.0140, 0.0480–0.0500 |

- **Block 44's simulator** runs all streaming attempts and then a collision phase on a frozen configuration. For an isolated pair that phase is exactly `I + (1 − e^{−γ})(T − I)`. Within the closure, its `Γ` replaces `γ` by `γ' = 1 − e^{−γ}` and `1/λ` by `1/λ_tick − 1/2`: six axes `Γ = 2/3 + ρ/6 + γ'ρ/2 + 1/(3γ'ρ) − 1/3`. This gives 0.0109 and 0.0462 for the six axes, and 0.0029 and 0.0117 for the sphere.
- **The clause in continuous time,** simulated, damps the six-axis wave at 0.0120 (`ρ = 0.3`), 0.0090 (`ρ = 0.5`) and 0.0220 (`ρ = 0.15`). The closure gives 0.0095, 0.0080 and 0.0144.
- **Where the six-axis gap sits.** The measured quadrupole relaxation is 0.447, 0.776 and 0.224 against the closure's `2γρ` = 0.6, 1.0 and 0.3. An opposite pair that has been re-drawn stays on its bond and is re-drawn again without further relaxation until streaming separates it. Using the measured rate in the closure's `Γ` gives 0.0114, 0.0090 and 0.0181.

**(c) What is exact and what is a closure.** Listed in §(2) by tag.

## (2) Steps

1. **PROVED.** The exact one-point equation of (S) is

   `d⟨n_y(c)⟩/dt = ⟨n_{y−c}(c)⟩ − ⟨n_y(c)⟩ + Σ_e [⟨n_y(e) n_{y+e}(c)⟩ − ⟨n_{y−e}(e) n_y(c)⟩]`.

   Swaps triggered at `y` replace `y`'s state by that of `y + e`. Swaps triggered at `y − e` put `e` on `y`. `Σ_e n_y(e) n_y(c) = n_y(c)`. The mass current across a bond is `f_y(e)(1 − ρ_{y+e}) − f_{y+e}(−e)(1 − ρ_y)`, which reduces to block 44's `(1−ρ)g` in product states.

2. **CHECKED (A1, exact).** The 36 × 36 re-draw matrix `T` is symmetric and stochastic, with `T² = T` and rank 19, equal to the number of momentum classes (6 singletons, 12 pairs, one class of 6).
   - The generator `γ(T − I)` has eigenvalues 0 (19 times) and `−γ` (17 times).
   - The conserved modes are the class indicators; number and pair momentum are among them.
   - An isolated pair evolved for time `t` is `I + (1 − e^{−γt})(T − I)`.

3. **CHECKED (A2, exact).** The one-site 6 × 6 operator at `k = 0` (partner deviation equal) is `γρ(U + V − 6I − J)`.
   - Its eigenvalues are 0 (4 times: density and the three momenta) and `−2γρ` (twice: the axis quadrupole).
   - `U = V`. One collision with a uniform partner retains 1/2 of the momentum and 1/3 of the quadrupole.
   - For `k ≠ 0` the closure's collision term is `γρ[a_l(6 + 2Σ_j cos k_j) − 6]` on each sector with `l ≥ 1`, and 0 on density.

4. **CLOSURE, algebra exact (B1).** The linearised operator is `M(k) = S(k) + C(k)`, where
   - `S(k)_{cc'} = δ_{cc'}(e^{−ik·c} − 1) + (ρ/6)[(1 − e^{−ik·c'}) + δ_{cc'}(2Σ_j cos k_j − 6)]`;
   - `C(k) = γ(ρ/6)[6U + (2Σ_j cos k_j)V − 36I − (2Σ_j cos k_j)J]`.

   Along an axis, the longitudinal invariant block is 3 × 3. Its characteristic polynomial, expanded exactly (sympy), gives the sound root with the stated `Γ`, and the transverse eigenvector gives the exact shear eigenvalue.

   The mechanism, from perturbation theory on the conserved subspace:
   - `S₁` couples momentum to the quadrupole `d_x² − 1/3` with weight 1, and the quadrupole back to momentum with weight `2/3`. The quadrupole relaxes at `2γρ`, which gives `ν_kin = (2/3)/(2γρ)`.
   - The `k²` terms give 1/2 (Poisson hop noise), `ρ/6` (exchange diffusion) and `γρ/2` (collisions move contents across bonds).

5. **EXACT (C1)** sphere moments and retentions, and **CLOSURE** sphere `Γ_s`, `ν_T`. Here `S₁ = −(s_x/√3)` plus a rank-one exchange term, so the smooth velocity is `s/√3`.
   - The chain from momentum through `l = 2` gives `(1/√3)·(4/(15√3))/(3γρ) = 4/(135γρ)`.
   - The `k²` terms give `⟨|s_x|³⟩·3/(2√3) = 3/(8√3)`, `ρp̄ = ρ/(4√3)` with `p̄ = 1/(4√3)`, and `γρ a_1 = γρ/2`.
   - Density: `D = ⟨|s_x|⟩/(2√3) = 1/(4√3)`, which is `(1−ρ)/(4√3)` from hop noise plus `ρ/(4√3)` from exchange.
   - Shear: `⟨|s_x| s_y²⟩·3/(2√3) = √3/16`, plus the kinetic part. `s_y` goes to `−s_x s_y/√3` (pure `l = 2`), which relaxes at `3γρ`, and comes back as `−s_x² s_y/(3·3γρ)`. Projecting with `⟨s_x² s_y²⟩/⟨s_y²⟩ = 1/5` gives `1/(45γρ)`.

6. **CHECKED (C2, floating point).** A Galerkin version of the sphere closure (harmonics `l ≤ 10`, octant Gauss rule) at `ρ = 0.3`, `γ = 1`, `k = 0.01` gives `Γ` 0.65290 against 0.65291, speed 0.27888 against `√(1−ρ)/3`, and shear 0.37562 against 0.37563.

7. **CLOSURE, derivation PROVED (D1).** Write the tick map as `T_k = (I + K)·e^{S}`, with `K` the collision operator at `γ'`.
   - `log T_k` on the conserved subspace, to order `k²`, is `ikPS₁P + k²[PS₂P + PK₂P − PS₁Q(1/λ_t − 1/2)S₁P]`. The `−1/2` comes from `S²/2` in `e^{S}`, as in lattice-BGK viscosity.
   - The formula agrees with the tick map's eigenvalue at `k = 0.004`: six 2.2360 against 2.2359, sphere 0.6108 against 0.6108.
   - Only the isolated-pair phase map (step 2) is exact. Applying it bond by bond, linearly, is the closure.

8. **FLOAT (E1, F1, F2).**
   - E1: predictions, as in the table above.
   - F1: block 44's own simulator, re-run with its own fit (side 64, 4 runs, 300 ticks), gives six 0.0140 and 0.0490, sphere 0.0030 and 0.0130.
   - F2: the clause in continuous time (streaming attempts and bond draws interleaved at random), with its quadrupole relaxation rate at `k = 0`, as quoted in §(1)(b).

### ASSUMED

- That a damped cosine fit to 300 ticks measures the sound root. This is block 44's procedure; the fit's grid step is 0.001.
- That `L = 64` is large enough.

## (3) Where the route fails

**The first step that fails is the product closure of the collision term,** that is, the rate at which (C) relaxes the diagonal momentum flux. In the clause itself the quadrupole relaxes at 0.447, 0.776 and 0.224 (`ρ` = 0.3, 0.5, 0.15; `γ = 1`), not at `2γρ`. The cause is recollisions. After a re-draw, an opposite pair stays opposite on its bond; further re-draws do not relax it further until streaming separates the pair, while the closure counts each re-draw as fresh.

This matters for the six axes, where the collision-limited term dominates `Γ` (1.11 of 1.98 at `ρ = 0.3`, `γ = 1`). It matters little for the sphere, where the term is 0.099 of 0.653. That is why the closure meets the sphere's numbers and falls short on the six axes.

Using the measured rate in the closure's formula recovers the continuous-time damping at `ρ = 0.3` and `0.5` within 5%. At `ρ = 0.15` it is 18% low, so other correlations remain at low density.

The block's split tick adds a further 10–15% on top.

## (4) What would finish it

- A pair-level (ring) closure for the bond-pair function of opposite contents. It would include the separation of a pair by streaming and by third-party exchanges, and would give the quadrupole relaxation rate from the clause.
- The pair-correlation corrections to the streaming terms, which is where the `ρ = 0.15` residual sits.
- Longer runs and several side lengths, to put error bars on the measured dampings; the fit's grid step is 0.001.
