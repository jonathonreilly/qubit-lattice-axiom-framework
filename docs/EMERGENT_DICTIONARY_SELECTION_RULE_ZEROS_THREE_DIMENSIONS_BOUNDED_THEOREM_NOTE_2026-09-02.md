---
claim_id: emergent_dictionary_selection_rule_zeros_3d
claim_type: bounded_theorem
claim_scope: "On three finite open graphs -- the 2x2x2 cube graph (8 vertices, 12 edges, 6 faces), the 3x3 grid graph (9 vertices, 12 edges, 4 faces), and the 3x3 grid with one pendant auxiliary mode at vertex 0 (10 vertices, 13 edges, 4 faces) -- qubits are placed on the EDGE sites, the sites compose ordinarily (tensor product, operators on disjoint regions commute, no graded clause anywhere), and vertex occupancy is read out by the parity dictionary n_i = (1 - B_i)/2 with B_i the product of the Z's on the edges incident to vertex i. With no floating point in any exact statement: (T1) the encoding A_ij = X(edge ij) times the Z's ordered before it at both endpoints, A_ji = -A_ij, B_i, and the ordered four-A face loops satisfies relations R0-R4 pair by pair; the cube's 6 face loops carry exactly one relation, the product of all six being +I, leaving 5 independent generators, the two grids carry none and leave 4; the stabilizer groups 2^5, 2^4, 2^4 contain no -I and have code dimension 2^12/2^5 = 128, 2^12/2^4 = 256, 2^13/2^4 = 512, in each case 2^(V-1); and prod_i B_i = +I identically, so the dictionary registers an EVEN record number on every one of the 4096, 4096 and 8192 edge patterns and the coset-to-record map is injective on the 128, 256 and 512 code states, which is why an odd record target uses one pendant mode. (T2) In the record-number sectors of dimensions 70 (cube, N=4), 84 (grid3x3, N=6) and 84 (pendant, n_aux=1 and N_grid=3) the encoded matrix H_enc of the law -t sum_edges (hop) + V sum_edges n_i n_j has diagonals equal to the fermionic bond counts, 2^k H_enc is a Gaussian-integer matrix of max modulus 32, 16, 16, and an exact diagonal gauge D with entries in {1, i, -1, -i} satisfies D H_enc D^dag = H_F entrywise against the Jordan-Wigner matrix of the same law on the same occupation patterns; the gauge is a unitary diagonal, so spectra and record statistics agree at every coupling exactly. (T3) At g = V/t = 0 the record statistics recomputed independently from exact Slater determinants over Q(sqrt2) are: cube ground energy -6, value multiset 0 x12, 1/64 x56, 1/16 x2, the 12 zeros exactly the 6 occupied cube faces and the 6 patterns of two disjoint adjacent pairs; grid at N_grid = 3 ground energy -4 sqrt2, multiset 0 x8, 1/256 x12, 1/128 x32, 1/64 x20, 1/32 x8, 9/256 x4, the 8 zeros exactly the 3 rows, 3 columns and 2 diagonals; grid at N = 6 the same multiset with the 8 zeros exactly the complements of those, the particle-hole image. Each of the 70, 84 and 84 vertex patterns carries a constant fibre of 2^k = 32, 16, 16 edge records with |phi(y)| = 1 throughout, so the edge-record probability is the vertex probability divided by the fibre size and the 384, 128 and 128 edge records over a zero are themselves exactly zero. (T4) As a floating-point witness at g in {0, 0.5, 1, 2} the encoded and fermionic record statistics agree to L1 at most 3.4e-15, the zero sets coincide (12/12/12/12 on the cube, 8/4/4/4 on both grids), the ground state is simple at every point with smallest gaps 0.573988, 0.788251 and 1.293567, and the zeros surviving every g in {0.5, 1, 2} are all 12 on the cube and exactly 4 of 8 on the grid, the four lines through the centre at N_grid = 3 and their complements at N = 6. (T5) Every off-diagonal amplitude in the edge-record basis is exactly +i or -i, 15360 of them split 7680/7680 on the cube and 8064 split 4032/4032 on the grid; the Z-support of A_ij B_i lies inside star(i) U star(j), and sign(y) = s_e (-1)^{|y & Z(A_ij B_i)|} holds for every edge and all 4096 records, so every sign is a parity of the record over one vertex's incident edges; the gauge-invariant four-cycle flux of the configuration graph is -1 on 144 of 444 cube cycles and 80 of 344 grid cycles, identical for H_F, and a spanning-tree gauge leaves 90 of 240 and 80 of 252 entries at +1. (T6) The control that puts a bare X_e in place of A_ij anticommutes with 16 of 60 and 12 of 48 (term, stabilizer generator) pairs, so it leaves the code space; it still conserves the record on edge sectors of dimension 2240 and 1344, where a diagonal unit gauge turns all 7680 and 4032 off-diagonal entries into -1 on a graph of one connected component, so by Perron-Frobenius its ground vector is simple and strictly positive at every real g, and numerically at g in {0, 0.5, 1, 2} all 70 and 84 vertex patterns carry probability at least 1.4861e-03 and 2.3740e-04 with 0 exact zeros. This note declares a dictionary and computes with it; no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/emergent_dictionary_selection_rule_zeros_three_dimensions_check_2026_09_02.py
---

