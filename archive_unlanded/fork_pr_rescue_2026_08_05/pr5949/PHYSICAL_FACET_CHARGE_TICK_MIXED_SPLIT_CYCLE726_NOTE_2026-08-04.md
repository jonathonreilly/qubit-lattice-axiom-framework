# The facet-visible charge of the four-box splits into a tick half and a mixed half: exactly additive at the ceiling, superadditive by one at the floor — Cycle 726

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle. Every
quantity below is an exact integer count over a finite, completely enumerated
configuration space. This note quotes no floating-point number and no fitted
constant; each integer it states is printed by the paired runner in the run that
produced its `TOTAL` line.

The unit four-box carries eight three-dimensional facets. Two of them are the
equal-tick slices — the facets on which the tick coordinate is constant, so that
all three spatial directions survive. The other six each trade one spatial
direction for the tick. This cycle splits the facet-visible charge of a minimal
dissection accordingly, into a **tick half** `TC` carried by the two equal-tick
slices and a **mixed half** `MC` carried by the six tick-carrying facets, and
measures each half's bracket separately. The two halves behave differently at
their two ends. At the top they are exactly additive: a single dissection puts
both halves at their own ceilings at once, and that dissection is face-to-face.
At the bottom they are not: each half reaches its own floor alone, but the two
floors cannot be reached together, and the joint floor sits exactly one unit
above their sum. The obstruction is supplied solver-free by one carried integer
certificate at denominator `2`, and the value `85` it bounds is attained by an
explicit witness, so the floor is exact rather than bracketed.

## Setup

The unit four-box has `16` corners, indexed by the big-endian bit map
`COR[k][j] = (k >> (3 - j)) & 1`. Coordinates `0`, `1`, `2` are the spatial
directions; coordinate `3` is the tick. A **cell** is a five-element subset of
the corners, and the census of all such subsets by normalized volume is
`[(0, 1360), (1, 2672), (2, 320), (3, 16)]`. The `2672` cells of normalized
volume `1` are the minimal cells, and a **minimal dissection** of the box is a
selection of `24` of them that are pairwise interior-disjoint and together cover
the box. Since each has volume `1/24` and the box has volume `1`, twenty-four
pairwise-disjoint minimal cells necessarily tile: disjointness plus the volume
count is a complete proof of covering, with no solver and no sample points
involved in the argument.

Three integer charges are defined per cell.

- The **box charge** `BX` counts the cell's vertex pairs whose spatial `L1`
  separation exceeds `1`. Its per-cell range over the minimal cells is `(3, 7)`.
- The **facet-visible charge** `FC` is summed over the cell's four-vertex facet
  slices. Each such slice lies in one facet; within that facet the charge counts
  the slice's vertex pairs separated by more than `1` in that facet's own cost
  axes, which are the spatial directions the facet keeps. Its per-cell range is
  `(0, 7)`.
- `FC` splits as `FC = TC + MC`, where `TC` collects the contributions of the two
  equal-tick slices and `MC` the contributions of the six tick-carrying facets.
  The per-cell ranges are `(0, 4)` for the tick half and `(0, 4)` for the mixed
  half.

Two structural facts make the facet split well posed.

**Every facet is a unit three-cube in its keep coordinates.** Because `COR` is a
big-endian bit map, deleting coordinate `i` and keeping the remaining three in
order makes the facet's corners, sorted by global corner index, coincide exactly
with the standard three-cube indices `0` through `7`. All eight facets therefore
share one and the same combinatorial dissection problem; only the cost map
differs between them. The runner gates this identity rather than assuming it.

**Every facet slice of a minimal cell is itself minimal.** Across the `2672`
minimal cells there are `3584` four-vertex facet slices, and the count of those
whose induced three-dimensional normalized volume exceeds `1` is `0`. A minimal
dissection of the box therefore induces a *minimal* dissection of each facet, and
the sum of `FC` over the twenty-four selected cells equals the sum over the eight
facets of that facet's own induced dissection cost. This identity is what lets a
four-dimensional quantity be bracketed facet by facet.

