---
claim_id: record_formation_emergent_vacuum_parity_forced_odds
claim_type: bounded_theorem
claim_scope: "On three finite open graphs -- the 2x2x2 cube graph (8 vertices, 12 edge sites, 6 faces), the 3x3 grid graph (9, 12, 4), and the 3x3 grid with one pendant site at vertex 0 (10, 13, 4) -- qubits sit on the EDGE sites, the sites compose ordinarily (tensor product, operators on disjoint regions commute, no graded clause anywhere), a record at an edge site registers a Z-value there, and the vertex-level parity dictionary n_v = (1 - B_v)/2, with B_v the product of the Z's on the edges incident to v, registers occupancy from those records. The update rule throughout is Lueders conditioning on the value a forming record locks; it is STIPULATED here as this note's update clause and is not derived. With no floating point in any exact statement: (T1) the encoding A_ij = X(edge ij) times the Z's ordered before it at both endpoints, A_ji = -A_ij, B_v, and the ordered four-A face loops satisfies R0-R4 pair by pair, the code dimensions are 2^12/2^5 = 128, 2^12/2^4 = 256 and 2^13/2^4 = 512, each 2^(V-1), the cube's one face relation is the product of all six S_f = +I, and the emergent vacuum is on each cluster the unique code state carrying B_v = +1 at every vertex; its allowed set of record patterns is uniform on a LINEAR subspace of F2^E of dimension E - V + 1 -- 32 of 4096 at p = 1/32 on the cube, 16 of 4096 and 16 of 8192 on the two grids -- cut out by the single-vertex parity conditions ALONE, the Z-type subgroup of <S_f, B_v> having rank V - 1 = 7, 8, 9, sign +1 on every element, and equalling <B_v> exactly. (T2) The odds that a forming record locks the value 1 at a site, given the records already present in its neighbourhood, are 1/2 or forced to 0 or 1 and never anything between: on the cube 1/2 at all 12 sites before any record and after any single record, on grid3x3 a record at one of the 8 sites at a degree-2 corner forces its partner there, and on the pendant cluster the bridge site (0,9) carries odds 0 with no record present at all. (T3) A record elsewhere never fixes a site's possibility by itself; over all 66 cube site pairs x 4 values the odds elsewhere change in exactly the 96 cases where the two records close a vertex star and never in the other 168, and the changed site is that vertex's third edge, forced to 0 or 1. (T4) Forcing is the cocircuit structure of the graph: cut spaces of dimension 7, 8, 9, with 63 minimal cocircuits of weights 3-6 (cube, every site forced by exactly 25 inclusion-minimal record sets, the two smallest its endpoints' two-record vertex stars), 53 of weights 2-5 (grid3x3) and 54 of weights 1-5 (pendant); every listed set is deterministic and inclusion-minimal and an exhaustive sweep of all record sets of size <= 3 against the cocircuit prediction gives 0 mismatches. (T5) The finished set of records carries the same odds whatever order the records formed in: 264, 264 and 312 ordered pairs identical either way, 40 shuffled full orders per cluster closing on the same joint odds 1/32, 1/16, 1/16, all Z_e pairwise commuting exactly, and the same census with 0 mismatches on two non-stabilizer states. (T6) A fermion pair, B_v = -1 at two corners, has as its allowed set a genuine coset of the vacuum's subspace -- 32 patterns, uniform, odds 1/2 everywhere, the same 63 cocircuits of weights 3-6 at different forced values -- with the parity on star(v) equal to 1 on every allowed pattern, so n_v = 1 exactly; checked for adjacent, face-diagonal and antipodal pairs. (T7) In the cube's N = 2 sector of 28 cosets the encoded hopping is carried entrywise onto the Jordan-Wigner matrix by an exact diagonal gauge in {1, i, -1, -i}; a superposition ACROSS sectors adds no cancellation zero (support exactly 2 cosets x 32, disjoint), while coherence WITHIN one sector does: the Slater ground state at E = -4 has support 512 = 16 cosets uniform at 1/512 with 384 cancellation zeros = 12 cosets, exactly the corner pairs on one x-face, and a coherent mix of two E = -4 states has 256 = 8 cosets, whereas the projector onto the 3-fold E = -4 manifold has no vanishing diagonal entry, so those zeros belong to the state and not to the manifold. This note declares a model and computes with it; the update clause is stipulated, no formation dynamics is supplied, no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/record_formation_on_the_emergent_vacuum_parity_forced_odds_check_2026_09_02.py
---

