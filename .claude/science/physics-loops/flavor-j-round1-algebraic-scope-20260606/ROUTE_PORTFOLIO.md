# Route Portfolio

## Route A: Keep Broad Q/First-Order Claim

Status: rejected for this PR.

Reason: the audit blocker identifies missing one-hop authority for the `Q`
default/readout steps, and this packet does not derive a first-order action.

## Route B: Add New Axiom

Status: rejected.

Reason: user direction is to avoid new axioms, and no new axiom is needed to
expose the finite obstruction.

## Route C: Bounded-Support Static-J No-Go

Status: implemented.

The note and runner now close only the static-`J_cs` non-selection result and
the false `Gamma_chi = J_cs` identity route.
