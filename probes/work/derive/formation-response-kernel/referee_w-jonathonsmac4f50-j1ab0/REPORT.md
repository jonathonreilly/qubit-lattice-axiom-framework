# Referee report: J:derive:formation-response-kernel:a5

- **Author:** w-macbookpro90c72-jcaf5 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j1ab0 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jcaf5__15ced1c5__20260919T014254Z`.

**Provenance.** This referee's model family refereed attempts a1, a2, a3 and a6 of this problem (all grok). The directed `1/R` of the point
response was checked in those reports. `check.py` here is independent code: sympy, exact rationals and big integers.

## The claim

- The response is `R = 1/(1 − φe^{iw})`, with static limit `χ = 1/(1 − φ)`.
- At `(π, 0)`: `φ = 1/3`, `χ = 3/2`, `C = 9/8` and `1/E = 1/4`. So fluctuation–response fails (`χ/C = 4/3`), and no channel is `1/E`.
- The four in-plane corner orders all give `χ = 3/2` there.
- The truncated `L = 4` sum is `40/27`.
- The equal-level kernel is 2D (logarithmic). The SUMMARY adds "no 1/r in 3D from this 2D level-plane law".

## Step by step

**Step 1: holds.** V1: the geometric series.

**Step 2: holds.** V2: `φ = 1/3`, `χ = 3/2`, `C = 9/8`, `E = 4` and `χ/C = 4/3 = 1 + φ`.

**Step 3: holds as an exact statement.** V3: all four corner `φ`'s equal `1/3` at `(π, 0)`, so each `χ` is `3/2`. One momentum is enough to show
that no channel *equals* `1/E`.

**Step 4: holds.** V3: `(1 − φ⁴)/(1 − φ) = 40/27`.

**The 2D kernel: holds.** V4: the return sum grows by `0.5733` per doubling of `L`.

## Correction: the scope of "no 1/r"

The attempt's section (3) and its SUMMARY use the one-momentum inequality as a no-go for `1/r` *decay*. That does not follow, because decay is
set by small `k`, not by `k = (π, 0)`. The point response in fact has a directed `1/R` along the drift diagonal (V5):
- `T(n,n,n) = (3n)!/(n!³ 27ⁿ)`;
- `n T` is `0.27505`, `0.27560` and `0.27564` at `n = 100, 1000, 3000`, approaching `√3/(2π) = 0.27566`.

The earlier referee reports also recorded planar `1/k²` poles of `R₈`. So the defensible statement is "no *isotropic* `1/r`".

## Verdict

The partial claim survives: the exact numbers, and "no channel equals `1/E`". The correction is to the scope of "no 1/r in 3D".

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
