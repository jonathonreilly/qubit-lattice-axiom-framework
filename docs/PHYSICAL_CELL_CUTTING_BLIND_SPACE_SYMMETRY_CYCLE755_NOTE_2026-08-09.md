# The cutting-kernel overlaps the seen module in isotypic multiplicity — Cycle 755

Date: 2026-08-09 (revised 2026-08-14 by review-loop)

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_blind_space_symmetry_cycle755_2026_08_09.py)

Independent checker:

- [character/orbital independent checker](../scripts/physical_cell_cutting_blind_space_symmetry_cycle755_independent_check_2026_08_09.py)

Both executables are co-load-bearing. The checker imports no Cycle 755
primary symbols. It live-replays the current Cycle 754 helper and reconstructs
the new character, orbital-residual, and signed-exchange calculations with
separate exact and modular implementations.

Direct scientific dependency:

- [Cycle 754 exact incidence shadow and least unseen exchange](PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09.md)

Both Cycle 755 executables authenticate the current Cycle 754 primary and
independent receipts, including their source and declared-input hashes.

```text
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_blind_space_symmetry_cycle755_note_2026-08-09
target_blocker_text: determine whether the finite symmetry representation isolates the rank-88 seen subspace and identify how much of the kernel one least exchange orbit generates
source_of_blocker_text: Cycle 754 exact rank/kernel and four-for-four exchange boundary
reachability_to_target: exact finite representation theory and exhaustive computation on the supplied coordinate four-cube
artifact_role: bounded finite representation-theory theorem candidate
next_trace_action: independent audit of the landed primary and helper evidence
conditional_surface_status: direct Cycle 754 dependency remains subject to independent audit
hypothetical_axiom_status: none
admitted_observation_status: none
claim_type_reason: exact finite character, commutant, and exchange-orbit identities without a physical or multicell lift
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_blind_space_symmetry_cycle755_independent_check_2026_08_09.py
```

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings, the piece sharing table and the group of
symmetries from scratch and gates each quantity in place. Constitutional
effect: none. This package changes no axiom, no framework Admissibility rule,
no primitive, no policy, and no audit status, and it adds no import and no
assumption to the framework's `MINIMAL_AXIOMS_2026-06-29.md` baseline.

## What this answers

The object is the unit four-cube on sixteen corners, cut into least-volume
pieces at the adjacency cost floor. There are 15800 such cuttings. Between
them they draw on 192 pieces, 24 pieces to a cutting, and each piece lies on
1975 of the cuttings. From that, the piece sharing table: the 192-by-192
integer table whose entry at a pair of pieces counts the cuttings using both,
its diagonal constant at 1975. Call a weighting of the 192 pieces seen if it
lies in the image of that table, and blind if the table sends it to zero —
blind meaning that every one of the 15800 cuttings, totalled piece by piece
against the weighting, comes out zero.

The [preceding cycle](PHYSICAL_CELL_CUTTING_SHADOW_RANK_UNSEEN_SWAP_CYCLE754_NOTE_2026-08-09.md) measured the exact rational rank of the sharing table as
88, so the blind space has dimension 104 and the two add back to 192. That
cycle recorded the rank as a measurement and said in as many words that it did
not derive it. This cycle asks the next question: does the group of 384
symmetries of the whole system — the piece permutations that carry cuttings to
cuttings — single the blind space out as a complete isotypic summand? The
answer is no, and the obstruction is measured by two different calculations
on the same finite object, both returning 21. The kernel itself is nevertheless
invariant under all 384 symmetries.

## Two results against interest, first

**The blind space is invariant but is not a sum of complete isotypic
components, so the named character route does not go through.** The plan was
to derive 88 from the group: if the blind space were a sum of complete
isotypic components of the 384-symmetry representation,
its dimension would be fixed by the trace counts of the group alone, and 88
would follow as the complement. For the invariant orthogonal splitting used
here, the kernel is a sum of complete isotypic components exactly when no
irreducible type appears in both it and the seen row space — exactly when the
character inner product is zero. Here that inner product is 21. In character
notation this is `sum_lambda m_blind(lambda) m_seen(lambda)=21`; it is a
multiplicity-weighted overlap, not a count of 21 distinct irreducible types.
So the fixed-point character together with this splitting does not derive
rank 88.

**The failure count of the natural basis overstated the obstruction.** The
maps commuting with every symmetry have the pair-orbit matrices as a basis. Of
those 104 matrices, only 2 carry the blind space into itself on their own, and
both of those are permutation matrices lying in the group of 384 already; the
other 102 miss, by as much as 12738 in a single entry. The first reading this
cycle made of its own probe was that 102 failures out of 104 means the space
of commuting maps preserving the blind space is tiny. That reading is wrong.
Of the 104 dimensions, 83 preserve the blind space. The natural basis is badly
adapted to the splitting, and the failure count of a basis is not the
dimension of a subspace. The correction is set down here rather than quietly
dropped, because the mistake was this cycle's own.

