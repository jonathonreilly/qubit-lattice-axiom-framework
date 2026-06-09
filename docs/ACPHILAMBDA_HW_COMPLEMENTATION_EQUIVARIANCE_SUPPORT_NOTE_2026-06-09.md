# AC_phi_lambda Hamming-Complementation Equivariance Support

**Date:** 2026-06-09
**Claim type:** open_gate (finite support theorem; no registry action)
**Type:** open_gate
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_acphilambda_hw_complementation_equivariance_2026_06_09.py`](../scripts/frontier_acphilambda_hw_complementation_equivariance_2026_06_09.py)
(SCORECARD: PASS=8, FAIL=0; cached:
[`logs/runner-cache/frontier_acphilambda_hw_complementation_equivariance_2026_06_09.txt`](../logs/runner-cache/frontier_acphilambda_hw_complementation_equivariance_2026_06_09.txt))

## Boundary

This note records a finite algebraic support result about the Hamming-weight
triplets in the BZ-corner cube. It does **not** reclassify `AC_phi_lambda`, edit
the Tier-A registry, retire an admission, remove bounded status from any
consumer, close the staggered realization gate, select a physical species
reading, derive a readout context, or derive the charged-lepton value.

## Claim

On the Boolean corner cube `{0,1}^3`, complementation `b -> 1-b` maps the
`hw=1` triplet bijectively to the `hw=2` triplet and commutes with the
`C_3[111]` rotation. The two triplets therefore carry the same finite `C_3`
orbit structure. In the standard three-slot circulant bookkeeping, the
assignment of the three slots is invisible to symmetric mass-readout
polynomials: the determinant depends on the phase only through `cos(3 delta)`.

The result is support-only. It says the finite `hw=1` versus `hw=2`
complementation choice is not distinguished by these tested `C_3` and symmetric
circulant invariants. It does not prove that the physical matter sector is
`hw=1`, that the choice is pure convention in the full dynamics, or that any
registry class should change.

## Runner Checks

- `hw=1` and `hw=2` are exchanged by complementation.
- Complementation commutes with the `C_3[111]` rotation on every cube corner.
- Each triplet is a free three-cycle under the rotation.
- The fixed-locus density check gives the same `L_3(1,2)=2/9` arithmetic on the
  complementary triplets.
- The circulant determinant identity
  `e3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta)` is exact.
- The elementary symmetric polynomials are invariant under slot permutation.
- No registry, audit, or effective-status field is read or written.

## What This Does Not Claim

- No Tier-A registry edit or convention-class proposal is made here.
- No consumer is made unbounded by this note.
- No physical-species bridge is derived.
- No `AC_phi_lambda`, `theta`, Record, primitive, or axiom status is changed.
- No audit verdict is applied.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status
authority.
