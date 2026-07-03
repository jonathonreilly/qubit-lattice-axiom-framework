# Flavor Retention Law Supplied-Onsite Algebra Boundary

**Date:** 2026-05-31
**Scope repair date:** 2026-06-04
**Updated:** 2026-06-07
**Claim type:** bounded_theorem
**Actual current surface status:** bounded-support
**Runner:** `scripts/flavor_retention_law_is_A2plus_2026_05_31.py`
(SCORECARD PASS=6 FAIL=0).

## Scope

This packet is a finite supplied-definition theorem. It does not derive
source-locality from Axiom 2, does not upgrade "Axiom 2-plus" into Axiom 2,
and does not identify the displayed coordinate value with the physical
charged-lepton Koide value.

The supplied surface is:

```text
onsite diagonal sources + the formula Q(z)=2/(3(1+z)).
```

The theorem is about the algebra on that supplied surface.

## Finite Algebra

1. In the onsite diagonal algebra `D=diag(a,b,c)`, imposing `C_3` invariance
   forces `a=b=c`, so the onsite invariant source is scalar.

2. For the supplied formula

   ```text
   Q(z)=2/(3(1+z)),
   ```

   the coordinate values are

   ```text
   Q(0)=2/3,        Q(-1/3)=1.
   ```

   These are coordinate values of the supplied formula, not physical mass
   predictions.

3. With `Z=2P_+ - I`, the finite matrix

   ```text
   S_Q1 = I - Z/3
   ```

   has diagonal entries `10/9` and off-diagonal entries `-2/9` at `d=3`.

4. The intersection of onsite diagonal operators with the circulant algebra is
   only `span{I}`. Therefore diagonal onsite descent erases the sample
   off-diagonal circulant mass splitting in

   ```text
   H = I + bC + bC^T.
   ```

## Boundary

The finite algebra shows why the onsite source-locality/readout premise is
substantive: onsite descent collapses the circulant mass mechanism to a scalar
and changes the available coordinate. But this packet does not select onsite
sources as the physical readout surface.

The open bridge is:

```text
derive from the current framework why the physical charged-lepton readout uses
onsite diagonal source locality and the supplied Q(z) formula.
```

Until that bridge is proved, `Q(0)=2/3` is a supplied-coordinate result, not a
framework-native charged-lepton value.

## Removed Claims

The following are not asserted:

- A2 alone entails source-domain retention.
- The source-domain retention law is accepted as a framework rule.
- Axiom 2-plus has been upgraded to Axiom 2.
- The finite `Q(0)=2/3` coordinate is the physical charged-lepton Koide value.
- `single_axiom_hilbert`, `single_axiom_information`, or substrate-necessity
  bridges close source-locality here.

## Audit Relevance

The row should be read as bounded support for finite supplied-onsite algebra
and as a boundary exposing the still-open physical source-locality/readout
bridge. It does not retag the audit ledger, does not propose an effective
status change, and does not add a new axiom.
