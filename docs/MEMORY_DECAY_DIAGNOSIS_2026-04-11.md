# Memory Signal — Geometry and Lattice-Size Dependence

**Primary runner:** scripts/frontier_memory_mu2_size_sweep.py

**Status authority:** independent audit lane only
**Type:** bounded_observation
**Date:** 2026-04-11 (narrowed 2026-05-23 to audit-named claim boundary)

## Claim (narrowed)

The toy runner's measured memory depends strongly on geometry and lattice size.

Concretely, with `scripts/frontier_memory_mu2_size_sweep.py` at its current parameters
(MASS=0.30, GAMMA=0.05, BETA=5.0, PULSE_AMP=1.0):

Relative-geometry slice (posA=N/4, posB=3N/4, source=N/2, marker distance ~N/4):

| N | mu2=0.22 memory | mu2=0 memory |
|---|-----------------|--------------|
| 61 | +0.016780 | +0.020854 |
| 81 | +0.007071 | +0.010084 |
| 101 | +0.002722 | +0.004608 |
| 121 | +0.000865 | +0.001767 |

Fixed-geometry slice (posA=15, posB=45, source=30, marker distance fixed at 15):

| N | mu2=0.22 memory | mu2=0 memory |
|---|-----------------|--------------|
| 61 | +0.016780 | +0.020854 |
| 81 | +0.244260 | +0.231199 |
| 101 | +1.143707 | +1.255389 |
| 121 | +2.599619 | +2.580905 |

Both slices vary by more than an order of magnitude as N changes, and the
two slices disagree sharply for the same N. The measured memory is not a
geometry-invariant or N-invariant quantity at this runner's parameters.

## Audit verdict acknowledgment

The 2026-05-10 audit verdict (`audited_failed`) named the following claim
boundary for this row:

> "this packet supports only that this toy runner's measured memory depends
> strongly on geometry and lattice size, not that Yukawa screening is the
> established root cause."

This note has been narrowed (2026-05-23) to that named claim boundary. The
prior diagnosis framing is retained below as historical context, not as a
load-bearing claim.

## Historical hypothesis (not supported by current runner)

The prior version of this note (2026-04-11) hypothesised that the observed
size-dependence was a Yukawa-screening finite-size artifact, with the
following load-bearing assertions:

- a claimed `exp(-2 mu d)` numerical match across N=41..101,
- a 7-order-of-magnitude memory drop from N=41 to N=101,
- the prediction that the mu=0 (massless) limit would yield N-independent
  memory.

The 2026-05-10 audit verdict found all three contradicted by the current
runner:

1. The N=41 datum is not produced by the current runner (its N_SIZES tuple
   is `(61, 81, 101, 121)`); the historical N=41 number cannot be reproduced
   from this runner.
2. The current runner's relative-geometry slice falls from +0.020854 at
   N=61 to +0.001767 at N=121 in the massless slice — about one order of
   magnitude over that span, not seven.
3. The mu2=0 massless slice is not N-independent (see the +0.020854 → +0.001767
   spread above).

Additionally, the note quoted `screening length = 1/mu approximately 4.5`
treating `0.22` as `mu`, while the runner uses `mu2` with screening length
`1/sqrt(mu2) = 1/sqrt(0.22) approximately 2.13`. The mu vs mu2 convention
mismatch is not reconciled in the historical text.

These assertions are therefore retained only as historical hypothesis and
are not supported by the current runner. The narrowed claim above ("memory
depends strongly on geometry and lattice size") is what the runner does
support.

## What this row may be cited for

- Citing the toy runner's geometry- and N-sensitivity as a reason to treat
  the prior `bounded-retained` memory result as exploratory at this
  runner's parameters.
- As input for future work that registers a proof of the quadratic-Phi
  observable, a single mu vs mu2 convention, and an explicit screening-law
  test on a runner that includes the historical N=41 datum.

## What this row may NOT be cited for

- The `exp(-2 mu d)` Yukawa-screening diagnosis (contradicted by the
  current runner).
- A 7-order-of-magnitude memory drop (not produced by the current runner).
- mu=0 yielding N-independent memory (contradicted by the current
  runner's massless slice).
