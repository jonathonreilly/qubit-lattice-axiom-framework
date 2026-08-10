# Every incidence orbit is individually maximal, so the 39 is pure cancellation, and it is born on pairs — Cycle 766

Date: 2026-08-09

Authority: none

Audit: unset.

Status: derived location of the missing rank on the sub-sum lattice, with the non-monotonicity measured and one exchange to the ceiling

Claim type: bounded_theorem

Runner:

- [`physical_cell_cutting_incidence_cancellation_cycle766_2026_08_09.py`](../scripts/physical_cell_cutting_incidence_cancellation_cycle766_2026_08_09.py)

Axioms:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## What this responds to

Cycle 764 derived a ceiling of 144 on the rank of any table covariant under the
cell's own symmetry and a floor of 48 on its blind space, and showed the ceiling
attained. Cycle 765 reduced any such table to a list of twenty small matrices and
named the missing 39 as eight per-part rank drops. Both cycles could say how much
rank is missing and on which parts, but neither could say *where in the cover
table's own construction* the loss happens.

The cover table is the sum of 4 whole cell orbits. That makes the question finite
and sharp: is each of those four orbits already deficient, or are they
individually maximal and the deficiency created only when they are added? This
cycle answers it, then locates the loss on the lattice of sub-sums, and measures
how far the cover table sits from the ceiling in its own one-exchange
neighbourhood.

## The object

The unit four-cube on sixteen corners, cut into least-volume pieces at the
adjacency-cost floor: 2672 candidate pieces of determinant one, 400 of them at
cost floor 6, 15800 cuttings of 24 pieces, 192 pieces actually used and 192
eight-piece covers.

The symmetry permutes the four coordinates and flips any of them: 384 maps,
closed over all 147456 products, acting transitively on the 192 pieces and on the
192 covers. It has 104 orbits on ordered pairs of pieces, 120 on ordered pairs of
covers and 96 on the cells of the cover-by-piece square. By exact rational
arithmetic the cutting table has rank 88 with kernel 104, and the cover table has
rank 105 with kernel 87.

The reduction kept from cycle 765: a covariant table acts on part `i` as one
`mc_i` by `m_i` matrix tensored with an identity, so its rank is
`sum_i d_i rank(beta_i)`; the coefficient map from the 96 cell orbits to the
twenty small matrices is one-to-one and onto (stacked width 96, rank 96). Five of
the twenty parts carry no matrix at all, so 15 parts are active.

## The four incidence orbits are each at the ceiling

Each of the 4 cell orbits summing to the cover table has, on its own, exact
rational rank 144 — the derived ceiling — and its modular rank agrees. Read part
by part, all 60 single-orbit small matrices meet their own allowance
`min(m, mc)`, with 0 short.

This settles the dichotomy the cycle opened with, and it settles it the strong
way. **No incidence orbit is deficient anywhere.** Every one of the eight rank
drops that make up the 39 is therefore pure cancellation: rank that each summand
has and that the sum destroys. The 39 is not a property of any single orbit; it
exists only in the addition.

## Where the loss is born: the sub-sum lattice

All 15 non-empty sub-sums of the four incidence orbits, by exact rational rank
(no modulus enters this block):

- singletons: 144, 144, 144, 144
- pairs: 72, 93, 117, 129, 144, 144
- triples: 114, 130, 142, 142
- all four: 105

Two facts here are new and neither was anticipated.

First, **the cancellation starts immediately**: one pair already drops to 72, half
the ceiling, while two other pairs are still at 144. The pair spectrum is wide,
so the four orbits are not interchangeable with respect to each other.

Second, **the quadruple sits below every triple**. The least triple is 114 and the
cover table's 105 is below it. Rank on this lattice is not monotone under adding
orbits, and the cover table is exactly where the non-monotonicity bites: the
fourth incidence orbit destroys rank that the first three already had. The 39
acquires a location, not just a size.

Part by part, every one of the 8 rank-losing parts first goes short on a **pair**,
never on a single orbit, with 0 at size one. So the loss is born at the smallest
size where cancellation is possible at all.

## Rank loss is not monotone, part by part either

The design for this cycle predicted that a part goes short on a proper sub-sum if
and only if it is one of the eight drop parts. That prediction is false, and the
runner reports the measurement rather than the prediction.

**3 further parts go short on a pair yet meet `min(m, mc)` on all four**, with
`d/m/mc` equal to 3/1/3, 4/2/1 and 8/4/2. These parts lose rank on a pair and get
it back when the remaining orbits are added. Their recovery is not inferred from
the drop bookkeeping; the second prime rebuilds their four-orbit matrices from
scratch and confirms that each meets its allowance there too.

