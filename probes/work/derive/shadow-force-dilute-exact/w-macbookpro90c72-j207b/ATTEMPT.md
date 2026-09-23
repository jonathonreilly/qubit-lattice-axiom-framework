# J:derive:shadow-force-dilute-exact:a3

Worker `w-macbookpro90c72-j207b` (claude-opus-5-5). This is attempt 3 of 4. No earlier attempt's files or claims exist on `ai/probes`, so the plan is my own.

**Overlap disclosed.** The same session just finished `inertial-gas-viscosity-and-damping:a2`, a different task in block 44's clause. Nothing from it is used here.

All definitions come from block 44 (open PR #8550) and `probes/lib/inertial_bodies.py`:
- A capturing body removes a record at its first attempt to enter a body site and takes up its content.
- An emitter releases records at its surface.

## (1) Exact statement

### The dilute limit

Records are independent and keep their contents.
- **Six-axis menu:** a record steps along its axis at rate 1.
- **Sphere menu:** a record with content `s` steps along `sgn(s_k)e_k` at rate `|s_k|/√3`. This is a directed random walk with step choice `q = |s|/‖s‖₁`.

The steady state is fed by a distant uniform reservoir of density `ρ`. Two flux constants appear:
- `j₆ = ρ/6`: records per axis line, per tick, per direction;
- `j = ρ/(4√3)`: the one-sided flux through a lattice face (sphere menu).

### Claims

**(a) Six axes.**
- The force of a capturing body `B` on a capturing body `A` is exactly `F_A = j₆ Σ_axes Σ_lines [1(A meets the + stream first) − 1(A meets the − stream first)] e_axis`.
- This is `j₆ ×` (the number of axis lines through both bodies), directed towards `B`, whenever `B` lies on one side of `A` on those lines.
- It is the same at every separation: the streams are beams, and there is no inverse-square law.
- A body alone feels 0, and there is no force without an overlap.

**(b) Sphere menu.**
1. A record with content `s` visits the site `m` (oriented, `N = ‖m‖₁`) with probability `Mult(m; q) = N!/(m_x! m_y! m_z!) Π q_k^{m_k}`.
2. A site is entered at rate `ρ‖s‖₁/√3` per `dΩ/4π`. So the arrivals at a site are **not isotropic**: the weight is `‖s‖₁`, the projected area of a unit cube. Per unit projected area they are isotropic.
3. For two single sites at `r = m r̂`, with `m → ∞`,

   `r² F → (j/π) 2^z ‖r̂‖₁² r̂`, directed towards `B`,

   where `z` is the number of zero components of `r̂`. Thus `F = C j A_A A_B/r²` with `A = ‖r̂‖₁` (the unit-cube projection) and `C = 2^z/π`: `1/π` in generic directions, `2/π` on lattice coordinate planes, `4/π` on axes.
4. The enhancement is channelling. Contents within about `1/r` of a lattice plane or axis take no steps across it, and the peak of the visit probability is shared by `2^z` octants.
5. For two `2×2×2` cubes on an axis, `r²F/(j/π)` tends to 35.97, extrapolated from `r = 96, 192`. This matches the sum over pairs of facing columns of `2^{#equal transverse coordinates}`, which is 36, not the smooth `A_A A_B = 16`.

**(c) Porous bodies.**
- **Six axes.** For bodies of `N` random capturing sites in a cross-section of `a` lines and length `T`, placed apart along the axis:
  - `E[F]/j₆ = a p_A p_B`, with `p(N) = 1 − C(aT−T, N)/C(aT, N)`.
  - For `N ≪ a` this is `≈ N_A N_B/a` (additive).
  - It saturates to `a`, with `p → 1 − e^{−τ}` and opacity `τ = N/a`. Half-saturation is at `τ = ln 2` (`N = 11` for `a = 16`, `T = 8`).
- **Sphere.** The capture cross-section of random clusters in a `6³` block (generic content) is 1.98, 7.22, 19.81, 32.38 and 36 for `N` = 2, 8, 32, 108, 216. It is additive at low opacity and saturates to the block's projection, close to `A_env(1 − e^{−N/A_env})`.

**(d) Emitters.**
- An isotropic emitter of `Q` records per tick pushes a capturing site at `r` with `(Q/4π) 2^z ‖r̂‖₁ r̂/r²`: repulsion, with the same distance law and the same channelling.
- A reflecting receiver on an axis takes `2s_x` per arrival, twice the capture. The last step into it is along `x` with probability `m_x/N = 1`.

## (2) Steps

1. **PROVED (a).** In the dilute limit a six-axis record moves along its line at rate 1, and there are no sources. In steady state, each stream on each line has density `ρ/6` upstream of the first body site it meets and zero downstream of it.
   - The flux `j₆` is therefore absorbed at that first site, which takes up momentum `j₆ e` per tick.
   - Summing over lines gives the formula.
   - A body alone takes both streams of each of its lines, which cancel.
   - With `B` on the line, the stream from `B`'s side is absorbed by `B`, leaving `j₆` towards `B`.
   - Separation does not enter.

2. **CHECKED (A1, exact integer counting).** 400 placements: four shapes (site, `2×2×2` cube, `1×3×2` slab, L-shape), five transverse offsets and separations 3 to 21. Two diagonal placements (overlap along `x` only, or along `y` only) are also checked.

3. **PROVED (b.1).** A sphere-menu record steps only along `sgn(s_k)e_k`, and each step raises the oriented level `‖·‖₁` by one. So it visits `m` exactly when its first `N` steps land on `m`, which has multinomial probability. **CHECKED (B1):** an exact DP over levels with rational `q` agrees with the formula.

4. **PROVED (b.2).** In the uniform state every site holds a record with content in `dΩ` with probability `ρ dΩ/4π`. The entry rate into a site is therefore `Σ_k (ρ dΩ/4π) p_k(s) = ρ‖s‖₁ dΩ/(4π√3)`. `‖s‖₁ = Σ|s_k|` is the projected area of a unit cube along `s`. The total is `√3ρ/2 = 6j`.

5. **PROVED (b.3), the constant, by Dirichlet concentration.**
   - For single sites, the momentum missing at `A` is exactly `∫ (ρ/4π)(‖s‖₁/√3) Mult(m; q(s)) s dΩ`, with `m` the step from `B` to `A`. These are the records entering `B` whose continuation visits `A`.
   - On each octant `σ`, put `s = σ⊙q/‖q‖₂`. Then `dΩ = d²q/‖q‖₂³` and `‖s‖₁ = 1/‖q‖₂`, so the integrand is `(ρ/(4π√3)) σ⊙q ‖q‖₂^{−5} Mult d²q`.
   - `(N+1)(N+2) Mult(m; q)` is the Dirichlet(`m + 1`) density; its integral is checked exactly in B1. It concentrates at `q* = |m|/N` with variance `O(1/N)`.
   - The function `σ⊙q‖q‖₂^{−5}` is continuous on the simplex (`‖q‖₂ ≥ 1/√3`), so the octant integral is `(1/N²)·m̂‖m̂‖₁⁴·(1 + o(1))`.
   - The octants that contribute have `σ_k = sgn(m_k)`, with both signs when `m_k = 0`: `2^z` of them.
   - With `N = r‖m̂‖₁`: `r²F → (ρ/(4π√3)) 2^z ‖r̂‖₁² r̂ = (j/π) 2^z ‖r̂‖₁² r̂`, pointing towards `B`.

6. **CHECKED (B2, floating point).** Gauss quadrature over contents of the exact multinomial (Duffy map per octant; node doubling agrees to `10⁻⁶`), with Richardson extrapolation in `1/r`. The limits `2^z‖r̂‖₁²`:

   | direction | limit |
   |---|---|
   | (1,0,0) | 3.997 → 4 |
   | (1,1,0) | 3.999 → 4 |
   | (1,1,1) | 2.997 → 3 |
   | (3,2,1) | 2.571 → 2.571 |

   An independent spherical-coordinate quadrature matched the axis values to every printed digit.

7. **CHECKED (B3, floating point on exact per-content densities).** The DP computes the steady-state density `n(x) = Σ_k q_k n(x − e_k)`, oriented, for `B` absorbing and for `B` transparent, then integrates over contents.
   - For `2×2×2` cubes, `r²F/(j/π)` is 41.51, 38.70 and 37.33 at `r` = 48, 96, 192. The differences halve, and the extrapolation gives 35.97.
   - The column-pair law — at fixed transverse offset `δ`, `∫dΩ P(offset δ) → 2^{z(δ)}/N²` — is derived here by a Poisson-regime argument and **CHECKED**, not proved.

8. **PROVED (c), six axes.** The two bodies' line sets are independent, and a line is blocked by `N` random sites with the hypergeometric probability `p(N)`, so `E[F] = j₆ a p_A p_B`. As `T → ∞` at fixed `τ = N/a`, `p → 1 − e^{−τ}`. **CHECKED (C1):** exhaustive enumeration on a 2-line body; exact values; half-saturation at `N = 11` (`τ = 0.688`, and `ln 2 = 0.693`).

   **CHECKED (C2), sphere:** cluster cross-sections by the same DP.

9. **PROVED (d).** An isotropic emitter has density `Q/4π` per `dΩ`, and a capturing receiver takes up `∫ (Q/4π) Mult(m; q) s dΩ`. The same Dirichlet argument, with `σ⊙q ‖q‖₂^{−4}`, gives `(Q/4π) 2^z ‖r̂‖₁ r̂/r²` directed away from the emitter.
   - For a reflecting receiver, the multinomial path ends with a step along `k` with probability `m_k/N`. On the axis this probability is 1, so each arrival transfers `2s_x e_x → 2e_x`.
   - **CHECKED (D1)** for the capturing receiver: 4.001, 2.828, 1.731 against `2^z‖r̂‖₁` = 4, 2.828, 1.732.

### ASSUMED

- The dilute limit itself: no collisions and no exchanges, so records are independent.
- A distant uniform reservoir.
- The emitter in (d) is taken as isotropic. For `inertial_bodies.py`'s ball, hemispherical emission from the six face types sums to isotropic. Near-field reflections off the emitting body are not analysed.

## (3) Where the route fails

No step fails. The conjectured form "`F = C j A_A A_B/r²` with one constant `C`" does not hold for this lattice rule:
- `C` depends on the direction (channelling: `2^z/π`);
- for extended bodies on a lattice axis, `A_A A_B` is replaced by the facing-column sum (36 against 16 for `2×2×2` cubes).

Only in generic directions (no zero component of `r̂`) does the rule behave like isotropic straight rays with unit-cube cross-sections, with `C = 1/π`.

Block 44's executed forces (`ρ = 0.3`, `γ = 1`) are in the collisional regime and are not predicted here.

## (4) What would finish it

- A proof of the facing-column law for extended bodies. This needs the Poisson-regime density `2^{z(δ)}/N²` at fixed offset `δ`, with side entries bounded.
- The `O(1/r)` corrections: `4(1 + c/N)` on the axis, where the numerics suggest `c ≈ 5`.
- The crossover from this dilute law to block 44's collisional wind as `γρ` grows.
