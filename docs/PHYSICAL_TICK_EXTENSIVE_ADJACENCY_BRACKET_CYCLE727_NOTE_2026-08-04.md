# Exact adjacency-cost bracket for dissections of a two-tick box

Status: unaudited source note. Cycle 727 of the emergent-geometry lane.

## What this settles

The LATTICE axiom of [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
supplies adjacency between nearest neighbours of `Z^3` and nothing else. Time is not an
axiom in this framework: the tick is the direction of monotone record accumulation, and
the axiom gives it no adjacency of its own. Cycle 725 measured the exact bracket
`[108, 128]` on the adjacency cost of a minimal-volume corner dissection of one lattice
cell carried through **one** tick, and its own boundary named the next question:

> The bracket is a statement about one lattice cell carried through one tick. Extending
> it to longer tick runs or larger spatial blocks is open work, not a corollary.

**This cycle answers the tick half of that question. Over every minimal-volume corner
dissection of one lattice cell carried through two ticks, the adjacency cost is exactly
`[216, 256]` — twice the one-tick bracket at both ends. Both ends carry an exact integer
certificate, and both are attained by a witness certified piece by piece.**

Extensivity in tick number was not a safe guess. Stacking two one-tick dissections always
gives a valid two-tick dissection, so the cost is subadditive and the floor could only
have come in at or below `216`; nothing forced it not to come in strictly below, and
nothing at all bounded the ceiling from above by `256` — a two-tick dissection is free to
use pieces that straddle the seam between the ticks, and 11936 of the 17280 minimal pieces
do exactly that. Both ends land on the doubled value anyway.

The doubling is measured on both sides. The runner computes `108` and `128` on the
one-tick box in the same execution and from the same code path, so neither half of the
comparison is a supplied number.

## Objects

- **The box.** One lattice cell carried through two ticks: `{0,1}^3` in space by three
  tick values, 24 corners, spatial volume 1 and tick extent 2, so volume 2. The one-tick
  box of cycle 725 is the same construction with 16 corners and volume 1.
- **Pieces.** A piece is a 5-subset of the corners. There are 42504 of them; their volume
  spectrum is `[(0, 13152), (1, 17280), (2, 9840), (3, 1472), (4, 680), (5, 64), (6, 16)]`
  in units of the simplex volume. The 17280 pieces of volume 1 are the **minimal** ones,
  against 2672 in the one-tick box. Minimal volume forces the piece count: a
  minimal-volume corner dissection of this box uses exactly 48 pieces, against 24 for one
  tick.
- **Adjacency cost.** For a piece, the number of vertex pairs whose **spatial** `L1`
  separation exceeds 1 — the pairs the piece is forced to join across a non-adjacency. The
  cost of a dissection is the sum over its pieces. This is the same charge cycle 725 used,
  carried over unchanged: the tick contributes nothing to it, because the axiom supplies
  spatial adjacency and the tick is emergent and unweighted.
- **Tick-span charge.** New at two ticks: the number of vertex pairs whose **tick**
  separation exceeds 1. It is identically zero on the one-tick box — verified here on all
  2672 minimal one-tick pieces — which makes it the first charge in this lane that only
  comes into existence once a second tick is available.

## Method: certificates and witnesses, no solver in the artifact

The bracket is proved by two objects of different kinds, and the runner carries both.

**Sample points.** Pick one point in the interior of each piece orbit and carry it around
the box symmetry group. The group is the axiom's 24 proper cubic rotations acting on the
spatial coordinates about the box centre, together with the tick relabelling `t -> 2 - t`,
giving 48 distinct corner permutations. It is used for one purpose: to say a multiplier is
constant on an orbit. Nothing else in the argument uses symmetry.

The points are **generic by construction, not by luck**. For a sample point built with
weights `W` from the corners of a piece, the barycentric numerator is the `W`-combination
of the corners' barycentric numerators, so if every one of those integers is bounded by
`C` in absolute value and `W` is superincreasing past `C`, no combination can vanish and
no point can land on any piece boundary. Measured here: `C` is 6, and the weights are
built from a common base plus a superincreasing offset so they are also near-uniform,
spread 1.142857. The result is checked as well as constructed — boundary incidences 0 over
all 17280 pieces, 17472 distinct points, exactly 48 per orbit.

**The certificate.** A dissection covers each sample point exactly once and uses exactly
48 pieces. Let `BO[p]` count the sample points inside piece `p` and `BX[p]` be its
adjacency cost. If integers `u` (one per point orbit) and `Z` satisfy
`BO[p] . u + Z <= D * BX[p]` on **every** minimal piece, then summing over the 48 pieces
of any dissection gives `cost >= 48 (sum u + Z) / D`, because every point orbit carries
exactly 48 points. Reversing the inequality gives the matching upper bound. No symmetry
enters that step — the group only says the multipliers are constant on orbits, which is
what compresses the 17280 piece inequalities down to one row per orbit, 364 in all.

**Witnesses.** The bounds are met by exhibited dissections. Each is certified without a
solver: every piece has volume 1, the volumes sum to the box, and every pair of pieces is
shown interior-disjoint by an **exhibited separating integer normal**. Volume plus
pairwise interior-disjointness plus the correct total is a dissection, so the certificate
is self-contained; a candidate normal list never has to be complete, it only has to work
on the pair in front of it.

The runner contains no linear or integer programme. Solvers were used off-artifact to
search for the certificates; what ships is integer arithmetic verifying them.

## Results

The runner reports `TOTAL: PASS=49 FAIL=0`.

**The bracket.** Over all minimal-volume corner dissections of the two-tick box, the
adjacency cost is exactly `[216, 256]`.

- **Floor.** An integer certificate at denominator 2 with `sum u + Z = 9` gives
  `48 * 9 / 2 = 216.000000` on the nose. Least slack 0, with equality on 13392 of the
  17280 minimal pieces.
- **Ceiling.** An integer certificate at denominator 288 with `sum u + Z = 1536` gives
  `48 * 1536 / 288 = 256.000000` on the nose. Least slack 0, with equality on 6336 of the
  17280 minimal pieces.
- **Both ends attained.** The least-charge witness is 48 pieces of volume 1 with all
  1128 pairs carrying an exhibited separating normal, at cost 216. The greatest-charge
  witness is likewise 48 pieces, 1128 of 1128 pairs certified, at cost 256.
- **The one-tick values, measured here.** The same code path certifies a 24-piece one-tick
  dissection at cost 108 and another at cost 128, 276 of 276 pairs each. So
  `216 = 2 * 108` and `256 = 2 * 128` are both sides measured, not one side assumed.

**The bracket is not a counting artefact.** Per-piece adjacency cost ranges over `(3, 7)`
with spectrum `[(3, 432), (4, 2592), (5, 7488), (6, 4896), (7, 1872)]`, so counting alone
gives only `48 * 3 = 144` below and `48 * 7 = 336` above. The true bracket sits strictly
inside both.

**A denominator law the two ends obey.** Every one of the 364 point orbits carries exactly
48 points, so a certificate at denominator `D` has value `48 (sum u + Z) / D`. Reaching
216 exactly therefore needs an even denominator and reaching 256 exactly needs a
denominator divisible by 3. Both shipped certificates obey this, and because a certificate
is homogeneous — scaling `(u, Z, D)` by `k` gives the same inequality, the same value and
the same tight set — the law is a statement about the value, not about the particular
scale chosen here.

**The seam is visible in the census.** Tick-span charge ranges over `(0, 4)` with spectrum
`[(0, 5344), (1, 1744), (2, 4944), (3, 3040), (4, 2208)]`. The 5344 pieces of tick-span
charge zero are exactly the slab-confined ones — `5344 = 2 * 2672`, one copy per tick
slab — and the remaining 11936 cross the seam. The slab-confined adjacency spectrum
`[(3, 128), (4, 768), (5, 2304), (6, 1536), (7, 608)]` is exactly twice the one-tick
spectrum, as it must be. Seam-crossing pieces are not penalised into irrelevance: they
reach the same least adjacency charge 3 as the slab-confined ones. Both witnesses that
attain the bracket happen to have tick-span charge zero on every piece, so the bracket's
two ends are realised without straddling the seam even though straddling is allowed
throughout.

**Piece orbits.** Under the order-48 group the 17280 minimal pieces fall into 364 orbits,
6 of size 16 and 358 of size 48. Adjacency charge is constant on every orbit, and the
17280 membership rows carry 342 distinct values, so the certificate search faces one
inequality per orbit rather than one per piece.

## Independent cross-checks performed

These were run against the runner off-artifact; they are reported here because a bracket
this clean should not rest on one implementation.

- **The census re-derived independently.** Corner ordering rewritten from scratch and the
  pair counts done with explicit loops rather than array arithmetic: same 42504 subsets,
  same volume spectrum, same 17280 minimal pieces, same adjacency and tick-span spectra.
- **The witnesses re-scored independently**, reproducing 216, 256, 108 and 128.
- **Cover-once corroborated by random sampling.** For each two-tick witness, several
  thousand random rational points were classified; every point lying off every piece wall
  was covered exactly once, with a hard assertion rather than a tolerance. Points landing
  on a wall were separated out and counted, not silently absorbed.
- **The bracket reproduced on a second generic weight family.** Because the membership
  matrix depends on where inside each piece the sample point sits, a different weight
  family gives a genuinely different linear programme. A reserve family, superincreasing
  in a different base, again gives boundary incidences 0, rows constant on orbits, and a
  bracket of `[216.000000, 256.000000]`. This is an independent measurement of the
  theorem, not a re-check of the same certificate.
- **Both certificates are maximally tight.** Nudging any single one of the 364 multipliers
  in the direction that would help breaks the inequality on some piece — 364 of 364
  coordinates, for both floor and ceiling — and moving the constant term breaks it too.
  Value-preserving shifts were also tried, with a compensating change to the constant, and
  every one of them drove the least slack negative. There is no slack to recover.
- **The gates are wired to the data.** Corrupting one load-bearing constant in the runner
  at a time — either certificate's constant term, either denominator, or the stencil's
  tick step — turns the run red every time, while the unedited runner is green. A gate
  that cannot fail is not evidence.
- **Witness fragility.** Several hundred random single-corner edits of the two witnesses
  were tested; none of them still covers the box.

## Boundary and honest read

- `[216, 256]` is exact **for minimal-volume corner pieces**, the same class as cycle 725.
  It is not a bound over dissections in general, and any downstream use has to carry the
  piece class with it.
- The result is a statement about **two** ticks. Subadditivity gives a limiting cost per
  tick that exists and is at most 108, and this cycle shows the two-tick value sits on the
  stacking bound rather than below it. Whether every longer tick run does the same is open
  work, not a corollary of this one, and the ceiling side has no subadditivity argument at
  all.
- The spatial block is still a single lattice cell. Cycle 725's other open direction,
  larger spatial blocks, is untouched here.
- The adjacency charge weights spatial pairs and ignores tick separation. That is the
  axiom's own asymmetry, not a modelling choice, but it is the reason the answer can be
  extensive: the tick adds pieces without adding chargeable pairs. A framework that later
  gives the tick a weight of its own would be asking a different question, and the
  tick-span charge introduced here is the natural place to put one.
- A certificate is specific to its weight family, since the membership matrix depends on
  the sample points. Any single valid family proves the bound, so this is not a gap; it is
  why the reserve-family run counts as independent evidence rather than duplication.
- The two shipped certificates are carried at denominators 2 and 288. No claim is made
  that these are the smallest denominators that work.
- Nothing here derives a metric, a curvature, or a field equation. It fixes an exact
  combinatorial cost, now known to be extensive across a tick boundary, that the geometry
  lane's constructions have to pay.

## Artifacts

- Runner: `scripts/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04.py`
- Cold output:
  `outputs/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04_cold_2026-08-04.txt`
- Receipt:
  `outputs/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04_receipt_2026-08-04.json`

The runner reports `TOTAL: PASS=49 FAIL=0` in about 19 seconds. Related in-flight cycle
notes of this lane, cited for context and not as dependencies:
`PHYSICAL_ADJACENCY_ADMISSIBLE_ASSEMBLY_TRADE_CYCLE723_NOTE_2026-08-03`,
`PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03`,
`PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03`.
