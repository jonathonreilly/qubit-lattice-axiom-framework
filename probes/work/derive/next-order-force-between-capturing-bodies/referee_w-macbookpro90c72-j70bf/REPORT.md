# Referee report: J:derive:next-order-force-between-capturing-bodies:a1

- **Author:** `w-macbookpro90c72-j5f35` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j70bf` (`grok-4.6`). Different model family.
- **Checks:** sympy on the continuum identities, and an independent real-space solve of the periodic lattice Stokes system. The author's script is not called. The shear-wave and balanced-body runs are not re-executed.

## The statement

In the sphere-menu gas, a pure momentum sink drives a Stokeslet, and a second capturing body is pulled toward the source as `K₀ C₁ C₂ N₂ / (4π ν ρ r³)`. That is (a) and (b). (c) is a size at block 49's parameters, not a new identity.

## Steps

**H1.** With `J = (1−ρ) g/√3` and `p = n/(3√3)`, a longitudinal wave has `λ² + (ν+ν_b) k² λ + (1−ρ) k²/9 = 0`, so `c = √(1−ρ)/3`. A transverse wave has `λ = −ν k²`.

**H2.** A number sink `N` gives `g = −√3 N x̂ / (4π (1−ρ) r²)`. The number flux through every sphere is `N`, and `u = g/ρ = −K₀ N/r²` with `K₀ = √3 / (4π ρ (1−ρ))`.

**S1–S2.** Off the origin, `G = (I/r + x xᵀ/r³)/(8πν)` with `P = x/(4π r³)` is divergence-free and solves `ν ∇² G − ∇P = 0`. On the axis `G_xx = 1/(4π ν r)` and the transverse entry is half of that. A sampler that takes up `(C₂/ρ) g` is therefore pulled toward the source by `C₂ F / (4π ν ρ r)`. Substituting the first-order push `F = K₀ C₁ N₂/r²` gives `K₀ C₁ C₂ N₂ / (4π ν ρ r³)`. If `C = N = Q`, body 2 feels a factor `Q₂` and body 1 a factor `Q₁`, so the pair forces differ by `K₀ Q₁ Q₂ (Q₂−Q₁)/(4π ν ρ r³)`.

**S3.** A pure momentum sink has `∇·J = 0` in steady state, and `J ∝ g`, so `∇·g = 0` and `ν_b` drops out. That step is the divergence identity above.

**S4.** On the periodic boxes `L = 3` and `L = 4`, a least-squares real-space solve of `Δg − ∇⁺ p + f = 0` and `∇⁻·g = 0` matches the Fourier solution `ĝ = (I − a a†/|a|²) f̂ / |a|²` to `1e−15`.

**S10.** The arithmetic `R = (f/ref) C₂ b / (4π ν ρ r)` at `ρ = 0.3`, `r = 16`, `ν = 0.36`, `C₂ = 7.86`, `b = 0.923` and `f/ref = 0.784` is `0.262` (`0.284` in free space, `0.334` if the push is the full first-order value). The executed scatter behind that `0.784`, and the `2.4σ` comparison, were not re-run.

## Verdict

(a) and (b) survive. The second-order force is the Stokeslet pull, attractive, `r⁻³`, and unequal between the two bodies.
