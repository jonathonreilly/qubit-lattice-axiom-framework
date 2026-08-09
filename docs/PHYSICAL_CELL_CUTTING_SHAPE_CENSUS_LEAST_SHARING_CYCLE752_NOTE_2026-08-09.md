# The shape is common; the counts of shared cuttings carry the charge — Cycle 752

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09.py)

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
of the cuttings, needs sixteen pieces to carry it, and the system holds 132
such smallest carriers, each piece lying on 11 of them.

An earlier cycle joined two pieces of one carrier whenever no cutting used
both and found the corners and edges of a four-cube on 60 of those 132; the
cycle after it put the rest of the 192 pieces back and found that shape to be the
distance the whole object already had. Neither asked the flat question that
comes next. Is the four-cube shape rare?

It is not, and this note reports that against the interest of the two cycles
before it.

## The shape is common

Join every one of the 192 pieces to every other sharing none of the 15800
cuttings, which gives 33 joins at each piece, and then count every sixteen
pieces joined exactly like the corners of a four-cube.

| four-cubes among the never-sharing joins | count |
| --- | --- |
| through one piece | 4978, the same number at all 192 |
| in all | 59736 |
| carrying none of the eight readings | 59676 |
| carrying the charge called four | 60 |

All 50 generating symmetries of the table carry every one of the 59736 shapes
to a shape. The four-cube is therefore not the mark of the charge. It is
available at every piece in the object, thousands of times over, and 59676 of
the 59736 read as nothing at all. Whatever separated the 60 carriers from
their surroundings in the earlier cycles, it was not the shape.

## What carries the charge is a ranking, not a test

There is a single number attached to a shape that has no reading anywhere in
it. Take the 120 pairs of pieces in the shape, count for each pair how many of
the 15800 cuttings use both, and add the 120 counts. Nothing in that recipe
consults a mark, a reading, or a charge.

Rank all 59736 shapes by it. The 60 lightest are exactly the 60 four-cube
carriers of four, and the ranking steps clear across the boundary:

| shapes ranked by the cuttings their 120 pairs share | total |
| --- | --- |
| every four-cube carrier of four | 19800 and below |
| every one of the other 59676 shapes | 20338 and above |

The same holds piece by piece rather than only in aggregate. At all 192 of the
192 pieces, the 5 lightest of the 4978 shapes through that piece are the 5
carriers through it, and the sixth is at least 538 heavier. So the ranking is
not a global accident that a local view would break.

Two weaker readings are reported alongside, because they show that not every
plausible test does this work. Asking only that pairs two steps apart share
fewer cuttings than pairs three steps apart picks out the same 60. Asking the
same of three against four lets 1488 shapes through, and asking that all eight
far corners sit at 433 lets 672 through. Inside a carrier the bands are 170 to
184 at two steps, 240 to 250 at three, and 433 at the far corner every time.

## Why there is a floor underneath it

The ranking is not only measured. Part of it follows.

A sixteen-piece set meets the 15800 cuttings 31600 times in all, since each
piece lies on 1975 of them. Carrying the charge called four means meeting each
of the 5664 marked cuttings an odd number of times and each of the others an
even number. The total this note ranks by is the sum over cuttings of the
pairs a cutting contributes, so it falls as the 31600 meetings are spread more
evenly, and the parity requirement is what stops them spreading evenly. The
cheapest spread consistent with it leaves half of the 5664 marked cuttings met
once and half met three times, and everything else met twice, which costs

    15800 + 5664 / 2 = 18632

shared cuttings at the very least. That number is derived, not measured.

The carriers come within 1008 of it, sitting at 19640, and the 1008 is
accounted for exactly: 252 cuttings the carrier misses altogether and 252 it
meets four times, each of them displaced from the cheapest value. Across all
132 carriers the total takes just 4 distinct values, least 19640 and most
24216.

So the bottom of the ranking is where a carrier has to be, and the carriers
sit close to the bottom. That the gap is 1008 and not something else is
measured, not derived.

## Boundary and honest read

**The metric test does not single out four among the eight readings.** Of the
59736 shapes, 59676 carry no reading at all and 60 carry four, so within this
population carrying a reading and carrying four are the same condition. The
ranking separates shapes that carry something from shapes that carry nothing.
Every shape it finds does carry four; nothing here shows it would tell four
from a different reading in a population holding both.

**The separation test is not claimed to be the only description that fits.**
It is reported because it names no value, which the two weaker tests do not
improve on. Tests that do name a value select these same shapes as well. The
content of the section is the 1488 and the 672: not every plausible test works.

**The floor is derived but is not shown to be attained.** 18632 is a lower
bound that any carrier of a reading with this many marked cuttings must
respect. Nothing here shows that 19640 is forced, or that 18632 is out of
reach for some carrier this search did not produce.

**The shape result cuts against the two cycles before this one.** They
established that a carrier has a definite shape and that the shape survives
being put back in the object. This note establishes that the shape is common,
so neither of those results can be read as the shape detecting the charge.
What survives is narrower and better founded: the shape is real, and it is the
counts on the shape that track the charge.

**All 132 carriers carry four**, so that reading alone does not separate the 60
four-cube carriers from the rest of the 132. The split between the two shapes
remains a fact about the families, not about which charge is carried.

Nothing here moves the bracket on an eighteen-piece carrier of any other
reading, and nothing here bears on the axioms, on Admissibility, or on any
primitive.
