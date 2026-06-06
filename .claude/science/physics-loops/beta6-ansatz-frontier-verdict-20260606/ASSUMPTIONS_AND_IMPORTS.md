# Assumptions And Imports

Allowed current-surface inputs:

- `P_1plaq(beta)` from the retained single-plaquette recurrence used by the
  existing harness.
- Exact connected coefficients `d_5..d_11` as exposed by the current beta6
  coefficient packets on main.
- `0.594` / `0.5934` only as a Monte-Carlo comparator, never as a fitted or
  load-bearing proof input.

Open imports and boundaries:

- Independent audit of the coefficient packets remains separate.
- Padé and d-log-Padé are methodology/diagnostic tools here, not a proof of
  the true analytic continuation.
- No new axiom, carrier convention, or physical beta=6 value theorem is added.