# Record formation on the emergent vacuum: the odds at a site are one half or parity-forced

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/record_formation_on_the_emergent_vacuum_parity_forced_odds_check_2026_09_02.py`](../scripts/record_formation_on_the_emergent_vacuum_parity_forced_odds_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/record_formation_on_the_emergent_vacuum_parity_forced_odds_check_2026_09_02.txt`](../logs/runner-cache/record_formation_on_the_emergent_vacuum_parity_forced_odds_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

An encoding that puts qubits on the edge sites of a graph and registers vertex occupancy from a parity of one vertex's incident records has an **emergent vacuum**: the one
code state with `B_v = +1` everywhere. What do the record axiom's own quantities look like on that state -- which record patterns the law allows, the odds at a site, and what
the records already present do to them? The answers are entirely combinatorial: the allowed set is a linear subspace cut out by single-vertex parity conditions, the odds are
one half or forced and never between, and the order in which the records formed leaves no trace.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems on three named open graphs -- the allowed set as a linear subspace of F2^E cut out by single-vertex parity conditions, the two-valued odds census, the cocircuit characterisation of forcing with an exhaustive size-3 cross-check, the order-independence census on stabilizer and non-stabilizer states, the pair coset, and the exact cancellation-zero counts -- with one clause labelled [numerical] where a projector diagonal is read at 1e-12."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: what the framework's formation clause is, of which T3 and T5 are the behaviour any candidate must reproduce."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the seven statements below, exactly the runner's check groups `A`-`G`: `T1` (`A`, `B`) the encoding, the emergent vacuum, and its allowed set
as a coset cut out by single-vertex parity conditions alone; `T2` (`C`) the odds at a site given its neighbourhood records are `1/2` or forced, never between; `T3` (`C`)
records elsewhere fix nothing by themselves and change the odds exactly when a parity closes, the `96`/`168` census; `T4` (`D`) forcing is the cocircuit structure of the
graph, with minimal forcing sets and an exhaustive size-`3` cross-check; `T5` (`E`) order independence, on stabilizer and non-stabilizer states alike; `T6` (`F`) a fermion
pair is a parity condition on the records around two corners, a different coset with `n_v = 1` on every allowed pattern; `T7` (`G`) coherence within a sector adds cancellation
zeros, across sectors it adds none, and the zeros belong to the state and not to the manifold.

All of `T1`-`T6` and all but one clause of `T7` are exact -- Pauli algebra in the symplectic representation with phases mod `4`, `F2` linear algebra, Gaussian-integer
amplitudes and `Fraction` arithmetic. The one clause read at `1e-12`, a projector diagonal, is labelled `[numerical]` on its runner line.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Jordan-Wigner transform, Slater determinants, and the cycle/cut-space duality of a
finite graph are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's defining relations included. No observational
value, no fitted number, and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight:
`EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7842 -- the same three clusters and encoding conventions, computing
the selection-rule zeros Theorem 7 revisits from the record side), and
`EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834 -- the operator-level construction of the same
encoding on `Z^3`, whose coarse superlattice marker sites are not part of these clusters); and `MINIMAL_AXIOMS_2026-06-29.md`, from which the four axioms in "Setting" are
quoted verbatim. This note cites no grade of any of these, consumes no ledger row, and adopts no hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." "No site is privileged. Sites are distinguished by the supplied lattice structure alone." **Qubit / Site
Possibility**: "Each site has a domain of local possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`." "No possibility is privileged.
Possibilities are distinguished by the supplied algebraic structure alone."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each
site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Two of its reading notes (interpretive,
non-governing) are exactly what this note instantiates and are quoted with it: "(2) Read with Record, the distribution concerns which possibility a forming record locks,
conditional on formation at that site; it does not supply the formation site, probability, or rate." "(3) The distribution is a probability measure on the local possibility
domain; "available"/"admissible" denotes its support -- on finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may
have zero singleton measure; Record locks a supported realization."

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are
permanent." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded or signed clause
is used anywhere. The clusters below are finite open subgraphs of that lattice, drawn as graphs, so "edge site" and "vertex" have their graph meanings. The **record ontology**
is used as declared: a record at an edge site registers a value there; it does not report one the site already had. Every distribution below is law-level in the sense of
reading note (2) -- it says which value a record forming at that site locks -- and the **allowed set** is its support in the sense of reading note (3). The **update clause is
stipulated, not derived**: when a record forms with a given value, this note conditions the state in the Lueders form, restricting to the `Z`-eigenspace of that value at that
site and renormalizing. That is a choice declared here, of a shape the record axiom permits; nothing below claims it is taken from an axiom. The emergent vacuum is likewise a
state of this encoding, not of the framework.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P7`.

1. `P0` (declared here): the three graphs, the edge-site qubits, the encoding, the parity dictionary, the law, and the stipulated Lueders update clause.
2. `P1` (`A`, `B`): the encoding relations, the code dimension, the emergent vacuum, and its allowed set. `P2` (`C`): the two-valued odds. `P3` (`C`): what a record elsewhere
   does. `P4` (`D`): forcing as the cocircuit structure. `P5` (`E`): order independence. `P6` (`F`): the pair coset. `P7` (`G`): coherence and the cancellation zeros.

## Definitions

A **cluster** is a finite open graph: `cube`, the `2x2x2` cube graph, vertex `s = 4a + 2b + c`, `8/12/6` vertices, edge sites, faces; `grid3x3`, vertex `3r + c`, `9/12/4`;
`grid3x3+pendant`, that grid plus a vertex `9` joined to `0`, `10/13/4`. One qubit sits on each **edge site**, neighbours ordered by index:

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_v  = prod of the Z's on the edges incident to v,     S_f = the ordered product of the A's around a face f,
H = -sum_edges ( hop across the edge ),                star(v) = the set of edges incident to v.
```

