# Fall and bending of rays with the full inverse metric

Attempt 2 of 2. Worker `w-macbookpro90c72-j2bd3`, model `claude-opus-5-5`. Script: `check.py` in this directory. It prints 4 checks, then a `SUMMARY` line and a `HIT` line.

**Provenance.** No earlier attempt at this problem is on `ai/probes`, and the plan is my own.
- **Overlap.** My unit `ray-limit-of-the-clocked-walk:a4` (issue #8760) studied the adiabatic ray limit of the walk: its lattice Berry curvature, which is a correction at the next order in gradients. That correction is not used here. The ray equations below are the leading (eikonal) order.
- **Sources.**
  - Block 59 (PR #8581): T4, bending against falling, and the rates.
  - Block 60 (PR #8590): the curvature member's static field; T4(d), the far fields.
  - Block 62 (PR #8592): the frame, `H = ½Σ_j{E^j·σ, S_j}`; T1, `H² = g^{ij} sin k_i sin k_j`; T4, the transverse traceless disturbances.

## 1. Statement attempted

**Setting.** The ray function is

    E(x, k)² = a(x)² m² + w(x)² Σ_ij g^{ij}(x) sin k_i sin k_j,    g^{ij} = Σ_a E_a^i E_a^j.

Here `a` is the rate that times the rest energy and `w` the rate that times the hops. Rays follow Hamilton's equations: `ẋ = ∂E/∂k`, `k̇ = −∂E/∂x`.

**(a) The ray equations.** Exactly, with `s_j = sin k_j`:

    v_i = w² Σ_j g^{ij} s_j cos k_i / E,
    k̇_i = −[m² a ∂_i a + w ∂_i w g^{jl} s_j s_l + (w²/2) ∂_i g^{jl} s_j s_l] / E.

- *A slow body.* It falls with `dv^i/dt = −w² g^{il} ∂_l log a`: the metric raises the index.
- *An isotropic frame.* For `g = δ/ℓ²` this is block 59's `E² = a²m² + c² Σ sin² k` with `c = w/ℓ`. A ray along an axis then turns at `−c² ∂_⊥ log c`, exactly on the lattice.

**(b) Block 60's field as a frame.** Write it as `E = (1/ℓ)·1` with `ℓ = w̄/w`, and take `a = w`. Then `c = w²/w̄`, so bending/fall `= d log c/d log a = 2` exactly. In block 60's strong field (`ℓ = χ²`, `w = N/χ`) the far-field ratio is `(P + 3Q)/(P + Q)`, which is block 60 T4(d)'s `1 + 2Q/(P + Q)`.

**(c) Transverse traceless disturbances.** Take `h = (A₊(e₁e₁ − e₂e₂) + A_×(e₁e₂ + e₂e₁)) cos(q x₃ − Ωt)`, so `g^{ij} = δ − h` at first order.
- *Which components.* A ray along axis `j` feels only the row `h_j·`:
  - `h_jj` slows it, `v_j = cos k (1 − h_jj/2)`, which gives the delay `½∫h_jj`;
  - `h_jj` also turns it towards `∇_⊥ h_jj`, at `k̇_⊥ = (sin k/2) ∂_⊥ h_jj`;
  - `h_jl` (`l ≠ j`) drifts it sideways, `v_l = −h_jl`.
- *Along the unperturbed ray,* delay, drift and turn are bounded oscillations: of size `A/Ω` for the delay and drift, `qA sin k/(2Ω)` for the turn.
- *A ray along `q`* feels nothing at first order.

**(d) Rest energy compatible with a frame.**
- No hermitian 2×2 matrix anticommutes with `σ₁`, `σ₂` and `σ₃`. So no on-site rest energy that is the same at every site is compatible with a frame whose coin vectors span three axes. The reduced walk's `mσ₁` requires `E₁^j = 0`, a frame of rank at most 2.
- The staggered term `(−1)^{x₁+x₂+x₃} m` anticommutes with the hops of every frame field, and so gives `(H + M)² = H² + m²`. It changes sign under a unit translation.
- Timed by the site rate `a`, it falls as block 59 says, with the inverse metric: `−w² g^{il} ∂_l log a`.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S0 — ASSUMED: the ray limit.** For fields that vary slowly on the lattice scale, a wave packet of the walk follows Hamilton's equations for the local symbol's eigenvalue `E(x, k)`.
- This is the eikonal limit.
- The Berry-curvature (anomalous velocity) correction is of next order in gradients (#8760) and is not included.
- The symbol's square is `a²m² + w²g^{ij}s_is_j` for uniform fields: block 62 T1, block 59, and S5 for the rest energy.
- Symmetrising the anticommutator changes the symbol only at first order in gradients.

**S1 — PROVED and CHECKED [R1]. The ray equations.** Differentiate `E` (sympy, with generic functions `a`, `w`, `g^{ij}` of `x`). The two closed forms above hold identically.

**S2 — PROVED and CHECKED [R1]. The fall.** At `k = 0`:
- `∂v_i/∂k_l = w² g^{il}/(am)`;
- `k̇_l = −m ∂_l a`;
- so `dv_i/dt = −(w²/a) g^{il} ∂_l a`.

For the isotropic frame the ray along axis 1 across a gradient along `x₃` has `∂v₃/∂k₃ = c²/E` and `k̇₃ = −c ∂₃c sin²k₁/E`, so `dv₃/dt = −c ∂₃ c`. This is block 59 T4, recovered symbolically.

**S3 — PROVED and CHECKED [R2]. Bending twice the fall.**
- *Weak field.* With `E = (1/ℓ)·1`, `c = w/ℓ`. Block 60 has `β = 1`, so `ℓ = w̄/w` and `c = w²/w̄`. With `a = w`, `d log c/d log a = 2`.
- *Strong field.* `ℓ = χ²` (block 60 premise), so `c = w/χ² = N/χ³` and `a = N/χ`. Far away `log c ≈ −(P + 3Q)g` and `log a ≈ −(P + Q)g`, so the ratio is `(P + 3Q)/(P + Q)`.

**S4 — PROVED and CHECKED [R3]. Transverse traceless disturbances.** Block 62 T4 has `p_i h_ij = 0` and `h_ii = 0`. For `q` along axis 3, `h_{i3} = 0`, and a plane polarisation has `h₁₁ = −h₂₂ = A₊` and `h₁₂ = A_×`.
- *Ray along axis 1.* Expanding `E = √(g^{ij}s_is_j)` to first order at `k = (κ, 0, 0)`, with `κ = π/3` exactly, gives:
  - `v₁ = cos κ (1 − h₁₁/2)`;
  - `v₂ = −h₁₂`;
  - `v₃ = 0`;
  - `k̇₂ = 0`;
  - `k̇₃ = (sin κ/2) ∂₃ h₁₁`.
- *Integrated* along `x₃ = z₀` for `0 < t < T`:
  - the drift is `−A_×(sin qz₀ − sin(qz₀ − ΩT))/Ω`;
  - the turn is `−sin κ A₊ q (cos(qz₀ − ΩT) − cos qz₀)/(2Ω)`.
- *Ray along axis 3.* All first-order terms vanish.
- *General axis.* The row structure holds for any axis `j`, because at `k ∥ e_j` only `g^{jj}` and `g^{jl}` meet `s_j`.

**S5 — PROVED and CHECKED [R4]. Rest energy.**
1. *Nothing anticommutes with all three.* Write `M = m₀ + Σ m_a σ_a`. Then `{M, σ_b} = 2m₀σ_b + 2m_b`, which vanishes for all `b` only if `M = 0`.
2. *A full frame.* If `{E^j·σ}` spans the three `σ`'s, the same holds.
3. *The reduced walk.* `{σ₁, E·σ} = 2E₁`, so `mσ₁` requires `E₁^j = 0` for every `j`.
4. *The staggered term.* Every hop of `½Σ_j{E^j(x)·σ, S_j}` joins sites of opposite parity, for any frame field. So `ε(x) = (−1)^{x₁+x₂+x₃}` anticommutes with it, and `(H + mε)² = H² + m²`. On a 4³ torus with a random integer frame field this is checked in exact integer arithmetic: `{ε, H} = 0`, and `(H + mε)² − H² − m² = 0`.
5. *Covariance.* `ε` flips under a unit translation and is invariant under proper rotations about a site.
6. *The fall.* With the site rate, `M = a m ε` gives `E² = a²m² + w²g^{ij}s_is_j` for uniform fields, and S2 applies.

## 3. Where the route stops

- S0, the ray limit, is assumed; no floating-point packet control was run.
- The lattice placement of `h` (block 62: diagonal entries on sites, off-diagonal on faces) is replaced by its value at the ray, which is exact only at leading order in gradients.
- The staggered rest energy doubles the unit cell and couples `k` with `k + (π,π,π)`. Its species structure (blocks 68–70) is not worked out here.
- Second-order effects of the disturbances are not computed. In particular, a ray moving along `q` at the disturbances' speed could accumulate an effect.

## 4. What would finish it

1. A packet control on a 2D slice, in floating point and labelled as such: bending over fall in block 60's weak field, and the row structure for a slowly varying `h`.
2. The anomalous velocity in a frame: #8760's Berry curvature with `g^{ij}` present.
3. Second order in `h`, for rays co-moving with the disturbances.
