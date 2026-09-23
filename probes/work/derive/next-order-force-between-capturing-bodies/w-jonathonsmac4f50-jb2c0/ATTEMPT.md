# next-order-force-between-capturing-bodies: derivation attempt 3 of 3

Worker `w-jonathonsmac4f50-jb2c0` (claude-opus-5-5), unit `J-derive-next-order-force-between-capturing-bodies-a3`.

**Provenance.** No earlier attempt at this problem is on `ai/probes` (a1 and a2 were not delivered). The plan is my own:
- steady linearized hydrodynamics of the sphere-menu gas;
- the momentum sink as a Stokeslet, since number conservation makes the steady flow exactly divergence-free;
- the second-order force from the collisional capture law.

**Sources.**
- Blocks 44 and 45 (PRs #8550, #8553): the mass current `J = (1 − ρ)g/√3`, the pressure `ρ/(3√3)`, the wind `g = √3Q/(4π(1 − ρ)r²)`, and `K₀ = √3/(4πρ(1 − ρ))`.
- Block 48: every captured record brings the wind's mean content `u = g/ρ`.
- Block 49 (PR #8559): the executed forces between bodies in balance and capturing bodies. The setup is side 96 with reservoir walls, `ρ = 0.3`, `γ = 1`, radius-3 balls with `Q ≈ 7.8`, and separation 16. The body in balance is pushed with `0.75 ± 0.06` of the reference and pulls with `0.10 ± 0.07`; two capturing bodies give `0.92 ± 0.05`.
- The task statement: the executed longitudinal diffusivity is about `0.6` (`0.62` from the damping `0.0030` per tick at wavelength 64).

Nothing is adopted.

## 1. Statement attempted

**(a) The linearized hydrodynamics.** Write `δρ` for the density perturbation and `g` for the momentum density, with the viscosity `ν` a parameter:

  `∂_t δρ + ∇·J = 0`,  with `J = (1 − ρ)g/√3`,
  `∂_t g + ∇p = ν∇²g + ν_b∇(∇·g) + f`,  with `p = δρ/(3√3)`.

This reproduces block 44's sound speed, `c² = (1 − ρ)/9`. The longitudinal diffusivity is `D_L = (4/3)ν + ν_b`. In a steady state, `∇·J = 0` gives `∇·g = 0` exactly at linear order. So the bulk term drops out, and a point momentum sink `f = −F δ` gives exactly the Stokes problem

  `ν∇²g − ∇p = Fδ`,  `∇·g = 0`.

**(b) The Stokeslet and the force.**
- The steady response is the Oseen tensor, `g(x) = −F·(I + r̂r̂)/(8πν r)`: `1/(4πνr)` along `F`, `1/(8πνr)` across it.
- A body taking up momentum `F₁` from a wind is such a sink.
- A capturing body 2 at distance `r` captures records that bring `u = g/ρ`, so it is pushed by `δF₂ = Q₂ g(r)/ρ`.
- With `F₁ = K₀Q₁Q₂/r²` (body 1 in body 2's wind), along the line of centres:

  `δF₂ = −(K₀ Q₁ Q₂²)/(4πνρ r³)` (towards body 1), i.e. `δF₂/F_ref = Q₂/(4πνρr)`, where `F_ref = K₀Q₁Q₂/r²`.

- **Sign:** attractive. The sink leaves a backflow towards body 1 at body 2.
- **Power:** `r^{−3}`, one power faster than the first order.
- **Dependence:** `∝ Q₁Q₂²/ν`.

A body in balance has no inverse-square wind (block 49 T1). It still takes up momentum with its gross capture, so it still makes this backflow. **This is the pull of a body in balance.**

**(c) Size at the executed parameters** (`Q = 7.8`, `r = 16`, `ρ = 0.3`).
- `δF₂/F_ref = 0.129/ν × (F₁/F_ref)`.
- With a non-negative bulk viscosity, `ν ≤ (3/4)D_L ≈ 0.465`. With block 49's measured push on the body in balance, `F₁ = 0.75F_ref`, the pull is **at least `0.21` of the reference** in infinite space.
- The executed box has side 96. As a comparator, a periodic box of side 96 keeps `0.70` of the axial Stokeslet at `r = 16`, which gives `0.15`.
- **Executed:** `0.10 ± 0.07` (block 49). The same mechanism adds a second-order push to two capturing bodies. The measured `0.92 ± 0.05` against the balanced push `0.75 ± 0.06` implies an extra `0.17 ± 0.08`.
- **The Stokeslet accounts for both**, within the errors, at the upper side of the pull.

## 2. Steps

**S1 (PROVED; CHECKED `E1.1`). The equations.**
- Number conservation with block 44's exact current gives the first equation.
- Momentum conservation (block 45 T2) gives the second. Its flux to first order is the pressure, plus a viscous stress. The viscous stress is a closure: its coefficients `ν` and `ν_b` are parameters, assumed isotropic.
- The two equations give `ω² = (1 − ρ)k²/9` (`E1.1`).

**S2 (PROVED). The steady problem is Stokes.** Stationarity gives `∇·J = 0`. Since `1 − ρ` is a constant background, `∇·g = 0`. Then the momentum equation reads `ν∇²g − ∇p = F δ` (the sink is `−Fδ`), with `p` the Lagrange multiplier.

**S3 (PROVED; CHECKED `E1.2`, `E1.3`). The Oseen tensor.**
- `u = (I + r̂r̂)e_x/(8πr)` and `p = x/(4πr³)` satisfy `∇²u = ∇p` and `∇·u = 0` for `r > 0` (sympy).
- The normalization, a unit force at the origin, is the standard Fourier inverse of `(I − k̂k̂)/k²`. That is ASSUMED at the continuum level. `N1` and `N2` confirm it through the lattice version: the lattice Green function tends to it, with the axial ratio `1.003` at `r = 4` on `192³`.

**S4 (PROVED within the closure). The force on body 2.**
- By block 48, a capturing body takes up `Q₂` times the mean content of the gas at it.
- The disturbance adds `δu = δg/ρ`.
- On the line of centres `(I + r̂r̂)F₁ = 2F₁`.
- So `δF₂ = −2Q₂F₁/(8πνρr)`, directed towards body 1 because `F₁` points from body 1 to body 2.
- Then insert `F₁ = K₀Q₁Q₂/r²`. The balanced body's measured push `0.75F_ref` replaces it in (c).

**S5 (PROVED; CHECKED `E2`, `N1`). The lattice Green function.**
- Use forward-difference gradients `d_a = e^{ik_a} − 1` and backward divergences.
- The discrete Stokes system is solved by `g = (I − dd†/|d|²)F/(ν|d|²)`, with `p = d̄·F/|d|²`, exactly (`E2`).
- `N1`: an FFT evaluation equals a direct solve of the real-space system on a periodic `6³` box to `4·10⁻¹⁶`. That is the check the task asks for.

**S6 (NUMERICAL, labelled; `N2`, `N3`). Box and numbers.**
- The periodic lattice Stokeslet is computed by FFT for sides 64, 96, 128, 192.
- The axial value at `r = 16` is `0.58, 0.70, 0.77, 0.85` of the continuum, roughly `1 − 1.8r/L`.
- Block 49's box has reservoir walls, not periodic ones. The periodic box is a comparator for the size of the finite-box reduction, not the executed boundary.

## 3. What is not settled, and what would finish it

- **`ν` itself.** Only the bound `ν ≤ (3/4)D_L` is used, which needs `ν_b ≥ 0`. A Chapman–Enskog value would fix the pull without the bound. The stress relaxation rate of clause (C) (`3γρ`, attempt a4 of the wind-force problem) is the start.
- **Anisotropy.** On a cubic lattice the shear viscosity has two components. Along a lattice axis the relevant combination is the one that sets the axial Stokeslet.
- **The executed boundary.** The Stokeslet of a reservoir-walled cube of side 96 (`g → 0` at the walls) would replace the periodic comparator. It is a larger sparse solve, not attempted here.
- **Higher orders.** The self-consistent loop (body 2's backflow slows the gas at body 1) is third order.

`SUMMARY: PROVED` within the linearized hydrodynamics, with the executed comparison labelled numerical (see `check.py`).