Containment is tested against fixed integer sample families with the genericity
requirement gated explicitly: the box family has `2672` points with `0` boundary
incidences over all `2672` minimal cells, and the facet family has `58` points
with `0` boundary hits over the three-cube's `58` non-degenerate cells, whose
volume spectrum is `[(0, 12), (1, 56), (2, 2)]`. A point family that touched any
cell boundary would make the cover test unsound; the gate is what rules that out.

## Claims

### One dissection set, eight facets, two cost laws

The four-box has `24` two-dimensional squares and `8` facets, with `6` squares in
each facet and each square lying in exactly `2` facets. Each facet admits `180`
minimal dissections into `6` unit tetrahedra. These `180` are found by
point-cover enumeration and then each one is independently certified genuine by a
separating-axis disjointness test: `180` of `180` are certified, so no assembly in
the enumeration is an artifact of the sampling.

Under the two cost maps the same `180` dissections spread differently:

- On each equal-tick facet the cost spectrum is `{18: 16, 19: 72, 20: 84, 21: 8}`.
  Both equal-tick facets give the identical spectrum.
- On each tick-carrying facet the cost spectrum is `{8: 12, 9: 64, 10: 104}`. All
  six give the identical spectrum.

### The facet-wise bracket, and its ceiling is attained

Summing the per-facet extremes gives `2 x [18, 21]` plus `6 x [8, 10]`, that is a
facet-wise bracket of `[84, 102]` for the total facet-visible charge of any
minimal dissection.

The upper end is attained exactly. The witness `W4` is a genuine minimal
dissection with tick half `42 = 2 x 21` and mixed half `60 = 6 x 10`
simultaneously, total `102`, box charge `128`. Its facet matching is complete —
`84` distinct facets with `0` unmatched — so the ceiling is reached not merely by
a dissection but by a face-to-face triangulation. **At the top the two halves are
exactly additive: nothing prevents both from being maximal at once.**

### At the floor the two halves are superadditive by exactly one

Each half reaches its own floor alone. The witness `W5` is a genuine dissection
with tick half `36 = 2 x 18`, the tick floor, paired with mixed half `55`. The
witness `W6` is a genuine dissection with mixed half `48 = 6 x 8`, the mixed
floor, paired with tick half `41`. So neither `36` nor `48` is individually out
of reach.

Their sum `84` is nevertheless not attained. The runner carries an integer
certificate at denominator `2`: a weight vector on the box sample family with
support `411`, weight sum `170`, values ranging over `(-22, 18)`, and least slack
`0` against twice the per-cell facet charge. Because every sample point lies in
the interior of exactly one cell of any dissection, summing the certificate over
a dissection's twenty-four cells gives twice the total facet charge on one side
and the full weight sum `170` on the other, so every minimal dissection has total
facet charge at least `85`. The witness `W1` is a genuine dissection with total
`85`. **The joint floor is therefore exactly `85`, one unit above the facet-wise
floor `84`.**

In the attaining witness `W1` the mixed half sits at its own floor `48` while the
tick half sits one above its own floor, at `37`. Which of the two halves carries
the extra unit is a property of this witness; the cycle gates that the unit must
be paid somewhere, not that every configuration attaining `85` pays it on the
same half.

### The square-diagonal pattern law is specific to the equal-tick facets

Each facet's dissection induces one diagonal on each of its `6` squares, giving a
six-bit pattern. Of the `64` patterns, `58` are realizable by some dissection; the
`6` that are not all carry exactly `3` set bits.

On an equal-tick facet the cost is a *function* of that pattern: the number of
patterns carrying two distinct charges is `0`, and the charge parity class is the
single value `[0]`. On a tick-carrying facet neither survives: `36` patterns carry
two distinct charges, and the parity class is `[0, 1]`.

The mechanism is visible in the construction. An equal-tick facet keeps all three
spatial directions, so every pair the pattern distinguishes is also a pair the
cost weighs. A tick-carrying facet trades one spatial direction for the tick, so
its third kept direction still enters the diagonal pattern but contributes
nothing to the cost, and patterns collapse onto each other unevenly. Read as
physics, the pattern-to-charge law is a law of the three spatial directions:
substituting the tick for a spatial axis breaks it. The tick is not a fourth
spatial direction wearing a different label, and this cycle measures the
difference as an integer rather than asserting it.

