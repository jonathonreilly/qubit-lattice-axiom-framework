# Referee report: J:derive:corrigendum-PR8180:a2

- **Author:** `w-jonathonsmac4f50-jb8bf` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-j05ea` (`grok-4.6`). Different model family.
- **Checks:** the mode multipliers, the mode counts, the Laplacian identity, the propagator algebra, and two mixed derivatives. The author's script is not called.

## The statement

With modes `θ̂_k = L^{-1} Σ e^{-ik·x} θ_x` and `Cov(X, Y) = E[X conj(Y)]`, `P` multiplies `e^{ik·x}` by `conj(φ)` and `Pᵀ` by `φ`. The mode therefore advances by `conj(φ)`, while the covariance display `φ^s Var` is the one that matches this pairing. The comparator and the formation kernel share the phase `conj(φ)^τ` and differ by their decay rates.

## Steps

**S1–S3.** `(Pe_k)/e_k = (1 + e^{-ik_1} + e^{-ik_2})/3 = conj(φ)`, and `Pᵀ` gives `φ`. Then `E[θ̂ conj(conj(φ)^s θ̂)] = φ^s |θ̂|^2`. On `L = 3`, `φ^s` is real for 8 of 24 pairs and `φ` itself is non-real on 6 of 8 modes. On `L = 4` the counts are 19 of 45 and 10 of 15.

**S4–S6.** `P(Pᵀ)e_k = |φ|^2 e_k`, so the variance is the geometric sum. The stationary eigenvalue on `e_k` is `σ² φ^s/(1 − u)`.

**S7.** `E(K) = Σ_a |1 − e^{iK_a}|^2` equals `3|1 − φ e^{iw}|^2 + 3(1 − u)`. The test quantity `f² ∂² log f` is `−2` for the comparator at `(π/2, π/3, π/6)`, and `−5√3/9 − 2/3` for `1/S_F` at `(π/3, π/6, π/2)`.

**S8–S9.** The small root is `z = conj(φ)/(1 + y)`, with `|z|^2 = (1 − y)/(1 + y)`. `Ĝ/Ĉ = y/(6σ²(1 + y)^τ)`. The rates are `artanh y = y + y³/3 + …` and `−½ log(1 − y²) = y²/2 + y⁴/4 + O(y⁶)`. The quadratic form is `kᵀ M k` with `M = (1/9)[[2, −1], [−1, 2]]`.

The line-by-line census of the other notes was not repeated.

## Verdict

The corrected identities survive. The display `φ^s Var` matches the declared pairing; the evolution multiplier is `conj(φ)`. The two kernels share that phase and are separated by the order of the decay.
