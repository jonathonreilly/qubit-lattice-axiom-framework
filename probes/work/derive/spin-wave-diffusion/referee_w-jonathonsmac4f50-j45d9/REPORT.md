# Referee report: J:derive:spin-wave-diffusion:a4

- **Author:** w-macbookpro90c72-j9a21 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j45d9 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `8c343f43`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (exact rationals, sympy).

## The claim

The attempt claims an exact partial result:
- `1 − |φ|² = (6 − 2cos k₁ − 2cos k₂ − 2cos(k₁ − k₂))/9`;
- the return sums `G_2 = 27/32`, `G_3 = 11/9` and `G_4 = 189/128`;
- the linearized zero mode has `φ(0) = 1` and variance `σ²t/N` per component, so `D₁L²/σ² = 1` for the linear law.

The nonlinear statement is explicitly not claimed.

## Step by step

**Step 1 (cosine identity): holds.** It holds identically (S1, sympy).

**Step 2 (`G_L`): holds.** Each value was computed two independent ways (S2): the Fourier sum with exact rational cosines,
and the site variance of the stationary centred linear field, solved in real space as a translation-invariant Lyapunov
equation. The two agree:

| L | Fourier | real space |
|---|---|---|
| 2 | `27/32` | `27/32` |
| 3 | `11/9` | `11/9` |
| 4 | `189/128` | `189/128` |

**Step 3 (zero mode): holds.**
- `P` is doubly stochastic on the `L = 3` torus.
- The exact covariance recursion `Σ_{t+1} = PΣ_tPᵀ + I`, started from `θ₀ = 0`, gives plane-average variance `t/N` per
  component at `t = 1, …, 6` (S3).
- So the linear zero mode diffuses at `σ²/N` per level.

## Classic failure modes

None. The scope is stated precisely: the linear law and the exact return sums. The remark in section (3) about the nonlinear
limit is flagged there as not proved.

## Verdict

The exact partial result survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
