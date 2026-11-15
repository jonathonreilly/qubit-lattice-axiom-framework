Reviewer model: claude-opus-5-5

# INDUCT55 — closing the RG induction: (R_m) ⇒ (R_{m+1}), the flow/large-field fixed point, two-sided windows

Worker: Claude Opus 5.5 (model ID above, verbatim from the system prompt). Role: worker (WORK, not review); a Codex
gpt-6-astra/max reviewer checks before anything is banked. Brief: scratchpad queue/induct.md; shared rules
REVIEW_BRIEF_55.md. Writes only this file and checks/in55_*. No git.

## 0. PRE-STATED (written 2026-10-29 06:32 UTC, before any derivation)

Targets (the brief's four jobs):
- T1. A precise induction hypothesis (R_m): every norm, every constant tagged INPUT or OUTPUT, the small-field /
  large-field split, returned activities and failed returns, in DICT55's conventions as corrected by CODEX_REVIEW_DICT.
- T2. A proof (or the precise failure) of (R_m) ⇒ (R_{m+1}) from the per-step package (STEP55), the large-field step
  (LARGE55 / RLARGE v3 R-operation), and the flow step (FLOW55 / UIR55), constants uniform in m, every input named with
  its status (BANKED in PROOF [S26-BANKED] / Codex-confirmed-not-banked / OPEN / candidate).
- T3. The fixed-point argument that removes the flow ↔ remainder circularity, with explicit smallness conditions
  (per-level IVT à la FI-1, or a sequence-space contraction / Brouwer-type argument as in Dimock's QED d=3 papers).
- T4. Every two-sided window whose constants are now outputs, each checked non-empty with exact arithmetic
  (checks/in55_*), or the empty one reported.

What would count as a refutation (of the claim that the induction closes on the inputs on disk):
- R1. A constant that must be chosen before another but whose admissible range depends on that other one
  (a genuine cycle in the constant-choice order) that no fixed-point or monotonicity argument can break.
- R2. An empty two-sided window: an interval [lower, upper] whose lower bound, evaluated with the output constants,
  exceeds its upper bound (exact rational arithmetic), or whose emptiness is forced for all admissible parameters.
- R3. A loss per step that is not summable / not absorbed (e.g. a factor >1 per step on the remainder norm that the
  contraction L^{-α} cannot beat, or a large-field suppression that does not beat entropy uniformly in m).
- R4. An input that the induction needs at strength X while the file on disk supplies only strength < X
  (e.g. a bound proved for real fields used at complex width, or proved at fixed m used uniformly in m).
- R5. A circularity in the cited statuses: an input whose own proof assumes (R_{m+1}) or a later-scale output.
A result of the form "closes conditionally on inputs I_a..I_b" is NOT a refutation; it is reported as a conditional
implication with each I named. An honest NOT-VERIFIED is preferred to a wrong PROVEN.