The **code space** is the joint `+1` eigenspace of the face loops. A **record** at an edge site registers a `Z`-value there, so a full set of records is a vector `y` in
`F2^E`; the **parity dictionary** is `n_v(y) = (1 - B_v)/2 = |y intersect star(v)| mod 2`, a condition on the records of that one vertex's incident edges, and the **record
number** is `N = sum_v n_v`. The **emergent vacuum** is the code state with `B_v = +1` at every vertex. For a state, the **allowed set** is the set of record patterns it gives
nonzero probability; the **odds at a site** are the probability that a record forming there locks the value `1`, given the records already present; a **neighbourhood
condition** is one of the single-vertex parity conditions. In `H` the encoded hop across `(i, j)` is `T_ij = (i/2) A_ij (B_i - B_j)`, and the fermionic reference uses the
Jordan-Wigner ladders on the same occupation patterns. The **cut space** of the allowed set is its `F2`-orthogonal complement, its **minimal cocircuits** the inclusion-minimal
nonzero members, and a **minimal forcing set** for a site an inclusion-minimal set whose records leave that site's value deterministic.

## Theorem 1 -- the allowed set is a coset cut out by single-vertex parity conditions alone

**Conclusion.** On all three clusters:

1. `R0`-`R4` hold pair by pair; the cube's `6` face loops carry exactly one relation, the product of all six being `+I`, so `k = 5`, and each grid's `4` carry none, so `k` is
   `4`; no group contains `-I`; the code dimensions are `128`, `256`, `512`, each `2^(V-1)`.
