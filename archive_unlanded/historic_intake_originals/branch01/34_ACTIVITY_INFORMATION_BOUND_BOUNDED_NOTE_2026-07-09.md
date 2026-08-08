# Activity And Information -- The Necessity Direction Exhibited, Rate-Proportionality Not

**Date:** 2026-07-09
**Type:** bounded measurement (declared comparator)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/activity_information_bound_2026_07_09.py`](../scripts/activity_information_bound_2026_07_09.py)
(TOTAL: BOUND-PARTIAL, exit 1)
**Cache:**
[`logs/runner-cache/activity_information_bound_2026_07_09.txt`](../logs/runner-cache/activity_information_bound_2026_07_09.txt)

## Purpose

The gravity chain's bridge premise reads "local activity is
record-formation opportunity". Its load-bearing direction -- the one
the activity-energy bound (#5079) and the chain actually use -- is
NECESSITY: no activity, no opportunity. This block measures that
direction and probes how much more is true.

## Exhibited (the necessity direction)

- **Stationary control (exact):** on the unkicked ground state, the
  maximum per-step change of any cell's register information and of
  any cell state is at the numerical floor (~1e-15 measured against a
  1e-8 gate). No activity, no information, anywhere, ever.
- **Entropy envelope (theorem layer, zero violations):** every
  per-step information change respects the sharp Fannes-Audenaert
  envelope of the measured cell-state change. Composed with the
  interface data this gives a conditional information-rate envelope --
  stated as such, NOT a linear information bound.
- **Excess register information appears only after kicks and grows
  from exactly zero** (phase kicks leave all occupation distributions
  at their ground-state values at t = 0 by construction; the runner
  verifies this to 1e-17).

## Measured limits (kept as findings, not gated away)

1. **No linear activity gate on pointer FLOW exists.** The pointer
   distribution moves with bond COHERENCE (a current value), while
   activity is state CHANGE (a rate): a steady current through a
   quiet bond moves the pointer with arbitrarily little activity. The
   runner's pointer-continuity gate retains its measured violations as
   the counterexample (27 across the sweep at fitted c1 = 0.27), with
   the interpretation declared in its SPEC-NOTE. Opportunity requires
   activity; pointer transport does not track it linearly.
2. **Opportunity tracks activity only loosely in d = 1**
   (r = 0.63 against the 0.8 gate): the same Markov-blanket geometry
   that blocks redundancy (companion note) makes per-cell attribution
   saturate -- all exterior information about every cell flows through
   the shared boundary channels, so integrated activity at a cell only
   partially predicts the register information written about it.

## What this does to the bridge premise

The premise weakens the same way the sparsity premise did: the
necessity direction ("records can form only where energy acts, because
information reaches no register without activity") is now exhibited
with exact controls; what remains supplied is only the rate
NORMALIZATION -- which is precisely the measured kappa of the
deposition-rate campaign, not an assumption. The proportionality
question is deferred to d >= 2 alongside the redundancy bar.

## Boundaries

Conditional on the QD record reading; d = 1 comparator (N = 12,
Wmax = 4, t <= 10); the early-window and screening-zone attribution
conventions are declared in the runner.

## Changelog

- **2026-07-09.** Three worker versions (gpt-5.6-sol/max), honest
  partials throughout: v1 gates were spec-defective (full-environment
  Holevo degenerate for pure states; linear entropy-vs-trace-norm gate
  ignores the log divergence -- the worker flagged it); v2 corrected
  quantities (r moved -0.42 -> +0.77 early-window); v3 pointer-
  continuity form + screening-zone attribution + g = 0.3
  (r = 0.63, c1 = 0.27). Supervisor: the coherence-vs-activity
  diagnosis of the residual violations, kept as a finding.
