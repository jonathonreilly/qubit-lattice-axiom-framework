# Handoff

## Current Status

Stacked branch:

```text
physics-loop/kz-beta6-reproduction-contract-20260606
```

Intended base:

```text
physics-loop/kz-su3-beta6-convention-split-20260606
```

PR for this block:

```text
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2812
```

GitHub verification: open PR, base
`physics-loop/kz-su3-beta6-convention-split-20260606`, head
`physics-loop/kz-beta6-reproduction-contract-20260606`, mergeable
`MERGEABLE`, merge state `CLEAN` at latest verification.

## Result

This block proves a support-only SDP firewall for the K-Z beta=6 route.
The endpoint assignment `P=R=Q=1`, with all listed moments and
cross-correlators equal to `1`, satisfies the support, Hankel, Hausdorff,
Wilson-loop Gram, area-style, and lower-bound constraints in scope. Therefore
those constraints cannot be accepted as a finite `SU(3)`, Wilson `beta=6`
reproduction.

## Remaining Blocker

The K-Z external-lift route still needs a primary source-data/table bracket at
paper coordinate `lambda=1.5`, or a repo-owned beta-coupled SDP reproduction
with explicit loop equations and solver/cutoff evidence.

## Next Action

Continue the 12-hour campaign on the next highest-value lane.