# The emergent dictionary reproduces the three-dimensional selection-rule zeros, from single-vertex neighbourhood conditions alone

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/emergent_dictionary_selection_rule_zeros_three_dimensions_check_2026_09_02.py`](../scripts/emergent_dictionary_selection_rule_zeros_three_dimensions_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/emergent_dictionary_selection_rule_zeros_three_dimensions_check_2026_09_02.txt`](../logs/runner-cache/emergent_dictionary_selection_rule_zeros_three_dimensions_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

A separate finite test found record patterns that a graded nearest-neighbour law gives probability exactly zero while every ungraded member of the same family
gives them positive probability; that test lives on vertices and reads occupancy directly. This note asks whether the same zeros are available on a lattice
whose sites compose ordinarily and whose readout is a **dictionary**: qubits on the edges, vertex occupancy computed from the records of the edges at that one
vertex. They are, in three dimensions and in two, with the same zero sets and value multisets, from a parity over a single vertex's incident edges.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems on three named open graphs -- encoding relations and code dimensions, an exact diagonal unit gauge identifying the encoded and fermionic matrices entrywise, the exact zero sets and their fibres, the exact sign structure and flux, and the exact Perron-Frobenius control -- together with one floating-point persistence witness, labelled as such wherever it appears."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: whether the framework's readout is a dictionary of this kind."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`G`. `T1`, `T2`, `T3`, `T5` and the structural half of `T6`
are exact -- integer and `F2`/`Z4` bit arithmetic, Gaussian-integer amplitudes, `Fraction` and `Q(sqrt2)` arithmetic; `T4` and the confirming half of `T6` are
floating-point witnesses at `1e-12`, labelled `[numerical]` wherever they appear.

1. `T1` (`A`). Encoding: `R0`-`R4`, the face relations, code dimension `2^(V-1)`, and `prod_i B_i = +I`, so an odd target uses one pendant mode.
2. `T2` (`B`). Unit gauge: an exact diagonal `D` with `D H_enc D^dag = H_F` entrywise, hence identical spectra and record statistics at every coupling.
3. `T3` (`C`, `E`). Zeros at `g = 0`: the exact value multisets and zero sets, recomputed from Slater determinants, and the fibre carrying them to the records.
4. `T4` (`D`). Persistence: agreement, equal zero sets and simplicity at `g != 0`, and the four lines through the centre.
5. `T5` (`F`). Sign structure: every negative amplitude is a parity of the record over one vertex's incident edges, with the flux witness.
6. `T6` (`G`). Control: the bare edge-flip law leaves the code space and is sign-uniform on what it preserves, so its statistics are strictly positive.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Jordan-Wigner transform, Slater determinants and the
Perron-Frobenius theorem are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's defining relations
included. No observational value, no fitted number, and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade or weight:

- `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7833 -- the finite test whose zero sets are reproduced here) and
  `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834 -- the operator-level
  construction of the same encoding on `Z^3`).
