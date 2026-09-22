---
claim_id: admissibility_rule_covariant_frame_constructions_cube_orbits_and_antipodal_kernel_propagation_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Normalized equivariant frames and supplied finite atomic kernels on fixed ordered neighbour slots; explicit proper-cubic orbit examples; supplied antipodal-kernel propagation; aligned and tilted overlap evaluations. Exhaustive support classification and minimality certification deferred."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_menus_neighbour_generated_supports_and_cube_orbit_menus_2026_09_15.py
---

# Covariant frame constructions, cube-orbit examples and antipodal-kernel propagation

**Date:** 2026-09-15
**Type:** bounded_theorem

## Result up front

For a supplied pure-state sphere and specified covariance action, a normalized
frame transports finite atomic reference kernels into covariant kernels. The
proper cubic group gives explicit orbit examples with 6, 8, 12 and 24 points.
Under a separately supplied antipodal transition kernel and a one-neighbour
formation order, induction keeps all records on the first seed's axis.
The overlap formula has aligned values 1 and 0; a tilted readout gives 4/5 and
1/5 on the same antipodal pair. These overlap values do not select the
probabilities with which the two records form.

The original broader classification/minimality and generated-alphabet claims
are deferred or corrected below. Their complete arguments remain in the
[original recovery manifest](work_history/review_loop/pr8152/original-manifest.json).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain explicit constructions and finite witnesses; broader classification certification remains deferred."
conditional_surface_status: "Supplied sphere, covariance action, atomic kernels and formation order as stated."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) states: "Each site has a domain
of local possibilities." "No possibility is privileged." "There is one fixed
nearest-neighbor admissibility rule, covariant under lattice translations and
proper cubic rotations." "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." "Records form."

The [possibility-covariance parent](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md)
provides the conditional Bloch-sphere representation and the two supplied
covariance readings. The sphere, records-only conditioning, action on values,
and actual kernels below are mathematical conditions, not selected framework
laws. Under the independent-internal-rotation reading (unsoldered), kernels
obey `r(g A | (x_i,g q_i)) = r(A | (x_i,q_i))`; under the joint-cubic reading
(soldered), `r(h A | (h x_i,h q_i)) = r(A | (x_i,q_i))`. Here `A` is a Borel
subset of the sphere. Support means topological support of a probability
measure. Uniform sphere measure has full support despite zero singleton
masses. Finite atomic supports below are nonempty, and their weights are
positive and sum to one.

Uniform sphere measure is an explicitly supplied no-neighbour seed law,
invariant under internal rotations. It is exempt from the later finite-support assumption.
No physical initial distribution is selected. Standard group action and
probability-kernel constructions are mathematical imports. Haar invariance
and the Bloch overlap are used only within these supplied mathematical models.

## Theorem M1 — axial covariance identities and finite witnesses

For recorded values `±q`, every internal rotation about `q` fixes those
values. Kernel covariance therefore implies invariance of that conditional
measure and its support under these rotations. Conversely, the supplied
atomic kernel `a δ_q + (1-a) δ_(-q)`, for a fixed `0≤a≤1`, obeys this axial
invariance, and transport of `q` gives the corresponding rotation covariance.
Zero weights remove the relevant point from the support.

The primary computes twelve distinct iterates of `(3/5,0,4/5)` under the
rational rotation about `z` with cosine `3/5`, while fixing the pole. This is
a finite orbit witness. The original exhaustive finite-support exclusion is
preserved historically and is not established by twelve iterations.

## Theorem M2 — normalized frames and supplied atomic kernels

Fix two ordered occupied neighbour slots `x_1,x_2` and non-collinear unit
values `q_1,q_2`. Set `t=q_1·q_2` and

`e_1=q_1`, `e_2=(q_2-t q_1)/sqrt(1-t²)`,
`e_3=(q_1×q_2)/sqrt(1-t²)`, `F=(e_1,e_2,e_3)`.

The columns are orthonormal, `e_1×e_2=e_3`, hence `F∈SO(3)`. Preservation of
dot and cross products gives `F(gq_1,gq_2)=gF(q_1,q_2)` for every `g∈SO(3)`.
The original unnormalized third column was incorrect for a generic pair.

Choose finitely many Borel maps `u_j(t)∈S²` and Borel positive weights
`a_j(t)` summing to one. Then

`r(·|q_1,q_2)=Σ_j a_j(t) δ_(F(q_1,q_2)u_j(t))`

is a Borel probability kernel on this non-collinear ordered-pair domain,
and the displayed equivariance proves its internal rotation covariance.
Repeated support points simply combine their masses. A fixed supplied choice
of the maps and weights is part of this construction.

This statement fixes the ordered slot geometry. To transport it across
proper cubic rotations of positions, keep the same reference data within
each ordered-slot orbit. Adjacent and opposite slot configurations may have
different data. An unordered-neighbour law additionally needs compatibility
under exchange; none is silently assumed here. For additional recorded
values, reference data may depend on all their frame coordinates as well as
the slot geometry; the angle `t` alone does not parameterize them. No
exhaustive assignment classification or automatic data selection is claimed.

## Theorem M3 — explicit proper-cubic orbit examples

