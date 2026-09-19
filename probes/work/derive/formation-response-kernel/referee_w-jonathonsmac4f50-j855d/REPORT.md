# Referee report: J:derive:formation-response-kernel:a4

- **Author:** w-macbookpro90c72-j00b3 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j855d (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j00b3__13ac7c00__20260919T013214Z`.

**Provenance.** This referee's model family refereed attempts a1, a2, a3, a5 and a6 of this problem (all grok). Three facts were checked there:
- the axis value `R₈ = 3/2`;
- the body-diagonal limit `7/2`;
- the planar pole coefficient `3/2`.

The new items in a4 are the exact expansions. `check.py` is independent: sympy and exact Gaussian rationals. Nothing is taken from the author's
script.

## Step by step

**Step 1 (response): holds.** Q1:
- `1/(1 − φ)` inverts `I − P` on all 15 nonzero modes of `L = 4` (exact Gaussian rationals, including a direct character check);
- it does the same on the 8 nonzero modes of `L = 3` (sympy roots of unity);
- the geometric series gives `R = 1/(1 − φe^{iw})`.

**Step 2 (E-identity): holds.** Q2 checks `E(w+k₁, w+k₂, w) = 3(|1 − φe^{iw}|² + 1 − u)` symbolically.

**Step 3 (small `k`): holds.** Q3:
- `∇φ(0) = i(1,1)/3`, a drift of `(1,1)/3` per level;
- `M = (1/9)[[2,−1],[−1,2]]`, with eigenvalue `1/9` on `(1,1)` and `1/3` on `(1,−1)`.

**Step 4 (eight corners): holds.** Q4:

| slice | `R₈` |
|---|---|
| axis `(λ,0,0)` | `3/2` identically |
| body diagonal `(λ,λ,λ)` | `7/2 − 27λ²/4 + O(λ³)` |
| plane diagonal `(λ,−λ,0)` | `3(3 − cos λ)/(8(1 − cos λ)) = (3/2)λ⁻² + 1/2 + O(λ²)` |

For comparison, `1/E(λ,−λ,0) = 1/(2λ²) + 1/24 + O(λ²)`.

**Step 5 (FDR, time-integrated covariance): holds.** Q5:
- `C₀/R_static` takes 8 distinct values on the nonzero `L = 4` modes;
- `Σ_s C₀φ^s = C₀ R_static`.

**Step 6 (one-corner occupancy): holds.** Q6: the number of walks to `(n,n,n)` is `(3n)!/(n!)³` for `n = 1..8`, by path counting.

**(c) No isotropic `1/r`: holds.** It follows from the axis value, and the attempt correctly separates the planar pole from an isotropic one.

## Verdict

The partial claim survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
