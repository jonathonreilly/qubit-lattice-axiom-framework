# Physical cell cutting: mirror atoms and the Boolean toggle group of a finite class-set fiber

Date: 2026-08-15
Authority: none
Audit: unset
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.
Primary runner: [physical_cell_cutting_mirror_atom_toggle_orbit_cycle799_2026_08_15.py](../scripts/physical_cell_cutting_mirror_atom_toggle_orbit_cycle799_2026_08_15.py)

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
- `claim_type_reason: an exhaustive exact computation on the declared finite four-cube sample-grid object of the chain-word mirror involution, all 4116 class-set fibers and all 15800 member transports, their Boolean atom decompositions and six measured atom-size profiles, the free mirror action, and the stated measured axis-order and ascent censuses; no physical, continuum, multicell, offset-independent, or frame-independent claim is made`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Imports, provenance, and scope

The primary runner is self-contained and imports no ancestral scientific result or repository data
file. It rebuilds every count below from finite definitions supplied here. Those underivable choices
are explicit:

- **Cell and candidate rule.** The 16 binary corners of the unit four-cube, five-corner subsets of
  absolute determinant one, and the adjacency cost that counts non-edge corner pairs define the
  candidate object. Their role is definitional; their provenance is this supplied finite model. The
  minimum cost 6, the 2672 candidates, the 400 minimizers, the 15800 exact 24-piece covers, the 192
  used pieces, and the 384 signed coordinate maps are recomputed results, not imported values. No
  open bridge is needed inside this bounded target; correspondence to another cell model is outside
  it.
- **Point sample.** The per-axis offsets 1, 2, 4 and 8, five values per axis, and integer width 80
  define the declared 625-point sample. Their role is to make the point masks and overlap graph
  finite; their provenance is a supplied sampling convention. No claim of genericity or invariance
  under other offsets is made, and extension to another sample is open outside this target.
- **Distinguished mirror.** The pure fourth-axis flip is the supplied involution used in every
  mirror and overlap statement. Its role and coordinate-frame provenance are explicit. Other axes or
  frames are not imported as equivalent and remain outside the target.
- **Bookkeeping conventions.** The smaller-labelled degree-one endpoint orients a chain, the smaller
  of a word and its reversed complement names its class, and the first enumerated member names a
  fiber head. These choices fix representatives only. Their provenance is this note, and the
  all-member transport and full-mirror checks ensure the atom result is not restricted to the chosen
  head.

No measured, fitted, literature, observational, normalization, boundary-condition, framework-
primitive, or external physics input enters. In this declared object each of the 192 used pieces is
a chain carrying a four-letter word; the 192 words pair into 96 mirror classes, every cutting carries
24 distinct classes, and the 15800 cuttings form 4116 distinct class-set fibers. This note derives
the Boolean toggle structure behind their measured multiplicities 2, 4, 8, 16 and 64.

## Exact target and proof-obligation graph

**Exact target.** For the declared finite object, prove that every one of the 4116 class-set fibers is
the free orbit of an elementary abelian two-group whose GF(2) basis is its atom partition; prove that
the membership-profile atoms of a head equal its flip-overlap components and transport to all 15800
members; and prove that the full toggle is the fixed fourth-axis mirror, while reporting the exact
bounded atom-profile, axis-order, and ascent censuses without promoting those measurements to
general structural laws.