## Reading the trace of a symmetry on the blind space

Take a basis of the blind space in reduced row echelon form: 104 rows across
192 columns, with a set of pivot columns on which the basis restricts to the
identity. A symmetry acts by moving coordinates. The trace of that symmetry on
the blind space is then the sum, over the 104 basis rows, of the single basis
entry standing in the place the row's own pivot column was moved to — one
entry read per row, with no projector formed at all. The trace of each
symmetry costs 104 lookups. That is what makes this whole cycle cheap enough
to run inside its allowance.

The identity itself is elementary; it is what reduced row echelon form is for.
What the runner supplies is not the identity but the check on it — that the
basis really is in the form the identity needs, and that the one-entry-per-row
sum agrees with the trace of the formed matrix on every one of the 384
symmetries, with no disagreement anywhere.

## The pair-orbit count 104, by three routes

The group has 104 orbits on ordered pairs of pieces, and the runner reaches
that number three ways.

- The averaged square of the fixed-piece count over the 384 symmetries is 104.
- The direct count of orbits on ordered pairs is 104.
- The group has one orbit on the pieces, and the stabiliser of a piece has
  order 2 whose non-identity element fixes 16 pieces; so twice the pair-orbit
  count is 192 plus 16.

Three routes, one number. The third is the one worth keeping, because it ties
the count to the structure of the group — one orbit on the 192 pieces, a
stabiliser of order 2, that stabiliser's other element fixing 16 pieces —
rather than to a sweep over all 384 symmetries.

## What the seen and the blind space share

Averaging the products of the trace counts over the group, block by block,
gives three numbers: seen with seen 29, seen with blind 21, blind with blind
33. They rebuild the pair-orbit count, the cross term entering twice:
29 + 21 + 21 + 33 = 104. That the four add back to 104 is the arithmetic check
that the splitting of the 192 weightings into seen and blind is fully
accounted for, with no part of the module missing from the two sides.

The lead result is the middle number. 21 is not zero, so at least one
irreducible type appears in both the seen space and the blind space, and the
blind space is therefore not a sum of complete isotypic components of the
384-symmetry representation. The exact consequence, and nothing past it: the
isotypic splitting of the 192 weightings is coarser than the seen/blind
splitting; the fixed-point character alone leaves the multiplicity-space
choice open; and so this character route does not fix rank 88. This is not a statement
that the group forbids a blind space of dimension 104 — the group plainly
permits this one, which exists and is carried into itself by every symmetry.
It is a statement that the group does not single this one out.

Also gated here: the symmetries have one orbit on the pieces, so the constant
weighting is the one symmetric weighting. It is seen and it is not blind, and
the blind space holds no constant weighting at all — the trivial part appears
once on the seen side and not at all on the blind side.

## The maps that commute with every symmetry

The linear maps on the 192 weightings that commute with every one of the 384
symmetries span 104 dimensions, and the pair-orbit matrices are a basis for
them. That is why the pair-orbit count is the number that matters here.
Splitting the module into blind plus seen splits that algebra into four
blocks: maps of blind to blind, maps of seen to seen, and the two cross
blocks. Their dimensions are exactly the four averaged products already
listed — 33, 29, 21 and 21. That the dimensions over the rationals are the
same numbers the averaged products give, rather than smaller ones, is because
a space of commuting maps is the solution set of a system of rational linear
equations, and the dimension of such a solution set does not change when the
field is widened.

A commuting map carries the blind space into itself exactly when its
blind-to-seen block vanishes. So the maps that both commute with every
symmetry and carry the blind space into itself form a subspace of dimension
104 minus 21, that is 83. Because the equivalence is exact, the 21 is the
whole of what stands in the way and not a symptom of something larger.

The second route reaches the same 21 without touching a trace count at all. In
coordinates, a map carries the blind space into itself exactly when the
sharing table, times the map, times the transpose of the blind basis is zero:
the blind space is what the sharing table kills, and the transpose of the
blind basis has the blind space as its column span. That condition is linear
in the map, so its rank on the 104-dimensional commuting algebra is
104 minus 83 = 21. The runner computes that rank by elimination over a prime
field on the flattened residuals of the 104 pair-orbit matrices, and gets 21.
A prime-field rank is a floor on the rational rank, hence a ceiling on the
preserving dimension, so this route meets the count from the other side.

The agreement is what discriminates here. One route averages products of trace
counts over 384 symmetries; the other does elimination on residual matrices in
a different arithmetic. They share the supplied finite incidence object and
group action but not the new calculation. Their agreement is a cross-check,
not statistical evidence that coding error is impossible.

## One least exchange orbit reaches 60 of the 104 blind dimensions

