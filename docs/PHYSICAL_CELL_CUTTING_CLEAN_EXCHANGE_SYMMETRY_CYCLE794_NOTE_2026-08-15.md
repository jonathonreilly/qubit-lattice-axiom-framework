# The clean exchange: four minimal exchanges, one of them the whole symmetry, and the parity of fourteen down to two cuttings

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
- `next_trace_action: read the anatomy of the two held cuttings that the dominant exchange leaves unpaired — what distinguishes them from the twelve it pairs, whether the kernel vector joining them is itself structured, and whether a natively named involution pairs them, since such a pairing would carry the evenness of fourteen outright; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, at every wall fiber of the declared finite cell, of the graph of minimal exchanges on the fold-held cuttings, of the equality of its edge differences with the weight-four vectors of the fiber's own kernel, of the closure of the held set under the four toggles those vectors define, of a derived lemma carrying the unique clean toggle to a coordinate-level self-equivalence verified by explicit image on cuttings, kernel and coset, of a complete backtracking search showing that toggle is the instance's entire nontrivial symmetry, and of the parity descent that pairs twelve of the fourteen held cuttings and localises the evenness of fourteen to two of them; the point cardinalities of the equal-union exchanges are fiber-dependent and are anchored as a measured census over the fibers, never as one value; no physical or lattice-wide identification`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the unit
four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive at the
adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into, the 192
pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell. The pair
of tetrahedral letters on the two slots of axis zero, drawn from a 16-letter alphabet, gives the
interface matrix of trace 2000 with exactly 48 entries equal to 36. Each of those 48 fibers holds
36 cuttings and is held setwise by exactly 2 of the 384 maps; its nontrivial holder is that fiber's
fold, and each fold holds 14 of its own fiber's 36 cuttings.

The stem `PHYSICAL_CELL_CUTTING_WALL_INSTANCE_UNIQUENESS_CYCLE793_NOTE_2026-08-15` is not yet on
main and is referenced by name only. It put the 48 per-fiber systems into one instance up to
relabelling of the 40 rows, carrying exactly 2 self-equivalences. Everything that rests on is
rebuilt here rather than assumed and regated at all 48 fibers: each fold cuts the 400 kept pieces
into 200 two-orbits, each held cutting is an exact union of 12 of them, exactly 40 of the 200 occur
across the 14, the 625 by 40 point-row incidence over the field with two elements has rank 32 and
kernel dimension 8 with all 256 kernel vectors of even weight, every one of the 256 coset members
solves the all-ones system, each of the 672 held cuttings covers each of the 625 sample points
exactly once, and the pairwise shared-row census over the 91 pairs is
`{0: 12, 1: 6, 2: 10, 3: 14, 4: 4, 5: 14, 6: 4, 7: 5, 8: 10, 9: 1, 10: 11}` at every fiber.

The question this note asks is which exchanges of rows carry held cuttings to held cuttings, which
of those extend to symmetries of the whole instance, and how far the evenness of 14 can be pushed
down by them. The answer is that there are exactly four such exchanges, that exactly one of them is
clean, that the clean one is the instance's entire nontrivial symmetry, and that the largest of the
four pairs 12 of the 14, leaving the parity of 14 carried by exactly two named cuttings.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from that object alone: it rebuilds the object from the corner list
before any gate runs, uses the standard library only, performs no file input or output and no
randomness, and gates each recomputed value against the value stated here.

## The law

- **The minimal exchanges are the light kernel vectors.** Call two held cuttings a minimal exchange
  when they share 10 of their 12 rows. At every fiber there are exactly 11 such pairs; as a graph on
  the 14 they give degree census `{0: 1, 1: 4, 2: 9}` and five components of sizes 4, 4, 3, 2 and 1,
  with both components of size 4 being closed cycles of 4 edges. Every difference of two held
  cuttings lies in the kernel, both being coset members. The 11 edge differences all have weight 4
  and take exactly 4 distinct values, with multiplicities 6, 2, 2 and 1, and those 4 values are
  exactly the 4 kernel vectors of weight 4 — the light part of the kernel is not merely where the
  minimal exchanges live, it is exactly what they are. The unique pair sharing 9 rows differs by the
  unique kernel vector of weight 6, and over all 91 pairs the multiplicity census of distinct
  differences is `{1: 25, 2: 30, 6: 1}`, single-valued over the 48 fibers.