| obligation | status in this note | evidence and preserved hypotheses |
| --- | --- | --- |
| Rebuild the finite domain | proved here | The primary runner starts from the 16 supplied corners and fixed sample and gates every object count before using it. |
| Establish the chain coordinates and word law | proved here | All 192 used pieces are tested; the smaller-endpoint orientation and fixed offsets remain explicit. |
| Identify the piece mirror with the point flip and reversed-complement word | proved here | All 192 used pieces are checked under the supplied fourth-axis involution, including involution, fixed-point, word, and class conditions. |
| Identify every class-set fiber member with one support toggle | proved here | All 15800 members are compared with the selected head, with distinct supports and all 24 classes preserved. |
| Make the supports a Boolean group | proved here | Symmetric-difference closure is checked in all 4116 fibers; the support-to-member map is injective, so the action is free. |
| Make the membership blocks a GF(2) basis | proved here | Every support is a union of membership-profile blocks and the support count equals the number of all block subsets in all 4116 fibers, so every subset occurs. |
| Match the independent atom constructions and remove head dependence | proved here | Point-flip overlap and fiber membership share the declared object and head but not a derived partition; equality is checked at every head and transported to all 15800 members. |
| Establish the full mirror action | proved here | Toggling every atom is checked to be the fixed mirror in every fiber, and all 15800 mirrored cuttings are present with no fixed cutting. |
| State the profile, axis-order, and ascent values | measured here | Complete finite censuses are decisively gated, but no non-enumerative law selecting their values is claimed. |

The target has no cited-authority leaf and no open proof leaf. Its degenerate cases are exercised:
one-atom fibers are present, six-atom fibers are present, and fixed pieces or fixed cuttings under the
mirror are counted as zero rather than assumed away. The strongest missing lemma beyond the target
is a non-enumerative derivation selecting the six atom-size profiles (including divisibility by 4)
and the common ascent census across fiber heads. Relative to the target, that is a strictly stronger
explanatory obligation, not a target-equivalent terminal premise; no completed step relies on it, and
it remains explicitly open.

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

## The Boolean toggle group of a fiber

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
two to the number of atoms, at 4116 of 4116 fibers: the supports are exactly the subsets of atoms and
nothing else, so the toggle group is an elementary abelian two-group with the atoms as a GF(2) basis.
Its action on the fiber is free. The atom-count census is 1 at 2636 fibers, 2
at 936, 3 at 336, 4 at 192 and 6 at 16, and raising two to those counts returns 2, 4, 8, 16 and 64
with exactly the multiplicities of the recomputed ladder. The ladder is therefore derived, not observed: the powers of
two are the subsets of a basis of independent toggles, and the value 64 is six atoms rather than a
coincidence.

## The two routes to the atoms

The atoms have a second description that reads no fiber data. Take one cutting, join two of its
pieces whenever the point mask of one meets the flip of the point mask of the other, and take the
components. This is a statement about the 625 points and the flip alone; it never looks at any other
cutting, any class, or any support. The components of the head agree with the atoms of its fiber at
4116 of 4116 fibers. Beyond the shared declared finite object and selected head, the constructions
use independent derived data: one reads point masks and the fixed flip, while the other reads
membership profiles across the members of a fiber; neither consumes the other's atom partition, and
a single mismatch anywhere fails the check.

The description also survives transport. Over all 4116 fibers and all 15800 of their members,
carrying each atom of the head along the toggle, that is replacing its pieces that lie in the
support by their mirrors, gives exactly the flip-overlap components of the member, 15800 of 15800.
Thus each cutting recovers the transported atom split from its own point masks and the fixed flip;
the result is not restricted to the chosen head.

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

Two censuses are complete measurements and are decisively gated. The axis-order census over the 48
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
15800 members. The divisibility of every atom size by 4 and the sum 24 are
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
- The two atom descriptions are computed by independent derived-data paths beyond the shared finite
  object and selected head. The geometric path reads point masks and the point flip; the fiber path
  reads membership profiles across the difference supports. Neither consumes the other's derived
  partition, and the gate requires equality of the sorted decompositions, so one mismatch fails it.
- The multiplicity ladder is never pinned as an input: it is recomputed from the fibers and then
  reproduced a second time by raising two to the measured atom counts, and the two must match.
- The transport check over every member of all 4116 fibers is what rules out restricting the atom
  split to the chosen head.
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
Its final line is `TOTAL: PASS=12 FAIL=0`.