A least exchange is a four-for-four: four pieces weighted plus one, four
pieces weighted minus one, every other piece zero. The preceding cycle settled
that no exchange of two pieces for two, and none of three for three, is blind,
so four for four is the smallest shape available. Take one such exchange. It
is blind — no cutting sees it. Its images under the 384 symmetries are 192
distinct signed vectors, and the runner checks every one of the 192 blind
against all 15800 cuttings.

Their span has dimension 60 of the 104 blind dimensions, which leaves 44. That
span is carried into itself by every symmetry and holds no constant weighting.
Its averaged products: with itself 13, with the rest of the blind space 8,
across 6, and with the seen space 11; and 13 + 6 + 6 + 8 = 33 rebuilds the
blind-with-blind count.

So blindness is not generated by this orbit. 44 dimensions of the blind space
are not reached by it, and what does reach those 44 is open — this cycle does
not name a generator for them. Whether a four-for-four exchange exists outside
this orbit was not swept, so the sharper statement, that least exchanges as a
class fall short of generating blindness, is not made here.

## What the runner gates

The repaired primary has source/input-bound receipts, hostile predecessor and
boundary mutations, fail-closed nonzero exit behavior, and the five-line N5
resolution certificate. Its exact gate count and elapsed resources are in the
current canonical cache rather than frozen into this note. It checks:

- the group is rebuilt from scratch and its order 384 gated, along with its
  one orbit on the 192 pieces;
- the piece sharing table is built in exact integers, with the constant
  diagonal 1975 gated and the largest share of two pieces gated at 1266;
- the rank 88 comes from exact rational elimination, not from a numerical
  threshold;
- the symmetry check — that each of the 384 fixes the sharing table and
  carries the blind space into itself — runs in exact integers and again in a
  bounded second arithmetic, and the two agree;
- every averaged product is gated to come out a whole number with remainder
  zero, which a wrong trace count would not give;
- the prime-field elimination that returns 21 the second time is a separate
  arithmetic from everything else in the file.

## Boundary and honest read

**Derived, and holding for finite characteristic-zero representations with the
invariant orthogonal splitting used here:** the four-block splitting of the
commuting algebra along the blind-plus-seen splitting, and hence the 83; the
equivalence between a commuting map carrying the blind space into itself and
the vanishing of its blind-to-seen block; the trace identity that reads one
basis entry per row; and the fact that this invariant subspace is a sum of
complete isotypic components exactly when its character inner product with the
invariant orthogonal complement is zero. These are the general parts, and they
are what the measured numbers are fed into. The kernel itself remains a genuine
invariant subrepresentation; only the stronger complete-isotypic-summand
property fails.

**Measured on this object, and not claimed beyond it:** the group order 384;
the rank 88 and the blind dimension 104; the averaged products 29, 21 and
33 and the pair-orbit count 104; the span 60 and the gap 44; the 2 of 104 and
the 12738. As in the preceding cycle, the rank is a measurement and not a
derivation — and this cycle now adds that the trace counts of the symmetries
do not derive it either.

**Where a gate follows from its premise, that is disclosed.** The rebuild of
33 from 13, 6, 6 and 8 follows by algebra once the splitting is right; it is
not independent evidence for the splitting. The measured content there is that
every averaged product came out a whole number with remainder zero, which a
wrong trace count would not give. The same applies to the rebuild of 104 from
29, 21, 21 and 33.

**What is not swept.** Whether every blind vector supported on eight pieces
lies in the single orbit of 192 was not swept; the count of eight-piece
supports is far past what this runner would carry. What generates the 44 blind
dimensions the least exchanges do not reach is open. And nothing here derives
88 from anything — this cycle narrows where such a derivation could come from,
and that is the whole of what it does.

## Proof-obligation graph

1. Current Cycle 754 primary and helper receipts bind the supplied incidence
   object, rational rank 88, 104-dimensional kernel, symmetry group, and least
   four-for-four exchange.
2. The Cycle 755 primary rebuilds the finite object; the helper live-replays
   the independent predecessor and imports no Cycle 755 primary symbols.
3. Exact kernel invariance makes the blind and seen spaces representations of
   the 384-element group, so their characters and character inner products are
   defined.
4. The exact character inner products 29, 21, and 33 prove multiplicity
   overlap and rebuild the 104-dimensional commutant.
5. Ordered-pair orbitals independently span that commutant; the residual map
   `A -> Gram A kernel^T` has rank 21 over two primes, hence the preserving
   subspace has dimension 83 when combined with the exact character upper
   bound.
6. Exact and modular ranks of all 192 signed images of one least exchange give
   span dimension 60, leaving a 44-dimensional complement in the kernel.
7. Source/input-bound receipts, hostile mutations, nonzero failure exits, and
   independent helper contracts close the process obligations.