- **Each of the four is an equal-union exchange, and the held set is closed under all four toggles.**
  Search the 40 rows directly for unordered pairs of disjoint two-row halves, each half a pair of
  rows disjoint as point sets, whose two halves have equal union as point sets. There are exactly 4
  at every fiber and their four supports are exactly the 4 kernel vectors of weight 4, so the
  minimal exchanges are found twice over by independent routes: once as differences of held
  cuttings, once as a bare point-set enumeration on the rows that never looks at the 14. Toggling by
  such a vector — swapping one half for the other in any held cutting that contains a half in full —
  lands inside the held set every time, with 0 images outside at every fiber. The moved census over
  the four is `{2: 1, 4: 2, 12: 1}`, the census of broken cuttings, those meeting a support in a
  nonempty set that is not a full half, is `{0: 1, 2: 1, 4: 1, 6: 1}`, and for every distinct pair
  difference the number of held cuttings moved equals 2 times its multiplicity. The
  multiplicity-6 exchange meets all 14 held cuttings; none is disjoint from its 4 rows.

- **The lemma: a clean exchange extends to a coordinate-level self-equivalence.** Call an exchange
  clean when its broken count is 0, that is, when every held cutting meeting its support contains a
  full half. Pair the two halves by either of the two bijections between them. A held cutting
  containing one half in full maps to the cutting with the other half substituted, which is again
  held, by closure. Every other held cutting meets no row of the support at all, by cleanliness, so
  it is fixed row by row. Hence the 14-set is carried onto itself; since the differences of the 14
  span the kernel and their affine hull is the coset, kernel and coset are carried onto themselves
  as sets. Both half-pairings therefore give self-equivalences. This is a derivation, not a
  measurement, and the runner nevertheless verifies both pairings by explicit image: the 14 held
  cuttings onto the 14, all 256 kernel vectors onto the kernel, all 256 coset members onto the
  coset, at 48 of 48 fibers.

- **The selector is cleanliness, and it accounts for the whole symmetry.** Exactly 1 of the 4
  exchanges is clean at every fiber; it has multiplicity 2 and moves 4 cuttings. It is not the
  exchange of largest multiplicity, which is 6, and it is not picked out by the sizes of its halves,
  which are 2 and 2 for all four; cleanliness is the selector and nothing else in the census
  distinguishes it. Running the complete backtracking search for self-equivalences of the instance
  against itself returns exactly 2 at every fiber, and its nontrivial member is precisely the clean
  exchange's toggle: the induced permutation of the 40 rows fixes 10 blocks identically as sets and
  has 2 two-cycles, the same permutation for either half-pairing. So the instance's entire
  nontrivial symmetry is one clean equal-union exchange of two rows for two rows.

- **The parity descent.** For any nonzero kernel vector the map that adds it is a fixed-point-free
  involution of the 256-member coset, so the held cuttings it moves are paired two by two and their
  number is even; over all 255 nonzero kernel vectors the runner confirms that number is even and
  equals 2 times the multiplicity of the vector. Hence 14 has the same parity as the number of held
  cuttings the vector leaves unpaired, for every nonzero kernel vector, and the way to make the
  evenness of 14 small is to make that multiplicity large. The maximum multiplicity over all 255 is
  6, attained by exactly 1 vector, and 0 vectors attain 7 or more — a multiplicity of 7 would pair
  all 14 at once and make the instance a translation of itself, and the measured maximum refutes
  that natively, with no appeal outside the object. So 14 = 6 pairs + 2: the dominant exchange pairs
  12 of the 14, and the evenness of 14 is now the evenness of the 2 cuttings it strands, which are
  exactly its 2 broken cuttings and have graph degrees 0 and 1.

## Derived versus measured

Derived at the declared finite scope. Two held cuttings each cover the 625 points exactly once, so
after deleting their shared rows the two remainders cover the same point set: equal-union
remainders are forced, not observed, and the equal-union exchanges are the minimal instance of that
remainder lemma. The clean-exchange lemma above is derived in full, both half-pairings with it. The
evenness of the number of held cuttings moved by a nonzero kernel vector is derived, from
fixed-point-freeness of adding a nonzero vector on a coset. And the congruence that 14 has the same
parity as the count of cuttings left unpaired follows from that evenness for every nonzero kernel
vector at once.

