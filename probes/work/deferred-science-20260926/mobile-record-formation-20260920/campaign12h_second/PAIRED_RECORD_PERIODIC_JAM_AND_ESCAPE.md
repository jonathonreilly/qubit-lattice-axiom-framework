# A periodic paired-record jam and a local immutable escape

Status: author conditional construction and counterexample, 2026-09-21.
This supplements PAIRED_RECORD_FORMATION_AND_DIMER_GAUSS.md without changing
its frozen process. No continuum phase, general accessibility theorem, or
wave result is claimed. The extension below is an additional supplied
transition rule, not an inferred axiom or a silent alteration of a test.

## An exact periodic absorbing state of the original process

Tile Z^3 by cubes 2z+{0,1}^3. In each cube leave corners 000 and 111 empty
and place the three dimers

    100--110 (y),   010--011 (z),   001--101 (x).              (1)

At the lower coordinate end of each edge the record content points along
its positive coordinate direction; the other record has opposite content.
This is a reciprocal matching with density 3/4, and applies on every even
periodic side N>=4. Vacancies occur exactly when all three coordinate
parities agree. Records of all six direction contents occur equally often.

The original generator has no exit from this configuration:

1. No two vacancies are nearest neighbors, so no paired birth is enabled.
2. A dimer translated along its own axis lies on a line where the other
   two coordinate parities differ. No site on that line is vacant, so
   either axial translation is blocked.
3. A transverse rigid dimer translation needs two adjacent vacant target
   sites, which do not exist.
4. Every unit cube contains all eight coordinate-parity triples, including
   the two vacancy triples. No cube is fully occupied, so the original
   full-cube exchange is disabled.

These four points exhaust exactly the stated event families. This is a
support-specific counterexample, not an exclusion of collective motion or
of all immutable-record processes. On a finite even torus it is reachable
from empty with positive probability: successively create precisely the
3N^3/8 prescribed dimers before any other effective event. Every required
birth stays enabled until it is made and has positive rate; total rates are
finite. Therefore the original finite-torus process does not fill almost
surely from empty for positive finite beta,kappa,nu. The argument gives no
useful thermodynamic lower bound on that exceptional history's probability
and says nothing about typical macroscopic densities.

The period-two state itself breaks translations and cubic rotations. A
uniform mixture over its finite translation/proper-rotation orbit is an
invariant, translation- and proper-cubic-symmetric absorbing law of the
same process. An invariant mixture is not a formation limit or an ergodic
phase, and this mixture retains long-range periodic order.

## Why a reflecting cube cannot solve its own three-orientation cage

On a reflecting unit cube with three dimers, one in each coordinate
direction, consider the cut into its two coordinate-i faces. Exactly one
dimer crosses that cut. Thus each face has an odd number of occupied
vertices: paired vertices within a face contribute two and the crossing
dimer contributes one. Since a face has four vertices, it has an odd
number of vacancies. There are only two vacancies total, so each face
has exactly one. Applying this to all three cuts places the vacancies at
opposite corners.

Consequently any rearrangement confined to that cube that preserves the
three direction counts leaves nonadjacent vacancies. No paired birth can
occur, even if many immutable records move collectively within the cube.
This explains why merely adding a richer local permutation family need
not repair the reflecting-cube absorption counterexample. The surrounding
lattice can change the relevant cuts and is the positive route below.

## A larger family of local parallel swaps

Add the following conservative channels, each with a supplied symmetric
rate mu>0. For each unit cube, choose an axis i and a nonempty subset of
its four edges parallel to i. Simultaneously swap the contents and identities
on those disjoint nearest-neighbor edges, including vacancies as empty
slots. Accept the event exactly when the resulting global configuration
still obeys the reciprocal matching relation. Events leaving all readable
contents unchanged can be retained as identity transport or omitted from
the projected content process; the acceptance condition is unchanged.

This is a finite list of 3(2^4-1)=45 attempted local involutions per cube.
The reciprocal condition can be checked on the changed sites and their
nearest neighbors. The event's support is the cube; its rate/acceptance
may read that bounded surrounding neighborhood. No record is created,
erased, or rotated. Every moved record takes one nearest-neighbor step.
The family is translation- and proper-cubic-covariant, and its inverse is
the same channel with the same rate. The former formation hazards are
unchanged. Rates and this larger move support are extra model choices.

## Four-record escape and renewed birth

In one cube of (1), simultaneously swap these three y-directed edges:

    000 <-> 010,   001 <-> 011,   101 <-> 111.                (2)

The y dimer 100--110 remains fixed. The z dimer 010--011 moves by -e_y
to 000--001. The x dimer 001--101 moves by +e_y to 011--111.
Two of the three swaps exchange a record with a vacancy; the remaining
swap exchanges two records. Exactly four records move, each one step,
with all original identities and contents preserved. The new vacancies
are 010 and 101, still opposite corners of this cube, as required by the
preceding cut argument.

But the neighboring period-two cube has a vacancy at 020. Therefore the
edge 010--020 is now empty at both ends and a paired birth at rate beta
is enabled. This is an explicit, entirely local escape from the periodic
jam followed by an occupancy increase. On N=4, for example, the record
count changes from 48 to 50 after the swap and birth. The original records
remain intact. For every even N>=4 the same local history works, with
coordinates interpreted periodically. The site 010, which formed a record
in the original construction, can form another after that record moves.

The extension remains reversible with respect to uniform matching laws
when births are off: each accepted involution pairs two states at equal
rate. The exact dimer Gauss identity remains true because every accepted
state is a matching. These facts do not establish irreducibility, eliminate
other jams, select a Coulomb state, or supply oscillatory waves. Those are
separate next questions. The result here is a concrete diagnosis of one
failed support and a demonstrated allowed local repair to that support.

## Verification target

A separate periodic checker constructs (1) on N=4,6,8, enumerates all
original births/translations/full-cube channels, and requires zero exits.
It implements (2) on actual tracked records, checks every displacement and
content, verifies the exact inverse, then executes the newly enabled birth.
It checks that the matching Gauss identity survives the history, including
periodic edges. A separate cube census checks the orientation-cut argument
against every matching with one dimer in each direction. These finite checks
support the general proofs above; they do not replace a mixing or limit
argument. Independent checking remains pending.
