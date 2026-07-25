# Cycle 703 H/K/P plaquette quotient — 2026-07-25

Authority: none

Audit: unset

## Result

This checkpoint takes the exact square residual left by the frozen coframe
edge/corner dictionary and promotes it to one transported elementary
plaquette word `P`.  It then freezes `H`, `K`, and `P` on their adjacent, L,
and square training fixtures before testing `3x3`, an out-of-plane corner,
and a `2x2x2` cube without refit.

`P` closes the training square exactly but does not produce a held recurrent
law:

- `P` contains 72 quadratic pairs, has alternating `GF(2)` rank 8, four
  parity-product channels, and support-cell diameter 3;
- frozen `H/K/P` closes the adjacent pair, L, and `2x2` fixtures exactly;
- one `P` on each of the four elementary `3x3` plaquettes leaves 482 pairs of
  rank 24;
- all 16 independent subsets of those four transported `P` words fail, with
  dictionary/augmented ranks `4/5` and closest miss 364;
- one `P` on each of the six cube faces leaves 680 pairs of rank 48;
- all 64 independent cube-face subsets fail, with ranks `6/7` and closest miss
  668.

The constructive content is a bounded, covariant square repair.  The negative
content is limited to this target-derived `H/K/P` dictionary.  No physical
common-`E` map, leakage result, target-independent recurrence, shared
obstruction, or axiom pressure is claimed.

## Definition and exact local execution

With the preceding target-derived edge word `H` and corner word `K`, define

```text
P = R_(2x2) xor H/K candidate_(2x2).
```

Its distance census is `1:18, 2:36, 3:18`.  Factoring its alternating
quadratic matrix gives exactly four parity-product channels and reconstructs
all 72 pairs with symmetric-difference zero.  The predecessor's dirty-loop
echo is executed for these four new masks on 6,568 vacuum, one-particle,
two-particle, and dirty-scratch cases.  Phase and returned-work failures are
both zero.  One returned dirty loop M2 can therefore execute the finite `P`
program sequentially without a global parity service.

This is an implementation of the extracted finite word, not a derivation of
`P` from target-independent incidence or gauge constraints.  The masks remain
supplied finite data.

## Frozen training and held fixtures

The candidate applies `H` once per selected-center adjacency, `K` at every
scheduled earlier right-angle corner, and `P` once per elementary center
plaquette.  The coframe determines local positive axes and transports each
word.  The bounded 27-color schedule and origin are unchanged from the
preceding Cycle 703 checkpoint.

| Fixture | Target | `H/K/P` terms | Candidate | Miss / rank | Distance census |
|---|---:|---:|---:|---:|---|
| adjacent pair | 24 | `1/0/0` | 24 | `0/0` | empty |
| three-center L | 178 | `2/1/0` | 178 | `0/0` | empty |
| `2x2` centers | 250 | `4/1/1` | 250 | `0/0` | empty |
| `3x3` centers | 942 | `12/4/4` | 580 | `482/24` | `0:2, 1:42, 2:131, 3:196, 4:111` |
| `2x2x2` cube | 1,136 | `12/6/6` | 1,112 | `680/48` | `0:4, 1:64, 2:224, 3:288, 4:100` |

Adding all four square terms changes the fixed `3x3` miss from the H/K value
502/rank 26 to 482/rank 24.  The improvement is real but small.  Exhaustive
P-subset enumeration shows this is not merely the wrong choice of which
plaquettes fire: no subset closes, although the closest subset reaches 364
pairs.  On the cube, no face subset closes and the best of 64 leaves 668
pairs.

The exact quotient statements are only that the held residual vector is
outside the span of the four or six transported copies of this `P`.  They do
not exclude different plaquette words, multiple plaquette channels, a vertex
or cube term, encoding rephasing, or a different local gauge algebra.

## Proper-cubic and out-of-plane audit

The transported `P` family has zero composition failures over all 576 ordered
proper-cubic frame products.  Plaquette frames have zero covariance failures
in 1,728 coframe/plane/physical-frame cases.  Rebuilding the complete H/K/P
candidate on all 24 frames of the square, `3x3`, and cube gives zero failures
in 72 fixture-frame cases.

The out-of-plane corner isolates an important boundary.  Rotating the training
L from the x-y plane into the x-z plane and transporting both its coframe and
target gives zero H/K/P mismatch.  Separately recomputing the first-owner
target with the repository's fixed exterior order produces 210 rather than
178 pairs; the transported candidate then differs by 150 pairs of rank 14.
Using the wrong identity coframe instead gives a different 124-pair/rank-10
miss.

Thus geometric word transport is covariant, while the preferred exterior
target gauge has no compiled physical frame action in this probe.  The
150-pair discriminator is not called a violation of physical cubic symmetry,
because the physical common-`E` representation was not constructed.

## Deletion, mass, constraints, and lawful domain

Deleting the sole `P` from the exact square exposes exactly 72 pairs of rank
8.  Deleting one of the four `3x3` `P` terms leaves respectively
`426/20`, `528/26`, `420/22`, or `534/26` pairs/rank.  Every cube-face deletion
also changes the held residual, yielding 674–742 pairs and rank 48 or 50.

All H/K/P additions are off-diagonal quadratic occupation phases.  They are
therefore identity on vacuum and every one-particle basis state and preserve
the inherited one-particle mass fixture in the affected sector.  No mass
matrix was independently rerun.

The local coframe, chart, and color code space is inherited from the preceding
Cycle 703 H/K checkpoint, where exact diagonal-projector ranks, exhaustive
local alphabet truth tables, deletion complements, 1,944 color-loop tests,
and all 341 rebuilt L5/L6 finite translations were executed.  The L5 periodic
Z3 seam failure remains.  This runner adds `P` but does not construct an
autonomous color clock or constraint-penalty dynamics.

