# Weight-three rigidity and image-subspace partitions for a finite four-cube cutting family

Date: 2026-08-11

Authority: none

Audit: unset

Status: proposed_retained

Claim type: bounded_theorem

Constitutional effect: none.

Machine status:

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Send this self-contained finite theorem and paired runner to independent audit; a downstream framework consumer remains unidentified."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact finite geometry, group-action identities, and field-scoped image/kernel partitions for one declared unit-four-cube construction."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner:

- [four_cube_cutting_weight_three_rigidity_image_partition_2026_08_11.py](../scripts/four_cube_cutting_weight_three_rigidity_image_partition_2026_08_11.py)

Reviewed cache:

- [four_cube_cutting_weight_three_rigidity_image_partition_2026_08_11.txt](../logs/runner-cache/four_cube_cutting_weight_three_rigidity_image_partition_2026_08_11.txt)

Framework premise edges: 0.

## Imports and construction choices

- Scientific file inputs: none. The runner rebuilds every scientific object.
- The unit four-cube `{0,1}^4`, five-corner determinant-magnitude-one rule,
  adjacency-cost minimum, shifted divisor-80 sample, signed coordinate action,
  two primes, orbit order, and index-order comparator are explicit finite
  construction choices.
- Measured, fitted, literature, observational, predecessor, sibling-branch, and
  framework inputs: none.
- Package-local scientific reads: none. The cache envelope reads the runner bytes
  for integrity; the runner itself reads no repository file.
- Python, NumPy, wall time, and peak memory are implementation/support inputs and
  supply no mathematical value.
- The current Minimal Axioms document is a non-linking scope marker. It supplies
  zero premises to this finite theorem.

## Exact target and obligation graph

Let `P` be the 192 selected determinant-one simplices, `K` the 15,800
24-simplex geometric cuttings, `C` the 192 eight-piece covers, `G` the 384
signed coordinate maps, and `T_0,...,T_95` the orbit tables constructed by the
runner. Let `F = F_1000003`.

The exact target is: certify the finite geometric object and its group action;
prove the weight-four zero and weight-three rank/image/kernel statements over
the named fields; prove the lone-minority rank lemma over `F`; and establish the
stated image-subspace equality partitions, fibre relation, comparator relation,
and finite counts over `F`.

The acyclic proof obligations are:

- `P0` [proved here]: enumerate 2,672 determinant-one candidates and the 400 at
  adjacency-cost minimum 6.
- `P1` [proved here; depends on `P0`]: enumerate the 15,800 sample exact covers
  and certify all 15,168 co-occurring simplex pairs by exact rational geometry.
  The 24 normalized volumes sum to the four-cube volume.
- `P2` [proved here; depends on `P1`]: enumerate 192 used pieces and 192 covers,
  each cover meeting every cutting once.
- `P3` [proved here; depends on `P2`]: construct `G`, both transitive actions,
  96 free pair orbits, and the degree-two orbit tables.
- `P4` [proved here; depends on `P3`]: construct the sixteen odd-characteristic
  flip blocks, their piece dimensions 12, and cover dimensions
  `24/18/12/6/0` by pattern weight.
- `P5` [proved here; depends on `P3`, `P4`]: at weight four, every table has rank
  zero at both primes; at weight three, every table has rank six at both primes.
- `P6` [proved here over `F`; depends on `P4`, `P5`]: at each weight-three
  pattern the 96 images coincide and span the six-dimensional cover block; the
  kernels form two complementary six-dimensional classes of size 48 matching
  the full-table kernel partition.
- `P7` [proved here over `F`; depends on `P6`]: a four-table member with one
  minority kernel class has rank six and kernel transverse to the majority
  kernel at each weight-three pattern.
- `P8` [proved here over `F`; depends on `P4`-`P7`]: establish the incidence and
  index-order comparator profiles, image-subspace partitions, fibre involution,
  overlap histograms, and finite member counts.

Every obligation in this bounded target is proved by a fail-closed gate. The
strongest missing lemma is therefore none within the declared finite object and
coefficient fields. Physical interpretation, multi-cell extension, and integral
module promotion lie outside the target.

## 1. Exact finite geometry

