# The prediction verified — and the checker's finding that the test was easy — Cycle 771

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded worked result (prediction VERIFIED on the landed
surface; verification WEAKENED by the block-additivity finding; no law
claim)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle771_prediction_verification_2026_07_28.py`](../scripts/frontier_cycle771_prediction_verification_2026_07_28.py)
- [`frontier_cycle771_prediction_independent_check_2026_07_28.py`](../scripts/frontier_cycle771_prediction_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 768 left a determinate, unverified prediction: the derived kernel
says the composite channel-pair (0,2) configuration must respond with
rows `((-2,-2,0),(1,1,0),(1,1,0))`. This cycle put the question to the
landed surface directly — and then the checker measured how hard the
question actually was:

- **VERIFIED**: the firewalled direct simulation — two input columns on
  the landed `link_recoil_vertex`, probability-weighted displacement
  bookkeeping over the full branch tensor, no kernel reference anywhere
  in the evaluation path (AST-certified) — returns exactly
  `((-2,-2,0),(1,1,0),(1,1,0))`; every entry diff zero;
- **not pair-specific**: the checker's own census evaluates all three
  channel pairs (0,1), (0,2), (1,2) against the kernel's composition
  with independent arithmetic — **all three match**;
- **the weakening, stated as loudly as the verification**: the checker's
  cross-term probe shows the composite configuration is **exactly
  block-additive** on the landed vertex — branch supports (1,1) with
  overlap 0, no interference anywhere. The composite response is
  therefore the plain sum of the single-channel rows, and a prediction
  that only tests additivity is a weak out-of-sample test;
- **the convention, now named**: the checker's normalized coherent
  superposition of the same two channels produces half-sized rows that
  do NOT match the prediction. The 768 extension probe's composition
  convention — unnormalized column mixture, not coherent superposition —
  is a supplied convention, and the kernel's extension domain is only
  defined relative to it;
- controls: the defining-row calibration reproduces the landed row; a
  perturbed configuration mismatches; determinism; C_source firewall
  declarations verbatim.

**Boundaries, verbatim**: `response_law_established: false`,
`w7_closed: false`, no-refit attachment still open. **The decisive next
experiment is now precise**: find or construct a composite
configuration where the landed vertex produces nonzero interference
cross-terms — the kernel's prediction there is non-trivially
falsifiable in a way this cycle's was not. If no such configuration
exists in the bounded family, that structural fact (a block-diagonal
response sector) is itself the result.

## Supplied / derived / open

### Supplied

- the composition convention (unnormalized column mixture — the 768
  probe's implicit choice, made explicit here); the frozen kernel and
  prediction (extracted as comparator data, never imported); everything
  the Cycle-320/322/749/768 packages declare.

### Derived

- the direct-simulation rows and the exact match; the three-pair
  census; the block-additivity fact (supports (1,1), overlap 0); the
  coherent-variant mismatch; the controls.

### Open

- the interference-sector experiment (the named next cycle); the
  no-refit attachment program; the composition-convention question
  (which composite states are physical inputs); everything inherited.

## Negative-claim discipline

No negative claim ships. The coherent-variant mismatch is a
convention-dependence fact, not a refutation: the prediction was made
and verified under one named convention.

## Verdict

The kernel passed its first out-of-sample test — on every pair, exactly
— and the adversarial checker immediately showed the test was graded on
a curve: zero interference means additivity was never at risk. Both
facts ship together. The kernel is alive, unrefuted, and still
unearned; the interference sector is where it either becomes a law or
dies. Independent audit still required.