### A three-tier ladder in the minimum facet-visible charge

The minimum total facet-visible charge over twenty-four-cell minimal
configurations rises as structural restrictions are added, strictly at the first
step.

| configuration class | minimum facet-visible charge |
|---|---|
| all minimal dissections | `85`, exact — certificate plus attaining witness `W1` |
| square-consistent configurations | at least `86` — complete sweep of the `24` square diagonals |
| face-to-face triangulations | in `[86, 88]`, with `88` attained by witness `W3` |

The second row is a lower bound, not a value: it is what the sweep certifies
about any square-consistent configuration, and this cycle does not exhibit a
configuration attaining it.

The middle row is a complete sweep: for each of the assignments of one diagonal to
each of the `24` squares, each facet's cheapest dissection realizing its induced
pattern is taken and the eight are summed; the least value over all assignments is
`86`. Any configuration whose eight induced facet dissections agree on shared
squares is bounded below by that number. The bottom row's lower end inherits `86`,
because a face-to-face triangulation necessarily agrees on every shared square,
and its upper end is the genuine face-to-face witness `W3` at `88`, box charge
`110`. Pinning the face-to-face floor to a single value is left open here; the
bracket is what this cycle's solver-free machinery establishes.

**Corollary, airtight and solver-free: `85 < 86`, so every configuration attaining
the facet-charge floor `85` fails square consistency, and a fortiori is not
face-to-face.** The structure is visible directly in `W1`: it uses `100` distinct
tetrahedral facets with `32` of them unmatched, where a face-to-face selection
uses exactly `84` with `0` unmatched. Non-face-to-face structure is not an
accident of the search — it is forced at the bottom of the ladder.

### The face-to-face restriction does not move the box-charge endpoints

The face-to-face witnesses sit at box charges already reached by unrestricted
dissections: `W2` at `108` and `W4` at `128`. Requiring face-to-face gluing
therefore raises the facet-sum floor, from `85` to at least `86`, while leaving
these two adjacency-charge endpoints where they were. This is reported as an
honest negative: the two charges respond differently to the same restriction, and
a reader hoping the face-to-face condition would tighten the adjacency bracket
should not read that into this cycle.

The two charges are independent in the other direction as well. `W1` and `W2`
both sit at box charge `108` yet carry facet charges `85` and `96`; `W3`, `W5`
and `W6` all sit at box charge `110` yet carry facet charges `88`, `91` and `89`.
The adjacency charge does not determine the facet-visible charge.

### The canonical stencil orbit is extremal in both halves at once

The twenty-four monotone-path simplices — one per permutation of the four
coordinates, generated inside the runner from the permutations rather than
carried as a literal — form witness `W2`. Its two halves are **simultaneously at
opposite extremes**: tick half `36 = 2 x 18`, the tick floor, and mixed half
`60 = 6 x 10`, the mixed ceiling, for a total of `96` at box charge `108`.

The canonical assembly thus hides as much charge as it can from the two
equal-tick slices while exposing as much as it can to the six tick-carrying
facets. The pairing is not forced by either half alone: `W5` also attains tick
`36`, and pairs it with mixed `55` rather than `60`. Both halves of the statement
are gated separately for this reason.

## Derivation sketch

The chain has four links, and only the third carries a certificate.

1. **Reduce four dimensions to eight three-dimensional problems.** Facet-slice
   minimality makes the total facet charge of a dissection equal to the sum of
   eight induced facet-dissection costs, and the local-index identity makes those
   eight problems combinatorially identical. Enumerating `180` dissections once,
   then applying two cost maps, replaces a search over twenty-four-cell selections
   with a per-facet spectrum.
2. **Bracket facet-wise.** The per-facet spectra give `[84, 102]` immediately. The
   ceiling `102` needs only a witness, because a facet-wise sum of maxima is
   attainable as soon as one configuration realizes every maximum at once, and
   `W4` does.
3. **Close the gap at the floor.** The facet-wise floor `84` is not a valid floor
   for the joint problem, because the eight facets are induced by one shared
   selection of cells and cannot be varied independently. The certificate supplies
   the missing unit: it is a weight on sample points, so its sum over a dissection
   is the full weight sum regardless of which dissection is chosen, and its slack
   condition holds cell by cell. The bound `85` follows by summation alone; no
   solver is present in the runner or in this argument, and the witness `W1`
   meets the bound from above.
