---
claim_id: possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "On the six-neighbour window of Z^3 with the one-site possibility domain presented as M_2(C) and states coordinatised by Bloch vectors (centre p, six slots q_1..q_6, unrecorded slots absent): exact dimensions of the covariant admissibility-rule space under two readings of the possibility-side symmetry, unsoldered (internal Aut(M_2(C)) = SO(3), or O(3) with the inversion adjoined, acting independently of the 24 proper cubic rotations) and soldered (the three Cl(3,0) generators are the lattice axes, so the action is diagonal). Complete degree-0 to degree-3 tables on all ten recorded-slot strata for scalar-valued, internal-vector-valued and lattice-vector-valued rules, by exact Molien-Weyl character sums with the internal Haar average as a Laurent residue, cross-checked against so(3)-derivation kernels with a Reynolds projector (120 dimensions), against a Frobenius orbit count on the soldered linear row, and out of band against a numerical nullity computation (72 dimensions). Results: no occupancy-only internal-vector response exists unsoldered on any stratum, and exactly one exists soldered on each of the six strata whose recorded barycentre is nonzero; no covariant rule term is linear in the vectors unsoldered, while soldered linear terms exist on every occupied stratum; on the empty neighbourhood the unsoldered invariant ring over the Bloch sphere is one-dimensional through degree ten, so every unsoldered-invariant empty-neighbourhood law agrees with the rotation-invariant law through that degree, while the soldered reading admits a second sphere invariant from degree four, the two laws agreeing on every antipodal two-outcome menu along a lattice axis and separating first at the quartic axis sum (3/5 against 1). Witness pair: Model A (soldered barycentre selector) against Model B (unsoldered neighbour barycentre), agreeing on the empty neighbourhood and differing 2/3 to 1/2 on one recorded neighbour. No continuum, no dynamics, no formation rate; the soldering is a separating clause recorded as a decision point, not adopted."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - admissibility_six_neighbor_affine_cq_channel_solder_support_boundary_bounded_theorem_note_2026-08-14
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
  - admissibility_axis_separable_barycenter_selector_bounded_theorem_note_2026-08-14
  - admissibility_sharp_qubit_record_writer_orientation_axiom_decision_bounded_theorem_note_2026-09-01
  - born_price_wordings_homogeneity_collinear_menus_four_outcome_fair_coin_2026_09_05
  - admissibility_handed_rule_pseudoscalar_invariant_census_and_parity_odd_record_correlators_bounded_theorem_note_2026-09-13
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
runner: scripts/possibility_covariance_soldering_fork_invariant_rules_2026_09_14.py
---

# Possibility covariance: the soldering fork, the invariant rules it permits, and the sphere law it leaves free

**Date:** 2026-09-14
**Type:** bounded_theorem
**Campaign block:** possibility-covariance, wave B of the TOE derivation
campaign by underdetermination witnesses (design note 2026-09-13). The block
asks which symmetry Admissibility must be covariant under on the possibility
side, given that the Qubit axiom names `M_2(C)` and allows a `Cl(3,0)`
presentation that "adds no further primitive structure", and what that
symmetry permits the fixed rule to depend on.

## Result up front

**The axioms leave a fork, and the fork is the whole content of the block.**
The Lattice axiom gives the 24 proper cubic rotations. The Qubit axiom gives
a one-site domain whose automorphism group is `SO(3)`. The Admissibility axiom
requires the one fixed rule to be covariant, but it does not say whether those
two groups act independently or are identified. Reading them independently is
the **unsoldered** reading; identifying the three `Cl(3,0)` generators with the
lattice axes is the **soldered** reading, in which the group acting is the
diagonal copy of the 24 rotations. Every quantity below is computed under both.

**Unsoldered, the recorded neighbours cannot tell the site which way to
point.** On all ten recorded-slot strata the space of covariant rules valued in
an internal Bloch vector and depending on occupancy alone is zero-dimensional,
under `SO(3)` and under `O(3)` alike. Soldered, it is exactly one-dimensional
on each of the six strata whose recorded barycentre `d = sum of the recorded
lattice directions` is nonzero, and zero on the four antipodally closed strata
where `d` vanishes. This reproduces the landed solder-boundary intertwiner
result, which found a single occupancy-to-Bloch intertwiner proportional to `d`
given supplied soldering, and extends it from that note's setting to a
complete stratum-by-stratum table.

**Unsoldered, no covariant rule term is linear in the Bloch vectors at all.**
The degree-1 scalar dimension is zero on every stratum in both unsoldered
readings. Soldered it is `0, 2, 1, 4, 4, 5, 1, 7, 5, 1` across the ten strata,
and that row is reproduced independently as a Frobenius orbit count. Soldering
therefore strictly enlarges the rule space at every positive degree; the
smallest unsoldered rule term that is not built from inner products is the
handed cubic `T = sum over slot triples of det(n_i, n_j, n_k) (q_i x q_j) . q_k`,
48 monomials, the unique unsoldered invariant of degree three, and it dies when
the inversion is adjoined.

