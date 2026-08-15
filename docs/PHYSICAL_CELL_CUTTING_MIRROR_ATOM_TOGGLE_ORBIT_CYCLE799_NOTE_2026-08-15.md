# Physical cell cutting: the mirror atoms of a cutting and the free toggle group behind its class set

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
- `next_trace_action: derive why the atom-size profiles of the declared cell are exactly the six lists (24), (4, 20), (12, 12), (4, 4, 16), (4, 4, 4, 12) and (4, 4, 4, 4, 4, 4) with fiber counts 2636, 552, 384, 336, 192 and 16, rather than merely enumerating them; derive why every atom has size divisible by 4; and derive the single per-cutting ascent census across the 4116 fiber heads, of which only the constancy inside a fiber is derived here; none of that is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, on the declared finite cell, that every one of the 192 used pieces is a five-corner chain whose four steps carry the four axes once each and whose four-letter word is fixed by its start corner and its axis order alone, 192 of 192; that the piece map of the pure fourth-axis flip agrees with the point flip of the sample grid at 192 of 192 used pieces, is an involution with 0 fixed pieces, and sends each chain word to its reversed complement, so that the 96 word classes are blind to it; that the 15800 cuttings fall into 4116 class-set fibers in which every member is the fiber head with a subset of its pieces replaced by their mirrors, 15800 of 15800; that inside every fiber the difference supports are closed under symmetric difference, 4116 of 4116, that every support is a union of least moving parts (atoms) and that the fiber size is two to the atom count, 4116 of 4116, which derives the multiplicity ladder 2, 4, 8, 16 and 64 with counts 2636, 936, 336, 192 and 16 rather than observing it; that the atoms admit a second and independent description as the flip-overlap components of the point masks of one cutting, agreeing with the first at 4116 of 4116 fibers and, over the first 500 fibers and all 2368 of their members, transporting correctly along the toggle, so the atom split is a property of each cutting alone; that the atom-size profiles are exactly six, every atom size divisible by 4, every profile summing to 24, with the induced recount of 15800 cuttings; and that toggling every atom of a fiber head returns its mirror, which is again a cutting at 15800 of 15800 with none fixed; the axis-order census over the 48 walk representations and the single per-cutting ascent census 1, 11, 11 and 1 across the fiber heads are anchored as measured, and no physical or lattice-wide identification is made`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the unit
four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive at the
adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into, the 192
pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell. Points are
counted on the generic sample grid with per-axis offsets 1, 2, 4 and 8, that is 5 values on each of
the four axes and 625 points in all, written here on the integer scale in which the cell has width
80. Every count below is recomputed from that rebuild; nothing outside it enters.

The note `PHYSICAL_CELL_CUTTING_PIECE_TAXONOMY_COUNT_LAW_CYCLE798_NOTE_2026-08-15.md` left
one question sharp. Each of the 192 used pieces is a chain carrying a four-letter word; the class of
a word is the smaller of the word and its reversed complement; the 192 words are pairwise distinct
and pair into 96 classes of two; every cutting carries 24 distinct classes; and yet the 15800
cuttings carry only 4116 distinct class sets, with multiplicities 2, 4, 8, 16 and 64. This note
derives that ladder. The fibers of the class-set map are the orbits of a free action by toggles, and
the toggleable units are pinned down twice over, once inside the fiber and once in the point
geometry of a single cutting, with the two descriptions agreeing everywhere.

## Chain coordinates and the word law

Each used piece has five corners, four corner-adjacency edges, and degree list 1, 1, 2, 2, 2, so it
is a path; walking it from its smaller-labelled end of degree one gives a canonical corner sequence
whose four steps carry the four axes once each, 192 of 192. The word law is then exact: the letter
of the step on axis `ax` is the offset of that axis when the corner bit rises along the step, and 16
minus that offset when it falls, so the word is a function of the start corner and the axis order
alone and needs no walk, at 192 of 192 chains. Because the letters of distinct axes never coincide,
the four letters of a word are pairwise distinct and its three adjacent comparisons are all strict.

## The mirror lemma

The mirror is the pure fourth-axis flip. Two statements hold at 192 of 192 used pieces: the piece it
sends `t` to is the piece whose point mask is the flip of the mask of `t`, and its word is the
reversed complement of the word of `t`. The first makes the piece-level map and the point-level map
one and the same object; the second makes the mirror blind on classes, since the class was defined
as the smaller of a word and its reversed complement. The map is an involution with 0 fixed pieces,
so the 192 chains fall into 96 mirror pairs, one per class.