So non-monotone behaviour is not a curiosity of the top of the lattice. It occurs
on individual parts, in both directions, and any account of the 39 that treats
rank as accumulating monotonically along a chain of orbits is wrong.

The whole level computation is reproduced at the second prime: 15 active parts
compared, 0 differ, 30 short sub-sums found at those sizes. The primes are
1000003 and 1000033.

## The cover table in its own neighbourhood

Replace one of the four incidence orbits by any other cell orbit: 368
substitutions. By the small-matrix reduction their values run from 72 to 144,
with 53 at the ceiling, 1 equal to 105, and 9 lower. So of the 368 one-exchange
neighbours, 53 are already maximal and just 9 are worse than the cover table
itself: the cover table sits near the bottom of its own neighbourhood.

A named exact witness: **slot 0 taking orbit 5** lifts the exact rational rank of
the four-orbit table from 105 to 144. That substitution was found by search over
the neighbourhood, not assumed, and both its rank and the unswapped table's 105
are confirmed by exact rational arithmetic.

Adding rather than exchanging does the same thing: the five-orbit table formed by
the four incidence orbits together with that same orbit has exact rank 144. One
extra orbit is enough to reach the ceiling from 105.

## The two blind spaces barely overlap

The cover table's blind space has dimension 87; a table at the ceiling has blind
space of dimension 48, the floor. Exactly, by stacking the two tables and taking
one rational rank:

- they meet in dimension 12,
- they span 123 together,
- the smaller does **not** sit inside the larger.

Two independent routes to the intersection agree. So the 39 of extra blindness is
not a matter of the cover table being blind to everything a maximal table is
blind to plus a little more. The two blind spaces are largely transverse: the
cover table sees things a ceiling table misses, and is blind to a great deal that
a ceiling table sees.

## A corollary that is not gated

The width-96, rank-96 isomorphism of cycle 765 gives one further exact integer
per part for free. Fix a part `i` and a non-zero vector `v` in `C^{m_i}`. The map
sending a table's coefficient vector to `beta_i v` is onto `C^{mc_i}`, because the
coefficient map is onto the full matrix space. Hence the covariant tables blind to
`v` on part `i` form a subspace of codimension exactly `mc_i` inside the 96
available coefficients.

This is stated as a corollary and deliberately not gated in the runner: it follows
from an isomorphism the runner already establishes, so a gate for it would hold by
construction and would be evidence of nothing.

## Runner

`physical_cell_cutting_incidence_cancellation_cycle766_2026_08_09.py`, 46 gates,
0 failures, 5512 characters of output, 174 seconds of wall time and 156 MB peak
resident memory. Every number above is printed by a gate of that run. Group
construction, orbit decomposition, the central decomposition into twenty parts,
the ceiling and floor, and the small-matrix reduction are the kept prefix from
cycles 763 to 765 and are re-derived from the pieces on every run, not read from a
file. The sub-sum lattice, the per-part levels, the neighbourhood scan and the
blind-space comparison are this cycle's work.

## Boundary

- The sub-sum lattice of 15 exact rational ranks carries no modulus. The pair,
  triple and quadruple values, the singleton value 144, the witness rank 144, the
  five-orbit rank 144, and the intersection dimension 12 are all exact.
- The per-part levels and the neighbourhood values are modular ranks, and a
  modular rank can only fall. So a measured level is a lower bound on the true
  level, the count of 53 neighbours at the ceiling is a lower bound, and the
  counts of 1 equal to 105 and 9 below it are upper bounds. The second prime
  agreeing on all 15
  active parts is an independent-construction control, not a proof.
- That a table at rank 144 has every part at its own allowance is forced
  arithmetic once the ceiling theorem is in hand, not evidence. It is used here
  only as a consistency check on the witness.
- The three non-monotone parts are reported exactly as measured, against the
  cycle's own prior expectation.
- Nothing here says which geometric feature distinguishes the incidence orbits
  from the orbit that repairs them. That stratification of the 96 cell orbits, and
  the question of which pairs are responsible for the deficiency, are the next
  units and are named here so the boundary is honest about what was left.
- The symmetry used throughout is the full symmetry of the four-cube, which
  permutes the four coordinates and flips any of them. It is larger than the
  proper cubic rotations the admissibility axiom names, so none of this is a
  statement about that axiom's own covariance. It is a statement about a finite
  combinatorial object the axiom's adjacency rule picks out.
- No axiom, primitive, registry entry, effective status or framework claim changes
  here. This is finite exact linear algebra on a fixed finite object.
