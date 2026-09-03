---
claim_id: through_lattice_role_marking_two_finite_negatives
claim_type: bounded_theorem
claim_scope: "On the cubic lattice Z^3 with one qubit per site, ordinary (commuting) composition throughout, two named classes of star-local rule are evaluated on named finite clusters against the superlattice role patterns of PR #7834, exactly where stated and matrix-free-numerically where tagged. (T1, exact) The 24 proper rotations and the 48-element full cubic group induce the same 20 orbits on the 128 seven-bit star patterns with identical canonical representatives, so every rotation-invariant value-reading star rule is inversion-invariant; and at spacing 2 the 48 templates of the period-(4,2,2) pattern give every corner six free code neighbours and their stars realise all 128 value patterns and all 4 adjacent pairs, so the maximal value-reading star rule is vacuous there. (T2, exact, exhaustive constraint propagation, no SAT solver) On the spaced superlattices with coarse spacing s and one code site per coarse edge at position p, for s = 3 at both code positions (10 marker orbits, 1024 covariant assignments each) and s = 4 midpoint (9 orbits, 512 assignments): accepted set sizes span 28-111, 28-111 and 8-69 of 128 with 0 vacuous; the sound uniform-configuration filter passes 282/1024, 282/1024 and 32/512; and for every one of the 2560 assignments a branch-on-first-undetermined-site propagation search returns a zero-penalty configuration on the s-torus that is no translate or rotation of the intended pattern, 0 junk-free, in 38590 and 16363 branch nodes, at most 133 and 301 for one assignment, with period multiset censuses of the lexicographically least witness 489x(3,3,3) 438x(1,1,1) 73x(1,3,3) 24x(1,1,3) at s = 3 and 321x(1,1,1) 37x(1,2,2) 36x(2,2,2) 33x(1,1,2) 31x(1,1,4) 17x(4,4,4) 15x(1,4,4) 11x(1,2,4) 8x(2,2,4) 3x(2,4,4) at s = 4; each of the 2560 witnesses tiles to the 2s-torus (6^3, 8^3) with penalty 0 and is still no translate or rotation; and the maximum number of code neighbours of a site is 3 at s = 3 and 1 at s = 4 midpoint, never 6, so the spacing-2 vacuity is defeated and the failure has a different mechanism. (T3, exact) For state-reading frustration-free star templates h = 1 - Pi_K, a torus side of length 2 identifies the two +- neighbour slots on that axis and the star term becomes the pullback h = 1 - V^dag Pi_K V, whose diagonal isometry has image span{|00>,|11>} on that pair, holding the pinned product |p>|p> exactly when ab = 0 for |p> = a|0> + b|1>, a Z eigenstate; on the 2D 4x2 torus 30 of 72 (pin pair, variant) cases are vacuous, exactly FULL at all 30 pairs with v != f, and of the 42 live cases 22 are faithful and 20 are not, the unfaithful being exactly those with neither pin a Z eigenstate. (T4, exact) On the 2D 4x2 torus the faithful Z-pin rows carry junk zero modes 12 and 4 at v = f = |0> (dim K 17, nullity 35, 23 intended) and 36 at v = |0>, f = |1> (dim K 24, nullity 64, 28 intended), with no faithful pin choice junk-free; on the non-aliased 2D 4x4 torus, matrix-free with state vectors of length 65536 [numerical], alternating projections reach residual energy at most 9e-14 and the converged zero-energy vectors carry junk fraction 0.85-0.89, 0.31-0.33, 0.91-0.92, 0.65-0.67 and 0.78-0.84 at (+,+) EVEN, (+,+) FULL, (0,1) EVEN, (+,-) EVEN and (0,+) EVEN, with Hutchinson kernel-dimension estimates over 4 probes of 743+-13, 743+-13, 1534+-22, 399+-7 and 690+-17 against 96, 511, 124, 128 and 128 intended [numerical, stochastic, seed fixed]. (T5) The 3D seven-site star has dim K 51-76 of 128 in EVEN and 65-105 in FULL over all 64 pin triples from {0,1,+,-}, none vacuous, and all 16 all-Z triples are faithful on the 4x2x2 torus (exact); there [numerical, matrix-free, seed fixed] junk fractions are 0.56-0.62, 0.53-0.54, 0.74-0.76 and 0.89-0.90 at (0,0,0) EVEN, (0,0,0) FULL, (0,1,0) EVEN and (0,1,1) EVEN with residual energy at most 1e-15. (T6) One 2D and one 3D junk vector have energy at most 2e-15, weight inside the intended span at most 7e-31, Schmidt rank 35 and 31 across a half cut of 256, and every single-site reduced state mixed with purity at most 0.661 and 0.725, so no site is pinned [numerical, matrix-free, seed fixed]; and exactly (exact) the one-dimensional three-site star on an 8-ring is junk-free for the Z pins in the EVEN variant, dim K 3 and nullity 3 against 3 intended, 2 of 8 choices junk-free. These are finite negative results on two named classes over named finite clusters. The s = 4 off-midpoint, s = 5 and s = 6 superlattices and the Haar-pin templates are scratch-only and are not claimed here. No axiom is amended, no status is set, no registry entry is created, and nothing here is derived from any axiom."
upstream_dependencies: []
runner: scripts/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.py
---

