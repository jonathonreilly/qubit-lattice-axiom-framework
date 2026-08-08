# The complete search at fourteen is empty for the six charges — Cycle 741

Date: 2026-08-05

Cycle: 741

Authority: none

Audit: unset.

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [the complete search at fourteen, licensing, orbit inventories, planted controls](../scripts/physical_cell_cutting_fourteen_frontier_cycle741_2026_08_05.py)

Standing framework: [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This package changes no axiom, framework
Admissibility rule, primitive, registry, policy, audit result, or audit status.
It measures finite structure on an object the previous cycles already built, and
nothing in it is promoted above its own scope.

## Result

The object is the incidence table of the least-cost cuttings of the unit
four-cube into pieces of least volume: 15800 cuttings, 24 pieces to a cutting,
192 pieces in all, over the field with two elements. Row rank 88, kernel
dimension 104, all 15800 rows pairwise distinct, every piece used by exactly
1975 cuttings. A piece set *carries* a reading when on every one of the 15800
cuttings the parity of its meet with that cutting reproduces the reading there.

The previous cycle searched every set of at most twelve pieces and found no set
carrying either side of any of the three physical charges, and the forced-parity
certificate makes each of those six readings force an even whole, so every odd
size is barred. Fourteen was the open size. This cycle runs the complete search
at exactly fourteen.

**Nothing at fourteen carries a charge.** The complete search over the licensed
cells at fourteen returns, on the eighteen readings carried through the runner,
the counts

    34560,26880,0,0,0,0,0,0,2665,274,329,236,1,3,11,2,6,0

The first two entries are the constant zero and constant one readings; the next
six are the two sides of each of the three charges and every one of them is
empty; the next four are the planted controls; the next five are the planted
fourteen-piece sets, each recovered by a search blind to it; the last is the
synthetic reading, which lies outside the column space and licenses no cell at
fourteen at all. All 64967 recorded sets recompute to their own reading on all
15800 cuttings, have weight 14, and are distinct.

**The floor for the six charge readings moves to sixteen.** The searches at two,
four, six, eight, ten, twelve and fourteen are complete and empty for the six in
this same run, and each of the six forces an even whole, so no odd size can hold
one either. A set carrying a side of one of the three charges therefore needs at
least sixteen pieces.

The zero and one readings at fourteen fall into 720 and 560 orbits respectively,
every orbit of size 48, under the 48 symmetries that fix those readings. That is
not decoration: a complete family of fourteen-piece carriers is closed under the
symmetries that fix its reading, so it can only break into orbits whose sizes
divide 48, and an incomplete search shows up there immediately as an orbit of
some other size.

## What was searched

Eighteen readings are carried through every sweep at once:

- the constant zero reading and the constant one reading;
- the two sides of each of the three physical charges, six readings;
- four planted controls of the previous cycles' construction;
- five planted fourteen-piece sets, drawn from a printed fixed seed to the five
  quarter profiles 7-7-0-0, 4-4-4-2, 2-2-4-6, 0-2-4-8 and 0-0-2-12. Two of them,
  0-2-4-8 and 0-0-2-12, hold one quarter heavy enough to force the eighth cut
  described below, and 7-7-0-0 holds two such quarters at once, the case that
  first appears at fourteen;
- one synthetic reading built to force an odd whole, which therefore cannot lie
  in the column space and must be carried by nothing.

The sweeps run at every set of at most eight pieces, then at exactly ten, twelve
and fourteen. The three earlier sizes are reproduction: at most eight returns 648
sets for the zero reading and 192 for the one reading with orbit inventories 17
of size 24 and 5 of size 48, and 2 of size 24 and 3 of size 48; ten returns
`0, 0, 0, 0, 0, 0, 0, 0, 108, 1, 2, 0` on the twelve readings it shares with the
previous cycle; twelve returns `7808, 3072, 0, 0, 0, 0, 0, 0, 661, 25, 38, 38`.
Those are the earlier cycle's landed values, recomputed here from the
construction rather than read back.

"Complete" here means complete over the cells a reading licenses, with the
licensing itself derived in-run from the forced-parity certificate. A cell is the
quarter profile of a candidate set. Of the 15 single-block indicators exactly the
whole set, its two halves and the two quarters of the second half lie in the row
space, so their parities are forced for every reading; a cell whose whole, half
or quarter parity disagrees with what a reading forces cannot hold a carrier of
that reading and is skipped, and nothing is skipped for any other cause. At
fourteen this licenses 204 cells for an even reading, 140 for an odd quarter
reading, none for the synthetic reading, and 344 cells in all across the
eighteen readings; every one of the 344 is visited.

The licensed counts for an even reading at sizes two through fourteen are 5, 14,
30, 55, 91, 140, 204, whose consecutive differences are 9, 16, 25, 36, 49, 64 —
the squares. The count 204 at fourteen is obtained here by direct enumeration and
then compared, in-run, against the arithmetic continuation 140 plus 64; the odd
quarter readings give 140 against 91 plus 49 the same way.

## Method

The runner builds the 15800 by 192 table from the construction, reduces it over
the field with two elements, and reads the forced block parities off the row
space. It then enumerates, for each size, the cells each reading licenses, and
searches each licensed cell once with all live readings folded together.

A cell is searched by splitting it into one streamed part and the parts met
against it. A part is one quarter of the 192 pieces at a count the six-subset
tables cover, or one eighth at any count up to fourteen. Every quarter whose count
passes what those tables cover is cut into its two eighths, and the cell is
covered by the product of those cuts; a quarter part requested past the tables
raises rather than falling back to a lower count. At fourteen that rule is
load-bearing, because a licensed cell can hold two quarters of seven pieces each,
which no smaller size permits. The 344 licensed cells at fourteen take 2562
splits and the splits are distinct.

A meet joins two part tables on the parities that live inside the blocks joined
so far. Every join is a necessary condition on the same final set, so the answer
does not depend on the join order, and the order is chosen to keep the largest
intermediate table small. No intermediate or final table is permitted past
30000000 entries; a cell that reached that cap would have been counted and would
have failed a gate, and the search over that cell would not have been complete.
No cell reached it.

Independent of the sweeps, the sets inside the first quarter met evenly by every
cutting are enumerated directly as a space of dimension 14 with 16384 words, of
least nonzero weight 8, with 30 words at weight 8, 63 at weight 12 and 164 at
weight 14. The search restricted to that quarter alone at fourteen is then
required to return exactly those 164 words.

## Verification

Every line below is a gate in the runner, printed in this order, all passing.

- G01  the cuttings of least cost form a 15800 by 192 table over the two element field
- G02  every one of the 192 pieces is used by exactly 1975 cuttings, an odd count
- G03  that table has rank 88 and kernel dimension 104
- G04  the 15800 cuttings are pairwise distinct as piece sets
- G05  of the 15 block indicators exactly the whole set, its halves and the two quarters of the second half lie in the row space
- G06  those quarters force the printed parity vector on the first twelve readings; the whole and its halves force even; the synthetic reading forces an odd whole
- G07  each planted fourteen piece reading forces exactly the whole, half and quarter parities its own profile has
- G08  the sets inside the first quarter met evenly by every cutting form a space of dimension 14, all 16384 words verified
- G09  its least nonzero weight is 8, with 30 words there and 63 at weight 12
- G10  the five planted readings are fourteen distinct pieces each, drawn to the five quarter profiles their names carry
- G11  all but the synthetic reading lie in the column space, so each of the six charges is carried by some set
- G12  the cells an even reading licenses at sizes 2 to 12 are [5, 14, 30, 55, 91, 140] with square differences [9, 16, 25, 36, 49], reproducing an earlier cycle
- G13  at fourteen the count 204 for an even reading equals the continuation 140 plus the next square 64, and 140 for an odd quarter reading equals 91 plus 49
- G14  the synthetic reading, whose forced whole is odd, licenses no cell at fourteen
- G15  a complete search of every set of at most eight pieces finds 648 carrying the constant zero reading and 192 the constant one reading, all 845 recorded sets verified
- G16  no set of eight or fewer carries either side of any charge, or the synthetic odd reading
- G17  the 648 zero-reading sets fall into 22 orbits of the symmetries, 17 of size 24 and 5 of size 48, and the 192 one-reading sets into 5 orbits, 2 of size 24 and 3 of size 48
- G18  all 30 weight 8 words of the quarter subcode, enumerated apart from it, are among those 648
- G19  a complete search at ten reproduces an earlier cycle on the twelve readings it shares: [0, 0, 0, 0, 0, 0, 0, 0, 108, 1, 2, 0], the synthetic reading licensing no cell
- G20  a complete search at twelve reproduces an earlier cycle on the twelve readings it shares: [7808, 3072, 0, 0, 0, 0, 0, 0, 661, 25, 38, 38], and finds no synthetic set
- G21  every licensed cell at twelve is met once per reading, 140 per even and 91 per odd quarter reading, its 1167 splits distinct
- G22  all 11642 recorded sets at twelve recompute to their own reading, have weight 12, and are distinct
- G23  all 63 weight 12 words of the quarter subcode are among the 7808 sets carrying the zero reading at twelve
- G24  the complete search of the first quarter alone at fourteen returns the 164 weight 14 words of its subcode, enumerated apart from the search
- G25  every licensed cell at fourteen is met once per reading, 204 per even and 140 per odd quarter reading, its 2562 splits distinct
- G26  no intermediate or final table in any of the searches reached the cap of 30000000 entries
- G27  all 64967 recorded sets at fourteen recompute to their own reading, have weight 14, and are distinct
- G28  each of the five planted fourteen piece sets is found by a search blind to it, including the two whose profile cuts one quarter and the one that cuts two
- G29  the sets found at fourteen fall into orbits of the symmetries that fix their reading, of sizes dividing 48
- G30  the synthetic reading outside the column space is carried by no set at any size searched
- G31  neither side of any of the three charges is carried by any set of exactly fourteen pieces
- G32  the searches at every even size to fourteen are complete and empty for the six, and each forces an even total, barring every odd size: the six charges need at least sixteen pieces
- G33  the whole runner finishes under 900 seconds inside the printed 2500 MB
- G34  its output stays under 5500 characters

The runner keeps its output under 5500 characters, and the run is bounded at
elapsed under 500 s and peak memory under 2500 MB, both printed and both checked
against the measured run.

## Boundary and honest read

The construction is one canonical cutting family in one fixed piece order. The
block labels, the quarter and eighth partitions, and therefore the cells, are
properties of that order: they are measured, not derived. Another order would
relabel every cell in this note, and the forced-parity certificate that does the
licensing would have to be re-measured against it. Nothing here shows the family
of least-cost cuttings is unique or canonical in any sense beyond the
construction the runner builds.

"Complete" is complete over licensed cells, not over all cells. The licensing is
derived in-run from the certificate and from nothing else, and a cell is dropped
only when its forced whole, half or quarter parity contradicts the reading's; the
gate that every licensed cell is met once per reading, with distinct splits, is
what carries that claim. If the certificate itself were wrong the licensing would
be wrong with it, which is why the forced blocks are recomputed here from the row
space rather than assumed.

The square-difference continuation of the licensed counts is measured, not
proven. The count 204 at fourteen is enumerated directly and then found to agree
with 140 plus 64; no argument is given here that the pattern continues past
fourteen, and the runner would have printed both numbers and failed its gate had
they disagreed.

The table cap is a real boundary. Had any intermediate or final table passed
30000000 entries the runner would have recorded it and failed a gate, and the
cell that blew it would have been searched incompletely — the emptiness claim
would then cover strictly less than it says. No cell reached the cap in this run,
and the cap was not moved to make that true.

The orbit inventory is a completeness check and not a summary. A complete family
of fourteen-piece carriers is closed under the 48 symmetries fixing the zero and
one readings, so it must break into orbits of sizes dividing 48; the measured
inventories are 720 orbits of size 48 and 560 orbits of
size 48. A search that missed part of a cell would show an orbit of some other
size, and the gate is written to fail on exactly that.

On the six charges, this note says only that no set of at most fourteen pieces
carries a side of one of them, and that every odd size is barred by the forced
even whole. It says nothing about sixteen beyond that bound: no search at sixteen
was run, and nothing here shows a carrier at sixteen exists, or that the smallest
carrier is unique, or what any such carrier would mean physically. The six
readings do lie in the column space, so a carrier of some size exists for each of
them; where the smallest one sits at or above sixteen is open.

## Claim type

`Claim type: bounded_theorem`. The claims are finite, integer and
field-with-two-elements statements about an explicitly constructed 15800 by 192
table, each one carrying a certificate checked in the runner. The conditionality
is stated above: the cell labels are relative to the fixed canonical order, and
completeness is relative to the licensing the certificate supplies.

## Audit

`Audit: unset.` This note sets no audit verdict and predicts none. The
independent audit lane is the sole authority on audit language for this package.