That gives the toggle criterion in both directions. Let a cutting cover each of the 625 sample
points exactly once, let `S` be a subset of its pieces and let `U` be the union of their point sets.
Replacing every piece of `S` by its mirror vacates `U` and lays down exactly the flip of `U`, since
the mirror of a family of pieces with disjoint point sets is again a family with disjoint point
sets, of the same total size. If `U` is carried to itself by the flip, the vacated region is
re-covered exactly once and the result is again a cutting. Conversely, if the result is a cutting,
the untouched pieces still cover the complement of `U` exactly once each, so the mirrored pieces
must cover exactly `U`; but they cover exactly the flip of `U`, forcing the flip of `U` to be `U`.
Since the mirror keeps every class, such a toggle never moves the class set of a cutting.

## The toggle group of a fiber

Grouping the 15800 cuttings by their set of 24 classes gives 4116 fibers. Taking the first member of
a fiber as its head `A`, every member `B` of that fiber is exactly `A` with the pieces of the
difference support `S` replaced by their mirrors, at 15800 of 15800 members: the converse direction
of the criterion above is therefore not merely available in principle but realized by every member,
and the difference supports of a fiber are pairwise distinct, so a fiber member and its support are
the same information. Inside every fiber the supports are closed under symmetric difference, 4116 of
4116, so they form a group of toggles acting on the head, and the fiber is one orbit of it. The
action is free because a support determines its member.

## The atoms and the derived ladder

Partitioning the 24 pieces of the head by their membership profile across all the supports of the
fiber gives the atoms of that fiber. Every support is then a union of atoms, and the fiber size is
two to the number of atoms, at 4116 of 4116 fibers: the supports are exactly the unions of atoms and
nothing else, so the toggle group is free on the atoms. The atom-count census is 1 at 2636 fibers, 2
at 936, 3 at 336, 4 at 192 and 6 at 16, and raising two to those counts returns 2, 4, 8, 16 and 64
with exactly the multiplicities of the recomputed ladder. The ladder is therefore derived, not observed: the powers of
two are the subsets of a basis of independent toggles, and the value 64 is six atoms rather than a
coincidence.

## The two routes to the atoms

The atoms have a second description that reads no fiber at all. Take one cutting, join two of its
pieces whenever the point mask of one meets the flip of the point mask of the other, and take the
components. This is a statement about the 625 points and the flip alone; it never looks at any other
cutting, any class, or any support. The components of the head agree with the atoms of its fiber at
4116 of 4116 fibers. The two routes share no input: one reads only point masks of a single cutting,
the other only membership profiles across the members of a fiber, and a single mismatch anywhere
would fail the check.

The description also survives transport. Over the first 500 fibers and all 2368 of their members,
carrying each atom of the head along the toggle, that is replacing its pieces that lie in the
support by their mirrors, gives exactly the flip-overlap components of the member, 2368 of 2368. So
the atom split is a property of each cutting on its own, not a privilege of the head, and the fiber
inherits it rather than defining it.

## The atom-size profiles

The sizes of the atoms of a fiber, listed in increasing order, take exactly six values over all 4116
fibers: (24) at 2636 fibers, (4, 20) at 552, (12, 12) at 384, (4, 4, 16) at 336, (4, 4, 4, 12) at
192 and (4, 4, 4, 4, 4, 4) at 16. Every atom size is divisible by 4 and every profile sums to 24, as
it must, since the atoms partition the pieces of the cutting. Weighting each profile by two to its
length recovers 15800 cuttings, which reconciles the count with the rebuild. Toggling every atom at
once sends a head to its full mirror image, again a cutting of the same fiber, at 4116 of 4116; over
all 15800 cuttings the mirror image is again a cutting, with 0 fixed, so the mirror acts freely.

## The ascent census inside a fiber

The ascent count of a word is the number of its adjacent comparisons that increase, a value between
0 and 3. Reversing a word exchanges its ascents with its descents, and complementing every letter in
16 does the same, so the reversed complement, which is the mirror word, preserves the ascent count.
With the mirror lemma this makes the per-cutting ascent census invariant under every toggle, hence
constant on each of the 4116 fibers. The measured census is the single shape 1, 11, 11 and 1 at all
15800 cuttings, and only its constancy inside a fiber is derived here.

Two censuses are printed as measurements and gated as nothing. The axis-order census over the 48
walk representations of a cutting, each chain read in both directions, takes exactly five shapes,
with 9368 cuttings at the shape whose 24 axis orders each occur twice, 5664 at the shape of 12
orders once and 12 orders three times, 552 at 8 orders twice and 8 orders four times, 120 at 12
orders four times, and 96 at 16 orders twice and 4 orders four times.