# Through-lattice role marking: two finite negative results, one on value-reading star rules and one on state-reading star templates

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.py`](../scripts/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.txt`](../logs/runner-cache/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (PR #7834) supplies a law on a `5x5x5` window whose zero set is exactly `48`
superlattice role patterns, and leaves one item open in its Proof boundary: "whether a rule whose direct dependence is on adjacent sites only, longer reach arising through chains of adjacent
conditions, can select the same zero set is open -- for value-reading star rules Theorem 3 item 2 answers no at this spacing, and for possibility-state rules it is untested here." Its Interfaces
name the second half again: "A rule whose star constraint reads which local possibilities remain admissible, rather than which value is recorded, is untouched by it." This note answers that item
for two named classes of star-local rule, on named finite clusters, and for no others. Both answers are negative, both are finite, and the two mechanisms differ and are named. Neither says that a
rule of adjacent-site direct dependence is unavailable; each says that one class of such rule, on the clusters listed, has no junk-free member.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite negative results on two named classes of star-local rule, over named finite clusters. Groups A and B are exact -- bit arithmetic, exhaustive enumeration, exhaustive constraint propagation with no solver. Group C mixes exact dense linear algebra on 8-qubit and 7-qubit spaces with matrix-free numerical statements on 16-qubit tori; every numerical line is tagged and carries its converged residual, and the two stochastic lines fix their seed and report standard errors."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster result, and route to its owner the question this note leaves open: whether some other adjacent-site rule -- energetic rather than frustration-free, or reading more than one star -- selects the role pattern."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`C`.

1. `T1` (`A1`, `A2`). The star-pattern orbit fact, and the spacing-2 vacuity of PR #7834 restated and recomputed.
2. `T2` (`B1`-`B6`). Value-reading star rules on spaced superlattices, exhaustive at `s = 3` for both code positions and at `s = 4` midpoint, with the period-collapse census and the zoom-out
   lemma.
3. `T3` (`C1`, `C2`). The aliasing lemma for state-reading star templates on tori with a side of length `2`.
4. `T4` (`C3`, `C5`, `C6`) and `T5` (`C4`, `C7`). Two and three dimensions: the exact rows, and the matrix-free rows on the `16`-qubit tori.
5. `T6` (`C8`, `C9`). The character of the junk, and the one-dimensional contrast, which is junk-free.

## Imports and authority

Imported scientific authority: none load-bearing. Alternating projection onto an intersection of subspaces and the Hutchinson trace estimator are standard methodology; every object is redeclared
here and the runner recomputes every statement. No observational value, no fitted number, and no framework premise enters any proof. Non-load-bearing context pointers, plain file names citing no
grade and consuming no row:

- `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (the `48`-sector role pattern whose open item this note answers for two classes,
  and the source of the two quotations above).
- `MINIMAL_AXIOMS_2026-06-29.md` (the four framework axioms quoted in "Setting").

## Setting

The four framework axioms are quoted, not amended, and nothing below is derived from them. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." **Qubit**: each site has a domain of local possibilities whose full one-site possibility domain has algebraic presentation
`M_2(C)` -- one qubit per site, and no more. **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."
**Record**: records form, lock exactly one admissible local possibility, are permanent, and are the only readable thing. Composition here is **ordinary**: the algebra of a region is the tensor
product of its sites' algebras and operators on disjoint regions commute. The two rule classes below are both of the form Admissibility permits in shape -- one fixed rule, identical at every site,
covariant under the lattice motions, whose direct dependence is a site and its six neighbours. What is at issue is not their shape but what each of them selects.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the strongest supported scope is precisely `P0`-`P4`.

1. `P0` (declared here): the star, the two rule classes, the role patterns, the spaced superlattices, and what counts as junk.
2. `P1` (`A`): the orbit fact and the spacing-2 vacuity.
3. `P2` (`B`): the value-reading result on spaced superlattices, its census, and the zoom-out lemma.
4. `P3` (`C1`-`C4`): the aliasing lemma, the exact `4x2` rows and the exact star-kernel dimensions; `P4` (`C5`-`C9`): the matrix-free rows, the junk character, and the one-dimensional contrast.

## Definitions

A site's **star** is the site together with its six nearest neighbours: seven sites, seven values, `128` value patterns. A **superlattice role pattern** is a repeating arrangement of pinned site
values whose period exceeds the lattice spacing, with some sites left free; in PR #7834 the period is `(4, 2, 2)`, corners, faces and cube centres pinned by coordinate parity and coarse edge sites
free. The lattice itself is unchanged.

A **value-reading star rule** is a predicate on the seven recorded `Z`-values of a star, invariant under the `24` proper rotations; its **penalty** on a configuration is the number of stars it
rejects. Given an intended arrangement, the **maximal** such rule accepts exactly the star patterns realised in the intended configurations over every filling of the free sites; every other rule
of the class accepts at least those, so the maximal rule is the most selective member. **Junk** is a zero-penalty configuration on the torus whose values on the pinned sites are no translate and
no rotation of the intended pattern.

A **spaced superlattice** has coarse spacing `s` and one free code site per coarse edge at position `p` along it: the code sites of the `s`-cell are `(p,0,0)`, `(0,p,0)`, `(0,0,p)` and every other
site is a pinned marker site, with marker values constant on the orbits of the space-group stabiliser of the code sublattice -- `24` rotations at the midpoint `p = s/2`, `C3` otherwise -- so an
**assignment** is one bit per marker orbit.

A **state-reading frustration-free star template** is a positive semidefinite operator `h` on the seven-site star, identical at every site, whose kernel contains the intended role-star states; the
canonical maximal choice is `h = 1 - Pi_K` with `K` the span of those states, and any other template of the class has a kernel at least as large. The zero space of `H = sum_s h_s` is the
intersection of the star kernels, and **junk** here is a zero-energy state outside the span of the intended global states. The **EVEN** variant restricts the free bits around a pinned centre to
even parity; the **FULL** variant does not. On a torus with a side of length `2` the `+` and `-` neighbours along that axis are the same physical site, and the star term is the pullback `h = 1 -
V^dag Pi_K V` through the **diagonal isometry** `V : |b> -> |bb>` on that slot pair.

## Theorem 1 -- the star-pattern orbits, and the spacing-2 vacuity restated

**Conclusion.**

1. The `24` proper rotations and the `48`-element full cubic group induce the **same** `20` orbits on the `128` seven-bit star patterns, with identical canonical representatives. Hence every
   rotation-invariant value-reading star rule is automatically invariant under the full group, inversions included, and no rule of this class distinguishes a pattern from its mirror image.
2. At spacing `2`, on the `4x4x4` torus, the `48` templates of the period-`(4, 2, 2)` role pattern give every corner site six free code neighbours; the corner stars realise all `128` value
   patterns and all `4` adjacent value pairs, so the maximal value-reading star rule at that spacing accepts everything.

**Proof.** Item 1 canonicalises all `128` patterns under both permutation groups of the six neighbour slots and compares the tables entry by entry. Item 2 builds the `48` templates as arrays on
the torus, counts the free neighbours of every pinned site, and enumerates the realised star patterns and adjacent pairs. Both exact.

**Reading, not theorem.** A rule that sees only the seven values around a point has no way to tell left from right. And where every neighbour of a pinned site is free, the seven values around that
site take every arrangement there is, so a rule reading them alone has nothing to reject.

## Theorem 2 -- value-reading star rules on spaced superlattices

**Conclusion.** For the spaced superlattices `s = 3` with both code positions (`10` marker orbits, `1024` covariant assignments each) and `s = 4` midpoint (`9` orbits, `512` assignments):

1. **Zoom-out lemma.** The maximum number of code neighbours of any site is `3` at `s = 3` and `1` at `s = 4` midpoint -- never `6`. No site has an all-code star, so the vacuity of Theorem 1 item
   2 does not apply at either spacing, and any failure below has a different mechanism.
2. The maximal rule accepts its own intended configurations and is covariant: penalty `0` for all `2560` assignments with every code filling, and for `48` sampled assignments over every rotation
   and translate as well. Accepted set sizes span `28`-`111`, `28`-`111` and `8`-`69` of `128`, and `0` assignments are vacuous.
3. The uniform-configuration filter is sound -- if some intended star can be made all-`0` or all-`1` by the code bits, that uniform configuration has penalty `0` and is no translate -- and its
   pass counts are `282/1024`, `282/1024` and `32/512`.
4. For every one of the `2560` assignments there is junk on the `s`-torus: `1024`, `1024` and `512` admit it and `0` are junk-free, in `38590` and `16363` branch nodes, at most `133` and `301` for
   a single assignment. The period multiset census of the lexicographically least witness is `489x(3,3,3) 438x(1,1,1) 73x(1,3,3) 24x(1,1,3)` at `s = 3`, the same for both code positions, and
   `321x(1,1,1) 37x(1,2,2) 36x(2,2,2) 33x(1,1,2) 31x(1,1,4) 17x(4,4,4) 15x(1,4,4) 11x(1,2,4) 8x(2,2,4) 3x(2,4,4)` at `s = 4`.
5. Each of the `2560` witnesses tiles to the `2s`-torus, `6^3` and `8^3`, with penalty `0`, and is still no translate or rotation of the intended pattern, so the junk survives the doubled box.

**Proof.** Items 1 to 3 are direct enumerations over the cell and over every assignment. Item 4 is a complete branch-on-first-undetermined-site constraint propagation: at each node the star
constraints are propagated to a fixed point through a lookup of the accepted-pattern set against the known slot bits, a conflict closes the branch, and a completed configuration is either an
intended translate -- and the search continues -- or a witness, whose penalty is recomputed from scratch and whose distinctness from every translate and rotation is checked site by site. Branching
`0` before `1` makes the first witness the lexicographically least one, so the census is a property of the rule and not of a solver. No SAT solver and no external solver is used anywhere. Item 5
tiles each witness and recomputes penalty and distinctness on the doubled torus. All exact.

**Reading, not theorem.** A rule that looks only at a site and its six neighbours can forbid local arrangements. On every box here it does not force a pattern that repeats every three or more
sites: some other repeating pattern always fits, most often a flat one, sometimes a columnar or layered rival with a shorter period along one axis, and the census is the shape of that. The wider
spacing removes the earlier vacuity; what replaces it has a different name.

## Theorem 3 -- the aliasing lemma for state-reading templates

**Conclusion.**

1. On a torus with a side of length `2` the two `+-` neighbour slots along that axis are the same site, so the star term is the pullback `h = 1 - V^dag Pi_K V`, and the image of the diagonal
   isometry `V` on that slot pair is `span{|00>, |11>}`. The intended star state carries the pinned product `|p>|p>` there, and for `|p> = a|0> + b|1>` that product lies in the diagonal subspace
   exactly when `ab = 0`, that is, exactly for the `Z` eigenstates. For any other pin `V` delivers an entangled diagonal vector instead, and the intended state is a zero mode only if `K` happens
   to contain it. Which pins that happens for is item 2, not a consequence of item 1.
2. On the `2D` `4x2` torus, of the `72` (pin pair, variant) cases, `30` are vacuous -- exactly the `FULL` variant at all `30` pairs with `v != f` -- and of the `42` live cases `22` are faithful,
   meaning the intended states really are zero modes, and `20` are not. The `20` are exactly those with neither pin a `Z` eigenstate.

**Proof.** Item 1 is two lines of algebra on the expansion of `|p>|p>`, checked on all six named pins. Item 2 constructs `Pi_K` by singular value decomposition on the `32`-dimensional star space,
compresses it through the isometry, assembles the dense `256x256` Hamiltonian, and evaluates the intended states directly. All exact.

**Reading, not theorem.** When a box is only two sites wide, a site's two neighbours in that direction are one and the same, so the template asks for two copies of one value at once, and only a
definite value is two copies of itself. That is a fact about the small box, and it is why the three-dimensional rows below keep to definite-value pins.

## Theorem 4 -- two dimensions

**Conclusion.**

1. Exact, `4x2` torus, at the faithful `Z` pins: `v = f = |0>` gives `dim K = 17`, nullity `35` against `23` intended, so `12` junk zero modes in `EVEN` and `4` in `FULL`; `v = |0>`, `f = |1>`
   gives `dim K = 24`, nullity `64` against `28`, so `36` junk. No faithful pin choice on this torus is junk-free.
2. Matrix-free, `4x4` torus, no aliasing, state vectors of length `65536` [numerical, seed fixed]: alternating projections from a random start reach residual energy at most `9e-14`, and the
   converged zero-energy vectors carry junk fraction -- weight outside the intended span -- `0.85`-`0.89` at `(+,+)` `EVEN`, `0.31`-`0.33` at `(+,+)` `FULL`, `0.91`-`0.92` at `(0,1)` `EVEN`,
   `0.65`-`0.67` at `(+,-)` `EVEN` and `0.78`-`0.84` at `(0,+)` `EVEN`.
3. Hutchinson kernel-dimension estimates from the same runs, `4` probes, one standard error [numerical, stochastic, seed fixed]: `743+-13`, `743+-13`, `1534+-22`, `399+-7` and `690+-17` against
   `96`, `511`, `124`, `128` and `128` intended.

**Proof.** Item 1 is dense and exact on `8` qubits. Item 2 applies each star's kernel projector in turn to a block of random vectors, never forming a matrix larger than `32x32` and never storing
more than `65536 x 4` amplitudes; the residual energy of the converged block is reported, and the weight inside the intended span is computed against the Gram matrix of the intended product
states, so that span is never materialised either. Item 3 reads the Hutchinson estimator off the same block, the overlap of each start vector with its own limit estimating the diagonal of the
kernel projector; it is stochastic and reports its standard error.

**Reading, not theorem.** The template is satisfied by far more than the arrangements it was built from, and what sits in the extra room is not another arrangement but a blend of several.

## Theorem 5 -- three dimensions

**Conclusion.**

1. Exact: over all `64` pin triples from `{0, 1, +, -}` and both variants, the `3D` seven-site star has `dim K` between `51` and `76` of `128` in `EVEN` and between `65` and `105` in `FULL`, so no
   template of this family is vacuous; and all `16` all-`Z` triples are faithful on the `4x2x2` torus.
2. Matrix-free, `4x2x2` torus, `Z` pins [numerical, seed fixed]: junk fraction `0.56`-`0.62` at `(0,0,0)` `EVEN`, `0.53`-`0.54` at `(0,0,0)` `FULL`, `0.74`-`0.76` at `(0,1,0)` `EVEN` and
   `0.89`-`0.90` at `(0,1,1)` `EVEN`, with residual energy at most `1e-15` and intended-state energy at most `2e-15`; the Hutchinson estimates are `451+-9`, `756+-16`, `988+-18` and `2260+-14`
   against `173`, `349`, `252` and `244` intended [numerical, stochastic, seed fixed].

**Proof.** Item 1 is exact singular value decomposition on the `128`-dimensional star space, once per triple and variant, with a direct evaluation of the intended states. Item 2 uses the same
matrix-free apparatus as Theorem 4 item 2 on a `16`-qubit torus, the aliased stars compressed through the isometry first.

**Reading, not theorem.** The same extra room appears in three dimensions as in two, and the small size of the star is not what opens it: every template here rejects something, and none of them
rejects the blends.

## Theorem 6 -- what the junk is, and the one-dimensional contrast

**Conclusion.**

1. [numerical, matrix-free, seed fixed] One `2D` and one `3D` junk vector, extracted by removing the intended-span component from a converged zero-energy vector, have energy at most `2e-15` and
   weight inside the intended span at most `7e-31`. Their Schmidt rank across a half cut is `35` and `31` of a possible `256`, and every single-site reduced state is mixed, with purity at most
   `0.661` and `0.725`. No site is pinned to any value.
2. Exact: the one-dimensional analogue -- three-site stars on an `8`-ring -- is junk-free at the `Z` pins in the `EVEN` variant, `dim K = 3` and nullity `3` against `3` intended states. The `|+>`
   and `|->` pins in `EVEN` give nullity `9` against `4`, and every `FULL` choice gives `47` against `31`. Two of the eight choices are junk-free.

**Proof.** Item 1 reshapes the normalised junk vector into a bipartite matrix across a half cut and takes its singular values, and traces out all but one site for each site in turn. Item 2 is
dense and exact on `8` qubits.

**Reading, not theorem.** The extra states are superpositions in which a site carries two roles at once, spread across the whole box rather than concentrated anywhere. A template of this kind has
a subspace for a kernel, and a subspace holds the sums of the arrangements it was built from as well as the arrangements themselves; in one dimension the sums are the arrangements again, and there
the same construction leaves nothing over.

## Corollary -- what the two classes give, on the clusters tested

Within the setting declared above, and on the finite clusters named:

1. On the classes and clusters tested, no junk-free rule was found -- by exhaustive enumeration and exact linear algebra where the theorems say exact, and by matrix-free evaluation where they say
   numerical. A star-local rule of either kind does not, on these clusters, select a superlattice role pattern with free code sites.
2. The two mechanisms are different and both are named. Value-reading rules fail by **period collapse**: a predicate on seven values can forbid local arrangements, and on every box here it does
   not impose a period of three or more. State-reading frustration-free templates fail by **superposition junk**: their kernels are subspaces, and a subspace holds the sums of the intended
   arrangements as well as the arrangements.
3. PR #7834's open item is therefore answered negatively for these two classes, on these clusters, and stays open for others: energetic or otherwise non-frustration-free selection; larger
   direct-dependence windows; templates reading more than one star; and rules on the pre-record possibility state other than the projector complements used here. The zoom-out meanwhile does what
   it was meant to: the spacing-2 vacuity of Theorem 1 item 2 is defeated at every spacing here, no site having an all-code star, and the class still admits junk for an unrelated reason.

**Reading, not theorem.** A rule that looks only at a site and its six neighbours can forbid local arrangements, but on every box here it could not force a pattern that repeats every three or more
sites: some other repeating pattern always slipped through. A rule that looks at the possibilities at those sites rather than their values lets mixtures of two roles through instead. Neither
result says a nearby-only rule is unavailable; they say these two kinds are not it.

## What does not move

- This decides nothing about what the framework's law is. It declares two rule classes, of a form Admissibility permits in shape, and computes what they select. It supplies no update rule, no
  formation site, no formation rate, and no values, and no coupling, absolute unit or dynamical clause appears anywhere.
- It says nothing about rules outside the two classes, about clusters larger than those named, or about the `48`-sector zero set of PR #7834, which is not contradicted anywhere here.
- No axiom text is amended, extended, reworded, or reinterpreted, no hypothesis is adopted, and no status value is set, predicted, or implied. No premise registry, citation manifest, or
  axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

- **Energetic selection.** Both classes here are frustration-free. A rule that pays energy for the wrong arrangement rather than forbidding it outright is untouched by Theorems 2 and 4 to 6, and a
  lane taking it up should treat the period census of Theorem 2 item 4 as the rival arrangements its gap has to lift.
- **Larger windows.** The direct dependence here is one star; a `3x3x3` or `5x5x5` window read as a constraint on values is a different class, and PR #7834 supplies a member of it. A single term
  supported on two adjacent stars, or a product of star terms, is likewise outside Theorems 3 to 6.
- **The possibility-state reading beyond projector complements.** `h = 1 - Pi_K` is the maximal frustration-free choice with the intended states in its kernel; a term that reads the possibility
  state without being a projector complement -- a positive operator with a smaller kernel and a nonzero value on the intended states, or a non-frustration-free sum -- is not covered.
- **Larger tori for the three-dimensional state-reading case.** The `4x2x2` torus aliases two axes, which is why only `Z` pins are faithful there; a non-aliased three-dimensional torus needs
  `4x4x4`, `64` qubits, and is not reached by the apparatus here.

## Remaining live routes

1. Spacings and code positions beyond those claimed: the `s = 4` off-midpoint superlattice with its `23` marker orbits, and `s = 5` and `s = 6`.
2. Other intended arrangements, and the gap between the two classes. Every result here is about the role patterns of PR #7834 and their spaced analogues, and a rule reading values on some sites
   and possibility states on others is neither class.
3. Whether the period collapse of Theorem 2 has a proof rather than a census: the runner exhibits junk for every assignment, and no general argument is offered.

## Executable claim block

The canonical machine-bound restatement of the six theorem conclusions.

```text
setting: one qubit per site of Z^3; ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md; nothing derived from them
class_1_value_reading: a rotation-invariant predicate on the 7 recorded Z-values of a star; penalty = number of rejected stars; maximal rule = accept every star pattern realised in the intended configurations over all free-site fillings. class_2_state_reading: a PSD operator h on the 7-site star, identical at every site, with the intended role-star states in ker h; canonical maximal choice h = 1 - Pi_K; zero space of sum_s h_s = intersection of star kernels
star_pattern_orbits: ROT24 and the full 48-element cubic group induce the same 20 orbits on the 128 patterns, identical canonical representatives; every rotation-invariant star rule is inversion-invariant. spacing_2_vacuity: 48 templates of period (4,2,2) on the 4x4x4 torus; every corner has 6 free code neighbours; corner stars realise 128 of 128 value patterns and 4 of 4 adjacent pairs; maximal rule vacuous
spaced_superlattice_geometry: s=3 p=1 and p=2 |G_pt|=3, 10 marker orbits, 11 star masks, at most 3 code neighbours; s=4 p=2 |G_pt|=24, 9 orbits, 10 masks, at most 1; never 6
spaced_superlattice_acceptance: penalty 0 on all 2560 assignments with every code filling, and on 48 sampled assignments over every rotation and translate; |A| spans 28-111, 28-111, 8-69 of 128; 0 vacuous; sound uniform filter passes 282/1024, 282/1024, 32/512
junk_search: exhaustive branch-on-first-undetermined-site constraint propagation, no SAT solver; 1024, 1024, 512 assignments admit junk on the s-torus; 0 junk-free; 38590 and 16363 branch nodes, at most 133 and 301 for one assignment
period_census_s3: 489x(3,3,3) 438x(1,1,1) 73x(1,3,3) 24x(1,1,3), identical at p=1 and p=2, intended (3,3,3); witness = lexicographically least
period_census_s4: 321x(1,1,1) 37x(1,2,2) 36x(2,2,2) 33x(1,1,2) 31x(1,1,4) 17x(4,4,4) 15x(1,4,4) 11x(1,2,4) 8x(2,2,4) 3x(2,4,4), intended (4,4,4)
doubled_box: all 2560 witnesses tile to 6^3 and 8^3 with penalty 0 and are still no translate or rotation
aliasing_lemma: side length 2 identifies the two +- slots; h = 1 - V^dag Pi_K V; image of V on that pair = span{|00>,|11>}, holding |p>|p> iff ab = 0; 4x2 torus 72 cases, 30 vacuous (FULL at all 30 pairs with v != f), 42 live, 22 faithful, 20 not, the 20 being exactly those with neither pin a Z eigenstate
two_d_exact: 4x2 torus, v=f=|0> dim K 17, nullity 35 vs 23 intended, junk 12 EVEN and 4 FULL; v=|0> f=|1> dim K 24, nullity 64 vs 28, junk 36; 0 faithful choices junk-free
two_d_matrix_free: 4x4 torus, vectors of length 65536, residual energy at most 9e-14; junk fractions 0.85-0.89, 0.31-0.33, 0.91-0.92, 0.65-0.67, 0.78-0.84 at (+,+) EVEN, (+,+) FULL, (0,1) EVEN, (+,-) EVEN, (0,+) EVEN [numerical]
two_d_hutchinson: 743+-13, 743+-13, 1534+-22, 399+-7, 690+-17 against 96, 511, 124, 128, 128 intended, 4 probes [numerical, stochastic, seed fixed]
three_d_exact: 7-site star, 64 triples from {0,1,+,-}, dim K 51-76 of 128 EVEN and 65-105 FULL, none vacuous; all 16 all-Z triples faithful on 4x2x2
three_d_matrix_free: 4x2x2, Z pins, junk fractions 0.56-0.62, 0.53-0.54, 0.74-0.76, 0.89-0.90; Hutchinson 451+-9, 756+-16, 988+-18, 2260+-14 vs 173, 349, 252, 244; residual at most 1e-15 [numerical]
junk_character: energy at most 2e-15, weight inside the intended span at most 7e-31, Schmidt rank 35 and 31 of 256, single-site purity at most 0.661 and 0.725; no site pinned [numerical]
one_d_contrast: three-site stars on an 8-ring; Z pins EVEN junk-free, dim K 3, nullity 3 = 3 intended; |+>/|-> EVEN nullity 9 vs 4; FULL 47 vs 31; 2 of 8 junk-free
not_claimed: s=4 off-midpoint (23 orbits), s=5, s=6, and Haar-random pins; scratch-only, sampled or solver-checked, and claimed nowhere here
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=17 FAIL=0
```

## Proof boundary

The two classes are **finite and named**, and nothing here extends past them. Class 1 is value-reading star rules; class 2 is frustration-free star templates of the form `h = 1 - Pi_K`. A rule
that pays energy rather than forbidding, a rule reading a wider window, a term supported on more than one star, and a possibility-state term that is not a projector complement are each outside
both classes and are named in "Interfaces" for that reason. The clusters are **finite and named**: the `4x4x4` torus for Theorem 1; the `3^3`, `4^3`, `6^3` and `8^3` tori for Theorem 2; the `4x2`
and `4x4` tori for Theorems 3 and 4; the `4x2x2` torus and the `7`-qubit star for Theorem 5; the `4x4` and `4x2x2` tori and the `8`-ring for Theorem 6. Nothing is claimed for infinite lattices or
larger boxes.

Three superlattice families were examined in scratch and are **not claimed**: `s = 4` off-midpoint with `23` marker orbits, `s = 5`, and `s = 6`. At `s = 6` midpoint the scratch pass covered
`9501` of the `10090` uniform-filter survivors and the `s = 4` off-midpoint pass sampled; both used a SAT solver that is not a repository dependency, and neither is reproduced by the runner or
asserted anywhere here, as the Haar-random pin templates of the state-reading class are likewise scratch-only. Where this note says exhaustive it means exhaustive in the runner, over the
assignment space stated. The junk **census** is a property of a stated witness rule, not of a solver: branching value `0` before `1` on the first undetermined site makes the returned witness the
lexicographically least zero-penalty non-intended configuration, and a different witness rule gives a different census with the same totals -- `2560` of `2560` admitting junk, `0` junk-free --
which is what the conclusion rests on.

Three lines are **numerical**, and every one is tagged in the runner: the matrix-free `4x4` and `4x2x2` rows, and the junk-character row. Each reports the converged residual energy of its
zero-energy vector, at most `9e-14`, and the weight of that vector outside the intended span. Two of those lines are additionally **stochastic** -- the Hutchinson kernel-dimension estimates -- and
fix their seed and report a standard error; no conclusion here depends on a Hutchinson number, which is why they are reported as estimates and used nowhere else. The exact lines use integer and
bit arithmetic, exhaustive enumeration, exhaustive constraint propagation, and dense linear algebra on spaces of dimension at most `256`. Nothing here is derived from the four axioms: they are
quoted in "Setting" to fix the lattice, the one-qubit site, the covariance and the record, and the two rule classes are declared, not deduced. No claim is made about the framework's law, and PR
#7834's construction is not contradicted; its rule reads a `5x5x5` window, outside both classes tested here.

## Review record

An honest auditor should come away with: two finite negative results on two named classes, over named finite clusters; two named mechanisms, period collapse and superposition junk; one junk-free
contrast in one dimension, which shows the failure is not an artefact of the construction; a clearly marked line between the exact and the numerical and between the numerical and the stochastic;
and a list of what stays open, headed by energetic selection and wider windows. The strongest thing this note says is that two kinds of adjacent-site rule, on the boxes named, have no junk-free
member; it does not say that a rule of adjacent-site direct dependence is unavailable, and no sentence here should be read that way.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the two context notes in "Imports and authority" are
plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=17 FAIL=0` with runtime under the declared `300` seconds and stdout
under `5500` characters, and passing repository pipeline, strict-lint, and changed-evidence gates; independent audit remains a separate lane.
