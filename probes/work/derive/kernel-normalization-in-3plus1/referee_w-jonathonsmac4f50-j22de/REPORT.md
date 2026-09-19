# Referee report: J:derive:kernel-normalization-in-3plus1:a3

- **Author:** w-macbookpro90c72-j2171 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j22de (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j2171__7a526566__20260919T010938Z`.

**Disclosure.** This referee's model family has already refereed the other two attempts of this problem:
- a1 (`referee_w-jonathonsmac4f50-j303f`) failed at step 2;
- a2 (`referee_w-jonathonsmac4f50-jdd85`) failed at step 3.

The value `G_4(3+1) = 1913/1344` used here was also computed there. `check.py` is independent code, using sympy, Fractions and numpy.
Nothing is taken from the author's script.

## The claim

The claim is partial and concerns the mean map only. Take the cubic truncation of the vMF mean map with `A = 1 − 1/κ` and close it at
Gaussian order on the linear covariance. Then:
- **The multiplier.** The effective one-step multiplier is exactly `K(k) = gφ(k)`, with `g = 1 − 1/(nβ) + σ²(1 − 1/V)`. In infinite volume
  this is `g = 1 − 1/(n²β²) + 2/(nβ(e^{2nβ} − 1))`.
- **The cancellation.** The `O(1/β)` terms cancel, and `G_3` drops out.
- **The consequence.** No `a/β` correction to `R(k)` comes from the mean map. The noise factor is not treated.

## Step by step

**Step 1 (vMF moments): holds.** V1 confirms, symbolically:
- `Z = 4π sinh κ/κ` and `A = coth κ − 1/κ`;
- `E[(s·u)²] = 1 − 2A/κ`, so each transverse component has variance `A/κ`;
- `A = 1 − 1/κ + 2/(e^{2κ} − 1)`.

**Step 2 (A3 form of `1 − |φ|²`): holds.** V2 confirms the six-cosine identity.

**Step 3 (`G_4`): holds.** V3 enumerates exactly and gets `1913/1344`.

**Step 4 (the A3 orbit): holds.** V4 enumerates all 3×3 matrices with entries in `{−1,0,1}`:
- 48 of them have `|det| = 1` and map the signed root set onto itself;
- 4 of those send `e₁` to `e₁ − e₂`, and the attempt's `M` is one of them;
- `f(Mᵀk) = f(k)` holds for all 48 on the `L = 4` and `L = 5` grids.

**Step 5 (tetrahedron Gram matrix, `H = C_v φ`): holds.**
- **Exact, `L = 4`, `σ² = 1`, zero mode removed (V5).**
  - `C(x) = 149/1344` at all six root vectors.
  - `C(0) = 1913/1344` and `C_v = 295/672`.
  - `Γ = (C(0) + 3C₁)/4 = C_v`.
  - `H(k) = C_v φ(k)` holds on all 64 modes over the Gaussian rationals.
- **Floating point.** `H/φ − C_v` is at most `2·10⁻¹⁵` on `L = 5` and `L = 6`.

**Step 6 (cubic jet): holds.** V6 uses four predecessors with random rational two-component `θ` and a sympy series in the scale `ε`:
- the order-`ε` term is `[1 − 1/(nβ)]Pθ`;
- the `β`-free order-`ε³` term is `(Q/2n)Pθ − ½|Pθ|²Pθ`;
- the even orders vanish.

An `O(θ³/β)` part is present. The attempt drops it and says so.

**Step 7 (Wick closure, `K = gφ`): holds.** V7 re-derives it by another route. For a Gaussian field, the Gaussian-closed linear map is
`E[∇F]` (Stein). Exact on `L = 4`, with `β` and `σ²` symbolic, this gives `g = 1 − 1/(nβ) + σ²(63/64)`, which is
`1 − 1/(nβ) + σ²(1 − 1/V)`.

**Step 8 (no `O(1/β)`): holds, and more generally than the attempt claims.** V8 applies the same Gaussian closure to the exact vMF mean map,
with `A` untruncated and all orders in `θ`.
- **Covariance.** Infinite volume, with `G_3 = 1.79288` extrapolated from `64³` and `128³`.
- **Why `K = g_full φ` still holds.** The four predecessors are exchangeable under the A3-symmetric covariance.
- **Monte Carlo of `E[∂F/∂θ]`** (2·10⁶ samples per `β`):

  | `β` | `β(1 − g_full)` | `β²(1 − g_full)` |
  |---|---|---|
  | 6 | `−0.0250` | `−0.15` |
  | 12 | `−0.0077` | `−0.09` |
  | 24 | `−0.0029` | `−0.07` |
  | 48 | `−0.0013` | `−0.06` |

  For comparison, the naive loss of gain without the Hartree term would give `β(1 − g) = 0.25`.
- **Control.** The same samples with the cubic map reproduce the truncation formula to about `10⁻⁴` at every `β`.

So the `O(1/β)` cancellation holds beyond the cubic truncation. The `O(1/β²)` coefficient does not:
- the untruncated map gives about `−0.06`, while the truncation displays `+1/16`, so the sign is opposite;
- the "Goldstone mass" `1 − g² > 0` at finite `β` in step 8 is therefore an artefact of the truncation;
- the attempt's section (3) already says the dropped terms are `O(1/β²)`.

## Verdict

**The claim survives.**
- **What holds.** Within the cubic Gaussian closure, `K = gφ` exactly (by A3 symmetry), with `g = 1 − 1/(nβ) + σ²(1 − 1/V)`. So the
  mean map has no `O(1/β)` correction and `G_3` drops out. Every finite fact re-verifies, and the `O(1/β)` statement also holds for the
  untruncated map.
- **One correction.** The displayed `1 − g = 1/(16β²)` belongs to the truncation only. The full map's `O(1/β²)` coefficient is about `−0.06`.
- **Not derived.** The noise factor, and hence the task's `a`.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
