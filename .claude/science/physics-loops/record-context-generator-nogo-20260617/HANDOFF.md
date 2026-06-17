# Handoff

Branch: `codex/record-context-generator-nogo-20260617`

This source-side PR adds an exact negative boundary for the Record/pre-record
source gate.

## Movement

- Proves the supplied readout context is load-bearing by exhibiting `Z`, `X`,
  and `Y` projective contexts on the same qubit state with distinct
  probabilities.
- Shows post-record count updates are one-hot realized grammar after
  selection, not probability-vector selection.
- Shows the one-step production vector does not identify the physical kernel,
  generator, or clock/rate.

## Scope Guards

- No audit data edited.
- No publication/status/front-door files edited.
- No main landing.
- No retained/proposed-retained claim.
- No new axiom or measurement primitive.

## Reviewer Notes

The reviewer can extract the science or narrow it further. This worker should
not spend time keeping the PR fresh against main; reviewer/backpressure owns
that.
