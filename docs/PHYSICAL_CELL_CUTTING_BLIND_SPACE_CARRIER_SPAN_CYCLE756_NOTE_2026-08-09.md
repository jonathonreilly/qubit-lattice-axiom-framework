# The space the cuttings cannot see is the span of the differences of their eight-piece exact covers — Cycle 756

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the least-volume pieces, the cuttings at the adjacency cost floor,
the piece sharing table, the eight-piece carriers, the span of their
differences and a complete sweep of the small supports a blind weighting could
have, gating each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## What this answers

The object is the unit four-cube on sixteen corners, cut into least-volume
pieces at the adjacency cost floor. There are 15800 such cuttings. Between
them they draw on 192 pieces, 24 pieces to a cutting, and each piece lies on
1975 of the cuttings. Write the incidence table of that system: 15800 rows,
one per cutting, 192 columns, one per piece, a one where the cutting uses the
piece. Call a weighting of the 192 pieces blind when this table sends it to
zero, so that every one of the 15800 cuttings, totalled piece by piece against
the weighting, comes out zero.

The preceding cycle measured the rank of the table as 88, so the blind space
has dimension 104 and the two add back to 192, and then asked whether the
group of 384 symmetries fixes 88 on its own. It does not: the seen and the
blind space share same-type parts, so the trace counts of the group are too
coarse to pick the blind space out. That cycle left the rank as a
measurement and named the next place to look — the structure of the incidence
map itself rather than the trace counts of the group.

This cycle looks there, and finds the whole blind space sitting inside a
family of objects the incidence table names by itself.

## The result

There are exactly 192 sets of eight pieces that no cutting uses twice. Each
one of them meets every single one of the 15800 cuttings exactly once: each is
an exact cover of the cutting system. Call them carriers. Two immediate
consequences.

**Every carrier difference is blind.** If two carriers both send every cutting
to one, their difference sends every cutting to zero. So the differences of
the 192 carriers all lie in the blind space, and nothing about symmetry is
used to say so.

**Those differences are the whole blind space, and this is exact.** The 192
carriers, as weightings of the 192 pieces, span 105 dimensions. Their
differences therefore span 104, one fewer, because no carrier lies in the span
of the differences — a carrier sends every cutting to one, a difference sends
every cutting to zero. And 104 is the dimension of the blind space. So the two
coincide:

> the space the cuttings cannot see is exactly the span of the differences of
> the eight-piece exact covers of the cutting system, and the rank 88 is the
> 192 coordinates less those 104.

## The two-sided count that makes it exact

The two numbers 105 and 88 are each measured in a bounded arithmetic, and a
bounded rank is never larger than the exact rank. That inequality points the
same way both times, which is what makes the argument close without any exact
rational elimination at all:

- the table has bounded rank 88, so its exact rank is at least 88, so the
  blind space has dimension **at most** 104;
- the carriers have bounded rank 105, so their exact rank is at least 105, so
  their differences span **at least** 104 dimensions, all of them blind.

At most 104 and at least 104 leaves exactly 104, and forces both bounded ranks
to have been exact. Two different bounded arithmetics are run and agree on
both numbers, which a wrong elimination would not give. Nothing here is a
floating-point rank, a threshold on a small number, or a comparison against a
value carried in from the preceding cycle: 88 and 104 are re-measured from the
rebuilt object and then pinned by the inequality.

## No one class of exchange is the source

Two carriers share 0, 1, 2 or 4 pieces, never 3. Over all 18336 pairs the
counts are 15072, 1920, 960 and 384. The difference of a pair sharing k pieces
is supported on 16, 14, 12 and 8 pieces respectively, so the 384 pairs sharing
4 pieces give the shortest differences — the least exchanges, four pieces
traded for four.

Each of the four sharing classes, taken alone, already spans all 104
dimensions. So there is no privileged class of exchange generating the space
and no residue left to the others: the least exchanges alone suffice, and so
do the widest. This is the sharpest form of the previous cycle's negative
result. That cycle measured a single orbit of least exchanges falling short of the
whole blind space, and was careful to make no class-level claim. The
class-level truth is that the class of least exchanges spans everything; what
fell short was one orbit inside it.

## The smallest blind support has exactly the size of a carrier

Every cutting meets the support of a blind weighting in 0 or in at least 2
pieces — a cutting meeting the support once could not cancel. That is a
necessary condition and not a sufficient one, and necessity is the direction
the sweep needs: a support failing it carries no blind weighting. So for a
blind weighting supported on a set S, every piece p in S must have all 1975 of
its cuttings met by the other members of S. That is a covering condition, and
it can be pushed hard.

**Sizes 2, 3 and 4 are impossible.** For each of the four kinds of piece, the
1975 cuttings through a piece are not covered by any 2 other pieces, nor by
any 3, and are covered by 4. Four is therefore the least number of partners a
member of a blind support can have, so a blind support holds at least 5
pieces.

