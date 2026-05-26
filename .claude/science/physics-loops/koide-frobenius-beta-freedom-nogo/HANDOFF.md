# Handoff

This branch repairs `koide_frobenius_isotype_split_uniqueness_note_2026-04-21`
by replacing a conditional AM-GM packet with a finite no-go for the missing
normalization bridge.

## What It Fully Supports

- `B_{alpha,beta}` diagonalizes on scalar/traceless isotypes with weights
  `alpha + 3 beta` and `alpha`.
- Positive-definiteness requires `alpha > 0` and `alpha + 3 beta > 0`.
- `alpha = beta = 1` is positive definite, Ad-invariant on the tested pair,
  and differs from Frobenius on a trace-bearing matrix.
- Therefore the listed linear-algebra premises do not force `beta = 0`.

## What Remains Open

- A framework authority fixing `w_scalar / w_traceless = 1`.
- A physical charged-lepton Koide derivation.

## Reviewer Notes

The branch does not add axioms and does not apply an audit verdict. The audit
pipeline queues the row for independent review as `no_go`, `unaudited`,
`ready=true`, with no open dependency paths.