2. The emergent vacuum is on each cluster the **unique** code state carrying `B_v = +1` at every vertex: one coset of `32`, `16` and `16` edge-site records, on which the
   parity dictionary registers no record number anywhere.
3. Its allowed set is **uniform** on that coset -- `32` of `4096` at `p = 1/32`, `16` of `4096` and `16` of `8192` at `p = 1/16` -- and is a **linear subspace of `F2^E`** of
   dimension `E - V + 1` (`5`, `4`, `4`), exactly the set the `V` single-vertex parity conditions cut out.
4. The `Z`-type subgroup of `<S_f, B_v>` has rank `V - 1` (`7`, `8`, `9`), carries sign `+1` on every element, and **equals `<B_v>`** exactly: no condition on a region wider
   than one vertex's star is present, and `prod_v B_v = +I` is the sole dependency among the `V` conditions.

**Proof.** Item 1 is an exhaustive symplectic computation with `Z4` phases, every relation checked pair by pair, the face relations obtained by exhausting all products of
subsets of the face loops, the code dimension read from a Gaussian elimination on the `X`-parts. For items 2 and 3 the cosets are built explicitly, the all-zero record pattern
labels exactly one of them, and its member set is compared against the independently generated solution set of the parity conditions and tested for closure under `xor`. Item 4
takes the `F2` kernel of the `X`-parts of `<S_f, B_v>`, forms each `Z`-type element, reads its phase, and compares its span with the span of the star masks. All exact.

**Reading, not theorem.** What the law permits is decided one vertex at a time, nothing wider ever consulted: a pattern is allowed exactly when the records around each corner
have even parity, and within that set no pattern is preferred to another.

## Theorem 2 -- the odds at a site are one half or forced, never between

**Conclusion.** Given the records already present in a site's neighbourhood, the odds there take only the values `1/2`, `0` and `1`:

1. Cube: `1/2` at all `12` sites before any record, and in each of the `24` (site, value) cases the allowed set stays uniform on `16` patterns with the odds at the `11` other
   sites still exactly `1/2`. The table at site `(0,4)`: `1/2` with no record, `1/2` after `(0,1) = 1`, `1/2` after the distant `(6,7) = 1`, `1/2` after `(0,1) = 1` together
   with `(5,7) = 1`, then `1` after `(0,1) = 1, (0,2) = 0` and `0` after `(0,1) = 1, (0,2) = 1`.
2. `grid3x3`: all `12` sites start at `1/2`; a record at one of the `8` sites at a degree-`2` corner forces its partner there to `0` or `1` in all `16` cases and changes
   nothing else; a record at any of the other `4` changes nothing.
3. `grid3x3+pendant`: the bridge site `(0,9)` carries odds `0` with **no record present at all** -- vertex `9` has degree `1`, so its own parity condition forces the site and
   a record of value `1` never forms there. The other `12` start at `1/2`.

**Proof.** The allowed set is finite and held explicitly; each odds value is a `Fraction` counting members, every case is enumerated rather than sampled, uniformity is
inherited from Theorem 1 item 3, and the conditional sets are checked to halve exactly where the odds are `1/2`. All exact.

**Reading, not theorem.** There is no partial pressure on a site. Either the neighbourhood conditions leave it free, and the odds are one half exactly, or they settle it, and
the odds are zero or one. The pendant shows the extreme case: a site settled before any record has formed anywhere.

## Theorem 3 -- a record elsewhere fixes nothing by itself

**Conclusion.** On the cube, over all `66` site pairs and `4` value combinations each: the odds at a third site change in **exactly the `96` cases** where the two records
close a vertex star, never in the other `168`; where they change, the site that changes is exactly that vertex's third edge, and its odds become `0` or `1`, never
intermediate. A single record changes the odds nowhere else at all (Theorem 2 item 1), and a distant record changes nothing unless it completes a star.