**Sizes 5, 6 and 7 are impossible, by a complete sweep.** The 48 proper cube
symmetries carry the table to itself and leave four kinds of piece, 48 of each
kind, so every support of any size is the same, up to symmetry, as one holding
a fixed piece of one of those four kinds. Anchor on such a piece. Every valid
support contains a least cover of that piece's 1975 cuttings, and at these
sizes a least cover uses at most 6 other pieces, so enumerate all least
covers up to that size and extend each by every way of filling out to the
target size. That builds every candidate, without exception, and there are
3306820 of them across the four anchors and the three sizes. A necessary
count bound — the shares of a member with the rest must total at least 1975 —
cuts them to 27824, and each survivor is then tested against the full
condition at every one of its members. None passes.

**And 8 is reached.** The 384 least exchanges are blind and are supported on
exactly 8 pieces. So:

> no blind weighting of the cutting table touches fewer than 8 pieces, and 8
> is attained: the smallest blind support has exactly the size of a carrier.

The two results fit together. The blind space is generated by differences of
eight-piece exact covers, and 8 is the smallest support any blind weighting
can have. The exact covers are not one convenient family of generators among
many — they sit at the floor.

## What the runner gates

15 gates, `TOTAL: PASS=15 FAIL=0`, in under 900 s and under 2500 MB, with
output under 6000 characters. What is checked, and how:

- the cell complex, the pieces and the cuttings are rebuilt from scratch, and
  the two independent counts of the incidences are gated against each other;
- the 192 carriers are found as eight-piece sets no cutting uses twice, and
  then separately gated to meet every one of the 15800 cuttings exactly once,
  so the exact-cover property is measured and not assumed;
- both ranks are measured twice, in two different bounded arithmetics, and
  the gate requires the two to agree before the inequality argument is run;
- the criterion used throughout is gated to discriminate: all 384 least
  exchanges meet every cutting 0 or 2 times, while a carrier, which is not
  blind, meets every cutting exactly once, and the same test applied to the
  eight pieces of a carrier returns no;
- each of the 48 proper cube symmetries is gated to carry the table to itself
  by a piece relabelling paired with a cutting relabelling, which is what
  licenses anchoring the sweep on four pieces instead of 192;
- the sweep is gated on the count it built and the count that survived the
  necessary bound, both non-zero, so a sweep that silently built nothing
  cannot pass.

## Boundary and honest read

**Derived, and general.** That the difference of two exact covers is blind.
That a bounded rank is a floor for the exact rank, and hence that a floor on
the carrier rank and a floor on the table rank, pointing opposite ways, can
pin both. That every cutting meets the support of a blind weighting in 0 or at
least 2 pieces, so a support failing that carries no blind weighting — the
converse is neither claimed nor used. That every valid support contains a least
cover of any one of its members' cuttings, which is what makes the
cores-and-extensions sweep complete rather than merely large.

**Measured on this object, and not claimed beyond it.** The counts 15800,
192, 24 and 1975; the 192 carriers; the sharing profile 15072, 1920, 960, 384
over 18336 pairs; the ranks 105 and 88 and the blind dimension 104; the
four-kind orbit structure of the 48; the covering number 4 at each kind; the
3306820 candidates and the 27824 survivors; and the least blind support 8.

**What the sweep does and does not settle.** It settles that no blind
weighting has support smaller than 8. It does not settle which supports of
size 8 carry blind weightings beyond the 384 least exchanges — that would
need least covers of size 7, a sweep this runner does not attempt. So
"the smallest blind support is 8" is established; "every blind weighting of
support 8 is a least exchange" is not, and is not claimed here.

**What is still a measurement.** The rank 88 is now identified with a
structural quantity — the 192 coordinates less the span of the carrier
differences — rather than left as a bare elimination result. That is a
relocation of the question, not a derivation of the number: what remains open
is why the exact covers span 105 and not some other dimension. This cycle
moves the question from the rank of a 15800-by-192 table to the span of 192
explicitly named eight-piece sets, which is a far smaller and far more
structured object to reason about.

## Next

Three paths open. Ask whether every blind weighting of support 8 is a least
exchange, which needs the size-7 least covers the present sweep stops short
of, and which would say the least exchanges are the entire floor and not part
of it. Ask why the 192 carriers span 105 and not more — 105 is one more than 104, so
the carriers are as close to independent as an exact-cover family can be while
all sending every cutting to one, and the count of coordinates they leave
unspanned falls one short of the rank 88; that near-coincidence is worth a
cycle on its own.
And take the sharing profile 15072, 1920, 960, 384 as the next thing to
derive: it is the multiplication table of the carrier family, and a derivation
of it would carry the span with it.
