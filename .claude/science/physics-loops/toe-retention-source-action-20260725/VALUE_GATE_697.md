# Promotion Value Gate — Cycle 697

Answered in writing before the PR, per the physics-loop skill. This record is
not an audit certificate and predicts no audit verdict.

## V1 — What specific verdict-identified obstruction does this PR close?

It does not close one; it narrows two and separates a third. The quoted
obstructions are, verbatim from the audit verdicts:

- `gate_b_farfield_note` (`missing_bridge_theorem`): *"cite or derive retained
  connections from the accepted framework premises to the growth rule, source
  field, propagation/action rule, and TOWARD/F~M physical readout before
  seeking a non-conditional physics verdict."*
- `gravity_law_cleanup_note` (five-judge panel, 5/5): *"the minimal-axiom
  authority expressly withholds dynamics, weights, source/action, and
  physical-observable bridges, while the runner stipulates each of those
  ingredients."*
- `ac_reta_hclass_hunit_readout_derivation_obligation`: *"Record additivity and
  the approved primitives do not themselves determine the carrier, source
  action, or dimensionless readout normalization."*

L1 addresses the **propagation/action rule** clause of the first two: the
operator is not free, it lies in a 2-dimensional family, and one further named
condition reduces it to the Laplacian ray. L2 and L3 address the
**physical-observable** and **dimensionless normalization** clauses by proving
what the axioms cannot supply and naming exactly what must be. The claim made
is narrowing, not closure, and the note says so in its own scope section.

## V2 — What new derivation does this PR contain?

Three results not on `main`:

1. The invariant-kernel dimension for a rotation-closed support set equals the
   number of proper-octahedral orbits in that set, exactly solved at six radii;
   at range 1 this is 2, giving `span{I, Delta}`, and adding
   offset-insensitivity leaves the Laplacian ray. The prior-art sweep found no
   note deriving the form of a record-sourced law from lattice covariance;
   `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`
   *imports* the graph-Laplacian Green's-function identification as an accepted
   premise packet (P1), which is the surface this narrows.
2. Position-blindness: content-only readout at every site forces a constant
   field, so a nonconstant field is never a family of Record readouts.
3. No nonzero Record readout is dimensionless, proved from additivity plus a
   distant-translate duplication whose admissibility legality is checked.

## V3 — Could the audit lane complete this from retained primitives plus standard math?

No. The mathematics of each step is elementary; what is not available to the
audit lane is which axiom clause licenses which hypothesis. The load-bearing
inputs are the exact wording of the Record readout clause (content-only,
finite additive) and the exact symmetry content of Lattice (translations plus
*proper* cubic rotations, no privileged site). Dropping the rotations changes
the dimension from 2 to 7; the runner checks that. The audit lane's own
verdicts state the opposite conclusion is what it currently records — that the
propagation rule is entirely stipulated — so this is not a derivation it
already has.

## V4 — Is the marginal content non-trivial?

Yes. The result is a dimension count with a negative control at every step: the
2-dimensionality is specific to range 1 and is checked to fail at range
`sqrt(2)`; the Laplacian-ray collapse is checked to fail at range `sqrt(2)`;
the forward difference is a local operator that is checked to be excluded. None
of the three results is a definition restated: L2 and L3 are impossibility
statements with explicit witnesses, and L1 is a classification with an
independently computed orbit count.

## V5 — Is this a one-step variant of an already-landed cycle?

No. The closest landed cycle is 693 (Record readout carrier three-way split).
693 classifies scalar readouts of collections and shows Record supplies neither
a finite alphabet, a complex codomain, nor a product. It contains no site
index, no lattice symmetry group, and no operator. Cycle 697's L1 is about
laws on site functions and uses the proper cubic rotation group, which 693 does
not touch; L2 and L3 are properties (position, scale) that 693 does not
address. Cycle 692 is the second-closest: it enumerated scale-fixing mechanisms
on one two-block surface and explicitly disclaimed classifying every
dimensionless construction. L3 is the general statement 692 disclaimed, proved
from the axiom clause rather than by enumeration.

**Verdict: PR allowed.** All five questions pass.

## Cluster cap

This is the first PR in the readout/source-action parent family this campaign.
The cluster-cap evaluator applies from the third; it is not triggered here.