**Proof.** Exhaustive enumeration: for each unordered pair of sites and each of the four value combinations the conditioned allowed set is formed and the odds at all remaining
sites recomputed as `Fraction`s, the changed set compared against the star prediction and each changed value asserted to lie in `{0, 1}`. The tally is reported as the pair
`(shared vertices, changed sites) -> count`, and comes out `(1,1): 96` and `(0,0): 168` with no other key. All exact.

**Reading, not theorem.** A record at one site fixes nothing at another. It joins that site's neighbourhood, and only when the records around one corner close a parity does
anything change there -- and then the remaining record at that corner is not merely likelier, it is forced.

## Theorem 4 -- forcing is the cocircuit structure of the graph

**Conclusion.** For the vacuum's allowed set on each cluster, the minimal forcing sets for a site are exactly the minimal cocircuits through it, with that site deleted:

1. Cube: cut space of dimension `7`, `63` minimal cocircuits of weights `3`-`6`, every site forced by exactly `25` inclusion-minimal record sets whose two smallest are its
   endpoints' two-record vertex stars.
2. `grid3x3`: dimension `8`, `53` minimal cocircuits of weights `2`-`5`. `grid3x3+pendant`: dimension `9`, `54` of weights `1`-`5`, one of them of weight `1` -- the bridge,
   forced by the empty record set.
3. Every listed set is verified deterministic and inclusion-minimal, and an exhaustive sweep of **all** record sets of size at most `3` against the cocircuit prediction gives
   `0` mismatches on all three clusters.

**Proof.** The cut space is the `F2`-orthogonal complement of the allowed subspace, verified equal to the span of the star masks; its inclusion-minimal nonzero members are the
minimal cocircuits. Determinism is tested by conditioning on every assignment, minimality by dropping each element in turn and exhibiting an assignment that leaves the target
free, and the size-`3` sweep tests the prediction directly against conditioning, site by site. All exact.

**Reading, not theorem.** Which collections of records settle a site is not an extra rule but the cut structure of the graph; the smallest are the records around one corner.

## Theorem 5 -- the finished set of records does not remember the order

**Conclusion.** Under the stipulated Lueders update clause: all `264`, `264` and `312` ordered pairs of (site, value) give identical joint odds in either order, with `0`
mismatches on every cluster; `40` shuffled full orders per cluster, over all `12`, `12` and `13` sites, close on the same joint odds `1/32`, `1/16`, `1/16`; all `Z_e` commute
pairwise in the symplectic representation, which is the operator-level reason; and the same census gives `0` mismatches on the two **non-stabilizer** states of Theorem 7, so
this is no artefact of the vacuum's stabilizer form.

**Proof.** Both orders are formed explicitly and compared entrywise; the chain rule is walked along each shuffled order and its product compared against the flat value
`1/2^k`; the commutation test is done in the symplectic representation, and the census is re-run on the two coherent states. The vector comparisons are in double precision on
integer-valued data at a `1e-12` threshold; the operator statement they confirm, that the conditionings commute, is exact.

**Reading, not theorem.** The finished set has the same odds whatever order the records formed in; order leaves nothing behind that a later record can find.

## Theorem 6 -- a fermion pair is a parity condition on the records around two corners

**Conclusion.** On the cube, with `B_v = -1` at two corners `v, v'` -- adjacent `(0,1)`, face-diagonal `(0,3)`, antipodal `(0,7)`:

1. The allowed set is `32` of `4096` patterns and a **genuine coset** of the vacuum's subspace: translating it by any one member returns that subspace exactly. It is uniform
   at `p = 1/32`, with the odds at every one of the `12` sites exactly `1/2` before any record.
