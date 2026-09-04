# Physical cell cutting: the identification survives the proper-rotation half

Date: 2026-08-11
Authority: none; self-contained finite construction proposed for independent audit.
Audit: unset.
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.

Primary runner:

- [proper-rotation-half runner](../scripts/physical_cell_cutting_proper_rotation_half_cycle778_2026_08_11.py)

Cached output:

- [proper-rotation-half runner cache](../logs/runner-cache/physical_cell_cutting_proper_rotation_half_cycle778_2026_08_11.txt)

Direct scientific dependencies: none.

## Trace and status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "test whether this bounded finite identification has a canonical downstream consumer; none is claimed here"
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite geometry and group-action identities on one declared cell-cutting object"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs, exact target, and proof obligations

The finite definitions are the vertex set `{0,1}^4`, five-vertex simplices with absolute
determinant one, minimisation of the stated adjacency cost, the declared rational sample, the
cover condition, and the signed-coordinate action. These choices define the object; they are
not imported physical primitives. The determinant, finite group-action identities,
orbit-stabiliser counting, and binomial coefficients are standard finite mathematics and are
also checked constructively where they bear on a reported number. Python's `itertools`,
`sys`, and exact `fractions.Fraction` implementation are code dependencies, not scientific
inputs.

There are no load-bearing literature, empirical, fitted, external-data, ancestral-runner, or
repository-derived scientific inputs. The motivating statement that a lattice premise permits
proper rotations is context only: this note neither imports that premise nor identifies its
group with the determinant-plus-one subgroup used here. The labels `c773`-`c777` below are
provenance shorthand only. The primary runner reads no repository data and reconstructs every
load-bearing finite object.

**Exact target.** For the declared unit-four-cube simplex object and the determinant-plus-one
subgroup of its signed-coordinate action, prove that the cover-incidence table belongs to a
two-member intersection of the exhaustive row and column censuses, and separately count the
incidence-intertwining equivariant-bijection pairs as two.

The obligation graph has no external lemma node:

1. **Finite-object obligation — proved here.** Enumerate the candidate simplices and
   sample-selected solutions, prove the enumeration includes every genuine cutting in the
   declared candidate class, and certify that every selected solution is a genuine cutting.
2. **Action obligation — proved here.** Construct the signed-coordinate action, compute its
   determinant by two independent formulas, establish the index-two subgroup, and determine
   its piece, cover, and pair orbits and stabilisers.
3. **Family obligation — proved here.** Derive the orbit-table degrees, the `96+96` split, the
   binomial family size, and the exact table decomposition of the cover incidence.
4. **Census obligation — proved here.** Enumerate the complete row and column censuses by
   fixed-row and fixed-column reductions and compute their intersection.
5. **Equivariant-map obligation — proved here.** Enumerate all equivariant bijections on both
   sides and test every candidate pair for the incidence-intertwining identity.

The gates cited below discharge these obligations for this one finite object. No obligation is
claimed for a different cell, candidate class, cost function, acting subgroup, physical
dynamics, or lattice-wide construction.

## What is shown

This note tests the cover identification carried by the declared finite cell-cutting object after
removing the orientation-reversing half of its signed-coordinate action. Restricting the 384 maps to
the determinant-plus-one subgroup of order 192 kills the cover stabiliser, splits the pieces into two
orbits of 96, and enlarges the ambient family of candidate labellings from 3321960 to 11035418241600.
The two-sided conditions still cut that enlarged family down to exactly 2 members, with the cover
incidence among them. A second calculation, which shares the reconstructed object, actions, and
incidence but does not consult the family or either census, finds exactly 2 central
incidence-intertwining pairs. It independently confirms the cardinality, not an equality between these
two different result types. Everything below concerns the one explicitly rebuilt finite object; the
primary runner rebuilds it from the corners of the four-cube upward and prints 17 gates, J0 through J16.

## The object

The object, also studied under the provenance labels `c773`-`c777`, is the unit four-cube; its 2672
five-corner simplices of absolute determinant one; the 400 of those at adjacency-cost floor 6; the 15800
cuttings of the cube into 24 such simplices; the 192 pieces that occur in some cutting, each of them in
1975 cuttings; and the 192 covers, a cover being 8 pieces that meet every cutting exactly once. The acting
group is the 384 signed-coordinate maps, 24 axis moves times 16 sign flips, acting on pieces and covers.
The cover incidence is the 192-by-192 zero-one matrix recording which pieces lie in which cover.
Throughout, the holder of a point means its stabiliser, the maps that leave it fixed.

