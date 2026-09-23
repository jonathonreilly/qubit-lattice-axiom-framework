# The force of second order in the capture rates: derivation attempt 1 of 3

Worker `w-macbookpro90c72-j5f35` (claude-opus-5-5), unit `J-derive-next-order-force-between-capturing-bodies-a1`.

**Sources**, pinned by commit. Line numbers below refer to these heads.

| Block | PR | Head | What it supplies |
|---|---|---|---|
| 44 | #8550 | `502a7a21` | the clause; `J = (1 − ρ)g/√3` (L113); the sphere-menu step (L56) |
| 45 | #8553 | `e07ae767` | `K₀ = √3/(4πρ(1−ρ))` (L58); "Reynolds numbers below 0.1" (L4, L29, L107) |
| 48 | #8558 | — | the sampling closure, cited through block 49 L84: "in the closure every record that steps onto the body is a sample of the gas" |
| 49 | #8559 | `589280e3` | the remark naming this effect (L86); the balanced-body control (L96–L104); the pinned-body wind control (L106–L113) |

The simulators are in `probes/lib` (`inertial.py`, `inertial_balanced.py`). `check.py` verifies every exact claim, quotes 11 source lines verbatim (8 from the notes, 3 from `probes/lib`), and reads the committed outputs of the executed and numerical parts.

