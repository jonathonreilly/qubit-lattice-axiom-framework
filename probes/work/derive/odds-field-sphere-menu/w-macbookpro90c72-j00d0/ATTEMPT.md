# J:derive:odds-field-sphere-menu:a1: the turn of the lean stays massless; at the neutral scale the ordered sea gives mass a first-order channel, with a tricritical point and a massless surface of its own

**Provenance.**
- Worker `w-macbookpro90c72-j00d0`, model `claude-opus-5-5`, one session. Unit a1 (attempt 1 of 4).
- **Plan, formed before reading the prior attempt:**
  - Funk–Hecke;
  - a spectral (Legendre) solution of the exact ordered equation;
  - the per-neighbour spectrum split by azimuthal number `m` about the lean (the turn by symmetry, the longitudinal mass);
  - `SO(2)` selection rules for what records feed in;
  - capacities from the lattice Green function.
- **The prior attempt a2** (worker `jff2b`) is on the branch. It is the same model family and has not been refereed.
  - It covers (a)–(d) along similar lines. Where the two overlap, they agree: its cubic coefficient equals B1's, and its lean and longitudinal-mass tables are reproduced in B2.
  - This attempt keeps its own route and does not rely on a2. It adds a2's first unfinished item (the seven-outcome reading at the neutral scale), plus:
    - a certified `β_c`;
    - a proof of the eigenvalue ordering;
    - the longitudinal mass law near the point;
    - capacities on the infinite lattice.
- **Related earlier units by the same model:** #8723 (odds map of the six-axis menu) and #8742 (a vector-coupled record in an ordered medium). Neither is a premise here.
- **Setting.** Blocks 41 and 42, read on the PR branch of #8548: T2's self-consistent odds, T5's seven-outcome reading, T6's boundary values. They are applied to the sphere menu with pair weight `e^{βs·s'}`.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Notation.** `dσ` is the uniform probability on the sphere, and `K₁f(s) = ∫e^{βs·b}f(b)dσ(b) / ∫e^{βs·b}dσ(b)`. The self-consistent odds are `π_x ∝ Π_{y∼x} K₁π_y`, and a record is a point mass. For the ordered sea, `t = s·n`.

**(a) The one-neighbour operator.**
- **The spectrum.**
  - `K₁` multiplies degree-`l` harmonics by `λ_l = i_l(β)/i₀(β)` (PROVED; CHECKED A1 to `10⁻⁴¹`).
  - `λ₁ = L(β) = coth β − 1/β` and `λ_{l+1} = λ_{l−1} − (2l+1)λ_l/β`.
  - Exact series: `λ₁ = β/3 − β³/45 + 2β⁵/945 − β⁷/4725 + …` and `λ₂ = β²/15 − 2β⁴/315 + β⁶/1575 − …`.
- **Ordering.** `1 > λ₁ > λ₂ > … > 0` for every `β > 0` (PROVED; CHECKED A2).
- **Linearization.** The linearized map is `K₁ − P₀` per neighbour, so a wave `k` in channel `l` has eigenvalue `λ_l(6 − E(k))` (PROVED).
- **The massless point.** `6L(β) = 1` at

  `β_c ∈ [0.50855806178558212313, 0.50855806178558212315]`

  (CHECKED A3 by interval arithmetic; unique because `L' = 1/β² − 1/sinh²β > 0`).
- **Below `β_c`.** `(−Δ + m²)v = source/L` with `m² = (1 − 6L)/L`, and the decay along an axis is `cosh κ = (1/L − 4)/2`. At `β = 0.3, 0.45, 0.5`: `1/m = 0.496, 1.15, 3.17` and `1/κ = 0.564, 1.18, 3.19`.

**(b) Beyond `β_c`: the ordered sea.**
- **The exact equation.** The uniform ordered field is `π = F(t)`, where `F = g⁶/⟨g⁶⟩` and `g = K₁F`. In Legendre coefficients, `g_l = λ_l f_l`.
- **Onset (exact; CHECKED B1).** With `F = 1 + aP₁ + ba²P₂ + …`:
  - `b = 10λ₁²/(1 − 6λ₂)`;
  - `a = 6λ₁a + c₃a³`, with `c₃ = 6λ₁³(38λ₂ − 3)/(1 − 6λ₂)`;
  - `c₃ < 0` at `β_c`, since `λ₂ = 0.0168 < 3/38` there. So the lean `M = a/3` is born continuously, with `M² → (6L − 1)(1 − 6λ₂)/(54λ₁³(3 − 38λ₂))`.
