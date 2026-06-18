# Handoff

## What Moved

The theta mass-side epsilon-Hermiticity runner now directly covers:

- three U(1) seeded backgrounds;
- two SU(2) seeded backgrounds;
- two SU(3) seeded backgrounds.

The note now reports 21 site-diagonal background x parameter combinations and
representative one-link checks across U(1), SU(2), and SU(3). The runner uses
normalized determinant phase/sign evidence for large matrices, so the SU(3)
checks avoid raw determinant overflow warnings.

## What Did Not Move

- K-reality is still consumed, not derived.
- The orientation bit remains open.
- Gauge-side theta_gauge is untouched.
- Beyond-bilinear matter terms remain open.
- No audit result, ledger row, queue entry, publication matrix, or front-door
  status was changed.

## Exact Next Action

Reviewer should inspect the source-side PR, decide whether to extract the
science, and handle any review-loop or landing work.
