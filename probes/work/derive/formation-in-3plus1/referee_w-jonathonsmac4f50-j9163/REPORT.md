# Referee report: J:derive:formation-in-3plus1:a1

- **Author:** w-macbookpro90c72-j8db3 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j9163 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j8db3__5b9614a9__20260919T013130Z`.

**Provenance.** This referee's model family refereed attempts a2, a3 and a6 of this problem (all grok), which share the Hessian. `check.py`
is written afresh: sympy, exact Gaussian-rational torus sums, and numpy for the return sums. Nothing is taken from the author's script.

## The claim

The setting is linear formation on a `d`-dimensional level plane, with `φ = (1 + Σⱼ e^{ikⱼ})/(d+1)`.
- `1 − |φ|² = kᵀMk + O(k⁴)` with `M` positive definite.
- The zero-mode sum is finite iff `d > 2`. So 3+1 is the lowest dimension with a `1/r` equal-level kernel, and the campaign's `d = 2` is
  logarithmic.
- The drift is `(1,1,1)/4`.

Nonlinear LRO is not claimed.

## Step by step

**Steps 1–2: hold.** L1, for `d = 3`:
- `H = (1/8)[[3,−1,−1],[−1,3,−1],[−1,−1,3]]`, with eigenvalues `1/8, 1/2, 1/2`;
- `kᵀMk = (4|k|² − (1·k)²)/16`, and `4|k|² − (1·k)² = |k|² + Σ_{i<j}(kᵢ − kⱼ)²` symbolically;
- `φ(0) = 1` and `∇φ(0) = i(1,1,1)/4`;
- the one-level kernel's mean displacement is `(1,1,1)/4`.

L2 adds two facts beyond `d = 3`:
- the Hessians are positive definite for every `d = 1..5`;
- on `(Z/4)^d` for `d ≤ 4`, `|φ|² = 1` only at the zero mode.

**Step 3 (integral test): holds.** L3: `∫₀¹ k^{d−3} dk` diverges for `d = 1, 2` and equals 1 for `d = 3`.

**Step 4 (`d = 2`): holds.** L3: the Hessian eigenvalues are `2/9` and `2/3`.

**Numerics (I1, INFO).** The return sum `G_L` behaves as the dichotomy says:

| `d` | `G_L` at `L = 8, 16, 32, 64, 128` | increment per doubling |
|---|---|---|
| 2 | 2.0667, 2.6443, 3.2186, 3.7921, 4.3654 | → `0.5733` |
| 3 | 1.6098, 1.7016, 1.7473, 1.7701 (to `L = 64`) | 0.0918, 0.0457, 0.0228 |

- In `d = 2` the growth is logarithmic. The increment approaches `ln 2/(2π√det M) = 0.5733`, with `det M = 1/27`.
- In `d = 3` the sum levels off. Also `G₄ = 1913/1344`.

**Step 5 (LRO): not claimed**, and the stated obstruction is accurate.

## Verdict

The partial claim survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
