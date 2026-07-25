# Cycle 703 coframe edge/corner loop dictionary — 2026-07-25

Authority: none

Audit: unset

## Scope and disposition

This checkpoint tests the smallest coframe-transported dictionary suggested by
the recurrent L-shape handoff evidence.  It extracts one adjacent-center word
`H` and one right-angle corner associator `K`, transports both through an
explicit proper-cubic coframe, and holds their definitions and bounded color
schedule unchanged on the L, `2x2`, and `3x3` center fixtures.

The result is constructive on the training L and negative on the held blocks:

- `H` has 24 quadratic pairs, alternating `GF(2)` rank 2, and support-cell
  diameter 2;
- `K = R_L xor H_(+x) xor H_(+y)` has 154 pairs, rank 10, five
  parity-product channels, and support-cell diameter 4;
- two transported `H` terms plus one `K` reconstruct the 178-pair L residual
  exactly;
- with no refit, the same rule misses 72 pairs of rank 8 on `2x2` and 502
  pairs of rank 26 on `3x3`;
- even allowing an independent binary `K` coefficient at every right-angle
  center incidence leaves the square target outside the four-column span and
  the `3x3` target outside the sixteen-column span.

This falsifies the declared `H/K` dictionary, not local gauge compilation.
Both words were extracted from finite exterior targets, the periodic `L5`
color schedule fails its seam constraints, and no physical common-`E`
intertwiner was constructed.  There is no route-independent obstruction or
axiom pressure.

## Elementary transported words

Let `R_X` be the exact residual of two adjacent selected centers and `R_L` the
first-owner residual of centers `(0,0,0)`, `(1,0,0)`, and `(0,1,0)`.  The
runner defines

```text
H = R_X
K = R_L xor H_(+x) xor transport_(+x -> +y)(H).
```

The transport is not a scalar edge flag.  Every cell carries a supplied
24-state proper-cubic coframe.  For each local axial direction the runner
selects a canonical one of the four proper frames taking `+x` to that
direction; an edge carries the associated four-state chart.  A corner frame
is fixed by its two ordered local legs and their cross product.  Under a
physical frame `Q`, the cell coframe changes as `R -> Q R`, so local direction
labels and bounded color labels remain invariant.

The complete word and frame checks give:

- zero frame-group closure failures over 576 ordered products;
- zero `H` and `K` transported-word composition failures over those products;
- zero edge-frame covariance failures in 3,456 cases;
- zero corner-frame covariance failures in 6,912 cases;
- zero candidate rebuild failures on all 24 frames of each of the three
  fixtures.

These are site-word geometry tests.  No 59,941-row ambient common-`E` matrix
was rebuilt.  Naively recomputing the first-owner exterior target after a
frame rotation disagrees with direct word transport in 69 of 72 fixture-frame
cases because that diagnostic retains its fixed exterior-order gauge.  It is
reported as a scope discriminator, not called a physical covariance failure.

## Held no-refit test

The supplied schedule uses local coframe coordinates modulo three.  Its color
tuple is `(y mod 3, x mod 3, z mod 3)`, reproducing the training owner order
without a patch-length traversal.  Equal-color radius-one owner stars are
disjoint in the infinite lifted lattice.  Each selected-center adjacency gets
one `H`; each center earlier than two perpendicular selected neighbors gets
one transported `K`.

| Fixture | Target | `H` / fixed `K` terms | Candidate | Miss | Miss rank | Distance census |
|---|---:|---:|---:|---:|---:|---|
| three-center L | 178 | `2 / 1` | 178 | 0 | 0 | empty |
| `2x2` centers | 250 | `4 / 1` | 214 | 72 | 8 | `1:18, 2:36, 3:18` |
| `3x3` centers | 942 | `12 / 4` | 584 | 502 | 26 | `0:2, 1:54, 2:137, 3:198, 4:111` |

The stronger dictionary test removes the fixed corner selection and gives an
independent Z2 coefficient to every right-angle center incidence.  It
exhausts all binary assignments:

| Fixture | Corner columns | Dictionary / augmented rank | Assignments | Closest miss |
|---|---:|---:|---:|---:|
| L | 1 | `1 / 1` | 2 | 0 |
| `2x2` | 4 | `4 / 5` | 16 | 72 |
| `3x3` | 16 | `16 / 17` | 65,536 | 402 |

Thus the held targets are not in the span even after independent corner-bit
refitting.  The `3x3` closest assignment improves the fixed miss from 502 to
402, but cannot close it.  The next constructive rung is an elementary square
plaquette word `P`, not an impossibility claim.

