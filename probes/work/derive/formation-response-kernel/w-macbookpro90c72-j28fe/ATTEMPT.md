# formation-response-kernel, attempt 3 (worker w-macbookpro90c72-j28fe, model grok-4.6)

## (1) The statement attempted

Objects of blocks 26, 34, 35 (PRs #8170, #8178, #8180): linearized sphere formation on the periodic `L × L` level plane,
`θ_{t+1} = P θ_t + ξ_t`, `P` the average over the three predecessors of `(i, j)`, namely `(i, j)`, `(i−1, j)`, `(i, j−1)`
on the level below; modes `φ(k) = (1 + e^{i k_1} + e^{i k_2})/3`, `u = |φ|²`; stationary covariance of nonzero modes
`C_s(k) = σ² φ(k)^s / (1 − u)` (block 35 T1). Comparator kernel `1/E(k)`, `E(k) = Σ_{j=1}^3 2(1 − cos k_j)` on `Z³`.

A persistent source is a mean increment `h` added at every level: `m_{t+1} = P m_t + h` (a pinned site is the same linear
equation for the mean, with `h` the bias that holds the pin). The linear response is the map `h ↦ m`.

**Statement.**
(a) In Fourier-level time with `z = e^{i w}`, the causal generating function of the mode recursion `m_{t+1} = φ m_t + h_t`
from rest is `R(k, w) = 1 / (1 − φ(k) e^{i w})` (equivalently `Σ_{t ≥ 0} φ(k)^t e^{i w t}`); its static limit is
`R(k, 0) = 1 / (1 − φ(k))` on nonzero modes. The zero mode has no stationary response: `m̄_{t} = t h̄`.
(b) In the co-moving frame `y = x − t(1, 1)/3`, the heat kernel is Gaussian with anisotropic covariance from `M` of T2
and amplitude `∼ 1/t`. The static real-space kernel (time-integrated heat kernel) is the 2D convection-diffusion Green
function of `−Δ/6 − (1/3)(∂_1 + ∂_2)`: `(3/π) e^{x_1 + x_2} K_0(√2 |x|)` plus lattice corrections `O(1/|x|)` smaller than
the leading Bessel; downstream along the cone axis this is `∼ 1/√r`, upstream it is exponential.
(c) None of the channels decays like `1/r` in three dimensions: the static response is a 2D wake; the time-integrated
covariance `σ² / ((1 − u)(1 − φ))` is the same 2D object times a real factor; the co-moving heat kernel is `1/t` at the
peak (`t ∼ r²`); the average of `1/(1 − φ_ε)` over the eight corner orders (sign patterns `ε ∈ {±1}³` for the three
predecessor axes) is *not* `1/E(k)` and has no `1/k²` pole (it stays `O(1)` along an axis). The 3D Coulomb kernel is
replaced by a directed 2D convection-diffusion kernel (wake `1/√r` downstream, exponential upstream).
(d) Regression holds: `C_s(k) = C_0(k) φ(k)^s = C_0(k) R_t(k)|_{z^t}`. Equilibrium fluctuation-response fails: the static
susceptibility `1/(1 − φ)` is not a real multiple of the static variance `1/(1 − u)`, because `φ` is not real.

The identity `E(k) = 3(|1 − φ(q) e^{i w}|^2 + 1 − u(q))` in level coordinates `k = (q_1 + w, q_2 + w, w)` holds identically
(so `1/E` is a *symmetrized modulus* of the formation resolvent, not the response itself).

## (2) Steps

On `e^{ik·x}` modes the predecessor average has multiplier `(1 + e^{-ik_1} + e^{-ik_2})/3`; the note's `φ(k) = (1 + e^{ik_1} + e^{ik_2})/3` is the same function of `−k`. Checks F1/F3 use the predecessor sign; the E-identity (F2) uses the note's sign and the matching level map `k = (q + w, w)`.

**Step 1 — generating function (PROVED; CHECKED as F1).** From rest, `m_0 = 0`, `m_{t+1} = φ m_t + h_t`. The z-transform
`G(z) = Σ_{t ≥ 0} m_{t+1} z^t` (response of the updated field) satisfies `G = φ z G + H`, hence `G = H / (1 − φ z)`.
With `z = e^{i w}` this is `R(k, w) = 1 / (1 − φ(k) e^{i w})`. The coefficients are `φ^t`. Static: `z = 1`, `R = 1/(1 − φ)`
for `φ ≠ 1`. Zero mode `φ(0) = 1`: `m̄_{t} = m̄_0 + t h̄`. Checked: geometric sum `Σ_{t=0}^{N-1} φ^t z^t = (1 − (φ z)^N)/(1 − φ z)`
against `R` on every nonzero mode of `L = 4`, `N = 40`; real-space `(I − z P)^{-1}` against the DFT of `R` at `z = 1` and
`z = i` (exact in `Q(i)` for `L = 4`).

**Step 2 — the E-identity (PROVED; CHECKED as F2).** Level coordinates: plane wave `e^{i(q_1 i + q_2 j + w t)}` with
`t = x_1 + x_2 + x_3` and `(i, j) = (x_1, x_2)` is a 3D wave with `k = (q_1 + w, q_2 + w, w)`. Then
`φ(q) e^{i w} = (e^{i k_1} + e^{i k_2} + e^{i k_3})/3`, so `1 − φ e^{i w} = (3 − Σ_j e^{i k_j})/3`, and expanding
`|3 − Σ e^{i k_j}|^2 + 9(1 − u)` recovers `9 E / 3` after the trigonometric reduction (sympy, identically zero).
Thus `1/E` is not `R` and not `C_0`.

**Step 3 — continuum static kernel (PROVED; CHECKED as F3).** `1 − φ(k) = (2 − cos k_1 − cos k_2)/3 − i(sin k_1 + sin k_2)/3
= (k_1² + k_2²)/6 − i(k_1 + k_2)/3 + O(|k|³)`. The symbol is that of `L = −Δ/6 − (1/3)(∂_1 + ∂_2)`. Rescaling
`L = −(1/6)(Δ + 2 b · ∇)` with `b = (1, 1)`, whose Green function on `R²` is `(6 / 2π) e^{b · x} K_0(|b| |x|) =
(3/π) e^{x_1 + x_2} K_0(√2 r)`. Downstream `x = r(1, 1)/√2`: the exponential in `K_0` cancels `e^{b·x}` and leaves
`∼ 1/√r`; upstream it is `e^{−2√2 r}/√r`. Checked on the `L = 32` torus (mean-zero source) along the diagonal and the
anti-diagonal: the ratio of `|m(n, n)| √n` is slowly varying for `4 ≤ n ≤ 12`, while `|m(n, −n)|` drops faster than any
negative power of `n` on that range (numerical, not exact).

**Step 4 — no 1/r channel (PROVED; CHECKED as F4).** (i) The static response lives on the 2D plane and is the kernel of
Step 3, not the 3D lattice Green function. (ii) `Σ_{s ≥ 0} C_s(k) = σ² / ((1 − u)(1 − φ))` has the same complex pole
`1 − φ = 0` as `R`, not the real pole `E = 0`. (iii) Co-moving peak `∼ 1/t` with `t ∼ r²` is `1/r²`, not `1/r`.
(iv) Eight corner orders: `φ_ε(k) = Σ_{j=1}^3 e^{−i ε_j k_j}/3`, `ε ∈ {±1}³`. The average `R_8(k) = (1/8) Σ_ε 1/(1 − φ_ε)`
is real (pairs of opposite cones) and, along an axis, `R_8(κ, 0, 0) → 3/2` as `κ → 0`, while `1/E ∼ 1/κ² → ∞`. So
symmetrization cancels the Coulomb pole rather than restoring it. Checked at four small wavevectors and as a sympy limit
along an axis.

**Step 5 — fluctuation-response (PROVED; CHECKED as F5).** The linear Gaussian recursion gives `Cov(θ_t, θ_{t+s}) = φ^s Var(θ_t)`
(T1), i.e. `C_s = C_0 R_s` mode by mode (regression). Static objects: `1/(1 − φ)` vs `1/(1 − |φ|²)` are equal iff `φ = |φ|²`
or `φ` is real. On `L = 4` the mode `k = (π/2, 0)` has `φ = (1 + i)/3` not real, and the two values differ
(`3/(2 − i)` vs `9/8`). Equilibrium Kubo (`χ = β C`) fails; the directed static susceptibility is not the covariance.

## (3) Where the route stops

The linear model is solved. What is not done: the nonlinear sphere law's response to a pin (block 35 executed the
covariance, not a source); a gravity-lane construction that *takes* this kernel as input; a theorem that the
continuum `K_0` form is the exact lattice asymptotic with a controlled remainder (F3 is a torus diagnostic).
The 8-order average being `O(1)` along an axis is exact in the small-`κ` expansion to order `κ^0`; higher orders are
not needed to kill `1/k²`.

## (4) What would finish it

A lattice saddle / Watson lemma giving `m(n, n) ∼ c / √n` with an explicit `c` matching `3/π` times the Bessel
prefactor, and one nonlinear pin on a large plane. The gravity node still has to say what it does with a 2D wake
instead of `1/r`.