2. The parity of the records on `star(v)` is `1` at both corners on **every** allowed pattern, so `n_v = (1 - B_v)/2 = 1` exactly, with no exception.
3. The cut space and its `63` minimal cocircuits of weights `3`-`6` are identical to the vacuum's; only the forced values differ. Around vertex `0` the records at `(0,1)` and
   `(0,2)` send `(0,4)` to `1, 0, 0, 1` here against `0, 1, 1, 0` on the vacuum.

**Proof.** The coset carrying the target record pattern is located by the dictionary, its members translated and compared setwise with the vacuum's, and the star parities
collected over every member. The cut space and cocircuits are recomputed from the translated subspace, and the forcing table is read by conditioning. All exact.

**Reading, not theorem.** A fermion is a parity condition on the records around a corner: the same allowed patterns, shifted, forced the same way to different values.

## Theorem 7 -- coherence within a sector adds zeros; across sectors it adds none

**Conclusion.** In the cube's `N = 2` sector of `28` cosets, where `2^5 H_enc` is Gaussian-integer and an exact diagonal gauge with entries in `{1, i, -1, -i}` carries it
entrywise onto the Jordan-Wigner matrix of the same law with no residual:

1. **Across** sectors: `sqrt(a)|vacuum> + sqrt(b)|pair(0,1)>` at `(a,b) = (1/2,1/2)` and `(1/3,2/3)` has support exactly `64` patterns, `2` cosets of `32`, odds exactly `a/32`
   and `b/32`, and `0` cancellation zeros: disjoint supports add none.
2. **Within** one sector: the Slater ground state of two particles at `E = -4` has support `512 = 16` cosets, uniform at `1/512`, and `384` cancellation zeros = `12` cosets
   each carrying a legal weight-`2` record pattern -- exactly the `12` corner pairs on a common `x`-face. A coherent mix of two `E = -4` states has `256 = 8` cosets.
3. `[numerical, 1e-12]` The projector onto the `3`-fold `E = -4` manifold has `0` vanishing diagonal entries of `28`. The cancellation zeros therefore belong to the particular
   state, not to the energy manifold.

**Proof.** The sector matrix is assembled from the encoded hop over every edge pattern of every kept coset and certified integral after multiplication by `2^k`; the gauge is
fixed by a spanning-tree walk and verified entrywise. The Slater vectors are integer vectors built from the hypercube characters and verified exact eigenvectors of the integer
hopping matrix at `E = -4`. Every probability is then a `Fraction`, and the zero census splits exactly into patterns outside the record-number sector and cancellation zeros
inside it, the latter classified by their corner pairs. Only item 3, a projector diagonal from a `QR` factorization, is floating point, and it is labelled as such.

**Reading, not theorem.** There are two reasons a record pattern never forms. One is the allowed set: it violates a parity, and no state of this kind gives it weight. The
other is cancellation: it is allowed, but the amplitudes reaching it in this state sum to nothing. The second goes when the state changes; the first does not.

## Corollary -- concrete instances of the readout root's open items

Within the setting declared above, and on the three finite clusters named:

1. Admissibility's law-level distribution at a site is here **entirely a function of the neighbourhood records**, and takes only two shapes: flat on `{0, 1}`, or a delta.
   Reading note (2)'s "which possibility a forming record locks" is instantiated exactly, and reading note (3)'s support is Theorem 1's allowed set.
2. The informal statement that some records cannot form at a site because of neighbour conditions is **exact** here: the forced values of Theorems 2 and 4, with the bridge
   site of `grid3x3+pendant` the case where a site is settled before any record exists.