Measured, not derived, at the declared finite scope: that there are exactly 4 minimal exchanges,
that exactly 1 of them is clean, that the self-equivalence count is 2, the whole shape of the
minimal-exchange graph and all of the censuses quoted above, the maximum multiplicity 6 and its
attainment by exactly 1 vector, and, above all, the count 14 itself, whose evenness remains
measured, not derived. The descent moves that evenness from 14 cuttings onto 2, and does not
discharge it.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

## What the wall now asks

Why does the dominant exchange strand exactly two held cuttings? Everything else about it is now
named: it is the kernel vector of weight 4 of multiplicity 6, it meets all 14 held cuttings, and it
pairs 12 of them. The 2 it does not pair are exactly its 2 broken cuttings, they are the vertices of
degree 0 and degree 1 in the minimal-exchange graph, and they share 8 of their 12 rows, so the
kernel vector joining them has weight 8, single-valued over the 48 fibers. A natively named pairing
of those two — any involution of the instance exchanging them, or any reason forcing them to come in
a pair — would carry the evenness of 14 outright, because the rest of the 14 is already paired by
the dominant exchange. The wall is no longer "why is 14 even"; it is "why are these two cuttings
two".

## Next entrance

Read the anatomy of the two exceptional cuttings. They are now distinguished objects rather than
two of 14: one is the isolated vertex of the minimal-exchange graph, the other an endpoint of a
path, they share 8 of their 12 rows, and the kernel vector joining them is not one of the 4 light
ones. What is worth reading next is whether that joining vector has any distinguished place in the
kernel, whether the two cuttings differ from the other 12 by any invariant of the instance rather
than of a labelling, and whether any involution of the instance, or of the cell's 384 maps acting on
the fiber, exchanges them. Whether such a pairing exists is not claimed here; what is claimed is
that the parity target has shrunk from 14 cuttings to 2.

## Review record

- Rows are the two-orbits of the 400 kept pieces under each fiber's own fold, and blocks are that
  fiber's fold-held cuttings written as row sets. Both conventions are fixed before any computation
  runs, and every statement is made for all 48 fibers, not for a chosen one; every census is a
  multiset, never a list of row labels, and the runner gates that each takes exactly 1 distinct
  value over the 48 fibers.
- Equal-union tests compare actual point sets as bitmasks over the 625 sample points, never sizes;
  cover tests are point-by-point in the integer sense; the kernel is computed by row reduction over
  the field with two elements of each fiber's own incidence, never carried between fibers.
- The point cardinalities of the equal-union exchanges are fiber-dependent; the runner's G5 gate is
  anchored to the full measured census over the 48 fibers, never to a single sample-fiber value.
  The four union sizes read 50 100 100 100 at 8 fibers, 100 100 100 100 at 32 and 100 100 100 175 at
  8; the two three-row remainders of the pair sharing 9 rows have equal point union at 48 of 48
  fibers, of size 120 at 8 fibers, 150 at 32 and 205 at 8. A row's point support depends on which
  pieces its fiber uses, so these cardinalities are properties of a labelling and not of the
  instance. What is single-valued and holds at 48 of 48 is the enumeration itself: exactly 4
  equal-union exchanges, halves disjoint as point sets with equal union, supports exactly the 4
  kernel vectors of weight 4. Nothing else in this note depends on a point cardinality.
- No witness is derived from its target: each self-equivalence is built from the clean exchange's
  half-pairing and then verified by explicit image on the 14 held cuttings, on all 256 kernel
  vectors and on all 256 coset members, as frozen sets compared for equality.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a commit
  cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run
[physical_cell_cutting_clean_exchange_symmetry_cycle794_2026_08_15.py](../scripts/physical_cell_cutting_clean_exchange_symmetry_cycle794_2026_08_15.py).
The reviewed cached output belongs at
[physical_cell_cutting_clean_exchange_symmetry_cycle794_2026_08_15.txt](../logs/runner-cache/physical_cell_cutting_clean_exchange_symmetry_cycle794_2026_08_15.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes in
well under a minute on the reference machine, and stays far below one gigabyte. Its final line is
`TOTAL: PASS=10 FAIL=0`.