## Derived versus measured

Derived at the declared finite scope. The chain structure, the axis-once property and the word law
are checked at every one of the 192 used pieces, not sampled. The mirror lemma is checked as an
identity of point masks at all 192, and the reversed-complement form of the mirror word at all 192,
so the class blindness of the mirror is a consequence rather than an observation. The toggle form of
every fiber member is checked at all 15800 members, the closure of the supports under symmetric
difference at all 4116 fibers, and the atom law and the size law at all 4116, so the multiplicity
ladder 2, 4, 8, 16 and 64 is derived from the atom counts. The agreement of the geometric and the
fiber routes is derived by complete enumeration over all 4116 fibers, and its transport over all
2368 members of the first 500 fibers. The divisibility of every atom size by 4 and the sum 24 are
verified atom by atom. That the reversed complement preserves the ascent count, and hence that the
ascent census is constant on a fiber, is derived in prose above and rests only on the mirror lemma.

What is measured, not derived, at the declared finite scope: why the atom-size profiles are exactly
those six and carry exactly those fiber counts; why every atom size is divisible by 4; the atom-count
census 2636, 936, 336, 192 and 16 itself; the axis-order census with its five shapes and counts
9368, 5664, 552, 120 and 96; and the fact that the per-cutting ascent census is the same shape 1,
11, 11 and 1 at all 4116 fiber heads, of which the derivation above covers only the passage from a
head to the rest of its fiber. The choice of the first member of a fiber as its head is a
bookkeeping convention; the transport check is what makes the atom split independent of it.

## Boundary and the honest auditor read

All of the above are computational identities of the declared unit four-cube object, its 400 kept
pieces, its 15800 cuttings, its 192 used pieces and the order-384 symmetry group of the cell. The
point statements are made on the sample grid of 625 points on the integer scale of width 80 with the
per-axis offsets 1, 2, 4 and 8, and the flip is the one of the fourth axis in that frame; nothing
here claims the atom split survives a different offset choice or a different distinguished axis. The
atom decomposition is established for the cutting family of this cell and is not claimed for any
other cutting family. The word, class and ascent statements are stated in the labels of the declared
letter frame and are not claimed to be frame-independent. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

## Next entrance

Three questions are now sharp. The first is the profile law: the atoms partition 24 pieces into
parts of sizes divisible by 4, and the six lists that occur are a small subset of the possibilities,
so some structure is choosing them and it is not identified here. The second is the atom itself: the
flip-overlap description says an atom is a chunk of the cutting that the flip cannot break, and its
sizes 4, 12, 16, 20 and 24 invite a description of that chunk in the point frame directly. The third
is the ascent census: its constancy inside a fiber is now derived, so what remains is constancy
across the 4116 heads, a statement about which words can share a cutting rather than about the
mirror at all.

## Review record

- The rebuild is recomputed from the 16 corners in the runner itself, with the candidate count, the
  floor, the kept count, the cutting count, the used count and the group order all gated, so a drift
  in the object fails before any new claim is reached.
- The word law is checked in the honest direction: the word is walked first from the corner sequence,
  the law then predicts it from the start corner and the axis order alone, and the gate requires
  agreement at every used piece rather than a count match.
- The mirror lemma is a two-route identity: the piece map is formed from the corner action of the
  flip, the point flip is formed as a permutation of the 625 grid points, and the gate requires the
  masks to agree exactly.
- The two atom descriptions are computed by disjoint code paths. The geometric path reads only the
  point masks of one cutting and the point flip; the fiber path reads only membership profiles across
  the difference supports. Neither is derived from the other, and the gate requires equality of the
  sorted decompositions, so a single fiber out of place fails it.
- The multiplicity ladder is never pinned as an input: it is recomputed from the fibers and then
  reproduced a second time by raising two to the measured atom counts, and the two must match.
- The transport check over every member of the first 500 fibers is what rules out the reading that
  the atom split is an artifact of the choice of head.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a commit
  cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run the [runner](../scripts/physical_cell_cutting_mirror_atom_toggle_orbit_cycle799_2026_08_15.py).
The reviewed
[cache](../logs/runner-cache/physical_cell_cutting_mirror_atom_toggle_orbit_cycle799_2026_08_15.txt)
belongs beside it and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC`
budget, finishes in well under a minute on the reference machine, and stays far below one gigabyte.
Its final line is `TOTAL: PASS=10 FAIL=0`.