Let `O` be the 24 determinant-one signed permutation matrices. For a supplied
unit vector `v`, the set `O v` is invariant, since multiplying by a member
of `O` permutes `O`. A uniform measure on an orbit is invariant; convex
mixtures of such measures give further supplied invariant laws.

The primary enumerates all matrices and the directions represented by
`(1,0,0)`, `(1,1,1)`, `(1,1,0)`, `(1,2,3)`, `(1,1,2)`. Normalize each to
unit length when reading it on the sphere; normalization does not change
orbit or stabilizer counts. The exact pairs (orbit size, stabilizer order)
are `(6,4)`, `(8,3)`, `(12,2)`, `(24,1)`, `(24,1)`. Their products are 24.
The axis, diagonal and edge sets and a union are invariant; the specific
mixed set of three axes and one diagonal is not. These are explicit finite
group computations. The original exhaustive orbit-type/minimal-menu
certification is deferred, with its full proof retained in recovery.

## Theorem M4 — supplied antipodal-kernel propagation

Begin with a supplied seed `s_0`; a uniform seed is one declared option.
Specify an order in which every later site has exactly one already-recorded
neighbour, and supply an antipodal kernel supported in `{q,-q}` when that
neighbour has value `q`. Induction then gives every later record a value
in `{s_0,-s_0}`. A single-seeded path or an order on a tree meeting the stated
condition is an example. Forming a row inward from two ends need not meet
the condition at the joining site.

The primary checks 32 sign patterns of a five-entry symbolic seed array;
the general finite-order claim is the induction above. It does not execute
a random formation process. General frame-reference supports contain
additional supplied directions `u_j`; they are not generated solely by the
seed and compositions of frame maps. The original general assertion is
withdrawn.

## Theorem M5 — aligned and tilted overlap values

For the supplied overlap `B(s,r)=(1+s·r)/2`, `B(q,q)=1` and `B(-q,q)=0`.
With `q=e_z` and `r=(4/5,0,3/5)`, the same antipodal records instead give
`B(q,r)=4/5` and `B(-q,r)=1/5`. Thus the original assertion that every
nontrivial Born statistic requires support beyond an antipodal pair is
false. These are evaluations of a supplied function, not a derivation of
Born probabilities, a formation kernel or deterministic copying.

## No-Go Discipline Gate

### N1 — Deferred certification
The original four-row route table mixes scope changes and unattempted
alternatives; it does not satisfy five distinct exact-target attack families.
No negative packet PASS is asserted. Exhaustive support/menu exclusions and
minimality certification remain deferred; their full proofs are preserved.

### N2 — Conditions
The sphere, covariance action, ordered slot geometry, reference kernels and
formation order are explicit conditions. No count of independent walls is
asserted.

### N3 — Hidden inputs repaired
Continuous support is distinguished from positive singleton probability;
the seed is separated from finite later supports; measurable reference data,
weights, extra frame coordinates and readout direction are explicit.

### N4 — Parent scope
The axiom and possibility-covariance links supply exactly their stated
premise/representation context. No earlier campaign assertion that a Born
derivation was closed is imported.

### N5 — Resolution
The primary reports the twelve rotation iterates, one rational frame check,
five orbit examples, invariant sets, symbolic sign patterns and overlap
values. No infinite orbit, stochastic process or whole-lattice execution is
inferred from these finite checks.

### N6 — Primitive boundary
No registered primitive is enlarged into a selector for a menu, kernel,
measure, formation order or readout law.

### N7 — Remaining objection
The explicit constructions leave the supplied reference data free. They do
not by themselves establish the deferred exhaustive/minimal classifications.

### N8 — Recovery
Original arguments and controls remain byte-exact in the manifest, and the
original branch remains available. Withholding packet certification is not
a claim that every original classification theorem is mathematically false.

## Prior art and what is new

Group actions, orbit-stabilizer counting, atomic kernel transport and Bloch
overlap evaluation are standard mathematics. The repository contribution is
the explicit conditional constructions and finite controls for the supplied
local possibility readings. Klein's classification is historical context,
not a substituted proof or a selected physical law.

## Imports

The linked sources provide the authority/representation scope stated above.
The mathematical choices `u_j`, `a_j`, ordered slots, seed, antipodal kernel
and readout direction are supplied. No observational values are fitted.

## Boundaries and non-claims

This note retains covariant constructions and finite witnesses; exhaustive support classification and minimality certification are deferred, and no menu, kernel, covariance reading or physical probability law is selected.
No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
The sphere, reference supports and weights, formation order and overlap function are explicitly supplied mathematical inputs.

## Verification

Run `python3 scripts/admissibility_rule_menus_neighbour_generated_supports_and_cube_orbit_menus_2026_09_15.py`.
The [canonical evidence](../logs/runner-cache/admissibility_rule_menus_neighbour_generated_supports_and_cube_orbit_menus_2026_09_15.txt)
binds the corrected note and actual proof inputs. Its 15 groups include
authority/text/resource-independent scope predicates as well as finite
mathematical checks; they are not 15 independent theorem proofs. Original
control, mutation and review records remain historical in the manifest.
