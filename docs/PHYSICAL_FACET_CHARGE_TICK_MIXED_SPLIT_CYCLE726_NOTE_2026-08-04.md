# In a supplied one-box corner-simplex model, the facet charge splits into tick and mixed halves — Cycle 726

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

## Supplied model and open physical bridges

This is a finite theorem of a **supplied structural model**, not a derivation of
that model from the framework axioms. The supplied domain is one unit box with
three spatial corner coordinates and one equal-grained tick corner coordinate;
a piece is the convex hull of five box corners; and a minimal dissection is made
of `24` normalized-volume-one pieces with disjoint interiors. The facet-visible
charge is also declared here: it counts selected vertex pairs under the spatial
`L1` rule defined below.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the spatial `Z^3`
nearest-neighbour grading and proper cubic rotations. The registered
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies only equal tick/edge graining. Neither selects corner simplices or
dissections, identifies all vertex pairs of a simplex with physical slot uses,
selects this charge as physical, nor supplies a tick--Admissibility realization
bridge. A nonsimplicial complex, non-corner pieces, coarser pieces, or a larger
multi-box domain is outside this theorem.

No coupling value, sign, or scale is selected or derived. Every theorem below
is an exact integer statement over the declared finite domain and is computed
or gated by the paired runner; the imported endpoint pair is read from the
pinned Cycle 725 receipt.

The supplied unit four-box carries eight three-dimensional facets. Two are the
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
explicit witness. These are finite facts about the declared model, not a
framework-wide physical cost law.

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
whose induced three-dimensional normalized volume differs from `1` is `0`. A minimal
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

Interior disjointness is decided by an integer separator sweep. For zero--one
vertices, relevant differences lie in the ternary cube. In four dimensions a
supporting normal may be chosen orthogonal to three independent ternary
differences, so its components are three-by-three ternary minors bounded in
absolute value by `4`; the runner sweeps the full `[-4,4]^4` range. The
three-dimensional checker uses the corresponding bounded cross-product range.
Non-strict separation is intentional: boundary contact is allowed while shared
interior is not.

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

The finite mechanism is visible in the declared charge construction. An equal-tick facet keeps all three
spatial directions, so every pair the pattern distinguishes is also a pair the
cost weighs. A tick-carrying facet trades one spatial direction for the tick, so
its third kept direction still enters the diagonal pattern but contributes
nothing to this declared cost, and patterns collapse onto each other unevenly.
Thus, in this one-box model, replacing one of the three charged spatial axes by
the uncharged tick coordinate destroys the six-bit-pattern functional relation.
This does not establish a general physical distinction between time and space.

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

**Finite corollary: `85 < 86`, so every declared-model configuration attaining
the facet-charge floor `85` fails square consistency, and a fortiori is not
face-to-face.** The structure is visible directly in `W1`: it uses `100` distinct
tetrahedral facets with `32` of them unmatched, where a face-to-face selection
uses exactly `84` with `0` unmatched. Non-face-to-face structure is not an
accident of the search — it is forced at the bottom of the ladder.

### The face-to-face restriction does not move the contained Cycle 725 box-charge endpoints

The paired runner reads and gates the contained Cycle 725 receipt, whose exact
minimal-piece box-charge bracket is `[108, 128]` in this same supplied model.
The face-to-face witnesses sit at both endpoints: `W2` at `108` and `W4` at
`128`. Requiring face-to-face gluing
therefore raises the facet-sum floor, from `85` to at least `86`, while leaving
these two adjacency-charge endpoints where they were. This is reported as an
honest negative: the two charges respond differently to the same restriction, and
a reader hoping the face-to-face condition would tighten the adjacency bracket
should not read that into this cycle.

The two charges are independent in the other direction as well. `W1` and `W2`
both sit at box charge `108` yet carry facet charges `85` and `96`; `W3`, `W5`
and `W6` all sit at box charge `110` yet carry facet charges `88`, `91` and `89`.
The supplied-model adjacency charge does not determine the supplied-model
facet-visible charge on these witness pairs.

### The monotone-path family is extremal in both halves at once

The twenty-four monotone-path simplices — one per permutation of the four
coordinates, generated inside the runner from the permutations rather than
carried as a literal — form witness `W2`. Its two halves are **simultaneously at
opposite extremes**: tick half `36 = 2 x 18`, the tick floor, and mixed half
`60 = 6 x 10`, the mixed ceiling, for a total of `96` at box charge `108`.

Within the supplied model, the monotone-path family hides as much charge as it can from the two
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