**At a site with no recorded neighbour the two readings give different
freedoms, and they separate at fourth order.** Over the Bloch sphere the
unsoldered invariant ring is one-dimensional through degree ten, so every
unsoldered-invariant empty-neighbourhood law has the moments of the
rotation-invariant law through that degree: even axial moments `1/3, 1/5, 1/7`,
every odd moment zero. The soldered reading admits a second sphere invariant
from degree four, and the six-axis law that puts mass `1/6` on each lattice
axis direction realises it. The two laws agree on every antipodal two-outcome
menu along a lattice axis, both giving the fair coin, and separate first at the
quartic axis sum: `3/5` for the rotation-invariant law, `1` for the six-axis
law. The Born-price fair-coin result therefore does not distinguish them; a
fourth-order record statistic does.

**Witness pair.** Model A is the soldered rule that sends the recorded
neighbours to the barycentre selector `D(d) = [I + d.sigma/3]/2`; Model B is
the unsoldered rule that sends them to the barycentre of the recorded
neighbours' own Bloch vectors. Both satisfy every axiom sentence and the
primitives, both return states on every menu, and both give the fair coin on
the empty neighbourhood. On one recorded neighbour they differ: `2/3` against
`1/2` on the antipodal menu along the recorded direction. Model A is covariant
under the soldered action on the whole group and on every stratum, and fails
covariance both under the cubic rotation acting on slots alone and under an
independent internal rotation; Model B is covariant under all three. The pair
is separated by the soldering, not by the lattice symmetry. **Separating
clause, recorded as a decision point and not adopted:** whether the `Cl(3,0)`
presentation's generators are the lattice axes, or whether the internal
`SO(3)` acts independently of the lattice rotations.

**A record can register the identification the law withholds.** The three
recorded Bloch vectors on a positively oriented slot triple form a matrix that
transforms as `M -> g M R^T` under a lattice rotation `g` and an internal
rotation `R`, and is generically invertible. Through such a registered frame a
lattice direction reads as an internal vector even under the unsoldered law:
the composite is exactly equivariant for all 24 rotations and every internal
rotation tested. The law-level dimension count says that reading is not
available from the law alone, since the lattice-vector-valued occupancy
response is zero-dimensional unsoldered and one-dimensional soldered. So
soldering is available as record content without being law content.

