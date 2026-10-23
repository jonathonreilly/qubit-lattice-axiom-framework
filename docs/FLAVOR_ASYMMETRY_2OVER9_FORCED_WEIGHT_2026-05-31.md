# Flavor: finite C3 complement weights and the coefficient 2/9

**Type:** bounded_theorem
**Review scope:** supplied finite algebra under the stated hypotheses; no
physical state, generation-space identification, or audit status is derived.

Date: 2026-05-31. Claim type: bounded conditional algebra.
Runner: `scripts/flavor_asymmetry_2over9_forced_weight_2026_05_31.py`.

Supply the regular representation of C3 on C³ and remove its invariant
singlet. The remaining two-dimensional complex representation has weights
(1,2), up to ordering, because the regular character decomposes into all three
characters once. This is a statement about a chosen representation, not a
derivation of physical generations or of a gravitational/mass readout.
The [three-label theorem](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
explicitly excludes physical species and full-carrier multiplicity.

## Exact finite coefficient

For zeta=exp(2pi i/3), define

    L3(a,b)=(1/3) sum_{k=1,2} 1/[(zeta^(ka)-1)(zeta^(kb)-1)].

For the supplied complement, each denominator is 3, so L3(1,2)=2/9.
For the alternative repeated nontrivial weights, L3(1,1)=L3(2,2)=1/9.
Among pairs of nonzero characters, a+b=0 modulo 3 selects (1,2) up to
ordering. This condition means determinant one. It does NOT mean the
representation matrix has trace zero: its trace is zeta+zeta²=−1.
The phrase 'trace-free plane' previously conflated this with the coordinate
sum-zero complement of the singlet. The regular-representation hypothesis,
not a generic trace constraint, fixes the weights.

This inverse-normal-determinant average is a finite defined coefficient.
Identifying it as the full contribution of a particular index theorem needs
that theorem's operator, numerator/fibre trace, fixed-locus, and normalization
hypotheses. The scalar arithmetic alone supplies none of these. In particular,
2/9 cannot be a finite character-valued index in Z[zeta]: a rational algebraic
integer is an integer. This does not constrain general analytically regularized
eta invariants or prohibit fractional local summands.

## Coincidences and physical boundary

The supplied functions (d−1)/d²,2/d²,(d²−1)/(12d) agree at d=3 and differ
away from it. Their agreement with the separately defined L3(1,2) is not
independent corroboration of a physical datum or a shared invariant. No
variable-d Ld was defined or tested by this runner.

The [finite KS operator packet](FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md)
is cited for its separate finite symmetry/spectrum construction. This note's
helper does not import/replay it and does not certify global ABSS applicability,
continuum limits, or physical single-fixed-point selection. Those implications
cannot be inferred merely from the coefficient calculation.

A dimensionless intensive readout could be zero or 2/9, among other possibilities.
A separate physical readout principle and applicability proof are needed to
associate this supplied coefficient with charged-lepton asymmetry. Neither
scale/r balance nor a radian phase is derived here. The previous blanket
'operator arc complete, only one remaining gate' and reflection-positivity
readout claims are not conclusions of these checks.
