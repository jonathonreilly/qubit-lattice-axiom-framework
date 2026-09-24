# deferred-20260924-transport, first pass a1: collisions restore the local law, not one coefficient in every direction

**Provenance and scope.**
- Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-macbookpro9927a-j6ef6`, task `J:derive:deferred-20260924-transport:a1`.
- This is the first bounded pass on batch 6. It is not an exhaustion of the bundle.
- `origin/main` is `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8` and is the science authority.
- The frozen head of PR8558 is `f23fd989d6ef2290319167208ab7098cd7975f62`. It was fetched, and its 15 source blobs were verified against the manifest SHA256 (RECOVERY_STATUS.json).
- **Related problems, inspected before calculating:**
  - `collisional-viscosity-and-eta`. It has no attempts and no active claim. **The computation of this pass is that problem's parts (a) and (b)**, and I disclose it here. Its part (c), the effect of exclusion at finite density, and its simulator check are left to it. This machine's claim loop will release that problem's units, so that its attempts stay independent.
  - `isotropic-streaming-clause`. a3 is this machine (#9127) and concerns alternative streaming rules; it explicitly left the collisional viscosity open.
  - `inertial-gas-viscosity-and-damping` a2 (this machine, `jd030`). It covers the six-axis one-point closure and damping rates.

  Neither of the last two is reused, and neither is the same question.
- **Plan, formed before calculating.** Linearize block 44's sphere-menu re-draw. Check whether its second-harmonic relaxation depends on the lattice. Carry it through the expansion about local equilibrium into block 51's viscous operator.

## 1. Landed baseline, and the deferred statement

**Landed on main:**
- **Block 44.**
  - The streaming is `max(0, s·e_k)/√3`, i.e. axis hops at rate `|s_k|/√3`, with exchange at occupied targets.
  - The scattering: each bond, at rate `γ`, re-draws the contents of its two records on their momentum class, as `P/2 ± r w`. Here `w` is uniform on the unit circle orthogonal to `P = s + s′`, and `r² = 1 − |P|²/4`.
- **Block 51** (conditional). The streaming gives `ν_lat(∇²g_i + ∂_i²g_i)` with `ν_lat = √3/16`. The supplied creeping model has `0 ≤ η ≤ 1`. Its T3: for `η > 0` the harmonic inverse-distance potential fails its curl compatibility condition. And "the collision viscosity … not derived".
- **Block 48, narrowed.** Its N1 route 2 now reads: "Collisions — may motivate a local closure but do not establish isotropic inflow; the companion cubic-viscosity note explicitly shows why this inference fails." This landed correction is preserved.

**Deferred.** Block 48 as submitted (frozen note, SHA256 `1dd75e82…`) says: "the collisional coefficient of block 47 at small density is `(3/2)² = 9/4` in every direction". Its route 2 says: "Collisions — restore a first-harmonic wind and with it one coefficient in every direction". Review U6-R5 demoted this ("Collisions said to restore isotropy").

**The question.** Does a collision calculation under the stated streaming law supply an actual isotropization mechanism, or is there an exact counterexample?

## 2. The residual and what is claimed

**Domain.**
- Block 44's sphere-menu clause.
- Small density: `ρ → 0` at fixed `γρ`. This is the product closure, in which each of a record's six bonds hosts a collision at rate `γ` with probability `ρ`.
- First order about local equilibrium (Chapman–Enskog), inside block 51's conditional first-harmonic closure.

**Claims.**
- **(i) The first half holds.** Per collision, the linearized re-draw multiplies a degree-`l` harmonic by
  ```
  a_l = 4 ∫₀¹ u P_l(u)² du = 2, 1, 1/2, 3/8, 9/32, 15/64, …
  ```
  - `a₀ = 2` and `a₁ = 1` are the number and momentum invariants.
  - For `l ≥ 2`, `a_l < 4/(2l+1) ≤ 4/5`, so every `l ≥ 2` relaxes at `6γρ(1 − a_l) > (6/5)γρ`.
  - So collisions do restore a first-harmonic local law.
- **(ii) The second harmonics relax at one rate.** `a₂ = 1/2` on all five second harmonics, including both cubic irreps (`x²−y²` and `xy` types). The stress relaxes at `3γρ` in every direction.
- **(iii) The collisional viscosity is isotropic.** It is `ν_coll = 1/(45γρ)`, with force `(1/(45γρ))(∇²g_i + (1/3)∂_i∇·g)`. There is no `∂_i²g_i` term.
- **(iv) The total operator.**
  ```
  ν(∇²g_i + η∂_i²g_i) + (1/(135γρ))∂_i∇·g,
  ν = √3/16 + 1/(45γρ),     η = 45√3γρ/(45√3γρ + 16) ∈ (0, 1),
  ```
  - `η` increases strictly with `γρ` and tends to 1 as `γρ → ∞`.
  - As `γρ → 0`, `η ≈ (45√3/16)γρ`.
- **(v) The second half fails at every collision rate.** This holds within the landed conditional model. Since `η > 0`, block 51 T3 says the inverse-distance potential inflow is not a solution, and T4 gives direction dependence at every distance.
  - No collision rate gives one coefficient in every direction.
  - Stronger collisions make it worse (`η → 1`).
  - Weak collisions dilute the cubic term only beyond the mean free path `1/(3√3γρ)`. Inside that, block 48 T3's anisotropic collisionless shadow holds.
- **(vi) A measurable signature.** Take transverse waves with in-plane polarization. Along a face diagonal they decay faster than along an axis by `ν_lat k²/2`, at every `γ`.

## 3. Steps

1. **ASSUMED.**
   - Block 44's clause as landed, the small-density product closure, the first-order expansion about local equilibrium, and block 51's conditional first-harmonic closure and supplied creeping model. These are supplied hypotheses, and none is adopted.
   - **Neglected at leading order** is the collisional-transfer stress: the momentum a collision moves between the two sites of an axis bond. It is `O(γρ²)`, against `O(1/(γρ))` for the kinetic part. Its symmetry is not computed; it could carry a cubic part at finite density.

2. **PROVED / CHECKED (E1) — the re-draw geometry.**
   - With `D = s₁ − s₂`, the re-drawn content is `s = P/2 + cos θ D/2 − sin θ (s₁×s₂)/|P|`, with `θ` uniform. This is a unit vector on the momentum class (`s·P = |P|²/2`), checked symbolically.
   - Its circle average is `E[ssᵀ] = PPᵀ/4 + DDᵀ/8 + (s₁×s₂)(s₁×s₂)ᵀ/(2|P|²) = ((1−c)/4)I + ((1+3c)/(8(1+c)))PPᵀ`, with `c = s₁·s₂`. Checked exactly at 196 rational pairs.
   - It depends only on `P` and `c`. No lattice axis enters the kernel.

3. **PROVED / CHECKED (E2) — linearization and multipliers.**
   - **The rates.** At leading order, a record at `x` is re-drawn at rate `6γρ`. The gain at content `s` is `6γ∫∫f(s₁)f(s₂)T(s|s₁,s₂)`, where `T` is uniform on the circle.
   - **Linearizing.** Put `f = (ρ/4π)(1+φ)`. The collision term is `6γρ(A − I)φ` on `l ≥ 1`, with `Aφ(s) = (1/4π)∫∫T(s|s₁,s₂)[φ(s₁) + φ(s₂)]`.
   - **The kernel is covariant.** `T` is built from `P` and the circle orthogonal to it, so it is rotation-covariant. By Funk–Hecke, `A` multiplies `Y_l` by `a_l = 2E[P_l(s·s₁)]`.
   - **The circle average.** `s` and `s₁` lie on the circle of angular radius `ρ_c` about `P̂`, with `cos ρ_c = |P|/2 = √((1+c)/2)`. The Legendre addition theorem gives `E_θ[P_l(s·s₁)] = P_l(cos ρ_c)²`.
   - **The average over pairs.** `c` is uniform on `[−1,1]`, so `u = cos ρ_c` has density `2u` on `[0,1]`. Hence `a_l = 4∫₀¹uP_l(u)²du`.
   - **Checked.** The direct double integral and this formula agree exactly for `l ≤ 8`.
   - **The bound.** `u < 1` a.e. gives `a_l < 4∫₀¹P_l² = 4/(2l+1)`, checked exactly to `l = 20`.

4. **PROVED / CHECKED (E3) — no cubic part in the stress relaxation.** This is a direct proof, not relying on covariance. Take a traceless symmetric `B` and `φ_B = sᵀBs`.
   - By E1, `E_θ[φ_B(s)] = ((1+3c)/(8(1+c)))PᵀBP`.
   - Averaged over `s₂` on the circle at cosine `c` from `s₁`, `PᵀBP` becomes `s₁ᵀBs₁(1+c)(1+3c)/2`. This is symbolic in general `B` and general `s₁`.
   - So `E[φ_B(s)φ_B(s₁)] = E_c[(1+3c)²/16]·E[φ_B(s₁)²] = (1/4)E[φ_B²]`.
   - By polarization and self-adjointness, the compression of `A` to the second harmonics is `(1/2)I`, for every `B`.

5. **PROVED / CHECKED (E4) — the collisional stress.**
   - The `l = 2` part of `(1/√3)s·∇f_le`, with `f_le = (n/4π)(1 + 3u·s)` and `g = nu`, is `(√3/4π)(s_is_j − δ_ij/3)S_ij[g]`.
   - The first correction is `f₁ = −(source)/(3γρ)`.
   - Then `Π_ij = (1/√3)∫s_is_jf₁ = −(2/(45γρ))S_ij[g]`, by symbolic sphere integrals.
   - On a plane wave, `−∂_jΠ_ij = (1/(45γρ))(∇²g_i + (1/3)∂_i∇·g)`. Checked exactly.

6. **PROVED / CHECKED (E5) — the lattice term, recomputed in the same equation.**
   - `⟨|s_z|³⟩ = 1/4` and `⟨s_x²|s_z|⟩ = 1/8`.
   - So the second-order axis streaming gives `(√3/16)(∇²g_i + ∂_i²g_i)`. This is block 51's value.

7. **PROVED / CHECKED (E6) — `η`.**
   - `η = 45√3γρ/(45√3γρ+16)`, with derivative `720√3/(45√3γρ+16)² > 0`, and the limits stated in §2.
   - The values are `0.4935` at `(ρ, γ) = (0.1, 2)` and `0.5937` at `(0.3, 1)`.
   - The transverse-wave difference `ν_lat k²/2` is checked exactly.

8. **CHECKED (float, N1) — an independent code path.**
   - 200 000 re-draws of the rule as written (`w` projected onto the plane orthogonal to `P`).
   - Every sampled content lies on its momentum class.
   - `⟨P₂(s·s₁)⟩ = 0.2506`. The two cubic-irrep quotients are `0.2475` and `0.2510`, against the exact `1/4`.

9. **The deferred sentence, resolved within the landed model.**
   - Collisions restore the local first-harmonic law (i).
   - They add only an isotropic viscosity (ii–iii), so `η > 0` at every finite `γρ` (iv).
   - Block 51's landed T3 then excludes the isotropic potential inflow. The "one coefficient in every direction" half fails, which confirms and sharpens the landed N1 correction.

**Historical comparison, not evidence.**
- Block 51's executed runs, as author reports, gave an axes-to-body-diagonal ratio of `1.35 ± 0.03` at `(0.1, 2)` and `1.30 ± 0.02` at `(0.3, 1)`. Its grid solution of the supplied creeping model, also an author report, gives `1.37` at `η = 1/2`.
- At `(0.1, 2)`, `η = 0.49` fits that pattern.
- At `(0.3, 1)` the small-density `η = 0.59` lies above the pattern. This is consistent with the `O(ρ)` corrections not computed here.

## 4. Where the route stops, and the next obligation

- **The first step not taken is finite density.**
  - Exclusion and the exchange rule correct `ν_lat` and `ν_coll`.
  - The collisional-transfer stress across axis bonds is `O(γρ²)`. It involves the bond direction, so it is the first place where collisions could feed the cubic term. Its sign and size are the next exact obligation. This is also collisional-viscosity-and-eta's part (c).
- **Also open:**
  - Burnett order.
  - Matching the collisionless near field to the viscous far field.
  - A simulator check of the transverse-wave prediction `ν_lat k²/2`.
- **Not claimed:** a physical wind, a force law or a gravitational reading; any edit of a landed note.
- The next ranked source groups are in RECOVERY_STATUS.json.

## 5. Running it

```
python3 probes/work/derive/deferred-20260924-transport/w-macbookpro9927a-j6ef6/check.py
```

- **Dependencies:** sympy and numpy (single-threaded).
- **Checks.** Six exact families (E1–E6) and one labelled float family (N1).
- **Runtime:** about 6 s.
- **Mutation census: 7 of 7 caught.**
  - a wrong circle radius;
  - the addition-theorem weight;
  - the circle average;
  - the rate without `λ₂`;
  - the lattice term from the diagonal moment;
  - the `η` constant;
  - an unprojected circle vector.
