# The force of a slow wind on a capturing sphere: the relaxation spectrum of the scattering clause

Attempt 4 of 4. Worker `w-macbookpro90c72-j9625`, model `claude-opus-5-5`. Script: `check.py` in this directory. It prints 5 checks, then a `SUMMARY` line and a `HIT` line.

**Provenance.** No earlier attempt at this problem is on `ai/probes`, and the plan is my own. There is no overlap with my other units. Sources: blocks 44 and 45 (PRs #8550, #8553), and the task statement's executed numbers.

**Result in one line.** This attempt delivers the part the task asks `check.py` for: the exact relaxation rates of the moments under clause (C). The flow past an absorbing sphere, and so an explanation of the executed `K/K₀`, is not solved.

## 1. Statement attempted

**Clause (C), sphere menu.** Each bond, at rate `γ`, re-draws the contents of its two records uniformly on the pairs with the same sum (block 44). For `s₁ + s₂ = P`, those pairs are the diametrically opposite points of the circle `C(P) = {s : |s| = 1, s·P̂ = |P|/2}`, with the uniform measure.

**Claim (exact).** Linearise the re-draw about the uniform content law: the one-particle law `(1 + εY)/4π`, with `Y` a degree-`l` harmonic, collides with a partner of the same law. The collision multiplies the degree-`l` part by

    μ_l = 4 ∫_0^1 u P_l(u)² du = 2 c_{⌊l/2⌋} c_{⌈l/2⌉},    c_k = (2k−1)!!/(2k)!!.

The first values, for `l = 1, 2, …, 8`, are `1, ½, 3/8, 9/32, 15/64, 25/128, 175/1024, 1225/8192`.
- **Momentum is conserved:** `μ₁ = 1`.
- **The traceless second moment is halved:** `μ₂ = ½`. This traceless moment is the part of the momentum flux that departs from the isotropic pressure; call it the stress.
- **For large `l`,** `μ_l ~ 4/(πl)`.

In the product closure a record meets a re-draw at rate `6γρ`: six bonds, each with the other end occupied. So the degree-`l` part of the local content law relaxes at `6γρ(1 − μ_l)`:
- `3γρ` for the stress (`l = 2`);
- `15γρ/4` for `l = 3`;
- `69γρ/16` for `l = 4`.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S1 — PROVED and CHECKED [K1]. The class is a circle.**
- `|s| = 1` and `|P − s| = 1` give `s·P = |P|²/2`: a circle around `P̂`.
- If `s` lies on it, so does `P − s`, since `(P − s)·P̂ = |P|/2`, and it is the diametrically opposite point.
- The uniform product measure conditioned on `s₁ + s₂ = P` is invariant under rotations about `P̂`, so it is uniform on the circle.

**S2 — PROVED and CHECKED [K1, K2]. The spectrum.**
1. The perturbation of `f ⊗ f` at first order is `ε(Y(s₁) + Y(s₂))`. So
   `μ_l ⟨Y, Y⟩ = ½ E_u[(Y(s₁') + Y(s₂'))(Y(s₁) + Y(s₂))]`,
   where `E_u` is the expectation over independent uniform contents.
2. *Funk–Hecke, over the circle.* The average of a degree-`l` harmonic over `C(P)` is `P_l(|P|/2) Y(P̂)`. Both outgoing contents lie on `C(P)`, so `E_φ[Y(s₁') + Y(s₂')] = 2P_l(|P|/2)Y(P̂)`.
3. *Funk–Hecke, over the partner.* Averaging `s₂` about `s₁`, with `t = s₁·s₂` uniform on `[−1, 1]`: `E_{s₂}[P_l(|P|/2) Y(P̂)] = Y(s₁) E_t[P_l(u) P_l(P̂·s₁)]`.
4. *The key coincidence.* `|P|/2 = P̂·s₁ = u = √((1 + t)/2)`.
5. Hence `μ_l = 2 E_t[P_l(u)²] = 2 ∫_0^1 P_l(√v)² dv = 4 ∫_0^1 u P_l(u)² du`.
6. The closed form `2c_{⌊l/2⌋}c_{⌈l/2⌉}` is verified exactly for `l ≤ 12`. It is not proved in general.

**S3 — CHECKED [K3]. `μ₂ = ½` by an independent route.**
- Let `g(P) = E_φ[s₁'s₁'ᵀ + s₂'s₂'ᵀ]`, and `T_ijkl = E_u[g_ij s₁_k s₁_l] = a δ_ijδ_kl + b(δ_ikδ_jl + δ_ilδ_jk)`.
- Two contractions fix `a` and `b`: `tr g = 2` gives `9a + 6b = 2`, and `E_t[s₁ᵀg s₁] = E_t[(1+t)²/2 + (1−t)²/4] = 1` gives `3a + 12b = 1`. So `a = 1/5`, `b = 1/30`.
- For a traceless quadrupole `Q`, a pair's traceless second moment goes from `4εQ/15` to `4bεQ = 2εQ/15`: halved.

**S4 — ASSUMED, then CHECKED [K4]. Product closure for the collision rate.** A record meets a re-draw at rate `6γρ`: each of its 6 bonds, times the probability that the other end is occupied. That probability is independent of the content law at this order.

**S5 — executed [K5], in floating point.** A Monte Carlo of the re-draw on 600,000 pairs drawn from `1 ± 0.3 P₂(z)`. The `±` difference cancels the second-order terms, and the `l = 2` factor comes out at `0.491`, against the exact `½`.

## 3. Where the route stops

The task's (a)–(c) ask for more than the collision spectrum. This attempt stops at the spectrum.

- **(a)** The collision part of the linearised kinetic operator is now exact. It is diagonal, with one rate per `l`, not a single relaxation time. The streaming part is not assembled:
  - steps along the axes with rates `|s_k|/√3`;
  - exchange with an occupied target, which moves contents but not records;
  - the product closure for exclusion.

  Its Chapman–Enskog viscosity has two parts, neither computed here. One is collisional, `∝ 1/(3γρ)`, from the `l = 2` rate above. The other is a lattice part from the randomness of the hops, independent of `γ`.
- **(b)** The flow past an absorbing sphere of radius `R` is not solved. That is the kinetic boundary-value problem, and it needs the missing pieces above. So `K/K₀(ρ, γ, R)` in the viscous regime, and the executed `1.02, 1.0, 0.72, 0.57`, are not explained here.
- **(c)** The inviscid value, with its sign change at `ρ = 3/5`, needs two things: a Reynolds number `gR/ν ≫ 1`, and a stress relaxation length `(speed)/(3γρ)` much smaller than `R`. Raising `γ` shortens the collisional part of `ν` as `1/(3γρ)` but cannot remove the lattice part. The largest reachable Reynolds number is bounded by the surface inflow of a capturing body. It is not computed here, so whether an executable run reaches it is not decided.

## 4. What would finish it

1. Assemble the linearised kinetic operator with the streaming, exchange and exclusion of the product closure. Its viscosity is then `ν = ν_coll(γ, ρ) + ν_lattice`, with `ν_coll` from `τ₂ = 1/(3γρ)`.
2. Solve Stokes flow past an absorbing sphere with that `ν`, including the depletion of the gas near the body and the slip set by the absorbing boundary. This gives `K/K₀` at `Re ≪ 1` as a function of `λ/R`.
3. Compare the result with `1.02, 1.0, 0.72, 0.57` (`ρ = 0.15, 0.3, 0.5, 0.75`) and `1.13, 0.87` (`γ = 0.1, 4`).
