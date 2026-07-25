# Cycle 703 two-frame colored rephase — 2026-07-25

Authority: none

Audit: unset

## Scope and result

The preceding checkpoint proved that one static diagonal phase on the same
occupation register cannot reproduce the local-owner residual.  This
checkpoint tests the nearest escape: distinct bounded input and output phases,

```text
r(n) = f_in(n) xor f_out(S n),
```

using a supplied 27-color coframe chart and target-independent geometric pair
bases.  It solves on adjacent, L, and `2x2` training fixtures, selects one
canonical free-zero coefficient vector, freezes it, and evaluates `3x3` and a
`2x2x2` cube.

There is a real training construction but no held law:

- the taxi-distance-at-most-two colored basis is exactly training-consistent;
- its canonical solution uses 110 input-phase and 170 output-phase pair
  monomials and closes all 14,256 training equations;
- held `3x3` misses 714 pairs of rank 42;
- held cube misses 906 pairs of rank 54;
- those failures cannot be removed merely by choosing different free
  coefficients while retaining the same training fit: 251 `3x3` and 224 cube
  target bits are already contradicted by equations fixed by the training row
  space.

This falsifies the declared colored two-frame/taxi-two basis.  It does not
falsify longer-range, different-color, auxiliary-updated, non-diagonal, or
local-Gauss encodings.  The fitted 280 coefficients are not called a
target-independent law, and there is no shared obstruction or axiom pressure.

## Basis tournament

For each unordered pair of occupation modes, the basis records:

- the first cell's bounded color `(y mod 3, x mod 3, z mod 3)`;
- cell displacement in the local proper-cubic coframe;
- the two local direction-mode labels;
- identification with the reversed pair representation.

This feature grammar is generated before the residual is read.  `f_in` and
`f_out` have independent coefficients on the same basis.  Across the adjacent,
L, and square training fixtures:

| Colored basis | Keys per phase / total coefficients | Coefficient rank | Augmented rank | Disposition |
|---|---:|---:|---:|---|
| onsite-edge | `3,321 / 6,642` | 2,069 | 2,070 | inconsistent |
| onsite-edge-face | `9,153 / 18,306` | 4,135 | 4,136 | inconsistent |
| onsite-edge-two-step | `12,069 / 24,138` | 4,701 | 4,701 | consistent |
| elementary-cube | `13,041 / 26,082` | 4,935 | 4,936 | inconsistent |

The fact that the cube neighborhood fails while taxi-two succeeds identifies
the collinear distance-two features as load bearing; body diagonals do not
replace them in this basis.

The chosen system has 19,437 free coefficients.  To avoid post-hoc held
selection, the runner fixes a deterministic solution: lexicographically sort
columns, eliminate with the highest available pivot, and set every free
coefficient to zero.  The resulting active index inventory has SHA-256
`af7fb13638f0e64baa952c21cff5b56d56f5486adc328edbf3629bc2c18b38f1`.
It has 110 active `f_in` and 170 active `f_out` coefficients and reproduces
24, 178, and 250 training pairs with zero mismatch.

The feature basis is target independent.  The selected coefficients are not:
they are solved from the three residual right-hand sides, and their predictive
status is determined only by held tests.

## Held prediction and solution-family audit

The canonical frozen solution gives:

| Held fixture | Target / predicted pairs | Mismatch / rank | Equations fixed by training | Underdetermined equations | Fixed target conflicts |
|---|---:|---:|---:|---:|---:|
| `3x3` centers | `942 / 288` | `714 / 42` | 20,020 | 7,241 | 251 |
| `2x2x2` cube | `1,136 / 250` | `906 / 54` | 13,041 | 5,295 | 224 |

The canonical errors alone could have been blamed on the free-zero selector.
The row-space audit prevents that mistake.  A held equation whose coefficient
row lies in the training row span has the same predicted value for every
training solution.  Among those fixed equations, 251 and 224 require the
opposite target bit.  Therefore no coefficient vector in the full training
solution affine space closes either held fixture.

The equivalent combined-system ranks are:

| System | Equations | Coefficient / augmented rank |
|---|---:|---:|
| training | 14,256 | `4,701 / 4,701` |
| training + `3x3` | 41,517 | `11,188 / 11,189` |
| training + cube | 32,592 | `9,210 / 9,211` |
| training + both held | 59,853 | `14,442 / 14,443` |

These are exact failures of one finite colored feature class, not a general
two-frame cohomology obstruction.

## Bounded realization, covariance, translation, and deletion

The active solution has 182 distinct geometric keys because some keys occur in
both frame phases.  Transporting those keys with the coframe gives:

- zero failures in 4,368 active-key/frame cases;
- zero failures in 104,832 active-key/ordered-frame-product cases;
- zero failures in 62,062 active-key translations over all L5 and L6 finite
  shifts with the color origin transported.

All 24 proper-cubic frames and 576 products are covered.  These are local
feature/candidate checks, not ambient common-`E` matrix covariance.

Every chosen pair has taxi distance at most two.  An offsite CZ is implemented
by a coframe-axis SWAP path to adjacency, CZ, and the reversed path.  Maximum
cost is two SWAPs out and back, with zero adjacency and returned-routing
failures.  Onsite terms use bounded intra-cell CZ.  Deleting each of the 280
active coefficients is detected on training; one deletion creates between one
and three pair failures.

The 27-color origin is transported with each lifted finite fixture.  The
inherited full-torus result remains: the Z3 schedule violates 75 positive seam
constraints per sector on L5 and closes them on L6.  No autonomous two-frame
clock or L5-compatible periodic scheduler is constructed.
No schedule counter is physical time.

