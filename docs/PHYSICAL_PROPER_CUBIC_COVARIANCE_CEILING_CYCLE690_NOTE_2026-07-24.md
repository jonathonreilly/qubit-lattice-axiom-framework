# Proper-cubic covariance ceiling of eight-vertex unit-cube triangulations — Cycle 690

Date: 2026-07-24

Claim type: no_go

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface.

Runner:
[`scripts/physical_proper_cubic_covariance_ceiling_cycle690_2026_07_24.py`](../scripts/physical_proper_cubic_covariance_ceiling_cycle690_2026_07_24.py)
(15 PASS / 0 FAIL, exit 0, 0.10 s in the shipped cold run).

## The question

The landed real-space Regge construction repeats a fixed triangulation of each
unit cube whose vertices are lattice sites. Before asking whether such a
unit-cube-local construction is cubically covariant, there is a prior question
about that local substrate:

> For how many of the 24 proper cubic rotations can such a decomposition be
> covariant **at all**?

This cycle answers that exactly. Every decisive quantity is computed in exact
integer or exact rational arithmetic on the eight cube vertices. There is no
tolerance, no fixture, no fitted constant, and no floating-point comparison
anywhere in the argument.

## Result

**No-go.** No triangulation of the cube on its eight vertices is invariant under
all 24 proper cubic rotations.

*Proof.* Every non-degenerate tetrahedron on cube vertices uses at least one
diagonal (checked exhaustively over all 58 non-degenerate 4-subsets), so an
invariant triangulation has a nonempty invariant diagonal set, which must be a
union of orbits. There are exactly two diagonal orbits: the 12 face diagonals
form one, and the 4 body diagonals form another (both verified to be single
orbits). Each full orbit is simplicially inadmissible: the two diagonals of each
face meet at that face's centre (6 interior crossings), and all four body
diagonals meet at the cube centre (6 interior crossings). Neither crossing point
is a vertex. Every union of orbits therefore contains an inadmissible pair. ∎

**Ceiling.** A stabilizer order divides 24 by Lagrange. With 24 excluded, the
attainable order is at most 12; and 12 **is attained**, by the five-tetrahedron
decomposition. The runner verifies the full complex, not merely its central
tetrahedron: exact volumes sum to 1, every pair has disjoint interior by an
exact separating-axis test, and the full-complex stabilizer has order 12.
So the maximum proper-cubic covariance of any eight-vertex unit-cube
triangulation is **exactly 12**.

**The ceiling costs a combinatorial chirality.** The five-tetrahedron
decomposition is built on one of the two alternating vertex sets. The runner
computes that the proper cubic group's commutator subgroup has order 12, so it
is the unique index-2 subgroup. It is exactly the alternating-set stabilizer.
The other 12 rotations exchange the two members of a ceiling-attaining pair.
Thus reaching 12 requires a binary unit-cube triangulation choice. This is not
a claim about physical parity.

**The standard Kuhn comparison.** The runner independently constructs the
Kuhn/Freudenthal path decomposition and computes its full-complex stabilizer as
**6**: half the ceiling, a quarter of the full group. Source inspection confirms
that this is the constant-tick spatial path complex constructed by the landed
`scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py`.
That repository comparison is not used in the no-go or ceiling proof.

| eight-vertex unit-cube decomposition | proper-cubic covariance |
|---|---|
| any all-24-invariant triangulation | **does not exist in this class** |
| five-tetrahedron (maximal) | **12**, forces a chirality choice |
| Kuhn/Freudenthal (landed) | **6** |

## Mechanism

The obstruction is not subtle once located: the 0/1 spatial direction set is
closed under coordinate permutation but **not** under sign flip. Only the 3 even
permutations preserve {0,1}^3; the other 21 rotations carry some spatial
direction out of the set entirely (witness recorded in the receipt). For those
frames, decorated covariance on the complex is **ill posed rather than
violated** — there is no image object to compare against.

Two counts appear in this area and must not be conflated. The oriented
nonnegative *spatial direction set* has stabilizer 3. The same set read up to
one global sign has stabilizer 6. The runner computes both sets and checks that
the latter six frames are exactly the Kuhn complex's cube-centred stabilizer.

## Escape conditions

Stated explicitly, because a no-go that hides its escapes is not useful:

1. **Enrich the vertex set beyond Z^3.** Adding the cube centre and all six face
   centres gives an exact 24-tetrahedron refinement invariant under all 24
   rotations. The runner constructs its simplices, verifies exact total volume
   1, checks every pair for interior disjointness, and computes the
   full-complex stabilizer. The ceiling is a property of the eight-vertex unit
   cube, not of cubic symmetry. The cost is leaving the lattice.
2. **Accept 12 and declare a chirality**, via the five-tetrahedron
   decomposition.
3. **Accept 6**, which is what the landed complex already carries.

## Consequence for the gravity lane

Any construction that repeats one fixed eight-vertex triangulation on every
unit cube cannot make that triangulation invariant under all 24 cube-centred
proper rotations. For the standard Kuhn complex, a report of 6 of 24 is its
exact full-complex stabilizer, not a numerical shortfall from 24. This theorem
does not quantify over larger cells, tetrahedra spanning multiple unit cubes,
non-unit-periodic global triangulations, or enriched vertex sets.

This cycle was prompted by exactly that situation: an open-real-space
coframe/endpoint compiler measured its well-posed covariance scope as 6 frames
and could not meet an all-24 success gate on the fixed Kuhn unit-cube complex.
That gate was unreachable in that class. No claim from that work is adopted
here; only the local substrate fact is established, and it is established
independently.

## Firewalls

- A stabilizer is not a symmetry of a physical law.
- A lattice chirality choice is **not** parity violation, and nothing here
  derives, explains, or predicts any physical chirality or parity asymmetry.
- No gravity, stress, energy, metric, or Einstein-dynamics claim is made.
- No ratio is identified with any physical observable.
- The result bounds what this eight-vertex unit-cube substrate can support.
  Nothing more.

## No-go scope for independent N1–N8 review

The negative claim is narrow and fully enumerated: it quantifies over
triangulations of *one cube* on *its own eight vertices* under the *24 proper*
rotations, and the quantification is exhaustive by orbit decomposition rather
than by sampling. It asserts no shared obstruction, exerts no axiom pressure,
and its escape conditions are stated above and computed in-run. The improper
rotations (the full 48-element octahedral group), larger-cell triangulations,
and global non-unit-periodic complexes are outside scope and were not tested.
The review-loop N1–N8 verdict remains a reviewer-owned gate, not a
self-awarded source-note result.

## Dependency citations

This note's runner imports nothing from the repository; it is self-contained
exact combinatorics. The landed-module comparison above is contextual source
inspection and is not a premise of the no-go or ceiling.
