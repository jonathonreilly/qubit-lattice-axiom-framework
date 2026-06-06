# Route Portfolio

## Route A: Keep Broad Q/Wall Claim

Status: rejected for this PR.

Reason: the audit blocker correctly identifies missing one-hop authorities for
P1, round-1 measure-neutrality, and `det_C`/`det_R` to `r,Q` mappings.

## Route B: Add New Axiom

Status: rejected.

Reason: user direction is to avoid adding axioms, and this packet does not need
one to expose its closed algebraic content.

## Route C: Bounded-Support Algebraic Non-Selection

Status: implemented.

The source note and runner now prove only that fermionic determinant power does
not select the antisymmetric `J` pairing. This preserves the useful science and
removes unsupported downstream conclusions.
