# Supplied zero-source, real commutant and endpoint-law algebra

**Date:** 2026-04-24
**Type:** bounded_theorem
**Status:** conditional finite algebra; no physical endpoint or phase identification.
**Primary runner:** `scripts/frontier_koide_native_zero_section_closure_route.py`

## Rational definitions and domain

For real z with z≠−1,+1, put w=(1+z)/2 and t=(1−w)/w. Define
Q=(1+t)/3 and K=(t²−1)/(4t). The common original domain excludes both
endpoints: w=0 makes t undefined, and w=1 gives t=0 in K's denominator.
If the weights are probabilities, impose the stronger −1<z<1 separately.
Direct cancellation yields Q=2/[3(1+z)] and K=−z/(1−z²) on this domain.
Thus z=0 gives w=1/2,Q=2/3,K=0; z=−1/3 gives w=1/3,Q=1,K=3/8.
These are properties of supplied functions. They do not select a physical
zero source or identify Q with a measured charged-lepton scalar.

## Complete real commutant and idempotent calculation

Let J=[[0,−1],[1,0]] and R=−I/2+(sqrt(3)/2)J, the120-degree real rotation.
Since sqrt(3)/2≠0, XR=RX iff XJ=JX. Writing X=[[x0,x1],[x2,x3]] and
comparing entries gives x0=x3,x1=−x2, hence exactly X=aI+bJ.
Because J²=−I, X²=X iff

```
a²−a−b²=0,   b(2a−1)=0.
```

If b≠0, a=1/2 requires b²=−1/4, impossible over the reals. Hence b=0
and a=0 or1. The two equivariant idempotents are0 and I. This classifies
endomorphisms of the specified real representation; it is not a physical
spectator selection or an identification of an experimental endpoint.

For every unit real vector v, P=vv^T is rotation-conjugate to diag(1,0).
Rotations commute with R and preserve the Frobenius norm. At diag(1,0),
PR−RP has two off-diagonal entries of magnitude sqrt(3)/2, so
||PR−RP||_F²=3/2 for every orientation. This proves the complete rank-one
commutator statement. The old empty symbolic-solver result remains a diagnostic,
not the proof; the runner adds the exact trigonometric norm identity.

## Supplied affine endpoint and finite scalar

For omega=exp(2pi i/3), define
eta=(1/3)sum_{k=1,2}1/[(omega^k−1)(omega^(2k)−1)].
For either k the denominator is (omega−1)(omega²−1)=3, using
omega+omega²=−1 and omega³=1. Thus eta=(1/3)(1/3+1/3)=2/9.
This finite sum does not itself identify an anomaly or physical phase.

Supply F(phi)=phi+c. The extra based condition F(0)=0 implies c=0.
Supply, separately, the endpoint law delta_open=selected*eta+c and selected=1.
Then c=0 gives delta_open=2/9; c=1/9 gives1/3 as a finite counterfixture.
The variable spectator is absent from this formula. The commutant classification
does not derive the law, the coefficient selected=1, the affine form of F, or
its physical interpretation. In particular no target-provenance independence
is proved merely by calculating eta. No identification with the free Brannen
Fourier phase follows.

## Verification boundary

The child preserves12 old nonliteral conditions, makes six literalTrue assertions
explicitly HISTORICAL_UNSCORED, and adds four controls: rational identities,
excluded endpoints, complete commutator norm and both finite-sum denominators.
It declares this own note, literal120s, resets state, rejects excluded numerical
endpoints/missing input, and returns nonzero on failed conditions. A successful
run would report PASSED:16/16 and SUPPLIED_ROUTE_MATH_CHECKS=PASS. Those flags
are operational summaries, not independent proof or physical/audit certification.
No execution is claimed in this source revision. Old source/cache and assertions
remain preserved. The finite representation classification has a complete proof;
any applicable negative-governance gate remains binding, with no waiver requested.