- **The transverse channel has no mass term at every `β > β_c`.** The turn of the lean is an eigenvector with eigenvalue exactly `1/6` per neighbour (PROVED by the rotation symmetry; CHECKED to `10⁻¹²`, eigenvector residual `< 10⁻¹¹`).
- **Every other sector is massive on the grid `β = 0.52, 0.6, 0.8, 1, 2, 4`** (CHECKED B2; not proved for every `β`):
  - the second `m = 1` eigenvalue;
  - `m = 0` (the longitudinal mass);
  - `m = 2` and `m = 3`.
- **Longitudinal masses** `m_L² = 0.263, 2.21, 7.02, 10.7, 19.1, 24.1` on that grid.
- **Near the point** `m_L² → 12(6L − 1)`, twice the screened side's `m² ≈ 6(1 − 6L)` at the same distance from `β_c` (PROVED at leading order; CHECKED B3).

**(c) What records and masses feed in.**
- **(i) A record of content `s₀`.** Its neighbours' factor is `e^{βs·s₀}` in place of `g(s)`. The `m = ±1` part of `log(e^{βs·s₀}/g)` is exactly `β s_⊥·s₀⊥`. A record aligned with the lean feeds nothing transverse at any order, because the whole problem then keeps the rotations about `n` (PROVED).
- **(ii) A mass without vacancies.** A record count, or a record whose content is averaged over those rotations or drawn from the sea, is invariant under them. So it feeds only `m = 0`, which is massive on the grid (PROVED by symmetry; the `m = 0` mass is CHECKED on the grid).
- **(iii) With "no record" as a seventh possibility (block 42 T5's reading), at the neutral scale `g = 1`.** Here `c₀ = β/sinh β`. New results:
  - **Reduction (PROVED).** The content map at density `ρ` is the map with every `λ_k` replaced by `ρλ_k`. The sea orders when `6ρλ₁ > 1`.
  - **The mass channel's own first-order strength in the ordered sea is `(1 − ρ)(1 − ⟨b⁵⟩/⟨b⁶⟩) > 0`** (PROVED; CHECKED C3). In the isotropic sea it is zero (T5). So in the ordered sea a record raises its neighbours' odds of holding a record, even at the neutral scale.
  - **Mixing.** The mass mixes with the longitudinal lean and never with the turn, which stays exactly `1/6` (PROVED; CHECKED C3).
  - **Tricritical point (PROVED as the Landau expansion; CHECKED C2).** At fixed fugacity the cubic coefficient is `c₃(ρλ) + 30λ₁³ρ³(1 − ρ)`. On the ordering line `6ρλ₁ = 1` it vanishes iff

    `12λ₁² + 8λ₁λ₂ − 5λ₁ + 5λ₂ = 0`,

    that is at `β_t = 0.957910880617496`, `ρ_t = 0.553095169776`. For `β < β_t` the ordering at fixed fugacity is continuous; for `β > β_t` it is discontinuous.
  - **A massless surface for mass (CHECKED C4, numerical).** For `β > β_t` the uniform ordered sea at fixed density has a lower stability edge `6μ₀(β, ρ*) = 1` for the density-lean block: `ρ* = 0.57228, 0.74417, 0.79781` at `β = 1, 2, 4`. On it that block has no mass term, and the mass source lies mostly on the massless mode (coefficient `0.96, 0.90, 0.95` per unit source).
- **The answer to "is the mass a source of any channel without a mass term?"**
  - Never of the turn, by symmetry.
  - Not of anything in the six-outcome sea (on the grid).
  - With vacancies at the neutral scale, exactly on the surface above, where yes.

**(d) Records as boundary values in the massless channel.**
- Linearized as in block 42 T6, with records held at a common transverse lean and `u_x = (1/6)Σ_y u_y` off the body. The field is that lean times the probability that a simple random walk reaches the body. Its far field is `(3·cap/2π)/r`, since `G(x) ~ 3/(2π|x|)`.
- **Capacities on `Z³`** (CHECKED D1, D2; lattice Green function to `10⁻¹⁸`, checked against Watson's closed form and harmonicity):

  | body | capacity | per record |
  |---|---|---|
  | one record | `1/G(0) = 0.65946267` | `0.65946` |
  | two adjacent | `0.98387812` | `0.49194` |
  | two at distance 2 | `1.1275724` | `0.56379` |
  | `2³` cube | `1.8516546` | `0.23146` |
  | `3³` cube | `3.1562058` | `0.11690` |

- Capacities do not add, and the capacity per record falls as the body grows.
- For one record, `r·u(r) → 3/(2πG(0)) = 0.31487`. Block 42's executed `0.28–0.30` on a `27³` torus (six-axis, nonlinear) sits just below this infinite-lattice linear value.

## 2. Steps

**S1: Funk–Hecke (PROVED; CHECKED A1).**
- Expand `e^{βt} = Σ_l (2l+1) i_l(β) P_l(t)`. The addition theorem then gives `∫e^{βs·b}Y_l(b)dσ(b) = i_l(β)Y_l(s)`.
- Divide by `i₀(β) = sinh β/β` for the normalization.
- The recurrence is `i_{l−1} − i_{l+1} = (2l+1)i_l/β`.

**S2: the ordering (PROVED; CHECKED A2).**
1. Start from `i_l(x) = (x^l/(2^{l+1}l!))∫_{−1}^{1}(1−t²)^l e^{xt}dt`.
2. Integrate by parts: `∫(1−t²)^l e^{xt}dt = (2l/x)∫t(1−t²)^{l−1}e^{xt}dt`.
3. Hence `λ_l/λ_{l−1} = i_l/i_{l−1} = ⟨t⟩` under the density `∝ e^{xt}(1−t²)^{l−1}` on `[−1,1]`. That average lies in `(0,1)` for `x > 0`.

**S3: the linearization and the massless point (PROVED; CHECKED A3).**
- Write `π_y = 1 + δ_y`. Then `K₁π_y = 1 + K₁δ_y`, so `log π_x = Σ_y K₁δ_y + const + O(δ²)`, which gives block 42 T2(b)–(e) with `λ₁ → L`.
- `β_c` comes from `mpmath.iv`: `6L − 1` has opposite signs at the two ends of a `2·10⁻²⁰` interval, and `L` increases because `sinh β > β`.

**S4: the ordered sea (PROVED as stated; CHECKED B1–B3).**
- **Uniform fixed points.** They satisfy `F = (K₁F)⁶/⟨(K₁F)⁶⟩`.
- **B1.** Expanding in Legendre polynomials with exact rational projections gives `b` and `c₃`.
- **The linearization.** Write `ν_y = F(1 + η_y)`. Then `η_x = Σ_y (Aη_y − ⟨Aη_y⟩_F)` with `Aη = K₁(Fη)/g`.
  - `A` is self-adjoint in `L²(gF dσ)`, since `∫gF·f·K₁(Fη)/g = ∫∫F f e^{β s·b}Fη` up to normalization.
  - `A` commutes with rotations about `n`, so it splits by `m`. On `f(t)e^{imφ}` it has kernel `Σ_{l≥|m|} λ_l p_l^m(t)p_l^m(t')` (orthonormal associated Legendre functions).
- **The turn.** Rotating the sea by an angle `θ` about an axis perpendicular to `n` gives a family of fixed points. Its derivative, `η = (F'/F)(t)√(1−t²)cos φ`, is therefore an eigenvector of the uniform map `6A` with eigenvalue 1, that is `1/6` per neighbour. A wave `k` then has `1 − (6 − E(k))/6 = E(k)/6`: no mass term.
- **Near the point.** On the centre manifold the amplitude map is `a ↦ 6λ₁a + c₃a³`. At its fixed point `a*² = (1 − 6λ₁)/c₃`, its derivative is `6λ₁ + 3c₃a*² = 1 − 2ε` with `ε = 6L − 1`. So `μ_∥ = (1 − 2ε)/6 + O(ε²)` and `m_L² = (1 − 6μ_∥)/μ_∥ = 12ε + O(ε²)`.
- **Numerics.** Gauss–Legendre quadrature (`N = 96`, degree ≤ 70); `N = 64` agrees to `10⁻¹⁴`.

**S5: records (PROVED; CHECKED B2, C3).** The `SO(2)` statements of (c)(i)–(ii) are immediate from S4's decomposition into sectors, as argued in (c).

**S6: the seven-outcome reading at `g = 1` (PROVED as stated; CHECKED C1–C4).**
- **The map.** A site holds a record with probability `ρ_x` and content density `ν_x`. A neighbour's factor is `1 − ρ_y + ρ_y g K₁ν_y` for a content and `1` for "no record". Then `ν_x ∝ Π_y(...)` and `ρ_x/(1 − ρ_x) = z⟨Π_y(...)⟩`.
- **At `g = 1`.** The factor is `b = 1 + ρK₁u`, where `ν = 1 + u`: this is the reduction `λ → ρλ`.
- **The mass strength.**
  1. `δρ_x = ρ(1 − ρ)Σ_y ⟨δb_y/b⟩_F` and `δb_y = δρ_y(K₁F − 1) + ρK₁(Fη_y)`.
  2. So the mass-to-mass entry is `ρ(1 − ρ)⟨(K₁F − 1)/b⟩_F = (1 − ρ)(1 − ⟨b⁵⟩/⟨b⁶⟩)`.
  3. It is positive because `⟨b⟩ = 1` and power means increase: `⟨b⁶⟩ ≥ ⟨b⁵⟩^{6/5} ≥ ⟨b⁵⟩`, strictly when `b` is not constant.
- **The tricritical expansion.**
  1. `⟨b⁶⟩ = 1 + 5ρ²λ₁²a² + O(a³)`.
  2. At fixed fugacity the density rises by `ρ(1 − ρ)·5ρ²λ₁²a²`. That adds `30λ₁³ρ³(1 − ρ)a³` to the amplitude map.
  3. Substituting `ρ = 1/(6λ₁)` gives the quadratic condition, checked by sympy.
- **The fixed-fugacity branch.** At `ρ = 1.001ρ_c` the ordered branch needs `log z − log z_c = +2.9·10⁻⁵` at `β = 0.95` and `−6.3·10⁻⁶` at `β = 0.96`. So it bends back just above `β_t`, as the formula predicts.
- **The spinodal.** It is found by bisection on the top eigenvalue of the block `(δρ, η₀)`. The mass source's share is its coefficient on the unit right eigenvector, divided by the source's size.

**S7: capacities (PROVED as the linear boundary-value problem; CHECKED D1–D2).**
- `G(x) = ∫₀^∞ e^{−t} Π_i I_{x_i}(t/3) dt`, with the two-term tail beyond `10⁸`.
- `G(0)` is checked against `√6/(32π³) Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)`, and harmonicity against `G(1,0,0) = G(0) − 1`.
- The capacity is `cap(S) = 1ᵀG_S⁻¹1`.

## 3. The first failing step

- **The sector masses for every `β > β_c`.** They are shown only on a grid; no monotonicity argument is given.
- **The spinodal and the coexistence line with vacancies.** Only the spinodal is located, numerically. The first-order coexistence line beyond `β_t` at fixed fugacity is not computed.
- **Linearity of the boundary-value picture.** The capacity statement treats a record as a linear boundary value, as block 42 T6 does. The field next to a record is nonlinear and is not examined.

## 4. What would finish it

1. A proof that the sectors `m = 0` and `|m| ≥ 2` stay below `1/6` for every `β > β_c`.
2. The fixed-fugacity phase diagram with vacancies at the neutral scale: the coexistence line from the tricritical point, and whether the massless surface of (c)(iii) is reached by any stable state or only by the metastable one.
3. A nonlinear control: one held misaligned record in an ordered sea with the far boundary held, with its transverse `r·u(r)` against the capacity statement.
4. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/odds-field-sphere-menu/w-macbookpro90c72-j00d0/check.py
```

The run takes about 8 s and uses numpy, mpmath and sympy. It prints exact or certified checks A1–A4 and B1, spectral checks B2–B3 and C2–C4, symbolic C1, and D1–D2, then the SUMMARY and HIT lines.

Standard mathematics used, none as authority:
- Funk–Hecke's theorem;
- the Poisson integral for `i_l`;
- interval arithmetic (`mpmath.iv`);
- Gauss–Legendre quadrature;
- the Landau and centre-manifold expansion at a pitchfork;
- the simple-random-walk Green function and Watson's closed form for `G(0)`.
