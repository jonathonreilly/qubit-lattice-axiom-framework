# persistent-sources — attempt a5

Worker `w-jonathonsmac4f50-j09ae` (model claude-opus-5). Check script: `check.py` in this directory (exact rational torus solves for
`L = 6..16`, sympy; two numerical checks, labelled; about 12 s).

**How this attempt was prepared.**

- The plan was made before reading any prior material: treat persistent pins as a path-space large-deviation problem for the free
  Gaussian process, and compute it by minimal action.
- No attempt of this problem was printed at claim time.
- I then read the five round-1 referee reports on `two-source-interaction` and the simulator `probes/lib/formation_response.py`.
- Round 1 failed by conditioning the equal-time law instead of pinning at every level, as the task's GIVEN says. This attempt never
  conditions the equal-time law.

## 1. The model and the statements attempted

**Model (GIVEN).** `θ_{t+1} = P θ_t + ξ_{t+1}` on `Z³` or `(Z/L)³`:

- `P` is the average over the 7-stencil (self and six neighbours), with symbol `φ = 1 − E/7`, `E(k) = 6 − 2Σ cos k_j`;
- `ξ` is i.i.d. `N(0, σ²)`;
- `G = (I − P)^{−1}` has symbol `7/E`. On a torus it is the pseudo-inverse on mean-zero functions;
- `G² = G∘G`;
- `D(r) = G²(0) − G²(r)`.

**Interpretation of (a).** "The probability that the unpinned process stays within the pins" is read as the path probability that the
free process has `θ_t(y₁) = a` and `θ_t(y₂) = b` at every level `t ≤ T`. Its exponential rate per level, as `T → ∞`, is the pins'
cost. The `(a, b)`-dependent part is `ΔR(a, b; r)`.

**(a)** `ΔR(a, b; r) = (a − b)² / (4σ² D(r))`, with `r = y₂ − y₁`.

- *Like pins* (`a = b`) cost nothing at every distance.
- *Unlike pins* cost a positive amount, decreasing along the axis (computed).
- *Infinite volume.* `D(r)/r → 49/(8π)`, so `ΔR = 2π (a − b)² / (49 σ² r) + o(1/r)`. The coefficient of `1/r` is
  `2π(a − b)²/(49σ²)`.
- *Constant offset.* `D(r) − 49r/(8π) → ≈ 0.59` (numerical).
- *The cheapest pinning configuration.* The profile `μ(G²(· − y₁) − G²(· − y₂))` plus a free constant. It is not the pinned process's
  mean, which is a `G`-profile.

**(b)** Two field sources `h₁, h₂`, i.e. `θ_{t+1} = Pθ_t + h + ξ` with `h = h₁δ_{y₁} + h₂δ_{y₂}`.

- *The stationary mean* is `Gh = h₁G(· − y₁) + h₂G(· − y₂)` on `Z³`. On a torus a stationary law exists only for `h₁ + h₂ = 0`.
- *The path relative-entropy rate* against the free process is `(h₁² + h₂²)/(2σ²)`: no interaction.
- *The reversible law's `−log π`.* The linear chain is reversible, and `π_h = N(Gh, C)` with `C = σ²(I − P²)^{−1}`. So `−log π_h`
  couples to `θ` through `(I + P)h/σ²`. The free energy `F(h) = −log E_{π₀} e^{θ·(I+P)h/σ²} = −D(π_h ‖ π₀)` equals
  `−(1/(2σ²)) hᵀ(I + P)G h`. Its cross term is `−(2/σ²) h₁h₂ G(r)` for `r ≠ 0`, which is `−7h₁h₂/(2πσ² r)` at large `r` with
  `G(r) ~ 7/(4πr)`: like fields attract.
- *Answer.* The dynamical cost has no interaction energy, while the stationary law has a Coulomb one.

**(c)** Field sources superpose exactly (linear). Pins do not: the two-pin mean is not the sum of the one-pin means. The first
nonlinear correction in `1/β` is not attempted.

## 2. Steps

**S1 (PROVED) Reduction to the difference process.** Write `Δ_t = θ_t(y₁) − θ_t(y₂)` and `Σ_t = (θ_t(y₁) + θ_t(y₂))/2`.

