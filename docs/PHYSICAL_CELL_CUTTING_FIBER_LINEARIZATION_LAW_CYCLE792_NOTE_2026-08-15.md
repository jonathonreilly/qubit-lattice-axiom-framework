# The fiber linearization law: every wall fiber cover problem is a coset minimum-weight problem

Date: 2026-08-15
Authority: none
Audit: unset
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
- `next_trace_action: derive the single fiber-independent weight census, or at least the parity of its minimum-weight count, from the kernel and its coset alone, beginning with whether the pairwise-distinct row systems carry one census because their kernel-and-coset pairs are equivalent under a relabelling of rows; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, at every wall fiber of the declared finite cell, of the rank and kernel of the fiber's point-row incidence over the field with two elements, of the coset carrying its cover solutions, of the weight census of that coset, of the identification of the fold-held cuttings with the coset minimum-weight members and with its exact covers, and of the complete refutation of translation carriers at both the fiber and the native level; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the
unit four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive
at the adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into,
the 192 pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell.
The pair of tetrahedral letters on the two slots of axis zero, drawn from a 16-letter alphabet,
gives the interface matrix of trace 2000 with exactly 48 entries equal to 36. Each of those 48
fibers holds 36 cuttings and is held setwise by exactly 2 of the 384 maps. Its nontrivial holder
is that fiber's fold; the 48 folds are involutions and collapse to 6 distinct maps with serving
census `{8: 6}`, and each fold holds 14 of its own fiber's 36 cuttings.

The stem `PHYSICAL_CELL_CUTTING_SINGLE_FIBER_COVER_RIGIDITY_CYCLE791_NOTE_2026-08-15` is not yet
on main and is referenced by name only. On one sample fiber it determined the whole group of row
permutations preserving the cover instance, found the induced group on the 14 to have order 2 with
no free involution among its elements, and found the only geometrically carried element to be the
identity — so no permutation symmetry of that instance accounts for the evenness of 14. Its named
entrance was to leave group actions and take the linear structure over the field with two
elements. This note takes it, and takes it at all 48 fibers rather than one.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from that object alone: it rebuilds the object from the corner
list before any gate runs, uses the standard library only, performs no file input or output and no
randomness, and gates each recomputed value against the value stated here.

## The law

- **Per-fiber linearization.** Each fold cuts the 400 kept pieces into 200 two-orbits, with 0
  singletons and 0 two-orbits whose two pieces share an interior sample point. Each of the fiber's
  14 fold-held cuttings is an exact union of exactly 12 of those two-orbits, and exactly 40 of the
  200 occur across the 14, so each held cutting is a weight-12 vector over the field with two
  elements on 40 rows. Let N be the 625 by 40 point-row incidence matrix. At every one of the 48
  fibers the rank of N is 32 and its kernel has dimension 8; the kernel is an even-weight code,
  all 256 of its vectors having even weight; and the 13 differences of the held vectors from the
  first all lie in the kernel and span it entirely. The affine hull of the 14 solutions is
  therefore the full 256-element coset, and all 256 of its members solve the all-ones system.

- **The exact characterization.** Exact cover in the integer sense — every one of the 625 sample
  points lying in exactly one selected row — forces the all-ones system over the field with two
  elements, so every exact cover of a 40-row instance lies in that coset. Inside the coset the
  minimum weight is 12, the weight-12 members are exactly the 14 held vectors, and the members
  that are genuine exact covers are exactly the same 14. Hence each 40-row instance has exactly
  14 exact covers and they are the fiber's 14 fold-held cuttings: the count 14 is a coset
  minimum-weight count.

- **The universality.** One and the same weight census
  `{12: 14, 14: 11, 16: 37, 18: 29, 20: 55, 22: 45, 24: 51, 26: 11, 28: 3}` — 1 distinct census
  over the 48 fibers, of total 256 — while the 48 instances are pairwise distinct objects: 48
  distinct fold-and-row-set pairs, 48 distinct 14-solution systems, and 672 held cuttings in the
  union, which is 48 times 14, so no cutting is held in two fibers. Within a fold the 8 served
  fibers share rows with census `{12: 24, 14: 24, 18: 48, 20: 24, 22: 48}` over the 168 within-fold
  pairs: between 12 and 22 of the 40 rows in common, never all 40.

- **The refuted translation.** A nonzero vector that translates the 14-solution set onto itself
  must carry the first solution into the set, so the 13 differences are the complete candidate
  list — nothing outside it can translate. All 13 fail at every fiber: 0 of 624 tests pass. The
  same refutation holds natively, before any fiber is singled out: the sample fold holds 336 of
  the 15800 cuttings, each an exact union of 12 of its 200 two-orbits, and of the 335 candidate
  translations of that 336-element system, 0 pass. Together with the previous cycle, the parity
  carrier of the evenness of 14 is neither a permutation symmetry of the instance nor a
  translation of its solution set.

## What the wall now asks

The wall question was "why is 14 even". It is now exactly "why is the minimum-weight count of this
one census even" — and it is one question rather than 48, because the census does not depend on
the fiber even though the 48 instances are pairwise distinct. The cover problem has been replaced
without residue by a coset problem: a kernel of dimension 8 over the field with two elements, one
coset of it, and the count of minimum-weight members in that coset. Nothing about the parity of
that count follows from what is proved here; what follows is that the parity question may now be
asked of a linear object of dimension 8 rather than of a cover search over 400 pieces.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: the weight census itself; the rows-per-point
census `{2: 235, 3: 108, 4: 186, 5: 64, 6: 32}` of the sample fiber at letter pair `(0,4)`; the
rank 32 and the kernel dimension 8; the within-fold row-sharing census; and, above all, the
per-fiber count 14, whose evenness remains measured, not derived.

Derived at the declared finite scope: that each fiber's cover problem is exactly a coset
minimum-weight problem, since the weight-12 members of the coset and its exact covers are the same
14 vectors at all 48 fibers; that the affine hull of the 14 is the whole coset, since the 13
differences span the full kernel; that the count of exact covers of each 40-row instance is
exactly 14; that the 48 instances are pairwise distinct while carrying 1 census; and that no
nonzero translation preserves any of the 48 solution systems or the native 336-element system,
the candidate lists of 13 and of 335 being complete.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

## Next entrance

Derive the census — or at least the parity of its minimum-weight count — from the kernel and its
coset alone. The first recon question is whether the 48 pairwise-distinct row systems carry one
census because the 48 kernel-and-coset pairs are equivalent under a relabelling of rows, and if
so, what carries that equivalence: the cell group cannot, since it already fails to move one
fiber's solutions. If the equivalence is real but uncarried by the cell group, the parity question
descends to a single kernel of dimension 8 and its distinguished coset, where a weight-count
argument has room to work. Nothing about the outcome is claimed here.

## Review record and boundary

- Rows are the two-orbits of the 400 kept pieces under each fiber's own fold, and solutions are
  that fiber's fold-held cuttings written as row sets. Both conventions are fixed before any
  computation runs, and every statement is made for all 48 fibers, not for a chosen one.
- Membership of the exact covers in the coset is not assumed from the standard linear-algebra
  containment: the runner checks all 256 coset members against the all-ones system and against the
  integer exact-cover condition point by point, and separately verifies each of the 14 held
  cuttings as an exact cover of the 625 sample points.
- The candidate lists for a translation are complete by the argument stated, so 0 passes refutes
  translation carriers outright rather than reporting a failed search.
- The runner prints censuses and counts; the incidence matrices, the row lists and the solution
  vectors are not printed, so the note quotes censuses and identities instead.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run
[physical_cell_cutting_fiber_linearization_law_cycle792_2026_08_15.py](../scripts/physical_cell_cutting_fiber_linearization_law_cycle792_2026_08_15.py).
The reviewed cached output belongs at
[physical_cell_cutting_fiber_linearization_law_cycle792_2026_08_15.txt](../logs/runner-cache/physical_cell_cutting_fiber_linearization_law_cycle792_2026_08_15.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes in
well under a minute on the reference machine, and stays far below one gigabyte. Its final line is
`TOTAL: PASS=12 FAIL=0`, and it exits nonzero if any gate fails.
