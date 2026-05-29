# Koide Order-One Circulant Diagnostic

**Date:** 2026-05-29
**Claim type:** bounded_theorem
**Status:** bounded route diagnostic. This note does not approve the
Connes-Lott product triple, order-one as a repo primitive, or any new
framework axiom. It sets no audit verdict.
**Primary runner:** `scripts/frontier_koide_order_one_circulant_diagnostic_2026_05_29.py`
with cache
`logs/runner-cache/frontier_koide_order_one_circulant_diagnostic_2026_05_29.txt`.

## Question

Does imposing the NCG order-one condition on the C_3-circulant generation
algebra select the charged-lepton Koide ratio `Q=2/3`, equivalently
`r=|b|^2/a^2=1/2`, for a what-if Connes-Lott/product-grading mass operator?

## Result

No, in this bounded setting. For the C_3-circulant generation algebra,
the mass operator `M = a I + b R + c R^2` commutes with every algebra
element `A = alpha I + beta R + gamma R^2`. Therefore the inner commutator
in the order-one expression vanishes identically before the real structure
or grading enters:

`[D, pi(A)] = 0`.

The order-one condition then reads `0=0` for every `a,b,c`. The runner also
checks explicit distinct ratios `r in {0.05, 0.2, 0.5, 1, 2, 5}`; all satisfy
the condition in the same C_3-circulant setup. This proves non-selection for
this route: order-one, on this algebra, does not choose `r=1/2`.

## Boundary

This is not a global no-go on NCG, product triples, or all possible
order-one constructions. It is a route diagnostic for the natural
C_3-circulant generation algebra. The existing repo order-one surfaces
remain open-gate / conditional where they already were; this note does not
change that status.

## Relation to Koide

The retained Koide algebraic surfaces still locate the observed value at the
`C_3` character-norm split. This diagnostic only says that the C_3-circulant
order-one condition is not the missing selector for that split.
