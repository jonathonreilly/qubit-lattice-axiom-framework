# The ranked total is a spread about a forced mean — Cycle 753

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings and the block bookkeeping from scratch and
gates each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## What this answers

The unit four-cube cuts into least-volume pieces at the adjacency cost floor
in 15800 ways, and those cuttings use 192 pieces between them, 24 to a cutting
and 1975 cuttings through each piece. The charge called four is marked on 5664
of the cuttings and needs sixteen pieces to carry it.

A preceding cycle joined two pieces whenever no cutting used both, counted
every sixteen pieces joined exactly like the corners of a four-cube, found
59736 of them with 4978 through every single piece, and ranked them by one
number: take each pair of pieces, count how many cuttings use both, and add
those counts over all pairs. The 60 shapes that carry the charge came out
lightest. That cycle reported the ranking as a measurement and a floor
underneath it as a derivation, with no account of why the ranking works.

This cycle supplies the account, and it is not the account the preceding cycle
would have guessed. The ranked total turns out to be a spread about a mean the
system fixes in advance, and the statistic that picks the carriers out is not
the size of their reading support.

## The mean is fixed before any shape is chosen

For a set of sixteen pieces write `m` for the number of its pieces lying on a
given cutting. Each piece lies on 1975 cuttings, so the sixteen pieces meet
the 15800 cuttings 31600 times in total, and

```
31600 = 2 x 15800
```

Whichever sixteen pieces are taken, and whether or not they carry anything,
the average number of them met per cutting is exactly two. Nothing about the
choice can move it.

## The ranked total is the squared departure from that mean

Every cutting met `m` times contributes `m(m-1)/2` such pairs, so the ranked
total is the sum of `m(m-1)/2` over the 15800 cuttings. Expanding about two,

```
sum (m-2)^2  =  sum m^2  -  4 x 31600  +  4 x 15800
```

and the ranked total is `(sum m^2 - 31600) / 2`, so for every sixteen-piece
set whatsoever,

```
ranked total  =  15800  +  (1/2) x sum (m-2)^2
```

This is an identity, not a fit. It carries no condition on how large `m` may
get. The right-hand side is a whole number because the departures sum to zero
and a square has the parity of its root, so their squares sum to an even
number.

So the quantity the preceding cycle ranked by is a spread. Ranking the shapes
by shared cuttings is ranking them by how far their meetings stray from the
two-per-cutting average the system already imposed, and being light means
being flat.

## The floor, and exactly what reaching it would take

Carrying a reading marked on `S` cuttings means meeting each of those an odd
number of times, so the departure from two is at least one on each of them and
at least zero elsewhere. Hence

```
ranked total  >=  15800 + S/2
```

for any carrier of that reading, which for the charge called four is 18632.
The identity says more than the bound: equality holds precisely when the
carrier meets each of the 5664 marked cuttings once or three times and each of
the rest exactly twice. The mean then forces the split, 2832 met once and 2832
met three times. The floor is not merely a number to sit above; it
names a single profile, and any carrier failing to reach it fails by a
countable number of off-mean cuttings.

In particular the floor demands that the carrier miss no cutting at all. A
cutting the carrier does not meet sits two below the mean, so it costs four
where a marked cutting costs one, and a missed cutting cannot be a marked one
because zero is even. The floor therefore rises by two for every cutting
missed. So the floor is not merely unreached by the carriers found here; it is
out of reach for any carrier that misses a cutting, and the shortfall grows
with the number missed.

The preceding cycle derived 18632 and left it there. What is added here is
that reaching it is a determinate combinatorial demand, so the gap between
18632 and what carriers actually do is a fact about the object rather than
slack in the argument.

## What the carriers actually do

The lightest carrier meets 9632 cuttings twice, 2832 once, 2832 three times,
252 not at all and 252 four times, and no cutting more than four times. Its
squared departure is 7680, so its total is

```
15800 + 7680/2 = 19640
```

which is 1008 above the floor, and the 1008 is accounted for exactly by the
cuttings sitting two away from the mean, 252 in each direction.
Across all 132 smallest carriers the squared departure takes 4 values, least
7680 and most 16832.