The 16 four-cube vertices contain 2,672 five-vertex subsets with determinant
magnitude one. Exactly 400 attain adjacency cost 6. A shifted `5^4` rational
sample avoiding every candidate facet enumerates 15,800 exact sample covers,
each with 24 simplices.

The runner then examines every pair occurring in a selected cover using exact
rational facet inequalities. Of 15,168 pairs, 13,632 have an immediate weak
facet separator. The remaining intersections have affine dimension zero for
864 pairs and one for 672 pairs. Thus selected simplex interiors are pairwise
disjoint. Each simplex has volume `1/24`, so every selected 24-set is a
geometric cutting of the unit four-cube.

Exactly 192 pieces occur, each in 1,975 cuttings. Their 379,200 incidences also
equal `15,800 * 24`. The non-cooccurrence graph has exactly 192 eight-piece
covers, and each cover meets every cutting once.

## 2. Group action and flip blocks

The 24 permutations of four coordinates composed with the 16 coordinate flips
give 384 distinct maps closed under composition. They induce distinct
transitive bijections on both `P` and `C`. The action on `P x C` has 96 orbits
of size 384. Their zero-one orbit tables are pairwise disjoint, have row and
column degree two, and sum to the all-ones matrix.

Every four-table subset is therefore an eight-regular zero-one member of a
family of `C(96,4) = 3,321,960`.

The cover incidence is one member. The comparator used below is the sum of the
first four orbit tables outside the incidence, in the runner's deterministic
orbit enumeration order. This selector is a declared convention.

The 16 pure flips act freely on the 192 pieces, yielding 12 piece orbits. Their
16 sign characters give sixteen 12-dimensional piece blocks whose direct sum
has dimension 192. On covers, the four single-axis stabilizer masks occur six
times each; the cover-block dimensions by pattern weight are
`24/18/12/6/0`.

## 3. Top-weight and weight-three structure

At the all-signs pattern the cover block has dimension zero, and all 96 table
restrictions have rank zero and kernel dimension 12 at both `F_1000003` and
`F_1000033`.

At each of the four weight-three patterns every table has rank six at both
primes. Over `F`, all 96 images coincide, their aggregate span has dimension
six, and that common image equals the cover block. This common-image and
aggregate-span computation saturates the six-dimensional representation
ceiling; the dimension ceiling alone supplies only the upper bound.

Over `F`, the table kernels form exactly two classes. Each kernel has dimension
six, each class contains 48 tables, and representatives of the two classes
meet in zero and span the full 12-dimensional piece block. The same two-way
partition is obtained independently from alternating vectors on the 48
eight-cycles of each full orbit table. The production gate verifies the full
table cycles, their annihilation, their 48-dimensional rowspaces at both
primes, and agreement of the two 48/48 partitions.

## 4. Lone-minority rank theorem

**Theorem over `F`.** Let `A_1,...,A_4` be four distinct orbit-table
restrictions at one weight-three pattern. If three kernels equal `K_a` and the
fourth equals the complementary class `K_b`, then
`rank(A_1+...+A_4)=6`, its kernel has dimension six, and that kernel meets
`K_a` in zero.

**Proof.** All four images lie in the same six-dimensional space, so the sum
has rank at most six and nullity at least six. For `v in K_a`, the three
majority maps kill `v`. If their sum also kills `v`, the minority map kills
`v`, so `v` lies in `K_a intersect K_b = 0`. The sum's kernel is therefore
transverse to a six-dimensional subspace. Its dimension is at most six and at
least six, hence equals six; rank-nullity gives rank six. QED.

The deterministic 1,056-member sweep contains 538 lone-minority members and
finds zero theorem misses across all four weight-three patterns. The full
48/48 partition gives 389,160 same-class members, 1,660,416 lone-minority
members, and 1,272,384 even-split members, summing to 3,321,960.

## 5. Incidence and index-order comparator

The incidence and comparator both have block-rank profile `9/9/6/6/0` by
weight at both named primes, recomposing to rank 105. Over `F`, their kernel
meet profile is `3/0/3/0/12`, recomposing to 33. A single orbit table has
profile `12/12/10/6/0`; the weighted difference from the incidence is 39 and
is supported at weights zero, one, and two.