Both phases are quadratic, hence identity on vacuum and one-particle states.
The inherited one-particle mass fixture is preserved at the affected level.
No physical common-`E` map exists here, so physical leakage is undefined.

## Supplied structure and dependency effect

Supplied structure includes the bounded coframe and 27-color chart/origin,
separate input/output phase slots, the three training residual right-hand
sides, and the canonical free-zero selector.  The solution has no runtime
exterior-order query, but its 280 active entries were learned from targets and
are not a derived local law.

| Wall | Effect |
|---|---|
| `C_ref` | unchanged: active features transport covariantly, but color/coframe genesis is supplied and L5 periodic color holonomy fails |
| `C_num` | unchanged: training and prediction remain in the declared `n<=2` sign sector |
| `C_wrap` | unchanged: two frame phases and color stages are not causal time or realized history |
| `C_int` | unchanged: only the stream-sign residual is fitted |
| `C_local` | sharpened: a bounded two-frame colored fit exists on adjacent/L/square, but exact row-space conflicts falsify held transfer in this basis |
| `C_source` | unchanged |

No global TOE maturity score changes.  No Record, time law, gravity/source
rule, or Born/probability result is constructed.

## No-go-discipline N1-N8 gate

The current `origin/main` no-go-discipline instructions were applied.  The
negative conclusion is limited to the named colored two-frame feature basis.
Any inference of a general two-frame impossibility, minimum substrate content,
shared obstruction, or axiom pressure fails the gate.

### N1 — alternative route enumeration

1. **Colored onsite-edge — ATTEMPTED.** Training rank `2069/2070`; no fit.
2. **Add face diagonals — ATTEMPTED.** Rank `4135/4136`; no fit.
3. **Add collinear two-step features — ATTEMPTED.** Rank `4701/4701`; exact
   training fit, then held canonical misses 714/rank 42 and 906/rank 54.
4. **Choose different free coefficients — EXHAUSTED ALGEBRAICALLY for held
   closure.** Training row-space implications force 251 and 224 wrong held
   bits, and both combined systems are inconsistent.
5. **Replace collinear features by full unit-cube diagonals — ATTEMPTED.** Rank
   `4935/4936`; no training fit.
6. **Larger-radius colored bases, a different chart period, an auxiliary frame
   bit or multiple local gauge states, or a learned recurrence among
   coefficients — OPEN.** These change the ansatz.
7. **Auxiliary-updated, non-diagonal, and local-Gauss encodings — OPEN.** They
   change the phase equation or representation and escape this result.

### N2 — wall independence

`W_two-frame-basis` is held inconsistency of this taxi-two colored feature
space; `W_periodic-color` is the separate L5 seam failure; `W_clock` is absence
of autonomous phase-slot control; and `W_common-E` is absence of a physical
intertwiner/leakage test.  Closing one does not close the others, and their
count is not inflated into a shared obstruction.

### N3 — hidden-wall scan

The color/coframe origin, two phase slots, feature support, training RHS,
free-zero selector, active coefficient provenance, held shapes, covariance
scope, routing program, periodic seam failure, and missing clock/common-E are
explicit.  “Target-independent” qualifies the feature grammar only, not the
fitted coefficient vector.

### N4 — residual matching

Training residual counts 24, 178, and 250 match the predecessor exactly; the
canonical solution reproduces all three with zero difference.  Held targets
942 and 1,136 use the same constructor and no coefficient refit.  The
row-space and combined-rank audits independently establish that the held miss
is not a poor free-variable choice.  H/K/P and local-Gauss results are distinct
routes.

### N5 — resolution audit

The runner tests all pair equations on three training and two held fixtures,
four colored geometric bases, the complete training solution affine space as
it constrains held rows, all active-key 24/576 transports, every L5/L6 finite
translation, local CZ routing, and active-coefficient deletion.  It does not
test support beyond taxi two for the consistent basis, other color systems,
arbitrary number, auxiliary dynamics, non-diagonal encodings, or common-E
matrices.

### N6 — partial-closure paths

The route retires the same-register orbit condition on training: distinct
input/output phases plus collinear two-step colored features fit exactly with
bounded gates.  A more structured coefficient recurrence, larger bounded
neighborhood, locally updated gauge label, or different periodic scheduler can
change held implications.  The local-Gauss route can avoid target-fitted phase
tables altogether.

### N7 — steelman

A hostile reviewer should demand a small target-independent rule generating
the 280 active coefficients from local incidence/Gauss data, not another basis
expansion.  Such a rule must reproduce training, predict the 251 and 224
currently forced-wrong held bits, route with returned work, and eliminate the
L5 color holonomy or replace that scheduler.  This sets a concrete terminal
obligation for the next constructive route.

### N8 — cross-cycle echo

The same-register diagonal obstruction disappeared on training when the phase
slots and bounded color were enlarged, confirming that it was route-specific.
The new held failure likewise cannot be promoted beyond its feature space.
Earlier gauge and plaquette repairs support the same lesson: retask to a new
local representation, not axioms.

## Reproduction

With the Cycle 703 rephase runner and dependencies on `PYTHONPATH`, run:

```text
python3 scripts/frontier_cycle703_two_frame_colored_rephase_2026_07_25.py
```

The terminal marker is
`CYCLE703_TWO_FRAME_TRAIN_EXACT_HELD_714_906_FORCED_CONFLICTS_251_224`.
The content-pinned output cache is
`logs/runner-cache/frontier_cycle703_two_frame_colored_rephase_2026_07_25.txt`.
