# Proper-cubic covariance ceiling of Z^3-vertex simplicial substrates — Cycle 690

Date: 2026-07-24

Claim type: no_go

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface.

Runner:
`scripts/physical_proper_cubic_covariance_ceiling_cycle690_2026_07_24.py`
(15 PASS / 0 FAIL, exit 0, 0.01 s).

## The question

Every real-space Regge construction in this repository stands on a simplicial
decomposition whose vertices are lattice sites. Before asking whether a
particular construction is cubically covariant, there is a prior question about
the substrate itself:

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
decomposition (verified a genuine triangulation: exact volumes summing to 1 and
pairwise interior-disjoint by an exact separating-axis test). So the maximum
proper-cubic covariance of any Z^3-vertex cube triangulation is **exactly 12**.

**The ceiling costs a chirality.** The five-tetrahedron decomposition is built on
one of the two alternating vertex sets. Each set has stabilizer of order 12, and
the two are exchanged by the remaining 12 rotations. Maximal covariance and full
parity symmetry cannot be held together on this substrate: reaching 12 forces a
binary chirality declaration.

**What the landed substrate carries.** The Kuhn/Freudenthal path decomposition —
the one used by the landed 3+1 module
`frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09` — attains
**6**: half the ceiling, a quarter of the full group.

| decomposition on Z^3 vertices | proper-cubic covariance |
|---|---|
| any all-24-invariant triangulation | **does not exist** |
| five-tetrahedron (maximal) | **12**, forces a chirality choice |
| Kuhn/Freudenthal (landed) | **6** |

## Mechanism

The obstruction is not subtle once located: the 0/1 spatial direction set is
closed under coordinate permutation but **not** under sign flip. Only the 3 even
permutations preserve {0,1}^3; the other 21 rotations carry some spatial
direction out of the set entirely (witness recorded in the receipt). For those
frames, decorated covariance on the complex is **ill posed rather than
violated** — there is no image object to compare against.

Two counts appear in this area and must not be conflated. The *spatial direction
set* has stabilizer 3. The *folded static object* admits 6, because the static
tick fold absorbs a global sign, so −P acts on it exactly as P does. The runner
computes and reports both, and the Kuhn decomposition's cube-centred stabilizer
independently equals 6.

## Escape conditions

Stated explicitly, because a no-go that hides its escapes is not useful:

1. **Enrich the vertex set beyond Z^3.** Adding the cube centre gives a
   six-piece decomposition invariant under all 24 rotations (verified). The
   ceiling is a property of *Z^3 vertices*, not of cubic symmetry. The cost is
   leaving the lattice: a simplicial refinement needs further added vertices.
2. **Accept 12 and declare a chirality**, via the five-tetrahedron
   decomposition.
3. **Accept 6**, which is what the landed complex already carries.

## Consequence for the gravity lane

Any construction targeting "all-24 decorated covariance through a real-space
Regge stage" on Z^3 vertices is targeting something unreachable. Such a target
should be restated against the achievable scope (6 as landed, 12 after a
substrate change with a declared chirality), and a construction that reports 6
of 24 is at the substrate's ceiling for its complex, not short of a
reachable goal.

This cycle was prompted by exactly that situation: an open-real-space
coframe/endpoint compiler measured its well-posed covariance scope as 6 frames
and could not meet an all-24 success gate. That gate was unreachable by
construction. No claim from that work is adopted here; only the substrate fact
is established, and it is established independently.

## Firewalls

- A stabilizer is not a symmetry of a physical law.
- A lattice chirality choice is **not** parity violation, and nothing here
  derives, explains, or predicts any physical chirality or parity asymmetry.
- No gravity, stress, energy, metric, or Einstein-dynamics claim is made.
- No ratio is identified with any physical observable.
- The result bounds what a substrate can support. Nothing more.

## No-go discipline (N1–N8)

The negative claim is narrow and fully enumerated: it quantifies over
triangulations of *one cube* on *its own eight vertices* under the *24 proper*
rotations, and the quantification is exhaustive by orbit decomposition rather
than by sampling. It asserts no shared obstruction, exerts no axiom pressure,
and its escape conditions are stated above and computed in-run. The improper
rotations (the full 48-element octahedral group) are outside scope and were not
tested.

## Dependency citations

This note's runner imports nothing from the repository; it is self-contained
exact combinatorics. It refers to, but does not consume, the landed complex of
[Cycle 576](PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md).
