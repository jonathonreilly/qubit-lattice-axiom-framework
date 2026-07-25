# L-shape local-gauge handoff rank baseline — 2026-07-25

Authority: none

Audit: unset

## Scope and result

This checkpoint starts the recurrent local-gauge retask without replacing the
failed finite transition by another claimed whole-patch compiler.  It
independently reconstructs the exact three-center L residual from the local
owner charts, classifies that residual as a quadratic form over `GF(2)`, and
executes its finite factorization through a returned Z2 loop scratch.  It then
holds the local-owner construction unchanged on chain, `2x2`, and `3x3`
center blocks and audits the proper-cubic edge-chart orbit.

The finite L residual is exactly compressible, but the compression is not yet
a recurrent plaquette law:

- all six center-owner orders miss exactly 178 quadratic pairs;
- every one of those six residuals has alternating `GF(2)` rank 10;
- the first order's 178-pair word factors exactly into five products of two
  linear occupation parities;
- one reusable, arbitrarily dirty loop M2 executes the five products with zero
  phase or return failures on all 46,570 `n<=2`/dirty-loop cases;
- the 56 distance-three terms alone have rank 6, hence three parity-product
  channels in this exact quadratic ansatz;
- the extracted five masks have maximum combined cell diameter 4 and were
  obtained from the finite target comparison, so they are not promoted as an
  elementary recurrent rule.

On all 4,560 two-mode addresses, the declared feature-word/role rule fixes the
qutrit at each occupied endpoint to `01`; this endpoint state occurs at both
required signs and is therefore insufficient. The runner does not construct
the extended L-patch qutrit histories, so full chart conditioning remains open.

The recurrent success contract therefore remains open.  Authority stays none,
audit stays unset, and there is no shared obstruction or axiom pressure.

## Independent reconstruction

The runner rebuilds the cell/edge geometry, two-cell seam specifications,
local owned target, source pullback, and global target comparison without
calling the source runner's corresponding helper functions.  It then compares
its census with commit `a8928b71aa`,
`frontier_two_star_fixed_register_local_executor_2026_07_25.py`.

Both routes give minimum and maximum 178 pairs across all six orders.  The
independent rows are:

| Owner order | Distance `0/1/2/3` | Rank |
|---|---|---:|
| `0,1,2` | `2,32,88,56` | 10 |
| `0,2,1` | `1,33,89,55` | 10 |
| `1,0,2` | `4,32,86,56` | 10 |
| `1,2,0` | `4,36,86,52` | 10 |
| `2,0,1` | `1,37,89,51` | 10 |
| `2,1,0` | `3,37,87,51` | 10 |

The separate whole-patch inversion correction remains 454 pairs with distance
census `0:48, 1:174, 2:176, 3:56`.  This agreement cross-checks both the
178-pair local-owner miss and the 56 distance-three diagnostic before any new
synthesis is attempted.

## Exact finite loop factorization

Represent a quadratic sign word by its symmetric zero-diagonal adjacency
matrix `A` over `GF(2)`.  The runner repeatedly extracts columns `a,b` with

`A = sum_k (a_k b_k^T + b_k a_k^T)`.

Each product of two linear parities contributes matrix rank at most two.
Therefore an alternating rank-10 form requires at least five such products,
and the emitted five-product reconstruction has symmetric-difference zero.
This is an exact lower bound only in the declared linear-parity-product
factor class; it is not a minimum substrate-content claim.

The five `(weight(a), weight(b), overlap)` rows are:

`(2,6,0), (2,24,0), (4,32,0), (26,26,12), (24,24,12)`.

For one channel, let `s` be the reusable loop bit, possibly dirty, and let
`A(n),B(n)` be its two occupation parities.  The word is

```text
CZ(s,B); s ^= A; CZ(s,B); s ^= A; Z on every a-intersect-b mode.
```

Its exponent is

`s B + (s+A) B + diagonal(a intersect b)`,

which equals the required off-diagonal quadratic product.  The initial `sB`
term cancels, so the loop M2 needs no initialization and returns exactly.  On
every vacuum, one-particle, and two-particle word, for both initial loop values,
the runner finds zero phase and work-return failures.  Deleting the first
echo, second use, parity compute, or parity uncompute is detected in 7,976,
9,392, 3,888, or 8,700 cases respectively.

This closes the algebraic finite L correction.  It does not yet route every
parity fan-in through a fixed elementary plaquette neighborhood, nor does it
derive the masks without the finite exterior target.

## Corner incidence and declared endpoint-qutrit classification

