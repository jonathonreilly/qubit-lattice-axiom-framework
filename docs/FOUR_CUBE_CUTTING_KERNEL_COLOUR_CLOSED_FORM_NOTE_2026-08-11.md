# Four-cube cutting orbit tables: two kernel classes and a geometric colour rule

Date: 2026-08-11
Authority: none
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.

## Trace gate

- `trace_class: frontier_discovery`
- `target_claim_id: null`
- `target_blocker_text: null`
- `source_of_blocker_text: frontier_question`
- `reachability_to_target: unknown_frontier`
- `artifact_role: theorem`
- `next_trace_action: seek a characteristic-free structural explanation of the incidence rank; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact finite geometry and group-action identities, with modular claims restricted result by result to named fields`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object consists of the 16 vertices of the unit four-cube,
the five-vertex determinant-one simplices at adjacency-cost minimum 6, the
cuttings selected from that candidate class, and the 384 signed coordinate
maps of the cell. These are finite object choices, not imported physical
primitives. The generic 625-point lattice is an enumeration device; it is not
used as the geometric admissibility certificate.

There are no load-bearing literature, empirical, fitted, external-data,
framework-axiom, or repository-derived scientific inputs. NumPy and Python are
implementation dependencies and supply no scientific value. The field of
order 1000003 is the primary modular computation field. The field of order
1000033 is a replication control only for the gates that explicitly name it.

The linked runner
[four_cube_cutting_kernel_colour_closed_form_2026_08_11.py](../scripts/four_cube_cutting_kernel_colour_closed_form_2026_08_11.py)
rebuilds every finite object in this note without reading cached scientific
data. Its cache is only a reproducibility record.

## Exact target and proof obligations

The exact target is to classify the modular kernels of the 96 piece-cover
orbit tables for this declared four-cube cutting corpus, identify their
primary-field meet and stack rule, derive a geometric rule for the two-class
partition, and decompose the cover incidence table, with every coefficient
domain stated.

The obligation DAG is:

1. **Exact geometry (closed).** Enumerate the determinant-one candidates and
   prove that every selected 24-simplex set is a genuine cutting.
2. **Finite actions (closed).** Build the pieces, covers, signed-coordinate
   group, stabilizers, and 96 free piece-cover orbits.
3. **Kernel classes (closed at the named fields).** Construct the integer
   alternating cycle vectors, prove their independence and annihilation, and
   compare their row spaces over the primary field and replication field.
4. **Meet, module, and stack (closed at the primary field).** Identify the
   12-dimensional sign space, verify generator stability, and measure all
   same-class and cross-class stacks.
5. **Blocks and labels (closed).** Factor the two colour sums, name their row
   and column blocks by exact cell geometry, and verify equivariance.
6. **Incidence (closed at the named fields).** Express incidence as four orbit
   tables, count their colours, and measure the stated modular ranks.
7. **Boundary (closed).** Do not promote the result beyond the declared
   candidate class, fields, finite cell, or conventional class names.

All target obligations are discharged below and by named hard gates. The
strongest missing structural lemma beyond this target is a
characteristic-free explanation of the incidence rank 105 and its 87-
dimensional nullity. Those modular values are measured here; no general
mechanism for them is claimed.

## 1. Exact finite geometry

There are 2672 five-corner subsets of normalized simplex volume one. Of these,
400 attain adjacency-cost floor 6. The sample enumeration returns 15800
24-piece selections using 192 distinct pieces, each in 1975 selections, so

`24 x 15800 = 192 x 1975 = 379200`.

The sample lattice avoids every candidate facet and therefore makes the cover
search exhaustive inside the declared 400-simplex candidate class. A separate
integer certificate establishes geometric admissibility. Across all selected
cuttings, 15168 unordered simplex pairs co-occur. Every one is weakly separated
by at least one of the 80 nonzero normals in `{-1,0,1}^4`. Because every
simplex is full-dimensional, their strict interiors lie on opposite sides.
All vertices lie in the four-cube and the 24 normalized simplex volumes sum to
the cube's normalized volume 24. Thus every selected set is a genuine cutting;
shared boundary faces are allowed and strict-interior overlap is excluded.

The geometry mutation uses the two candidate simplices `(0,1,2,4,8)` and
`(0,1,3,7,15)`. Their sample masks are disjoint, but `(4,3,2,1)/11` is
strictly inside both. The exact separator predicate rejects this injected pair,
showing that the sample mask is not the proof oracle.

## 2. Pieces, covers, and orbit tables

The 192 eight-piece covers meet every cutting exactly once:

`8 x 1975 = 15800`.

The 384 signed coordinate maps act by distinct bijections, transitively on the
192 pieces and 192 covers and freely on the 36864 piece-cover pairs. The pairs
therefore split into 96 orbits of size 384. Each orbit is read as a 192 by 192
zero-one table over covers by pieces. Every table has two ones in each row and
column, so its bipartite graph is a disjoint union of 48 cycles of length 8.

On each cycle, alternating plus and minus one on its four piece vertices gives
an integer vector killed by the table. The 48 supports are disjoint, proving
independence. Thus every table has an exhibited 48-dimensional modular kernel.

## 3. Two modular kernel classes