The split itself is definitional: `TC` and `MC` are the same facet-slice sum
restricted to the two families of facets. The endpoint relations are not
definitional; the runner gates them separately.

## Honest boundary

- The theorem's domain is supplied: one equal-grained tick-box, corner
  five-simplices, normalized-volume-one pieces, twenty-four-piece dissections,
  and the declared pair charge. The framework does not select this domain or
  require physical constructions to pay either charge.
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
- The witness box-charge values are recomputed here. The statement that `108`
  and `128` are the global minimal-piece endpoints is a direct dependency on
  the contained Cycle 725 receipt, which the runner reads and gates. Cycle 725
  has the same supplied-model and open-bridge boundary.
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
- The cycle establishes exact finite brackets in the supplied configuration
  space; it selects no coupling, sets no scale, and proposes no new primitive.
- Nothing is claimed for coarser or non-corner pieces, nonsimplicial complexes,
  more than one box or tick, other boundary conditions, a thermodynamic or
  continuum limit, curvature, a metric, an action, or a field equation.

## The next paths opened

- The face-to-face bracket `[86, 88]` invites a solver-free certificate for its
  lower end. The square-consistent sweep already produces per-square structure;
  strengthening it with the facet-matching count is the natural next attempt.
- The pattern-to-charge law holds on the equal-tick facets and fails on the
  tick-carrying ones by a measured `36` patterns. Classifying *which* `36`, and
  whether they share a corner-incidence profile, would turn a count into a rule.
- The monotone-path family's double extremality suggests looking for the smallest
  sub-block on which the tick floor and mixed ceiling still coincide, which is the
  natural sequel to this cycle.
- The `6` unrealizable patterns all carry exactly `3` set bits. A direct
  characterization of the obstruction would sharpen the sweep in the middle tier
  of the ladder from a `2^24` enumeration to a structural argument.

## Runner

- Runner: `scripts/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.py`
- Independent checker: `scripts/physical_facet_charge_tick_mixed_split_cycle726_independent_check_2026_08_04.py`
- Pinned cache: `logs/runner-cache/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.txt`
- Independent cache: `logs/runner-cache/physical_facet_charge_tick_mixed_split_cycle726_independent_check_2026_08_04.txt`
- Receipt: `outputs/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04_receipt_2026-08-04.json`

The runner executes every gated row above and reports

```
TOTAL: PASS=32 FAIL=0
```

with exit code `0`. Any failed gate exits nonzero. The primary runner contains
no solver: every bound is either a complete enumeration, a witness, or a
summation against the carried certificate. The cache binds the exact runner and
its declared Cycle 725 receipt input; the receipt is generated from the same
gate list emitted by the run.

The independent checker reports `TOTAL: PASS=8 FAIL=0`. It does not import or
execute the primary. It parses only the carried certificate/witness literals,
then independently checks the four-dimensional certificate by exact integer
barycentric numerators and enumerates the `180` facet triangulations as
compatibility six-cliques rather than by the primary's sample-cover recursion.

Every substantive count quoted in this note is computed or dependency-gated
in the run that produced that `TOTAL` line.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — supply only the spatial
  `Z^3` nearest-neighbour grading and proper cubic rotations.
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — supplies only equal tick/edge graining.
- [Cycle 725 exact adjacency bracket](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md)
  — landed but unaudited; supplies the `[108, 128]` minimal-piece box-charge
  bracket and the same explicit corner-simplex supplied-model boundary. The
  Cycle 726 runner pins its receipt as a declared input. The endpoint-comparison
  claim here remains conditional on that unaudited dependency.

Cycle 723 is provenance only and is not a scientific dependency: this runner
constructs the monotone-path family and recomputes all of its charges. Cycle
724 is superseded for the only imported comparison by Cycle 725. Cycle 873 is
unrelated ordering context.

## No-Go Discipline Gate

This packet covers only the negative-flavoured finite conclusions inside the
declared model: no charge-`84` minimal dissection; no square-consistent or
face-to-face charge-`85` configuration; no mixed-facet functional dependence
on the six-bit diagonal pattern; and no determination of facet charge by box
charge on the exhibited equal-box-charge witness pairs. It makes no physical,
all-model, multi-box, or continuum no-go claim.

**N1 — Alternative route enumeration.** The approach families are normalized
by mathematical object, mechanism, and terminal obligation.

1. `ATTEMPTED` — dual sample-weight route: all `2672` cell slacks are checked
   against a denominator-two weight vector of total `170`; nonnegative slack
   proves every declared minimal dissection has charge at least `85`.