There is no unresolved leaf in these finite identities. A structural
derivation of rank 88, a classification of all support-eight kernel vectors,
generators for the remaining 44 dimensions, and any physical or multicell
interpretation remain open.

## No-Go Discipline Gate

The negative conclusions are deliberately narrow: one fixed-point-character
route does not isolate the measured kernel as a complete isotypic summand, and
one signed least-exchange orbit does not generate the whole kernel. No claim is
made that every symmetry, incidence, spectral, coding, or combinatorial route
to rank 88 fails.

### N1 — alternative routes

1. **ATTEMPTED — exact kernel route.** Exact rational elimination and direct
   incidence multiplication establish the 104-dimensional kernel and its
   invariance, preventing the rhetoric from denying that it is a symmetry
   subrepresentation.
2. **ATTEMPTED — character-orthogonality route.** Exact character inner
   products give seen/blind overlap 21, which rules out only a decomposition
   into complete isotypic components.
3. **ATTEMPTED — orbital-commutant route.** Ordered-pair orbitals and the
   residual map independently give rank 21 and preserving dimension 83; the
   primary and helper use distinct arithmetic implementations.
4. **ATTEMPTED — Burnside/stabilizer route.** Fixed-point averaging, direct
   ordered-pair orbits, and the order-two point stabilizer independently give
   commutant dimension 104, closing the ambient dimension used by route 3.
5. **ATTEMPTED — least-exchange generation route.** All 192 signed images of
   the Cycle 754 witness are checked and span only 60 kernel dimensions,
   leaving 44; this says nothing about other exchange or incidence generators.
6. **ATTEMPTED — hostile-boundary route.** Both receipts reject a mutation
   that widens the named character obstruction into a universal no-route
   claim, so stale broad rhetoric cannot remain green.

### N2 — wall independence

No multiple-wall theorem is asserted. The three open questions — a structural
rank derivation, classification of all support-eight kernel vectors, and
generation of the remaining 44 dimensions — are an inventory, not an
independence claim or wall count.

### N3 — hidden-wall scan

The load-bearing inputs are the supplied finite incidence object and current
Cycle 754 rank/kernel/exchange certificate. Standard finite-group character
orthogonality is used transparently. No framework primitive, physical bridge,
continuum limit, probability rule, or empirical input is hidden in the claim.

### N4 — residual matching

The direct predecessor is Cycle 754: it supplies rank 88, kernel dimension 104,
the 384 exact symmetries, and the explicit four-for-four exchange. Cycle 755
tests exactly the next residuals — complete-isotypic isolation and orbit-span
generation. It does not cite Cycle 754 as having already answered either one.

### N5 — rhetoric and resolution

- `per_element`: all 192 piece coordinates are exercised.
- `per_site`: one supplied coordinate four-cube is exercised; no multi-site
  or translated-lattice claim is made.
- `per_mode`: exact characters test irreducible multiplicity overlap.
- `per_block`: blind, seen, exchange-orbit, and complementary blocks are
  exercised.
- `lattice_wide`: not exercised; no infinite-lattice or continuum conclusion
  is made.

Accordingly, the earlier phrase “not a symmetry object” is rejected. The
kernel is invariant. The landed claim is only failure of the stronger
complete-isotypic-summand property and of one named exchange-orbit generator.

### N6 — partial-closure paths

No new axiom, primitive, convention, or physical import is required for these
finite identities. The open rank route could still close through the incidence
algebra, a finer group-module invariant, an exact design identity, coding
theory, or a different combinatorial generator. Those are research paths, not
walls promoted into premises.

### N7 — steelman

A hostile reviewer should insist that character overlap 21 only defeats the
complete-isotypic-summand shortcut. The full labeled incidence algebra contains
far more information than the fixed-point character, and another canonical
invariant could still force rank 88. Likewise, a single least-exchange orbit
spanning 60 dimensions says nothing about other support-eight or larger
generators. This steelman is correct and is built into the narrowed claim; it
would defeat any universal symmetry or exchange no-go.

### N8 — cross-cycle echo

Cycle 754 already distinguished failure of two proposed rank/lower-bound
routes from a universal impossibility result. The same mechanism applies here:
record the exact failed route and preserve the broader target as open. No prior
wall-retirement mechanism is foreclosed or relabeled as requiring a new axiom.

No-Go Discipline result: **PASS for the narrowed finite negative boundary.**

## Next

Three paths open from here. Find the smallest blind vectors lying outside the
60-dimensional span, since those are what name the missing generators, and
their supports are the first thing to look at. Ask whether the 60-dimensional
span is exactly the span of all blind vectors supported on eight pieces, which
would say the least exchange is not merely one generator among others but the
whole of the eight-piece blind content. And look for the rank 88 in the
structure of the incidence map itself — in how the 15800 cuttings meet the 192
pieces — rather than in the trace counts of the group, which this cycle shows
do not carry it.