3. The selection-rule zeros of `EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7842) are the **coherent-state zeros of
   Theorem 7**, and are **not** parity zeros. The two mechanisms are distinct: a pattern can fail to form because the allowed set excludes it, or because the amplitudes cancel
   on it -- the first a property of the model, the second of the state.
4. This supplies a worked instance, not a derivation of the framework's readout, and whether that readout is a dictionary of this kind stays open below.

## Reading, not theorem -- the whole thing in plain words

A record at one site fixes nothing at another. It joins that site's neighbourhood, and the odds there change only when the records around one corner close a parity; then the
last record is forced. Otherwise the odds stay at one half. The finished set of records has the same odds whatever order the records formed in. A fermion is a parity condition
on the records around a corner.

## Interfaces named for other lanes, not settled here

- **The formation clause.** The site at which a record forms, the probability that it forms there, and the rate are all outside this note. A lane writing that clause should
  treat Theorem 3 and Theorem 5 as the behaviour its clause has to reproduce: a record elsewhere changes a site's odds only through the neighbourhood conditions, and the
  finished set is order-blind.
- **The update clause as a tick.** Lueders conditioning is stipulated here; a lane proposing a different one inherits the same two obligations. **Larger clusters**, periodic
  boundaries and the `3x3x3` case, where the face relations and hence the code dimension change, are likewise outside this note.
- **The fine-lattice marker sites.** Only edge sites carry records in this model. The coarse corner, face and cube-centre marker sites of the superlattice construction of
  `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834) are pinned and are not part of these
  clusters; what a record on one of them would be is not modelled here.

## Remaining live routes

1. Whether the two-valued odds of Theorem 2 survive on clusters whose cut space is richer, and whether the cocircuit characterisation holds for record patterns outside the
   vacuum's coset -- Theorem 6 gives one such case unchanged, which is a data point, not a proof.
2. Whether the two zero mechanisms of Theorem 7 stay disjoint. Here the parity zeros and the cancellation zeros do not overlap on any state examined, but no theorem forbids a
   state whose cancellation zeros land inside the allowed set's complement, and none is offered.

## Executable claim block

The canonical machine-bound restatement of the seven theorem conclusions.

```text
setting: qubits on the EDGE sites of three finite open graphs; ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md; clusters cube 2x2x2 V/E/F 8/12/6, grid3x3 9/12/4, grid3x3+pendant at vertex 0 10/13/4
encoding: A_ij = X(edge ij) * Z's ordered before it at both endpoints; A_ji = -A_ij; B_v the Z's incident to v; S_f the ordered four-A face loop
dictionary: n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2, a condition on one vertex's incident edges
update_clause: Lueders conditioning on the value a forming record locks -- STIPULATED by this note, not derived
relations_and_code: R0-R4 pair by pair; k = 5, 4, 4; no -I in any group; code dims 128, 256, 512, each 2^(V-1); cube's one relation = product of all six S_f = +I
vacuum: the unique code state with B_v = +1 at every vertex, one coset of 32, 16, 16 records, registering no record number
allowed_set: uniform, 32 of 4096 at 1/32, 16 of 4096 and 16 of 8192 at 1/16; a LINEAR subspace of F2^E of dim E - V + 1 = 5, 4, 4, cut out by the V single-vertex parity conditions ALONE; Z-type subgroup of <S_f,B_v> rank V-1 = 7, 8, 9, sign +1 throughout, equals <B_v>; prod_v B_v = +I the sole dependency
odds: 1/2 or forced to 0 or 1, never between; cube 1/2 at all 12 before and after any single record; grid3x3 a degree-2 corner record forces its partner, 16 cases; bridge (0,9) odds 0 with no record present
census_cube: 66 cube site pairs x 4 values -> odds elsewhere change in exactly 96 (a vertex star closes), never in 168; the changed site is that vertex's third edge, value 0 or 1, never intermediate
forcing: cut spaces dim 7, 8, 9; minimal cocircuits 63 (weights 3-6), 53 (2-5), 54 (1-5, one of weight 1); cube every site forced by exactly 25 minimal sets, two smallest the endpoints' vertex stars; every listed set deterministic and inclusion-minimal; exhaustive sweep of all record sets of size <= 3 vs the cocircuit prediction = 0 mismatches
order_independence: 264, 264, 312 ordered pairs identical either way, 0 mismatches; 40 shuffled full orders per cluster close on 1/32, 1/16, 1/16; all Z_e commute exactly; 0 mismatches on 2 non-stabilizer states
pair_state: B_v = -1 at two corners -> 32 allowed of 4096, a genuine coset of the vacuum's subspace, uniform, odds 1/2 everywhere; parity on star(v) = 1 on EVERY allowed pattern so n_v = 1 exactly; same cut space and same 63 cocircuits of weights 3-6, only forced values differ -- ((0,1),(0,2)) send (0,4) to 1,0,0,1 against 0,1,1,0 on the vacuum; adjacent, face-diagonal and antipodal checked
gauge_N2: cube N=2 sector 28 cosets; 2^5 H_enc Gaussian-integer; exact diagonal gauge in {1,i,-1,-i} carries it entrywise onto Jordan-Wigner, no residual
cross_sector: sqrt(a)|vac> + sqrt(b)|pair(0,1)> at (1/2,1/2) and (1/3,2/3): support exactly 64 = 2 cosets x 32, odds a/32 and b/32, 0 cancellation zeros
within_sector: Slater E=-4 support 512 = 16 cosets uniform at 1/512, 384 cancellation zeros = 12 cosets = the corner pairs on one x-face; a coherent mix of two E=-4 states 256 = 8 cosets
manifold_numerical: the projector onto the 3-fold E=-4 manifold has 0 vanishing diagonal entries of 28 at 1e-12 -- the zeros are the state's, not the manifold's
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=27 FAIL=0
```

