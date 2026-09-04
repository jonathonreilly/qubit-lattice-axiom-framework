---
claim_id: support_conditions_confine_shifting_record_groups
claim_type: bounded_theorem
claim_scope: "On three declared finite objects -- (a) the cubic lattice Z^3 with nearest-neighbour adjacency, exhaustively over every fixed polycube up to n = 6 records and the whole reachable set of each; (b) the 2x2x2 cube graph (8 corners, 12 edge sites, 6 faces) with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, over all 4096 record patterns; and (c) the coarse L^3 torus carrying one-particle hopping with Kogut-Susskind staggered (pi-flux) link signs, unit amplitude, unit spacing and coordination 6, at L = 6 and L = 8 for two records -- under TWO STIPULATED SUPPORT CONDITIONS and THREE STIPULATED TICK MODELS declared here in full and derived from nothing: C_comp, every record has at least one adjacent record; C_rig, every pair of records adjacent now stays adjacent (with an isometry form); K1, one record shifts one site per tick, uniformly over the admissible shifts; KS, every member shifts at once, under a STRICT or a PERMISSIVE occupancy convention; KT, the pre-record amplitude runs for a time tau and the odds are its weights conditioned on the admissible set -- PR #7889's M2 registration with a support condition in place of that note's energy cost. (T1) [exact] Z^3 is bipartite, so two distinct neighbours of a site are never adjacent and for every shift x -> y the neighbour sets N(x), N(y) are disjoint (0 violations over the 1296 shifts of the L = 6 torus and 6480 ordered neighbour pairs): a record that shifts one step loses EVERY former companion at once. (T2) [exact] Under C_comp and K1 the exhaustive polycube census (fixed polycubes 1, 3, 15, 86, 534, 3481 at n = 1..6; reachable sets 3, 15, 86, 990, 11851 mod translation at n = 2..6 carrying 0, 24, 192, 3372, 52320 admissible shifts) gives: the dimer, the straight trimer, the straight-4 and the 2x2 square are FROZEN while the bent trimer carries 2 shifts and the tripod 6; no one-record group is admissible at all, so a record is never alone; record number is conserved exactly; a group of size <= 4 can never split, while at n = 5 there are 336 splitting shifts whose parts always hold >= 2 records, and merges are as many; and the CAGE theorem -- for n = 3, 4, 5, 6 an exact RATIONAL potential Phi of the SHAPE satisfies CoM(s') - CoM(s) = Phi(s') - Phi(s) at every admissible shift, 0 inconsistencies over 24/192/3372/52320 shifts and 6/13/34/40 components, with within-component spread 1/3, 1/2, 4/5, 4/3 lattice units -- so the lab centre of mass takes finitely many values and D_group = 0 EXACTLY: the group rattles in a cage and does not walk, the bent trimer occupying three corners of one FIXED unit square forever. (T3) [exact] Under C_rig a one-step shift is frozen outright (0 admissible over all 104 connected groups of size 2, 3, 4); under the SIMULTANEOUS tick KS with STRICT occupancy the only admissible whole-group moves are RIGID UNIT TRANSLATIONS (0 non-translations over 8 named groups), and the isometry form with PERMISSIVE occupancy adds exactly the rigid rotations and reflections (all 160 admissible assignments over 10 groups land on a congruent copy, 0 violations). The occupancy convention is load-bearing: PERMISSIVE admits all 6 unit translations so D_group = D_1 EXACTLY, while STRICT blocks the longitudinal directions -- dimer 4/6, bent trimer 2/6, 2x2x2 block 0/6. (T4) [exact] On the cube the 4096 record patterns split into 128 parity sectors of 32, each sector's membership being a support condition on record patterns. In the vacuum sector no single edge-record complement is admissible (0 of 12); the sector-preserving complement sets form a 5-dimensional subspace of 32 elements with weight census {0: 1, 4: 6, 6: 16, 8: 9} that is EXACTLY the span of the six face 4-cycles and EXACTLY the cube's cycle space, so admissible vacuum moves are CLOSED LOOPS only. In a one-pair sector the admissible single complements are exactly the edges incident to exactly one of the two odd corners (0 mismatches over 28 pairs; 4 hops plus 1 annihilation at distance 1, 6 hops at distances 2 and 3), each hop changing the VALUE of exactly one edge record and moving exactly one odd corner: the star does not translate, the odd corner does. All 24 adjacent two-edge complements leave the vacuum sector. (T5) [numerical, 1e-3] Under KT a pair held by a HARD ADJACENCY support condition on the L = 6 and L = 8 pi-flux tori -- 22572 and 129280 non-adjacent two-record configurations carrying odds 0, leaving 648 and 1536 admissible, the tick kernel translation covariant to 1.9e-16 -- stays adjacent at every tick with certainty and still moves: D_pair/D_1 = 0.5016 and 0.5075 at tau = 0.5, 0.1058 and 0.1453 at tau = 1, against the independent-record value 1/2; the odds on the admissible set before renormalising are 0.31 at tau = 0.5 and 0.28 at tau = 1; the orientation is a 3-state chain with stationary odds exactly (1/3, 1/3, 1/3) and P(the axis changes) 0.476 at tau = 0.5 and 0.072 at tau = 1; and the joint-move census at L = 8, tau = 0.5 reads one record shifts 0.540, rigid translation 0.239, same sites 0.218, non-rigid 0.002. The same torus under PR #7889's ENERGY COST g = 32 and no support condition carries P(adjacent) 0.978 -> 0.424 over 40 ticks toward the uniform 0.0279. This note declares support conditions and tick models and computes with them; nothing is derived from any axiom, no formation clause is supplied, no axiom is amended, no status is set, and no claim is made about what the framework's tick is or about which conditions the framework's law carries."
upstream_dependencies: []
runner: scripts/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.py
---

