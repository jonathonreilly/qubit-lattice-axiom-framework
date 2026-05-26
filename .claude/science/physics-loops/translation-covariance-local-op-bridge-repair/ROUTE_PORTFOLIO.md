# Route Portfolio

## Route A - Narrow To Retained Tensor-Product Surface

Status: selected and implemented.

The audit blocker asked for either a retained bridge supplying the
regular representation or a narrowed claim. The retained
tensor-product bridge supplies the finite Fock-space representation for
factor permutations, so the repair narrows to exactly that surface.

## Route B - Preserve Full H_phys Scope

Status: rejected for this block.

The repo does not currently expose a retained all-`H_phys`
one-site-translation regular-representation theorem. Preserving that
scope would reintroduce the audited overclaim.

## Route C - Two-Step Noether-Only Narrowing

Status: not used.

A two-step Noether-only version would be weaker and less useful for the
tensor-product tight-binding descendants now unlocked by the retained
bridge.