## Proof boundary

Every statement above is proved on **three finite open clusters**: the `2x2x2` cube graph (`12` edge sites, `4096` record patterns), the `3x3` grid (`12`, `4096`), and the
`3x3` grid with one pendant site (`13`, `8192`), plus the cube's `N = 2` sector of `28` cosets. Nothing is claimed for larger clusters, periodic boundaries, infinite lattices,
or any law family other than the one in "Definitions". The law is **designed**, not derived: the encoding is chosen so that the Majorana relations `R0`-`R4` hold, the face
constraints are what makes that choice consistent, and the parity dictionary is one readout map among many, with no minimality or uniqueness claimed for either.

**Only edge sites carry records in this model.** The coarse corner, face and cube-centre marker sites of the superlattice construction are pinned, are not part of these
clusters, and nothing here says what a record on one would be.

**Lueders conditioning is stipulated**, declared as this note's update clause and not derived from any axiom. Consequently every "odds" statement above is a statement about
that clause applied to the declared state, and **nothing about formation dynamics** follows: no formation site, no formation probability, and no formation rate is supplied,
and none is implied. Theorems 3 and 5 constrain what a formation clause would have to reproduce; they do not supply one. Nor does this note decide what the framework's readout
is: it declares one model, of a form the record axiom permits, and computes with it. No absolute unit and no dynamical clause appears anywhere, no axiom text is amended,
extended, reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

One clause is a **floating-point witness at `1e-12`**: the vanishing-diagonal count of the `E = -4` manifold's projector in Theorem 7 item 3, labelled `[numerical]` on its
runner line. Theorem 5's comparisons are in double precision on integer data, and what they confirm -- that all `Z_e` commute, so the conditionings do -- is checked exactly.

## Review record

An honest auditor should come away with: a declared model and its consequences, not a claim about the framework's readout; six exact theorems and one carrying a single
labelled numerical clause, on named finite clusters; a stipulated update clause declared as stipulated in the front matter, the setting, the claim block and the proof boundary
alike; two distinct mechanisms for a record pattern never forming, both exhibited; and formation dynamics named as the interface it is.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the pointers in "Imports and authority"
are plain text carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=27 FAIL=0`, runtime under the declared `120` seconds, stdout
under `5500` characters, a current zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane.
