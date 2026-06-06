# Route Portfolio

## Route A: Projective Pointer Write

Status: selected and implemented.

Use the finite pointer projectors from the bounded formation model and define
`W|psi> = sum_r (P_r|psi>) tensor |r>`. Verify `W^dagger W = I`, `K_r = P_r`,
CPTP, selective updates, and repeat-read stability.

Expected outcome: exact-support for a finite model bridge.

## Route B: General Persistent Dynamics To W

Status: rejected for this block.

This would require deriving a normalized record-writing isometry from arbitrary
persistent-record dynamics. Existing source notes explicitly mark that bridge
open.

## Route C: Post-Record Counts To Probability

Status: rejected for this block.

The exact post-record layer consumes realized atoms. It does not select branch
probabilities or production rates.

## Route D: Dial Selection

Status: rejected for this block.

The generation/Koide dial is not selected by the record-write isometry. At
most, separate work can certify stable dial locations under explicit dynamics.