## What picks the sixty out is the count of cuttings met exactly twice

Rank all 59736 shapes by how many cuttings they meet exactly twice, largest
first. The 60 carriers occupy the top 60 places. The least of them meets
9616 cuttings twice; the next shape down the list meets 8688. So within
this population the carriers are exactly the shapes meeting at least 9616
cuttings exactly twice, with no shape tying across the boundary.

That is a sharper statement than the preceding cycle's, and it says what the
ranking is sensitive to: not the total spread but the number of cuttings
sitting exactly on the mean.

## What does not pick them out is the reading

This cycle set out to test the opposite hypothesis, and the measurement went
against it, which is worth stating plainly because the preceding cycle's
headline depends on the answer.

The suspicion was that the ranking might be a disguised count of the reading
support: a carrier of the charge called four is odd on 5664 cuttings, and a
term of that size set against the modest step separating the carriers from
everything else would mean the ranking was detecting the mark it claimed not
to consult. Ranking the shapes by how many
cuttings they meet an odd number of times puts the matter to rest in the other
direction. The carriers rank 57973rd to 58032nd of 59736. Fully 57972 shapes
meet strictly more cuttings an odd number of times than a carrier does, so the
odd count is not what the carriers are extreme in; on that scale they are near
the bottom, and the term works against their position rather than for it.

The size of the reading support therefore does not explain the separation; the
twice-met count is the statistic that performs it. Why the carriers should be
the shapes flattest against the mean is a further question this page does not
answer, and nothing here says the reading is irrelevant to it: every shape in
the top sixty carries one.

## Where the earlier linear form does and does not hold

If no cutting is met more than four times, eliminating the thrice-met count
between the two sum rules gives a linear form in the odd count and the
twice-met count alone, with the four-times count cancelling. That form holds
on exactly 17544 of the 59736 shapes. It fails on the rest because the
condition fails on the rest: 42192 of the shapes have some cutting met more
than four times. The shapes satisfying the form and the shapes no cutting
meets more than four times are the same 17544 shapes.

How far a cutting can go is not a measurement. Two pieces joined in the
never-sharing graph lie on no common cutting, so the pieces of one shape that
a single cutting meets are pairwise unjoined, and a four-cube has at most 8
corners that are pairwise unjoined. No cutting can meet one of these shapes
more than 8 times, and 8 is reached.

This is recorded because the linear form is the natural first thing to write
down, and it is the identity above, not that one, that holds without a
condition.

## Boundary

- The identity relating the ranked total to the squared departure is derived
  and holds for every sixteen-piece set in the system, carrier or not. The
  floor and its equality condition are derived. Everything else on this page is
  measured over the 59736 four-cube-shaped sets and is not claimed beyond them.
- What the runner measures about the identity is its premise and its arithmetic,
  not the identity itself: that the multiplicities of each of the 59736 shapes
  sum to 15800 and weigh 31600, and that the total taken from the multiplicity
  profile agrees with the total taken from the shared-cutting counts. Given the
  premise the identity is algebra, and that is what makes it unconditional.
- **The floor 18632 is still not shown to be attained.** No shape found here
  reaches it. Nothing here shows 19640 is forced, and nothing here rules out a
  carrier of some other shape reaching 18632.
- **The twice-met criterion is a threshold on this population, not a proof.**
  Nothing here derives 9616, and nothing here shows a shape outside these 59736
  could not meet at least that many cuttings twice without carrying anything.
- Within these 59736 sets, carrying a reading and carrying the charge called
  four coincide, so what these rankings demonstrably separate is sets that
  carry something from sets that carry nothing. Neither ranking is shown to
  tell the charge called four from a different reading.
- The refutation reported above is a refutation of a hypothesis about this
  ranking. It does not show that no count of reading support could separate
  these shapes; it shows this one does not, in the direction claimed.

## Runner

Rebuilds the cell complex, the cuttings, the readings and the block
bookkeeping from scratch and gates every quantity in place. Class-A: integer
and two-element-field arithmetic on a finite explicit object, no solver.

```
TOTAL: PASS=42 FAIL=0
```
