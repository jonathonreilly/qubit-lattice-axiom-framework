# Handoff

This PR repairs the source boundary for the DM leptogenesis PMNS transport
interval row.

What changed:

- The parent note now states that the exact `eta/eta_obs = 1` interpolation
  point is an intermediate-value diagnostic, not a selected physical source.
- A companion selector-firewall note proves that the crossing root is
  target-defined unless an independent selector theorem supplies the endpoint
  or `lambda_*`.
- The registered parent runner now checks that the source cites and preserves
  this firewall.

Reviewer focus:

- Check that the repair is not too narrow: it preserves the interval witness,
  the overshoot endpoint, and the reproducible root.
- Check that no audit status is claimed.
- If accepted, the audit lane can decide whether the parent row should move
  from numerical-match classification to bounded interval support plus
  selector firewall.

Exact next action: run review-loop on this branch.