Every residual endpoint lies in the radius-one union of the three center
stars.  Classifying each endpoint by the bit mask of incident center stars and
by endpoint separation produces 17 nonempty incidence classes.  Thus the
residual is corner-supported, but not a single uniform endpoint class.

The feature qutrit has lawful words `0,1,2`. The runner compares all 4,560
two-mode address rows against the residual, not against a self-derived phase
formula. Under the declared feature-word/role rule, the qutrit at each occupied
endpoint is `01`: for a same-cell pair the carrier is sentinel, while for
separated particles every allowed carrier excludes the occupied mode. Thus the
occupied endpoint outer tag is one in zero address rows. Nevertheless 178
addresses require correction phase `-1` and 4,382 require `+1`. The declared
endpoint-state class has a real sign conflict, and incidence-only conditioning
also retains conflicts.

This is an analytic classification of mode addresses under the supplied local
rule. The runner does not construct extended L-patch qutrit rows or replay the
source/target paths with all chart tags. It establishes that occupied-endpoint
state alone cannot classify the sign; it does not close conditioning on the
full qutrit chart. Geometric address or additional loop/chart data remains a
live discriminator.

Swapping only the two same-color L owners changes the required correction by
eight pairs of rank two.  One local Z2 handoff bit is algebraically sufficient
to select between those two relative-order corrections.  That is a useful
local-gauge target, not yet a mutually consistent multi-plaquette schedule.

## Held scaling without refit

The same local-owner construction and diagnostic are run without parameter
refit:

| Fixture | Centers / cells / edges | Residual pairs | Rank / parity channels | Maximum distance |
|---|---:|---:|---:|---:|
| adjacent pair | `2 / 12 / 11` | 24 | `2 / 1` | 2 |
| three-center chain | `3 / 17 / 16` | 48 | `4 / 2` | 2 |
| three-center L | `3 / 16 / 16` | 178 | `10 / 5` | 3 |
| `2x2` centers | `4 / 20 / 20` | 250 | `16 / 8` | 3 |
| `3x3` centers | `9 / 39 / 42` | 942 | `36 / 18` | 4 |

This is exact evidence that the five extracted L channels do not themselves
constitute a held recurrent law.  Rank growth is not evidence that another
local gauge, a different encoding, or a plaquette recurrence cannot close.

## Proper-cubic chart discriminator

The isolated adjacent-center residual has 24 pairs and rank two.  Under the
four proper-cubic rotations that fix its `+x` edge, it produces four distinct
24-pair words; their symmetric differences from the selected base word are
`0,24,24,48`.  Consequently a scalar unoriented edge flag cannot represent
this chart transition.

The complete transported family is nevertheless consistent: it has a
24-word proper-cubic orbit, zero group-closure failures, and zero transported
word composition failures over all 576 ordered frame products.  The exact
positive statement is therefore that a transported chart family is
covariant.  At least a four-state axial chart, or equivalent incident
plaquette-loop data, is needed by this particular edge-word representation.
This is not called minimum physical content: another representation could
remove the stabilizer dependence.  No 59,941-row ambient matrices were rebuilt
per frame.

## Supplied structure and dependency effect

The probe supplies the finite exterior target as a comparison oracle, the
first-owner patch order in its diagnostic scaling rows, local star charts and
direction labels, and one reusable loop scratch M2.  It does not call that
patch order a recurrent law or the extracted masks target independent.

| Wall | Effect |
|---|---|
| `C_ref` | unchanged; chart orientation, owner order, and finite target remain supplied |
| `C_num` | unchanged; the diagnostic is restricted to the declared `n<=2` sector |
| `C_wrap` | unchanged; factor or owner order is not time or realized history |
| `C_int` | unchanged; this probe classifies only the stream sign correction |
| `C_local` | sharpened: exact rank/channel structure and dirty-loop implementation are constructed, while held recurrence and scalar-frame closure fail for this candidate |
| `C_source` | unchanged |

The result does not change global TOE maturity scores.  It advances the
operational/matter compiler search but produces no Record, causal time,
gravity/source, or Born/probability result.

## No-go-discipline N1-N8 gate

The current `origin/main` no-go-discipline skill was applied.  The narrow
linear-algebra statement—rank 10 requires five rank-two parity products—passes
as a theorem inside its explicitly declared ansatz.  Any claim that the
substrate requires five new physical registers, that no scalar-free compiler
exists, or that recurrence is impossible **fails** the gate and is not
shipped.

### N1 — alternative route enumeration

1. **Owner-order change — ATTEMPTED.** All six orders retain 178 pairs and rank
   10, so order alone does not lower the ansatz rank.
