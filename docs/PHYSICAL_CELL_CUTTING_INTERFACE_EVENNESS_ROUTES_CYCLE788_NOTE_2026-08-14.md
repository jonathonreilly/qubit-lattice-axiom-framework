# Physical cell cutting: interface evenness routes, the incidence transport obstruction, boundary frames, and the exchange distance law

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
- `next_trace_action: test whether the six-dimensional letter-functional quotient invisible to the tetra incidence carries the evenness mechanism; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: refutation certificates for candidate evenness mechanisms, an exact incidence transport identity with a rank obstruction, boundary-frame determinacy, and the within-fiber exchange distance law for the declared unit four-cube object; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the
unit four-cube, the 2672 five-corner determinant-one pieces built on them, the 400 pieces
surviving at the adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400
assemble into, the 192 pieces that actually occur in a cutting, the 384 signed coordinate maps
of the cell, and the slot-preserving subgroup of order ninety-six that fixes the two boundary
three-cubes of axis zero as a pair. Each cutting dissects each boundary three-cube into 6 unit
tetrahedra drawn from a support of 24, and exactly 16 such dissections occur, the same 16 on
every one of the 8 slots: 12 light letters of slot multiplicity 862 and 4 heavy letters of
multiplicity 1364. These are finite-scope object choices, not imported physical primitives.
Every integer below is derived by the linked runner from that object alone; it rebuilds the
whole object from the corner list before any gate runs, uses the standard library only,
performs no file input or output, draws no random numbers, and carries out every load-bearing
check in integer or exact rational arithmetic.

The interface reading is the 16 x 16 matrix T whose entry at a letter pair counts the cuttings
carrying those two letters on the two sides of axis zero. The runner recomputes T: it is the
same matrix on all four axes, it is symmetric, its trace is 2000, its least entry is 18, its
entry census is `{18: 24, 36: 48, 50: 48, 52: 48, 90: 12, 92: 48, 100: 12, 104: 12, 200: 4}`,
and all 256 entries are even. The sibling cycles
`PHYSICAL_CELL_CUTTING_FACET_ALPHABET_HEAVY_PARITY_CYCLE786_NOTE_2026-08-14` and
`PHYSICAL_CELL_CUTTING_INTERFACE_TRANSFER_SPECTRUM_CYCLE787_NOTE_2026-08-14` established that
reading and reduced the evenness question to a free-pairing mechanism that reaches the 208
fibers whose entry is not 36 and leaves the 48 fibers of entry 36 uncovered. Those 48 fibers
are the named wall this cycle attacks. Nothing is imported from the siblings: every fact
quoted above is recomputed here.

The cycle lands refutation certificates for five candidate mechanisms, one exact transport
identity with its rank obstruction, one determinacy theorem, and one distance law. The wall
stands; what changes is that the region where the mechanism can live is now much narrower and
has two named entrances.

## Letter membership is not affine over the piece vector

Work over GF(2) with functions on the 15800 cuttings as bit vectors, one bit per cutting. The
indicator of a used piece is the set of cuttings containing it. The 192 used-piece indicators
together with the all-ones function span a space of GF(2) rank 88.

For each of the 24 tetrahedra and each side of axis zero, the producers of that tetra are the
used pieces placing it there; their supports are pairwise disjoint, certified by the equality
of the support size of the exclusive-or with the sum of the individual support sizes. The
tetra functional is that exclusive-or. The 24 tetra functionals together with the all-ones
function span rank 10, the same on both sides.

None of the 16 letter indicator functions lies in the tetra span, and none lies in the full
used-piece span: 0 of 16 in all four combinations, side zero and side one, tetra span and
column span. Letter membership is therefore not a GF(2)-affine function of the piece vector of
a cutting, and the first candidate mechanism — an affine letter functional whose fibers would
split evenly by a linear complement — is refuted.

## The two-case stabilizer theorem

Take a letter pair of entry 36 and its stabilizer inside the slot-preserving subgroup of order
ninety-six: the non-swapping maps that fix both letters, together with the swapping maps that
exchange them. For all 48 such pairs the stabilizer has order exactly 2, census `{2: 48}`.

A group action certifies evenness of a set only when every orbit is even. There are exactly
two subgroups to consider. The trivial subgroup has all orbits of size one, which is odd. The
full stabilizer of order 2 is generated by a single map, and the runner certifies that in all
48 of 48 fibers that map carries the fiber to itself and has at least one odd cycle on it, so
it too has an odd orbit. Hence no subgroup of the pair stabilizer acts on any of the 48 fibers
with all orbits even, and the group-pairing mechanism cannot certify the evenness of a single
stubborn fiber at any subgroup level. This sharpens the sibling result, which ruled out only
the single distinguished element, into a statement over the whole subgroup lattice.

## Incidence transport and its rank obstruction

Let A be the letter-tetra incidence: 16 rows, 24 columns, entry one exactly when the tetra
belongs to the letter. Every row sum is 6 and every column sum is 4, and 16 x 6 = 96 = 24 x 4.
Let N be the 24 x 24 tetra-pair matrix whose entry counts the cuttings whose side-zero
dissection contains the first tetra and whose side-one dissection contains the second; the
disjointness of producer supports makes that count the support size of an intersection of two
tetra functionals.

Exact identity, verified entry by entry on all 576 entries with 0 misses:

`N = A-transpose T A`.

The value census of N is
`{862: 168, 872: 48, 894: 48, 904: 168, 1270: 24, 1280: 48, 1322: 48, 1332: 24}`, and all 576
entries are even. That evenness is a corollary of the evenness of T and nothing more: each
entry of N is a sum of entries of T, all of them even. It is recorded here as a consistency
check on the identity, not as independent evidence for the wall, and the note claims no more
for it than that.

The obstruction is on the other side of the identity. Over GF(2) the incidence A has rank 10
and kernel dimension 6. Parity transport through the tetra level therefore sees only a rank-10
image of the 16-dimensional letter space, and a 6-dimensional quotient of letter functionals is
invisible to the tetra alphabet. If the mechanism behind the wall is letter-linear at all, it
lives in that quotient — which is why the quotient is named as the first next surface rather
than a leftover.

One coincidence deserves a single remark and no weight: 862 is both the light-letter slot
multiplicity and, tied with 904, the most frequent value of N, each occurring at 168 pairs. No
structural link between the two readings is claimed here.

## Boundary frames, determinacy, and the odd classes

The axis-zero frame of a cutting is the pair of piece sets that contribute a facet tetra on the
two sides. Both sets have size 6 for every cutting, census `{(6, 6): 15800}`, and they are
always disjoint: a piece has 5 corners, so it cannot place 4 corners on each of two parallel
bounding hyperplanes, which would need 8 distinct corners. The runner certifies the disjointness
directly as well.

Determinacy. The frame on a side determines the letter on that side single-valuedly. There are
1024 distinct side-zero frames and 1024 distinct side-one frames, and no frame on either side
carries two different letters — 0 exceptions on each side. There are 6184 distinct joint frames,
and no joint frame carries two different letter pairs — 0 exceptions. The frame is thus a strict
refinement of the letter, and a candidate carrier of finer structure.

Refutation. The frame partition does not refine evenness. Of the 6184 joint frame classes, 3368
have odd size; of the 1024 side-zero classes, 856 have odd size. Pairing cuttings inside a frame
class is therefore impossible in general. And the refutation reaches inside the wall: restricted
to each of the 48 stubborn fibers, the within-fiber joint-frame partition has at least one odd
class, in all 48 of them, and the same holds for the full eight-slot letter profile — the tuple
of all 8 facet letters of a cutting — again in all 48. Neither the frame class nor the complete
letter profile of a cutting supplies a pairing that could certify the evenness of a stubborn
fiber.

## Column parities

All 192 used-piece indicators have odd support: each used piece lies in an odd number of
cuttings. Every one of the 24 tetra functionals has even support, on both sides of axis zero.
The two parities sit on opposite sides of the exclusive-or that builds a tetra functional from
its producers, which is consistent with each tetra having an even number of producers, and
neither parity by itself reaches the letter level.

## The exchange distance law

Within a letter-pair fiber, measure the symmetric-difference distance between the piece sets of
two cuttings. Since both have 24 pieces, sharing t of them gives distance d = 48 - 2t, so every
within-fiber distance is even and determined by the shared count.

Across all 256 fibers the complete value list is

`[8, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 48]`

— 19 values. The even values 10 and 46 are absent, and the least value is 8. Restated in shared
pieces: two cuttings in the same fiber never share exactly 1 piece and never share exactly 19,
and the least separation is a four-piece exchange, the least-exchange scale of this lane.

The odd-degree counting argument is the natural next mechanism: in a finite graph where every
degree is odd, the vertex count is even, so a distance rule making all within-fiber degrees odd
would derive fiber evenness. It fails at every rule available here. For each of the 19 values,
the number of fibers whose equal-distance graph has all degrees odd is 0 of 256. For each cutoff
below 48, the number of fibers whose at-most-that-distance graph has all degrees odd is likewise
0 of 256. The sole cutoff that passes is 48, where it passes for all 256 fibers — and that case
is tautological and is recorded here only as a guard: at cutoff 48 the graph is complete, every
degree is the fiber size minus 1, and "all degrees odd" is a restatement of "the fiber is even",
so it derives nothing. The runner prints it labelled as the tautological complete-graph case for
exactly that reason.

## Minimal exchange inside a stubborn fiber

Take the first entry-36 fiber in lexicographic letter order; it has 36 members. Every one of the
36 attains the least distance 8 to some other member, census `{8: 36}`. But the minimizer is not
unique: the runner counts the members carrying a tied minimizer and finds that count nonzero. And
the nearest-partner map obtained by breaking ties on the member order is not an involution: the
runner counts the members whose partner's partner is not themselves and finds that count nonzero
too. So even the minimal-exchange relation, the most canonical-looking pairing candidate the
geometry offers, supplies no pairing of a stubborn fiber.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: the entry census of T and its trace 2000;
the value census of N; the ranks 88, 10 and 6 and the kernel dimension 6; the frame counts 1024,
1024 and 6184 and the odd-class counts 3368 and 856; the distance value list with its absent
values 10 and 46; and, above all, the evenness of the 48 entry-36 fibers itself, which remains
measured, not derived.

Derived at the declared finite scope: the disjointness of the two frame sides from the
five-corner bound; the exact transport identity `N = A-transpose T A`; the corollary status of
the evenness of N; the two-case stabilizer theorem, which needs only the order-2 census and the
odd-cycle witness; the determinacy of the letter by the frame; and the parity restatement
d = 48 - 2t of the distance law together with the absence of shared counts 1 and 19.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

What the cycle buys is a narrowing. The mechanism behind the evenness of the 48 stubborn fibers
cannot be a GF(2)-affine letter functional, cannot be a subgroup action of the pair stabilizer,
cannot be parity transport through the tetra alphabet alone, cannot be a boundary-frame or
letter-profile class pairing, and cannot be odd-degree counting on any exchange-distance rule.
Two entrances are named and open: the 6-dimensional quotient of letter functionals that the
incidence A cannot see, and the frame determinacy theorem, which gives a strictly finer
single-valued carrier of the letter than the letter itself. Both are attacked in the next cycle;
neither is claimed here.

## Reproduction

Run
[physical_cell_cutting_interface_evenness_routes_cycle788_2026_08_14.py](../scripts/physical_cell_cutting_interface_evenness_routes_cycle788_2026_08_14.py).
The reviewed cached output belongs at
[physical_cell_cutting_interface_evenness_routes_cycle788_2026_08_14.txt](../logs/runner-cache/physical_cell_cutting_interface_evenness_routes_cycle788_2026_08_14.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes
in well under a minute on the reference machine, and stays far below one gigabyte. Its final
line is `TOTAL: PASS=16 FAIL=0`, and it exits nonzero if any gate fails.

## Review record and boundary

- The runner prints censuses, ranks, stabilizer and frame counts, and the distance value list;
  the full interface matrix, the incidence matrix and the tetra-pair matrix are deliberately not
  printed, so the note quotes their censuses and the identity between them instead.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- The two sibling stems cited above are not yet on main and are referenced by name only.
- Independent review is required before any downstream use of these results.

Within those boundaries, the appropriate review classification is **bounded support** for the
declared exact finite object.
