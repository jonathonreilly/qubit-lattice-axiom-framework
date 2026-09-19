# formation-response-kernel, attempt 4 (worker w-macbookpro90c72-j00b3, model grok-4.6)

Plan, locked from the task and block 35's declared objects before using other
attempts' writeups: compute the linear response of `θ_{t+1} = P θ_t + f_t` exactly;
read it in 3D by the eight corner orders of block 09; compare every candidate
channel to `1/E(k)` and to the covariance; decide the decay.

## (1) The statement attempted

Linearized formation law (block 35 / 34): `θ_{t+1} = P θ_t + ξ_t` on the level
plane, `P` the average of the three predecessors `(i,j)`, `(i-1,j)`, `(i,j-1)`,
`φ(k) = (1 + e^{ik_1} + e^{ik_2})/3`, `u = |φ|²`. Persistent source: replace `ξ`
by `ξ + f`. Eight corners `ε ∈ {±1}³` have `φ_ε(q) = (1/3) Σ_j e^{-i ε_j q_j}`.
Comparator kernel `E(q) = Σ_j 2(1 − cos q_j)`, with the 3D embedding
`q = (w + k_1, w + k_2, w)` of a level mode `(k, w)`.

**Statement.**
- (a) The retarded response is `R(k, w) = 1 / (1 − φ(k) e^{iw})` (conventions:
  `θ̂(t+1) = φ θ̂(t) + f̂(t)`, Fourier in the time slot `e^{iwt}`). Static limit
  `w = 0` is `1/(1 − φ(k))`. On every nonzero torus mode of `L = 3, 4` this equals
  the exact resolvent of `I − P`.
- (b) Co-moving: `φ(k) = 1 + i(k_1+k_2)/3 + O(k²)`, drift `(1,1)/3` per level.
  After removing the drift, `1 − u = kᵀ M k + O(k⁴)` with `M = (1/9)[[2,−1],[−1,2]]`,
  eigenvalues `1/9` along `(1,1)` and `1/3` along `(1,−1)`. The static plane kernel
  is an anisotropic 2D Green function (log), not a 3D Coulomb kernel.
- (c) No channel is `c/|x|` in three dimensions.
  - One-corner heat kernel along the body diagonal has occupancy
    `(3n)!/(n!)^3 3^{-3n}`, a `1/n` ray (not isotropic `1/r`).
  - Eight-corner static `R_8(q) = (1/8) Σ_ε 1/(1 − φ_ε(q))` equals `3/2`
    identically on every coordinate axis, and tends to `7/2` along the body
    diagonal. A function finite and nonzero along an axis cannot be `c/|x|`.
  - Along the plane-diagonal `(λ, −λ, 0)`, the `1/λ` terms of opposite corners
    cancel and `R_8 ∼ (3/2)/λ² + 1/2`. That is a *planar* `1/k²` pole, with
    coefficient `3/2` against `1/E ∼ 1/(2λ²)` (coefficient `1/2`), and it is
    absent on the axes, so it is not the isotropic 3D Coulomb pole.
- (d) Fluctuation-response fails: stationary covariance `C_0 = σ²/(1 − u)` is
  not proportional to `R(k, 0) = 1/(1 − φ)` on any `L = 3, 4` torus (the ratio
  takes more than one value on nonzero modes). Time-integrated covariance
  `Σ_{s≥0} C_s = σ² / ((1 − u)(1 − φ))` is `C_0 R`, still not `1/E`.
- (e) The identity `E(q) = 3(|1 − φ e^{iw}|² + 1 − u)` holds identically in the
  embedding `q = (w+k_1, w+k_2, w)`, so `1/E` is a symmetric combination of
  `|R|⁻²` and the plane Green, not `R` itself.

## (2) Steps

**Step 1: response of the linear recursion (PROVED; CHECKED as A1–A3).**
`θ̂(t+1) = φ θ̂(t) + f̂(t)`. Iterate: `θ̂(t) = Σ_{s≥0} φ^s f̂(t−1−s)` (rest at
`−∞`). The retarded kernel in the slot `t` is `φ^t` for `t ≥ 0`. The Fourier
series `Σ_{t≥0} φ^t e^{iwt} = 1/(1 − φ e^{iw})`. Static: `f` constant in time
gives `θ̂ = f̂ / (1 − φ)` on every mode with `φ ≠ 1`. On `L = 3, 4`, every
nonzero mode has `φ ≠ 1`, and `1/(1 − φ(k))` matches `(I − P)⁻¹` applied to that
character. The zero mode is a random walk (block 35 T1) and has no static
response to a net source.