## Local constraint boundary

The auxiliary code space is specified by bounded diagonal computational-basis
projectors:

1. exactly one of 24 coframe M2 bits per cell;
2. equality of neighboring coframes;
3. exactly one of four directed-edge chart M2 bits, equal to the local
   coframe/direction function;
4. exactly one of 27 color M2 bits per cell, with the neighboring color fixed
   by the local coframe direction.

The runner executes exact rank, truth, and deletion counts rather than merely
naming these constraints:

- the coframe one-hot projector has rank 24 in dimension `2^24` and rejects
  16,777,192 words;
- the edge-chart one-hot projector has rank 4 in dimension 16 and rejects 12
  words;
- the color one-hot projector has rank 27 in dimension `2^27` and rejects
  134,217,701 words;
- all 576 coframe-neighbor alphabet pairs give zero acceptance/rejection
  failures; deleting equality admits 552 mismatched pairs;
- all 576 coframe/direction/chart cases give zero failures; deleting chart
  consistency admits 432 wrong states;
- all 104,976 coframe/direction/two-color cases give zero failures; deleting
  color increment admits 101,088 wrong states;
- all 1,944 proper-frame/color/elementary-loop cases return the color exactly,
  while deleting one loop edge is detected in all 1,944 cases;
- 120 enumerated homogeneous-sector plaquette cases have identity coframe
  holonomy.

These are exact local diagonal projector predicates and code-alphabet truth
tables.  An autonomous penalty dynamics that generates or repairs the
coframe/color sector is not constructed.  Coframe and color genesis remain
supplied `C_ref` structure.

The register inventory is constant but deliberately generous: 24 coframe M2
bits and 27 color M2 bits per cell, four chart M2 bits per directed schedule
edge, and one returned dirty loop M2 reused sequentially for the finite parity
program.  This is not a minimal-content claim.

## Translation, periodicity, mass, and deletion controls

For every translation of the held `3x3` fixture on `L5` and `L6`, the runner
rebuilds the candidate from shifted centers and the shifted coframe/color
origin, then compares it with direct transport of the unshifted candidate.
All 125 `L5` and 216 `L6` rebuilt comparisons pass, with no wrapped support
collisions.

That finite lifted covariance does not solve periodic color holonomy.  A Z3
color must increment across each positive torus seam.  The declared coloring
has 75 seam violations per homogeneous sector on `L5` and zero on `L6`.
Therefore this schedule cannot be the requested size-independent physical
compiler for both sizes.  A fixed absolute origin is not claimed; the
supplied origin is transported with the fixture.

All correction terms are off-diagonal quadratic occupation pairs, so their
phase is exactly zero on vacuum and every one-particle basis state.  The
runner checks 450 one-particle addresses across the three fixtures with zero
failures.  This preserves the inherited one-particle mass fixture at the
level affected by this correction; the mass matrix itself was not rerun.

On the exact L, deleting either `H` term exposes 24 pairs of rank 2, and
deleting `K` exposes 154 pairs of rank 10.  The earlier dirty-loop truth test
supplies the returned-work implementation for each finite parity channel.
There is no physical common-`E` map here, so a physical code-space leakage norm
is not defined and is not reported as zero.  The endpoint-qutrit result is only
the earlier analytical 4,560-address comparison; extended-L `E_refresh`
histories and full surrounding chart conditioning remain open.

## Supplied structure and dependency effect

Supplied structure is explicit: the finite adjacent and L exterior targets
used to extract `H` and `K`; homogeneous coframe sector and genesis; bounded
27-color chart and transported origin; fixed 27-stage order; local
direction-mode labels; and the finite parity masks plus returned scratch.
There is no runtime patch-length traversal or global parity service, but the
target derivation still depends on a preferred finite exterior order.

| Wall | Effect |
|---|---|
| `C_ref` | sharpened, not retired: local coframe/color projectors and transported finite translations are exact, but genesis is supplied and `L5` periodic color holonomy fails |
| `C_num` | unchanged: the comparison remains in the declared vacuum/one-/two-particle sector |
| `C_wrap` | unchanged: color stages are not causal time or realized history |
| `C_int` | unchanged: only the CAR stream-sign correction is tested |
| `C_local` | sharpened: a bounded covariant `H/K` dictionary closes the L, but held span tests falsify it on square and `3x3` |
| `C_source` | unchanged |

