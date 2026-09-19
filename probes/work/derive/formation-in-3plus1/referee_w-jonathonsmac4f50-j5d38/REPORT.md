# Referee report: J:derive:formation-in-3plus1:a4

- **Author:** w-macbookpro90c72-j5855 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j5d38 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j5855__9fbddbe5__20260919T013644Z`.

**Disclosure.** This referee's model family has already refereed four attempts of this problem, all by grok authors:

| Attempt | Referee directory |
|---|---|
| a1 | `referee_w-jonathonsmac4f50-j9163` |
| a2 | `referee_w-jonathonsmac4f50-j8735` |
| a3 | `referee_w-jonathonsmac4f50-jff50` |
| a6 | `referee_w-jonathonsmac4f50-j223e` |

The a3 referee confirmed `det M = 1/256` and the `4/π` prefactor as a continuum statement. `check.py` here is independent code, using sympy
and numpy FFT. Nothing is taken from the author's script.

## The claim

The claim is linear only. For the linearized formation law on `Z^{d+1}`, `φ_d = (1 + Σ_{j≤d} e^{ik_j})/(d+1)`:

1. **Small `k`.** `1 − u = kᵀM_d k + O(k⁴)` with `M_d = ((d+1)I − J)/(d+1)² ≻ 0`.
2. **The dichotomy.** `u = 1` only at `k = 0`. `∫ 1/(1−u)` is finite iff `d > 2`, so `3+1` is the lowest dimension with a finite
   equal-level variance and a `1/r` kernel.
3. **At `d = 3`.**
   - `M` has eigenvalues `1/16` and `1/4` (twice), and `det M = 1/256`.
   - The continuum Green function is `4/(π√(xᵀM⁻¹x))`.
   - The drift is `(1,1,1)/4`.
4. **The causal response.** It is the four-direction multinomial `(4n)!/(n!)⁴`, which is not the covariance.

Sphere LRO and bounds on the nonlinear `S(k)` are explicitly not claimed.

## Step by step

**Step 1 (`u = 1` only at 0): holds.** The triangle-inequality argument is complete, because the term `1` fixes the phase. V2 confirms it:
- exactly on `(2π/4)Zᵈ`, over the Gaussian rationals, for `d = 1..4`;
- in floating point on `(2π/n)Zᵈ` for `n = 5..9` and `d = 1..3`, where `max u` away from 0 is `0.912`.

**Step 2 (Hessian): holds for `d = 3` and for `M_d ≻ 0`, with a wrong general-`d` display.**
- V1 derives `M_d` as the covariance of the step law, uniform on `{0, e₁..e_d}`. It matches an exact multivariate Taylor expansion of
  `1 − |φ_d|²` for `d = 1..5`, with no cubic term.
- The eigenvalues are `1/(d+1)²` along `(1..1)` and `1/(d+1)` on its complement.
- At `d = 3`: `det = 1/256`, eigenvalues `1/16` and `1/4` (twice).

**Correction.** ATTEMPT.md's general-`d` display is half the true form, and V1 finds the ratio exactly 2 for every `d = 1..5`:
- the display: `(d/(2(d+1)²))|k|² − (1/(d+1)²) Σ_{i<j} k_i k_j`;
- the true form: `(d/(d+1)²)|k|² − (2/(d+1)²) Σ_{i<j} k_i k_j`.

The text also guesses "`(d+2)/2` once along `(1..1)?`". The form `(d/2)Σk² − Σ_{i<j}k_ik_j` has eigenvalue `1/2` there. The attempt's own
check A3 and its HIT line carry the correct `M_d`, so nothing downstream uses the wrong display.

**Step 3 (integrability iff `d > 2`): holds.** The power counting plus compactness argument is complete. V3 runs torus sums
`G_L = L⁻ᵈ Σ_{k≠0} 1/(1−u)` for `L = 8..128`:

| `d` | Behaviour | Numbers |
|---|---|---|
| 1 | grows like `L` | `21.3 → 42.7` |
| 2 | grows like `log L` | increment per doubling `0.5776, 0.5743, 0.5735, 0.5733` |
| 3 | settles | increments halve: `0.092, 0.046, 0.023, 0.011`, towards `≈ 1.79` |

For `d = 2` the predicted increment per doubling is `log 2/(2π√(det M₂)) = 3√3 log 2/(2π) = 0.5732`, with `det M₂ = 1/27`.

**Step 4 (the `1/r` kernel): holds, and V4 checks it on the lattice, which the attempt did not.** The attempt computes only the continuum
transform of `1/(kᵀMk)` (`1/(4π√det M) = 4/π`). V4 checks that the lattice kernel matches it:
- **Method.** An FFT of `1/(1−u)` on the `256³` torus, zero mode removed. Differences `G(x) − G(2x)` cancel the constant torus offset, so
  the tested quantity is `(G(x) − G(2x))·2√(xᵀM⁻¹x)`.
- **Across the cone axis** (`(1,−1,0)` and `(1,0,0)`): `1.2823`, `1.2750`, `1.2732` at `x = 3, 5, 8` times the direction.
- **Along it** (`(1,1,1)`): `1.2744`, `1.2714`, `1.2633`. Against `4/π = 1.2732`, the `(1,1,1)` values drift slightly with `|x|`. That is
  the torus images, since at `L = 160` the same point gave `1.2313`.
- **Anisotropy.** At equal distance the kernel across the axis is twice the kernel along it. This follows from `M⁻¹ = 4(I + J)`, with
  eigenvalue 16 along `(1,1,1)` and 4 across it.

**Step 5 (drift, multinomial cone): holds.**
- V5 gives `∇φ(0) = (i/4, i/4, i/4)`.
- A dynamic-programming count of step sequences reaching `(n,n,n,n)` in `Z⁴` gives `24, 2520, 369600, 63063000, 11732745024,
  2308743493056` for `n = 1..6`. That equals `(4n)!/(n!)⁴`.

**Step 6 (LRO): not attempted.** The attempt says so and makes no claim.

## Verdict

**The linear partial survives:**
- the dichotomy at `d > 2`;
- `M_d = ((d+1)I − J)/(d+1)²`;
- `det M = 1/256`;
- the `4/π` prefactor, now also on the lattice;
- the drift `(1,1,1)/4`;
- the multinomial cone.

One correction: step 2's general-`d` display is off by a factor 2, and its eigenvalue guess is wrong. The HIT line is right. What is not
covered is the nonlinear part of the task: LRO for the sphere (a), and two-sided bounds on the nonlinear `S(k)` (b).

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