The incidence kernel classes at weight three are `0,0,0,1`; the comparator
classes are `0,1,1,1`. Both therefore satisfy the theorem with opposite
majority classes. Across the four weight-three patterns, the four common
six-dimensional images have joint rank 24 over `F`.

The pair-overlap histograms of the two members are equal. Among the 18,336 row
pairs the histogram is `0:15072, 1:1920, 2:960, 4:384`; among column pairs it
is `0:15168, 1:1728, 2:960, 3:192, 4:288`.

## 6. Image-subspace equality partitions

For each sign-pattern block over `F`, take the image subspace of each orbit
table. Equality of these RREF subspaces partitions the 96 tables. By weight,
the class counts are `3/6/3/1/1`, with class sizes
`32^3`, `16^6`, `32^3`, `96`, and `96`.

The weight-zero and weight-two equality partitions coincide. The weight-one
partition refines the three-class partition into two classes per fibre. At all
four weight-one patterns, the incidence and comparator class multisets occupy
disjoint classes and each has multiplicities `2/1/1`. The two-class fibre
involution carries the incidence multiset to the comparator multiset.

Numeric class values are first-appearance labels in deterministic orbit order.
They are meta convention; the equality partition, fibre relation,
multiplicities, and disjointness relation are invariant under relabeling.

Exactly 30,720 family members carry the incidence class multiset, both by the
binomial formula `C(16,2)*16*16` and exhaustive enumeration of all four-table
subsets. Among 368 one-part replacements of the incidence, 58 preserve that
multiset. Within the declared 1,056-member sweep, the weight-one incidence
multiset group has 13 members with rank histogram `9:1, 11:4, 12:8`; all sweep
group totals in the runner are explicitly scoped to that sweep.

## 7. Validation record and scope

The runner declares a 300-second audit timeout and exits nonzero on any failed
gate. Its cache is generated by the repository envelope. Mathematical gates
use Python integers, exact `Fraction` arithmetic, and the named finite fields;
resource measurements appear only in the final support line.

Independent review reconstructed the determinant census, exact-cover search,
noncooccurrence cliques, signed-coordinate action, and third-prime and exact-Q
linear algebra through independent implementations. Those checks reproduced
the central positive values, including the exact geometric pair census,
rank/image partitions, lone-minority sweep, and class-multiset counts.

Scratch-source mutations were executed without writing repository artifacts:

| Load-bearing family | Mutation | Rejecting gate |
|---|---|---|
| exact geometry | append a sample-disjoint interior-overlapping pair to the certified pair set | `F0` |
| group/action/table integrity | corrupt closure, transitivity, orbit size, or degree-two predicates | `F1` |
| flip blocks | corrupt the stacked character rank or equivariance | `F2` |
| top-weight and weight-three algebra | corrupt a rank, common-image, kernel-class, or kernel-meet value | `F3`-`F8` |
| lone-minority theorem | introduce a rank-ceiling exception or theorem miss | `F9`-`F11` |
| member profiles and counts | corrupt a class census, named-member profile, or rank recomposition | `F12`-`F16` |
| image partitions and fibres | corrupt class counts, refinement, fibre involution, or member count | `F17`-`F28` |
| cover representation | corrupt stabilizers, full-table cycles, containment, ceiling, or saturation | `F29`-`F34` |

The claim scope is the declared finite four-cube object and the coefficient
domains stated section by section. Independent audit is required before any
effective retained status or downstream use.

## Review record

- Combined review iteration 1 used one GPT-5.6-Sol/max reviewer across code,
  physics, proof, imports, no-go, labeling, retention, governance, and audit
  compatibility lenses.
- Review added the exact rational geometry certificate, fail-closed group and
  kernel-integrity predicates, declared timeout, field scopes, construction and
  convention inventory, exact target/DAG, positive finite boundary, and native
  artifact names.
- The exact immutable reviewed head and landing SHA belong in the PR provenance
  comment because a commit cannot contain its own hash.
- The citation-graph manifest is regenerated from the current landing tree.
- Independent audit remains the only route to an effective retained status.
