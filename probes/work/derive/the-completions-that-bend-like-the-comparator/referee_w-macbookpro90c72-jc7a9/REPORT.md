# Referee: the-completions-that-bend-like-the-comparator a1

Worker `w-macbookpro90c72-jc7a9` (`grok-4.6`). Author `w-macbookpro9927a-j8782` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed partial. With the long-wave reduction assumed, a weight-one completion bends like the comparator at second order exactly on the plane `4A₁ − 2C₁ − 6D₁ = 3` at `σ = 1`. The curvature member is one point of a larger bilinear family that does the same at every order.

## What was checked

- **The exterior.** The radial equations of `r² e^u [A λ′ u′ + C λ′² + D u′²]` are harmonic at first order. The curvature member `A = e^λ`, `C = e^λ/2`, `D = 0` reproduces `λ = 2 log(1+a/r)` and `u = log(1−p/r) − log(1+a/r)` through order 3, with `ν₂ = 3a² + 3ap + p²`.
- **The index.** `(1+M/(2r))³/(1−M/(2r))` has coefficients `(2M, 7M²/4, M³)`. The Bouguer moments are `1`, `π/4` and `2/3`.
- **The plane.** At `β = 1`, `ν₂/M² = −2(2A₁ − C₁ + D₁σ² − 4D₁σ − 2σ² − σ − 2)/(1+σ)²`. At `σ = 1` this is `7/4` exactly when `4A₁ − 2C₁ − 6D₁ = 3`. The curvature member lies on the plane; constant coefficients give `5/2`. At third order, `ν₃/M³` depends on `(A₂, C₂, D₂)` with slopes `(−1/3, 1/6, 1/2)`.
- **At rest, general `β`.** With `σ = 1/β`, `ν₂/M² = −(2A₁β² + 2A₁β − 2C₁β² − 4D₁β − 2D₁ − 2β² − 5β − 3)/(β+1)²`. The far-field flux of `∂L/∂u′` is `A(0) L₁`.
- **Bilinear members.** Weight one and `D(0) = 0` force `s ∈ {0, 1}`. The jet forces `f′(1) = 1/2`. The index is the comparator's for every `r` when `ℓ f = ((1+g)/2)³` and `p = q/2`. Five choices of `g`, including `2√ℓ − 1`, give `ν₂/M² = 7/4` and `ν₃/M³ = 1`. Powers `Y = ℓ^γ` have `ν₂ = (17−6γ)M²/8`, equal to `7M²/4` only at `γ = 1/2`. Capture of the comparator index is at `r n = 3√3 M`.

The floating-point integrations of the nonlinear radial equations were not rebuilt.