At the primary field, canonical row reduction of the 96 exhibited kernels
gives exactly two subspaces, each carried by 48 tables. The same 48/48 split is
reproduced at the field of order 1000033. At both fields the two exhibited
kernels have join dimension 84, hence meet dimension

`48 + 48 - 84 = 12`.

This is a result over the two named fields, not a claim about characteristic 2,
all characteristics, or equality of integral lattices. The integer
annihilation of each table's own alternating basis is stronger and is checked
before modular reduction.

The 16 pure flips act freely on the pieces with 12 orbits. Alternating by the
flip sign on each orbit gives 12 independent integer vectors. Every orbit table
kills them over the integers. At the primary field these vectors span the
12-dimensional meet. The trivial-character orbit vectors also have rank 12,
but meet every kernel trivially at the primary field and remain alive under all
96 tables.

## 4. Primary-field submodules and stacks

Seven maps generate all 384 signed coordinate maps. At the primary field all
672 images of the two representative kernel bases under these generators stay
in the corresponding kernel. The two kernels are therefore submodules over
that field.

At the same field, stacking all 48 tables of either class gives rank 144, equal
to every single-table rank. All 2256 same-class pairs stay at 144. All 2304
cross-class pairs have rank 180, equal to `192 - 12`. These submodule and
stack claims are not promoted to untested characteristics.

## 5. Exact block factorisation and geometric label

Let `A` and `B` be the entrywise sums of the 48 tables in the two modular
classes. Their sum is the all-ones matrix. Each has four distinct rows, each
shared by 48 covers, and six distinct columns, each shared by 32 pieces. They
are constant on the resulting 24 blocks. The 4 by 6 patterns are complementary,
have row sums 3 and column sums 2, and contain a determinant-2 minor. Therefore
their rank, and the rational rank of `A` and `B`, is exactly 4. The two named
large-prime computations agree with that exact certificate.

Each cover has a unique non-identity fixer, a flip of one coordinate axis. The
four resulting axis labels are exactly the four row blocks. For a piece, count
its five corners on each side of each axis and take `min(k,5-k)`. The maximum
is attained on exactly two axes. Those six unordered axis pairs are exactly the
six column blocks. Both labels are equivariant under every signed coordinate
map.

For every piece-cover pair, membership of the cover axis in the piece's axis
pair is constant on its orbit. It splits the 96 orbits 48/48 and agrees with the
two modular kernel classes up to one global swap. The names `0` and `1` are
conventional; only the partition and its geometric rule are intrinsic.

Two further bounded fibre censuses are recorded without route-exclusion force.
The adjacent-corner statistic is constant on the 192 pieces, while fixer weight
has three fibres. The shared-corner profile has 25 fibres, 21 of which contain
both observed colours. These are positive facts about this finite corpus and do
not foreclose other label mechanisms.

## 6. Incidence decomposition

The cover incidence table is the entrywise sum of four of the 96 orbit tables,
three from one class and one from the other. Every cover contains eight pieces,
six carrying its own axis; every piece lies in eight covers, six carrying one
of its two axes.

At the primary field, stacking the four constituent tables has rank 180. Their
entrywise sum has rank 105 at both named fields and nullity 87. The rank drop is
localized to addition, but this note offers no characteristic-free explanation
for it.

## 7. Mutation record and fail-closed behavior

Six load-bearing mutation gates operate only on copied in-memory objects; the
canonical data are never changed. They inject and reject:

1. the exact overlapping-simplex pair described in section 1;
2. a duplicated image in a copied non-identity stabilizer action;
3. one changed entry in a copied cycle-kernel basis;
4. independent corruptions of a copied sign-meet basis, generator image, and
   table stack;
5. one shifted copied piece-axis label; and
6. one flipped copied incidence entry.

Each mutation is passed through the corresponding production predicate. If a
corruption is not rejected, its mutation gate fails and the final process exits
nonzero. The runner also retains its narrower controls for alternate kernels,
trivial-character vectors, index-order sums, and shifted labels; those controls
are not substitutes for the mutation record.

## 8. Boundary

- The adjacency-cost floor is a declared selector. No classification of all
  determinant-one simplices or all four-cube triangulations is claimed.
- Full dimensionality is guaranteed by determinant magnitude one. Weak
  separation permits common boundary faces but excludes strict-interior
  overlap; degenerate simplices are outside the object.
- Primary-field-only results are the sign-space equality, submodule checks,
  all same/cross stack ranks, and the four-orbit stack rank.
- Replicated two-field results are the two kernel classes, kernel join, colour
  sums, block patterns, and incidence-sum rank. Agreement at two primes is not
  promoted to a universal-characteristic theorem.
- Exact integer results include the separating normals, cycle and sign-vector
  annihilation, colour-sum annihilation, group and incidence identities, and
  all combinatorial counts. The determinant-2 block minor proves rational rank
  4 for the colour sums.
- Characteristic 2 and every untested characteristic are excluded. No physical
  dynamics, continuum limit, lattice-wide construction, uniqueness statement,
  empirical comparison, axiom amendment, or retention verdict is claimed.
- The geometric colour rule does not derive which four orbit tables form the
  incidence matrix. Their selection is read from the finite object.
