# no-waves-under-positive-formation, attempt 4 (worker w-macbookpro90c72-j1a93, model grok-4.6)

## (1) The statement attempted

**Hypotheses.** Real scalar records; a linear formation step of gain one with **positive** weights on a finite
predecessor set in earlier levels:
`θ_{t+1}(x) = Σ_{j∈J} w_j θ_{t−τ_j}(x − v_j)`, `w_j > 0`, `τ_j ≥ 0`, `Σ_j w_j = 1`.

**Statement.** (A) *One previous level* (`τ_j = 0` all j): the multiplier is `λ(k) = Σ_j w_j e^{−i k·v_j}`.
Then `|λ(k)| ≤ 1`, with equality iff `k·(v_j − v_0) ∈ 2πZ` for all j. The small-`k` expansion is
`λ(k) = 1 − i μ·k − (1/2) kᵀ Σ k + O(|k|³)`, where `μ = Σ w_j v_j` and `Σ = Σ_j w_j v_j v_jᵀ − μμᵀ`
is positive semidefinite, and positive definite on `R^d` iff the vectors `{v_j}` affinely span `R^d`.
In particular `|λ(k)| = 1 − (1/2) kᵀ Σ k + O(|k|³) < 1` for small `k ≠ 0` whenever Σ ≻ 0: **drift plus
diffusion, never a wave** (`|λ| = 1` and `arg λ = c|k|`). A pure phase `e^{−i k·v}` occurs only if all
`v_j` coincide (no spatial spread): advection, not `ω = c|k|`.
(B) *Several earlier levels.* `z^{T+1} = Σ_{s=0}^{T} a_s(k) z^{T−s}` with each `a_s` a positive combination
of characters and `Σ_s a_s(0) = 1`. Then `z = 1` is a root at `k = 0`; the perturbation of that root is
`z(k) = 1 − i μ·k − D(k) + O(|k|³)` with `D` a PSD quadratic (the same covariance of the space-time
displacements `(v_j, τ_j)` projected orthogonal to the gain-one constraint). So again drift + diffusion.
(C) *Exceptions that WOULD give waves*, and their axiom cost:
- a **negative** weight: excluded by positivity of overlap weights;
- a **complex/unitary** overlap (spinor or U(1) record): costs "the record is real" / the six-axis menu;
- a **conserved oscillation** (a second mode with `|λ|=1` at finite k): requires `|λ|=1` hence aligned
  characters, i.e. a lattice periodicity, not a continuum wave.

## (2) Steps

**Step 1 — one-level multiplier (PROVED).** Fourier mode `e^{i k·x}` is an eigenfunction of a translation-invariant
average of shifts, with eigenvalue `λ(k) = Σ w_j e^{−i k·v_j}`. Triangle inequality in `C` gives `|λ| ≤ Σ w_j = 1`,
equality iff all `e^{−i k·v_j}` coincide.

**Step 2 — expansion (PROVED; CHECKED as D1).** `e^{−iθ} = 1 − iθ − θ²/2 + O(θ³)`. Collecting terms:
constant `1`; linear `−i Σ w_j (k·v_j) = −i μ·k`; quadratic `−(1/2) Σ w_j (k·v_j)² = −(1/2) kᵀ (Σ_j w_j v_j v_jᵀ) k`.
The real part of `λ` is `1 − (1/2) kᵀ (Σ w vvᵀ) k + O(k^4)` (even), the imaginary part `−μ·k + O(k³)` (odd).
`|λ|² = 1 − kᵀ Σ k + O(k^4)` with `Σ = Cov(v)` as above. Checked: NEC `φ(k) = (1+e^{ik_1}+e^{ik_2})/3` against
`μ = (1,1)/3`, `Σ = (1/9)[[2,−1],[−1,2]]` (block 35's `M` is `kᵀ M k = 1−|φ|²` to leading order, and
`1−|φ|² = kᵀ Σ k + O(k^4)`); sympy series to order 4; `Σ` eigenvalues `1/3, 1/9`.

**Step 3 — no `c|k|` phase (PROVED; CHECKED as D2).** `arg λ = −μ·k + O(k³)`, linear in `k`, not in `|k|` unless
`d = 1`. On a grid of 200 small `k ∈ R^2 \ 0`, `|arg φ(k) + μ·k| / |k|³` stays bounded and
`|arg φ(k)| / |k|` is not constant (varies with direction).

**Step 4 — two-level (PROVED; CHECKED as D3).** `z² = a(k) z + b(k)`, `a(0)+b(0)=1`, `a,b` positive character
sums. At `k=0`, `(z−1)(z+b(0))=0`. The root `z=1` perturbs as `∂z = (∂a + ∂b)/(1+b)` at 0; second derivative
gives a PSD quadratic (explicit for `a = p e^{−ik·u}`, `b = q`, `p+q=1`). Checked: the series of the analytic
branch `z_+(k)` with `z_+(0)=1` for `(p,q)=(2/3,1/3)`, `u=e_1`, to order 2.

**Step 5 — exception list (PROVED as a classification under the hypotheses).** Waves with `|λ|=1` for a
cone of small `k` require `Σ = 0`, hence all `v_j` equal: then `λ(k) = e^{−i k·v}`, a drift. Negative `w_j`
can make `|λ|>1` or a pair of unimodular roots (not proved beyond a 1D two-weight example: `w = (2, −1)`
on `{0,1}` has `|λ(π)| = 3`).

## (3) First unclosed step

The multi-level PSD quadratic is stated; the general second-derivative formula is written only for two
levels. Infinite-range (non-finite predecessor set) is outside the hypotheses.

## (4) What would finish it

The general multi-level Hessian, and one explicit negative-weight 1D example that produces a unimodular
oscillatory root (already sketched).
