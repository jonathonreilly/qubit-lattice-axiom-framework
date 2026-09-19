# Referee report: J:derive:two-source-interaction:a5

Two grok-4.6 attempts were logged under this task. This report referees both.
- **jef9b:** w-macbookpro90c72-jef9b, log `…__67d01ead__20260919T015109Z`.
- **jc4c2:** w-macbookpro90c72-jc4c2, log `…__dca6a6f5__20260919T015237Z`.

**Referee:** w-jonathonsmac4f50-jf209 (claude-opus-5).

**Disclosure.** This referee's model family refereed attempt a2 of this problem (grok, `referee_w-jonathonsmac4f50-jc66e`). a2 failed
at its two-pin step: the static equal-time marginal stood in for persistent sources. Both a5 attempts repeat a2's `L = 4` values and pin
algebra. `check.py` is independent code:
- exact real-space solves in Fractions;
- sympy for the symbol algebra;
- scipy Bessel quadrature for the lattice Green function.

## jef9b: the kernel's 1/r coefficient — confirmed

**Claim.** The HIT line claims two things:
1. Naive FDR fails: `χ/C = 1 + φ` identically.
2. The linear equal-time kernel is Coulomb with coefficient `7σ²/(8πr)`.

The statement also gives the field-source mean `χ * h ~ (7/(4πr)) h`. The lattice-to-continuum Fourier step is ASSUMED.

**Steps 1–2 hold.** A1 checks with sympy:
- `χ = 7/E`;
- `C = 7σ²/(2E(1−E/14))`;
- `χ/C = (1+φ)/σ²`, which is `12/7` on the `L = 4` mode `(π/2,0,0)`.

The expansion `E = |k|² + O(k⁴)` is standard.

**Step 3 holds, with its ASSUMED item.**
- A4: `C = (7σ²/2)(1/E + 1/(14−E))` exactly. Since `14 − E ∈ [2,14)`, the second part is the transform of a function analytic on the
  torus and decays exponentially.
- So the `1/r` coefficient of `C` is `7σ²/2` times that of the simple-cubic Green function `G`. The attempt's ASSUMED item is exactly
  `G(x) ~ 1/(4π|x|)`.
- I1 (INFO) evaluates `G` numerically. `G(0) = 0.2527310` reproduces Watson's constant over 2. Along the axis:

  | `r` | `r·G(r e₁)` | `r·C(r e₁)/σ²` |
  |---|---|---|
  | 16 | 0.0796561 | 0.2787963 |
  | 32 | 0.0795970 | 0.2785893 |
  | 64 | 0.0795823 | 0.2785382 |

  These approach `1/(4π) = 0.0795775` and `7/(8π) = 0.2785212`.

**Caveats.**
- The coefficient belongs to the kernel `C`, a quantity neighbouring the task's (c). The task asks for the interaction of two persistent
  sources.
- The remark "like pins: interaction `∼ −ab C(r)`, attractive" concerns the equal-time marginal of the unpinned law, not pinned sources.
  This is the a2 finding.

## jc4c2: `L = 4` pin quadratics — fails at its superposition clause

**Claim.**
- The `L = 4` values `C(0) = 18179/15360`, `C(e₁) = 539/15360`, `χ(0) = 10619/7680` and `χ(e₁) = 1799/7680`.
- The Gaussian pin quadratics `1/(C₀−C₁) = 128/147` (unlike) and `7680/9359` (like), with like pins attractive.
- `χ/C = 12/7` on `(π/2,0,0)`.
- "Mass = pin amplitude; superposition of means is exact."

**Numbers hold** (A1, A2, exact).

**The pins are the equal-time Gaussian marginal of the unpinned law.** They are not the task's sources, which are pinned at every level.
This is the same neighbouring statement as a2's step 5.

**"Superposition of means is exact" is false for pins** (A3, exact). The summed one-pin means miss the pin value in both readings of
"pin":

| reading | setup | summed one-pin means at the pin | should be |
|---|---|---|---|
| Gaussian | condition `θ(0) = θ(e₁) = 1` | `1 + C(e₁)/C(0) = 382/371` | 1 |
| persistent | pins on a `5³` box with zero far boundary | `1 + G(e₁)/G(0) = 1.275194` | 1 |

Only the response to field sources, `m = χ * h`, is additive. No step of the attempt proves the clause.

## Verdict

- **jef9b:** confirmed, as a partial on the kernel: the coefficient `7σ²/(8πr)` with its stated ASSUMED item, and the FDR ratio.
- **jc4c2:** fails at its superposition clause. Its numbers hold.

`check.py` prints `HIT: confirmed - ...` for jef9b, and a SUMMARY line recording both verdicts.
