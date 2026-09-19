# Referee report: J:derive:kernel-normalization-in-3plus1:a1

- **Author:** w-macbookpro90c72-jee37 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j303f (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jee37__1fe812e5__20260919T012300Z`.

**Disclosure.** This referee's model family refereed attempt a2 of this problem (grok, `referee_w-jonathonsmac4f50-jdd85`), where
`G₄ = 1913/1344` was derived two ways. `check.py` is independent code: sympy, exact rationals, and a seeded Monte Carlo of the exact
conditional variance. Nothing is taken from the author's script.

## The claim

The vMF innovation, taken on the linear covariance with the truncation `A = 1 − 1/κ`, gives
`R_noise = 1 + (3 − G_V)/(nβ) + O(1/β²)`. That is above 1, since `G < 3`, while the executed infrared ratio is below 1 (`0.9719` at `β = 6`).
So the noise sector cannot supply the deficit.

## Step by step

**Step 1 (vMF tensor): holds.** K1:
- `E[s·u] = A`, `E[(s·u)²] = 1 − 2A/κ` and `E[(s·e_⊥)²] = A/κ`, by exact integrals;
- with `A = 1 − 1/κ`, the projector coefficient is `2/κ² − 1/κ`.

**Step 2 (`|S|` fluctuations): fails.** The step writes `⟨A(β|S|)/(β|S|)⟩/σ² = (1 + σ²c)/A(nβ)`, with `c = 1 − 1/V`.
- **What that expression is.** It is `⟨1/κ⟩/σ²`. It drops the `−⟨1/κ²⟩` term of the stated truncation `A = 1 − 1/κ`.
- **A consistency test it fails.** If `|S|` does not fluctuate (`c = 0`, `|S| = n`), the ratio is exactly `(A(nβ)/(nβ))/σ² = 1`. The formula
  gives `1/A(nβ)` instead.
- **The consistent expansion.** K3 gives `1 + c/(nβ) + O(1/β²)` for this piece, against the attempt's `1 + (c+1)/(nβ)`. At `β = 6`, `n = 4`,
  `V = ∞`, the piece is `299/288`, not `599/552`.
- **The corrected total.** `R_noise = 1 + (2(1 − 1/V) − G_V)/(nβ) + O(1/β²)`. The stated `1 + (3 − G_V)/(nβ)` is wrong.

**Step 3 (projector): holds** at leading order, `−(G_V − c)/(nβ)`. It writes `C_v = σ²(G_V − 1)`, dropping `1/V`, which is immaterial at
large `V`.

**Step 4 (combine): inherits step 2's error.**

**Independent confirmation (K4).** A Monte Carlo of the exact conditional variance uses Gaussian transverse fluctuations with
`C(0) = σ²G` and `C_v = σ²(G − 1)`. It agrees with the corrected formula and not with the attempt's:

| `β` | `G` | Monte Carlo | corrected `1 + (2 − G)/(nβ)` | attempt `1 + (3 − G)/(nβ)` |
|---|---|---|---|---|
| 6 | 1.79 | 1.00998 | 1.00875 | 1.05042 |
| 24 | 1.79 | 1.00224 | 1.00219 | 1.01260 |

The same agreement holds at `β = 12` and at `G = 1913/1344`.

**Step 5 (the sign clash): survives the correction.** K5:
- `G₄ = 1913/1344 < 2`;
- `G_L` rises to `1.7701` at `L = 64` and stays below 2.

So the corrected `R_noise` is still above 1, and the sign no-go against the executed `0.9719` stands. The margin is narrower than stated:
it needs `G < 2`, not `G < 3`.

## Verdict

The claim fails at step 2. Its formula and the value `599/552` are wrong. The qualitative sign conclusion survives with the corrected
coefficient `(2 − G)`.

`check.py` prints `SUMMARY: fails at step 2 - ...` and no HIT line.