- `RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md`,
  `ENDPOINT_LOCALIZATION_THREE_ROUTE_DISCRIMINATOR_CYCLE705_NOTE_2026-07-26.md`, `ENERGY_GAUSS_CONSTRAINT_OBSTRUCTION_ROUTE_B_NOTE_2026-07-08.md` and
  `ROUTE_B_TYPED_SPECTATOR_RADIUS_ONE_SYNTHESIS_CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md` (earlier superfast, bosonization and route-B surveys).
- `FINITE_FLAT_LINK_EVEN_CAR_SUPPORT_CENSUS_BOUNDED_THEOREM_NOTE_2026-07-23.md`, `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md` (the earlier ring and
  chain probes) and `MINIMAL_AXIOMS_2026-06-29.md` (the four axioms quoted in "Setting"). This note cites none of their grades, consumes no row, and adopts no
  hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`", with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site. **Qubit**: each site has a domain of local possibilities whose full one-site possibility
domain has algebraic presentation `M_2(C)`. **Admissibility**: there is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and
proper cubic rotations. **Record**: when present, a record locks exactly one admissible local possibility, a site never carries more than one record, records
are permanent, and only records are readable.

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded or
signed composition clause is used anywhere. The clusters below are finite open subgraphs of that lattice, drawn as graphs so "edge site" and "vertex" have
their graph meanings. The **record ontology** is used as declared: records register, they do not read. The parity dictionary of "Definitions" is a **readout
map** from edge-site records to the occupancy of a vertex, a condition on the records of that one vertex's incident edges and not a claim about anything else.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P6`.

1. `P0` (declared here): the three graphs, the edge-site qubits, the encoding, the parity dictionary, the law, and the control.
2. `P1` (`A`): the encoding relations, the face relations, the code dimension, and the even-number identity.
3. `P2` (`B`): the exact diagonal unit gauge. `P3` (`C`, `E`): the `g = 0` record statistics, the zero sets, and the constant fibre.
4. `P4` (`D`): persistence at `g != 0` and the four centre lines. `P5` (`F`): the sign structure and the flux witness. `P6` (`G`): the control.

## Definitions

