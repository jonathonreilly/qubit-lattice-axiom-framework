# Handoff

## Result

Bounded-support / reversible sink-construction block ready for stacked review.

## Main Finding

Adding explicit sink bits restores reversibility: old fragment memory is moved
to the sink while fragments become a clean pointer broadcast, provided the sink
starts blank.

## Boundaries

- Does not derive sink blankness, thermodynamic cost, physical reset dynamics,
  rates, clock, probabilities, or a dial setting.
- Does not apply audit verdicts.

## Next Exact Action

Open stacked PR against `physics-loop/record-blank-boundary-reset-no-go-20260605`,
then patch this loop pack with the PR URL.