# Support conditions confine groups of shifting records; energy costs do not

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.py`](../scripts/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.txt`](../logs/runner-cache/support_conditions_confine_groups_of_shifting_records_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`SHIFTING_POSITION_RECORDS_EXACT_DIFFUSION_LAW_AND_THE_UNIFORM_ATTRACTOR_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7889) showed that two records held together by an
**energy cost** come apart at every cost, and named as an interface the mechanism it did not test: a **support condition** of the law, whose parting configurations carry
odds `0` and are never registered. This note answers that interface. It writes two support conditions down, computes exhaustively what they do to a group of shifting
records, and finds a sharper answer than either "they hold" or "they fail": the confinement is exact and absolute, and on this lattice it is a **cage** rather than a
vehicle unless the tick reaches further than one site.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-object theorems -- the bipartite census on the L = 6 torus, the exhaustive polycube census and reachability closure to n = 6 records, the exact Fraction coboundary certificate over 55908 admissible shifts, the simultaneous-shift and isometry enumerations, and the 4096-pattern parity census on the cube -- together with deterministic double-precision evaluations of exactly specified quantities on the L = 6 and L = 8 pi-flux tori, tagged [numerical] at stated thresholds. There is no sampling, no seed and no random number anywhere in the runner."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Route to its owner the one question this note raises and does not decide: whether the framework's actual law carries a support condition that moves a composite rigidly, which on the results below requires either a tick whose amplitude reaches beyond one site or a condition stated on simultaneous whole-group moves."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`: `T1` (`A`) the bipartite lemma; `T2` (`B`) the companion condition;
`T3` (`C`) the rigid condition; `T4` (`D`) the cube's parity sectors; `T5` (`E`) the hard-adjacency pair. Groups `A`-`D` are **exact**: integer, `F2` and `Fraction`
arithmetic with no floating point in the statement. Group `E` is a **deterministic double-precision evaluation** of exactly specified quantities at the thresholds printed
in its tags: the propagator `exp(-i tau H)` is transcendental, so no rational value exists to compare against, but there is **no sampling, no seed and no random number
anywhere in this runner**. No line is a witness.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kogut-Susskind staggered link signs, polycube enumeration, reachability closure and the Markov-additive martingale decomposition of a functional's variance are standard methodology; every object is redeclared here and the runner recomputes every statement. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight: `SHIFTING_POSITION_RECORDS_EXACT_DIFFUSION_LAW_AND_THE_UNIFORM_ATTRACTOR_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7889 -- whose `M2` registration is the `KT`
tick reused here, whose `T5` energetic pair is the contrast recomputed in `T5` below, and whose "support-conditioned shifts" interface this note answers),
`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7858 -- the same cube, encoding and parity cosets),
`RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7876 -- the frozen-record tick convention), and
`MINIMAL_AXIOMS_2026-06-29.md`, from which the axiom text in "Setting" is quoted verbatim. This note cites no grade of any of these and consumes no ledger row.

## Setting

The framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site." "No site is privileged." **Qubit / Site Possibility**: "Each site has a domain of local
possibilities."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each
site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Reading note (3), interpretive and
non-governing, quoted verbatim and in full:

> The distribution is a probability measure on the local possibility domain; "available"/"admissible" denotes its support -- on finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure; Record locks a supported realization.