A **cluster** is a finite open graph: `cube` is the `2x2x2` cube graph, vertex `s = 4a + 2b + c`, `8/12/6` vertices, edges, four-cycle faces; `grid3x3` is the
`3x3` grid graph, vertex `3r + c`, `9/12/4`; `pendant` is `grid3x3` with an extra vertex `9` joined to vertex `0`, `10/13/4`. One qubit sits on each **edge
site**, neighbours of a vertex ordered by vertex index. For an ordered edge `(i, j)`,

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_i  = prod of the Z's on the edges incident to i,     S_f = the ordered product of the A's around a face f,
H(t, V) = -t sum_edges ( hop across the edge ) + V sum_edges n_i n_j,      g = V/t at t = 1.
```

The **code space** is the joint `+1` eigenspace of the face loops. The **parity dictionary** is the readout map `n_i(y) = (1 - B_i)/2` on the edge
record `y`, which is `|y intersect star(i)| mod 2` with `star(i)` the edges incident to `i`; the **record number** is `N = sum_i n_i` and a **record
pattern** the vector `(n_0, ..., n_{V-1})`. In `H(t, V)` the encoded hop across `(i, j)` is `T_ij = (i/2) A_ij (B_i - B_j)`, and the fermionic
reference `H_F` uses the Jordan-Wigner ladders on the same occupation patterns. The **record statistics** of a law are the occupation-basis diagonal
of its lowest-energy state in a fixed record-number sector, the normalized ground-space projector diagonal if degenerate. The **control** replaces
`A_ij` by the bare edge flip `X_e`.

## Theorem 1 -- the encoding, and why an odd record number needs one more site

**Conclusion.** On all three clusters:

1. Relations `R0`-`R4` hold pair by pair: `A_ij` well defined, `A_ji = -A_ij`, `A` and `B` Hermitian involutions, the `B`'s commuting and anticommuting with
   `A_ij` exactly at `i` and `j`, two `A`'s anticommuting exactly when they share a vertex, the face loops involutions commuting with every `A`, `B` and each
   other.
2. The cube's `6` face loops carry exactly one relation, the product of all six being `+I`, so `5` are independent; each grid's `4` carry none. The groups of
   order `2^5`, `2^4`, `2^4` contain no `-I` and only the identity has trivial `X`-part, so the code dimensions are `128`, `256`, `512`, each `2^(V-1)`.
3. `prod_i B_i = +I` identically, so the dictionary registers an **even** record number on every one of the `4096`, `4096` and `8192` edge patterns and the
   coset-to-record map is injective on the `128`, `256` and `512` code states.
4. Consequently the odd sector `N = 3` of `grid3x3` is not carried by its `12` edge qubits; one pendant auxiliary mode at vertex `0`, whose edge carries no term
   of the law, makes `n_aux = 1` and `N_grid = 3` available with the same face structure.

**Proof.** Items 1 and 2 are exhaustive symplectic computations with `Z4` phases, every relation checked pair by pair rather than assumed, the face relations
obtained by exhausting all products of subsets of the face loops, the code dimension read off a Gaussian elimination on the `X`-parts. Item 3 is immediate from
every edge appearing in exactly two stars and is confirmed on every edge pattern; item 4 is a construction plus the same audit re-run. All exact.

**Reading, not theorem.** Under this readout the cluster can only ever show an even number of records. That is not a choice made when the readout was written
down; it is forced by the readout, because each edge record counts at both of its ends. An odd count needs one more site, and the pendant is it.

## Theorem 2 -- the encoded law and the fermionic law are the same matrix up to a diagonal unit gauge

**Conclusion.** In the record-number sectors of dimension `70` (cube, `N = 4`), `84` (`grid3x3`, `N = 6`) and `84` (pendant, `n_aux = 1` and `N_grid = 3`):

1. The diagonal of `H_enc` is the fermionic bond count on every pattern, and `2^k H_enc` a Gaussian-integer matrix of maximum modulus `32`, `16`, `16`.
2. There is an exact diagonal `D` with all entries in `{1, i, -1, -i}` -- `38`, `40` and `44` of them non-real -- with `D H_enc D^dag = H_F` **entrywise**, no
   residual whatsoever. `D` is unitary, so the two matrices have identical spectra, identical ground spaces up to that phase, and identical record statistics
   at every real `g`.

**Proof.** The sector matrix is assembled from the encoded hop acting on every edge pattern of every kept coset, and its exactness certified by multiplying
through by `2^k` and checking integrality of real and imaginary parts with zero residual. The gauge is found by a spanning-tree walk on the off-diagonal
support: the support sets are compared first, each entry then fixes one phase relative to its neighbour, every remaining entry is a consistency test rather than
a free choice, and the identity is finally verified entrywise. Conjugation by a diagonal unitary preserves the spectrum and every diagonal probability.

**Reading, not theorem.** Two descriptions that look different -- one about records on edges, one about occupancy on vertices -- are the same description up to
a phase attached to each pattern, and such a phase changes no probability. So the two agree on everything readable, at every coupling, not only at the one
point where the answer is available in closed form.

## Theorem 3 -- the zero sets at `g = 0`, and the records that carry them

**Conclusion.** At `g = 0`, recomputed independently from exact Slater determinants over `Q(sqrt2)` after verifying the orbitals are eigenvectors and the
ground determinant unique across a strict single-particle gap:

1. Cube, `N = 4`: ground energy `-6`, normalization `1`, value multiset `0 x12`, `1/64 x56`, `1/16 x2`. The `12` zeros are exactly the `6` occupied cube faces
   and the `6` patterns of two disjoint adjacent pairs, `0` other.
2. Pendant, `N_grid = 3`: `E0 = -4 sqrt2`, normalization `1`, multiset `0 x8`, `1/256 x12`, `1/128 x32`, `1/64 x20`, `1/32 x8`, `9/256 x4`; the `8` zeros are
   exactly the `3` rows, `3` columns and `2` diagonals. `grid3x3` at `N = 6` on the plain `12`-qubit code has the same multiset, its `8` zeros exactly the
   complements of those -- the particle-hole image.
3. Every vertex pattern carries a constant fibre of `2^k = 32`, `16`, `16` edge records, with `|phi(y)| = 1` throughout, so an edge record's probability is its
   vertex pattern's divided by the fibre size and the `384`, `128` and `128` edge records over a zero are exactly zero.

**Proof.** The single-particle orbitals are exhibited and checked to be exact eigenvectors of the cluster adjacency over `Q(sqrt2)`; each pattern's Slater
amplitude is the determinant of the occupied rows, taken by Gaussian elimination in the field `Q(sqrt2)` with `Fraction` coefficients, so no floating point
enters. The vector is verified to satisfy `H_F v = E v` exactly against the integer matrix and to have `<v|v> = 1`, uniqueness following from the strict gap
between the highest filled and lowest empty single-particle level. The zero-set classifications are exhaustive enumerations, and item 3 follows from the coset
structure -- every coset has exactly `2^k` members, each coefficient a unit -- both halves checked directly. All exact.

**Reading, not theorem.** Some record patterns never form. Which ones is decided by the shape of the whole pattern: on the cube the six faces and the six pairs
of opposite edges, on the grid the eight straight lines. The exclusion is visible in the records themselves, since every edge-level record reading out to an
excluded pattern has probability exactly zero too.

## Theorem 4 -- the zeros at other couplings, and the four lines through the centre

**Conclusion.** As a floating-point witness at tolerance `1e-12`, over `g in {0, 0.5, 1, 2}`:

1. The encoded and fermionic record statistics agree to `L1` distance at most `2.0e-15` (cube), `3.4e-15` (`grid3x3`, `N = 6`) and `2.6e-15` (pendant), their
   zero sets coincide at every point, and the ground state is simple throughout, with smallest gaps `0.573988`, `0.788251` and `1.293567`.
2. The zero counts are `12/12/12/12` on the cube, `8/4/4/4` on both grid sectors.
3. The zeros surviving every `g in {0.5, 1, 2}` are all `12` on the cube -- the whole `g = 0` set -- and exactly `4` of `8` on the grid: the four centre lines
   `(3,4,5)`, `(1,4,7)`, `(0,4,8)`, `(2,4,6)` at `N_grid = 3`, and their complements at `N = 6`.

**Proof.** Both matrices are formed at each coupling and diagonalised; the ground-space projector diagonal is compared entry by entry, the zero sets taken at
`1e-12`, the degeneracy read at `1e-9`, and the surviving set obtained as the intersection over the non-zero couplings and compared with the named line set.
This is a numerical witness, labelled as such; the exact statement that the two laws agree at every coupling is Theorem 2, of which this is a confirmation at
four points rather than a substitute.

**Reading, not theorem.** Four of the grid's eight zeros persist once the two-site term carries weight and four do not; the four that persist are the four
straight lines through the centre. What the coupling leaves alone is the part of the pattern a symmetry of the cluster already fixes.

## Theorem 5 -- every negative amplitude is a parity over one vertex's incident edges

**Conclusion.** In the edge-record basis of the sector:

1. Every off-diagonal amplitude is exactly `+i` or `-i` -- `15360` of them on the cube, split `7680/7680`, and `8064` on `grid3x3`, split `4032/4032`.
2. The `Z`-support of `A_ij B_i` lies inside `star(i) U star(j)`, and `sign(y) = s_e (-1)^{|y intersect Z(A_ij B_i)|}` with one constant `s_e` per edge, for
   every edge and every one of the `4096` records, so each sign is a parity of the record over **single-vertex incident-edge sets**.
3. The signs are not a relabelling. The gauge-invariant product of amplitudes around a four-cycle of the configuration graph is `-1` on `144` of the cube's
   `444` cycles and `80` of the grid's `344`, identical for `H_F`; in a spanning-tree gauge `90` of `240` and `80` of `252` entries remain `+1`, so no diagonal
   gauge makes either law sign-uniform.

**Proof.** Item 1 is collected while the sector matrix is assembled, each amplitude asserted to be a unit purely imaginary Gaussian integer. Item 2 tests mask
containment on every edge and evaluates the closed form on every record of the full edge space, fixing `s_e` from the first non-vanishing record. Item 3
computes a quantity invariant under diagonal rephasing -- the product around a closed four-step circuit -- so no artefact of a convention. All exact.

**Reading, not theorem.** Whether a record pattern can form depends on the parity of the records around single sites. Every minus sign in the law is one of
those parities, and no larger region is consulted. Nor are those signs bookkeeping: a quantity no relabelling can change is negative on `144` of `444` circuits.

## Theorem 6 -- the control: the bare edge flip has no zeros at any coupling

**Conclusion.** Replacing `A_ij` by the bare edge flip `X_e`:

1. The bare term anticommutes with `16` of the `60` and `12` of the `48` (term, stabilizer generator) pairs on the cube and on `grid3x3`, so it does not
   preserve the code space.
2. It still conserves the record, and on the preserved edge sectors -- dimension `2240` and `1344` -- a diagonal unit gauge turns all `7680` and `4032`
   off-diagonal entries into `-1` on a configuration graph of exactly one connected component.
3. Hence by Perron-Frobenius its lowest state is simple and strictly positive at every real `g`, and its pushforward through the dictionary sums positive
   numbers. Numerically at `g in {0, 0.5, 1, 2}` all `70` and `84` patterns carry probability at least `1.4861e-03` and `2.3740e-04`, with `0` exact zeros.

**Proof.** Item 1 is a pairwise commutation test against the stabilizer generators. Item 2 builds the bare sector explicitly, verifies Hermiticity and record
conservation on every basis element, then runs a spanning-tree gauge whose residual counts are exhibited: all entries land on `-1` and the walk visits the
whole graph, which is the irreducibility hypothesis. Item 3 is Perron-Frobenius with both hypotheses checked. Items 1 and 2 are exact; the confirming
diagonalisation is a labelled numerical witness.

**Reading, not theorem.** Take away the one ingredient that is a condition on a whole neighbourhood and the exclusions vanish entirely. The control is not a
weaker version of the law: it does not respect the constraints that make the readout well defined, and on the part it does respect every pattern has positive
probability.

## Corollary -- the readable shadow, produced in three dimensions by ordinary composition

Within the setting declared above, and on the three finite clusters named:

1. The zero sets that `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7833) identifies as the readable shadow of a
   cross-site sign -- `12` of `70` on the cube, `8` of `84` on the `3x3` grid, same value multisets -- are reproduced here on an **ordinary-composition**
   edge-site lattice, the plain tensor product throughout with no graded clause anywhere.
