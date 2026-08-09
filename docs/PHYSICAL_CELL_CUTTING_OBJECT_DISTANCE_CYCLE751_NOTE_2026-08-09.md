# The shape inside a smallest carrier is the object's own distance — Cycle 751

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_object_distance_cycle751_2026_08_09.py)

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

A preceding cycle joined two pieces of one carrier whenever no cutting used
both, threw the rest of the system away, and got one of exactly two shapes:
the corners and edges of a four-cube on 60 of the 132, two separate
three-cubes on the other 72. Throwing the rest of the system away is the
weakness of that result. Sixteen pieces looked at alone can be made to look
like anything; the question is whether the shape survives putting the rest of
the system back.

It does, and that is this cycle's claim. Join every one of the 192 pieces to
every other piece that shares no cutting with it. The result is a single
object, the same 33 joins at every piece, 3168 joins in all, carried to itself
by all 384 symmetries of the table, and with no two pieces standing more than
three steps apart:

| steps apart in the whole object | pairs of pieces |
| --- | --- |
| 1 | 3168 |
| 2 | 12576 |
| 3 | 2592 |

Two independent computations of those steps, walking outward from each piece
and multiplying the join table by itself, agree on all 18336 pairs.

Now put a carrier back into it. Every pair inside a smallest carrier of four
that the carrier's own shape puts one, two or three steps apart stands exactly
that far in the whole object: 10752 of 10752. The shape is not a picture drawn
by isolating sixteen pieces. It is the distance the object already had.

## What is automatic and what is not

Two of the three rows are forced and are stated here as forced, not sold as
findings.

A pair joined in the shape is joined in the object, because it is the same
relation restricted; so one step agrees by construction. A pair two steps
apart in the shape has a piece of the carrier joined to both, so the object
cannot need more than two, and it cannot need fewer, because a pair not joined
in the shape is not joined in the object either; so two steps agrees by
construction as well.

Three steps is the row with content. Here the object is free to be shorter
than the shape, by routing through a piece the carrier does not contain, and
nothing forbids it. There are 2496 such pairs, and the object
takes the shortcut in none of them.

| pairs inside a carrier | count | forced? |
| --- | --- | --- |
| at one, two or three steps in the shape, same in the object | 10752 of 10752 | rows one and two only |
| of those, at three steps | 2496 | no |
| far corners of a four-cube, four steps in the shape | 480 | folds to three |

The last row is the single place a carrier bends, and it bends for a stated
reason rather than an interesting one: nothing in the whole object stands more
than three steps from anything else, so the eight far corners of each
four-cube have nowhere to be. All 480 of them sit at three steps and 0 at
four. A four-cube carrier is therefore isometric in its first three rows and
folded at its antipode, which is the most any sixteen pieces could be.

For the 72 carriers made of two three-cubes, the two cubes are not held apart
in the object. Of the pairs taken across them, 4032 stand two steps apart and
576 stand three; the cubes interleave rather than separate.

## The control, and the negative that matters

Sixteen pieces taken evenly spaced through the table's own ordering, in four
spacings, give 768 control sets. In 730 of the 768 a pair is brought closer by
a piece outside the set. Carriers of the charge do this in 0 pairs of the
10752. Being isometrically placed is not what sixteen pieces do; it is what
carrying the charge makes them do.

That reading survives only because the surrounding object is uneven, and the
runner measures the unevenness rather than assuming it. Count, for a pair of
pieces, how many pieces are joined to both. If the object were evenly built
that count would depend on the number of steps and nothing else. It does not:
the counts take 9 shapes at one step and 10 at three. So the four-cube inside
a carrier is not a fragment of a homogeneous surround that any sixteen pieces
would inherit. It is produced by carrying the charge.

The same unevenness bounds the preceding cycle's other result. Inside a
carrier, the number of cuttings a pair shares settles how many steps apart the
pair is. Across the whole object that fails: of the 47 counts that occur, 44
settle the step and three do not, at 202, 212 and 250, on 1632 pairs. The
count-to-distance law is a property of a carrier, not of the system, and this
note does not extend it.

## Boundary and honest read

The one-step and two-step agreements are consequences of restricting a
relation and are labelled as such in the runner's own gate. Anyone reading
10752 of 10752 as one measurement is reading it wrong; the measurement is
2496.

The far-corner fold is likewise forced by the object having no fourth step. It
is reported because leaving it out would make the isometry look total when it
is not.

The relabelling search that fits a carrier's joins onto a four-cube reads the
0/1 join table alone and never how many cuttings a pair shares, and it is
given a four-cube with two joins moved that keeps every corner at 4 joins,
which it refuses. Nothing in the distance result can have been arranged by the
search.

A control is not a proof of rarity. That 730 of 768 evenly spaced sets are
shortened from outside is evidence that isometric placement tracks the charge;
it is not a theorem that no other sixteen pieces can be placed isometrically.

Nothing here shows that a carrier of some other charge must behave this way,
and nothing here derives the shape from the 384 symmetries; the shapes are
measured on all 132 carriers, one at a time.

Nothing here moves the bracket on an eighteen-piece carrier of the flip
partner of four, and nothing here bears on the axioms, on Admissibility, or on
any primitive.