**Roles cannot be law content under translation covariance.** Translations act
transitively on the eight sites of the parity cell, so a translation-covariant
function of a single site is constant; the staggered two-class labelling keeps
an index-two subgroup of translations and the four-role labelling keeps the
identity alone. A nearest-neighbour step flips the parity class and a
next-nearest step preserves it, so the roles separate sites that the
six-neighbour window identifies. The roles the support-rule block had to supply
are therefore not derivable from a covariant possibility domain at
nearest-neighbour range; they are ordered-pair data, and the
translation-invariant functions of an ordered site pair span eight.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the Qubit axiom presents the one-site domain as M_2(C) and allows a Cl(3,0) presentation that adds no further primitive structure, and the Admissibility axiom requires one fixed covariant nearest-neighbour rule; whether the internal automorphism group acts independently of the proper cubic rotations or is identified with them was not fixed, and the rule space permitted under each reading had no exact finite census"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the two readings into the menus-and-Born block, where the empty-neighbourhood sphere law and the quartic axis-sum separation become record statistics; test whether the registered frame of Theorem 4 can be promoted from record content to a formation-order statistic; check whether the soldered degree-one row's Frobenius orbit structure survives on the second axial orbit"
conditional_surface_status: "if a clause soldered the Cl(3,0) generators to the lattice axes, the occupancy-to-Bloch response would be one-dimensional wherever the recorded barycentre is nonzero and the empty-neighbourhood law would be free at fourth order; if instead the internal group acts independently, the occupancy-only Bloch response is zero on every stratum and the empty-neighbourhood law is the rotation-invariant one through degree ten"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every dimension, moment and menu value is an exact finite computation in rational arithmetic (Molien-Weyl character sums over a group of order 24 with the internal Haar average taken as a Laurent residue, so(3)-derivation kernels with a Reynolds projector, exact rank over Q, exact Haar moments of the Bloch sphere) on a declared 21-coordinate domain; nothing is asserted beyond the declared degrees and strata"
```

## Premises and declared objects

**Axiom sentences used (canonical text, `docs/MINIMAL_AXIOMS_2026-06-29.md`).**
Lattice: sites are `Z^3` with nearest-neighbour adjacency, "standard
translations, proper cubic rotations". Qubit: "The full one-site possibility
domain has algebraic presentation `M_2(C)`", and "A `Cl(3,0)`-compatible
real-algebra presentation may be used equivalently and adds no further
primitive structure", and "No possibility is privileged. Possibilities are
distinguished by the supplied algebraic structure alone." Admissibility:
"There is one fixed nearest-neighbor admissibility rule, covariant under
lattice translations and proper cubic rotations", and "For each site, the
probability distribution over the possibilities is determined by, and varies
with, the nearest-neighbor conditions." Record: a site need not carry a record;
when present a record locks exactly one admissible possibility.

**Where the two readings come from.** The Admissibility sentence names
covariance under translations and proper cubic rotations, and nothing else. The
internal requirement is supplied by the Qubit sentence "possibilities are
distinguished by the supplied algebraic structure alone": a rule that singles
out an internal direction distinguishes possibilities by something the
algebraic structure does not supply. The inner automorphism group of `M_2(C)`
is `PSU(2) = SO(3)`, which is the unsoldered reading `U`. The `Cl(3,0)`
presentation carries one further automorphism, the grade involution sending
each generator `e_a` to `-e_a`; adjoining it gives the unsoldered reading `U3`
with internal group `O(3)`, and the Qubit sentence that the presentation "adds
no further primitive structure" is exactly what makes admitting it a reading
rather than an import. The soldered reading `S` is the third option: the three
`Cl(3,0)` generators are the lattice axes, so a proper cubic rotation acts on
the slots and on the Bloch vectors together, and no independent internal
rotation is required.

**Domain.** A site's neighbourhood is coordinatised by 21 rational numbers:
the centre's Bloch vector `p` (coordinate block 0) and six slot vectors
`q_1..q_6` (blocks 1 to 6) in the slot order
`DIRS = [+x, -x, +y, -y, +z, -z]`. A slot that carries no record contributes no
coordinate; a recorded-slot subset is therefore a stratum, and the 24 proper
cubic rotations permute the 64 subsets into ten orbits with sizes summing to
64 and representatives `(), (0,), (0,1), (0,2), (0,2,4), (0,1,2), (0,1,2,3),
(0,1,2,4), (0,1,2,3,4), (0,1,2,3,4,5)` in slot indices `0..5`. The recorded
barycentre `d` is the sum of the recorded lattice directions; it is nonzero on
six of the ten strata and vanishes on the four antipodally closed ones.

**Counting convention (stated once, used everywhere).** Every table in this
note and in the runner counts the polynomial ring on the centre vector
together with the recorded slot vectors. Degree zero of any vector-valued
series is independent of that choice, so the occupancy-only response results
below do not depend on it; the higher-degree rows do, and are stated in this
convention throughout.

**Grading caveat against the handed-rule census.** The concurrent handed-rule
census note reports a lowest handed degree of 5 in the unsoldered `SO(3)`
reading. That degree counts letter-indicator variables on a discrete alphabet;
the degrees here count Bloch coordinates. The two gradings are different, and
the handed cubic `T` of degree 3 below is not in tension with that number.

**What is not used.** No Hamiltonian, transfer operator or action; no clock,
formation rate or formation order; no Born weights beyond the two-outcome
antipodal menu evaluated through the landed barycentre selector; no continuum
limit; no lattice larger than one site and its six neighbours.

## Prior art and what is new

Landed and cited: the solder-support-boundary note establishes that with a
supplied soldering there is exactly one occupancy-to-Bloch intertwiner and that
it is proportional to `d`, and states that "Without a soldering, independent
internal naturality kills every occupancy-only Bloch response"; the
axis-separable barycentre selector note supplies `D(d) = [I + d.sigma/3]/2`,
used unchanged here as Model A's menu map; the Q8 conditional-law pair note is
the method precedent for a covariant conditional-law witness pair; the sharp
qubit record-writer note records the orientation decision on the record side;
the Born-price note supplies the four-outcome fair-coin wording that the two
sphere laws are tested against. The internal-external `SU(2)` identification
note, the `Cl(3,0)` colour-automorphism theorem and the inner-automorphism
tracial-identification note are the earlier treatments of the same
identification question in operator language. The concurrent handed-rule
census note supplies the three readings by name and the parity-odd correlators;
the concurrent support-rule note supplies the roles whose derivability is
tested in Theorem 7.

New here: (a) the first use of Molien-Weyl series to classify admissibility
rules, giving complete degree-0 to degree-3 dimension tables for scalar,
internal-vector and lattice-vector rules on all ten strata under all three
readings; (b) the extension of the single-intertwiner solder-boundary result
to a stratum-by-stratum statement, with the four vanishing strata identified as
exactly the antipodally closed ones; (c) the first treatment of the
empty-neighbourhood law as an invariant-ring question on the Bloch sphere, with
the rotation-invariant law pinned through degree ten unsoldered and the
fourth-order separation `3/5` against `1` exhibited soldered; (d) the
registered-frame construction showing a soldering can be record content without
being law content; (e) the translation argument placing the superlattice roles
outside law content at nearest-neighbour range.

## Exact target and obligation graph

**Target.** Fix the symmetry group under which the one fixed nearest-neighbour
admissibility rule must be covariant on the possibility side, and census the
rule terms each choice permits, on the six-neighbour window in Bloch
coordinates, to degree three in general and to degree ten on the empty
neighbourhood.

The obligations below are discharged one per runner section.

- **O1 — the group and the strata.** Exhibit the 24 proper cubic rotations,
  verify closure and faithfulness on the six slots, and reduce the 64
  recorded-slot subsets to their ten orbits with the barycentre computed on each.
  Runner section 1, 13 checks.
- **O2 — the rule-space dimension by reading.** Compute the dimension of the
  covariant rule space for each reading at low degree by exact Molien-Weyl, on
  a single Bloch vector, on the centre with one recorded neighbour and on the
  full window, and verify that soldering strictly enlarges it at every positive
  degree. Runner section 2, 13 checks.
- **O3 — per-stratum tables and an independent route.** Tabulate scalar,
  internal-vector and lattice-vector rule dimensions on all ten strata under all
  three readings to degree three, decide the occupancy-only response question
  stratum by stratum, and reproduce every dimension by a second route that uses
  no character sum. Runner section 3, 14 checks.
- **O4 — explicit rule terms and the frame a record can register.** Exhibit the
  soldered axis-weighted sum, the handed unsoldered cubic, a spanning set of
  unsoldered quadratics, and the record-side frame map, with its transformation
  law and invertibility. Runner section 4, 14 checks.
- **O5 — the law where nothing is recorded.** Compute the invariant ring on the
  Bloch sphere to degree ten under each reading, construct the rotation-invariant
  law and the six-axis law, and find the lowest record statistic that separates
  them. Runner section 5, 13 checks.
- **O6 — the witness pair.** Exhibit two rules, each satisfying every axiom
  sentence and each primitive, that agree on the empty neighbourhood and differ
  on a recorded menu, and verify which symmetry each respects. Runner section 6,
  12 checks.
- **O7 — where oriented data can come from.** Test whether the superlattice
  roles of the concurrent support-rule note can be law content under translation
  covariance, and whether a registered frame supplies the lattice-to-internal
  reading the unsoldered law withholds. Runner section 7, 12 checks.

## Theorems

**Theorem 1 (the group, the strata, the barycentre).** The proper cubic
rotations form a group of order 24, act faithfully on the six lattice
directions, and carry antipodal slots to antipodal slots. The 64 recorded-slot
subsets fall into exactly ten orbits, with orbit sizes summing to 64 and each
orbit size times its stabiliser order equal to 24. The recorded barycentre
`d = sum of recorded directions` is nonzero on six orbits and zero on the four
whose recorded set is closed under antipodal pairing, namely `()`, `(0,1)`,
`(0,1,2,3)` and the full window. *Runner section 1.*

**Theorem 2 (dimension of the covariant rule space).** On a single Bloch vector
the unsoldered ring has exactly one invariant in each even degree and none in
each odd degree, while the soldered ring first gains a second invariant at
degree four, which is the lowest cubic harmonic. On the full window the
soldered dimension strictly exceeds the unsoldered dimension in every positive
degree. Under the unsoldered readings no covariant rule term is linear in the
Bloch vectors, on any stratum. Under the soldered reading the degree-one
dimension is

| stratum | `()` | `(0,)` | `(0,1)` | `(0,2)` | `(0,2,4)` | `(0,1,2)` | `(0,1,2,3)` | `(0,1,2,4)` | `(0,1,2,3,4)` | full |
|---|---|---|---|---|---|---|---|---|---|---|
| soldered degree-one scalars | 0 | 2 | 1 | 4 | 4 | 5 | 1 | 7 | 5 | 1 |

and this row is reproduced independently as a Frobenius orbit count on the
coordinate set under the stratum stabiliser. *Runner section 2.*

**Theorem 3 (the ten-stratum census, and the occupancy-only response).** With
the centre included among the counted vectors, the covariant rule-space
dimensions in degrees 0 to 3 are

| stratum | `d != 0` | scalar, `U` | scalar, `U3` | scalar, `S` | internal vector, `U` | internal vector, `S` | lattice vector, `U` | lattice vector, `S` |
|---|---|---|---|---|---|---|---|---|
| `()` | no | 1,0,1,0 | 1,0,1,0 | 1,0,1,0 | 0,1,0,1 | 0,1,0,2 | 0,0,0,0 | 1,1,3,3 |
| `(0,)` | yes | 1,0,3,0 | 1,0,3,0 | 1,2,7,12 | 0,2,1,6 | 1,6,15,44 | 0,2,1,6 | 3,14,49,124 |
| `(0,1)` | no | 1,0,4,0 | 1,0,4,0 | 1,1,10,16 | 0,2,1,10 | 0,5,14,67 | 0,1,2,8 | 2,10,55,181 |
| `(0,2)` | yes | 1,0,4,0 | 1,0,4,0 | 1,4,25,80 | 0,2,1,10 | 1,14,65,250 | 0,4,5,26 | 5,40,205,740 |
| `(0,2,4)` | yes | 1,0,4,2 | 1,0,4,0 | 1,4,26,124 | 0,2,2,14 | 1,12,78,364 | 0,4,6,40 | 3,36,234,1092 |
| `(0,1,2)` | yes | 1,0,7,1 | 1,0,7,0 | 1,5,43,175 | 0,3,3,24 | 1,19,113,553 | 0,5,9,56 | 5,53,355,1631 |
| `(0,1,2,3)` | no | 1,0,5,0 | 1,0,5,0 | 1,1,21,75 | 0,2,1,16 | 0,7,39,265 | 0,1,4,22 | 2,16,141,755 |
| `(0,1,2,4)` | yes | 1,0,9,4 | 1,0,9,0 | 1,7,64,336 | 0,3,4,39 | 1,23,176,1024 | 0,7,16,111 | 5,67,544,3056 |
| `(0,1,2,3,4)` | yes | 1,0,8,4 | 1,0,8,0 | 1,5,46,280 | 0,3,4,37 | 1,15,126,860 | 0,5,12,95 | 3,41,388,2560 |
| full | no | 1,0,5,1 | 1,0,5,0 | 1,1,15,69 | 0,2,1,17 | 0,4,25,229 | 0,1,4,25 | 1,8,92,657 |

Three readings of this table are load-bearing.

First, the internal-vector column at degree zero is the occupancy-only Bloch
response: a rule that turns which slots carry records, and nothing else, into a
Bloch direction for the centre. Under `U` it is 0 on all ten strata. Under `U3`
it is 0 on all ten strata. Under `S` it is 1 exactly on the six strata with
`d != 0` and 0 on the four antipodally closed ones. This reproduces the landed
solder-support-boundary theorem, which found exactly one such intertwiner
proportional to `d` given a supplied soldering and none without one, and extends
it to a statement about every stratum: the response is not merely absent
unsoldered, it is one-dimensional soldered precisely where the recorded
barycentre survives, and absent soldered on the four strata where it does not.

Second, the lattice-vector and internal-vector columns coincide identically on
all ten strata under the soldered reading and differ under the unsoldered one.
Soldering is exactly the identification of the two vector representations, read
off the census rather than assumed.

Third, the `U3` scalar column equals the `U` column in even degrees and vanishes
in odd degrees. Adjoining the `Cl(3,0)` grade involution removes the handed
content and nothing else.

Every one of the 120 dimensions in this table was produced twice inside the
runner, once by a Molien-Weyl character sum with the internal Haar average taken
as a Laurent residue and once by intersecting the kernels of the three so(3)
derivations with a Reynolds projector onto the cubic-invariant subspace, with
zero mismatches. *Runner section 3.*

**Theorem 4 (explicit terms, and the frame a record can register).** Four
exhibits pin the census down in closed form on the full window.

- The axis-weighted sum `S1 = sum over slots i and axes a of (r_i)_a (q_i)_a`,
  where `r_i` is the lattice direction of slot `i`, has one term per lattice axis
  direction, is invariant under the soldered action, is not invariant under the
  unsoldered lattice action, and is not annihilated by internal so(3). It is the
  simplest soldered rule term and the reason the soldered degree-one dimension is
  nonzero.
- The handed lattice term `T = sum over slot triples (i,j,k) of
  det(r_i, r_j, r_k) ((q_i x q_j) . q_k)` has 48 monomials, is annihilated by
  internal so(3), is invariant under the unsoldered lattice action, is the unique
  unsoldered invariant of degree three, and does not survive adjoining the grade
  involution. So the lowest unsoldered handed rule term on this window sits at
  cubic order in the Bloch coordinates, and the handedness is carried by the
  lattice determinant, not by any internal choice.
- Five explicit quadratics span the whole unsoldered quadratic space: the centre
  norm, the sum of slot norms, the centre-to-slot sum, the antipodal-pair sum,
  and the non-antipodal-pair sum. All five are so(3)-annihilated and
  lattice-invariant, are linearly independent, and their span has the dimension
  the census predicts.
- The recorded frame `M`, whose columns are the recorded slot vectors in lattice
  order, transforms as `M -> g M R^T` under a cubic rotation `g` acting on slots
  and an internal rotation `R` acting on vectors, is generically invertible, and
  the transformation law was verified for all 24 cubic rotations and for the
  internal rotations tested.

The frame is the sharp point. A rule may not use an identification of the
lattice axes with the internal generators, unsoldered; but a record whose slot
vectors are linearly independent already carries one, as the map `M`. The
identification is therefore available as record content on a generic recorded
configuration while being unavailable as law content. *Runner section 4.*

**Theorem 5 (the law at a site with no recorded neighbour).** On the empty
stratum the rule is a probability law on the Bloch sphere `S^2`, and the question
is which such laws are covariant.

Under both unsoldered readings the invariant ring restricted to the sphere is
one-dimensional in degree 0 and empty in every degree from 1 to 10, with series

| degree | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| unsoldered, sphere | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| soldered, sphere | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 |

So an unsoldered-covariant empty-neighbourhood law has the same moments as the
rotation-invariant law through degree ten, while the soldered reading first
admits a free direction at degree four. The two candidate laws are the
rotation-invariant one, whose even axial moments are

| moment | `E[n_z^2]` | `E[n_z^4]` | `E[n_z^6]` |
|---|---|---|---|
| rotation-invariant law | 1/3 | 1/5 | 1/7 |
| six-axis law | 1/3 | 1/3 | 1/3 |

with every odd moment zero on both, and the six-axis law, which places weight
`1/6` on each of the six lattice directions. The six-axis law is invariant under
the lattice rotations and is not invariant under an internal rotation, so it
exists soldered and not unsoldered.

Both laws give the same fair antipodal coin along a lattice axis: each outcome
has probability exactly `1/2`. They first separate at the quartic axis sum
`sum over a of E[n_a^4]`, which is `3/5` for the rotation-invariant law and `1`
for the six-axis law. They also separate on the mixed even moment
`E[n_x^2 n_y^2]`, which is `1/15` and `0` respectively. The Born-price
fair-coin wording therefore does not distinguish the two readings; a
fourth-order record statistic does. *Runner section 5.*

**Theorem 6 (the witness pair).** Two rules are exhibited on the recorded-menu
window.

- **Model A, soldered.** The centre's Bloch direction is the recorded
  barycentre `d`, and the menu along an antipodal pair `+m, -m` is given by the
  landed barycentre selector `D(d) = [I + d.sigma/3]/2`.
- **Model B, unsoldered.** The centre's Bloch direction is the barycentre of the
  recorded neighbours' own Bloch vectors, fed through the same selector.

Both are probability laws on every stratum and on both readings: every menu
either returns is a state. They agree on the empty neighbourhood, where both
give the fair coin `1/2, 1/2`. They disagree on one recorded neighbour in the
`+x` slot whose own Bloch vector points along `+x`, where Model A returns
`2/3, 1/3` along the `x` axis and Model B returns `1/2, 1/2`.

Model A is covariant under the soldered action, both as a whole group and stratum
by stratum, and that test is not vacuous, since the soldered action moves the
menu Model A returns. Model A is not covariant when a cubic rotation moves the
slots alone, and not covariant under an independent internal rotation. Model B is
covariant under independent internal rotations, under a cubic rotation acting on
slots alone, and under the soldered action as well.

So the pair is separated by the soldering and not by the lattice symmetry. The
minimal separating clause is recorded as a decision point, not adopted: *the
three `Cl(3,0)` generators are the three lattice axes*. With that clause, Model
A is admissible and the occupancy-to-Bloch response exists; without it, Model A
is not covariant and every occupancy-only response vanishes. *Runner section 6.*

**Theorem 7 (roles, translations, and where oriented data can come from).** The
concurrent support-rule note obtained a Gauss-law support set and a flux of 5 by
supplying parity roles on a two-by-two-by-two cell. Under translation covariance
those roles cannot be law content.

The translations act transitively on the eight sites of the parity cell, so a
translation-covariant function of a single site is constant. The staggered
labelling by site parity is preserved by an index-two subgroup of the
translations, and the translation-invariant functions of the parity class are the
constants. The four-role labelling is preserved by the identity translation
alone. A nearest-neighbour step has parity weight one and flips the parity class;
a next-nearest step has parity weight two and preserves it. So the roles separate
sites that the six-neighbour window identifies, and they are next-nearest-range
data. Translation-invariant functions of an *ordered* site pair span an
eight-dimensional space, which is where such data can live.

The registered frame of Theorem 4 inverts exactly, and through it a lattice
direction reads as an internal vector even under the unsoldered reading. That
reading is not available from the law alone. Oriented link data of the kind the
support-rule note supplied is therefore consistent with an unsoldered law
provided it is carried by records, not by the rule. *Runner section 7.*

## No-Go Discipline Gate

The negative content of this note is four statements, each scoped to the
six-neighbour window, to the declared Bloch coordinatisation, and to the declared
degrees: (i) under either unsoldered reading there is no covariant rule sending
the recorded-slot pattern alone to a Bloch direction, on any of the ten strata;
(ii) under either unsoldered reading no covariant rule term is linear in the
Bloch coordinates, on any stratum; (iii) an unsoldered-covariant law on the empty
neighbourhood has no non-constant invariant through degree ten, so its moments
there are those of the rotation-invariant law; (iv) the superlattice roles of the
concurrent support-rule note are not translation-covariant functions of a site or
of its parity class. The gate is applied to that content only.

**N1 — alternative routes.** Routes that would give an unsoldered occupancy-only
response, each left open: extend the window past nearest neighbours, where the
ordered-pair invariants of Theorem 7 already span eight dimensions; let the rule
depend on record content beyond the Bloch vector, for example a registered frame,
which Theorem 4 shows is available; let the response be a higher-rank internal
tensor rather than a vector, which the census here does not cover; let the
identification be carried by a formation order rather than by the rule, which the
formation-order block left as a decision point; let the internal group be a
proper subgroup of `SO(3)` fixed by some further supplied structure, which the
handed-rule census reads as its own separate clause. None of these is tested
here, and none is argued against.

**N2 — wall independence.** The four statements do not share a mechanism. (i) is
a degree-zero equivariance count; (ii) is a degree-one count; (iii) is a
restriction of the invariant ring to the sphere; (iv) is a transitivity argument
about lattice translations that uses no internal group at all. (i) and (ii) do
share the character-sum machinery, and both were reproduced by the derivation
kernel route and the out-of-band nullity route, so the agreement is not an
artefact of one method.

**N3 — hidden walls.** Three assumptions are visible and named rather than
hidden: the rule is a polynomial in the Bloch coordinates of the centre and the
recorded neighbours, so a non-polynomial covariant rule is outside this census;
the degree ceiling is three on the full window and ten on the sphere, so nothing
is said above those degrees; and the counting convention includes the centre
vector among the counted vectors, which affects the higher-degree rows and not
the degree-zero results that carry (i).

**N4 — residual matching.** The residual left by (i) to (iii) is precisely one
sentence of supplied structure, the soldering clause, and it is the same sentence
the landed solder-support-boundary note already identified as the price of the
occupancy-to-Bloch intertwiner. The residual left by (iv) is next-nearest-range
data or record content, which matches the concurrent support-rule note's own
recorded decision point that its roles are next-nearest-neighbour structure.

**N5 — rhetoric audit.** The statements above are scoped to a window, a
coordinatisation and a degree ceiling, and each is a count rather than an
impossibility. This note asserts no terminal claim about the search space, names
no route as the final one, and treats the soldering clause as a decision point
that is recorded rather than adopted. Where the text says a response is absent,
it means absent in the declared degrees on the declared window.

**N6 — partial-closure paths.** Two partial routes are already visible inside
this note. The registered frame of Theorem 4 supplies the identification on any
generically recorded configuration, so an unsoldered law that reads its
neighbours' vectors can behave like a soldered one wherever a frame is present.
And the soldered degree-one row of Theorem 2 is a Frobenius orbit count, which
suggests the soldered rule space has a combinatorial description that may extend
past the degree ceiling used here.

**N7 — steelman.** The strongest case against the negative content is that the
Qubit axiom's `Cl(3,0)` sentence says a real-algebra presentation "may be used
equivalently and adds no further primitive structure", and one might read the
equivalence as already fixing which real generators are which lattice axes. The
census answers that reading on its own terms: if the sentence is read as a
soldering, every dimension in the soldered columns is available and the
occupancy-to-Bloch response exists; if it is read as an equivalence of
presentations with no preferred pairing, the unsoldered columns apply. The two
readings give different, exactly computed rule spaces, and the witness pair of
Theorem 6 shows the difference is observable in a recorded menu. That is why the
clause is recorded as a decision point rather than settled here.

**N8 — cross-cycle echo.** The landed solder-support-boundary note states
"Without a soldering, independent internal naturality kills every occupancy-only
Bloch response". Statement (i) is the same fact, computed independently by three
routes and extended to all ten strata, with the additional finding that the
soldered response is absent on the four antipodally closed strata as well. The
concurrent handed-rule census reports the three readings and the parity-odd
correlators; statement (ii) is consistent with it once the two gradings are
distinguished, as recorded in the premises. No earlier note treats the
empty-neighbourhood sphere law, so (iii) has no echo to reconcile.

## Falsifiers

- Exhibit a polynomial rule in the declared coordinates, of degree at most
  three, that is covariant under the unsoldered action and sends the
  recorded-slot pattern alone to a nonzero Bloch direction on any stratum. That
  contradicts Theorem 3.
- Exhibit a covariant rule term linear in the Bloch coordinates under either
  unsoldered reading. That contradicts Theorem 2.
- Exhibit an unsoldered-covariant law on the empty neighbourhood whose moments
  differ from `1/3, 1/5, 1/7` at or below degree ten. That contradicts
  Theorem 5.
- Exhibit a fourth unsoldered invariant of degree three on the full window, or a
  second one that survives the grade involution. That contradicts Theorem 4.
- Show that Model A of Theorem 6 fails an axiom sentence or a primitive, or that
  Model B does, or that the two agree on the one-recorded-neighbour menu. That
  dissolves the witness.
- Exhibit a translation-covariant function of a single site, or of its parity
  class, that reproduces the four roles of the concurrent support-rule note. That
  contradicts Theorem 7.

## Boundaries and non-claims

- **No clause is adopted.** The soldering is recorded as a separating clause and a
  decision point. This note does not add it to the axioms, does not recommend
  adding it, and does not report a status change for any ledger row.
- **No dynamics.** No Hamiltonian, transfer operator, action, clock, formation
  rate or formation order appears anywhere in the runner.
- **No continuum.** One site and its six neighbours, on the cubic point group of
  order 24. No lattice limit, no field, no propagator.
- **Degrees and window are the scope.** Degree three on the full window, degree
  ten on the sphere, polynomial rules in the declared 21 coordinates. A
  non-polynomial rule, a longer-range rule, or a higher-degree term is outside
  what is computed.
- **The Born content is narrow.** The one Born-style statement is that both
  candidate empty-neighbourhood laws give the fair antipodal coin, evaluated
  through the landed barycentre selector. No weight values are derived and no
  menu beyond the antipodal pair is treated.
- **The frame is record content.** Theorem 4 shows a record can register the
  identification. It does not show that any record does, nor that formation
  produces frames, nor that the registered frame is unique.

## Imports

None.

## Review record

- **Seat:** one Opus 5 seat; no subagents; runner and note by the same seat.
- **Independence sources:** (i) exact Molien-Weyl character sums over the
  stratum stabiliser in the cubic group, with the internal Haar average taken as
  a Laurent residue in the `SU(2)` character variable; (ii) a second in-runner
  route that builds each graded piece as the intersection of the kernels of the
  three so(3) derivations and then applies a Reynolds projector, with an exact
  rank over the rationals, and uses no character sum at all, agreeing with (i) on
  all 120 tabulated dimensions; (iii) a Frobenius orbit count on the coordinate
  set under the stratum stabiliser, independently reproducing the soldered
  degree-one row of Theorem 2; (iv) an out-of-band floating-point recomputation,
  not part of the landed runner, computing each dimension as the nullity of the
  stacked system `rho(g) - I` over degree-`d` monomials with random internal
  rotations standing in for the Haar average, agreeing on 72 of 72 values across
  all three readings and six strata.
- **Mutation census** (each mutant run to completion; caught = at least one FAIL
  or a nonzero exit):

| mutation | substitution | result |
|---|---|---|
| improper cubic elements admitted into the lattice group | determinant filter `== 1` relaxed to `!= 0` | caught, PASS=76 FAIL=18 |
| unsoldered action stops permuting the recorded slots | slot permutation replaced by the identity | caught, PASS=91 FAIL=3 |
| internal Haar average dropped from the Molien route | the Laurent residue keeps its first term only | caught, PASS=78 FAIL=16 |
| barycentre of the recorded slots omits one direction | the sum skips slot index 5 | caught, PASS=90 FAIL=4 |
| empty-neighbourhood law placed on three axes, not six | weight `1/3` on the first three directions | caught, PASS=93 FAIL=1 |
| model B reads lattice directions instead of Bloch vectors | neighbour vector replaced by its slot direction | caught, PASS=90 FAIL=4 |
| the test internal rotation is replaced by the identity | the quarter turn becomes the identity matrix | caught, PASS=92 FAIL=2 |
| barycentre selector scaled by three instead of one third | division by three becomes multiplication | caught, PASS=92 FAIL=2 |
| equivariant correction index transposed in the kernel route | the epsilon indices are swapped in the vector route | caught, PASS=93 FAIL=1 |

  Nine mutants, nine caught. A tenth substitution was run and is reported here as
  a non-defect: restricting the so(3) kernel loop to two of the three generators
  left the runner green, correctly, because two generators annihilating a
  polynomial force the third through their commutator, so the invariant space is
  unchanged. It is recorded to show the miss was diagnosed rather than ignored.
- **Vacuity guard:** every covariance test that could pass by moving nothing is
  paired with a check that the group element does move the object. The soldered
  covariance of Model A is paired with a check that the soldered action changes
  the menu Model A returns; the internal-rotation tests are paired with a check
  that the test rotation is a proper rotation and moves the menu direction; the
  slot-only test is paired with the failure it is supposed to produce. Two
  defects of exactly this kind were found and repaired during construction, a
  vacuous covariance test and an unsoldered failure that was invisible because
  nothing moved.
- **Budget:** about 15 s, 94 checks, stdout 5901 characters, largest dense object
  the degree-three monomial basis on 21 coordinates restricted by multidegree, no
  dense space of dimension 2^11 or more, exact rational arithmetic throughout the
  landed runner.

## Verification

```bash
python3 scripts/possibility_covariance_soldering_fork_invariant_rules_2026_09_14.py
```

Expected summary line: `TOTAL: PASS=94 FAIL=0` (followed by the elapsed time).
Cached output:
`logs/runner-cache/possibility_covariance_soldering_fork_invariant_rules_2026_09_14.txt`.
