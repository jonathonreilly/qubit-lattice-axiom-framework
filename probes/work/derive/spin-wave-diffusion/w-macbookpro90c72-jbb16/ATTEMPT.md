# spin-wave-diffusion, attempt 3 (worker w-macbookpro90c72-jbb16, model grok-4.6)

## (1) The statement attempted

Objects of blocks 26 and 34: sphere formation on the `L × L` torus; one-site conditional is von Mises–Fisher with
concentration `κ = β|S|`, `S` the sum of the three predecessors; Langevin `A(κ) = coth κ − 1/κ`; linearized noise
`σ² = A(3β)/(3β)`. Write `N = L²`, `M_t = N^{−1} Σ_x s_x(t)` the plane average, `n_t = M_t / |M_t|` its direction,
and `D_L` the diffusion constant of `n_t` defined by `E|n_{t+ℓ} − n_t|² ∼ 4 D_L ℓ` (two transverse components, so
`D_1 = 2 D_L` in the probe's per-component normalization, and the probe's ratio is `D_1 L² / σ²`).

**Statement (PARTIAL).** (i) A single vMF draw of concentration `κ` has mean `A(κ) n` and transverse variance `A(κ)/κ`
per component (exact). (ii) If every predecessor triple is the same vector of length 3 (aligned plane), the plane
average `M'` has mean `A(3β) n` and independent-site transverse variance `σ² / N` per component. (iii) The map
`M ↦ M/|M|` has derivative `(I − nnᵀ)/|M|` on the tangent space, so to first order the direction diffuses
`1/|M|²` times as fast as `M` itself. (iv) Hence on the aligned plane, `D_1 L² / σ² = 1 / |M|² = 1 / A(3β)²`.
This is the large-`β` limit at fixed `L` (spin-wave variance → 0, `|M| → A(3β) → 1`, ratio → 1). It is *not* the
executed factor at moderate `β`: `1/A(3β)²` is `1.121, 1.058, 1.028, 1.014` at `β = 6, 12, 24, 48`, while the
probe's ratios are `1.34, 1.14, 1.06, 1.02`. The missing enhancement is the reduction of `|M|` below `A(3β)` by the
nonzero modes (block 34's `V_L`); the first-order Jacobian still says the ratio is `1/|M|²` for the *actual*
magnetization. Controlling `E[1/|M|²]` and the fluctuation of `κ_x` by `V_L` is the remaining step (not closed).

## (2) Steps

**Step 1 — vMF moments (PROVED; CHECKED as S1).** Density `∝ e^{κ s·n} dσ` on `S²`. With `μ = s·n`,
`Z = 4π sinh(κ)/κ`, `E[μ] = ∂_κ log(sinh κ / κ) = coth κ − 1/κ = A(κ)`. `E[μ²] = 1 − 2A(κ)/κ`, hence each of the
two transverse components has variance `(1 − E[μ²])/2 = A(κ)/κ`. Checked: the identities
`A' = 1/κ² − 1/sinh² κ`, `1 − A² − 2A/κ = 0` is *false* (that would be the 1D Langevin); the correct relation is
`E[μ²] = 1 − 2A/κ`, i.e. `1 − E[μ²] − 2A/κ = 0`, at 40 digits for `κ = 1, 3, 6, 18, 36, 72, 144`.

**Step 2 — aligned-plane one-step (PROVED).** On the aligned plane every `S_x = 3n`, `κ_x = 3β`. The `N` draws are
conditionally independent, so `M' = N^{−1} Σ s_x` has mean `A(3β) n` and covariance `(A(3β)/(3β)) N^{−1}` times the
projector `I − nnᵀ` (plus a longitudinal piece of order `1/N`). Per transverse component this is `σ² / L²`. The
linearized zero mode (block 34) is exactly this: `θ̄_{t+1} = θ̄_t + ξ̄` with `Var ξ̄ = σ²/L²`.

**Step 3 — Jacobian of the direction (PROVED; CHECKED as S2).** For `M ≠ 0`, `d(M/|M|) = (I − nnᵀ) dM / |M|`.
Checked: the `3×3` Jacobian matrix of `x ↦ x/|x|` at `x = (0,0,m)` is `diag(1/m, 1/m, 0)`, for `m = 1, 1/2, 3/4`
as exact rationals (sympy). Consequently, if `M` diffuses with transverse variance `v` per step, `n` diffuses with
`v / |M|²` plus `O(v²)` Itô corrections (ASSUMED: the Itô term is higher order in `1/N` at fixed `β`).

**Step 4 — aligned-plane ratio (PROVED).** Steps 2–3 give `D_1 = (σ² / L²) / A(3β)²` on the aligned plane, i.e.
`D_1 L² / σ² = 1/A(3β)²`. As `β → ∞`, `A(3β) = 1 − 1/(3β) + O(β^{−2})`, so the ratio is `1 + 2/(3β) + O(β^{−2}) → 1`.
Checked: `A(3β)` and `1/A(3β)²` at the four executed couplings (S3).

**Step 5 — why the executed table is larger (PROVED as a comparison, not a bound).** The actual `|M|` is smaller than
`A(3β)` by the spin-wave (nonzero-mode) variance. Block 34: `E|θ_x|² = N^{−1} Σ_{k ≠ 0} σ²/(1 − u(k))`. The z-component
of a nearly aligned spin is `1 − |θ|²/2`, so `E|M| ≈ 1 − (1/2) E|θ|²`. The Jacobian then predicts
`D_1 L² / σ² ≈ 1 / (E|M|)²`, which tracks the executed 1.34…1.02 once `|M|` is the measured magnetization, but this
identification is not proved: one still has to (a) replace `κ_x = 3β` by `β|S_x|` with `S_x` fluctuating, (b) justify
replacing `|M|` by its mean inside `1/|M|²`, (c) control the Itô/second-order terms. Not closed.

## (3) First unclosed step

Step 5. The aligned-plane calculation (steps 1–4) is exact and gives ratio `1/A(3β)² → 1`, which is the asked
`β → ∞` at fixed `L` for the *aligned* (or linearized) law. The nonlinear enhancement at finite `β` is the Jacobian
`1/|M|²` evaluated at the reduced magnetization, but passing from that heuristic to two-sided bounds
`c_1 / |m|² ≤ D L²/σ² ≤ c_2 / |m|²` needs a remainder controlled by `V_L`.

## (4) What would finish it

Expand `A(β|S|) S/|S|` to second order in the three predecessors' transverse parts, average using the Gaussian
covariances of block 34 (the matrix `σ² (I − PP*)^{−1}`), and bound the cubic remainder by `E|θ|⁶ ≤ C V_L³` at large
`β`. The Itô term for `n = M/|M|` is `O(σ² / (N |M|³))` per step and is smaller than the leading `σ²/(N |M|²)` by
`1/(N |M|)`.