2. **Alternative parity basis/pivots — ATTEMPTED.** Exact Gaussian
   factorization reconstructs the word; matrix-rank subadditivity prevents
   fewer than five rank-two products regardless of pivot basis.
3. **Direct pair-CZ realization — ATTEMPTED.** The 178 literal terms work but
   use a different factor class and do not provide a smaller recurrent rule.
4. **Occupied-endpoint qutrit conditioning — ATTEMPTED.** Under the declared
   local rule, all 4,560 two-mode address rows have occupied word `01`, but
   split into 178 negative and 4,382 positive requirements. This endpoint
   state cannot split the residual. Extended L-patch qutrit-chart conditioning
   was not constructed and remains open.
5. **Local same-color order handoff — ATTEMPTED.** One Z2 bit closes the
   eight-pair/rank-two order swap, but it does not close the baseline rank-10
   target or held blocks.
6. **Transported multi-state chart, plaquette gauge, rephased encoding, BKSF
   even algebra, and staggered loop schedule — OPEN.** These materially change
   the object or terminal obligation and defeat any broader minimum/no-go
   claim.

### N2 — wall independence

`W_qutrit` is the unconstructed extended L-patch chart conditioning; `W_chart`
is the four-state axial stabilizer dependence of this edge word; `W_recur` is
failure to derive a fixed held plaquette recurrence. Full qutrit replay need
not solve chart transport or recurrence. Retiring a chart orientation does not
prove held recurrence, and a different recurrent encoding need not use this
edge chart. None implies another; no inflated wall count is used.

### N3 — hidden-wall scan

The code and note were scanned for the skill's assumption-euphemism list. The
finite target, patch order, local charts, qutrit alphabet, scratch register,
sector, and frame scope are all inventoried. The analytic endpoint rule and
absence of extended qutrit histories are explicit. “Exact” refers to
enumerated equalities or ranks, not full chart conditioning.

### N4 — residual matching

The source `a8928b71aa` residual matches exactly: same L cells/edges, all six
orders, and 178-pair extrema.  The 56 distance-three terms match the earlier
whole-transition extension.  Cycle-233's four-site plaquette repair and
Cycle-232's gauge construction concern different encodings and residuals;
they are live escape routes, not witnesses for this rank statement.

### N5 — resolution audit

The runner tests quadratic pair coefficients, all `n<=2` L inputs, one L
corner, one chain, `2x2` and `3x3` center blocks, and transported edge-word
geometry. It analytically classifies occupied endpoint qutrits but does not
construct the extended L-patch qutrit histories. It also does not test
arbitrary number, an infinite lattice, every encoding, or frame-by-frame
common-`E` matrices. Every negative phrase is restricted to the named finite
owner/chart construction.

### N6 — partial-closure paths

The four-state edge orbit can be carried by transported local chart data or
incident plaquette loops.  The rank-two same-color commutator can be handled by
one local Z2 bit.  A target-independent edge-plus-corner recurrence, a local
encoding rephase, BKSF-style loop constraints, or the staggered plaquette route
could close the residual constructively. Separately, an extended source/target
qutrit replay could test conditioning on all chart sites. None requires an
axiom edit.

### N7 — steelman

A hostile reviewer can replace the extracted five global masks by a local
edge-plus-corner cocycle: use one rank-two handoff on every adjacent center
pair, store the transverse chart in incident plaquette Z2 variables, and use
the rank-two same-color commutator to update a corner loop when two star owners
cross.  The terminal obligation is a fixed recurrence that reproduces the L,
`2x2`, and `3x3` targets with returned work and a 24/576 physical code action.
The exact adjacent, chain, and local-order ranks make this an actionable live
route.  Therefore the held growth is not a no-go.

### N8 — cross-cycle echo

The direct Route-A 240-column failure was already retired on the finite patch
by the gauge transition, demonstrating that exact route failures can disappear
under added local state.  Cycle 232 explicitly kept gauge/loop routes live;
Cycle 233 repaired its elementary exchange witness with a plaquette phase;
Cycle 563 retired another supplied ordering using bounded local correction
tables.  The applicable lesson is constructive retasking, not axiom pressure.

## Reproduction

With commits `a8928b71aa`, `efbc469453`, and their carrier dependencies on
`PYTHONPATH`, run:

```text
python3 scripts/frontier_l_shape_local_gauge_handoff_rank_probe_2026_07_25.py
```

The terminal marker is
`L_SHAPE_RANK10_FIVE_LOOP_CHANNELS_CLOSED_RECURRENT_HANDOFF_OPEN`.