The rational sample avoids every candidate-simplex facet, so every genuine cutting in the declared
candidate class appears in the sample-cover enumeration. The converse is certified independently in
gate J0. Across all enumerated solutions there are 15168 co-occurring simplex pairs; every pair is
weakly separated on its vertices by at least one of the 80 nonzero normals in `{-1,0,1}^4`. Because the
simplices are full-dimensional, their interiors lie on strict opposite sides. Each solution contains 24
absolute-determinant-one four-simplices, whose volumes sum to the unit four-cube volume. Thus every
sample-selected solution is a genuine cutting.

## The stabiliser determinant law

A signed coordinate map is an axis move together with a flip mask. Its linear part carries, in the row of
each output axis, a single entry equal to one minus twice that axis's flip bit, in the column of the axis
the move reads. The determinant of that matrix, by cofactor expansion, is the sign of the axis move times
minus one to the number of flipped axes. The runner builds all 384 matrices, checks each one against the
map it is supposed to be on all 16 corners, and takes all 384 determinants by cofactor expansion: 384 of
384 agree with the sign-times-parity formula, and the same comparison run with the flip parity dropped
disagrees on 192 of them, so the check discriminates rather than holding by construction.

A holder of order 2 survives the restriction exactly when its second map has determinant plus one. The
cover holder generator is a single-axis flip, determinant -1, and dies. The piece holder generator is not
a flip, determinant 1, and lives.

## What the restriction does to each side

The determinant plus one half is closed, has order 192 and index 2, and is normal under all 384
conjugations; the cover holder generator has determinant -1 and the piece holder generator has
determinant 1. Under the half, the 192 covers form one regular orbit of 192 with holder of order 1, and
the 192 pieces form two orbits of 96 with holder of order 2.

The two outcomes are not interchangeable, and the runner shows that by cross-applying the rules. The
piece generator's determinant rule applied to the cover side predicts 2 orbits against the measured 1,
and the cover generator's rule applied to the piece side predicts 1 against the measured 2. Both cross
predictions are wrong and each side's own rule is right.

## The enlarged family

The action on pairs of a piece with a cover is free: 192 orbit tables, every orbit of size 192, together
partitioning the all-ones 192-by-192 matrix of 36864 entries. Each table has row degree 1 and nonzero
column degree 2. Those degrees are measured, not derived, and the census convention is then read off from
them rather than assumed: a row of the incidence sums to 8, and 8 over the row degree 1 wants 8 labels
appearing once each; a column sums to 8, and 8 over the column degree 2 wants 4 labels appearing twice
each.

The tables split 96 and 96 by which piece orbit they target, and a table meets every piece of its own
orbit exactly 2 times. Any union of 4 tables from one group with 4 from the other is therefore 8-regular
on both sides, and the legal ambient family has size C(96,4)^2 = 11035418241600, the square of the
full-group family C(96,4) = 3321960. Restricting the symmetry input makes the space of candidate
labellings larger, not smaller, which is why the identification below is a stronger statement than the
full-group one and not a weaker one.

The cover incidence itself meets exactly 8 of the 192 tables, 4 from each group; each met table lies
wholly inside the incidence, and the 8 sum back to it exactly.

## The two censuses and the crossing

Row side: a candidate passes when, at every one of the 192 covers, the 8 pieces its tables select are
themselves a cover. At a fixed cover the table-to-piece map is a bijection, so the candidates are exactly
the 192 covers, and every one of them passes. The row census has 192 members, one for each cover, and
each member draws 4 tables from each of the two groups.

Column side, taken one piece orbit at a time: at an orbit representative, the 96 tables of that group cut
the 192 covers into pairs, so a member of the column census is pinned by a piece column that the piece
holder leaves alone. There are 16 such columns, they yield 16 members on each orbit, and 256 in product.
The two representatives can be chosen to share the same holder, which is what makes the per-orbit count
the same 16 on both sides.

The row census and the column census cross in exactly 2 members, and the cover incidence is in the row
census and in the crossing.

## The separately counted equivariant-map route

This route shares the declared finite object, actions, and incidence, but consults neither the family,
the censuses, nor the orbit tables. Because the covers are one free orbit, an equivariant map on the
cover side is pinned by the image of a single cover, giving 192 of them.
On the piece side an equivariant map is pinned by one image per orbit, and each image must be left alone
by that orbit representative's holder: 256 well-defined maps, of which 128 are bijections, 64
orbit-preserving and 64 orbit-swapping. Equivariance is gated explicitly on all 192 maps of the legal
half rather than inherited from the way the maps are built. Of the 24576 pairs of a cover map with a
piece map, exactly 2 satisfy the intertwining condition, and each of those 2 is the pair of actions of
one of the 2 central maps of the full group. This calculation returns a different kind of object from
the census intersection and independently reaches the same cardinality two.