2. `ATTEMPTED` — local primal construction route: every one-piece replacement
   of `W1` that would lower `85` to `84` is tested against the full exact
   cover-once incidence rows; none survives. This is a hostile control, while
   the dual certificate supplies the global proof.
3. `ATTEMPTED` — shared-square relaxation route: all `2^24` assignments of the
   box's square diagonals are swept, with the cheapest realizing facet
   dissection selected independently; the relaxed minimum is `86`, excluding
   square-consistent charge `85`.
4. `ATTEMPTED` — face-matching route: every witness's tetrahedral facets are
   counted exactly, and face-to-face implies shared-square consistency; hence
   the `86` relaxation excludes face-to-face charge `85` as well.
5. `ATTEMPTED` — complete facet-enumeration route: all `180` minimal cube
   dissections are reconstructed and separator-certified. On mixed facets,
   exactly `36` six-bit patterns carry two charges, directly refuting a
   pattern-only functional law there.
6. `ATTEMPTED` — explicit counter-witness route: `W1/W2` share box charge
   `108` but have facet charges `85/96`, while `W3/W5/W6` share box charge
   `110` but have facet charges `88/91/89`; box charge therefore does not fix
   facet charge even on these carried families.

**N2 — Open-condition independence.** These are walls only to a physical or
wider interpretation, not premises missing from the finite theorem.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| physical model selection / tick--Admissibility realization | no | no | yes |
| physical model selection / multi-box or multi-tick extension | no | no | yes |
| tick--Admissibility realization / multi-box or multi-tick extension | no | no | yes |

**N3 — Hidden-condition scan.** “Supplied model” is now explicit at the front
of the note and runner. “Registered” refers only to the kinetic-isotropy
primitive and is linked to its registry source; it grants equal graining, not
the model. “Monotone-path” names a generated finite family, not a canonical
physical selection. No “standard,” “natural,” “obvious,” background, or
framework-provides phrase supplies a proof step.

**N4 — Residual matching.** Cycle 725 is used only for the exact `[108,128]`
minimal-piece box-charge bracket in the identical supplied corner-simplex
domain; this matches. Its certificate and parity residuals are not imported.
The minimal axioms and kinetic-isotropy primitive are premise sources, not
no-go witnesses. Cycles 723, 724, and 873 supply no negative witness here.

**N5 — Rhetoric audit.** The primary cached stdout carries substantive
`per_element:`, `per_site:`, `per_mode:`, `per_block:`, and `lattice_wide:`
execution-certificate lines. Only per-element/per-site checks inside one
per-block finite box are executed. Per-mode and lattice-wide claims are
explicitly not executed and are not asserted.

**N6 — Partial-closure paths.** The legitimate present shape is explicit
supplied model, bounded theorem, and later import-retirement review. A retained
physical cell-selection theorem could retire the model-selection condition; a
retained tick-realization theorem could retire the tick condition; a separate
composition theorem could extend the domain. The approved kinetic-isotropy
primitive is not a wall and is not enlarged. None of these routes is called a
required new axiom.

**N7 — Steelman.** A hostile reader should reject any physical extrapolation:
coarser corner pieces already change the Cycle 725 floor, while non-corner,
nonsimplicial, multi-box, and alternative boundary constructions are not tested.
That concrete route can evade the numerical floors and must remain open. It does
not break the finite theorem, because those objects are outside its quantified
domain; it does break the submitted physical rhetoric, which has been removed.

**N8 — Cross-cycle echo.** The landed reviews of Cycles 724 and 725 found the
same overread: exact corner-simplex counts do not select the physical assembly
model. Both were repaired by declaring the supplied domain and open physical
bridges. Cycle 726 adopts that mechanism and binds Cycle 725 directly rather
than treating its result as in-flight context. Cycle 722 likewise separated a
finite monotone-path orbit fact from an axiomatic selection claim; this note
uses only a generated witness family.

Status: **PASS** for the finite negative scope above. The N5 lines land in the
primary cache with this packet.

## Review record

Review-loop iteration 1 (Codex, 2026-08-12) returned `FIX_THEN_PROCEED`. The
submitted note was demoted from physical four-box rhetoric to a theorem of the
supplied one-box corner-simplex model; the kinetic-isotropy premise and Cycle
725 dependency were made explicit; the mixed-pattern gate was strengthened
from “greater than zero” to exactly `36`; all six witness tuples were pinned;
the runner became fail-closed and input-bound; certificate and construction
hostile controls, a generated receipt, a pinned cache, and the N1--N8/N5 packet
were added. No audit verdict was applied.