That sentence is the whole hinge of this note. A **support condition** is a **zero of the law-level distribution** at a site given its neighbourhood: a configuration the distribution gives odds `0` is not admissible, so no record ever locks it. It is therefore a property of the **supplied law**, not an extra axiom and not a new primitive -- the axioms already permit a distribution with zeros, and this note stipulates two particular families of zeros to see what they do.

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are
permanent." "Only records are readable."

The owner's point, quoted on 2026-09-03 as the question this note answers on declared conditions and does not settle for the framework: **"neighbourhood conditions keep
records together through translation. Groups of records could be forced to translate together due to neighbourhood conditions"**.

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, and no graded or signed clause is used anywhere. The **record
ontology** is used as declared: a record at a site **registers** a value there; it does not report one the site already had. Reading note (2) says the axioms supply no
formation site, probability or rate, and this note **stipulates** its conditions and ticks rather than deriving any.

## The stipulated conditions and tick models, declared in full

Two support conditions and three ticks, all declared here, none derived. A lane proposing a different condition or tick inherits the obligations of `T2`-`T5` and none of
these choices.

1. **`C_comp` the companion condition.** Every record has at least one adjacent record. Every configuration with a lone record carries odds `0`. This is the weakest
   condition that makes "records stay together" mean anything at all.
2. **`C_rig` the rigid condition.** Every pair of records adjacent now stays adjacent. Its **isometry form** strengthens this to: every pair keeps its exact separation.
   This is the strongest reading of "forced to translate together".
3. **`K1` the one-step tick.** Each tick exactly one record shifts to a nearest-neighbour site, with uniform odds over the admissible shifts. Uniformity is a choice of
   convention and every `[exact]` statement below -- what is admissible, what is conserved, what is reachable, and the coboundary certificate -- is independent of it.
4. **`KS` the simultaneous tick.** Each tick every member of the group shifts at once, by one site or not at all. Two occupancy conventions are computed separately:
   **STRICT**, a target site must be vacant in the OLD configuration, and **PERMISSIVE**, a site vacated in the same tick counts as vacant.