**Step 2: E-identity (PROVED; CHECKED as B1).**
Write `φ = (p_r + i p_i)` with `p_r = (1+cos k_1+cos k_2)/3`,
`p_i = (sin k_1+sin k_2)/3`. Then `|1 − φ e^{iw}|² + 1 − |φ|²` expands to
`2 − (2/3)(cos w + cos(k_1+w) + cos(k_2+w))`, and
`E(w+k_1, w+k_2, w) = 6 − 2(cos(w+k_1)+cos(w+k_2)+cos w)` equals three times
that. So `E = 3(|R|⁻² + 1 − u)` along the formation 3D embedding.

**Step 3: small-k and co-moving (PROVED; CHECKED as C1).**
`φ = 1 + i(k_1+k_2)/3 − (k_1²+k_2²)/6 − i(k_1³+k_2³)/18 + O(k⁴)`. Drift
`(1,1)/3` per level. `u = |φ|² = 1 − kᵀ M k + O(k⁴)` with the stated `M`;
characteristic polynomial `λ² − (4/9)λ + 1/27 = 0`, roots `1/9, 1/3`.

**Step 4: eight-corner symbol (PROVED; CHECKED as D1–D4).**
`R_ε = 3 / (3 − Σ_j e^{-i ε_j q_j})`. On an axis `q = (λ, 0, 0)`,
`R_ε = 3/(1 − e^{-i ε_1 λ})`, independent of `ε_2, ε_3`. The two signs of `ε_1`
sum to `3`, eight corners give `R_8 = 3/2` identically. Body diagonal:
`R_8(λ,λ,λ) → 7/2` as `λ → 0`, series `7/2 − 27 λ²/4 + O(λ³)`. Plane diagonal:
opposite-sign pairs `ε_1 = −ε_2` contribute `O(1/λ)` with opposite signs and
cancel; same-sign pairs contribute `O(1/λ²)`; the series is
`(3/2) λ⁻² + 1/2 + O(λ²)`. Meanwhile `E(λ,−λ,0) = 4(1−cos λ)` so
`1/E ∼ 1/(2λ²)`, coefficient `1/2` not `3/2`, and `E(λ,0,0) ∼ λ²` diverges
while `R_8` stays `3/2`.

**Step 5: FDR and time-integrated covariance (PROVED; CHECKED as E1, E2).**
`C_0(k) = σ²/(1−u)`, `R(k,0) = 1/(1−φ)`. The ratio `C_0 / R` on the nonzero
modes of `L = 4` takes more than one value (it would be constant in equilibrium).
`Σ_{s≥0} C_s = σ² φ^0 / ((1−u)(1−φ))` whenever `|φ| < 1`.

**Step 6: one-corner occupancy along `(n,n,n)` (CHECKED as F1).**
The number of 3-direction walks of length `3n` from the origin to `(n,n,n)` is
`(3n)!/(n!)^3`, each of weight `3^{-3n}`. Exact integers for `n = 1..8`. This is
a ray, not a 3D `1/r` field.

## (3) Where the route stops

No step fails for (a)–(e) of the linear model. The route does not construct a
gravity node, and it does not claim a nonlinear response. The located `1/k²`
pole of `R_8` on `(λ,−λ,0)` is a 2D-style pole of the corner average, not the
comparator's isotropic `1/E`.

## (4) What would finish it

A gravity-lane construction that takes `R` or `R_8` as input and produces an
observable; a proof that the planar pole of `R_8` is (or is not) a Newtonian
potential in the plane `x_3 = 0`; the nonlinear response at finite `β`.

Imports: block 35 T1 (covariance of the free linearized field) is used as the
fluctuation side of (d), and is re-checked on `L = 3, 4`. The eight corners are
the sign patterns of the three predecessor axes (block 09 / 12, as declared).
Stirling's `1/n` reading of the multinomial is not used as a claim.
