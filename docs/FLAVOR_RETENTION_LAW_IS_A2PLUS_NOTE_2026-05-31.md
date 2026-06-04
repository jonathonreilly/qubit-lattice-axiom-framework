# Flavor Retention Law: Conditional Algebra Scope Repair

> **Packaging / supersession note:** The earlier single-input framing around source-locality remains a
> possible face of later charged-lepton chain-of-custody work. This repaired packet does not use that
> broader surface as load-bearing authority.

**Date:** 2026-05-31
**Scope repair date:** 2026-06-04
**Claim type:** bounded_theorem
**Actual current surface status:** bounded-support
**Runner:** `scripts/flavor_retention_law_is_A2plus_2026_05_31.py` (SCORECARD PASS=4).
**Audit repair target:** remove the hard-coded R1 assertion and keep only the executable conditional
algebra around onsite source-locality, projected-domain readout, and circulant descent.

## Narrow Claim

This packet proves only the following finite algebra:

1. In the onsite diagonal algebra `D=diag(a,b,c)`, imposing `C3` invariance forces `a=b=c`, so the
   onsite invariant source is scalar.
2. For the supplied formula `Q(z)=2/(3(1+z))`, the onsite scalar value gives `Q(0)=2/3`, while the
   projected-domain value `z=-1/3` gives `Q=1`.
3. With `Z=2P_+-I`, the runner verifies `Z^2=I` and `S_Q1=I-Z/3` has diagonal `10/9` and off-diagonal
   `-2/9` at `d=3`.
4. The intersection of the onsite diagonal algebra with the circulant algebra is only `span{I}`.
   Therefore the sample circulant generation operator `H=I+bC+bC^T` has nonzero off-diagonal mass
   splitting that diagonal compression removes.

These checks support a conditional statement: if an additional physical source-locality/readout premise
selects onsite diagonal sources, then the displayed onsite algebra yields the `Q=2/3` value. The packet
also verifies that this premise is substantive because the sample circulant mass mechanism lives in
off-diagonal data erased by onsite descent.

## Out Of Scope

The following earlier conclusions are not asserted by this narrowed note:

- A2 alone entails the source-domain retention law.
- The source-domain retention law is accepted as a framework rule.
- Charged-lepton `Q=2/3` has an actual effective status from this packet.
- Axiom 2-plus has been upgraded to A2.
- `single_axiom_hilbert`, `single_axiom_information`, or substrate-necessity bridges close the missing
  source-locality theorem here.

The auditor specifically found that the chain from A2 to source-locality was not derived and that the
old runner's R1 pass was hard-coded. This branch removes that pass instead of trying to disguise the
missing bridge.

## Audit Relevance

The repaired source is reauditable as finite conditional algebra, not as a clean A2-to-source-locality
derivation. It does not retag the audit ledger, does not propose an effective status change, and does
not add a new axiom.