5. **`KT` the tau-tick.** The pre-record amplitude runs for a time `tau` and the odds are its weights **conditioned on the admissible set** and renormalised. This is
   exactly PR #7889's `M2` registration with a **support condition** in place of that note's **energy cost**, so the two mechanisms are compared on one tick and one
   torus.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P5`.

`P0` (declared here): `Z^3`, the cube, the coarse torus, and the conditions and ticks above. `P1` (`A`): the bipartite lemma. `P2` (`B`): `C_comp` under `K1`. `P3` (`C`):
`C_rig` under `K1` and `KS`. `P4` (`D`): the cube's sectors. `P5` (`E`): the hard-adjacency pair under `KT`.

## Definitions

A **group of records** is a finite set of occupied sites of `Z^3`. A **fixed polycube** of size `n` is a connected such set modulo translation; the **reachable set** of
`n` is the closure of all of them under the admissible shifts of the condition in force, again modulo translation. `CoM(S)` is the arithmetic mean of the occupied sites,
and `D_1` is the diffusion constant of one free record: `E|dx|^2 = 1` and `D_1 = 1/6` per `K1` tick.

The **cube** is the `2x2x2` cube graph, corner `s = 4a + 2b + c`, `8` corners, `12` edge sites, `6` faces, one qubit per edge site, with `B_v` the product of the `Z`'s
on the edges incident to `v` and `star(v)` the edges incident to `v`. A record at an edge site registers a `Z`-value there, so a **finished set of records** is a vector
`y` in `F2^12`; the **parity dictionary** is `n_v(y) = (1 - B_v)/2 = |y intersect star(v)| mod 2`. A **sector** fixes every `B_v`, and sector membership is the support
condition: the `4096` patterns fall into `128` sectors of `32`, indexed by the set of **odd corners**, whose size is always even because `prod_v B_v = I`.

The **coarse torus** is `Z_L^3` with nearest-neighbour hopping of unit amplitude and unit spacing, coordination `6`, and Kogut-Susskind staggered (pi-flux) link signs
`eta(v, 1) = 1`, `eta(v, 2) = (-1)^{v_x}`, `eta(v, 3) = (-1)^{v_x + v_y}`. The two-record generator is the corresponding hopping on the `C(L^3, 2)` configurations with
the site-ordered exchange sign. `D_pair` is the asymptotic diffusion constant of the pair's centre of mass under `KT`, taken with the correlations of the orientation
chain included.

## Theorem 1 -- one step severs every companion

**Conclusion.** `[exact]` `Z^3` is bipartite by coordinate-sum parity: on the `L = 6` torus every one of the `1296` bonds joins opposite classes (`0` violations), so no
triangle closes and two distinct neighbours of a site are never adjacent (`0` violations over `6480` ordered pairs). Hence for every one of the `1296` shifts `x -> y` the
neighbour sets `N(x)` and `N(y)` are **disjoint** (maximum overlap `0`), and no former companion of `x` survives as a companion at `y` (`0` survivors).

**Proof.** Exhaustive integer enumeration over the sites, bonds and ordered neighbour pairs of the `L = 6` torus, whose girth `4` matches `Z^3`'s for this statement. No
floating point.

**Reading, not theorem.** This is the geometric fact everything below turns on. On this lattice a record cannot edge away from its neighbours: one step away from a site
is one step away from **all** of that site's neighbours at once. Whatever a condition asks a group to preserve, a single one-site shift breaks every adjacency the moving
record had.

## Theorem 2 -- the companion condition confines absolutely, and the cage is small

**Conclusion.** `[exact]` Under `C_comp` with the `K1` tick. **The census.** Fixed polycubes number `1, 3, 15, 86, 534, 3481` at `n = 1..6`; the reachable sets modulo
translation number `3, 15, 86, 990, 11851` at `n = 2..6` and carry `0, 24, 192, 3372, 52320` admissible shifts. By shape: the dimer, the straight trimer, the straight-4
and the `2x2` square are **frozen** (`0` shifts); the L tetracube carries `1`, the S and skew tetracubes and the bent trimer `2`, the T tetracube `4`, the tripod `6`.
**The invariants.** No one-record group is admissible at all, so a record is never alone; the record number is conserved at every shift (`0` violations); every reachable
group satisfies the condition (`0` violations). **Splitting.** A connected group of size `<= 4` can **never** split (`0` splitting shifts at `n = 2, 3, 4`); at `n = 5`
there are `336`, the witness `[(0,0,0),(1,0,0),(2,0,0),(3,0,0),(3,1,0)]` splitting into parts of sizes `2` and `3`; no part of any split at `n <= 6` holds fewer than `2`
records, and merges are exactly as many. **The cage.** For `n = 3, 4, 5, 6` an exact **rational** potential `Phi` of the **shape** satisfies
`CoM(s') - CoM(s) = Phi(s') - Phi(s)` at every admissible shift -- `0` inconsistencies over `24/192/3372/52320` shifts and `6/13/34/40` connected components of the shift
graph -- with within-component spread `1/3, 1/2, 4/5, 4/3` lattice units. Hence the lab centre of mass takes finitely many values and **`D_group = 0` exactly**. The bent
trimer's lab orbit is exactly `4` configurations inside one **fixed** unit square: three of that square's four corners, forever.

**Proof.** The censuses are exhaustive enumerations in integer arithmetic; the reachable sets are the closures of the polycube sets under the admissible shifts, taken
modulo translation, and the shift graph is undirected because the reverse of an admissible shift restores a configuration already known to satisfy the condition. The
potential is built by breadth-first assignment from one root per component with exact `Fraction` increments `(y - x)/n`, then **every** edge is re-checked against it, so
the certificate is a proof of exactness and not a fit. `Phi` is determined up to one additive constant per component, which is why the spread is taken **within** a
component; that spread bounds the whole lab excursion of the centre of mass, and a bounded centre of mass has diffusion constant `0` identically.

**Reading, not theorem.** Forbid a record from ever being alone and the owner's mechanism appears in its strongest form: the group is held together not approximately but
absolutely, because the shift that would break it carries odds `0` and is never registered. But by `T1` one step away is away from **all** companions at once, so the only
shifts left are the ones that find a **new** companion, and those turn out to trace a closed loop. The centre of mass is a function of the shape alone; the shape has
finitely many values; so the group never travels. It shuffles inside a box a little over one site wide. A bent trimer under this rule sits on three corners of one square
for all time, permuting which corner is empty.

## Theorem 3 -- the rigid condition freezes one-step shifts and makes simultaneous ones rigid

**Conclusion.** `[exact]` Under `C_rig`. **One-step shifts.** Summed over **all** `104` connected groups of size `2, 3, 4`, the admissible `K1` shifts number `0`: a
record with any companion cannot move alone. **Simultaneous shifts.** Under `KS` with **strict** occupancy the only admissible whole-group moves are **rigid unit
translations** -- `0` non-translations over the `8` named groups -- with `4, 4, 2, 2, 4, 2, 2, 0` of the `6` unit directions free, in the runner's declared order: the
dimer, the straight trimer, the bent trimer, the square, and the straight-4, L and T tetracubes, then the tripod. **The isometry form** with **permissive** occupancy adds exactly the rigid rotations and reflections: all `160` admissible
assignments over the `10` named groups carry the group to a **congruent** copy (`0` violations), of which `70` are pure translations, `7` per group. **The convention is
load-bearing.** Permissive occupancy admits all `6` unit translations from every group, so the centre of mass performs the free one-record walk and `D_group = D_1`
**exactly**; strict occupancy blocks the longitudinal directions -- dimer `4/6`, bent trimer `2/6`, `2x2x2` block `0/6`, giving `D_group/D_1 = 0.667, 0.333, 0.000`.

**Proof.** The one-step count enumerates every group, every record and every direction and tests the condition on every currently-adjacent pair. The simultaneous counts
enumerate all `6^n` or `7^n` assignments of unit steps to members, reject those that collide or that violate the occupancy convention, and keep those preserving every
current adjacency; the isometry count keeps those preserving every pairwise squared distance and then verifies the image against the `48`-element cubic point group
modulo translation. Under permissive occupancy the group's own translations are always admissible and the shape is unchanged, so the walk of the centre of mass is
literally the free single-record walk; under strict occupancy the admissible direction set is the same at every step, so the walk is i.i.d. on it and the ratio is the
count over `6`.

**Reading, not theorem.** Ask that nothing currently touching ever stops touching and a single record can no longer move at all. What is left is a group that steps as one
piece -- and then it travels exactly as fast as a single free record would, no faster and no slower. Whether it can step at all in a given direction depends on a
bookkeeping choice nobody has made yet: if a site being vacated this same tick counts as free, a dimer can move along its own axis; if it must have been free already, it
cannot, and a solid `2x2x2` block cannot move in any direction whatsoever. That choice is not decoration; it is the difference between a mobile composite and a
permanently pinned one.

## Theorem 4 -- the cube's parity sectors are worked support conditions

**Conclusion.** `[exact]` The cube's `4096` record patterns split into `128` parity sectors of `32`. **The vacuum.** In the sector with every `B_v = +1`, **no** single
edge-record complement is admissible (`0` of `12`): complementing one edge flips the parity at **both** its corners. The sector-preserving complement sets form a linear
subspace of `32` elements with weight census `{0: 1, 4: 6, 6: 16, 8: 9}`, and that subspace is **exactly** the span of the six face `4`-cycles and **exactly** the cycle
space of the cube graph, of dimension `E - V + 1 = 5`. So admissible vacuum moves are **closed loops** of edge-record complements: no record changes alone. **One pair.**
In a sector with `B_v = -1` at exactly two corners `u, w`, the admissible single complements are **exactly** the edges incident to exactly one of `u, w` (`0` mismatches
over the `28` corner pairs): `4` hops plus `1` annihilation at corner distance `1`, `6` hops at distances `2` and `3`. At every such hop exactly **one** edge record
changes its **value** and exactly **one** odd corner moves, to an adjacent corner. And all `24` adjacent two-edge complements -- the nearest thing to a rigid two-record
shift -- leave the vacuum sector.

**Proof.** Exhaustive enumeration in `F2` over the `4096` patterns, the `12` edge sites, the `128` sectors and the `28` corner pairs, with the dictionary evaluated by
popcount. The subspace is computed as `{w : y XOR w` lies in the sector for every `y` in it`}`, the face span by closing the six face `4`-cycles under `XOR`, and the
cycle space as the even-degree subsets; the three sets are compared as sets. No floating point.

**Reading, not theorem.** The emergent model already carries support conditions of exactly this kind, and they behave the way `T2` and `T3` describe. In the vacuum no
record can change on its own: changes come only as closed loops. Where a particle sits -- an odd corner -- a record can change alone, and when it does the particle steps
to the next corner. What moves is not the group of records around the corner, which stays exactly where it is, but the **parity pattern**: one value flips and the odd
corner is somewhere else. This is a worked instance of the general lesson, in a model nobody designed for the purpose.

## Theorem 5 -- a hard-adjacency pair, against PR #7889's energetic pair

**Conclusion.** `[numerical, 1e-9]` On the `L = 6` and `L = 8` pi-flux tori a support condition of **hard adjacency** gives odds `0` to all `22572` and `129280`
non-adjacent two-record configurations, leaving `648` and `1536` admissible; the tick kernel is translation covariant to `1.9e-16`, so the reduction to relative classes
is exact. `[numerical, 1e-3]` Under `KT` the pair stays adjacent at **every** tick with certainty -- the orientation chain's rows sum to `1` to `3.3e-16` -- and still
moves: `D_pair/D_1 = 0.5016` and `0.5075` at `tau = 0.5`, `0.1058` and `0.1453` at `tau = 1`, against the independent-record value `1/2`. The odds the law puts on the
admissible set before renormalising are `0.31` at `tau = 0.5` and `0.28` at `tau = 1`; the wrap mass on the centre-of-mass displacement is at most `1.5e-2` and the mean
drift, zero by symmetry, at most `1.0e-2`. `[numerical, 1e-9]` The orientation is a `3`-state chain on the relative axis with stationary odds exactly `(1/3, 1/3, 1/3)`
(deviation `7.8e-16`) and `P(the axis changes)` `0.475, 0.476` at `tau = 0.5` and `0.079, 0.072` at `tau = 1`. `[numerical, 1e-6]` The joint-move census at `L = 8`,
`tau = 0.5` from an axis-`1` pair reads **one record shifts** `0.540`, **rigid translation** `0.239`, **same sites** `0.218`, **non-rigid** `0.002`. `[numerical, 1e-6]`
The contrast: the same `6^3` torus under PR #7889's **energy cost** `g = 32` with no support condition carries `P(adjacent) = 0.978, 0.957, 0.896, 0.804, 0.648, 0.424` at
ticks `1, 2, 5, 10, 20, 40`, running toward the uniform-over-configurations value `0.0279`.

**Proof.** The two-record generator is built sparsely and never densified; one column is propagated per relative class by Krylov exponentiation, and translation
covariance -- verified entrywise against explicit lattice translations -- makes the relative class a Markov chain, so the reduction is exact rather than an approximation.
The centre-of-mass step variance is accumulated along that chain with the martingale correction that makes it the true asymptotic constant rather than a per-tick
variance. The energetic row adds the diagonal cost to the same generator and propagates the `111`-class chain of PR #7889 for `40` ticks. Torus wrap mass is reported and
is small wherever a row is tabulated.

**Reading, not theorem.** Give the law a genuine zero -- the two records are never registered apart -- and the pair is bound with certainty at every tick, which no energy
cost achieves at any strength. And it is not pinned: it diffuses at half the single-record rate, exactly as two independent records' centre of mass would. But look at how
it moves. Nearly all the weight is on one record shifting while the other stays, or on nothing moving at all; genuine rigid translation is under a quarter of it. The pair
travels the way a caterpillar does, by rearranging, not by stepping as one piece.

## Corollary -- what this says about the owner's point

Within the setting declared above, on the three named objects, and for the stipulated conditions and ticks alone:

1. **The mechanism is real and exactly characterisable.** A translation-covariant support condition whose members' conditions reference each other confines a group
   **absolutely**: the parting configuration carries odds `0`, is never registered, and no strength parameter can be turned down. `T2`'s coboundary certificate and `T5`'s
   `P(adjacent) = 1` are two forms of the same statement, and PR #7889's energy cost achieves neither at any `g`. The owner's reading of neighbourhood conditions is
   correct on the mechanism.
2. **But confinement is not transport, and the tick's reach is what separates them.** By `T1` a one-step shift on the bipartite cubic lattice severs **every** companion at
   once. So a companion-conditioned group under one-step ticks rattles in a cage -- `D_group = 0` exactly, a box `4/3` of a site wide at `n = 6` -- rather than walking.
   Rigid translation needs a **simultaneous whole-group** tick (`T3`), or a tick whose amplitude reaches beyond one site (`T5`, where the group does move, though mostly
   by rearranging). **The mobility of a bound group is set by how far a record can shift in one tick, not by the condition alone.**
3. **The emergent model is a worked instance.** By `T4` no record changes alone in the cube's vacuum -- changes come as closed loops or, where a particle sits, as the
   motion of an odd corner by one record changing value. The object that moves is the parity pattern, not the group of records that marks it. The general lesson is
   already visible in a model built for other reasons.
4. **Whether the framework's law carries such a condition is untested.** Nothing here derives a support condition from any axiom, and nothing here says which zeros the
   supplied distribution actually has. What the results do say is what such a condition would have to be paired with to move a composite rigidly: a further condition
   stated on simultaneous whole-group moves, or a gap scale large compared with the tick. That is a question for its owner and for the lane that fixes the tick.

## Reading, not theorem -- the whole thing in plain words

Forbid a record from ever being alone and it can never leave its companions; but on this lattice one step away is always away from all of them at once, so a small group
under that rule does not travel, it shuffles inside a box the size of a few sites. Let the whole group step together and it travels as one, exactly as fast as a single
record would. In the emergent picture the vacuum's records can only change in closed loops, and a particle moves by one record at a time changing value while the odd
corner it marks steps to the next.

## Interfaces named for other lanes, not settled here

- **The tick's reach.** Every frozen result above is a statement about **one-site** shifts. A tick reaching two sites, or moving several records at once, is a different object; `T3` and `T5` show two ways it changes the answer. What the framework's tick is remains open and untouched here.
- **The occupancy convention.** Whether a site vacated in the same tick counts as vacant decides whether a bound group can move along its own axis at all (`T3`). This is
  a convention, not a theorem, and this note computes both branches rather than choosing one.
- **Which conditions the actual law carries.** The two conditions here are stipulated. Reading note (3) makes support a property of the supplied distribution, so the
  question "does the framework's law have these zeros?" is a question about the law and is not asked here.
- **Larger groups and other conditions.** The exhaustive census stops at `n = 6` records, the cube has `8` corners, and the tori are `L = 6` and `L = 8` with two records.
  Longer-range conditions, three-body conditions, and the thermodynamic limit are outside this note.
- **The fine-lattice marker sites.** Only edge sites carry records in the cube model. The coarse corner, face and cube-centre marker sites of the **superlattice role
  pattern** construction (open PR #7834) are pinned and are not part of these groups.

## Remaining live routes

1. Whether the `D_group = 0` cage of `T2` survives to arbitrary `n`, or whether some size admits a shape cycle whose centre-of-mass increments fail to close. The certificate is exact to `n = 6` and the component count is still growing.
2. Whether the joint-move census of `T5` -- rigid translation under a quarter of the weight at `tau = 0.5` -- has a `tau` at which rigid motion dominates.

## Executable claim block

The canonical machine-bound restatement of the five theorem conclusions.

```text
setting: (a) Z^3 with nearest-neighbour adjacency, exhaustively over fixed polycubes to n = 6 and the whole reachable set of each; (b) qubits on the 12 EDGE sites of the 2x2x2 cube graph, ordinary composition, superfast encoding, dictionary n_v = (1 - B_v)/2, all 4096 patterns; (c) the coarse L^3 torus, two-record hopping, KS staggered (pi-flux) signs, unit amplitude and spacing, coordination 6, L = 6 and L = 8; axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading note (3) quoted in full
conditions_and_ticks: STIPULATED -- C_comp (every record has >= 1 adjacent record); C_rig (every currently adjacent pair stays adjacent; isometry form: every pair keeps its separation); K1 (one record shifts one site per tick, uniform over admissible shifts); KS (all members shift at once, STRICT or PERMISSIVE occupancy); KT (the pre-record amplitude runs for tau, odds = its weights conditioned on the admissible set) = PR #7889's M2 with a support condition in place of that note's energy cost. A support condition is a ZERO of the law-level distribution; none is derived, and no formation site, probability or rate is taken from any axiom
T1_bipartite_lemma [exact]: Z^3 is bipartite by coordinate-sum parity (0 violations over the 1296 bonds of the L = 6 torus), so no triangle closes (0 over 6480 ordered neighbour pairs) and for every one of the 1296 shifts x -> y the sets N(x), N(y) are DISJOINT (max overlap 0, 0 surviving companions): one step severs every companion at once
T2_companion_condition [exact]: fixed polycubes 1, 3, 15, 86, 534, 3481 at n = 1..6; reachable sets 3, 15, 86, 990, 11851 mod translation at n = 2..6 with 0, 24, 192, 3372, 52320 admissible shifts; dimer/straight trimer/straight-4/2x2 square FROZEN, L 1, S 2, skew 2, bent trimer 2, T 4, tripod 6; NO one-record group admissible; record number conserved (0 violations); no split at n <= 4 (0 shifts), 336 at n = 5 with every part >= 2 records, merges as many; CAGE: an exact rational Phi of the SHAPE with CoM(s') - CoM(s) = Phi(s') - Phi(s), 0 inconsistencies over 24/192/3372/52320 shifts and 6/13/34/40 components, within-component spread 1/3, 1/2, 4/5, 4/3 -> D_group = 0 EXACTLY; the bent trimer's lab orbit is 4 configurations in one fixed unit square
T3_rigid_condition [exact]: 0 admissible one-step shifts over all 104 connected groups of size 2, 3, 4; under KS with STRICT occupancy 0 non-translations over 8 named groups (free directions 4, 4, 2, 2, 4, 2, 2, 0 of 6, for dimer, straight trimer, bent trimer, square, straight-4, L, T, tripod); the isometry form with PERMISSIVE occupancy gives 160 admissible assignments over 10 groups, all landing on a CONGRUENT copy (0 violations), 70 of them translations; PERMISSIVE gives D_group = D_1 EXACTLY, STRICT gives dimer 4/6, bent trimer 2/6, 2x2x2 block 0/6
T4_cube_sectors [exact]: 4096 patterns in 128 parity sectors of 32; vacuum admits 0 of 12 single edge-record complements; the sector-preserving sets are a 5-dim subspace of 32 with weights {0: 1, 4: 6, 6: 16, 8: 9} = the span of the six face 4-cycles = the cube's cycle space, so vacuum moves are CLOSED LOOPS only; in a one-pair sector the admissible single complements are exactly the edges incident to exactly one odd corner (0 mismatches over 28 pairs; 4 hops + 1 annihilation at distance 1, 6 hops at distances 2 and 3), each changing exactly 1 edge-record VALUE and moving exactly 1 odd corner; all 24 adjacent two-edge complements leave the vacuum sector
T5_hard_adjacency_pair [numerical, 1e-3]: on L = 6 and L = 8, 22572 and 129280 non-adjacent two-record configurations carry odds 0, leaving 648 and 1536; tick kernel translation covariant to 1.9e-16; P(adjacent) = 1 at every tick (rows sum to 1 to 3.3e-16); D_pair/D_1 = 0.5016, 0.5075 at tau = 0.5 and 0.1058, 0.1453 at tau = 1 against the independent 1/2; admissible-set odds 0.31 and 0.28; stationary orientation odds exactly (1/3, 1/3, 1/3) (7.8e-16), P(axis changes) 0.475, 0.476 at tau = 0.5 and 0.079, 0.072 at tau = 1; joint-move census at L = 8, tau = 0.5: one record shifts 0.540, rigid translation 0.239, same sites 0.218, non-rigid 0.002; CONTRAST, PR #7889's energy cost g = 32 with no support condition: P(adjacent) 0.978, 0.957, 0.896, 0.804, 0.648, 0.424 at ticks 1, 2, 5, 10, 20, 40 toward the uniform 0.0279
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=21 FAIL=0
```

## Proof boundary

Every statement above is proved on **declared finite objects**: the fixed polycubes of `Z^3` up to `n = 6` records and their reachable closures, the `2x2x2` cube graph
with its `4096` record patterns and `128` parity sectors, and the `L = 6` and `L = 8` pi-flux tori with two records and free hopping. Nothing is claimed for larger
groups, for the thermodynamic limit, for other lattices or flux conventions, or for any condition or tick other than the ones in "The stipulated conditions and tick
models". The coarse law is **designed**, not derived: the staggered sign convention is one pi-flux gauge among many and no minimality or uniqueness is claimed for it, and
the parity dictionary is one readout map among many.

**The two support conditions and the three ticks are stipulated in full and derived from nothing.** Reading note (3) makes support a property of the **supplied
distribution**, so stipulating a condition here is stipulating a law, not amending an axiom; reading note (2) is explicit that the axioms supply no formation site,
probability or rate, and this note supplies none either. **Nothing here says what the framework's tick is, and nothing forecloses any tick.** In particular `T2`'s
`D_group = 0` is a statement about **one-step** shifts under `C_comp`, and says nothing about a tick that reaches further; `T3`'s rigid translations are a statement about
**simultaneous** shifts under `C_rig`; and `T5` is a statement about one hard-adjacency condition under one registration convention. No no-go is asserted and none is
implied: every frozen count above is a property of a declared condition-and-tick pair, and a different pair is a different object.

The `[exact]` lines -- groups `A` through `D`, including the `Fraction` coboundary certificate -- carry no floating point. Group `E` is a **deterministic double-precision
evaluation** of exactly specified quantities at the thresholds printed in its tags: the propagator is transcendental, so no exact rational value exists to compare
against, but there is **no sampling, no seed and no random number anywhere in the runner**, and no line is a witness. The `K1` tick's uniform odds are a convention and no
`[exact]` conclusion depends on them. Torus wrap mass is reported wherever it could matter. No absolute unit appears anywhere, no axiom text is amended, extended,
reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

An honest auditor should come away with two declared support conditions, three declared ticks and their consequences, not a claim about which conditions the framework's
law carries or what its tick is; four exhaustive exact censuses and one exact rational coboundary certificate, with group `E` a deterministic unsampled double-precision
evaluation on named finite objects; no Monte Carlo anywhere; the stipulation declared as stipulated in the front matter, the setting, its own section, the claim block and
the proof boundary alike; an answer to PR #7889's named interface that **confirms** the mechanism it named -- absolute confinement, which no energy cost achieves -- and
then separates it cleanly from transport, which the tick's reach and not the condition decides; and a corollary written as an answer to its owner's point, with the one
open question handed back rather than settled.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority"
pointers are plain text carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=21 FAIL=0`, runtime under the declared `150`
seconds, stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a
separate lane.
