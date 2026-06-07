# Handoff

## What changed

This branch adds an I4 bridge proving strict all-weight positivity of the
one-link Wilson character coefficients and formalizing the all-weight
convolution object as a central character distribution on finite-character
tests.

The parent plaquette all-weight note now cites that bridge and no longer
presents the boundary object as an unqualified `L2` class function/operator
closure. The parent runner checks the bridge note, runner, and cache inline.

## Why it matters

The latest audit blocker on the plaquette all-weight row was dependency
scope, not arithmetic. This PR supplies the missing source-side theorem packet
needed to re-audit that row without importing coefficient nonvanishing or
formal-series authority.

## Remaining blockers

Independent review/audit must certify I4. A separate decay theorem would be
needed for any L2/bounded-operator upgrade. A separate computation/proof is
still needed for the parent beta=6 Perron residual data.

## Exact next action

Run review-loop/audit on this branch. If I4 is accepted, re-audit the parent
all-weight row against the now-explicit bridge packet.