No TOE maturity score changes.  This is an operational/matter compiler probe;
it constructs no Record, causal-time law, gravity/source rule, or Born
probability result.

## No-go-discipline N1-N8 gate

The current `origin/main` no-go-discipline instructions were applied.  The
exact claims are limited to the declared transported `H/K` dictionary and
listed finite fixtures.  Any inference of minimum substrate content,
impossibility of local CAR compilation, or axiom pressure fails the gate.

### N1 — alternative route enumeration

1. **Fixed transported `H/K` schedule — ATTEMPTED.** It closes the L and leaves
   exact held residuals 72/rank 8 and 502/rank 26.
2. **Independent corner Z2 bits — ATTEMPTED.** Exhaustive four- and sixteen-bit
   dictionaries have augmented rank one above dictionary rank and no exact
   held assignment.
3. **Proper-cubic coframe/chart transport — ATTEMPTED.** Word, frame, group,
   and fixture-candidate covariance checks pass; scalar unoriented transport
   was already falsified in the predecessor checkpoint.
4. **Bounded spatial color — ATTEMPTED.** Lifted finite translation passes, but
   Z3 holonomy fails on `L5`.
5. **Elementary square plaquette word `P` — OPEN/NEXT.** This adds a distinct
   two-dimensional cocycle channel and is not in the tested `K` span.
6. **Full surrounding qutrit/chart conditioning, encoding rephase, BKSF-style
   even algebra, independent edge gauge, and staggered autonomous clock —
   OPEN.** These change the dictionary or physical terminal obligation and
   defeat any broader no-go.

### N2 — wall independence

`W_dictionary` is the held failure of the extracted `H/K` span;
`W_periodic-color` is L5 Z3 holonomy; `W_common-E` is absence of a physical
intertwiner and leakage calculation; `W_genesis` is the supplied coframe/color
sector.  Solving any one does not logically solve the others.  They are not
collapsed into an inflated shared obstruction.

### N3 — hidden-wall scan

The target oracle, exterior order used during extraction, coframe sector,
color origin/stage convention, local direction labels, finite parity masks,
scratch, particle-number scope, covariance scope, and missing autonomous
constraint dynamics are inventoried.  “Exact” refers only to enumerated word
equalities, ranks, or projector truth tables.

### N4 — residual matching

The `H` source matches the predecessor adjacent fixture at 24 pairs/rank 2.
The `K` construction reproduces the predecessor 178-pair/rank-10 L target
exactly.  Applying the frozen rule to the predecessor square and `3x3` targets
gives the stated 72- and 502-pair residuals.  Earlier plaquette and gauge
engines concern different encodings and remain escape routes rather than
evidence for this failure.

### N5 — resolution audit

The runner tests quadratic site words in the vacuum/one-/two-particle sector,
three finite planar fixtures, all 24 proper frames, 576 frame products, local
projector alphabets, lifted L5/L6 translations, and periodic Z3 seam
constraints.  It does not test arbitrary number, infinite-volume recurrence,
an out-of-plane cube, physical common-`E` matrices, or autonomous constraint
dynamics.

### N6 — partial-closure paths

The L is exactly closed with bounded support and covariant transport.  `L6`
accepts the declared color holonomy.  A square word `P` can absorb the first
held quotient; another scheduler can remove the L5 Z3 obstruction; a rephased
encoding can change `H`, `K`, and the target quotient.  These are concrete
constructive continuations without axiom changes.

### N7 — steelman

A hostile reviewer should add one coframe-transported square plaquette word
equal to the `2x2` residual after `H/K`, apply it once per elementary
plaquette, and freeze `H/K/P` before testing `3x3` and an out-of-plane
corner/cube.  If the next residual is another bounded cell-complex coboundary,
the current failure is merely the missing two-cell rung.  This route is now
the immediate retask.

### N8 — cross-cycle echo

The direct finite common-`E` failure was retired by gauge correction, so a
dictionary failure cannot be promoted to constitutional evidence.  Earlier
bounded local correction and plaquette repairs likewise show that a new local
cell-complex rung can close an exact lower-rung miss.  The correct inference is
to test `P`, not to edit axioms.

## Reproduction

With the predecessor runner and its dependencies on `PYTHONPATH`, run:

```text
python3 scripts/frontier_cycle703_coframe_corner_loop_dictionary_2026_07_25.py
```

The terminal marker is
`CYCLE703_L_EXACT_SQUARE72_HELD502_HK_DICTIONARY_OPEN`.
