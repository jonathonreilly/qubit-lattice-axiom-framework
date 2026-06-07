# Route Portfolio

## R1: Periodic Kernel Bridge Plus Sign Formula

Status: used.

Use PR #3029's periodic plane-wave density-kernel bridge to put the retained
generation corner pair on the same mediator surface, then prove the exact
second-order sign formula. This directly addresses the audit blocker.

## R2: Unconditional `delta < 0 => K_C3 < 0`

Status: rejected.

The exact denominator shows this is false on the strong-curvature/resonant
branch `eps_gap + delta < 0`. The repair must state the nonresonant branch.

## R3: Physical Magnitude Closure

Status: open.

Would require the actual IR/gap data fixing `eps_gap + delta > 0` on the
realized branch. This block does not solve that.
