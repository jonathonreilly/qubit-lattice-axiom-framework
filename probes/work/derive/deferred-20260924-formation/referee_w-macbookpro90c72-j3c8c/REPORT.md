# Referee: deferred-20260924-formation a1

Attempt `w-macbookpro9927a-jd76a`. This script does not import that attempt. The seeded Monte Carlo was not repeated.

The chain is the periodic plane `Z_L^2`. Each record is a unit vector. The local field is `S_x = s_x + s_{x-e1} + s_{x-e2}`, and the next record is drawn with density proportional to `exp(β s · S_x)`. `A(κ) = coth κ − 1/κ`, `σ² = A(3β)/(3β)`, `τ_L = L²/σ²`, and `S*_L = L^{-2} Σ_{k≠0} 1/(1−u_k)` with `u_k = (3 + 2 cos k1 + 2 cos k2 + 2 cos(k1−k2))/9`.

## Verdicts

**S1, S6.** The moments of `w` on `[-1, 1]` are `A`, `1 − 2A/κ`, and `coth κ − 3/κ + 6A/κ²`. The third-moment combination `E[(1−w²)(w−A)]` equals `2/κ − 6A/κ² − 2A²/κ`.

**S4, S5.** `A(κ) = 1 − 1/κ + 2/(e^{2κ}−1)`. In the power-law part, the ratio of local noise to `σ²` at field length `3 − q/2` is `6/(6−q) − 6q/((6−q)²(3β−1))`, whose large-`β` value is `1 + q/6 + O(q²)`. The transverse trace of the von Mises–Fisher covariance is `b(1+c²) + ℓ(1−c²)`.

**D1–D3.** On stereographic rational points of the sphere, for `L = 2` and `L = 3`, `Σ_x S_x = 3 Σ_x s_x` and `|S_x|² = 9 − Σ_{i<j}|s_i−s_j|²`. The part of `Σ h_x S_x` orthogonal to the mean equals the same sum with every height shifted by a constant, because `Σ S_x` is parallel to the mean.

**S8.** `1 − n·n' = X/2 − (3/8) X² + O(X³)` with `X = |b|²/(m+a)²`.

**C1, C2.** Exact cosines give `S*_2 = 27/32`, `S*_3 = 11/9`, `S*_4 = 189/128`, `S*_6 = 2627/1440`. For `L = 2, 3, 4` the circulant Lyapunov equation reproduces `c(0,0) = S*` and `E(Pπ̃)² = S* − 1 + 1/L²` per component at `σ² = 1`.

**F1–F3, under A1–A2.** Inserting the attempt's assembled moments into the chord expansion gives
`x₁ τ_L = 1 + σ²(S*_L + 2 − 1/L²) + O(σ⁴)`,
`λ₁ τ_L = 1 + σ²(S*_L + 2 − 1/(2L²)) + O(σ⁴)`,
`1/E|M|² = 1 + 2 σ² S*_L + O(σ⁴)`.
At `S* = 0` and `L = 1` the memory slope is `3/2`. These three series are conditional on the small-noise premises A1 and A2. Those premises are not proved.

**F4.** The first-order gap `2 − 1/(2L²) − S*` is `33/32`, `13/18`, `63/128`, and `233/1440` at `L = 2, 3, 4, 6`. Floating-point sums are positive at `L = 5, 7` and negative at `L = 8, 9, 10, 16, 32, 64`, each separated from zero by more than `10^{-3}`.

**Log coefficient.** `1 − u = (2/9)(k1² − k1 k2 + k2²) + O(k⁴)`. The angular integral of the inverse quadratic form is `4π/√3`, so the infrared coefficient of `S*_L` is `2 c₀ log L` with `c₀ = 3√3/(4π)`. The additive offset `0.3528…` was not recomputed. The excess of `λ₁ τ_L` over 1 then has log coefficient `2 c₀ σ²`, and `1/|M|²` has `4 c₀ σ²`.

**E, unconditional at `L = 1`.** Here `λ₁ = −log A(3β)` and `τ₁ = 1/σ²`, so `λ₁ τ₁ = −κ log A/A` with `κ = 3β`. For `κ > 0`:

- `κ cosh κ − sinh κ` vanishes at 0 and equals `∫₀^κ t sinh t dt`. Since `cosh κ = (e^κ + e^{-κ})/2 > 0`, `sinh` is positive and the integrand is positive, so `A(κ) > 0`.
- `e^{2κ} − 1 − 2κ − 2κ²` equals `∫₀^κ ∫₀^t ∫₀^s 8 e^{2u} du ds dt`, so it is positive. The identity `A − κ/(κ+1) = −(that quantity)/((e^{2κ}−1)κ(κ+1))` follows, and the denominator is positive. Thus `A < κ/(κ+1) < 1`.
- The same identity rearranges to `1 − A − A/κ = (e^{2κ}−1−2κ−2κ²)/(κ²(e^{2κ}−1)) > 0`.
- `−log(1−z) − z` vanishes at 0 and has derivative `z/(1−z) > 0` on `(0,1)`. With `z = 1−A`, `−log A > 1−A > A/κ`.

Therefore `−κ log A/A > 1` for every `κ > 0`. Dropping the exponential tail `2/(e^{2κ}−1)` and setting `A = 1 − x`, the rate is `1 + (3/2)σ² + O(σ⁴)`.

## What stays open

A1 (stationary moments of the relative field at large `β`) and A2 (increment correlations of order `σ⁶`) are assumptions. The one-level coefficient uses A1. The memory-rate coefficient uses A1 and A2. The Monte Carlo table, the historical rows, and the continuum additive constant were not rebuilt.

## Result

HIT: confirmed. The factor `1/|M|²` is not the strong-coupling memory law. Under A1–A2 the memory rate is `1 + σ²(S*_L + 2 − 1/(2L²))` at first order, and at one site the rate exceeds 1 for every `β > 0`.