- The point reflection through the midpoint of `y₁, y₂` is a lattice symmetry commuting with `P` (the stencil is symmetric). It maps
  `Δ → −Δ` and `Σ → Σ`, so the jointly Gaussian processes `Δ` and `Σ` are uncorrelated, hence independent.
- The path density of the pinned pair therefore factorizes into `Δ ≡ a − b` times `Σ ≡ (a + b)/2`.
- `Σ` contains the zero mode, and a common shift of the whole field costs nothing: `(I − P)1 = 0`. On a torus the zero mode is an
  exact random walk; on `Z³`, `G²(0) = ∞`. So the value of `Σ` enters only through an `O(1)` boundary term and not the rate.
- `ΔR` is therefore the constant-path rate of the stationary scalar Gaussian process `Δ`.

**S2 (ASSUMED, classical; CHECKED numerically A3).** For a stationary Gaussian process with continuous positive spectral density `f`,
the Toeplitz forms satisfy `(1/T) 1ᵀ Γ_T^{−1} 1 → 1/(2πf(0))` (Grenander–Szegő). So a constant path `δ` costs `δ²/(2 · 2πf(0))` per
level. `Δ`'s spectral density is continuous and positive on the circle: `k = 0` is absent, `|φ| < 1` elsewhere, and the numerator
`2 − 2cos k·r` is nonnegative and not identically zero.

*CHECKED (A3, numerical, `L = 6`, `r = 2e₁`):* `(1/(2T)) 1ᵀΓ_T^{−1}1 = 0.0896, 0.0870, 0.0856, 0.0850` at `T = 50, 100, 200, 400`,
decreasing toward `1/(4D) = 0.0843`.

**S3 (PROVED) The long-run variance.** `2πf_Δ(0) = Σ_τ Cov(Δ₀, Δ_τ) = σ² Σ_{k≠0} (1/N)|e^{ik·y₁} − e^{ik·y₂}|² / (1 − φ(k))²`. This is
`2σ² (1/N) Σ_{k≠0} (1 − cos k·r) · 49/E(k)² = 2σ² D(r)`. So `ΔR = (a − b)²/(2 · 2πf_Δ(0)) = (a − b)²/(4σ² D(r))`.

**S4 (PROVED; CHECKED A2) The same number by minimal action.** Minimize `(1/(2σ²))|(I − P)θ|²` over fields with
`θ(y₁) − θ(y₂) = δ`, with a common constant free. The Lagrange condition `(I − P)²θ = μ'(δ_{y₁} − δ_{y₂})` gives
`θ* = μ(G²(· − y₁) − G²(· − y₂)) + const` and `(I − P)θ* = μ(G(· − y₁) − G(· − y₂))`. The action is `δ²/(2D)`, so the rate per level
is `δ²/(4σ²D)`. This agrees with S3: the time-constant field `θ*` is the minimal-action path.

*CHECKED:* on `L = 8` with `r = 3e₁`, exactly: the constraint, the identity `(I − P)θ* = μ(G(· − y₁) − G(· − y₂))`, and the action
`1/(2D) = 2508359454720/20786148822853`. `(I − P)1 = 0` is also checked.

**S5 (PROVED; CHECKED A1, A4) Exact torus values and the `1/r` law.**

- *Tori.* `G` and `G²` solve `L₃ g = 7(δ − 1/N)` and `L₃ h = 7g` (mean zero), with `L₃` the lattice Laplacian. They are computed
  exactly in rationals on the octahedral orbits, for `L = 6, 8, 10, 12, 14, 16`, and cross-checked against FFT sums. For example
  `D_{16}(e₁) = 1.94881…`, an exact rational, and `D_L(r e₁)` increases with `r` on every torus.
- *Infinite volume.* Substitute `k = q/r`. Since `r²E(q/r) → |q|²` and `E(k) ≥ (4/π²)|k|²` on the zone, dominated convergence with
  the integrable majorant `min(q², 2)/|q|⁴` gives
  `D(r)/r → 49 ∫_{R³} (1 − cos q_z)/|q|⁴ d³q/(2π)³ = 49 (1/(2π²)) ∫₀^∞ (q − sin q)/q³ dq = 49/(8π)`.
  The last integral is `π/4` (CHECKED, sympy); the limit does not depend on the direction.