**Prior attempt and overlaps.**
- I formed the plan before reading anything of attempt a3 (`w-jonathonsmac4f50-jb2c0`, claude-opus-5-5, issue #8836). It has a self-triage but no referee, so nothing of it is GIVEN.
- Its summary line reaches the same answer to (a) and (b), the Stokeslet push `K₀Q₁Q₂²/(4πνρr³)`.
- For (c) it bounds `ν ≤ (3/4)D_L` and concludes that the push accounts for the executed pull.
- This attempt answers (c) differently, from three measurements:
  - the transverse diffusivity `ν_T`, measured with block 44's own simulator;
  - the box factor of block 49's actual walls (reservoirs, not periodic);
  - more seeds of block 49's own balanced control.
- Related earlier units of mine, on different tasks in the same lane:
  - #8725: capture rate of transparent bodies;
  - #8758: viscosity and damping of the inertial gas (its sound-damping closure);
  - #8759: the shadow force;
  - #8765: bodies in balance and the share of returning emissions;
  - #8828: the linearized sphere menu, where the stress harmonic relaxes at `3γρ`.

  None of them is an attempt at this problem. #8758 and #8828 supply the kinetic closure quoted in S7 as a cross-check only.

## 1. The statement attempted

Work in the sphere-menu gas at density `ρ`. Let `g` be the momentum density and `n` the number density.

**(a) Linearized hydrodynamics.**

```
∂_t n + ((1 − ρ)/√3) ∇·g = −Σ_b N_b δ_b
∂_t g + (1/(3√3)) ∇n = ν∇²g + ν_b ∇(∇·g) − Σ_b F_b δ_b
```

- The pressure is `n/(3√3)`, so `∂p/∂n = 1/(3√3)`.
- `N_b` is body `b`'s net uptake of records per tick, and `F_b` its net uptake of momentum.
- The sound speed is `c = √(1 − ρ)/3`. The transverse mode is purely diffusive, with `λ = −νk²` (CHECKED H1).

**(b) The response to a point momentum sink `F₁` at body 1, and the force on a capturing body 2 at `x₂ = r r̂`.**

1. In steady state `∇·g = 0` holds exactly, because `J ∝ g` and there is no number sink. So `ν_b` drops out.
2. The flow is the Stokeslet `g(x) = −G(x)F₁`, with `G = (I/|x| + x xᵀ/|x|³)/(8πν)`.
3. It carries a pressure `−F₁·x/(4π|x|³)` and a density change of `3√3` times that pressure.
4. By the sampling closure, body 2 takes up `C₂ g(x₂)/ρ` per tick, where `C₂` is its gross capture.

The push on body 2 is therefore

```
F₂⁽²⁾ = −(C₂/(8πνρr)) (F₁ + (F₁·r̂) r̂).
```

- **Sign.** Body 1 is pushed towards body 2, so `F₁ = f r̂`. Body 2 is then pushed towards body 1 with `C₂ f/(4πνρr)`: an attraction.
- **Across the axis.** A transverse `F₁` gives half that magnitude, antiparallel to `F₁`.
- **Power of r.** With `f = K₀ C₁ N₂/r²` (block 49, T3):

  ```
  F₂⁽²⁾ = K₀ C₁ C₂ N₂ / (4πνρ r³) = √3 C₁ C₂ N₂ / (16π² ν ρ² (1 − ρ) r³),
  ```

  which falls one power of `r` faster than the first order.
- **As a fraction** of the first-order reference `K₀C₁C₂/r²`, it is `(f/ref)·C₂/(4πνρr)`.
- **Dependence on the charges.** For two bodies that only capture (`C = N = Q`), body 2 feels `K₀Q₁Q₂²/(4πνρr³)` and body 1 feels `K₀Q₁²Q₂/(4πνρr³)`. At this order the pair forces are unequal. The momentum balance closes through the gas and the walls.
- **Dependence on ν.** The force goes as `1/ν`.

**(c) Its size at block 49's parameters.**

The parameters are `ρ = 0.3`, `γ = 1`, `r = 16`, `C₁ = 7.24` (in balance), `C₂ = N₂ ≈ 7.86` (7.84 in block 49, 7.82 to 7.92 in the new runs), and the reference `0.1455`.

- **The viscosity.** `ν_T = 0.36 ± 0.01`, measured with block 44's own simulator from the decay of shear waves along the axes. It varies by at most ±0.02 over `k = 0.10` to `0.39`, and it is `0.60` of the longitudinal `0.6`. The `(1,1,0)` shear gives `0.41`: the gas is cubic-anisotropic. Along a lattice axis the axial pull depends exactly on the axis value alone (S7a).
- **The box factor.** Block 49's walls are reservoir layers. At the second body they keep `0.92` of the free-space Stokeslet. A periodic side-96 box would keep `0.70`.
- **The predicted pull** of the body in balance on body 2 is `0.26 ± 0.02` of the reference. It uses the push `0.78 ± 0.05` on the body in balance, pooled over seven executed runs. In free space it would be `0.28`, and with the first-order push `1` it would be `0.33`.
- **The executed value.** Block 49 reports `0.10 ± 0.07` from two runs, with errors from the ten blocks of each run. Five new seeds of the same control give `+0.24`, `+0.32`, `−0.17`, `+0.12` and `−0.26`, each `±0.06` to `±0.11` by the same block errors.
  - Those block errors understate the run-to-run scatter by a factor `2.6`: `χ² = 39` for 6 degrees of freedom over the seven runs (S11).
  - With run-to-run errors the seven runs give `0.065 ± 0.079`. The pull is not resolved from zero, and the Stokeslet value lies `2.4σ` above the mean.
- **Answer to (c).** The Stokeslet pull at the executed parameters is `0.26` of the reference. That is not a small correction: at `r = 16` it is a quarter of the first-order force. The executed runs do not resolve a pull, so they can neither confirm nor exclude this size. They favour a smaller pull at the `2.4σ` level. Block 49's quoted `0.10 ± 0.07` understates its own error.

## 2. Steps

**S1 (PROVED; CHECKED H1).** The linearized equations of (a).
- Number conservation carries block 44's exact current `J = (1 − ρ)g/√3`.
- Momentum conservation carries the momentum flux `(n/(3√3))I`, plus viscous stresses parametrized by `ν` and `ν_b`.
- For a plane wave `e^{ikx + λt}`:
  - the longitudinal pair `(n, g_x)` has `λ² + (ν + ν_b)k²λ + (1 − ρ)k²/9 = 0`, so `c² = (1 − ρ)/9`. This agrees with the simulator's own prediction, `np.sqrt(1 - rho0) / 3` (`inertial.py`);
  - the transverse components satisfy `λ = −νk²`.

**S2 (PROVED; CHECKED H2).** The first order is recovered. A sink of `N` records per tick gives, in steady state, `g = −√3N x/(4π(1 − ρ)|x|³)`.
- It is divergence-free off 0, with number flux `−N` through every sphere.
- So `u = g/ρ = −K₀N r̂/r²`, which is block 45's wind.

**S3 (PROVED).** A pure momentum sink leaves an incompressible flow.
- In steady state `∂_t n = 0`, so `∇·J = 0` away from number sinks. Since `J = (1 − ρ)g/√3`, this gives `∇·g = 0` exactly.
- The momentum equation becomes `ν∇²g − ∇p = F₁δ(x − x₁)`, with `p = n/(3√3)`. The bulk term `ν_b∇(∇·g)` vanishes.
- Body 2's own number sink superposes linearly and adds S2's radial wind, which gives body 2 no net momentum.

**S4 (PROVED; CHECKED S1).** The Stokeslet solves this problem, and it is the only decaying solution.
- `G = (I/r + x xᵀ/r³)/(8πν)` with pressure `P_j = x_j/(4πr³)` satisfies `ν∇²G − ∇P = 0` and `∇·G = 0` off 0 (sympy, exact).
- `G` is homogeneous of degree −1, so `∂_rG = −G/r`. On `|x| = R`, the sphere integral of `ν∂_rG_ij − P_j n_i` is `−δ_ij` (exact integration). This is the unit point force on the gas.
- Uniqueness: take the difference of two solutions that decay at infinity.
  - Its pressure is harmonic, since the divergence of the momentum equation gives `∇²p = 0`. It decays, so it vanishes (Liouville).
  - Then every component of `g` is harmonic and decaying, so it vanishes too.
- Hence `g = −G F₁` and `p = −F₁·x/(4π|x|³)`.

**S5 (PROVED; CHECKED S2, S3).** The force on body 2.
- Block 48's closure says every record that steps onto a body is a sample of the gas. By the task's established statement (re-checked in S3), each captured record then brings the local `u = g/ρ`: capture is proportional to `|s|₁`, `⟨|s|₁⟩ = 3/2` and `⟨|s|₁ s_i s_j⟩ = δ_ij/2`.
- So `F₂⁽²⁾ = (C₂/ρ)g(x₂) = −(C₂/ρ)G(x₂ − x₁)F₁`.
- On the axis `G r̂ = r̂/(4πνr)`, and `G e_⊥ = e_⊥/(8πνr)` across it. The formulas of (b) follow, including the attraction and the `r⁻³` law, by sympy algebra.
- The Stokes flow is a first-harmonic local equilibrium plus even-harmonic gradient terms, and the even harmonics do not contribute to `⟨|s|₁ s⟩`.

**S6 (PROVED; CHECKED D1).** The lattice Green function against a direct solve.
- Take the steady lattice equations `Δg_j − ∇⁺_j p + f_j = 0` and `Σ_j ∇⁻_j g_j = 0` on a periodic box. Here `∇⁺` is the forward difference, `∇⁻` the backward difference, and `Δ = Σ∇⁻∇⁺` the 7-point Laplacian. The force `e_x` sits at the origin, compensated by its mean.
- Their Fourier solution is `ĝ = (I − a aᴴ/|a|²)f̂/(ν|a|²)` and `p̂ = aᴴf̂/|a|²`, with `a_j = e^{ik_j} − 1`.
  - Derivation: `∇⁺ ↦ a`, `∇⁻ ↦ −ā`, `Δ ↦ −|a|²`, and `|a|² = 0` only at `k = 0`.
- **The task's direct numerical solve** was done in exact arithmetic on `L = 3` and `L = 4`:
  - the real-space system (`4L³` unknowns), with the dependent equations replaced by `Σg = 0` and `Σp = 0`;
  - solved by exact rational elimination;
  - it equals the Fourier Green function at every site and component, and in the pressure. The Fourier side is evaluated in Q(ζ₁₂).
- This lattice Green function's free-space value at `r = 16` on the axis is `1.004` of the continuum `1/(4πνr)` (numerical, `box_green.txt`).

**S7 (EXECUTED; not claimed).** The transverse diffusivity.
- Method (`shear_wave.py`, block 44's own `tick_s`):
  - a periodic box at `ρ = 0.3`, `γ = 1`;
  - contents drawn from `(1 + 3u·s)/(4π)` with `u = ε cos(ky) x̂`, so there is no density perturbation;
  - the amplitude decays as `exp(−ν_T k²t)`.
- Results:

  | `k` | Side `L` | `ε` | `ν_T` |
  |---|---|---|---|
  | 0.098 | 64 | 0.3 | 0.359 ± 0.004 |
  | 0.131 | 48 | 0.3 | 0.363 ± 0.007 |
  | 0.196 | 32 | 0.15 | 0.350 ± 0.015 |
  | 0.196 | 32 | 0.3 | 0.337 ± 0.005 |
  | 0.262 | 48 | 0.3 | 0.355 ± 0.004 |
  | 0.393 | 32 | 0.3 | 0.341 ± 0.011 |
  | 0.139, along (1,1,0) | 64 | 0.3 | 0.411 ± 0.002 |
  | 0.185, along (1,1,0) | 48 | 0.3 | 0.417 ± 0.005 |

  Halving `ε` changes nothing within errors, so the runs are in the linear regime. The shear viscosity is cubic-anisotropic: `0.36` for a shear along the axes against `0.41` for the `(1,1,0)` shear. By S7a only the axis value `c = ν_T = 0.36 ± 0.01` enters block 49's on-axis pull.
- Cross-check, a closure (not claimed). Three contributions:
  - streaming, from the upwind hops and the exchange with occupied targets: `(3/16 + ρ/4)/√3 = 0.152`;
  - the redraw: `γρ/2 = 0.15`;
  - Chapman–Enskog: `1/(15λ₂)` with `λ₂ = 3γρ` (#8828), giving `0.074`. Its `(4/3)` multiple is #8758's sound-damping term `4/(135γρ)`.

  In continuous time the total is `0.376`. With the split tick's `γ → 1 − e^{−γ}` it is `0.32`. The measurement lies between them.

**S7a (PROVED; CHECKED S4).** Only the axis shear viscosity enters the on-axis pull.
- With cubic symmetry, the viscous operator on transverse modes is `c|k|² + d Σ_n e_n²k_n²`. The axis shear viscosity is `c`, and the `(1,1,0)` shear viscosity is `c + d/2`. The longitudinal and bulk parts are removed by the projection.
- The Stokeslet `Ĝ(k)` is even and homogeneous of degree −2. On the axis, `∫_0^∞ e^{ikrn_x} dk = πδ(rn_x)` plus a part odd in `n_x`, so `G_xx(r x̂) = (1/(2π)³)(π/r) ∮ Ĝ_xx(n) dφ` over the great circle `n_x = 0`.
- On that circle `x̂` is transverse to `n`, and the operator is diagonal in `{x̂, t}`. So `Ĝ_xx = 1/c`, and `G_xx(r x̂) = 1/(4πcr)` for every `d`.
- So the axial component of the pull uses `c` alone. The transverse components do depend on `d`: `t·D·t = c + (d/2)sin²2φ`.

**S8 (NUMERICAL; not claimed).** The box factor (`box_green.py`).
- Block 49's reservoir layers fix the density and give incoming records zero mean content. Macroscopically that is `p = 0` and zero tangential `g` on the walls, with the normal flux free.
- That problem is diagonal in the mixed sine/cosine basis. Equivalently, it is a periodic box of side `2D` with the image forces `f → −R f`: an x-reflection keeps `f_x`, and y- and z-reflections flip it.
- With the walls at 1.5 and 93.5, the Stokeslet at body 2 is `0.923` of free space; it is `0.922` to `0.925` for walls one layer either way.
- A periodic side-96 box gives `0.701`. Hasimoto's uniform term alone gives `0.685`.

**S9 (EXECUTED; not claimed).** More seeds of block 49's own balanced control.
- The command is `inertial_balanced.py 96 0.3 16 8000 <seed> 1.0 3 1.0 b c`. That is block 49's configuration: side 96, reservoir, two solid balls of radius 3 at separation 16, body 1 in balance, body 2 capturing, 1500 + 8000 ticks.
- Seeds 201–205 (floating point; the outputs are `balanced_bc_s20*.txt`). In block 49's units, per tick, with ten-block errors:

  | Seed | Body 1 (in balance): captures, emits | Push on body 1 | Body 2 captures | Pull on body 2 | Reference |
  |---|---|---|---|---|---|
  | 201 | 7.240, 7.241 | +0.124 ± 0.020 | 7.915 | +0.035 ± 0.016 | 0.1469 |
  | 202 | 7.238, 7.238 | +0.140 ± 0.019 | 7.824 | +0.046 ± 0.012 | 0.1452 |
  | 203 | 7.222, 7.221 | +0.132 ± 0.023 | 7.862 | −0.024 ± 0.009 | 0.1456 |
  | 204 | 7.255, 7.256 | +0.106 ± 0.017 | 7.862 | +0.018 ± 0.016 | 0.1462 |
  | 205 | 7.204, 7.204 | +0.082 ± 0.016 | 7.862 | −0.037 ± 0.014 | 0.1452 |

- Pooled with block 49's two runs, as fractions of each run's reference, with run-to-run errors:
  - push on the body in balance: `0.784 ± 0.054` (block errors consistent: `χ² = 9.1` for 6 degrees of freedom);
  - pull on the capturing body: `0.065 ± 0.079` (block errors not consistent: `χ² = 39.0`).

**S10 (PROVED arithmetic on S5–S9).** The size at the executed parameters.
- The ratio is `R = (f/ref)·C₂·b/(4πν_Tρr)`, with the box factor `b = 0.923`.
- With the pooled executed push `f/ref = 0.784 ± 0.054`: `R = 0.262 ± 0.019` in block 49's box and `0.284` in free space. The error combines the push, the spread of `ν_T` over the two smallest `k`, and 1% for the box.
- With the first-order push `f/ref = 1`: `R = 0.334`.
- Block 49's second control measures, for a smaller porous capturing body at `γ = 1`, a sampling efficiency of `0.89 ± 0.03` (L106–L113). Applied here it would lower `R` to about `0.23`.

**S11 (EXECUTED and NUMERICAL; not claimed).** The executed pull's errors.
- Block 49's errors come from ten 800-tick blocks of one run. For the pull, the seven runs scatter about their mean with `χ² = 39.0` against those errors, for 6 degrees of freedom. The errors understate the run-to-run scatter by a factor `2.6`.
- A mechanism of that size exists: slow flows of the box.
  - Under S8's walls, the slowest transverse flow of the gas has `k² = 2(π/D)²`, with `D = 92`. It relaxes at `ν_T k² ≈ 8.4·10⁻⁴` per tick, a time of about 1200 ticks. That is longer than a block.
  - Blocks correlated over `τ` count as about `10/(1 + 2τ/800) ≈ 2.5` independent ones. That understates the error by about `2`, of the observed size.
- The push on the body in balance (`χ² = 9.1`) carries larger block errors from its own emission noise, and does not show the excess.
- The run-to-run standard deviation of the pull is `0.21` of the reference per 8000-tick run.

**ASSUMED.**
- **(A1)** Linearized hydrodynamics at `r = 16`: the mean free path is about 1 site, and block 45 puts the Reynolds number below 0.1.
- **(A2)** Block 48's sampling closure for body 2. Its measured efficiency is `0.89 ± 0.03` at `γ = 1` for a smaller body.
- **(A3)** The reservoir walls act as in S8.
- **(A4)** The bodies are points. For a ball of radius `a`:
  - The uptake's anisotropic part is even in the surface normal, so its first moment (the stresslet) vanishes.
  - The remaining corrections are of relative order `(a/r)² ≈ 3.5%`. The Faxén term is `−a²/(3r²) = −1.2%` on the axis.
  - The number dipole from asymmetric capture and uniform emission gives about 1% of the reference.
  - The Stokeslet pressure gradient on body 2 gives about 0.4%.

## 3. Where the route stands

(a) and (b) are complete within A1 and A2. The step that stays open is not a derivation step but the executed comparison in (c).
- The size is computed from measured inputs: `0.26 ± 0.02` of the reference.
- The executed pull, `0.065 ± 0.079` with honest errors, does not resolve it. It lies `2.4σ` below it.

No step of the route fails. What (c) establishes is the predicted size, and that the executed pull's quoted error is too small.

## 4. What would finish it

- More executed ticks. At `0.21` of the reference per run, about 50 runs of block 49's control would bring the error to `0.03` and decide `0.26` against the present `0.07`. A smaller box with the same wall factor, or a variance-reduced estimator, would cost less.
- The sampling efficiency of a solid ball of radius 3 capturing 7.8 per tick at `γ = 1`, which block 49's second control measured only for a smaller porous body.
- A kinetic derivation of `ν_T`, to replace S7's measurement and bracketing closure.
- A direct test of the unequal pair forces, `K₀Q₁Q₂(Q₂ − Q₁)/(4πνρr³)`, between a light and a heavy capturing body.
