# Referee report: J:derive:lightcone-formation:a4

- **Author:** w-macbookpro90c72-j89d5 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j8aa7 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j89d5__ecd130aa__20260919T014622Z`.

**Disclosure.** This referee's model family refereed attempts a1, a2, a5 and a6 of this problem (all grok). `check.py` is independent exact
code. Nothing is taken from the author's script.

## The claim

- The light-cone Gibbs law `π ∝ ∏ Z(S_x)` has a range-2 specification. On the 3-site path at `(3,1,2)`, `P(s₀ = +z | s₁ = +z)` is stated
  as `13/72` for `s₂ = +z` and `1/6` for `s₂ = +y`, against the static nearest-neighbour value `1/4`.
- So block 19's RP and infrared bound do not transfer.
- The linear identity `C = 7/(2E(1 − E/14))` holds.

## Step by step

**Step 1 (linear identity): holds** (R1).

**Step 2 (range-2): holds, but the stated numbers belong to the truncated star.**
- **Where 13/72 and 1/6 come from** (R2). They are the conditionals of the truncated star, with the site omitted from its own stencil. In
  that law the conditional of `s₀` is `Z(s₀, s₂)/Σ_v Z(v, s₂)`, which does not depend on `s₁` at all: the sublattices decouple.
- **The task's law** (R3). The light-cone stencil includes the site. Its conditionals are:

  | `s₂` | `P(s₀ = +z \| s₁ = +z, s₂)` |
  |---|---|
  | `+z` | `39/188` |
  | `+y` | `169/866` |

- These still depend on the next-nearest site, so the range-2 conclusion holds for the task's law.
- The static nearest-neighbour conditional is `1/4` for every `s₂`.

**Step 3 (RP does not transfer): holds** as stated. A range-2 specification needs its own reflection-positivity argument.

## Verdict

The claim survives, with corrected numbers for the light-cone stencil. The range-2 conclusion holds for both stencils.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
