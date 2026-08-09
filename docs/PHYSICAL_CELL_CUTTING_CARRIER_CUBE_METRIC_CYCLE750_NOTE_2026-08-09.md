# A distance appears inside a smallest carrier of a charge — Cycle 750

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_carrier_cube_metric_cycle750_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings and the block bookkeeping from scratch and
gates each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Headline

The unit four-cube cuts into least-volume pieces at the adjacency cost floor
in 15800 ways, and those cuttings use 192 pieces between them, 24 to a cutting
and 1975 cuttings through each piece. The charge called four is marked on 5664
of the cuttings, needs sixteen pieces to carry it, and the system holds
exactly 132 such smallest carriers, each piece lying on 11 of them.

Take one of those carriers, throw away everything except the incidence table
restricted to its own sixteen pieces, and join two pieces when no cutting in
the whole system uses both. What comes back is not an assortment. It is one of
exactly two shapes and never anything else:

| shape of the never-sharing joins | carriers | joins | families |
| --- | --- | --- | --- |
| the corners and edges of a four-cube | 60 | 32 | 12, 12, 12, 24 |
| two separate three-cubes | 72 | 24 | 24, 48 |

Sixty and seventy-two make 132, and no carrier gives a third answer. The two
join counts, 32 and 24, are the two values an earlier cycle recorded without
naming: a four-cube has 32 edges and two three-cubes have 24 between them. The
shape is constant on a family, and the split it makes is exactly the split
that reading made.

That is the first half. The second half is that the shape then carries a
distance, and the incidence table gives the distance back.

## The distance the shape carries

Inside a four-cube carrier, walk from one piece to another along the joins and
count the steps. Then look up how many of the 15800 cuttings the two pieces
share. The counts sort by the number of steps into bands that do not meet and
that rise:

| steps apart in the four-cube | cuttings the pair shares |
| --- | --- |
| 1 | 0 |
| 2 | 170 to 184 |
| 3 | 240 to 250 |
| 4, the far corner | 433, every time |

The first row is how the joining was made and says nothing on its own: one
step in the shape *is* a pair sharing no cutting, by definition. Nothing made
the other three rows. They are measured, not derived from the construction,
and they could have overlapped. They do not. Twelve counts occur in all, and
each of the twelve belongs to one number of steps and no other, so the number
of steps is a function of the count. The far corner is sharper still: a single
value, 433, on every four-cube carrier in the system.

Two consequences follow at once from that, without any further computation.
First, the distance a pair receives does not depend on which relabelling of
the shape onto the four-cube the search happens to return, because the count
is a property of the pair alone and the count already determines the distance.
Second, counting cuttings recovers the whole metric: there are no coordinates
anywhere in the computation, only integer counts on a finite table, and out of
them comes a distance on sixteen pieces.

The other 72 carriers behave the same way inside each of their two cubes: one
step gives 0, two steps give 170 to 174, and the far corner of a three-cube
gives 250 every time, again a single value. Pairs taken across the two cubes
give 202 to 666, which meets none of the inside values, and the largest count
anywhere in such a carrier is always a crossing pair, in 576 of 576 cases.

## What the shape is not

The pieces are cells on five of the object's own 16 corners, so there is an
obvious guess: that this four-cube is the ambient four-cube wearing a
disguise. Two measurements are reported against that guess, and the second
refuses it.

A four-cube carrier's sixteen cells do cover all 16 corners of the object, and
two pieces joined by never-sharing do meet in exactly 2 corners, a shared
edge. But the converse fails, and by a wide margin: 2016 farther pairs, pairs
at two, three or four steps, also meet in exactly 2 corners. Meeting in an
edge is therefore not what makes a join, and the shape reported here is not
the ambient four-cube relabelled. It is a shape the cutting system produces.

Two checks guard the result itself. The relabelling search is given a
four-cube with two of its joins moved elsewhere, which still has 32 joins and
still has the same count of joins at every piece, and refuses it; it also
refuses the two three-cubes against the four-cube in both directions. And sixteen pieces taken
evenly spaced through the table's own ordering, in four spacings, give 768
control sets, of which 0 produce either shape, against 132 of 132 for the
carriers. The shape follows from carrying the charge, not from taking sixteen
pieces.

## Boundary and honest read

The one-step row of the distance table is true by construction and is stated
that way here and in the runner's own gate; the content is in the three rows
below it.

The shapes are measured on all 132 carriers and found constant on each family.
Nothing here proves from the symmetry group that they must be constant, or
that a third shape is impossible for a carrier of some other charge.

A control is not a proof of rarity. That 0 of 768 evenly spaced sets give
either shape is evidence that the shape tracks the charge; it is not a theorem
that no other sixteen pieces can give it.

Across the two cubes of a 72-carrier there is no distance to sort by, and none
is claimed: the crossing counts are reported as one band, disjoint from the
inside bands, and nothing more is read into them.

The relabelling search is a direct backtracking search over labellings and
sees only the 0/1 table of joins. It never sees how many cuttings a pair
shares. The counts are read off afterwards, so no part of the distance result
can have been arranged by the search.

Nothing here moves the bracket on an eighteen-piece carrier of the flip
partner of four, and nothing here bears on the axioms, on Admissibility, or on
any primitive.
