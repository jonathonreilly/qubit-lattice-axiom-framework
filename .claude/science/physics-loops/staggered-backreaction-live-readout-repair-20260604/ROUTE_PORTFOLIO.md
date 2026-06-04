# Route Portfolio

## Route A: Stable Bound Display

Status: executed.

Print the certified `two-body max < 1e-12` bound in the runner's SAFE READ and
mirror that in the source note.

## Route B: Pin Raw Roundoff Digits

Status: rejected.

The raw residual can vary at roundoff level across fresh executions while
remaining far below the asserted tolerance. Pinning one raw value would create
another stale-display hazard.
