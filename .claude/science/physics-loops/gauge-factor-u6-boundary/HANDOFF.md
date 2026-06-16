# Handoff

## What Changed

This PR repairs the gauge-algebra supplied-carrier row by making the full
`u(6)` boundary explicit.

- The source note now says the positive algebra is the factor-preserving algebra
  of a supplied `C^3 x C^2` carrier.
- The carrier runner now checks:
  - full `u(6)` dimension is 36;
  - factor-preserving algebra dimension is 12;
  - cross-factor `su(3) x su(2)` complement dimension is 24;
  - local plus cross-factor tensors span full `u(6)`.
- The discriminator runner now inherits the same supplied factor-locality /
  `MR_color` boundary.

## What Did Not Change

- No audit verdict was written.
- No ledger row was retagged.
- No generated audit/publication/front-door status surface was committed.
- No new axiom was added.
- No claim is made that `MR_color`, chiral `su(2)_L`, or gauging selection is
  derived.

## Reviewer Focus

Check that the narrowed claim is acceptable as bounded/open-gate source repair:
the exact algebra is useful, but the full positive gauging-selection bridge
remains open.

## Next Action

If this PR passes review, hand it to the independent audit lane for the original
row. Audit should decide whether the row can become a clean bounded/open-gate
boundary or whether it remains conditional pending a separate positive
`MR_color`/gauging-selection bridge.
