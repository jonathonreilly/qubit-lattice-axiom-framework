# Referee report: J:derive:plane-memory-loss:a3

- **Author:** w-macbookpro90c72-j17cb (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j8129 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `31f9011d`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (exact rationals, sympy, mpmath). One
numerical side computation is printed as INFO and is not a claim.

## The problem and the claim

The task asks for a proof that the sphere formation law started from an aligned plane has `m_t → 0` on the infinite plane
for every `β` (or on a larger range), or else for the obstruction, naming the failing step of each route. It suggests
three routes:
- (i) a relative-entropy argument with a slowly varying rotation field `θ(x, t)`;
- (ii) comparison with the linear model;
- (iii) invariance plus ergodicity.

The attempt claims partial results. Route (i) "is closed as a no-go", because a twist costs `Θ(T)`. Route (ii) reduces to
an open global `W₁` bound with constant `1/3`. Route (iii) needs mixing uniform in `L`. The attempt also states the
identities `KL = κA(κ)(1 − u·u')`, the z-marginal `W₁ = A(κ)`, the small-field `W₁` rate `1/3`, the mean-field threshold
`β ≤ 1`, and `P_1 … P_4`.

## Step by step

**Step 1 (Langevin bounds): holds, with one mislabelled justification.**
- `A(κ) < κ/3` holds (M1).
- The step says `A(κ)/κ` is decreasing and justifies it by the polynomial `κ² sinh²κ − 3 sinh²κ + 3κ² ≥ 0`. That polynomial
  is `≥ 0` exactly where `A'(κ) ≤ 1/3` (M1, 399 grid points), so it proves a different inequality.
- The monotonicity is true: `κ² + κ sinh κ cosh κ − 2 sinh²κ > 0`, whose `κ^{2m}` coefficient is
  `2^{2m−2}(2m − 4)/(2m)! ≥ 0`.
- The monotonicity is not used later.

**Step 2 (route (i) fails): the identity and the cost of a static twist hold; the no-go does not follow.**
- `KL(vMF(κu) ‖ vMF(κu')) = κA(κ)(1 − u·u')` is correct (M2, by quadrature).
- A twist that is *static in level time*, with gradient `1/L`, costs `O(1)` per level and `Θ(T)` in total, as stated.
- Route (i) in the task uses a *space-time* rotation field `θ(x, t)`. For such fields, the part of the path-space relative
  entropy that is of order `β` is `Σ_t ‖θ_{t+1} − Pθ_t‖²`, the level-time Dirichlet form of the plane walk.
- Subject to `θ(·, 0) = 0` and `θ(x₀, T) = 1`, its minimum is exactly `1/Σ_{k<T} P_k`. This follows from Cauchy–Schwarz
  and is attained by `u_s ∝ (Pᵀ)^{T−1−s} δ`.
- The minimum tends to 0 like `1/(c₀ log T)` by the recurrence of the walk. Exact values are `1, 3/4, 243/400` at
  `T = 1, 2, 4`, and `0.447, 0.355, 0.295` at `T = 16, 64, 256` (M3). `Σ P_k` grows by `0.414` per unit `log T`, against
  `c₀ = 3√3/(4π) = 0.4135`.
- So the mechanism step 2 names, `Θ(T)` from the gradient, is not forced. "A twist of bounded cost … does not exist" is
  shown only for the static twist.

What decides route (i) is a second, order-one part of the relative entropy.
- Rotating the three predecessors by different angles moves `S` at first order through the records' transverse
  fluctuations. This produces a spread term `Σ_t Σ_x Var_{predecessors}(θ_t)` with a `β`-independent coefficient.
- For the linear-optimal twist that term grows with `T`: `0.18`, `0.72`, `1.37` at `T = 8, 32, 64` (INFO M3b, numerical).
- Whether some space-time twist makes both parts small is open. The attempt neither proves nor refutes it.

**Step 3 (one-dimensional `W₁`): holds.**
- The z-marginal `W₁` between the uniform law and `vMF(κe)` is the difference of means `A(κ)`, because the two are
  stochastically ordered (M4).
- The small-field `W₁` rate is exactly `1/3`. The lower half comes from this identity. The upper half needs a coupling:
  the reflection coupling transports `s₁ dσ/(4π)` at cost exactly `1/3`, matched by the test function `s₁` (M4). The
  attempt asserts "exactly" without that half.
- The comparison with block 27's `1/√3` sets a `W₁` constant against a total-variation one, so it compares different
  metrics.

**Step 4 (the `β < 1` reduction): holds as a reduction.** The global inequality `W₁(K_V, K_{V'}) ≤ |V − V'|/3` is
correctly marked ASSUMED and open. The attempt also correctly notes that `W₁` can exceed the distance of the means.

**Step 5 (linear comparison): holds** in the narrow form stated. `P_1 … P_4 = 1/3, 5/27, 31/243, 71/729`, and
`kP_k → 3√3/(4π)` (M5, exact return sums to `k = 255`). The linear variance cannot be a lower bound once it is of order
one, since `|s| = 1`. This shows that one comparison fails, not that route (ii) fails.

**Step 6 (mean field): holds.** `A(3βm) ≤ βm`. For `β > 1` there is a positive fixed point: at `β = 2`, `m = 0.7889`
(M5).

**Step 7 (route (iii)): holds** as a reduction to mixing uniform in `L`.

## Classic failure modes

- *A no-go shown for one instance.* Step 2 costs one twist and concludes about all twists.
- *Mislabelled justification.* Step 1's polynomial proves `A' ≤ 1/3`, not the monotonicity it is cited for.
- *Different metrics compared.* Step 3's `1/3` (`W₁`) against block 27's `1/√3` (total variation).

## Verdict

**First failing step: 2.** The attempt's "route (i) is closed as a no-go" does not follow: its cost argument covers only a
twist that is static in level time. For space-time twists the order-`β` cost has exact minimum `1/Σ_{k<T} P_k → 0`. Whether
the order-one spread part can also be made small, and so whether route (i) works, is open.

The identities and reductions of steps 1 and 3–7 hold and were re-verified independently.

`check.py` prints `SUMMARY: fails at step 2 - ...` and no `HIT: confirmed` line.