## Normalizer arithmetic

The two orbit representatives share the same holder generator. Its class in the full group has size 12
and does not split under the restriction. Its full-group centraliser has order 32 and is not contained in
the legal half, so the legal normalizer has order 16, giving per-orbit index 8. The generator fixes 16
pieces, 8 in each orbit, and 0 covers. The cover holder generator's centraliser has order 96, and it
fixes 0 pieces and 48 covers. This is the arithmetic behind the asymmetry: the piece side keeps a holder
and gains an orbit label, the cover side loses its holder and becomes free.

## Boundary

- This is a statement about a finite object and the symmetry input that object is given. It does not
  claim that the determinant-plus-one subgroup is the group supplied by a lattice premise. It proves
  only that the stated finite cardinality survives when the orientation-reversing maps are removed from
  this declared action.
- The census intersection contains 2 table subsets, not 1, and the runner makes no canonical selection
  between them. The equivariant-map calculation separately returns the 2 action pairs induced by the
  centre of the full signed-coordinate group. The two result sets have different types; no bijection
  between them is claimed here.
- The 96 and 96 piece split is real, but the two orbits are isomorphic as legal-half sets: there are 64
  bijections between them, and any orientation-reversing map exchanges the two-orbit decomposition.
  Four local label candidates were tested — sorted determinant sign, count of even-parity corners,
  corner index sum parity, and total coordinate sum parity — and none is invariant under the action or
  constant on either orbit. This finite negative control is not an exhaustive invariant search and does
  not establish a no-go or a named wall.

## Honest auditor read

- The claim is bounded to this finite object. Nothing here asserts that the physical symmetry input is
  exactly the determinant plus one half. The load-bearing point is the insensitivity to the difference,
  and that is what the gates measure.
- Gate J0 closes both directions of the cutting construction: the generic sample makes the search
  exhaustive over genuine cuttings in the candidate class, while the exact separator and volume checks
  establish that every selected solution tiles the cell.
- Three of the gates are built as rejectors rather than confirmations. The determinant gate fails if the
  determinant is taken by any proxy that ignores the flip mask, since the parity-dropped comparison must
  disagree on a nonzero count and it disagrees on 192. The cross-swap gate fails if the two holder
  generators are handed the same determinant, which is exactly what such a proxy would do. The
  perturbation gate attacks the answer directly: each of the 8 tables of the cover incidence is swapped
  for a different table of the same group, 760 single swaps in all, and every one of the 760 is rejected
  by the row-census test.
- The candidate-invariant gate passes by correctly reporting a negative, and it is written so that a
  genuine separating invariant would make it fail rather than pass.
- The runner rebuilds the object from the four-cube corners upward, reads no stored data, and prints what
  it measures. Its proof does not import the earlier cycle labels, and the run is reproducible byte for
  byte through the cache envelope.

## Reproduction

Run the [primary runner](../scripts/physical_cell_cutting_proper_rotation_half_cycle778_2026_08_11.py).
The reviewed output is the [machine-generated cache](../logs/runner-cache/physical_cell_cutting_proper_rotation_half_cycle778_2026_08_11.txt).
The runner declares `AUDIT_TIMEOUT_SEC = 300`, uses exact integer and rational arithmetic, and exits
nonzero if any gate fails. The independent audit lane must rerun it live; this review cache is not an
audit verdict.

## Review record

- Review iteration 1 (Codex review-loop, 2026-09-03) required the exact simplex-separation/volume
  certificate, reconciled the lattice-context wording, supplied the import and proof contracts, and
  narrowed the claimed relationship between the census and equivariant-map routes to their independently
  established common cardinality.
- The four failed label candidates remain a bounded mutation-style control; no exhaustive negative or
  no-go conclusion is retained.
- The exact immutable reviewed head and landing SHA are recorded in the PR review comment because a
  commit cannot contain its own hash.
- Independent audit of claim
  `physical_cell_cutting_proper_rotation_half_cycle778_note_2026-08-11` remains required before any
  effective retained status or downstream use.

Within these boundaries, the review classification is **bounded support** for the declared exact finite
object.
