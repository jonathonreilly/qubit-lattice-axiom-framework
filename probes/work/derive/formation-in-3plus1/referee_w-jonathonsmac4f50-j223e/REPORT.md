# Referee report: J:derive:formation-in-3plus1:a6

- **Author:** w-macbookpro90c72-j30e1 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j223e (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j30e1__59181689__20260919T013419Z`.

**Provenance.** This referee's model family refereed attempts a2 and a3 of this problem (grok). This attempt shares their mean-field threshold
and Hessian. `check.py` is written afresh, with sympy using exponential rewrites and mpmath. Nothing is taken from the author's script.

## The claim

- **(1) Mean-field threshold.** The four-predecessor mean-field map `m ↦ A(4β|m|)` sends every orbit to 0 iff `β ≤ 3/4`. Its slope at 0 is
  `4β/3`. The 2+1 threshold is `β = 1`.
- **(2) Linear envelope.** The Hessian of `1 − |φ|²` at 0 has eigenvalues `1/8` and `1/2` (twice). So, to leading order,
  `4σ²/|k|² ≤ S(k) ≤ 16σ²/|k|²`.
- **Stated limit.** Nonlinear LRO is not proved.

## Step by step

**Step 1 (`A(κ)/κ < 1/3`): holds.** Q1:
- `A < κ/3` is equivalent to `u = (κ²+3) sinh κ − 3κ cosh κ > 0`, as a sympy identity after multiplying by `3κ sinh κ > 0`;
- `u(0) = 0`, `u' = κ(κ cosh κ − sinh κ)`, and `(κ cosh κ − sinh κ)' = κ sinh κ > 0`.

**Step 2 (threshold `3/4`): holds.**
- **The argument.** `f(m) < (4β/3)m`, so for `β ≤ 3/4` every orbit decreases to the only fixed point, 0. For `β > 3/4` the slope at 0
  exceeds 1 and `f(1) = A(4β) < 1`, so a positive fixed point exists.
- **Numerics (Q2).** Orbits from `m₀ = 1`:

  | `β` | behaviour |
  |---|---|
  | 0.70 | decreases to 0 |
  | 0.75 | decreases towards 0 (`m₄₀₀₀ = 0.0144`) |
  | 0.80 | converges to the fixed point `0.316988` |
  | 1.00 | converges to the fixed point `0.599839` |

**Step 3 (Hessian envelope): holds.** Q3:
- the Hessian eigenvalues are `{1/8, 1/2, 1/2}`, with `1/8` along `(1,1,1)`;
- `|k|² S/σ²` at `|k| = 10⁻⁴` is `16.0000000` along `(1,1,1)` and `4.0000000` along `(1,−1,0)`, so both ends of the envelope are attained.

**Step 4 (nonlinear LRO): stated as open.** The attempt's reason is the sign of the triangle inequality. That is a comment on where the route
stops, not a claim.

## Verdict

The partial claim survives with no failing step. It overlaps attempt a2, whose threshold and Hessian were confirmed in #8389.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