The lawful occupation scope remains vacuum plus one- and two-particle sign
words.  No physical common-`E` is built, so physical code-space leakage is
undefined rather than zero.  The endpoint qutrit remains bounded by the prior
analytical address result; no extended patch refresh histories are added.

## Supplied structure and dependency effect

The adjacent, L, and square exterior targets; extracted H/K/P masks;
homogeneous coframe sector; 27-color chart and origin; stage convention; and
direction-mode labels are supplied.  There is no patch-length runtime
traversal, but target extraction still uses the preferred finite exterior
order and is not a physical-site compiler.

| Wall | Effect |
|---|---|
| `C_ref` | unchanged from the preceding checkpoint: coframe/color transport is local, but genesis is supplied, L5 color holonomy fails, and exterior-order frame action is uncompiled |
| `C_num` | unchanged: the result is restricted to the declared `n<=2` sign sector |
| `C_wrap` | unchanged: color stages are not causal time or realized history |
| `C_int` | unchanged: only the CAR stream-sign correction is tested |
| `C_local` | sharpened: one bounded square cell closes `2x2`, but exact held `3x3` and cube quotients lie outside the transported one-P-per-cell span |
| `C_source` | unchanged |

No global TOE maturity score changes.  This checkpoint advances only the
operational/matter compiler search and constructs no Record, causal-time law,
gravity/source rule, or Born/probability result.

## No-go-discipline N1-N8 gate

The current `origin/main` no-go-discipline instructions were applied.  The
rank and span statements pass only for the named finite H/K/P dictionary.  A
claim that local CAR compilation is impossible, that a particular minimum
auxiliary content is necessary, or that axioms must change fails the gate.

### N1 — alternative route enumeration

1. **One frozen `P` per plaquette — ATTEMPTED.** It closes `2x2` and leaves
   exact held residuals 482/rank 24 and 680/rank 48.
2. **Independent plaquette firing bits — ATTEMPTED.** All 16 square-block and
   64 cube-face subsets were exhausted; neither held target is in the P span.
3. **Out-of-plane coframe transport — ATTEMPTED.** It exactly closes the
   transported corner target and isolates the uncompiled exterior-order gauge.
4. **Additional plaquette channels or orientation-dependent P families —
   OPEN.** The present dictionary contains only one P orbit.
5. **Vertex/cube associator or target-independent cell-complex coboundary —
   OPEN.** These add a different rung rather than another coefficient on P.
6. **Full surrounding qutrit/chart law, encoding rephase, even-bond gauge
   algebra, and autonomous staggered schedule — OPEN.** These materially
   change the object and defeat any broader no-go claim.

### N2 — wall independence

`W_P-span` is failure of one target-derived P orbit on held blocks;
`W_exterior-frame` is the missing physical action of the exterior-order gauge;
`W_periodic-color` is the inherited L5 holonomy; and `W_common-E` is absence of
the physical intertwiner/leakage test.  None implies another, and none is
treated as a shared substrate obstruction.

### N3 — hidden-wall scan

The three finite target oracles, preferred exterior order used during
extraction, H/K/P masks, coframe sector, color origin/stages, local mode
labels, scratch, particle sector, frame scope, inherited periodic failure, and
missing common-E/autonomous constraint dynamics are explicit.  “Exact” refers
only to the enumerated word, rank, factorization, and span results.

### N4 — residual matching

H and K reproduce the predecessor adjacent and L targets.  Their frozen square
miss is exactly the 72-pair/rank-8 P extracted here, and H/K/P closes that
square with zero symmetric difference.  The held comparisons use the same
owner target constructor and no parameter refit.  Other encodings and earlier
plaquette mechanisms are escape routes, not witnesses for this dictionary.

### N5 — resolution audit

The runner covers quadratic site words in the declared `n<=2` sector,
adjacent/L/square training cells, `3x3`, one x-z corner, one cube, 24 frames,
576 products, four P bits, and six P bits.  It does not cover arbitrary
particle number, all patch shapes, infinite recurrence, a physical common-E
matrix, full endpoint refresh histories, or autonomous constraint dynamics.

### N6 — partial-closure paths

The square and covariantly transported out-of-plane L are exact.  P reduces
the fixed `3x3` rank from 26 to 24.  A second independent plaquette channel,
vertex/cube associator, or target-independent gauge coboundary can address the
new quotient.  A different periodic scheduler can separately address L5.
None requires axiom changes.

### N7 — steelman

A hostile reviewer should stop extending a lookup hierarchy blindly and use
the H/K/P residuals as equations for a target-independent local incidence
law.  One route is to introduce explicit edge and face gauge generators with
Gauss/flatness projectors, solve their local commutation signs on the adjacent,
L, and square fixtures, and then predict rather than fit `3x3` and cube.  A
second route is a distinct cube/vertex associator tested simultaneously on
planar and out-of-plane held shapes.  Both remain live.

### N8 — cross-cycle echo

The earlier direct common-E failure was retired by a gauge correction, and the
H/K square failure here was partly retired by P.  These precedents show why a
failure of one cell-complex truncation is route-specific.  The correct next
move is a target-independent incidence/gauge derivation or a genuinely new
local channel, not constitutional escalation.

## Reproduction

With the Cycle 703 H/K runner and its dependencies on `PYTHONPATH`, run:

```text
python3 scripts/frontier_cycle703_hkp_plaquette_quotient_2026_07_25.py
```

The terminal marker is
`CYCLE703_HKP_CLOSES_SQUARE_HELD_3X3_482_CUBE_680`.
