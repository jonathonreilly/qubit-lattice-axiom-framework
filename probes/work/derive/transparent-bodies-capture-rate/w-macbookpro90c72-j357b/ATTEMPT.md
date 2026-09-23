# J:derive:transparent-bodies-capture-rate:a1 — capture is kinetic, not diffusive: face counts predict solid balls, optical depth 2Rφ sets additivity

**Provenance.**
- Worker `w-macbookpro90c72-j357b`, model `claude-opus-5-5`, one session. The claim printed no prior attempts.
- Setting, per the task:
  - blocks 44 and 45 (the inertial clause, the wind law);
  - block 48 T1 (a site's capture rate, `(ρ/√3)⟨|s|₁⟩`) and T3 (independent records stream as directed walks).
- The executed numbers are the task's.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Task.**
- (a) Derive `Q(N, R)` for a porous ball in the diffusive picture: the crossover `N*` and the saturated value.
- (b) Predict the executed values:
  - porous balls, `R = 5`, `N = 51, 164, 515`: `Q = 9.4, 17.8, 21.8`;
  - solid balls, `R = 2..5`: `Q = 3.2, 7.8, 13.2, 21.8`;
  - both at `ρ = 0.29`, `γ = 1`.
- (c) Say when `F ∝ N₁N₂`.

**Result (PARTIAL).**

1. **The diffusive route fails at its first step.**
   - It supposes the gas near the body is depleted, so that the capture rate is set by transport: `Q = 4πD_eff Rρ`, which grows like `R`.
   - Block 45's executed wind shows the density stays **flat** around a capturing body: the momentum-carrying inflow replenishes it.
   - The executed solid balls grow like `R²` (`Q/R² = 0.80, 0.87, 0.83, 0.87`).
   - So the rate-limiting step is kinetic entry into the capturing sites, not transport. No tracer diffusion constant appears in `Q` in this regime.

2. **The kinetic rate (exact).**
   - An exposed face (a capturing site next to a site of isotropic gas at density `ρ`) takes up records at `ρ⟨max(0, s·n)⟩/√3 = ρ/(4√3)`.
   - A site has six faces, and `6·ρ/(4√3) = (ρ/√3)⟨|s|₁⟩ = q₁ = ρ√3/2` (block 48 T1).
   - So a body in a locally equilibrated gas captures `Q_loc = ρF/(4√3)`, where `F` is its number of exposed capturing faces.

3. **Solid balls (exact counts, parameter-free).**
   - The lattice balls of radius 2–5 have `33, 123, 257, 515` sites and `F = 78, 174, 294, 486` exposed faces.
   - So `Q_loc = 3.26, 7.28, 12.31, 20.34`, against the executed `3.2, 7.8, 13.2, 21.8`: within 7%. The small excess is plausibly the inflow wind, whose inward drift adds to the face flux.
   - **Saturated value.** `F → (3/2)·4πR²` (the mean `|n|₁` of a sphere's normals), so `Q_sat ≈ (√3π/2)ρR²`.

4. **Porous balls: the optical depth (exact in the chord model).**
   - A straight streaming path of length `ℓ` visits `|s|₁ℓ` sites, `3/2` per unit length on average. A ball's chords under a uniform isotropic flux have density `ℓ/(2R²)` on `[0, 2R]`, with mean `4R/3`.
   - A ball with fill `φ = N/V` therefore has optical depth `τ = 2Rφ`. The **crossover** is `N* = (2π/3)R²`: 52 at `R = 5`.
   - In the chord model `Q/(Nq₁) = 1 − (9/16)τ + O(τ²)`.

5. **Porous balls: brackets (executed transport, parameter-free).**
   - **Collisionless streaming** (independent records, exact transport recursion) and a **locally re-equilibrated gas** (`Q_loc` with the expected exposed faces) bracket the executed values:

     | `N` | collisionless | executed | locally re-equilibrated |
     |---|---|---|---|
     | 51 | 8.47 | 9.4 | 11.76 |
     | 164 | 13.48 | 17.8 | 30.18 |

   - A hybrid model gives `8.67` and `14.46`: re-equilibrated outside the ball (block 45's flat density), collisionless streaming inside.
   - The executed values lie 8% and 23% above the hybrid: collisions inside the body refill part of its shadow.

6. **(c) When the force is `∝ N₁N₂`.**
   - `F = KQ₁Q₂/r²` is `∝ N₁N₂` only while both bodies are optically thin, `N ≪ (2π/3)R²`, i.e. fill `φ ≪ 1/(2R)`.
   - Additivity within `ε` needs `N ≲ (16/9)ε·N*`: about `0.37R²` records at 10%.
   - At `N ≈ N*` the executed body is already screened by 27% (9.4 against 12.8).
   - **The cost.** Matter is additive only if it is empty at the scale of its own size: a body of radius `R` may hold fewer than about `2R²` capturing records, a vanishing fraction of its `(4π/3)R³` sites.

## 2. Steps

**S1 (PROVED; CHECKED E.single). Capture of one streaming record, exactly.**
- With independent records, a record of content `s` performs the directed walk with step frequencies `w = |s|/|s|₁` (block 48 T3).
- The probability that it steps onto a capturing site is given by the transport recursion `n(x) = Σ_k w_k n(x − e_k)·[x − e_k not capturing]`, `n(0) = 1`, with the capture probability `Σ_{x∈B} Σ_k w_k n(x − e_k)·[x − e_k ∉ B]`.
- CHECKED exactly (Fractions) against enumeration of every step sequence, for 3 small porous bodies and 3 rational step laws. For example, `7/9` for `B = {(1,0,0), (1,1,0), (2,1,1), (0,2,1)}` with `w = (1/2, 1/3, 1/6)`.
- This is the task's requested check.

**S2 (PROVED; CHECKED E.faces). The kinetic face rate and the solid balls.**
- Over the uniform sphere, `s_z` is uniform on `[−1, 1]`, so `⟨max(0, s_z)⟩ = 1/4` and `⟨|s|₁⟩ = 3/2`.
- A face between a capturing site and a gas site in the isotropic product state at density `ρ` receives the records of that site stepping across it, at rate `ρ⟨max(0, s·n)⟩/√3 = ρ/(4√3)`.
- Summing over the six faces gives block 48's `q₁`.
- The lattice-ball face counts are exact integers (CHECKED), giving `Q_loc(R)`.
- The comparison with the executed values is in §1 item 3.

**S3 (PROVED). The diffusive route's first step fails.**
- Its first step is the depletion picture: `ρ(r) → ρ` far away, `ρ(R) < ρ`, and a diffusive flux `4πD_eff Rρ`.
- The task's own executed data rule it out:
  - block 45's density is flat, to within its quoted tolerance, from `r = 7` to `32` around a capturing body;
  - the solid-ball rates grow like `R²`, not `R`.
- Any single `D_eff` fitting `R = 5` (`D_eff = Q/(4πRρ) ≈ 1.2`) predicts `Q(2) = 8.7`, against the executed 3.2.
- The inflow of a momentum-conserving gas is not tracer diffusion. The kinetic surface rate is what limits capture at these sizes.

**S4 (PROVED; CHECKED E.crossover, E.screening). The optical depth.**
- **Cauchy.** For a ball under a uniform isotropic (μ-random) flux, the chord length has density `ℓ/(2R²)` on `[0, 2R]` (CHECKED normalised), with mean `4R/3`, i.e. `4V/S`.
- **Sites per unit length.** Along a chord in direction `s` the lattice path visits `|s|₁` sites per unit length. By the ball's symmetry the chord directions are uniform overall, so the mean is `3/2`.
- **Depth.** A fill `φ` gives the mean number of capturing sites per chord `τ = 2Rφ`.
- **The absorbed fraction.** For independent sites with absorption `μ = (3/2)φ` per unit length:

  `P_abs = 1 − ∫ e^{−μℓ} ℓ/(2R²) dℓ = 1 − (1 − (1 + 2μR)e^{−2μR})/(2μ²R²)`.
- **Relative to the additive value** `(4/3)μR`: `Q/(Nq₁) = 1 − (9/16)τ + O(τ²)` (CHECKED).
- This is the continuum idealisation. The lattice paths are the directed walks of S1, which S5 computes exactly.

**S5 (executed; notes). The porous brackets.**
- The transport recursion of S1 is run over the sphere of contents: collapsed Gauss–Legendre quadrature on each octant's simplex, weight `dΩ|s|₁ = dw/|w|⁴`. It reproduces the single-site `q₁ = 0.2511`.
- **The three models.** Averaged over 6 random bodies (each `N` sites drawn from the 515 of the radius-5 ball):
  - collisionless everywhere;
  - collisionless inside the ball and re-equilibrated outside;
  - the locally re-equilibrated face count, from the exact expected number of adjacent capturing pairs, `1302·N(N−1)/(515·514)`.
- The numbers are in §1 item 5.

**ASSUMED.**
- The executed values and block 45's flat density, as the task reports them.
- Isotropy of the gas at the faces for `Q_loc`. The inflow wind is neglected; it is the likely source of the 7% excess.

## 3. The first failing step

**The diffusive route (task (a) as posed) fails at S3.**
- There is no depletion around a capturing body in this clause's executed regime, and `Q` grows like `R²`.
- So the capture rate is not `4πD_eff Rρ f(opacity)` with a transport-limited prefactor.
- It is `ρ/(4√3)` times an effective count of exposed capturing faces:
  - between the collisionless and the re-equilibrated counts for porous bodies;
  - equal to the exposed-face count for solid ones.

## 4. What would finish it

1. **The inflow correction.** With block 45's wind `u(R)` at the surface, the face flux becomes `ρ(1/4 + u_in/2)/√3`. Checking that this accounts for the 7% excess of the solid balls would close (b) for them.
2. **The collisional interior.** The executed porous values lie 8–23% above the hybrid model. A kinetic model with the clause's re-draw rate `γ` and exchanges inside the body (for example a BGK-type relaxation of contents at the executed rate) should close the bracket. Its one input is the tagged record's content-relaxation rate, which the clause fixes.
3. **Large bodies.** When `R` exceeds the scale at which the inflow can no longer keep the density flat (its viscous length), depletion and a diffusive or Stokes-type limit should appear. The crossover size is a question for block 45's hydrodynamics.

## 5. Running it

```
python3 probes/work/derive/transparent-bodies-capture-rate/w-macbookpro90c72-j357b/check.py
```

The run takes about 1 s. It makes four exact checks:
- enumeration against the recursion, in Fractions;
- the sphere moments and the lattice-ball counts;
- the chord density, the crossover and the screening expansion, in sympy.

The two `note` lines are the transport quadratures, in floating point.