2. The only non-trivial ingredient is a **single-vertex neighbourhood condition**: the readout is a parity over one vertex's incident edges, by Theorem 5 every
   sign in the law is such a parity as well, and nothing in the construction reads a region larger than one vertex's star.
3. This is the record-level face of the operator-level construction in
   `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): that note establishes the
   same encoding's exchange statistics on `Z^3` as an operator statement, this one what the encoding does to the probabilities a record readout returns on
   finite clusters. Neither derives the other; they check different quantities of one declared construction.
4. What the dictionary supplies is a translation, not an explanation: the zeros are reproduced because Theorem 2 makes the two matrices the same matrix, and
   why the exclusion law holds is untouched by that and stated as open in "Proof boundary".

## What does not move

- This does not decide what the framework's readout is: it declares one dictionary, of a form the record axiom permits, and computes with it. It supplies no
  update rule, no formation site, no formation rate, and no values; no absolute unit and no dynamical clause appears anywhere, and it says nothing about larger
  clusters, periodic boundaries, infinite lattices, or law families other than the one in "Definitions". No axiom text is amended, extended, reworded, or
  reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Interfaces named for other lanes, not moved here

- The exclusion law itself. This note reproduces a zero set and derives no exclusion principle; a lane wanting one should treat Theorem 3 as the target to
  explain and Theorem 5 as the structure available to explain it with.
- The pendant construction. Theorem 1 item 3 makes the even record number an identity of the readout; whether a dictionary registering odd record numbers
  without an auxiliary site exists is untouched, as is whether an analogue of Theorem 4's four centre lines survives on larger grids or on `3x3x3`.

## Remaining live routes

1. Bigger clusters and periodic boundaries. The face relations, and with them the code dimension, change on a torus; nothing here covers that case, and only
   the one nearest-neighbour family of "Definitions" is read -- a longer-range or multi-site family is another question.
2. The coupling scan. Theorem 4 is a witness at four points; an exact statement about which zeros persist at every `g` would supersede it. The readout's
   uniqueness is likewise open: the parity dictionary is one readout map among many, and no minimality is claimed for it.

## Executable claim block

The canonical machine-bound restatement of the six theorem conclusions.

```text
setting: qubits on the EDGE sites of three finite open graphs; ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
clusters: cube 2x2x2 V/E/F 8/12/6; grid3x3 9/12/4; grid3x3+pendant at vertex 0 10/13/4
encoding: A_ij = X(edge ij) * Z's ordered before it at both endpoints; A_ji = -A_ij; B_i the Z's incident to i; S_f the ordered four-A face loop
dictionary: n_i = (1 - B_i)/2 = |y intersect star(i)| mod 2, a condition on one vertex's incident edges
relations_and_code: R0-R4 pair by pair; faces 6 with one relation (product of all six) = +I so k=5, 4 with none so k=4, 4 with none so k=4; no -I in any group
code_dimensions: 2^12/2^5 = 128, 2^12/2^4 = 256, 2^13/2^4 = 512, each equal to 2^(V-1); sectors cube N=4 dim 70, grid3x3 N=6 dim 84, pendant N_grid=3 dim 84
even_record_identity: prod_i B_i = +I identically; even record number on all 4096/4096/8192 edge patterns; record map injective on 128/256/512 code states
unit_gauge: 2^k H_enc Gaussian-integer of max modulus 32/16/16; D in {1,i,-1,-i}, 38/40/44 non-real, D H_enc D^dag = H_F entrywise
g0_cube: E0 = -6; values 0 x12, 1/64 x56, 1/16 x2; zeros = 6 occupied faces + 6 two-disjoint-adjacent-pair patterns, 0 other
g0_grid: E0 = -4 sqrt2; values 0 x8, 1/256 x12, 1/128 x32, 1/64 x20, 1/32 x8, 9/256 x4; zeros at N_grid=3 = 3 rows + 3 columns + 2 diagonals; at N=6 their complements
fibres: |phi(y)| = 1 everywhere; constant fibre 2^k = 32/16/16; 70x32 = 2240, 84x16 = 1344 twice in the sector; 384/128/128 records over a zero, all exactly 0
persistence_numerical: g in {0, 0.5, 1, 2}; L1 <= 2.0e-15 / 3.4e-15 / 2.6e-15; zero counts 12/12/12/12 and 8/4/4/4; ground simple; gaps 0.573988 / 0.788251 / 1.293567
persistent_zeros: cube 12 of 12; grid 4 of 8, the lines (3,4,5) (1,4,7) (0,4,8) (2,4,6) at N_grid=3 and their complements at N=6
sign_structure: 15360 amplitudes split 7680/7680 (cube) and 8064 split 4032/4032 (grid), each exactly +i or -i; Z(A_ij B_i) inside star(i) U star(j); sign(y) = s_e (-1)^{|y & Z(A_ij B_i)|} on all 4096 records
flux_witness: four-cycle flux -1 on 144 of 444 (cube) and 80 of 344 (grid), identical for H_F; spanning-tree gauge leaves 90 of 240 and 80 of 252 entries at +1
control: bare X_e anticommutes with 16 of 60 and 12 of 48 (term, generator) pairs; preserved sectors 2240 and 1344; unit gauge makes all 7680 and 4032 entries -1 on 1 component; Perron-Frobenius simple and strictly positive at every real g; min probability 1.4861e-03 and 2.3740e-04, 0 exact zeros
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=25 FAIL=0
```

## Proof boundary

Every statement above is proved on **four finite open clusters at fixed record number**: cube `N = 4` (dimension `70`), `grid3x3` `N = 6` (`84`), `grid3x3`
with a pendant mode at `n_aux = 1` and `N_grid = 3` (`84`), and the control's edge sectors of dimension `2240` and `1344`. Nothing is claimed for larger
clusters, periodic boundaries, infinite lattices, or any law family other than the one written in "Definitions".

This note supplies a **dictionary, not a derivation of the exclusion law**. Theorem 2 shows the encoded and the fermionic matrix are the same matrix up to a
diagonal unit gauge, so the zero sets have to agree; that is a translation between two descriptions, and it explains why the numbers match without explaining
why the numbers are zero. The exclusion is imported from the structure of the encoding, not deduced from any axiom.

The encoding is **chosen** so that the Majorana relations `R0`-`R4` hold, and the face constraints are exactly what makes that choice consistent: the code
space is the joint `+1` eigenspace of the face loops, and outside it the encoded hop is not the operator computed here. The `12`-qubit lattices carry an even
record number only, `prod_i B_i = +I` being an identity of the readout rather than a property of a state, so the odd target `N = 3` uses one pendant mode whose
edge carries no term of the law -- an auxiliary device, declared as such, with the `N = 6` sector reported alongside it precisely so the same zero set is
exhibited without any auxiliary mode, as the particle-hole image.

Theorem 4 and the confirming half of Theorem 6 are **floating-point witnesses at `1e-12`** over four couplings; the exact content of the coupling statement is
Theorem 2's unit-gauge identity, which holds at every real `g` without approximation, and the four surviving grid zeros are the intersection over the three
non-zero couplings tested, not a proof that no further coupling changes the set. The sign structure of Theorem 5 is about **this** encoding's amplitudes in
**this** basis: the closed form is verified on every record rather than sampled and the flux is invariant under diagonal rephasing, so neither depends on the
ordering convention, but a different encoding or neighbour ordering is a different computation. No axiom is amended, no status set, no registry entry made.

## Review record

An honest auditor should come away with: a dictionary and its consequences, not a claim about the framework's readout; five exact theorems and one numerical
witness on named finite clusters; one open question stated as open (why the exclusion law holds at all, as against why these two descriptions agree); and one
device declared as a device (the pendant mode). Floating point is confined to Theorem 4 and item 3 of Theorem 6, both labelled `[numerical]` on every runner
line where they appear, and no exact statement rests on them.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the context notes in
"Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at
`PASS=25 FAIL=0` with runtime under the declared `300` seconds and stdout under `5500` characters, a current zero-dependency citation-manifest entry, and
passing pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
