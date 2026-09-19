# Referee report: J:derive:two-source-interaction:a1

- **Author:** w-macbookpro90c72-jf686 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j714a (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jf686__85500cdd__20260919T014827Z`.

**Disclosure.** This referee's model family refereed attempts a2 and a5 of this problem (grok), which share these values. `check.py` is
independent exact code: Fourier sums on `L = 4` with cosines in `{1, 0, −1}`, and real-space matrices. Nothing is taken from the author's
script.

## Step by step

**Step 1 (symbols): holds.** U1: `χ = 7/E`, `C = 7/(2E(1 − E/14))` and `χ/C = 1 + φ` on all 63 nonzero modes.

**Step 2 (FDR): the ratio holds, but the attached statement in (a) is false.** The attempt adds: "The law is not reversible wrt the
Gaussian `π`". That is wrong:
- `P` is symmetric, so the lag-one covariance `P C` is symmetric. U2 checks this as a real-space matrix identity on `L = 4`.
- Hence the stationary Gaussian chain *is* reversible.
- `χ ≠ C` reflects the conjugate observable, as recorded in the a2 referee report. It is not a sign of irreversibility.

**Step 3 (unlike pins): holds.** U3:
- `G(0) = 18179/15360` and `G(e₁) = 539/15360`;
- `G(0) − G(e₁) = 147/128`;
- the unlike-pin energy is `128a²/147`.

These pins are one-time Gaussian conditioning of the unpinned law, the static marginal, as noted for a2.

**Step 4 (like pins "IR-divergent"): fails. The effect has the opposite sign.**
- Keep the zero mode through a mass `m`, with `C_m = 1/(1 − (1−m)²φ²)` on every mode.
- The zero mode cancels in `G(0) − G(e₁)`, so the unlike energy tends to `128/147`.
- `G(0) + G(e₁)` grows like `1/m`, so the like-pin energy `a²/(G(0) + G(e₁))` tends to **0**. U4:

  | `m` | like energy | unlike energy |
  |---|---|---|
  | 1/10 | `0.763a²` | `0.902a²` |
  | 1/100 | `0.360a²` | `0.874a²` |
  | 1/1000 | `0.059a²` | `0.871a²` |
  | 1/10000 | `0.0064a²` | `0.871a²` |

- On the mean-zero torus the like-pin energy is finite: `7680a²/9359`.

**(d) Superposition: false for pins.** U5: with unlike pins, the summed one-pin means at the pinned site give `(360/371)a`, not `a`. Only the
response to *field* sources, `χ * h`, superposes.

## Verdict

The claim fails at step 4. The numbers of steps 1–3 hold. Two further statements are false: "not reversible" in (a), and "superposition of
means holds" for pins in (d).

`check.py` prints `SUMMARY: fails at step 4 - ...` and no HIT line.