- *Numerical, labelled.* `D(r e₁) = 49 ∫₀^∞ t e^{−6t} I₀(2t)² (I₀(2t) − I_r(2t)) dt` gives `D/r = 2.0666, 1.9850, 1.9588, 1.9543` at
  `r = 4, 16, 64, 128`. The offset `D − 49r/(8π)` is `0.468, 0.566, 0.588, 0.592`.

**S6 (PROVED; CHECKED B1) Field sources: the mean.** Stationarity `m = Pm + h` gives `m = Gh`, linear in `h`, so the one-source means
superpose. On a torus the spatial mean grows by `h₁ + h₂` per level, so a stationary mean exists only for the dipole. *CHECKED:* the
dipole on `L = 8`, exactly.

**S7 (PROVED; CHECKED B2) The path rate.** Per level and per source site, the log-likelihood ratio of the sourced chain against the
free one is `((h + ξ)² − ξ²)/(2σ²)`, with mean `h²/(2σ²)`. So the rate is `(h₁² + h₂²)/(2σ²)`, independent of `r`.

**S8 (PROVED; CHECKED B3) The stationary law.**

- *Reversibility.* The chain is reversible, because `PC = CP` is symmetric; the referees of round 1 confirmed this. `π_h = N(Gh, C)`,
  and `C^{−1}G = (I + P)/σ²` since `(1 − φ²)/(1 − φ) = 1 + φ`.
- *The free energy.* So `F(h) = −(1/(2σ²)) hᵀ(I + P)G h = −D(π_h ‖ π₀)`.
- *The cross term.* Since `((I + P)G)(r) = 2G(r) − δ_{r,0}`, the cross term is `−(2/σ²) h₁h₂ G(r)` for `r ≠ 0`.
- *Large `r`.* `G(r) ~ 7/(4π r)` (ASSUMED: the standard lattice Green-function asymptotic; round-1 referee I1 reproduced it
  numerically), so the cross term is `−7h₁h₂/(2πσ² r)`.
- *CHECKED:* the dipole value on `L = 8`, `F = −3970507/1888768` at `σ = 1`, both through `(I + P)G` and through `2(G(0) − G(r)) − 1`.

**S9 (PROVED; CHECKED C1) Superposition for pins fails.** On `Z³`, the two-pin mean is `c₁G(· − y₁) + c₂G(· − y₂)` with
`[[G(0), G(r)], [G(r), G(0)]] c = (a, b)`. The sum of the one-pin means `αG(· − y)/G(0)` overshoots the pin at `y₁` by `bG(r)/G(0)`.

## 3. Reading the answers against the task's questions

- **(a)** The pin cost is quadratic in `a − b` alone.
  - *Sign.* Like pins: `0` at every `r`. Unlike pins: positive, decreasing toward `0` like `2π(a − b)²/(49σ²r)`.
  - *Self terms.* In infinite volume a single pin costs nothing at rate level, so the whole cost is "interaction". There is no separate
    self energy.
  - *Contrast with round 1.* This is not round 1's equal-time pin energy `a²/(C₀ ± C_r)`, which has a finite like-pin energy.
- **(b)** "Is there an interaction energy for a non-equilibrium process?"
  - The dynamical path cost (relative entropy rate) has no interaction.
  - The stationary law, which here is reversible, has one: `−(2/σ²)h₁h₂G(r)`, Coulomb-like, with like fields attracting.
  - The pin rate of (a) is a third object: a path large deviation, `∝ (a − b)²/r`.
  - These three quantities differ in sign structure, so "the interaction" must name which of them is meant.
- **(c)** Field sources superpose at linear order; pins do not.

## 4. Open

- The first nonlinear correction in `1/β` for the sphere law (the executed ratio `0.96–0.99`) is not attempted. It needs the cubic
  terms of the spin-wave expansion about the aligned plane.
- S2 is ASSUMED (a classical Toeplitz theorem) and checked numerically only. A self-contained proof, e.g. an LQ-control argument
  showing that time-constant paths are asymptotically optimal, would remove the assumption.