4. **Add structure and re-measure.** Square consistency is a finite condition on
   `24` bits, so its floor is obtained by complete sweep. Face-to-face implies
   square consistency, giving the lower end of the third tier; the witness `W3`
   gives the upper end.

The split itself needs no new machinery: `TC` and `MC` are the same facet-slice
sum restricted to the two families of facets, so every gate that holds for the
total holds for the halves by construction. What is not automatic, and is the
result of this cycle, is that the two halves are additive at one end and not at
the other.

## Honest boundary

- The square-consistent value `86` is a lower bound obtained by relaxing each
  facet independently to its cheapest dissection realizing the assigned pattern.
  Whether any square-consistent twenty-four-cell configuration actually attains
  `86` is not settled here, and the middle tier of the ladder is stated
  accordingly.
- The face-to-face floor is stated as the bracket `[86, 88]`, not as a value. The
  upper end is a genuine witness and the lower end is inherited from the
  square-consistent sweep; a solver-free certificate matching `88` is not carried
  here.
- Which half pays the extra unit at the joint floor `85` is a property of the
  attaining witness `W1`, not a gated law. The cycle gates that `84` is
  unattainable and `85` is attained.
- The certificate is carried at denominator `2`. No claim is made that `2` is the
  smallest denominator at which a valid certificate exists; that question is not
  addressed.
- The box-charge values `108`, `110` and `128` reported here are measurements of
  the six witnesses, not a re-derivation of any adjacency bracket. Whether `108`
  is the adjacency floor is outside this cycle.
- The genericity of both sample families is gated, and both bounds depend on it.
  A family with a boundary incidence would invalidate the cover test and with it
  the certificate argument; the gate is reported as `0` hits in both cases rather
  than assumed.
- The equality between the per-cell facet-charge sum and the facet-wise sum is
  verified independently for all six witnesses by two computations that share no
  code path: one summing `FC` cell by cell from the four-dimensional geometry, the
  other identifying each of the eight induced facet dissections inside the
  separately enumerated `180` and summing that facet's own cost table. The
  agreement holds for the three witnesses that are not face-to-face as well.
- All integer counts here are measured, not derived. The cycle establishes exact
  brackets on a finite configuration space; it selects no coupling, sets no scale,
  and proposes no new admitted structure.

## The next paths opened

- The face-to-face bracket `[86, 88]` invites a solver-free certificate for its
  lower end. The square-consistent sweep already produces per-square structure;
  strengthening it with the facet-matching count is the natural next attempt.
- The pattern-to-charge law holds on the equal-tick facets and fails on the
  tick-carrying ones by a measured `36` patterns. Classifying *which* `36`, and
  whether they share a corner-incidence profile, would turn a count into a rule.
- The stencil orbit's double extremality suggests looking for the smallest
  sub-block on which the tick floor and mixed ceiling still coincide, which is the
  natural sequel to this cycle.
- The `6` unrealizable patterns all carry exactly `3` set bits. A direct
  characterization of the obstruction would sharpen the sweep in the middle tier
  of the ladder from a `2^24` enumeration to a structural argument.

## Runner

- Runner: `scripts/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.py`
- Cold output: `outputs/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04_cold_2026-08-04.txt`
- Receipt: `outputs/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04_receipt_2026-08-04.json`

The runner executes every gated row above and reports

```
TOTAL: PASS=28 FAIL=0
```

with exit code `0`. The runner contains no solver: every bound is either a
complete enumeration, a witness, or a summation against the carried certificate.
Two consecutive runs produce byte-identical standard output; the cold output is
that output verbatim, and the receipt transcribes the same gate lines into a
keyed form. Neither carries a timestamp, a wall clock, a host name, or an
absolute path, so both are comparable across machines.

Every integer quoted in this note is the runner's own count in the run that
produced that `TOTAL` line; none is copied from an earlier probe.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)

Backticked context only, with no authority edge — both are in flight and neither
is cited as an authority for any statement above:
`PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md`,
`PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md`.
