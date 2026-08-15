# Physical cell cutting: the facet alphabet, heavy parity, and the forty period-one cuttings

Date: 2026-08-14
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
- `next_trace_action: test whether the boundary alphabet and the parity charge it carries have a canonical downstream consumer; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact finite alphabet, census, GF(2) rank and orbit results for the declared unit four-cube object; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object consists of the 16 corners of the unit four-cube, the
five-corner determinant-one pieces built on them, the pieces surviving at the adjacency-cost
floor, the cuttings assembled from those pieces, the pieces that actually occur in a cutting,
and the 384 signed coordinate maps of the cell. These are finite-scope object choices, not
imported physical primitives. Every integer below is derived by the linked runner from that
object alone.

There are no load-bearing literature, empirical, fitted, external-data, or repository-derived
scientific inputs. The runner uses the standard library only, performs no file input or
output, draws no random numbers, and carries out every load-bearing check in integer or exact
rational arithmetic. It rebuilds the whole object from the corner list before any gate runs.

The exact target of this cycle is the interface, that is the boundary reading of the object:
the alphabet of facet dissections the cuttings induce, the laws that alphabet obeys, and the
parity charge it carries. The proof obligations are:

1. certify the facet-face lemma — every used piece cuts exactly two facet faces, and they lie
   on distinct axes;
2. certify the alphabet — exactly 16 facet dissections, the same 16 on every slot;
3. exhibit the intrinsic heavy and light split of the letters by diagonal profile;
4. derive the two-valued slot multiplicity law from the boundary group action;
5. derive the symmetry of the interface matrix from the coordinate reflection, and record its
   entry, trace, gluing and row-sum censuses;
6. record the self-match censuses over all four axes;
7. derive the even-heavy parity law and locate its charge in the blind space recorded in
   `PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09`;
8. gate the impossibility of a strictly per-piece certificate for that law; and
9. identify the period-one cuttings, their orbits and their letter profiles.

Each obligation is discharged below and by a named hard gate in the runner. This note makes
no claim about arbitrary cell-cutting systems, physical dynamics, or a lattice-wide
construction.

## The exact finite object

Gate K1. The cell has 2672 five-corner subsets of unit determinant, 400 of them at the
adjacency-cost floor 6, and those 400 assemble into exactly 15800 cuttings of 24 pieces each.
Exactly 192 of the 400 occur in some cutting; the remaining kept pieces occur in none. The
runner derives all six of these anchors from the corner list, using the same candidate
enumeration, floor selection and exact-cover order as the earlier cycles of this lane. The
enumeration of cuttings is the declared object of the lane and is inherited as such; this note
adds no new tiling certificate and rests none of its results on one.

## The facet-face lemma

Gate K2. A facet face of a piece is a set of four of its five corners lying in one boundary
hyperplane `x_a = c` with `c` in `{0, 1}`; those four corners project, along the axis `a`, to a
unit tetrahedron of the boundary three-cube.

Two facet faces on the same axis are impossible. They would require four corners in `x_a = 0`
and four in `x_a = 1`; the two hyperplanes are disjoint, so that is `4 + 4 = 8` distinct
corners, and a piece has only five. Hence a piece carries at most one facet face per axis, and
whenever it carries two they sit on distinct axes. That the count is exactly two for every used
piece is measured, not derived: the runner checks all 192 and finds exactly two faces on each,
on distinct axes in every case, with all 384 faces lying in the 24-tetrahedron support of the
alphabet below.

Each used piece therefore has a well-defined unordered slot-pair, the pair of `(axis, side)`
slots its two faces occupy. The 192 pieces spread over exactly 24 such pairs with exactly 8
pieces on each, and `24 x 8 = 192`.

## Facet dissections and the alphabet

Gates K3 and K4. Fix a cutting and one of the 8 boundary three-cubes. Of the 24 pieces, exactly
6 contribute a face there, and their 6 projected tetrahedra are distinct — checked on all
`15800 x 8 = 126400` facet slots with 0 misses. Each cutting thus dissects each boundary
three-cube into 6 unit tetrahedra.

Over all 15800 cuttings and all 8 slots exactly 16 distinct dissections occur, and the set of
dissections occurring is the same 16 on every one of the 8 slots. These 16 are the letters of
the facet alphabet. Their combined tetrahedron support has exactly 24 members, and the runner
fixes a canonical order on those 24 and a canonical numbering of the 16 letters; every index
quoted below refers to those two orders.

## Tetrahedron structure and the intrinsic heavy and light split

Gate K5. Each of the 24 tetrahedra contains exactly one antipodal corner pair of the
three-cube, that is exactly one main diagonal, and each of the 4 main diagonals lies in exactly
6 of them. A letter therefore carries a diagonal profile: the multiset of the diagonals of its
6 tetrahedra.

Exactly 4 letters are single-diagonal — all six of their tetrahedra share one diagonal — and
the assignment of diagonal to letter is a bijection onto the 4 diagonals, with canonical map
`{1: 2, 6: 3, 8: 1, 15: 0}`. The other 12 letters split `(3, 3)` over an unordered pair of
diagonals, exactly 2 letters for each of the 6 pairs. This split is intrinsic to the alphabet:
it is read off the letters themselves and uses no information about how often they occur.

## The multiplicity law

Gates K6 and K7. On a fixed slot each letter occurs in a definite number of cuttings. The
census is identical on every one of the 8 slots: 12 letters of multiplicity 862 and 4 of
multiplicity 1364, with `12*862 + 4*1364 = 15800`. The heavy letters, defined as those of
multiplicity 1364, are exactly the 4 single-diagonal letters.

Two-valuedness is derived, not merely observed. The maps of the order-384 cell group that
carry a fixed facet to itself form a subgroup of order 48, and the runner certifies that the
maps they induce on the boundary three-cube are exactly the 48 signed coordinate maps of that
cube, with no strays. Such a map sends cuttings to cuttings and sends the letter at that slot
to its own image, so slot multiplicity is constant along the orbits of the 48 induced maps on
the 16 letters. The runner certifies that the 16 letters are closed under those maps, with 0
failures, and that they fall into exactly 2 orbits, of sizes 12 and 4. At most 2 multiplicity
values can therefore occur on a slot, and the census shows exactly 2. The 4-element orbit is
the single-diagonal one, because the induced maps permute the 4 diagonals and so preserve the
property of being single-diagonal; the heavy letters are that orbit.

## The interface matrix and its symmetry

Gate K8. For each axis `a`, let `N_a` be the `16 x 16` integer matrix whose `(k, l)` entry
counts the cuttings whose letter on side 0 of axis `a` is `k` and whose letter on side 1 is
`l`.

`N_a` is symmetric on every axis, and this is derived. The reflection `r_a` of the coordinate
`a` lies in the order-384 group; it carries cuttings to cuttings, exchanges the two facets of
axis `a`, and leaves the remaining three coordinates alone, so it leaves the projected
dissections unchanged and merely swaps the two letters of axis `a`. The map `s -> r_a(s)` is
therefore a bijection of the `(k, l)` cell onto the `(l, k)` cell. The runner certifies the
key-swap property directly, on all 4 axes and all 15800 cuttings, with 0 misses, and then
confirms the symmetry entrywise.

The entry-value census of `N_a` is the same for all four axes:
`{18: 24, 36: 48, 50: 48, 52: 48, 90: 12, 92: 48, 100: 12, 104: 12, 200: 4}`. On the diagonal a
light letter carries 100 and a heavy letter 200, so the trace is `12*100 + 4*200 = 2000` on
every axis. Every heavy row decomposes as `200 + 3*104 + 6*92 + 6*50 = 1364`, recovering that
letter's multiplicity as its row sum.

Gluing along axis `a` pairs cuttings whose facing letters agree. The number of such pairs is
`12*862*862 + 4*1364*1364 = 16358512` on every axis. Since the number of partners of a cutting
is the multiplicity of its own facing letter, the row-sum census over the 15800 cuttings is
`{862: 10344, 1364: 5456}`, with `12*862 = 10344` and `4*1364 = 5456`.

## Self-match laws

Gate K9. A cutting self-matches on axis `a` when its two letters on that axis agree, that is
when it contributes to the trace of `N_a`; there are 2000 such cuttings on each axis. Call the
number of axes on which a cutting self-matches its weight. The weight census over all 15800
cuttings is `{0: 9504, 1: 4672, 2: 1584, 4: 40}` — weight 3 never occurs. The absence of weight
3 is a complete measurement over the whole census; no structural derivation of it is claimed
here.

The refined counts are: singleton weight 1168 for each of the 4 axes, pair weight 264 for each
of the 6 axis pairs, and `1168 + 3*264 + 40 = 2000` recovers the per-axis trace. Splitting by
whether the matching letter is heavy (H) or light (L), weight 2 gives `HH 384`, `HL 768`,
`LL 432`, and weight 1 gives `H 1600`, `L 3072`.

## The even-heavy parity law

Gate K10. The number of heavy letters a cutting shows across its 8 slots has census
`{0: 1200, 2: 7872, 4: 6240, 6: 480, 8: 8}`: no cutting shows an odd heavy count. The
derivation runs in three steps and is global, not slot by slot.

First, the letter system. Introduce one unknown `psi(t)` over GF(2) for each of the 24
tetrahedra and one equation per letter — the sum of `psi` over that letter's 6 tetrahedra
equals 1 if the letter is heavy and 0 otherwise. Row reduction gives rank 10, consistency, and
a solution space of dimension 14. The runner exhibits the explicit solution read off the
reduced form, with pivot columns `[0, 1, 2, 3, 4, 6, 8, 12, 14, 18]` and support
`[0, 2, 3, 4, 8, 12, 14, 18]` in the canonical tetrahedron order, and verifies all 16 letter
equations on it.

Second, the face-multiset identity. For every cutting, the multiset of the 48 facet faces of
its 24 pieces equals the multiset union of the 6 tetrahedra of each of its 8 letters — checked
on all 15800 cuttings with 0 violations. Modulo 2 the heavy count of a cutting is therefore the
sum of `psi` over its 8 letters, hence the sum of `psi` over those 48 faces, hence the sum over
its 24 pieces of `psi(f1) + psi(f2)`. A piece contributes 1 exactly when its two faces disagree
on `psi`. Writing `O` for the fixed set of such pieces, `|O| = 88`, the heavy count of a cutting
is congruent modulo 2 to the size of its intersection with `O`.

Third, the blind space. The cutting-indicator matrix over the 192 used pieces, one row per
cutting, has GF(2) rank 88, so its orthocomplement has dimension 104. The runner collects an
88-row basis during the reduction and checks that `O` meets each basis row evenly; every
cutting row is a GF(2) sum of basis rows, so `O` meets every cutting evenly. The gate also
confirms this directly on all 15800 cuttings, 0 odd. The parity law follows for the entire
census at once.

The mod-2 rank 88 and orthocomplement dimension 104 agree with the exact rational rank and
kernel dimension of the same incidence recorded in
`PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09`; the runner re-derives
the mod-2 statement itself and imports nothing from that note. `O` is a weight-88 vector of
that orthocomplement, the blind space of the earlier cycles, so the parity law reads as a
boundary charge carried by the blind space.

## No strictly per-piece certificate

Gate K10, sharp negative. Adjoining to the letter system the per-piece equality rows
`psi(f1) = psi(f2)`, one for each of the 192 used pieces, makes the system inconsistent: the
rank rises to 23 of a possible 24 and no solution exists. Exactly 2 of those 192 rows are
trivial, because for 2 pieces the two facet faces project to the same tetrahedron of the
boundary three-cube; the other 190 are not, and the inconsistency comes from them. So there is
no assignment
that both reads the heavy bit correctly on letters and makes every piece individually
conservative — the parity law is genuinely global at piece level, and the mismatch set `O` is
not removable by a better choice of `psi`.

In the other direction, appending all 15800 cutting functionals to the letter system leaves
the rank at 10 and leaves it consistent. The cutting rows lie in the span of the letter rows,
which, through the face-multiset identity, is another reading of the parity law itself.

## The forty period-one cuttings

Gates K11 and K12. Exactly 40 cuttings have weight 4, that is self-match on all four axes. For
such a cutting the induced dissections on the two facets of every axis agree, so the dissection
of the cell boundary is invariant under the unit translation of each axis; consequently all
integer translates of the cutting meet face to face and each of the 40 tiles four-space
periodically with 1 cell per period. The runner exhibits 1 witness per orbit and re-checks
letter equality on both sides of all 4 axes for it.

Under the order-384 cell group the 40 fall into exactly 2 orbits, of sizes 8 and 32, with
stabiliser orders 48 and 12; the orbit-stabiliser arithmetic `8*48 = 384` and `32*12 = 384`
checks out on both. The axis-letter profiles are constant on each orbit: the size-8 orbit is
all-heavy, profile `(H, H, H, H)`, and coincides exactly with the 8 cuttings of heavy count 8
in the parity census above; the size-32 orbit has profile `(H, L, L, L)`. The most symmetric
period-one cuttings are thus precisely the extreme cell of the parity census, which is a
positive identification of two independently defined sets of size 8, not a coincidence of
counts.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: that every used piece cuts exactly two
facet faces; the multiplicity values 862 and 1364 themselves; every census value quoted above,
including the entry, trace, gluing, row-sum, self-match, weight and heavy-count censuses; and
the absence of weight 3.

Derived at the declared finite scope: the distinct-axes half of the facet-face lemma; the
symmetry of every interface matrix; the two-valuedness of slot multiplicity, from the induced
order-48 boundary group and its 2 letter orbits; the even-heavy parity law, together with the
placement of its charge in the blind space; the impossibility of a strictly per-piece
certificate for that law; and the period-one tiling property of the 40.

All of the above are computational identities of the declared unit four-cube object and its
15800 cuttings. No physical, dynamical, or lattice-wide identification is claimed, no continuum
limit is taken, and nothing here is asserted about cell-cutting systems outside the declared
object.

## Reproduction

Run
[physical_cell_cutting_facet_alphabet_heavy_parity_cycle786_2026_08_14.py](../scripts/physical_cell_cutting_facet_alphabet_heavy_parity_cycle786_2026_08_14.py).
The reviewed cached output belongs at
[physical_cell_cutting_facet_alphabet_heavy_parity_cycle786_2026_08_14.txt](../logs/runner-cache/physical_cell_cutting_facet_alphabet_heavy_parity_cycle786_2026_08_14.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget,
typically finishes in about a minute, and stays well under one gigabyte. Its final line is
`TOTAL: PASS=25 FAIL=0`, and it exits nonzero if any gate fails.

## Review record and boundary

- The runner prints only censuses, ranks, orbit data and derived identities; the full
  interface matrix is deliberately not printed, so the note quotes its entry census, trace and
  heavy-row decomposition instead.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries, the appropriate review classification is **bounded support** for the
declared exact finite object.
