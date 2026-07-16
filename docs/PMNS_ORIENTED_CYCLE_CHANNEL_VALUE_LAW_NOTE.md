# Oriented-Cycle Coordinate-Extraction Lemma

**Date:** 2026-04-16  
**Claim type:** bounded_theorem
**Status:** bounded finite-dimensional algebra lemma
**Stable claim id:** `pmns_oriented_cycle_channel_value_law_note`
**Script:** `scripts/frontier_pmns_oriented_cycle_channel_value_law.py`

## Claim scope

This row proves a finite-dimensional algebra statement for an explicitly
supplied complex `3 x 3` matrix `A`, an explicitly supplied triplet embedding,
and the displayed finite cycle representation.

It proves only:

1. the exact projected-cycle and coordinate-projector identities;
2. the ordered basis identity
   `(P_1 C, P_2 C, P_3 C) = (E_12, E_23, E_31)`;
3. the exact coordinate extraction
   `c = diag(A C^dagger)`;
4. the exact reconstruction of the orthogonal forward-cycle projection of
   `A` from those coordinates.

The title, theorem, and runner do not interpret `c` as a physical observable
or as a value law.

## Supplied finite matrices

Let

`C = E_12 + E_23 + E_31`

and let

- `P_1 = E_11`;
- `P_2 = E_22`;
- `P_3 = E_33`.

The runner also displays an explicit `8 x 8` finite cycle representation `U`
and an explicit isometric triplet embedding `V`. Direct multiplication gives

`V^dagger U^2 V = C`

and the displayed site projectors compress to `P_1, P_2, P_3`.

These are exact identities of the supplied matrices. They are not a derivation
of a retained `hw=1` taste carrier.

## Lemma

Define the ordered forward-cycle basis

`B_i = P_i C`.

Then

- `B_1 = E_12`;
- `B_2 = E_23`;
- `B_3 = E_31`.

The three matrices are orthonormal for the Hilbert--Schmidt inner product

`<X,Y> = Tr(X^dagger Y)`.

For every supplied `A in M_3(C)`, define

`c_i = <B_i,A>`.

Direct multiplication gives

`c_i = Tr((P_i C)^dagger A)`

and therefore

`(c_1,c_2,c_3) = diag(A C^dagger) = (A_12,A_23,A_31)`.

Consequently the Hilbert--Schmidt projection of `A` onto
`span{E_12,E_23,E_31}` is exactly

`Pi_fwd(A) = c_1 E_12 + c_2 E_23 + c_3 E_31`.

Equivalently, the residual `A - Pi_fwd(A)` is orthogonal to all three displayed
basis matrices.

## What the runner establishes

The runner verifies the lemma on all nine standard matrix units and on
multiple deterministic dense complex `3 x 3` matrices, not on an
`active_operator` or a target-derived response fixture. It checks:

- the supplied embedding and projected-cycle identity;
- projector orthogonality, completeness, and the edge-basis identities;
- Hilbert--Schmidt orthonormality of the edge basis;
- exact extraction by both `diag(A C^dagger)` and trace coordinates;
- exact reconstruction and residual orthogonality;
- linearity and idempotence of the forward-cycle projection;
- hostile wrong-cycle and wrong-basis negative controls;
- the source-scope firewall and truthful nonzero failure exit.

## Consistency-only boundary

The former lower-level response-profile round trip was constructed from the
target block and then inverted back to that block. That construction is
consistency-only and is not part of the load-bearing theorem or runner. It is
not independent evidence for a physical PMNS carrier, observable, or readout.

## Open bridges

The remaining `missing_bridge_theorem` is explicit. This row does not supply:

1. a retained derivation identifying the displayed triplet embedding with a
   physical `hw=1` taste carrier;
2. a Record-compatible physical observable/readout map from record content to
   the complex coordinate tuple `(c_1,c_2,c_3)`;
3. a framework construction identifying which matrix-valued block is `A`,
   without assuming its realized entries;
4. a separate state, parameter, or selector law fixing the numerical cycle
   coordinates of that block.

Until those bridges are separately derived and retained, this row is only the
bounded algebraic coordinate-extraction lemma above.

## Command

```bash
python3 scripts/frontier_pmns_oriented_cycle_channel_value_law.py
```
