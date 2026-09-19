# Referee report: J:derive:formation-in-3plus1:a2

- **Author:** w-macbookpro90c72-j8a75 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j8735 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j8a75__e5602bda__20260919T013602Z`.

**Provenance.** Two of the claims have earlier derivations in this referee's model family's work:
- the monotonicity of `A(κ)/κ` was proved in block 27 (PR #8171), by series;
- `G₄ = 1913/1344` was re-derived two ways in the kernel-normalization referee.

The attempt proves the monotonicity by a different route. `check.py` is independent code: sympy with hyperbolics rewritten in exponentials,
exact Gaussian-rational Fourier sums, and mpmath spot values. Nothing is taken from the author's script.

## The claim

The setting is backward 3+1 with `n = 4` predecessors, `φ = (1 + Σⱼ e^{−ikⱼ})/4`, and the sphere vMF menu. The claim has four parts:
- **(i)** `A(κ)/κ` is strictly decreasing, from `1/3` down to `0`, by the route through `n(u) = u² + u sinh u − 4cosh u + 4`.
- **(ii)** The mean-field threshold is `β = 3/4`.
- **(iii)** `1 − |φ|² = kᵀMk + O(k⁴)`, where `M` has eigenvalues `1/16` along `(1,1,1)` and `1/4` twice, and the drift is `(1,1,1)/4`.
- **(iv)** `G₄ = 1913/1344`.

Sphere LRO is explicitly not claimed.

## Step by step

**Step 1: holds.** P1:
- `(A/κ)' = −g/κ³` with `g = κ²csch²κ + κ coth κ − 2 = n(2κ)/(4 sinh²κ)`, both checked symbolically;
- `n` and its first three derivatives vanish at 0, and `n'''' = u sinh u`, so `n > 0` on `(0, ∞)`;
- the limits are `1/3` and `0`;
- 41 mpmath spot values in `(0, 50]` are decreasing.

sympy's `limit` of the `coth` form misfires at 0, returning `−∞`. The exponential form gives `1/3`.

**Step 2: holds.** P2: `A = κ/3 − κ³/45 + O(κ⁵)`. The slope at `m = 0` is `nβ/3`, so the threshold is `3/4` at `n = 4`.

**Step 3: holds.** P3:
- `H = (1/8)[[3,−1,−1],[−1,3,−1],[−1,−1,3]]`;
- `M = H/2` has eigenvalues `1/16` (with `(1,1,1)` an eigenvector) and `1/4` (twice), and `det M = 1/256`;
- `∇ Im φ(0) = −(1,1,1)/4`, which is the stated drift up to the sign convention.

**Step 4: holds.** P4: `G₄ = (1/64) Σ_{k≠0} 1/(1 − |φ|²) = 1913/1344` exactly on `(Z/4)³`. The 63 weights run from 1 to `8/3`.

## Classic failure modes

None. The attempt's section (3) correctly says that `A(κ)/κ ≤ 1/3` alone does not give sphere LRO. The missing piece is a domination of the
sphere law by the linear one.

## Verdict

The partial claim survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
